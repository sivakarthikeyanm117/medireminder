#!/usr/bin/env python3
"""
Simple WhatsApp Reminder - Easy to understand version
"""

import pywhatkit as pwk
import json
from datetime import datetime

def send_reminder():
    """
    Simple function to send a WhatsApp reminder
    """
    print("=== Simple WhatsApp Reminder ===")
    
    # Get user input
    phone = input("Enter phone number (with country code): +")
    medication = input("Enter medication name: ")
    dose = input("Enter dosage: ")
    
    # Get time
    hour = int(input("Enter hour (24-hour format): "))
    minute = int(input("Enter minute: "))
    
    # Create message
    message = f"💊 Time to take {medication} ({dose})"
    
    print(f"\nSending message to +{phone}")
    print(f"Message: {message}")
    print(f"Time: {hour}:{minute:02d}")
    
    try:
        # Send WhatsApp message with better parameters
        pwk.sendwhatmsg(f"+{phone}", message, hour, minute, wait_time=10, tab_close=False, close_time=5)
        print("✅ Message scheduled successfully!")
        print("📱 WhatsApp Web will open and send the message automatically!")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        print("💡 Make sure WhatsApp Web is open and logged in!")
        # Try alternative method
        try:
            print("🔄 Trying alternative method...")
            pwk.sendwhatmsg(f"+{phone}", message, hour, minute)
        except Exception as e2:
            print(f"❌ Alternative method also failed: {e2}")

def send_now():
    """
    Send message immediately
    """
    print("=== Send Message Now ===")
    
    phone = input("Enter phone number (with country code): +")
    medication = input("Enter medication name: ")
    dose = input("Enter dosage: ")
    
    message = f"💊 Time to take {medication} ({dose})"
    
    try:
        # Send immediately with better parameters
        pwk.sendwhatmsg_instantly(f"+{phone}", message, wait_time=10, tab_close=False, close_time=5)
        print("✅ Message sent!")
        print("📱 WhatsApp Web will open and send the message automatically!")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        print("💡 Make sure WhatsApp Web is open and logged in!")
        # Try alternative method
        try:
            print("🔄 Trying alternative method...")
            pwk.sendwhatmsg_instantly(f"+{phone}", message)
        except Exception as e2:
            print(f"❌ Alternative method also failed: {e2}")

def main():
    """
    Main menu
    """
    print("MediRemainder WhatsApp Helper")
    print("=" * 30)
    print("1. Schedule reminder")
    print("2. Send message now")
    print("3. Exit")
    
    choice = input("\nChoose option (1-3): ")
    
    if choice == "1":
        send_reminder()
    elif choice == "2":
        send_now()
    elif choice == "3":
        print("Goodbye! 👋")
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
