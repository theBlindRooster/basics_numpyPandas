def dupInt(start, stop, inter, dups):
    outp=[]
    for x in range(dups):
        outp=np.concatenate((outp, np.arange(start,stop,inter)))
        x+=1
    return outp

def randInt(start, stop, inter, numret):
    arr=dupInt(start, stop, inter, numret)
    while len(arr) > numret:
        arr = np.delete(arr,round((len(arr)-1)*np.random.rand()-1))
    return arr

def dupDates(start, periods, dups):
    outp=[]
    for x in range(dups):
        dates=pd.date_range(start=start, periods=periods)
        outp.extend(dates)
        x+=1
    return outp

def randDates(start, periods, numret):
    arr=dupDates(start, periods, (numret))    
    while len(arr) > numret:
        arr.pop(round((len(arr)-1)*np.random.rand()-1))
    return arr
	
