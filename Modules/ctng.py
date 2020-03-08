# Copyright (C) 2020, M.B.Moessner
#
# SPDX-License-Identifier: Apache-2.0 
#

from Modules.Git import *


def ctng_build_ctng(topDir, ctngSrc, prefix):
    logger.info("Boostrap crosstool-ng source")
    cmd = "./bootstrap"
    run_cmd(cmd, ctngSrc)
    cmd_env = os.environ.copy()
    cmd_env["CFLAGS"] = "-DKBUILD_NO_NLS"
    cmd = "./configure --prefix={0}".format(prefix)
    run_cmd(cmd, ctngSrc, env=cmd_env)
    cmd = "make"
    run_cmd(cmd, ctngSrc, env=cmd_env)
    cmd = "make install"
    run_cmd(cmd, ctngSrc, env=cmd_env)


def ctng_build_toolchain(topDir, buildDir,ctng_prefix,toolchain_prefix, arch, opsys):

    localbuildDir =  buildDir+"/build_" + arch + "_" + opsys
    cfgInputFile = topDir + "/configs/" + arch + ".config"

    if not os.path.isfile(cfgInputFile):
        logger.error("Configuration for target {0} not found".format(arch))
        sys.exit(-1)

    if os.path.exists(buildDir):
        shutil.rmtree(buildDir, ignore_errors=True)

    os.mkdir(buildDir)
    shutil.copy(cfgInputFile, buildDir)
  
    cfgInputFile = buildDir + "/" + arch + ".config"

    f = open(cfgInputFile,'r')
    cfg = f.read()
    f.close()

    cfg = cfg.replace("CT_PREFIX=","CT_PREFIX=\"{0}\"".format(toolchain_prefix))
    cfg = cfg.replace("CT_LOCAL_TARBALLS_DIR=","CT_LOCAL_TARBALLS_DIR=\"{0}/tarballs\"".format(ctng_prefix))

    f = open(cfgInputFile,'w')
    f.write(cfg)
    f.close()

    if opsys == "windows":
        f=open(cfgInputFile, "a+")
        f.write("CT_CANADIAN=y\n")
        f.write("CT_HOST=\"x86_64-w64-mingw32\"\n")
        f.close()


    if os.path.exists(localbuildDir):
        shutil.rmtree(localbuildDir, ignore_errors=True)

    if os.path.exists(toolchain_prefix):
        shutil.rmtree(toolchain_prefix, ignore_errors=True)

    os.mkdir(localbuildDir)

    cmd = "{0}/bin/ct-ng clean".format(ctng_prefix)
    run_cmd(cmd, localbuildDir)
    cmd = "{0}/bin/ct-ng defconfig DEFCONFIG={1}".format(ctng_prefix, cfgInputFile)
    run_cmd(cmd, localbuildDir)
    cmd = "{0}/bin/ct-ng savedefconfig DEFCONFIG={1}.config".format(ctng_prefix,arch)
    run_cmd(cmd, localbuildDir)
    cmd = "{0}/bin/ct-ng build.{1}".format(ctng_prefix,psutil.cpu_count())
    run_cmd_ng(cmd, localbuildDir)
