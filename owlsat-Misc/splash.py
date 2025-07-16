import gc,time,sys,os,microcontroller

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
        print(text)
        print("Platform:", sys.platform)
        print("CircuitPython version:", os.uname().version)
        print("Board:", os.uname().machine)
        print("CPU:", os.uname().sysname)
        gc.collect()
        max_ram = gc.mem_free() + gc.mem_alloc()
        print("Free memory: ", gc.mem_free(), "/", max_ram, " bytes")
        print("Uptime: ", _format_uptime())
        print("CPU frequency:", microcontroller.cpu.frequency / 1000000, "MHz")
        print("Disk:", get_storage_info())
    except Exception as e:
        print("Splash error:", e)
