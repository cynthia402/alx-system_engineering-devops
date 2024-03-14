#!/usr/bin/env ruby

if ARGV.empty?
    puts "required 1 argument, 'phone number'"
else
    arg = ARGV[0]
    pattern = /^[0-9]{10}$/
    match_is = arg.match(pattern)
    if match_is
        puts "#{match_is}"
    end
end
