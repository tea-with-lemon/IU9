package main

import (
        "fmt"
        "github.com/skorobogatov/input"
)

type vertex struct {
    num int
    color int
    next *vertex
}

func main() {

	var n, m int

	input.Scanf("%d%d", &n, &m)

	length := make([]int, n)
	list := make([]vertex, n)

	for i := 0; i < n; i++ {
		length[i] = 300000
	}

	for i := 0; i < m; i++ {
		var x, y, c int
		input.Scanf ("%d%d%d", &x, &y, &c)
		x--
		y--

		if list[x].next == nil{
			list[x].next = new(vertex)
			list[x].next.num = y
			list[x].next.color = c
			list[x].next.next = nil
		} else {
			tek := list[x].next
			for tek = list[x].next; tek.next != nil; tek = tek.next {
			}
			tek.next = new(vertex)
			tek.next.num = y
			tek.next.color = c
			tek.next.next = nil
		}

		if list[y].next == nil{
			list[y].next = new(vertex)
			list[y].next.num = x
			list[y].next.color = c
			list[y].next.next = nil
		} else {
			tek := list[y].next
			for tek = list[y].next; tek.next != nil; tek = tek.next {
			}
			tek.next = new(vertex)
			tek.next.num = x
			tek.next.color = c
			tek.next.next = nil
		}

	}

	start := n - 1
	finish := 0
	length[start] = 0

	/*
	for i := 0; i < n; i++ {
		tek := list[i].next
		fmt.Printf("%d: ", i)
		for tek != nil {
			fmt.Printf("%d ", tek.num)
			tek = tek.next
		}
		fmt.Printf("\n")
	}
	*/

	q1 := make (chan int, n)
	q2 := make (chan int, n)
	q3 := make (chan int, n)

	q1 <- start

	for len(q1) > 0 {
		tek := <-q1
		for k := list[tek].next; k != nil; k = k.next{
			if length[k.num] > length[tek] + 1 {
				length[k.num] = length[tek] + 1
				q1 <- k.num
			}
		}
	}

	fmt.Printf("%d\n", length[finish])

	q1 <- finish
	q2 <- finish
	for i := 0; i < length[finish]; i++ {
		min := 300000
		for len(q1) > 0 {
			tek := <-q1
			for k := list[tek].next; k != nil; k = k.next{
				if length[k.num] == length[tek] - 1 && k.color < min {
					min = k.color
				}
			}
		}
		for len(q2) > 0 {
			tek := <-q2
			for k := list[tek].next; k != nil; k = k.next{
				if length[k.num] == length[tek] - 1 && k.color == min {
					q3 <- k.num
				}
			}
		}

		fmt.Printf("%d ", min)

		for len(q3) > 0 {
			tek := <-q3
			q1 <- tek
			q2 <- tek
		}
	}

	fmt.Printf("\n")
}
