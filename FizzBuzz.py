def fizzBuzz(n: int):
    answer = []
    fizz_buzz_dic = {3: 'Fizz', 5: 'Buzz', 7: 'Jazz'}
    for num in range(1, n + 1):
        current_answer = ''
        for key in fizz_buzz_dic.keys():
            if num % key == 0:
                current_answer += fizz_buzz_dic[key]
        if not current_answer:
            current_answer = str(num)
        answer.append(current_answer)
    return answer


print(fizzBuzz(15))




print(fizzBuzz(5))
