# Dynamic Optimization of Essential Oil Extraction
> A project to model and eventually control the batch distillation of essential oil

## Initial Model
An initial model is found in `initial_model.py`.

This model is based on a FOPDT relation between `u` (heat input) and `y_model` (condenser flow rate). After that a fractional flow model is used to determine the fraction of condenser flow that is essential oil.

## Initial data
From the videos we received from YoungLiving, we estimate a total essential oil yield of about 7ml from 1 kg of plant matter. They ran with the still at a consistent heat and had a relatively constant condensate flowrate of about 7 ml/min. The videos also said that about 90% of the oil comes out in the first hour of distillation. Hopefully these values will allow better generation of fake data while we are waiting for real data.

## Trial Data
Trial data files are the trialx.csv file. They include volume measurements of oil and hydrosol, as well as the temperature setpoint on the hotplate. Time is in units of minutes after passover.