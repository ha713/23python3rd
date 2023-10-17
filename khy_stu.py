#5명의 성적을 입력을 받아 평균을 내는 프로그램을 만든다.
#반복문과 조건문을 사용한다.
#변수는  total, counter, grade, average
total =  0          #  변수 total은 0으로 선언 하였다.
counter = 1             # 변수 counter은 1로 선언 하였다.
while  counter <= 10:      # 반복문 whil을 사용하여 counter가 10보다 작거나 같을때 다음 내부문장으로 넘어간다.
            grade = int(input("성적을 입력하시오.:")) # 변수 grade에 int(정수형 변환 ) 와 사용자로부터 입력을 받는 input을 사용하여 정수를 받는다.
            total = grade + total           # 변수 total의  성적 grade와 변수 toal을 합한 값을  선언한다.
            counter = counter + 1        # 변수 counter는 초기 선언한 counter의 값에 실행할 때 마다 1씩 추가된다.
average = total/10          # 변수 averge에 반복문에서 계산한 total 값을 10으로 나눈다.
print(average)
# write by  김하영

