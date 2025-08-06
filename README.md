# Voice-Activated Emergency Alert System 🔊🚨

This project is a **voice-activated emergency alert system** built using a **Raspberry Pi Zero W**. It listens for predefined distress phrases (like "Help me!") and sends an emergency alert via email or SMS with location details.

## 🚀 Features

- 🎙️ Real-time voice recognition using Google Web Speech API
- 🔒 Detects custom distress phrases (e.g., "help me", "emergency")
- 📧 Sends alert via Email (SMTP) or SMS (Twilio)
- 📍 Captures approximate GPS location using IP-based geolocation
- 🔇 Ambient noise adjustment for better accuracy
- 💡 Designed for personal safety (children, elderly, solo travelers)

## 🛠️ Tech Stack

- **Device**: Raspberry Pi Zero W
- **Languages**: Python 3
- **Libraries**:
  - `speech_recognition` (Google Web Speech API)
  - `smtplib` (Email alerts)
  - `twilio` (SMS alerts – optional)
  - `requests`, `geocoder` (for IP-based location)
- **Audio Requirements**: USB microphone, `flac` encoder

## ⚙️ Installation

### Prerequisites

Install required packages:

```bash
sudo apt update
sudo apt install flac portaudio19-dev python3-pyaudio
Create and activate a virtual environment:

bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate
Install Python dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Example requirements.txt:
nginx
Copy
Edit
speechrecognition
pyaudio
requests
geocoder
twilio
Update .env file:
Create a .env file with your credentials:

env
Copy
Edit
EMAIL_ADDRESS=your_email@example.com
EMAIL_PASSWORD=your_email_password
TO_EMAIL=recipient_email@example.com
TWILIO_SID=your_twilio_sid
TWILIO_AUTH_TOKEN=your_twilio_token
TWILIO_PHONE=your_twilio_phone
DEST_PHONE=recipient_phone_number
🧪 Running the Script
Run the listener:

bash
Copy
Edit
python3 main.py
The program will:

Adjust for ambient noise

Listen for distress phrases

Recognize your speech

Send alerts if a distress phrase is detected

🐛 Troubleshooting
If you see an error like:

pgsql
Copy
Edit
OSError: FLAC conversion utility not available
Fix it by installing flac:

bash
Copy
Edit
sudo apt install flac
📦 Project Structure
bash
Copy
Edit
.
├── main.py
├── alert.py
├── location.py
├── .env
├── requirements.txt
└── README.md
📌 Use-Cases
Personal safety for elderly or children

Solo travel safety companion

Emergency alerting in low-tech environments



ChatGPT can make mistakes. Check important
