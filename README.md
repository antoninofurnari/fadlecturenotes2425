# This Repository

This repository contain lecture notes for the Fundamental of Data Analysis course 2023/2024. University of Catania. Prof. Antonino Furnari.

## Creating an Conda Environment

The conda environment is provided as `environment.yml`. This environment is used for all testing by Github Actions and can be setup by:

1. `conda env create -f environment.yml`
2. `conda activate fadlecturenotes

## Building a Jupyter Book

Run the following command in your terminal:

```bash
jb build lecturenotes/
```

If you would like to work with a clean build, you can empty the build folder by running:

```bash
jb clean lecturenotes/
```

If jupyter execution is cached, this command will not delete the cached folder. 

To remove the build folder (including `cached` executables), you can run:

```bash
jb clean --all lecturenotes/
```

## Building a PDF

```bash
jupyter-book build lecturenotes --builder pdflatex
```

## MARP

```bash
mkdir -p lecturenotes/_build/marp; for f in lecturenotes/slides/*.md; do ff=${f/.md/.pdf}; marp $f --pdf --allow-local-files -o lecturenotes/_build/marp/$(basename $ff); done
```

## Publishing this Jupyter Book

This repository is published automatically to `gh-pages` upon `push` to the `master` branch.

## Notes

This repository is used as a test case for [jupyter-book](https://github.com/executablebooks/jupyter-book) and 
a `requirements.txt` file is provided to support this `CI` application.