# SNMP MIB module (HH3C-LswDEVM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-LswDEVM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:53:54 2024
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

(hh3cLswFrameIndex,
 hh3cLswSlotIndex) = mibBuilder.importSymbols(
    "HH3C-LSW-DEV-ADM-MIB",
    "hh3cLswFrameIndex",
    "hh3cLswSlotIndex")

(hh3cRhw,
 hh3clswCommon) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cRhw",
    "hh3clswCommon")

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

hh3cLswdevMMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 9)
)
hh3cLswdevMMib.setRevisions(
        ("2001-06-29 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cDevice_ObjectIdentity = ObjectIdentity
hh3cDevice = _Hh3cDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 8)
)
_Hh3cCpuTable_Object = MibTable
hh3cCpuTable = _Hh3cCpuTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 8, 1)
)
if mibBuilder.loadTexts:
    hh3cCpuTable.setStatus("current")
_Hh3cCpuEntry_Object = MibTableRow
hh3cCpuEntry = _Hh3cCpuEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 8, 1, 1)
)
hh3cCpuEntry.setIndexNames(
    (0, "HH3C-LswDEVM-MIB", "hh3cCpuIndex"),
)
if mibBuilder.loadTexts:
    hh3cCpuEntry.setStatus("current")
_Hh3cCpuIndex_Type = Integer32
_Hh3cCpuIndex_Object = MibTableColumn
hh3cCpuIndex = _Hh3cCpuIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 8, 1, 1, 1),
    _Hh3cCpuIndex_Type()
)
hh3cCpuIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cCpuIndex.setStatus("current")
_Hh3cCpuCostRate_Type = Gauge32
_Hh3cCpuCostRate_Object = MibTableColumn
hh3cCpuCostRate = _Hh3cCpuCostRate_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 8, 1, 1, 2),
    _Hh3cCpuCostRate_Type()
)
hh3cCpuCostRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCpuCostRate.setStatus("current")
_Hh3cCpuCostRatePer1Min_Type = Gauge32
_Hh3cCpuCostRatePer1Min_Object = MibTableColumn
hh3cCpuCostRatePer1Min = _Hh3cCpuCostRatePer1Min_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 8, 1, 1, 3),
    _Hh3cCpuCostRatePer1Min_Type()
)
hh3cCpuCostRatePer1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCpuCostRatePer1Min.setStatus("current")
_Hh3cCpuCostRatePer5Min_Type = Gauge32
_Hh3cCpuCostRatePer5Min_Object = MibTableColumn
hh3cCpuCostRatePer5Min = _Hh3cCpuCostRatePer5Min_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 8, 1, 1, 4),
    _Hh3cCpuCostRatePer5Min_Type()
)
hh3cCpuCostRatePer5Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCpuCostRatePer5Min.setStatus("current")
_Hh3cMem_ObjectIdentity = ObjectIdentity
hh3cMem = _Hh3cMem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 8, 2)
)
_Hh3cMemTable_Object = MibTable
hh3cMemTable = _Hh3cMemTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 8, 2, 1)
)
if mibBuilder.loadTexts:
    hh3cMemTable.setStatus("current")
_Hh3cMemEntry_Object = MibTableRow
hh3cMemEntry = _Hh3cMemEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 8, 2, 1, 1)
)
hh3cMemEntry.setIndexNames(
    (0, "HH3C-LswDEVM-MIB", "hh3cMemModuleIndex"),
)
if mibBuilder.loadTexts:
    hh3cMemEntry.setStatus("current")
