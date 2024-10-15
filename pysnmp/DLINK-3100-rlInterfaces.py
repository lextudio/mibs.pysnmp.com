# SNMP MIB module (DLINK-3100-rlInterfaces) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DLINK-3100-rlInterfaces
# Produced by pysmi-1.5.4 at Mon Oct 14 21:30:35 2024
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

(rlIfInterfaces,
 swInterfaces) = mibBuilder.importSymbols(
    "DLINK-3100-MIB",
    "rlIfInterfaces",
    "swInterfaces")

(InterfaceIndex,
 InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero",
    "ifIndex")

(PortList,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



class AutoNegCapabilitiesBits(Bits, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_SwIfTable_Object = MibTable
swIfTable = _SwIfTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 43, 1)
)
if mibBuilder.loadTexts:
    swIfTable.setStatus("current")
_SwIfEntry_Object = MibTableRow
swIfEntry = _SwIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 43, 1, 1)
)
swIfEntry.setIndexNames(
    (0, "DLINK-3100-rlInterfaces", "swIfIndex"),
)
if mibBuilder.loadTexts:
    swIfEntry.setStatus("current")
_SwIfIndex_Type = Integer32
_SwIfIndex_Object = MibTableColumn
swIfIndex = _SwIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 43, 1, 1, 1),
    _SwIfIndex_Type()
)
swIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIfIndex.setStatus("current")


class _SwIfPhysAddressType_Type(Integer32):
    """Custom type swIfPhysAddressType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("reserve", 2))
    )


_SwIfPhysAddressType_Type.__name__ = "Integer32"
_SwIfPhysAddressType_Object = MibTableColumn
swIfPhysAddressType = _SwIfPhysAddressType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 43, 1, 1, 2),
    _SwIfPhysAddressType_Type()
)
swIfPhysAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swIfPhysAddressType.setStatus("obsolete")


class _SwIfDuplexAdminMode_Type(Integer32):
    """Custom type swIfDuplexAdminMode based on Integer32"""
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
        *(("full", 3),
          ("half", 2),
          ("none", 1))
    )


_SwIfDuplexAdminMode_Type.__name__ = "Integer32"
_SwIfDuplexAdminMode_Object = MibTableColumn
swIfDuplexAdminMode = _SwIfDuplexAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 43, 1, 1, 3),
    _SwIfDuplexAdminMode_Type()
)
swIfDuplexAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swIfDuplexAdminMode.setStatus("current")


class _SwIfDuplexOperMode_Type(Integer32):
    """Custom type swIfDuplexOperMode based on Integer32"""
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
        *(("full", 2),
          ("half", 1),
          ("hybrid", 3),
          ("unknown", 4))
    )


_SwIfDuplexOperMode_Type.__name__ = "Integer32"
_SwIfDuplexOperMode_Object = MibTableColumn
swIfDuplexOperMode = _SwIfDuplexOperMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 43, 1, 1, 4),
    _SwIfDuplexOperMode_Type()
)
swIfDuplexOperMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIfDuplexOperMode.setStatus("current")


class _SwIfBackPressureMode_Type(Integer32):
    """Custom type swIfBackPressureMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_SwIfBackPressureMode_Type.__name__ = "Integer32"
_SwIfBackPressureMode_Object = MibTableColumn
swIfBackPressureMode = _SwIfBackPressureMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 43, 1, 1, 5),
    _SwIfBackPressureMode_Type()
)
swIfBackPressureMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swIfBackPressureMode.setStatus("current")


class _SwIfTaggedMode_Type(Integer32):
    """Custom type swIfTaggedMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_SwIfTaggedMode_Type.__name__ = "Integer32"
_SwIfTaggedMode_Object = MibTableColumn
swIfTaggedMode = _SwIfTaggedMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 43, 1, 1, 6),
    _SwIfTaggedMode_Type()
)
swIfTaggedMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swIfTaggedMode.setStatus("current")


class _SwIfTransceiverType_Type(Integer32):
    """Custom type swIfTransceiverType based on Integer32"""
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
        *(("comboFiberOptics", 4),
          ("comboRegular", 3),
          ("fiberOptics", 2),
          ("regular", 1))
    )


_SwIfTransceiverType_Type.__name__ = "Integer32"
_SwIfTransceiverType_Object = MibTableColumn
swIfTransceiverType = _SwIfTransceiverType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 43, 1, 1, 7),
    _SwIfTransceiverType_Type()
)
swIfTransceiverType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIfTransceiverType.setStatus("current")


class _SwIfLockAdminStatus_Type(Integer32):
    """Custom type swIfLockAdminStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("locked", 1),
          ("unlocked", 2))
    )


_SwIfLockAdminStatus_Type.__name__ = "Integer32"
_SwIfLockAdminStatus_Object = MibTableColumn
swIfLockAdminStatus = _SwIfLockAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 43, 1, 1, 8),
    _SwIfLockAdminStatus_Type()
)
swIfLockAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swIfLockAdminStatus.setStatus("current")


