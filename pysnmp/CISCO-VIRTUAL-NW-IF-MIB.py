# SNMP MIB module (CISCO-VIRTUAL-NW-IF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-VIRTUAL-NW-IF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:11:43 2024
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

(FcAddressId,) = mibBuilder.importSymbols(
    "CISCO-ST-TC",
    "FcAddressId")

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

(InterfaceIndex,
 ifName) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifName")

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

(DisplayString,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

ciscoVirtualNwIfMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 290)
)
ciscoVirtualNwIfMIB.setRevisions(
        ("2002-10-02 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoVirtualNwIfObjects_ObjectIdentity = ObjectIdentity
ciscoVirtualNwIfObjects = _CiscoVirtualNwIfObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 290, 1)
)
_VirtualNwIfConfig_ObjectIdentity = ObjectIdentity
virtualNwIfConfig = _VirtualNwIfConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 290, 1, 1)
)
_VirtualNwIfTable_Object = MibTable
virtualNwIfTable = _VirtualNwIfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 290, 1, 1, 1)
)
if mibBuilder.loadTexts:
    virtualNwIfTable.setStatus("current")
_VirtualNwIfEntry_Object = MibTableRow
virtualNwIfEntry = _VirtualNwIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 290, 1, 1, 1, 1)
)
virtualNwIfEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-VIRTUAL-NW-IF-MIB", "virtualNwIfType"),
    (0, "CISCO-VIRTUAL-NW-IF-MIB", "virtualNwIfId"),
)
if mibBuilder.loadTexts:
    virtualNwIfEntry.setStatus("current")


