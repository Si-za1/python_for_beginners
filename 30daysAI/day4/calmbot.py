from ai import calm_bot_message

class CalmBot:
    def __init__(self, verbose=True):
        self.verbose = verbose

    def handle_error_text(self, error_text: str) -> str:
        if not any(kw in error_text for kw in ["Error", "Exception", "Traceback", "SyntaxError"]):
            return "❓ Hmm, that doesn't look like a standard Python error. Could you paste the full message, including traceback if available?"

        error_type = self._extract_error_type(error_text)
        error_msg = self._extract_error_message(error_text)
        tb = error_text  # Treat full input as traceback

        if self.verbose:
            print("\n🌿 Calm Error Bot says:\n")

        return calm_bot_message(error_type, error_msg, tb)

    def _extract_error_type(self, error_text: str) -> str:
        # Look for typical Python error formats
        for line in error_text.strip().split('\n'):
            if ':' in line and any(err in line for err in ["Error", "Exception"]):
                return line.split(':')[0].strip()
        return "UnknownError"

    def _extract_error_message(self, error_text: str) -> str:
        for line in error_text.strip().split('\n'):
            if ':' in line and any(err in line for err in ["Error", "Exception"]):
                return line.split(':', 1)[1].strip()
        return error_text.strip()