class _SwIfLockOperStatus_Type(Integer32):
    """Custom type swIfLockOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("locked", 1),
          ("unlocked", 2))
    )


_SwIfLockOperStatus_Type.__name__ = "Integer32"
_SwIfLockOperStatus_Object = MibTableColumn
swIfLockOperStatus = _SwIfLockOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 43, 1, 1, 9),
    _SwIfLockOperStatus_Type()
)
swIfLockOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIfLockOperStatus.setStatus("current")


class _SwIfType_Type(Integer32):
    """Custom type swIfType based on Integer32"""
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
        *(("eth1000M", 3),
          ("eth100M", 2),
          ("eth10G", 4),
          ("eth10M", 1),
          ("unknown", 5))
    )


_SwIfType_Type.__name__ = "Integer32"
_SwIfType_Object = MibTableColumn
swIfType = _SwIfType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 43, 1, 1, 10),
    _SwIfType_Type()
)
swIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIfType.setStatus("current")


class _SwIfDefaultTag_Type(Integer32):
    """Custom type swIfDefaultTag based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_SwIfDefaultTag_Type.__name__ = "Integer32"
_SwIfDefaultTag_Object = MibTableColumn
swIfDefaultTag = _SwIfDefaultTag_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 43, 1, 1, 11),
    _SwIfDefaultTag_Type()
)
swIfDefaultTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIfDefaultTag.setStatus("current")


class _SwIfDefaultPriority_Type(Integer32):
    """Custom type swIfDefaultPriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_SwIfDefaultPriority_Type.__name__ = "Integer32"
_SwIfDefaultPriority_Object = MibTableColumn
swIfDefaultPriority = _SwIfDefaultPriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 43, 1, 1, 12),
    _SwIfDefaultPriority_Type()
)
swIfDefaultPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swIfDefaultPriority.setStatus("current")
_SwIfStatus_Type = RowStatus
_SwIfStatus_Object = MibTableColumn
swIfStatus = _SwIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 43, 1, 1, 13),
    _SwIfStatus_Type()
)
swIfStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swIfStatus.setStatus("current")


class _SwIfFlowControlMode_Type(Integer32):
    """Custom type swIfFlowControlMode based on Integer32"""
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
        *(("autoNegotiation", 3),
          ("enabledRx", 4),
          ("enabledTx", 5),
          ("off", 2),
          ("on", 1))
    )


_SwIfFlowControlMode_Type.__name__ = "Integer32"
_SwIfFlowControlMode_Object = MibTableColumn
swIfFlowControlMode = _SwIfFlowControlMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 43, 1, 1, 14),
    _SwIfFlowControlMode_Type()
)
swIfFlowControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swIfFlowControlMode.setStatus("current")


class _SwIfSpeedAdminMode_Type(Integer32):
    """Custom type swIfSpeedAdminMode based on Integer32"""
    defaultValue = 0


_SwIfSpeedAdminMode_Object = MibTableColumn
swIfSpeedAdminMode = _SwIfSpeedAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 43, 1, 1, 15),
    _SwIfSpeedAdminMode_Type()
)
swIfSpeedAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swIfSpeedAdminMode.setStatus("current")


class _SwIfSpeedDuplexAutoNegotiation_Type(Integer32):
    """Custom type swIfSpeedDuplexAutoNegotiation based on Integer32"""
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


_SwIfSpeedDuplexAutoNegotiation_Type.__name__ = "Integer32"
_SwIfSpeedDuplexAutoNegotiation_Object = MibTableColumn
swIfSpeedDuplexAutoNegotiation = _SwIfSpeedDuplexAutoNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 43, 1, 1, 16),
    _SwIfSpeedDuplexAutoNegotiation_Type()
)
swIfSpeedDuplexAutoNegotiation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swIfSpeedDuplexAutoNegotiation.setStatus("current")


class _SwIfOperFlowControlMode_Type(Integer32):
    """Custom type swIfOperFlowControlMode based on Integer32"""
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
        *(("enabledRx", 3),
          ("enabledTx", 4),
          ("off", 2),
          ("on", 1))
    )


_SwIfOperFlowControlMode_Type.__name__ = "Integer32"
_SwIfOperFlowControlMode_Object = MibTableColumn
swIfOperFlowControlMode = _SwIfOperFlowControlMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 43, 1, 1, 17),
    _SwIfOperFlowControlMode_Type()
)
swIfOperFlowControlMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIfOperFlowControlMode.setStatus("current")


class _SwIfOperSpeedDuplexAutoNegotiation_Type(Integer32):
    """Custom type swIfOperSpeedDuplexAutoNegotiation based on Integer32"""
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
        *(("disabled", 2),
          ("enabled", 1),
          ("hybrid", 3),
          ("unknown", 4))
    )


_SwIfOperSpeedDuplexAutoNegotiation_Type.__name__ = "Integer32"
_SwIfOperSpeedDuplexAutoNegotiation_Object = MibTableColumn
swIfOperSpeedDuplexAutoNegotiation = _SwIfOperSpeedDuplexAutoNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 43, 1, 1, 18),
    _SwIfOperSpeedDuplexAutoNegotiation_Type()
)
swIfOperSpeedDuplexAutoNegotiation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIfOperSpeedDuplexAutoNegotiation.setStatus("current")


class _SwIfOperBackPressureMode_Type(Integer32):
    """Custom type swIfOperBackPressureMode based on Integer32"""
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
        *(("disable", 2),
          ("enable", 1),
          ("hybrid", 3),
          ("unknown", 4))
    )


_SwIfOperBackPressureMode_Type.__name__ = "Integer32"
_SwIfOperBackPressureMode_Object = MibTableColumn
swIfOperBackPressureMode = _SwIfOperBackPressureMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 43, 1, 1, 19),
    _SwIfOperBackPressureMode_Type()
)
swIfOperBackPressureMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIfOperBackPressureMode.setStatus("current")


class _SwIfAdminLockAction_Type(Integer32):
    """Custom type swIfAdminLockAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("discard", 1),
          ("discardDisable", 3),
          ("forwardNormal", 2))
    )


