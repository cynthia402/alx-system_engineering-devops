#!/usr/bin/env ruby
if ARGV.empty?
    puts "provide one argument"
else
	arg = ARGV[0]
	pattern = /(\Ahb)(t{2,5})(n\Z)/
	match_is = arg.match(pattern)
	if match_is
	    puts "#{match_is}"
	end

end
