// https://tour.golang.org/basics/7

package main

import "fmt"

func split(sum int) (x,y int)  {
    x = sum * 4 / 9     // since it's an integer, x is 7 in our example (sum=17)
    y = sum - x
    return              // 'naked' return of objects declared
}

func main()  {
    fmt.Println(split(17))
}
