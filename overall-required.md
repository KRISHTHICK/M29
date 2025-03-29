#Step 1: Set Up Your Development Environment
##1.Install Python: Ensure you have Python installed on your machine. You can download it from python.org.

##2.Create a Virtual Environment: It's good practice to create a virtual environment for your project.
python -m venv chatbot-env
source chatbot-env/bin/activate  # On Windows use `chatbot-env\Scripts\activate`

##3.Install Necessary Libraries: You will need libraries such as rasa, numpy, pandas, etc. Install them using pip.
pip install rasa numpy pandas

#Step 2: Initialize a Rasa Project
##1.Initialize a New Rasa Project:
rasa init
##This command will create a basic Rasa project with some initial files and configurations.

#Step 3: Define Intents and Responses
## Next pg -Edit data/nlu.yml: Define the intents and example user queries.
## Next pg -Edit domain.yml: Define the responses corresponding to the intents.
## Next pg -Edit data/stories.yml: Define stories that represent the conversation paths.

#Step 4: Train the Chatbot
##Train the Chatbot:
rasa train
#Step 5: Test the Chatbot
##Run the Chatbot in Interactive Mode:
rasa shell
#Step 6: Deploy the Chatbot
#Next pg -
#Example: Deploying with Flask
#Install Flask:
pip install Flask
#Create a Flask App:
#Run the Flask App:
python app.py
#Test the Endpoint: You can use tools like Postman or cURL to send a POST request to http://localhost:5005/chat with a JSON payload containing the user's message and receive the chatbot's response.
