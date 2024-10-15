# SNMP MIB module (HUAWEI-DLDP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-DLDP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:03:35 2024
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
 MacAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hwDldpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 173)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class PortIndex(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 575),
    )



# MIB Managed Objects in the order of their OIDs

_HwDldpObjects_ObjectIdentity = ObjectIdentity
hwDldpObjects = _HwDldpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 173, 1)
)
_HwDldpConfiguration_ObjectIdentity = ObjectIdentity
hwDldpConfiguration = _HwDldpConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 173, 1, 1)
)
_HwDldpEnable_Type = EnabledStatus
_HwDldpEnable_Object = MibScalar
hwDldpEnable = _HwDldpEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 173, 1, 1, 1),
    _HwDldpEnable_Type()
)
hwDldpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDldpEnable.setStatus("current")


class _HwDldpUnidirectionalShutdown_Type(Integer32):
    """Custom type hwDldpUnidirectionalShutdown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("manual", 2))
    )


_HwDldpUnidirectionalShutdown_Type.__name__ = "Integer32"
_HwDldpUnidirectionalShutdown_Object = MibScalar
hwDldpUnidirectionalShutdown = _HwDldpUnidirectionalShutdown_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 173, 1, 1, 2),
    _HwDldpUnidirectionalShutdown_Type()
)
hwDldpUnidirectionalShutdown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDldpUnidirectionalShutdown.setStatus("current")


class _HwDldpWorkMode_Type(Integer32):
    """Custom type hwDldpWorkMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enhance", 2),
          ("normal", 1))
    )


_HwDldpWorkMode_Type.__name__ = "Integer32"
_HwDldpWorkMode_Object = MibScalar
hwDldpWorkMode = _HwDldpWorkMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 173, 1, 1, 3),
    _HwDldpWorkMode_Type()
)
hwDldpWorkMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDldpWorkMode.setStatus("current")


class _HwDldpAdvertInterval_Type(Integer32):
    """Custom type hwDldpAdvertInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HwDldpAdvertInterval_Type.__name__ = "Integer32"
_HwDldpAdvertInterval_Object = MibScalar
hwDldpAdvertInterval = _HwDldpAdvertInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 173, 1, 1, 4),
    _HwDldpAdvertInterval_Type()
)
hwDldpAdvertInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDldpAdvertInterval.setStatus("current")


class _HwDelayDownTimer_Type(Integer32):
    """Custom type hwDelayDownTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_HwDelayDownTimer_Type.__name__ = "Integer32"
_HwDelayDownTimer_Object = MibScalar
hwDelayDownTimer = _HwDelayDownTimer_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 173, 1, 1, 5),
    _HwDelayDownTimer_Type()
)
hwDelayDownTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDelayDownTimer.setStatus("current")


class _HwDldpAuthenMode_Type(Integer32):
    """Custom type hwDldpAuthenMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("md5", 2),
          ("none", 1),
          ("simple", 3))
    )


_HwDldpAuthenMode_Type.__name__ = "Integer32"
_HwDldpAuthenMode_Object = MibScalar
hwDldpAuthenMode = _HwDldpAuthenMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 173, 1, 1, 6),
    _HwDldpAuthenMode_Type()
)
hwDldpAuthenMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDldpAuthenMode.setStatus("current")


class _HwDldpMd5Password_Type(OctetString):
    """Custom type hwDldpMd5Password based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_HwDldpMd5Password_Type.__name__ = "OctetString"
_HwDldpMd5Password_Object = MibScalar
hwDldpMd5Password = _HwDldpMd5Password_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 173, 1, 1, 7),
    _HwDldpMd5Password_Type()
)
hwDldpMd5Password.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDldpMd5Password.setStatus("current")


