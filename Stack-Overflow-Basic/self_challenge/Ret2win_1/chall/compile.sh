#!/bin/bash

rm -f ret2win
gcc -no-pie -m32 -o ret2win ret2win.c > /dev/null 2>&1
checksec --file=ret2win