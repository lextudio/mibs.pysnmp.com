# SNMP MIB module (STREAMS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/STREAMS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:58:27 2024
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

streams = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 539, 16, 4)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Aii_ObjectIdentity = ObjectIdentity
aii = _Aii_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539)
)
_AiSLC2_ObjectIdentity = ObjectIdentity
aiSLC2 = _AiSLC2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 16)
)
_StreamsAdmnTable_Object = MibTable
streamsAdmnTable = _StreamsAdmnTable_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 4, 1)
)
if mibBuilder.loadTexts:
    streamsAdmnTable.setStatus("current")
_StreamsAdmnEntry_Object = MibTableRow
streamsAdmnEntry = _StreamsAdmnEntry_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 4, 1, 1)
)
streamsAdmnEntry.setIndexNames(
    (0, "STREAMS-MIB", "streamsAdmnSubsystemIndex"),
)
if mibBuilder.loadTexts:
    streamsAdmnEntry.setStatus("current")
_StreamsAdmnSubsystemIndex_Type = Integer32
_StreamsAdmnSubsystemIndex_Object = MibTableColumn
streamsAdmnSubsystemIndex = _StreamsAdmnSubsystemIndex_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 4, 1, 1, 1),
    _StreamsAdmnSubsystemIndex_Type()
)
streamsAdmnSubsystemIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    streamsAdmnSubsystemIndex.setStatus("current")
_StreamsAdmnMaxStorage_Type = Integer32
_StreamsAdmnMaxStorage_Object = MibTableColumn
streamsAdmnMaxStorage = _StreamsAdmnMaxStorage_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 4, 1, 1, 2),
    _StreamsAdmnMaxStorage_Type()
)
streamsAdmnMaxStorage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    streamsAdmnMaxStorage.setStatus("current")
_StreamsAdmnNumQueues_Type = Integer32
_StreamsAdmnNumQueues_Object = MibTableColumn
streamsAdmnNumQueues = _StreamsAdmnNumQueues_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 4, 1, 1, 3),
    _StreamsAdmnNumQueues_Type()
)
streamsAdmnNumQueues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamsAdmnNumQueues.setStatus("current")
_StreamsAdmnNumStreams_Type = Integer32
_StreamsAdmnNumStreams_Object = MibTableColumn
streamsAdmnNumStreams = _StreamsAdmnNumStreams_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 4, 1, 1, 4),
    _StreamsAdmnNumStreams_Type()
)
streamsAdmnNumStreams.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    streamsAdmnNumStreams.setStatus("current")
_StreamsAdmnNumBufcalls_Type = Integer32
_StreamsAdmnNumBufcalls_Object = MibTableColumn
streamsAdmnNumBufcalls = _StreamsAdmnNumBufcalls_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 4, 1, 1, 5),
    _StreamsAdmnNumBufcalls_Type()
)
streamsAdmnNumBufcalls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    streamsAdmnNumBufcalls.setStatus("current")
_StreamsAdmnNumTimeouts_Type = Integer32
_StreamsAdmnNumTimeouts_Object = MibTableColumn
streamsAdmnNumTimeouts = _StreamsAdmnNumTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 4, 1, 1, 6),
    _StreamsAdmnNumTimeouts_Type()
)
streamsAdmnNumTimeouts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    streamsAdmnNumTimeouts.setStatus("current")
_StreamsAdmnNumMblks_Type = Integer32
_StreamsAdmnNumMblks_Object = MibTableColumn
streamsAdmnNumMblks = _StreamsAdmnNumMblks_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 4, 1, 1, 7),
    _StreamsAdmnNumMblks_Type()
)
streamsAdmnNumMblks.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    streamsAdmnNumMblks.setStatus("current")
_StreamsAdmnNumExtended_Type = Integer32
_StreamsAdmnNumExtended_Object = MibTableColumn
streamsAdmnNumExtended = _StreamsAdmnNumExtended_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 4, 1, 1, 8),
    _StreamsAdmnNumExtended_Type()
)
streamsAdmnNumExtended.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    streamsAdmnNumExtended.setStatus("current")
_StreamsAdmnLoSafetyMark_Type = Integer32
_StreamsAdmnLoSafetyMark_Object = MibTableColumn
streamsAdmnLoSafetyMark = _StreamsAdmnLoSafetyMark_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 4, 1, 1, 9),
    _StreamsAdmnLoSafetyMark_Type()
)
streamsAdmnLoSafetyMark.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    streamsAdmnLoSafetyMark.setStatus("current")
_StreamsAdmnMidSafetyMark_Type = Integer32
_StreamsAdmnMidSafetyMark_Object = MibTableColumn
streamsAdmnMidSafetyMark = _StreamsAdmnMidSafetyMark_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 4, 1, 1, 10),
    _StreamsAdmnMidSafetyMark_Type()
)
streamsAdmnMidSafetyMark.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    streamsAdmnMidSafetyMark.setStatus("current")
_StreamsAdmnNumBufs0_Type = Integer32
_StreamsAdmnNumBufs0_Object = MibTableColumn
streamsAdmnNumBufs0 = _StreamsAdmnNumBufs0_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 4, 1, 1, 11),
    _StreamsAdmnNumBufs0_Type()
)
streamsAdmnNumBufs0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    streamsAdmnNumBufs0.setStatus("current")
_StreamsAdmnNumBufs1_Type = Integer32
_StreamsAdmnNumBufs1_Object = MibTableColumn
streamsAdmnNumBufs1 = _StreamsAdmnNumBufs1_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 4, 1, 1, 12),
    _StreamsAdmnNumBufs1_Type()
)
streamsAdmnNumBufs1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    streamsAdmnNumBufs1.setStatus("current")
_StreamsAdmnNumBufs2_Type = Integer32
_StreamsAdmnNumBufs2_Object = MibTableColumn
streamsAdmnNumBufs2 = _StreamsAdmnNumBufs2_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 4, 1, 1, 13),
    _StreamsAdmnNumBufs2_Type()
)
streamsAdmnNumBufs2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    streamsAdmnNumBufs2.setStatus("current")
_StreamsAdmnNumBufs3_Type = Integer32
_StreamsAdmnNumBufs3_Object = MibTableColumn
streamsAdmnNumBufs3 = _StreamsAdmnNumBufs3_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 4, 1, 1, 14),
    _StreamsAdmnNumBufs3_Type()
)
streamsAdmnNumBufs3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    streamsAdmnNumBufs3.setStatus("current")
_StreamsAdmnNumBufs4_Type = Integer32
_StreamsAdmnNumBufs4_Object = MibTableColumn
streamsAdmnNumBufs4 = _StreamsAdmnNumBufs4_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 4, 1, 1, 15),
    _StreamsAdmnNumBufs4_Type()
)
streamsAdmnNumBufs4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    streamsAdmnNumBufs4.setStatus("current")
_StreamsAdmnNumBufs5_Type = Integer32
_StreamsAdmnNumBufs5_Object = MibTableColumn
streamsAdmnNumBufs5 = _StreamsAdmnNumBufs5_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 4, 1, 1, 16),
    _StreamsAdmnNumBufs5_Type()
)
streamsAdmnNumBufs5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    streamsAdmnNumBufs5.setStatus("current")
_StreamsAdmnNumBufs6_Type = Integer32
_StreamsAdmnNumBufs6_Object = MibTableColumn
streamsAdmnNumBufs6 = _StreamsAdmnNumBufs6_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 4, 1, 1, 17),
    _StreamsAdmnNumBufs6_Type()
)
streamsAdmnNumBufs6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    streamsAdmnNumBufs6.setStatus("current")
_StreamsAdmnNumBufs7_Type = Integer32
_StreamsAdmnNumBufs7_Object = MibTableColumn
streamsAdmnNumBufs7 = _StreamsAdmnNumBufs7_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 4, 1, 1, 18),
    _StreamsAdmnNumBufs7_Type()
)
streamsAdmnNumBufs7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    streamsAdmnNumBufs7.setStatus("current")
_StreamsAdmnNumBufs8_Type = Integer32
_StreamsAdmnNumBufs8_Object = MibTableColumn
streamsAdmnNumBufs8 = _StreamsAdmnNumBufs8_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 4, 1, 1, 19),
    _StreamsAdmnNumBufs8_Type()
)
streamsAdmnNumBufs8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    streamsAdmnNumBufs8.setStatus("current")
_StreamsAdmnNumBufs9_Type = Integer32
_StreamsAdmnNumBufs9_Object = MibTableColumn
streamsAdmnNumBufs9 = _StreamsAdmnNumBufs9_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 4, 1, 1, 20),
    _StreamsAdmnNumBufs9_Type()
)
streamsAdmnNumBufs9.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    streamsAdmnNumBufs9.setStatus("current")
_StreamsAdmnSizeBufs0_Type = Integer32
_StreamsAdmnSizeBufs0_Object = MibTableColumn
streamsAdmnSizeBufs0 = _StreamsAdmnSizeBufs0_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 4, 1, 1, 21),
    _StreamsAdmnSizeBufs0_Type()
)
streamsAdmnSizeBufs0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    streamsAdmnSizeBufs0.setStatus("current")
_StreamsAdmnSizeBufs1_Type = Integer32
_StreamsAdmnSizeBufs1_Object = MibTableColumn
streamsAdmnSizeBufs1 = _StreamsAdmnSizeBufs1_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 4, 1, 1, 22),
    _StreamsAdmnSizeBufs1_Type()
)
streamsAdmnSizeBufs1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    streamsAdmnSizeBufs1.setStatus("current")
_StreamsAdmnSizeBufs2_Type = Integer32
_StreamsAdmnSizeBufs2_Object = MibTableColumn
streamsAdmnSizeBufs2 = _StreamsAdmnSizeBufs2_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 4, 1, 1, 23),
    _StreamsAdmnSizeBufs2_Type()
)
streamsAdmnSizeBufs2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    streamsAdmnSizeBufs2.setStatus("current")
_StreamsAdmnSizeBufs3_Type = Integer32
_StreamsAdmnSizeBufs3_Object = MibTableColumn
streamsAdmnSizeBufs3 = _StreamsAdmnSizeBufs3_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 4, 1, 1, 24),
    _StreamsAdmnSizeBufs3_Type()
)
streamsAdmnSizeBufs3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    streamsAdmnSizeBufs3.setStatus("current")
_StreamsAdmnSizeBufs4_Type = Integer32
_StreamsAdmnSizeBufs4_Object = MibTableColumn
streamsAdmnSizeBufs4 = _StreamsAdmnSizeBufs4_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 4, 1, 1, 25),
    _StreamsAdmnSizeBufs4_Type()
)
streamsAdmnSizeBufs4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    streamsAdmnSizeBufs4.setStatus("current")
_StreamsAdmnSizeBufs5_Type = Integer32
_StreamsAdmnSizeBufs5_Object = MibTableColumn
streamsAdmnSizeBufs5 = _StreamsAdmnSizeBufs5_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 4, 1, 1, 26),
    _StreamsAdmnSizeBufs5_Type()
)
streamsAdmnSizeBufs5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    streamsAdmnSizeBufs5.setStatus("current")
_StreamsAdmnSizeBufs6_Type = Integer32
_StreamsAdmnSizeBufs6_Object = MibTableColumn
streamsAdmnSizeBufs6 = _StreamsAdmnSizeBufs6_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 4, 1, 1, 27),
    _StreamsAdmnSizeBufs6_Type()
)
streamsAdmnSizeBufs6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    streamsAdmnSizeBufs6.setStatus("current")
_StreamsAdmnSizeBufs7_Type = Integer32
_StreamsAdmnSizeBufs7_Object = MibTableColumn
streamsAdmnSizeBufs7 = _StreamsAdmnSizeBufs7_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 4, 1, 1, 28),
    _StreamsAdmnSizeBufs7_Type()
)
streamsAdmnSizeBufs7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    streamsAdmnSizeBufs7.setStatus("current")
_StreamsAdmnSizeBufs8_Type = Integer32
_StreamsAdmnSizeBufs8_Object = MibTableColumn
streamsAdmnSizeBufs8 = _StreamsAdmnSizeBufs8_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 4, 1, 1, 29),
    _StreamsAdmnSizeBufs8_Type()
)
streamsAdmnSizeBufs8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    streamsAdmnSizeBufs8.setStatus("current")
_StreamsAdmnSizeBufs9_Type = Integer32
_StreamsAdmnSizeBufs9_Object = MibTableColumn
streamsAdmnSizeBufs9 = _StreamsAdmnSizeBufs9_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 4, 1, 1, 30),
    _StreamsAdmnSizeBufs9_Type()
)
streamsAdmnSizeBufs9.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    streamsAdmnSizeBufs9.setStatus("current")
_StreamsStatsTable_Object = MibTable
streamsStatsTable = _StreamsStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 4, 2)
)
if mibBuilder.loadTexts:
    streamsStatsTable.setStatus("current")
