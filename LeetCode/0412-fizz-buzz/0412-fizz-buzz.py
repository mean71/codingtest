class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        return [(str(i),'Fizz','Buzz','FizzBuzz')[(i%3==0)+2*(i%5==0)]for i in range(1,n+1)]