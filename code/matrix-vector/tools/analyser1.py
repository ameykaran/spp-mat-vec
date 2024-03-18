import matplotlib.pyplot as plt
import os 

threads = 50

with open('./build/dump1', 'r', encoding='utf-8') as f:
    dumpData = f.readlines()

    times = [[] for i in range(threads)]
    flops = [[] for i in range(threads)]

    it = 0
    for line in dumpData:
        ind = it // 10
        if "Time" in line:
            times[ind].append(float(line.split()[2]))
            # it += 1
        if "FLOPS" in line:
            flops[ind].append(float(line.split()[1]))
            it += 1
    
    minTimes = [min(times[i]) for i in range(threads)]
    maxTimes = [max(times[i]) for i in range(threads)]
    avgTimes = [sum(times[i]) / len(times[i]) for i in range(threads)]
    minFlops = [min(flops[i]) for i in range(threads)]
    maxFlops = [max(flops[i]) for i in range(threads)]
    avgFlops = [sum(flops[i]) / len(flops[i]) for i in range(threads)]

    # plt.plot(avgTimes, label='Average time')
    # plt.plot(minTimes, label='Minimum time')
    # plt.plot(maxTimes, label='Maximum time')
    # plt.xlabel('Iteration')
    # plt.ylabel('Time (s)')
    # plt.title('Time')
    # plt.legend()
    # plt.show()

    plt.plot(avgFlops, label='Average FLOPS')
    plt.plot(maxFlops, label='Maximum FLOPS')
    plt.xlabel('Num of threads')
    plt.ylabel('GFLOPS')
    plt.title('GFLOPS vs threads')
    plt.legend()
    plt.show()
    # plt.savefig(f'flops{}.png')

    