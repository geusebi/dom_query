import setuptools

long_desc = open("README.md").read()

setuptools.setup(
    name='pydom_query',
    version='0.0.1',
    packages=('pydom_query', ),

    description="",
    long_description=long_desc,
    long_description_content_type='text/markdown',

    # url git
    url='https://gitlab.com/geusebi/pydom_query',

    python_requires='>=3.7',
    install_requires=tuple(),

    author='Giampaolo Eusebi',
    author_email='giampaolo.eusebi@gmail.com',

    license='GNU LGPL 3.0',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
    ],
)