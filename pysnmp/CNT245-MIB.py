# SNMP MIB module (CNT245-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CNT245-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:15:58 2024
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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

cnt2Compression = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 5)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Cnt2CompressionTable_Object = MibTable
cnt2CompressionTable = _Cnt2CompressionTable_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 5, 1)
)
if mibBuilder.loadTexts:
    cnt2CompressionTable.setStatus("current")
_Cnt2CompressionEntry_Object = MibTableRow
cnt2CompressionEntry = _Cnt2CompressionEntry_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 5, 1, 1)
)
cnt2CompressionEntry.setIndexNames(
    (0, "CNT245-MIB", "cnt2CompressionSlotIndex"),
    (0, "CNT245-MIB", "cnt2CompressionIndex"),
)
if mibBuilder.loadTexts:
    cnt2CompressionEntry.setStatus("current")
_Cnt2CompressionSlotIndex_Type = Integer32
_Cnt2CompressionSlotIndex_Object = MibTableColumn
cnt2CompressionSlotIndex = _Cnt2CompressionSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 5, 1, 1, 1),
    _Cnt2CompressionSlotIndex_Type()
)
cnt2CompressionSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2CompressionSlotIndex.setStatus("current")
_Cnt2CompressionIndex_Type = Integer32
_Cnt2CompressionIndex_Object = MibTableColumn
cnt2CompressionIndex = _Cnt2CompressionIndex_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 5, 1, 1, 2),
    _Cnt2CompressionIndex_Type()
)
cnt2CompressionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2CompressionIndex.setStatus("current")
_Cnt2BytesToCompress_Type = Counter64
_Cnt2BytesToCompress_Object = MibTableColumn
cnt2BytesToCompress = _Cnt2BytesToCompress_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 5, 1, 1, 3),
    _Cnt2BytesToCompress_Type()
)
cnt2BytesToCompress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2BytesToCompress.setStatus("current")
_Cnt2CompressedBytes_Type = Counter64
_Cnt2CompressedBytes_Object = MibTableColumn
cnt2CompressedBytes = _Cnt2CompressedBytes_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 5, 1, 1, 4),
    _Cnt2CompressedBytes_Type()
)
cnt2CompressedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2CompressedBytes.setStatus("current")
_Cnt2BytesToDecompress_Type = Counter64
_Cnt2BytesToDecompress_Object = MibTableColumn
cnt2BytesToDecompress = _Cnt2BytesToDecompress_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 5, 1, 1, 5),
    _Cnt2BytesToDecompress_Type()
)
cnt2BytesToDecompress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2BytesToDecompress.setStatus("current")
_Cnt2DecompressedBytes_Type = Counter64
_Cnt2DecompressedBytes_Object = MibTableColumn
cnt2DecompressedBytes = _Cnt2DecompressedBytes_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 5, 1, 1, 6),
    _Cnt2DecompressedBytes_Type()
)
cnt2DecompressedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2DecompressedBytes.setStatus("current")
_Cnt2ifCompressionNumber_Type = Integer32
_Cnt2ifCompressionNumber_Object = MibScalar
cnt2ifCompressionNumber = _Cnt2ifCompressionNumber_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 5, 2),
    _Cnt2ifCompressionNumber_Type()
)
cnt2ifCompressionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2ifCompressionNumber.setStatus("current")
_Cnt2ifCompressionTable_Object = MibTable
cnt2ifCompressionTable = _Cnt2ifCompressionTable_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 5, 3)
)
if mibBuilder.loadTexts:
    cnt2ifCompressionTable.setStatus("current")
_Cnt2ifCompressionEntry_Object = MibTableRow
cnt2ifCompressionEntry = _Cnt2ifCompressionEntry_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 5, 3, 1)
)
cnt2ifCompressionEntry.setIndexNames(
    (0, "CNT245-MIB", "cnt2ifCompressionSlotIndex"),
    (0, "CNT245-MIB", "cnt2ifCompressionIndex"),
)
if mibBuilder.loadTexts:
    cnt2ifCompressionEntry.setStatus("current")
