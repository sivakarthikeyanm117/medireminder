# MediRemainder WhatsApp Integration

## 🚀 Setup Instructions

### 1. Install Python Dependencies
```bash
pip install -r requirements.txt
```

### 2. WhatsApp Web Setup
1. Open WhatsApp Web in your browser: https://web.whatsapp.com
2. Scan the QR code with your phone
3. Keep WhatsApp Web open and logged in

### 3. Phone Number Format
- Use international format: `+1234567890`
- Include country code (e.g., +1 for US, +91 for India)

## 📱 How It Works

### Web App Integration
1. **Add Reminder**: Select "WhatsApp Message" or "Both Web & WhatsApp"
2. **Enter Phone Number**: Include country code
3. **Set Time**: Choose when you want the reminder
4. **Submit**: The reminder is saved and scheduled

### Python Script
1. **Run the script**: `python whatsapp_reminder.py`
2. **Automatic scheduling**: Messages are sent at the exact time
3. **WhatsApp Web opens**: Automatically opens with the message ready

## 🔧 Features

### ✅ Web Notifications
- Instant browser notifications
- No setup required
- Works on all devices

### ✅ WhatsApp Messages
- Direct WhatsApp messages
- Rich formatting with emojis
- Automatic scheduling
- Works with any phone number

### ✅ Combined Notifications
- Both web and WhatsApp
- Redundancy for important reminders
- Multiple notification channels

## 📋 Usage Examples

### Example 1: Web Notification Only
```
Medication: Paracetamol
Dosage: 500mg
Date: 2024-01-15
Time: 10:00
Notification Type: Web Notification
```

### Example 2: WhatsApp Message
```
Medication: Vitamin C
Dosage: 1000mg
Date: 2024-01-15
Time: 09:00
Phone: +1234567890
Notification Type: WhatsApp Message
```

### Example 3: Both Notifications
```
Medication: ColdAct
Dosage: 2 tablets
Date: 2024-01-15
Time: 20:00
Phone: +1234567890
Notification Type: Both Web & WhatsApp
```

## 🛠️ Troubleshooting

### WhatsApp Issues
- **WhatsApp Web not opening**: Make sure it's logged in
- **Message not sending**: Check phone number format
- **Permission denied**: Allow pop-ups in browser

### Web Notification Issues
- **No notifications**: Check browser notification permissions
- **Permission denied**: Click "Allow" when prompted

### General Issues
- **Reminders not saving**: Check browser localStorage
- **Time not working**: Use 24-hour format (HH:MM)
- **Phone validation**: Include country code

## 🔒 Privacy & Security

- **Phone numbers**: Stored locally in browser
- **No server**: All data stays on your device
- **WhatsApp Web**: Uses official WhatsApp Web interface
- **No data sharing**: Your information stays private

## 📞 Support

If you encounter issues:
1. Check WhatsApp Web is logged in
2. Verify phone number format
3. Ensure browser notifications are enabled
4. Try refreshing the page

## 🎯 Best Practices

1. **Test first**: Try a reminder 1-2 minutes in the future
2. **Keep WhatsApp Web open**: Don't close the browser tab
3. **Use reliable times**: Avoid scheduling during sleep hours
4. **Backup reminders**: Export your data regularly
