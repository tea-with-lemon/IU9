/*
Реализуйте алгоритмы перевода текста из UTF-32 в UTF-8, и обратно. Алгоритмы должны быть оформлены в виде двух функций:

func encode(utf32 []rune) []byte {
    ...
}

func decode(utf8 []byte) []rune {
    ...
}
Функция encode принимает в качестве параметра текст в виде массива кодовых точек и возвращает образ этого текста в UTF-8. Функция decode выполняет обратное преобразование.
Правила кодирования текста в UTF-8 приведены в таблице:

Код символа в Unicode	       |        1	       |        2	      |      3	      |       4     |
-----------------------------------------------------------------------------------------------
0 0000 0000 0000 0xxx xxxx   |    0xxx xxxx    |        -       |      -        |       -     |
-----------------------------------------------------------------------------------------------
0 0000 0000 0yyy yyxx xxxx   |    110y yyyy    |    10xx xxxx   |      -        |       -     |
-----------------------------------------------------------------------------------------------
0 0000 zzzz yyyy yyxx xxxx   |    1110 zzzz    |    10yy yyyy   |   10xx xxxx   |       -     |
-----------------------------------------------------------------------------------------------
u uuzz zzzz yyyy yyxx xxxx   |    1111 0uuu    |    10zz zzzz   |   10yy yyyy   |    10xx xxxx|
----------------------------------------------------------------------------------------------
Составьте программу utf8.go, демонстрирующую работоспособность функций decode и encode. Проверьте правильность результатов работы функций с помощью встроенных средств Go.
*/





package main

import (
        "fmt"
)

func decode(utf8 []byte) []uint32 {
    var utf32 []uint32
        var sym uint32
    for i := 0; i < len(utf8); i++ {
		if utf8[i] & 0x00000080 == 0 {
			utf32 = append(utf32, uint32(utf8[i]))
		} else if utf8[i] & 0x000000E0 == 0x000000C0 {
				sym = ((uint32(utf8[i]) & 0x0000001F) << 6) | (uint32(utf8[i+1]) & 0x0000003F)
				utf32 = append(utf32, sym)
				i++
			} else if utf8[i] & 0x000000F0 == 0x000000E0 {
					sym = ((uint32(utf8[i]) & 0x0000000F) << 6) | (uint32(utf8[i+1]) & 0x0000003F)
					i++
					sym = (sym << 6) | (uint32(utf8[i+1]) & 0x0000003F)
                	utf32 = append(utf32, sym)
                	i++
				} else {
					sym = ((uint32(utf8[i]) & 0x00000007) << 6) | ((uint32(utf8[i+1])) & 0x0000003F)
					i++
					sym = (sym << 6) | ((uint32(utf8[i+1])) & 0x0000003F)
					i++
					sym = (sym << 6) | ((uint32(utf8[i+1])) & 0x0000003F)
                	utf32 = append(utf32, sym)
                	i++
				}
    }
	return utf32
}

func encode(utf32 []uint32) []byte {
    var utf8 []byte
    for _, x := range utf32 {
        if x < 0x0000007F {
            utf8 = append(utf8, byte(x))
        } else if x < 0x000007FF {
	            b1 := byte(((x & 0x000007C0) >> 6)| 0x000000C0)
	            b2 := byte((x & 0x0000003F) | 0x00000080)
	            utf8 = append(utf8, b1, b2)
	        } else if x < 0x0000FFFF {
		            b1 := byte(((x & 0x0000F000) >> 12)| 0x000000E0)
		            b2 := byte(((x & 0x00000FC0) >> 6 )| 0x00000080)
		            b3 := byte((x & 0x0000003F) | 0x00000080)
		            utf8 = append(utf8, b1, b2, b3)
		        } else {
		            b1 := byte(((x & 0x00180000) >> 18)| 0x03C00000)
		            b2 := byte(((x & 0x0003F000) >> 12)| 0x00080000)
		            b3 := byte(((x & 0x00000FC0) >> 6 )| 0x00002000)
		            b4 := byte((x & 0x0000003F) | 0x00000080)
		            utf8 = append(utf8, b1, b2, b3, b4)
		        }
    }
    return utf8
}

func main() {
	example := []uint32{'万', '里', '长', '城'}
	result1 := encode(example)
	result2 := decode(result1)
	fmt.Printf("%s\n%s\n%s\n", example, result1, result2)
}
