from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path: str)->List[str]:
    '''
    returns list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

setup(
    name="student-test-performance-prediction",
    version='0.0.1',
    author='Dhrumi',
    author_email='dhrumikansara8@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),

    
)