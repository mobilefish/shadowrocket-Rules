import os
import time
import re


def get_from_file(path):
    file = open(path, 'r', encoding='utf-8')
    content = file.read()
    file.close()
    return content


values = {
    'build_time': time.strftime("%Y-%m-%d %H:%M:%S %Z"),
    'gfw': get_from_file(os.getcwd() + '/temp/gfw.txt'),
    'direct': get_from_file(os.getcwd() + '/temp/direct.txt'),
    'netease': get_from_file(os.getcwd() + '/temp/netease.txt'),
    'ad': get_from_file(os.getcwd() + '/temp/ad.txt'),
    'telegram': get_from_file(os.getcwd() + '/temp/telegram.txt'),
    'custom': get_from_file(os.getcwd() + '/temp/custom.txt'),
}

def gen_file(name):
    template_file = open(os.getcwd() + '/template/' + name + '-template.conf', mode='r', encoding='utf-8')
    template = template_file.read()
    output_file = open(os.getcwd() + '/gen/' + name +'.conf', mode='w', encoding='utf-8')
    marks = re.findall(r'{{(.+)}}', template)
    for mark in marks:
        template = template.replace('{{' + mark + '}}', values[mark])
    output_file.write(template)
    template_file.close()
    output_file.close()

file_names = [
    'gfw-ad-netease',
    'proxy-ad-netease'
]

if __name__ == '__main__':
    for name in file_names:
        gen_file(name)