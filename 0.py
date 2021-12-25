import socket
import struct
import telnetlib

def telnet():
    t = telnetlib.Telnet()
    t.sock = s
    t.interact()

s = socket.socket()
s.connect(('vortex.labs.overthewire.org', 5842))

ints = 0

for x in range(0, 4, 1):
    ints += struct.unpack("<I", s.recv(4))[0]

s.send(struct.pack("<I", ints))
telnet()