_Hh3cMemModuleIndex_Type = Integer32
_Hh3cMemModuleIndex_Object = MibTableColumn
hh3cMemModuleIndex = _Hh3cMemModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 8, 2, 1, 1, 1),
    _Hh3cMemModuleIndex_Type()
)
hh3cMemModuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cMemModuleIndex.setStatus("current")
_Hh3cMemSize_Type = Gauge32
_Hh3cMemSize_Object = MibTableColumn
hh3cMemSize = _Hh3cMemSize_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 8, 2, 1, 1, 2),
    _Hh3cMemSize_Type()
)
hh3cMemSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMemSize.setStatus("current")
_Hh3cMemFree_Type = Gauge32
_Hh3cMemFree_Object = MibTableColumn
hh3cMemFree = _Hh3cMemFree_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 8, 2, 1, 1, 3),
    _Hh3cMemFree_Type()
)
hh3cMemFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMemFree.setStatus("current")
_Hh3cMemRawSliceUsed_Type = Gauge32
_Hh3cMemRawSliceUsed_Object = MibTableColumn
hh3cMemRawSliceUsed = _Hh3cMemRawSliceUsed_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 8, 2, 1, 1, 4),
    _Hh3cMemRawSliceUsed_Type()
)
hh3cMemRawSliceUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMemRawSliceUsed.setStatus("current")
_Hh3cMemLgFree_Type = Gauge32
_Hh3cMemLgFree_Object = MibTableColumn
hh3cMemLgFree = _Hh3cMemLgFree_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 8, 2, 1, 1, 5),
    _Hh3cMemLgFree_Type()
)
hh3cMemLgFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMemLgFree.setStatus("current")
_Hh3cMemFail_Type = Gauge32
_Hh3cMemFail_Object = MibTableColumn
hh3cMemFail = _Hh3cMemFail_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 8, 2, 1, 1, 6),
    _Hh3cMemFail_Type()
)
hh3cMemFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMemFail.setStatus("current")
_Hh3cMemFailNoMem_Type = Gauge32
_Hh3cMemFailNoMem_Object = MibTableColumn
hh3cMemFailNoMem = _Hh3cMemFailNoMem_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 8, 2, 1, 1, 7),
    _Hh3cMemFailNoMem_Type()
)
hh3cMemFailNoMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMemFailNoMem.setStatus("current")
_Hh3cBufTable_Object = MibTable
hh3cBufTable = _Hh3cBufTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 8, 2, 2)
)
if mibBuilder.loadTexts:
    hh3cBufTable.setStatus("current")
_Hh3cBufEntry_Object = MibTableRow
hh3cBufEntry = _Hh3cBufEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 8, 2, 2, 1)
)
hh3cBufEntry.setIndexNames(
    (0, "HH3C-LswDEVM-MIB", "hh3cBufModuleIndex"),
    (0, "HH3C-LswDEVM-MIB", "hh3cBufSize"),
)
if mibBuilder.loadTexts:
    hh3cBufEntry.setStatus("current")
_Hh3cBufModuleIndex_Type = Integer32
_Hh3cBufModuleIndex_Object = MibTableColumn
hh3cBufModuleIndex = _Hh3cBufModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 8, 2, 2, 1, 1),
    _Hh3cBufModuleIndex_Type()
)
hh3cBufModuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cBufModuleIndex.setStatus("current")
_Hh3cBufSize_Type = Integer32
_Hh3cBufSize_Object = MibTableColumn
hh3cBufSize = _Hh3cBufSize_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 8, 2, 2, 1, 2),
    _Hh3cBufSize_Type()
)
hh3cBufSize.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cBufSize.setStatus("current")
_Hh3cBufCurrentTotal_Type = Gauge32
_Hh3cBufCurrentTotal_Object = MibTableColumn
hh3cBufCurrentTotal = _Hh3cBufCurrentTotal_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 8, 2, 2, 1, 3),
    _Hh3cBufCurrentTotal_Type()
)
hh3cBufCurrentTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cBufCurrentTotal.setStatus("current")
_Hh3cBufCurrentUsed_Type = Gauge32
_Hh3cBufCurrentUsed_Object = MibTableColumn
hh3cBufCurrentUsed = _Hh3cBufCurrentUsed_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 8, 2, 2, 1, 4),
    _Hh3cBufCurrentUsed_Type()
)
hh3cBufCurrentUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cBufCurrentUsed.setStatus("current")
_Hh3cFlh_ObjectIdentity = ObjectIdentity
hh3cFlh = _Hh3cFlh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 8, 3)
)
_Hh3cFlhTotalSize_Type = Integer32
_Hh3cFlhTotalSize_Object = MibScalar
hh3cFlhTotalSize = _Hh3cFlhTotalSize_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 8, 3, 1),
    _Hh3cFlhTotalSize_Type()
)
hh3cFlhTotalSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFlhTotalSize.setStatus("current")
_Hh3cFlhTotalFree_Type = Integer32
_Hh3cFlhTotalFree_Object = MibScalar
hh3cFlhTotalFree = _Hh3cFlhTotalFree_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 8, 3, 2),
    _Hh3cFlhTotalFree_Type()
)
hh3cFlhTotalFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFlhTotalFree.setStatus("current")


