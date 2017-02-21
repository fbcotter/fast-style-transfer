from setuptools import setup, find_packages
import os

def read_file(path):
    with open(os.path.join(os.path.dirname(__file__), path), "r") as fobj:
        return fobj.read()

setup(name="fast_style_transfer",
      version="0.0.1",
      packages=find_packages(),
      install_requires=["future", "numpy", "tensorflow", "scipy", "pdb"],
      author="Logan Engstrom"
)
