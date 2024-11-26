import yaml

if __name__ == '__main__':
    # Load the Conda environment file
    with open('environment.yml') as f:
        conda_env = yaml.safe_load(f)

    # Write the requirements.txt file
    with open('requirements.txt', 'w') as f:
        for dep in conda_env['dependencies']:
            if isinstance(dep, str):  # Regular package
                f.write(f"{dep}\n")
            elif isinstance(dep, dict) and 'pip' in dep:  # Pip packages
                for pip_dep in dep['pip']:
                    f.write(f"{pip_dep}\n")