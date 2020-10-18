import marshal
f=open('__init__.pyc','rb')
data=marshal.load(f)
exec(data)
