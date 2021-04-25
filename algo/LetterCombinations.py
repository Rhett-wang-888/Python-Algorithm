# @title: LetterCombination
# @description: TODO 电话号码和字母组合
# @author  Rhett
# @date 2021/4/25 17:00
from typing import List


def letterCombinations(digits:str)->List[str]:
    if not digits:
        return list()

    phoneMap={
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }
    def backtrack(index:int):
        if index==len(digits):
            combinations.append("".join(combination))
        else:
            digit=digits[index]
            for letter in phoneMap[digit]:
                combination.append(letter)
                backtrack(index+1)
                combination.pop()


    combinations=list()
    combination=list()
    backtrack(0)
    return combinations