# SNMP MIB module (ARISTA-QUEUE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ARISTA-QUEUE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:40:26 2024
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

(aristaMibs,) = mibBuilder.importSymbols(
    "ARISTA-SMI-MIB",
    "aristaMibs")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

aristaQueueMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 6)
)
aristaQueueMIB.setRevisions(
        ("2014-08-15 00:00",
         "2012-08-23 13:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class QueueIndex(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class PacketType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mixedPacketType", 2),
          ("multicast", 1),
          ("unicast", 0))
    )



class DropPrecedence(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dropPrecedence0", 0),
          ("dropPrecedence1", 1),
          ("dropPrecedence2", 2))
    )



# MIB Managed Objects in the order of their OIDs

_AristaQueue_ObjectIdentity = ObjectIdentity
aristaQueue = _AristaQueue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 6, 1)
)
_AristaIngressQueueTable_Object = MibTable
aristaIngressQueueTable = _AristaIngressQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 6, 1, 1)
)
if mibBuilder.loadTexts:
    aristaIngressQueueTable.setStatus("current")
_AristaIngressQueueEntry_Object = MibTableRow
aristaIngressQueueEntry = _AristaIngressQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 6, 1, 1, 1)
)
aristaIngressQueueEntry.setIndexNames(
    (0, "ARISTA-QUEUE-MIB", "aristaIngressIfIndex"),
    (0, "ARISTA-QUEUE-MIB", "aristaIngressQueueIndex"),
)
if mibBuilder.loadTexts:
    aristaIngressQueueEntry.setStatus("current")
_AristaIngressIfIndex_Type = InterfaceIndex
_AristaIngressIfIndex_Object = MibTableColumn
aristaIngressIfIndex = _AristaIngressIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 6, 1, 1, 1, 1),
    _AristaIngressIfIndex_Type()
)
aristaIngressIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aristaIngressIfIndex.setStatus("current")
_AristaIngressQueueIndex_Type = QueueIndex
_AristaIngressQueueIndex_Object = MibTableColumn
aristaIngressQueueIndex = _AristaIngressQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 6, 1, 1, 1, 2),
    _AristaIngressQueueIndex_Type()
)
aristaIngressQueueIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aristaIngressQueueIndex.setStatus("current")
_AristaIngressQueuePktsDropped_Type = Counter64
_AristaIngressQueuePktsDropped_Object = MibTableColumn
aristaIngressQueuePktsDropped = _AristaIngressQueuePktsDropped_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 6, 1, 1, 1, 3),
    _AristaIngressQueuePktsDropped_Type()
)
aristaIngressQueuePktsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaIngressQueuePktsDropped.setStatus("current")
_AristaIngressQueueBytesDropped_Type = Counter64
_AristaIngressQueueBytesDropped_Object = MibTableColumn
aristaIngressQueueBytesDropped = _AristaIngressQueueBytesDropped_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 6, 1, 1, 1, 4),
    _AristaIngressQueueBytesDropped_Type()
)
aristaIngressQueueBytesDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaIngressQueueBytesDropped.setStatus("current")
_AristaEgressQueueTable_Object = MibTable
aristaEgressQueueTable = _AristaEgressQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 6, 1, 2)
)
if mibBuilder.loadTexts:
    aristaEgressQueueTable.setStatus("current")
_AristaEgressQueueEntry_Object = MibTableRow
aristaEgressQueueEntry = _AristaEgressQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 6, 1, 2, 1)
)
aristaEgressQueueEntry.setIndexNames(
    (0, "ARISTA-QUEUE-MIB", "aristaEgressIfIndex"),
    (0, "ARISTA-QUEUE-MIB", "aristaEgressQueueIndex"),
    (0, "ARISTA-QUEUE-MIB", "aristaEgressPacketType"),
)
if mibBuilder.loadTexts:
    aristaEgressQueueEntry.setStatus("current")
