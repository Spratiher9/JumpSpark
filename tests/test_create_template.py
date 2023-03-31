import os
import re
import subprocess  # noqa


def build_files_list(root_dir):
    """Build a list containing absolute paths to the generated files."""
    return [
        os.path.join(dirpath, file_path)
        for dirpath, _, files in os.walk(root_dir)
        for file_path in files
    ]


def test_run_cookiecutter_result(cookies):
    """Runs cookiecutter and checks a couple of things"""
    project_name = "Nephelheim"
    result = cookies.bake(
        extra_context={"project_name": project_name}
    )

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_path.name == project_name
    assert result.project_path.is_dir()

    readme_path = result.project_path / "README.md"
    assert readme_path.is_file()

    with open(readme_path, "r") as f:
        readme = f.read()
        assert project_name in readme
        assert "project_name" not in readme


def test_cookiecutter_generated_files(cookies):
    """tests the generated files names make sense"""
    re_bad = re.compile(r"{{\s?cookiecutter\..*?}}")
    result = cookies.bake()

    assert all(
        re_bad.search(str(file_path)) is None
        for file_path in result.project_path.glob("*")
    )


def test_cookiecutter_make_qa(cookies):
    """runs tests on the generated dir"""
    result = cookies.bake()

    make_proc = subprocess.Popen(
        ["/usr/bin/make", "qa"],
        shell=False,  # noqa
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        cwd=result.project_path,
    )
    # stdout, stderr are for debuggin
    stdout, stderr = make_proc.communicate()
    assert make_proc.returncode == 0


def test_python_installation(cookies):
    """tests the poetry installation scripts"""
    result = cookies.bake()

    make_proc = subprocess.Popen(
        ["/usr/bin/which", "python"],
        shell=False,  # noqa
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        cwd=result.project_path,
    )
    stdout, stderr = make_proc.communicate()
    assert make_proc.returncode == 0
    assert "pypoetry/virtualenvs" in str(stdout)