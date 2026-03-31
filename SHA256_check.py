import hashlib
import os

def sha256sum(filepath):
    h = hashlib.sha256()
    with open(filepath, "rb") as f:
        while chunk := f.read(8192):
            h.update(chunk)
    return h.hexdigest()

file1 = input("Path to first file: ").strip()
file2 = input("Path to second file: ").strip()

for path in (file1, file2):
    if not os.path.exists(path):
        print(f"File not found: {path}")
        exit()

hash1 = sha256sum(file1)
hash2 = sha256sum(file2)

print("\nFile 1 SHA256:", hash1)
print("File 2 SHA256:", hash2)

if hash1 == hash2:
    print("\nSHA256 are identical.")
else:
    print("\nFiles are not identical")
input()
