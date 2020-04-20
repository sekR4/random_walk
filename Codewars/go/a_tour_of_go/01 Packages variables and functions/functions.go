// https://tour.golang.org/basics/4

package main

import "fmt"

// func add(x int, y int) int {
// 	return x + y
// 	// u have to define data types of what goes in: add(x int, y int)
// 	// and what goes out: add(...) int
// }

func add(x, y int) int {
	return x + y
    // if both input variables have the same type
    // i can omit one except the last
}

func main() {
	fmt.Println(add(17, 4))
}