_SwIfAdminLockAction_Type.__name__ = "Integer32"
_SwIfAdminLockAction_Object = MibTableColumn
swIfAdminLockAction = _SwIfAdminLockAction_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 43, 1, 1, 20),
    _SwIfAdminLockAction_Type()
)
swIfAdminLockAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swIfAdminLockAction.setStatus("current")


class _SwIfOperLockAction_Type(Integer32):
    """Custom type swIfOperLockAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("discard", 1),
          ("discardDisable", 3),
          ("forwardNormal", 2))
    )


_SwIfOperLockAction_Type.__name__ = "Integer32"
_SwIfOperLockAction_Object = MibTableColumn
swIfOperLockAction = _SwIfOperLockAction_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 43, 1, 1, 21),
    _SwIfOperLockAction_Type()
)
swIfOperLockAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIfOperLockAction.setStatus("current")
_SwIfAdminLockTrapEnable_Type = TruthValue
_SwIfAdminLockTrapEnable_Object = MibTableColumn
swIfAdminLockTrapEnable = _SwIfAdminLockTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 43, 1, 1, 22),
    _SwIfAdminLockTrapEnable_Type()
)
swIfAdminLockTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swIfAdminLockTrapEnable.setStatus("current")
_SwIfOperLockTrapEnable_Type = TruthValue
_SwIfOperLockTrapEnable_Object = MibTableColumn
swIfOperLockTrapEnable = _SwIfOperLockTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 43, 1, 1, 23),
    _SwIfOperLockTrapEnable_Type()
)
swIfOperLockTrapEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIfOperLockTrapEnable.setStatus("current")
_SwIfOperSuspendedStatus_Type = TruthValue
_SwIfOperSuspendedStatus_Object = MibTableColumn
swIfOperSuspendedStatus = _SwIfOperSuspendedStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 43, 1, 1, 24),
    _SwIfOperSuspendedStatus_Type()
)
swIfOperSuspendedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIfOperSuspendedStatus.setStatus("current")


class _SwIfLockOperTrapCount_Type(Integer32):
    """Custom type swIfLockOperTrapCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwIfLockOperTrapCount_Type.__name__ = "Integer32"
_SwIfLockOperTrapCount_Object = MibTableColumn
swIfLockOperTrapCount = _SwIfLockOperTrapCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 43, 1, 1, 25),
    _SwIfLockOperTrapCount_Type()
)
swIfLockOperTrapCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIfLockOperTrapCount.setStatus("current")


class _SwIfLockAdminTrapFrequency_Type(Integer32):
    """Custom type swIfLockAdminTrapFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000000),
    )


_SwIfLockAdminTrapFrequency_Type.__name__ = "Integer32"
_SwIfLockAdminTrapFrequency_Object = MibTableColumn
swIfLockAdminTrapFrequency = _SwIfLockAdminTrapFrequency_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 43, 1, 1, 26),
    _SwIfLockAdminTrapFrequency_Type()
)
swIfLockAdminTrapFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swIfLockAdminTrapFrequency.setStatus("current")


class _SwIfReActivate_Type(TruthValue):
    """Custom type swIfReActivate based on TruthValue"""


_SwIfReActivate_Object = MibTableColumn
swIfReActivate = _SwIfReActivate_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 43, 1, 1, 27),
    _SwIfReActivate_Type()
)
swIfReActivate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swIfReActivate.setStatus("current")


class _SwIfAdminMdix_Type(Integer32):
    """Custom type swIfAdminMdix based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 3),
          ("cross", 1),
          ("normal", 2))
    )


_SwIfAdminMdix_Type.__name__ = "Integer32"
_SwIfAdminMdix_Object = MibTableColumn
swIfAdminMdix = _SwIfAdminMdix_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 43, 1, 1, 28),
    _SwIfAdminMdix_Type()
)
swIfAdminMdix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swIfAdminMdix.setStatus("current")


