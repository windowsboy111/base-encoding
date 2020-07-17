char64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
char128 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789あいうえおかきくけこさしすせそざじずぜぞたちつてとだぢづでどなにぬねのはひふへほばびぶべぼぱぴぷぺぽまみむめもやゆよらりるれろわをん"
char256 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789ぁあぃいぅうぇえぉおかがきぎくぐけげこごさざしじすずせぜそぞただちぢっつづてでとどなにぬねのはばぱひびぴふぶぷへべぺほぼぽまみむめもゃやゅゆょよらりるれろゎわをんァアィイゥウェエォオカガキギクグケゲコゴサザシジスズセゼソゾタダチヂッツヅテデトドナニヌネノハバパヒビピフブプヘベペホボポマミムメモャヤュユョヨラリルレロヮワヲンヴヵヶ亜唖娃阿哀愛挨姶逢葵茜穐悪握渥旭葦芦鯵梓圧斡扱宛姐虻飴絢綾"


def encode_base64(value: int) -> str:
    return (char64[value] if (value < 64) else encode_base64(value // 64) + char64[value % 64]) if value >= 64 else char64[value]


def decode_base64(value: str) -> int:
    return (char64.index(value[-1]) + decode_base64(value[:-1]) * 64) if (len(value) > 1) else char64.index(value)


def encode_base128(value: int) -> str:
    return (char128[value] if (value < 128) else encode_base128(value // 128) + char128[value % 128]) if value >= 128 else char128[value]


def decode_base128(value: str) -> int:
    return (char128.index(value[-1]) + decode_base128(value[:-1]) * 128) if (len(value) > 1) else char128.index(value)


def encode_base256(value: int) -> str:
    return (char256[value] if (value < 256) else encode_base256(value // 256) + char256[value % 256]) if value >= 256 else char256[value]


def decode_base256(value: str) -> int:
    return (char256.index(value[-1]) + decode_base256(value[:-1]) * 256) if (len(value) > 1) else char256.index(value)
