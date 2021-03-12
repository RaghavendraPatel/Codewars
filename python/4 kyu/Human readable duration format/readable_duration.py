def format_duration(sec):
    s=''
    m=0
    h=0
    d=0
    y=0
    se=0
    if sec==0:
        s='now'
    else:
        if int(sec/(3600*24*365))>0:
            y=1
            if int(sec/(3600*24*365))>1:
                 s=s+f"{int(sec/(3600*24*365))} years"
            else:
                s=s+f"{int(sec/(3600*24*365))} year"
        if int(sec/(3600*24)%365)>0:
            if y==1:
                s=s+', '
            d=1
            if int(sec/(3600*24)%365)>1:
                s=s+f"{int(sec/(3600*24)%365)} days"
            else:
                s=s+f"{int(sec/(3600*24))} day"
        if int(sec/3600)%24>0:
            h=1
            if d==1:
                s=s+', '
            if int(sec/3600)%24>1:
                s=s+f"{int(sec/3600)%24} hours"
            else:
                s=s+f"{int(sec/3600)%24} hour"
        if int(sec/60)%60>0:
            m=1
            if h==1 or d==1:
                s=s+', '
            if int(sec/60)%60>1:
                s=s+f"{int(sec/60)%60} minutes"
            else:
                s=s+f"{int(sec/60)%60} minute"
        if sec%60>0:
            se=1
            if m==1 or d==1:
                s=s+' and '
            if sec%60>1:
                s=s+f"{sec%60} seconds"
            else:
                s=s+f"{sec%60} second"
        if se==0:
            s=s.replace(f', {int(sec/60)%60} mi',f' and {int(sec/60)%60} mi')
    return s
