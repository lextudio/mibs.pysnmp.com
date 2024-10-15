# SNMP MIB module (CISCO-ENHANCED-MEMPOOL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-ENHANCED-MEMPOOL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:59:24 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

(CounterBasedGauge64,) = mibBuilder.importSymbols(
    "HCNUM-TC",
    "CounterBasedGauge64")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

(AutonomousType,
 DisplayString,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "AutonomousType",
    "DisplayString",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoEnhancedMemPoolMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 221)
)
ciscoEnhancedMemPoolMIB.setRevisions(
        ("2008-12-05 00:00",
         "2008-05-07 00:00",
         "2003-02-24 00:00",
         "2001-06-05 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CempMemPoolIndex(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



class CempMemPoolIndexOrNone(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class CempMemPoolTypes(Integer32, TextualConvention):
    status = "current"
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
              8,
              9,
              10,
              11,
              12,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("asicMemory", 13),
          ("fastMemory", 5),
          ("imageMemory", 12),
          ("interruptStackMemory", 7),
          ("ioMemory", 3),
          ("localExceptionMemory", 9),
          ("multibusMemory", 6),
          ("other", 1),
          ("pciMemory", 4),
          ("posixMemory", 14),
          ("processStackMemory", 8),
          ("processorMemory", 2),
          ("reservedMemory", 11),
          ("virtualMemory", 10))
    )



class CempMemBufferPoolIndex(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



# MIB Managed Objects in the order of their OIDs

_CempMIBNotifications_ObjectIdentity = ObjectIdentity
cempMIBNotifications = _CempMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 221, 0)
)
_CempMIBObjects_ObjectIdentity = ObjectIdentity
cempMIBObjects = _CempMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 221, 1)
)
_CempMemPool_ObjectIdentity = ObjectIdentity
cempMemPool = _CempMemPool_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 221, 1, 1)
)
_CempMemPoolTable_Object = MibTable
cempMemPoolTable = _CempMemPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 221, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cempMemPoolTable.setStatus("current")
_CempMemPoolEntry_Object = MibTableRow
cempMemPoolEntry = _CempMemPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 221, 1, 1, 1, 1)
)
cempMemPoolEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-ENHANCED-MEMPOOL-MIB", "cempMemPoolIndex"),
)
if mibBuilder.loadTexts:
    cempMemPoolEntry.setStatus("current")
_CempMemPoolIndex_Type = CempMemPoolIndex
_CempMemPoolIndex_Object = MibTableColumn
cempMemPoolIndex = _CempMemPoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 221, 1, 1, 1, 1, 1),
    _CempMemPoolIndex_Type()
)
cempMemPoolIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cempMemPoolIndex.setStatus("current")
_CempMemPoolType_Type = CempMemPoolTypes
_CempMemPoolType_Object = MibTableColumn
cempMemPoolType = _CempMemPoolType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 221, 1, 1, 1, 1, 2),
    _CempMemPoolType_Type()
)
cempMemPoolType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cempMemPoolType.setStatus("current")
_CempMemPoolName_Type = SnmpAdminString
_CempMemPoolName_Object = MibTableColumn
cempMemPoolName = _CempMemPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 221, 1, 1, 1, 1, 3),
    _CempMemPoolName_Type()
)
cempMemPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cempMemPoolName.setStatus("current")
_CempMemPoolPlatformMemory_Type = AutonomousType
_CempMemPoolPlatformMemory_Object = MibTableColumn
cempMemPoolPlatformMemory = _CempMemPoolPlatformMemory_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 221, 1, 1, 1, 1, 4),
    _CempMemPoolPlatformMemory_Type()
)
cempMemPoolPlatformMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cempMemPoolPlatformMemory.setStatus("current")
_CempMemPoolAlternate_Type = CempMemPoolIndexOrNone
_CempMemPoolAlternate_Object = MibTableColumn
cempMemPoolAlternate = _CempMemPoolAlternate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 221, 1, 1, 1, 1, 5),
    _CempMemPoolAlternate_Type()
)
cempMemPoolAlternate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cempMemPoolAlternate.setStatus("current")
_CempMemPoolValid_Type = TruthValue
_CempMemPoolValid_Object = MibTableColumn
cempMemPoolValid = _CempMemPoolValid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 221, 1, 1, 1, 1, 6),
    _CempMemPoolValid_Type()
)
cempMemPoolValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cempMemPoolValid.setStatus("current")
_CempMemPoolUsed_Type = Gauge32
_CempMemPoolUsed_Object = MibTableColumn
cempMemPoolUsed = _CempMemPoolUsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 221, 1, 1, 1, 1, 7),
    _CempMemPoolUsed_Type()
)
cempMemPoolUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cempMemPoolUsed.setStatus("current")
if mibBuilder.loadTexts:
    cempMemPoolUsed.setUnits("bytes")
_CempMemPoolFree_Type = Gauge32
_CempMemPoolFree_Object = MibTableColumn
cempMemPoolFree = _CempMemPoolFree_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 221, 1, 1, 1, 1, 8),
    _CempMemPoolFree_Type()
)
cempMemPoolFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cempMemPoolFree.setStatus("current")
if mibBuilder.loadTexts:
    cempMemPoolFree.setUnits("bytes")
_CempMemPoolLargestFree_Type = Gauge32
_CempMemPoolLargestFree_Object = MibTableColumn
cempMemPoolLargestFree = _CempMemPoolLargestFree_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 221, 1, 1, 1, 1, 9),
    _CempMemPoolLargestFree_Type()
)
cempMemPoolLargestFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cempMemPoolLargestFree.setStatus("current")
if mibBuilder.loadTexts:
    cempMemPoolLargestFree.setUnits("bytes")
