# SNMP MIB module (HUAWEI-LDT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-LDT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:04:32 2024
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

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

(VlanId,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId")

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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hwLdtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 174)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwLdtObjects_ObjectIdentity = ObjectIdentity
hwLdtObjects = _HwLdtObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 174, 1)
)
_HwLdtConfiguration_ObjectIdentity = ObjectIdentity
hwLdtConfiguration = _HwLdtConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 174, 1, 1)
)


class _HwLdtEnable_Type(Integer32):
    """Custom type hwLdtEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_HwLdtEnable_Type.__name__ = "Integer32"
_HwLdtEnable_Object = MibScalar
hwLdtEnable = _HwLdtEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 174, 1, 1, 1),
    _HwLdtEnable_Type()
)
hwLdtEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwLdtEnable.setStatus("current")


class _HwLdtIntervalTime_Type(Integer32):
    """Custom type hwLdtIntervalTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 300),
    )


_HwLdtIntervalTime_Type.__name__ = "Integer32"
_HwLdtIntervalTime_Object = MibScalar
hwLdtIntervalTime = _HwLdtIntervalTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 174, 1, 1, 2),
    _HwLdtIntervalTime_Type()
)
hwLdtIntervalTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwLdtIntervalTime.setStatus("current")


class _HwLdtVlanListLow_Type(OctetString):
    """Custom type hwLdtVlanListLow based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(256, 256),
    )


_HwLdtVlanListLow_Type.__name__ = "OctetString"
_HwLdtVlanListLow_Object = MibScalar
hwLdtVlanListLow = _HwLdtVlanListLow_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 174, 1, 1, 3),
    _HwLdtVlanListLow_Type()
)
hwLdtVlanListLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwLdtVlanListLow.setStatus("current")


class _HwLdtVlanListHigh_Type(OctetString):
    """Custom type hwLdtVlanListHigh based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(256, 256),
    )


_HwLdtVlanListHigh_Type.__name__ = "OctetString"
_HwLdtVlanListHigh_Object = MibScalar
hwLdtVlanListHigh = _HwLdtVlanListHigh_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 174, 1, 1, 4),
    _HwLdtVlanListHigh_Type()
)
hwLdtVlanListHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwLdtVlanListHigh.setStatus("current")
_HwLdtPortConfigTable_Object = MibTable
hwLdtPortConfigTable = _HwLdtPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 174, 1, 1, 5)
)
if mibBuilder.loadTexts:
    hwLdtPortConfigTable.setStatus("current")
_HwLdtPortConfigEntry_Object = MibTableRow
hwLdtPortConfigEntry = _HwLdtPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 174, 1, 1, 5, 1)
)
hwLdtPortConfigEntry.setIndexNames(
    (0, "HUAWEI-LDT-MIB", "hwLdtInterfaceIndex"),
)
if mibBuilder.loadTexts:
    hwLdtPortConfigEntry.setStatus("current")
_HwLdtInterfaceIndex_Type = InterfaceIndex
_HwLdtInterfaceIndex_Object = MibTableColumn
hwLdtInterfaceIndex = _HwLdtInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 174, 1, 1, 5, 1, 1),
    _HwLdtInterfaceIndex_Type()
)
hwLdtInterfaceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwLdtInterfaceIndex.setStatus("current")


class _HwLdtInterfaceName_Type(OctetString):
    """Custom type hwLdtInterfaceName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_HwLdtInterfaceName_Type.__name__ = "OctetString"
_HwLdtInterfaceName_Object = MibTableColumn
hwLdtInterfaceName = _HwLdtInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 174, 1, 1, 5, 1, 2),
    _HwLdtInterfaceName_Type()
)
hwLdtInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLdtInterfaceName.setStatus("current")


class _HwLdtPortLdtEnable_Type(Integer32):
    """Custom type hwLdtPortLdtEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_HwLdtPortLdtEnable_Type.__name__ = "Integer32"
