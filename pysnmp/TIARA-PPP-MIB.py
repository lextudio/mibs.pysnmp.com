# SNMP MIB module (TIARA-PPP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TIARA-PPP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:01:44 2024
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

tiaraPppMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3174, 2, 14)
)
tiaraPppMib.setRevisions(
        ("1900-02-01 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PppTable_Object = MibTable
pppTable = _PppTable_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 14, 1)
)
if mibBuilder.loadTexts:
    pppTable.setStatus("current")
_PppTableEntry_Object = MibTableRow
pppTableEntry = _PppTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 14, 1, 1)
)
pppTableEntry.setIndexNames(
    (0, "TIARA-BUNDLE-MIB", "bundleId"),
)
if mibBuilder.loadTexts:
    pppTableEntry.setStatus("current")


class _PppMtu_Type(DisplayString):
    """Custom type pppMtu based on DisplayString"""
    defaultValue = OctetString("64-1500-4096")


_PppMtu_Object = MibTableColumn
pppMtu = _PppMtu_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 14, 1, 1, 1),
    _PppMtu_Type()
)
pppMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppMtu.setStatus("current")


class _PppMru_Type(DisplayString):
    """Custom type pppMru based on DisplayString"""
    defaultValue = OctetString("46-1500-4096")


_PppMru_Object = MibTableColumn
pppMru = _PppMru_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 14, 1, 1, 2),
    _PppMru_Type()
)
pppMru.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppMru.setStatus("current")


class _MlpppMrru_Type(DisplayString):
    """Custom type mlpppMrru based on DisplayString"""
    defaultValue = OctetString("1500-1524-8192")


_MlpppMrru_Object = MibTableColumn
mlpppMrru = _MlpppMrru_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 14, 1, 1, 3),
    _MlpppMrru_Type()
)
mlpppMrru.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mlpppMrru.setStatus("current")


class _MlpppSeq_Type(Integer32):
    """Custom type mlpppSeq based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("long", 2),
          ("short", 1))
    )


_MlpppSeq_Type.__name__ = "Integer32"
_MlpppSeq_Object = MibTableColumn
mlpppSeq = _MlpppSeq_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 14, 1, 1, 4),
    _MlpppSeq_Type()
)
mlpppSeq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mlpppSeq.setStatus("current")


class _MlpppSegmentThreshold_Type(Integer32):
    """Custom type mlpppSegmentThreshold based on Integer32"""
    defaultValue = 512


_MlpppSegmentThreshold_Object = MibTableColumn
mlpppSegmentThreshold = _MlpppSegmentThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 14, 1, 1, 5),
    _MlpppSegmentThreshold_Type()
)
mlpppSegmentThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mlpppSegmentThreshold.setStatus("current")


class _MlpppDiffDelay_Type(Integer32):
    """Custom type mlpppDiffDelay based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_MlpppDiffDelay_Type.__name__ = "Integer32"
_MlpppDiffDelay_Object = MibTableColumn
mlpppDiffDelay = _MlpppDiffDelay_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 14, 1, 1, 6),
    _MlpppDiffDelay_Type()
)
mlpppDiffDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mlpppDiffDelay.setStatus("current")
_MlpppDiscriminator_Type = IpAddress
_MlpppDiscriminator_Object = MibTableColumn
mlpppDiscriminator = _MlpppDiscriminator_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 14, 1, 1, 7),
    _MlpppDiscriminator_Type()
)
mlpppDiscriminator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mlpppDiscriminator.setStatus("current")
_PppStatsTable_Object = MibTable
pppStatsTable = _PppStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 14, 2)
)
if mibBuilder.loadTexts:
    pppStatsTable.setStatus("current")
_PppStatsTableEntry_Object = MibTableRow
pppStatsTableEntry = _PppStatsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 14, 2, 1)
)
pppStatsTableEntry.setIndexNames(
    (0, "TIARA-BUNDLE-MIB", "bundleId"),
)
if mibBuilder.loadTexts:
    pppStatsTableEntry.setStatus("current")
