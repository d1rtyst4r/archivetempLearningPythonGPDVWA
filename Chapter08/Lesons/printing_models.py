def printing_models(unprinted_designs, completed_models):
    """Cycle print all models until list has unprinted models"""
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        # Print model
        print("Printing model: " + current_design)
        completed_models.append(current_design)


def show_completed_models(complited_models: object) -> object:
    """Print all models that are done."""
    print("\nThe following models have been printed:")
    for completed_model in complited_models:
        print(completed_model)



