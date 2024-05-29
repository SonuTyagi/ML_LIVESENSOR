from setuptools import find_packages,setup


def get_requires():
    with open("requirements.txt","r") as f:
        req=f.readlines()
    return req

    




setup (
    name="LiveSensor",
    version="0.0.1",
    author="sonu tyagi",
    author_email="sonutyagi1712@gmail.com",
    packages= find_packages(),
    install_requires= get_requires(),

)