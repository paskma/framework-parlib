
JPFDIR=/home/paskma/projects/jpf_trunk2
TARGET=$JPFDIR/testcase_exception2
mkdir -p $TARGET
cp -r unpacked/* $TARGET

cd $JPFDIR
java RunJPF +vm.classpath=testcase_exception2 pypy.Main
