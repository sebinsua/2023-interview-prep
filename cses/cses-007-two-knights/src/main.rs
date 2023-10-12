use std::io::stdin;

fn total_piece_configurations(n: u64) -> u64 {
    // In order to compute the total number of chess piece configurations,
    // for a given n x n chess board, we have to consider the number of
    // squares available when we place both chess pieces onto the board.
    // 
    // For example:
    // 
    // First choice: `n * n` squares are available.
    //
    // Second choice: `(n * n) - 1` squares are available as one square is occupied
    //                by the first chess piece.
    //
    // We then multiply these together (e.g. `(n * n) * ((n * n) - 1)`) to get the
    // total number of configurations for the first two chess pieces. However,
    // because we don't consider the two pieces uniquely (e.g. both knights are
    // indistinguishable), we have to divide by 2 to get the correct number of
    // chess piece configurations.
    //
    // This is actually a more efficient way of computing the "binomial coefficient"
    // (n choose k) for k = 2, which is normally written as:
    //
    // binomial(n, k) = factorial(n) / (factorial(k) * factorial(n - k))
    //
    // See: http://cses.fi/book/book.pdf#page=218
    //
    // If we wanted to compute the total number of chess piece configurations for
    // k = 3, we would have to compute:
    //
    // (((n * n) - 0) * ((n * n) - 1) * ((n * n) - 2))) / (1 * 2 * 3)
    ((n * n) * ((n * n) - 1)) / 2
}

fn attacking_knight_configurations(n: u64) -> u64 {
    // When a chessboard is smaller than 3x3, it's not
    // possible for two knight pieces to attack each other.
    if n < 3 {
        return 0;
    }

    // In order to compute the total number of attacking knight configurations,
    // for a given n x n chess board, we have to consider the number of 2x3 or
    // 3x2 rectangles that can be placed onto the board, as we can base the
    // number of attacking knight configurations on these rectangles (since a 
    // knight moves in an L-shape, 1 square in one direction and 2 squares in 
    // another direction).
    //
    // If you think about a 2x3 rectangle (y*x), along the y-axis you can only
    // place the rectangle in n - 1 positions, while along the x-axis, you can
    // only place the rectangle in n - 2 positions. Therefore the total number
    // of ways a 2x3 rectangle can be placed on a board is `(n - 1) * (n - 2)`.
    // 
    // However, we multiply this by 4, because:
    // 1. For each rectangle, we have to consider its two orientations (e.g. 2x3
    //    and 3x2).
    // 2. Within each rectangle a knight can attack another knight when they are
    //    on opposite corners of the rectangle. This would suggest that there are
    //    4 ways a knight can attack another knight within a rectangle, but we 
    //    have to divide by 2 to account for the fact that we don't consider the
    //    two knights uniquely (e.g. both knights are indistinguishable).
    // 
    // To be clear, the real equation is:
    // number_of_orientations_of_a_rectangle * (number_of_attacking_knight_positions_in_a_rectangle / factor_to_account_for_indistinguishable_knights) * number_of_ways_rectangles_can_be_placed
    // 2 * ((4 / 2) * ((n - 1) * (n - 2)))
    //
    // Note: if we needed to deal with k>=3 knights, the approach would have to get
    //       significantly more complicated, as we would have to consider different
    //       attack shapes and orientations, on top of the factor to account for
    //       indistinguishable knights being updated to `k!`.
    4 * (n - 1) * (n - 2)
}

fn safe_knight_configurations(n: u64) -> u64 {
    // The number of safe knight configurations is the total number of 
    // chess piece configurations minus the number of attacking knight 
    // configurations.
    total_piece_configurations(n) - attacking_knight_configurations(n)
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

    for i in 1..=n {
        // Print the number of safe configurations that two knight pieces
        // can be placed on within an n x n chessboard.
        println!("{}", safe_knight_configurations(i));
    }
}
