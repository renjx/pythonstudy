import pandas as pd

class XH9Error(Exception):pass

class HealthInfo:
    def __init__(self,*args0,**args1):
        if 9999999<args1['xh']<100000000:
            self.xh = args1['xh']
        else:
            raise XH9Error('学号{}需要是8位数'.format(args1['xh']))
            
        self.xm = args1['xm']
        self.ma = args1['ma']
        self.bj = args1['bj']
        self.xy = args1['xy']
        self.yy = args1['yy']
    def __repr__(self):
        return '(学号:{}，姓名:{}，健康码:{},班级:{},学院:{},原因:{})'.format(self.xh,self.xm,self.ma,self.bj,self.xy,self.yy) 
    
    @staticmethod
    def getstudentfromexcel(filename):
        xls = pd.ExcelFile(filename)
        valuehb = xls.parse('湖北旅居史')
        valuejw = xls.parse('境外人员')
        studentshealthinfo = []
        for i in range(valuehb.shape[0]):

            try:
                studentshealthinfo.append(HealthInfo(xh=int(valuehb.iloc[i,0]), xm=valuehb.iloc[i,1], xy=valuehb.iloc[i,3],bj=valuehb.iloc[i,4],ma=valuehb.iloc[i,5],yy='湖北旅居史'))
            except Exception as e:
                print(e)
        for i in range(valuejw.shape[0]):

            try:
                studentshealthinfo.append(HealthInfo(xh=int(valuehb.iloc[i,0]), xm=valuehb.iloc[i,1], xy=valuehb.iloc[i,3],bj=valuehb.iloc[i,4],ma=valuehb.iloc[i,5],yy='境外旅居史'))
            except Exception as e:
                print(e)
        return studentshealthinfo

def test():
    try:
        stu0 = HealthInfo(xh=11111111,xm='haha',ma='红码',bj='111',xy='rrrr',yy='在国外')
        print(stu0)
    except XH9Error as e:
        print(e)


    try:
        stus = HealthInfo.getstudentfromexcel('excel.xlsx')
    except Exception as e:
        print(e)
    else:
        print(stus)
        
if __name__ == '__main__':
    test()