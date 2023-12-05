from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/weather/<city>')
def get_weather(city):
    api_key = 'f43ca829cbc60273f891756cf4356e5b'
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    print(response.json())
    return jsonify(response.json())


if __name__ == '__main__':
    app.run(debug=True)
