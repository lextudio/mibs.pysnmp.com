# SNMP MIB module (GENERIC-HDLC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/GENERIC-HDLC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:48:31 2024
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

(nnbundleId,) = mibBuilder.importSymbols(
    "BUNDLE-MIB",
    "nnbundleId")

(ntEnterpriseDataTasmanMgmt,) = mibBuilder.importSymbols(
    "NT-ENTERPRISE-DATA-MIB",
    "ntEnterpriseDataTasmanMgmt")

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

nngenHdlcMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 15)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NngenHdlcTable_Object = MibTable
nngenHdlcTable = _NngenHdlcTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 15, 1)
)
if mibBuilder.loadTexts:
    nngenHdlcTable.setStatus("current")
_NngenHdlcTableEntry_Object = MibTableRow
nngenHdlcTableEntry = _NngenHdlcTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 15, 1, 1)
)
nngenHdlcTableEntry.setIndexNames(
    (0, "BUNDLE-MIB", "nnbundleId"),
)
if mibBuilder.loadTexts:
    nngenHdlcTableEntry.setStatus("current")


class _NngenHdlcKeepAlive_Type(Integer32):
    """Custom type nngenHdlcKeepAlive based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_NngenHdlcKeepAlive_Type.__name__ = "Integer32"
_NngenHdlcKeepAlive_Object = MibTableColumn
nngenHdlcKeepAlive = _NngenHdlcKeepAlive_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 15, 1, 1, 1),
    _NngenHdlcKeepAlive_Type()
)
nngenHdlcKeepAlive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nngenHdlcKeepAlive.setStatus("current")
if mibBuilder.loadTexts:
    nngenHdlcKeepAlive.setUnits("seconds")


class _NngenHdlcMtu_Type(Integer32):
    """Custom type nngenHdlcMtu based on Integer32"""
    defaultValue = 1500


_NngenHdlcMtu_Object = MibTableColumn
nngenHdlcMtu = _NngenHdlcMtu_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 15, 1, 1, 2),
    _NngenHdlcMtu_Type()
)
nngenHdlcMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nngenHdlcMtu.setStatus("current")
_NngenHdlcStatsTable_Object = MibTable
nngenHdlcStatsTable = _NngenHdlcStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 15, 2)
)
if mibBuilder.loadTexts:
    nngenHdlcStatsTable.setStatus("current")
_NngenHdlcStatsTableEntry_Object = MibTableRow
nngenHdlcStatsTableEntry = _NngenHdlcStatsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 15, 2, 1)
)
nngenHdlcStatsTableEntry.setIndexNames(
    (0, "BUNDLE-MIB", "nnbundleId"),
)
if mibBuilder.loadTexts:
    nngenHdlcStatsTableEntry.setStatus("current")
_NngenHdlcStatsBytesRxLastBootClear_Type = Counter32
_NngenHdlcStatsBytesRxLastBootClear_Object = MibTableColumn
nngenHdlcStatsBytesRxLastBootClear = _NngenHdlcStatsBytesRxLastBootClear_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 15, 2, 1, 1),
    _NngenHdlcStatsBytesRxLastBootClear_Type()
)
nngenHdlcStatsBytesRxLastBootClear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nngenHdlcStatsBytesRxLastBootClear.setStatus("current")
_NngenHdlcStatsBytesTxLastBootClear_Type = Counter32
_NngenHdlcStatsBytesTxLastBootClear_Object = MibTableColumn
nngenHdlcStatsBytesTxLastBootClear = _NngenHdlcStatsBytesTxLastBootClear_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 15, 2, 1, 2),
    _NngenHdlcStatsBytesTxLastBootClear_Type()
)
nngenHdlcStatsBytesTxLastBootClear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nngenHdlcStatsBytesTxLastBootClear.setStatus("current")
_NngenHdlcStatsPktsRxLastBootClear_Type = Counter32
_NngenHdlcStatsPktsRxLastBootClear_Object = MibTableColumn
nngenHdlcStatsPktsRxLastBootClear = _NngenHdlcStatsPktsRxLastBootClear_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 15, 2, 1, 3),
    _NngenHdlcStatsPktsRxLastBootClear_Type()
)
nngenHdlcStatsPktsRxLastBootClear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nngenHdlcStatsPktsRxLastBootClear.setStatus("current")
_NngenHdlcStatsPktsTxLastBootClear_Type = Counter32
_NngenHdlcStatsPktsTxLastBootClear_Object = MibTableColumn
nngenHdlcStatsPktsTxLastBootClear = _NngenHdlcStatsPktsTxLastBootClear_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 15, 2, 1, 4),
    _NngenHdlcStatsPktsTxLastBootClear_Type()
)
nngenHdlcStatsPktsTxLastBootClear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nngenHdlcStatsPktsTxLastBootClear.setStatus("current")
_NngenHdlcStatsErrPktsRxLastBootClear_Type = Counter32
_NngenHdlcStatsErrPktsRxLastBootClear_Object = MibTableColumn
nngenHdlcStatsErrPktsRxLastBootClear = _NngenHdlcStatsErrPktsRxLastBootClear_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 15, 2, 1, 5),
    _NngenHdlcStatsErrPktsRxLastBootClear_Type()
)
nngenHdlcStatsErrPktsRxLastBootClear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nngenHdlcStatsErrPktsRxLastBootClear.setStatus("current")
_NngenHdlcStatsUpDownStatesLastBootClear_Type = Counter32
_NngenHdlcStatsUpDownStatesLastBootClear_Object = MibTableColumn
nngenHdlcStatsUpDownStatesLastBootClear = _NngenHdlcStatsUpDownStatesLastBootClear_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 15, 2, 1, 6),
    _NngenHdlcStatsUpDownStatesLastBootClear_Type()
)
nngenHdlcStatsUpDownStatesLastBootClear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nngenHdlcStatsUpDownStatesLastBootClear.setStatus("current")
_NngenHdlcStatsBytesRxLastFiveMins_Type = Counter32
_NngenHdlcStatsBytesRxLastFiveMins_Object = MibTableColumn
nngenHdlcStatsBytesRxLastFiveMins = _NngenHdlcStatsBytesRxLastFiveMins_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 15, 2, 1, 7),
    _NngenHdlcStatsBytesRxLastFiveMins_Type()
)
nngenHdlcStatsBytesRxLastFiveMins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nngenHdlcStatsBytesRxLastFiveMins.setStatus("current")
_NngenHdlcStatsBytesTxLastFiveMins_Type = Counter32
_NngenHdlcStatsBytesTxLastFiveMins_Object = MibTableColumn
nngenHdlcStatsBytesTxLastFiveMins = _NngenHdlcStatsBytesTxLastFiveMins_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 15, 2, 1, 8),
    _NngenHdlcStatsBytesTxLastFiveMins_Type()
)
nngenHdlcStatsBytesTxLastFiveMins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nngenHdlcStatsBytesTxLastFiveMins.setStatus("current")
_NngenHdlcStatsPktsRxLastFiveMins_Type = Counter32
_NngenHdlcStatsPktsRxLastFiveMins_Object = MibTableColumn
nngenHdlcStatsPktsRxLastFiveMins = _NngenHdlcStatsPktsRxLastFiveMins_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 15, 2, 1, 9),
    _NngenHdlcStatsPktsRxLastFiveMins_Type()
)
nngenHdlcStatsPktsRxLastFiveMins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nngenHdlcStatsPktsRxLastFiveMins.setStatus("current")
_NngenHdlcStatsPktsTxLastFiveMins_Type = Counter32
_NngenHdlcStatsPktsTxLastFiveMins_Object = MibTableColumn
nngenHdlcStatsPktsTxLastFiveMins = _NngenHdlcStatsPktsTxLastFiveMins_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 15, 2, 1, 10),
    _NngenHdlcStatsPktsTxLastFiveMins_Type()
)
nngenHdlcStatsPktsTxLastFiveMins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nngenHdlcStatsPktsTxLastFiveMins.setStatus("current")
_NngenHdlcStatsErrPktsRxLastFiveMins_Type = Counter32
_NngenHdlcStatsErrPktsRxLastFiveMins_Object = MibTableColumn
nngenHdlcStatsErrPktsRxLastFiveMins = _NngenHdlcStatsErrPktsRxLastFiveMins_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 15, 2, 1, 11),
    _NngenHdlcStatsErrPktsRxLastFiveMins_Type()
)
nngenHdlcStatsErrPktsRxLastFiveMins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nngenHdlcStatsErrPktsRxLastFiveMins.setStatus("current")
_NngenHdlcStatsUpDownStatesLastFiveMins_Type = Counter32
_NngenHdlcStatsUpDownStatesLastFiveMins_Object = MibTableColumn
nngenHdlcStatsUpDownStatesLastFiveMins = _NngenHdlcStatsUpDownStatesLastFiveMins_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 15, 2, 1, 12),
    _NngenHdlcStatsUpDownStatesLastFiveMins_Type()
)
nngenHdlcStatsUpDownStatesLastFiveMins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nngenHdlcStatsUpDownStatesLastFiveMins.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GENERIC-HDLC-MIB",
    **{"nngenHdlcMib": nngenHdlcMib,
       "nngenHdlcTable": nngenHdlcTable,
       "nngenHdlcTableEntry": nngenHdlcTableEntry,
       "nngenHdlcKeepAlive": nngenHdlcKeepAlive,
       "nngenHdlcMtu": nngenHdlcMtu,
       "nngenHdlcStatsTable": nngenHdlcStatsTable,
       "nngenHdlcStatsTableEntry": nngenHdlcStatsTableEntry,
       "nngenHdlcStatsBytesRxLastBootClear": nngenHdlcStatsBytesRxLastBootClear,
       "nngenHdlcStatsBytesTxLastBootClear": nngenHdlcStatsBytesTxLastBootClear,
       "nngenHdlcStatsPktsRxLastBootClear": nngenHdlcStatsPktsRxLastBootClear,
       "nngenHdlcStatsPktsTxLastBootClear": nngenHdlcStatsPktsTxLastBootClear,
       "nngenHdlcStatsErrPktsRxLastBootClear": nngenHdlcStatsErrPktsRxLastBootClear,
       "nngenHdlcStatsUpDownStatesLastBootClear": nngenHdlcStatsUpDownStatesLastBootClear,
       "nngenHdlcStatsBytesRxLastFiveMins": nngenHdlcStatsBytesRxLastFiveMins,
       "nngenHdlcStatsBytesTxLastFiveMins": nngenHdlcStatsBytesTxLastFiveMins,
       "nngenHdlcStatsPktsRxLastFiveMins": nngenHdlcStatsPktsRxLastFiveMins,
       "nngenHdlcStatsPktsTxLastFiveMins": nngenHdlcStatsPktsTxLastFiveMins,
       "nngenHdlcStatsErrPktsRxLastFiveMins": nngenHdlcStatsErrPktsRxLastFiveMins,
       "nngenHdlcStatsUpDownStatesLastFiveMins": nngenHdlcStatsUpDownStatesLastFiveMins}
)
