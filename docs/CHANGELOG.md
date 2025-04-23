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


### 2022-07-28
- fix: resolve OpenCV display crash on Windows 11


### 2022-07-28
- feat: add OpenCV webcam capture loop with configurable index


### 2022-08-01
- feat: add FastAPI health and watchlist endpoints


### 2022-08-01
- test: add price change percentage calculation tests


### 2022-08-11
- chore: add pre-commit hooks for black and ruff


### 2022-08-16
- test: add integration test for watchlist REST API


### 2022-08-16
- feat: implement detection confidence overlay on live frame


### 2022-08-16
- refactor: extract phone detection logic from main loop


### 2022-08-23
- feat: add concurrent ticker fetching with asyncio gather


### 2022-08-24
- chore: update requirements.txt with current versions


### 2022-08-26
- refactor: separate FastAPI routes into dedicated routers


### 2022-08-31
- feat: implement OpenAI agent for price anomaly analysis


### 2022-09-06
- fix: handle OpenAI API timeout in analysis agent


### 2022-09-07
- refactor: separate alert dispatch from detection pipeline


### 2022-09-08
- refactor: extract phone detection logic from main loop


### 2022-09-08
- fix: handle missing model files with graceful fallback


### 2022-09-13
- style: format all files with black


### 2022-09-13
- fix: handle OpenAI API timeout in analysis agent


### 2022-09-14
- refactor: extract phone detection logic from main loop


### 2022-09-14
- style: normalise import ordering


### 2022-09-26
- feat: add FastAPI health and watchlist endpoints


### 2022-09-27
- feat: implement alert deduplication within cooldown window


### 2022-10-06
- test: add price change percentage calculation tests


### 2022-10-07
- refactor: extract watchlist management into service class


### 2022-10-10
- fix: handle empty watchlist gracefully on startup


### 2022-10-15
- fix: resolve APScheduler job duplication on hot restart


### 2022-10-16
- docs: add model download instructions to setup guide


### 2022-10-19
- feat: add graceful retry on yFinance API failure


### 2022-10-24
- docs: document alert threshold configuration options


### 2022-10-24
- test: add cooldown timer unit tests


### 2022-11-01
- fix: correct price change percentage sign for falling assets


### 2022-11-07
- test: add price change percentage calculation tests


### 2022-11-15
- feat: add camera index configuration via environment variable


### 2022-11-16
- fix: correct price change percentage sign for falling assets


### 2022-11-28
- feat: implement structured JSON logging throughout


### 2022-11-29
- test: add integration test for watchlist REST API


### 2022-12-05
- fix: correct timezone handling for alert timestamps


### 2022-12-05
- fix: handle OpenAI API timeout in analysis agent


### 2022-12-06
- refactor: consolidate database operations into repository


### 2022-12-08
- feat: implement MobileNet SSD phone detection via OpenCV DNN


### 2022-12-08
- refactor: extract watchlist management into service class


### 2022-12-15
- chore: add .gitignore entries for SQLite database files


### 2022-12-19
- refactor: separate alert dispatch from detection pipeline


### 2022-12-23
- test: add unit tests for phone detection confidence logic


### 2022-12-24
- fix: resolve APScheduler job duplication on hot restart


### 2023-01-17
- fix: fix alert threshold comparison for downside moves


### 2023-01-21
- feat: implement MobileNet SSD phone detection via OpenCV DNN


### 2023-01-23
- docs: add model download instructions to setup guide


### 2023-01-30
- perf: implement async yFinance fetching for concurrent tickers


### 2023-02-01
- feat: implement graceful shutdown on Q keypress


### 2023-02-02
- feat: add APScheduler job for configurable polling interval


### 2023-02-03
- feat: add Docker Compose for local development setup


### 2023-02-15
- refactor: separate FastAPI routes into dedicated routers


### 2023-02-16
- refactor: move all configuration to environment variables


### 2023-02-22
- feat: add Twilio SMS alert dispatch on condition trigger


### 2023-02-28
- feat: add FastAPI health and watchlist endpoints


### 2023-03-05
- fix: fix cooldown timer reset logic after detection


### 2023-03-15
- test: add price change percentage calculation tests


### 2023-03-19
- docs: update docs/API.md with all watchlist endpoints


### 2023-03-29
- style: normalise import ordering


### 2023-03-29
- feat: add price change percentage threshold alerting


### 2023-04-06
- test: add price change percentage calculation tests


### 2023-04-07
- test: add mock-based test for Twilio SMS dispatch


### 2023-04-10
- refactor: extract OpenAI agent setup into factory function


