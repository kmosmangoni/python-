#salary calculation with late & early time!!!
#
#
print("Here you can see your monthly salary with substraction for any problem (if have!!)")

month=int(input("enter no of days in month :"))
working_days=int(input("Enter working day: "))
salary_per_day=int(input("Enter the daily salary :"))
monthly_salary=int(working_days*salary_per_day)
print("monthly_salary: ",monthly_salary)
print("If you late in any days then please give us input......\n")
late_entry=int(input("enter the no of late days :"))

total_salary=0
final_salary=0
total_salary=int(total_salary)

if late_entry == 0:
     total_salary = int(monthly_salary)

if late_entry >= 3 and late_entry <= 6 :
     total_salary = int(monthly_salary - (salary_per_day*1))

if late_entry >6 and late_entry <=9:
     total_salary = int (monthly_salary - (salary_per_day*2))

if late_entry >9 and late_entry <= 12:
     total_salary = int(monthly_salary - (salary_per_day*3))
else :
     print("monthly_salary: ",monthly_salary)
     
print("If you late in any days then give us input.........")
early_leave=int(input("enter the no of early left days :"))

for i in range (1):
    if early_leave == 0:
         final_salary = int(total_salary)
    if early_leave == 4 and early_leave <8:
          final_salary = int(total_salary - (salary_per_day*1))
    if early_leave >= 8 and early_leave < 12:
          final_salary = int (total_salary - (salary_per_day*2))      
    else:
         print("total_salary: ",total_salary)

print(f"final saraly : {final_salary} taka")