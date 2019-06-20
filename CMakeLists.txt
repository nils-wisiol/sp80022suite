cmake_minimum_required(VERSION 3.14)
project(sp_800_22_suite C)

set(CMAKE_C_STANDARD 11)

include_directories(include)

add_executable(sp_800_22_suite
        include/cephes.h
        include/config.h
        include/decls.h
        include/defs.h
        include/externs.h
        include/generators.h
        include/genutils.h
        include/matrix.h
        include/stat_fncs.h
        include/utilities.h
        src/approximateEntropy.c
        src/assess.c
        src/blockFrequency.c
        src/cephes.c
        src/cusum.c
        src/dfft.c
        src/discreteFourierTransform.c
        src/frequency.c
        src/generators.c
        src/genutils.c
        src/linearComplexity.c
        src/longestRunOfOnes.c
        src/matrix.c
        src/nonOverlappingTemplateMatchings.c
        src/overlappingTemplateMatchings.c
        src/randomExcursions.c
        src/randomExcursionsVariant.c
        src/rank.c
        src/runs.c
        src/serial.c
        src/universal.c
        src/utilities.c)

target_link_libraries(sp_800_22_suite m)
