from flask import Flask, request, jsonify

app = Flask(__name__)


def convert_to_unicode_escape(text):
    """
    Convert special characters (non-ASCII) to Unicode escape sequences.
    Returns a string with Unicode escape sequences like \\uXXXX.
    """
    result = []
    for char in text:
        # Check if character is ASCII (0-127)
        if ord(char) < 128:
            result.append(char)
        else:
            # Convert to Unicode escape sequence (\\uXXXX format)
            unicode_escape = f"\\u{ord(char):04X}"
            result.append(unicode_escape)
    return ''.join(result)


@app.route('/convert', methods=['POST'])
def convert_string():
    """
    REST API endpoint that accepts JSON with a string and converts
    special characters to Unicode escape sequences.

    Expected input JSON:
    {
        "string": "Hello, 世界! 🌍"
    }

    Returns JSON:
    {
        "converted_string": "Hello, \\u4e16\\u754c! \\ud83c\\udf0d"
    }
    """
    try:
        # Get JSON data from request
        data = request.get_json()

        # Validate that 'string' key exists
        if not data or 'string' not in data:
            return jsonify({
                'error': 'Invalid JSON format. Expected: {"string": "your string here"}'
            }), 400

        input_string = data['string']

        # Validate that the value is a string
        if not isinstance(input_string, str):
            return jsonify({
                'error': 'The "string" field must be a string type'
            }), 400

        # Convert special characters to Unicode escape sequences
        converted_string = convert_to_unicode_escape(input_string)

        # Return the converted string in JSON format
        return jsonify({
            'converted_string': converted_string
        }), 200

    except Exception as e:
        return jsonify({
            'error': f'An error occurred: {str(e)}'
        }), 500


@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint to verify the service is running."""
    return jsonify({
        'status': 'healthy',
        'service': 'char_unicode_converter'
    }), 200


if __name__ == '__main__':
    print("Starting Character to Unicode Converter Microservice...")
    print("API endpoint: http://localhost:5000/convert")
    print("Health check: http://localhost:5000/health")
    app.run(host='0.0.0.0', port=5000, debug=True)
