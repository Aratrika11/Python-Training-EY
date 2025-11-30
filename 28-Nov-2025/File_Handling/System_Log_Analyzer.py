""" 10. System Log Analyzer
 Read system.log and count:
 number of ERROR lines
 number of WARNING lines
 number of INFO lines
 Write the summary into log_summary.txt ."""

error_cnt = 0
warning_cnt = 0
info_cnt = 0

with open("system.log","r") as f:
    for line in f:
        if "ERROR" in line:
            error_cnt += 1
        elif "WARNING" in line:
            warning_cnt += 1
        elif "INFO" in line:
            info_cnt += 1

with open("log_summary.txt","w") as f:
    f.write(f"ERROR lines: {error_cnt}\n")
    f.write(f"WARNING lines: {warning_cnt}\n")
    f.write(f"INFO lines: {info_cnt}\n")

print("System Log Analyzed")