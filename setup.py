from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path:str)->List[str]:
    HYPEN_E_DOT = "-e ."
    with open(file_path) as f:
        requirements = f.readlines()
        requirements = [req.replace('\n','') for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name="kidney_disease_classifier",
    version="0.0.1",
    description="Image Classification",
    author="Nikhil",
    author_email="nikhilshetty439@gmail.com",
    packages= find_packages(),
    install_requires = get_requirements('requirements.txt')
)