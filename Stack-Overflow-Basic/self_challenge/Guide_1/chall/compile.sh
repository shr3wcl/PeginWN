#!/bin/sh

rm -f guide_1
gcc -o guide_1 guide_1.c > /dev/null 2>&1
checksec --file=guide_1