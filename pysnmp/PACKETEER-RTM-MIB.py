# SNMP MIB module (PACKETEER-RTM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PACKETEER-RTM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:36:02 2024
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

(classIndex,
 psCommonMib) = mibBuilder.importSymbols(
    "PACKETEER-MIB",
    "classIndex",
    "psCommonMib")

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

(DateAndTime,
 DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PsClassResponseTimes_ObjectIdentity = ObjectIdentity
psClassResponseTimes = _PsClassResponseTimes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 7)
)
_ClassRTMConfigTable_Object = MibTable
classRTMConfigTable = _ClassRTMConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 7, 1)
)
if mibBuilder.loadTexts:
    classRTMConfigTable.setStatus("mandatory")
_ClassRTMConfigEntry_Object = MibTableRow
classRTMConfigEntry = _ClassRTMConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 7, 1, 1)
)
classRTMConfigEntry.setIndexNames(
    (0, "PACKETEER-MIB", "classIndex"),
)
if mibBuilder.loadTexts:
    classRTMConfigEntry.setStatus("mandatory")
_ClassTotalDelayThreshold_Type = Integer32
_ClassTotalDelayThreshold_Object = MibTableColumn
classTotalDelayThreshold = _ClassTotalDelayThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 7, 1, 1, 2),
    _ClassTotalDelayThreshold_Type()
)
classTotalDelayThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    classTotalDelayThreshold.setStatus("mandatory")
_ClassServiceLevelThreshold_Type = Integer32
_ClassServiceLevelThreshold_Object = MibTableColumn
classServiceLevelThreshold = _ClassServiceLevelThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 7, 1, 1, 6),
    _ClassServiceLevelThreshold_Type()
)
classServiceLevelThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    classServiceLevelThreshold.setStatus("mandatory")
_ClassTotalDelayTable_Object = MibTable
classTotalDelayTable = _ClassTotalDelayTable_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 7, 2)
)
if mibBuilder.loadTexts:
    classTotalDelayTable.setStatus("mandatory")
_ClassTotalDelayEntry_Object = MibTableRow
classTotalDelayEntry = _ClassTotalDelayEntry_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 7, 2, 1)
)
classTotalDelayEntry.setIndexNames(
    (0, "PACKETEER-MIB", "classIndex"),
    (0, "PACKETEER-RTM-MIB", "classTotalDelayBucketLimit"),
)
if mibBuilder.loadTexts:
    classTotalDelayEntry.setStatus("mandatory")
_ClassTotalDelayBucketLimit_Type = Integer32
_ClassTotalDelayBucketLimit_Object = MibTableColumn
classTotalDelayBucketLimit = _ClassTotalDelayBucketLimit_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 7, 2, 1, 1),
    _ClassTotalDelayBucketLimit_Type()
)
classTotalDelayBucketLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    classTotalDelayBucketLimit.setStatus("mandatory")
_ClassTotalDelayBucketCount_Type = Counter32
_ClassTotalDelayBucketCount_Object = MibTableColumn
classTotalDelayBucketCount = _ClassTotalDelayBucketCount_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 7, 2, 1, 2),
    _ClassTotalDelayBucketCount_Type()
)
classTotalDelayBucketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    classTotalDelayBucketCount.setStatus("mandatory")
_ClassNetworkDelayTable_Object = MibTable
classNetworkDelayTable = _ClassNetworkDelayTable_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 7, 3)
)
if mibBuilder.loadTexts:
    classNetworkDelayTable.setStatus("mandatory")
_ClassNetworkDelayEntry_Object = MibTableRow
classNetworkDelayEntry = _ClassNetworkDelayEntry_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 7, 3, 1)
)
classNetworkDelayEntry.setIndexNames(
    (0, "PACKETEER-MIB", "classIndex"),
    (0, "PACKETEER-RTM-MIB", "classNetworkDelayBucketLimit"),
)
if mibBuilder.loadTexts:
    classNetworkDelayEntry.setStatus("mandatory")
