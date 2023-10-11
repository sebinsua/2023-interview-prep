use std::io::stdin;
use std::collections::HashMap;

fn gauss_sum(n: u64) -> u64 {
    n * (n + 1) / 2
}

fn find_subsets(sequence: Vec<u64>, dp: HashMap<usize, bool>, target_sum: u64) -> (Vec<u64>, Vec<u64>) {
    // We know that it's technically possible to build a subset with the target sum.
    // We now need to find the two subsets of the `sequence` that sum to the target sum.
    let mut subset1: Vec<u64> = vec![];
    let mut subset2: Vec<u64> = vec![];

    let mut remaining_sum = target_sum;
    for num in sequence.iter().rev().copied() {
        // For each value in the sequence, we need to decide whether to put it in
        // `subset1` or `subset2`, however to do this we only need to consider decisions
        // with regards to `subset1` and can infer the decisions for `subset2` from this.
        // 
        // What we do is use `remaining_sum` to track the sum of the numbers in `subset1`
        // and add numbers from the `sequence` into this if we know that (1) they are less
        // than or equal to the `remaining_sum` (which ensures that we don't accidentally 
        // create a sequence that is greater than the `target_sum`), and (2) it's possible
        // to produce the next `remaining_sum` from the sequence having decreased it by 
        // this number (if we didn't do this we might end up adding a number from the 
        // sequence that results in a sequence with a sum that has no way of ever reaching
        // the `target_sum` with the remaining numbers found in the `sequence`).
        if num <= remaining_sum && *dp.get(&(remaining_sum as usize - num as usize)).unwrap_or(&false) {
            remaining_sum -= num;
            subset1.push(num);
        } else {
            subset2.push(num);
        }
    }

    (subset1, subset2)
}

fn dp_solution(n: u64) -> Option<(Vec<u64>, Vec<u64>)> {
    let total_sum = gauss_sum(n);

    // Test if the sum of the numbers from 1 to n is odd or even.
    // If it's odd, it will not be possible to break the sequence into two equal sets.
    if total_sum % 2 != 0 {
        return None;
    }
    
    let sequence = (1..=n).collect::<Vec<u64>>();
    let target_sum = total_sum as usize / 2;

    // The table `dp` stores a boolean describing whether a particular `sum` can be 
    // produced using the numbers in the sequence.
    // 
    // The base case is that you can always produce a sum of 0 by using no numbers
    // from the sequence.
    // 
    // It's initialised by iterating backwards from the target_sum down to an ascending
    // value from the sequence and on each iteration either (1) moving the boolean value 
    // from a previously calculated sum to the current sum when the current sum can be 
    // formed from this previous `sum` plus the current `num` in the sequence, or 
    // (2) once we know it's possible to compute a sum and `dp[sum]` is marked `true`
    // then keeping this true boolean state.
    let mut dp: HashMap<usize, bool> = HashMap::new();
    dp.insert(0, true);
    for num in sequence.iter().copied() {
        for sum in (num as usize..=target_sum).rev() {
            if *dp.get(&sum).unwrap_or(&false) {
                continue;
            }

            dp.insert(sum, *dp.get(&(sum - num as usize)).unwrap_or(&false));
        }
    }

    if !dp.get(&target_sum).unwrap_or(&false) {
        return None;
    }

    let (subset1, subset2) = find_subsets(
        sequence,
        dp,
        target_sum as u64
    );

    Some((subset1, subset2))
}

fn greedy_solution(n: u64) -> Option<(Vec<u64>, Vec<u64>)> {
    let total_sum = gauss_sum(n);

    // Test if the sum of the numbers from 1 to n is odd or even.
    // If it's odd, it will not be possible to break the sequence into two equal sets.
    if total_sum % 2 != 0 {
        return None;
    }

    let target_sum = total_sum / 2;
    
    let mut subset1 = Vec::new();
    let mut subset2 = Vec::new();

    let mut current_sum = 0;
    for num in (1..=n).rev() {
        // For each value in the sequence, we need to decide whether to put it in
        // `subset1` or `subset2`, however to do this we only need to consider decisions
        // with regards to `subset1` and can infer the decisions for `subset2` from this.
        // 
        // What we do is use `current_sum` to track the sum of the numbers in `subset1`
        // and add numbers from the `sequence` into this if we know that when they are 
        // added to the current sum they are less than or equal to the `target_sum`.
        if current_sum + num <= target_sum {
            current_sum += num;
            subset1.push(num);
        } else {
            subset2.push(num);
        }
    }

    Some((subset1, subset2))
}

fn main() {
    // Read input from `stdin` and parse it into a 64-bit unsigned integer.
    let n = match stdin().lines().next() {
        Some(Ok(line)) => 
            line
                .trim()
                .parse::<u64>()
                .expect("Invalid input. Please enter a valid positive integer for n."),
        _ => {
            println!("Error reading input.");
            std::process::exit(1);
        }
    };

    match greedy_solution(n) {
        Some((subset1, subset2)) => {
            println!("YES");

            println!("{}", subset1.len());
            println!("{}", subset1.iter().map(|&num| num.to_string()).collect::<Vec<String>>().join(" "));
        
            println!("{}", subset2.len());
            println!("{}", subset2.iter().map(|&num| num.to_string()).collect::<Vec<String>>().join(" "));
        },
        None => {
            println!("NO");
            return
        }
    }
}
