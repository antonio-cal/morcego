from setuptools import setup 
with open("README.md", "r", encoding='utf-8') as arq:
    readme = arq.read()
with open("descrição.md", "r", encoding='utf-8') as arq:
    descrição = arq.read()
setup(name='morcego',
      version='0.0.1',
      license='MIT License',
      author='antonio-cal',
      long_description=readme,
      long_description_content_type='text/markdown',
      author_email='antonio.caldeira.carvalho@gmail.com',
      keywords='morcego',
      description=descrição,
      packages=["morcego"],
      install_requires=["time"])
