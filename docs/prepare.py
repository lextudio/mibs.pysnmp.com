import os
import glob
import re

def new_toc(path = "./mibs"):
    # Get all .rst files in the specified directory, excluding index.rst
    rst_files = glob.glob(os.path.join(path, "*.rst"))
    rst_files = [file for file in rst_files if 'index.rst' not in file]

    # Format the filenames for the toctree
    rst_file_names = ["   " + os.path.splitext(os.path.basename(file))[0] + "\n" for file in sorted(rst_files)]

    # Read the current contents of index.rst
    with open("index.rst.txt", 'r') as file:
        index_content = file.readlines()

    # Find the line number to insert the filenames
    line_number = next(i for i, line in enumerate(index_content) if '.. toctree::' in line)

    # Insert the filenames into the index.rst content
    updated_content = index_content[0:line_number+3] + rst_file_names + index_content[line_number+4:]

    # Write the updated content back to index.rst
    with open(os.path.join(path, "index.rst"), 'w') as file:
        file.write(''.join(updated_content))

def new_rst_files():
    # Get all files in the ..\asn1 directory
    asn1_files = glob.glob("../asn1/*")

    # Read the template content
    with open("./page.rst.txt", 'r') as file:
        template_content = file.read()

    # Create the mibs directory if it does not exist
    if not os.path.exists('./mibs'):
        os.makedirs('./mibs')

    for file in asn1_files:
        # Check if the corresponding .py file exists
        py_file = os.path.join("../pysnmp", os.path.splitext(os.path.basename(file))[0] + ".py")
        if not os.path.exists(py_file):
            continue

        # Set the metadata.module variable to the file name (without the directory)
        metadata_module = os.path.splitext(os.path.basename(file))[0]

        # Replace {{ metadata.module }} in the template with the actual variable value
        rst_content = template_content.replace('{{ metadata.module }}', metadata_module)

        # Write the .rst file
        with open(f"./mibs/{metadata_module}.rst", 'w') as rst_file:
            rst_file.write(rst_content)

# Delete all files in the mibs folder
files = glob.glob('./mibs/*')
for file in files:
    os.remove(file)

new_rst_files()

print("New .rst files created")

new_toc()

print("index.rst updated")
