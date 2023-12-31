"""
https://leetcode.com/problems/binary-search/solutions/

Его величество Binary search

Есть отсортированная коллекция из элментов, найти эл-нт:
1. Завести переменные границы, левая с нулевого индекса, правая равна длине списка `(left, right)`
2. Сравнить является ли левая граница и правая граница таргетом `left or right == target`
3. Поделить на 2 нацело и взять элемент посередине `(right+left)//2`
4. Проверить `mid == target`
5. Если нет, тогда проверяю эле-т больше или меньше искомого? `mid < target`
6. Если `mid` меньше тогда передвигаю левую границу на середину `left = mid + 1` и проверяю, всё что правее
7. Или наоборот `right = mid`
8. Повторяю пункты со 2 по 4 с помощью `while loop`

- Исправил правую границу, которая выходила за индекс
- Цикл while теперь не отваливается, если у нас всего один эл-т и его надо проверить
- не проверяю лишний раз левую и правую границу с помощью сдвига индекса + 1
"""


class Solution:
    
    def search(self, nums: list, target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (right + left) // 2 # может возникнуть переполнение при больших числах для этого `left + ((right - left) // 2)` из-за знака - вычисления не так велики
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
    
    
s = Solution()
assert(s.search([1, 15, 28, 32, 35, 36, 48], 15) == 1)

#повторение
def binary_search(nums, target) -> int:
    left, right = 0, len(nums)
    while left<=right:
        mid = ((right-left) // 2) + left
        if target == nums[mid]:
            return mid
        elif target < nums[mid]:
            right = mid - 1
        else:
            left = mid + 1        
    return -1    
    