# SNMP MIB module (CADANT-CMTS-EXPORTIMPORT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CADANT-CMTS-EXPORTIMPORT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:52:29 2024
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

(trapCounter,
 trapSeverity) = mibBuilder.importSymbols(
    "CADANT-CMTS-EQUIPMENT-MIB",
    "trapCounter",
    "trapSeverity")

(cadExperimental,) = mibBuilder.importSymbols(
    "CADANT-PRODUCTS-MIB",
    "cadExperimental")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

cadExportImportMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 1)
)
cadExportImportMib.setRevisions(
        ("2001-03-09 00:00",
         "2004-02-13 00:00",
         "2004-02-16 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class ExportImportAction(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("caCertExport", 4),
          ("export", 1),
          ("import", 2),
          ("noop", 0),
          ("pCmCertExport", 3))
    )



class ExportResult(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("fileNameTooLong", 2),
          ("fileSystemFull", 4),
          ("invalidCharactersInFilename", 3),
          ("otherError", 5),
          ("success", 1),
          ("unknown", 0))
    )



class ImportResult(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("fileDecodingError", 3),
          ("fileNotFound", 2),
          ("otherError", 4),
          ("success", 1),
          ("unknown", 0))
    )



# MIB Managed Objects in the order of their OIDs

_CadCmtsExportImportTraps_ObjectIdentity = ObjectIdentity
cadCmtsExportImportTraps = _CadCmtsExportImportTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 1, 0)
)
_CadCmtsExportImportGroup_ObjectIdentity = ObjectIdentity
cadCmtsExportImportGroup = _CadCmtsExportImportGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 1, 1)
)


class _CadCmtsExportImportFilename_Type(DisplayString):
    """Custom type cadCmtsExportImportFilename based on DisplayString"""
    defaultValue = OctetString("update:/export.txt")


_CadCmtsExportImportFilename_Object = MibScalar
cadCmtsExportImportFilename = _CadCmtsExportImportFilename_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 1, 1, 1),
    _CadCmtsExportImportFilename_Type()
)
cadCmtsExportImportFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadCmtsExportImportFilename.setStatus("current")


class _CadCmtsExportImportAction_Type(ExportImportAction):
    """Custom type cadCmtsExportImportAction based on ExportImportAction"""


_CadCmtsExportImportAction_Object = MibScalar
cadCmtsExportImportAction = _CadCmtsExportImportAction_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 1, 1, 2),
    _CadCmtsExportImportAction_Type()
)
cadCmtsExportImportAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadCmtsExportImportAction.setStatus("current")


class _CadCmtsExportResult_Type(ExportResult):
    """Custom type cadCmtsExportResult based on ExportResult"""


_CadCmtsExportResult_Object = MibScalar
cadCmtsExportResult = _CadCmtsExportResult_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 1, 1, 3),
    _CadCmtsExportResult_Type()
)
cadCmtsExportResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadCmtsExportResult.setStatus("current")


class _CadCmtsImportResult_Type(ImportResult):
    """Custom type cadCmtsImportResult based on ImportResult"""


_CadCmtsImportResult_Object = MibScalar
cadCmtsImportResult = _CadCmtsImportResult_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 1, 1, 4),
    _CadCmtsImportResult_Type()
)
cadCmtsImportResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadCmtsImportResult.setStatus("current")


class _CadCmtsExportImportWithLineNums_Type(TruthValue):
    """Custom type cadCmtsExportImportWithLineNums based on TruthValue"""


_CadCmtsExportImportWithLineNums_Object = MibScalar
cadCmtsExportImportWithLineNums = _CadCmtsExportImportWithLineNums_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 1, 1, 5),
    _CadCmtsExportImportWithLineNums_Type()
)
cadCmtsExportImportWithLineNums.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadCmtsExportImportWithLineNums.setStatus("current")


class _CadCmtsExportImportWithDefaults_Type(TruthValue):
    """Custom type cadCmtsExportImportWithDefaults based on TruthValue"""


