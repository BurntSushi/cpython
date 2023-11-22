# This file is generated by mkstringprep.py. DO NOT EDIT.
"""Library that exposes various tables found in the StringPrep RFC 3454.

There are two kinds of tables: sets, for which a member test is provided,
and mappings, for which a mapping function is provided.
"""

from unicodedata import ucd_3_2_0 as unicodedata

assert unicodedata.unidata_version == "3.2.0"


def in_table_a1(code):
    if unicodedata.category(code) != "Cn":
        return False
    c = ord(code)
    if 0xFDD0 <= c < 0xFDF0:
        return False
    return (c & 0xFFFF) not in (0xFFFE, 0xFFFF)


b1_set = set(
    [173, 847, 6150, 6155, 6156, 6157, 8203, 8204, 8205, 8288, 65279]
    + list(range(65024, 65040))
)


def in_table_b1(code):
    return ord(code) in b1_set


b3_exceptions = {
    0xB5: "\u03bc",
    0xDF: "ss",
    0x130: "i\u0307",
    0x149: "\u02bcn",
    0x17F: "s",
    0x1F0: "j\u030c",
    0x345: "\u03b9",
    0x37A: " \u03b9",
    0x390: "\u03b9\u0308\u0301",
    0x3B0: "\u03c5\u0308\u0301",
    0x3C2: "\u03c3",
    0x3D0: "\u03b2",
    0x3D1: "\u03b8",
    0x3D2: "\u03c5",
    0x3D3: "\u03cd",
    0x3D4: "\u03cb",
    0x3D5: "\u03c6",
    0x3D6: "\u03c0",
    0x3F0: "\u03ba",
    0x3F1: "\u03c1",
    0x3F2: "\u03c3",
    0x3F5: "\u03b5",
    0x587: "\u0565\u0582",
    0x1E96: "h\u0331",
    0x1E97: "t\u0308",
    0x1E98: "w\u030a",
    0x1E99: "y\u030a",
    0x1E9A: "a\u02be",
    0x1E9B: "\u1e61",
    0x1F50: "\u03c5\u0313",
    0x1F52: "\u03c5\u0313\u0300",
    0x1F54: "\u03c5\u0313\u0301",
    0x1F56: "\u03c5\u0313\u0342",
    0x1F80: "\u1f00\u03b9",
    0x1F81: "\u1f01\u03b9",
    0x1F82: "\u1f02\u03b9",
    0x1F83: "\u1f03\u03b9",
    0x1F84: "\u1f04\u03b9",
    0x1F85: "\u1f05\u03b9",
    0x1F86: "\u1f06\u03b9",
    0x1F87: "\u1f07\u03b9",
    0x1F88: "\u1f00\u03b9",
    0x1F89: "\u1f01\u03b9",
    0x1F8A: "\u1f02\u03b9",
    0x1F8B: "\u1f03\u03b9",
    0x1F8C: "\u1f04\u03b9",
    0x1F8D: "\u1f05\u03b9",
    0x1F8E: "\u1f06\u03b9",
    0x1F8F: "\u1f07\u03b9",
    0x1F90: "\u1f20\u03b9",
    0x1F91: "\u1f21\u03b9",
    0x1F92: "\u1f22\u03b9",
    0x1F93: "\u1f23\u03b9",
    0x1F94: "\u1f24\u03b9",
    0x1F95: "\u1f25\u03b9",
    0x1F96: "\u1f26\u03b9",
    0x1F97: "\u1f27\u03b9",
    0x1F98: "\u1f20\u03b9",
    0x1F99: "\u1f21\u03b9",
    0x1F9A: "\u1f22\u03b9",
    0x1F9B: "\u1f23\u03b9",
    0x1F9C: "\u1f24\u03b9",
    0x1F9D: "\u1f25\u03b9",
    0x1F9E: "\u1f26\u03b9",
    0x1F9F: "\u1f27\u03b9",
    0x1FA0: "\u1f60\u03b9",
    0x1FA1: "\u1f61\u03b9",
    0x1FA2: "\u1f62\u03b9",
    0x1FA3: "\u1f63\u03b9",
    0x1FA4: "\u1f64\u03b9",
    0x1FA5: "\u1f65\u03b9",
    0x1FA6: "\u1f66\u03b9",
    0x1FA7: "\u1f67\u03b9",
    0x1FA8: "\u1f60\u03b9",
    0x1FA9: "\u1f61\u03b9",
    0x1FAA: "\u1f62\u03b9",
    0x1FAB: "\u1f63\u03b9",
    0x1FAC: "\u1f64\u03b9",
    0x1FAD: "\u1f65\u03b9",
    0x1FAE: "\u1f66\u03b9",
    0x1FAF: "\u1f67\u03b9",
    0x1FB2: "\u1f70\u03b9",
    0x1FB3: "\u03b1\u03b9",
    0x1FB4: "\u03ac\u03b9",
    0x1FB6: "\u03b1\u0342",
    0x1FB7: "\u03b1\u0342\u03b9",
    0x1FBC: "\u03b1\u03b9",
    0x1FBE: "\u03b9",
    0x1FC2: "\u1f74\u03b9",
    0x1FC3: "\u03b7\u03b9",
    0x1FC4: "\u03ae\u03b9",
    0x1FC6: "\u03b7\u0342",
    0x1FC7: "\u03b7\u0342\u03b9",
    0x1FCC: "\u03b7\u03b9",
    0x1FD2: "\u03b9\u0308\u0300",
    0x1FD3: "\u03b9\u0308\u0301",
    0x1FD6: "\u03b9\u0342",
    0x1FD7: "\u03b9\u0308\u0342",
    0x1FE2: "\u03c5\u0308\u0300",
    0x1FE3: "\u03c5\u0308\u0301",
    0x1FE4: "\u03c1\u0313",
    0x1FE6: "\u03c5\u0342",
    0x1FE7: "\u03c5\u0308\u0342",
    0x1FF2: "\u1f7c\u03b9",
    0x1FF3: "\u03c9\u03b9",
    0x1FF4: "\u03ce\u03b9",
    0x1FF6: "\u03c9\u0342",
    0x1FF7: "\u03c9\u0342\u03b9",
    0x1FFC: "\u03c9\u03b9",
    0x20A8: "rs",
    0x2102: "c",
    0x2103: "\xb0c",
    0x2107: "\u025b",
    0x2109: "\xb0f",
    0x210B: "h",
    0x210C: "h",
    0x210D: "h",
    0x2110: "i",
    0x2111: "i",
    0x2112: "l",
    0x2115: "n",
    0x2116: "no",
    0x2119: "p",
    0x211A: "q",
    0x211B: "r",
    0x211C: "r",
    0x211D: "r",
    0x2120: "sm",
    0x2121: "tel",
    0x2122: "tm",
    0x2124: "z",
    0x2128: "z",
    0x212C: "b",
    0x212D: "c",
    0x2130: "e",
    0x2131: "f",
    0x2133: "m",
    0x213E: "\u03b3",
    0x213F: "\u03c0",
    0x2145: "d",
    0x3371: "hpa",
    0x3373: "au",
    0x3375: "ov",
    0x3380: "pa",
    0x3381: "na",
    0x3382: "\u03bca",
    0x3383: "ma",
    0x3384: "ka",
    0x3385: "kb",
    0x3386: "mb",
    0x3387: "gb",
    0x338A: "pf",
    0x338B: "nf",
    0x338C: "\u03bcf",
    0x3390: "hz",
    0x3391: "khz",
    0x3392: "mhz",
    0x3393: "ghz",
    0x3394: "thz",
    0x33A9: "pa",
    0x33AA: "kpa",
    0x33AB: "mpa",
    0x33AC: "gpa",
    0x33B4: "pv",
    0x33B5: "nv",
    0x33B6: "\u03bcv",
    0x33B7: "mv",
    0x33B8: "kv",
    0x33B9: "mv",
    0x33BA: "pw",
    0x33BB: "nw",
    0x33BC: "\u03bcw",
    0x33BD: "mw",
    0x33BE: "kw",
    0x33BF: "mw",
    0x33C0: "k\u03c9",
    0x33C1: "m\u03c9",
    0x33C3: "bq",
    0x33C6: "c\u2215kg",
    0x33C7: "co.",
    0x33C8: "db",
    0x33C9: "gy",
    0x33CB: "hp",
    0x33CD: "kk",
    0x33CE: "km",
    0x33D7: "ph",
    0x33D9: "ppm",
    0x33DA: "pr",
    0x33DC: "sv",
    0x33DD: "wb",
    0xFB00: "ff",
    0xFB01: "fi",
    0xFB02: "fl",
    0xFB03: "ffi",
    0xFB04: "ffl",
    0xFB05: "st",
    0xFB06: "st",
    0xFB13: "\u0574\u0576",
    0xFB14: "\u0574\u0565",
    0xFB15: "\u0574\u056b",
    0xFB16: "\u057e\u0576",
    0xFB17: "\u0574\u056d",
    0x1D400: "a",
    0x1D401: "b",
    0x1D402: "c",
    0x1D403: "d",
    0x1D404: "e",
    0x1D405: "f",
    0x1D406: "g",
    0x1D407: "h",
    0x1D408: "i",
    0x1D409: "j",
    0x1D40A: "k",
    0x1D40B: "l",
    0x1D40C: "m",
    0x1D40D: "n",
    0x1D40E: "o",
    0x1D40F: "p",
    0x1D410: "q",
    0x1D411: "r",
    0x1D412: "s",
    0x1D413: "t",
    0x1D414: "u",
    0x1D415: "v",
    0x1D416: "w",
    0x1D417: "x",
    0x1D418: "y",
    0x1D419: "z",
    0x1D434: "a",
    0x1D435: "b",
    0x1D436: "c",
    0x1D437: "d",
    0x1D438: "e",
    0x1D439: "f",
    0x1D43A: "g",
    0x1D43B: "h",
    0x1D43C: "i",
    0x1D43D: "j",
    0x1D43E: "k",
    0x1D43F: "l",
    0x1D440: "m",
    0x1D441: "n",
    0x1D442: "o",
    0x1D443: "p",
    0x1D444: "q",
    0x1D445: "r",
    0x1D446: "s",
    0x1D447: "t",
    0x1D448: "u",
    0x1D449: "v",
    0x1D44A: "w",
    0x1D44B: "x",
    0x1D44C: "y",
    0x1D44D: "z",
    0x1D468: "a",
    0x1D469: "b",
    0x1D46A: "c",
    0x1D46B: "d",
    0x1D46C: "e",
    0x1D46D: "f",
    0x1D46E: "g",
    0x1D46F: "h",
    0x1D470: "i",
    0x1D471: "j",
    0x1D472: "k",
    0x1D473: "l",
    0x1D474: "m",
    0x1D475: "n",
    0x1D476: "o",
    0x1D477: "p",
    0x1D478: "q",
    0x1D479: "r",
    0x1D47A: "s",
    0x1D47B: "t",
    0x1D47C: "u",
    0x1D47D: "v",
    0x1D47E: "w",
    0x1D47F: "x",
    0x1D480: "y",
    0x1D481: "z",
    0x1D49C: "a",
    0x1D49E: "c",
    0x1D49F: "d",
    0x1D4A2: "g",
    0x1D4A5: "j",
    0x1D4A6: "k",
    0x1D4A9: "n",
    0x1D4AA: "o",
    0x1D4AB: "p",
    0x1D4AC: "q",
    0x1D4AE: "s",
    0x1D4AF: "t",
    0x1D4B0: "u",
    0x1D4B1: "v",
    0x1D4B2: "w",
    0x1D4B3: "x",
    0x1D4B4: "y",
    0x1D4B5: "z",
    0x1D4D0: "a",
    0x1D4D1: "b",
    0x1D4D2: "c",
    0x1D4D3: "d",
    0x1D4D4: "e",
    0x1D4D5: "f",
    0x1D4D6: "g",
    0x1D4D7: "h",
    0x1D4D8: "i",
    0x1D4D9: "j",
    0x1D4DA: "k",
    0x1D4DB: "l",
    0x1D4DC: "m",
    0x1D4DD: "n",
    0x1D4DE: "o",
    0x1D4DF: "p",
    0x1D4E0: "q",
    0x1D4E1: "r",
    0x1D4E2: "s",
    0x1D4E3: "t",
    0x1D4E4: "u",
    0x1D4E5: "v",
    0x1D4E6: "w",
    0x1D4E7: "x",
    0x1D4E8: "y",
    0x1D4E9: "z",
    0x1D504: "a",
    0x1D505: "b",
    0x1D507: "d",
    0x1D508: "e",
    0x1D509: "f",
    0x1D50A: "g",
    0x1D50D: "j",
    0x1D50E: "k",
    0x1D50F: "l",
    0x1D510: "m",
    0x1D511: "n",
    0x1D512: "o",
    0x1D513: "p",
    0x1D514: "q",
    0x1D516: "s",
    0x1D517: "t",
    0x1D518: "u",
    0x1D519: "v",
    0x1D51A: "w",
    0x1D51B: "x",
    0x1D51C: "y",
    0x1D538: "a",
    0x1D539: "b",
    0x1D53B: "d",
    0x1D53C: "e",
    0x1D53D: "f",
    0x1D53E: "g",
    0x1D540: "i",
    0x1D541: "j",
    0x1D542: "k",
    0x1D543: "l",
    0x1D544: "m",
    0x1D546: "o",
    0x1D54A: "s",
    0x1D54B: "t",
    0x1D54C: "u",
    0x1D54D: "v",
    0x1D54E: "w",
    0x1D54F: "x",
    0x1D550: "y",
    0x1D56C: "a",
    0x1D56D: "b",
    0x1D56E: "c",
    0x1D56F: "d",
    0x1D570: "e",
    0x1D571: "f",
    0x1D572: "g",
    0x1D573: "h",
    0x1D574: "i",
    0x1D575: "j",
    0x1D576: "k",
    0x1D577: "l",
    0x1D578: "m",
    0x1D579: "n",
    0x1D57A: "o",
    0x1D57B: "p",
    0x1D57C: "q",
    0x1D57D: "r",
    0x1D57E: "s",
    0x1D57F: "t",
    0x1D580: "u",
    0x1D581: "v",
    0x1D582: "w",
    0x1D583: "x",
    0x1D584: "y",
    0x1D585: "z",
    0x1D5A0: "a",
    0x1D5A1: "b",
    0x1D5A2: "c",
    0x1D5A3: "d",
    0x1D5A4: "e",
    0x1D5A5: "f",
    0x1D5A6: "g",
    0x1D5A7: "h",
    0x1D5A8: "i",
    0x1D5A9: "j",
    0x1D5AA: "k",
    0x1D5AB: "l",
    0x1D5AC: "m",
    0x1D5AD: "n",
    0x1D5AE: "o",
    0x1D5AF: "p",
    0x1D5B0: "q",
    0x1D5B1: "r",
    0x1D5B2: "s",
    0x1D5B3: "t",
    0x1D5B4: "u",
    0x1D5B5: "v",
    0x1D5B6: "w",
    0x1D5B7: "x",
    0x1D5B8: "y",
    0x1D5B9: "z",
    0x1D5D4: "a",
    0x1D5D5: "b",
    0x1D5D6: "c",
    0x1D5D7: "d",
    0x1D5D8: "e",
    0x1D5D9: "f",
    0x1D5DA: "g",
    0x1D5DB: "h",
    0x1D5DC: "i",
    0x1D5DD: "j",
    0x1D5DE: "k",
    0x1D5DF: "l",
    0x1D5E0: "m",
    0x1D5E1: "n",
    0x1D5E2: "o",
    0x1D5E3: "p",
    0x1D5E4: "q",
    0x1D5E5: "r",
    0x1D5E6: "s",
    0x1D5E7: "t",
    0x1D5E8: "u",
    0x1D5E9: "v",
    0x1D5EA: "w",
    0x1D5EB: "x",
    0x1D5EC: "y",
    0x1D5ED: "z",
    0x1D608: "a",
    0x1D609: "b",
    0x1D60A: "c",
    0x1D60B: "d",
    0x1D60C: "e",
    0x1D60D: "f",
    0x1D60E: "g",
    0x1D60F: "h",
    0x1D610: "i",
    0x1D611: "j",
    0x1D612: "k",
    0x1D613: "l",
    0x1D614: "m",
    0x1D615: "n",
    0x1D616: "o",
    0x1D617: "p",
    0x1D618: "q",
    0x1D619: "r",
    0x1D61A: "s",
    0x1D61B: "t",
    0x1D61C: "u",
    0x1D61D: "v",
    0x1D61E: "w",
    0x1D61F: "x",
    0x1D620: "y",
    0x1D621: "z",
    0x1D63C: "a",
    0x1D63D: "b",
    0x1D63E: "c",
    0x1D63F: "d",
    0x1D640: "e",
    0x1D641: "f",
    0x1D642: "g",
    0x1D643: "h",
    0x1D644: "i",
    0x1D645: "j",
    0x1D646: "k",
    0x1D647: "l",
    0x1D648: "m",
    0x1D649: "n",
    0x1D64A: "o",
    0x1D64B: "p",
    0x1D64C: "q",
    0x1D64D: "r",
    0x1D64E: "s",
    0x1D64F: "t",
    0x1D650: "u",
    0x1D651: "v",
    0x1D652: "w",
    0x1D653: "x",
    0x1D654: "y",
    0x1D655: "z",
    0x1D670: "a",
    0x1D671: "b",
    0x1D672: "c",
    0x1D673: "d",
    0x1D674: "e",
    0x1D675: "f",
    0x1D676: "g",
    0x1D677: "h",
    0x1D678: "i",
    0x1D679: "j",
    0x1D67A: "k",
    0x1D67B: "l",
    0x1D67C: "m",
    0x1D67D: "n",
    0x1D67E: "o",
    0x1D67F: "p",
    0x1D680: "q",
    0x1D681: "r",
    0x1D682: "s",
    0x1D683: "t",
    0x1D684: "u",
    0x1D685: "v",
    0x1D686: "w",
    0x1D687: "x",
    0x1D688: "y",
    0x1D689: "z",
    0x1D6A8: "\u03b1",
    0x1D6A9: "\u03b2",
    0x1D6AA: "\u03b3",
    0x1D6AB: "\u03b4",
    0x1D6AC: "\u03b5",
    0x1D6AD: "\u03b6",
    0x1D6AE: "\u03b7",
    0x1D6AF: "\u03b8",
    0x1D6B0: "\u03b9",
    0x1D6B1: "\u03ba",
    0x1D6B2: "\u03bb",
    0x1D6B3: "\u03bc",
    0x1D6B4: "\u03bd",
    0x1D6B5: "\u03be",
    0x1D6B6: "\u03bf",
    0x1D6B7: "\u03c0",
    0x1D6B8: "\u03c1",
    0x1D6B9: "\u03b8",
    0x1D6BA: "\u03c3",
    0x1D6BB: "\u03c4",
    0x1D6BC: "\u03c5",
    0x1D6BD: "\u03c6",
    0x1D6BE: "\u03c7",
    0x1D6BF: "\u03c8",
    0x1D6C0: "\u03c9",
    0x1D6D3: "\u03c3",
    0x1D6E2: "\u03b1",
    0x1D6E3: "\u03b2",
    0x1D6E4: "\u03b3",
    0x1D6E5: "\u03b4",
    0x1D6E6: "\u03b5",
    0x1D6E7: "\u03b6",
    0x1D6E8: "\u03b7",
    0x1D6E9: "\u03b8",
    0x1D6EA: "\u03b9",
    0x1D6EB: "\u03ba",
    0x1D6EC: "\u03bb",
    0x1D6ED: "\u03bc",
    0x1D6EE: "\u03bd",
    0x1D6EF: "\u03be",
    0x1D6F0: "\u03bf",
    0x1D6F1: "\u03c0",
    0x1D6F2: "\u03c1",
    0x1D6F3: "\u03b8",
    0x1D6F4: "\u03c3",
    0x1D6F5: "\u03c4",
    0x1D6F6: "\u03c5",
    0x1D6F7: "\u03c6",
    0x1D6F8: "\u03c7",
    0x1D6F9: "\u03c8",
    0x1D6FA: "\u03c9",
    0x1D70D: "\u03c3",
    0x1D71C: "\u03b1",
    0x1D71D: "\u03b2",
    0x1D71E: "\u03b3",
    0x1D71F: "\u03b4",
    0x1D720: "\u03b5",
    0x1D721: "\u03b6",
    0x1D722: "\u03b7",
    0x1D723: "\u03b8",
    0x1D724: "\u03b9",
    0x1D725: "\u03ba",
    0x1D726: "\u03bb",
    0x1D727: "\u03bc",
    0x1D728: "\u03bd",
    0x1D729: "\u03be",
    0x1D72A: "\u03bf",
    0x1D72B: "\u03c0",
    0x1D72C: "\u03c1",
    0x1D72D: "\u03b8",
    0x1D72E: "\u03c3",
    0x1D72F: "\u03c4",
    0x1D730: "\u03c5",
    0x1D731: "\u03c6",
    0x1D732: "\u03c7",
    0x1D733: "\u03c8",
    0x1D734: "\u03c9",
    0x1D747: "\u03c3",
    0x1D756: "\u03b1",
    0x1D757: "\u03b2",
    0x1D758: "\u03b3",
    0x1D759: "\u03b4",
    0x1D75A: "\u03b5",
    0x1D75B: "\u03b6",
    0x1D75C: "\u03b7",
    0x1D75D: "\u03b8",
    0x1D75E: "\u03b9",
    0x1D75F: "\u03ba",
    0x1D760: "\u03bb",
    0x1D761: "\u03bc",
    0x1D762: "\u03bd",
    0x1D763: "\u03be",
    0x1D764: "\u03bf",
    0x1D765: "\u03c0",
    0x1D766: "\u03c1",
    0x1D767: "\u03b8",
    0x1D768: "\u03c3",
    0x1D769: "\u03c4",
    0x1D76A: "\u03c5",
    0x1D76B: "\u03c6",
    0x1D76C: "\u03c7",
    0x1D76D: "\u03c8",
    0x1D76E: "\u03c9",
    0x1D781: "\u03c3",
    0x1D790: "\u03b1",
    0x1D791: "\u03b2",
    0x1D792: "\u03b3",
    0x1D793: "\u03b4",
    0x1D794: "\u03b5",
    0x1D795: "\u03b6",
    0x1D796: "\u03b7",
    0x1D797: "\u03b8",
    0x1D798: "\u03b9",
    0x1D799: "\u03ba",
    0x1D79A: "\u03bb",
    0x1D79B: "\u03bc",
    0x1D79C: "\u03bd",
    0x1D79D: "\u03be",
    0x1D79E: "\u03bf",
    0x1D79F: "\u03c0",
    0x1D7A0: "\u03c1",
    0x1D7A1: "\u03b8",
    0x1D7A2: "\u03c3",
    0x1D7A3: "\u03c4",
    0x1D7A4: "\u03c5",
    0x1D7A5: "\u03c6",
    0x1D7A6: "\u03c7",
    0x1D7A7: "\u03c8",
    0x1D7A8: "\u03c9",
    0x1D7BB: "\u03c3",
}


