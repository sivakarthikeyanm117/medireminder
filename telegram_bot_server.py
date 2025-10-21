#!/usr/bin/env python3
"""
Simple Telegram Bot Server for MediRemainder
This bot handles medication reminders with simple commands
"""

import asyncio
import json
import logging
from datetime import datetime
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Bot configuration
BOT_TOKEN = "8383719479:AAH_Utq0CT_tUUx7cEE6V2kupMC8mZB-x2M"

# Simple storage
reminders = []

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /start command"""
    user = update.effective_user
    
    welcome_message = f"""🏥 *Welcome to MediRemainder Bot!*

Hello {user.first_name}! 👋

I'm here to help you never miss your medication again.

📋 *Available Commands:*
/start - Show this welcome message
/add - Add a new medication reminder
/list - View your reminders
/help - Get help

💊 *Quick Start:*
Use /add to create your first reminder!"""
    
    keyboard = [
        [InlineKeyboardButton("➕ Add Reminder", callback_data="add_reminder")],
        [InlineKeyboardButton("📋 My Reminders", callback_data="list_reminders")],
        [InlineKeyboardButton("❓ Help", callback_data="help")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        welcome_message, 
        parse_mode='Markdown',
        reply_markup=reply_markup
    )
    logger.info(f"User {user.id} started the bot")

async def add_reminder_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /add command"""
    if len(context.args) < 4:
        await update.message.reply_text(
            "📝 *Add Medication Reminder*\n\n"
            "Usage: /add <medication_name> <dose> <date> <time>\n\n"
            "Example: /add Paracetamol 500mg 2024-01-15 10:00\n\n"
            "📅 Date format: YYYY-MM-DD\n"
            "⏰ Time format: HH:MM (24-hour)",
            parse_mode='Markdown'
        )
        return
    
    try:
        medication = context.args[0]
        dose = context.args[1]
        date_str = context.args[2]
        time_str = context.args[3]
        
        # Create reminder
        reminder = {
            "id": len(reminders) + 1,
            "user_id": update.effective_user.id,
            "medication": medication,
            "dose": dose,
            "date": date_str,
            "time": time_str,
            "created_at": datetime.now().isoformat()
        }
        
        reminders.append(reminder)
        
        await update.message.reply_text(
            f"✅ *Reminder Added Successfully!*\n\n"
            f"💊 Medication: {medication}\n"
            f"💉 Dose: {dose}\n"
            f"📅 Date: {date_str}\n"
            f"⏰ Time: {time_str}\n\n"
            f"I'll remind you when it's time! 🏥",
            parse_mode='Markdown'
        )
        
        logger.info(f"Reminder added: {medication} for user {update.effective_user.id}")
        
    except Exception as e:
        await update.message.reply_text(
            f"❌ Error adding reminder: {str(e)}\n\n"
            "Please check your input format and try again."
        )
        logger.error(f"Error adding reminder: {e}")

async def list_reminders_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /list command"""
    user_id = update.effective_user.id
    user_reminders = [r for r in reminders if r["user_id"] == user_id]
    
    if not user_reminders:
        await update.message.reply_text("📋 You don't have any reminders yet.\n\nUse /add to create your first reminder!")
        return
    
    message = "📋 *Your Reminders:*\n\n"
    for i, reminder in enumerate(user_reminders, 1):
        message += f"{i}. 💊 *{reminder['medication']}*\n"
        message += f"   💉 Dose: {reminder['dose']}\n"
        message += f"   📅 Date: {reminder['date']}\n"
        message += f"   ⏰ Time: {reminder['time']}\n\n"
    
    await update.message.reply_text(message, parse_mode='Markdown')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /help command"""
    help_text = """🆘 *MediRemainder Bot Help*

📋 *Available Commands:*
/start - Welcome message
/add - Add a new medication reminder
/list - View your reminders
/help - Show this help message

💊 *Adding Reminders:*
Use: /add <medication> <dose> <date> <time>
Example: /add Paracetamol 500mg 2024-01-15 10:00

📅 *Date Format:* YYYY-MM-DD
⏰ *Time Format:* HH:MM (24-hour)

🔄 *How It Works:*
1. Add your medication reminders
2. I'll send you notifications at the scheduled time
3. You can view your reminders anytime

💡 *Tips:*
• Set reminders for regular medications
• Include dosage information
• Use 24-hour time format

Need more help? Contact support! 🏥"""
    
    await update.message.reply_text(help_text, parse_mode='Markdown')

async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle button callbacks"""
    query = update.callback_query
    await query.answer()
    
    if query.data == "add_reminder":
        await query.edit_message_text(
            "📝 *Add Medication Reminder*\n\n"
            "Use: /add <medication> <dose> <date> <time>\n\n"
            "Example: /add Paracetamol 500mg 2024-01-15 10:00",
            parse_mode='Markdown'
        )
    elif query.data == "list_reminders":
        await list_reminders_command(update, context)
    elif query.data == "help":
        await help_command(update, context)

async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle errors"""
    logger.error(f"Update {update} caused error {context.error}")
    if update and update.effective_message:
        await update.effective_message.reply_text(
            "❌ Sorry, something went wrong. Please try again later."
        )

def main():
    """Main function to run the bot"""
    print("🤖 Starting MediRemainder Telegram Bot...")
    print(f"Bot Token: {BOT_TOKEN[:10]}...")
    
    try:
        # Create application
        application = Application.builder().token(BOT_TOKEN).build()
        
        # Add handlers
        application.add_handler(CommandHandler("start", start_command))
        application.add_handler(CommandHandler("add", add_reminder_command))
        application.add_handler(CommandHandler("list", list_reminders_command))
        application.add_handler(CommandHandler("help", help_command))
        application.add_handler(CallbackQueryHandler(button_callback))
        
        # Add error handler
        application.add_error_handler(error_handler)
        
        print("✅ Bot handlers registered")
        print("🚀 Starting bot polling...")
        print("💡 Find your bot on Telegram and send /start")
        
        # Start bot
        application.run_polling()
        
    except Exception as e:
        print(f"❌ Error starting bot: {e}")
        print("\nTroubleshooting steps:")
        print("1. Check your internet connection")
        print("2. Verify the bot token is correct")
        print("3. Make sure python-telegram-bot is installed")
        print("4. Try running: pip install python-telegram-bot==20.7")

if __name__ == "__main__":
    main()
