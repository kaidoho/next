# Copyright (C) 2020, M.B.Moessner
#
# SPDX-License-Identifier: Apache-2.0 
#

from Modules.Git import *
from Modules.ConfigParser import *

def rtems_clean_src_dir(rdir):
    logger.info("Remove old CMake additions")

    if os.path.exists(rdir + "/cmake"):
        logger.info("\tDelete folder: {0}".format(rdir + "/cmake"))
        shutil.rmtree(rdir + "/cmake", ignore_errors=True)
    for f in glob.iglob(rdir + "/**/CMakeLists.txt", recursive=True):
      os.remove(f)

def rtems_copy_in_static_cmake_files(rdir):
    logger.info("Copy in static CMake files")

    cmScriptInDir = os.getcwd() + "/cmake/RTEMS"
    cmakeScriptOutDir = rdir

    filesToCopy = []
    for filename in glob.iglob(cmScriptInDir + "/**/*.*", recursive=True):
        filesToCopy.append(os.path.relpath(filename, cmScriptInDir))

    for i in range(len(filesToCopy)):
        tmpPath = os.path.dirname(os.path.abspath(cmakeScriptOutDir + "/" + filesToCopy[i]))
        if not os.path.exists(tmpPath):
            logger.info("\tCreate folder: {0}".format(tmpPath))
            os.makedirs(tmpPath, exist_ok=True)
        logger.info("\tCopy file: {0}".format(filesToCopy[i]))
        shutil.copy2(cmScriptInDir + "/" + filesToCopy[i], cmakeScriptOutDir + "/" + filesToCopy[i])





def rtems_add_cmake(repospecfile):
    cwd = os.getcwd()


    repo = get_repo_by_name(repospecfile,"rtems")
    repodir = cwd+repo["destination"]

    logger.info("Bootstrap RTEMS")
    logger.info("Current work directory: {0}".format(cwd))
    logger.info("RTEMS directory: {0}".format(repodir))


    git_clone_repos(repospecfile)

    rtems_clean_src_dir(repodir)
    rtems_copy_in_static_cmake_files(repodir)

    Parser = CpukitParser(repodir)
    Parser.parseMakefile()
