

#
#
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * start of CF.setup.py
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
#
#


from setuptools import find_packages
from setuptools import setup


setup(
  author="GaelicGrime",
  author_email="will.angus.blaylock@gmail.com",
  license="GPLv3",
  name="**PACKAGE_NAME**",
  url="https://github.com/ComfortableSoftware/commonFunctions_py",
  version="0.8.0",
  package_dir={"**PACKAGE_NAME**": "**PACKAGE_NAME**"},
  package_data={
      "**PACKAGE_NAME**": [
          "../doc/*",
      ]
  },
  packages=["**PACKAGE_NAME**"],
  install_requires=[
  ],
  extras_require={
      "hashing": ["hashlib"],
      "pickling": ["pickle"],
      "timestuff": [
          "datedelta",
          "datetime",
          "dateutil",
          "time",
      ],
      "debugging": [
          "inspect",
      ],
  }
)
