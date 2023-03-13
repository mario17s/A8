from src.repository.general_repo import Repository
from src.repository.grade_repo import GradeRepository
from src.services.discipline_service import DisciplineService
from src.services.grade_service import GradeService
from src.services.student_service import StudentService
from src.ui.console import Console

if __name__ == "__main__":
    student_repo = Repository()
    discipline_repo = Repository()
    grade_repo = GradeRepository(student_repo, discipline_repo)
    student_service = StudentService(student_repo)
    discipline_service = DisciplineService(discipline_repo)
    grade_service = GradeService(grade_repo)
    console = Console(student_service, discipline_service, grade_service)
    console.run_console()