_ClassNetworkDelayBucketLimit_Type = Integer32
_ClassNetworkDelayBucketLimit_Object = MibTableColumn
classNetworkDelayBucketLimit = _ClassNetworkDelayBucketLimit_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 7, 3, 1, 1),
    _ClassNetworkDelayBucketLimit_Type()
)
classNetworkDelayBucketLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    classNetworkDelayBucketLimit.setStatus("mandatory")
_ClassNetworkDelayBucketCount_Type = Counter32
_ClassNetworkDelayBucketCount_Object = MibTableColumn
classNetworkDelayBucketCount = _ClassNetworkDelayBucketCount_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 7, 3, 1, 2),
    _ClassNetworkDelayBucketCount_Type()
)
classNetworkDelayBucketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    classNetworkDelayBucketCount.setStatus("mandatory")
_ClassServerDelayTable_Object = MibTable
classServerDelayTable = _ClassServerDelayTable_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 7, 4)
)
if mibBuilder.loadTexts:
    classServerDelayTable.setStatus("mandatory")
_ClassServerDelayEntry_Object = MibTableRow
classServerDelayEntry = _ClassServerDelayEntry_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 7, 4, 1)
)
classServerDelayEntry.setIndexNames(
    (0, "PACKETEER-MIB", "classIndex"),
    (0, "PACKETEER-RTM-MIB", "classServerDelayBucketLimit"),
)
if mibBuilder.loadTexts:
    classServerDelayEntry.setStatus("mandatory")
_ClassServerDelayBucketLimit_Type = Integer32
_ClassServerDelayBucketLimit_Object = MibTableColumn
classServerDelayBucketLimit = _ClassServerDelayBucketLimit_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 7, 4, 1, 1),
    _ClassServerDelayBucketLimit_Type()
)
classServerDelayBucketLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    classServerDelayBucketLimit.setStatus("mandatory")
_ClassServerDelayBucketCount_Type = Counter32
_ClassServerDelayBucketCount_Object = MibTableColumn
classServerDelayBucketCount = _ClassServerDelayBucketCount_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 7, 4, 1, 2),
    _ClassServerDelayBucketCount_Type()
)
classServerDelayBucketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    classServerDelayBucketCount.setStatus("mandatory")
_ClassRTMTable_Object = MibTable
classRTMTable = _ClassRTMTable_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 7, 5)
)
if mibBuilder.loadTexts:
    classRTMTable.setStatus("mandatory")
_ClassRTMEntry_Object = MibTableRow
classRTMEntry = _ClassRTMEntry_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 7, 5, 1)
)
classRTMEntry.setIndexNames(
    (0, "PACKETEER-MIB", "classIndex"),
)
if mibBuilder.loadTexts:
    classRTMEntry.setStatus("mandatory")
