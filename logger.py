class Logger(object):
    ''' Utility class responsible for logging all interactions during the simulation. '''
    # TODO: Write a test suite for this class to make sure each method is working
    # as expected.

    # PROTIP: Write your tests before you solve each function, that way you can
    # test them one by one as you write your class.

    def __init__(self, file_name):
        self.file_name = file_name
        self.file = open(file_name, "w")

    def write_metadata(self, pop_size, vacc_percentage, virus_name, mortality_rate,
                       basic_repro_num):
        '''
        The simulation class should use this method immediately to log the specific
        parameters of the simulation as the first line of the file.
        '''
        self.file.write("Parameters:%s\t%s\t%s\t%s\t%s\n" % (pop_size, vacc_percentage, virus_name, mortality_rate, basic_repro_num))

    def log_interaction(self, person, random_person, random_person_sick=None,
                        random_person_vacc=None, did_infect=None):
        '''
        The Simulation object should use this method to log every interaction
        a sick person has during each time step.
        The format of the log should be: "{person.ID} infects {random_person.ID} \n"
        or the other edge cases:
            "{person.ID} didn't infect {random_person.ID} because {'vaccinated' or 'already sick'} \n"
        '''
        if did_infect:
            self.file.write("%s did infect %s\n" % (person._id, random_person._id))
        elif random_person_vacc:
            self.file.write("%s did not infect %s because vaccinated\n" % (person._id, random_person._id))
        elif random_person_sick:
            self.file.write("%s did not infect %s because already infected\n" % (person._id, random_person._id))
        else:
            self.file.write("%s did not infect %s because chance\n" % (person._id, random_person._id))

    def log_infection_survival(self, person, did_die_from_infection):
        ''' The Simulation object uses this method to log the results of every
        call of a Person object's .resolve_infection() method.
        The format of the log should be:
            "{person.ID} died from infection\n" or "{person.ID} survived infection.\n"
        '''
        if did_die_from_infection:
            self.file.write("%s died\n" % person._id)
        else:
            self.file.write("%s survived infection\n" % person._id)

    def close(self):
        '''Closes the logging file.'''
        self.file.close()

    def log_time_step(self, time_step_counter, num_died, num_vaccinated, num_infected, total_dead, total_vaccinated):
        ''' STRETCH CHALLENGE DETAILS:
        If you choose to extend this method, the format of the summary statistics logged
        are up to you.
        At minimum, it should contain:
            The number of people that were infected during this specific time step.
            The number of people that died on this specific time step.
            The total number of people infected in the population, including the newly infected
            The total number of dead, including those that died during this time step.
        The format of this log should be:
            "Time step {time_step_number} ended, beginning {time_step_number + 1}\n"
        '''
        self.file.write("\n\n\n\n\n==========\n")
        self.file.write("Time step %s ended\n" % time_step_counter)
        self.file.write("Num died: %s\n" % num_died)
        self.file.write("Num vaccinated: %s\n" % num_vaccinated)
        self.file.write("Num infected: %s\n" % num_infected)
        self.file.write("Total dead: %s\n" % total_dead)
        self.file.write("Total vaccinated: %s\n" % total_vaccinated)
        self.file.write("\n==========\n\n\n\n\n")