class _HwDldpSimplePassword_Type(OctetString):
    """Custom type hwDldpSimplePassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_HwDldpSimplePassword_Type.__name__ = "OctetString"
_HwDldpSimplePassword_Object = MibScalar
hwDldpSimplePassword = _HwDldpSimplePassword_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 173, 1, 1, 8),
    _HwDldpSimplePassword_Type()
)
hwDldpSimplePassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDldpSimplePassword.setStatus("current")
_HwDldpPortTable_Object = MibTable
hwDldpPortTable = _HwDldpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 173, 1, 1, 9)
)
if mibBuilder.loadTexts:
    hwDldpPortTable.setStatus("current")
_HwDldpPortEntry_Object = MibTableRow
hwDldpPortEntry = _HwDldpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 173, 1, 1, 9, 1)
)
hwDldpPortEntry.setIndexNames(
    (0, "HUAWEI-DLDP-MIB", "hwDldpPortIndex"),
)
if mibBuilder.loadTexts:
    hwDldpPortEntry.setStatus("current")
_HwDldpPortIndex_Type = PortIndex
_HwDldpPortIndex_Object = MibTableColumn
hwDldpPortIndex = _HwDldpPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 173, 1, 1, 9, 1, 1),
    _HwDldpPortIndex_Type()
)
hwDldpPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwDldpPortIndex.setStatus("current")


class _HwDldpPortStateReset_Type(TruthValue):
    """Custom type hwDldpPortStateReset based on TruthValue"""


_HwDldpPortStateReset_Object = MibTableColumn
hwDldpPortStateReset = _HwDldpPortStateReset_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 173, 1, 1, 9, 1, 2),
    _HwDldpPortStateReset_Type()
)
hwDldpPortStateReset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDldpPortStateReset.setStatus("current")


class _HwDldpPortState_Type(Integer32):
    """Custom type hwDldpPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("active", 3),
          ("advertisement", 4),
          ("delayDown", 7),
          ("disable", 6),
          ("inactive", 2),
          ("initial", 1),
          ("loop", 8),
          ("probe", 5))
    )


_HwDldpPortState_Type.__name__ = "Integer32"
_HwDldpPortState_Object = MibTableColumn
hwDldpPortState = _HwDldpPortState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 173, 1, 1, 9, 1, 3),
    _HwDldpPortState_Type()
)
hwDldpPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDldpPortState.setStatus("current")


class _HwDldpPortLinkState_Type(Integer32):
    """Custom type hwDldpPortLinkState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_HwDldpPortLinkState_Type.__name__ = "Integer32"
_HwDldpPortLinkState_Object = MibTableColumn
hwDldpPortLinkState = _HwDldpPortLinkState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 173, 1, 1, 9, 1, 4),
    _HwDldpPortLinkState_Type()
)
hwDldpPortLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDldpPortLinkState.setStatus("current")
_HwDldpResetStatistics_Type = TruthValue
_HwDldpResetStatistics_Object = MibTableColumn
hwDldpResetStatistics = _HwDldpResetStatistics_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 173, 1, 1, 9, 1, 5),
    _HwDldpResetStatistics_Type()
)
hwDldpResetStatistics.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDldpResetStatistics.setStatus("current")
_HwDldpRowStatus_Type = RowStatus
_HwDldpRowStatus_Object = MibTableColumn
hwDldpRowStatus = _HwDldpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 173, 1, 1, 9, 1, 6),
    _HwDldpRowStatus_Type()
)
hwDldpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDldpRowStatus.setStatus("current")
_HwDldpNeighbourTable_Object = MibTable
hwDldpNeighbourTable = _HwDldpNeighbourTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 173, 1, 1, 10)
)
if mibBuilder.loadTexts:
    hwDldpNeighbourTable.setStatus("current")
_HwDldpNeighbourEntry_Object = MibTableRow
hwDldpNeighbourEntry = _HwDldpNeighbourEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 173, 1, 1, 10, 1)
)
hwDldpNeighbourEntry.setIndexNames(
    (0, "HUAWEI-DLDP-MIB", "hwDldpPortIndex"),
    (0, "HUAWEI-DLDP-MIB", "hwDldpNeighbourMacAddr"),
    (0, "HUAWEI-DLDP-MIB", "hwDldpNeighbourPortIndex"),
)
if mibBuilder.loadTexts:
    hwDldpNeighbourEntry.setStatus("current")
_HwDldpNeighbourMacAddr_Type = MacAddress
_HwDldpNeighbourMacAddr_Object = MibTableColumn
hwDldpNeighbourMacAddr = _HwDldpNeighbourMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 173, 1, 1, 10, 1, 1),
    _HwDldpNeighbourMacAddr_Type()
)
hwDldpNeighbourMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwDldpNeighbourMacAddr.setStatus("current")


class _HwDldpNeighbourPortIndex_Type(Integer32):
    """Custom type hwDldpNeighbourPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwDldpNeighbourPortIndex_Type.__name__ = "Integer32"
