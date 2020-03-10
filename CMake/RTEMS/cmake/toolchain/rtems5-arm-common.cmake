


set(RTEMS_TOP_ARCH  arm)



list(APPEND RTEMS_CPU_FLAGS -mthumb -mthumb-interwork)
list(APPEND RTEMS_CPU_FLAGS -march=armv7e-m+fp.dp)



include(${CMAKE_CURRENT_LIST_DIR}/rtems5-common.cmake)