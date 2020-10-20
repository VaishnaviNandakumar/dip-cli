## DIP-CLI
A cli tool to implement image processing filters on an image or a sample matrix.

### Introduction 
Digital image processing can be defined as the manipulation of images using specific algorithms for the purpose of feature extraction. This process can be done in several domains. In the spatial domain, we use the images just as they are and apply the required filters through a process called <b>covolution</b>. Whereas, to work with an image in the frequency domain, the conversion of an image to its frequency distribution is neccessary. This is done using a process called <b>transformation</b>. Some examples of the transformations that can be used are  - Discrete Fourier Transform, Discrete Cosine Transform and the Laplace Transform.

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
![Spatial Domain](https://github.com/VaishnaviNandakumar/dip-cli/blob/master/outputs/Spatial-Domain-Outputs.jpg)
![Frequency Domain](https://github.com/VaishnaviNandakumar/dip-cli/blob/master/outputs/Frequency-Domain-Outputs.jpg)
