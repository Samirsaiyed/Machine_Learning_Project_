
from setuptools import setup
from typing import List

# Declare variables for setup function
PROJECT_NAME="housing-predictor"
VERSION="0.0.1"
AUTHOR="Samir"
DESCRIPTION="This is a first FSDS nov batch machine learning project"
PACKAGES=["housing"]
REQUIREMENT_FILE_NAME="requirements.txt"


    
def get_requirements_list()->List[str]:
    """
    Description : This function is going to return list of requirements 
    mention in requirements.txt file

    return This function is going to return a list which contain name of 
    libraries mwntioned in requirements.txt file 
    """
    with open( REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines()




setup(
name=PROJECT_NAME,
version=VERSION,
author=AUTHOR,
description=DESCRIPTION,
packages=PACKAGES,
install_requires=get_requirements_list()
)


#get_requirements_list is woking ro not