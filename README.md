# HTTPeeper - HTTP Requester Tester
Take a peep 
This Python script is designed to perform HTTP requests GET, POST, PUT, DELETE, PATCH, and OPTIONS to a specified URL. 

## Installation
Before running this script, ensure Python is installed on your system. This script is compatible with Python 3.x versions. You will also need the requests library.

Clone the repository or download the script to your local machine.
```markdown
git clone https://github.com/napSec/HTTPeeper
```

Install the Dependencies :

``` python3
'pip install requests'

```
## Usage
To use the script, follow these steps:
```python
cd httpeeper
```

Run the script from your terminal or command prompt.
``` python3
python3 httpeeper.py

```

Enter the URL you wish to test when prompted. Ensure you have authorization to interact with this URL.

```javascript
Select the HTTP method you want to use for the request. The script supports GET, POST, PUT, DELETE, PATCH, and OPTIONS methods.

```


After selecting the HTTP method and entering the URL, the script will perform the selected HTTP request to the given URL and print the status code, response headers, and the first 500 characters of the response body directly in the terminal.

## Features

Support for Multiple HTTP Methods: This script allows users to test how a web application responds to different types of HTTP requests.
Custom Headers and Data: The script includes an example of sending requests with JSON data and custom headers, demonstrating how to test APIs or web applications that require such inputs.
Response Display: 

The script outputs the response's status code, headers, and body to help users analyze the application's behavior.
## Legal Disclaimer



This script is for educational purposes only and should only be used on web servers or applications where you have explicit permission from the rightful owners. Unauthorized testing against websites, servers, or applications is illegal and unethical.


## License 

This project is licensed under the MIT License. Please see the LICENSE file for details.


