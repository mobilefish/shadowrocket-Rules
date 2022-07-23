import requests


def get_ad(url):
    res = requests.get(url)
    if res.status_code != 200:
        raise Exception('Connect error')
    return res.text.split('\n')

adlite_url = 'https://cdn.jsdelivr.net/gh/ACL4SSR/ACL4SSR@master/Clash/BanAD.list'

if __name__ == '__main__':
    reject = get_ad(adlite_url)
    ad_file = open('./clash/adlite.yaml', mode='w', encoding='utf-8')
    ad_file.write("# Convert from ACL4SSR/ACL4SSR\n")
    ad_file.write("payload:\n")
    for line in reject:
        if not line.startswith('#') and len(line) > 0:
            ad_file.write('  - %s\n' % line)
    ad_file.close()
    print('The adlite rule has been built successfully! Rule size: {}.'.format(len(reject)))
