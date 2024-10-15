# SNMP MIB module (SNMP-USER-BASED-SM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SNMP-USER-BASED-SM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:43:40 2024
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

(SnmpAdminString,
 SnmpEngineID,
 snmpAuthProtocols,
 snmpPrivProtocols) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString",
    "SnmpEngineID",
    "snmpAuthProtocols",
    "snmpPrivProtocols")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 iso,
 snmpModules) = mibBuilder.importSymbols(
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
    "iso",
    "snmpModules")

(AutonomousType,
 DisplayString,
 RowPointer,
 RowStatus,
 StorageType,
 TextualConvention,
 TestAndIncr) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "AutonomousType",
    "DisplayString",
    "RowPointer",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TestAndIncr")


# MODULE-IDENTITY

snmpUsmMIB = ModuleIdentity(
    (1, 3, 6, 1, 6, 3, 15)
)
snmpUsmMIB.setRevisions(
        ("2002-10-16 00:00",
         "1999-01-20 00:00",
         "1997-11-20 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class KeyChange(OctetString, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_UsmNoAuthProtocol_ObjectIdentity = ObjectIdentity
usmNoAuthProtocol = _UsmNoAuthProtocol_ObjectIdentity(
    (1, 3, 6, 1, 6, 3, 10, 1, 1, 1)
)
if mibBuilder.loadTexts:
    usmNoAuthProtocol.setStatus("current")
_UsmHMACMD5AuthProtocol_ObjectIdentity = ObjectIdentity
usmHMACMD5AuthProtocol = _UsmHMACMD5AuthProtocol_ObjectIdentity(
    (1, 3, 6, 1, 6, 3, 10, 1, 1, 2)
)
if mibBuilder.loadTexts:
    usmHMACMD5AuthProtocol.setStatus("current")
_UsmHMACSHAAuthProtocol_ObjectIdentity = ObjectIdentity
usmHMACSHAAuthProtocol = _UsmHMACSHAAuthProtocol_ObjectIdentity(
    (1, 3, 6, 1, 6, 3, 10, 1, 1, 3)
)
if mibBuilder.loadTexts:
    usmHMACSHAAuthProtocol.setStatus("current")
_UsmNoPrivProtocol_ObjectIdentity = ObjectIdentity
usmNoPrivProtocol = _UsmNoPrivProtocol_ObjectIdentity(
    (1, 3, 6, 1, 6, 3, 10, 1, 2, 1)
)
if mibBuilder.loadTexts:
    usmNoPrivProtocol.setStatus("current")
_UsmDESPrivProtocol_ObjectIdentity = ObjectIdentity
usmDESPrivProtocol = _UsmDESPrivProtocol_ObjectIdentity(
    (1, 3, 6, 1, 6, 3, 10, 1, 2, 2)
)
if mibBuilder.loadTexts:
    usmDESPrivProtocol.setStatus("current")
_UsmMIBObjects_ObjectIdentity = ObjectIdentity
usmMIBObjects = _UsmMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 6, 3, 15, 1)
)
_UsmStats_ObjectIdentity = ObjectIdentity
usmStats = _UsmStats_ObjectIdentity(
    (1, 3, 6, 1, 6, 3, 15, 1, 1)
)
_UsmStatsUnsupportedSecLevels_Type = Counter32
_UsmStatsUnsupportedSecLevels_Object = MibScalar
usmStatsUnsupportedSecLevels = _UsmStatsUnsupportedSecLevels_Object(
    (1, 3, 6, 1, 6, 3, 15, 1, 1, 1),
    _UsmStatsUnsupportedSecLevels_Type()
)
usmStatsUnsupportedSecLevels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usmStatsUnsupportedSecLevels.setStatus("current")
_UsmStatsNotInTimeWindows_Type = Counter32
_UsmStatsNotInTimeWindows_Object = MibScalar
usmStatsNotInTimeWindows = _UsmStatsNotInTimeWindows_Object(
    (1, 3, 6, 1, 6, 3, 15, 1, 1, 2),
    _UsmStatsNotInTimeWindows_Type()
)
usmStatsNotInTimeWindows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usmStatsNotInTimeWindows.setStatus("current")
_UsmStatsUnknownUserNames_Type = Counter32
_UsmStatsUnknownUserNames_Object = MibScalar
usmStatsUnknownUserNames = _UsmStatsUnknownUserNames_Object(
    (1, 3, 6, 1, 6, 3, 15, 1, 1, 3),
    _UsmStatsUnknownUserNames_Type()
)
usmStatsUnknownUserNames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usmStatsUnknownUserNames.setStatus("current")
_UsmStatsUnknownEngineIDs_Type = Counter32
_UsmStatsUnknownEngineIDs_Object = MibScalar
usmStatsUnknownEngineIDs = _UsmStatsUnknownEngineIDs_Object(
    (1, 3, 6, 1, 6, 3, 15, 1, 1, 4),
    _UsmStatsUnknownEngineIDs_Type()
)
usmStatsUnknownEngineIDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usmStatsUnknownEngineIDs.setStatus("current")
_UsmStatsWrongDigests_Type = Counter32
_UsmStatsWrongDigests_Object = MibScalar
usmStatsWrongDigests = _UsmStatsWrongDigests_Object(
    (1, 3, 6, 1, 6, 3, 15, 1, 1, 5),
    _UsmStatsWrongDigests_Type()
)
usmStatsWrongDigests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usmStatsWrongDigests.setStatus("current")
_UsmStatsDecryptionErrors_Type = Counter32
_UsmStatsDecryptionErrors_Object = MibScalar
usmStatsDecryptionErrors = _UsmStatsDecryptionErrors_Object(
    (1, 3, 6, 1, 6, 3, 15, 1, 1, 6),
    _UsmStatsDecryptionErrors_Type()
)
usmStatsDecryptionErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usmStatsDecryptionErrors.setStatus("current")
_UsmUser_ObjectIdentity = ObjectIdentity
usmUser = _UsmUser_ObjectIdentity(
    (1, 3, 6, 1, 6, 3, 15, 1, 2)
)
_UsmUserSpinLock_Type = TestAndIncr
_UsmUserSpinLock_Object = MibScalar
usmUserSpinLock = _UsmUserSpinLock_Object(
    (1, 3, 6, 1, 6, 3, 15, 1, 2, 1),
    _UsmUserSpinLock_Type()
)
usmUserSpinLock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usmUserSpinLock.setStatus("current")
_UsmUserTable_Object = MibTable
usmUserTable = _UsmUserTable_Object(
    (1, 3, 6, 1, 6, 3, 15, 1, 2, 2)
)
if mibBuilder.loadTexts:
    usmUserTable.setStatus("current")
