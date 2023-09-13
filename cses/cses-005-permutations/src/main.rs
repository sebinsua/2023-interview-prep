use std::io::{stdin, BufRead};
use std::process;

fn permutations(n: &u64) -> String  {
    let mut str = String::new();

    for i in (2..=*n).step_by(2) {
        str += format!("{} ", i).as_str();
    }

    for i in (1..=*n).step_by(2) {
        str += format!("{} ", i).as_str();
    }

    str
}

static MAX_N: u64 = 10u64.pow(6);

fn main() {
    let n = stdin()
        .lock()
        .lines()
        .next()
        .expect("Failed to read the line from the input stream")
        .expect("No input received for the line")
        .trim()
        .parse::<u64>()
        .expect("Failed to parse the line as u64");
    
    if n > MAX_N {
        process::exit(1);
    }
    
    if n == 3 || n == 2 {
        println!("NO SOLUTION");
        process::exit(0);
    }

    println!("{}", permutations(&n));

    process::exit(0);
}