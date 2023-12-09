


def filter_strings(arr):
    result = []
    for string in arr:
        if len(string) <= 3:
            result.append(string)
    return result

# Примеры использования
input_array = ["Hello", "2", "world", ":-)"]
result_array = filter_strings(input_array)
print(result_array)
