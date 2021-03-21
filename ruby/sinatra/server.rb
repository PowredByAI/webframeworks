require 'sinatra'
set :bind, '0.0.0.0'
set :port, 3030

get '/' do
  'Hello world!'
end