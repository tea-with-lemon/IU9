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

func DFS(a []graph, v int, n int) {
	fmt.Printf("%d ", v)
	a[v].visit = 1

	for i := 0; i < n; i++ {
		for tek := a[v].next; tek != nil; tek = tek.next {
			if tek.v != i {
				continue
			}
			if a[tek.v].visit == 0 {
				DFS(a, tek.v, n)
			}
		}
	}
}

func main() {
	var n, m, v int

	fmt.Scanf("%d", &n)
	fmt.Scanf("%d", &m)
	fmt.Scanf("%d", &v)
	//fmt.Printf("%d %d %d\n", n, m, v)

	a := make([]graph, n)

	for i := 0; i < m; i++ {
		var x, y int
		fmt.Scanf("%d %d", &x, &y)
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

	DFS(a, v, n)
}
