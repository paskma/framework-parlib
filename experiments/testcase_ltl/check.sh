
JPFDIR=/home/paskma/projects/jpf_trunk2
TARGET=$JPFDIR/testcase_ltl
mkdir -p $TARGET
cp -r unpacked/* $TARGET

export LTLFORM='G{{method:File_56.oopen}->{X{F{method:File_56.oclose}}}}'

cd $JPFDIR
java RunJPF +vm.classpath=testcase_ltl +jpf.listener=res.min.verifier.LTLVerifier pypy.Main
