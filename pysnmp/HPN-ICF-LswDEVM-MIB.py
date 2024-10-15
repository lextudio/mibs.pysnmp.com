# SNMP MIB module (HPN-ICF-LswDEVM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-LswDEVM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:00:53 2024
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

(hpnicfLswFrameIndex,
 hpnicfLswSlotIndex) = mibBuilder.importSymbols(
    "HPN-ICF-LSW-DEV-ADM-MIB",
    "hpnicfLswFrameIndex",
    "hpnicfLswSlotIndex")

(hpnicfRhw,
 hpnicflswCommon) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfRhw",
    "hpnicflswCommon")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

hpnicfLswdevMMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 9)
)
hpnicfLswdevMMib.setRevisions(
        ("2001-06-29 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpnicfDevice_ObjectIdentity = ObjectIdentity
hpnicfDevice = _HpnicfDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 8)
)
_HpnicfCpuTable_Object = MibTable
hpnicfCpuTable = _HpnicfCpuTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 8, 1)
)
if mibBuilder.loadTexts:
    hpnicfCpuTable.setStatus("current")
_HpnicfCpuEntry_Object = MibTableRow
hpnicfCpuEntry = _HpnicfCpuEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 8, 1, 1)
)
hpnicfCpuEntry.setIndexNames(
    (0, "HPN-ICF-LswDEVM-MIB", "hpnicfCpuIndex"),
)
if mibBuilder.loadTexts:
    hpnicfCpuEntry.setStatus("current")
_HpnicfCpuIndex_Type = Integer32
_HpnicfCpuIndex_Object = MibTableColumn
hpnicfCpuIndex = _HpnicfCpuIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 8, 1, 1, 1),
    _HpnicfCpuIndex_Type()
)
hpnicfCpuIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfCpuIndex.setStatus("current")
_HpnicfCpuCostRate_Type = Gauge32
_HpnicfCpuCostRate_Object = MibTableColumn
hpnicfCpuCostRate = _HpnicfCpuCostRate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 8, 1, 1, 2),
    _HpnicfCpuCostRate_Type()
)
hpnicfCpuCostRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCpuCostRate.setStatus("current")
_HpnicfCpuCostRatePer1Min_Type = Gauge32
_HpnicfCpuCostRatePer1Min_Object = MibTableColumn
hpnicfCpuCostRatePer1Min = _HpnicfCpuCostRatePer1Min_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 8, 1, 1, 3),
    _HpnicfCpuCostRatePer1Min_Type()
)
hpnicfCpuCostRatePer1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCpuCostRatePer1Min.setStatus("current")
_HpnicfCpuCostRatePer5Min_Type = Gauge32
_HpnicfCpuCostRatePer5Min_Object = MibTableColumn
hpnicfCpuCostRatePer5Min = _HpnicfCpuCostRatePer5Min_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 8, 1, 1, 4),
    _HpnicfCpuCostRatePer5Min_Type()
)
hpnicfCpuCostRatePer5Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCpuCostRatePer5Min.setStatus("current")
_HpnicfMem_ObjectIdentity = ObjectIdentity
hpnicfMem = _HpnicfMem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 8, 2)
)
_HpnicfMemTable_Object = MibTable
hpnicfMemTable = _HpnicfMemTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 8, 2, 1)
)
if mibBuilder.loadTexts:
    hpnicfMemTable.setStatus("current")
_HpnicfMemEntry_Object = MibTableRow
hpnicfMemEntry = _HpnicfMemEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 8, 2, 1, 1)
)
hpnicfMemEntry.setIndexNames(
    (0, "HPN-ICF-LswDEVM-MIB", "hpnicfMemModuleIndex"),
)
if mibBuilder.loadTexts:
    hpnicfMemEntry.setStatus("current")
