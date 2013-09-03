from setuptools import setup

setup(
  name='motoactv',
  version='0.1',
  description='Tool and library for managing Motoactv data',
  author='Kevin Sweeney',
  author_email='kevin.t.sweeney@gmail.com',
  url='https://github.com/kevints/motoactv',
  license='BSD',
  classifiers=[
    'Development Status :: 3 - Alpha',
    'License :: OSI Approved :: BSD License',
    'Natural Language :: English',
    'Programming Language :: Python :: 3.3',
    'Topic :: System :: Archiving :: Mirroring',
  ],
  py_modules=['motoactv'],
  entry_points={
    'console_scripts': [
      'motoactv = motoactv:main',
    ],
  },
)
