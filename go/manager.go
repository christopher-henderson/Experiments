package main

import (
	"fmt"
	"math/rand"
	"sync"
	"time"
)

type GetterPutter interface {
	Get(string) int
	Put(string, int)
}

type Pair struct {
	Key   string
	Value int
}

type ChanManager struct {
	put       chan Pair
	getKey    chan string
	sendValue chan int
	db        map[string]int
}

func (m *ChanManager) Serve() {
	for {
		select {
		case key := <-m.getKey:
			m.sendValue <- m.db[key]
		case pair := <-m.put:
			m.db[pair.Key] = pair.Value
		}
	}
}

func (m *ChanManager) Get(key string) int {
	m.getKey <- key
	return <-m.sendValue
}

func (m *ChanManager) Put(key string, value int) {
	m.put <- Pair{key, value}
}

func NewChanmanager() *ChanManager {
	m := &ChanManager{make(chan Pair), make(chan string), make(chan int), make(map[string]int)}
	go m.Serve()
	return m
}

type MutexManager struct {
	sync.RWMutex
	db map[string]int
}

func (m *MutexManager) Get(key string) int {
	m.RLock()
	defer m.RUnlock()
	return m.db[key]
}

func (m *MutexManager) Put(key string, value int) {
	m.Lock()
	defer m.Unlock()
	m.db[key] = value
}

func testManager(m GetterPutter) {
	s := sync.WaitGroup{}
	start := time.Now()
	for i := 0; i < 10000; i++ {
		go thrash(m, s)
	}
	s.Wait()
	fmt.Println(time.Now().Sub(start))
}

func thrash(m GetterPutter, s sync.WaitGroup) {
	s.Add(1)
	defer s.Done()
	for i := 0; i < 100000; i++ {
		action := rand.Int() % 2
		key := string(rand.Int() % 100)
		switch action {
		case 0:
			m.Put(key, i)
		case 1:
			m.Get(key)
		}
	}
}

func main() {
	// fmt.Println(string(10000))
	rand.Seed(time.Now().Unix())
	// fmt.Println("ChanManager")
	m := NewChanmanager()
	// mm := &MutexManager{sync.RWMutex{}, make(map[string]int)}
	// testManager(mm)
	// time.Sleep(time.Second * 5)
	// for i := 0; i < 5; i++ {
	testManager(m)
	// }
	// fmt.Println("MutexManager")
	// for i := 0; i < 5; i++ {

	// }
}
