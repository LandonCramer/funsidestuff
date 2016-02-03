root = "/home/phil/funsidestuff/stocks"
day = `date | awk '{print $2"_"$3"_"$6}'`.chomp

stocks = `ls #{root}/DOW/stocks`.split(/\n/)

if(!stocks.empty?)
  stocks.each {|stock|
    intraminute_values = `cat #{root}/DOW/stocks/#{stock}/#{day}/ery1min.data | awk '{print $2}'`.split(/\n/).compact.reject{ |e| e.empty? }

    total = 0.0
    low = intraminute_values[0].to_f
    high = intraminute_values[0].to_f
    open = intraminute_values[0].to_f
    close = intraminute_values[intraminute_values.size - 1].to_f
    change = "%" + (((close - open) / open) * 100).round(2).to_s
    intraminute_values.each { |value|
      if(value.to_f < low)
        low = value.to_f
      end
      if(value.to_f > high)
        high = value.to_f
      end
      total += value.to_f
    }
    average = (total/intraminute_values.size).round(2)
    puts "#{stock.center(8)} Average = #{average.to_s.center(8)}   Low = #{low.to_s.center(8)}   High = #{high.to_s.center(8)}"
    puts "         Open = #{open.to_s.center(8)}     Close = #{close.to_s.center(8)}  Change = #{change.to_s.center(8)}"
    puts
  }
end
