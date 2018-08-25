from setuptools import setup

setup(name="rand_param_envs",
      version='0.1',
      description='Environments with random model parameters, using gym 0.7.4 and mujoco-py 0.5.7',
      url='https://github.com/dennisl88/rand_param_envs',
      author='Dennis Lee, Ignasi Clavera, Jonas Rothfuss',
      author_email='dennisl88@berkeley.edu',
      license='MIT',
      packages=['rand_param_envs'],
      install_requires=[
        'numpy>=1.10.4',
        'requests>=2.0',
        'six',
        'pyglet>=1.2.0',
        'scipy==0.17.1',
        'PyOpenGL==3.1.0',
        'nose>=1.3.7'
      ],
      zip_safe=False)