_AristaEgressIfIndex_Type = InterfaceIndex
_AristaEgressIfIndex_Object = MibTableColumn
aristaEgressIfIndex = _AristaEgressIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 6, 1, 2, 1, 1),
    _AristaEgressIfIndex_Type()
)
aristaEgressIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aristaEgressIfIndex.setStatus("current")
_AristaEgressQueueIndex_Type = QueueIndex
_AristaEgressQueueIndex_Object = MibTableColumn
aristaEgressQueueIndex = _AristaEgressQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 6, 1, 2, 1, 2),
    _AristaEgressQueueIndex_Type()
)
aristaEgressQueueIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aristaEgressQueueIndex.setStatus("current")
_AristaEgressPacketType_Type = PacketType
_AristaEgressPacketType_Object = MibTableColumn
aristaEgressPacketType = _AristaEgressPacketType_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 6, 1, 2, 1, 3),
    _AristaEgressPacketType_Type()
)
aristaEgressPacketType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aristaEgressPacketType.setStatus("current")
_AristaEgressQueuePkts_Type = Counter64
_AristaEgressQueuePkts_Object = MibTableColumn
aristaEgressQueuePkts = _AristaEgressQueuePkts_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 6, 1, 2, 1, 4),
    _AristaEgressQueuePkts_Type()
)
aristaEgressQueuePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaEgressQueuePkts.setStatus("current")
_AristaEgressQueueBytes_Type = Counter64
_AristaEgressQueueBytes_Object = MibTableColumn
aristaEgressQueueBytes = _AristaEgressQueueBytes_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 6, 1, 2, 1, 5),
    _AristaEgressQueueBytes_Type()
)
aristaEgressQueueBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaEgressQueueBytes.setStatus("current")
_AristaEgressQueuePktsDropped_Type = Counter64
_AristaEgressQueuePktsDropped_Object = MibTableColumn
aristaEgressQueuePktsDropped = _AristaEgressQueuePktsDropped_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 6, 1, 2, 1, 6),
    _AristaEgressQueuePktsDropped_Type()
)
aristaEgressQueuePktsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaEgressQueuePktsDropped.setStatus("current")
_AristaEgressQueueBytesDropped_Type = Counter64
_AristaEgressQueueBytesDropped_Object = MibTableColumn
aristaEgressQueueBytesDropped = _AristaEgressQueueBytesDropped_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 6, 1, 2, 1, 7),
    _AristaEgressQueueBytesDropped_Type()
)
aristaEgressQueueBytesDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaEgressQueueBytesDropped.setStatus("current")
_AristaEgressQueuePktsDroppedQFull_Type = Counter64
_AristaEgressQueuePktsDroppedQFull_Object = MibTableColumn
aristaEgressQueuePktsDroppedQFull = _AristaEgressQueuePktsDroppedQFull_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 6, 1, 2, 1, 8),
    _AristaEgressQueuePktsDroppedQFull_Type()
)
aristaEgressQueuePktsDroppedQFull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaEgressQueuePktsDroppedQFull.setStatus("current")
_AristaEgressQueuePktsDroppedNoBuffer_Type = Counter64
_AristaEgressQueuePktsDroppedNoBuffer_Object = MibTableColumn
aristaEgressQueuePktsDroppedNoBuffer = _AristaEgressQueuePktsDroppedNoBuffer_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 6, 1, 2, 1, 9),
    _AristaEgressQueuePktsDroppedNoBuffer_Type()
)
aristaEgressQueuePktsDroppedNoBuffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaEgressQueuePktsDroppedNoBuffer.setStatus("current")
_AristaEgressQueueDropPrec_Type = DropPrecedence
_AristaEgressQueueDropPrec_Object = MibTableColumn
aristaEgressQueueDropPrec = _AristaEgressQueueDropPrec_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 6, 1, 2, 1, 10),
    _AristaEgressQueueDropPrec_Type()
)
aristaEgressQueueDropPrec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaEgressQueueDropPrec.setStatus("current")
_AristaQueueCounterConformance_ObjectIdentity = ObjectIdentity
aristaQueueCounterConformance = _AristaQueueCounterConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 6, 2)
)
_AristaQueueCounterCompliances_ObjectIdentity = ObjectIdentity
aristaQueueCounterCompliances = _AristaQueueCounterCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 6, 2, 1)
)
_AristaQueueCounterGroups_ObjectIdentity = ObjectIdentity
aristaQueueCounterGroups = _AristaQueueCounterGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 6, 2, 2)
)

