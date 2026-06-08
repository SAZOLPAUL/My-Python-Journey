import os

# Current working directory
print("Current Directory:")
print(os.getcwd())

# List files and folders
print("\nFiles and Folders:")
print(os.listdir())

# Create a folder
os.mkdir("MyFolder")
print("\nFolder Created!")

# Check if a file exists
print("\nFile Exists:")
print(os.path.exists("source.txt"))

# Check if it's a file
print("\nIs File:")
print(os.path.isfile("source.txt"))

# Check if it's a folder
print("\nIs Directory:")
print(os.path.isdir("MyFolder"))

# Absolute path
print("\nAbsolute Path:")
print(os.path.abspath("source.txt"))

# File size
if os.path.exists("source.txt"):
    print("\nFile Size:")
    print(os.path.getsize("source.txt"), "bytes")

# Split filename and extension
name, ext = os.path.splitext("photo.jpg")

print("\nFile Name:", name)
print("Extension:", ext)

# Join paths
path = os.path.join("Documents", "Python", "test.py")

print("\nJoined Path:")
print(path)

# Directory name
print("\nDirectory:")
print(os.path.dirname(path))

# Base name
print("\nFile Name:")
print(os.path.basename(path))