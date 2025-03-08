'use strict';
const MANIFEST = 'flutter-app-manifest';
const TEMP = 'flutter-temp-cache';
const CACHE_NAME = 'flutter-app-cache';

const RESOURCES = {"flutter_bootstrap.js": "5302ec7bd90d61790b0762cfc8df20ee",
"version.json": "8af9dfd0e1bbb0b9986e90cb5ed36aea",
"index.html": "7bfe9e8e5f0f6ac7b6e29b3bc47b9780",
"/": "7bfe9e8e5f0f6ac7b6e29b3bc47b9780",
"main.dart.js": "288733fad5380df23f96afb6be0dc900",
"flutter.js": "4b2350e14c6650ba82871f60906437ea",
"favicon.png": "da45cebea79b0f52ab086b77790db8cf",
"icons/Icon-192.png": "808fa5a9a608ec2403cd4e82e6e96e22",
"icons/Icon-maskable-192.png": "808fa5a9a608ec2403cd4e82e6e96e22",
"icons/Icon-maskable-512.png": "f9ef5deb778ff308ebfd82901a0ce3eb",
"icons/Icon-512.png": "f9ef5deb778ff308ebfd82901a0ce3eb",
"manifest.json": "c9a3df536c567a9969f7151d762fcee6",
"assets/shorebird.yaml": "59261ba8ae30da88bbceb17d7e565230",
"assets/AssetManifest.json": "e16321e36be1655157b7920fac934b47",
"assets/NOTICES": "14784c424a7161017ec9dfd77b8bb828",
"assets/FontManifest.json": "dae25ba92f85e0882064813f81f93d8a",
"assets/AssetManifest.bin.json": "2c40ea739539473d3fa9fa1b2425e710",
"assets/packages/cupertino_icons/assets/CupertinoIcons.ttf": "e986ebe42ef785b27164c36a9abc7818",
"assets/packages/spine_flutter/lib/assets/libspine_flutter.wasm": "ef93456d438f1de6874ef9c4622a2ef9",
"assets/packages/spine_flutter/lib/assets/libspine_flutter.js": "36495360fc0dc6835f6a6c78ebafc345",
"assets/packages/spine_flutter/src/spine-cpp-lite/spine-cpp-lite.h": "e6d1ddb9ec01f1c4adff19e5957f1e3a",
"assets/packages/spine_flutter/src/spine-cpp-lite/spine-cpp-lite.cpp": "55d7aac2b3f838d3a6ccff6d0cef2538",
"assets/shaders/ink_sparkle.frag": "ecc85a2e95f5e9f53123dcaf8cb9b6ce",
"assets/AssetManifest.bin": "94710704108b352c78a521f3e302ee65",
"assets/fonts/MaterialIcons-Regular.otf": "40a89a54008fb059c27e3f4916dd3a7d",
"assets/assets/svg/footer_right_icon.svg": "661caa190a09515ed3a514d2160fab90",
"assets/assets/svg/login_facebook.svg": "91fb92f3afc27044865b524d592cd794",
"assets/assets/svg/header_background_2.svg": "20f7b5e13cadba99ca5e17a9a149e97f",
"assets/assets/svg/header_background_1.svg": "e1d493628d03d4640ce9333a79c016bd",
"assets/assets/svg/login_phone.svg": "b3a2ca19f568ae36bdd36d811980d6b0",
"assets/assets/svg/header_avatar_background.svg": "95ddcb7f1eb91e32b62b65925694e0c0",
"assets/assets/svg/header_add_1.svg": "e6b3f220d185defcfd5c1a7820642ce5",
"assets/assets/svg/header_card.svg": "b66ae89e359af8287da28a55578d9759",
"assets/assets/svg/footer_left_icon.svg": "b11ba3ed56e07a0f764457a7c6a7014f",
"assets/assets/svg/login_guest.svg": "e2493c88eaa2474dbc863688ed73f4ab",
"assets/assets/svg/header_add_2.svg": "f9dbf4d4a8403d93aeaeb36f7a4de5eb",
"assets/assets/svg/header_stone.svg": "736fa29aa0a6ff4a79b5a8be66d1f13c",
"assets/assets/svg/login_google.svg": "861f8b01e44fcab9504a7993305b8f28",
"assets/assets/svg/login_email.svg": "5915de28fba714fbfb56ead9a97dffc9",
"assets/assets/audios/exchange_successful.mp3": "092c15baa5bc58bff4d47a3f43fdad40",
"assets/assets/audios/scan.mp3": "da1e81c121c21ae89b01af82c21b8d43",
"assets/assets/audios/setting.mp3": "563b4f753843dcec1d8cd447c816abda",
"assets/assets/audios/dialog.mp3": "93325ac713f8f458d494387f82f6d863",
"assets/assets/audios/achievement.mp3": "9569c8fea0278219e3633c946873c667",
"assets/assets/audios/click.mp3": "4d55f704b9897973feb18e392b82098d",
"assets/assets/audios/exchange_failed.mp3": "4106e2612ece08dc599ca7b7549e21eb",
"assets/assets/audios/coin_drop.mp3": "521bf8b7e9db28f4bbfcf614b0edae64",
"assets/assets/audios/news.mp3": "073da492432373f36c3b95cf056673db",
"assets/assets/spine/baoxiang_skel.skel": "ef4b8d9a367ad243c80c732ca8902397",
"assets/assets/spine/you.png": "f602b439ee19e95ca0cd6eedcce059c7",
"assets/assets/spine/baoxiang_atlas.atlas": "9812275aa4e6291afb2af45a0e173b21",
"assets/assets/spine/eff_caidai_atlas.atlas": "a9c7cac12b83b9a7e3a87698637b49f6",
"assets/assets/spine/zuo.png": "3b43e0906d46f4dce098d477f23ed804",
"assets/assets/spine/you_atlas.atlas": "fa1621750b65f43f7c8336b4e6e4dc95",
"assets/assets/spine/you_skel.skel": "b4ad9b1d32d9bbf0f0dfebc4541d3729",
"assets/assets/spine/zuo_atlas.atlas": "07fef7b9ea2c711f3e68c07ba7d64a22",
"assets/assets/spine/eff_caidai.png": "cbe7711a952a98e549d13a17b8bd41aa",
"assets/assets/spine/eff_caidai_skel.skel": "931a5223451e980286ecc8355ce6a400",
"assets/assets/spine/baoxiang.png": "6d4e617684f5707f9eb3bba7bfe0732c",
"assets/assets/spine/zuo_skel.skel": "b884736827830c8218ce56607391e230",
"assets/assets/images/setting_button_audio.png": "d4a1f434401ec9ff19a5363dfb698dcd",
"assets/assets/images/invite_url_background_middle.png": "b5672af298c8f5c290e72777449b20b3",
"assets/assets/images/sign_in_win_14.png": "83b81e1a6da4ed516ace6e7c0910cc5c",
"assets/assets/images/store_buy_50.png": "57e103598703e87772238702ab5dcddc",
"assets/assets/images/game_1_title.png": "3ee887fa2d015e2957dd2da0248bc68b",
"assets/assets/images/header_background_1.png": "adc10ca8465cafd8d7406f1555ce4b51",
"assets/assets/images/invite_button_1.png": "ba4e7d95a26418bcab04d8a65f7fe0fc",
"assets/assets/images/login_background.png": "0db8f88832785ffb6e093ec3c709a481",
"assets/assets/images/store_star.png": "c10802592ac68499b30593a81a1e6c20",
"assets/assets/images/game_right.png": "05069f3b19ac55d4dc3959121d7621b6",
"assets/assets/images/me_button_bottom_right.png": "2d1de1172a33cf80d0e1de37dd00f3ab",
"assets/assets/images/invite_button_0.png": "6b83e134f1bcf6823249acc63a7ca836",
"assets/assets/images/header_background_2.png": "143266b50ea59f8f50a419e0b785e222",
"assets/assets/images/store_skin_18.png": "0eb8941c847916437bf34fcafa76bae6",
"assets/assets/images/header_avatar.png": "618d340a1d51ac5ebf0fbf2a5af305c9",
"assets/assets/images/sign_in_never_win_icon.png": "b63b2263b1809868f3545a5aa49760b4",
"assets/assets/images/sign_in_title.png": "9672accc02d8c0b97a6cbf8313ee025b",
"assets/assets/images/header_background.png": "44dae98b215659a1a0d44b119543e2ec",
"assets/assets/images/alert_header_top_right.png": "898be55879ceb6c311c7edf3c5762948",
"assets/assets/images/app_icon.png": "808fa5a9a608ec2403cd4e82e6e96e22",
"assets/assets/images/alert_header_center.png": "4a7d3fbcc4a1ce9997cdd5fbc4762ae8",
"assets/assets/images/alert_body_background.png": "c78b228f3cd106eda267aec5293d3aaa",
"assets/assets/images/lang_en.png": "8a28bd88ea2d5fa252bd7c50799f2524",
"assets/assets/images/game_4_icon.png": "f252a2f2b39809eb53edea759d4af56a",
"assets/assets/images/game_5_icon.png": "9494ff585b0ebb4da66f9ffe68bb401e",
"assets/assets/images/me_button_top_right.png": "1dac294aac5309d53b33b15cd2e20139",
"assets/assets/images/invite_url_background_left.png": "10e083d3cabcf256cbbf701ab7f6e9e3",
"assets/assets/images/alert_header_top_left.png": "77e8fba8d89d051a48dc3cedf37db892",
"assets/assets/images/alert_bottom_left_1.png": "b094f47cc4f27609b84e5d3209bfda2c",
"assets/assets/images/alert_bottom_right_1.png": "439aa0070e103252ab908d3adbfd7368",
"assets/assets/images/store_skin_2.png": "abb49ec61b5bc7508e8c9ecfb76df0bb",
"assets/assets/images/setting_button_lang.png": "f85bb1d35c64eae09040b22d36b615e6",
"assets/assets/images/invite_register.png": "26f122e367486db2c07475bb09953c1f",
"assets/assets/images/turntable_win.png": "4ad71df6bf6bcff954f385405ba01e94",
"assets/assets/images/store_skin_3.png": "0fb51172ca50288e223e96c3fbcd130e",
"assets/assets/images/alert_background.png": "29f1d2523d2d7b41cddee594955eae8a",
"assets/assets/images/footer_selected.png": "48c20003366f407a310f3b83cd1a703a",
"assets/assets/images/alert_bottom_left_2.png": "17d75aee2ebfe2c04da64d0c729cf640",
"assets/assets/images/alert_bottom_right_2.png": "688132bc1c5125898c3188d1a3be94fd",
"assets/assets/images/store_skin_1.png": "9eb7279eaa0ef9cf05312a5401b27535",
"assets/assets/images/lang_checked.png": "c96426959d07130462f418a8339dfb7e",
"assets/assets/images/game_3_icon.png": "722579bea66938303d6e080da0527daa",
"assets/assets/images/game_2_icon.png": "09b1c5900dd02402bddded88b2f7029d",
"assets/assets/images/switch_on.png": "c02091b70122b5ffb193243a8aa13016",
"assets/assets/images/game_timer.png": "0cbe0238136e18116eaa22ba81e4d57f",
"assets/assets/images/game_help.png": "d6a5a2289f08244d27c22526114bb338",
"assets/assets/images/game_6_title.png": "52d0c24a21f31630f4d3a5dc912ec1e0",
"assets/assets/images/store_skin_4.png": "860a3e5196a901217dc2b0b976356b7f",
"assets/assets/images/lottery_body.png": "45db6cf62b7081f13346ed509d3f0672",
"assets/assets/images/store_buy_20.png": "d05f92b2f1e3d249f7bfc826b846ee80",
"assets/assets/images/lang_cn.png": "4785526d4e214c46e04416177f030f55",
"assets/assets/images/sign_in_already_win_icon.png": "98dcc6040dd07ac76350a47364668aaa",
"assets/assets/images/switch_off.png": "932d493cab0278de4d563a0382b1451f",
"assets/assets/images/store_skin_5.png": "3f06bc49ff2ea75d56cf620a8c4ceb7c",
"assets/assets/images/lang_vn.png": "57b1f423d7013be9f80685a348bf0d95",
"assets/assets/images/invite_header_icon.png": "adbac6e0177c8b4ba1e135a39e3b8d65",
"assets/assets/images/sign_in_miss.png": "19e8462b3b59bd1d8a3ef9f8486c355c",
"assets/assets/images/setting_button_login_out.png": "9a62aba6010f7002ad24e7930897a5b4",
"assets/assets/images/me_button_bottom_icon.png": "aee362c822591b2f5725642fcdbe9a4f",
"assets/assets/images/game_left.png": "cf00090a8204fc7dca793ca3b0b35bb3",
"assets/assets/images/store_skin_7.png": "3354d4eaf2b9d36754871008a83d8f3d",
"assets/assets/images/edit_cancel.png": "9554beb8f30c3495961cacd2e93f3895",
"assets/assets/images/lottery_turntable.png": "fd1df4e77f884b239072ca5d6f562690",
"assets/assets/images/lottery_pointer.png": "7f5c4db17077264d43515a3ee7aaa75e",
"assets/assets/images/invite_url.png": "c447827d360a5a5ddf4f7c1839b85627",
"assets/assets/images/store_skin_6.png": "7c3393aa21adcb50ec0fc4bb77527a19",
"assets/assets/images/game_6_2.png": "f881e898cb0c08a8326fd2fa004d1c2a",
"assets/assets/images/sign_in_win_1.png": "0b2fde58334b96c9771a74f4e92f9e25",
"assets/assets/images/sign_in_day.png": "3d7af6acf92b95c9523b36602597d650",
"assets/assets/images/game_3_title.png": "089e16ef2200f8fa354b3cf852a459df",
"assets/assets/images/sign_in_note.png": "d8d2aa06c282ccedb4666e2c479f1784",
"assets/assets/images/game_6_icon.png": "f19f3e8415df938fcb8f503e2c54f6b1",
"assets/assets/images/invite_recharged.png": "c493eb8396de07c05189ed5d6e183253",
"assets/assets/images/game_4_1.png": "3e33ed669953d6366f7d0bdb64b323d9",
"assets/assets/images/edit_sure.png": "ff0dd553bb57243ee9b847a74e245efc",
"assets/assets/images/footer_games.png": "30d21cf530b9d35bde4297d99b38302b",
"assets/assets/images/invite_win_icon_left.png": "c4f311599aa38b7da26df5cea3df0887",
"assets/assets/images/game_6_1.png": "6b2ff2097e713624802ff356847d772b",
"assets/assets/images/store_skin_8.png": "93d00fda87106778a4d0b986826f08cb",
"assets/assets/images/store_buy_10.png": "5bbc5d4b36bc6f78c491e27a29f38819",
"assets/assets/images/alert_failed.png": "aff55e184dbaeeb92c961cc994d6aeb3",
"assets/assets/images/invite_url_background_right.png": "1cf5ed824cf35807eaa0ccdbd524ec46",
"assets/assets/images/lottery_background.png": "7e95ec39c9c8722ee69ce585720f2b59",
"assets/assets/images/store_skin_9.png": "c09b3b1d5b0454d4ea88490a15b7398d",
"assets/assets/images/game_4_2.png": "2a4f91dde42eb0e2dd62b2468a41d793",
"assets/assets/images/logo.png": "1f09740d71f01877b1aaf022a0d5c3b6",
"assets/assets/images/box_background.png": "5d1b9e41e9af336b199bb482fd27494e",
"assets/assets/images/edit_user_info.png": "d12fcbadb6fd05918eaca1ce0a7b6884",
"assets/assets/images/invite_already_background.png": "617db3a8411d8f13c867661d4144b34c",
"assets/assets/images/store_banner_1.png": "761363a9cd8c6b4b3eed1f620e37c4d3",
"assets/assets/images/sign_in_win_7.png": "a7f376b2c7850ef966fdc3c987849074",
"assets/assets/images/game_banner_2.png": "389f4f20e9c55e17a8f47a9e377f9f01",
"assets/assets/images/sign_in_win_day.png": "1f78ed728e6791d3589f286c4b8d286d",
"assets/assets/images/game_2_1.png": "10529a71dab85c3603763e57f13737b1",
"assets/assets/images/game_banner_3.png": "e20b60fe16b32c5c03b03ba02bd56c89",
"assets/assets/images/setting_button_version.png": "938c563e80877638c27ff037b21f2186",
"assets/assets/images/footer_mine.png": "9bbfd82f91fef382a932663bcf287c53",
"assets/assets/images/game_5_title.png": "6e52d475ed3fe6df04bcc9523aa3f795",
"assets/assets/images/invite_already_count.png": "3dde2cb16f3511737dc8aa2d8a2836b4",
"assets/assets/images/game_banner_1.png": "3e2adddaac8ea0c7407dfc30e481a741",
"assets/assets/images/lottery_header_button_1.png": "437d8c26856bb205c70b64bf7bb9e3e5",
"assets/assets/images/lottery_header_button_0.png": "643451c6eaa054aed62b4966f76debaf",
"assets/assets/images/game_2_2.png": "ed72b3b2bdaf81d794db258e288e2962",
"assets/assets/images/store_item_background.png": "41360c0f992bdd2557e54802c5f4fe0b",
"assets/assets/images/invite_url_copy.png": "3467c04833b0b08d6e5818597615f4b3",
"assets/assets/images/store_skin_13.png": "567f4664f4510a1fc6fe0421739d068a",
"assets/assets/images/invite_win_icon_right.png": "d3523ae8d3f39b7b9bf39633ba2f6ce8",
"assets/assets/images/game_2_title.png": "a3e0d77a57a0d7074f1da5f0add62453",
"assets/assets/images/store_buy_100.png": "82c40987471447f18012344f23febfbb",
"assets/assets/images/invite_win_icon_middle.png": "ca32c8302d575292c563be0bbc0e4ca8",
"assets/assets/images/sign_in_win_21.png": "b6487335075bc68535292da286dd2f68",
"assets/assets/images/game_5_2.png": "5d81bdfc48980e797d683a0a96de7521",
"assets/assets/images/alert_header_left.png": "06ff23aaf8332fd88fc91fc7bdaf2d62",
"assets/assets/images/store_skin_12.png": "9ec206cc67e3a06984a2005dcad671c7",
"assets/assets/images/store_skin_10.png": "d836205a8b1f8e757e35007f6f3a990b",
"assets/assets/images/store_title_icon.png": "6f1e73e0fd1d7ab3fbb6aa488f99b7fb",
"assets/assets/images/game_5_1.png": "d2a5a7cda001b6b75ee6adf5c92f1c8d",
"assets/assets/images/game_background.png": "855c2b4ba945fa4a32aabfa5eb6dcc3e",
"assets/assets/images/store_skin_11.png": "687ccc6c0128dfc444c443b2332d5595",
"assets/assets/images/store_skin_15.png": "df29a38099b02cd1417c9d630299e533",
"assets/assets/images/store_skin_level_1.png": "d8cca6c83f1df10c5c02e59cd6cd32fc",
"assets/assets/images/game_1_1.png": "9a0e2801f0579692e38cb6ddc6c484b5",
"assets/assets/images/footer_store.png": "19729134b6763964ef152eda701984b3",
"assets/assets/images/alert_header_right.png": "8157c001ae3c3a4cd5643eac19b821bd",
"assets/assets/images/game_4_title.png": "4d20b2ce3a7ba35432da6e805f2830e5",
"assets/assets/images/game_1_icon.png": "f151f6d120ada772fd96fe49bcb89ff0",
"assets/assets/images/lottery_button_2.png": "1ee1c13661c95ea3641895595a468101",
"assets/assets/images/game_3_2.png": "973b81d45fac79ab6429e37875610713",
"assets/assets/images/back.png": "a8a707f7b4b2194aa89ca0e3d3ec818e",
"assets/assets/images/store_skin_14.png": "7a1c11521469f30bd11a83789796810c",
"assets/assets/images/me_button_bottom_left.png": "c63a5dea1a1581aadc89e2c23528301f",
"assets/assets/images/store_skin_16.png": "4945428d2baae9729f6d4e12ba0a3a39",
"assets/assets/images/me_button_top_left.png": "9ee98a3e5b4705278d3a76029ace966c",
"assets/assets/images/store_buy_1000.png": "300329ae72dc3ae4deaa5721d4d8d831",
"assets/assets/images/store_skin_level_2.png": "6e7d6dc2a6c8febd8bcbfb5555a64a1e",
"assets/assets/images/lottery_button_0.png": "2f4ea9359f1dd782b8a33c9d991f07ec",
"assets/assets/images/game_1_2.png": "a189349eab734c70c5c5371ad05b22c8",
"assets/assets/images/invite_url_share.png": "420bb8f699c9202e4421480de664d8ba",
"assets/assets/images/alert_bottom_center.png": "3e5712afd306e9f90a160ca43a2687f2",
"assets/assets/images/sign_in_win_30.png": "7ba69ec2f94589782759bdea0c5c2e40",
"assets/assets/images/bag.png": "061acf5d94ec79bc5abcb113a12a234e",
"assets/assets/images/store_buy_500.png": "83ae6a4a7b78868e9d5ac9f05e6a6ab4",
"assets/assets/images/store_banner_background.png": "5cafadae5ed81285ce0de5b164ab3b1a",
"assets/assets/images/lottery_button_1.png": "3198e60cf8aff72aa8a0fad0a98ad411",
"assets/assets/images/store_skin_level_3.png": "e296348c2710ab31ee4727be47fe46e7",
"assets/assets/images/close.png": "e361c0cb27954b05bc0f7251ac9d2693",
"assets/assets/images/game_team.png": "849e3abfa41dacd81b2d8ecf09912a6f",
"assets/assets/images/game_3_1.png": "a232308bf201b5bfd3c24bdc1228eb88",
"assets/assets/images/store_skin_17.png": "5a1ec9e0e275058dc2b47140b9586dbc",
"assets/assets/lottie/loading.zip": "f05278728c9aef9b67b28fbcfe941a40",
"assets/assets/fonts/Sans.otf": "f4d01a1a737b77bc6709c81300eb09a4",
"canvaskit/skwasm.js": "ac0f73826b925320a1e9b0d3fd7da61c",
"canvaskit/skwasm.js.symbols": "96263e00e3c9bd9cd878ead867c04f3c",
"canvaskit/canvaskit.js.symbols": "efc2cd87d1ff6c586b7d4c7083063a40",
"canvaskit/skwasm.wasm": "828c26a0b1cc8eb1adacbdd0c5e8bcfa",
"canvaskit/chromium/canvaskit.js.symbols": "e115ddcfad5f5b98a90e389433606502",
"canvaskit/chromium/canvaskit.js": "b7ba6d908089f706772b2007c37e6da4",
"canvaskit/chromium/canvaskit.wasm": "ea5ab288728f7200f398f60089048b48",
"canvaskit/canvaskit.js": "26eef3024dbc64886b7f48e1b6fb05cf",
"canvaskit/canvaskit.wasm": "e7602c687313cfac5f495c5eac2fb324",
"canvaskit/skwasm.worker.js": "89990e8c92bcb123999aa81f7e203b1c"};
// The application shell files that are downloaded before a service worker can
// start.
const CORE = ["main.dart.js",
"index.html",
"flutter_bootstrap.js",
"assets/AssetManifest.bin.json",
"assets/FontManifest.json"];

