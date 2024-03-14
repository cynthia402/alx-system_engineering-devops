#!/usr/bin/env ruby

if ARGV.empty?
    puts "missing one argument"
else
    arg = ARGV[0]
    pattern = /[A-Z]+/
    match_is = arg.scan(pattern)
    if match_is
        puts "#{match_is.join("")}"
    end
end
