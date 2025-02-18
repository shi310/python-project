from enum import Enum, auto

class BuildType(Enum):
    FLUTTER_ALL = auto()
    FLUTTER_ANDROID = auto()
    FLUTTER_IOS = auto()

    SHOREBIRD_ALL = auto()
    SHOREBIRD_ANDROID = auto()
    SHOREBIRD_IOS = auto()

    PATCH_ALL = auto()
    PATCH_ANDROID = auto()
    PATCH_IOS = auto()