// During install, the TEMP cache is populated with the application shell files.
self.addEventListener("install", (event) => {
  self.skipWaiting();
  return event.waitUntil(
    caches.open(TEMP).then((cache) => {
      return cache.addAll(
        CORE.map((value) => new Request(value, {'cache': 'reload'})));
    })
  );
});
// During activate, the cache is populated with the temp files downloaded in
// install. If this service worker is upgrading from one with a saved
// MANIFEST, then use this to retain unchanged resource files.
self.addEventListener("activate", function(event) {
  return event.waitUntil(async function() {
    try {
      var contentCache = await caches.open(CACHE_NAME);
      var tempCache = await caches.open(TEMP);
      var manifestCache = await caches.open(MANIFEST);
      var manifest = await manifestCache.match('manifest');
      // When there is no prior manifest, clear the entire cache.
      if (!manifest) {
        await caches.delete(CACHE_NAME);
        contentCache = await caches.open(CACHE_NAME);
        for (var request of await tempCache.keys()) {
          var response = await tempCache.match(request);
          await contentCache.put(request, response);
        }
        await caches.delete(TEMP);
        // Save the manifest to make future upgrades efficient.
        await manifestCache.put('manifest', new Response(JSON.stringify(RESOURCES)));
        // Claim client to enable caching on first launch
        self.clients.claim();
        return;
      }
      var oldManifest = await manifest.json();
      var origin = self.location.origin;
      for (var request of await contentCache.keys()) {
        var key = request.url.substring(origin.length + 1);
        if (key == "") {
          key = "/";
        }
        // If a resource from the old manifest is not in the new cache, or if
        // the MD5 sum has changed, delete it. Otherwise the resource is left
        // in the cache and can be reused by the new service worker.
        if (!RESOURCES[key] || RESOURCES[key] != oldManifest[key]) {
          await contentCache.delete(request);
        }
      }
      // Populate the cache with the app shell TEMP files, potentially overwriting
      // cache files preserved above.
      for (var request of await tempCache.keys()) {
        var response = await tempCache.match(request);
        await contentCache.put(request, response);
      }
      await caches.delete(TEMP);
      // Save the manifest to make future upgrades efficient.
      await manifestCache.put('manifest', new Response(JSON.stringify(RESOURCES)));
      // Claim client to enable caching on first launch
      self.clients.claim();
      return;
    } catch (err) {
      // On an unhandled exception the state of the cache cannot be guaranteed.
      console.error('Failed to upgrade service worker: ' + err);
      await caches.delete(CACHE_NAME);
      await caches.delete(TEMP);
      await caches.delete(MANIFEST);
    }
  }());
});
// The fetch handler redirects requests for RESOURCE files to the service
// worker cache.
self.addEventListener("fetch", (event) => {
  if (event.request.method !== 'GET') {
    return;
  }
  var origin = self.location.origin;
  var key = event.request.url.substring(origin.length + 1);
  // Redirect URLs to the index.html
  if (key.indexOf('?v=') != -1) {
    key = key.split('?v=')[0];
  }
  if (event.request.url == origin || event.request.url.startsWith(origin + '/#') || key == '') {
    key = '/';
  }
  // If the URL is not the RESOURCE list then return to signal that the
  // browser should take over.
  if (!RESOURCES[key]) {
    return;
  }
  // If the URL is the index.html, perform an online-first request.
  if (key == '/') {
    return onlineFirst(event);
  }
  event.respondWith(caches.open(CACHE_NAME)
    .then((cache) =>  {
      return cache.match(event.request).then((response) => {
        // Either respond with the cached resource, or perform a fetch and
        // lazily populate the cache only if the resource was successfully fetched.
        return response || fetch(event.request).then((response) => {
          if (response && Boolean(response.ok)) {
            cache.put(event.request, response.clone());
          }
          return response;
        });
      })
    })
  );
});
self.addEventListener('message', (event) => {
  // SkipWaiting can be used to immediately activate a waiting service worker.
  // This will also require a page refresh triggered by the main worker.
  if (event.data === 'skipWaiting') {
    self.skipWaiting();
    return;
  }
  if (event.data === 'downloadOffline') {
    downloadOffline();
    return;
  }
});
// Download offline will check the RESOURCES for all files not in the cache
// and populate them.
async function downloadOffline() {
  var resources = [];
  var contentCache = await caches.open(CACHE_NAME);
  var currentContent = {};
  for (var request of await contentCache.keys()) {
    var key = request.url.substring(origin.length + 1);
    if (key == "") {
      key = "/";
    }
    currentContent[key] = true;
  }
  for (var resourceKey of Object.keys(RESOURCES)) {
    if (!currentContent[resourceKey]) {
      resources.push(resourceKey);
    }
  }
  return contentCache.addAll(resources);
}
// Attempt to download the resource online before falling back to
// the offline cache.
function onlineFirst(event) {
  return event.respondWith(
    fetch(event.request).then((response) => {
      return caches.open(CACHE_NAME).then((cache) => {
        cache.put(event.request, response.clone());
        return response;
      });
    }).catch((error) => {
      return caches.open(CACHE_NAME).then((cache) => {
        return cache.match(event.request).then((response) => {
          if (response != null) {
            return response;
          }
          throw error;
        });
      });
    })
  );
}
