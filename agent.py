import os
from google import genai
from google.genai import types
from dotenv import load_dotenv
load_dotenv()

grounding_tool = types.Tool(
    google_search=types.GoogleSearch()
)

def chat_agent(inputs):
    client = genai.Client(
        api_key=os.environ.get("GEMINI_API_KEY"),
    )

    model = "gemini-2.5-flash"
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text=f"""{inputs}"""),
            ],
        ),
    ]
    generate_content_config = types.GenerateContentConfig(
        thinking_config = types.ThinkingConfig(
            thinking_budget=-1,
        ),
        response_mime_type="text/plain",
        system_instruction=[
            types.Part.from_text(text="""
            তুমি একজন বুদ্ধিমান, সদা-সচেতন ও আপডেটেড ভার্চুয়াল সহকারী। তোমার প্রধান কাজ হলো ব্যবহারকারীকে শুধু **বাংলা ভাষায়** তথ্য, সহায়তা ও পরামর্শ দেওয়া। 

            ✅ সবসময় আপডেটেড তথ্য দাও — প্রয়োজনে গুগল সার্চ ব্যবহার করে তা যাচাই করে নাও।

            ✅ প্রতিটি প্রশ্নের উত্তর দাও **সংক্ষেপে, প্রাসঙ্গিকভাবে এবং শুধুই বাংলায়**।

            ✅ তুমি বর্তমানে **কলকাতাকেন্দ্রিক** — যেকোনো প্রশ্নে প্রথমে ব্যবহারকারীর স্থানীয় প্রেক্ষাপট, সংস্কৃতি, ভাষা ও প্রয়োজন বিবেচনা করো।

            ✅ ইনপুট হিসেবে তুমি **টেক্সট / অডিও / ছবি** বুঝতে পারো এবং **আউটপুট টেক্সট / অডিও** দিতে পারো।

            ✅ ভাষা হবে সহজ, কথ্য, স্থানীয় — যেন যেকোনো বয়সের মানুষ বুঝতে পারে।

            🚫 ইংরেজি ব্যবহার করো না, ব্যতিক্রম কেবল নির্দিষ্ট নাম বা প্রযুক্তিগত শব্দ থাকলে।

            🎯 লক্ষ্য: বাংলা ভাষাভাষী, বিশেষত কলকাতা অঞ্চলের মানুষের জন্য সবচেয়ে উপযোগী, নির্ভরযোগ্য এবং তাৎক্ষণিক তথ্য সহায়তা দেওয়া।


                                 """),
        ],
        tools=[
            grounding_tool,
        ]
    )

    # for chunk in client.models.generate_content_stream(
    #     model=model,
    #     contents=contents,
    #     config=generate_content_config,
    # ):
    #     yield chunk.text
    response = client.models.generate_content(
        model=model,
        contents=contents,
        config=generate_content_config,
    )
    return response.text


if __name__ == "__main__":
    res = chat_agent("What is the capital of India?")
    print(res)
