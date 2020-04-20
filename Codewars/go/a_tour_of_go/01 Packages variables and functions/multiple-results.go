// https://tour.golang.org/basics/6

package main

import "fmt"

func swap(x, y string) (string, string) {
    return y, x
    // here we're returning to variables
    // so we also need to define two types
}

func main()  {
    a, b := swap("hello", "world")
    fmt.Println(a,b)
}
