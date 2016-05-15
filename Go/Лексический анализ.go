/*
Пусть идентификатор – это последовательность латинских букв и цифр, начинающаяся с буквы.
Известно, что в некоторой строке записаны идентификаторы, разделённые произвольным количеством пробелов. При этом строка может начинаться и заканчиваться произвольным количеством пробелов. Назовём такую строку предложением.
Лексический анализ предложения заключается в выделении из него последовательности записанных в нём идентификаторов. В результате лексического анализа получается массив целых чисел, каждое из которых соответствует одному из идентификаторов. Целые числа назначаются идентификаторам произвольно, но так, чтобы разным идентификаторам соответствовали разные числа, а равным идентификаторам – одинаковые числа.

Пример.
Пусть дано предложение
alpha x1 beta alpha x1 y

Тогда на выходе лексического анализатора может получиться последовательность чисел

1 2 3 1 2 4

Здесь число 1 соответствует идентификатору alpha, число 2 – идентификатору x1, число 3 – идентификатору beta, а число 4 – идентификатору y.
Необходимо разработать функцию lex, выполняющую лексический анализ предложения:

func lex(sentence string, array AssocArray) []int {
    ...
}
В качестве первого параметра функция lex принимает предложение, а второй параметр задаёт ассоциативный массив, который должен быть использован внутри функции для хранения соответствия идентификаторов и целых чисел.
Ассоциативный массив, который можно передавать в функцию lex, должен реализовывать интерфейс AssocArray:

type AssocArray interface {
    Assign(s string, x int)
    Lookup(s string) (x int, exists bool)
}
Метод Assign добавляет в ассоциативный массив словарную пару.
Метод Lookup выполняет поиск словарной пары по ключу и возвращает два значения: x и exists. Если словарной пары с указанным ключом в массиве нет, то exists принимает значение false. В противном случае exists равен true, а x – связанное с ключом значение.
Составьте программу lex.go, демонстрирующую работоспособность функции lex. В качестве ассоциативных массивов для тестирования функции lex нужно использовать список с пропусками и АВЛ-дерево.
*/




// lex project main.go
package main

import (
    "fmt"
        "strings"
	"os"
	"rand"
)

type AssocArray interface {
	Assign(s string, x int)
	Lookup(s string) (x int, exists bool)
}

type SkipList struct {
	key string
	value int
	size int
	next []*SkipList
}

type AVL_Tree struct {
	k string
	v, balance int
	left, right, parent *AVL_Tree
}

type Tree struct {
	tree *AVL_Tree
}

func Panic() {
	fmt.Printf("panic\n");
	os.Exit(0)
}

func InitSkipList(m int) (*SkipList) {
	l := new(SkipList)
	l.size = m
	l.next = make([]*SkipList, m)

	for i := 0; i < l.size; i++ {
		l.next[i] = nil
	}

	return l
}

func (l *SkipList) Skip(k string) ([]*SkipList) {
	x := l
	p := make([]*SkipList, l.size)

	for i := l.size  - 1; i >= 0; i-- {
		for x.next[i] != nil && k < x.next[i].key {
			x = x.next[i]
		}
		p[i] = x
	}

	return p
}

func (l *SkipList) Lookup(s string) (x int, exist bool){
	p := l.Skip(s)
	X := p[0].Succ()

	if X == nil || X.key != s {
		return 0, false
	} else {
		return X.value, true
	}
	return
}

func (x *SkipList) Succ() (*SkipList) {
	return x.next[0]
}

func (l *SkipList) Assign(s string, x int) {
	p := l.Skip(s)

	if p[0].next[0] != nil && p[0].next[0].key == s {
		Panic()
	}

	X := new(SkipList)
	X.next = make([]*SkipList, l.size)
	X.value = x
	X.key = s

	r := rand.Int()*2

	var i int
	i = 0

	for (i < l.size) && (r % 2 == 0) {
		X.next[i] = p[i].next[i]
		p[i].next[i] = X
		i++
		r /= 2
	}
	for i < l.size {
		X.next[i] = nil
		i++
	}
}

