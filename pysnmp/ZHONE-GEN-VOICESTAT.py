# SNMP MIB module (ZHONE-GEN-VOICESTAT) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZHONE-GEN-VOICESTAT
# Produced by pysmi-1.5.4 at Mon Oct 14 23:20:33 2024
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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(zhoneGeneric,
 zhoneShelfIndex,
 zhoneSlotIndex) = mibBuilder.importSymbols(
    "Zhone",
    "zhoneGeneric",
    "zhoneShelfIndex",
    "zhoneSlotIndex")

(ZhoneRowStatus,) = mibBuilder.importSymbols(
    "Zhone-TC",
    "ZhoneRowStatus")


# MODULE-IDENTITY

zhoneVoiceStatsRecords = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 3, 11, 1)
)
zhoneVoiceStatsRecords.setRevisions(
        ("2005-09-06 15:30",
         "2003-06-27 12:18")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZhoneVoiceStats_ObjectIdentity = ObjectIdentity
zhoneVoiceStats = _ZhoneVoiceStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 3, 11)
)
if mibBuilder.loadTexts:
    zhoneVoiceStats.setStatus("current")
_ZhoneSystemStats_ObjectIdentity = ObjectIdentity
zhoneSystemStats = _ZhoneSystemStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 3, 11, 1, 1)
)
if mibBuilder.loadTexts:
    zhoneSystemStats.setStatus("current")
_SystemIncomingCallsCompleted_Type = Integer32
_SystemIncomingCallsCompleted_Object = MibScalar
systemIncomingCallsCompleted = _SystemIncomingCallsCompleted_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 11, 1, 1, 1),
    _SystemIncomingCallsCompleted_Type()
)
systemIncomingCallsCompleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemIncomingCallsCompleted.setStatus("current")
_SystemIncomingCallsBlocked_Type = Integer32
_SystemIncomingCallsBlocked_Object = MibScalar
systemIncomingCallsBlocked = _SystemIncomingCallsBlocked_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 11, 1, 1, 2),
    _SystemIncomingCallsBlocked_Type()
)
systemIncomingCallsBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemIncomingCallsBlocked.setStatus("current")
_SystemOutgoingCallsCompleted_Type = Integer32
_SystemOutgoingCallsCompleted_Object = MibScalar
systemOutgoingCallsCompleted = _SystemOutgoingCallsCompleted_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 11, 1, 1, 3),
    _SystemOutgoingCallsCompleted_Type()
)
systemOutgoingCallsCompleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemOutgoingCallsCompleted.setStatus("current")
_SystemOutgoingCallsBlocked_Type = Integer32
_SystemOutgoingCallsBlocked_Object = MibScalar
systemOutgoingCallsBlocked = _SystemOutgoingCallsBlocked_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 11, 1, 1, 4),
    _SystemOutgoingCallsBlocked_Type()
)
systemOutgoingCallsBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemOutgoingCallsBlocked.setStatus("current")
_SystemActiveCalls_Type = Integer32
_SystemActiveCalls_Object = MibScalar
systemActiveCalls = _SystemActiveCalls_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 11, 1, 1, 5),
    _SystemActiveCalls_Type()
)
systemActiveCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemActiveCalls.setStatus("current")
_ZhoneCardStatsTable_Object = MibTable
zhoneCardStatsTable = _ZhoneCardStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 11, 1, 2)
)
if mibBuilder.loadTexts:
    zhoneCardStatsTable.setStatus("current")
_ZhoneCardStatsEntry_Object = MibTableRow
zhoneCardStatsEntry = _ZhoneCardStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 11, 1, 2, 1)
)
zhoneCardStatsEntry.setIndexNames(
    (0, "Zhone", "zhoneShelfIndex"),
    (0, "Zhone", "zhoneSlotIndex"),
)
if mibBuilder.loadTexts:
    zhoneCardStatsEntry.setStatus("current")