class _SwIfOperMdix_Type(Integer32):
    """Custom type swIfOperMdix based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cross", 1),
          ("normal", 2),
          ("unknown", 3))
    )


_SwIfOperMdix_Type.__name__ = "Integer32"
_SwIfOperMdix_Object = MibTableColumn
swIfOperMdix = _SwIfOperMdix_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 43, 1, 1, 29),
    _SwIfOperMdix_Type()
)
swIfOperMdix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIfOperMdix.setStatus("current")


class _SwIfHostMode_Type(Integer32):
    """Custom type swIfHostMode based on Integer32"""
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
        *(("multiple", 2),
          ("multiple-auth", 3),
          ("single", 1))
    )


_SwIfHostMode_Type.__name__ = "Integer32"
_SwIfHostMode_Object = MibTableColumn
swIfHostMode = _SwIfHostMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 43, 1, 1, 30),
    _SwIfHostMode_Type()
)
swIfHostMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swIfHostMode.setStatus("current")


class _SwIfSingleHostViolationAdminAction_Type(Integer32):
    """Custom type swIfSingleHostViolationAdminAction based on Integer32"""
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
        *(("discard", 1),
          ("discardDisable", 3),
          ("forwardNormal", 2))
    )


_SwIfSingleHostViolationAdminAction_Type.__name__ = "Integer32"
_SwIfSingleHostViolationAdminAction_Object = MibTableColumn
swIfSingleHostViolationAdminAction = _SwIfSingleHostViolationAdminAction_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 43, 1, 1, 31),
    _SwIfSingleHostViolationAdminAction_Type()
)
swIfSingleHostViolationAdminAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swIfSingleHostViolationAdminAction.setStatus("current")


class _SwIfSingleHostViolationOperAction_Type(Integer32):
    """Custom type swIfSingleHostViolationOperAction based on Integer32"""
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
        *(("discard", 1),
          ("discardDisable", 3),
          ("forwardNormal", 2))
    )


_SwIfSingleHostViolationOperAction_Type.__name__ = "Integer32"
_SwIfSingleHostViolationOperAction_Object = MibTableColumn
swIfSingleHostViolationOperAction = _SwIfSingleHostViolationOperAction_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 43, 1, 1, 32),
    _SwIfSingleHostViolationOperAction_Type()
)
swIfSingleHostViolationOperAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIfSingleHostViolationOperAction.setStatus("current")


class _SwIfSingleHostViolationAdminTrapEnable_Type(TruthValue):
    """Custom type swIfSingleHostViolationAdminTrapEnable based on TruthValue"""


_SwIfSingleHostViolationAdminTrapEnable_Object = MibTableColumn
swIfSingleHostViolationAdminTrapEnable = _SwIfSingleHostViolationAdminTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 43, 1, 1, 33),
    _SwIfSingleHostViolationAdminTrapEnable_Type()
)
swIfSingleHostViolationAdminTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swIfSingleHostViolationAdminTrapEnable.setStatus("current")
_SwIfSingleHostViolationOperTrapEnable_Type = TruthValue
_SwIfSingleHostViolationOperTrapEnable_Object = MibTableColumn
swIfSingleHostViolationOperTrapEnable = _SwIfSingleHostViolationOperTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 43, 1, 1, 34),
    _SwIfSingleHostViolationOperTrapEnable_Type()
)
swIfSingleHostViolationOperTrapEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIfSingleHostViolationOperTrapEnable.setStatus("current")


class _SwIfSingleHostViolationOperTrapCount_Type(Integer32):
    """Custom type swIfSingleHostViolationOperTrapCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwIfSingleHostViolationOperTrapCount_Type.__name__ = "Integer32"
_SwIfSingleHostViolationOperTrapCount_Object = MibTableColumn
swIfSingleHostViolationOperTrapCount = _SwIfSingleHostViolationOperTrapCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 43, 1, 1, 35),
    _SwIfSingleHostViolationOperTrapCount_Type()
)
swIfSingleHostViolationOperTrapCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIfSingleHostViolationOperTrapCount.setStatus("current")


class _SwIfSingleHostViolationAdminTrapFrequency_Type(Integer32):
    """Custom type swIfSingleHostViolationAdminTrapFrequency based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000000),
    )


_SwIfSingleHostViolationAdminTrapFrequency_Type.__name__ = "Integer32"
_SwIfSingleHostViolationAdminTrapFrequency_Object = MibTableColumn
swIfSingleHostViolationAdminTrapFrequency = _SwIfSingleHostViolationAdminTrapFrequency_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 43, 1, 1, 36),
    _SwIfSingleHostViolationAdminTrapFrequency_Type()
)
swIfSingleHostViolationAdminTrapFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swIfSingleHostViolationAdminTrapFrequency.setStatus("current")


class _SwIfLockLimitationMode_Type(Integer32):
    """Custom type swIfLockLimitationMode based on Integer32"""
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
        *(("disabled", 1),
          ("dynamic", 2),
          ("secure-delete-on-reset", 4),
          ("secure-permanent", 3))
    )


_SwIfLockLimitationMode_Type.__name__ = "Integer32"
_SwIfLockLimitationMode_Object = MibTableColumn
swIfLockLimitationMode = _SwIfLockLimitationMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 43, 1, 1, 37),
    _SwIfLockLimitationMode_Type()
)
swIfLockLimitationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swIfLockLimitationMode.setStatus("current")


class _SwIfLockMaxMacAddresses_Type(Integer32):
    """Custom type swIfLockMaxMacAddresses based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SwIfLockMaxMacAddresses_Type.__name__ = "Integer32"
_SwIfLockMaxMacAddresses_Object = MibTableColumn
swIfLockMaxMacAddresses = _SwIfLockMaxMacAddresses_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 43, 1, 1, 38),
    _SwIfLockMaxMacAddresses_Type()
)
swIfLockMaxMacAddresses.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swIfLockMaxMacAddresses.setStatus("current")


