import os
import random
import string

def generate_random_name(length=8):
    """Generate a random name with the given length."""
    return ''.join(random.choices(string.ascii_letters, k=length))

def create_recursive_folders(base_path, depth):
    """Create a recursive folder structure with random names."""
    if depth <= 0:
        return

    max_folders_per_level = random.randint(1, 5)
    current_level_folders = random.randint(1, max_folders_per_level)
    folders = []

    for _ in range(current_level_folders):
        folder_name = generate_random_name()
        folder_path = os.path.join(base_path, folder_name)
        os.mkdir(folder_path)
        print(f"Created folder: {folder_path}")
        folders.append(folder_path)

        create_recursive_folders(folder_path, depth - 1)

    return folders

def create_final_file(destination_folder, content):
    """Create a final destination file with specific content."""
    final_file_path = os.path.join(destination_folder, "flag.txt")
    with open(final_file_path, "w") as file:
        file.write(content)
    print(f"Created final destination file: {final_file_path}")

# Example usage
base_directory = "root_directory"
recursive_depth = 6
final_file_content = "flag{r3curs1ve}"

if not os.path.exists(base_directory):
    os.mkdir(base_directory)

deepest_folders = create_recursive_folders(base_directory, recursive_depth)

# Choose the deepest folder
deepest_folder = max(deepest_folders, key=lambda x: x.count(os.sep))

create_final_file(deepest_folder, final_file_content)
