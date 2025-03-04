from flask import Flask, jsonify, request
import cw_aida,cw_quest,cw_pas
import traceback
from flask_cors import CORS


app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
    

@app.route('/aida', methods=['POST'])
def aida():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No data provided"}), 400

        # Extracting data from request
        creativity = data.get('creativity', 'Unknown')
        product_name = data.get('product_name', 'Unknown')
        description = data.get('description', 'Unknown')
        target_audience = data.get('target_audience', 'Unknown')
        tone_of_voice = data.get('tone_of_voice', 'Professional')

        result = cw_aida.generate_aida(creativity, product_name, target_audience, description, tone_of_voice)

        return jsonify({
            "message": "QUEST marketing copy generated",
            "data": result,
            "status": "success"
        })

    except Exception as e:
        print(f"Server error: {str(e)}")
        print(traceback.format_exc())
        return jsonify({
            "error": "Server error",
            "message": str(e)
        }), 500



@app.route('/quest', methods=['POST'])
def quest():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No data provided"}), 400

        # Extracting data from request
        creativity = data.get('creativity', 'Unknown')
        product_name = data.get('product_name', 'Unknown')
        description = data.get('description', 'Unknown')
        target_audience = data.get('target_audience', 'Unknown')
        tone_of_voice = data.get('tone_of_voice', 'Professional')

        result = cw_quest.generate_quest(creativity, product_name, target_audience, description, tone_of_voice)

        return jsonify({
            "message": "QUEST marketing copy generated",
            "data": result,
            "status": "success"
        })

    except Exception as e:
        print(f"Server error: {str(e)}")
        print(traceback.format_exc())
        return jsonify({
            "error": "Server error",
            "message": str(e)
        }), 500



@app.route('/pas', methods=['POST'])
def pas():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No data provided"}), 400

        # Extracting data from request
        creativity = data.get('creativity', 'Unknown')
        product_name = data.get('product_name', 'Unknown')
        description = data.get('description', 'Unknown')
        target_audience = data.get('target_audience', 'Unknown')
        tone_of_voice = data.get('tone_of_voice', 'Professional')

        result = cw_pas.generate_pas(creativity, product_name, target_audience, description, tone_of_voice)

        return jsonify({
            "message": "QUEST marketing copy generated",
            "data": result,
            "status": "success"
        })

    except Exception as e:
        print(f"Server error: {str(e)}")
        print(traceback.format_exc())
        return jsonify({
            "error": "Server error",
            "message": str(e)
        }), 500



    
if __name__ == '__main__':
    app.run(debug=True)
