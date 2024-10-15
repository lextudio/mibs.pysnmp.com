# SNMP MIB module (SWAPCOM-SNMP) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SWAPCOM-SNMP
# Produced by pysmi-1.5.4 at Mon Oct 14 22:59:07 2024
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
 enterprises,
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
    "enterprises",
    "iso")

(DateAndTime,
 DisplayString,
 MacAddress,
 RowStatus,
 StorageType,
 TextualConvention,
 TestAndIncr,
 TimeInterval,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TestAndIncr",
    "TimeInterval",
    "TruthValue")


# MODULE-IDENTITY

swapcom = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11308)
)
swapcom.setRevisions(
        ("2005-07-13 18:17",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Org_ObjectIdentity = ObjectIdentity
org = _Org_ObjectIdentity(
    (1, 3)
)
_Dod_ObjectIdentity = ObjectIdentity
dod = _Dod_ObjectIdentity(
    (1, 3, 6)
)
_Internet_ObjectIdentity = ObjectIdentity
internet = _Internet_ObjectIdentity(
    (1, 3, 6, 1)
)
_Private_ObjectIdentity = ObjectIdentity
private = _Private_ObjectIdentity(
    (1, 3, 6, 1, 4)
)
_Enterprises_ObjectIdentity = ObjectIdentity
enterprises = _Enterprises_ObjectIdentity(
    (1, 3, 6, 1, 4, 1)
)
_Snmp_ObjectIdentity = ObjectIdentity
snmp = _Snmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11308, 2)
)
_Platform_ObjectIdentity = ObjectIdentity
platform = _Platform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11308, 2, 1)
)
_NotificationGroup_ObjectIdentity = ObjectIdentity
notificationGroup = _NotificationGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11308, 2, 1, 1)
)
_NotificationMessage_Type = DisplayString
_NotificationMessage_Object = MibScalar
notificationMessage = _NotificationMessage_Object(
    (1, 3, 6, 1, 4, 1, 11308, 2, 1, 1, 2),
    _NotificationMessage_Type()
)
notificationMessage.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    notificationMessage.setStatus("current")
_PlatformPlatformId_Type = DisplayString
_PlatformPlatformId_Object = MibScalar
platformPlatformId = _PlatformPlatformId_Object(
    (1, 3, 6, 1, 4, 1, 11308, 2, 1, 2),
    _PlatformPlatformId_Type()
)
platformPlatformId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    platformPlatformId.setStatus("current")


