#Continuously request user input until the user enters a keyboard interrupt to quit. At each input, use gpt4free (g4f package) to submit 
#The input to GPT-4 via g4f.Provider.Bing. Print the response to the user. 
#If the user enters "ctrl+c" to quit, print "Goodbye!" and exit the program.

import g4f
import time
import sys
import io

first_run=True

while True:
    try:
        if first_run==True:
            user_input = input("Enter your prompt: ")
            first_run=False
        else:
            user_input = input(": ")
        saved_stdout = sys.stdout
        sys.stdout = io.StringIO()
        response = g4f.ChatCompletion.create(model='gpt-4', messages=[{"role":"user","content":user_input}], provider=g4f.Provider.Bing, stream=True)
        sys.stdout = saved_stdout
        print_message=""
        for message in response:
            print_message+=message
        print(print_message)
    except KeyboardInterrupt:
        print("Goodbye!")
        exit()

