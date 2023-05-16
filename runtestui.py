import easygui as eg
import subprocess
import json

# Load function and payload information from a JSON config file
with open('testConfig.json', 'r') as f:
  config = json.load(f)

# Show a choice box to select the function
function_choice = eg.choicebox("Select a function to invoke:", "Function Selector", config.keys())
if function_choice is None:  # User cancelled
  exit()

# Show a choice box to select the payload
payload_choice = eg.choicebox("Select a payload to use:", "Payload Selector", config[function_choice])
if payload_choice is None:  # User cancelled
  exit()

# Build the sls invoke command
command = ["sls", "invoke", "-f", function_choice, "-p", payload_choice]

# Execute the command
subprocess.run(command)
