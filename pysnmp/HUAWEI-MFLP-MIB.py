# SNMP MIB module (HUAWEI-MFLP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-MFLP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:04:57 2024
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
 MacAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

hwMFlpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 160)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwMflpObjects_ObjectIdentity = ObjectIdentity
hwMflpObjects = _HwMflpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 160, 1)
)
_HwMflpVlanCfgTable_Object = MibTable
hwMflpVlanCfgTable = _HwMflpVlanCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 160, 1, 1)
)
if mibBuilder.loadTexts:
    hwMflpVlanCfgTable.setStatus("current")
_HwMflpVlanCfgEntry_Object = MibTableRow
hwMflpVlanCfgEntry = _HwMflpVlanCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 160, 1, 1, 1)
)
hwMflpVlanCfgEntry.setIndexNames(
    (0, "HUAWEI-MFLP-MIB", "hwMflpVlanId"),
)
if mibBuilder.loadTexts:
    hwMflpVlanCfgEntry.setStatus("current")
_HwMflpVlanId_Type = VlanId
_HwMflpVlanId_Object = MibTableColumn
hwMflpVlanId = _HwMflpVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 160, 1, 1, 1, 1),
    _HwMflpVlanId_Type()
)
hwMflpVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMflpVlanId.setStatus("current")


class _HwMflpVlanCfgLoopTimes_Type(Unsigned32):
    """Custom type hwMflpVlanCfgLoopTimes based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 1000),
    )


_HwMflpVlanCfgLoopTimes_Type.__name__ = "Unsigned32"
_HwMflpVlanCfgLoopTimes_Object = MibTableColumn
hwMflpVlanCfgLoopTimes = _HwMflpVlanCfgLoopTimes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 160, 1, 1, 1, 2),
    _HwMflpVlanCfgLoopTimes_Type()
)
hwMflpVlanCfgLoopTimes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMflpVlanCfgLoopTimes.setStatus("current")


class _HwMflpVlanCfgDetectCycle_Type(Unsigned32):
    """Custom type hwMflpVlanCfgDetectCycle based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 30),
    )


_HwMflpVlanCfgDetectCycle_Type.__name__ = "Unsigned32"
_HwMflpVlanCfgDetectCycle_Object = MibTableColumn
hwMflpVlanCfgDetectCycle = _HwMflpVlanCfgDetectCycle_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 160, 1, 1, 1, 3),
    _HwMflpVlanCfgDetectCycle_Type()
)
hwMflpVlanCfgDetectCycle.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMflpVlanCfgDetectCycle.setStatus("current")


class _HwMflpVlanCfgCycles_Type(Unsigned32):
    """Custom type hwMflpVlanCfgCycles based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_HwMflpVlanCfgCycles_Type.__name__ = "Unsigned32"
_HwMflpVlanCfgCycles_Object = MibTableColumn
hwMflpVlanCfgCycles = _HwMflpVlanCfgCycles_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 160, 1, 1, 1, 4),
    _HwMflpVlanCfgCycles_Type()
)
hwMflpVlanCfgCycles.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMflpVlanCfgCycles.setStatus("current")


class _HwMflpVlanCfgAction_Type(Integer32):
    """Custom type hwMflpVlanCfgAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alarmOnly", 2),
          ("block", 1))
    )


_HwMflpVlanCfgAction_Type.__name__ = "Integer32"
_HwMflpVlanCfgAction_Object = MibTableColumn
hwMflpVlanCfgAction = _HwMflpVlanCfgAction_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 160, 1, 1, 1, 5),
    _HwMflpVlanCfgAction_Type()
)
hwMflpVlanCfgAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMflpVlanCfgAction.setStatus("current")


