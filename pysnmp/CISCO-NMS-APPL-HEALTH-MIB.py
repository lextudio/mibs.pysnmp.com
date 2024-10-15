# SNMP MIB module (CISCO-NMS-APPL-HEALTH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-NMS-APPL-HEALTH-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:06:14 2024
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

(CiscoAlarmSeverity,) = mibBuilder.importSymbols(
    "CISCO-TC",
    "CiscoAlarmSeverity")

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

(DateAndTime,
 DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

ciscoNmsApplHealthMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 237)
)
ciscoNmsApplHealthMIB.setRevisions(
        ("2001-10-24 00:00",
         "2001-10-15 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoNmsApplHealthNotifs_ObjectIdentity = ObjectIdentity
ciscoNmsApplHealthNotifs = _CiscoNmsApplHealthNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 237, 0)
)
_CiscoNmsApplHealthMIBObjects_ObjectIdentity = ObjectIdentity
ciscoNmsApplHealthMIBObjects = _CiscoNmsApplHealthMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 237, 1)
)
_CnaHealthObj_ObjectIdentity = ObjectIdentity
cnaHealthObj = _CnaHealthObj_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 237, 1, 1)
)
_CnaHealthNotifSeqNum_Type = Counter32
_CnaHealthNotifSeqNum_Object = MibScalar
cnaHealthNotifSeqNum = _CnaHealthNotifSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 237, 1, 1, 1),
    _CnaHealthNotifSeqNum_Type()
)
cnaHealthNotifSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnaHealthNotifSeqNum.setStatus("current")
_CnaHealthTable_Object = MibTable
cnaHealthTable = _CnaHealthTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 237, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cnaHealthTable.setStatus("current")
_CnaHealthTableEntry_Object = MibTableRow
cnaHealthTableEntry = _CnaHealthTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 237, 1, 1, 2, 1)
)
cnaHealthTableEntry.setIndexNames(
    (0, "CISCO-NMS-APPL-HEALTH-MIB", "cnaHealthTableIndex"),
)
if mibBuilder.loadTexts:
    cnaHealthTableEntry.setStatus("current")


class _CnaHealthTableIndex_Type(Unsigned32):
    """Custom type cnaHealthTableIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CnaHealthTableIndex_Type.__name__ = "Unsigned32"
_CnaHealthTableIndex_Object = MibTableColumn
cnaHealthTableIndex = _CnaHealthTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 237, 1, 1, 2, 1, 1),
    _CnaHealthTableIndex_Type()
)
cnaHealthTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnaHealthTableIndex.setStatus("current")
_CnaHealthStatusChangeTime_Type = DateAndTime
_CnaHealthStatusChangeTime_Object = MibTableColumn
cnaHealthStatusChangeTime = _CnaHealthStatusChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 237, 1, 1, 2, 1, 2),
    _CnaHealthStatusChangeTime_Type()
)
cnaHealthStatusChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnaHealthStatusChangeTime.setStatus("current")


class _CnaHealthName_Type(SnmpAdminString):
    """Custom type cnaHealthName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CnaHealthName_Type.__name__ = "SnmpAdminString"
_CnaHealthName_Object = MibTableColumn
cnaHealthName = _CnaHealthName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 237, 1, 1, 2, 1, 3),
    _CnaHealthName_Type()
)
cnaHealthName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnaHealthName.setStatus("current")


class _CnaHealthStatus_Type(Integer32):
    """Custom type cnaHealthStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("busy", 3),
          ("exited", 5),
          ("failed", 4),
          ("started", 1),
          ("stopped", 2))
    )


_CnaHealthStatus_Type.__name__ = "Integer32"
_CnaHealthStatus_Object = MibTableColumn
cnaHealthStatus = _CnaHealthStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 237, 1, 1, 2, 1, 4),
    _CnaHealthStatus_Type()
)
cnaHealthStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnaHealthStatus.setStatus("current")


class _CnaHealthSevLevel_Type(CiscoAlarmSeverity):
    """Custom type cnaHealthSevLevel based on CiscoAlarmSeverity"""


_CnaHealthSevLevel_Object = MibTableColumn
cnaHealthSevLevel = _CnaHealthSevLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 237, 1, 1, 2, 1, 5),
    _CnaHealthSevLevel_Type()
)
cnaHealthSevLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnaHealthSevLevel.setStatus("current")


class _CnaHealthComLineArgs_Type(SnmpAdminString):
    """Custom type cnaHealthComLineArgs based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CnaHealthComLineArgs_Type.__name__ = "SnmpAdminString"
_CnaHealthComLineArgs_Object = MibTableColumn
cnaHealthComLineArgs = _CnaHealthComLineArgs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 237, 1, 1, 2, 1, 6),
    _CnaHealthComLineArgs_Type()
)
cnaHealthComLineArgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnaHealthComLineArgs.setStatus("current")


