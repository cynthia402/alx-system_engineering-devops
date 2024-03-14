#!/usr/bin/env ruby
#Your script should output: [SENDER],[RECEIVER],[FLAGS]
#The sender phone number or name (including country code if present)
#The receiver phone number or name (including country code if present)
#The flags that were used

if ARGV.empty?
    puts 'one argument is missed'
else
    address = ARGV[0].split(" ")[14].split(':')[1].split("]")[0]
    phone_no = ARGV[0].split(" ")[15].split(":")[1].split("]")[0]
    flag = ARGV[0].split(" ")[16].split("flags:")[1].split("]")[0]
    puts "#{address},#{phone_no},#{flag}"

end
