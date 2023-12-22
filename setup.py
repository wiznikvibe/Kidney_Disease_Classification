import setuptools
from typing import List


def get_requirements(file_path:str)-> List[str]:
    HYPEN_EDOT = "-e ."
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n','') for req in requirements]
        if HYPEN_EDOT in requirements:
            requirements.remove(HYPEN_EDOT)

    return requirements

setuptools.setup(
    name = "Kidney_Disease_Classifier",
    version = "0.0.0.1",
    description = "Image Classifier Using CNN",
    author="Nikhil",
    author_email = "nikhilshetty00@gmail.com",
    packages = setuptools.find_packages(),
    install_requires = get_requirements(file_path='requirements.txt')
)

    
