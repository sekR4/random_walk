package main

import "fmt"

func main()  {
    sum := 0
    for i := 0; i < 10; i++ { // ~ for i in range(10):
        fmt.Println(sum, "+", i, "=")
        // sum += i
        sum = sum + i
        fmt.Println(sum)
    }
    fmt.Println(sum)
}
