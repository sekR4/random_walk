// https://tour.golang.org/basics/1

package main

import (
	"fmt"
	"math/rand"
	// if i comment math/rand but use rand.Intn,
	// math/rand will added to imports automatically
)

func main() {
	fmt.Println("My favorite number is", rand.Intn(10))
	// interestingly the number stays constant
	// linter also shows an error because
	// i define main() in another script, too
}
