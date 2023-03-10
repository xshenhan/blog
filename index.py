import os

pathlst=[]
filelst=[]

# print(os.listdir())



def get_dir_reclusively(root,basedir):
    contents = os.listdir(os.path.join(basedir, root))
    status = False
    res = []
    res.append(str(root).split("\\")[-1])
    for dir in contents:
        if os.path.isdir(os.path.join(root,dir)) and dir[0]!=".":
            res.append(get_dir_reclusively(os.path.join(root, dir), basedir))
        if dir[-4:]=="html":
            res.append(os.path.join(root, dir))
    return res



def write_to_md(methods, domain, rec_list, basedir):
    with open(os.path.join(basedir, "index.md"), "wt", encoding="utf-8") as index:
        index.write("# 目录\n")
        for num1,dir1 in enumerate(rec_list):
            if num1 == 0:
                index.write("## "+dir1+"\n")
                continue
            for num2,dir2 in enumerate(dir1):
                if num2 == 0:
                    index.write("### "+dir2+"\n")
                    continue
                for num3,dir3 in enumerate(dir2):
                    if num3 ==0 :
                        index.write("#### "+dir3+"\n")
                        continue
                    for num4, dir4 in enumerate(dir3):
                        if num4==0:
                            index.write(f"[{dir4}]")
                        else:
                            index.write(f"({dir4})\n")







print(get_dir_reclusively("first", r"E:\www\site\github\hanleo001.github.io"))
if __name__ == "__main__":
    write_to_md(
        "https",
        "blog.leoh.top",
        get_dir_reclusively("first", r"E:\www\site\github\hanleo001.github.io"),
        r"E:\www\site\github\hanleo001.github.io"
    )
