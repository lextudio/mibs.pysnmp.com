# SNMP MIB module (ALTIGA-SYNC-STATS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALTIGA-SYNC-STATS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:38:24 2024
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

(alSyncMibModule,) = mibBuilder.importSymbols(
    "ALTIGA-GLOBAL-REG",
    "alSyncMibModule")

(alStatsSync,
 alSyncGroup) = mibBuilder.importSymbols(
    "ALTIGA-MIB",
    "alStatsSync",
    "alSyncGroup")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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

(DisplayString,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

altigaSyncStatsMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 37, 2)
)
altigaSyncStatsMibModule.setRevisions(
        ("2002-09-05 13:00",
         "2002-07-10 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AltigaSyncStatsMibConformance_ObjectIdentity = ObjectIdentity
altigaSyncStatsMibConformance = _AltigaSyncStatsMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 37, 2, 1)
)
_AltigaSyncStatsMibCompliances_ObjectIdentity = ObjectIdentity
altigaSyncStatsMibCompliances = _AltigaSyncStatsMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 37, 2, 1, 1)
)
_AlStatsSyncGlobal_ObjectIdentity = ObjectIdentity
alStatsSyncGlobal = _AlStatsSyncGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 32, 1)
)
_AlSyncStatsTable_Object = MibTable
alSyncStatsTable = _AlSyncStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 32, 2)
)
if mibBuilder.loadTexts:
    alSyncStatsTable.setStatus("current")
_AlSyncStatsEntry_Object = MibTableRow
alSyncStatsEntry = _AlSyncStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 32, 2, 1)
)
alSyncStatsEntry.setIndexNames(
    (0, "ALTIGA-SYNC-STATS-MIB", "alSyncStatsSlot"),
    (0, "ALTIGA-SYNC-STATS-MIB", "alSyncStatsConn"),
    (0, "ALTIGA-SYNC-STATS-MIB", "alSyncStatsChannel"),
)
if mibBuilder.loadTexts:
    alSyncStatsEntry.setStatus("current")
_AlSyncStatsRowStatus_Type = RowStatus
_AlSyncStatsRowStatus_Object = MibTableColumn
alSyncStatsRowStatus = _AlSyncStatsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 32, 2, 1, 1),
    _AlSyncStatsRowStatus_Type()
)
alSyncStatsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alSyncStatsRowStatus.setStatus("current")


class _AlSyncStatsSlot_Type(Integer32):
    """Custom type alSyncStatsSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AlSyncStatsSlot_Type.__name__ = "Integer32"
_AlSyncStatsSlot_Object = MibTableColumn
alSyncStatsSlot = _AlSyncStatsSlot_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 32, 2, 1, 2),
    _AlSyncStatsSlot_Type()
)
alSyncStatsSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alSyncStatsSlot.setStatus("current")


class _AlSyncStatsConn_Type(Integer32):
    """Custom type alSyncStatsConn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AlSyncStatsConn_Type.__name__ = "Integer32"
_AlSyncStatsConn_Object = MibTableColumn
alSyncStatsConn = _AlSyncStatsConn_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 32, 2, 1, 3),
    _AlSyncStatsConn_Type()
)
alSyncStatsConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alSyncStatsConn.setStatus("current")


