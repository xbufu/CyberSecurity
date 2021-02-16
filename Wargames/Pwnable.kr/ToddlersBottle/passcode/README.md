* In function login() we get segfault because author did not use & to load address of variables passcode1 and passcode2 but used the actual values themselves as addresses

* We also have a possible overflow in the welcome() function since it uses scanf() and we can enter as many characters as we want

* We can overflow from the name variable into the initial value of the passcode1 variable

* Address of name variable: ebp-0x70

* Address of passcode1: ebp-0x10

* 0x70 - 0x10 = 96

* Our offset is 96 characters. Anything after that gets written into passcode1

* Since the author did not use &passcode1 to get the actual address of the variable, the initial value of passcode1 (which we control) gets treated as an address

* What we give scanf() as input will be the contents of the memory location we choose

* To exploit this, we can chose the address of another function in the program and have that function point to anything we want

* We overwrite the contents of fflush() in the GOT

* In our case, we point it to the location of the system function that gets us our flag

* We can get the address of a function from the GOT by either stepping into it in GDB or using objdump 

* Address of fflush():	0x804a004

* Address of system function: 0x080485e3 = 134514147

* We need the decimal value of the system function since it will get converted to hex when we store it in memory

* We send our 96 character offset + address of fflush() + int value of system function
