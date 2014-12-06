#!/bin/bash
useradd -m -d /home/$1 -s /bin/bash -U $1
echo -e "$2\n$2" | passwd $1
/usr/bin/supervisord -n
