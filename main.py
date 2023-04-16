from fastapi import FastAPI
from pydantic import BaseModel
import model

app = FastAPI(title="Hameln API")


class DailyNovel(BaseModel):
    daily_novel: dict = model.get_daily_novel()

class WeeklyNovel(BaseModel):
    weekly_novel: dict = model.get_weekly_novel()

class MonthlyNovel(BaseModel):
    monthly_novel: dict = model.get_monthly_novel()

class ThreeMonthlyNovel(BaseModel):
    monthly_novel: dict = model.get_three_monthly_novel()

class YearlyNovel(BaseModel):
    monthly_novel: dict = model.get_yearly_novel()

class TotalNovel(BaseModel):
    monthly_novel: dict = model.get_total_novel()

@app.get("/daily/novels/")
async def daily_novels(daily_novels: DailyNovel):
    return {"daily_novels": daily_novels}

@app.get("/weekly/novels/")
def weekly_novels(weekly_novels: WeeklyNovel):
    return {"weekly_novels": weekly_novels}

@app.get("/monthly/novels/")
def monthly_novels(monthly_novels: MonthlyNovel):
    return {"monthly_novels": monthly_novels}

@app.get("/three_monthly/novels/")
def three_monthly_novels(three_monthly_novels: ThreeMonthlyNovel):
    return {"three_monthly_novels": three_monthly_novels}

@app.get("/yearly/novels/")
def yearly_novels(yearly_novels: YearlyNovel):
    return {"yearly_novels": yearly_novels}

@app.get("/total/novels/")
def total_novels(total_novels: TotalNovel):
    return {"total_novels": total_novels}