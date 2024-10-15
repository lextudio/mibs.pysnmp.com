# SNMP MIB module (ACC-COMPRESS) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ACC-COMPRESS
# Produced by pysmi-1.5.4 at Mon Oct 14 20:32:01 2024
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

(DisplayString,
 IfIndex,
 RowStatus,
 SmdsAddress,
 accBRG) = mibBuilder.importSymbols(
    "ACC-MIB",
    "DisplayString",
    "IfIndex",
    "RowStatus",
    "SmdsAddress",
    "accBRG")

(accTrapLogSeqNum,) = mibBuilder.importSymbols(
    "ACC-SYSTEM",
    "accTrapLogSeqNum")

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


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AccCompress_ObjectIdentity = ObjectIdentity
accCompress = _AccCompress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6)
)
_AccCompressDialNeighborTable_Object = MibTable
accCompressDialNeighborTable = _AccCompressDialNeighborTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 1)
)
if mibBuilder.loadTexts:
    accCompressDialNeighborTable.setStatus("mandatory")
_AccCompressDialNeighborEntry_Object = MibTableRow
accCompressDialNeighborEntry = _AccCompressDialNeighborEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 1, 1)
)
accCompressDialNeighborEntry.setIndexNames(
    (0, "ACC-COMPRESS", "accCompressDialNeighborIfIndex"),
    (0, "ACC-COMPRESS", "accCompressDialNeighborCallAddress"),
)
if mibBuilder.loadTexts:
    accCompressDialNeighborEntry.setStatus("mandatory")
_AccCompressDialNeighborIfIndex_Type = Integer32
_AccCompressDialNeighborIfIndex_Object = MibTableColumn
accCompressDialNeighborIfIndex = _AccCompressDialNeighborIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 1, 1, 1),
    _AccCompressDialNeighborIfIndex_Type()
)
accCompressDialNeighborIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressDialNeighborIfIndex.setStatus("mandatory")
_AccCompressDialNeighborCallAddress_Type = DisplayString
_AccCompressDialNeighborCallAddress_Object = MibTableColumn
accCompressDialNeighborCallAddress = _AccCompressDialNeighborCallAddress_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 1, 1, 2),
    _AccCompressDialNeighborCallAddress_Type()
)
accCompressDialNeighborCallAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressDialNeighborCallAddress.setStatus("mandatory")


class _AccCompressDialNeighborStatus_Type(Integer32):
    """Custom type accCompressDialNeighborStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              128)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 128),
          ("off", 2),
          ("on", 1))
    )


_AccCompressDialNeighborStatus_Type.__name__ = "Integer32"
_AccCompressDialNeighborStatus_Object = MibTableColumn
accCompressDialNeighborStatus = _AccCompressDialNeighborStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 1, 1, 3),
    _AccCompressDialNeighborStatus_Type()
)
accCompressDialNeighborStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accCompressDialNeighborStatus.setStatus("mandatory")
_AccCompressFfrNeighborTable_Object = MibTable
accCompressFfrNeighborTable = _AccCompressFfrNeighborTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 2)
)
if mibBuilder.loadTexts:
    accCompressFfrNeighborTable.setStatus("mandatory")
_AccCompressFfrNeighborEntry_Object = MibTableRow
accCompressFfrNeighborEntry = _AccCompressFfrNeighborEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 2, 1)
)
accCompressFfrNeighborEntry.setIndexNames(
    (0, "ACC-COMPRESS", "accCompressFfrNeighborIfIndex"),
    (0, "ACC-COMPRESS", "accCompressFfrNeighborDlci"),
)
if mibBuilder.loadTexts:
    accCompressFfrNeighborEntry.setStatus("mandatory")
_AccCompressFfrNeighborIfIndex_Type = Integer32
_AccCompressFfrNeighborIfIndex_Object = MibTableColumn
accCompressFfrNeighborIfIndex = _AccCompressFfrNeighborIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 2, 1, 1),
    _AccCompressFfrNeighborIfIndex_Type()
)
accCompressFfrNeighborIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressFfrNeighborIfIndex.setStatus("mandatory")
_AccCompressFfrNeighborDlci_Type = Integer32
_AccCompressFfrNeighborDlci_Object = MibTableColumn
accCompressFfrNeighborDlci = _AccCompressFfrNeighborDlci_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 2, 1, 2),
    _AccCompressFfrNeighborDlci_Type()
)
accCompressFfrNeighborDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressFfrNeighborDlci.setStatus("mandatory")


class _AccCompressFfrNeighborStatus_Type(Integer32):
    """Custom type accCompressFfrNeighborStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              128)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 128),
          ("off", 1),
          ("on", 2))
    )


_AccCompressFfrNeighborStatus_Type.__name__ = "Integer32"
_AccCompressFfrNeighborStatus_Object = MibTableColumn
accCompressFfrNeighborStatus = _AccCompressFfrNeighborStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 2, 1, 3),
    _AccCompressFfrNeighborStatus_Type()
)
accCompressFfrNeighborStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accCompressFfrNeighborStatus.setStatus("mandatory")
_AccCompressX25NeighborTable_Object = MibTable
accCompressX25NeighborTable = _AccCompressX25NeighborTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 3)
)
if mibBuilder.loadTexts:
    accCompressX25NeighborTable.setStatus("mandatory")
_AccCompressX25NeighborEntry_Object = MibTableRow
accCompressX25NeighborEntry = _AccCompressX25NeighborEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 3, 1)
)
accCompressX25NeighborEntry.setIndexNames(
    (0, "ACC-COMPRESS", "accCompressX25NeighborIfIndex"),
    (0, "ACC-COMPRESS", "accCompressX25NeighborAddress"),
)
if mibBuilder.loadTexts:
    accCompressX25NeighborEntry.setStatus("mandatory")
_AccCompressX25NeighborIfIndex_Type = Integer32
_AccCompressX25NeighborIfIndex_Object = MibTableColumn
accCompressX25NeighborIfIndex = _AccCompressX25NeighborIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 3, 1, 1),
    _AccCompressX25NeighborIfIndex_Type()
)
accCompressX25NeighborIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressX25NeighborIfIndex.setStatus("mandatory")
_AccCompressX25NeighborAddress_Type = DisplayString
_AccCompressX25NeighborAddress_Object = MibTableColumn
accCompressX25NeighborAddress = _AccCompressX25NeighborAddress_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 3, 1, 2),
    _AccCompressX25NeighborAddress_Type()
)
accCompressX25NeighborAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressX25NeighborAddress.setStatus("mandatory")


