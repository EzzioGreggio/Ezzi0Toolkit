import json, os, sys
from multiprocessing.pool import ThreadPool
from rich.console import Console

console = Console()

def exctractJsonData(filename):
    with open(filename, "r") as file:
        data = json.load(file)
    return data


def displayProgress(iteration, total):
    barMaxWidth = 45
    barCurrentWidth = barMaxWidth * iteration // total
    bar = "█"* barCurrentWidth + "-" * (barMaxWidth-barCurrentWidth)
    progress = "%.1f" % (iteration / total * 100)
    console.print(f"|{bar}| {progress} %", end="\r", style="bold green")
    if iteration == total:
        print()


def thredpoolExecuter(function, iterable, iterableLength):
    numberOfWorkers = os.cpu_count()
    console.print(f"\nRunning port scanner using [bold green]{numberOfWorkers}[/bold green] workers.\n", style="bold blue")

    with ThreadPool(numberOfWorkers) as pool:
        for loop_index, _ in enumerate(pool.imap(function, iterable), 1):
            displayProgress(loop_index, iterableLength)


def closeModule():
    os.system("sudo python3 toolkit.py")
    sys.exit()