_HwDldpNeighbourPortIndex_Object = MibTableColumn
hwDldpNeighbourPortIndex = _HwDldpNeighbourPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 173, 1, 1, 10, 1, 2),
    _HwDldpNeighbourPortIndex_Type()
)
hwDldpNeighbourPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwDldpNeighbourPortIndex.setStatus("current")


class _HwDldpNeighbourPortName_Type(OctetString):
    """Custom type hwDldpNeighbourPortName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HwDldpNeighbourPortName_Type.__name__ = "OctetString"
_HwDldpNeighbourPortName_Object = MibTableColumn
hwDldpNeighbourPortName = _HwDldpNeighbourPortName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 173, 1, 1, 10, 1, 3),
    _HwDldpNeighbourPortName_Type()
)
hwDldpNeighbourPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDldpNeighbourPortName.setStatus("current")


class _HwDldpNeighbourState_Type(Integer32):
    """Custom type hwDldpNeighbourState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("oneWay", 2),
          ("twoWay", 3),
          ("unknown", 1))
    )


_HwDldpNeighbourState_Type.__name__ = "Integer32"
_HwDldpNeighbourState_Object = MibTableColumn
hwDldpNeighbourState = _HwDldpNeighbourState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 173, 1, 1, 10, 1, 4),
    _HwDldpNeighbourState_Type()
)
hwDldpNeighbourState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDldpNeighbourState.setStatus("current")


class _HwDldpNeighbourAgeTime_Type(Integer32):
    """Custom type hwDldpNeighbourAgeTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 300),
    )


_HwDldpNeighbourAgeTime_Type.__name__ = "Integer32"
_HwDldpNeighbourAgeTime_Object = MibTableColumn
hwDldpNeighbourAgeTime = _HwDldpNeighbourAgeTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 173, 1, 1, 10, 1, 5),
    _HwDldpNeighbourAgeTime_Type()
)
hwDldpNeighbourAgeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDldpNeighbourAgeTime.setStatus("current")
_HwDldpStatistics_ObjectIdentity = ObjectIdentity
hwDldpStatistics = _HwDldpStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 173, 1, 2)
)
_HwDldpPortStatisticsTable_Object = MibTable
hwDldpPortStatisticsTable = _HwDldpPortStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 173, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hwDldpPortStatisticsTable.setStatus("current")
_HwDldpPortStatisticsEntry_Object = MibTableRow
hwDldpPortStatisticsEntry = _HwDldpPortStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 173, 1, 2, 1, 1)
)
hwDldpPortStatisticsEntry.setIndexNames(
    (0, "HUAWEI-DLDP-MIB", "hwDldpPortIndex"),
)
if mibBuilder.loadTexts:
    hwDldpPortStatisticsEntry.setStatus("current")
_HwDldpPortStatisticsTx_Type = Counter32
_HwDldpPortStatisticsTx_Object = MibTableColumn
hwDldpPortStatisticsTx = _HwDldpPortStatisticsTx_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 173, 1, 2, 1, 1, 1),
    _HwDldpPortStatisticsTx_Type()
)
hwDldpPortStatisticsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDldpPortStatisticsTx.setStatus("current")
_HwDldpPortStatisticsRxTotal_Type = Counter32
_HwDldpPortStatisticsRxTotal_Object = MibTableColumn
hwDldpPortStatisticsRxTotal = _HwDldpPortStatisticsRxTotal_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 173, 1, 2, 1, 1, 2),
    _HwDldpPortStatisticsRxTotal_Type()
)
hwDldpPortStatisticsRxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDldpPortStatisticsRxTotal.setStatus("current")
_HwDldpPortStatisticsRxError_Type = Counter32
_HwDldpPortStatisticsRxError_Object = MibTableColumn
hwDldpPortStatisticsRxError = _HwDldpPortStatisticsRxError_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 173, 1, 2, 1, 1, 3),
    _HwDldpPortStatisticsRxError_Type()
)
hwDldpPortStatisticsRxError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDldpPortStatisticsRxError.setStatus("current")
_HwDldpPortStatisticsRxLoop_Type = Counter32
_HwDldpPortStatisticsRxLoop_Object = MibTableColumn
hwDldpPortStatisticsRxLoop = _HwDldpPortStatisticsRxLoop_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 173, 1, 2, 1, 1, 4),
    _HwDldpPortStatisticsRxLoop_Type()
)
hwDldpPortStatisticsRxLoop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDldpPortStatisticsRxLoop.setStatus("current")
_HwDldpPortStatisticsRxValid_Type = Counter32
_HwDldpPortStatisticsRxValid_Object = MibTableColumn
hwDldpPortStatisticsRxValid = _HwDldpPortStatisticsRxValid_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 173, 1, 2, 1, 1, 5),
    _HwDldpPortStatisticsRxValid_Type()
)
hwDldpPortStatisticsRxValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDldpPortStatisticsRxValid.setStatus("current")
_HwDldpPortStatisticsRxAuthenFail_Type = Counter32
_HwDldpPortStatisticsRxAuthenFail_Object = MibTableColumn
hwDldpPortStatisticsRxAuthenFail = _HwDldpPortStatisticsRxAuthenFail_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 173, 1, 2, 1, 1, 6),
    _HwDldpPortStatisticsRxAuthenFail_Type()
)
hwDldpPortStatisticsRxAuthenFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDldpPortStatisticsRxAuthenFail.setStatus("current")
_HwDldpPortTrapObjects_ObjectIdentity = ObjectIdentity
hwDldpPortTrapObjects = _HwDldpPortTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 173, 2)
)
_HwDldpTrapInterfaceIndex_Type = InterfaceIndex
_HwDldpTrapInterfaceIndex_Object = MibScalar
hwDldpTrapInterfaceIndex = _HwDldpTrapInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 173, 2, 1),
    _HwDldpTrapInterfaceIndex_Type()
)
hwDldpTrapInterfaceIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwDldpTrapInterfaceIndex.setStatus("current")


class _HwDldpTrapIfName_Type(OctetString):
    """Custom type hwDldpTrapIfName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HwDldpTrapIfName_Type.__name__ = "OctetString"
