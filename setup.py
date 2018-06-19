from distutils.core import setup

setup(
    name='opay',
    version='v1.0',
    packages=['opay', 'opay.bank', 'opay.card',
              'opay.charge', 'opay.utils', 'opay.gateway',
              'opay.test'],
    url='https://github.com/alekaizer/opay-python',
    license='MIT',
    author='Achille AROUKO',
    author_email='achille.arouko@gmail.com',
    description='MoneyWave Python Library'
)
