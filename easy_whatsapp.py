#!/usr/bin/env python3
"""
Super Easy WhatsApp Reminder
Just run this and follow the instructions!
"""

import pywhatkit as pwk

# Step 1: Get information from user
print("🏥 MediRemainder WhatsApp Helper")
print("=" * 40)

phone = input("📱 Phone number (with country code): +")
medication = input("💊 Medication name: ")
dose = input("💉 Dosage: ")

# Step 2: Get time
print("\n⏰ When do you want the reminder?")
hour = int(input("Hour (0-23): "))
minute = int(input("Minute (0-59): "))

# Step 3: Create the message
message = f"💊 Time to take {medication} ({dose})"

# Step 4: Send the message
print(f"\n📤 Sending message...")
print(f"To: +{phone}")
print(f"Message: {message}")
print(f"Time: {hour}:{minute:02d}")

try:
    pwk.sendwhatmsg(f"+{phone}", message, hour, minute, wait_time=10, tab_close=False, close_time=5)
    print("✅ Success! Message will be sent at the scheduled time.")
    print("📱 WhatsApp Web will open and send the message automatically!")
    
except Exception as e:
    print(f"❌ Error: {e}")
    print("💡 Make sure WhatsApp Web is open and you're logged in!")
    print("🔧 Try opening WhatsApp Web manually first: https://web.whatsapp.com")
    # Try alternative method
    try:
        print("🔄 Trying alternative method...")
        pwk.sendwhatmsg(f"+{phone}", message, hour, minute)
        print("✅ Alternative method worked!")
    except Exception as e2:
        print(f"❌ Alternative method also failed: {e2}")
        print("💡 Try running the script again or check your internet connection.")

print("\n🎉 Done! Your reminder is scheduled.")
print("\n📋 IMPORTANT NOTES:")
print("• The message will be sent automatically")
print("• Don't close the browser window")
print("• If it doesn't work, try running the script again")
print("• Make sure WhatsApp Web is logged in")