_HwDldpTrapIfName_Object = MibScalar
hwDldpTrapIfName = _HwDldpTrapIfName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 173, 2, 2),
    _HwDldpTrapIfName_Type()
)
hwDldpTrapIfName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwDldpTrapIfName.setStatus("current")


class _HwDldpTrapFaultReason_Type(OctetString):
    """Custom type hwDldpTrapFaultReason based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HwDldpTrapFaultReason_Type.__name__ = "OctetString"
_HwDldpTrapFaultReason_Object = MibScalar
hwDldpTrapFaultReason = _HwDldpTrapFaultReason_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 173, 2, 3),
    _HwDldpTrapFaultReason_Type()
)
hwDldpTrapFaultReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwDldpTrapFaultReason.setStatus("current")
_HwDldpTraps_ObjectIdentity = ObjectIdentity
hwDldpTraps = _HwDldpTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 173, 3)
)
_HwDldpConformance_ObjectIdentity = ObjectIdentity
hwDldpConformance = _HwDldpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 173, 4)
)
_HwDldpCompliances_ObjectIdentity = ObjectIdentity
hwDldpCompliances = _HwDldpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 173, 4, 1)
)
_HwDldpGroups_ObjectIdentity = ObjectIdentity
hwDldpGroups = _HwDldpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 173, 4, 2)
)

# Managed Objects groups

hwDldpConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 173, 4, 2, 1)
)
hwDldpConfigGroup.setObjects(
      *(("HUAWEI-DLDP-MIB", "hwDldpEnable"),
        ("HUAWEI-DLDP-MIB", "hwDldpUnidirectionalShutdown"),
        ("HUAWEI-DLDP-MIB", "hwDldpWorkMode"),
        ("HUAWEI-DLDP-MIB", "hwDldpAdvertInterval"),
        ("HUAWEI-DLDP-MIB", "hwDelayDownTimer"),
        ("HUAWEI-DLDP-MIB", "hwDldpAuthenMode"),
        ("HUAWEI-DLDP-MIB", "hwDldpMd5Password"),
        ("HUAWEI-DLDP-MIB", "hwDldpSimplePassword"))
)
if mibBuilder.loadTexts:
    hwDldpConfigGroup.setStatus("current")

hwDldpStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 173, 4, 2, 2)
)
hwDldpStatisticsGroup.setObjects(
      *(("HUAWEI-DLDP-MIB", "hwDldpPortStatisticsTx"),
        ("HUAWEI-DLDP-MIB", "hwDldpPortStatisticsRxTotal"),
        ("HUAWEI-DLDP-MIB", "hwDldpPortStatisticsRxError"),
        ("HUAWEI-DLDP-MIB", "hwDldpPortStatisticsRxLoop"),
        ("HUAWEI-DLDP-MIB", "hwDldpPortStatisticsRxValid"),
        ("HUAWEI-DLDP-MIB", "hwDldpPortStatisticsRxAuthenFail"))
)
if mibBuilder.loadTexts:
    hwDldpStatisticsGroup.setStatus("current")

hwDldpPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 173, 4, 2, 3)
)
hwDldpPortGroup.setObjects(
      *(("HUAWEI-DLDP-MIB", "hwDldpPortStateReset"),
        ("HUAWEI-DLDP-MIB", "hwDldpPortState"),
        ("HUAWEI-DLDP-MIB", "hwDldpPortLinkState"),
        ("HUAWEI-DLDP-MIB", "hwDldpResetStatistics"),
        ("HUAWEI-DLDP-MIB", "hwDldpRowStatus"),
        ("HUAWEI-DLDP-MIB", "hwDldpNeighbourPortName"),
        ("HUAWEI-DLDP-MIB", "hwDldpNeighbourState"),
        ("HUAWEI-DLDP-MIB", "hwDldpNeighbourAgeTime"))
)
if mibBuilder.loadTexts:
    hwDldpPortGroup.setStatus("current")

hwDldpPortTrapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 173, 4, 2, 4)
)
hwDldpPortTrapGroup.setObjects(
      *(("HUAWEI-DLDP-MIB", "hwDldpTrapInterfaceIndex"),
        ("HUAWEI-DLDP-MIB", "hwDldpTrapIfName"))
)
if mibBuilder.loadTexts:
    hwDldpPortTrapGroup.setStatus("current")


# Notification objects

hwDldpUnidirectionalLink = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 173, 3, 1)
)
hwDldpUnidirectionalLink.setObjects(
      *(("HUAWEI-DLDP-MIB", "hwDldpTrapInterfaceIndex"),
        ("HUAWEI-DLDP-MIB", "hwDldpTrapIfName"),
        ("HUAWEI-DLDP-MIB", "hwDldpTrapFaultReason"))
)
if mibBuilder.loadTexts:
    hwDldpUnidirectionalLink.setStatus(
        "current"
    )

hwDldpLinkResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 173, 3, 2)
)
hwDldpLinkResume.setObjects(
      *(("HUAWEI-DLDP-MIB", "hwDldpTrapInterfaceIndex"),
        ("HUAWEI-DLDP-MIB", "hwDldpTrapIfName"))
)
if mibBuilder.loadTexts:
    hwDldpLinkResume.setStatus(
        "current"
    )

hwDldpLoopDetect = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 173, 3, 3)
)
hwDldpLoopDetect.setObjects(
      *(("HUAWEI-DLDP-MIB", "hwDldpTrapInterfaceIndex"),
        ("HUAWEI-DLDP-MIB", "hwDldpTrapIfName"))
)
if mibBuilder.loadTexts:
    hwDldpLoopDetect.setStatus(
        "current"
    )

hwDldpLoopResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 173, 3, 4)
)
hwDldpLoopResume.setObjects(
      *(("HUAWEI-DLDP-MIB", "hwDldpTrapInterfaceIndex"),
        ("HUAWEI-DLDP-MIB", "hwDldpTrapIfName"))
)
if mibBuilder.loadTexts:
    hwDldpLoopResume.setStatus(
        "current"
    )


# Notifications groups

hwDldpTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 173, 4, 2, 5)
)
hwDldpTrapGroup.setObjects(
      *(("HUAWEI-DLDP-MIB", "hwDldpUnidirectionalLink"),
        ("HUAWEI-DLDP-MIB", "hwDldpLinkResume"),
        ("HUAWEI-DLDP-MIB", "hwDldpLoopDetect"),
        ("HUAWEI-DLDP-MIB", "hwDldpLoopResume"))
)
if mibBuilder.loadTexts:
    hwDldpTrapGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hwDldpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 173, 4, 1, 1)
)
if mibBuilder.loadTexts:
    hwDldpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-DLDP-MIB",
    **{"PortIndex": PortIndex,
       "hwDldpMIB": hwDldpMIB,
       "hwDldpObjects": hwDldpObjects,
       "hwDldpConfiguration": hwDldpConfiguration,
       "hwDldpEnable": hwDldpEnable,
       "hwDldpUnidirectionalShutdown": hwDldpUnidirectionalShutdown,
       "hwDldpWorkMode": hwDldpWorkMode,
       "hwDldpAdvertInterval": hwDldpAdvertInterval,
       "hwDelayDownTimer": hwDelayDownTimer,
       "hwDldpAuthenMode": hwDldpAuthenMode,
       "hwDldpMd5Password": hwDldpMd5Password,
       "hwDldpSimplePassword": hwDldpSimplePassword,
       "hwDldpPortTable": hwDldpPortTable,
       "hwDldpPortEntry": hwDldpPortEntry,
       "hwDldpPortIndex": hwDldpPortIndex,
       "hwDldpPortStateReset": hwDldpPortStateReset,
       "hwDldpPortState": hwDldpPortState,
       "hwDldpPortLinkState": hwDldpPortLinkState,
       "hwDldpResetStatistics": hwDldpResetStatistics,
       "hwDldpRowStatus": hwDldpRowStatus,
       "hwDldpNeighbourTable": hwDldpNeighbourTable,
       "hwDldpNeighbourEntry": hwDldpNeighbourEntry,
       "hwDldpNeighbourMacAddr": hwDldpNeighbourMacAddr,
       "hwDldpNeighbourPortIndex": hwDldpNeighbourPortIndex,
       "hwDldpNeighbourPortName": hwDldpNeighbourPortName,
       "hwDldpNeighbourState": hwDldpNeighbourState,
       "hwDldpNeighbourAgeTime": hwDldpNeighbourAgeTime,
       "hwDldpStatistics": hwDldpStatistics,
       "hwDldpPortStatisticsTable": hwDldpPortStatisticsTable,
       "hwDldpPortStatisticsEntry": hwDldpPortStatisticsEntry,
       "hwDldpPortStatisticsTx": hwDldpPortStatisticsTx,
       "hwDldpPortStatisticsRxTotal": hwDldpPortStatisticsRxTotal,
       "hwDldpPortStatisticsRxError": hwDldpPortStatisticsRxError,
       "hwDldpPortStatisticsRxLoop": hwDldpPortStatisticsRxLoop,
       "hwDldpPortStatisticsRxValid": hwDldpPortStatisticsRxValid,
       "hwDldpPortStatisticsRxAuthenFail": hwDldpPortStatisticsRxAuthenFail,
       "hwDldpPortTrapObjects": hwDldpPortTrapObjects,
       "hwDldpTrapInterfaceIndex": hwDldpTrapInterfaceIndex,
       "hwDldpTrapIfName": hwDldpTrapIfName,
       "hwDldpTrapFaultReason": hwDldpTrapFaultReason,
       "hwDldpTraps": hwDldpTraps,
       "hwDldpUnidirectionalLink": hwDldpUnidirectionalLink,
       "hwDldpLinkResume": hwDldpLinkResume,
       "hwDldpLoopDetect": hwDldpLoopDetect,
       "hwDldpLoopResume": hwDldpLoopResume,
       "hwDldpConformance": hwDldpConformance,
       "hwDldpCompliances": hwDldpCompliances,
       "hwDldpCompliance": hwDldpCompliance,
       "hwDldpGroups": hwDldpGroups,
       "hwDldpConfigGroup": hwDldpConfigGroup,
       "hwDldpStatisticsGroup": hwDldpStatisticsGroup,
       "hwDldpPortGroup": hwDldpPortGroup,
       "hwDldpPortTrapGroup": hwDldpPortTrapGroup,
       "hwDldpTrapGroup": hwDldpTrapGroup}
)
