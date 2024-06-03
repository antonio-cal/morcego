import os
import platform as pl
from colorama import Style, Fore

from datetime import datetime as dt
def criar(readme):
    if os.path.exists("README.md"):
        with open("README.md", "w+") as arq:
            arq.write(readme)
            arq.seek(0)
            readmer = arq.read()
    if os.path.exists("LICENSE"):
         with open("LICENSE", "w") as arq:
            arq.write(f"""MIT License

Copyright (c) {ano} {user}

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
""")
    if os.path.exists("setup.py"):
        with open("setup.py", "w") as arq:
            plata = pl.system()
            try:
                if plata == "Windows":
                    user = os.environ.get("USERNAME")
                elif plata in ["Linux", "Darwin"]:
                    user = os.environ.get("USER")
                ano = dt.now().year
            except:
                print(Fore.RED + "nao tem system" + Style.RESET_ALL)
            arq.write(f"""from setuptools import setup 
            setup(name='',
        version='',
        license='MIT License',
        author='{user}',
        long_description='{readmer}',
        long_description_content_type='',
        author_email='',
        keywords='',
        description=',
        packages=[""],
        install_requires=[""])""")
        