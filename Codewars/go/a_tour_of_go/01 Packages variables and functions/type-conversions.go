package main

import (
	"fmt"
	"math"
)

// func main() {
// 	var x, y int = 3, 4
// 	var f float64 = math.Sqrt(float64(x*x + y*y))
// 	var z uint = uint(f)
// 	fmt.Println(x, y, z)
// }

// func main() {
// 	var x, y int = 3, 4
// 	var f = math.Sqrt(float64(x*x + y*y))
// 	var z = uint(f)
// 	fmt.Println(x, y, z)
// }

func main()  {
    x, y := 3, 4
    // a := x*x + y*y
    f := math.Sqrt(float64(x*x + y*y))
    z := uint(f)
    fmt.Println(x, y, z, math.Sqrt(25))
}

// the func below does not work,
// since Sqrt requires float64 if its input
// is a calculation (x*x...) as well

// func main() {
// 	var x, y int = 3, 4
// 	var f float64 = math.Sqrt(x*x + y*y)
// 	var z uint = f
// 	fmt.Println(x, y, z)
// }
