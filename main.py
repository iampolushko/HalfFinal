import socket
import requests
import sys
import csv
import itertools


def read_csv(agrv):
    path = None
    for param in sys.argv:
        path = param

    with open(path, 'r') as file:
        reader = csv.reader(file, delimiter=";")
        return list(itertools.chain.from_iterable(reader))


def check(elems_in_csv):
    for elem in elems_in_csv:
        print("current elem: " + elem)
        is_ip = False
        try:
            socket.inet_aton(elem)
            is_ip = True
        except:
            pass

        if (is_ip):
            try:
                socket_info = socket.gethostbyaddr(elem)
                socket_link = requests.get("https://" + socket_info[0])
                result_https = requests.get("Https://" + socket_link)
                result_http = requests.get("Http://" + socket_link)
                print(result_https)
                print(result_http)
            except Exception as e:
                print(e)

        else:
            try:
                result_https = requests.get("Https://" + elem)
                result_http = requests.get("http://" + elem)
                print(result_https)
                print(result_http)
            except ConnectionError:
                print("Invalid elem")
            except Exception as e:
                print(e)


def main():
    urls = read_csv(sys.argv)
    check(urls)
    print("test")



if __name__ == "__main__":
    main()

