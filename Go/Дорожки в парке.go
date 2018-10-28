// kruskal project main.go
package main

import (
        "fmt"
	"math"
)

type edge struct {
	u, v int
}

type point struct {
	x, y int
}

func SpanningTree(e []edge, n int, m int)([]edge) {
	e_new := make([]edge, 0, m)
	s := make([]int, n)
	for i := 0; i < n; i++ {
		s[i] = 0
	}
	t := 1
	for i := 0; (i < m) && (len(e_new) < n - 1); i++ {
		if (s[e[i].u] == 0) && (s[e[i].v] == 0) && (e[i].u != e[i].v) {
			s[e[i].u], s[e[i].v] = t, t
			t++
			e_new = append(e_new, e[i])
		} else if (s[e[i].u] != s[e[i].v]) {
			if s[e[i].u] == 0 {
				s[e[i].u] = s[e[i].v]
			} else if s[e[i].v] == 0 {
				s[e[i].v] = s[e[i].u]
			} else {
				k := s[e[i].v]
				for j := 0; j < n; j++ {
					if s[j] == k {
						s[j] = s[e[i].u]
					}
				}
			}
			e_new = append(e_new, e[i])
		}
	}

	return e_new
}


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
	var n int

	fmt.Scanf("%d\n", &n)

	a := make([]point, n)
	for i := 0; i < n; i++ {
		fmt.Scanf("%d %d\n", &a[i].x, &a[i].y)
	}

	edg := make([]edge, 0, n * (n - 1) / 2)
	for i := 0; i < n; i++ {
		for j := i + 1; j < n; j++ {
			var buf edge
			buf.u, buf.v = i, j
			edg = append(edg, buf)
		}
	}

	qsort(len(edg),
		func (i, j int) bool { return (a[edg[i].u].x - a[edg[i].v].x) * (a[edg[i].u].x - a[edg[i].v].x) +
		(a[edg[i].u].y - a[edg[i].v].y) * (a[edg[i].u].y - a[edg[i].v].y) <
		(a[edg[j].u].x - a[edg[j].v].x) * (a[edg[j].u].x - a[edg[j].v].x) +
		(a[edg[j].u].y - a[edg[j].v].y) * (a[edg[j].u].y - a[edg[j].v].y)  },
		func (i, j int) { edg[i], edg[j] = edg[j], edg[i] },
		)

	ans := SpanningTree(edg, n, len(edg))
	var sum float64 = 0

	for i := 0; i < len(ans); i++ {
		sum += math.Sqrt((float64)((a[ans[i].u].x - a[ans[i].v].x)) * (float64)((a[ans[i].u].x - a[ans[i].v].x)) +
		(float64)((a[ans[i].u].y - a[ans[i].v].y)) * (float64)((a[ans[i].u].y - a[ans[i].v].y)))
	}
	fmt.Printf("%f\n", sum)
}
