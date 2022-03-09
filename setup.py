from setuptools import setup, find_packages

setup(
    name='hy-tools',
    description= 'HyTools: Hyperspectral image processing library',
    version='1.2.0',
    license='GNU General Public License v3.0',
    url='https://github.com/EnSpec/hytools',
    author = 'Adam Chlus, Zhiwei Ye, Ting Zheng, Natalie Queally, Evan Greenberg and Philip Townsend',
    packages=find_packages(),
    install_requires=['h5py',
                      'matplotlib>=2.2.2',
                      'numpy>=1.19.2',
                      'pandas',
                      'ray>=1.2.0',
                      'scikit-learn>=0.19.1',
                      'scipy>=1.3.0'],
    python_requires='>=3.6, !=3.9.*'
    )


