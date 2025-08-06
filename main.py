import speech_recognition as sr
import time
import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart



# Cool-down time to avoid multiple alerts in a short period (in seconds)
COOL_DOWN_TIME = 10

# List of distress phrases (both Hinglish and English)
distress_phrases = [
    "help me", "I need help", "emergency", "help", "call for help", "I'm in danger",
    "madad karo", "mujhe madad chahiye", "emergency hai", "madad ki zarurat hai", 
    "bachao", "bacha lo"
]

def get_location():
    try:
        response = requests.get("https://ipinfo.io/json")
        data = response.json()
        location = data.get("loc", "")  # Latitude and longitude as a string
        city = data.get("city", "")
        region = data.get("region", "")
        country = data.get("country", "")
        return f"{city}, {region}, {country} (Coordinates: {location})"
    except Exception as e:
        print(f"Could not get location: {e}")
        return "Location not available"



def send_email_alert(text):
    sender_email = "devkhimani99@gmail.com"
    receiver_email = "singhmohit86935@gmail.com"
    password = "ypib lrmv rmxx mtni "

    location = get_location()
    
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = 'Emergency Alert Detected'
    body = f'''
This is an emergency alert!

Detected Phrase:
"{text}"

Location:
{location}

Please take immediate action.
'''
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()
        print("Email alert sent!")
    except Exception as e:
        print(f"Failed to send email: {e}")


def listen_for_distress():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    # Adjust for ambient noise
    with mic as source:
        print("Adjusting for ambient noise...")
        recognizer.adjust_for_ambient_noise(source)

    last_alert_time = time.time()  # Time of last alert

    print("Listening for distress phrases... (Say any of the distress phrases to trigger an alert)")

    while True:
        try:
            # Listen for audio
            with mic as source:
                print("Listening...")
                audio = recognizer.listen(source)

            print("Recognizing...")
            text = recognizer.recognize_google(audio, language='en-IN')  # Hinglish support
            print("You said:", text)

            # Check if any distress phrase is detected
            for phrase in distress_phrases:
                if phrase.lower() in text.lower():
                    current_time = time.time()

                    # Only send alert if cool-down period has passed
                    if current_time - last_alert_time >= COOL_DOWN_TIME:
                        print(f"Distress phrase detected: {phrase} - Sending alert!")
                        # send_sms_alert()  # Send SMS alert
                        send_email_alert(text)  # Send Email alert
                        last_alert_time = current_time  # Update last alert time
                    else:
                        print(f"Cooldown period active. Try again after {COOL_DOWN_TIME - (current_time - last_alert_time):.1f} seconds.")
                    break  # Exit the loop when distress is detected

        except sr.UnknownValueError:
            print("Sorry, I couldn't understand that. Try again.")
        except sr.RequestError as e:
            print(f"Error with speech recognition service: {e}")
        except KeyboardInterrupt:
            print("\nExiting... Goodbye!")
            break

if __name__ == "_main_":
    listen_for_distress()