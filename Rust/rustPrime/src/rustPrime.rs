    /*
    @author Christopher Henderson (chris@chenderson.org)

    This is interesting.

    A Box of sufficient size will overflow the stack whereas a vector will not.
    Research shows that the contents of Boxes are first allocated to the stack
    and THEN copied to the heap. This is surprising and seems self-defeating.

    I would much rather use an array here than a vector, but it seems to be
    the only choice at the moment.

    This Rust is several times slower at finding the 1 millionth prime number
    than my Cython version of this naive algorithm. I'm thinking it may be
    due to the use of the vector over an array, but I am not sure at this time.
    */

use std::num::Float; // Brought in for its square root method.

const CEILING: usize = 1000000;

fn main() {
    let mut primes: Vec<u32> = std::iter::repeat(0).take(CEILING).collect();
    //let mut primes: Box<[u32;SIZE]> = Box::new([0; SIZE]); // Stack overflow for large values of SIZE
    let mut found: usize = 0;
    let mut test: u32 = 3;
    let increment: u32 = 2;
    let mut test_root: f64;
    let mut is_prime: bool;
    primes[found] = 2;
    found += 1;
    while found < CEILING {
        test_root = (test as f64).sqrt();
        is_prime = true;
        for &prime in primes.iter() {
            if (prime as f64) > test_root { 
                break;
            }
            if test % prime == 0 {
                is_prime = false;
                break;
            }
        }
        if is_prime {
            primes[found] = test;
            found += 1;
        }
        test += increment;   
    }
    println!("The {}th prime number is {}", CEILING, primes[CEILING-1]);   
}
