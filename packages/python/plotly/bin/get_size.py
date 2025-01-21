"""Calculate total size and total number of files of package."""

from pathlib import Path
import sys


def main():
    """Main driver."""
    assert len(sys.argv) == 3, "Usage: get_size.py src_dir build_dir"
    src_files, src_bytes = get_size(sys.argv[1])
    build_files, build_bytes = get_size(sys.argv[2])
    print(f"which\t{'num_files':8s}\t{'num_bytes':8s}")
    print(f"src\t{src_files:8d}\t{src_bytes:8d}")
    print(f"build\t{build_files:8d}\t{build_bytes:8d}")


def get_size(root_dir):
    """Count files and size in bytes."""
    num_files, num_bytes = 0, 0
    for f in Path(root_dir).glob("**/*.*"):
        num_files += 1
        num_bytes += f.stat().st_size
    return num_files, num_bytes


if __name__ == "__main__":
    main()
