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


class Server(cmd.Cmd):
    parameters = {
        "host": "0.0.0.0",
        "port": "5333"
    }
    
    completions = list(parameters.keys())
    
    prompt = 'bS - Server  > '
    
    
    doc_header = 'Server Commands (type help <topic>):'
    undoc_header = 'Undocumented commands:'
    
    
    def do_run(self, line):
        print('Running server...')
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((HOST, PORT))
        server.listen(5)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            incoming_client_socket, incoming_client_address = server.accept()
            print(f"Incomming connection from: {incoming_client_address[0]}:{incoming_client_address[1]}")
            
            while True:
                req = incoming_client_address = incoming_client_socket.recv(1024)
                req = req.decode("utf-8")
                
                if req.lower() == 'close':
                    print("Closing connection...")
                    incoming_client_socket.send("closed".encode("utf-8"))
                    break
                print(f"Received: {req}")
            
                res = "Accepted".encode("utf-8")
                
                incoming_client_socket.send(res)
            
            incoming_client_socket.close()
            server.close()
            
            print("Connection closed.")
            
            
            
            
    def do_server(self, line):
        host = socket.gethostname()
        port = 5000  

        server_socket = socket.socket()  
        server_socket.bind((host, port))  
        server_socket.listen(2)
        conn, address = server_socket.accept()  
        print("Connection from: " + str(address))
        while True:
            if not data:
                break
            print("from connected user: " + str(data))
            data = input(' -> ')
            conn.send(data.encode()) 

        conn.close()  
        
        
        
        
            
    def do_help(self, arg: str) -> bool | None:
        return super().do_help(arg)
    
    def do_EOF(self, arg: str) -> bool:
        return True
    
    
    def default(self, line):
        if line:
            os.system(line)
            
            
            
            
def loop():
    try:
        Server().cmdloop()
    except KeyboardInterrupt:
        sys.exit()
        
        
if __name__ == '__main__':
    loop()
            