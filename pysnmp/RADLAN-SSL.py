# SNMP MIB module (RADLAN-SSL) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RADLAN-SSL
# Produced by pysmi-1.5.4 at Mon Oct 14 22:43:30 2024
# On host MacBook-Pro.local platform Darwin version 24.0.0 by user lextm
# Using Python version 3.12.0 (main, Nov 14 2023, 23:52:11) [Clang 15.0.0 (clang-1500.0.40.1)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint,
 ConstraintsUnion) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint",
    "ConstraintsUnion")

# Import SMI symbols from the MIBs this MIB depends on

(rnd,) = mibBuilder.importSymbols(
    "RADLAN-MIB",
    "rnd")

(RowStatus,
 TruthValue) = mibBuilder.importSymbols(
    "RADLAN-SNMPv2",
    "RowStatus",
    "TruthValue")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(DisplayString,) = mibBuilder.importSymbols(
    "SNMPv2-TC-v1",
    "DisplayString")


# MODULE-IDENTITY

rlSsl = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 89, 100)
)
rlSsl.setRevisions(
        ("2003-09-21 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RlSslCertificateGenerationTable_Object = MibTable
rlSslCertificateGenerationTable = _RlSslCertificateGenerationTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 100, 1)
)
if mibBuilder.loadTexts:
    rlSslCertificateGenerationTable.setStatus("current")
_RlSslCertificateGenerationEntry_Object = MibTableRow
rlSslCertificateGenerationEntry = _RlSslCertificateGenerationEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 100, 1, 1)
)
rlSslCertificateGenerationEntry.setIndexNames(
    (0, "RADLAN-SSL", "rlSslCertificateGenerationIndex"),
)
if mibBuilder.loadTexts:
    rlSslCertificateGenerationEntry.setStatus("current")
_RlSslCertificateGenerationIndex_Type = Integer32
_RlSslCertificateGenerationIndex_Object = MibTableColumn
rlSslCertificateGenerationIndex = _RlSslCertificateGenerationIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 100, 1, 1, 1),
    _RlSslCertificateGenerationIndex_Type()
)
rlSslCertificateGenerationIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSslCertificateGenerationIndex.setStatus("current")
_RlSslCertificateGenerationId_Type = Integer32
_RlSslCertificateGenerationId_Object = MibTableColumn
rlSslCertificateGenerationId = _RlSslCertificateGenerationId_Object(
    (1, 3, 6, 1, 4, 1, 89, 100, 1, 1, 2),
    _RlSslCertificateGenerationId_Type()
)
rlSslCertificateGenerationId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSslCertificateGenerationId.setStatus("current")


class _RlSslCertificateGenerationCountryName_Type(DisplayString):
    """Custom type rlSslCertificateGenerationCountryName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_RlSslCertificateGenerationCountryName_Type.__name__ = "DisplayString"
_RlSslCertificateGenerationCountryName_Object = MibTableColumn
rlSslCertificateGenerationCountryName = _RlSslCertificateGenerationCountryName_Object(
    (1, 3, 6, 1, 4, 1, 89, 100, 1, 1, 3),
    _RlSslCertificateGenerationCountryName_Type()
)
rlSslCertificateGenerationCountryName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSslCertificateGenerationCountryName.setStatus("current")


class _RlSslCertificateGenerationStateOrProvinceName_Type(DisplayString):
    """Custom type rlSslCertificateGenerationStateOrProvinceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_RlSslCertificateGenerationStateOrProvinceName_Type.__name__ = "DisplayString"
_RlSslCertificateGenerationStateOrProvinceName_Object = MibTableColumn
rlSslCertificateGenerationStateOrProvinceName = _RlSslCertificateGenerationStateOrProvinceName_Object(
    (1, 3, 6, 1, 4, 1, 89, 100, 1, 1, 4),
    _RlSslCertificateGenerationStateOrProvinceName_Type()
)
rlSslCertificateGenerationStateOrProvinceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSslCertificateGenerationStateOrProvinceName.setStatus("current")


