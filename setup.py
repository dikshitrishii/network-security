from setuptools import setup, find_packages
from typing import List

def get_requirements() -> List[str]:
    """
    This function returns a list of requirements for the project.
    It reads from a 'requirements.txt' file and returns the list of packages.
    """
    requirement_list: List[str] = []
    try:
        with open('requirements.txt', 'r') as file:
            # Read the lines from the file
            lines = file.readlines()
            for line in lines:
                # Remove any leading/trailing whitespace and comments
                requirement = line.strip()
                # ignore empty lines and -e .
                if requirement and not requirement.startswith('#') and not requirement.startswith('-e'):
                    requirement_list.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found. Please ensure it exists in the project directory.")
    return requirement_list

print(get_requirements())

setup(
    name="Network_Security",
    version="0.0.1",
    author="Dikshit Rishi",
    author_email="dikshit.rishii@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(),
)