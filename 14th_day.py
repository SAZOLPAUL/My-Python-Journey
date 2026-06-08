# ==========================================
# PYTHON FILE HANDLING - COMPLETE EXAMPLE
# ==========================================

# ------------------------------------------
# 1. CREATE / OVERWRITE A FILE
# ------------------------------------------

with open("source.txt", "w") as file:
    file.write("Hello World\n")
    file.write("Python File Handling\n")
    file.write("Learning is fun!\n")

print("File Created Successfully!\n")


# ------------------------------------------
# 2. READ WHOLE FILE
# ------------------------------------------

print("===== read() =====")

with open("source.txt", "r") as file:
    content = file.read()
    print(content)


# ------------------------------------------
# 3. READ FIRST LINE
# ------------------------------------------

print("===== readline() =====")

with open("source.txt", "r") as file:
    first_line = file.readline()
    print(first_line)


# ------------------------------------------
# 4. READ ALL LINES AS A LIST
# ------------------------------------------

print("===== readlines() =====")

with open("source.txt", "r") as file:
    lines = file.readlines()
    print(lines)


# ------------------------------------------
# 5. READ FILE LINE BY LINE
# ------------------------------------------

print("===== for loop =====")

with open("source.txt", "r") as file:
    for line in file:
        print(line, end="")


# ------------------------------------------
# 6. APPEND DATA
# ------------------------------------------

with open("source.txt", "a") as file:
    file.write("\nThis line was appended.")
    file.write("\nAppending does not remove old data.")

print("\n\nAppend Completed!")


# ------------------------------------------
# 7. WRITE MULTIPLE LINES
# ------------------------------------------

extra_lines = [
    "\nFirst Extra Line",
    "\nSecond Extra Line",
    "\nThird Extra Line"
]

with open("source.txt", "a") as file:
    file.writelines(extra_lines)

print("Multiple Lines Added!")


# ------------------------------------------
# 8. CHECK FINAL CONTENT
# ------------------------------------------

print("\n===== Final File Content =====")

with open("source.txt", "r") as file:
    print(file.read())


# ------------------------------------------
# 9. BINARY FILE WRITE
# ------------------------------------------

with open("binary_file.bin", "wb") as file:
    file.write(b"Hello Binary World")

print("Binary File Created!")


# ------------------------------------------
# 10. BINARY FILE READ
# ------------------------------------------

print("\n===== Binary Read =====")

with open("binary_file.bin", "rb") as file:
    data = file.read()
    print(data)


# ------------------------------------------
# 11. EXCEPTION HANDLING
# ------------------------------------------

print("\n===== Error Handling =====")

try:
    with open("not_found.txt", "r") as file:
        print(file.read())

except FileNotFoundError:
    print("File does not exist!")

except Exception as e:
    print("Something went wrong:", e)


# ------------------------------------------
# 12. FILE INFORMATION
# ------------------------------------------

with open("source.txt", "r") as file:
    print("\n===== File Info =====")
    print("File Name :", file.name)
    print("Mode      :", file.mode)
    print("Closed?   :", file.closed)

print("Closed After Block :", file.closed)