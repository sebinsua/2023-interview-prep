use std::io::{stdin, BufRead};
use std::process;

static MAX_LEN: usize = 1 * 10usize.pow(6);

fn repetitions(dna_sequence: &Vec<char>) -> usize {
    let mut current_len = 1;
    let mut max = 1;
    let mut previous = dna_sequence[0];
    for i in 1..dna_sequence.len() {
        if dna_sequence[i] == previous {
            current_len += 1;
        } else {
            current_len = 1;
        }

        if current_len > max {
            max = current_len;
        }

        previous = dna_sequence[i];
    }

    max
}

fn main() {
    let dna_sequence: Vec<char> = stdin()
        .lock()
        .lines()
        .next()
        .expect("Failed to read the line from the input stream")
        .expect("No input received for the line")
        .trim()
        .chars()
        .collect();
    
    if dna_sequence.len() < 1 {
        process::exit(1);
    } 
    if dna_sequence.len() > MAX_LEN {
        process::exit(1);
    }

    let repetitions = repetitions(&dna_sequence);

    println!("{}", repetitions);

    process::exit(0);
}