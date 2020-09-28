from setuptools import setup, find_packages


with open('requirements.txt') as f:
    INSTALL_REQUIRES = [l.strip() for l in f.readlines() if l]


setup(
    name='spherecluster',
    version='0.1.7',
    description='Clustering on the unit hypersphere in scikit-learn.',
    author='Jason Laska',
    author_email='jason@claralabs.com',
    packages=find_packages(),
    install_requires=INSTALL_REQUIRES,
    url='https://github.com/clara-labs/spherecluster',
    license='MIT',
)
