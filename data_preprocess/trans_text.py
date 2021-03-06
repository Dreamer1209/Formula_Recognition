import os

formula_path='../data/full/formulas/formulas.norm.txt'
images_path='../data/full/images/'

def getBlankLineIds(filename):
  errlist = []
  with open(filename) as f:
    lines = f.readlines()
    linenumber = 0
    for line in lines:
      if len(line) <= 1:
        errlist.append(linenumber)
      linenumber += 1
  return errlist

def getExistImageNames(images_dir):
  return os.listdir(images_dir)

def trans_matching(fin_name, fout_name):
  errlist = getBlankLineIds(formula_path)
  imglist = getExistImageNames(images_path)
  with open(fin_name) as fin:
    with open(fout_name, 'w') as fout:
      for line in fin:
        tokens = line.strip().split(' ')
        formula_id = int(tokens[0])-1
        img_id = str(int(tokens[1]) - 1)+'.png'
        if formula_id+1 in errlist:
          continue
        if img_id not in imglist:
          continue
        newline = ' '.join([img_id, str(formula_id)])+'\n'
        fout.write(newline)


trans_matching('../data/full/formulas/train.lst', '../data/full/matching/train.matching.txt')
trans_matching('../data/full/formulas/val.lst', '../data/full/matching/val.matching.txt')
trans_matching('../data/full/formulas/test.lst', '../data/full/matching/test.matching.txt')