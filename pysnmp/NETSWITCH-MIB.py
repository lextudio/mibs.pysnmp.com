# SNMP MIB module (NETSWITCH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NETSWITCH-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:58:59 2024
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

(hpSwitch,) = mibBuilder.importSymbols(
    "HP-ICF-OID",
    "hpSwitch")

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


# Types definitions



class MacAddress(OctetString):
    """Custom type MacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpOpSystem_ObjectIdentity = ObjectIdentity
hpOpSystem = _HpOpSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 1)
)
_HpBuf_ObjectIdentity = ObjectIdentity
hpBuf = _HpBuf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 1, 1)
)
_HpMsgBuf_ObjectIdentity = ObjectIdentity
hpMsgBuf = _HpMsgBuf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 1, 1, 1)
)
_HpMsgBufTable_Object = MibTable
hpMsgBufTable = _HpMsgBufTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hpMsgBufTable.setStatus("mandatory")
_HpMsgBufEntry_Object = MibTableRow
hpMsgBufEntry = _HpMsgBufEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 1, 1, 1, 1, 1)
)
hpMsgBufEntry.setIndexNames(
    (0, "NETSWITCH-MIB", "hpMsgBufSlotIndex"),
)
if mibBuilder.loadTexts:
    hpMsgBufEntry.setStatus("mandatory")


class _HpMsgBufSlotIndex_Type(Integer32):
    """Custom type hpMsgBufSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_HpMsgBufSlotIndex_Type.__name__ = "Integer32"
_HpMsgBufSlotIndex_Object = MibTableColumn
hpMsgBufSlotIndex = _HpMsgBufSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 1, 1, 1, 1, 1, 1),
    _HpMsgBufSlotIndex_Type()
)
hpMsgBufSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpMsgBufSlotIndex.setStatus("mandatory")
_HpMsgBufCorrupted_Type = Counter32
_HpMsgBufCorrupted_Object = MibTableColumn
hpMsgBufCorrupted = _HpMsgBufCorrupted_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 1, 1, 1, 1, 1, 2),
    _HpMsgBufCorrupted_Type()
)
hpMsgBufCorrupted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpMsgBufCorrupted.setStatus("mandatory")
_HpMsgBufFree_Type = Integer32
_HpMsgBufFree_Object = MibTableColumn
hpMsgBufFree = _HpMsgBufFree_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 1, 1, 1, 1, 1, 3),
    _HpMsgBufFree_Type()
)
hpMsgBufFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpMsgBufFree.setStatus("mandatory")
_HpMsgBufInit_Type = Integer32
_HpMsgBufInit_Object = MibTableColumn
hpMsgBufInit = _HpMsgBufInit_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 1, 1, 1, 1, 1, 4),
    _HpMsgBufInit_Type()
)
hpMsgBufInit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpMsgBufInit.setStatus("mandatory")
_HpMsgBufMin_Type = Integer32
_HpMsgBufMin_Object = MibTableColumn
hpMsgBufMin = _HpMsgBufMin_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 1, 1, 1, 1, 1, 5),
    _HpMsgBufMin_Type()
)
hpMsgBufMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpMsgBufMin.setStatus("mandatory")
_HpMsgBufMiss_Type = Counter32
_HpMsgBufMiss_Object = MibTableColumn
hpMsgBufMiss = _HpMsgBufMiss_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 1, 1, 1, 1, 1, 6),
    _HpMsgBufMiss_Type()
)
hpMsgBufMiss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpMsgBufMiss.setStatus("mandatory")
_HpMsgBufSize_Type = Integer32
_HpMsgBufSize_Object = MibTableColumn
hpMsgBufSize = _HpMsgBufSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 1, 1, 1, 1, 1, 7),
    _HpMsgBufSize_Type()
)
hpMsgBufSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpMsgBufSize.setStatus("mandatory")
_HpPktBuf_ObjectIdentity = ObjectIdentity
hpPktBuf = _HpPktBuf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 1, 1, 2)
)
_HpPktBufTable_Object = MibTable
hpPktBufTable = _HpPktBufTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hpPktBufTable.setStatus("mandatory")
_HpPktBufEntry_Object = MibTableRow
hpPktBufEntry = _HpPktBufEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 1, 1, 2, 1, 1)
)
hpPktBufEntry.setIndexNames(
    (0, "NETSWITCH-MIB", "hpPktBufSlotIndex"),
)
if mibBuilder.loadTexts:
    hpPktBufEntry.setStatus("mandatory")


