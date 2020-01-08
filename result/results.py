
    def get_grade(self, ca_score, exam_score):
        scores = int(ca_score) + int(exam_score)
        if scores >= 70:
            grade = 'A'
        elif scores < 70 and scores >=60:
            grade = 'B'
        elif scores < 60 and scores >=50:
            grade = 'C'
        elif scores <50 and scores >=45:
            grade =  'D'
        else:
            grade = 'F'
    
    

    def get_score(self, ca_score, exam_score):
        return intsubject.ca_score + exam_score    


    def get_total_scores(self):
        term = Term.objects.get(current_term=True)
        students = SubjectOffered.objects.filter(student=self.student,
        subject_level =self.student.student_class, subject_term = term)
        total_scores = 0
        scores = []
        for score in students.total_score:
            total_scores =+ score    
            scores.append(score)


    def get_total_subject(self):
        term = Term.objects.get(current_term=True)
        students = SubjectOffered.objects.filter(student=self.student, 
        subject_level = self.student.student_class, subject_term = term)
        total_subject= []
        for subject in student.subject:
            total_subject.append(subject)
        total_subject_offered = len(total_subject)
        return(total_subject_offered) 
    
    def get_average_scores(self):
        term = Term.objects.get(current_term = True)
        students = SubjectOffered.objects.filter(student=self.student,
        subject_level = self.student.student_class, subject_term = term)
        scores = []
        total_score = 0
        for score in students.total_score:
            scores.append(score)
            total_score =+ score 
        lenth = len(scores)
        average = total_score/lenth
        return average



    def get_full_name(self, full_name ):
        name = full_name
        return name