# SNMP MIB module (CISCO-SEU-MITIGATION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-SEU-MITIGATION-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:08:13 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(EntPhysicalIndexOrZero,) = mibBuilder.importSymbols(
    "CISCO-TC",
    "EntPhysicalIndexOrZero")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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

(DateAndTime,
 DisplayString,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoSeuMitigationMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 701)
)
ciscoSeuMitigationMIB.setRevisions(
        ("2009-06-24 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoSeuMitigationMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoSeuMitigationMIBNotifs = _CiscoSeuMitigationMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 701, 0)
)
_CiscoSeuMitigationMIBObjects_ObjectIdentity = ObjectIdentity
ciscoSeuMitigationMIBObjects = _CiscoSeuMitigationMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 701, 1)
)
_CsmScrubTable_Object = MibTable
csmScrubTable = _CsmScrubTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 701, 1, 1)
)
if mibBuilder.loadTexts:
    csmScrubTable.setStatus("current")
_CsmScrubEntry_Object = MibTableRow
csmScrubEntry = _CsmScrubEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 701, 1, 1, 1)
)
csmScrubEntry.setIndexNames(
    (0, "CISCO-SEU-MITIGATION-MIB", "csmScrubIndex"),
)
if mibBuilder.loadTexts:
    csmScrubEntry.setStatus("current")


