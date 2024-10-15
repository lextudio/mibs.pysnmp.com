# SNMP MIB module (Wellfleet-QOS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-QOS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:16:56 2024
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

(wfServicePkgGroup,) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfServicePkgGroup")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfQosServPkgTable_Object = MibTable
wfQosServPkgTable = _WfQosServPkgTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 1, 1)
)
if mibBuilder.loadTexts:
    wfQosServPkgTable.setStatus("mandatory")
_WfQosServPkgEntry_Object = MibTableRow
wfQosServPkgEntry = _WfQosServPkgEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 1, 1, 1)
)
wfQosServPkgEntry.setIndexNames(
    (0, "Wellfleet-QOS-MIB", "wfQosServPkgIndex"),
)
if mibBuilder.loadTexts:
    wfQosServPkgEntry.setStatus("mandatory")


class _WfQosServPkgDelete_Type(Integer32):
    """Custom type wfQosServPkgDelete based on Integer32"""
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


_WfQosServPkgDelete_Type.__name__ = "Integer32"
_WfQosServPkgDelete_Object = MibTableColumn
wfQosServPkgDelete = _WfQosServPkgDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 1, 1, 1, 1),
    _WfQosServPkgDelete_Type()
)
wfQosServPkgDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfQosServPkgDelete.setStatus("mandatory")
_WfQosServPkgIndex_Type = Integer32
_WfQosServPkgIndex_Object = MibTableColumn
wfQosServPkgIndex = _WfQosServPkgIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 1, 1, 1, 2),
    _WfQosServPkgIndex_Type()
)
wfQosServPkgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfQosServPkgIndex.setStatus("mandatory")
_WfQosServPkgServiceName_Type = DisplayString
_WfQosServPkgServiceName_Object = MibTableColumn
wfQosServPkgServiceName = _WfQosServPkgServiceName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 1, 1, 1, 3),
    _WfQosServPkgServiceName_Type()
)
wfQosServPkgServiceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfQosServPkgServiceName.setStatus("mandatory")


