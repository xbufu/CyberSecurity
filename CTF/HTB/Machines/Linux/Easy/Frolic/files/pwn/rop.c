#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>

void vuln(char *argv)
{
	char *buffer[48];

	strcopy(buffer, argv);
	printf("[+] Message sent: ");
	printf("%s\n", argv);

	return;
}

int main(int argc, char *argv[])
{
	setuid(0);

	if(argc < 2)
	{
		puts("[*] Usage: program <message>");
	}
	else
	{
		vuln(argv + 2);
	}

	return 0;
}
