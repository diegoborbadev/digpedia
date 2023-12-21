import os

if __name__ == "__main__":
    for root, dirs, files in os.walk('.'):
        if root.startswith('.\\.'):
            continue
        
        summary_file_path = f'{root}/Summary.md'
        with open(summary_file_path, "w") as summary_file:
            summary_file.write("# Summary\n\n")

            for dir in dirs:
                if not dir.startswith('.'):
                    summary_file.write(f"- [{dir}]({dir}/Summary.md)\n")
            
            for file in files:
                if not (file == 'Summary.md' or file == 'Script.py'):
                    summary_file.write(f"- [{file}]({file})\n")