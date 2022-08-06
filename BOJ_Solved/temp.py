def solution(lines):
    """
    2016-09-15 00:00:00.000
    2016-09-15 23:59:59.999
    """
    time_series = [0 for _ in range(60000 * 60 * 24)]
    for l in lines:
        _, time, T = l.split()
        time = "".join(time.split("."))
        hour, minute, second = map(int, time.split(":"))
        idx = second + 60 * minute + 60 * 60 * hour
        cnt = T[:len(T) - 1] * 1000
        # cnt = int(float(T[:len(T)-1]) * 1000)
        while cnt != 0:
            time_series[idx] += 1
            cnt -= 1

    answer = max(time_series)
    return answer


if __name__ == "__main__":
    lines = [
"2016-09-15 20:59:57.421 0.351s",
"2016-09-15 20:59:58.233 1.181s",
"2016-09-15 20:59:58.299 0.8s",
"2016-09-15 20:59:58.688 1.041s",
"2016-09-15 20:59:59.591 1.412s",
"2016-09-15 21:00:00.464 1.466s",
"2016-09-15 21:00:00.741 1.581s",
"2016-09-15 21:00:00.748 2.31s",
"2016-09-15 21:00:00.966 0.381s",
"2016-09-15 21:00:02.066 2.62s"
]
    print(solution(lines))