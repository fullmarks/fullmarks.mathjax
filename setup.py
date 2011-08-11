# coding=utf-8

from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='fullmarks.mathjax',
      version=version,
      description="MathJax for Plone",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='plone mathjax mathml mathematics',
      author='Mark Horner and Roché Compaan',
      author_email='dev@fullmarks.org.za',
      url='http://github.com/fullmarks/fullmarks.mathjax',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['fullmarks'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      setup_requires=["PasteScript"],
      paster_plugins=["ZopeSkel"],
      )
