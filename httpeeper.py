import requests

def exploit(url, method):
    """
   Sends an HTTP request to specified URL using the your specified method and prints the results.
    """
    # Common data for demonstration purposes (might not be applicable for GET, HEAD, OPTIONS)
    data = {'sample_key': 'sample_value'}
    headers = {'Content-Type': 'application/json'}
    
    try:
        # Dynamically calling the method on the requests object based on user input
        response = getattr(requests, method.lower())(url, headers=headers, json=data)
        
        print(f"Sent {method} request to {url}")
        print(f"Status Code: {response.status_code}")
        print("\nResponse Headers:")
        for header, value in response.headers.items():
            print(f"{header}: {value}")
        print("\nResponse Body (first 500 characters):")
        print(response.text[:500])
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    url = input("Enter the URL to exploit: ")
    print("Supported HTTP Methods: GET, POST, PUT, DELETE, PATCH, OPTIONS")
    method = input("Enter the HTTP method to use: ")
    
    if method.upper() in ['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'OPTIONS']:
        exploit(url, method)
    else:
        print("Unsupported HTTP method. Please choose from the listed options.")