_CardIncomingCallsCompleted_Type = Integer32
_CardIncomingCallsCompleted_Object = MibTableColumn
cardIncomingCallsCompleted = _CardIncomingCallsCompleted_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 11, 1, 2, 1, 1),
    _CardIncomingCallsCompleted_Type()
)
cardIncomingCallsCompleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardIncomingCallsCompleted.setStatus("current")
_CardIncomingCallsBlocked_Type = Integer32
_CardIncomingCallsBlocked_Object = MibTableColumn
cardIncomingCallsBlocked = _CardIncomingCallsBlocked_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 11, 1, 2, 1, 2),
    _CardIncomingCallsBlocked_Type()
)
cardIncomingCallsBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardIncomingCallsBlocked.setStatus("current")
_CardOutgoingCallsCompleted_Type = Integer32
_CardOutgoingCallsCompleted_Object = MibTableColumn
cardOutgoingCallsCompleted = _CardOutgoingCallsCompleted_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 11, 1, 2, 1, 3),
    _CardOutgoingCallsCompleted_Type()
)
cardOutgoingCallsCompleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardOutgoingCallsCompleted.setStatus("current")
_CardOutgoingCallsBlocked_Type = Integer32
_CardOutgoingCallsBlocked_Object = MibTableColumn
cardOutgoingCallsBlocked = _CardOutgoingCallsBlocked_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 11, 1, 2, 1, 4),
    _CardOutgoingCallsBlocked_Type()
)
cardOutgoingCallsBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardOutgoingCallsBlocked.setStatus("current")
_CardActiveCalls_Type = Integer32
_CardActiveCalls_Object = MibTableColumn
cardActiveCalls = _CardActiveCalls_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 11, 1, 2, 1, 5),
    _CardActiveCalls_Type()
)
cardActiveCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardActiveCalls.setStatus("current")
_ZhoneSubscriberEPStatsTable_Object = MibTable
zhoneSubscriberEPStatsTable = _ZhoneSubscriberEPStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 11, 1, 3)
)
if mibBuilder.loadTexts:
    zhoneSubscriberEPStatsTable.setStatus("current")
_ZhoneSubscriberEPStatsEntry_Object = MibTableRow
zhoneSubscriberEPStatsEntry = _ZhoneSubscriberEPStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 11, 1, 3, 1)
)
zhoneSubscriberEPStatsEntry.setIndexNames(
    (0, "ZHONE-GEN-VOICESTAT", "subVoiceEndPointIndex"),
)
if mibBuilder.loadTexts:
    zhoneSubscriberEPStatsEntry.setStatus("current")


