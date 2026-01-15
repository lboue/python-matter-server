/**
 * Utilities for formatting attribute values for display.
 */

/**
 * Decode a base64-encoded string.
 * @param base64 - The base64-encoded string
 * @returns The decoded string
 */
function decodeBase64(base64: string): string {
  try {
    // Decode base64 to binary string
    const binaryString = atob(base64);
    // Convert binary string to Uint8Array
    const bytes = new Uint8Array(binaryString.length);
    for (let i = 0; i < binaryString.length; i++) {
      bytes[i] = binaryString.charCodeAt(i);
    }
    // Decode as UTF-8 string
    const decoder = new TextDecoder("utf-8");
    return decoder.decode(bytes);
  } catch (e) {
    // If decoding fails, return the original base64 string
    return base64;
  }
}

/**
 * Format an attribute value for display based on its type.
 * @param value - The attribute value (can be base64-encoded bytes)
 * @param type - The type string from the cluster description (e.g., "bytes", "Union[NoneType, Nullable, bytes]")
 * @returns The formatted value as a string
 */
export function formatAttributeValue(value: any, type?: string): string {
  // Handle null/undefined
  if (value === null || value === undefined) {
    return "null";
  }

  // Check if the type indicates bytes
  const isBytesType = type?.includes("bytes");

  // If it's a bytes type and the value is a string (base64-encoded)
  if (isBytesType && typeof value === "string") {
    // Try to decode as UTF-8 string
    const decoded = decodeBase64(value);
    // If the decoded string contains only printable characters, use it
    if (/^[\x20-\x7E]*$/.test(decoded)) {
      return decoded || "(empty)";
    }
    // Otherwise, show as hex
    try {
      const binaryString = atob(value);
      const hex = Array.from(binaryString)
        .map((char) => char.charCodeAt(0).toString(16).padStart(2, "0"))
        .join(" ");
      return `0x${hex.replace(/ /g, " ")}`;
    } catch {
      return value;
    }
  }

  // For List[bytes], decode each element
  if (
    isBytesType &&
    Array.isArray(value) &&
    type?.startsWith("List[bytes]")
  ) {
    return (
      "[" +
      value
        .map((item) => {
          if (typeof item === "string") {
            const decoded = decodeBase64(item);
            if (/^[\x20-\x7E]*$/.test(decoded)) {
              return `"${decoded}"`;
            }
          }
          return JSON.stringify(item);
        })
        .join(", ") +
      "]"
    );
  }

  // For all other types, use JSON.stringify
  return JSON.stringify(value);
}
