# SNMP MIB module (Wellfleet-CCTOPTS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-CCTOPTS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:15:56 2024
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

(wfCircuitOptsGroup,) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfCircuitOptsGroup")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfCctOptsTable_Object = MibTable
wfCctOptsTable = _WfCctOptsTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 1)
)
if mibBuilder.loadTexts:
    wfCctOptsTable.setStatus("mandatory")
_WfCctOptsEntry_Object = MibTableRow
wfCctOptsEntry = _WfCctOptsEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 1, 1)
)
wfCctOptsEntry.setIndexNames(
    (0, "Wellfleet-CCTOPTS-MIB", "wfCctOptsCct"),
)
if mibBuilder.loadTexts:
    wfCctOptsEntry.setStatus("mandatory")


class _WfCctOptsDelete_Type(Integer32):
    """Custom type wfCctOptsDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfCctOptsDelete_Type.__name__ = "Integer32"
_WfCctOptsDelete_Object = MibTableColumn
wfCctOptsDelete = _WfCctOptsDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 1, 1, 1),
    _WfCctOptsDelete_Type()
)
wfCctOptsDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCctOptsDelete.setStatus("mandatory")


class _WfCctOptsPriorityQueueingDisable_Type(Integer32):
    """Custom type wfCctOptsPriorityQueueingDisable based on Integer32"""
    defaultValue = 1

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


_WfCctOptsPriorityQueueingDisable_Type.__name__ = "Integer32"
_WfCctOptsPriorityQueueingDisable_Object = MibTableColumn
wfCctOptsPriorityQueueingDisable = _WfCctOptsPriorityQueueingDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 1, 1, 2),
    _WfCctOptsPriorityQueueingDisable_Type()
)
wfCctOptsPriorityQueueingDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCctOptsPriorityQueueingDisable.setStatus("mandatory")
_WfCctOptsCct_Type = Integer32
_WfCctOptsCct_Object = MibTableColumn
wfCctOptsCct = _WfCctOptsCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 1, 1, 3),
    _WfCctOptsCct_Type()
)
wfCctOptsCct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCctOptsCct.setStatus("mandatory")


class _WfCctOptsHighPriorityQueueLimit_Type(Integer32):
    """Custom type wfCctOptsHighPriorityQueueLimit based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            20
        )
    )
    namedValues = NamedValues(
        ("default", 20)
    )


_WfCctOptsHighPriorityQueueLimit_Type.__name__ = "Integer32"
_WfCctOptsHighPriorityQueueLimit_Object = MibTableColumn
wfCctOptsHighPriorityQueueLimit = _WfCctOptsHighPriorityQueueLimit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 1, 1, 4),
    _WfCctOptsHighPriorityQueueLimit_Type()
)
wfCctOptsHighPriorityQueueLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCctOptsHighPriorityQueueLimit.setStatus("mandatory")


class _WfCctOptsNormalPriorityQueueLimit_Type(Integer32):
    """Custom type wfCctOptsNormalPriorityQueueLimit based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            20
        )
    )
    namedValues = NamedValues(
        ("default", 20)
    )


_WfCctOptsNormalPriorityQueueLimit_Type.__name__ = "Integer32"
_WfCctOptsNormalPriorityQueueLimit_Object = MibTableColumn
wfCctOptsNormalPriorityQueueLimit = _WfCctOptsNormalPriorityQueueLimit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 1, 1, 5),
    _WfCctOptsNormalPriorityQueueLimit_Type()
)
wfCctOptsNormalPriorityQueueLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCctOptsNormalPriorityQueueLimit.setStatus("mandatory")


class _WfCctOptsLowPriorityQueueLimit_Type(Integer32):
    """Custom type wfCctOptsLowPriorityQueueLimit based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            20
        )
    )
    namedValues = NamedValues(
        ("default", 20)
    )


_WfCctOptsLowPriorityQueueLimit_Type.__name__ = "Integer32"
_WfCctOptsLowPriorityQueueLimit_Object = MibTableColumn
wfCctOptsLowPriorityQueueLimit = _WfCctOptsLowPriorityQueueLimit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 1, 1, 6),
    _WfCctOptsLowPriorityQueueLimit_Type()
)
wfCctOptsLowPriorityQueueLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCctOptsLowPriorityQueueLimit.setStatus("mandatory")


class _WfCctOptsMaxInterruptQueueLatency_Type(Integer32):
    """Custom type wfCctOptsMaxInterruptQueueLatency based on Integer32"""
    defaultValue = 2500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 5000),
    )


_WfCctOptsMaxInterruptQueueLatency_Type.__name__ = "Integer32"
_WfCctOptsMaxInterruptQueueLatency_Object = MibTableColumn
wfCctOptsMaxInterruptQueueLatency = _WfCctOptsMaxInterruptQueueLatency_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 1, 1, 7),
    _WfCctOptsMaxInterruptQueueLatency_Type()
)
wfCctOptsMaxInterruptQueueLatency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCctOptsMaxInterruptQueueLatency.setStatus("mandatory")


class _WfCctOptsMaxHighPriorityQueueLatency_Type(Integer32):
    """Custom type wfCctOptsMaxHighPriorityQueueLatency based on Integer32"""
    defaultValue = 250

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 5000),
    )


_WfCctOptsMaxHighPriorityQueueLatency_Type.__name__ = "Integer32"
_WfCctOptsMaxHighPriorityQueueLatency_Object = MibTableColumn
wfCctOptsMaxHighPriorityQueueLatency = _WfCctOptsMaxHighPriorityQueueLatency_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 1, 1, 8),
    _WfCctOptsMaxHighPriorityQueueLatency_Type()
)
wfCctOptsMaxHighPriorityQueueLatency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCctOptsMaxHighPriorityQueueLatency.setStatus("mandatory")
_WfCctOptsHiXmits_Type = Counter32
_WfCctOptsHiXmits_Object = MibTableColumn
wfCctOptsHiXmits = _WfCctOptsHiXmits_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 1, 1, 9),
    _WfCctOptsHiXmits_Type()
)
wfCctOptsHiXmits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCctOptsHiXmits.setStatus("mandatory")
_WfCctOptsNormalXmits_Type = Counter32
_WfCctOptsNormalXmits_Object = MibTableColumn
wfCctOptsNormalXmits = _WfCctOptsNormalXmits_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 1, 1, 10),
    _WfCctOptsNormalXmits_Type()
)
wfCctOptsNormalXmits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCctOptsNormalXmits.setStatus("mandatory")
_WfCctOptsLoXmits_Type = Counter32
_WfCctOptsLoXmits_Object = MibTableColumn
wfCctOptsLoXmits = _WfCctOptsLoXmits_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 1, 1, 11),
    _WfCctOptsLoXmits_Type()
)
wfCctOptsLoXmits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCctOptsLoXmits.setStatus("mandatory")
_WfCctOptsHiClippedPkts_Type = Counter32
_WfCctOptsHiClippedPkts_Object = MibTableColumn
wfCctOptsHiClippedPkts = _WfCctOptsHiClippedPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 1, 1, 12),
    _WfCctOptsHiClippedPkts_Type()
)
wfCctOptsHiClippedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCctOptsHiClippedPkts.setStatus("mandatory")
_WfCctOptsNormalClippedPkts_Type = Counter32
_WfCctOptsNormalClippedPkts_Object = MibTableColumn
wfCctOptsNormalClippedPkts = _WfCctOptsNormalClippedPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 1, 1, 13),
    _WfCctOptsNormalClippedPkts_Type()
)
wfCctOptsNormalClippedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCctOptsNormalClippedPkts.setStatus("mandatory")
_WfCctOptsLoClippedPkts_Type = Counter32
_WfCctOptsLoClippedPkts_Object = MibTableColumn
wfCctOptsLoClippedPkts = _WfCctOptsLoClippedPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 1, 1, 14),
    _WfCctOptsLoClippedPkts_Type()
)
wfCctOptsLoClippedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCctOptsLoClippedPkts.setStatus("mandatory")
_WfCctOptsIntrQHighWaterPkts_Type = Gauge32
_WfCctOptsIntrQHighWaterPkts_Object = MibTableColumn
wfCctOptsIntrQHighWaterPkts = _WfCctOptsIntrQHighWaterPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 1, 1, 15),
    _WfCctOptsIntrQHighWaterPkts_Type()
)
wfCctOptsIntrQHighWaterPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCctOptsIntrQHighWaterPkts.setStatus("mandatory")
_WfCctOptsHiQHighWaterPkts_Type = Gauge32
_WfCctOptsHiQHighWaterPkts_Object = MibTableColumn
wfCctOptsHiQHighWaterPkts = _WfCctOptsHiQHighWaterPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 1, 1, 16),
    _WfCctOptsHiQHighWaterPkts_Type()
)
wfCctOptsHiQHighWaterPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCctOptsHiQHighWaterPkts.setStatus("mandatory")
_WfCctOptsNormalQHighWaterPkts_Type = Gauge32
_WfCctOptsNormalQHighWaterPkts_Object = MibTableColumn
wfCctOptsNormalQHighWaterPkts = _WfCctOptsNormalQHighWaterPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 1, 1, 17),
    _WfCctOptsNormalQHighWaterPkts_Type()
)
wfCctOptsNormalQHighWaterPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCctOptsNormalQHighWaterPkts.setStatus("mandatory")
_WfCctOptsLoQHighWaterPkts_Type = Gauge32
_WfCctOptsLoQHighWaterPkts_Object = MibTableColumn
wfCctOptsLoQHighWaterPkts = _WfCctOptsLoQHighWaterPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 1, 1, 18),
    _WfCctOptsLoQHighWaterPkts_Type()
)
wfCctOptsLoQHighWaterPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCctOptsLoQHighWaterPkts.setStatus("mandatory")
_WfCctOptsHighWaterPktsClear_Type = Integer32
_WfCctOptsHighWaterPktsClear_Object = MibTableColumn
wfCctOptsHighWaterPktsClear = _WfCctOptsHighWaterPktsClear_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 1, 1, 19),
    _WfCctOptsHighWaterPktsClear_Type()
)
wfCctOptsHighWaterPktsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCctOptsHighWaterPktsClear.setStatus("mandatory")
_WfCctOptsDroppedPkts_Type = Counter32
_WfCctOptsDroppedPkts_Object = MibTableColumn
wfCctOptsDroppedPkts = _WfCctOptsDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 1, 1, 20),
    _WfCctOptsDroppedPkts_Type()
)
wfCctOptsDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCctOptsDroppedPkts.setStatus("mandatory")
_WfCctOptsLargePkts_Type = Counter32
_WfCctOptsLargePkts_Object = MibTableColumn
wfCctOptsLargePkts = _WfCctOptsLargePkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 1, 1, 21),
    _WfCctOptsLargePkts_Type()
)
wfCctOptsLargePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCctOptsLargePkts.setStatus("mandatory")
_WfCctOptsRxPkts_Type = Counter32
_WfCctOptsRxPkts_Object = MibTableColumn
wfCctOptsRxPkts = _WfCctOptsRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 1, 1, 22),
    _WfCctOptsRxPkts_Type()
)
wfCctOptsRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCctOptsRxPkts.setStatus("mandatory")


class _WfCctOptsChooserType_Type(Integer32):
    """Custom type wfCctOptsChooserType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("addrbased", 2),
          ("multilinkfr", 3),
          ("random", 1))
    )


_WfCctOptsChooserType_Type.__name__ = "Integer32"
_WfCctOptsChooserType_Object = MibTableColumn
wfCctOptsChooserType = _WfCctOptsChooserType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 1, 1, 23),
    _WfCctOptsChooserType_Type()
)
wfCctOptsChooserType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCctOptsChooserType.setStatus("mandatory")


class _WfCctOptsPqDequeueAlgType_Type(Integer32):
    """Custom type wfCctOptsPqDequeueAlgType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allocation", 2),
          ("prioritization", 1))
    )


_WfCctOptsPqDequeueAlgType_Type.__name__ = "Integer32"
_WfCctOptsPqDequeueAlgType_Object = MibTableColumn
wfCctOptsPqDequeueAlgType = _WfCctOptsPqDequeueAlgType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 1, 1, 24),
    _WfCctOptsPqDequeueAlgType_Type()
)
wfCctOptsPqDequeueAlgType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCctOptsPqDequeueAlgType.setStatus("mandatory")


class _WfCctOptsHiPercent_Type(Integer32):
    """Custom type wfCctOptsHiPercent based on Integer32"""
    defaultValue = 70

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            70
        )
    )
    namedValues = NamedValues(
        ("default", 70)
    )


_WfCctOptsHiPercent_Type.__name__ = "Integer32"
_WfCctOptsHiPercent_Object = MibTableColumn
wfCctOptsHiPercent = _WfCctOptsHiPercent_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 1, 1, 25),
    _WfCctOptsHiPercent_Type()
)
wfCctOptsHiPercent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCctOptsHiPercent.setStatus("mandatory")


class _WfCctOptsNormalPercent_Type(Integer32):
    """Custom type wfCctOptsNormalPercent based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            20
        )
    )
    namedValues = NamedValues(
        ("default", 20)
    )


_WfCctOptsNormalPercent_Type.__name__ = "Integer32"
_WfCctOptsNormalPercent_Object = MibTableColumn
wfCctOptsNormalPercent = _WfCctOptsNormalPercent_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 1, 1, 26),
    _WfCctOptsNormalPercent_Type()
)
wfCctOptsNormalPercent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCctOptsNormalPercent.setStatus("mandatory")


class _WfCctOptsLoPercent_Type(Integer32):
    """Custom type wfCctOptsLoPercent based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            10
        )
    )
    namedValues = NamedValues(
        ("default", 10)
    )


_WfCctOptsLoPercent_Type.__name__ = "Integer32"
_WfCctOptsLoPercent_Object = MibTableColumn
wfCctOptsLoPercent = _WfCctOptsLoPercent_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 1, 1, 27),
    _WfCctOptsLoPercent_Type()
)
wfCctOptsLoPercent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCctOptsLoPercent.setStatus("mandatory")
_WfCctOptsHiTotalOctets_Type = Counter32
_WfCctOptsHiTotalOctets_Object = MibTableColumn
wfCctOptsHiTotalOctets = _WfCctOptsHiTotalOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 1, 1, 28),
    _WfCctOptsHiTotalOctets_Type()
)
wfCctOptsHiTotalOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCctOptsHiTotalOctets.setStatus("mandatory")
_WfCctOptsNormalTotalOctets_Type = Counter32
_WfCctOptsNormalTotalOctets_Object = MibTableColumn
wfCctOptsNormalTotalOctets = _WfCctOptsNormalTotalOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 1, 1, 29),
    _WfCctOptsNormalTotalOctets_Type()
)
wfCctOptsNormalTotalOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCctOptsNormalTotalOctets.setStatus("mandatory")
_WfCctOptsLoTotalOctets_Type = Counter32
_WfCctOptsLoTotalOctets_Object = MibTableColumn
wfCctOptsLoTotalOctets = _WfCctOptsLoTotalOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 1, 1, 30),
    _WfCctOptsLoTotalOctets_Type()
)
wfCctOptsLoTotalOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCctOptsLoTotalOctets.setStatus("mandatory")


class _WfCctOptsCircuitType_Type(Integer32):
    """Custom type wfCctOptsCircuitType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              99)
        )
    )
    namedValues = NamedValues(
        *(("bandwidthondemand", 4),
          ("dialondemand", 3),
          ("normal", 1),
          ("primary", 2),
          ("standbyprimary", 5),
          ("unused", 99))
    )


_WfCctOptsCircuitType_Type.__name__ = "Integer32"
_WfCctOptsCircuitType_Object = MibTableColumn
wfCctOptsCircuitType = _WfCctOptsCircuitType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 1, 1, 31),
    _WfCctOptsCircuitType_Type()
)
wfCctOptsCircuitType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCctOptsCircuitType.setStatus("mandatory")
_WfCctOptsBackupCct_Type = Integer32
_WfCctOptsBackupCct_Object = MibTableColumn
wfCctOptsBackupCct = _WfCctOptsBackupCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 1, 1, 32),
    _WfCctOptsBackupCct_Type()
)
wfCctOptsBackupCct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCctOptsBackupCct.setStatus("mandatory")


class _WfCctOptsPrimaryCctWanProtocolType_Type(Integer32):
    """Custom type wfCctOptsPrimaryCctWanProtocolType based on Integer32"""
    defaultValue = 1

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
        *(("ppp", 2),
          ("relay", 3),
          ("sync", 4),
          ("unknown", 1))
    )


_WfCctOptsPrimaryCctWanProtocolType_Type.__name__ = "Integer32"
_WfCctOptsPrimaryCctWanProtocolType_Object = MibTableColumn
wfCctOptsPrimaryCctWanProtocolType = _WfCctOptsPrimaryCctWanProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 1, 1, 33),
    _WfCctOptsPrimaryCctWanProtocolType_Type()
)
wfCctOptsPrimaryCctWanProtocolType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCctOptsPrimaryCctWanProtocolType.setStatus("mandatory")


class _WfCctOptsMacFilterFormat_Type(Integer32):
    """Custom type wfCctOptsMacFilterFormat based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("tokenring", 2))
    )


_WfCctOptsMacFilterFormat_Type.__name__ = "Integer32"
_WfCctOptsMacFilterFormat_Object = MibTableColumn
wfCctOptsMacFilterFormat = _WfCctOptsMacFilterFormat_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 1, 1, 34),
    _WfCctOptsMacFilterFormat_Type()
)
wfCctOptsMacFilterFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCctOptsMacFilterFormat.setStatus("mandatory")
_WfCctOptsPktsNotQueued_Type = Counter32
_WfCctOptsPktsNotQueued_Object = MibTableColumn
wfCctOptsPktsNotQueued = _WfCctOptsPktsNotQueued_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 1, 1, 35),
    _WfCctOptsPktsNotQueued_Type()
)
wfCctOptsPktsNotQueued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCctOptsPktsNotQueued.setStatus("mandatory")


class _WfCctOptsBitsShiftCount_Type(Integer32):
    """Custom type wfCctOptsBitsShiftCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_WfCctOptsBitsShiftCount_Type.__name__ = "Integer32"
_WfCctOptsBitsShiftCount_Object = MibTableColumn
wfCctOptsBitsShiftCount = _WfCctOptsBitsShiftCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 1, 1, 36),
    _WfCctOptsBitsShiftCount_Type()
)
wfCctOptsBitsShiftCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCctOptsBitsShiftCount.setStatus("mandatory")


class _WfCctOptsFrSetDeLowQ_Type(Integer32):
    """Custom type wfCctOptsFrSetDeLowQ based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("dontsetdebit", 2))
    )


_WfCctOptsFrSetDeLowQ_Type.__name__ = "Integer32"
_WfCctOptsFrSetDeLowQ_Object = MibTableColumn
wfCctOptsFrSetDeLowQ = _WfCctOptsFrSetDeLowQ_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 1, 1, 37),
    _WfCctOptsFrSetDeLowQ_Type()
)
wfCctOptsFrSetDeLowQ.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCctOptsFrSetDeLowQ.setStatus("mandatory")


class _WfCctOptsFrSetDeNormQ_Type(Integer32):
    """Custom type wfCctOptsFrSetDeNormQ based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("setdebit", 2))
    )


_WfCctOptsFrSetDeNormQ_Type.__name__ = "Integer32"
_WfCctOptsFrSetDeNormQ_Object = MibTableColumn
wfCctOptsFrSetDeNormQ = _WfCctOptsFrSetDeNormQ_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 1, 1, 38),
    _WfCctOptsFrSetDeNormQ_Type()
)
wfCctOptsFrSetDeNormQ.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCctOptsFrSetDeNormQ.setStatus("mandatory")


class _WfCctOptsShapedPriorityQueueLimit_Type(Integer32):
    """Custom type wfCctOptsShapedPriorityQueueLimit based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            200
        )
    )
    namedValues = NamedValues(
        ("default", 200)
    )


_WfCctOptsShapedPriorityQueueLimit_Type.__name__ = "Integer32"
_WfCctOptsShapedPriorityQueueLimit_Object = MibTableColumn
wfCctOptsShapedPriorityQueueLimit = _WfCctOptsShapedPriorityQueueLimit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 1, 1, 39),
    _WfCctOptsShapedPriorityQueueLimit_Type()
)
wfCctOptsShapedPriorityQueueLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCctOptsShapedPriorityQueueLimit.setStatus("mandatory")


class _WfCctOptsMaxShapedPriorityQueueLatency_Type(Integer32):
    """Custom type wfCctOptsMaxShapedPriorityQueueLatency based on Integer32"""
    defaultValue = 250

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 5000),
    )


_WfCctOptsMaxShapedPriorityQueueLatency_Type.__name__ = "Integer32"
_WfCctOptsMaxShapedPriorityQueueLatency_Object = MibTableColumn
wfCctOptsMaxShapedPriorityQueueLatency = _WfCctOptsMaxShapedPriorityQueueLatency_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 1, 1, 40),
    _WfCctOptsMaxShapedPriorityQueueLatency_Type()
)
wfCctOptsMaxShapedPriorityQueueLatency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCctOptsMaxShapedPriorityQueueLatency.setStatus("mandatory")
_WfCctOptsShapedXmits_Type = Counter32
_WfCctOptsShapedXmits_Object = MibTableColumn
wfCctOptsShapedXmits = _WfCctOptsShapedXmits_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 1, 1, 41),
    _WfCctOptsShapedXmits_Type()
)
wfCctOptsShapedXmits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCctOptsShapedXmits.setStatus("mandatory")
_WfCctOptsShapedClippedPkts_Type = Counter32
_WfCctOptsShapedClippedPkts_Object = MibTableColumn
wfCctOptsShapedClippedPkts = _WfCctOptsShapedClippedPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 1, 1, 42),
    _WfCctOptsShapedClippedPkts_Type()
)
wfCctOptsShapedClippedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCctOptsShapedClippedPkts.setStatus("mandatory")
_WfCctOptsShapedQHighWaterPkts_Type = Gauge32
_WfCctOptsShapedQHighWaterPkts_Object = MibTableColumn
wfCctOptsShapedQHighWaterPkts = _WfCctOptsShapedQHighWaterPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 1, 1, 43),
    _WfCctOptsShapedQHighWaterPkts_Type()
)
wfCctOptsShapedQHighWaterPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCctOptsShapedQHighWaterPkts.setStatus("mandatory")
_WfCctOptsShapedTotalOctets_Type = Counter32
_WfCctOptsShapedTotalOctets_Object = MibTableColumn
wfCctOptsShapedTotalOctets = _WfCctOptsShapedTotalOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 1, 1, 44),
    _WfCctOptsShapedTotalOctets_Type()
)
wfCctOptsShapedTotalOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCctOptsShapedTotalOctets.setStatus("mandatory")


