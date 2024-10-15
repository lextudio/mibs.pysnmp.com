# SNMP MIB module (HUAWEI-INNER-LINK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-INNER-LINK-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:04:04 2024
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

(PhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "PhysicalIndex")

(hwDatacomm,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "hwDatacomm")

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
 Bits,
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

hwInnerLinkMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 158)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwInnerLinkMIBObjects_ObjectIdentity = ObjectIdentity
hwInnerLinkMIBObjects = _HwInnerLinkMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 158, 1)
)
_HwInnerLinkMIBObjPrefix_ObjectIdentity = ObjectIdentity
hwInnerLinkMIBObjPrefix = _HwInnerLinkMIBObjPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 158, 1, 1)
)
_HwInnerLinkLeftPortPhysicalIndex_Type = PhysicalIndex
_HwInnerLinkLeftPortPhysicalIndex_Object = MibScalar
hwInnerLinkLeftPortPhysicalIndex = _HwInnerLinkLeftPortPhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 158, 1, 1, 1),
    _HwInnerLinkLeftPortPhysicalIndex_Type()
)
hwInnerLinkLeftPortPhysicalIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwInnerLinkLeftPortPhysicalIndex.setStatus("current")
_HwInnerLinkLeftPortPhysicalName_Type = SnmpAdminString
_HwInnerLinkLeftPortPhysicalName_Object = MibScalar
hwInnerLinkLeftPortPhysicalName = _HwInnerLinkLeftPortPhysicalName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 158, 1, 1, 2),
    _HwInnerLinkLeftPortPhysicalName_Type()
)
hwInnerLinkLeftPortPhysicalName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwInnerLinkLeftPortPhysicalName.setStatus("current")
_HwInnerLinkRightPortPhysicalIndex_Type = PhysicalIndex
_HwInnerLinkRightPortPhysicalIndex_Object = MibScalar
hwInnerLinkRightPortPhysicalIndex = _HwInnerLinkRightPortPhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 158, 1, 1, 3),
    _HwInnerLinkRightPortPhysicalIndex_Type()
)
hwInnerLinkRightPortPhysicalIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwInnerLinkRightPortPhysicalIndex.setStatus("current")
_HwInnerLinkRightPortPhysicalName_Type = SnmpAdminString
_HwInnerLinkRightPortPhysicalName_Object = MibScalar
hwInnerLinkRightPortPhysicalName = _HwInnerLinkRightPortPhysicalName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 158, 1, 1, 4),
    _HwInnerLinkRightPortPhysicalName_Type()
)
hwInnerLinkRightPortPhysicalName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwInnerLinkRightPortPhysicalName.setStatus("current")
_HwInnerLinkTable_Object = MibTable
hwInnerLinkTable = _HwInnerLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 158, 1, 2)
)
if mibBuilder.loadTexts:
    hwInnerLinkTable.setStatus("current")
_HwInnerLinkEntry_Object = MibTableRow
hwInnerLinkEntry = _HwInnerLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 158, 1, 2, 1)
)
hwInnerLinkEntry.setIndexNames(
    (0, "HUAWEI-INNER-LINK-MIB", "hwInnerLinkIndex"),
)
if mibBuilder.loadTexts:
    hwInnerLinkEntry.setStatus("current")
_HwInnerLinkIndex_Type = Unsigned32
_HwInnerLinkIndex_Object = MibTableColumn
hwInnerLinkIndex = _HwInnerLinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 158, 1, 2, 1, 1),
    _HwInnerLinkIndex_Type()
)
hwInnerLinkIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwInnerLinkIndex.setStatus("current")


