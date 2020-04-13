from setuptools import setup, find_packages

setup(
    name                = 'eapt',
    version             = '0.1',
    description         = 'Enhanced Advanced Packaging Tools',
    author              = '2gilhee',
    author_email        = '2gilhee@naver.com',
    url                 = 'https://github.com/2gilhee/eAPT',
    download_url        = 'https://github.com/2gilhee/eAPT',
    install_requires    =  [],
    packages            = find_packages(exclude = []),
    keywords            = ['apt'],
    python_requires     = '>=3',
    package_data        = {},
    zip_safe            = True,
    classifiers         = [
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)