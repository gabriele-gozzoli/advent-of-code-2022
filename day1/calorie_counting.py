import os


def calculate_calories():
    calories = []
    calories_cnt = 0
    input_path = os.path.join(os.path.dirname(__file__), "./input")
    with open(input_path) as f:
        for line in f:
            if calorie := line.strip():
                calories_cnt += int(calorie)
            else:
                calories.append(calories_cnt)
                calories_cnt = 0

    calories.sort(reverse=True)
    part_one_res = calories[0]
    print(part_one_res)
    part_two_res = sum(calories[0:3])
    print(part_two_res)


if __name__ == '__main__':
    calculate_calories()