class _HwInnerLinkLeftFrameType_Type(Integer32):
    """Custom type hwInnerLinkLeftFrameType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("centralChassis", 2),
          ("lineChassis", 3),
          ("unknown", 1))
    )


_HwInnerLinkLeftFrameType_Type.__name__ = "Integer32"
_HwInnerLinkLeftFrameType_Object = MibTableColumn
hwInnerLinkLeftFrameType = _HwInnerLinkLeftFrameType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 158, 1, 2, 1, 2),
    _HwInnerLinkLeftFrameType_Type()
)
hwInnerLinkLeftFrameType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInnerLinkLeftFrameType.setStatus("current")
_HwInnerLinkLeftFrameId_Type = Unsigned32
_HwInnerLinkLeftFrameId_Object = MibTableColumn
hwInnerLinkLeftFrameId = _HwInnerLinkLeftFrameId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 158, 1, 2, 1, 3),
    _HwInnerLinkLeftFrameId_Type()
)
hwInnerLinkLeftFrameId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInnerLinkLeftFrameId.setStatus("current")
_HwInnerLinkLeftPortId_Type = Unsigned32
_HwInnerLinkLeftPortId_Object = MibTableColumn
hwInnerLinkLeftPortId = _HwInnerLinkLeftPortId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 158, 1, 2, 1, 4),
    _HwInnerLinkLeftPortId_Type()
)
hwInnerLinkLeftPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInnerLinkLeftPortId.setStatus("current")


class _HwInnerLinkRightFrameType_Type(Integer32):
    """Custom type hwInnerLinkRightFrameType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("centralChassis", 2),
          ("lineChassis", 3),
          ("unknown", 1))
    )


_HwInnerLinkRightFrameType_Type.__name__ = "Integer32"
_HwInnerLinkRightFrameType_Object = MibTableColumn
hwInnerLinkRightFrameType = _HwInnerLinkRightFrameType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 158, 1, 2, 1, 5),
    _HwInnerLinkRightFrameType_Type()
)
hwInnerLinkRightFrameType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInnerLinkRightFrameType.setStatus("current")
_HwInnerLinkRightFrameId_Type = Unsigned32
_HwInnerLinkRightFrameId_Object = MibTableColumn
hwInnerLinkRightFrameId = _HwInnerLinkRightFrameId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 158, 1, 2, 1, 6),
    _HwInnerLinkRightFrameId_Type()
)
hwInnerLinkRightFrameId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInnerLinkRightFrameId.setStatus("current")
_HwInnerLinkRightPortId_Type = Unsigned32
_HwInnerLinkRightPortId_Object = MibTableColumn
hwInnerLinkRightPortId = _HwInnerLinkRightPortId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 158, 1, 2, 1, 7),
    _HwInnerLinkRightPortId_Type()
)
hwInnerLinkRightPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInnerLinkRightPortId.setStatus("current")


class _HwInnerLinkType_Type(Integer32):
    """Custom type hwInnerLinkType based on Integer32"""
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
        *(("controlChannel", 2),
          ("forwardChannel", 4),
          ("monitorChannel", 3),
          ("unknown", 1))
    )


_HwInnerLinkType_Type.__name__ = "Integer32"
_HwInnerLinkType_Object = MibTableColumn
hwInnerLinkType = _HwInnerLinkType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 158, 1, 2, 1, 8),
    _HwInnerLinkType_Type()
)
hwInnerLinkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInnerLinkType.setStatus("current")


class _HwInnerLinkAdminState_Type(Integer32):
    """Custom type hwInnerLinkAdminState based on Integer32"""
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
        *(("locked", 2),
          ("notSupported", 1),
          ("shuttingDown", 3),
          ("unlocked", 4))
    )


_HwInnerLinkAdminState_Type.__name__ = "Integer32"
_HwInnerLinkAdminState_Object = MibTableColumn
hwInnerLinkAdminState = _HwInnerLinkAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 158, 1, 2, 1, 9),
    _HwInnerLinkAdminState_Type()
)
hwInnerLinkAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwInnerLinkAdminState.setStatus("current")


class _HwInnerLinkOperState_Type(Integer32):
    """Custom type hwInnerLinkOperState based on Integer32"""
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
        *(("mostPhyChannelDown", 4),
          ("mostPhyChannelUp", 2),
          ("partPhyChannelUp", 3),
          ("unknown", 1))
    )


_HwInnerLinkOperState_Type.__name__ = "Integer32"
_HwInnerLinkOperState_Object = MibTableColumn
hwInnerLinkOperState = _HwInnerLinkOperState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 158, 1, 2, 1, 10),
    _HwInnerLinkOperState_Type()
)
hwInnerLinkOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInnerLinkOperState.setStatus("current")


