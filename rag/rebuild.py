import argparse
import shutil
from pathlib import Path

from rag.retriever import DB_PATH, create_vectorstore


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Rebuild FAISS vectorstore from data/raw and web sources."
    )
    parser.add_argument(
        "--reset",
        action="store_true",
        help="Delete existing vectorstore before rebuilding.",
    )
    args = parser.parse_args()

    db_path = Path(DB_PATH)
    if args.reset and db_path.exists():
        shutil.rmtree(db_path)
        print(f"Deleted existing vectorstore at: {db_path}")

    create_vectorstore()
    print("Vectorstore rebuild completed.")


if __name__ == "__main__":
    main()
