from requests import delete, post

# корректный запрос
print(post('http://localhost:5000/api/jobs/5').json())
# нет такого id
print(delete('http://localhost:5000/api/jobs/9999'))
# некорректный запрос
print(delete('http://localhost:5000/api/jobs/ras').json())