class _WfCctOptsPpqDebugLevel_Type(Integer32):
    """Custom type wfCctOptsPpqDebugLevel based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_WfCctOptsPpqDebugLevel_Type.__name__ = "Integer32"
_WfCctOptsPpqDebugLevel_Object = MibTableColumn
wfCctOptsPpqDebugLevel = _WfCctOptsPpqDebugLevel_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 1, 1, 45),
    _WfCctOptsPpqDebugLevel_Type()
)
wfCctOptsPpqDebugLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCctOptsPpqDebugLevel.setStatus("mandatory")


class _WfDequeueAtLineRate_Type(Integer32):
    """Custom type wfDequeueAtLineRate based on Integer32"""
    defaultValue = 2

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


_WfDequeueAtLineRate_Type.__name__ = "Integer32"
_WfDequeueAtLineRate_Object = MibTableColumn
wfDequeueAtLineRate = _WfDequeueAtLineRate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 1, 1, 46),
    _WfDequeueAtLineRate_Type()
)
wfDequeueAtLineRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDequeueAtLineRate.setStatus("mandatory")
_WfCctOptsBrFilterTable_Object = MibTable
wfCctOptsBrFilterTable = _WfCctOptsBrFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 2)
)
if mibBuilder.loadTexts:
    wfCctOptsBrFilterTable.setStatus("mandatory")
_WfCctOptsBrFilterEntry_Object = MibTableRow
wfCctOptsBrFilterEntry = _WfCctOptsBrFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 2, 1)
)
wfCctOptsBrFilterEntry.setIndexNames(
    (0, "Wellfleet-CCTOPTS-MIB", "wfCctOptsBrFilterCct"),
    (0, "Wellfleet-CCTOPTS-MIB", "wfCctOptsBrFilterRuleNumber"),
    (0, "Wellfleet-CCTOPTS-MIB", "wfCctOptsBrFilterFragment"),
)
if mibBuilder.loadTexts:
    wfCctOptsBrFilterEntry.setStatus("mandatory")


class _WfCctOptsBrFilterCreate_Type(Integer32):
    """Custom type wfCctOptsBrFilterCreate based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfCctOptsBrFilterCreate_Type.__name__ = "Integer32"
_WfCctOptsBrFilterCreate_Object = MibTableColumn
wfCctOptsBrFilterCreate = _WfCctOptsBrFilterCreate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 2, 1, 1),
    _WfCctOptsBrFilterCreate_Type()
)
wfCctOptsBrFilterCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCctOptsBrFilterCreate.setStatus("mandatory")


class _WfCctOptsBrFilterEnable_Type(Integer32):
    """Custom type wfCctOptsBrFilterEnable based on Integer32"""
    defaultValue = 1

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


_WfCctOptsBrFilterEnable_Type.__name__ = "Integer32"
_WfCctOptsBrFilterEnable_Object = MibTableColumn
wfCctOptsBrFilterEnable = _WfCctOptsBrFilterEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 2, 1, 2),
    _WfCctOptsBrFilterEnable_Type()
)
wfCctOptsBrFilterEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCctOptsBrFilterEnable.setStatus("mandatory")


class _WfCctOptsBrFilterState_Type(Integer32):
    """Custom type wfCctOptsBrFilterState based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("error", 2),
          ("inactive", 3))
    )


_WfCctOptsBrFilterState_Type.__name__ = "Integer32"
_WfCctOptsBrFilterState_Object = MibTableColumn
wfCctOptsBrFilterState = _WfCctOptsBrFilterState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 2, 1, 3),
    _WfCctOptsBrFilterState_Type()
)
wfCctOptsBrFilterState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCctOptsBrFilterState.setStatus("mandatory")
_WfCctOptsBrFilterCounter_Type = Counter32
_WfCctOptsBrFilterCounter_Object = MibTableColumn
wfCctOptsBrFilterCounter = _WfCctOptsBrFilterCounter_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 2, 1, 4),
    _WfCctOptsBrFilterCounter_Type()
)
wfCctOptsBrFilterCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCctOptsBrFilterCounter.setStatus("mandatory")
_WfCctOptsBrFilterDefinition_Type = OctetString
_WfCctOptsBrFilterDefinition_Object = MibTableColumn
wfCctOptsBrFilterDefinition = _WfCctOptsBrFilterDefinition_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 2, 1, 5),
    _WfCctOptsBrFilterDefinition_Type()
)
wfCctOptsBrFilterDefinition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCctOptsBrFilterDefinition.setStatus("mandatory")
_WfCctOptsBrFilterReserved_Type = Integer32
_WfCctOptsBrFilterReserved_Object = MibTableColumn
wfCctOptsBrFilterReserved = _WfCctOptsBrFilterReserved_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 2, 1, 6),
    _WfCctOptsBrFilterReserved_Type()
)
wfCctOptsBrFilterReserved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCctOptsBrFilterReserved.setStatus("mandatory")
_WfCctOptsBrFilterCct_Type = Integer32
_WfCctOptsBrFilterCct_Object = MibTableColumn
wfCctOptsBrFilterCct = _WfCctOptsBrFilterCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 2, 1, 7),
    _WfCctOptsBrFilterCct_Type()
)
wfCctOptsBrFilterCct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCctOptsBrFilterCct.setStatus("mandatory")
_WfCctOptsBrFilterRuleNumber_Type = Integer32
_WfCctOptsBrFilterRuleNumber_Object = MibTableColumn
wfCctOptsBrFilterRuleNumber = _WfCctOptsBrFilterRuleNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 2, 1, 8),
    _WfCctOptsBrFilterRuleNumber_Type()
)
wfCctOptsBrFilterRuleNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCctOptsBrFilterRuleNumber.setStatus("mandatory")
_WfCctOptsBrFilterFragment_Type = Integer32
_WfCctOptsBrFilterFragment_Object = MibTableColumn
wfCctOptsBrFilterFragment = _WfCctOptsBrFilterFragment_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 2, 1, 9),
    _WfCctOptsBrFilterFragment_Type()
)
wfCctOptsBrFilterFragment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCctOptsBrFilterFragment.setStatus("mandatory")
_WfCctOptsBrFilterName_Type = DisplayString
_WfCctOptsBrFilterName_Object = MibTableColumn
wfCctOptsBrFilterName = _WfCctOptsBrFilterName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 2, 1, 10),
    _WfCctOptsBrFilterName_Type()
)
wfCctOptsBrFilterName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCctOptsBrFilterName.setStatus("mandatory")
_WfCctOptsIpFilterTable_Object = MibTable
wfCctOptsIpFilterTable = _WfCctOptsIpFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 3)
)
if mibBuilder.loadTexts:
    wfCctOptsIpFilterTable.setStatus("mandatory")
_WfCctOptsIpFilterEntry_Object = MibTableRow
wfCctOptsIpFilterEntry = _WfCctOptsIpFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 3, 1)
)
wfCctOptsIpFilterEntry.setIndexNames(
    (0, "Wellfleet-CCTOPTS-MIB", "wfCctOptsIpFilterCct"),
    (0, "Wellfleet-CCTOPTS-MIB", "wfCctOptsIpFilterRuleNumber"),
    (0, "Wellfleet-CCTOPTS-MIB", "wfCctOptsIpFilterFragment"),
)
if mibBuilder.loadTexts:
    wfCctOptsIpFilterEntry.setStatus("mandatory")


class _WfCctOptsIpFilterCreate_Type(Integer32):
    """Custom type wfCctOptsIpFilterCreate based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfCctOptsIpFilterCreate_Type.__name__ = "Integer32"
_WfCctOptsIpFilterCreate_Object = MibTableColumn
wfCctOptsIpFilterCreate = _WfCctOptsIpFilterCreate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 3, 1, 1),
    _WfCctOptsIpFilterCreate_Type()
)
wfCctOptsIpFilterCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCctOptsIpFilterCreate.setStatus("mandatory")


class _WfCctOptsIpFilterEnable_Type(Integer32):
    """Custom type wfCctOptsIpFilterEnable based on Integer32"""
    defaultValue = 1

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


_WfCctOptsIpFilterEnable_Type.__name__ = "Integer32"
_WfCctOptsIpFilterEnable_Object = MibTableColumn
wfCctOptsIpFilterEnable = _WfCctOptsIpFilterEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 3, 1, 2),
    _WfCctOptsIpFilterEnable_Type()
)
wfCctOptsIpFilterEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCctOptsIpFilterEnable.setStatus("mandatory")


class _WfCctOptsIpFilterState_Type(Integer32):
    """Custom type wfCctOptsIpFilterState based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("error", 2),
          ("inactive", 3))
    )


_WfCctOptsIpFilterState_Type.__name__ = "Integer32"
_WfCctOptsIpFilterState_Object = MibTableColumn
wfCctOptsIpFilterState = _WfCctOptsIpFilterState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 3, 1, 3),
    _WfCctOptsIpFilterState_Type()
)
wfCctOptsIpFilterState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCctOptsIpFilterState.setStatus("mandatory")
_WfCctOptsIpFilterCounter_Type = Counter32
_WfCctOptsIpFilterCounter_Object = MibTableColumn
wfCctOptsIpFilterCounter = _WfCctOptsIpFilterCounter_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 3, 1, 4),
    _WfCctOptsIpFilterCounter_Type()
)
wfCctOptsIpFilterCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCctOptsIpFilterCounter.setStatus("mandatory")
_WfCctOptsIpFilterDefinition_Type = OctetString
_WfCctOptsIpFilterDefinition_Object = MibTableColumn
wfCctOptsIpFilterDefinition = _WfCctOptsIpFilterDefinition_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 3, 1, 5),
    _WfCctOptsIpFilterDefinition_Type()
)
wfCctOptsIpFilterDefinition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCctOptsIpFilterDefinition.setStatus("mandatory")
_WfCctOptsIpFilterReserved_Type = Integer32
_WfCctOptsIpFilterReserved_Object = MibTableColumn
wfCctOptsIpFilterReserved = _WfCctOptsIpFilterReserved_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 3, 1, 6),
    _WfCctOptsIpFilterReserved_Type()
)
wfCctOptsIpFilterReserved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCctOptsIpFilterReserved.setStatus("mandatory")
_WfCctOptsIpFilterCct_Type = Integer32
_WfCctOptsIpFilterCct_Object = MibTableColumn
wfCctOptsIpFilterCct = _WfCctOptsIpFilterCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 3, 1, 7),
    _WfCctOptsIpFilterCct_Type()
)
wfCctOptsIpFilterCct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCctOptsIpFilterCct.setStatus("mandatory")
_WfCctOptsIpFilterRuleNumber_Type = Integer32
_WfCctOptsIpFilterRuleNumber_Object = MibTableColumn
wfCctOptsIpFilterRuleNumber = _WfCctOptsIpFilterRuleNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 3, 1, 8),
    _WfCctOptsIpFilterRuleNumber_Type()
)
wfCctOptsIpFilterRuleNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCctOptsIpFilterRuleNumber.setStatus("mandatory")
_WfCctOptsIpFilterFragment_Type = Integer32
_WfCctOptsIpFilterFragment_Object = MibTableColumn
wfCctOptsIpFilterFragment = _WfCctOptsIpFilterFragment_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 3, 1, 9),
    _WfCctOptsIpFilterFragment_Type()
)
wfCctOptsIpFilterFragment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCctOptsIpFilterFragment.setStatus("mandatory")
_WfCctOptsIpFilterName_Type = DisplayString
_WfCctOptsIpFilterName_Object = MibTableColumn
wfCctOptsIpFilterName = _WfCctOptsIpFilterName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 3, 1, 10),
    _WfCctOptsIpFilterName_Type()
)
wfCctOptsIpFilterName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCctOptsIpFilterName.setStatus("mandatory")
_WfCctOptsLengthBasedTable_Object = MibTable
wfCctOptsLengthBasedTable = _WfCctOptsLengthBasedTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 4)
)
if mibBuilder.loadTexts:
    wfCctOptsLengthBasedTable.setStatus("mandatory")
_WfCctOptsLengthBasedEntry_Object = MibTableRow
wfCctOptsLengthBasedEntry = _WfCctOptsLengthBasedEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 4, 1)
)
wfCctOptsLengthBasedEntry.setIndexNames(
    (0, "Wellfleet-CCTOPTS-MIB", "wfCctOptsLengthBasedCct"),
    (0, "Wellfleet-CCTOPTS-MIB", "wfCctOptsLengthBasedMux"),
    (0, "Wellfleet-CCTOPTS-MIB", "wfCctOptsLengthBasedData"),
)
if mibBuilder.loadTexts:
    wfCctOptsLengthBasedEntry.setStatus("mandatory")


class _WfCctOptsLengthBasedDelete_Type(Integer32):
    """Custom type wfCctOptsLengthBasedDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfCctOptsLengthBasedDelete_Type.__name__ = "Integer32"
_WfCctOptsLengthBasedDelete_Object = MibTableColumn
wfCctOptsLengthBasedDelete = _WfCctOptsLengthBasedDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 4, 1, 1),
    _WfCctOptsLengthBasedDelete_Type()
)
wfCctOptsLengthBasedDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCctOptsLengthBasedDelete.setStatus("mandatory")


class _WfCctOptsLengthBasedDisable_Type(Integer32):
    """Custom type wfCctOptsLengthBasedDisable based on Integer32"""
    defaultValue = 1

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


_WfCctOptsLengthBasedDisable_Type.__name__ = "Integer32"
_WfCctOptsLengthBasedDisable_Object = MibTableColumn
wfCctOptsLengthBasedDisable = _WfCctOptsLengthBasedDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 4, 1, 2),
    _WfCctOptsLengthBasedDisable_Type()
)
wfCctOptsLengthBasedDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCctOptsLengthBasedDisable.setStatus("mandatory")


class _WfCctOptsLengthBasedState_Type(Integer32):
    """Custom type wfCctOptsLengthBasedState based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("error", 2),
          ("inactive", 3))
    )


_WfCctOptsLengthBasedState_Type.__name__ = "Integer32"
_WfCctOptsLengthBasedState_Object = MibTableColumn
wfCctOptsLengthBasedState = _WfCctOptsLengthBasedState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 4, 1, 3),
    _WfCctOptsLengthBasedState_Type()
)
wfCctOptsLengthBasedState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCctOptsLengthBasedState.setStatus("mandatory")
_WfCctOptsLengthBasedCct_Type = Integer32
_WfCctOptsLengthBasedCct_Object = MibTableColumn
wfCctOptsLengthBasedCct = _WfCctOptsLengthBasedCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 4, 1, 4),
    _WfCctOptsLengthBasedCct_Type()
)
wfCctOptsLengthBasedCct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCctOptsLengthBasedCct.setStatus("mandatory")


class _WfCctOptsLengthBasedMux_Type(Integer32):
    """Custom type wfCctOptsLengthBasedMux based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("etype", 1),
          ("lsap", 2),
          ("snap", 3))
    )


_WfCctOptsLengthBasedMux_Type.__name__ = "Integer32"
_WfCctOptsLengthBasedMux_Object = MibTableColumn
wfCctOptsLengthBasedMux = _WfCctOptsLengthBasedMux_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 4, 1, 5),
    _WfCctOptsLengthBasedMux_Type()
)
wfCctOptsLengthBasedMux.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCctOptsLengthBasedMux.setStatus("mandatory")


class _WfCctOptsLengthBasedData_Type(OctetString):
    """Custom type wfCctOptsLengthBasedData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_WfCctOptsLengthBasedData_Type.__name__ = "OctetString"
_WfCctOptsLengthBasedData_Object = MibTableColumn
wfCctOptsLengthBasedData = _WfCctOptsLengthBasedData_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 4, 1, 6),
    _WfCctOptsLengthBasedData_Type()
)
wfCctOptsLengthBasedData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCctOptsLengthBasedData.setStatus("mandatory")
_WfCctOptsLengthBasedLength_Type = Integer32
_WfCctOptsLengthBasedLength_Object = MibTableColumn
wfCctOptsLengthBasedLength = _WfCctOptsLengthBasedLength_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 4, 1, 7),
    _WfCctOptsLengthBasedLength_Type()
)
wfCctOptsLengthBasedLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCctOptsLengthBasedLength.setStatus("mandatory")


class _WfCctOptsLengthBasedLessThanQ_Type(Integer32):
    """Custom type wfCctOptsLengthBasedLessThanQ based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hi", 3),
          ("lo", 1),
          ("normal", 2))
    )


_WfCctOptsLengthBasedLessThanQ_Type.__name__ = "Integer32"
_WfCctOptsLengthBasedLessThanQ_Object = MibTableColumn
wfCctOptsLengthBasedLessThanQ = _WfCctOptsLengthBasedLessThanQ_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 4, 1, 8),
    _WfCctOptsLengthBasedLessThanQ_Type()
)
wfCctOptsLengthBasedLessThanQ.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCctOptsLengthBasedLessThanQ.setStatus("mandatory")


class _WfCctOptsLengthBasedGreaterThanQ_Type(Integer32):
    """Custom type wfCctOptsLengthBasedGreaterThanQ based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hi", 3),
          ("lo", 1),
          ("normal", 2))
    )


_WfCctOptsLengthBasedGreaterThanQ_Type.__name__ = "Integer32"
_WfCctOptsLengthBasedGreaterThanQ_Object = MibTableColumn
wfCctOptsLengthBasedGreaterThanQ = _WfCctOptsLengthBasedGreaterThanQ_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 4, 1, 9),
    _WfCctOptsLengthBasedGreaterThanQ_Type()
)
wfCctOptsLengthBasedGreaterThanQ.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCctOptsLengthBasedGreaterThanQ.setStatus("mandatory")
_WfSwservOptsTable_Object = MibTable
wfSwservOptsTable = _WfSwservOptsTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 5)
)
if mibBuilder.loadTexts:
    wfSwservOptsTable.setStatus("mandatory")
_WfSwservOptsEntry_Object = MibTableRow
wfSwservOptsEntry = _WfSwservOptsEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 5, 1)
)
wfSwservOptsEntry.setIndexNames(
    (0, "Wellfleet-CCTOPTS-MIB", "wfSwservOptsCct"),
)
if mibBuilder.loadTexts:
    wfSwservOptsEntry.setStatus("mandatory")


class _WfSwservOptsDelete_Type(Integer32):
    """Custom type wfSwservOptsDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfSwservOptsDelete_Type.__name__ = "Integer32"
_WfSwservOptsDelete_Object = MibTableColumn
wfSwservOptsDelete = _WfSwservOptsDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 5, 1, 1),
    _WfSwservOptsDelete_Type()
)
wfSwservOptsDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSwservOptsDelete.setStatus("mandatory")
_WfSwservOptsCct_Type = Integer32
_WfSwservOptsCct_Object = MibTableColumn
wfSwservOptsCct = _WfSwservOptsCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 5, 1, 2),
    _WfSwservOptsCct_Type()
)
wfSwservOptsCct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSwservOptsCct.setStatus("mandatory")


class _WfSwservOptsCircuitType_Type(Integer32):
    """Custom type wfSwservOptsCircuitType based on Integer32"""
    defaultValue = 1

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
        *(("bandwidthondemand", 4),
          ("dialondemand", 3),
          ("normal", 1),
          ("primary", 2))
    )


_WfSwservOptsCircuitType_Type.__name__ = "Integer32"
_WfSwservOptsCircuitType_Object = MibTableColumn
wfSwservOptsCircuitType = _WfSwservOptsCircuitType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 5, 1, 3),
    _WfSwservOptsCircuitType_Type()
)
wfSwservOptsCircuitType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSwservOptsCircuitType.setStatus("mandatory")
_WfSwservOptsBackupCct_Type = Integer32
_WfSwservOptsBackupCct_Object = MibTableColumn
wfSwservOptsBackupCct = _WfSwservOptsBackupCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 5, 1, 4),
    _WfSwservOptsBackupCct_Type()
)
wfSwservOptsBackupCct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSwservOptsBackupCct.setStatus("mandatory")


class _WfSwservOptsBackupPool_Type(Integer32):
    """Custom type wfSwservOptsBackupPool based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_WfSwservOptsBackupPool_Type.__name__ = "Integer32"
_WfSwservOptsBackupPool_Object = MibTableColumn
wfSwservOptsBackupPool = _WfSwservOptsBackupPool_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 5, 1, 5),
    _WfSwservOptsBackupPool_Type()
)
wfSwservOptsBackupPool.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSwservOptsBackupPool.setStatus("mandatory")


class _WfSwservOptsDemandPool_Type(Integer32):
    """Custom type wfSwservOptsDemandPool based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_WfSwservOptsDemandPool_Type.__name__ = "Integer32"
_WfSwservOptsDemandPool_Object = MibTableColumn
wfSwservOptsDemandPool = _WfSwservOptsDemandPool_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 5, 1, 6),
    _WfSwservOptsDemandPool_Type()
)
wfSwservOptsDemandPool.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSwservOptsDemandPool.setStatus("mandatory")


class _WfSwservOptsBackupMode_Type(Integer32):
    """Custom type wfSwservOptsBackupMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("master", 1),
          ("slave", 2))
    )


_WfSwservOptsBackupMode_Type.__name__ = "Integer32"
_WfSwservOptsBackupMode_Object = MibTableColumn
wfSwservOptsBackupMode = _WfSwservOptsBackupMode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 5, 1, 7),
    _WfSwservOptsBackupMode_Type()
)
wfSwservOptsBackupMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSwservOptsBackupMode.setStatus("mandatory")
_WfSwservOptsActiveBackupCct_Type = Integer32
_WfSwservOptsActiveBackupCct_Object = MibTableColumn
wfSwservOptsActiveBackupCct = _WfSwservOptsActiveBackupCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 5, 1, 8),
    _WfSwservOptsActiveBackupCct_Type()
)
wfSwservOptsActiveBackupCct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSwservOptsActiveBackupCct.setStatus("mandatory")


class _WfSwservOptsForcedDial_Type(Integer32):
    """Custom type wfSwservOptsForcedDial based on Integer32"""
    defaultValue = 2

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


_WfSwservOptsForcedDial_Type.__name__ = "Integer32"
_WfSwservOptsForcedDial_Object = MibTableColumn
wfSwservOptsForcedDial = _WfSwservOptsForcedDial_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 5, 1, 9),
    _WfSwservOptsForcedDial_Type()
)
wfSwservOptsForcedDial.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSwservOptsForcedDial.setStatus("mandatory")


class _WfSwservOptsMaxUpTime_Type(Integer32):
    """Custom type wfSwservOptsMaxUpTime based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 999999),
    )


