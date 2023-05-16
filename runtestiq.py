import inquirer
import subprocess
import json
from inquirer.themes import Default

# Load function and payload information from a JSON config file
with open('testConfig.json', 'r') as f:
    config = json.load(f)

# Show a list of functions and get user input
question = [
  inquirer.List('function_choice',
    message="Select a function to invoke:",
    choices=list(config.keys()),
  )
]
answers = inquirer.prompt(question, theme=Default())
function_choice = answers['function_choice']

# Show a list of payloads and get user input
question = [
  inquirer.List('payload_choice',
    message="Select a payload to use:",
    choices=list(config[function_choice]),
  )
]
answers = inquirer.prompt(question, theme=Default())
payload_choice = answers['payload_choice']

# Build the sls invoke command
command = ["C:\\Users\\nnola\AppData\\Local\\Yarn\\bin\\sls.cmd", "invoke", "-f", function_choice, "-p", payload_choice]

# Execute the command
subprocess.run(command)
