# SNMP MIB module (HUAWEI-PORT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-PORT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:05:33 2024
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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hwPortMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 157)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwPortMIBObjects_ObjectIdentity = ObjectIdentity
hwPortMIBObjects = _HwPortMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1)
)
_HwEthernet_ObjectIdentity = ObjectIdentity
hwEthernet = _HwEthernet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 1)
)
_HwEthernetTable_Object = MibTable
hwEthernetTable = _HwEthernetTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hwEthernetTable.setStatus("current")
_HwEthernetEntry_Object = MibTableRow
hwEthernetEntry = _HwEthernetEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 1, 1, 1)
)
hwEthernetEntry.setIndexNames(
    (0, "HUAWEI-PORT-MIB", "hwEthernetIfIndex"),
)
if mibBuilder.loadTexts:
    hwEthernetEntry.setStatus("current")
_HwEthernetIfIndex_Type = InterfaceIndex
_HwEthernetIfIndex_Object = MibTableColumn
hwEthernetIfIndex = _HwEthernetIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 1, 1, 1, 1),
    _HwEthernetIfIndex_Type()
)
hwEthernetIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwEthernetIfIndex.setStatus("current")


class _HwEthernetLoopback_Type(Integer32):
    """Custom type hwEthernetLoopback based on Integer32"""
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
        *(("local", 3),
          ("otherLoop", 1),
          ("remote", 4),
          ("stopLoopback", 2))
    )


_HwEthernetLoopback_Type.__name__ = "Integer32"
_HwEthernetLoopback_Object = MibTableColumn
hwEthernetLoopback = _HwEthernetLoopback_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 1, 1, 1, 11),
    _HwEthernetLoopback_Type()
)
hwEthernetLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwEthernetLoopback.setStatus("current")


class _HwEthernetPortType_Type(Integer32):
    """Custom type hwEthernetPortType based on Integer32"""
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
          ("fiber", 3),
          ("other", 1))
    )


_HwEthernetPortType_Type.__name__ = "Integer32"
_HwEthernetPortType_Object = MibTableColumn
hwEthernetPortType = _HwEthernetPortType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 1, 1, 1, 12),
    _HwEthernetPortType_Type()
)
hwEthernetPortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwEthernetPortType.setStatus("current")


class _HwEthernetSpeedSet_Type(Integer32):
    """Custom type hwEthernetSpeedSet based on Integer32"""
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
        *(("other", 1),
          ("speed10", 2),
          ("speed100", 3),
          ("speed1000", 4),
          ("speed10000", 5))
    )


_HwEthernetSpeedSet_Type.__name__ = "Integer32"
_HwEthernetSpeedSet_Object = MibTableColumn
hwEthernetSpeedSet = _HwEthernetSpeedSet_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 1, 1, 1, 13),
    _HwEthernetSpeedSet_Type()
)
hwEthernetSpeedSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwEthernetSpeedSet.setStatus("current")


class _HwEthernetDuplex_Type(Integer32):
    """Custom type hwEthernetDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("full", 1),
          ("half", 2))
    )


_HwEthernetDuplex_Type.__name__ = "Integer32"
_HwEthernetDuplex_Object = MibTableColumn
hwEthernetDuplex = _HwEthernetDuplex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 1, 1, 1, 14),
    _HwEthernetDuplex_Type()
)
hwEthernetDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwEthernetDuplex.setStatus("current")
_HwEthernetNegotiation_Type = EnabledStatus
_HwEthernetNegotiation_Object = MibTableColumn
hwEthernetNegotiation = _HwEthernetNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 1, 1, 1, 15),
    _HwEthernetNegotiation_Type()
)
hwEthernetNegotiation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwEthernetNegotiation.setStatus("current")


class _HwEthernetPortTypeOperate_Type(Integer32):
    """Custom type hwEthernetPortTypeOperate based on Integer32"""
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
        *(("copper", 2),
          ("fiber100", 3),
          ("fiber1000", 4),
          ("other", 1))
    )


_HwEthernetPortTypeOperate_Type.__name__ = "Integer32"
_HwEthernetPortTypeOperate_Object = MibTableColumn
hwEthernetPortTypeOperate = _HwEthernetPortTypeOperate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 1, 1, 1, 16),
    _HwEthernetPortTypeOperate_Type()
)
hwEthernetPortTypeOperate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwEthernetPortTypeOperate.setStatus("current")


class _HwEthernetClock_Type(Integer32):
    """Custom type hwEthernetClock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("master", 1),
          ("slave", 2))
    )


_HwEthernetClock_Type.__name__ = "Integer32"
_HwEthernetClock_Object = MibTableColumn
hwEthernetClock = _HwEthernetClock_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 1, 1, 1, 20),
    _HwEthernetClock_Type()
)
hwEthernetClock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwEthernetClock.setStatus("current")


class _HwEthernetFlagJ0Mode_Type(Integer32):
    """Custom type hwEthernetFlagJ0Mode based on Integer32"""
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
        *(("j016ByteMode", 2),
          ("j01ByteMode", 1),
          ("j064ByteOrNullMode", 3),
          ("peer", 4))
    )


_HwEthernetFlagJ0Mode_Type.__name__ = "Integer32"
_HwEthernetFlagJ0Mode_Object = MibTableColumn
hwEthernetFlagJ0Mode = _HwEthernetFlagJ0Mode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 1, 1, 1, 21),
    _HwEthernetFlagJ0Mode_Type()
)
hwEthernetFlagJ0Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwEthernetFlagJ0Mode.setStatus("current")


class _HwEthernetFlagJ0Value_Type(Integer32):
    """Custom type hwEthernetFlagJ0Value based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HwEthernetFlagJ0Value_Type.__name__ = "Integer32"
_HwEthernetFlagJ0Value_Object = MibTableColumn
hwEthernetFlagJ0Value = _HwEthernetFlagJ0Value_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 1, 1, 1, 22),
    _HwEthernetFlagJ0Value_Type()
)
hwEthernetFlagJ0Value.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwEthernetFlagJ0Value.setStatus("current")


class _HwEthernetFlagJ0Trace_Type(OctetString):
    """Custom type hwEthernetFlagJ0Trace based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HwEthernetFlagJ0Trace_Type.__name__ = "OctetString"
_HwEthernetFlagJ0Trace_Object = MibTableColumn
hwEthernetFlagJ0Trace = _HwEthernetFlagJ0Trace_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 1, 1, 1, 23),
    _HwEthernetFlagJ0Trace_Type()
)
hwEthernetFlagJ0Trace.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwEthernetFlagJ0Trace.setStatus("current")


class _HwEthernetFlagJ1Mode_Type(Integer32):
    """Custom type hwEthernetFlagJ1Mode based on Integer32"""
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
        *(("j116ByteMode", 2),
          ("j11ByteMode", 1),
          ("j164ByteOrNullMode", 3),
          ("peer", 4))
    )


_HwEthernetFlagJ1Mode_Type.__name__ = "Integer32"
_HwEthernetFlagJ1Mode_Object = MibTableColumn
hwEthernetFlagJ1Mode = _HwEthernetFlagJ1Mode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 1, 1, 1, 24),
    _HwEthernetFlagJ1Mode_Type()
)
hwEthernetFlagJ1Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwEthernetFlagJ1Mode.setStatus("current")


class _HwEthernetFlagJ1Value_Type(Integer32):
    """Custom type hwEthernetFlagJ1Value based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HwEthernetFlagJ1Value_Type.__name__ = "Integer32"
_HwEthernetFlagJ1Value_Object = MibTableColumn
hwEthernetFlagJ1Value = _HwEthernetFlagJ1Value_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 1, 1, 1, 25),
    _HwEthernetFlagJ1Value_Type()
)
hwEthernetFlagJ1Value.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwEthernetFlagJ1Value.setStatus("current")


class _HwEthernetFlagJ1Trace_Type(OctetString):
    """Custom type hwEthernetFlagJ1Trace based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HwEthernetFlagJ1Trace_Type.__name__ = "OctetString"
