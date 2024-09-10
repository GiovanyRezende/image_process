from setuptools import setup, find_packages

setup(
    name="image_process",
    version="0.0.1",
    author="GiovanyRezende",
    author_email="giovanyrmedeiros@gmail.com",
    url="https://github.com/GiovanyRezende/image_process",
    packages=find_packages(),
    install_requires=['numpy','matplotlib','PIL'],
    python_requires='>=3.8'
)