class _CsmScrubIndex_Type(Unsigned32):
    """Custom type csmScrubIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_CsmScrubIndex_Type.__name__ = "Unsigned32"
_CsmScrubIndex_Object = MibTableColumn
csmScrubIndex = _CsmScrubIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 701, 1, 1, 1, 1),
    _CsmScrubIndex_Type()
)
csmScrubIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csmScrubIndex.setStatus("current")
_CsmScrubEntPhysicalIndex_Type = EntPhysicalIndexOrZero
_CsmScrubEntPhysicalIndex_Object = MibTableColumn
csmScrubEntPhysicalIndex = _CsmScrubEntPhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 701, 1, 1, 1, 2),
    _CsmScrubEntPhysicalIndex_Type()
)
csmScrubEntPhysicalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csmScrubEntPhysicalIndex.setStatus("current")
_CsmScrubScrubName_Type = DisplayString
_CsmScrubScrubName_Object = MibTableColumn
csmScrubScrubName = _CsmScrubScrubName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 701, 1, 1, 1, 3),
    _CsmScrubScrubName_Type()
)
csmScrubScrubName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csmScrubScrubName.setStatus("current")
_CsmScrubRateAdaptive_Type = TruthValue
_CsmScrubRateAdaptive_Object = MibTableColumn
csmScrubRateAdaptive = _CsmScrubRateAdaptive_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 701, 1, 1, 1, 4),
    _CsmScrubRateAdaptive_Type()
)
csmScrubRateAdaptive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csmScrubRateAdaptive.setStatus("current")
_CsmScrubAlgorithmEnabled_Type = TruthValue
_CsmScrubAlgorithmEnabled_Object = MibTableColumn
csmScrubAlgorithmEnabled = _CsmScrubAlgorithmEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 701, 1, 1, 1, 5),
    _CsmScrubAlgorithmEnabled_Type()
)
csmScrubAlgorithmEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csmScrubAlgorithmEnabled.setStatus("current")


class _CsmScrubRunInterval_Type(Unsigned32):
    """Custom type csmScrubRunInterval based on Unsigned32"""
    defaultValue = 60


_CsmScrubRunInterval_Object = MibTableColumn
csmScrubRunInterval = _CsmScrubRunInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 701, 1, 1, 1, 6),
    _CsmScrubRunInterval_Type()
)
csmScrubRunInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csmScrubRunInterval.setStatus("current")


class _CsmScrubRunIntervalUnits_Type(DisplayString):
    """Custom type csmScrubRunIntervalUnits based on DisplayString"""
    defaultValue = OctetString("Minutes")


_CsmScrubRunIntervalUnits_Object = MibTableColumn
csmScrubRunIntervalUnits = _CsmScrubRunIntervalUnits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 701, 1, 1, 1, 7),
    _CsmScrubRunIntervalUnits_Type()
)
csmScrubRunIntervalUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csmScrubRunIntervalUnits.setStatus("current")


class _CsmScrubDeltaInterval_Type(Unsigned32):
    """Custom type csmScrubDeltaInterval based on Unsigned32"""
    defaultValue = 10


_CsmScrubDeltaInterval_Object = MibTableColumn
csmScrubDeltaInterval = _CsmScrubDeltaInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 701, 1, 1, 1, 8),
    _CsmScrubDeltaInterval_Type()
)
csmScrubDeltaInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csmScrubDeltaInterval.setStatus("current")


class _CsmScrubDeltaIntervalUnits_Type(DisplayString):
    """Custom type csmScrubDeltaIntervalUnits based on DisplayString"""
    defaultValue = OctetString("Minutes")


_CsmScrubDeltaIntervalUnits_Object = MibTableColumn
csmScrubDeltaIntervalUnits = _CsmScrubDeltaIntervalUnits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 701, 1, 1, 1, 9),
    _CsmScrubDeltaIntervalUnits_Type()
)
csmScrubDeltaIntervalUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csmScrubDeltaIntervalUnits.setStatus("current")


class _CsmScrubRetryInterval_Type(Unsigned32):
    """Custom type csmScrubRetryInterval based on Unsigned32"""
    defaultValue = 10


_CsmScrubRetryInterval_Object = MibTableColumn
csmScrubRetryInterval = _CsmScrubRetryInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 701, 1, 1, 1, 10),
    _CsmScrubRetryInterval_Type()
)
csmScrubRetryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csmScrubRetryInterval.setStatus("current")


class _CsmScrubRetryIntervalUnits_Type(DisplayString):
    """Custom type csmScrubRetryIntervalUnits based on DisplayString"""
    defaultValue = OctetString("Minutes")


_CsmScrubRetryIntervalUnits_Object = MibTableColumn
csmScrubRetryIntervalUnits = _CsmScrubRetryIntervalUnits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 701, 1, 1, 1, 11),
    _CsmScrubRetryIntervalUnits_Type()
)
csmScrubRetryIntervalUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csmScrubRetryIntervalUnits.setStatus("current")
_CsmScrubCurrentInterval_Type = Unsigned32
_CsmScrubCurrentInterval_Object = MibTableColumn
csmScrubCurrentInterval = _CsmScrubCurrentInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 701, 1, 1, 1, 12),
    _CsmScrubCurrentInterval_Type()
)
csmScrubCurrentInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csmScrubCurrentInterval.setStatus("current")
_CsmScrubCurrentIntervalUnits_Type = DisplayString
_CsmScrubCurrentIntervalUnits_Object = MibTableColumn
csmScrubCurrentIntervalUnits = _CsmScrubCurrentIntervalUnits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 701, 1, 1, 1, 13),
    _CsmScrubCurrentIntervalUnits_Type()
)
csmScrubCurrentIntervalUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csmScrubCurrentIntervalUnits.setStatus("current")


class _CsmScrubThresholdInterval_Type(Unsigned32):
    """Custom type csmScrubThresholdInterval based on Unsigned32"""
    defaultValue = 60


_CsmScrubThresholdInterval_Object = MibTableColumn
csmScrubThresholdInterval = _CsmScrubThresholdInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 701, 1, 1, 1, 14),
    _CsmScrubThresholdInterval_Type()
)
csmScrubThresholdInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csmScrubThresholdInterval.setStatus("current")


class _CsmScrubThresholdIntervalUnits_Type(DisplayString):
    """Custom type csmScrubThresholdIntervalUnits based on DisplayString"""
    defaultValue = OctetString("Minutes")


_CsmScrubThresholdIntervalUnits_Object = MibTableColumn
csmScrubThresholdIntervalUnits = _CsmScrubThresholdIntervalUnits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 701, 1, 1, 1, 15),
    _CsmScrubThresholdIntervalUnits_Type()
)
csmScrubThresholdIntervalUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csmScrubThresholdIntervalUnits.setStatus("current")


class _CsmScrubThresholdIntervalCount_Type(Unsigned32):
    """Custom type csmScrubThresholdIntervalCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_CsmScrubThresholdIntervalCount_Type.__name__ = "Unsigned32"
