# Open AI Chat GPT Demo with Flask API 

## Installation Steps 

* Used virtual environment to develop the application, but you can also work without it, just run `pip install -r requirements.txt` to install all the dependencies.
* create a file named `api_key.json` and store you api key in the format 
```(json)
{
  "api_key" :"<YOU API KEY>"
}
```

* Then start local server by running `python app.py` in terminal. 
* Please import postman collection `Flask-App.postman_collection.json` that I have added for reference. 

## Notes
* Currently no context is being maintained, so the prompt from ChatGTP will only know what you have said in current message. 
* No Database is being Used, so restrting your application will remove all the prompt messages. 