class _PlatformPlatformStatus_Type(Integer32):
    """Custom type platformPlatformStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("domains-initializing", 2),
          ("platform-initialized", 1),
          ("platform-initializing", 0),
          ("started", 3))
    )


_PlatformPlatformStatus_Type.__name__ = "Integer32"
_PlatformPlatformStatus_Object = MibScalar
platformPlatformStatus = _PlatformPlatformStatus_Object(
    (1, 3, 6, 1, 4, 1, 11308, 2, 1, 3),
    _PlatformPlatformStatus_Type()
)
platformPlatformStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    platformPlatformStatus.setStatus("current")
_PlatformVersion_ObjectIdentity = ObjectIdentity
platformVersion = _PlatformVersion_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11308, 2, 1, 6)
)
_PlatformVersionProductName_Type = DisplayString
_PlatformVersionProductName_Object = MibScalar
platformVersionProductName = _PlatformVersionProductName_Object(
    (1, 3, 6, 1, 4, 1, 11308, 2, 1, 6, 1),
    _PlatformVersionProductName_Type()
)
platformVersionProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    platformVersionProductName.setStatus("current")
_PlatformVersionProductVersion_Type = DisplayString
_PlatformVersionProductVersion_Object = MibScalar
platformVersionProductVersion = _PlatformVersionProductVersion_Object(
    (1, 3, 6, 1, 4, 1, 11308, 2, 1, 6, 2),
    _PlatformVersionProductVersion_Type()
)
platformVersionProductVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    platformVersionProductVersion.setStatus("current")
_PlatformVersionBuildNumber_Type = Integer32
_PlatformVersionBuildNumber_Object = MibScalar
platformVersionBuildNumber = _PlatformVersionBuildNumber_Object(
    (1, 3, 6, 1, 4, 1, 11308, 2, 1, 6, 3),
    _PlatformVersionBuildNumber_Type()
)
platformVersionBuildNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    platformVersionBuildNumber.setStatus("current")
_PlatformVersionBuildDate_Type = DisplayString
_PlatformVersionBuildDate_Object = MibScalar
platformVersionBuildDate = _PlatformVersionBuildDate_Object(
    (1, 3, 6, 1, 4, 1, 11308, 2, 1, 6, 4),
    _PlatformVersionBuildDate_Type()
)
platformVersionBuildDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    platformVersionBuildDate.setStatus("current")
_ApplicationVersion_ObjectIdentity = ObjectIdentity
applicationVersion = _ApplicationVersion_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11308, 2, 1, 7)
)
_ApplicationVersionProductName_Type = DisplayString
_ApplicationVersionProductName_Object = MibScalar
applicationVersionProductName = _ApplicationVersionProductName_Object(
    (1, 3, 6, 1, 4, 1, 11308, 2, 1, 7, 1),
    _ApplicationVersionProductName_Type()
)
applicationVersionProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationVersionProductName.setStatus("current")
_ApplicationVersionProductVersion_Type = DisplayString
_ApplicationVersionProductVersion_Object = MibScalar
applicationVersionProductVersion = _ApplicationVersionProductVersion_Object(
    (1, 3, 6, 1, 4, 1, 11308, 2, 1, 7, 2),
    _ApplicationVersionProductVersion_Type()
)
applicationVersionProductVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationVersionProductVersion.setStatus("current")
_ApplicationVersionBuildNumber_Type = Integer32
_ApplicationVersionBuildNumber_Object = MibScalar
applicationVersionBuildNumber = _ApplicationVersionBuildNumber_Object(
    (1, 3, 6, 1, 4, 1, 11308, 2, 1, 7, 3),
    _ApplicationVersionBuildNumber_Type()
)
applicationVersionBuildNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationVersionBuildNumber.setStatus("current")
_ApplicationVersionBuildDate_Type = DisplayString
_ApplicationVersionBuildDate_Object = MibScalar
applicationVersionBuildDate = _ApplicationVersionBuildDate_Object(
    (1, 3, 6, 1, 4, 1, 11308, 2, 1, 7, 4),
    _ApplicationVersionBuildDate_Type()
)
applicationVersionBuildDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationVersionBuildDate.setStatus("current")
_Logger_ObjectIdentity = ObjectIdentity
logger = _Logger_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11308, 2, 1, 8)
)
_RemotePlatform_ObjectIdentity = ObjectIdentity
remotePlatform = _RemotePlatform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11308, 2, 1, 9)
)
_RemotePlatformTable_Object = MibTable
remotePlatformTable = _RemotePlatformTable_Object(
    (1, 3, 6, 1, 4, 1, 11308, 2, 1, 9, 1)
)
if mibBuilder.loadTexts:
    remotePlatformTable.setStatus("current")
_RemotePlatformEntry_Object = MibTableRow
remotePlatformEntry = _RemotePlatformEntry_Object(
    (1, 3, 6, 1, 4, 1, 11308, 2, 1, 9, 1, 1)
)
remotePlatformEntry.setIndexNames(
    (0, "SWAPCOM-SNMP", "remotePlatformPlatformId"),
)
if mibBuilder.loadTexts:
    remotePlatformEntry.setStatus("current")
_RemotePlatformPlatformId_Type = DisplayString
_RemotePlatformPlatformId_Object = MibTableColumn
remotePlatformPlatformId = _RemotePlatformPlatformId_Object(
    (1, 3, 6, 1, 4, 1, 11308, 2, 1, 9, 1, 1, 1),
    _RemotePlatformPlatformId_Type()
)
remotePlatformPlatformId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remotePlatformPlatformId.setStatus("current")
_RemotePlatformPlatformProtocol_Type = DisplayString
_RemotePlatformPlatformProtocol_Object = MibTableColumn
remotePlatformPlatformProtocol = _RemotePlatformPlatformProtocol_Object(
    (1, 3, 6, 1, 4, 1, 11308, 2, 1, 9, 1, 1, 2),
    _RemotePlatformPlatformProtocol_Type()
)
remotePlatformPlatformProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remotePlatformPlatformProtocol.setStatus("current")


class _RemotePlatformPlatformStatus_Type(Integer32):
    """Custom type remotePlatformPlatformStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("unknown", 0),
          ("up", 1))
    )


