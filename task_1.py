def count_minutes(text=""):
    values = text.split(",")
    total_minutes = 0
    for i in range(len(values)):
        current_value = values[i].split(" ")
        for j in range(len(current_value)):
            time_str = current_value[j]
            if "h" in time_str:
                hours = int(time_str.replace("h", ""))
                total_minutes += hours * 60
            elif "m" in time_str:
                total_minutes += int(time_str.replace("m", ""))
            else:
                seconds = int(time_str.replace("s", ""))
                total_minutes += seconds / 60
    return int(total_minutes)
