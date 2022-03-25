import subprocess


# run a linux command
# list files in current directory
subprocess.run('ls')


# if on windows use shell=True to prevent errors
subprocess.run('ls -la', shell=True)


# run with command and arguments
subprocess.run(['ls', '-la'])


# to get a proces object
p1 = subprocess.run(['ls', '-la'])
print(p1)
print(p1.args) # gives the args provided to the subprocess
print(p1.returncode) # gives the returncode
print(p1.stdout) # will give the stdout if it was captured


# capture the output
p1 = subprocess.run(['ls', '-la'], capture_output=True)
print(p1.stdout) # will print as bytestring

print(p1.stdout.decode()) # will print as string


# convert to text on capture
p1 = subprocess.run(['ls', '-la'], capture_output=True, text=True)
print(p1.stdout)


# alternative to capture_output
p1 = subprocess.run(['ls', '-la'], stdout=subprocess.PIPE, text=True)
print(p1.stdout)


# redirect output to a file
with open('output.txt', 'w') as f:
    p1 = subprocess.run(['ls', '-la'], stdout=f, text=True)


# try to run command on a non existing directory
p1 = subprocess.run(['ls', '-la', 'dne'], capture_output=True, text=True)
print(p1.returncode) # prints the returncode
print(p1.stderr) # prints the stderr

# throw error if not true
#p1 = subprocess.run(['ls', '-la', 'dne'], capture_output=True, text=True, check=True)

# redirect error to DEVNULL so no error is thrown
p1 = subprocess.run(['ls', '-la', 'dne'], stderr=subprocess.DEVNULL)
print(p1.stderr) # will print None as stderr was redirected


# pipe output from one command to another
p1 = subprocess.run(['cat', 'test.txt', 'dne'], capture_output=True, text=True)

print(p1.stdout)

p2 = subprocess.run(['grep', '-n', 'test'], capture_output=True, text=True, input=p1.stdout)

print(p2.stdout)


# alternative method using pipe symbol
p1 = subprocess.run('cat test.txt | grep -n test', capture_output=True, text=True, shell=True)

print(p1.stdout)
