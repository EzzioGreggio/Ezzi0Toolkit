#!/usr/bin/python
#
#       Ezzi0 TOOLKIT v1.0
#       
#       Created By : Ezzi0
#       GitHub : https://github.com/EzzioGreggio
#       
#       Disclaimer : Educational Purpose Only

try:
    import os, sys, colorama, time
    from colorama import Fore

except ModuleNotFoundError:
            print("One or more libraries not found, try running the 'setup.py' file.")


colorama.init(autoreset=True)

v = '1.0'

banner = f"""{Fore.CYAN}

!!!BANNER HERE!!!

    {Fore.BLUE}[1] PassGenerator                   
    {Fore.BLUE}[2] PortScanner
    {Fore.BLUE}[3] PyCrypt                         
    {Fore.BLUE}[4] Coming Soon!
    {Fore.BLUE}[5] Coming Soon!                    
    {Fore.BLUE}[6] Coming Soon!
    {Fore.RED}[q] Quit
"""


#    code start here    #

def quit():
    print(Fore.BLUE + "Thanks for using Ezzi0's Toolkit!. Goodbye")
    sys.exit()


def checkRoot():
    print("Checking root...")
    if os.geteuid() != 0:
        input(f"{Fore.RED}You need to run the script as root. Press enter to quit program.")
        sys.exit()
    else:
        print(f"{Fore.GREEN}✔ You are root, running script. ✔")


def runModule(moduleToRun):
    try:
        f = open(f"modules/{moduleToRun}/{moduleToRun}.py")
        print(f"{Fore.CYAN}\n################### Running {moduleToRun}.py ###################")
        f.close()
        os.system(f"sudo python3 modules/{moduleToRun}/{moduleToRun}.py")
        sys.exit()
    except IOError:
        print(os.system("pwd"))
        print(f"Downloading Password Generator from https://github.com/EzzioGreggio/{moduleToRun}.")
        os.system(f"git clone https://github.com/EzzioGreggio/{moduleToRun}")


def start():
    os.system("clear")
    print(banner)
    while True:
        choose = str(input(f"{Fore.YELLOW}Select an option>:{Fore.WHITE} ")).lower()

        if choose == "q":
            quit()
        
        elif choose == "1":
            moduleToRun = "passGenerator"
            runModule(moduleToRun)
        
        elif choose == "2":
            moduleToRun = "portScanner"
            runModule(moduleToRun)

        elif choose == "99":
            moduleToRun = "test"
            runModule(moduleToRun)
        
        else:
            print(Fore.RED + "\n\nPlease choose an option from the list.\n")
            time.sleep(1.5)
            os.system("clear")
            start()

checkRoot()
start()