_HwEthernetFlagJ1Trace_Object = MibTableColumn
hwEthernetFlagJ1Trace = _HwEthernetFlagJ1Trace_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 1, 1, 1, 26),
    _HwEthernetFlagJ1Trace_Type()
)
hwEthernetFlagJ1Trace.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwEthernetFlagJ1Trace.setStatus("current")


class _HwEthernetFlagC2Value_Type(Integer32):
    """Custom type hwEthernetFlagC2Value based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HwEthernetFlagC2Value_Type.__name__ = "Integer32"
_HwEthernetFlagC2Value_Object = MibTableColumn
hwEthernetFlagC2Value = _HwEthernetFlagC2Value_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 1, 1, 1, 27),
    _HwEthernetFlagC2Value_Type()
)
hwEthernetFlagC2Value.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwEthernetFlagC2Value.setStatus("current")


class _HwEthernetUpHoldTime_Type(Integer32):
    """Custom type hwEthernetUpHoldTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3000),
    )


_HwEthernetUpHoldTime_Type.__name__ = "Integer32"
_HwEthernetUpHoldTime_Object = MibTableColumn
hwEthernetUpHoldTime = _HwEthernetUpHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 1, 1, 1, 31),
    _HwEthernetUpHoldTime_Type()
)
hwEthernetUpHoldTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwEthernetUpHoldTime.setStatus("current")


class _HwEthernetDownHoldTime_Type(Integer32):
    """Custom type hwEthernetDownHoldTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_HwEthernetDownHoldTime_Type.__name__ = "Integer32"
_HwEthernetDownHoldTime_Object = MibTableColumn
hwEthernetDownHoldTime = _HwEthernetDownHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 1, 1, 1, 32),
    _HwEthernetDownHoldTime_Type()
)
hwEthernetDownHoldTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwEthernetDownHoldTime.setStatus("current")
_HwEthernetSubinterfaceStatisticEnable_Type = EnabledStatus
_HwEthernetSubinterfaceStatisticEnable_Object = MibTableColumn
hwEthernetSubinterfaceStatisticEnable = _HwEthernetSubinterfaceStatisticEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 1, 1, 1, 33),
    _HwEthernetSubinterfaceStatisticEnable_Type()
)
hwEthernetSubinterfaceStatisticEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwEthernetSubinterfaceStatisticEnable.setStatus("current")
_HwPos_ObjectIdentity = ObjectIdentity
hwPos = _HwPos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 2)
)
_HwPosTable_Object = MibTable
hwPosTable = _HwPosTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hwPosTable.setStatus("current")
_HwPosEntry_Object = MibTableRow
hwPosEntry = _HwPosEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 2, 1, 1)
)
hwPosEntry.setIndexNames(
    (0, "HUAWEI-PORT-MIB", "hwPosIfIndex"),
)
if mibBuilder.loadTexts:
    hwPosEntry.setStatus("current")
_HwPosIfIndex_Type = InterfaceIndex
_HwPosIfIndex_Object = MibTableColumn
hwPosIfIndex = _HwPosIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 2, 1, 1, 1),
    _HwPosIfIndex_Type()
)
hwPosIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwPosIfIndex.setStatus("current")


class _HwPosLinkProtocol_Type(Integer32):
    """Custom type hwPosLinkProtocol based on Integer32"""
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
        *(("hdlc", 3),
          ("ietf", 1),
          ("nonstandard", 2),
          ("ppp", 4))
    )


_HwPosLinkProtocol_Type.__name__ = "Integer32"
_HwPosLinkProtocol_Object = MibTableColumn
hwPosLinkProtocol = _HwPosLinkProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 2, 1, 1, 11),
    _HwPosLinkProtocol_Type()
)
hwPosLinkProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPosLinkProtocol.setStatus("current")


class _HwPosFrameFormat_Type(Integer32):
    """Custom type hwPosFrameFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sdh", 2),
          ("sonet", 1))
    )


_HwPosFrameFormat_Type.__name__ = "Integer32"
_HwPosFrameFormat_Object = MibTableColumn
hwPosFrameFormat = _HwPosFrameFormat_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 2, 1, 1, 12),
    _HwPosFrameFormat_Type()
)
hwPosFrameFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPosFrameFormat.setStatus("current")


class _HwPosLoopback_Type(Integer32):
    """Custom type hwPosLoopback based on Integer32"""
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
        *(("local", 3),
          ("otherLoop", 1),
          ("remote", 4),
          ("stopLoopback", 2))
    )


_HwPosLoopback_Type.__name__ = "Integer32"
_HwPosLoopback_Object = MibTableColumn
hwPosLoopback = _HwPosLoopback_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 2, 1, 1, 13),
    _HwPosLoopback_Type()
)
hwPosLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPosLoopback.setStatus("current")
_HwPosScramble_Type = EnabledStatus
_HwPosScramble_Object = MibTableColumn
hwPosScramble = _HwPosScramble_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 2, 1, 1, 14),
    _HwPosScramble_Type()
)
hwPosScramble.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPosScramble.setStatus("current")


class _HwPosClock_Type(Integer32):
    """Custom type hwPosClock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("master", 1),
          ("slave", 2))
    )


_HwPosClock_Type.__name__ = "Integer32"
_HwPosClock_Object = MibTableColumn
hwPosClock = _HwPosClock_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 2, 1, 1, 15),
    _HwPosClock_Type()
)
hwPosClock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPosClock.setStatus("current")


class _HwPosCrcVerifyCode_Type(Integer32):
    """Custom type hwPosCrcVerifyCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("crc16", 1),
          ("crc32", 2))
    )


_HwPosCrcVerifyCode_Type.__name__ = "Integer32"
_HwPosCrcVerifyCode_Object = MibTableColumn
hwPosCrcVerifyCode = _HwPosCrcVerifyCode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 2, 1, 1, 16),
    _HwPosCrcVerifyCode_Type()
)
hwPosCrcVerifyCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPosCrcVerifyCode.setStatus("current")


class _HwPosFlagJ0Mode_Type(Integer32):
    """Custom type hwPosFlagJ0Mode based on Integer32"""
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
        *(("j016ByteMode", 2),
          ("j01ByteMode", 1),
          ("j064ByteOrNullMode", 3),
          ("peer", 4))
    )


_HwPosFlagJ0Mode_Type.__name__ = "Integer32"
_HwPosFlagJ0Mode_Object = MibTableColumn
hwPosFlagJ0Mode = _HwPosFlagJ0Mode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 2, 1, 1, 21),
    _HwPosFlagJ0Mode_Type()
)
hwPosFlagJ0Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPosFlagJ0Mode.setStatus("current")


class _HwPosFlagJ0Value_Type(Integer32):
    """Custom type hwPosFlagJ0Value based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_HwPosFlagJ0Value_Type.__name__ = "Integer32"
_HwPosFlagJ0Value_Object = MibTableColumn
hwPosFlagJ0Value = _HwPosFlagJ0Value_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 2, 1, 1, 22),
    _HwPosFlagJ0Value_Type()
)
hwPosFlagJ0Value.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPosFlagJ0Value.setStatus("current")


class _HwPosFlagJ0Trace_Type(OctetString):
    """Custom type hwPosFlagJ0Trace based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HwPosFlagJ0Trace_Type.__name__ = "OctetString"
