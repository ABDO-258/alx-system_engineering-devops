#   manifest that kills a process named killmenow.
exec {'kill_me_now':
    command   => 'pkill killmenow',
}