_HpnicfMemModuleIndex_Type = Integer32
_HpnicfMemModuleIndex_Object = MibTableColumn
hpnicfMemModuleIndex = _HpnicfMemModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 8, 2, 1, 1, 1),
    _HpnicfMemModuleIndex_Type()
)
hpnicfMemModuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfMemModuleIndex.setStatus("current")
_HpnicfMemSize_Type = Gauge32
_HpnicfMemSize_Object = MibTableColumn
hpnicfMemSize = _HpnicfMemSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 8, 2, 1, 1, 2),
    _HpnicfMemSize_Type()
)
hpnicfMemSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfMemSize.setStatus("current")
_HpnicfMemFree_Type = Gauge32
_HpnicfMemFree_Object = MibTableColumn
hpnicfMemFree = _HpnicfMemFree_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 8, 2, 1, 1, 3),
    _HpnicfMemFree_Type()
)
hpnicfMemFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfMemFree.setStatus("current")
_HpnicfMemRawSliceUsed_Type = Gauge32
_HpnicfMemRawSliceUsed_Object = MibTableColumn
hpnicfMemRawSliceUsed = _HpnicfMemRawSliceUsed_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 8, 2, 1, 1, 4),
    _HpnicfMemRawSliceUsed_Type()
)
hpnicfMemRawSliceUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfMemRawSliceUsed.setStatus("current")
_HpnicfMemLgFree_Type = Gauge32
_HpnicfMemLgFree_Object = MibTableColumn
hpnicfMemLgFree = _HpnicfMemLgFree_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 8, 2, 1, 1, 5),
    _HpnicfMemLgFree_Type()
)
hpnicfMemLgFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfMemLgFree.setStatus("current")
_HpnicfMemFail_Type = Gauge32
_HpnicfMemFail_Object = MibTableColumn
hpnicfMemFail = _HpnicfMemFail_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 8, 2, 1, 1, 6),
    _HpnicfMemFail_Type()
)
hpnicfMemFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfMemFail.setStatus("current")
_HpnicfMemFailNoMem_Type = Gauge32
_HpnicfMemFailNoMem_Object = MibTableColumn
hpnicfMemFailNoMem = _HpnicfMemFailNoMem_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 8, 2, 1, 1, 7),
    _HpnicfMemFailNoMem_Type()
)
hpnicfMemFailNoMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfMemFailNoMem.setStatus("current")
_HpnicfBufTable_Object = MibTable
hpnicfBufTable = _HpnicfBufTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 8, 2, 2)
)
if mibBuilder.loadTexts:
    hpnicfBufTable.setStatus("current")
_HpnicfBufEntry_Object = MibTableRow
hpnicfBufEntry = _HpnicfBufEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 8, 2, 2, 1)
)
hpnicfBufEntry.setIndexNames(
    (0, "HPN-ICF-LswDEVM-MIB", "hpnicfBufModuleIndex"),
    (0, "HPN-ICF-LswDEVM-MIB", "hpnicfBufSize"),
)
if mibBuilder.loadTexts:
    hpnicfBufEntry.setStatus("current")
_HpnicfBufModuleIndex_Type = Integer32
_HpnicfBufModuleIndex_Object = MibTableColumn
hpnicfBufModuleIndex = _HpnicfBufModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 8, 2, 2, 1, 1),
    _HpnicfBufModuleIndex_Type()
)
hpnicfBufModuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfBufModuleIndex.setStatus("current")
_HpnicfBufSize_Type = Integer32
_HpnicfBufSize_Object = MibTableColumn
hpnicfBufSize = _HpnicfBufSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 8, 2, 2, 1, 2),
    _HpnicfBufSize_Type()
)
hpnicfBufSize.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfBufSize.setStatus("current")
_HpnicfBufCurrentTotal_Type = Gauge32
_HpnicfBufCurrentTotal_Object = MibTableColumn
hpnicfBufCurrentTotal = _HpnicfBufCurrentTotal_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 8, 2, 2, 1, 3),
    _HpnicfBufCurrentTotal_Type()
)
hpnicfBufCurrentTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfBufCurrentTotal.setStatus("current")
_HpnicfBufCurrentUsed_Type = Gauge32
_HpnicfBufCurrentUsed_Object = MibTableColumn
hpnicfBufCurrentUsed = _HpnicfBufCurrentUsed_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 8, 2, 2, 1, 4),
    _HpnicfBufCurrentUsed_Type()
)
hpnicfBufCurrentUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfBufCurrentUsed.setStatus("current")
_HpnicfFlh_ObjectIdentity = ObjectIdentity
hpnicfFlh = _HpnicfFlh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 8, 3)
)
_HpnicfFlhTotalSize_Type = Integer32
_HpnicfFlhTotalSize_Object = MibScalar
hpnicfFlhTotalSize = _HpnicfFlhTotalSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 8, 3, 1),
    _HpnicfFlhTotalSize_Type()
)
hpnicfFlhTotalSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFlhTotalSize.setStatus("current")
_HpnicfFlhTotalFree_Type = Integer32
_HpnicfFlhTotalFree_Object = MibScalar
hpnicfFlhTotalFree = _HpnicfFlhTotalFree_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 8, 3, 2),
    _HpnicfFlhTotalFree_Type()
)
hpnicfFlhTotalFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFlhTotalFree.setStatus("current")


