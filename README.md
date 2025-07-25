# Main

The Recoding Effort!

## Compiling for CircuitPython
You'll have to build mpy-cross yourself on a Unix shell (for Windows users I recommend WSL2) from the [CircuitPython](https://github.com/adafruit/circuitpython/) version loaded onto the board. Load the compiled bytecode `.mpy` files onto the board, reset the kernel (^C, ^D inside the REPL console), and make sure the module is valid by running `import module-name-here` in the REPL terminal. If it says nothing, you're good to go.
Any other version of mpy-cross generates a bad mpy file.

## DEPENDENCIES
You can compile these yourself or use the raw `.py` file


[debugcolor](https://github.com/pycubed/software/blob/master/mainboard-v05/lib/debugcolor.py)
[bq25883](https://github.com/pycubed/software/blob/master/mainboard-v05/lib/bq25883.py)
[bmx160](https://github.com/pycubed/software/blob/master/mainboard-v05/lib/bmx160.py)
[bitflags](https://github.com/pycubed/software/blob/master/mainboard-v05/lib/bitflags.py)
[adm1176](https://github.com/pycubed/software/blob/master/mainboard-v05/lib/adm1176.py)

[pycubed](https://github.com/pycubed/library_pycubed.py)
[tasko](https://github.com/aramcon-badge/tasko)
[pycubed_rfm9x](https://github.com/pycubed/library_pycubed_rfm9x.py)

Recommend you copy the entire lib folder from mainboard-v05 then replace `tasko`, `pycubed`, and `pycubed_rfm9x`

For copyright and licensing reasons, do not commit any of these libraries into this repo unless you want to go through each original repo by hand and make sure each license is listed. I don't want to get a headache doing that, and I trust you don't either.

## To-do

- Get everyone comfortable with CircuitPython's API
- Get main function working (code.py)
- Get a proto-comm system working (via REPL initially)
- Make fake data
- Test software integration with satellite modules (should use dummy circuits for now)
- TASKS:
  - Battery
  - Sensor
  - Orbit
    - Test with fake data
  - Communications 
    - Enable key exchange (for security reasons)
    - Send data and delete confirmed received data 
  - Watchdog
    - Reset if something wrong
  - Update
    - Failsafe, switch back to proven
- Develop transceiver API from scratch to communicate over CAN and AMSAT or whatever (listen to Luke, he understands this better than me)
- Build CircuitPython for new boards

## Deployment
I'll put together a directory tree once everyone's on the same page.
