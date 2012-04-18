
JPFDIR=/home/paskma/projects/jpf_trunk2
PROJ=proj_ftpclient
TARGET=$JPFDIR/$PROJ
mkdir -p $TARGET
cp -r unpacked/* $TARGET

cd $JPFDIR
java RunJPF +vm.classpath=$PROJ +jpf.listener=gov.nasa.jpf.tools.PreciseRaceDetector pypy.Main $@
