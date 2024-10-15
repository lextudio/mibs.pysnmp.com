# SNMP MIB module (HOTWIRE-MSDSL-INTERFACE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HOTWIRE-MSDSL-INTERFACE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:56:51 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(pdnmsdsl,) = mibBuilder.importSymbols(
    "PDN-HEADER-MIB",
    "pdnmsdsl")

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
 NotificationType,
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
    "NotificationType",
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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MsdslDevice_ObjectIdentity = ObjectIdentity
msdslDevice = _MsdslDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1)
)
_MsdslCurrent_ObjectIdentity = ObjectIdentity
msdslCurrent = _MsdslCurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 1)
)
_MsdslCurrentTable_Object = MibTable
msdslCurrentTable = _MsdslCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 1, 1)
)
if mibBuilder.loadTexts:
    msdslCurrentTable.setStatus("mandatory")
_MsdslCurrentEntry_Object = MibTableRow
msdslCurrentEntry = _MsdslCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 1, 1, 1)
)
msdslCurrentEntry.setIndexNames(
    (0, "HOTWIRE-MSDSL-INTERFACE-MIB", "msdslCurrentIfIndex"),
)
if mibBuilder.loadTexts:
    msdslCurrentEntry.setStatus("mandatory")


class _MsdslCurrentIfIndex_Type(Integer32):
    """Custom type msdslCurrentIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MsdslCurrentIfIndex_Type.__name__ = "Integer32"
_MsdslCurrentIfIndex_Object = MibTableColumn
msdslCurrentIfIndex = _MsdslCurrentIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 1, 1, 1, 1),
    _MsdslCurrentIfIndex_Type()
)
msdslCurrentIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdslCurrentIfIndex.setStatus("mandatory")
_MsdslCurrentESs_Type = Gauge32
_MsdslCurrentESs_Object = MibTableColumn
msdslCurrentESs = _MsdslCurrentESs_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 1, 1, 1, 2),
    _MsdslCurrentESs_Type()
)
msdslCurrentESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdslCurrentESs.setStatus("mandatory")
_MsdslCurrentSESs_Type = Gauge32
_MsdslCurrentSESs_Object = MibTableColumn
msdslCurrentSESs = _MsdslCurrentSESs_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 1, 1, 1, 3),
    _MsdslCurrentSESs_Type()
)
msdslCurrentSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdslCurrentSESs.setStatus("mandatory")
_MsdslCurrentFEBEs_Type = Gauge32
_MsdslCurrentFEBEs_Object = MibTableColumn
msdslCurrentFEBEs = _MsdslCurrentFEBEs_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 1, 1, 1, 4),
    _MsdslCurrentFEBEs_Type()
)
msdslCurrentFEBEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdslCurrentFEBEs.setStatus("mandatory")


class _MsdslErrEventsCounter_Type(Integer32):
    """Custom type msdslErrEventsCounter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MsdslErrEventsCounter_Type.__name__ = "Integer32"
_MsdslErrEventsCounter_Object = MibTableColumn
msdslErrEventsCounter = _MsdslErrEventsCounter_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 1, 1, 1, 5),
    _MsdslErrEventsCounter_Type()
)
msdslErrEventsCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdslErrEventsCounter.setStatus("mandatory")


class _MsdslErrTimeElapsed_Type(Integer32):
    """Custom type msdslErrTimeElapsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 899),
    )


_MsdslErrTimeElapsed_Type.__name__ = "Integer32"
_MsdslErrTimeElapsed_Object = MibTableColumn
msdslErrTimeElapsed = _MsdslErrTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 1, 1, 1, 6),
    _MsdslErrTimeElapsed_Type()
)
msdslErrTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdslErrTimeElapsed.setStatus("mandatory")


class _MsdslErrValidIntervals_Type(Integer32):
    """Custom type msdslErrValidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_MsdslErrValidIntervals_Type.__name__ = "Integer32"
_MsdslErrValidIntervals_Object = MibTableColumn
msdslErrValidIntervals = _MsdslErrValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 1, 1, 1, 7),
    _MsdslErrValidIntervals_Type()
)
msdslErrValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdslErrValidIntervals.setStatus("mandatory")
_MsdslInterval_ObjectIdentity = ObjectIdentity
msdslInterval = _MsdslInterval_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 2)
)
_MsdslIntervalTable_Object = MibTable
msdslIntervalTable = _MsdslIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 2, 2)
)
if mibBuilder.loadTexts:
    msdslIntervalTable.setStatus("mandatory")
_MsdslIntervalEntry_Object = MibTableRow
msdslIntervalEntry = _MsdslIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 2, 2, 1)
)
msdslIntervalEntry.setIndexNames(
    (0, "HOTWIRE-MSDSL-INTERFACE-MIB", "msdslIntervalIfIndex"),
    (0, "HOTWIRE-MSDSL-INTERFACE-MIB", "msdslIntervalNumber"),
)
if mibBuilder.loadTexts:
    msdslIntervalEntry.setStatus("mandatory")


class _MsdslIntervalIfIndex_Type(Integer32):
    """Custom type msdslIntervalIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MsdslIntervalIfIndex_Type.__name__ = "Integer32"
_MsdslIntervalIfIndex_Object = MibTableColumn
msdslIntervalIfIndex = _MsdslIntervalIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 2, 2, 1, 1),
    _MsdslIntervalIfIndex_Type()
)
msdslIntervalIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdslIntervalIfIndex.setStatus("mandatory")


class _MsdslIntervalNumber_Type(Integer32):
    """Custom type msdslIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_MsdslIntervalNumber_Type.__name__ = "Integer32"
_MsdslIntervalNumber_Object = MibTableColumn
msdslIntervalNumber = _MsdslIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 2, 2, 1, 2),
    _MsdslIntervalNumber_Type()
)
msdslIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdslIntervalNumber.setStatus("mandatory")
_MsdslIntervalESs_Type = Gauge32
_MsdslIntervalESs_Object = MibTableColumn
msdslIntervalESs = _MsdslIntervalESs_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 2, 2, 1, 3),
    _MsdslIntervalESs_Type()
)
msdslIntervalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdslIntervalESs.setStatus("mandatory")
_MsdslIntervalSESs_Type = Gauge32
_MsdslIntervalSESs_Object = MibTableColumn
msdslIntervalSESs = _MsdslIntervalSESs_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 2, 2, 1, 4),
    _MsdslIntervalSESs_Type()
)
msdslIntervalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdslIntervalSESs.setStatus("mandatory")
_MsdslIntervalFEBEs_Type = Gauge32
_MsdslIntervalFEBEs_Object = MibTableColumn
msdslIntervalFEBEs = _MsdslIntervalFEBEs_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 2, 2, 1, 5),
    _MsdslIntervalFEBEs_Type()
)
msdslIntervalFEBEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdslIntervalFEBEs.setStatus("mandatory")
_MsdslWorstInterval_ObjectIdentity = ObjectIdentity
msdslWorstInterval = _MsdslWorstInterval_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 3)
)
_MsdslWorstIntervalTable_Object = MibTable
msdslWorstIntervalTable = _MsdslWorstIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 3, 3)
)
if mibBuilder.loadTexts:
    msdslWorstIntervalTable.setStatus("mandatory")
_MsdslWorstIntervalEntry_Object = MibTableRow
msdslWorstIntervalEntry = _MsdslWorstIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 3, 3, 1)
)
msdslWorstIntervalEntry.setIndexNames(
    (0, "HOTWIRE-MSDSL-INTERFACE-MIB", "msdslWorstIntervalIfIndex"),
)
if mibBuilder.loadTexts:
    msdslWorstIntervalEntry.setStatus("mandatory")


