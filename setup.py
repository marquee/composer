from setuptools import setup

setup(
        name                = 'marquee-composer',
        version             = '0.2.3-dev',
        description         = '',
        long_description    = file('README.md').read(),
        url                 = 'https://github.com/marquee/composer',
        author              = 'Alec Perkins',
        author_email        = 'alec@marquee.by',
        license             = 'UNLICENSE',
        packages            = ['composer'],
        zip_safe            = False,
        keywords            = '',
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
