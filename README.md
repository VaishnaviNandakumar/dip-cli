## DIP-CLI
A cli tool to implement image processing filters on an image or a sample matrix.

### Introduction 
### Filters available
#### Spatial Domain
* [Laplacian Filter] (#Laplacian Filter)
* [Sobel Filter](#Sobel Filter)
* [Prewitt Filter] (#Prewitt Filter)
* [Statistical Filters ](#Statistical Filters - Mean, Median, Min, Max)
#### Frequency Domain
* [Ideal Filter](#Ideal Filter)
* [Gaussian Filter](#Gaussian Filter)
* [Butterworth Filter](#Butterworth Filter)
  
### Laplacian Filter
### Sobel Filter
### Prewitt Filter
### Statistical Filters 
  
### Ideal Filter
### Gaussian Filter
### Butterworth Filter


## Usage
Input - Image Format
```
python main.py --p \dip-cli\samples\sample.png --dim 300x300 --s laplacian
```
Input - Matrix in a text format
```
python main.py --p \dip-cli\samples\test.txt --dim 3x3 --f gaussian --d 10 --n 1.2
```

## Sample Outputs
