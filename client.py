import socket

# create an INET, STREAMing socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# now connect to the web server on port 80 - the normal http port
s.connect(('localhost', 60080))
msg = b'Hello, world'
msg_len = len(msg)
print(f'Sending message:\n---\n{msg}\n---\nwith length {msg_len}')
s.send(msg)