class _SwIfLockMacAddressesCount_Type(Integer32):
    """Custom type swIfLockMacAddressesCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwIfLockMacAddressesCount_Type.__name__ = "Integer32"
_SwIfLockMacAddressesCount_Object = MibTableColumn
swIfLockMacAddressesCount = _SwIfLockMacAddressesCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 43, 1, 1, 39),
    _SwIfLockMacAddressesCount_Type()
)
swIfLockMacAddressesCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIfLockMacAddressesCount.setStatus("current")


class _SwIfAdminSpeedDuplexAutoNegotiationLocalCapabilities_Type(AutoNegCapabilitiesBits):
    """Custom type swIfAdminSpeedDuplexAutoNegotiationLocalCapabilities based on AutoNegCapabilitiesBits"""
    defaultBinValue = "1"


_SwIfAdminSpeedDuplexAutoNegotiationLocalCapabilities_Object = MibTableColumn
swIfAdminSpeedDuplexAutoNegotiationLocalCapabilities = _SwIfAdminSpeedDuplexAutoNegotiationLocalCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 43, 1, 1, 40),
    _SwIfAdminSpeedDuplexAutoNegotiationLocalCapabilities_Type()
)
swIfAdminSpeedDuplexAutoNegotiationLocalCapabilities.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swIfAdminSpeedDuplexAutoNegotiationLocalCapabilities.setStatus("current")
_SwIfOperSpeedDuplexAutoNegotiationLocalCapabilities_Type = AutoNegCapabilitiesBits
_SwIfOperSpeedDuplexAutoNegotiationLocalCapabilities_Object = MibTableColumn
swIfOperSpeedDuplexAutoNegotiationLocalCapabilities = _SwIfOperSpeedDuplexAutoNegotiationLocalCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 43, 1, 1, 41),
    _SwIfOperSpeedDuplexAutoNegotiationLocalCapabilities_Type()
)
swIfOperSpeedDuplexAutoNegotiationLocalCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIfOperSpeedDuplexAutoNegotiationLocalCapabilities.setStatus("current")
_SwIfSpeedDuplexNegotiationRemoteCapabilities_Type = AutoNegCapabilitiesBits
_SwIfSpeedDuplexNegotiationRemoteCapabilities_Object = MibTableColumn
swIfSpeedDuplexNegotiationRemoteCapabilities = _SwIfSpeedDuplexNegotiationRemoteCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 43, 1, 1, 42),
    _SwIfSpeedDuplexNegotiationRemoteCapabilities_Type()
)
swIfSpeedDuplexNegotiationRemoteCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIfSpeedDuplexNegotiationRemoteCapabilities.setStatus("current")


class _SwIfAdminComboMode_Type(Integer32):
    """Custom type swIfAdminComboMode based on Integer32"""
    defaultValue = 3

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
        *(("force-copper", 2),
          ("force-fiber", 1),
          ("prefer-copper", 4),
          ("prefer-fiber", 3))
    )


_SwIfAdminComboMode_Type.__name__ = "Integer32"
_SwIfAdminComboMode_Object = MibTableColumn
swIfAdminComboMode = _SwIfAdminComboMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 43, 1, 1, 43),
    _SwIfAdminComboMode_Type()
)
swIfAdminComboMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swIfAdminComboMode.setStatus("current")


class _SwIfOperComboMode_Type(Integer32):
    """Custom type swIfOperComboMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("copper", 2),
          ("fiber", 1),
          ("unknown", 3))
    )


_SwIfOperComboMode_Type.__name__ = "Integer32"
_SwIfOperComboMode_Object = MibTableColumn
swIfOperComboMode = _SwIfOperComboMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 43, 1, 1, 44),
    _SwIfOperComboMode_Type()
)
swIfOperComboMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIfOperComboMode.setStatus("current")
_SwIfMibVersion_Type = Integer32
_SwIfMibVersion_Object = MibScalar
swIfMibVersion = _SwIfMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 43, 2),
    _SwIfMibVersion_Type()
)
swIfMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIfMibVersion.setStatus("current")


class _SwIfPortLockSupport_Type(Integer32):
    """Custom type swIfPortLockSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 2),
          ("supported", 1))
    )


_SwIfPortLockSupport_Type.__name__ = "Integer32"
_SwIfPortLockSupport_Object = MibScalar
swIfPortLockSupport = _SwIfPortLockSupport_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 43, 3),
    _SwIfPortLockSupport_Type()
)
swIfPortLockSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIfPortLockSupport.setStatus("current")


class _SwIfPortLockActionSupport_Type(OctetString):
    """Custom type swIfPortLockActionSupport based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_SwIfPortLockActionSupport_Type.__name__ = "OctetString"
_SwIfPortLockActionSupport_Object = MibScalar
swIfPortLockActionSupport = _SwIfPortLockActionSupport_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 43, 4),
    _SwIfPortLockActionSupport_Type()
)
swIfPortLockActionSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIfPortLockActionSupport.setStatus("current")


class _SwIfPortLockTrapSupport_Type(OctetString):
    """Custom type swIfPortLockTrapSupport based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_SwIfPortLockTrapSupport_Type.__name__ = "OctetString"
_SwIfPortLockTrapSupport_Object = MibScalar
swIfPortLockTrapSupport = _SwIfPortLockTrapSupport_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 43, 5),
    _SwIfPortLockTrapSupport_Type()
)
swIfPortLockTrapSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIfPortLockTrapSupport.setStatus("current")
_SwIfPortLockIfRangeTable_Object = MibTable
swIfPortLockIfRangeTable = _SwIfPortLockIfRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 43, 6)
)
if mibBuilder.loadTexts:
    swIfPortLockIfRangeTable.setStatus("current")
_SwIfPortLockIfRangeEntry_Object = MibTableRow
swIfPortLockIfRangeEntry = _SwIfPortLockIfRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 43, 6, 1)
)
swIfPortLockIfRangeEntry.setIndexNames(
    (0, "DLINK-3100-rlInterfaces", "swIfPortLockIfRangeIndex"),
)
if mibBuilder.loadTexts:
    swIfPortLockIfRangeEntry.setStatus("current")
_SwIfPortLockIfRangeIndex_Type = Integer32
_SwIfPortLockIfRangeIndex_Object = MibTableColumn
swIfPortLockIfRangeIndex = _SwIfPortLockIfRangeIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 43, 6, 1, 1),
    _SwIfPortLockIfRangeIndex_Type()
)
swIfPortLockIfRangeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIfPortLockIfRangeIndex.setStatus("current")
_SwIfPortLockIfRange_Type = PortList
_SwIfPortLockIfRange_Object = MibTableColumn
swIfPortLockIfRange = _SwIfPortLockIfRange_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 43, 6, 1, 2),
    _SwIfPortLockIfRange_Type()
)
swIfPortLockIfRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swIfPortLockIfRange.setStatus("current")


class _SwIfPortLockIfRangeLockStatus_Type(Integer32):
    """Custom type swIfPortLockIfRangeLockStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("locked", 1),
          ("unlocked", 2))
    )