class _HpPktBufSlotIndex_Type(Integer32):
    """Custom type hpPktBufSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_HpPktBufSlotIndex_Type.__name__ = "Integer32"
_HpPktBufSlotIndex_Object = MibTableColumn
hpPktBufSlotIndex = _HpPktBufSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 1, 1, 2, 1, 1, 1),
    _HpPktBufSlotIndex_Type()
)
hpPktBufSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpPktBufSlotIndex.setStatus("mandatory")
_HpPktBufCorrupted_Type = Counter32
_HpPktBufCorrupted_Object = MibTableColumn
hpPktBufCorrupted = _HpPktBufCorrupted_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 1, 1, 2, 1, 1, 2),
    _HpPktBufCorrupted_Type()
)
hpPktBufCorrupted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpPktBufCorrupted.setStatus("mandatory")
_HpPktBufFree_Type = Integer32
_HpPktBufFree_Object = MibTableColumn
hpPktBufFree = _HpPktBufFree_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 1, 1, 2, 1, 1, 3),
    _HpPktBufFree_Type()
)
hpPktBufFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpPktBufFree.setStatus("mandatory")
_HpPktBufInit_Type = Integer32
_HpPktBufInit_Object = MibTableColumn
hpPktBufInit = _HpPktBufInit_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 1, 1, 2, 1, 1, 4),
    _HpPktBufInit_Type()
)
hpPktBufInit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpPktBufInit.setStatus("mandatory")
_HpPktBufMin_Type = Integer32
_HpPktBufMin_Object = MibTableColumn
hpPktBufMin = _HpPktBufMin_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 1, 1, 2, 1, 1, 5),
    _HpPktBufMin_Type()
)
hpPktBufMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpPktBufMin.setStatus("mandatory")
_HpPktBufMiss_Type = Counter32
_HpPktBufMiss_Object = MibTableColumn
hpPktBufMiss = _HpPktBufMiss_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 1, 1, 2, 1, 1, 6),
    _HpPktBufMiss_Type()
)
hpPktBufMiss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpPktBufMiss.setStatus("mandatory")
_HpPktBufSize_Type = Integer32
_HpPktBufSize_Object = MibTableColumn
hpPktBufSize = _HpPktBufSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 1, 1, 2, 1, 1, 7),
    _HpPktBufSize_Type()
)
hpPktBufSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpPktBufSize.setStatus("mandatory")
_HpMem_ObjectIdentity = ObjectIdentity
hpMem = _HpMem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 1, 2)
)
_HpLocalMem_ObjectIdentity = ObjectIdentity
hpLocalMem = _HpLocalMem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 1, 2, 1)
)
_HpLocalMemTable_Object = MibTable
hpLocalMemTable = _HpLocalMemTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hpLocalMemTable.setStatus("mandatory")
_HpLocalMemEntry_Object = MibTableRow
hpLocalMemEntry = _HpLocalMemEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 1, 2, 1, 1, 1)
)
hpLocalMemEntry.setIndexNames(
    (0, "NETSWITCH-MIB", "hpLocalMemSlotIndex"),
)
if mibBuilder.loadTexts:
    hpLocalMemEntry.setStatus("mandatory")


class _HpLocalMemSlotIndex_Type(Integer32):
    """Custom type hpLocalMemSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_HpLocalMemSlotIndex_Type.__name__ = "Integer32"
