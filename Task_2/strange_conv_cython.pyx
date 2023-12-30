cimport numpy as cnp
cimport cython

@cython.boundscheck(False)
@cython.wraparound(False)
cpdef double strange_conv_cython(cnp.ndarray a):
    cdef int x = a.shape[0]
    cdef int y = a.shape[1]

    cdef double t = 1.0
    cdef double c
    for y in range(y - 5):
        for x in range(x - 3):
            c = 1.5 * a[y+1, x+2] - a[y+5, x+3] * a[y, x] + 0.2 * a[y+4, x]
            t = 0.2 * t + 0.8 * c
    return t
