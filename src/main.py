import random
from fastapi import FastAPI

from opentelemetry import trace
from opentelemetry import metrics

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
        result = random_number()
        rollspan.set_attribute("roll.value", result)
        roll_counter.add(1, {"roll.value": result})
        return result

def random_number():
    result = random.randrange(1, 6)
    return result