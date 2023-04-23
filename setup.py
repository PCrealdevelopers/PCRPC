from setuptools import setup, find_packages
import re

version = ''
with open('PCRPC/__init__.py') as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError('Version is not set')



setup(
    name='PCRPC',
    version=version,
    author='PCDevlpoment',
    description='An Python wrapper for Discord RPC',
    long_description_content_type='text/markdown',
    packages=find_packages(),
    include_package_data=True,
    keywords=["Discord", "rpc", "discord rpc", "pcdev"],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: MacOS',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python'
    ]
)