/*
Реализуйте алгоритм сложения натуральных чисел, представленных в виде массива цифр в системе счисления по основанию p, где 1 < p < 230. Порядок цифр в массиве – little-endian (младшая цифра располагается в нулевом элементе массива).

func add(a, b []int32, p int) []int32 {
    ...
}
Составьте программу add.go, демонстрирующую работоспособность функции add.
*/




package main

import (
        "fmt"
)

func max(x, y int) int {
	if x > y {
		return x
	}
	return y
}

func min(x, y int) int {
	if x > y {
		return y
	}
	return x
}

func add(a, b []int32, p int) []int32 {
	result := make([]int32, 0, max(len(a), len(b)))
	var sum, carry int32
	carry = 0

	for i := 0; i < min(len(a), len(b)); i++ {
		sum = a[i] + b[i] + carry
		if sum >= int32(p) {
			sum -= int32(p)
			carry = 1
		} else {
			carry = 0
		}
		result = append(result, sum)
	}

	if len(a) > len(b) {
		for i := len(b); i < len(a); i++ {
			sum = a[i] + carry
			if sum >= int32(p) {
				sum -= int32(p)
				carry = 1
			} else {
				carry = 0
			}
			result = append(result, sum)
		}
	} else {
		if len(b) > len(a) {
			for i := len(a); i < len(b); i++ {
				sum = b[i] + carry
				if sum >= int32(p) {
					sum -= int32(p)
					carry = 1
				} else {
					carry = 0
				}
				result = append(result, sum)
			}
		}
	}

	if carry > 0 {
				result = append(result, carry)
			}

	return result
}

func main() {
	a := []int32 {1, 2, 3}
	b := []int32 {4, 5,7, 7}
	sum := add(a, b, 10)

	for i := len(a) - 1; i >= 0; i-- {
		fmt.Printf("%d", a[i])
	}
	fmt.Printf(" + ")
	for i := len(b) - 1; i >= 0; i-- {
		fmt.Printf("%d", b[i])
	}
	fmt.Printf("\n")

	for i := len(sum) - 1; i >= 0; i-- {
		fmt.Printf("%d", sum[i])
	}

}