class _HpnicfFlhLastDelTime_Type(TimeTicks):
    """Custom type hpnicfFlhLastDelTime based on TimeTicks"""
    defaultValue = 0


_HpnicfFlhLastDelTime_Object = MibScalar
hpnicfFlhLastDelTime = _HpnicfFlhLastDelTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 8, 3, 3),
    _HpnicfFlhLastDelTime_Type()
)
hpnicfFlhLastDelTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFlhLastDelTime.setStatus("current")


class _HpnicfFlhDelState_Type(Integer32):
    """Custom type hpnicfFlhDelState based on Integer32"""
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
        *(("blockMallocFail", 6),
          ("error", 3),
          ("executing", 1),
          ("failtoopen", 5),
          ("noneDelOperationSinceStart", 7),
          ("ok", 2),
          ("readOnly", 4))
    )


_HpnicfFlhDelState_Type.__name__ = "Integer32"
_HpnicfFlhDelState_Object = MibScalar
hpnicfFlhDelState = _HpnicfFlhDelState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 8, 3, 4),
    _HpnicfFlhDelState_Type()
)
hpnicfFlhDelState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFlhDelState.setStatus("current")


class _HpnicfFlhState_Type(Integer32):
    """Custom type hpnicfFlhState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("busy", 1),
          ("free", 2))
    )


_HpnicfFlhState_Type.__name__ = "Integer32"
_HpnicfFlhState_Object = MibScalar
hpnicfFlhState = _HpnicfFlhState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 8, 3, 5),
    _HpnicfFlhState_Type()
)
hpnicfFlhState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFlhState.setStatus("current")
_HpnicfLswdevMMibObject_ObjectIdentity = ObjectIdentity
hpnicfLswdevMMibObject = _HpnicfLswdevMMibObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 9, 1)
)
if mibBuilder.loadTexts:
    hpnicfLswdevMMibObject.setStatus("current")
_HpnicfdevMFanStatusTable_Object = MibTable
hpnicfdevMFanStatusTable = _HpnicfdevMFanStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 9, 1, 1)
)
if mibBuilder.loadTexts:
    hpnicfdevMFanStatusTable.setStatus("current")
_HpnicfdevMFanStatusEntry_Object = MibTableRow
hpnicfdevMFanStatusEntry = _HpnicfdevMFanStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 9, 1, 1, 1)
)
hpnicfdevMFanStatusEntry.setIndexNames(
    (0, "HPN-ICF-LswDEVM-MIB", "hpnicfDevMFanNum"),
)
if mibBuilder.loadTexts:
    hpnicfdevMFanStatusEntry.setStatus("current")
_HpnicfDevMFanNum_Type = Integer32
_HpnicfDevMFanNum_Object = MibTableColumn
hpnicfDevMFanNum = _HpnicfDevMFanNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 9, 1, 1, 1, 1),
    _HpnicfDevMFanNum_Type()
)
hpnicfDevMFanNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDevMFanNum.setStatus("current")


class _HpnicfDevMFanStatus_Type(Integer32):
    """Custom type hpnicfDevMFanStatus based on Integer32"""
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
        *(("active", 1),
          ("deactive", 2),
          ("not-install", 3),
          ("unsupport", 4))
    )


_HpnicfDevMFanStatus_Type.__name__ = "Integer32"
_HpnicfDevMFanStatus_Object = MibTableColumn
hpnicfDevMFanStatus = _HpnicfDevMFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 9, 1, 1, 1, 2),
    _HpnicfDevMFanStatus_Type()
)
hpnicfDevMFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDevMFanStatus.setStatus("current")
_HpnicfdevMPowerStatusTable_Object = MibTable
hpnicfdevMPowerStatusTable = _HpnicfdevMPowerStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 9, 1, 2)
)
if mibBuilder.loadTexts:
    hpnicfdevMPowerStatusTable.setStatus("current")
_HpnicfdevMPowerStatusEntry_Object = MibTableRow
hpnicfdevMPowerStatusEntry = _HpnicfdevMPowerStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 9, 1, 2, 1)
)
hpnicfdevMPowerStatusEntry.setIndexNames(
    (0, "HPN-ICF-LswDEVM-MIB", "hpnicfDevMPowerNum"),
)
if mibBuilder.loadTexts:
    hpnicfdevMPowerStatusEntry.setStatus("current")
_HpnicfDevMPowerNum_Type = Integer32
_HpnicfDevMPowerNum_Object = MibTableColumn
hpnicfDevMPowerNum = _HpnicfDevMPowerNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 9, 1, 2, 1, 1),
    _HpnicfDevMPowerNum_Type()
)
hpnicfDevMPowerNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDevMPowerNum.setStatus("current")


class _HpnicfDevMPowerStatus_Type(Integer32):
    """Custom type hpnicfDevMPowerStatus based on Integer32"""
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
        *(("active", 1),
          ("deactive", 2),
          ("not-install", 3),
          ("unsupport", 4))
    )


_HpnicfDevMPowerStatus_Type.__name__ = "Integer32"
_HpnicfDevMPowerStatus_Object = MibTableColumn
hpnicfDevMPowerStatus = _HpnicfDevMPowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 9, 1, 2, 1, 2),
    _HpnicfDevMPowerStatus_Type()
)
hpnicfDevMPowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDevMPowerStatus.setStatus("current")
_HpnicfdevMSlotEnvironmentTable_Object = MibTable
hpnicfdevMSlotEnvironmentTable = _HpnicfdevMSlotEnvironmentTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 9, 1, 3)
)
if mibBuilder.loadTexts:
    hpnicfdevMSlotEnvironmentTable.setStatus("current")
_HpnicfdevMSlotEnvironmentEntry_Object = MibTableRow
hpnicfdevMSlotEnvironmentEntry = _HpnicfdevMSlotEnvironmentEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 9, 1, 3, 1)
)
hpnicfdevMSlotEnvironmentEntry.setIndexNames(
    (0, "HPN-ICF-LSW-DEV-ADM-MIB", "hpnicfLswFrameIndex"),
    (0, "HPN-ICF-LSW-DEV-ADM-MIB", "hpnicfLswSlotIndex"),
    (0, "HPN-ICF-LswDEVM-MIB", "hpnicfdevMSlotEnvironmentType"),
)
if mibBuilder.loadTexts:
    hpnicfdevMSlotEnvironmentEntry.setStatus("current")


class _HpnicfdevMSlotEnvironmentType_Type(Integer32):
    """Custom type hpnicfdevMSlotEnvironmentType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fog", 3),
          ("humidity", 2),
          ("temperature", 1))
    )


