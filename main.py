import hashlib
import os
import json

# Function to calculate hash of a file
def calculate_hash(file_path, hash_algo='sha256'):
    h = hashlib.new(hash_algo)
    try:
        with open(file_path, 'rb') as f:
            while chunk := f.read(4096):
                h.update(chunk)
        return h.hexdigest()
    except FileNotFoundError:
        return None

# Save hash values to a JSON file
def save_hashes(directory, hash_file='hashes.json'):
    hashes = {}
    for root, _, files in os.walk(directory):
        for file in files:
            full_path = os.path.join(root, file)
            hashes[full_path] = calculate_hash(full_path)
    
    with open(hash_file, 'w') as f:
        json.dump(hashes, f, indent=4)
    print(f"\n Hashes saved to '{hash_file}' for directory: {directory}")

# Check for file changes using saved hashes
def check_integrity(hash_file='hashes.json'):
    if not os.path.exists(hash_file):
        print(" No hash file found. Please run save_hashes() first.")
        return

    with open(hash_file, 'r') as f:
        old_hashes = json.load(f)

    print(f"\n Checking file integrity from '{hash_file}':\n")
    for file_path, old_hash in old_hashes.items():
        current_hash = calculate_hash(file_path)
        if current_hash is None:
            print(f"[DELETED]  {file_path}")
        elif current_hash != old_hash:
            print(f"[MODIFIED] {file_path}")
        else:
            print(f"[OK]       {file_path}")


import kagglehub

# Download the file from kaggle dataset
path = kagglehub.dataset_download("deepcontractor/cyber-security-salaries")

print("Path to dataset files:", path)

# Check file
check_integrity()


