package main

import ("fmt")

func main()  {
    original := []string {"A","B","C"}
    result := make([][]string, 0)

    for _, w := range original{ 
        combination(original, []string {w}, &result) 
    }

    print(result)
}

func combination(original []string, point []string, result *[][]string)  {
    wordWithouthPoint := filter(original, func(v string) bool {
            return !contains(point, v)
        })
    
    for _, w := range wordWithouthPoint{
        clonePoint := point
        clonePoint = append(clonePoint, w)  

        *result = append(*result, clonePoint)
        combination(original, clonePoint, result)
    }     
}  

func print(result [][]string){
    for _, each := range result{
        fmt.Printf("%v", each)
        fmt.Println()
    }
}

func filter(original []string, f func(s string) bool) []string{
    filtered := make([]string,0)

    for _, each := range original{
        if f(each){
            filtered = append(filtered, each)
        }
    }     
    return filtered
}

func contains(list []string, s string) bool{
     for _,each := range list{
        if each == s {
            return true
        }
    }
    return false
}