# Dynamic Optimization of Essential Oil Extraction
> A project to model and eventually control the batch distillation of essential oil

## Initial Model
An initial model is found in `initial_model.py`.

This model is based on a FOPDT relation between `u` (heat input) and `y_model` (condenser flow rate). After that a fractional flow model is used to determine the fraction of condenser flow that is essential oil.