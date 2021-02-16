* As soon as we see the use of `gets()` function we know we have a buffer overflow

* The variable we want to overwrite is `key`

* We can get the offset by examining the stack

* We find that we need a padding of 52 characters

* After that we can put the value we want to write in order to get the flag
