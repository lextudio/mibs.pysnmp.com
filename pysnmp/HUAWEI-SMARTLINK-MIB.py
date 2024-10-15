# SNMP MIB module (HUAWEI-SMARTLINK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-SMARTLINK-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:05:57 2024
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

(MacAddress,) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "MacAddress")

(hwDatacomm,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "hwDatacomm")

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

(VlanIdOrNone,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanIdOrNone")

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

(DateAndTime,
 DisplayString,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

hwSmartLinkMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwL2Mgmt_ObjectIdentity = ObjectIdentity
hwL2Mgmt = _HwL2Mgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42)
)
_HwSmartLinkMibObjects_ObjectIdentity = ObjectIdentity
hwSmartLinkMibObjects = _HwSmartLinkMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 1)
)
_HwSmartLinkRevFlushTotal_Type = Counter32
_HwSmartLinkRevFlushTotal_Object = MibScalar
hwSmartLinkRevFlushTotal = _HwSmartLinkRevFlushTotal_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 1, 1),
    _HwSmartLinkRevFlushTotal_Type()
)
hwSmartLinkRevFlushTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSmartLinkRevFlushTotal.setStatus("current")
_HwSmartLinkRevLastFlushIfIndex_Type = InterfaceIndexOrZero
_HwSmartLinkRevLastFlushIfIndex_Object = MibScalar
hwSmartLinkRevLastFlushIfIndex = _HwSmartLinkRevLastFlushIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 1, 2),
    _HwSmartLinkRevLastFlushIfIndex_Type()
)
hwSmartLinkRevLastFlushIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSmartLinkRevLastFlushIfIndex.setStatus("current")


class _HwSmartLinkRevLastFlushTime_Type(DateAndTime):
    """Custom type hwSmartLinkRevLastFlushTime based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_HwSmartLinkRevLastFlushTime_Type.__name__ = "DateAndTime"
_HwSmartLinkRevLastFlushTime_Object = MibScalar
hwSmartLinkRevLastFlushTime = _HwSmartLinkRevLastFlushTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 1, 3),
    _HwSmartLinkRevLastFlushTime_Type()
)
hwSmartLinkRevLastFlushTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSmartLinkRevLastFlushTime.setStatus("current")
_HwSmartLinkRevLastFlushSourceMacAddr_Type = MacAddress
_HwSmartLinkRevLastFlushSourceMacAddr_Object = MibScalar
hwSmartLinkRevLastFlushSourceMacAddr = _HwSmartLinkRevLastFlushSourceMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 1, 4),
    _HwSmartLinkRevLastFlushSourceMacAddr_Type()
)
hwSmartLinkRevLastFlushSourceMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSmartLinkRevLastFlushSourceMacAddr.setStatus("current")
_HwSmartLinkRevLastFlushVlan_Type = VlanIdOrNone
_HwSmartLinkRevLastFlushVlan_Object = MibScalar
hwSmartLinkRevLastFlushVlan = _HwSmartLinkRevLastFlushVlan_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 1, 5),
    _HwSmartLinkRevLastFlushVlan_Type()
)
hwSmartLinkRevLastFlushVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSmartLinkRevLastFlushVlan.setStatus("current")


class _HwSmartLinkResetFlushStatistics_Type(Integer32):
    """Custom type hwSmartLinkResetFlushStatistics based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cleared", 1),
          ("unused", 2))
    )


_HwSmartLinkResetFlushStatistics_Type.__name__ = "Integer32"
_HwSmartLinkResetFlushStatistics_Object = MibScalar
hwSmartLinkResetFlushStatistics = _HwSmartLinkResetFlushStatistics_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 1, 6),
    _HwSmartLinkResetFlushStatistics_Type()
)
hwSmartLinkResetFlushStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSmartLinkResetFlushStatistics.setStatus("current")
_HwSmartLinkRevPortCfgTable_Object = MibTable
hwSmartLinkRevPortCfgTable = _HwSmartLinkRevPortCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 1, 7)
)
if mibBuilder.loadTexts:
    hwSmartLinkRevPortCfgTable.setStatus("current")
_HwSmartLinkRevPortCfgEntry_Object = MibTableRow
hwSmartLinkRevPortCfgEntry = _HwSmartLinkRevPortCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 1, 7, 1)
)
hwSmartLinkRevPortCfgEntry.setIndexNames(
    (0, "HUAWEI-SMARTLINK-MIB", "hwSmartLinkRpcIfIndex"),
)
if mibBuilder.loadTexts:
    hwSmartLinkRevPortCfgEntry.setStatus("current")
_HwSmartLinkRpcIfIndex_Type = InterfaceIndex
_HwSmartLinkRpcIfIndex_Object = MibTableColumn
hwSmartLinkRpcIfIndex = _HwSmartLinkRpcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 1, 7, 1, 1),
    _HwSmartLinkRpcIfIndex_Type()
)
hwSmartLinkRpcIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwSmartLinkRpcIfIndex.setStatus("current")
_HwSmartLinkRpcRevVlan_Type = VlanIdOrNone
_HwSmartLinkRpcRevVlan_Object = MibTableColumn
hwSmartLinkRpcRevVlan = _HwSmartLinkRpcRevVlan_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 1, 7, 1, 2),
    _HwSmartLinkRpcRevVlan_Type()
)
hwSmartLinkRpcRevVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSmartLinkRpcRevVlan.setStatus("current")


