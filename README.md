# PeginWN

Welcome to PeginWN! This repository is dedicated to those who are beginning their journey into the world of binary exploitation. Here, you'll find resources, examples, and exercises to help you understand the basics of pwn and binary exploitation.

## About this Repository

This repository aims to provide a structured path for beginners to get started with binary exploitation. It covers basic concepts, common vulnerabilities, and provides practical examples to test your skills.

## Table of Contents

- [PeginWN](#peginwn)
  - [About this Repository](#about-this-repository)
  - [Table of Contents](#table-of-contents)
  - [Getting Started](#getting-started)
  - [Resources](#resources)
  - [List of Vulnerabilities](#list-of-vulnerabilities)
  - [Exercises](#exercises)
  - [Contributing](#contributing)

## Getting Started

To get started with binary exploitation, you will need to set up your environment with the necessary tools. Here is a basic list of tools you might find useful:

- **GDB**: The GNU Project Debugger
- **pwntools**: A CTF framework and exploit development library
- **Binary Ninja / IDA Pro / Ghidra**: Binary analysis tools
- **gef, pwndbg, or peda**: GDB plug-ins to enhance the debugging output

You can install pwntools with pip:
`pip install pwntools`

## Resources

This section provides links to tutorials, books, and websites where you can learn more about binary exploitation:
- [LiveOverflow Binary Exploitation Playlist](https://www.youtube.com/watch?v=iyAyN3GFM7A&list=PLhixgUqwRTjxglIswKp9mpkfPNfHkzyeN)
- "Hacking: The Art of Exploitation" by Jon Erickson
- [pwn.college](https://pwn.college/)
- [Root-me:App-System](https://www.root-me.org/en/Challenges/App-System/)
- [pwnable.kr](https://pwnable.kr/)
- [pwnable.tw](https://pwnable.tw/)

## List of Vulnerabilities

Here's a list of common vulnerabilities you'll learn about in this repository:

| Vulnerability Type                | Description                                                                                                                                           | Link                                   |
|-----------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------|
| Buffer Overflow                   | Occurs when data exceeds the buffer's boundary and overwrites adjacent memory.                                                                      | [Link](./Stack-Overflow-Basic/)        |
| Format String                     | Exploits involving the misuse of the format string functions like `printf`.                                                                         | [Link](./Format-String/)               |
| Integer Overflow                  | Happens when an arithmetic operation attempts to create a numeric value that is outside the range that can be represented with a given number of digits.| [Link](./Integer-Overflow/)            |
| Use After Free                    | Accessing memory after it has been freed, which can lead to arbitrary code execution.                                                                | [Link](./Use-After-Free/)              |
| Heap Overflow                     | Similar to buffer overflow but occurs in the heap memory, allowing attackers to overwrite important data structures.                                  | [Link](./Heap-Overflow/)               |
| Double Free                       | The program frees the same memory location twice, which can lead to memory corruption and arbitrary code execution.                                   | [Link](./Double-Free/)                  |
| Return Oriented Programming (ROP) | A technique that allows an attacker to execute code by chaining together small sequences of instructions already present in the binary.                | [Link](./ROP/)                          |
| Stack Canary Bypass               | Techniques used to bypass stack canaries, which are used to detect buffer overflows on the stack.                                                    | [Link](./Stack-Canary-Bypass/)          |
| Arbitrary Write                   | Allows an attacker to write data to an arbitrary location in memory, which can be exploited to modify program behavior or execute code.                 | [Link](./Arbitrary-Write/)              |
| Type Confusion                    | Occurs when a program mistakenly treats a piece of data as a different type, leading to unexpected behavior or vulnerabilities.                        | [Link](./Type-Confusion/)               |
| Uninitialized Memory Read         | Reading from memory that has not been initialized, which can leak sensitive information or cause undefined behavior.                                     | [Link](./Uninitialized-Memory-Read/)    |
| Null Byte Injection               | Inserting null bytes (`\x00`) into inputs to manipulate string handling functions and potentially bypass security checks.                              | [Link](./Null-Byte-Injection/)          |
| Memory Leak                       | Occurs when a program fails to release memory that is no longer needed, potentially leading to resource exhaustion and other issues.                      | [Link](./Memory-Leak/)                   |
| Race Conditions                   | Exploiting the timing of actions in concurrent environments to cause unexpected behavior or gain unauthorized access.                                   | [Link](./Race-Conditions/)               |
| Stack Smashing                    | A specific type of buffer overflow that targets the stack, potentially allowing attackers to overwrite return addresses and execute arbitrary code.       | [Link](./Stack-Smashing/)                |
| Command Injection                 | Although more common in web applications, command injection can also occur in binary applications if user input is improperly handled and passed to system commands.| [Link](./Command-Injection/)            |
| Shellcode                 | Shellcode | [Link](./Shellcode/) |

## Exercises

We provide a set of exercises to practice your skills. Each exercise comes with a challenge binary and a solution write-up.

## Contributing

Contributions are welcome! If you have any exercises, resources, or improvements, please feel free to fork the repository and submit a pull request.

We appreciate any contributions that help make this a valuable resource for everyone starting in binary exploitation.
