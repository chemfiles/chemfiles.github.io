#include <stdio.h>
#include <stdlib.h>
#include <chemfiles.h>

int main() {
    CHFL_TRAJECTORY* file = chfl_trajectory_open("filename.xyz", 'r');
    CHFL_FRAME* frame = chfl_frame();

    chfl_trajectory_read(file, frame);

    uint64_t natoms = 0;
    chfl_vector3d* positions = NULL;
    chfl_frame_positions(frame, &positions, &natoms);

    printf("There are %d atoms in the frame", natoms);

    // Do awesome science here with the positions

    bool has_velocities = false;
    chfl_frame_has_velocities(frame, &has_velocities);

    if (has_velocities) {
        chfl_vector3d* velocities = NULL;
        chfl_frame_velocities(frame, &velocities, &natoms);

        // If the file contains information about the
        // velocities, you will find them here.
    }

    chfl_trajectory_close(file);
    chfl_free(frame);
    return EXIT_SUCCESS;
}
