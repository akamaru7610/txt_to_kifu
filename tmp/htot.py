import re
import sys
import os

"""
  正規表現定義
"""
RE_PTH_SENTE = 'p1'
RE_PTH_GOTE  = 'p2'
RE_PTN1      = 'x['
RE_PTN2      = "^x([^;]*;){1}"
RE_PTN3      = '"(.*?)"'

def main(target_file):
    try:
        out_file = os.path.basename(target_file)+'.conv'

        target_lines = get_target_lines(target_file)
        for line in target_lines:
            ret1 = re.match(RE_PTN2, line)
            ret2 = re.findall(RE_PTN3, ret1.group(0).replace("\'", '\"'))
            write_file(out_file, ret2[0])

    except Exception as e:
        print("例外args:", e.args)
    else:
        print("Success!! file:" + target_file)

def get_target_lines(target_file):
    with open(target_file) as f:
        lines = f.readlines()
        lines_strip = [line.strip() for line in lines]
        target_lines = [line for line in lines_strip if line.startswith(RE_PTN1)]
        return target_lines

def write_file(out_file, context):
    with open(out_file, 'a') as f:
        f.write(context + "\n")

if __name__ == "__main__":
    args = sys.argv
    main(args[1])

