from setuptools import setup, find_packages

setup(
    name                = 'eapt',
    version             = '0.1.1',
    description         = 'Enhanced Advanced Packaging Tools',
    author              = 'Taegeun Moon',
    author_email        = 'xorms987@gmail.com',
    url                 = 'https://github.com/eAPT2020/eAPT',
    download_url        = 'https://github.com/eAPT2020/eAPT',
    install_requires    =  ["pygeoip>=0.*", "geoip2>=3.0.0", "pycurl>=7.*.*.*", "haversine>=2.*.*"],
    packages            = find_packages(exclude = []),
    keywords            = ['apt'],
    python_requires     = '>=3.7',
    package_data        = {},
    zip_safe            = True,
    classifiers         = [
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    entry_points={
    'console_scripts': [ 
        'eapt = eapt.core:main' 
    ] 
},
)