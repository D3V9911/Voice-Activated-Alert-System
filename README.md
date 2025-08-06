# Voice-Activated Emergency Alert System

This project is a **voice-activated emergency alert system** built using a **Raspberry Pi Zero W**. It continuously listens for specific distress phrases (e.g., "Help me!") and sends emergency alerts via email or SMS, along with the sender's approximate location.

---

## Features

- Real-time voice recognition using Google Web Speech API
- Detects custom distress phrases (e.g., "help me", "emergency")
- Sends alerts via email (SMTP)
- Captures approximate location using IP-based geolocation
- Ambient noise calibration for better recognition
- Lightweight and power-efficient, ideal for portable use cases

---

## Tech Stack

- **Device**: Raspberry Pi Zero W
- **Programming Language**: Python 3
- **Key Libraries**:
  - `speech_recognition` – voice-to-text using Google Web Speech API
  - `smtplib` – email alerts
  - `requests`, `geocoder` – IP-based location fetching
- **Hardware**:
  - USB Microphone
  - Internet Connectivity (Wi-Fi)
  - Audio encoder: `flac` (for voice recognition)

---