_HwLdtPortLdtEnable_Object = MibTableColumn
hwLdtPortLdtEnable = _HwLdtPortLdtEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 174, 1, 1, 5, 1, 3),
    _HwLdtPortLdtEnable_Type()
)
hwLdtPortLdtEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwLdtPortLdtEnable.setStatus("current")


class _HwLdtPortMode_Type(Integer32):
    """Custom type hwLdtPortMode based on Integer32"""
    defaultValue = 2

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
        *(("blocking", 2),
          ("noLearning", 3),
          ("shutdown", 4),
          ("trap", 1))
    )


_HwLdtPortMode_Type.__name__ = "Integer32"
_HwLdtPortMode_Object = MibTableColumn
hwLdtPortMode = _HwLdtPortMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 174, 1, 1, 5, 1, 4),
    _HwLdtPortMode_Type()
)
hwLdtPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwLdtPortMode.setStatus("current")


class _HwLdtPortStatus_Type(Integer32):
    """Custom type hwLdtPortStatus based on Integer32"""
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
        *(("blocking", 2),
          ("noLearning", 3),
          ("normal", 1),
          ("shutdown", 4))
    )


_HwLdtPortStatus_Type.__name__ = "Integer32"
_HwLdtPortStatus_Object = MibTableColumn
hwLdtPortStatus = _HwLdtPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 174, 1, 1, 5, 1, 5),
    _HwLdtPortStatus_Type()
)
hwLdtPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLdtPortStatus.setStatus("current")


class _HwLdtPortRecoveryTime_Type(Integer32):
    """Custom type hwLdtPortRecoveryTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HwLdtPortRecoveryTime_Type.__name__ = "Integer32"
_HwLdtPortRecoveryTime_Object = MibTableColumn
hwLdtPortRecoveryTime = _HwLdtPortRecoveryTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 174, 1, 1, 5, 1, 6),
    _HwLdtPortRecoveryTime_Type()
)
hwLdtPortRecoveryTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwLdtPortRecoveryTime.setStatus("current")
_HwLdtPortStatusTable_Object = MibTable
hwLdtPortStatusTable = _HwLdtPortStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 174, 1, 1, 6)
)
if mibBuilder.loadTexts:
    hwLdtPortStatusTable.setStatus("current")
_HwLdtPortStatusEntry_Object = MibTableRow
hwLdtPortStatusEntry = _HwLdtPortStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 174, 1, 1, 6, 1)
)
hwLdtPortStatusEntry.setIndexNames(
    (0, "HUAWEI-LDT-MIB", "hwLdtInterfaceIndex"),
    (0, "HUAWEI-LDT-MIB", "hwLdtPortVlanIDIndex"),
)
if mibBuilder.loadTexts:
    hwLdtPortStatusEntry.setStatus("current")
_HwLdtPortVlanIDIndex_Type = VlanId
_HwLdtPortVlanIDIndex_Object = MibTableColumn
hwLdtPortVlanIDIndex = _HwLdtPortVlanIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 174, 1, 1, 6, 1, 1),
    _HwLdtPortVlanIDIndex_Type()
)
hwLdtPortVlanIDIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwLdtPortVlanIDIndex.setStatus("current")


class _HwLdtPortVlanStatus_Type(Integer32):
    """Custom type hwLdtPortVlanStatus based on Integer32"""
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
        *(("blocking", 2),
          ("noLearning", 3),
          ("normal", 1),
          ("shutdown", 4))
    )


_HwLdtPortVlanStatus_Type.__name__ = "Integer32"
_HwLdtPortVlanStatus_Object = MibTableColumn
hwLdtPortVlanStatus = _HwLdtPortVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 174, 1, 1, 6, 1, 2),
    _HwLdtPortVlanStatus_Type()
)
hwLdtPortVlanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLdtPortVlanStatus.setStatus("current")
_HwPortLoopDetectTable_Object = MibTable
hwPortLoopDetectTable = _HwPortLoopDetectTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 174, 1, 1, 7)
)
if mibBuilder.loadTexts:
    hwPortLoopDetectTable.setStatus("current")
_HwPortLoopDetectEntry_Object = MibTableRow
hwPortLoopDetectEntry = _HwPortLoopDetectEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 174, 1, 1, 7, 1)
)
hwPortLoopDetectEntry.setIndexNames(
    (0, "HUAWEI-LDT-MIB", "hwPortLoopDetectIfIndex"),
)
if mibBuilder.loadTexts:
    hwPortLoopDetectEntry.setStatus("current")
_HwPortLoopDetectIfIndex_Type = InterfaceIndex
_HwPortLoopDetectIfIndex_Object = MibTableColumn
hwPortLoopDetectIfIndex = _HwPortLoopDetectIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 174, 1, 1, 7, 1, 1),
    _HwPortLoopDetectIfIndex_Type()
)
hwPortLoopDetectIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwPortLoopDetectIfIndex.setStatus("current")


class _HwLPortLoopDetectIfName_Type(OctetString):
    """Custom type hwLPortLoopDetectIfName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_HwLPortLoopDetectIfName_Type.__name__ = "OctetString"
