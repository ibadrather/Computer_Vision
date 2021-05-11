# Shape, area and color detection using OpenCV

## Install Miniconda from the following link:
https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe

I recommend you register Miniconda as your default Python 3.8 during installation


## Now open anaconda prompt:
Change directory to current working directory

## To see the current environments:
	conda env list

or
	
	conda info --envs

or
	
	conda info -e

## Create environment:
	conda env create --name env_name_of_choice -f requirements.yml

Replace env_name_of_choice with env name of your choice. 
Note: There should be no space in the environment name.

## Let's verify the previous step: 
### Type: 
	conda env list  
and you should now expect the environment name: env_name_of_choice

## Activate the environment:
	conda activate env_name_of_choice

## To run the file:
	python 01_shape_area_color_detection_opencv.py

## To deactivate current environment:
	conda deactivate 
