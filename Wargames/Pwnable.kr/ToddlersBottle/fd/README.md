* We can see that the string in `buf` need to be equal to "LETMEWIN"

* We can see in the instructions before that that the variable gets modified by the read() instruction

* Its first parameter is a file descriptor

* In our case we want this to be 0 to use stdin as input, meaning we can type our input in with the keyboard

* The fd variable is assigned by converting our function argument to an integer and subtracting 0x1234 from it

* If the result is 0 we can simply type in LETMEWIN and get our flag

* 0x1234 is 4660 as an integer so we just need to pass that as an argument we can execute the binary
