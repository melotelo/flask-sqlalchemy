from flask_sqlalchemy.extension import SQLAlchemy, print_coverage, branch_coverage

def test_make_metadata():
    sqlalchemy_instance = SQLAlchemy()

    # Testing with a valid example key
    result = sqlalchemy_instance._make_metadata("example_key")

    # Test with no keys
    result = sqlalchemy_instance._make_metadata(None)

def test_set_rel_query():
    sqlalchemy_instance = SQLAlchemy()

    # Testing with backref as a string
    kwargs_example = {"query_class": None, "backref": "example_backref"}
    sqlalchemy_instance._set_rel_query(kwargs_example)

    # Testing without backref
    kwargs_example = {"query_class": None}
    sqlalchemy_instance._set_rel_query(kwargs_example)

def reset_coverage():
    for key in branch_coverage.keys():
        branch_coverage[key] = False

if __name__ == "__main__":
    
    reset_coverage()
    
    test_make_metadata()
    test_set_rel_query()

    print_coverage()