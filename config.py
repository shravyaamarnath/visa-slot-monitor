"""
Configuration — edit this file to customise your monitor.
"""

import os
from dotenv import load_dotenv

load_dotenv()  # reads .env file automatically

# ── URLs to watch ──────────────────────────────────────────────────────────────
URLS = [
    {
        "label": "CheckVisaSlots — H1B Regular",
        "url": "https://checkvisaslots.com/latest-us-visa-availability/h-1b-regular/",
    },
    # ── VisaGrader — H1B Biometrics ───────────────────────────────────────────
    {
        "label": "VisaGrader — New Delhi H1B Biometrics",
        "url": "https://visagrader.com/us-visa-time-slots-availability/india-ind/new-delhi-P147/h1b-visa-H1B#Biometrics",
    },
    {
        "label": "VisaGrader — Chennai H1B Biometrics",
        "url": "https://visagrader.com/us-visa-time-slots-availability/india-ind/chennai-P48/h1b-visa-H1B#Biometrics",
    },
    {
        "label": "VisaGrader — Hyderabad H1B Biometrics",
        "url": "https://visagrader.com/us-visa-time-slots-availability/india-ind/hyderabad-P85/h1b-visa-H1B#Biometrics",
    },
    {
        "label": "VisaGrader — Kolkata H1B Biometrics",
        "url": "https://visagrader.com/us-visa-time-slots-availability/india-ind/kolkata-P100/h1b-visa-H1B#Biometrics",
    },
    {
        "label": "VisaGrader — Mumbai H1B Biometrics",
        "url": "https://visagrader.com/us-visa-time-slots-availability/india-ind/mumbai-P139/h1b-visa-H1B#Biometrics",
    },
    # ── VisaGrader — H1B Interview ────────────────────────────────────────────
    {
        "label": "VisaGrader — New Delhi H1B Interview",
        "url": "https://visagrader.com/us-visa-time-slots-availability/india-ind/new-delhi-P147/h1b-visa-H1B#Interview",
    },
    {
        "label": "VisaGrader — Chennai H1B Interview",
        "url": "https://visagrader.com/us-visa-time-slots-availability/india-ind/chennai-P48/h1b-visa-H1B#Interview",
    },
    {
        "label": "VisaGrader — Hyderabad H1B Interview",
        "url": "https://visagrader.com/us-visa-time-slots-availability/india-ind/hyderabad-P85/h1b-visa-H1B#Interview",
    },
    {
        "label": "VisaGrader — Kolkata H1B Interview",
        "url": "https://visagrader.com/us-visa-time-slots-availability/india-ind/kolkata-P100/h1b-visa-H1B#Interview",
    },
    {
        "label": "VisaGrader — Mumbai H1B Interview",
        "url": "https://visagrader.com/us-visa-time-slots-availability/india-ind/mumbai-P139/h1b-visa-H1B#Interview",
    },
]

# ── Check frequency ────────────────────────────────────────────────────────────
# How often to check each URL (in seconds)
# 300 = every 5 minutes  |  60 = every minute  |  180 = every 3 minutes
CHECK_INTERVAL_SECONDS = int(os.getenv("CHECK_INTERVAL", 300))

# ── Notification channels ──────────────────────────────────────────────────────
# Set to True to enable each channel. Configure credentials below or in .env

# 1. Telegram (FREE — recommended)
TELEGRAM_ENABLED = os.getenv("TELEGRAM_ENABLED", "true").lower() == "true"
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")   # From @BotFather
TELEGRAM_CHAT_ID   = os.getenv("TELEGRAM_CHAT_ID", "")     # Your personal chat ID

# 2. WhatsApp via Twilio (needs Twilio account — free sandbox available)
WHATSAPP_ENABLED = os.getenv("WHATSAPP_ENABLED", "false").lower() == "true"
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID", "")
TWILIO_AUTH_TOKEN  = os.getenv("TWILIO_AUTH_TOKEN", "")
TWILIO_WHATSAPP_FROM = os.getenv("TWILIO_WHATSAPP_FROM", "whatsapp:+14155238886")  # Twilio sandbox number
TWILIO_WHATSAPP_TO   = os.getenv("TWILIO_WHATSAPP_TO", "")     # e.g. whatsapp:+919876543210

# 3. SMS via Twilio
SMS_ENABLED = os.getenv("SMS_ENABLED", "false").lower() == "true"
TWILIO_SMS_FROM = os.getenv("TWILIO_SMS_FROM", "")   # Your Twilio phone number
TWILIO_SMS_TO   = os.getenv("TWILIO_SMS_TO", "")     # Your mobile number e.g. +919876543210

# ── Files ──────────────────────────────────────────────────────────────────────
STATE_FILE = "state.json"   # Stores page hashes between runs
LOG_FILE   = "monitor.log"  # Log file
