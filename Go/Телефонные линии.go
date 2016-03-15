// prim project main.go
package main

import (
        "fmt"
)

type vertex struct {
    v, l int
	next *vertex
}

type graph struct  {
	next *vertex
	index, key, value int
}

type queue struct {
	heap []int
	count int
}

func Init(n int, q *queue) {
	q.heap = make([]int, n)
	q.count = 0
}

func Insert(q *queue, g []graph, x int) {
	q.heap[q.count] = x
	q.count++
	var i int
	for i = q.count - 1; (i > 0) && (g[q.heap[(i - 1) / 2]].key > g[q.heap[i]].key); i = (i - 1) / 2 {
		q.heap[(i - 1) / 2], q.heap[i] = q.heap[i], q.heap[(i - 1) / 2]
		g[q.heap[i]].index = i
	}
	g[q.heap[i]].index = i
}

func Heapify(i int, n int, p []int, g []graph) {
	for {
		l := 2 * i + 1
		r := l + 1
		j := i
		if (l < n) && (g[p[i]].key > g[p[l]].key) {
			i = l
		}
		if (r < n) && (g[p[i]].key > g[p[r]].key) {
			i = r
		}
		if i == j {
			break
		}
		p[i], p[j] = p[j], p[i]
		g[p[i]].index = i
		g[p[j]].index = j
	}
}

func ExtractMin(q *queue, g []graph)(int) {
	ptr := q.heap[0]
	q.count--
	if q.count > 0 {
		q.heap[0] = q.heap[q.count]
		g[q.heap[0]].index = 0
		Heapify(0, q.count, q.heap, g)
	}
	return ptr
}

func DecreaseKey(q *queue, i int, k int, g []graph) {
	g[q.heap[i]].key = k
	for (i > 0) && (g[q.heap[(i - 1) / 2]].key > k) {
		q.heap[(i - 1) / 2], q.heap[i] = q.heap[i], q.heap[(i - 1) / 2]
		g[q.heap[i]].index = i
		i = (i - 1) / 2
	}
	g[q.heap[i]].index = i
}

func MST_Prim(g []graph, n int)(int) {
	for i := 0; i < n; i++ {
		g[i].index = -1
	}
	answer := 0
	var q queue
	Init(n - 1, &q)

	v := 0
		for {
			g[v].index = -2
			tek := g[v].next
			for tek != nil {
				if g[tek.v].index == -1 {
					g[tek.v].key = tek.l
					g[tek.v].value = v
					Insert(&q, g, tek.v)
				} else if (g[tek.v].index != -2) && (tek.l < g[tek.v].key) {
					g[tek.v].value = v
					DecreaseKey(&q, g[tek.v].index, tek.l, g)
				}
				tek = tek.next
			}
			if q.count == 0 {
				break
			}
			v = ExtractMin(&q, g)
			answer += g[v].key
		}
	return answer
}

func main() {
	var n, m int
	fmt.Scanf("%d\n", &n)
	fmt.Scanf("%d\n", &m)
	a := make([]graph, n)

	for i := 0; i < m; i++ {
		var x, y, l int
		fmt.Scanf("%d %d %d\n", &x, &y, &l)

		if a[x].next == nil {
			a[x].next = new(vertex)
			a[x].next.v = y
			a[x].next.l = l
			a[x].next.next = nil
		} else {
			tek := a[x].next
			for tek = a[x].next; tek.next != nil; tek = tek.next {
			}
			tek.next = new(vertex)
			tek.next.v = y
			tek.next.l = l
			tek.next.next = nil
		}

		if a[y].next == nil {
			a[y].next = new(vertex)
			a[y].next.v = x
			a[y].next.l = l
			a[y].next.next = nil
		} else {
			tek := a[x].next
			for tek = a[y].next; tek.next != nil; tek = tek.next {
			}
			tek.next = new(vertex)
			tek.next.v = x
			tek.next.l = l
			tek.next.next = nil
		}
	}

	fmt.Printf("%d\n", MST_Prim(a, n))
}