_WfSwservOptsMaxUpTime_Type.__name__ = "Integer32"
_WfSwservOptsMaxUpTime_Object = MibTableColumn
wfSwservOptsMaxUpTime = _WfSwservOptsMaxUpTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 5, 1, 10),
    _WfSwservOptsMaxUpTime_Type()
)
wfSwservOptsMaxUpTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSwservOptsMaxUpTime.setStatus("mandatory")
_WfSwservOptsBringUpHour_Type = Integer32
_WfSwservOptsBringUpHour_Object = MibTableColumn
wfSwservOptsBringUpHour = _WfSwservOptsBringUpHour_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 5, 1, 11),
    _WfSwservOptsBringUpHour_Type()
)
wfSwservOptsBringUpHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSwservOptsBringUpHour.setStatus("mandatory")
_WfSwservOptsBringUpMinute_Type = Integer32
_WfSwservOptsBringUpMinute_Object = MibTableColumn
wfSwservOptsBringUpMinute = _WfSwservOptsBringUpMinute_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 5, 1, 12),
    _WfSwservOptsBringUpMinute_Type()
)
wfSwservOptsBringUpMinute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSwservOptsBringUpMinute.setStatus("mandatory")
_WfSwservOptsTakeDownHour_Type = Integer32
_WfSwservOptsTakeDownHour_Object = MibTableColumn
wfSwservOptsTakeDownHour = _WfSwservOptsTakeDownHour_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 5, 1, 13),
    _WfSwservOptsTakeDownHour_Type()
)
wfSwservOptsTakeDownHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSwservOptsTakeDownHour.setStatus("mandatory")
_WfSwservOptsTakeDownMinute_Type = Integer32
_WfSwservOptsTakeDownMinute_Object = MibTableColumn
wfSwservOptsTakeDownMinute = _WfSwservOptsTakeDownMinute_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 5, 1, 14),
    _WfSwservOptsTakeDownMinute_Type()
)
wfSwservOptsTakeDownMinute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSwservOptsTakeDownMinute.setStatus("mandatory")


class _WfSwservOptsInactivityTime_Type(Integer32):
    """Custom type wfSwservOptsInactivityTime based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_WfSwservOptsInactivityTime_Type.__name__ = "Integer32"
_WfSwservOptsInactivityTime_Object = MibTableColumn
wfSwservOptsInactivityTime = _WfSwservOptsInactivityTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 5, 1, 15),
    _WfSwservOptsInactivityTime_Type()
)
wfSwservOptsInactivityTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSwservOptsInactivityTime.setStatus("mandatory")


class _WfSwservOptsCircuitState_Type(Integer32):
    """Custom type wfSwservOptsCircuitState based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2),
          ("notpresent", 3))
    )


_WfSwservOptsCircuitState_Type.__name__ = "Integer32"
_WfSwservOptsCircuitState_Object = MibTableColumn
wfSwservOptsCircuitState = _WfSwservOptsCircuitState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 5, 1, 16),
    _WfSwservOptsCircuitState_Type()
)
wfSwservOptsCircuitState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSwservOptsCircuitState.setStatus("mandatory")


class _WfSwservOptsPrimaryDownTime_Type(Integer32):
    """Custom type wfSwservOptsPrimaryDownTime based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            5
        )
    )
    namedValues = NamedValues(
        ("default", 5)
    )


_WfSwservOptsPrimaryDownTime_Type.__name__ = "Integer32"
_WfSwservOptsPrimaryDownTime_Object = MibTableColumn
wfSwservOptsPrimaryDownTime = _WfSwservOptsPrimaryDownTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 5, 1, 17),
    _WfSwservOptsPrimaryDownTime_Type()
)
wfSwservOptsPrimaryDownTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSwservOptsPrimaryDownTime.setStatus("mandatory")
_WfSwservOptsNumOutgoingConn_Type = Counter32
_WfSwservOptsNumOutgoingConn_Object = MibTableColumn
wfSwservOptsNumOutgoingConn = _WfSwservOptsNumOutgoingConn_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 5, 1, 18),
    _WfSwservOptsNumOutgoingConn_Type()
)
wfSwservOptsNumOutgoingConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSwservOptsNumOutgoingConn.setStatus("mandatory")
_WfSwservOptsNumIncomingConn_Type = Counter32
_WfSwservOptsNumIncomingConn_Object = MibTableColumn
wfSwservOptsNumIncomingConn = _WfSwservOptsNumIncomingConn_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 5, 1, 19),
    _WfSwservOptsNumIncomingConn_Type()
)
wfSwservOptsNumIncomingConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSwservOptsNumIncomingConn.setStatus("mandatory")
_WfSwservOptsActiveSlot_Type = Integer32
_WfSwservOptsActiveSlot_Object = MibTableColumn
wfSwservOptsActiveSlot = _WfSwservOptsActiveSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 5, 1, 20),
    _WfSwservOptsActiveSlot_Type()
)
wfSwservOptsActiveSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSwservOptsActiveSlot.setStatus("mandatory")
_WfSwservOptsActiveLine_Type = Integer32
_WfSwservOptsActiveLine_Object = MibTableColumn
wfSwservOptsActiveLine = _WfSwservOptsActiveLine_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 5, 1, 21),
    _WfSwservOptsActiveLine_Type()
)
wfSwservOptsActiveLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSwservOptsActiveLine.setStatus("mandatory")
_WfSwservOptsPacketsDropped_Type = Counter32
_WfSwservOptsPacketsDropped_Object = MibTableColumn
wfSwservOptsPacketsDropped = _WfSwservOptsPacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 5, 1, 22),
    _WfSwservOptsPacketsDropped_Type()
)
wfSwservOptsPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSwservOptsPacketsDropped.setStatus("mandatory")
_WfSwservOptsTimeLastPktDropped_Type = Integer32
_WfSwservOptsTimeLastPktDropped_Object = MibTableColumn
wfSwservOptsTimeLastPktDropped = _WfSwservOptsTimeLastPktDropped_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 5, 1, 23),
    _WfSwservOptsTimeLastPktDropped_Type()
)
wfSwservOptsTimeLastPktDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSwservOptsTimeLastPktDropped.setStatus("mandatory")


class _WfSwservOptsForcedTakedown_Type(Integer32):
    """Custom type wfSwservOptsForcedTakedown based on Integer32"""
    defaultValue = 2

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


_WfSwservOptsForcedTakedown_Type.__name__ = "Integer32"
_WfSwservOptsForcedTakedown_Object = MibTableColumn
wfSwservOptsForcedTakedown = _WfSwservOptsForcedTakedown_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 5, 1, 24),
    _WfSwservOptsForcedTakedown_Type()
)
wfSwservOptsForcedTakedown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSwservOptsForcedTakedown.setStatus("mandatory")


class _WfSwservOptsRetryMax_Type(Integer32):
    """Custom type wfSwservOptsRetryMax based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_WfSwservOptsRetryMax_Type.__name__ = "Integer32"
_WfSwservOptsRetryMax_Object = MibTableColumn
wfSwservOptsRetryMax = _WfSwservOptsRetryMax_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 5, 1, 25),
    _WfSwservOptsRetryMax_Type()
)
wfSwservOptsRetryMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSwservOptsRetryMax.setStatus("mandatory")
_WfSwservOptsRetryCount_Type = Counter32
_WfSwservOptsRetryCount_Object = MibTableColumn
wfSwservOptsRetryCount = _WfSwservOptsRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 5, 1, 26),
    _WfSwservOptsRetryCount_Type()
)
wfSwservOptsRetryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSwservOptsRetryCount.setStatus("mandatory")


class _WfSwservOptsRetryDelay_Type(Integer32):
    """Custom type wfSwservOptsRetryDelay based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_WfSwservOptsRetryDelay_Type.__name__ = "Integer32"
_WfSwservOptsRetryDelay_Object = MibTableColumn
wfSwservOptsRetryDelay = _WfSwservOptsRetryDelay_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 5, 1, 27),
    _WfSwservOptsRetryDelay_Type()
)
wfSwservOptsRetryDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSwservOptsRetryDelay.setStatus("mandatory")


class _WfSwservOptsDemandConnectionMode_Type(Integer32):
    """Custom type wfSwservOptsDemandConnectionMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("collmaster", 2),
          ("collslave", 3),
          ("nodial", 1))
    )


_WfSwservOptsDemandConnectionMode_Type.__name__ = "Integer32"
_WfSwservOptsDemandConnectionMode_Object = MibTableColumn
wfSwservOptsDemandConnectionMode = _WfSwservOptsDemandConnectionMode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 5, 1, 28),
    _WfSwservOptsDemandConnectionMode_Type()
)
wfSwservOptsDemandConnectionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSwservOptsDemandConnectionMode.setStatus("mandatory")


class _WfSwservOptsAutoDemandTermination_Type(Integer32):
    """Custom type wfSwservOptsAutoDemandTermination based on Integer32"""
    defaultValue = 2

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


_WfSwservOptsAutoDemandTermination_Type.__name__ = "Integer32"
_WfSwservOptsAutoDemandTermination_Object = MibTableColumn
wfSwservOptsAutoDemandTermination = _WfSwservOptsAutoDemandTermination_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 5, 1, 29),
    _WfSwservOptsAutoDemandTermination_Type()
)
wfSwservOptsAutoDemandTermination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSwservOptsAutoDemandTermination.setStatus("mandatory")


class _WfSwservOptsAutoDemandTermReset_Type(Integer32):
    """Custom type wfSwservOptsAutoDemandTermReset based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 999999),
    )


_WfSwservOptsAutoDemandTermReset_Type.__name__ = "Integer32"
_WfSwservOptsAutoDemandTermReset_Object = MibTableColumn
wfSwservOptsAutoDemandTermReset = _WfSwservOptsAutoDemandTermReset_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 5, 1, 30),
    _WfSwservOptsAutoDemandTermReset_Type()
)
wfSwservOptsAutoDemandTermReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSwservOptsAutoDemandTermReset.setStatus("mandatory")
_WfSwservOptsChapLocalName_Type = DisplayString
_WfSwservOptsChapLocalName_Object = MibTableColumn
wfSwservOptsChapLocalName = _WfSwservOptsChapLocalName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 5, 1, 31),
    _WfSwservOptsChapLocalName_Type()
)
wfSwservOptsChapLocalName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSwservOptsChapLocalName.setStatus("mandatory")
_WfSwservOptsChapSecret_Type = DisplayString
_WfSwservOptsChapSecret_Object = MibTableColumn
wfSwservOptsChapSecret = _WfSwservOptsChapSecret_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 5, 1, 32),
    _WfSwservOptsChapSecret_Type()
)
wfSwservOptsChapSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSwservOptsChapSecret.setStatus("mandatory")


class _WfSwservOptsMaxUpTermination_Type(Integer32):
    """Custom type wfSwservOptsMaxUpTermination based on Integer32"""
    defaultValue = 2

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


_WfSwservOptsMaxUpTermination_Type.__name__ = "Integer32"
_WfSwservOptsMaxUpTermination_Object = MibTableColumn
wfSwservOptsMaxUpTermination = _WfSwservOptsMaxUpTermination_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 5, 1, 33),
    _WfSwservOptsMaxUpTermination_Type()
)
wfSwservOptsMaxUpTermination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSwservOptsMaxUpTermination.setStatus("mandatory")


class _WfSwservOptsMaxUpTermReset_Type(Integer32):
    """Custom type wfSwservOptsMaxUpTermReset based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 999999),
    )


_WfSwservOptsMaxUpTermReset_Type.__name__ = "Integer32"
_WfSwservOptsMaxUpTermReset_Object = MibTableColumn
wfSwservOptsMaxUpTermReset = _WfSwservOptsMaxUpTermReset_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 5, 1, 34),
    _WfSwservOptsMaxUpTermReset_Type()
)
wfSwservOptsMaxUpTermReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSwservOptsMaxUpTermReset.setStatus("mandatory")


class _WfSwservOptsBandwidthPool_Type(Integer32):
    """Custom type wfSwservOptsBandwidthPool based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_WfSwservOptsBandwidthPool_Type.__name__ = "Integer32"
_WfSwservOptsBandwidthPool_Object = MibTableColumn
wfSwservOptsBandwidthPool = _WfSwservOptsBandwidthPool_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 5, 1, 35),
    _WfSwservOptsBandwidthPool_Type()
)
wfSwservOptsBandwidthPool.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSwservOptsBandwidthPool.setStatus("mandatory")


class _WfSwservOptsBandwidthMode_Type(Integer32):
    """Custom type wfSwservOptsBandwidthMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("monitor", 1),
          ("normal", 2))
    )


_WfSwservOptsBandwidthMode_Type.__name__ = "Integer32"
_WfSwservOptsBandwidthMode_Object = MibTableColumn
wfSwservOptsBandwidthMode = _WfSwservOptsBandwidthMode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 5, 1, 36),
    _WfSwservOptsBandwidthMode_Type()
)
wfSwservOptsBandwidthMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSwservOptsBandwidthMode.setStatus("mandatory")
_WfSwservOptsPapId_Type = DisplayString
_WfSwservOptsPapId_Object = MibTableColumn
wfSwservOptsPapId = _WfSwservOptsPapId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 5, 1, 37),
    _WfSwservOptsPapId_Type()
)
wfSwservOptsPapId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSwservOptsPapId.setStatus("mandatory")
_WfSwservOptsPapPassword_Type = DisplayString
_WfSwservOptsPapPassword_Object = MibTableColumn
wfSwservOptsPapPassword = _WfSwservOptsPapPassword_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 5, 1, 38),
    _WfSwservOptsPapPassword_Type()
)
wfSwservOptsPapPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSwservOptsPapPassword.setStatus("mandatory")


class _WfSwservOptsDebugMsgLevel_Type(Integer32):
    """Custom type wfSwservOptsDebugMsgLevel based on Integer32"""
    defaultValue = 4

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
        *(("debug", 4),
          ("one", 1),
          ("three", 3),
          ("two", 2))
    )


_WfSwservOptsDebugMsgLevel_Type.__name__ = "Integer32"
_WfSwservOptsDebugMsgLevel_Object = MibTableColumn
wfSwservOptsDebugMsgLevel = _WfSwservOptsDebugMsgLevel_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 5, 1, 39),
    _WfSwservOptsDebugMsgLevel_Type()
)
wfSwservOptsDebugMsgLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSwservOptsDebugMsgLevel.setStatus("mandatory")
_WfSwservOptsDmdCctGroupNum_Type = Integer32
_WfSwservOptsDmdCctGroupNum_Object = MibTableColumn
wfSwservOptsDmdCctGroupNum = _WfSwservOptsDmdCctGroupNum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 5, 1, 40),
    _WfSwservOptsDmdCctGroupNum_Type()
)
wfSwservOptsDmdCctGroupNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSwservOptsDmdCctGroupNum.setStatus("mandatory")


class _WfSwservOptsWanProtocol_Type(Integer32):
    """Custom type wfSwservOptsWanProtocol based on Integer32"""
    defaultValue = 2

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
        *(("fr", 3),
          ("frswitch", 4),
          ("ppp", 2),
          ("unknown", 1))
    )


_WfSwservOptsWanProtocol_Type.__name__ = "Integer32"
_WfSwservOptsWanProtocol_Object = MibTableColumn
wfSwservOptsWanProtocol = _WfSwservOptsWanProtocol_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 5, 1, 41),
    _WfSwservOptsWanProtocol_Type()
)
wfSwservOptsWanProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSwservOptsWanProtocol.setStatus("mandatory")
_WfSwservOptsSecondaryCct_Type = Integer32
_WfSwservOptsSecondaryCct_Object = MibTableColumn
wfSwservOptsSecondaryCct = _WfSwservOptsSecondaryCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 5, 1, 42),
    _WfSwservOptsSecondaryCct_Type()
)
wfSwservOptsSecondaryCct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSwservOptsSecondaryCct.setStatus("mandatory")
_WfSwservOptsPoolLineNumber_Type = Integer32
_WfSwservOptsPoolLineNumber_Object = MibTableColumn
wfSwservOptsPoolLineNumber = _WfSwservOptsPoolLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 5, 1, 43),
    _WfSwservOptsPoolLineNumber_Type()
)
wfSwservOptsPoolLineNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSwservOptsPoolLineNumber.setStatus("mandatory")
_WfSwservOptsPoolLineIndex_Type = Integer32
_WfSwservOptsPoolLineIndex_Object = MibTableColumn
wfSwservOptsPoolLineIndex = _WfSwservOptsPoolLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 5, 1, 44),
    _WfSwservOptsPoolLineIndex_Type()
)
wfSwservOptsPoolLineIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSwservOptsPoolLineIndex.setStatus("mandatory")


class _WfSwservOptsMinDuration_Type(Integer32):
    """Custom type wfSwservOptsMinDuration based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 2147483647),
    )


_WfSwservOptsMinDuration_Type.__name__ = "Integer32"
_WfSwservOptsMinDuration_Object = MibTableColumn
wfSwservOptsMinDuration = _WfSwservOptsMinDuration_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 5, 1, 45),
    _WfSwservOptsMinDuration_Type()
)
wfSwservOptsMinDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSwservOptsMinDuration.setStatus("mandatory")


class _WfSwservOptsInactivityMode_Type(Integer32):
    """Custom type wfSwservOptsInactivityMode based on Integer32"""
    defaultValue = 1

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
        *(("bothdirection", 1),
          ("eitherdirection", 4),
          ("receiveonly", 3),
          ("transmitonly", 2))
    )


_WfSwservOptsInactivityMode_Type.__name__ = "Integer32"
_WfSwservOptsInactivityMode_Object = MibTableColumn
wfSwservOptsInactivityMode = _WfSwservOptsInactivityMode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 5, 1, 46),
    _WfSwservOptsInactivityMode_Type()
)
wfSwservOptsInactivityMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSwservOptsInactivityMode.setStatus("mandatory")


class _WfSwservOptsOpportunityRouting_Type(Integer32):
    """Custom type wfSwservOptsOpportunityRouting based on Integer32"""
    defaultValue = 2

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


_WfSwservOptsOpportunityRouting_Type.__name__ = "Integer32"
_WfSwservOptsOpportunityRouting_Object = MibTableColumn
wfSwservOptsOpportunityRouting = _WfSwservOptsOpportunityRouting_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 5, 1, 47),
    _WfSwservOptsOpportunityRouting_Type()
)
wfSwservOptsOpportunityRouting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSwservOptsOpportunityRouting.setStatus("mandatory")


class _WfSwservOptsOutboundAuth_Type(Integer32):
    """Custom type wfSwservOptsOutboundAuth based on Integer32"""
    defaultValue = 1

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


_WfSwservOptsOutboundAuth_Type.__name__ = "Integer32"
_WfSwservOptsOutboundAuth_Object = MibTableColumn
wfSwservOptsOutboundAuth = _WfSwservOptsOutboundAuth_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 5, 1, 48),
    _WfSwservOptsOutboundAuth_Type()
)
wfSwservOptsOutboundAuth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSwservOptsOutboundAuth.setStatus("mandatory")


class _WfSwservOptsOverSubRetryTimer_Type(Integer32):
    """Custom type wfSwservOptsOverSubRetryTimer based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_WfSwservOptsOverSubRetryTimer_Type.__name__ = "Integer32"
_WfSwservOptsOverSubRetryTimer_Object = MibTableColumn
wfSwservOptsOverSubRetryTimer = _WfSwservOptsOverSubRetryTimer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 5, 1, 49),
    _WfSwservOptsOverSubRetryTimer_Type()
)
wfSwservOptsOverSubRetryTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSwservOptsOverSubRetryTimer.setStatus("mandatory")


class _WfSwservOptsStandbyMode_Type(Integer32):
    """Custom type wfSwservOptsStandbyMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("demandnormal", 1),
          ("standbyhot", 3),
          ("standbynormal", 2))
    )


_WfSwservOptsStandbyMode_Type.__name__ = "Integer32"
_WfSwservOptsStandbyMode_Object = MibTableColumn
wfSwservOptsStandbyMode = _WfSwservOptsStandbyMode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 5, 1, 50),
    _WfSwservOptsStandbyMode_Type()
)
wfSwservOptsStandbyMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSwservOptsStandbyMode.setStatus("mandatory")


class _WfSwservOptsStandbyFailBackMode_Type(Integer32):
    """Custom type wfSwservOptsStandbyFailBackMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 2),
          ("manual", 3),
          ("none", 1))
    )


_WfSwservOptsStandbyFailBackMode_Type.__name__ = "Integer32"
_WfSwservOptsStandbyFailBackMode_Object = MibTableColumn
wfSwservOptsStandbyFailBackMode = _WfSwservOptsStandbyFailBackMode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 5, 1, 51),
    _WfSwservOptsStandbyFailBackMode_Type()
)
wfSwservOptsStandbyFailBackMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSwservOptsStandbyFailBackMode.setStatus("mandatory")


class _WfSwservOptsManualStandbyAction_Type(Integer32):
    """Custom type wfSwservOptsManualStandbyAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("activate", 2),
          ("deactivate", 3),
          ("noaction", 1))
    )


_WfSwservOptsManualStandbyAction_Type.__name__ = "Integer32"
_WfSwservOptsManualStandbyAction_Object = MibTableColumn
wfSwservOptsManualStandbyAction = _WfSwservOptsManualStandbyAction_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 5, 1, 52),
    _WfSwservOptsManualStandbyAction_Type()
)
wfSwservOptsManualStandbyAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSwservOptsManualStandbyAction.setStatus("mandatory")


class _WfSwservOptsCallbackMode_Type(Integer32):
    """Custom type wfSwservOptsCallbackMode based on Integer32"""
    defaultValue = 1

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
              9)
        )
    )
    namedValues = NamedValues(
        *(("client", 3),
          ("client-one-charge", 5),
          ("client-rfc1570", 8),
          ("inactive", 1),
          ("server", 2),
          ("server-callid", 4),
          ("server-one-charge", 6),
          ("server-one-charge-callid", 7),
          ("server-rfc1570", 9))
    )


_WfSwservOptsCallbackMode_Type.__name__ = "Integer32"
_WfSwservOptsCallbackMode_Object = MibTableColumn
wfSwservOptsCallbackMode = _WfSwservOptsCallbackMode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 5, 1, 53),
    _WfSwservOptsCallbackMode_Type()
)
wfSwservOptsCallbackMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSwservOptsCallbackMode.setStatus("mandatory")


class _WfSwservOptsCallbackServerDelay_Type(Integer32):
    """Custom type wfSwservOptsCallbackServerDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1800),
    )


_WfSwservOptsCallbackServerDelay_Type.__name__ = "Integer32"
_WfSwservOptsCallbackServerDelay_Object = MibTableColumn
wfSwservOptsCallbackServerDelay = _WfSwservOptsCallbackServerDelay_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 5, 1, 54),
    _WfSwservOptsCallbackServerDelay_Type()
)
wfSwservOptsCallbackServerDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSwservOptsCallbackServerDelay.setStatus("mandatory")


class _WfSwservOptsCallbackClientDelay_Type(Integer32):
    """Custom type wfSwservOptsCallbackClientDelay based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1800),
    )


_WfSwservOptsCallbackClientDelay_Type.__name__ = "Integer32"
_WfSwservOptsCallbackClientDelay_Object = MibTableColumn
wfSwservOptsCallbackClientDelay = _WfSwservOptsCallbackClientDelay_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 5, 1, 55),
    _WfSwservOptsCallbackClientDelay_Type()
)
wfSwservOptsCallbackClientDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSwservOptsCallbackClientDelay.setStatus("mandatory")


class _WfSwservOptsQueueSize_Type(Integer32):
    """Custom type wfSwservOptsQueueSize based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_WfSwservOptsQueueSize_Type.__name__ = "Integer32"
