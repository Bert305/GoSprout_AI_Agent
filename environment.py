# print(".env file created and variables written!")


# Open or create the .gitignore file
with open('.gitignore', 'w') as gitignore_file:
    # Write patterns of files and directories to be ignored by Git
    gitignore_file.write('.env\n')
    gitignore_file.write('__pycache__/\n')
    gitignore_file.write('*.pyc\n')
    gitignore_file.write('node_modules/\n')
    
    # don't forget .venv as well inside .gitignore

print(".gitignore file created and patterns written!")