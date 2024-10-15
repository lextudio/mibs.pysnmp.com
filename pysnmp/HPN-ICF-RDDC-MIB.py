# SNMP MIB module (HPN-ICF-RDDC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-RDDC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:01:41 2024
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

(hpnicfCommon,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfCommon")

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

hpnicfRddc = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 151)
)
hpnicfRddc.setRevisions(
        ("2014-01-03 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpnicfRddcNotifications_ObjectIdentity = ObjectIdentity
hpnicfRddcNotifications = _HpnicfRddcNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 151, 0)
)
_HpnicfRddcObjects_ObjectIdentity = ObjectIdentity
hpnicfRddcObjects = _HpnicfRddcObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 151, 1)
)
_HpnicfRddcInfo_ObjectIdentity = ObjectIdentity
hpnicfRddcInfo = _HpnicfRddcInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 151, 1, 1)
)
_HpnicfRddcTable_Object = MibTable
hpnicfRddcTable = _HpnicfRddcTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 151, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hpnicfRddcTable.setStatus("current")
_HpnicfRddcEntry_Object = MibTableRow
hpnicfRddcEntry = _HpnicfRddcEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 151, 1, 1, 1, 1)
)
hpnicfRddcEntry.setIndexNames(
    (0, "HPN-ICF-RDDC-MIB", "hpnicfRddcGroupIdx"),
)
if mibBuilder.loadTexts:
    hpnicfRddcEntry.setStatus("current")
_HpnicfRddcGroupIdx_Type = Unsigned32
_HpnicfRddcGroupIdx_Object = MibTableColumn
hpnicfRddcGroupIdx = _HpnicfRddcGroupIdx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 151, 1, 1, 1, 1, 1),
    _HpnicfRddcGroupIdx_Type()
)
hpnicfRddcGroupIdx.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfRddcGroupIdx.setStatus("current")