class _VirtualNwIfType_Type(Integer32):
    """Custom type virtualNwIfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vlan", 2),
          ("vsan", 1))
    )


_VirtualNwIfType_Type.__name__ = "Integer32"
_VirtualNwIfType_Object = MibTableColumn
virtualNwIfType = _VirtualNwIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 290, 1, 1, 1, 1, 1),
    _VirtualNwIfType_Type()
)
virtualNwIfType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    virtualNwIfType.setStatus("current")
_VirtualNwIfId_Type = Unsigned32
_VirtualNwIfId_Object = MibTableColumn
virtualNwIfId = _VirtualNwIfId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 290, 1, 1, 1, 1, 2),
    _VirtualNwIfId_Type()
)
virtualNwIfId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    virtualNwIfId.setStatus("current")
_VirtualNwIfIndex_Type = InterfaceIndex
_VirtualNwIfIndex_Object = MibTableColumn
virtualNwIfIndex = _VirtualNwIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 290, 1, 1, 1, 1, 3),
    _VirtualNwIfIndex_Type()
)
virtualNwIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualNwIfIndex.setStatus("current")
_VirtualNwIfFcId_Type = FcAddressId
_VirtualNwIfFcId_Object = MibTableColumn
virtualNwIfFcId = _VirtualNwIfFcId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 290, 1, 1, 1, 1, 4),
    _VirtualNwIfFcId_Type()
)
virtualNwIfFcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualNwIfFcId.setStatus("current")


class _VirtualNwIfOperStatusCause_Type(Integer32):
    """Custom type virtualNwIfOperStatusCause based on Integer32"""
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
        *(("adminDown", 2),
          ("kernelConfFailure", 5),
          ("noFcid", 4),
          ("none", 1),
          ("vsanNotOperational", 3))
    )


_VirtualNwIfOperStatusCause_Type.__name__ = "Integer32"
_VirtualNwIfOperStatusCause_Object = MibTableColumn
virtualNwIfOperStatusCause = _VirtualNwIfOperStatusCause_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 290, 1, 1, 1, 1, 5),
    _VirtualNwIfOperStatusCause_Type()
)
virtualNwIfOperStatusCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualNwIfOperStatusCause.setStatus("current")
_VirtualNwIfOperStatusCauseDescr_Type = SnmpAdminString
_VirtualNwIfOperStatusCauseDescr_Object = MibTableColumn
virtualNwIfOperStatusCauseDescr = _VirtualNwIfOperStatusCauseDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 290, 1, 1, 1, 1, 6),
    _VirtualNwIfOperStatusCauseDescr_Type()
)
virtualNwIfOperStatusCauseDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualNwIfOperStatusCauseDescr.setStatus("current")
_VirtualNwIfRowStatus_Type = RowStatus
_VirtualNwIfRowStatus_Object = MibTableColumn
virtualNwIfRowStatus = _VirtualNwIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 290, 1, 1, 1, 1, 7),
    _VirtualNwIfRowStatus_Type()
)
virtualNwIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    virtualNwIfRowStatus.setStatus("current")
_VirtualNwIfStatistics_ObjectIdentity = ObjectIdentity
virtualNwIfStatistics = _VirtualNwIfStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 290, 1, 2)
)
_VirtualNwIfNotification_ObjectIdentity = ObjectIdentity
virtualNwIfNotification = _VirtualNwIfNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 290, 1, 3)
)
_VirtualNwIfNotifications_ObjectIdentity = ObjectIdentity
virtualNwIfNotifications = _VirtualNwIfNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 290, 1, 3, 0)
)
_VirtualNwIfMIBConformance_ObjectIdentity = ObjectIdentity
virtualNwIfMIBConformance = _VirtualNwIfMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 290, 2)
)
_VirtualNwIfMIBCompliances_ObjectIdentity = ObjectIdentity
virtualNwIfMIBCompliances = _VirtualNwIfMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 290, 2, 1)
)
_VirtualNwIfMIBGroups_ObjectIdentity = ObjectIdentity
virtualNwIfMIBGroups = _VirtualNwIfMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 290, 2, 2)
)

# Managed Objects groups

virtualNwIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 290, 2, 2, 1)
)
virtualNwIfGroup.setObjects(
      *(("CISCO-VIRTUAL-NW-IF-MIB", "virtualNwIfIndex"),
        ("CISCO-VIRTUAL-NW-IF-MIB", "virtualNwIfFcId"),
        ("CISCO-VIRTUAL-NW-IF-MIB", "virtualNwIfOperStatusCause"),
        ("CISCO-VIRTUAL-NW-IF-MIB", "virtualNwIfOperStatusCauseDescr"),
        ("CISCO-VIRTUAL-NW-IF-MIB", "virtualNwIfRowStatus"))
)
if mibBuilder.loadTexts:
    virtualNwIfGroup.setStatus("current")


# Notification objects

virtualNwIfCreateEntryNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 290, 1, 3, 0, 1)
)
virtualNwIfCreateEntryNotify.setObjects(
      *(("CISCO-VIRTUAL-NW-IF-MIB", "virtualNwIfIndex"),
        ("IF-MIB", "ifName"))
)
if mibBuilder.loadTexts:
    virtualNwIfCreateEntryNotify.setStatus(
        "current"
    )

virtualNwIfDeleteEntryNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 290, 1, 3, 0, 2)
)
virtualNwIfDeleteEntryNotify.setObjects(
    ("CISCO-VIRTUAL-NW-IF-MIB", "virtualNwIfIndex")
)
if mibBuilder.loadTexts:
    virtualNwIfDeleteEntryNotify.setStatus(
        "current"
    )


# Notifications groups

virtualNwIfNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 290, 2, 2, 2)
)
virtualNwIfNotificationGroup.setObjects(
      *(("CISCO-VIRTUAL-NW-IF-MIB", "virtualNwIfCreateEntryNotify"),
        ("CISCO-VIRTUAL-NW-IF-MIB", "virtualNwIfDeleteEntryNotify"))
)
if mibBuilder.loadTexts:
    virtualNwIfNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

virtualNwIfMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 290, 2, 1, 1)
)
if mibBuilder.loadTexts:
    virtualNwIfMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-VIRTUAL-NW-IF-MIB",
    **{"ciscoVirtualNwIfMIB": ciscoVirtualNwIfMIB,
       "ciscoVirtualNwIfObjects": ciscoVirtualNwIfObjects,
       "virtualNwIfConfig": virtualNwIfConfig,
       "virtualNwIfTable": virtualNwIfTable,
       "virtualNwIfEntry": virtualNwIfEntry,
       "virtualNwIfType": virtualNwIfType,
       "virtualNwIfId": virtualNwIfId,
       "virtualNwIfIndex": virtualNwIfIndex,
       "virtualNwIfFcId": virtualNwIfFcId,
       "virtualNwIfOperStatusCause": virtualNwIfOperStatusCause,
       "virtualNwIfOperStatusCauseDescr": virtualNwIfOperStatusCauseDescr,
       "virtualNwIfRowStatus": virtualNwIfRowStatus,
       "virtualNwIfStatistics": virtualNwIfStatistics,
       "virtualNwIfNotification": virtualNwIfNotification,
       "virtualNwIfNotifications": virtualNwIfNotifications,
       "virtualNwIfCreateEntryNotify": virtualNwIfCreateEntryNotify,
       "virtualNwIfDeleteEntryNotify": virtualNwIfDeleteEntryNotify,
       "virtualNwIfMIBConformance": virtualNwIfMIBConformance,
       "virtualNwIfMIBCompliances": virtualNwIfMIBCompliances,
       "virtualNwIfMIBCompliance": virtualNwIfMIBCompliance,
       "virtualNwIfMIBGroups": virtualNwIfMIBGroups,
       "virtualNwIfGroup": virtualNwIfGroup,
       "virtualNwIfNotificationGroup": virtualNwIfNotificationGroup}
)
