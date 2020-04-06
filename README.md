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