_CempMemPoolLowestFree_Type = Gauge32
_CempMemPoolLowestFree_Object = MibTableColumn
cempMemPoolLowestFree = _CempMemPoolLowestFree_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 221, 1, 1, 1, 1, 10),
    _CempMemPoolLowestFree_Type()
)
cempMemPoolLowestFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cempMemPoolLowestFree.setStatus("current")
if mibBuilder.loadTexts:
    cempMemPoolLowestFree.setUnits("bytes")
_CempMemPoolUsedLowWaterMark_Type = Gauge32
_CempMemPoolUsedLowWaterMark_Object = MibTableColumn
cempMemPoolUsedLowWaterMark = _CempMemPoolUsedLowWaterMark_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 221, 1, 1, 1, 1, 11),
    _CempMemPoolUsedLowWaterMark_Type()
)
cempMemPoolUsedLowWaterMark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cempMemPoolUsedLowWaterMark.setStatus("current")
_CempMemPoolAllocHit_Type = Counter32
_CempMemPoolAllocHit_Object = MibTableColumn
cempMemPoolAllocHit = _CempMemPoolAllocHit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 221, 1, 1, 1, 1, 12),
    _CempMemPoolAllocHit_Type()
)
cempMemPoolAllocHit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cempMemPoolAllocHit.setStatus("current")
_CempMemPoolAllocMiss_Type = Counter32
_CempMemPoolAllocMiss_Object = MibTableColumn
cempMemPoolAllocMiss = _CempMemPoolAllocMiss_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 221, 1, 1, 1, 1, 13),
    _CempMemPoolAllocMiss_Type()
)
cempMemPoolAllocMiss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cempMemPoolAllocMiss.setStatus("current")
_CempMemPoolFreeHit_Type = Counter32
_CempMemPoolFreeHit_Object = MibTableColumn
cempMemPoolFreeHit = _CempMemPoolFreeHit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 221, 1, 1, 1, 1, 14),
    _CempMemPoolFreeHit_Type()
)
cempMemPoolFreeHit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cempMemPoolFreeHit.setStatus("current")
_CempMemPoolFreeMiss_Type = Counter32
_CempMemPoolFreeMiss_Object = MibTableColumn
cempMemPoolFreeMiss = _CempMemPoolFreeMiss_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 221, 1, 1, 1, 1, 15),
    _CempMemPoolFreeMiss_Type()
)
cempMemPoolFreeMiss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cempMemPoolFreeMiss.setStatus("current")
_CempMemPoolShared_Type = Gauge32
_CempMemPoolShared_Object = MibTableColumn
cempMemPoolShared = _CempMemPoolShared_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 221, 1, 1, 1, 1, 16),
    _CempMemPoolShared_Type()
)
cempMemPoolShared.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cempMemPoolShared.setStatus("current")
if mibBuilder.loadTexts:
    cempMemPoolShared.setUnits("bytes")
_CempMemPoolUsedOvrflw_Type = Gauge32
_CempMemPoolUsedOvrflw_Object = MibTableColumn
cempMemPoolUsedOvrflw = _CempMemPoolUsedOvrflw_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 221, 1, 1, 1, 1, 17),
    _CempMemPoolUsedOvrflw_Type()
)
cempMemPoolUsedOvrflw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cempMemPoolUsedOvrflw.setStatus("current")
if mibBuilder.loadTexts:
    cempMemPoolUsedOvrflw.setUnits("bytes")
_CempMemPoolHCUsed_Type = CounterBasedGauge64
_CempMemPoolHCUsed_Object = MibTableColumn
cempMemPoolHCUsed = _CempMemPoolHCUsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 221, 1, 1, 1, 1, 18),
    _CempMemPoolHCUsed_Type()
)
cempMemPoolHCUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cempMemPoolHCUsed.setStatus("current")
if mibBuilder.loadTexts:
    cempMemPoolHCUsed.setUnits("bytes")
_CempMemPoolFreeOvrflw_Type = Gauge32
_CempMemPoolFreeOvrflw_Object = MibTableColumn
cempMemPoolFreeOvrflw = _CempMemPoolFreeOvrflw_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 221, 1, 1, 1, 1, 19),
    _CempMemPoolFreeOvrflw_Type()
)
cempMemPoolFreeOvrflw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cempMemPoolFreeOvrflw.setStatus("current")
if mibBuilder.loadTexts:
    cempMemPoolFreeOvrflw.setUnits("bytes")
_CempMemPoolHCFree_Type = CounterBasedGauge64
_CempMemPoolHCFree_Object = MibTableColumn
cempMemPoolHCFree = _CempMemPoolHCFree_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 221, 1, 1, 1, 1, 20),
    _CempMemPoolHCFree_Type()
)
cempMemPoolHCFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cempMemPoolHCFree.setStatus("current")
if mibBuilder.loadTexts:
    cempMemPoolHCFree.setUnits("bytes")
_CempMemPoolLargestFreeOvrflw_Type = Gauge32
_CempMemPoolLargestFreeOvrflw_Object = MibTableColumn
cempMemPoolLargestFreeOvrflw = _CempMemPoolLargestFreeOvrflw_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 221, 1, 1, 1, 1, 21),
    _CempMemPoolLargestFreeOvrflw_Type()
)
cempMemPoolLargestFreeOvrflw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cempMemPoolLargestFreeOvrflw.setStatus("current")
if mibBuilder.loadTexts:
    cempMemPoolLargestFreeOvrflw.setUnits("bytes")
