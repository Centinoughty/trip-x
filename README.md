# AI Travel Planner Agent

An AI-powered travel planning assistant designed to simplify the way people plan their trips. It uses multi-agent architecture to understand travel requirements, gather relevant information, and generate personalized travel plans.

The project is built with extensibility in mind, allowing new tools to be added eventually.

## Table of Contents

- [Introduction](#-introduction)
- [Architecture](#-architecture)
- [Tech Stack](#-tech-stack)
- [Installation](#-installation)
- [Extensibility](#-extensibility)
- [Future Enhancements](#-future-enhancements)

## Introduction

Planning a trip often involves researching destinations, checking weather conditions, comparing travel costs, and organizing itineraries. This project aims to bring these activities together through an AI-powered multi-agent system. The agent coordinates different responsibilities to create travel plans based on user preferences, requirements, and constraints.

## Architecture

The system follows a multi-agent architecture, where each agent is responsible for a specific part of the travel planning process. The main components include:

- **Travel Planner Agent**: Understands user requirements and coordinates the planning process
- **Specialized Agents**: Handle specific tasks such as destination research, itinerary planning, and travel recommendations.
- **Tool Integrations**: Provide external information and capabilities to agents.
- **LLM Layer**: Reasoning, decision-making, and natural language interactions.

## Tech Stack

- **Language**: Python
- **Package Manager**: uv
- **AI/LLM**: Gemini
- **Architecture**: Multi-Agent System

## Installation

### Prerequisites
- [Python](https://www.python.org/downloads/)
- [uv](https://docs.astral.sh/uv/getting-started/installation/)
- [Google Gemini API](https://aistudio.google.com/api-keys)

### Installation Steps

#### 1. Clone the repository

```bash
git clone https://github.com/Centinoughty/trip-x.git
cd trip-x
```

#### 2. Install dependencies

```bash
uv sync
```

#### 3. Update the environment variables

To copy `.env.example` to `.env`, choose the exact command below based on your operating system and terminal.

```bash
cp .env.example .env        ## Linux and macOS
Copy-Item .env.example .env ## Windows PowerShell
copy .env.example .env      ## Windows CMD
```

Configure the required environment variables for your chosen LLM provider before running the application.

#### 4. Run the application

```bash
uv run python -m trip_x.main
```

## Extensibility

One of the key design goals is to make the system easy to extend. New tools can be integrated without significantly changing the existing architecture. Potential integrations include weather information, flight and hotel pricing, destination research, maps and location services, currency conversion, etc.

## Future Enhancements

- Expand the collection of specialized agents.
- Integrate real-time travel information.
- Improve itinerary personalization.
- Introduce additional external tools and services.
- Enhance planning and decision-making capabilities.

*Built as an exploration of agentic AI, multi-agent orchestration, and extensible AI systems.*
