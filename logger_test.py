from person import Person
from logger import Logger

def test_file_logger():
    test_file_name = "test_file.txt"
    logger = Logger(test_file_name)
    logger.write_metadata(pop_size=100, vacc_percentage=0.2, virus_name="AIDS", mortality_rate=0.03, basic_repro_num=0.4)
    person_1 = Person(1, None)
    person_2 = Person(2, None)
    logger.log_interaction(person_1, person_2, random_person_sick=True, random_person_vacc=False, did_infect=True)
    logger.log_interaction(person_1, person_2, random_person_sick=False, random_person_vacc=True, did_infect=False)
    logger.log_interaction(person_1, person_2, random_person_sick=True, random_person_vacc=False, did_infect=False)
    logger.log_infection_survival(person_1, True)
    logger.log_infection_survival(person_1, False)
    logger.close()

    test_file = open(test_file_name)
    metadata_line = test_file.readline()
    assert metadata_line == "Parameters:%s\t%s\t%s\t%s\t%s\n" % (100, 0.2, "AIDS", 0.03, 0.4)
    print("Passed write_metadata")

    interaction_line = test_file.readline()
    assert interaction_line == "1 did infect 2\n"
    interaction_line = test_file.readline()
    assert interaction_line == "1 did not infect 2 because vaccinated\n"
    interaction_line = test_file.readline()
    assert interaction_line == "1 did not infect 2 because already infected\n"
    print("Passed log_interaction")

    infection_survival_line = test_file.readline()
    assert infection_survival_line == "1 died\n"
    infection_survival_line = test_file.readline()
    assert infection_survival_line == "1 survived infection\n"
    print("Passed infection_survival_line")

if __name__ == "__main__":
    test_file_logger()