_CempMemPoolHCLargestFree_Type = CounterBasedGauge64
_CempMemPoolHCLargestFree_Object = MibTableColumn
cempMemPoolHCLargestFree = _CempMemPoolHCLargestFree_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 221, 1, 1, 1, 1, 22),
    _CempMemPoolHCLargestFree_Type()
)
cempMemPoolHCLargestFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cempMemPoolHCLargestFree.setStatus("current")
if mibBuilder.loadTexts:
    cempMemPoolHCLargestFree.setUnits("bytes")
_CempMemPoolLowestFreeOvrflw_Type = Gauge32
_CempMemPoolLowestFreeOvrflw_Object = MibTableColumn
cempMemPoolLowestFreeOvrflw = _CempMemPoolLowestFreeOvrflw_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 221, 1, 1, 1, 1, 23),
    _CempMemPoolLowestFreeOvrflw_Type()
)
cempMemPoolLowestFreeOvrflw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cempMemPoolLowestFreeOvrflw.setStatus("current")
if mibBuilder.loadTexts:
    cempMemPoolLowestFreeOvrflw.setUnits("bytes")
_CempMemPoolHCLowestFree_Type = CounterBasedGauge64
_CempMemPoolHCLowestFree_Object = MibTableColumn
cempMemPoolHCLowestFree = _CempMemPoolHCLowestFree_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 221, 1, 1, 1, 1, 24),
    _CempMemPoolHCLowestFree_Type()
)
cempMemPoolHCLowestFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cempMemPoolHCLowestFree.setStatus("current")
if mibBuilder.loadTexts:
    cempMemPoolHCLowestFree.setUnits("bytes")
_CempMemPoolUsedLowWaterMarkOvrflw_Type = Gauge32
_CempMemPoolUsedLowWaterMarkOvrflw_Object = MibTableColumn
cempMemPoolUsedLowWaterMarkOvrflw = _CempMemPoolUsedLowWaterMarkOvrflw_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 221, 1, 1, 1, 1, 25),
    _CempMemPoolUsedLowWaterMarkOvrflw_Type()
)
cempMemPoolUsedLowWaterMarkOvrflw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cempMemPoolUsedLowWaterMarkOvrflw.setStatus("current")
if mibBuilder.loadTexts:
    cempMemPoolUsedLowWaterMarkOvrflw.setUnits("bytes")
_CempMemPoolHCUsedLowWaterMark_Type = CounterBasedGauge64
_CempMemPoolHCUsedLowWaterMark_Object = MibTableColumn
cempMemPoolHCUsedLowWaterMark = _CempMemPoolHCUsedLowWaterMark_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 221, 1, 1, 1, 1, 26),
    _CempMemPoolHCUsedLowWaterMark_Type()
)
cempMemPoolHCUsedLowWaterMark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cempMemPoolHCUsedLowWaterMark.setStatus("current")
if mibBuilder.loadTexts:
    cempMemPoolHCUsedLowWaterMark.setUnits("bytes")
_CempMemPoolSharedOvrflw_Type = Gauge32
_CempMemPoolSharedOvrflw_Object = MibTableColumn
cempMemPoolSharedOvrflw = _CempMemPoolSharedOvrflw_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 221, 1, 1, 1, 1, 27),
    _CempMemPoolSharedOvrflw_Type()
)
cempMemPoolSharedOvrflw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cempMemPoolSharedOvrflw.setStatus("current")
if mibBuilder.loadTexts:
    cempMemPoolSharedOvrflw.setUnits("bytes")
_CempMemPoolHCShared_Type = CounterBasedGauge64
_CempMemPoolHCShared_Object = MibTableColumn
cempMemPoolHCShared = _CempMemPoolHCShared_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 221, 1, 1, 1, 1, 28),
    _CempMemPoolHCShared_Type()
)
cempMemPoolHCShared.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cempMemPoolHCShared.setStatus("current")
if mibBuilder.loadTexts:
    cempMemPoolHCShared.setUnits("bytes")
_CempMemBufferPoolTable_Object = MibTable
cempMemBufferPoolTable = _CempMemBufferPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 221, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cempMemBufferPoolTable.setStatus("current")
_CempMemBufferPoolEntry_Object = MibTableRow
cempMemBufferPoolEntry = _CempMemBufferPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 221, 1, 1, 2, 1)
)
cempMemBufferPoolEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-ENHANCED-MEMPOOL-MIB", "cempMemBufferPoolIndex"),
)
if mibBuilder.loadTexts:
    cempMemBufferPoolEntry.setStatus("current")
_CempMemBufferPoolIndex_Type = CempMemBufferPoolIndex
_CempMemBufferPoolIndex_Object = MibTableColumn
cempMemBufferPoolIndex = _CempMemBufferPoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 221, 1, 1, 2, 1, 1),
    _CempMemBufferPoolIndex_Type()
)
cempMemBufferPoolIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cempMemBufferPoolIndex.setStatus("current")
_CempMemBufferMemPoolIndex_Type = CempMemPoolIndex
_CempMemBufferMemPoolIndex_Object = MibTableColumn
cempMemBufferMemPoolIndex = _CempMemBufferMemPoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 221, 1, 1, 2, 1, 2),
    _CempMemBufferMemPoolIndex_Type()
)
cempMemBufferMemPoolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cempMemBufferMemPoolIndex.setStatus("current")
_CempMemBufferName_Type = SnmpAdminString
_CempMemBufferName_Object = MibTableColumn
cempMemBufferName = _CempMemBufferName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 221, 1, 1, 2, 1, 3),
    _CempMemBufferName_Type()
)
cempMemBufferName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cempMemBufferName.setStatus("current")
_CempMemBufferDynamic_Type = TruthValue
_CempMemBufferDynamic_Object = MibTableColumn
cempMemBufferDynamic = _CempMemBufferDynamic_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 221, 1, 1, 2, 1, 4),
    _CempMemBufferDynamic_Type()
)
cempMemBufferDynamic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cempMemBufferDynamic.setStatus("current")
_CempMemBufferSize_Type = Unsigned32
_CempMemBufferSize_Object = MibTableColumn
cempMemBufferSize = _CempMemBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 221, 1, 1, 2, 1, 5),
    _CempMemBufferSize_Type()
)
cempMemBufferSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cempMemBufferSize.setStatus("current")
if mibBuilder.loadTexts:
    cempMemBufferSize.setUnits("bytes")
