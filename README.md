# sl0s (Simple List of Scanners)
**sl0s (Simple List of Scanners)** is a simple and useful tool for automatic scanning of web applications that uses third-party scanners to save your time.
All you need to do is specify the necessary scanners and get on with your business.

# Features
* Switchable pool of scanners: You can change list of scanners and use your favorite.
* Stop wasting your time: You can run several scanners at the same time, which will search for vulnerabilities in the background.
* Comfortable: In the result of scannig you will have a .txt file which consist of reviews from scanners in a convenient format.
* Easy to Use: Simple command-line interface with informative tips.

# Installation
You can install sl0s using git clone:

$ git clone https://github.com/imnoturbadboy/sl0s.git

# Usage
$ python3 sl0s.py

An input field will appear on your screen where you can enter the names of the scanners you need (for example, --nmap). 

**Attention** - Enter the names of the scanners using "--{scannername}". 

After entering the name, you need to enter the flags for the scanners, the flags can be entered the way you usually do when using utilities. 

After the scanners and their flags, you must enter the address of the target host. 

**For your attention** - The address of the target host must be entered once. 

If you need to use multiple scanners, your string will look like this: --{scannername} -{flag} -{flag} --{scannername} --{flag} --{scannername} -{flag} -{flag} --{flag} url/ip

When the scan is over, you will be prompted to open the file with the scan results, if you refuse to open it immediately, it's okay, the file will be saved in the same directory where the utility is located. 

The file will be named "scan_results_{targetname}".  

The scan reports are separated from each other, so you won't get confused!

# Support
If you have any ideas or thoughts on how to improve or implement new features, submit an issue or create a pull request! 
