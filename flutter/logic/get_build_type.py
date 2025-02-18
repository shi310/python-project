import inquirer
from flutter.models.build_type import BuildType
from utils import consol

def run() -> BuildType:
    # 定义打包类型的选项和对应的 BuildType 枚举值
    build_type_mapping = {
        'Flutter 安卓和IOS': BuildType.FLUTTER_ALL,
        'Flutter 安卓': BuildType.FLUTTER_ANDROID,
        'Flutter IOS': BuildType.FLUTTER_IOS,

        'Shorebird 安卓和IOS': BuildType.SHOREBIRD_ALL,
        'Shorebird 安卓': BuildType.SHOREBIRD_ANDROID,
        'Shorebird IOS': BuildType.SHOREBIRD_IOS,

        'PATCH 安卓和IOS': BuildType.PATCH_ALL,
        'PATCH 安卓': BuildType.PATCH_ANDROID,
        'PATCH IOS': BuildType.PATCH_IOS,
    }

    # 用户提示信息中的名称
    build_type_display_names = list(build_type_mapping.keys())
    
    # 提问用户选择打包类型
    questions = [
        inquirer.List(
            'build_type',
            message="请选择打包类型",
            choices=build_type_display_names,
            default=build_type_display_names[0]
        )
    ]

    answers = inquirer.prompt(questions)
    selected_build_type_name = answers['build_type']
    
    # 获取对应的 BuildType 枚举
    selected_build_type = build_type_mapping.get(selected_build_type_name, BuildType.FLUTTER)
    
    # 打印用户选择的类型
    consol.log(f"你选择的打包环境是: {selected_build_type_name}，对应的类型是: {selected_build_type}")
    print()
    
    return selected_build_type