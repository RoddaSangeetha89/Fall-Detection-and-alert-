import numpy as np
import tensorflow as tf

# Load the LSTM model
model_path = r"C:\Users\rodda\OneDrive\Desktop\fall-detection-alert\models\lstm_model.h5"
lstm_model = tf.keras.models.load_model(model_path)

# Print model summary to understand its input shape requirements
lstm_model.summary()

def predict_with_lstm(sequence):
    # Convert sequence to numpy array
    sequence_array = np.array(sequence)

    # Print shape of sequence_array for debugging
    print(f"Sequence array shape before reshaping: {sequence_array.shape}")

    # Adjust the sequence length and features based on model's expected input shape
    sequence_length = lstm_model.input_shape[1]
    features = lstm_model.input_shape[2]

    if len(sequence) != sequence_length:
        raise ValueError(f"Expected sequence length: {sequence_length}, but got: {len(sequence)}")

    # Flatten frames and stack them into a sequence
    flattened_sequence = [frame.flatten() for frame in sequence]
    sequence_array = np.array(flattened_sequence)

    if sequence_array.shape[1] != features:
        raise ValueError(f"Expected frame size: {features}, but got: {sequence_array.shape[1]}")

    sequence_array = sequence_array.reshape((1, sequence_length, features))

    # Print shape of sequence_array after reshaping for debugging
    print(f"Sequence array shape after reshaping: {sequence_array.shape}")

    # Call your LSTM model prediction function here
    lstm_fall = lstm_model.predict(sequence_array)
    return lstm_fall>0.5

def detect_fall(frame_buffer, processed_frame):
    frame_buffer.append(processed_frame)
    
    # Maintain a buffer of the last sequence_length frames
    sequence_length = lstm_model.input_shape[1]
    if len(frame_buffer) > sequence_length:
        frame_buffer.pop(0)

    if len(frame_buffer) == sequence_length:
        sequence = frame_buffer  # Use the last sequence_length frames
        is_fall = predict_with_lstm(sequence)
        return is_fall

        if is_fall:
            print("fall detected")
            send_email_alert()
    
    return False  # Not enough frames to make a prediction yet
