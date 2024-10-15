# SNMP MIB module (HH3C-RDDC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-RDDC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:54:43 2024
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

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

(ifDescr,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifDescr",
    "ifIndex")

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


# MODULE-IDENTITY

hh3cRddc = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 151)
)
hh3cRddc.setRevisions(
        ("2014-01-03 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cRddcNotifications_ObjectIdentity = ObjectIdentity
hh3cRddcNotifications = _Hh3cRddcNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 151, 0)
)
_Hh3cRddcObjects_ObjectIdentity = ObjectIdentity
hh3cRddcObjects = _Hh3cRddcObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 151, 1)
)
_Hh3cRddcInfo_ObjectIdentity = ObjectIdentity
hh3cRddcInfo = _Hh3cRddcInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 151, 1, 1)
)
_Hh3cRddcTable_Object = MibTable
hh3cRddcTable = _Hh3cRddcTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 151, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cRddcTable.setStatus("current")
_Hh3cRddcEntry_Object = MibTableRow
hh3cRddcEntry = _Hh3cRddcEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 151, 1, 1, 1, 1)
)
hh3cRddcEntry.setIndexNames(
    (0, "HH3C-RDDC-MIB", "hh3cRddcGroupIdx"),
)
if mibBuilder.loadTexts:
    hh3cRddcEntry.setStatus("current")
_Hh3cRddcGroupIdx_Type = Unsigned32
_Hh3cRddcGroupIdx_Object = MibTableColumn
hh3cRddcGroupIdx = _Hh3cRddcGroupIdx_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 151, 1, 1, 1, 1, 1),
    _Hh3cRddcGroupIdx_Type()
)
hh3cRddcGroupIdx.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cRddcGroupIdx.setStatus("current")


class _Hh3cRddcGroupName_Type(OctetString):
    """Custom type hh3cRddcGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Hh3cRddcGroupName_Type.__name__ = "OctetString"
_Hh3cRddcGroupName_Object = MibTableColumn
hh3cRddcGroupName = _Hh3cRddcGroupName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 151, 1, 1, 1, 1, 2),
    _Hh3cRddcGroupName_Type()
)
hh3cRddcGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRddcGroupName.setStatus("current")
_Hh3cRddcPreempTimeRemain_Type = Unsigned32
_Hh3cRddcPreempTimeRemain_Object = MibTableColumn
hh3cRddcPreempTimeRemain = _Hh3cRddcPreempTimeRemain_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 151, 1, 1, 1, 1, 3),
    _Hh3cRddcPreempTimeRemain_Type()
)
hh3cRddcPreempTimeRemain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRddcPreempTimeRemain.setStatus("current")
if mibBuilder.loadTexts:
    hh3cRddcPreempTimeRemain.setUnits("minutes")
_Hh3cRddcPreempTimeConfig_Type = Unsigned32
_Hh3cRddcPreempTimeConfig_Object = MibTableColumn
hh3cRddcPreempTimeConfig = _Hh3cRddcPreempTimeConfig_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 151, 1, 1, 1, 1, 4),
    _Hh3cRddcPreempTimeConfig_Type()
)
hh3cRddcPreempTimeConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRddcPreempTimeConfig.setStatus("current")
if mibBuilder.loadTexts:
    hh3cRddcPreempTimeConfig.setUnits("minutes")
_Hh3cRddcHoldTimeRemain_Type = Unsigned32
_Hh3cRddcHoldTimeRemain_Object = MibTableColumn
hh3cRddcHoldTimeRemain = _Hh3cRddcHoldTimeRemain_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 151, 1, 1, 1, 1, 5),
    _Hh3cRddcHoldTimeRemain_Type()
)
hh3cRddcHoldTimeRemain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRddcHoldTimeRemain.setStatus("current")
if mibBuilder.loadTexts:
    hh3cRddcHoldTimeRemain.setUnits("seconds")
_Hh3cRddcHoldTimeConfig_Type = Unsigned32
_Hh3cRddcHoldTimeConfig_Object = MibTableColumn
hh3cRddcHoldTimeConfig = _Hh3cRddcHoldTimeConfig_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 151, 1, 1, 1, 1, 6),
    _Hh3cRddcHoldTimeConfig_Type()
)
hh3cRddcHoldTimeConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRddcHoldTimeConfig.setStatus("current")
if mibBuilder.loadTexts:
    hh3cRddcHoldTimeConfig.setUnits("seconds")
_Hh3cRddcNodeTable_Object = MibTable
hh3cRddcNodeTable = _Hh3cRddcNodeTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 151, 1, 1, 2)
)
if mibBuilder.loadTexts:
    hh3cRddcNodeTable.setStatus("current")
_Hh3cRddcNodeEntry_Object = MibTableRow
hh3cRddcNodeEntry = _Hh3cRddcNodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 151, 1, 1, 2, 1)
)
hh3cRddcNodeEntry.setIndexNames(
    (0, "HH3C-RDDC-MIB", "hh3cRddcNodeGroupIdx"),
    (0, "HH3C-RDDC-MIB", "hh3cRddcNodeId"),
)
if mibBuilder.loadTexts:
    hh3cRddcNodeEntry.setStatus("current")
_Hh3cRddcNodeGroupIdx_Type = Unsigned32
_Hh3cRddcNodeGroupIdx_Object = MibTableColumn
hh3cRddcNodeGroupIdx = _Hh3cRddcNodeGroupIdx_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 151, 1, 1, 2, 1, 1),
    _Hh3cRddcNodeGroupIdx_Type()
)
hh3cRddcNodeGroupIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cRddcNodeGroupIdx.setStatus("current")
_Hh3cRddcNodeId_Type = Unsigned32
_Hh3cRddcNodeId_Object = MibTableColumn
hh3cRddcNodeId = _Hh3cRddcNodeId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 151, 1, 1, 2, 1, 2),
    _Hh3cRddcNodeId_Type()
)
hh3cRddcNodeId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cRddcNodeId.setStatus("current")


class _Hh3cRddcNodeBindType_Type(Integer32):
    """Custom type hh3cRddcNodeBindType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("chassis", 2),
          ("invalid", 1))
    )