### 2023-04-11
- test: add price change percentage calculation tests


### 2023-04-20
- docs: add model download instructions to setup guide


### 2023-04-25
- feat: add model download helper script for weights


### 2023-04-27
- feat: add FastAPI health and watchlist endpoints


### 2023-05-02
- refactor: extract phone detection logic from main loop


### 2023-05-05
- feat: add price change percentage threshold alerting


### 2023-05-08
- feat: implement SQLite persistence for alert history


### 2023-05-11
- refactor: separate FastAPI routes into dedicated routers


### 2023-05-12
- feat: implement alert history endpoint with date filtering


### 2023-05-17
- docs: update docs/API.md with all watchlist endpoints


### 2023-05-17
- feat: add Twilio SMS alert dispatch on condition trigger


### 2023-05-18
- refactor: extract watchlist management into service class


### 2023-05-22
- feat: add price change percentage threshold alerting


### 2023-05-23
- fix: correct confidence threshold comparison operator


### 2023-05-25
- fix: correct timezone handling for alert timestamps


### 2023-05-25
- docs: update .env.example with all required variables


### 2023-05-26
- test: add cooldown timer unit tests


### 2023-05-29
- feat: implement COCO class 77 phone classifier detection


### 2023-05-30
- feat: implement cooldown timer between consecutive alert triggers


### 2023-05-31
- perf: use connection pool for SQLite write operations


### 2023-06-01
- chore: bump fastapi to 0.115.x


### 2023-06-05
- feat: implement OpenAI agent for price anomaly analysis


### 2023-06-06
- fix: fix alert threshold comparison for downside moves


### 2023-06-06
- feat: add price change percentage threshold alerting


### 2023-06-09
- test: add integration test for watchlist REST API


### 2023-06-14
- test: add mock-based test for Twilio SMS dispatch


### 2023-06-19
- docs: update .env.example with all required variables


### 2023-06-22
- feat: add OpenCV webcam capture loop with configurable index


### 2023-06-23
- fix: handle webcam open failure with descriptive error


### 2023-06-24
- feat: implement MobileNet SSD phone detection via OpenCV DNN


### 2023-07-07
- test: add integration test for watchlist REST API


### 2023-07-07
- style: normalise import ordering


### 2023-07-11
- test: add mock-based test for Twilio SMS dispatch


### 2023-07-19
- feat: add browser-based rickroll alert dispatch via webbrowser


### 2023-07-24
- fix: fix cooldown timer reset logic after detection


### 2023-07-31
- feat: add browser-based rickroll alert dispatch via webbrowser


### 2023-07-31
- feat: implement yFinance ticker price polling loop


### 2023-08-11
- feat: implement cooldown timer between consecutive alert triggers


### 2023-08-14
- refactor: extract OpenAI agent setup into factory function


### 2023-08-22
- fix: resolve APScheduler job duplication on hot restart


### 2023-08-30
- feat: add APScheduler job for configurable polling interval


### 2023-08-30
- feat: add camera index configuration via environment variable


### 2023-08-31
- feat: implement alert deduplication within cooldown window


### 2023-08-31
- chore: update requirements.txt with current versions


### 2023-09-06
- feat: add graceful retry on yFinance API failure


### 2023-09-10
- refactor: consolidate database operations into repository


### 2023-09-15
- feat: add Docker Compose for local development setup


### 2023-09-19
- feat: implement real-time price dashboard endpoint


### 2023-09-22
- feat: implement cooldown timer between consecutive alert triggers


### 2023-09-29
- fix: fix SQLite connection handling in async context


### 2023-10-04
- feat: implement OpenAI agent for price anomaly analysis


### 2023-10-05
- docs: update docs/API.md with all watchlist endpoints


### 2023-10-09
- refactor: separate alert dispatch from detection pipeline


### 2023-10-13
- feat: implement SQLite persistence for alert history


### 2023-10-20
- fix: handle network error during webcam frame read


### 2023-10-27
- feat: implement detection confidence overlay on live frame


### 2023-10-29
- feat: add browser-based rickroll alert dispatch via webbrowser


### 2023-10-30
- feat: add OpenCV webcam capture loop with configurable index


### 2023-10-31
- feat: implement OpenAI agent for price anomaly analysis


### 2023-11-06
- fix: fix cooldown timer reset logic after detection


### 2023-11-06
- refactor: separate alert dispatch from detection pipeline


### 2023-11-06
- chore: add .gitignore entries for SQLite database files


### 2023-11-17
- chore: update requirements.txt with current versions


### 2023-11-30
- docs: update .env.example with all required variables


