# SNMP MIB module (HUAWEI-GTSM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-GTSM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:03:54 2024
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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

hwGTSMModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 126)
)
hwGTSMModule.setRevisions(
        ("2006-09-05 19:38",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwGTSM_ObjectIdentity = ObjectIdentity
hwGTSM = _HwGTSM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 126, 1)
)


class _HwGTSMDefaultAction_Type(Integer32):
    """Custom type hwGTSMDefaultAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("drop", 2),
          ("pass", 1))
    )


_HwGTSMDefaultAction_Type.__name__ = "Integer32"
_HwGTSMDefaultAction_Object = MibScalar
hwGTSMDefaultAction = _HwGTSMDefaultAction_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 126, 1, 1),
    _HwGTSMDefaultAction_Type()
)
hwGTSMDefaultAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwGTSMDefaultAction.setStatus("current")
_HwGTSMPolicyTable_Object = MibTable
hwGTSMPolicyTable = _HwGTSMPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 126, 1, 2)
)
if mibBuilder.loadTexts:
    hwGTSMPolicyTable.setStatus("current")
_HwGTSMPolicyEntry_Object = MibTableRow
hwGTSMPolicyEntry = _HwGTSMPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 126, 1, 2, 1)
)
hwGTSMPolicyEntry.setIndexNames(
    (0, "HUAWEI-GTSM-MIB", "hwGTSMvrfIndex"),
    (0, "HUAWEI-GTSM-MIB", "hwGTSMPolicyAddressType"),
    (0, "HUAWEI-GTSM-MIB", "hwGTSMPolicyProtocol"),
    (0, "HUAWEI-GTSM-MIB", "hwGTSMPolicySourceIpAddress"),
    (0, "HUAWEI-GTSM-MIB", "hwGTSMPolicyDestIpAddress"),
    (0, "HUAWEI-GTSM-MIB", "hwGTSMPolicySourcePort"),
    (0, "HUAWEI-GTSM-MIB", "hwGTSMPolicyDestPort"),
)
if mibBuilder.loadTexts:
    hwGTSMPolicyEntry.setStatus("current")


class _HwGTSMvrfIndex_Type(Integer32):
    """Custom type hwGTSMvrfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwGTSMvrfIndex_Type.__name__ = "Integer32"
_HwGTSMvrfIndex_Object = MibTableColumn
hwGTSMvrfIndex = _HwGTSMvrfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 126, 1, 2, 1, 1),
    _HwGTSMvrfIndex_Type()
)
hwGTSMvrfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwGTSMvrfIndex.setStatus("current")
_HwGTSMPolicyAddressType_Type = InetAddressType
_HwGTSMPolicyAddressType_Object = MibTableColumn
hwGTSMPolicyAddressType = _HwGTSMPolicyAddressType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 126, 1, 2, 1, 2),
    _HwGTSMPolicyAddressType_Type()
)
hwGTSMPolicyAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwGTSMPolicyAddressType.setStatus("current")


class _HwGTSMPolicyProtocol_Type(Integer32):
    """Custom type hwGTSMPolicyProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_HwGTSMPolicyProtocol_Type.__name__ = "Integer32"
_HwGTSMPolicyProtocol_Object = MibTableColumn
hwGTSMPolicyProtocol = _HwGTSMPolicyProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 126, 1, 2, 1, 3),
    _HwGTSMPolicyProtocol_Type()
)
hwGTSMPolicyProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwGTSMPolicyProtocol.setStatus("current")
_HwGTSMPolicySourceIpAddress_Type = InetAddress
_HwGTSMPolicySourceIpAddress_Object = MibTableColumn
hwGTSMPolicySourceIpAddress = _HwGTSMPolicySourceIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 126, 1, 2, 1, 4),
    _HwGTSMPolicySourceIpAddress_Type()
)
hwGTSMPolicySourceIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwGTSMPolicySourceIpAddress.setStatus("current")
_HwGTSMPolicyDestIpAddress_Type = InetAddress
_HwGTSMPolicyDestIpAddress_Object = MibTableColumn
hwGTSMPolicyDestIpAddress = _HwGTSMPolicyDestIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 126, 1, 2, 1, 5),
    _HwGTSMPolicyDestIpAddress_Type()
)
hwGTSMPolicyDestIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwGTSMPolicyDestIpAddress.setStatus("current")


class _HwGTSMPolicySourcePort_Type(Integer32):
    """Custom type hwGTSMPolicySourcePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwGTSMPolicySourcePort_Type.__name__ = "Integer32"
