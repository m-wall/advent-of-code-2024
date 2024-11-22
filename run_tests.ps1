# Get the current directory
$currentDirectory = Get-Location

# Loop through folders numbered 01 to 25
for ($i = 1; $i -le 25; $i++) {
  # Construct the folder path with leading zero padding
  $folderPath = Join-Path $currentDirectory ("{0:D2}" -f $i)

  # Check if the folder exists
  if (Test-Path $folderPath) {
    # Change directory to the folder
    Set-Location $folderPath

    # Run python tests.py using the full path to the python executable
    & uv run python "tests.py"

    # Change back to the current directory
    Set-Location $currentDirectory
  }
}