class _Hh3cFlhLastDelTime_Type(TimeTicks):
    """Custom type hh3cFlhLastDelTime based on TimeTicks"""
    defaultValue = 0


_Hh3cFlhLastDelTime_Object = MibScalar
hh3cFlhLastDelTime = _Hh3cFlhLastDelTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 8, 3, 3),
    _Hh3cFlhLastDelTime_Type()
)
hh3cFlhLastDelTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFlhLastDelTime.setStatus("current")


class _Hh3cFlhDelState_Type(Integer32):
    """Custom type hh3cFlhDelState based on Integer32"""
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


_Hh3cFlhDelState_Type.__name__ = "Integer32"
_Hh3cFlhDelState_Object = MibScalar
hh3cFlhDelState = _Hh3cFlhDelState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 8, 3, 4),
    _Hh3cFlhDelState_Type()
)
hh3cFlhDelState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFlhDelState.setStatus("current")


class _Hh3cFlhState_Type(Integer32):
    """Custom type hh3cFlhState based on Integer32"""
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


_Hh3cFlhState_Type.__name__ = "Integer32"
_Hh3cFlhState_Object = MibScalar
hh3cFlhState = _Hh3cFlhState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 8, 3, 5),
    _Hh3cFlhState_Type()
)
hh3cFlhState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFlhState.setStatus("current")
_Hh3cLswdevMMibObject_ObjectIdentity = ObjectIdentity
hh3cLswdevMMibObject = _Hh3cLswdevMMibObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 9, 1)
)
if mibBuilder.loadTexts:
    hh3cLswdevMMibObject.setStatus("current")
_Hh3cdevMFanStatusTable_Object = MibTable
hh3cdevMFanStatusTable = _Hh3cdevMFanStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 9, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cdevMFanStatusTable.setStatus("current")
_Hh3cdevMFanStatusEntry_Object = MibTableRow
hh3cdevMFanStatusEntry = _Hh3cdevMFanStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 9, 1, 1, 1)
)
hh3cdevMFanStatusEntry.setIndexNames(
    (0, "HH3C-LswDEVM-MIB", "hh3cDevMFanNum"),
)
if mibBuilder.loadTexts:
    hh3cdevMFanStatusEntry.setStatus("current")
_Hh3cDevMFanNum_Type = Integer32
_Hh3cDevMFanNum_Object = MibTableColumn
hh3cDevMFanNum = _Hh3cDevMFanNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 9, 1, 1, 1, 1),
    _Hh3cDevMFanNum_Type()
)
hh3cDevMFanNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDevMFanNum.setStatus("current")


class _Hh3cDevMFanStatus_Type(Integer32):
    """Custom type hh3cDevMFanStatus based on Integer32"""
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


