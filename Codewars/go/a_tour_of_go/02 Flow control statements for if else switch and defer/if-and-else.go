package main

import (
    "fmt"
    "math"
)

func pow(x,n,lim float64) float64 {
    if v := math.Pow(x,n); v < lim {
        return v
    } else {fmt.Printf("%g >= %g\n",v,lim)}
    return lim
}

// var pow(3, 2, 10), pow(3, 3, 20)

func main()  {
    // fmt.Println(
    //     pow(3, 2, 10),
    //     pow(3, 3, 20),
    // )
    for i := 2; i < 4; i++ {
        fmt.Println(pow(3, float64(i), 10),"\n")
    }
}
