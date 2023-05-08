# Comparative Analysis of High-Performance Computing Facilities (TACC & NCAR)
## Table of Contents
1. [Introduction](#introduction)
1. [Video Demonstration](#video-demonstration)
2. [Features](#features)
3. [Running website locally on your machine](#running-website-locally-on-your-machine)
4. [Poster](#poster)

### Introduction
This is a Dash web application that visualizes the comparison between Texas Advanced Computing Center (TACC) and National Center for Atmospheric Research (NCAR) in terms of their high-performance computing capabilities, data storage systems, research domains, funding, and software ecosystem.

The application is deployed on Heroku and is built using Python, Dash, and Plotly.

[Website Link](https://tacc-ncar-visualization.herokuapp.com/)
###### Video Demonstration
https://user-images.githubusercontent.com/76918821/233721489-f253c20b-a5fb-4234-8bdf-26c422b6233c.mp4

### Features
- LINPACK Performance and Power Usage Comparison
- Data Storage Capacities Comparison
- Data Storage and Management Solutions Comparison
- Research Domains and Projects Comparison
- Research Domains Distribution (Pie Charts)
- Funding and Support Sources Comparison
- Software Ecosystem Comparison

### Running website locally on your machine

Make sure you have Python 3.7 or higher installed.

1. Clone the repository or download the source code.

2. Navigate to the project directory and create a virtual environment using the following command:
`python -m venv venv`
3. Activate the virtual environment:

- On Windows: `venv\Scripts\activate`
- On macOS/Linux: `source venv/bin/activate`
4. Install the required packages using pip:
`pip install -r requirements.txt`
5. Run the dash app (website):
`python3 website.py`
6. Make sure you see the following ouput on the terminal:
```
Dash is running on http://127.0.0.1:8050/

 * Serving Flask app 'website'
 * Debug mode: on 
 ```
7. Follow the link and enjoy the visualizations!

### Poster 
This is the poster I submitted for my CI Compass Fellowship Program (INFO-I 499 - 3 credits)

[![PDF Preview](Poster+Presentation/Img.jpg)](Poster+Presentation/poster.pdf)





