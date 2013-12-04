filename="input.txt"
def read_file(filename):
    buff=[]
    f=open(filename,"r")
    #split by ; and strip
    buff=[[x.strip() for x in l.split(";")] for l in f]
    f.close()
    buff.pop(0)
    return buff

#map of fields
fmap={
    'bool': 'BooleanField',
    'str':  'CharField',
    'int':  'IntegerField',
    'uint': 'PositiveIntegerField',
    'date': 'DateField',
    'dt':   'DateTimeField',
    'float':'FloatField',
    'email':'EmailField',
    'url':  'UrlField',
#    '':'',
#    '':'',
        }

#base string to fill
s = "\t%s = models.%s('%s'%s%s)"

out=[]
if __name__ == "__main__":
    buff = read_file(filename)
    for (ftype, name, descr, nullable, default) in buff:
        args1 = args2 = ""
        if ftype in fmap:
           field_type = fmap[ftype] 
        else: #attention - no field defined
            field_type = "!!!Field"
        if nullable == "True": #TODO won't work with NullBooleanField nad sth else I'm sure
            args1 = ", null=True, blank=True"
        if default:
            args2 = ", default=%s"%default
        out.append( s % (name, field_type, descr, args1, args2 ) )
    print "\n".join(out)
