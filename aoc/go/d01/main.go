package main

import (
	"fmt"
	"io/ioutil"
	"path"
	"runtime"
	"sort"
	"strconv"
	"strings"
)

func sum(array []int) int {
	result := 0
	for _, v := range array {
		result += v
	}
	return result
}

func max(array []int) int {
	result := 0
	for _, v := range array {
		if v > result {
			result = v
		}
	}
	return result
}

func top(array []int, count int) []int {
	sort.Slice(array, func(i, j int) bool {
		return array[i] > array[j]
	})

	return array[:count]
}

func readFile(relativePath string) string {
	_, filename, _, ok := runtime.Caller(0)
	if !ok {
		panic("Could not find caller of this file")
	}

	absolutePath := path.Join(path.Dir(filename), relativePath)
	content, err := ioutil.ReadFile(absolutePath)

	if err != nil {
		panic(err)
	}

	return string(content)
}

func strSliceToIntSlice(slice []string) []int {
	var result []int
	for _, s := range slice {
		s_int, err := strconv.Atoi(s)
		if err != nil {
			panic(err)
		}

		result = append(result, s_int)
	}
	return result
}

func getCaloriesPerElf(input []string) []int {
	var elvesCalories []int

	for _, e := range input {
		calories := strings.Split(e, "\n")
		caloriesInt := strSliceToIntSlice(calories)
		elvesCalories = append(elvesCalories, sum(caloriesInt))
	}
	return elvesCalories
}

func puzzleOne(input []string) {
	elvesCalories := getCaloriesPerElf(input)

	topCalories := max(elvesCalories)

	fmt.Println(topCalories)
}

func puzzleTwo(input []string) {
	elvesCalories := getCaloriesPerElf(input)

	topThreeCalories := top(elvesCalories, 3)
	totalCalories := sum(topThreeCalories)

	fmt.Println(totalCalories)
}

func main() {
	content := readFile("../../data/2022-1.txt")
	elvesInput := strings.Split(content, "\n\n")
	puzzleOne(elvesInput)
	puzzleTwo(elvesInput)
}
