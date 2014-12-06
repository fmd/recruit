#!/bin/bash
useradd -m -d /recruit -s /bin/bash -g sudo $1
echo -e "$2\n$2" | passwd $1
/usr/bin/supervisord -n
