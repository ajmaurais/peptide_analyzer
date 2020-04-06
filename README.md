# peptide_analyzer
An example project to teach common proteomics data analysis tasks.

The finished proigram reads a `tsv` file containing UniProt IDs, and peptide sequences and outputs a file with,
the peptide formula, mass, modified residue numbers, and protein GO function, and subcelluar location.

__Input__

| ID     | seq
| ------ | ------ |
| P26641 | FPEELTQTFMSC\*NLITGMFQR |
| Q9NTZ6 | VC\*AHITNIPFSITK |
| P19012 | AGLENSLAETEC\*R |
| P42224 | HLLPLWNDGC\*IMGFISK |
| Q15257 | QSVSC\*DEC\*IPLPR |
| P30041 | DFTPVC\*TTELGR |

__Output__

| ID | seq | formula | mass | modified residues | go fxn | subcelluar loc |
| ------ | ------ | ------ | ------ | ------ | ------ | ------ |
| P26641 | FPEELTQTFMSC\*NLITGMFQR | C136H208O37N34S3 | 3005.4609 | C339 | cadherin binding, ... | no\_annotated\_location |
| Q9NTZ6 | VC\*AHITNIPFSITK | C96H153O23N25S | 2056.12974 | C545 | RNA binding | nucleus |
| P19012 | AGLENSLAETEC\*R | C81H132O27N24S | 1904.94188 | C355 | scaffold protein binding, ... | no\_annotated\_location |
| P42224 | HLLPLWNDGC\*IMGFISK | C116H177O26N29S2 | 2456.28674 | C577 | cadherin binding, ... | nucleus, cytoplasm |
| Q15257 | QSVSC\*DEC\*IPLPR | C111H177O29N31S2 | 2472.27761 | C91\|C94 | ATP binding, ... | nucleus, cytoplasm |
| P30041 | DFTPVC\*TTELGR | C83H130O24N22S | 1850.93535 | C47 | cadherin binding, ... | lysosome, cytoplasm |

## Prerequisites

* The Software Carpentry [python course](http://swcarpentry.github.io/python-novice-inflammation/index.html)
* You should know how to read and acess data in [pandas.DataFrame(s)](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html). See the DataFrames section in the [Plotting and Programming in Python course](http://swcarpentry.github.io/python-novice-gapminder/07-reading-tabular/index.html).
* In addition to [lists](https://docs.python.org/3/tutorial/introduction.html#lists), you should be farmiluar with other standard python containsers including, [dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries), and [sets](https://docs.python.org/3/tutorial/datastructures.html#sets). 
    * These YouTube videos on [sets and lists](https://www.youtube.com/watch?v=W8KRzm-HUcc), and [dictionaries](https://www.youtube.com/watch?v=daefaLgNkw0) are a good place to start.
* You don't have to use them in your own code, but in many of my examples I use [list comprehensions](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions).
    * Corey Schafer also has a good [video](https://www.youtube.com/watch?v=3dt4OGnU5sM) about them.

## Project structure

```bash
./LICENSE   ./README.md

./data:
input_peptides.tsv  output_peptides.tsv residue_atoms.txt

./complete:
biopython_lite/       molecular_formula.py uniprot.py
main.py              tests/

./template:
biopython_lite/       molecular_formula.py uniprot.py
main.py              tests/
```

* `data` has the program input files.
* There are 2 subdirectories with python soure files.
    * `complete` contains the working proigram described above.
    * `template` has the same structure as `complete` except the code in the body of functions has been deleted.
* There are comments and docstrings in the `main.py`, `molecular_formula.py`, and `uniprot.py` files which describe what the code should do in each part.
* Your task is to fill in the python code so the program will function as described.
    * For now, all the functions in the program you have to implement will raise a `NotImplementedError` if they are called.
    * You should delete that part when you fill in your own code.

## Setup

* [Download](https://github.com/ajmaurais/peptide_analyzer/archive/master.zip) the repository and unzip the .zip archive.
    * You can also clone the git repo instead if you have git installed on your computer.
* Open `Spyder` and create a new project for `peptide_analyzer`.
    * Go to `Projects -> New Project`
    * Select `Existing directory` and add the path to 

* Once you have loaded the project in `Spyder`, you will want run the program and import funcions you have written in Spyder's `ipython` console.
* There are two things you have to do first so everything will work properly.

1. Tell `ipython` to reload your code every time it has changed. Otherwise you would have to restart `ipython` every time you make changes.
    
    ```python
    # In the ipython console
    %load_ext autoreload
    %autoreload 2
    ```
    
2. Add your `template` directory to your python path so the interpreter can find your code. Otherwise you will get errors.
    
    ```python
    # In the ipython console
    import sys
    sys.path.append('./template')
    ```

* You can run the entire program,

    ```python
    %run template/main.py
    ```

* or you can import your functions and test them from the console.

    ```python
    import molecular_formula
    molecular_formula.read_atom_count_table(ATOM_COUNT_TABLE_PATH)
    ```

* The functions that you have to implement, in the order they shoud be called from `main.py` are:
    * `molecular_formula.read_atom_count_table`
    * `molecular_formula.calc_formula`
    * `molecular_formula.format_formula`
    * `molecular_formula.calc_mass`
    * `uniprot.get_unipror_record`
    * `uniprot.get_modified_residue_numbers`
    * `uniprot.get_go_fxn`
    * `uniprot.remove_braces`
    * `uniprot.get_protein_location`

* For each function, I have kindly provided a unit test.
    * The purpose of unit tests in software development is to test idividual parts of code with edge test cases, before they are integrated into the larger project.
    * You can run a test from the `ipython` console by calling: `%run template/tests/test_<function_name>.py`

    __Example__

    ```python
    %run template/tests/test_read_atom_count_table.py
    ```
