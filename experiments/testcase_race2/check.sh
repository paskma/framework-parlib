
JPFDIR=/home/paskma/projects/jpf_trunk2
TARGET=$JPFDIR/testcase_race
mkdir -p $TARGET
cp -r unpacked/* $TARGET

cd $JPFDIR
java RunJPF +vm.classpath=testcase_race +jpf.listener=gov.nasa.jpf.tools.PreciseRaceDetector pypy.Main $@
