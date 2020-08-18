import setuptools

setuptools.setup(
    name='Automancy',
    version='0.0.1',
    author='Jonathan Craig',
    author_email='blurr@iamtheblurr.com',
    classifiers=[
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Software Development :: Quality Assurance',
        'Topic :: Software Development :: Testing',
        'Topic :: Internet :: WWW/HTTP :: Browsers'
    ],
    packages=setuptools.find_packages(),
    url='https://github.com/iamtheblurr/automancy',
    license='MIT',
    install_requires=[
        'chronomancy',
        'lxml',
        'pytest',
        'selenium',
        'webvtt-py',
    ],
    long_description=open('README.md', encoding='utf8').read(),
)
