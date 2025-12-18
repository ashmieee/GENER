from google import genai
client = genai.Client(api_key="AIzaSyC_Mr95SLQ61qdbAizCCnWIfzkhdmbtYi4")
message =[]
while True:

  user_input = input("you ")
  message.append("user" + user_input)

  response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=message,
  )

  print("AI:" + response.text)

