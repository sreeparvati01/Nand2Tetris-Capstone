# Nand2Tetris Capstone Project
## Make the Computer Draw a Box

**Student Name:** Sree Parvati  
**University Roll Number:** 2501730236  
**Personal Number (K):** 36

---

## Project Overview

This project demonstrates the working of the Hack Computer through hardware implementation, assembly programming and machine-code generation. It includes a Python-based assembler and an assembly program designed to draw a rectangular box on the Hack computer screen.

## Box Specifications

| Parameter | Value |
|---|---|
| Starting Row | 36 |
| Box Width | 16 pixels |
| Box Height | 20 rows |
| Starting Screen Address | 17536 |

## Technologies Used

- Hack Assembly Language
- Hardware Description Language (HDL)
- Python
- Nand2Tetris Hardware Simulator
- Nand2Tetris CPU Emulator

## Project Structure

```text
Nand2Tetris-Capstone/
│
├── CPU.hdl
├── Memory.hdl
├── Computer.hdl
├── assembler.py
├── Box.asm
├── Box.hack
├── symbols.txt
├── REPORT_FINAL.md
├── README.md
│
└── Screenshots/
    ├── Box.asm source code
    ├── Box.hack machine code
    ├── CPU Emulator
    └── Final output
```

## Assemble the Box Program

Run the following command from the project directory:

```bash
python assembler.py Box.asm
```

This generates:

- `Box.hack` – Binary machine-code output.
- `symbols.txt` – Exported labels and variables with their addresses.

## Additional Feature

The project includes a K-specific assembler feature that exports labels and variables into `symbols.txt`.

Since K = 36:

**36 mod 3 = 0**

Therefore, the symbol table export feature is included.

## Project Documentation

Refer to `REPORT_FINAL.md` for the detailed project description, implementation details, testing information and verification evidence.

## Author

**Sree Parvati**  
University Roll Number: 2501730236