_CsmScrubThresholdIntervalCount_Object = MibTableColumn
csmScrubThresholdIntervalCount = _CsmScrubThresholdIntervalCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 701, 1, 1, 1, 16),
    _CsmScrubThresholdIntervalCount_Type()
)
csmScrubThresholdIntervalCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csmScrubThresholdIntervalCount.setStatus("current")


class _CsmScrubThresholdErrorValue_Type(Unsigned32):
    """Custom type csmScrubThresholdErrorValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_CsmScrubThresholdErrorValue_Type.__name__ = "Unsigned32"
_CsmScrubThresholdErrorValue_Object = MibTableColumn
csmScrubThresholdErrorValue = _CsmScrubThresholdErrorValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 701, 1, 1, 1, 17),
    _CsmScrubThresholdErrorValue_Type()
)
csmScrubThresholdErrorValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csmScrubThresholdErrorValue.setStatus("current")
_CsmScrubRunning_Type = TruthValue
_CsmScrubRunning_Object = MibTableColumn
csmScrubRunning = _CsmScrubRunning_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 701, 1, 1, 1, 18),
    _CsmScrubRunning_Type()
)
csmScrubRunning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csmScrubRunning.setStatus("current")


class _CsmScrubStatus_Type(Integer32):
    """Custom type csmScrubStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("decreased", 2),
          ("elevated", 1),
          ("normal", 3))
    )


_CsmScrubStatus_Type.__name__ = "Integer32"
_CsmScrubStatus_Object = MibTableColumn
csmScrubStatus = _CsmScrubStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 701, 1, 1, 1, 19),
    _CsmScrubStatus_Type()
)
csmScrubStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csmScrubStatus.setStatus("current")
_CsmScrubLastRun_Type = DateAndTime
_CsmScrubLastRun_Object = MibTableColumn
csmScrubLastRun = _CsmScrubLastRun_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 701, 1, 1, 1, 20),
    _CsmScrubLastRun_Type()
)
csmScrubLastRun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csmScrubLastRun.setStatus("current")
_CsmScrubPassesCompleted_Type = Unsigned32
_CsmScrubPassesCompleted_Object = MibTableColumn
csmScrubPassesCompleted = _CsmScrubPassesCompleted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 701, 1, 1, 1, 21),
    _CsmScrubPassesCompleted_Type()
)
csmScrubPassesCompleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csmScrubPassesCompleted.setStatus("current")
_CsmScrubErrorsTable_Object = MibTable
csmScrubErrorsTable = _CsmScrubErrorsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 701, 1, 2)
)
if mibBuilder.loadTexts:
    csmScrubErrorsTable.setStatus("current")
_CsmScrubErrorsEntry_Object = MibTableRow
csmScrubErrorsEntry = _CsmScrubErrorsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 701, 1, 2, 1)
)
csmScrubErrorsEntry.setIndexNames(
    (0, "CISCO-SEU-MITIGATION-MIB", "csmScrubErrorsIndex"),
)
if mibBuilder.loadTexts:
    csmScrubErrorsEntry.setStatus("current")


