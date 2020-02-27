use chemfiles::Trajectory;

fn main() -> Result<(), Box<std::error::Error>> {
    let file = Trajectory("filename.xyz", "r")?;

    let frame = file.read()?;
    println!("There are {} atoms in the frame",  frame.size());
    let positions = frame.positions();

    // Do awesome science here with the positions

    if frame.has_velocities() {
        let velocities = frame.velocities();

        // If the file contains information about the
        // velocities, you will find them here.
    }

    return OK(());
}
