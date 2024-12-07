import re
import random

class ShopBot:
    def __init__(self):
        self.greetings = ['Hello!', 'Hi!', 'Hey there!', 'Howdy!', 'Greetings!']
        self.questions = ['How can I assist you with your shopping today?', 'What products are you looking for?', 'Do you need help with your order?']
        self.responses = ['I am here to assist you with your shopping needs. How can I help you today?',
                          'I can help you with product information, order status, returns, and more. What do you need assistance with?',
                          'We have a variety of products available. What are you interested in?',
                          'If you have any questions, feel free to ask. I am here to help!',
                          'Thank you for visiting our store. How can I assist you today?']

    def get_response(self, user_input):
        user_input = user_input.lower()
        if self.match_greeting(user_input):
            return random.choice(self.greetings) + ' ' + random.choice(self.responses)
        if user_input.endswith('?'):
            return random.choice(self.questions)
        return self.match_patterns(user_input)

    def match_greeting(self, user_input):
        return re.search(r'hi|hello|hey', user_input)

    def match_patterns(self, user_input):
        patterns = [
            (r'what is your name', "My name is ShopBot, your shopping assistant."),
            (r'my name is (.+)', lambda match: f"Nice to meet you, {match.group(1)}! How can I assist you today?"),
            (r'joke|funny|laugh', lambda _: random.choice([
                "Why did the tomato turn red? Because it saw the salad dressing!",
                "Why did the chicken cross the playground? To get to the other slide!",
                "What do you call a bear with no teeth? A gummy bear!"
            ])),
            (r'order status|track order|where is my order', "Please provide your order number, and I will check the status for you."),
            (r'return policy|how to return|return item', "You can return any item within 30 days of purchase. Please visit our returns page for more details."),
            (r'payment methods|how to pay|payment options', "We accept credit cards, debit cards, PayPal, and other payment methods. Please visit our payment options page for more details."),
            (r'product details|tell me about (.+)', lambda match: f"Please visit our website and search for '{match.group(1)}' to get detailed information about it."),
            (r'shipping information|shipping cost|delivery time', "Shipping costs and delivery times vary based on your location and the items ordered. Please visit our shipping information page for more details."),
            (r'discounts|promotions|sales', "We have ongoing promotions and discounts. Please visit our promotions page to see the latest offers."),
            (r'customer reviews|product reviews', "You can find customer reviews on the product pages on our website."),
            (r'new arrivals|latest products', "Check out our new arrivals section on the website to see the latest products."),
            (r'best sellers|popular products', "Visit our best sellers section to see the most popular products."),
            (r'contact support|customer service', "You can contact our customer support team via the contact us page on our website."),
            (r'account issues|login problems|password reset', "For account issues, please visit the account help section on our website."),
            (r'gift cards|gift vouchers', "You can purchase gift cards and vouchers from our gift cards page."),
            (r'loyalty program|rewards', "Join our loyalty program to earn rewards on your purchases. Visit our loyalty program page for more details.")
        ]
        for pattern, response in patterns:
            match = re.search(pattern, user_input)
            if match:
                return response(match) if callable(response) else response
        return random.choice(self.greetings) + ' ' + random.choice(self.responses)

def main():
    bot = ShopBot()
    while True:
        user_input = input("You: ")
        response = bot.get_response(user_input)
        print("ShopBot:", response)

if __name__ == "__main__":
    main()