class _MsdslWorstIntervalIfIndex_Type(Integer32):
    """Custom type msdslWorstIntervalIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MsdslWorstIntervalIfIndex_Type.__name__ = "Integer32"
_MsdslWorstIntervalIfIndex_Object = MibTableColumn
msdslWorstIntervalIfIndex = _MsdslWorstIntervalIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 3, 3, 1, 1),
    _MsdslWorstIntervalIfIndex_Type()
)
msdslWorstIntervalIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdslWorstIntervalIfIndex.setStatus("mandatory")


class _MsdslWorstIntervalESs_Type(Integer32):
    """Custom type msdslWorstIntervalESs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_MsdslWorstIntervalESs_Type.__name__ = "Integer32"
_MsdslWorstIntervalESs_Object = MibTableColumn
msdslWorstIntervalESs = _MsdslWorstIntervalESs_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 3, 3, 1, 2),
    _MsdslWorstIntervalESs_Type()
)
msdslWorstIntervalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdslWorstIntervalESs.setStatus("mandatory")


class _MsdslWorstIntervalSESs_Type(Integer32):
    """Custom type msdslWorstIntervalSESs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_MsdslWorstIntervalSESs_Type.__name__ = "Integer32"
_MsdslWorstIntervalSESs_Object = MibTableColumn
msdslWorstIntervalSESs = _MsdslWorstIntervalSESs_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 3, 3, 1, 3),
    _MsdslWorstIntervalSESs_Type()
)
msdslWorstIntervalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdslWorstIntervalSESs.setStatus("mandatory")


class _MsdslWorstIntervalFEBEs_Type(Integer32):
    """Custom type msdslWorstIntervalFEBEs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_MsdslWorstIntervalFEBEs_Type.__name__ = "Integer32"
_MsdslWorstIntervalFEBEs_Object = MibTableColumn
msdslWorstIntervalFEBEs = _MsdslWorstIntervalFEBEs_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 3, 3, 1, 4),
    _MsdslWorstIntervalFEBEs_Type()
)
msdslWorstIntervalFEBEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdslWorstIntervalFEBEs.setStatus("mandatory")
_MsdslTotal_ObjectIdentity = ObjectIdentity
msdslTotal = _MsdslTotal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 4)
)
_MsdslTotalTable_Object = MibTable
msdslTotalTable = _MsdslTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 4, 4)
)
if mibBuilder.loadTexts:
    msdslTotalTable.setStatus("mandatory")
_MsdslTotalEntry_Object = MibTableRow
msdslTotalEntry = _MsdslTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 4, 4, 1)
)
msdslTotalEntry.setIndexNames(
    (0, "HOTWIRE-MSDSL-INTERFACE-MIB", "msdslTotalIfIndex"),
)
if mibBuilder.loadTexts:
    msdslTotalEntry.setStatus("mandatory")


class _MsdslTotalIfIndex_Type(Integer32):
    """Custom type msdslTotalIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MsdslTotalIfIndex_Type.__name__ = "Integer32"
_MsdslTotalIfIndex_Object = MibTableColumn
msdslTotalIfIndex = _MsdslTotalIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 4, 4, 1, 1),
    _MsdslTotalIfIndex_Type()
)
msdslTotalIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdslTotalIfIndex.setStatus("mandatory")
_MsdslTotalESs_Type = Gauge32
_MsdslTotalESs_Object = MibTableColumn
msdslTotalESs = _MsdslTotalESs_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 4, 4, 1, 2),
    _MsdslTotalESs_Type()
)
msdslTotalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdslTotalESs.setStatus("mandatory")
_MsdslTotalSESs_Type = Gauge32
_MsdslTotalSESs_Object = MibTableColumn
msdslTotalSESs = _MsdslTotalSESs_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 4, 4, 1, 3),
    _MsdslTotalSESs_Type()
)
msdslTotalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdslTotalSESs.setStatus("mandatory")
_MsdslTotalFEBEs_Type = Gauge32
_MsdslTotalFEBEs_Object = MibTableColumn
msdslTotalFEBEs = _MsdslTotalFEBEs_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 4, 4, 1, 4),
    _MsdslTotalFEBEs_Type()
)
msdslTotalFEBEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdslTotalFEBEs.setStatus("mandatory")
_MsdslFarEndCurrent_ObjectIdentity = ObjectIdentity
msdslFarEndCurrent = _MsdslFarEndCurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 5)
)
_MsdslFarEndCurrentTable_Object = MibTable
msdslFarEndCurrentTable = _MsdslFarEndCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 5, 5)
)
if mibBuilder.loadTexts:
    msdslFarEndCurrentTable.setStatus("mandatory")
_MsdslFarEndCurrentEntry_Object = MibTableRow
msdslFarEndCurrentEntry = _MsdslFarEndCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 5, 5, 1)
)
msdslFarEndCurrentEntry.setIndexNames(
    (0, "HOTWIRE-MSDSL-INTERFACE-MIB", "msdslFarEndCurrentIfIndex"),
)
if mibBuilder.loadTexts:
    msdslFarEndCurrentEntry.setStatus("mandatory")


class _MsdslFarEndCurrentIfIndex_Type(Integer32):
    """Custom type msdslFarEndCurrentIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MsdslFarEndCurrentIfIndex_Type.__name__ = "Integer32"
_MsdslFarEndCurrentIfIndex_Object = MibTableColumn
msdslFarEndCurrentIfIndex = _MsdslFarEndCurrentIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 5, 5, 1, 1),
    _MsdslFarEndCurrentIfIndex_Type()
)
msdslFarEndCurrentIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdslFarEndCurrentIfIndex.setStatus("mandatory")
_MsdslFarEndCurrentESs_Type = Gauge32
_MsdslFarEndCurrentESs_Object = MibTableColumn
msdslFarEndCurrentESs = _MsdslFarEndCurrentESs_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 5, 5, 1, 2),
    _MsdslFarEndCurrentESs_Type()
)
msdslFarEndCurrentESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdslFarEndCurrentESs.setStatus("mandatory")
_MsdslFarEndCurrentSESs_Type = Gauge32
_MsdslFarEndCurrentSESs_Object = MibTableColumn
msdslFarEndCurrentSESs = _MsdslFarEndCurrentSESs_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 5, 5, 1, 3),
    _MsdslFarEndCurrentSESs_Type()
)
msdslFarEndCurrentSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdslFarEndCurrentSESs.setStatus("mandatory")
_MsdslFarEndCurrentFEBEs_Type = Gauge32
_MsdslFarEndCurrentFEBEs_Object = MibTableColumn
msdslFarEndCurrentFEBEs = _MsdslFarEndCurrentFEBEs_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 5, 5, 1, 4),
    _MsdslFarEndCurrentFEBEs_Type()
)
msdslFarEndCurrentFEBEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdslFarEndCurrentFEBEs.setStatus("mandatory")
_MsdslFarEndInterval_ObjectIdentity = ObjectIdentity
msdslFarEndInterval = _MsdslFarEndInterval_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 6)
)
_MsdslFarEndIntervalTable_Object = MibTable
msdslFarEndIntervalTable = _MsdslFarEndIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 6, 6)
)
if mibBuilder.loadTexts:
    msdslFarEndIntervalTable.setStatus("mandatory")
_MsdslFarEndIntervalEntry_Object = MibTableRow
msdslFarEndIntervalEntry = _MsdslFarEndIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 6, 6, 1)
)
msdslFarEndIntervalEntry.setIndexNames(
    (0, "HOTWIRE-MSDSL-INTERFACE-MIB", "msdslFarEndIntervalIfIndex"),
    (0, "HOTWIRE-MSDSL-INTERFACE-MIB", "msdslFarEndIntervalNumber"),
)
if mibBuilder.loadTexts:
    msdslFarEndIntervalEntry.setStatus("mandatory")


