<!-- PROJECT SHIELDS -->

[![Contributors][contributors-shield]](https://github.com/10Fred10/pasSecure/graphs/contributors)
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]
[![Gmail][gmail-shield]][gmail-url]

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/10Fred10/patternExtractor">
    <img src="https://raw.githubusercontent.com/10Fred10/patternExtractor/master/readme-assets/Motif-Extractor-logo.png" alt="Logo" width="70" height="150">
  </a>

  <h3 align="center">PATTERN EXTRACTOR</h3>

  <p align="center">
    Desktop application to help BioInformatics engineers do N-gram analysis on DNA Sequences
    <br />
    <a href="https://github.com/10Fred10/patternExtractor/raw/master/Motif-Extractor.exe" target="_blank"><strong>« DOWNLOAD »</strong></a>
    <br />
    <br />
    <a href="https://github.com/10Fred10/patternExtractor/issues" target="_blank">Report Bug</a>
    ·
    <a href="https://github.com/10Fred10/patternExtractor/pulls" target="_blank">Request Feature</a>
  </p>
</p>

<!-- TABLE OF CONTENTS -->

Table of Contents | 
------------ |
[About the Project](#about-the-project) |
[Installation](#installation) |
[Usage](#usage) |
[Contact](#contact) |
[Acknowledgements](#acknowledgements) | 


<!-- ABOUT THE PROJECT -->

## About The Project

<p align="center">
  <img  src="https://raw.githubusercontent.com/10Fred10/patternExtractor/master/readme-assets/Motif-Extractor.png">
</p>
<br>

>_This is a project I made in my BioInformatics Class._

A desktop application that splits a genome sequence into words of length k, then generates a `Boolean` | `Frequency` | `Occurence` | `TFIDF` matrix I use later to train a classifier. 

### Built With

<p align="center">
  <img  src="https://raw.githubusercontent.com/10Fred10/patternExtractor/master/readme-assets/used.png">
</p>


- [PYTHON](https://en.wikipedia.org/wiki/Python_(genus)) A genus of constricting snakes in the Pythonidae family living in the Eastern Hemisphere.
- [TKINTER](https://wiki.python.org/moin/TkInter) : _Graphical User Interface package_ | Creates the UI.
- [NLTK](https://www.nltk.org/) : _Natural Language Toolkit_ | Generates the `ngrams`.
- [NUMPY](http://www.numpy.org/) : _Package for scientific computing_ | Helps with N-dimensional array objects.


<!-- GETTING STARTED -->

## Installation

Simply download the `Motif-Extractor.exe` file and run it.

<!-- USAGE EXAMPLES -->

## Usage


<p align="center">
  <img  src="https://raw.githubusercontent.com/10Fred10/patternExtractor/master/readme-assets/Explained.png">
</p>

Fllow the steps mentionned in the UI and you should be fine.

<p align = "center">
  <img  src="https://raw.githubusercontent.com/10Fred10/patternExtractor/master/readme-assets/pattern-gif.gif">
</p>

:bulb: **Input File :**

1. Should be a `.txt` file.
2. First couple of lines should have these points :
   * Number of classes.
   * Number of Sequences in each class.
   * The beginning of a class starting from `0`.

<p align="center">
  <img  src="https://raw.githubusercontent.com/10Fred10/patternExtractor/master/readme-assets/seq-img.png">
</p>

:star: **Output File :**

The output file will be a `.txt` file containing a matrix.

>I could've gone for an `Excel` file here but that won't be a optimal,
we are dealing with **huge** sequences here, and writing an Excel file will take unnecessary time.

The DataMining software used afterward accepts `.txt` files and works just fine.



<!-- CONTACT -->

## Contact

[![LinkedIn][linkedin-shield]][linkedin-url] [![Gmail][gmail-shield]][gmail-url]

<!-- ACKNOWLEDGEMENTS -->

## Acknowledgements

- :octocat: [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet) | Emojies
- :key: [Img Shields](https://shields.io) | Shields

<!-- MARKDOWN LINKS & IMAGES -->

[build-shield]: https://img.shields.io/badge/build-passing-brightgreen.svg?style=flat-square
[contributors-shield]: https://img.shields.io/badge/contributors-1-orange.svg?style=flat-square
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-blue.svg?style=flat-square&logo=linkedin
[linkedin-url]: https://linkedin.com/in/fredhm
[gmail-shield]: https://img.shields.io/badge/Gmail-red.svg?style=flat-square&logo=gmail&logoColor=white
[gmail-url]: mailto:contact.hammami.fredj@gmail.com
[behance-shield]: https://img.shields.io/badge/Behance-blue.svg?style=flat-square&logo=behance&logoColor=white
[behance-url]: https://www.behance.net/fredhm
[license-shield]: https://img.shields.io/badge/license-MIT-green.svg?style=flat-square
[license-url]: https://choosealicense.com/licenses/mit