_HwLPortLoopDetectIfName_Object = MibTableColumn
hwLPortLoopDetectIfName = _HwLPortLoopDetectIfName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 174, 1, 1, 7, 1, 2),
    _HwLPortLoopDetectIfName_Type()
)
hwLPortLoopDetectIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLPortLoopDetectIfName.setStatus("current")
_HwPortLoopDetectEnabled_Type = EnabledStatus
_HwPortLoopDetectEnabled_Object = MibTableColumn
hwPortLoopDetectEnabled = _HwPortLoopDetectEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 174, 1, 1, 7, 1, 3),
    _HwPortLoopDetectEnabled_Type()
)
hwPortLoopDetectEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPortLoopDetectEnabled.setStatus("current")


class _HwPortLoopDetectRecoveryTime_Type(Integer32):
    """Custom type hwPortLoopDetectRecoveryTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HwPortLoopDetectRecoveryTime_Type.__name__ = "Integer32"
_HwPortLoopDetectRecoveryTime_Object = MibTableColumn
hwPortLoopDetectRecoveryTime = _HwPortLoopDetectRecoveryTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 174, 1, 1, 7, 1, 4),
    _HwPortLoopDetectRecoveryTime_Type()
)
hwPortLoopDetectRecoveryTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPortLoopDetectRecoveryTime.setStatus("current")


class _HwPortLoopDetectAction_Type(Integer32):
    """Custom type hwPortLoopDetectAction based on Integer32"""
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
        *(("blocking", 2),
          ("noLearning", 4),
          ("shutdown", 1),
          ("trap", 3))
    )


_HwPortLoopDetectAction_Type.__name__ = "Integer32"
_HwPortLoopDetectAction_Object = MibTableColumn
hwPortLoopDetectAction = _HwPortLoopDetectAction_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 174, 1, 1, 7, 1, 5),
    _HwPortLoopDetectAction_Type()
)
hwPortLoopDetectAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPortLoopDetectAction.setStatus("current")


class _HwPortLoopDetectStatus_Type(Integer32):
    """Custom type hwPortLoopDetectStatus based on Integer32"""
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
        *(("blocking", 2),
          ("noLearning", 5),
          ("normal", 1),
          ("shutdown", 3),
          ("trap", 4))
    )


_HwPortLoopDetectStatus_Type.__name__ = "Integer32"
_HwPortLoopDetectStatus_Object = MibTableColumn
hwPortLoopDetectStatus = _HwPortLoopDetectStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 174, 1, 1, 7, 1, 6),
    _HwPortLoopDetectStatus_Type()
)
hwPortLoopDetectStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPortLoopDetectStatus.setStatus("current")


class _HwPortLoopDetectProtocol_Type(OctetString):
    """Custom type hwPortLoopDetectProtocol based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_HwPortLoopDetectProtocol_Type.__name__ = "OctetString"