_WfSwservOptsQueueSize_Object = MibTableColumn
wfSwservOptsQueueSize = _WfSwservOptsQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 5, 1, 56),
    _WfSwservOptsQueueSize_Type()
)
wfSwservOptsQueueSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSwservOptsQueueSize.setStatus("mandatory")


class _WfSwservOptsDequeueWaitTimer_Type(Integer32):
    """Custom type wfSwservOptsDequeueWaitTimer based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_WfSwservOptsDequeueWaitTimer_Type.__name__ = "Integer32"
_WfSwservOptsDequeueWaitTimer_Object = MibTableColumn
wfSwservOptsDequeueWaitTimer = _WfSwservOptsDequeueWaitTimer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 5, 1, 57),
    _WfSwservOptsDequeueWaitTimer_Type()
)
wfSwservOptsDequeueWaitTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSwservOptsDequeueWaitTimer.setStatus("mandatory")


class _WfSwservOptsMru_Type(Integer32):
    """Custom type wfSwservOptsMru based on Integer32"""
    defaultValue = 1500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4600),
    )


_WfSwservOptsMru_Type.__name__ = "Integer32"
_WfSwservOptsMru_Object = MibTableColumn
wfSwservOptsMru = _WfSwservOptsMru_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 5, 1, 58),
    _WfSwservOptsMru_Type()
)
wfSwservOptsMru.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSwservOptsMru.setStatus("mandatory")


class _WfSwservOptsRfc1661Compliance_Type(Integer32):
    """Custom type wfSwservOptsRfc1661Compliance based on Integer32"""
    defaultValue = 2

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


_WfSwservOptsRfc1661Compliance_Type.__name__ = "Integer32"
_WfSwservOptsRfc1661Compliance_Object = MibTableColumn
wfSwservOptsRfc1661Compliance = _WfSwservOptsRfc1661Compliance_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 5, 1, 59),
    _WfSwservOptsRfc1661Compliance_Type()
)
wfSwservOptsRfc1661Compliance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSwservOptsRfc1661Compliance.setStatus("mandatory")


class _WfSwservOptsBootupDelay_Type(Integer32):
    """Custom type wfSwservOptsBootupDelay based on Integer32"""
    defaultValue = 0


_WfSwservOptsBootupDelay_Object = MibTableColumn
wfSwservOptsBootupDelay = _WfSwservOptsBootupDelay_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 5, 1, 60),
    _WfSwservOptsBootupDelay_Type()
)
wfSwservOptsBootupDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSwservOptsBootupDelay.setStatus("mandatory")


class _WfSwservOptsCallbackOptRfc1570_Type(Integer32):
    """Custom type wfSwservOptsCallbackOptRfc1570 based on Integer32"""
    defaultValue = 2

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
        *(("dialstring", 2),
          ("e164number", 4),
          ("location", 1),
          ("locationid", 3),
          ("name", 5))
    )


_WfSwservOptsCallbackOptRfc1570_Type.__name__ = "Integer32"
_WfSwservOptsCallbackOptRfc1570_Object = MibTableColumn
wfSwservOptsCallbackOptRfc1570 = _WfSwservOptsCallbackOptRfc1570_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 5, 1, 61),
    _WfSwservOptsCallbackOptRfc1570_Type()
)
wfSwservOptsCallbackOptRfc1570.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSwservOptsCallbackOptRfc1570.setStatus("mandatory")
_WfSwservOptsCallbackDataRfc1570_Type = DisplayString
_WfSwservOptsCallbackDataRfc1570_Object = MibTableColumn
wfSwservOptsCallbackDataRfc1570 = _WfSwservOptsCallbackDataRfc1570_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 5, 1, 62),
    _WfSwservOptsCallbackDataRfc1570_Type()
)
wfSwservOptsCallbackDataRfc1570.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSwservOptsCallbackDataRfc1570.setStatus("mandatory")
_WfSwservOutPhoneNumTable_Object = MibTable
wfSwservOutPhoneNumTable = _WfSwservOutPhoneNumTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 6)
)
if mibBuilder.loadTexts:
    wfSwservOutPhoneNumTable.setStatus("mandatory")
_WfSwservOutPhoneNumEntry_Object = MibTableRow
wfSwservOutPhoneNumEntry = _WfSwservOutPhoneNumEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 6, 1)
)
wfSwservOutPhoneNumEntry.setIndexNames(
    (0, "Wellfleet-CCTOPTS-MIB", "wfSwservOutPhoneNumCct"),
    (0, "Wellfleet-CCTOPTS-MIB", "wfSwservOutPhoneNumIndex"),
)
if mibBuilder.loadTexts:
    wfSwservOutPhoneNumEntry.setStatus("mandatory")


class _WfSwservOutPhoneNumDelete_Type(Integer32):
    """Custom type wfSwservOutPhoneNumDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("delete", 2))
    )


_WfSwservOutPhoneNumDelete_Type.__name__ = "Integer32"
_WfSwservOutPhoneNumDelete_Object = MibTableColumn
wfSwservOutPhoneNumDelete = _WfSwservOutPhoneNumDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 6, 1, 1),
    _WfSwservOutPhoneNumDelete_Type()
)
wfSwservOutPhoneNumDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSwservOutPhoneNumDelete.setStatus("mandatory")


class _WfSwservOutPhoneNumCct_Type(Integer32):
    """Custom type wfSwservOutPhoneNumCct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_WfSwservOutPhoneNumCct_Type.__name__ = "Integer32"
_WfSwservOutPhoneNumCct_Object = MibTableColumn
wfSwservOutPhoneNumCct = _WfSwservOutPhoneNumCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 6, 1, 2),
    _WfSwservOutPhoneNumCct_Type()
)
wfSwservOutPhoneNumCct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSwservOutPhoneNumCct.setStatus("mandatory")


class _WfSwservOutPhoneNumIndex_Type(Integer32):
    """Custom type wfSwservOutPhoneNumIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_WfSwservOutPhoneNumIndex_Type.__name__ = "Integer32"
_WfSwservOutPhoneNumIndex_Object = MibTableColumn
wfSwservOutPhoneNumIndex = _WfSwservOutPhoneNumIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 6, 1, 3),
    _WfSwservOutPhoneNumIndex_Type()
)
wfSwservOutPhoneNumIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSwservOutPhoneNumIndex.setStatus("mandatory")
_WfSwservOutPhoneNumRmtStationNum_Type = DisplayString
_WfSwservOutPhoneNumRmtStationNum_Object = MibTableColumn
wfSwservOutPhoneNumRmtStationNum = _WfSwservOutPhoneNumRmtStationNum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 6, 1, 4),
    _WfSwservOutPhoneNumRmtStationNum_Type()
)
wfSwservOutPhoneNumRmtStationNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSwservOutPhoneNumRmtStationNum.setStatus("mandatory")
_WfSwservOutPhoneNumSubAddr_Type = DisplayString
_WfSwservOutPhoneNumSubAddr_Object = MibTableColumn
wfSwservOutPhoneNumSubAddr = _WfSwservOutPhoneNumSubAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 6, 1, 5),
    _WfSwservOutPhoneNumSubAddr_Type()
)
wfSwservOutPhoneNumSubAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSwservOutPhoneNumSubAddr.setStatus("mandatory")
_WfSwservOutPhoneNumDelimiter_Type = DisplayString
_WfSwservOutPhoneNumDelimiter_Object = MibTableColumn
wfSwservOutPhoneNumDelimiter = _WfSwservOutPhoneNumDelimiter_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 6, 1, 6),
    _WfSwservOutPhoneNumDelimiter_Type()
)
wfSwservOutPhoneNumDelimiter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSwservOutPhoneNumDelimiter.setStatus("mandatory")


class _WfSwservOutPhoneNumType_Type(Integer32):
    """Custom type wfSwservOutPhoneNumType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dial", 1),
          ("dialasync", 3),
          ("isdn", 2))
    )


_WfSwservOutPhoneNumType_Type.__name__ = "Integer32"
_WfSwservOutPhoneNumType_Object = MibTableColumn
wfSwservOutPhoneNumType = _WfSwservOutPhoneNumType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 6, 1, 7),
    _WfSwservOutPhoneNumType_Type()
)
wfSwservOutPhoneNumType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSwservOutPhoneNumType.setStatus("mandatory")


class _WfSwservOutPhoneNumTypeofNum_Type(Integer32):
    """Custom type wfSwservOutPhoneNumTypeofNum based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              16,
              32,
              48,
              64,
              96)
        )
    )
    namedValues = NamedValues(
        *(("abbreviated", 96),
          ("international", 16),
          ("national", 32),
          ("specific", 48),
          ("subscriber", 64),
          ("unknown", 1))
    )


_WfSwservOutPhoneNumTypeofNum_Type.__name__ = "Integer32"
_WfSwservOutPhoneNumTypeofNum_Object = MibTableColumn
wfSwservOutPhoneNumTypeofNum = _WfSwservOutPhoneNumTypeofNum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 6, 1, 8),
    _WfSwservOutPhoneNumTypeofNum_Type()
)
wfSwservOutPhoneNumTypeofNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSwservOutPhoneNumTypeofNum.setStatus("mandatory")


class _WfSwservOutPhoneNumPlan_Type(Integer32):
    """Custom type wfSwservOutPhoneNumPlan based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4,
              8,
              9,
              16)
        )
    )
    namedValues = NamedValues(
        *(("private", 9),
          ("standard", 8),
          ("telephony", 1),
          ("telex", 4),
          ("unknown", 16),
          ("x121", 3))
    )


_WfSwservOutPhoneNumPlan_Type.__name__ = "Integer32"
_WfSwservOutPhoneNumPlan_Object = MibTableColumn
wfSwservOutPhoneNumPlan = _WfSwservOutPhoneNumPlan_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 6, 1, 9),
    _WfSwservOutPhoneNumPlan_Type()
)
wfSwservOutPhoneNumPlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSwservOutPhoneNumPlan.setStatus("mandatory")


class _WfSwservOutPhoneNumRateAdaption_Type(Integer32):
    """Custom type wfSwservOutPhoneNumRateAdaption based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rate56", 2),
          ("rate64", 1))
    )


_WfSwservOutPhoneNumRateAdaption_Type.__name__ = "Integer32"
_WfSwservOutPhoneNumRateAdaption_Object = MibTableColumn
wfSwservOutPhoneNumRateAdaption = _WfSwservOutPhoneNumRateAdaption_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 6, 1, 10),
    _WfSwservOutPhoneNumRateAdaption_Type()
)
wfSwservOutPhoneNumRateAdaption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSwservOutPhoneNumRateAdaption.setStatus("mandatory")


class _WfSwservOutPhoneNumRemotePoolType_Type(Integer32):
    """Custom type wfSwservOutPhoneNumRemotePoolType based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bandwidthondemand", 2),
          ("dialandbandwidth", 3),
          ("dialondemand", 1))
    )


_WfSwservOutPhoneNumRemotePoolType_Type.__name__ = "Integer32"
_WfSwservOutPhoneNumRemotePoolType_Object = MibTableColumn
wfSwservOutPhoneNumRemotePoolType = _WfSwservOutPhoneNumRemotePoolType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 6, 1, 11),
    _WfSwservOutPhoneNumRemotePoolType_Type()
)
wfSwservOutPhoneNumRemotePoolType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSwservOutPhoneNumRemotePoolType.setStatus("mandatory")


class _WfSwservOutPhoneNumConnectionType_Type(Integer32):
    """Custom type wfSwservOutPhoneNumConnectionType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("multiple", 2),
          ("single", 1))
    )


_WfSwservOutPhoneNumConnectionType_Type.__name__ = "Integer32"
_WfSwservOutPhoneNumConnectionType_Object = MibTableColumn
wfSwservOutPhoneNumConnectionType = _WfSwservOutPhoneNumConnectionType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 6, 1, 12),
    _WfSwservOutPhoneNumConnectionType_Type()
)
wfSwservOutPhoneNumConnectionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSwservOutPhoneNumConnectionType.setStatus("mandatory")


class _WfSwservOutPhoneNumChannelType_Type(Integer32):
    """Custom type wfSwservOutPhoneNumChannelType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bchannel", 1),
          ("multirate", 2))
    )


_WfSwservOutPhoneNumChannelType_Type.__name__ = "Integer32"
_WfSwservOutPhoneNumChannelType_Object = MibTableColumn
wfSwservOutPhoneNumChannelType = _WfSwservOutPhoneNumChannelType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 6, 1, 13),
    _WfSwservOutPhoneNumChannelType_Type()
)
wfSwservOutPhoneNumChannelType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSwservOutPhoneNumChannelType.setStatus("mandatory")


class _WfSwservOutPhoneNumAggrChanCnt_Type(Integer32):
    """Custom type wfSwservOutPhoneNumAggrChanCnt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 23),
    )


_WfSwservOutPhoneNumAggrChanCnt_Type.__name__ = "Integer32"
_WfSwservOutPhoneNumAggrChanCnt_Object = MibTableColumn
wfSwservOutPhoneNumAggrChanCnt = _WfSwservOutPhoneNumAggrChanCnt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 6, 1, 14),
    _WfSwservOutPhoneNumAggrChanCnt_Type()
)
wfSwservOutPhoneNumAggrChanCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSwservOutPhoneNumAggrChanCnt.setStatus("mandatory")
_WfSwservOutPhoneNumPrefix_Type = DisplayString
_WfSwservOutPhoneNumPrefix_Object = MibTableColumn
wfSwservOutPhoneNumPrefix = _WfSwservOutPhoneNumPrefix_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 6, 1, 15),
    _WfSwservOutPhoneNumPrefix_Type()
)
wfSwservOutPhoneNumPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSwservOutPhoneNumPrefix.setStatus("mandatory")


class _WfSwservOutPhoneNumBearerService_Type(Integer32):
    """Custom type wfSwservOutPhoneNumBearerService based on Integer32"""
    defaultValue = 2

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


_WfSwservOutPhoneNumBearerService_Type.__name__ = "Integer32"
_WfSwservOutPhoneNumBearerService_Object = MibTableColumn
wfSwservOutPhoneNumBearerService = _WfSwservOutPhoneNumBearerService_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 6, 1, 16),
    _WfSwservOutPhoneNumBearerService_Type()
)
wfSwservOutPhoneNumBearerService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSwservOutPhoneNumBearerService.setStatus("mandatory")
_WfSwservInPhoneNumTable_Object = MibTable
wfSwservInPhoneNumTable = _WfSwservInPhoneNumTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 7)
)
if mibBuilder.loadTexts:
    wfSwservInPhoneNumTable.setStatus("mandatory")
_WfSwservInPhoneNumEntry_Object = MibTableRow
wfSwservInPhoneNumEntry = _WfSwservInPhoneNumEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 7, 1)
)
wfSwservInPhoneNumEntry.setIndexNames(
    (0, "Wellfleet-CCTOPTS-MIB", "wfSwservInPhoneNumIndex"),
)
if mibBuilder.loadTexts:
    wfSwservInPhoneNumEntry.setStatus("mandatory")


class _WfSwservInPhoneNumDelete_Type(Integer32):
    """Custom type wfSwservInPhoneNumDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("delete", 2))
    )


_WfSwservInPhoneNumDelete_Type.__name__ = "Integer32"
_WfSwservInPhoneNumDelete_Object = MibTableColumn
wfSwservInPhoneNumDelete = _WfSwservInPhoneNumDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 7, 1, 1),
    _WfSwservInPhoneNumDelete_Type()
)
wfSwservInPhoneNumDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSwservInPhoneNumDelete.setStatus("mandatory")


class _WfSwservInPhoneNumIndex_Type(Integer32):
    """Custom type wfSwservInPhoneNumIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_WfSwservInPhoneNumIndex_Type.__name__ = "Integer32"
_WfSwservInPhoneNumIndex_Object = MibTableColumn
wfSwservInPhoneNumIndex = _WfSwservInPhoneNumIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 7, 1, 2),
    _WfSwservInPhoneNumIndex_Type()
)
wfSwservInPhoneNumIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSwservInPhoneNumIndex.setStatus("mandatory")
_WfSwservInPhoneNumRmtStationNum_Type = DisplayString
_WfSwservInPhoneNumRmtStationNum_Object = MibTableColumn
wfSwservInPhoneNumRmtStationNum = _WfSwservInPhoneNumRmtStationNum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 7, 1, 3),
    _WfSwservInPhoneNumRmtStationNum_Type()
)
wfSwservInPhoneNumRmtStationNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSwservInPhoneNumRmtStationNum.setStatus("mandatory")
_WfSwservInPhoneNumSubAddr_Type = DisplayString
_WfSwservInPhoneNumSubAddr_Object = MibTableColumn
wfSwservInPhoneNumSubAddr = _WfSwservInPhoneNumSubAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 7, 1, 4),
    _WfSwservInPhoneNumSubAddr_Type()
)
wfSwservInPhoneNumSubAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSwservInPhoneNumSubAddr.setStatus("mandatory")
_WfSwservInPhoneNumDelimiter_Type = DisplayString
_WfSwservInPhoneNumDelimiter_Object = MibTableColumn
wfSwservInPhoneNumDelimiter = _WfSwservInPhoneNumDelimiter_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 7, 1, 5),
    _WfSwservInPhoneNumDelimiter_Type()
)
wfSwservInPhoneNumDelimiter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSwservInPhoneNumDelimiter.setStatus("mandatory")


class _WfSwservInPhoneNumType_Type(Integer32):
    """Custom type wfSwservInPhoneNumType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dial", 1),
          ("isdn", 2))
    )


_WfSwservInPhoneNumType_Type.__name__ = "Integer32"
_WfSwservInPhoneNumType_Object = MibTableColumn
wfSwservInPhoneNumType = _WfSwservInPhoneNumType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 7, 1, 6),
    _WfSwservInPhoneNumType_Type()
)
wfSwservInPhoneNumType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSwservInPhoneNumType.setStatus("mandatory")


class _WfSwservInPhoneNumTypeofNum_Type(Integer32):
    """Custom type wfSwservInPhoneNumTypeofNum based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              16,
              32,
              48,
              64,
              96)
        )
    )
    namedValues = NamedValues(
        *(("abbreviated", 96),
          ("international", 16),
          ("national", 32),
          ("specific", 48),
          ("subscriber", 64),
          ("unknown", 1))
    )


_WfSwservInPhoneNumTypeofNum_Type.__name__ = "Integer32"
_WfSwservInPhoneNumTypeofNum_Object = MibTableColumn
wfSwservInPhoneNumTypeofNum = _WfSwservInPhoneNumTypeofNum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 7, 1, 7),
    _WfSwservInPhoneNumTypeofNum_Type()
)
wfSwservInPhoneNumTypeofNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSwservInPhoneNumTypeofNum.setStatus("mandatory")


class _WfSwservInPhoneNumPlan_Type(Integer32):
    """Custom type wfSwservInPhoneNumPlan based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4,
              8,
              9,
              16)
        )
    )
    namedValues = NamedValues(
        *(("private", 9),
          ("standard", 8),
          ("telephony", 1),
          ("telex", 4),
          ("unknown", 16),
          ("x121", 3))
    )


_WfSwservInPhoneNumPlan_Type.__name__ = "Integer32"
_WfSwservInPhoneNumPlan_Object = MibTableColumn
wfSwservInPhoneNumPlan = _WfSwservInPhoneNumPlan_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 7, 1, 8),
    _WfSwservInPhoneNumPlan_Type()
)
wfSwservInPhoneNumPlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSwservInPhoneNumPlan.setStatus("mandatory")
_WfSwservInPhoneNumCct_Type = Integer32
_WfSwservInPhoneNumCct_Object = MibTableColumn
wfSwservInPhoneNumCct = _WfSwservInPhoneNumCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 7, 1, 9),
    _WfSwservInPhoneNumCct_Type()
)
wfSwservInPhoneNumCct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSwservInPhoneNumCct.setStatus("mandatory")
_WfCctOptsBrBuPppFilterTable_Object = MibTable
wfCctOptsBrBuPppFilterTable = _WfCctOptsBrBuPppFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 8)
)
if mibBuilder.loadTexts:
    wfCctOptsBrBuPppFilterTable.setStatus("mandatory")
_WfCctOptsBrBuPppFilterEntry_Object = MibTableRow
wfCctOptsBrBuPppFilterEntry = _WfCctOptsBrBuPppFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 8, 1)
)
wfCctOptsBrBuPppFilterEntry.setIndexNames(
    (0, "Wellfleet-CCTOPTS-MIB", "wfCctOptsBrBuPppFilterCct"),
    (0, "Wellfleet-CCTOPTS-MIB", "wfCctOptsBrBuPppFilterRuleNumber"),
    (0, "Wellfleet-CCTOPTS-MIB", "wfCctOptsBrBuPppFilterFragment"),
)
if mibBuilder.loadTexts:
    wfCctOptsBrBuPppFilterEntry.setStatus("mandatory")


class _WfCctOptsBrBuPppFilterCreate_Type(Integer32):
    """Custom type wfCctOptsBrBuPppFilterCreate based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfCctOptsBrBuPppFilterCreate_Type.__name__ = "Integer32"
_WfCctOptsBrBuPppFilterCreate_Object = MibTableColumn
wfCctOptsBrBuPppFilterCreate = _WfCctOptsBrBuPppFilterCreate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 8, 1, 1),
    _WfCctOptsBrBuPppFilterCreate_Type()
)
wfCctOptsBrBuPppFilterCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCctOptsBrBuPppFilterCreate.setStatus("mandatory")


class _WfCctOptsBrBuPppFilterEnable_Type(Integer32):
    """Custom type wfCctOptsBrBuPppFilterEnable based on Integer32"""
    defaultValue = 1

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


_WfCctOptsBrBuPppFilterEnable_Type.__name__ = "Integer32"
_WfCctOptsBrBuPppFilterEnable_Object = MibTableColumn
wfCctOptsBrBuPppFilterEnable = _WfCctOptsBrBuPppFilterEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 8, 1, 2),
    _WfCctOptsBrBuPppFilterEnable_Type()
)
wfCctOptsBrBuPppFilterEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCctOptsBrBuPppFilterEnable.setStatus("mandatory")


