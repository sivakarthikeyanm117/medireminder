# 🤖 Telegram Bot Setup - Quick Guide

## 🚀 **Quick Start (2 minutes):**

### **Step 1: Start the Bot**
```bash
python start_bot.py
```

### **Step 2: Test the Bot**
1. **Open Telegram** on your phone
2. **Search for your bot** (the name you gave it)
3. **Send** `/start`
4. **You should get a welcome message!**

## 📱 **Bot Commands:**

- `/start` - Welcome message
- `/add Paracetamol 500mg 2024-01-15 10:00` - Add reminder
- `/list` - View your reminders
- `/help` - Get help

## 🔧 **If Bot Doesn't Work:**

### **Check 1: Bot Token**
- Make sure your bot token is correct
- Bot should be created on @BotFather

### **Check 2: Internet Connection**
- Bot needs internet to work
- Check if Telegram is accessible

### **Check 3: Dependencies**
```bash
pip install python-telegram-bot==20.7
```

## 🎯 **For Your Web App:**

Once the bot is running:
1. **Open your web app** (`index.html`)
2. **Click "📲 Setup Telegram"**
3. **Follow the 3 steps**
4. **Add a reminder**
5. **Check Telegram** - you should get the message!

## 🏆 **Success Indicators:**

✅ Bot responds to `/start`
✅ Bot shows welcome message
✅ Bot accepts `/add` commands
✅ No error messages in console
✅ Bot appears online in Telegram

## 🆘 **Troubleshooting:**

- **"Module not found"** → Run `pip install python-telegram-bot==20.7`
- **"Bot token invalid"** → Check your token on @BotFather
- **"Connection error"** → Check internet connection
- **"Bot not responding"** → Make sure bot is running

**Your bot is now ready! Test it with `/start` command! 🎉**