class _HwMflpVlanCfgBlockTime_Type(Unsigned32):
    """Custom type hwMflpVlanCfgBlockTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwMflpVlanCfgBlockTime_Type.__name__ = "Unsigned32"
_HwMflpVlanCfgBlockTime_Object = MibTableColumn
hwMflpVlanCfgBlockTime = _HwMflpVlanCfgBlockTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 160, 1, 1, 1, 6),
    _HwMflpVlanCfgBlockTime_Type()
)
hwMflpVlanCfgBlockTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMflpVlanCfgBlockTime.setStatus("current")


class _HwMflpVlanCfgRetryTimes_Type(Unsigned32):
    """Custom type hwMflpVlanCfgRetryTimes based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_HwMflpVlanCfgRetryTimes_Type.__name__ = "Unsigned32"
_HwMflpVlanCfgRetryTimes_Object = MibTableColumn
hwMflpVlanCfgRetryTimes = _HwMflpVlanCfgRetryTimes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 160, 1, 1, 1, 7),
    _HwMflpVlanCfgRetryTimes_Type()
)
hwMflpVlanCfgRetryTimes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMflpVlanCfgRetryTimes.setStatus("current")
_HwMflpVlanCfgIfName_Type = DisplayString
_HwMflpVlanCfgIfName_Object = MibTableColumn
hwMflpVlanCfgIfName = _HwMflpVlanCfgIfName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 160, 1, 1, 1, 8),
    _HwMflpVlanCfgIfName_Type()
)
hwMflpVlanCfgIfName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwMflpVlanCfgIfName.setStatus("current")
_HwMflpVlanCfgAlarmReason_Type = DisplayString
_HwMflpVlanCfgAlarmReason_Object = MibTableColumn
hwMflpVlanCfgAlarmReason = _HwMflpVlanCfgAlarmReason_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 160, 1, 1, 1, 9),
    _HwMflpVlanCfgAlarmReason_Type()
)
hwMflpVlanCfgAlarmReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwMflpVlanCfgAlarmReason.setStatus("current")
_HwMflpVlanCfgRowstatus_Type = RowStatus
_HwMflpVlanCfgRowstatus_Object = MibTableColumn
hwMflpVlanCfgRowstatus = _HwMflpVlanCfgRowstatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 160, 1, 1, 1, 10),
    _HwMflpVlanCfgRowstatus_Type()
)
hwMflpVlanCfgRowstatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMflpVlanCfgRowstatus.setStatus("current")
_HwMflpVlanDetectMAC_Type = DisplayString
_HwMflpVlanDetectMAC_Object = MibTableColumn
hwMflpVlanDetectMAC = _HwMflpVlanDetectMAC_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 160, 1, 1, 1, 11),
    _HwMflpVlanDetectMAC_Type()
)
hwMflpVlanDetectMAC.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwMflpVlanDetectMAC.setStatus("current")
_HwMflpVlanCfgMacAddr_Type = MacAddress
_HwMflpVlanCfgMacAddr_Object = MibTableColumn
hwMflpVlanCfgMacAddr = _HwMflpVlanCfgMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 160, 1, 1, 1, 12),
    _HwMflpVlanCfgMacAddr_Type()
)
hwMflpVlanCfgMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMflpVlanCfgMacAddr.setStatus("current")
_HwMflpVlanCfgPreIfName_Type = DisplayString
_HwMflpVlanCfgPreIfName_Object = MibTableColumn
hwMflpVlanCfgPreIfName = _HwMflpVlanCfgPreIfName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 160, 1, 1, 1, 13),
    _HwMflpVlanCfgPreIfName_Type()
)
hwMflpVlanCfgPreIfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMflpVlanCfgPreIfName.setStatus("current")
_HwMflpVsiCfgTable_Object = MibTable
hwMflpVsiCfgTable = _HwMflpVsiCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 160, 1, 2)
)
if mibBuilder.loadTexts:
    hwMflpVsiCfgTable.setStatus("current")
_HwMflpVsiCfgEntry_Object = MibTableRow
hwMflpVsiCfgEntry = _HwMflpVsiCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 160, 1, 2, 1)
)
hwMflpVsiCfgEntry.setIndexNames(
    (0, "HUAWEI-MFLP-MIB", "hwMflpVsiName"),
)
if mibBuilder.loadTexts:
    hwMflpVsiCfgEntry.setStatus("current")


