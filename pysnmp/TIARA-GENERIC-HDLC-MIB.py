# SNMP MIB module (TIARA-GENERIC-HDLC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TIARA-GENERIC-HDLC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:01:34 2024
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

(bundleId,) = mibBuilder.importSymbols(
    "TIARA-BUNDLE-MIB",
    "bundleId")

(tiaraMgmt,) = mibBuilder.importSymbols(
    "TIARA-NETWORKS-SMI",
    "tiaraMgmt")


# MODULE-IDENTITY

tiaraGenHdlcMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3174, 2, 15)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_GenHdlcTable_Object = MibTable
genHdlcTable = _GenHdlcTable_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 15, 1)
)
if mibBuilder.loadTexts:
    genHdlcTable.setStatus("current")
_GenHdlcTableEntry_Object = MibTableRow
genHdlcTableEntry = _GenHdlcTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 15, 1, 1)
)
genHdlcTableEntry.setIndexNames(
    (0, "TIARA-BUNDLE-MIB", "bundleId"),
)
if mibBuilder.loadTexts:
    genHdlcTableEntry.setStatus("current")


class _GenHdlcKeepAlive_Type(Integer32):
    """Custom type genHdlcKeepAlive based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_GenHdlcKeepAlive_Type.__name__ = "Integer32"
_GenHdlcKeepAlive_Object = MibTableColumn
genHdlcKeepAlive = _GenHdlcKeepAlive_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 15, 1, 1, 1),
    _GenHdlcKeepAlive_Type()
)
genHdlcKeepAlive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genHdlcKeepAlive.setStatus("current")
if mibBuilder.loadTexts:
    genHdlcKeepAlive.setUnits("seconds")


class _GenHdlcMtu_Type(Integer32):
    """Custom type genHdlcMtu based on Integer32"""
    defaultValue = 1500


_GenHdlcMtu_Object = MibTableColumn
genHdlcMtu = _GenHdlcMtu_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 15, 1, 1, 2),
    _GenHdlcMtu_Type()
)
genHdlcMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genHdlcMtu.setStatus("current")
_GenHdlcStatsTable_Object = MibTable
genHdlcStatsTable = _GenHdlcStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 15, 2)
)
if mibBuilder.loadTexts:
    genHdlcStatsTable.setStatus("current")
_GenHdlcStatsTableEntry_Object = MibTableRow
genHdlcStatsTableEntry = _GenHdlcStatsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 15, 2, 1)
)
genHdlcStatsTableEntry.setIndexNames(
    (0, "TIARA-BUNDLE-MIB", "bundleId"),
)
if mibBuilder.loadTexts:
    genHdlcStatsTableEntry.setStatus("current")
_GenHdlcStatsBytesRxLastBootClear_Type = Counter32
_GenHdlcStatsBytesRxLastBootClear_Object = MibTableColumn
genHdlcStatsBytesRxLastBootClear = _GenHdlcStatsBytesRxLastBootClear_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 15, 2, 1, 1),
    _GenHdlcStatsBytesRxLastBootClear_Type()
)
genHdlcStatsBytesRxLastBootClear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genHdlcStatsBytesRxLastBootClear.setStatus("current")
_GenHdlcStatsBytesTxLastBootClear_Type = Counter32
_GenHdlcStatsBytesTxLastBootClear_Object = MibTableColumn
genHdlcStatsBytesTxLastBootClear = _GenHdlcStatsBytesTxLastBootClear_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 15, 2, 1, 2),
    _GenHdlcStatsBytesTxLastBootClear_Type()
)
genHdlcStatsBytesTxLastBootClear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genHdlcStatsBytesTxLastBootClear.setStatus("current")
_GenHdlcStatsPktsRxLastBootClear_Type = Counter32
_GenHdlcStatsPktsRxLastBootClear_Object = MibTableColumn
genHdlcStatsPktsRxLastBootClear = _GenHdlcStatsPktsRxLastBootClear_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 15, 2, 1, 3),
    _GenHdlcStatsPktsRxLastBootClear_Type()
)
genHdlcStatsPktsRxLastBootClear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genHdlcStatsPktsRxLastBootClear.setStatus("current")
_GenHdlcStatsPktsTxLastBootClear_Type = Counter32
_GenHdlcStatsPktsTxLastBootClear_Object = MibTableColumn
genHdlcStatsPktsTxLastBootClear = _GenHdlcStatsPktsTxLastBootClear_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 15, 2, 1, 4),
    _GenHdlcStatsPktsTxLastBootClear_Type()
)
genHdlcStatsPktsTxLastBootClear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genHdlcStatsPktsTxLastBootClear.setStatus("current")
_GenHdlcStatsErrPktsRxLastBootClear_Type = Counter32
_GenHdlcStatsErrPktsRxLastBootClear_Object = MibTableColumn
genHdlcStatsErrPktsRxLastBootClear = _GenHdlcStatsErrPktsRxLastBootClear_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 15, 2, 1, 5),
    _GenHdlcStatsErrPktsRxLastBootClear_Type()
)
genHdlcStatsErrPktsRxLastBootClear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genHdlcStatsErrPktsRxLastBootClear.setStatus("current")
_GenHdlcStatsUpDownStatesLastBootClear_Type = Counter32
_GenHdlcStatsUpDownStatesLastBootClear_Object = MibTableColumn
genHdlcStatsUpDownStatesLastBootClear = _GenHdlcStatsUpDownStatesLastBootClear_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 15, 2, 1, 6),
    _GenHdlcStatsUpDownStatesLastBootClear_Type()
)
genHdlcStatsUpDownStatesLastBootClear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genHdlcStatsUpDownStatesLastBootClear.setStatus("current")
_GenHdlcStatsBytesRxLastFiveMins_Type = Counter32
_GenHdlcStatsBytesRxLastFiveMins_Object = MibTableColumn
genHdlcStatsBytesRxLastFiveMins = _GenHdlcStatsBytesRxLastFiveMins_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 15, 2, 1, 7),
    _GenHdlcStatsBytesRxLastFiveMins_Type()
)
genHdlcStatsBytesRxLastFiveMins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genHdlcStatsBytesRxLastFiveMins.setStatus("current")
_GenHdlcStatsBytesTxLastFiveMins_Type = Counter32
_GenHdlcStatsBytesTxLastFiveMins_Object = MibTableColumn
genHdlcStatsBytesTxLastFiveMins = _GenHdlcStatsBytesTxLastFiveMins_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 15, 2, 1, 8),
    _GenHdlcStatsBytesTxLastFiveMins_Type()
)
genHdlcStatsBytesTxLastFiveMins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genHdlcStatsBytesTxLastFiveMins.setStatus("current")
_GenHdlcStatsPktsRxLastFiveMins_Type = Counter32
_GenHdlcStatsPktsRxLastFiveMins_Object = MibTableColumn
genHdlcStatsPktsRxLastFiveMins = _GenHdlcStatsPktsRxLastFiveMins_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 15, 2, 1, 9),
    _GenHdlcStatsPktsRxLastFiveMins_Type()
)
genHdlcStatsPktsRxLastFiveMins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genHdlcStatsPktsRxLastFiveMins.setStatus("current")
_GenHdlcStatsPktsTxLastFiveMins_Type = Counter32
_GenHdlcStatsPktsTxLastFiveMins_Object = MibTableColumn
genHdlcStatsPktsTxLastFiveMins = _GenHdlcStatsPktsTxLastFiveMins_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 15, 2, 1, 10),
    _GenHdlcStatsPktsTxLastFiveMins_Type()
)
genHdlcStatsPktsTxLastFiveMins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genHdlcStatsPktsTxLastFiveMins.setStatus("current")
_GenHdlcStatsErrPktsRxLastFiveMins_Type = Counter32
_GenHdlcStatsErrPktsRxLastFiveMins_Object = MibTableColumn
genHdlcStatsErrPktsRxLastFiveMins = _GenHdlcStatsErrPktsRxLastFiveMins_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 15, 2, 1, 11),
    _GenHdlcStatsErrPktsRxLastFiveMins_Type()
)
genHdlcStatsErrPktsRxLastFiveMins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genHdlcStatsErrPktsRxLastFiveMins.setStatus("current")
_GenHdlcStatsUpDownStatesLastFiveMins_Type = Counter32
_GenHdlcStatsUpDownStatesLastFiveMins_Object = MibTableColumn
genHdlcStatsUpDownStatesLastFiveMins = _GenHdlcStatsUpDownStatesLastFiveMins_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 15, 2, 1, 12),
    _GenHdlcStatsUpDownStatesLastFiveMins_Type()
)
genHdlcStatsUpDownStatesLastFiveMins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genHdlcStatsUpDownStatesLastFiveMins.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIARA-GENERIC-HDLC-MIB",
    **{"tiaraGenHdlcMib": tiaraGenHdlcMib,
       "genHdlcTable": genHdlcTable,
       "genHdlcTableEntry": genHdlcTableEntry,
       "genHdlcKeepAlive": genHdlcKeepAlive,
       "genHdlcMtu": genHdlcMtu,
       "genHdlcStatsTable": genHdlcStatsTable,
       "genHdlcStatsTableEntry": genHdlcStatsTableEntry,
       "genHdlcStatsBytesRxLastBootClear": genHdlcStatsBytesRxLastBootClear,
       "genHdlcStatsBytesTxLastBootClear": genHdlcStatsBytesTxLastBootClear,
       "genHdlcStatsPktsRxLastBootClear": genHdlcStatsPktsRxLastBootClear,
       "genHdlcStatsPktsTxLastBootClear": genHdlcStatsPktsTxLastBootClear,
       "genHdlcStatsErrPktsRxLastBootClear": genHdlcStatsErrPktsRxLastBootClear,
       "genHdlcStatsUpDownStatesLastBootClear": genHdlcStatsUpDownStatesLastBootClear,
       "genHdlcStatsBytesRxLastFiveMins": genHdlcStatsBytesRxLastFiveMins,
       "genHdlcStatsBytesTxLastFiveMins": genHdlcStatsBytesTxLastFiveMins,
       "genHdlcStatsPktsRxLastFiveMins": genHdlcStatsPktsRxLastFiveMins,
       "genHdlcStatsPktsTxLastFiveMins": genHdlcStatsPktsTxLastFiveMins,
       "genHdlcStatsErrPktsRxLastFiveMins": genHdlcStatsErrPktsRxLastFiveMins,
       "genHdlcStatsUpDownStatesLastFiveMins": genHdlcStatsUpDownStatesLastFiveMins}
)