_PppStatsBytesRxLastBootOrClear_Type = Counter32
_PppStatsBytesRxLastBootOrClear_Object = MibTableColumn
pppStatsBytesRxLastBootOrClear = _PppStatsBytesRxLastBootOrClear_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 14, 2, 1, 1),
    _PppStatsBytesRxLastBootOrClear_Type()
)
pppStatsBytesRxLastBootOrClear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppStatsBytesRxLastBootOrClear.setStatus("current")
_PppStatsBytesTxLastBootOrClear_Type = Counter32
_PppStatsBytesTxLastBootOrClear_Object = MibTableColumn
pppStatsBytesTxLastBootOrClear = _PppStatsBytesTxLastBootOrClear_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 14, 2, 1, 2),
    _PppStatsBytesTxLastBootOrClear_Type()
)
pppStatsBytesTxLastBootOrClear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppStatsBytesTxLastBootOrClear.setStatus("current")
_PppStatsPktsRxLastBootOrClear_Type = Counter32
_PppStatsPktsRxLastBootOrClear_Object = MibTableColumn
pppStatsPktsRxLastBootOrClear = _PppStatsPktsRxLastBootOrClear_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 14, 2, 1, 3),
    _PppStatsPktsRxLastBootOrClear_Type()
)
pppStatsPktsRxLastBootOrClear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppStatsPktsRxLastBootOrClear.setStatus("current")
_PppStatsPktsTxLastBootOrClear_Type = Counter32
_PppStatsPktsTxLastBootOrClear_Object = MibTableColumn
pppStatsPktsTxLastBootOrClear = _PppStatsPktsTxLastBootOrClear_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 14, 2, 1, 4),
    _PppStatsPktsTxLastBootOrClear_Type()
)
pppStatsPktsTxLastBootOrClear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppStatsPktsTxLastBootOrClear.setStatus("current")
_PppStatsErrPktsRxLastBootOrClear_Type = Counter32
_PppStatsErrPktsRxLastBootOrClear_Object = MibTableColumn
pppStatsErrPktsRxLastBootOrClear = _PppStatsErrPktsRxLastBootOrClear_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 14, 2, 1, 5),
    _PppStatsErrPktsRxLastBootOrClear_Type()
)
pppStatsErrPktsRxLastBootOrClear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppStatsErrPktsRxLastBootOrClear.setStatus("current")
_PppStatsUpDownStatesLastBootOrClear_Type = Counter32
_PppStatsUpDownStatesLastBootOrClear_Object = MibTableColumn
pppStatsUpDownStatesLastBootOrClear = _PppStatsUpDownStatesLastBootOrClear_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 14, 2, 1, 6),
    _PppStatsUpDownStatesLastBootOrClear_Type()
)
pppStatsUpDownStatesLastBootOrClear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppStatsUpDownStatesLastBootOrClear.setStatus("current")
_PppStatsBytesRxLastFiveMins_Type = Counter32
_PppStatsBytesRxLastFiveMins_Object = MibTableColumn
pppStatsBytesRxLastFiveMins = _PppStatsBytesRxLastFiveMins_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 14, 2, 1, 7),
    _PppStatsBytesRxLastFiveMins_Type()
)
pppStatsBytesRxLastFiveMins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppStatsBytesRxLastFiveMins.setStatus("current")
_PppStatsBytesTxLastFiveMins_Type = Counter32
_PppStatsBytesTxLastFiveMins_Object = MibTableColumn
pppStatsBytesTxLastFiveMins = _PppStatsBytesTxLastFiveMins_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 14, 2, 1, 8),
    _PppStatsBytesTxLastFiveMins_Type()
)
pppStatsBytesTxLastFiveMins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppStatsBytesTxLastFiveMins.setStatus("current")
_PppStatsPktsRxLastFiveMins_Type = Counter32
_PppStatsPktsRxLastFiveMins_Object = MibTableColumn
pppStatsPktsRxLastFiveMins = _PppStatsPktsRxLastFiveMins_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 14, 2, 1, 9),
    _PppStatsPktsRxLastFiveMins_Type()
)
pppStatsPktsRxLastFiveMins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppStatsPktsRxLastFiveMins.setStatus("current")
_PppStatsPktsTxLastFiveMins_Type = Counter32
_PppStatsPktsTxLastFiveMins_Object = MibTableColumn
pppStatsPktsTxLastFiveMins = _PppStatsPktsTxLastFiveMins_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 14, 2, 1, 10),
    _PppStatsPktsTxLastFiveMins_Type()
)
pppStatsPktsTxLastFiveMins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppStatsPktsTxLastFiveMins.setStatus("current")
_PppStatsErrPktsRxLastFiveMins_Type = Counter32
_PppStatsErrPktsRxLastFiveMins_Object = MibTableColumn
pppStatsErrPktsRxLastFiveMins = _PppStatsErrPktsRxLastFiveMins_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 14, 2, 1, 11),
    _PppStatsErrPktsRxLastFiveMins_Type()
)
pppStatsErrPktsRxLastFiveMins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppStatsErrPktsRxLastFiveMins.setStatus("current")
_PppStatsUpDownStatesLastFiveMins_Type = Counter32
_PppStatsUpDownStatesLastFiveMins_Object = MibTableColumn
pppStatsUpDownStatesLastFiveMins = _PppStatsUpDownStatesLastFiveMins_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 14, 2, 1, 12),
    _PppStatsUpDownStatesLastFiveMins_Type()
)
pppStatsUpDownStatesLastFiveMins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppStatsUpDownStatesLastFiveMins.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIARA-PPP-MIB",
    **{"tiaraPppMib": tiaraPppMib,
       "pppTable": pppTable,
       "pppTableEntry": pppTableEntry,
       "pppMtu": pppMtu,
       "pppMru": pppMru,
       "mlpppMrru": mlpppMrru,
       "mlpppSeq": mlpppSeq,
       "mlpppSegmentThreshold": mlpppSegmentThreshold,
       "mlpppDiffDelay": mlpppDiffDelay,
       "mlpppDiscriminator": mlpppDiscriminator,
       "pppStatsTable": pppStatsTable,
       "pppStatsTableEntry": pppStatsTableEntry,
       "pppStatsBytesRxLastBootOrClear": pppStatsBytesRxLastBootOrClear,
       "pppStatsBytesTxLastBootOrClear": pppStatsBytesTxLastBootOrClear,
       "pppStatsPktsRxLastBootOrClear": pppStatsPktsRxLastBootOrClear,
       "pppStatsPktsTxLastBootOrClear": pppStatsPktsTxLastBootOrClear,
       "pppStatsErrPktsRxLastBootOrClear": pppStatsErrPktsRxLastBootOrClear,
       "pppStatsUpDownStatesLastBootOrClear": pppStatsUpDownStatesLastBootOrClear,
       "pppStatsBytesRxLastFiveMins": pppStatsBytesRxLastFiveMins,
       "pppStatsBytesTxLastFiveMins": pppStatsBytesTxLastFiveMins,
       "pppStatsPktsRxLastFiveMins": pppStatsPktsRxLastFiveMins,
       "pppStatsPktsTxLastFiveMins": pppStatsPktsTxLastFiveMins,
       "pppStatsErrPktsRxLastFiveMins": pppStatsErrPktsRxLastFiveMins,
       "pppStatsUpDownStatesLastFiveMins": pppStatsUpDownStatesLastFiveMins}
)
