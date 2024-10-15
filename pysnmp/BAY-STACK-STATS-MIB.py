# SNMP MIB module (BAY-STACK-STATS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BAY-STACK-STATS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:46:22 2024
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

(bayStackMibs,) = mibBuilder.importSymbols(
    "SYNOPTICS-ROOT-MIB",
    "bayStackMibs")


# MODULE-IDENTITY

bayStackStatsMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 12)
)
bayStackStatsMib.setRevisions(
        ("2015-05-11 00:00",
         "2014-12-03 00:00",
         "2014-10-15 00:00",
         "2012-09-12 00:00",
         "2007-03-09 00:00",
         "2005-08-12 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BayStackStatsNotifications_ObjectIdentity = ObjectIdentity
bayStackStatsNotifications = _BayStackStatsNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 12, 0)
)
_BayStackStatsObjects_ObjectIdentity = ObjectIdentity
bayStackStatsObjects = _BayStackStatsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 12, 1)
)
_BayStackStatsIfTable_Object = MibTable
bayStackStatsIfTable = _BayStackStatsIfTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 12, 1, 1)
)
if mibBuilder.loadTexts:
    bayStackStatsIfTable.setStatus("current")
_BayStackStatsIfEntry_Object = MibTableRow
bayStackStatsIfEntry = _BayStackStatsIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 12, 1, 1, 1)
)
bayStackStatsIfEntry.setIndexNames(
    (0, "BAY-STACK-STATS-MIB", "bayStackStatsIfIndex"),
)
if mibBuilder.loadTexts:
    bayStackStatsIfEntry.setStatus("current")
_BayStackStatsIfIndex_Type = InterfaceIndex
_BayStackStatsIfIndex_Object = MibTableColumn
bayStackStatsIfIndex = _BayStackStatsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 12, 1, 1, 1, 1),
    _BayStackStatsIfIndex_Type()
)
bayStackStatsIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bayStackStatsIfIndex.setStatus("current")
_BayStackStatsIfNoResourcesPktsDropped_Type = Counter64
_BayStackStatsIfNoResourcesPktsDropped_Object = MibTableColumn
bayStackStatsIfNoResourcesPktsDropped = _BayStackStatsIfNoResourcesPktsDropped_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 12, 1, 1, 1, 2),
    _BayStackStatsIfNoResourcesPktsDropped_Type()
)
bayStackStatsIfNoResourcesPktsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bayStackStatsIfNoResourcesPktsDropped.setStatus("current")
_BayStackStatsIfInPfcFrames_Type = Counter64
_BayStackStatsIfInPfcFrames_Object = MibTableColumn
bayStackStatsIfInPfcFrames = _BayStackStatsIfInPfcFrames_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 12, 1, 1, 1, 3),
    _BayStackStatsIfInPfcFrames_Type()
)
bayStackStatsIfInPfcFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bayStackStatsIfInPfcFrames.setStatus("current")
_BayStackStatsIfOutPfcFrames_Type = Counter64
_BayStackStatsIfOutPfcFrames_Object = MibTableColumn
bayStackStatsIfOutPfcFrames = _BayStackStatsIfOutPfcFrames_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 12, 1, 1, 1, 4),
    _BayStackStatsIfOutPfcFrames_Type()
)
bayStackStatsIfOutPfcFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bayStackStatsIfOutPfcFrames.setStatus("current")
_BayStackStatsUnitTable_Object = MibTable
bayStackStatsUnitTable = _BayStackStatsUnitTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 12, 1, 2)
)
if mibBuilder.loadTexts:
    bayStackStatsUnitTable.setStatus("current")
_BayStackStatsUnitEntry_Object = MibTableRow
bayStackStatsUnitEntry = _BayStackStatsUnitEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 12, 1, 2, 1)
)
bayStackStatsUnitEntry.setIndexNames(
    (0, "BAY-STACK-STATS-MIB", "bayStackStatsUnitIndex"),
)
if mibBuilder.loadTexts:
    bayStackStatsUnitEntry.setStatus("current")


class _BayStackStatsUnitIndex_Type(Integer32):
    """Custom type bayStackStatsUnitIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_BayStackStatsUnitIndex_Type.__name__ = "Integer32"
_BayStackStatsUnitIndex_Object = MibTableColumn
bayStackStatsUnitIndex = _BayStackStatsUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 12, 1, 2, 1, 1),
    _BayStackStatsUnitIndex_Type()
)
bayStackStatsUnitIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bayStackStatsUnitIndex.setStatus("current")
_BayStackStatsUnitNoResourcesPktsDropped_Type = Counter64
_BayStackStatsUnitNoResourcesPktsDropped_Object = MibTableColumn
bayStackStatsUnitNoResourcesPktsDropped = _BayStackStatsUnitNoResourcesPktsDropped_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 12, 1, 2, 1, 2),
    _BayStackStatsUnitNoResourcesPktsDropped_Type()
)
bayStackStatsUnitNoResourcesPktsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bayStackStatsUnitNoResourcesPktsDropped.setStatus("current")
_BayStackStatsCoSQueueTable_Object = MibTable
bayStackStatsCoSQueueTable = _BayStackStatsCoSQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 12, 1, 3)
)
if mibBuilder.loadTexts:
    bayStackStatsCoSQueueTable.setStatus("current")
_BayStackStatsCoSQueueEntry_Object = MibTableRow
bayStackStatsCoSQueueEntry = _BayStackStatsCoSQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 12, 1, 3, 1)
)
bayStackStatsCoSQueueEntry.setIndexNames(
    (0, "BAY-STACK-STATS-MIB", "bayStackStatsCoSQueueIfIndex"),
    (0, "BAY-STACK-STATS-MIB", "bayStackStatsCoSQueueQueue"),
)
if mibBuilder.loadTexts:
    bayStackStatsCoSQueueEntry.setStatus("current")
_BayStackStatsCoSQueueIfIndex_Type = InterfaceIndex
_BayStackStatsCoSQueueIfIndex_Object = MibTableColumn
bayStackStatsCoSQueueIfIndex = _BayStackStatsCoSQueueIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 12, 1, 3, 1, 1),
    _BayStackStatsCoSQueueIfIndex_Type()
)
bayStackStatsCoSQueueIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bayStackStatsCoSQueueIfIndex.setStatus("current")


class _BayStackStatsCoSQueueQueue_Type(Integer32):
    """Custom type bayStackStatsCoSQueueQueue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_BayStackStatsCoSQueueQueue_Type.__name__ = "Integer32"
