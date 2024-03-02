n= int(input())

#N명의 학생 정보를 입력받아 리스트에 저장
student=[]
for i in range(n):
  name, score= input().split()
  student.append((name, int(score)))
  #input_data= input().split()
  #array.append((input_data[0], int(input_data[1]))) 로 작성해도됨

student=sorted(student, key=lambda x:x[1])
for i in student:
  print(i[0],end=' ')