# SNMP MIB module (HUAWEI-MG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-MG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:04:58 2024
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

(hwDatacomm,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "hwDatacomm")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

hwMG = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 312)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwMGMonitorGroupObjects_ObjectIdentity = ObjectIdentity
hwMGMonitorGroupObjects = _HwMGMonitorGroupObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 312, 1)
)
_HwMGMonitorGroupTable_Object = MibTable
hwMGMonitorGroupTable = _HwMGMonitorGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 312, 1, 1)
)
if mibBuilder.loadTexts:
    hwMGMonitorGroupTable.setStatus("current")
_HwMGMonitorGroupEntry_Object = MibTableRow
hwMGMonitorGroupEntry = _HwMGMonitorGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 312, 1, 1, 1)
)
hwMGMonitorGroupEntry.setIndexNames(
    (0, "HUAWEI-MG-MIB", "hwMGMonitorGroupIndex"),
)
if mibBuilder.loadTexts:
    hwMGMonitorGroupEntry.setStatus("current")


class _HwMGMonitorGroupIndex_Type(Integer32):
    """Custom type hwMGMonitorGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_HwMGMonitorGroupIndex_Type.__name__ = "Integer32"
_HwMGMonitorGroupIndex_Object = MibTableColumn
hwMGMonitorGroupIndex = _HwMGMonitorGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 312, 1, 1, 1, 1),
    _HwMGMonitorGroupIndex_Type()
)
hwMGMonitorGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMGMonitorGroupIndex.setStatus("current")


class _HwMGMonitorGroupName_Type(OctetString):
    """Custom type hwMGMonitorGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwMGMonitorGroupName_Type.__name__ = "OctetString"
_HwMGMonitorGroupName_Object = MibTableColumn
hwMGMonitorGroupName = _HwMGMonitorGroupName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 312, 1, 1, 1, 2),
    _HwMGMonitorGroupName_Type()
)
hwMGMonitorGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMGMonitorGroupName.setStatus("current")
_HwMGMonitorGroupDownWeight_Type = Integer32
_HwMGMonitorGroupDownWeight_Object = MibTableColumn
hwMGMonitorGroupDownWeight = _HwMGMonitorGroupDownWeight_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 312, 1, 1, 1, 3),
    _HwMGMonitorGroupDownWeight_Type()
)
hwMGMonitorGroupDownWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMGMonitorGroupDownWeight.setStatus("current")


class _HwMGMonitorGroupStatus_Type(Integer32):
    """Custom type hwMGMonitorGroupStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_HwMGMonitorGroupStatus_Type.__name__ = "Integer32"
_HwMGMonitorGroupStatus_Object = MibTableColumn
hwMGMonitorGroupStatus = _HwMGMonitorGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 312, 1, 1, 1, 4),
    _HwMGMonitorGroupStatus_Type()
)
hwMGMonitorGroupStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMGMonitorGroupStatus.setStatus("current")
_HwMGMonitorGroupDelayTime_Type = Unsigned32
_HwMGMonitorGroupDelayTime_Object = MibTableColumn
hwMGMonitorGroupDelayTime = _HwMGMonitorGroupDelayTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 312, 1, 1, 1, 5),
    _HwMGMonitorGroupDelayTime_Type()
)
hwMGMonitorGroupDelayTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMGMonitorGroupDelayTime.setStatus("current")
_HwMGBindingInterfaceTable_Object = MibTable
hwMGBindingInterfaceTable = _HwMGBindingInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 312, 1, 2)
)
if mibBuilder.loadTexts:
    hwMGBindingInterfaceTable.setStatus("current")
_HwMGBindingInterfaceEntry_Object = MibTableRow
hwMGBindingInterfaceEntry = _HwMGBindingInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 312, 1, 2, 1)
)
hwMGBindingInterfaceEntry.setIndexNames(
    (0, "HUAWEI-MG-MIB", "hwMGMonitorGroupIndex"),
    (0, "HUAWEI-MG-MIB", "hwMGBindingInterfaceIndex"),
)
if mibBuilder.loadTexts:
    hwMGBindingInterfaceEntry.setStatus("current")
_HwMGBindingInterfaceIndex_Type = InterfaceIndex
_HwMGBindingInterfaceIndex_Object = MibTableColumn
hwMGBindingInterfaceIndex = _HwMGBindingInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 312, 1, 2, 1, 1),
    _HwMGBindingInterfaceIndex_Type()
)
hwMGBindingInterfaceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMGBindingInterfaceIndex.setStatus("current")


class _HwMGBindingInterfaceWeight_Type(Integer32):
    """Custom type hwMGBindingInterfaceWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_HwMGBindingInterfaceWeight_Type.__name__ = "Integer32"
_HwMGBindingInterfaceWeight_Object = MibTableColumn
hwMGBindingInterfaceWeight = _HwMGBindingInterfaceWeight_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 312, 1, 2, 1, 2),
    _HwMGBindingInterfaceWeight_Type()
)
hwMGBindingInterfaceWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMGBindingInterfaceWeight.setStatus("current")
_HwMGTrackInterfaceTable_Object = MibTable
hwMGTrackInterfaceTable = _HwMGTrackInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 312, 1, 3)
)
if mibBuilder.loadTexts:
    hwMGTrackInterfaceTable.setStatus("current")
_HwMGTrackInterfaceEntry_Object = MibTableRow
hwMGTrackInterfaceEntry = _HwMGTrackInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 312, 1, 3, 1)
)
hwMGTrackInterfaceEntry.setIndexNames(
    (0, "HUAWEI-MG-MIB", "hwMGMonitorGroupIndex"),
    (0, "HUAWEI-MG-MIB", "hwMGTrackInterfaceIndex"),
)
if mibBuilder.loadTexts:
    hwMGTrackInterfaceEntry.setStatus("current")