_BayStackStatsCoSQueueQueue_Object = MibTableColumn
bayStackStatsCoSQueueQueue = _BayStackStatsCoSQueueQueue_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 12, 1, 3, 1, 2),
    _BayStackStatsCoSQueueQueue_Type()
)
bayStackStatsCoSQueueQueue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bayStackStatsCoSQueueQueue.setStatus("current")
_BayStackStatsCoSQueueOutPackets_Type = Counter64
_BayStackStatsCoSQueueOutPackets_Object = MibTableColumn
bayStackStatsCoSQueueOutPackets = _BayStackStatsCoSQueueOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 12, 1, 3, 1, 3),
    _BayStackStatsCoSQueueOutPackets_Type()
)
bayStackStatsCoSQueueOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bayStackStatsCoSQueueOutPackets.setStatus("current")
_BayStackStatsCoSQueueOutBytes_Type = Counter64
_BayStackStatsCoSQueueOutBytes_Object = MibTableColumn
bayStackStatsCoSQueueOutBytes = _BayStackStatsCoSQueueOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 12, 1, 3, 1, 4),
    _BayStackStatsCoSQueueOutBytes_Type()
)
bayStackStatsCoSQueueOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bayStackStatsCoSQueueOutBytes.setStatus("current")
_BayStackStatsCoSQueueDropPackets_Type = Counter64
_BayStackStatsCoSQueueDropPackets_Object = MibTableColumn
bayStackStatsCoSQueueDropPackets = _BayStackStatsCoSQueueDropPackets_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 12, 1, 3, 1, 5),
    _BayStackStatsCoSQueueDropPackets_Type()
)
bayStackStatsCoSQueueDropPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bayStackStatsCoSQueueDropPackets.setStatus("current")
_BayStackStatsCoSQueueDropBytes_Type = Counter64
_BayStackStatsCoSQueueDropBytes_Object = MibTableColumn
bayStackStatsCoSQueueDropBytes = _BayStackStatsCoSQueueDropBytes_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 12, 1, 3, 1, 6),
    _BayStackStatsCoSQueueDropBytes_Type()
)
bayStackStatsCoSQueueDropBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bayStackStatsCoSQueueDropBytes.setStatus("current")


class _BayStackStatsCoSQueueClear_Type(Integer32):
    """Custom type bayStackStatsCoSQueueClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("none", 1))
    )


_BayStackStatsCoSQueueClear_Type.__name__ = "Integer32"
_BayStackStatsCoSQueueClear_Object = MibTableColumn
bayStackStatsCoSQueueClear = _BayStackStatsCoSQueueClear_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 12, 1, 3, 1, 7),
    _BayStackStatsCoSQueueClear_Type()
)
bayStackStatsCoSQueueClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bayStackStatsCoSQueueClear.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BAY-STACK-STATS-MIB",
    **{"bayStackStatsMib": bayStackStatsMib,
       "bayStackStatsNotifications": bayStackStatsNotifications,
       "bayStackStatsObjects": bayStackStatsObjects,
       "bayStackStatsIfTable": bayStackStatsIfTable,
       "bayStackStatsIfEntry": bayStackStatsIfEntry,
       "bayStackStatsIfIndex": bayStackStatsIfIndex,
       "bayStackStatsIfNoResourcesPktsDropped": bayStackStatsIfNoResourcesPktsDropped,
       "bayStackStatsIfInPfcFrames": bayStackStatsIfInPfcFrames,
       "bayStackStatsIfOutPfcFrames": bayStackStatsIfOutPfcFrames,
       "bayStackStatsUnitTable": bayStackStatsUnitTable,
       "bayStackStatsUnitEntry": bayStackStatsUnitEntry,
       "bayStackStatsUnitIndex": bayStackStatsUnitIndex,
       "bayStackStatsUnitNoResourcesPktsDropped": bayStackStatsUnitNoResourcesPktsDropped,
       "bayStackStatsCoSQueueTable": bayStackStatsCoSQueueTable,
       "bayStackStatsCoSQueueEntry": bayStackStatsCoSQueueEntry,
       "bayStackStatsCoSQueueIfIndex": bayStackStatsCoSQueueIfIndex,
       "bayStackStatsCoSQueueQueue": bayStackStatsCoSQueueQueue,
       "bayStackStatsCoSQueueOutPackets": bayStackStatsCoSQueueOutPackets,
       "bayStackStatsCoSQueueOutBytes": bayStackStatsCoSQueueOutBytes,
       "bayStackStatsCoSQueueDropPackets": bayStackStatsCoSQueueDropPackets,
       "bayStackStatsCoSQueueDropBytes": bayStackStatsCoSQueueDropBytes,
       "bayStackStatsCoSQueueClear": bayStackStatsCoSQueueClear}
)