_CempMemBufferMin_Type = Unsigned32
_CempMemBufferMin_Object = MibTableColumn
cempMemBufferMin = _CempMemBufferMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 221, 1, 1, 2, 1, 6),
    _CempMemBufferMin_Type()
)
cempMemBufferMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cempMemBufferMin.setStatus("current")
_CempMemBufferMax_Type = Unsigned32
_CempMemBufferMax_Object = MibTableColumn
cempMemBufferMax = _CempMemBufferMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 221, 1, 1, 2, 1, 7),
    _CempMemBufferMax_Type()
)
cempMemBufferMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cempMemBufferMax.setStatus("current")
_CempMemBufferPermanent_Type = Unsigned32
_CempMemBufferPermanent_Object = MibTableColumn
cempMemBufferPermanent = _CempMemBufferPermanent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 221, 1, 1, 2, 1, 8),
    _CempMemBufferPermanent_Type()
)
cempMemBufferPermanent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cempMemBufferPermanent.setStatus("current")
_CempMemBufferTransient_Type = Unsigned32
_CempMemBufferTransient_Object = MibTableColumn
cempMemBufferTransient = _CempMemBufferTransient_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 221, 1, 1, 2, 1, 9),
    _CempMemBufferTransient_Type()
)
cempMemBufferTransient.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cempMemBufferTransient.setStatus("current")
_CempMemBufferTotal_Type = Gauge32
_CempMemBufferTotal_Object = MibTableColumn
cempMemBufferTotal = _CempMemBufferTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 221, 1, 1, 2, 1, 10),
    _CempMemBufferTotal_Type()
)
cempMemBufferTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cempMemBufferTotal.setStatus("current")
_CempMemBufferFree_Type = Gauge32
_CempMemBufferFree_Object = MibTableColumn
cempMemBufferFree = _CempMemBufferFree_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 221, 1, 1, 2, 1, 11),
    _CempMemBufferFree_Type()
)
cempMemBufferFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cempMemBufferFree.setStatus("current")
_CempMemBufferHit_Type = Counter32
_CempMemBufferHit_Object = MibTableColumn
cempMemBufferHit = _CempMemBufferHit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 221, 1, 1, 2, 1, 12),
    _CempMemBufferHit_Type()
)
cempMemBufferHit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cempMemBufferHit.setStatus("current")
_CempMemBufferMiss_Type = Counter32
_CempMemBufferMiss_Object = MibTableColumn
cempMemBufferMiss = _CempMemBufferMiss_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 221, 1, 1, 2, 1, 13),
    _CempMemBufferMiss_Type()
)
cempMemBufferMiss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cempMemBufferMiss.setStatus("current")
_CempMemBufferFreeHit_Type = Counter32
_CempMemBufferFreeHit_Object = MibTableColumn
cempMemBufferFreeHit = _CempMemBufferFreeHit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 221, 1, 1, 2, 1, 14),
    _CempMemBufferFreeHit_Type()
)
cempMemBufferFreeHit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cempMemBufferFreeHit.setStatus("current")
_CempMemBufferFreeMiss_Type = Counter32
_CempMemBufferFreeMiss_Object = MibTableColumn
cempMemBufferFreeMiss = _CempMemBufferFreeMiss_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 221, 1, 1, 2, 1, 15),
    _CempMemBufferFreeMiss_Type()
)
cempMemBufferFreeMiss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cempMemBufferFreeMiss.setStatus("current")
_CempMemBufferPermChange_Type = Integer32
_CempMemBufferPermChange_Object = MibTableColumn
cempMemBufferPermChange = _CempMemBufferPermChange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 221, 1, 1, 2, 1, 16),
    _CempMemBufferPermChange_Type()
)
cempMemBufferPermChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cempMemBufferPermChange.setStatus("current")
_CempMemBufferPeak_Type = Counter32
_CempMemBufferPeak_Object = MibTableColumn
cempMemBufferPeak = _CempMemBufferPeak_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 221, 1, 1, 2, 1, 17),
    _CempMemBufferPeak_Type()
)
cempMemBufferPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cempMemBufferPeak.setStatus("current")
_CempMemBufferPeakTime_Type = TimeStamp
_CempMemBufferPeakTime_Object = MibTableColumn
cempMemBufferPeakTime = _CempMemBufferPeakTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 221, 1, 1, 2, 1, 18),
    _CempMemBufferPeakTime_Type()
)
cempMemBufferPeakTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cempMemBufferPeakTime.setStatus("current")
_CempMemBufferTrim_Type = Counter32
_CempMemBufferTrim_Object = MibTableColumn
cempMemBufferTrim = _CempMemBufferTrim_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 221, 1, 1, 2, 1, 19),
    _CempMemBufferTrim_Type()
)
cempMemBufferTrim.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cempMemBufferTrim.setStatus("current")
_CempMemBufferGrow_Type = Counter32
_CempMemBufferGrow_Object = MibTableColumn
cempMemBufferGrow = _CempMemBufferGrow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 221, 1, 1, 2, 1, 20),
    _CempMemBufferGrow_Type()
)
cempMemBufferGrow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cempMemBufferGrow.setStatus("current")
_CempMemBufferFailures_Type = Counter32
_CempMemBufferFailures_Object = MibTableColumn
cempMemBufferFailures = _CempMemBufferFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 221, 1, 1, 2, 1, 21),
    _CempMemBufferFailures_Type()
)
cempMemBufferFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cempMemBufferFailures.setStatus("current")
_CempMemBufferNoStorage_Type = Counter32
_CempMemBufferNoStorage_Object = MibTableColumn
cempMemBufferNoStorage = _CempMemBufferNoStorage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 221, 1, 1, 2, 1, 22),
    _CempMemBufferNoStorage_Type()
)
cempMemBufferNoStorage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cempMemBufferNoStorage.setStatus("current")
_CempMemBufferCachePoolTable_Object = MibTable
cempMemBufferCachePoolTable = _CempMemBufferCachePoolTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 221, 1, 1, 3)
)
if mibBuilder.loadTexts:
    cempMemBufferCachePoolTable.setStatus("current")
