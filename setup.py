import setuptools

setuptools.setup(
    name='Automancy',
    version='0.0.1',
    author='Jonathan Craig',
    author_email='blurr@iamtheblurr.com',
    classifiers=[
        'Programming Language :: Python :: 3.7'
        'Topic :: Web Automation :: Quality Assurance'
    ],
    packages=setuptools.find_packages(),
    url='https://github.com/iamtheblurr/automancy',
    license='MIT',
    install_requires=[
        'chronomancy',
        'lxml==4.2.5',
        'selenium==3.14.1',
        'webvtt-py==0.4.2',
    ],
    long_description=open('README.md', encoding='utf8').read(),
)
