# SNMP MIB module (HUAWEI-CCC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-CCC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:03:18 2024
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

(HWEnableValue,
 HWL2VpnStateChangeReason,
 HWL2VpnVcEncapsType) = mibBuilder.importSymbols(
    "HUAWEI-VPLS-EXT-MIB",
    "HWEnableValue",
    "HWL2VpnStateChangeReason",
    "HWL2VpnVcEncapsType")

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

hwL2VpnCCC = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 3)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwL2Vpn_ObjectIdentity = ObjectIdentity
hwL2Vpn = _HwL2Vpn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119)
)
_HwCCCMIBObjects_ObjectIdentity = ObjectIdentity
hwCCCMIBObjects = _HwCCCMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 3, 1)
)
_HwCCCVcTable_Object = MibTable
hwCCCVcTable = _HwCCCVcTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 3, 1, 1)
)
if mibBuilder.loadTexts:
    hwCCCVcTable.setStatus("current")
_HwCCCVcEntry_Object = MibTableRow
hwCCCVcEntry = _HwCCCVcEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 3, 1, 1, 1)
)
hwCCCVcEntry.setIndexNames(
    (0, "HUAWEI-CCC-MIB", "hwCCCVcName"),
)
if mibBuilder.loadTexts:
    hwCCCVcEntry.setStatus("current")


class _HwCCCVcName_Type(DisplayString):
    """Custom type hwCCCVcName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_HwCCCVcName_Type.__name__ = "DisplayString"
_HwCCCVcName_Object = MibTableColumn
hwCCCVcName = _HwCCCVcName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 3, 1, 1, 1, 1),
    _HwCCCVcName_Type()
)
hwCCCVcName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwCCCVcName.setStatus("current")


class _HwCCCVcConnectionType_Type(Integer32):
    """Custom type hwCCCVcConnectionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("remote", 2))
    )


_HwCCCVcConnectionType_Type.__name__ = "Integer32"
_HwCCCVcConnectionType_Object = MibTableColumn
hwCCCVcConnectionType = _HwCCCVcConnectionType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 3, 1, 1, 1, 2),
    _HwCCCVcConnectionType_Type()
)
hwCCCVcConnectionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCCCVcConnectionType.setStatus("current")
_HwCCCVcEncapType_Type = HWL2VpnVcEncapsType
_HwCCCVcEncapType_Object = MibTableColumn
hwCCCVcEncapType = _HwCCCVcEncapType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 3, 1, 1, 1, 3),
    _HwCCCVcEncapType_Type()
)
hwCCCVcEncapType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCCCVcEncapType.setStatus("current")
_HwCCCVcIfIndex_Type = InterfaceIndexOrZero
_HwCCCVcIfIndex_Object = MibTableColumn
hwCCCVcIfIndex = _HwCCCVcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 3, 1, 1, 1, 4),
    _HwCCCVcIfIndex_Type()
)
hwCCCVcIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCCCVcIfIndex.setStatus("current")
_HwCCCVcInboundlabel_Type = Unsigned32
_HwCCCVcInboundlabel_Object = MibTableColumn
hwCCCVcInboundlabel = _HwCCCVcInboundlabel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 3, 1, 1, 1, 5),
    _HwCCCVcInboundlabel_Type()
)
hwCCCVcInboundlabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCCCVcInboundlabel.setStatus("current")
_HwCCCVcOutboundlabel_Type = Unsigned32
_HwCCCVcOutboundlabel_Object = MibTableColumn
hwCCCVcOutboundlabel = _HwCCCVcOutboundlabel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 3, 1, 1, 1, 6),
    _HwCCCVcOutboundlabel_Type()
)
hwCCCVcOutboundlabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCCCVcOutboundlabel.setStatus("current")
_HwCCCVcOutIfIndex_Type = InterfaceIndexOrZero
_HwCCCVcOutIfIndex_Object = MibTableColumn
hwCCCVcOutIfIndex = _HwCCCVcOutIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 3, 1, 1, 1, 7),
    _HwCCCVcOutIfIndex_Type()
)
hwCCCVcOutIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCCCVcOutIfIndex.setStatus("current")
_HwCCCVcNextHop_Type = IpAddress
_HwCCCVcNextHop_Object = MibTableColumn
hwCCCVcNextHop = _HwCCCVcNextHop_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 3, 1, 1, 1, 8),
    _HwCCCVcNextHop_Type()
)
hwCCCVcNextHop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCCCVcNextHop.setStatus("current")
_HwCCCVcCtrlWord_Type = HWEnableValue
_HwCCCVcCtrlWord_Object = MibTableColumn
hwCCCVcCtrlWord = _HwCCCVcCtrlWord_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 3, 1, 1, 1, 9),
    _HwCCCVcCtrlWord_Type()
)
hwCCCVcCtrlWord.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCCCVcCtrlWord.setStatus("current")


