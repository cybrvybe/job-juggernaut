from setuptools import setup

setup(
    name="job-juggernaut",
    version="0.1",
    packages=["job_juggernaut"],
    entry_points={
        "console_scripts": [
            "juggernaut=job_juggernaut.cli.main:main",
        ],
    },
)
