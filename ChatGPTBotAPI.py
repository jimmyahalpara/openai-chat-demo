import openai 
"""
This class is used to interact with the openai api to create a chatbot

Note: I have not maitained context of the conversation here, so the bot will only know 
what you tell it. To main tain the context, I would need to also send some last messages 
and also store the response from chat gpt, which I am not doing considering the time limit 
given to me. 
"""
class ChatGPTBotAPI:
    def __init__(self, open_api_key : str):
        """
        Initializes the ChatGPTBotAPI class

        Args:
            open_api_key (str): The open api key for openai
        """
        openai.api_key = open_api_key
        self.__modal : str = "gpt-3.5-turbo"
        self.__messages : list[dict[str, str]] = [
        ]
        self.__temperature : float = 0.9
    
    def create_prompt(self, prompt : str) -> int:
        """
        Creates a prompt for the bot to respond to

        Args:
            prompt (str): The prompt to send to the bot

        Returns:
            None
        """
        self.__messages.append({"role" : "user", "content" : prompt})
        # return index 
        return len(self.__messages) - 1
    
    def get_response(self, prompt_index : int) -> str:
        """
        Returns the response from the bot
        
        Args:
            prompt_index (int): The index of the prompt to get the response from
                openai
        Returns:
            str: The response from the bot
        """
        response : dict = openai.ChatCompletion.create(
            model=self.__modal,
            messages = [self.__messages[prompt_index]],
            temperature=self.__temperature,
        )
        return response['choices'][0]['message']['content']
    
    def update_prompt(self, prompt_index : int, new_prompt : str):
        """
        Updates the prompt at the given index

        Args:
            prompt_index (int): The index of the prompt to update
            new_prompt (str): The new prompt to update the prompt with

        Returns:
            None
        """
        self.__messages[prompt_index]['content'] = new_prompt

    def delete_prompt(self, prompt_index : int):
        """
        Deletes the prompt at the given index

        Args:
            prompt_index (int): The index of the prompt to delete

        Returns:
            None
        """
        del self.__messages[prompt_index]

