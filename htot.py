import re
import sys
import os

"""
  正規表現定義
"""
RE_PTN_DATE = '/// nitiji'
RE_PTN_P1   = 'p1'
RE_PTN_P2   = 'p2'
RE_PTN_KIFU = 'x['
RE_PTN2     = "^x([^;]*;){1}"
RE_PTN3     = '"(.*?)"'

def main(target_file):
    try:
        out_file = os.path.basename(target_file)+'.conv'
        # WANNIG: 対局日時は抽出失敗のためコメントアウト
        # write_date(out_file, target_file)
        write_player1(out_file, target_file)
        write_player2(out_file, target_file)
        write_kifu(out_file, target_file)
    except Exception as e:
        print("例外args:", e.args)
    else:
        print("Success!! file:" + target_file)

def get_target_lines(target_file, ptn):
    with open(target_file) as f:
        lines = f.readlines()
        lines_strip = [line.strip() for line in lines]
        target_lines = [line for line in lines_strip if line.startswith(ptn)]
        return target_lines

def write_file(out_file, target_lines, is_kifu):
    for line in target_lines:
        if (is_kifu):
            ret1 = re.match(RE_PTN2, line)
            ret2 = re.findall(RE_PTN3, ret1.group(0).replace("\'", '\"'))
            write_context(out_file, ret2[0])
        else:
            ret = re.findall(RE_PTN3, str(line).replace("\'", '\"'))
            write_context(out_file, ret[0])

def write_context(out_file, context):
    with open(out_file, 'a') as f:
        f.write(context + "\n")

def write_date(out_file, target_file):
    target_lines = get_target_lines(target_file, RE_PTN_DATE)
    write_file(out_file, target_lines, False)

def write_player1(out_file, target_file):
    target_lines = get_target_lines(target_file, RE_PTN_P1)
    write_file(out_file, target_lines, False)

def write_player2(out_file, target_file):
    target_lines = get_target_lines(target_file, RE_PTN_P2)
    write_file(out_file, target_lines, False)

def write_kifu(out_file, target_file):
    target_lines = get_target_lines(target_file, RE_PTN_KIFU)
    write_file(out_file, target_lines, True)

if __name__ == "__main__":
    args = sys.argv
    main(args[1])

