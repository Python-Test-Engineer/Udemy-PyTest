
## 01 Python Version

I am using 11/12 but much lower versions OK
VS Code

## 02 Virtual Environment

Treat each SECTION as its own project.

I find it best to:
 
- open that say SECTION_05_PROJECTS as root in VS Code
- `python -m venv venv`
- `.\venv\Scripts\activate` (Windows)
- `source venv/bin/activate` (Mac/Linux)
- `pip install -r requirements.txt`

## 03 Editor and extensions

- theme is material theme darker
- extensions rainbow indent
- setting.json
- explorer on right: view > appearance > move primary bar
- font sizes larger for recordings

## 04 Console formatting

- Rich <https://rich.readthedocs.io/en/stable/introduction.html>
- Pyboxen <https://github.com/savioxavier/pyboxen>
- examples in SECTION_O2_ENVIRONEMENT > rich_pyboxen_samples
- colors for Rich/PyBoxen <https://rich.readthedocs.io/en/stable/appendix/colors.html>

## 05 Packages in requirments.txt

We will just need:

- PyTest
- Rich
- Pyboxen

