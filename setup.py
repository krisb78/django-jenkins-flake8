from setuptools import (
    setup,
    find_packages
)

import dj_flake8

setup(
    name='dj_flake8',
    author="Krzysztof Bandurski",
    author_email="krzysztof.bandurski@gmail.com",
    version=dj_flake8.__version__,
    description='Simple flake8 report generation for django-jenkins',
    license='BSD License',
    platforms=['OS Independent'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
    ],
    packages=find_packages(exclude=["example", "example.*"]),
    include_package_data=True,
    zip_safe=False
)
