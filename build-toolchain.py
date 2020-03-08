# Copyright (C) 2020, M.B.Moessner
#
# SPDX-License-Identifier: Apache-2.0 
#

from Modules.ctng import *


if __name__ == '__main__':
    argParser = argparse.ArgumentParser(description='Open SICK AG SDK')
    optArgs = argParser._action_groups.pop()
    optArgs.add_argument('-a', '--architecture',
                         help="select the target architecture"
                         "(default=arm)",
                         default="arm")
    optArgs.add_argument('-host', '--hostos',
                         help="select the host operating system"
                         "(default=linux)",
                         default="linux")
    
    
    argParser._action_groups.append(optArgs)
    args = argParser.parse_args()
    cwd = os.getcwd()
    ctng_prefix = cwd + "/Tools/ctng"
    toolchain_prefix =  cwd + "/Tools/toolchain"

    build_dir = cwd + "/tmp-tc-build"

    logger.info("Initialize...")
    logger.info("Current directory: {0}".format(cwd))

    repospecfile = cwd  + "/System/SDK/Meta/git-repos.json"
    

    repo = get_repo_by_name(repospecfile, "ctng")

    if -1 == check_if_file_exits(ctng_prefix + "/bin/ct-ng"):
        if not os.path.exists(os.path.abspath(ctng_prefix+"/..")):
            os.mkdir(os.path.abspath(ctng_prefix+"/.."))
        if os.path.exists(cwd+repo["destination"]):
            shutil.rmtree(cwd+repo["destination"], ignore_errors=True)
        git_clone_repos(repospecfile)
        apply_patches(cwd, cwd+repo["destination"] ,cwd + "/System/SDK/patches/crosstool-ng")

        ctng_build_ctng(cwd, cwd+repo["destination"],ctng_prefix)


    ctng_build_toolchain(cwd+ "/System/SDK",build_dir,ctng_prefix,toolchain_prefix,args.architecture,args.hostos)
