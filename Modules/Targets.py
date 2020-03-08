# Copyright (C) 2020, M.B.Moessner
#
# SPDX-License-Identifier: Apache-2.0 
#


from Modules.Utils import *


class Depender():
  __dependencyDepth = 0
  __dependencyNames = []

  def __init__(self):
    self.__dependencyDepth = 0
    self.__dependencyNames = []

  def findDependency(self, makefile, searchString):
    linenumber = 1
    with open(makefile, 'r') as f:
      line = f.readline()

      ldependencyDepth = 0;
      ldependencyNames = ['empty']

      while line:
        line = line.rstrip()

        idx = line.find("if ")
        if 0 == idx:
          ldependencyDepth = ldependencyDepth + 1;
          ldependencyNames.append(line[3:])

        idx = line.find('endif')
        if 0 == idx:
          ldependencyDepth = ldependencyDepth - 1;
          del ldependencyNames[-1]

        idx = line.find(searchString)
        if -1 != idx:
          self.__dependencyDepth = ldependencyDepth
          self.__dependencyNames = ldependencyNames[:]
          break
        if ldependencyDepth < 0:
          self.logger.error("ERROR: this should not happen at line " + str(linenumber))
          sys.exit()
        linenumber = linenumber + 1;
        line = f.readline()

  def setDependencyDepth(self, depth):
    self.__dependencyDepth = depth

  def setDependencyNames(self, names):
    self.__dependencyNames = names

  def getDependencyDepth(self):
    return self.__dependencyDepth

  def getDependencyNames(self):
    return self.__dependencyNames


class SourceFile(Depender):
  __sourcePath = ""

  def __init__(self, pfile):
    super().__init__()
    self.__sourcePath = pfile

  def getSourcePath(self, topCmFile):
    ret = os.path.relpath(self.__sourcePath, topCmFile)
    return ret.replace("\\", "/")


class LibraryTarget(Depender):
  __name = ""
  sourceDir = ""
  blockIncludeFiles = []
  __sourceFiles = []
  __c_flags = []
  __cpp_flags = []

  def __init__(self,  name, sourceDir):
    super().__init__()
    self.__name = name
    self.sourceDir = sourceDir
    self.blockIncludeFiles = []
    self.__sourceFiles = []
    self.__c_flags = []
    self.__cpp_flags = []
    return

  def getName(self):
    return self.__name

  def getNumberOfSourceFiles(self):
    return len(self.__sourceFiles)

  def findLibraryDependencies(self, makefile):
    findstring = "project_lib_LIBRARIES += lib" + self.__name + ".a"
    self.findDependency(makefile, findstring)

  def addSourceFile(self, sFile):
    self.__sourceFiles.append(sFile)

  def setCompilerFlags(self, c_flags, cpp_flags):
    self.__c_flags = c_flags
    self.__cpp_flags = cpp_flags

  def getCFlags(self):
    return self.__c_flags

  def getCppFlags(self):
    return self.__cpp_flags

  def getSourceFiles(self):
    return self.__sourceFiles

  def printSourceDependencys(self):

    for i in range(len(self.__sourceFiles)):
      self.__sourceFiles[i].printSourceDependency()

  def addArchitectureIncludePaths(self, cmakefile, searchPath):

    headerPath = searchPath
    idx = headerPath.find("score")
    if -1 != idx:
      headerPath = headerPath[idx:]
      headerPath = headerPath.replace("\\", "/")

    cmakefile.write("set(CPU_HEADER_DIR \"${PROJECT_SOURCE_DIR}/")
    cmakefile.write(headerPath)
    cmakefile.write("\")\n")

    headerPath = headerPath + "/include"

    cmakefile.write("include_directories (\"${PROJECT_SOURCE_DIR}/")
    cmakefile.write(headerPath)
    cmakefile.write("\")\n")

  def findBlockFlags(self, makefile):
    searchString = "lib" + self.__name + "_a_CFLAGS +="
    linenumber = 1
    with open(makefile, 'r') as f:
      line = f.readline()

      while line:
        if -1 != line.find(searchString):

          idx = line.find(" += -I")
          if -1 != idx:
            line = line[idx + 6:]
            self.logger.info("Found CFLAGS: " + line)
        line = f.readline()

    searchString = "lib" + self.name + "_a_CPPFLAGS +="
    with open(makefile, 'r') as f:
      line = f.readline()
      while line:
        line = line.rstrip()
        if -1 != line.find(searchString):
          idx = line.find(" += -I")
          if -1 != idx:
            line = line[idx + 6:]
            self.logger.info("Found CPPFLAGS: " + line)
            line = line.replace("$(srcdir)", "${PROJECT_SOURCE_DIR}")
            line = line.replace("$(RTEMS_SOURCE_ROOT)", "${PROJECT_SOURCE_DIR}/../../../../../..")
            self.logger.info("Found CPPFLAGS: " + line)
            self.blockIncludeFiles.append(line)
        line = f.readline()

  def writeTargetIncludeFiles(self, cmakefile, name):
    for i in range(len(self.blockIncludeFiles)):
      headerPath = self.blockIncludeFiles[i]
      idx = headerPath.find("cpukit")
      if -1 != idx:
        headerPath = headerPath[idx + 6:]
        headerPath = headerPath.replace("\\", "/")
      cmakefile.write("target_include_directories(" + name + " PUBLIC\n")
      cmakefile.write("$<BUILD_INTERFACE:" + self.blockIncludeFiles[i] + ">)\n")


class BspSwitchHelper():
  __clause = ""
  __value = ""

  def __init__(self, clause, value):
    self.__clause = clause
    self.__value = value

  def getClause(self):
    return self.__clause

  def getValue(self):
    return self.__value


class BspSwitch():
  __name = ""
  __helper = []

  def __init__(self, name):
    self.__name = name
    self.__helper = []

  def getName(self):
    return self.__name

  def addClause(self, clause, value):

    idx = clause.find("|")
    if -1 != idx:
      while -1 != idx:
        self.__helper.append(BspSwitchHelper(clause[:idx], value))
        clause = clause[idx + 2:]
        idx = clause.find("|")
    self.__helper.append(BspSwitchHelper(clause, value))

  def getClauses(self):
    return self.__helper
