import base64
import requests
import json

class gpt_api:
    def __init__(self, api_key):
        self.api_key = api_key

    def encode_image(self, image_path):
        """Encodes the image at the specified path to a base64 string."""
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')

    def update(self, ingredients, utensils):
        self.ingredients = ingredients
        self.utensils = utensils

    def debug_print(self):
        print(self.ingredients)
        print(self.utensils)

    def prompt_specific(self, meal):
        """Gets a recipe based on the image provided."""
        #base64_image = self.encode_image(image_path)
        
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }

        payload = {
            "model": "gpt-4o-mini",
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": "I am going to give you a list of all of the ingredients in my house and all of the means of cooking, I want you to give me a step by step recipe to make this specific meal if I have all of the ingredients. If I am missing anything required, fill me in first on what I am missing, then give me a step by step recipe on how to cook this meal. Separate the recipe into distinct steps, with time stamps for each. Also include at the end all of the ingredients consumed." + "In my house, I have " + self.ingredients + ", and all of the cooking appliances I own are " + self.utensils + ". I want to make " + meal
                        },
                    ]
                }
            ],
            "max_tokens": 300
        }

        response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
        
        return response.json()['choices'][0]['message']['content']
    
    def prompt_list(self):
        
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }

        payload = {
            "model": "gpt-4o",
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": "I am going to give you a list of all of the ingredients in my house and all of the means of cooking. I want you to give me recipies using only what I have provided and nothing more. Separate each recipe into distinct steps, with time stamps for each. Also include at the end all of the ingredients consumed. Do not be verbose, don't say anything other than what the instructions provided. Also, assume I only have what I am about to list. " + "In my house, I have " + self.ingredients + ", and all of the cooking appliances I own are " + self.utensils + ". Tell me what I can make!"
                        },
                    ]
                }
            ],
            "max_tokens": 600
        }

        response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
        return response.json()['choices'][0]['message']['content']
