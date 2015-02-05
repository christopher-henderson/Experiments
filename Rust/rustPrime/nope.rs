extern crate core;
use core::num::ToPrimitive;

fn isPrime(x: i32, y: f64) -> bool {
    match x.to_f64() {
        Some(num) => num > y,
        None => false
    }
}

fn main() {
    let x = 5;
    let y = 7.0;
    isPrime(x,y);
}