class _HpnicfRddcGroupName_Type(OctetString):
    """Custom type hpnicfRddcGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_HpnicfRddcGroupName_Type.__name__ = "OctetString"
_HpnicfRddcGroupName_Object = MibTableColumn
hpnicfRddcGroupName = _HpnicfRddcGroupName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 151, 1, 1, 1, 1, 2),
    _HpnicfRddcGroupName_Type()
)
hpnicfRddcGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfRddcGroupName.setStatus("current")
_HpnicfRddcPreempTimeRemain_Type = Unsigned32
_HpnicfRddcPreempTimeRemain_Object = MibTableColumn
hpnicfRddcPreempTimeRemain = _HpnicfRddcPreempTimeRemain_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 151, 1, 1, 1, 1, 3),
    _HpnicfRddcPreempTimeRemain_Type()
)
hpnicfRddcPreempTimeRemain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfRddcPreempTimeRemain.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfRddcPreempTimeRemain.setUnits("minutes")
_HpnicfRddcPreempTimeConfig_Type = Unsigned32
_HpnicfRddcPreempTimeConfig_Object = MibTableColumn
hpnicfRddcPreempTimeConfig = _HpnicfRddcPreempTimeConfig_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 151, 1, 1, 1, 1, 4),
    _HpnicfRddcPreempTimeConfig_Type()
)
hpnicfRddcPreempTimeConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfRddcPreempTimeConfig.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfRddcPreempTimeConfig.setUnits("minutes")
_HpnicfRddcHoldTimeRemain_Type = Unsigned32
_HpnicfRddcHoldTimeRemain_Object = MibTableColumn
hpnicfRddcHoldTimeRemain = _HpnicfRddcHoldTimeRemain_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 151, 1, 1, 1, 1, 5),
    _HpnicfRddcHoldTimeRemain_Type()
)
hpnicfRddcHoldTimeRemain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfRddcHoldTimeRemain.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfRddcHoldTimeRemain.setUnits("seconds")
_HpnicfRddcHoldTimeConfig_Type = Unsigned32
_HpnicfRddcHoldTimeConfig_Object = MibTableColumn
hpnicfRddcHoldTimeConfig = _HpnicfRddcHoldTimeConfig_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 151, 1, 1, 1, 1, 6),
    _HpnicfRddcHoldTimeConfig_Type()
)
hpnicfRddcHoldTimeConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfRddcHoldTimeConfig.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfRddcHoldTimeConfig.setUnits("seconds")
_HpnicfRddcNodeTable_Object = MibTable
hpnicfRddcNodeTable = _HpnicfRddcNodeTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 151, 1, 1, 2)
)
if mibBuilder.loadTexts:
    hpnicfRddcNodeTable.setStatus("current")
_HpnicfRddcNodeEntry_Object = MibTableRow
hpnicfRddcNodeEntry = _HpnicfRddcNodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 151, 1, 1, 2, 1)
)
hpnicfRddcNodeEntry.setIndexNames(
    (0, "HPN-ICF-RDDC-MIB", "hpnicfRddcNodeGroupIdx"),
    (0, "HPN-ICF-RDDC-MIB", "hpnicfRddcNodeId"),
)
if mibBuilder.loadTexts:
    hpnicfRddcNodeEntry.setStatus("current")
_HpnicfRddcNodeGroupIdx_Type = Unsigned32
_HpnicfRddcNodeGroupIdx_Object = MibTableColumn
hpnicfRddcNodeGroupIdx = _HpnicfRddcNodeGroupIdx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 151, 1, 1, 2, 1, 1),
    _HpnicfRddcNodeGroupIdx_Type()
)
hpnicfRddcNodeGroupIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfRddcNodeGroupIdx.setStatus("current")
_HpnicfRddcNodeId_Type = Unsigned32
_HpnicfRddcNodeId_Object = MibTableColumn
hpnicfRddcNodeId = _HpnicfRddcNodeId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 151, 1, 1, 2, 1, 2),
    _HpnicfRddcNodeId_Type()
)
hpnicfRddcNodeId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfRddcNodeId.setStatus("current")


class _HpnicfRddcNodeBindType_Type(Integer32):
    """Custom type hpnicfRddcNodeBindType based on Integer32"""
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


_HpnicfRddcNodeBindType_Type.__name__ = "Integer32"
_HpnicfRddcNodeBindType_Object = MibTableColumn
hpnicfRddcNodeBindType = _HpnicfRddcNodeBindType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 151, 1, 1, 2, 1, 3),
    _HpnicfRddcNodeBindType_Type()
)
hpnicfRddcNodeBindType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfRddcNodeBindType.setStatus("current")
_HpnicfRddcNodeBindInfo_Type = Unsigned32
_HpnicfRddcNodeBindInfo_Object = MibTableColumn
hpnicfRddcNodeBindInfo = _HpnicfRddcNodeBindInfo_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 151, 1, 1, 2, 1, 4),
    _HpnicfRddcNodeBindInfo_Type()
)
hpnicfRddcNodeBindInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfRddcNodeBindInfo.setStatus("current")


class _HpnicfRddcNodePriority_Type(Unsigned32):
    """Custom type hpnicfRddcNodePriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_HpnicfRddcNodePriority_Type.__name__ = "Unsigned32"
_HpnicfRddcNodePriority_Object = MibTableColumn
hpnicfRddcNodePriority = _HpnicfRddcNodePriority_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 151, 1, 1, 2, 1, 5),
    _HpnicfRddcNodePriority_Type()
)
hpnicfRddcNodePriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfRddcNodePriority.setStatus("current")
_HpnicfRddcNodeWeight_Type = Integer32
_HpnicfRddcNodeWeight_Object = MibTableColumn
hpnicfRddcNodeWeight = _HpnicfRddcNodeWeight_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 151, 1, 1, 2, 1, 6),
    _HpnicfRddcNodeWeight_Type()
)
hpnicfRddcNodeWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfRddcNodeWeight.setStatus("current")


class _HpnicfRddcNodeStatus_Type(Integer32):
    """Custom type hpnicfRddcNodeStatus based on Integer32"""
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


_HpnicfRddcNodeStatus_Type.__name__ = "Integer32"
_HpnicfRddcNodeStatus_Object = MibTableColumn
hpnicfRddcNodeStatus = _HpnicfRddcNodeStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 151, 1, 1, 2, 1, 7),
    _HpnicfRddcNodeStatus_Type()
)
hpnicfRddcNodeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfRddcNodeStatus.setStatus("current")
_HpnicfRddcTrapObjects_ObjectIdentity = ObjectIdentity
hpnicfRddcTrapObjects = _HpnicfRddcTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 151, 1, 2)
)


