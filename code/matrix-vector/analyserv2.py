with open('dump', 'r', encoding='utf-8') as f:
    dumpData = f.readlines()

    modes = ["SIMD"]
    # modes = ["O0", "O1", "O2", "O3", "Vec", "Omp", "OmpVec", "SIMD"]
    modeNum = len(modes)
    perfList = [list() for i in range(modeNum)]

    num = 0
    ind = 0
    for line in dumpData:
        if "GFLOPS" in line:
            perfList[num].append(float(line.split(": ")[1]))
            ind += 1
            if ind % 25 == 0:
                num += 1

    for num in range(modeNum):
        print(modes[num])
        print("Min", min(perfList[num]))
        print("Average", sum(perfList[num])/len(perfList[num]))
        print("Max", max(perfList[num]))
        print("")
