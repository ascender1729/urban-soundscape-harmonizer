import numpy as np
from src.ml.data_preparation import load_and_preprocess_audio
from src.ml.model import create_model

def test_load_and_preprocess_audio():
    # Create a dummy audio file for testing
    dummy_audio = np.random.rand(22050 * 5)  # 5 seconds of random noise
    np.save('dummy_audio.npy', dummy_audio)
    
    features = load_and_preprocess_audio('dummy_audio.npy')
    assert features.shape[1] == 14  # 13 MFCCs + 1 spectral centroid

def test_create_model():
    model = create_model(input_shape=(100, 14), num_classes=10)
    assert len(model.layers) == 7  # Input layer + 2 Conv1D + 2 MaxPooling1D + 2 Dense
