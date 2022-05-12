from distutils.core import setup
setup(
  name = 'foopackage',         # How you named your package folder (MyLib)
  packages = ['foopackage'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license = 'GPLv2',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'This is a test package',   # Give a short description about your library
  author = 'Gonzalo Vidal',                   # Type in your name
  author_email = 'gvidal@betterfood.com',      # Type in your E-Mail
  url = 'https://github.com/user/reponame',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',    # I explain this later on
  keywords = ['foo', 'bar'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'validators',
          'beautifulsoup4',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: GPLv2 License',   # Again, pick a license
    'Programming Language :: Python :: 3.10',      #Specify which pyhton versions that you want to support
  ],
)