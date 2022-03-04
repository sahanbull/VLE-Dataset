from setuptools import setup

setup(
    name='',
    version='1.0',
    packages=['helper_code', 'helper_code.helper_tools',
              'helper_code.feature_extraction', 'helper_code.models'],
    url='',
    license='',
    author='',
    author_email='',
    description='This python package includes the datasets and the helpfer functions that allow building models for predicting context-agnostic (population-based) of video lectures. ',
    install_requires=[
        'numpy>=1.14.1',
        'pandas>=0.22.0',
        'scipy>=1.0.1',
        'nltk>=3.2.5',
        'ujson>=1.35',
        'scikit-learn>=0.19.1',
        'pyspark>=2.4.5',
        'textatistic>=0.0.1']
)