_HwPosFlagJ0Trace_Object = MibTableColumn
hwPosFlagJ0Trace = _HwPosFlagJ0Trace_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 2, 1, 1, 23),
    _HwPosFlagJ0Trace_Type()
)
hwPosFlagJ0Trace.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPosFlagJ0Trace.setStatus("current")


class _HwPosFlagJ1Mode_Type(Integer32):
    """Custom type hwPosFlagJ1Mode based on Integer32"""
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
        *(("j116ByteMode", 2),
          ("j11ByteMode", 1),
          ("j164ByteOrNullMode", 3),
          ("peer", 4))
    )


_HwPosFlagJ1Mode_Type.__name__ = "Integer32"
_HwPosFlagJ1Mode_Object = MibTableColumn
hwPosFlagJ1Mode = _HwPosFlagJ1Mode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 2, 1, 1, 24),
    _HwPosFlagJ1Mode_Type()
)
hwPosFlagJ1Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPosFlagJ1Mode.setStatus("current")


class _HwPosFlagJ1Value_Type(Integer32):
    """Custom type hwPosFlagJ1Value based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_HwPosFlagJ1Value_Type.__name__ = "Integer32"
_HwPosFlagJ1Value_Object = MibTableColumn
hwPosFlagJ1Value = _HwPosFlagJ1Value_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 2, 1, 1, 25),
    _HwPosFlagJ1Value_Type()
)
hwPosFlagJ1Value.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPosFlagJ1Value.setStatus("current")


class _HwPosFlagJ1Trace_Type(OctetString):
    """Custom type hwPosFlagJ1Trace based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HwPosFlagJ1Trace_Type.__name__ = "OctetString"
_HwPosFlagJ1Trace_Object = MibTableColumn
hwPosFlagJ1Trace = _HwPosFlagJ1Trace_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 2, 1, 1, 26),
    _HwPosFlagJ1Trace_Type()
)
hwPosFlagJ1Trace.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPosFlagJ1Trace.setStatus("current")


class _HwPosFlagC2Value_Type(Integer32):
    """Custom type hwPosFlagC2Value based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HwPosFlagC2Value_Type.__name__ = "Integer32"
_HwPosFlagC2Value_Object = MibTableColumn
hwPosFlagC2Value = _HwPosFlagC2Value_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 2, 1, 1, 27),
    _HwPosFlagC2Value_Type()
)
hwPosFlagC2Value.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPosFlagC2Value.setStatus("current")
_HwCpos_ObjectIdentity = ObjectIdentity
hwCpos = _HwCpos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 3)
)
_HwCposTable_Object = MibTable
hwCposTable = _HwCposTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 3, 1)
)
if mibBuilder.loadTexts:
    hwCposTable.setStatus("current")
_HwCposEntry_Object = MibTableRow
hwCposEntry = _HwCposEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 3, 1, 1)
)
hwCposEntry.setIndexNames(
    (0, "HUAWEI-PORT-MIB", "hwCposIfIndex"),
)
if mibBuilder.loadTexts:
    hwCposEntry.setStatus("current")
_HwCposIfIndex_Type = InterfaceIndex
_HwCposIfIndex_Object = MibTableColumn
hwCposIfIndex = _HwCposIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 3, 1, 1, 1),
    _HwCposIfIndex_Type()
)
hwCposIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwCposIfIndex.setStatus("current")


class _HwCposClock_Type(Integer32):
    """Custom type hwCposClock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("master", 1),
          ("slave", 2))
    )


_HwCposClock_Type.__name__ = "Integer32"
_HwCposClock_Object = MibTableColumn
hwCposClock = _HwCposClock_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 3, 1, 1, 11),
    _HwCposClock_Type()
)
hwCposClock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwCposClock.setStatus("current")


class _HwCposIfType_Type(Integer32):
    """Custom type hwCposIfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("stm1", 1),
          ("stm16", 2))
    )


_HwCposIfType_Type.__name__ = "Integer32"
_HwCposIfType_Object = MibTableColumn
hwCposIfType = _HwCposIfType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 3, 1, 1, 12),
    _HwCposIfType_Type()
)
hwCposIfType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwCposIfType.setStatus("current")


class _HwCposFrameFormat_Type(Integer32):
    """Custom type hwCposFrameFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sdh", 2),
          ("sonet", 1))
    )


_HwCposFrameFormat_Type.__name__ = "Integer32"
_HwCposFrameFormat_Object = MibTableColumn
hwCposFrameFormat = _HwCposFrameFormat_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 3, 1, 1, 13),
    _HwCposFrameFormat_Type()
)
hwCposFrameFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwCposFrameFormat.setStatus("current")


class _HwCposMultiplex_Type(Integer32):
    """Custom type hwCposMultiplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("au3", 1),
          ("au4", 2))
    )


_HwCposMultiplex_Type.__name__ = "Integer32"
_HwCposMultiplex_Object = MibTableColumn
hwCposMultiplex = _HwCposMultiplex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 3, 1, 1, 14),
    _HwCposMultiplex_Type()
)
hwCposMultiplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwCposMultiplex.setStatus("current")


class _HwCposLoopback_Type(Integer32):
    """Custom type hwCposLoopback based on Integer32"""
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
        *(("local", 3),
          ("otherloop", 1),
          ("remote", 4),
          ("stopLoopback", 2))
    )


_HwCposLoopback_Type.__name__ = "Integer32"
_HwCposLoopback_Object = MibTableColumn
hwCposLoopback = _HwCposLoopback_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 3, 1, 1, 15),
    _HwCposLoopback_Type()
)
hwCposLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwCposLoopback.setStatus("current")


class _HwCposFlagJ0Mode_Type(Integer32):
    """Custom type hwCposFlagJ0Mode based on Integer32"""
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
        *(("j016ByteMode", 2),
          ("j01ByteMode", 1),
          ("j064ByteOrNullMode", 3),
          ("peer", 4))
    )


_HwCposFlagJ0Mode_Type.__name__ = "Integer32"
_HwCposFlagJ0Mode_Object = MibTableColumn
hwCposFlagJ0Mode = _HwCposFlagJ0Mode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 3, 1, 1, 21),
    _HwCposFlagJ0Mode_Type()
)
hwCposFlagJ0Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwCposFlagJ0Mode.setStatus("current")


class _HwCposFlagJ0Value_Type(Integer32):
    """Custom type hwCposFlagJ0Value based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_HwCposFlagJ0Value_Type.__name__ = "Integer32"
_HwCposFlagJ0Value_Object = MibTableColumn
hwCposFlagJ0Value = _HwCposFlagJ0Value_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 3, 1, 1, 22),
    _HwCposFlagJ0Value_Type()
)
hwCposFlagJ0Value.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwCposFlagJ0Value.setStatus("current")


class _HwCposFlagJ0Trace_Type(OctetString):
    """Custom type hwCposFlagJ0Trace based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HwCposFlagJ0Trace_Type.__name__ = "OctetString"
_HwCposFlagJ0Trace_Object = MibTableColumn
hwCposFlagJ0Trace = _HwCposFlagJ0Trace_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 3, 1, 1, 23),
    _HwCposFlagJ0Trace_Type()
)
hwCposFlagJ0Trace.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwCposFlagJ0Trace.setStatus("current")


class _HwCposFlagJ1Mode_Type(Integer32):
    """Custom type hwCposFlagJ1Mode based on Integer32"""
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
        *(("j116ByteMode", 2),
          ("j11ByteMode", 1),
          ("j164ByteOrNullMode", 3),
          ("peer", 4))
    )


_HwCposFlagJ1Mode_Type.__name__ = "Integer32"
_HwCposFlagJ1Mode_Object = MibTableColumn
hwCposFlagJ1Mode = _HwCposFlagJ1Mode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 3, 1, 1, 24),
    _HwCposFlagJ1Mode_Type()
)
hwCposFlagJ1Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwCposFlagJ1Mode.setStatus("current")


class _HwCposFlagJ1Value_Type(Integer32):
    """Custom type hwCposFlagJ1Value based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_HwCposFlagJ1Value_Type.__name__ = "Integer32"
