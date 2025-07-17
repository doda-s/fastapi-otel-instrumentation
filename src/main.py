import pyroscope
from fastapi import FastAPI

from opentelemetry import trace
from opentelemetry import metrics

from utils.utils import dice_random_number
from services.order_service import order

pyroscope.configure(
  application_name = "my.fastapi.app", # replace this with some name for your application
  server_address   = "http://localhost:4040", # replace this with the address of your Pyroscope server
  sample_rate      = 100, # default is 100
  oncpu            = True, # report cpu time only; default is True
)

tracer = trace.get_tracer("diceroller.tracer")
meter = metrics.get_meter("diceroller.meter")

roll_counter = meter.create_counter(
    "dice.rolls",
    description="The number of rolls by roll value.",
)

with tracer.start_as_current_span("foo"):
    current_span = trace.get_current_span()
    current_span.add_event("This is a span event.")

app = FastAPI()

@app.get("/dice/roll")
async def diceRoll():
    with tracer.start_as_current_span("roll") as rollspan:
        result = dice_random_number()
        rollspan.set_attribute("roll.value", result)
        roll_counter.add(1, {"roll.value": result})
        return result
    
@app.get("/order/car")
async def order_car():
    order(0.5, "car")
    return {"message": "New car order"}

@app.get("/order/bike")
async def order_bike():
    order(0.4, "bike")
    return {"message": "New bike order"}

@app.get("/order/scooter")
async def order_scooter():
    order(0.5, "scooter")
    return {"message": "New scooter order"}