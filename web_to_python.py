#!/usr/bin/env python3
"""
Web App to Python Integration
This connects your web app to WhatsApp functionality
"""

import pywhatkit as pwk
import json
import sys

def send_whatsapp_from_web(phone, medication, dose, date, time_str):
    """
    Function called by your web app
    """
    try:
        # Parse time
        hour = int(time_str.split(':')[0])
        minute = int(time_str.split(':')[1])
        
        # Create message
        message = f"💊 Medication Reminder\n\nTime to take: {medication}\nDosage: {dose}\nDate: {date}\nTime: {time_str}\n\nStay healthy! 🏥"
        
        # Send message with better parameters
        pwk.sendwhatmsg(phone, message, hour, minute, wait_time=10, tab_close=False, close_time=5)
        return "Success"
        
    except Exception as e:
        return f"Error: {str(e)}"

# Get data from web app
if len(sys.argv) >= 6:
    phone = sys.argv[1]
    medication = sys.argv[2]
    dose = sys.argv[3]
    date = sys.argv[4]
    time_str = sys.argv[5]
    
    result = send_whatsapp_from_web(phone, medication, dose, date, time_str)
    print(result)
else:
    print("Usage: python web_to_python.py phone medication dose date time")
