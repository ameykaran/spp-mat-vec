f = open("./build/output", "r", encoding="utf-8")

header = " | ".join(["Optimisation", "Avg. Time (ms)",
                    "Min GLOPs", "Avg GFLOPs", "Max GFLOPs"])
separator = "|".join(["---" for i in range(len(header.split("|")))])


mode = []
times = []
min_glops = []
avg_glops = []
max_glops = []

for line in f.readlines():
    if line == "\n":
        # mode = mode + 1
        continue

    if "Avg. Time" in line:
        secs = line.split()[2][:-1]
        time = float(secs) * 1000
        times.append(str(round(time, 6)) + "ms")
    elif "Min" in line:
        min_glops.append(str(round(float(line.split()[1]), 6)))
    elif "Average" in line:
        avg_glops.append(str(round(float(line.split()[1]), 6)))
    elif "Max" in line:
        max_glops.append(str(round(float(line.split()[1]), 6)))
    else:
        mode.append(line.split()[0])

report_text = header + "\n" + separator + "\n"

for ind, val in enumerate(mode):
    report_text += " | ".join([mode[ind],
                               times[ind], min_glops[ind],
                               avg_glops[ind], max_glops[ind]]) + "\n"

report_file = open("report.md", "w", encoding="utf-8")
report_file.write(report_text)
report_file.close()
