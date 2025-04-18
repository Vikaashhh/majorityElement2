class Solution:
    # Function to find the majority elements in the array
    def findMajority(self, arr):
        n = len(arr)
        
        # Agar array empty hai to seedha empty list return kar do
        if not arr:
            return []

        # Teen variables - do candidate aur unke counters
        count1, count2 = 0, 0
        candidate1, candidate2 = None, None

        # Pehla pass - Moore's Voting Algorithm ka extended version (for > n/3)
        for num in arr:
            if candidate1 == num:
                count1 += 1  # candidate1 mila to uska count badhao
            elif candidate2 == num:
                count2 += 1  # candidate2 mila to uska count badhao
            elif count1 == 0:
                candidate1, count1 = num, 1  # naya candidate1 assign karo
            elif count2 == 0:
                candidate2, count2 = num, 1  # naya candidate2 assign karo
            else:
                count1 -= 1  # dono match nahi kiye, dono ka count ghatao
                count2 -= 1

        # Dusra pass - confirm karo ki in dono ka actual count > n/3 hai ya nahi
        result = []
        if arr.count(candidate1) > n // 3:
            result.append(candidate1)
        if candidate2 != candidate1 and arr.count(candidate2) > n // 3:
            result.append(candidate2)

        # Sorted output mein return karo
        return sorted(result) if result else []


# Test code to run
if __name__ == "__main__":
    arr = [2, 1, 5, 5, 5, 5, 6, 6, 6, 6, 6]
    ob = Solution()
    ans = ob.findMajority(arr)
    print("Output:", " ".join(map(str, ans)))  # Expected Output: 5 6