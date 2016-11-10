import os
from setuptools import setup


def read(frame):
    return open(os.path.join(os.path.dirname(__file__), frame)).read()


# def long_description(frame):
#     import codecs
#     with codecs.open(
#             os.path.join(os.path.dirname(__file__), frame), encoding="utf-8"
#     ) as f:
#         return f.read()


setup(
    name='Python-Project-Template',
    version='0.0.1',
    author='VicYu',
    author_email='no@vicyu.com',
    license='GNU v3',
    description='',
    # home page for the package
    url='https://github.com/Vic020/Python-Project-Template',
    packages=[
        'Project',
        'Project.libs'
    ],
    long_description=read("README"),
    requires=[
        'click'
    ]
)