class _MsdslFarEndIntervalIfIndex_Type(Integer32):
    """Custom type msdslFarEndIntervalIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MsdslFarEndIntervalIfIndex_Type.__name__ = "Integer32"
_MsdslFarEndIntervalIfIndex_Object = MibTableColumn
msdslFarEndIntervalIfIndex = _MsdslFarEndIntervalIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 6, 6, 1, 1),
    _MsdslFarEndIntervalIfIndex_Type()
)
msdslFarEndIntervalIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdslFarEndIntervalIfIndex.setStatus("mandatory")


class _MsdslFarEndIntervalNumber_Type(Integer32):
    """Custom type msdslFarEndIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_MsdslFarEndIntervalNumber_Type.__name__ = "Integer32"
_MsdslFarEndIntervalNumber_Object = MibTableColumn
msdslFarEndIntervalNumber = _MsdslFarEndIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 6, 6, 1, 2),
    _MsdslFarEndIntervalNumber_Type()
)
msdslFarEndIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdslFarEndIntervalNumber.setStatus("mandatory")
_MsdslFarEndIntervalESs_Type = Gauge32
_MsdslFarEndIntervalESs_Object = MibTableColumn
msdslFarEndIntervalESs = _MsdslFarEndIntervalESs_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 6, 6, 1, 3),
    _MsdslFarEndIntervalESs_Type()
)
msdslFarEndIntervalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdslFarEndIntervalESs.setStatus("mandatory")
_MsdslFarEndIntervalSESs_Type = Gauge32
_MsdslFarEndIntervalSESs_Object = MibTableColumn
msdslFarEndIntervalSESs = _MsdslFarEndIntervalSESs_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 6, 6, 1, 4),
    _MsdslFarEndIntervalSESs_Type()
)
msdslFarEndIntervalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdslFarEndIntervalSESs.setStatus("mandatory")
_MsdslFarEndIntervalFEBEs_Type = Gauge32
_MsdslFarEndIntervalFEBEs_Object = MibTableColumn
msdslFarEndIntervalFEBEs = _MsdslFarEndIntervalFEBEs_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 6, 6, 1, 5),
    _MsdslFarEndIntervalFEBEs_Type()
)
msdslFarEndIntervalFEBEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdslFarEndIntervalFEBEs.setStatus("mandatory")
_MsdslFarEndWorstInterval_ObjectIdentity = ObjectIdentity
msdslFarEndWorstInterval = _MsdslFarEndWorstInterval_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 7)
)
_MsdslFarEndWorstIntervalTable_Object = MibTable
msdslFarEndWorstIntervalTable = _MsdslFarEndWorstIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 7, 7)
)
if mibBuilder.loadTexts:
    msdslFarEndWorstIntervalTable.setStatus("mandatory")
_MsdslFarEndWorstIntervalEntry_Object = MibTableRow
msdslFarEndWorstIntervalEntry = _MsdslFarEndWorstIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 7, 7, 1)
)
msdslFarEndWorstIntervalEntry.setIndexNames(
    (0, "HOTWIRE-MSDSL-INTERFACE-MIB", "msdslFarEndWorstIntervalIfIndex"),
)
if mibBuilder.loadTexts:
    msdslFarEndWorstIntervalEntry.setStatus("mandatory")


class _MsdslFarEndWorstIntervalIfIndex_Type(Integer32):
    """Custom type msdslFarEndWorstIntervalIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MsdslFarEndWorstIntervalIfIndex_Type.__name__ = "Integer32"
_MsdslFarEndWorstIntervalIfIndex_Object = MibTableColumn
msdslFarEndWorstIntervalIfIndex = _MsdslFarEndWorstIntervalIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 7, 7, 1, 1),
    _MsdslFarEndWorstIntervalIfIndex_Type()
)
msdslFarEndWorstIntervalIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdslFarEndWorstIntervalIfIndex.setStatus("mandatory")


class _MsdslFarEndWorstIntervalESs_Type(Integer32):
    """Custom type msdslFarEndWorstIntervalESs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_MsdslFarEndWorstIntervalESs_Type.__name__ = "Integer32"
_MsdslFarEndWorstIntervalESs_Object = MibTableColumn
msdslFarEndWorstIntervalESs = _MsdslFarEndWorstIntervalESs_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 7, 7, 1, 2),
    _MsdslFarEndWorstIntervalESs_Type()
)
msdslFarEndWorstIntervalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdslFarEndWorstIntervalESs.setStatus("mandatory")


class _MsdslFarEndWorstIntervalSESs_Type(Integer32):
    """Custom type msdslFarEndWorstIntervalSESs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_MsdslFarEndWorstIntervalSESs_Type.__name__ = "Integer32"
_MsdslFarEndWorstIntervalSESs_Object = MibTableColumn
msdslFarEndWorstIntervalSESs = _MsdslFarEndWorstIntervalSESs_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 7, 7, 1, 3),
    _MsdslFarEndWorstIntervalSESs_Type()
)
msdslFarEndWorstIntervalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdslFarEndWorstIntervalSESs.setStatus("mandatory")


class _MsdslFarEndWorstIntervalFEBEs_Type(Integer32):
    """Custom type msdslFarEndWorstIntervalFEBEs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_MsdslFarEndWorstIntervalFEBEs_Type.__name__ = "Integer32"
_MsdslFarEndWorstIntervalFEBEs_Object = MibTableColumn
msdslFarEndWorstIntervalFEBEs = _MsdslFarEndWorstIntervalFEBEs_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 7, 7, 1, 4),
    _MsdslFarEndWorstIntervalFEBEs_Type()
)
msdslFarEndWorstIntervalFEBEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdslFarEndWorstIntervalFEBEs.setStatus("mandatory")
_MsdslFarEndTotal_ObjectIdentity = ObjectIdentity
msdslFarEndTotal = _MsdslFarEndTotal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 8)
)
_MsdslFarEndTotalTable_Object = MibTable
msdslFarEndTotalTable = _MsdslFarEndTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 8, 8)
)
if mibBuilder.loadTexts:
    msdslFarEndTotalTable.setStatus("mandatory")
_MsdslFarEndTotalEntry_Object = MibTableRow
msdslFarEndTotalEntry = _MsdslFarEndTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 8, 8, 1)
)
msdslFarEndTotalEntry.setIndexNames(
    (0, "HOTWIRE-MSDSL-INTERFACE-MIB", "msdslTotalIfIndex"),
)
if mibBuilder.loadTexts:
    msdslFarEndTotalEntry.setStatus("mandatory")


