from flask import Flask, request, jsonify
from ChatGPTBotAPI import ChatGPTBotAPI
import json
# load chat gpt api key 
with open('api_key.json', 'r') as f:
    data = json.load(f)
    api_key = data['api_key']

app = Flask(__name__)
chat_gpt_instance = ChatGPTBotAPI(api_key)



@app.route('/')
def index():
    return 'Sample Chat Application'

# POST: /chat/create 
@app.route('/chat/create', methods=['POST'])
def create_chat():
    """
    Creates a chat prompt for the bot to respond to
    Note: This is a POST request because we are fetching data from the request,
    I would not recommend using a GET request as theere i possiblity of GET request
    being hit by crawlers and bots, which would create a lot of prompts and our bill
    would go up.

    Args:
        None

    Returns:
        int: The index of the prompt
    """
    # get the prompt from the request
    prompt = request.form['prompt']
    # create the prompt 
    prompt_index = chat_gpt_instance.create_prompt(prompt)
    # send Content-Type: application/json
    return jsonify({
        "status" : "success",
        "data" : {
            "prompt_index" : prompt_index
        }
    })

# POST: /chat/<int:prompt_index>/get_response
@app.route('/chat/<int:prompt_index>/get-response', methods=['POST'])
def get_response(prompt_index : int):
    """
    Gets the response from the bot

    Args:
        prompt_index (int): The index of the prompt to get the response from

    Returns:
        str: The response from the bot
    """
    # get the response from the bot
    response = chat_gpt_instance.get_response(prompt_index)
    # send Content-Type: application/json
    return jsonify({
        "status" : "success",
        "data" : {
            "response" : response
        }
    })

# PUT: /chat/<int:prompt_index>/
@app.route('/chat/<int:prompt_index>/', methods=['PUT'])
def update_prompt(prompt_index : int):
    """
    Updates the prompt at the given index

    Args:
        prompt_index (int): The index of the prompt to update

    Returns:
        None
    """
    # get the new prompt from the request
    new_prompt = request.form['new_prompt']
    # update the prompt
    chat_gpt_instance.update_prompt(prompt_index, new_prompt)
    # send Content-Type: application/json
    return jsonify({
        "status" : "success",
        "data" : {}
    })

# DELETE: /chat/<int:prompt_index>/
@app.route('/chat/<int:prompt_index>/', methods=['DELETE'])
def delete_prompt(prompt_index : int):
    """
    Deletes the prompt at the given index

    Args:
        prompt_index (int): The index of the prompt to delete

    Returns:
        None
    """
    # delete the prompt
    chat_gpt_instance.delete_prompt(prompt_index)
    # send Content-Type: application/json
    return jsonify({
        "status" : "success",
        "data" : {}
    })




if __name__ == '__main__':
    app.run(debug=True)