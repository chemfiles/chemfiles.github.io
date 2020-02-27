from chemfiles import Trajectory

file = Trajectory("filename.xyz")
frame = file.read()

print("There are {} atoms in the frame".format(len(frame.atoms)))
positions = frame.positions

# Do awesome science here with the positions

if frame.has_velocities():
    velocities = frame.velocities
    # If the file contains information about the
    # velocities, you will find them here.
