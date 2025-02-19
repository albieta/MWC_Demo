import nbformat as nbf

script_file = "main4.py"
notebook_file = "main_demo.ipynb"

with open(script_file, "r") as f:
    code = f.read()

nb = nbf.v4.new_notebook()
nb.cells.append(nbf.v4.new_code_cell(code))

with open(notebook_file, "w") as f:
    nbf.write(nb, f)