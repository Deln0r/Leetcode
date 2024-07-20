/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func countPairs(root *TreeNode, distance int) int {
	re := 0
	_ = Count(root, &re, distance)
	return re
}

func Count(root *TreeNode, result *int, d int) map[int]int {
	if root == nil {
		return make(map[int]int)
	}
	re := make(map[int]int)
	if root.Left == nil && root.Right == nil {
		re[1] = 1
		return re
	}
	l := Count(root.Left, result, d)
	r := Count(root.Right, result, d)

	if len(l) == 0 {
		for i, v := range r {
			re[i+1] = v
		}
		return re
	}

	if len(r) == 0 {
		for i, v := range l {
			re[i+1] = v
		}
		return re
	}
	// fmt.Println(l, r)

	// fmt.Println("root: ", root.Val)

	for i, v := range l {
		if i+1 < d {
			re[i+1] += v
		}
	}

	for i, v := range r {
		if i+1 < d {
			re[i+1] += v
		}
	}

	for i, v := range l {
		if i > d {
			continue
		}
		for ii, vv := range r {
			if ii > d {
				continue
			}
			if i+ii > d {
				continue
			}
			// fmt.Println(i, ii, l, r, *result, v, vv)
			if i+ii <= d {
				*result += (v * vv)
			}
		}
	}
	return re
}