class _MsdslFarEndTotalIfIndex_Type(Integer32):
    """Custom type msdslFarEndTotalIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MsdslFarEndTotalIfIndex_Type.__name__ = "Integer32"
_MsdslFarEndTotalIfIndex_Object = MibTableColumn
msdslFarEndTotalIfIndex = _MsdslFarEndTotalIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 8, 8, 1, 1),
    _MsdslFarEndTotalIfIndex_Type()
)
msdslFarEndTotalIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdslFarEndTotalIfIndex.setStatus("mandatory")
_MsdslFarEndTotalESs_Type = Gauge32
_MsdslFarEndTotalESs_Object = MibTableColumn
msdslFarEndTotalESs = _MsdslFarEndTotalESs_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 8, 8, 1, 2),
    _MsdslFarEndTotalESs_Type()
)
msdslFarEndTotalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdslFarEndTotalESs.setStatus("mandatory")
_MsdslFarEndTotalSESs_Type = Gauge32
_MsdslFarEndTotalSESs_Object = MibTableColumn
msdslFarEndTotalSESs = _MsdslFarEndTotalSESs_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 8, 8, 1, 3),
    _MsdslFarEndTotalSESs_Type()
)
msdslFarEndTotalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdslFarEndTotalSESs.setStatus("mandatory")
_MsdslFarEndTotalFEBEs_Type = Gauge32
_MsdslFarEndTotalFEBEs_Object = MibTableColumn
msdslFarEndTotalFEBEs = _MsdslFarEndTotalFEBEs_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 8, 8, 1, 4),
    _MsdslFarEndTotalFEBEs_Type()
)
msdslFarEndTotalFEBEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdslFarEndTotalFEBEs.setStatus("mandatory")
_MsdslCurrentPerf_ObjectIdentity = ObjectIdentity
msdslCurrentPerf = _MsdslCurrentPerf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 9)
)
_MsdslCurrentPerfTable_Object = MibTable
msdslCurrentPerfTable = _MsdslCurrentPerfTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 9, 9)
)
if mibBuilder.loadTexts:
    msdslCurrentPerfTable.setStatus("mandatory")
_MsdslCurrentPerfEntry_Object = MibTableRow
msdslCurrentPerfEntry = _MsdslCurrentPerfEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 9, 9, 1)
)
msdslCurrentPerfEntry.setIndexNames(
    (0, "HOTWIRE-MSDSL-INTERFACE-MIB", "msdslCurrentPerfIfIndex"),
)
if mibBuilder.loadTexts:
    msdslCurrentPerfEntry.setStatus("mandatory")


class _MsdslCurrentPerfIfIndex_Type(Integer32):
    """Custom type msdslCurrentPerfIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MsdslCurrentPerfIfIndex_Type.__name__ = "Integer32"
_MsdslCurrentPerfIfIndex_Object = MibTableColumn
msdslCurrentPerfIfIndex = _MsdslCurrentPerfIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 9, 9, 1, 1),
    _MsdslCurrentPerfIfIndex_Type()
)
msdslCurrentPerfIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdslCurrentPerfIfIndex.setStatus("mandatory")
_MsdslCurrentPerfMargin_Type = Gauge32
_MsdslCurrentPerfMargin_Object = MibTableColumn
msdslCurrentPerfMargin = _MsdslCurrentPerfMargin_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 9, 9, 1, 2),
    _MsdslCurrentPerfMargin_Type()
)
msdslCurrentPerfMargin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdslCurrentPerfMargin.setStatus("mandatory")
_MsdslCurrentPerfTxPwr_Type = Gauge32
_MsdslCurrentPerfTxPwr_Object = MibTableColumn
msdslCurrentPerfTxPwr = _MsdslCurrentPerfTxPwr_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 9, 9, 1, 3),
    _MsdslCurrentPerfTxPwr_Type()
)
msdslCurrentPerfTxPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdslCurrentPerfTxPwr.setStatus("mandatory")
_MsdslCurrentPerfRxGain_Type = Gauge32
_MsdslCurrentPerfRxGain_Object = MibTableColumn
msdslCurrentPerfRxGain = _MsdslCurrentPerfRxGain_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 9, 9, 1, 4),
    _MsdslCurrentPerfRxGain_Type()
)
msdslCurrentPerfRxGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdslCurrentPerfRxGain.setStatus("mandatory")
_MsdslPerfPayloadRate_Type = Gauge32
_MsdslPerfPayloadRate_Object = MibTableColumn
msdslPerfPayloadRate = _MsdslPerfPayloadRate_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 9, 9, 1, 5),
    _MsdslPerfPayloadRate_Type()
)
msdslPerfPayloadRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdslPerfPayloadRate.setStatus("mandatory")


class _MsdslTimeElapsed_Type(Integer32):
    """Custom type msdslTimeElapsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 899),
    )


_MsdslTimeElapsed_Type.__name__ = "Integer32"
_MsdslTimeElapsed_Object = MibTableColumn
msdslTimeElapsed = _MsdslTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 9, 9, 1, 6),
    _MsdslTimeElapsed_Type()
)
msdslTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdslTimeElapsed.setStatus("mandatory")


class _MsdslValidIntervals_Type(Integer32):
    """Custom type msdslValidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_MsdslValidIntervals_Type.__name__ = "Integer32"
_MsdslValidIntervals_Object = MibTableColumn
msdslValidIntervals = _MsdslValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 9, 9, 1, 7),
    _MsdslValidIntervals_Type()
)
msdslValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdslValidIntervals.setStatus("mandatory")
_MsdslIntervalPerf_ObjectIdentity = ObjectIdentity
msdslIntervalPerf = _MsdslIntervalPerf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 10)
)
_MsdslIntervalPerfTable_Object = MibTable
msdslIntervalPerfTable = _MsdslIntervalPerfTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 10, 10)
)
if mibBuilder.loadTexts:
    msdslIntervalPerfTable.setStatus("mandatory")
_MsdslIntervalPerfEntry_Object = MibTableRow
msdslIntervalPerfEntry = _MsdslIntervalPerfEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 10, 10, 1)
)
msdslIntervalPerfEntry.setIndexNames(
    (0, "HOTWIRE-MSDSL-INTERFACE-MIB", "msdslIntervalPerfIfIndex"),
    (0, "HOTWIRE-MSDSL-INTERFACE-MIB", "msdslIntervalPerfNumber"),
)
if mibBuilder.loadTexts:
    msdslIntervalPerfEntry.setStatus("mandatory")


class _MsdslIntervalPerfIfIndex_Type(Integer32):
    """Custom type msdslIntervalPerfIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MsdslIntervalPerfIfIndex_Type.__name__ = "Integer32"
_MsdslIntervalPerfIfIndex_Object = MibTableColumn
msdslIntervalPerfIfIndex = _MsdslIntervalPerfIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 10, 10, 1, 1),
    _MsdslIntervalPerfIfIndex_Type()
)
msdslIntervalPerfIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdslIntervalPerfIfIndex.setStatus("mandatory")


class _MsdslIntervalPerfNumber_Type(Integer32):
    """Custom type msdslIntervalPerfNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_MsdslIntervalPerfNumber_Type.__name__ = "Integer32"
_MsdslIntervalPerfNumber_Object = MibTableColumn
msdslIntervalPerfNumber = _MsdslIntervalPerfNumber_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 10, 10, 1, 2),
    _MsdslIntervalPerfNumber_Type()
)
msdslIntervalPerfNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdslIntervalPerfNumber.setStatus("mandatory")
_MsdslIntervalPerfMargin_Type = Gauge32
_MsdslIntervalPerfMargin_Object = MibTableColumn
msdslIntervalPerfMargin = _MsdslIntervalPerfMargin_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 10, 10, 1, 3),
    _MsdslIntervalPerfMargin_Type()
)
msdslIntervalPerfMargin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdslIntervalPerfMargin.setStatus("mandatory")
_MsdslIntervalPerfTxPwr_Type = Gauge32
_MsdslIntervalPerfTxPwr_Object = MibTableColumn
msdslIntervalPerfTxPwr = _MsdslIntervalPerfTxPwr_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 10, 10, 1, 4),
    _MsdslIntervalPerfTxPwr_Type()
)
msdslIntervalPerfTxPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdslIntervalPerfTxPwr.setStatus("mandatory")
_MsdslIntervalPerfRxGain_Type = Gauge32
_MsdslIntervalPerfRxGain_Object = MibTableColumn
msdslIntervalPerfRxGain = _MsdslIntervalPerfRxGain_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 10, 10, 1, 5),
    _MsdslIntervalPerfRxGain_Type()
)
msdslIntervalPerfRxGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdslIntervalPerfRxGain.setStatus("mandatory")
_MsdslFarEndCurrentPerf_ObjectIdentity = ObjectIdentity
msdslFarEndCurrentPerf = _MsdslFarEndCurrentPerf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 11)
)
_MsdslFarEndCurrentPerfTable_Object = MibTable
msdslFarEndCurrentPerfTable = _MsdslFarEndCurrentPerfTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 11, 11)
)
if mibBuilder.loadTexts:
    msdslFarEndCurrentPerfTable.setStatus("mandatory")
