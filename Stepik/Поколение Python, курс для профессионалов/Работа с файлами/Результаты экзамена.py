import csv, json, arrow

in_path = '/home/user/py-studying/Stepik/Поколение Python, курс для профессионалов/Работа с файлами/exam_results.csv'
out_path = '/home/user/py-studying/Stepik/Поколение Python, курс для профессионалов/Работа с файлами/best_scores.json'

with open(in_path, 'r', encoding='UTF-8', newline='') as f, \
     open(out_path, 'w', encoding='UTF-8', newline='') as fo:

    data = csv.DictReader(f)
    best_result = {}

    for r in data:
        email = r['email']
        score = int(r['score'])
        date = arrow.get(r['date_and_time'])

        if email not in best_result:
            best_result[email] = r
        else:
            existing = best_result[email]
            existing_score = int(existing['score'])
            existing_date = arrow.get(existing['date_and_time'])

            if score > existing_score or (score == existing_score and date > existing_date):
                best_result[email] = r

    result_list = [v for k, v in sorted(best_result.items())]
    for record in result_list:
        record['best_score'] = int(record.pop('score'))

    json.dump(result_list, fo, ensure_ascii=False, indent=4)