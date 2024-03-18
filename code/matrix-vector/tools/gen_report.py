f = open("./build/output", "r", encoding="utf-8")

# include output of lscpu
lscpu = open("./tools/lscpu", "r", encoding="utf-8")
lscpu_text = lscpu.read()
lscpu.close()

report_text = ""


report_text += "## System Information\n"
report_text += "### lscpu\n\n"
report_text += "```"
report_text += lscpu_text
report_text += "```\n\n"


header = " | ".join(["Optimisation", "Min Time (ms)", "Avg. Time (ms)", "Max Time (ms)",
                    "Min GLOPs", "Avg GFLOPs", "Max GFLOPs", "Speedup Avg. (Max)"])
separator = "|".join(["---" for i in range(len(header.split("|")))])


mode = []
min_times = []
avg_times = []
max_times = []
min_gflops = []
avg_gflops = []
max_gflops = []

for line in f.readlines():
    if line == "\n":
        continue

    if "Min. Time" in line:
        secs = line.split()[2][:-1]
        time = float(secs) * 1000
        min_times.append(str(round(time, 6)) + "ms")
    elif "Avg. Time" in line:
        secs = line.split()[2][:-1]
        time = float(secs) * 1000
        avg_times.append(str(round(time, 6)) + "ms")
    elif "Max. Time" in line:
        secs = line.split()[2][:-1]
        time = float(secs) * 1000
        max_times.append(str(round(time, 6)) + "ms")

    elif "Min" in line:
        min_gflops.append(round(float(line.split()[1]), 6))
    elif "Average" in line:
        avg_gflops.append(round(float(line.split()[1]), 6))
    elif "Max" in line:
        max_gflops.append(round(float(line.split()[1]), 6))
    else:
        mode.append(line.split()[0])

report_text += "## Observations\n"
report_text += header + "\n" + separator + "\n"

for ind, val in enumerate(mode):
    report_text += " | ".join(
        [mode[ind],
         min_times[ind], avg_times[ind], max_times[ind],
         str(min_gflops[ind]), str(avg_gflops[ind]), str(max_gflops[ind]),
         f"x{round(float(avg_gflops[ind])/float(avg_gflops[0]), 2)}"
         f" (x{round(float(max_gflops[ind])/float(max_gflops[0]), 2)})"]
    ) + "\n"

report_text += "\n\n"
report_text += "The max GFLOPs achieved: " + \
  str(  max(max_gflops)) + " with " + \
    mode[max_gflops.index(max(max_gflops))] + " optimisation.\n\n"
report_text += "The min time achieved: " + \
    min(min_times) + " with " + \
    mode[min_times.index(min(min_times))] + " optimisation.\n"

report_text += "\n\n## Conclusion\n"
report_text += "The best optimisation I could get is upto 36.44 GFLOPs (x32 speedup) with SIMD, OMP and other compiler flags\n\n"
report_text += "All the flags used can be found in the [Makefile](Makefile)\n\n"
report_text += "\n\n"
report_text += "OMP performance was the best at 4 threads as can be observed in the figure below\n\n"
report_text += "![OMP Performance](threads.png)\n\n"
report_text += "The code was run with battery plugged in. Performance almost halved when running on battery\n\n"
report_text += "The code was run on a 20 core Intel i7 12th gen machine\n\n"


report_file = open("report.md", "w", encoding="utf-8")
report_file.write(report_text)
report_file.close()
