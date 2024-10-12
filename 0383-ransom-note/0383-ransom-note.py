class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for note in set(ransomNote):
            if ransomNote.count(note) > magazine.count(note):
                return False
        return True