class _RlSslCertificateGenerationLocalityName_Type(DisplayString):
    """Custom type rlSslCertificateGenerationLocalityName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_RlSslCertificateGenerationLocalityName_Type.__name__ = "DisplayString"
_RlSslCertificateGenerationLocalityName_Object = MibTableColumn
rlSslCertificateGenerationLocalityName = _RlSslCertificateGenerationLocalityName_Object(
    (1, 3, 6, 1, 4, 1, 89, 100, 1, 1, 5),
    _RlSslCertificateGenerationLocalityName_Type()
)
rlSslCertificateGenerationLocalityName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSslCertificateGenerationLocalityName.setStatus("current")


class _RlSslCertificateGenerationOrganizationName_Type(DisplayString):
    """Custom type rlSslCertificateGenerationOrganizationName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_RlSslCertificateGenerationOrganizationName_Type.__name__ = "DisplayString"
_RlSslCertificateGenerationOrganizationName_Object = MibTableColumn
rlSslCertificateGenerationOrganizationName = _RlSslCertificateGenerationOrganizationName_Object(
    (1, 3, 6, 1, 4, 1, 89, 100, 1, 1, 6),
    _RlSslCertificateGenerationOrganizationName_Type()
)
rlSslCertificateGenerationOrganizationName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSslCertificateGenerationOrganizationName.setStatus("current")


class _RlSslCertificateGenerationOrganizationUnitName_Type(DisplayString):
    """Custom type rlSslCertificateGenerationOrganizationUnitName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_RlSslCertificateGenerationOrganizationUnitName_Type.__name__ = "DisplayString"
_RlSslCertificateGenerationOrganizationUnitName_Object = MibTableColumn
rlSslCertificateGenerationOrganizationUnitName = _RlSslCertificateGenerationOrganizationUnitName_Object(
    (1, 3, 6, 1, 4, 1, 89, 100, 1, 1, 7),
    _RlSslCertificateGenerationOrganizationUnitName_Type()
)
rlSslCertificateGenerationOrganizationUnitName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSslCertificateGenerationOrganizationUnitName.setStatus("current")


class _RlSslCertificateGenerationCommonName_Type(DisplayString):
    """Custom type rlSslCertificateGenerationCommonName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_RlSslCertificateGenerationCommonName_Type.__name__ = "DisplayString"
_RlSslCertificateGenerationCommonName_Object = MibTableColumn
rlSslCertificateGenerationCommonName = _RlSslCertificateGenerationCommonName_Object(
    (1, 3, 6, 1, 4, 1, 89, 100, 1, 1, 8),
    _RlSslCertificateGenerationCommonName_Type()
)
rlSslCertificateGenerationCommonName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSslCertificateGenerationCommonName.setStatus("current")
_RlSslCertificateGenerationValidDays_Type = Integer32
_RlSslCertificateGenerationValidDays_Object = MibTableColumn
rlSslCertificateGenerationValidDays = _RlSslCertificateGenerationValidDays_Object(
    (1, 3, 6, 1, 4, 1, 89, 100, 1, 1, 9),
    _RlSslCertificateGenerationValidDays_Type()
)
rlSslCertificateGenerationValidDays.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSslCertificateGenerationValidDays.setStatus("current")