class _AccCompressX25NeighborStatus_Type(Integer32):
    """Custom type accCompressX25NeighborStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              128)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 128),
          ("off", 1),
          ("on", 2))
    )


_AccCompressX25NeighborStatus_Type.__name__ = "Integer32"
_AccCompressX25NeighborStatus_Object = MibTableColumn
accCompressX25NeighborStatus = _AccCompressX25NeighborStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 3, 1, 3),
    _AccCompressX25NeighborStatus_Type()
)
accCompressX25NeighborStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accCompressX25NeighborStatus.setStatus("mandatory")
_AccCompressDialStatTable_Object = MibTable
accCompressDialStatTable = _AccCompressDialStatTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 4)
)
if mibBuilder.loadTexts:
    accCompressDialStatTable.setStatus("mandatory")
_AccCompressDialStatEntry_Object = MibTableRow
accCompressDialStatEntry = _AccCompressDialStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 4, 1)
)
accCompressDialStatEntry.setIndexNames(
    (0, "ACC-COMPRESS", "accCompressDialStatIfIndex"),
)
if mibBuilder.loadTexts:
    accCompressDialStatEntry.setStatus("mandatory")
_AccCompressDialStatIfIndex_Type = Integer32
_AccCompressDialStatIfIndex_Object = MibTableColumn
accCompressDialStatIfIndex = _AccCompressDialStatIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 4, 1, 1),
    _AccCompressDialStatIfIndex_Type()
)
accCompressDialStatIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressDialStatIfIndex.setStatus("mandatory")
_AccCompressDialStatCallAddress_Type = OctetString
_AccCompressDialStatCallAddress_Object = MibTableColumn
accCompressDialStatCallAddress = _AccCompressDialStatCallAddress_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 4, 1, 2),
    _AccCompressDialStatCallAddress_Type()
)
accCompressDialStatCallAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressDialStatCallAddress.setStatus("mandatory")


class _AccCompressDialStatStatus_Type(Integer32):
    """Custom type accCompressDialStatStatus based on Integer32"""
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
        *(("conn", 2),
          ("disc", 1),
          ("resync", 4),
          ("sync", 3))
    )


_AccCompressDialStatStatus_Type.__name__ = "Integer32"
_AccCompressDialStatStatus_Object = MibTableColumn
accCompressDialStatStatus = _AccCompressDialStatStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 4, 1, 3),
    _AccCompressDialStatStatus_Type()
)
accCompressDialStatStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressDialStatStatus.setStatus("mandatory")
_AccCompressDialStatOctetsIns_Type = Counter32
_AccCompressDialStatOctetsIns_Object = MibTableColumn
accCompressDialStatOctetsIns = _AccCompressDialStatOctetsIns_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 4, 1, 4),
    _AccCompressDialStatOctetsIns_Type()
)
accCompressDialStatOctetsIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressDialStatOctetsIns.setStatus("mandatory")
_AccCompressDialStatOctetsOuts_Type = Counter32
_AccCompressDialStatOctetsOuts_Object = MibTableColumn
accCompressDialStatOctetsOuts = _AccCompressDialStatOctetsOuts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 4, 1, 5),
    _AccCompressDialStatOctetsOuts_Type()
)
accCompressDialStatOctetsOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressDialStatOctetsOuts.setStatus("mandatory")
_AccCompressDialStatPacketsIns_Type = Counter32
_AccCompressDialStatPacketsIns_Object = MibTableColumn
accCompressDialStatPacketsIns = _AccCompressDialStatPacketsIns_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 4, 1, 6),
    _AccCompressDialStatPacketsIns_Type()
)
accCompressDialStatPacketsIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressDialStatPacketsIns.setStatus("mandatory")
_AccCompressDialStatPacketsOuts_Type = Counter32
_AccCompressDialStatPacketsOuts_Object = MibTableColumn
accCompressDialStatPacketsOuts = _AccCompressDialStatPacketsOuts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 4, 1, 7),
    _AccCompressDialStatPacketsOuts_Type()
)
accCompressDialStatPacketsOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressDialStatPacketsOuts.setStatus("mandatory")
_AccCompressDialStatUnCompIns_Type = Counter32
_AccCompressDialStatUnCompIns_Object = MibTableColumn
accCompressDialStatUnCompIns = _AccCompressDialStatUnCompIns_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 4, 1, 8),
    _AccCompressDialStatUnCompIns_Type()
)
accCompressDialStatUnCompIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressDialStatUnCompIns.setStatus("mandatory")
_AccCompressDialStatUnCompOuts_Type = Counter32
_AccCompressDialStatUnCompOuts_Object = MibTableColumn
accCompressDialStatUnCompOuts = _AccCompressDialStatUnCompOuts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 4, 1, 9),
    _AccCompressDialStatUnCompOuts_Type()
)
accCompressDialStatUnCompOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressDialStatUnCompOuts.setStatus("mandatory")
_AccCompressDialStatAvgCompIn_Type = Gauge32
_AccCompressDialStatAvgCompIn_Object = MibTableColumn
accCompressDialStatAvgCompIn = _AccCompressDialStatAvgCompIn_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 4, 1, 10),
    _AccCompressDialStatAvgCompIn_Type()
)
accCompressDialStatAvgCompIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressDialStatAvgCompIn.setStatus("mandatory")
_AccCompressDialStatAvgCompOut_Type = Gauge32
_AccCompressDialStatAvgCompOut_Object = MibTableColumn
accCompressDialStatAvgCompOut = _AccCompressDialStatAvgCompOut_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 4, 1, 11),
    _AccCompressDialStatAvgCompOut_Type()
)
accCompressDialStatAvgCompOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressDialStatAvgCompOut.setStatus("mandatory")
_AccCompressDialStatHdrErrors_Type = Counter32
_AccCompressDialStatHdrErrors_Object = MibTableColumn
accCompressDialStatHdrErrors = _AccCompressDialStatHdrErrors_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 4, 1, 12),
    _AccCompressDialStatHdrErrors_Type()
)
accCompressDialStatHdrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressDialStatHdrErrors.setStatus("mandatory")
_AccCompressDialStatResyncs_Type = Counter32
_AccCompressDialStatResyncs_Object = MibTableColumn
accCompressDialStatResyncs = _AccCompressDialStatResyncs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 4, 1, 13),
    _AccCompressDialStatResyncs_Type()
)
accCompressDialStatResyncs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressDialStatResyncs.setStatus("mandatory")
_AccCompressDialStatNoEndMarks_Type = Counter32
_AccCompressDialStatNoEndMarks_Object = MibTableColumn
accCompressDialStatNoEndMarks = _AccCompressDialStatNoEndMarks_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 4, 1, 14),
    _AccCompressDialStatNoEndMarks_Type()
)
accCompressDialStatNoEndMarks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressDialStatNoEndMarks.setStatus("mandatory")
_AccCompressDialStatNoBufAvails_Type = Counter32
_AccCompressDialStatNoBufAvails_Object = MibTableColumn
accCompressDialStatNoBufAvails = _AccCompressDialStatNoBufAvails_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 4, 1, 15),
    _AccCompressDialStatNoBufAvails_Type()
)
accCompressDialStatNoBufAvails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressDialStatNoBufAvails.setStatus("mandatory")
_AccCompressFfrStatTable_Object = MibTable
accCompressFfrStatTable = _AccCompressFfrStatTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 5)
)
if mibBuilder.loadTexts:
    accCompressFfrStatTable.setStatus("mandatory")
_AccCompressFfrStatEntry_Object = MibTableRow
accCompressFfrStatEntry = _AccCompressFfrStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 5, 1)
)
accCompressFfrStatEntry.setIndexNames(
    (0, "ACC-COMPRESS", "accCompressFfrStatIfIndex"),
    (0, "ACC-COMPRESS", "accCompressFfrStatDlci"),
)
if mibBuilder.loadTexts:
    accCompressFfrStatEntry.setStatus("mandatory")
_AccCompressFfrStatIfIndex_Type = Integer32
_AccCompressFfrStatIfIndex_Object = MibTableColumn
accCompressFfrStatIfIndex = _AccCompressFfrStatIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 5, 1, 1),
    _AccCompressFfrStatIfIndex_Type()
)
accCompressFfrStatIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressFfrStatIfIndex.setStatus("mandatory")
_AccCompressFfrStatDlci_Type = Integer32
_AccCompressFfrStatDlci_Object = MibTableColumn
accCompressFfrStatDlci = _AccCompressFfrStatDlci_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 5, 1, 2),
    _AccCompressFfrStatDlci_Type()
)
accCompressFfrStatDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressFfrStatDlci.setStatus("mandatory")


class _AccCompressFfrStatStatus_Type(Integer32):
    """Custom type accCompressFfrStatStatus based on Integer32"""
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
        *(("conn", 2),
          ("disc", 1),
          ("resync", 4),
          ("sync", 3))
    )


_AccCompressFfrStatStatus_Type.__name__ = "Integer32"
_AccCompressFfrStatStatus_Object = MibTableColumn
accCompressFfrStatStatus = _AccCompressFfrStatStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 5, 1, 3),
    _AccCompressFfrStatStatus_Type()
)
accCompressFfrStatStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressFfrStatStatus.setStatus("mandatory")
_AccCompressFfrStatOctetsIns_Type = Counter32
_AccCompressFfrStatOctetsIns_Object = MibTableColumn
accCompressFfrStatOctetsIns = _AccCompressFfrStatOctetsIns_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 5, 1, 4),
    _AccCompressFfrStatOctetsIns_Type()
)
accCompressFfrStatOctetsIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressFfrStatOctetsIns.setStatus("mandatory")
_AccCompressFfrStatOctetsOuts_Type = Counter32
_AccCompressFfrStatOctetsOuts_Object = MibTableColumn
accCompressFfrStatOctetsOuts = _AccCompressFfrStatOctetsOuts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 5, 1, 5),
    _AccCompressFfrStatOctetsOuts_Type()
)
accCompressFfrStatOctetsOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressFfrStatOctetsOuts.setStatus("mandatory")
_AccCompressFfrStatPacketsIns_Type = Counter32
_AccCompressFfrStatPacketsIns_Object = MibTableColumn
accCompressFfrStatPacketsIns = _AccCompressFfrStatPacketsIns_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 5, 1, 6),
    _AccCompressFfrStatPacketsIns_Type()
)
accCompressFfrStatPacketsIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressFfrStatPacketsIns.setStatus("mandatory")
_AccCompressFfrStatPacketsOuts_Type = Counter32
_AccCompressFfrStatPacketsOuts_Object = MibTableColumn
accCompressFfrStatPacketsOuts = _AccCompressFfrStatPacketsOuts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 5, 1, 7),
    _AccCompressFfrStatPacketsOuts_Type()
)
accCompressFfrStatPacketsOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressFfrStatPacketsOuts.setStatus("mandatory")
_AccCompressFfrStatUnCompIns_Type = Counter32
_AccCompressFfrStatUnCompIns_Object = MibTableColumn
accCompressFfrStatUnCompIns = _AccCompressFfrStatUnCompIns_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 5, 1, 8),
    _AccCompressFfrStatUnCompIns_Type()
)
accCompressFfrStatUnCompIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressFfrStatUnCompIns.setStatus("mandatory")
_AccCompressFfrStatUnCompOuts_Type = Counter32
_AccCompressFfrStatUnCompOuts_Object = MibTableColumn
accCompressFfrStatUnCompOuts = _AccCompressFfrStatUnCompOuts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 5, 1, 9),
    _AccCompressFfrStatUnCompOuts_Type()
)
accCompressFfrStatUnCompOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressFfrStatUnCompOuts.setStatus("mandatory")
_AccCompressFfrStatAvgCompIn_Type = Gauge32
_AccCompressFfrStatAvgCompIn_Object = MibTableColumn
accCompressFfrStatAvgCompIn = _AccCompressFfrStatAvgCompIn_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 5, 1, 10),
    _AccCompressFfrStatAvgCompIn_Type()
)
accCompressFfrStatAvgCompIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressFfrStatAvgCompIn.setStatus("mandatory")
_AccCompressFfrStatAvgCompOut_Type = Gauge32
_AccCompressFfrStatAvgCompOut_Object = MibTableColumn
accCompressFfrStatAvgCompOut = _AccCompressFfrStatAvgCompOut_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 5, 1, 11),
    _AccCompressFfrStatAvgCompOut_Type()
)
accCompressFfrStatAvgCompOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressFfrStatAvgCompOut.setStatus("mandatory")
_AccCompressFfrStatHdrErrors_Type = Counter32
_AccCompressFfrStatHdrErrors_Object = MibTableColumn
accCompressFfrStatHdrErrors = _AccCompressFfrStatHdrErrors_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 5, 1, 12),
    _AccCompressFfrStatHdrErrors_Type()
)
accCompressFfrStatHdrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressFfrStatHdrErrors.setStatus("mandatory")
_AccCompressFfrStatResyncs_Type = Counter32
_AccCompressFfrStatResyncs_Object = MibTableColumn
accCompressFfrStatResyncs = _AccCompressFfrStatResyncs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 5, 1, 13),
    _AccCompressFfrStatResyncs_Type()
)
accCompressFfrStatResyncs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressFfrStatResyncs.setStatus("mandatory")
_AccCompressFfrStatNoEndMarks_Type = Counter32
_AccCompressFfrStatNoEndMarks_Object = MibTableColumn
accCompressFfrStatNoEndMarks = _AccCompressFfrStatNoEndMarks_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 5, 1, 14),
    _AccCompressFfrStatNoEndMarks_Type()
)
accCompressFfrStatNoEndMarks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressFfrStatNoEndMarks.setStatus("mandatory")
_AccCompressFfrStatNoBufAvails_Type = Counter32
_AccCompressFfrStatNoBufAvails_Object = MibTableColumn
accCompressFfrStatNoBufAvails = _AccCompressFfrStatNoBufAvails_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 5, 1, 15),
    _AccCompressFfrStatNoBufAvails_Type()
)
accCompressFfrStatNoBufAvails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressFfrStatNoBufAvails.setStatus("mandatory")
_AccCompressX25StatTable_Object = MibTable
accCompressX25StatTable = _AccCompressX25StatTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 6)
)
if mibBuilder.loadTexts:
    accCompressX25StatTable.setStatus("mandatory")
_AccCompressX25StatEntry_Object = MibTableRow
accCompressX25StatEntry = _AccCompressX25StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 6, 1)
)
accCompressX25StatEntry.setIndexNames(
    (0, "ACC-COMPRESS", "accCompressX25StatIfIndex"),
    (0, "ACC-COMPRESS", "accCompressX25StatAddress"),
)
if mibBuilder.loadTexts:
    accCompressX25StatEntry.setStatus("mandatory")
_AccCompressX25StatIfIndex_Type = Integer32
_AccCompressX25StatIfIndex_Object = MibTableColumn
accCompressX25StatIfIndex = _AccCompressX25StatIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 6, 1, 1),
    _AccCompressX25StatIfIndex_Type()
)
accCompressX25StatIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressX25StatIfIndex.setStatus("mandatory")
_AccCompressX25StatAddress_Type = OctetString
_AccCompressX25StatAddress_Object = MibTableColumn
accCompressX25StatAddress = _AccCompressX25StatAddress_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 6, 1, 2),
    _AccCompressX25StatAddress_Type()
)
accCompressX25StatAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressX25StatAddress.setStatus("mandatory")


class _AccCompressX25StatStatus_Type(Integer32):
    """Custom type accCompressX25StatStatus based on Integer32"""
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
        *(("conn", 2),
          ("disc", 1),
          ("resync", 4),
          ("sync", 3))
    )


_AccCompressX25StatStatus_Type.__name__ = "Integer32"
_AccCompressX25StatStatus_Object = MibTableColumn
accCompressX25StatStatus = _AccCompressX25StatStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 6, 1, 3),
    _AccCompressX25StatStatus_Type()
)
accCompressX25StatStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressX25StatStatus.setStatus("mandatory")
_AccCompressX25StatOctetsIns_Type = Counter32
_AccCompressX25StatOctetsIns_Object = MibTableColumn
accCompressX25StatOctetsIns = _AccCompressX25StatOctetsIns_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 6, 1, 4),
    _AccCompressX25StatOctetsIns_Type()
)
accCompressX25StatOctetsIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressX25StatOctetsIns.setStatus("mandatory")
_AccCompressX25StatOctetsOuts_Type = Counter32
_AccCompressX25StatOctetsOuts_Object = MibTableColumn
accCompressX25StatOctetsOuts = _AccCompressX25StatOctetsOuts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 6, 1, 5),
    _AccCompressX25StatOctetsOuts_Type()
)
accCompressX25StatOctetsOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressX25StatOctetsOuts.setStatus("mandatory")
_AccCompressX25StatPacketsIns_Type = Counter32
_AccCompressX25StatPacketsIns_Object = MibTableColumn
accCompressX25StatPacketsIns = _AccCompressX25StatPacketsIns_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 6, 1, 6),
    _AccCompressX25StatPacketsIns_Type()
)
accCompressX25StatPacketsIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressX25StatPacketsIns.setStatus("mandatory")
_AccCompressX25StatPacketsOuts_Type = Counter32
_AccCompressX25StatPacketsOuts_Object = MibTableColumn
accCompressX25StatPacketsOuts = _AccCompressX25StatPacketsOuts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 6, 1, 7),
    _AccCompressX25StatPacketsOuts_Type()
)
accCompressX25StatPacketsOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressX25StatPacketsOuts.setStatus("mandatory")
_AccCompressX25StatUnCompIns_Type = Counter32
_AccCompressX25StatUnCompIns_Object = MibTableColumn
accCompressX25StatUnCompIns = _AccCompressX25StatUnCompIns_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 6, 1, 8),
    _AccCompressX25StatUnCompIns_Type()
)
accCompressX25StatUnCompIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressX25StatUnCompIns.setStatus("mandatory")
_AccCompressX25StatUnCompOuts_Type = Counter32
_AccCompressX25StatUnCompOuts_Object = MibTableColumn
accCompressX25StatUnCompOuts = _AccCompressX25StatUnCompOuts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 6, 1, 9),
    _AccCompressX25StatUnCompOuts_Type()
)
accCompressX25StatUnCompOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressX25StatUnCompOuts.setStatus("mandatory")
_AccCompressX25StatAvgCompIn_Type = Gauge32
_AccCompressX25StatAvgCompIn_Object = MibTableColumn
accCompressX25StatAvgCompIn = _AccCompressX25StatAvgCompIn_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 6, 1, 10),
    _AccCompressX25StatAvgCompIn_Type()
)
accCompressX25StatAvgCompIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressX25StatAvgCompIn.setStatus("mandatory")
_AccCompressX25StatAvgCompOut_Type = Gauge32
_AccCompressX25StatAvgCompOut_Object = MibTableColumn
accCompressX25StatAvgCompOut = _AccCompressX25StatAvgCompOut_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 6, 1, 11),
    _AccCompressX25StatAvgCompOut_Type()
)
accCompressX25StatAvgCompOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressX25StatAvgCompOut.setStatus("mandatory")
_AccCompressX25StatHdrErrors_Type = Counter32
_AccCompressX25StatHdrErrors_Object = MibTableColumn
accCompressX25StatHdrErrors = _AccCompressX25StatHdrErrors_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 6, 1, 12),
    _AccCompressX25StatHdrErrors_Type()
)
accCompressX25StatHdrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressX25StatHdrErrors.setStatus("mandatory")
_AccCompressX25StatResyncs_Type = Counter32
_AccCompressX25StatResyncs_Object = MibTableColumn
accCompressX25StatResyncs = _AccCompressX25StatResyncs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 6, 1, 13),
    _AccCompressX25StatResyncs_Type()
)
accCompressX25StatResyncs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressX25StatResyncs.setStatus("mandatory")
_AccCompressX25StatNoEndMarks_Type = Counter32
_AccCompressX25StatNoEndMarks_Object = MibTableColumn
accCompressX25StatNoEndMarks = _AccCompressX25StatNoEndMarks_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 6, 1, 14),
    _AccCompressX25StatNoEndMarks_Type()
)
accCompressX25StatNoEndMarks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressX25StatNoEndMarks.setStatus("mandatory")
_AccCompressX25StatNoBufAvails_Type = Counter32
_AccCompressX25StatNoBufAvails_Object = MibTableColumn
accCompressX25StatNoBufAvails = _AccCompressX25StatNoBufAvails_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 6, 1, 15),
    _AccCompressX25StatNoBufAvails_Type()
)
accCompressX25StatNoBufAvails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressX25StatNoBufAvails.setStatus("mandatory")
_AccCompressPhysStatTable_Object = MibTable
accCompressPhysStatTable = _AccCompressPhysStatTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 7)
)
if mibBuilder.loadTexts:
    accCompressPhysStatTable.setStatus("mandatory")
_AccCompressPhysStatEntry_Object = MibTableRow
accCompressPhysStatEntry = _AccCompressPhysStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 7, 1)
)
accCompressPhysStatEntry.setIndexNames(
    (0, "ACC-COMPRESS", "accCompressPhysStatIfIndex"),
)
if mibBuilder.loadTexts:
    accCompressPhysStatEntry.setStatus("mandatory")
_AccCompressPhysStatIfIndex_Type = Integer32
_AccCompressPhysStatIfIndex_Object = MibTableColumn
accCompressPhysStatIfIndex = _AccCompressPhysStatIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 7, 1, 1),
    _AccCompressPhysStatIfIndex_Type()
)
accCompressPhysStatIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressPhysStatIfIndex.setStatus("mandatory")


class _AccCompressPhysStatStatus_Type(Integer32):
    """Custom type accCompressPhysStatStatus based on Integer32"""
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
        *(("conn", 2),
          ("disc", 1),
          ("resync", 4),
          ("sync", 3))
    )


_AccCompressPhysStatStatus_Type.__name__ = "Integer32"
_AccCompressPhysStatStatus_Object = MibTableColumn
accCompressPhysStatStatus = _AccCompressPhysStatStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 7, 1, 2),
    _AccCompressPhysStatStatus_Type()
)
accCompressPhysStatStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressPhysStatStatus.setStatus("mandatory")
_AccCompressPhysStatOctetsIns_Type = Counter32
_AccCompressPhysStatOctetsIns_Object = MibTableColumn
accCompressPhysStatOctetsIns = _AccCompressPhysStatOctetsIns_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 7, 1, 3),
    _AccCompressPhysStatOctetsIns_Type()
)
accCompressPhysStatOctetsIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressPhysStatOctetsIns.setStatus("mandatory")
_AccCompressPhysStatOctetsOuts_Type = Counter32
_AccCompressPhysStatOctetsOuts_Object = MibTableColumn
accCompressPhysStatOctetsOuts = _AccCompressPhysStatOctetsOuts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 7, 1, 4),
    _AccCompressPhysStatOctetsOuts_Type()
)
accCompressPhysStatOctetsOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressPhysStatOctetsOuts.setStatus("mandatory")
_AccCompressPhysStatPacketsIns_Type = Counter32
_AccCompressPhysStatPacketsIns_Object = MibTableColumn
accCompressPhysStatPacketsIns = _AccCompressPhysStatPacketsIns_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 7, 1, 5),
    _AccCompressPhysStatPacketsIns_Type()
)
accCompressPhysStatPacketsIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressPhysStatPacketsIns.setStatus("mandatory")
_AccCompressPhysStatPacketsOuts_Type = Counter32
_AccCompressPhysStatPacketsOuts_Object = MibTableColumn
accCompressPhysStatPacketsOuts = _AccCompressPhysStatPacketsOuts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 7, 1, 6),
    _AccCompressPhysStatPacketsOuts_Type()
)
accCompressPhysStatPacketsOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressPhysStatPacketsOuts.setStatus("mandatory")
_AccCompressPhysStatUnCompIns_Type = Counter32
_AccCompressPhysStatUnCompIns_Object = MibTableColumn
accCompressPhysStatUnCompIns = _AccCompressPhysStatUnCompIns_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 7, 1, 7),
    _AccCompressPhysStatUnCompIns_Type()
)
accCompressPhysStatUnCompIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressPhysStatUnCompIns.setStatus("mandatory")
_AccCompressPhysStatUnCompOuts_Type = Counter32
_AccCompressPhysStatUnCompOuts_Object = MibTableColumn
accCompressPhysStatUnCompOuts = _AccCompressPhysStatUnCompOuts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 7, 1, 8),
    _AccCompressPhysStatUnCompOuts_Type()
)
accCompressPhysStatUnCompOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressPhysStatUnCompOuts.setStatus("mandatory")
_AccCompressPhysStatAvgCompIn_Type = Gauge32
_AccCompressPhysStatAvgCompIn_Object = MibTableColumn
accCompressPhysStatAvgCompIn = _AccCompressPhysStatAvgCompIn_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 7, 1, 9),
    _AccCompressPhysStatAvgCompIn_Type()
)
accCompressPhysStatAvgCompIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressPhysStatAvgCompIn.setStatus("mandatory")
_AccCompressPhysStatAvgCompOut_Type = Gauge32
_AccCompressPhysStatAvgCompOut_Object = MibTableColumn
accCompressPhysStatAvgCompOut = _AccCompressPhysStatAvgCompOut_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 7, 1, 10),
    _AccCompressPhysStatAvgCompOut_Type()
)
accCompressPhysStatAvgCompOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressPhysStatAvgCompOut.setStatus("mandatory")
_AccCompressPhysStatHdrErrors_Type = Counter32
_AccCompressPhysStatHdrErrors_Object = MibTableColumn
accCompressPhysStatHdrErrors = _AccCompressPhysStatHdrErrors_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 7, 1, 11),
    _AccCompressPhysStatHdrErrors_Type()
)
accCompressPhysStatHdrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressPhysStatHdrErrors.setStatus("mandatory")
_AccCompressPhysStatResyncs_Type = Counter32
_AccCompressPhysStatResyncs_Object = MibTableColumn
accCompressPhysStatResyncs = _AccCompressPhysStatResyncs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 7, 1, 12),
    _AccCompressPhysStatResyncs_Type()
)
accCompressPhysStatResyncs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressPhysStatResyncs.setStatus("mandatory")
_AccCompressPhysStatNoEndMarks_Type = Counter32
_AccCompressPhysStatNoEndMarks_Object = MibTableColumn
accCompressPhysStatNoEndMarks = _AccCompressPhysStatNoEndMarks_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 7, 1, 13),
    _AccCompressPhysStatNoEndMarks_Type()
)
accCompressPhysStatNoEndMarks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressPhysStatNoEndMarks.setStatus("mandatory")
_AccCompressPhysStatNoBufAvails_Type = Counter32
_AccCompressPhysStatNoBufAvails_Object = MibTableColumn
accCompressPhysStatNoBufAvails = _AccCompressPhysStatNoBufAvails_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 7, 1, 14),
    _AccCompressPhysStatNoBufAvails_Type()
)
accCompressPhysStatNoBufAvails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressPhysStatNoBufAvails.setStatus("mandatory")


class _AccCompressPhysStatusInStats_Type(Integer32):
    """Custom type accCompressPhysStatusInStats based on Integer32"""
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
        *(("conn", 2),
          ("disc", 1),
          ("resync", 4),
          ("sync", 3))
    )


_AccCompressPhysStatusInStats_Type.__name__ = "Integer32"
_AccCompressPhysStatusInStats_Object = MibTableColumn
accCompressPhysStatusInStats = _AccCompressPhysStatusInStats_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 7, 1, 15),
    _AccCompressPhysStatusInStats_Type()
)
accCompressPhysStatusInStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressPhysStatusInStats.setStatus("mandatory")


class _AccCompressPhysStatusOutStats_Type(Integer32):
    """Custom type accCompressPhysStatusOutStats based on Integer32"""
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
        *(("conn", 2),
          ("disc", 1),
          ("resync", 4),
          ("sync", 3))
    )


_AccCompressPhysStatusOutStats_Type.__name__ = "Integer32"
_AccCompressPhysStatusOutStats_Object = MibTableColumn
accCompressPhysStatusOutStats = _AccCompressPhysStatusOutStats_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 7, 1, 16),
    _AccCompressPhysStatusOutStats_Type()
)
accCompressPhysStatusOutStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressPhysStatusOutStats.setStatus("mandatory")
_AccCompressPhysExpandInStats_Type = Counter32
_AccCompressPhysExpandInStats_Object = MibTableColumn
accCompressPhysExpandInStats = _AccCompressPhysExpandInStats_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 7, 1, 17),
    _AccCompressPhysExpandInStats_Type()
)
accCompressPhysExpandInStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressPhysExpandInStats.setStatus("mandatory")
_AccCompressPhysExpandOutStats_Type = Counter32
_AccCompressPhysExpandOutStats_Object = MibTableColumn
accCompressPhysExpandOutStats = _AccCompressPhysExpandOutStats_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 7, 1, 18),
    _AccCompressPhysExpandOutStats_Type()
)
accCompressPhysExpandOutStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressPhysExpandOutStats.setStatus("mandatory")
_AccCompressPhysDiscardInStats_Type = Counter32
_AccCompressPhysDiscardInStats_Object = MibTableColumn
accCompressPhysDiscardInStats = _AccCompressPhysDiscardInStats_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 7, 1, 19),
    _AccCompressPhysDiscardInStats_Type()
)
accCompressPhysDiscardInStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressPhysDiscardInStats.setStatus("mandatory")
_AccCompressPhysDiscardOutStats_Type = Counter32
_AccCompressPhysDiscardOutStats_Object = MibTableColumn
accCompressPhysDiscardOutStats = _AccCompressPhysDiscardOutStats_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 7, 1, 20),
    _AccCompressPhysDiscardOutStats_Type()
)
accCompressPhysDiscardOutStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressPhysDiscardOutStats.setStatus("mandatory")
_AccCompressSmdsNeighborTable_Object = MibTable
accCompressSmdsNeighborTable = _AccCompressSmdsNeighborTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 8)
)
if mibBuilder.loadTexts:
    accCompressSmdsNeighborTable.setStatus("mandatory")
_AccCompressSmdsNeighborEntry_Object = MibTableRow
accCompressSmdsNeighborEntry = _AccCompressSmdsNeighborEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 8, 1)
)
accCompressSmdsNeighborEntry.setIndexNames(
    (0, "ACC-COMPRESS", "accCompressSmdsNeighborIfIndex"),
    (0, "ACC-COMPRESS", "accCompressSmdsNeighborSNI"),
)
if mibBuilder.loadTexts:
    accCompressSmdsNeighborEntry.setStatus("mandatory")
_AccCompressSmdsNeighborIfIndex_Type = Integer32
_AccCompressSmdsNeighborIfIndex_Object = MibTableColumn
accCompressSmdsNeighborIfIndex = _AccCompressSmdsNeighborIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 8, 1, 1),
    _AccCompressSmdsNeighborIfIndex_Type()
)
accCompressSmdsNeighborIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressSmdsNeighborIfIndex.setStatus("mandatory")
_AccCompressSmdsNeighborSNI_Type = SmdsAddress
_AccCompressSmdsNeighborSNI_Object = MibTableColumn
accCompressSmdsNeighborSNI = _AccCompressSmdsNeighborSNI_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 8, 1, 2),
    _AccCompressSmdsNeighborSNI_Type()
)
accCompressSmdsNeighborSNI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressSmdsNeighborSNI.setStatus("mandatory")


class _AccCompressSmdsNeighborStatus_Type(Integer32):
    """Custom type accCompressSmdsNeighborStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              128)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 128),
          ("off", 1),
          ("on", 2))
    )


