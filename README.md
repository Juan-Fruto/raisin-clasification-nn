# Clasification neural network for the Raisin dataset

This repository contains Python code for building and training a neural network using TensorFlow and Keras for binary classification. The model is designed to classify data into two classes based on a dataset provided in an Excel file (`Clean_Raisin_Dataset.xlsx`). The code includes data preprocessing, model architecture, training, and visualization of training metrics.

## Limitations

- ** Algorithmic Complexity
   The current implementation of the algorithm for data verification has a time complexity of \(O(n \cdot m)\), where \(n\) is the number of rows and \(m\) is the number of columns in the dataframe.
   While the current complexity may be acceptable for moderate-sized datasets, it could become a limitation for larger datasets. Contributions to optimize and reduce the algorithmic complexity are welcomed. If you have ideas or improvements to make the code more efficient, feel free to submit a pull request.

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/your-repository.git
   cd your-repository
   ```

2. Install the required dependencies:

   ```bash
   pip install tensorflow scikit-learn pandas matplotlib
   ```

3. Run the code:

   ```bash
   python your_script.py
   ```

## Code Structure

- **Data Loading and Preprocessing:**
  - The dataset is loaded from the Excel file, and the features and labels are separated.
  - The features are normalized using `StandardScaler`.

- **Model Architecture:**
  - A sequential neural network model is created using Keras.
  - Input layer with 7 units, followed by three hidden layers with 28 units each and sigmoid activation function.
  - Output layer with 1 unit and sigmoid activation function.

- **Model Compilation:**
  - The model is compiled using the Adam optimizer with a learning rate of 0.01 and binary crossentropy loss.
  - Accuracy is used as a metric for evaluation.

- **Training:**
  - The model is trained on the training data for 4000 epochs with validation on a separate test set.

- **Results Visualization:**
  - Training history is visualized with plots for loss and accuracy over epochs.
  - Plots are saved in the `results` directory.

## Results

Training results, including loss and accuracy graphs, can be found in the `results` directory. Adjust hyperparameters, model architecture, or dataset as needed for your specific use case.

Feel free to explore, modify, and integrate this code into your projects. If you find it helpful, consider giving it a star!
