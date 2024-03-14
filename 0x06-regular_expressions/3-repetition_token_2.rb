#!/usr/bin/env ruby

if ARGV.empty?
    puts "need argument"
else
    arg = ARGV[0]
    pattern = /(\Ahb)t{1,}(n\Z)/
    match_is = arg.match(pattern)
    if match_is
        puts "#{match_is}"
    end
end
