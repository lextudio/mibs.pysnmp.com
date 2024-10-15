# SNMP MIB module (HUAWEI-RBRP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-RBRP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:05:42 2024
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
 MacAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

hwRBRPMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 117)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class EnabledStatus(Integer32, TextualConvention):
    status = "current"
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



# MIB Managed Objects in the order of their OIDs

_HwRBRPMibObject_ObjectIdentity = ObjectIdentity
hwRBRPMibObject = _HwRBRPMibObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 117, 1)
)
_HwRBRPLocalDeviceID_Type = IpAddress
_HwRBRPLocalDeviceID_Object = MibScalar
hwRBRPLocalDeviceID = _HwRBRPLocalDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 117, 1, 1),
    _HwRBRPLocalDeviceID_Type()
)
hwRBRPLocalDeviceID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRBRPLocalDeviceID.setStatus("current")
_HwRBRPWrapToNormalTable_Object = MibTable
hwRBRPWrapToNormalTable = _HwRBRPWrapToNormalTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 117, 1, 2)
)
if mibBuilder.loadTexts:
    hwRBRPWrapToNormalTable.setStatus("current")
_HwRBRPWrapToNormalEntry_Object = MibTableRow
hwRBRPWrapToNormalEntry = _HwRBRPWrapToNormalEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 117, 1, 2, 1)
)
hwRBRPWrapToNormalEntry.setIndexNames(
    (0, "HUAWEI-RBRP-MIB", "hwRBRPRingIfIndex"),
)
if mibBuilder.loadTexts:
    hwRBRPWrapToNormalEntry.setStatus("current")
_HwRBRPRingIfIndex_Type = InterfaceIndex
_HwRBRPRingIfIndex_Object = MibTableColumn
hwRBRPRingIfIndex = _HwRBRPRingIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 117, 1, 2, 1, 1),
    _HwRBRPRingIfIndex_Type()
)
hwRBRPRingIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwRBRPRingIfIndex.setStatus("current")


class _HwRBRPWrapToNormalVal_Type(Integer32):
    """Custom type hwRBRPWrapToNormalVal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HwRBRPWrapToNormalVal_Type.__name__ = "Integer32"
_HwRBRPWrapToNormalVal_Object = MibTableColumn
hwRBRPWrapToNormalVal = _HwRBRPWrapToNormalVal_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 117, 1, 2, 1, 11),
    _HwRBRPWrapToNormalVal_Type()
)
hwRBRPWrapToNormalVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRBRPWrapToNormalVal.setStatus("current")
_HwRBRPGroupCfgTable_Object = MibTable
hwRBRPGroupCfgTable = _HwRBRPGroupCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 117, 1, 3)
)
if mibBuilder.loadTexts:
    hwRBRPGroupCfgTable.setStatus("current")
_HwRBRPGroupCfgEntry_Object = MibTableRow
hwRBRPGroupCfgEntry = _HwRBRPGroupCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 117, 1, 3, 1)
)
hwRBRPGroupCfgEntry.setIndexNames(
    (0, "HUAWEI-RBRP-MIB", "hwRBRPGroupCfgGroupID"),
)
if mibBuilder.loadTexts:
    hwRBRPGroupCfgEntry.setStatus("current")


class _HwRBRPGroupCfgGroupID_Type(Integer32):
    """Custom type hwRBRPGroupCfgGroupID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_HwRBRPGroupCfgGroupID_Type.__name__ = "Integer32"
_HwRBRPGroupCfgGroupID_Object = MibTableColumn
hwRBRPGroupCfgGroupID = _HwRBRPGroupCfgGroupID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 117, 1, 3, 1, 1),
    _HwRBRPGroupCfgGroupID_Type()
)
hwRBRPGroupCfgGroupID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwRBRPGroupCfgGroupID.setStatus("current")


