with open('build/dump', 'r', encoding='utf-8') as f:
    dumpData = f.readlines()

    # modes = ["Vec", "OMP"]
    modes = ["O0", "O1", "O2", "O3", "Vec", "Omp",
             "OmpVec", "SIMD", "SIMD-Vec", "SIMD-Omp", "SIMD-OmpVec"]

    modeNum = len(modes)
    perfList = [list() for i in range(modeNum)]
    timeList = [list() for i in range(modeNum)]

    num = 0
    for line in dumpData:
        if "GFLOPS" in line:
            perfList[num].append(float(line.split(": ")[1]))
            num = (num + 1) % modeNum
        if "Time" in line:
            timeList[num].append(float(line.split()[2]))

    for num in range(modeNum):
        assert len(perfList[num]) == len(timeList[num])

    for num in range(modeNum):
        print(modes[num])
        print(f"Min. Time {min(timeList[num])}s")
        print(f"Avg. Time {sum(timeList[num])/len(timeList[num])}s")
        print(f"Max. Time {max(timeList[num])}s")
        print("Min", min(perfList[num]))
        print("Average", sum(perfList[num])/len(perfList[num]))
        print("Max", max(perfList[num]))
        print("")
