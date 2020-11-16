import json
from os import walk, path
import re
from shutil import copyfile
DIST_DIR = "./dist"
MATERIAL_ICONS_ROOT_DIR = "../material-design-icons"
MATERIAL_ICONS_SVG_DIR = MATERIAL_ICONS_ROOT_DIR + "/src"

SIZE_VARIANT_NAME_MAP = {
    "materialiconsoutlined": "outlined",
    "materialiconsround": "round",
    "materialiconssharp": "sharp",
    "materialicons": "",
    "materialiconstwotone": "twotone",
}

SIZE_VARIANT_FLUTTER_NAME_MAP = {
    "outlined": "outlined",
    "round": "round",
    "sharp": "sharp",
    "": "",
    "twotone": "twotone"
}




def main():
    config = {}

    # Get the list of all files in directory tree at given path
    svg_paths = list()
    for (dirpath, dirnames, filenames) in walk(MATERIAL_ICONS_SVG_DIR):
        svg_paths += [path.join(dirpath, file) for file in filenames]

    for svg_path in svg_paths:
        splits = svg_path.split('/')
        icon_name = splits[-3]
        icon_variant = SIZE_VARIANT_FLUTTER_NAME_MAP[SIZE_VARIANT_NAME_MAP[splits[-2]]]
        size = re.search(r'(.*?)px\.svg', splits[-1]).group(1)
        icon_full_name = f"{icon_name}_{icon_variant}" if icon_variant != "" else icon_name
        print(icon_name, icon_variant, size)
        config[icon_full_name] = {
            "default_size": size,
            "variant": "default" if icon_variant == "" else icon_variant,
            "family": icon_name,
            "host": "material"
        }

        out = f"{DIST_DIR}/{icon_full_name}.svg"
        copyfile(svg_path, out)
    print(config)
    with open(f'{DIST_DIR}/config.json', 'w') as file:
        json.dump(config, file, indent=2)

if __name__ == '__main__':
    main()
#
# def main():
#     # file structure is like
#     # -src
#     #     - category_name
#     #       - icon_name
#     #         - 24px.svg
#
#     svg_maps = {}
#     a = [x[0] for x in walk(MATERIAL_ICONS_SVG_DIR)]
#     print(a)
#
#
#     categories = [f for f in listdir(MATERIAL_ICONS_SVG_DIR) if isdir(join(MATERIAL_ICONS_SVG_DIR, f))]
#     print(categories)
#     for category in categories:
#         icon_dirs = [c for c in listdir(category) if isdir(category, c)]
#         print(icon_dirs)
#         for icon_name_dir in icon_dirs:
#             # looping through the directory, but it will have only 24px.svg under it.
#             svgs = [f for f in listdir(
#                 icon_name_dir) if isfile(join(icon_name_dir, f))]
#
#             for svg_path in svgs:
#                 icon_name = icon_name_dir.split('/')[-1]
#                 svg_maps[icon_name] = svg_path
#
#     print(svg_maps)
#
#
# if __name__ == "__main__":
#     main()
