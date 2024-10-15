# SNMP MIB module (CISCO-NOTIFICATION-CONTROL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-NOTIFICATION-CONTROL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:06:15 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

(AutonomousType,
 DisplayString,
 RowStatus,
 StorageType,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "AutonomousType",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention")


# MODULE-IDENTITY

ciscoNotificationControlMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 586)
)
ciscoNotificationControlMIB.setRevisions(
        ("2009-09-20 00:00",
         "2006-09-27 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CNotifCtrlMIBObjects_ObjectIdentity = ObjectIdentity
cNotifCtrlMIBObjects = _CNotifCtrlMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 586, 1)
)
_CNotifCtrlConfig_ObjectIdentity = ObjectIdentity
cNotifCtrlConfig = _CNotifCtrlConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 586, 1, 1)
)


class _CNotifCtrlMode_Type(Integer32):
    """Custom type cNotifCtrlMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("automaticControl", 3),
          ("forcedControl", 2),
          ("noControl", 1))
    )


_CNotifCtrlMode_Type.__name__ = "Integer32"
_CNotifCtrlMode_Object = MibScalar
cNotifCtrlMode = _CNotifCtrlMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 586, 1, 1, 1),
    _CNotifCtrlMode_Type()
)
cNotifCtrlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cNotifCtrlMode.setStatus("current")


class _CNotifCtrlCurrentState_Type(Integer32):
    """Custom type cNotifCtrlCurrentState based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("controlOff", 2),
          ("controlOn", 1))
    )


_CNotifCtrlCurrentState_Type.__name__ = "Integer32"
_CNotifCtrlCurrentState_Object = MibScalar
cNotifCtrlCurrentState = _CNotifCtrlCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 586, 1, 1, 2),
    _CNotifCtrlCurrentState_Type()
)
cNotifCtrlCurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cNotifCtrlCurrentState.setStatus("current")


class _CNotifCtrlThreshold_Type(Unsigned32):
    """Custom type cNotifCtrlThreshold based on Unsigned32"""
    defaultValue = 50

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CNotifCtrlThreshold_Type.__name__ = "Unsigned32"
_CNotifCtrlThreshold_Object = MibScalar
cNotifCtrlThreshold = _CNotifCtrlThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 586, 1, 1, 3),
    _CNotifCtrlThreshold_Type()
)
cNotifCtrlThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cNotifCtrlThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cNotifCtrlThreshold.setUnits("notifications")


class _CNotifCtrlSamplingInterval_Type(Unsigned32):
    """Custom type cNotifCtrlSamplingInterval based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CNotifCtrlSamplingInterval_Type.__name__ = "Unsigned32"
_CNotifCtrlSamplingInterval_Object = MibScalar
cNotifCtrlSamplingInterval = _CNotifCtrlSamplingInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 586, 1, 1, 4),
    _CNotifCtrlSamplingInterval_Type()
)
cNotifCtrlSamplingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cNotifCtrlSamplingInterval.setStatus("current")
if mibBuilder.loadTexts:
    cNotifCtrlSamplingInterval.setUnits("minutes")


class _CNotifCtrlTableSize_Type(Unsigned32):
    """Custom type cNotifCtrlTableSize based on Unsigned32"""
    defaultValue = 200

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CNotifCtrlTableSize_Type.__name__ = "Unsigned32"
_CNotifCtrlTableSize_Object = MibScalar
cNotifCtrlTableSize = _CNotifCtrlTableSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 586, 1, 1, 5),
    _CNotifCtrlTableSize_Type()
)
cNotifCtrlTableSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cNotifCtrlTableSize.setStatus("current")


class _CNotifCtrlIndexNext_Type(Unsigned32):
    """Custom type cNotifCtrlIndexNext based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CNotifCtrlIndexNext_Type.__name__ = "Unsigned32"
_CNotifCtrlIndexNext_Object = MibScalar
cNotifCtrlIndexNext = _CNotifCtrlIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 586, 1, 1, 6),
    _CNotifCtrlIndexNext_Type()
)
cNotifCtrlIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cNotifCtrlIndexNext.setStatus("current")
_CNotifCtrlTable_Object = MibTable
cNotifCtrlTable = _CNotifCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 586, 1, 1, 7)
)
if mibBuilder.loadTexts:
    cNotifCtrlTable.setStatus("current")
_CNotifCtrlEntry_Object = MibTableRow
cNotifCtrlEntry = _CNotifCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 586, 1, 1, 7, 1)
)
cNotifCtrlEntry.setIndexNames(
    (0, "CISCO-NOTIFICATION-CONTROL-MIB", "cNotifCtrlIndex"),
)
if mibBuilder.loadTexts:
    cNotifCtrlEntry.setStatus("current")