_ClassTotalDelayMedian_Type = Gauge32
_ClassTotalDelayMedian_Object = MibTableColumn
classTotalDelayMedian = _ClassTotalDelayMedian_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 7, 5, 1, 1),
    _ClassTotalDelayMedian_Type()
)
classTotalDelayMedian.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    classTotalDelayMedian.setStatus("mandatory")
_ClassTotalDelayAverage_Type = Gauge32
_ClassTotalDelayAverage_Object = MibTableColumn
classTotalDelayAverage = _ClassTotalDelayAverage_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 7, 5, 1, 2),
    _ClassTotalDelayAverage_Type()
)
classTotalDelayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    classTotalDelayAverage.setStatus("mandatory")
_ClassTransactionsAboveTotalDelayThreshold_Type = Counter32
_ClassTransactionsAboveTotalDelayThreshold_Object = MibTableColumn
classTransactionsAboveTotalDelayThreshold = _ClassTransactionsAboveTotalDelayThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 7, 5, 1, 3),
    _ClassTransactionsAboveTotalDelayThreshold_Type()
)
classTransactionsAboveTotalDelayThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    classTransactionsAboveTotalDelayThreshold.setStatus("mandatory")
_ClassIntervalsAboveServiceLevelThreshold_Type = Counter32
_ClassIntervalsAboveServiceLevelThreshold_Object = MibTableColumn
classIntervalsAboveServiceLevelThreshold = _ClassIntervalsAboveServiceLevelThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 7, 5, 1, 4),
    _ClassIntervalsAboveServiceLevelThreshold_Type()
)
classIntervalsAboveServiceLevelThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    classIntervalsAboveServiceLevelThreshold.setStatus("mandatory")
_ClassLastIntervalAboveServiceLevelThreshold_Type = DateAndTime
_ClassLastIntervalAboveServiceLevelThreshold_Object = MibTableColumn
classLastIntervalAboveServiceLevelThreshold = _ClassLastIntervalAboveServiceLevelThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 7, 5, 1, 5),
    _ClassLastIntervalAboveServiceLevelThreshold_Type()
)
classLastIntervalAboveServiceLevelThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    classLastIntervalAboveServiceLevelThreshold.setStatus("mandatory")
_ClassServerDelayMedian_Type = Gauge32
_ClassServerDelayMedian_Object = MibTableColumn
classServerDelayMedian = _ClassServerDelayMedian_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 7, 5, 1, 6),
    _ClassServerDelayMedian_Type()
)
classServerDelayMedian.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    classServerDelayMedian.setStatus("mandatory")
_ClassServerDelayAverage_Type = Gauge32
_ClassServerDelayAverage_Object = MibTableColumn
classServerDelayAverage = _ClassServerDelayAverage_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 7, 5, 1, 7),
    _ClassServerDelayAverage_Type()
)
classServerDelayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    classServerDelayAverage.setStatus("mandatory")
_ClassNetworkDelayMedian_Type = Gauge32
_ClassNetworkDelayMedian_Object = MibTableColumn
classNetworkDelayMedian = _ClassNetworkDelayMedian_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 7, 5, 1, 11),
    _ClassNetworkDelayMedian_Type()
)
classNetworkDelayMedian.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    classNetworkDelayMedian.setStatus("mandatory")
_ClassNetworkDelayAverage_Type = Gauge32
_ClassNetworkDelayAverage_Object = MibTableColumn
classNetworkDelayAverage = _ClassNetworkDelayAverage_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 7, 5, 1, 12),
    _ClassNetworkDelayAverage_Type()
)
classNetworkDelayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    classNetworkDelayAverage.setStatus("mandatory")
_ClassTransactionBytes_Type = Counter32
_ClassTransactionBytes_Object = MibTableColumn
classTransactionBytes = _ClassTransactionBytes_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 7, 5, 1, 13),
    _ClassTransactionBytes_Type()
)
classTransactionBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    classTransactionBytes.setStatus("mandatory")
_ClassTransactionBytesHi_Type = Counter32
_ClassTransactionBytesHi_Object = MibTableColumn
classTransactionBytesHi = _ClassTransactionBytesHi_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 7, 5, 1, 14),
    _ClassTransactionBytesHi_Type()
)
classTransactionBytesHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    classTransactionBytesHi.setStatus("mandatory")
_ClassRoundTripTime_Type = Counter32
_ClassRoundTripTime_Object = MibTableColumn
classRoundTripTime = _ClassRoundTripTime_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 7, 5, 1, 15),
    _ClassRoundTripTime_Type()
)
classRoundTripTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    classRoundTripTime.setStatus("mandatory")
_ClassRoundTripTimeHi_Type = Counter32
_ClassRoundTripTimeHi_Object = MibTableColumn
classRoundTripTimeHi = _ClassRoundTripTimeHi_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 7, 5, 1, 16),
    _ClassRoundTripTimeHi_Type()
)
classRoundTripTimeHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    classRoundTripTimeHi.setStatus("mandatory")
_ClassTransactionsTotal_Type = Counter32
_ClassTransactionsTotal_Object = MibTableColumn
classTransactionsTotal = _ClassTransactionsTotal_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 7, 5, 1, 17),
    _ClassTransactionsTotal_Type()
)
classTransactionsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    classTransactionsTotal.setStatus("mandatory")
_ClassTotalDelayMsec_Type = Counter32
_ClassTotalDelayMsec_Object = MibTableColumn
classTotalDelayMsec = _ClassTotalDelayMsec_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 7, 5, 1, 18),
    _ClassTotalDelayMsec_Type()
)
classTotalDelayMsec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    classTotalDelayMsec.setStatus("mandatory")
_ClassTotalDelayMsecHi_Type = Counter32
_ClassTotalDelayMsecHi_Object = MibTableColumn
classTotalDelayMsecHi = _ClassTotalDelayMsecHi_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 7, 5, 1, 19),
    _ClassTotalDelayMsecHi_Type()
)
classTotalDelayMsecHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    classTotalDelayMsecHi.setStatus("mandatory")
_ClassServerDelayMsec_Type = Counter32
_ClassServerDelayMsec_Object = MibTableColumn
classServerDelayMsec = _ClassServerDelayMsec_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 7, 5, 1, 20),
    _ClassServerDelayMsec_Type()
)
classServerDelayMsec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    classServerDelayMsec.setStatus("mandatory")
_ClassServerDelayMsecHi_Type = Counter32
_ClassServerDelayMsecHi_Object = MibTableColumn
classServerDelayMsecHi = _ClassServerDelayMsecHi_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 7, 5, 1, 21),
    _ClassServerDelayMsecHi_Type()
)
classServerDelayMsecHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    classServerDelayMsecHi.setStatus("mandatory")
_ClassNetworkDelayMsec_Type = Counter32
_ClassNetworkDelayMsec_Object = MibTableColumn
classNetworkDelayMsec = _ClassNetworkDelayMsec_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 7, 5, 1, 22),
    _ClassNetworkDelayMsec_Type()
)
classNetworkDelayMsec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    classNetworkDelayMsec.setStatus("mandatory")
_ClassNetworkDelayMsecHi_Type = Counter32
_ClassNetworkDelayMsecHi_Object = MibTableColumn
classNetworkDelayMsecHi = _ClassNetworkDelayMsecHi_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 7, 5, 1, 23),
    _ClassNetworkDelayMsecHi_Type()
)
classNetworkDelayMsecHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    classNetworkDelayMsecHi.setStatus("mandatory")
_ClassWorstServerTable_Object = MibTable
classWorstServerTable = _ClassWorstServerTable_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 7, 6)
)
if mibBuilder.loadTexts:
    classWorstServerTable.setStatus("mandatory")
