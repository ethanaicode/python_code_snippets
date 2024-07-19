import random
import bisect
import os

print(random.random())

def custom_choice(questions, weights):
    cumulative_weights = []
    cumulative_sum = 0

    for weight in weights:
        cumulative_sum += weight
        cumulative_weights.append(cumulative_sum)

    random_number = random.random() * cumulative_sum
    index = bisect.bisect(cumulative_weights, random_number)
    return questions[index]

# 问题列表和对应的权重值
questions = ["问题1", "问题2", "问题3", "问题4"]
weights = [0.1, 0.3, 0.4, 0.2]

# selected_question = random.choices(questions, weights)[0]
selected_question = custom_choice(questions, weights)

print(f"抽取到的问题是: {selected_question}")
