use std::io::{stdin, BufRead};
use std::process;


fn increasing_array(_ns: &Vec<u64>) -> u64 {
    let mut ns = _ns.clone();

    let mut number_of_moves = 0;
    for i in 1..ns.len() {
        if ns[i] < ns[i - 1] {
            number_of_moves += ns[i - 1] - ns[i];
            ns[i] = ns[i - 1];
        }
    }

    number_of_moves
}

static MAX_N: u64 = 2 * 10u64.pow(5);
static MAX_LEN: usize = 10usize.pow(9);

fn main() {
    let max_ns_len = stdin()
        .lock()
        .lines()
        .next()
        .expect("Failed to read the first line from the input stream")
        .expect("No input received for the first line")
        .trim()
        .parse::<u64>()
        .expect("Failed to parse the first line as u64");
    
    if max_ns_len > MAX_N {
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
    
    if ns.len() > MAX_LEN || ns.len() > max_ns_len as usize {
        process::exit(1);
    }

    println!("{}", increasing_array(&ns));

    process::exit(0);
}