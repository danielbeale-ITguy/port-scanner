#! /usr/bin/python3
import socket






s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def portscan(targetname,startport,endport):
        
            for port in range(startport,endport +1):
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(1)

                try:
                    s.connect((targetname, port))
                    print(f'port {port} connected')
                except socket.error as e:
                       print(f'port {port} failed to connect')

                finally:
                       s.close()
                
                
target = input(str('What is the targets IP address?'))


portscan(target,1,81)




