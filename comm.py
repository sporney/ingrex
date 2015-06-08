"COMM monitor"
import ingrex
import time
import datetime

def main():
    "main function"
    field = {
        'minLngE6':116298171,
        'minLatE6':39986831,
        'maxLngE6':116311303,
        'maxLatE6':39990941,
    }
    with open('cookies') as cookies:
        cookies = cookies.read().strip()

    mints = -1

    while True:
        intel = ingrex.Intel(cookies, field)
        result = intel.fetch_msg(mints)
        if result:
            mints = result[0][1] + 1
        print(mints)
        for item in result[::-1]:
            date = datetime.datetime.fromtimestamp(item[1] // 1000)
            date += datetime.timedelta(milliseconds=(item[1] % 1000))
            print('{} {}'.format(date.strftime('%Y/%m/%d %H:%M:%S:%f')[:-3], item[2]['plext']['text']))
        time.sleep(10)

if __name__ == '__main__':
    main()