class _HpnicfRddcNodeInfo_Type(DisplayString):
    """Custom type hpnicfRddcNodeInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfRddcNodeInfo_Type.__name__ = "DisplayString"
_HpnicfRddcNodeInfo_Object = MibScalar
hpnicfRddcNodeInfo = _HpnicfRddcNodeInfo_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 151, 1, 2, 1),
    _HpnicfRddcNodeInfo_Type()
)
hpnicfRddcNodeInfo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfRddcNodeInfo.setStatus("current")


class _HpnicfRddcSwitchReason_Type(DisplayString):
    """Custom type hpnicfRddcSwitchReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfRddcSwitchReason_Type.__name__ = "DisplayString"
_HpnicfRddcSwitchReason_Object = MibScalar
hpnicfRddcSwitchReason = _HpnicfRddcSwitchReason_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 151, 1, 2, 2),
    _HpnicfRddcSwitchReason_Type()
)
hpnicfRddcSwitchReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfRddcSwitchReason.setStatus("current")

# Managed Objects groups


# Notification objects

hpnicfRddcSwitchoverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 151, 0, 1)
)
hpnicfRddcSwitchoverTrap.setObjects(
      *(("HPN-ICF-RDDC-MIB", "hpnicfRddcGroupIdx"),
        ("HPN-ICF-RDDC-MIB", "hpnicfRddcGroupName"),
        ("HPN-ICF-RDDC-MIB", "hpnicfRddcNodeInfo"),
        ("HPN-ICF-RDDC-MIB", "hpnicfRddcSwitchReason"))
)
if mibBuilder.loadTexts:
    hpnicfRddcSwitchoverTrap.setStatus(
        "current"
    )

hpnicfRddcFailIfRecoverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 151, 0, 2)
)
hpnicfRddcFailIfRecoverTrap.setObjects(
      *(("HPN-ICF-RDDC-MIB", "hpnicfRddcGroupIdx"),
        ("HPN-ICF-RDDC-MIB", "hpnicfRddcGroupName"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    hpnicfRddcFailIfRecoverTrap.setStatus(
        "current"
    )

hpnicfRddcFailIfGenerateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 151, 0, 3)
)
hpnicfRddcFailIfGenerateTrap.setObjects(
      *(("HPN-ICF-RDDC-MIB", "hpnicfRddcGroupIdx"),
        ("HPN-ICF-RDDC-MIB", "hpnicfRddcGroupName"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    hpnicfRddcFailIfGenerateTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-RDDC-MIB",
    **{"hpnicfRddc": hpnicfRddc,
       "hpnicfRddcNotifications": hpnicfRddcNotifications,
       "hpnicfRddcSwitchoverTrap": hpnicfRddcSwitchoverTrap,
       "hpnicfRddcFailIfRecoverTrap": hpnicfRddcFailIfRecoverTrap,
       "hpnicfRddcFailIfGenerateTrap": hpnicfRddcFailIfGenerateTrap,
       "hpnicfRddcObjects": hpnicfRddcObjects,
       "hpnicfRddcInfo": hpnicfRddcInfo,
       "hpnicfRddcTable": hpnicfRddcTable,
       "hpnicfRddcEntry": hpnicfRddcEntry,
       "hpnicfRddcGroupIdx": hpnicfRddcGroupIdx,
       "hpnicfRddcGroupName": hpnicfRddcGroupName,
       "hpnicfRddcPreempTimeRemain": hpnicfRddcPreempTimeRemain,
       "hpnicfRddcPreempTimeConfig": hpnicfRddcPreempTimeConfig,
       "hpnicfRddcHoldTimeRemain": hpnicfRddcHoldTimeRemain,
       "hpnicfRddcHoldTimeConfig": hpnicfRddcHoldTimeConfig,
       "hpnicfRddcNodeTable": hpnicfRddcNodeTable,
       "hpnicfRddcNodeEntry": hpnicfRddcNodeEntry,
       "hpnicfRddcNodeGroupIdx": hpnicfRddcNodeGroupIdx,
       "hpnicfRddcNodeId": hpnicfRddcNodeId,
       "hpnicfRddcNodeBindType": hpnicfRddcNodeBindType,
       "hpnicfRddcNodeBindInfo": hpnicfRddcNodeBindInfo,
       "hpnicfRddcNodePriority": hpnicfRddcNodePriority,
       "hpnicfRddcNodeWeight": hpnicfRddcNodeWeight,
       "hpnicfRddcNodeStatus": hpnicfRddcNodeStatus,
       "hpnicfRddcTrapObjects": hpnicfRddcTrapObjects,
       "hpnicfRddcNodeInfo": hpnicfRddcNodeInfo,
       "hpnicfRddcSwitchReason": hpnicfRddcSwitchReason}
)