_Hh3cDevMFanStatus_Type.__name__ = "Integer32"
_Hh3cDevMFanStatus_Object = MibTableColumn
hh3cDevMFanStatus = _Hh3cDevMFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 9, 1, 1, 1, 2),
    _Hh3cDevMFanStatus_Type()
)
hh3cDevMFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDevMFanStatus.setStatus("current")
_Hh3cdevMPowerStatusTable_Object = MibTable
hh3cdevMPowerStatusTable = _Hh3cdevMPowerStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 9, 1, 2)
)
if mibBuilder.loadTexts:
    hh3cdevMPowerStatusTable.setStatus("current")
_Hh3cdevMPowerStatusEntry_Object = MibTableRow
hh3cdevMPowerStatusEntry = _Hh3cdevMPowerStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 9, 1, 2, 1)
)
hh3cdevMPowerStatusEntry.setIndexNames(
    (0, "HH3C-LswDEVM-MIB", "hh3cDevMPowerNum"),
)
if mibBuilder.loadTexts:
    hh3cdevMPowerStatusEntry.setStatus("current")
_Hh3cDevMPowerNum_Type = Integer32
_Hh3cDevMPowerNum_Object = MibTableColumn
hh3cDevMPowerNum = _Hh3cDevMPowerNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 9, 1, 2, 1, 1),
    _Hh3cDevMPowerNum_Type()
)
hh3cDevMPowerNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDevMPowerNum.setStatus("current")


class _Hh3cDevMPowerStatus_Type(Integer32):
    """Custom type hh3cDevMPowerStatus based on Integer32"""
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


_Hh3cDevMPowerStatus_Type.__name__ = "Integer32"
_Hh3cDevMPowerStatus_Object = MibTableColumn
hh3cDevMPowerStatus = _Hh3cDevMPowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 9, 1, 2, 1, 2),
    _Hh3cDevMPowerStatus_Type()
)
hh3cDevMPowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDevMPowerStatus.setStatus("current")
_Hh3cdevMSlotEnvironmentTable_Object = MibTable
hh3cdevMSlotEnvironmentTable = _Hh3cdevMSlotEnvironmentTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 9, 1, 3)
)
if mibBuilder.loadTexts:
    hh3cdevMSlotEnvironmentTable.setStatus("current")
_Hh3cdevMSlotEnvironmentEntry_Object = MibTableRow
hh3cdevMSlotEnvironmentEntry = _Hh3cdevMSlotEnvironmentEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 9, 1, 3, 1)
)
hh3cdevMSlotEnvironmentEntry.setIndexNames(
    (0, "HH3C-LSW-DEV-ADM-MIB", "hh3cLswFrameIndex"),
    (0, "HH3C-LSW-DEV-ADM-MIB", "hh3cLswSlotIndex"),
    (0, "HH3C-LswDEVM-MIB", "hh3cdevMSlotEnvironmentType"),
)
if mibBuilder.loadTexts:
    hh3cdevMSlotEnvironmentEntry.setStatus("current")


class _Hh3cdevMSlotEnvironmentType_Type(Integer32):
    """Custom type hh3cdevMSlotEnvironmentType based on Integer32"""
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


_Hh3cdevMSlotEnvironmentType_Type.__name__ = "Integer32"
_Hh3cdevMSlotEnvironmentType_Object = MibTableColumn
hh3cdevMSlotEnvironmentType = _Hh3cdevMSlotEnvironmentType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 9, 1, 3, 1, 1),
    _Hh3cdevMSlotEnvironmentType_Type()
)
hh3cdevMSlotEnvironmentType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cdevMSlotEnvironmentType.setStatus("current")


class _Hh3cDevMSlotEnvironmentStatus_Type(Integer32):
    """Custom type hh3cDevMSlotEnvironmentStatus based on Integer32"""
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