_CempMemBufferCachePoolEntry_Object = MibTableRow
cempMemBufferCachePoolEntry = _CempMemBufferCachePoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 221, 1, 1, 3, 1)
)
cempMemBufferCachePoolEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-ENHANCED-MEMPOOL-MIB", "cempMemBufferPoolIndex"),
)
if mibBuilder.loadTexts:
    cempMemBufferCachePoolEntry.setStatus("current")
_CempMemBufferCacheSize_Type = Unsigned32
_CempMemBufferCacheSize_Object = MibTableColumn
cempMemBufferCacheSize = _CempMemBufferCacheSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 221, 1, 1, 3, 1, 1),
    _CempMemBufferCacheSize_Type()
)
cempMemBufferCacheSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cempMemBufferCacheSize.setStatus("current")
_CempMemBufferCacheTotal_Type = Gauge32
_CempMemBufferCacheTotal_Object = MibTableColumn
cempMemBufferCacheTotal = _CempMemBufferCacheTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 221, 1, 1, 3, 1, 2),
    _CempMemBufferCacheTotal_Type()
)
cempMemBufferCacheTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cempMemBufferCacheTotal.setStatus("current")
_CempMemBufferCacheUsed_Type = Gauge32
_CempMemBufferCacheUsed_Object = MibTableColumn
cempMemBufferCacheUsed = _CempMemBufferCacheUsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 221, 1, 1, 3, 1, 3),
    _CempMemBufferCacheUsed_Type()
)
cempMemBufferCacheUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cempMemBufferCacheUsed.setStatus("current")
_CempMemBufferCacheHit_Type = Counter32
_CempMemBufferCacheHit_Object = MibTableColumn
cempMemBufferCacheHit = _CempMemBufferCacheHit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 221, 1, 1, 3, 1, 4),
    _CempMemBufferCacheHit_Type()
)
cempMemBufferCacheHit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cempMemBufferCacheHit.setStatus("current")
_CempMemBufferCacheMiss_Type = Counter32
_CempMemBufferCacheMiss_Object = MibTableColumn
cempMemBufferCacheMiss = _CempMemBufferCacheMiss_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 221, 1, 1, 3, 1, 5),
    _CempMemBufferCacheMiss_Type()
)
cempMemBufferCacheMiss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cempMemBufferCacheMiss.setStatus("current")
_CempMemBufferCacheThreshold_Type = Gauge32
_CempMemBufferCacheThreshold_Object = MibTableColumn
cempMemBufferCacheThreshold = _CempMemBufferCacheThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 221, 1, 1, 3, 1, 6),
    _CempMemBufferCacheThreshold_Type()
)
cempMemBufferCacheThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cempMemBufferCacheThreshold.setStatus("current")
_CempMemBufferCacheThresholdCount_Type = Counter32
_CempMemBufferCacheThresholdCount_Object = MibTableColumn
cempMemBufferCacheThresholdCount = _CempMemBufferCacheThresholdCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 221, 1, 1, 3, 1, 7),
    _CempMemBufferCacheThresholdCount_Type()
)
cempMemBufferCacheThresholdCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cempMemBufferCacheThresholdCount.setStatus("current")
_CempNotificationConfig_ObjectIdentity = ObjectIdentity
cempNotificationConfig = _CempNotificationConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 221, 1, 2)
)


class _CempMemBufferNotifyEnabled_Type(TruthValue):
    """Custom type cempMemBufferNotifyEnabled based on TruthValue"""


_CempMemBufferNotifyEnabled_Object = MibScalar
cempMemBufferNotifyEnabled = _CempMemBufferNotifyEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 221, 1, 2, 1),
    _CempMemBufferNotifyEnabled_Type()
)
cempMemBufferNotifyEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cempMemBufferNotifyEnabled.setStatus("current")
_CempMIBConformance_ObjectIdentity = ObjectIdentity
cempMIBConformance = _CempMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 221, 3)
)
_CempMIBCompliances_ObjectIdentity = ObjectIdentity
cempMIBCompliances = _CempMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 221, 3, 1)
)
_CempMIBGroups_ObjectIdentity = ObjectIdentity
cempMIBGroups = _CempMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 221, 3, 2)
)

# Managed Objects groups

cempMemPoolGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 221, 3, 2, 1)
)
cempMemPoolGroup.setObjects(
      *(("CISCO-ENHANCED-MEMPOOL-MIB", "cempMemPoolType"),
        ("CISCO-ENHANCED-MEMPOOL-MIB", "cempMemPoolName"),
        ("CISCO-ENHANCED-MEMPOOL-MIB", "cempMemPoolValid"),
        ("CISCO-ENHANCED-MEMPOOL-MIB", "cempMemPoolUsed"),
        ("CISCO-ENHANCED-MEMPOOL-MIB", "cempMemPoolFree"))
)
if mibBuilder.loadTexts:
    cempMemPoolGroup.setStatus("deprecated")

cempMemPoolExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 221, 3, 2, 2)
)
cempMemPoolExtGroup.setObjects(
      *(("CISCO-ENHANCED-MEMPOOL-MIB", "cempMemPoolPlatformMemory"),
        ("CISCO-ENHANCED-MEMPOOL-MIB", "cempMemPoolAlternate"),
        ("CISCO-ENHANCED-MEMPOOL-MIB", "cempMemPoolLargestFree"),
        ("CISCO-ENHANCED-MEMPOOL-MIB", "cempMemPoolLowestFree"))
)
if mibBuilder.loadTexts:
    cempMemPoolExtGroup.setStatus("deprecated")

cempMemBufferGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 221, 3, 2, 3)
)
cempMemBufferGroup.setObjects(
      *(("CISCO-ENHANCED-MEMPOOL-MIB", "cempMemBufferMemPoolIndex"),
        ("CISCO-ENHANCED-MEMPOOL-MIB", "cempMemBufferName"),
        ("CISCO-ENHANCED-MEMPOOL-MIB", "cempMemBufferDynamic"),
        ("CISCO-ENHANCED-MEMPOOL-MIB", "cempMemBufferSize"),
        ("CISCO-ENHANCED-MEMPOOL-MIB", "cempMemBufferMin"),
        ("CISCO-ENHANCED-MEMPOOL-MIB", "cempMemBufferMax"),
        ("CISCO-ENHANCED-MEMPOOL-MIB", "cempMemBufferPermanent"),
        ("CISCO-ENHANCED-MEMPOOL-MIB", "cempMemBufferTransient"),
        ("CISCO-ENHANCED-MEMPOOL-MIB", "cempMemBufferTotal"),
        ("CISCO-ENHANCED-MEMPOOL-MIB", "cempMemBufferFree"),
        ("CISCO-ENHANCED-MEMPOOL-MIB", "cempMemBufferHit"),
        ("CISCO-ENHANCED-MEMPOOL-MIB", "cempMemBufferMiss"),
        ("CISCO-ENHANCED-MEMPOOL-MIB", "cempMemBufferFreeHit"),
        ("CISCO-ENHANCED-MEMPOOL-MIB", "cempMemBufferFreeMiss"),
        ("CISCO-ENHANCED-MEMPOOL-MIB", "cempMemBufferPermChange"),
        ("CISCO-ENHANCED-MEMPOOL-MIB", "cempMemBufferPeak"),
        ("CISCO-ENHANCED-MEMPOOL-MIB", "cempMemBufferPeakTime"),
        ("CISCO-ENHANCED-MEMPOOL-MIB", "cempMemBufferTrim"),
        ("CISCO-ENHANCED-MEMPOOL-MIB", "cempMemBufferGrow"),
        ("CISCO-ENHANCED-MEMPOOL-MIB", "cempMemBufferFailures"),
        ("CISCO-ENHANCED-MEMPOOL-MIB", "cempMemBufferNoStorage"))
)
if mibBuilder.loadTexts:
    cempMemBufferGroup.setStatus("current")

cempMemBufferExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 221, 3, 2, 4)
)
cempMemBufferExtGroup.setObjects(
      *(("CISCO-ENHANCED-MEMPOOL-MIB", "cempMemBufferCacheSize"),
        ("CISCO-ENHANCED-MEMPOOL-MIB", "cempMemBufferCacheTotal"),
        ("CISCO-ENHANCED-MEMPOOL-MIB", "cempMemBufferCacheUsed"),
        ("CISCO-ENHANCED-MEMPOOL-MIB", "cempMemBufferCacheHit"),
        ("CISCO-ENHANCED-MEMPOOL-MIB", "cempMemBufferCacheMiss"),
        ("CISCO-ENHANCED-MEMPOOL-MIB", "cempMemBufferCacheThreshold"),
        ("CISCO-ENHANCED-MEMPOOL-MIB", "cempMemBufferCacheThresholdCount"))
)
if mibBuilder.loadTexts:
    cempMemBufferExtGroup.setStatus("current")

cempMemBufferNotifyEnableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 221, 3, 2, 5)
)
cempMemBufferNotifyEnableGroup.setObjects(
    ("CISCO-ENHANCED-MEMPOOL-MIB", "cempMemBufferNotifyEnabled")
)
if mibBuilder.loadTexts:
    cempMemBufferNotifyEnableGroup.setStatus("current")

cempMemPoolExtGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 221, 3, 2, 7)
)
cempMemPoolExtGroupRev1.setObjects(
      *(("CISCO-ENHANCED-MEMPOOL-MIB", "cempMemPoolPlatformMemory"),
        ("CISCO-ENHANCED-MEMPOOL-MIB", "cempMemPoolAlternate"),
        ("CISCO-ENHANCED-MEMPOOL-MIB", "cempMemPoolLargestFree"),
        ("CISCO-ENHANCED-MEMPOOL-MIB", "cempMemPoolLowestFree"),
        ("CISCO-ENHANCED-MEMPOOL-MIB", "cempMemPoolUsedLowWaterMark"),
        ("CISCO-ENHANCED-MEMPOOL-MIB", "cempMemPoolAllocHit"),
        ("CISCO-ENHANCED-MEMPOOL-MIB", "cempMemPoolAllocMiss"),
        ("CISCO-ENHANCED-MEMPOOL-MIB", "cempMemPoolFreeHit"),
        ("CISCO-ENHANCED-MEMPOOL-MIB", "cempMemPoolFreeMiss"))
)
if mibBuilder.loadTexts:
    cempMemPoolExtGroupRev1.setStatus("current")

cempMemPoolGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 221, 3, 2, 8)
)
cempMemPoolGroupRev1.setObjects(
      *(("CISCO-ENHANCED-MEMPOOL-MIB", "cempMemPoolType"),
        ("CISCO-ENHANCED-MEMPOOL-MIB", "cempMemPoolName"),
        ("CISCO-ENHANCED-MEMPOOL-MIB", "cempMemPoolValid"),
        ("CISCO-ENHANCED-MEMPOOL-MIB", "cempMemPoolUsed"),
        ("CISCO-ENHANCED-MEMPOOL-MIB", "cempMemPoolFree"),
        ("CISCO-ENHANCED-MEMPOOL-MIB", "cempMemPoolShared"))
)
if mibBuilder.loadTexts:
    cempMemPoolGroupRev1.setStatus("current")

cempMemPoolHCGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 221, 3, 2, 9)
)
cempMemPoolHCGroup.setObjects(
      *(("CISCO-ENHANCED-MEMPOOL-MIB", "cempMemPoolHCUsed"),
        ("CISCO-ENHANCED-MEMPOOL-MIB", "cempMemPoolHCFree"),
        ("CISCO-ENHANCED-MEMPOOL-MIB", "cempMemPoolHCLargestFree"),
        ("CISCO-ENHANCED-MEMPOOL-MIB", "cempMemPoolHCLowestFree"),
        ("CISCO-ENHANCED-MEMPOOL-MIB", "cempMemPoolHCUsedLowWaterMark"),
        ("CISCO-ENHANCED-MEMPOOL-MIB", "cempMemPoolHCShared"))
)
if mibBuilder.loadTexts:
    cempMemPoolHCGroup.setStatus("current")

cempMemPoolOvrflwGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 221, 3, 2, 10)
)
cempMemPoolOvrflwGroup.setObjects(
      *(("CISCO-ENHANCED-MEMPOOL-MIB", "cempMemPoolUsedOvrflw"),
        ("CISCO-ENHANCED-MEMPOOL-MIB", "cempMemPoolFreeOvrflw"),
        ("CISCO-ENHANCED-MEMPOOL-MIB", "cempMemPoolLargestFreeOvrflw"),
        ("CISCO-ENHANCED-MEMPOOL-MIB", "cempMemPoolLowestFreeOvrflw"),
        ("CISCO-ENHANCED-MEMPOOL-MIB", "cempMemPoolUsedLowWaterMarkOvrflw"),
        ("CISCO-ENHANCED-MEMPOOL-MIB", "cempMemPoolSharedOvrflw"))
)
if mibBuilder.loadTexts:
    cempMemPoolOvrflwGroup.setStatus("current")


# Notification objects

cempMemBufferNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 221, 0, 1)
)
cempMemBufferNotify.setObjects(
      *(("CISCO-ENHANCED-MEMPOOL-MIB", "cempMemBufferName"),
        ("CISCO-ENHANCED-MEMPOOL-MIB", "cempMemBufferPeak"),
        ("CISCO-ENHANCED-MEMPOOL-MIB", "cempMemBufferPeakTime"))
)
if mibBuilder.loadTexts:
    cempMemBufferNotify.setStatus(
        "current"
    )


# Notifications groups

cempMemBufferNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 221, 3, 2, 6)
)
cempMemBufferNotifyGroup.setObjects(
    ("CISCO-ENHANCED-MEMPOOL-MIB", "cempMemBufferNotify")
)
if mibBuilder.loadTexts:
    cempMemBufferNotifyGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

cempMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 221, 3, 1, 1)
)
if mibBuilder.loadTexts:
    cempMIBCompliance.setStatus(
        "deprecated"
    )

cempMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 221, 3, 1, 2)
)
if mibBuilder.loadTexts:
    cempMIBComplianceRev1.setStatus(
        "deprecated"
    )

cempMIBComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 221, 3, 1, 3)
)
if mibBuilder.loadTexts:
    cempMIBComplianceRev2.setStatus(
        "deprecated"
    )

