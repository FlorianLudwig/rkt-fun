if ! [ -d "rkt-v0.5.5" ]; then
    wget https://github.com/coreos/rkt/releases/download/v0.5.5/rkt-v0.5.5.tar.gz
    tar xzvf rkt-v0.5.5.tar.gz
fi

if ! [ -d "supermin" ]; then
    git clone git@github.com:libguestfs/supermin.git
fi

cd supermin
git pull

./bootstrap
./autogen.sh
./configure
make

# as root
yum-builddep supermin
