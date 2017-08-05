
import subprocess

class ShellException(Exception):
    def __init__(self, code, stdout = '', stderr = ''):
        self.code = code
        self.stdout = stdout
        self.stderr = stderr
    
    def __str__(self):
        return 'exit code %d - %s' % (self.code, self.stderr)
    
def run_command(command):
    # Run the command and wait for it to complete
    process = subprocess.Popen(command.split(' '), 
        stdout = subprocess.PIPE, 
        stderr = subprocess.PIPE)
    process.wait()

    # Get the stdout/stderr from the shell
    stdout, stderr = process.communicate()

    # If the shell returned a non-zero exit status, raise an exception
    if process.returncode > 0:
        raise ShellException(process.returncode, stdout, stderr)
    
    return stdout

# Run a command
run_command('rm fake/')