class _WfQosServPkgScheduling_Type(Integer32):
    """Custom type wfQosServPkgScheduling based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("round-robin", 1),
          ("strict-priority", 2))
    )


_WfQosServPkgScheduling_Type.__name__ = "Integer32"
_WfQosServPkgScheduling_Object = MibTableColumn
wfQosServPkgScheduling = _WfQosServPkgScheduling_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 1, 1, 1, 4),
    _WfQosServPkgScheduling_Type()
)
wfQosServPkgScheduling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfQosServPkgScheduling.setStatus("mandatory")
_WfQosServPkgNumQueues_Type = Integer32
_WfQosServPkgNumQueues_Object = MibTableColumn
wfQosServPkgNumQueues = _WfQosServPkgNumQueues_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 1, 1, 1, 5),
    _WfQosServPkgNumQueues_Type()
)
wfQosServPkgNumQueues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfQosServPkgNumQueues.setStatus("mandatory")
_WfQosServPkgNumLines_Type = Integer32
_WfQosServPkgNumLines_Object = MibTableColumn
wfQosServPkgNumLines = _WfQosServPkgNumLines_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 1, 1, 1, 6),
    _WfQosServPkgNumLines_Type()
)
wfQosServPkgNumLines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfQosServPkgNumLines.setStatus("mandatory")
_WfQosServPkgQueCfgTable_Object = MibTable
wfQosServPkgQueCfgTable = _WfQosServPkgQueCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 1, 2)
)
if mibBuilder.loadTexts:
    wfQosServPkgQueCfgTable.setStatus("mandatory")
_WfQosServPkgQueCfgEntry_Object = MibTableRow
wfQosServPkgQueCfgEntry = _WfQosServPkgQueCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 1, 2, 1)
)
wfQosServPkgQueCfgEntry.setIndexNames(
    (0, "Wellfleet-QOS-MIB", "wfQosServPkgQueCfgServiceIndex"),
    (0, "Wellfleet-QOS-MIB", "wfQosServPkgQueCfgQueueIndex"),
)
if mibBuilder.loadTexts:
    wfQosServPkgQueCfgEntry.setStatus("mandatory")


class _WfQosServPkgQueCfgDelete_Type(Integer32):
    """Custom type wfQosServPkgQueCfgDelete based on Integer32"""
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


_WfQosServPkgQueCfgDelete_Type.__name__ = "Integer32"
_WfQosServPkgQueCfgDelete_Object = MibTableColumn
wfQosServPkgQueCfgDelete = _WfQosServPkgQueCfgDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 1, 2, 1, 1),
    _WfQosServPkgQueCfgDelete_Type()
)
wfQosServPkgQueCfgDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfQosServPkgQueCfgDelete.setStatus("mandatory")
_WfQosServPkgQueCfgServiceIndex_Type = Integer32
_WfQosServPkgQueCfgServiceIndex_Object = MibTableColumn
wfQosServPkgQueCfgServiceIndex = _WfQosServPkgQueCfgServiceIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 1, 2, 1, 2),
    _WfQosServPkgQueCfgServiceIndex_Type()
)
wfQosServPkgQueCfgServiceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfQosServPkgQueCfgServiceIndex.setStatus("mandatory")
_WfQosServPkgQueCfgQueueIndex_Type = Integer32
_WfQosServPkgQueCfgQueueIndex_Object = MibTableColumn
wfQosServPkgQueCfgQueueIndex = _WfQosServPkgQueCfgQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 1, 2, 1, 3),
    _WfQosServPkgQueCfgQueueIndex_Type()
)
wfQosServPkgQueCfgQueueIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfQosServPkgQueCfgQueueIndex.setStatus("mandatory")
_WfQosServPkgQueCfgQueueName_Type = DisplayString
_WfQosServPkgQueCfgQueueName_Object = MibTableColumn
wfQosServPkgQueCfgQueueName = _WfQosServPkgQueCfgQueueName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 1, 2, 1, 4),
    _WfQosServPkgQueCfgQueueName_Type()
)
wfQosServPkgQueCfgQueueName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfQosServPkgQueCfgQueueName.setStatus("mandatory")


class _WfQosServPkgQueCfgState_Type(Integer32):
    """Custom type wfQosServPkgQueCfgState based on Integer32"""
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
        *(("misCfg", 3),
          ("up", 1),
          ("waitPkg", 2))
    )


_WfQosServPkgQueCfgState_Type.__name__ = "Integer32"
_WfQosServPkgQueCfgState_Object = MibTableColumn
wfQosServPkgQueCfgState = _WfQosServPkgQueCfgState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 1, 2, 1, 5),
    _WfQosServPkgQueCfgState_Type()
)
wfQosServPkgQueCfgState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfQosServPkgQueCfgState.setStatus("mandatory")


class _WfQosServPkgQueCfgClass_Type(Integer32):
    """Custom type wfQosServPkgQueCfgClass based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WfQosServPkgQueCfgClass_Type.__name__ = "Integer32"
_WfQosServPkgQueCfgClass_Object = MibTableColumn
wfQosServPkgQueCfgClass = _WfQosServPkgQueCfgClass_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 1, 2, 1, 6),
    _WfQosServPkgQueCfgClass_Type()
)
wfQosServPkgQueCfgClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfQosServPkgQueCfgClass.setStatus("mandatory")


class _WfQosServPkgQueCfgAcctRule_Type(Integer32):
    """Custom type wfQosServPkgQueCfgAcctRule based on Integer32"""
    defaultValue = 0


_WfQosServPkgQueCfgAcctRule_Object = MibTableColumn
wfQosServPkgQueCfgAcctRule = _WfQosServPkgQueCfgAcctRule_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 1, 2, 1, 7),
    _WfQosServPkgQueCfgAcctRule_Type()
)
wfQosServPkgQueCfgAcctRule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfQosServPkgQueCfgAcctRule.setStatus("mandatory")


class _WfQosServPkgQueCfgRxCommitInfoRate_Type(Integer32):
    """Custom type wfQosServPkgQueCfgRxCommitInfoRate based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1536),
    )


_WfQosServPkgQueCfgRxCommitInfoRate_Type.__name__ = "Integer32"
_WfQosServPkgQueCfgRxCommitInfoRate_Object = MibTableColumn
wfQosServPkgQueCfgRxCommitInfoRate = _WfQosServPkgQueCfgRxCommitInfoRate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 1, 2, 1, 8),
    _WfQosServPkgQueCfgRxCommitInfoRate_Type()
)
wfQosServPkgQueCfgRxCommitInfoRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfQosServPkgQueCfgRxCommitInfoRate.setStatus("mandatory")


class _WfQosServPkgQueCfgRxBurstRate_Type(Integer32):
    """Custom type wfQosServPkgQueCfgRxBurstRate based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1536),
    )