_HwGTSMPolicySourcePort_Object = MibTableColumn
hwGTSMPolicySourcePort = _HwGTSMPolicySourcePort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 126, 1, 2, 1, 6),
    _HwGTSMPolicySourcePort_Type()
)
hwGTSMPolicySourcePort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwGTSMPolicySourcePort.setStatus("current")


class _HwGTSMPolicyDestPort_Type(Integer32):
    """Custom type hwGTSMPolicyDestPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwGTSMPolicyDestPort_Type.__name__ = "Integer32"
_HwGTSMPolicyDestPort_Object = MibTableColumn
hwGTSMPolicyDestPort = _HwGTSMPolicyDestPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 126, 1, 2, 1, 7),
    _HwGTSMPolicyDestPort_Type()
)
hwGTSMPolicyDestPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwGTSMPolicyDestPort.setStatus("current")


class _HwGTSMPolicyTTLMin_Type(Integer32):
    """Custom type hwGTSMPolicyTTLMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_HwGTSMPolicyTTLMin_Type.__name__ = "Integer32"
_HwGTSMPolicyTTLMin_Object = MibTableColumn
hwGTSMPolicyTTLMin = _HwGTSMPolicyTTLMin_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 126, 1, 2, 1, 11),
    _HwGTSMPolicyTTLMin_Type()
)
hwGTSMPolicyTTLMin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwGTSMPolicyTTLMin.setStatus("current")


class _HwGTSMPolicyTTLMax_Type(Integer32):
    """Custom type hwGTSMPolicyTTLMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_HwGTSMPolicyTTLMax_Type.__name__ = "Integer32"
_HwGTSMPolicyTTLMax_Object = MibTableColumn
hwGTSMPolicyTTLMax = _HwGTSMPolicyTTLMax_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 126, 1, 2, 1, 12),
    _HwGTSMPolicyTTLMax_Type()
)
hwGTSMPolicyTTLMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwGTSMPolicyTTLMax.setStatus("current")
_HwGTSMPolicyRowStatus_Type = RowStatus
_HwGTSMPolicyRowStatus_Object = MibTableColumn
hwGTSMPolicyRowStatus = _HwGTSMPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 126, 1, 2, 1, 51),
    _HwGTSMPolicyRowStatus_Type()
)
hwGTSMPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwGTSMPolicyRowStatus.setStatus("current")
_HwGTSMBgpPeergroupTable_Object = MibTable
hwGTSMBgpPeergroupTable = _HwGTSMBgpPeergroupTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 126, 1, 3)
)
if mibBuilder.loadTexts:
    hwGTSMBgpPeergroupTable.setStatus("current")
_HwGTSMBgpPeergroupEntry_Object = MibTableRow
hwGTSMBgpPeergroupEntry = _HwGTSMBgpPeergroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 126, 1, 3, 1)
)
hwGTSMBgpPeergroupEntry.setIndexNames(
    (0, "HUAWEI-GTSM-MIB", "hwGTSMvrfIndex"),
    (0, "HUAWEI-GTSM-MIB", "hwGTSMBgpPeergroupName"),
)
if mibBuilder.loadTexts:
    hwGTSMBgpPeergroupEntry.setStatus("current")


class _HwGTSMBgpPeergroupName_Type(OctetString):
    """Custom type hwGTSMBgpPeergroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 47),
    )


_HwGTSMBgpPeergroupName_Type.__name__ = "OctetString"
_HwGTSMBgpPeergroupName_Object = MibTableColumn
hwGTSMBgpPeergroupName = _HwGTSMBgpPeergroupName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 126, 1, 3, 1, 1),
    _HwGTSMBgpPeergroupName_Type()
)
hwGTSMBgpPeergroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwGTSMBgpPeergroupName.setStatus("current")