_MsdslFarEndCurrentPerfEntry_Object = MibTableRow
msdslFarEndCurrentPerfEntry = _MsdslFarEndCurrentPerfEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 11, 11, 1)
)
msdslFarEndCurrentPerfEntry.setIndexNames(
    (0, "HOTWIRE-MSDSL-INTERFACE-MIB", "msdslFarEndCurrentPerfIfIndex"),
)
if mibBuilder.loadTexts:
    msdslFarEndCurrentPerfEntry.setStatus("mandatory")


class _MsdslFarEndCurrentPerfIfIndex_Type(Integer32):
    """Custom type msdslFarEndCurrentPerfIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MsdslFarEndCurrentPerfIfIndex_Type.__name__ = "Integer32"
_MsdslFarEndCurrentPerfIfIndex_Object = MibTableColumn
msdslFarEndCurrentPerfIfIndex = _MsdslFarEndCurrentPerfIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 11, 11, 1, 1),
    _MsdslFarEndCurrentPerfIfIndex_Type()
)
msdslFarEndCurrentPerfIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdslFarEndCurrentPerfIfIndex.setStatus("mandatory")
_MsdslFarEndCurrentPerfMargin_Type = Gauge32
_MsdslFarEndCurrentPerfMargin_Object = MibTableColumn
msdslFarEndCurrentPerfMargin = _MsdslFarEndCurrentPerfMargin_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 11, 11, 1, 2),
    _MsdslFarEndCurrentPerfMargin_Type()
)
msdslFarEndCurrentPerfMargin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdslFarEndCurrentPerfMargin.setStatus("mandatory")
_MsdslFarEndCurrentPerfTxPwr_Type = Gauge32
_MsdslFarEndCurrentPerfTxPwr_Object = MibTableColumn
msdslFarEndCurrentPerfTxPwr = _MsdslFarEndCurrentPerfTxPwr_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 11, 11, 1, 3),
    _MsdslFarEndCurrentPerfTxPwr_Type()
)
msdslFarEndCurrentPerfTxPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdslFarEndCurrentPerfTxPwr.setStatus("mandatory")
_MsdslFarEndCurrentPerfRxGain_Type = Gauge32
_MsdslFarEndCurrentPerfRxGain_Object = MibTableColumn
msdslFarEndCurrentPerfRxGain = _MsdslFarEndCurrentPerfRxGain_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 11, 11, 1, 4),
    _MsdslFarEndCurrentPerfRxGain_Type()
)
msdslFarEndCurrentPerfRxGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdslFarEndCurrentPerfRxGain.setStatus("mandatory")
_MsdslFarEndIntervalPerf_ObjectIdentity = ObjectIdentity
msdslFarEndIntervalPerf = _MsdslFarEndIntervalPerf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 12)
)
_MsdslFarEndIntervalPerfTable_Object = MibTable
msdslFarEndIntervalPerfTable = _MsdslFarEndIntervalPerfTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 12, 12)
)
if mibBuilder.loadTexts:
    msdslFarEndIntervalPerfTable.setStatus("mandatory")
_MsdslFarEndIntervalPerfEntry_Object = MibTableRow
msdslFarEndIntervalPerfEntry = _MsdslFarEndIntervalPerfEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 12, 12, 1)
)
msdslFarEndIntervalPerfEntry.setIndexNames(
    (0, "HOTWIRE-MSDSL-INTERFACE-MIB", "msdslFarEndIntervalPerfIfIndex"),
    (0, "HOTWIRE-MSDSL-INTERFACE-MIB", "msdslFarEndIntervalPerfNumber"),
)
if mibBuilder.loadTexts:
    msdslFarEndIntervalPerfEntry.setStatus("mandatory")


class _MsdslFarEndIntervalPerfIfIndex_Type(Integer32):
    """Custom type msdslFarEndIntervalPerfIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MsdslFarEndIntervalPerfIfIndex_Type.__name__ = "Integer32"
_MsdslFarEndIntervalPerfIfIndex_Object = MibTableColumn
msdslFarEndIntervalPerfIfIndex = _MsdslFarEndIntervalPerfIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 12, 12, 1, 1),
    _MsdslFarEndIntervalPerfIfIndex_Type()
)
msdslFarEndIntervalPerfIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdslFarEndIntervalPerfIfIndex.setStatus("mandatory")


class _MsdslFarEndIntervalPerfNumber_Type(Integer32):
    """Custom type msdslFarEndIntervalPerfNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_MsdslFarEndIntervalPerfNumber_Type.__name__ = "Integer32"
_MsdslFarEndIntervalPerfNumber_Object = MibTableColumn
msdslFarEndIntervalPerfNumber = _MsdslFarEndIntervalPerfNumber_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 12, 12, 1, 2),
    _MsdslFarEndIntervalPerfNumber_Type()
)
msdslFarEndIntervalPerfNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdslFarEndIntervalPerfNumber.setStatus("mandatory")
_MsdslFarEndIntervalPerfMargin_Type = Gauge32
_MsdslFarEndIntervalPerfMargin_Object = MibTableColumn
msdslFarEndIntervalPerfMargin = _MsdslFarEndIntervalPerfMargin_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 12, 12, 1, 3),
    _MsdslFarEndIntervalPerfMargin_Type()
)
msdslFarEndIntervalPerfMargin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdslFarEndIntervalPerfMargin.setStatus("mandatory")
_MsdslFarEndIntervalPerfTxPwr_Type = Gauge32
_MsdslFarEndIntervalPerfTxPwr_Object = MibTableColumn
msdslFarEndIntervalPerfTxPwr = _MsdslFarEndIntervalPerfTxPwr_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 12, 12, 1, 4),
    _MsdslFarEndIntervalPerfTxPwr_Type()
)
msdslFarEndIntervalPerfTxPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdslFarEndIntervalPerfTxPwr.setStatus("mandatory")
_MsdslFarEndIntervalPerfRxGain_Type = Gauge32
_MsdslFarEndIntervalPerfRxGain_Object = MibTableColumn
msdslFarEndIntervalPerfRxGain = _MsdslFarEndIntervalPerfRxGain_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 12, 12, 1, 5),
    _MsdslFarEndIntervalPerfRxGain_Type()
)
msdslFarEndIntervalPerfRxGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdslFarEndIntervalPerfRxGain.setStatus("mandatory")
_Msdsldsx1WorstInterval_ObjectIdentity = ObjectIdentity
msdsldsx1WorstInterval = _Msdsldsx1WorstInterval_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 13)
)
_Msdsldsx1WorstIntervalTable_Object = MibTable
msdsldsx1WorstIntervalTable = _Msdsldsx1WorstIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 13, 13)
)
if mibBuilder.loadTexts:
    msdsldsx1WorstIntervalTable.setStatus("mandatory")
_Msdsldsx1WorstIntervalEntry_Object = MibTableRow
msdsldsx1WorstIntervalEntry = _Msdsldsx1WorstIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 13, 13, 1)
)
msdsldsx1WorstIntervalEntry.setIndexNames(
    (0, "HOTWIRE-MSDSL-INTERFACE-MIB", "msdsldsx1WorstIntervalIfIndex"),
)
if mibBuilder.loadTexts:
    msdsldsx1WorstIntervalEntry.setStatus("mandatory")


class _Msdsldsx1WorstIntervalIfIndex_Type(Integer32):
    """Custom type msdsldsx1WorstIntervalIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Msdsldsx1WorstIntervalIfIndex_Type.__name__ = "Integer32"
