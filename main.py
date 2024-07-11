from user_interaction import UserInteraction
from vacancy_controler import VacancyController
from in_out import InOutController


if __name__ == '__main__':
    app = UserInteraction()
    app.run()
    vacancies_list = list(InOutController.load_vacancies(app.filter_words, app.search_query))
    InOutController.write_in_file(vacancies_list, 'vacancies.txt')
    v = InOutController.get_from_file('vacancies.txt')

    InOutController.print_vacancies(v)

    controller = VacancyController()

    filtered_vacancies = controller.filter_vacancies(vacancies_list, app.filter_words)
    ranged_vacancies = controller.get_vacancies_by_salary(filtered_vacancies, app.min_salary, app.max_salary)
    sorted_vacancies = controller.sort_vacancies(ranged_vacancies)
    top_vacancies = controller.get_top_vacancies(sorted_vacancies, app.top_n)

    InOutController.print_vacancies(top_vacancies)

