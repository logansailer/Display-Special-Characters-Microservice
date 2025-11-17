import json
import requests
import os
from datetime import datetime

# Microservice URL
MICROSERVICE_URL = "http://localhost:5000/convert"

def prompt_user_string():
    """Prompt the user to enter a string."""
    print("=" * 60)
    print("Character to Unicode Converter - Client")
    print("=" * 60)
    user_input = input("\nEnter a string to convert (special characters will be converted to Unicode):\n> ")
    return user_input

def create_json_file(data, filename="input.json"):
    """Create a JSON file with the input data."""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"\n✓ Input JSON file created: {filename}")
    return filename

def send_to_microservice(json_data):
    """Send JSON data to the microservice and return the response."""
    try:
        print(f"Sending request to microservice at {MICROSERVICE_URL}...")
        response = requests.post(
            MICROSERVICE_URL,
            json=json_data,
            headers={'Content-Type': 'application/json'},
            timeout=10
        )
        
        # Check if request was successful
        response.raise_for_status()
        
        return response.json()
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to microservice.")
        print("   Make sure the microservice is running on http://localhost:5000")
        return None
    except requests.exceptions.Timeout:
        print("Error: Request timed out.")
        return None
    except requests.exceptions.HTTPError as e:
        print(f"Error: HTTP {response.status_code}")
        try:
            error_data = response.json()
            print(f"   {error_data.get('error', 'Unknown error')}")
        except:
            print(f"   {str(e)}")
        return None
    except Exception as e:
        print(f"Error: {str(e)}")
        return None

def save_response_json(response_data, filename="output.json"):
    """Save the response to a JSON file."""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(response_data, f, ensure_ascii=False, indent=2)
    print(f" Output JSON file created: {filename}")
    return filename

def display_results(input_string, response_data):
    """Display the conversion results."""
    if response_data and 'converted_string' in response_data:
        converted = response_data['converted_string']
        print("\n" + "=" * 60)
        print("CONVERSION RESULTS")
        print("=" * 60)
        print(f"\nOriginal string:")
        print(f"  {input_string}")
        print(f"\nConverted string (Unicode escape sequences):")
        print(f"  {converted}")
        print("\n" + "=" * 60)
    else:
        print("No conversion result received from microservice.")

def main():
    """Main function to run the client application."""
    try:
        # Step 1: Prompt user for input
        user_string = prompt_user_string()
        
        if not user_string:
            print("\n⚠ No string entered. Exiting.")
            return
        
        # Step 2: Create JSON file with the input string
        input_data = {"string": user_string}
        input_filename = create_json_file(input_data)
        
        # Step 3: Send to microservice
        response_data = send_to_microservice(input_data)
        
        if response_data:
            # Step 4: Save response to JSON file
            output_filename = save_response_json(response_data)
            
            # Step 5: Display results
            display_results(user_string, response_data)
        else:
            print("\n⚠ Conversion failed. Please check the microservice connection.")
            
    except KeyboardInterrupt:
        print("\n\n Program interrupted by user.")
    except Exception as e:
        print(f"\n Unexpected error: {str(e)}")

if __name__ == "__main__":
    main()

