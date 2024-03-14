#!/usr/bin/env ruby

if ARGV.empty?
    puts "required argument"
else
   arg = ARGV[0]
   pattern = /(School)/
   match_is = arg.scan(pattern)
   if match_is
       puts "#{match_is.join("")}"
   end
end
