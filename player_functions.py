def batting(dic):
    points = dic['runs']/2;

    if dic['runs'] > 50:
        points = points+5
    elif dic['runs'] > 100:
        points = points+10

    s_rate = (dic['runs']/dic['balls'])*100

    if s_rate > 80.0 and s_rate < 100.0:
        points = points+2
    elif s_rate > 100:
        points = points+4

    points = points+dic['four']
    points = points+(2*dic['six'])
    points = points+dic['field']

    return points

        
def bowling(dic):
    points = 10*dic['wkts']

    if dic['wkts'] >= 3 and dic['wkts'] <=4:
        points = points+5
    elif dic['wkts'] >= 5:
        points = points+10

    economy = dic['runs']/dic['overs']

    if economy > 3.5 and economy <= 4.5:
        points = points+4
    elif economy > 2.0 and economy  <= 3.5:
        points = points+7
    elif economy <= 2.0:
        points = points+10

    points = points+10*dic['field']
    
    return points