_WfQosServPkgQueCfgRxBurstRate_Type.__name__ = "Integer32"
_WfQosServPkgQueCfgRxBurstRate_Object = MibTableColumn
wfQosServPkgQueCfgRxBurstRate = _WfQosServPkgQueCfgRxBurstRate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 1, 2, 1, 9),
    _WfQosServPkgQueCfgRxBurstRate_Type()
)
wfQosServPkgQueCfgRxBurstRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfQosServPkgQueCfgRxBurstRate.setStatus("mandatory")


class _WfQosServPkgQueCfgRxBurstSize_Type(Integer32):
    """Custom type wfQosServPkgQueCfgRxBurstSize based on Integer32"""
    defaultValue = 8000


_WfQosServPkgQueCfgRxBurstSize_Object = MibTableColumn
wfQosServPkgQueCfgRxBurstSize = _WfQosServPkgQueCfgRxBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 1, 2, 1, 10),
    _WfQosServPkgQueCfgRxBurstSize_Type()
)
wfQosServPkgQueCfgRxBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfQosServPkgQueCfgRxBurstSize.setStatus("mandatory")


class _WfQosServPkgQueCfgRxBurstAction_Type(Integer32):
    """Custom type wfQosServPkgQueCfgRxBurstAction based on Integer32"""
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
        *(("downgrade", 2),
          ("mark", 3),
          ("mark-downgrade", 4),
          ("none", 1))
    )


_WfQosServPkgQueCfgRxBurstAction_Type.__name__ = "Integer32"
_WfQosServPkgQueCfgRxBurstAction_Object = MibTableColumn
wfQosServPkgQueCfgRxBurstAction = _WfQosServPkgQueCfgRxBurstAction_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 1, 2, 1, 11),
    _WfQosServPkgQueCfgRxBurstAction_Type()
)
wfQosServPkgQueCfgRxBurstAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfQosServPkgQueCfgRxBurstAction.setStatus("mandatory")


class _WfQosServPkgQueCfgTxDropThresh_Type(Integer32):
    """Custom type wfQosServPkgQueCfgTxDropThresh based on Integer32"""
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
        *(("none", 1),
          ("percent-50", 4),
          ("percent-66", 3),
          ("percent-83", 2))
    )


_WfQosServPkgQueCfgTxDropThresh_Type.__name__ = "Integer32"
_WfQosServPkgQueCfgTxDropThresh_Object = MibTableColumn
wfQosServPkgQueCfgTxDropThresh = _WfQosServPkgQueCfgTxDropThresh_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 1, 2, 1, 12),
    _WfQosServPkgQueCfgTxDropThresh_Type()
)
wfQosServPkgQueCfgTxDropThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfQosServPkgQueCfgTxDropThresh.setStatus("mandatory")


class _WfQosServPkgQueCfgTxWeight_Type(Integer32):
    """Custom type wfQosServPkgQueCfgTxWeight based on Integer32"""
    defaultValue = 100


_WfQosServPkgQueCfgTxWeight_Object = MibTableColumn
wfQosServPkgQueCfgTxWeight = _WfQosServPkgQueCfgTxWeight_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 1, 2, 1, 13),
    _WfQosServPkgQueCfgTxWeight_Type()
)
wfQosServPkgQueCfgTxWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfQosServPkgQueCfgTxWeight.setStatus("mandatory")
_WfQosServPkgQueCfgTxActualWeight_Type = DisplayString
_WfQosServPkgQueCfgTxActualWeight_Object = MibTableColumn
wfQosServPkgQueCfgTxActualWeight = _WfQosServPkgQueCfgTxActualWeight_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 1, 2, 1, 14),
    _WfQosServPkgQueCfgTxActualWeight_Type()
)
wfQosServPkgQueCfgTxActualWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfQosServPkgQueCfgTxActualWeight.setStatus("mandatory")
_WfQueueStatTable_Object = MibTable
wfQueueStatTable = _WfQueueStatTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 1, 3)
)
if mibBuilder.loadTexts:
    wfQueueStatTable.setStatus("mandatory")