_CadCmtsExportImportWithDefaults_Object = MibScalar
cadCmtsExportImportWithDefaults = _CadCmtsExportImportWithDefaults_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 1, 1, 6),
    _CadCmtsExportImportWithDefaults_Type()
)
cadCmtsExportImportWithDefaults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadCmtsExportImportWithDefaults.setStatus("current")


class _CadCmtsExportImportNested_Type(TruthValue):
    """Custom type cadCmtsExportImportNested based on TruthValue"""


_CadCmtsExportImportNested_Object = MibScalar
cadCmtsExportImportNested = _CadCmtsExportImportNested_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 1, 1, 7),
    _CadCmtsExportImportNested_Type()
)
cadCmtsExportImportNested.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadCmtsExportImportNested.setStatus("current")


class _CadCmtsExportImportWithCertificates_Type(TruthValue):
    """Custom type cadCmtsExportImportWithCertificates based on TruthValue"""


_CadCmtsExportImportWithCertificates_Object = MibScalar
cadCmtsExportImportWithCertificates = _CadCmtsExportImportWithCertificates_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 1, 1, 8),
    _CadCmtsExportImportWithCertificates_Type()
)
cadCmtsExportImportWithCertificates.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadCmtsExportImportWithCertificates.setStatus("current")


class _CadCmtsExportImportIfIndex_Type(InterfaceIndexOrZero):
    """Custom type cadCmtsExportImportIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_CadCmtsExportImportIfIndex_Object = MibScalar
cadCmtsExportImportIfIndex = _CadCmtsExportImportIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 1, 1, 9),
    _CadCmtsExportImportIfIndex_Type()
)
cadCmtsExportImportIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadCmtsExportImportIfIndex.setStatus("current")

# Managed Objects groups


# Notification objects

cadCmtsExportNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 1, 0, 1)
)
cadCmtsExportNotification.setObjects(
      *(("CADANT-CMTS-EQUIPMENT-MIB", "trapCounter"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "trapSeverity"),
        ("CADANT-CMTS-EXPORTIMPORT-MIB", "cadCmtsExportResult"))
)
if mibBuilder.loadTexts:
    cadCmtsExportNotification.setStatus(
        "current"
    )

cadCmtsImportNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 1, 0, 2)
)
cadCmtsImportNotification.setObjects(
      *(("CADANT-CMTS-EQUIPMENT-MIB", "trapCounter"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "trapSeverity"),
        ("CADANT-CMTS-EXPORTIMPORT-MIB", "cadCmtsImportResult"))
)
if mibBuilder.loadTexts:
    cadCmtsImportNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CADANT-CMTS-EXPORTIMPORT-MIB",
    **{"ExportImportAction": ExportImportAction,
       "ExportResult": ExportResult,
       "ImportResult": ImportResult,
       "cadExportImportMib": cadExportImportMib,
       "cadCmtsExportImportTraps": cadCmtsExportImportTraps,
       "cadCmtsExportNotification": cadCmtsExportNotification,
       "cadCmtsImportNotification": cadCmtsImportNotification,
       "cadCmtsExportImportGroup": cadCmtsExportImportGroup,
       "cadCmtsExportImportFilename": cadCmtsExportImportFilename,
       "cadCmtsExportImportAction": cadCmtsExportImportAction,
       "cadCmtsExportResult": cadCmtsExportResult,
       "cadCmtsImportResult": cadCmtsImportResult,
       "cadCmtsExportImportWithLineNums": cadCmtsExportImportWithLineNums,
       "cadCmtsExportImportWithDefaults": cadCmtsExportImportWithDefaults,
       "cadCmtsExportImportNested": cadCmtsExportImportNested,
       "cadCmtsExportImportWithCertificates": cadCmtsExportImportWithCertificates,
       "cadCmtsExportImportIfIndex": cadCmtsExportImportIfIndex}
)
