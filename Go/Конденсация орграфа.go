package main

import (
        "fmt"
)

var time, count int

type vertex struct {
    v int
	next *vertex
}

type graph struct  {
	next *vertex
	comp, T1, low int
}

type stack struct {
	a []int
	l int
}

func InitStack(x int, s *stack) {
	s.a = make([]int, x)
	s.l = 0
}

func Push(x int, s *stack) {
	s.a[s.l] = x
	s.l++
}

func Pop(s *stack)(int) {
	s.l--
	return s.a[s.l]
}

func VisitVertex_Tarjan(g []graph, v int, s *stack) {
	g[v].T1, g[v].low = time, time
	time++
	Push(v, s)
	tek := g[v].next
	for tek != nil {
		if g[tek.v].T1 == 0 {
			VisitVertex_Tarjan(g, tek.v, s)
		}
		if (g[tek.v].comp == 0) && (g[v].low > g[tek.v].low) {
			g[v].low = g[tek.v].low
		}
		tek = tek.next
	}

	if g[v].T1 == g[v].low {
		//fmt.Printf("%d\n", v)
		for {
			u := Pop(s)
			g[u].comp = count
			if u == v {
				break
			}
		}
		count++
	}
}

func Tarjan(g []graph, n int) {
	time, count = 1, 1
	for v := 0; v < n; v++ {
		g[v].T1, g[v].comp = 0, 0
	}
	var s stack
	InitStack(n, &s)
	for v := 0; v < n; v++ {
		if g[v].T1 == 0 {
			VisitVertex_Tarjan(g, v, &s)
		}
	}
}

func main() {
	var n, m int
	fmt.Scanf("%d\n", &n)
	fmt.Scanf("%d\n", &m)
	a := make([]graph, n)

	for i := 0; i < m; i++ {
		var x, y int
		fmt.Scanf("%d %d\n", &x, &y)
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
	}

	Tarjan(a, n)

	components := make([][]int, count)
	for i := 0; i < n; i++ {
		components[a[i].comp] = append(components[a[i].comp], i)
	}

	fmt.Printf("digraph name {\n")
	for i := 1; i < count; i++ {
		fmt.Printf("%d [label=\" ", i)
		for j := 0; j < len(components[i]); j++ {
			fmt.Printf("%d ", components[i][j])
		}
		fmt.Printf("\"]\n")
	}

	mark := make([][]byte, count)
	for i := 0; i < count; i++ {
		mark[i] = make([]byte, count)
	}

	for i := 0; i < n; i++ {
		tek := a[i].next
		for tek != nil {
			if (a[i].comp != a[tek.v].comp) && (mark[a[i].comp - 1][a[tek.v].comp - 1] != 1) {
				mark[a[i].comp - 1][a[tek.v].comp - 1] = 1
				fmt.Printf("%d -> %d\n", a[i].comp, a[tek.v].comp)
			}
			tek = tek.next
		}
	}
	fmt.Printf("}\n")
}
