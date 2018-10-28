package main

import (
        "fmt"
)

type vertex struct {
        v int
	next *vertex
}

type graph struct  {
	visit int
	next *vertex
}

func main() {
	var n, m int

	fmt.Scanf("%d", &n)
	fmt.Scanf("%d\n", &m)
	//fmt.Printf("n = %d; m = %d\n", n ,m )

	a := make([]graph, n)

	for i := 0; i < m; i++ {
		var x, y int
		fmt.Scanf("%d", &x)
		fmt.Scanf("%d\n", &y)
		//fmt.Printf("%d %d\n", x, y)

		a[x].visit = 0
		a[y].visit = 0

		if a[x].next == nil {
			a[x].next = new(vertex)
			a[x].next.v = y
			a[x].next.next = nil
		} else {
			tek := a[x].next
			for tek = a[x].next; tek.next != nil; tek = tek.next {
			}
			tek.next = new(vertex)
			tek.next.v = y
			tek.next.next = nil
		}

		if a[y].next == nil {
			a[y].next = new(vertex)
			a[y].next.v = x
			a[y].next.next = nil
		} else {
			tek := a[x].next
			for tek = a[y].next; tek.next != nil; tek = tek.next {
			}
			tek.next = new(vertex)
			tek.next.v = x
			tek.next.next = nil
		}
	}
/*
	for i := 0; i < n; i++ {
		tek := a[i].next
		fmt.Printf("%d: ", i)
		for tek != nil {
			fmt.Printf("%d ", tek.v)
			tek = tek.next
		}
		fmt.Printf("\n")
	}
*/
	q := make(chan int, n)
	col := 0

	for i := 0; i < n; i++ {
		if a[i].visit == 0 {
			q <- i
			col++
			for len(q) > 0 {
				ver := <- q
				a[ver].visit = col
				tek := a[ver].next
				for tek != nil {
					if a[tek.v].visit == 0 {
						q <- tek.v
					}
					tek = tek.next
				}
			}
		}
	}

	fmt.Printf("Answer = %d\n", col)
}
