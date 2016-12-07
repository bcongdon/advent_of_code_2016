.data
PRINT_INT = 1
PRINT_STRING = 4
PRINT_CHAR = 11


.text

# print string #########################################################
#
# argument $a0: string to print
# returns       nothing

.globl print_string
print_string:
        li      $v0, PRINT_STRING       # print string command
        syscall                         # string is in $a0
        jr      $ra


# print int ##################################################
#
# argument $a0: number to print
# returns       nothing

.globl print_int
print_int:
        li      $v0, PRINT_INT  # load the syscall option for printing ints
        syscall                 # print the number
        
        jr      $ra             # return to the calling procedure

# print newline ########################################################
#
# no arguments
# returns       nothing

.globl print_newline
print_newline:
        li      $a0, '\n'       # print a newline
        li      $v0, PRINT_CHAR # load the syscall option for printing chars
        syscall                 # print the char
        jr      $ra

# print char and space #################################################
#
# argument $a0: character to print
# returns       nothing

.globl print_char
print_char:
        li      $v0, PRINT_CHAR # load the syscall option for printing chars
        syscall                 # print the number
        
        jr      $ra             # return to the calling procedure