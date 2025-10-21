#!/usr/bin/env python3
"""
Quick start script for MediRemainder Telegram Bot
"""

import subprocess
import sys
import os

def install_requirements():
    """Install required packages"""
    print("📦 Installing required packages...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "python-telegram-bot==20.7"])
        print("✅ Packages installed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing packages: {e}")
        return False

def start_bot():
    """Start the Telegram bot"""
    print("🤖 Starting MediRemainder Telegram Bot...")
    try:
        import telegram_bot_server
        telegram_bot_server.main()
    except ImportError:
        print("❌ Bot server not found. Make sure telegram_bot_server.py exists.")
    except Exception as e:
        print(f"❌ Error starting bot: {e}")

def main():
    """Main function"""
    print("🏥 MediRemainder Telegram Bot Setup")
    print("=" * 40)
    
    # Install requirements
    if not install_requirements():
        print("❌ Setup failed at package installation")
        return
    
    # Start bot
    print("\n🚀 Starting bot...")
    start_bot()

if __name__ == "__main__":
    main()