_HwCposFlagJ1Value_Object = MibTableColumn
hwCposFlagJ1Value = _HwCposFlagJ1Value_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 3, 1, 1, 25),
    _HwCposFlagJ1Value_Type()
)
hwCposFlagJ1Value.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwCposFlagJ1Value.setStatus("current")


class _HwCposFlagJ1Trace_Type(OctetString):
    """Custom type hwCposFlagJ1Trace based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HwCposFlagJ1Trace_Type.__name__ = "OctetString"
_HwCposFlagJ1Trace_Object = MibTableColumn
hwCposFlagJ1Trace = _HwCposFlagJ1Trace_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 3, 1, 1, 26),
    _HwCposFlagJ1Trace_Type()
)
hwCposFlagJ1Trace.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwCposFlagJ1Trace.setStatus("current")


class _HwCposFlagC2Value_Type(Integer32):
    """Custom type hwCposFlagC2Value based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HwCposFlagC2Value_Type.__name__ = "Integer32"
_HwCposFlagC2Value_Object = MibTableColumn
hwCposFlagC2Value = _HwCposFlagC2Value_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 3, 1, 1, 27),
    _HwCposFlagC2Value_Type()
)
hwCposFlagC2Value.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwCposFlagC2Value.setStatus("current")
_HwDs0ChannelBundle_ObjectIdentity = ObjectIdentity
hwDs0ChannelBundle = _HwDs0ChannelBundle_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 4)
)
_HwDs0ChannelBundleTable_Object = MibTable
hwDs0ChannelBundleTable = _HwDs0ChannelBundleTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 4, 1)
)
if mibBuilder.loadTexts:
    hwDs0ChannelBundleTable.setStatus("current")
_HwDs0ChannelBundleEntry_Object = MibTableRow
hwDs0ChannelBundleEntry = _HwDs0ChannelBundleEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 4, 1, 1)
)
hwDs0ChannelBundleEntry.setIndexNames(
    (0, "HUAWEI-PORT-MIB", "hwDs0ChannelBundleParentIfIndex"),
    (0, "HUAWEI-PORT-MIB", "hwDs0ChannelBundleDs1ChannelId"),
    (0, "HUAWEI-PORT-MIB", "hwDs0ChannelBundleId"),
)
if mibBuilder.loadTexts:
    hwDs0ChannelBundleEntry.setStatus("current")
_HwDs0ChannelBundleParentIfIndex_Type = InterfaceIndex
_HwDs0ChannelBundleParentIfIndex_Object = MibTableColumn
hwDs0ChannelBundleParentIfIndex = _HwDs0ChannelBundleParentIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 4, 1, 1, 1),
    _HwDs0ChannelBundleParentIfIndex_Type()
)
hwDs0ChannelBundleParentIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwDs0ChannelBundleParentIfIndex.setStatus("current")
_HwDs0ChannelBundleDs1ChannelId_Type = Integer32
_HwDs0ChannelBundleDs1ChannelId_Object = MibTableColumn
hwDs0ChannelBundleDs1ChannelId = _HwDs0ChannelBundleDs1ChannelId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 4, 1, 1, 2),
    _HwDs0ChannelBundleDs1ChannelId_Type()
)
hwDs0ChannelBundleDs1ChannelId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwDs0ChannelBundleDs1ChannelId.setStatus("current")


class _HwDs0ChannelBundleId_Type(Integer32):
    """Custom type hwDs0ChannelBundleId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_HwDs0ChannelBundleId_Type.__name__ = "Integer32"
_HwDs0ChannelBundleId_Object = MibTableColumn
hwDs0ChannelBundleId = _HwDs0ChannelBundleId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 4, 1, 1, 3),
    _HwDs0ChannelBundleId_Type()
)
hwDs0ChannelBundleId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwDs0ChannelBundleId.setStatus("current")
_HwDs0ChannelBundleIfIndex_Type = InterfaceIndex
_HwDs0ChannelBundleIfIndex_Object = MibTableColumn
hwDs0ChannelBundleIfIndex = _HwDs0ChannelBundleIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 4, 1, 1, 11),
    _HwDs0ChannelBundleIfIndex_Type()
)
hwDs0ChannelBundleIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDs0ChannelBundleIfIndex.setStatus("current")


class _HwDs0ChannelBundleTimeSlots_Type(OctetString):
    """Custom type hwDs0ChannelBundleTimeSlots based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 61),
    )


_HwDs0ChannelBundleTimeSlots_Type.__name__ = "OctetString"
_HwDs0ChannelBundleTimeSlots_Object = MibTableColumn
hwDs0ChannelBundleTimeSlots = _HwDs0ChannelBundleTimeSlots_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 4, 1, 1, 12),
    _HwDs0ChannelBundleTimeSlots_Type()
)
hwDs0ChannelBundleTimeSlots.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDs0ChannelBundleTimeSlots.setStatus("current")


class _HwDs0ChannelBundleSpeed_Type(Integer32):
    """Custom type hwDs0ChannelBundleSpeed based on Integer32"""
    defaultValue = 64

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("s56", 1),
          ("s64", 2))
    )


_HwDs0ChannelBundleSpeed_Type.__name__ = "Integer32"
_HwDs0ChannelBundleSpeed_Object = MibTableColumn
hwDs0ChannelBundleSpeed = _HwDs0ChannelBundleSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 4, 1, 1, 13),
    _HwDs0ChannelBundleSpeed_Type()
)
hwDs0ChannelBundleSpeed.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDs0ChannelBundleSpeed.setStatus("current")
if mibBuilder.loadTexts:
    hwDs0ChannelBundleSpeed.setUnits("kilo bytes")
_HwDs0ChannelBundleRowStatus_Type = RowStatus
_HwDs0ChannelBundleRowStatus_Object = MibTableColumn
hwDs0ChannelBundleRowStatus = _HwDs0ChannelBundleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 4, 1, 1, 51),
    _HwDs0ChannelBundleRowStatus_Type()
)
hwDs0ChannelBundleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDs0ChannelBundleRowStatus.setStatus("current")
_HwDs1_ObjectIdentity = ObjectIdentity
hwDs1 = _HwDs1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 5)
)
_HwDs1Table_Object = MibTable
hwDs1Table = _HwDs1Table_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 5, 1)
)
if mibBuilder.loadTexts:
    hwDs1Table.setStatus("current")
_HwDs1Entry_Object = MibTableRow
hwDs1Entry = _HwDs1Entry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 5, 1, 1)
)
hwDs1Entry.setIndexNames(
    (0, "HUAWEI-PORT-MIB", "hwDs1ParentIfIndex"),
    (0, "HUAWEI-PORT-MIB", "hwDs1ChannelId"),
    (0, "HUAWEI-PORT-MIB", "hwDs1IfIndex"),
)
if mibBuilder.loadTexts:
    hwDs1Entry.setStatus("current")
_HwDs1ParentIfIndex_Type = InterfaceIndex
_HwDs1ParentIfIndex_Object = MibTableColumn
hwDs1ParentIfIndex = _HwDs1ParentIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 5, 1, 1, 1),
    _HwDs1ParentIfIndex_Type()
)
hwDs1ParentIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwDs1ParentIfIndex.setStatus("current")


