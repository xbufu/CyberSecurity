# Table of content

* [Computer organization](#computer-organization)
    * [Register names](#register-names)
        * [64-bit](#64-bit)
        * [32-bit](#32-bit)
        * [16-bit](#16-bit)
    * [Calling convention/ABI:](#calling-conventionabi)
    * [General information about binaries](#general-information-about-binaries)
        * [Program headers](#program-headers)
        * [Section headers](#section-headers)
    *  [System calls](#system-calls)
    * [Interpreter](#interpreter)
    * [Program images](#program-images)
    * [Stack frames](#stack-frames)
* [Binary Exploitation](#binary-exploitation)
    * [Types of vulnerabilites](#types-of-vulnerabilites)
    * [Defense mechanisms](#defense-mechanisms)
    * [Defeating ASLR and PIE](#defeating-aslr-and-pie)

# Computer organization

## Register names

### 64-bit

`rax`
	
### 32-bit

`eax`
	
### 16-bit

- Higher 16-bits

	`ah`
	
- Lower 16-bits

	`al`

## Calling convention/ABI:

- Arguments to functions are passed in order to the following registers:

	`rdi rsi rdx rcx r8 r9`

- Additional arguments are pushed onto the stack

- Return values are returned in rax

- Functions must preserve

	`rbx rsp rbp r12-15`


## General information about binaries

### Program headers

- LOAD:

	Which parts of the code actually get loaded into memory

- Section:

	Parts of the ELF file while on disk

- Segment:

	Parts of the ELF file while in memory

### Section headers

- .text:

	Instructions the program executes

- .data:

	Initialized data/variables

- .rodata:

	Read-only data (const, defines)

- .bss:

	Data initialized to 0

- .got:

	Global offset tables
	Contains addresses of dynamic functions

- .got.plt:

	Procedure linkage table
	Functions called to either jump to a GOT address or trigger loader to look up dynamic function

## System calls

- Functions provided by kernel

- All processes on Linux need to be forked first then started by exec()

- `fork()`

	Create duplicate process (child) from parent
	Which process defined by return value


## Interpreter

- Will find out where libraries/shared objects needed for functions are located and link them

- When shared libary function is called for the firs time

	- Jump to PLT

	- Stub function in PLT looks up GOT entry for wanted function and jumps to it

	- GOT entry for function is copied as next instruction in PLT

	- Stub function jumps to loader fixup

	- Loader looks up function location and replaces dummy entry in GOT with real entry

	- Loader restarts call to function (jump to PLT)

	- Execution continues normally

	- Loader is not needed anymore for the function

## Program images

- Created when new program is run

- From top-to-bottom in memory:

	- Kernel Memory space (not writeable by user code)

	- Random stack offset (security, ASLR)

	- Program stack:

		- Grows from high to low addresses

		- Used for local variables

	- Random mmap offset (security, ASLR)

	- MMapped segment containing shared libraries used by program

	- Random mmap offset (security, ASLR)

	- Heap

		- Grows from low to high addresses

		- Contains user-managed data

		- e.g. `int x = malloc(sizeof(int));`

		- Data will (usually) stay there unless cleared manually

	- Random brk offset

	- BSS:

		- Amount of uninitialized data

		- `int x; // adds 4 bytes`

	- Data:

		- Amount of initialized data in bytes

		- e.g. `int x = 10; // adds 4 bytes`

	- Text:

		- User-written code

		- Functions

		- Constants

## Stack frames

- Created for each function call

- Program prologue:

	- Save instruction pointer and base pointer on the stack
		
		`push rbp`
		
		`push rip`
		

	- Set base pointer to old stack pointer

		`mov rbp, rsp`

	- Allocate space needed for function call

		`sub rsp, 0x10`

- Program epilogue:

	- First set RBP to previously saved RBP

		`leave`

	- Set instruction pointer to saved instruction pointer

		`ret`


# Binary Exploitation

## Types of vulnerabilites

- Bash/Shell tricks
- Buffer overflows
- Off-by one errors
- Function misuse
- Race conditions
- Input validation

## Defense mechanisms

- ASLR - Address Space Layour Randomization
- PIE - Position Independet Execution
- NX - Non-executable memory
- Stack canaries

## Defeating ASLR and PIE

- The 12 least significant bits do not change since they are from the ELF itself (page alignment)

- Functions in binary are stored close together, so you only need to overwrite the least significant byte of RIP

- Find out addresses of RIP and function you want to execute in gdb

- If there are other variables between the buffer and RIP on the stack, overwrite the least significant byte there with the offset between RIP and the function you want to execute

- Can be brute forced (reasonably) for up to 3 bytes

- Watch out for null bytes!
