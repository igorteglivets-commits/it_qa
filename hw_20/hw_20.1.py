import datetime
import os

LOG_KEY = "Key TSTFEED0300|7E3E|0400"


def extract_timestamp(line: str):

    idx = line.find("Timestamp ")
    if idx == -1:
        return None

    time_str = line[idx + 10: idx + 18]
    try:
        return datetime.datetime.strptime(time_str, "%H:%M:%S")
    except ValueError:
        return None


def analyze_heartbeat(input_file="hblog.txt", output_file="hb_test.log"):

    base_dir = os.path.dirname(os.path.abspath(__file__))

    input_path = os.path.join(base_dir, input_file)
    output_path = os.path.join(base_dir, output_file)

    previous_ts = None
    previous_line = None

    with open(input_path, "r") as f, open(output_path, "w") as logf:
        for line in f:

            if LOG_KEY not in line:
                continue

            ts = extract_timestamp(line)
            if ts is None:
                continue

            if previous_ts is None:
                previous_ts = ts
                previous_line = line
                continue

            diff = abs((ts - previous_ts).total_seconds())

            if 31 < diff < 33:
                logf.write(f"WARNING at {previous_ts.time()} heartbeat={diff} seconds\n")

            elif diff >= 33:
                logf.write(f"ERROR at {previous_ts.time()} heartbeat={diff} seconds\n")

            previous_ts = ts
            previous_line = line

    print(f"Готово Лог створено: {output_path}")


analyze_heartbeat()
