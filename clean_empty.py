from pprint import pprint


def clean_empty(d: object) -> object:
    if not isinstance(d, (dict, list)):
        return d
    if isinstance(d, list):
        return [v for v in (clean_empty(v) for v in d) if v]
    return {k: v for k, v in ((k, clean_empty(v)) for k, v in d.items()) if v}


if __name__ == '__main__':
    data = [{
        'empty': [{}, []],
        'not_empty': [{
            'value': '1'
        }, []],
    }]
    pprint(clean_empty(data))