class _HwSmartLinkRpcRevPassword_Type(OctetString):
    """Custom type hwSmartLinkRpcRevPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_HwSmartLinkRpcRevPassword_Type.__name__ = "OctetString"
_HwSmartLinkRpcRevPassword_Object = MibTableColumn
hwSmartLinkRpcRevPassword = _HwSmartLinkRpcRevPassword_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 1, 7, 1, 3),
    _HwSmartLinkRpcRevPassword_Type()
)
hwSmartLinkRpcRevPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSmartLinkRpcRevPassword.setStatus("current")
_HwSmartLinkGroupCfgTable_Object = MibTable
hwSmartLinkGroupCfgTable = _HwSmartLinkGroupCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 1, 8)
)
if mibBuilder.loadTexts:
    hwSmartLinkGroupCfgTable.setStatus("current")
_HwSmartLinkGroupCfgEntry_Object = MibTableRow
hwSmartLinkGroupCfgEntry = _HwSmartLinkGroupCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 1, 8, 1)
)
hwSmartLinkGroupCfgEntry.setIndexNames(
    (0, "HUAWEI-SMARTLINK-MIB", "hwSmartLinkGcGroupId"),
)
if mibBuilder.loadTexts:
    hwSmartLinkGroupCfgEntry.setStatus("current")


class _HwSmartLinkGcGroupId_Type(Integer32):
    """Custom type hwSmartLinkGcGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_HwSmartLinkGcGroupId_Type.__name__ = "Integer32"
_HwSmartLinkGcGroupId_Object = MibTableColumn
hwSmartLinkGcGroupId = _HwSmartLinkGcGroupId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 1, 8, 1, 1),
    _HwSmartLinkGcGroupId_Type()
)
hwSmartLinkGcGroupId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwSmartLinkGcGroupId.setStatus("current")
_HwSmartLinkGcMasterIfIndex_Type = InterfaceIndexOrZero
_HwSmartLinkGcMasterIfIndex_Object = MibTableColumn
hwSmartLinkGcMasterIfIndex = _HwSmartLinkGcMasterIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 1, 8, 1, 2),
    _HwSmartLinkGcMasterIfIndex_Type()
)
hwSmartLinkGcMasterIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSmartLinkGcMasterIfIndex.setStatus("current")
_HwSmartLinkGcSlaveIfIndex_Type = InterfaceIndexOrZero
_HwSmartLinkGcSlaveIfIndex_Object = MibTableColumn
hwSmartLinkGcSlaveIfIndex = _HwSmartLinkGcSlaveIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 1, 8, 1, 3),
    _HwSmartLinkGcSlaveIfIndex_Type()
)
hwSmartLinkGcSlaveIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSmartLinkGcSlaveIfIndex.setStatus("current")


class _HwSmartLinkGcGroupStatus_Type(Integer32):
    """Custom type hwSmartLinkGcGroupStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("master", 2),
          ("none", 1),
          ("slave", 3))
    )


_HwSmartLinkGcGroupStatus_Type.__name__ = "Integer32"
_HwSmartLinkGcGroupStatus_Object = MibTableColumn
hwSmartLinkGcGroupStatus = _HwSmartLinkGcGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 1, 8, 1, 4),
    _HwSmartLinkGcGroupStatus_Type()
)
hwSmartLinkGcGroupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSmartLinkGcGroupStatus.setStatus("current")
_HwSmartLinkGcEnable_Type = EnabledStatus
_HwSmartLinkGcEnable_Object = MibTableColumn
hwSmartLinkGcEnable = _HwSmartLinkGcEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 1, 8, 1, 5),
    _HwSmartLinkGcEnable_Type()
)
hwSmartLinkGcEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSmartLinkGcEnable.setStatus("current")
_HwSmartLinkGcSendControlVlan_Type = VlanIdOrNone
_HwSmartLinkGcSendControlVlan_Object = MibTableColumn
hwSmartLinkGcSendControlVlan = _HwSmartLinkGcSendControlVlan_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 1, 8, 1, 6),
    _HwSmartLinkGcSendControlVlan_Type()
)
hwSmartLinkGcSendControlVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSmartLinkGcSendControlVlan.setStatus("current")


class _HwSmartLinkGcSendPassword_Type(OctetString):
    """Custom type hwSmartLinkGcSendPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_HwSmartLinkGcSendPassword_Type.__name__ = "OctetString"
_HwSmartLinkGcSendPassword_Object = MibTableColumn
hwSmartLinkGcSendPassword = _HwSmartLinkGcSendPassword_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 1, 8, 1, 7),
    _HwSmartLinkGcSendPassword_Type()
)
hwSmartLinkGcSendPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSmartLinkGcSendPassword.setStatus("current")
_HwSmartLinkGcLock_Type = EnabledStatus
_HwSmartLinkGcLock_Object = MibTableColumn
hwSmartLinkGcLock = _HwSmartLinkGcLock_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 1, 8, 1, 8),
    _HwSmartLinkGcLock_Type()
)
hwSmartLinkGcLock.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSmartLinkGcLock.setStatus("current")
_HwSmartLinkGcForce_Type = EnabledStatus
_HwSmartLinkGcForce_Object = MibTableColumn
hwSmartLinkGcForce = _HwSmartLinkGcForce_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 1, 8, 1, 9),
    _HwSmartLinkGcForce_Type()
)
hwSmartLinkGcForce.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSmartLinkGcForce.setStatus("current")


class _HwSmartLinkGcRevertWtrTime_Type(Integer32):
    """Custom type hwSmartLinkGcRevertWtrTime based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 1200),
    )


_HwSmartLinkGcRevertWtrTime_Type.__name__ = "Integer32"
_HwSmartLinkGcRevertWtrTime_Object = MibTableColumn
hwSmartLinkGcRevertWtrTime = _HwSmartLinkGcRevertWtrTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 1, 8, 1, 10),
    _HwSmartLinkGcRevertWtrTime_Type()
)
hwSmartLinkGcRevertWtrTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSmartLinkGcRevertWtrTime.setStatus("current")
_HwSmartLinkGcRevertEnable_Type = EnabledStatus
_HwSmartLinkGcRevertEnable_Object = MibTableColumn
hwSmartLinkGcRevertEnable = _HwSmartLinkGcRevertEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 1, 8, 1, 11),
    _HwSmartLinkGcRevertEnable_Type()
)
hwSmartLinkGcRevertEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSmartLinkGcRevertEnable.setStatus("current")


class _HwSmartLinkGcManual_Type(Integer32):
    """Custom type hwSmartLinkGcManual based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("switch", 1),
          ("unused", 2))
    )