class _CnaHealthStatusDesc_Type(SnmpAdminString):
    """Custom type cnaHealthStatusDesc based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CnaHealthStatusDesc_Type.__name__ = "SnmpAdminString"
_CnaHealthStatusDesc_Object = MibTableColumn
cnaHealthStatusDesc = _CnaHealthStatusDesc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 237, 1, 1, 2, 1, 7),
    _CnaHealthStatusDesc_Type()
)
cnaHealthStatusDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnaHealthStatusDesc.setStatus("current")
_CiscoNmsApplHealthMIBConforms_ObjectIdentity = ObjectIdentity
ciscoNmsApplHealthMIBConforms = _CiscoNmsApplHealthMIBConforms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 237, 2)
)
_CnaHealthMIBCompliances_ObjectIdentity = ObjectIdentity
cnaHealthMIBCompliances = _CnaHealthMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 237, 2, 1)
)
_CnaHealthMIBGroups_ObjectIdentity = ObjectIdentity
cnaHealthMIBGroups = _CnaHealthMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 237, 2, 2)
)

# Managed Objects groups

cnaHealthMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 237, 2, 2, 1)
)
cnaHealthMIBGroup.setObjects(
      *(("CISCO-NMS-APPL-HEALTH-MIB", "cnaHealthNotifSeqNum"),
        ("CISCO-NMS-APPL-HEALTH-MIB", "cnaHealthTableIndex"),
        ("CISCO-NMS-APPL-HEALTH-MIB", "cnaHealthStatusChangeTime"),
        ("CISCO-NMS-APPL-HEALTH-MIB", "cnaHealthName"),
        ("CISCO-NMS-APPL-HEALTH-MIB", "cnaHealthStatus"),
        ("CISCO-NMS-APPL-HEALTH-MIB", "cnaHealthSevLevel"),
        ("CISCO-NMS-APPL-HEALTH-MIB", "cnaHealthComLineArgs"),
        ("CISCO-NMS-APPL-HEALTH-MIB", "cnaHealthStatusDesc"))
)
if mibBuilder.loadTexts:
    cnaHealthMIBGroup.setStatus("current")


# Notification objects

cnaHealthNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 237, 0, 1)
)
cnaHealthNotif.setObjects(
      *(("CISCO-NMS-APPL-HEALTH-MIB", "cnaHealthNotifSeqNum"),
        ("CISCO-NMS-APPL-HEALTH-MIB", "cnaHealthStatusChangeTime"),
        ("CISCO-NMS-APPL-HEALTH-MIB", "cnaHealthName"),
        ("CISCO-NMS-APPL-HEALTH-MIB", "cnaHealthStatus"),
        ("CISCO-NMS-APPL-HEALTH-MIB", "cnaHealthSevLevel"),
        ("CISCO-NMS-APPL-HEALTH-MIB", "cnaHealthComLineArgs"),
        ("CISCO-NMS-APPL-HEALTH-MIB", "cnaHealthStatusDesc"))
)
if mibBuilder.loadTexts:
    cnaHealthNotif.setStatus(
        "current"
    )


# Notifications groups

cnaHealthNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 237, 2, 2, 2)
)
cnaHealthNotifGroup.setObjects(
    ("CISCO-NMS-APPL-HEALTH-MIB", "cnaHealthNotif")
)
if mibBuilder.loadTexts:
    cnaHealthNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

cnaHealthMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 237, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cnaHealthMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-NMS-APPL-HEALTH-MIB",
    **{"ciscoNmsApplHealthMIB": ciscoNmsApplHealthMIB,
       "ciscoNmsApplHealthNotifs": ciscoNmsApplHealthNotifs,
       "cnaHealthNotif": cnaHealthNotif,
       "ciscoNmsApplHealthMIBObjects": ciscoNmsApplHealthMIBObjects,
       "cnaHealthObj": cnaHealthObj,
       "cnaHealthNotifSeqNum": cnaHealthNotifSeqNum,
       "cnaHealthTable": cnaHealthTable,
       "cnaHealthTableEntry": cnaHealthTableEntry,
       "cnaHealthTableIndex": cnaHealthTableIndex,
       "cnaHealthStatusChangeTime": cnaHealthStatusChangeTime,
       "cnaHealthName": cnaHealthName,
       "cnaHealthStatus": cnaHealthStatus,
       "cnaHealthSevLevel": cnaHealthSevLevel,
       "cnaHealthComLineArgs": cnaHealthComLineArgs,
       "cnaHealthStatusDesc": cnaHealthStatusDesc,
       "ciscoNmsApplHealthMIBConforms": ciscoNmsApplHealthMIBConforms,
       "cnaHealthMIBCompliances": cnaHealthMIBCompliances,
       "cnaHealthMIBCompliance": cnaHealthMIBCompliance,
       "cnaHealthMIBGroups": cnaHealthMIBGroups,
       "cnaHealthMIBGroup": cnaHealthMIBGroup,
       "cnaHealthNotifGroup": cnaHealthNotifGroup}
)
