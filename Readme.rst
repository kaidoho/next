

python build-toolchain.py
python init-repo.py

mkdir build
cd build
cmake -G"Eclipse CDT4 - Ninja" 

  cmd.append("-DCMAKE_INSTALL_PREFIX={0}".format(installfolder))
  cmd.append("-DCMAKE_TOOLCHAIN_FILE={0}".format(tcdef) )
  cmd.append("-DCMAKE_VERBOSE_MAKEFILE=ON")
  
  cmd.append("-DRTEMS_CPU={0}".format(cpu))
  
  cmd.append("-DRTEMS_NETWORKING={0}".format(str(int(enable_networking))))
  cmd.append("-DRTEMS_POSIX_API={0}".format(str(int(enable_posix))))
  cmd.append("-DRTEMS_MULTIPROCESSING={0}".format(str(int(enable_multiprocessing))))
  cmd.append("-DRTEMS_SMP={0}".format(str(int(enable_smp))))
  cmd.append("-DRTEMS_ENABLE_RTEMS_DEBUG={0}".format(str(int(enable_rtems_debug))))
  cmd.append("-DRTEMS_CXX={0}".format(str(int(enable_cxx))))
  cmd.append("-DRTEMS_TESTS={0}".format(str(int(enable_tests))))
  cmd.append("-DRTEMS_PARAVIRT={0}".format(str(int(enable_paravirt))))
  cmd.append("-DRTEMS_DRVMGR={0}".format(str(int(enable_drvmgr))))
  
  

../System/OS/rtems