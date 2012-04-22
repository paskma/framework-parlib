
JPFDIR=/home/paskma/projects/jpf_trunk2
WORKDIR=testcase_random
TARGET=$JPFDIR/$WORKDIR
mkdir -p $TARGET
cp -r unpacked/* $TARGET

cd $JPFDIR
java RunJPF +vm.classpath=$WORKDIR pypy.Main