_ClassWorstServerEntry_Object = MibTableRow
classWorstServerEntry = _ClassWorstServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 7, 6, 1)
)
classWorstServerEntry.setIndexNames(
    (0, "PACKETEER-MIB", "classIndex"),
    (0, "PACKETEER-RTM-MIB", "classWorstServerIndex"),
)
if mibBuilder.loadTexts:
    classWorstServerEntry.setStatus("mandatory")
_ClassWorstServerIndex_Type = Integer32
_ClassWorstServerIndex_Object = MibTableColumn
classWorstServerIndex = _ClassWorstServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 7, 6, 1, 1),
    _ClassWorstServerIndex_Type()
)
classWorstServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    classWorstServerIndex.setStatus("mandatory")
_ClassWorstServerAddress_Type = IpAddress
_ClassWorstServerAddress_Object = MibTableColumn
classWorstServerAddress = _ClassWorstServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 7, 6, 1, 2),
    _ClassWorstServerAddress_Type()
)
classWorstServerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    classWorstServerAddress.setStatus("mandatory")
_ClassWorstServerTransactionCount_Type = Counter32
_ClassWorstServerTransactionCount_Object = MibTableColumn
classWorstServerTransactionCount = _ClassWorstServerTransactionCount_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 7, 6, 1, 3),
    _ClassWorstServerTransactionCount_Type()
)
classWorstServerTransactionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    classWorstServerTransactionCount.setStatus("mandatory")
_ClassWorstClientTable_Object = MibTable
classWorstClientTable = _ClassWorstClientTable_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 7, 7)
)
if mibBuilder.loadTexts:
    classWorstClientTable.setStatus("mandatory")
_ClassWorstClientEntry_Object = MibTableRow
classWorstClientEntry = _ClassWorstClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 7, 7, 1)
)
classWorstClientEntry.setIndexNames(
    (0, "PACKETEER-MIB", "classIndex"),
    (0, "PACKETEER-RTM-MIB", "classWorstClientIndex"),
)
if mibBuilder.loadTexts:
    classWorstClientEntry.setStatus("mandatory")
