## Python program for implementation of atoi , this function takes a string and returns an integer


def python_atoi(ip_str):
    val = 0
    ip_str = ip_str[::-1]
    for i, v in enumerate(ip_str):
        val += int(v) * pow(10, i)
    return val

print python_atoi("1234")