class _WfCctOptsBrBuPppFilterState_Type(Integer32):
    """Custom type wfCctOptsBrBuPppFilterState based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("error", 2),
          ("inactive", 3))
    )


_WfCctOptsBrBuPppFilterState_Type.__name__ = "Integer32"
_WfCctOptsBrBuPppFilterState_Object = MibTableColumn
wfCctOptsBrBuPppFilterState = _WfCctOptsBrBuPppFilterState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 8, 1, 3),
    _WfCctOptsBrBuPppFilterState_Type()
)
wfCctOptsBrBuPppFilterState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCctOptsBrBuPppFilterState.setStatus("mandatory")
_WfCctOptsBrBuPppFilterCounter_Type = Counter32
_WfCctOptsBrBuPppFilterCounter_Object = MibTableColumn
wfCctOptsBrBuPppFilterCounter = _WfCctOptsBrBuPppFilterCounter_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 8, 1, 4),
    _WfCctOptsBrBuPppFilterCounter_Type()
)
wfCctOptsBrBuPppFilterCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCctOptsBrBuPppFilterCounter.setStatus("mandatory")
_WfCctOptsBrBuPppFilterDefinition_Type = OctetString
_WfCctOptsBrBuPppFilterDefinition_Object = MibTableColumn
wfCctOptsBrBuPppFilterDefinition = _WfCctOptsBrBuPppFilterDefinition_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 8, 1, 5),
    _WfCctOptsBrBuPppFilterDefinition_Type()
)
wfCctOptsBrBuPppFilterDefinition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCctOptsBrBuPppFilterDefinition.setStatus("mandatory")
_WfCctOptsBrBuPppFilterReserved_Type = Integer32
_WfCctOptsBrBuPppFilterReserved_Object = MibTableColumn
wfCctOptsBrBuPppFilterReserved = _WfCctOptsBrBuPppFilterReserved_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 8, 1, 6),
    _WfCctOptsBrBuPppFilterReserved_Type()
)
wfCctOptsBrBuPppFilterReserved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCctOptsBrBuPppFilterReserved.setStatus("mandatory")
_WfCctOptsBrBuPppFilterCct_Type = Integer32
_WfCctOptsBrBuPppFilterCct_Object = MibTableColumn
wfCctOptsBrBuPppFilterCct = _WfCctOptsBrBuPppFilterCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 8, 1, 7),
    _WfCctOptsBrBuPppFilterCct_Type()
)
wfCctOptsBrBuPppFilterCct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCctOptsBrBuPppFilterCct.setStatus("mandatory")
_WfCctOptsBrBuPppFilterRuleNumber_Type = Integer32
_WfCctOptsBrBuPppFilterRuleNumber_Object = MibTableColumn
wfCctOptsBrBuPppFilterRuleNumber = _WfCctOptsBrBuPppFilterRuleNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 8, 1, 8),
    _WfCctOptsBrBuPppFilterRuleNumber_Type()
)
wfCctOptsBrBuPppFilterRuleNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCctOptsBrBuPppFilterRuleNumber.setStatus("mandatory")
_WfCctOptsBrBuPppFilterFragment_Type = Integer32
_WfCctOptsBrBuPppFilterFragment_Object = MibTableColumn
wfCctOptsBrBuPppFilterFragment = _WfCctOptsBrBuPppFilterFragment_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 8, 1, 9),
    _WfCctOptsBrBuPppFilterFragment_Type()
)
wfCctOptsBrBuPppFilterFragment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCctOptsBrBuPppFilterFragment.setStatus("mandatory")
_WfCctOptsBrBuPppFilterName_Type = DisplayString
_WfCctOptsBrBuPppFilterName_Object = MibTableColumn
wfCctOptsBrBuPppFilterName = _WfCctOptsBrBuPppFilterName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 8, 1, 10),
    _WfCctOptsBrBuPppFilterName_Type()
)
wfCctOptsBrBuPppFilterName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCctOptsBrBuPppFilterName.setStatus("mandatory")
_WfCctOptsIpBuPppFilterTable_Object = MibTable
wfCctOptsIpBuPppFilterTable = _WfCctOptsIpBuPppFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 9)
)
if mibBuilder.loadTexts:
    wfCctOptsIpBuPppFilterTable.setStatus("mandatory")
_WfCctOptsIpBuPppFilterEntry_Object = MibTableRow
wfCctOptsIpBuPppFilterEntry = _WfCctOptsIpBuPppFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 9, 1)
)
wfCctOptsIpBuPppFilterEntry.setIndexNames(
    (0, "Wellfleet-CCTOPTS-MIB", "wfCctOptsIpBuPppFilterCct"),
    (0, "Wellfleet-CCTOPTS-MIB", "wfCctOptsIpBuPppFilterRuleNumber"),
    (0, "Wellfleet-CCTOPTS-MIB", "wfCctOptsIpBuPppFilterFragment"),
)
if mibBuilder.loadTexts:
    wfCctOptsIpBuPppFilterEntry.setStatus("mandatory")


class _WfCctOptsIpBuPppFilterCreate_Type(Integer32):
    """Custom type wfCctOptsIpBuPppFilterCreate based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfCctOptsIpBuPppFilterCreate_Type.__name__ = "Integer32"
_WfCctOptsIpBuPppFilterCreate_Object = MibTableColumn
wfCctOptsIpBuPppFilterCreate = _WfCctOptsIpBuPppFilterCreate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 9, 1, 1),
    _WfCctOptsIpBuPppFilterCreate_Type()
)
wfCctOptsIpBuPppFilterCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCctOptsIpBuPppFilterCreate.setStatus("mandatory")


class _WfCctOptsIpBuPppFilterEnable_Type(Integer32):
    """Custom type wfCctOptsIpBuPppFilterEnable based on Integer32"""
    defaultValue = 1

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


_WfCctOptsIpBuPppFilterEnable_Type.__name__ = "Integer32"
_WfCctOptsIpBuPppFilterEnable_Object = MibTableColumn
wfCctOptsIpBuPppFilterEnable = _WfCctOptsIpBuPppFilterEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 9, 1, 2),
    _WfCctOptsIpBuPppFilterEnable_Type()
)
wfCctOptsIpBuPppFilterEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCctOptsIpBuPppFilterEnable.setStatus("mandatory")


class _WfCctOptsIpBuPppFilterState_Type(Integer32):
    """Custom type wfCctOptsIpBuPppFilterState based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("error", 2),
          ("inactive", 3))
    )


_WfCctOptsIpBuPppFilterState_Type.__name__ = "Integer32"
_WfCctOptsIpBuPppFilterState_Object = MibTableColumn
wfCctOptsIpBuPppFilterState = _WfCctOptsIpBuPppFilterState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 9, 1, 3),
    _WfCctOptsIpBuPppFilterState_Type()
)
wfCctOptsIpBuPppFilterState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCctOptsIpBuPppFilterState.setStatus("mandatory")
_WfCctOptsIpBuPppFilterCounter_Type = Counter32
_WfCctOptsIpBuPppFilterCounter_Object = MibTableColumn
wfCctOptsIpBuPppFilterCounter = _WfCctOptsIpBuPppFilterCounter_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 9, 1, 4),
    _WfCctOptsIpBuPppFilterCounter_Type()
)
wfCctOptsIpBuPppFilterCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCctOptsIpBuPppFilterCounter.setStatus("mandatory")
_WfCctOptsIpBuPppFilterDefinition_Type = OctetString
_WfCctOptsIpBuPppFilterDefinition_Object = MibTableColumn
wfCctOptsIpBuPppFilterDefinition = _WfCctOptsIpBuPppFilterDefinition_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 9, 1, 5),
    _WfCctOptsIpBuPppFilterDefinition_Type()
)
wfCctOptsIpBuPppFilterDefinition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCctOptsIpBuPppFilterDefinition.setStatus("mandatory")
_WfCctOptsIpBuPppFilterReserved_Type = Integer32
_WfCctOptsIpBuPppFilterReserved_Object = MibTableColumn
wfCctOptsIpBuPppFilterReserved = _WfCctOptsIpBuPppFilterReserved_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 9, 1, 6),
    _WfCctOptsIpBuPppFilterReserved_Type()
)
wfCctOptsIpBuPppFilterReserved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCctOptsIpBuPppFilterReserved.setStatus("mandatory")
_WfCctOptsIpBuPppFilterCct_Type = Integer32
_WfCctOptsIpBuPppFilterCct_Object = MibTableColumn
wfCctOptsIpBuPppFilterCct = _WfCctOptsIpBuPppFilterCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 9, 1, 7),
    _WfCctOptsIpBuPppFilterCct_Type()
)
wfCctOptsIpBuPppFilterCct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCctOptsIpBuPppFilterCct.setStatus("mandatory")
_WfCctOptsIpBuPppFilterRuleNumber_Type = Integer32
_WfCctOptsIpBuPppFilterRuleNumber_Object = MibTableColumn
wfCctOptsIpBuPppFilterRuleNumber = _WfCctOptsIpBuPppFilterRuleNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 9, 1, 8),
    _WfCctOptsIpBuPppFilterRuleNumber_Type()
)
wfCctOptsIpBuPppFilterRuleNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCctOptsIpBuPppFilterRuleNumber.setStatus("mandatory")
_WfCctOptsIpBuPppFilterFragment_Type = Integer32
_WfCctOptsIpBuPppFilterFragment_Object = MibTableColumn
wfCctOptsIpBuPppFilterFragment = _WfCctOptsIpBuPppFilterFragment_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 9, 1, 9),
    _WfCctOptsIpBuPppFilterFragment_Type()
)
wfCctOptsIpBuPppFilterFragment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCctOptsIpBuPppFilterFragment.setStatus("mandatory")
_WfCctOptsIpBuPppFilterName_Type = DisplayString
_WfCctOptsIpBuPppFilterName_Object = MibTableColumn
wfCctOptsIpBuPppFilterName = _WfCctOptsIpBuPppFilterName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 9, 1, 10),
    _WfCctOptsIpBuPppFilterName_Type()
)
wfCctOptsIpBuPppFilterName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCctOptsIpBuPppFilterName.setStatus("mandatory")
_WfCctOptsCngcTable_Object = MibTable
wfCctOptsCngcTable = _WfCctOptsCngcTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 10)
)
if mibBuilder.loadTexts:
    wfCctOptsCngcTable.setStatus("mandatory")
_WfCctOptsCngcEntry_Object = MibTableRow
wfCctOptsCngcEntry = _WfCctOptsCngcEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 10, 1)
)
wfCctOptsCngcEntry.setIndexNames(
    (0, "Wellfleet-CCTOPTS-MIB", "wfCctOptsCngcCct"),
)
if mibBuilder.loadTexts:
    wfCctOptsCngcEntry.setStatus("mandatory")


class _WfCctOptsCngcDelete_Type(Integer32):
    """Custom type wfCctOptsCngcDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfCctOptsCngcDelete_Type.__name__ = "Integer32"
_WfCctOptsCngcDelete_Object = MibTableColumn
wfCctOptsCngcDelete = _WfCctOptsCngcDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 10, 1, 1),
    _WfCctOptsCngcDelete_Type()
)
wfCctOptsCngcDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCctOptsCngcDelete.setStatus("mandatory")


class _WfCctOptsCngcDisable_Type(Integer32):
    """Custom type wfCctOptsCngcDisable based on Integer32"""
    defaultValue = 1

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


_WfCctOptsCngcDisable_Type.__name__ = "Integer32"
_WfCctOptsCngcDisable_Object = MibTableColumn
wfCctOptsCngcDisable = _WfCctOptsCngcDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 10, 1, 2),
    _WfCctOptsCngcDisable_Type()
)
wfCctOptsCngcDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCctOptsCngcDisable.setStatus("mandatory")
_WfCctOptsCngcCct_Type = Integer32
_WfCctOptsCngcCct_Object = MibTableColumn
wfCctOptsCngcCct = _WfCctOptsCngcCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 10, 1, 3),
    _WfCctOptsCngcCct_Type()
)
wfCctOptsCngcCct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCctOptsCngcCct.setStatus("mandatory")


class _WfCctOptsCngcSmdsDiscardability_Type(Integer32):
    """Custom type wfCctOptsCngcSmdsDiscardability based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("datagram", 1),
          ("frde", 2),
          ("frnde", 3))
    )


_WfCctOptsCngcSmdsDiscardability_Type.__name__ = "Integer32"
_WfCctOptsCngcSmdsDiscardability_Object = MibTableColumn
wfCctOptsCngcSmdsDiscardability = _WfCctOptsCngcSmdsDiscardability_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 10, 1, 4),
    _WfCctOptsCngcSmdsDiscardability_Type()
)
wfCctOptsCngcSmdsDiscardability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCctOptsCngcSmdsDiscardability.setStatus("mandatory")


class _WfCctOptsCngcCfgSwtxqThreshold_Type(Integer32):
    """Custom type wfCctOptsCngcCfgSwtxqThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_WfCctOptsCngcCfgSwtxqThreshold_Type.__name__ = "Integer32"
_WfCctOptsCngcCfgSwtxqThreshold_Object = MibTableColumn
wfCctOptsCngcCfgSwtxqThreshold = _WfCctOptsCngcCfgSwtxqThreshold_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 10, 1, 5),
    _WfCctOptsCngcCfgSwtxqThreshold_Type()
)
wfCctOptsCngcCfgSwtxqThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCctOptsCngcCfgSwtxqThreshold.setStatus("mandatory")
_WfCctOptsCngcSwtxqThreshold_Type = Integer32
_WfCctOptsCngcSwtxqThreshold_Object = MibTableColumn
wfCctOptsCngcSwtxqThreshold = _WfCctOptsCngcSwtxqThreshold_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 10, 1, 6),
    _WfCctOptsCngcSwtxqThreshold_Type()
)
wfCctOptsCngcSwtxqThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCctOptsCngcSwtxqThreshold.setStatus("mandatory")


class _WfCctOptsCngcCngLevel0Threshold_Type(Integer32):
    """Custom type wfCctOptsCngcCngLevel0Threshold based on Integer32"""
    defaultValue = 25

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_WfCctOptsCngcCngLevel0Threshold_Type.__name__ = "Integer32"
_WfCctOptsCngcCngLevel0Threshold_Object = MibTableColumn
wfCctOptsCngcCngLevel0Threshold = _WfCctOptsCngcCngLevel0Threshold_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 10, 1, 7),
    _WfCctOptsCngcCngLevel0Threshold_Type()
)
wfCctOptsCngcCngLevel0Threshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCctOptsCngcCngLevel0Threshold.setStatus("mandatory")


class _WfCctOptsCngcCngLevel1Threshold_Type(Integer32):
    """Custom type wfCctOptsCngcCngLevel1Threshold based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_WfCctOptsCngcCngLevel1Threshold_Type.__name__ = "Integer32"
_WfCctOptsCngcCngLevel1Threshold_Object = MibTableColumn
wfCctOptsCngcCngLevel1Threshold = _WfCctOptsCngcCngLevel1Threshold_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 10, 1, 8),
    _WfCctOptsCngcCngLevel1Threshold_Type()
)
wfCctOptsCngcCngLevel1Threshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCctOptsCngcCngLevel1Threshold.setStatus("mandatory")


class _WfCctOptsCngcCngLevel2Threshold_Type(Integer32):
    """Custom type wfCctOptsCngcCngLevel2Threshold based on Integer32"""
    defaultValue = 75

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_WfCctOptsCngcCngLevel2Threshold_Type.__name__ = "Integer32"
_WfCctOptsCngcCngLevel2Threshold_Object = MibTableColumn
wfCctOptsCngcCngLevel2Threshold = _WfCctOptsCngcCngLevel2Threshold_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 10, 1, 9),
    _WfCctOptsCngcCngLevel2Threshold_Type()
)
wfCctOptsCngcCngLevel2Threshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCctOptsCngcCngLevel2Threshold.setStatus("mandatory")


class _WfCctOptsCngcLinkType_Type(Integer32):
    """Custom type wfCctOptsCngcLinkType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("access", 1),
          ("nodal", 2))
    )


_WfCctOptsCngcLinkType_Type.__name__ = "Integer32"
_WfCctOptsCngcLinkType_Object = MibTableColumn
wfCctOptsCngcLinkType = _WfCctOptsCngcLinkType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 10, 1, 10),
    _WfCctOptsCngcLinkType_Type()
)
wfCctOptsCngcLinkType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCctOptsCngcLinkType.setStatus("mandatory")


class _WfCctOptsCngcTrfPriorityEnable_Type(Integer32):
    """Custom type wfCctOptsCngcTrfPriorityEnable based on Integer32"""
    defaultValue = 2

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


_WfCctOptsCngcTrfPriorityEnable_Type.__name__ = "Integer32"
_WfCctOptsCngcTrfPriorityEnable_Object = MibTableColumn
wfCctOptsCngcTrfPriorityEnable = _WfCctOptsCngcTrfPriorityEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 10, 1, 11),
    _WfCctOptsCngcTrfPriorityEnable_Type()
)
wfCctOptsCngcTrfPriorityEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCctOptsCngcTrfPriorityEnable.setStatus("mandatory")


class _WfCctOptsCngcPortIPTrfPriority_Type(Integer32):
    """Custom type wfCctOptsCngcPortIPTrfPriority based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("one", 1),
          ("three", 3),
          ("two", 2))
    )


_WfCctOptsCngcPortIPTrfPriority_Type.__name__ = "Integer32"
_WfCctOptsCngcPortIPTrfPriority_Object = MibTableColumn
wfCctOptsCngcPortIPTrfPriority = _WfCctOptsCngcPortIPTrfPriority_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 10, 1, 12),
    _WfCctOptsCngcPortIPTrfPriority_Type()
)
wfCctOptsCngcPortIPTrfPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCctOptsCngcPortIPTrfPriority.setStatus("mandatory")


class _WfCctOptsCngcPortTrfDiscardLvl_Type(Integer32):
    """Custom type wfCctOptsCngcPortTrfDiscardLvl based on Integer32"""
    defaultValue = 2

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
        *(("four", 4),
          ("one", 1),
          ("three", 3),
          ("two", 2))
    )


_WfCctOptsCngcPortTrfDiscardLvl_Type.__name__ = "Integer32"
_WfCctOptsCngcPortTrfDiscardLvl_Object = MibTableColumn
wfCctOptsCngcPortTrfDiscardLvl = _WfCctOptsCngcPortTrfDiscardLvl_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 10, 1, 13),
    _WfCctOptsCngcPortTrfDiscardLvl_Type()
)
wfCctOptsCngcPortTrfDiscardLvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCctOptsCngcPortTrfDiscardLvl.setStatus("mandatory")


class _WfCctOptsCngcPortTrfPriority_Type(Integer32):
    """Custom type wfCctOptsCngcPortTrfPriority based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("one", 1),
          ("three", 3),
          ("two", 2))
    )


_WfCctOptsCngcPortTrfPriority_Type.__name__ = "Integer32"
_WfCctOptsCngcPortTrfPriority_Object = MibTableColumn
wfCctOptsCngcPortTrfPriority = _WfCctOptsCngcPortTrfPriority_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 10, 1, 14),
    _WfCctOptsCngcPortTrfPriority_Type()
)
wfCctOptsCngcPortTrfPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCctOptsCngcPortTrfPriority.setStatus("mandatory")


class _WfCctOptsCngcCfgHwtxQThreshold_Type(Integer32):
    """Custom type wfCctOptsCngcCfgHwtxQThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_WfCctOptsCngcCfgHwtxQThreshold_Type.__name__ = "Integer32"
_WfCctOptsCngcCfgHwtxQThreshold_Object = MibTableColumn
wfCctOptsCngcCfgHwtxQThreshold = _WfCctOptsCngcCfgHwtxQThreshold_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 10, 1, 15),
    _WfCctOptsCngcCfgHwtxQThreshold_Type()
)
wfCctOptsCngcCfgHwtxQThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCctOptsCngcCfgHwtxQThreshold.setStatus("mandatory")
_WfCctOptsCngcHwtxQThreshold_Type = Integer32
_WfCctOptsCngcHwtxQThreshold_Object = MibTableColumn
wfCctOptsCngcHwtxQThreshold = _WfCctOptsCngcHwtxQThreshold_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 10, 1, 16),
    _WfCctOptsCngcHwtxQThreshold_Type()
)
wfCctOptsCngcHwtxQThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCctOptsCngcHwtxQThreshold.setStatus("mandatory")


class _WfCctOptsCngcSndTrapForPktsDropped_Type(Integer32):
    """Custom type wfCctOptsCngcSndTrapForPktsDropped based on Integer32"""
    defaultValue = 100000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000000),
    )


_WfCctOptsCngcSndTrapForPktsDropped_Type.__name__ = "Integer32"
_WfCctOptsCngcSndTrapForPktsDropped_Object = MibTableColumn
wfCctOptsCngcSndTrapForPktsDropped = _WfCctOptsCngcSndTrapForPktsDropped_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 10, 1, 17),
    _WfCctOptsCngcSndTrapForPktsDropped_Type()
)
wfCctOptsCngcSndTrapForPktsDropped.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCctOptsCngcSndTrapForPktsDropped.setStatus("mandatory")


class _WfCctOptsCngcCfgQp0Threshold_Type(Integer32):
    """Custom type wfCctOptsCngcCfgQp0Threshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2048),
    )


_WfCctOptsCngcCfgQp0Threshold_Type.__name__ = "Integer32"
_WfCctOptsCngcCfgQp0Threshold_Object = MibTableColumn
wfCctOptsCngcCfgQp0Threshold = _WfCctOptsCngcCfgQp0Threshold_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 10, 1, 18),
    _WfCctOptsCngcCfgQp0Threshold_Type()
)
wfCctOptsCngcCfgQp0Threshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCctOptsCngcCfgQp0Threshold.setStatus("mandatory")
_WfCctOptsCngcQp0Threshold_Type = Integer32
_WfCctOptsCngcQp0Threshold_Object = MibTableColumn
wfCctOptsCngcQp0Threshold = _WfCctOptsCngcQp0Threshold_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 10, 1, 19),
    _WfCctOptsCngcQp0Threshold_Type()
)
wfCctOptsCngcQp0Threshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCctOptsCngcQp0Threshold.setStatus("mandatory")


class _WfCctOptsCngcQp0CngLvl0Threshold_Type(Integer32):
    """Custom type wfCctOptsCngcQp0CngLvl0Threshold based on Integer32"""
    defaultValue = 25

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_WfCctOptsCngcQp0CngLvl0Threshold_Type.__name__ = "Integer32"
_WfCctOptsCngcQp0CngLvl0Threshold_Object = MibTableColumn
wfCctOptsCngcQp0CngLvl0Threshold = _WfCctOptsCngcQp0CngLvl0Threshold_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 10, 1, 20),
    _WfCctOptsCngcQp0CngLvl0Threshold_Type()
)
wfCctOptsCngcQp0CngLvl0Threshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCctOptsCngcQp0CngLvl0Threshold.setStatus("mandatory")


class _WfCctOptsCngcQp0CngLvl1Threshold_Type(Integer32):
    """Custom type wfCctOptsCngcQp0CngLvl1Threshold based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_WfCctOptsCngcQp0CngLvl1Threshold_Type.__name__ = "Integer32"
_WfCctOptsCngcQp0CngLvl1Threshold_Object = MibTableColumn
wfCctOptsCngcQp0CngLvl1Threshold = _WfCctOptsCngcQp0CngLvl1Threshold_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 10, 1, 21),
    _WfCctOptsCngcQp0CngLvl1Threshold_Type()
)
wfCctOptsCngcQp0CngLvl1Threshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCctOptsCngcQp0CngLvl1Threshold.setStatus("mandatory")


class _WfCctOptsCngcQp0CngLvl2Threshold_Type(Integer32):
    """Custom type wfCctOptsCngcQp0CngLvl2Threshold based on Integer32"""
    defaultValue = 75

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_WfCctOptsCngcQp0CngLvl2Threshold_Type.__name__ = "Integer32"
_WfCctOptsCngcQp0CngLvl2Threshold_Object = MibTableColumn
wfCctOptsCngcQp0CngLvl2Threshold = _WfCctOptsCngcQp0CngLvl2Threshold_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 10, 1, 22),
    _WfCctOptsCngcQp0CngLvl2Threshold_Type()
)
wfCctOptsCngcQp0CngLvl2Threshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCctOptsCngcQp0CngLvl2Threshold.setStatus("mandatory")


class _WfCctOptsCngcQp0PktsServPriNxtQ_Type(Integer32):
    """Custom type wfCctOptsCngcQp0PktsServPriNxtQ based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_WfCctOptsCngcQp0PktsServPriNxtQ_Type.__name__ = "Integer32"
