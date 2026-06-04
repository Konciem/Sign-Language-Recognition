# Sign Language Recognition

![Made with Python](https://img.shields.io/badge/Python-FFD43B?style=flat&logo=python&logoColor=blue)

## Project Description
This is a desktop application that uses AI to recognize American Sign Language (ASL) signs. The program analyzes the camera, locates the user's hand, and based on the finger positions in real-time, guesses which letter of the alphabet is currently being shown.

## Model Training
The entire "learning" process of AI is located in the Jupyter Notebook file (`training.ipynb`). It is divided into two main stages:

* **Data Extraction:** Instead of training the algorithm on raw images, the program uses the MediaPipe library to "see" key hand landmarks (e.g., joint positions and fingertips) across thousands of training photos. These exact coordinates are extracted and saved into the `extracted_data.csv` spreadsheet.
* **Model Training:** In this section, I feed the collected points into a Random Forest Classifier algorithm. The program evaluates its knowledge by generating a confusion matrix – in tests, it achieved an excellent accuracy of over 98.2%. The ready model is saved to the `asl_model.pkl` file so the main application can use it instantly.

<div align="center">
  <img width="500" alt="Confusion Matrix" src="https://github.com/user-attachments/assets/2e60c138-efe7-4014-a59e-b7e00572363e">
</div>

## To Do
The following features are planned to be implemented:
* **Gesture Stabilizer:** Special logic in the code to prevent "flickering" and jumping letters on the screen. The sign will only be displayed when the user holds their hand in a stable position for a brief moment.
* **State Machine:** A mechanism that allows combining single letters into words and entire sentences. It will also allow defining action signs (e.g., detecting a specific gesture as "Space" or "Delete"), turning the application into a working virtual notepad operated without touching a keyboard.

## Dataset
The dataset used to train the machine learning models in this project is the **ASL Alphabet Dataset**, created by Akash. It is publicly available on Kaggle.

* **Source:** [ASL Alphabet on Kaggle](https://www.kaggle.com/datasets/grassknoted/asl-alphabet)
* **Author:** grassknoted (Akash)

The dataset was used purely for educational and training purposes.
