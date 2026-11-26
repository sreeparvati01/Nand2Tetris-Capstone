#!/usr/bin/env python3
"""Hack assembler: .asm -> .hack
Usage: python assembler.py Prog.asm
Extra feature (K mod 3 == 0): writes all labels and variables to symbols.txt
"""
import sys

COMP = {
    "0": "0101010", "1": "0111111", "-1": "0111010",
    "D": "0001100", "A": "0110000", "!D": "0001101", "!A": "0110001",
    "-D": "0001111", "-A": "0110011", "D+1": "0011111", "A+1": "0110111",
    "D-1": "0001110", "A-1": "0110010", "D+A": "0000010", "D-A": "0010011",
    "A-D": "0000111", "D&A": "0000000", "D|A": "0010101",
    "M": "1110000", "!M": "1110001", "-M": "1110011", "M+1": "1110111",
    "M-1": "1110010", "D+M": "1000010", "D-M": "1010011", "M-D": "1000111",
    "D&M": "1000000", "D|M": "1010101",
}
DEST = {"": "000", "M": "001", "D": "010", "DM": "011",
        "A": "100", "AM": "101", "AD": "110", "ADM": "111"}
JUMP = {"": "000", "JGT": "001", "JEQ": "010", "JGE": "011",
        "JLT": "100", "JNE": "101", "JLE": "110", "JMP": "111"}

PREDEFINED = {"SP": 0, "LCL": 1, "ARG": 2, "THIS": 3, "THAT": 4,
              "SCREEN": 16384, "KBD": 24576}
for i in range(16):
    PREDEFINED["R%d" % i] = i


def norm_dest(d):
    """Accept any letter order: DM, MD, AM, MA, ADM ... -> canonical key."""
    return "".join(c for c in "ADM" if c in d) if d else ""


def norm_comp(c):
    """Accept commutative forms: M+D = D+M, A&D = D&A, A|D = D|A, ..."""
    if c in COMP:
        return c
    for op in "+&|":
        if op in c:
            left, right = c.split(op, 1)
            swapped = right + op + left
            if swapped in COMP:
                return swapped
    return c


def clean(line):
    """Remove comments and all whitespace."""
    return line.split("//")[0].replace(" ", "").replace("\t", "").strip()


def assemble(lines):
    symbols = dict(PREDEFINED)
    labels, variables = {}, {}

    # First pass: labels
    cleaned = []
    for raw in lines:
        line = clean(raw)
        if not line:
            continue
        if line.startswith("(") and line.endswith(")"):
            name = line[1:-1]
            labels[name] = len(cleaned)
            symbols[name] = len(cleaned)
        else:
            cleaned.append(line)

    # Second pass: translate, allocating variables from RAM 16
    next_var = 16
    out = []
    for line in cleaned:
        if line.startswith("@"):
            val = line[1:]
            if val.isdigit():
                addr = int(val)
            else:
                if val not in symbols:
                    symbols[val] = next_var
                    variables[val] = next_var
                    next_var += 1
                addr = symbols[val]
            out.append(format(addr, "016b"))
        else:
            dest, jump = "", ""
            comp = line
            if "=" in comp:
                dest, comp = comp.split("=", 1)
            if ";" in comp:
                comp, jump = comp.split(";", 1)
            out.append("111" + COMP[norm_comp(comp)] + DEST[norm_dest(dest)] + JUMP[jump])
    return out, labels, variables


def main():
    if len(sys.argv) != 2:
        print("Usage: python assembler.py Prog.asm")
        sys.exit(1)
    path = sys.argv[1]
    with open(path) as f:
        lines = f.readlines()

    out, labels, variables = assemble(lines)

    with open(path.rsplit(".", 1)[0] + ".hack", "w") as f:
        f.write("\n".join(out) + "\n")

    # Extra feature for K mod 3 == 0
    with open("symbols.txt", "w") as f:
        for name, addr in sorted(labels.items(), key=lambda x: x[1]):
            f.write("%s\t%d\tlabel\n" % (name, addr))
        for name, addr in sorted(variables.items(), key=lambda x: x[1]):
            f.write("%s\t%d\tvariable\n" % (name, addr))


if __name__ == "__main__":
    main()