_WfCctOptsCngcQp0PktsServPriNxtQ_Object = MibTableColumn
wfCctOptsCngcQp0PktsServPriNxtQ = _WfCctOptsCngcQp0PktsServPriNxtQ_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 10, 1, 23),
    _WfCctOptsCngcQp0PktsServPriNxtQ_Type()
)
wfCctOptsCngcQp0PktsServPriNxtQ.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCctOptsCngcQp0PktsServPriNxtQ.setStatus("mandatory")


class _WfCctOptsCngcCfgQp1Threshold_Type(Integer32):
    """Custom type wfCctOptsCngcCfgQp1Threshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2048),
    )


_WfCctOptsCngcCfgQp1Threshold_Type.__name__ = "Integer32"
_WfCctOptsCngcCfgQp1Threshold_Object = MibTableColumn
wfCctOptsCngcCfgQp1Threshold = _WfCctOptsCngcCfgQp1Threshold_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 10, 1, 24),
    _WfCctOptsCngcCfgQp1Threshold_Type()
)
wfCctOptsCngcCfgQp1Threshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCctOptsCngcCfgQp1Threshold.setStatus("mandatory")
_WfCctOptsCngcQp1Threshold_Type = Integer32
_WfCctOptsCngcQp1Threshold_Object = MibTableColumn
wfCctOptsCngcQp1Threshold = _WfCctOptsCngcQp1Threshold_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 10, 1, 25),
    _WfCctOptsCngcQp1Threshold_Type()
)
wfCctOptsCngcQp1Threshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCctOptsCngcQp1Threshold.setStatus("mandatory")


class _WfCctOptsCngcQp1CngLvl0Threshold_Type(Integer32):
    """Custom type wfCctOptsCngcQp1CngLvl0Threshold based on Integer32"""
    defaultValue = 25

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_WfCctOptsCngcQp1CngLvl0Threshold_Type.__name__ = "Integer32"
_WfCctOptsCngcQp1CngLvl0Threshold_Object = MibTableColumn
wfCctOptsCngcQp1CngLvl0Threshold = _WfCctOptsCngcQp1CngLvl0Threshold_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 10, 1, 26),
    _WfCctOptsCngcQp1CngLvl0Threshold_Type()
)
wfCctOptsCngcQp1CngLvl0Threshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCctOptsCngcQp1CngLvl0Threshold.setStatus("mandatory")


class _WfCctOptsCngcQp1CngLvl1Threshold_Type(Integer32):
    """Custom type wfCctOptsCngcQp1CngLvl1Threshold based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_WfCctOptsCngcQp1CngLvl1Threshold_Type.__name__ = "Integer32"
_WfCctOptsCngcQp1CngLvl1Threshold_Object = MibTableColumn
wfCctOptsCngcQp1CngLvl1Threshold = _WfCctOptsCngcQp1CngLvl1Threshold_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 10, 1, 27),
    _WfCctOptsCngcQp1CngLvl1Threshold_Type()
)
wfCctOptsCngcQp1CngLvl1Threshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCctOptsCngcQp1CngLvl1Threshold.setStatus("mandatory")


class _WfCctOptsCngcQp1CngLvl2Threshold_Type(Integer32):
    """Custom type wfCctOptsCngcQp1CngLvl2Threshold based on Integer32"""
    defaultValue = 75

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_WfCctOptsCngcQp1CngLvl2Threshold_Type.__name__ = "Integer32"
_WfCctOptsCngcQp1CngLvl2Threshold_Object = MibTableColumn
wfCctOptsCngcQp1CngLvl2Threshold = _WfCctOptsCngcQp1CngLvl2Threshold_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 10, 1, 28),
    _WfCctOptsCngcQp1CngLvl2Threshold_Type()
)
wfCctOptsCngcQp1CngLvl2Threshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCctOptsCngcQp1CngLvl2Threshold.setStatus("mandatory")


class _WfCctOptsCngcQp1PktsServPriNxtQ_Type(Integer32):
    """Custom type wfCctOptsCngcQp1PktsServPriNxtQ based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_WfCctOptsCngcQp1PktsServPriNxtQ_Type.__name__ = "Integer32"
_WfCctOptsCngcQp1PktsServPriNxtQ_Object = MibTableColumn
wfCctOptsCngcQp1PktsServPriNxtQ = _WfCctOptsCngcQp1PktsServPriNxtQ_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 10, 1, 29),
    _WfCctOptsCngcQp1PktsServPriNxtQ_Type()
)
wfCctOptsCngcQp1PktsServPriNxtQ.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCctOptsCngcQp1PktsServPriNxtQ.setStatus("mandatory")


class _WfCctOptsCngcCfgQp2Threshold_Type(Integer32):
    """Custom type wfCctOptsCngcCfgQp2Threshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2048),
    )


_WfCctOptsCngcCfgQp2Threshold_Type.__name__ = "Integer32"
_WfCctOptsCngcCfgQp2Threshold_Object = MibTableColumn
wfCctOptsCngcCfgQp2Threshold = _WfCctOptsCngcCfgQp2Threshold_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 10, 1, 30),
    _WfCctOptsCngcCfgQp2Threshold_Type()
)
wfCctOptsCngcCfgQp2Threshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCctOptsCngcCfgQp2Threshold.setStatus("mandatory")
_WfCctOptsCngcQp2Threshold_Type = Integer32
_WfCctOptsCngcQp2Threshold_Object = MibTableColumn
wfCctOptsCngcQp2Threshold = _WfCctOptsCngcQp2Threshold_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 10, 1, 31),
    _WfCctOptsCngcQp2Threshold_Type()
)
wfCctOptsCngcQp2Threshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCctOptsCngcQp2Threshold.setStatus("mandatory")


class _WfCctOptsCngcQp2CngLvl0Threshold_Type(Integer32):
    """Custom type wfCctOptsCngcQp2CngLvl0Threshold based on Integer32"""
    defaultValue = 25

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_WfCctOptsCngcQp2CngLvl0Threshold_Type.__name__ = "Integer32"
_WfCctOptsCngcQp2CngLvl0Threshold_Object = MibTableColumn
wfCctOptsCngcQp2CngLvl0Threshold = _WfCctOptsCngcQp2CngLvl0Threshold_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 10, 1, 32),
    _WfCctOptsCngcQp2CngLvl0Threshold_Type()
)
wfCctOptsCngcQp2CngLvl0Threshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCctOptsCngcQp2CngLvl0Threshold.setStatus("mandatory")


class _WfCctOptsCngcQp2CngLvl1Threshold_Type(Integer32):
    """Custom type wfCctOptsCngcQp2CngLvl1Threshold based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_WfCctOptsCngcQp2CngLvl1Threshold_Type.__name__ = "Integer32"
_WfCctOptsCngcQp2CngLvl1Threshold_Object = MibTableColumn
wfCctOptsCngcQp2CngLvl1Threshold = _WfCctOptsCngcQp2CngLvl1Threshold_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 10, 1, 33),
    _WfCctOptsCngcQp2CngLvl1Threshold_Type()
)
wfCctOptsCngcQp2CngLvl1Threshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCctOptsCngcQp2CngLvl1Threshold.setStatus("mandatory")


class _WfCctOptsCngcQp2CngLvl2Threshold_Type(Integer32):
    """Custom type wfCctOptsCngcQp2CngLvl2Threshold based on Integer32"""
    defaultValue = 75

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_WfCctOptsCngcQp2CngLvl2Threshold_Type.__name__ = "Integer32"
_WfCctOptsCngcQp2CngLvl2Threshold_Object = MibTableColumn
wfCctOptsCngcQp2CngLvl2Threshold = _WfCctOptsCngcQp2CngLvl2Threshold_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 10, 1, 34),
    _WfCctOptsCngcQp2CngLvl2Threshold_Type()
)
wfCctOptsCngcQp2CngLvl2Threshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCctOptsCngcQp2CngLvl2Threshold.setStatus("mandatory")


class _WfCctOptsCngcQp2PktsServPriNxtQ_Type(Integer32):
    """Custom type wfCctOptsCngcQp2PktsServPriNxtQ based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_WfCctOptsCngcQp2PktsServPriNxtQ_Type.__name__ = "Integer32"
_WfCctOptsCngcQp2PktsServPriNxtQ_Object = MibTableColumn
wfCctOptsCngcQp2PktsServPriNxtQ = _WfCctOptsCngcQp2PktsServPriNxtQ_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 10, 1, 35),
    _WfCctOptsCngcQp2PktsServPriNxtQ_Type()
)
wfCctOptsCngcQp2PktsServPriNxtQ.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCctOptsCngcQp2PktsServPriNxtQ.setStatus("mandatory")


class _WfCctOptsCngcCfgQp3Threshold_Type(Integer32):
    """Custom type wfCctOptsCngcCfgQp3Threshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2048),
    )


_WfCctOptsCngcCfgQp3Threshold_Type.__name__ = "Integer32"
_WfCctOptsCngcCfgQp3Threshold_Object = MibTableColumn
wfCctOptsCngcCfgQp3Threshold = _WfCctOptsCngcCfgQp3Threshold_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 10, 1, 36),
    _WfCctOptsCngcCfgQp3Threshold_Type()
)
wfCctOptsCngcCfgQp3Threshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCctOptsCngcCfgQp3Threshold.setStatus("mandatory")
_WfCctOptsCngcQp3Threshold_Type = Integer32
_WfCctOptsCngcQp3Threshold_Object = MibTableColumn
wfCctOptsCngcQp3Threshold = _WfCctOptsCngcQp3Threshold_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 10, 1, 37),
    _WfCctOptsCngcQp3Threshold_Type()
)
wfCctOptsCngcQp3Threshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCctOptsCngcQp3Threshold.setStatus("mandatory")


class _WfCctOptsCngcQp3CngLvl0Threshold_Type(Integer32):
    """Custom type wfCctOptsCngcQp3CngLvl0Threshold based on Integer32"""
    defaultValue = 25

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_WfCctOptsCngcQp3CngLvl0Threshold_Type.__name__ = "Integer32"
_WfCctOptsCngcQp3CngLvl0Threshold_Object = MibTableColumn
wfCctOptsCngcQp3CngLvl0Threshold = _WfCctOptsCngcQp3CngLvl0Threshold_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 10, 1, 38),
    _WfCctOptsCngcQp3CngLvl0Threshold_Type()
)
wfCctOptsCngcQp3CngLvl0Threshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCctOptsCngcQp3CngLvl0Threshold.setStatus("mandatory")


class _WfCctOptsCngcQp3CngLvl1Threshold_Type(Integer32):
    """Custom type wfCctOptsCngcQp3CngLvl1Threshold based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_WfCctOptsCngcQp3CngLvl1Threshold_Type.__name__ = "Integer32"
_WfCctOptsCngcQp3CngLvl1Threshold_Object = MibTableColumn
wfCctOptsCngcQp3CngLvl1Threshold = _WfCctOptsCngcQp3CngLvl1Threshold_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 10, 1, 39),
    _WfCctOptsCngcQp3CngLvl1Threshold_Type()
)
wfCctOptsCngcQp3CngLvl1Threshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCctOptsCngcQp3CngLvl1Threshold.setStatus("mandatory")


class _WfCctOptsCngcQp3CngLvl2Threshold_Type(Integer32):
    """Custom type wfCctOptsCngcQp3CngLvl2Threshold based on Integer32"""
    defaultValue = 75

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_WfCctOptsCngcQp3CngLvl2Threshold_Type.__name__ = "Integer32"
_WfCctOptsCngcQp3CngLvl2Threshold_Object = MibTableColumn
wfCctOptsCngcQp3CngLvl2Threshold = _WfCctOptsCngcQp3CngLvl2Threshold_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 10, 1, 40),
    _WfCctOptsCngcQp3CngLvl2Threshold_Type()
)
wfCctOptsCngcQp3CngLvl2Threshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCctOptsCngcQp3CngLvl2Threshold.setStatus("mandatory")
_WfCctOptsCngcPriority0TxPkts_Type = Counter32
_WfCctOptsCngcPriority0TxPkts_Object = MibTableColumn
wfCctOptsCngcPriority0TxPkts = _WfCctOptsCngcPriority0TxPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 10, 1, 41),
    _WfCctOptsCngcPriority0TxPkts_Type()
)
wfCctOptsCngcPriority0TxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCctOptsCngcPriority0TxPkts.setStatus("mandatory")
_WfCctOptsCngcPriority0TxOctets_Type = Counter32
_WfCctOptsCngcPriority0TxOctets_Object = MibTableColumn
wfCctOptsCngcPriority0TxOctets = _WfCctOptsCngcPriority0TxOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 10, 1, 42),
    _WfCctOptsCngcPriority0TxOctets_Type()
)
wfCctOptsCngcPriority0TxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCctOptsCngcPriority0TxOctets.setStatus("mandatory")
_WfCctOptsCngcPriority0DropPkts_Type = Counter32
_WfCctOptsCngcPriority0DropPkts_Object = MibTableColumn
wfCctOptsCngcPriority0DropPkts = _WfCctOptsCngcPriority0DropPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 10, 1, 43),
    _WfCctOptsCngcPriority0DropPkts_Type()
)
wfCctOptsCngcPriority0DropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCctOptsCngcPriority0DropPkts.setStatus("mandatory")
_WfCctOptsCngcPriority0DropOctets_Type = Counter32
_WfCctOptsCngcPriority0DropOctets_Object = MibTableColumn
wfCctOptsCngcPriority0DropOctets = _WfCctOptsCngcPriority0DropOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 10, 1, 44),
    _WfCctOptsCngcPriority0DropOctets_Type()
)
wfCctOptsCngcPriority0DropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCctOptsCngcPriority0DropOctets.setStatus("mandatory")
_WfCctOptsCngcPriority1TxPkts_Type = Counter32
_WfCctOptsCngcPriority1TxPkts_Object = MibTableColumn
wfCctOptsCngcPriority1TxPkts = _WfCctOptsCngcPriority1TxPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 10, 1, 45),
    _WfCctOptsCngcPriority1TxPkts_Type()
)
wfCctOptsCngcPriority1TxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCctOptsCngcPriority1TxPkts.setStatus("mandatory")
_WfCctOptsCngcPriority1TxOctets_Type = Counter32
_WfCctOptsCngcPriority1TxOctets_Object = MibTableColumn
wfCctOptsCngcPriority1TxOctets = _WfCctOptsCngcPriority1TxOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 10, 1, 46),
    _WfCctOptsCngcPriority1TxOctets_Type()
)
wfCctOptsCngcPriority1TxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCctOptsCngcPriority1TxOctets.setStatus("mandatory")
_WfCctOptsCngcPriority1DropPkts_Type = Counter32
_WfCctOptsCngcPriority1DropPkts_Object = MibTableColumn
wfCctOptsCngcPriority1DropPkts = _WfCctOptsCngcPriority1DropPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 10, 1, 47),
    _WfCctOptsCngcPriority1DropPkts_Type()
)
wfCctOptsCngcPriority1DropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCctOptsCngcPriority1DropPkts.setStatus("mandatory")
_WfCctOptsCngcPriority1DropOctets_Type = Counter32
_WfCctOptsCngcPriority1DropOctets_Object = MibTableColumn
wfCctOptsCngcPriority1DropOctets = _WfCctOptsCngcPriority1DropOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 10, 1, 48),
    _WfCctOptsCngcPriority1DropOctets_Type()
)
wfCctOptsCngcPriority1DropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCctOptsCngcPriority1DropOctets.setStatus("mandatory")
_WfCctOptsCngcPriority2TxPkts_Type = Counter32
_WfCctOptsCngcPriority2TxPkts_Object = MibTableColumn
wfCctOptsCngcPriority2TxPkts = _WfCctOptsCngcPriority2TxPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 10, 1, 49),
    _WfCctOptsCngcPriority2TxPkts_Type()
)
wfCctOptsCngcPriority2TxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCctOptsCngcPriority2TxPkts.setStatus("mandatory")
_WfCctOptsCngcPriority2TxOctets_Type = Counter32
_WfCctOptsCngcPriority2TxOctets_Object = MibTableColumn
wfCctOptsCngcPriority2TxOctets = _WfCctOptsCngcPriority2TxOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 10, 1, 50),
    _WfCctOptsCngcPriority2TxOctets_Type()
)
wfCctOptsCngcPriority2TxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCctOptsCngcPriority2TxOctets.setStatus("mandatory")
_WfCctOptsCngcPriority2DropPkts_Type = Counter32
_WfCctOptsCngcPriority2DropPkts_Object = MibTableColumn
wfCctOptsCngcPriority2DropPkts = _WfCctOptsCngcPriority2DropPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 10, 1, 51),
    _WfCctOptsCngcPriority2DropPkts_Type()
)
wfCctOptsCngcPriority2DropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCctOptsCngcPriority2DropPkts.setStatus("mandatory")
_WfCctOptsCngcPriority2DropOctets_Type = Counter32
_WfCctOptsCngcPriority2DropOctets_Object = MibTableColumn
wfCctOptsCngcPriority2DropOctets = _WfCctOptsCngcPriority2DropOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 10, 1, 52),
    _WfCctOptsCngcPriority2DropOctets_Type()
)
wfCctOptsCngcPriority2DropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCctOptsCngcPriority2DropOctets.setStatus("mandatory")
_WfCctOptsCngcPriority3TxPkts_Type = Counter32
_WfCctOptsCngcPriority3TxPkts_Object = MibTableColumn
wfCctOptsCngcPriority3TxPkts = _WfCctOptsCngcPriority3TxPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 10, 1, 53),
    _WfCctOptsCngcPriority3TxPkts_Type()
)
wfCctOptsCngcPriority3TxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCctOptsCngcPriority3TxPkts.setStatus("mandatory")
_WfCctOptsCngcPriority3TxOctets_Type = Counter32
_WfCctOptsCngcPriority3TxOctets_Object = MibTableColumn
wfCctOptsCngcPriority3TxOctets = _WfCctOptsCngcPriority3TxOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 10, 1, 54),
    _WfCctOptsCngcPriority3TxOctets_Type()
)
wfCctOptsCngcPriority3TxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCctOptsCngcPriority3TxOctets.setStatus("mandatory")
_WfCctOptsCngcPriority3DropPkts_Type = Counter32
_WfCctOptsCngcPriority3DropPkts_Object = MibTableColumn
wfCctOptsCngcPriority3DropPkts = _WfCctOptsCngcPriority3DropPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 10, 1, 55),
    _WfCctOptsCngcPriority3DropPkts_Type()
)
wfCctOptsCngcPriority3DropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCctOptsCngcPriority3DropPkts.setStatus("mandatory")
_WfCctOptsCngcPriority3DropOctets_Type = Counter32
_WfCctOptsCngcPriority3DropOctets_Object = MibTableColumn
wfCctOptsCngcPriority3DropOctets = _WfCctOptsCngcPriority3DropOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 10, 1, 56),
    _WfCctOptsCngcPriority3DropOctets_Type()
)
wfCctOptsCngcPriority3DropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCctOptsCngcPriority3DropOctets.setStatus("mandatory")
_WfCctOptsCngcTxFRNonDePkts_Type = Counter32
_WfCctOptsCngcTxFRNonDePkts_Object = MibTableColumn
wfCctOptsCngcTxFRNonDePkts = _WfCctOptsCngcTxFRNonDePkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 10, 1, 57),
    _WfCctOptsCngcTxFRNonDePkts_Type()
)
wfCctOptsCngcTxFRNonDePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCctOptsCngcTxFRNonDePkts.setStatus("mandatory")
_WfCctOptsCngcTxFRNonDeOctets_Type = Counter32
_WfCctOptsCngcTxFRNonDeOctets_Object = MibTableColumn
wfCctOptsCngcTxFRNonDeOctets = _WfCctOptsCngcTxFRNonDeOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 10, 1, 58),
    _WfCctOptsCngcTxFRNonDeOctets_Type()
)
wfCctOptsCngcTxFRNonDeOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCctOptsCngcTxFRNonDeOctets.setStatus("mandatory")
_WfCctOptsCngcTxFRDePkts_Type = Counter32
_WfCctOptsCngcTxFRDePkts_Object = MibTableColumn
wfCctOptsCngcTxFRDePkts = _WfCctOptsCngcTxFRDePkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 10, 1, 59),
    _WfCctOptsCngcTxFRDePkts_Type()
)
wfCctOptsCngcTxFRDePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCctOptsCngcTxFRDePkts.setStatus("mandatory")
_WfCctOptsCngcTxFRDeOctets_Type = Counter32
_WfCctOptsCngcTxFRDeOctets_Object = MibTableColumn
wfCctOptsCngcTxFRDeOctets = _WfCctOptsCngcTxFRDeOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 10, 1, 60),
    _WfCctOptsCngcTxFRDeOctets_Type()
)
wfCctOptsCngcTxFRDeOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCctOptsCngcTxFRDeOctets.setStatus("mandatory")
_WfCctOptsCngcDropFRNonDePkts_Type = Counter32
_WfCctOptsCngcDropFRNonDePkts_Object = MibTableColumn
wfCctOptsCngcDropFRNonDePkts = _WfCctOptsCngcDropFRNonDePkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 10, 1, 61),
    _WfCctOptsCngcDropFRNonDePkts_Type()
)
wfCctOptsCngcDropFRNonDePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCctOptsCngcDropFRNonDePkts.setStatus("mandatory")
_WfCctOptsCngcDropFRNonDeOctets_Type = Counter32
_WfCctOptsCngcDropFRNonDeOctets_Object = MibTableColumn
wfCctOptsCngcDropFRNonDeOctets = _WfCctOptsCngcDropFRNonDeOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 10, 1, 62),
    _WfCctOptsCngcDropFRNonDeOctets_Type()
)
wfCctOptsCngcDropFRNonDeOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCctOptsCngcDropFRNonDeOctets.setStatus("mandatory")
_WfCctOptsCngcDropFRDePkts_Type = Counter32
_WfCctOptsCngcDropFRDePkts_Object = MibTableColumn
wfCctOptsCngcDropFRDePkts = _WfCctOptsCngcDropFRDePkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 10, 1, 63),
    _WfCctOptsCngcDropFRDePkts_Type()
)
wfCctOptsCngcDropFRDePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCctOptsCngcDropFRDePkts.setStatus("mandatory")
_WfCctOptsCngcDropFRDeOctets_Type = Counter32
_WfCctOptsCngcDropFRDeOctets_Object = MibTableColumn
wfCctOptsCngcDropFRDeOctets = _WfCctOptsCngcDropFRDeOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 10, 1, 64),
    _WfCctOptsCngcDropFRDeOctets_Type()
)
wfCctOptsCngcDropFRDeOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCctOptsCngcDropFRDeOctets.setStatus("mandatory")
_WfCctOptsCngcFRSetFecnPkts_Type = Counter32
_WfCctOptsCngcFRSetFecnPkts_Object = MibTableColumn
wfCctOptsCngcFRSetFecnPkts = _WfCctOptsCngcFRSetFecnPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 10, 1, 65),
    _WfCctOptsCngcFRSetFecnPkts_Type()
)
wfCctOptsCngcFRSetFecnPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCctOptsCngcFRSetFecnPkts.setStatus("mandatory")
_WfCctOptsCngcFRSetFecnOctets_Type = Counter32
_WfCctOptsCngcFRSetFecnOctets_Object = MibTableColumn
wfCctOptsCngcFRSetFecnOctets = _WfCctOptsCngcFRSetFecnOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 10, 1, 66),
    _WfCctOptsCngcFRSetFecnOctets_Type()
)
wfCctOptsCngcFRSetFecnOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCctOptsCngcFRSetFecnOctets.setStatus("mandatory")
_WfCctOptsCngcFRSetBecnPkts_Type = Counter32
_WfCctOptsCngcFRSetBecnPkts_Object = MibTableColumn
wfCctOptsCngcFRSetBecnPkts = _WfCctOptsCngcFRSetBecnPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 10, 1, 67),
    _WfCctOptsCngcFRSetBecnPkts_Type()
)
wfCctOptsCngcFRSetBecnPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCctOptsCngcFRSetBecnPkts.setStatus("mandatory")
_WfCctOptsCngcFRSetBecnOctets_Type = Counter32
_WfCctOptsCngcFRSetBecnOctets_Object = MibTableColumn
wfCctOptsCngcFRSetBecnOctets = _WfCctOptsCngcFRSetBecnOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 10, 1, 68),
    _WfCctOptsCngcFRSetBecnOctets_Type()
)
wfCctOptsCngcFRSetBecnOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCctOptsCngcFRSetBecnOctets.setStatus("mandatory")
_WfCctOptsCngcDropNonFRPkts_Type = Counter32
_WfCctOptsCngcDropNonFRPkts_Object = MibTableColumn
wfCctOptsCngcDropNonFRPkts = _WfCctOptsCngcDropNonFRPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 10, 1, 69),
    _WfCctOptsCngcDropNonFRPkts_Type()
)
wfCctOptsCngcDropNonFRPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCctOptsCngcDropNonFRPkts.setStatus("mandatory")
_WfCctOptsCngcDropNonFROctets_Type = Counter32
_WfCctOptsCngcDropNonFROctets_Object = MibTableColumn
wfCctOptsCngcDropNonFROctets = _WfCctOptsCngcDropNonFROctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 10, 1, 70),
    _WfCctOptsCngcDropNonFROctets_Type()
)
wfCctOptsCngcDropNonFROctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCctOptsCngcDropNonFROctets.setStatus("mandatory")


