## DIP-CLI
A cli tool to implement image processing filters on an image or a sample matrix.

### Introduction to digital image processing
## Filters available
* Spatial Domain
  - Laplacian Filter
  - Sobel Filter
  - Prewitt Filter
  - Statistical Filters - Mean, Median, Min, Max
* Frequency Domain
  - Ideal Filter
  - Gaussian Filter
  - Butterworth Filter
  
## Usage
If filter is to be applied on an image
'''
python main.py --p \dip-cli\samples\sample.png --dim 300x300 --s laplacian
'''
If filter is to be applied on a matrix
'''
python main.py --p \dip-cli\samples\test.txt --dim 3x3 --f gaussian --d 10 --n 1.2
'''
