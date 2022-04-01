from requests_html import HTMLSession
from ticket import Ticket

url = 'https://www.calottery.com/'
powerball_prizes_url = 'https://www.calottery.com/draw-games/powerball#section-content-1-3'
superball_prizes_url = 'https://www.calottery.com/draw-games/superlotto-plus#section-content-1-3'
megaball_prizes_url = 'https://www.calottery.com/draw-games/mega-millions#section-content-1-3'

def get_winning_nums() -> list[Ticket]:
    session = HTMLSession()

    request = session.get(url)
    result = []
    result.append(scrape_nums(request, '//*[@id="drawGame12"]/div[1]/ul', "Powerball"))
    result.append(scrape_nums(request, '//*[@id="drawGame8"]/div[1]/ul', "Superball"))
    result.append(scrape_nums(request, '//*[@id="drawGame15"]/div[1]/ul', "Megaball"))

    get_prizes_for_winning_tickets(session, powerball_prizes_url, result[0])
    get_prizes_for_winning_tickets(session, superball_prizes_url, result[1])
    get_prizes_for_winning_tickets(session, megaball_prizes_url, result[2])
    return result

def scrape_nums(request, xpath, ticket_name) -> Ticket:
    nums_path = request.html.xpath(xpath)
    nums = []

    for line in nums_path:
        for num in line.text.split('\n'):
            if ticket_name in num:
                index = num.index(ticket_name)
                nums.append(int(num[0: index - 1]))
            else:
                nums.append(int(num))
    
    ticket = Ticket(ticket_name)
    ticket.set_ticket_nums(nums)
    return ticket

def get_prizes_for_winning_tickets(session, price_url, ticket):
    request = session.get(price_url)

    winning_prizes = []
    
    # index 0 = specials match, index 1 = 1 num + special ...
    # For reference: see https://www.calottery.com/draw-games/powerball#section-content-1-3
    for i in range(8, -1, -1):
        winning_prizes.append(int(request.html.xpath('//*[@id="section-content-1-3"]/div[2]/div[1]/div/table/tbody/tr[' + str(i + 1) + ']/td[3]')[0].text[1:].replace(',', '')))

    ticket.set_winning_prizes(winning_prizes)