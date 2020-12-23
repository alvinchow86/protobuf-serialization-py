import subprocess

version = '0.1.2'

# Append a branch name to the version for development purpose
try:
    output = subprocess.run("git rev-parse --abbrev-ref HEAD", shell=True, capture_output=True)
    branch = output.stdout.decode().strip()

    if branch != 'master':
        version = f'dev.{branch}.{version}'
except Exception as e:
    print('Could not get git branch', e)


__version__ = version
