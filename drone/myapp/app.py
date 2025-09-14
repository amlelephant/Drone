from flask import Flask, request, jsonify, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/flightPlan')
def flightPlan():
    return render_template('index.html')


@app.route('/savedRoutes')
def savedRoutes():
    return render_template('saved.html')


@app.route('/waypoints', methods=['POST'])
def get_waypoints():
    data = request.json
    print("Received waypoints:", data)
    # You can write these to a file or send them over MAVLink
    return jsonify({"status": "ok", "received": len(data)})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Accessible over local Wi-Fi