_Msdsldsx1WorstIntervalIfIndex_Object = MibTableColumn
msdsldsx1WorstIntervalIfIndex = _Msdsldsx1WorstIntervalIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 13, 13, 1, 1),
    _Msdsldsx1WorstIntervalIfIndex_Type()
)
msdsldsx1WorstIntervalIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdsldsx1WorstIntervalIfIndex.setStatus("mandatory")
_Msdsldsx1WorstIntervalESs_Type = Integer32
_Msdsldsx1WorstIntervalESs_Object = MibTableColumn
msdsldsx1WorstIntervalESs = _Msdsldsx1WorstIntervalESs_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 13, 13, 1, 2),
    _Msdsldsx1WorstIntervalESs_Type()
)
msdsldsx1WorstIntervalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdsldsx1WorstIntervalESs.setStatus("mandatory")
_Msdsldsx1WorstIntervalUASs_Type = Integer32
_Msdsldsx1WorstIntervalUASs_Object = MibTableColumn
msdsldsx1WorstIntervalUASs = _Msdsldsx1WorstIntervalUASs_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 13, 13, 1, 3),
    _Msdsldsx1WorstIntervalUASs_Type()
)
msdsldsx1WorstIntervalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdsldsx1WorstIntervalUASs.setStatus("mandatory")
_Msdsldsx1WorstIntervalSESs_Type = Integer32
_Msdsldsx1WorstIntervalSESs_Object = MibTableColumn
msdsldsx1WorstIntervalSESs = _Msdsldsx1WorstIntervalSESs_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 13, 13, 1, 4),
    _Msdsldsx1WorstIntervalSESs_Type()
)
msdsldsx1WorstIntervalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdsldsx1WorstIntervalSESs.setStatus("mandatory")
_Msdsldsx1WorstIntervalBESs_Type = Integer32
_Msdsldsx1WorstIntervalBESs_Object = MibTableColumn
msdsldsx1WorstIntervalBESs = _Msdsldsx1WorstIntervalBESs_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 13, 13, 1, 5),
    _Msdsldsx1WorstIntervalBESs_Type()
)
msdsldsx1WorstIntervalBESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdsldsx1WorstIntervalBESs.setStatus("mandatory")
_Msdsldsx1WorstIntervalCSSs_Type = Integer32
_Msdsldsx1WorstIntervalCSSs_Object = MibTableColumn
msdsldsx1WorstIntervalCSSs = _Msdsldsx1WorstIntervalCSSs_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 13, 13, 1, 6),
    _Msdsldsx1WorstIntervalCSSs_Type()
)
msdsldsx1WorstIntervalCSSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdsldsx1WorstIntervalCSSs.setStatus("mandatory")
_Msdsldsx1WorstIntervalLOFC_Type = Integer32
_Msdsldsx1WorstIntervalLOFC_Object = MibTableColumn
msdsldsx1WorstIntervalLOFC = _Msdsldsx1WorstIntervalLOFC_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 13, 13, 1, 7),
    _Msdsldsx1WorstIntervalLOFC_Type()
)
msdsldsx1WorstIntervalLOFC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdsldsx1WorstIntervalLOFC.setStatus("mandatory")
_MsdslG703WorstInterval_ObjectIdentity = ObjectIdentity
msdslG703WorstInterval = _MsdslG703WorstInterval_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 14)
)
_MsdslG703WorstIntervalTable_Object = MibTable
msdslG703WorstIntervalTable = _MsdslG703WorstIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 14, 14)
)
if mibBuilder.loadTexts:
    msdslG703WorstIntervalTable.setStatus("mandatory")
_MsdslG703WorstIntervalEntry_Object = MibTableRow
msdslG703WorstIntervalEntry = _MsdslG703WorstIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 14, 14, 1)
)
msdslG703WorstIntervalEntry.setIndexNames(
    (0, "HOTWIRE-MSDSL-INTERFACE-MIB", "msdslG703WorstIntervalIfIndex"),
)
if mibBuilder.loadTexts:
    msdslG703WorstIntervalEntry.setStatus("mandatory")


class _MsdslG703WorstIntervalIfIndex_Type(Integer32):
    """Custom type msdslG703WorstIntervalIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MsdslG703WorstIntervalIfIndex_Type.__name__ = "Integer32"
_MsdslG703WorstIntervalIfIndex_Object = MibTableColumn
msdslG703WorstIntervalIfIndex = _MsdslG703WorstIntervalIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 14, 14, 1, 1),
    _MsdslG703WorstIntervalIfIndex_Type()
)
msdslG703WorstIntervalIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdslG703WorstIntervalIfIndex.setStatus("mandatory")
_MsdslG703WorstIntervalESs_Type = Integer32
_MsdslG703WorstIntervalESs_Object = MibTableColumn
msdslG703WorstIntervalESs = _MsdslG703WorstIntervalESs_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 14, 14, 1, 2),
    _MsdslG703WorstIntervalESs_Type()
)
msdslG703WorstIntervalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdslG703WorstIntervalESs.setStatus("mandatory")
_MsdslG703WorstIntervalUASs_Type = Integer32
_MsdslG703WorstIntervalUASs_Object = MibTableColumn
msdslG703WorstIntervalUASs = _MsdslG703WorstIntervalUASs_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 14, 14, 1, 3),
    _MsdslG703WorstIntervalUASs_Type()
)
msdslG703WorstIntervalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdslG703WorstIntervalUASs.setStatus("mandatory")
_MsdslG703WorstIntervalSESs_Type = Integer32
_MsdslG703WorstIntervalSESs_Object = MibTableColumn
msdslG703WorstIntervalSESs = _MsdslG703WorstIntervalSESs_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 14, 14, 1, 4),
    _MsdslG703WorstIntervalSESs_Type()
)
msdslG703WorstIntervalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdslG703WorstIntervalSESs.setStatus("mandatory")
_MsdslG703WorstIntervalBESs_Type = Integer32
_MsdslG703WorstIntervalBESs_Object = MibTableColumn
msdslG703WorstIntervalBESs = _MsdslG703WorstIntervalBESs_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 14, 14, 1, 5),
    _MsdslG703WorstIntervalBESs_Type()
)
msdslG703WorstIntervalBESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdslG703WorstIntervalBESs.setStatus("mandatory")
_MsdslG703WorstIntervalCSSs_Type = Integer32
_MsdslG703WorstIntervalCSSs_Object = MibTableColumn
msdslG703WorstIntervalCSSs = _MsdslG703WorstIntervalCSSs_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 14, 14, 1, 6),
    _MsdslG703WorstIntervalCSSs_Type()
)
msdslG703WorstIntervalCSSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdslG703WorstIntervalCSSs.setStatus("mandatory")
_MsdslG703WorstIntervalLOFC_Type = Integer32
_MsdslG703WorstIntervalLOFC_Object = MibTableColumn
msdslG703WorstIntervalLOFC = _MsdslG703WorstIntervalLOFC_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 14, 14, 1, 7),
    _MsdslG703WorstIntervalLOFC_Type()
)
msdslG703WorstIntervalLOFC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdslG703WorstIntervalLOFC.setStatus("mandatory")
_MsdslConfiguration_ObjectIdentity = ObjectIdentity
msdslConfiguration = _MsdslConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 15)
)
_MsdslFracTable_Object = MibTable
msdslFracTable = _MsdslFracTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 15, 28)
)
if mibBuilder.loadTexts:
    msdslFracTable.setStatus("mandatory")
_MsdslFracEntry_Object = MibTableRow
msdslFracEntry = _MsdslFracEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 15, 28, 1)
)
msdslFracEntry.setIndexNames(
    (0, "HOTWIRE-MSDSL-INTERFACE-MIB", "msdslFracPortIndex"),
    (0, "HOTWIRE-MSDSL-INTERFACE-MIB", "msdslFracPortTS"),
)
if mibBuilder.loadTexts:
    msdslFracEntry.setStatus("mandatory")
_MsdslFracPortIndex_Type = Integer32
_MsdslFracPortIndex_Object = MibTableColumn
msdslFracPortIndex = _MsdslFracPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 15, 28, 1, 1),
    _MsdslFracPortIndex_Type()
)
msdslFracPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdslFracPortIndex.setStatus("mandatory")


class _MsdslFracPortTS_Type(Integer32):
    """Custom type msdslFracPortTS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_MsdslFracPortTS_Type.__name__ = "Integer32"