class _HwMflpVsiName_Type(OctetString):
    """Custom type hwMflpVsiName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwMflpVsiName_Type.__name__ = "OctetString"
_HwMflpVsiName_Object = MibTableColumn
hwMflpVsiName = _HwMflpVsiName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 160, 1, 2, 1, 1),
    _HwMflpVsiName_Type()
)
hwMflpVsiName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMflpVsiName.setStatus("current")


class _HwMflpVsiCfgLoopTimes_Type(Unsigned32):
    """Custom type hwMflpVsiCfgLoopTimes based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 1000),
    )


_HwMflpVsiCfgLoopTimes_Type.__name__ = "Unsigned32"
_HwMflpVsiCfgLoopTimes_Object = MibTableColumn
hwMflpVsiCfgLoopTimes = _HwMflpVsiCfgLoopTimes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 160, 1, 2, 1, 2),
    _HwMflpVsiCfgLoopTimes_Type()
)
hwMflpVsiCfgLoopTimes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMflpVsiCfgLoopTimes.setStatus("current")


class _HwMflpVsiCfgDetectCycle_Type(Unsigned32):
    """Custom type hwMflpVsiCfgDetectCycle based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 30),
    )


_HwMflpVsiCfgDetectCycle_Type.__name__ = "Unsigned32"
_HwMflpVsiCfgDetectCycle_Object = MibTableColumn
hwMflpVsiCfgDetectCycle = _HwMflpVsiCfgDetectCycle_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 160, 1, 2, 1, 3),
    _HwMflpVsiCfgDetectCycle_Type()
)
hwMflpVsiCfgDetectCycle.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMflpVsiCfgDetectCycle.setStatus("current")


class _HwMflpVsiCfgCycles_Type(Unsigned32):
    """Custom type hwMflpVsiCfgCycles based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_HwMflpVsiCfgCycles_Type.__name__ = "Unsigned32"
_HwMflpVsiCfgCycles_Object = MibTableColumn
hwMflpVsiCfgCycles = _HwMflpVsiCfgCycles_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 160, 1, 2, 1, 4),
    _HwMflpVsiCfgCycles_Type()
)
hwMflpVsiCfgCycles.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMflpVsiCfgCycles.setStatus("current")


class _HwMflpVsiCfgAction_Type(Integer32):
    """Custom type hwMflpVsiCfgAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alarmOnly", 2),
          ("block", 1))
    )


_HwMflpVsiCfgAction_Type.__name__ = "Integer32"
_HwMflpVsiCfgAction_Object = MibTableColumn
hwMflpVsiCfgAction = _HwMflpVsiCfgAction_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 160, 1, 2, 1, 5),
    _HwMflpVsiCfgAction_Type()
)
hwMflpVsiCfgAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMflpVsiCfgAction.setStatus("current")


class _HwMflpVsiCfgBlockTime_Type(Unsigned32):
    """Custom type hwMflpVsiCfgBlockTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwMflpVsiCfgBlockTime_Type.__name__ = "Unsigned32"
_HwMflpVsiCfgBlockTime_Object = MibTableColumn
hwMflpVsiCfgBlockTime = _HwMflpVsiCfgBlockTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 160, 1, 2, 1, 6),
    _HwMflpVsiCfgBlockTime_Type()
)
hwMflpVsiCfgBlockTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMflpVsiCfgBlockTime.setStatus("current")


