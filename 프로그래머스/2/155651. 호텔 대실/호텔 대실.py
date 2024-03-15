def convert_to_second(time_string):
    splited_time = list(map(int, time_string.split(":")))
    return splited_time[0] * 60 + splited_time[1]

def solution(book_time):
    answer = 0
    time_table = [0 for _ in range(24 * 60 + 10)]
    
    for book in book_time:
        start = book[0]
        end = book[1]
        start_idx = convert_to_second(start)
        end_idx = convert_to_second(end) + 10
        for idx in range(start_idx, end_idx):
            time_table[idx] += 1
    
    return max(time_table)