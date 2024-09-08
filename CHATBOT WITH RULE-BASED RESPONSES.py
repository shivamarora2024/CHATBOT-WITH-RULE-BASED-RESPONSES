#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import re

def chatbot_response(user_input):
    """
    Processes user input and provides a response based on predefined rules.

    Args:
        user_input (str): The user's input.

    Returns:
        str: The chatbot's response.
    """

    rules = {
        "hello": "Hi there! How can I help you today?",
        "how are you": "I'm doing well, thank you! How can I assist you?",
        "what is your name": "I'm a chatbot. You can call me [Chatbot Name].",
        "what is the weather like": "I can't access real-time weather information. Please check a weather app.",
        "quit": "Goodbye!"
    }

    for pattern, response in rules.items():
        if re.search(pattern, user_input, re.IGNORECASE):
            return response

    return "I couldn't understand that. Please try asking something else."

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            break
        response = chatbot_response(user_input)
        print("Chatbot:", response)


# In[ ]:




