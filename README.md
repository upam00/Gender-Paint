<div align="center" class="row">
  <img src="https://dummyimage.com/300x300/ff8000/0011ff&text=GP" width="200"/>
</div>
<h3 align="center">Gender-Paint API</h3>
<h5 align="center">A gender recognition solution</h5>
<br>


### Technologies used

* Flask
* OpenCV
* Tensorflow
* Keras

### Steps to run the application

1. `cd Gender-Paint`
   
2. `pip3 install -r requirements.txt` (only for the first time) then `python3 app.py`

3. Add or Edit the routes and functions in the file app.py

### Testing the API

1. Locally, eg: http://localhost:3434/status
2. With LIVE Heroku Server, eg: https://genderpaintapi.herokuapp.com/status
3. Test the API with POSTMAN. 


Example input for POST:
* Set the URL TO `https://genderpaintapi.herokuapp.com/upload`

INPUT:
```json
    {
        "base64":"Add Your Base64 string here"
    }
```


### Authors

##### [Adittya Dey](https://github.com/adiXcodr)
##### [Subhasish Goswami](https://github.com/subhasishgosw5)
##### [Upam Sarmah](https://github.com/upam00) 
