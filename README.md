<div align="center" class="row">
  <img src="https://i.imgur.com/ocR2K0r.png" width="400"/>
</div>
<h3 align="center">Gender-Paint API</h3>
<h5 align="center">A Deep Learning Model to Predict Gender From Paitings</h5>
<br>

### Model Architecture-
The keras model is created by training SmallerVGGNet from scratch on around 2200 face images (~1100 for each class). Face region is cropped by applying face detection using cvlib on the images gathered from Google Images. It acheived around 96% training accuracy and ~90% validation accuracy. (20% of the dataset is used for validation)
<div align="center" class="row">
  <img src="https://i.imgur.com/TpOlyyo.png" width="250"/>
</div>

### Screenshots
<div align="center" class="row">
  <img src="https://i.imgur.com/7gnaiMa.png" width="500"/>
</div>

<div align="center" class="row">
  <img src="https://i.imgur.com/87rHkSV.png" width="500"/>
</div>


### Sample Input
<div align="center" class="row">
  <img src="https://i.imgur.com/hc2d4hd.jpg" width="300"/>
</div>

### Sample Output
<div align="center" class="row">
  <img src="https://i.imgur.com/Kt0mUlU.jpg" width="300"/>
</div>


### Technologies used
* Tensorflow
* Keras
* Flask
* OpenCV

### Steps to run user interface
1. Run the file Gender Detection.exe

### Steps to run the application

1. `cd Gender-Paint`
   
2. `pip3 install -r requirements.txt` (only for the first time) then `python3 app.py`

3. Add or Edit the routes and functions in the file app.py

### Testing the API

1. Locally, eg: http://localhost:3434/status
2. With LIVE Heroku Server, eg: https://genderpaintapi.herokuapp.com/status
3. Test the API with POSTMAN. 


Example input for POST:
* Set the URL TO `https://genderpaintapi.herokuapp.com//upload`

INPUT:
```json
    {
        "base64":"Add Your Base64 string here"
    }
```

<hr>

### Authors

##### [Adittya Dey](https://github.com/adiXcodr)
##### [Subhasish Goswami](https://github.com/subhasishgosw5)
##### [Upam Sarmah](https://github.com/upam00) 
