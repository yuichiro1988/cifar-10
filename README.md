# CIFAR-10  

## Overview  
We  classify 300,000 color images of CIFAR-10 into 10 classes by using Neural network.  
#### What is CIFAR-10  
CIFAR-10 is an established computer-vision dataset used for object recognition. It is a subset of the 80 million tiny images dataset and consists of 60,000 32x32 color images containing one of 10 object classes, with 6000 images per class. It was collected by Alex Krizhevsky, Vinod Nair, and Geoffrey Hinton.  

#### Evaluation  
The score is evaluated on classification accuracy (the percent of labels that are predicted correctly).  
## Installation  
#### Download the data  
1. Clone this repo to your computer.
2. Get into the folder using ``cd cifar-10``.
3. Run mkdir data.
4. Change directory using ``cd data``.  
5. Download the data files from Kaggle into the data directory.  
  * You can find the train and test data [here](https://www.kaggle.com/c/cifar-10/data).  
  * You need to register with Kaggle to download the data.  
6. Extract train.7z and test.7z files that you downloaded.  
  * You may need p7zip or p7zip-full package to unzip the files.  
  * You will get train and test directory in the data directory.  
          cifar-10/  
           |-data/  
                |-train/
                |-test/
  * You can remove all the .7z files by running ``rm *.7z``  

## Requirements  
* Install the requirements using ``pip install -r requirements.txt``.  
* You may want to use a virtual environment for this project.  

## Usage  
* Run ``mkdir processed`` to create a directory for our processed datasets.  
* Run ``python setup.py`` to split the images in the train directory into train and validation directory. These directories are made in the processed directory.  

## Licence  
Read LICENSE.txt.   
