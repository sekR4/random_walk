package main

import "fmt"

func main() {
	sum := 1
	for ; sum < 1000; {
		fmt.Println(sum)
		sum = sum + sum
	}
	fmt.Println(sum)
}

// ok... It's not complicated, but much more convenient in python ;)
// s = 1
// while s < 1000:
//     s = s + s
//     print(s)