class _HwDs1ChannelId_Type(Integer32):
    """Custom type hwDs1ChannelId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_HwDs1ChannelId_Type.__name__ = "Integer32"
_HwDs1ChannelId_Object = MibTableColumn
hwDs1ChannelId = _HwDs1ChannelId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 5, 1, 1, 2),
    _HwDs1ChannelId_Type()
)
hwDs1ChannelId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwDs1ChannelId.setStatus("current")
_HwDs1IfIndex_Type = InterfaceIndex
_HwDs1IfIndex_Object = MibTableColumn
hwDs1IfIndex = _HwDs1IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 5, 1, 1, 3),
    _HwDs1IfIndex_Type()
)
hwDs1IfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwDs1IfIndex.setStatus("current")


class _HwDs1ChannelType_Type(Integer32):
    """Custom type hwDs1ChannelType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e1", 2),
          ("t1", 1))
    )


_HwDs1ChannelType_Type.__name__ = "Integer32"
_HwDs1ChannelType_Object = MibTableColumn
hwDs1ChannelType = _HwDs1ChannelType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 5, 1, 1, 11),
    _HwDs1ChannelType_Type()
)
hwDs1ChannelType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDs1ChannelType.setStatus("current")


class _HwDs1IfType_Type(Integer32):
    """Custom type hwDs1IfType based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              255)
        )
    )
    namedValues = NamedValues(
        *(("atm", 4),
          ("cpos", 3),
          ("e3", 1),
          ("none", 255),
          ("t3", 2))
    )


_HwDs1IfType_Type.__name__ = "Integer32"
_HwDs1IfType_Object = MibTableColumn
hwDs1IfType = _HwDs1IfType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 5, 1, 1, 12),
    _HwDs1IfType_Type()
)
hwDs1IfType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDs1IfType.setStatus("current")


class _HwDs1Channelized_Type(TruthValue):
    """Custom type hwDs1Channelized based on TruthValue"""


_HwDs1Channelized_Object = MibTableColumn
hwDs1Channelized = _HwDs1Channelized_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 5, 1, 1, 13),
    _HwDs1Channelized_Type()
)
hwDs1Channelized.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDs1Channelized.setStatus("current")


class _HwDs1CodeType_Type(Integer32):
    """Custom type hwDs1CodeType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ami", 1),
          ("b8zs", 3),
          ("hdb3", 2))
    )


_HwDs1CodeType_Type.__name__ = "Integer32"
_HwDs1CodeType_Object = MibTableColumn
hwDs1CodeType = _HwDs1CodeType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 5, 1, 1, 14),
    _HwDs1CodeType_Type()
)
hwDs1CodeType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDs1CodeType.setStatus("current")


class _HwDs1Clock_Type(Integer32):
    """Custom type hwDs1Clock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("master", 1),
          ("slave", 2))
    )


_HwDs1Clock_Type.__name__ = "Integer32"
_HwDs1Clock_Object = MibTableColumn
hwDs1Clock = _HwDs1Clock_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 5, 1, 1, 15),
    _HwDs1Clock_Type()
)
hwDs1Clock.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDs1Clock.setStatus("current")


class _HwDs1FrameFormat_Type(Integer32):
    """Custom type hwDs1FrameFormat based on Integer32"""
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
        *(("crc", 4),
          ("esf", 1),
          ("noCrc4", 3),
          ("sf", 2))
    )


_HwDs1FrameFormat_Type.__name__ = "Integer32"
_HwDs1FrameFormat_Object = MibTableColumn
hwDs1FrameFormat = _HwDs1FrameFormat_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 5, 1, 1, 16),
    _HwDs1FrameFormat_Type()
)
hwDs1FrameFormat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDs1FrameFormat.setStatus("current")


class _HwDs1Cable_Type(Integer32):
    """Custom type hwDs1Cable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("long", 1),
          ("short", 2))
    )


_HwDs1Cable_Type.__name__ = "Integer32"
_HwDs1Cable_Object = MibTableColumn
hwDs1Cable = _HwDs1Cable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 5, 1, 1, 17),
    _HwDs1Cable_Type()
)
hwDs1Cable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDs1Cable.setStatus("current")


class _HwDs1Loopback_Type(Integer32):
    """Custom type hwDs1Loopback based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              255)
        )
    )
    namedValues = NamedValues(
        *(("cell", 4),
          ("local", 1),
          ("none", 255),
          ("payload", 3),
          ("remote", 2))
    )


_HwDs1Loopback_Type.__name__ = "Integer32"
_HwDs1Loopback_Object = MibTableColumn
hwDs1Loopback = _HwDs1Loopback_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 5, 1, 1, 18),
    _HwDs1Loopback_Type()
)
hwDs1Loopback.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDs1Loopback.setStatus("current")
_HwDs1RowStatus_Type = RowStatus
_HwDs1RowStatus_Object = MibTableColumn
hwDs1RowStatus = _HwDs1RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 5, 1, 1, 51),
    _HwDs1RowStatus_Type()
)
hwDs1RowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDs1RowStatus.setStatus("current")
_HwDs3_ObjectIdentity = ObjectIdentity
hwDs3 = _HwDs3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 6)
)
_HwDs3Table_Object = MibTable
hwDs3Table = _HwDs3Table_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 6, 1)
)
if mibBuilder.loadTexts:
    hwDs3Table.setStatus("current")
_HwDs3Entry_Object = MibTableRow
hwDs3Entry = _HwDs3Entry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 6, 1, 1)
)
hwDs3Entry.setIndexNames(
    (0, "HUAWEI-PORT-MIB", "hwDs3ParentIfIndex"),
    (0, "HUAWEI-PORT-MIB", "hwDs3ChannelId"),
    (0, "HUAWEI-PORT-MIB", "hwDs3IfIndex"),
)
if mibBuilder.loadTexts:
    hwDs3Entry.setStatus("current")
_HwDs3ParentIfIndex_Type = InterfaceIndex
_HwDs3ParentIfIndex_Object = MibTableColumn
hwDs3ParentIfIndex = _HwDs3ParentIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 6, 1, 1, 1),
    _HwDs3ParentIfIndex_Type()
)
hwDs3ParentIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwDs3ParentIfIndex.setStatus("current")


class _HwDs3ChannelId_Type(Integer32):
    """Custom type hwDs3ChannelId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_HwDs3ChannelId_Type.__name__ = "Integer32"
_HwDs3ChannelId_Object = MibTableColumn
hwDs3ChannelId = _HwDs3ChannelId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 6, 1, 1, 2),
    _HwDs3ChannelId_Type()
)
hwDs3ChannelId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwDs3ChannelId.setStatus("current")
_HwDs3IfIndex_Type = InterfaceIndex
_HwDs3IfIndex_Object = MibTableColumn
hwDs3IfIndex = _HwDs3IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 6, 1, 1, 3),
    _HwDs3IfIndex_Type()
)
hwDs3IfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwDs3IfIndex.setStatus("current")


class _HwDs3ChannelType_Type(Integer32):
    """Custom type hwDs3ChannelType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e3", 2),
          ("t3", 1))
    )


_HwDs3ChannelType_Type.__name__ = "Integer32"
_HwDs3ChannelType_Object = MibTableColumn
hwDs3ChannelType = _HwDs3ChannelType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 6, 1, 1, 11),
    _HwDs3ChannelType_Type()
)
hwDs3ChannelType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDs3ChannelType.setStatus("current")


class _HwDs3IfType_Type(Integer32):
    """Custom type hwDs3IfType based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("cpos", 1),
          ("none", 255))
    )


_HwDs3IfType_Type.__name__ = "Integer32"
_HwDs3IfType_Object = MibTableColumn
hwDs3IfType = _HwDs3IfType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 6, 1, 1, 12),
    _HwDs3IfType_Type()
)
hwDs3IfType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDs3IfType.setStatus("current")


