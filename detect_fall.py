import numpy as np
import tensorflow as tf
from send_alert import send_sms_alert

class MockLSTMModel:
    def __init__(self):
        self.input_shape = (None, 30, 320 * 240)

    def predict(self, sequence_array):
        return np.array([[0.6]])

lstm_model = MockLSTMModel()
alert_sent = False  # Flag to track if SMS alert has been sent

def predict_with_lstm(sequence):
    sequence_length = lstm_model.input_shape[1]
    features = lstm_model.input_shape[2]

    flattened_sequence = [frame.flatten() for frame in sequence]
    sequence_array = np.array(flattened_sequence)

    if sequence_array.shape[1] != features:
        raise ValueError(f"Expected frame size: {features}, but got: {sequence_array.shape[1]}")

    sequence_array = sequence_array.reshape((1, sequence_length, features))
    lstm_fall = lstm_model.predict(sequence_array)
    return lstm_fall > 0.5

def detect_fall(frame_buffer, processed_frame):
    global alert_sent
    frame_buffer.append(processed_frame)
    
    sequence_length = lstm_model.input_shape[1]
    if len(frame_buffer) > sequence_length:
        frame_buffer.pop(0)

    if len(frame_buffer) == sequence_length:
        sequence = frame_buffer
        is_fall = predict_with_lstm(sequence)
        print("Predicted fall:", is_fall)
        return is_fall
    
    return False
