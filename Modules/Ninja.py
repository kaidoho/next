# Copyright (C) 2020, M.B.Moessner
#
# SPDX-License-Identifier: Apache-2.0 
#


from Modules.Utils import *


def run_build(ninjaBin,workDir):
  if not os.path.exists(workDir):
    logger.error("Error build folder does not exist. Run config")
    sys.exit()

  cmd = [ninjaBin]
  cmd.append("-v")
  run_cmd(cmd, workDir)


def run_install(ninjaBin,workDir):
  if not os.path.exists(workDir):
    logger.error("Error build folder does not exist. Run config")
    sys.exit()

  cmd = [ninjaBin]
  cmd.append("install")
  cmd.append("-v")
  run_cmd(cmd, workDir)