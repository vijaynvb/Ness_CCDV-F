from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Docs")
docs = {"plan.md": "The plan outlines the project steps."}

@mcp.tool()
def read_doc(doc_id: str) -> str:
    """Read a document by id."""
    return docs[doc_id]

@mcp.resource("docs://list")
def list_docs() -> list[str]:
    return list(docs)

@mcp.prompt()
def summarise(doc_id: str) -> str:
    return f"Summarise document {doc_id}."

if __name__ == "__main__":
    mcp.run(transport="stdio")