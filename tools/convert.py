import argparse
import nbformat as nbf
import re  # Import the "re" module

def convert_markdown_to_notebook(markdown_file, output_notebook):
    with open(markdown_file, 'r') as md_file:
        markdown_content = md_file.read()

    # Split the Markdown content at headers of any level (e.g., ##, ###, ####, etc.)
    sections = re.split(r'(#+\s.+)', markdown_content)[1:]

    # Create a new Jupyter Notebook
    nb = nbf.v4.new_notebook()

    # Process each section
    for section_title, section_content in zip(sections[::2], sections[1::2]):
        # Create a Markdown cell with the section title followed by the section content
        cell_content = section_title + section_content
        cell = nbf.v4.new_markdown_cell(cell_content)
        nb.cells.append(cell)

    # Write the Notebook to the output file
    nbf.write(nb, output_notebook)

def main():
    parser = argparse.ArgumentParser(description="Convert Markdown file to Jupyter Notebook with sections as cells.")
    parser.add_argument("markdown_file", help="Input Markdown file with sections.")
    parser.add_argument("output_notebook", help="Output Jupyter Notebook file.")
    args = parser.parse_args()

    convert_markdown_to_notebook(args.markdown_file, args.output_notebook)
    print(f"Converted {args.markdown_file} to {args.output_notebook}")

if __name__ == "__main__":
    main()
