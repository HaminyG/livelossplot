from setuptools import setup, find_packages
import codecs

def readme():
    with codecs.open('README.md', encoding='utf-8') as f:
        return f.read()

setup(name='livelossplot',
      version='0.1.4',
      install_requires=['matplotlib', 'notebook'],
      description='Live training loss plot in Jupyter Notebook for Keras, PyTorch and others.',
      long_description=readme(),
      url='https://github.com/stared/livelossplot',
      author='Piotr Migdał',
      author_email='pmigdal@gmail.com',
      keywords=['keras', 'pytorch', 'plot', 'chart'],
      license='MIT',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Framework :: Jupyter',
          'Intended Audience :: Developers',
          'Intended Audience :: Education',
          'Intended Audience :: Science/Research',
          'Topic :: Scientific/Engineering',
          'Topic :: Scientific/Engineering :: Artificial Intelligence',
          'Topic :: Scientific/Engineering :: Visualization',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 3'
      ],
      packages=find_packages(),
      zip_safe=False)
