ackage main

import (
        "fmt"
        "github.com/skorobogatov/input"
)

func Split1(n int, delta [][]int, fi [][]byte)(int, []int) {
	m := n
	pi := make([]int, m)

	for i := 0; i < m; i++ {
		pi[i] = i
	}

	for q1 := 0; q1 < n; q1++ {
		for q2 := 0; q2 < n; q2++ {
			if pi[q1] != pi[q2] {
				eq := 1
				for x := 0; x < 3; x++ {
					if fi[q1][x] != fi[q2][x] {
						eq = 0
						break
					}
				}
				if eq == 1 {
					k := pi[q1]
					for j := 0; j < n; j++ {
						if pi[j] == k {
							pi[j] = pi[q2]
						}
					}
					m--
				}
			}
		}
	}

	return m, pi
}

func Split(n int, delta [][]int, fi [][]byte, pi []int)(int, []int) {
	m_ := n
	pi_ := make([]int, m_)

	for i := 0; i < m_; i++ {
		pi_[i] = i
	}

	for q1 := 0; q1 < n; q1++ {
		for q2 := 0; q2 < n; q2++ {
			if (pi[q1] == pi[q2]) && (pi_[q1] != pi_[q2]) {
				eq := 1
				for x := 0; x < 3; x++ {
					w1, w2 := delta[q1][x], delta[q2][x]
					if pi[w1] != pi[w2] {
						eq = 0
						break
					}
				}
				if eq == 1 {
					k := pi_[q1]
					for j := 0; j < n; j++ {
						if pi_[j] == k {
							pi_[j] = pi_[q2]
						}
					}
					m_--
				}
			}
		}
	}

	return m_, pi_
}

func AufenkampHohn(n int, delta [][]int, fi [][]byte)([][]int, [][]byte, int) {
	m, pi := Split1(n, delta, fi)

	var pi_ []int
	var m_ int

	for {
		m_, pi_ = Split(n, delta, fi, pi)
		if m == m_ {
			break
		}
		m, pi = m_, pi_
	}

	fi_ := make([][]byte, m)
	delta_ := make([][]int, m)

	for i := 0; i < m; i++ {
		fi_[i] = make([]byte, 3)
		delta_[i] = make([]int, 3)
	}

	count := 0
	for i := 0; i < n; i++ {
		if pi_[i] < count {
			continue
		}
		buf := pi_[i]
		for j := i; j < n; j++ {
			if pi_[j] == buf {
				pi_[j] = count
			}
		}
		count++
	}

	for i := 0; i < n; i++ {
		q_ := pi_[i]
		for x := 0; x < 3; x++ {
			delta_[q_][x] = pi_[delta[i][x]]
			fi_[q_][x] = fi[i][x]
		}
	}

	return delta_, fi_, m
}

func main() {
	var n int
	input.Scanf("%d", &n)

	fi := make([][]byte, n)
	delta := make([][]int, n)
	for i := 0; i < n; i++ {
		fi[i] = make([]byte, 3)
		delta[i] = make([]int, 3)
	}

	for i := 0; i < n; i++ {
		for j := 0; j < 3; j++ {
			input.Scanf("%d", &delta[i][j])
		}
	}
	input.Scanf("\n")
	for i := 0; i < n; i++ {
		for j := 0; j < 3; j++ {
			var s string
                        input.Scanf("%s", &s)
                        fi[i][j] = s[0]
		}
	}

	delta_, fi_, n_ := AufenkampHohn(n, delta, fi)

	fmt.Printf("digraph {\nrankdir = LR\n")
	for i := 0; i < n_; i++ {
		for j := 0; j < 3; j++ {
			fmt.Printf("%d -> %d [label = \"%c(%c)\"]\n", i, delta_[i][j], 'a' + j, fi_[i][j])
		}
	}
	fmt.Printf("}\n")
}
