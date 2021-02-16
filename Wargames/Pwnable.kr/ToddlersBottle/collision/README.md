* To get our flag the return value of the `check_password` function needs to be `0x21DD09EC`

* If we check the function we see that it converts the string, which is actually just a character pointer, to an integer pointer

* Then it iterates over it and adds to contents at the current location to the `res` variable

* The important parts here are the conversion between the pointers and the length of the entered passcode compared to the loop length

* Our string is 20 characters or bytes long but the loop only iterates 5 times

* This is because a character is only 1 byte with an integer is 4 bytes big

* When converting the `char *` to an `int *` it tells the computer to interpret 4 bytes of the string as a single integer, meaning that the first 4 characters are the first number, so next 4 bytes the second number and so on

* Characters are stored in memory as their hex representations, so if you wanted to store the string ABC in memory it would look like this

	`0x434241`

* Note that `A = 0x41`, `B = 0x42` and `C = 0x43` 

* You can see that it is stored in little endian format or just in reverse order

* You can check which format a binary uses to store data by using `readelf -h`

* So we need to input a specific sequence of characters that when interpreted as chunks of 4 bytes, stored in little endian, sum up to the hex value `0x21DD09EC`

* An easy way to calculate this is to simply divide that value by 5

	`0x21DD09EC / 5 = 0x6C5CEC8 = 113626824`

* If we check if that divided evenly we see that it did not

	`0x21DD09EC % 5 = 4`

* This means that we need to enter `0x6C5CEC8` 4 times and for the 5th part we simply need to subtract 4 from that so our last number will be `0x6C5CECC`

* Don't forget to send the input in reverse order because of little endian and we get our flag
