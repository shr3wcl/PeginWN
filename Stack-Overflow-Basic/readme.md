# Stack Overflow & Related Exploits

A **Stack Overflow** (or **stack-based buffer overflow**) happens when a program writes more data to a buffer on the stack than it can hold, corrupting adjacent memory. This often leads to crashes, unexpected behavior, and in many cases, arbitrary code execution.

## How Does a Stack Overflow Occur?

1. The program allocates a fixed-size buffer (e.g., `char buf[64]`) on the stack.
2. User input is copied into this buffer without proper bounds checking.
3. If the user supplies data exceeding `64` bytes, the overflow overwrites local variables, control data (like saved EIP/RIP), and possibly more.

By manipulating these overwritten values, attackers can hijack the normal flow of execution, potentially gaining full control over the process.

## Common Vulnerabilities & Exploits

Below is a table listing various **stack-based vulnerabilities** or **exploitation techniques** often encountered in security research and Capture the Flag (CTF) challenges.

| **Vulnerability / Exploit**                        | **Description**                                                                                                                                                      | **Cause**                                                                                                                     | **Potential Impact**                                                                                                                                                                       | Link |
|----------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| --- |
| **Basic Stack Overflow**                           | Writing more data into a buffer than it can hold, overwriting adjacent memory.                                                                                       | No boundary checks when copying/reading data into a buffer.                                                                   | Crashes, corruption of variables, overwriting saved return pointers, arbitrary code execution.                                                                                             | [Link](./Variable%20Overwritting/) |
| **Off-by-One Overwrite**                           | A variant of buffer overflow where indexing or size calculations are off by exactly one byte, potentially overwriting a single critical byte on the stack.           | Incorrect loop bounds or usage of string operations (e.g. forgetting the `\0` terminator).                                    | Overwriting stack canaries, return pointers, or null terminators leading to hijacked control flow or crashes.                                                                              | |
| **Stack Canary Bypass**                            | Modern compilers place a "canary" (random value) just before saved EIP/RIP on the stack. If the canary is altered, the program aborts. A bypass is when an attacker can overwrite the canary undetected. | Leakage of canary value (e.g., via format string vulnerability), partial overwrite techniques, or weak canary randomization.   | Once bypassed, attackers can overwrite return addresses and hijack control flow, leading to arbitrary code execution.                                                                       | |
| **Return-to-libc (ret2libc)**                      | Overwrite the return address with the address of a C library function (e.g., `system`). Instead of injecting shellcode, you call existing code in memory.            | Stack overflow that allows overwriting saved return addresses or function pointers.                                           | Execution of existing functions such as `system("/bin/sh")`, potentially escalating privileges or spawning shells.                                                                          | |
| **ROP (Return-Oriented Programming)**              | Chains small code fragments ("gadgets") already present in memory (usually in libraries/executables) to perform arbitrary computation.                               | Full control of the return pointer and knowledge of memory layout to locate and chain gadgets.                                | Powerful method; can bypass DEP/NX by reusing existing code, leading to advanced exploits even on hardened systems.                                                                         | |
| **ret2win**                                        | A CTF-oriented scenario where the binary contains a “win” function (or similar) that gives a flag or spawns a shell. The attacker overwrites the return address to directly jump to that function. | Similar to Return-to-libc: The saved return pointer is overwritten, but the target is a special local function (like `win`) instead of a standard library function. | Grants direct access to a privileged function, revealing flags, spawning shells, or performing secret tasks hidden within the binary.                                                       | [Link](./Return%20Address%20Overwrite/) |
| **ret2shellcode**                                  | Attackers place custom shellcode in a writable/executable region (often on the stack if NX is disabled) and overwrite the return address to jump there.             | Classic stack overflow with an executable stack (or another R/W/X region).                                                    | Arbitrary code execution via attacker-supplied instructions.                                                                                                                               | |
| **ret2csu**                                        | A specialized ROP technique using the `.init_array` section or the “__libc_csu_init” function to set up registers and call functions with controlled parameters.    | Overwrite of return address + knowledge of the compiler-generated function prologues/epilogues in the binary.                 | Allows partial register control, function calls with arguments, and advanced pivoting in limited ROP scenarios.                                                                             | |
| **ret2dlresolve**                                  | Exploit the dynamic linker’s resolve mechanism at runtime to call any library function by forging a fake “reloc” structure on the stack.                            | Ability to write a fake relocation structure and overwrite return addresses to point into dynamic linker routines.            | Bypasses situations where function symbols are not yet resolved or addresses are hidden by ASLR, allowing calls to arbitrary library functions.                                             | |
| **Sigreturn Oriented Programming (SROP)**          | Uses the `sigreturn` system call to set register state arbitrarily, allowing the attacker to craft a desired CPU context upon returning from a signal handler.       | Overwrite the return address with the `syscall` instruction address, arrange stack data to fake a signal frame.              | Full register control, enabling advanced ROP and bypassing certain security controls (e.g., easily setting up `rax` for `execve` system call).                                             | |

## Mitigations

1. **Use Safer Functions**  
   - Avoid unsafe functions like `strcpy`, `sprintf`, `gets`.
   - Use safer alternatives such as `strncpy`, `snprintf`, or explicit bounds checks.

2. **Stack Canaries**  
   - Modern compilers (e.g., `-fstack-protector`) insert a special "canary" value to detect overflows.

3. **Address Space Layout Randomization (ASLR)**  
   - Randomizes the base addresses of the stack, heap, and libraries, making it harder for attackers to guess critical addresses.

4. **Non-Executable Stack (NX / DEP)**  
   - Marks the stack as non-executable, preventing direct shellcode execution from the stack.

5. **Position-Independent Executables (PIE)**  
   - Randomizes the base address of the executable itself, making ROP gadget discovery harder.

6. **Fortify Source**  
   - A compiler feature (`-D_FORTIFY_SOURCE=2`) that adds checks for certain unsafe library functions at runtime.

## References & Further Reading

- [OWASP: Buffer Overflow](https://owasp.org/www-community/vulnerabilities/Buffer_Overflow)
- [MITRE: CWE-121 (Stack-based Buffer Overflow)](https://cwe.mitre.org/data/definitions/121.html)
- [Aleph One: “Smashing The Stack For Fun And Profit”](http://insecure.org/stf/smashstack.html)
- [LiveOverflow YouTube: Binary Exploitation Tutorials](https://www.youtube.com/c/LiveOverflow)

---

**Disclaimer**: All information here is for educational purposes only. Always follow ethical guidelines, and only test or research these techniques in environments where you have explicit permission.
