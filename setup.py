from setuptools import setup

setup(name='pytest-selenium-multi',
      version='1.3.1',
      description='pytest plugin for Selenium',
      long_description=open('README.rst').read(),
      author='bwalkowi',
      author_email='wallko1@hotmail.com',
      url='https://github.com/bwalkowi/pytest-selenium-multi',
      packages=['pytest_selenium_multi', 'pytest_selenium_multi.drivers'],
      install_requires=[
          'pytest>=2.7.3',
          'pytest-base-url',
          'pytest-html>=1.7',
          'pytest-variables',
          'selenium>=2.26.0',
          'requests'],
      entry_points={'pytest11': [
          'selenium = pytest_selenium_multi.pytest_selenium_multi',
          'selenium_safety = pytest_selenium_multi.safety',
          'browserstack_driver = pytest_selenium_multi.drivers.browserstack',
          'chrome_driver = pytest_selenium_multi.drivers.chrome',
          'firefox_driver = pytest_selenium_multi.drivers.firefox',
          'ie_driver = pytest_selenium_multi.drivers.internet_explorer',
          'remote_driver = pytest_selenium_multi.drivers.remote',
          'phantomjs_driver = pytest_selenium_multi.drivers.phantomjs',
          'saucelabs_driver = pytest_selenium_multi.drivers.saucelabs',
          'testingbot_driver = pytest_selenium_multi.drivers.testingbot']},
      license='Mozilla Public License 2.0 (MPL 2.0)',
      keywords='py.test pytest selenium saucelabs browserstack webqa qa '
               'mozilla',
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Framework :: Pytest',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
          'Operating System :: POSIX',
          'Operating System :: Microsoft :: Windows',
          'Operating System :: MacOS :: MacOS X',
          'Topic :: Software Development :: Quality Assurance',
          'Topic :: Software Development :: Testing',
          'Topic :: Utilities',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: Implementation :: CPython',
          'Programming Language :: Python :: Implementation :: PyPy'])