_RemotePlatformPlatformStatus_Type.__name__ = "Integer32"
_RemotePlatformPlatformStatus_Object = MibTableColumn
remotePlatformPlatformStatus = _RemotePlatformPlatformStatus_Object(
    (1, 3, 6, 1, 4, 1, 11308, 2, 1, 9, 1, 1, 3),
    _RemotePlatformPlatformStatus_Type()
)
remotePlatformPlatformStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remotePlatformPlatformStatus.setStatus("current")

# Managed Objects groups


# Notification objects

defaultNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 11308, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    defaultNotification.setStatus(
        "current"
    )

platformStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 11308, 2, 1, 4)
)
if mibBuilder.loadTexts:
    platformStart.setStatus(
        "current"
    )

platformStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 11308, 2, 1, 5)
)
if mibBuilder.loadTexts:
    platformStop.setStatus(
        "current"
    )

unknownLog = NotificationType(
    (1, 3, 6, 1, 4, 1, 11308, 2, 1, 8, 1)
)
if mibBuilder.loadTexts:
    unknownLog.setStatus(
        "current"
    )

infoLog = NotificationType(
    (1, 3, 6, 1, 4, 1, 11308, 2, 1, 8, 2)
)
if mibBuilder.loadTexts:
    infoLog.setStatus(
        "current"
    )

warnLog = NotificationType(
    (1, 3, 6, 1, 4, 1, 11308, 2, 1, 8, 3)
)
if mibBuilder.loadTexts:
    warnLog.setStatus(
        "current"
    )

errorLog = NotificationType(
    (1, 3, 6, 1, 4, 1, 11308, 2, 1, 8, 4)
)
if mibBuilder.loadTexts:
    errorLog.setStatus(
        "current"
    )

fatalLog = NotificationType(
    (1, 3, 6, 1, 4, 1, 11308, 2, 1, 8, 5)
)
if mibBuilder.loadTexts:
    fatalLog.setStatus(
        "current"
    )

remotePlatformUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 11308, 2, 1, 9, 2)
)
if mibBuilder.loadTexts:
    remotePlatformUp.setStatus(
        "current"
    )

remotePlatformDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 11308, 2, 1, 9, 3)
)
if mibBuilder.loadTexts:
    remotePlatformDown.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SWAPCOM-SNMP",
    **{"org": org,
       "dod": dod,
       "internet": internet,
       "private": private,
       "enterprises": enterprises,
       "swapcom": swapcom,
       "snmp": snmp,
       "platform": platform,
       "notificationGroup": notificationGroup,
       "defaultNotification": defaultNotification,
       "notificationMessage": notificationMessage,
       "platformPlatformId": platformPlatformId,
       "platformPlatformStatus": platformPlatformStatus,
       "platformStart": platformStart,
       "platformStop": platformStop,
       "platformVersion": platformVersion,
       "platformVersionProductName": platformVersionProductName,
       "platformVersionProductVersion": platformVersionProductVersion,
       "platformVersionBuildNumber": platformVersionBuildNumber,
       "platformVersionBuildDate": platformVersionBuildDate,
       "applicationVersion": applicationVersion,
       "applicationVersionProductName": applicationVersionProductName,
       "applicationVersionProductVersion": applicationVersionProductVersion,
       "applicationVersionBuildNumber": applicationVersionBuildNumber,
       "applicationVersionBuildDate": applicationVersionBuildDate,
       "logger": logger,
       "unknownLog": unknownLog,
       "infoLog": infoLog,
       "warnLog": warnLog,
       "errorLog": errorLog,
       "fatalLog": fatalLog,
       "remotePlatform": remotePlatform,
       "remotePlatformTable": remotePlatformTable,
       "remotePlatformEntry": remotePlatformEntry,
       "remotePlatformPlatformId": remotePlatformPlatformId,
       "remotePlatformPlatformProtocol": remotePlatformPlatformProtocol,
       "remotePlatformPlatformStatus": remotePlatformPlatformStatus,
       "remotePlatformUp": remotePlatformUp,
       "remotePlatformDown": remotePlatformDown}
)
