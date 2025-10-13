#!/usr/bin/env python3
"""
MediRemainder WhatsApp Integration
This script handles WhatsApp notifications for medication reminders
"""

import pywhatkit as pwk
import json
import time
from datetime import datetime, timedelta
import os

def send_whatsapp_reminder(phone_number, medication, dose, date, time_str):
    """
    Send WhatsApp reminder for medication
    
    Args:
        phone_number (str): Phone number with country code (e.g., +1234567890)
        medication (str): Name of medication
        dose (str): Dosage information
        date (str): Date of reminder
        time_str (str): Time of reminder
    """
    try:
        # Clean phone number
        clean_phone = phone_number.replace('+', '').replace(' ', '').replace('-', '')
        
        # Create message
        message = f"""💊 *Medication Reminder*

Time to take: *{medication}*
Dosage: *{dose}*
Date: *{date}*
Time: *{time_str}*

Stay healthy! 🏥"""
        
        # Get current time
        now = datetime.now()
        
        # Parse reminder time
        reminder_datetime = datetime.strptime(f"{date} {time_str}", "%Y-%m-%d %H:%M")
        
        # Calculate delay in seconds
        delay_seconds = (reminder_datetime - now).total_seconds()
        
        if delay_seconds > 0:
            print(f"Scheduling WhatsApp message for {reminder_datetime}")
            print(f"Message will be sent in {delay_seconds/60:.1f} minutes")
            
            # Schedule the message with better parameters
            pwk.sendwhatmsg(clean_phone, message, reminder_datetime.hour, reminder_datetime.minute, wait_time=10, tab_close=False, close_time=5)
            
            print(f"WhatsApp reminder scheduled successfully for {medication}")
            return True
        else:
            print("Reminder time has already passed!")
            return False
            
    except Exception as e:
        print(f"Error sending WhatsApp reminder: {str(e)}")
        return False

def process_reminders_from_file():
    """
    Process reminders from a JSON file
    """
    try:
        # Read reminders from file (you can create this file from your web app)
        with open('reminders.json', 'r') as f:
            reminders = json.load(f)
        
        for reminder in reminders:
            if reminder.get('notificationType') in ['whatsapp', 'both']:
                send_whatsapp_reminder(
                    reminder['phone'],
                    reminder['medication'],
                    reminder['dose'],
                    reminder['date'],
                    reminder['time']
                )
                
    except FileNotFoundError:
        print("No reminders.json file found. Create one with your reminders.")
    except Exception as e:
        print(f"Error processing reminders: {str(e)}")

def create_sample_reminder():
    """
    Create a sample reminder for testing
    """
    sample_reminder = {
        "id": 1234567890,
        "medication": "Paracetamol",
        "dose": "500mg",
        "date": "2024-01-15",
        "time": "10:00",
        "phone": "+1234567890",
        "notificationType": "whatsapp"
    }
    
    with open('reminders.json', 'w') as f:
        json.dump([sample_reminder], f, indent=2)
    
    print("Sample reminder created in reminders.json")
    print("Edit the file with your actual phone number and reminder details")

if __name__ == "__main__":
    print("MediRemainder WhatsApp Integration")
    print("=" * 40)
    
    # Check if pywhatkit is installed
    try:
        import pywhatkit
        print("✅ pywhatkit is installed")
    except ImportError:
        print("❌ pywhatkit not found. Install it with: pip install pywhatkit")
        exit(1)
    
    # Create sample reminder file if it doesn't exist
    if not os.path.exists('reminders.json'):
        create_sample_reminder()
        print("\n📝 Created sample reminders.json file")
        print("Edit the file with your details and run again")
    else:
        print("\n🔄 Processing reminders from reminders.json")
        process_reminders_from_file()
    
    print("\n📱 Make sure WhatsApp Web is logged in and ready!")
    print("💡 The script will open WhatsApp Web automatically")
