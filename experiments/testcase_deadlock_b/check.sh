
JPFDIR=/home/paskma/projects/jpf_trunk2
TARGET=$JPFDIR/testcase_deadlock_b
mkdir -p $TARGET
cp -r unpacked/* $TARGET

cd $JPFDIR
java RunJPF +vm.classpath=testcase_deadlock_b pypy.Main