_HpLocalMemSlotIndex_Object = MibTableColumn
hpLocalMemSlotIndex = _HpLocalMemSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 1, 2, 1, 1, 1, 1),
    _HpLocalMemSlotIndex_Type()
)
hpLocalMemSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpLocalMemSlotIndex.setStatus("mandatory")
_HpLocalMemSlabCnt_Type = Counter32
_HpLocalMemSlabCnt_Object = MibTableColumn
hpLocalMemSlabCnt = _HpLocalMemSlabCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 1, 2, 1, 1, 1, 2),
    _HpLocalMemSlabCnt_Type()
)
hpLocalMemSlabCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpLocalMemSlabCnt.setStatus("mandatory")
_HpLocalMemFreeSegCnt_Type = Counter32
_HpLocalMemFreeSegCnt_Object = MibTableColumn
hpLocalMemFreeSegCnt = _HpLocalMemFreeSegCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 1, 2, 1, 1, 1, 3),
    _HpLocalMemFreeSegCnt_Type()
)
hpLocalMemFreeSegCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpLocalMemFreeSegCnt.setStatus("mandatory")
_HpLocalMemAllocSegCnt_Type = Counter32
_HpLocalMemAllocSegCnt_Object = MibTableColumn
hpLocalMemAllocSegCnt = _HpLocalMemAllocSegCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 1, 2, 1, 1, 1, 4),
    _HpLocalMemAllocSegCnt_Type()
)
hpLocalMemAllocSegCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpLocalMemAllocSegCnt.setStatus("mandatory")
_HpLocalMemTotalBytes_Type = Integer32
_HpLocalMemTotalBytes_Object = MibTableColumn
hpLocalMemTotalBytes = _HpLocalMemTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 1, 2, 1, 1, 1, 5),
    _HpLocalMemTotalBytes_Type()
)
hpLocalMemTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpLocalMemTotalBytes.setStatus("mandatory")
_HpLocalMemFreeBytes_Type = Integer32
_HpLocalMemFreeBytes_Object = MibTableColumn
hpLocalMemFreeBytes = _HpLocalMemFreeBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 1, 2, 1, 1, 1, 6),
    _HpLocalMemFreeBytes_Type()
)
hpLocalMemFreeBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpLocalMemFreeBytes.setStatus("mandatory")
_HpLocalMemAllocBytes_Type = Integer32
_HpLocalMemAllocBytes_Object = MibTableColumn
hpLocalMemAllocBytes = _HpLocalMemAllocBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 1, 2, 1, 1, 1, 7),
    _HpLocalMemAllocBytes_Type()
)
hpLocalMemAllocBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpLocalMemAllocBytes.setStatus("mandatory")
_HpGlobalMem_ObjectIdentity = ObjectIdentity
hpGlobalMem = _HpGlobalMem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 1, 2, 2)
)
_HpGlobalMemTable_Object = MibTable
hpGlobalMemTable = _HpGlobalMemTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    hpGlobalMemTable.setStatus("mandatory")
_HpGlobalMemEntry_Object = MibTableRow
hpGlobalMemEntry = _HpGlobalMemEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 1, 2, 2, 1, 1)
)
hpGlobalMemEntry.setIndexNames(
    (0, "NETSWITCH-MIB", "hpGlobalMemSlotIndex"),
)
if mibBuilder.loadTexts:
    hpGlobalMemEntry.setStatus("mandatory")


