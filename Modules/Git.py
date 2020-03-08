# Copyright (C) 2020, M.B.Moessner
#
# SPDX-License-Identifier: Apache-2.0 
#


from Modules.Utils import *

def git_clone_repo(repo):
    cwd = os.getcwd()
    repodir = cwd+format(repo['destination'])

    if os.path.exists(repodir):
        logger.info("Repository {0} already cloned".format(repo['source']) )
    else:
        top = os.path.abspath(repodir + "/..")
        if not os.path.exists(top):
            os.makedirs(top, exist_ok=True)
            logger.info("Clone repository {0}".format(repo['source']) )

        cmd = "git clone {0}".format(repo['source'])
        run_cmd(cmd, top)

        if repo['commit'] != "latest":
            cmd = "git checkout {0}".format(repo['commit'])
            run_cmd(cmd, repodir)


def git_clone_repos(repospecfile):

    if os.path.isfile( repospecfile ):
        with open( repospecfile , 'r') as f:
            repospec = json.load(f)
            repos = repospec['repo']
            for repo in range(len(repos)):
                git_clone_repo(repospec['repo'][repo])

    else:
        logger.error("Repo specification not found at {0}".format(repospecfile))
        sys.exit(-1)
