import cmd
import os
import sys
import socket
import subprocess
import logging
import time
import threading
import json
import re
import shlex


from cmd import Cmd

HOST = "0.0.0.0"
PORT = 5333


class Client(cmd.Cmd):
    
    parameters = {
        "host": "0.0.0.0",
        "port": "5333"
    }
    
    completions = list(parameters.keys())
    
    prompt = 'bS - Client > '
    
    
    doc_header = 'Client Commands (type help <topic>):'
    undoc_header = 'Undocumented commands:'
    
    
    def complete_set(self, text, line, begidx, endidx):
        mline = line.partition(' ')[2]
        offs = len(mline) - len(text)
        return [s[offs:] for s in self.completions if s.startswith(mline)]
    
    
    def do_run(self, line):
        print('Running server...')
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            while True:
                s.connect((HOST, PORT))
                msg = input("Enter msg: ")
                s.send(b'{msg}')
            #s.sendall(b'Hello, world')
                data = s.recv(1024)
                data = data.decode("utf-8")
                print(data)
            
                if data.lower() == 'closed':
                    break
            
                print(f"Received: {data}")
                s.close()
                print("Connection closed.")
                
                
def loop():
    try:
        Client().cmdloop()
    except KeyboardInterrupt:
        sys.exit(0)
        
if __name__ == '__main__':
    loop()
        
        
            