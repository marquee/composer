from setuptools import setup

setup(
        name                = 'marquee-composer',
        version             = '0.2.2-dev',
        description         = '',
        long_description    = file('README.md').read(),
        url                 = 'https://github.com/marquee/composer',
        author              = 'Alec Perkins',
        author_email        = 'alec@marquee.by',
        license             = 'UNLICENSE',
        packages            = ['composer'],
        zip_safe            = False,
        keywords            = '',
        install_requires    = ['content==0.1.0'],
        dependency_links    = [
            'git+ssh://git@github.com/marquee/content@v0.1.0-alpha#egg=content-0.1.0',
        ],
        package_data        = {
            'droptype-composer': ['../stylesheets/*'],
        },
        classifiers         = [
            'Development Status :: 2 - Pre-Alpha',
            'Intended Audience :: Developers',
            'License :: Public Domain',
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: Implementation :: CPython',
            'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        ],
    )