_HwSmartLinkGcManual_Type.__name__ = "Integer32"
_HwSmartLinkGcManual_Object = MibTableColumn
hwSmartLinkGcManual = _HwSmartLinkGcManual_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 1, 8, 1, 12),
    _HwSmartLinkGcManual_Type()
)
hwSmartLinkGcManual.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSmartLinkGcManual.setStatus("current")
_HwSmartLinkGcRowStatus_Type = RowStatus
_HwSmartLinkGcRowStatus_Object = MibTableColumn
hwSmartLinkGcRowStatus = _HwSmartLinkGcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 1, 8, 1, 13),
    _HwSmartLinkGcRowStatus_Type()
)
hwSmartLinkGcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSmartLinkGcRowStatus.setStatus("current")
_HwSmartLinkPortCfgTable_Object = MibTable
hwSmartLinkPortCfgTable = _HwSmartLinkPortCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 1, 9)
)
if mibBuilder.loadTexts:
    hwSmartLinkPortCfgTable.setStatus("current")
_HwSmartLinkPortCfgEntry_Object = MibTableRow
hwSmartLinkPortCfgEntry = _HwSmartLinkPortCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 1, 9, 1)
)
hwSmartLinkPortCfgEntry.setIndexNames(
    (0, "HUAWEI-SMARTLINK-MIB", "hwSmartLinkPcGroupId"),
    (0, "HUAWEI-SMARTLINK-MIB", "hwSmartLinkPcPortType"),
)
if mibBuilder.loadTexts:
    hwSmartLinkPortCfgEntry.setStatus("current")


class _HwSmartLinkPcGroupId_Type(Integer32):
    """Custom type hwSmartLinkPcGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_HwSmartLinkPcGroupId_Type.__name__ = "Integer32"
_HwSmartLinkPcGroupId_Object = MibTableColumn
hwSmartLinkPcGroupId = _HwSmartLinkPcGroupId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 1, 9, 1, 1),
    _HwSmartLinkPcGroupId_Type()
)
hwSmartLinkPcGroupId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwSmartLinkPcGroupId.setStatus("current")


class _HwSmartLinkPcPortType_Type(Integer32):
    """Custom type hwSmartLinkPcPortType based on Integer32"""
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


_HwSmartLinkPcPortType_Type.__name__ = "Integer32"
_HwSmartLinkPcPortType_Object = MibTableColumn
hwSmartLinkPcPortType = _HwSmartLinkPcPortType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 1, 9, 1, 2),
    _HwSmartLinkPcPortType_Type()
)
hwSmartLinkPcPortType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwSmartLinkPcPortType.setStatus("current")
_HwSmartLinkPcIfIndex_Type = InterfaceIndexOrZero
_HwSmartLinkPcIfIndex_Object = MibTableColumn
hwSmartLinkPcIfIndex = _HwSmartLinkPcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 1, 9, 1, 3),
    _HwSmartLinkPcIfIndex_Type()
)
hwSmartLinkPcIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSmartLinkPcIfIndex.setStatus("current")


class _HwSmartLinkPcPortStatus_Type(Integer32):
    """Custom type hwSmartLinkPcPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 3),
          ("unknown", 1))
    )


_HwSmartLinkPcPortStatus_Type.__name__ = "Integer32"
_HwSmartLinkPcPortStatus_Object = MibTableColumn
hwSmartLinkPcPortStatus = _HwSmartLinkPcPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 1, 9, 1, 4),
    _HwSmartLinkPcPortStatus_Type()
)
hwSmartLinkPcPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSmartLinkPcPortStatus.setStatus("current")
_HwSmartLinkPcSendFlushNum_Type = Counter32
_HwSmartLinkPcSendFlushNum_Object = MibTableColumn
hwSmartLinkPcSendFlushNum = _HwSmartLinkPcSendFlushNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 1, 9, 1, 5),
    _HwSmartLinkPcSendFlushNum_Type()
)
hwSmartLinkPcSendFlushNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSmartLinkPcSendFlushNum.setStatus("current")


class _HwSmartLinkPcSendFlushTime_Type(DateAndTime):
    """Custom type hwSmartLinkPcSendFlushTime based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_HwSmartLinkPcSendFlushTime_Type.__name__ = "DateAndTime"
_HwSmartLinkPcSendFlushTime_Object = MibTableColumn
hwSmartLinkPcSendFlushTime = _HwSmartLinkPcSendFlushTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 1, 9, 1, 6),
    _HwSmartLinkPcSendFlushTime_Type()
)
hwSmartLinkPcSendFlushTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSmartLinkPcSendFlushTime.setStatus("current")
_HwSmartLinkPcRowStatus_Type = RowStatus
_HwSmartLinkPcRowStatus_Object = MibTableColumn
hwSmartLinkPcRowStatus = _HwSmartLinkPcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 1, 9, 1, 7),
    _HwSmartLinkPcRowStatus_Type()
)
hwSmartLinkPcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSmartLinkPcRowStatus.setStatus("current")
_HwMonitorLinkGroupCfgTable_Object = MibTable
hwMonitorLinkGroupCfgTable = _HwMonitorLinkGroupCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 1, 10)
)
if mibBuilder.loadTexts:
    hwMonitorLinkGroupCfgTable.setStatus("current")
_HwMonitorLinkGroupCfgEntry_Object = MibTableRow
hwMonitorLinkGroupCfgEntry = _HwMonitorLinkGroupCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 1, 10, 1)
)
hwMonitorLinkGroupCfgEntry.setIndexNames(
    (0, "HUAWEI-SMARTLINK-MIB", "hwMonitorLinkGcGroupId"),
)
if mibBuilder.loadTexts:
    hwMonitorLinkGroupCfgEntry.setStatus("current")


class _HwMonitorLinkGcGroupId_Type(Integer32):
    """Custom type hwMonitorLinkGcGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_HwMonitorLinkGcGroupId_Type.__name__ = "Integer32"
