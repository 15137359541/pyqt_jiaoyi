# _*_ coding:utf-8 _*_
import time,datetime
import schedule
import threading

class T_date():
    # 判断交易日
    def mnTime(self):
        """
        周六周日不加入数据库
         0 : '星期一',
        1 : '星期二',
        2 : '星期三',
        3 : '星期四',
        4 : '星期五',
        5 : '星期六',
        6 : '星期天',
        :return:
        """
        # 获取当前时间（小时分钟）
        now_time = datetime.datetime.now().strftime("%H:%M:%S")
        week = datetime.datetime.now().weekday()
        if week in [5, 6]:
            print("today is", week + 1)
            return False
        else:
            print("weekday is :", week + 1)
            print('now time is：', now_time)
            print(datetime.datetime.now())
            if "09:20:00" <= now_time <= "11:30:00" or "13:30:00" <= now_time <= "15:00:00" or "21:00:00" <= now_time <= "23:59:59" or "00:00:00" <= now_time <= "02:30:00":
                return True
            else:
                return False

                # schedule执行时，会有函数阻塞，所以使用多线程

    def _main(self):
        # 判断是否可以在规定的时间段
        flag = self.mnTime()
        if flag:
            pass
        else:
            pass

    def thread_method(self):
        threading.Thread(target=self._main()).start()

    # 每一秒执行一次查询
    def run(self):
        schedule.every(1).minutes.do(self.thread_method)

        while True:
            schedule.run_pending()

if __name__ == '__main__':
    date = T_date()
    date.run()