class _WfCctOptsCngcLogPower_Type(Integer32):
    """Custom type wfCctOptsCngcLogPower based on Integer32"""
    defaultValue = 31

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 31),
    )


_WfCctOptsCngcLogPower_Type.__name__ = "Integer32"
_WfCctOptsCngcLogPower_Object = MibTableColumn
wfCctOptsCngcLogPower = _WfCctOptsCngcLogPower_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 10, 1, 71),
    _WfCctOptsCngcLogPower_Type()
)
wfCctOptsCngcLogPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCctOptsCngcLogPower.setStatus("mandatory")
_WfSwservTODTable_Object = MibTable
wfSwservTODTable = _WfSwservTODTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 11)
)
if mibBuilder.loadTexts:
    wfSwservTODTable.setStatus("mandatory")
_WfSwservTODEntry_Object = MibTableRow
wfSwservTODEntry = _WfSwservTODEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 11, 1)
)
wfSwservTODEntry.setIndexNames(
    (0, "Wellfleet-CCTOPTS-MIB", "wfSwservTODCct"),
    (0, "Wellfleet-CCTOPTS-MIB", "wfSwservTODIndex"),
)
if mibBuilder.loadTexts:
    wfSwservTODEntry.setStatus("mandatory")


class _WfSwservTODDelete_Type(Integer32):
    """Custom type wfSwservTODDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("delete", 2))
    )


_WfSwservTODDelete_Type.__name__ = "Integer32"
_WfSwservTODDelete_Object = MibTableColumn
wfSwservTODDelete = _WfSwservTODDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 11, 1, 1),
    _WfSwservTODDelete_Type()
)
wfSwservTODDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSwservTODDelete.setStatus("mandatory")


class _WfSwservTODCct_Type(Integer32):
    """Custom type wfSwservTODCct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_WfSwservTODCct_Type.__name__ = "Integer32"
_WfSwservTODCct_Object = MibTableColumn
wfSwservTODCct = _WfSwservTODCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 11, 1, 2),
    _WfSwservTODCct_Type()
)
wfSwservTODCct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSwservTODCct.setStatus("mandatory")


class _WfSwservTODIndex_Type(Integer32):
    """Custom type wfSwservTODIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_WfSwservTODIndex_Type.__name__ = "Integer32"
_WfSwservTODIndex_Object = MibTableColumn
wfSwservTODIndex = _WfSwservTODIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 11, 1, 3),
    _WfSwservTODIndex_Type()
)
wfSwservTODIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSwservTODIndex.setStatus("mandatory")


class _WfSwservTODType_Type(Integer32):
    """Custom type wfSwservTODType based on Integer32"""
    defaultValue = 8

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
              9)
        )
    )
    namedValues = NamedValues(
        *(("fri", 6),
          ("mon", 2),
          ("sat", 7),
          ("sun", 1),
          ("thurs", 5),
          ("tues", 3),
          ("wed", 4),
          ("weekday", 8),
          ("weekend", 9))
    )


_WfSwservTODType_Type.__name__ = "Integer32"
_WfSwservTODType_Object = MibTableColumn
wfSwservTODType = _WfSwservTODType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 11, 1, 4),
    _WfSwservTODType_Type()
)
wfSwservTODType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSwservTODType.setStatus("mandatory")


class _WfSwservTODStartTime_Type(Integer32):
    """Custom type wfSwservTODStartTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2400),
    )


_WfSwservTODStartTime_Type.__name__ = "Integer32"
_WfSwservTODStartTime_Object = MibTableColumn
wfSwservTODStartTime = _WfSwservTODStartTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 11, 1, 5),
    _WfSwservTODStartTime_Type()
)
wfSwservTODStartTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSwservTODStartTime.setStatus("mandatory")


class _WfSwservTODEndTime_Type(Integer32):
    """Custom type wfSwservTODEndTime based on Integer32"""
    defaultValue = 2400

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2400),
    )


_WfSwservTODEndTime_Type.__name__ = "Integer32"
_WfSwservTODEndTime_Object = MibTableColumn
wfSwservTODEndTime = _WfSwservTODEndTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 11, 1, 6),
    _WfSwservTODEndTime_Type()
)
wfSwservTODEndTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSwservTODEndTime.setStatus("mandatory")


class _WfSwservTODInactivityEnable_Type(Integer32):
    """Custom type wfSwservTODInactivityEnable based on Integer32"""
    defaultValue = 2

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


_WfSwservTODInactivityEnable_Type.__name__ = "Integer32"
_WfSwservTODInactivityEnable_Object = MibTableColumn
wfSwservTODInactivityEnable = _WfSwservTODInactivityEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 11, 1, 7),
    _WfSwservTODInactivityEnable_Type()
)
wfSwservTODInactivityEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSwservTODInactivityEnable.setStatus("mandatory")


class _WfSwservTODAvailabilityMode_Type(Integer32):
    """Custom type wfSwservTODAvailabilityMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("available", 1),
          ("notavailable", 2))
    )


_WfSwservTODAvailabilityMode_Type.__name__ = "Integer32"
_WfSwservTODAvailabilityMode_Object = MibTableColumn
wfSwservTODAvailabilityMode = _WfSwservTODAvailabilityMode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 11, 1, 8),
    _WfSwservTODAvailabilityMode_Type()
)
wfSwservTODAvailabilityMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSwservTODAvailabilityMode.setStatus("mandatory")


class _WfSwservTODStandbyFailBackMode_Type(Integer32):
    """Custom type wfSwservTODStandbyFailBackMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 1),
          ("manual", 2))
    )


_WfSwservTODStandbyFailBackMode_Type.__name__ = "Integer32"
_WfSwservTODStandbyFailBackMode_Object = MibTableColumn
wfSwservTODStandbyFailBackMode = _WfSwservTODStandbyFailBackMode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 11, 1, 9),
    _WfSwservTODStandbyFailBackMode_Type()
)
wfSwservTODStandbyFailBackMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSwservTODStandbyFailBackMode.setStatus("mandatory")


class _WfSwservTODStandbyFailBackTime_Type(Integer32):
    """Custom type wfSwservTODStandbyFailBackTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1439),
    )


_WfSwservTODStandbyFailBackTime_Type.__name__ = "Integer32"
_WfSwservTODStandbyFailBackTime_Object = MibTableColumn
wfSwservTODStandbyFailBackTime = _WfSwservTODStandbyFailBackTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 11, 1, 10),
    _WfSwservTODStandbyFailBackTime_Type()
)
wfSwservTODStandbyFailBackTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSwservTODStandbyFailBackTime.setStatus("mandatory")
_WfDemandCctGrpTable_Object = MibTable
wfDemandCctGrpTable = _WfDemandCctGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 12)
)
if mibBuilder.loadTexts:
    wfDemandCctGrpTable.setStatus("mandatory")
_WfDemandCctGrpEntry_Object = MibTableRow
wfDemandCctGrpEntry = _WfDemandCctGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 12, 1)
)
wfDemandCctGrpEntry.setIndexNames(
    (0, "Wellfleet-CCTOPTS-MIB", "wfDmdCctGroupNum"),
    (0, "Wellfleet-CCTOPTS-MIB", "wfDmdCctGroupPoolId"),
)
if mibBuilder.loadTexts:
    wfDemandCctGrpEntry.setStatus("mandatory")


class _WfDmdCctGroupDelete_Type(Integer32):
    """Custom type wfDmdCctGroupDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfDmdCctGroupDelete_Type.__name__ = "Integer32"
_WfDmdCctGroupDelete_Object = MibTableColumn
wfDmdCctGroupDelete = _WfDmdCctGroupDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 12, 1, 1),
    _WfDmdCctGroupDelete_Type()
)
wfDmdCctGroupDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDmdCctGroupDelete.setStatus("mandatory")
_WfDmdCctGroupNum_Type = Integer32
_WfDmdCctGroupNum_Object = MibTableColumn
wfDmdCctGroupNum = _WfDmdCctGroupNum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 12, 1, 2),
    _WfDmdCctGroupNum_Type()
)
wfDmdCctGroupNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDmdCctGroupNum.setStatus("mandatory")


class _WfDmdCctGroupPoolId_Type(Integer32):
    """Custom type wfDmdCctGroupPoolId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_WfDmdCctGroupPoolId_Type.__name__ = "Integer32"
_WfDmdCctGroupPoolId_Object = MibTableColumn
wfDmdCctGroupPoolId = _WfDmdCctGroupPoolId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 12, 1, 3),
    _WfDmdCctGroupPoolId_Type()
)
wfDmdCctGroupPoolId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDmdCctGroupPoolId.setStatus("mandatory")


class _WfDmdCctGroupNumofCcts_Type(Integer32):
    """Custom type wfDmdCctGroupNumofCcts based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 124),
    )


_WfDmdCctGroupNumofCcts_Type.__name__ = "Integer32"
_WfDmdCctGroupNumofCcts_Object = MibTableColumn
wfDmdCctGroupNumofCcts = _WfDmdCctGroupNumofCcts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 12, 1, 4),
    _WfDmdCctGroupNumofCcts_Type()
)
wfDmdCctGroupNumofCcts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDmdCctGroupNumofCcts.setStatus("mandatory")


class _WfDmdCctGroupIPEnable_Type(Integer32):
    """Custom type wfDmdCctGroupIPEnable based on Integer32"""
    defaultValue = 2

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


_WfDmdCctGroupIPEnable_Type.__name__ = "Integer32"
_WfDmdCctGroupIPEnable_Object = MibTableColumn
wfDmdCctGroupIPEnable = _WfDmdCctGroupIPEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 12, 1, 5),
    _WfDmdCctGroupIPEnable_Type()
)
wfDmdCctGroupIPEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDmdCctGroupIPEnable.setStatus("mandatory")
_WfDmdCctGroupIPUnnumAssoc_Type = IpAddress
_WfDmdCctGroupIPUnnumAssoc_Object = MibTableColumn
wfDmdCctGroupIPUnnumAssoc = _WfDmdCctGroupIPUnnumAssoc_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 12, 1, 6),
    _WfDmdCctGroupIPUnnumAssoc_Type()
)
wfDmdCctGroupIPUnnumAssoc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDmdCctGroupIPUnnumAssoc.setStatus("mandatory")


class _WfDmdCctGroupRIPEnable_Type(Integer32):
    """Custom type wfDmdCctGroupRIPEnable based on Integer32"""
    defaultValue = 2

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


_WfDmdCctGroupRIPEnable_Type.__name__ = "Integer32"
_WfDmdCctGroupRIPEnable_Object = MibTableColumn
wfDmdCctGroupRIPEnable = _WfDmdCctGroupRIPEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 12, 1, 7),
    _WfDmdCctGroupRIPEnable_Type()
)
wfDmdCctGroupRIPEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDmdCctGroupRIPEnable.setStatus("mandatory")


class _WfDmdCctGroupOSPFEnable_Type(Integer32):
    """Custom type wfDmdCctGroupOSPFEnable based on Integer32"""
    defaultValue = 2

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


_WfDmdCctGroupOSPFEnable_Type.__name__ = "Integer32"
_WfDmdCctGroupOSPFEnable_Object = MibTableColumn
wfDmdCctGroupOSPFEnable = _WfDmdCctGroupOSPFEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 12, 1, 8),
    _WfDmdCctGroupOSPFEnable_Type()
)
wfDmdCctGroupOSPFEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDmdCctGroupOSPFEnable.setStatus("mandatory")


class _WfDmdCctGroupIPXEnable_Type(Integer32):
    """Custom type wfDmdCctGroupIPXEnable based on Integer32"""
    defaultValue = 2

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


_WfDmdCctGroupIPXEnable_Type.__name__ = "Integer32"
_WfDmdCctGroupIPXEnable_Object = MibTableColumn
wfDmdCctGroupIPXEnable = _WfDmdCctGroupIPXEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 12, 1, 9),
    _WfDmdCctGroupIPXEnable_Type()
)
wfDmdCctGroupIPXEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDmdCctGroupIPXEnable.setStatus("mandatory")


class _WfDmdCctGroupBridgeEnable_Type(Integer32):
    """Custom type wfDmdCctGroupBridgeEnable based on Integer32"""
    defaultValue = 2

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


_WfDmdCctGroupBridgeEnable_Type.__name__ = "Integer32"
_WfDmdCctGroupBridgeEnable_Object = MibTableColumn
wfDmdCctGroupBridgeEnable = _WfDmdCctGroupBridgeEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 12, 1, 10),
    _WfDmdCctGroupBridgeEnable_Type()
)
wfDmdCctGroupBridgeEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDmdCctGroupBridgeEnable.setStatus("mandatory")
_WfDmdCctGroupCctList_Type = OctetString
_WfDmdCctGroupCctList_Object = MibTableColumn
wfDmdCctGroupCctList = _WfDmdCctGroupCctList_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 12, 1, 11),
    _WfDmdCctGroupCctList_Type()
)
wfDmdCctGroupCctList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDmdCctGroupCctList.setStatus("mandatory")