class _HwGTSMBgpPeergroupTTLMin_Type(Integer32):
    """Custom type hwGTSMBgpPeergroupTTLMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_HwGTSMBgpPeergroupTTLMin_Type.__name__ = "Integer32"
_HwGTSMBgpPeergroupTTLMin_Object = MibTableColumn
hwGTSMBgpPeergroupTTLMin = _HwGTSMBgpPeergroupTTLMin_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 126, 1, 3, 1, 11),
    _HwGTSMBgpPeergroupTTLMin_Type()
)
hwGTSMBgpPeergroupTTLMin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwGTSMBgpPeergroupTTLMin.setStatus("current")


class _HwGTSMBgpPeergroupTTLMax_Type(Integer32):
    """Custom type hwGTSMBgpPeergroupTTLMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_HwGTSMBgpPeergroupTTLMax_Type.__name__ = "Integer32"
_HwGTSMBgpPeergroupTTLMax_Object = MibTableColumn
hwGTSMBgpPeergroupTTLMax = _HwGTSMBgpPeergroupTTLMax_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 126, 1, 3, 1, 12),
    _HwGTSMBgpPeergroupTTLMax_Type()
)
hwGTSMBgpPeergroupTTLMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwGTSMBgpPeergroupTTLMax.setStatus("current")
_HwGTSMBgpPeergroupRowStatus_Type = RowStatus
_HwGTSMBgpPeergroupRowStatus_Object = MibTableColumn
hwGTSMBgpPeergroupRowStatus = _HwGTSMBgpPeergroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 126, 1, 3, 1, 51),
    _HwGTSMBgpPeergroupRowStatus_Type()
)
hwGTSMBgpPeergroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwGTSMBgpPeergroupRowStatus.setStatus("current")
_HwGTSMStatisticsTable_Object = MibTable
hwGTSMStatisticsTable = _HwGTSMStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 126, 1, 4)
)
if mibBuilder.loadTexts:
    hwGTSMStatisticsTable.setStatus("current")
_HwGTSMStatisticsEntry_Object = MibTableRow
hwGTSMStatisticsEntry = _HwGTSMStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 126, 1, 4, 1)
)
hwGTSMStatisticsEntry.setIndexNames(
    (0, "HUAWEI-GTSM-MIB", "hwGTSMSlotIndex"),
)
if mibBuilder.loadTexts:
    hwGTSMStatisticsEntry.setStatus("current")


class _HwGTSMSlotIndex_Type(Integer32):
    """Custom type hwGTSMSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_HwGTSMSlotIndex_Type.__name__ = "Integer32"
_HwGTSMSlotIndex_Object = MibTableColumn
hwGTSMSlotIndex = _HwGTSMSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 126, 1, 4, 1, 1),
    _HwGTSMSlotIndex_Type()
)
hwGTSMSlotIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwGTSMSlotIndex.setStatus("current")
_HwGTSMStatisticsRcvPacketNumber_Type = Counter64
_HwGTSMStatisticsRcvPacketNumber_Object = MibTableColumn
hwGTSMStatisticsRcvPacketNumber = _HwGTSMStatisticsRcvPacketNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 126, 1, 4, 1, 11),
    _HwGTSMStatisticsRcvPacketNumber_Type()
)
hwGTSMStatisticsRcvPacketNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwGTSMStatisticsRcvPacketNumber.setStatus("current")
_HwGTSMStatisticsPassPacketNumber_Type = Counter64
_HwGTSMStatisticsPassPacketNumber_Object = MibTableColumn
hwGTSMStatisticsPassPacketNumber = _HwGTSMStatisticsPassPacketNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 126, 1, 4, 1, 12),
    _HwGTSMStatisticsPassPacketNumber_Type()
)
hwGTSMStatisticsPassPacketNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwGTSMStatisticsPassPacketNumber.setStatus("current")
_HwGTSMStatisticsDropPacketNumber_Type = Counter64
_HwGTSMStatisticsDropPacketNumber_Object = MibTableColumn
hwGTSMStatisticsDropPacketNumber = _HwGTSMStatisticsDropPacketNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 126, 1, 4, 1, 13),
    _HwGTSMStatisticsDropPacketNumber_Type()
)
hwGTSMStatisticsDropPacketNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwGTSMStatisticsDropPacketNumber.setStatus("current")
_HwGTSMGlobalConfigTable_Object = MibTable
hwGTSMGlobalConfigTable = _HwGTSMGlobalConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 126, 1, 5)
)
if mibBuilder.loadTexts:
    hwGTSMGlobalConfigTable.setStatus("current")
_HwGTSMGlobalConfigEntry_Object = MibTableRow
hwGTSMGlobalConfigEntry = _HwGTSMGlobalConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 126, 1, 5, 1)
)
hwGTSMGlobalConfigEntry.setIndexNames(
    (0, "HUAWEI-GTSM-MIB", "hwGTSMSlotIndex"),
)
if mibBuilder.loadTexts:
    hwGTSMGlobalConfigEntry.setStatus("current")


class _HwGTSMGlobalConfigClearStatistics_Type(Integer32):
    """Custom type hwGTSMGlobalConfigClearStatistics based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("reset", 1),
          ("unused", 255))
    )


