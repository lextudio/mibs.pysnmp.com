# SNMP MIB module (HUAWEI-GARP-APP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-GARP-APP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:03:53 2024
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

(ifEntry,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifEntry",
    "ifIndex")

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
 TextualConvention,
 TimeInterval) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeInterval")


# MODULE-IDENTITY

hwGarpAppMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 213)
)
hwGarpAppMIB.setRevisions(
        ("2009-09-27 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class InterfaceIndex(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



# MIB Managed Objects in the order of their OIDs

_HwGarpAppProtoObject_ObjectIdentity = ObjectIdentity
hwGarpAppProtoObject = _HwGarpAppProtoObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 213, 1)
)
if mibBuilder.loadTexts:
    hwGarpAppProtoObject.setStatus("current")
_HwGarpAppLeaveAllTime_Type = TimeInterval
_HwGarpAppLeaveAllTime_Object = MibScalar
hwGarpAppLeaveAllTime = _HwGarpAppLeaveAllTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 213, 1, 1),
    _HwGarpAppLeaveAllTime_Type()
)
hwGarpAppLeaveAllTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwGarpAppLeaveAllTime.setStatus("current")
_HwGarpAppSwitchCountTable_Object = MibTable
hwGarpAppSwitchCountTable = _HwGarpAppSwitchCountTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 213, 1, 2)
)
if mibBuilder.loadTexts:
    hwGarpAppSwitchCountTable.setStatus("current")
_HwGarpAppSwitchCountEntry_Object = MibTableRow
hwGarpAppSwitchCountEntry = _HwGarpAppSwitchCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 213, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hwGarpAppSwitchCountEntry.setStatus("current")
_HwGarpAppSwitchGmrpRxPkt_Type = Counter32
_HwGarpAppSwitchGmrpRxPkt_Object = MibTableColumn
hwGarpAppSwitchGmrpRxPkt = _HwGarpAppSwitchGmrpRxPkt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 213, 1, 2, 1, 1),
    _HwGarpAppSwitchGmrpRxPkt_Type()
)
hwGarpAppSwitchGmrpRxPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwGarpAppSwitchGmrpRxPkt.setStatus("current")
_HwGarpAppSwitchGvrpRxPkt_Type = Counter32
_HwGarpAppSwitchGvrpRxPkt_Object = MibTableColumn
hwGarpAppSwitchGvrpRxPkt = _HwGarpAppSwitchGvrpRxPkt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 213, 1, 2, 1, 2),
    _HwGarpAppSwitchGvrpRxPkt_Type()
)
hwGarpAppSwitchGvrpRxPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwGarpAppSwitchGvrpRxPkt.setStatus("current")
_HwGarpAppSwitchGmrpTxPkt_Type = Counter32
_HwGarpAppSwitchGmrpTxPkt_Object = MibTableColumn
hwGarpAppSwitchGmrpTxPkt = _HwGarpAppSwitchGmrpTxPkt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 213, 1, 2, 1, 3),
    _HwGarpAppSwitchGmrpTxPkt_Type()
)
hwGarpAppSwitchGmrpTxPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwGarpAppSwitchGmrpTxPkt.setStatus("current")
_HwGarpAppSwitchGvrpTxPkt_Type = Counter32
_HwGarpAppSwitchGvrpTxPkt_Object = MibTableColumn
hwGarpAppSwitchGvrpTxPkt = _HwGarpAppSwitchGvrpTxPkt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 213, 1, 2, 1, 4),
    _HwGarpAppSwitchGvrpTxPkt_Type()
)
hwGarpAppSwitchGvrpTxPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwGarpAppSwitchGvrpTxPkt.setStatus("current")
_HwGarpAppSwitchDiscardedPkt_Type = Counter32
_HwGarpAppSwitchDiscardedPkt_Object = MibTableColumn
hwGarpAppSwitchDiscardedPkt = _HwGarpAppSwitchDiscardedPkt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 213, 1, 2, 1, 5),
    _HwGarpAppSwitchDiscardedPkt_Type()
)
hwGarpAppSwitchDiscardedPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwGarpAppSwitchDiscardedPkt.setStatus("current")