### 2023-11-30
- fix: handle network error during webcam frame read


### 2023-12-14
- docs: add data flow diagram for agent architecture


### 2023-12-17
- feat: implement detection confidence overlay on live frame


### 2023-12-18
- refactor: separate FastAPI routes into dedicated routers


### 2023-12-20
- docs: update .env.example with all required variables


### 2023-12-22
- fix: correct confidence threshold comparison operator


### 2023-12-22
- feat: implement detection confidence overlay on live frame


### 2023-12-27
- feat: add OpenCV webcam capture loop with configurable index


### 2023-12-28
- test: add mock-based test for Twilio SMS dispatch


### 2024-01-02
- feat: add detection confidence threshold configuration


### 2024-01-05
- feat: add price change percentage threshold alerting


### 2024-01-10
- chore: bump fastapi to 0.115.x


### 2024-01-11
- feat: implement structured JSON logging throughout


### 2024-01-14
- refactor: extract OpenAI agent setup into factory function


### 2024-01-18
- fix: handle missing model files with graceful fallback


### 2024-01-19
- feat: implement cooldown timer between consecutive alert triggers


### 2024-01-19
- refactor: separate alert dispatch from detection pipeline


### 2024-02-02
- test: add integration test for watchlist REST API


### 2024-02-05
- feat: implement COCO class 77 phone classifier detection


### 2024-02-06
- refactor: separate alert dispatch from detection pipeline


### 2024-02-06
- docs: document alert threshold configuration options


### 2024-02-23
- docs: add model download instructions to setup guide


### 2024-02-27
- fix: handle OpenAI API timeout in analysis agent


### 2024-03-04
- fix: handle network error during webcam frame read


### 2024-03-11
- refactor: separate FastAPI routes into dedicated routers


### 2024-03-18
- feat: add Twilio SMS alert dispatch on condition trigger


### 2024-03-22
- fix: handle OpenAI API timeout in analysis agent


### 2024-03-24
- feat: add FastAPI health and watchlist endpoints


### 2024-03-28
- refactor: extract OpenAI agent setup into factory function


### 2024-03-30
- docs: add model download instructions to setup guide


### 2024-04-04
- feat: add detection confidence threshold configuration


### 2024-04-06
- fix: correct confidence threshold comparison operator


### 2024-04-07
- refactor: extract phone detection logic from main loop


### 2024-04-10
- chore: bump fastapi to 0.115.x


### 2024-04-17
- refactor: extract phone detection logic from main loop


### 2024-04-17
- fix: fix alert threshold comparison for downside moves


### 2024-04-30
- feat: add Docker Compose for local development setup


### 2024-05-02
- feat: add browser-based rickroll alert dispatch via webbrowser


### 2024-05-04
- chore: update requirements.txt with current versions


### 2024-05-04
- docs: add model download instructions to setup guide


### 2024-05-09
- fix: handle network error during webcam frame read


### 2024-05-11
- feat: implement graceful shutdown on Q keypress


### 2024-05-11
- chore: update requirements.txt with current versions


### 2024-05-15
- feat: add Twilio SMS alert dispatch on condition trigger


### 2024-05-16
- feat: add graceful retry on yFinance API failure


### 2024-05-17
- style: format all files with black


### 2024-05-20
- feat: implement MobileNet SSD phone detection via OpenCV DNN


### 2024-05-22
- feat: implement COCO class 77 phone classifier detection


### 2024-05-22
- fix: correct timezone handling for alert timestamps


### 2024-06-04
- feat: add concurrent ticker fetching with asyncio gather


### 2024-06-05
- perf: implement async yFinance fetching for concurrent tickers


### 2024-06-20
- test: add unit tests for phone detection confidence logic


### 2024-06-22
- fix: resolve Twilio auth token validation error


### 2024-06-25
- perf: implement async yFinance fetching for concurrent tickers


### 2024-06-25
- feat: implement cooldown timer between consecutive alert triggers


### 2024-06-28
- chore: add .gitignore entries for SQLite database files


### 2024-06-29
- refactor: move all configuration to environment variables


### 2024-07-02
- feat: implement real-time price dashboard endpoint


### 2024-07-03
- fix: resolve Twilio auth token validation error


### 2024-07-09
- chore: add pre-commit hooks for black and ruff


### 2024-07-11
- fix: handle network error during webcam frame read


### 2024-07-15
- refactor: extract phone detection logic from main loop


### 2024-07-18
- feat: add browser-based rickroll alert dispatch via webbrowser


### 2024-07-18
- feat: add Docker Compose for local development setup


### 2024-07-22
- feat: add model download helper script for weights