class _HwRBRPPriorityValue_Type(Integer32):
    """Custom type hwRBRPPriorityValue based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HwRBRPPriorityValue_Type.__name__ = "Integer32"
_HwRBRPPriorityValue_Object = MibTableColumn
hwRBRPPriorityValue = _HwRBRPPriorityValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 117, 1, 3, 1, 11),
    _HwRBRPPriorityValue_Type()
)
hwRBRPPriorityValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRBRPPriorityValue.setStatus("current")


class _HwRBRPPreemptedEnable_Type(EnabledStatus):
    """Custom type hwRBRPPreemptedEnable based on EnabledStatus"""


_HwRBRPPreemptedEnable_Object = MibTableColumn
hwRBRPPreemptedEnable = _HwRBRPPreemptedEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 117, 1, 3, 1, 12),
    _HwRBRPPreemptedEnable_Type()
)
hwRBRPPreemptedEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRBRPPreemptedEnable.setStatus("current")


class _HwRBRPStatePromptSwitchEnable_Type(EnabledStatus):
    """Custom type hwRBRPStatePromptSwitchEnable based on EnabledStatus"""


_HwRBRPStatePromptSwitchEnable_Object = MibTableColumn
hwRBRPStatePromptSwitchEnable = _HwRBRPStatePromptSwitchEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 117, 1, 3, 1, 13),
    _HwRBRPStatePromptSwitchEnable_Type()
)
hwRBRPStatePromptSwitchEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRBRPStatePromptSwitchEnable.setStatus("current")


class _HwRBRPPreemptDelayValue_Type(Integer32):
    """Custom type hwRBRPPreemptDelayValue based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 1200),
    )


_HwRBRPPreemptDelayValue_Type.__name__ = "Integer32"
_HwRBRPPreemptDelayValue_Object = MibTableColumn
hwRBRPPreemptDelayValue = _HwRBRPPreemptDelayValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 117, 1, 3, 1, 14),
    _HwRBRPPreemptDelayValue_Type()
)
hwRBRPPreemptDelayValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRBRPPreemptDelayValue.setStatus("current")
_HwRBRPGroupCfgRowStatus_Type = RowStatus
_HwRBRPGroupCfgRowStatus_Object = MibTableColumn
hwRBRPGroupCfgRowStatus = _HwRBRPGroupCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 117, 1, 3, 1, 51),
    _HwRBRPGroupCfgRowStatus_Type()
)
hwRBRPGroupCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRBRPGroupCfgRowStatus.setStatus("current")
_HwRBRPPGRingIfCfgTable_Object = MibTable
hwRBRPPGRingIfCfgTable = _HwRBRPPGRingIfCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 117, 1, 4)
)
if mibBuilder.loadTexts:
    hwRBRPPGRingIfCfgTable.setStatus("current")
_HwRBRPPGRingIfCfgEntry_Object = MibTableRow
hwRBRPPGRingIfCfgEntry = _HwRBRPPGRingIfCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 117, 1, 4, 1)
)
hwRBRPPGRingIfCfgEntry.setIndexNames(
    (0, "HUAWEI-RBRP-MIB", "hwRBRPPGGroupID"),
    (0, "HUAWEI-RBRP-MIB", "hwRBRPRingType"),
)
if mibBuilder.loadTexts:
    hwRBRPPGRingIfCfgEntry.setStatus("current")


class _HwRBRPPGGroupID_Type(Integer32):
    """Custom type hwRBRPPGGroupID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_HwRBRPPGGroupID_Type.__name__ = "Integer32"
_HwRBRPPGGroupID_Object = MibTableColumn
hwRBRPPGGroupID = _HwRBRPPGGroupID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 117, 1, 4, 1, 1),
    _HwRBRPPGGroupID_Type()
)
hwRBRPPGGroupID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwRBRPPGGroupID.setStatus("current")


class _HwRBRPRingType_Type(Integer32):
    """Custom type hwRBRPRingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_HwRBRPRingType_Type.__name__ = "Integer32"