_HwMonitorLinkGcGroupId_Object = MibTableColumn
hwMonitorLinkGcGroupId = _HwMonitorLinkGcGroupId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 1, 10, 1, 1),
    _HwMonitorLinkGcGroupId_Type()
)
hwMonitorLinkGcGroupId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMonitorLinkGcGroupId.setStatus("current")


class _HwMonitorLinkGcRecoverTime_Type(Integer32):
    """Custom type hwMonitorLinkGcRecoverTime based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 60),
    )


_HwMonitorLinkGcRecoverTime_Type.__name__ = "Integer32"
_HwMonitorLinkGcRecoverTime_Object = MibTableColumn
hwMonitorLinkGcRecoverTime = _HwMonitorLinkGcRecoverTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 1, 10, 1, 2),
    _HwMonitorLinkGcRecoverTime_Type()
)
hwMonitorLinkGcRecoverTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMonitorLinkGcRecoverTime.setStatus("current")
_HwMonitorLinkGcRowStatus_Type = RowStatus
_HwMonitorLinkGcRowStatus_Object = MibTableColumn
hwMonitorLinkGcRowStatus = _HwMonitorLinkGcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 1, 10, 1, 3),
    _HwMonitorLinkGcRowStatus_Type()
)
hwMonitorLinkGcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMonitorLinkGcRowStatus.setStatus("current")
_HwMonitorLinkUpLinkPortTable_Object = MibTable
hwMonitorLinkUpLinkPortTable = _HwMonitorLinkUpLinkPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 1, 11)
)
if mibBuilder.loadTexts:
    hwMonitorLinkUpLinkPortTable.setStatus("current")
_HwMonitorLinkUpLinkPortEntry_Object = MibTableRow
hwMonitorLinkUpLinkPortEntry = _HwMonitorLinkUpLinkPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 1, 11, 1)
)
hwMonitorLinkUpLinkPortEntry.setIndexNames(
    (0, "HUAWEI-SMARTLINK-MIB", "hwMonitorLinkUlGroupId"),
    (0, "HUAWEI-SMARTLINK-MIB", "hwMonitorLinkUlPortType"),
)
if mibBuilder.loadTexts:
    hwMonitorLinkUpLinkPortEntry.setStatus("current")


class _HwMonitorLinkUlGroupId_Type(Integer32):
    """Custom type hwMonitorLinkUlGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_HwMonitorLinkUlGroupId_Type.__name__ = "Integer32"
_HwMonitorLinkUlGroupId_Object = MibTableColumn
hwMonitorLinkUlGroupId = _HwMonitorLinkUlGroupId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 1, 11, 1, 1),
    _HwMonitorLinkUlGroupId_Type()
)
hwMonitorLinkUlGroupId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMonitorLinkUlGroupId.setStatus("current")


class _HwMonitorLinkUlPortType_Type(Integer32):
    """Custom type hwMonitorLinkUlPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("smartLink", 1),
          ("switchPort", 2))
    )


_HwMonitorLinkUlPortType_Type.__name__ = "Integer32"
_HwMonitorLinkUlPortType_Object = MibTableColumn
hwMonitorLinkUlPortType = _HwMonitorLinkUlPortType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 1, 11, 1, 2),
    _HwMonitorLinkUlPortType_Type()
)
hwMonitorLinkUlPortType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMonitorLinkUlPortType.setStatus("current")
_HwMonitorLinkUlPortValue_Type = Integer32
_HwMonitorLinkUlPortValue_Object = MibTableColumn
hwMonitorLinkUlPortValue = _HwMonitorLinkUlPortValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 1, 11, 1, 3),
    _HwMonitorLinkUlPortValue_Type()
)
hwMonitorLinkUlPortValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMonitorLinkUlPortValue.setStatus("current")


class _HwMonitorLinkUlPortStatus_Type(Integer32):
    """Custom type hwMonitorLinkUlPortStatus based on Integer32"""
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


_HwMonitorLinkUlPortStatus_Type.__name__ = "Integer32"
_HwMonitorLinkUlPortStatus_Object = MibTableColumn
hwMonitorLinkUlPortStatus = _HwMonitorLinkUlPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 1, 11, 1, 4),
    _HwMonitorLinkUlPortStatus_Type()
)
hwMonitorLinkUlPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMonitorLinkUlPortStatus.setStatus("current")


class _HwMonitorLinkUlPortUpTime_Type(DateAndTime):
    """Custom type hwMonitorLinkUlPortUpTime based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_HwMonitorLinkUlPortUpTime_Type.__name__ = "DateAndTime"
_HwMonitorLinkUlPortUpTime_Object = MibTableColumn
hwMonitorLinkUlPortUpTime = _HwMonitorLinkUlPortUpTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 1, 11, 1, 5),
    _HwMonitorLinkUlPortUpTime_Type()
)
hwMonitorLinkUlPortUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMonitorLinkUlPortUpTime.setStatus("current")


