print('подсчет корней квадратного уравнения ')
a=int(input('введите первый аргумент:'))
b=int(input('введите второй аргумент:'))
c=int(input('введите третий аргумент:'))
D=b**2-4*a*c
x1=float(-b+D**0.5)/2*a
x2=float(-b-D**0.5)/2*a
print('первый корень:',x1,'\nвторой корень:',x2)