class _AlSyncStatsChannel_Type(Integer32):
    """Custom type alSyncStatsChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AlSyncStatsChannel_Type.__name__ = "Integer32"
_AlSyncStatsChannel_Object = MibTableColumn
alSyncStatsChannel = _AlSyncStatsChannel_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 32, 2, 1, 4),
    _AlSyncStatsChannel_Type()
)
alSyncStatsChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alSyncStatsChannel.setStatus("current")
_AlSyncStatsIfIndex_Type = InterfaceIndex
_AlSyncStatsIfIndex_Object = MibTableColumn
alSyncStatsIfIndex = _AlSyncStatsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 32, 2, 1, 5),
    _AlSyncStatsIfIndex_Type()
)
alSyncStatsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alSyncStatsIfIndex.setStatus("current")


class _AlSyncStatsPortState_Type(Integer32):
    """Custom type alSyncStatsPortState based on Integer32"""
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
        *(("down", 4),
          ("init", 1),
          ("running", 2),
          ("up", 3))
    )


_AlSyncStatsPortState_Type.__name__ = "Integer32"
_AlSyncStatsPortState_Object = MibTableColumn
alSyncStatsPortState = _AlSyncStatsPortState_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 32, 2, 1, 6),
    _AlSyncStatsPortState_Type()
)
alSyncStatsPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alSyncStatsPortState.setStatus("current")
_AlSyncStatsRxFrames_Type = Counter32
_AlSyncStatsRxFrames_Object = MibTableColumn
alSyncStatsRxFrames = _AlSyncStatsRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 32, 2, 1, 7),
    _AlSyncStatsRxFrames_Type()
)
alSyncStatsRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alSyncStatsRxFrames.setStatus("current")
_AlSyncStatsRxOctets_Type = Counter32
_AlSyncStatsRxOctets_Object = MibTableColumn
alSyncStatsRxOctets = _AlSyncStatsRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 32, 2, 1, 8),
    _AlSyncStatsRxOctets_Type()
)
alSyncStatsRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alSyncStatsRxOctets.setStatus("current")
_AlSyncStatsRxReplenFails_Type = Counter32
_AlSyncStatsRxReplenFails_Object = MibTableColumn
alSyncStatsRxReplenFails = _AlSyncStatsRxReplenFails_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 32, 2, 1, 9),
    _AlSyncStatsRxReplenFails_Type()
)
alSyncStatsRxReplenFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alSyncStatsRxReplenFails.setStatus("current")
_AlSyncStatsRxClockErrors_Type = Counter32
_AlSyncStatsRxClockErrors_Object = MibTableColumn
alSyncStatsRxClockErrors = _AlSyncStatsRxClockErrors_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 32, 2, 1, 10),
    _AlSyncStatsRxClockErrors_Type()
)
alSyncStatsRxClockErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alSyncStatsRxClockErrors.setStatus("current")
_AlSyncStatsRxDpllErrors_Type = Counter32
_AlSyncStatsRxDpllErrors_Object = MibTableColumn
alSyncStatsRxDpllErrors = _AlSyncStatsRxDpllErrors_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 32, 2, 1, 11),
    _AlSyncStatsRxDpllErrors_Type()
)
alSyncStatsRxDpllErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alSyncStatsRxDpllErrors.setStatus("current")
_AlSyncStatsRxFrameTooLongErrors_Type = Counter32
_AlSyncStatsRxFrameTooLongErrors_Object = MibTableColumn
alSyncStatsRxFrameTooLongErrors = _AlSyncStatsRxFrameTooLongErrors_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 32, 2, 1, 12),
    _AlSyncStatsRxFrameTooLongErrors_Type()
)
alSyncStatsRxFrameTooLongErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alSyncStatsRxFrameTooLongErrors.setStatus("current")
_AlSyncStatsRxFrameOctetAlignErrors_Type = Counter32
_AlSyncStatsRxFrameOctetAlignErrors_Object = MibTableColumn
alSyncStatsRxFrameOctetAlignErrors = _AlSyncStatsRxFrameOctetAlignErrors_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 32, 2, 1, 13),
    _AlSyncStatsRxFrameOctetAlignErrors_Type()
)
alSyncStatsRxFrameOctetAlignErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alSyncStatsRxFrameOctetAlignErrors.setStatus("current")
_AlSyncStatsRxAbortErrors_Type = Counter32
_AlSyncStatsRxAbortErrors_Object = MibTableColumn
alSyncStatsRxAbortErrors = _AlSyncStatsRxAbortErrors_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 32, 2, 1, 14),
    _AlSyncStatsRxAbortErrors_Type()
)
alSyncStatsRxAbortErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alSyncStatsRxAbortErrors.setStatus("current")
_AlSyncStatsRxCrcErrors_Type = Counter32
_AlSyncStatsRxCrcErrors_Object = MibTableColumn
alSyncStatsRxCrcErrors = _AlSyncStatsRxCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 32, 2, 1, 15),
    _AlSyncStatsRxCrcErrors_Type()
)
alSyncStatsRxCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alSyncStatsRxCrcErrors.setStatus("current")
_AlSyncStatsRxRcvrOverrunErrors_Type = Counter32
_AlSyncStatsRxRcvrOverrunErrors_Object = MibTableColumn
alSyncStatsRxRcvrOverrunErrors = _AlSyncStatsRxRcvrOverrunErrors_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 32, 2, 1, 16),
    _AlSyncStatsRxRcvrOverrunErrors_Type()
)
alSyncStatsRxRcvrOverrunErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alSyncStatsRxRcvrOverrunErrors.setStatus("current")
_AlSyncStatsTxFrames_Type = Counter32
_AlSyncStatsTxFrames_Object = MibTableColumn
alSyncStatsTxFrames = _AlSyncStatsTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 32, 2, 1, 17),
    _AlSyncStatsTxFrames_Type()
)
alSyncStatsTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alSyncStatsTxFrames.setStatus("current")
_AlSyncStatsTxOctets_Type = Counter32
_AlSyncStatsTxOctets_Object = MibTableColumn
alSyncStatsTxOctets = _AlSyncStatsTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 32, 2, 1, 18),
    _AlSyncStatsTxOctets_Type()
)
alSyncStatsTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alSyncStatsTxOctets.setStatus("current")
_AlSyncStatsTxRingFullDropsErrors_Type = Counter32
_AlSyncStatsTxRingFullDropsErrors_Object = MibTableColumn
alSyncStatsTxRingFullDropsErrors = _AlSyncStatsTxRingFullDropsErrors_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 32, 2, 1, 19),
    _AlSyncStatsTxRingFullDropsErrors_Type()
)
alSyncStatsTxRingFullDropsErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alSyncStatsTxRingFullDropsErrors.setStatus("current")
_AlSyncStatsTxClockErrors_Type = Counter32
_AlSyncStatsTxClockErrors_Object = MibTableColumn
alSyncStatsTxClockErrors = _AlSyncStatsTxClockErrors_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 32, 2, 1, 20),
    _AlSyncStatsTxClockErrors_Type()
)
alSyncStatsTxClockErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alSyncStatsTxClockErrors.setStatus("current")
_AlSyncStatsTxFrameTooLongErrors_Type = Counter32
_AlSyncStatsTxFrameTooLongErrors_Object = MibTableColumn
alSyncStatsTxFrameTooLongErrors = _AlSyncStatsTxFrameTooLongErrors_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 32, 2, 1, 21),
    _AlSyncStatsTxFrameTooLongErrors_Type()
)
alSyncStatsTxFrameTooLongErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alSyncStatsTxFrameTooLongErrors.setStatus("current")
_AlSyncStatsTxUnderrunErrors_Type = Counter32
_AlSyncStatsTxUnderrunErrors_Object = MibTableColumn
alSyncStatsTxUnderrunErrors = _AlSyncStatsTxUnderrunErrors_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 32, 2, 1, 22),
    _AlSyncStatsTxUnderrunErrors_Type()
)
alSyncStatsTxUnderrunErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alSyncStatsTxUnderrunErrors.setStatus("current")

# Managed Objects groups

altigaSyncStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1, 32, 2)
)
altigaSyncStatsGroup.setObjects(
      *(("ALTIGA-SYNC-STATS-MIB", "alSyncStatsRowStatus"),
        ("ALTIGA-SYNC-STATS-MIB", "alSyncStatsSlot"),
        ("ALTIGA-SYNC-STATS-MIB", "alSyncStatsConn"),
        ("ALTIGA-SYNC-STATS-MIB", "alSyncStatsChannel"),
        ("ALTIGA-SYNC-STATS-MIB", "alSyncStatsIfIndex"),
        ("ALTIGA-SYNC-STATS-MIB", "alSyncStatsPortState"),
        ("ALTIGA-SYNC-STATS-MIB", "alSyncStatsRxFrames"),
        ("ALTIGA-SYNC-STATS-MIB", "alSyncStatsRxOctets"),
        ("ALTIGA-SYNC-STATS-MIB", "alSyncStatsRxReplenFails"),
        ("ALTIGA-SYNC-STATS-MIB", "alSyncStatsRxClockErrors"),
        ("ALTIGA-SYNC-STATS-MIB", "alSyncStatsRxDpllErrors"),
        ("ALTIGA-SYNC-STATS-MIB", "alSyncStatsRxFrameTooLongErrors"),
        ("ALTIGA-SYNC-STATS-MIB", "alSyncStatsRxFrameOctetAlignErrors"),
        ("ALTIGA-SYNC-STATS-MIB", "alSyncStatsRxAbortErrors"),
        ("ALTIGA-SYNC-STATS-MIB", "alSyncStatsRxCrcErrors"),
        ("ALTIGA-SYNC-STATS-MIB", "alSyncStatsRxRcvrOverrunErrors"),
        ("ALTIGA-SYNC-STATS-MIB", "alSyncStatsTxFrames"),
        ("ALTIGA-SYNC-STATS-MIB", "alSyncStatsTxOctets"),
        ("ALTIGA-SYNC-STATS-MIB", "alSyncStatsTxRingFullDropsErrors"),
        ("ALTIGA-SYNC-STATS-MIB", "alSyncStatsTxClockErrors"),
        ("ALTIGA-SYNC-STATS-MIB", "alSyncStatsTxFrameTooLongErrors"),
        ("ALTIGA-SYNC-STATS-MIB", "alSyncStatsTxUnderrunErrors"))
)
if mibBuilder.loadTexts:
    altigaSyncStatsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

altigaSyncStatsMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 37, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    altigaSyncStatsMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALTIGA-SYNC-STATS-MIB",
    **{"altigaSyncStatsMibModule": altigaSyncStatsMibModule,
       "altigaSyncStatsMibConformance": altigaSyncStatsMibConformance,
       "altigaSyncStatsMibCompliances": altigaSyncStatsMibCompliances,
       "altigaSyncStatsMibCompliance": altigaSyncStatsMibCompliance,
       "altigaSyncStatsGroup": altigaSyncStatsGroup,
       "alStatsSyncGlobal": alStatsSyncGlobal,
       "alSyncStatsTable": alSyncStatsTable,
       "alSyncStatsEntry": alSyncStatsEntry,
       "alSyncStatsRowStatus": alSyncStatsRowStatus,
       "alSyncStatsSlot": alSyncStatsSlot,
       "alSyncStatsConn": alSyncStatsConn,
       "alSyncStatsChannel": alSyncStatsChannel,
       "alSyncStatsIfIndex": alSyncStatsIfIndex,
       "alSyncStatsPortState": alSyncStatsPortState,
       "alSyncStatsRxFrames": alSyncStatsRxFrames,
       "alSyncStatsRxOctets": alSyncStatsRxOctets,
       "alSyncStatsRxReplenFails": alSyncStatsRxReplenFails,
       "alSyncStatsRxClockErrors": alSyncStatsRxClockErrors,
       "alSyncStatsRxDpllErrors": alSyncStatsRxDpllErrors,
       "alSyncStatsRxFrameTooLongErrors": alSyncStatsRxFrameTooLongErrors,
       "alSyncStatsRxFrameOctetAlignErrors": alSyncStatsRxFrameOctetAlignErrors,
       "alSyncStatsRxAbortErrors": alSyncStatsRxAbortErrors,
       "alSyncStatsRxCrcErrors": alSyncStatsRxCrcErrors,
       "alSyncStatsRxRcvrOverrunErrors": alSyncStatsRxRcvrOverrunErrors,
       "alSyncStatsTxFrames": alSyncStatsTxFrames,
       "alSyncStatsTxOctets": alSyncStatsTxOctets,
       "alSyncStatsTxRingFullDropsErrors": alSyncStatsTxRingFullDropsErrors,
       "alSyncStatsTxClockErrors": alSyncStatsTxClockErrors,
       "alSyncStatsTxFrameTooLongErrors": alSyncStatsTxFrameTooLongErrors,
       "alSyncStatsTxUnderrunErrors": alSyncStatsTxUnderrunErrors}
)