class _HwGarpAppSwitchGarpStatClear_Type(Integer32):
    """Custom type hwGarpAppSwitchGarpStatClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear", 1)
    )


_HwGarpAppSwitchGarpStatClear_Type.__name__ = "Integer32"
_HwGarpAppSwitchGarpStatClear_Object = MibTableColumn
hwGarpAppSwitchGarpStatClear = _HwGarpAppSwitchGarpStatClear_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 213, 1, 2, 1, 6),
    _HwGarpAppSwitchGarpStatClear_Type()
)
hwGarpAppSwitchGarpStatClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwGarpAppSwitchGarpStatClear.setStatus("current")
_HwGarpAppHoldTimeTable_Object = MibTable
hwGarpAppHoldTimeTable = _HwGarpAppHoldTimeTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 213, 1, 3)
)
if mibBuilder.loadTexts:
    hwGarpAppHoldTimeTable.setStatus("current")
_HwGarpAppHoldTimeEntry_Object = MibTableRow
hwGarpAppHoldTimeEntry = _HwGarpAppHoldTimeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 213, 1, 3, 1)
)
if mibBuilder.loadTexts:
    hwGarpAppHoldTimeEntry.setStatus("current")


class _HwGarpAppHoldTime_Type(Integer32):
    """Custom type hwGarpAppHoldTime based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 32765),
    )


_HwGarpAppHoldTime_Type.__name__ = "Integer32"
_HwGarpAppHoldTime_Object = MibTableColumn
hwGarpAppHoldTime = _HwGarpAppHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 213, 1, 3, 1, 1),
    _HwGarpAppHoldTime_Type()
)
hwGarpAppHoldTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwGarpAppHoldTime.setStatus("current")
_HwGarpAppInfObject_ObjectIdentity = ObjectIdentity
hwGarpAppInfObject = _HwGarpAppInfObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 213, 2)
)
_HwGarpAppTrunkStatusTable_Object = MibTable
hwGarpAppTrunkStatusTable = _HwGarpAppTrunkStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 213, 2, 1)
)
if mibBuilder.loadTexts:
    hwGarpAppTrunkStatusTable.setStatus("current")
_HwGarpAppTrunkStatusEntry_Object = MibTableRow
hwGarpAppTrunkStatusEntry = _HwGarpAppTrunkStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 213, 2, 1, 1)
)
hwGarpAppTrunkStatusEntry.setIndexNames(
    (0, "HUAWEI-GARP-APP-MIB", "hwGarpAppTrunkIndex"),
)
if mibBuilder.loadTexts:
    hwGarpAppTrunkStatusEntry.setStatus("current")
_HwGarpAppTrunkIndex_Type = InterfaceIndex
_HwGarpAppTrunkIndex_Object = MibTableColumn
hwGarpAppTrunkIndex = _HwGarpAppTrunkIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 213, 2, 1, 1, 1),
    _HwGarpAppTrunkIndex_Type()
)
hwGarpAppTrunkIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwGarpAppTrunkIndex.setStatus("current")


