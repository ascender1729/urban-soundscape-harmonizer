from data_preparation import prepare_dataset
from model import create_model
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

def train_model(dataset_path):
    # Prepare dataset
    X, y = prepare_dataset(dataset_path)
    
    # Encode labels
    le = LabelEncoder()
    y_encoded = le.fit_transform(y)
    
    # Split dataset
    X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)
    
    # Create and train model
    input_shape = X_train.shape[1:]
    num_classes = len(np.unique(y_encoded))
    model = create_model(input_shape, num_classes)
    
    model.fit(X_train, y_train, epochs=10, validation_split=0.2)
    
    # Evaluate model
    test_loss, test_acc = model.evaluate(X_test, y_test)
    print(f"Test accuracy: {test_acc}")
    
    # Save model
    model.save('soundscape_model.h5')

if __name__ == "__main__":
    train_model('path/to/dataset')