# Managed Objects groups

aristaQueueCounterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 30065, 3, 6, 2, 2, 1)
)
aristaQueueCounterGroup.setObjects(
      *(("ARISTA-QUEUE-MIB", "aristaIngressQueuePktsDropped"),
        ("ARISTA-QUEUE-MIB", "aristaIngressQueueBytesDropped"),
        ("ARISTA-QUEUE-MIB", "aristaEgressQueuePkts"),
        ("ARISTA-QUEUE-MIB", "aristaEgressQueueBytes"),
        ("ARISTA-QUEUE-MIB", "aristaEgressQueuePktsDropped"),
        ("ARISTA-QUEUE-MIB", "aristaEgressQueueBytesDropped"),
        ("ARISTA-QUEUE-MIB", "aristaEgressQueuePktsDroppedQFull"),
        ("ARISTA-QUEUE-MIB", "aristaEgressQueuePktsDroppedNoBuffer"),
        ("ARISTA-QUEUE-MIB", "aristaEgressQueueDropPrec"))
)
if mibBuilder.loadTexts:
    aristaQueueCounterGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

aristaQueueCounterCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 30065, 3, 6, 2, 1, 1)
)
if mibBuilder.loadTexts:
    aristaQueueCounterCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARISTA-QUEUE-MIB",
    **{"QueueIndex": QueueIndex,
       "PacketType": PacketType,
       "DropPrecedence": DropPrecedence,
       "aristaQueueMIB": aristaQueueMIB,
       "aristaQueue": aristaQueue,
       "aristaIngressQueueTable": aristaIngressQueueTable,
       "aristaIngressQueueEntry": aristaIngressQueueEntry,
       "aristaIngressIfIndex": aristaIngressIfIndex,
       "aristaIngressQueueIndex": aristaIngressQueueIndex,
       "aristaIngressQueuePktsDropped": aristaIngressQueuePktsDropped,
       "aristaIngressQueueBytesDropped": aristaIngressQueueBytesDropped,
       "aristaEgressQueueTable": aristaEgressQueueTable,
       "aristaEgressQueueEntry": aristaEgressQueueEntry,
       "aristaEgressIfIndex": aristaEgressIfIndex,
       "aristaEgressQueueIndex": aristaEgressQueueIndex,
       "aristaEgressPacketType": aristaEgressPacketType,
       "aristaEgressQueuePkts": aristaEgressQueuePkts,
       "aristaEgressQueueBytes": aristaEgressQueueBytes,
       "aristaEgressQueuePktsDropped": aristaEgressQueuePktsDropped,
       "aristaEgressQueueBytesDropped": aristaEgressQueueBytesDropped,
       "aristaEgressQueuePktsDroppedQFull": aristaEgressQueuePktsDroppedQFull,
       "aristaEgressQueuePktsDroppedNoBuffer": aristaEgressQueuePktsDroppedNoBuffer,
       "aristaEgressQueueDropPrec": aristaEgressQueueDropPrec,
       "aristaQueueCounterConformance": aristaQueueCounterConformance,
       "aristaQueueCounterCompliances": aristaQueueCounterCompliances,
       "aristaQueueCounterCompliance": aristaQueueCounterCompliance,
       "aristaQueueCounterGroups": aristaQueueCounterGroups,
       "aristaQueueCounterGroup": aristaQueueCounterGroup}
)
