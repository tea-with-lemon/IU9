package main

import (
	"fmt"
)

func DFS(used []int, massiv [][]int, begin int, index *int, m int) {
	used[begin] = *index
	(*index)++
	for i := 0; i < m; i++ {
		if used[massiv[begin][i]] == -1 {
			DFS(used, massiv, massiv[begin][i], index, m)
		}
	}
}

func main() {
	var (
		n, m, q, index int
		M              = [][]int{}
		S              = [][]string{}
		MNew           = [][]int{}
		SNew           = [][]string{}
		used           = []int{}
		value          int
		value1         string
	)
	fmt.Scan(&n, &m, &q)
	for i := 0; i < n; i++ {
		M = append(M, []int{})
		for j := 0; j < m; j++ {
			fmt.Scan(&value)
			M[i] = append(M[i], value)
		}
	}
	for i := 0; i < n; i++ {
		S = append(S, []string{})
		for j := 0; j < m; j++ {
			fmt.Scan(&value1)
			S[i] = append(S[i], value1)
		}
	}
	used = make([]int, n)
	for i := 0; i < n; i++ {
		used[i] = -1
	}
	MNew = make([][]int, n)
	for i := range MNew {
		MNew[i] = make([]int, m)
	}
	SNew = make([][]string, n)
	for i := range SNew {
		SNew[i] = make([]string, m)
	}

	DFS(used, M, q, &index, m)
	for i := 0; i < n; i++ {
		if used[i] != -1 {
			SNew[used[i]] = S[i]
			for j := 0; j < m; j++ {
				MNew[used[i]][j] = used[M[i][j]]
			}
		}
	}
	fmt.Print(index, "\n", m, "\n", 0, "\n")
	for i := 0; i < index; i++ {
		for j := 0; j < m; j++ {
			fmt.Print(MNew[i][j], " ")
		}
		fmt.Println()
	}
	for i := 0; i < index; i++ {
		for j := 0; j < m; j++ {
			fmt.Print(SNew[i][j], " ")
		}
		fmt.Println()
	}
}
