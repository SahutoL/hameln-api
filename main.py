from fastapi import FastAPI
import model

app = FastAPI(title="Hameln API")


@app.get("/daily/novels")
async def daily_novels(): return model.get_daily_novel()

@app.get("/weekly/novels/")
def weekly_novels(): return model.get_weekly_novel()

@app.get("/monthly/novels/")
def monthly_novels(): return model.get_monthly_novel()

@app.get("/three_monthly/novels/")
def three_monthly_novels(): return model.get_three_monthly_novel()

@app.get("/yearly/novels/")
def yearly_novels(): return model.get_yearly_novel()

@app.get("/total/novels/")
def total_novels(): return model.get_total_novel()
