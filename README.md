# xcli

The official Xedix versioning cli tool.
A lightweight version control system implemented in Python.

## How to use

1. Download the source

2. Navigate to the folder in the terminal

3. run `cd back`

4. run `python3 xedix.init.py`

- Enter the files you are changing
- Enter commit message
- Make changes

5. Check the changes

- run `cd ..`
- run `cd front`
- open the `index.html`

## Installation

```bash
git clone "https://github.com/mostypc123/xedix-versioning-system"
pip install .
```

## Usage

After installation, you can use the `xvs` command:

```bash
xvs branch main                            # Switch to or create 'main' branch
xvs commit "file1.txt" "Initial commit"    # Commit changes
xvs stage "file1.txt" "Work in progress"   # Stage changes
xvs init
xvs status
```
