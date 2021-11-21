def printing_models(unprinted_designs, completed_models):
    """Cycle print all models until list has unprinted models"""
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        # Print model
        print("Printing model: " + current_design)
        completed_models.append(current_design)


def show_completed_models(complited_models):
    """Print all models that are done."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)


# List of models that need to be printed
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

printing_models(unprinted_designs, completed_models)
show_completed_models(completed_models)


