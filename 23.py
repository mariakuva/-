a=int(input())
hour=a//3600
minute=a//60%60
second=a%60
print(hour,"часов", minute, "минут", second ,"секунд")