_AccCompressSmdsNeighborStatus_Type.__name__ = "Integer32"
_AccCompressSmdsNeighborStatus_Object = MibTableColumn
accCompressSmdsNeighborStatus = _AccCompressSmdsNeighborStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 8, 1, 3),
    _AccCompressSmdsNeighborStatus_Type()
)
accCompressSmdsNeighborStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accCompressSmdsNeighborStatus.setStatus("mandatory")
_AccCompressSmdsNeighborRowStatus_Type = RowStatus
_AccCompressSmdsNeighborRowStatus_Object = MibTableColumn
accCompressSmdsNeighborRowStatus = _AccCompressSmdsNeighborRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 8, 1, 4),
    _AccCompressSmdsNeighborRowStatus_Type()
)
accCompressSmdsNeighborRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accCompressSmdsNeighborRowStatus.setStatus("mandatory")
_AccCompressSmdsStatTable_Object = MibTable
accCompressSmdsStatTable = _AccCompressSmdsStatTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 9)
)
if mibBuilder.loadTexts:
    accCompressSmdsStatTable.setStatus("mandatory")
_AccCompressSmdsStatEntry_Object = MibTableRow
accCompressSmdsStatEntry = _AccCompressSmdsStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 9, 1)
)
accCompressSmdsStatEntry.setIndexNames(
    (0, "ACC-COMPRESS", "accCompressSmdsStatIfIndex"),
    (0, "ACC-COMPRESS", "accCompressSmdsStatSNI"),
)
if mibBuilder.loadTexts:
    accCompressSmdsStatEntry.setStatus("mandatory")
