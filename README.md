
<div align="center">
<img src="https://raw.githubusercontent.com/StuntKids/.github/bc5cf0393ed004c1a57ed0b9fdee921332e94fd1/TensorFlow_logo.svg" width="40%" height="40%">
</div>


# Description
Developing a stunting classification model using TensorFlow. This model can predict a child's nutritional status, classifying it into one of four categories: severely stunted, stunted, normal, or above average height.


# Dataset
Data is taken from: https://www.kaggle.com/datasets/rendiputra/stunting-balita-detection-121k-rows


# Builth With
- Python
- TensorFlow
- Google Colab
  
# Model Architecture
<div align="center">
<img src="https://github.com/StuntKids/.github/blob/main/Model_architecture.png"width="70%" height="70%">
</div>

# Result
<div align="center">
<img src="https://github.com/StuntKids/.github/blob/main/download%20(2).png" width="70%" height="70%">
</div>

# Documentation
- Collect dataset about stunting
- Cleaned the dataset from the duplicate data
- Apply SMOTE technique to oversampling on imbalanced dataset
- Split the dataset into 80% for the training and 20% for the test
- Build the classification model
- Train and evaluates the model
- Build the model with hyperparameter tuning
- Save the best model into h5 and convert it to TFLite
- Create a matching algorithm to determine food recommendations based on the model's prediction results
- Test the model