class _RlSslCertificateGenerationRsaKeyLength_Type(Integer32):
    """Custom type rlSslCertificateGenerationRsaKeyLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(512, 2048),
    )


_RlSslCertificateGenerationRsaKeyLength_Type.__name__ = "Integer32"
_RlSslCertificateGenerationRsaKeyLength_Object = MibTableColumn
rlSslCertificateGenerationRsaKeyLength = _RlSslCertificateGenerationRsaKeyLength_Object(
    (1, 3, 6, 1, 4, 1, 89, 100, 1, 1, 10),
    _RlSslCertificateGenerationRsaKeyLength_Type()
)
rlSslCertificateGenerationRsaKeyLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSslCertificateGenerationRsaKeyLength.setStatus("current")
_RlSslCertificateGenerationPassphrase_Type = DisplayString
_RlSslCertificateGenerationPassphrase_Object = MibTableColumn
rlSslCertificateGenerationPassphrase = _RlSslCertificateGenerationPassphrase_Object(
    (1, 3, 6, 1, 4, 1, 89, 100, 1, 1, 11),
    _RlSslCertificateGenerationPassphrase_Type()
)
rlSslCertificateGenerationPassphrase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSslCertificateGenerationPassphrase.setStatus("current")


class _RlSslCertificateGenerationAction_Type(Integer32):
    """Custom type rlSslCertificateGenerationAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("generateCertificateRequest", 4),
          ("generatePkcs12", 3),
          ("generateRsaKeyAndSelfSignedCertificate", 1),
          ("generateSelfSignedCertificate", 2))
    )


_RlSslCertificateGenerationAction_Type.__name__ = "Integer32"
_RlSslCertificateGenerationAction_Object = MibTableColumn
rlSslCertificateGenerationAction = _RlSslCertificateGenerationAction_Object(
    (1, 3, 6, 1, 4, 1, 89, 100, 1, 1, 12),
    _RlSslCertificateGenerationAction_Type()
)
rlSslCertificateGenerationAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSslCertificateGenerationAction.setStatus("current")
_RlSslCertificateExportTable_Object = MibTable
rlSslCertificateExportTable = _RlSslCertificateExportTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 100, 2)
)
if mibBuilder.loadTexts:
    rlSslCertificateExportTable.setStatus("current")
_RlSslCertificateExportEntry_Object = MibTableRow
rlSslCertificateExportEntry = _RlSslCertificateExportEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 100, 2, 1)
)
rlSslCertificateExportEntry.setIndexNames(
    (0, "RADLAN-SSL", "rlSslCertificateExportId"),
    (0, "RADLAN-SSL", "rlSslCertificateExportType"),
    (0, "RADLAN-SSL", "rlSslCertificateExportFragmentId"),
)
if mibBuilder.loadTexts:
    rlSslCertificateExportEntry.setStatus("current")
_RlSslCertificateExportId_Type = Integer32
_RlSslCertificateExportId_Object = MibTableColumn
rlSslCertificateExportId = _RlSslCertificateExportId_Object(
    (1, 3, 6, 1, 4, 1, 89, 100, 2, 1, 1),
    _RlSslCertificateExportId_Type()
)
rlSslCertificateExportId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSslCertificateExportId.setStatus("current")


class _RlSslCertificateExportType_Type(Integer32):
    """Custom type rlSslCertificateExportType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("certificateAndKeyPkcs12", 4),
          ("certificateOpenSslFormat", 3),
          ("certificatePemFormat", 2),
          ("certificateRequestPemFormat", 1))
    )


_RlSslCertificateExportType_Type.__name__ = "Integer32"
_RlSslCertificateExportType_Object = MibTableColumn
rlSslCertificateExportType = _RlSslCertificateExportType_Object(
    (1, 3, 6, 1, 4, 1, 89, 100, 2, 1, 2),
    _RlSslCertificateExportType_Type()
)
rlSslCertificateExportType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSslCertificateExportType.setStatus("current")
_RlSslCertificateExportFragmentId_Type = Integer32
_RlSslCertificateExportFragmentId_Object = MibTableColumn
rlSslCertificateExportFragmentId = _RlSslCertificateExportFragmentId_Object(
    (1, 3, 6, 1, 4, 1, 89, 100, 2, 1, 3),
    _RlSslCertificateExportFragmentId_Type()
)
rlSslCertificateExportFragmentId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSslCertificateExportFragmentId.setStatus("current")
_RlSslCertificateExportFragmentText_Type = OctetString
_RlSslCertificateExportFragmentText_Object = MibTableColumn
rlSslCertificateExportFragmentText = _RlSslCertificateExportFragmentText_Object(
    (1, 3, 6, 1, 4, 1, 89, 100, 2, 1, 4),
    _RlSslCertificateExportFragmentText_Type()
)
rlSslCertificateExportFragmentText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSslCertificateExportFragmentText.setStatus("current")
_RlSslCertificateSave_Type = Integer32
_RlSslCertificateSave_Object = MibScalar
rlSslCertificateSave = _RlSslCertificateSave_Object(
    (1, 3, 6, 1, 4, 1, 89, 100, 3),
    _RlSslCertificateSave_Type()
)
rlSslCertificateSave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSslCertificateSave.setStatus("current")


class _RlSslCertificateSaveFormat_Type(Integer32):
    """Custom type rlSslCertificateSaveFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pkcs12", 2),
          ("x509", 1))
    )


