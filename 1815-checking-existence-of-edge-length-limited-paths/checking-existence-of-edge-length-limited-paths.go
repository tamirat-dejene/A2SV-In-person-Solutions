type uf struct {
	root, size []int
}

func NewUF(n int) *uf {
	var root = make([]int, n)
	var size = make([]int, n)

	for i := range n {
		root[i] = i
		size[i] = 1
	}

	return &uf{
		root: root,
		size: size,
	}
}

func (u *uf) union(nd1, nd2 int) bool {
	r1 := u.find(nd1)
	r2 := u.find(nd2)

	if r1 == r2 {
		return false
	}

	if u.size[r1] < u.size[r2] {
		r1, r2 = r2, r1
	}

	u.root[r2] = u.root[r1]
	u.size[r1] += u.size[r2]

	return true
}

func (u *uf) find(nd int) int {
	if nd != u.root[nd] {
		u.root[nd] = u.find(u.root[nd])
	}
	return u.root[nd]
}

func (u *uf) connected(nd1, nd2 int) bool {
	return u.find(nd1) == u.find(nd2)
}

func distanceLimitedPathsExist(n int, edgeList [][]int, queries [][]int) []bool {
	var qrs = make([][]int, len(queries))
	for i, qr := range queries {
		p, q, l := qr[0], qr[1], qr[2]
		qrs[i] = []int{l, p, q, i}
	}

	sort.Slice(qrs, func(i, j int) bool {
		return qrs[i][0] < qrs[j][0]
	})

	sort.Slice(edgeList, func(i, j int) bool {
		return edgeList[i][2] < edgeList[j][2]
	})

	fmt.Println(edgeList)
	fmt.Println(qrs)

	dsu := NewUF(n)
	ans := make([]bool, len(queries))
	ei := 0

	for _, qr := range qrs {
		l, p, q, i := qr[0], qr[1], qr[2], qr[3]

		for ei < len(edgeList) && edgeList[ei][2] < l {
			a, b := edgeList[ei][0], edgeList[ei][1]

			dsu.union(a, b)
			ei += 1
		}

		ans[i] = dsu.connected(p, q)
	}

	return ans
}