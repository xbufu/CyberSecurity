* If we check the file with readelf, objdump, file the output is very weird since there is no information at all

* We also get nothing when we open it in GDB

* If we run strings on it and scroll through the output it tells us that the binary was packed with UPX

* After unpacking it we can view the defined strings in ghidra and get our flag
