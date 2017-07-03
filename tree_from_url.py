# -*- coding: utf-8 -*-
import json
import urllib


try:
    from clean_empty import clean_empty
except ImportError:
    clean_empty = None


def tree_from_url(urls):
    tree = {}
    paths = []

    if len(urls) > 0:
        for url in urls:
            split = url.split('/')
            paths.append(split[2:-1])

    if len(paths) > 0:
        for path in paths:
            branch = tree.setdefault(path[0], [{}, []])
            for step in path[1:-1]:
                # TODO Formatar
                #step_formated = urllib.parse.unquote(urllib.parse.unquote(step))
                step_formated = step
                branch = branch[0].setdefault(step_formated, [{}, []])
            branch[1].append(path[-1])

    if clean_empty:
        tree = clean_empty(tree)
    return json.dumps(tree)


if __name__ == '__main__':
    url_list = [
        'http://www.example.com.br/something/nivel1/1/',
        'http://www.example.com.br/something/nivel1/2/',
        'http://www.example.com.br/something/nivel1/3/',
        'http://www.example.com.br/something/nivel2/1/',
        'http://www.example.com.br/something/nivel3/português I/',
        'http://www.example.com.br/something/nivel3/português II/',
    ]

    print('List of urls:')
    for url in url_list:
        print('url: {0}'.format(url))

    res = tree_from_url(url_list)
    print('Result tree format:')
    print('{0}'.format(json.dumps(json.loads(res), indent=4, sort_keys=True)))