class _HpGlobalMemSlotIndex_Type(Integer32):
    """Custom type hpGlobalMemSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_HpGlobalMemSlotIndex_Type.__name__ = "Integer32"
_HpGlobalMemSlotIndex_Object = MibTableColumn
hpGlobalMemSlotIndex = _HpGlobalMemSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 1, 2, 2, 1, 1, 1),
    _HpGlobalMemSlotIndex_Type()
)
hpGlobalMemSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpGlobalMemSlotIndex.setStatus("mandatory")
_HpGlobalMemSlabCnt_Type = Counter32
_HpGlobalMemSlabCnt_Object = MibTableColumn
hpGlobalMemSlabCnt = _HpGlobalMemSlabCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 1, 2, 2, 1, 1, 2),
    _HpGlobalMemSlabCnt_Type()
)
hpGlobalMemSlabCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpGlobalMemSlabCnt.setStatus("mandatory")
_HpGlobalMemFreeSegCnt_Type = Counter32
_HpGlobalMemFreeSegCnt_Object = MibTableColumn
hpGlobalMemFreeSegCnt = _HpGlobalMemFreeSegCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 1, 2, 2, 1, 1, 3),
    _HpGlobalMemFreeSegCnt_Type()
)
hpGlobalMemFreeSegCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpGlobalMemFreeSegCnt.setStatus("mandatory")
_HpGlobalMemAllocSegCnt_Type = Counter32
_HpGlobalMemAllocSegCnt_Object = MibTableColumn
hpGlobalMemAllocSegCnt = _HpGlobalMemAllocSegCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 1, 2, 2, 1, 1, 4),
    _HpGlobalMemAllocSegCnt_Type()
)
hpGlobalMemAllocSegCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpGlobalMemAllocSegCnt.setStatus("mandatory")
_HpGlobalMemTotalBytes_Type = Integer32
_HpGlobalMemTotalBytes_Object = MibTableColumn
hpGlobalMemTotalBytes = _HpGlobalMemTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 1, 2, 2, 1, 1, 5),
    _HpGlobalMemTotalBytes_Type()
)
hpGlobalMemTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpGlobalMemTotalBytes.setStatus("mandatory")
_HpGlobalMemFreeBytes_Type = Integer32
_HpGlobalMemFreeBytes_Object = MibTableColumn
hpGlobalMemFreeBytes = _HpGlobalMemFreeBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 1, 2, 2, 1, 1, 6),
    _HpGlobalMemFreeBytes_Type()
)
hpGlobalMemFreeBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpGlobalMemFreeBytes.setStatus("mandatory")
_HpGlobalMemAllocBytes_Type = Integer32
_HpGlobalMemAllocBytes_Object = MibTableColumn
hpGlobalMemAllocBytes = _HpGlobalMemAllocBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 1, 2, 2, 1, 1, 7),
    _HpGlobalMemAllocBytes_Type()
)
hpGlobalMemAllocBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpGlobalMemAllocBytes.setStatus("mandatory")
_HpSwitchOsVersion_Type = DisplayString
_HpSwitchOsVersion_Object = MibScalar
hpSwitchOsVersion = _HpSwitchOsVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 1, 3),
    _HpSwitchOsVersion_Type()
)
hpSwitchOsVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchOsVersion.setStatus("mandatory")
_HpSwitchRomVersion_Type = DisplayString
_HpSwitchRomVersion_Object = MibScalar
hpSwitchRomVersion = _HpSwitchRomVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 1, 4),
    _HpSwitchRomVersion_Type()
)
hpSwitchRomVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchRomVersion.setStatus("mandatory")


class _HpSwitchSmartCardType_Type(Integer32):
    """Custom type hpSwitchSmartCardType based on Integer32"""
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
        *(("atm", 3),
          ("fddi", 2),
          ("fddiAndATM", 4),
          ("none", 1),
          ("other", 5))
    )


_HpSwitchSmartCardType_Type.__name__ = "Integer32"
_HpSwitchSmartCardType_Object = MibScalar
hpSwitchSmartCardType = _HpSwitchSmartCardType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 1, 5),
    _HpSwitchSmartCardType_Type()
)
hpSwitchSmartCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchSmartCardType.setStatus("mandatory")
_HpSwitchBaseMACAddress_Type = MacAddress
_HpSwitchBaseMACAddress_Object = MibScalar
hpSwitchBaseMACAddress = _HpSwitchBaseMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 1, 6),
    _HpSwitchBaseMACAddress_Type()
)
hpSwitchBaseMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchBaseMACAddress.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NETSWITCH-MIB",
    **{"MacAddress": MacAddress,
       "hpOpSystem": hpOpSystem,
       "hpBuf": hpBuf,
       "hpMsgBuf": hpMsgBuf,
       "hpMsgBufTable": hpMsgBufTable,
       "hpMsgBufEntry": hpMsgBufEntry,
       "hpMsgBufSlotIndex": hpMsgBufSlotIndex,
       "hpMsgBufCorrupted": hpMsgBufCorrupted,
       "hpMsgBufFree": hpMsgBufFree,
       "hpMsgBufInit": hpMsgBufInit,
       "hpMsgBufMin": hpMsgBufMin,
       "hpMsgBufMiss": hpMsgBufMiss,
       "hpMsgBufSize": hpMsgBufSize,
       "hpPktBuf": hpPktBuf,
       "hpPktBufTable": hpPktBufTable,
       "hpPktBufEntry": hpPktBufEntry,
       "hpPktBufSlotIndex": hpPktBufSlotIndex,
       "hpPktBufCorrupted": hpPktBufCorrupted,
       "hpPktBufFree": hpPktBufFree,
       "hpPktBufInit": hpPktBufInit,
       "hpPktBufMin": hpPktBufMin,
       "hpPktBufMiss": hpPktBufMiss,
       "hpPktBufSize": hpPktBufSize,
       "hpMem": hpMem,
       "hpLocalMem": hpLocalMem,
       "hpLocalMemTable": hpLocalMemTable,
       "hpLocalMemEntry": hpLocalMemEntry,
       "hpLocalMemSlotIndex": hpLocalMemSlotIndex,
       "hpLocalMemSlabCnt": hpLocalMemSlabCnt,
       "hpLocalMemFreeSegCnt": hpLocalMemFreeSegCnt,
       "hpLocalMemAllocSegCnt": hpLocalMemAllocSegCnt,
       "hpLocalMemTotalBytes": hpLocalMemTotalBytes,
       "hpLocalMemFreeBytes": hpLocalMemFreeBytes,
       "hpLocalMemAllocBytes": hpLocalMemAllocBytes,
       "hpGlobalMem": hpGlobalMem,
       "hpGlobalMemTable": hpGlobalMemTable,
       "hpGlobalMemEntry": hpGlobalMemEntry,
       "hpGlobalMemSlotIndex": hpGlobalMemSlotIndex,
       "hpGlobalMemSlabCnt": hpGlobalMemSlabCnt,
       "hpGlobalMemFreeSegCnt": hpGlobalMemFreeSegCnt,
       "hpGlobalMemAllocSegCnt": hpGlobalMemAllocSegCnt,
       "hpGlobalMemTotalBytes": hpGlobalMemTotalBytes,
       "hpGlobalMemFreeBytes": hpGlobalMemFreeBytes,
       "hpGlobalMemAllocBytes": hpGlobalMemAllocBytes,
       "hpSwitchOsVersion": hpSwitchOsVersion,
       "hpSwitchRomVersion": hpSwitchRomVersion,
       "hpSwitchSmartCardType": hpSwitchSmartCardType,
       "hpSwitchBaseMACAddress": hpSwitchBaseMACAddress}
)