class _WfDmdCctGroupIPXRouting_Type(Integer32):
    """Custom type wfDmdCctGroupIPXRouting based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nlsp", 2),
          ("rip", 1),
          ("ripnlsp", 3))
    )


_WfDmdCctGroupIPXRouting_Type.__name__ = "Integer32"
_WfDmdCctGroupIPXRouting_Object = MibTableColumn
wfDmdCctGroupIPXRouting = _WfDmdCctGroupIPXRouting_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 12, 1, 12),
    _WfDmdCctGroupIPXRouting_Type()
)
wfDmdCctGroupIPXRouting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDmdCctGroupIPXRouting.setStatus("mandatory")


class _WfDmdCctGroupIPXWANEnable_Type(Integer32):
    """Custom type wfDmdCctGroupIPXWANEnable based on Integer32"""
    defaultValue = 2

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


_WfDmdCctGroupIPXWANEnable_Type.__name__ = "Integer32"
_WfDmdCctGroupIPXWANEnable_Object = MibTableColumn
wfDmdCctGroupIPXWANEnable = _WfDmdCctGroupIPXWANEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 12, 1, 13),
    _WfDmdCctGroupIPXWANEnable_Type()
)
wfDmdCctGroupIPXWANEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDmdCctGroupIPXWANEnable.setStatus("mandatory")


class _WfDmdCctGroupRadiusEnable_Type(Integer32):
    """Custom type wfDmdCctGroupRadiusEnable based on Integer32"""
    defaultValue = 2

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


_WfDmdCctGroupRadiusEnable_Type.__name__ = "Integer32"
_WfDmdCctGroupRadiusEnable_Object = MibTableColumn
wfDmdCctGroupRadiusEnable = _WfDmdCctGroupRadiusEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 12, 1, 14),
    _WfDmdCctGroupRadiusEnable_Type()
)
wfDmdCctGroupRadiusEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDmdCctGroupRadiusEnable.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-CCTOPTS-MIB",
    **{"wfCctOptsTable": wfCctOptsTable,
       "wfCctOptsEntry": wfCctOptsEntry,
       "wfCctOptsDelete": wfCctOptsDelete,
       "wfCctOptsPriorityQueueingDisable": wfCctOptsPriorityQueueingDisable,
       "wfCctOptsCct": wfCctOptsCct,
       "wfCctOptsHighPriorityQueueLimit": wfCctOptsHighPriorityQueueLimit,
       "wfCctOptsNormalPriorityQueueLimit": wfCctOptsNormalPriorityQueueLimit,
       "wfCctOptsLowPriorityQueueLimit": wfCctOptsLowPriorityQueueLimit,
       "wfCctOptsMaxInterruptQueueLatency": wfCctOptsMaxInterruptQueueLatency,
       "wfCctOptsMaxHighPriorityQueueLatency": wfCctOptsMaxHighPriorityQueueLatency,
       "wfCctOptsHiXmits": wfCctOptsHiXmits,
       "wfCctOptsNormalXmits": wfCctOptsNormalXmits,
       "wfCctOptsLoXmits": wfCctOptsLoXmits,
       "wfCctOptsHiClippedPkts": wfCctOptsHiClippedPkts,
       "wfCctOptsNormalClippedPkts": wfCctOptsNormalClippedPkts,
       "wfCctOptsLoClippedPkts": wfCctOptsLoClippedPkts,
       "wfCctOptsIntrQHighWaterPkts": wfCctOptsIntrQHighWaterPkts,
       "wfCctOptsHiQHighWaterPkts": wfCctOptsHiQHighWaterPkts,
       "wfCctOptsNormalQHighWaterPkts": wfCctOptsNormalQHighWaterPkts,
       "wfCctOptsLoQHighWaterPkts": wfCctOptsLoQHighWaterPkts,
       "wfCctOptsHighWaterPktsClear": wfCctOptsHighWaterPktsClear,
       "wfCctOptsDroppedPkts": wfCctOptsDroppedPkts,
       "wfCctOptsLargePkts": wfCctOptsLargePkts,
       "wfCctOptsRxPkts": wfCctOptsRxPkts,
       "wfCctOptsChooserType": wfCctOptsChooserType,
       "wfCctOptsPqDequeueAlgType": wfCctOptsPqDequeueAlgType,
       "wfCctOptsHiPercent": wfCctOptsHiPercent,
       "wfCctOptsNormalPercent": wfCctOptsNormalPercent,
       "wfCctOptsLoPercent": wfCctOptsLoPercent,
       "wfCctOptsHiTotalOctets": wfCctOptsHiTotalOctets,
       "wfCctOptsNormalTotalOctets": wfCctOptsNormalTotalOctets,
       "wfCctOptsLoTotalOctets": wfCctOptsLoTotalOctets,
       "wfCctOptsCircuitType": wfCctOptsCircuitType,
       "wfCctOptsBackupCct": wfCctOptsBackupCct,
       "wfCctOptsPrimaryCctWanProtocolType": wfCctOptsPrimaryCctWanProtocolType,
       "wfCctOptsMacFilterFormat": wfCctOptsMacFilterFormat,
       "wfCctOptsPktsNotQueued": wfCctOptsPktsNotQueued,
       "wfCctOptsBitsShiftCount": wfCctOptsBitsShiftCount,
       "wfCctOptsFrSetDeLowQ": wfCctOptsFrSetDeLowQ,
       "wfCctOptsFrSetDeNormQ": wfCctOptsFrSetDeNormQ,
       "wfCctOptsShapedPriorityQueueLimit": wfCctOptsShapedPriorityQueueLimit,
       "wfCctOptsMaxShapedPriorityQueueLatency": wfCctOptsMaxShapedPriorityQueueLatency,
       "wfCctOptsShapedXmits": wfCctOptsShapedXmits,
       "wfCctOptsShapedClippedPkts": wfCctOptsShapedClippedPkts,
       "wfCctOptsShapedQHighWaterPkts": wfCctOptsShapedQHighWaterPkts,
       "wfCctOptsShapedTotalOctets": wfCctOptsShapedTotalOctets,
       "wfCctOptsPpqDebugLevel": wfCctOptsPpqDebugLevel,
       "wfDequeueAtLineRate": wfDequeueAtLineRate,
       "wfCctOptsBrFilterTable": wfCctOptsBrFilterTable,
       "wfCctOptsBrFilterEntry": wfCctOptsBrFilterEntry,
       "wfCctOptsBrFilterCreate": wfCctOptsBrFilterCreate,
       "wfCctOptsBrFilterEnable": wfCctOptsBrFilterEnable,
       "wfCctOptsBrFilterState": wfCctOptsBrFilterState,
       "wfCctOptsBrFilterCounter": wfCctOptsBrFilterCounter,
       "wfCctOptsBrFilterDefinition": wfCctOptsBrFilterDefinition,
       "wfCctOptsBrFilterReserved": wfCctOptsBrFilterReserved,
       "wfCctOptsBrFilterCct": wfCctOptsBrFilterCct,
       "wfCctOptsBrFilterRuleNumber": wfCctOptsBrFilterRuleNumber,
       "wfCctOptsBrFilterFragment": wfCctOptsBrFilterFragment,
       "wfCctOptsBrFilterName": wfCctOptsBrFilterName,
       "wfCctOptsIpFilterTable": wfCctOptsIpFilterTable,
       "wfCctOptsIpFilterEntry": wfCctOptsIpFilterEntry,
       "wfCctOptsIpFilterCreate": wfCctOptsIpFilterCreate,
       "wfCctOptsIpFilterEnable": wfCctOptsIpFilterEnable,
       "wfCctOptsIpFilterState": wfCctOptsIpFilterState,
       "wfCctOptsIpFilterCounter": wfCctOptsIpFilterCounter,
       "wfCctOptsIpFilterDefinition": wfCctOptsIpFilterDefinition,
       "wfCctOptsIpFilterReserved": wfCctOptsIpFilterReserved,
       "wfCctOptsIpFilterCct": wfCctOptsIpFilterCct,
       "wfCctOptsIpFilterRuleNumber": wfCctOptsIpFilterRuleNumber,
       "wfCctOptsIpFilterFragment": wfCctOptsIpFilterFragment,
       "wfCctOptsIpFilterName": wfCctOptsIpFilterName,
       "wfCctOptsLengthBasedTable": wfCctOptsLengthBasedTable,
       "wfCctOptsLengthBasedEntry": wfCctOptsLengthBasedEntry,
       "wfCctOptsLengthBasedDelete": wfCctOptsLengthBasedDelete,
       "wfCctOptsLengthBasedDisable": wfCctOptsLengthBasedDisable,
       "wfCctOptsLengthBasedState": wfCctOptsLengthBasedState,
       "wfCctOptsLengthBasedCct": wfCctOptsLengthBasedCct,
       "wfCctOptsLengthBasedMux": wfCctOptsLengthBasedMux,
       "wfCctOptsLengthBasedData": wfCctOptsLengthBasedData,
       "wfCctOptsLengthBasedLength": wfCctOptsLengthBasedLength,
       "wfCctOptsLengthBasedLessThanQ": wfCctOptsLengthBasedLessThanQ,
       "wfCctOptsLengthBasedGreaterThanQ": wfCctOptsLengthBasedGreaterThanQ,
       "wfSwservOptsTable": wfSwservOptsTable,
       "wfSwservOptsEntry": wfSwservOptsEntry,
       "wfSwservOptsDelete": wfSwservOptsDelete,
       "wfSwservOptsCct": wfSwservOptsCct,
       "wfSwservOptsCircuitType": wfSwservOptsCircuitType,
       "wfSwservOptsBackupCct": wfSwservOptsBackupCct,
       "wfSwservOptsBackupPool": wfSwservOptsBackupPool,
       "wfSwservOptsDemandPool": wfSwservOptsDemandPool,
       "wfSwservOptsBackupMode": wfSwservOptsBackupMode,
       "wfSwservOptsActiveBackupCct": wfSwservOptsActiveBackupCct,
       "wfSwservOptsForcedDial": wfSwservOptsForcedDial,
       "wfSwservOptsMaxUpTime": wfSwservOptsMaxUpTime,
       "wfSwservOptsBringUpHour": wfSwservOptsBringUpHour,
       "wfSwservOptsBringUpMinute": wfSwservOptsBringUpMinute,
       "wfSwservOptsTakeDownHour": wfSwservOptsTakeDownHour,
       "wfSwservOptsTakeDownMinute": wfSwservOptsTakeDownMinute,
       "wfSwservOptsInactivityTime": wfSwservOptsInactivityTime,
       "wfSwservOptsCircuitState": wfSwservOptsCircuitState,
       "wfSwservOptsPrimaryDownTime": wfSwservOptsPrimaryDownTime,
       "wfSwservOptsNumOutgoingConn": wfSwservOptsNumOutgoingConn,
       "wfSwservOptsNumIncomingConn": wfSwservOptsNumIncomingConn,
       "wfSwservOptsActiveSlot": wfSwservOptsActiveSlot,
       "wfSwservOptsActiveLine": wfSwservOptsActiveLine,
       "wfSwservOptsPacketsDropped": wfSwservOptsPacketsDropped,
       "wfSwservOptsTimeLastPktDropped": wfSwservOptsTimeLastPktDropped,
       "wfSwservOptsForcedTakedown": wfSwservOptsForcedTakedown,
       "wfSwservOptsRetryMax": wfSwservOptsRetryMax,
       "wfSwservOptsRetryCount": wfSwservOptsRetryCount,
       "wfSwservOptsRetryDelay": wfSwservOptsRetryDelay,
       "wfSwservOptsDemandConnectionMode": wfSwservOptsDemandConnectionMode,
       "wfSwservOptsAutoDemandTermination": wfSwservOptsAutoDemandTermination,
       "wfSwservOptsAutoDemandTermReset": wfSwservOptsAutoDemandTermReset,
       "wfSwservOptsChapLocalName": wfSwservOptsChapLocalName,
       "wfSwservOptsChapSecret": wfSwservOptsChapSecret,
       "wfSwservOptsMaxUpTermination": wfSwservOptsMaxUpTermination,
       "wfSwservOptsMaxUpTermReset": wfSwservOptsMaxUpTermReset,
       "wfSwservOptsBandwidthPool": wfSwservOptsBandwidthPool,
       "wfSwservOptsBandwidthMode": wfSwservOptsBandwidthMode,
       "wfSwservOptsPapId": wfSwservOptsPapId,
       "wfSwservOptsPapPassword": wfSwservOptsPapPassword,
       "wfSwservOptsDebugMsgLevel": wfSwservOptsDebugMsgLevel,
       "wfSwservOptsDmdCctGroupNum": wfSwservOptsDmdCctGroupNum,
       "wfSwservOptsWanProtocol": wfSwservOptsWanProtocol,
       "wfSwservOptsSecondaryCct": wfSwservOptsSecondaryCct,
       "wfSwservOptsPoolLineNumber": wfSwservOptsPoolLineNumber,
       "wfSwservOptsPoolLineIndex": wfSwservOptsPoolLineIndex,
       "wfSwservOptsMinDuration": wfSwservOptsMinDuration,
       "wfSwservOptsInactivityMode": wfSwservOptsInactivityMode,
       "wfSwservOptsOpportunityRouting": wfSwservOptsOpportunityRouting,
       "wfSwservOptsOutboundAuth": wfSwservOptsOutboundAuth,
       "wfSwservOptsOverSubRetryTimer": wfSwservOptsOverSubRetryTimer,
       "wfSwservOptsStandbyMode": wfSwservOptsStandbyMode,
       "wfSwservOptsStandbyFailBackMode": wfSwservOptsStandbyFailBackMode,
       "wfSwservOptsManualStandbyAction": wfSwservOptsManualStandbyAction,
       "wfSwservOptsCallbackMode": wfSwservOptsCallbackMode,
       "wfSwservOptsCallbackServerDelay": wfSwservOptsCallbackServerDelay,
       "wfSwservOptsCallbackClientDelay": wfSwservOptsCallbackClientDelay,
       "wfSwservOptsQueueSize": wfSwservOptsQueueSize,
       "wfSwservOptsDequeueWaitTimer": wfSwservOptsDequeueWaitTimer,
       "wfSwservOptsMru": wfSwservOptsMru,
       "wfSwservOptsRfc1661Compliance": wfSwservOptsRfc1661Compliance,
       "wfSwservOptsBootupDelay": wfSwservOptsBootupDelay,
       "wfSwservOptsCallbackOptRfc1570": wfSwservOptsCallbackOptRfc1570,
       "wfSwservOptsCallbackDataRfc1570": wfSwservOptsCallbackDataRfc1570,
       "wfSwservOutPhoneNumTable": wfSwservOutPhoneNumTable,
       "wfSwservOutPhoneNumEntry": wfSwservOutPhoneNumEntry,
       "wfSwservOutPhoneNumDelete": wfSwservOutPhoneNumDelete,
       "wfSwservOutPhoneNumCct": wfSwservOutPhoneNumCct,
       "wfSwservOutPhoneNumIndex": wfSwservOutPhoneNumIndex,
       "wfSwservOutPhoneNumRmtStationNum": wfSwservOutPhoneNumRmtStationNum,
       "wfSwservOutPhoneNumSubAddr": wfSwservOutPhoneNumSubAddr,
       "wfSwservOutPhoneNumDelimiter": wfSwservOutPhoneNumDelimiter,
       "wfSwservOutPhoneNumType": wfSwservOutPhoneNumType,
       "wfSwservOutPhoneNumTypeofNum": wfSwservOutPhoneNumTypeofNum,
       "wfSwservOutPhoneNumPlan": wfSwservOutPhoneNumPlan,
       "wfSwservOutPhoneNumRateAdaption": wfSwservOutPhoneNumRateAdaption,
       "wfSwservOutPhoneNumRemotePoolType": wfSwservOutPhoneNumRemotePoolType,
       "wfSwservOutPhoneNumConnectionType": wfSwservOutPhoneNumConnectionType,
       "wfSwservOutPhoneNumChannelType": wfSwservOutPhoneNumChannelType,
       "wfSwservOutPhoneNumAggrChanCnt": wfSwservOutPhoneNumAggrChanCnt,
       "wfSwservOutPhoneNumPrefix": wfSwservOutPhoneNumPrefix,
       "wfSwservOutPhoneNumBearerService": wfSwservOutPhoneNumBearerService,
       "wfSwservInPhoneNumTable": wfSwservInPhoneNumTable,
       "wfSwservInPhoneNumEntry": wfSwservInPhoneNumEntry,
       "wfSwservInPhoneNumDelete": wfSwservInPhoneNumDelete,
       "wfSwservInPhoneNumIndex": wfSwservInPhoneNumIndex,
       "wfSwservInPhoneNumRmtStationNum": wfSwservInPhoneNumRmtStationNum,
       "wfSwservInPhoneNumSubAddr": wfSwservInPhoneNumSubAddr,
       "wfSwservInPhoneNumDelimiter": wfSwservInPhoneNumDelimiter,
       "wfSwservInPhoneNumType": wfSwservInPhoneNumType,
       "wfSwservInPhoneNumTypeofNum": wfSwservInPhoneNumTypeofNum,
       "wfSwservInPhoneNumPlan": wfSwservInPhoneNumPlan,
       "wfSwservInPhoneNumCct": wfSwservInPhoneNumCct,
       "wfCctOptsBrBuPppFilterTable": wfCctOptsBrBuPppFilterTable,
       "wfCctOptsBrBuPppFilterEntry": wfCctOptsBrBuPppFilterEntry,
       "wfCctOptsBrBuPppFilterCreate": wfCctOptsBrBuPppFilterCreate,
       "wfCctOptsBrBuPppFilterEnable": wfCctOptsBrBuPppFilterEnable,
       "wfCctOptsBrBuPppFilterState": wfCctOptsBrBuPppFilterState,
       "wfCctOptsBrBuPppFilterCounter": wfCctOptsBrBuPppFilterCounter,
       "wfCctOptsBrBuPppFilterDefinition": wfCctOptsBrBuPppFilterDefinition,
       "wfCctOptsBrBuPppFilterReserved": wfCctOptsBrBuPppFilterReserved,
       "wfCctOptsBrBuPppFilterCct": wfCctOptsBrBuPppFilterCct,
       "wfCctOptsBrBuPppFilterRuleNumber": wfCctOptsBrBuPppFilterRuleNumber,
       "wfCctOptsBrBuPppFilterFragment": wfCctOptsBrBuPppFilterFragment,
       "wfCctOptsBrBuPppFilterName": wfCctOptsBrBuPppFilterName,
       "wfCctOptsIpBuPppFilterTable": wfCctOptsIpBuPppFilterTable,
       "wfCctOptsIpBuPppFilterEntry": wfCctOptsIpBuPppFilterEntry,
       "wfCctOptsIpBuPppFilterCreate": wfCctOptsIpBuPppFilterCreate,
       "wfCctOptsIpBuPppFilterEnable": wfCctOptsIpBuPppFilterEnable,
       "wfCctOptsIpBuPppFilterState": wfCctOptsIpBuPppFilterState,
       "wfCctOptsIpBuPppFilterCounter": wfCctOptsIpBuPppFilterCounter,
       "wfCctOptsIpBuPppFilterDefinition": wfCctOptsIpBuPppFilterDefinition,
       "wfCctOptsIpBuPppFilterReserved": wfCctOptsIpBuPppFilterReserved,
       "wfCctOptsIpBuPppFilterCct": wfCctOptsIpBuPppFilterCct,
       "wfCctOptsIpBuPppFilterRuleNumber": wfCctOptsIpBuPppFilterRuleNumber,
       "wfCctOptsIpBuPppFilterFragment": wfCctOptsIpBuPppFilterFragment,
       "wfCctOptsIpBuPppFilterName": wfCctOptsIpBuPppFilterName,
       "wfCctOptsCngcTable": wfCctOptsCngcTable,
       "wfCctOptsCngcEntry": wfCctOptsCngcEntry,
       "wfCctOptsCngcDelete": wfCctOptsCngcDelete,
       "wfCctOptsCngcDisable": wfCctOptsCngcDisable,
       "wfCctOptsCngcCct": wfCctOptsCngcCct,
       "wfCctOptsCngcSmdsDiscardability": wfCctOptsCngcSmdsDiscardability,
       "wfCctOptsCngcCfgSwtxqThreshold": wfCctOptsCngcCfgSwtxqThreshold,
       "wfCctOptsCngcSwtxqThreshold": wfCctOptsCngcSwtxqThreshold,
       "wfCctOptsCngcCngLevel0Threshold": wfCctOptsCngcCngLevel0Threshold,
       "wfCctOptsCngcCngLevel1Threshold": wfCctOptsCngcCngLevel1Threshold,
       "wfCctOptsCngcCngLevel2Threshold": wfCctOptsCngcCngLevel2Threshold,
       "wfCctOptsCngcLinkType": wfCctOptsCngcLinkType,
       "wfCctOptsCngcTrfPriorityEnable": wfCctOptsCngcTrfPriorityEnable,
       "wfCctOptsCngcPortIPTrfPriority": wfCctOptsCngcPortIPTrfPriority,
       "wfCctOptsCngcPortTrfDiscardLvl": wfCctOptsCngcPortTrfDiscardLvl,
       "wfCctOptsCngcPortTrfPriority": wfCctOptsCngcPortTrfPriority,
       "wfCctOptsCngcCfgHwtxQThreshold": wfCctOptsCngcCfgHwtxQThreshold,
       "wfCctOptsCngcHwtxQThreshold": wfCctOptsCngcHwtxQThreshold,
       "wfCctOptsCngcSndTrapForPktsDropped": wfCctOptsCngcSndTrapForPktsDropped,
       "wfCctOptsCngcCfgQp0Threshold": wfCctOptsCngcCfgQp0Threshold,
       "wfCctOptsCngcQp0Threshold": wfCctOptsCngcQp0Threshold,
       "wfCctOptsCngcQp0CngLvl0Threshold": wfCctOptsCngcQp0CngLvl0Threshold,
       "wfCctOptsCngcQp0CngLvl1Threshold": wfCctOptsCngcQp0CngLvl1Threshold,
       "wfCctOptsCngcQp0CngLvl2Threshold": wfCctOptsCngcQp0CngLvl2Threshold,
       "wfCctOptsCngcQp0PktsServPriNxtQ": wfCctOptsCngcQp0PktsServPriNxtQ,
       "wfCctOptsCngcCfgQp1Threshold": wfCctOptsCngcCfgQp1Threshold,
       "wfCctOptsCngcQp1Threshold": wfCctOptsCngcQp1Threshold,
       "wfCctOptsCngcQp1CngLvl0Threshold": wfCctOptsCngcQp1CngLvl0Threshold,
       "wfCctOptsCngcQp1CngLvl1Threshold": wfCctOptsCngcQp1CngLvl1Threshold,
       "wfCctOptsCngcQp1CngLvl2Threshold": wfCctOptsCngcQp1CngLvl2Threshold,
       "wfCctOptsCngcQp1PktsServPriNxtQ": wfCctOptsCngcQp1PktsServPriNxtQ,
       "wfCctOptsCngcCfgQp2Threshold": wfCctOptsCngcCfgQp2Threshold,
       "wfCctOptsCngcQp2Threshold": wfCctOptsCngcQp2Threshold,
       "wfCctOptsCngcQp2CngLvl0Threshold": wfCctOptsCngcQp2CngLvl0Threshold,
       "wfCctOptsCngcQp2CngLvl1Threshold": wfCctOptsCngcQp2CngLvl1Threshold,
       "wfCctOptsCngcQp2CngLvl2Threshold": wfCctOptsCngcQp2CngLvl2Threshold,
       "wfCctOptsCngcQp2PktsServPriNxtQ": wfCctOptsCngcQp2PktsServPriNxtQ,
       "wfCctOptsCngcCfgQp3Threshold": wfCctOptsCngcCfgQp3Threshold,
       "wfCctOptsCngcQp3Threshold": wfCctOptsCngcQp3Threshold,
       "wfCctOptsCngcQp3CngLvl0Threshold": wfCctOptsCngcQp3CngLvl0Threshold,
       "wfCctOptsCngcQp3CngLvl1Threshold": wfCctOptsCngcQp3CngLvl1Threshold,
       "wfCctOptsCngcQp3CngLvl2Threshold": wfCctOptsCngcQp3CngLvl2Threshold,
       "wfCctOptsCngcPriority0TxPkts": wfCctOptsCngcPriority0TxPkts,
       "wfCctOptsCngcPriority0TxOctets": wfCctOptsCngcPriority0TxOctets,
       "wfCctOptsCngcPriority0DropPkts": wfCctOptsCngcPriority0DropPkts,
       "wfCctOptsCngcPriority0DropOctets": wfCctOptsCngcPriority0DropOctets,
       "wfCctOptsCngcPriority1TxPkts": wfCctOptsCngcPriority1TxPkts,
       "wfCctOptsCngcPriority1TxOctets": wfCctOptsCngcPriority1TxOctets,
       "wfCctOptsCngcPriority1DropPkts": wfCctOptsCngcPriority1DropPkts,
       "wfCctOptsCngcPriority1DropOctets": wfCctOptsCngcPriority1DropOctets,
       "wfCctOptsCngcPriority2TxPkts": wfCctOptsCngcPriority2TxPkts,
       "wfCctOptsCngcPriority2TxOctets": wfCctOptsCngcPriority2TxOctets,
       "wfCctOptsCngcPriority2DropPkts": wfCctOptsCngcPriority2DropPkts,
       "wfCctOptsCngcPriority2DropOctets": wfCctOptsCngcPriority2DropOctets,
       "wfCctOptsCngcPriority3TxPkts": wfCctOptsCngcPriority3TxPkts,
       "wfCctOptsCngcPriority3TxOctets": wfCctOptsCngcPriority3TxOctets,
       "wfCctOptsCngcPriority3DropPkts": wfCctOptsCngcPriority3DropPkts,
       "wfCctOptsCngcPriority3DropOctets": wfCctOptsCngcPriority3DropOctets,
       "wfCctOptsCngcTxFRNonDePkts": wfCctOptsCngcTxFRNonDePkts,
       "wfCctOptsCngcTxFRNonDeOctets": wfCctOptsCngcTxFRNonDeOctets,
       "wfCctOptsCngcTxFRDePkts": wfCctOptsCngcTxFRDePkts,
       "wfCctOptsCngcTxFRDeOctets": wfCctOptsCngcTxFRDeOctets,
       "wfCctOptsCngcDropFRNonDePkts": wfCctOptsCngcDropFRNonDePkts,
       "wfCctOptsCngcDropFRNonDeOctets": wfCctOptsCngcDropFRNonDeOctets,
       "wfCctOptsCngcDropFRDePkts": wfCctOptsCngcDropFRDePkts,
       "wfCctOptsCngcDropFRDeOctets": wfCctOptsCngcDropFRDeOctets,
       "wfCctOptsCngcFRSetFecnPkts": wfCctOptsCngcFRSetFecnPkts,
       "wfCctOptsCngcFRSetFecnOctets": wfCctOptsCngcFRSetFecnOctets,
       "wfCctOptsCngcFRSetBecnPkts": wfCctOptsCngcFRSetBecnPkts,
       "wfCctOptsCngcFRSetBecnOctets": wfCctOptsCngcFRSetBecnOctets,
       "wfCctOptsCngcDropNonFRPkts": wfCctOptsCngcDropNonFRPkts,
       "wfCctOptsCngcDropNonFROctets": wfCctOptsCngcDropNonFROctets,
       "wfCctOptsCngcLogPower": wfCctOptsCngcLogPower,
       "wfSwservTODTable": wfSwservTODTable,
       "wfSwservTODEntry": wfSwservTODEntry,
       "wfSwservTODDelete": wfSwservTODDelete,
       "wfSwservTODCct": wfSwservTODCct,
       "wfSwservTODIndex": wfSwservTODIndex,
       "wfSwservTODType": wfSwservTODType,
       "wfSwservTODStartTime": wfSwservTODStartTime,
       "wfSwservTODEndTime": wfSwservTODEndTime,
       "wfSwservTODInactivityEnable": wfSwservTODInactivityEnable,
       "wfSwservTODAvailabilityMode": wfSwservTODAvailabilityMode,
       "wfSwservTODStandbyFailBackMode": wfSwservTODStandbyFailBackMode,
       "wfSwservTODStandbyFailBackTime": wfSwservTODStandbyFailBackTime,
       "wfDemandCctGrpTable": wfDemandCctGrpTable,
       "wfDemandCctGrpEntry": wfDemandCctGrpEntry,
       "wfDmdCctGroupDelete": wfDmdCctGroupDelete,
       "wfDmdCctGroupNum": wfDmdCctGroupNum,
       "wfDmdCctGroupPoolId": wfDmdCctGroupPoolId,
       "wfDmdCctGroupNumofCcts": wfDmdCctGroupNumofCcts,
       "wfDmdCctGroupIPEnable": wfDmdCctGroupIPEnable,
       "wfDmdCctGroupIPUnnumAssoc": wfDmdCctGroupIPUnnumAssoc,
       "wfDmdCctGroupRIPEnable": wfDmdCctGroupRIPEnable,
       "wfDmdCctGroupOSPFEnable": wfDmdCctGroupOSPFEnable,
       "wfDmdCctGroupIPXEnable": wfDmdCctGroupIPXEnable,
       "wfDmdCctGroupBridgeEnable": wfDmdCctGroupBridgeEnable,
       "wfDmdCctGroupCctList": wfDmdCctGroupCctList,
       "wfDmdCctGroupIPXRouting": wfDmdCctGroupIPXRouting,
       "wfDmdCctGroupIPXWANEnable": wfDmdCctGroupIPXWANEnable,
       "wfDmdCctGroupRadiusEnable": wfDmdCctGroupRadiusEnable}
)
