from tensorflow.keras.models import load_model
import os
from detect_fall import detect_fall
from send_alert import send_email_alert

def main(data):
    if detect_fall(data):
        print("Fall detected!")
    else:
        print("No fall detected.")

if __name__ == "__main__":
    # Example data for testing
    data = [0.1, 0.2, 0.3, 0.4, 0.5]  # Replace with actual data
    main(data)
