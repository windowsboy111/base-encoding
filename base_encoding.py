char64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
alt128 = "!\"#$%&'()*+,-./0123456789:;<=>?@[\\]^_`{|}~µ¶¡¿¢£¤¥±ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzαβγδεζηθικλμνξοπρςστυφχψω"
char128 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789あいうえおかきくけこさしすせそざじずぜぞたちつてとだぢづでどなにぬねのはひふへほばびぶべぼぱぴぷぺぽまみむめもやゆよらりるれろわをん"
char256 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789ぁあぃいぅうぇえぉおかがきぎくぐけげこごさざしじすずせぜそぞただちぢっつづてでとどなにぬねのはばぱひびぴふぶぷへべぺほぼぽまみむめもゃやゅゆょよらりるれろゎわをんァアィイゥウェエォオカガキギクグケゲコゴサザシジスズセゼソゾタダチヂッツヅテデトドナニヌネノハバパヒビピフブプヘベペホボポマミムメモャヤュユョヨラリルレロヮワヲンヴヵヶ亜唖娃阿哀愛挨姶逢葵茜穐悪握渥旭葦芦鯵梓圧斡扱宛姐虻飴絢綾"
char512 = "!\"#$%&'()*+,-./0123456789:;<=>?@[\\]^_`{|}~¡¢£¤¥¦§©«¬®¯°±²³´µ¶·¹»¼½¾¿×÷˽∱∲∳∴∵∶∷∸∹∺∻∼∽∾∿≀≁≂≃≄≅ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzͰͱͲͳ͵ͶͷͺͻͼͽͿ΄ΆΈΉΊΌΎΏΐΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩΪΫάέήίΰαβγδεζηθικλμνξοπρςστυφχψωϊϋόύώϏϐϑϒϓϔϕϖϗϘϙϚϛϜϝϞϟϠϡϰϱϲϳϴϵ϶ϷϸϹϺϻϼϽϾϿᴦᴧᴨᴩᴪᵝᵞᵟᵠᵡᵦᵧᵨᵩᵪᶿἀἁἂἃἄἅἆἇἈἉἊἋἌἍἎἏἐἑἒἓἔἕἘἙἚἛἜἝἠἡἢἣἤἥἦἧἨἩἪἫἬἭἮἯἰἱἲἳἴἵἶἷἸἹἺἻἼἽἾἿὀὁὂὃὄὅὈὉὊὋὌὍὐὑὒὓὔὕὖὗὙὛὝὟὠὡὢὣὤὥὦὧὨὩὪὫὬὭὮὯὰάὲέὴήὶίὸόὺύὼώᾀᾁᾂᾃᾄᾅᾆᾇᾈᾉᾊᾋᾌᾍᾎᾏᾐᾑᾒᾓᾔᾕᾖᾗᾘᾙᾚᾛᾜᾝᾞᾟᾠᾡᾢᾣᾤᾥᾦᾧᾨᾩᾪᾫᾬᾭᾮᾯᾰᾱᾲᾳᾴᾶᾷᾸᾹᾺΆᾼ᾽ι᾿῀῁ῂῃῄῆῇῈΈῊΉῌ῍῎῏ῐῑῒΐῖῗῘῙῚΊ῝῞῟ῠῡῢΰῤῥῦῧῨῩῪΎῬ῭΅`ῲῳῴῶῷῸΌῺΏῼ´῾Ωꭥ"


class IntEncoder:
	@classmethod
	def encode_base64(cls, value: int) -> str:
		return (char64[value] if (value < 64) else cls.encode_base64(value // 64) + char64[value % 64]) if value >= 64 else char64[value]

	@classmethod
	def decode_base64(cls, value: str) -> int:
		return (char64.index(value[-1]) + cls.decode_base64(value[:-1]) * 64) if (len(value) > 1) else char64.index(value)

	@classmethod
	def encode_base128(cls, value: int) -> str:
		return (alt128[value] if (value < 128) else cls.encode_base128(value // 128) + alt128[value % 128]) if value >= 128 else alt128[value]

	@classmethod
	def decode_base128(cls, value: str) -> int:
		return (alt128.index(value[-1]) + cls.decode_base128(value[:-1]) * 128) if (len(value) > 1) else alt128.index(value)

	@classmethod
	def encode_base256(cls, value: int) -> str:
		return (char256[value] if (value < 256) else cls.encode_base256(value // 256) + char256[value % 256]) if value >= 256 else char256[value]

	@classmethod
	def decode_base256(cls, value: str) -> int:
		return (char256.index(value[-1]) + cls.decode_base256(value[:-1]) * 256) if (len(value) > 1) else char256.index(value)


class StrEncoder:
	@classmethod
	def encode_base64(cls, value: str) -> str:
		return IntEncoder.encode_base64(ord(value))

	@classmethod
	def decode_base64(cls, value: str) -> str:
		return chr(IntEncoder.decode_base64(value))

	@classmethod
	def encode_base128(cls, value: str) -> str:
		return IntEncoder.encode_base128(ord(value))

	@classmethod
	def decode_base128(cls, value: str) -> str:
		return chr(IntEncoder.decode_base64(value))

	@classmethod
	def encode_base256(cls, value: str) -> str:
		return IntEncoder.encode_base256(ord(value))

	@classmethod
	def decode_base256(cls, value: str) -> str:
		return chr(IntEncoder.decode_base256(value))

def encode(encodeStr: str, value: int) -> str:
	return (encodeStr[value] if (value < len(encodeStr)) else encode(encodeStr, value // len(encodeStr)) + encodeStr[value % len(encodeStr)]) if value >= len(encodeStr) else encodeStr[value]
def decode(encodeStr: str, value: str) -> int:
	return (encodeStr.index(value[-1]) + decode(encodeStr, value[:-1]) * len(encodeStr)) if (len(value) > 1) else encodeStr.index(value)