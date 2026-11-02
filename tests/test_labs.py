from pathlib import Path
from validate_labs import validate_cloudformation_template

ROOT = Path(__file__).parent.parent


def test_cloudformation_template_valid():
    cfn_path = ROOT / "LAMP_template.json"
    assert cfn_path.exists()
    data, errors = validate_cloudformation_template(cfn_path)
    assert len(errors) == 0
    assert "Resources" in data
    assert len(data["Resources"]) > 0


def test_markdown_guides_exist():
    assert (ROOT / "Clean_CloudFormation_LAMP_Lab_README.md").exists()
    assert (ROOT / "iam-ec2-intro-lab-README.md").exists()
    assert (ROOT / "vpc-custom-subnet-lab-README.md").exists()