class _HwDs3Channelized_Type(TruthValue):
    """Custom type hwDs3Channelized based on TruthValue"""


_HwDs3Channelized_Object = MibTableColumn
hwDs3Channelized = _HwDs3Channelized_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 6, 1, 1, 13),
    _HwDs3Channelized_Type()
)
hwDs3Channelized.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDs3Channelized.setStatus("current")


class _HwDs3Clock_Type(Integer32):
    """Custom type hwDs3Clock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("master", 1),
          ("slave", 2))
    )


_HwDs3Clock_Type.__name__ = "Integer32"
_HwDs3Clock_Object = MibTableColumn
hwDs3Clock = _HwDs3Clock_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 6, 1, 1, 14),
    _HwDs3Clock_Type()
)
hwDs3Clock.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDs3Clock.setStatus("current")


class _HwDs3FrameFormat_Type(Integer32):
    """Custom type hwDs3FrameFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("cbitAdm", 4),
          ("cbitPlcp", 5),
          ("g751Adm", 2),
          ("g751Plcp", 3),
          ("g832Adm", 1),
          ("m23Adm", 6),
          ("m23Plcp", 7))
    )


_HwDs3FrameFormat_Type.__name__ = "Integer32"
_HwDs3FrameFormat_Object = MibTableColumn
hwDs3FrameFormat = _HwDs3FrameFormat_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 6, 1, 1, 15),
    _HwDs3FrameFormat_Type()
)
hwDs3FrameFormat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDs3FrameFormat.setStatus("current")


class _HwDs3Scramble_Type(TruthValue):
    """Custom type hwDs3Scramble based on TruthValue"""


_HwDs3Scramble_Object = MibTableColumn
hwDs3Scramble = _HwDs3Scramble_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 6, 1, 1, 16),
    _HwDs3Scramble_Type()
)
hwDs3Scramble.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDs3Scramble.setStatus("current")


class _HwDs3Cable_Type(Integer32):
    """Custom type hwDs3Cable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("long", 1),
          ("short", 2))
    )


_HwDs3Cable_Type.__name__ = "Integer32"
_HwDs3Cable_Object = MibTableColumn
hwDs3Cable = _HwDs3Cable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 6, 1, 1, 17),
    _HwDs3Cable_Type()
)
hwDs3Cable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDs3Cable.setStatus("current")


class _HwDs3NationalBit_Type(Integer32):
    """Custom type hwDs3NationalBit based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("n0", 1),
          ("n1", 2))
    )


_HwDs3NationalBit_Type.__name__ = "Integer32"
_HwDs3NationalBit_Object = MibTableColumn
hwDs3NationalBit = _HwDs3NationalBit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 6, 1, 1, 18),
    _HwDs3NationalBit_Type()
)
hwDs3NationalBit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDs3NationalBit.setStatus("current")


class _HwDs3Loopback_Type(Integer32):
    """Custom type hwDs3Loopback based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              255)
        )
    )
    namedValues = NamedValues(
        *(("cell", 4),
          ("local", 1),
          ("none", 255),
          ("payload", 3),
          ("remote", 2))
    )


_HwDs3Loopback_Type.__name__ = "Integer32"
_HwDs3Loopback_Object = MibTableColumn
hwDs3Loopback = _HwDs3Loopback_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 6, 1, 1, 19),
    _HwDs3Loopback_Type()
)
hwDs3Loopback.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDs3Loopback.setStatus("current")


class _HwDs3CreateSerial_Type(TruthValue):
    """Custom type hwDs3CreateSerial based on TruthValue"""


_HwDs3CreateSerial_Object = MibTableColumn
hwDs3CreateSerial = _HwDs3CreateSerial_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 6, 1, 1, 20),
    _HwDs3CreateSerial_Type()
)
hwDs3CreateSerial.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDs3CreateSerial.setStatus("current")
_HwDs3RowStatus_Type = RowStatus
_HwDs3RowStatus_Object = MibTableColumn
hwDs3RowStatus = _HwDs3RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 6, 1, 1, 51),
    _HwDs3RowStatus_Type()
)
hwDs3RowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDs3RowStatus.setStatus("current")
_HwBundleSerial_ObjectIdentity = ObjectIdentity
hwBundleSerial = _HwBundleSerial_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 7)
)
_HwBundleSerialTable_Object = MibTable
hwBundleSerialTable = _HwBundleSerialTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 7, 1)
)
if mibBuilder.loadTexts:
    hwBundleSerialTable.setStatus("current")
_HwBundleSerialEntry_Object = MibTableRow
hwBundleSerialEntry = _HwBundleSerialEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 7, 1, 1)
)
hwBundleSerialEntry.setIndexNames(
    (0, "HUAWEI-PORT-MIB", "hwBundleSerialIfIndex"),
)
if mibBuilder.loadTexts:
    hwBundleSerialEntry.setStatus("current")
_HwBundleSerialIfIndex_Type = InterfaceIndex
_HwBundleSerialIfIndex_Object = MibTableColumn
hwBundleSerialIfIndex = _HwBundleSerialIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 7, 1, 1, 1),
    _HwBundleSerialIfIndex_Type()
)
hwBundleSerialIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBundleSerialIfIndex.setStatus("current")


class _HwBundleSerialLinkProtocol_Type(Integer32):
    """Custom type hwBundleSerialLinkProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("atm", 6),
          ("hdlc", 3),
          ("ietf", 1),
          ("lapb", 5),
          ("nonstandard", 2),
          ("ppp", 4),
          ("tdm", 7))
    )


_HwBundleSerialLinkProtocol_Type.__name__ = "Integer32"
_HwBundleSerialLinkProtocol_Object = MibTableColumn
hwBundleSerialLinkProtocol = _HwBundleSerialLinkProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 7, 1, 1, 11),
    _HwBundleSerialLinkProtocol_Type()
)
hwBundleSerialLinkProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBundleSerialLinkProtocol.setStatus("current")


class _HwBundleSerialTimerHold_Type(Integer32):
    """Custom type hwBundleSerialTimerHold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_HwBundleSerialTimerHold_Type.__name__ = "Integer32"
_HwBundleSerialTimerHold_Object = MibTableColumn
hwBundleSerialTimerHold = _HwBundleSerialTimerHold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 7, 1, 1, 12),
    _HwBundleSerialTimerHold_Type()
)
hwBundleSerialTimerHold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBundleSerialTimerHold.setStatus("current")


class _HwBundleSerialLoopback_Type(TruthValue):
    """Custom type hwBundleSerialLoopback based on TruthValue"""


_HwBundleSerialLoopback_Object = MibTableColumn
hwBundleSerialLoopback = _HwBundleSerialLoopback_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 7, 1, 1, 13),
    _HwBundleSerialLoopback_Type()
)
hwBundleSerialLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBundleSerialLoopback.setStatus("current")


class _HwBundleSerialCrcVerifyCode_Type(Integer32):
    """Custom type hwBundleSerialCrcVerifyCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("crc16", 1),
          ("crc32", 2))
    )


_HwBundleSerialCrcVerifyCode_Type.__name__ = "Integer32"
_HwBundleSerialCrcVerifyCode_Object = MibTableColumn
hwBundleSerialCrcVerifyCode = _HwBundleSerialCrcVerifyCode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 7, 1, 1, 14),
    _HwBundleSerialCrcVerifyCode_Type()
)
hwBundleSerialCrcVerifyCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBundleSerialCrcVerifyCode.setStatus("current")
_HwPortConformance_ObjectIdentity = ObjectIdentity
hwPortConformance = _HwPortConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 11)
)
_HwPortCompliances_ObjectIdentity = ObjectIdentity
hwPortCompliances = _HwPortCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 11, 1)
)
_HwPortGroups_ObjectIdentity = ObjectIdentity
hwPortGroups = _HwPortGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 11, 2)
)

