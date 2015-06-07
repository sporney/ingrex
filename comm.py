import ingrex

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

    intel = ingrex.Intel(cookies, field)

    result = intel.fetch_msg()

    for item in result:


    print(result)

if __name__ == '__main__':
    main()
