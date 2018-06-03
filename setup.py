from setuptools import setup, find_packages

setup(
    name             = 'tmi_test',
    version          = '0.5.599',
    description      = "NoStress team (2018 HU-OSS B-6)'s Open Source CLI Todo List - test",
    author           = 'RDCPP',
    author_email     = 'zzzz1362@naver.com',
    url              = 'https://github.com/RDCPP/hu-oss-sw-2018-B-6',
    download_url     = 'https://github.com/RDCPP/hu-oss-sw-2018-B-6/archive/master.tar.gz',
    install_requires = [ ],
    packages         = find_packages(exclude = [ ]),
    keywords         = ['tmi_test', 'todo list', 'todo cli'],
    python_requires  = '>=3',
    package_data     =  {'tmi_test' : [ "LICENSE" ]},
    zip_safe=False,
    classifiers      = [
        'Environment :: Consol',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ],
    entry_points = {
        'console scripts' : [
            'tmi = tmi',
            'tmi_test = tmi_test'
        ],
    },
)