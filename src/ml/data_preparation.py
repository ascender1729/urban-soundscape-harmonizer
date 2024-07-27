import librosa
import numpy as np
import os

def load_and_preprocess_audio(file_path, sr=22050, duration=5):
    # Load audio file
    y, _ = librosa.load(file_path, sr=sr, duration=duration)
    
    # Extract features
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
    spectral_centroids = librosa.feature.spectral_centroid(y=y, sr=sr)
    
    # Combine features
    features = np.concatenate([mfccs, spectral_centroids])
    
    return features.T

def prepare_dataset(dataset_path):
    X = []
    y = []
    
    for root, _, files in os.walk(dataset_path):
        for file in files:
            if file.endswith('.wav'):
                file_path = os.path.join(root, file)
                features = load_and_preprocess_audio(file_path)
                X.append(features)
                y.append(os.path.basename(root))  # Assuming class name is the folder name
    
    return np.array(X), np.array(y)
