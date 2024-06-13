import tensorflow as tf
import cv2
import numpy as np
from detect_fall import detect_fall
from send_alert import send_sms_alert

# Define parameters
sequence_length = 30  # Number of frames in each sequence
frame_buffer = []
alert_sent = False  # Flag to track if SMS alert has been sent

def process_frame(frame):
    # Resize frame to match the model input size, if necessary
    resized_frame = cv2.resize(frame, (320, 240))
    return resized_frame

def main(video_path):
    global alert_sent
    cap = cv2.VideoCapture(video_path)
    
    if not cap.isOpened():
        print("Error: Could not open video file.")
        return
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        # Convert frame to grayscale and process it
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        processed_frame = process_frame(gray_frame)
        
        # Add frame to buffer
        frame_buffer.append(processed_frame)
        
        # Ensure frame_buffer contains the correct number of frames
        if len(frame_buffer) == sequence_length:
            # Perform fall detection
            is_fall = detect_fall(frame_buffer, processed_frame)
            
            if is_fall and not alert_sent:
                # Define message
                message = "Fall detected! Please check immediately."
                send_sms_alert(message)
                alert_sent = True  # Set flag to True to indicate alert has been sent
            
            # Remove the oldest frame to maintain buffer size
            frame_buffer.pop(0)
        
        # Display the frame (optional)
        cv2.imshow('Video Feed', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the capture and close windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    video_path = r"path to ur file"  # Replace with the path to your video file
    main(video_path)
