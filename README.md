# vilota_assessment

## Requirement

open3d, spatialmath-python, numpy

Recommended to use conda: 
```
conda env create -f environment.yml
```
```
conda activate vilota-1
```
## Explanation

### First script

This script visualizes three transformations, the first is pure translation, the second is rotation + translation, the third is the second one incorporated with a translation.
<img src="gifs/1.gif" width="400"/>


### Second script

This script visualizes a bounding box representing the camera wireframe that is rotating and translating in the 3D space. The DoF is 6 and the motion can be modified. For simplicity, I didn't use the parser to make it more convinient to customize the motion, etc.

The gifs first visualize the trajectory of the wireframe, then the fixed view on the camera (cannot see the translation)

<img src="gifs/2.gif" width="400"/>



