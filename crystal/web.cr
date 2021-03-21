# A very basic HTTP server
require "http/server"

server = HTTP::Server.new do |context|
  context.response.content_type = "text/plain"
  context.response.print "{context.request.path}!"
  puts context.request
end

puts "Listening on http://127.0.0.1:2077"
server.listen("0.0.0.0",2077)