_RlSslCertificateSaveFormat_Type.__name__ = "Integer32"
_RlSslCertificateSaveFormat_Object = MibScalar
rlSslCertificateSaveFormat = _RlSslCertificateSaveFormat_Object(
    (1, 3, 6, 1, 4, 1, 89, 100, 4),
    _RlSslCertificateSaveFormat_Type()
)
rlSslCertificateSaveFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSslCertificateSaveFormat.setStatus("current")


class _RlSslImportedPKCS12CertificatePassphrase_Type(DisplayString):
    """Custom type rlSslImportedPKCS12CertificatePassphrase based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 96),
    )


_RlSslImportedPKCS12CertificatePassphrase_Type.__name__ = "DisplayString"
_RlSslImportedPKCS12CertificatePassphrase_Object = MibScalar
rlSslImportedPKCS12CertificatePassphrase = _RlSslImportedPKCS12CertificatePassphrase_Object(
    (1, 3, 6, 1, 4, 1, 89, 100, 5),
    _RlSslImportedPKCS12CertificatePassphrase_Type()
)
rlSslImportedPKCS12CertificatePassphrase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSslImportedPKCS12CertificatePassphrase.setStatus("current")
_RlSslCertificateImportTable_Object = MibTable
rlSslCertificateImportTable = _RlSslCertificateImportTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 100, 6)
)
if mibBuilder.loadTexts:
    rlSslCertificateImportTable.setStatus("current")
_RlSslCertificateImportEntry_Object = MibTableRow
rlSslCertificateImportEntry = _RlSslCertificateImportEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 100, 6, 1)
)
rlSslCertificateImportEntry.setIndexNames(
    (0, "RADLAN-SSL", "rlSslCertificateImportId"),
    (0, "RADLAN-SSL", "rlSslCertificateImportFormat"),
    (0, "RADLAN-SSL", "rlSslCertificateImportFragmentId"),
)
if mibBuilder.loadTexts:
    rlSslCertificateImportEntry.setStatus("current")
_RlSslCertificateImportId_Type = Integer32
_RlSslCertificateImportId_Object = MibTableColumn
rlSslCertificateImportId = _RlSslCertificateImportId_Object(
    (1, 3, 6, 1, 4, 1, 89, 100, 6, 1, 1),
    _RlSslCertificateImportId_Type()
)
rlSslCertificateImportId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSslCertificateImportId.setStatus("current")


class _RlSslCertificateImportFormat_Type(Integer32):
    """Custom type rlSslCertificateImportFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pkcs12", 2),
          ("x509", 1))
    )


