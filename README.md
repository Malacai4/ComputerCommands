# ComputerCommands

This is a package used to run computer commands using python
in any operating system.

## Installation

Run this command to install:
```python
pip install ComputerCommands
```

## Usage

```python
import ComputerCommands

# Create an object that contains the local computer (replace 'Windows' with computers OS if different)
computer = ComputerCommands.Computer('Windows')

# Shutdown
computer.shutdown()

# Reboot
computer.reboot()

# Sleep
computer.sleep()

# Logout
computer.logout()

# Get computer IP address
computer.ip_addr()
```
