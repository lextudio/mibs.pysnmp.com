# SNMP MIB module (CISCOSB-CPU-COUNTERS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCOSB-CPU-COUNTERS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:14:05 2024
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

(switch001,) = mibBuilder.importSymbols(
    "CISCOSB-MIB",
    "switch001")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

rlCpuCounters = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 124)
)
rlCpuCounters.setRevisions(
        ("2007-05-15 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RlCpuCountersTable_Object = MibTable
rlCpuCountersTable = _RlCpuCountersTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 124, 1)
)
if mibBuilder.loadTexts:
    rlCpuCountersTable.setStatus("current")
_RlCpuCountersEntry_Object = MibTableRow
rlCpuCountersEntry = _RlCpuCountersEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 124, 1, 1)
)
rlCpuCountersEntry.setIndexNames(
    (0, "CISCOSB-CPU-COUNTERS-MIB", "rlCpuCountersTarget"),
)
if mibBuilder.loadTexts:
    rlCpuCountersEntry.setStatus("current")


class _RlCpuCountersTarget_Type(Integer32):
    """Custom type rlCpuCountersTarget based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("cpuCounters", 0)
    )


_RlCpuCountersTarget_Type.__name__ = "Integer32"
_RlCpuCountersTarget_Object = MibTableColumn
rlCpuCountersTarget = _RlCpuCountersTarget_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 124, 1, 1, 1),
    _RlCpuCountersTarget_Type()
)
rlCpuCountersTarget.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlCpuCountersTarget.setStatus("current")
_RlCpuCountersTxBC_Type = Counter32
_RlCpuCountersTxBC_Object = MibTableColumn
rlCpuCountersTxBC = _RlCpuCountersTxBC_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 124, 1, 1, 2),
    _RlCpuCountersTxBC_Type()
)
rlCpuCountersTxBC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCpuCountersTxBC.setStatus("current")
_RlCpuCountersTxMC_Type = Counter32
_RlCpuCountersTxMC_Object = MibTableColumn
rlCpuCountersTxMC = _RlCpuCountersTxMC_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 124, 1, 1, 3),
    _RlCpuCountersTxMC_Type()
)
rlCpuCountersTxMC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCpuCountersTxMC.setStatus("current")
_RlCpuCountersTxUC_Type = Counter32
_RlCpuCountersTxUC_Object = MibTableColumn
rlCpuCountersTxUC = _RlCpuCountersTxUC_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 124, 1, 1, 4),
    _RlCpuCountersTxUC_Type()
)
rlCpuCountersTxUC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCpuCountersTxUC.setStatus("current")
_RlCpuCountersTxOctets_Type = Counter32
_RlCpuCountersTxOctets_Object = MibTableColumn
rlCpuCountersTxOctets = _RlCpuCountersTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 124, 1, 1, 5),
    _RlCpuCountersTxOctets_Type()
)
rlCpuCountersTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCpuCountersTxOctets.setStatus("current")
_RlCpuCountersRxBC_Type = Counter32
_RlCpuCountersRxBC_Object = MibTableColumn
rlCpuCountersRxBC = _RlCpuCountersRxBC_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 124, 1, 1, 6),
    _RlCpuCountersRxBC_Type()
)
rlCpuCountersRxBC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCpuCountersRxBC.setStatus("current")
_RlCpuCountersRxMC_Type = Counter32
_RlCpuCountersRxMC_Object = MibTableColumn
rlCpuCountersRxMC = _RlCpuCountersRxMC_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 124, 1, 1, 7),
    _RlCpuCountersRxMC_Type()
)
rlCpuCountersRxMC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCpuCountersRxMC.setStatus("current")
_RlCpuCountersRxUC_Type = Counter32
_RlCpuCountersRxUC_Object = MibTableColumn
rlCpuCountersRxUC = _RlCpuCountersRxUC_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 124, 1, 1, 8),
    _RlCpuCountersRxUC_Type()
)
rlCpuCountersRxUC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCpuCountersRxUC.setStatus("current")
_RlCpuCountersRxOctets_Type = Counter32
_RlCpuCountersRxOctets_Object = MibTableColumn
rlCpuCountersRxOctets = _RlCpuCountersRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 124, 1, 1, 9),
    _RlCpuCountersRxOctets_Type()
)
rlCpuCountersRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCpuCountersRxOctets.setStatus("current")


class _RlCpuCountersReset_Type(TruthValue):
    """Custom type rlCpuCountersReset based on TruthValue"""


_RlCpuCountersReset_Object = MibScalar
rlCpuCountersReset = _RlCpuCountersReset_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 124, 2),
    _RlCpuCountersReset_Type()
)
rlCpuCountersReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCpuCountersReset.setStatus("current")


class _RlCpuCountersEnabled_Type(TruthValue):
    """Custom type rlCpuCountersEnabled based on TruthValue"""


_RlCpuCountersEnabled_Object = MibScalar
rlCpuCountersEnabled = _RlCpuCountersEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 124, 3),
    _RlCpuCountersEnabled_Type()
)
rlCpuCountersEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCpuCountersEnabled.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCOSB-CPU-COUNTERS-MIB",
    **{"rlCpuCounters": rlCpuCounters,
       "rlCpuCountersTable": rlCpuCountersTable,
       "rlCpuCountersEntry": rlCpuCountersEntry,
       "rlCpuCountersTarget": rlCpuCountersTarget,
       "rlCpuCountersTxBC": rlCpuCountersTxBC,
       "rlCpuCountersTxMC": rlCpuCountersTxMC,
       "rlCpuCountersTxUC": rlCpuCountersTxUC,
       "rlCpuCountersTxOctets": rlCpuCountersTxOctets,
       "rlCpuCountersRxBC": rlCpuCountersRxBC,
       "rlCpuCountersRxMC": rlCpuCountersRxMC,
       "rlCpuCountersRxUC": rlCpuCountersRxUC,
       "rlCpuCountersRxOctets": rlCpuCountersRxOctets,
       "rlCpuCountersReset": rlCpuCountersReset,
       "rlCpuCountersEnabled": rlCpuCountersEnabled}
)
