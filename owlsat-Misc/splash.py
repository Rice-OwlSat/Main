import gc,time,sys,os,microcontroller

RED = '\033[91m'
GREEN = '\033[92m'
BLUE = '\033[94m'
RESET = '\033[0m'  

def _format_uptime():
    seconds = int(time.monotonic())
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return f"{hours:02}:{minutes:02}:{seconds:02}"

def get_storage_info():
    stat = os.statvfs("/")
    block_size = stat[0]
    total_blocks = stat[2]
    free_blocks = stat[3]
    
    total = block_size * total_blocks
    free = block_size * free_blocks
    used = total - free

    return f"{used / 1024:.2f} KiB / {total / 1024:.2f} KiB"

def show_splash():
    try:
        with open("/splash", "r") as f:
            text = f.read()
        print(f"{BLUE}{text}{RESET}")
        print(f"{BLUE}Platform:{RESET}", sys.platform)
        print(f"{BLUE}CircuitPython version:{RESET}", os.uname().version)
        print(f"{BLUE}Board:{RESET}", os.uname().machine)
        print(f"{BLUE}CPU:{RESET}", os.uname().sysname)
        gc.collect()
        max_ram = gc.mem_free() + gc.mem_alloc()
        print(f"{BLUE}Free memory:{RESET} ", gc.mem_free(), "/", max_ram, " bytes")
        print(f"{BLUE}Uptime:{RESET}", _format_uptime())
        print(f"{BLUE}CPU frequency:{RESET}", microcontroller.cpu.frequency / 1000000, "MHz")
        print(f"{BLUE}Disk:{RESET}", get_storage_info())
    except Exception as e:
        print(f"{RED}Splash error:", e)