_AccCompressSmdsStatIfIndex_Type = Integer32
_AccCompressSmdsStatIfIndex_Object = MibTableColumn
accCompressSmdsStatIfIndex = _AccCompressSmdsStatIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 9, 1, 1),
    _AccCompressSmdsStatIfIndex_Type()
)
accCompressSmdsStatIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressSmdsStatIfIndex.setStatus("mandatory")
_AccCompressSmdsStatSNI_Type = SmdsAddress
_AccCompressSmdsStatSNI_Object = MibTableColumn
accCompressSmdsStatSNI = _AccCompressSmdsStatSNI_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 9, 1, 2),
    _AccCompressSmdsStatSNI_Type()
)
accCompressSmdsStatSNI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accCompressSmdsStatSNI.setStatus("mandatory")


class _AccCompressSmdsStatStatus_Type(Integer32):
    """Custom type accCompressSmdsStatStatus based on Integer32"""
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
        *(("conn", 2),
          ("disc", 1),
          ("resync", 4),
          ("sync", 3))
    )


_AccCompressSmdsStatStatus_Type.__name__ = "Integer32"
_AccCompressSmdsStatStatus_Object = MibTableColumn
accCompressSmdsStatStatus = _AccCompressSmdsStatStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 9, 1, 3),
    _AccCompressSmdsStatStatus_Type()
)
accCompressSmdsStatStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressSmdsStatStatus.setStatus("mandatory")
_AccCompressSmdsStatOctetsIns_Type = Counter32
_AccCompressSmdsStatOctetsIns_Object = MibTableColumn
accCompressSmdsStatOctetsIns = _AccCompressSmdsStatOctetsIns_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 9, 1, 4),
    _AccCompressSmdsStatOctetsIns_Type()
)
accCompressSmdsStatOctetsIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressSmdsStatOctetsIns.setStatus("mandatory")
_AccCompressSmdsStatOctetsOuts_Type = Counter32
_AccCompressSmdsStatOctetsOuts_Object = MibTableColumn
accCompressSmdsStatOctetsOuts = _AccCompressSmdsStatOctetsOuts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 9, 1, 5),
    _AccCompressSmdsStatOctetsOuts_Type()
)
accCompressSmdsStatOctetsOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressSmdsStatOctetsOuts.setStatus("mandatory")
_AccCompressSmdsStatPacketsIns_Type = Counter32
_AccCompressSmdsStatPacketsIns_Object = MibTableColumn
accCompressSmdsStatPacketsIns = _AccCompressSmdsStatPacketsIns_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 9, 1, 6),
    _AccCompressSmdsStatPacketsIns_Type()
)
accCompressSmdsStatPacketsIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressSmdsStatPacketsIns.setStatus("mandatory")
_AccCompressSmdsStatPacketsOuts_Type = Counter32
_AccCompressSmdsStatPacketsOuts_Object = MibTableColumn
accCompressSmdsStatPacketsOuts = _AccCompressSmdsStatPacketsOuts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 9, 1, 7),
    _AccCompressSmdsStatPacketsOuts_Type()
)
accCompressSmdsStatPacketsOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressSmdsStatPacketsOuts.setStatus("mandatory")
_AccCompressSmdsStatUnCompIns_Type = Counter32
_AccCompressSmdsStatUnCompIns_Object = MibTableColumn
accCompressSmdsStatUnCompIns = _AccCompressSmdsStatUnCompIns_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 9, 1, 8),
    _AccCompressSmdsStatUnCompIns_Type()
)
accCompressSmdsStatUnCompIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressSmdsStatUnCompIns.setStatus("mandatory")
_AccCompressSmdsStatUnCompOuts_Type = Counter32
_AccCompressSmdsStatUnCompOuts_Object = MibTableColumn
accCompressSmdsStatUnCompOuts = _AccCompressSmdsStatUnCompOuts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 9, 1, 9),
    _AccCompressSmdsStatUnCompOuts_Type()
)
accCompressSmdsStatUnCompOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressSmdsStatUnCompOuts.setStatus("mandatory")
_AccCompressSmdsStatAvgCompIn_Type = Gauge32
_AccCompressSmdsStatAvgCompIn_Object = MibTableColumn
accCompressSmdsStatAvgCompIn = _AccCompressSmdsStatAvgCompIn_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 9, 1, 10),
    _AccCompressSmdsStatAvgCompIn_Type()
)
accCompressSmdsStatAvgCompIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressSmdsStatAvgCompIn.setStatus("mandatory")
_AccCompressSmdsStatAvgCompOut_Type = Gauge32
_AccCompressSmdsStatAvgCompOut_Object = MibTableColumn
accCompressSmdsStatAvgCompOut = _AccCompressSmdsStatAvgCompOut_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 9, 1, 11),
    _AccCompressSmdsStatAvgCompOut_Type()
)
accCompressSmdsStatAvgCompOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressSmdsStatAvgCompOut.setStatus("mandatory")
_AccCompressSmdsStatHdrErrors_Type = Counter32
_AccCompressSmdsStatHdrErrors_Object = MibTableColumn
accCompressSmdsStatHdrErrors = _AccCompressSmdsStatHdrErrors_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 9, 1, 12),
    _AccCompressSmdsStatHdrErrors_Type()
)
accCompressSmdsStatHdrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressSmdsStatHdrErrors.setStatus("mandatory")
_AccCompressSmdsStatResyncs_Type = Counter32
_AccCompressSmdsStatResyncs_Object = MibTableColumn
accCompressSmdsStatResyncs = _AccCompressSmdsStatResyncs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 9, 1, 13),
    _AccCompressSmdsStatResyncs_Type()
)
accCompressSmdsStatResyncs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressSmdsStatResyncs.setStatus("mandatory")
_AccCompressSmdsStatNoEndMarks_Type = Counter32
_AccCompressSmdsStatNoEndMarks_Object = MibTableColumn
accCompressSmdsStatNoEndMarks = _AccCompressSmdsStatNoEndMarks_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 9, 1, 14),
    _AccCompressSmdsStatNoEndMarks_Type()
)
accCompressSmdsStatNoEndMarks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressSmdsStatNoEndMarks.setStatus("mandatory")
_AccCompressSmdsStatNoBufAvails_Type = Counter32
_AccCompressSmdsStatNoBufAvails_Object = MibTableColumn
accCompressSmdsStatNoBufAvails = _AccCompressSmdsStatNoBufAvails_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 9, 1, 15),
    _AccCompressSmdsStatNoBufAvails_Type()
)
accCompressSmdsStatNoBufAvails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressSmdsStatNoBufAvails.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ACC-COMPRESS",
    **{"accCompress": accCompress,
       "accCompressDialNeighborTable": accCompressDialNeighborTable,
       "accCompressDialNeighborEntry": accCompressDialNeighborEntry,
       "accCompressDialNeighborIfIndex": accCompressDialNeighborIfIndex,
       "accCompressDialNeighborCallAddress": accCompressDialNeighborCallAddress,
       "accCompressDialNeighborStatus": accCompressDialNeighborStatus,
       "accCompressFfrNeighborTable": accCompressFfrNeighborTable,
       "accCompressFfrNeighborEntry": accCompressFfrNeighborEntry,
       "accCompressFfrNeighborIfIndex": accCompressFfrNeighborIfIndex,
       "accCompressFfrNeighborDlci": accCompressFfrNeighborDlci,
       "accCompressFfrNeighborStatus": accCompressFfrNeighborStatus,
       "accCompressX25NeighborTable": accCompressX25NeighborTable,
       "accCompressX25NeighborEntry": accCompressX25NeighborEntry,
       "accCompressX25NeighborIfIndex": accCompressX25NeighborIfIndex,
       "accCompressX25NeighborAddress": accCompressX25NeighborAddress,
       "accCompressX25NeighborStatus": accCompressX25NeighborStatus,
       "accCompressDialStatTable": accCompressDialStatTable,
       "accCompressDialStatEntry": accCompressDialStatEntry,
       "accCompressDialStatIfIndex": accCompressDialStatIfIndex,
       "accCompressDialStatCallAddress": accCompressDialStatCallAddress,
       "accCompressDialStatStatus": accCompressDialStatStatus,
       "accCompressDialStatOctetsIns": accCompressDialStatOctetsIns,
       "accCompressDialStatOctetsOuts": accCompressDialStatOctetsOuts,
       "accCompressDialStatPacketsIns": accCompressDialStatPacketsIns,
       "accCompressDialStatPacketsOuts": accCompressDialStatPacketsOuts,
       "accCompressDialStatUnCompIns": accCompressDialStatUnCompIns,
       "accCompressDialStatUnCompOuts": accCompressDialStatUnCompOuts,
       "accCompressDialStatAvgCompIn": accCompressDialStatAvgCompIn,
       "accCompressDialStatAvgCompOut": accCompressDialStatAvgCompOut,
       "accCompressDialStatHdrErrors": accCompressDialStatHdrErrors,
       "accCompressDialStatResyncs": accCompressDialStatResyncs,
       "accCompressDialStatNoEndMarks": accCompressDialStatNoEndMarks,
       "accCompressDialStatNoBufAvails": accCompressDialStatNoBufAvails,
       "accCompressFfrStatTable": accCompressFfrStatTable,
       "accCompressFfrStatEntry": accCompressFfrStatEntry,
       "accCompressFfrStatIfIndex": accCompressFfrStatIfIndex,
       "accCompressFfrStatDlci": accCompressFfrStatDlci,
       "accCompressFfrStatStatus": accCompressFfrStatStatus,
       "accCompressFfrStatOctetsIns": accCompressFfrStatOctetsIns,
       "accCompressFfrStatOctetsOuts": accCompressFfrStatOctetsOuts,
       "accCompressFfrStatPacketsIns": accCompressFfrStatPacketsIns,
       "accCompressFfrStatPacketsOuts": accCompressFfrStatPacketsOuts,
       "accCompressFfrStatUnCompIns": accCompressFfrStatUnCompIns,
       "accCompressFfrStatUnCompOuts": accCompressFfrStatUnCompOuts,
       "accCompressFfrStatAvgCompIn": accCompressFfrStatAvgCompIn,
       "accCompressFfrStatAvgCompOut": accCompressFfrStatAvgCompOut,
       "accCompressFfrStatHdrErrors": accCompressFfrStatHdrErrors,
       "accCompressFfrStatResyncs": accCompressFfrStatResyncs,
       "accCompressFfrStatNoEndMarks": accCompressFfrStatNoEndMarks,
       "accCompressFfrStatNoBufAvails": accCompressFfrStatNoBufAvails,
       "accCompressX25StatTable": accCompressX25StatTable,
       "accCompressX25StatEntry": accCompressX25StatEntry,
       "accCompressX25StatIfIndex": accCompressX25StatIfIndex,
       "accCompressX25StatAddress": accCompressX25StatAddress,
       "accCompressX25StatStatus": accCompressX25StatStatus,
       "accCompressX25StatOctetsIns": accCompressX25StatOctetsIns,
       "accCompressX25StatOctetsOuts": accCompressX25StatOctetsOuts,
       "accCompressX25StatPacketsIns": accCompressX25StatPacketsIns,
       "accCompressX25StatPacketsOuts": accCompressX25StatPacketsOuts,
       "accCompressX25StatUnCompIns": accCompressX25StatUnCompIns,
       "accCompressX25StatUnCompOuts": accCompressX25StatUnCompOuts,
       "accCompressX25StatAvgCompIn": accCompressX25StatAvgCompIn,
       "accCompressX25StatAvgCompOut": accCompressX25StatAvgCompOut,
       "accCompressX25StatHdrErrors": accCompressX25StatHdrErrors,
       "accCompressX25StatResyncs": accCompressX25StatResyncs,
       "accCompressX25StatNoEndMarks": accCompressX25StatNoEndMarks,
       "accCompressX25StatNoBufAvails": accCompressX25StatNoBufAvails,
       "accCompressPhysStatTable": accCompressPhysStatTable,
       "accCompressPhysStatEntry": accCompressPhysStatEntry,
       "accCompressPhysStatIfIndex": accCompressPhysStatIfIndex,
       "accCompressPhysStatStatus": accCompressPhysStatStatus,
       "accCompressPhysStatOctetsIns": accCompressPhysStatOctetsIns,
       "accCompressPhysStatOctetsOuts": accCompressPhysStatOctetsOuts,
       "accCompressPhysStatPacketsIns": accCompressPhysStatPacketsIns,
       "accCompressPhysStatPacketsOuts": accCompressPhysStatPacketsOuts,
       "accCompressPhysStatUnCompIns": accCompressPhysStatUnCompIns,
       "accCompressPhysStatUnCompOuts": accCompressPhysStatUnCompOuts,
       "accCompressPhysStatAvgCompIn": accCompressPhysStatAvgCompIn,
       "accCompressPhysStatAvgCompOut": accCompressPhysStatAvgCompOut,
       "accCompressPhysStatHdrErrors": accCompressPhysStatHdrErrors,
       "accCompressPhysStatResyncs": accCompressPhysStatResyncs,
       "accCompressPhysStatNoEndMarks": accCompressPhysStatNoEndMarks,
       "accCompressPhysStatNoBufAvails": accCompressPhysStatNoBufAvails,
       "accCompressPhysStatusInStats": accCompressPhysStatusInStats,
       "accCompressPhysStatusOutStats": accCompressPhysStatusOutStats,
       "accCompressPhysExpandInStats": accCompressPhysExpandInStats,
       "accCompressPhysExpandOutStats": accCompressPhysExpandOutStats,
       "accCompressPhysDiscardInStats": accCompressPhysDiscardInStats,
       "accCompressPhysDiscardOutStats": accCompressPhysDiscardOutStats,
       "accCompressSmdsNeighborTable": accCompressSmdsNeighborTable,
       "accCompressSmdsNeighborEntry": accCompressSmdsNeighborEntry,
       "accCompressSmdsNeighborIfIndex": accCompressSmdsNeighborIfIndex,
       "accCompressSmdsNeighborSNI": accCompressSmdsNeighborSNI,
       "accCompressSmdsNeighborStatus": accCompressSmdsNeighborStatus,
       "accCompressSmdsNeighborRowStatus": accCompressSmdsNeighborRowStatus,
       "accCompressSmdsStatTable": accCompressSmdsStatTable,
       "accCompressSmdsStatEntry": accCompressSmdsStatEntry,
       "accCompressSmdsStatIfIndex": accCompressSmdsStatIfIndex,
       "accCompressSmdsStatSNI": accCompressSmdsStatSNI,
       "accCompressSmdsStatStatus": accCompressSmdsStatStatus,
       "accCompressSmdsStatOctetsIns": accCompressSmdsStatOctetsIns,
       "accCompressSmdsStatOctetsOuts": accCompressSmdsStatOctetsOuts,
       "accCompressSmdsStatPacketsIns": accCompressSmdsStatPacketsIns,
       "accCompressSmdsStatPacketsOuts": accCompressSmdsStatPacketsOuts,
       "accCompressSmdsStatUnCompIns": accCompressSmdsStatUnCompIns,
       "accCompressSmdsStatUnCompOuts": accCompressSmdsStatUnCompOuts,
       "accCompressSmdsStatAvgCompIn": accCompressSmdsStatAvgCompIn,
       "accCompressSmdsStatAvgCompOut": accCompressSmdsStatAvgCompOut,
       "accCompressSmdsStatHdrErrors": accCompressSmdsStatHdrErrors,
       "accCompressSmdsStatResyncs": accCompressSmdsStatResyncs,
       "accCompressSmdsStatNoEndMarks": accCompressSmdsStatNoEndMarks,
       "accCompressSmdsStatNoBufAvails": accCompressSmdsStatNoBufAvails}
)
