from setuptools import setup

setup(
        name                = 'marquee-composer',
        version             = '0.2.2-dev',
        description         = '',
        long_description    = file('README.md').read(),
        url                 = 'https://github.com/marquee/composer',
        author              = 'Alec Perkins',
        author_email        = 'alec@marquee.com',
        license             = 'UNLICENSE',
        packages            = ['composer'],
        zip_safe            = False,
        keywords            = '',
        install_requires    = ['content'],
        dependency_links    = ['http://github.com/marquee/content/tarball/master#egg=content-dev'],
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
