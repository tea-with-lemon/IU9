/*
Составьте программу gauss.go, выполняющую решение системы линейных алгебраических уравнений в рациональных числах методом Гаусса.
Формат входных данных:
Программа должна считывать из входного потока число N уравнений (1 ≤ N ≤ 5) и матрицу системы размером N ×(N  + 1). Матрица содержит целые числа от -9 до 9.
Формат результата работы программы:
Если система не имеет решения, следует выводить фразу "No solution".
Если решение существует, программа должна печатать в выходной поток N значений переменных, каждое из которых представляет собой нормализованное рациональное число, записанное в виде n/d, где n – числитель дроби, d – знаменатель дроби.
Например, если на вход программы подаётся

3
-4  -1   8   2
 7  -7   7   3
 5  -1  -4   7

то на выходе мы получаем

377/21
214/7
274/21
*/






package main

import (
        "fmt"
	"os"
)

func abs(a int) int {
	if a < 0 {
		return -a
	}
	return a
}

func nod(x, y int) int {
	if x == 0 || y == 0 {
		return x + y
	}
	if x > y {
		return nod(x % y, y)
	}
	return nod(x, y % x)
}

func main() {
	var n int
	var a, b [10][10]int // a[i][j] / b[i][j]

	fmt.Scanf("%d", &n)

	for i := 0; i < n; i++ {
		for j := 0; j < n + 1; j++ {
			fmt.Scanf("%d", &a[i][j])
			b[i][j] = 1
		}
	}

	for i := 0; i < n; i++ {
		if a[i][i] == 0 {
			for j := i + 1; j < n; j++ {
				if a[j][i] != 0 {
					for z := 0; z < n; z++ {
						a[i][z], a[j][z] = a[j][z], a[i][z]
						b[i][z], b[j][z] = b[j][z], b[i][z]
					}
					break
				}
			}
			if a[i][i] == 0 {
				fmt.Printf("No solution\n")
				os.Exit(0)
			}
		}
	}

	for i := 0; i < n; i++ {
		chisl := a[i][i]
		zname := b[i][i]
		for j := 0; j < n + 1; j++ {
			a[i][j], b[i][j] = a[i][j] * zname, b[i][j] * chisl
			k := nod(abs(a[i][j]), abs(b[i][j]))
			if k == 0 {
				fmt.Printf("No solution\n")
				os.Exit(0)
			}
			a[i][j], b[i][j] = a[i][j] / k, b[i][j] /k
		}

		for j := 0; j < n; j++ {
			if j == i {
				continue
			}
			chisl := a[j][i]
			zname := b[j][i]
			for z := 0; z < n + 1; z++ {
				a[j][z] = a[j][z] * zname * b[i][z] - chisl * b[j][z] * a[i][z]
				b[j][z] *= zname * b[i][z]
				k := nod(abs(a[j][z]), abs(b[j][z]))
				a[j][z], b[j][z] = a[j][z] / k, b[j][z] / k
			}
		}
	}

	for i := 0; i < n; i++ {
		for j := 0; j < n + 1; j++ {
			fmt.Printf("%d/%d ", a[i][j], b[i][j])
		}
		fmt.Printf("\n")
	}
	fmt.Printf("ANSSWER:\n")
	for i := 0; i < n; i++ {
		fmt.Printf("%d/%d\n", a[i][n], b[i][n])
	}
}