# Managed Objects groups

hwEthernetObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 11, 2, 1)
)
hwEthernetObjectGroup.setObjects(
      *(("HUAWEI-PORT-MIB", "hwEthernetLoopback"),
        ("HUAWEI-PORT-MIB", "hwEthernetPortType"),
        ("HUAWEI-PORT-MIB", "hwEthernetSpeedSet"),
        ("HUAWEI-PORT-MIB", "hwEthernetDuplex"),
        ("HUAWEI-PORT-MIB", "hwEthernetNegotiation"),
        ("HUAWEI-PORT-MIB", "hwEthernetPortTypeOperate"),
        ("HUAWEI-PORT-MIB", "hwEthernetClock"),
        ("HUAWEI-PORT-MIB", "hwEthernetFlagJ0Mode"),
        ("HUAWEI-PORT-MIB", "hwEthernetFlagJ0Value"),
        ("HUAWEI-PORT-MIB", "hwEthernetFlagJ0Trace"),
        ("HUAWEI-PORT-MIB", "hwEthernetFlagJ1Mode"),
        ("HUAWEI-PORT-MIB", "hwEthernetFlagJ1Value"),
        ("HUAWEI-PORT-MIB", "hwEthernetFlagJ1Trace"),
        ("HUAWEI-PORT-MIB", "hwEthernetFlagC2Value"),
        ("HUAWEI-PORT-MIB", "hwEthernetUpHoldTime"),
        ("HUAWEI-PORT-MIB", "hwEthernetDownHoldTime"),
        ("HUAWEI-PORT-MIB", "hwEthernetSubinterfaceStatisticEnable"))
)
if mibBuilder.loadTexts:
    hwEthernetObjectGroup.setStatus("current")

hwPosObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 11, 2, 2)
)
hwPosObjectGroup.setObjects(
      *(("HUAWEI-PORT-MIB", "hwPosLinkProtocol"),
        ("HUAWEI-PORT-MIB", "hwPosFrameFormat"),
        ("HUAWEI-PORT-MIB", "hwPosLoopback"),
        ("HUAWEI-PORT-MIB", "hwPosScramble"),
        ("HUAWEI-PORT-MIB", "hwPosClock"),
        ("HUAWEI-PORT-MIB", "hwPosCrcVerifyCode"),
        ("HUAWEI-PORT-MIB", "hwPosFlagJ0Mode"),
        ("HUAWEI-PORT-MIB", "hwPosFlagJ0Value"),
        ("HUAWEI-PORT-MIB", "hwPosFlagJ0Trace"),
        ("HUAWEI-PORT-MIB", "hwPosFlagJ1Mode"),
        ("HUAWEI-PORT-MIB", "hwPosFlagJ1Value"),
        ("HUAWEI-PORT-MIB", "hwPosFlagJ1Trace"),
        ("HUAWEI-PORT-MIB", "hwPosFlagC2Value"))
)
if mibBuilder.loadTexts:
    hwPosObjectGroup.setStatus("current")

hwCposObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 11, 2, 3)
)
hwCposObjectGroup.setObjects(
      *(("HUAWEI-PORT-MIB", "hwCposFrameFormat"),
        ("HUAWEI-PORT-MIB", "hwCposMultiplex"),
        ("HUAWEI-PORT-MIB", "hwCposClock"),
        ("HUAWEI-PORT-MIB", "hwCposIfType"),
        ("HUAWEI-PORT-MIB", "hwCposLoopback"),
        ("HUAWEI-PORT-MIB", "hwCposFlagJ0Mode"),
        ("HUAWEI-PORT-MIB", "hwCposFlagJ0Value"),
        ("HUAWEI-PORT-MIB", "hwCposFlagJ0Trace"),
        ("HUAWEI-PORT-MIB", "hwCposFlagJ1Mode"),
        ("HUAWEI-PORT-MIB", "hwCposFlagJ1Value"),
        ("HUAWEI-PORT-MIB", "hwCposFlagJ1Trace"),
        ("HUAWEI-PORT-MIB", "hwCposFlagC2Value"))
)
if mibBuilder.loadTexts:
    hwCposObjectGroup.setStatus("current")

hwDs0ChannelBundleObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 11, 2, 4)
)
hwDs0ChannelBundleObjectGroup.setObjects(
      *(("HUAWEI-PORT-MIB", "hwDs0ChannelBundleIfIndex"),
        ("HUAWEI-PORT-MIB", "hwDs0ChannelBundleTimeSlots"),
        ("HUAWEI-PORT-MIB", "hwDs0ChannelBundleSpeed"),
        ("HUAWEI-PORT-MIB", "hwDs0ChannelBundleRowStatus"))
)
if mibBuilder.loadTexts:
    hwDs0ChannelBundleObjectGroup.setStatus("current")

hwDs1ObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 11, 2, 5)
)
hwDs1ObjectGroup.setObjects(
      *(("HUAWEI-PORT-MIB", "hwDs1ChannelType"),
        ("HUAWEI-PORT-MIB", "hwDs1IfType"),
        ("HUAWEI-PORT-MIB", "hwDs1Channelized"),
        ("HUAWEI-PORT-MIB", "hwDs1CodeType"),
        ("HUAWEI-PORT-MIB", "hwDs1Clock"),
        ("HUAWEI-PORT-MIB", "hwDs1FrameFormat"),
        ("HUAWEI-PORT-MIB", "hwDs1Cable"),
        ("HUAWEI-PORT-MIB", "hwDs1Loopback"),
        ("HUAWEI-PORT-MIB", "hwDs1RowStatus"))
)
if mibBuilder.loadTexts:
    hwDs1ObjectGroup.setStatus("current")

hwDs3ObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 11, 2, 6)
)
hwDs3ObjectGroup.setObjects(
      *(("HUAWEI-PORT-MIB", "hwDs3ChannelType"),
        ("HUAWEI-PORT-MIB", "hwDs3IfType"),
        ("HUAWEI-PORT-MIB", "hwDs3Channelized"),
        ("HUAWEI-PORT-MIB", "hwDs3Clock"),
        ("HUAWEI-PORT-MIB", "hwDs3FrameFormat"),
        ("HUAWEI-PORT-MIB", "hwDs3Scramble"),
        ("HUAWEI-PORT-MIB", "hwDs3Cable"),
        ("HUAWEI-PORT-MIB", "hwDs3NationalBit"),
        ("HUAWEI-PORT-MIB", "hwDs3Loopback"),
        ("HUAWEI-PORT-MIB", "hwDs3CreateSerial"),
        ("HUAWEI-PORT-MIB", "hwDs3RowStatus"))
)
if mibBuilder.loadTexts:
    hwDs3ObjectGroup.setStatus("current")

hwBundleSerialObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 11, 2, 7)
)
hwBundleSerialObjectGroup.setObjects(
      *(("HUAWEI-PORT-MIB", "hwBundleSerialLinkProtocol"),
        ("HUAWEI-PORT-MIB", "hwBundleSerialTimerHold"),
        ("HUAWEI-PORT-MIB", "hwBundleSerialCrcVerifyCode"),
        ("HUAWEI-PORT-MIB", "hwBundleSerialLoopback"))
)
if mibBuilder.loadTexts:
    hwBundleSerialObjectGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hwPortCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 11, 1, 1)
)
if mibBuilder.loadTexts:
    hwPortCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-PORT-MIB",
    **{"hwPortMIB": hwPortMIB,
       "hwPortMIBObjects": hwPortMIBObjects,
       "hwEthernet": hwEthernet,
       "hwEthernetTable": hwEthernetTable,
       "hwEthernetEntry": hwEthernetEntry,
       "hwEthernetIfIndex": hwEthernetIfIndex,
       "hwEthernetLoopback": hwEthernetLoopback,
       "hwEthernetPortType": hwEthernetPortType,
       "hwEthernetSpeedSet": hwEthernetSpeedSet,
       "hwEthernetDuplex": hwEthernetDuplex,
       "hwEthernetNegotiation": hwEthernetNegotiation,
       "hwEthernetPortTypeOperate": hwEthernetPortTypeOperate,
       "hwEthernetClock": hwEthernetClock,
       "hwEthernetFlagJ0Mode": hwEthernetFlagJ0Mode,
       "hwEthernetFlagJ0Value": hwEthernetFlagJ0Value,
       "hwEthernetFlagJ0Trace": hwEthernetFlagJ0Trace,
       "hwEthernetFlagJ1Mode": hwEthernetFlagJ1Mode,
       "hwEthernetFlagJ1Value": hwEthernetFlagJ1Value,
       "hwEthernetFlagJ1Trace": hwEthernetFlagJ1Trace,
       "hwEthernetFlagC2Value": hwEthernetFlagC2Value,
       "hwEthernetUpHoldTime": hwEthernetUpHoldTime,
       "hwEthernetDownHoldTime": hwEthernetDownHoldTime,
       "hwEthernetSubinterfaceStatisticEnable": hwEthernetSubinterfaceStatisticEnable,
       "hwPos": hwPos,
       "hwPosTable": hwPosTable,
       "hwPosEntry": hwPosEntry,
       "hwPosIfIndex": hwPosIfIndex,
       "hwPosLinkProtocol": hwPosLinkProtocol,
       "hwPosFrameFormat": hwPosFrameFormat,
       "hwPosLoopback": hwPosLoopback,
       "hwPosScramble": hwPosScramble,
       "hwPosClock": hwPosClock,
       "hwPosCrcVerifyCode": hwPosCrcVerifyCode,
       "hwPosFlagJ0Mode": hwPosFlagJ0Mode,
       "hwPosFlagJ0Value": hwPosFlagJ0Value,
       "hwPosFlagJ0Trace": hwPosFlagJ0Trace,
       "hwPosFlagJ1Mode": hwPosFlagJ1Mode,
       "hwPosFlagJ1Value": hwPosFlagJ1Value,
       "hwPosFlagJ1Trace": hwPosFlagJ1Trace,
       "hwPosFlagC2Value": hwPosFlagC2Value,
       "hwCpos": hwCpos,
       "hwCposTable": hwCposTable,
       "hwCposEntry": hwCposEntry,
       "hwCposIfIndex": hwCposIfIndex,
       "hwCposClock": hwCposClock,
       "hwCposIfType": hwCposIfType,
       "hwCposFrameFormat": hwCposFrameFormat,
       "hwCposMultiplex": hwCposMultiplex,
       "hwCposLoopback": hwCposLoopback,
       "hwCposFlagJ0Mode": hwCposFlagJ0Mode,
       "hwCposFlagJ0Value": hwCposFlagJ0Value,
       "hwCposFlagJ0Trace": hwCposFlagJ0Trace,
       "hwCposFlagJ1Mode": hwCposFlagJ1Mode,
       "hwCposFlagJ1Value": hwCposFlagJ1Value,
       "hwCposFlagJ1Trace": hwCposFlagJ1Trace,
       "hwCposFlagC2Value": hwCposFlagC2Value,
       "hwDs0ChannelBundle": hwDs0ChannelBundle,
       "hwDs0ChannelBundleTable": hwDs0ChannelBundleTable,
       "hwDs0ChannelBundleEntry": hwDs0ChannelBundleEntry,
       "hwDs0ChannelBundleParentIfIndex": hwDs0ChannelBundleParentIfIndex,
       "hwDs0ChannelBundleDs1ChannelId": hwDs0ChannelBundleDs1ChannelId,
       "hwDs0ChannelBundleId": hwDs0ChannelBundleId,
       "hwDs0ChannelBundleIfIndex": hwDs0ChannelBundleIfIndex,
       "hwDs0ChannelBundleTimeSlots": hwDs0ChannelBundleTimeSlots,
       "hwDs0ChannelBundleSpeed": hwDs0ChannelBundleSpeed,
       "hwDs0ChannelBundleRowStatus": hwDs0ChannelBundleRowStatus,
       "hwDs1": hwDs1,
       "hwDs1Table": hwDs1Table,
       "hwDs1Entry": hwDs1Entry,
       "hwDs1ParentIfIndex": hwDs1ParentIfIndex,
       "hwDs1ChannelId": hwDs1ChannelId,
       "hwDs1IfIndex": hwDs1IfIndex,
       "hwDs1ChannelType": hwDs1ChannelType,
       "hwDs1IfType": hwDs1IfType,
       "hwDs1Channelized": hwDs1Channelized,
       "hwDs1CodeType": hwDs1CodeType,
       "hwDs1Clock": hwDs1Clock,
       "hwDs1FrameFormat": hwDs1FrameFormat,
       "hwDs1Cable": hwDs1Cable,
       "hwDs1Loopback": hwDs1Loopback,
       "hwDs1RowStatus": hwDs1RowStatus,
       "hwDs3": hwDs3,
       "hwDs3Table": hwDs3Table,
       "hwDs3Entry": hwDs3Entry,
       "hwDs3ParentIfIndex": hwDs3ParentIfIndex,
       "hwDs3ChannelId": hwDs3ChannelId,
       "hwDs3IfIndex": hwDs3IfIndex,
       "hwDs3ChannelType": hwDs3ChannelType,
       "hwDs3IfType": hwDs3IfType,
       "hwDs3Channelized": hwDs3Channelized,
       "hwDs3Clock": hwDs3Clock,
       "hwDs3FrameFormat": hwDs3FrameFormat,
       "hwDs3Scramble": hwDs3Scramble,
       "hwDs3Cable": hwDs3Cable,
       "hwDs3NationalBit": hwDs3NationalBit,
       "hwDs3Loopback": hwDs3Loopback,
       "hwDs3CreateSerial": hwDs3CreateSerial,
       "hwDs3RowStatus": hwDs3RowStatus,
       "hwBundleSerial": hwBundleSerial,
       "hwBundleSerialTable": hwBundleSerialTable,
       "hwBundleSerialEntry": hwBundleSerialEntry,
       "hwBundleSerialIfIndex": hwBundleSerialIfIndex,
       "hwBundleSerialLinkProtocol": hwBundleSerialLinkProtocol,
       "hwBundleSerialTimerHold": hwBundleSerialTimerHold,
       "hwBundleSerialLoopback": hwBundleSerialLoopback,
       "hwBundleSerialCrcVerifyCode": hwBundleSerialCrcVerifyCode,
       "hwPortConformance": hwPortConformance,
       "hwPortCompliances": hwPortCompliances,
       "hwPortCompliance": hwPortCompliance,
       "hwPortGroups": hwPortGroups,
       "hwEthernetObjectGroup": hwEthernetObjectGroup,
       "hwPosObjectGroup": hwPosObjectGroup,
       "hwCposObjectGroup": hwCposObjectGroup,
       "hwDs0ChannelBundleObjectGroup": hwDs0ChannelBundleObjectGroup,
       "hwDs1ObjectGroup": hwDs1ObjectGroup,
       "hwDs3ObjectGroup": hwDs3ObjectGroup,
       "hwBundleSerialObjectGroup": hwBundleSerialObjectGroup}
)
