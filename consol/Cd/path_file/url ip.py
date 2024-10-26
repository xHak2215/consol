# Importing socket module
import socket

# Defining functin to get the IP address from the URL
def get_ip_address(url):
    try:
        # Using gethostbyname() function of socket module for IP address
        ip_address = socket.gethostbyname(url)
        
        # Returning IP address from the function
        return ip_address
    # if error occurs, returns the error
    except socket.error as err:
        print(f"Error: {err}")

# Defining URL whose IP adddres needs to be found
url = "google.com"

# Calling function with URL
ip = get_ip_address(url)
print(f"The IP address of {url} is {ip}")