_Hh3cRddcNodeBindType_Type.__name__ = "Integer32"
_Hh3cRddcNodeBindType_Object = MibTableColumn
hh3cRddcNodeBindType = _Hh3cRddcNodeBindType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 151, 1, 1, 2, 1, 3),
    _Hh3cRddcNodeBindType_Type()
)
hh3cRddcNodeBindType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRddcNodeBindType.setStatus("current")
_Hh3cRddcNodeBindInfo_Type = Unsigned32
_Hh3cRddcNodeBindInfo_Object = MibTableColumn
hh3cRddcNodeBindInfo = _Hh3cRddcNodeBindInfo_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 151, 1, 1, 2, 1, 4),
    _Hh3cRddcNodeBindInfo_Type()
)
hh3cRddcNodeBindInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRddcNodeBindInfo.setStatus("current")


class _Hh3cRddcNodePriority_Type(Unsigned32):
    """Custom type hh3cRddcNodePriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Hh3cRddcNodePriority_Type.__name__ = "Unsigned32"
_Hh3cRddcNodePriority_Object = MibTableColumn
hh3cRddcNodePriority = _Hh3cRddcNodePriority_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 151, 1, 1, 2, 1, 5),
    _Hh3cRddcNodePriority_Type()
)
hh3cRddcNodePriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRddcNodePriority.setStatus("current")
_Hh3cRddcNodeWeight_Type = Integer32
_Hh3cRddcNodeWeight_Object = MibTableColumn
hh3cRddcNodeWeight = _Hh3cRddcNodeWeight_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 151, 1, 1, 2, 1, 6),
    _Hh3cRddcNodeWeight_Type()
)
hh3cRddcNodeWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRddcNodeWeight.setStatus("current")


class _Hh3cRddcNodeStatus_Type(Integer32):
    """Custom type hh3cRddcNodeStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("master", 2),
          ("standby", 3))
    )


_Hh3cRddcNodeStatus_Type.__name__ = "Integer32"
_Hh3cRddcNodeStatus_Object = MibTableColumn
hh3cRddcNodeStatus = _Hh3cRddcNodeStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 151, 1, 1, 2, 1, 7),
    _Hh3cRddcNodeStatus_Type()
)
hh3cRddcNodeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRddcNodeStatus.setStatus("current")
_Hh3cRddcTrapObjects_ObjectIdentity = ObjectIdentity
hh3cRddcTrapObjects = _Hh3cRddcTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 151, 1, 2)
)