_HwPortLoopDetectProtocol_Object = MibTableColumn
hwPortLoopDetectProtocol = _HwPortLoopDetectProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 174, 1, 1, 7, 1, 7),
    _HwPortLoopDetectProtocol_Type()
)
hwPortLoopDetectProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPortLoopDetectProtocol.setStatus("current")


class _HwPortLoopDetectVlanLow_Type(OctetString):
    """Custom type hwPortLoopDetectVlanLow based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(256, 256),
    )


_HwPortLoopDetectVlanLow_Type.__name__ = "OctetString"
_HwPortLoopDetectVlanLow_Object = MibTableColumn
hwPortLoopDetectVlanLow = _HwPortLoopDetectVlanLow_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 174, 1, 1, 7, 1, 8),
    _HwPortLoopDetectVlanLow_Type()
)
hwPortLoopDetectVlanLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPortLoopDetectVlanLow.setStatus("current")


class _HwPortLoopDetectVlanHigh_Type(OctetString):
    """Custom type hwPortLoopDetectVlanHigh based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(256, 256),
    )


_HwPortLoopDetectVlanHigh_Type.__name__ = "OctetString"
_HwPortLoopDetectVlanHigh_Object = MibTableColumn
hwPortLoopDetectVlanHigh = _HwPortLoopDetectVlanHigh_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 174, 1, 1, 7, 1, 9),
    _HwPortLoopDetectVlanHigh_Type()
)
hwPortLoopDetectVlanHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPortLoopDetectVlanHigh.setStatus("current")


class _HwLoopDetectInterval_Type(Integer32):
    """Custom type hwLoopDetectInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 300),
    )


_HwLoopDetectInterval_Type.__name__ = "Integer32"
_HwLoopDetectInterval_Object = MibScalar
hwLoopDetectInterval = _HwLoopDetectInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 174, 1, 1, 8),
    _HwLoopDetectInterval_Type()
)
hwLoopDetectInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwLoopDetectInterval.setStatus("current")


class _HwLoopDetectSendingPacketInterval_Type(Integer32):
    """Custom type hwLoopDetectSendingPacketInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_HwLoopDetectSendingPacketInterval_Type.__name__ = "Integer32"
_HwLoopDetectSendingPacketInterval_Object = MibScalar
hwLoopDetectSendingPacketInterval = _HwLoopDetectSendingPacketInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 174, 1, 1, 9),
    _HwLoopDetectSendingPacketInterval_Type()
)
hwLoopDetectSendingPacketInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwLoopDetectSendingPacketInterval.setStatus("current")
_HwLdtPortTrapObjects_ObjectIdentity = ObjectIdentity
hwLdtPortTrapObjects = _HwLdtPortTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 174, 2)
)


class _HwLdtPortLoopVlanListLow_Type(OctetString):
    """Custom type hwLdtPortLoopVlanListLow based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(256, 256),
    )


_HwLdtPortLoopVlanListLow_Type.__name__ = "OctetString"
_HwLdtPortLoopVlanListLow_Object = MibScalar
hwLdtPortLoopVlanListLow = _HwLdtPortLoopVlanListLow_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 174, 2, 1),
    _HwLdtPortLoopVlanListLow_Type()
)
hwLdtPortLoopVlanListLow.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwLdtPortLoopVlanListLow.setStatus("current")


class _HwLdtPortLoopVlanListHigh_Type(OctetString):
    """Custom type hwLdtPortLoopVlanListHigh based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(256, 256),
    )


_HwLdtPortLoopVlanListHigh_Type.__name__ = "OctetString"
_HwLdtPortLoopVlanListHigh_Object = MibScalar
hwLdtPortLoopVlanListHigh = _HwLdtPortLoopVlanListHigh_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 174, 2, 2),
    _HwLdtPortLoopVlanListHigh_Type()
)
hwLdtPortLoopVlanListHigh.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwLdtPortLoopVlanListHigh.setStatus("current")


