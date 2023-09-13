use std::io::{stdin, BufRead};
use std::process;

fn weird_algorithm(n: &mut u64) {
    print!("{}", *n);
    while *n > 1 {
        if *n % 2 == 0 {
            *n /= 2;
        } else {
            *n = 3 * *n + 1;
        }
        print!(" {}", *n);
    }
}

fn main() {
    for line in stdin().lock().lines() {
        let mut n = line.unwrap().trim().parse::<u64>().expect("Failed to parse input as u64");
        
        weird_algorithm(&mut n);

        process::exit(0);
    }
    process::exit(1);
}
