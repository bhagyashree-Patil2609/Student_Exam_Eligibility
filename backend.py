def evaluate_eligibility(file):
    try:
        if file is None:
            return "INVALID INPUT FILE"

        with open(file.name, "r", encoding="utf-8") as f:
            lines = f.readlines()

        if not lines:
            return "INVALID INPUT FILE"

        result = []

        for line in lines:
            line = line.strip()
            if not line:
                continue

            try:
                roll, attendance = line.split(",")
                roll = roll.strip()
                attendance = float(attendance.strip())

                if attendance >= 85:
                    status = "ELIGIBLE FOR EXAM"
                elif 65 <= attendance <= 84:
                    status = "CONDONATION REQUIRED"
                else:
                    status = "NOT ELIGIBLE"

                result.append(f"Roll No: {roll} - {status}")

            except:
                continue   # ignore invalid records

        if not result:
            return "INVALID INPUT FILE"

        return "\n".join(result)

    except Exception:
        return "INVALID INPUT FILE"
