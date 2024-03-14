with open('dump', 'r', encoding='utf-8') as f:
    dumpData = f.readlines()

    # modes = ["Omp"]
    modes = ["O0", "O1", "O2", "O3", "Vec", "Omp", "OmpVec"]
    modeNum = len(modes)
    perfList = [[] for i in range(modeNum)]

    num = 0
    for line in dumpData:
        if "GFLOPS/s" in line:
            perfList[num].append(float(line.split(": ")[1]))
            num = (num + 1) % modeNum

    for num in range(modeNum):
        print(modes[num])
        print("Min", min(perfList[num]))
        print("Average", sum(perfList[num])/len(perfList[num]))
        print("Max", max(perfList[num]))
        print("")
