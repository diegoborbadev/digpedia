import os

# IMPORTANT: This script only works in linux systems
if __name__ == "__main__":
    # Walk through all directories and files
    for root, dirs, files in os.walk('.', topdown=True):
        # Ignore hidden directories
        if root.startswith('./.'):
            continue

        # Filepath to summary file
        summary_file_path = f'{root}/Summary.md'
        with open(summary_file_path, "w") as summary_file:
            # Add title
            summary_file.write("# Summary\n\n")

            # Check if README.md is in files
            if 'README.md' in files:
                # Bring README to the front
                files.insert(0, files.pop(files.index('README.md')))

            # Add files to summary
            for file in sorted(files):
                # Ignore specific files
                if not (file == 'Summary.md' or file == 'Script.py'):
                    # Remove extension
                    filename = os.path.splitext(file)[0]

                    # Replace underscores with spaces
                    filename = filename.replace('_', ' ')

                    # Add to summary
                    summary_file.write(f"- [*{filename}*]({file})\n")

            # Add directories to summary
            for dir in sorted(dirs):
                # Ignore hidden directories
                if not dir.startswith('.'):
                    # Add to summary
                    summary_file.write(f"- [***{dir.replace('_', ' ')}***]({dir}/Summary.md)\n")