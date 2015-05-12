import os
import subprocess
import tempfile
import shutil

BASE = os.path.abspath('.')
SUPERMIN = os.path.join(BASE, 'supermin', 'src', 'supermin')


def main():
    pkgs = ['bash', 'coreutils']
    target = 'fedora_min'

    tmp = tempfile.mkdtemp()

    cmd = [SUPERMIN, '--prepare'] + pkgs + ['-o', tmp]
    subprocess.Popen(cmd).wait()

    os.makedirs(target)
    cmd = [SUPERMIN, '--build', '-f', 'chroot', '-o', target, tmp]
    subprocess.Popen(cmd).wait()

    shutil.rmtree(tmp)


main()
