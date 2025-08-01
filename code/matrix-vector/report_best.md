## System Information
```### lscpuArchitecture:                       x86_64
CPU op-mode(s):                     32-bit, 64-bit
Address sizes:                      39 bits physical, 48 bits virtual
Byte Order:                         Little Endian
CPU(s):                             20
On-line CPU(s) list:                0-19
Vendor ID:                          GenuineIntel
Model name:                         12th Gen Intel(R) Core(TM) i7-12700H
CPU family:                         6
Model:                              154
Thread(s) per core:                 2
Core(s) per socket:                 14
Socket(s):                          1
Stepping:                           3
CPU(s) scaling MHz:                 48%
CPU max MHz:                        4700.0000
CPU min MHz:                        400.0000
BogoMIPS:                           5378.00
Flags:                              fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx pdpe1gb rdtscp lm constant_tsc art arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc cpuid aperfmperf tsc_known_freq pni pclmulqdq dtes64 monitor ds_cpl vmx smx est tm2 ssse3 sdbg fma cx16 xtpr pdcm sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand lahf_lm abm 3dnowprefetch cpuid_fault epb ssbd ibrs ibpb stibp ibrs_enhanced tpr_shadow flexpriority ept vpid ept_ad fsgsbase tsc_adjust bmi1 avx2 smep bmi2 erms invpcid rdseed adx smap clflushopt clwb intel_pt sha_ni xsaveopt xsavec xgetbv1 xsaves split_lock_detect user_shstk avx_vnni dtherm ida arat pln pts hwp hwp_notify hwp_act_window hwp_epp hwp_pkg_req hfi vnmi umip pku ospke waitpkg gfni vaes vpclmulqdq rdpid movdiri movdir64b fsrm md_clear serialize arch_lbr ibt flush_l1d arch_capabilities
Virtualization:                     VT-x
L1d cache:                          544 KiB (14 instances)
L1i cache:                          704 KiB (14 instances)
L2 cache:                           11.5 MiB (8 instances)
L3 cache:                           24 MiB (1 instance)
NUMA node(s):                       1
NUMA node0 CPU(s):                  0-19
Vulnerability Gather data sampling: Not affected
Vulnerability Itlb multihit:        Not affected
Vulnerability L1tf:                 Not affected
Vulnerability Mds:                  Not affected
Vulnerability Meltdown:             Not affected
Vulnerability Mmio stale data:      Not affected
Vulnerability Retbleed:             Not affected
Vulnerability Spec rstack overflow: Not affected
Vulnerability Spec store bypass:    Mitigation; Speculative Store Bypass disabled via prctl
Vulnerability Spectre v1:           Mitigation; usercopy/swapgs barriers and __user pointer sanitization
Vulnerability Spectre v2:           Mitigation; Enhanced / Automatic IBRS, IBPB conditional, RSB filling, PBRSB-eIBRS SW sequence
Vulnerability Srbds:                Not affected
Vulnerability Tsx async abort:      Not affected
```

## Observations
Optimisation | Min Time (ms) | Avg. Time (ms) | Max Time (ms) | Min GLOPs | Avg GFLOPs | Max GFLOPs | Speedup Avg. (Max)
---|---|---|---|---|---|---|---
O0 | 1.857ms | 2.00312ms | 2.616ms | 0.807939 | 1.060495 | 1.138163 | x1.0 (x1.0)
O1 | 0.517ms | 0.62696ms | 0.749ms | 2.821853 | 3.406938 | 4.088139 | x3.21 (x3.59)
O2 | 0.544ms | 0.6352ms | 0.764ms | 2.76645 | 3.35049 | 3.885235 | x3.16 (x3.41)
O3 | 0.534ms | 0.66316ms | 0.806ms | 2.622293 | 3.209714 | 3.957993 | x3.03 (x3.48)
Vec | 0.3ms | 0.36028ms | 0.51ms | 4.144251 | 5.962026 | 7.045227 | x5.62 (x6.19)
Omp | 0.193ms | 0.26876ms | 0.39ms | 5.419405 | 8.138677 | 10.95113 | x7.67 (x9.62)
OmpVec | 0.132ms | 0.19012ms | 0.279ms | 7.575513 | 11.611427 | 16.011879 | x10.95 (x14.07)
SIMD | 0.134ms | 0.14876ms | 0.182ms | 11.613011 | 14.293437 | 15.772896 | x13.48 (x13.86)
SIMD-Vec | 0.134ms | 0.1484ms | 0.275ms | 7.685702 | 14.529489 | 15.772896 | x13.7 (x13.86)
SIMD-Omp | 0.062ms | 0.08848ms | 0.198ms | 10.674586 | 25.773588 | 34.089806 | x24.3 (x29.95)
SIMD-OmpVec | 0.058ms | 0.09352ms | 0.192ms | 11.008167 | 25.137523 | 36.440828 | x23.7 (x32.02)


The max GFLOPs achieved: 36.440828 with SIMD-OmpVec optimisation.

The min time achieved: 0.058ms with SIMD-OmpVec optimisation.


## Conclusion
The best optimisation I could get is upto 36.44 GFLOPs (x32 speedup) with SIMD, OMP and other compiler flags

All the flags used can be found in the [Makefile](Makefile)