_HwRBRPRingType_Object = MibTableColumn
hwRBRPRingType = _HwRBRPRingType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 117, 1, 4, 1, 2),
    _HwRBRPRingType_Type()
)
hwRBRPRingType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwRBRPRingType.setStatus("current")
_HwRBRPRGRingIfIndex_Type = InterfaceIndex
_HwRBRPRGRingIfIndex_Object = MibTableColumn
hwRBRPRGRingIfIndex = _HwRBRPRGRingIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 117, 1, 4, 1, 11),
    _HwRBRPRGRingIfIndex_Type()
)
hwRBRPRGRingIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRBRPRGRingIfIndex.setStatus("current")
_HwRBRPGroupRowStatus_Type = RowStatus
_HwRBRPGroupRowStatus_Object = MibTableColumn
hwRBRPGroupRowStatus = _HwRBRPGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 117, 1, 4, 1, 51),
    _HwRBRPGroupRowStatus_Type()
)
hwRBRPGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRBRPGroupRowStatus.setStatus("current")
_HwRBRPPStatisTable_Object = MibTable
hwRBRPPStatisTable = _HwRBRPPStatisTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 117, 1, 5)
)
if mibBuilder.loadTexts:
    hwRBRPPStatisTable.setStatus("current")
_HwRBRPPStatisEntry_Object = MibTableRow
hwRBRPPStatisEntry = _HwRBRPPStatisEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 117, 1, 5, 1)
)
hwRBRPPStatisEntry.setIndexNames(
    (0, "HUAWEI-RBRP-MIB", "hwRBRPStatisGroupID"),
)
if mibBuilder.loadTexts:
    hwRBRPPStatisEntry.setStatus("current")


class _HwRBRPStatisGroupID_Type(Integer32):
    """Custom type hwRBRPStatisGroupID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_HwRBRPStatisGroupID_Type.__name__ = "Integer32"
_HwRBRPStatisGroupID_Object = MibTableColumn
hwRBRPStatisGroupID = _HwRBRPStatisGroupID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 117, 1, 5, 1, 1),
    _HwRBRPStatisGroupID_Type()
)
hwRBRPStatisGroupID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwRBRPStatisGroupID.setStatus("current")
_HwRBRPStatisRevPacketsNum_Type = Counter32
_HwRBRPStatisRevPacketsNum_Object = MibTableColumn
hwRBRPStatisRevPacketsNum = _HwRBRPStatisRevPacketsNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 117, 1, 5, 1, 11),
    _HwRBRPStatisRevPacketsNum_Type()
)
hwRBRPStatisRevPacketsNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRBRPStatisRevPacketsNum.setStatus("current")
_HwRBRPStatisRevByteNum_Type = Counter32
_HwRBRPStatisRevByteNum_Object = MibTableColumn
hwRBRPStatisRevByteNum = _HwRBRPStatisRevByteNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 117, 1, 5, 1, 12),
    _HwRBRPStatisRevByteNum_Type()
)
hwRBRPStatisRevByteNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRBRPStatisRevByteNum.setStatus("current")
_HwRBRPStatisSendPacketsNum_Type = Counter32
_HwRBRPStatisSendPacketsNum_Object = MibTableColumn
hwRBRPStatisSendPacketsNum = _HwRBRPStatisSendPacketsNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 117, 1, 5, 1, 13),
    _HwRBRPStatisSendPacketsNum_Type()
)
hwRBRPStatisSendPacketsNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRBRPStatisSendPacketsNum.setStatus("current")
_HwRBRPStatisSendByteNum_Type = Counter32
_HwRBRPStatisSendByteNum_Object = MibTableColumn
hwRBRPStatisSendByteNum = _HwRBRPStatisSendByteNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 117, 1, 5, 1, 14),
    _HwRBRPStatisSendByteNum_Type()
)
hwRBRPStatisSendByteNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRBRPStatisSendByteNum.setStatus("current")
_HwRBRPClearStatisticPacket_Type = EnabledStatus
_HwRBRPClearStatisticPacket_Object = MibTableColumn
hwRBRPClearStatisticPacket = _HwRBRPClearStatisticPacket_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 117, 1, 5, 1, 15),
    _HwRBRPClearStatisticPacket_Type()
)
hwRBRPClearStatisticPacket.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRBRPClearStatisticPacket.setStatus("current")
_HwRBRPGroupInfoTable_Object = MibTable
hwRBRPGroupInfoTable = _HwRBRPGroupInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 117, 1, 6)
)
if mibBuilder.loadTexts:
    hwRBRPGroupInfoTable.setStatus("current")
_HwRBRPGroupInfoEntry_Object = MibTableRow
hwRBRPGroupInfoEntry = _HwRBRPGroupInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 117, 1, 6, 1)
)
hwRBRPGroupInfoEntry.setIndexNames(
    (0, "HUAWEI-RBRP-MIB", "hwRBRPGroupID"),
    (0, "HUAWEI-RBRP-MIB", "hwRBRPDeviceId"),
)
if mibBuilder.loadTexts:
    hwRBRPGroupInfoEntry.setStatus("current")


class _HwRBRPGroupID_Type(Integer32):
    """Custom type hwRBRPGroupID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_HwRBRPGroupID_Type.__name__ = "Integer32"
