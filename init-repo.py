# Copyright (C) 2020, M.B.Moessner
#
# SPDX-License-Identifier: Apache-2.0 
#



from Modules.RTEMS import *



if __name__ == '__main__':

    
    cwd = os.getcwd()

    logger.info("Clone GIT Repositories...")
    repospecfile = cwd  + "/Meta/git-repos.json"

    logger.info("Extend RTEMS to build with CMake")
    rtems_add_cmake(repospecfile)