class _Hh3cRddcNodeInfo_Type(DisplayString):
    """Custom type hh3cRddcNodeInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cRddcNodeInfo_Type.__name__ = "DisplayString"
_Hh3cRddcNodeInfo_Object = MibScalar
hh3cRddcNodeInfo = _Hh3cRddcNodeInfo_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 151, 1, 2, 1),
    _Hh3cRddcNodeInfo_Type()
)
hh3cRddcNodeInfo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cRddcNodeInfo.setStatus("current")


class _Hh3cRddcSwitchReason_Type(DisplayString):
    """Custom type hh3cRddcSwitchReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cRddcSwitchReason_Type.__name__ = "DisplayString"
_Hh3cRddcSwitchReason_Object = MibScalar
hh3cRddcSwitchReason = _Hh3cRddcSwitchReason_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 151, 1, 2, 2),
    _Hh3cRddcSwitchReason_Type()
)
hh3cRddcSwitchReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cRddcSwitchReason.setStatus("current")

# Managed Objects groups


# Notification objects

hh3cRddcSwitchoverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 151, 0, 1)
)
hh3cRddcSwitchoverTrap.setObjects(
      *(("HH3C-RDDC-MIB", "hh3cRddcGroupIdx"),
        ("HH3C-RDDC-MIB", "hh3cRddcGroupName"),
        ("HH3C-RDDC-MIB", "hh3cRddcNodeInfo"),
        ("HH3C-RDDC-MIB", "hh3cRddcSwitchReason"))
)
if mibBuilder.loadTexts:
    hh3cRddcSwitchoverTrap.setStatus(
        "current"
    )

hh3cRddcFailIfRecoverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 151, 0, 2)
)
hh3cRddcFailIfRecoverTrap.setObjects(
      *(("HH3C-RDDC-MIB", "hh3cRddcGroupIdx"),
        ("HH3C-RDDC-MIB", "hh3cRddcGroupName"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    hh3cRddcFailIfRecoverTrap.setStatus(
        "current"
    )

hh3cRddcFailIfGenerateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 151, 0, 3)
)
hh3cRddcFailIfGenerateTrap.setObjects(
      *(("HH3C-RDDC-MIB", "hh3cRddcGroupIdx"),
        ("HH3C-RDDC-MIB", "hh3cRddcGroupName"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    hh3cRddcFailIfGenerateTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-RDDC-MIB",
    **{"hh3cRddc": hh3cRddc,
       "hh3cRddcNotifications": hh3cRddcNotifications,
       "hh3cRddcSwitchoverTrap": hh3cRddcSwitchoverTrap,
       "hh3cRddcFailIfRecoverTrap": hh3cRddcFailIfRecoverTrap,
       "hh3cRddcFailIfGenerateTrap": hh3cRddcFailIfGenerateTrap,
       "hh3cRddcObjects": hh3cRddcObjects,
       "hh3cRddcInfo": hh3cRddcInfo,
       "hh3cRddcTable": hh3cRddcTable,
       "hh3cRddcEntry": hh3cRddcEntry,
       "hh3cRddcGroupIdx": hh3cRddcGroupIdx,
       "hh3cRddcGroupName": hh3cRddcGroupName,
       "hh3cRddcPreempTimeRemain": hh3cRddcPreempTimeRemain,
       "hh3cRddcPreempTimeConfig": hh3cRddcPreempTimeConfig,
       "hh3cRddcHoldTimeRemain": hh3cRddcHoldTimeRemain,
       "hh3cRddcHoldTimeConfig": hh3cRddcHoldTimeConfig,
       "hh3cRddcNodeTable": hh3cRddcNodeTable,
       "hh3cRddcNodeEntry": hh3cRddcNodeEntry,
       "hh3cRddcNodeGroupIdx": hh3cRddcNodeGroupIdx,
       "hh3cRddcNodeId": hh3cRddcNodeId,
       "hh3cRddcNodeBindType": hh3cRddcNodeBindType,
       "hh3cRddcNodeBindInfo": hh3cRddcNodeBindInfo,
       "hh3cRddcNodePriority": hh3cRddcNodePriority,
       "hh3cRddcNodeWeight": hh3cRddcNodeWeight,
       "hh3cRddcNodeStatus": hh3cRddcNodeStatus,
       "hh3cRddcTrapObjects": hh3cRddcTrapObjects,
       "hh3cRddcNodeInfo": hh3cRddcNodeInfo,
       "hh3cRddcSwitchReason": hh3cRddcSwitchReason}
)
