import subprocess
import json

# Load function and payload information from a JSON config file
with open('testConfig.json', 'r') as f:
    config = json.load(f)

# Display a list of functions and get user input
print("Functions:")
for i, function in enumerate(config.keys(), start=1):
    print(f"{i}. {function}")
function_choice = input("Select a function to invoke by number: ")
function = list(config.keys())[int(function_choice) - 1]

# Display a list of payloads and get user input
print("Payloads:")
for i, payload in enumerate(config[function], start=1):
    print(f"{i}. {payload}")
payload_choice = input("Select a payload to use by number: ")
payload = config[function][int(payload_choice) - 1]

# Build the sls invoke command
command = ["C:\\Users\\nnola\AppData\\Local\\Yarn\\bin\\sls.cmd", "invoke", "-f", function, "-p", payload]

# Execute the command
subprocess.run(command)
