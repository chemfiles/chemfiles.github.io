using Chemfiles

file = Trajectory("filename.xyz")
frame = read(file)

println("There are $(size(frame)) atoms in the frame")
pos = positions(frame);

# Do awesome science here with the positions

if has_velocities(frame)
    vel = velocities(frame)

    # If the file contains information about the
    # velocities, you will find them here.
end