class _CsmScrubErrorsIndex_Type(Unsigned32):
    """Custom type csmScrubErrorsIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_CsmScrubErrorsIndex_Type.__name__ = "Unsigned32"
_CsmScrubErrorsIndex_Object = MibTableColumn
csmScrubErrorsIndex = _CsmScrubErrorsIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 701, 1, 2, 1, 1),
    _CsmScrubErrorsIndex_Type()
)
csmScrubErrorsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csmScrubErrorsIndex.setStatus("current")
_CsmScrubErrorsEntPhysicalIndex_Type = EntPhysicalIndexOrZero
_CsmScrubErrorsEntPhysicalIndex_Object = MibTableColumn
csmScrubErrorsEntPhysicalIndex = _CsmScrubErrorsEntPhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 701, 1, 2, 1, 2),
    _CsmScrubErrorsEntPhysicalIndex_Type()
)
csmScrubErrorsEntPhysicalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csmScrubErrorsEntPhysicalIndex.setStatus("current")
_CsmScrubErrorsDescription_Type = DisplayString
_CsmScrubErrorsDescription_Object = MibTableColumn
csmScrubErrorsDescription = _CsmScrubErrorsDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 701, 1, 2, 1, 3),
    _CsmScrubErrorsDescription_Type()
)
csmScrubErrorsDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csmScrubErrorsDescription.setStatus("current")
_CsmScrubErrorsReference_Type = DisplayString
_CsmScrubErrorsReference_Object = MibTableColumn
csmScrubErrorsReference = _CsmScrubErrorsReference_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 701, 1, 2, 1, 4),
    _CsmScrubErrorsReference_Type()
)
csmScrubErrorsReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csmScrubErrorsReference.setStatus("current")
_CsmScrubErrorsSingleBit_Type = Counter32
_CsmScrubErrorsSingleBit_Object = MibTableColumn
csmScrubErrorsSingleBit = _CsmScrubErrorsSingleBit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 701, 1, 2, 1, 5),
    _CsmScrubErrorsSingleBit_Type()
)
csmScrubErrorsSingleBit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csmScrubErrorsSingleBit.setStatus("current")
_CsmScrubErrorsSingleBitInterrupts_Type = Counter32
_CsmScrubErrorsSingleBitInterrupts_Object = MibTableColumn
csmScrubErrorsSingleBitInterrupts = _CsmScrubErrorsSingleBitInterrupts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 701, 1, 2, 1, 6),
    _CsmScrubErrorsSingleBitInterrupts_Type()
)
csmScrubErrorsSingleBitInterrupts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csmScrubErrorsSingleBitInterrupts.setStatus("current")
_CsmScrubErrorsMultibit_Type = Counter32
_CsmScrubErrorsMultibit_Object = MibTableColumn
csmScrubErrorsMultibit = _CsmScrubErrorsMultibit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 701, 1, 2, 1, 7),
    _CsmScrubErrorsMultibit_Type()
)
csmScrubErrorsMultibit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csmScrubErrorsMultibit.setStatus("current")
_CsmScrubErrorsMultibitInterrupts_Type = Counter32
_CsmScrubErrorsMultibitInterrupts_Object = MibTableColumn
csmScrubErrorsMultibitInterrupts = _CsmScrubErrorsMultibitInterrupts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 701, 1, 2, 1, 8),
    _CsmScrubErrorsMultibitInterrupts_Type()
)
csmScrubErrorsMultibitInterrupts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csmScrubErrorsMultibitInterrupts.setStatus("current")


class _CsmSeuEventLogMaxEntries_Type(Unsigned32):
    """Custom type csmSeuEventLogMaxEntries based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CsmSeuEventLogMaxEntries_Type.__name__ = "Unsigned32"
_CsmSeuEventLogMaxEntries_Object = MibScalar
csmSeuEventLogMaxEntries = _CsmSeuEventLogMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 701, 1, 3),
    _CsmSeuEventLogMaxEntries_Type()
)
csmSeuEventLogMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csmSeuEventLogMaxEntries.setStatus("current")
_CsmSeuEventLogTable_Object = MibTable
csmSeuEventLogTable = _CsmSeuEventLogTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 701, 1, 4)
)
if mibBuilder.loadTexts:
    csmSeuEventLogTable.setStatus("current")