_Hh3cDevMSlotEnvironmentStatus_Type.__name__ = "Integer32"
_Hh3cDevMSlotEnvironmentStatus_Object = MibTableColumn
hh3cDevMSlotEnvironmentStatus = _Hh3cDevMSlotEnvironmentStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 9, 1, 3, 1, 2),
    _Hh3cDevMSlotEnvironmentStatus_Type()
)
hh3cDevMSlotEnvironmentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDevMSlotEnvironmentStatus.setStatus("current")
_Hh3cDevMSlotEnvironmentValue_Type = Integer32
_Hh3cDevMSlotEnvironmentValue_Object = MibTableColumn
hh3cDevMSlotEnvironmentValue = _Hh3cDevMSlotEnvironmentValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 9, 1, 3, 1, 3),
    _Hh3cDevMSlotEnvironmentValue_Type()
)
hh3cDevMSlotEnvironmentValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDevMSlotEnvironmentValue.setStatus("current")
_Hh3cDevMSlotEnvironmentUpperLimit_Type = Integer32
_Hh3cDevMSlotEnvironmentUpperLimit_Object = MibTableColumn
hh3cDevMSlotEnvironmentUpperLimit = _Hh3cDevMSlotEnvironmentUpperLimit_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 9, 1, 3, 1, 4),
    _Hh3cDevMSlotEnvironmentUpperLimit_Type()
)
hh3cDevMSlotEnvironmentUpperLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDevMSlotEnvironmentUpperLimit.setStatus("current")
_Hh3cDevMSlotEnvironmentLowerLimit_Type = Integer32
_Hh3cDevMSlotEnvironmentLowerLimit_Object = MibTableColumn
hh3cDevMSlotEnvironmentLowerLimit = _Hh3cDevMSlotEnvironmentLowerLimit_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 9, 1, 3, 1, 5),
    _Hh3cDevMSlotEnvironmentLowerLimit_Type()
)
hh3cDevMSlotEnvironmentLowerLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDevMSlotEnvironmentLowerLimit.setStatus("current")


class _Hh3cLinkUpDownTrapEnable_Type(Integer32):
    """Custom type hh3cLinkUpDownTrapEnable based on Integer32"""
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


_Hh3cLinkUpDownTrapEnable_Type.__name__ = "Integer32"
_Hh3cLinkUpDownTrapEnable_Object = MibScalar
hh3cLinkUpDownTrapEnable = _Hh3cLinkUpDownTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 9, 1, 9),
    _Hh3cLinkUpDownTrapEnable_Type()
)
hh3cLinkUpDownTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cLinkUpDownTrapEnable.setStatus("current")


class _Hh3cdot1qTpFdbLearnStatus_Type(Integer32):
    """Custom type hh3cdot1qTpFdbLearnStatus based on Integer32"""
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


_Hh3cdot1qTpFdbLearnStatus_Type.__name__ = "Integer32"
_Hh3cdot1qTpFdbLearnStatus_Object = MibScalar
hh3cdot1qTpFdbLearnStatus = _Hh3cdot1qTpFdbLearnStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 9, 1, 10),
    _Hh3cdot1qTpFdbLearnStatus_Type()
)
hh3cdot1qTpFdbLearnStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdot1qTpFdbLearnStatus.setStatus("current")


class _Hh3cCfmWriteFlash_Type(Integer32):
    """Custom type hh3cCfmWriteFlash based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("write", 1)
    )


_Hh3cCfmWriteFlash_Type.__name__ = "Integer32"
_Hh3cCfmWriteFlash_Object = MibScalar
hh3cCfmWriteFlash = _Hh3cCfmWriteFlash_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 9, 1, 11),
    _Hh3cCfmWriteFlash_Type()
)
hh3cCfmWriteFlash.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cCfmWriteFlash.setStatus("current")


class _Hh3cCfmEraseFlash_Type(Integer32):
    """Custom type hh3cCfmEraseFlash based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("erase", 1)
    )


