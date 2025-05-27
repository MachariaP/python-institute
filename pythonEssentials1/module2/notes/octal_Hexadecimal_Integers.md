# Deepening Understanding of Octal and Hexadecimal Integers

## Recap of Octal and Hexadecimal

### Literals:

    - Fixed values in code (e.g., `123`, `"hello"`, `0o123`).
    - Integers literals can be in decimal (base 10), octal (base 8), hexadecimal (base 16)
      or binary (base 2)

### Octal Numbers (Base 8):

    * **Syntax**: Prefixed with `0o` or `0O` (e.g., `0o123`).
    * **Digits**: Only `0` to `7` (e.g., `0o89` is invalid)
    * *Conversion to decimal*: For `0o123`:
        - `1 * 8² + 2 * 8¹ + 3 * 8⁰ = 1 * 64 + 2 * 8 + 3 * 1 = 64 + 16 + 3 = 83`.
        - `print(0o123) outputs `83`.
    * *Use Case*: Common in Unix file permissions (e.g., `0o755` for `rwxr-xr-x`).

### Hexadecimal Numbers (Base 16):

    * **Syntax**: Prefixed with `0x` or `0X` (e.g., `0x123`).
    * **Digits**: `0` to `9` and `A` to `F` (or `a` to `f`, where `A/a=10`, `F/f=15`).
    * *Conversion to Decimal*: For `0x123`:
        - `1 * 16² + 2 * 16¹ + 3 * 16⁰ = 1 * 256 + 2 * 16 + 3 * 1 = 256 + 32 + 3 = 291`.
        - `print(0x123)` outputs `291`.
    * *Use Case*: Used for memory addresses, color codes (e.g., `0xFF0000` for red), and bitwise operations.
