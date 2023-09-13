use std::cmp::Ordering;
use std::io::{stdin, BufRead};
use std::process;

static MAX_LINES: u64 = 10u64.pow(5);

fn layer_range(layer: u64) -> (u64, u64) {
    let low = (layer - 1).pow(2) + 1;
    let high = layer.pow(2);
    (low, high)
}

fn number_spiral(y: u64, x: u64) -> u64 {
    if y == 1 && x == 1 {
        return 1;
    }

    let layer = std::cmp::max(y, x);
    let (low, high) = layer_range(layer);

    if layer % 2 == 0 {
        match y.cmp(&x) {
            Ordering::Less => low + (y - 1),
            Ordering::Equal => low + (y - 1),
            Ordering::Greater => high - (x - 1),
        }
    } else {
        match y.cmp(&x) {
            Ordering::Less => high - (y - 1),
            Ordering::Equal => high - (y - 1),
            Ordering::Greater => low + (x - 1),
        }
    }
}

fn main() {
    let number_of_tests = stdin()
        .lock()
        .lines()
        .next()
        .expect("Failed to read the first line from the input stream")
        .expect("No input received for the first line")
        .trim()
        .parse::<u64>()
        .expect("Failed to parse the first line as u64");
    
    if number_of_tests > MAX_LINES {
        process::exit(1);
    }
    
    let mut current_line = 1;
    for line in stdin().lock().lines() {
        if current_line > number_of_tests {
            break;
        }

        let l = line.unwrap();
        let (y, x): (u64, u64) = {
            let mut words = l.trim().split_whitespace().map(|w| w.parse().unwrap());
            (words.next().unwrap(), words.next().unwrap())
        };

        println!("{}", number_spiral(y, x));

        current_line += 1;
    }

    process::exit(0);
}