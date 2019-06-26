import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='sp80022suite',
    version='0.0.1',
    author="Nils Wisiol",
    author_email="mail@nils-wisiol.de",
    description="NIST SP 800-22 Statistical Tests",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nils-wisiol/sp80022suite",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    ext_modules=[setuptools.Extension('sp80022suite', [
        # root
        'src/pythonInterface.c',

        # helpers
        'src/cephes.c',  # for longest run of ones test
        'src/matrix.c',  # for rank test
        'src/dfft.c',  # for discrete fourier transform test

        # tests
        'src/frequency.c',
        'src/blockFrequency.c',
        'src/runs.c',
        'src/longestRunOfOnes.c',
        'src/rank.c',
        'src/discreteFourierTransform.c',
        'src/nonOverlappingTemplateMatchings.c',
        'src/overlappingTemplateMatchings.c',
        'src/universal.c',
        'src/linearComplexity.c',
        'src/approximateEntropy.c',
        'src/serial.c',
        'src/cusum.c',
        'src/randomExcursions.c',
        'src/randomExcursionsVariant.c',
    ])]
)
