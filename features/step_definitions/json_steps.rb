Given /^I embed a screenshot/ do
  File.open("screenshot.png", "w") { |file| file << "foo" }
  embed "screenshot.png", "image/png"
end

Given /^I print from step definition/ do
  puts "from step definition"
end

Given /^I embed data directly/ do
  data = "YWJj"
  embed data, "mime-type;base64"
end