# Changelog

All notable changes are documented here.


### 2022-01-07
- fix: handle network error during webcam frame read


### 2022-01-12
- feat: add model download helper script for weights


### 2022-01-14
- fix: handle webcam open failure with descriptive error


### 2022-01-16
- fix: resolve APScheduler job duplication on hot restart


### 2022-01-19
- fix: fix cooldown timer reset logic after detection


### 2022-01-19
- fix: resolve CORS preflight failure on dashboard endpoint


### 2022-01-21
- test: add unit tests for phone detection confidence logic


### 2022-02-02
- fix: resolve APScheduler job duplication on hot restart


### 2022-02-11
- fix: resolve CORS preflight failure on dashboard endpoint


### 2022-02-13
- test: add mock-based test for Twilio SMS dispatch


### 2022-02-18
- feat: add price change percentage threshold alerting


### 2022-02-21
- fix: resolve OpenCV display crash on Windows 11


### 2022-03-03
- feat: implement SQLite persistence for alert history


### 2022-03-03
- feat: add concurrent ticker fetching with asyncio gather


### 2022-03-08
- feat: implement SQLite persistence for alert history


### 2022-03-14
- refactor: separate FastAPI routes into dedicated routers


### 2022-03-15
- refactor: separate alert dispatch from detection pipeline


### 2022-03-17
- fix: resolve CORS preflight failure on dashboard endpoint


### 2022-03-19
- fix: fix SQLite connection handling in async context


### 2022-03-23
- fix: handle OpenAI API timeout in analysis agent


### 2022-04-04
- perf: cache OpenCV DNN model to avoid reloading per frame


### 2022-04-05
- feat: add FastAPI health and watchlist endpoints


### 2022-04-05
- chore: add pre-commit hooks for black and ruff


### 2022-04-06
- refactor: separate FastAPI routes into dedicated routers


### 2022-04-06
- feat: add graceful retry on yFinance API failure


### 2022-04-13
- fix: fix SQLite connection handling in async context


### 2022-04-19
- fix: correct confidence threshold comparison operator


### 2022-04-25
- fix: resolve OpenCV display crash on Windows 11


### 2022-04-30
- chore: add pre-commit hooks for black and ruff


### 2022-05-04
- feat: implement yFinance ticker price polling loop


### 2022-05-09
- docs: document camera index configuration in README


### 2022-05-13
- fix: correct price change percentage sign for falling assets


### 2022-05-21
- fix: fix yFinance rate limit with exponential backoff


### 2022-05-26
- chore: add .gitignore entries for SQLite database files


### 2022-06-07
- fix: resolve CORS preflight failure on dashboard endpoint


### 2022-06-09
- feat: implement COCO class 77 phone classifier detection


### 2022-06-09
- docs: document alert threshold configuration options


### 2022-06-13
- fix: fix yFinance rate limit with exponential backoff


### 2022-06-14
- chore: add .gitignore entries for SQLite database files


### 2022-06-15
- feat: add OpenCV webcam capture loop with configurable index


### 2022-06-21
- feat: implement yFinance ticker price polling loop


### 2022-06-22
- feat: add Docker Compose for local development setup


### 2022-07-06
- feat: implement MobileNet SSD phone detection via OpenCV DNN


### 2022-07-06
- fix: resolve APScheduler job duplication on hot restart


### 2022-07-07
- style: format all files with black


### 2022-07-08
- fix: correct timezone handling for alert timestamps


### 2022-07-12
- feat: add OpenCV webcam capture loop with configurable index


### 2022-07-15
- chore: add pre-commit hooks for black and ruff


### 2022-07-19
- fix: handle network error during webcam frame read


### 2022-07-25
- refactor: extract phone detection logic from main loop


