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


