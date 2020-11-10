<div align="center" class="row">
  <img src="https://i.imgur.com/ocR2K0r.png" width="200"/>
</div>
<h3 align="center">Gender-Paint API</h3>
<h5 align="center">A gender recognition model trained</h5>
<br>

### Model Architecture-
The keras model is created by training SmallerVGGNet from scratch on around 2200 face images (~1100 for each class). Face region is cropped by applying face detection using cvlib on the images gathered from Google Images. It acheived around 96% training accuracy and ~90% validation accuracy. (20% of the dataset is used for validation)
<div align="center" class="row">
  <img src="https://i.imgur.com/TpOlyyo.png" width="100"/>
</div>

### Technologies used
* Tensorflow
* Keras
* Flask
* OpenCV


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
