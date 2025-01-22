#!/bin/sh

rm -f guide_2

gcc -o guide_2 guide_2.c > /dev/null 2>&1

checksec --file=guide_2