_SwIfPortLockIfRangeLockStatus_Type.__name__ = "Integer32"
_SwIfPortLockIfRangeLockStatus_Object = MibTableColumn
swIfPortLockIfRangeLockStatus = _SwIfPortLockIfRangeLockStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 43, 6, 1, 3),
    _SwIfPortLockIfRangeLockStatus_Type()
)
swIfPortLockIfRangeLockStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swIfPortLockIfRangeLockStatus.setStatus("current")


class _SwIfPortLockIfRangeAction_Type(Integer32):
    """Custom type swIfPortLockIfRangeAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("discard", 1),
          ("discardDisable", 3),
          ("forwardNormal", 2))
    )


_SwIfPortLockIfRangeAction_Type.__name__ = "Integer32"
_SwIfPortLockIfRangeAction_Object = MibTableColumn
swIfPortLockIfRangeAction = _SwIfPortLockIfRangeAction_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 43, 6, 1, 4),
    _SwIfPortLockIfRangeAction_Type()
)
swIfPortLockIfRangeAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swIfPortLockIfRangeAction.setStatus("current")
_SwIfPortLockIfRangeTrapEn_Type = TruthValue
_SwIfPortLockIfRangeTrapEn_Object = MibTableColumn
swIfPortLockIfRangeTrapEn = _SwIfPortLockIfRangeTrapEn_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 43, 6, 1, 5),
    _SwIfPortLockIfRangeTrapEn_Type()
)
swIfPortLockIfRangeTrapEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swIfPortLockIfRangeTrapEn.setStatus("current")


class _SwIfPortLockIfRangeTrapFreq_Type(Integer32):
    """Custom type swIfPortLockIfRangeTrapFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000000),
    )


_SwIfPortLockIfRangeTrapFreq_Type.__name__ = "Integer32"
_SwIfPortLockIfRangeTrapFreq_Object = MibTableColumn
swIfPortLockIfRangeTrapFreq = _SwIfPortLockIfRangeTrapFreq_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 43, 6, 1, 6),
    _SwIfPortLockIfRangeTrapFreq_Type()
)
swIfPortLockIfRangeTrapFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swIfPortLockIfRangeTrapFreq.setStatus("current")
_SwIfExtTable_Object = MibTable
swIfExtTable = _SwIfExtTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 43, 7)
)
if mibBuilder.loadTexts:
    swIfExtTable.setStatus("current")
_SwIfExtEntry_Object = MibTableRow
swIfExtEntry = _SwIfExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 43, 7, 1)
)
swIfExtEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    swIfExtEntry.setStatus("current")


class _SwIfExtSFPSpeed_Type(Integer32):
    """Custom type swIfExtSFPSpeed based on Integer32"""
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
        *(("default", 1),
          ("eth100M", 2),
          ("eth1G", 3))
    )


_SwIfExtSFPSpeed_Type.__name__ = "Integer32"
_SwIfExtSFPSpeed_Object = MibTableColumn
swIfExtSFPSpeed = _SwIfExtSFPSpeed_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 43, 7, 1, 1),
    _SwIfExtSFPSpeed_Type()
)
swIfExtSFPSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swIfExtSFPSpeed.setStatus("current")
_RlIfMibVersion_Type = Integer32
_RlIfMibVersion_Object = MibScalar
rlIfMibVersion = _RlIfMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 54, 1),
    _RlIfMibVersion_Type()
)
rlIfMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIfMibVersion.setStatus("current")
_RlIfNumOfPhPorts_Type = Integer32
_RlIfNumOfPhPorts_Object = MibScalar
rlIfNumOfPhPorts = _RlIfNumOfPhPorts_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 54, 2),
    _RlIfNumOfPhPorts_Type()
)
rlIfNumOfPhPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIfNumOfPhPorts.setStatus("current")
_RlIfMapOfOnPhPorts_Type = OctetString
_RlIfMapOfOnPhPorts_Object = MibScalar
rlIfMapOfOnPhPorts = _RlIfMapOfOnPhPorts_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 54, 3),
    _RlIfMapOfOnPhPorts_Type()
)
rlIfMapOfOnPhPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIfMapOfOnPhPorts.setStatus("current")
_RlIfClearPortMibCounters_Type = PortList
_RlIfClearPortMibCounters_Object = MibScalar
rlIfClearPortMibCounters = _RlIfClearPortMibCounters_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 54, 4),
    _RlIfClearPortMibCounters_Type()
)
rlIfClearPortMibCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIfClearPortMibCounters.setStatus("current")
_RlIfNumOfUserDefinedPorts_Type = Integer32
_RlIfNumOfUserDefinedPorts_Object = MibScalar
rlIfNumOfUserDefinedPorts = _RlIfNumOfUserDefinedPorts_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 54, 5),
    _RlIfNumOfUserDefinedPorts_Type()
)
rlIfNumOfUserDefinedPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIfNumOfUserDefinedPorts.setStatus("current")
_RlIfFirstOutOfBandIfIndex_Type = Integer32
_RlIfFirstOutOfBandIfIndex_Object = MibScalar
rlIfFirstOutOfBandIfIndex = _RlIfFirstOutOfBandIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 54, 6),
    _RlIfFirstOutOfBandIfIndex_Type()
)
rlIfFirstOutOfBandIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIfFirstOutOfBandIfIndex.setStatus("current")
_RlIfNumOfLoopbackPorts_Type = Integer32
_RlIfNumOfLoopbackPorts_Object = MibScalar
rlIfNumOfLoopbackPorts = _RlIfNumOfLoopbackPorts_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 54, 7),
    _RlIfNumOfLoopbackPorts_Type()
)
rlIfNumOfLoopbackPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIfNumOfLoopbackPorts.setStatus("current")
_RlIfFirstLoopbackIfIndex_Type = Integer32
_RlIfFirstLoopbackIfIndex_Object = MibScalar
rlIfFirstLoopbackIfIndex = _RlIfFirstLoopbackIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 54, 8),
    _RlIfFirstLoopbackIfIndex_Type()
)
rlIfFirstLoopbackIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIfFirstLoopbackIfIndex.setStatus("current")
_RlIfExistingPortList_Type = PortList
_RlIfExistingPortList_Object = MibScalar
rlIfExistingPortList = _RlIfExistingPortList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 54, 9),
    _RlIfExistingPortList_Type()
)
rlIfExistingPortList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIfExistingPortList.setStatus("current")
_RlIfBaseMACAddressPerIfIndex_Type = TruthValue
_RlIfBaseMACAddressPerIfIndex_Object = MibScalar
rlIfBaseMACAddressPerIfIndex = _RlIfBaseMACAddressPerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 54, 10),
    _RlIfBaseMACAddressPerIfIndex_Type()
)
rlIfBaseMACAddressPerIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIfBaseMACAddressPerIfIndex.setStatus("current")


