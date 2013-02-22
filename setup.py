from setuptools import setup, find_packages


setup(
    name='yesno',
    version='0.1',
    url="http://github.com/philippbosch/yesno",
    description="Get answers to simple yes/no questions",
    long_description="A collection of coded questions that answer simple yes/no questions for use in is___.com websites.",
    author="Philipp Bosch",
    author_email="hello@pb.io",
    license="MIT",
    keywords=["yes","no","question","answer"],
    platforms="any",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
    ],
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
)
