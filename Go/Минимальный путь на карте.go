package main

import (
        "fmt"
)

func main() {
	const (
		MAXN int = 500
		MAXINT = 2147483647
	)
	var (
		x, y, n int
		a, b [MAXN][MAXN] int
	)

	fmt.Scanf("%d\n", &n)
	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			fmt.Scanf("%d", &a[i][j])
			b[i][j] = MAXINT
		}
		fmt.Scanf("\n")
	}

	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			fmt.Printf("%d ", a[i][j])
		}
		fmt.Printf("\n")

	}

	x_mov := [4]int {0, 0, -1, 1}
	y_mov := [4]int {1, -1, 0, 0}
	b[0][0] = a[0][0]
	q := make(chan int, n * n)
	q <- 0
	for len(q) > 0 {
		x = <-q
		y = x % 1000
		x /= 1000
		//fmt.Printf("%d %d len = %d\n", x, y, len(q))
		for i, _ := range(x_mov) {
			if ((x + x_mov[i] >= 0) && (x + x_mov[i] < n)) && ((y + y_mov[i] >= 0) && (y + y_mov[i] < n)) {
				if a[x + x_mov[i]][y + y_mov[i]] + b[x][y] < b[x + x_mov[i]][y + y_mov[i]] {
					b[x + x_mov[i]][y + y_mov[i]] = a[x + x_mov[i]][y + y_mov[i]] + b[x][y]
					//fmt.Printf("%d %d %d\n", x + x_mov[i], y + y_mov[i], b[x + x_mov[i]][y + y_mov[i]])
					q <- (x + x_mov[i]) * 1000 + (y + y_mov[i])
				}
			}
		}
	}

	fmt.Printf("%d\n", b[n - 1][n - 1])
}