_UsmUserEntry_Object = MibTableRow
usmUserEntry = _UsmUserEntry_Object(
    (1, 3, 6, 1, 6, 3, 15, 1, 2, 2, 1)
)
usmUserEntry.setIndexNames(
    (0, "SNMP-USER-BASED-SM-MIB", "usmUserEngineID"),
    (0, "SNMP-USER-BASED-SM-MIB", "usmUserName"),
)
if mibBuilder.loadTexts:
    usmUserEntry.setStatus("current")
_UsmUserEngineID_Type = SnmpEngineID
_UsmUserEngineID_Object = MibTableColumn
usmUserEngineID = _UsmUserEngineID_Object(
    (1, 3, 6, 1, 6, 3, 15, 1, 2, 2, 1, 1),
    _UsmUserEngineID_Type()
)
usmUserEngineID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usmUserEngineID.setStatus("current")


class _UsmUserName_Type(SnmpAdminString):
    """Custom type usmUserName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_UsmUserName_Type.__name__ = "SnmpAdminString"
_UsmUserName_Object = MibTableColumn
usmUserName = _UsmUserName_Object(
    (1, 3, 6, 1, 6, 3, 15, 1, 2, 2, 1, 2),
    _UsmUserName_Type()
)
usmUserName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usmUserName.setStatus("current")
_UsmUserSecurityName_Type = SnmpAdminString
_UsmUserSecurityName_Object = MibTableColumn
usmUserSecurityName = _UsmUserSecurityName_Object(
    (1, 3, 6, 1, 6, 3, 15, 1, 2, 2, 1, 3),
    _UsmUserSecurityName_Type()
)
usmUserSecurityName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usmUserSecurityName.setStatus("current")
_UsmUserCloneFrom_Type = RowPointer
_UsmUserCloneFrom_Object = MibTableColumn
usmUserCloneFrom = _UsmUserCloneFrom_Object(
    (1, 3, 6, 1, 6, 3, 15, 1, 2, 2, 1, 4),
    _UsmUserCloneFrom_Type()
)
usmUserCloneFrom.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usmUserCloneFrom.setStatus("current")


class _UsmUserAuthProtocol_Type(AutonomousType):
    """Custom type usmUserAuthProtocol based on AutonomousType"""
    defaultValue = (1, 3, 6, 1, 6, 3, 10, 1, 1, 1)


_UsmUserAuthProtocol_Object = MibTableColumn
usmUserAuthProtocol = _UsmUserAuthProtocol_Object(
    (1, 3, 6, 1, 6, 3, 15, 1, 2, 2, 1, 5),
    _UsmUserAuthProtocol_Type()
)
usmUserAuthProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usmUserAuthProtocol.setStatus("current")


class _UsmUserAuthKeyChange_Type(KeyChange):
    """Custom type usmUserAuthKeyChange based on KeyChange"""
    defaultHexValue = ""


_UsmUserAuthKeyChange_Object = MibTableColumn
usmUserAuthKeyChange = _UsmUserAuthKeyChange_Object(
    (1, 3, 6, 1, 6, 3, 15, 1, 2, 2, 1, 6),
    _UsmUserAuthKeyChange_Type()
)
usmUserAuthKeyChange.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usmUserAuthKeyChange.setStatus("current")


class _UsmUserOwnAuthKeyChange_Type(KeyChange):
    """Custom type usmUserOwnAuthKeyChange based on KeyChange"""
    defaultHexValue = ""


_UsmUserOwnAuthKeyChange_Object = MibTableColumn
usmUserOwnAuthKeyChange = _UsmUserOwnAuthKeyChange_Object(
    (1, 3, 6, 1, 6, 3, 15, 1, 2, 2, 1, 7),
    _UsmUserOwnAuthKeyChange_Type()
)
usmUserOwnAuthKeyChange.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usmUserOwnAuthKeyChange.setStatus("current")


class _UsmUserPrivProtocol_Type(AutonomousType):
    """Custom type usmUserPrivProtocol based on AutonomousType"""
    defaultValue = (1, 3, 6, 1, 6, 3, 10, 1, 2, 1)


_UsmUserPrivProtocol_Object = MibTableColumn
usmUserPrivProtocol = _UsmUserPrivProtocol_Object(
    (1, 3, 6, 1, 6, 3, 15, 1, 2, 2, 1, 8),
    _UsmUserPrivProtocol_Type()
)
usmUserPrivProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usmUserPrivProtocol.setStatus("current")


class _UsmUserPrivKeyChange_Type(KeyChange):
    """Custom type usmUserPrivKeyChange based on KeyChange"""
    defaultHexValue = ""


_UsmUserPrivKeyChange_Object = MibTableColumn
usmUserPrivKeyChange = _UsmUserPrivKeyChange_Object(
    (1, 3, 6, 1, 6, 3, 15, 1, 2, 2, 1, 9),
    _UsmUserPrivKeyChange_Type()
)
usmUserPrivKeyChange.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usmUserPrivKeyChange.setStatus("current")


class _UsmUserOwnPrivKeyChange_Type(KeyChange):
    """Custom type usmUserOwnPrivKeyChange based on KeyChange"""
    defaultHexValue = ""


_UsmUserOwnPrivKeyChange_Object = MibTableColumn
usmUserOwnPrivKeyChange = _UsmUserOwnPrivKeyChange_Object(
    (1, 3, 6, 1, 6, 3, 15, 1, 2, 2, 1, 10),
    _UsmUserOwnPrivKeyChange_Type()
)
usmUserOwnPrivKeyChange.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usmUserOwnPrivKeyChange.setStatus("current")


class _UsmUserPublic_Type(OctetString):
    """Custom type usmUserPublic based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_UsmUserPublic_Type.__name__ = "OctetString"
