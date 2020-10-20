# DIP-CLI
#### A cli tool to implement image processing filters on any image or sample matrix taken as input.

## Introduction
Digital image processing is the manipulation of images using specific algorithms for the purpose of feature extraction. The filters applied are heavily dependent on the domain used. The spatial domain uses images just as they are and applies the required filter through a process called covolution. However for the frequency domain, the image is first required to be converted into to its frequency distribution using a process called transformation. <br>
The list of filters enabled in this project are given below. Usage of this implementation is domain specific and thus, their respective attributes must be specified to get the correct output. 

### Filters Available
#### Spatial Domain
* Laplacian Filter
* Sobel Filter
* Prewitt Filter
* Statistical Filters 

#### Frequency Domain
* Ideal Filter
* Gaussian Filter
* Butterworth Filter
  
## Usage
Input - Image Format
```
python main.py --p \dip-cli\samples\sample.png --dim 300x300 --s laplacian
```
Input - Matrix in a text format
```
python main.py --p \dip-cli\samples\test.txt --dim 3x3 --f gaussian --d 10 --n 1.2
```
### Attributes
```Path``` - To take image or text file containing the matrix as input <br>
```Dimension``` - To specify the size of the output <br>
```Domain``` - Spatial\Frequency Domain <br>
```Filter``` - Specified Filter <br>
```D0\N``` - Threshold Values <br>
```Save``` - Save\Display Output <br>

## Sample Outputs
![Spatial Domain](https://github.com/VaishnaviNandakumar/dip-cli/blob/master/outputs/readme/Spatial-Domain-Outputs.jpg)
![Frequency Domain](https://github.com/VaishnaviNandakumar/dip-cli/blob/master/outputs/readme/Frequency-Domain-Outputs.jpg)
