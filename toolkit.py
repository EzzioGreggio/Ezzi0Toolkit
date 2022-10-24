#!/usr/bin/python
#
#       Ezzi0 TOOLKIT V1.1
#
#       My GitHub : https://github.com/EzzioGreggio
#
#       This Toolkit's GitHub link: https://github.com/EzzioGreggio/Ezzi0Toolkit
#       
#       Disclaimer : Educational Purpose Only

import pyfiglet, sys, os, time
from rich.console import Console
from rich.table import Table

sys.path.append('./utilities/public/')
from utils import exctractJsonData


console = Console()

class toolKit:
    v = "1.1"

    def checkUpdate():
        pass


    def __init__(self):
        self.modules = ["Port Scanner", "Test"]
        self.modulesInfo = {"1": "portScanner", "2": "test",}


    def keyQuit(self):
        console.print("\nCTRL+C is pressed. Exiting.", style="bold red")
        sys.exit()

    def quit(self):
        console.print("Thanks for using Ezzi0 ToolKit. Goodbye.", style="bold red")
        sys.exit()


    def showStartupMessage(self):
        asciiArt = pyfiglet.figlet_format("Ezzi0TKit")
        console.print(f"[bold cyan]{asciiArt}[/bold cyan]")

        table = Table(show_edge=False, show_header=False)
        table.add_column("TOOL_NUMBER", style="cyan", justify="right")
        table.add_column("TOOL_NAME", style="cyan", justify="left")
        n = 0
        for i in self.modules:
            if n < 10:
                table.add_row(f"[{n+1}]", i)
                n+=1
        table.add_row("[99]", "Quit")

        console.print(table)


    def checkModuleInstallation(self, module):
        try:
            f = open(f"modules/{module}/{module}.py")
            console.print(f"\n################### Running {module}.py ###################", style="bold blue")
            f.close()
            os.system(f"sudo python3 modules/{module}/{module}.py")
            sys.exit()
        except IOError:
            install = input(f"Can't find the {module} files, do you want to auto-download it now(y/n)?:> ")
            if install == "y":
                console.print(f"Downloading {module} from https://github.com/EzzioGreggio/Ezzi0Toolkit/modules/{module}.", style="bold cyan")
                #os.system(f"git clone https://github.com/EzzioGreggio/Ezzi0Toolkit/modules/{module}")
            else:
                console.print(f"Skipping...", style="bold cyan")
        self.initialize()

    def runModule(self, moduleCode):
        if moduleCode == "99" or moduleCode == "q":
            self.quit()
        elif moduleCode in self.modulesInfo.keys():
            try:
                moduleToRun = self.modulesInfo.get(moduleCode)
                self.checkModuleInstallation(moduleToRun)
            except Exception as e:
                console.print(f"An error accourred: [italic red]{str(e)}[/italic red]", style="bold red")
        else:
            console.print(f"The module code N°[bold red]{moduleCode}[/bold red] is not a module you can run, check again if it's on the list above.", style="bold red")
            time.sleep(4)
            self.initialize()


    
    def initialize(self):
        self.showStartupMessage()
        
        try:
            choose = input(":> ")
            if choose != "": (self.runModule(choose))
            else: (self.initialize())
        except KeyboardInterrupt:
            self.keyQuit()


if __name__ == "__main__":

    def checkRoot():
        console.print("[bold blue]Checking root...[/bold blue]")
        if os.geteuid() != 0:
            console.input(f"[bold red]You need to run the script as root. Press enter to quit program.[/bold red]")
            sys.exit()
        else:
            console.print(f"✔ You are root, running script. ✔", style="bold green")


    def checkUpdate():
        os.system("cd ./utilities/public")
        os.system("git clone https://github.com/EzzioGreggio/Ezzi0Toolkit/")
        os.system("rm latestVersion.txt")


    checkRoot()
    checkUpdate()

    runToolkit = toolKit()
    runToolkit.initialize()