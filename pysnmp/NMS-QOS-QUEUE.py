# SNMP MIB module (NMS-QOS-QUEUE) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NMS-QOS-QUEUE
# Produced by pysmi-1.5.4 at Mon Oct 14 22:28:04 2024
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

(nmstemporary,) = mibBuilder.importSymbols(
    "NMS-SMI",
    "nmstemporary")

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


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NmsQosQueue_ObjectIdentity = ObjectIdentity
nmsQosQueue = _NmsQosQueue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11606, 10, 3, 7)
)
_NmsQosQueueTable_Object = MibTable
nmsQosQueueTable = _NmsQosQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 3, 7, 1)
)
if mibBuilder.loadTexts:
    nmsQosQueueTable.setStatus("mandatory")
_NmsQosQueueEntry_Object = MibTableRow
nmsQosQueueEntry = _NmsQosQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 3, 7, 1, 1)
)
nmsQosQueueEntry.setIndexNames(
    (0, "NMS-QOS-QUEUE", "ifIndex"),
    (0, "NMS-QOS-QUEUE", "queueNo"),
)
if mibBuilder.loadTexts:
    nmsQosQueueEntry.setStatus("mandatory")
_IfIndex_Type = Integer32
_IfIndex_Object = MibTableColumn
ifIndex = _IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 3, 7, 1, 1, 1),
    _IfIndex_Type()
)
ifIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifIndex.setStatus("mandatory")
_QueueNo_Type = Integer32
_QueueNo_Object = MibTableColumn
queueNo = _QueueNo_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 3, 7, 1, 1, 2),
    _QueueNo_Type()
)
queueNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queueNo.setStatus("mandatory")
_QueueLen_Type = Integer32
_QueueLen_Object = MibTableColumn
queueLen = _QueueLen_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 3, 7, 1, 1, 3),
    _QueueLen_Type()
)
queueLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queueLen.setStatus("mandatory")
_QueueDrops_Type = Integer32
_QueueDrops_Object = MibTableColumn
queueDrops = _QueueDrops_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 3, 7, 1, 1, 4),
    _QueueDrops_Type()
)
queueDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queueDrops.setStatus("mandatory")
_QueueCross_Type = Integer32
_QueueCross_Object = MibTableColumn
queueCross = _QueueCross_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 3, 7, 1, 1, 5),
    _QueueCross_Type()
)
queueCross.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queueCross.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NMS-QOS-QUEUE",
    **{"nmsQosQueue": nmsQosQueue,
       "nmsQosQueueTable": nmsQosQueueTable,
       "nmsQosQueueEntry": nmsQosQueueEntry,
       "ifIndex": ifIndex,
       "queueNo": queueNo,
       "queueLen": queueLen,
       "queueDrops": queueDrops,
       "queueCross": queueCross}
)
