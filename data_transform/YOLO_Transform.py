import dota_utils as util
import os
import numpy as np

## trans dota format to format YOLO(darknet) required
def dota2darknet(srcpath, dstpath, extractclassname):
    """
    :param srcpath:  the path of txt in dota format
    :param dstpath: the path of txt in YOLO format
    :param extractclassname: the category you selected
    :return:
    """
    filelist = util.GetFileFromThisRootDir(srcpath)
    for fullname in filelist:
        objects = util.parse_dota_poly(fullname)
        name = os.path.splitext(os.path.basename(fullname))[0]
        with open(os.path.join(dstpath, name + '.txt'), 'w') as f_out:
            for obj in objects:
                poly = obj['poly']
                bbox = np.array(util.dots4ToRecC(poly)) / 1024
                if (sum(bbox <= 0) + sum(bbox >= 1)) >= 1:
                    continue
                if (obj['name'] in extractclassname):
                    id = extractclassname.index(obj['name'])
                else:
                    continue
                outline = str(id) + ' ' + ' '.join(list(map(str, bbox)))
                f_out.write(outline + '\n')

if __name__ == '__main__':
    ## an example
    dota2darknet('path1',
                 'path2',
                 util.wordname_15)