_RlSslCertificateImportFormat_Type.__name__ = "Integer32"
_RlSslCertificateImportFormat_Object = MibTableColumn
rlSslCertificateImportFormat = _RlSslCertificateImportFormat_Object(
    (1, 3, 6, 1, 4, 1, 89, 100, 6, 1, 2),
    _RlSslCertificateImportFormat_Type()
)
rlSslCertificateImportFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSslCertificateImportFormat.setStatus("current")
_RlSslCertificateImportFragmentId_Type = Integer32
_RlSslCertificateImportFragmentId_Object = MibTableColumn
rlSslCertificateImportFragmentId = _RlSslCertificateImportFragmentId_Object(
    (1, 3, 6, 1, 4, 1, 89, 100, 6, 1, 3),
    _RlSslCertificateImportFragmentId_Type()
)
rlSslCertificateImportFragmentId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSslCertificateImportFragmentId.setStatus("current")
_RlSslCertificateImportFragmentText_Type = OctetString
_RlSslCertificateImportFragmentText_Object = MibTableColumn
rlSslCertificateImportFragmentText = _RlSslCertificateImportFragmentText_Object(
    (1, 3, 6, 1, 4, 1, 89, 100, 6, 1, 4),
    _RlSslCertificateImportFragmentText_Type()
)
rlSslCertificateImportFragmentText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSslCertificateImportFragmentText.setStatus("current")
_RlSslCertificateImportFragmentStatus_Type = RowStatus
_RlSslCertificateImportFragmentStatus_Object = MibTableColumn
rlSslCertificateImportFragmentStatus = _RlSslCertificateImportFragmentStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 100, 6, 1, 5),
    _RlSslCertificateImportFragmentStatus_Type()
)
rlSslCertificateImportFragmentStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSslCertificateImportFragmentStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RADLAN-SSL",
    **{"rlSsl": rlSsl,
       "rlSslCertificateGenerationTable": rlSslCertificateGenerationTable,
       "rlSslCertificateGenerationEntry": rlSslCertificateGenerationEntry,
       "rlSslCertificateGenerationIndex": rlSslCertificateGenerationIndex,
       "rlSslCertificateGenerationId": rlSslCertificateGenerationId,
       "rlSslCertificateGenerationCountryName": rlSslCertificateGenerationCountryName,
       "rlSslCertificateGenerationStateOrProvinceName": rlSslCertificateGenerationStateOrProvinceName,
       "rlSslCertificateGenerationLocalityName": rlSslCertificateGenerationLocalityName,
       "rlSslCertificateGenerationOrganizationName": rlSslCertificateGenerationOrganizationName,
       "rlSslCertificateGenerationOrganizationUnitName": rlSslCertificateGenerationOrganizationUnitName,
       "rlSslCertificateGenerationCommonName": rlSslCertificateGenerationCommonName,
       "rlSslCertificateGenerationValidDays": rlSslCertificateGenerationValidDays,
       "rlSslCertificateGenerationRsaKeyLength": rlSslCertificateGenerationRsaKeyLength,
       "rlSslCertificateGenerationPassphrase": rlSslCertificateGenerationPassphrase,
       "rlSslCertificateGenerationAction": rlSslCertificateGenerationAction,
       "rlSslCertificateExportTable": rlSslCertificateExportTable,
       "rlSslCertificateExportEntry": rlSslCertificateExportEntry,
       "rlSslCertificateExportId": rlSslCertificateExportId,
       "rlSslCertificateExportType": rlSslCertificateExportType,
       "rlSslCertificateExportFragmentId": rlSslCertificateExportFragmentId,
       "rlSslCertificateExportFragmentText": rlSslCertificateExportFragmentText,
       "rlSslCertificateSave": rlSslCertificateSave,
       "rlSslCertificateSaveFormat": rlSslCertificateSaveFormat,
       "rlSslImportedPKCS12CertificatePassphrase": rlSslImportedPKCS12CertificatePassphrase,
       "rlSslCertificateImportTable": rlSslCertificateImportTable,
       "rlSslCertificateImportEntry": rlSslCertificateImportEntry,
       "rlSslCertificateImportId": rlSslCertificateImportId,
       "rlSslCertificateImportFormat": rlSslCertificateImportFormat,
       "rlSslCertificateImportFragmentId": rlSslCertificateImportFragmentId,
       "rlSslCertificateImportFragmentText": rlSslCertificateImportFragmentText,
       "rlSslCertificateImportFragmentStatus": rlSslCertificateImportFragmentStatus}
)
