# Table of contents

* [gcc](#gcc)
* [readelf](#readelf)
* [gdb](#gdb)
* [objdump](#objdump)
* [Pwntools](#pwntools)
   * [Basics](#basics)
   * [Debugging](#debugging)
   * [ELF](#elf)
   * [ROP](#rop)

# gcc

- Preprocessing

	`gcc -E`

- Compiling

	`gcc -S -masm=intel`

- Assembly

	`gcc -c`

# readelf

- Dump all information:

	`readelf -a`

- File/ELF header:

	`readelf -h`

- Program headers:

	`readelf -l`

- Section headers:

	`readelf -S`

- Symbol table:

	`readelf -s`
	
# gdb

You can shorten the commands to the starting letter most of the time if it does not conflict with another command

- Execute/restart program
	
	`run`

- Continue to next breakpoint

	`continue`

- Set breakpoint at given function/address. Prefix memory addresses with `*`, e.g. `b *0x56789`

	`break`

- Step forward one line/instruction, stepping into function calls

	`stepi`

- Step forward one line/instruction, stepping over functions calls

	`nexti`

- Set values for variables or registers. Prefix register with `*`. Tip: set $rip to jump anywhere you want in the code

	`set`

- Examine content of memory location and print it in specified format (like C). Add `w` for 32-bit value or `g` for 64-bit.

	`x/<format><size> <address>`

- Print variable

	`print`

- Print disassembly of given function/location

	`disassemble`

- Print current stack of function calls

	`where`

- Run until current function ends

	`fin`

- Print process mappings. Where are is everything loaded for our program located?

	`info proc mappings`

- Start program and stop after first instruction

	`starti`
	
- Show all functions loaded for program

	`info functions`

- Show all functions relevant to current file

	`info file`
	
- Print information about stack frames

	`bt`
	
- Print information about the current frame

	`info frame`
	
- Print arguments of current frame

	`info args`
	
- Print local variables of current frame

	`info locals`
	
- Print parts of current source file

	`list`
	
- Display expression every time program stop

	`display/format expression`
	
- Print names and values of current registers

	`info registers`
	
- Print location information for given symbol

	`info address`
	
- Print symbol at given address

	`info symbol`
	
- Print variables defined outside of functions

	`info variables`
	
# objdump

- Print all symbols

	`objdump -t`
	
- Print all dynamic relocations/functions in GOT

	`objdump -R`

# Pwntools

## Basics

- Open local process

	`p = process(<PROCESS>)`

- Open remote process

	`r = remote(<IP>, <PORT>)`

- Write to process

	`p.send(message)`

	`p.sendline(line)`

	`p.sendlineafter(<DELIMITER>, line)`

- Read from process

	`p.recv()`

	`p.recvline()`

	`p.recvuntil(<DELIMITER>)`

	`p.recvall()`

- Manual control

	`p.interactive()`

- Set architecture for script

	`context.arch = <ARCH>`

- Pack value for 32/64-bit little endian

	`x = p32(<VALUE>)`

	`y = p64(<VALUE>)`

- Pack value for 32/64-bit big endian

	`x = p32(<VALUE>, endian='big')`

	`y = p64(<VALUE>, endian='big')`
	
## Debugging

- Set context of terminal to tmux and split the window 

	`context.terminal = ['tmux', 'splitw', '-h']`
	
- Attach gdb and break at main

	`gdb.attach(p, 'b main')`

## ELF

- Create ELF object

	`binary = ELF(<BINARY>)`

- Get address of symbol

	`foo = p64(binary.symbols[<SYMBOL>])`

- Search binary for string

	`binary.search(b'<STRING>')`

## ROP

- Create ROP object

	`rop = ROP(<BINARY>)`

- Dump ROP gadgets

	`rop.dump()`

- Call function

	`rop.call(<FUNCTION>, <ARGS>)	# Arguments are integer values for pointers to strings`

	`rop.chain()`
