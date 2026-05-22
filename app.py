from flask import request, jsonify

@app.route('/api/log-simulation', methods=['POST'])
def log_simulation():
    data = request.json
    # Process or save your solar area / consumption data here
    print(f"User generated {data.get('generation')} kWh simulation data.")
    return jsonify({"status": "success", "message": "Metrics logged."})
