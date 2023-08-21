def flatten(data):
    out = [] # 결과 리스트 저장 (평탄화)
    for item in data:
        if type(item) == list:
            out+=flatten(item)

        else:
            out.append(item)
    return out

example = [[1,2,3], [4,[5,6]], 7,[8,9]]
print("원본:", example)
print("변환:", flatten(example))

dictionary = {
    1: 1,
    2: 2
}

def fibonacci(n):
    if n in dictionary:
        return dictionary[n]
    else:
        output = fibonacci(n - 1) + fibonacci(n - 2)
        dictionary[n] = output
        return output
    
print("fibonacci(10)")