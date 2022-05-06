"""
백준 3107번 : IPv6
"""

input_ip = input()
ip_elements = list(input_ip.split(':'))
# print(ip_elements)

def solution():
    if input_ip[:2] == '::':
        # start as zeros
        for _ in range(2):
            ip_elements.pop(0)
        make_zeros = 8 - len(ip_elements)
        original_ip = ['0000' for _ in range(make_zeros)]
        for ip in ip_elements:
            if len(ip) != 4:
                prefix = '0' * (4 - len(ip))
                new = prefix + ip
                original_ip.append(new)
            else:
                original_ip.append(ip)
        return ":".join(original_ip)

    elif input_ip[-2:] == '::':
        # end as zeros
        for _ in range(2):
            ip_elements.pop()
        make_zeros = 8 - len(ip_elements)
        original_ip = []
        for ip in ip_elements:
            if len(ip) != 4:
                prefix = '0' * (4 - len(ip))
                new = prefix + ip
                original_ip.append(new)
            else:
                original_ip.append(ip)
        for _ in range(make_zeros):
            original_ip.append('0000')
        return ":".join(original_ip)
    else:
        # 중간에 :: 있거나 없는 경우
        make_zeros = 9 - len(ip_elements)
        original_ip = []
        for ip in ip_elements:
            if ip == '':
                for _ in range(make_zeros):
                    original_ip.append('0000')
            else:
                if len(ip) != 4:
                    prefix = '0' * (4 - len(ip))
                    new = prefix + ip
                    original_ip.append(new)
                else:
                    original_ip.append(ip)
        return ":".join(original_ip)


print(solution())