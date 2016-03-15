package main

import (
        "fmt"
)

type vertex struct {
        v int
        s string
	next *vertex
}

type graph struct  {
	next *vertex
}

var visit []string

func DFS(a []graph, v int, n int, m int, parent string) {
	f := 1
	for i := 0; i < n; i++ {
		for tek := a[v].next; tek != nil; tek = tek.next {
			//fmt.Printf("ver = %d, tekv = %d, i = %d\n", v, tek.v, i)
			if tek.v != i {
				continue
			}

			flag := 1

			for _, x := range(visit) {
				if x == tek.s {
					flag = 0
					break
				}
			}
			if flag == 1 {
				f = 0
				visit = append(visit, tek.s)
				fmt.Printf("%s ", tek.s)
				DFS(a, tek.v, n, m, tek.s)
			}
		}
	}
	if (f == 1) && (len(visit) != m) {
		fmt.Printf("%s ", parent)
	}
}

func main() {
	var n, m, v int

	fmt.Scanf("%d", &n)
	fmt.Scanf("%d", &m)
	fmt.Scanf("%d", &v)

	a := make([]graph, n)

	for i := 0; i < m; i++ {
		var x, y int
		var s string
		fmt.Scanf("%d %d %s", &x, &y, &s)

		if a[x].next == nil {
			a[x].next = new(vertex)
			a[x].next.v = y
			a[x].next.s = s
			a[x].next.next = nil
		} else {
			tek := a[x].next
			for tek = a[x].next; tek.next != nil; tek = tek.next {
			}
			tek.next = new(vertex)
			tek.next.v = y
			tek.next.s = s
			tek.next.next = nil
		}

		if a[y].next == nil {
			a[y].next = new(vertex)
			a[y].next.v = x
			a[y].next.s = s
			a[y].next.next = nil
		} else {
			tek := a[x].next
			for tek = a[y].next; tek.next != nil; tek = tek.next {
			}
			tek.next = new(vertex)
			tek.next.v = x
			tek.next.s = s
			tek.next.next = nil
		}
	}

	DFS(a, v, n, m, "")
}
