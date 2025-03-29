from flask import Flask, request, jsonify
from rasa.core.agent import Agent
from rasa.utils.endpoints import EndpointConfig

app = Flask(__name__)

model_path = 'models'  # Path to your trained Rasa model
agent = Agent.load(model_path, action_endpoint=EndpointConfig(url="http://localhost:5055/webhook"))

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    responses = agent.handle_text(user_message)
    return jsonify(responses)

if __name__ == '__main__':
    app.run(port=5005)
