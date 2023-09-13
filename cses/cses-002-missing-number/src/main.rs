use std::io::{stdin, BufRead};
use std::process;

fn gauss_sum(n: &u64) -> u64 {
    (n * (n + 1)) / 2
}

fn missing_number(max_n: &u64, ns: &Vec<u64>) -> u64 {
    let expected_sum = gauss_sum(max_n);
    let actual_sum = ns.iter().fold(0, |acc, x| acc + x);
    expected_sum - actual_sum
}

static MAX_N: u64 = 2 * 10u64.pow(5);

fn main() {
    let max_n = stdin()
        .lock()
        .lines()
        .next()
        .expect("Failed to read the first line from the input stream")
        .expect("No input received for the first line")
        .trim()
        .parse::<u64>()
        .expect("Failed to parse the first line as u64");
    
    if max_n > MAX_N {
        process::exit(1);
    }
    
    let ns: Vec<u64> = stdin()
        .lock()
        .lines()
        .next()
        .expect("Failed to read the second line from the input stream")
        .expect("No input received for the second line")
        .trim()
        .split_whitespace().map(|s| s.parse().expect("Failed to parse an element from the second line as u64")).collect();
    
    if ns.len() != (max_n as usize) - 1 {
        process::exit(1);
    }

    println!("{}", missing_number(&max_n, &ns));

    process::exit(0);
}