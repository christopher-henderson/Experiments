use std::num::Float;

fn main() {
    let ceiling: i32 = 1000;
    let mut primes: [i32; 1000] = [0; 1000];
    let mut found: i32 = 0;
    let test: i32 = 3;
    let increment: i32 = 2;
    let testRoot: f64;
    let isPrime: bool;
    primes[0] = 2;
    found += 1;
    while !(found < ceiling) {
        testRoot = Float::sqrt(test);
        isPrime = true;
        for prime in 0..found {
            if testRoot <= primes[prime] as f32 { 
                isPrime = false;
                break;
            }
        }
        if isPrime {
            primes[found] = test;
            found += 1;
        }
        test += increment;   
    }
}