_MsdslFracPortTS_Object = MibTableColumn
msdslFracPortTS = _MsdslFracPortTS_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 15, 28, 1, 2),
    _MsdslFracPortTS_Type()
)
msdslFracPortTS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msdslFracPortTS.setStatus("mandatory")
_MsdslFracPortIfIndex_Type = Integer32
_MsdslFracPortIfIndex_Object = MibTableColumn
msdslFracPortIfIndex = _MsdslFracPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 15, 28, 1, 3),
    _MsdslFracPortIfIndex_Type()
)
msdslFracPortIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msdslFracPortIfIndex.setStatus("mandatory")


class _MsdslFracPortIfTS_Type(Integer32):
    """Custom type msdslFracPortIfTS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_MsdslFracPortIfTS_Type.__name__ = "Integer32"
_MsdslFracPortIfTS_Object = MibTableColumn
msdslFracPortIfTS = _MsdslFracPortIfTS_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 15, 28, 1, 4),
    _MsdslFracPortIfTS_Type()
)
msdslFracPortIfTS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msdslFracPortIfTS.setStatus("mandatory")


class _MsdslFracPortVoiceData_Type(Integer32):
    """Custom type msdslFracPortVoiceData based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("data", 2),
          ("voice", 1))
    )


_MsdslFracPortVoiceData_Type.__name__ = "Integer32"
_MsdslFracPortVoiceData_Object = MibTableColumn
msdslFracPortVoiceData = _MsdslFracPortVoiceData_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 15, 28, 1, 5),
    _MsdslFracPortVoiceData_Type()
)
msdslFracPortVoiceData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msdslFracPortVoiceData.setStatus("mandatory")
_MsdslPortConfigAllocMethodTable_Object = MibTable
msdslPortConfigAllocMethodTable = _MsdslPortConfigAllocMethodTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 15, 29)
)
if mibBuilder.loadTexts:
    msdslPortConfigAllocMethodTable.setStatus("mandatory")
_MsdslPortConfigAllocMethodEntry_Object = MibTableRow
msdslPortConfigAllocMethodEntry = _MsdslPortConfigAllocMethodEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 15, 29, 1)
)
msdslPortConfigAllocMethodEntry.setIndexNames(
    (0, "HOTWIRE-MSDSL-INTERFACE-MIB", "msdslPortConfigAllocMethodIfIndex"),
)
if mibBuilder.loadTexts:
    msdslPortConfigAllocMethodEntry.setStatus("mandatory")
_MsdslPortConfigAllocMethodIfIndex_Type = Integer32
_MsdslPortConfigAllocMethodIfIndex_Object = MibTableColumn
msdslPortConfigAllocMethodIfIndex = _MsdslPortConfigAllocMethodIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 15, 29, 1, 1),
    _MsdslPortConfigAllocMethodIfIndex_Type()
)
msdslPortConfigAllocMethodIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdslPortConfigAllocMethodIfIndex.setStatus("mandatory")


class _MsdslPortConfigAllocMethod_Type(Integer32):
    """Custom type msdslPortConfigAllocMethod based on Integer32"""
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
        *(("disabled", 5),
          ("ds0CrossConn", 3),
          ("ds1ByPass", 1),
          ("ds1CrossConn", 2),
          ("notAssigned", 4))
    )


_MsdslPortConfigAllocMethod_Type.__name__ = "Integer32"
_MsdslPortConfigAllocMethod_Object = MibTableColumn
msdslPortConfigAllocMethod = _MsdslPortConfigAllocMethod_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 15, 29, 1, 2),
    _MsdslPortConfigAllocMethod_Type()
)
msdslPortConfigAllocMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msdslPortConfigAllocMethod.setStatus("mandatory")

# Managed Objects groups


# Notification objects

msdslMarginLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 0, 3)
)
msdslMarginLow.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    msdslMarginLow.setStatus(
        ""
    )

msdslErrorRateHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 0, 4)
)
msdslErrorRateHigh.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    msdslErrorRateHigh.setStatus(
        ""
    )

msdslNTUTypeMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 0, 7)
)
msdslNTUTypeMismatch.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    msdslNTUTypeMismatch.setStatus(
        ""
    )

msdslMarginNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 0, 103)
)
msdslMarginNormal.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    msdslMarginNormal.setStatus(
        ""
    )

msdslErrorRateNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 0, 104)
)
msdslErrorRateNormal.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    msdslErrorRateNormal.setStatus(
        ""
    )