_ClassWorstClientIndex_Type = Integer32
_ClassWorstClientIndex_Object = MibTableColumn
classWorstClientIndex = _ClassWorstClientIndex_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 7, 7, 1, 1),
    _ClassWorstClientIndex_Type()
)
classWorstClientIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    classWorstClientIndex.setStatus("mandatory")
_ClassWorstClientAddress_Type = IpAddress
_ClassWorstClientAddress_Object = MibTableColumn
classWorstClientAddress = _ClassWorstClientAddress_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 7, 7, 1, 2),
    _ClassWorstClientAddress_Type()
)
classWorstClientAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    classWorstClientAddress.setStatus("mandatory")
_ClassWorstClientTransactionCount_Type = Counter32
_ClassWorstClientTransactionCount_Object = MibTableColumn
classWorstClientTransactionCount = _ClassWorstClientTransactionCount_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 7, 7, 1, 3),
    _ClassWorstClientTransactionCount_Type()
)
classWorstClientTransactionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    classWorstClientTransactionCount.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PACKETEER-RTM-MIB",
    **{"psClassResponseTimes": psClassResponseTimes,
       "classRTMConfigTable": classRTMConfigTable,
       "classRTMConfigEntry": classRTMConfigEntry,
       "classTotalDelayThreshold": classTotalDelayThreshold,
       "classServiceLevelThreshold": classServiceLevelThreshold,
       "classTotalDelayTable": classTotalDelayTable,
       "classTotalDelayEntry": classTotalDelayEntry,
       "classTotalDelayBucketLimit": classTotalDelayBucketLimit,
       "classTotalDelayBucketCount": classTotalDelayBucketCount,
       "classNetworkDelayTable": classNetworkDelayTable,
       "classNetworkDelayEntry": classNetworkDelayEntry,
       "classNetworkDelayBucketLimit": classNetworkDelayBucketLimit,
       "classNetworkDelayBucketCount": classNetworkDelayBucketCount,
       "classServerDelayTable": classServerDelayTable,
       "classServerDelayEntry": classServerDelayEntry,
       "classServerDelayBucketLimit": classServerDelayBucketLimit,
       "classServerDelayBucketCount": classServerDelayBucketCount,
       "classRTMTable": classRTMTable,
       "classRTMEntry": classRTMEntry,
       "classTotalDelayMedian": classTotalDelayMedian,
       "classTotalDelayAverage": classTotalDelayAverage,
       "classTransactionsAboveTotalDelayThreshold": classTransactionsAboveTotalDelayThreshold,
       "classIntervalsAboveServiceLevelThreshold": classIntervalsAboveServiceLevelThreshold,
       "classLastIntervalAboveServiceLevelThreshold": classLastIntervalAboveServiceLevelThreshold,
       "classServerDelayMedian": classServerDelayMedian,
       "classServerDelayAverage": classServerDelayAverage,
       "classNetworkDelayMedian": classNetworkDelayMedian,
       "classNetworkDelayAverage": classNetworkDelayAverage,
       "classTransactionBytes": classTransactionBytes,
       "classTransactionBytesHi": classTransactionBytesHi,
       "classRoundTripTime": classRoundTripTime,
       "classRoundTripTimeHi": classRoundTripTimeHi,
       "classTransactionsTotal": classTransactionsTotal,
       "classTotalDelayMsec": classTotalDelayMsec,
       "classTotalDelayMsecHi": classTotalDelayMsecHi,
       "classServerDelayMsec": classServerDelayMsec,
       "classServerDelayMsecHi": classServerDelayMsecHi,
       "classNetworkDelayMsec": classNetworkDelayMsec,
       "classNetworkDelayMsecHi": classNetworkDelayMsecHi,
       "classWorstServerTable": classWorstServerTable,
       "classWorstServerEntry": classWorstServerEntry,
       "classWorstServerIndex": classWorstServerIndex,
       "classWorstServerAddress": classWorstServerAddress,
       "classWorstServerTransactionCount": classWorstServerTransactionCount,
       "classWorstClientTable": classWorstClientTable,
       "classWorstClientEntry": classWorstClientEntry,
       "classWorstClientIndex": classWorstClientIndex,
       "classWorstClientAddress": classWorstClientAddress,
       "classWorstClientTransactionCount": classWorstClientTransactionCount}
)
