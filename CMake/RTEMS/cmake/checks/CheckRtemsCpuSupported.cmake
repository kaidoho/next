function(check_rtems_cpu_supported)

  if(EXISTS ${PROJECT_SOURCE_DIR}/cpukit/score/cpu/${RTEMS_CPU})
    message(STATUS  "Checking if architecture ${RTEMS_CPU} is supported... yes" )
    
    if (${RTEMS_CPU} MATCHES "arm")
      set(CPU_ARM "1" CACHE INTERNAL "CPU_ARM")
    elseif (${RTEMS_CPU} MATCHES "bfin")
      set(CPU_BFIN "1" CACHE INTERNAL "CPU_BFIN")
    elseif (${RTEMS_CPU} MATCHES "epiphany")
      set(CPU_EPIPHANY "1" CACHE INTERNAL "CPU_EPIPHANY")
    elseif (${RTEMS_CPU} MATCHES "i386")
      set(CPU_I386 "1" CACHE INTERNAL "CPU_I386")
    elseif (${RTEMS_CPU} MATCHES "lm32")
      set(CPU_LM32 "1" CACHE INTERNAL "CPU_LM32")
    elseif (${RTEMS_CPU} MATCHES "m68k")
      set(CPU_M68K "1" CACHE INTERNAL "CPU_M68K")
    elseif (${RTEMS_CPU} MATCHES "mips")
      set(CPU_MIPS "1" CACHE INTERNAL "CPU_MIPS")
    elseif (${RTEMS_CPU} MATCHES "moxie")
      set(CPU_MOXIE "1" CACHE INTERNAL "CPU_MOXIE")
    elseif (${RTEMS_CPU} MATCHES "nios2")
      set(CPU_NIOS2 "1" CACHE INTERNAL "CPU_NIOS2")
    elseif (${RTEMS_CPU} MATCHES "no_cpu")
      set(CPU_NO_CPU "1" CACHE INTERNAL "CPU_NO_CPU")
    elseif (${RTEMS_CPU} MATCHES "or1k")
      set(CPU_OR1K "1" CACHE INTERNAL "CPU_OR1K")
    elseif (${RTEMS_CPU} MATCHES "powerpc")
      set(CPU_POWERPC "1" CACHE INTERNAL "CPU_POWERPC")
    elseif (${RTEMS_CPU} MATCHES "riscv")
      set(CPU_RISCV "1" CACHE INTERNAL "CPU_RISCV")
    elseif (${RTEMS_CPU} MATCHES "sh")
      set(CPU_SH "1" CACHE INTERNAL "CPU_SH")
    elseif (${RTEMS_CPU} MATCHES "sparc64")
      set(CPU_SPARC64 "1" CACHE INTERNAL "CPU_SPARC64")
    elseif (${RTEMS_CPU} MATCHES "sparc")
      set(CPU_SPARC "1" CACHE INTERNAL "CPU_SPARC")
    elseif (${RTEMS_CPU} MATCHES "v850")
      set(CPU_V850 "1" CACHE INTERNAL "CPU_V850")
    elseif (${RTEMS_CPU} MATCHES "x86_64")
      set(CPU_X86_64 "1" CACHE INTERNAL "CPU_X86_64")
    endif()
  else()
    message(FATAL_ERROR  "FAILED - architecture ${RTEMS_CPU} is not supported!" )
  endif()
  
endfunction()