_WfQueueStatEntry_Object = MibTableRow
wfQueueStatEntry = _WfQueueStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 1, 3, 1)
)
wfQueueStatEntry.setIndexNames(
    (0, "Wellfleet-QOS-MIB", "wfQueueStatPortLineNumber"),
    (0, "Wellfleet-QOS-MIB", "wfQueueStatLineIndex"),
    (0, "Wellfleet-QOS-MIB", "wfQueueStatQueueIndex"),
)
if mibBuilder.loadTexts:
    wfQueueStatEntry.setStatus("mandatory")
_WfQueueStatPortLineNumber_Type = Integer32
_WfQueueStatPortLineNumber_Object = MibTableColumn
wfQueueStatPortLineNumber = _WfQueueStatPortLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 1, 3, 1, 1),
    _WfQueueStatPortLineNumber_Type()
)
wfQueueStatPortLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfQueueStatPortLineNumber.setStatus("mandatory")
_WfQueueStatLineIndex_Type = Integer32
_WfQueueStatLineIndex_Object = MibTableColumn
wfQueueStatLineIndex = _WfQueueStatLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 1, 3, 1, 2),
    _WfQueueStatLineIndex_Type()
)
wfQueueStatLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfQueueStatLineIndex.setStatus("mandatory")
_WfQueueStatQueueIndex_Type = Integer32
_WfQueueStatQueueIndex_Object = MibTableColumn
wfQueueStatQueueIndex = _WfQueueStatQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 1, 3, 1, 3),
    _WfQueueStatQueueIndex_Type()
)
wfQueueStatQueueIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfQueueStatQueueIndex.setStatus("mandatory")
_WfQueueStatTxOctets_Type = Counter32
_WfQueueStatTxOctets_Object = MibTableColumn
wfQueueStatTxOctets = _WfQueueStatTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 1, 3, 1, 4),
    _WfQueueStatTxOctets_Type()
)
wfQueueStatTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfQueueStatTxOctets.setStatus("mandatory")
_WfQueueStatTxPackets_Type = Counter32
_WfQueueStatTxPackets_Object = MibTableColumn
wfQueueStatTxPackets = _WfQueueStatTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 1, 3, 1, 5),
    _WfQueueStatTxPackets_Type()
)
wfQueueStatTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfQueueStatTxPackets.setStatus("mandatory")
_WfQueueStatTxDrops_Type = Counter32
_WfQueueStatTxDrops_Object = MibTableColumn
wfQueueStatTxDrops = _WfQueueStatTxDrops_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 1, 3, 1, 6),
    _WfQueueStatTxDrops_Type()
)
wfQueueStatTxDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfQueueStatTxDrops.setStatus("mandatory")
_WfQueueStatRxBelowCirOctets_Type = Counter32
_WfQueueStatRxBelowCirOctets_Object = MibTableColumn
wfQueueStatRxBelowCirOctets = _WfQueueStatRxBelowCirOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 1, 3, 1, 7),
    _WfQueueStatRxBelowCirOctets_Type()
)
wfQueueStatRxBelowCirOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfQueueStatRxBelowCirOctets.setStatus("mandatory")
_WfQueueStatRxBelowCirPackets_Type = Counter32
_WfQueueStatRxBelowCirPackets_Object = MibTableColumn
wfQueueStatRxBelowCirPackets = _WfQueueStatRxBelowCirPackets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 1, 3, 1, 8),
    _WfQueueStatRxBelowCirPackets_Type()
)
wfQueueStatRxBelowCirPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfQueueStatRxBelowCirPackets.setStatus("mandatory")
_WfQueueStatRxAboveCirOctets_Type = Counter32
_WfQueueStatRxAboveCirOctets_Object = MibTableColumn
wfQueueStatRxAboveCirOctets = _WfQueueStatRxAboveCirOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 1, 3, 1, 9),
    _WfQueueStatRxAboveCirOctets_Type()
)
wfQueueStatRxAboveCirOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfQueueStatRxAboveCirOctets.setStatus("mandatory")
_WfQueueStatRxAboveCirPackets_Type = Counter32
_WfQueueStatRxAboveCirPackets_Object = MibTableColumn
wfQueueStatRxAboveCirPackets = _WfQueueStatRxAboveCirPackets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 1, 3, 1, 10),
    _WfQueueStatRxAboveCirPackets_Type()
)
wfQueueStatRxAboveCirPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfQueueStatRxAboveCirPackets.setStatus("mandatory")
_WfQueueStatRxAboveBrOctets_Type = Counter32
_WfQueueStatRxAboveBrOctets_Object = MibTableColumn
wfQueueStatRxAboveBrOctets = _WfQueueStatRxAboveBrOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 1, 3, 1, 11),
    _WfQueueStatRxAboveBrOctets_Type()
)
wfQueueStatRxAboveBrOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfQueueStatRxAboveBrOctets.setStatus("mandatory")
_WfQueueStatRxAboveBrPackets_Type = Counter32
_WfQueueStatRxAboveBrPackets_Object = MibTableColumn
wfQueueStatRxAboveBrPackets = _WfQueueStatRxAboveBrPackets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 1, 3, 1, 12),
    _WfQueueStatRxAboveBrPackets_Type()
)
wfQueueStatRxAboveBrPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfQueueStatRxAboveBrPackets.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-QOS-MIB",
    **{"wfQosServPkgTable": wfQosServPkgTable,
       "wfQosServPkgEntry": wfQosServPkgEntry,
       "wfQosServPkgDelete": wfQosServPkgDelete,
       "wfQosServPkgIndex": wfQosServPkgIndex,
       "wfQosServPkgServiceName": wfQosServPkgServiceName,
       "wfQosServPkgScheduling": wfQosServPkgScheduling,
       "wfQosServPkgNumQueues": wfQosServPkgNumQueues,
       "wfQosServPkgNumLines": wfQosServPkgNumLines,
       "wfQosServPkgQueCfgTable": wfQosServPkgQueCfgTable,
       "wfQosServPkgQueCfgEntry": wfQosServPkgQueCfgEntry,
       "wfQosServPkgQueCfgDelete": wfQosServPkgQueCfgDelete,
       "wfQosServPkgQueCfgServiceIndex": wfQosServPkgQueCfgServiceIndex,
       "wfQosServPkgQueCfgQueueIndex": wfQosServPkgQueCfgQueueIndex,
       "wfQosServPkgQueCfgQueueName": wfQosServPkgQueCfgQueueName,
       "wfQosServPkgQueCfgState": wfQosServPkgQueCfgState,
       "wfQosServPkgQueCfgClass": wfQosServPkgQueCfgClass,
       "wfQosServPkgQueCfgAcctRule": wfQosServPkgQueCfgAcctRule,
       "wfQosServPkgQueCfgRxCommitInfoRate": wfQosServPkgQueCfgRxCommitInfoRate,
       "wfQosServPkgQueCfgRxBurstRate": wfQosServPkgQueCfgRxBurstRate,
       "wfQosServPkgQueCfgRxBurstSize": wfQosServPkgQueCfgRxBurstSize,
       "wfQosServPkgQueCfgRxBurstAction": wfQosServPkgQueCfgRxBurstAction,
       "wfQosServPkgQueCfgTxDropThresh": wfQosServPkgQueCfgTxDropThresh,
       "wfQosServPkgQueCfgTxWeight": wfQosServPkgQueCfgTxWeight,
       "wfQosServPkgQueCfgTxActualWeight": wfQosServPkgQueCfgTxActualWeight,
       "wfQueueStatTable": wfQueueStatTable,
       "wfQueueStatEntry": wfQueueStatEntry,
       "wfQueueStatPortLineNumber": wfQueueStatPortLineNumber,
       "wfQueueStatLineIndex": wfQueueStatLineIndex,
       "wfQueueStatQueueIndex": wfQueueStatQueueIndex,
       "wfQueueStatTxOctets": wfQueueStatTxOctets,
       "wfQueueStatTxPackets": wfQueueStatTxPackets,
       "wfQueueStatTxDrops": wfQueueStatTxDrops,
       "wfQueueStatRxBelowCirOctets": wfQueueStatRxBelowCirOctets,
       "wfQueueStatRxBelowCirPackets": wfQueueStatRxBelowCirPackets,
       "wfQueueStatRxAboveCirOctets": wfQueueStatRxAboveCirOctets,
       "wfQueueStatRxAboveCirPackets": wfQueueStatRxAboveCirPackets,
       "wfQueueStatRxAboveBrOctets": wfQueueStatRxAboveBrOctets,
       "wfQueueStatRxAboveBrPackets": wfQueueStatRxAboveBrPackets}
)
