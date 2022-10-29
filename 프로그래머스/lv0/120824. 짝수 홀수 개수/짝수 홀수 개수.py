def solution(num_list):
    cnt = {"odd" : 0,
          "even": 0}
    for num in num_list:
        if num % 2 == 0: cnt["even"] += 1
        else: cnt["odd"] += 1
    return [cnt["even"], cnt["odd"]]