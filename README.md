# Shockley-Queisser-Calculator
A Shockley-Queisser calculator for calculating theoretical efficiencies of solar cells with an interactive user interface.

[DOWNLOAD](https://github.com/SarthakJariwala/Schokley-Queisser-Calculator/releases)

## Features
* Calculate Shockley Queisser efficiency limit and related parameters for a given bandgap, temperature and solar spectrum
* Plot SQ limit J-V curve for a given bandgap of the solar cell
* Plot power conversion efficiency, fill factor, current density, and open-circuit voltage as a function of different bandgaps
* Can export calculated PCE, Voc, FF, Jsc for an array of bandgaps (new in v1.0.1)
* Can also use SMARTS spectrum output (wavelength and global tilted irradiance must be first and second column respectively)

## How to contribute/develop?
### Basic setup
* Create a new python environment. 
    * If you are using Anaconda or Miniconda 
        * `conda create --name sq python=3.6` 
        * `conda activate sq`
    * Alternatively, you can also create a virtual environment using `venv`.
        * Run `python -m venv sq` 
        * On Windows - `cd sq\Scripts\` and `activate` or `activate.bat`
        * On Mac - `cd sq\bin` and `activate`
* Install dependencies 
    * Run `pip install -r requirements.txt`
### Run Shockley-Queisser Calculator from command line
* `fbs run`
* Make changes to the code and check if it works
### *Freeze* the application and create an installer
* `fbs freeze` - this will create a _frozen_ version of your code
* `fbs installer` - this will create an installer for your application
* Depending on your operating system, the above commands will create an application and installer for that operating system. For example, if you do it on a Mac, you will get an application and installer for Mac.
### Once you have created an installer, you can share it with your users. You can submit a pull request with your changes.