_CsmSeuEventLogEntry_Object = MibTableRow
csmSeuEventLogEntry = _CsmSeuEventLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 701, 1, 4, 1)
)
csmSeuEventLogEntry.setIndexNames(
    (0, "CISCO-SEU-MITIGATION-MIB", "csmSeuEventLogIndex"),
)
if mibBuilder.loadTexts:
    csmSeuEventLogEntry.setStatus("current")
_CsmSeuEventLogIndex_Type = Unsigned32
_CsmSeuEventLogIndex_Object = MibTableColumn
csmSeuEventLogIndex = _CsmSeuEventLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 701, 1, 4, 1, 1),
    _CsmSeuEventLogIndex_Type()
)
csmSeuEventLogIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csmSeuEventLogIndex.setStatus("current")


class _CsmSeuEventLogDescription_Type(DisplayString):
    """Custom type csmSeuEventLogDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 255),
    )


_CsmSeuEventLogDescription_Type.__name__ = "DisplayString"
_CsmSeuEventLogDescription_Object = MibTableColumn
csmSeuEventLogDescription = _CsmSeuEventLogDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 701, 1, 4, 1, 2),
    _CsmSeuEventLogDescription_Type()
)
csmSeuEventLogDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csmSeuEventLogDescription.setStatus("current")
_CsmSeuEventLogReference_Type = DisplayString
_CsmSeuEventLogReference_Object = MibTableColumn
csmSeuEventLogReference = _CsmSeuEventLogReference_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 701, 1, 4, 1, 3),
    _CsmSeuEventLogReference_Type()
)
csmSeuEventLogReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csmSeuEventLogReference.setStatus("current")
_CsmSeuEventLogAddress_Type = DisplayString
_CsmSeuEventLogAddress_Object = MibTableColumn
csmSeuEventLogAddress = _CsmSeuEventLogAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 701, 1, 4, 1, 4),
    _CsmSeuEventLogAddress_Type()
)
csmSeuEventLogAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csmSeuEventLogAddress.setStatus("current")
_CsmSeuEventLogTimeStamp_Type = DateAndTime
_CsmSeuEventLogTimeStamp_Object = MibTableColumn
csmSeuEventLogTimeStamp = _CsmSeuEventLogTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 701, 1, 4, 1, 5),
    _CsmSeuEventLogTimeStamp_Type()
)
csmSeuEventLogTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csmSeuEventLogTimeStamp.setStatus("current")
_CiscoSeuMitigationMIBConform_ObjectIdentity = ObjectIdentity
ciscoSeuMitigationMIBConform = _CiscoSeuMitigationMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 701, 2)
)
_CiscoSeuMitigationMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoSeuMitigationMIBCompliances = _CiscoSeuMitigationMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 701, 2, 1)
)
_CiscoSeuMitigationMIBGroups_ObjectIdentity = ObjectIdentity
ciscoSeuMitigationMIBGroups = _CiscoSeuMitigationMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 701, 2, 2)
)

# Managed Objects groups

ciscoSeuMitigationMIBMainObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 701, 2, 2, 1)
)
ciscoSeuMitigationMIBMainObjectGroup.setObjects(
      *(("CISCO-SEU-MITIGATION-MIB", "csmScrubEntPhysicalIndex"),
        ("CISCO-SEU-MITIGATION-MIB", "csmScrubAlgorithmEnabled"),
        ("CISCO-SEU-MITIGATION-MIB", "csmScrubScrubName"),
        ("CISCO-SEU-MITIGATION-MIB", "csmScrubRateAdaptive"),
        ("CISCO-SEU-MITIGATION-MIB", "csmScrubRunInterval"),
        ("CISCO-SEU-MITIGATION-MIB", "csmScrubRunIntervalUnits"),
        ("CISCO-SEU-MITIGATION-MIB", "csmScrubDeltaInterval"),
        ("CISCO-SEU-MITIGATION-MIB", "csmScrubDeltaIntervalUnits"),
        ("CISCO-SEU-MITIGATION-MIB", "csmScrubRetryInterval"),
        ("CISCO-SEU-MITIGATION-MIB", "csmScrubRetryIntervalUnits"),
        ("CISCO-SEU-MITIGATION-MIB", "csmScrubThresholdInterval"),
        ("CISCO-SEU-MITIGATION-MIB", "csmScrubThresholdIntervalUnits"),
        ("CISCO-SEU-MITIGATION-MIB", "csmScrubCurrentInterval"),
        ("CISCO-SEU-MITIGATION-MIB", "csmScrubCurrentIntervalUnits"),
        ("CISCO-SEU-MITIGATION-MIB", "csmScrubThresholdIntervalCount"),
        ("CISCO-SEU-MITIGATION-MIB", "csmScrubThresholdErrorValue"),
        ("CISCO-SEU-MITIGATION-MIB", "csmScrubRunning"),
        ("CISCO-SEU-MITIGATION-MIB", "csmScrubStatus"),
        ("CISCO-SEU-MITIGATION-MIB", "csmScrubLastRun"),
        ("CISCO-SEU-MITIGATION-MIB", "csmScrubPassesCompleted"),
        ("CISCO-SEU-MITIGATION-MIB", "csmScrubErrorsEntPhysicalIndex"),
        ("CISCO-SEU-MITIGATION-MIB", "csmScrubErrorsDescription"),
        ("CISCO-SEU-MITIGATION-MIB", "csmScrubErrorsReference"),
        ("CISCO-SEU-MITIGATION-MIB", "csmScrubErrorsSingleBit"),
        ("CISCO-SEU-MITIGATION-MIB", "csmScrubErrorsSingleBitInterrupts"),
        ("CISCO-SEU-MITIGATION-MIB", "csmScrubErrorsMultibit"),
        ("CISCO-SEU-MITIGATION-MIB", "csmScrubErrorsMultibitInterrupts"),
        ("CISCO-SEU-MITIGATION-MIB", "csmSeuEventLogMaxEntries"),
        ("CISCO-SEU-MITIGATION-MIB", "csmSeuEventLogDescription"),
        ("CISCO-SEU-MITIGATION-MIB", "csmSeuEventLogReference"),
        ("CISCO-SEU-MITIGATION-MIB", "csmSeuEventLogAddress"),
        ("CISCO-SEU-MITIGATION-MIB", "csmSeuEventLogTimeStamp"))
)
if mibBuilder.loadTexts:
    ciscoSeuMitigationMIBMainObjectGroup.setStatus("current")


# Notification objects

csmSeuScrubAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 701, 0, 1)
)
csmSeuScrubAlert.setObjects(
    ("CISCO-SEU-MITIGATION-MIB", "csmScrubStatus")
)
if mibBuilder.loadTexts:
    csmSeuScrubAlert.setStatus(
        "current"
    )


# Notifications groups

ciscoSeuMitigationMIBNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 701, 2, 2, 2)
)
ciscoSeuMitigationMIBNotificationGroup.setObjects(
    ("CISCO-SEU-MITIGATION-MIB", "csmSeuScrubAlert")
)
if mibBuilder.loadTexts:
    ciscoSeuMitigationMIBNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoSeuMitigationMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 701, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoSeuMitigationMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-SEU-MITIGATION-MIB",
    **{"ciscoSeuMitigationMIB": ciscoSeuMitigationMIB,
       "ciscoSeuMitigationMIBNotifs": ciscoSeuMitigationMIBNotifs,
       "csmSeuScrubAlert": csmSeuScrubAlert,
       "ciscoSeuMitigationMIBObjects": ciscoSeuMitigationMIBObjects,
       "csmScrubTable": csmScrubTable,
       "csmScrubEntry": csmScrubEntry,
       "csmScrubIndex": csmScrubIndex,
       "csmScrubEntPhysicalIndex": csmScrubEntPhysicalIndex,
       "csmScrubScrubName": csmScrubScrubName,
       "csmScrubRateAdaptive": csmScrubRateAdaptive,
       "csmScrubAlgorithmEnabled": csmScrubAlgorithmEnabled,
       "csmScrubRunInterval": csmScrubRunInterval,
       "csmScrubRunIntervalUnits": csmScrubRunIntervalUnits,
       "csmScrubDeltaInterval": csmScrubDeltaInterval,
       "csmScrubDeltaIntervalUnits": csmScrubDeltaIntervalUnits,
       "csmScrubRetryInterval": csmScrubRetryInterval,
       "csmScrubRetryIntervalUnits": csmScrubRetryIntervalUnits,
       "csmScrubCurrentInterval": csmScrubCurrentInterval,
       "csmScrubCurrentIntervalUnits": csmScrubCurrentIntervalUnits,
       "csmScrubThresholdInterval": csmScrubThresholdInterval,
       "csmScrubThresholdIntervalUnits": csmScrubThresholdIntervalUnits,
       "csmScrubThresholdIntervalCount": csmScrubThresholdIntervalCount,
       "csmScrubThresholdErrorValue": csmScrubThresholdErrorValue,
       "csmScrubRunning": csmScrubRunning,
       "csmScrubStatus": csmScrubStatus,
       "csmScrubLastRun": csmScrubLastRun,
       "csmScrubPassesCompleted": csmScrubPassesCompleted,
       "csmScrubErrorsTable": csmScrubErrorsTable,
       "csmScrubErrorsEntry": csmScrubErrorsEntry,
       "csmScrubErrorsIndex": csmScrubErrorsIndex,
       "csmScrubErrorsEntPhysicalIndex": csmScrubErrorsEntPhysicalIndex,
       "csmScrubErrorsDescription": csmScrubErrorsDescription,
       "csmScrubErrorsReference": csmScrubErrorsReference,
       "csmScrubErrorsSingleBit": csmScrubErrorsSingleBit,
       "csmScrubErrorsSingleBitInterrupts": csmScrubErrorsSingleBitInterrupts,
       "csmScrubErrorsMultibit": csmScrubErrorsMultibit,
       "csmScrubErrorsMultibitInterrupts": csmScrubErrorsMultibitInterrupts,
       "csmSeuEventLogMaxEntries": csmSeuEventLogMaxEntries,
       "csmSeuEventLogTable": csmSeuEventLogTable,
       "csmSeuEventLogEntry": csmSeuEventLogEntry,
       "csmSeuEventLogIndex": csmSeuEventLogIndex,
       "csmSeuEventLogDescription": csmSeuEventLogDescription,
       "csmSeuEventLogReference": csmSeuEventLogReference,
       "csmSeuEventLogAddress": csmSeuEventLogAddress,
       "csmSeuEventLogTimeStamp": csmSeuEventLogTimeStamp,
       "ciscoSeuMitigationMIBConform": ciscoSeuMitigationMIBConform,
       "ciscoSeuMitigationMIBCompliances": ciscoSeuMitigationMIBCompliances,
       "ciscoSeuMitigationMIBCompliance": ciscoSeuMitigationMIBCompliance,
       "ciscoSeuMitigationMIBGroups": ciscoSeuMitigationMIBGroups,
       "ciscoSeuMitigationMIBMainObjectGroup": ciscoSeuMitigationMIBMainObjectGroup,
       "ciscoSeuMitigationMIBNotificationGroup": ciscoSeuMitigationMIBNotificationGroup}
)
