from setuptools import setup 

setup(name="geventdaemon",
      version="0.1dev",
      author="Antonin Amand",
      author_email="antonin.amand@gmail.com",
      description="gevent daemonizer",
      package_dir = {'':'lib'},
      packages=[''],
      zip_safe=False,
      install_requires=[
          'gevent',
          'python-daemon',
        ],
    )

