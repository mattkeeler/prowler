from prowler.lib.check.models import Check, Check_Report_GCP
from prowler.providers.gcp.services.cloudstorage.cloudstorage_client import (
    cloudstorage_client,
)


class cloudstorage_bucket_public_access(Check):
    def execute(self) -> Check_Report_GCP:
        findings = []
        for bucket in cloudstorage_client.buckets:
            report = Check_Report_GCP(metadata=self.metadata(), resource=bucket)
            report.status = "PASS"
            report.status_extended = f"Bucket {bucket.name} is not publicly accessible."
            if bucket.public:
                report.status = "FAIL"
                report.status_extended = f"Bucket {bucket.name} is publicly accessible."
            findings.append(report)

        return findings