class _HwGarpAppTrunkGvrpRegistration_Type(Integer32):
    """Custom type hwGarpAppTrunkGvrpRegistration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fixed", 2),
          ("forbidden", 3),
          ("normal", 1))
    )


_HwGarpAppTrunkGvrpRegistration_Type.__name__ = "Integer32"
_HwGarpAppTrunkGvrpRegistration_Object = MibTableColumn
hwGarpAppTrunkGvrpRegistration = _HwGarpAppTrunkGvrpRegistration_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 213, 2, 1, 1, 2),
    _HwGarpAppTrunkGvrpRegistration_Type()
)
hwGarpAppTrunkGvrpRegistration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwGarpAppTrunkGvrpRegistration.setStatus("current")
_HwGarpAppTrunkPassListLow_Type = OctetString
_HwGarpAppTrunkPassListLow_Object = MibTableColumn
hwGarpAppTrunkPassListLow = _HwGarpAppTrunkPassListLow_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 213, 2, 1, 1, 3),
    _HwGarpAppTrunkPassListLow_Type()
)
hwGarpAppTrunkPassListLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwGarpAppTrunkPassListLow.setStatus("current")
_HwGarpAppTrunkPassListHigh_Type = OctetString
_HwGarpAppTrunkPassListHigh_Object = MibTableColumn
hwGarpAppTrunkPassListHigh = _HwGarpAppTrunkPassListHigh_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 213, 2, 1, 1, 4),
    _HwGarpAppTrunkPassListHigh_Type()
)
hwGarpAppTrunkPassListHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwGarpAppTrunkPassListHigh.setStatus("current")
_HwGarpAppConformance_ObjectIdentity = ObjectIdentity
hwGarpAppConformance = _HwGarpAppConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 213, 3)
)
_HwGarpAppCompliances_ObjectIdentity = ObjectIdentity
hwGarpAppCompliances = _HwGarpAppCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 213, 3, 1)
)
_HwGarpAppGroups_ObjectIdentity = ObjectIdentity
hwGarpAppGroups = _HwGarpAppGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 213, 3, 2)
)
hwGarpAppTrunkStatusEntry.registerAugmentions(
    ("HUAWEI-GARP-APP-MIB",
     "hwGarpAppSwitchCountEntry")
)
hwGarpAppSwitchCountEntry.setIndexNames(*hwGarpAppTrunkStatusEntry.getIndexNames())
ifEntry.registerAugmentions(
    ("HUAWEI-GARP-APP-MIB",
     "hwGarpAppHoldTimeEntry")
)
hwGarpAppHoldTimeEntry.setIndexNames(*ifEntry.getIndexNames())

# Managed Objects groups

hwGarpAppGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 213, 3, 2, 1)
)
hwGarpAppGroup.setObjects(
      *(("HUAWEI-GARP-APP-MIB", "hwGarpAppLeaveAllTime"),
        ("HUAWEI-GARP-APP-MIB", "hwGarpAppSwitchGmrpRxPkt"),
        ("HUAWEI-GARP-APP-MIB", "hwGarpAppSwitchGvrpRxPkt"),
        ("HUAWEI-GARP-APP-MIB", "hwGarpAppSwitchGmrpTxPkt"),
        ("HUAWEI-GARP-APP-MIB", "hwGarpAppSwitchGvrpTxPkt"),
        ("HUAWEI-GARP-APP-MIB", "hwGarpAppSwitchDiscardedPkt"),
        ("HUAWEI-GARP-APP-MIB", "hwGarpAppSwitchGarpStatClear"),
        ("HUAWEI-GARP-APP-MIB", "hwGarpAppHoldTime"),
        ("HUAWEI-GARP-APP-MIB", "hwGarpAppTrunkGvrpRegistration"),
        ("HUAWEI-GARP-APP-MIB", "hwGarpAppTrunkPassListLow"),
        ("HUAWEI-GARP-APP-MIB", "hwGarpAppTrunkPassListHigh"))
)
if mibBuilder.loadTexts:
    hwGarpAppGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hwGarpAppCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 213, 3, 1, 1)
)
if mibBuilder.loadTexts:
    hwGarpAppCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-GARP-APP-MIB",
    **{"InterfaceIndex": InterfaceIndex,
       "hwGarpAppMIB": hwGarpAppMIB,
       "hwGarpAppProtoObject": hwGarpAppProtoObject,
       "hwGarpAppLeaveAllTime": hwGarpAppLeaveAllTime,
       "hwGarpAppSwitchCountTable": hwGarpAppSwitchCountTable,
       "hwGarpAppSwitchCountEntry": hwGarpAppSwitchCountEntry,
       "hwGarpAppSwitchGmrpRxPkt": hwGarpAppSwitchGmrpRxPkt,
       "hwGarpAppSwitchGvrpRxPkt": hwGarpAppSwitchGvrpRxPkt,
       "hwGarpAppSwitchGmrpTxPkt": hwGarpAppSwitchGmrpTxPkt,
       "hwGarpAppSwitchGvrpTxPkt": hwGarpAppSwitchGvrpTxPkt,
       "hwGarpAppSwitchDiscardedPkt": hwGarpAppSwitchDiscardedPkt,
       "hwGarpAppSwitchGarpStatClear": hwGarpAppSwitchGarpStatClear,
       "hwGarpAppHoldTimeTable": hwGarpAppHoldTimeTable,
       "hwGarpAppHoldTimeEntry": hwGarpAppHoldTimeEntry,
       "hwGarpAppHoldTime": hwGarpAppHoldTime,
       "hwGarpAppInfObject": hwGarpAppInfObject,
       "hwGarpAppTrunkStatusTable": hwGarpAppTrunkStatusTable,
       "hwGarpAppTrunkStatusEntry": hwGarpAppTrunkStatusEntry,
       "hwGarpAppTrunkIndex": hwGarpAppTrunkIndex,
       "hwGarpAppTrunkGvrpRegistration": hwGarpAppTrunkGvrpRegistration,
       "hwGarpAppTrunkPassListLow": hwGarpAppTrunkPassListLow,
       "hwGarpAppTrunkPassListHigh": hwGarpAppTrunkPassListHigh,
       "hwGarpAppConformance": hwGarpAppConformance,
       "hwGarpAppCompliances": hwGarpAppCompliances,
       "hwGarpAppCompliance": hwGarpAppCompliance,
       "hwGarpAppGroups": hwGarpAppGroups,
       "hwGarpAppGroup": hwGarpAppGroup}
)
