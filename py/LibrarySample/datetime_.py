from datetime import datetime,timezone,timedelta
# ------获取当前时间-------
now=datetime.now()
print(now)
# -------获取指定日期和时间----
dt=datetime(2015,5,1,19,20,20)
print(dt)
# -------datetime转换为timestamp----
print(dt.timestamp())
# -------timestamp转换为datetime----
t=1429417200.0
print(datetime.fromtimestamp(t))
print(datetime.utcfromtimestamp(t))
# ---------str转换为datetiem-----
cday=datetime.strptime('2015-6-1 18:19:50','%Y-%m-%d %H:%M:%S')
print(cday)
# ---------datetime转换为str-------
print(now.strftime('%Y-%m-%d %a,%b %d %H:%M:%S'))
# ---------datetime加减------------
print(now+timedelta(days=1,hours=10))
#--------本地时间转换为UTC时间-----
tz_utc_8 = timezone(timedelta(hours=8))#创建时区东8区
dt = now.replace(tzinfo=tz_utc_8)
print(dt)
# -----时区转换------------
print('时区转换')
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_dt)
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print(bj_dt)
tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt)
tokyo_dt2 = dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt2)