class _HwLdtPortRecoverVlanListLow_Type(OctetString):
    """Custom type hwLdtPortRecoverVlanListLow based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(256, 256),
    )


_HwLdtPortRecoverVlanListLow_Type.__name__ = "OctetString"
_HwLdtPortRecoverVlanListLow_Object = MibScalar
hwLdtPortRecoverVlanListLow = _HwLdtPortRecoverVlanListLow_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 174, 2, 3),
    _HwLdtPortRecoverVlanListLow_Type()
)
hwLdtPortRecoverVlanListLow.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwLdtPortRecoverVlanListLow.setStatus("current")


class _HwLdtPortRecoverVlanListHigh_Type(OctetString):
    """Custom type hwLdtPortRecoverVlanListHigh based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(256, 256),
    )


_HwLdtPortRecoverVlanListHigh_Type.__name__ = "OctetString"
_HwLdtPortRecoverVlanListHigh_Object = MibScalar
hwLdtPortRecoverVlanListHigh = _HwLdtPortRecoverVlanListHigh_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 174, 2, 4),
    _HwLdtPortRecoverVlanListHigh_Type()
)
hwLdtPortRecoverVlanListHigh.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwLdtPortRecoverVlanListHigh.setStatus("current")


class _HwLdtPortLoopDetectVlanList_Type(OctetString):
    """Custom type hwLdtPortLoopDetectVlanList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_HwLdtPortLoopDetectVlanList_Type.__name__ = "OctetString"
_HwLdtPortLoopDetectVlanList_Object = MibScalar
hwLdtPortLoopDetectVlanList = _HwLdtPortLoopDetectVlanList_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 174, 2, 5),
    _HwLdtPortLoopDetectVlanList_Type()
)
hwLdtPortLoopDetectVlanList.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwLdtPortLoopDetectVlanList.setStatus("current")
_HwLdtTraps_ObjectIdentity = ObjectIdentity
hwLdtTraps = _HwLdtTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 174, 3)
)
_HwLdtConformance_ObjectIdentity = ObjectIdentity
hwLdtConformance = _HwLdtConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 174, 4)
)
_HwLdtConformances_ObjectIdentity = ObjectIdentity
hwLdtConformances = _HwLdtConformances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 174, 4, 1)
)
_HwLdtGroups_ObjectIdentity = ObjectIdentity
hwLdtGroups = _HwLdtGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 174, 4, 2)
)

# Managed Objects groups

hwLdtConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 174, 4, 2, 1)
)
hwLdtConfigGroup.setObjects(
      *(("HUAWEI-LDT-MIB", "hwLdtEnable"),
        ("HUAWEI-LDT-MIB", "hwLdtIntervalTime"),
        ("HUAWEI-LDT-MIB", "hwLdtVlanListLow"),
        ("HUAWEI-LDT-MIB", "hwLdtVlanListHigh"),
        ("HUAWEI-LDT-MIB", "hwLoopDetectInterval"),
        ("HUAWEI-LDT-MIB", "hwLoopDetectSendingPacketInterval"))
)
if mibBuilder.loadTexts:
    hwLdtConfigGroup.setStatus("current")

hwLdtPortConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 174, 4, 2, 2)
)
hwLdtPortConfigGroup.setObjects(
      *(("HUAWEI-LDT-MIB", "hwLdtPortLdtEnable"),
        ("HUAWEI-LDT-MIB", "hwLdtInterfaceName"),
        ("HUAWEI-LDT-MIB", "hwLdtPortMode"),
        ("HUAWEI-LDT-MIB", "hwLdtPortStatus"),
        ("HUAWEI-LDT-MIB", "hwLdtPortRecoveryTime"),
        ("HUAWEI-LDT-MIB", "hwLPortLoopDetectIfName"),
        ("HUAWEI-LDT-MIB", "hwPortLoopDetectEnabled"),
        ("HUAWEI-LDT-MIB", "hwPortLoopDetectRecoveryTime"),
        ("HUAWEI-LDT-MIB", "hwPortLoopDetectAction"),
        ("HUAWEI-LDT-MIB", "hwPortLoopDetectStatus"),
        ("HUAWEI-LDT-MIB", "hwPortLoopDetectProtocol"),
        ("HUAWEI-LDT-MIB", "hwPortLoopDetectVlanLow"),
        ("HUAWEI-LDT-MIB", "hwPortLoopDetectVlanHigh"))
)
if mibBuilder.loadTexts:
    hwLdtPortConfigGroup.setStatus("current")

hwLdtTrapPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 174, 4, 2, 3)
)
hwLdtTrapPortGroup.setObjects(
      *(("HUAWEI-LDT-MIB", "hwLdtPortLoopVlanListLow"),
        ("HUAWEI-LDT-MIB", "hwLdtPortLoopVlanListHigh"),
        ("HUAWEI-LDT-MIB", "hwLdtPortRecoverVlanListLow"),
        ("HUAWEI-LDT-MIB", "hwLdtPortRecoverVlanListHigh"),
        ("HUAWEI-LDT-MIB", "hwLdtPortLoopDetectVlanList"))
)
if mibBuilder.loadTexts:
    hwLdtTrapPortGroup.setStatus("current")


# Notification objects

hwLdtPortLoop = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 174, 3, 1)
)
hwLdtPortLoop.setObjects(
      *(("HUAWEI-LDT-MIB", "hwLdtInterfaceName"),
        ("HUAWEI-LDT-MIB", "hwLdtPortLoopVlanListLow"),
        ("HUAWEI-LDT-MIB", "hwLdtPortLoopVlanListHigh"))
)
if mibBuilder.loadTexts:
    hwLdtPortLoop.setStatus(
        "current"
    )

hwLdtPortRecovry = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 174, 3, 2)
)
hwLdtPortRecovry.setObjects(
      *(("HUAWEI-LDT-MIB", "hwLdtInterfaceName"),
        ("HUAWEI-LDT-MIB", "hwLdtPortRecoverVlanListLow"),
        ("HUAWEI-LDT-MIB", "hwLdtPortRecoverVlanListHigh"))
)
if mibBuilder.loadTexts:
    hwLdtPortRecovry.setStatus(
        "current"
    )

hwLdtPortLoopDetect = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 174, 3, 3)
)
hwLdtPortLoopDetect.setObjects(
      *(("HUAWEI-LDT-MIB", "hwLPortLoopDetectIfName"),
        ("HUAWEI-LDT-MIB", "hwLdtPortLoopDetectVlanList"),
        ("HUAWEI-LDT-MIB", "hwPortLoopDetectStatus"))
)
if mibBuilder.loadTexts:
    hwLdtPortLoopDetect.setStatus(
        "current"
    )

hwLdtPortLoopDetectRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 174, 3, 4)
)
hwLdtPortLoopDetectRecovery.setObjects(
      *(("HUAWEI-LDT-MIB", "hwLPortLoopDetectIfName"),
        ("HUAWEI-LDT-MIB", "hwPortLoopDetectStatus"))
)
if mibBuilder.loadTexts:
    hwLdtPortLoopDetectRecovery.setStatus(
        "current"
    )


# Notifications groups

hwLdtTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 174, 4, 2, 4)
)
hwLdtTrapGroup.setObjects(
      *(("HUAWEI-LDT-MIB", "hwLdtPortLoop"),
        ("HUAWEI-LDT-MIB", "hwLdtPortRecovry"),
        ("HUAWEI-LDT-MIB", "hwLdtPortLoopDetect"),
        ("HUAWEI-LDT-MIB", "hwLdtPortLoopDetectRecovery"))
)
if mibBuilder.loadTexts:
    hwLdtTrapGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hwLdtCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 174, 4, 1, 1)
)
if mibBuilder.loadTexts:
    hwLdtCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-LDT-MIB",
    **{"hwLdtMIB": hwLdtMIB,
       "hwLdtObjects": hwLdtObjects,
       "hwLdtConfiguration": hwLdtConfiguration,
       "hwLdtEnable": hwLdtEnable,
       "hwLdtIntervalTime": hwLdtIntervalTime,
       "hwLdtVlanListLow": hwLdtVlanListLow,
       "hwLdtVlanListHigh": hwLdtVlanListHigh,
       "hwLdtPortConfigTable": hwLdtPortConfigTable,
       "hwLdtPortConfigEntry": hwLdtPortConfigEntry,
       "hwLdtInterfaceIndex": hwLdtInterfaceIndex,
       "hwLdtInterfaceName": hwLdtInterfaceName,
       "hwLdtPortLdtEnable": hwLdtPortLdtEnable,
       "hwLdtPortMode": hwLdtPortMode,
       "hwLdtPortStatus": hwLdtPortStatus,
       "hwLdtPortRecoveryTime": hwLdtPortRecoveryTime,
       "hwLdtPortStatusTable": hwLdtPortStatusTable,
       "hwLdtPortStatusEntry": hwLdtPortStatusEntry,
       "hwLdtPortVlanIDIndex": hwLdtPortVlanIDIndex,
       "hwLdtPortVlanStatus": hwLdtPortVlanStatus,
       "hwPortLoopDetectTable": hwPortLoopDetectTable,
       "hwPortLoopDetectEntry": hwPortLoopDetectEntry,
       "hwPortLoopDetectIfIndex": hwPortLoopDetectIfIndex,
       "hwLPortLoopDetectIfName": hwLPortLoopDetectIfName,
       "hwPortLoopDetectEnabled": hwPortLoopDetectEnabled,
       "hwPortLoopDetectRecoveryTime": hwPortLoopDetectRecoveryTime,
       "hwPortLoopDetectAction": hwPortLoopDetectAction,
       "hwPortLoopDetectStatus": hwPortLoopDetectStatus,
       "hwPortLoopDetectProtocol": hwPortLoopDetectProtocol,
       "hwPortLoopDetectVlanLow": hwPortLoopDetectVlanLow,
       "hwPortLoopDetectVlanHigh": hwPortLoopDetectVlanHigh,
       "hwLoopDetectInterval": hwLoopDetectInterval,
       "hwLoopDetectSendingPacketInterval": hwLoopDetectSendingPacketInterval,
       "hwLdtPortTrapObjects": hwLdtPortTrapObjects,
       "hwLdtPortLoopVlanListLow": hwLdtPortLoopVlanListLow,
       "hwLdtPortLoopVlanListHigh": hwLdtPortLoopVlanListHigh,
       "hwLdtPortRecoverVlanListLow": hwLdtPortRecoverVlanListLow,
       "hwLdtPortRecoverVlanListHigh": hwLdtPortRecoverVlanListHigh,
       "hwLdtPortLoopDetectVlanList": hwLdtPortLoopDetectVlanList,
       "hwLdtTraps": hwLdtTraps,
       "hwLdtPortLoop": hwLdtPortLoop,
       "hwLdtPortRecovry": hwLdtPortRecovry,
       "hwLdtPortLoopDetect": hwLdtPortLoopDetect,
       "hwLdtPortLoopDetectRecovery": hwLdtPortLoopDetectRecovery,
       "hwLdtConformance": hwLdtConformance,
       "hwLdtConformances": hwLdtConformances,
       "hwLdtCompliance": hwLdtCompliance,
       "hwLdtGroups": hwLdtGroups,
       "hwLdtConfigGroup": hwLdtConfigGroup,
       "hwLdtPortConfigGroup": hwLdtPortConfigGroup,
       "hwLdtTrapPortGroup": hwLdtTrapPortGroup,
       "hwLdtTrapGroup": hwLdtTrapGroup}
)
