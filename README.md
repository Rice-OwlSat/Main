# Main

The Recoding Effort!

## Compiling for CircuitPython
You'll have to build mpy-cross yourself on a Unix shell (for Windows users I recommend WSL2) from the [CircuitPython](https://github.com/adafruit/circuitpython/) version loaded onto the board. Load the compiled bytecode `.mpy` files onto the board, reset the kernel (^C, ^D inside the REPL console), and make sure the module is valid by running `import module-name-here` in the REPL terminal. If it says nothing, you're good to go.
Any other version of mpy-cross generates a bad mpy file.
