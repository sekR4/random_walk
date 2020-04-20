// https://tour.golang.org/basics/8

package main

import "fmt"

// package level
var c, python, java, maus, irgendwas bool

func main()  {
    // function level
    var i int
    fmt.Println(i, c, python, maus, irgendwas)
}

// var declares lists on different levels
