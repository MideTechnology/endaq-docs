import codecs
import os.path
import setuptools


def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), 'r') as fp:
        return fp.read()


INSTALL_REQUIRES = [
]

TEST_REQUIRES = [
]

DOCS_REQUIRES = [
]


setuptools.setup(
        name='endaq-docs',
        version='1.0',
        author='Mide Technology',
        author_email='help@mide.com',
        description='Landing page for enDAQ documentation',
        long_description=read('README.md'),
        long_description_content_type='text/markdown',
        url='https://github.com/MideTechnology/endaq-docs',
        license='MIT',
        classifiers=['Development Status :: 5 - Production/Stable',
                     'License :: OSI Approved :: MIT License',
                     'Natural Language :: English',
                     'Programming Language :: Python :: 3.9',
                     'Programming Language :: Python :: 3.10',
                     'Programming Language :: Python :: 3.11',
                     'Programming Language :: Python :: 3.12',
                     'Programming Language :: Python :: 3.13',
                     ],
        keywords='endaq configure recorder hardware',
        project_urls={
            "Bug Tracker": "https://github.com/MideTechnology/endaq-docs/issues",
            "Documentation": "https://mide-technology-endaq-docs.readthedocs-hosted.com/en/latest/",
            "Source Code": "https://github.com/MideTechnology/endaq-docs",
            },
        packages=[
            ],
        package_dir={
            'endaq_docs': './docs',
            },
        package_data={
        },
        test_suite='tests',
        install_requires=[
            ],
        extras_require={
            },
        # tests_require=[
        #     'pytest',
        #     'mock'
        #     ],
)