class _HwInnerLinkAlarmLight_Type(Bits):
    """Custom type hwInnerLinkAlarmLight based on Bits"""
    namedValues = NamedValues(
        *(("alarmOutstanding", 5),
          ("critical", 2),
          ("indeterminate", 7),
          ("major", 3),
          ("minor", 4),
          ("notSupported", 0),
          ("underRepair", 1),
          ("warning", 6))
    )

_HwInnerLinkAlarmLight_Type.__name__ = "Bits"
_HwInnerLinkAlarmLight_Object = MibTableColumn
hwInnerLinkAlarmLight = _HwInnerLinkAlarmLight_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 158, 1, 2, 1, 11),
    _HwInnerLinkAlarmLight_Type()
)
hwInnerLinkAlarmLight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInnerLinkAlarmLight.setStatus("current")
_HwInnerLinkTraps_ObjectIdentity = ObjectIdentity
hwInnerLinkTraps = _HwInnerLinkTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 158, 2)
)
_HwInnerLinkTrapsPrefix_ObjectIdentity = ObjectIdentity
hwInnerLinkTrapsPrefix = _HwInnerLinkTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 158, 2, 1)
)
_HwInnerLinkConformance_ObjectIdentity = ObjectIdentity
hwInnerLinkConformance = _HwInnerLinkConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 158, 3)
)
_HwInnerLinkCompliances_ObjectIdentity = ObjectIdentity
hwInnerLinkCompliances = _HwInnerLinkCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 158, 3, 1)
)
_HwInnerLinkGroups_ObjectIdentity = ObjectIdentity
hwInnerLinkGroups = _HwInnerLinkGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 158, 3, 2)
)

# Managed Objects groups

hwInnerLinkGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 158, 3, 2, 1)
)
hwInnerLinkGroup.setObjects(
      *(("HUAWEI-INNER-LINK-MIB", "hwInnerLinkLeftPortPhysicalIndex"),
        ("HUAWEI-INNER-LINK-MIB", "hwInnerLinkLeftPortPhysicalName"),
        ("HUAWEI-INNER-LINK-MIB", "hwInnerLinkRightPortPhysicalIndex"),
        ("HUAWEI-INNER-LINK-MIB", "hwInnerLinkRightPortPhysicalName"),
        ("HUAWEI-INNER-LINK-MIB", "hwInnerLinkLeftFrameType"),
        ("HUAWEI-INNER-LINK-MIB", "hwInnerLinkLeftFrameId"),
        ("HUAWEI-INNER-LINK-MIB", "hwInnerLinkLeftPortId"),
        ("HUAWEI-INNER-LINK-MIB", "hwInnerLinkRightFrameType"),
        ("HUAWEI-INNER-LINK-MIB", "hwInnerLinkRightFrameId"),
        ("HUAWEI-INNER-LINK-MIB", "hwInnerLinkRightPortId"),
        ("HUAWEI-INNER-LINK-MIB", "hwInnerLinkType"),
        ("HUAWEI-INNER-LINK-MIB", "hwInnerLinkAdminState"),
        ("HUAWEI-INNER-LINK-MIB", "hwInnerLinkOperState"),
        ("HUAWEI-INNER-LINK-MIB", "hwInnerLinkAlarmLight"))
)
if mibBuilder.loadTexts:
    hwInnerLinkGroup.setStatus("current")


# Notification objects

hwInnerLinkOnePhysicalLinkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 158, 2, 1, 1)
)
hwInnerLinkOnePhysicalLinkUp.setObjects(
      *(("HUAWEI-INNER-LINK-MIB", "hwInnerLinkLeftPortPhysicalIndex"),
        ("HUAWEI-INNER-LINK-MIB", "hwInnerLinkLeftPortPhysicalName"),
        ("HUAWEI-INNER-LINK-MIB", "hwInnerLinkRightPortPhysicalIndex"),
        ("HUAWEI-INNER-LINK-MIB", "hwInnerLinkRightPortPhysicalName"))
)
if mibBuilder.loadTexts:
    hwInnerLinkOnePhysicalLinkUp.setStatus(
        "current"
    )

hwInnerLinkOnePhysicalLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 158, 2, 1, 2)
)
hwInnerLinkOnePhysicalLinkDown.setObjects(
      *(("HUAWEI-INNER-LINK-MIB", "hwInnerLinkLeftPortPhysicalIndex"),
        ("HUAWEI-INNER-LINK-MIB", "hwInnerLinkLeftPortPhysicalName"),
        ("HUAWEI-INNER-LINK-MIB", "hwInnerLinkRightPortPhysicalIndex"),
        ("HUAWEI-INNER-LINK-MIB", "hwInnerLinkRightPortPhysicalName"))
)
if mibBuilder.loadTexts:
    hwInnerLinkOnePhysicalLinkDown.setStatus(
        "current"
    )


# Notifications groups

hwInnerLinkNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 158, 3, 2, 2)
)
hwInnerLinkNotificationGroup.setObjects(
      *(("HUAWEI-INNER-LINK-MIB", "hwInnerLinkOnePhysicalLinkUp"),
        ("HUAWEI-INNER-LINK-MIB", "hwInnerLinkOnePhysicalLinkDown"))
)
if mibBuilder.loadTexts:
    hwInnerLinkNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hwInnerLinkCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 158, 3, 1, 1)
)
if mibBuilder.loadTexts:
    hwInnerLinkCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-INNER-LINK-MIB",
    **{"hwInnerLinkMIB": hwInnerLinkMIB,
       "hwInnerLinkMIBObjects": hwInnerLinkMIBObjects,
       "hwInnerLinkMIBObjPrefix": hwInnerLinkMIBObjPrefix,
       "hwInnerLinkLeftPortPhysicalIndex": hwInnerLinkLeftPortPhysicalIndex,
       "hwInnerLinkLeftPortPhysicalName": hwInnerLinkLeftPortPhysicalName,
       "hwInnerLinkRightPortPhysicalIndex": hwInnerLinkRightPortPhysicalIndex,
       "hwInnerLinkRightPortPhysicalName": hwInnerLinkRightPortPhysicalName,
       "hwInnerLinkTable": hwInnerLinkTable,
       "hwInnerLinkEntry": hwInnerLinkEntry,
       "hwInnerLinkIndex": hwInnerLinkIndex,
       "hwInnerLinkLeftFrameType": hwInnerLinkLeftFrameType,
       "hwInnerLinkLeftFrameId": hwInnerLinkLeftFrameId,
       "hwInnerLinkLeftPortId": hwInnerLinkLeftPortId,
       "hwInnerLinkRightFrameType": hwInnerLinkRightFrameType,
       "hwInnerLinkRightFrameId": hwInnerLinkRightFrameId,
       "hwInnerLinkRightPortId": hwInnerLinkRightPortId,
       "hwInnerLinkType": hwInnerLinkType,
       "hwInnerLinkAdminState": hwInnerLinkAdminState,
       "hwInnerLinkOperState": hwInnerLinkOperState,
       "hwInnerLinkAlarmLight": hwInnerLinkAlarmLight,
       "hwInnerLinkTraps": hwInnerLinkTraps,
       "hwInnerLinkTrapsPrefix": hwInnerLinkTrapsPrefix,
       "hwInnerLinkOnePhysicalLinkUp": hwInnerLinkOnePhysicalLinkUp,
       "hwInnerLinkOnePhysicalLinkDown": hwInnerLinkOnePhysicalLinkDown,
       "hwInnerLinkConformance": hwInnerLinkConformance,
       "hwInnerLinkCompliances": hwInnerLinkCompliances,
       "hwInnerLinkCompliance": hwInnerLinkCompliance,
       "hwInnerLinkGroups": hwInnerLinkGroups,
       "hwInnerLinkGroup": hwInnerLinkGroup,
       "hwInnerLinkNotificationGroup": hwInnerLinkNotificationGroup}
)
