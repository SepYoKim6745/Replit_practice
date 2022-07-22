# n = 배열의 크기 // m = 더해지는 횟수 // k = 중복 사용 횟수
n, m, k = map(int, input().split())
data = list(map(int , input().split()))
data.sort()
first = data[n-1]
second = data[n-2] 

cnt = int(m / (k+1)) * k # 전체 길이에서 수열을 나눈다. 
                        # 그 후 중복 횟수만큼 곱한다.

cnt += m % (k+1) # 전체 길이에서 수열이 나누어 떨어지지 않을 경우

result = 0
result += (cnt) *  first
result += (m-cnt) * second # m - cnt를 하는 이유는 cnt는 제일 큰 수의 더해지는 횟수만 구했기 떄문
print(result)

# 제한시간동안 실패!!