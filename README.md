# XMI - SPARQL DDL
A python program to convert an xmi file into a ddl file to load into sparql queried databases

# How to
## Create the model
Find some conceptual modeling software (we used genmymodel.com) to build the model and export it as an XMI
## Set up the program
Open up the directory containing the code in the terminal. We used the ply library to do our parsing so make sure that is installed
## Running the program
Once in the directory, type this format into the command line then run it.
```
python main.py fileToConvert.xmi nameOfNewFile
```
## Enjoy your new ddl file