class _HwCCCVcOperStatus_Type(Integer32):
    """Custom type hwCCCVcOperStatus based on Integer32"""
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


_HwCCCVcOperStatus_Type.__name__ = "Integer32"
_HwCCCVcOperStatus_Object = MibTableColumn
hwCCCVcOperStatus = _HwCCCVcOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 3, 1, 1, 1, 10),
    _HwCCCVcOperStatus_Type()
)
hwCCCVcOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCCCVcOperStatus.setStatus("current")


class _HwCCCVcUpStartTime_Type(DisplayString):
    """Custom type hwCCCVcUpStartTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_HwCCCVcUpStartTime_Type.__name__ = "DisplayString"
_HwCCCVcUpStartTime_Object = MibTableColumn
hwCCCVcUpStartTime = _HwCCCVcUpStartTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 3, 1, 1, 1, 11),
    _HwCCCVcUpStartTime_Type()
)
hwCCCVcUpStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCCCVcUpStartTime.setStatus("current")
_HwCCCVcUpSumTime_Type = Unsigned32
_HwCCCVcUpSumTime_Object = MibTableColumn
hwCCCVcUpSumTime = _HwCCCVcUpSumTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 3, 1, 1, 1, 12),
    _HwCCCVcUpSumTime_Type()
)
hwCCCVcUpSumTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCCCVcUpSumTime.setStatus("current")
_HwCCCVcMaxAtmCells_Type = Unsigned32
_HwCCCVcMaxAtmCells_Object = MibTableColumn
hwCCCVcMaxAtmCells = _HwCCCVcMaxAtmCells_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 3, 1, 1, 1, 13),
    _HwCCCVcMaxAtmCells_Type()
)
hwCCCVcMaxAtmCells.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCCCVcMaxAtmCells.setStatus("current")
_HwCCCVcAtmPackOvertime_Type = Unsigned32
_HwCCCVcAtmPackOvertime_Object = MibTableColumn
hwCCCVcAtmPackOvertime = _HwCCCVcAtmPackOvertime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 3, 1, 1, 1, 14),
    _HwCCCVcAtmPackOvertime_Type()
)
hwCCCVcAtmPackOvertime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCCCVcAtmPackOvertime.setStatus("current")
_HwCCCVcPwJitterBufferDepth_Type = Unsigned32
_HwCCCVcPwJitterBufferDepth_Object = MibTableColumn
hwCCCVcPwJitterBufferDepth = _HwCCCVcPwJitterBufferDepth_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 3, 1, 1, 1, 15),
    _HwCCCVcPwJitterBufferDepth_Type()
)
hwCCCVcPwJitterBufferDepth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCCCVcPwJitterBufferDepth.setStatus("current")
_HwCCCVcPwTdmEncapsulationNum_Type = Unsigned32
_HwCCCVcPwTdmEncapsulationNum_Object = MibTableColumn
hwCCCVcPwTdmEncapsulationNum = _HwCCCVcPwTdmEncapsulationNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 3, 1, 1, 1, 16),
    _HwCCCVcPwTdmEncapsulationNum_Type()
)
hwCCCVcPwTdmEncapsulationNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCCCVcPwTdmEncapsulationNum.setStatus("current")
_HwCCCVcPwIdleCode_Type = Unsigned32
_HwCCCVcPwIdleCode_Object = MibTableColumn
hwCCCVcPwIdleCode = _HwCCCVcPwIdleCode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 3, 1, 1, 1, 17),
    _HwCCCVcPwIdleCode_Type()
)
hwCCCVcPwIdleCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCCCVcPwIdleCode.setStatus("current")
_HwCCCVcPwRtpHeader_Type = Unsigned32
_HwCCCVcPwRtpHeader_Object = MibTableColumn
hwCCCVcPwRtpHeader = _HwCCCVcPwRtpHeader_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 3, 1, 1, 1, 18),
    _HwCCCVcPwRtpHeader_Type()
)
hwCCCVcPwRtpHeader.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCCCVcPwRtpHeader.setStatus("current")
_HwCCCVcIpInterworking_Type = HWEnableValue
_HwCCCVcIpInterworking_Object = MibTableColumn
hwCCCVcIpInterworking = _HwCCCVcIpInterworking_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 3, 1, 1, 1, 19),
    _HwCCCVcIpInterworking_Type()
)
hwCCCVcIpInterworking.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCCCVcIpInterworking.setStatus("current")
_HwCCCVcRowStatus_Type = RowStatus
_HwCCCVcRowStatus_Object = MibTableColumn
hwCCCVcRowStatus = _HwCCCVcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 3, 1, 1, 1, 51),
    _HwCCCVcRowStatus_Type()
)
hwCCCVcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCCCVcRowStatus.setStatus("current")
_HwCCCVcStatisticsTable_Object = MibTable
hwCCCVcStatisticsTable = _HwCCCVcStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 3, 1, 2)
)
if mibBuilder.loadTexts:
    hwCCCVcStatisticsTable.setStatus("current")
_HwCCCVcStatisticsEntry_Object = MibTableRow
hwCCCVcStatisticsEntry = _HwCCCVcStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 3, 1, 2, 1)
)
hwCCCVcStatisticsEntry.setIndexNames(
    (0, "HUAWEI-CCC-MIB", "hwCCCVcName"),
    (0, "HUAWEI-CCC-MIB", "hwCCCVcStatisticsIfIndex"),
)
if mibBuilder.loadTexts:
    hwCCCVcStatisticsEntry.setStatus("current")
_HwCCCVcStatisticsIfIndex_Type = InterfaceIndex
_HwCCCVcStatisticsIfIndex_Object = MibTableColumn
hwCCCVcStatisticsIfIndex = _HwCCCVcStatisticsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 3, 1, 2, 1, 1),
    _HwCCCVcStatisticsIfIndex_Type()
)
hwCCCVcStatisticsIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwCCCVcStatisticsIfIndex.setStatus("current")
_HwCCCVcStatisticsRcvPkts_Type = Counter64
_HwCCCVcStatisticsRcvPkts_Object = MibTableColumn
hwCCCVcStatisticsRcvPkts = _HwCCCVcStatisticsRcvPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 3, 1, 2, 1, 2),
    _HwCCCVcStatisticsRcvPkts_Type()
)
hwCCCVcStatisticsRcvPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCCCVcStatisticsRcvPkts.setStatus("current")
_HwCCCVcStatisticsRcvBytes_Type = Counter64
_HwCCCVcStatisticsRcvBytes_Object = MibTableColumn
hwCCCVcStatisticsRcvBytes = _HwCCCVcStatisticsRcvBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 3, 1, 2, 1, 3),
    _HwCCCVcStatisticsRcvBytes_Type()
)
hwCCCVcStatisticsRcvBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCCCVcStatisticsRcvBytes.setStatus("current")
_HwCCCVcStatisticsSndPkts_Type = Counter64
_HwCCCVcStatisticsSndPkts_Object = MibTableColumn
hwCCCVcStatisticsSndPkts = _HwCCCVcStatisticsSndPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 3, 1, 2, 1, 4),
    _HwCCCVcStatisticsSndPkts_Type()
)
hwCCCVcStatisticsSndPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCCCVcStatisticsSndPkts.setStatus("current")
_HwCCCVcStatisticsSndBytes_Type = Counter64
_HwCCCVcStatisticsSndBytes_Object = MibTableColumn
hwCCCVcStatisticsSndBytes = _HwCCCVcStatisticsSndBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 3, 1, 2, 1, 5),
    _HwCCCVcStatisticsSndBytes_Type()
)
hwCCCVcStatisticsSndBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCCCVcStatisticsSndBytes.setStatus("current")


class _HwCCCVcUpDownNotifEnable_Type(HWEnableValue):
    """Custom type hwCCCVcUpDownNotifEnable based on HWEnableValue"""


_HwCCCVcUpDownNotifEnable_Object = MibScalar
hwCCCVcUpDownNotifEnable = _HwCCCVcUpDownNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 3, 1, 3),
    _HwCCCVcUpDownNotifEnable_Type()
)
hwCCCVcUpDownNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwCCCVcUpDownNotifEnable.setStatus("current")


class _HwCCCVcDeletedNotifEnable_Type(HWEnableValue):
    """Custom type hwCCCVcDeletedNotifEnable based on HWEnableValue"""


_HwCCCVcDeletedNotifEnable_Object = MibScalar
hwCCCVcDeletedNotifEnable = _HwCCCVcDeletedNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 3, 1, 4),
    _HwCCCVcDeletedNotifEnable_Type()
)
hwCCCVcDeletedNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwCCCVcDeletedNotifEnable.setStatus("current")
_HwCCCVcStateChangeReason_Type = HWL2VpnStateChangeReason
_HwCCCVcStateChangeReason_Object = MibScalar
hwCCCVcStateChangeReason = _HwCCCVcStateChangeReason_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 3, 1, 5),
    _HwCCCVcStateChangeReason_Type()
)
hwCCCVcStateChangeReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwCCCVcStateChangeReason.setStatus("current")
_HwCCCMIBTraps_ObjectIdentity = ObjectIdentity
hwCCCMIBTraps = _HwCCCMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 3, 2)
)
_HwCCCMIBConformance_ObjectIdentity = ObjectIdentity
hwCCCMIBConformance = _HwCCCMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 3, 3)
)
_HwCCCMIBCompliances_ObjectIdentity = ObjectIdentity
hwCCCMIBCompliances = _HwCCCMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 3, 3, 1)
)
_HwCCCMIBGroups_ObjectIdentity = ObjectIdentity
hwCCCMIBGroups = _HwCCCMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 3, 3, 2)
)

# Managed Objects groups

hwCCCVcGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 3, 3, 2, 1)
)
hwCCCVcGroup.setObjects(
      *(("HUAWEI-CCC-MIB", "hwCCCVcConnectionType"),
        ("HUAWEI-CCC-MIB", "hwCCCVcEncapType"),
        ("HUAWEI-CCC-MIB", "hwCCCVcIfIndex"),
        ("HUAWEI-CCC-MIB", "hwCCCVcInboundlabel"),
        ("HUAWEI-CCC-MIB", "hwCCCVcOutboundlabel"),
        ("HUAWEI-CCC-MIB", "hwCCCVcOutIfIndex"),
        ("HUAWEI-CCC-MIB", "hwCCCVcNextHop"),
        ("HUAWEI-CCC-MIB", "hwCCCVcCtrlWord"),
        ("HUAWEI-CCC-MIB", "hwCCCVcOperStatus"),
        ("HUAWEI-CCC-MIB", "hwCCCVcUpStartTime"),
        ("HUAWEI-CCC-MIB", "hwCCCVcUpSumTime"),
        ("HUAWEI-CCC-MIB", "hwCCCVcMaxAtmCells"),
        ("HUAWEI-CCC-MIB", "hwCCCVcAtmPackOvertime"),
        ("HUAWEI-CCC-MIB", "hwCCCVcPwJitterBufferDepth"),
        ("HUAWEI-CCC-MIB", "hwCCCVcPwTdmEncapsulationNum"),
        ("HUAWEI-CCC-MIB", "hwCCCVcPwIdleCode"),
        ("HUAWEI-CCC-MIB", "hwCCCVcPwRtpHeader"),
        ("HUAWEI-CCC-MIB", "hwCCCVcIpInterworking"),
        ("HUAWEI-CCC-MIB", "hwCCCVcRowStatus"))
)
if mibBuilder.loadTexts:
    hwCCCVcGroup.setStatus("current")

hwCCCVcStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 3, 3, 2, 2)
)
hwCCCVcStatisticsGroup.setObjects(
      *(("HUAWEI-CCC-MIB", "hwCCCVcStatisticsRcvPkts"),
        ("HUAWEI-CCC-MIB", "hwCCCVcStatisticsRcvBytes"),
        ("HUAWEI-CCC-MIB", "hwCCCVcStatisticsSndPkts"),
        ("HUAWEI-CCC-MIB", "hwCCCVcStatisticsSndBytes"))
)
if mibBuilder.loadTexts:
    hwCCCVcStatisticsGroup.setStatus("current")

hwCCCNotificationControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 3, 3, 2, 3)
)
hwCCCNotificationControlGroup.setObjects(
      *(("HUAWEI-CCC-MIB", "hwCCCVcUpDownNotifEnable"),
        ("HUAWEI-CCC-MIB", "hwCCCVcDeletedNotifEnable"))
)
if mibBuilder.loadTexts:
    hwCCCNotificationControlGroup.setStatus("current")

hwCCCVcStateChangeReasonGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 3, 3, 2, 4)
)
hwCCCVcStateChangeReasonGroup.setObjects(
    ("HUAWEI-CCC-MIB", "hwCCCVcStateChangeReason")
)
if mibBuilder.loadTexts:
    hwCCCVcStateChangeReasonGroup.setStatus("current")


# Notification objects

hwCCCVcDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 3, 2, 1)
)
hwCCCVcDown.setObjects(
      *(("HUAWEI-CCC-MIB", "hwCCCVcIfIndex"),
        ("HUAWEI-CCC-MIB", "hwCCCVcStateChangeReason"))
)
if mibBuilder.loadTexts:
    hwCCCVcDown.setStatus(
        "current"
    )

hwCCCVcUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 3, 2, 2)
)
hwCCCVcUp.setObjects(
      *(("HUAWEI-CCC-MIB", "hwCCCVcIfIndex"),
        ("HUAWEI-CCC-MIB", "hwCCCVcStateChangeReason"))
)
if mibBuilder.loadTexts:
    hwCCCVcUp.setStatus(
        "current"
    )

hwCCCVcDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 3, 2, 3)
)
hwCCCVcDeleted.setObjects(
    ("HUAWEI-CCC-MIB", "hwCCCVcIfIndex")
)
if mibBuilder.loadTexts:
    hwCCCVcDeleted.setStatus(
        "current"
    )


# Notifications groups

hwCCCNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 3, 3, 2, 5)
)
hwCCCNotificationGroup.setObjects(
      *(("HUAWEI-CCC-MIB", "hwCCCVcDown"),
        ("HUAWEI-CCC-MIB", "hwCCCVcUp"),
        ("HUAWEI-CCC-MIB", "hwCCCVcDeleted"))
)
if mibBuilder.loadTexts:
    hwCCCNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hwCCCMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 3, 3, 1, 1)
)
if mibBuilder.loadTexts:
    hwCCCMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-CCC-MIB",
    **{"hwL2Vpn": hwL2Vpn,
       "hwL2VpnCCC": hwL2VpnCCC,
       "hwCCCMIBObjects": hwCCCMIBObjects,
       "hwCCCVcTable": hwCCCVcTable,
       "hwCCCVcEntry": hwCCCVcEntry,
       "hwCCCVcName": hwCCCVcName,
       "hwCCCVcConnectionType": hwCCCVcConnectionType,
       "hwCCCVcEncapType": hwCCCVcEncapType,
       "hwCCCVcIfIndex": hwCCCVcIfIndex,
       "hwCCCVcInboundlabel": hwCCCVcInboundlabel,
       "hwCCCVcOutboundlabel": hwCCCVcOutboundlabel,
       "hwCCCVcOutIfIndex": hwCCCVcOutIfIndex,
       "hwCCCVcNextHop": hwCCCVcNextHop,
       "hwCCCVcCtrlWord": hwCCCVcCtrlWord,
       "hwCCCVcOperStatus": hwCCCVcOperStatus,
       "hwCCCVcUpStartTime": hwCCCVcUpStartTime,
       "hwCCCVcUpSumTime": hwCCCVcUpSumTime,
       "hwCCCVcMaxAtmCells": hwCCCVcMaxAtmCells,
       "hwCCCVcAtmPackOvertime": hwCCCVcAtmPackOvertime,
       "hwCCCVcPwJitterBufferDepth": hwCCCVcPwJitterBufferDepth,
       "hwCCCVcPwTdmEncapsulationNum": hwCCCVcPwTdmEncapsulationNum,
       "hwCCCVcPwIdleCode": hwCCCVcPwIdleCode,
       "hwCCCVcPwRtpHeader": hwCCCVcPwRtpHeader,
       "hwCCCVcIpInterworking": hwCCCVcIpInterworking,
       "hwCCCVcRowStatus": hwCCCVcRowStatus,
       "hwCCCVcStatisticsTable": hwCCCVcStatisticsTable,
       "hwCCCVcStatisticsEntry": hwCCCVcStatisticsEntry,
       "hwCCCVcStatisticsIfIndex": hwCCCVcStatisticsIfIndex,
       "hwCCCVcStatisticsRcvPkts": hwCCCVcStatisticsRcvPkts,
       "hwCCCVcStatisticsRcvBytes": hwCCCVcStatisticsRcvBytes,
       "hwCCCVcStatisticsSndPkts": hwCCCVcStatisticsSndPkts,
       "hwCCCVcStatisticsSndBytes": hwCCCVcStatisticsSndBytes,
       "hwCCCVcUpDownNotifEnable": hwCCCVcUpDownNotifEnable,
       "hwCCCVcDeletedNotifEnable": hwCCCVcDeletedNotifEnable,
       "hwCCCVcStateChangeReason": hwCCCVcStateChangeReason,
       "hwCCCMIBTraps": hwCCCMIBTraps,
       "hwCCCVcDown": hwCCCVcDown,
       "hwCCCVcUp": hwCCCVcUp,
       "hwCCCVcDeleted": hwCCCVcDeleted,
       "hwCCCMIBConformance": hwCCCMIBConformance,
       "hwCCCMIBCompliances": hwCCCMIBCompliances,
       "hwCCCMIBCompliance": hwCCCMIBCompliance,
       "hwCCCMIBGroups": hwCCCMIBGroups,
       "hwCCCVcGroup": hwCCCVcGroup,
       "hwCCCVcStatisticsGroup": hwCCCVcStatisticsGroup,
       "hwCCCNotificationControlGroup": hwCCCNotificationControlGroup,
       "hwCCCVcStateChangeReasonGroup": hwCCCVcStateChangeReasonGroup,
       "hwCCCNotificationGroup": hwCCCNotificationGroup}
)
