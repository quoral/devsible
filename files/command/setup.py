from setuptools import setup

setup(
    dependencies = [
        "GitPython",
        "distro",
    ],
    entry_points={
        'console_scripts': [
            'devsible = devsible:main',
        ]
    }
)