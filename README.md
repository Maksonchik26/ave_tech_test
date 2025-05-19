# 📦 Ave Tech Test Backend

FastAPI-приложение для технического теста, развёртываемое в Docker.

---

## 🚀 Быстрый старт

### 🔧 Зависимости

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

---

## ⚙️ Сборка и запуск

```bash
docker-compose up --build
```

После успешной сборки приложение будет доступно по адресу:

- 🌐 **API**: [http://localhost:8000](http://localhost:8000)
- 📄 **Документация Swagger (OpenAPI)**: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## ⚠️ Важно: Установка рабочей версии Redis клиента

По умолчанию в контейнере может присутствовать ошибка, затрагивающая библиотеки `redis`, что вызывает ошибки при запуске.

### 🛠️ Решение (временно вручную):

1. Зайти в контейнер:

```bash
docker exec -it ave_tech_test-backend-1 bash
```

2. Удалить текущую версию `redis`:

```bash
pip uninstall redis -y
```

3. Установить актуальную версию заново:

```bash
pip install redis
```

4. Выйти из контейнера:

```bash
exit
```

5. Перезапустить контейнер:

```bash
docker restart ave_tech_test-backend-1
```