_StreamsStatsEntry_Object = MibTableRow
streamsStatsEntry = _StreamsStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 4, 2, 1)
)
streamsStatsEntry.setIndexNames(
    (0, "STREAMS-MIB", "streamsStatsSubsystemIndex"),
)
if mibBuilder.loadTexts:
    streamsStatsEntry.setStatus("current")
_StreamsStatsSubsystemIndex_Type = Integer32
_StreamsStatsSubsystemIndex_Object = MibTableColumn
streamsStatsSubsystemIndex = _StreamsStatsSubsystemIndex_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 4, 2, 1, 1),
    _StreamsStatsSubsystemIndex_Type()
)
streamsStatsSubsystemIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamsStatsSubsystemIndex.setStatus("current")
_StreamsStatsAllocStorage_Type = Integer32
_StreamsStatsAllocStorage_Object = MibTableColumn
streamsStatsAllocStorage = _StreamsStatsAllocStorage_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 4, 2, 1, 2),
    _StreamsStatsAllocStorage_Type()
)
streamsStatsAllocStorage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamsStatsAllocStorage.setStatus("current")
_StreamsStatsQueuesConfig_Type = Integer32
_StreamsStatsQueuesConfig_Object = MibTableColumn
streamsStatsQueuesConfig = _StreamsStatsQueuesConfig_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 4, 2, 1, 3),
    _StreamsStatsQueuesConfig_Type()
)
streamsStatsQueuesConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamsStatsQueuesConfig.setStatus("current")
_StreamsStatsQueuesInUse_Type = Integer32
_StreamsStatsQueuesInUse_Object = MibTableColumn
streamsStatsQueuesInUse = _StreamsStatsQueuesInUse_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 4, 2, 1, 4),
    _StreamsStatsQueuesInUse_Type()
)
streamsStatsQueuesInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamsStatsQueuesInUse.setStatus("current")
_StreamsStatsQueuesUsed_Type = Integer32
_StreamsStatsQueuesUsed_Object = MibTableColumn
streamsStatsQueuesUsed = _StreamsStatsQueuesUsed_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 4, 2, 1, 5),
    _StreamsStatsQueuesUsed_Type()
)
streamsStatsQueuesUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamsStatsQueuesUsed.setStatus("current")
_StreamsStatsQueuesMaxUsed_Type = Integer32
_StreamsStatsQueuesMaxUsed_Object = MibTableColumn
streamsStatsQueuesMaxUsed = _StreamsStatsQueuesMaxUsed_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 4, 2, 1, 6),
    _StreamsStatsQueuesMaxUsed_Type()
)
streamsStatsQueuesMaxUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamsStatsQueuesMaxUsed.setStatus("current")
_StreamsStatsQueuesFails_Type = Integer32
_StreamsStatsQueuesFails_Object = MibTableColumn
streamsStatsQueuesFails = _StreamsStatsQueuesFails_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 4, 2, 1, 7),
    _StreamsStatsQueuesFails_Type()
)
streamsStatsQueuesFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamsStatsQueuesFails.setStatus("current")
_StreamsStatsStreamsConfig_Type = Integer32
_StreamsStatsStreamsConfig_Object = MibTableColumn
streamsStatsStreamsConfig = _StreamsStatsStreamsConfig_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 4, 2, 1, 8),
    _StreamsStatsStreamsConfig_Type()
)
streamsStatsStreamsConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamsStatsStreamsConfig.setStatus("current")
_StreamsStatsStreamsInUse_Type = Integer32
_StreamsStatsStreamsInUse_Object = MibTableColumn
streamsStatsStreamsInUse = _StreamsStatsStreamsInUse_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 4, 2, 1, 9),
    _StreamsStatsStreamsInUse_Type()
)
streamsStatsStreamsInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamsStatsStreamsInUse.setStatus("current")
_StreamsStatsStreamsUsed_Type = Integer32
_StreamsStatsStreamsUsed_Object = MibTableColumn
streamsStatsStreamsUsed = _StreamsStatsStreamsUsed_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 4, 2, 1, 10),
    _StreamsStatsStreamsUsed_Type()
)
streamsStatsStreamsUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamsStatsStreamsUsed.setStatus("current")
_StreamsStatsStreamsMaxUsed_Type = Integer32
_StreamsStatsStreamsMaxUsed_Object = MibTableColumn
streamsStatsStreamsMaxUsed = _StreamsStatsStreamsMaxUsed_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 4, 2, 1, 11),
    _StreamsStatsStreamsMaxUsed_Type()
)
streamsStatsStreamsMaxUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamsStatsStreamsMaxUsed.setStatus("current")
_StreamsStatsStreamsFails_Type = Integer32
_StreamsStatsStreamsFails_Object = MibTableColumn
streamsStatsStreamsFails = _StreamsStatsStreamsFails_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 4, 2, 1, 12),
    _StreamsStatsStreamsFails_Type()
)
streamsStatsStreamsFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamsStatsStreamsFails.setStatus("current")
_StreamsStatsBufcallsConfig_Type = Integer32
_StreamsStatsBufcallsConfig_Object = MibTableColumn
streamsStatsBufcallsConfig = _StreamsStatsBufcallsConfig_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 4, 2, 1, 13),
    _StreamsStatsBufcallsConfig_Type()
)
streamsStatsBufcallsConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamsStatsBufcallsConfig.setStatus("current")
_StreamsStatsBufcallsInUse_Type = Integer32
_StreamsStatsBufcallsInUse_Object = MibTableColumn
streamsStatsBufcallsInUse = _StreamsStatsBufcallsInUse_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 4, 2, 1, 14),
    _StreamsStatsBufcallsInUse_Type()
)
streamsStatsBufcallsInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamsStatsBufcallsInUse.setStatus("current")
_StreamsStatsBufcallsUsed_Type = Integer32
_StreamsStatsBufcallsUsed_Object = MibTableColumn
streamsStatsBufcallsUsed = _StreamsStatsBufcallsUsed_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 4, 2, 1, 15),
    _StreamsStatsBufcallsUsed_Type()
)
streamsStatsBufcallsUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamsStatsBufcallsUsed.setStatus("current")
_StreamsStatsBufcallsMaxUsed_Type = Integer32
_StreamsStatsBufcallsMaxUsed_Object = MibTableColumn
streamsStatsBufcallsMaxUsed = _StreamsStatsBufcallsMaxUsed_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 4, 2, 1, 16),
    _StreamsStatsBufcallsMaxUsed_Type()
)
streamsStatsBufcallsMaxUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamsStatsBufcallsMaxUsed.setStatus("current")
_StreamsStatsBufcallsFails_Type = Integer32
_StreamsStatsBufcallsFails_Object = MibTableColumn
streamsStatsBufcallsFails = _StreamsStatsBufcallsFails_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 4, 2, 1, 17),
    _StreamsStatsBufcallsFails_Type()
)
streamsStatsBufcallsFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamsStatsBufcallsFails.setStatus("current")
_StreamsStatsTimeoutsConfig_Type = Integer32
_StreamsStatsTimeoutsConfig_Object = MibTableColumn
streamsStatsTimeoutsConfig = _StreamsStatsTimeoutsConfig_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 4, 2, 1, 18),
    _StreamsStatsTimeoutsConfig_Type()
)
streamsStatsTimeoutsConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamsStatsTimeoutsConfig.setStatus("current")
_StreamsStatsTimeoutsInUse_Type = Integer32
_StreamsStatsTimeoutsInUse_Object = MibTableColumn
streamsStatsTimeoutsInUse = _StreamsStatsTimeoutsInUse_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 4, 2, 1, 19),
    _StreamsStatsTimeoutsInUse_Type()
)
streamsStatsTimeoutsInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamsStatsTimeoutsInUse.setStatus("current")
_StreamsStatsTimeoutsUsed_Type = Integer32
_StreamsStatsTimeoutsUsed_Object = MibTableColumn
streamsStatsTimeoutsUsed = _StreamsStatsTimeoutsUsed_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 4, 2, 1, 20),
    _StreamsStatsTimeoutsUsed_Type()
)
streamsStatsTimeoutsUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamsStatsTimeoutsUsed.setStatus("current")
_StreamsStatsTimeoutsMaxUsed_Type = Integer32
_StreamsStatsTimeoutsMaxUsed_Object = MibTableColumn
streamsStatsTimeoutsMaxUsed = _StreamsStatsTimeoutsMaxUsed_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 4, 2, 1, 21),
    _StreamsStatsTimeoutsMaxUsed_Type()
)
streamsStatsTimeoutsMaxUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamsStatsTimeoutsMaxUsed.setStatus("current")
_StreamsStatsTimeoutsFails_Type = Integer32
_StreamsStatsTimeoutsFails_Object = MibTableColumn
streamsStatsTimeoutsFails = _StreamsStatsTimeoutsFails_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 4, 2, 1, 22),
    _StreamsStatsTimeoutsFails_Type()
)
streamsStatsTimeoutsFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamsStatsTimeoutsFails.setStatus("current")
_StreamsStatsMblksConfig_Type = Integer32
_StreamsStatsMblksConfig_Object = MibTableColumn
streamsStatsMblksConfig = _StreamsStatsMblksConfig_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 4, 2, 1, 23),
    _StreamsStatsMblksConfig_Type()
)
streamsStatsMblksConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamsStatsMblksConfig.setStatus("current")
_StreamsStatsMblksInUse_Type = Integer32
_StreamsStatsMblksInUse_Object = MibTableColumn
streamsStatsMblksInUse = _StreamsStatsMblksInUse_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 4, 2, 1, 24),
    _StreamsStatsMblksInUse_Type()
)
streamsStatsMblksInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamsStatsMblksInUse.setStatus("current")
_StreamsStatsMblksUsed_Type = Integer32
_StreamsStatsMblksUsed_Object = MibTableColumn
streamsStatsMblksUsed = _StreamsStatsMblksUsed_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 4, 2, 1, 25),
    _StreamsStatsMblksUsed_Type()
)
streamsStatsMblksUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamsStatsMblksUsed.setStatus("current")
_StreamsStatsMblksMaxUsed_Type = Integer32
_StreamsStatsMblksMaxUsed_Object = MibTableColumn
streamsStatsMblksMaxUsed = _StreamsStatsMblksMaxUsed_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 4, 2, 1, 26),
    _StreamsStatsMblksMaxUsed_Type()
)
streamsStatsMblksMaxUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamsStatsMblksMaxUsed.setStatus("current")
_StreamsStatsMblksFails_Type = Integer32
_StreamsStatsMblksFails_Object = MibTableColumn
streamsStatsMblksFails = _StreamsStatsMblksFails_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 4, 2, 1, 27),
    _StreamsStatsMblksFails_Type()
)
streamsStatsMblksFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamsStatsMblksFails.setStatus("current")
_StreamsStatsExtendedConfig_Type = Integer32
_StreamsStatsExtendedConfig_Object = MibTableColumn
streamsStatsExtendedConfig = _StreamsStatsExtendedConfig_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 4, 2, 1, 28),
    _StreamsStatsExtendedConfig_Type()
)
streamsStatsExtendedConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamsStatsExtendedConfig.setStatus("current")
_StreamsStatsExtendedInUse_Type = Integer32
_StreamsStatsExtendedInUse_Object = MibTableColumn
streamsStatsExtendedInUse = _StreamsStatsExtendedInUse_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 4, 2, 1, 29),
    _StreamsStatsExtendedInUse_Type()
)
streamsStatsExtendedInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamsStatsExtendedInUse.setStatus("current")
_StreamsStatsExtendedUsed_Type = Integer32
_StreamsStatsExtendedUsed_Object = MibTableColumn
streamsStatsExtendedUsed = _StreamsStatsExtendedUsed_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 4, 2, 1, 30),
    _StreamsStatsExtendedUsed_Type()
)
streamsStatsExtendedUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamsStatsExtendedUsed.setStatus("current")
_StreamsStatsExtendedMaxUsed_Type = Integer32
_StreamsStatsExtendedMaxUsed_Object = MibTableColumn
streamsStatsExtendedMaxUsed = _StreamsStatsExtendedMaxUsed_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 4, 2, 1, 31),
    _StreamsStatsExtendedMaxUsed_Type()
)
streamsStatsExtendedMaxUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamsStatsExtendedMaxUsed.setStatus("current")
_StreamsStatsExtendedFails_Type = Integer32
_StreamsStatsExtendedFails_Object = MibTableColumn
streamsStatsExtendedFails = _StreamsStatsExtendedFails_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 4, 2, 1, 32),
    _StreamsStatsExtendedFails_Type()
)
streamsStatsExtendedFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamsStatsExtendedFails.setStatus("current")
_StreamsStatsBufs0Config_Type = Integer32
_StreamsStatsBufs0Config_Object = MibTableColumn
streamsStatsBufs0Config = _StreamsStatsBufs0Config_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 4, 2, 1, 33),
    _StreamsStatsBufs0Config_Type()
)
streamsStatsBufs0Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamsStatsBufs0Config.setStatus("current")
_StreamsStatsBufs0InUse_Type = Integer32
_StreamsStatsBufs0InUse_Object = MibTableColumn
streamsStatsBufs0InUse = _StreamsStatsBufs0InUse_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 4, 2, 1, 34),
    _StreamsStatsBufs0InUse_Type()
)
streamsStatsBufs0InUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamsStatsBufs0InUse.setStatus("current")
_StreamsStatsBufs0Used_Type = Integer32
_StreamsStatsBufs0Used_Object = MibTableColumn
streamsStatsBufs0Used = _StreamsStatsBufs0Used_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 4, 2, 1, 35),
    _StreamsStatsBufs0Used_Type()
)
streamsStatsBufs0Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamsStatsBufs0Used.setStatus("current")
_StreamsStatsBufs0MaxUsed_Type = Integer32
_StreamsStatsBufs0MaxUsed_Object = MibTableColumn
streamsStatsBufs0MaxUsed = _StreamsStatsBufs0MaxUsed_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 4, 2, 1, 36),
    _StreamsStatsBufs0MaxUsed_Type()
)
streamsStatsBufs0MaxUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamsStatsBufs0MaxUsed.setStatus("current")
_StreamsStatsBufs0Fails_Type = Integer32
_StreamsStatsBufs0Fails_Object = MibTableColumn
streamsStatsBufs0Fails = _StreamsStatsBufs0Fails_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 4, 2, 1, 37),
    _StreamsStatsBufs0Fails_Type()
)
streamsStatsBufs0Fails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamsStatsBufs0Fails.setStatus("current")
_StreamsStatsBufs1Config_Type = Integer32
_StreamsStatsBufs1Config_Object = MibTableColumn
streamsStatsBufs1Config = _StreamsStatsBufs1Config_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 4, 2, 1, 38),
    _StreamsStatsBufs1Config_Type()
)
streamsStatsBufs1Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamsStatsBufs1Config.setStatus("current")
_StreamsStatsBufs1InUse_Type = Integer32
_StreamsStatsBufs1InUse_Object = MibTableColumn
streamsStatsBufs1InUse = _StreamsStatsBufs1InUse_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 4, 2, 1, 39),
    _StreamsStatsBufs1InUse_Type()
)
streamsStatsBufs1InUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamsStatsBufs1InUse.setStatus("current")
_StreamsStatsBufs1Used_Type = Integer32
_StreamsStatsBufs1Used_Object = MibTableColumn
streamsStatsBufs1Used = _StreamsStatsBufs1Used_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 4, 2, 1, 40),
    _StreamsStatsBufs1Used_Type()
)
streamsStatsBufs1Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamsStatsBufs1Used.setStatus("current")
_StreamsStatsBufs1MaxUsed_Type = Integer32
_StreamsStatsBufs1MaxUsed_Object = MibTableColumn
streamsStatsBufs1MaxUsed = _StreamsStatsBufs1MaxUsed_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 4, 2, 1, 41),
    _StreamsStatsBufs1MaxUsed_Type()
)
streamsStatsBufs1MaxUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamsStatsBufs1MaxUsed.setStatus("current")
_StreamsStatsBufs1Fails_Type = Integer32
_StreamsStatsBufs1Fails_Object = MibTableColumn
streamsStatsBufs1Fails = _StreamsStatsBufs1Fails_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 4, 2, 1, 42),
    _StreamsStatsBufs1Fails_Type()
)
streamsStatsBufs1Fails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamsStatsBufs1Fails.setStatus("current")
_StreamsStatsBufs2Config_Type = Integer32
_StreamsStatsBufs2Config_Object = MibTableColumn
streamsStatsBufs2Config = _StreamsStatsBufs2Config_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 4, 2, 1, 43),
    _StreamsStatsBufs2Config_Type()
)
streamsStatsBufs2Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamsStatsBufs2Config.setStatus("current")
_StreamsStatsBufs2InUse_Type = Integer32
_StreamsStatsBufs2InUse_Object = MibTableColumn
streamsStatsBufs2InUse = _StreamsStatsBufs2InUse_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 4, 2, 1, 44),
    _StreamsStatsBufs2InUse_Type()
)
streamsStatsBufs2InUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamsStatsBufs2InUse.setStatus("current")
_StreamsStatsBufs2Used_Type = Integer32
_StreamsStatsBufs2Used_Object = MibTableColumn
streamsStatsBufs2Used = _StreamsStatsBufs2Used_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 4, 2, 1, 45),
    _StreamsStatsBufs2Used_Type()
)
streamsStatsBufs2Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamsStatsBufs2Used.setStatus("current")
_StreamsStatsBufs2MaxUsed_Type = Integer32
_StreamsStatsBufs2MaxUsed_Object = MibTableColumn
streamsStatsBufs2MaxUsed = _StreamsStatsBufs2MaxUsed_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 4, 2, 1, 46),
    _StreamsStatsBufs2MaxUsed_Type()
)
streamsStatsBufs2MaxUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamsStatsBufs2MaxUsed.setStatus("current")
_StreamsStatsBufs2Fails_Type = Integer32
_StreamsStatsBufs2Fails_Object = MibTableColumn
streamsStatsBufs2Fails = _StreamsStatsBufs2Fails_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 4, 2, 1, 47),
    _StreamsStatsBufs2Fails_Type()
)
streamsStatsBufs2Fails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamsStatsBufs2Fails.setStatus("current")
_StreamsStatsBufs3Config_Type = Integer32
_StreamsStatsBufs3Config_Object = MibTableColumn
streamsStatsBufs3Config = _StreamsStatsBufs3Config_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 4, 2, 1, 48),
    _StreamsStatsBufs3Config_Type()
)
streamsStatsBufs3Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamsStatsBufs3Config.setStatus("current")
_StreamsStatsBufs3InUse_Type = Integer32
_StreamsStatsBufs3InUse_Object = MibTableColumn
streamsStatsBufs3InUse = _StreamsStatsBufs3InUse_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 4, 2, 1, 49),
    _StreamsStatsBufs3InUse_Type()
)
streamsStatsBufs3InUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamsStatsBufs3InUse.setStatus("current")
_StreamsStatsBufs3Used_Type = Integer32
_StreamsStatsBufs3Used_Object = MibTableColumn
streamsStatsBufs3Used = _StreamsStatsBufs3Used_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 4, 2, 1, 50),
    _StreamsStatsBufs3Used_Type()
)
streamsStatsBufs3Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamsStatsBufs3Used.setStatus("current")
_StreamsStatsBufs3MaxUsed_Type = Integer32
_StreamsStatsBufs3MaxUsed_Object = MibTableColumn
streamsStatsBufs3MaxUsed = _StreamsStatsBufs3MaxUsed_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 4, 2, 1, 51),
    _StreamsStatsBufs3MaxUsed_Type()
)
streamsStatsBufs3MaxUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamsStatsBufs3MaxUsed.setStatus("current")
_StreamsStatsBufs3Fails_Type = Integer32
_StreamsStatsBufs3Fails_Object = MibTableColumn
streamsStatsBufs3Fails = _StreamsStatsBufs3Fails_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 4, 2, 1, 52),
    _StreamsStatsBufs3Fails_Type()
)
streamsStatsBufs3Fails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamsStatsBufs3Fails.setStatus("current")
_StreamsStatsBufs4Config_Type = Integer32
_StreamsStatsBufs4Config_Object = MibTableColumn
streamsStatsBufs4Config = _StreamsStatsBufs4Config_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 4, 2, 1, 53),
    _StreamsStatsBufs4Config_Type()
)
streamsStatsBufs4Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamsStatsBufs4Config.setStatus("current")
_StreamsStatsBufs4InUse_Type = Integer32
_StreamsStatsBufs4InUse_Object = MibTableColumn
streamsStatsBufs4InUse = _StreamsStatsBufs4InUse_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 4, 2, 1, 54),
    _StreamsStatsBufs4InUse_Type()
)
streamsStatsBufs4InUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamsStatsBufs4InUse.setStatus("current")
_StreamsStatsBufs4Used_Type = Integer32
_StreamsStatsBufs4Used_Object = MibTableColumn
streamsStatsBufs4Used = _StreamsStatsBufs4Used_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 4, 2, 1, 55),
    _StreamsStatsBufs4Used_Type()
)
streamsStatsBufs4Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamsStatsBufs4Used.setStatus("current")
_StreamsStatsBufs4MaxUsed_Type = Integer32
_StreamsStatsBufs4MaxUsed_Object = MibTableColumn
streamsStatsBufs4MaxUsed = _StreamsStatsBufs4MaxUsed_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 4, 2, 1, 56),
    _StreamsStatsBufs4MaxUsed_Type()
)
streamsStatsBufs4MaxUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamsStatsBufs4MaxUsed.setStatus("current")
_StreamsStatsBufs4Fails_Type = Integer32
_StreamsStatsBufs4Fails_Object = MibTableColumn
streamsStatsBufs4Fails = _StreamsStatsBufs4Fails_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 4, 2, 1, 57),
    _StreamsStatsBufs4Fails_Type()
)
streamsStatsBufs4Fails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamsStatsBufs4Fails.setStatus("current")
_StreamsStatsBufs5Config_Type = Integer32
_StreamsStatsBufs5Config_Object = MibTableColumn
streamsStatsBufs5Config = _StreamsStatsBufs5Config_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 4, 2, 1, 58),
    _StreamsStatsBufs5Config_Type()
)
streamsStatsBufs5Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamsStatsBufs5Config.setStatus("current")
_StreamsStatsBufs5InUse_Type = Integer32
_StreamsStatsBufs5InUse_Object = MibTableColumn
streamsStatsBufs5InUse = _StreamsStatsBufs5InUse_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 4, 2, 1, 59),
    _StreamsStatsBufs5InUse_Type()
)
streamsStatsBufs5InUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamsStatsBufs5InUse.setStatus("current")
_StreamsStatsBufs5Used_Type = Integer32
_StreamsStatsBufs5Used_Object = MibTableColumn
streamsStatsBufs5Used = _StreamsStatsBufs5Used_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 4, 2, 1, 60),
    _StreamsStatsBufs5Used_Type()
)
streamsStatsBufs5Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamsStatsBufs5Used.setStatus("current")
_StreamsStatsBufs5MaxUsed_Type = Integer32
_StreamsStatsBufs5MaxUsed_Object = MibTableColumn
streamsStatsBufs5MaxUsed = _StreamsStatsBufs5MaxUsed_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 4, 2, 1, 61),
    _StreamsStatsBufs5MaxUsed_Type()
)
streamsStatsBufs5MaxUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamsStatsBufs5MaxUsed.setStatus("current")
_StreamsStatsBufs5Fails_Type = Integer32
_StreamsStatsBufs5Fails_Object = MibTableColumn
streamsStatsBufs5Fails = _StreamsStatsBufs5Fails_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 4, 2, 1, 62),
    _StreamsStatsBufs5Fails_Type()
)
streamsStatsBufs5Fails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamsStatsBufs5Fails.setStatus("current")
_StreamsStatsBufs6Config_Type = Integer32
_StreamsStatsBufs6Config_Object = MibTableColumn
streamsStatsBufs6Config = _StreamsStatsBufs6Config_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 4, 2, 1, 63),
    _StreamsStatsBufs6Config_Type()
)
streamsStatsBufs6Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamsStatsBufs6Config.setStatus("current")
_StreamsStatsBufs6InUse_Type = Integer32
_StreamsStatsBufs6InUse_Object = MibTableColumn
streamsStatsBufs6InUse = _StreamsStatsBufs6InUse_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 4, 2, 1, 64),
    _StreamsStatsBufs6InUse_Type()
)
streamsStatsBufs6InUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamsStatsBufs6InUse.setStatus("current")
_StreamsStatsBufs6Used_Type = Integer32
_StreamsStatsBufs6Used_Object = MibTableColumn
streamsStatsBufs6Used = _StreamsStatsBufs6Used_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 4, 2, 1, 65),
    _StreamsStatsBufs6Used_Type()
)
streamsStatsBufs6Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamsStatsBufs6Used.setStatus("current")
_StreamsStatsBufs6MaxUsed_Type = Integer32
_StreamsStatsBufs6MaxUsed_Object = MibTableColumn
streamsStatsBufs6MaxUsed = _StreamsStatsBufs6MaxUsed_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 4, 2, 1, 66),
    _StreamsStatsBufs6MaxUsed_Type()
)
streamsStatsBufs6MaxUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamsStatsBufs6MaxUsed.setStatus("current")
_StreamsStatsBufs6Fails_Type = Integer32
_StreamsStatsBufs6Fails_Object = MibTableColumn
streamsStatsBufs6Fails = _StreamsStatsBufs6Fails_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 4, 2, 1, 67),
    _StreamsStatsBufs6Fails_Type()
)
streamsStatsBufs6Fails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamsStatsBufs6Fails.setStatus("current")
_StreamsStatsBufs7Config_Type = Integer32
_StreamsStatsBufs7Config_Object = MibTableColumn
streamsStatsBufs7Config = _StreamsStatsBufs7Config_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 4, 2, 1, 68),
    _StreamsStatsBufs7Config_Type()
)
streamsStatsBufs7Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamsStatsBufs7Config.setStatus("current")
_StreamsStatsBufs7InUse_Type = Integer32
_StreamsStatsBufs7InUse_Object = MibTableColumn
streamsStatsBufs7InUse = _StreamsStatsBufs7InUse_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 4, 2, 1, 69),
    _StreamsStatsBufs7InUse_Type()
)
streamsStatsBufs7InUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamsStatsBufs7InUse.setStatus("current")
_StreamsStatsBufs7Used_Type = Integer32
_StreamsStatsBufs7Used_Object = MibTableColumn
streamsStatsBufs7Used = _StreamsStatsBufs7Used_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 4, 2, 1, 70),
    _StreamsStatsBufs7Used_Type()
)
streamsStatsBufs7Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamsStatsBufs7Used.setStatus("current")
_StreamsStatsBufs7MaxUsed_Type = Integer32
_StreamsStatsBufs7MaxUsed_Object = MibTableColumn
streamsStatsBufs7MaxUsed = _StreamsStatsBufs7MaxUsed_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 4, 2, 1, 71),
    _StreamsStatsBufs7MaxUsed_Type()
)
streamsStatsBufs7MaxUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamsStatsBufs7MaxUsed.setStatus("current")
_StreamsStatsBufs7Fails_Type = Integer32
_StreamsStatsBufs7Fails_Object = MibTableColumn
streamsStatsBufs7Fails = _StreamsStatsBufs7Fails_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 4, 2, 1, 72),
    _StreamsStatsBufs7Fails_Type()
)
streamsStatsBufs7Fails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamsStatsBufs7Fails.setStatus("current")
_StreamsStatsBufs8Config_Type = Integer32
_StreamsStatsBufs8Config_Object = MibTableColumn
streamsStatsBufs8Config = _StreamsStatsBufs8Config_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 4, 2, 1, 73),
    _StreamsStatsBufs8Config_Type()
)
streamsStatsBufs8Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamsStatsBufs8Config.setStatus("current")
_StreamsStatsBufs8InUse_Type = Integer32
_StreamsStatsBufs8InUse_Object = MibTableColumn
streamsStatsBufs8InUse = _StreamsStatsBufs8InUse_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 4, 2, 1, 74),
    _StreamsStatsBufs8InUse_Type()
)
streamsStatsBufs8InUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamsStatsBufs8InUse.setStatus("current")
_StreamsStatsBufs8Used_Type = Integer32
_StreamsStatsBufs8Used_Object = MibTableColumn
streamsStatsBufs8Used = _StreamsStatsBufs8Used_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 4, 2, 1, 75),
    _StreamsStatsBufs8Used_Type()
)
streamsStatsBufs8Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamsStatsBufs8Used.setStatus("current")
_StreamsStatsBufs8MaxUsed_Type = Integer32
_StreamsStatsBufs8MaxUsed_Object = MibTableColumn
streamsStatsBufs8MaxUsed = _StreamsStatsBufs8MaxUsed_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 4, 2, 1, 76),
    _StreamsStatsBufs8MaxUsed_Type()
)
streamsStatsBufs8MaxUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamsStatsBufs8MaxUsed.setStatus("current")
_StreamsStatsBufs8Fails_Type = Integer32
_StreamsStatsBufs8Fails_Object = MibTableColumn
streamsStatsBufs8Fails = _StreamsStatsBufs8Fails_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 4, 2, 1, 77),
    _StreamsStatsBufs8Fails_Type()
)
streamsStatsBufs8Fails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamsStatsBufs8Fails.setStatus("current")
_StreamsStatsBufs9Config_Type = Integer32
_StreamsStatsBufs9Config_Object = MibTableColumn
streamsStatsBufs9Config = _StreamsStatsBufs9Config_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 4, 2, 1, 78),
    _StreamsStatsBufs9Config_Type()
)
streamsStatsBufs9Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamsStatsBufs9Config.setStatus("current")
_StreamsStatsBufs9InUse_Type = Integer32
_StreamsStatsBufs9InUse_Object = MibTableColumn
streamsStatsBufs9InUse = _StreamsStatsBufs9InUse_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 4, 2, 1, 79),
    _StreamsStatsBufs9InUse_Type()
)
streamsStatsBufs9InUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamsStatsBufs9InUse.setStatus("current")
_StreamsStatsBufs9Used_Type = Integer32
_StreamsStatsBufs9Used_Object = MibTableColumn
streamsStatsBufs9Used = _StreamsStatsBufs9Used_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 4, 2, 1, 80),
    _StreamsStatsBufs9Used_Type()
)
streamsStatsBufs9Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamsStatsBufs9Used.setStatus("current")
_StreamsStatsBufs9MaxUsed_Type = Integer32
_StreamsStatsBufs9MaxUsed_Object = MibTableColumn
streamsStatsBufs9MaxUsed = _StreamsStatsBufs9MaxUsed_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 4, 2, 1, 81),
    _StreamsStatsBufs9MaxUsed_Type()
)
streamsStatsBufs9MaxUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamsStatsBufs9MaxUsed.setStatus("current")
_StreamsStatsBufs9Fails_Type = Integer32
_StreamsStatsBufs9Fails_Object = MibTableColumn
streamsStatsBufs9Fails = _StreamsStatsBufs9Fails_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 4, 2, 1, 82),
    _StreamsStatsBufs9Fails_Type()
)
streamsStatsBufs9Fails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamsStatsBufs9Fails.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "STREAMS-MIB",
    **{"aii": aii,
       "aiSLC2": aiSLC2,
       "streams": streams,
       "streamsAdmnTable": streamsAdmnTable,
       "streamsAdmnEntry": streamsAdmnEntry,
       "streamsAdmnSubsystemIndex": streamsAdmnSubsystemIndex,
       "streamsAdmnMaxStorage": streamsAdmnMaxStorage,
       "streamsAdmnNumQueues": streamsAdmnNumQueues,
       "streamsAdmnNumStreams": streamsAdmnNumStreams,
       "streamsAdmnNumBufcalls": streamsAdmnNumBufcalls,
       "streamsAdmnNumTimeouts": streamsAdmnNumTimeouts,
       "streamsAdmnNumMblks": streamsAdmnNumMblks,
       "streamsAdmnNumExtended": streamsAdmnNumExtended,
       "streamsAdmnLoSafetyMark": streamsAdmnLoSafetyMark,
       "streamsAdmnMidSafetyMark": streamsAdmnMidSafetyMark,
       "streamsAdmnNumBufs0": streamsAdmnNumBufs0,
       "streamsAdmnNumBufs1": streamsAdmnNumBufs1,
       "streamsAdmnNumBufs2": streamsAdmnNumBufs2,
       "streamsAdmnNumBufs3": streamsAdmnNumBufs3,
       "streamsAdmnNumBufs4": streamsAdmnNumBufs4,
       "streamsAdmnNumBufs5": streamsAdmnNumBufs5,
       "streamsAdmnNumBufs6": streamsAdmnNumBufs6,
       "streamsAdmnNumBufs7": streamsAdmnNumBufs7,
       "streamsAdmnNumBufs8": streamsAdmnNumBufs8,
       "streamsAdmnNumBufs9": streamsAdmnNumBufs9,
       "streamsAdmnSizeBufs0": streamsAdmnSizeBufs0,
       "streamsAdmnSizeBufs1": streamsAdmnSizeBufs1,
       "streamsAdmnSizeBufs2": streamsAdmnSizeBufs2,
       "streamsAdmnSizeBufs3": streamsAdmnSizeBufs3,
       "streamsAdmnSizeBufs4": streamsAdmnSizeBufs4,
       "streamsAdmnSizeBufs5": streamsAdmnSizeBufs5,
       "streamsAdmnSizeBufs6": streamsAdmnSizeBufs6,
       "streamsAdmnSizeBufs7": streamsAdmnSizeBufs7,
       "streamsAdmnSizeBufs8": streamsAdmnSizeBufs8,
       "streamsAdmnSizeBufs9": streamsAdmnSizeBufs9,
       "streamsStatsTable": streamsStatsTable,
       "streamsStatsEntry": streamsStatsEntry,
       "streamsStatsSubsystemIndex": streamsStatsSubsystemIndex,
       "streamsStatsAllocStorage": streamsStatsAllocStorage,
       "streamsStatsQueuesConfig": streamsStatsQueuesConfig,
       "streamsStatsQueuesInUse": streamsStatsQueuesInUse,
       "streamsStatsQueuesUsed": streamsStatsQueuesUsed,
       "streamsStatsQueuesMaxUsed": streamsStatsQueuesMaxUsed,
       "streamsStatsQueuesFails": streamsStatsQueuesFails,
       "streamsStatsStreamsConfig": streamsStatsStreamsConfig,
       "streamsStatsStreamsInUse": streamsStatsStreamsInUse,
       "streamsStatsStreamsUsed": streamsStatsStreamsUsed,
       "streamsStatsStreamsMaxUsed": streamsStatsStreamsMaxUsed,
       "streamsStatsStreamsFails": streamsStatsStreamsFails,
       "streamsStatsBufcallsConfig": streamsStatsBufcallsConfig,
       "streamsStatsBufcallsInUse": streamsStatsBufcallsInUse,
       "streamsStatsBufcallsUsed": streamsStatsBufcallsUsed,
       "streamsStatsBufcallsMaxUsed": streamsStatsBufcallsMaxUsed,
       "streamsStatsBufcallsFails": streamsStatsBufcallsFails,
       "streamsStatsTimeoutsConfig": streamsStatsTimeoutsConfig,
       "streamsStatsTimeoutsInUse": streamsStatsTimeoutsInUse,
       "streamsStatsTimeoutsUsed": streamsStatsTimeoutsUsed,
       "streamsStatsTimeoutsMaxUsed": streamsStatsTimeoutsMaxUsed,
       "streamsStatsTimeoutsFails": streamsStatsTimeoutsFails,
       "streamsStatsMblksConfig": streamsStatsMblksConfig,
       "streamsStatsMblksInUse": streamsStatsMblksInUse,
       "streamsStatsMblksUsed": streamsStatsMblksUsed,
       "streamsStatsMblksMaxUsed": streamsStatsMblksMaxUsed,
       "streamsStatsMblksFails": streamsStatsMblksFails,
       "streamsStatsExtendedConfig": streamsStatsExtendedConfig,
       "streamsStatsExtendedInUse": streamsStatsExtendedInUse,
       "streamsStatsExtendedUsed": streamsStatsExtendedUsed,
       "streamsStatsExtendedMaxUsed": streamsStatsExtendedMaxUsed,
       "streamsStatsExtendedFails": streamsStatsExtendedFails,
       "streamsStatsBufs0Config": streamsStatsBufs0Config,
       "streamsStatsBufs0InUse": streamsStatsBufs0InUse,
       "streamsStatsBufs0Used": streamsStatsBufs0Used,
       "streamsStatsBufs0MaxUsed": streamsStatsBufs0MaxUsed,
       "streamsStatsBufs0Fails": streamsStatsBufs0Fails,
       "streamsStatsBufs1Config": streamsStatsBufs1Config,
       "streamsStatsBufs1InUse": streamsStatsBufs1InUse,
       "streamsStatsBufs1Used": streamsStatsBufs1Used,
       "streamsStatsBufs1MaxUsed": streamsStatsBufs1MaxUsed,
       "streamsStatsBufs1Fails": streamsStatsBufs1Fails,
       "streamsStatsBufs2Config": streamsStatsBufs2Config,
       "streamsStatsBufs2InUse": streamsStatsBufs2InUse,
       "streamsStatsBufs2Used": streamsStatsBufs2Used,
       "streamsStatsBufs2MaxUsed": streamsStatsBufs2MaxUsed,
       "streamsStatsBufs2Fails": streamsStatsBufs2Fails,
       "streamsStatsBufs3Config": streamsStatsBufs3Config,
       "streamsStatsBufs3InUse": streamsStatsBufs3InUse,
       "streamsStatsBufs3Used": streamsStatsBufs3Used,
       "streamsStatsBufs3MaxUsed": streamsStatsBufs3MaxUsed,
       "streamsStatsBufs3Fails": streamsStatsBufs3Fails,
       "streamsStatsBufs4Config": streamsStatsBufs4Config,
       "streamsStatsBufs4InUse": streamsStatsBufs4InUse,
       "streamsStatsBufs4Used": streamsStatsBufs4Used,
       "streamsStatsBufs4MaxUsed": streamsStatsBufs4MaxUsed,
       "streamsStatsBufs4Fails": streamsStatsBufs4Fails,
       "streamsStatsBufs5Config": streamsStatsBufs5Config,
       "streamsStatsBufs5InUse": streamsStatsBufs5InUse,
       "streamsStatsBufs5Used": streamsStatsBufs5Used,
       "streamsStatsBufs5MaxUsed": streamsStatsBufs5MaxUsed,
       "streamsStatsBufs5Fails": streamsStatsBufs5Fails,
       "streamsStatsBufs6Config": streamsStatsBufs6Config,
       "streamsStatsBufs6InUse": streamsStatsBufs6InUse,
       "streamsStatsBufs6Used": streamsStatsBufs6Used,
       "streamsStatsBufs6MaxUsed": streamsStatsBufs6MaxUsed,
       "streamsStatsBufs6Fails": streamsStatsBufs6Fails,
       "streamsStatsBufs7Config": streamsStatsBufs7Config,
       "streamsStatsBufs7InUse": streamsStatsBufs7InUse,
       "streamsStatsBufs7Used": streamsStatsBufs7Used,
       "streamsStatsBufs7MaxUsed": streamsStatsBufs7MaxUsed,
       "streamsStatsBufs7Fails": streamsStatsBufs7Fails,
       "streamsStatsBufs8Config": streamsStatsBufs8Config,
       "streamsStatsBufs8InUse": streamsStatsBufs8InUse,
       "streamsStatsBufs8Used": streamsStatsBufs8Used,
       "streamsStatsBufs8MaxUsed": streamsStatsBufs8MaxUsed,
       "streamsStatsBufs8Fails": streamsStatsBufs8Fails,
       "streamsStatsBufs9Config": streamsStatsBufs9Config,
       "streamsStatsBufs9InUse": streamsStatsBufs9InUse,
       "streamsStatsBufs9Used": streamsStatsBufs9Used,
       "streamsStatsBufs9MaxUsed": streamsStatsBufs9MaxUsed,
       "streamsStatsBufs9Fails": streamsStatsBufs9Fails}
)