_HpnicfdevMSlotEnvironmentType_Type.__name__ = "Integer32"
_HpnicfdevMSlotEnvironmentType_Object = MibTableColumn
hpnicfdevMSlotEnvironmentType = _HpnicfdevMSlotEnvironmentType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 9, 1, 3, 1, 1),
    _HpnicfdevMSlotEnvironmentType_Type()
)
hpnicfdevMSlotEnvironmentType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfdevMSlotEnvironmentType.setStatus("current")


class _HpnicfDevMSlotEnvironmentStatus_Type(Integer32):
    """Custom type hpnicfDevMSlotEnvironmentStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("lower", 3),
          ("normal", 1),
          ("upper", 2))
    )


_HpnicfDevMSlotEnvironmentStatus_Type.__name__ = "Integer32"
_HpnicfDevMSlotEnvironmentStatus_Object = MibTableColumn
hpnicfDevMSlotEnvironmentStatus = _HpnicfDevMSlotEnvironmentStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 9, 1, 3, 1, 2),
    _HpnicfDevMSlotEnvironmentStatus_Type()
)
hpnicfDevMSlotEnvironmentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDevMSlotEnvironmentStatus.setStatus("current")
_HpnicfDevMSlotEnvironmentValue_Type = Integer32
_HpnicfDevMSlotEnvironmentValue_Object = MibTableColumn
hpnicfDevMSlotEnvironmentValue = _HpnicfDevMSlotEnvironmentValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 9, 1, 3, 1, 3),
    _HpnicfDevMSlotEnvironmentValue_Type()
)
hpnicfDevMSlotEnvironmentValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDevMSlotEnvironmentValue.setStatus("current")
_HpnicfDevMSlotEnvironmentUpperLimit_Type = Integer32
_HpnicfDevMSlotEnvironmentUpperLimit_Object = MibTableColumn
hpnicfDevMSlotEnvironmentUpperLimit = _HpnicfDevMSlotEnvironmentUpperLimit_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 9, 1, 3, 1, 4),
    _HpnicfDevMSlotEnvironmentUpperLimit_Type()
)
hpnicfDevMSlotEnvironmentUpperLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDevMSlotEnvironmentUpperLimit.setStatus("current")
_HpnicfDevMSlotEnvironmentLowerLimit_Type = Integer32
_HpnicfDevMSlotEnvironmentLowerLimit_Object = MibTableColumn
hpnicfDevMSlotEnvironmentLowerLimit = _HpnicfDevMSlotEnvironmentLowerLimit_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 9, 1, 3, 1, 5),
    _HpnicfDevMSlotEnvironmentLowerLimit_Type()
)
hpnicfDevMSlotEnvironmentLowerLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDevMSlotEnvironmentLowerLimit.setStatus("current")


class _HpnicfLinkUpDownTrapEnable_Type(Integer32):
    """Custom type hpnicfLinkUpDownTrapEnable based on Integer32"""
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
        *(("disableBoth", 2),
          ("enableBoth", 1),
          ("enableLinkDownTrapOnly", 4),
          ("enableLinkUpTrapOnly", 3))
    )


_HpnicfLinkUpDownTrapEnable_Type.__name__ = "Integer32"
_HpnicfLinkUpDownTrapEnable_Object = MibScalar
hpnicfLinkUpDownTrapEnable = _HpnicfLinkUpDownTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 9, 1, 9),
    _HpnicfLinkUpDownTrapEnable_Type()
)
hpnicfLinkUpDownTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfLinkUpDownTrapEnable.setStatus("current")


class _Hpnicfdot1qTpFdbLearnStatus_Type(Integer32):
    """Custom type hpnicfdot1qTpFdbLearnStatus based on Integer32"""
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


_Hpnicfdot1qTpFdbLearnStatus_Type.__name__ = "Integer32"
_Hpnicfdot1qTpFdbLearnStatus_Object = MibScalar
hpnicfdot1qTpFdbLearnStatus = _Hpnicfdot1qTpFdbLearnStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 9, 1, 10),
    _Hpnicfdot1qTpFdbLearnStatus_Type()
)
hpnicfdot1qTpFdbLearnStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfdot1qTpFdbLearnStatus.setStatus("current")


class _HpnicfCfmWriteFlash_Type(Integer32):
    """Custom type hpnicfCfmWriteFlash based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("write", 1)
    )


