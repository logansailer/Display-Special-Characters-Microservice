# Character to Unicode Converter Microservice

A REST API microservice that converts special characters in a string to Unicode escape sequences.

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the microservice:
```bash
python3 char_unicode.py
```

The service will start on `http://localhost:5000`

## Using the Client-Side Application

A client-side script (`client.py`) is provided to interact with the microservice:

1. Make sure the microservice is running
2. Run the client:
```bash
python3 client.py
```
3. Enter a string when prompted
4. The script will:
   - Create an `input.json` file with your string
   - Send it to the microservice
   - Save the response to `output.json`
   - Display the conversion results

## Architecture

<iframe style="border: 1px solid rgba(0, 0, 0, 0.1);" width="800" height="450" src="https://embed.figma.com/board/w8eLCQVEEqJ1GzvwrEPXcu/UML-Sequence-Diagram?node-id=0-1&embed-host=share" allowfullscreen></iframe>



*Flow*
1. User enters string → Client creates `input.json`
2. Client sends POST request → Microservice converts string
3. Microservice returns result → Client saves to `output.json`
4. Client displays results to User


**Example:**
```
Enter a string to convert (special characters will be converted to Unicode):
> Hello, 世界! 🌍

Input JSON file created: input.json
Sending request to microservice at http://localhost:5000/convert...
Output JSON file created: output.json

============================================================
CONVERSION RESULTS
============================================================

Original string:
  Hello, 世界! 🌍

Converted string (Unicode escape sequences):
  Hello, \u4e16\u754c! \ud83c\udf0d
============================================================
```

### POST /convert

Converts special characters in a string to Unicode escape sequences.

**Request:**
```json
{
    "string": "Hello, 世界! 🌍"
}
```

**Response:**
```json
{
    "converted_string": "Hello, \\u4e16\\u754c! \\ud83c\\udf0d"
}
```


## Client-Side Usage Example

response = requests.post('http://localhost:5000/convert', 
    json={'string': 'Hello, 世界! 🌍'})
data = response.json()
print(data['converted_string'])
```