_HwGTSMGlobalConfigClearStatistics_Type.__name__ = "Integer32"
_HwGTSMGlobalConfigClearStatistics_Object = MibTableColumn
hwGTSMGlobalConfigClearStatistics = _HwGTSMGlobalConfigClearStatistics_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 126, 1, 5, 1, 11),
    _HwGTSMGlobalConfigClearStatistics_Type()
)
hwGTSMGlobalConfigClearStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwGTSMGlobalConfigClearStatistics.setStatus("current")


class _HwGTSMGlobalConfigLogDroppedPacket_Type(Integer32):
    """Custom type hwGTSMGlobalConfigLogDroppedPacket based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("log", 1),
          ("nolog", 2))
    )


_HwGTSMGlobalConfigLogDroppedPacket_Type.__name__ = "Integer32"
_HwGTSMGlobalConfigLogDroppedPacket_Object = MibTableColumn
hwGTSMGlobalConfigLogDroppedPacket = _HwGTSMGlobalConfigLogDroppedPacket_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 126, 1, 5, 1, 12),
    _HwGTSMGlobalConfigLogDroppedPacket_Type()
)
hwGTSMGlobalConfigLogDroppedPacket.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwGTSMGlobalConfigLogDroppedPacket.setStatus("current")
_HwGTSMStatisticsInfoTable_Object = MibTable
hwGTSMStatisticsInfoTable = _HwGTSMStatisticsInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 126, 1, 6)
)
if mibBuilder.loadTexts:
    hwGTSMStatisticsInfoTable.setStatus("current")
_HwGTSMStatisticsInfoEntry_Object = MibTableRow
hwGTSMStatisticsInfoEntry = _HwGTSMStatisticsInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 126, 1, 6, 1)
)
hwGTSMStatisticsInfoEntry.setIndexNames(
    (0, "HUAWEI-GTSM-MIB", "hwGTSMSlotNum"),
    (0, "HUAWEI-GTSM-MIB", "hwGTSMPolicyAddressType"),
    (0, "HUAWEI-GTSM-MIB", "hwGTSMPolicyProtocol"),
)
if mibBuilder.loadTexts:
    hwGTSMStatisticsInfoEntry.setStatus("current")


class _HwGTSMSlotNum_Type(Integer32):
    """Custom type hwGTSMSlotNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_HwGTSMSlotNum_Type.__name__ = "Integer32"