func (t *Tree) ReplaceNode(x, y *AVL_Tree) {
	if x == t.tree {
		t.tree = y
	} else {
		p := x.parent
		if y != nil {
			y.parent = p
		}
		if p.left == x {
			p.left = y
		} else {
			p.right = y
		}
	}
}

func (t *Tree) RotateLeft(x *AVL_Tree) {
	y := x.right
	if y == nil {
		Panic()
	}
	t.ReplaceNode(x, y)
	b := y.left
	if b != nil {
		b.parent = x
	}
	x.right = b
	x.parent = y
	y.left = x

	x.balance--
	if y.balance > 0 {
		x.balance -= y.balance
	}

	y.balance--
	if x.balance < 0 {
		y.balance += x.balance
	}
}

func (t *Tree) RotateRight(x *AVL_Tree) {
	y := x.left
	if y == nil {
		Panic()
	}
	t.ReplaceNode(x, y)
	b := y.right
	if b != nil {
		b.parent = x
	}
	y.right = x
	x.parent = y
	x.left = b

	x.balance++
	if y.balance < 0 {
		x.balance -= y.balance
	}
	y.balance++
	if x.balance > 0 {
		y.balance += x.balance
	}

	return
}

func Descend(t *Tree, k string) *AVL_Tree {
	x := t.tree

	for x != nil && x.k != k {
		if k < x.k {
			x = x.left
		} else {
			x = x.right
		}
	}

	return x
}

func Insert(t *Tree, k string, v int) *AVL_Tree {
	y := new(AVL_Tree)
	y.k = k
	y.v = v
	y.parent = nil
	y.left = nil
	y.right = nil

	if t.tree == nil {
		t.tree = y
	} else {
		x := t.tree
		for {
			if x.k == k {
				Panic()
			}
			if k < x.k {
				if x.left == nil {
					x.left = y
					y.parent = x
					break
				}
				x = x.left
			} else {
				if x.right == nil {
					x.right = y
					y.parent = x
					break
				}
				x = x.right
			}
		}
	}
	return y
}

func (t *Tree) Assign(k string, v int) {
	a := Insert(t, k, v)
	a.balance = 0
	for {
		x := a.parent
		if x == nil {
			break
		}
		if a == x.left {
			x.balance--
			if x.balance == 0 {
				break
			}
			if x.balance == -2 {
				if a.balance == 1 {
					t.RotateLeft(a)
				}
				t.RotateRight(x)
				break
			}
		} else {
			x.balance++
			if x.balance == 0 {
				break
			}
			if x.balance == 2 {
				if a.balance == -1 {
					t.RotateRight(a)
				}
				t.RotateLeft(x)
				break
			}
		}
		a = x
	}
}

func (t *Tree) Lookup(s string) (int, bool) {
	x := Descend(t, s)
	if x == nil {
		return 0, false
	}
	return x.v, true
}

func analis(s []string, arr AssocArray) []int {
	ans := make([]int, 0, len(s))
	count := 0

	for i := 0; i < len(s); i++ {
		k, r := arr.Lookup(s[i])
		if r {
			ans = append(ans, k)
		} else {
			arr.Assign(s[i], count)
			ans = append(ans, count)
			count++
		}
	}

	return ans
}

func main() {
	example := "alpha x1 beta alpha x1 y"
	s := strings.Fields(example)
	var avl *Tree = new(Tree)
	avl_res := analis(s, avl)
	list := InitSkipList(len(s))
	list_res := analis(s, list)
	for _, x := range(avl_res) {
		fmt.Printf("%d ", x)
	}
	fmt.Printf("\n")
	for _, x := range(list_res) {
		fmt.Printf("%d ", x)
	}
	fmt.Printf("\n")
}