class _HwMonitorLinkUlPortDownTime_Type(DateAndTime):
    """Custom type hwMonitorLinkUlPortDownTime based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_HwMonitorLinkUlPortDownTime_Type.__name__ = "DateAndTime"
_HwMonitorLinkUlPortDownTime_Object = MibTableColumn
hwMonitorLinkUlPortDownTime = _HwMonitorLinkUlPortDownTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 1, 11, 1, 6),
    _HwMonitorLinkUlPortDownTime_Type()
)
hwMonitorLinkUlPortDownTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMonitorLinkUlPortDownTime.setStatus("current")
_HwMonitorLinkUlRowStatus_Type = RowStatus
_HwMonitorLinkUlRowStatus_Object = MibTableColumn
hwMonitorLinkUlRowStatus = _HwMonitorLinkUlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 1, 11, 1, 7),
    _HwMonitorLinkUlRowStatus_Type()
)
hwMonitorLinkUlRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMonitorLinkUlRowStatus.setStatus("current")
_HwMonitorLinkDownLinkPortTable_Object = MibTable
hwMonitorLinkDownLinkPortTable = _HwMonitorLinkDownLinkPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 1, 12)
)
if mibBuilder.loadTexts:
    hwMonitorLinkDownLinkPortTable.setStatus("current")
_HwMonitorLinkDownLinkPortEntry_Object = MibTableRow
hwMonitorLinkDownLinkPortEntry = _HwMonitorLinkDownLinkPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 1, 12, 1)
)
hwMonitorLinkDownLinkPortEntry.setIndexNames(
    (0, "HUAWEI-SMARTLINK-MIB", "hwMonitorLinkDlGroupId"),
    (0, "HUAWEI-SMARTLINK-MIB", "hwMonitorLinkDlArrayIndex"),
)
if mibBuilder.loadTexts:
    hwMonitorLinkDownLinkPortEntry.setStatus("current")


class _HwMonitorLinkDlGroupId_Type(Integer32):
    """Custom type hwMonitorLinkDlGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_HwMonitorLinkDlGroupId_Type.__name__ = "Integer32"
_HwMonitorLinkDlGroupId_Object = MibTableColumn
hwMonitorLinkDlGroupId = _HwMonitorLinkDlGroupId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 1, 12, 1, 1),
    _HwMonitorLinkDlGroupId_Type()
)
hwMonitorLinkDlGroupId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMonitorLinkDlGroupId.setStatus("current")


class _HwMonitorLinkDlArrayIndex_Type(Integer32):
    """Custom type hwMonitorLinkDlArrayIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_HwMonitorLinkDlArrayIndex_Type.__name__ = "Integer32"
_HwMonitorLinkDlArrayIndex_Object = MibTableColumn
hwMonitorLinkDlArrayIndex = _HwMonitorLinkDlArrayIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 1, 12, 1, 2),
    _HwMonitorLinkDlArrayIndex_Type()
)
hwMonitorLinkDlArrayIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMonitorLinkDlArrayIndex.setStatus("current")
_HwMonitorLinkDlIfIndex_Type = InterfaceIndexOrZero
_HwMonitorLinkDlIfIndex_Object = MibTableColumn
hwMonitorLinkDlIfIndex = _HwMonitorLinkDlIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 1, 12, 1, 3),
    _HwMonitorLinkDlIfIndex_Type()
)
hwMonitorLinkDlIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMonitorLinkDlIfIndex.setStatus("current")


class _HwMonitorLinkDlPortStatus_Type(Integer32):
    """Custom type hwMonitorLinkDlPortStatus based on Integer32"""
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


_HwMonitorLinkDlPortStatus_Type.__name__ = "Integer32"
_HwMonitorLinkDlPortStatus_Object = MibTableColumn
hwMonitorLinkDlPortStatus = _HwMonitorLinkDlPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 1, 12, 1, 4),
    _HwMonitorLinkDlPortStatus_Type()
)
hwMonitorLinkDlPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMonitorLinkDlPortStatus.setStatus("current")


class _HwMonitorLinkDlPortUpTime_Type(DateAndTime):
    """Custom type hwMonitorLinkDlPortUpTime based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_HwMonitorLinkDlPortUpTime_Type.__name__ = "DateAndTime"
_HwMonitorLinkDlPortUpTime_Object = MibTableColumn
hwMonitorLinkDlPortUpTime = _HwMonitorLinkDlPortUpTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 1, 12, 1, 5),
    _HwMonitorLinkDlPortUpTime_Type()
)
hwMonitorLinkDlPortUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMonitorLinkDlPortUpTime.setStatus("current")


