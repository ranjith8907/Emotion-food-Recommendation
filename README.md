# Emotion-Foods-Recommendation
Recommending Foods based on your facial expressions using FER 2013 dataset and Sporify api


(Forgive the image quality and my expressions 😆)

# Project Description:
The emotion recognition model is trained on FER 2013 dataset. It can detect 7 emotions. The project works by getting live video feed from web cam, pass it through the model to get a prediction of emotion. Then according to the emotion predicted, the app will suggest food according to the prediction and then displaying them on the screen for a users choice.

# Features:
- Real time expression detection and Foods recommendations.
- Neumorphism UI for website.


# Running the app:
Flask: 
    ## Installation Requirements

    ```
    Framework : Flask, Version : 1.11.8
    Language : Python, Version : 3.6.3

    To run it, you need to install some packages and libraries as follows:

    Flask==2.1.2
    spotipy==2.19.0 
    pandas==1.4.2
    gunicorn==20.1.0
    opencv_python_headless==4.5.5.64
    numpy==1.22.3
    Pillow==9.1.1
    tensorflow==2.9.0
    Time 
    pandas

    To install these, write this on the command line terminal:
    "pip install package-name"
    ```

    ## To run 

    ```

    Enter the command: "python app.py runserver"
    Copy the url and paste it in your favourite browser window.
    ```

# Tech Stack:
- Keras
- Tensorflow
- Spotipy
- Tkinter (For testing)
- Flask


# Dataset:
The dataset used for this project is the famous FER2013 dataset. Models trained on this dataset can classify 7 emotions. The dataset can be found <a href = "https://www.kaggle.com/msambare/fer2013">here</a>.

Note that the dataset is highly imbalanced with happy class having maxiumum representation. This might be a factor resulting in okaysish accuracy after training.


# Model Architecture:
- The model architecture is a sequential model consisting of Conv2d, Maxpool2d, Dropout and Dense layers:
1. Conv2D layers throughout the model have different filter size from 32 to 128, all with activation 'relu'
2. Pooling layers have pool size (2,2)
3. Dropout is set to 0.25 as anything above results in poor performance
4. Final Dense layer has 'softmax' activation for classifying 7 emotions
- Used 'categorical_crossentropy' for loss with 'Adam' optimizer with 'accuracy' metric

Note:- Tried Implementing various other models like VGG16 but accuracy was far too low. This model architecture gives good enough accuracy. A bit more tinkering with hyper parameters might lead to a better accuracy

# Image Processing and Training:
- The images were normalised, resized to (48,48) and converted to grayscale in batches of 64 with help of 'ImageDataGenerator' in Keras API.
- Training took around 13 hours locally for 75 epochs with an accuracy of ~66 %


# Current condition:
The entire project works perfectly fine. Live detection gives good frame rates due to multithreading.


# Project Components:
- camera.py is the module for video streaming, frame capturing, prediction and recommendation which are passed to main.py.
- main.py is the main flask application file.
- index.html in 'templates' directory is the web page for the application. Basic HTML and CSS.
- utils.py is an utility module for video streaming of web camera with threads to enable real time detection.
- train.py is the script for image processing and training the model.

