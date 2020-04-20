package main

import (
	"fmt"
)

func Sqrt(x float64) (float64,float64) {
    z := float64(x)
    for i := 0; i < 20; i++ {
        z -= (z*z - x) / (2*z)
        // z = z - (z*z - x) / (2*z)
        // z = z - ((z/2) - (x/(2*z)))
        // also see:
        // https://www.wikiwand.com/en/Newton%27s_method
    }
    return z, z*z
    // for comparison i've added z^2 to see
    // if we're really close to x
}

func main() {
	fmt.Println(Sqrt(3))
}
