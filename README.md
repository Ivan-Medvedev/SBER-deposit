# SBER-deposit

Для запуска с помощью Docker необходимо:
1) Собрать образ
```
docker build -t deposit .
```
2) Запустить
```
docker run --name depo --rm -d -p 5000:5000 deposit
```

Endpoints (точки доступа):
1) `..:5000/healthcheck` — для проверки статуса работы сервера.
2) `..:5000/deposit` — для подсчета депозита.
