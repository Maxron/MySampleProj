import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='MySampleProj',
    version='0.0.1.dev1',
    author='maxron',
    author_email='zero.maxima@gmail.com',
    description='A sample project for python',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='',
    license='MIT',

    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Sample",
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords="sample setuptools development",

    install_requires=[]
)
