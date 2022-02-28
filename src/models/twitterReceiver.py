from json import JSONDecoder
import json
import os,subprocess

bearer_token = os.getenv('TWITTER_BEARER_TOKEN')
#url = 'https://api.twitter.com/2/tweets/search/recent?query=Apple&start_time=2022-02-24T00:00:00.000Z&end_time=2022-02-26T00:00:00.000Z'
url = 'https://api.twitter.com/2/tweets/search/recent?query=stock%20watch%20&max_results=100'
headers = f"Authorization: Bearer {bearer_token}"
get_command = f'curl.exe {url} -H "{headers}"'
#ret = subprocess.call(get_command)

proc = subprocess.Popen(get_command,stdout=subprocess.PIPE)
s = proc.stdout.read()
sd = s.decode('UTF-8')

sd_list = sd.split(" ")

symbols = [w for w in sd_list if w.isupper() and "$" in w]

dict = {}
for symbol in symbols:
    if "(" in symbol:
        a = list(symbol)
        a.remove("(")
        a_str = "".join(a)
        dict[a_str] = dict.get(a_str, 0) + 1
    else:
        dict[symbol] = dict.get(symbol, 0) + 1

print(list(reversed(sorted(dict.items(), key=lambda x: x[1]))))
