import argparse
import requests
import json
import pyYAML

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="HTTP Requester with output in JSON or YAML")
    parser.add_argument('url', help="URL to fetch data from")
    parser.add_argument('-yaml', help="Output in YAML format", action='store_true')
    args = parser.parse_args()

    # Perform the HTTP request
    try:
        response = requests.get(args.url)
        response.raise_for_status()  # Raises stored HTTPError, if one occurred.
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        return

    # Process and print the response
    try:
        response_data = response.json()  # Convert response to JSON
    except ValueError as e:
        print(f"Error processing JSON response: {e}")
        return

    if args.yaml:
        # Output in YAML format
        print(yaml.dump(response_data, allow_unicode=True, default_flow_style=False))
    else:
        # Default output in JSON format
        print(json.dumps(response_data, indent=4))

if __name__ == "__main__":
    main()
