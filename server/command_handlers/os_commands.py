import subprocess
import logging
from . import CommandHandler

class OSCommandHandler(CommandHandler):
    def handle(self, request):
        try:
            command_name = request['command_name']
            parameters = request['parameters']
            full_command = [command_name] + parameters
            
            logging.info(f"Executing OS command: {' '.join(full_command)}")
            
            result = subprocess.run(full_command, capture_output=True, text=True)
            
            if result.returncode == 0:
                logging.info("Command executed successfully")
                return result.stdout
            else:
                error_msg = f"Command failed with return code {result.returncode}. Error: {result.stderr}"
                logging.error(error_msg)
                return error_msg
        
        except Exception as e:
            error_msg = f"Error executing OS command: {str(e)}"
            logging.error(error_msg)
            return error_msg