_HwMGTrackInterfaceIndex_Type = InterfaceIndex
_HwMGTrackInterfaceIndex_Object = MibTableColumn
hwMGTrackInterfaceIndex = _HwMGTrackInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 312, 1, 3, 1, 1),
    _HwMGTrackInterfaceIndex_Type()
)
hwMGTrackInterfaceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMGTrackInterfaceIndex.setStatus("current")


class _HwMGTrackInterfaceWeight_Type(Integer32):
    """Custom type hwMGTrackInterfaceWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_HwMGTrackInterfaceWeight_Type.__name__ = "Integer32"
_HwMGTrackInterfaceWeight_Object = MibTableColumn
hwMGTrackInterfaceWeight = _HwMGTrackInterfaceWeight_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 312, 1, 3, 1, 2),
    _HwMGTrackInterfaceWeight_Type()
)
hwMGTrackInterfaceWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMGTrackInterfaceWeight.setStatus("current")


class _HwMGTrackInterfaceTriggerStatus_Type(Integer32):
    """Custom type hwMGTrackInterfaceTriggerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 3),
          ("triggerdown", 2),
          ("triggerup", 1))
    )


_HwMGTrackInterfaceTriggerStatus_Type.__name__ = "Integer32"
_HwMGTrackInterfaceTriggerStatus_Object = MibTableColumn
hwMGTrackInterfaceTriggerStatus = _HwMGTrackInterfaceTriggerStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 312, 1, 3, 1, 3),
    _HwMGTrackInterfaceTriggerStatus_Type()
)
hwMGTrackInterfaceTriggerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMGTrackInterfaceTriggerStatus.setStatus("current")
_HwMonitorGroupConformance_ObjectIdentity = ObjectIdentity
hwMonitorGroupConformance = _HwMonitorGroupConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 312, 4)
)
_HwMonitorGroupGroups_ObjectIdentity = ObjectIdentity
hwMonitorGroupGroups = _HwMonitorGroupGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 312, 4, 1)
)
_HwMonitorGroupCompliances_ObjectIdentity = ObjectIdentity
hwMonitorGroupCompliances = _HwMonitorGroupCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 312, 4, 2)
)

# Managed Objects groups

hwMGMonitorGroupGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 312, 4, 1, 1)
)
hwMGMonitorGroupGroup.setObjects(
      *(("HUAWEI-MG-MIB", "hwMGMonitorGroupName"),
        ("HUAWEI-MG-MIB", "hwMGMonitorGroupDownWeight"),
        ("HUAWEI-MG-MIB", "hwMGMonitorGroupStatus"),
        ("HUAWEI-MG-MIB", "hwMGMonitorGroupDelayTime"))
)
if mibBuilder.loadTexts:
    hwMGMonitorGroupGroup.setStatus("current")

hwMGBindingInterfaceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 312, 4, 1, 2)
)
hwMGBindingInterfaceGroup.setObjects(
    ("HUAWEI-MG-MIB", "hwMGBindingInterfaceWeight")
)
if mibBuilder.loadTexts:
    hwMGBindingInterfaceGroup.setStatus("current")

hwMGTrackInterfaceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 312, 4, 1, 3)
)
hwMGTrackInterfaceGroup.setObjects(
      *(("HUAWEI-MG-MIB", "hwMGTrackInterfaceWeight"),
        ("HUAWEI-MG-MIB", "hwMGTrackInterfaceTriggerStatus"))
)
if mibBuilder.loadTexts:
    hwMGTrackInterfaceGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hwMonitorGroupCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 312, 4, 2, 1)
)
if mibBuilder.loadTexts:
    hwMonitorGroupCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-MG-MIB",
    **{"hwMG": hwMG,
       "hwMGMonitorGroupObjects": hwMGMonitorGroupObjects,
       "hwMGMonitorGroupTable": hwMGMonitorGroupTable,
       "hwMGMonitorGroupEntry": hwMGMonitorGroupEntry,
       "hwMGMonitorGroupIndex": hwMGMonitorGroupIndex,
       "hwMGMonitorGroupName": hwMGMonitorGroupName,
       "hwMGMonitorGroupDownWeight": hwMGMonitorGroupDownWeight,
       "hwMGMonitorGroupStatus": hwMGMonitorGroupStatus,
       "hwMGMonitorGroupDelayTime": hwMGMonitorGroupDelayTime,
       "hwMGBindingInterfaceTable": hwMGBindingInterfaceTable,
       "hwMGBindingInterfaceEntry": hwMGBindingInterfaceEntry,
       "hwMGBindingInterfaceIndex": hwMGBindingInterfaceIndex,
       "hwMGBindingInterfaceWeight": hwMGBindingInterfaceWeight,
       "hwMGTrackInterfaceTable": hwMGTrackInterfaceTable,
       "hwMGTrackInterfaceEntry": hwMGTrackInterfaceEntry,
       "hwMGTrackInterfaceIndex": hwMGTrackInterfaceIndex,
       "hwMGTrackInterfaceWeight": hwMGTrackInterfaceWeight,
       "hwMGTrackInterfaceTriggerStatus": hwMGTrackInterfaceTriggerStatus,
       "hwMonitorGroupConformance": hwMonitorGroupConformance,
       "hwMonitorGroupGroups": hwMonitorGroupGroups,
       "hwMGMonitorGroupGroup": hwMGMonitorGroupGroup,
       "hwMGBindingInterfaceGroup": hwMGBindingInterfaceGroup,
       "hwMGTrackInterfaceGroup": hwMGTrackInterfaceGroup,
       "hwMonitorGroupCompliances": hwMonitorGroupCompliances,
       "hwMonitorGroupCompliance": hwMonitorGroupCompliance}
)
