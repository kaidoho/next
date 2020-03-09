# Copyright (C) 2020, M.B.Moessner
#
# SPDX-License-Identifier: Apache-2.0 
#

from Modules.Utils import *




if __name__ == '__main__':
    cwd = os.getcwd()
    logger.info("Building...")
    
    buildFolder = cwd + "/build"
    
    if os.path.exists(buildFolder):
        shutil.rmtree(buildFolder, ignore_errors=True)
    
    os.makedirs(buildFolder, exist_ok=True)
    
    cmd = "cmake -G\"Eclipse CDT4 - Ninja\" -DCMAKE_INSTALL_PREFIX=../install \
        -DCMAKE_MAKE_PROGRAM=ninja \
        -DRTEMS_TOOLCHAIN_ROOT=D:/Projekte/arm-sickag-rtems5 \
        -DCMAKE_TOOLCHAIN_FILE=D:/Projekte/OpenSource/next/System/OS/rtems/cmake/toolchain/rtems5-stm32f7x7.cmake \
        -DCMAKE_VERBOSE_MAKEFILE=ON \
        -DRTEMS_CPU=arm \
        -DRTEMS_NETWORKING=1 \
        -DRTEMS_POSIX_API=1 \
        -DRTEMS_MULTIPROCESSING=0 \
        -DRTEMS_SMP=0 \
        -DRTEMS_ENABLE_RTEMS_DEBUG=0 \
        -DRTEMS_CXX=1 \
        -DRTEMS_TESTS=0 \
        -DRTEMS_PARAVIRT=0 \
        -DRTEMS_DRVMGR=0 \
        ../System/OS/rtems"
        
    run_cmd(cmd, buildFolder)

