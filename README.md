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



*Flow*
1. User enters string → Client creates `input.json`
2. Client sends POST request → Microservice converts string
3. Microservice returns result → Client saves to `output.json`
4. Client displays results to User

<img width="1116" height="1196" alt="UML Sequence Diagram" src="https://github.com/user-attachments/assets/82e0295b-51ae-4eb5-b182-c3f810e49d87" />

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


