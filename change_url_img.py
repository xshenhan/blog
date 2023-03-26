# This program will walk through a folder tree recusively and search for all md and html files. And then it will change the url of the images in the md and html files.
# Path: change_url_img.py


import os
import argparse

def get_dir_reclusively(root, basedir):
    contents = os.listdir(os.path.join(basedir, root))
    res = []
    for dir in contents:
        if os.path.isdir(os.path.join(root, dir)) and dir[0] != ".":
            res.extend(get_dir_reclusively(os.path.join(root, dir), basedir))
        elif dir[-3:] == ".md" or dir[-5:] == ".html":
            res.append(os.path.join(root, dir))
    return res


# change the url of the images in the md and html files reading and writing by lines.
def change_url_in_a_file(filepath, origin_url, target_url):
    with open(filepath, "rt", encoding="utf-8") as file:
        lines = file.readlines()
    with open(filepath, "wt", encoding="utf-8") as file:
        print("do one")
        for line in lines:
            file.write(line.replace(origin_url, target_url))


def change_url_img(methods, domain, file_list, basedir):
    for filepath in file_list:
        change_url_in_a_file(
            os.path.join(basedir, filepath),
            "https://raw.githubusercontent.com/hanleo001/img/",
            f"{methods}://{domain}",
        )

# determine whether the file is a md or html file.
def is_md_or_html(filepath):
    try:
        if len(filepath)<3:
            return False
        if filepath[-3:] == ".md" :
            return True
        if len(filepath)<5:
            return False
        if filepath[-5:] == ".html":
            return True
        return False
    except:
        print("error")
        return False


# # main function
# def change_url_img(methods, domain, rec_list, basedir):
#     for num1, dir1 in enumerate(rec_list):
#         if num1 == 0:
#             continue
#         for num2, dir2 in enumerate(dir1):
#             if num2 == 0:
#                 continue
#             for num3, dir3 in enumerate(dir2):
#                 if num3 == 0:
#                     continue
#                 for num4, dir4 in enumerate(dir3):
#                     if num4 == 0:
#                         continue
#                     else:
#                         if is_md_or_html(dir4):
#                             change_url_in_a_file(
#                                 os.path.join(basedir, dir4),
#                                 "https://hanleo001.github.io",
#                                 f"{methods}://{domain}",
#                             )


if __name__ == "__main__":
    # parser = argparse.ArgumentParser(description="Change URL of images in md and html files.")
    # parser.add_argument("root_folder", help="Root folder to search for md and html files")
    # parser.add_argument("basedir", help="Base directory of the root folder")
    # parser.add_argument("methods", help="URL methods (e.g., 'https')")
    # parser.add_argument("domain", help="Target domain to replace the origin_url")
    # args = parser.parse_args()

    # file_list = get_dir_reclusively(args.root_folder, args.basedir)
    # change_url_img(args.methods, args.domain, file_list, args.basedir)

    file_list = get_dir_reclusively("first", r"E:\www\site\github\hanleo001.github.io")
    print(file_list)
    change_url_img("https", "raw.githubusercontent.com/hanleo001/img/main/", file_list, r"E:\www\site\github\hanleo001.github.io")