def map_table_b3(code):
    r = b3_exceptions.get(ord(code))
    if r is not None:
        return r
    return code.lower()


def map_table_b2(a):
    al = map_table_b3(a)
    b = unicodedata.normalize("NFKC", al)
    bl = "".join([map_table_b3(ch) for ch in b])
    c = unicodedata.normalize("NFKC", bl)
    if b != c:
        return c
    else:
        return al


def in_table_c11(code):
    return code == " "


def in_table_c12(code):
    return unicodedata.category(code) == "Zs" and code != " "


def in_table_c11_c12(code):
    return unicodedata.category(code) == "Zs"


def in_table_c21(code):
    return ord(code) < 128 and unicodedata.category(code) == "Cc"


c22_specials = set(
    [1757, 1807, 6158, 8204, 8205, 8232, 8233, 65279]
    + list(range(8288, 8292))
    + list(range(8298, 8304))
    + list(range(65529, 65533))
    + list(range(119155, 119163))
)


def in_table_c22(code):
    c = ord(code)
    if c < 128:
        return False
    if unicodedata.category(code) == "Cc":
        return True
    return c in c22_specials


def in_table_c21_c22(code):
    return unicodedata.category(code) == "Cc" or ord(code) in c22_specials


def in_table_c3(code):
    return unicodedata.category(code) == "Co"


def in_table_c4(code):
    c = ord(code)
    if c < 0xFDD0:
        return False
    if c < 0xFDF0:
        return True
    return (ord(code) & 0xFFFF) in (0xFFFE, 0xFFFF)


def in_table_c5(code):
    return unicodedata.category(code) == "Cs"


c6_set = set(range(65529, 65534))


def in_table_c6(code):
    return ord(code) in c6_set


c7_set = set(range(12272, 12284))


def in_table_c7(code):
    return ord(code) in c7_set


c8_set = set([832, 833, 8206, 8207] + list(range(8234, 8239)) + list(range(8298, 8304)))


def in_table_c8(code):
    return ord(code) in c8_set


c9_set = set([917505] + list(range(917536, 917632)))


def in_table_c9(code):
    return ord(code) in c9_set


def in_table_d1(code):
    return unicodedata.bidirectional(code) in ("R", "AL")


def in_table_d2(code):
    return unicodedata.bidirectional(code) == "L"