_UsmUserPublic_Object = MibTableColumn
usmUserPublic = _UsmUserPublic_Object(
    (1, 3, 6, 1, 6, 3, 15, 1, 2, 2, 1, 11),
    _UsmUserPublic_Type()
)
usmUserPublic.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usmUserPublic.setStatus("current")


class _UsmUserStorageType_Type(StorageType):
    """Custom type usmUserStorageType based on StorageType"""


_UsmUserStorageType_Object = MibTableColumn
usmUserStorageType = _UsmUserStorageType_Object(
    (1, 3, 6, 1, 6, 3, 15, 1, 2, 2, 1, 12),
    _UsmUserStorageType_Type()
)
usmUserStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usmUserStorageType.setStatus("current")
_UsmUserStatus_Type = RowStatus
_UsmUserStatus_Object = MibTableColumn
usmUserStatus = _UsmUserStatus_Object(
    (1, 3, 6, 1, 6, 3, 15, 1, 2, 2, 1, 13),
    _UsmUserStatus_Type()
)
usmUserStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usmUserStatus.setStatus("current")
_UsmMIBConformance_ObjectIdentity = ObjectIdentity
usmMIBConformance = _UsmMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 6, 3, 15, 2)
)
_UsmMIBCompliances_ObjectIdentity = ObjectIdentity
usmMIBCompliances = _UsmMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 6, 3, 15, 2, 1)
)
_UsmMIBGroups_ObjectIdentity = ObjectIdentity
usmMIBGroups = _UsmMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 6, 3, 15, 2, 2)
)