_HwRBRPGroupID_Object = MibTableColumn
hwRBRPGroupID = _HwRBRPGroupID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 117, 1, 6, 1, 1),
    _HwRBRPGroupID_Type()
)
hwRBRPGroupID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwRBRPGroupID.setStatus("current")
_HwRBRPDeviceId_Type = IpAddress
_HwRBRPDeviceId_Object = MibTableColumn
hwRBRPDeviceId = _HwRBRPDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 117, 1, 6, 1, 2),
    _HwRBRPDeviceId_Type()
)
hwRBRPDeviceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwRBRPDeviceId.setStatus("current")
_HwRBRPPrimaryRPRMacAddress_Type = MacAddress
_HwRBRPPrimaryRPRMacAddress_Object = MibTableColumn
hwRBRPPrimaryRPRMacAddress = _HwRBRPPrimaryRPRMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 117, 1, 6, 1, 11),
    _HwRBRPPrimaryRPRMacAddress_Type()
)
hwRBRPPrimaryRPRMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRBRPPrimaryRPRMacAddress.setStatus("current")
_HwRBRPSecondaryRPRMacAddress_Type = MacAddress
_HwRBRPSecondaryRPRMacAddress_Object = MibTableColumn
hwRBRPSecondaryRPRMacAddress = _HwRBRPSecondaryRPRMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 117, 1, 6, 1, 12),
    _HwRBRPSecondaryRPRMacAddress_Type()
)
hwRBRPSecondaryRPRMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRBRPSecondaryRPRMacAddress.setStatus("current")


class _HwRBRPPriority_Type(Integer32):
    """Custom type hwRBRPPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HwRBRPPriority_Type.__name__ = "Integer32"
_HwRBRPPriority_Object = MibTableColumn
hwRBRPPriority = _HwRBRPPriority_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 117, 1, 6, 1, 13),
    _HwRBRPPriority_Type()
)
hwRBRPPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRBRPPriority.setStatus("current")


class _HwRBRPCurrentStatus_Type(Integer32):
    """Custom type hwRBRPCurrentStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_HwRBRPCurrentStatus_Type.__name__ = "Integer32"
_HwRBRPCurrentStatus_Object = MibTableColumn
hwRBRPCurrentStatus = _HwRBRPCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 117, 1, 6, 1, 14),
    _HwRBRPCurrentStatus_Type()
)
hwRBRPCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRBRPCurrentStatus.setStatus("current")
_HwRBRPTraps_ObjectIdentity = ObjectIdentity
hwRBRPTraps = _HwRBRPTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 117, 2)
)
_HwRBRPConformance_ObjectIdentity = ObjectIdentity
hwRBRPConformance = _HwRBRPConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 117, 3)
)
_HwRBRPGroups_ObjectIdentity = ObjectIdentity
hwRBRPGroups = _HwRBRPGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 117, 3, 1)
)

# Managed Objects groups

hwRBRPLoclaDeveceIDGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 117, 3, 1, 1)
)
hwRBRPLoclaDeveceIDGroup.setObjects(
    ("HUAWEI-RBRP-MIB", "hwRBRPLocalDeviceID")
)
if mibBuilder.loadTexts:
    hwRBRPLoclaDeveceIDGroup.setStatus("current")

hwRBRPWrapToNormalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 117, 3, 1, 2)
)
hwRBRPWrapToNormalGroup.setObjects(
    ("HUAWEI-RBRP-MIB", "hwRBRPWrapToNormalVal")
)
if mibBuilder.loadTexts:
    hwRBRPWrapToNormalGroup.setStatus("current")

hwRBRPGroupCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 117, 3, 1, 3)
)
hwRBRPGroupCfgGroup.setObjects(
      *(("HUAWEI-RBRP-MIB", "hwRBRPPriorityValue"),
        ("HUAWEI-RBRP-MIB", "hwRBRPPreemptDelayValue"),
        ("HUAWEI-RBRP-MIB", "hwRBRPGroupCfgRowStatus"),
        ("HUAWEI-RBRP-MIB", "hwRBRPStatePromptSwitchEnable"),
        ("HUAWEI-RBRP-MIB", "hwRBRPPreemptedEnable"))
)
if mibBuilder.loadTexts:
    hwRBRPGroupCfgGroup.setStatus("current")

hwRBRPPGRingIfCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 117, 3, 1, 4)
)
hwRBRPPGRingIfCfgGroup.setObjects(
      *(("HUAWEI-RBRP-MIB", "hwRBRPRGRingIfIndex"),
        ("HUAWEI-RBRP-MIB", "hwRBRPGroupRowStatus"))
)
if mibBuilder.loadTexts:
    hwRBRPPGRingIfCfgGroup.setStatus("current")

hwRBRPPStatisGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 117, 3, 1, 5)
)
hwRBRPPStatisGroup.setObjects(
      *(("HUAWEI-RBRP-MIB", "hwRBRPStatisRevPacketsNum"),
        ("HUAWEI-RBRP-MIB", "hwRBRPStatisRevByteNum"),
        ("HUAWEI-RBRP-MIB", "hwRBRPStatisSendPacketsNum"),
        ("HUAWEI-RBRP-MIB", "hwRBRPStatisSendByteNum"),
        ("HUAWEI-RBRP-MIB", "hwRBRPClearStatisticPacket"))
)
if mibBuilder.loadTexts:
    hwRBRPPStatisGroup.setStatus("current")

hwRBRPGroupInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 117, 3, 1, 6)
)
hwRBRPGroupInfoGroup.setObjects(
      *(("HUAWEI-RBRP-MIB", "hwRBRPCurrentStatus"),
        ("HUAWEI-RBRP-MIB", "hwRBRPPriority"),
        ("HUAWEI-RBRP-MIB", "hwRBRPSecondaryRPRMacAddress"),
        ("HUAWEI-RBRP-MIB", "hwRBRPPrimaryRPRMacAddress"))
)
if mibBuilder.loadTexts:
    hwRBRPGroupInfoGroup.setStatus("current")


# Notification objects

hwRBRPDeviceIDConflict = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 117, 2, 1)
)
hwRBRPDeviceIDConflict.setObjects(
    ("HUAWEI-RBRP-MIB", "hwRBRPCurrentStatus")
)
if mibBuilder.loadTexts:
    hwRBRPDeviceIDConflict.setStatus(
        "current"
    )

hwRBRPUnreadyStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 117, 2, 2)
)
hwRBRPUnreadyStatus.setObjects(
    ("HUAWEI-RBRP-MIB", "hwRBRPPreemptedEnable")
)
if mibBuilder.loadTexts:
    hwRBRPUnreadyStatus.setStatus(
        "current"
    )

hwRBRPClearUnreadyStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 117, 2, 3)
)
hwRBRPClearUnreadyStatus.setObjects(
    ("HUAWEI-RBRP-MIB", "hwRBRPPreemptedEnable")
)
if mibBuilder.loadTexts:
    hwRBRPClearUnreadyStatus.setStatus(
        "current"
    )


# Notifications groups

hwRBRPTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 117, 3, 1, 7)
)
hwRBRPTrapGroup.setObjects(
      *(("HUAWEI-RBRP-MIB", "hwRBRPClearUnreadyStatus"),
        ("HUAWEI-RBRP-MIB", "hwRBRPDeviceIDConflict"),
        ("HUAWEI-RBRP-MIB", "hwRBRPUnreadyStatus"))
)
if mibBuilder.loadTexts:
    hwRBRPTrapGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-RBRP-MIB",
    **{"EnabledStatus": EnabledStatus,
       "hwRBRPMIB": hwRBRPMIB,
       "hwRBRPMibObject": hwRBRPMibObject,
       "hwRBRPLocalDeviceID": hwRBRPLocalDeviceID,
       "hwRBRPWrapToNormalTable": hwRBRPWrapToNormalTable,
       "hwRBRPWrapToNormalEntry": hwRBRPWrapToNormalEntry,
       "hwRBRPRingIfIndex": hwRBRPRingIfIndex,
       "hwRBRPWrapToNormalVal": hwRBRPWrapToNormalVal,
       "hwRBRPGroupCfgTable": hwRBRPGroupCfgTable,
       "hwRBRPGroupCfgEntry": hwRBRPGroupCfgEntry,
       "hwRBRPGroupCfgGroupID": hwRBRPGroupCfgGroupID,
       "hwRBRPPriorityValue": hwRBRPPriorityValue,
       "hwRBRPPreemptedEnable": hwRBRPPreemptedEnable,
       "hwRBRPStatePromptSwitchEnable": hwRBRPStatePromptSwitchEnable,
       "hwRBRPPreemptDelayValue": hwRBRPPreemptDelayValue,
       "hwRBRPGroupCfgRowStatus": hwRBRPGroupCfgRowStatus,
       "hwRBRPPGRingIfCfgTable": hwRBRPPGRingIfCfgTable,
       "hwRBRPPGRingIfCfgEntry": hwRBRPPGRingIfCfgEntry,
       "hwRBRPPGGroupID": hwRBRPPGGroupID,
       "hwRBRPRingType": hwRBRPRingType,
       "hwRBRPRGRingIfIndex": hwRBRPRGRingIfIndex,
       "hwRBRPGroupRowStatus": hwRBRPGroupRowStatus,
       "hwRBRPPStatisTable": hwRBRPPStatisTable,
       "hwRBRPPStatisEntry": hwRBRPPStatisEntry,
       "hwRBRPStatisGroupID": hwRBRPStatisGroupID,
       "hwRBRPStatisRevPacketsNum": hwRBRPStatisRevPacketsNum,
       "hwRBRPStatisRevByteNum": hwRBRPStatisRevByteNum,
       "hwRBRPStatisSendPacketsNum": hwRBRPStatisSendPacketsNum,
       "hwRBRPStatisSendByteNum": hwRBRPStatisSendByteNum,
       "hwRBRPClearStatisticPacket": hwRBRPClearStatisticPacket,
       "hwRBRPGroupInfoTable": hwRBRPGroupInfoTable,
       "hwRBRPGroupInfoEntry": hwRBRPGroupInfoEntry,
       "hwRBRPGroupID": hwRBRPGroupID,
       "hwRBRPDeviceId": hwRBRPDeviceId,
       "hwRBRPPrimaryRPRMacAddress": hwRBRPPrimaryRPRMacAddress,
       "hwRBRPSecondaryRPRMacAddress": hwRBRPSecondaryRPRMacAddress,
       "hwRBRPPriority": hwRBRPPriority,
       "hwRBRPCurrentStatus": hwRBRPCurrentStatus,
       "hwRBRPTraps": hwRBRPTraps,
       "hwRBRPDeviceIDConflict": hwRBRPDeviceIDConflict,
       "hwRBRPUnreadyStatus": hwRBRPUnreadyStatus,
       "hwRBRPClearUnreadyStatus": hwRBRPClearUnreadyStatus,
       "hwRBRPConformance": hwRBRPConformance,
       "hwRBRPGroups": hwRBRPGroups,
       "hwRBRPLoclaDeveceIDGroup": hwRBRPLoclaDeveceIDGroup,
       "hwRBRPWrapToNormalGroup": hwRBRPWrapToNormalGroup,
       "hwRBRPGroupCfgGroup": hwRBRPGroupCfgGroup,
       "hwRBRPPGRingIfCfgGroup": hwRBRPPGRingIfCfgGroup,
       "hwRBRPPStatisGroup": hwRBRPPStatisGroup,
       "hwRBRPGroupInfoGroup": hwRBRPGroupInfoGroup,
       "hwRBRPTrapGroup": hwRBRPTrapGroup}
)
