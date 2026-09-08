from dataclasses import dataclass
import re
from typing import List


@dataclass
class FraudSignal:
    name: str
    weight: float
    explanation: str


class DocumentFraudIntelligence:
    """OCR-oriented validation and explainable risk scoring demo."""

    GSTIN_PATTERN = re.compile(r"^[0-9]{2}[A-Z]{5}[0-9]{4}[A-Z][1-9A-Z]Z[0-9A-Z]$")
    RC_PATTERN = re.compile(r"^[A-Z]{2}[0-9]{1,2}[A-Z]{1,3}[0-9]{4}$")

    def inspect(self, extracted: dict) -> dict:
        signals: List[FraudSignal] = []
        gstin = str(extracted.get("gstin", "")).replace(" ", "").upper()
        rc = str(extracted.get("vehicle_rc", "")).replace(" ", "").upper()
        amount = extracted.get("amount")
        qr_amount = extracted.get("qr_amount")

        if gstin and not self.GSTIN_PATTERN.match(gstin):
            signals.append(FraudSignal("invalid_gstin_format", 0.35, "GSTIN does not match the expected structural pattern."))
        if rc and not self.RC_PATTERN.match(rc):
            signals.append(FraudSignal("invalid_rc_format", 0.20, "Vehicle registration identifier has an unexpected format."))
        if amount is not None and qr_amount is not None and abs(float(amount) - float(qr_amount)) > 1.0:
            signals.append(FraudSignal("amount_qr_mismatch", 0.40, "OCR amount and QR payload amount disagree."))
        if extracted.get("duplicate_document_hash"):
            signals.append(FraudSignal("duplicate_document", 0.45, "Document hash was observed previously in the synthetic store."))
        if extracted.get("ocr_confidence", 1.0) < 0.65:
            signals.append(FraudSignal("low_ocr_confidence", 0.10, "Critical fields were read with low OCR confidence."))

        risk = min(1.0, sum(signal.weight for signal in signals))
        return {
            "risk_score": round(risk, 3),
            "decision": "review" if risk >= 0.35 else "pass",
            "signals": [signal.__dict__ for signal in signals],
        }


if __name__ == "__main__":
    engine = DocumentFraudIntelligence()
    print(engine.inspect({"gstin": "22AAAAA0000A1Z5", "amount": 12500, "qr_amount": 12000, "ocr_confidence": 0.91}))