class _RlFlowControlCascadeMode_Type(Integer32):
    """Custom type rlFlowControlCascadeMode based on Integer32"""
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


_RlFlowControlCascadeMode_Type.__name__ = "Integer32"
_RlFlowControlCascadeMode_Object = MibScalar
rlFlowControlCascadeMode = _RlFlowControlCascadeMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 54, 11),
    _RlFlowControlCascadeMode_Type()
)
rlFlowControlCascadeMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlFlowControlCascadeMode.setStatus("current")


class _RlFlowControlCascadeType_Type(Integer32):
    """Custom type rlFlowControlCascadeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("internalexternal", 2),
          ("internalonly", 1))
    )


_RlFlowControlCascadeType_Type.__name__ = "Integer32"
_RlFlowControlCascadeType_Object = MibScalar
rlFlowControlCascadeType = _RlFlowControlCascadeType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 54, 12),
    _RlFlowControlCascadeType_Type()
)
rlFlowControlCascadeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlFlowControlCascadeType.setStatus("current")
_RlFlowControlRxPerSystem_Type = TruthValue
_RlFlowControlRxPerSystem_Object = MibScalar
rlFlowControlRxPerSystem = _RlFlowControlRxPerSystem_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 54, 13),
    _RlFlowControlRxPerSystem_Type()
)
rlFlowControlRxPerSystem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlFlowControlRxPerSystem.setStatus("current")
_RlCascadePortProtectionAction_Type = TruthValue
_RlCascadePortProtectionAction_Object = MibScalar
rlCascadePortProtectionAction = _RlCascadePortProtectionAction_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 54, 14),
    _RlCascadePortProtectionAction_Type()
)
rlCascadePortProtectionAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCascadePortProtectionAction.setStatus("current")
_RlManagementIfIndex_Type = InterfaceIndex
_RlManagementIfIndex_Object = MibScalar
rlManagementIfIndex = _RlManagementIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 54, 15),
    _RlManagementIfIndex_Type()
)
rlManagementIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlManagementIfIndex.setStatus("current")
_RlIfClearStackPortsCounters_Type = TruthValue
_RlIfClearStackPortsCounters_Object = MibScalar
rlIfClearStackPortsCounters = _RlIfClearStackPortsCounters_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 54, 16),
    _RlIfClearStackPortsCounters_Type()
)
rlIfClearStackPortsCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIfClearStackPortsCounters.setStatus("current")
_RlIfClearPortMacAddresses_Type = InterfaceIndexOrZero
_RlIfClearPortMacAddresses_Object = MibScalar
rlIfClearPortMacAddresses = _RlIfClearPortMacAddresses_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 54, 17),
    _RlIfClearPortMacAddresses_Type()
)
rlIfClearPortMacAddresses.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIfClearPortMacAddresses.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLINK-3100-rlInterfaces",
    **{"AutoNegCapabilitiesBits": AutoNegCapabilitiesBits,
       "swIfTable": swIfTable,
       "swIfEntry": swIfEntry,
       "swIfIndex": swIfIndex,
       "swIfPhysAddressType": swIfPhysAddressType,
       "swIfDuplexAdminMode": swIfDuplexAdminMode,
       "swIfDuplexOperMode": swIfDuplexOperMode,
       "swIfBackPressureMode": swIfBackPressureMode,
       "swIfTaggedMode": swIfTaggedMode,
       "swIfTransceiverType": swIfTransceiverType,
       "swIfLockAdminStatus": swIfLockAdminStatus,
       "swIfLockOperStatus": swIfLockOperStatus,
       "swIfType": swIfType,
       "swIfDefaultTag": swIfDefaultTag,
       "swIfDefaultPriority": swIfDefaultPriority,
       "swIfStatus": swIfStatus,
       "swIfFlowControlMode": swIfFlowControlMode,
       "swIfSpeedAdminMode": swIfSpeedAdminMode,
       "swIfSpeedDuplexAutoNegotiation": swIfSpeedDuplexAutoNegotiation,
       "swIfOperFlowControlMode": swIfOperFlowControlMode,
       "swIfOperSpeedDuplexAutoNegotiation": swIfOperSpeedDuplexAutoNegotiation,
       "swIfOperBackPressureMode": swIfOperBackPressureMode,
       "swIfAdminLockAction": swIfAdminLockAction,
       "swIfOperLockAction": swIfOperLockAction,
       "swIfAdminLockTrapEnable": swIfAdminLockTrapEnable,
       "swIfOperLockTrapEnable": swIfOperLockTrapEnable,
       "swIfOperSuspendedStatus": swIfOperSuspendedStatus,
       "swIfLockOperTrapCount": swIfLockOperTrapCount,
       "swIfLockAdminTrapFrequency": swIfLockAdminTrapFrequency,
       "swIfReActivate": swIfReActivate,
       "swIfAdminMdix": swIfAdminMdix,
       "swIfOperMdix": swIfOperMdix,
       "swIfHostMode": swIfHostMode,
       "swIfSingleHostViolationAdminAction": swIfSingleHostViolationAdminAction,
       "swIfSingleHostViolationOperAction": swIfSingleHostViolationOperAction,
       "swIfSingleHostViolationAdminTrapEnable": swIfSingleHostViolationAdminTrapEnable,
       "swIfSingleHostViolationOperTrapEnable": swIfSingleHostViolationOperTrapEnable,
       "swIfSingleHostViolationOperTrapCount": swIfSingleHostViolationOperTrapCount,
       "swIfSingleHostViolationAdminTrapFrequency": swIfSingleHostViolationAdminTrapFrequency,
       "swIfLockLimitationMode": swIfLockLimitationMode,
       "swIfLockMaxMacAddresses": swIfLockMaxMacAddresses,
       "swIfLockMacAddressesCount": swIfLockMacAddressesCount,
       "swIfAdminSpeedDuplexAutoNegotiationLocalCapabilities": swIfAdminSpeedDuplexAutoNegotiationLocalCapabilities,
       "swIfOperSpeedDuplexAutoNegotiationLocalCapabilities": swIfOperSpeedDuplexAutoNegotiationLocalCapabilities,
       "swIfSpeedDuplexNegotiationRemoteCapabilities": swIfSpeedDuplexNegotiationRemoteCapabilities,
       "swIfAdminComboMode": swIfAdminComboMode,
       "swIfOperComboMode": swIfOperComboMode,
       "swIfMibVersion": swIfMibVersion,
       "swIfPortLockSupport": swIfPortLockSupport,
       "swIfPortLockActionSupport": swIfPortLockActionSupport,
       "swIfPortLockTrapSupport": swIfPortLockTrapSupport,
       "swIfPortLockIfRangeTable": swIfPortLockIfRangeTable,
       "swIfPortLockIfRangeEntry": swIfPortLockIfRangeEntry,
       "swIfPortLockIfRangeIndex": swIfPortLockIfRangeIndex,
       "swIfPortLockIfRange": swIfPortLockIfRange,
       "swIfPortLockIfRangeLockStatus": swIfPortLockIfRangeLockStatus,
       "swIfPortLockIfRangeAction": swIfPortLockIfRangeAction,
       "swIfPortLockIfRangeTrapEn": swIfPortLockIfRangeTrapEn,
       "swIfPortLockIfRangeTrapFreq": swIfPortLockIfRangeTrapFreq,
       "swIfExtTable": swIfExtTable,
       "swIfExtEntry": swIfExtEntry,
       "swIfExtSFPSpeed": swIfExtSFPSpeed,
       "rlIfMibVersion": rlIfMibVersion,
       "rlIfNumOfPhPorts": rlIfNumOfPhPorts,
       "rlIfMapOfOnPhPorts": rlIfMapOfOnPhPorts,
       "rlIfClearPortMibCounters": rlIfClearPortMibCounters,
       "rlIfNumOfUserDefinedPorts": rlIfNumOfUserDefinedPorts,
       "rlIfFirstOutOfBandIfIndex": rlIfFirstOutOfBandIfIndex,
       "rlIfNumOfLoopbackPorts": rlIfNumOfLoopbackPorts,
       "rlIfFirstLoopbackIfIndex": rlIfFirstLoopbackIfIndex,
       "rlIfExistingPortList": rlIfExistingPortList,
       "rlIfBaseMACAddressPerIfIndex": rlIfBaseMACAddressPerIfIndex,
       "rlFlowControlCascadeMode": rlFlowControlCascadeMode,
       "rlFlowControlCascadeType": rlFlowControlCascadeType,
       "rlFlowControlRxPerSystem": rlFlowControlRxPerSystem,
       "rlCascadePortProtectionAction": rlCascadePortProtectionAction,
       "rlManagementIfIndex": rlManagementIfIndex,
       "rlIfClearStackPortsCounters": rlIfClearStackPortsCounters,
       "rlIfClearPortMacAddresses": rlIfClearPortMacAddresses}
)
