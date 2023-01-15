from selene.support.shared import browser


def set_date(month, year, day):
    browser.element('#dateOfBirthInput').click()
    browser.element('[class="react-datepicker__month-select"]').click()
    browser.element(f'[value="{month}"]').click()
    browser.element('[class="react-datepicker__year-select"]').click()
    browser.element(f'[value="{year}"]').click()
    browser.element(f'.react-datepicker__day--0{day}').click()
