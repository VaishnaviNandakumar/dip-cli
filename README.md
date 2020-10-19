## DIP-CLI
A cli tool to implement image processing filters on an image or a sample matrix.

### Introduction 
### Filters available
#### Spatial Domain
* [Laplacian Filter](#Laplacian-Filter)
* [Sobel Filter](#Sobel-Filter)
* [Prewitt Filter](#Prewitt-Filter)
* [Statistical Filters ](#Statistical-Filters)
#### Frequency Domain
* [Ideal Filter](#Ideal-Filter)
* [Gaussian Filter](#Gaussian-Filter)
* [Butterworth Filter](#Butterworth-Filter)
  
<a name="Laplacian-Filter"></a>
### Laplacian Filter

<a name="Sobel-Filter"></a>
### Sobel Filter

<a name="Prewitt-Filter"></a>
### Prewitt Filter

<a name="Statistical-Filters"></a>
### Statistical Filters 

<a name="Ideal-Filter"></a> 
### Ideal Filter

<a name="Gaussian-Filter"></a>
### Gaussian Filter

<a name="Butterworth-Filter"></a>
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