class _CNotifCtrlIndex_Type(Unsigned32):
    """Custom type cNotifCtrlIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CNotifCtrlIndex_Type.__name__ = "Unsigned32"
_CNotifCtrlIndex_Object = MibTableColumn
cNotifCtrlIndex = _CNotifCtrlIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 586, 1, 1, 7, 1, 1),
    _CNotifCtrlIndex_Type()
)
cNotifCtrlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cNotifCtrlIndex.setStatus("current")
_CNotifCtrlOID_Type = AutonomousType
_CNotifCtrlOID_Object = MibTableColumn
cNotifCtrlOID = _CNotifCtrlOID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 586, 1, 1, 7, 1, 2),
    _CNotifCtrlOID_Type()
)
cNotifCtrlOID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cNotifCtrlOID.setStatus("current")


class _CNotifCtrlStorageType_Type(StorageType):
    """Custom type cNotifCtrlStorageType based on StorageType"""


_CNotifCtrlStorageType_Object = MibTableColumn
cNotifCtrlStorageType = _CNotifCtrlStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 586, 1, 1, 7, 1, 3),
    _CNotifCtrlStorageType_Type()
)
cNotifCtrlStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cNotifCtrlStorageType.setStatus("current")
_CNotifCtrlRowStatus_Type = RowStatus
_CNotifCtrlRowStatus_Object = MibTableColumn
cNotifCtrlRowStatus = _CNotifCtrlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 586, 1, 1, 7, 1, 4),
    _CNotifCtrlRowStatus_Type()
)
cNotifCtrlRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cNotifCtrlRowStatus.setStatus("current")


class _CNotifCtrlDescr_Type(SnmpAdminString):
    """Custom type cNotifCtrlDescr based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CNotifCtrlDescr_Type.__name__ = "SnmpAdminString"
_CNotifCtrlDescr_Object = MibTableColumn
cNotifCtrlDescr = _CNotifCtrlDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 586, 1, 1, 7, 1, 5),
    _CNotifCtrlDescr_Type()
)
cNotifCtrlDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cNotifCtrlDescr.setStatus("current")
_CNotifCtrlMIBConformance_ObjectIdentity = ObjectIdentity
cNotifCtrlMIBConformance = _CNotifCtrlMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 586, 2)
)
_CNotifCtrlMIBCompliances_ObjectIdentity = ObjectIdentity
cNotifCtrlMIBCompliances = _CNotifCtrlMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 586, 2, 1)
)
_CNotifCtrlMIBGroups_ObjectIdentity = ObjectIdentity
cNotifCtrlMIBGroups = _CNotifCtrlMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 586, 2, 2)
)

# Managed Objects groups

cNotifCtrlConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 586, 2, 2, 1)
)
cNotifCtrlConfigGroup.setObjects(
      *(("CISCO-NOTIFICATION-CONTROL-MIB", "cNotifCtrlMode"),
        ("CISCO-NOTIFICATION-CONTROL-MIB", "cNotifCtrlCurrentState"),
        ("CISCO-NOTIFICATION-CONTROL-MIB", "cNotifCtrlThreshold"),
        ("CISCO-NOTIFICATION-CONTROL-MIB", "cNotifCtrlSamplingInterval"),
        ("CISCO-NOTIFICATION-CONTROL-MIB", "cNotifCtrlTableSize"),
        ("CISCO-NOTIFICATION-CONTROL-MIB", "cNotifCtrlIndexNext"),
        ("CISCO-NOTIFICATION-CONTROL-MIB", "cNotifCtrlOID"),
        ("CISCO-NOTIFICATION-CONTROL-MIB", "cNotifCtrlStorageType"),
        ("CISCO-NOTIFICATION-CONTROL-MIB", "cNotifCtrlRowStatus"))
)
if mibBuilder.loadTexts:
    cNotifCtrlConfigGroup.setStatus("current")

cNotifCtrlConfigExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 586, 2, 2, 2)
)
cNotifCtrlConfigExtGroup.setObjects(
    ("CISCO-NOTIFICATION-CONTROL-MIB", "cNotifCtrlDescr")
)
if mibBuilder.loadTexts:
    cNotifCtrlConfigExtGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cNotifCtrlMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 586, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cNotifCtrlMIBCompliance.setStatus(
        "deprecated"
    )

cNotifCtrlMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 586, 2, 1, 2)
)
if mibBuilder.loadTexts:
    cNotifCtrlMIBComplianceRev1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-NOTIFICATION-CONTROL-MIB",
    **{"ciscoNotificationControlMIB": ciscoNotificationControlMIB,
       "cNotifCtrlMIBObjects": cNotifCtrlMIBObjects,
       "cNotifCtrlConfig": cNotifCtrlConfig,
       "cNotifCtrlMode": cNotifCtrlMode,
       "cNotifCtrlCurrentState": cNotifCtrlCurrentState,
       "cNotifCtrlThreshold": cNotifCtrlThreshold,
       "cNotifCtrlSamplingInterval": cNotifCtrlSamplingInterval,
       "cNotifCtrlTableSize": cNotifCtrlTableSize,
       "cNotifCtrlIndexNext": cNotifCtrlIndexNext,
       "cNotifCtrlTable": cNotifCtrlTable,
       "cNotifCtrlEntry": cNotifCtrlEntry,
       "cNotifCtrlIndex": cNotifCtrlIndex,
       "cNotifCtrlOID": cNotifCtrlOID,
       "cNotifCtrlStorageType": cNotifCtrlStorageType,
       "cNotifCtrlRowStatus": cNotifCtrlRowStatus,
       "cNotifCtrlDescr": cNotifCtrlDescr,
       "cNotifCtrlMIBConformance": cNotifCtrlMIBConformance,
       "cNotifCtrlMIBCompliances": cNotifCtrlMIBCompliances,
       "cNotifCtrlMIBCompliance": cNotifCtrlMIBCompliance,
       "cNotifCtrlMIBComplianceRev1": cNotifCtrlMIBComplianceRev1,
       "cNotifCtrlMIBGroups": cNotifCtrlMIBGroups,
       "cNotifCtrlConfigGroup": cNotifCtrlConfigGroup,
       "cNotifCtrlConfigExtGroup": cNotifCtrlConfigExtGroup}
)
