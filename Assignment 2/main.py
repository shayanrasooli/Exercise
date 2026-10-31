"""پروژه تکمیلی: تحلیل ثبت‌نام، پرداخت و گواهی‌های آموزشگاه

راهنما:
1) ابتدا چهار فایل JSON را باز و ساختار آن‌ها را بررسی کنید.
2) جای خالی‌های مشخص‌شده با _____ را تکمیل کنید.
3) فقط از کتابخانه‌های استاندارد Python استفاده کنید.
4) استفاده از Counter و defaultdict ممنوع است.
"""

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

# وضعیت‌های مجاز ثبت‌نام و تراکنش‌ها
VALID_ENROLLMENT_STATUSES = {"COMPLETED", "IN_PROGRESS"}
VALID_PAYMENT_TYPES = {"PAYMENT", "REFUND"}
VALID_PAYMENT_STATUS = "SUCCESS"


def load_json(filename, key):
    """یک فایل JSON را بخوانید و مقدار کلید اصلی آن را برگردانید."""
    file_path = BASE_DIR / filename
    with file_path.open("r", encoding="utf-8") as file:
        data = json.load(file)

    return data[key]


def main():
    students = load_json("students.json", "students")
    courses = load_json("courses.json", "courses")
    enrollment_rows = load_json("enrollments.json", "enrollments")
    transactions = load_json("payments.json", "transactions")

    # ------------------------------------------------------------
    # مرحله اول: ساخت نمایه‌ها و اعتبارسنجی ثبت‌نام‌ها
    # ------------------------------------------------------------

    students_by_id = {}
    for student in students:
        # TODO 1:
        # اطلاعات هر دانش‌آموز باید با شناسه‌اش قابل دسترسی باشد.
        # دلیل: در هر رکورد ثبت‌نام فقط student_id داریم و نباید هر بار
        # برای پیدا کردن دانش‌آموز، کل فهرست را از ابتدا جست‌وجو کنیم.
        students_by_id[_____] = student

    # نمایه دوره‌ها؛ کلید دیکشنری کد دوره است.
    # مجموعه کدها برای بررسی سریع معتبر بودن دوره استفاده می‌شود.
    courses_by_code = {course["code"]: course for course in courses}
    available_course_codes = set(courses_by_code)

    active_students = []
    for student in students:
        if student["active"]:
            active_students.append(student)

    clean_enrollments = []
    enrollments_by_key = {}
    seen_enrollment_keys = set()

    students_by_course = {}
    course_counts = {}
    scores_by_course = {}
    courses_with_enrollments = set()
    ignored_enrollment_count = 0

    for row in enrollment_rows:
        student_id = row["student_id"]

        # TODO 2:
        # دانش‌آموز را با استفاده از نمایه ساخته‌شده پیدا کنید.
        # دلیل: ممکن است شناسه در فایل وجود نداشته باشد؛ در این حالت
        # برنامه نباید با KeyError متوقف شود.
        student = students_by_id._____(student_id)

        # TODO 3:
        # رکورد دانش‌آموز ناشناخته یا غیرفعال را نپذیرید.
        # دلیل: ثبت‌نام فقط برای دانش‌آموز فعال و شناخته‌شده معتبر است.
        if _____:
            ignored_enrollment_count += 1
            continue

        # TODO 4:
        # کد دوره را قبل از مقایسه استاندارد کنید.
        # دلیل: " py101 " و "PY101" باید یک کد در نظر گرفته شوند.
        course_code = row["course_code"]._____()._____

        # TODO 5:
        # وضعیت ثبت‌نام را نیز استاندارد کنید.
        # دلیل: فاصله و بزرگی/کوچکی حروف نباید باعث رد رکورد معتبر شود.
        status = row["status"]._____()._____

        # TODO 6:
        # فقط دوره‌های موجود در کاتالوگ و وضعیت‌های مجاز را نگه دارید.
        # دلیل: دوره ناشناخته یا ثبت‌نام لغوشده نباید وارد گزارش شود.
        if _____ or status not in VALID_ENROLLMENT_STATUSES:
            ignored_enrollment_count += 1
            continue

        score = row["score"]

        # TODO 7:
        # نمره باید یا None باشد یا عددی بین 0 تا 100.
        # دلیل: داده خراب نباید میانگین دوره یا تصمیم گواهی را خراب کند.
        if score is not None and (_____):
            ignored_enrollment_count += 1
            continue

        # TODO 8:
        # ثبت‌نام تکمیل‌شده حتماً باید نمره داشته باشد.
        # دلیل: بدون نمره نمی‌توان قبولی یا عدم قبولی را تعیین کرد.
        if status == "COMPLETED" and _____:
            ignored_enrollment_count += 1
            continue

        # TODO 9:
        # یک کلید مرکب بسازید که ترکیب دانش‌آموز و دوره را مشخص کند.
        # دلیل: هر دانش‌آموز فقط یک ثبت‌نام معتبر برای هر دوره دارد.
        enrollment_key = _____

        # TODO 10:
        # اگر این ترکیب قبلاً دیده شده، رکورد تکراری را رد کنید.
        # دلیل: یک ثبت‌نام نباید در آمار دوره دو بار شمرده شود.
        if enrollment_key in _____:
            ignored_enrollment_count += 1
            continue

        # TODO 11:
        # ترکیب معتبر را برای تشخیص تکرارهای بعدی ذخیره کنید.
        # دلیل: Set برای نگهداری کلیدهای مرکب یکتا مناسب است.
        seen_enrollment_keys._____(enrollment_key)

        # TODO 12:
        # یک دیکشنری تازه بسازید؛ اطلاعات اصلی را نگه دارید، اما
        # course_code و status استانداردشده را جایگزین کنید.
        # دلیل: ** دیکشنری را باز می‌کند و کلیدهای بعدی مقدار قبلی را می‌پوشانند.
        clean_row = {_____, "course_code": course_code, "status": status}
        clean_enrollments.append(clean_row)
        enrollments_by_key[enrollment_key] = clean_row

        # TODO 13:
        # دانش‌آموز را در گروه همان دوره قرار دهید.
        # دلیل: هر دوره باید فهرست جداگانه‌ای از دانش‌آموزان داشته باشد.
        students_by_course._____(course_code, [])._____(student["name"])

        # TODO 14:
        # تعداد ثبت‌نام‌های یکتای دوره را افزایش دهید.
        # دلیل: ممکن است کلید دوره هنوز در دیکشنری شمارش وجود نداشته باشد.
        course_counts[course_code] = course_counts._____(course_code, 0) + 1

        if score is not None:
            # TODO 15:
            # نمره را به فهرست نمره‌های همان دوره اضافه کنید.
            # دلیل: در مرحله گزارش باید میانگین نمره هر دوره محاسبه شود.
            scores_by_course._____(course_code, [])._____(score)

        # TODO 16:
        # دوره دارای ثبت‌نام معتبر را به مجموعه دوره‌های استفاده‌شده اضافه کنید.
        # دلیل: بعداً با تفاضل Setها دوره‌های بدون ثبت‌نام را پیدا می‌کنیم.
        courses_with_enrollments._____(course_code)

    # ------------------------------------------------------------
    # مرحله دوم: محاسبه پرداخت خالص هر ثبت‌نام
    # ------------------------------------------------------------

    seen_transaction_ids = set()
    net_paid_by_enrollment = {}
    ignored_transaction_count = 0

    for transaction in transactions:
        transaction_id = transaction["transaction_id"]

        # TODO 17:
        # هر شناسه تراکنش را فقط یک بار پردازش کنید.
        # دلیل: ممکن است یک رکورد پرداخت به دلیل خطای خروجی چند بار تکرار شده باشد.
        if transaction_id in _____:
            ignored_transaction_count += 1
            continue
        seen_transaction_ids._____(transaction_id)

        transaction_type = transaction["type"].strip().upper()
        transaction_status = transaction["status"].strip().upper()
        student_id = transaction["student_id"]
        course_code = transaction["course_code"].strip().upper()

        # TODO 18:
        # از Tuple به‌عنوان کلید مرکب پرداخت استفاده کنید.
        # دلیل: مبلغ باید برای هر ترکیب دانش‌آموز و دوره جداگانه محاسبه شود.
        payment_key = _____

        # TODO 19:
        # پرداختی را نپذیرید که برای ثبت‌نام معتبر وجود ندارد.
        # دلیل: پرداخت یک دوره ناشناخته یا ثبت‌نام‌نشده نباید وارد گزارش شود.
        if payment_key not in _____:
            ignored_transaction_count += 1
            continue

        # TODO 20:
        # فقط تراکنش موفق از نوع پرداخت یا برگشت وجه معتبر است.
        # دلیل: تراکنش ناموفق یا نوع ناشناخته نباید روی مانده اثر بگذارد.
        if _____ or transaction_type not in VALID_PAYMENT_TYPES:
            ignored_transaction_count += 1
            continue

        amount = transaction["amount"]

        # TODO 21:
        # مبلغ باید عددی و بزرگ‌تر از صفر باشد.
        # دلیل: مبلغ منفی یا متن، ورودی مالی معتبری نیست.
        if _____:
            ignored_transaction_count += 1
            continue

        current_total = net_paid_by_enrollment.get(payment_key, 0)

        # TODO 22:
        # PAYMENT مبلغ را اضافه می‌کند؛ REFUND از مبلغ خالص کم می‌کند.
        # دلیل: برای تشخیص تسویه کامل باید پرداخت‌ها و برگشت وجه‌ها را با هم حساب کرد.
        if transaction_type == "PAYMENT":
            net_paid_by_enrollment[payment_key] = _____
        else:
            net_paid_by_enrollment[payment_key] = _____

    # جمع مبلغ خالص به تفکیک دوره
    revenue_by_course = {}
    for payment_key, net_amount in net_paid_by_enrollment.items():
        # TODO 23:
        # دو بخش کلید Tuple را در دو متغیر جدا قرار دهید.
        # دلیل: بخش دوم کلید، کد دوره‌ای است که باید درآمد به آن نسبت داده شود.
        student_id, course_code = _____
        revenue_by_course[course_code] = revenue_by_course.get(course_code, 0) + net_amount

    # ------------------------------------------------------------
    # مرحله سوم: مانده بدهی و بررسی گواهی پایان دوره
    # ------------------------------------------------------------

    outstanding_balances = []
    for enrollment in clean_enrollments:
        course = courses_by_code[enrollment["course_code"]]
        payment_key = (enrollment["student_id"], enrollment["course_code"])
        paid_amount = net_paid_by_enrollment.get(payment_key, 0)
        balance = course["price"] - paid_amount

        # TODO 24:
        # فقط ثبت‌نام‌هایی را نگه دارید که هنوز مبلغی بدهکارند.
        # دلیل: مدیر آموزشگاه باید بتواند پیگیری مالی را از روی گزارش انجام دهد.
        if _____:
            student = students_by_id[enrollment["student_id"]]
            outstanding_balances.append({
                "student": student["name"],
                "course_code": course["code"],
                "balance": balance,
            })

    certificates = []
    certificates_by_student = {}

    for student in active_students:
        certified_courses = set()

        # ترتیب دوره‌ها در courses.json رعایت‌کننده پیش‌نیازهاست:
        # ابتدا دوره‌های پایه و سپس دوره‌های وابسته قرار گرفته‌اند.
        for course in courses:
            course_code = course["code"]
            enrollment_key = (student["id"], course_code)
            enrollment = enrollments_by_key.get(enrollment_key)

            if enrollment is None or enrollment["status"] != "COMPLETED":
                continue

            # TODO 25:
            # اگر نمره کمتر از حد قبولی دوره است، گواهی صادر نشود.
            # دلیل: صرفاً ثبت‌نام یا حضور در دوره به معنی قبولی نیست.
            if _____:
                continue

            # TODO 26:
            # پیش‌نیازهای دوره را به Set تبدیل کنید.
            # دلیل: برای بررسی عضویت تمام پیش‌نیازها از عملیات مجموعه‌ای استفاده می‌کنیم.
            required_courses = _____

            # TODO 27:
            # گواهی فقط وقتی صادر شود که تمام پیش‌نیازها قبلاً تأیید شده باشند.
            # دلیل: قبولی در دوره پیشرفته بدون گذراندن پیش‌نیازها کافی نیست.
            if not required_courses._____(certified_courses):
                continue

            paid_amount = net_paid_by_enrollment.get(enrollment_key, 0)

            # TODO 28:
            # اگر پرداخت خالص کمتر از شهریه دوره است، گواهی صادر نشود.
            # دلیل: صدور گواهی علاوه بر قبولی، به تسویه مالی هم وابسته است.
            if _____:
                continue

            # TODO 29:
            # کد دوره تأییدشده را به Set گواهی‌های دانش‌آموز اضافه کنید.
            # دلیل: دوره‌های تأییدشده باید یکتا باشند تا پیش‌نیاز دوره بعدی شوند.
            certified_courses._____(course_code)

            certificates.append({
                "student_id": student["id"],
                "student_name": student["name"],
                "course_code": course_code,
                "course_title": course["title"],
            })

        certificates_by_student[student["id"]] = certified_courses

    # ------------------------------------------------------------
    # مرحله چهارم: ساخت گزارش نهایی
    # ------------------------------------------------------------

    # TODO 30:
    # دوره‌های ارائه‌شده‌ای را پیدا کنید که ثبت‌نام معتبر ندارند.
    # دلیل: تفاضل Setها این مسئله را بدون حلقه تو در تو حل می‌کند.
    courses_without_enrollments = _____ - _____

    course_reports = []
    for course in courses:
        code = course["code"]
        scores = scores_by_course.get(code, [])
        average_score = round(sum(scores) / len(scores), 1) if scores else None

        report_row = {"code": code, "title": course["title"]}

        # TODO 31:
        # اطلاعات آماری را یک‌جا به دیکشنری گزارش اضافه کنید.
        # دلیل: update برای افزودن/به‌روزرسانی چند کلید در یک مرحله مناسب است.
        report_row._____(
            {
                "registered_students": course_counts.get(code, 0),
                "average_score": average_score,
                "net_revenue": revenue_by_course.get(code, 0),
            }
        )
        course_reports.append(report_row)

    print("\n========== ACADEMY TERM REPORT ==========")
    print("Total student records:", len(students))
    print("Active students:", len(active_students))
    print("Enrollment rows in file:", len(enrollment_rows))
    print("Accepted unique enrollments:", len(clean_enrollments))
    print("Ignored enrollment rows:", ignored_enrollment_count)
    print("Payment transactions in file:", len(transactions))
    print("Ignored payment transactions:", ignored_transaction_count)

    print("\n--- COURSE REPORT ---")
    for report in course_reports:
        print(
            f"{report['code']} | {report['title']} | "
            f"students={report['registered_students']} | "
            f"average={report['average_score']} | "
            f"net_revenue={report['net_revenue']}"
        )
        print("  Students:", students_by_course.get(report["code"], []))

    print("\n--- CERTIFICATES ISSUED ---")
    for certificate in certificates:
        print(
            f"{certificate['student_name']} ({certificate['student_id']}) "
            f"-> {certificate['course_code']}"
        )

    print("\n--- OUTSTANDING BALANCES ---")
    for item in outstanding_balances:
        print(f"{item['student']} | {item['course_code']} | balance={item['balance']}")

    print("\n--- COURSES WITHOUT VALID ENROLLMENTS ---")
    print(sorted(courses_without_enrollments))

    print("\n--- CERTIFIED COURSES PER ACTIVE STUDENT ---")
    for student in active_students:
        print(student["name"], sorted(certificates_by_student.get(student["id"], set())))


if __name__ == "__main__":
    main()
