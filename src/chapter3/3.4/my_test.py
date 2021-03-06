from my_debugger import *

debugger = Debugger()

pid = input("Enter the PID of the process to attach to: ")
debugger.attach(int(pid))

printf_address = debugger.func_resolve(b"msvcrt.dll", b"printf")

print("[*] Address of printf: 0x{0:X}".format(printf_address))

#debugger.bp_set(printf_address)
#debugger.bp_set_hw(printf_address, 1, HW_EXECUTE)
debugger.bp_set_mem(printf_address, 1)
debugger.run()