msdslTestOver = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15, 1, 0, 106)
)
msdslTestOver.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    msdslTestOver.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HOTWIRE-MSDSL-INTERFACE-MIB",
    **{"msdslDevice": msdslDevice,
       "msdslMarginLow": msdslMarginLow,
       "msdslErrorRateHigh": msdslErrorRateHigh,
       "msdslNTUTypeMismatch": msdslNTUTypeMismatch,
       "msdslMarginNormal": msdslMarginNormal,
       "msdslErrorRateNormal": msdslErrorRateNormal,
       "msdslTestOver": msdslTestOver,
       "msdslCurrent": msdslCurrent,
       "msdslCurrentTable": msdslCurrentTable,
       "msdslCurrentEntry": msdslCurrentEntry,
       "msdslCurrentIfIndex": msdslCurrentIfIndex,
       "msdslCurrentESs": msdslCurrentESs,
       "msdslCurrentSESs": msdslCurrentSESs,
       "msdslCurrentFEBEs": msdslCurrentFEBEs,
       "msdslErrEventsCounter": msdslErrEventsCounter,
       "msdslErrTimeElapsed": msdslErrTimeElapsed,
       "msdslErrValidIntervals": msdslErrValidIntervals,
       "msdslInterval": msdslInterval,
       "msdslIntervalTable": msdslIntervalTable,
       "msdslIntervalEntry": msdslIntervalEntry,
       "msdslIntervalIfIndex": msdslIntervalIfIndex,
       "msdslIntervalNumber": msdslIntervalNumber,
       "msdslIntervalESs": msdslIntervalESs,
       "msdslIntervalSESs": msdslIntervalSESs,
       "msdslIntervalFEBEs": msdslIntervalFEBEs,
       "msdslWorstInterval": msdslWorstInterval,
       "msdslWorstIntervalTable": msdslWorstIntervalTable,
       "msdslWorstIntervalEntry": msdslWorstIntervalEntry,
       "msdslWorstIntervalIfIndex": msdslWorstIntervalIfIndex,
       "msdslWorstIntervalESs": msdslWorstIntervalESs,
       "msdslWorstIntervalSESs": msdslWorstIntervalSESs,
       "msdslWorstIntervalFEBEs": msdslWorstIntervalFEBEs,
       "msdslTotal": msdslTotal,
       "msdslTotalTable": msdslTotalTable,
       "msdslTotalEntry": msdslTotalEntry,
       "msdslTotalIfIndex": msdslTotalIfIndex,
       "msdslTotalESs": msdslTotalESs,
       "msdslTotalSESs": msdslTotalSESs,
       "msdslTotalFEBEs": msdslTotalFEBEs,
       "msdslFarEndCurrent": msdslFarEndCurrent,
       "msdslFarEndCurrentTable": msdslFarEndCurrentTable,
       "msdslFarEndCurrentEntry": msdslFarEndCurrentEntry,
       "msdslFarEndCurrentIfIndex": msdslFarEndCurrentIfIndex,
       "msdslFarEndCurrentESs": msdslFarEndCurrentESs,
       "msdslFarEndCurrentSESs": msdslFarEndCurrentSESs,
       "msdslFarEndCurrentFEBEs": msdslFarEndCurrentFEBEs,
       "msdslFarEndInterval": msdslFarEndInterval,
       "msdslFarEndIntervalTable": msdslFarEndIntervalTable,
       "msdslFarEndIntervalEntry": msdslFarEndIntervalEntry,
       "msdslFarEndIntervalIfIndex": msdslFarEndIntervalIfIndex,
       "msdslFarEndIntervalNumber": msdslFarEndIntervalNumber,
       "msdslFarEndIntervalESs": msdslFarEndIntervalESs,
       "msdslFarEndIntervalSESs": msdslFarEndIntervalSESs,
       "msdslFarEndIntervalFEBEs": msdslFarEndIntervalFEBEs,
       "msdslFarEndWorstInterval": msdslFarEndWorstInterval,
       "msdslFarEndWorstIntervalTable": msdslFarEndWorstIntervalTable,
       "msdslFarEndWorstIntervalEntry": msdslFarEndWorstIntervalEntry,
       "msdslFarEndWorstIntervalIfIndex": msdslFarEndWorstIntervalIfIndex,
       "msdslFarEndWorstIntervalESs": msdslFarEndWorstIntervalESs,
       "msdslFarEndWorstIntervalSESs": msdslFarEndWorstIntervalSESs,
       "msdslFarEndWorstIntervalFEBEs": msdslFarEndWorstIntervalFEBEs,
       "msdslFarEndTotal": msdslFarEndTotal,
       "msdslFarEndTotalTable": msdslFarEndTotalTable,
       "msdslFarEndTotalEntry": msdslFarEndTotalEntry,
       "msdslFarEndTotalIfIndex": msdslFarEndTotalIfIndex,
       "msdslFarEndTotalESs": msdslFarEndTotalESs,
       "msdslFarEndTotalSESs": msdslFarEndTotalSESs,
       "msdslFarEndTotalFEBEs": msdslFarEndTotalFEBEs,
       "msdslCurrentPerf": msdslCurrentPerf,
       "msdslCurrentPerfTable": msdslCurrentPerfTable,
       "msdslCurrentPerfEntry": msdslCurrentPerfEntry,
       "msdslCurrentPerfIfIndex": msdslCurrentPerfIfIndex,
       "msdslCurrentPerfMargin": msdslCurrentPerfMargin,
       "msdslCurrentPerfTxPwr": msdslCurrentPerfTxPwr,
       "msdslCurrentPerfRxGain": msdslCurrentPerfRxGain,
       "msdslPerfPayloadRate": msdslPerfPayloadRate,
       "msdslTimeElapsed": msdslTimeElapsed,
       "msdslValidIntervals": msdslValidIntervals,
       "msdslIntervalPerf": msdslIntervalPerf,
       "msdslIntervalPerfTable": msdslIntervalPerfTable,
       "msdslIntervalPerfEntry": msdslIntervalPerfEntry,
       "msdslIntervalPerfIfIndex": msdslIntervalPerfIfIndex,
       "msdslIntervalPerfNumber": msdslIntervalPerfNumber,
       "msdslIntervalPerfMargin": msdslIntervalPerfMargin,
       "msdslIntervalPerfTxPwr": msdslIntervalPerfTxPwr,
       "msdslIntervalPerfRxGain": msdslIntervalPerfRxGain,
       "msdslFarEndCurrentPerf": msdslFarEndCurrentPerf,
       "msdslFarEndCurrentPerfTable": msdslFarEndCurrentPerfTable,
       "msdslFarEndCurrentPerfEntry": msdslFarEndCurrentPerfEntry,
       "msdslFarEndCurrentPerfIfIndex": msdslFarEndCurrentPerfIfIndex,
       "msdslFarEndCurrentPerfMargin": msdslFarEndCurrentPerfMargin,
       "msdslFarEndCurrentPerfTxPwr": msdslFarEndCurrentPerfTxPwr,
       "msdslFarEndCurrentPerfRxGain": msdslFarEndCurrentPerfRxGain,
       "msdslFarEndIntervalPerf": msdslFarEndIntervalPerf,
       "msdslFarEndIntervalPerfTable": msdslFarEndIntervalPerfTable,
       "msdslFarEndIntervalPerfEntry": msdslFarEndIntervalPerfEntry,
       "msdslFarEndIntervalPerfIfIndex": msdslFarEndIntervalPerfIfIndex,
       "msdslFarEndIntervalPerfNumber": msdslFarEndIntervalPerfNumber,
       "msdslFarEndIntervalPerfMargin": msdslFarEndIntervalPerfMargin,
       "msdslFarEndIntervalPerfTxPwr": msdslFarEndIntervalPerfTxPwr,
       "msdslFarEndIntervalPerfRxGain": msdslFarEndIntervalPerfRxGain,
       "msdsldsx1WorstInterval": msdsldsx1WorstInterval,
       "msdsldsx1WorstIntervalTable": msdsldsx1WorstIntervalTable,
       "msdsldsx1WorstIntervalEntry": msdsldsx1WorstIntervalEntry,
       "msdsldsx1WorstIntervalIfIndex": msdsldsx1WorstIntervalIfIndex,
       "msdsldsx1WorstIntervalESs": msdsldsx1WorstIntervalESs,
       "msdsldsx1WorstIntervalUASs": msdsldsx1WorstIntervalUASs,
       "msdsldsx1WorstIntervalSESs": msdsldsx1WorstIntervalSESs,
       "msdsldsx1WorstIntervalBESs": msdsldsx1WorstIntervalBESs,
       "msdsldsx1WorstIntervalCSSs": msdsldsx1WorstIntervalCSSs,
       "msdsldsx1WorstIntervalLOFC": msdsldsx1WorstIntervalLOFC,
       "msdslG703WorstInterval": msdslG703WorstInterval,
       "msdslG703WorstIntervalTable": msdslG703WorstIntervalTable,
       "msdslG703WorstIntervalEntry": msdslG703WorstIntervalEntry,
       "msdslG703WorstIntervalIfIndex": msdslG703WorstIntervalIfIndex,
       "msdslG703WorstIntervalESs": msdslG703WorstIntervalESs,
       "msdslG703WorstIntervalUASs": msdslG703WorstIntervalUASs,
       "msdslG703WorstIntervalSESs": msdslG703WorstIntervalSESs,
       "msdslG703WorstIntervalBESs": msdslG703WorstIntervalBESs,
       "msdslG703WorstIntervalCSSs": msdslG703WorstIntervalCSSs,
       "msdslG703WorstIntervalLOFC": msdslG703WorstIntervalLOFC,
       "msdslConfiguration": msdslConfiguration,
       "msdslFracTable": msdslFracTable,
       "msdslFracEntry": msdslFracEntry,
       "msdslFracPortIndex": msdslFracPortIndex,
       "msdslFracPortTS": msdslFracPortTS,
       "msdslFracPortIfIndex": msdslFracPortIfIndex,
       "msdslFracPortIfTS": msdslFracPortIfTS,
       "msdslFracPortVoiceData": msdslFracPortVoiceData,
       "msdslPortConfigAllocMethodTable": msdslPortConfigAllocMethodTable,
       "msdslPortConfigAllocMethodEntry": msdslPortConfigAllocMethodEntry,
       "msdslPortConfigAllocMethodIfIndex": msdslPortConfigAllocMethodIfIndex,
       "msdslPortConfigAllocMethod": msdslPortConfigAllocMethod}
)
