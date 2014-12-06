#!/bin/bash
useradd -m -d /recruit -s /bin/bash -g sudo $USER
echo -e "$PASS\n$PASS" | passwd $USER
/usr/bin/supervisord -n
