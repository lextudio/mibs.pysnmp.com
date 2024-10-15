# SNMP MIB module (BLUECOAT-AV-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BLUECOAT-AV-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:48:15 2024
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

(blueCoatMgmt,) = mibBuilder.importSymbols(
    "BLUECOAT-MIB",
    "blueCoatMgmt")

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

(DateAndTime,
 DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

blueCoatAvMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 2, 10)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BlueCoatAvMibObjects_ObjectIdentity = ObjectIdentity
blueCoatAvMibObjects = _BlueCoatAvMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 2, 10, 1)
)
_AvFilesScanned_Type = Counter32
_AvFilesScanned_Object = MibScalar
avFilesScanned = _AvFilesScanned_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 10, 1, 1),
    _AvFilesScanned_Type()
)
avFilesScanned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avFilesScanned.setStatus("current")
_AvVirusesDetected_Type = Counter32
_AvVirusesDetected_Object = MibScalar
avVirusesDetected = _AvVirusesDetected_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 10, 1, 2),
    _AvVirusesDetected_Type()
)
avVirusesDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avVirusesDetected.setStatus("current")
_AvPatternVersion_Type = DisplayString
_AvPatternVersion_Object = MibScalar
avPatternVersion = _AvPatternVersion_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 10, 1, 3),
    _AvPatternVersion_Type()
)
avPatternVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avPatternVersion.setStatus("current")
_AvPatternDateTime_Type = DateAndTime
_AvPatternDateTime_Object = MibScalar
avPatternDateTime = _AvPatternDateTime_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 10, 1, 4),
    _AvPatternDateTime_Type()
)
avPatternDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avPatternDateTime.setStatus("current")
_AvEngineVersion_Type = DisplayString
_AvEngineVersion_Object = MibScalar
avEngineVersion = _AvEngineVersion_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 10, 1, 5),
    _AvEngineVersion_Type()
)
avEngineVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avEngineVersion.setStatus("current")
_AvVendorName_Type = DisplayString
_AvVendorName_Object = MibScalar
avVendorName = _AvVendorName_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 10, 1, 6),
    _AvVendorName_Type()
)
avVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avVendorName.setStatus("current")
_AvLicenseDaysRemaining_Type = Integer32
_AvLicenseDaysRemaining_Object = MibScalar
avLicenseDaysRemaining = _AvLicenseDaysRemaining_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 10, 1, 7),
    _AvLicenseDaysRemaining_Type()
)
avLicenseDaysRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avLicenseDaysRemaining.setStatus("current")
_AvPublishedFirmwareVersion_Type = DisplayString
_AvPublishedFirmwareVersion_Object = MibScalar
avPublishedFirmwareVersion = _AvPublishedFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 10, 1, 8),
    _AvPublishedFirmwareVersion_Type()
)
avPublishedFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avPublishedFirmwareVersion.setStatus("current")
_AvInstalledFirmwareVersion_Type = DisplayString
_AvInstalledFirmwareVersion_Object = MibScalar
avInstalledFirmwareVersion = _AvInstalledFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 10, 1, 9),
    _AvInstalledFirmwareVersion_Type()
)
avInstalledFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avInstalledFirmwareVersion.setStatus("current")
_AvSlowICAPConnections_Type = Gauge32
_AvSlowICAPConnections_Object = MibScalar
avSlowICAPConnections = _AvSlowICAPConnections_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 10, 1, 10),
    _AvSlowICAPConnections_Type()
)
avSlowICAPConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avSlowICAPConnections.setStatus("current")
_BlueCoatAvMibNotificationObjects_ObjectIdentity = ObjectIdentity
blueCoatAvMibNotificationObjects = _BlueCoatAvMibNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 2, 10, 2)
)
_AvUpdateFailureReason_Type = DisplayString
_AvUpdateFailureReason_Object = MibScalar
avUpdateFailureReason = _AvUpdateFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 10, 2, 1),
    _AvUpdateFailureReason_Type()
)
avUpdateFailureReason.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    avUpdateFailureReason.setStatus("current")
_AvUrl_Type = DisplayString
_AvUrl_Object = MibScalar
avUrl = _AvUrl_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 10, 2, 2),
    _AvUrl_Type()
)
avUrl.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    avUrl.setStatus("current")
_AvVirusName_Type = DisplayString
_AvVirusName_Object = MibScalar
avVirusName = _AvVirusName_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 10, 2, 3),
    _AvVirusName_Type()
)
avVirusName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    avVirusName.setStatus("current")
_AvVirusDetails_Type = DisplayString
_AvVirusDetails_Object = MibScalar
avVirusDetails = _AvVirusDetails_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 10, 2, 4),
    _AvVirusDetails_Type()
)
avVirusDetails.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    avVirusDetails.setStatus("current")
_AvErrorCode_Type = DisplayString
_AvErrorCode_Object = MibScalar
avErrorCode = _AvErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 10, 2, 5),
    _AvErrorCode_Type()
)
avErrorCode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    avErrorCode.setStatus("current")
_AvErrorDetails_Type = DisplayString
_AvErrorDetails_Object = MibScalar
avErrorDetails = _AvErrorDetails_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 10, 2, 6),
    _AvErrorDetails_Type()
)
avErrorDetails.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    avErrorDetails.setStatus("current")
_AvPreviousFirmwareVersion_Type = DisplayString
_AvPreviousFirmwareVersion_Object = MibScalar
avPreviousFirmwareVersion = _AvPreviousFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 10, 2, 7),
    _AvPreviousFirmwareVersion_Type()
)
avPreviousFirmwareVersion.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    avPreviousFirmwareVersion.setStatus("current")
_AvICTMWarningReason_Type = DisplayString
_AvICTMWarningReason_Object = MibScalar
avICTMWarningReason = _AvICTMWarningReason_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 10, 2, 8),
    _AvICTMWarningReason_Type()
)
avICTMWarningReason.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    avICTMWarningReason.setStatus("current")
_BlueCoatAvMibNotifications_ObjectIdentity = ObjectIdentity
blueCoatAvMibNotifications = _BlueCoatAvMibNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 2, 10, 3)
)