class _HwMflpVsiCfgRetryTimes_Type(Unsigned32):
    """Custom type hwMflpVsiCfgRetryTimes based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_HwMflpVsiCfgRetryTimes_Type.__name__ = "Unsigned32"
_HwMflpVsiCfgRetryTimes_Object = MibTableColumn
hwMflpVsiCfgRetryTimes = _HwMflpVsiCfgRetryTimes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 160, 1, 2, 1, 7),
    _HwMflpVsiCfgRetryTimes_Type()
)
hwMflpVsiCfgRetryTimes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMflpVsiCfgRetryTimes.setStatus("current")


class _HwMflpVsiCfgBlockPolicy_Type(Integer32):
    """Custom type hwMflpVsiCfgBlockPolicy based on Integer32"""
    defaultValue = 1

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
        *(("acFirst", 2),
          ("acOnly", 4),
          ("default", 1),
          ("pwFirst", 3))
    )


_HwMflpVsiCfgBlockPolicy_Type.__name__ = "Integer32"
_HwMflpVsiCfgBlockPolicy_Object = MibTableColumn
hwMflpVsiCfgBlockPolicy = _HwMflpVsiCfgBlockPolicy_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 160, 1, 2, 1, 8),
    _HwMflpVsiCfgBlockPolicy_Type()
)
hwMflpVsiCfgBlockPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMflpVsiCfgBlockPolicy.setStatus("current")
_HwMflpVsiCfgAcName_Type = DisplayString
_HwMflpVsiCfgAcName_Object = MibTableColumn
hwMflpVsiCfgAcName = _HwMflpVsiCfgAcName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 160, 1, 2, 1, 9),
    _HwMflpVsiCfgAcName_Type()
)
hwMflpVsiCfgAcName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwMflpVsiCfgAcName.setStatus("current")
_HwMflpVsiCfgAlarmReason_Type = DisplayString
_HwMflpVsiCfgAlarmReason_Object = MibTableColumn
hwMflpVsiCfgAlarmReason = _HwMflpVsiCfgAlarmReason_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 160, 1, 2, 1, 10),
    _HwMflpVsiCfgAlarmReason_Type()
)
hwMflpVsiCfgAlarmReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwMflpVsiCfgAlarmReason.setStatus("current")
_HwMflpVsiCfgIpAddr_Type = IpAddress
_HwMflpVsiCfgIpAddr_Object = MibTableColumn
hwMflpVsiCfgIpAddr = _HwMflpVsiCfgIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 160, 1, 2, 1, 11),
    _HwMflpVsiCfgIpAddr_Type()
)
hwMflpVsiCfgIpAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwMflpVsiCfgIpAddr.setStatus("current")
_HwMflpVsiCfgPwId_Type = Unsigned32
_HwMflpVsiCfgPwId_Object = MibTableColumn
hwMflpVsiCfgPwId = _HwMflpVsiCfgPwId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 160, 1, 2, 1, 12),
    _HwMflpVsiCfgPwId_Type()
)
hwMflpVsiCfgPwId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwMflpVsiCfgPwId.setStatus("current")
_HwMflpVsiCfgRowstatus_Type = RowStatus
_HwMflpVsiCfgRowstatus_Object = MibTableColumn
hwMflpVsiCfgRowstatus = _HwMflpVsiCfgRowstatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 160, 1, 2, 1, 13),
    _HwMflpVsiCfgRowstatus_Type()
)
hwMflpVsiCfgRowstatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMflpVsiCfgRowstatus.setStatus("current")
_HwMflpVsiDetectMAC_Type = DisplayString
_HwMflpVsiDetectMAC_Object = MibTableColumn
hwMflpVsiDetectMAC = _HwMflpVsiDetectMAC_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 160, 1, 2, 1, 14),
    _HwMflpVsiDetectMAC_Type()
)
hwMflpVsiDetectMAC.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwMflpVsiDetectMAC.setStatus("current")
_HwMflpGeneralObjects_ObjectIdentity = ObjectIdentity
hwMflpGeneralObjects = _HwMflpGeneralObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 160, 2)
)
_HwMflpTrapEnable_Type = EnabledStatus
_HwMflpTrapEnable_Object = MibScalar
hwMflpTrapEnable = _HwMflpTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 160, 2, 1),
    _HwMflpTrapEnable_Type()
)
hwMflpTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMflpTrapEnable.setStatus("current")
_HwMflpMIBTraps_ObjectIdentity = ObjectIdentity
hwMflpMIBTraps = _HwMflpMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 160, 3)
)
_HwMflpConformance_ObjectIdentity = ObjectIdentity
hwMflpConformance = _HwMflpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 160, 4)
)
_HwMflpCompliances_ObjectIdentity = ObjectIdentity
hwMflpCompliances = _HwMflpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 160, 4, 1)
)
_HwMflpGroups_ObjectIdentity = ObjectIdentity
hwMflpGroups = _HwMflpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 160, 4, 2)
)

# Managed Objects groups

hwMflpVlanCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 160, 4, 2, 1)
)
hwMflpVlanCfgGroup.setObjects(
      *(("HUAWEI-MFLP-MIB", "hwMflpVlanCfgLoopTimes"),
        ("HUAWEI-MFLP-MIB", "hwMflpVlanCfgDetectCycle"),
        ("HUAWEI-MFLP-MIB", "hwMflpVlanCfgCycles"),
        ("HUAWEI-MFLP-MIB", "hwMflpVlanCfgRetryTimes"),
        ("HUAWEI-MFLP-MIB", "hwMflpVlanCfgAction"),
        ("HUAWEI-MFLP-MIB", "hwMflpVlanCfgBlockTime"),
        ("HUAWEI-MFLP-MIB", "hwMflpVlanCfgIfName"),
        ("HUAWEI-MFLP-MIB", "hwMflpVlanCfgAlarmReason"),
        ("HUAWEI-MFLP-MIB", "hwMflpVlanCfgRowstatus"),
        ("HUAWEI-MFLP-MIB", "hwMflpVlanDetectMAC"),
        ("HUAWEI-MFLP-MIB", "hwMflpVlanCfgMacAddr"),
        ("HUAWEI-MFLP-MIB", "hwMflpVlanCfgPreIfName"))
)
if mibBuilder.loadTexts:
    hwMflpVlanCfgGroup.setStatus("current")

hwMflpVsiCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 160, 4, 2, 2)
)
hwMflpVsiCfgGroup.setObjects(
      *(("HUAWEI-MFLP-MIB", "hwMflpVsiCfgLoopTimes"),
        ("HUAWEI-MFLP-MIB", "hwMflpVsiCfgDetectCycle"),
        ("HUAWEI-MFLP-MIB", "hwMflpVsiCfgCycles"),
        ("HUAWEI-MFLP-MIB", "hwMflpVsiCfgRetryTimes"),
        ("HUAWEI-MFLP-MIB", "hwMflpVsiCfgAction"),
        ("HUAWEI-MFLP-MIB", "hwMflpVsiCfgBlockTime"),
        ("HUAWEI-MFLP-MIB", "hwMflpVsiCfgBlockPolicy"),
        ("HUAWEI-MFLP-MIB", "hwMflpVsiCfgAcName"),
        ("HUAWEI-MFLP-MIB", "hwMflpVsiCfgAlarmReason"),
        ("HUAWEI-MFLP-MIB", "hwMflpVsiCfgIpAddr"),
        ("HUAWEI-MFLP-MIB", "hwMflpVsiCfgPwId"),
        ("HUAWEI-MFLP-MIB", "hwMflpVsiCfgRowstatus"),
        ("HUAWEI-MFLP-MIB", "hwMflpVsiDetectMAC"))
)
if mibBuilder.loadTexts:
    hwMflpVsiCfgGroup.setStatus("current")

hwMflpTrapEnableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 160, 4, 2, 3)
)
hwMflpTrapEnableGroup.setObjects(
    ("HUAWEI-MFLP-MIB", "hwMflpTrapEnable")
)
if mibBuilder.loadTexts:
    hwMflpTrapEnableGroup.setStatus("current")


# Notification objects

hwMflpIfBlock = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 160, 3, 1)
)
hwMflpIfBlock.setObjects(
      *(("HUAWEI-MFLP-MIB", "hwMflpVlanCfgIfName"),
        ("HUAWEI-MFLP-MIB", "hwMflpVlanCfgBlockTime"),
        ("HUAWEI-MFLP-MIB", "hwMflpVlanCfgAlarmReason"),
        ("HUAWEI-MFLP-MIB", "hwMflpVlanDetectMAC"))
)
if mibBuilder.loadTexts:
    hwMflpIfBlock.setStatus(
        "current"
    )

hwMflpIfResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 160, 3, 2)
)
hwMflpIfResume.setObjects(
      *(("HUAWEI-MFLP-MIB", "hwMflpVlanCfgIfName"),
        ("HUAWEI-MFLP-MIB", "hwMflpVlanCfgBlockTime"),
        ("HUAWEI-MFLP-MIB", "hwMflpVlanCfgAlarmReason"))
)
if mibBuilder.loadTexts:
    hwMflpIfResume.setStatus(
        "current"
    )

hwMflpAcBlock = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 160, 3, 3)
)
hwMflpAcBlock.setObjects(
      *(("HUAWEI-MFLP-MIB", "hwMflpVsiCfgAcName"),
        ("HUAWEI-MFLP-MIB", "hwMflpVsiCfgBlockTime"),
        ("HUAWEI-MFLP-MIB", "hwMflpVsiCfgAlarmReason"),
        ("HUAWEI-MFLP-MIB", "hwMflpVsiDetectMAC"))
)
if mibBuilder.loadTexts:
    hwMflpAcBlock.setStatus(
        "current"
    )

hwMflpAcResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 160, 3, 4)
)
hwMflpAcResume.setObjects(
      *(("HUAWEI-MFLP-MIB", "hwMflpVsiCfgAcName"),
        ("HUAWEI-MFLP-MIB", "hwMflpVsiCfgBlockTime"),
        ("HUAWEI-MFLP-MIB", "hwMflpVsiCfgAlarmReason"))
)
if mibBuilder.loadTexts:
    hwMflpAcResume.setStatus(
        "current"
    )

hwMflpPwBlock = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 160, 3, 5)
)
hwMflpPwBlock.setObjects(
      *(("HUAWEI-MFLP-MIB", "hwMflpVsiCfgIpAddr"),
        ("HUAWEI-MFLP-MIB", "hwMflpVsiCfgPwId"),
        ("HUAWEI-MFLP-MIB", "hwMflpVsiCfgBlockTime"),
        ("HUAWEI-MFLP-MIB", "hwMflpVsiCfgAlarmReason"),
        ("HUAWEI-MFLP-MIB", "hwMflpVsiDetectMAC"))
)
if mibBuilder.loadTexts:
    hwMflpPwBlock.setStatus(
        "current"
    )

hwMflpPwResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 160, 3, 6)
)
hwMflpPwResume.setObjects(
      *(("HUAWEI-MFLP-MIB", "hwMflpVsiCfgIpAddr"),
        ("HUAWEI-MFLP-MIB", "hwMflpVsiCfgPwId"),
        ("HUAWEI-MFLP-MIB", "hwMflpVsiCfgBlockTime"),
        ("HUAWEI-MFLP-MIB", "hwMflpVsiCfgAlarmReason"))
)
if mibBuilder.loadTexts:
    hwMflpPwResume.setStatus(
        "current"
    )

hwMflpVlanAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 160, 3, 7)
)
hwMflpVlanAlarm.setObjects(
    ("HUAWEI-MFLP-MIB", "hwMflpVlanCfgAlarmReason")
)
if mibBuilder.loadTexts:
    hwMflpVlanAlarm.setStatus(
        "current"
    )

hwMflpVsiAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 160, 3, 8)
)
hwMflpVsiAlarm.setObjects(
    ("HUAWEI-MFLP-MIB", "hwMflpVsiCfgAlarmReason")
)
if mibBuilder.loadTexts:
    hwMflpVsiAlarm.setStatus(
        "current"
    )

hwMflpMacAddrAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 160, 3, 9)
)
hwMflpMacAddrAlarm.setObjects(
      *(("HUAWEI-MFLP-MIB", "hwMflpVlanCfgMacAddr"),
        ("HUAWEI-MFLP-MIB", "hwMflpVlanCfgBlockTime"),
        ("HUAWEI-MFLP-MIB", "hwMflpVlanCfgPreIfName"),
        ("HUAWEI-MFLP-MIB", "hwMflpVlanCfgIfName"),
        ("HUAWEI-MFLP-MIB", "hwMflpVlanCfgAlarmReason"))
)
if mibBuilder.loadTexts:
    hwMflpMacAddrAlarm.setStatus(
        "current"
    )

hwMflpMacAddrResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 160, 3, 10)
)
hwMflpMacAddrResume.setObjects(
      *(("HUAWEI-MFLP-MIB", "hwMflpVlanCfgMacAddr"),
        ("HUAWEI-MFLP-MIB", "hwMflpVlanCfgBlockTime"),
        ("HUAWEI-MFLP-MIB", "hwMflpVlanCfgPreIfName"),
        ("HUAWEI-MFLP-MIB", "hwMflpVlanCfgIfName"),
        ("HUAWEI-MFLP-MIB", "hwMflpVlanCfgAlarmReason"))
)
if mibBuilder.loadTexts:
    hwMflpMacAddrResume.setStatus(
        "current"
    )

hwMflpQuitVlanAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 160, 3, 11)
)
hwMflpQuitVlanAlarm.setObjects(
      *(("HUAWEI-MFLP-MIB", "hwMflpVlanCfgIfName"),
        ("HUAWEI-MFLP-MIB", "hwMflpVlanCfgAlarmReason"))
)
if mibBuilder.loadTexts:
    hwMflpQuitVlanAlarm.setStatus(
        "current"
    )

hwMflpQuitVlanResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 160, 3, 12)
)
hwMflpQuitVlanResume.setObjects(
      *(("HUAWEI-MFLP-MIB", "hwMflpVlanCfgIfName"),
        ("HUAWEI-MFLP-MIB", "hwMflpVlanCfgAlarmReason"))
)
if mibBuilder.loadTexts:
    hwMflpQuitVlanResume.setStatus(
        "current"
    )


# Notifications groups

hwMflpTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 160, 4, 2, 4)
)
hwMflpTrapGroup.setObjects(
      *(("HUAWEI-MFLP-MIB", "hwMflpIfBlock"),
        ("HUAWEI-MFLP-MIB", "hwMflpIfResume"),
        ("HUAWEI-MFLP-MIB", "hwMflpAcBlock"),
        ("HUAWEI-MFLP-MIB", "hwMflpAcResume"),
        ("HUAWEI-MFLP-MIB", "hwMflpPwBlock"),
        ("HUAWEI-MFLP-MIB", "hwMflpPwResume"),
        ("HUAWEI-MFLP-MIB", "hwMflpVlanAlarm"),
        ("HUAWEI-MFLP-MIB", "hwMflpVsiAlarm"),
        ("HUAWEI-MFLP-MIB", "hwMflpMacAddrAlarm"),
        ("HUAWEI-MFLP-MIB", "hwMflpMacAddrResume"),
        ("HUAWEI-MFLP-MIB", "hwMflpQuitVlanAlarm"),
        ("HUAWEI-MFLP-MIB", "hwMflpQuitVlanResume"))
)
if mibBuilder.loadTexts:
    hwMflpTrapGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hwMflpFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 160, 4, 1, 1)
)
if mibBuilder.loadTexts:
    hwMflpFullCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-MFLP-MIB",
    **{"hwMFlpMIB": hwMFlpMIB,
       "hwMflpObjects": hwMflpObjects,
       "hwMflpVlanCfgTable": hwMflpVlanCfgTable,
       "hwMflpVlanCfgEntry": hwMflpVlanCfgEntry,
       "hwMflpVlanId": hwMflpVlanId,
       "hwMflpVlanCfgLoopTimes": hwMflpVlanCfgLoopTimes,
       "hwMflpVlanCfgDetectCycle": hwMflpVlanCfgDetectCycle,
       "hwMflpVlanCfgCycles": hwMflpVlanCfgCycles,
       "hwMflpVlanCfgAction": hwMflpVlanCfgAction,
       "hwMflpVlanCfgBlockTime": hwMflpVlanCfgBlockTime,
       "hwMflpVlanCfgRetryTimes": hwMflpVlanCfgRetryTimes,
       "hwMflpVlanCfgIfName": hwMflpVlanCfgIfName,
       "hwMflpVlanCfgAlarmReason": hwMflpVlanCfgAlarmReason,
       "hwMflpVlanCfgRowstatus": hwMflpVlanCfgRowstatus,
       "hwMflpVlanDetectMAC": hwMflpVlanDetectMAC,
       "hwMflpVlanCfgMacAddr": hwMflpVlanCfgMacAddr,
       "hwMflpVlanCfgPreIfName": hwMflpVlanCfgPreIfName,
       "hwMflpVsiCfgTable": hwMflpVsiCfgTable,
       "hwMflpVsiCfgEntry": hwMflpVsiCfgEntry,
       "hwMflpVsiName": hwMflpVsiName,
       "hwMflpVsiCfgLoopTimes": hwMflpVsiCfgLoopTimes,
       "hwMflpVsiCfgDetectCycle": hwMflpVsiCfgDetectCycle,
       "hwMflpVsiCfgCycles": hwMflpVsiCfgCycles,
       "hwMflpVsiCfgAction": hwMflpVsiCfgAction,
       "hwMflpVsiCfgBlockTime": hwMflpVsiCfgBlockTime,
       "hwMflpVsiCfgRetryTimes": hwMflpVsiCfgRetryTimes,
       "hwMflpVsiCfgBlockPolicy": hwMflpVsiCfgBlockPolicy,
       "hwMflpVsiCfgAcName": hwMflpVsiCfgAcName,
       "hwMflpVsiCfgAlarmReason": hwMflpVsiCfgAlarmReason,
       "hwMflpVsiCfgIpAddr": hwMflpVsiCfgIpAddr,
       "hwMflpVsiCfgPwId": hwMflpVsiCfgPwId,
       "hwMflpVsiCfgRowstatus": hwMflpVsiCfgRowstatus,
       "hwMflpVsiDetectMAC": hwMflpVsiDetectMAC,
       "hwMflpGeneralObjects": hwMflpGeneralObjects,
       "hwMflpTrapEnable": hwMflpTrapEnable,
       "hwMflpMIBTraps": hwMflpMIBTraps,
       "hwMflpIfBlock": hwMflpIfBlock,
       "hwMflpIfResume": hwMflpIfResume,
       "hwMflpAcBlock": hwMflpAcBlock,
       "hwMflpAcResume": hwMflpAcResume,
       "hwMflpPwBlock": hwMflpPwBlock,
       "hwMflpPwResume": hwMflpPwResume,
       "hwMflpVlanAlarm": hwMflpVlanAlarm,
       "hwMflpVsiAlarm": hwMflpVsiAlarm,
       "hwMflpMacAddrAlarm": hwMflpMacAddrAlarm,
       "hwMflpMacAddrResume": hwMflpMacAddrResume,
       "hwMflpQuitVlanAlarm": hwMflpQuitVlanAlarm,
       "hwMflpQuitVlanResume": hwMflpQuitVlanResume,
       "hwMflpConformance": hwMflpConformance,
       "hwMflpCompliances": hwMflpCompliances,
       "hwMflpFullCompliance": hwMflpFullCompliance,
       "hwMflpGroups": hwMflpGroups,
       "hwMflpVlanCfgGroup": hwMflpVlanCfgGroup,
       "hwMflpVsiCfgGroup": hwMflpVsiCfgGroup,
       "hwMflpTrapEnableGroup": hwMflpTrapEnableGroup,
       "hwMflpTrapGroup": hwMflpTrapGroup}
)
