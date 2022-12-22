<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
<!-- [![Forks][forks-shield]][forks-url] -->
<!-- [![Issues][issues-shield]][issues-url] -->
<!-- [![MIT License][license-shield]][license-url] -->

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/ASU-Lim-Lab/Absolute-Q">
    <img src="logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">QuantStudio Absolute Q Digital PCR</h3>

  <p align="center">
    Scripts
    <br />
    <a href="https://github.com/ASU-Lim-Lab/Absolute-Q/blob/main/fluorescence_analysis.py"><strong>Fluoresence analysis »</strong></a>
    <br />
    <a href="https://github.com/ASU-Lim-Lab/Absolute-Q/blob/main/codon_analysis.py"><strong>Codon analysis »</strong></a>
    <br />
    <br />
<!--     <a href="https://github.com/ASU-Lim-Lab/Absolute-Q/">any_criteria</a> -->
<!--     · -->
<!--     <a href="https://github.com/ASU-Lim-Lab/Absolute-Q/">any_criteria</a> -->
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about-the-project">About The Project</a></li>
    <li><a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#fluoresence-analysis">Fluoresence Analysis</a></li>
    <li><a href="#codon-analysis">Codon Analysis</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributors">Contributors</a></li>
  </ol>
</details>


<!-- ABOUT THE PROJECT -->
## About The Project

<!-- [![Product Name Screen Shot][product-screenshot]](https://example.com) -->

This repository contains files associated with projects involving the QuantStudio Absolute Q Digital PCR. 
Current efforts involve detection of SARS-CoV-2 spike mutations that enable mAb resistance. 

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

Scripts are comatable with Python 3.9.14+, Pandas 1.5.1+, Biopython 1.79+.

### Prerequisites

* [![Python][Python]][Python-url]
* [![Pandas][Pandas]][Pandas-url]
* [![Biopython][Biopython]][Biopython-url]


### Installation

  ```sh
  conda install python
  ```

  ```sh
  conda install pandas
  ```

  ```sh
  conda install -c conda-forge biopython
  ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Fluoresence Analysis
File name formating should be consistant with the sample csv files.
(eg. BT01_143_01_01_F.csv)
Information separated by underscore include test number (BT01), probe locaiton (143), batch number (01), sample number (01) and specific probe (F) ID.
All formatted csv files should reside in the same directory before running script. 
<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Codon Analysis
Printed output can be saved using CL command $ script.py > output.txt.
Unhash df output for troubleshooting.
<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ROADMAP -->
## Roadmap

- [ ] Continued development of codon analysis script.
<!-- - [ ] Feature 2 -->
<!-- - [ ] Feature 3 -->
<!--     - [ ] Nested Feature -->

[Open issues](https://github.com/ASU-Lim-Lab/Absolute-Q/issues)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Contributors
<br />
<div align="left">
    <a href="https://github.com/ASU-Lim-Lab/Absolute-Q/graphs/contributors"><strong>Contributors »</strong></a>
</div>

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/ASU-Lim-Lab/Absolute-Q.svg?style=for-the-badge
[contributors-url]: https://github.com/ASU-Lim-Lab/Absolute-Q/graphs/contributors
[Biopython]: https://img.shields.io/badge/Biopython-1.80-blue
[Biopython-url]: https://biopython.org/
[Pandas]: https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white
[Pandas-url]: https://pandas.pydata.org/
[Python]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[Python-url]: https://www.python.org/
