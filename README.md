# Handwritten Text Recognition
This repository contains code and resources for a Handwritten Text Recognition project. It consists of two main components:

## Jupyter Notebook (HANDWRITTEN_TEXT_RECOGNITION.ipynb) - 
A notebook that provides detailed steps for training, validating, and evaluating a handwritten character recognition model using machine learning.
## Python Script (Board.py) - 
A graphical interface built with Pygame that allows users to draw characters or digits on a canvas. The drawn characters are then predicted by the trained model.

## Overview
This project demonstrates how to recognize handwritten characters (both digits and letters) using a neural network model. The model is trained on image data of handwritten characters, and the trained model is integrated with a Pygame-based graphical interface where users can draw digits or letters, which are then classified by the model in real time.

### Components:

### HANDWRITTEN_TEXT_RECOGNITION.ipynb:
-Trains a Convolutional Neural Network (Keras) using a dataset of handwritten characters. <br />
-Evaluates the model’s performance. <br />
-Saves the best model for use in predictions.

### Board.py:
-Creates a simple GUI using Pygame where users can draw characters. <br />
-Captures the drawn image, processes it, and sends it to the pre-trained model for prediction. <br />
-Displays the predicted character on the screen.


### Additional Notes:
-Make sure to change "bestmodel.keras" in both the notebook and Board.py to point to the correct file path if you're saving/loading the model in a specific directory <br />
-If you need to save the model in a specific folder, refer to the section of the Board.py script where the model is loaded and saved.
