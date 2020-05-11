# Additional modules
import os
import socket

# Computer Object
class Computer:
    def __init__(self, OS='Windows'):
        self.OS = OS

# Shutdown computer
    def shutdown(self):
        if self.OS == "Windows":
            os.system("shutdown /s")

        elif self.OS == "MacOS" or self.OS == "Linux":
            os.system("sudo shutdown -h now")

# Reboot computer
    def reboot(self):
        if self.OS == "Windows":
            os.system("shutdown /r")

        elif self.OS == "MacOS" or self.OS == "Linux":
            os.system("sudo shutdown -r now")

# Put computer to sleep
    def sleep(self):
        if self.OS == "Windows":
            os.system("shutdown /h")

        elif self.OS == "MacOS" or self.OS == "Linux":
            os.system("sudo shutdown -s now")

#Logout of computer
    def logout(self):
        if self.OS == "Windows":
            os.system("shutdown /l")

        elif self.OS == "MacOS" or self.OS == "Linux":
            os.system("sudo -s")

# Get IP Address of computer
    def ip_addr(self):
        if self.OS == "Windows":
            hostname = socket.gethostname()
            ip_address = socket.gethostbyname(hostname)
            return ip_address

        elif self.OS == "Linux":
            run = os.popen("hostname -I")
            output = run.read()
            ip = ""
            for i in output:
                if i != " ":
                    ip += i
                elif i == " ":
                    break
            return ip.strip()

        elif self.OS == "MacOS":
            run = os.popen("ipconfig getifaddr en1")
            output = run.read()
            return output.strip()