class _HwMonitorLinkDlPortDownTime_Type(DateAndTime):
    """Custom type hwMonitorLinkDlPortDownTime based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_HwMonitorLinkDlPortDownTime_Type.__name__ = "DateAndTime"
_HwMonitorLinkDlPortDownTime_Object = MibTableColumn
hwMonitorLinkDlPortDownTime = _HwMonitorLinkDlPortDownTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 1, 12, 1, 6),
    _HwMonitorLinkDlPortDownTime_Type()
)
hwMonitorLinkDlPortDownTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMonitorLinkDlPortDownTime.setStatus("current")
_HwMonitorLinkDlRowStatus_Type = RowStatus
_HwMonitorLinkDlRowStatus_Object = MibTableColumn
hwMonitorLinkDlRowStatus = _HwMonitorLinkDlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 1, 12, 1, 7),
    _HwMonitorLinkDlRowStatus_Type()
)
hwMonitorLinkDlRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMonitorLinkDlRowStatus.setStatus("current")
_HwSmartLinkMibTraps_ObjectIdentity = ObjectIdentity
hwSmartLinkMibTraps = _HwSmartLinkMibTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 2)
)
if mibBuilder.loadTexts:
    hwSmartLinkMibTraps.setStatus("current")
_HwSmartLinkConformance_ObjectIdentity = ObjectIdentity
hwSmartLinkConformance = _HwSmartLinkConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 3)
)
_HwSmartLinkGroups_ObjectIdentity = ObjectIdentity
hwSmartLinkGroups = _HwSmartLinkGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 3, 1)
)
_HwSmartLinkTrapGroups_ObjectIdentity = ObjectIdentity
hwSmartLinkTrapGroups = _HwSmartLinkTrapGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 3, 2)
)
_HwSmartLinkCompliances_ObjectIdentity = ObjectIdentity
hwSmartLinkCompliances = _HwSmartLinkCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 3, 3)
)

# Managed Objects groups

hwSmartLinkInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 3, 1, 1)
)
hwSmartLinkInfoGroup.setObjects(
      *(("HUAWEI-SMARTLINK-MIB", "hwSmartLinkRevFlushTotal"),
        ("HUAWEI-SMARTLINK-MIB", "hwSmartLinkRevLastFlushIfIndex"),
        ("HUAWEI-SMARTLINK-MIB", "hwSmartLinkRevLastFlushTime"),
        ("HUAWEI-SMARTLINK-MIB", "hwSmartLinkRevLastFlushSourceMacAddr"),
        ("HUAWEI-SMARTLINK-MIB", "hwSmartLinkRevLastFlushVlan"),
        ("HUAWEI-SMARTLINK-MIB", "hwSmartLinkResetFlushStatistics"))
)
if mibBuilder.loadTexts:
    hwSmartLinkInfoGroup.setStatus("current")

hwSmartLinkRevPortCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 3, 1, 2)
)
hwSmartLinkRevPortCfgGroup.setObjects(
      *(("HUAWEI-SMARTLINK-MIB", "hwSmartLinkRpcRevVlan"),
        ("HUAWEI-SMARTLINK-MIB", "hwSmartLinkRpcRevPassword"))
)
if mibBuilder.loadTexts:
    hwSmartLinkRevPortCfgGroup.setStatus("current")

hwSmartLinkGroupCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 3, 1, 3)
)
hwSmartLinkGroupCfgGroup.setObjects(
      *(("HUAWEI-SMARTLINK-MIB", "hwSmartLinkGcMasterIfIndex"),
        ("HUAWEI-SMARTLINK-MIB", "hwSmartLinkGcSlaveIfIndex"),
        ("HUAWEI-SMARTLINK-MIB", "hwSmartLinkGcGroupStatus"),
        ("HUAWEI-SMARTLINK-MIB", "hwSmartLinkGcEnable"),
        ("HUAWEI-SMARTLINK-MIB", "hwSmartLinkGcSendControlVlan"),
        ("HUAWEI-SMARTLINK-MIB", "hwSmartLinkGcSendPassword"),
        ("HUAWEI-SMARTLINK-MIB", "hwSmartLinkGcLock"),
        ("HUAWEI-SMARTLINK-MIB", "hwSmartLinkGcForce"),
        ("HUAWEI-SMARTLINK-MIB", "hwSmartLinkGcRevertWtrTime"),
        ("HUAWEI-SMARTLINK-MIB", "hwSmartLinkGcRevertEnable"),
        ("HUAWEI-SMARTLINK-MIB", "hwSmartLinkGcManual"),
        ("HUAWEI-SMARTLINK-MIB", "hwSmartLinkGcRowStatus"))
)
if mibBuilder.loadTexts:
    hwSmartLinkGroupCfgGroup.setStatus("current")

hwSmartLinkPortCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 3, 1, 4)
)
hwSmartLinkPortCfgGroup.setObjects(
      *(("HUAWEI-SMARTLINK-MIB", "hwSmartLinkPcIfIndex"),
        ("HUAWEI-SMARTLINK-MIB", "hwSmartLinkPcPortStatus"),
        ("HUAWEI-SMARTLINK-MIB", "hwSmartLinkPcSendFlushNum"),
        ("HUAWEI-SMARTLINK-MIB", "hwSmartLinkPcSendFlushTime"),
        ("HUAWEI-SMARTLINK-MIB", "hwSmartLinkPcRowStatus"))
)
if mibBuilder.loadTexts:
    hwSmartLinkPortCfgGroup.setStatus("current")

hwMonitorLinkGroupCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 3, 1, 5)
)
hwMonitorLinkGroupCfgGroup.setObjects(
      *(("HUAWEI-SMARTLINK-MIB", "hwMonitorLinkGcRecoverTime"),
        ("HUAWEI-SMARTLINK-MIB", "hwMonitorLinkGcRowStatus"))
)
if mibBuilder.loadTexts:
    hwMonitorLinkGroupCfgGroup.setStatus("current")

hwMonitorLinkUpLinkPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 3, 1, 6)
)
hwMonitorLinkUpLinkPortGroup.setObjects(
      *(("HUAWEI-SMARTLINK-MIB", "hwMonitorLinkUlPortValue"),
        ("HUAWEI-SMARTLINK-MIB", "hwMonitorLinkUlPortStatus"),
        ("HUAWEI-SMARTLINK-MIB", "hwMonitorLinkUlPortUpTime"),
        ("HUAWEI-SMARTLINK-MIB", "hwMonitorLinkUlPortDownTime"),
        ("HUAWEI-SMARTLINK-MIB", "hwMonitorLinkUlRowStatus"))
)
if mibBuilder.loadTexts:
    hwMonitorLinkUpLinkPortGroup.setStatus("current")

hwMonitorLinkDownLinkPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 3, 1, 7)
)
hwMonitorLinkDownLinkPortGroup.setObjects(
      *(("HUAWEI-SMARTLINK-MIB", "hwMonitorLinkDlIfIndex"),
        ("HUAWEI-SMARTLINK-MIB", "hwMonitorLinkDlPortStatus"),
        ("HUAWEI-SMARTLINK-MIB", "hwMonitorLinkDlPortUpTime"),
        ("HUAWEI-SMARTLINK-MIB", "hwMonitorLinkDlPortDownTime"),
        ("HUAWEI-SMARTLINK-MIB", "hwMonitorLinkDlRowStatus"))
)
if mibBuilder.loadTexts:
    hwMonitorLinkDownLinkPortGroup.setStatus("current")


# Notification objects

hwSmartLinkLinkSwitch = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 2, 1)
)
hwSmartLinkLinkSwitch.setObjects(
    ("HUAWEI-SMARTLINK-MIB", "hwSmartLinkGcGroupStatus")
)
if mibBuilder.loadTexts:
    hwSmartLinkLinkSwitch.setStatus(
        "current"
    )

hwSmartLinkInactiveLinkFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 2, 2)
)
hwSmartLinkInactiveLinkFail.setObjects(
    ("HUAWEI-SMARTLINK-MIB", "hwSmartLinkPcIfIndex")
)
if mibBuilder.loadTexts:
    hwSmartLinkInactiveLinkFail.setStatus(
        "current"
    )

hwSmartLinkInactiveLinkResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 2, 3)
)
hwSmartLinkInactiveLinkResume.setObjects(
    ("HUAWEI-SMARTLINK-MIB", "hwSmartLinkPcIfIndex")
)
if mibBuilder.loadTexts:
    hwSmartLinkInactiveLinkResume.setStatus(
        "current"
    )

hwSmartLinkGroupEnable = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 2, 4)
)
hwSmartLinkGroupEnable.setObjects(
    ("HUAWEI-SMARTLINK-MIB", "hwSmartLinkGcEnable")
)
if mibBuilder.loadTexts:
    hwSmartLinkGroupEnable.setStatus(
        "current"
    )

hwSmartLinkGroupDisable = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 2, 5)
)
hwSmartLinkGroupDisable.setObjects(
    ("HUAWEI-SMARTLINK-MIB", "hwSmartLinkGcEnable")
)
if mibBuilder.loadTexts:
    hwSmartLinkGroupDisable.setStatus(
        "current"
    )

hwSmartLinkLinkSwitchToMaster = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 2, 6)
)
hwSmartLinkLinkSwitchToMaster.setObjects(
    ("HUAWEI-SMARTLINK-MIB", "hwSmartLinkGcGroupStatus")
)
if mibBuilder.loadTexts:
    hwSmartLinkLinkSwitchToMaster.setStatus(
        "current"
    )

hwSmartLinkLinkSwitchToSlave = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 2, 7)
)
hwSmartLinkLinkSwitchToSlave.setObjects(
    ("HUAWEI-SMARTLINK-MIB", "hwSmartLinkGcGroupStatus")
)
if mibBuilder.loadTexts:
    hwSmartLinkLinkSwitchToSlave.setStatus(
        "current"
    )

hwSmartLinkGroupUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 2, 8)
)
hwSmartLinkGroupUp.setObjects(
    ("HUAWEI-SMARTLINK-MIB", "hwSmartLinkGcGroupStatus")
)
if mibBuilder.loadTexts:
    hwSmartLinkGroupUp.setStatus(
        "current"
    )

hwSmartLinkGroupDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 2, 9)
)
hwSmartLinkGroupDown.setObjects(
    ("HUAWEI-SMARTLINK-MIB", "hwSmartLinkGcGroupStatus")
)
if mibBuilder.loadTexts:
    hwSmartLinkGroupDown.setStatus(
        "current"
    )


# Notifications groups

hwSmartLinkTrapsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 3, 2, 1)
)
hwSmartLinkTrapsGroup.setObjects(
      *(("HUAWEI-SMARTLINK-MIB", "hwSmartLinkLinkSwitch"),
        ("HUAWEI-SMARTLINK-MIB", "hwSmartLinkInactiveLinkFail"),
        ("HUAWEI-SMARTLINK-MIB", "hwSmartLinkInactiveLinkResume"),
        ("HUAWEI-SMARTLINK-MIB", "hwSmartLinkGroupEnable"),
        ("HUAWEI-SMARTLINK-MIB", "hwSmartLinkGroupDisable"),
        ("HUAWEI-SMARTLINK-MIB", "hwSmartLinkLinkSwitchToMaster"),
        ("HUAWEI-SMARTLINK-MIB", "hwSmartLinkLinkSwitchToSlave"),
        ("HUAWEI-SMARTLINK-MIB", "hwSmartLinkGroupUp"),
        ("HUAWEI-SMARTLINK-MIB", "hwSmartLinkGroupDown"))
)
if mibBuilder.loadTexts:
    hwSmartLinkTrapsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-SMARTLINK-MIB",
    **{"hwL2Mgmt": hwL2Mgmt,
       "hwSmartLinkMib": hwSmartLinkMib,
       "hwSmartLinkMibObjects": hwSmartLinkMibObjects,
       "hwSmartLinkRevFlushTotal": hwSmartLinkRevFlushTotal,
       "hwSmartLinkRevLastFlushIfIndex": hwSmartLinkRevLastFlushIfIndex,
       "hwSmartLinkRevLastFlushTime": hwSmartLinkRevLastFlushTime,
       "hwSmartLinkRevLastFlushSourceMacAddr": hwSmartLinkRevLastFlushSourceMacAddr,
       "hwSmartLinkRevLastFlushVlan": hwSmartLinkRevLastFlushVlan,
       "hwSmartLinkResetFlushStatistics": hwSmartLinkResetFlushStatistics,
       "hwSmartLinkRevPortCfgTable": hwSmartLinkRevPortCfgTable,
       "hwSmartLinkRevPortCfgEntry": hwSmartLinkRevPortCfgEntry,
       "hwSmartLinkRpcIfIndex": hwSmartLinkRpcIfIndex,
       "hwSmartLinkRpcRevVlan": hwSmartLinkRpcRevVlan,
       "hwSmartLinkRpcRevPassword": hwSmartLinkRpcRevPassword,
       "hwSmartLinkGroupCfgTable": hwSmartLinkGroupCfgTable,
       "hwSmartLinkGroupCfgEntry": hwSmartLinkGroupCfgEntry,
       "hwSmartLinkGcGroupId": hwSmartLinkGcGroupId,
       "hwSmartLinkGcMasterIfIndex": hwSmartLinkGcMasterIfIndex,
       "hwSmartLinkGcSlaveIfIndex": hwSmartLinkGcSlaveIfIndex,
       "hwSmartLinkGcGroupStatus": hwSmartLinkGcGroupStatus,
       "hwSmartLinkGcEnable": hwSmartLinkGcEnable,
       "hwSmartLinkGcSendControlVlan": hwSmartLinkGcSendControlVlan,
       "hwSmartLinkGcSendPassword": hwSmartLinkGcSendPassword,
       "hwSmartLinkGcLock": hwSmartLinkGcLock,
       "hwSmartLinkGcForce": hwSmartLinkGcForce,
       "hwSmartLinkGcRevertWtrTime": hwSmartLinkGcRevertWtrTime,
       "hwSmartLinkGcRevertEnable": hwSmartLinkGcRevertEnable,
       "hwSmartLinkGcManual": hwSmartLinkGcManual,
       "hwSmartLinkGcRowStatus": hwSmartLinkGcRowStatus,
       "hwSmartLinkPortCfgTable": hwSmartLinkPortCfgTable,
       "hwSmartLinkPortCfgEntry": hwSmartLinkPortCfgEntry,
       "hwSmartLinkPcGroupId": hwSmartLinkPcGroupId,
       "hwSmartLinkPcPortType": hwSmartLinkPcPortType,
       "hwSmartLinkPcIfIndex": hwSmartLinkPcIfIndex,
       "hwSmartLinkPcPortStatus": hwSmartLinkPcPortStatus,
       "hwSmartLinkPcSendFlushNum": hwSmartLinkPcSendFlushNum,
       "hwSmartLinkPcSendFlushTime": hwSmartLinkPcSendFlushTime,
       "hwSmartLinkPcRowStatus": hwSmartLinkPcRowStatus,
       "hwMonitorLinkGroupCfgTable": hwMonitorLinkGroupCfgTable,
       "hwMonitorLinkGroupCfgEntry": hwMonitorLinkGroupCfgEntry,
       "hwMonitorLinkGcGroupId": hwMonitorLinkGcGroupId,
       "hwMonitorLinkGcRecoverTime": hwMonitorLinkGcRecoverTime,
       "hwMonitorLinkGcRowStatus": hwMonitorLinkGcRowStatus,
       "hwMonitorLinkUpLinkPortTable": hwMonitorLinkUpLinkPortTable,
       "hwMonitorLinkUpLinkPortEntry": hwMonitorLinkUpLinkPortEntry,
       "hwMonitorLinkUlGroupId": hwMonitorLinkUlGroupId,
       "hwMonitorLinkUlPortType": hwMonitorLinkUlPortType,
       "hwMonitorLinkUlPortValue": hwMonitorLinkUlPortValue,
       "hwMonitorLinkUlPortStatus": hwMonitorLinkUlPortStatus,
       "hwMonitorLinkUlPortUpTime": hwMonitorLinkUlPortUpTime,
       "hwMonitorLinkUlPortDownTime": hwMonitorLinkUlPortDownTime,
       "hwMonitorLinkUlRowStatus": hwMonitorLinkUlRowStatus,
       "hwMonitorLinkDownLinkPortTable": hwMonitorLinkDownLinkPortTable,
       "hwMonitorLinkDownLinkPortEntry": hwMonitorLinkDownLinkPortEntry,
       "hwMonitorLinkDlGroupId": hwMonitorLinkDlGroupId,
       "hwMonitorLinkDlArrayIndex": hwMonitorLinkDlArrayIndex,
       "hwMonitorLinkDlIfIndex": hwMonitorLinkDlIfIndex,
       "hwMonitorLinkDlPortStatus": hwMonitorLinkDlPortStatus,
       "hwMonitorLinkDlPortUpTime": hwMonitorLinkDlPortUpTime,
       "hwMonitorLinkDlPortDownTime": hwMonitorLinkDlPortDownTime,
       "hwMonitorLinkDlRowStatus": hwMonitorLinkDlRowStatus,
       "hwSmartLinkMibTraps": hwSmartLinkMibTraps,
       "hwSmartLinkLinkSwitch": hwSmartLinkLinkSwitch,
       "hwSmartLinkInactiveLinkFail": hwSmartLinkInactiveLinkFail,
       "hwSmartLinkInactiveLinkResume": hwSmartLinkInactiveLinkResume,
       "hwSmartLinkGroupEnable": hwSmartLinkGroupEnable,
       "hwSmartLinkGroupDisable": hwSmartLinkGroupDisable,
       "hwSmartLinkLinkSwitchToMaster": hwSmartLinkLinkSwitchToMaster,
       "hwSmartLinkLinkSwitchToSlave": hwSmartLinkLinkSwitchToSlave,
       "hwSmartLinkGroupUp": hwSmartLinkGroupUp,
       "hwSmartLinkGroupDown": hwSmartLinkGroupDown,
       "hwSmartLinkConformance": hwSmartLinkConformance,
       "hwSmartLinkGroups": hwSmartLinkGroups,
       "hwSmartLinkInfoGroup": hwSmartLinkInfoGroup,
       "hwSmartLinkRevPortCfgGroup": hwSmartLinkRevPortCfgGroup,
       "hwSmartLinkGroupCfgGroup": hwSmartLinkGroupCfgGroup,
       "hwSmartLinkPortCfgGroup": hwSmartLinkPortCfgGroup,
       "hwMonitorLinkGroupCfgGroup": hwMonitorLinkGroupCfgGroup,
       "hwMonitorLinkUpLinkPortGroup": hwMonitorLinkUpLinkPortGroup,
       "hwMonitorLinkDownLinkPortGroup": hwMonitorLinkDownLinkPortGroup,
       "hwSmartLinkTrapGroups": hwSmartLinkTrapGroups,
       "hwSmartLinkTrapsGroup": hwSmartLinkTrapsGroup,
       "hwSmartLinkCompliances": hwSmartLinkCompliances}
)