_Hh3cCfmEraseFlash_Type.__name__ = "Integer32"
_Hh3cCfmEraseFlash_Object = MibScalar
hh3cCfmEraseFlash = _Hh3cCfmEraseFlash_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 9, 1, 12),
    _Hh3cCfmEraseFlash_Type()
)
hh3cCfmEraseFlash.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cCfmEraseFlash.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-LswDEVM-MIB",
    **{"hh3cDevice": hh3cDevice,
       "hh3cCpuTable": hh3cCpuTable,
       "hh3cCpuEntry": hh3cCpuEntry,
       "hh3cCpuIndex": hh3cCpuIndex,
       "hh3cCpuCostRate": hh3cCpuCostRate,
       "hh3cCpuCostRatePer1Min": hh3cCpuCostRatePer1Min,
       "hh3cCpuCostRatePer5Min": hh3cCpuCostRatePer5Min,
       "hh3cMem": hh3cMem,
       "hh3cMemTable": hh3cMemTable,
       "hh3cMemEntry": hh3cMemEntry,
       "hh3cMemModuleIndex": hh3cMemModuleIndex,
       "hh3cMemSize": hh3cMemSize,
       "hh3cMemFree": hh3cMemFree,
       "hh3cMemRawSliceUsed": hh3cMemRawSliceUsed,
       "hh3cMemLgFree": hh3cMemLgFree,
       "hh3cMemFail": hh3cMemFail,
       "hh3cMemFailNoMem": hh3cMemFailNoMem,
       "hh3cBufTable": hh3cBufTable,
       "hh3cBufEntry": hh3cBufEntry,
       "hh3cBufModuleIndex": hh3cBufModuleIndex,
       "hh3cBufSize": hh3cBufSize,
       "hh3cBufCurrentTotal": hh3cBufCurrentTotal,
       "hh3cBufCurrentUsed": hh3cBufCurrentUsed,
       "hh3cFlh": hh3cFlh,
       "hh3cFlhTotalSize": hh3cFlhTotalSize,
       "hh3cFlhTotalFree": hh3cFlhTotalFree,
       "hh3cFlhLastDelTime": hh3cFlhLastDelTime,
       "hh3cFlhDelState": hh3cFlhDelState,
       "hh3cFlhState": hh3cFlhState,
       "hh3cLswdevMMib": hh3cLswdevMMib,
       "hh3cLswdevMMibObject": hh3cLswdevMMibObject,
       "hh3cdevMFanStatusTable": hh3cdevMFanStatusTable,
       "hh3cdevMFanStatusEntry": hh3cdevMFanStatusEntry,
       "hh3cDevMFanNum": hh3cDevMFanNum,
       "hh3cDevMFanStatus": hh3cDevMFanStatus,
       "hh3cdevMPowerStatusTable": hh3cdevMPowerStatusTable,
       "hh3cdevMPowerStatusEntry": hh3cdevMPowerStatusEntry,
       "hh3cDevMPowerNum": hh3cDevMPowerNum,
       "hh3cDevMPowerStatus": hh3cDevMPowerStatus,
       "hh3cdevMSlotEnvironmentTable": hh3cdevMSlotEnvironmentTable,
       "hh3cdevMSlotEnvironmentEntry": hh3cdevMSlotEnvironmentEntry,
       "hh3cdevMSlotEnvironmentType": hh3cdevMSlotEnvironmentType,
       "hh3cDevMSlotEnvironmentStatus": hh3cDevMSlotEnvironmentStatus,
       "hh3cDevMSlotEnvironmentValue": hh3cDevMSlotEnvironmentValue,
       "hh3cDevMSlotEnvironmentUpperLimit": hh3cDevMSlotEnvironmentUpperLimit,
       "hh3cDevMSlotEnvironmentLowerLimit": hh3cDevMSlotEnvironmentLowerLimit,
       "hh3cLinkUpDownTrapEnable": hh3cLinkUpDownTrapEnable,
       "hh3cdot1qTpFdbLearnStatus": hh3cdot1qTpFdbLearnStatus,
       "hh3cCfmWriteFlash": hh3cCfmWriteFlash,
       "hh3cCfmEraseFlash": hh3cCfmEraseFlash}
)
