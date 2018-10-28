/*
Реализуйте алгоритм быстрой сортировки произвольных данных в функции

func qsort(n int,
           less func(i, j int) bool,
           swap func(i, j int)) {
    ...
}
В качестве параметров функция qsort должна принимать:
n – количество сортируемых записей,
less – функцию сравнения i-той и j-той записи,
swap – функцию обмена i-той и j-той записи.
Составьте программу qsort.go, демонстрирующую работоспособность функции qsort.
*/



package main

import (
        "fmt"
)

func qsort(n int,
           less func(i, j int) bool,
           swap func(i, j int)) {
	low := 0
	high := n - 1

	partition := func(low, high int) int {
		i, j := low, low
		for j < high{
			if less(j, high){
				swap(i, j)
				i++
			}
			j++
		}
		swap(i, high)
		return i
	}

	var qsortrec func(int, int)
	qsortrec = func(low, high int){
		if low < high{
			q := partition( low, high)
			qsortrec(low, q - 1)
			qsortrec(q + 1, high)
		}
	}

	qsortrec(low, high);
}

func main() {
	A := []int { 2, 4, 6, 8, 1, 3, 5, 7, 9}
	qsort(len(A),
		func (i, j int) bool { return A[i] < A[j] },
		func (i, j int) { A[i], A[j] = A[j], A[i] },
		)

	for _, x := range A { fmt.Printf("%d ", x) }
}
