# def greet(name):
#     return f"Hello, {name}!"
# def square(number):
#     return number**2
# def max_of_two(a,b):
#     return max(a,b)
# na=str(input())
# num=int(input())
# num2=int(input())
# print(greet(na),square(num),max_of_two)

# def calculate_rectangle(width,height):
#     return width*height
# def calculate_perimeter(width,height):
#     return 2*(width+height)
# def describe_rectangle(width,height,unit="см"):
#     return f"{width}  и {height} "
# print(describe_rectangle(16,56))

# def example():
#     value = 20
#     var = 99
#     print(value)
# value = 10
# example()
# print(value)
# print(var)

# a=[1,15,25,78,2,6,23,6,32,89,32,44,534,332]
# a[4]=46
# a.append(110)
# a.pop(7)
# print(a[0])
# print(a[2])
# print(a[-1])
# print(a,len(a))

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(numbers[:3])
# print(numbers[-3:])
# print(numbers[3:7])
# print(numbers[0:len(numbers)+1:2])
# print(numbers[::-1])

# measurements=(56,45,23,74,12,74,34,87,67)
# measurements=list(measurements)
# measurements[0]=76
# measurements=tuple(measurements)
# el1=measurements[0]
# el2=measurements[1]
# print(el1)
# print(el2)
# print(measurements[0])
# print(measurements[-1])

# num=[1,15,25,78,2,6,23,6,32,89,32,44,534,332]
# count=len(num)
# summ=sum(num)
# mini=min(num)
# maxi=max(num)
# sr=summ/count
# copy=sorted(num)
# num.sort()
# print(count,summ,mini,maxi,sr,copy,num)

# def calculate_sum(numbers):
#     summ=0
#     for i in range(0,len(numbers)):
#         summ+=numbers[i]
#     return summ
# def find_min(numbers):
#     mini=100000000000
#     for i in range(0,len(numbers)):
#         if numbers[i]<mini:
#             mini=numbers[i]
#     return mini
# def find_max(numbers):
#     maxi=0
#     for i in range(0,len(numbers)):
#         if numbers[i]>maxi:
#             maxi=numbers[i]
#     return maxi
# num=[67,34,7653,234523,123354,12,4,56,2,6543434]
# print(sum(num))
# print(calculate_sum(num))
# print(max(num))
# print(find_max(num))
# print(min(num))
# print(find_min(num))

# def find_element(numbers, target):
#     for i in range(0,len(numbers)):
#         if numbers[i]==target:
#             return i
#     return -1
# a=[10,20,30,60,90,432,563]
# print(find_element(a,20))
# print(find_element(a,67))

# def analyze(numbers):
#     cort=(max(numbers),min(numbers),((sum(numbers))//len(numbers)))
#     return cort
# a=[10,123,233,23,64,34,76,45]
# el1=analyze(a)[0]
# el2=analyze(a)[1]
# el3=analyze(a)[2]
# print(el1,el2,el3)

# numbers = [-10, 3, -2, 8, -5]
# sor1=sorted(numbers)
# sor2=sorted(numbers,key=lambda x:abs(x))
# print(sor1)
# print(sor2)


def calculate_average(measurements):
    kol=0
    for i in measurements:
        kol+=i
    return kol/len(measurements)
def find_min(measurements):
    mini=100000000000
    for i in range(0,len(measurements)):
        if measurements[i]<mini:
            mini=measurements[i]
    return mini
def find_max(measurements):
    maxi=0
    for i in range(0,len(measurements)):
        if measurements[i]>maxi:
            maxi=measurements[i]
    return maxi
def count_above_average(measurements):
    average=calculate_average(measurements)
    count=0
    for i in measurements:
        if i>average:
            count+=1
    return count
def find_element(numbers, target):
    for i in range(0,len(numbers)):
        if numbers[i]==target:
            return i
    return -1
def analyze(numbers):
    cort=(find_max(num),find_min(num),calculate_average(num))
    return cort

num=[123,24,253,74,67,356,864,56,44,75,895]
maxi=analyze(num)[0]
mini=analyze(num)[1]
sr=analyze(num)[2]
target=67
pos=find_element(num,target)
print(f'количество измерен {len(num)}')
print(f'максимум {maxi}')
print(f'минимум {mini}')
print(f'средняя {sr}')
print(f'выше среднего кол {count_above_average(num)}')
print(f'индекс {pos}')