_HwGTSMSlotNum_Object = MibTableColumn
hwGTSMSlotNum = _HwGTSMSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 126, 1, 6, 1, 1),
    _HwGTSMSlotNum_Type()
)
hwGTSMSlotNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwGTSMSlotNum.setStatus("current")
_HwGTSMStatisticsReceivePacketNum_Type = Counter64
_HwGTSMStatisticsReceivePacketNum_Object = MibTableColumn
hwGTSMStatisticsReceivePacketNum = _HwGTSMStatisticsReceivePacketNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 126, 1, 6, 1, 11),
    _HwGTSMStatisticsReceivePacketNum_Type()
)
hwGTSMStatisticsReceivePacketNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwGTSMStatisticsReceivePacketNum.setStatus("current")
_HwGTSMStatisticsPassPacketNum_Type = Counter64
_HwGTSMStatisticsPassPacketNum_Object = MibTableColumn
hwGTSMStatisticsPassPacketNum = _HwGTSMStatisticsPassPacketNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 126, 1, 6, 1, 12),
    _HwGTSMStatisticsPassPacketNum_Type()
)
hwGTSMStatisticsPassPacketNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwGTSMStatisticsPassPacketNum.setStatus("current")
_HwGTSMStatisticsDropPacketNum_Type = Counter64
_HwGTSMStatisticsDropPacketNum_Object = MibTableColumn
hwGTSMStatisticsDropPacketNum = _HwGTSMStatisticsDropPacketNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 126, 1, 6, 1, 13),
    _HwGTSMStatisticsDropPacketNum_Type()
)
hwGTSMStatisticsDropPacketNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwGTSMStatisticsDropPacketNum.setStatus("current")
_HwGTSMGlobalConfigInfoTable_Object = MibTable
hwGTSMGlobalConfigInfoTable = _HwGTSMGlobalConfigInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 126, 1, 7)
)
if mibBuilder.loadTexts:
    hwGTSMGlobalConfigInfoTable.setStatus("current")
_HwGTSMGlobalConfigInfoEntry_Object = MibTableRow
hwGTSMGlobalConfigInfoEntry = _HwGTSMGlobalConfigInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 126, 1, 7, 1)
)
hwGTSMGlobalConfigInfoEntry.setIndexNames(
    (0, "HUAWEI-GTSM-MIB", "hwGTSMSlotNum"),
)
if mibBuilder.loadTexts:
    hwGTSMGlobalConfigInfoEntry.setStatus("current")


class _HwGTSMGlobalConfigClearStatisticsInfo_Type(Integer32):
    """Custom type hwGTSMGlobalConfigClearStatisticsInfo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("reset", 1),
          ("unused", 255))
    )


_HwGTSMGlobalConfigClearStatisticsInfo_Type.__name__ = "Integer32"
_HwGTSMGlobalConfigClearStatisticsInfo_Object = MibTableColumn
hwGTSMGlobalConfigClearStatisticsInfo = _HwGTSMGlobalConfigClearStatisticsInfo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 126, 1, 7, 1, 11),
    _HwGTSMGlobalConfigClearStatisticsInfo_Type()
)
hwGTSMGlobalConfigClearStatisticsInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwGTSMGlobalConfigClearStatisticsInfo.setStatus("current")


class _HwGTSMGlobalConfigLogDroppedPacketInfo_Type(Integer32):
    """Custom type hwGTSMGlobalConfigLogDroppedPacketInfo based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("log", 1),
          ("nolog", 2))
    )


_HwGTSMGlobalConfigLogDroppedPacketInfo_Type.__name__ = "Integer32"
_HwGTSMGlobalConfigLogDroppedPacketInfo_Object = MibTableColumn
hwGTSMGlobalConfigLogDroppedPacketInfo = _HwGTSMGlobalConfigLogDroppedPacketInfo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 126, 1, 7, 1, 12),
    _HwGTSMGlobalConfigLogDroppedPacketInfo_Type()
)
hwGTSMGlobalConfigLogDroppedPacketInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwGTSMGlobalConfigLogDroppedPacketInfo.setStatus("current")
_HwGTSMConformance_ObjectIdentity = ObjectIdentity
hwGTSMConformance = _HwGTSMConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 126, 2)
)
_HwGTSMCompliances_ObjectIdentity = ObjectIdentity
hwGTSMCompliances = _HwGTSMCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 126, 2, 1)
)
_HwGTSMGroups_ObjectIdentity = ObjectIdentity
hwGTSMGroups = _HwGTSMGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 126, 2, 2)
)

# Managed Objects groups

hwGTSMDefaultActionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 126, 2, 2, 1)
)
hwGTSMDefaultActionGroup.setObjects(
    ("HUAWEI-GTSM-MIB", "hwGTSMDefaultAction")
)
if mibBuilder.loadTexts:
    hwGTSMDefaultActionGroup.setStatus("current")

hwGTSMPolicyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 126, 2, 2, 2)
)
hwGTSMPolicyGroup.setObjects(
      *(("HUAWEI-GTSM-MIB", "hwGTSMPolicyTTLMin"),
        ("HUAWEI-GTSM-MIB", "hwGTSMPolicyTTLMax"),
        ("HUAWEI-GTSM-MIB", "hwGTSMPolicyRowStatus"))
)
if mibBuilder.loadTexts:
    hwGTSMPolicyGroup.setStatus("current")

hwGTSMBgpPeergroupGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 126, 2, 2, 3)
)
hwGTSMBgpPeergroupGroup.setObjects(
      *(("HUAWEI-GTSM-MIB", "hwGTSMBgpPeergroupTTLMin"),
        ("HUAWEI-GTSM-MIB", "hwGTSMBgpPeergroupTTLMax"),
        ("HUAWEI-GTSM-MIB", "hwGTSMBgpPeergroupRowStatus"))
)
if mibBuilder.loadTexts:
    hwGTSMBgpPeergroupGroup.setStatus("current")

hwGTSMStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 126, 2, 2, 4)
)
hwGTSMStatisticsGroup.setObjects(
      *(("HUAWEI-GTSM-MIB", "hwGTSMStatisticsRcvPacketNumber"),
        ("HUAWEI-GTSM-MIB", "hwGTSMStatisticsPassPacketNumber"),
        ("HUAWEI-GTSM-MIB", "hwGTSMStatisticsDropPacketNumber"))
)
if mibBuilder.loadTexts:
    hwGTSMStatisticsGroup.setStatus("current")

hwGTSMGlobalConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 126, 2, 2, 5)
)
hwGTSMGlobalConfigGroup.setObjects(
      *(("HUAWEI-GTSM-MIB", "hwGTSMGlobalConfigClearStatistics"),
        ("HUAWEI-GTSM-MIB", "hwGTSMGlobalConfigLogDroppedPacket"))
)
if mibBuilder.loadTexts:
    hwGTSMGlobalConfigGroup.setStatus("current")

hwGTSMStatisticsInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 126, 2, 2, 6)
)
hwGTSMStatisticsInfoGroup.setObjects(
      *(("HUAWEI-GTSM-MIB", "hwGTSMStatisticsReceivePacketNum"),
        ("HUAWEI-GTSM-MIB", "hwGTSMStatisticsPassPacketNum"),
        ("HUAWEI-GTSM-MIB", "hwGTSMStatisticsDropPacketNum"))
)
if mibBuilder.loadTexts:
    hwGTSMStatisticsInfoGroup.setStatus("current")

hwGTSMGlobalConfigInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 126, 2, 2, 7)
)
hwGTSMGlobalConfigInfoGroup.setObjects(
      *(("HUAWEI-GTSM-MIB", "hwGTSMGlobalConfigClearStatisticsInfo"),
        ("HUAWEI-GTSM-MIB", "hwGTSMGlobalConfigLogDroppedPacketInfo"))
)
if mibBuilder.loadTexts:
    hwGTSMGlobalConfigInfoGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hwGTSMCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 126, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hwGTSMCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-GTSM-MIB",
    **{"hwGTSMModule": hwGTSMModule,
       "hwGTSM": hwGTSM,
       "hwGTSMDefaultAction": hwGTSMDefaultAction,
       "hwGTSMPolicyTable": hwGTSMPolicyTable,
       "hwGTSMPolicyEntry": hwGTSMPolicyEntry,
       "hwGTSMvrfIndex": hwGTSMvrfIndex,
       "hwGTSMPolicyAddressType": hwGTSMPolicyAddressType,
       "hwGTSMPolicyProtocol": hwGTSMPolicyProtocol,
       "hwGTSMPolicySourceIpAddress": hwGTSMPolicySourceIpAddress,
       "hwGTSMPolicyDestIpAddress": hwGTSMPolicyDestIpAddress,
       "hwGTSMPolicySourcePort": hwGTSMPolicySourcePort,
       "hwGTSMPolicyDestPort": hwGTSMPolicyDestPort,
       "hwGTSMPolicyTTLMin": hwGTSMPolicyTTLMin,
       "hwGTSMPolicyTTLMax": hwGTSMPolicyTTLMax,
       "hwGTSMPolicyRowStatus": hwGTSMPolicyRowStatus,
       "hwGTSMBgpPeergroupTable": hwGTSMBgpPeergroupTable,
       "hwGTSMBgpPeergroupEntry": hwGTSMBgpPeergroupEntry,
       "hwGTSMBgpPeergroupName": hwGTSMBgpPeergroupName,
       "hwGTSMBgpPeergroupTTLMin": hwGTSMBgpPeergroupTTLMin,
       "hwGTSMBgpPeergroupTTLMax": hwGTSMBgpPeergroupTTLMax,
       "hwGTSMBgpPeergroupRowStatus": hwGTSMBgpPeergroupRowStatus,
       "hwGTSMStatisticsTable": hwGTSMStatisticsTable,
       "hwGTSMStatisticsEntry": hwGTSMStatisticsEntry,
       "hwGTSMSlotIndex": hwGTSMSlotIndex,
       "hwGTSMStatisticsRcvPacketNumber": hwGTSMStatisticsRcvPacketNumber,
       "hwGTSMStatisticsPassPacketNumber": hwGTSMStatisticsPassPacketNumber,
       "hwGTSMStatisticsDropPacketNumber": hwGTSMStatisticsDropPacketNumber,
       "hwGTSMGlobalConfigTable": hwGTSMGlobalConfigTable,
       "hwGTSMGlobalConfigEntry": hwGTSMGlobalConfigEntry,
       "hwGTSMGlobalConfigClearStatistics": hwGTSMGlobalConfigClearStatistics,
       "hwGTSMGlobalConfigLogDroppedPacket": hwGTSMGlobalConfigLogDroppedPacket,
       "hwGTSMStatisticsInfoTable": hwGTSMStatisticsInfoTable,
       "hwGTSMStatisticsInfoEntry": hwGTSMStatisticsInfoEntry,
       "hwGTSMSlotNum": hwGTSMSlotNum,
       "hwGTSMStatisticsReceivePacketNum": hwGTSMStatisticsReceivePacketNum,
       "hwGTSMStatisticsPassPacketNum": hwGTSMStatisticsPassPacketNum,
       "hwGTSMStatisticsDropPacketNum": hwGTSMStatisticsDropPacketNum,
       "hwGTSMGlobalConfigInfoTable": hwGTSMGlobalConfigInfoTable,
       "hwGTSMGlobalConfigInfoEntry": hwGTSMGlobalConfigInfoEntry,
       "hwGTSMGlobalConfigClearStatisticsInfo": hwGTSMGlobalConfigClearStatisticsInfo,
       "hwGTSMGlobalConfigLogDroppedPacketInfo": hwGTSMGlobalConfigLogDroppedPacketInfo,
       "hwGTSMConformance": hwGTSMConformance,
       "hwGTSMCompliances": hwGTSMCompliances,
       "hwGTSMCompliance": hwGTSMCompliance,
       "hwGTSMGroups": hwGTSMGroups,
       "hwGTSMDefaultActionGroup": hwGTSMDefaultActionGroup,
       "hwGTSMPolicyGroup": hwGTSMPolicyGroup,
       "hwGTSMBgpPeergroupGroup": hwGTSMBgpPeergroupGroup,
       "hwGTSMStatisticsGroup": hwGTSMStatisticsGroup,
       "hwGTSMGlobalConfigGroup": hwGTSMGlobalConfigGroup,
       "hwGTSMStatisticsInfoGroup": hwGTSMStatisticsInfoGroup,
       "hwGTSMGlobalConfigInfoGroup": hwGTSMGlobalConfigInfoGroup}
)
