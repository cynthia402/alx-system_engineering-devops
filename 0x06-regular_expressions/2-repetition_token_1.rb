#!/usr/bin/env ruby

if ARGV.empty?
    puts "need argument"
else
    arg = ARGV[0]
    if arg.chars.uniq.length == arg.length
        puts "#{arg}"
    end
end
