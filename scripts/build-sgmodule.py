import os
import re

temp_path = "template-sg"


def get_from_file(path):
    file = open(path, 'r', encoding='utf-8')
    content = file.read()
    file.close()
    return content

values = {
    'netease': get_from_file(os.getcwd() + '/temp/netease.txt'),
    'ad': get_from_file(os.getcwd() + '/temp/ad.txt')
}

def gen_file(name):
    template_file = open(os.path.join(temp_path, name),mode='r', encoding='utf-8')
    template = template_file.read()
    output_file = open(os.path.join("sgmodule", name), mode='w', encoding='utf-8')
    marks = re.findall(r'{{(.+)}}', template)
    for mark in marks:
        template = template.replace('{{' + mark + '}}', values[mark])
    output_file.write(template)
    template_file.close()
    output_file.close()

if __name__ == '__main__':
    file_names = os.listdir(temp_path)
    for name in file_names:
        gen_file(name)