import psutil
import platform
from datetime import datetime
import ctypes
from os import terminal_size
import os
import time
from colorama import init, Fore, Back, Style
import pwinput
import win10toast
from win10toast import ToastNotifier
notify = ToastNotifier()
pip_installtask_complete = ToastNotifier()


# used for clear
clear = lambda: os.system('cls')
packs = lambda: os.system('pip install ' + package_name)
app = lambda: os.system(appname + ".exe")
site = lambda: os.system("start https://" + site_name)

## used for neofetch
def get_size(bytes, suffix="B"):
    """
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

## Setup.
ctypes.windll.kernel32.SetConsoleTitleW("teniaShell v1.0 - preparing shell")
time.sleep(3)
print("Launching Tenia teniashell.")
time.sleep(4.13)
print("")
print("")
ctypes.windll.kernel32.SetConsoleTitleW("teniaShell v1.0 - login")
print("Tenia Shell DEMO on tenia-v1.0-demo - running on Python")
tenia_login = input("login >> ")
tenia_password = pwinput.pwinput("password >> ")

## Shell goes here.
while True:
    ctypes.windll.kernel32.SetConsoleTitleW("teniaShell v1.0 - teniashell")
    ## Prompt
    tenia_shell = input(Fore.LIGHTGREEN_EX + tenia_login + "@tenia" + Fore.LIGHTMAGENTA_EX + ">> " + Fore.WHITE)
    ## Commands.
    if tenia_shell == "help":
        print("$ help - you are here!")
        print("$ sysinfo - linux reference, it checks your computer.")
        print("$ echo - prints your stuff.")
        print("$ exit - self explanatory.")
        print("$ command.com - ms-dos reference, tells you about the system.")
        print("$ clear - clears shell.")
        print("$ whoami - which user are you.")
        print("$ switchuser - switch users")
        print("$ pip - installs packages through cmd.")
        print("$ open - opens windows apps.")
        print("$ browser - opens up your browser with the link that you input.")
        print("$ notify - create a notification!")
    elif tenia_shell == "notify":
        notify_what = input("title>> ")
        notify_what2 = input("message>> ")
        notify.show_toast(notify_what,notify_what2)

    elif tenia_shell == "browser":
        site_name = input("website>> ")
        site()
    elif tenia_shell == "open":
        appname = input("appname>> ")
        app()
    elif tenia_shell == "pip":
        package_name = input("packagename>> ")
        packs()
        pip_installtask_complete.show_toast("teniaShell","pip install task of " + package_name + " is complete.")
    elif tenia_shell == "switchuser":
        clear = lambda: os.system('cls')
        clear()
        tenia_login = input("teniaShell - login >> ")
        tenia_password = input("teniaShell - password >> ")
    elif tenia_shell == "clear":
        clear = lambda: os.system('cls')
        clear()
    elif tenia_shell == "whoami":
        print("You are " + tenia_login)
    elif tenia_shell == "sysinfo":
        print("teniaShell SysInfo is detecting your computer hardware.")
        time.sleep(4)
        ## System Information
        print("="*40, "System Information", "="*40)
        uname = platform.uname()
        print(f"System: teniaShell on {uname.system}")
        print(f"Node Name: {uname.node}")
        print(f"Release: {uname.release}")
        print(f"Version: {uname.version}")
        print(f"Machine: {uname.machine}")
        print(f"Processor: {uname.processor}") 
        # Boot Time
        print("="*40, "Boot Time", "="*40)
        boot_time_timestamp = psutil.boot_time()
        bt = datetime.fromtimestamp(boot_time_timestamp)
        print(f"Boot Time: {bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}")
        # let's print CPU information
        print("="*40, "CPU Info", "="*40)
        # number of cores
        print("Physical cores:", psutil.cpu_count(logical=False))
        print("Total cores:", psutil.cpu_count(logical=True))
        # CPU frequencies
        cpufreq = psutil.cpu_freq()
        print(f"Max Frequency: {cpufreq.max:.2f}Mhz")
        print(f"Min Frequency: {cpufreq.min:.2f}Mhz")
        print(f"Current Frequency: {cpufreq.current:.2f}Mhz")
        # CPU usage
        print("CPU Usage Per Core:")
        for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
            print(f"Core {i}: {percentage}%")
        print(f"Total CPU Usage: {psutil.cpu_percent()}%")
            # Memory Information
        print("="*40, "Memory Information", "="*40)
        # get the memory details
        svmem = psutil.virtual_memory()
        print(f"Total: {get_size(svmem.total)}")
        print(f"Available: {get_size(svmem.available)}")
        print(f"Used: {get_size(svmem.used)}")
        print(f"Percentage: {svmem.percent}%")
        print("="*20, "SWAP", "="*20)
        # get the swap memory details (if exists)
        swap = psutil.swap_memory()
        print(f"Total: {get_size(swap.total)}")
        print(f"Free: {get_size(swap.free)}")
        print(f"Used: {get_size(swap.used)}")
        print(f"Percentage: {swap.percent}%")   
    elif tenia_shell == "echo":
        echo = input("echo>> ")
        print(echo)
    elif tenia_shell == "exit":
        print("Exiting.")
        time.sleep(2.15)
        exit()
    elif tenia_shell == "command.com":
        print("teniaShell v1.0 running on Python 3.")
        print("2022 bruhlnv.")