_HpnicfCfmWriteFlash_Type.__name__ = "Integer32"
_HpnicfCfmWriteFlash_Object = MibScalar
hpnicfCfmWriteFlash = _HpnicfCfmWriteFlash_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 9, 1, 11),
    _HpnicfCfmWriteFlash_Type()
)
hpnicfCfmWriteFlash.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfCfmWriteFlash.setStatus("current")


class _HpnicfCfmEraseFlash_Type(Integer32):
    """Custom type hpnicfCfmEraseFlash based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("erase", 1)
    )


_HpnicfCfmEraseFlash_Type.__name__ = "Integer32"
_HpnicfCfmEraseFlash_Object = MibScalar
hpnicfCfmEraseFlash = _HpnicfCfmEraseFlash_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 9, 1, 12),
    _HpnicfCfmEraseFlash_Type()
)
hpnicfCfmEraseFlash.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfCfmEraseFlash.setStatus("current")
_HpnicfDevMFirstTrapTime_Type = TimeTicks
_HpnicfDevMFirstTrapTime_Object = MibScalar
hpnicfDevMFirstTrapTime = _HpnicfDevMFirstTrapTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 9, 1, 13),
    _HpnicfDevMFirstTrapTime_Type()
)
hpnicfDevMFirstTrapTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfDevMFirstTrapTime.setStatus("current")
_HpnicfdevMExternalAlarmStatus_ObjectIdentity = ObjectIdentity
hpnicfdevMExternalAlarmStatus = _HpnicfdevMExternalAlarmStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 9, 1, 14)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-LswDEVM-MIB",
    **{"hpnicfDevice": hpnicfDevice,
       "hpnicfCpuTable": hpnicfCpuTable,
       "hpnicfCpuEntry": hpnicfCpuEntry,
       "hpnicfCpuIndex": hpnicfCpuIndex,
       "hpnicfCpuCostRate": hpnicfCpuCostRate,
       "hpnicfCpuCostRatePer1Min": hpnicfCpuCostRatePer1Min,
       "hpnicfCpuCostRatePer5Min": hpnicfCpuCostRatePer5Min,
       "hpnicfMem": hpnicfMem,
       "hpnicfMemTable": hpnicfMemTable,
       "hpnicfMemEntry": hpnicfMemEntry,
       "hpnicfMemModuleIndex": hpnicfMemModuleIndex,
       "hpnicfMemSize": hpnicfMemSize,
       "hpnicfMemFree": hpnicfMemFree,
       "hpnicfMemRawSliceUsed": hpnicfMemRawSliceUsed,
       "hpnicfMemLgFree": hpnicfMemLgFree,
       "hpnicfMemFail": hpnicfMemFail,
       "hpnicfMemFailNoMem": hpnicfMemFailNoMem,
       "hpnicfBufTable": hpnicfBufTable,
       "hpnicfBufEntry": hpnicfBufEntry,
       "hpnicfBufModuleIndex": hpnicfBufModuleIndex,
       "hpnicfBufSize": hpnicfBufSize,
       "hpnicfBufCurrentTotal": hpnicfBufCurrentTotal,
       "hpnicfBufCurrentUsed": hpnicfBufCurrentUsed,
       "hpnicfFlh": hpnicfFlh,
       "hpnicfFlhTotalSize": hpnicfFlhTotalSize,
       "hpnicfFlhTotalFree": hpnicfFlhTotalFree,
       "hpnicfFlhLastDelTime": hpnicfFlhLastDelTime,
       "hpnicfFlhDelState": hpnicfFlhDelState,
       "hpnicfFlhState": hpnicfFlhState,
       "hpnicfLswdevMMib": hpnicfLswdevMMib,
       "hpnicfLswdevMMibObject": hpnicfLswdevMMibObject,
       "hpnicfdevMFanStatusTable": hpnicfdevMFanStatusTable,
       "hpnicfdevMFanStatusEntry": hpnicfdevMFanStatusEntry,
       "hpnicfDevMFanNum": hpnicfDevMFanNum,
       "hpnicfDevMFanStatus": hpnicfDevMFanStatus,
       "hpnicfdevMPowerStatusTable": hpnicfdevMPowerStatusTable,
       "hpnicfdevMPowerStatusEntry": hpnicfdevMPowerStatusEntry,
       "hpnicfDevMPowerNum": hpnicfDevMPowerNum,
       "hpnicfDevMPowerStatus": hpnicfDevMPowerStatus,
       "hpnicfdevMSlotEnvironmentTable": hpnicfdevMSlotEnvironmentTable,
       "hpnicfdevMSlotEnvironmentEntry": hpnicfdevMSlotEnvironmentEntry,
       "hpnicfdevMSlotEnvironmentType": hpnicfdevMSlotEnvironmentType,
       "hpnicfDevMSlotEnvironmentStatus": hpnicfDevMSlotEnvironmentStatus,
       "hpnicfDevMSlotEnvironmentValue": hpnicfDevMSlotEnvironmentValue,
       "hpnicfDevMSlotEnvironmentUpperLimit": hpnicfDevMSlotEnvironmentUpperLimit,
       "hpnicfDevMSlotEnvironmentLowerLimit": hpnicfDevMSlotEnvironmentLowerLimit,
       "hpnicfLinkUpDownTrapEnable": hpnicfLinkUpDownTrapEnable,
       "hpnicfdot1qTpFdbLearnStatus": hpnicfdot1qTpFdbLearnStatus,
       "hpnicfCfmWriteFlash": hpnicfCfmWriteFlash,
       "hpnicfCfmEraseFlash": hpnicfCfmEraseFlash,
       "hpnicfDevMFirstTrapTime": hpnicfDevMFirstTrapTime,
       "hpnicfdevMExternalAlarmStatus": hpnicfdevMExternalAlarmStatus}
)