_Cnt2ifCompressionSlotIndex_Type = Integer32
_Cnt2ifCompressionSlotIndex_Object = MibTableColumn
cnt2ifCompressionSlotIndex = _Cnt2ifCompressionSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 5, 3, 1, 1),
    _Cnt2ifCompressionSlotIndex_Type()
)
cnt2ifCompressionSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2ifCompressionSlotIndex.setStatus("current")
_Cnt2ifCompressionIndex_Type = Integer32
_Cnt2ifCompressionIndex_Object = MibTableColumn
cnt2ifCompressionIndex = _Cnt2ifCompressionIndex_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 5, 3, 1, 2),
    _Cnt2ifCompressionIndex_Type()
)
cnt2ifCompressionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2ifCompressionIndex.setStatus("current")
_Cnt2ifCompressedOctets_Type = Counter64
_Cnt2ifCompressedOctets_Object = MibTableColumn
cnt2ifCompressedOctets = _Cnt2ifCompressedOctets_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 5, 3, 1, 3),
    _Cnt2ifCompressedOctets_Type()
)
cnt2ifCompressedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2ifCompressedOctets.setStatus("current")
_Cnt2ifCompressionRatio_Type = Integer32
_Cnt2ifCompressionRatio_Object = MibTableColumn
cnt2ifCompressionRatio = _Cnt2ifCompressionRatio_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 5, 3, 1, 4),
    _Cnt2ifCompressionRatio_Type()
)
cnt2ifCompressionRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2ifCompressionRatio.setStatus("current")
_Cnt2ifDecompressionTable_Object = MibTable
cnt2ifDecompressionTable = _Cnt2ifDecompressionTable_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 5, 4)
)
if mibBuilder.loadTexts:
    cnt2ifDecompressionTable.setStatus("current")
_Cnt2ifDecompressionEntry_Object = MibTableRow
cnt2ifDecompressionEntry = _Cnt2ifDecompressionEntry_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 5, 4, 1)
)
cnt2ifDecompressionEntry.setIndexNames(
    (0, "CNT245-MIB", "cnt2ifDecompressionSlotIndex"),
    (0, "CNT245-MIB", "cnt2ifDecompressionIndex"),
)
if mibBuilder.loadTexts:
    cnt2ifDecompressionEntry.setStatus("current")
_Cnt2ifDecompressionSlotIndex_Type = Integer32
_Cnt2ifDecompressionSlotIndex_Object = MibTableColumn
cnt2ifDecompressionSlotIndex = _Cnt2ifDecompressionSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 5, 4, 1, 1),
    _Cnt2ifDecompressionSlotIndex_Type()
)
cnt2ifDecompressionSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2ifDecompressionSlotIndex.setStatus("current")
_Cnt2ifDecompressionIndex_Type = Integer32
_Cnt2ifDecompressionIndex_Object = MibTableColumn
cnt2ifDecompressionIndex = _Cnt2ifDecompressionIndex_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 5, 4, 1, 2),
    _Cnt2ifDecompressionIndex_Type()
)
cnt2ifDecompressionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2ifDecompressionIndex.setStatus("current")
_Cnt2ifDecompressedOctets_Type = Counter64
_Cnt2ifDecompressedOctets_Object = MibTableColumn
cnt2ifDecompressedOctets = _Cnt2ifDecompressedOctets_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 5, 4, 1, 3),
    _Cnt2ifDecompressedOctets_Type()
)
cnt2ifDecompressedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2ifDecompressedOctets.setStatus("current")
_Cnt2ifDecompressionRatio_Type = Integer32
_Cnt2ifDecompressionRatio_Object = MibTableColumn
cnt2ifDecompressionRatio = _Cnt2ifDecompressionRatio_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 5, 4, 1, 4),
    _Cnt2ifDecompressionRatio_Type()
)
cnt2ifDecompressionRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2ifDecompressionRatio.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CNT245-MIB",
    **{"cnt2Compression": cnt2Compression,
       "cnt2CompressionTable": cnt2CompressionTable,
       "cnt2CompressionEntry": cnt2CompressionEntry,
       "cnt2CompressionSlotIndex": cnt2CompressionSlotIndex,
       "cnt2CompressionIndex": cnt2CompressionIndex,
       "cnt2BytesToCompress": cnt2BytesToCompress,
       "cnt2CompressedBytes": cnt2CompressedBytes,
       "cnt2BytesToDecompress": cnt2BytesToDecompress,
       "cnt2DecompressedBytes": cnt2DecompressedBytes,
       "cnt2ifCompressionNumber": cnt2ifCompressionNumber,
       "cnt2ifCompressionTable": cnt2ifCompressionTable,
       "cnt2ifCompressionEntry": cnt2ifCompressionEntry,
       "cnt2ifCompressionSlotIndex": cnt2ifCompressionSlotIndex,
       "cnt2ifCompressionIndex": cnt2ifCompressionIndex,
       "cnt2ifCompressedOctets": cnt2ifCompressedOctets,
       "cnt2ifCompressionRatio": cnt2ifCompressionRatio,
       "cnt2ifDecompressionTable": cnt2ifDecompressionTable,
       "cnt2ifDecompressionEntry": cnt2ifDecompressionEntry,
       "cnt2ifDecompressionSlotIndex": cnt2ifDecompressionSlotIndex,
       "cnt2ifDecompressionIndex": cnt2ifDecompressionIndex,
       "cnt2ifDecompressedOctets": cnt2ifDecompressedOctets,
       "cnt2ifDecompressionRatio": cnt2ifDecompressionRatio}
)