class _SubVoiceEndPointIndex_Type(Integer32):
    """Custom type subVoiceEndPointIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SubVoiceEndPointIndex_Type.__name__ = "Integer32"
_SubVoiceEndPointIndex_Object = MibTableColumn
subVoiceEndPointIndex = _SubVoiceEndPointIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 11, 1, 3, 1, 2),
    _SubVoiceEndPointIndex_Type()
)
subVoiceEndPointIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    subVoiceEndPointIndex.setStatus("current")
_SubEPIncomingCallsCompleted_Type = Integer32
_SubEPIncomingCallsCompleted_Object = MibTableColumn
subEPIncomingCallsCompleted = _SubEPIncomingCallsCompleted_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 11, 1, 3, 1, 3),
    _SubEPIncomingCallsCompleted_Type()
)
subEPIncomingCallsCompleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subEPIncomingCallsCompleted.setStatus("current")
_SubEPIncomingCallsBlocked_Type = Integer32
_SubEPIncomingCallsBlocked_Object = MibTableColumn
subEPIncomingCallsBlocked = _SubEPIncomingCallsBlocked_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 11, 1, 3, 1, 4),
    _SubEPIncomingCallsBlocked_Type()
)
subEPIncomingCallsBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subEPIncomingCallsBlocked.setStatus("current")
_SubEPOutgoingCallsCompleted_Type = Integer32
_SubEPOutgoingCallsCompleted_Object = MibTableColumn
subEPOutgoingCallsCompleted = _SubEPOutgoingCallsCompleted_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 11, 1, 3, 1, 5),
    _SubEPOutgoingCallsCompleted_Type()
)
subEPOutgoingCallsCompleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subEPOutgoingCallsCompleted.setStatus("current")
_SubEPOutgoingCallsBlocked_Type = Integer32
_SubEPOutgoingCallsBlocked_Object = MibTableColumn
subEPOutgoingCallsBlocked = _SubEPOutgoingCallsBlocked_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 11, 1, 3, 1, 6),
    _SubEPOutgoingCallsBlocked_Type()
)
subEPOutgoingCallsBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subEPOutgoingCallsBlocked.setStatus("current")
_SubEPActiveCalls_Type = Integer32
_SubEPActiveCalls_Object = MibTableColumn
subEPActiveCalls = _SubEPActiveCalls_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 11, 1, 3, 1, 7),
    _SubEPActiveCalls_Type()
)
subEPActiveCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subEPActiveCalls.setStatus("current")
_ZhoneVoiceRingTable_Object = MibTable
zhoneVoiceRingTable = _ZhoneVoiceRingTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 11, 1, 8)
)
if mibBuilder.loadTexts:
    zhoneVoiceRingTable.setStatus("current")
_ZhoneVoiceRingEntry_Object = MibTableRow
zhoneVoiceRingEntry = _ZhoneVoiceRingEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 11, 1, 8, 1)
)
zhoneVoiceRingEntry.setIndexNames(
    (0, "ZHONE-GEN-VOICESTAT", "zhoneVoiceRingIfIndex"),
)
if mibBuilder.loadTexts:
    zhoneVoiceRingEntry.setStatus("current")
_ZhoneVoiceRingIfIndex_Type = InterfaceIndex
_ZhoneVoiceRingIfIndex_Object = MibTableColumn
zhoneVoiceRingIfIndex = _ZhoneVoiceRingIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 11, 1, 8, 1, 1),
    _ZhoneVoiceRingIfIndex_Type()
)
zhoneVoiceRingIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhoneVoiceRingIfIndex.setStatus("current")


class _ZhoneVoiceRingRingingCadence_Type(Integer32):
    """Custom type zhoneVoiceRingRingingCadence based on Integer32"""
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
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("ringCadenceCommon", 9),
          ("ringCadenceR0", 1),
          ("ringCadenceR1", 2),
          ("ringCadenceR2", 3),
          ("ringCadenceR3", 4),
          ("ringCadenceR4", 5),
          ("ringCadenceR5", 6),
          ("ringCadenceR6", 7),
          ("ringCadenceR7", 8),
          ("ringCadenceSplash", 10))
    )


_ZhoneVoiceRingRingingCadence_Type.__name__ = "Integer32"
_ZhoneVoiceRingRingingCadence_Object = MibTableColumn
zhoneVoiceRingRingingCadence = _ZhoneVoiceRingRingingCadence_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 11, 1, 8, 1, 2),
    _ZhoneVoiceRingRingingCadence_Type()
)
zhoneVoiceRingRingingCadence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVoiceRingRingingCadence.setStatus("current")


class _ZhoneVoiceRingTimer_Type(Integer32):
    """Custom type zhoneVoiceRingTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_ZhoneVoiceRingTimer_Type.__name__ = "Integer32"
_ZhoneVoiceRingTimer_Object = MibTableColumn
zhoneVoiceRingTimer = _ZhoneVoiceRingTimer_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 11, 1, 8, 1, 3),
    _ZhoneVoiceRingTimer_Type()
)
zhoneVoiceRingTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVoiceRingTimer.setStatus("current")
_ZhoneVoiceRingRowStatus_Type = ZhoneRowStatus
_ZhoneVoiceRingRowStatus_Object = MibTableColumn
zhoneVoiceRingRowStatus = _ZhoneVoiceRingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 11, 1, 8, 1, 4),
    _ZhoneVoiceRingRowStatus_Type()
)
zhoneVoiceRingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVoiceRingRowStatus.setStatus("current")

# Managed Objects groups

zhoneVoiceStatsObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 3, 11, 1, 7)
)
zhoneVoiceStatsObjectsGroup.setObjects(
      *(("ZHONE-GEN-VOICESTAT", "systemIncomingCallsCompleted"),
        ("ZHONE-GEN-VOICESTAT", "systemIncomingCallsBlocked"),
        ("ZHONE-GEN-VOICESTAT", "systemOutgoingCallsCompleted"),
        ("ZHONE-GEN-VOICESTAT", "systemOutgoingCallsBlocked"),
        ("ZHONE-GEN-VOICESTAT", "systemActiveCalls"),
        ("ZHONE-GEN-VOICESTAT", "cardIncomingCallsCompleted"),
        ("ZHONE-GEN-VOICESTAT", "cardIncomingCallsBlocked"),
        ("ZHONE-GEN-VOICESTAT", "cardOutgoingCallsCompleted"),
        ("ZHONE-GEN-VOICESTAT", "cardOutgoingCallsBlocked"),
        ("ZHONE-GEN-VOICESTAT", "cardActiveCalls"),
        ("ZHONE-GEN-VOICESTAT", "subEPIncomingCallsCompleted"),
        ("ZHONE-GEN-VOICESTAT", "subEPIncomingCallsBlocked"),
        ("ZHONE-GEN-VOICESTAT", "subEPOutgoingCallsCompleted"),
        ("ZHONE-GEN-VOICESTAT", "subEPOutgoingCallsBlocked"),
        ("ZHONE-GEN-VOICESTAT", "subEPActiveCalls"))
)
if mibBuilder.loadTexts:
    zhoneVoiceStatsObjectsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZHONE-GEN-VOICESTAT",
    **{"zhoneVoiceStats": zhoneVoiceStats,
       "zhoneVoiceStatsRecords": zhoneVoiceStatsRecords,
       "zhoneSystemStats": zhoneSystemStats,
       "systemIncomingCallsCompleted": systemIncomingCallsCompleted,
       "systemIncomingCallsBlocked": systemIncomingCallsBlocked,
       "systemOutgoingCallsCompleted": systemOutgoingCallsCompleted,
       "systemOutgoingCallsBlocked": systemOutgoingCallsBlocked,
       "systemActiveCalls": systemActiveCalls,
       "zhoneCardStatsTable": zhoneCardStatsTable,
       "zhoneCardStatsEntry": zhoneCardStatsEntry,
       "cardIncomingCallsCompleted": cardIncomingCallsCompleted,
       "cardIncomingCallsBlocked": cardIncomingCallsBlocked,
       "cardOutgoingCallsCompleted": cardOutgoingCallsCompleted,
       "cardOutgoingCallsBlocked": cardOutgoingCallsBlocked,
       "cardActiveCalls": cardActiveCalls,
       "zhoneSubscriberEPStatsTable": zhoneSubscriberEPStatsTable,
       "zhoneSubscriberEPStatsEntry": zhoneSubscriberEPStatsEntry,
       "subVoiceEndPointIndex": subVoiceEndPointIndex,
       "subEPIncomingCallsCompleted": subEPIncomingCallsCompleted,
       "subEPIncomingCallsBlocked": subEPIncomingCallsBlocked,
       "subEPOutgoingCallsCompleted": subEPOutgoingCallsCompleted,
       "subEPOutgoingCallsBlocked": subEPOutgoingCallsBlocked,
       "subEPActiveCalls": subEPActiveCalls,
       "zhoneVoiceStatsObjectsGroup": zhoneVoiceStatsObjectsGroup,
       "zhoneVoiceRingTable": zhoneVoiceRingTable,
       "zhoneVoiceRingEntry": zhoneVoiceRingEntry,
       "zhoneVoiceRingIfIndex": zhoneVoiceRingIfIndex,
       "zhoneVoiceRingRingingCadence": zhoneVoiceRingRingingCadence,
       "zhoneVoiceRingTimer": zhoneVoiceRingTimer,
       "zhoneVoiceRingRowStatus": zhoneVoiceRingRowStatus}
)