cempMIBComplianceRev3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 221, 3, 1, 4)
)
if mibBuilder.loadTexts:
    cempMIBComplianceRev3.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-ENHANCED-MEMPOOL-MIB",
    **{"CempMemPoolIndex": CempMemPoolIndex,
       "CempMemPoolIndexOrNone": CempMemPoolIndexOrNone,
       "CempMemPoolTypes": CempMemPoolTypes,
       "CempMemBufferPoolIndex": CempMemBufferPoolIndex,
       "ciscoEnhancedMemPoolMIB": ciscoEnhancedMemPoolMIB,
       "cempMIBNotifications": cempMIBNotifications,
       "cempMemBufferNotify": cempMemBufferNotify,
       "cempMIBObjects": cempMIBObjects,
       "cempMemPool": cempMemPool,
       "cempMemPoolTable": cempMemPoolTable,
       "cempMemPoolEntry": cempMemPoolEntry,
       "cempMemPoolIndex": cempMemPoolIndex,
       "cempMemPoolType": cempMemPoolType,
       "cempMemPoolName": cempMemPoolName,
       "cempMemPoolPlatformMemory": cempMemPoolPlatformMemory,
       "cempMemPoolAlternate": cempMemPoolAlternate,
       "cempMemPoolValid": cempMemPoolValid,
       "cempMemPoolUsed": cempMemPoolUsed,
       "cempMemPoolFree": cempMemPoolFree,
       "cempMemPoolLargestFree": cempMemPoolLargestFree,
       "cempMemPoolLowestFree": cempMemPoolLowestFree,
       "cempMemPoolUsedLowWaterMark": cempMemPoolUsedLowWaterMark,
       "cempMemPoolAllocHit": cempMemPoolAllocHit,
       "cempMemPoolAllocMiss": cempMemPoolAllocMiss,
       "cempMemPoolFreeHit": cempMemPoolFreeHit,
       "cempMemPoolFreeMiss": cempMemPoolFreeMiss,
       "cempMemPoolShared": cempMemPoolShared,
       "cempMemPoolUsedOvrflw": cempMemPoolUsedOvrflw,
       "cempMemPoolHCUsed": cempMemPoolHCUsed,
       "cempMemPoolFreeOvrflw": cempMemPoolFreeOvrflw,
       "cempMemPoolHCFree": cempMemPoolHCFree,
       "cempMemPoolLargestFreeOvrflw": cempMemPoolLargestFreeOvrflw,
       "cempMemPoolHCLargestFree": cempMemPoolHCLargestFree,
       "cempMemPoolLowestFreeOvrflw": cempMemPoolLowestFreeOvrflw,
       "cempMemPoolHCLowestFree": cempMemPoolHCLowestFree,
       "cempMemPoolUsedLowWaterMarkOvrflw": cempMemPoolUsedLowWaterMarkOvrflw,
       "cempMemPoolHCUsedLowWaterMark": cempMemPoolHCUsedLowWaterMark,
       "cempMemPoolSharedOvrflw": cempMemPoolSharedOvrflw,
       "cempMemPoolHCShared": cempMemPoolHCShared,
       "cempMemBufferPoolTable": cempMemBufferPoolTable,
       "cempMemBufferPoolEntry": cempMemBufferPoolEntry,
       "cempMemBufferPoolIndex": cempMemBufferPoolIndex,
       "cempMemBufferMemPoolIndex": cempMemBufferMemPoolIndex,
       "cempMemBufferName": cempMemBufferName,
       "cempMemBufferDynamic": cempMemBufferDynamic,
       "cempMemBufferSize": cempMemBufferSize,
       "cempMemBufferMin": cempMemBufferMin,
       "cempMemBufferMax": cempMemBufferMax,
       "cempMemBufferPermanent": cempMemBufferPermanent,
       "cempMemBufferTransient": cempMemBufferTransient,
       "cempMemBufferTotal": cempMemBufferTotal,
       "cempMemBufferFree": cempMemBufferFree,
       "cempMemBufferHit": cempMemBufferHit,
       "cempMemBufferMiss": cempMemBufferMiss,
       "cempMemBufferFreeHit": cempMemBufferFreeHit,
       "cempMemBufferFreeMiss": cempMemBufferFreeMiss,
       "cempMemBufferPermChange": cempMemBufferPermChange,
       "cempMemBufferPeak": cempMemBufferPeak,
       "cempMemBufferPeakTime": cempMemBufferPeakTime,
       "cempMemBufferTrim": cempMemBufferTrim,
       "cempMemBufferGrow": cempMemBufferGrow,
       "cempMemBufferFailures": cempMemBufferFailures,
       "cempMemBufferNoStorage": cempMemBufferNoStorage,
       "cempMemBufferCachePoolTable": cempMemBufferCachePoolTable,
       "cempMemBufferCachePoolEntry": cempMemBufferCachePoolEntry,
       "cempMemBufferCacheSize": cempMemBufferCacheSize,
       "cempMemBufferCacheTotal": cempMemBufferCacheTotal,
       "cempMemBufferCacheUsed": cempMemBufferCacheUsed,
       "cempMemBufferCacheHit": cempMemBufferCacheHit,
       "cempMemBufferCacheMiss": cempMemBufferCacheMiss,
       "cempMemBufferCacheThreshold": cempMemBufferCacheThreshold,
       "cempMemBufferCacheThresholdCount": cempMemBufferCacheThresholdCount,
       "cempNotificationConfig": cempNotificationConfig,
       "cempMemBufferNotifyEnabled": cempMemBufferNotifyEnabled,
       "cempMIBConformance": cempMIBConformance,
       "cempMIBCompliances": cempMIBCompliances,
       "cempMIBCompliance": cempMIBCompliance,
       "cempMIBComplianceRev1": cempMIBComplianceRev1,
       "cempMIBComplianceRev2": cempMIBComplianceRev2,
       "cempMIBComplianceRev3": cempMIBComplianceRev3,
       "cempMIBGroups": cempMIBGroups,
       "cempMemPoolGroup": cempMemPoolGroup,
       "cempMemPoolExtGroup": cempMemPoolExtGroup,
       "cempMemBufferGroup": cempMemBufferGroup,
       "cempMemBufferExtGroup": cempMemBufferExtGroup,
       "cempMemBufferNotifyEnableGroup": cempMemBufferNotifyEnableGroup,
       "cempMemBufferNotifyGroup": cempMemBufferNotifyGroup,
       "cempMemPoolExtGroupRev1": cempMemPoolExtGroupRev1,
       "cempMemPoolGroupRev1": cempMemPoolGroupRev1,
       "cempMemPoolHCGroup": cempMemPoolHCGroup,
       "cempMemPoolOvrflwGroup": cempMemPoolOvrflwGroup}
)
