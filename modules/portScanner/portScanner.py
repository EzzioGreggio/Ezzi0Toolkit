import socket, sys, pyfiglet
from rich.console import Console
from rich.table import Table

sys.path.append('./utilities/public/')
from utils import exctractJsonData, displayProgress, thredpoolExecuter, closeModule

console = Console()

class portScanner:

    PORTS_DATA_FILE = "./utilities/public/commonPorts.json"
    

    def __init__(self):
        self.openPorts = []
        self.portsInfo = {}
        self.remoteHost = ""

    def getPortsInfo(self):
        data = exctractJsonData(portScanner.PORTS_DATA_FILE)
        self.portsInfo = {int(k): v for (k, v) in data.items()}


    @staticmethod
    def getHostIpAddr(target):
        try:
            ipAddr = socket.gethostbyname(target)
        except socket.gaierror as e:
            print(f"An error accourred. [{e}]")
            closeModule()
        console.print(f"\nIP Address aquired: [bold blue]{ipAddr}[/bold blue]")
        return ipAddr


    def scanPort(self, port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1.0)
        connStatus = sock.connect_ex((self.remoteHost, port))
        if connStatus == 0:
            self.openPorts.append(port)
        sock.close()


    def showCompletionMessage(self):
        if self.openPorts:
            #print(f"Number of open ports found on:[{self.remoteHost}] : {len(self.openPorts)}")
            #print(f"\nOpen Ports Information: ")
            console.print("Scan Completed, Open Ports:", style="bold blue")
            table = Table(show_header=True, header_style="bold cyan")
            table.add_column("PORT", style="blue")
            table.add_column("STATE", style="blue", justify="center")
            table.add_column("SERVICE", style="blue")
            for port in self.openPorts:
                table.add_row(str(port), "OPEN", self.portsInfo[port])
                #print(f"Port n°:{str(port)} - Type:{self.portsInfo[port]}")
            console.print(table)
        else:
            console.print("No open ports found.", style="bold red")


    @staticmethod
    def showStartupMessage():
        asciiArt = pyfiglet.figlet_format("PyPScanner")
        console.print(asciiArt, style="bold cyan")
        console.print("#" * 56, style="bold red")
        console.print(
            "#" * 13, "MultiThread TCP Port Scanner", "#" * 13, style="bold red"
        )
        console.print("#" * 56, style="bold red")
        print()


    def initialize(self):
        self.showStartupMessage()
        self.getPortsInfo()

        try:
            target = input("Insert The Target:> ")
            if(target == "test" or target == ""): target = "scanme.nmap.org" #possibilmente da rimuovere in seguito
        except KeyboardInterrupt:
            console.print("\nCTRL+C is pressed. Exiting.", style="bold red")
            closeModule()

        
        self.remoteHost = self.getHostIpAddr(target)
        
        try:
            input("\nPort Scanner is ready. Press ENTER to run the scanner.")
        except KeyboardInterrupt:
            console.print("\nCTRL+C is pressed. Exiting.", style="bold red")            
            closeModule()
        else:
            self.run()


    def run(self):
        try:
            thredpoolExecuter(
                self.scanPort, self.portsInfo.keys(), len(self.portsInfo.keys())
            )
            self.showCompletionMessage()
        except KeyboardInterrupt:
            console.print("\nCTRL+C is pressed. Exiting.", style="bold red")
            self.showCompletionMessage()
            closeModule()



if __name__ == "__main__":
    runScanner = portScanner()
    runScanner.initialize()