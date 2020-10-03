banner_params = ['path', 'name', 'hash', 'type', 'begins', 'ends']


def get_banners_list(data):
    params = []
    for i in range(len(data)):
        for j in banner_params:
            params.append(data[i][j])
    return params
