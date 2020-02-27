program example
    use chemfiles
    use iso_fortran_env, only: real64
    implicit none

    type(chfl_trajectory) :: file
    type(chfl_frame) :: frame
    real(real64), dimension(:, :), pointer :: positions, velocities

    call file%open("filename.xyz", "r", status=status)
    if (status /= 0) stop

    call frame%init()
    call file%read(frame, status=status)
    if (status /= 0) stop

    positions => frame%positions()
    write(*, *) "There are", size(positions, 2), "atoms in the frame"

    ! Do awesome science here with the positions

    if (frame%has_velocities()) then
        velocities => frame%velocities()

        ! If the file contains information about the
        ! velocities, you will find them here.
    end if
end program