# Managed Objects groups

usmMIBBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 6, 3, 15, 2, 2, 1)
)
usmMIBBasicGroup.setObjects(
      *(("SNMP-USER-BASED-SM-MIB", "usmStatsUnsupportedSecLevels"),
        ("SNMP-USER-BASED-SM-MIB", "usmStatsNotInTimeWindows"),
        ("SNMP-USER-BASED-SM-MIB", "usmStatsUnknownUserNames"),
        ("SNMP-USER-BASED-SM-MIB", "usmStatsUnknownEngineIDs"),
        ("SNMP-USER-BASED-SM-MIB", "usmStatsWrongDigests"),
        ("SNMP-USER-BASED-SM-MIB", "usmStatsDecryptionErrors"),
        ("SNMP-USER-BASED-SM-MIB", "usmUserSpinLock"),
        ("SNMP-USER-BASED-SM-MIB", "usmUserSecurityName"),
        ("SNMP-USER-BASED-SM-MIB", "usmUserCloneFrom"),
        ("SNMP-USER-BASED-SM-MIB", "usmUserAuthProtocol"),
        ("SNMP-USER-BASED-SM-MIB", "usmUserAuthKeyChange"),
        ("SNMP-USER-BASED-SM-MIB", "usmUserOwnAuthKeyChange"),
        ("SNMP-USER-BASED-SM-MIB", "usmUserPrivProtocol"),
        ("SNMP-USER-BASED-SM-MIB", "usmUserPrivKeyChange"),
        ("SNMP-USER-BASED-SM-MIB", "usmUserOwnPrivKeyChange"),
        ("SNMP-USER-BASED-SM-MIB", "usmUserPublic"),
        ("SNMP-USER-BASED-SM-MIB", "usmUserStorageType"),
        ("SNMP-USER-BASED-SM-MIB", "usmUserStatus"))
)
if mibBuilder.loadTexts:
    usmMIBBasicGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

usmMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 6, 3, 15, 2, 1, 1)
)
if mibBuilder.loadTexts:
    usmMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SNMP-USER-BASED-SM-MIB",
    **{"KeyChange": KeyChange,
       "usmNoAuthProtocol": usmNoAuthProtocol,
       "usmHMACMD5AuthProtocol": usmHMACMD5AuthProtocol,
       "usmHMACSHAAuthProtocol": usmHMACSHAAuthProtocol,
       "usmNoPrivProtocol": usmNoPrivProtocol,
       "usmDESPrivProtocol": usmDESPrivProtocol,
       "snmpUsmMIB": snmpUsmMIB,
       "usmMIBObjects": usmMIBObjects,
       "usmStats": usmStats,
       "usmStatsUnsupportedSecLevels": usmStatsUnsupportedSecLevels,
       "usmStatsNotInTimeWindows": usmStatsNotInTimeWindows,
       "usmStatsUnknownUserNames": usmStatsUnknownUserNames,
       "usmStatsUnknownEngineIDs": usmStatsUnknownEngineIDs,
       "usmStatsWrongDigests": usmStatsWrongDigests,
       "usmStatsDecryptionErrors": usmStatsDecryptionErrors,
       "usmUser": usmUser,
       "usmUserSpinLock": usmUserSpinLock,
       "usmUserTable": usmUserTable,
       "usmUserEntry": usmUserEntry,
       "usmUserEngineID": usmUserEngineID,
       "usmUserName": usmUserName,
       "usmUserSecurityName": usmUserSecurityName,
       "usmUserCloneFrom": usmUserCloneFrom,
       "usmUserAuthProtocol": usmUserAuthProtocol,
       "usmUserAuthKeyChange": usmUserAuthKeyChange,
       "usmUserOwnAuthKeyChange": usmUserOwnAuthKeyChange,
       "usmUserPrivProtocol": usmUserPrivProtocol,
       "usmUserPrivKeyChange": usmUserPrivKeyChange,
       "usmUserOwnPrivKeyChange": usmUserOwnPrivKeyChange,
       "usmUserPublic": usmUserPublic,
       "usmUserStorageType": usmUserStorageType,
       "usmUserStatus": usmUserStatus,
       "usmMIBConformance": usmMIBConformance,
       "usmMIBCompliances": usmMIBCompliances,
       "usmMIBCompliance": usmMIBCompliance,
       "usmMIBGroups": usmMIBGroups,
       "usmMIBBasicGroup": usmMIBBasicGroup}
)
