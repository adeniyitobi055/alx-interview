# 0x02-minimum_operations

## Question
In a text file, there is a single character `H`. Your text editor can execute only two operations in this file: `Copy All` and `Paste`. Given a number `n`, write a method that calculates the fewest number of operations needed to result in exactly `n` `H` characters in the file.

<ul><li>Prototype: `def minOperations(n)`</li><li>Returns an integer</li><li>If `n` is impossible to achieve, return `0`</li></ul>

**Example:**
`n = 9`

`H` => `Copy All` => `Paste` => `HH` => `Paste` =>`HHH` => `Copy All` => `Paste` => `HHHHHH` => `Paste` => `HHHHHHHHH`

Number of operations: `6`

## Files

Main to test our function: [0-main.py](0-main.py)

Function file: [0-minoperations.py](0-minoperations.py)