# Managed Objects groups


# Notification objects

avAntivirusUpdateSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 3417, 2, 10, 3, 1)
)
avAntivirusUpdateSuccess.setObjects(
      *(("BLUECOAT-AV-MIB", "avVendorName"),
        ("BLUECOAT-AV-MIB", "avEngineVersion"),
        ("BLUECOAT-AV-MIB", "avPatternVersion"),
        ("BLUECOAT-AV-MIB", "avPatternDateTime"))
)
if mibBuilder.loadTexts:
    avAntivirusUpdateSuccess.setStatus(
        "current"
    )

avAntivirusUpdateFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 3417, 2, 10, 3, 2)
)
avAntivirusUpdateFailed.setObjects(
      *(("BLUECOAT-AV-MIB", "avUpdateFailureReason"),
        ("BLUECOAT-AV-MIB", "avVendorName"),
        ("BLUECOAT-AV-MIB", "avEngineVersion"),
        ("BLUECOAT-AV-MIB", "avPatternVersion"),
        ("BLUECOAT-AV-MIB", "avPatternDateTime"))
)
if mibBuilder.loadTexts:
    avAntivirusUpdateFailed.setStatus(
        "current"
    )

avVirusDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 3417, 2, 10, 3, 3)
)
avVirusDetected.setObjects(
      *(("BLUECOAT-AV-MIB", "avUrl"),
        ("BLUECOAT-AV-MIB", "avVirusName"),
        ("BLUECOAT-AV-MIB", "avVirusDetails"))
)
if mibBuilder.loadTexts:
    avVirusDetected.setStatus(
        "current"
    )

avFileServed = NotificationType(
    (1, 3, 6, 1, 4, 1, 3417, 2, 10, 3, 4)
)
avFileServed.setObjects(
      *(("BLUECOAT-AV-MIB", "avUrl"),
        ("BLUECOAT-AV-MIB", "avErrorCode"),
        ("BLUECOAT-AV-MIB", "avErrorDetails"))
)
if mibBuilder.loadTexts:
    avFileServed.setStatus(
        "current"
    )

avFileBlocked = NotificationType(
    (1, 3, 6, 1, 4, 1, 3417, 2, 10, 3, 5)
)
avFileBlocked.setObjects(
      *(("BLUECOAT-AV-MIB", "avUrl"),
        ("BLUECOAT-AV-MIB", "avErrorCode"),
        ("BLUECOAT-AV-MIB", "avErrorDetails"))
)
if mibBuilder.loadTexts:
    avFileBlocked.setStatus(
        "current"
    )

avNewFirmwareAvailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 3417, 2, 10, 3, 6)
)
avNewFirmwareAvailable.setObjects(
      *(("BLUECOAT-AV-MIB", "avInstalledFirmwareVersion"),
        ("BLUECOAT-AV-MIB", "avPublishedFirmwareVersion"))
)
if mibBuilder.loadTexts:
    avNewFirmwareAvailable.setStatus(
        "current"
    )

avFirmwareUpdateSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 3417, 2, 10, 3, 7)
)
avFirmwareUpdateSuccess.setObjects(
      *(("BLUECOAT-AV-MIB", "avPreviousFirmwareVersion"),
        ("BLUECOAT-AV-MIB", "avInstalledFirmwareVersion"))
)
if mibBuilder.loadTexts:
    avFirmwareUpdateSuccess.setStatus(
        "current"
    )

avFirmwareUpdateFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 3417, 2, 10, 3, 8)
)
avFirmwareUpdateFailed.setObjects(
      *(("BLUECOAT-AV-MIB", "avInstalledFirmwareVersion"),
        ("BLUECOAT-AV-MIB", "avPublishedFirmwareVersion"),
        ("BLUECOAT-AV-MIB", "avUpdateFailureReason"))
)
if mibBuilder.loadTexts:
    avFirmwareUpdateFailed.setStatus(
        "current"
    )

avAntivirusLicenseWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 3417, 2, 10, 3, 9)
)
avAntivirusLicenseWarning.setObjects(
      *(("BLUECOAT-AV-MIB", "avVendorName"),
        ("BLUECOAT-AV-MIB", "avLicenseDaysRemaining"))
)
if mibBuilder.loadTexts:
    avAntivirusLicenseWarning.setStatus(
        "current"
    )

avICTMWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 3417, 2, 10, 3, 10)
)
avICTMWarning.setObjects(
      *(("BLUECOAT-AV-MIB", "avICTMWarningReason"),
        ("BLUECOAT-AV-MIB", "avSlowICAPConnections"))
)
if mibBuilder.loadTexts:
    avICTMWarning.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BLUECOAT-AV-MIB",
    **{"blueCoatAvMib": blueCoatAvMib,
       "blueCoatAvMibObjects": blueCoatAvMibObjects,
       "avFilesScanned": avFilesScanned,
       "avVirusesDetected": avVirusesDetected,
       "avPatternVersion": avPatternVersion,
       "avPatternDateTime": avPatternDateTime,
       "avEngineVersion": avEngineVersion,
       "avVendorName": avVendorName,
       "avLicenseDaysRemaining": avLicenseDaysRemaining,
       "avPublishedFirmwareVersion": avPublishedFirmwareVersion,
       "avInstalledFirmwareVersion": avInstalledFirmwareVersion,
       "avSlowICAPConnections": avSlowICAPConnections,
       "blueCoatAvMibNotificationObjects": blueCoatAvMibNotificationObjects,
       "avUpdateFailureReason": avUpdateFailureReason,
       "avUrl": avUrl,
       "avVirusName": avVirusName,
       "avVirusDetails": avVirusDetails,
       "avErrorCode": avErrorCode,
       "avErrorDetails": avErrorDetails,
       "avPreviousFirmwareVersion": avPreviousFirmwareVersion,
       "avICTMWarningReason": avICTMWarningReason,
       "blueCoatAvMibNotifications": blueCoatAvMibNotifications,
       "avAntivirusUpdateSuccess": avAntivirusUpdateSuccess,
       "avAntivirusUpdateFailed": avAntivirusUpdateFailed,
       "avVirusDetected": avVirusDetected,
       "avFileServed": avFileServed,
       "avFileBlocked": avFileBlocked,
       "avNewFirmwareAvailable": avNewFirmwareAvailable,
       "avFirmwareUpdateSuccess": avFirmwareUpdateSuccess,
       "avFirmwareUpdateFailed": avFirmwareUpdateFailed,
       "avAntivirusLicenseWarning": avAntivirusLicenseWarning,
       "avICTMWarning": avICTMWarning}
)
