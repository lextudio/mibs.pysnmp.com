# SNMP MIB module (PACKETLOGIC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PACKETLOGIC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:36:07 2024
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

(CounterBasedGauge64,) = mibBuilder.importSymbols(
    "HCNUM-TC",
    "CounterBasedGauge64")

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

(DateAndTime,
 DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

procera = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 15397)
)
procera.setRevisions(
        ("2012-09-26 12:48",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Packetlogic2_ObjectIdentity = ObjectIdentity
packetlogic2 = _Packetlogic2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2)
)
_Sysdiag_ObjectIdentity = ObjectIdentity
sysdiag = _Sysdiag_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1)
)
_Packetprocessing_ObjectIdentity = ObjectIdentity
packetprocessing = _Packetprocessing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 8)
)
_PacketprocessingRx_ObjectIdentity = ObjectIdentity
packetprocessingRx = _PacketprocessingRx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 8, 1)
)
_PacketprocessingRxVal_Type = Counter64
_PacketprocessingRxVal_Object = MibScalar
packetprocessingRxVal = _PacketprocessingRxVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 8, 1, 1),
    _PacketprocessingRxVal_Type()
)
packetprocessingRxVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    packetprocessingRxVal.setStatus("current")
_PacketprocessingRxMom_Type = CounterBasedGauge64
_PacketprocessingRxMom_Object = MibScalar
packetprocessingRxMom = _PacketprocessingRxMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 8, 1, 2),
    _PacketprocessingRxMom_Type()
)
packetprocessingRxMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    packetprocessingRxMom.setStatus("current")
_PacketprocessingRxMax_Type = CounterBasedGauge64
_PacketprocessingRxMax_Object = MibScalar
packetprocessingRxMax = _PacketprocessingRxMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 8, 1, 3),
    _PacketprocessingRxMax_Type()
)
packetprocessingRxMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    packetprocessingRxMax.setStatus("current")
_PacketprocessingRxDrops_ObjectIdentity = ObjectIdentity
packetprocessingRxDrops = _PacketprocessingRxDrops_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 8, 2)
)
_PacketprocessingRxDropsVal_Type = Counter64
_PacketprocessingRxDropsVal_Object = MibScalar
packetprocessingRxDropsVal = _PacketprocessingRxDropsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 8, 2, 1),
    _PacketprocessingRxDropsVal_Type()
)
packetprocessingRxDropsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    packetprocessingRxDropsVal.setStatus("current")
_PacketprocessingRxDropsMom_Type = CounterBasedGauge64
_PacketprocessingRxDropsMom_Object = MibScalar
packetprocessingRxDropsMom = _PacketprocessingRxDropsMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 8, 2, 2),
    _PacketprocessingRxDropsMom_Type()
)
packetprocessingRxDropsMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    packetprocessingRxDropsMom.setStatus("current")
_PacketprocessingRxDropsMax_Type = CounterBasedGauge64
_PacketprocessingRxDropsMax_Object = MibScalar
packetprocessingRxDropsMax = _PacketprocessingRxDropsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 8, 2, 3),
    _PacketprocessingRxDropsMax_Type()
)
packetprocessingRxDropsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    packetprocessingRxDropsMax.setStatus("current")
_PacketprocessingTx_ObjectIdentity = ObjectIdentity
packetprocessingTx = _PacketprocessingTx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 8, 6)
)
_PacketprocessingTxVal_Type = Counter64
_PacketprocessingTxVal_Object = MibScalar
packetprocessingTxVal = _PacketprocessingTxVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 8, 6, 1),
    _PacketprocessingTxVal_Type()
)
packetprocessingTxVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    packetprocessingTxVal.setStatus("current")
_PacketprocessingTxMom_Type = CounterBasedGauge64
_PacketprocessingTxMom_Object = MibScalar
packetprocessingTxMom = _PacketprocessingTxMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 8, 6, 2),
    _PacketprocessingTxMom_Type()
)
packetprocessingTxMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    packetprocessingTxMom.setStatus("current")
_PacketprocessingTxMax_Type = CounterBasedGauge64
_PacketprocessingTxMax_Object = MibScalar
packetprocessingTxMax = _PacketprocessingTxMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 8, 6, 3),
    _PacketprocessingTxMax_Type()
)
packetprocessingTxMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    packetprocessingTxMax.setStatus("current")
_PacketprocessingTxDrops_ObjectIdentity = ObjectIdentity
packetprocessingTxDrops = _PacketprocessingTxDrops_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 8, 7)
)
_PacketprocessingTxDropsVal_Type = Counter64
_PacketprocessingTxDropsVal_Object = MibScalar
packetprocessingTxDropsVal = _PacketprocessingTxDropsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 8, 7, 1),
    _PacketprocessingTxDropsVal_Type()
)
packetprocessingTxDropsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    packetprocessingTxDropsVal.setStatus("current")
_PacketprocessingTxDropsMom_Type = CounterBasedGauge64
_PacketprocessingTxDropsMom_Object = MibScalar
packetprocessingTxDropsMom = _PacketprocessingTxDropsMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 8, 7, 2),
    _PacketprocessingTxDropsMom_Type()
)
packetprocessingTxDropsMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    packetprocessingTxDropsMom.setStatus("current")
_PacketprocessingTxDropsMax_Type = CounterBasedGauge64
_PacketprocessingTxDropsMax_Object = MibScalar
packetprocessingTxDropsMax = _PacketprocessingTxDropsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 8, 7, 3),
    _PacketprocessingTxDropsMax_Type()
)
packetprocessingTxDropsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    packetprocessingTxDropsMax.setStatus("current")
_PacketprocessingPacketPoolSize_ObjectIdentity = ObjectIdentity
packetprocessingPacketPoolSize = _PacketprocessingPacketPoolSize_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 8, 10)
)
_PacketprocessingPacketPoolSizeVal_Type = CounterBasedGauge64
_PacketprocessingPacketPoolSizeVal_Object = MibScalar
packetprocessingPacketPoolSizeVal = _PacketprocessingPacketPoolSizeVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 8, 10, 1),
    _PacketprocessingPacketPoolSizeVal_Type()
)
packetprocessingPacketPoolSizeVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    packetprocessingPacketPoolSizeVal.setStatus("current")
_PacketprocessingPacketPoolSizeMax_Type = CounterBasedGauge64
_PacketprocessingPacketPoolSizeMax_Object = MibScalar
packetprocessingPacketPoolSizeMax = _PacketprocessingPacketPoolSizeMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 8, 10, 3),
    _PacketprocessingPacketPoolSizeMax_Type()
)
packetprocessingPacketPoolSizeMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    packetprocessingPacketPoolSizeMax.setStatus("current")
_PacketprocessingDmaAllocs_ObjectIdentity = ObjectIdentity
packetprocessingDmaAllocs = _PacketprocessingDmaAllocs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 8, 13)
)
_PacketprocessingDmaAllocsVal_Type = CounterBasedGauge64
_PacketprocessingDmaAllocsVal_Object = MibScalar
packetprocessingDmaAllocsVal = _PacketprocessingDmaAllocsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 8, 13, 1),
    _PacketprocessingDmaAllocsVal_Type()
)
packetprocessingDmaAllocsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    packetprocessingDmaAllocsVal.setStatus("current")
_PacketprocessingDmaAllocsMax_Type = CounterBasedGauge64
_PacketprocessingDmaAllocsMax_Object = MibScalar
packetprocessingDmaAllocsMax = _PacketprocessingDmaAllocsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 8, 13, 3),
    _PacketprocessingDmaAllocsMax_Type()
)
packetprocessingDmaAllocsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    packetprocessingDmaAllocsMax.setStatus("current")
_PacketprocessingLoad_ObjectIdentity = ObjectIdentity
packetprocessingLoad = _PacketprocessingLoad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 8, 15)
)
_PacketprocessingLoadVal_Type = Unsigned32
_PacketprocessingLoadVal_Object = MibScalar
packetprocessingLoadVal = _PacketprocessingLoadVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 8, 15, 1),
    _PacketprocessingLoadVal_Type()
)
packetprocessingLoadVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    packetprocessingLoadVal.setStatus("current")
_PacketprocessingLoadMax_Type = Unsigned32
_PacketprocessingLoadMax_Object = MibScalar
packetprocessingLoadMax = _PacketprocessingLoadMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 8, 15, 3),
    _PacketprocessingLoadMax_Type()
)
packetprocessingLoadMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    packetprocessingLoadMax.setStatus("current")
_PacketprocessingHeapfree_ObjectIdentity = ObjectIdentity
packetprocessingHeapfree = _PacketprocessingHeapfree_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 8, 16)
)
_PacketprocessingHeapfreeVal_Type = CounterBasedGauge64
_PacketprocessingHeapfreeVal_Object = MibScalar
packetprocessingHeapfreeVal = _PacketprocessingHeapfreeVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 8, 16, 1),
    _PacketprocessingHeapfreeVal_Type()
)
packetprocessingHeapfreeVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    packetprocessingHeapfreeVal.setStatus("current")
_PacketprocessingHeapfreeMax_Type = CounterBasedGauge64
_PacketprocessingHeapfreeMax_Object = MibScalar
packetprocessingHeapfreeMax = _PacketprocessingHeapfreeMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 8, 16, 3),
    _PacketprocessingHeapfreeMax_Type()
)
packetprocessingHeapfreeMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    packetprocessingHeapfreeMax.setStatus("current")
_PacketprocessingUptime_ObjectIdentity = ObjectIdentity
packetprocessingUptime = _PacketprocessingUptime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 8, 17)
)
_PacketprocessingUptimeVal_Type = TimeTicks
_PacketprocessingUptimeVal_Object = MibScalar
packetprocessingUptimeVal = _PacketprocessingUptimeVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 8, 17, 1),
    _PacketprocessingUptimeVal_Type()
)
packetprocessingUptimeVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    packetprocessingUptimeVal.setStatus("current")
_PacketprocessingPushbackQueueFull_ObjectIdentity = ObjectIdentity
packetprocessingPushbackQueueFull = _PacketprocessingPushbackQueueFull_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 8, 18)
)
_PacketprocessingPushbackQueueFullVal_Type = Counter64
_PacketprocessingPushbackQueueFullVal_Object = MibScalar
packetprocessingPushbackQueueFullVal = _PacketprocessingPushbackQueueFullVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 8, 18, 1),
    _PacketprocessingPushbackQueueFullVal_Type()
)
packetprocessingPushbackQueueFullVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    packetprocessingPushbackQueueFullVal.setStatus("obsolete")
_PacketprocessingPushbackQueueFullMom_Type = CounterBasedGauge64
_PacketprocessingPushbackQueueFullMom_Object = MibScalar
packetprocessingPushbackQueueFullMom = _PacketprocessingPushbackQueueFullMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 8, 18, 2),
    _PacketprocessingPushbackQueueFullMom_Type()
)
packetprocessingPushbackQueueFullMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    packetprocessingPushbackQueueFullMom.setStatus("obsolete")
_PacketprocessingPushbackQueueFullMax_Type = CounterBasedGauge64
_PacketprocessingPushbackQueueFullMax_Object = MibScalar
packetprocessingPushbackQueueFullMax = _PacketprocessingPushbackQueueFullMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 8, 18, 3),
    _PacketprocessingPushbackQueueFullMax_Type()
)
packetprocessingPushbackQueueFullMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    packetprocessingPushbackQueueFullMax.setStatus("obsolete")
_PacketprocessingPushbackPackets_ObjectIdentity = ObjectIdentity
packetprocessingPushbackPackets = _PacketprocessingPushbackPackets_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 8, 19)
)
_PacketprocessingPushbackPacketsVal_Type = Counter64
_PacketprocessingPushbackPacketsVal_Object = MibScalar
packetprocessingPushbackPacketsVal = _PacketprocessingPushbackPacketsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 8, 19, 1),
    _PacketprocessingPushbackPacketsVal_Type()
)
packetprocessingPushbackPacketsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    packetprocessingPushbackPacketsVal.setStatus("obsolete")
_PacketprocessingPushbackPacketsMom_Type = CounterBasedGauge64
_PacketprocessingPushbackPacketsMom_Object = MibScalar
packetprocessingPushbackPacketsMom = _PacketprocessingPushbackPacketsMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 8, 19, 2),
    _PacketprocessingPushbackPacketsMom_Type()
)
packetprocessingPushbackPacketsMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    packetprocessingPushbackPacketsMom.setStatus("obsolete")
_PacketprocessingPushbackPacketsMax_Type = CounterBasedGauge64
_PacketprocessingPushbackPacketsMax_Object = MibScalar
packetprocessingPushbackPacketsMax = _PacketprocessingPushbackPacketsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 8, 19, 3),
    _PacketprocessingPushbackPacketsMax_Type()
)
packetprocessingPushbackPacketsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    packetprocessingPushbackPacketsMax.setStatus("obsolete")
_PacketprocessingPushbackQueueSize_ObjectIdentity = ObjectIdentity
packetprocessingPushbackQueueSize = _PacketprocessingPushbackQueueSize_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 8, 20)
)
_PacketprocessingPushbackQueueSizeVal_Type = CounterBasedGauge64
_PacketprocessingPushbackQueueSizeVal_Object = MibScalar
packetprocessingPushbackQueueSizeVal = _PacketprocessingPushbackQueueSizeVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 8, 20, 1),
    _PacketprocessingPushbackQueueSizeVal_Type()
)
packetprocessingPushbackQueueSizeVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    packetprocessingPushbackQueueSizeVal.setStatus("obsolete")
_PacketprocessingPushbackQueueSizeMax_Type = CounterBasedGauge64
_PacketprocessingPushbackQueueSizeMax_Object = MibScalar
packetprocessingPushbackQueueSizeMax = _PacketprocessingPushbackQueueSizeMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 8, 20, 3),
    _PacketprocessingPushbackQueueSizeMax_Type()
)
packetprocessingPushbackQueueSizeMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    packetprocessingPushbackQueueSizeMax.setStatus("obsolete")
_PacketprocessingPushbackRequeues_ObjectIdentity = ObjectIdentity
packetprocessingPushbackRequeues = _PacketprocessingPushbackRequeues_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 8, 21)
)
_PacketprocessingPushbackRequeuesVal_Type = Counter64
_PacketprocessingPushbackRequeuesVal_Object = MibScalar
packetprocessingPushbackRequeuesVal = _PacketprocessingPushbackRequeuesVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 8, 21, 1),
    _PacketprocessingPushbackRequeuesVal_Type()
)
packetprocessingPushbackRequeuesVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    packetprocessingPushbackRequeuesVal.setStatus("obsolete")
_PacketprocessingPushbackRequeuesMom_Type = CounterBasedGauge64
_PacketprocessingPushbackRequeuesMom_Object = MibScalar
packetprocessingPushbackRequeuesMom = _PacketprocessingPushbackRequeuesMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 8, 21, 2),
    _PacketprocessingPushbackRequeuesMom_Type()
)
packetprocessingPushbackRequeuesMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    packetprocessingPushbackRequeuesMom.setStatus("obsolete")
_PacketprocessingPushbackRequeuesMax_Type = CounterBasedGauge64
_PacketprocessingPushbackRequeuesMax_Object = MibScalar
packetprocessingPushbackRequeuesMax = _PacketprocessingPushbackRequeuesMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 8, 21, 3),
    _PacketprocessingPushbackRequeuesMax_Type()
)
packetprocessingPushbackRequeuesMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    packetprocessingPushbackRequeuesMax.setStatus("obsolete")
_PacketprocessingBalancerDrops_ObjectIdentity = ObjectIdentity
packetprocessingBalancerDrops = _PacketprocessingBalancerDrops_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 8, 22)
)
_PacketprocessingBalancerDropsVal_Type = Counter64
_PacketprocessingBalancerDropsVal_Object = MibScalar
packetprocessingBalancerDropsVal = _PacketprocessingBalancerDropsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 8, 22, 1),
    _PacketprocessingBalancerDropsVal_Type()
)
packetprocessingBalancerDropsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    packetprocessingBalancerDropsVal.setStatus("current")
_PacketprocessingBalancerDropsMom_Type = CounterBasedGauge64
_PacketprocessingBalancerDropsMom_Object = MibScalar
packetprocessingBalancerDropsMom = _PacketprocessingBalancerDropsMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 8, 22, 2),
    _PacketprocessingBalancerDropsMom_Type()
)
packetprocessingBalancerDropsMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    packetprocessingBalancerDropsMom.setStatus("current")
_PacketprocessingBalancerDropsMax_Type = CounterBasedGauge64
_PacketprocessingBalancerDropsMax_Object = MibScalar
packetprocessingBalancerDropsMax = _PacketprocessingBalancerDropsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 8, 22, 3),
    _PacketprocessingBalancerDropsMax_Type()
)
packetprocessingBalancerDropsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    packetprocessingBalancerDropsMax.setStatus("current")
_PacketprocessingNICRXDrops_ObjectIdentity = ObjectIdentity
packetprocessingNICRXDrops = _PacketprocessingNICRXDrops_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 8, 23)
)
_PacketprocessingNICRXDropsVal_Type = Counter64
_PacketprocessingNICRXDropsVal_Object = MibScalar
packetprocessingNICRXDropsVal = _PacketprocessingNICRXDropsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 8, 23, 1),
    _PacketprocessingNICRXDropsVal_Type()
)
packetprocessingNICRXDropsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    packetprocessingNICRXDropsVal.setStatus("current")
_PacketprocessingNICRXDropsMom_Type = CounterBasedGauge64
_PacketprocessingNICRXDropsMom_Object = MibScalar
packetprocessingNICRXDropsMom = _PacketprocessingNICRXDropsMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 8, 23, 2),
    _PacketprocessingNICRXDropsMom_Type()
)
packetprocessingNICRXDropsMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    packetprocessingNICRXDropsMom.setStatus("current")
_PacketprocessingNICRXDropsMax_Type = CounterBasedGauge64
_PacketprocessingNICRXDropsMax_Object = MibScalar
packetprocessingNICRXDropsMax = _PacketprocessingNICRXDropsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 8, 23, 3),
    _PacketprocessingNICRXDropsMax_Type()
)
packetprocessingNICRXDropsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    packetprocessingNICRXDropsMax.setStatus("current")
_PacketprocessingBalancerQueueLength_ObjectIdentity = ObjectIdentity
packetprocessingBalancerQueueLength = _PacketprocessingBalancerQueueLength_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 8, 24)
)
_PacketprocessingBalancerQueueLengthVal_Type = CounterBasedGauge64
_PacketprocessingBalancerQueueLengthVal_Object = MibScalar
packetprocessingBalancerQueueLengthVal = _PacketprocessingBalancerQueueLengthVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 8, 24, 1),
    _PacketprocessingBalancerQueueLengthVal_Type()
)
packetprocessingBalancerQueueLengthVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    packetprocessingBalancerQueueLengthVal.setStatus("current")
_PacketprocessingBalancerQueueLengthMax_Type = CounterBasedGauge64
_PacketprocessingBalancerQueueLengthMax_Object = MibScalar
packetprocessingBalancerQueueLengthMax = _PacketprocessingBalancerQueueLengthMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 8, 24, 3),
    _PacketprocessingBalancerQueueLengthMax_Type()
)
packetprocessingBalancerQueueLengthMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    packetprocessingBalancerQueueLengthMax.setStatus("current")
_PacketprocessingOverLoad_ObjectIdentity = ObjectIdentity
packetprocessingOverLoad = _PacketprocessingOverLoad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 8, 27)
)
_PacketprocessingOverLoadVal_Type = CounterBasedGauge64
_PacketprocessingOverLoadVal_Object = MibScalar
packetprocessingOverLoadVal = _PacketprocessingOverLoadVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 8, 27, 1),
    _PacketprocessingOverLoadVal_Type()
)
packetprocessingOverLoadVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    packetprocessingOverLoadVal.setStatus("current")
_PacketprocessingOverLoadMax_Type = CounterBasedGauge64
_PacketprocessingOverLoadMax_Object = MibScalar
packetprocessingOverLoadMax = _PacketprocessingOverLoadMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 8, 27, 3),
    _PacketprocessingOverLoadMax_Type()
)
packetprocessingOverLoadMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    packetprocessingOverLoadMax.setStatus("current")
_Drdl_ObjectIdentity = ObjectIdentity
drdl = _Drdl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 24)
)
_DrdlWaitingChildren_ObjectIdentity = ObjectIdentity
drdlWaitingChildren = _DrdlWaitingChildren_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 24, 1)
)
_DrdlWaitingChildrenVal_Type = CounterBasedGauge64
_DrdlWaitingChildrenVal_Object = MibScalar
drdlWaitingChildrenVal = _DrdlWaitingChildrenVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 24, 1, 1),
    _DrdlWaitingChildrenVal_Type()
)
drdlWaitingChildrenVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drdlWaitingChildrenVal.setStatus("current")
_DrdlWaitingChildrenMax_Type = CounterBasedGauge64
_DrdlWaitingChildrenMax_Object = MibScalar
drdlWaitingChildrenMax = _DrdlWaitingChildrenMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 24, 1, 3),
    _DrdlWaitingChildrenMax_Type()
)
drdlWaitingChildrenMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drdlWaitingChildrenMax.setStatus("current")
_DrdlAddedChildren_ObjectIdentity = ObjectIdentity
drdlAddedChildren = _DrdlAddedChildren_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 24, 2)
)
_DrdlAddedChildrenVal_Type = Counter64
_DrdlAddedChildrenVal_Object = MibScalar
drdlAddedChildrenVal = _DrdlAddedChildrenVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 24, 2, 1),
    _DrdlAddedChildrenVal_Type()
)
drdlAddedChildrenVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drdlAddedChildrenVal.setStatus("current")
_DrdlAddedChildrenMom_Type = CounterBasedGauge64
_DrdlAddedChildrenMom_Object = MibScalar
drdlAddedChildrenMom = _DrdlAddedChildrenMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 24, 2, 2),
    _DrdlAddedChildrenMom_Type()
)
drdlAddedChildrenMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drdlAddedChildrenMom.setStatus("current")
_DrdlAddedChildrenMax_Type = CounterBasedGauge64
_DrdlAddedChildrenMax_Object = MibScalar
drdlAddedChildrenMax = _DrdlAddedChildrenMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 24, 2, 3),
    _DrdlAddedChildrenMax_Type()
)
drdlAddedChildrenMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drdlAddedChildrenMax.setStatus("current")
_DrdlChildAbuses_ObjectIdentity = ObjectIdentity
drdlChildAbuses = _DrdlChildAbuses_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 24, 3)
)
_DrdlChildAbusesVal_Type = Counter64
_DrdlChildAbusesVal_Object = MibScalar
drdlChildAbusesVal = _DrdlChildAbusesVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 24, 3, 1),
    _DrdlChildAbusesVal_Type()
)
drdlChildAbusesVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drdlChildAbusesVal.setStatus("current")
_DrdlChildAbusesMom_Type = CounterBasedGauge64
_DrdlChildAbusesMom_Object = MibScalar
drdlChildAbusesMom = _DrdlChildAbusesMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 24, 3, 2),
    _DrdlChildAbusesMom_Type()
)
drdlChildAbusesMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drdlChildAbusesMom.setStatus("current")
_DrdlChildAbusesMax_Type = CounterBasedGauge64
_DrdlChildAbusesMax_Object = MibScalar
drdlChildAbusesMax = _DrdlChildAbusesMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 24, 3, 3),
    _DrdlChildAbusesMax_Type()
)
drdlChildAbusesMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drdlChildAbusesMax.setStatus("current")
_DrdlChildEmpty_ObjectIdentity = ObjectIdentity
drdlChildEmpty = _DrdlChildEmpty_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 24, 4)
)
_DrdlChildEmptyVal_Type = Counter64
_DrdlChildEmptyVal_Object = MibScalar
drdlChildEmptyVal = _DrdlChildEmptyVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 24, 4, 1),
    _DrdlChildEmptyVal_Type()
)
drdlChildEmptyVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drdlChildEmptyVal.setStatus("current")
_DrdlChildEmptyMom_Type = CounterBasedGauge64
_DrdlChildEmptyMom_Object = MibScalar
drdlChildEmptyMom = _DrdlChildEmptyMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 24, 4, 2),
    _DrdlChildEmptyMom_Type()
)
drdlChildEmptyMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drdlChildEmptyMom.setStatus("current")
_DrdlChildEmptyMax_Type = CounterBasedGauge64
_DrdlChildEmptyMax_Object = MibScalar
drdlChildEmptyMax = _DrdlChildEmptyMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 24, 4, 3),
    _DrdlChildEmptyMax_Type()
)
drdlChildEmptyMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drdlChildEmptyMax.setStatus("current")
_DrdlProp32Fail_ObjectIdentity = ObjectIdentity
drdlProp32Fail = _DrdlProp32Fail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 24, 5)
)
_DrdlProp32FailVal_Type = Counter64
_DrdlProp32FailVal_Object = MibScalar
drdlProp32FailVal = _DrdlProp32FailVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 24, 5, 1),
    _DrdlProp32FailVal_Type()
)
drdlProp32FailVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drdlProp32FailVal.setStatus("current")
_DrdlProp32FailMom_Type = CounterBasedGauge64
_DrdlProp32FailMom_Object = MibScalar
drdlProp32FailMom = _DrdlProp32FailMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 24, 5, 2),
    _DrdlProp32FailMom_Type()
)
drdlProp32FailMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drdlProp32FailMom.setStatus("current")
_DrdlProp32FailMax_Type = CounterBasedGauge64
_DrdlProp32FailMax_Object = MibScalar
drdlProp32FailMax = _DrdlProp32FailMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 24, 5, 3),
    _DrdlProp32FailMax_Type()
)
drdlProp32FailMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drdlProp32FailMax.setStatus("current")
_DrdlProp64Fail_ObjectIdentity = ObjectIdentity
drdlProp64Fail = _DrdlProp64Fail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 24, 6)
)
_DrdlProp64FailVal_Type = Counter64
_DrdlProp64FailVal_Object = MibScalar
drdlProp64FailVal = _DrdlProp64FailVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 24, 6, 1),
    _DrdlProp64FailVal_Type()
)
drdlProp64FailVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drdlProp64FailVal.setStatus("obsolete")
_DrdlProp64FailMom_Type = CounterBasedGauge64
_DrdlProp64FailMom_Object = MibScalar
drdlProp64FailMom = _DrdlProp64FailMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 24, 6, 2),
    _DrdlProp64FailMom_Type()
)
drdlProp64FailMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drdlProp64FailMom.setStatus("obsolete")
_DrdlProp64FailMax_Type = CounterBasedGauge64
_DrdlProp64FailMax_Object = MibScalar
drdlProp64FailMax = _DrdlProp64FailMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 24, 6, 3),
    _DrdlProp64FailMax_Type()
)
drdlProp64FailMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drdlProp64FailMax.setStatus("obsolete")
_DrdlProp256Fail_ObjectIdentity = ObjectIdentity
drdlProp256Fail = _DrdlProp256Fail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 24, 7)
)
_DrdlProp256FailVal_Type = Counter64
_DrdlProp256FailVal_Object = MibScalar
drdlProp256FailVal = _DrdlProp256FailVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 24, 7, 1),
    _DrdlProp256FailVal_Type()
)
drdlProp256FailVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drdlProp256FailVal.setStatus("current")
_DrdlProp256FailMom_Type = CounterBasedGauge64
_DrdlProp256FailMom_Object = MibScalar
drdlProp256FailMom = _DrdlProp256FailMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 24, 7, 2),
    _DrdlProp256FailMom_Type()
)
drdlProp256FailMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drdlProp256FailMom.setStatus("current")
_DrdlProp256FailMax_Type = CounterBasedGauge64
_DrdlProp256FailMax_Object = MibScalar
drdlProp256FailMax = _DrdlProp256FailMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 24, 7, 3),
    _DrdlProp256FailMax_Type()
)
drdlProp256FailMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drdlProp256FailMax.setStatus("current")
_DrdlProp32Used_ObjectIdentity = ObjectIdentity
drdlProp32Used = _DrdlProp32Used_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 24, 8)
)
_DrdlProp32UsedVal_Type = CounterBasedGauge64
_DrdlProp32UsedVal_Object = MibScalar
drdlProp32UsedVal = _DrdlProp32UsedVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 24, 8, 1),
    _DrdlProp32UsedVal_Type()
)
drdlProp32UsedVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drdlProp32UsedVal.setStatus("current")
_DrdlProp32UsedMax_Type = CounterBasedGauge64
_DrdlProp32UsedMax_Object = MibScalar
drdlProp32UsedMax = _DrdlProp32UsedMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 24, 8, 3),
    _DrdlProp32UsedMax_Type()
)
drdlProp32UsedMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drdlProp32UsedMax.setStatus("current")
_DrdlProp64Used_ObjectIdentity = ObjectIdentity
drdlProp64Used = _DrdlProp64Used_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 24, 9)
)
_DrdlProp64UsedVal_Type = Counter64
_DrdlProp64UsedVal_Object = MibScalar
drdlProp64UsedVal = _DrdlProp64UsedVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 24, 9, 1),
    _DrdlProp64UsedVal_Type()
)
drdlProp64UsedVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drdlProp64UsedVal.setStatus("obsolete")
_DrdlProp64UsedMom_Type = CounterBasedGauge64
_DrdlProp64UsedMom_Object = MibScalar
drdlProp64UsedMom = _DrdlProp64UsedMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 24, 9, 2),
    _DrdlProp64UsedMom_Type()
)
drdlProp64UsedMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drdlProp64UsedMom.setStatus("obsolete")
_DrdlProp64UsedMax_Type = CounterBasedGauge64
_DrdlProp64UsedMax_Object = MibScalar
drdlProp64UsedMax = _DrdlProp64UsedMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 24, 9, 3),
    _DrdlProp64UsedMax_Type()
)
drdlProp64UsedMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drdlProp64UsedMax.setStatus("obsolete")
_DrdlProp256Used_ObjectIdentity = ObjectIdentity
drdlProp256Used = _DrdlProp256Used_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 24, 10)
)
_DrdlProp256UsedVal_Type = CounterBasedGauge64
_DrdlProp256UsedVal_Object = MibScalar
drdlProp256UsedVal = _DrdlProp256UsedVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 24, 10, 1),
    _DrdlProp256UsedVal_Type()
)
drdlProp256UsedVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drdlProp256UsedVal.setStatus("current")
_DrdlProp256UsedMax_Type = CounterBasedGauge64
_DrdlProp256UsedMax_Object = MibScalar
drdlProp256UsedMax = _DrdlProp256UsedMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 24, 10, 3),
    _DrdlProp256UsedMax_Type()
)
drdlProp256UsedMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drdlProp256UsedMax.setStatus("current")
_DrdlAnalyzerChecks_ObjectIdentity = ObjectIdentity
drdlAnalyzerChecks = _DrdlAnalyzerChecks_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 24, 11)
)
_DrdlAnalyzerChecksVal_Type = Counter64
_DrdlAnalyzerChecksVal_Object = MibScalar
drdlAnalyzerChecksVal = _DrdlAnalyzerChecksVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 24, 11, 1),
    _DrdlAnalyzerChecksVal_Type()
)
drdlAnalyzerChecksVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drdlAnalyzerChecksVal.setStatus("current")
_DrdlAnalyzerChecksMom_Type = CounterBasedGauge64
_DrdlAnalyzerChecksMom_Object = MibScalar
drdlAnalyzerChecksMom = _DrdlAnalyzerChecksMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 24, 11, 2),
    _DrdlAnalyzerChecksMom_Type()
)
drdlAnalyzerChecksMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drdlAnalyzerChecksMom.setStatus("current")
_DrdlAnalyzerChecksMax_Type = CounterBasedGauge64
_DrdlAnalyzerChecksMax_Object = MibScalar
drdlAnalyzerChecksMax = _DrdlAnalyzerChecksMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 24, 11, 3),
    _DrdlAnalyzerChecksMax_Type()
)
drdlAnalyzerChecksMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drdlAnalyzerChecksMax.setStatus("current")
_DrdlAnalyzerCheckedBytes_ObjectIdentity = ObjectIdentity
drdlAnalyzerCheckedBytes = _DrdlAnalyzerCheckedBytes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 24, 12)
)
_DrdlAnalyzerCheckedBytesVal_Type = Counter64
_DrdlAnalyzerCheckedBytesVal_Object = MibScalar
drdlAnalyzerCheckedBytesVal = _DrdlAnalyzerCheckedBytesVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 24, 12, 1),
    _DrdlAnalyzerCheckedBytesVal_Type()
)
drdlAnalyzerCheckedBytesVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drdlAnalyzerCheckedBytesVal.setStatus("current")
_DrdlAnalyzerCheckedBytesMom_Type = CounterBasedGauge64
_DrdlAnalyzerCheckedBytesMom_Object = MibScalar
drdlAnalyzerCheckedBytesMom = _DrdlAnalyzerCheckedBytesMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 24, 12, 2),
    _DrdlAnalyzerCheckedBytesMom_Type()
)
drdlAnalyzerCheckedBytesMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drdlAnalyzerCheckedBytesMom.setStatus("current")
_DrdlAnalyzerCheckedBytesMax_Type = CounterBasedGauge64
_DrdlAnalyzerCheckedBytesMax_Object = MibScalar
drdlAnalyzerCheckedBytesMax = _DrdlAnalyzerCheckedBytesMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 24, 12, 3),
    _DrdlAnalyzerCheckedBytesMax_Type()
)
drdlAnalyzerCheckedBytesMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drdlAnalyzerCheckedBytesMax.setStatus("current")
_DrdlAnalyzerSkippedBytes_ObjectIdentity = ObjectIdentity
drdlAnalyzerSkippedBytes = _DrdlAnalyzerSkippedBytes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 24, 13)
)
_DrdlAnalyzerSkippedBytesVal_Type = Counter64
_DrdlAnalyzerSkippedBytesVal_Object = MibScalar
drdlAnalyzerSkippedBytesVal = _DrdlAnalyzerSkippedBytesVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 24, 13, 1),
    _DrdlAnalyzerSkippedBytesVal_Type()
)
drdlAnalyzerSkippedBytesVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drdlAnalyzerSkippedBytesVal.setStatus("current")
_DrdlAnalyzerSkippedBytesMom_Type = CounterBasedGauge64
_DrdlAnalyzerSkippedBytesMom_Object = MibScalar
drdlAnalyzerSkippedBytesMom = _DrdlAnalyzerSkippedBytesMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 24, 13, 2),
    _DrdlAnalyzerSkippedBytesMom_Type()
)
drdlAnalyzerSkippedBytesMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drdlAnalyzerSkippedBytesMom.setStatus("current")
_DrdlAnalyzerSkippedBytesMax_Type = CounterBasedGauge64
_DrdlAnalyzerSkippedBytesMax_Object = MibScalar
drdlAnalyzerSkippedBytesMax = _DrdlAnalyzerSkippedBytesMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 24, 13, 3),
    _DrdlAnalyzerSkippedBytesMax_Type()
)
drdlAnalyzerSkippedBytesMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drdlAnalyzerSkippedBytesMax.setStatus("current")
_DrdlAnalyzerActions_ObjectIdentity = ObjectIdentity
drdlAnalyzerActions = _DrdlAnalyzerActions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 24, 14)
)
_DrdlAnalyzerActionsVal_Type = Counter64
_DrdlAnalyzerActionsVal_Object = MibScalar
drdlAnalyzerActionsVal = _DrdlAnalyzerActionsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 24, 14, 1),
    _DrdlAnalyzerActionsVal_Type()
)
drdlAnalyzerActionsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drdlAnalyzerActionsVal.setStatus("current")
_DrdlAnalyzerActionsMom_Type = CounterBasedGauge64
_DrdlAnalyzerActionsMom_Object = MibScalar
drdlAnalyzerActionsMom = _DrdlAnalyzerActionsMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 24, 14, 2),
    _DrdlAnalyzerActionsMom_Type()
)
drdlAnalyzerActionsMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drdlAnalyzerActionsMom.setStatus("current")
_DrdlAnalyzerActionsMax_Type = CounterBasedGauge64
_DrdlAnalyzerActionsMax_Object = MibScalar
drdlAnalyzerActionsMax = _DrdlAnalyzerActionsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 24, 14, 3),
    _DrdlAnalyzerActionsMax_Type()
)
drdlAnalyzerActionsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drdlAnalyzerActionsMax.setStatus("current")
_DrdlPropertySet_ObjectIdentity = ObjectIdentity
drdlPropertySet = _DrdlPropertySet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 24, 15)
)
_DrdlPropertySetVal_Type = Counter64
_DrdlPropertySetVal_Object = MibScalar
drdlPropertySetVal = _DrdlPropertySetVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 24, 15, 1),
    _DrdlPropertySetVal_Type()
)
drdlPropertySetVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drdlPropertySetVal.setStatus("current")
_DrdlPropertySetMom_Type = CounterBasedGauge64
_DrdlPropertySetMom_Object = MibScalar
drdlPropertySetMom = _DrdlPropertySetMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 24, 15, 2),
    _DrdlPropertySetMom_Type()
)
drdlPropertySetMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drdlPropertySetMom.setStatus("current")
_DrdlPropertySetMax_Type = CounterBasedGauge64
_DrdlPropertySetMax_Object = MibScalar
drdlPropertySetMax = _DrdlPropertySetMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 24, 15, 3),
    _DrdlPropertySetMax_Type()
)
drdlPropertySetMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drdlPropertySetMax.setStatus("current")
_DrdlOrphans_ObjectIdentity = ObjectIdentity
drdlOrphans = _DrdlOrphans_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 24, 18)
)
_DrdlOrphansVal_Type = Counter64
_DrdlOrphansVal_Object = MibScalar
drdlOrphansVal = _DrdlOrphansVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 24, 18, 1),
    _DrdlOrphansVal_Type()
)
drdlOrphansVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drdlOrphansVal.setStatus("current")
_DrdlOrphansMom_Type = CounterBasedGauge64
_DrdlOrphansMom_Object = MibScalar
drdlOrphansMom = _DrdlOrphansMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 24, 18, 2),
    _DrdlOrphansMom_Type()
)
drdlOrphansMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drdlOrphansMom.setStatus("current")
_DrdlOrphansMax_Type = CounterBasedGauge64
_DrdlOrphansMax_Object = MibScalar
drdlOrphansMax = _DrdlOrphansMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 24, 18, 3),
    _DrdlOrphansMax_Type()
)
drdlOrphansMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drdlOrphansMax.setStatus("current")
_DrdlAutoAccepts_ObjectIdentity = ObjectIdentity
drdlAutoAccepts = _DrdlAutoAccepts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 24, 21)
)
_DrdlAutoAcceptsVal_Type = Counter64
_DrdlAutoAcceptsVal_Object = MibScalar
drdlAutoAcceptsVal = _DrdlAutoAcceptsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 24, 21, 1),
    _DrdlAutoAcceptsVal_Type()
)
drdlAutoAcceptsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drdlAutoAcceptsVal.setStatus("current")
_DrdlAutoAcceptsMom_Type = CounterBasedGauge64
_DrdlAutoAcceptsMom_Object = MibScalar
drdlAutoAcceptsMom = _DrdlAutoAcceptsMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 24, 21, 2),
    _DrdlAutoAcceptsMom_Type()
)
drdlAutoAcceptsMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drdlAutoAcceptsMom.setStatus("current")
_DrdlAutoAcceptsMax_Type = CounterBasedGauge64
_DrdlAutoAcceptsMax_Object = MibScalar
drdlAutoAcceptsMax = _DrdlAutoAcceptsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 24, 21, 3),
    _DrdlAutoAcceptsMax_Type()
)
drdlAutoAcceptsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drdlAutoAcceptsMax.setStatus("current")
_DrdlBuffersUsed_ObjectIdentity = ObjectIdentity
drdlBuffersUsed = _DrdlBuffersUsed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 24, 22)
)
_DrdlBuffersUsedVal_Type = CounterBasedGauge64
_DrdlBuffersUsedVal_Object = MibScalar
drdlBuffersUsedVal = _DrdlBuffersUsedVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 24, 22, 1),
    _DrdlBuffersUsedVal_Type()
)
drdlBuffersUsedVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drdlBuffersUsedVal.setStatus("current")
_DrdlBuffersUsedMax_Type = CounterBasedGauge64
_DrdlBuffersUsedMax_Object = MibScalar
drdlBuffersUsedMax = _DrdlBuffersUsedMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 24, 22, 3),
    _DrdlBuffersUsedMax_Type()
)
drdlBuffersUsedMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drdlBuffersUsedMax.setStatus("current")
_DrdlBufferAllocationFailures_ObjectIdentity = ObjectIdentity
drdlBufferAllocationFailures = _DrdlBufferAllocationFailures_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 24, 23)
)
_DrdlBufferAllocationFailuresVal_Type = Counter64
_DrdlBufferAllocationFailuresVal_Object = MibScalar
drdlBufferAllocationFailuresVal = _DrdlBufferAllocationFailuresVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 24, 23, 1),
    _DrdlBufferAllocationFailuresVal_Type()
)
drdlBufferAllocationFailuresVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drdlBufferAllocationFailuresVal.setStatus("current")
_DrdlBufferAllocationFailuresMom_Type = CounterBasedGauge64
_DrdlBufferAllocationFailuresMom_Object = MibScalar
drdlBufferAllocationFailuresMom = _DrdlBufferAllocationFailuresMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 24, 23, 2),
    _DrdlBufferAllocationFailuresMom_Type()
)
drdlBufferAllocationFailuresMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drdlBufferAllocationFailuresMom.setStatus("current")
_DrdlBufferAllocationFailuresMax_Type = CounterBasedGauge64
_DrdlBufferAllocationFailuresMax_Object = MibScalar
drdlBufferAllocationFailuresMax = _DrdlBufferAllocationFailuresMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 24, 23, 3),
    _DrdlBufferAllocationFailuresMax_Type()
)
drdlBufferAllocationFailuresMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drdlBufferAllocationFailuresMax.setStatus("current")
_DrdlFullPackets_ObjectIdentity = ObjectIdentity
drdlFullPackets = _DrdlFullPackets_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 24, 24)
)
_DrdlFullPacketsVal_Type = Counter64
_DrdlFullPacketsVal_Object = MibScalar
drdlFullPacketsVal = _DrdlFullPacketsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 24, 24, 1),
    _DrdlFullPacketsVal_Type()
)
drdlFullPacketsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drdlFullPacketsVal.setStatus("current")
_DrdlFullPacketsMom_Type = CounterBasedGauge64
_DrdlFullPacketsMom_Object = MibScalar
drdlFullPacketsMom = _DrdlFullPacketsMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 24, 24, 2),
    _DrdlFullPacketsMom_Type()
)
drdlFullPacketsMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drdlFullPacketsMom.setStatus("current")
_DrdlFullPacketsMax_Type = CounterBasedGauge64
_DrdlFullPacketsMax_Object = MibScalar
drdlFullPacketsMax = _DrdlFullPacketsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 24, 24, 3),
    _DrdlFullPacketsMax_Type()
)
drdlFullPacketsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drdlFullPacketsMax.setStatus("current")
_DrdlProp0Fail_ObjectIdentity = ObjectIdentity
drdlProp0Fail = _DrdlProp0Fail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 24, 25)
)
_DrdlProp0FailVal_Type = CounterBasedGauge64
_DrdlProp0FailVal_Object = MibScalar
drdlProp0FailVal = _DrdlProp0FailVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 24, 25, 1),
    _DrdlProp0FailVal_Type()
)
drdlProp0FailVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drdlProp0FailVal.setStatus("obsolete")
_DrdlProp0FailMax_Type = CounterBasedGauge64
_DrdlProp0FailMax_Object = MibScalar
drdlProp0FailMax = _DrdlProp0FailMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 24, 25, 3),
    _DrdlProp0FailMax_Type()
)
drdlProp0FailMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drdlProp0FailMax.setStatus("obsolete")
_DrdlProp0Used_ObjectIdentity = ObjectIdentity
drdlProp0Used = _DrdlProp0Used_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 24, 26)
)
_DrdlProp0UsedVal_Type = CounterBasedGauge64
_DrdlProp0UsedVal_Object = MibScalar
drdlProp0UsedVal = _DrdlProp0UsedVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 24, 26, 1),
    _DrdlProp0UsedVal_Type()
)
drdlProp0UsedVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drdlProp0UsedVal.setStatus("obsolete")
_DrdlProp0UsedMax_Type = CounterBasedGauge64
_DrdlProp0UsedMax_Object = MibScalar
drdlProp0UsedMax = _DrdlProp0UsedMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 24, 26, 3),
    _DrdlProp0UsedMax_Type()
)
drdlProp0UsedMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drdlProp0UsedMax.setStatus("obsolete")
_DrdlSliceStateUsed_ObjectIdentity = ObjectIdentity
drdlSliceStateUsed = _DrdlSliceStateUsed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 24, 27)
)
_DrdlSliceStateUsedVal_Type = CounterBasedGauge64
_DrdlSliceStateUsedVal_Object = MibScalar
drdlSliceStateUsedVal = _DrdlSliceStateUsedVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 24, 27, 1),
    _DrdlSliceStateUsedVal_Type()
)
drdlSliceStateUsedVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drdlSliceStateUsedVal.setStatus("current")
_DrdlSliceStateUsedMax_Type = CounterBasedGauge64
_DrdlSliceStateUsedMax_Object = MibScalar
drdlSliceStateUsedMax = _DrdlSliceStateUsedMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 24, 27, 3),
    _DrdlSliceStateUsedMax_Type()
)
drdlSliceStateUsedMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drdlSliceStateUsedMax.setStatus("current")
_DrdlSliceStateFail_ObjectIdentity = ObjectIdentity
drdlSliceStateFail = _DrdlSliceStateFail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 24, 28)
)
_DrdlSliceStateFailVal_Type = Counter64
_DrdlSliceStateFailVal_Object = MibScalar
drdlSliceStateFailVal = _DrdlSliceStateFailVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 24, 28, 1),
    _DrdlSliceStateFailVal_Type()
)
drdlSliceStateFailVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drdlSliceStateFailVal.setStatus("current")
_DrdlSliceStateFailMom_Type = CounterBasedGauge64
_DrdlSliceStateFailMom_Object = MibScalar
drdlSliceStateFailMom = _DrdlSliceStateFailMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 24, 28, 2),
    _DrdlSliceStateFailMom_Type()
)
drdlSliceStateFailMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drdlSliceStateFailMom.setStatus("current")
_DrdlSliceStateFailMax_Type = CounterBasedGauge64
_DrdlSliceStateFailMax_Object = MibScalar
drdlSliceStateFailMax = _DrdlSliceStateFailMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 24, 28, 3),
    _DrdlSliceStateFailMax_Type()
)
drdlSliceStateFailMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drdlSliceStateFailMax.setStatus("current")
_DrdlLiteralSet_ObjectIdentity = ObjectIdentity
drdlLiteralSet = _DrdlLiteralSet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 24, 29)
)
_DrdlLiteralSetVal_Type = Counter64
_DrdlLiteralSetVal_Object = MibScalar
drdlLiteralSetVal = _DrdlLiteralSetVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 24, 29, 1),
    _DrdlLiteralSetVal_Type()
)
drdlLiteralSetVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drdlLiteralSetVal.setStatus("current")
_DrdlLiteralSetMom_Type = CounterBasedGauge64
_DrdlLiteralSetMom_Object = MibScalar
drdlLiteralSetMom = _DrdlLiteralSetMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 24, 29, 2),
    _DrdlLiteralSetMom_Type()
)
drdlLiteralSetMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drdlLiteralSetMom.setStatus("current")
_DrdlLiteralSetMax_Type = CounterBasedGauge64
_DrdlLiteralSetMax_Object = MibScalar
drdlLiteralSetMax = _DrdlLiteralSetMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 24, 29, 3),
    _DrdlLiteralSetMax_Type()
)
drdlLiteralSetMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drdlLiteralSetMax.setStatus("current")
_DrdlPropertyFail_ObjectIdentity = ObjectIdentity
drdlPropertyFail = _DrdlPropertyFail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 24, 30)
)
_DrdlPropertyFailVal_Type = Counter64
_DrdlPropertyFailVal_Object = MibScalar
drdlPropertyFailVal = _DrdlPropertyFailVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 24, 30, 1),
    _DrdlPropertyFailVal_Type()
)
drdlPropertyFailVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drdlPropertyFailVal.setStatus("current")
_DrdlPropertyFailMom_Type = CounterBasedGauge64
_DrdlPropertyFailMom_Object = MibScalar
drdlPropertyFailMom = _DrdlPropertyFailMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 24, 30, 2),
    _DrdlPropertyFailMom_Type()
)
drdlPropertyFailMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drdlPropertyFailMom.setStatus("current")
_DrdlPropertyFailMax_Type = CounterBasedGauge64
_DrdlPropertyFailMax_Object = MibScalar
drdlPropertyFailMax = _DrdlPropertyFailMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 24, 30, 3),
    _DrdlPropertyFailMax_Type()
)
drdlPropertyFailMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drdlPropertyFailMax.setStatus("current")
_DrdlChildIterateMax_ObjectIdentity = ObjectIdentity
drdlChildIterateMax = _DrdlChildIterateMax_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 24, 33)
)
_DrdlChildIterateMaxVal_Type = CounterBasedGauge64
_DrdlChildIterateMaxVal_Object = MibScalar
drdlChildIterateMaxVal = _DrdlChildIterateMaxVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 24, 33, 1),
    _DrdlChildIterateMaxVal_Type()
)
drdlChildIterateMaxVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drdlChildIterateMaxVal.setStatus("current")
_DrdlChildIterateMaxMax_Type = CounterBasedGauge64
_DrdlChildIterateMaxMax_Object = MibScalar
drdlChildIterateMaxMax = _DrdlChildIterateMaxMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 24, 33, 3),
    _DrdlChildIterateMaxMax_Type()
)
drdlChildIterateMaxMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drdlChildIterateMaxMax.setStatus("current")
_DrdlVsRangeTests_ObjectIdentity = ObjectIdentity
drdlVsRangeTests = _DrdlVsRangeTests_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 24, 45)
)
_DrdlVsRangeTestsVal_Type = Counter64
_DrdlVsRangeTestsVal_Object = MibScalar
drdlVsRangeTestsVal = _DrdlVsRangeTestsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 24, 45, 1),
    _DrdlVsRangeTestsVal_Type()
)
drdlVsRangeTestsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drdlVsRangeTestsVal.setStatus("current")
_DrdlVsRangeTestsMom_Type = CounterBasedGauge64
_DrdlVsRangeTestsMom_Object = MibScalar
drdlVsRangeTestsMom = _DrdlVsRangeTestsMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 24, 45, 2),
    _DrdlVsRangeTestsMom_Type()
)
drdlVsRangeTestsMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drdlVsRangeTestsMom.setStatus("current")
_DrdlVsRangeTestsMax_Type = CounterBasedGauge64
_DrdlVsRangeTestsMax_Object = MibScalar
drdlVsRangeTestsMax = _DrdlVsRangeTestsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 24, 45, 3),
    _DrdlVsRangeTestsMax_Type()
)
drdlVsRangeTestsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drdlVsRangeTestsMax.setStatus("current")
_DrdlVsRangeSteps_ObjectIdentity = ObjectIdentity
drdlVsRangeSteps = _DrdlVsRangeSteps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 24, 46)
)
_DrdlVsRangeStepsVal_Type = Counter64
_DrdlVsRangeStepsVal_Object = MibScalar
drdlVsRangeStepsVal = _DrdlVsRangeStepsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 24, 46, 1),
    _DrdlVsRangeStepsVal_Type()
)
drdlVsRangeStepsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drdlVsRangeStepsVal.setStatus("current")
_DrdlVsRangeStepsMom_Type = CounterBasedGauge64
_DrdlVsRangeStepsMom_Object = MibScalar
drdlVsRangeStepsMom = _DrdlVsRangeStepsMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 24, 46, 2),
    _DrdlVsRangeStepsMom_Type()
)
drdlVsRangeStepsMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drdlVsRangeStepsMom.setStatus("current")
_DrdlVsRangeStepsMax_Type = CounterBasedGauge64
_DrdlVsRangeStepsMax_Object = MibScalar
drdlVsRangeStepsMax = _DrdlVsRangeStepsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 24, 46, 3),
    _DrdlVsRangeStepsMax_Type()
)
drdlVsRangeStepsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drdlVsRangeStepsMax.setStatus("current")
_DrdlVsRegexTests_ObjectIdentity = ObjectIdentity
drdlVsRegexTests = _DrdlVsRegexTests_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 24, 47)
)
_DrdlVsRegexTestsVal_Type = Counter64
_DrdlVsRegexTestsVal_Object = MibScalar
drdlVsRegexTestsVal = _DrdlVsRegexTestsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 24, 47, 1),
    _DrdlVsRegexTestsVal_Type()
)
drdlVsRegexTestsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drdlVsRegexTestsVal.setStatus("current")
_DrdlVsRegexTestsMom_Type = CounterBasedGauge64
_DrdlVsRegexTestsMom_Object = MibScalar
drdlVsRegexTestsMom = _DrdlVsRegexTestsMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 24, 47, 2),
    _DrdlVsRegexTestsMom_Type()
)
drdlVsRegexTestsMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drdlVsRegexTestsMom.setStatus("current")
_DrdlVsRegexTestsMax_Type = CounterBasedGauge64
_DrdlVsRegexTestsMax_Object = MibScalar
drdlVsRegexTestsMax = _DrdlVsRegexTestsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 24, 47, 3),
    _DrdlVsRegexTestsMax_Type()
)
drdlVsRegexTestsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drdlVsRegexTestsMax.setStatus("current")
_DrdlVsRegexSteps_ObjectIdentity = ObjectIdentity
drdlVsRegexSteps = _DrdlVsRegexSteps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 24, 48)
)
_DrdlVsRegexStepsVal_Type = Counter64
_DrdlVsRegexStepsVal_Object = MibScalar
drdlVsRegexStepsVal = _DrdlVsRegexStepsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 24, 48, 1),
    _DrdlVsRegexStepsVal_Type()
)
drdlVsRegexStepsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drdlVsRegexStepsVal.setStatus("current")
_DrdlVsRegexStepsMom_Type = CounterBasedGauge64
_DrdlVsRegexStepsMom_Object = MibScalar
drdlVsRegexStepsMom = _DrdlVsRegexStepsMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 24, 48, 2),
    _DrdlVsRegexStepsMom_Type()
)
drdlVsRegexStepsMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drdlVsRegexStepsMom.setStatus("current")
_DrdlVsRegexStepsMax_Type = CounterBasedGauge64
_DrdlVsRegexStepsMax_Object = MibScalar
drdlVsRegexStepsMax = _DrdlVsRegexStepsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 24, 48, 3),
    _DrdlVsRegexStepsMax_Type()
)
drdlVsRegexStepsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drdlVsRegexStepsMax.setStatus("current")
_DrdlTaintFill_ObjectIdentity = ObjectIdentity
drdlTaintFill = _DrdlTaintFill_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 24, 49)
)
_DrdlTaintFillVal_Type = CounterBasedGauge64
_DrdlTaintFillVal_Object = MibScalar
drdlTaintFillVal = _DrdlTaintFillVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 24, 49, 1),
    _DrdlTaintFillVal_Type()
)
drdlTaintFillVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drdlTaintFillVal.setStatus("current")
_DrdlTaintFillMax_Type = CounterBasedGauge64
_DrdlTaintFillMax_Object = MibScalar
drdlTaintFillMax = _DrdlTaintFillMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 24, 49, 3),
    _DrdlTaintFillMax_Type()
)
drdlTaintFillMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drdlTaintFillMax.setStatus("current")
_DrdlTaintFillPercent_ObjectIdentity = ObjectIdentity
drdlTaintFillPercent = _DrdlTaintFillPercent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 24, 54)
)
_DrdlTaintFillPercentVal_Type = Unsigned32
_DrdlTaintFillPercentVal_Object = MibScalar
drdlTaintFillPercentVal = _DrdlTaintFillPercentVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 24, 54, 1),
    _DrdlTaintFillPercentVal_Type()
)
drdlTaintFillPercentVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drdlTaintFillPercentVal.setStatus("current")
_DrdlTaintFillPercentMax_Type = Unsigned32
_DrdlTaintFillPercentMax_Object = MibScalar
drdlTaintFillPercentMax = _DrdlTaintFillPercentMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 24, 54, 3),
    _DrdlTaintFillPercentMax_Type()
)
drdlTaintFillPercentMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drdlTaintFillPercentMax.setStatus("current")
_Ethernet_ObjectIdentity = ObjectIdentity
ethernet = _Ethernet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 28)
)
_EthernetUnicast_ObjectIdentity = ObjectIdentity
ethernetUnicast = _EthernetUnicast_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 28, 1)
)
_EthernetUnicastVal_Type = Counter64
_EthernetUnicastVal_Object = MibScalar
ethernetUnicastVal = _EthernetUnicastVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 28, 1, 1),
    _EthernetUnicastVal_Type()
)
ethernetUnicastVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetUnicastVal.setStatus("current")
_EthernetUnicastMom_Type = CounterBasedGauge64
_EthernetUnicastMom_Object = MibScalar
ethernetUnicastMom = _EthernetUnicastMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 28, 1, 2),
    _EthernetUnicastMom_Type()
)
ethernetUnicastMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetUnicastMom.setStatus("current")
_EthernetUnicastMax_Type = CounterBasedGauge64
_EthernetUnicastMax_Object = MibScalar
ethernetUnicastMax = _EthernetUnicastMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 28, 1, 3),
    _EthernetUnicastMax_Type()
)
ethernetUnicastMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetUnicastMax.setStatus("current")
_EthernetBroadcast_ObjectIdentity = ObjectIdentity
ethernetBroadcast = _EthernetBroadcast_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 28, 2)
)
_EthernetBroadcastVal_Type = Counter64
_EthernetBroadcastVal_Object = MibScalar
ethernetBroadcastVal = _EthernetBroadcastVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 28, 2, 1),
    _EthernetBroadcastVal_Type()
)
ethernetBroadcastVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetBroadcastVal.setStatus("current")
_EthernetBroadcastMom_Type = CounterBasedGauge64
_EthernetBroadcastMom_Object = MibScalar
ethernetBroadcastMom = _EthernetBroadcastMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 28, 2, 2),
    _EthernetBroadcastMom_Type()
)
ethernetBroadcastMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetBroadcastMom.setStatus("current")
_EthernetBroadcastMax_Type = CounterBasedGauge64
_EthernetBroadcastMax_Object = MibScalar
ethernetBroadcastMax = _EthernetBroadcastMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 28, 2, 3),
    _EthernetBroadcastMax_Type()
)
ethernetBroadcastMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetBroadcastMax.setStatus("current")
_EthernetMulticast_ObjectIdentity = ObjectIdentity
ethernetMulticast = _EthernetMulticast_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 28, 3)
)
_EthernetMulticastVal_Type = Counter64
_EthernetMulticastVal_Object = MibScalar
ethernetMulticastVal = _EthernetMulticastVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 28, 3, 1),
    _EthernetMulticastVal_Type()
)
ethernetMulticastVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetMulticastVal.setStatus("current")
_EthernetMulticastMom_Type = CounterBasedGauge64
_EthernetMulticastMom_Object = MibScalar
ethernetMulticastMom = _EthernetMulticastMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 28, 3, 2),
    _EthernetMulticastMom_Type()
)
ethernetMulticastMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetMulticastMom.setStatus("current")
_EthernetMulticastMax_Type = CounterBasedGauge64
_EthernetMulticastMax_Object = MibScalar
ethernetMulticastMax = _EthernetMulticastMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 28, 3, 3),
    _EthernetMulticastMax_Type()
)
ethernetMulticastMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetMulticastMax.setStatus("current")
_Ethernet8021q_ObjectIdentity = ObjectIdentity
ethernet8021q = _Ethernet8021q_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 28, 4)
)
_Ethernet8021qVal_Type = Counter64
_Ethernet8021qVal_Object = MibScalar
ethernet8021qVal = _Ethernet8021qVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 28, 4, 1),
    _Ethernet8021qVal_Type()
)
ethernet8021qVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernet8021qVal.setStatus("current")
_Ethernet8021qMom_Type = CounterBasedGauge64
_Ethernet8021qMom_Object = MibScalar
ethernet8021qMom = _Ethernet8021qMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 28, 4, 2),
    _Ethernet8021qMom_Type()
)
ethernet8021qMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernet8021qMom.setStatus("current")
_Ethernet8021qMax_Type = CounterBasedGauge64
_Ethernet8021qMax_Object = MibScalar
ethernet8021qMax = _Ethernet8021qMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 28, 4, 3),
    _Ethernet8021qMax_Type()
)
ethernet8021qMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernet8021qMax.setStatus("current")
_EthernetMpls_ObjectIdentity = ObjectIdentity
ethernetMpls = _EthernetMpls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 28, 5)
)
_EthernetMplsVal_Type = Counter64
_EthernetMplsVal_Object = MibScalar
ethernetMplsVal = _EthernetMplsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 28, 5, 1),
    _EthernetMplsVal_Type()
)
ethernetMplsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetMplsVal.setStatus("current")
_EthernetMplsMom_Type = CounterBasedGauge64
_EthernetMplsMom_Object = MibScalar
ethernetMplsMom = _EthernetMplsMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 28, 5, 2),
    _EthernetMplsMom_Type()
)
ethernetMplsMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetMplsMom.setStatus("current")
_EthernetMplsMax_Type = CounterBasedGauge64
_EthernetMplsMax_Object = MibScalar
ethernetMplsMax = _EthernetMplsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 28, 5, 3),
    _EthernetMplsMax_Type()
)
ethernetMplsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetMplsMax.setStatus("current")
_EthernetMplsOoh_ObjectIdentity = ObjectIdentity
ethernetMplsOoh = _EthernetMplsOoh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 28, 6)
)
_EthernetMplsOohVal_Type = Counter64
_EthernetMplsOohVal_Object = MibScalar
ethernetMplsOohVal = _EthernetMplsOohVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 28, 6, 1),
    _EthernetMplsOohVal_Type()
)
ethernetMplsOohVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetMplsOohVal.setStatus("current")
_EthernetMplsOohMom_Type = CounterBasedGauge64
_EthernetMplsOohMom_Object = MibScalar
ethernetMplsOohMom = _EthernetMplsOohMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 28, 6, 2),
    _EthernetMplsOohMom_Type()
)
ethernetMplsOohMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetMplsOohMom.setStatus("current")
_EthernetMplsOohMax_Type = CounterBasedGauge64
_EthernetMplsOohMax_Object = MibScalar
ethernetMplsOohMax = _EthernetMplsOohMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 28, 6, 3),
    _EthernetMplsOohMax_Type()
)
ethernetMplsOohMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetMplsOohMax.setStatus("current")
_EthernetNonIp_ObjectIdentity = ObjectIdentity
ethernetNonIp = _EthernetNonIp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 28, 7)
)
_EthernetNonIpVal_Type = Counter64
_EthernetNonIpVal_Object = MibScalar
ethernetNonIpVal = _EthernetNonIpVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 28, 7, 1),
    _EthernetNonIpVal_Type()
)
ethernetNonIpVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNonIpVal.setStatus("current")
_EthernetNonIpMom_Type = CounterBasedGauge64
_EthernetNonIpMom_Object = MibScalar
ethernetNonIpMom = _EthernetNonIpMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 28, 7, 2),
    _EthernetNonIpMom_Type()
)
ethernetNonIpMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNonIpMom.setStatus("current")
_EthernetNonIpMax_Type = CounterBasedGauge64
_EthernetNonIpMax_Object = MibScalar
ethernetNonIpMax = _EthernetNonIpMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 28, 7, 3),
    _EthernetNonIpMax_Type()
)
ethernetNonIpMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNonIpMax.setStatus("current")
_EthernetDivert_ObjectIdentity = ObjectIdentity
ethernetDivert = _EthernetDivert_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 28, 8)
)
_EthernetDivertVal_Type = Counter64
_EthernetDivertVal_Object = MibScalar
ethernetDivertVal = _EthernetDivertVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 28, 8, 1),
    _EthernetDivertVal_Type()
)
ethernetDivertVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetDivertVal.setStatus("current")
_EthernetDivertMom_Type = CounterBasedGauge64
_EthernetDivertMom_Object = MibScalar
ethernetDivertMom = _EthernetDivertMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 28, 8, 2),
    _EthernetDivertMom_Type()
)
ethernetDivertMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetDivertMom.setStatus("current")
_EthernetDivertMax_Type = CounterBasedGauge64
_EthernetDivertMax_Object = MibScalar
ethernetDivertMax = _EthernetDivertMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 28, 8, 3),
    _EthernetDivertMax_Type()
)
ethernetDivertMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetDivertMax.setStatus("current")
_EthernetHBResetDrops_ObjectIdentity = ObjectIdentity
ethernetHBResetDrops = _EthernetHBResetDrops_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 28, 21)
)
_EthernetHBResetDropsVal_Type = Counter64
_EthernetHBResetDropsVal_Object = MibScalar
ethernetHBResetDropsVal = _EthernetHBResetDropsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 28, 21, 1),
    _EthernetHBResetDropsVal_Type()
)
ethernetHBResetDropsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetHBResetDropsVal.setStatus("current")
_EthernetHBResetDropsMom_Type = CounterBasedGauge64
_EthernetHBResetDropsMom_Object = MibScalar
ethernetHBResetDropsMom = _EthernetHBResetDropsMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 28, 21, 2),
    _EthernetHBResetDropsMom_Type()
)
ethernetHBResetDropsMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetHBResetDropsMom.setStatus("current")
_EthernetHBResetDropsMax_Type = CounterBasedGauge64
_EthernetHBResetDropsMax_Object = MibScalar
ethernetHBResetDropsMax = _EthernetHBResetDropsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 28, 21, 3),
    _EthernetHBResetDropsMax_Type()
)
ethernetHBResetDropsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetHBResetDropsMax.setStatus("current")
_EthernetShuntEthertypePackets_ObjectIdentity = ObjectIdentity
ethernetShuntEthertypePackets = _EthernetShuntEthertypePackets_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 28, 22)
)
_EthernetShuntEthertypePacketsVal_Type = Counter64
_EthernetShuntEthertypePacketsVal_Object = MibScalar
ethernetShuntEthertypePacketsVal = _EthernetShuntEthertypePacketsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 28, 22, 1),
    _EthernetShuntEthertypePacketsVal_Type()
)
ethernetShuntEthertypePacketsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetShuntEthertypePacketsVal.setStatus("current")
_EthernetShuntEthertypePacketsMom_Type = CounterBasedGauge64
_EthernetShuntEthertypePacketsMom_Object = MibScalar
ethernetShuntEthertypePacketsMom = _EthernetShuntEthertypePacketsMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 28, 22, 2),
    _EthernetShuntEthertypePacketsMom_Type()
)
ethernetShuntEthertypePacketsMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetShuntEthertypePacketsMom.setStatus("current")
_EthernetShuntEthertypePacketsMax_Type = CounterBasedGauge64
_EthernetShuntEthertypePacketsMax_Object = MibScalar
ethernetShuntEthertypePacketsMax = _EthernetShuntEthertypePacketsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 28, 22, 3),
    _EthernetShuntEthertypePacketsMax_Type()
)
ethernetShuntEthertypePacketsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetShuntEthertypePacketsMax.setStatus("current")
_EthernetShuntEthertypeBytes_ObjectIdentity = ObjectIdentity
ethernetShuntEthertypeBytes = _EthernetShuntEthertypeBytes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 28, 23)
)
_EthernetShuntEthertypeBytesVal_Type = Counter64
_EthernetShuntEthertypeBytesVal_Object = MibScalar
ethernetShuntEthertypeBytesVal = _EthernetShuntEthertypeBytesVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 28, 23, 1),
    _EthernetShuntEthertypeBytesVal_Type()
)
ethernetShuntEthertypeBytesVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetShuntEthertypeBytesVal.setStatus("current")
_EthernetShuntEthertypeBytesMom_Type = CounterBasedGauge64
_EthernetShuntEthertypeBytesMom_Object = MibScalar
ethernetShuntEthertypeBytesMom = _EthernetShuntEthertypeBytesMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 28, 23, 2),
    _EthernetShuntEthertypeBytesMom_Type()
)
ethernetShuntEthertypeBytesMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetShuntEthertypeBytesMom.setStatus("current")
_EthernetShuntEthertypeBytesMax_Type = CounterBasedGauge64
_EthernetShuntEthertypeBytesMax_Object = MibScalar
ethernetShuntEthertypeBytesMax = _EthernetShuntEthertypeBytesMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 28, 23, 3),
    _EthernetShuntEthertypeBytesMax_Type()
)
ethernetShuntEthertypeBytesMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetShuntEthertypeBytesMax.setStatus("current")
_EthernetShuntMplsPackets_ObjectIdentity = ObjectIdentity
ethernetShuntMplsPackets = _EthernetShuntMplsPackets_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 28, 24)
)
_EthernetShuntMplsPacketsVal_Type = Counter64
_EthernetShuntMplsPacketsVal_Object = MibScalar
ethernetShuntMplsPacketsVal = _EthernetShuntMplsPacketsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 28, 24, 1),
    _EthernetShuntMplsPacketsVal_Type()
)
ethernetShuntMplsPacketsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetShuntMplsPacketsVal.setStatus("current")
_EthernetShuntMplsPacketsMom_Type = CounterBasedGauge64
_EthernetShuntMplsPacketsMom_Object = MibScalar
ethernetShuntMplsPacketsMom = _EthernetShuntMplsPacketsMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 28, 24, 2),
    _EthernetShuntMplsPacketsMom_Type()
)
ethernetShuntMplsPacketsMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetShuntMplsPacketsMom.setStatus("current")
_EthernetShuntMplsPacketsMax_Type = CounterBasedGauge64
_EthernetShuntMplsPacketsMax_Object = MibScalar
ethernetShuntMplsPacketsMax = _EthernetShuntMplsPacketsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 28, 24, 3),
    _EthernetShuntMplsPacketsMax_Type()
)
ethernetShuntMplsPacketsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetShuntMplsPacketsMax.setStatus("current")
_EthernetShuntMplsBytes_ObjectIdentity = ObjectIdentity
ethernetShuntMplsBytes = _EthernetShuntMplsBytes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 28, 25)
)
_EthernetShuntMplsBytesVal_Type = Counter64
_EthernetShuntMplsBytesVal_Object = MibScalar
ethernetShuntMplsBytesVal = _EthernetShuntMplsBytesVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 28, 25, 1),
    _EthernetShuntMplsBytesVal_Type()
)
ethernetShuntMplsBytesVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetShuntMplsBytesVal.setStatus("current")
_EthernetShuntMplsBytesMom_Type = CounterBasedGauge64
_EthernetShuntMplsBytesMom_Object = MibScalar
ethernetShuntMplsBytesMom = _EthernetShuntMplsBytesMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 28, 25, 2),
    _EthernetShuntMplsBytesMom_Type()
)
ethernetShuntMplsBytesMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetShuntMplsBytesMom.setStatus("current")
_EthernetShuntMplsBytesMax_Type = CounterBasedGauge64
_EthernetShuntMplsBytesMax_Object = MibScalar
ethernetShuntMplsBytesMax = _EthernetShuntMplsBytesMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 28, 25, 3),
    _EthernetShuntMplsBytesMax_Type()
)
ethernetShuntMplsBytesMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetShuntMplsBytesMax.setStatus("current")
_EthernetShuntEoMplsPackets_ObjectIdentity = ObjectIdentity
ethernetShuntEoMplsPackets = _EthernetShuntEoMplsPackets_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 28, 26)
)
_EthernetShuntEoMplsPacketsVal_Type = Counter64
_EthernetShuntEoMplsPacketsVal_Object = MibScalar
ethernetShuntEoMplsPacketsVal = _EthernetShuntEoMplsPacketsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 28, 26, 1),
    _EthernetShuntEoMplsPacketsVal_Type()
)
ethernetShuntEoMplsPacketsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetShuntEoMplsPacketsVal.setStatus("current")
_EthernetShuntEoMplsPacketsMom_Type = CounterBasedGauge64
_EthernetShuntEoMplsPacketsMom_Object = MibScalar
ethernetShuntEoMplsPacketsMom = _EthernetShuntEoMplsPacketsMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 28, 26, 2),
    _EthernetShuntEoMplsPacketsMom_Type()
)
ethernetShuntEoMplsPacketsMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetShuntEoMplsPacketsMom.setStatus("current")
_EthernetShuntEoMplsPacketsMax_Type = CounterBasedGauge64
_EthernetShuntEoMplsPacketsMax_Object = MibScalar
ethernetShuntEoMplsPacketsMax = _EthernetShuntEoMplsPacketsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 28, 26, 3),
    _EthernetShuntEoMplsPacketsMax_Type()
)
ethernetShuntEoMplsPacketsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetShuntEoMplsPacketsMax.setStatus("current")
_EthernetShuntEoMplsBytes_ObjectIdentity = ObjectIdentity
ethernetShuntEoMplsBytes = _EthernetShuntEoMplsBytes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 28, 27)
)
_EthernetShuntEoMplsBytesVal_Type = Counter64
_EthernetShuntEoMplsBytesVal_Object = MibScalar
ethernetShuntEoMplsBytesVal = _EthernetShuntEoMplsBytesVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 28, 27, 1),
    _EthernetShuntEoMplsBytesVal_Type()
)
ethernetShuntEoMplsBytesVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetShuntEoMplsBytesVal.setStatus("current")
_EthernetShuntEoMplsBytesMom_Type = CounterBasedGauge64
_EthernetShuntEoMplsBytesMom_Object = MibScalar
ethernetShuntEoMplsBytesMom = _EthernetShuntEoMplsBytesMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 28, 27, 2),
    _EthernetShuntEoMplsBytesMom_Type()
)
ethernetShuntEoMplsBytesMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetShuntEoMplsBytesMom.setStatus("current")
_EthernetShuntEoMplsBytesMax_Type = CounterBasedGauge64
_EthernetShuntEoMplsBytesMax_Object = MibScalar
ethernetShuntEoMplsBytesMax = _EthernetShuntEoMplsBytesMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 28, 27, 3),
    _EthernetShuntEoMplsBytesMax_Type()
)
ethernetShuntEoMplsBytesMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetShuntEoMplsBytesMax.setStatus("current")
_EthernetShuntDot1qPackets_ObjectIdentity = ObjectIdentity
ethernetShuntDot1qPackets = _EthernetShuntDot1qPackets_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 28, 28)
)
_EthernetShuntDot1qPacketsVal_Type = Counter64
_EthernetShuntDot1qPacketsVal_Object = MibScalar
ethernetShuntDot1qPacketsVal = _EthernetShuntDot1qPacketsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 28, 28, 1),
    _EthernetShuntDot1qPacketsVal_Type()
)
ethernetShuntDot1qPacketsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetShuntDot1qPacketsVal.setStatus("current")
_EthernetShuntDot1qPacketsMom_Type = CounterBasedGauge64
_EthernetShuntDot1qPacketsMom_Object = MibScalar
ethernetShuntDot1qPacketsMom = _EthernetShuntDot1qPacketsMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 28, 28, 2),
    _EthernetShuntDot1qPacketsMom_Type()
)
ethernetShuntDot1qPacketsMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetShuntDot1qPacketsMom.setStatus("current")
_EthernetShuntDot1qPacketsMax_Type = CounterBasedGauge64
_EthernetShuntDot1qPacketsMax_Object = MibScalar
ethernetShuntDot1qPacketsMax = _EthernetShuntDot1qPacketsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 28, 28, 3),
    _EthernetShuntDot1qPacketsMax_Type()
)
ethernetShuntDot1qPacketsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetShuntDot1qPacketsMax.setStatus("current")
_EthernetShuntDot1qBytes_ObjectIdentity = ObjectIdentity
ethernetShuntDot1qBytes = _EthernetShuntDot1qBytes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 28, 29)
)
_EthernetShuntDot1qBytesVal_Type = Counter64
_EthernetShuntDot1qBytesVal_Object = MibScalar
ethernetShuntDot1qBytesVal = _EthernetShuntDot1qBytesVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 28, 29, 1),
    _EthernetShuntDot1qBytesVal_Type()
)
ethernetShuntDot1qBytesVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetShuntDot1qBytesVal.setStatus("current")
_EthernetShuntDot1qBytesMom_Type = CounterBasedGauge64
_EthernetShuntDot1qBytesMom_Object = MibScalar
ethernetShuntDot1qBytesMom = _EthernetShuntDot1qBytesMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 28, 29, 2),
    _EthernetShuntDot1qBytesMom_Type()
)
ethernetShuntDot1qBytesMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetShuntDot1qBytesMom.setStatus("current")
_EthernetShuntDot1qBytesMax_Type = CounterBasedGauge64
_EthernetShuntDot1qBytesMax_Object = MibScalar
ethernetShuntDot1qBytesMax = _EthernetShuntDot1qBytesMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 28, 29, 3),
    _EthernetShuntDot1qBytesMax_Type()
)
ethernetShuntDot1qBytesMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetShuntDot1qBytesMax.setStatus("current")
_EthernetCountBytesIPv4IPv6_ObjectIdentity = ObjectIdentity
ethernetCountBytesIPv4IPv6 = _EthernetCountBytesIPv4IPv6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 28, 30)
)
_EthernetCountBytesIPv4IPv6Val_Type = Counter64
_EthernetCountBytesIPv4IPv6Val_Object = MibScalar
ethernetCountBytesIPv4IPv6Val = _EthernetCountBytesIPv4IPv6Val_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 28, 30, 1),
    _EthernetCountBytesIPv4IPv6Val_Type()
)
ethernetCountBytesIPv4IPv6Val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetCountBytesIPv4IPv6Val.setStatus("current")
_EthernetCountBytesIPv4IPv6Mom_Type = CounterBasedGauge64
_EthernetCountBytesIPv4IPv6Mom_Object = MibScalar
ethernetCountBytesIPv4IPv6Mom = _EthernetCountBytesIPv4IPv6Mom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 28, 30, 2),
    _EthernetCountBytesIPv4IPv6Mom_Type()
)
ethernetCountBytesIPv4IPv6Mom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetCountBytesIPv4IPv6Mom.setStatus("current")
_EthernetCountBytesIPv4IPv6Max_Type = CounterBasedGauge64
_EthernetCountBytesIPv4IPv6Max_Object = MibScalar
ethernetCountBytesIPv4IPv6Max = _EthernetCountBytesIPv4IPv6Max_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 28, 30, 3),
    _EthernetCountBytesIPv4IPv6Max_Type()
)
ethernetCountBytesIPv4IPv6Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetCountBytesIPv4IPv6Max.setStatus("current")
_Ipv4_ObjectIdentity = ObjectIdentity
ipv4 = _Ipv4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 32)
)
_Ipv4Packets_ObjectIdentity = ObjectIdentity
ipv4Packets = _Ipv4Packets_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 32, 1)
)
_Ipv4PacketsVal_Type = Counter64
_Ipv4PacketsVal_Object = MibScalar
ipv4PacketsVal = _Ipv4PacketsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 32, 1, 1),
    _Ipv4PacketsVal_Type()
)
ipv4PacketsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv4PacketsVal.setStatus("current")
_Ipv4PacketsMom_Type = CounterBasedGauge64
_Ipv4PacketsMom_Object = MibScalar
ipv4PacketsMom = _Ipv4PacketsMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 32, 1, 2),
    _Ipv4PacketsMom_Type()
)
ipv4PacketsMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv4PacketsMom.setStatus("current")
_Ipv4PacketsMax_Type = CounterBasedGauge64
_Ipv4PacketsMax_Object = MibScalar
ipv4PacketsMax = _Ipv4PacketsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 32, 1, 3),
    _Ipv4PacketsMax_Type()
)
ipv4PacketsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv4PacketsMax.setStatus("current")
_Ipv4Bytes_ObjectIdentity = ObjectIdentity
ipv4Bytes = _Ipv4Bytes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 32, 2)
)
_Ipv4BytesVal_Type = Counter64
_Ipv4BytesVal_Object = MibScalar
ipv4BytesVal = _Ipv4BytesVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 32, 2, 1),
    _Ipv4BytesVal_Type()
)
ipv4BytesVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv4BytesVal.setStatus("current")
_Ipv4BytesMom_Type = CounterBasedGauge64
_Ipv4BytesMom_Object = MibScalar
ipv4BytesMom = _Ipv4BytesMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 32, 2, 2),
    _Ipv4BytesMom_Type()
)
ipv4BytesMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv4BytesMom.setStatus("current")
_Ipv4BytesMax_Type = CounterBasedGauge64
_Ipv4BytesMax_Object = MibScalar
ipv4BytesMax = _Ipv4BytesMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 32, 2, 3),
    _Ipv4BytesMax_Type()
)
ipv4BytesMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv4BytesMax.setStatus("current")
_Ipv4RefusedShort_ObjectIdentity = ObjectIdentity
ipv4RefusedShort = _Ipv4RefusedShort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 32, 3)
)
_Ipv4RefusedShortVal_Type = Counter64
_Ipv4RefusedShortVal_Object = MibScalar
ipv4RefusedShortVal = _Ipv4RefusedShortVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 32, 3, 1),
    _Ipv4RefusedShortVal_Type()
)
ipv4RefusedShortVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv4RefusedShortVal.setStatus("current")
_Ipv4RefusedShortMom_Type = CounterBasedGauge64
_Ipv4RefusedShortMom_Object = MibScalar
ipv4RefusedShortMom = _Ipv4RefusedShortMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 32, 3, 2),
    _Ipv4RefusedShortMom_Type()
)
ipv4RefusedShortMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv4RefusedShortMom.setStatus("current")
_Ipv4RefusedShortMax_Type = CounterBasedGauge64
_Ipv4RefusedShortMax_Object = MibScalar
ipv4RefusedShortMax = _Ipv4RefusedShortMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 32, 3, 3),
    _Ipv4RefusedShortMax_Type()
)
ipv4RefusedShortMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv4RefusedShortMax.setStatus("current")
_Ipv4RefusedVersion_ObjectIdentity = ObjectIdentity
ipv4RefusedVersion = _Ipv4RefusedVersion_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 32, 4)
)
_Ipv4RefusedVersionVal_Type = Counter64
_Ipv4RefusedVersionVal_Object = MibScalar
ipv4RefusedVersionVal = _Ipv4RefusedVersionVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 32, 4, 1),
    _Ipv4RefusedVersionVal_Type()
)
ipv4RefusedVersionVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv4RefusedVersionVal.setStatus("current")
_Ipv4RefusedVersionMom_Type = CounterBasedGauge64
_Ipv4RefusedVersionMom_Object = MibScalar
ipv4RefusedVersionMom = _Ipv4RefusedVersionMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 32, 4, 2),
    _Ipv4RefusedVersionMom_Type()
)
ipv4RefusedVersionMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv4RefusedVersionMom.setStatus("current")
_Ipv4RefusedVersionMax_Type = CounterBasedGauge64
_Ipv4RefusedVersionMax_Object = MibScalar
ipv4RefusedVersionMax = _Ipv4RefusedVersionMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 32, 4, 3),
    _Ipv4RefusedVersionMax_Type()
)
ipv4RefusedVersionMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv4RefusedVersionMax.setStatus("current")
_Ipv4RefusedSelf_ObjectIdentity = ObjectIdentity
ipv4RefusedSelf = _Ipv4RefusedSelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 32, 5)
)
_Ipv4RefusedSelfVal_Type = Counter64
_Ipv4RefusedSelfVal_Object = MibScalar
ipv4RefusedSelfVal = _Ipv4RefusedSelfVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 32, 5, 1),
    _Ipv4RefusedSelfVal_Type()
)
ipv4RefusedSelfVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv4RefusedSelfVal.setStatus("current")
_Ipv4RefusedSelfMom_Type = CounterBasedGauge64
_Ipv4RefusedSelfMom_Object = MibScalar
ipv4RefusedSelfMom = _Ipv4RefusedSelfMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 32, 5, 2),
    _Ipv4RefusedSelfMom_Type()
)
ipv4RefusedSelfMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv4RefusedSelfMom.setStatus("current")
_Ipv4RefusedSelfMax_Type = CounterBasedGauge64
_Ipv4RefusedSelfMax_Object = MibScalar
ipv4RefusedSelfMax = _Ipv4RefusedSelfMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 32, 5, 3),
    _Ipv4RefusedSelfMax_Type()
)
ipv4RefusedSelfMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv4RefusedSelfMax.setStatus("current")
_Ipv4Unfragmented_ObjectIdentity = ObjectIdentity
ipv4Unfragmented = _Ipv4Unfragmented_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 32, 6)
)
_Ipv4UnfragmentedVal_Type = Counter64
_Ipv4UnfragmentedVal_Object = MibScalar
ipv4UnfragmentedVal = _Ipv4UnfragmentedVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 32, 6, 1),
    _Ipv4UnfragmentedVal_Type()
)
ipv4UnfragmentedVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv4UnfragmentedVal.setStatus("current")
_Ipv4UnfragmentedMom_Type = CounterBasedGauge64
_Ipv4UnfragmentedMom_Object = MibScalar
ipv4UnfragmentedMom = _Ipv4UnfragmentedMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 32, 6, 2),
    _Ipv4UnfragmentedMom_Type()
)
ipv4UnfragmentedMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv4UnfragmentedMom.setStatus("current")
_Ipv4UnfragmentedMax_Type = CounterBasedGauge64
_Ipv4UnfragmentedMax_Object = MibScalar
ipv4UnfragmentedMax = _Ipv4UnfragmentedMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 32, 6, 3),
    _Ipv4UnfragmentedMax_Type()
)
ipv4UnfragmentedMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv4UnfragmentedMax.setStatus("current")
_Ipv4Fragmented_ObjectIdentity = ObjectIdentity
ipv4Fragmented = _Ipv4Fragmented_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 32, 7)
)
_Ipv4FragmentedVal_Type = Counter64
_Ipv4FragmentedVal_Object = MibScalar
ipv4FragmentedVal = _Ipv4FragmentedVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 32, 7, 1),
    _Ipv4FragmentedVal_Type()
)
ipv4FragmentedVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv4FragmentedVal.setStatus("current")
_Ipv4FragmentedMom_Type = CounterBasedGauge64
_Ipv4FragmentedMom_Object = MibScalar
ipv4FragmentedMom = _Ipv4FragmentedMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 32, 7, 2),
    _Ipv4FragmentedMom_Type()
)
ipv4FragmentedMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv4FragmentedMom.setStatus("current")
_Ipv4FragmentedMax_Type = CounterBasedGauge64
_Ipv4FragmentedMax_Object = MibScalar
ipv4FragmentedMax = _Ipv4FragmentedMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 32, 7, 3),
    _Ipv4FragmentedMax_Type()
)
ipv4FragmentedMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv4FragmentedMax.setStatus("current")
_Ipv4FragmentedIds_ObjectIdentity = ObjectIdentity
ipv4FragmentedIds = _Ipv4FragmentedIds_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 32, 10)
)
_Ipv4FragmentedIdsVal_Type = CounterBasedGauge64
_Ipv4FragmentedIdsVal_Object = MibScalar
ipv4FragmentedIdsVal = _Ipv4FragmentedIdsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 32, 10, 1),
    _Ipv4FragmentedIdsVal_Type()
)
ipv4FragmentedIdsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv4FragmentedIdsVal.setStatus("current")
_Ipv4FragmentedIdsMax_Type = CounterBasedGauge64
_Ipv4FragmentedIdsMax_Object = MibScalar
ipv4FragmentedIdsMax = _Ipv4FragmentedIdsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 32, 10, 3),
    _Ipv4FragmentedIdsMax_Type()
)
ipv4FragmentedIdsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv4FragmentedIdsMax.setStatus("current")
_Ipv4Fragments_ObjectIdentity = ObjectIdentity
ipv4Fragments = _Ipv4Fragments_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 32, 11)
)
_Ipv4FragmentsVal_Type = CounterBasedGauge64
_Ipv4FragmentsVal_Object = MibScalar
ipv4FragmentsVal = _Ipv4FragmentsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 32, 11, 1),
    _Ipv4FragmentsVal_Type()
)
ipv4FragmentsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv4FragmentsVal.setStatus("current")
_Ipv4FragmentsMax_Type = CounterBasedGauge64
_Ipv4FragmentsMax_Object = MibScalar
ipv4FragmentsMax = _Ipv4FragmentsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 32, 11, 3),
    _Ipv4FragmentsMax_Type()
)
ipv4FragmentsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv4FragmentsMax.setStatus("current")
_Ipv4RefusedOof_ObjectIdentity = ObjectIdentity
ipv4RefusedOof = _Ipv4RefusedOof_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 32, 14)
)
_Ipv4RefusedOofVal_Type = Counter64
_Ipv4RefusedOofVal_Object = MibScalar
ipv4RefusedOofVal = _Ipv4RefusedOofVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 32, 14, 1),
    _Ipv4RefusedOofVal_Type()
)
ipv4RefusedOofVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv4RefusedOofVal.setStatus("current")
_Ipv4RefusedOofMom_Type = CounterBasedGauge64
_Ipv4RefusedOofMom_Object = MibScalar
ipv4RefusedOofMom = _Ipv4RefusedOofMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 32, 14, 2),
    _Ipv4RefusedOofMom_Type()
)
ipv4RefusedOofMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv4RefusedOofMom.setStatus("current")
_Ipv4RefusedOofMax_Type = CounterBasedGauge64
_Ipv4RefusedOofMax_Object = MibScalar
ipv4RefusedOofMax = _Ipv4RefusedOofMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 32, 14, 3),
    _Ipv4RefusedOofMax_Type()
)
ipv4RefusedOofMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv4RefusedOofMax.setStatus("current")
_Ipv4FragmentAllocationFailures_ObjectIdentity = ObjectIdentity
ipv4FragmentAllocationFailures = _Ipv4FragmentAllocationFailures_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 32, 15)
)
_Ipv4FragmentAllocationFailuresVal_Type = Counter64
_Ipv4FragmentAllocationFailuresVal_Object = MibScalar
ipv4FragmentAllocationFailuresVal = _Ipv4FragmentAllocationFailuresVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 32, 15, 1),
    _Ipv4FragmentAllocationFailuresVal_Type()
)
ipv4FragmentAllocationFailuresVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv4FragmentAllocationFailuresVal.setStatus("current")
_Ipv4FragmentAllocationFailuresMom_Type = CounterBasedGauge64
_Ipv4FragmentAllocationFailuresMom_Object = MibScalar
ipv4FragmentAllocationFailuresMom = _Ipv4FragmentAllocationFailuresMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 32, 15, 2),
    _Ipv4FragmentAllocationFailuresMom_Type()
)
ipv4FragmentAllocationFailuresMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv4FragmentAllocationFailuresMom.setStatus("current")
_Ipv4FragmentAllocationFailuresMax_Type = CounterBasedGauge64
_Ipv4FragmentAllocationFailuresMax_Object = MibScalar
ipv4FragmentAllocationFailuresMax = _Ipv4FragmentAllocationFailuresMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 32, 15, 3),
    _Ipv4FragmentAllocationFailuresMax_Type()
)
ipv4FragmentAllocationFailuresMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv4FragmentAllocationFailuresMax.setStatus("current")
_Ipv4FragmentReassFail_ObjectIdentity = ObjectIdentity
ipv4FragmentReassFail = _Ipv4FragmentReassFail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 32, 16)
)
_Ipv4FragmentReassFailVal_Type = Counter64
_Ipv4FragmentReassFailVal_Object = MibScalar
ipv4FragmentReassFailVal = _Ipv4FragmentReassFailVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 32, 16, 1),
    _Ipv4FragmentReassFailVal_Type()
)
ipv4FragmentReassFailVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv4FragmentReassFailVal.setStatus("current")
_Ipv4FragmentReassFailMom_Type = CounterBasedGauge64
_Ipv4FragmentReassFailMom_Object = MibScalar
ipv4FragmentReassFailMom = _Ipv4FragmentReassFailMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 32, 16, 2),
    _Ipv4FragmentReassFailMom_Type()
)
ipv4FragmentReassFailMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv4FragmentReassFailMom.setStatus("current")
_Ipv4FragmentReassFailMax_Type = CounterBasedGauge64
_Ipv4FragmentReassFailMax_Object = MibScalar
ipv4FragmentReassFailMax = _Ipv4FragmentReassFailMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 32, 16, 3),
    _Ipv4FragmentReassFailMax_Type()
)
ipv4FragmentReassFailMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv4FragmentReassFailMax.setStatus("current")
_Ipv4RefusedFilter_ObjectIdentity = ObjectIdentity
ipv4RefusedFilter = _Ipv4RefusedFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 32, 17)
)
_Ipv4RefusedFilterVal_Type = Counter64
_Ipv4RefusedFilterVal_Object = MibScalar
ipv4RefusedFilterVal = _Ipv4RefusedFilterVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 32, 17, 1),
    _Ipv4RefusedFilterVal_Type()
)
ipv4RefusedFilterVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv4RefusedFilterVal.setStatus("current")
_Ipv4RefusedFilterMom_Type = CounterBasedGauge64
_Ipv4RefusedFilterMom_Object = MibScalar
ipv4RefusedFilterMom = _Ipv4RefusedFilterMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 32, 17, 2),
    _Ipv4RefusedFilterMom_Type()
)
ipv4RefusedFilterMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv4RefusedFilterMom.setStatus("current")
_Ipv4RefusedFilterMax_Type = CounterBasedGauge64
_Ipv4RefusedFilterMax_Object = MibScalar
ipv4RefusedFilterMax = _Ipv4RefusedFilterMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 32, 17, 3),
    _Ipv4RefusedFilterMax_Type()
)
ipv4RefusedFilterMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv4RefusedFilterMax.setStatus("current")
_Ipv4FragmentTooNoisy_ObjectIdentity = ObjectIdentity
ipv4FragmentTooNoisy = _Ipv4FragmentTooNoisy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 32, 19)
)
_Ipv4FragmentTooNoisyVal_Type = Counter64
_Ipv4FragmentTooNoisyVal_Object = MibScalar
ipv4FragmentTooNoisyVal = _Ipv4FragmentTooNoisyVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 32, 19, 1),
    _Ipv4FragmentTooNoisyVal_Type()
)
ipv4FragmentTooNoisyVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv4FragmentTooNoisyVal.setStatus("current")
_Ipv4FragmentTooNoisyMom_Type = CounterBasedGauge64
_Ipv4FragmentTooNoisyMom_Object = MibScalar
ipv4FragmentTooNoisyMom = _Ipv4FragmentTooNoisyMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 32, 19, 2),
    _Ipv4FragmentTooNoisyMom_Type()
)
ipv4FragmentTooNoisyMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv4FragmentTooNoisyMom.setStatus("current")
_Ipv4FragmentTooNoisyMax_Type = CounterBasedGauge64
_Ipv4FragmentTooNoisyMax_Object = MibScalar
ipv4FragmentTooNoisyMax = _Ipv4FragmentTooNoisyMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 32, 19, 3),
    _Ipv4FragmentTooNoisyMax_Type()
)
ipv4FragmentTooNoisyMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv4FragmentTooNoisyMax.setStatus("current")
_Ipv4Reassembled_ObjectIdentity = ObjectIdentity
ipv4Reassembled = _Ipv4Reassembled_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 32, 20)
)
_Ipv4ReassembledVal_Type = Counter64
_Ipv4ReassembledVal_Object = MibScalar
ipv4ReassembledVal = _Ipv4ReassembledVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 32, 20, 1),
    _Ipv4ReassembledVal_Type()
)
ipv4ReassembledVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv4ReassembledVal.setStatus("current")
_Ipv4ReassembledMom_Type = CounterBasedGauge64
_Ipv4ReassembledMom_Object = MibScalar
ipv4ReassembledMom = _Ipv4ReassembledMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 32, 20, 2),
    _Ipv4ReassembledMom_Type()
)
ipv4ReassembledMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv4ReassembledMom.setStatus("current")
_Ipv4ReassembledMax_Type = CounterBasedGauge64
_Ipv4ReassembledMax_Object = MibScalar
ipv4ReassembledMax = _Ipv4ReassembledMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 32, 20, 3),
    _Ipv4ReassembledMax_Type()
)
ipv4ReassembledMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv4ReassembledMax.setStatus("current")
_Ipv4FragmentDrops_ObjectIdentity = ObjectIdentity
ipv4FragmentDrops = _Ipv4FragmentDrops_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 32, 21)
)
_Ipv4FragmentDropsVal_Type = Counter64
_Ipv4FragmentDropsVal_Object = MibScalar
ipv4FragmentDropsVal = _Ipv4FragmentDropsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 32, 21, 1),
    _Ipv4FragmentDropsVal_Type()
)
ipv4FragmentDropsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv4FragmentDropsVal.setStatus("current")
_Ipv4FragmentDropsMom_Type = CounterBasedGauge64
_Ipv4FragmentDropsMom_Object = MibScalar
ipv4FragmentDropsMom = _Ipv4FragmentDropsMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 32, 21, 2),
    _Ipv4FragmentDropsMom_Type()
)
ipv4FragmentDropsMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv4FragmentDropsMom.setStatus("current")
_Ipv4FragmentDropsMax_Type = CounterBasedGauge64
_Ipv4FragmentDropsMax_Object = MibScalar
ipv4FragmentDropsMax = _Ipv4FragmentDropsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 32, 21, 3),
    _Ipv4FragmentDropsMax_Type()
)
ipv4FragmentDropsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv4FragmentDropsMax.setStatus("current")
_Ipv4ShuntAddressPackets_ObjectIdentity = ObjectIdentity
ipv4ShuntAddressPackets = _Ipv4ShuntAddressPackets_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 32, 35)
)
_Ipv4ShuntAddressPacketsVal_Type = Counter64
_Ipv4ShuntAddressPacketsVal_Object = MibScalar
ipv4ShuntAddressPacketsVal = _Ipv4ShuntAddressPacketsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 32, 35, 1),
    _Ipv4ShuntAddressPacketsVal_Type()
)
ipv4ShuntAddressPacketsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv4ShuntAddressPacketsVal.setStatus("current")
_Ipv4ShuntAddressPacketsMom_Type = CounterBasedGauge64
_Ipv4ShuntAddressPacketsMom_Object = MibScalar
ipv4ShuntAddressPacketsMom = _Ipv4ShuntAddressPacketsMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 32, 35, 2),
    _Ipv4ShuntAddressPacketsMom_Type()
)
ipv4ShuntAddressPacketsMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv4ShuntAddressPacketsMom.setStatus("current")
_Ipv4ShuntAddressPacketsMax_Type = CounterBasedGauge64
_Ipv4ShuntAddressPacketsMax_Object = MibScalar
ipv4ShuntAddressPacketsMax = _Ipv4ShuntAddressPacketsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 32, 35, 3),
    _Ipv4ShuntAddressPacketsMax_Type()
)
ipv4ShuntAddressPacketsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv4ShuntAddressPacketsMax.setStatus("current")
_Ipv4ShuntAddressBytes_ObjectIdentity = ObjectIdentity
ipv4ShuntAddressBytes = _Ipv4ShuntAddressBytes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 32, 36)
)
_Ipv4ShuntAddressBytesVal_Type = Counter64
_Ipv4ShuntAddressBytesVal_Object = MibScalar
ipv4ShuntAddressBytesVal = _Ipv4ShuntAddressBytesVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 32, 36, 1),
    _Ipv4ShuntAddressBytesVal_Type()
)
ipv4ShuntAddressBytesVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv4ShuntAddressBytesVal.setStatus("current")
_Ipv4ShuntAddressBytesMom_Type = CounterBasedGauge64
_Ipv4ShuntAddressBytesMom_Object = MibScalar
ipv4ShuntAddressBytesMom = _Ipv4ShuntAddressBytesMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 32, 36, 2),
    _Ipv4ShuntAddressBytesMom_Type()
)
ipv4ShuntAddressBytesMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv4ShuntAddressBytesMom.setStatus("current")
_Ipv4ShuntAddressBytesMax_Type = CounterBasedGauge64
_Ipv4ShuntAddressBytesMax_Object = MibScalar
ipv4ShuntAddressBytesMax = _Ipv4ShuntAddressBytesMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 32, 36, 3),
    _Ipv4ShuntAddressBytesMax_Type()
)
ipv4ShuntAddressBytesMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv4ShuntAddressBytesMax.setStatus("current")
_Ipv4ShuntProtoPackets_ObjectIdentity = ObjectIdentity
ipv4ShuntProtoPackets = _Ipv4ShuntProtoPackets_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 32, 37)
)
_Ipv4ShuntProtoPacketsVal_Type = Counter64
_Ipv4ShuntProtoPacketsVal_Object = MibScalar
ipv4ShuntProtoPacketsVal = _Ipv4ShuntProtoPacketsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 32, 37, 1),
    _Ipv4ShuntProtoPacketsVal_Type()
)
ipv4ShuntProtoPacketsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv4ShuntProtoPacketsVal.setStatus("current")
_Ipv4ShuntProtoPacketsMom_Type = CounterBasedGauge64
_Ipv4ShuntProtoPacketsMom_Object = MibScalar
ipv4ShuntProtoPacketsMom = _Ipv4ShuntProtoPacketsMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 32, 37, 2),
    _Ipv4ShuntProtoPacketsMom_Type()
)
ipv4ShuntProtoPacketsMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv4ShuntProtoPacketsMom.setStatus("current")
_Ipv4ShuntProtoPacketsMax_Type = CounterBasedGauge64
_Ipv4ShuntProtoPacketsMax_Object = MibScalar
ipv4ShuntProtoPacketsMax = _Ipv4ShuntProtoPacketsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 32, 37, 3),
    _Ipv4ShuntProtoPacketsMax_Type()
)
ipv4ShuntProtoPacketsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv4ShuntProtoPacketsMax.setStatus("current")
_Ipv4ShuntProtoBytes_ObjectIdentity = ObjectIdentity
ipv4ShuntProtoBytes = _Ipv4ShuntProtoBytes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 32, 38)
)
_Ipv4ShuntProtoBytesVal_Type = Counter64
_Ipv4ShuntProtoBytesVal_Object = MibScalar
ipv4ShuntProtoBytesVal = _Ipv4ShuntProtoBytesVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 32, 38, 1),
    _Ipv4ShuntProtoBytesVal_Type()
)
ipv4ShuntProtoBytesVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv4ShuntProtoBytesVal.setStatus("current")
_Ipv4ShuntProtoBytesMom_Type = CounterBasedGauge64
_Ipv4ShuntProtoBytesMom_Object = MibScalar
ipv4ShuntProtoBytesMom = _Ipv4ShuntProtoBytesMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 32, 38, 2),
    _Ipv4ShuntProtoBytesMom_Type()
)
ipv4ShuntProtoBytesMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv4ShuntProtoBytesMom.setStatus("current")
_Ipv4ShuntProtoBytesMax_Type = CounterBasedGauge64
_Ipv4ShuntProtoBytesMax_Object = MibScalar
ipv4ShuntProtoBytesMax = _Ipv4ShuntProtoBytesMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 32, 38, 3),
    _Ipv4ShuntProtoBytesMax_Type()
)
ipv4ShuntProtoBytesMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv4ShuntProtoBytesMax.setStatus("current")
_Ipv4EcnEct0_ObjectIdentity = ObjectIdentity
ipv4EcnEct0 = _Ipv4EcnEct0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 32, 39)
)
_Ipv4EcnEct0Val_Type = Counter64
_Ipv4EcnEct0Val_Object = MibScalar
ipv4EcnEct0Val = _Ipv4EcnEct0Val_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 32, 39, 1),
    _Ipv4EcnEct0Val_Type()
)
ipv4EcnEct0Val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv4EcnEct0Val.setStatus("current")
_Ipv4EcnEct0Mom_Type = CounterBasedGauge64
_Ipv4EcnEct0Mom_Object = MibScalar
ipv4EcnEct0Mom = _Ipv4EcnEct0Mom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 32, 39, 2),
    _Ipv4EcnEct0Mom_Type()
)
ipv4EcnEct0Mom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv4EcnEct0Mom.setStatus("current")
_Ipv4EcnEct0Max_Type = CounterBasedGauge64
_Ipv4EcnEct0Max_Object = MibScalar
ipv4EcnEct0Max = _Ipv4EcnEct0Max_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 32, 39, 3),
    _Ipv4EcnEct0Max_Type()
)
ipv4EcnEct0Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv4EcnEct0Max.setStatus("current")
_Ipv4EcnEct1_ObjectIdentity = ObjectIdentity
ipv4EcnEct1 = _Ipv4EcnEct1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 32, 40)
)
_Ipv4EcnEct1Val_Type = Counter64
_Ipv4EcnEct1Val_Object = MibScalar
ipv4EcnEct1Val = _Ipv4EcnEct1Val_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 32, 40, 1),
    _Ipv4EcnEct1Val_Type()
)
ipv4EcnEct1Val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv4EcnEct1Val.setStatus("current")
_Ipv4EcnEct1Mom_Type = CounterBasedGauge64
_Ipv4EcnEct1Mom_Object = MibScalar
ipv4EcnEct1Mom = _Ipv4EcnEct1Mom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 32, 40, 2),
    _Ipv4EcnEct1Mom_Type()
)
ipv4EcnEct1Mom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv4EcnEct1Mom.setStatus("current")
_Ipv4EcnEct1Max_Type = CounterBasedGauge64
_Ipv4EcnEct1Max_Object = MibScalar
ipv4EcnEct1Max = _Ipv4EcnEct1Max_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 32, 40, 3),
    _Ipv4EcnEct1Max_Type()
)
ipv4EcnEct1Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv4EcnEct1Max.setStatus("current")
_Ipv4EcnCn_ObjectIdentity = ObjectIdentity
ipv4EcnCn = _Ipv4EcnCn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 32, 41)
)
_Ipv4EcnCnVal_Type = Counter64
_Ipv4EcnCnVal_Object = MibScalar
ipv4EcnCnVal = _Ipv4EcnCnVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 32, 41, 1),
    _Ipv4EcnCnVal_Type()
)
ipv4EcnCnVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv4EcnCnVal.setStatus("current")
_Ipv4EcnCnMom_Type = CounterBasedGauge64
_Ipv4EcnCnMom_Object = MibScalar
ipv4EcnCnMom = _Ipv4EcnCnMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 32, 41, 2),
    _Ipv4EcnCnMom_Type()
)
ipv4EcnCnMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv4EcnCnMom.setStatus("current")
_Ipv4EcnCnMax_Type = CounterBasedGauge64
_Ipv4EcnCnMax_Object = MibScalar
ipv4EcnCnMax = _Ipv4EcnCnMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 32, 41, 3),
    _Ipv4EcnCnMax_Type()
)
ipv4EcnCnMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv4EcnCnMax.setStatus("current")
_Tcpv4_ObjectIdentity = ObjectIdentity
tcpv4 = _Tcpv4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48)
)
_Tcpv4Packets_ObjectIdentity = ObjectIdentity
tcpv4Packets = _Tcpv4Packets_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 1)
)
_Tcpv4PacketsVal_Type = Counter64
_Tcpv4PacketsVal_Object = MibScalar
tcpv4PacketsVal = _Tcpv4PacketsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 1, 1),
    _Tcpv4PacketsVal_Type()
)
tcpv4PacketsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv4PacketsVal.setStatus("current")
_Tcpv4PacketsMom_Type = CounterBasedGauge64
_Tcpv4PacketsMom_Object = MibScalar
tcpv4PacketsMom = _Tcpv4PacketsMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 1, 2),
    _Tcpv4PacketsMom_Type()
)
tcpv4PacketsMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv4PacketsMom.setStatus("current")
_Tcpv4PacketsMax_Type = CounterBasedGauge64
_Tcpv4PacketsMax_Object = MibScalar
tcpv4PacketsMax = _Tcpv4PacketsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 1, 3),
    _Tcpv4PacketsMax_Type()
)
tcpv4PacketsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv4PacketsMax.setStatus("current")
_Tcpv4Bytes_ObjectIdentity = ObjectIdentity
tcpv4Bytes = _Tcpv4Bytes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 2)
)
_Tcpv4BytesVal_Type = Counter64
_Tcpv4BytesVal_Object = MibScalar
tcpv4BytesVal = _Tcpv4BytesVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 2, 1),
    _Tcpv4BytesVal_Type()
)
tcpv4BytesVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv4BytesVal.setStatus("current")
_Tcpv4BytesMom_Type = CounterBasedGauge64
_Tcpv4BytesMom_Object = MibScalar
tcpv4BytesMom = _Tcpv4BytesMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 2, 2),
    _Tcpv4BytesMom_Type()
)
tcpv4BytesMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv4BytesMom.setStatus("current")
_Tcpv4BytesMax_Type = CounterBasedGauge64
_Tcpv4BytesMax_Object = MibScalar
tcpv4BytesMax = _Tcpv4BytesMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 2, 3),
    _Tcpv4BytesMax_Type()
)
tcpv4BytesMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv4BytesMax.setStatus("current")
_Tcpv4CreateAttempts_ObjectIdentity = ObjectIdentity
tcpv4CreateAttempts = _Tcpv4CreateAttempts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 4)
)
_Tcpv4CreateAttemptsVal_Type = Counter64
_Tcpv4CreateAttemptsVal_Object = MibScalar
tcpv4CreateAttemptsVal = _Tcpv4CreateAttemptsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 4, 1),
    _Tcpv4CreateAttemptsVal_Type()
)
tcpv4CreateAttemptsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv4CreateAttemptsVal.setStatus("current")
_Tcpv4CreateAttemptsMom_Type = CounterBasedGauge64
_Tcpv4CreateAttemptsMom_Object = MibScalar
tcpv4CreateAttemptsMom = _Tcpv4CreateAttemptsMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 4, 2),
    _Tcpv4CreateAttemptsMom_Type()
)
tcpv4CreateAttemptsMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv4CreateAttemptsMom.setStatus("current")
_Tcpv4CreateAttemptsMax_Type = CounterBasedGauge64
_Tcpv4CreateAttemptsMax_Object = MibScalar
tcpv4CreateAttemptsMax = _Tcpv4CreateAttemptsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 4, 3),
    _Tcpv4CreateAttemptsMax_Type()
)
tcpv4CreateAttemptsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv4CreateAttemptsMax.setStatus("current")
_Tcpv4Created_ObjectIdentity = ObjectIdentity
tcpv4Created = _Tcpv4Created_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 5)
)
_Tcpv4CreatedVal_Type = Counter64
_Tcpv4CreatedVal_Object = MibScalar
tcpv4CreatedVal = _Tcpv4CreatedVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 5, 1),
    _Tcpv4CreatedVal_Type()
)
tcpv4CreatedVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv4CreatedVal.setStatus("current")
_Tcpv4CreatedMom_Type = CounterBasedGauge64
_Tcpv4CreatedMom_Object = MibScalar
tcpv4CreatedMom = _Tcpv4CreatedMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 5, 2),
    _Tcpv4CreatedMom_Type()
)
tcpv4CreatedMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv4CreatedMom.setStatus("current")
_Tcpv4CreatedMax_Type = CounterBasedGauge64
_Tcpv4CreatedMax_Object = MibScalar
tcpv4CreatedMax = _Tcpv4CreatedMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 5, 3),
    _Tcpv4CreatedMax_Type()
)
tcpv4CreatedMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv4CreatedMax.setStatus("current")
_Tcpv4RefusedRuleset_ObjectIdentity = ObjectIdentity
tcpv4RefusedRuleset = _Tcpv4RefusedRuleset_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 6)
)
_Tcpv4RefusedRulesetVal_Type = Counter64
_Tcpv4RefusedRulesetVal_Object = MibScalar
tcpv4RefusedRulesetVal = _Tcpv4RefusedRulesetVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 6, 1),
    _Tcpv4RefusedRulesetVal_Type()
)
tcpv4RefusedRulesetVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv4RefusedRulesetVal.setStatus("current")
_Tcpv4RefusedRulesetMom_Type = CounterBasedGauge64
_Tcpv4RefusedRulesetMom_Object = MibScalar
tcpv4RefusedRulesetMom = _Tcpv4RefusedRulesetMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 6, 2),
    _Tcpv4RefusedRulesetMom_Type()
)
tcpv4RefusedRulesetMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv4RefusedRulesetMom.setStatus("current")
_Tcpv4RefusedRulesetMax_Type = CounterBasedGauge64
_Tcpv4RefusedRulesetMax_Object = MibScalar
tcpv4RefusedRulesetMax = _Tcpv4RefusedRulesetMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 6, 3),
    _Tcpv4RefusedRulesetMax_Type()
)
tcpv4RefusedRulesetMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv4RefusedRulesetMax.setStatus("current")
_Tcpv4RefusedShort_ObjectIdentity = ObjectIdentity
tcpv4RefusedShort = _Tcpv4RefusedShort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 7)
)
_Tcpv4RefusedShortVal_Type = Counter64
_Tcpv4RefusedShortVal_Object = MibScalar
tcpv4RefusedShortVal = _Tcpv4RefusedShortVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 7, 1),
    _Tcpv4RefusedShortVal_Type()
)
tcpv4RefusedShortVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv4RefusedShortVal.setStatus("current")
_Tcpv4RefusedShortMom_Type = CounterBasedGauge64
_Tcpv4RefusedShortMom_Object = MibScalar
tcpv4RefusedShortMom = _Tcpv4RefusedShortMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 7, 2),
    _Tcpv4RefusedShortMom_Type()
)
tcpv4RefusedShortMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv4RefusedShortMom.setStatus("current")
_Tcpv4RefusedShortMax_Type = CounterBasedGauge64
_Tcpv4RefusedShortMax_Object = MibScalar
tcpv4RefusedShortMax = _Tcpv4RefusedShortMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 7, 3),
    _Tcpv4RefusedShortMax_Type()
)
tcpv4RefusedShortMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv4RefusedShortMax.setStatus("current")
_Tcpv4RefusedBroadcast_ObjectIdentity = ObjectIdentity
tcpv4RefusedBroadcast = _Tcpv4RefusedBroadcast_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 8)
)
_Tcpv4RefusedBroadcastVal_Type = Counter64
_Tcpv4RefusedBroadcastVal_Object = MibScalar
tcpv4RefusedBroadcastVal = _Tcpv4RefusedBroadcastVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 8, 1),
    _Tcpv4RefusedBroadcastVal_Type()
)
tcpv4RefusedBroadcastVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv4RefusedBroadcastVal.setStatus("current")
_Tcpv4RefusedBroadcastMom_Type = CounterBasedGauge64
_Tcpv4RefusedBroadcastMom_Object = MibScalar
tcpv4RefusedBroadcastMom = _Tcpv4RefusedBroadcastMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 8, 2),
    _Tcpv4RefusedBroadcastMom_Type()
)
tcpv4RefusedBroadcastMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv4RefusedBroadcastMom.setStatus("current")
_Tcpv4RefusedBroadcastMax_Type = CounterBasedGauge64
_Tcpv4RefusedBroadcastMax_Object = MibScalar
tcpv4RefusedBroadcastMax = _Tcpv4RefusedBroadcastMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 8, 3),
    _Tcpv4RefusedBroadcastMax_Type()
)
tcpv4RefusedBroadcastMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv4RefusedBroadcastMax.setStatus("current")
_Tcpv4RefusedOffset_ObjectIdentity = ObjectIdentity
tcpv4RefusedOffset = _Tcpv4RefusedOffset_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 9)
)
_Tcpv4RefusedOffsetVal_Type = Counter64
_Tcpv4RefusedOffsetVal_Object = MibScalar
tcpv4RefusedOffsetVal = _Tcpv4RefusedOffsetVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 9, 1),
    _Tcpv4RefusedOffsetVal_Type()
)
tcpv4RefusedOffsetVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv4RefusedOffsetVal.setStatus("current")
_Tcpv4RefusedOffsetMom_Type = CounterBasedGauge64
_Tcpv4RefusedOffsetMom_Object = MibScalar
tcpv4RefusedOffsetMom = _Tcpv4RefusedOffsetMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 9, 2),
    _Tcpv4RefusedOffsetMom_Type()
)
tcpv4RefusedOffsetMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv4RefusedOffsetMom.setStatus("current")
_Tcpv4RefusedOffsetMax_Type = CounterBasedGauge64
_Tcpv4RefusedOffsetMax_Object = MibScalar
tcpv4RefusedOffsetMax = _Tcpv4RefusedOffsetMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 9, 3),
    _Tcpv4RefusedOffsetMax_Type()
)
tcpv4RefusedOffsetMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv4RefusedOffsetMax.setStatus("current")
_Tcpv4Rejected_ObjectIdentity = ObjectIdentity
tcpv4Rejected = _Tcpv4Rejected_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 10)
)
_Tcpv4RejectedVal_Type = Counter64
_Tcpv4RejectedVal_Object = MibScalar
tcpv4RejectedVal = _Tcpv4RejectedVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 10, 1),
    _Tcpv4RejectedVal_Type()
)
tcpv4RejectedVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv4RejectedVal.setStatus("current")
_Tcpv4RejectedMom_Type = CounterBasedGauge64
_Tcpv4RejectedMom_Object = MibScalar
tcpv4RejectedMom = _Tcpv4RejectedMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 10, 2),
    _Tcpv4RejectedMom_Type()
)
tcpv4RejectedMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv4RejectedMom.setStatus("current")
_Tcpv4RejectedMax_Type = CounterBasedGauge64
_Tcpv4RejectedMax_Object = MibScalar
tcpv4RejectedMax = _Tcpv4RejectedMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 10, 3),
    _Tcpv4RejectedMax_Type()
)
tcpv4RejectedMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv4RejectedMax.setStatus("current")
_Tcpv4Lostsync_ObjectIdentity = ObjectIdentity
tcpv4Lostsync = _Tcpv4Lostsync_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 12)
)
_Tcpv4LostsyncVal_Type = CounterBasedGauge64
_Tcpv4LostsyncVal_Object = MibScalar
tcpv4LostsyncVal = _Tcpv4LostsyncVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 12, 1),
    _Tcpv4LostsyncVal_Type()
)
tcpv4LostsyncVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv4LostsyncVal.setStatus("current")
_Tcpv4LostsyncMax_Type = CounterBasedGauge64
_Tcpv4LostsyncMax_Object = MibScalar
tcpv4LostsyncMax = _Tcpv4LostsyncMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 12, 3),
    _Tcpv4LostsyncMax_Type()
)
tcpv4LostsyncMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv4LostsyncMax.setStatus("current")
_Tcpv4UntrackedPackets_ObjectIdentity = ObjectIdentity
tcpv4UntrackedPackets = _Tcpv4UntrackedPackets_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 13)
)
_Tcpv4UntrackedPacketsVal_Type = Counter64
_Tcpv4UntrackedPacketsVal_Object = MibScalar
tcpv4UntrackedPacketsVal = _Tcpv4UntrackedPacketsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 13, 1),
    _Tcpv4UntrackedPacketsVal_Type()
)
tcpv4UntrackedPacketsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv4UntrackedPacketsVal.setStatus("current")
_Tcpv4UntrackedPacketsMom_Type = CounterBasedGauge64
_Tcpv4UntrackedPacketsMom_Object = MibScalar
tcpv4UntrackedPacketsMom = _Tcpv4UntrackedPacketsMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 13, 2),
    _Tcpv4UntrackedPacketsMom_Type()
)
tcpv4UntrackedPacketsMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv4UntrackedPacketsMom.setStatus("current")
_Tcpv4UntrackedPacketsMax_Type = CounterBasedGauge64
_Tcpv4UntrackedPacketsMax_Object = MibScalar
tcpv4UntrackedPacketsMax = _Tcpv4UntrackedPacketsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 13, 3),
    _Tcpv4UntrackedPacketsMax_Type()
)
tcpv4UntrackedPacketsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv4UntrackedPacketsMax.setStatus("current")
_Tcpv4GoodputPackets_ObjectIdentity = ObjectIdentity
tcpv4GoodputPackets = _Tcpv4GoodputPackets_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 14)
)
_Tcpv4GoodputPacketsVal_Type = Counter64
_Tcpv4GoodputPacketsVal_Object = MibScalar
tcpv4GoodputPacketsVal = _Tcpv4GoodputPacketsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 14, 1),
    _Tcpv4GoodputPacketsVal_Type()
)
tcpv4GoodputPacketsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv4GoodputPacketsVal.setStatus("current")
_Tcpv4GoodputPacketsMom_Type = CounterBasedGauge64
_Tcpv4GoodputPacketsMom_Object = MibScalar
tcpv4GoodputPacketsMom = _Tcpv4GoodputPacketsMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 14, 2),
    _Tcpv4GoodputPacketsMom_Type()
)
tcpv4GoodputPacketsMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv4GoodputPacketsMom.setStatus("current")
_Tcpv4GoodputPacketsMax_Type = CounterBasedGauge64
_Tcpv4GoodputPacketsMax_Object = MibScalar
tcpv4GoodputPacketsMax = _Tcpv4GoodputPacketsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 14, 3),
    _Tcpv4GoodputPacketsMax_Type()
)
tcpv4GoodputPacketsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv4GoodputPacketsMax.setStatus("current")
_Tcpv4GoodputBytes_ObjectIdentity = ObjectIdentity
tcpv4GoodputBytes = _Tcpv4GoodputBytes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 15)
)
_Tcpv4GoodputBytesVal_Type = Counter64
_Tcpv4GoodputBytesVal_Object = MibScalar
tcpv4GoodputBytesVal = _Tcpv4GoodputBytesVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 15, 1),
    _Tcpv4GoodputBytesVal_Type()
)
tcpv4GoodputBytesVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv4GoodputBytesVal.setStatus("current")
_Tcpv4GoodputBytesMom_Type = CounterBasedGauge64
_Tcpv4GoodputBytesMom_Object = MibScalar
tcpv4GoodputBytesMom = _Tcpv4GoodputBytesMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 15, 2),
    _Tcpv4GoodputBytesMom_Type()
)
tcpv4GoodputBytesMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv4GoodputBytesMom.setStatus("current")
_Tcpv4GoodputBytesMax_Type = CounterBasedGauge64
_Tcpv4GoodputBytesMax_Object = MibScalar
tcpv4GoodputBytesMax = _Tcpv4GoodputBytesMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 15, 3),
    _Tcpv4GoodputBytesMax_Type()
)
tcpv4GoodputBytesMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv4GoodputBytesMax.setStatus("current")
_Tcpv4Segments_ObjectIdentity = ObjectIdentity
tcpv4Segments = _Tcpv4Segments_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 16)
)
_Tcpv4SegmentsVal_Type = CounterBasedGauge64
_Tcpv4SegmentsVal_Object = MibScalar
tcpv4SegmentsVal = _Tcpv4SegmentsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 16, 1),
    _Tcpv4SegmentsVal_Type()
)
tcpv4SegmentsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv4SegmentsVal.setStatus("current")
_Tcpv4SegmentsMax_Type = CounterBasedGauge64
_Tcpv4SegmentsMax_Object = MibScalar
tcpv4SegmentsMax = _Tcpv4SegmentsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 16, 3),
    _Tcpv4SegmentsMax_Type()
)
tcpv4SegmentsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv4SegmentsMax.setStatus("current")
_Tcpv4SegmentsPayload_ObjectIdentity = ObjectIdentity
tcpv4SegmentsPayload = _Tcpv4SegmentsPayload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 17)
)
_Tcpv4SegmentsPayloadVal_Type = CounterBasedGauge64
_Tcpv4SegmentsPayloadVal_Object = MibScalar
tcpv4SegmentsPayloadVal = _Tcpv4SegmentsPayloadVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 17, 1),
    _Tcpv4SegmentsPayloadVal_Type()
)
tcpv4SegmentsPayloadVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv4SegmentsPayloadVal.setStatus("current")
_Tcpv4SegmentsPayloadMax_Type = CounterBasedGauge64
_Tcpv4SegmentsPayloadMax_Object = MibScalar
tcpv4SegmentsPayloadMax = _Tcpv4SegmentsPayloadMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 17, 3),
    _Tcpv4SegmentsPayloadMax_Type()
)
tcpv4SegmentsPayloadMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv4SegmentsPayloadMax.setStatus("current")
_Tcpv4SegmentsDropped_ObjectIdentity = ObjectIdentity
tcpv4SegmentsDropped = _Tcpv4SegmentsDropped_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 18)
)
_Tcpv4SegmentsDroppedVal_Type = Counter64
_Tcpv4SegmentsDroppedVal_Object = MibScalar
tcpv4SegmentsDroppedVal = _Tcpv4SegmentsDroppedVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 18, 1),
    _Tcpv4SegmentsDroppedVal_Type()
)
tcpv4SegmentsDroppedVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv4SegmentsDroppedVal.setStatus("current")
_Tcpv4SegmentsDroppedMom_Type = CounterBasedGauge64
_Tcpv4SegmentsDroppedMom_Object = MibScalar
tcpv4SegmentsDroppedMom = _Tcpv4SegmentsDroppedMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 18, 2),
    _Tcpv4SegmentsDroppedMom_Type()
)
tcpv4SegmentsDroppedMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv4SegmentsDroppedMom.setStatus("current")
_Tcpv4SegmentsDroppedMax_Type = CounterBasedGauge64
_Tcpv4SegmentsDroppedMax_Object = MibScalar
tcpv4SegmentsDroppedMax = _Tcpv4SegmentsDroppedMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 18, 3),
    _Tcpv4SegmentsDroppedMax_Type()
)
tcpv4SegmentsDroppedMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv4SegmentsDroppedMax.setStatus("current")
_Tcpv4PacketAllocFail_ObjectIdentity = ObjectIdentity
tcpv4PacketAllocFail = _Tcpv4PacketAllocFail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 19)
)
_Tcpv4PacketAllocFailVal_Type = Counter64
_Tcpv4PacketAllocFailVal_Object = MibScalar
tcpv4PacketAllocFailVal = _Tcpv4PacketAllocFailVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 19, 1),
    _Tcpv4PacketAllocFailVal_Type()
)
tcpv4PacketAllocFailVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv4PacketAllocFailVal.setStatus("current")
_Tcpv4PacketAllocFailMom_Type = CounterBasedGauge64
_Tcpv4PacketAllocFailMom_Object = MibScalar
tcpv4PacketAllocFailMom = _Tcpv4PacketAllocFailMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 19, 2),
    _Tcpv4PacketAllocFailMom_Type()
)
tcpv4PacketAllocFailMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv4PacketAllocFailMom.setStatus("current")
_Tcpv4PacketAllocFailMax_Type = CounterBasedGauge64
_Tcpv4PacketAllocFailMax_Object = MibScalar
tcpv4PacketAllocFailMax = _Tcpv4PacketAllocFailMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 19, 3),
    _Tcpv4PacketAllocFailMax_Type()
)
tcpv4PacketAllocFailMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv4PacketAllocFailMax.setStatus("current")
_Tcpv4UntrackedGoodput_ObjectIdentity = ObjectIdentity
tcpv4UntrackedGoodput = _Tcpv4UntrackedGoodput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 23)
)
_Tcpv4UntrackedGoodputVal_Type = Counter64
_Tcpv4UntrackedGoodputVal_Object = MibScalar
tcpv4UntrackedGoodputVal = _Tcpv4UntrackedGoodputVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 23, 1),
    _Tcpv4UntrackedGoodputVal_Type()
)
tcpv4UntrackedGoodputVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv4UntrackedGoodputVal.setStatus("current")
_Tcpv4UntrackedGoodputMom_Type = CounterBasedGauge64
_Tcpv4UntrackedGoodputMom_Object = MibScalar
tcpv4UntrackedGoodputMom = _Tcpv4UntrackedGoodputMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 23, 2),
    _Tcpv4UntrackedGoodputMom_Type()
)
tcpv4UntrackedGoodputMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv4UntrackedGoodputMom.setStatus("current")
_Tcpv4UntrackedGoodputMax_Type = CounterBasedGauge64
_Tcpv4UntrackedGoodputMax_Object = MibScalar
tcpv4UntrackedGoodputMax = _Tcpv4UntrackedGoodputMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 23, 3),
    _Tcpv4UntrackedGoodputMax_Type()
)
tcpv4UntrackedGoodputMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv4UntrackedGoodputMax.setStatus("current")
_Tcpv4UntrackedBytes_ObjectIdentity = ObjectIdentity
tcpv4UntrackedBytes = _Tcpv4UntrackedBytes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 24)
)
_Tcpv4UntrackedBytesVal_Type = Counter64
_Tcpv4UntrackedBytesVal_Object = MibScalar
tcpv4UntrackedBytesVal = _Tcpv4UntrackedBytesVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 24, 1),
    _Tcpv4UntrackedBytesVal_Type()
)
tcpv4UntrackedBytesVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv4UntrackedBytesVal.setStatus("current")
_Tcpv4UntrackedBytesMom_Type = CounterBasedGauge64
_Tcpv4UntrackedBytesMom_Object = MibScalar
tcpv4UntrackedBytesMom = _Tcpv4UntrackedBytesMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 24, 2),
    _Tcpv4UntrackedBytesMom_Type()
)
tcpv4UntrackedBytesMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv4UntrackedBytesMom.setStatus("current")
_Tcpv4UntrackedBytesMax_Type = CounterBasedGauge64
_Tcpv4UntrackedBytesMax_Object = MibScalar
tcpv4UntrackedBytesMax = _Tcpv4UntrackedBytesMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 24, 3),
    _Tcpv4UntrackedBytesMax_Type()
)
tcpv4UntrackedBytesMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv4UntrackedBytesMax.setStatus("current")
_Tcpv4CorruptOptions_ObjectIdentity = ObjectIdentity
tcpv4CorruptOptions = _Tcpv4CorruptOptions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 25)
)
_Tcpv4CorruptOptionsVal_Type = Counter64
_Tcpv4CorruptOptionsVal_Object = MibScalar
tcpv4CorruptOptionsVal = _Tcpv4CorruptOptionsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 25, 1),
    _Tcpv4CorruptOptionsVal_Type()
)
tcpv4CorruptOptionsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv4CorruptOptionsVal.setStatus("current")
_Tcpv4CorruptOptionsMom_Type = CounterBasedGauge64
_Tcpv4CorruptOptionsMom_Object = MibScalar
tcpv4CorruptOptionsMom = _Tcpv4CorruptOptionsMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 25, 2),
    _Tcpv4CorruptOptionsMom_Type()
)
tcpv4CorruptOptionsMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv4CorruptOptionsMom.setStatus("current")
_Tcpv4CorruptOptionsMax_Type = CounterBasedGauge64
_Tcpv4CorruptOptionsMax_Object = MibScalar
tcpv4CorruptOptionsMax = _Tcpv4CorruptOptionsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 25, 3),
    _Tcpv4CorruptOptionsMax_Type()
)
tcpv4CorruptOptionsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv4CorruptOptionsMax.setStatus("current")
_Tcpv4CorruptConn_ObjectIdentity = ObjectIdentity
tcpv4CorruptConn = _Tcpv4CorruptConn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 26)
)
_Tcpv4CorruptConnVal_Type = Counter64
_Tcpv4CorruptConnVal_Object = MibScalar
tcpv4CorruptConnVal = _Tcpv4CorruptConnVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 26, 1),
    _Tcpv4CorruptConnVal_Type()
)
tcpv4CorruptConnVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv4CorruptConnVal.setStatus("current")
_Tcpv4CorruptConnMom_Type = CounterBasedGauge64
_Tcpv4CorruptConnMom_Object = MibScalar
tcpv4CorruptConnMom = _Tcpv4CorruptConnMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 26, 2),
    _Tcpv4CorruptConnMom_Type()
)
tcpv4CorruptConnMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv4CorruptConnMom.setStatus("current")
_Tcpv4CorruptConnMax_Type = CounterBasedGauge64
_Tcpv4CorruptConnMax_Object = MibScalar
tcpv4CorruptConnMax = _Tcpv4CorruptConnMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 26, 3),
    _Tcpv4CorruptConnMax_Type()
)
tcpv4CorruptConnMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv4CorruptConnMax.setStatus("current")
_Tcpv4SegmentedConnections_ObjectIdentity = ObjectIdentity
tcpv4SegmentedConnections = _Tcpv4SegmentedConnections_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 27)
)
_Tcpv4SegmentedConnectionsVal_Type = CounterBasedGauge64
_Tcpv4SegmentedConnectionsVal_Object = MibScalar
tcpv4SegmentedConnectionsVal = _Tcpv4SegmentedConnectionsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 27, 1),
    _Tcpv4SegmentedConnectionsVal_Type()
)
tcpv4SegmentedConnectionsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv4SegmentedConnectionsVal.setStatus("current")
_Tcpv4SegmentedConnectionsMax_Type = CounterBasedGauge64
_Tcpv4SegmentedConnectionsMax_Object = MibScalar
tcpv4SegmentedConnectionsMax = _Tcpv4SegmentedConnectionsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 27, 3),
    _Tcpv4SegmentedConnectionsMax_Type()
)
tcpv4SegmentedConnectionsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv4SegmentedConnectionsMax.setStatus("current")
_Tcpv4OutOfWindowPackets_ObjectIdentity = ObjectIdentity
tcpv4OutOfWindowPackets = _Tcpv4OutOfWindowPackets_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 28)
)
_Tcpv4OutOfWindowPacketsVal_Type = Counter64
_Tcpv4OutOfWindowPacketsVal_Object = MibScalar
tcpv4OutOfWindowPacketsVal = _Tcpv4OutOfWindowPacketsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 28, 1),
    _Tcpv4OutOfWindowPacketsVal_Type()
)
tcpv4OutOfWindowPacketsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv4OutOfWindowPacketsVal.setStatus("current")
_Tcpv4OutOfWindowPacketsMom_Type = CounterBasedGauge64
_Tcpv4OutOfWindowPacketsMom_Object = MibScalar
tcpv4OutOfWindowPacketsMom = _Tcpv4OutOfWindowPacketsMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 28, 2),
    _Tcpv4OutOfWindowPacketsMom_Type()
)
tcpv4OutOfWindowPacketsMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv4OutOfWindowPacketsMom.setStatus("current")
_Tcpv4OutOfWindowPacketsMax_Type = CounterBasedGauge64
_Tcpv4OutOfWindowPacketsMax_Object = MibScalar
tcpv4OutOfWindowPacketsMax = _Tcpv4OutOfWindowPacketsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 28, 3),
    _Tcpv4OutOfWindowPacketsMax_Type()
)
tcpv4OutOfWindowPacketsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv4OutOfWindowPacketsMax.setStatus("current")
_Tcpv4RefusedFilter_ObjectIdentity = ObjectIdentity
tcpv4RefusedFilter = _Tcpv4RefusedFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 29)
)
_Tcpv4RefusedFilterVal_Type = Counter64
_Tcpv4RefusedFilterVal_Object = MibScalar
tcpv4RefusedFilterVal = _Tcpv4RefusedFilterVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 29, 1),
    _Tcpv4RefusedFilterVal_Type()
)
tcpv4RefusedFilterVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv4RefusedFilterVal.setStatus("current")
_Tcpv4RefusedFilterMom_Type = CounterBasedGauge64
_Tcpv4RefusedFilterMom_Object = MibScalar
tcpv4RefusedFilterMom = _Tcpv4RefusedFilterMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 29, 2),
    _Tcpv4RefusedFilterMom_Type()
)
tcpv4RefusedFilterMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv4RefusedFilterMom.setStatus("current")
_Tcpv4RefusedFilterMax_Type = CounterBasedGauge64
_Tcpv4RefusedFilterMax_Object = MibScalar
tcpv4RefusedFilterMax = _Tcpv4RefusedFilterMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 29, 3),
    _Tcpv4RefusedFilterMax_Type()
)
tcpv4RefusedFilterMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv4RefusedFilterMax.setStatus("current")
_Tcpv4SynExisting_ObjectIdentity = ObjectIdentity
tcpv4SynExisting = _Tcpv4SynExisting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 32)
)
_Tcpv4SynExistingVal_Type = Counter64
_Tcpv4SynExistingVal_Object = MibScalar
tcpv4SynExistingVal = _Tcpv4SynExistingVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 32, 1),
    _Tcpv4SynExistingVal_Type()
)
tcpv4SynExistingVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv4SynExistingVal.setStatus("current")
_Tcpv4SynExistingMom_Type = CounterBasedGauge64
_Tcpv4SynExistingMom_Object = MibScalar
tcpv4SynExistingMom = _Tcpv4SynExistingMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 32, 2),
    _Tcpv4SynExistingMom_Type()
)
tcpv4SynExistingMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv4SynExistingMom.setStatus("current")
_Tcpv4SynExistingMax_Type = CounterBasedGauge64
_Tcpv4SynExistingMax_Object = MibScalar
tcpv4SynExistingMax = _Tcpv4SynExistingMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 32, 3),
    _Tcpv4SynExistingMax_Type()
)
tcpv4SynExistingMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv4SynExistingMax.setStatus("current")
_Tcpv4SegmentAllocFail_ObjectIdentity = ObjectIdentity
tcpv4SegmentAllocFail = _Tcpv4SegmentAllocFail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 33)
)
_Tcpv4SegmentAllocFailVal_Type = Counter64
_Tcpv4SegmentAllocFailVal_Object = MibScalar
tcpv4SegmentAllocFailVal = _Tcpv4SegmentAllocFailVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 33, 1),
    _Tcpv4SegmentAllocFailVal_Type()
)
tcpv4SegmentAllocFailVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv4SegmentAllocFailVal.setStatus("current")
_Tcpv4SegmentAllocFailMom_Type = CounterBasedGauge64
_Tcpv4SegmentAllocFailMom_Object = MibScalar
tcpv4SegmentAllocFailMom = _Tcpv4SegmentAllocFailMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 33, 2),
    _Tcpv4SegmentAllocFailMom_Type()
)
tcpv4SegmentAllocFailMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv4SegmentAllocFailMom.setStatus("current")
_Tcpv4SegmentAllocFailMax_Type = CounterBasedGauge64
_Tcpv4SegmentAllocFailMax_Object = MibScalar
tcpv4SegmentAllocFailMax = _Tcpv4SegmentAllocFailMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 33, 3),
    _Tcpv4SegmentAllocFailMax_Type()
)
tcpv4SegmentAllocFailMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv4SegmentAllocFailMax.setStatus("current")
_Tcpv4EnqueuedSegments_ObjectIdentity = ObjectIdentity
tcpv4EnqueuedSegments = _Tcpv4EnqueuedSegments_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 34)
)
_Tcpv4EnqueuedSegmentsVal_Type = Counter64
_Tcpv4EnqueuedSegmentsVal_Object = MibScalar
tcpv4EnqueuedSegmentsVal = _Tcpv4EnqueuedSegmentsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 34, 1),
    _Tcpv4EnqueuedSegmentsVal_Type()
)
tcpv4EnqueuedSegmentsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv4EnqueuedSegmentsVal.setStatus("current")
_Tcpv4EnqueuedSegmentsMom_Type = CounterBasedGauge64
_Tcpv4EnqueuedSegmentsMom_Object = MibScalar
tcpv4EnqueuedSegmentsMom = _Tcpv4EnqueuedSegmentsMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 34, 2),
    _Tcpv4EnqueuedSegmentsMom_Type()
)
tcpv4EnqueuedSegmentsMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv4EnqueuedSegmentsMom.setStatus("current")
_Tcpv4EnqueuedSegmentsMax_Type = CounterBasedGauge64
_Tcpv4EnqueuedSegmentsMax_Object = MibScalar
tcpv4EnqueuedSegmentsMax = _Tcpv4EnqueuedSegmentsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 34, 3),
    _Tcpv4EnqueuedSegmentsMax_Type()
)
tcpv4EnqueuedSegmentsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv4EnqueuedSegmentsMax.setStatus("current")
_Tcpv4DequeuedSegments_ObjectIdentity = ObjectIdentity
tcpv4DequeuedSegments = _Tcpv4DequeuedSegments_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 35)
)
_Tcpv4DequeuedSegmentsVal_Type = Counter64
_Tcpv4DequeuedSegmentsVal_Object = MibScalar
tcpv4DequeuedSegmentsVal = _Tcpv4DequeuedSegmentsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 35, 1),
    _Tcpv4DequeuedSegmentsVal_Type()
)
tcpv4DequeuedSegmentsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv4DequeuedSegmentsVal.setStatus("current")
_Tcpv4DequeuedSegmentsMom_Type = CounterBasedGauge64
_Tcpv4DequeuedSegmentsMom_Object = MibScalar
tcpv4DequeuedSegmentsMom = _Tcpv4DequeuedSegmentsMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 35, 2),
    _Tcpv4DequeuedSegmentsMom_Type()
)
tcpv4DequeuedSegmentsMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv4DequeuedSegmentsMom.setStatus("current")
_Tcpv4DequeuedSegmentsMax_Type = CounterBasedGauge64
_Tcpv4DequeuedSegmentsMax_Object = MibScalar
tcpv4DequeuedSegmentsMax = _Tcpv4DequeuedSegmentsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 35, 3),
    _Tcpv4DequeuedSegmentsMax_Type()
)
tcpv4DequeuedSegmentsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv4DequeuedSegmentsMax.setStatus("current")
_Tcpv4DiscardedSegments_ObjectIdentity = ObjectIdentity
tcpv4DiscardedSegments = _Tcpv4DiscardedSegments_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 36)
)
_Tcpv4DiscardedSegmentsVal_Type = Counter64
_Tcpv4DiscardedSegmentsVal_Object = MibScalar
tcpv4DiscardedSegmentsVal = _Tcpv4DiscardedSegmentsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 36, 1),
    _Tcpv4DiscardedSegmentsVal_Type()
)
tcpv4DiscardedSegmentsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv4DiscardedSegmentsVal.setStatus("current")
_Tcpv4DiscardedSegmentsMom_Type = CounterBasedGauge64
_Tcpv4DiscardedSegmentsMom_Object = MibScalar
tcpv4DiscardedSegmentsMom = _Tcpv4DiscardedSegmentsMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 36, 2),
    _Tcpv4DiscardedSegmentsMom_Type()
)
tcpv4DiscardedSegmentsMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv4DiscardedSegmentsMom.setStatus("current")
_Tcpv4DiscardedSegmentsMax_Type = CounterBasedGauge64
_Tcpv4DiscardedSegmentsMax_Object = MibScalar
tcpv4DiscardedSegmentsMax = _Tcpv4DiscardedSegmentsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 36, 3),
    _Tcpv4DiscardedSegmentsMax_Type()
)
tcpv4DiscardedSegmentsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv4DiscardedSegmentsMax.setStatus("current")
_Tcpv4EmptyPackets_ObjectIdentity = ObjectIdentity
tcpv4EmptyPackets = _Tcpv4EmptyPackets_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 37)
)
_Tcpv4EmptyPacketsVal_Type = Counter64
_Tcpv4EmptyPacketsVal_Object = MibScalar
tcpv4EmptyPacketsVal = _Tcpv4EmptyPacketsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 37, 1),
    _Tcpv4EmptyPacketsVal_Type()
)
tcpv4EmptyPacketsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv4EmptyPacketsVal.setStatus("current")
_Tcpv4EmptyPacketsMom_Type = CounterBasedGauge64
_Tcpv4EmptyPacketsMom_Object = MibScalar
tcpv4EmptyPacketsMom = _Tcpv4EmptyPacketsMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 37, 2),
    _Tcpv4EmptyPacketsMom_Type()
)
tcpv4EmptyPacketsMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv4EmptyPacketsMom.setStatus("current")
_Tcpv4EmptyPacketsMax_Type = CounterBasedGauge64
_Tcpv4EmptyPacketsMax_Object = MibScalar
tcpv4EmptyPacketsMax = _Tcpv4EmptyPacketsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 37, 3),
    _Tcpv4EmptyPacketsMax_Type()
)
tcpv4EmptyPacketsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv4EmptyPacketsMax.setStatus("current")
_Tcpv4OosPackets_ObjectIdentity = ObjectIdentity
tcpv4OosPackets = _Tcpv4OosPackets_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 38)
)
_Tcpv4OosPacketsVal_Type = Counter64
_Tcpv4OosPacketsVal_Object = MibScalar
tcpv4OosPacketsVal = _Tcpv4OosPacketsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 38, 1),
    _Tcpv4OosPacketsVal_Type()
)
tcpv4OosPacketsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv4OosPacketsVal.setStatus("current")
_Tcpv4OosPacketsMom_Type = CounterBasedGauge64
_Tcpv4OosPacketsMom_Object = MibScalar
tcpv4OosPacketsMom = _Tcpv4OosPacketsMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 38, 2),
    _Tcpv4OosPacketsMom_Type()
)
tcpv4OosPacketsMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv4OosPacketsMom.setStatus("current")
_Tcpv4OosPacketsMax_Type = CounterBasedGauge64
_Tcpv4OosPacketsMax_Object = MibScalar
tcpv4OosPacketsMax = _Tcpv4OosPacketsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 38, 3),
    _Tcpv4OosPacketsMax_Type()
)
tcpv4OosPacketsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv4OosPacketsMax.setStatus("current")
_Tcpv4OosBytes_ObjectIdentity = ObjectIdentity
tcpv4OosBytes = _Tcpv4OosBytes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 39)
)
_Tcpv4OosBytesVal_Type = Counter64
_Tcpv4OosBytesVal_Object = MibScalar
tcpv4OosBytesVal = _Tcpv4OosBytesVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 39, 1),
    _Tcpv4OosBytesVal_Type()
)
tcpv4OosBytesVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv4OosBytesVal.setStatus("current")
_Tcpv4OosBytesMom_Type = CounterBasedGauge64
_Tcpv4OosBytesMom_Object = MibScalar
tcpv4OosBytesMom = _Tcpv4OosBytesMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 39, 2),
    _Tcpv4OosBytesMom_Type()
)
tcpv4OosBytesMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv4OosBytesMom.setStatus("current")
_Tcpv4OosBytesMax_Type = CounterBasedGauge64
_Tcpv4OosBytesMax_Object = MibScalar
tcpv4OosBytesMax = _Tcpv4OosBytesMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 39, 3),
    _Tcpv4OosBytesMax_Type()
)
tcpv4OosBytesMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv4OosBytesMax.setStatus("current")
_Tcpv4Retransmits_ObjectIdentity = ObjectIdentity
tcpv4Retransmits = _Tcpv4Retransmits_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 40)
)
_Tcpv4RetransmitsVal_Type = Counter64
_Tcpv4RetransmitsVal_Object = MibScalar
tcpv4RetransmitsVal = _Tcpv4RetransmitsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 40, 1),
    _Tcpv4RetransmitsVal_Type()
)
tcpv4RetransmitsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv4RetransmitsVal.setStatus("current")
_Tcpv4RetransmitsMom_Type = CounterBasedGauge64
_Tcpv4RetransmitsMom_Object = MibScalar
tcpv4RetransmitsMom = _Tcpv4RetransmitsMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 40, 2),
    _Tcpv4RetransmitsMom_Type()
)
tcpv4RetransmitsMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv4RetransmitsMom.setStatus("current")
_Tcpv4RetransmitsMax_Type = CounterBasedGauge64
_Tcpv4RetransmitsMax_Object = MibScalar
tcpv4RetransmitsMax = _Tcpv4RetransmitsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 40, 3),
    _Tcpv4RetransmitsMax_Type()
)
tcpv4RetransmitsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv4RetransmitsMax.setStatus("current")
_Tcpv4Cwr_ObjectIdentity = ObjectIdentity
tcpv4Cwr = _Tcpv4Cwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 41)
)
_Tcpv4CwrVal_Type = Counter64
_Tcpv4CwrVal_Object = MibScalar
tcpv4CwrVal = _Tcpv4CwrVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 41, 1),
    _Tcpv4CwrVal_Type()
)
tcpv4CwrVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv4CwrVal.setStatus("current")
_Tcpv4CwrMom_Type = CounterBasedGauge64
_Tcpv4CwrMom_Object = MibScalar
tcpv4CwrMom = _Tcpv4CwrMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 41, 2),
    _Tcpv4CwrMom_Type()
)
tcpv4CwrMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv4CwrMom.setStatus("current")
_Tcpv4CwrMax_Type = CounterBasedGauge64
_Tcpv4CwrMax_Object = MibScalar
tcpv4CwrMax = _Tcpv4CwrMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 41, 3),
    _Tcpv4CwrMax_Type()
)
tcpv4CwrMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv4CwrMax.setStatus("current")
_Tcpv4Ecne_ObjectIdentity = ObjectIdentity
tcpv4Ecne = _Tcpv4Ecne_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 42)
)
_Tcpv4EcneVal_Type = Counter64
_Tcpv4EcneVal_Object = MibScalar
tcpv4EcneVal = _Tcpv4EcneVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 42, 1),
    _Tcpv4EcneVal_Type()
)
tcpv4EcneVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv4EcneVal.setStatus("current")
_Tcpv4EcneMom_Type = CounterBasedGauge64
_Tcpv4EcneMom_Object = MibScalar
tcpv4EcneMom = _Tcpv4EcneMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 42, 2),
    _Tcpv4EcneMom_Type()
)
tcpv4EcneMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv4EcneMom.setStatus("current")
_Tcpv4EcneMax_Type = CounterBasedGauge64
_Tcpv4EcneMax_Object = MibScalar
tcpv4EcneMax = _Tcpv4EcneMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 42, 3),
    _Tcpv4EcneMax_Type()
)
tcpv4EcneMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv4EcneMax.setStatus("current")
_Tcpv4SimOpen_ObjectIdentity = ObjectIdentity
tcpv4SimOpen = _Tcpv4SimOpen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 43)
)
_Tcpv4SimOpenVal_Type = Counter64
_Tcpv4SimOpenVal_Object = MibScalar
tcpv4SimOpenVal = _Tcpv4SimOpenVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 43, 1),
    _Tcpv4SimOpenVal_Type()
)
tcpv4SimOpenVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv4SimOpenVal.setStatus("current")
_Tcpv4SimOpenMom_Type = CounterBasedGauge64
_Tcpv4SimOpenMom_Object = MibScalar
tcpv4SimOpenMom = _Tcpv4SimOpenMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 43, 2),
    _Tcpv4SimOpenMom_Type()
)
tcpv4SimOpenMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv4SimOpenMom.setStatus("current")
_Tcpv4SimOpenMax_Type = CounterBasedGauge64
_Tcpv4SimOpenMax_Object = MibScalar
tcpv4SimOpenMax = _Tcpv4SimOpenMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 48, 43, 3),
    _Tcpv4SimOpenMax_Type()
)
tcpv4SimOpenMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv4SimOpenMax.setStatus("current")
_Connection_ObjectIdentity = ObjectIdentity
connection = _Connection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 56)
)
_ConnectionCount_ObjectIdentity = ObjectIdentity
connectionCount = _ConnectionCount_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 56, 1)
)
_ConnectionCountVal_Type = CounterBasedGauge64
_ConnectionCountVal_Object = MibScalar
connectionCountVal = _ConnectionCountVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 56, 1, 1),
    _ConnectionCountVal_Type()
)
connectionCountVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionCountVal.setStatus("current")
_ConnectionCountMax_Type = CounterBasedGauge64
_ConnectionCountMax_Object = MibScalar
connectionCountMax = _ConnectionCountMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 56, 1, 3),
    _ConnectionCountMax_Type()
)
connectionCountMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionCountMax.setStatus("current")
_ConnectionEstCount_ObjectIdentity = ObjectIdentity
connectionEstCount = _ConnectionEstCount_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 56, 2)
)
_ConnectionEstCountVal_Type = CounterBasedGauge64
_ConnectionEstCountVal_Object = MibScalar
connectionEstCountVal = _ConnectionEstCountVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 56, 2, 1),
    _ConnectionEstCountVal_Type()
)
connectionEstCountVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionEstCountVal.setStatus("current")
_ConnectionEstCountMax_Type = CounterBasedGauge64
_ConnectionEstCountMax_Object = MibScalar
connectionEstCountMax = _ConnectionEstCountMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 56, 2, 3),
    _ConnectionEstCountMax_Type()
)
connectionEstCountMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionEstCountMax.setStatus("current")
_ConnectionCreateAttemptsInbound_ObjectIdentity = ObjectIdentity
connectionCreateAttemptsInbound = _ConnectionCreateAttemptsInbound_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 56, 3)
)
_ConnectionCreateAttemptsInboundVal_Type = Counter64
_ConnectionCreateAttemptsInboundVal_Object = MibScalar
connectionCreateAttemptsInboundVal = _ConnectionCreateAttemptsInboundVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 56, 3, 1),
    _ConnectionCreateAttemptsInboundVal_Type()
)
connectionCreateAttemptsInboundVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionCreateAttemptsInboundVal.setStatus("current")
_ConnectionCreateAttemptsInboundMom_Type = CounterBasedGauge64
_ConnectionCreateAttemptsInboundMom_Object = MibScalar
connectionCreateAttemptsInboundMom = _ConnectionCreateAttemptsInboundMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 56, 3, 2),
    _ConnectionCreateAttemptsInboundMom_Type()
)
connectionCreateAttemptsInboundMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionCreateAttemptsInboundMom.setStatus("current")
_ConnectionCreateAttemptsInboundMax_Type = CounterBasedGauge64
_ConnectionCreateAttemptsInboundMax_Object = MibScalar
connectionCreateAttemptsInboundMax = _ConnectionCreateAttemptsInboundMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 56, 3, 3),
    _ConnectionCreateAttemptsInboundMax_Type()
)
connectionCreateAttemptsInboundMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionCreateAttemptsInboundMax.setStatus("current")
_ConnectionCreateAttemptsOutbound_ObjectIdentity = ObjectIdentity
connectionCreateAttemptsOutbound = _ConnectionCreateAttemptsOutbound_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 56, 4)
)
_ConnectionCreateAttemptsOutboundVal_Type = Counter64
_ConnectionCreateAttemptsOutboundVal_Object = MibScalar
connectionCreateAttemptsOutboundVal = _ConnectionCreateAttemptsOutboundVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 56, 4, 1),
    _ConnectionCreateAttemptsOutboundVal_Type()
)
connectionCreateAttemptsOutboundVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionCreateAttemptsOutboundVal.setStatus("current")
_ConnectionCreateAttemptsOutboundMom_Type = CounterBasedGauge64
_ConnectionCreateAttemptsOutboundMom_Object = MibScalar
connectionCreateAttemptsOutboundMom = _ConnectionCreateAttemptsOutboundMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 56, 4, 2),
    _ConnectionCreateAttemptsOutboundMom_Type()
)
connectionCreateAttemptsOutboundMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionCreateAttemptsOutboundMom.setStatus("current")
_ConnectionCreateAttemptsOutboundMax_Type = CounterBasedGauge64
_ConnectionCreateAttemptsOutboundMax_Object = MibScalar
connectionCreateAttemptsOutboundMax = _ConnectionCreateAttemptsOutboundMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 56, 4, 3),
    _ConnectionCreateAttemptsOutboundMax_Type()
)
connectionCreateAttemptsOutboundMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionCreateAttemptsOutboundMax.setStatus("current")
_ConnectionRefusedProt_ObjectIdentity = ObjectIdentity
connectionRefusedProt = _ConnectionRefusedProt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 56, 5)
)
_ConnectionRefusedProtVal_Type = Counter64
_ConnectionRefusedProtVal_Object = MibScalar
connectionRefusedProtVal = _ConnectionRefusedProtVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 56, 5, 1),
    _ConnectionRefusedProtVal_Type()
)
connectionRefusedProtVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionRefusedProtVal.setStatus("current")
_ConnectionRefusedProtMom_Type = CounterBasedGauge64
_ConnectionRefusedProtMom_Object = MibScalar
connectionRefusedProtMom = _ConnectionRefusedProtMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 56, 5, 2),
    _ConnectionRefusedProtMom_Type()
)
connectionRefusedProtMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionRefusedProtMom.setStatus("current")
_ConnectionRefusedProtMax_Type = CounterBasedGauge64
_ConnectionRefusedProtMax_Object = MibScalar
connectionRefusedProtMax = _ConnectionRefusedProtMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 56, 5, 3),
    _ConnectionRefusedProtMax_Type()
)
connectionRefusedProtMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionRefusedProtMax.setStatus("current")
_ConnectionRefusedFull_ObjectIdentity = ObjectIdentity
connectionRefusedFull = _ConnectionRefusedFull_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 56, 6)
)
_ConnectionRefusedFullVal_Type = Counter64
_ConnectionRefusedFullVal_Object = MibScalar
connectionRefusedFullVal = _ConnectionRefusedFullVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 56, 6, 1),
    _ConnectionRefusedFullVal_Type()
)
connectionRefusedFullVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionRefusedFullVal.setStatus("current")
_ConnectionRefusedFullMom_Type = CounterBasedGauge64
_ConnectionRefusedFullMom_Object = MibScalar
connectionRefusedFullMom = _ConnectionRefusedFullMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 56, 6, 2),
    _ConnectionRefusedFullMom_Type()
)
connectionRefusedFullMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionRefusedFullMom.setStatus("current")
_ConnectionRefusedFullMax_Type = CounterBasedGauge64
_ConnectionRefusedFullMax_Object = MibScalar
connectionRefusedFullMax = _ConnectionRefusedFullMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 56, 6, 3),
    _ConnectionRefusedFullMax_Type()
)
connectionRefusedFullMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionRefusedFullMax.setStatus("current")
_ConnectionCreatedInbound_ObjectIdentity = ObjectIdentity
connectionCreatedInbound = _ConnectionCreatedInbound_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 56, 7)
)
_ConnectionCreatedInboundVal_Type = Counter64
_ConnectionCreatedInboundVal_Object = MibScalar
connectionCreatedInboundVal = _ConnectionCreatedInboundVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 56, 7, 1),
    _ConnectionCreatedInboundVal_Type()
)
connectionCreatedInboundVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionCreatedInboundVal.setStatus("current")
_ConnectionCreatedInboundMom_Type = CounterBasedGauge64
_ConnectionCreatedInboundMom_Object = MibScalar
connectionCreatedInboundMom = _ConnectionCreatedInboundMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 56, 7, 2),
    _ConnectionCreatedInboundMom_Type()
)
connectionCreatedInboundMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionCreatedInboundMom.setStatus("current")
_ConnectionCreatedInboundMax_Type = CounterBasedGauge64
_ConnectionCreatedInboundMax_Object = MibScalar
connectionCreatedInboundMax = _ConnectionCreatedInboundMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 56, 7, 3),
    _ConnectionCreatedInboundMax_Type()
)
connectionCreatedInboundMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionCreatedInboundMax.setStatus("current")
_ConnectionCreatedOutbound_ObjectIdentity = ObjectIdentity
connectionCreatedOutbound = _ConnectionCreatedOutbound_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 56, 8)
)
_ConnectionCreatedOutboundVal_Type = Counter64
_ConnectionCreatedOutboundVal_Object = MibScalar
connectionCreatedOutboundVal = _ConnectionCreatedOutboundVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 56, 8, 1),
    _ConnectionCreatedOutboundVal_Type()
)
connectionCreatedOutboundVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionCreatedOutboundVal.setStatus("current")
_ConnectionCreatedOutboundMom_Type = CounterBasedGauge64
_ConnectionCreatedOutboundMom_Object = MibScalar
connectionCreatedOutboundMom = _ConnectionCreatedOutboundMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 56, 8, 2),
    _ConnectionCreatedOutboundMom_Type()
)
connectionCreatedOutboundMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionCreatedOutboundMom.setStatus("current")
_ConnectionCreatedOutboundMax_Type = CounterBasedGauge64
_ConnectionCreatedOutboundMax_Object = MibScalar
connectionCreatedOutboundMax = _ConnectionCreatedOutboundMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 56, 8, 3),
    _ConnectionCreatedOutboundMax_Type()
)
connectionCreatedOutboundMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionCreatedOutboundMax.setStatus("current")
_ConnectionLruAllocs_ObjectIdentity = ObjectIdentity
connectionLruAllocs = _ConnectionLruAllocs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 56, 9)
)
_ConnectionLruAllocsVal_Type = Counter64
_ConnectionLruAllocsVal_Object = MibScalar
connectionLruAllocsVal = _ConnectionLruAllocsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 56, 9, 1),
    _ConnectionLruAllocsVal_Type()
)
connectionLruAllocsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionLruAllocsVal.setStatus("current")
_ConnectionLruAllocsMom_Type = CounterBasedGauge64
_ConnectionLruAllocsMom_Object = MibScalar
connectionLruAllocsMom = _ConnectionLruAllocsMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 56, 9, 2),
    _ConnectionLruAllocsMom_Type()
)
connectionLruAllocsMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionLruAllocsMom.setStatus("current")
_ConnectionLruAllocsMax_Type = CounterBasedGauge64
_ConnectionLruAllocsMax_Object = MibScalar
connectionLruAllocsMax = _ConnectionLruAllocsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 56, 9, 3),
    _ConnectionLruAllocsMax_Type()
)
connectionLruAllocsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionLruAllocsMax.setStatus("current")
_ConnectionLookups_ObjectIdentity = ObjectIdentity
connectionLookups = _ConnectionLookups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 56, 10)
)
_ConnectionLookupsVal_Type = Counter64
_ConnectionLookupsVal_Object = MibScalar
connectionLookupsVal = _ConnectionLookupsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 56, 10, 1),
    _ConnectionLookupsVal_Type()
)
connectionLookupsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionLookupsVal.setStatus("current")
_ConnectionLookupsMom_Type = CounterBasedGauge64
_ConnectionLookupsMom_Object = MibScalar
connectionLookupsMom = _ConnectionLookupsMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 56, 10, 2),
    _ConnectionLookupsMom_Type()
)
connectionLookupsMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionLookupsMom.setStatus("current")
_ConnectionLookupsMax_Type = CounterBasedGauge64
_ConnectionLookupsMax_Object = MibScalar
connectionLookupsMax = _ConnectionLookupsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 56, 10, 3),
    _ConnectionLookupsMax_Type()
)
connectionLookupsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionLookupsMax.setStatus("current")
_ConnectionEstablished_ObjectIdentity = ObjectIdentity
connectionEstablished = _ConnectionEstablished_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 56, 11)
)
_ConnectionEstablishedVal_Type = Counter64
_ConnectionEstablishedVal_Object = MibScalar
connectionEstablishedVal = _ConnectionEstablishedVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 56, 11, 1),
    _ConnectionEstablishedVal_Type()
)
connectionEstablishedVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionEstablishedVal.setStatus("current")
_ConnectionEstablishedMom_Type = CounterBasedGauge64
_ConnectionEstablishedMom_Object = MibScalar
connectionEstablishedMom = _ConnectionEstablishedMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 56, 11, 2),
    _ConnectionEstablishedMom_Type()
)
connectionEstablishedMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionEstablishedMom.setStatus("current")
_ConnectionEstablishedMax_Type = CounterBasedGauge64
_ConnectionEstablishedMax_Object = MibScalar
connectionEstablishedMax = _ConnectionEstablishedMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 56, 11, 3),
    _ConnectionEstablishedMax_Type()
)
connectionEstablishedMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionEstablishedMax.setStatus("current")
_ConnectionUpdates_ObjectIdentity = ObjectIdentity
connectionUpdates = _ConnectionUpdates_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 56, 12)
)
_ConnectionUpdatesVal_Type = Counter64
_ConnectionUpdatesVal_Object = MibScalar
connectionUpdatesVal = _ConnectionUpdatesVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 56, 12, 1),
    _ConnectionUpdatesVal_Type()
)
connectionUpdatesVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionUpdatesVal.setStatus("current")
_ConnectionUpdatesMom_Type = CounterBasedGauge64
_ConnectionUpdatesMom_Object = MibScalar
connectionUpdatesMom = _ConnectionUpdatesMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 56, 12, 2),
    _ConnectionUpdatesMom_Type()
)
connectionUpdatesMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionUpdatesMom.setStatus("current")
_ConnectionUpdatesMax_Type = CounterBasedGauge64
_ConnectionUpdatesMax_Object = MibScalar
connectionUpdatesMax = _ConnectionUpdatesMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 56, 12, 3),
    _ConnectionUpdatesMax_Type()
)
connectionUpdatesMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionUpdatesMax.setStatus("current")
_ConnectionTtlTimeouts_ObjectIdentity = ObjectIdentity
connectionTtlTimeouts = _ConnectionTtlTimeouts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 56, 13)
)
_ConnectionTtlTimeoutsVal_Type = Counter64
_ConnectionTtlTimeoutsVal_Object = MibScalar
connectionTtlTimeoutsVal = _ConnectionTtlTimeoutsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 56, 13, 1),
    _ConnectionTtlTimeoutsVal_Type()
)
connectionTtlTimeoutsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionTtlTimeoutsVal.setStatus("current")
_ConnectionTtlTimeoutsMom_Type = CounterBasedGauge64
_ConnectionTtlTimeoutsMom_Object = MibScalar
connectionTtlTimeoutsMom = _ConnectionTtlTimeoutsMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 56, 13, 2),
    _ConnectionTtlTimeoutsMom_Type()
)
connectionTtlTimeoutsMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionTtlTimeoutsMom.setStatus("current")
_ConnectionTtlTimeoutsMax_Type = CounterBasedGauge64
_ConnectionTtlTimeoutsMax_Object = MibScalar
connectionTtlTimeoutsMax = _ConnectionTtlTimeoutsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 56, 13, 3),
    _ConnectionTtlTimeoutsMax_Type()
)
connectionTtlTimeoutsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionTtlTimeoutsMax.setStatus("current")
_ConnectionProtEnables_ObjectIdentity = ObjectIdentity
connectionProtEnables = _ConnectionProtEnables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 56, 14)
)
_ConnectionProtEnablesVal_Type = Counter64
_ConnectionProtEnablesVal_Object = MibScalar
connectionProtEnablesVal = _ConnectionProtEnablesVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 56, 14, 1),
    _ConnectionProtEnablesVal_Type()
)
connectionProtEnablesVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionProtEnablesVal.setStatus("current")
_ConnectionProtEnablesMom_Type = CounterBasedGauge64
_ConnectionProtEnablesMom_Object = MibScalar
connectionProtEnablesMom = _ConnectionProtEnablesMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 56, 14, 2),
    _ConnectionProtEnablesMom_Type()
)
connectionProtEnablesMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionProtEnablesMom.setStatus("current")
_ConnectionProtEnablesMax_Type = CounterBasedGauge64
_ConnectionProtEnablesMax_Object = MibScalar
connectionProtEnablesMax = _ConnectionProtEnablesMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 56, 14, 3),
    _ConnectionProtEnablesMax_Type()
)
connectionProtEnablesMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionProtEnablesMax.setStatus("current")
_ConnectionNotFound_ObjectIdentity = ObjectIdentity
connectionNotFound = _ConnectionNotFound_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 56, 15)
)
_ConnectionNotFoundVal_Type = Counter64
_ConnectionNotFoundVal_Object = MibScalar
connectionNotFoundVal = _ConnectionNotFoundVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 56, 15, 1),
    _ConnectionNotFoundVal_Type()
)
connectionNotFoundVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionNotFoundVal.setStatus("current")
_ConnectionNotFoundMom_Type = CounterBasedGauge64
_ConnectionNotFoundMom_Object = MibScalar
connectionNotFoundMom = _ConnectionNotFoundMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 56, 15, 2),
    _ConnectionNotFoundMom_Type()
)
connectionNotFoundMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionNotFoundMom.setStatus("current")
_ConnectionNotFoundMax_Type = CounterBasedGauge64
_ConnectionNotFoundMax_Object = MibScalar
connectionNotFoundMax = _ConnectionNotFoundMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 56, 15, 3),
    _ConnectionNotFoundMax_Type()
)
connectionNotFoundMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionNotFoundMax.setStatus("current")
_ConnectionRefusedExisting_ObjectIdentity = ObjectIdentity
connectionRefusedExisting = _ConnectionRefusedExisting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 56, 18)
)
_ConnectionRefusedExistingVal_Type = Counter64
_ConnectionRefusedExistingVal_Object = MibScalar
connectionRefusedExistingVal = _ConnectionRefusedExistingVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 56, 18, 1),
    _ConnectionRefusedExistingVal_Type()
)
connectionRefusedExistingVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionRefusedExistingVal.setStatus("current")
_ConnectionRefusedExistingMom_Type = CounterBasedGauge64
_ConnectionRefusedExistingMom_Object = MibScalar
connectionRefusedExistingMom = _ConnectionRefusedExistingMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 56, 18, 2),
    _ConnectionRefusedExistingMom_Type()
)
connectionRefusedExistingMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionRefusedExistingMom.setStatus("current")
_ConnectionRefusedExistingMax_Type = CounterBasedGauge64
_ConnectionRefusedExistingMax_Object = MibScalar
connectionRefusedExistingMax = _ConnectionRefusedExistingMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 56, 18, 3),
    _ConnectionRefusedExistingMax_Type()
)
connectionRefusedExistingMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionRefusedExistingMax.setStatus("current")
_ConnectionRefusedRuleset_ObjectIdentity = ObjectIdentity
connectionRefusedRuleset = _ConnectionRefusedRuleset_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 56, 19)
)
_ConnectionRefusedRulesetVal_Type = Counter64
_ConnectionRefusedRulesetVal_Object = MibScalar
connectionRefusedRulesetVal = _ConnectionRefusedRulesetVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 56, 19, 1),
    _ConnectionRefusedRulesetVal_Type()
)
connectionRefusedRulesetVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionRefusedRulesetVal.setStatus("current")
_ConnectionRefusedRulesetMom_Type = CounterBasedGauge64
_ConnectionRefusedRulesetMom_Object = MibScalar
connectionRefusedRulesetMom = _ConnectionRefusedRulesetMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 56, 19, 2),
    _ConnectionRefusedRulesetMom_Type()
)
connectionRefusedRulesetMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionRefusedRulesetMom.setStatus("current")
_ConnectionRefusedRulesetMax_Type = CounterBasedGauge64
_ConnectionRefusedRulesetMax_Object = MibScalar
connectionRefusedRulesetMax = _ConnectionRefusedRulesetMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 56, 19, 3),
    _ConnectionRefusedRulesetMax_Type()
)
connectionRefusedRulesetMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionRefusedRulesetMax.setStatus("current")
_ConnectionRedirected_ObjectIdentity = ObjectIdentity
connectionRedirected = _ConnectionRedirected_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 56, 20)
)
_ConnectionRedirectedVal_Type = CounterBasedGauge64
_ConnectionRedirectedVal_Object = MibScalar
connectionRedirectedVal = _ConnectionRedirectedVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 56, 20, 1),
    _ConnectionRedirectedVal_Type()
)
connectionRedirectedVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionRedirectedVal.setStatus("current")
_ConnectionRedirectedMax_Type = CounterBasedGauge64
_ConnectionRedirectedMax_Object = MibScalar
connectionRedirectedMax = _ConnectionRedirectedMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 56, 20, 3),
    _ConnectionRedirectedMax_Type()
)
connectionRedirectedMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionRedirectedMax.setStatus("current")
_ConnectionRedirectCollisions_ObjectIdentity = ObjectIdentity
connectionRedirectCollisions = _ConnectionRedirectCollisions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 56, 21)
)
_ConnectionRedirectCollisionsVal_Type = CounterBasedGauge64
_ConnectionRedirectCollisionsVal_Object = MibScalar
connectionRedirectCollisionsVal = _ConnectionRedirectCollisionsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 56, 21, 1),
    _ConnectionRedirectCollisionsVal_Type()
)
connectionRedirectCollisionsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionRedirectCollisionsVal.setStatus("current")
_ConnectionRedirectCollisionsMax_Type = CounterBasedGauge64
_ConnectionRedirectCollisionsMax_Object = MibScalar
connectionRedirectCollisionsMax = _ConnectionRedirectCollisionsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 56, 21, 3),
    _ConnectionRedirectCollisionsMax_Type()
)
connectionRedirectCollisionsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionRedirectCollisionsMax.setStatus("current")
_ConnectionUnestablished_ObjectIdentity = ObjectIdentity
connectionUnestablished = _ConnectionUnestablished_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 56, 24)
)
_ConnectionUnestablishedVal_Type = Counter64
_ConnectionUnestablishedVal_Object = MibScalar
connectionUnestablishedVal = _ConnectionUnestablishedVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 56, 24, 1),
    _ConnectionUnestablishedVal_Type()
)
connectionUnestablishedVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionUnestablishedVal.setStatus("current")
_ConnectionUnestablishedMom_Type = CounterBasedGauge64
_ConnectionUnestablishedMom_Object = MibScalar
connectionUnestablishedMom = _ConnectionUnestablishedMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 56, 24, 2),
    _ConnectionUnestablishedMom_Type()
)
connectionUnestablishedMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionUnestablishedMom.setStatus("current")
_ConnectionUnestablishedMax_Type = CounterBasedGauge64
_ConnectionUnestablishedMax_Object = MibScalar
connectionUnestablishedMax = _ConnectionUnestablishedMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 56, 24, 3),
    _ConnectionUnestablishedMax_Type()
)
connectionUnestablishedMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionUnestablishedMax.setStatus("current")
_ConnectionDestroyedEst_ObjectIdentity = ObjectIdentity
connectionDestroyedEst = _ConnectionDestroyedEst_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 56, 25)
)
_ConnectionDestroyedEstVal_Type = CounterBasedGauge64
_ConnectionDestroyedEstVal_Object = MibScalar
connectionDestroyedEstVal = _ConnectionDestroyedEstVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 56, 25, 1),
    _ConnectionDestroyedEstVal_Type()
)
connectionDestroyedEstVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionDestroyedEstVal.setStatus("current")
_ConnectionDestroyedEstMax_Type = CounterBasedGauge64
_ConnectionDestroyedEstMax_Object = MibScalar
connectionDestroyedEstMax = _ConnectionDestroyedEstMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 56, 25, 3),
    _ConnectionDestroyedEstMax_Type()
)
connectionDestroyedEstMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionDestroyedEstMax.setStatus("current")
_ConnectionInvalidRulesetUpdate_ObjectIdentity = ObjectIdentity
connectionInvalidRulesetUpdate = _ConnectionInvalidRulesetUpdate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 56, 26)
)
_ConnectionInvalidRulesetUpdateVal_Type = Counter64
_ConnectionInvalidRulesetUpdateVal_Object = MibScalar
connectionInvalidRulesetUpdateVal = _ConnectionInvalidRulesetUpdateVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 56, 26, 1),
    _ConnectionInvalidRulesetUpdateVal_Type()
)
connectionInvalidRulesetUpdateVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionInvalidRulesetUpdateVal.setStatus("current")
_ConnectionInvalidRulesetUpdateMom_Type = CounterBasedGauge64
_ConnectionInvalidRulesetUpdateMom_Object = MibScalar
connectionInvalidRulesetUpdateMom = _ConnectionInvalidRulesetUpdateMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 56, 26, 2),
    _ConnectionInvalidRulesetUpdateMom_Type()
)
connectionInvalidRulesetUpdateMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionInvalidRulesetUpdateMom.setStatus("current")
_ConnectionInvalidRulesetUpdateMax_Type = CounterBasedGauge64
_ConnectionInvalidRulesetUpdateMax_Object = MibScalar
connectionInvalidRulesetUpdateMax = _ConnectionInvalidRulesetUpdateMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 56, 26, 3),
    _ConnectionInvalidRulesetUpdateMax_Type()
)
connectionInvalidRulesetUpdateMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionInvalidRulesetUpdateMax.setStatus("current")
_ConnectionOrphaned_ObjectIdentity = ObjectIdentity
connectionOrphaned = _ConnectionOrphaned_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 56, 27)
)
_ConnectionOrphanedVal_Type = CounterBasedGauge64
_ConnectionOrphanedVal_Object = MibScalar
connectionOrphanedVal = _ConnectionOrphanedVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 56, 27, 1),
    _ConnectionOrphanedVal_Type()
)
connectionOrphanedVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionOrphanedVal.setStatus("current")
_ConnectionOrphanedMax_Type = CounterBasedGauge64
_ConnectionOrphanedMax_Object = MibScalar
connectionOrphanedMax = _ConnectionOrphanedMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 56, 27, 3),
    _ConnectionOrphanedMax_Type()
)
connectionOrphanedMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionOrphanedMax.setStatus("current")
_ConnectionFailureShuntPackets_ObjectIdentity = ObjectIdentity
connectionFailureShuntPackets = _ConnectionFailureShuntPackets_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 56, 40)
)
_ConnectionFailureShuntPacketsVal_Type = Counter64
_ConnectionFailureShuntPacketsVal_Object = MibScalar
connectionFailureShuntPacketsVal = _ConnectionFailureShuntPacketsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 56, 40, 1),
    _ConnectionFailureShuntPacketsVal_Type()
)
connectionFailureShuntPacketsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionFailureShuntPacketsVal.setStatus("current")
_ConnectionFailureShuntPacketsMom_Type = CounterBasedGauge64
_ConnectionFailureShuntPacketsMom_Object = MibScalar
connectionFailureShuntPacketsMom = _ConnectionFailureShuntPacketsMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 56, 40, 2),
    _ConnectionFailureShuntPacketsMom_Type()
)
connectionFailureShuntPacketsMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionFailureShuntPacketsMom.setStatus("current")
_ConnectionFailureShuntPacketsMax_Type = CounterBasedGauge64
_ConnectionFailureShuntPacketsMax_Object = MibScalar
connectionFailureShuntPacketsMax = _ConnectionFailureShuntPacketsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 56, 40, 3),
    _ConnectionFailureShuntPacketsMax_Type()
)
connectionFailureShuntPacketsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionFailureShuntPacketsMax.setStatus("current")
_ConnectionFailureShuntBytes_ObjectIdentity = ObjectIdentity
connectionFailureShuntBytes = _ConnectionFailureShuntBytes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 56, 41)
)
_ConnectionFailureShuntBytesVal_Type = Counter64
_ConnectionFailureShuntBytesVal_Object = MibScalar
connectionFailureShuntBytesVal = _ConnectionFailureShuntBytesVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 56, 41, 1),
    _ConnectionFailureShuntBytesVal_Type()
)
connectionFailureShuntBytesVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionFailureShuntBytesVal.setStatus("current")
_ConnectionFailureShuntBytesMom_Type = CounterBasedGauge64
_ConnectionFailureShuntBytesMom_Object = MibScalar
connectionFailureShuntBytesMom = _ConnectionFailureShuntBytesMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 56, 41, 2),
    _ConnectionFailureShuntBytesMom_Type()
)
connectionFailureShuntBytesMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionFailureShuntBytesMom.setStatus("current")
_ConnectionFailureShuntBytesMax_Type = CounterBasedGauge64
_ConnectionFailureShuntBytesMax_Object = MibScalar
connectionFailureShuntBytesMax = _ConnectionFailureShuntBytesMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 56, 41, 3),
    _ConnectionFailureShuntBytesMax_Type()
)
connectionFailureShuntBytesMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionFailureShuntBytesMax.setStatus("current")
_Connsync_ObjectIdentity = ObjectIdentity
connsync = _Connsync_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 60)
)
_ConnsyncSeenSnt_ObjectIdentity = ObjectIdentity
connsyncSeenSnt = _ConnsyncSeenSnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 60, 1)
)
_ConnsyncSeenSntVal_Type = Counter64
_ConnsyncSeenSntVal_Object = MibScalar
connsyncSeenSntVal = _ConnsyncSeenSntVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 60, 1, 1),
    _ConnsyncSeenSntVal_Type()
)
connsyncSeenSntVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connsyncSeenSntVal.setStatus("current")
_ConnsyncSeenSntMom_Type = CounterBasedGauge64
_ConnsyncSeenSntMom_Object = MibScalar
connsyncSeenSntMom = _ConnsyncSeenSntMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 60, 1, 2),
    _ConnsyncSeenSntMom_Type()
)
connsyncSeenSntMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connsyncSeenSntMom.setStatus("current")
_ConnsyncSeenSntMax_Type = CounterBasedGauge64
_ConnsyncSeenSntMax_Object = MibScalar
connsyncSeenSntMax = _ConnsyncSeenSntMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 60, 1, 3),
    _ConnsyncSeenSntMax_Type()
)
connsyncSeenSntMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connsyncSeenSntMax.setStatus("current")
_ConnsyncSeenRcv_ObjectIdentity = ObjectIdentity
connsyncSeenRcv = _ConnsyncSeenRcv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 60, 2)
)
_ConnsyncSeenRcvVal_Type = Counter64
_ConnsyncSeenRcvVal_Object = MibScalar
connsyncSeenRcvVal = _ConnsyncSeenRcvVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 60, 2, 1),
    _ConnsyncSeenRcvVal_Type()
)
connsyncSeenRcvVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connsyncSeenRcvVal.setStatus("current")
_ConnsyncSeenRcvMom_Type = CounterBasedGauge64
_ConnsyncSeenRcvMom_Object = MibScalar
connsyncSeenRcvMom = _ConnsyncSeenRcvMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 60, 2, 2),
    _ConnsyncSeenRcvMom_Type()
)
connsyncSeenRcvMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connsyncSeenRcvMom.setStatus("current")
_ConnsyncSeenRcvMax_Type = CounterBasedGauge64
_ConnsyncSeenRcvMax_Object = MibScalar
connsyncSeenRcvMax = _ConnsyncSeenRcvMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 60, 2, 3),
    _ConnsyncSeenRcvMax_Type()
)
connsyncSeenRcvMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connsyncSeenRcvMax.setStatus("current")
_ConnsyncUpdateSnt_ObjectIdentity = ObjectIdentity
connsyncUpdateSnt = _ConnsyncUpdateSnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 60, 3)
)
_ConnsyncUpdateSntVal_Type = Counter64
_ConnsyncUpdateSntVal_Object = MibScalar
connsyncUpdateSntVal = _ConnsyncUpdateSntVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 60, 3, 1),
    _ConnsyncUpdateSntVal_Type()
)
connsyncUpdateSntVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connsyncUpdateSntVal.setStatus("current")
_ConnsyncUpdateSntMom_Type = CounterBasedGauge64
_ConnsyncUpdateSntMom_Object = MibScalar
connsyncUpdateSntMom = _ConnsyncUpdateSntMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 60, 3, 2),
    _ConnsyncUpdateSntMom_Type()
)
connsyncUpdateSntMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connsyncUpdateSntMom.setStatus("current")
_ConnsyncUpdateSntMax_Type = CounterBasedGauge64
_ConnsyncUpdateSntMax_Object = MibScalar
connsyncUpdateSntMax = _ConnsyncUpdateSntMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 60, 3, 3),
    _ConnsyncUpdateSntMax_Type()
)
connsyncUpdateSntMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connsyncUpdateSntMax.setStatus("current")
_ConnsyncSeenackRcv_ObjectIdentity = ObjectIdentity
connsyncSeenackRcv = _ConnsyncSeenackRcv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 60, 4)
)
_ConnsyncSeenackRcvVal_Type = Counter64
_ConnsyncSeenackRcvVal_Object = MibScalar
connsyncSeenackRcvVal = _ConnsyncSeenackRcvVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 60, 4, 1),
    _ConnsyncSeenackRcvVal_Type()
)
connsyncSeenackRcvVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connsyncSeenackRcvVal.setStatus("current")
_ConnsyncSeenackRcvMom_Type = CounterBasedGauge64
_ConnsyncSeenackRcvMom_Object = MibScalar
connsyncSeenackRcvMom = _ConnsyncSeenackRcvMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 60, 4, 2),
    _ConnsyncSeenackRcvMom_Type()
)
connsyncSeenackRcvMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connsyncSeenackRcvMom.setStatus("current")
_ConnsyncSeenackRcvMax_Type = CounterBasedGauge64
_ConnsyncSeenackRcvMax_Object = MibScalar
connsyncSeenackRcvMax = _ConnsyncSeenackRcvMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 60, 4, 3),
    _ConnsyncSeenackRcvMax_Type()
)
connsyncSeenackRcvMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connsyncSeenackRcvMax.setStatus("current")
_ConnsyncUpdateRcv_ObjectIdentity = ObjectIdentity
connsyncUpdateRcv = _ConnsyncUpdateRcv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 60, 5)
)
_ConnsyncUpdateRcvVal_Type = Counter64
_ConnsyncUpdateRcvVal_Object = MibScalar
connsyncUpdateRcvVal = _ConnsyncUpdateRcvVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 60, 5, 1),
    _ConnsyncUpdateRcvVal_Type()
)
connsyncUpdateRcvVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connsyncUpdateRcvVal.setStatus("current")
_ConnsyncUpdateRcvMom_Type = CounterBasedGauge64
_ConnsyncUpdateRcvMom_Object = MibScalar
connsyncUpdateRcvMom = _ConnsyncUpdateRcvMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 60, 5, 2),
    _ConnsyncUpdateRcvMom_Type()
)
connsyncUpdateRcvMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connsyncUpdateRcvMom.setStatus("current")
_ConnsyncUpdateRcvMax_Type = CounterBasedGauge64
_ConnsyncUpdateRcvMax_Object = MibScalar
connsyncUpdateRcvMax = _ConnsyncUpdateRcvMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 60, 5, 3),
    _ConnsyncUpdateRcvMax_Type()
)
connsyncUpdateRcvMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connsyncUpdateRcvMax.setStatus("current")
_ConnsyncUnknownUpdateRcv_ObjectIdentity = ObjectIdentity
connsyncUnknownUpdateRcv = _ConnsyncUnknownUpdateRcv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 60, 6)
)
_ConnsyncUnknownUpdateRcvVal_Type = Counter64
_ConnsyncUnknownUpdateRcvVal_Object = MibScalar
connsyncUnknownUpdateRcvVal = _ConnsyncUnknownUpdateRcvVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 60, 6, 1),
    _ConnsyncUnknownUpdateRcvVal_Type()
)
connsyncUnknownUpdateRcvVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connsyncUnknownUpdateRcvVal.setStatus("current")
_ConnsyncUnknownUpdateRcvMom_Type = CounterBasedGauge64
_ConnsyncUnknownUpdateRcvMom_Object = MibScalar
connsyncUnknownUpdateRcvMom = _ConnsyncUnknownUpdateRcvMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 60, 6, 2),
    _ConnsyncUnknownUpdateRcvMom_Type()
)
connsyncUnknownUpdateRcvMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connsyncUnknownUpdateRcvMom.setStatus("current")
_ConnsyncUnknownUpdateRcvMax_Type = CounterBasedGauge64
_ConnsyncUnknownUpdateRcvMax_Object = MibScalar
connsyncUnknownUpdateRcvMax = _ConnsyncUnknownUpdateRcvMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 60, 6, 3),
    _ConnsyncUnknownUpdateRcvMax_Type()
)
connsyncUnknownUpdateRcvMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connsyncUnknownUpdateRcvMax.setStatus("current")
_ConnsyncOutofsync_ObjectIdentity = ObjectIdentity
connsyncOutofsync = _ConnsyncOutofsync_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 60, 7)
)
_ConnsyncOutofsyncVal_Type = Counter64
_ConnsyncOutofsyncVal_Object = MibScalar
connsyncOutofsyncVal = _ConnsyncOutofsyncVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 60, 7, 1),
    _ConnsyncOutofsyncVal_Type()
)
connsyncOutofsyncVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connsyncOutofsyncVal.setStatus("current")
_ConnsyncOutofsyncMom_Type = CounterBasedGauge64
_ConnsyncOutofsyncMom_Object = MibScalar
connsyncOutofsyncMom = _ConnsyncOutofsyncMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 60, 7, 2),
    _ConnsyncOutofsyncMom_Type()
)
connsyncOutofsyncMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connsyncOutofsyncMom.setStatus("current")
_ConnsyncOutofsyncMax_Type = CounterBasedGauge64
_ConnsyncOutofsyncMax_Object = MibScalar
connsyncOutofsyncMax = _ConnsyncOutofsyncMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 60, 7, 3),
    _ConnsyncOutofsyncMax_Type()
)
connsyncOutofsyncMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connsyncOutofsyncMax.setStatus("current")
_ConnsyncSynced_ObjectIdentity = ObjectIdentity
connsyncSynced = _ConnsyncSynced_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 60, 8)
)
_ConnsyncSyncedVal_Type = CounterBasedGauge64
_ConnsyncSyncedVal_Object = MibScalar
connsyncSyncedVal = _ConnsyncSyncedVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 60, 8, 1),
    _ConnsyncSyncedVal_Type()
)
connsyncSyncedVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connsyncSyncedVal.setStatus("current")
_ConnsyncSyncedMax_Type = CounterBasedGauge64
_ConnsyncSyncedMax_Object = MibScalar
connsyncSyncedMax = _ConnsyncSyncedMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 60, 8, 3),
    _ConnsyncSyncedMax_Type()
)
connsyncSyncedMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connsyncSyncedMax.setStatus("current")
_ConnsyncDoubleSeen_ObjectIdentity = ObjectIdentity
connsyncDoubleSeen = _ConnsyncDoubleSeen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 60, 9)
)
_ConnsyncDoubleSeenVal_Type = Counter64
_ConnsyncDoubleSeenVal_Object = MibScalar
connsyncDoubleSeenVal = _ConnsyncDoubleSeenVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 60, 9, 1),
    _ConnsyncDoubleSeenVal_Type()
)
connsyncDoubleSeenVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connsyncDoubleSeenVal.setStatus("current")
_ConnsyncDoubleSeenMom_Type = CounterBasedGauge64
_ConnsyncDoubleSeenMom_Object = MibScalar
connsyncDoubleSeenMom = _ConnsyncDoubleSeenMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 60, 9, 2),
    _ConnsyncDoubleSeenMom_Type()
)
connsyncDoubleSeenMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connsyncDoubleSeenMom.setStatus("current")
_ConnsyncDoubleSeenMax_Type = CounterBasedGauge64
_ConnsyncDoubleSeenMax_Object = MibScalar
connsyncDoubleSeenMax = _ConnsyncDoubleSeenMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 60, 9, 3),
    _ConnsyncDoubleSeenMax_Type()
)
connsyncDoubleSeenMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connsyncDoubleSeenMax.setStatus("current")
_ConnsyncHelloRcv_ObjectIdentity = ObjectIdentity
connsyncHelloRcv = _ConnsyncHelloRcv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 60, 10)
)
_ConnsyncHelloRcvVal_Type = Counter64
_ConnsyncHelloRcvVal_Object = MibScalar
connsyncHelloRcvVal = _ConnsyncHelloRcvVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 60, 10, 1),
    _ConnsyncHelloRcvVal_Type()
)
connsyncHelloRcvVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connsyncHelloRcvVal.setStatus("current")
_ConnsyncHelloRcvMom_Type = CounterBasedGauge64
_ConnsyncHelloRcvMom_Object = MibScalar
connsyncHelloRcvMom = _ConnsyncHelloRcvMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 60, 10, 2),
    _ConnsyncHelloRcvMom_Type()
)
connsyncHelloRcvMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connsyncHelloRcvMom.setStatus("current")
_ConnsyncHelloRcvMax_Type = CounterBasedGauge64
_ConnsyncHelloRcvMax_Object = MibScalar
connsyncHelloRcvMax = _ConnsyncHelloRcvMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 60, 10, 3),
    _ConnsyncHelloRcvMax_Type()
)
connsyncHelloRcvMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connsyncHelloRcvMax.setStatus("current")
_ConnsyncOutofsyncMissedRcv_ObjectIdentity = ObjectIdentity
connsyncOutofsyncMissedRcv = _ConnsyncOutofsyncMissedRcv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 60, 11)
)
_ConnsyncOutofsyncMissedRcvVal_Type = Counter64
_ConnsyncOutofsyncMissedRcvVal_Object = MibScalar
connsyncOutofsyncMissedRcvVal = _ConnsyncOutofsyncMissedRcvVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 60, 11, 1),
    _ConnsyncOutofsyncMissedRcvVal_Type()
)
connsyncOutofsyncMissedRcvVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connsyncOutofsyncMissedRcvVal.setStatus("current")
_ConnsyncOutofsyncMissedRcvMom_Type = CounterBasedGauge64
_ConnsyncOutofsyncMissedRcvMom_Object = MibScalar
connsyncOutofsyncMissedRcvMom = _ConnsyncOutofsyncMissedRcvMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 60, 11, 2),
    _ConnsyncOutofsyncMissedRcvMom_Type()
)
connsyncOutofsyncMissedRcvMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connsyncOutofsyncMissedRcvMom.setStatus("current")
_ConnsyncOutofsyncMissedRcvMax_Type = CounterBasedGauge64
_ConnsyncOutofsyncMissedRcvMax_Object = MibScalar
connsyncOutofsyncMissedRcvMax = _ConnsyncOutofsyncMissedRcvMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 60, 11, 3),
    _ConnsyncOutofsyncMissedRcvMax_Type()
)
connsyncOutofsyncMissedRcvMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connsyncOutofsyncMissedRcvMax.setStatus("current")
_ConnsyncOutofsyncCollision_ObjectIdentity = ObjectIdentity
connsyncOutofsyncCollision = _ConnsyncOutofsyncCollision_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 60, 12)
)
_ConnsyncOutofsyncCollisionVal_Type = Counter64
_ConnsyncOutofsyncCollisionVal_Object = MibScalar
connsyncOutofsyncCollisionVal = _ConnsyncOutofsyncCollisionVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 60, 12, 1),
    _ConnsyncOutofsyncCollisionVal_Type()
)
connsyncOutofsyncCollisionVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connsyncOutofsyncCollisionVal.setStatus("current")
_ConnsyncOutofsyncCollisionMom_Type = CounterBasedGauge64
_ConnsyncOutofsyncCollisionMom_Object = MibScalar
connsyncOutofsyncCollisionMom = _ConnsyncOutofsyncCollisionMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 60, 12, 2),
    _ConnsyncOutofsyncCollisionMom_Type()
)
connsyncOutofsyncCollisionMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connsyncOutofsyncCollisionMom.setStatus("current")
_ConnsyncOutofsyncCollisionMax_Type = CounterBasedGauge64
_ConnsyncOutofsyncCollisionMax_Object = MibScalar
connsyncOutofsyncCollisionMax = _ConnsyncOutofsyncCollisionMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 60, 12, 3),
    _ConnsyncOutofsyncCollisionMax_Type()
)
connsyncOutofsyncCollisionMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connsyncOutofsyncCollisionMax.setStatus("current")
_ConnsyncBadAdler_ObjectIdentity = ObjectIdentity
connsyncBadAdler = _ConnsyncBadAdler_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 60, 13)
)
_ConnsyncBadAdlerVal_Type = Counter64
_ConnsyncBadAdlerVal_Object = MibScalar
connsyncBadAdlerVal = _ConnsyncBadAdlerVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 60, 13, 1),
    _ConnsyncBadAdlerVal_Type()
)
connsyncBadAdlerVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connsyncBadAdlerVal.setStatus("current")
_ConnsyncBadAdlerMom_Type = CounterBasedGauge64
_ConnsyncBadAdlerMom_Object = MibScalar
connsyncBadAdlerMom = _ConnsyncBadAdlerMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 60, 13, 2),
    _ConnsyncBadAdlerMom_Type()
)
connsyncBadAdlerMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connsyncBadAdlerMom.setStatus("current")
_ConnsyncBadAdlerMax_Type = CounterBasedGauge64
_ConnsyncBadAdlerMax_Object = MibScalar
connsyncBadAdlerMax = _ConnsyncBadAdlerMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 60, 13, 3),
    _ConnsyncBadAdlerMax_Type()
)
connsyncBadAdlerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connsyncBadAdlerMax.setStatus("current")
_ConnsyncPktOverflow_ObjectIdentity = ObjectIdentity
connsyncPktOverflow = _ConnsyncPktOverflow_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 60, 14)
)
_ConnsyncPktOverflowVal_Type = Counter64
_ConnsyncPktOverflowVal_Object = MibScalar
connsyncPktOverflowVal = _ConnsyncPktOverflowVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 60, 14, 1),
    _ConnsyncPktOverflowVal_Type()
)
connsyncPktOverflowVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connsyncPktOverflowVal.setStatus("current")
_ConnsyncPktOverflowMom_Type = CounterBasedGauge64
_ConnsyncPktOverflowMom_Object = MibScalar
connsyncPktOverflowMom = _ConnsyncPktOverflowMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 60, 14, 2),
    _ConnsyncPktOverflowMom_Type()
)
connsyncPktOverflowMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connsyncPktOverflowMom.setStatus("current")
_ConnsyncPktOverflowMax_Type = CounterBasedGauge64
_ConnsyncPktOverflowMax_Object = MibScalar
connsyncPktOverflowMax = _ConnsyncPktOverflowMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 60, 14, 3),
    _ConnsyncPktOverflowMax_Type()
)
connsyncPktOverflowMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connsyncPktOverflowMax.setStatus("current")
_ConnsyncCorruptPkt_ObjectIdentity = ObjectIdentity
connsyncCorruptPkt = _ConnsyncCorruptPkt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 60, 15)
)
_ConnsyncCorruptPktVal_Type = Counter64
_ConnsyncCorruptPktVal_Object = MibScalar
connsyncCorruptPktVal = _ConnsyncCorruptPktVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 60, 15, 1),
    _ConnsyncCorruptPktVal_Type()
)
connsyncCorruptPktVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connsyncCorruptPktVal.setStatus("current")
_ConnsyncCorruptPktMom_Type = CounterBasedGauge64
_ConnsyncCorruptPktMom_Object = MibScalar
connsyncCorruptPktMom = _ConnsyncCorruptPktMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 60, 15, 2),
    _ConnsyncCorruptPktMom_Type()
)
connsyncCorruptPktMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connsyncCorruptPktMom.setStatus("current")
_ConnsyncCorruptPktMax_Type = CounterBasedGauge64
_ConnsyncCorruptPktMax_Object = MibScalar
connsyncCorruptPktMax = _ConnsyncCorruptPktMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 60, 15, 3),
    _ConnsyncCorruptPktMax_Type()
)
connsyncCorruptPktMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connsyncCorruptPktMax.setStatus("current")
_ConnsyncConnNotfound_ObjectIdentity = ObjectIdentity
connsyncConnNotfound = _ConnsyncConnNotfound_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 60, 16)
)
_ConnsyncConnNotfoundVal_Type = Counter64
_ConnsyncConnNotfoundVal_Object = MibScalar
connsyncConnNotfoundVal = _ConnsyncConnNotfoundVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 60, 16, 1),
    _ConnsyncConnNotfoundVal_Type()
)
connsyncConnNotfoundVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connsyncConnNotfoundVal.setStatus("current")
_ConnsyncConnNotfoundMom_Type = CounterBasedGauge64
_ConnsyncConnNotfoundMom_Object = MibScalar
connsyncConnNotfoundMom = _ConnsyncConnNotfoundMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 60, 16, 2),
    _ConnsyncConnNotfoundMom_Type()
)
connsyncConnNotfoundMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connsyncConnNotfoundMom.setStatus("current")
_ConnsyncConnNotfoundMax_Type = CounterBasedGauge64
_ConnsyncConnNotfoundMax_Object = MibScalar
connsyncConnNotfoundMax = _ConnsyncConnNotfoundMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 60, 16, 3),
    _ConnsyncConnNotfoundMax_Type()
)
connsyncConnNotfoundMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connsyncConnNotfoundMax.setStatus("current")
_ConnsyncBadVer_ObjectIdentity = ObjectIdentity
connsyncBadVer = _ConnsyncBadVer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 60, 17)
)
_ConnsyncBadVerVal_Type = Counter64
_ConnsyncBadVerVal_Object = MibScalar
connsyncBadVerVal = _ConnsyncBadVerVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 60, 17, 1),
    _ConnsyncBadVerVal_Type()
)
connsyncBadVerVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connsyncBadVerVal.setStatus("current")
_ConnsyncBadVerMom_Type = CounterBasedGauge64
_ConnsyncBadVerMom_Object = MibScalar
connsyncBadVerMom = _ConnsyncBadVerMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 60, 17, 2),
    _ConnsyncBadVerMom_Type()
)
connsyncBadVerMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connsyncBadVerMom.setStatus("current")
_ConnsyncBadVerMax_Type = CounterBasedGauge64
_ConnsyncBadVerMax_Object = MibScalar
connsyncBadVerMax = _ConnsyncBadVerMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 60, 17, 3),
    _ConnsyncBadVerMax_Type()
)
connsyncBadVerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connsyncBadVerMax.setStatus("current")
_ConnsyncBadType_ObjectIdentity = ObjectIdentity
connsyncBadType = _ConnsyncBadType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 60, 18)
)
_ConnsyncBadTypeVal_Type = Counter64
_ConnsyncBadTypeVal_Object = MibScalar
connsyncBadTypeVal = _ConnsyncBadTypeVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 60, 18, 1),
    _ConnsyncBadTypeVal_Type()
)
connsyncBadTypeVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connsyncBadTypeVal.setStatus("current")
_ConnsyncBadTypeMom_Type = CounterBasedGauge64
_ConnsyncBadTypeMom_Object = MibScalar
connsyncBadTypeMom = _ConnsyncBadTypeMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 60, 18, 2),
    _ConnsyncBadTypeMom_Type()
)
connsyncBadTypeMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connsyncBadTypeMom.setStatus("current")
_ConnsyncBadTypeMax_Type = CounterBasedGauge64
_ConnsyncBadTypeMax_Object = MibScalar
connsyncBadTypeMax = _ConnsyncBadTypeMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 60, 18, 3),
    _ConnsyncBadTypeMax_Type()
)
connsyncBadTypeMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connsyncBadTypeMax.setStatus("current")
_ConnsyncBadEngineid_ObjectIdentity = ObjectIdentity
connsyncBadEngineid = _ConnsyncBadEngineid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 60, 19)
)
_ConnsyncBadEngineidVal_Type = Counter64
_ConnsyncBadEngineidVal_Object = MibScalar
connsyncBadEngineidVal = _ConnsyncBadEngineidVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 60, 19, 1),
    _ConnsyncBadEngineidVal_Type()
)
connsyncBadEngineidVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connsyncBadEngineidVal.setStatus("current")
_ConnsyncBadEngineidMom_Type = CounterBasedGauge64
_ConnsyncBadEngineidMom_Object = MibScalar
connsyncBadEngineidMom = _ConnsyncBadEngineidMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 60, 19, 2),
    _ConnsyncBadEngineidMom_Type()
)
connsyncBadEngineidMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connsyncBadEngineidMom.setStatus("current")
_ConnsyncBadEngineidMax_Type = CounterBasedGauge64
_ConnsyncBadEngineidMax_Object = MibScalar
connsyncBadEngineidMax = _ConnsyncBadEngineidMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 60, 19, 3),
    _ConnsyncBadEngineidMax_Type()
)
connsyncBadEngineidMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connsyncBadEngineidMax.setStatus("current")
_ConnsyncUdpSnt_ObjectIdentity = ObjectIdentity
connsyncUdpSnt = _ConnsyncUdpSnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 60, 20)
)
_ConnsyncUdpSntVal_Type = Counter64
_ConnsyncUdpSntVal_Object = MibScalar
connsyncUdpSntVal = _ConnsyncUdpSntVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 60, 20, 1),
    _ConnsyncUdpSntVal_Type()
)
connsyncUdpSntVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connsyncUdpSntVal.setStatus("current")
_ConnsyncUdpSntMom_Type = CounterBasedGauge64
_ConnsyncUdpSntMom_Object = MibScalar
connsyncUdpSntMom = _ConnsyncUdpSntMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 60, 20, 2),
    _ConnsyncUdpSntMom_Type()
)
connsyncUdpSntMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connsyncUdpSntMom.setStatus("current")
_ConnsyncUdpSntMax_Type = CounterBasedGauge64
_ConnsyncUdpSntMax_Object = MibScalar
connsyncUdpSntMax = _ConnsyncUdpSntMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 60, 20, 3),
    _ConnsyncUdpSntMax_Type()
)
connsyncUdpSntMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connsyncUdpSntMax.setStatus("current")
_ConnsyncUdpRcv_ObjectIdentity = ObjectIdentity
connsyncUdpRcv = _ConnsyncUdpRcv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 60, 21)
)
_ConnsyncUdpRcvVal_Type = Counter64
_ConnsyncUdpRcvVal_Object = MibScalar
connsyncUdpRcvVal = _ConnsyncUdpRcvVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 60, 21, 1),
    _ConnsyncUdpRcvVal_Type()
)
connsyncUdpRcvVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connsyncUdpRcvVal.setStatus("current")
_ConnsyncUdpRcvMom_Type = CounterBasedGauge64
_ConnsyncUdpRcvMom_Object = MibScalar
connsyncUdpRcvMom = _ConnsyncUdpRcvMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 60, 21, 2),
    _ConnsyncUdpRcvMom_Type()
)
connsyncUdpRcvMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connsyncUdpRcvMom.setStatus("current")
_ConnsyncUdpRcvMax_Type = CounterBasedGauge64
_ConnsyncUdpRcvMax_Object = MibScalar
connsyncUdpRcvMax = _ConnsyncUdpRcvMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 60, 21, 3),
    _ConnsyncUdpRcvMax_Type()
)
connsyncUdpRcvMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connsyncUdpRcvMax.setStatus("current")
_Ruleset_ObjectIdentity = ObjectIdentity
ruleset = _Ruleset_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 64)
)
_RulesetReceived_ObjectIdentity = ObjectIdentity
rulesetReceived = _RulesetReceived_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 64, 1)
)
_RulesetReceivedVal_Type = Counter64
_RulesetReceivedVal_Object = MibScalar
rulesetReceivedVal = _RulesetReceivedVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 64, 1, 1),
    _RulesetReceivedVal_Type()
)
rulesetReceivedVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rulesetReceivedVal.setStatus("current")
_RulesetReceivedMom_Type = CounterBasedGauge64
_RulesetReceivedMom_Object = MibScalar
rulesetReceivedMom = _RulesetReceivedMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 64, 1, 2),
    _RulesetReceivedMom_Type()
)
rulesetReceivedMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rulesetReceivedMom.setStatus("current")
_RulesetReceivedMax_Type = CounterBasedGauge64
_RulesetReceivedMax_Object = MibScalar
rulesetReceivedMax = _RulesetReceivedMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 64, 1, 3),
    _RulesetReceivedMax_Type()
)
rulesetReceivedMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rulesetReceivedMax.setStatus("current")
_RulesetFwrules_ObjectIdentity = ObjectIdentity
rulesetFwrules = _RulesetFwrules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 64, 5)
)
_RulesetFwrulesVal_Type = CounterBasedGauge64
_RulesetFwrulesVal_Object = MibScalar
rulesetFwrulesVal = _RulesetFwrulesVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 64, 5, 1),
    _RulesetFwrulesVal_Type()
)
rulesetFwrulesVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rulesetFwrulesVal.setStatus("current")
_RulesetFwrulesMax_Type = CounterBasedGauge64
_RulesetFwrulesMax_Object = MibScalar
rulesetFwrulesMax = _RulesetFwrulesMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 64, 5, 3),
    _RulesetFwrulesMax_Type()
)
rulesetFwrulesMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rulesetFwrulesMax.setStatus("current")
_RulesetShapingrules_ObjectIdentity = ObjectIdentity
rulesetShapingrules = _RulesetShapingrules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 64, 6)
)
_RulesetShapingrulesVal_Type = CounterBasedGauge64
_RulesetShapingrulesVal_Object = MibScalar
rulesetShapingrulesVal = _RulesetShapingrulesVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 64, 6, 1),
    _RulesetShapingrulesVal_Type()
)
rulesetShapingrulesVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rulesetShapingrulesVal.setStatus("current")
_RulesetShapingrulesMax_Type = CounterBasedGauge64
_RulesetShapingrulesMax_Object = MibScalar
rulesetShapingrulesMax = _RulesetShapingrulesMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 64, 6, 3),
    _RulesetShapingrulesMax_Type()
)
rulesetShapingrulesMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rulesetShapingrulesMax.setStatus("current")
_RulesetClienttreeSize_ObjectIdentity = ObjectIdentity
rulesetClienttreeSize = _RulesetClienttreeSize_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 64, 7)
)
_RulesetClienttreeSizeVal_Type = CounterBasedGauge64
_RulesetClienttreeSizeVal_Object = MibScalar
rulesetClienttreeSizeVal = _RulesetClienttreeSizeVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 64, 7, 1),
    _RulesetClienttreeSizeVal_Type()
)
rulesetClienttreeSizeVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rulesetClienttreeSizeVal.setStatus("current")
_RulesetClienttreeSizeMax_Type = CounterBasedGauge64
_RulesetClienttreeSizeMax_Object = MibScalar
rulesetClienttreeSizeMax = _RulesetClienttreeSizeMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 64, 7, 3),
    _RulesetClienttreeSizeMax_Type()
)
rulesetClienttreeSizeMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rulesetClienttreeSizeMax.setStatus("current")
_RulesetServertreeSize_ObjectIdentity = ObjectIdentity
rulesetServertreeSize = _RulesetServertreeSize_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 64, 8)
)
_RulesetServertreeSizeVal_Type = CounterBasedGauge64
_RulesetServertreeSizeVal_Object = MibScalar
rulesetServertreeSizeVal = _RulesetServertreeSizeVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 64, 8, 1),
    _RulesetServertreeSizeVal_Type()
)
rulesetServertreeSizeVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rulesetServertreeSizeVal.setStatus("current")
_RulesetServertreeSizeMax_Type = CounterBasedGauge64
_RulesetServertreeSizeMax_Object = MibScalar
rulesetServertreeSizeMax = _RulesetServertreeSizeMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 64, 8, 3),
    _RulesetServertreeSizeMax_Type()
)
rulesetServertreeSizeMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rulesetServertreeSizeMax.setStatus("current")
_RulesetBgpNumpaths_ObjectIdentity = ObjectIdentity
rulesetBgpNumpaths = _RulesetBgpNumpaths_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 64, 9)
)
_RulesetBgpNumpathsVal_Type = CounterBasedGauge64
_RulesetBgpNumpathsVal_Object = MibScalar
rulesetBgpNumpathsVal = _RulesetBgpNumpathsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 64, 9, 1),
    _RulesetBgpNumpathsVal_Type()
)
rulesetBgpNumpathsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rulesetBgpNumpathsVal.setStatus("current")
_RulesetBgpNumpathsMax_Type = CounterBasedGauge64
_RulesetBgpNumpathsMax_Object = MibScalar
rulesetBgpNumpathsMax = _RulesetBgpNumpathsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 64, 9, 3),
    _RulesetBgpNumpathsMax_Type()
)
rulesetBgpNumpathsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rulesetBgpNumpathsMax.setStatus("current")
_RulesetBgpTreesize_ObjectIdentity = ObjectIdentity
rulesetBgpTreesize = _RulesetBgpTreesize_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 64, 10)
)
_RulesetBgpTreesizeVal_Type = CounterBasedGauge64
_RulesetBgpTreesizeVal_Object = MibScalar
rulesetBgpTreesizeVal = _RulesetBgpTreesizeVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 64, 10, 1),
    _RulesetBgpTreesizeVal_Type()
)
rulesetBgpTreesizeVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rulesetBgpTreesizeVal.setStatus("current")
_RulesetBgpTreesizeMax_Type = CounterBasedGauge64
_RulesetBgpTreesizeMax_Object = MibScalar
rulesetBgpTreesizeMax = _RulesetBgpTreesizeMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 64, 10, 3),
    _RulesetBgpTreesizeMax_Type()
)
rulesetBgpTreesizeMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rulesetBgpTreesizeMax.setStatus("current")
_RulesetBgpNumLookup_ObjectIdentity = ObjectIdentity
rulesetBgpNumLookup = _RulesetBgpNumLookup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 64, 12)
)
_RulesetBgpNumLookupVal_Type = Counter64
_RulesetBgpNumLookupVal_Object = MibScalar
rulesetBgpNumLookupVal = _RulesetBgpNumLookupVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 64, 12, 1),
    _RulesetBgpNumLookupVal_Type()
)
rulesetBgpNumLookupVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rulesetBgpNumLookupVal.setStatus("current")
_RulesetBgpNumLookupMom_Type = CounterBasedGauge64
_RulesetBgpNumLookupMom_Object = MibScalar
rulesetBgpNumLookupMom = _RulesetBgpNumLookupMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 64, 12, 2),
    _RulesetBgpNumLookupMom_Type()
)
rulesetBgpNumLookupMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rulesetBgpNumLookupMom.setStatus("current")
_RulesetBgpNumLookupMax_Type = CounterBasedGauge64
_RulesetBgpNumLookupMax_Object = MibScalar
rulesetBgpNumLookupMax = _RulesetBgpNumLookupMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 64, 12, 3),
    _RulesetBgpNumLookupMax_Type()
)
rulesetBgpNumLookupMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rulesetBgpNumLookupMax.setStatus("current")
_RulesetPropChecks_ObjectIdentity = ObjectIdentity
rulesetPropChecks = _RulesetPropChecks_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 64, 13)
)
_RulesetPropChecksVal_Type = Counter64
_RulesetPropChecksVal_Object = MibScalar
rulesetPropChecksVal = _RulesetPropChecksVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 64, 13, 1),
    _RulesetPropChecksVal_Type()
)
rulesetPropChecksVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rulesetPropChecksVal.setStatus("current")
_RulesetPropChecksMom_Type = CounterBasedGauge64
_RulesetPropChecksMom_Object = MibScalar
rulesetPropChecksMom = _RulesetPropChecksMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 64, 13, 2),
    _RulesetPropChecksMom_Type()
)
rulesetPropChecksMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rulesetPropChecksMom.setStatus("current")
_RulesetPropChecksMax_Type = CounterBasedGauge64
_RulesetPropChecksMax_Object = MibScalar
rulesetPropChecksMax = _RulesetPropChecksMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 64, 13, 3),
    _RulesetPropChecksMax_Type()
)
rulesetPropChecksMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rulesetPropChecksMax.setStatus("current")
_RulesetBitmasksAvg_ObjectIdentity = ObjectIdentity
rulesetBitmasksAvg = _RulesetBitmasksAvg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 64, 15)
)
_RulesetBitmasksAvgVal_Type = CounterBasedGauge64
_RulesetBitmasksAvgVal_Object = MibScalar
rulesetBitmasksAvgVal = _RulesetBitmasksAvgVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 64, 15, 1),
    _RulesetBitmasksAvgVal_Type()
)
rulesetBitmasksAvgVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rulesetBitmasksAvgVal.setStatus("current")
_RulesetBitmasksAvgMax_Type = CounterBasedGauge64
_RulesetBitmasksAvgMax_Object = MibScalar
rulesetBitmasksAvgMax = _RulesetBitmasksAvgMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 64, 15, 3),
    _RulesetBitmasksAvgMax_Type()
)
rulesetBitmasksAvgMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rulesetBitmasksAvgMax.setStatus("current")
_RulesetBitmasksMax_ObjectIdentity = ObjectIdentity
rulesetBitmasksMax = _RulesetBitmasksMax_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 64, 16)
)
_RulesetBitmasksMaxVal_Type = CounterBasedGauge64
_RulesetBitmasksMaxVal_Object = MibScalar
rulesetBitmasksMaxVal = _RulesetBitmasksMaxVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 64, 16, 1),
    _RulesetBitmasksMaxVal_Type()
)
rulesetBitmasksMaxVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rulesetBitmasksMaxVal.setStatus("current")
_RulesetBitmasksMaxMax_Type = CounterBasedGauge64
_RulesetBitmasksMaxMax_Object = MibScalar
rulesetBitmasksMaxMax = _RulesetBitmasksMaxMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 64, 16, 3),
    _RulesetBitmasksMaxMax_Type()
)
rulesetBitmasksMaxMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rulesetBitmasksMaxMax.setStatus("current")
_RulesetDynipAdd_ObjectIdentity = ObjectIdentity
rulesetDynipAdd = _RulesetDynipAdd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 64, 17)
)
_RulesetDynipAddVal_Type = Counter64
_RulesetDynipAddVal_Object = MibScalar
rulesetDynipAddVal = _RulesetDynipAddVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 64, 17, 1),
    _RulesetDynipAddVal_Type()
)
rulesetDynipAddVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rulesetDynipAddVal.setStatus("current")
_RulesetDynipAddMom_Type = CounterBasedGauge64
_RulesetDynipAddMom_Object = MibScalar
rulesetDynipAddMom = _RulesetDynipAddMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 64, 17, 2),
    _RulesetDynipAddMom_Type()
)
rulesetDynipAddMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rulesetDynipAddMom.setStatus("current")
_RulesetDynipAddMax_Type = CounterBasedGauge64
_RulesetDynipAddMax_Object = MibScalar
rulesetDynipAddMax = _RulesetDynipAddMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 64, 17, 3),
    _RulesetDynipAddMax_Type()
)
rulesetDynipAddMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rulesetDynipAddMax.setStatus("current")
_RulesetDynipRemove_ObjectIdentity = ObjectIdentity
rulesetDynipRemove = _RulesetDynipRemove_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 64, 18)
)
_RulesetDynipRemoveVal_Type = Counter64
_RulesetDynipRemoveVal_Object = MibScalar
rulesetDynipRemoveVal = _RulesetDynipRemoveVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 64, 18, 1),
    _RulesetDynipRemoveVal_Type()
)
rulesetDynipRemoveVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rulesetDynipRemoveVal.setStatus("current")
_RulesetDynipRemoveMom_Type = CounterBasedGauge64
_RulesetDynipRemoveMom_Object = MibScalar
rulesetDynipRemoveMom = _RulesetDynipRemoveMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 64, 18, 2),
    _RulesetDynipRemoveMom_Type()
)
rulesetDynipRemoveMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rulesetDynipRemoveMom.setStatus("current")
_RulesetDynipRemoveMax_Type = CounterBasedGauge64
_RulesetDynipRemoveMax_Object = MibScalar
rulesetDynipRemoveMax = _RulesetDynipRemoveMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 64, 18, 3),
    _RulesetDynipRemoveMax_Type()
)
rulesetDynipRemoveMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rulesetDynipRemoveMax.setStatus("current")
_RulesetLastUpdate_ObjectIdentity = ObjectIdentity
rulesetLastUpdate = _RulesetLastUpdate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 64, 22)
)
_RulesetLastUpdateVal_Type = DateAndTime
_RulesetLastUpdateVal_Object = MibScalar
rulesetLastUpdateVal = _RulesetLastUpdateVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 64, 22, 1),
    _RulesetLastUpdateVal_Type()
)
rulesetLastUpdateVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rulesetLastUpdateVal.setStatus("current")
_RulesetDynipNum_ObjectIdentity = ObjectIdentity
rulesetDynipNum = _RulesetDynipNum_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 64, 23)
)
_RulesetDynipNumVal_Type = CounterBasedGauge64
_RulesetDynipNumVal_Object = MibScalar
rulesetDynipNumVal = _RulesetDynipNumVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 64, 23, 1),
    _RulesetDynipNumVal_Type()
)
rulesetDynipNumVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rulesetDynipNumVal.setStatus("current")
_RulesetDynipNumMax_Type = CounterBasedGauge64
_RulesetDynipNumMax_Object = MibScalar
rulesetDynipNumMax = _RulesetDynipNumMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 64, 23, 3),
    _RulesetDynipNumMax_Type()
)
rulesetDynipNumMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rulesetDynipNumMax.setStatus("current")
_RulesetStatisticsrules_ObjectIdentity = ObjectIdentity
rulesetStatisticsrules = _RulesetStatisticsrules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 64, 24)
)
_RulesetStatisticsrulesVal_Type = CounterBasedGauge64
_RulesetStatisticsrulesVal_Object = MibScalar
rulesetStatisticsrulesVal = _RulesetStatisticsrulesVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 64, 24, 1),
    _RulesetStatisticsrulesVal_Type()
)
rulesetStatisticsrulesVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rulesetStatisticsrulesVal.setStatus("current")
_RulesetStatisticsrulesMax_Type = CounterBasedGauge64
_RulesetStatisticsrulesMax_Object = MibScalar
rulesetStatisticsrulesMax = _RulesetStatisticsrulesMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 64, 24, 3),
    _RulesetStatisticsrulesMax_Type()
)
rulesetStatisticsrulesMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rulesetStatisticsrulesMax.setStatus("current")
_RulesetLocaltreeSize_ObjectIdentity = ObjectIdentity
rulesetLocaltreeSize = _RulesetLocaltreeSize_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 64, 25)
)
_RulesetLocaltreeSizeVal_Type = CounterBasedGauge64
_RulesetLocaltreeSizeVal_Object = MibScalar
rulesetLocaltreeSizeVal = _RulesetLocaltreeSizeVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 64, 25, 1),
    _RulesetLocaltreeSizeVal_Type()
)
rulesetLocaltreeSizeVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rulesetLocaltreeSizeVal.setStatus("current")
_RulesetLocaltreeSizeMax_Type = CounterBasedGauge64
_RulesetLocaltreeSizeMax_Object = MibScalar
rulesetLocaltreeSizeMax = _RulesetLocaltreeSizeMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 64, 25, 3),
    _RulesetLocaltreeSizeMax_Type()
)
rulesetLocaltreeSizeMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rulesetLocaltreeSizeMax.setStatus("current")
_RulesetStatisticsRuleOverflow_ObjectIdentity = ObjectIdentity
rulesetStatisticsRuleOverflow = _RulesetStatisticsRuleOverflow_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 64, 26)
)
_RulesetStatisticsRuleOverflowVal_Type = Counter64
_RulesetStatisticsRuleOverflowVal_Object = MibScalar
rulesetStatisticsRuleOverflowVal = _RulesetStatisticsRuleOverflowVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 64, 26, 1),
    _RulesetStatisticsRuleOverflowVal_Type()
)
rulesetStatisticsRuleOverflowVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rulesetStatisticsRuleOverflowVal.setStatus("current")
_RulesetStatisticsRuleOverflowMom_Type = CounterBasedGauge64
_RulesetStatisticsRuleOverflowMom_Object = MibScalar
rulesetStatisticsRuleOverflowMom = _RulesetStatisticsRuleOverflowMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 64, 26, 2),
    _RulesetStatisticsRuleOverflowMom_Type()
)
rulesetStatisticsRuleOverflowMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rulesetStatisticsRuleOverflowMom.setStatus("current")
_RulesetStatisticsRuleOverflowMax_Type = CounterBasedGauge64
_RulesetStatisticsRuleOverflowMax_Object = MibScalar
rulesetStatisticsRuleOverflowMax = _RulesetStatisticsRuleOverflowMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 64, 26, 3),
    _RulesetStatisticsRuleOverflowMax_Type()
)
rulesetStatisticsRuleOverflowMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rulesetStatisticsRuleOverflowMax.setStatus("current")
_RulesetConnStatechange_ObjectIdentity = ObjectIdentity
rulesetConnStatechange = _RulesetConnStatechange_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 64, 27)
)
_RulesetConnStatechangeVal_Type = Counter64
_RulesetConnStatechangeVal_Object = MibScalar
rulesetConnStatechangeVal = _RulesetConnStatechangeVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 64, 27, 1),
    _RulesetConnStatechangeVal_Type()
)
rulesetConnStatechangeVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rulesetConnStatechangeVal.setStatus("current")
_RulesetConnStatechangeMom_Type = CounterBasedGauge64
_RulesetConnStatechangeMom_Object = MibScalar
rulesetConnStatechangeMom = _RulesetConnStatechangeMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 64, 27, 2),
    _RulesetConnStatechangeMom_Type()
)
rulesetConnStatechangeMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rulesetConnStatechangeMom.setStatus("current")
_RulesetConnStatechangeMax_Type = CounterBasedGauge64
_RulesetConnStatechangeMax_Object = MibScalar
rulesetConnStatechangeMax = _RulesetConnStatechangeMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 64, 27, 3),
    _RulesetConnStatechangeMax_Type()
)
rulesetConnStatechangeMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rulesetConnStatechangeMax.setStatus("current")
_RulesetConnStatechangeProp_ObjectIdentity = ObjectIdentity
rulesetConnStatechangeProp = _RulesetConnStatechangeProp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 64, 28)
)
_RulesetConnStatechangePropVal_Type = Counter64
_RulesetConnStatechangePropVal_Object = MibScalar
rulesetConnStatechangePropVal = _RulesetConnStatechangePropVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 64, 28, 1),
    _RulesetConnStatechangePropVal_Type()
)
rulesetConnStatechangePropVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rulesetConnStatechangePropVal.setStatus("current")
_RulesetConnStatechangePropMom_Type = CounterBasedGauge64
_RulesetConnStatechangePropMom_Object = MibScalar
rulesetConnStatechangePropMom = _RulesetConnStatechangePropMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 64, 28, 2),
    _RulesetConnStatechangePropMom_Type()
)
rulesetConnStatechangePropMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rulesetConnStatechangePropMom.setStatus("current")
_RulesetConnStatechangePropMax_Type = CounterBasedGauge64
_RulesetConnStatechangePropMax_Object = MibScalar
rulesetConnStatechangePropMax = _RulesetConnStatechangePropMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 64, 28, 3),
    _RulesetConnStatechangePropMax_Type()
)
rulesetConnStatechangePropMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rulesetConnStatechangePropMax.setStatus("current")
_RulesetConnStatechangeService_ObjectIdentity = ObjectIdentity
rulesetConnStatechangeService = _RulesetConnStatechangeService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 64, 29)
)
_RulesetConnStatechangeServiceVal_Type = Counter64
_RulesetConnStatechangeServiceVal_Object = MibScalar
rulesetConnStatechangeServiceVal = _RulesetConnStatechangeServiceVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 64, 29, 1),
    _RulesetConnStatechangeServiceVal_Type()
)
rulesetConnStatechangeServiceVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rulesetConnStatechangeServiceVal.setStatus("current")
_RulesetConnStatechangeServiceMom_Type = CounterBasedGauge64
_RulesetConnStatechangeServiceMom_Object = MibScalar
rulesetConnStatechangeServiceMom = _RulesetConnStatechangeServiceMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 64, 29, 2),
    _RulesetConnStatechangeServiceMom_Type()
)
rulesetConnStatechangeServiceMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rulesetConnStatechangeServiceMom.setStatus("current")
_RulesetConnStatechangeServiceMax_Type = CounterBasedGauge64
_RulesetConnStatechangeServiceMax_Object = MibScalar
rulesetConnStatechangeServiceMax = _RulesetConnStatechangeServiceMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 64, 29, 3),
    _RulesetConnStatechangeServiceMax_Type()
)
rulesetConnStatechangeServiceMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rulesetConnStatechangeServiceMax.setStatus("current")
_RulesetConnStatechangeFlags_ObjectIdentity = ObjectIdentity
rulesetConnStatechangeFlags = _RulesetConnStatechangeFlags_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 64, 30)
)
_RulesetConnStatechangeFlagsVal_Type = Counter64
_RulesetConnStatechangeFlagsVal_Object = MibScalar
rulesetConnStatechangeFlagsVal = _RulesetConnStatechangeFlagsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 64, 30, 1),
    _RulesetConnStatechangeFlagsVal_Type()
)
rulesetConnStatechangeFlagsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rulesetConnStatechangeFlagsVal.setStatus("current")
_RulesetConnStatechangeFlagsMom_Type = CounterBasedGauge64
_RulesetConnStatechangeFlagsMom_Object = MibScalar
rulesetConnStatechangeFlagsMom = _RulesetConnStatechangeFlagsMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 64, 30, 2),
    _RulesetConnStatechangeFlagsMom_Type()
)
rulesetConnStatechangeFlagsMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rulesetConnStatechangeFlagsMom.setStatus("current")
_RulesetConnStatechangeFlagsMax_Type = CounterBasedGauge64
_RulesetConnStatechangeFlagsMax_Object = MibScalar
rulesetConnStatechangeFlagsMax = _RulesetConnStatechangeFlagsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 64, 30, 3),
    _RulesetConnStatechangeFlagsMax_Type()
)
rulesetConnStatechangeFlagsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rulesetConnStatechangeFlagsMax.setStatus("current")
_RulesetConnStatechangeAspath_ObjectIdentity = ObjectIdentity
rulesetConnStatechangeAspath = _RulesetConnStatechangeAspath_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 64, 31)
)
_RulesetConnStatechangeAspathVal_Type = Counter64
_RulesetConnStatechangeAspathVal_Object = MibScalar
rulesetConnStatechangeAspathVal = _RulesetConnStatechangeAspathVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 64, 31, 1),
    _RulesetConnStatechangeAspathVal_Type()
)
rulesetConnStatechangeAspathVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rulesetConnStatechangeAspathVal.setStatus("current")
_RulesetConnStatechangeAspathMom_Type = CounterBasedGauge64
_RulesetConnStatechangeAspathMom_Object = MibScalar
rulesetConnStatechangeAspathMom = _RulesetConnStatechangeAspathMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 64, 31, 2),
    _RulesetConnStatechangeAspathMom_Type()
)
rulesetConnStatechangeAspathMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rulesetConnStatechangeAspathMom.setStatus("current")
_RulesetConnStatechangeAspathMax_Type = CounterBasedGauge64
_RulesetConnStatechangeAspathMax_Object = MibScalar
rulesetConnStatechangeAspathMax = _RulesetConnStatechangeAspathMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 64, 31, 3),
    _RulesetConnStatechangeAspathMax_Type()
)
rulesetConnStatechangeAspathMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rulesetConnStatechangeAspathMax.setStatus("current")
_RulesetRecalcVersion_ObjectIdentity = ObjectIdentity
rulesetRecalcVersion = _RulesetRecalcVersion_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 64, 32)
)
_RulesetRecalcVersionVal_Type = Counter64
_RulesetRecalcVersionVal_Object = MibScalar
rulesetRecalcVersionVal = _RulesetRecalcVersionVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 64, 32, 1),
    _RulesetRecalcVersionVal_Type()
)
rulesetRecalcVersionVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rulesetRecalcVersionVal.setStatus("current")
_RulesetRecalcVersionMom_Type = CounterBasedGauge64
_RulesetRecalcVersionMom_Object = MibScalar
rulesetRecalcVersionMom = _RulesetRecalcVersionMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 64, 32, 2),
    _RulesetRecalcVersionMom_Type()
)
rulesetRecalcVersionMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rulesetRecalcVersionMom.setStatus("current")
_RulesetRecalcVersionMax_Type = CounterBasedGauge64
_RulesetRecalcVersionMax_Object = MibScalar
rulesetRecalcVersionMax = _RulesetRecalcVersionMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 64, 32, 3),
    _RulesetRecalcVersionMax_Type()
)
rulesetRecalcVersionMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rulesetRecalcVersionMax.setStatus("current")
_RulesetRecalcTime_ObjectIdentity = ObjectIdentity
rulesetRecalcTime = _RulesetRecalcTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 64, 33)
)
_RulesetRecalcTimeVal_Type = Counter64
_RulesetRecalcTimeVal_Object = MibScalar
rulesetRecalcTimeVal = _RulesetRecalcTimeVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 64, 33, 1),
    _RulesetRecalcTimeVal_Type()
)
rulesetRecalcTimeVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rulesetRecalcTimeVal.setStatus("current")
_RulesetRecalcTimeMom_Type = CounterBasedGauge64
_RulesetRecalcTimeMom_Object = MibScalar
rulesetRecalcTimeMom = _RulesetRecalcTimeMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 64, 33, 2),
    _RulesetRecalcTimeMom_Type()
)
rulesetRecalcTimeMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rulesetRecalcTimeMom.setStatus("current")
_RulesetRecalcTimeMax_Type = CounterBasedGauge64
_RulesetRecalcTimeMax_Object = MibScalar
rulesetRecalcTimeMax = _RulesetRecalcTimeMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 64, 33, 3),
    _RulesetRecalcTimeMax_Type()
)
rulesetRecalcTimeMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rulesetRecalcTimeMax.setStatus("current")
_RulesetRecalcBgp_ObjectIdentity = ObjectIdentity
rulesetRecalcBgp = _RulesetRecalcBgp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 64, 34)
)
_RulesetRecalcBgpVal_Type = Counter64
_RulesetRecalcBgpVal_Object = MibScalar
rulesetRecalcBgpVal = _RulesetRecalcBgpVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 64, 34, 1),
    _RulesetRecalcBgpVal_Type()
)
rulesetRecalcBgpVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rulesetRecalcBgpVal.setStatus("current")
_RulesetRecalcBgpMom_Type = CounterBasedGauge64
_RulesetRecalcBgpMom_Object = MibScalar
rulesetRecalcBgpMom = _RulesetRecalcBgpMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 64, 34, 2),
    _RulesetRecalcBgpMom_Type()
)
rulesetRecalcBgpMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rulesetRecalcBgpMom.setStatus("current")
_RulesetRecalcBgpMax_Type = CounterBasedGauge64
_RulesetRecalcBgpMax_Object = MibScalar
rulesetRecalcBgpMax = _RulesetRecalcBgpMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 64, 34, 3),
    _RulesetRecalcBgpMax_Type()
)
rulesetRecalcBgpMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rulesetRecalcBgpMax.setStatus("current")
_RulesetRecalcUnknown_ObjectIdentity = ObjectIdentity
rulesetRecalcUnknown = _RulesetRecalcUnknown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 64, 35)
)
_RulesetRecalcUnknownVal_Type = Counter64
_RulesetRecalcUnknownVal_Object = MibScalar
rulesetRecalcUnknownVal = _RulesetRecalcUnknownVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 64, 35, 1),
    _RulesetRecalcUnknownVal_Type()
)
rulesetRecalcUnknownVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rulesetRecalcUnknownVal.setStatus("current")
_RulesetRecalcUnknownMom_Type = CounterBasedGauge64
_RulesetRecalcUnknownMom_Object = MibScalar
rulesetRecalcUnknownMom = _RulesetRecalcUnknownMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 64, 35, 2),
    _RulesetRecalcUnknownMom_Type()
)
rulesetRecalcUnknownMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rulesetRecalcUnknownMom.setStatus("current")
_RulesetRecalcUnknownMax_Type = CounterBasedGauge64
_RulesetRecalcUnknownMax_Object = MibScalar
rulesetRecalcUnknownMax = _RulesetRecalcUnknownMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 64, 35, 3),
    _RulesetRecalcUnknownMax_Type()
)
rulesetRecalcUnknownMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rulesetRecalcUnknownMax.setStatus("current")
_RulesetOutdatedService_ObjectIdentity = ObjectIdentity
rulesetOutdatedService = _RulesetOutdatedService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 64, 36)
)
_RulesetOutdatedServiceVal_Type = Counter64
_RulesetOutdatedServiceVal_Object = MibScalar
rulesetOutdatedServiceVal = _RulesetOutdatedServiceVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 64, 36, 1),
    _RulesetOutdatedServiceVal_Type()
)
rulesetOutdatedServiceVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rulesetOutdatedServiceVal.setStatus("current")
_RulesetOutdatedServiceMom_Type = CounterBasedGauge64
_RulesetOutdatedServiceMom_Object = MibScalar
rulesetOutdatedServiceMom = _RulesetOutdatedServiceMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 64, 36, 2),
    _RulesetOutdatedServiceMom_Type()
)
rulesetOutdatedServiceMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rulesetOutdatedServiceMom.setStatus("current")
_RulesetOutdatedServiceMax_Type = CounterBasedGauge64
_RulesetOutdatedServiceMax_Object = MibScalar
rulesetOutdatedServiceMax = _RulesetOutdatedServiceMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 64, 36, 3),
    _RulesetOutdatedServiceMax_Type()
)
rulesetOutdatedServiceMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rulesetOutdatedServiceMax.setStatus("current")
_RulesetSubscribers_ObjectIdentity = ObjectIdentity
rulesetSubscribers = _RulesetSubscribers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 64, 37)
)
_RulesetSubscribersVal_Type = CounterBasedGauge64
_RulesetSubscribersVal_Object = MibScalar
rulesetSubscribersVal = _RulesetSubscribersVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 64, 37, 1),
    _RulesetSubscribersVal_Type()
)
rulesetSubscribersVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rulesetSubscribersVal.setStatus("current")
_RulesetSubscribersMax_Type = CounterBasedGauge64
_RulesetSubscribersMax_Object = MibScalar
rulesetSubscribersMax = _RulesetSubscribersMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 64, 37, 3),
    _RulesetSubscribersMax_Type()
)
rulesetSubscribersMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rulesetSubscribersMax.setStatus("current")
_RulesetBadAspath_ObjectIdentity = ObjectIdentity
rulesetBadAspath = _RulesetBadAspath_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 64, 38)
)
_RulesetBadAspathVal_Type = Counter64
_RulesetBadAspathVal_Object = MibScalar
rulesetBadAspathVal = _RulesetBadAspathVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 64, 38, 1),
    _RulesetBadAspathVal_Type()
)
rulesetBadAspathVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rulesetBadAspathVal.setStatus("current")
_RulesetBadAspathMom_Type = CounterBasedGauge64
_RulesetBadAspathMom_Object = MibScalar
rulesetBadAspathMom = _RulesetBadAspathMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 64, 38, 2),
    _RulesetBadAspathMom_Type()
)
rulesetBadAspathMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rulesetBadAspathMom.setStatus("current")
_RulesetBadAspathMax_Type = CounterBasedGauge64
_RulesetBadAspathMax_Object = MibScalar
rulesetBadAspathMax = _RulesetBadAspathMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 64, 38, 3),
    _RulesetBadAspathMax_Type()
)
rulesetBadAspathMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rulesetBadAspathMax.setStatus("current")
_RulesetConnStatechangeLinklevel_ObjectIdentity = ObjectIdentity
rulesetConnStatechangeLinklevel = _RulesetConnStatechangeLinklevel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 64, 39)
)
_RulesetConnStatechangeLinklevelVal_Type = Counter64
_RulesetConnStatechangeLinklevelVal_Object = MibScalar
rulesetConnStatechangeLinklevelVal = _RulesetConnStatechangeLinklevelVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 64, 39, 1),
    _RulesetConnStatechangeLinklevelVal_Type()
)
rulesetConnStatechangeLinklevelVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rulesetConnStatechangeLinklevelVal.setStatus("current")
_RulesetConnStatechangeLinklevelMom_Type = CounterBasedGauge64
_RulesetConnStatechangeLinklevelMom_Object = MibScalar
rulesetConnStatechangeLinklevelMom = _RulesetConnStatechangeLinklevelMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 64, 39, 2),
    _RulesetConnStatechangeLinklevelMom_Type()
)
rulesetConnStatechangeLinklevelMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rulesetConnStatechangeLinklevelMom.setStatus("current")
_RulesetConnStatechangeLinklevelMax_Type = CounterBasedGauge64
_RulesetConnStatechangeLinklevelMax_Object = MibScalar
rulesetConnStatechangeLinklevelMax = _RulesetConnStatechangeLinklevelMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 64, 39, 3),
    _RulesetConnStatechangeLinklevelMax_Type()
)
rulesetConnStatechangeLinklevelMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rulesetConnStatechangeLinklevelMax.setStatus("current")
_RulesetSubscriberAllocFail_ObjectIdentity = ObjectIdentity
rulesetSubscriberAllocFail = _RulesetSubscriberAllocFail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 64, 40)
)
_RulesetSubscriberAllocFailVal_Type = Counter64
_RulesetSubscriberAllocFailVal_Object = MibScalar
rulesetSubscriberAllocFailVal = _RulesetSubscriberAllocFailVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 64, 40, 1),
    _RulesetSubscriberAllocFailVal_Type()
)
rulesetSubscriberAllocFailVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rulesetSubscriberAllocFailVal.setStatus("current")
_RulesetSubscriberAllocFailMom_Type = CounterBasedGauge64
_RulesetSubscriberAllocFailMom_Object = MibScalar
rulesetSubscriberAllocFailMom = _RulesetSubscriberAllocFailMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 64, 40, 2),
    _RulesetSubscriberAllocFailMom_Type()
)
rulesetSubscriberAllocFailMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rulesetSubscriberAllocFailMom.setStatus("current")
_RulesetSubscriberAllocFailMax_Type = CounterBasedGauge64
_RulesetSubscriberAllocFailMax_Object = MibScalar
rulesetSubscriberAllocFailMax = _RulesetSubscriberAllocFailMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 64, 40, 3),
    _RulesetSubscriberAllocFailMax_Type()
)
rulesetSubscriberAllocFailMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rulesetSubscriberAllocFailMax.setStatus("current")
_RulesetDynipAllocFail_ObjectIdentity = ObjectIdentity
rulesetDynipAllocFail = _RulesetDynipAllocFail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 64, 41)
)
_RulesetDynipAllocFailVal_Type = Counter64
_RulesetDynipAllocFailVal_Object = MibScalar
rulesetDynipAllocFailVal = _RulesetDynipAllocFailVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 64, 41, 1),
    _RulesetDynipAllocFailVal_Type()
)
rulesetDynipAllocFailVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rulesetDynipAllocFailVal.setStatus("current")
_RulesetDynipAllocFailMom_Type = CounterBasedGauge64
_RulesetDynipAllocFailMom_Object = MibScalar
rulesetDynipAllocFailMom = _RulesetDynipAllocFailMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 64, 41, 2),
    _RulesetDynipAllocFailMom_Type()
)
rulesetDynipAllocFailMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rulesetDynipAllocFailMom.setStatus("current")
_RulesetDynipAllocFailMax_Type = CounterBasedGauge64
_RulesetDynipAllocFailMax_Object = MibScalar
rulesetDynipAllocFailMax = _RulesetDynipAllocFailMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 64, 41, 3),
    _RulesetDynipAllocFailMax_Type()
)
rulesetDynipAllocFailMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rulesetDynipAllocFailMax.setStatus("current")
_RulesetDynipOversized_ObjectIdentity = ObjectIdentity
rulesetDynipOversized = _RulesetDynipOversized_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 64, 42)
)
_RulesetDynipOversizedVal_Type = Counter64
_RulesetDynipOversizedVal_Object = MibScalar
rulesetDynipOversizedVal = _RulesetDynipOversizedVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 64, 42, 1),
    _RulesetDynipOversizedVal_Type()
)
rulesetDynipOversizedVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rulesetDynipOversizedVal.setStatus("current")
_RulesetDynipOversizedMom_Type = CounterBasedGauge64
_RulesetDynipOversizedMom_Object = MibScalar
rulesetDynipOversizedMom = _RulesetDynipOversizedMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 64, 42, 2),
    _RulesetDynipOversizedMom_Type()
)
rulesetDynipOversizedMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rulesetDynipOversizedMom.setStatus("current")
_RulesetDynipOversizedMax_Type = CounterBasedGauge64
_RulesetDynipOversizedMax_Object = MibScalar
rulesetDynipOversizedMax = _RulesetDynipOversizedMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 64, 42, 3),
    _RulesetDynipOversizedMax_Type()
)
rulesetDynipOversizedMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rulesetDynipOversizedMax.setStatus("current")
_RulesetNonexistentSubscriber_ObjectIdentity = ObjectIdentity
rulesetNonexistentSubscriber = _RulesetNonexistentSubscriber_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 64, 43)
)
_RulesetNonexistentSubscriberVal_Type = Counter64
_RulesetNonexistentSubscriberVal_Object = MibScalar
rulesetNonexistentSubscriberVal = _RulesetNonexistentSubscriberVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 64, 43, 1),
    _RulesetNonexistentSubscriberVal_Type()
)
rulesetNonexistentSubscriberVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rulesetNonexistentSubscriberVal.setStatus("current")
_RulesetNonexistentSubscriberMom_Type = CounterBasedGauge64
_RulesetNonexistentSubscriberMom_Object = MibScalar
rulesetNonexistentSubscriberMom = _RulesetNonexistentSubscriberMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 64, 43, 2),
    _RulesetNonexistentSubscriberMom_Type()
)
rulesetNonexistentSubscriberMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rulesetNonexistentSubscriberMom.setStatus("current")
_RulesetNonexistentSubscriberMax_Type = CounterBasedGauge64
_RulesetNonexistentSubscriberMax_Object = MibScalar
rulesetNonexistentSubscriberMax = _RulesetNonexistentSubscriberMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 64, 43, 3),
    _RulesetNonexistentSubscriberMax_Type()
)
rulesetNonexistentSubscriberMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rulesetNonexistentSubscriberMax.setStatus("current")
_RulesetConnStatechangeTtl_ObjectIdentity = ObjectIdentity
rulesetConnStatechangeTtl = _RulesetConnStatechangeTtl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 64, 44)
)
_RulesetConnStatechangeTtlVal_Type = Counter64
_RulesetConnStatechangeTtlVal_Object = MibScalar
rulesetConnStatechangeTtlVal = _RulesetConnStatechangeTtlVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 64, 44, 1),
    _RulesetConnStatechangeTtlVal_Type()
)
rulesetConnStatechangeTtlVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rulesetConnStatechangeTtlVal.setStatus("current")
_RulesetConnStatechangeTtlMom_Type = CounterBasedGauge64
_RulesetConnStatechangeTtlMom_Object = MibScalar
rulesetConnStatechangeTtlMom = _RulesetConnStatechangeTtlMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 64, 44, 2),
    _RulesetConnStatechangeTtlMom_Type()
)
rulesetConnStatechangeTtlMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rulesetConnStatechangeTtlMom.setStatus("current")
_RulesetConnStatechangeTtlMax_Type = CounterBasedGauge64
_RulesetConnStatechangeTtlMax_Object = MibScalar
rulesetConnStatechangeTtlMax = _RulesetConnStatechangeTtlMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 64, 44, 3),
    _RulesetConnStatechangeTtlMax_Type()
)
rulesetConnStatechangeTtlMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rulesetConnStatechangeTtlMax.setStatus("current")
_Firewall_ObjectIdentity = ObjectIdentity
firewall = _Firewall_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 80)
)
_FwAccepts_ObjectIdentity = ObjectIdentity
fwAccepts = _FwAccepts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 80, 1)
)
_FwAcceptsVal_Type = Counter64
_FwAcceptsVal_Object = MibScalar
fwAcceptsVal = _FwAcceptsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 80, 1, 1),
    _FwAcceptsVal_Type()
)
fwAcceptsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwAcceptsVal.setStatus("current")
_FwAcceptsMom_Type = CounterBasedGauge64
_FwAcceptsMom_Object = MibScalar
fwAcceptsMom = _FwAcceptsMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 80, 1, 2),
    _FwAcceptsMom_Type()
)
fwAcceptsMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwAcceptsMom.setStatus("current")
_FwAcceptsMax_Type = CounterBasedGauge64
_FwAcceptsMax_Object = MibScalar
fwAcceptsMax = _FwAcceptsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 80, 1, 3),
    _FwAcceptsMax_Type()
)
fwAcceptsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwAcceptsMax.setStatus("current")
_FwRejects_ObjectIdentity = ObjectIdentity
fwRejects = _FwRejects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 80, 2)
)
_FwRejectsVal_Type = Counter64
_FwRejectsVal_Object = MibScalar
fwRejectsVal = _FwRejectsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 80, 2, 1),
    _FwRejectsVal_Type()
)
fwRejectsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwRejectsVal.setStatus("current")
_FwRejectsMom_Type = CounterBasedGauge64
_FwRejectsMom_Object = MibScalar
fwRejectsMom = _FwRejectsMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 80, 2, 2),
    _FwRejectsMom_Type()
)
fwRejectsMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwRejectsMom.setStatus("current")
_FwRejectsMax_Type = CounterBasedGauge64
_FwRejectsMax_Object = MibScalar
fwRejectsMax = _FwRejectsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 80, 2, 3),
    _FwRejectsMax_Type()
)
fwRejectsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwRejectsMax.setStatus("current")
_FwDrops_ObjectIdentity = ObjectIdentity
fwDrops = _FwDrops_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 80, 3)
)
_FwDropsVal_Type = Counter64
_FwDropsVal_Object = MibScalar
fwDropsVal = _FwDropsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 80, 3, 1),
    _FwDropsVal_Type()
)
fwDropsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwDropsVal.setStatus("current")
_FwDropsMom_Type = CounterBasedGauge64
_FwDropsMom_Object = MibScalar
fwDropsMom = _FwDropsMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 80, 3, 2),
    _FwDropsMom_Type()
)
fwDropsMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwDropsMom.setStatus("current")
_FwDropsMax_Type = CounterBasedGauge64
_FwDropsMax_Object = MibScalar
fwDropsMax = _FwDropsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 80, 3, 3),
    _FwDropsMax_Type()
)
fwDropsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwDropsMax.setStatus("current")
_FwRewites_ObjectIdentity = ObjectIdentity
fwRewites = _FwRewites_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 80, 4)
)
_FwRewitesVal_Type = Counter64
_FwRewitesVal_Object = MibScalar
fwRewitesVal = _FwRewitesVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 80, 4, 1),
    _FwRewitesVal_Type()
)
fwRewitesVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwRewitesVal.setStatus("current")
_FwRewitesMom_Type = CounterBasedGauge64
_FwRewitesMom_Object = MibScalar
fwRewitesMom = _FwRewitesMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 80, 4, 2),
    _FwRewitesMom_Type()
)
fwRewitesMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwRewitesMom.setStatus("current")
_FwRewitesMax_Type = CounterBasedGauge64
_FwRewitesMax_Object = MibScalar
fwRewitesMax = _FwRewitesMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 80, 4, 3),
    _FwRewitesMax_Type()
)
fwRewitesMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwRewitesMax.setStatus("current")
_FwDiverts_ObjectIdentity = ObjectIdentity
fwDiverts = _FwDiverts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 80, 5)
)
_FwDivertsVal_Type = Counter64
_FwDivertsVal_Object = MibScalar
fwDivertsVal = _FwDivertsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 80, 5, 1),
    _FwDivertsVal_Type()
)
fwDivertsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwDivertsVal.setStatus("current")
_FwDivertsMom_Type = CounterBasedGauge64
_FwDivertsMom_Object = MibScalar
fwDivertsMom = _FwDivertsMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 80, 5, 2),
    _FwDivertsMom_Type()
)
fwDivertsMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwDivertsMom.setStatus("current")
_FwDivertsMax_Type = CounterBasedGauge64
_FwDivertsMax_Object = MibScalar
fwDivertsMax = _FwDivertsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 80, 5, 3),
    _FwDivertsMax_Type()
)
fwDivertsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwDivertsMax.setStatus("current")
_FwRuleSets_ObjectIdentity = ObjectIdentity
fwRuleSets = _FwRuleSets_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 80, 6)
)
_FwRuleSetsVal_Type = Counter64
_FwRuleSetsVal_Object = MibScalar
fwRuleSetsVal = _FwRuleSetsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 80, 6, 1),
    _FwRuleSetsVal_Type()
)
fwRuleSetsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwRuleSetsVal.setStatus("current")
_FwRuleSetsMom_Type = CounterBasedGauge64
_FwRuleSetsMom_Object = MibScalar
fwRuleSetsMom = _FwRuleSetsMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 80, 6, 2),
    _FwRuleSetsMom_Type()
)
fwRuleSetsMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwRuleSetsMom.setStatus("current")
_FwRuleSetsMax_Type = CounterBasedGauge64
_FwRuleSetsMax_Object = MibScalar
fwRuleSetsMax = _FwRuleSetsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 80, 6, 3),
    _FwRuleSetsMax_Type()
)
fwRuleSetsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwRuleSetsMax.setStatus("current")
_FwLogs_ObjectIdentity = ObjectIdentity
fwLogs = _FwLogs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 80, 7)
)
_FwLogsVal_Type = Counter64
_FwLogsVal_Object = MibScalar
fwLogsVal = _FwLogsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 80, 7, 1),
    _FwLogsVal_Type()
)
fwLogsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwLogsVal.setStatus("current")
_FwLogsMom_Type = CounterBasedGauge64
_FwLogsMom_Object = MibScalar
fwLogsMom = _FwLogsMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 80, 7, 2),
    _FwLogsMom_Type()
)
fwLogsMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwLogsMom.setStatus("current")
_FwLogsMax_Type = CounterBasedGauge64
_FwLogsMax_Object = MibScalar
fwLogsMax = _FwLogsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 80, 7, 3),
    _FwLogsMax_Type()
)
fwLogsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwLogsMax.setStatus("current")
_FwMonitor_ObjectIdentity = ObjectIdentity
fwMonitor = _FwMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 80, 8)
)
_FwMonitorVal_Type = Counter64
_FwMonitorVal_Object = MibScalar
fwMonitorVal = _FwMonitorVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 80, 8, 1),
    _FwMonitorVal_Type()
)
fwMonitorVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwMonitorVal.setStatus("current")
_FwMonitorMom_Type = CounterBasedGauge64
_FwMonitorMom_Object = MibScalar
fwMonitorMom = _FwMonitorMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 80, 8, 2),
    _FwMonitorMom_Type()
)
fwMonitorMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwMonitorMom.setStatus("current")
_FwMonitorMax_Type = CounterBasedGauge64
_FwMonitorMax_Object = MibScalar
fwMonitorMax = _FwMonitorMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 80, 8, 3),
    _FwMonitorMax_Type()
)
fwMonitorMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwMonitorMax.setStatus("current")
_FwMonitorFailures_ObjectIdentity = ObjectIdentity
fwMonitorFailures = _FwMonitorFailures_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 80, 9)
)
_FwMonitorFailuresVal_Type = Counter64
_FwMonitorFailuresVal_Object = MibScalar
fwMonitorFailuresVal = _FwMonitorFailuresVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 80, 9, 1),
    _FwMonitorFailuresVal_Type()
)
fwMonitorFailuresVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwMonitorFailuresVal.setStatus("current")
_FwMonitorFailuresMom_Type = CounterBasedGauge64
_FwMonitorFailuresMom_Object = MibScalar
fwMonitorFailuresMom = _FwMonitorFailuresMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 80, 9, 2),
    _FwMonitorFailuresMom_Type()
)
fwMonitorFailuresMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwMonitorFailuresMom.setStatus("current")
_FwMonitorFailuresMax_Type = CounterBasedGauge64
_FwMonitorFailuresMax_Object = MibScalar
fwMonitorFailuresMax = _FwMonitorFailuresMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 80, 9, 3),
    _FwMonitorFailuresMax_Type()
)
fwMonitorFailuresMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwMonitorFailuresMax.setStatus("current")
_FwInjects_ObjectIdentity = ObjectIdentity
fwInjects = _FwInjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 80, 10)
)
_FwInjectsVal_Type = Counter64
_FwInjectsVal_Object = MibScalar
fwInjectsVal = _FwInjectsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 80, 10, 1),
    _FwInjectsVal_Type()
)
fwInjectsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwInjectsVal.setStatus("current")
_FwInjectsMom_Type = CounterBasedGauge64
_FwInjectsMom_Object = MibScalar
fwInjectsMom = _FwInjectsMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 80, 10, 2),
    _FwInjectsMom_Type()
)
fwInjectsMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwInjectsMom.setStatus("current")
_FwInjectsMax_Type = CounterBasedGauge64
_FwInjectsMax_Object = MibScalar
fwInjectsMax = _FwInjectsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 80, 10, 3),
    _FwInjectsMax_Type()
)
fwInjectsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwInjectsMax.setStatus("current")
_FwInjectsFailures_ObjectIdentity = ObjectIdentity
fwInjectsFailures = _FwInjectsFailures_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 80, 11)
)
_FwInjectsFailuresVal_Type = Counter64
_FwInjectsFailuresVal_Object = MibScalar
fwInjectsFailuresVal = _FwInjectsFailuresVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 80, 11, 1),
    _FwInjectsFailuresVal_Type()
)
fwInjectsFailuresVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwInjectsFailuresVal.setStatus("current")
_FwInjectsFailuresMom_Type = CounterBasedGauge64
_FwInjectsFailuresMom_Object = MibScalar
fwInjectsFailuresMom = _FwInjectsFailuresMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 80, 11, 2),
    _FwInjectsFailuresMom_Type()
)
fwInjectsFailuresMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwInjectsFailuresMom.setStatus("current")
_FwInjectsFailuresMax_Type = CounterBasedGauge64
_FwInjectsFailuresMax_Object = MibScalar
fwInjectsFailuresMax = _FwInjectsFailuresMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 80, 11, 3),
    _FwInjectsFailuresMax_Type()
)
fwInjectsFailuresMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwInjectsFailuresMax.setStatus("current")
_FwInjectsFailuresProp_ObjectIdentity = ObjectIdentity
fwInjectsFailuresProp = _FwInjectsFailuresProp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 80, 12)
)
_FwInjectsFailuresPropVal_Type = Counter64
_FwInjectsFailuresPropVal_Object = MibScalar
fwInjectsFailuresPropVal = _FwInjectsFailuresPropVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 80, 12, 1),
    _FwInjectsFailuresPropVal_Type()
)
fwInjectsFailuresPropVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwInjectsFailuresPropVal.setStatus("current")
_FwInjectsFailuresPropMom_Type = CounterBasedGauge64
_FwInjectsFailuresPropMom_Object = MibScalar
fwInjectsFailuresPropMom = _FwInjectsFailuresPropMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 80, 12, 2),
    _FwInjectsFailuresPropMom_Type()
)
fwInjectsFailuresPropMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwInjectsFailuresPropMom.setStatus("current")
_FwInjectsFailuresPropMax_Type = CounterBasedGauge64
_FwInjectsFailuresPropMax_Object = MibScalar
fwInjectsFailuresPropMax = _FwInjectsFailuresPropMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 80, 12, 3),
    _FwInjectsFailuresPropMax_Type()
)
fwInjectsFailuresPropMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwInjectsFailuresPropMax.setStatus("current")
_FwMidconnRewrite_ObjectIdentity = ObjectIdentity
fwMidconnRewrite = _FwMidconnRewrite_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 80, 13)
)
_FwMidconnRewriteVal_Type = Counter64
_FwMidconnRewriteVal_Object = MibScalar
fwMidconnRewriteVal = _FwMidconnRewriteVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 80, 13, 1),
    _FwMidconnRewriteVal_Type()
)
fwMidconnRewriteVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwMidconnRewriteVal.setStatus("current")
_FwMidconnRewriteMom_Type = CounterBasedGauge64
_FwMidconnRewriteMom_Object = MibScalar
fwMidconnRewriteMom = _FwMidconnRewriteMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 80, 13, 2),
    _FwMidconnRewriteMom_Type()
)
fwMidconnRewriteMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwMidconnRewriteMom.setStatus("current")
_FwMidconnRewriteMax_Type = CounterBasedGauge64
_FwMidconnRewriteMax_Object = MibScalar
fwMidconnRewriteMax = _FwMidconnRewriteMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 80, 13, 3),
    _FwMidconnRewriteMax_Type()
)
fwMidconnRewriteMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwMidconnRewriteMax.setStatus("current")
_Shaping_ObjectIdentity = ObjectIdentity
shaping = _Shaping_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88)
)
_ShapingEnqueued_ObjectIdentity = ObjectIdentity
shapingEnqueued = _ShapingEnqueued_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 1)
)
_ShapingEnqueuedVal_Type = Counter64
_ShapingEnqueuedVal_Object = MibScalar
shapingEnqueuedVal = _ShapingEnqueuedVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 1, 1),
    _ShapingEnqueuedVal_Type()
)
shapingEnqueuedVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingEnqueuedVal.setStatus("current")
_ShapingEnqueuedMom_Type = CounterBasedGauge64
_ShapingEnqueuedMom_Object = MibScalar
shapingEnqueuedMom = _ShapingEnqueuedMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 1, 2),
    _ShapingEnqueuedMom_Type()
)
shapingEnqueuedMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingEnqueuedMom.setStatus("current")
_ShapingEnqueuedMax_Type = CounterBasedGauge64
_ShapingEnqueuedMax_Object = MibScalar
shapingEnqueuedMax = _ShapingEnqueuedMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 1, 3),
    _ShapingEnqueuedMax_Type()
)
shapingEnqueuedMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingEnqueuedMax.setStatus("current")
_ShapingDequeued_ObjectIdentity = ObjectIdentity
shapingDequeued = _ShapingDequeued_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 2)
)
_ShapingDequeuedVal_Type = Counter64
_ShapingDequeuedVal_Object = MibScalar
shapingDequeuedVal = _ShapingDequeuedVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 2, 1),
    _ShapingDequeuedVal_Type()
)
shapingDequeuedVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingDequeuedVal.setStatus("current")
_ShapingDequeuedMom_Type = CounterBasedGauge64
_ShapingDequeuedMom_Object = MibScalar
shapingDequeuedMom = _ShapingDequeuedMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 2, 2),
    _ShapingDequeuedMom_Type()
)
shapingDequeuedMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingDequeuedMom.setStatus("current")
_ShapingDequeuedMax_Type = CounterBasedGauge64
_ShapingDequeuedMax_Object = MibScalar
shapingDequeuedMax = _ShapingDequeuedMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 2, 3),
    _ShapingDequeuedMax_Type()
)
shapingDequeuedMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingDequeuedMax.setStatus("current")
_ShapingBrownConnDrops_ObjectIdentity = ObjectIdentity
shapingBrownConnDrops = _ShapingBrownConnDrops_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 8)
)
_ShapingBrownConnDropsVal_Type = Counter64
_ShapingBrownConnDropsVal_Object = MibScalar
shapingBrownConnDropsVal = _ShapingBrownConnDropsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 8, 1),
    _ShapingBrownConnDropsVal_Type()
)
shapingBrownConnDropsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingBrownConnDropsVal.setStatus("current")
_ShapingBrownConnDropsMom_Type = CounterBasedGauge64
_ShapingBrownConnDropsMom_Object = MibScalar
shapingBrownConnDropsMom = _ShapingBrownConnDropsMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 8, 2),
    _ShapingBrownConnDropsMom_Type()
)
shapingBrownConnDropsMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingBrownConnDropsMom.setStatus("current")
_ShapingBrownConnDropsMax_Type = CounterBasedGauge64
_ShapingBrownConnDropsMax_Object = MibScalar
shapingBrownConnDropsMax = _ShapingBrownConnDropsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 8, 3),
    _ShapingBrownConnDropsMax_Type()
)
shapingBrownConnDropsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingBrownConnDropsMax.setStatus("current")
_ShapingQueueSize_ObjectIdentity = ObjectIdentity
shapingQueueSize = _ShapingQueueSize_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 9)
)
_ShapingQueueSizeVal_Type = CounterBasedGauge64
_ShapingQueueSizeVal_Object = MibScalar
shapingQueueSizeVal = _ShapingQueueSizeVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 9, 1),
    _ShapingQueueSizeVal_Type()
)
shapingQueueSizeVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingQueueSizeVal.setStatus("current")
_ShapingQueueSizeMax_Type = CounterBasedGauge64
_ShapingQueueSizeMax_Object = MibScalar
shapingQueueSizeMax = _ShapingQueueSizeMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 9, 3),
    _ShapingQueueSizeMax_Type()
)
shapingQueueSizeMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingQueueSizeMax.setStatus("current")
_ShapingRulesSetCount_ObjectIdentity = ObjectIdentity
shapingRulesSetCount = _ShapingRulesSetCount_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 10)
)
_ShapingRulesSetCountVal_Type = Counter64
_ShapingRulesSetCountVal_Object = MibScalar
shapingRulesSetCountVal = _ShapingRulesSetCountVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 10, 1),
    _ShapingRulesSetCountVal_Type()
)
shapingRulesSetCountVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingRulesSetCountVal.setStatus("current")
_ShapingRulesSetCountMom_Type = CounterBasedGauge64
_ShapingRulesSetCountMom_Object = MibScalar
shapingRulesSetCountMom = _ShapingRulesSetCountMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 10, 2),
    _ShapingRulesSetCountMom_Type()
)
shapingRulesSetCountMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingRulesSetCountMom.setStatus("current")
_ShapingRulesSetCountMax_Type = CounterBasedGauge64
_ShapingRulesSetCountMax_Object = MibScalar
shapingRulesSetCountMax = _ShapingRulesSetCountMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 10, 3),
    _ShapingRulesSetCountMax_Type()
)
shapingRulesSetCountMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingRulesSetCountMax.setStatus("current")
_ShapingEnqueuedBytes_ObjectIdentity = ObjectIdentity
shapingEnqueuedBytes = _ShapingEnqueuedBytes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 11)
)
_ShapingEnqueuedBytesVal_Type = Counter64
_ShapingEnqueuedBytesVal_Object = MibScalar
shapingEnqueuedBytesVal = _ShapingEnqueuedBytesVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 11, 1),
    _ShapingEnqueuedBytesVal_Type()
)
shapingEnqueuedBytesVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingEnqueuedBytesVal.setStatus("current")
_ShapingEnqueuedBytesMom_Type = CounterBasedGauge64
_ShapingEnqueuedBytesMom_Object = MibScalar
shapingEnqueuedBytesMom = _ShapingEnqueuedBytesMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 11, 2),
    _ShapingEnqueuedBytesMom_Type()
)
shapingEnqueuedBytesMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingEnqueuedBytesMom.setStatus("current")
_ShapingEnqueuedBytesMax_Type = CounterBasedGauge64
_ShapingEnqueuedBytesMax_Object = MibScalar
shapingEnqueuedBytesMax = _ShapingEnqueuedBytesMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 11, 3),
    _ShapingEnqueuedBytesMax_Type()
)
shapingEnqueuedBytesMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingEnqueuedBytesMax.setStatus("current")
_ShapingDequeuedBytes_ObjectIdentity = ObjectIdentity
shapingDequeuedBytes = _ShapingDequeuedBytes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 12)
)
_ShapingDequeuedBytesVal_Type = Counter64
_ShapingDequeuedBytesVal_Object = MibScalar
shapingDequeuedBytesVal = _ShapingDequeuedBytesVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 12, 1),
    _ShapingDequeuedBytesVal_Type()
)
shapingDequeuedBytesVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingDequeuedBytesVal.setStatus("current")
_ShapingDequeuedBytesMom_Type = CounterBasedGauge64
_ShapingDequeuedBytesMom_Object = MibScalar
shapingDequeuedBytesMom = _ShapingDequeuedBytesMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 12, 2),
    _ShapingDequeuedBytesMom_Type()
)
shapingDequeuedBytesMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingDequeuedBytesMom.setStatus("current")
_ShapingDequeuedBytesMax_Type = CounterBasedGauge64
_ShapingDequeuedBytesMax_Object = MibScalar
shapingDequeuedBytesMax = _ShapingDequeuedBytesMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 12, 3),
    _ShapingDequeuedBytesMax_Type()
)
shapingDequeuedBytesMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingDequeuedBytesMax.setStatus("current")
_ShapingObjectCopies_ObjectIdentity = ObjectIdentity
shapingObjectCopies = _ShapingObjectCopies_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 13)
)
_ShapingObjectCopiesVal_Type = CounterBasedGauge64
_ShapingObjectCopiesVal_Object = MibScalar
shapingObjectCopiesVal = _ShapingObjectCopiesVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 13, 1),
    _ShapingObjectCopiesVal_Type()
)
shapingObjectCopiesVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingObjectCopiesVal.setStatus("current")
_ShapingObjectCopiesMax_Type = CounterBasedGauge64
_ShapingObjectCopiesMax_Object = MibScalar
shapingObjectCopiesMax = _ShapingObjectCopiesMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 13, 3),
    _ShapingObjectCopiesMax_Type()
)
shapingObjectCopiesMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingObjectCopiesMax.setStatus("current")
_ShapingOutofpacketsDrops_ObjectIdentity = ObjectIdentity
shapingOutofpacketsDrops = _ShapingOutofpacketsDrops_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 15)
)
_ShapingOutofpacketsDropsVal_Type = Counter64
_ShapingOutofpacketsDropsVal_Object = MibScalar
shapingOutofpacketsDropsVal = _ShapingOutofpacketsDropsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 15, 1),
    _ShapingOutofpacketsDropsVal_Type()
)
shapingOutofpacketsDropsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingOutofpacketsDropsVal.setStatus("current")
_ShapingOutofpacketsDropsMom_Type = CounterBasedGauge64
_ShapingOutofpacketsDropsMom_Object = MibScalar
shapingOutofpacketsDropsMom = _ShapingOutofpacketsDropsMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 15, 2),
    _ShapingOutofpacketsDropsMom_Type()
)
shapingOutofpacketsDropsMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingOutofpacketsDropsMom.setStatus("current")
_ShapingOutofpacketsDropsMax_Type = CounterBasedGauge64
_ShapingOutofpacketsDropsMax_Object = MibScalar
shapingOutofpacketsDropsMax = _ShapingOutofpacketsDropsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 15, 3),
    _ShapingOutofpacketsDropsMax_Type()
)
shapingOutofpacketsDropsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingOutofpacketsDropsMax.setStatus("current")
_ShapingReceived_ObjectIdentity = ObjectIdentity
shapingReceived = _ShapingReceived_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 16)
)
_ShapingReceivedVal_Type = Counter64
_ShapingReceivedVal_Object = MibScalar
shapingReceivedVal = _ShapingReceivedVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 16, 1),
    _ShapingReceivedVal_Type()
)
shapingReceivedVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingReceivedVal.setStatus("current")
_ShapingReceivedMom_Type = CounterBasedGauge64
_ShapingReceivedMom_Object = MibScalar
shapingReceivedMom = _ShapingReceivedMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 16, 2),
    _ShapingReceivedMom_Type()
)
shapingReceivedMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingReceivedMom.setStatus("current")
_ShapingReceivedMax_Type = CounterBasedGauge64
_ShapingReceivedMax_Object = MibScalar
shapingReceivedMax = _ShapingReceivedMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 16, 3),
    _ShapingReceivedMax_Type()
)
shapingReceivedMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingReceivedMax.setStatus("current")
_ShapingObjectChecks_ObjectIdentity = ObjectIdentity
shapingObjectChecks = _ShapingObjectChecks_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 17)
)
_ShapingObjectChecksVal_Type = Counter64
_ShapingObjectChecksVal_Object = MibScalar
shapingObjectChecksVal = _ShapingObjectChecksVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 17, 1),
    _ShapingObjectChecksVal_Type()
)
shapingObjectChecksVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingObjectChecksVal.setStatus("current")
_ShapingObjectChecksMom_Type = CounterBasedGauge64
_ShapingObjectChecksMom_Object = MibScalar
shapingObjectChecksMom = _ShapingObjectChecksMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 17, 2),
    _ShapingObjectChecksMom_Type()
)
shapingObjectChecksMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingObjectChecksMom.setStatus("current")
_ShapingObjectChecksMax_Type = CounterBasedGauge64
_ShapingObjectChecksMax_Object = MibScalar
shapingObjectChecksMax = _ShapingObjectChecksMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 17, 3),
    _ShapingObjectChecksMax_Type()
)
shapingObjectChecksMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingObjectChecksMax.setStatus("current")
_ShapingObjectPoolExhausted_ObjectIdentity = ObjectIdentity
shapingObjectPoolExhausted = _ShapingObjectPoolExhausted_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 25)
)
_ShapingObjectPoolExhaustedVal_Type = Counter64
_ShapingObjectPoolExhaustedVal_Object = MibScalar
shapingObjectPoolExhaustedVal = _ShapingObjectPoolExhaustedVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 25, 1),
    _ShapingObjectPoolExhaustedVal_Type()
)
shapingObjectPoolExhaustedVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingObjectPoolExhaustedVal.setStatus("current")
_ShapingObjectPoolExhaustedMom_Type = CounterBasedGauge64
_ShapingObjectPoolExhaustedMom_Object = MibScalar
shapingObjectPoolExhaustedMom = _ShapingObjectPoolExhaustedMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 25, 2),
    _ShapingObjectPoolExhaustedMom_Type()
)
shapingObjectPoolExhaustedMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingObjectPoolExhaustedMom.setStatus("current")
_ShapingObjectPoolExhaustedMax_Type = CounterBasedGauge64
_ShapingObjectPoolExhaustedMax_Object = MibScalar
shapingObjectPoolExhaustedMax = _ShapingObjectPoolExhaustedMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 25, 3),
    _ShapingObjectPoolExhaustedMax_Type()
)
shapingObjectPoolExhaustedMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingObjectPoolExhaustedMax.setStatus("current")
_ShapingOutOfCreditsDrops_ObjectIdentity = ObjectIdentity
shapingOutOfCreditsDrops = _ShapingOutOfCreditsDrops_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 26)
)
_ShapingOutOfCreditsDropsVal_Type = Counter64
_ShapingOutOfCreditsDropsVal_Object = MibScalar
shapingOutOfCreditsDropsVal = _ShapingOutOfCreditsDropsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 26, 1),
    _ShapingOutOfCreditsDropsVal_Type()
)
shapingOutOfCreditsDropsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingOutOfCreditsDropsVal.setStatus("current")
_ShapingOutOfCreditsDropsMom_Type = CounterBasedGauge64
_ShapingOutOfCreditsDropsMom_Object = MibScalar
shapingOutOfCreditsDropsMom = _ShapingOutOfCreditsDropsMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 26, 2),
    _ShapingOutOfCreditsDropsMom_Type()
)
shapingOutOfCreditsDropsMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingOutOfCreditsDropsMom.setStatus("current")
_ShapingOutOfCreditsDropsMax_Type = CounterBasedGauge64
_ShapingOutOfCreditsDropsMax_Object = MibScalar
shapingOutOfCreditsDropsMax = _ShapingOutOfCreditsDropsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 26, 3),
    _ShapingOutOfCreditsDropsMax_Type()
)
shapingOutOfCreditsDropsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingOutOfCreditsDropsMax.setStatus("current")
_ShapingObjectOverflow_ObjectIdentity = ObjectIdentity
shapingObjectOverflow = _ShapingObjectOverflow_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 31)
)
_ShapingObjectOverflowVal_Type = Counter64
_ShapingObjectOverflowVal_Object = MibScalar
shapingObjectOverflowVal = _ShapingObjectOverflowVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 31, 1),
    _ShapingObjectOverflowVal_Type()
)
shapingObjectOverflowVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingObjectOverflowVal.setStatus("current")
_ShapingObjectOverflowMom_Type = CounterBasedGauge64
_ShapingObjectOverflowMom_Object = MibScalar
shapingObjectOverflowMom = _ShapingObjectOverflowMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 31, 2),
    _ShapingObjectOverflowMom_Type()
)
shapingObjectOverflowMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingObjectOverflowMom.setStatus("current")
_ShapingObjectOverflowMax_Type = CounterBasedGauge64
_ShapingObjectOverflowMax_Object = MibScalar
shapingObjectOverflowMax = _ShapingObjectOverflowMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 31, 3),
    _ShapingObjectOverflowMax_Type()
)
shapingObjectOverflowMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingObjectOverflowMax.setStatus("current")
_ShapingRuleOverflow_ObjectIdentity = ObjectIdentity
shapingRuleOverflow = _ShapingRuleOverflow_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 32)
)
_ShapingRuleOverflowVal_Type = Counter64
_ShapingRuleOverflowVal_Object = MibScalar
shapingRuleOverflowVal = _ShapingRuleOverflowVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 32, 1),
    _ShapingRuleOverflowVal_Type()
)
shapingRuleOverflowVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingRuleOverflowVal.setStatus("current")
_ShapingRuleOverflowMom_Type = CounterBasedGauge64
_ShapingRuleOverflowMom_Object = MibScalar
shapingRuleOverflowMom = _ShapingRuleOverflowMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 32, 2),
    _ShapingRuleOverflowMom_Type()
)
shapingRuleOverflowMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingRuleOverflowMom.setStatus("current")
_ShapingRuleOverflowMax_Type = CounterBasedGauge64
_ShapingRuleOverflowMax_Object = MibScalar
shapingRuleOverflowMax = _ShapingRuleOverflowMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 32, 3),
    _ShapingRuleOverflowMax_Type()
)
shapingRuleOverflowMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingRuleOverflowMax.setStatus("current")
_ShapingDrops_ObjectIdentity = ObjectIdentity
shapingDrops = _ShapingDrops_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 37)
)
_ShapingDropsVal_Type = Counter64
_ShapingDropsVal_Object = MibScalar
shapingDropsVal = _ShapingDropsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 37, 1),
    _ShapingDropsVal_Type()
)
shapingDropsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingDropsVal.setStatus("current")
_ShapingDropsMom_Type = CounterBasedGauge64
_ShapingDropsMom_Object = MibScalar
shapingDropsMom = _ShapingDropsMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 37, 2),
    _ShapingDropsMom_Type()
)
shapingDropsMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingDropsMom.setStatus("current")
_ShapingDropsMax_Type = CounterBasedGauge64
_ShapingDropsMax_Object = MibScalar
shapingDropsMax = _ShapingDropsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 37, 3),
    _ShapingDropsMax_Type()
)
shapingDropsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingDropsMax.setStatus("current")
_ShapingObjectFull_ObjectIdentity = ObjectIdentity
shapingObjectFull = _ShapingObjectFull_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 38)
)
_ShapingObjectFullVal_Type = Counter64
_ShapingObjectFullVal_Object = MibScalar
shapingObjectFullVal = _ShapingObjectFullVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 38, 1),
    _ShapingObjectFullVal_Type()
)
shapingObjectFullVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingObjectFullVal.setStatus("current")
_ShapingObjectFullMom_Type = CounterBasedGauge64
_ShapingObjectFullMom_Object = MibScalar
shapingObjectFullMom = _ShapingObjectFullMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 38, 2),
    _ShapingObjectFullMom_Type()
)
shapingObjectFullMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingObjectFullMom.setStatus("current")
_ShapingObjectFullMax_Type = CounterBasedGauge64
_ShapingObjectFullMax_Object = MibScalar
shapingObjectFullMax = _ShapingObjectFullMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 38, 3),
    _ShapingObjectFullMax_Type()
)
shapingObjectFullMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingObjectFullMax.setStatus("current")
_ShapingUnshaped_ObjectIdentity = ObjectIdentity
shapingUnshaped = _ShapingUnshaped_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 39)
)
_ShapingUnshapedVal_Type = Counter64
_ShapingUnshapedVal_Object = MibScalar
shapingUnshapedVal = _ShapingUnshapedVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 39, 1),
    _ShapingUnshapedVal_Type()
)
shapingUnshapedVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingUnshapedVal.setStatus("current")
_ShapingUnshapedMom_Type = CounterBasedGauge64
_ShapingUnshapedMom_Object = MibScalar
shapingUnshapedMom = _ShapingUnshapedMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 39, 2),
    _ShapingUnshapedMom_Type()
)
shapingUnshapedMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingUnshapedMom.setStatus("current")
_ShapingUnshapedMax_Type = CounterBasedGauge64
_ShapingUnshapedMax_Object = MibScalar
shapingUnshapedMax = _ShapingUnshapedMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 39, 3),
    _ShapingUnshapedMax_Type()
)
shapingUnshapedMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingUnshapedMax.setStatus("current")
_ShapingUnshapedBytes_ObjectIdentity = ObjectIdentity
shapingUnshapedBytes = _ShapingUnshapedBytes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 40)
)
_ShapingUnshapedBytesVal_Type = Counter64
_ShapingUnshapedBytesVal_Object = MibScalar
shapingUnshapedBytesVal = _ShapingUnshapedBytesVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 40, 1),
    _ShapingUnshapedBytesVal_Type()
)
shapingUnshapedBytesVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingUnshapedBytesVal.setStatus("current")
_ShapingUnshapedBytesMom_Type = CounterBasedGauge64
_ShapingUnshapedBytesMom_Object = MibScalar
shapingUnshapedBytesMom = _ShapingUnshapedBytesMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 40, 2),
    _ShapingUnshapedBytesMom_Type()
)
shapingUnshapedBytesMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingUnshapedBytesMom.setStatus("current")
_ShapingUnshapedBytesMax_Type = CounterBasedGauge64
_ShapingUnshapedBytesMax_Object = MibScalar
shapingUnshapedBytesMax = _ShapingUnshapedBytesMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 40, 3),
    _ShapingUnshapedBytesMax_Type()
)
shapingUnshapedBytesMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingUnshapedBytesMax.setStatus("current")
_ShapingDequeueCalls_ObjectIdentity = ObjectIdentity
shapingDequeueCalls = _ShapingDequeueCalls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 41)
)
_ShapingDequeueCallsVal_Type = Counter64
_ShapingDequeueCallsVal_Object = MibScalar
shapingDequeueCallsVal = _ShapingDequeueCallsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 41, 1),
    _ShapingDequeueCallsVal_Type()
)
shapingDequeueCallsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingDequeueCallsVal.setStatus("current")
_ShapingDequeueCallsMom_Type = CounterBasedGauge64
_ShapingDequeueCallsMom_Object = MibScalar
shapingDequeueCallsMom = _ShapingDequeueCallsMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 41, 2),
    _ShapingDequeueCallsMom_Type()
)
shapingDequeueCallsMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingDequeueCallsMom.setStatus("current")
_ShapingDequeueCallsMax_Type = CounterBasedGauge64
_ShapingDequeueCallsMax_Object = MibScalar
shapingDequeueCallsMax = _ShapingDequeueCallsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 41, 3),
    _ShapingDequeueCallsMax_Type()
)
shapingDequeueCallsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingDequeueCallsMax.setStatus("current")
_ShapingRecycleObjects_ObjectIdentity = ObjectIdentity
shapingRecycleObjects = _ShapingRecycleObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 42)
)
_ShapingRecycleObjectsVal_Type = CounterBasedGauge64
_ShapingRecycleObjectsVal_Object = MibScalar
shapingRecycleObjectsVal = _ShapingRecycleObjectsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 42, 1),
    _ShapingRecycleObjectsVal_Type()
)
shapingRecycleObjectsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingRecycleObjectsVal.setStatus("current")
_ShapingRecycleObjectsMax_Type = CounterBasedGauge64
_ShapingRecycleObjectsMax_Object = MibScalar
shapingRecycleObjectsMax = _ShapingRecycleObjectsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 42, 3),
    _ShapingRecycleObjectsMax_Type()
)
shapingRecycleObjectsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingRecycleObjectsMax.setStatus("current")
_ShapingDirect_ObjectIdentity = ObjectIdentity
shapingDirect = _ShapingDirect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 44)
)
_ShapingDirectVal_Type = Counter64
_ShapingDirectVal_Object = MibScalar
shapingDirectVal = _ShapingDirectVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 44, 1),
    _ShapingDirectVal_Type()
)
shapingDirectVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingDirectVal.setStatus("current")
_ShapingDirectMom_Type = CounterBasedGauge64
_ShapingDirectMom_Object = MibScalar
shapingDirectMom = _ShapingDirectMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 44, 2),
    _ShapingDirectMom_Type()
)
shapingDirectMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingDirectMom.setStatus("current")
_ShapingDirectMax_Type = CounterBasedGauge64
_ShapingDirectMax_Object = MibScalar
shapingDirectMax = _ShapingDirectMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 44, 3),
    _ShapingDirectMax_Type()
)
shapingDirectMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingDirectMax.setStatus("current")
_ShapingDirectBytes_ObjectIdentity = ObjectIdentity
shapingDirectBytes = _ShapingDirectBytes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 45)
)
_ShapingDirectBytesVal_Type = Counter64
_ShapingDirectBytesVal_Object = MibScalar
shapingDirectBytesVal = _ShapingDirectBytesVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 45, 1),
    _ShapingDirectBytesVal_Type()
)
shapingDirectBytesVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingDirectBytesVal.setStatus("current")
_ShapingDirectBytesMom_Type = CounterBasedGauge64
_ShapingDirectBytesMom_Object = MibScalar
shapingDirectBytesMom = _ShapingDirectBytesMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 45, 2),
    _ShapingDirectBytesMom_Type()
)
shapingDirectBytesMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingDirectBytesMom.setStatus("current")
_ShapingDirectBytesMax_Type = CounterBasedGauge64
_ShapingDirectBytesMax_Object = MibScalar
shapingDirectBytesMax = _ShapingDirectBytesMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 45, 3),
    _ShapingDirectBytesMax_Type()
)
shapingDirectBytesMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingDirectBytesMax.setStatus("current")
_ShapingBorrowDequeues_ObjectIdentity = ObjectIdentity
shapingBorrowDequeues = _ShapingBorrowDequeues_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 46)
)
_ShapingBorrowDequeuesVal_Type = Counter64
_ShapingBorrowDequeuesVal_Object = MibScalar
shapingBorrowDequeuesVal = _ShapingBorrowDequeuesVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 46, 1),
    _ShapingBorrowDequeuesVal_Type()
)
shapingBorrowDequeuesVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingBorrowDequeuesVal.setStatus("current")
_ShapingBorrowDequeuesMom_Type = CounterBasedGauge64
_ShapingBorrowDequeuesMom_Object = MibScalar
shapingBorrowDequeuesMom = _ShapingBorrowDequeuesMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 46, 2),
    _ShapingBorrowDequeuesMom_Type()
)
shapingBorrowDequeuesMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingBorrowDequeuesMom.setStatus("current")
_ShapingBorrowDequeuesMax_Type = CounterBasedGauge64
_ShapingBorrowDequeuesMax_Object = MibScalar
shapingBorrowDequeuesMax = _ShapingBorrowDequeuesMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 46, 3),
    _ShapingBorrowDequeuesMax_Type()
)
shapingBorrowDequeuesMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingBorrowDequeuesMax.setStatus("current")
_ShapingVbsSplitError_ObjectIdentity = ObjectIdentity
shapingVbsSplitError = _ShapingVbsSplitError_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 47)
)
_ShapingVbsSplitErrorVal_Type = Counter64
_ShapingVbsSplitErrorVal_Object = MibScalar
shapingVbsSplitErrorVal = _ShapingVbsSplitErrorVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 47, 1),
    _ShapingVbsSplitErrorVal_Type()
)
shapingVbsSplitErrorVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingVbsSplitErrorVal.setStatus("obsolete")
_ShapingVbsSplitErrorMom_Type = CounterBasedGauge64
_ShapingVbsSplitErrorMom_Object = MibScalar
shapingVbsSplitErrorMom = _ShapingVbsSplitErrorMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 47, 2),
    _ShapingVbsSplitErrorMom_Type()
)
shapingVbsSplitErrorMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingVbsSplitErrorMom.setStatus("obsolete")
_ShapingVbsSplitErrorMax_Type = CounterBasedGauge64
_ShapingVbsSplitErrorMax_Object = MibScalar
shapingVbsSplitErrorMax = _ShapingVbsSplitErrorMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 47, 3),
    _ShapingVbsSplitErrorMax_Type()
)
shapingVbsSplitErrorMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingVbsSplitErrorMax.setStatus("obsolete")
_ShapingBrownHostDrops_ObjectIdentity = ObjectIdentity
shapingBrownHostDrops = _ShapingBrownHostDrops_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 48)
)
_ShapingBrownHostDropsVal_Type = Counter64
_ShapingBrownHostDropsVal_Object = MibScalar
shapingBrownHostDropsVal = _ShapingBrownHostDropsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 48, 1),
    _ShapingBrownHostDropsVal_Type()
)
shapingBrownHostDropsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingBrownHostDropsVal.setStatus("current")
_ShapingBrownHostDropsMom_Type = CounterBasedGauge64
_ShapingBrownHostDropsMom_Object = MibScalar
shapingBrownHostDropsMom = _ShapingBrownHostDropsMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 48, 2),
    _ShapingBrownHostDropsMom_Type()
)
shapingBrownHostDropsMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingBrownHostDropsMom.setStatus("current")
_ShapingBrownHostDropsMax_Type = CounterBasedGauge64
_ShapingBrownHostDropsMax_Object = MibScalar
shapingBrownHostDropsMax = _ShapingBrownHostDropsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 48, 3),
    _ShapingBrownHostDropsMax_Type()
)
shapingBrownHostDropsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingBrownHostDropsMax.setStatus("current")
_ShapingMaxConnDrops_ObjectIdentity = ObjectIdentity
shapingMaxConnDrops = _ShapingMaxConnDrops_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 49)
)
_ShapingMaxConnDropsVal_Type = Counter64
_ShapingMaxConnDropsVal_Object = MibScalar
shapingMaxConnDropsVal = _ShapingMaxConnDropsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 49, 1),
    _ShapingMaxConnDropsVal_Type()
)
shapingMaxConnDropsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingMaxConnDropsVal.setStatus("current")
_ShapingMaxConnDropsMom_Type = CounterBasedGauge64
_ShapingMaxConnDropsMom_Object = MibScalar
shapingMaxConnDropsMom = _ShapingMaxConnDropsMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 49, 2),
    _ShapingMaxConnDropsMom_Type()
)
shapingMaxConnDropsMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingMaxConnDropsMom.setStatus("current")
_ShapingMaxConnDropsMax_Type = CounterBasedGauge64
_ShapingMaxConnDropsMax_Object = MibScalar
shapingMaxConnDropsMax = _ShapingMaxConnDropsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 49, 3),
    _ShapingMaxConnDropsMax_Type()
)
shapingMaxConnDropsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingMaxConnDropsMax.setStatus("current")
_ShapingScheduledOdirs_ObjectIdentity = ObjectIdentity
shapingScheduledOdirs = _ShapingScheduledOdirs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 50)
)
_ShapingScheduledOdirsVal_Type = CounterBasedGauge64
_ShapingScheduledOdirsVal_Object = MibScalar
shapingScheduledOdirsVal = _ShapingScheduledOdirsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 50, 1),
    _ShapingScheduledOdirsVal_Type()
)
shapingScheduledOdirsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingScheduledOdirsVal.setStatus("current")
_ShapingScheduledOdirsMax_Type = CounterBasedGauge64
_ShapingScheduledOdirsMax_Object = MibScalar
shapingScheduledOdirsMax = _ShapingScheduledOdirsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 50, 3),
    _ShapingScheduledOdirsMax_Type()
)
shapingScheduledOdirsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingScheduledOdirsMax.setStatus("current")
_ShapingQueuePoolExhausted_ObjectIdentity = ObjectIdentity
shapingQueuePoolExhausted = _ShapingQueuePoolExhausted_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 51)
)
_ShapingQueuePoolExhaustedVal_Type = Counter64
_ShapingQueuePoolExhaustedVal_Object = MibScalar
shapingQueuePoolExhaustedVal = _ShapingQueuePoolExhaustedVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 51, 1),
    _ShapingQueuePoolExhaustedVal_Type()
)
shapingQueuePoolExhaustedVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingQueuePoolExhaustedVal.setStatus("current")
_ShapingQueuePoolExhaustedMom_Type = CounterBasedGauge64
_ShapingQueuePoolExhaustedMom_Object = MibScalar
shapingQueuePoolExhaustedMom = _ShapingQueuePoolExhaustedMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 51, 2),
    _ShapingQueuePoolExhaustedMom_Type()
)
shapingQueuePoolExhaustedMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingQueuePoolExhaustedMom.setStatus("current")
_ShapingQueuePoolExhaustedMax_Type = CounterBasedGauge64
_ShapingQueuePoolExhaustedMax_Object = MibScalar
shapingQueuePoolExhaustedMax = _ShapingQueuePoolExhaustedMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 51, 3),
    _ShapingQueuePoolExhaustedMax_Type()
)
shapingQueuePoolExhaustedMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingQueuePoolExhaustedMax.setStatus("current")
_ShapingActiveQueues_ObjectIdentity = ObjectIdentity
shapingActiveQueues = _ShapingActiveQueues_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 52)
)
_ShapingActiveQueuesVal_Type = CounterBasedGauge64
_ShapingActiveQueuesVal_Object = MibScalar
shapingActiveQueuesVal = _ShapingActiveQueuesVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 52, 1),
    _ShapingActiveQueuesVal_Type()
)
shapingActiveQueuesVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingActiveQueuesVal.setStatus("current")
_ShapingActiveQueuesMax_Type = CounterBasedGauge64
_ShapingActiveQueuesMax_Object = MibScalar
shapingActiveQueuesMax = _ShapingActiveQueuesMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 52, 3),
    _ShapingActiveQueuesMax_Type()
)
shapingActiveQueuesMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingActiveQueuesMax.setStatus("current")
_ShapingQueueAllocations_ObjectIdentity = ObjectIdentity
shapingQueueAllocations = _ShapingQueueAllocations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 53)
)
_ShapingQueueAllocationsVal_Type = Counter64
_ShapingQueueAllocationsVal_Object = MibScalar
shapingQueueAllocationsVal = _ShapingQueueAllocationsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 53, 1),
    _ShapingQueueAllocationsVal_Type()
)
shapingQueueAllocationsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingQueueAllocationsVal.setStatus("current")
_ShapingQueueAllocationsMom_Type = CounterBasedGauge64
_ShapingQueueAllocationsMom_Object = MibScalar
shapingQueueAllocationsMom = _ShapingQueueAllocationsMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 53, 2),
    _ShapingQueueAllocationsMom_Type()
)
shapingQueueAllocationsMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingQueueAllocationsMom.setStatus("current")
_ShapingQueueAllocationsMax_Type = CounterBasedGauge64
_ShapingQueueAllocationsMax_Object = MibScalar
shapingQueueAllocationsMax = _ShapingQueueAllocationsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 53, 3),
    _ShapingQueueAllocationsMax_Type()
)
shapingQueueAllocationsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingQueueAllocationsMax.setStatus("current")
_ShapingDropsPrio1_ObjectIdentity = ObjectIdentity
shapingDropsPrio1 = _ShapingDropsPrio1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 54)
)
_ShapingDropsPrio1Val_Type = Counter64
_ShapingDropsPrio1Val_Object = MibScalar
shapingDropsPrio1Val = _ShapingDropsPrio1Val_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 54, 1),
    _ShapingDropsPrio1Val_Type()
)
shapingDropsPrio1Val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingDropsPrio1Val.setStatus("current")
_ShapingDropsPrio1Mom_Type = CounterBasedGauge64
_ShapingDropsPrio1Mom_Object = MibScalar
shapingDropsPrio1Mom = _ShapingDropsPrio1Mom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 54, 2),
    _ShapingDropsPrio1Mom_Type()
)
shapingDropsPrio1Mom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingDropsPrio1Mom.setStatus("current")
_ShapingDropsPrio1Max_Type = CounterBasedGauge64
_ShapingDropsPrio1Max_Object = MibScalar
shapingDropsPrio1Max = _ShapingDropsPrio1Max_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 54, 3),
    _ShapingDropsPrio1Max_Type()
)
shapingDropsPrio1Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingDropsPrio1Max.setStatus("current")
_ShapingDropsPrio2_ObjectIdentity = ObjectIdentity
shapingDropsPrio2 = _ShapingDropsPrio2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 55)
)
_ShapingDropsPrio2Val_Type = Counter64
_ShapingDropsPrio2Val_Object = MibScalar
shapingDropsPrio2Val = _ShapingDropsPrio2Val_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 55, 1),
    _ShapingDropsPrio2Val_Type()
)
shapingDropsPrio2Val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingDropsPrio2Val.setStatus("current")
_ShapingDropsPrio2Mom_Type = CounterBasedGauge64
_ShapingDropsPrio2Mom_Object = MibScalar
shapingDropsPrio2Mom = _ShapingDropsPrio2Mom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 55, 2),
    _ShapingDropsPrio2Mom_Type()
)
shapingDropsPrio2Mom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingDropsPrio2Mom.setStatus("current")
_ShapingDropsPrio2Max_Type = CounterBasedGauge64
_ShapingDropsPrio2Max_Object = MibScalar
shapingDropsPrio2Max = _ShapingDropsPrio2Max_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 55, 3),
    _ShapingDropsPrio2Max_Type()
)
shapingDropsPrio2Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingDropsPrio2Max.setStatus("current")
_ShapingDropsPrio3_ObjectIdentity = ObjectIdentity
shapingDropsPrio3 = _ShapingDropsPrio3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 56)
)
_ShapingDropsPrio3Val_Type = Counter64
_ShapingDropsPrio3Val_Object = MibScalar
shapingDropsPrio3Val = _ShapingDropsPrio3Val_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 56, 1),
    _ShapingDropsPrio3Val_Type()
)
shapingDropsPrio3Val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingDropsPrio3Val.setStatus("current")
_ShapingDropsPrio3Mom_Type = CounterBasedGauge64
_ShapingDropsPrio3Mom_Object = MibScalar
shapingDropsPrio3Mom = _ShapingDropsPrio3Mom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 56, 2),
    _ShapingDropsPrio3Mom_Type()
)
shapingDropsPrio3Mom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingDropsPrio3Mom.setStatus("current")
_ShapingDropsPrio3Max_Type = CounterBasedGauge64
_ShapingDropsPrio3Max_Object = MibScalar
shapingDropsPrio3Max = _ShapingDropsPrio3Max_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 56, 3),
    _ShapingDropsPrio3Max_Type()
)
shapingDropsPrio3Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingDropsPrio3Max.setStatus("current")
_ShapingDropsPrio4_ObjectIdentity = ObjectIdentity
shapingDropsPrio4 = _ShapingDropsPrio4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 57)
)
_ShapingDropsPrio4Val_Type = Counter64
_ShapingDropsPrio4Val_Object = MibScalar
shapingDropsPrio4Val = _ShapingDropsPrio4Val_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 57, 1),
    _ShapingDropsPrio4Val_Type()
)
shapingDropsPrio4Val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingDropsPrio4Val.setStatus("current")
_ShapingDropsPrio4Mom_Type = CounterBasedGauge64
_ShapingDropsPrio4Mom_Object = MibScalar
shapingDropsPrio4Mom = _ShapingDropsPrio4Mom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 57, 2),
    _ShapingDropsPrio4Mom_Type()
)
shapingDropsPrio4Mom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingDropsPrio4Mom.setStatus("current")
_ShapingDropsPrio4Max_Type = CounterBasedGauge64
_ShapingDropsPrio4Max_Object = MibScalar
shapingDropsPrio4Max = _ShapingDropsPrio4Max_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 57, 3),
    _ShapingDropsPrio4Max_Type()
)
shapingDropsPrio4Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingDropsPrio4Max.setStatus("current")
_ShapingDropsPrio5_ObjectIdentity = ObjectIdentity
shapingDropsPrio5 = _ShapingDropsPrio5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 58)
)
_ShapingDropsPrio5Val_Type = Counter64
_ShapingDropsPrio5Val_Object = MibScalar
shapingDropsPrio5Val = _ShapingDropsPrio5Val_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 58, 1),
    _ShapingDropsPrio5Val_Type()
)
shapingDropsPrio5Val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingDropsPrio5Val.setStatus("current")
_ShapingDropsPrio5Mom_Type = CounterBasedGauge64
_ShapingDropsPrio5Mom_Object = MibScalar
shapingDropsPrio5Mom = _ShapingDropsPrio5Mom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 58, 2),
    _ShapingDropsPrio5Mom_Type()
)
shapingDropsPrio5Mom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingDropsPrio5Mom.setStatus("current")
_ShapingDropsPrio5Max_Type = CounterBasedGauge64
_ShapingDropsPrio5Max_Object = MibScalar
shapingDropsPrio5Max = _ShapingDropsPrio5Max_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 58, 3),
    _ShapingDropsPrio5Max_Type()
)
shapingDropsPrio5Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingDropsPrio5Max.setStatus("current")
_ShapingDropsPrio6_ObjectIdentity = ObjectIdentity
shapingDropsPrio6 = _ShapingDropsPrio6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 59)
)
_ShapingDropsPrio6Val_Type = Counter64
_ShapingDropsPrio6Val_Object = MibScalar
shapingDropsPrio6Val = _ShapingDropsPrio6Val_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 59, 1),
    _ShapingDropsPrio6Val_Type()
)
shapingDropsPrio6Val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingDropsPrio6Val.setStatus("current")
_ShapingDropsPrio6Mom_Type = CounterBasedGauge64
_ShapingDropsPrio6Mom_Object = MibScalar
shapingDropsPrio6Mom = _ShapingDropsPrio6Mom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 59, 2),
    _ShapingDropsPrio6Mom_Type()
)
shapingDropsPrio6Mom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingDropsPrio6Mom.setStatus("current")
_ShapingDropsPrio6Max_Type = CounterBasedGauge64
_ShapingDropsPrio6Max_Object = MibScalar
shapingDropsPrio6Max = _ShapingDropsPrio6Max_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 59, 3),
    _ShapingDropsPrio6Max_Type()
)
shapingDropsPrio6Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingDropsPrio6Max.setStatus("current")
_ShapingDropsPrio7_ObjectIdentity = ObjectIdentity
shapingDropsPrio7 = _ShapingDropsPrio7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 60)
)
_ShapingDropsPrio7Val_Type = Counter64
_ShapingDropsPrio7Val_Object = MibScalar
shapingDropsPrio7Val = _ShapingDropsPrio7Val_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 60, 1),
    _ShapingDropsPrio7Val_Type()
)
shapingDropsPrio7Val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingDropsPrio7Val.setStatus("current")
_ShapingDropsPrio7Mom_Type = CounterBasedGauge64
_ShapingDropsPrio7Mom_Object = MibScalar
shapingDropsPrio7Mom = _ShapingDropsPrio7Mom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 60, 2),
    _ShapingDropsPrio7Mom_Type()
)
shapingDropsPrio7Mom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingDropsPrio7Mom.setStatus("current")
_ShapingDropsPrio7Max_Type = CounterBasedGauge64
_ShapingDropsPrio7Max_Object = MibScalar
shapingDropsPrio7Max = _ShapingDropsPrio7Max_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 60, 3),
    _ShapingDropsPrio7Max_Type()
)
shapingDropsPrio7Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingDropsPrio7Max.setStatus("current")
_ShapingDropsPrio8_ObjectIdentity = ObjectIdentity
shapingDropsPrio8 = _ShapingDropsPrio8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 61)
)
_ShapingDropsPrio8Val_Type = Counter64
_ShapingDropsPrio8Val_Object = MibScalar
shapingDropsPrio8Val = _ShapingDropsPrio8Val_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 61, 1),
    _ShapingDropsPrio8Val_Type()
)
shapingDropsPrio8Val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingDropsPrio8Val.setStatus("current")
_ShapingDropsPrio8Mom_Type = CounterBasedGauge64
_ShapingDropsPrio8Mom_Object = MibScalar
shapingDropsPrio8Mom = _ShapingDropsPrio8Mom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 61, 2),
    _ShapingDropsPrio8Mom_Type()
)
shapingDropsPrio8Mom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingDropsPrio8Mom.setStatus("current")
_ShapingDropsPrio8Max_Type = CounterBasedGauge64
_ShapingDropsPrio8Max_Object = MibScalar
shapingDropsPrio8Max = _ShapingDropsPrio8Max_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 61, 3),
    _ShapingDropsPrio8Max_Type()
)
shapingDropsPrio8Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingDropsPrio8Max.setStatus("current")
_ShapingDropsPrio9_ObjectIdentity = ObjectIdentity
shapingDropsPrio9 = _ShapingDropsPrio9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 62)
)
_ShapingDropsPrio9Val_Type = Counter64
_ShapingDropsPrio9Val_Object = MibScalar
shapingDropsPrio9Val = _ShapingDropsPrio9Val_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 62, 1),
    _ShapingDropsPrio9Val_Type()
)
shapingDropsPrio9Val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingDropsPrio9Val.setStatus("current")
_ShapingDropsPrio9Mom_Type = CounterBasedGauge64
_ShapingDropsPrio9Mom_Object = MibScalar
shapingDropsPrio9Mom = _ShapingDropsPrio9Mom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 62, 2),
    _ShapingDropsPrio9Mom_Type()
)
shapingDropsPrio9Mom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingDropsPrio9Mom.setStatus("current")
_ShapingDropsPrio9Max_Type = CounterBasedGauge64
_ShapingDropsPrio9Max_Object = MibScalar
shapingDropsPrio9Max = _ShapingDropsPrio9Max_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 62, 3),
    _ShapingDropsPrio9Max_Type()
)
shapingDropsPrio9Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingDropsPrio9Max.setStatus("current")
_ShapingDropsPrioOther_ObjectIdentity = ObjectIdentity
shapingDropsPrioOther = _ShapingDropsPrioOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 63)
)
_ShapingDropsPrioOtherVal_Type = Counter64
_ShapingDropsPrioOtherVal_Object = MibScalar
shapingDropsPrioOtherVal = _ShapingDropsPrioOtherVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 63, 1),
    _ShapingDropsPrioOtherVal_Type()
)
shapingDropsPrioOtherVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingDropsPrioOtherVal.setStatus("current")
_ShapingDropsPrioOtherMom_Type = CounterBasedGauge64
_ShapingDropsPrioOtherMom_Object = MibScalar
shapingDropsPrioOtherMom = _ShapingDropsPrioOtherMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 63, 2),
    _ShapingDropsPrioOtherMom_Type()
)
shapingDropsPrioOtherMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingDropsPrioOtherMom.setStatus("current")
_ShapingDropsPrioOtherMax_Type = CounterBasedGauge64
_ShapingDropsPrioOtherMax_Object = MibScalar
shapingDropsPrioOtherMax = _ShapingDropsPrioOtherMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 63, 3),
    _ShapingDropsPrioOtherMax_Type()
)
shapingDropsPrioOtherMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingDropsPrioOtherMax.setStatus("current")
_ShapingDropsCps_ObjectIdentity = ObjectIdentity
shapingDropsCps = _ShapingDropsCps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 64)
)
_ShapingDropsCpsVal_Type = Counter64
_ShapingDropsCpsVal_Object = MibScalar
shapingDropsCpsVal = _ShapingDropsCpsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 64, 1),
    _ShapingDropsCpsVal_Type()
)
shapingDropsCpsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingDropsCpsVal.setStatus("current")
_ShapingDropsCpsMom_Type = CounterBasedGauge64
_ShapingDropsCpsMom_Object = MibScalar
shapingDropsCpsMom = _ShapingDropsCpsMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 64, 2),
    _ShapingDropsCpsMom_Type()
)
shapingDropsCpsMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingDropsCpsMom.setStatus("current")
_ShapingDropsCpsMax_Type = CounterBasedGauge64
_ShapingDropsCpsMax_Object = MibScalar
shapingDropsCpsMax = _ShapingDropsCpsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 64, 3),
    _ShapingDropsCpsMax_Type()
)
shapingDropsCpsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingDropsCpsMax.setStatus("current")
_ShapingFailedFairnessObjects_ObjectIdentity = ObjectIdentity
shapingFailedFairnessObjects = _ShapingFailedFairnessObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 65)
)
_ShapingFailedFairnessObjectsVal_Type = Counter64
_ShapingFailedFairnessObjectsVal_Object = MibScalar
shapingFailedFairnessObjectsVal = _ShapingFailedFairnessObjectsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 65, 1),
    _ShapingFailedFairnessObjectsVal_Type()
)
shapingFailedFairnessObjectsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingFailedFairnessObjectsVal.setStatus("current")
_ShapingFailedFairnessObjectsMom_Type = CounterBasedGauge64
_ShapingFailedFairnessObjectsMom_Object = MibScalar
shapingFailedFairnessObjectsMom = _ShapingFailedFairnessObjectsMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 65, 2),
    _ShapingFailedFairnessObjectsMom_Type()
)
shapingFailedFairnessObjectsMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingFailedFairnessObjectsMom.setStatus("current")
_ShapingFailedFairnessObjectsMax_Type = CounterBasedGauge64
_ShapingFailedFairnessObjectsMax_Object = MibScalar
shapingFailedFairnessObjectsMax = _ShapingFailedFairnessObjectsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 65, 3),
    _ShapingFailedFairnessObjectsMax_Type()
)
shapingFailedFairnessObjectsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingFailedFairnessObjectsMax.setStatus("current")
_ShapingUsedFairnessObjects_ObjectIdentity = ObjectIdentity
shapingUsedFairnessObjects = _ShapingUsedFairnessObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 66)
)
_ShapingUsedFairnessObjectsVal_Type = CounterBasedGauge64
_ShapingUsedFairnessObjectsVal_Object = MibScalar
shapingUsedFairnessObjectsVal = _ShapingUsedFairnessObjectsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 66, 1),
    _ShapingUsedFairnessObjectsVal_Type()
)
shapingUsedFairnessObjectsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingUsedFairnessObjectsVal.setStatus("current")
_ShapingUsedFairnessObjectsMax_Type = CounterBasedGauge64
_ShapingUsedFairnessObjectsMax_Object = MibScalar
shapingUsedFairnessObjectsMax = _ShapingUsedFairnessObjectsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 66, 3),
    _ShapingUsedFairnessObjectsMax_Type()
)
shapingUsedFairnessObjectsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingUsedFairnessObjectsMax.setStatus("current")
_ShapingReloadDrops_ObjectIdentity = ObjectIdentity
shapingReloadDrops = _ShapingReloadDrops_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 67)
)
_ShapingReloadDropsVal_Type = Counter64
_ShapingReloadDropsVal_Object = MibScalar
shapingReloadDropsVal = _ShapingReloadDropsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 67, 1),
    _ShapingReloadDropsVal_Type()
)
shapingReloadDropsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingReloadDropsVal.setStatus("current")
_ShapingReloadDropsMom_Type = CounterBasedGauge64
_ShapingReloadDropsMom_Object = MibScalar
shapingReloadDropsMom = _ShapingReloadDropsMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 67, 2),
    _ShapingReloadDropsMom_Type()
)
shapingReloadDropsMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingReloadDropsMom.setStatus("current")
_ShapingReloadDropsMax_Type = CounterBasedGauge64
_ShapingReloadDropsMax_Object = MibScalar
shapingReloadDropsMax = _ShapingReloadDropsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 67, 3),
    _ShapingReloadDropsMax_Type()
)
shapingReloadDropsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingReloadDropsMax.setStatus("current")
_ShapingRequeueQueueUsed_ObjectIdentity = ObjectIdentity
shapingRequeueQueueUsed = _ShapingRequeueQueueUsed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 68)
)
_ShapingRequeueQueueUsedVal_Type = CounterBasedGauge64
_ShapingRequeueQueueUsedVal_Object = MibScalar
shapingRequeueQueueUsedVal = _ShapingRequeueQueueUsedVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 68, 1),
    _ShapingRequeueQueueUsedVal_Type()
)
shapingRequeueQueueUsedVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingRequeueQueueUsedVal.setStatus("current")
_ShapingRequeueQueueUsedMax_Type = CounterBasedGauge64
_ShapingRequeueQueueUsedMax_Object = MibScalar
shapingRequeueQueueUsedMax = _ShapingRequeueQueueUsedMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 68, 3),
    _ShapingRequeueQueueUsedMax_Type()
)
shapingRequeueQueueUsedMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingRequeueQueueUsedMax.setStatus("current")
_ShapingDirectBytesPrio0_ObjectIdentity = ObjectIdentity
shapingDirectBytesPrio0 = _ShapingDirectBytesPrio0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 69)
)
_ShapingDirectBytesPrio0Val_Type = Counter64
_ShapingDirectBytesPrio0Val_Object = MibScalar
shapingDirectBytesPrio0Val = _ShapingDirectBytesPrio0Val_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 69, 1),
    _ShapingDirectBytesPrio0Val_Type()
)
shapingDirectBytesPrio0Val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingDirectBytesPrio0Val.setStatus("current")
_ShapingDirectBytesPrio0Mom_Type = CounterBasedGauge64
_ShapingDirectBytesPrio0Mom_Object = MibScalar
shapingDirectBytesPrio0Mom = _ShapingDirectBytesPrio0Mom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 69, 2),
    _ShapingDirectBytesPrio0Mom_Type()
)
shapingDirectBytesPrio0Mom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingDirectBytesPrio0Mom.setStatus("current")
_ShapingDirectBytesPrio0Max_Type = CounterBasedGauge64
_ShapingDirectBytesPrio0Max_Object = MibScalar
shapingDirectBytesPrio0Max = _ShapingDirectBytesPrio0Max_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 69, 3),
    _ShapingDirectBytesPrio0Max_Type()
)
shapingDirectBytesPrio0Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingDirectBytesPrio0Max.setStatus("current")
_ShapingDequeuedOdirs_ObjectIdentity = ObjectIdentity
shapingDequeuedOdirs = _ShapingDequeuedOdirs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 70)
)
_ShapingDequeuedOdirsVal_Type = Counter64
_ShapingDequeuedOdirsVal_Object = MibScalar
shapingDequeuedOdirsVal = _ShapingDequeuedOdirsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 70, 1),
    _ShapingDequeuedOdirsVal_Type()
)
shapingDequeuedOdirsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingDequeuedOdirsVal.setStatus("current")
_ShapingDequeuedOdirsMom_Type = CounterBasedGauge64
_ShapingDequeuedOdirsMom_Object = MibScalar
shapingDequeuedOdirsMom = _ShapingDequeuedOdirsMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 70, 2),
    _ShapingDequeuedOdirsMom_Type()
)
shapingDequeuedOdirsMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingDequeuedOdirsMom.setStatus("current")
_ShapingDequeuedOdirsMax_Type = CounterBasedGauge64
_ShapingDequeuedOdirsMax_Object = MibScalar
shapingDequeuedOdirsMax = _ShapingDequeuedOdirsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 70, 3),
    _ShapingDequeuedOdirsMax_Type()
)
shapingDequeuedOdirsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingDequeuedOdirsMax.setStatus("current")
_ShapingSkippedQsyncUpdates_ObjectIdentity = ObjectIdentity
shapingSkippedQsyncUpdates = _ShapingSkippedQsyncUpdates_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 71)
)
_ShapingSkippedQsyncUpdatesVal_Type = Counter64
_ShapingSkippedQsyncUpdatesVal_Object = MibScalar
shapingSkippedQsyncUpdatesVal = _ShapingSkippedQsyncUpdatesVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 71, 1),
    _ShapingSkippedQsyncUpdatesVal_Type()
)
shapingSkippedQsyncUpdatesVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingSkippedQsyncUpdatesVal.setStatus("current")
_ShapingSkippedQsyncUpdatesMom_Type = CounterBasedGauge64
_ShapingSkippedQsyncUpdatesMom_Object = MibScalar
shapingSkippedQsyncUpdatesMom = _ShapingSkippedQsyncUpdatesMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 71, 2),
    _ShapingSkippedQsyncUpdatesMom_Type()
)
shapingSkippedQsyncUpdatesMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingSkippedQsyncUpdatesMom.setStatus("current")
_ShapingSkippedQsyncUpdatesMax_Type = CounterBasedGauge64
_ShapingSkippedQsyncUpdatesMax_Object = MibScalar
shapingSkippedQsyncUpdatesMax = _ShapingSkippedQsyncUpdatesMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 71, 3),
    _ShapingSkippedQsyncUpdatesMax_Type()
)
shapingSkippedQsyncUpdatesMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingSkippedQsyncUpdatesMax.setStatus("current")
_ShapingObjectCopiesCreated_ObjectIdentity = ObjectIdentity
shapingObjectCopiesCreated = _ShapingObjectCopiesCreated_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 72)
)
_ShapingObjectCopiesCreatedVal_Type = Counter64
_ShapingObjectCopiesCreatedVal_Object = MibScalar
shapingObjectCopiesCreatedVal = _ShapingObjectCopiesCreatedVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 72, 1),
    _ShapingObjectCopiesCreatedVal_Type()
)
shapingObjectCopiesCreatedVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingObjectCopiesCreatedVal.setStatus("current")
_ShapingObjectCopiesCreatedMom_Type = CounterBasedGauge64
_ShapingObjectCopiesCreatedMom_Object = MibScalar
shapingObjectCopiesCreatedMom = _ShapingObjectCopiesCreatedMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 72, 2),
    _ShapingObjectCopiesCreatedMom_Type()
)
shapingObjectCopiesCreatedMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingObjectCopiesCreatedMom.setStatus("current")
_ShapingObjectCopiesCreatedMax_Type = CounterBasedGauge64
_ShapingObjectCopiesCreatedMax_Object = MibScalar
shapingObjectCopiesCreatedMax = _ShapingObjectCopiesCreatedMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 72, 3),
    _ShapingObjectCopiesCreatedMax_Type()
)
shapingObjectCopiesCreatedMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingObjectCopiesCreatedMax.setStatus("current")
_ShapingEcnMarks_ObjectIdentity = ObjectIdentity
shapingEcnMarks = _ShapingEcnMarks_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 73)
)
_ShapingEcnMarksVal_Type = Counter64
_ShapingEcnMarksVal_Object = MibScalar
shapingEcnMarksVal = _ShapingEcnMarksVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 73, 1),
    _ShapingEcnMarksVal_Type()
)
shapingEcnMarksVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingEcnMarksVal.setStatus("current")
_ShapingEcnMarksMom_Type = CounterBasedGauge64
_ShapingEcnMarksMom_Object = MibScalar
shapingEcnMarksMom = _ShapingEcnMarksMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 73, 2),
    _ShapingEcnMarksMom_Type()
)
shapingEcnMarksMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingEcnMarksMom.setStatus("current")
_ShapingEcnMarksMax_Type = CounterBasedGauge64
_ShapingEcnMarksMax_Object = MibScalar
shapingEcnMarksMax = _ShapingEcnMarksMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 88, 73, 3),
    _ShapingEcnMarksMax_Type()
)
shapingEcnMarksMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingEcnMarksMax.setStatus("current")
_Pppoe_ObjectIdentity = ObjectIdentity
pppoe = _Pppoe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 96)
)
_PppoeShortPackets_ObjectIdentity = ObjectIdentity
pppoeShortPackets = _PppoeShortPackets_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 96, 1)
)
_PppoeShortPacketsVal_Type = Counter64
_PppoeShortPacketsVal_Object = MibScalar
pppoeShortPacketsVal = _PppoeShortPacketsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 96, 1, 1),
    _PppoeShortPacketsVal_Type()
)
pppoeShortPacketsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppoeShortPacketsVal.setStatus("current")
_PppoeShortPacketsMom_Type = CounterBasedGauge64
_PppoeShortPacketsMom_Object = MibScalar
pppoeShortPacketsMom = _PppoeShortPacketsMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 96, 1, 2),
    _PppoeShortPacketsMom_Type()
)
pppoeShortPacketsMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppoeShortPacketsMom.setStatus("current")
_PppoeShortPacketsMax_Type = CounterBasedGauge64
_PppoeShortPacketsMax_Object = MibScalar
pppoeShortPacketsMax = _PppoeShortPacketsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 96, 1, 3),
    _PppoeShortPacketsMax_Type()
)
pppoeShortPacketsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppoeShortPacketsMax.setStatus("current")
_PppoeBadversionPackets_ObjectIdentity = ObjectIdentity
pppoeBadversionPackets = _PppoeBadversionPackets_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 96, 2)
)
_PppoeBadversionPacketsVal_Type = Counter64
_PppoeBadversionPacketsVal_Object = MibScalar
pppoeBadversionPacketsVal = _PppoeBadversionPacketsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 96, 2, 1),
    _PppoeBadversionPacketsVal_Type()
)
pppoeBadversionPacketsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppoeBadversionPacketsVal.setStatus("current")
_PppoeBadversionPacketsMom_Type = CounterBasedGauge64
_PppoeBadversionPacketsMom_Object = MibScalar
pppoeBadversionPacketsMom = _PppoeBadversionPacketsMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 96, 2, 2),
    _PppoeBadversionPacketsMom_Type()
)
pppoeBadversionPacketsMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppoeBadversionPacketsMom.setStatus("current")
_PppoeBadversionPacketsMax_Type = CounterBasedGauge64
_PppoeBadversionPacketsMax_Object = MibScalar
pppoeBadversionPacketsMax = _PppoeBadversionPacketsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 96, 2, 3),
    _PppoeBadversionPacketsMax_Type()
)
pppoeBadversionPacketsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppoeBadversionPacketsMax.setStatus("current")
_PppoeControlPackets_ObjectIdentity = ObjectIdentity
pppoeControlPackets = _PppoeControlPackets_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 96, 3)
)
_PppoeControlPacketsVal_Type = Counter64
_PppoeControlPacketsVal_Object = MibScalar
pppoeControlPacketsVal = _PppoeControlPacketsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 96, 3, 1),
    _PppoeControlPacketsVal_Type()
)
pppoeControlPacketsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppoeControlPacketsVal.setStatus("current")
_PppoeControlPacketsMom_Type = CounterBasedGauge64
_PppoeControlPacketsMom_Object = MibScalar
pppoeControlPacketsMom = _PppoeControlPacketsMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 96, 3, 2),
    _PppoeControlPacketsMom_Type()
)
pppoeControlPacketsMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppoeControlPacketsMom.setStatus("current")
_PppoeControlPacketsMax_Type = CounterBasedGauge64
_PppoeControlPacketsMax_Object = MibScalar
pppoeControlPacketsMax = _PppoeControlPacketsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 96, 3, 3),
    _PppoeControlPacketsMax_Type()
)
pppoeControlPacketsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppoeControlPacketsMax.setStatus("current")
_PppoeTruncatedPackets_ObjectIdentity = ObjectIdentity
pppoeTruncatedPackets = _PppoeTruncatedPackets_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 96, 4)
)
_PppoeTruncatedPacketsVal_Type = Counter64
_PppoeTruncatedPacketsVal_Object = MibScalar
pppoeTruncatedPacketsVal = _PppoeTruncatedPacketsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 96, 4, 1),
    _PppoeTruncatedPacketsVal_Type()
)
pppoeTruncatedPacketsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppoeTruncatedPacketsVal.setStatus("current")
_PppoeTruncatedPacketsMom_Type = CounterBasedGauge64
_PppoeTruncatedPacketsMom_Object = MibScalar
pppoeTruncatedPacketsMom = _PppoeTruncatedPacketsMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 96, 4, 2),
    _PppoeTruncatedPacketsMom_Type()
)
pppoeTruncatedPacketsMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppoeTruncatedPacketsMom.setStatus("current")
_PppoeTruncatedPacketsMax_Type = CounterBasedGauge64
_PppoeTruncatedPacketsMax_Object = MibScalar
pppoeTruncatedPacketsMax = _PppoeTruncatedPacketsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 96, 4, 3),
    _PppoeTruncatedPacketsMax_Type()
)
pppoeTruncatedPacketsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppoeTruncatedPacketsMax.setStatus("current")
_PppoePaddedPackets_ObjectIdentity = ObjectIdentity
pppoePaddedPackets = _PppoePaddedPackets_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 96, 5)
)
_PppoePaddedPacketsVal_Type = Counter64
_PppoePaddedPacketsVal_Object = MibScalar
pppoePaddedPacketsVal = _PppoePaddedPacketsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 96, 5, 1),
    _PppoePaddedPacketsVal_Type()
)
pppoePaddedPacketsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppoePaddedPacketsVal.setStatus("current")
_PppoePaddedPacketsMom_Type = CounterBasedGauge64
_PppoePaddedPacketsMom_Object = MibScalar
pppoePaddedPacketsMom = _PppoePaddedPacketsMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 96, 5, 2),
    _PppoePaddedPacketsMom_Type()
)
pppoePaddedPacketsMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppoePaddedPacketsMom.setStatus("current")
_PppoePaddedPacketsMax_Type = CounterBasedGauge64
_PppoePaddedPacketsMax_Object = MibScalar
pppoePaddedPacketsMax = _PppoePaddedPacketsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 96, 5, 3),
    _PppoePaddedPacketsMax_Type()
)
pppoePaddedPacketsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppoePaddedPacketsMax.setStatus("current")
_PppoeIpv4Packets_ObjectIdentity = ObjectIdentity
pppoeIpv4Packets = _PppoeIpv4Packets_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 96, 6)
)
_PppoeIpv4PacketsVal_Type = Counter64
_PppoeIpv4PacketsVal_Object = MibScalar
pppoeIpv4PacketsVal = _PppoeIpv4PacketsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 96, 6, 1),
    _PppoeIpv4PacketsVal_Type()
)
pppoeIpv4PacketsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppoeIpv4PacketsVal.setStatus("current")
_PppoeIpv4PacketsMom_Type = CounterBasedGauge64
_PppoeIpv4PacketsMom_Object = MibScalar
pppoeIpv4PacketsMom = _PppoeIpv4PacketsMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 96, 6, 2),
    _PppoeIpv4PacketsMom_Type()
)
pppoeIpv4PacketsMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppoeIpv4PacketsMom.setStatus("current")
_PppoeIpv4PacketsMax_Type = CounterBasedGauge64
_PppoeIpv4PacketsMax_Object = MibScalar
pppoeIpv4PacketsMax = _PppoeIpv4PacketsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 96, 6, 3),
    _PppoeIpv4PacketsMax_Type()
)
pppoeIpv4PacketsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppoeIpv4PacketsMax.setStatus("current")
_PppoeNonIpPackets_ObjectIdentity = ObjectIdentity
pppoeNonIpPackets = _PppoeNonIpPackets_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 96, 7)
)
_PppoeNonIpPacketsVal_Type = Counter64
_PppoeNonIpPacketsVal_Object = MibScalar
pppoeNonIpPacketsVal = _PppoeNonIpPacketsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 96, 7, 1),
    _PppoeNonIpPacketsVal_Type()
)
pppoeNonIpPacketsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppoeNonIpPacketsVal.setStatus("current")
_PppoeNonIpPacketsMom_Type = CounterBasedGauge64
_PppoeNonIpPacketsMom_Object = MibScalar
pppoeNonIpPacketsMom = _PppoeNonIpPacketsMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 96, 7, 2),
    _PppoeNonIpPacketsMom_Type()
)
pppoeNonIpPacketsMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppoeNonIpPacketsMom.setStatus("current")
_PppoeNonIpPacketsMax_Type = CounterBasedGauge64
_PppoeNonIpPacketsMax_Object = MibScalar
pppoeNonIpPacketsMax = _PppoeNonIpPacketsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 96, 7, 3),
    _PppoeNonIpPacketsMax_Type()
)
pppoeNonIpPacketsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppoeNonIpPacketsMax.setStatus("current")
_PppoeIpv6Packets_ObjectIdentity = ObjectIdentity
pppoeIpv6Packets = _PppoeIpv6Packets_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 96, 8)
)
_PppoeIpv6PacketsVal_Type = Counter64
_PppoeIpv6PacketsVal_Object = MibScalar
pppoeIpv6PacketsVal = _PppoeIpv6PacketsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 96, 8, 1),
    _PppoeIpv6PacketsVal_Type()
)
pppoeIpv6PacketsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppoeIpv6PacketsVal.setStatus("current")
_PppoeIpv6PacketsMom_Type = CounterBasedGauge64
_PppoeIpv6PacketsMom_Object = MibScalar
pppoeIpv6PacketsMom = _PppoeIpv6PacketsMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 96, 8, 2),
    _PppoeIpv6PacketsMom_Type()
)
pppoeIpv6PacketsMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppoeIpv6PacketsMom.setStatus("current")
_PppoeIpv6PacketsMax_Type = CounterBasedGauge64
_PppoeIpv6PacketsMax_Object = MibScalar
pppoeIpv6PacketsMax = _PppoeIpv6PacketsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 96, 8, 3),
    _PppoeIpv6PacketsMax_Type()
)
pppoeIpv6PacketsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppoeIpv6PacketsMax.setStatus("current")
_Interface_ObjectIdentity = ObjectIdentity
interface = _Interface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 120)
)
_InterfaceBytesToEngine_ObjectIdentity = ObjectIdentity
interfaceBytesToEngine = _InterfaceBytesToEngine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 120, 8)
)
_InterfaceBytesToEngineVal_Type = Counter64
_InterfaceBytesToEngineVal_Object = MibScalar
interfaceBytesToEngineVal = _InterfaceBytesToEngineVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 120, 8, 1),
    _InterfaceBytesToEngineVal_Type()
)
interfaceBytesToEngineVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceBytesToEngineVal.setStatus("current")
_InterfaceBytesToEngineMom_Type = CounterBasedGauge64
_InterfaceBytesToEngineMom_Object = MibScalar
interfaceBytesToEngineMom = _InterfaceBytesToEngineMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 120, 8, 2),
    _InterfaceBytesToEngineMom_Type()
)
interfaceBytesToEngineMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceBytesToEngineMom.setStatus("current")
_InterfaceBytesToEngineMax_Type = CounterBasedGauge64
_InterfaceBytesToEngineMax_Object = MibScalar
interfaceBytesToEngineMax = _InterfaceBytesToEngineMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 120, 8, 3),
    _InterfaceBytesToEngineMax_Type()
)
interfaceBytesToEngineMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceBytesToEngineMax.setStatus("current")
_InterfaceBytesFromEngine_ObjectIdentity = ObjectIdentity
interfaceBytesFromEngine = _InterfaceBytesFromEngine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 120, 9)
)
_InterfaceBytesFromEngineVal_Type = Counter64
_InterfaceBytesFromEngineVal_Object = MibScalar
interfaceBytesFromEngineVal = _InterfaceBytesFromEngineVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 120, 9, 1),
    _InterfaceBytesFromEngineVal_Type()
)
interfaceBytesFromEngineVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceBytesFromEngineVal.setStatus("current")
_InterfaceBytesFromEngineMom_Type = CounterBasedGauge64
_InterfaceBytesFromEngineMom_Object = MibScalar
interfaceBytesFromEngineMom = _InterfaceBytesFromEngineMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 120, 9, 2),
    _InterfaceBytesFromEngineMom_Type()
)
interfaceBytesFromEngineMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceBytesFromEngineMom.setStatus("current")
_InterfaceBytesFromEngineMax_Type = CounterBasedGauge64
_InterfaceBytesFromEngineMax_Object = MibScalar
interfaceBytesFromEngineMax = _InterfaceBytesFromEngineMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 120, 9, 3),
    _InterfaceBytesFromEngineMax_Type()
)
interfaceBytesFromEngineMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceBytesFromEngineMax.setStatus("current")
_InterfaceFlowNewMissed_ObjectIdentity = ObjectIdentity
interfaceFlowNewMissed = _InterfaceFlowNewMissed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 120, 10)
)
_InterfaceFlowNewMissedVal_Type = Counter64
_InterfaceFlowNewMissedVal_Object = MibScalar
interfaceFlowNewMissedVal = _InterfaceFlowNewMissedVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 120, 10, 1),
    _InterfaceFlowNewMissedVal_Type()
)
interfaceFlowNewMissedVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceFlowNewMissedVal.setStatus("current")
_InterfaceFlowNewMissedMom_Type = CounterBasedGauge64
_InterfaceFlowNewMissedMom_Object = MibScalar
interfaceFlowNewMissedMom = _InterfaceFlowNewMissedMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 120, 10, 2),
    _InterfaceFlowNewMissedMom_Type()
)
interfaceFlowNewMissedMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceFlowNewMissedMom.setStatus("current")
_InterfaceFlowNewMissedMax_Type = CounterBasedGauge64
_InterfaceFlowNewMissedMax_Object = MibScalar
interfaceFlowNewMissedMax = _InterfaceFlowNewMissedMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 120, 10, 3),
    _InterfaceFlowNewMissedMax_Type()
)
interfaceFlowNewMissedMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceFlowNewMissedMax.setStatus("current")
_InterfaceFlowUpdMissed_ObjectIdentity = ObjectIdentity
interfaceFlowUpdMissed = _InterfaceFlowUpdMissed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 120, 11)
)
_InterfaceFlowUpdMissedVal_Type = Counter64
_InterfaceFlowUpdMissedVal_Object = MibScalar
interfaceFlowUpdMissedVal = _InterfaceFlowUpdMissedVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 120, 11, 1),
    _InterfaceFlowUpdMissedVal_Type()
)
interfaceFlowUpdMissedVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceFlowUpdMissedVal.setStatus("current")
_InterfaceFlowUpdMissedMom_Type = CounterBasedGauge64
_InterfaceFlowUpdMissedMom_Object = MibScalar
interfaceFlowUpdMissedMom = _InterfaceFlowUpdMissedMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 120, 11, 2),
    _InterfaceFlowUpdMissedMom_Type()
)
interfaceFlowUpdMissedMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceFlowUpdMissedMom.setStatus("current")
_InterfaceFlowUpdMissedMax_Type = CounterBasedGauge64
_InterfaceFlowUpdMissedMax_Object = MibScalar
interfaceFlowUpdMissedMax = _InterfaceFlowUpdMissedMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 120, 11, 3),
    _InterfaceFlowUpdMissedMax_Type()
)
interfaceFlowUpdMissedMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceFlowUpdMissedMax.setStatus("current")
_InterfaceFlowNew_ObjectIdentity = ObjectIdentity
interfaceFlowNew = _InterfaceFlowNew_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 120, 12)
)
_InterfaceFlowNewVal_Type = Counter64
_InterfaceFlowNewVal_Object = MibScalar
interfaceFlowNewVal = _InterfaceFlowNewVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 120, 12, 1),
    _InterfaceFlowNewVal_Type()
)
interfaceFlowNewVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceFlowNewVal.setStatus("current")
_InterfaceFlowNewMom_Type = CounterBasedGauge64
_InterfaceFlowNewMom_Object = MibScalar
interfaceFlowNewMom = _InterfaceFlowNewMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 120, 12, 2),
    _InterfaceFlowNewMom_Type()
)
interfaceFlowNewMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceFlowNewMom.setStatus("current")
_InterfaceFlowNewMax_Type = CounterBasedGauge64
_InterfaceFlowNewMax_Object = MibScalar
interfaceFlowNewMax = _InterfaceFlowNewMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 120, 12, 3),
    _InterfaceFlowNewMax_Type()
)
interfaceFlowNewMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceFlowNewMax.setStatus("current")
_InterfaceFlowHostnameAllocFail_ObjectIdentity = ObjectIdentity
interfaceFlowHostnameAllocFail = _InterfaceFlowHostnameAllocFail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 120, 13)
)
_InterfaceFlowHostnameAllocFailVal_Type = Counter64
_InterfaceFlowHostnameAllocFailVal_Object = MibScalar
interfaceFlowHostnameAllocFailVal = _InterfaceFlowHostnameAllocFailVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 120, 13, 1),
    _InterfaceFlowHostnameAllocFailVal_Type()
)
interfaceFlowHostnameAllocFailVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceFlowHostnameAllocFailVal.setStatus("current")
_InterfaceFlowHostnameAllocFailMom_Type = CounterBasedGauge64
_InterfaceFlowHostnameAllocFailMom_Object = MibScalar
interfaceFlowHostnameAllocFailMom = _InterfaceFlowHostnameAllocFailMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 120, 13, 2),
    _InterfaceFlowHostnameAllocFailMom_Type()
)
interfaceFlowHostnameAllocFailMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceFlowHostnameAllocFailMom.setStatus("current")
_InterfaceFlowHostnameAllocFailMax_Type = CounterBasedGauge64
_InterfaceFlowHostnameAllocFailMax_Object = MibScalar
interfaceFlowHostnameAllocFailMax = _InterfaceFlowHostnameAllocFailMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 120, 13, 3),
    _InterfaceFlowHostnameAllocFailMax_Type()
)
interfaceFlowHostnameAllocFailMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceFlowHostnameAllocFailMax.setStatus("current")
_InterfaceFlowUpdReordered_ObjectIdentity = ObjectIdentity
interfaceFlowUpdReordered = _InterfaceFlowUpdReordered_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 120, 14)
)
_InterfaceFlowUpdReorderedVal_Type = Counter64
_InterfaceFlowUpdReorderedVal_Object = MibScalar
interfaceFlowUpdReorderedVal = _InterfaceFlowUpdReorderedVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 120, 14, 1),
    _InterfaceFlowUpdReorderedVal_Type()
)
interfaceFlowUpdReorderedVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceFlowUpdReorderedVal.setStatus("current")
_InterfaceFlowUpdReorderedMom_Type = CounterBasedGauge64
_InterfaceFlowUpdReorderedMom_Object = MibScalar
interfaceFlowUpdReorderedMom = _InterfaceFlowUpdReorderedMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 120, 14, 2),
    _InterfaceFlowUpdReorderedMom_Type()
)
interfaceFlowUpdReorderedMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceFlowUpdReorderedMom.setStatus("current")
_InterfaceFlowUpdReorderedMax_Type = CounterBasedGauge64
_InterfaceFlowUpdReorderedMax_Object = MibScalar
interfaceFlowUpdReorderedMax = _InterfaceFlowUpdReorderedMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 120, 14, 3),
    _InterfaceFlowUpdReorderedMax_Type()
)
interfaceFlowUpdReorderedMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceFlowUpdReorderedMax.setStatus("current")
_Dynnetobjs_ObjectIdentity = ObjectIdentity
dynnetobjs = _Dynnetobjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 121)
)
_DynamicnetobjectFailedInserts_ObjectIdentity = ObjectIdentity
dynamicnetobjectFailedInserts = _DynamicnetobjectFailedInserts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 121, 1)
)
_DynamicnetobjectFailedInsertsVal_Type = Counter64
_DynamicnetobjectFailedInsertsVal_Object = MibScalar
dynamicnetobjectFailedInsertsVal = _DynamicnetobjectFailedInsertsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 121, 1, 1),
    _DynamicnetobjectFailedInsertsVal_Type()
)
dynamicnetobjectFailedInsertsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dynamicnetobjectFailedInsertsVal.setStatus("current")
_DynamicnetobjectFailedInsertsMom_Type = CounterBasedGauge64
_DynamicnetobjectFailedInsertsMom_Object = MibScalar
dynamicnetobjectFailedInsertsMom = _DynamicnetobjectFailedInsertsMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 121, 1, 2),
    _DynamicnetobjectFailedInsertsMom_Type()
)
dynamicnetobjectFailedInsertsMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dynamicnetobjectFailedInsertsMom.setStatus("current")
_DynamicnetobjectFailedInsertsMax_Type = CounterBasedGauge64
_DynamicnetobjectFailedInsertsMax_Object = MibScalar
dynamicnetobjectFailedInsertsMax = _DynamicnetobjectFailedInsertsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 121, 1, 3),
    _DynamicnetobjectFailedInsertsMax_Type()
)
dynamicnetobjectFailedInsertsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dynamicnetobjectFailedInsertsMax.setStatus("current")
_DynamicnetobjectListItems_ObjectIdentity = ObjectIdentity
dynamicnetobjectListItems = _DynamicnetobjectListItems_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 121, 2)
)
_DynamicnetobjectListItemsVal_Type = CounterBasedGauge64
_DynamicnetobjectListItemsVal_Object = MibScalar
dynamicnetobjectListItemsVal = _DynamicnetobjectListItemsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 121, 2, 1),
    _DynamicnetobjectListItemsVal_Type()
)
dynamicnetobjectListItemsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dynamicnetobjectListItemsVal.setStatus("current")
_DynamicnetobjectListItemsMax_Type = CounterBasedGauge64
_DynamicnetobjectListItemsMax_Object = MibScalar
dynamicnetobjectListItemsMax = _DynamicnetobjectListItemsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 121, 2, 3),
    _DynamicnetobjectListItemsMax_Type()
)
dynamicnetobjectListItemsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dynamicnetobjectListItemsMax.setStatus("current")
_DynamicnetobjectRemoveSucceeded_ObjectIdentity = ObjectIdentity
dynamicnetobjectRemoveSucceeded = _DynamicnetobjectRemoveSucceeded_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 121, 3)
)
_DynamicnetobjectRemoveSucceededVal_Type = Counter64
_DynamicnetobjectRemoveSucceededVal_Object = MibScalar
dynamicnetobjectRemoveSucceededVal = _DynamicnetobjectRemoveSucceededVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 121, 3, 1),
    _DynamicnetobjectRemoveSucceededVal_Type()
)
dynamicnetobjectRemoveSucceededVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dynamicnetobjectRemoveSucceededVal.setStatus("current")
_DynamicnetobjectRemoveSucceededMom_Type = CounterBasedGauge64
_DynamicnetobjectRemoveSucceededMom_Object = MibScalar
dynamicnetobjectRemoveSucceededMom = _DynamicnetobjectRemoveSucceededMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 121, 3, 2),
    _DynamicnetobjectRemoveSucceededMom_Type()
)
dynamicnetobjectRemoveSucceededMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dynamicnetobjectRemoveSucceededMom.setStatus("current")
_DynamicnetobjectRemoveSucceededMax_Type = CounterBasedGauge64
_DynamicnetobjectRemoveSucceededMax_Object = MibScalar
dynamicnetobjectRemoveSucceededMax = _DynamicnetobjectRemoveSucceededMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 121, 3, 3),
    _DynamicnetobjectRemoveSucceededMax_Type()
)
dynamicnetobjectRemoveSucceededMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dynamicnetobjectRemoveSucceededMax.setStatus("current")
_DynamicnetobjectRemoveFailed_ObjectIdentity = ObjectIdentity
dynamicnetobjectRemoveFailed = _DynamicnetobjectRemoveFailed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 121, 4)
)
_DynamicnetobjectRemoveFailedVal_Type = Counter64
_DynamicnetobjectRemoveFailedVal_Object = MibScalar
dynamicnetobjectRemoveFailedVal = _DynamicnetobjectRemoveFailedVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 121, 4, 1),
    _DynamicnetobjectRemoveFailedVal_Type()
)
dynamicnetobjectRemoveFailedVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dynamicnetobjectRemoveFailedVal.setStatus("current")
_DynamicnetobjectRemoveFailedMom_Type = CounterBasedGauge64
_DynamicnetobjectRemoveFailedMom_Object = MibScalar
dynamicnetobjectRemoveFailedMom = _DynamicnetobjectRemoveFailedMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 121, 4, 2),
    _DynamicnetobjectRemoveFailedMom_Type()
)
dynamicnetobjectRemoveFailedMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dynamicnetobjectRemoveFailedMom.setStatus("current")
_DynamicnetobjectRemoveFailedMax_Type = CounterBasedGauge64
_DynamicnetobjectRemoveFailedMax_Object = MibScalar
dynamicnetobjectRemoveFailedMax = _DynamicnetobjectRemoveFailedMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 121, 4, 3),
    _DynamicnetobjectRemoveFailedMax_Type()
)
dynamicnetobjectRemoveFailedMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dynamicnetobjectRemoveFailedMax.setStatus("current")
_DynamicnetobjectCurrentIpCount_ObjectIdentity = ObjectIdentity
dynamicnetobjectCurrentIpCount = _DynamicnetobjectCurrentIpCount_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 121, 5)
)
_DynamicnetobjectCurrentIpCountVal_Type = CounterBasedGauge64
_DynamicnetobjectCurrentIpCountVal_Object = MibScalar
dynamicnetobjectCurrentIpCountVal = _DynamicnetobjectCurrentIpCountVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 121, 5, 1),
    _DynamicnetobjectCurrentIpCountVal_Type()
)
dynamicnetobjectCurrentIpCountVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dynamicnetobjectCurrentIpCountVal.setStatus("current")
_DynamicnetobjectCurrentIpCountMax_Type = CounterBasedGauge64
_DynamicnetobjectCurrentIpCountMax_Object = MibScalar
dynamicnetobjectCurrentIpCountMax = _DynamicnetobjectCurrentIpCountMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 121, 5, 3),
    _DynamicnetobjectCurrentIpCountMax_Type()
)
dynamicnetobjectCurrentIpCountMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dynamicnetobjectCurrentIpCountMax.setStatus("current")
_DynamicnetobjectCurrentCount_ObjectIdentity = ObjectIdentity
dynamicnetobjectCurrentCount = _DynamicnetobjectCurrentCount_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 121, 6)
)
_DynamicnetobjectCurrentCountVal_Type = CounterBasedGauge64
_DynamicnetobjectCurrentCountVal_Object = MibScalar
dynamicnetobjectCurrentCountVal = _DynamicnetobjectCurrentCountVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 121, 6, 1),
    _DynamicnetobjectCurrentCountVal_Type()
)
dynamicnetobjectCurrentCountVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dynamicnetobjectCurrentCountVal.setStatus("current")
_DynamicnetobjectCurrentCountMax_Type = CounterBasedGauge64
_DynamicnetobjectCurrentCountMax_Object = MibScalar
dynamicnetobjectCurrentCountMax = _DynamicnetobjectCurrentCountMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 121, 6, 3),
    _DynamicnetobjectCurrentCountMax_Type()
)
dynamicnetobjectCurrentCountMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dynamicnetobjectCurrentCountMax.setStatus("current")
_DynamicnetobjectAddSucceeded_ObjectIdentity = ObjectIdentity
dynamicnetobjectAddSucceeded = _DynamicnetobjectAddSucceeded_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 121, 8)
)
_DynamicnetobjectAddSucceededVal_Type = Counter64
_DynamicnetobjectAddSucceededVal_Object = MibScalar
dynamicnetobjectAddSucceededVal = _DynamicnetobjectAddSucceededVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 121, 8, 1),
    _DynamicnetobjectAddSucceededVal_Type()
)
dynamicnetobjectAddSucceededVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dynamicnetobjectAddSucceededVal.setStatus("current")
_DynamicnetobjectAddSucceededMom_Type = CounterBasedGauge64
_DynamicnetobjectAddSucceededMom_Object = MibScalar
dynamicnetobjectAddSucceededMom = _DynamicnetobjectAddSucceededMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 121, 8, 2),
    _DynamicnetobjectAddSucceededMom_Type()
)
dynamicnetobjectAddSucceededMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dynamicnetobjectAddSucceededMom.setStatus("current")
_DynamicnetobjectAddSucceededMax_Type = CounterBasedGauge64
_DynamicnetobjectAddSucceededMax_Object = MibScalar
dynamicnetobjectAddSucceededMax = _DynamicnetobjectAddSucceededMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 121, 8, 3),
    _DynamicnetobjectAddSucceededMax_Type()
)
dynamicnetobjectAddSucceededMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dynamicnetobjectAddSucceededMax.setStatus("current")
_DynamicnetobjectAddFailed_ObjectIdentity = ObjectIdentity
dynamicnetobjectAddFailed = _DynamicnetobjectAddFailed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 121, 9)
)
_DynamicnetobjectAddFailedVal_Type = Counter64
_DynamicnetobjectAddFailedVal_Object = MibScalar
dynamicnetobjectAddFailedVal = _DynamicnetobjectAddFailedVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 121, 9, 1),
    _DynamicnetobjectAddFailedVal_Type()
)
dynamicnetobjectAddFailedVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dynamicnetobjectAddFailedVal.setStatus("current")
_DynamicnetobjectAddFailedMom_Type = CounterBasedGauge64
_DynamicnetobjectAddFailedMom_Object = MibScalar
dynamicnetobjectAddFailedMom = _DynamicnetobjectAddFailedMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 121, 9, 2),
    _DynamicnetobjectAddFailedMom_Type()
)
dynamicnetobjectAddFailedMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dynamicnetobjectAddFailedMom.setStatus("current")
_DynamicnetobjectAddFailedMax_Type = CounterBasedGauge64
_DynamicnetobjectAddFailedMax_Object = MibScalar
dynamicnetobjectAddFailedMax = _DynamicnetobjectAddFailedMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 121, 9, 3),
    _DynamicnetobjectAddFailedMax_Type()
)
dynamicnetobjectAddFailedMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dynamicnetobjectAddFailedMax.setStatus("current")
_DynamicnetobjectInsertPldbFailed_ObjectIdentity = ObjectIdentity
dynamicnetobjectInsertPldbFailed = _DynamicnetobjectInsertPldbFailed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 121, 10)
)
_DynamicnetobjectInsertPldbFailedVal_Type = Counter64
_DynamicnetobjectInsertPldbFailedVal_Object = MibScalar
dynamicnetobjectInsertPldbFailedVal = _DynamicnetobjectInsertPldbFailedVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 121, 10, 1),
    _DynamicnetobjectInsertPldbFailedVal_Type()
)
dynamicnetobjectInsertPldbFailedVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dynamicnetobjectInsertPldbFailedVal.setStatus("current")
_DynamicnetobjectInsertPldbFailedMom_Type = CounterBasedGauge64
_DynamicnetobjectInsertPldbFailedMom_Object = MibScalar
dynamicnetobjectInsertPldbFailedMom = _DynamicnetobjectInsertPldbFailedMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 121, 10, 2),
    _DynamicnetobjectInsertPldbFailedMom_Type()
)
dynamicnetobjectInsertPldbFailedMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dynamicnetobjectInsertPldbFailedMom.setStatus("current")
_DynamicnetobjectInsertPldbFailedMax_Type = CounterBasedGauge64
_DynamicnetobjectInsertPldbFailedMax_Object = MibScalar
dynamicnetobjectInsertPldbFailedMax = _DynamicnetobjectInsertPldbFailedMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 121, 10, 3),
    _DynamicnetobjectInsertPldbFailedMax_Type()
)
dynamicnetobjectInsertPldbFailedMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dynamicnetobjectInsertPldbFailedMax.setStatus("current")
_DynamicnetobjectAddCalls_ObjectIdentity = ObjectIdentity
dynamicnetobjectAddCalls = _DynamicnetobjectAddCalls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 121, 11)
)
_DynamicnetobjectAddCallsVal_Type = Counter64
_DynamicnetobjectAddCallsVal_Object = MibScalar
dynamicnetobjectAddCallsVal = _DynamicnetobjectAddCallsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 121, 11, 1),
    _DynamicnetobjectAddCallsVal_Type()
)
dynamicnetobjectAddCallsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dynamicnetobjectAddCallsVal.setStatus("current")
_DynamicnetobjectAddCallsMom_Type = CounterBasedGauge64
_DynamicnetobjectAddCallsMom_Object = MibScalar
dynamicnetobjectAddCallsMom = _DynamicnetobjectAddCallsMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 121, 11, 2),
    _DynamicnetobjectAddCallsMom_Type()
)
dynamicnetobjectAddCallsMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dynamicnetobjectAddCallsMom.setStatus("current")
_DynamicnetobjectAddCallsMax_Type = CounterBasedGauge64
_DynamicnetobjectAddCallsMax_Object = MibScalar
dynamicnetobjectAddCallsMax = _DynamicnetobjectAddCallsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 121, 11, 3),
    _DynamicnetobjectAddCallsMax_Type()
)
dynamicnetobjectAddCallsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dynamicnetobjectAddCallsMax.setStatus("current")
_DynamicnetobjectRemoveCalls_ObjectIdentity = ObjectIdentity
dynamicnetobjectRemoveCalls = _DynamicnetobjectRemoveCalls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 121, 12)
)
_DynamicnetobjectRemoveCallsVal_Type = Counter64
_DynamicnetobjectRemoveCallsVal_Object = MibScalar
dynamicnetobjectRemoveCallsVal = _DynamicnetobjectRemoveCallsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 121, 12, 1),
    _DynamicnetobjectRemoveCallsVal_Type()
)
dynamicnetobjectRemoveCallsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dynamicnetobjectRemoveCallsVal.setStatus("current")
_DynamicnetobjectRemoveCallsMom_Type = CounterBasedGauge64
_DynamicnetobjectRemoveCallsMom_Object = MibScalar
dynamicnetobjectRemoveCallsMom = _DynamicnetobjectRemoveCallsMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 121, 12, 2),
    _DynamicnetobjectRemoveCallsMom_Type()
)
dynamicnetobjectRemoveCallsMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dynamicnetobjectRemoveCallsMom.setStatus("current")
_DynamicnetobjectRemoveCallsMax_Type = CounterBasedGauge64
_DynamicnetobjectRemoveCallsMax_Object = MibScalar
dynamicnetobjectRemoveCallsMax = _DynamicnetobjectRemoveCallsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 121, 12, 3),
    _DynamicnetobjectRemoveCallsMax_Type()
)
dynamicnetobjectRemoveCallsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dynamicnetobjectRemoveCallsMax.setStatus("current")
_DynamicnetobjectListCalls_ObjectIdentity = ObjectIdentity
dynamicnetobjectListCalls = _DynamicnetobjectListCalls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 121, 15)
)
_DynamicnetobjectListCallsVal_Type = Counter64
_DynamicnetobjectListCallsVal_Object = MibScalar
dynamicnetobjectListCallsVal = _DynamicnetobjectListCallsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 121, 15, 1),
    _DynamicnetobjectListCallsVal_Type()
)
dynamicnetobjectListCallsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dynamicnetobjectListCallsVal.setStatus("current")
_DynamicnetobjectListCallsMom_Type = CounterBasedGauge64
_DynamicnetobjectListCallsMom_Object = MibScalar
dynamicnetobjectListCallsMom = _DynamicnetobjectListCallsMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 121, 15, 2),
    _DynamicnetobjectListCallsMom_Type()
)
dynamicnetobjectListCallsMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dynamicnetobjectListCallsMom.setStatus("current")
_DynamicnetobjectListCallsMax_Type = CounterBasedGauge64
_DynamicnetobjectListCallsMax_Object = MibScalar
dynamicnetobjectListCallsMax = _DynamicnetobjectListCallsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 121, 15, 3),
    _DynamicnetobjectListCallsMax_Type()
)
dynamicnetobjectListCallsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dynamicnetobjectListCallsMax.setStatus("current")
_DynamicnetobjectListItemsReturned_ObjectIdentity = ObjectIdentity
dynamicnetobjectListItemsReturned = _DynamicnetobjectListItemsReturned_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 121, 16)
)
_DynamicnetobjectListItemsReturnedVal_Type = Counter64
_DynamicnetobjectListItemsReturnedVal_Object = MibScalar
dynamicnetobjectListItemsReturnedVal = _DynamicnetobjectListItemsReturnedVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 121, 16, 1),
    _DynamicnetobjectListItemsReturnedVal_Type()
)
dynamicnetobjectListItemsReturnedVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dynamicnetobjectListItemsReturnedVal.setStatus("current")
_DynamicnetobjectListItemsReturnedMom_Type = CounterBasedGauge64
_DynamicnetobjectListItemsReturnedMom_Object = MibScalar
dynamicnetobjectListItemsReturnedMom = _DynamicnetobjectListItemsReturnedMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 121, 16, 2),
    _DynamicnetobjectListItemsReturnedMom_Type()
)
dynamicnetobjectListItemsReturnedMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dynamicnetobjectListItemsReturnedMom.setStatus("current")
_DynamicnetobjectListItemsReturnedMax_Type = CounterBasedGauge64
_DynamicnetobjectListItemsReturnedMax_Object = MibScalar
dynamicnetobjectListItemsReturnedMax = _DynamicnetobjectListItemsReturnedMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 121, 16, 3),
    _DynamicnetobjectListItemsReturnedMax_Type()
)
dynamicnetobjectListItemsReturnedMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dynamicnetobjectListItemsReturnedMax.setStatus("current")
_DynamicnetobjectSubscriberConflicts_ObjectIdentity = ObjectIdentity
dynamicnetobjectSubscriberConflicts = _DynamicnetobjectSubscriberConflicts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 121, 17)
)
_DynamicnetobjectSubscriberConflictsVal_Type = Counter64
_DynamicnetobjectSubscriberConflictsVal_Object = MibScalar
dynamicnetobjectSubscriberConflictsVal = _DynamicnetobjectSubscriberConflictsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 121, 17, 1),
    _DynamicnetobjectSubscriberConflictsVal_Type()
)
dynamicnetobjectSubscriberConflictsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dynamicnetobjectSubscriberConflictsVal.setStatus("current")
_DynamicnetobjectSubscriberConflictsMom_Type = CounterBasedGauge64
_DynamicnetobjectSubscriberConflictsMom_Object = MibScalar
dynamicnetobjectSubscriberConflictsMom = _DynamicnetobjectSubscriberConflictsMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 121, 17, 2),
    _DynamicnetobjectSubscriberConflictsMom_Type()
)
dynamicnetobjectSubscriberConflictsMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dynamicnetobjectSubscriberConflictsMom.setStatus("current")
_DynamicnetobjectSubscriberConflictsMax_Type = CounterBasedGauge64
_DynamicnetobjectSubscriberConflictsMax_Object = MibScalar
dynamicnetobjectSubscriberConflictsMax = _DynamicnetobjectSubscriberConflictsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 121, 17, 3),
    _DynamicnetobjectSubscriberConflictsMax_Type()
)
dynamicnetobjectSubscriberConflictsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dynamicnetobjectSubscriberConflictsMax.setStatus("current")
_DynamicnetobjectSubscriberCount_ObjectIdentity = ObjectIdentity
dynamicnetobjectSubscriberCount = _DynamicnetobjectSubscriberCount_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 121, 18)
)
_DynamicnetobjectSubscriberCountVal_Type = CounterBasedGauge64
_DynamicnetobjectSubscriberCountVal_Object = MibScalar
dynamicnetobjectSubscriberCountVal = _DynamicnetobjectSubscriberCountVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 121, 18, 1),
    _DynamicnetobjectSubscriberCountVal_Type()
)
dynamicnetobjectSubscriberCountVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dynamicnetobjectSubscriberCountVal.setStatus("current")
_DynamicnetobjectSubscriberCountMax_Type = CounterBasedGauge64
_DynamicnetobjectSubscriberCountMax_Object = MibScalar
dynamicnetobjectSubscriberCountMax = _DynamicnetobjectSubscriberCountMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 121, 18, 3),
    _DynamicnetobjectSubscriberCountMax_Type()
)
dynamicnetobjectSubscriberCountMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dynamicnetobjectSubscriberCountMax.setStatus("current")
_DynamicnetobjectSubscriberTooMany_ObjectIdentity = ObjectIdentity
dynamicnetobjectSubscriberTooMany = _DynamicnetobjectSubscriberTooMany_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 121, 19)
)
_DynamicnetobjectSubscriberTooManyVal_Type = Counter64
_DynamicnetobjectSubscriberTooManyVal_Object = MibScalar
dynamicnetobjectSubscriberTooManyVal = _DynamicnetobjectSubscriberTooManyVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 121, 19, 1),
    _DynamicnetobjectSubscriberTooManyVal_Type()
)
dynamicnetobjectSubscriberTooManyVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dynamicnetobjectSubscriberTooManyVal.setStatus("current")
_DynamicnetobjectSubscriberTooManyMom_Type = CounterBasedGauge64
_DynamicnetobjectSubscriberTooManyMom_Object = MibScalar
dynamicnetobjectSubscriberTooManyMom = _DynamicnetobjectSubscriberTooManyMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 121, 19, 2),
    _DynamicnetobjectSubscriberTooManyMom_Type()
)
dynamicnetobjectSubscriberTooManyMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dynamicnetobjectSubscriberTooManyMom.setStatus("current")
_DynamicnetobjectSubscriberTooManyMax_Type = CounterBasedGauge64
_DynamicnetobjectSubscriberTooManyMax_Object = MibScalar
dynamicnetobjectSubscriberTooManyMax = _DynamicnetobjectSubscriberTooManyMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 121, 19, 3),
    _DynamicnetobjectSubscriberTooManyMax_Type()
)
dynamicnetobjectSubscriberTooManyMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dynamicnetobjectSubscriberTooManyMax.setStatus("current")
_DynamicnetobjectSqliteMemoryUsed_ObjectIdentity = ObjectIdentity
dynamicnetobjectSqliteMemoryUsed = _DynamicnetobjectSqliteMemoryUsed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 121, 20)
)
_DynamicnetobjectSqliteMemoryUsedVal_Type = CounterBasedGauge64
_DynamicnetobjectSqliteMemoryUsedVal_Object = MibScalar
dynamicnetobjectSqliteMemoryUsedVal = _DynamicnetobjectSqliteMemoryUsedVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 121, 20, 1),
    _DynamicnetobjectSqliteMemoryUsedVal_Type()
)
dynamicnetobjectSqliteMemoryUsedVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dynamicnetobjectSqliteMemoryUsedVal.setStatus("obsolete")
_DynamicnetobjectSqliteMemoryUsedMax_Type = CounterBasedGauge64
_DynamicnetobjectSqliteMemoryUsedMax_Object = MibScalar
dynamicnetobjectSqliteMemoryUsedMax = _DynamicnetobjectSqliteMemoryUsedMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 121, 20, 3),
    _DynamicnetobjectSqliteMemoryUsedMax_Type()
)
dynamicnetobjectSqliteMemoryUsedMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dynamicnetobjectSqliteMemoryUsedMax.setStatus("obsolete")
_DynamicnetobjectPendingAdds_ObjectIdentity = ObjectIdentity
dynamicnetobjectPendingAdds = _DynamicnetobjectPendingAdds_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 121, 21)
)
_DynamicnetobjectPendingAddsVal_Type = CounterBasedGauge64
_DynamicnetobjectPendingAddsVal_Object = MibScalar
dynamicnetobjectPendingAddsVal = _DynamicnetobjectPendingAddsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 121, 21, 1),
    _DynamicnetobjectPendingAddsVal_Type()
)
dynamicnetobjectPendingAddsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dynamicnetobjectPendingAddsVal.setStatus("obsolete")
_DynamicnetobjectPendingAddsMax_Type = CounterBasedGauge64
_DynamicnetobjectPendingAddsMax_Object = MibScalar
dynamicnetobjectPendingAddsMax = _DynamicnetobjectPendingAddsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 121, 21, 3),
    _DynamicnetobjectPendingAddsMax_Type()
)
dynamicnetobjectPendingAddsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dynamicnetobjectPendingAddsMax.setStatus("obsolete")
_Bgp_ObjectIdentity = ObjectIdentity
bgp = _Bgp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 122)
)
_BgpUpdates_ObjectIdentity = ObjectIdentity
bgpUpdates = _BgpUpdates_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 122, 1)
)
_BgpUpdatesVal_Type = CounterBasedGauge64
_BgpUpdatesVal_Object = MibScalar
bgpUpdatesVal = _BgpUpdatesVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 122, 1, 1),
    _BgpUpdatesVal_Type()
)
bgpUpdatesVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpUpdatesVal.setStatus("current")
_BgpUpdatesMax_Type = CounterBasedGauge64
_BgpUpdatesMax_Object = MibScalar
bgpUpdatesMax = _BgpUpdatesMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 122, 1, 3),
    _BgpUpdatesMax_Type()
)
bgpUpdatesMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpUpdatesMax.setStatus("current")
_BgpPrefixes_ObjectIdentity = ObjectIdentity
bgpPrefixes = _BgpPrefixes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 122, 2)
)
_BgpPrefixesVal_Type = CounterBasedGauge64
_BgpPrefixesVal_Object = MibScalar
bgpPrefixesVal = _BgpPrefixesVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 122, 2, 1),
    _BgpPrefixesVal_Type()
)
bgpPrefixesVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPrefixesVal.setStatus("current")
_BgpPrefixesMax_Type = CounterBasedGauge64
_BgpPrefixesMax_Object = MibScalar
bgpPrefixesMax = _BgpPrefixesMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 122, 2, 3),
    _BgpPrefixesMax_Type()
)
bgpPrefixesMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPrefixesMax.setStatus("current")
_BgpPaths_ObjectIdentity = ObjectIdentity
bgpPaths = _BgpPaths_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 122, 3)
)
_BgpPathsVal_Type = CounterBasedGauge64
_BgpPathsVal_Object = MibScalar
bgpPathsVal = _BgpPathsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 122, 3, 1),
    _BgpPathsVal_Type()
)
bgpPathsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPathsVal.setStatus("current")
_BgpPathsMax_Type = CounterBasedGauge64
_BgpPathsMax_Object = MibScalar
bgpPathsMax = _BgpPathsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 122, 3, 3),
    _BgpPathsMax_Type()
)
bgpPathsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPathsMax.setStatus("current")
_BgpUptime_ObjectIdentity = ObjectIdentity
bgpUptime = _BgpUptime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 122, 4)
)
_BgpUptimeVal_Type = TimeTicks
_BgpUptimeVal_Object = MibScalar
bgpUptimeVal = _BgpUptimeVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 122, 4, 1),
    _BgpUptimeVal_Type()
)
bgpUptimeVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpUptimeVal.setStatus("current")
_BgpConvresionTime_ObjectIdentity = ObjectIdentity
bgpConvresionTime = _BgpConvresionTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 122, 5)
)
_BgpConvresionTimeVal_Type = CounterBasedGauge64
_BgpConvresionTimeVal_Object = MibScalar
bgpConvresionTimeVal = _BgpConvresionTimeVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 122, 5, 1),
    _BgpConvresionTimeVal_Type()
)
bgpConvresionTimeVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpConvresionTimeVal.setStatus("current")
_BgpConvresionTimeMax_Type = CounterBasedGauge64
_BgpConvresionTimeMax_Object = MibScalar
bgpConvresionTimeMax = _BgpConvresionTimeMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 122, 5, 3),
    _BgpConvresionTimeMax_Type()
)
bgpConvresionTimeMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpConvresionTimeMax.setStatus("current")
_BgpSendTime_ObjectIdentity = ObjectIdentity
bgpSendTime = _BgpSendTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 122, 6)
)
_BgpSendTimeVal_Type = CounterBasedGauge64
_BgpSendTimeVal_Object = MibScalar
bgpSendTimeVal = _BgpSendTimeVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 122, 6, 1),
    _BgpSendTimeVal_Type()
)
bgpSendTimeVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpSendTimeVal.setStatus("current")
_BgpSendTimeMax_Type = CounterBasedGauge64
_BgpSendTimeMax_Object = MibScalar
bgpSendTimeMax = _BgpSendTimeMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 122, 6, 3),
    _BgpSendTimeMax_Type()
)
bgpSendTimeMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpSendTimeMax.setStatus("current")
_BgpReplaces_ObjectIdentity = ObjectIdentity
bgpReplaces = _BgpReplaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 122, 7)
)
_BgpReplacesVal_Type = CounterBasedGauge64
_BgpReplacesVal_Object = MibScalar
bgpReplacesVal = _BgpReplacesVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 122, 7, 1),
    _BgpReplacesVal_Type()
)
bgpReplacesVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpReplacesVal.setStatus("current")
_BgpReplacesMax_Type = CounterBasedGauge64
_BgpReplacesMax_Object = MibScalar
bgpReplacesMax = _BgpReplacesMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 122, 7, 3),
    _BgpReplacesMax_Type()
)
bgpReplacesMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpReplacesMax.setStatus("current")
_BgpWithdraws_ObjectIdentity = ObjectIdentity
bgpWithdraws = _BgpWithdraws_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 122, 8)
)
_BgpWithdrawsVal_Type = CounterBasedGauge64
_BgpWithdrawsVal_Object = MibScalar
bgpWithdrawsVal = _BgpWithdrawsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 122, 8, 1),
    _BgpWithdrawsVal_Type()
)
bgpWithdrawsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpWithdrawsVal.setStatus("current")
_BgpWithdrawsMax_Type = CounterBasedGauge64
_BgpWithdrawsMax_Object = MibScalar
bgpWithdrawsMax = _BgpWithdrawsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 122, 8, 3),
    _BgpWithdrawsMax_Type()
)
bgpWithdrawsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpWithdrawsMax.setStatus("current")
_BgpAnnounces_ObjectIdentity = ObjectIdentity
bgpAnnounces = _BgpAnnounces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 122, 9)
)
_BgpAnnouncesVal_Type = CounterBasedGauge64
_BgpAnnouncesVal_Object = MibScalar
bgpAnnouncesVal = _BgpAnnouncesVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 122, 9, 1),
    _BgpAnnouncesVal_Type()
)
bgpAnnouncesVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpAnnouncesVal.setStatus("current")
_BgpAnnouncesMax_Type = CounterBasedGauge64
_BgpAnnouncesMax_Object = MibScalar
bgpAnnouncesMax = _BgpAnnouncesMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 122, 9, 3),
    _BgpAnnouncesMax_Type()
)
bgpAnnouncesMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpAnnouncesMax.setStatus("current")
_BgpReconnects_ObjectIdentity = ObjectIdentity
bgpReconnects = _BgpReconnects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 122, 10)
)
_BgpReconnectsVal_Type = CounterBasedGauge64
_BgpReconnectsVal_Object = MibScalar
bgpReconnectsVal = _BgpReconnectsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 122, 10, 1),
    _BgpReconnectsVal_Type()
)
bgpReconnectsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpReconnectsVal.setStatus("current")
_BgpReconnectsMax_Type = CounterBasedGauge64
_BgpReconnectsMax_Object = MibScalar
bgpReconnectsMax = _BgpReconnectsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 122, 10, 3),
    _BgpReconnectsMax_Type()
)
bgpReconnectsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpReconnectsMax.setStatus("current")
_BgpRecyclePaths_ObjectIdentity = ObjectIdentity
bgpRecyclePaths = _BgpRecyclePaths_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 122, 12)
)
_BgpRecyclePathsVal_Type = CounterBasedGauge64
_BgpRecyclePathsVal_Object = MibScalar
bgpRecyclePathsVal = _BgpRecyclePathsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 122, 12, 1),
    _BgpRecyclePathsVal_Type()
)
bgpRecyclePathsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpRecyclePathsVal.setStatus("current")
_BgpRecyclePathsMax_Type = CounterBasedGauge64
_BgpRecyclePathsMax_Object = MibScalar
bgpRecyclePathsMax = _BgpRecyclePathsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 122, 12, 3),
    _BgpRecyclePathsMax_Type()
)
bgpRecyclePathsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpRecyclePathsMax.setStatus("current")
_BgpFreelistPaths_ObjectIdentity = ObjectIdentity
bgpFreelistPaths = _BgpFreelistPaths_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 122, 13)
)
_BgpFreelistPathsVal_Type = CounterBasedGauge64
_BgpFreelistPathsVal_Object = MibScalar
bgpFreelistPathsVal = _BgpFreelistPathsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 122, 13, 1),
    _BgpFreelistPathsVal_Type()
)
bgpFreelistPathsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpFreelistPathsVal.setStatus("current")
_BgpFreelistPathsMax_Type = CounterBasedGauge64
_BgpFreelistPathsMax_Object = MibScalar
bgpFreelistPathsMax = _BgpFreelistPathsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 122, 13, 3),
    _BgpFreelistPathsMax_Type()
)
bgpFreelistPathsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpFreelistPathsMax.setStatus("current")
_BgpBalanceTime_ObjectIdentity = ObjectIdentity
bgpBalanceTime = _BgpBalanceTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 122, 14)
)
_BgpBalanceTimeVal_Type = CounterBasedGauge64
_BgpBalanceTimeVal_Object = MibScalar
bgpBalanceTimeVal = _BgpBalanceTimeVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 122, 14, 1),
    _BgpBalanceTimeVal_Type()
)
bgpBalanceTimeVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpBalanceTimeVal.setStatus("current")
_BgpBalanceTimeMax_Type = CounterBasedGauge64
_BgpBalanceTimeMax_Object = MibScalar
bgpBalanceTimeMax = _BgpBalanceTimeMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 122, 14, 3),
    _BgpBalanceTimeMax_Type()
)
bgpBalanceTimeMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpBalanceTimeMax.setStatus("current")
_BgpCommunityTooSmall_ObjectIdentity = ObjectIdentity
bgpCommunityTooSmall = _BgpCommunityTooSmall_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 122, 24)
)
_BgpCommunityTooSmallVal_Type = CounterBasedGauge64
_BgpCommunityTooSmallVal_Object = MibScalar
bgpCommunityTooSmallVal = _BgpCommunityTooSmallVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 122, 24, 1),
    _BgpCommunityTooSmallVal_Type()
)
bgpCommunityTooSmallVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpCommunityTooSmallVal.setStatus("current")
_BgpCommunityTooSmallMax_Type = CounterBasedGauge64
_BgpCommunityTooSmallMax_Object = MibScalar
bgpCommunityTooSmallMax = _BgpCommunityTooSmallMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 122, 24, 3),
    _BgpCommunityTooSmallMax_Type()
)
bgpCommunityTooSmallMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpCommunityTooSmallMax.setStatus("current")
_BgpCommunityMaxSeen_ObjectIdentity = ObjectIdentity
bgpCommunityMaxSeen = _BgpCommunityMaxSeen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 122, 25)
)
_BgpCommunityMaxSeenVal_Type = CounterBasedGauge64
_BgpCommunityMaxSeenVal_Object = MibScalar
bgpCommunityMaxSeenVal = _BgpCommunityMaxSeenVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 122, 25, 1),
    _BgpCommunityMaxSeenVal_Type()
)
bgpCommunityMaxSeenVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpCommunityMaxSeenVal.setStatus("current")
_BgpCommunityMaxSeenMax_Type = CounterBasedGauge64
_BgpCommunityMaxSeenMax_Object = MibScalar
bgpCommunityMaxSeenMax = _BgpCommunityMaxSeenMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 122, 25, 3),
    _BgpCommunityMaxSeenMax_Type()
)
bgpCommunityMaxSeenMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpCommunityMaxSeenMax.setStatus("current")
_Qsync_ObjectIdentity = ObjectIdentity
qsync = _Qsync_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 123)
)
_QsyncIUpdates_ObjectIdentity = ObjectIdentity
qsyncIUpdates = _QsyncIUpdates_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 123, 1)
)
_QsyncIUpdatesVal_Type = Counter64
_QsyncIUpdatesVal_Object = MibScalar
qsyncIUpdatesVal = _QsyncIUpdatesVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 123, 1, 1),
    _QsyncIUpdatesVal_Type()
)
qsyncIUpdatesVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qsyncIUpdatesVal.setStatus("current")
_QsyncIUpdatesMom_Type = CounterBasedGauge64
_QsyncIUpdatesMom_Object = MibScalar
qsyncIUpdatesMom = _QsyncIUpdatesMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 123, 1, 2),
    _QsyncIUpdatesMom_Type()
)
qsyncIUpdatesMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qsyncIUpdatesMom.setStatus("current")
_QsyncIUpdatesMax_Type = CounterBasedGauge64
_QsyncIUpdatesMax_Object = MibScalar
qsyncIUpdatesMax = _QsyncIUpdatesMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 123, 1, 3),
    _QsyncIUpdatesMax_Type()
)
qsyncIUpdatesMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qsyncIUpdatesMax.setStatus("current")
_QsyncIUpdatesOldRuleset_ObjectIdentity = ObjectIdentity
qsyncIUpdatesOldRuleset = _QsyncIUpdatesOldRuleset_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 123, 2)
)
_QsyncIUpdatesOldRulesetVal_Type = Counter64
_QsyncIUpdatesOldRulesetVal_Object = MibScalar
qsyncIUpdatesOldRulesetVal = _QsyncIUpdatesOldRulesetVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 123, 2, 1),
    _QsyncIUpdatesOldRulesetVal_Type()
)
qsyncIUpdatesOldRulesetVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qsyncIUpdatesOldRulesetVal.setStatus("current")
_QsyncIUpdatesOldRulesetMom_Type = CounterBasedGauge64
_QsyncIUpdatesOldRulesetMom_Object = MibScalar
qsyncIUpdatesOldRulesetMom = _QsyncIUpdatesOldRulesetMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 123, 2, 2),
    _QsyncIUpdatesOldRulesetMom_Type()
)
qsyncIUpdatesOldRulesetMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qsyncIUpdatesOldRulesetMom.setStatus("current")
_QsyncIUpdatesOldRulesetMax_Type = CounterBasedGauge64
_QsyncIUpdatesOldRulesetMax_Object = MibScalar
qsyncIUpdatesOldRulesetMax = _QsyncIUpdatesOldRulesetMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 123, 2, 3),
    _QsyncIUpdatesOldRulesetMax_Type()
)
qsyncIUpdatesOldRulesetMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qsyncIUpdatesOldRulesetMax.setStatus("current")
_QsyncIUpdatesUnknownObject_ObjectIdentity = ObjectIdentity
qsyncIUpdatesUnknownObject = _QsyncIUpdatesUnknownObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 123, 3)
)
_QsyncIUpdatesUnknownObjectVal_Type = Counter64
_QsyncIUpdatesUnknownObjectVal_Object = MibScalar
qsyncIUpdatesUnknownObjectVal = _QsyncIUpdatesUnknownObjectVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 123, 3, 1),
    _QsyncIUpdatesUnknownObjectVal_Type()
)
qsyncIUpdatesUnknownObjectVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qsyncIUpdatesUnknownObjectVal.setStatus("current")
_QsyncIUpdatesUnknownObjectMom_Type = CounterBasedGauge64
_QsyncIUpdatesUnknownObjectMom_Object = MibScalar
qsyncIUpdatesUnknownObjectMom = _QsyncIUpdatesUnknownObjectMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 123, 3, 2),
    _QsyncIUpdatesUnknownObjectMom_Type()
)
qsyncIUpdatesUnknownObjectMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qsyncIUpdatesUnknownObjectMom.setStatus("current")
_QsyncIUpdatesUnknownObjectMax_Type = CounterBasedGauge64
_QsyncIUpdatesUnknownObjectMax_Object = MibScalar
qsyncIUpdatesUnknownObjectMax = _QsyncIUpdatesUnknownObjectMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 123, 3, 3),
    _QsyncIUpdatesUnknownObjectMax_Type()
)
qsyncIUpdatesUnknownObjectMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qsyncIUpdatesUnknownObjectMax.setStatus("current")
_QsyncIReaperSplitsCreated_ObjectIdentity = ObjectIdentity
qsyncIReaperSplitsCreated = _QsyncIReaperSplitsCreated_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 123, 4)
)
_QsyncIReaperSplitsCreatedVal_Type = Counter64
_QsyncIReaperSplitsCreatedVal_Object = MibScalar
qsyncIReaperSplitsCreatedVal = _QsyncIReaperSplitsCreatedVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 123, 4, 1),
    _QsyncIReaperSplitsCreatedVal_Type()
)
qsyncIReaperSplitsCreatedVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qsyncIReaperSplitsCreatedVal.setStatus("current")
_QsyncIReaperSplitsCreatedMom_Type = CounterBasedGauge64
_QsyncIReaperSplitsCreatedMom_Object = MibScalar
qsyncIReaperSplitsCreatedMom = _QsyncIReaperSplitsCreatedMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 123, 4, 2),
    _QsyncIReaperSplitsCreatedMom_Type()
)
qsyncIReaperSplitsCreatedMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qsyncIReaperSplitsCreatedMom.setStatus("current")
_QsyncIReaperSplitsCreatedMax_Type = CounterBasedGauge64
_QsyncIReaperSplitsCreatedMax_Object = MibScalar
qsyncIReaperSplitsCreatedMax = _QsyncIReaperSplitsCreatedMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 123, 4, 3),
    _QsyncIReaperSplitsCreatedMax_Type()
)
qsyncIReaperSplitsCreatedMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qsyncIReaperSplitsCreatedMax.setStatus("current")
_QsyncIReaperSplitsActive_ObjectIdentity = ObjectIdentity
qsyncIReaperSplitsActive = _QsyncIReaperSplitsActive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 123, 5)
)
_QsyncIReaperSplitsActiveVal_Type = CounterBasedGauge64
_QsyncIReaperSplitsActiveVal_Object = MibScalar
qsyncIReaperSplitsActiveVal = _QsyncIReaperSplitsActiveVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 123, 5, 1),
    _QsyncIReaperSplitsActiveVal_Type()
)
qsyncIReaperSplitsActiveVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qsyncIReaperSplitsActiveVal.setStatus("current")
_QsyncIReaperSplitsActiveMax_Type = CounterBasedGauge64
_QsyncIReaperSplitsActiveMax_Object = MibScalar
qsyncIReaperSplitsActiveMax = _QsyncIReaperSplitsActiveMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 123, 5, 3),
    _QsyncIReaperSplitsActiveMax_Type()
)
qsyncIReaperSplitsActiveMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qsyncIReaperSplitsActiveMax.setStatus("current")
_QsyncISumFreelistSize_ObjectIdentity = ObjectIdentity
qsyncISumFreelistSize = _QsyncISumFreelistSize_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 123, 6)
)
_QsyncISumFreelistSizeVal_Type = CounterBasedGauge64
_QsyncISumFreelistSizeVal_Object = MibScalar
qsyncISumFreelistSizeVal = _QsyncISumFreelistSizeVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 123, 6, 1),
    _QsyncISumFreelistSizeVal_Type()
)
qsyncISumFreelistSizeVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qsyncISumFreelistSizeVal.setStatus("current")
_QsyncISumFreelistSizeMax_Type = CounterBasedGauge64
_QsyncISumFreelistSizeMax_Object = MibScalar
qsyncISumFreelistSizeMax = _QsyncISumFreelistSizeMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 123, 6, 3),
    _QsyncISumFreelistSizeMax_Type()
)
qsyncISumFreelistSizeMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qsyncISumFreelistSizeMax.setStatus("current")
_QsyncISumSplitsActive_ObjectIdentity = ObjectIdentity
qsyncISumSplitsActive = _QsyncISumSplitsActive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 123, 7)
)
_QsyncISumSplitsActiveVal_Type = CounterBasedGauge64
_QsyncISumSplitsActiveVal_Object = MibScalar
qsyncISumSplitsActiveVal = _QsyncISumSplitsActiveVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 123, 7, 1),
    _QsyncISumSplitsActiveVal_Type()
)
qsyncISumSplitsActiveVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qsyncISumSplitsActiveVal.setStatus("current")
_QsyncISumSplitsActiveMax_Type = CounterBasedGauge64
_QsyncISumSplitsActiveMax_Object = MibScalar
qsyncISumSplitsActiveMax = _QsyncISumSplitsActiveMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 123, 7, 3),
    _QsyncISumSplitsActiveMax_Type()
)
qsyncISumSplitsActiveMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qsyncISumSplitsActiveMax.setStatus("current")
_QsyncIAdjustmentsSent_ObjectIdentity = ObjectIdentity
qsyncIAdjustmentsSent = _QsyncIAdjustmentsSent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 123, 8)
)
_QsyncIAdjustmentsSentVal_Type = Counter64
_QsyncIAdjustmentsSentVal_Object = MibScalar
qsyncIAdjustmentsSentVal = _QsyncIAdjustmentsSentVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 123, 8, 1),
    _QsyncIAdjustmentsSentVal_Type()
)
qsyncIAdjustmentsSentVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qsyncIAdjustmentsSentVal.setStatus("current")
_QsyncIAdjustmentsSentMom_Type = CounterBasedGauge64
_QsyncIAdjustmentsSentMom_Object = MibScalar
qsyncIAdjustmentsSentMom = _QsyncIAdjustmentsSentMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 123, 8, 2),
    _QsyncIAdjustmentsSentMom_Type()
)
qsyncIAdjustmentsSentMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qsyncIAdjustmentsSentMom.setStatus("current")
_QsyncIAdjustmentsSentMax_Type = CounterBasedGauge64
_QsyncIAdjustmentsSentMax_Object = MibScalar
qsyncIAdjustmentsSentMax = _QsyncIAdjustmentsSentMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 123, 8, 3),
    _QsyncIAdjustmentsSentMax_Type()
)
qsyncIAdjustmentsSentMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qsyncIAdjustmentsSentMax.setStatus("current")
_QsyncENumPeers_ObjectIdentity = ObjectIdentity
qsyncENumPeers = _QsyncENumPeers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 123, 9)
)
_QsyncENumPeersVal_Type = CounterBasedGauge64
_QsyncENumPeersVal_Object = MibScalar
qsyncENumPeersVal = _QsyncENumPeersVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 123, 9, 1),
    _QsyncENumPeersVal_Type()
)
qsyncENumPeersVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qsyncENumPeersVal.setStatus("current")
_QsyncENumPeersMax_Type = CounterBasedGauge64
_QsyncENumPeersMax_Object = MibScalar
qsyncENumPeersMax = _QsyncENumPeersMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 123, 9, 3),
    _QsyncENumPeersMax_Type()
)
qsyncENumPeersMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qsyncENumPeersMax.setStatus("current")
_QsyncEUpdatesMismatch_ObjectIdentity = ObjectIdentity
qsyncEUpdatesMismatch = _QsyncEUpdatesMismatch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 123, 10)
)
_QsyncEUpdatesMismatchVal_Type = Counter64
_QsyncEUpdatesMismatchVal_Object = MibScalar
qsyncEUpdatesMismatchVal = _QsyncEUpdatesMismatchVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 123, 10, 1),
    _QsyncEUpdatesMismatchVal_Type()
)
qsyncEUpdatesMismatchVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qsyncEUpdatesMismatchVal.setStatus("current")
_QsyncEUpdatesMismatchMom_Type = CounterBasedGauge64
_QsyncEUpdatesMismatchMom_Object = MibScalar
qsyncEUpdatesMismatchMom = _QsyncEUpdatesMismatchMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 123, 10, 2),
    _QsyncEUpdatesMismatchMom_Type()
)
qsyncEUpdatesMismatchMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qsyncEUpdatesMismatchMom.setStatus("current")
_QsyncEUpdatesMismatchMax_Type = CounterBasedGauge64
_QsyncEUpdatesMismatchMax_Object = MibScalar
qsyncEUpdatesMismatchMax = _QsyncEUpdatesMismatchMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 123, 10, 3),
    _QsyncEUpdatesMismatchMax_Type()
)
qsyncEUpdatesMismatchMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qsyncEUpdatesMismatchMax.setStatus("current")
_QsyncEUpdatePackets_ObjectIdentity = ObjectIdentity
qsyncEUpdatePackets = _QsyncEUpdatePackets_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 123, 11)
)
_QsyncEUpdatePacketsVal_Type = Counter64
_QsyncEUpdatePacketsVal_Object = MibScalar
qsyncEUpdatePacketsVal = _QsyncEUpdatePacketsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 123, 11, 1),
    _QsyncEUpdatePacketsVal_Type()
)
qsyncEUpdatePacketsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qsyncEUpdatePacketsVal.setStatus("current")
_QsyncEUpdatePacketsMom_Type = CounterBasedGauge64
_QsyncEUpdatePacketsMom_Object = MibScalar
qsyncEUpdatePacketsMom = _QsyncEUpdatePacketsMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 123, 11, 2),
    _QsyncEUpdatePacketsMom_Type()
)
qsyncEUpdatePacketsMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qsyncEUpdatePacketsMom.setStatus("current")
_QsyncEUpdatePacketsMax_Type = CounterBasedGauge64
_QsyncEUpdatePacketsMax_Object = MibScalar
qsyncEUpdatePacketsMax = _QsyncEUpdatePacketsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 123, 11, 3),
    _QsyncEUpdatePacketsMax_Type()
)
qsyncEUpdatePacketsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qsyncEUpdatePacketsMax.setStatus("current")
_QsyncESplitTimeout_ObjectIdentity = ObjectIdentity
qsyncESplitTimeout = _QsyncESplitTimeout_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 123, 12)
)
_QsyncESplitTimeoutVal_Type = Counter64
_QsyncESplitTimeoutVal_Object = MibScalar
qsyncESplitTimeoutVal = _QsyncESplitTimeoutVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 123, 12, 1),
    _QsyncESplitTimeoutVal_Type()
)
qsyncESplitTimeoutVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qsyncESplitTimeoutVal.setStatus("current")
_QsyncESplitTimeoutMom_Type = CounterBasedGauge64
_QsyncESplitTimeoutMom_Object = MibScalar
qsyncESplitTimeoutMom = _QsyncESplitTimeoutMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 123, 12, 2),
    _QsyncESplitTimeoutMom_Type()
)
qsyncESplitTimeoutMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qsyncESplitTimeoutMom.setStatus("current")
_QsyncESplitTimeoutMax_Type = CounterBasedGauge64
_QsyncESplitTimeoutMax_Object = MibScalar
qsyncESplitTimeoutMax = _QsyncESplitTimeoutMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 123, 12, 3),
    _QsyncESplitTimeoutMax_Type()
)
qsyncESplitTimeoutMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qsyncESplitTimeoutMax.setStatus("current")
_QsyncERecvUpdateEntries_ObjectIdentity = ObjectIdentity
qsyncERecvUpdateEntries = _QsyncERecvUpdateEntries_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 123, 13)
)
_QsyncERecvUpdateEntriesVal_Type = Counter64
_QsyncERecvUpdateEntriesVal_Object = MibScalar
qsyncERecvUpdateEntriesVal = _QsyncERecvUpdateEntriesVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 123, 13, 1),
    _QsyncERecvUpdateEntriesVal_Type()
)
qsyncERecvUpdateEntriesVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qsyncERecvUpdateEntriesVal.setStatus("current")
_QsyncERecvUpdateEntriesMom_Type = CounterBasedGauge64
_QsyncERecvUpdateEntriesMom_Object = MibScalar
qsyncERecvUpdateEntriesMom = _QsyncERecvUpdateEntriesMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 123, 13, 2),
    _QsyncERecvUpdateEntriesMom_Type()
)
qsyncERecvUpdateEntriesMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qsyncERecvUpdateEntriesMom.setStatus("current")
_QsyncERecvUpdateEntriesMax_Type = CounterBasedGauge64
_QsyncERecvUpdateEntriesMax_Object = MibScalar
qsyncERecvUpdateEntriesMax = _QsyncERecvUpdateEntriesMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 123, 13, 3),
    _QsyncERecvUpdateEntriesMax_Type()
)
qsyncERecvUpdateEntriesMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qsyncERecvUpdateEntriesMax.setStatus("current")
_QsyncESendUpdateEntries_ObjectIdentity = ObjectIdentity
qsyncESendUpdateEntries = _QsyncESendUpdateEntries_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 123, 14)
)
_QsyncESendUpdateEntriesVal_Type = Counter64
_QsyncESendUpdateEntriesVal_Object = MibScalar
qsyncESendUpdateEntriesVal = _QsyncESendUpdateEntriesVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 123, 14, 1),
    _QsyncESendUpdateEntriesVal_Type()
)
qsyncESendUpdateEntriesVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qsyncESendUpdateEntriesVal.setStatus("current")
_QsyncESendUpdateEntriesMom_Type = CounterBasedGauge64
_QsyncESendUpdateEntriesMom_Object = MibScalar
qsyncESendUpdateEntriesMom = _QsyncESendUpdateEntriesMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 123, 14, 2),
    _QsyncESendUpdateEntriesMom_Type()
)
qsyncESendUpdateEntriesMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qsyncESendUpdateEntriesMom.setStatus("current")
_QsyncESendUpdateEntriesMax_Type = CounterBasedGauge64
_QsyncESendUpdateEntriesMax_Object = MibScalar
qsyncESendUpdateEntriesMax = _QsyncESendUpdateEntriesMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 123, 14, 3),
    _QsyncESendUpdateEntriesMax_Type()
)
qsyncESendUpdateEntriesMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qsyncESendUpdateEntriesMax.setStatus("current")
_QsyncESendUpdatePackets_ObjectIdentity = ObjectIdentity
qsyncESendUpdatePackets = _QsyncESendUpdatePackets_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 123, 15)
)
_QsyncESendUpdatePacketsVal_Type = Counter64
_QsyncESendUpdatePacketsVal_Object = MibScalar
qsyncESendUpdatePacketsVal = _QsyncESendUpdatePacketsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 123, 15, 1),
    _QsyncESendUpdatePacketsVal_Type()
)
qsyncESendUpdatePacketsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qsyncESendUpdatePacketsVal.setStatus("current")
_QsyncESendUpdatePacketsMom_Type = CounterBasedGauge64
_QsyncESendUpdatePacketsMom_Object = MibScalar
qsyncESendUpdatePacketsMom = _QsyncESendUpdatePacketsMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 123, 15, 2),
    _QsyncESendUpdatePacketsMom_Type()
)
qsyncESendUpdatePacketsMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qsyncESendUpdatePacketsMom.setStatus("current")
_QsyncESendUpdatePacketsMax_Type = CounterBasedGauge64
_QsyncESendUpdatePacketsMax_Object = MibScalar
qsyncESendUpdatePacketsMax = _QsyncESendUpdatePacketsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 123, 15, 3),
    _QsyncESendUpdatePacketsMax_Type()
)
qsyncESendUpdatePacketsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qsyncESendUpdatePacketsMax.setStatus("current")
_QsyncIUnsync_ObjectIdentity = ObjectIdentity
qsyncIUnsync = _QsyncIUnsync_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 123, 16)
)
_QsyncIUnsyncVal_Type = Counter64
_QsyncIUnsyncVal_Object = MibScalar
qsyncIUnsyncVal = _QsyncIUnsyncVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 123, 16, 1),
    _QsyncIUnsyncVal_Type()
)
qsyncIUnsyncVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qsyncIUnsyncVal.setStatus("current")
_QsyncIUnsyncMom_Type = CounterBasedGauge64
_QsyncIUnsyncMom_Object = MibScalar
qsyncIUnsyncMom = _QsyncIUnsyncMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 123, 16, 2),
    _QsyncIUnsyncMom_Type()
)
qsyncIUnsyncMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qsyncIUnsyncMom.setStatus("current")
_QsyncIUnsyncMax_Type = CounterBasedGauge64
_QsyncIUnsyncMax_Object = MibScalar
qsyncIUnsyncMax = _QsyncIUnsyncMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 123, 16, 3),
    _QsyncIUnsyncMax_Type()
)
qsyncIUnsyncMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qsyncIUnsyncMax.setStatus("current")
_QsyncESendbufFull_ObjectIdentity = ObjectIdentity
qsyncESendbufFull = _QsyncESendbufFull_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 123, 17)
)
_QsyncESendbufFullVal_Type = Counter64
_QsyncESendbufFullVal_Object = MibScalar
qsyncESendbufFullVal = _QsyncESendbufFullVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 123, 17, 1),
    _QsyncESendbufFullVal_Type()
)
qsyncESendbufFullVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qsyncESendbufFullVal.setStatus("current")
_QsyncESendbufFullMom_Type = CounterBasedGauge64
_QsyncESendbufFullMom_Object = MibScalar
qsyncESendbufFullMom = _QsyncESendbufFullMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 123, 17, 2),
    _QsyncESendbufFullMom_Type()
)
qsyncESendbufFullMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qsyncESendbufFullMom.setStatus("current")
_QsyncESendbufFullMax_Type = CounterBasedGauge64
_QsyncESendbufFullMax_Object = MibScalar
qsyncESendbufFullMax = _QsyncESendbufFullMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 123, 17, 3),
    _QsyncESendbufFullMax_Type()
)
qsyncESendbufFullMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qsyncESendbufFullMax.setStatus("current")
_QsyncESendbufUsage_ObjectIdentity = ObjectIdentity
qsyncESendbufUsage = _QsyncESendbufUsage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 123, 18)
)
_QsyncESendbufUsageVal_Type = CounterBasedGauge64
_QsyncESendbufUsageVal_Object = MibScalar
qsyncESendbufUsageVal = _QsyncESendbufUsageVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 123, 18, 1),
    _QsyncESendbufUsageVal_Type()
)
qsyncESendbufUsageVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qsyncESendbufUsageVal.setStatus("current")
_QsyncESendbufUsageMax_Type = CounterBasedGauge64
_QsyncESendbufUsageMax_Object = MibScalar
qsyncESendbufUsageMax = _QsyncESendbufUsageMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 123, 18, 3),
    _QsyncESendbufUsageMax_Type()
)
qsyncESendbufUsageMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qsyncESendbufUsageMax.setStatus("current")
_QsyncIIgnoredOOO_ObjectIdentity = ObjectIdentity
qsyncIIgnoredOOO = _QsyncIIgnoredOOO_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 123, 19)
)
_QsyncIIgnoredOOOVal_Type = Counter64
_QsyncIIgnoredOOOVal_Object = MibScalar
qsyncIIgnoredOOOVal = _QsyncIIgnoredOOOVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 123, 19, 1),
    _QsyncIIgnoredOOOVal_Type()
)
qsyncIIgnoredOOOVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qsyncIIgnoredOOOVal.setStatus("current")
_QsyncIIgnoredOOOMom_Type = CounterBasedGauge64
_QsyncIIgnoredOOOMom_Object = MibScalar
qsyncIIgnoredOOOMom = _QsyncIIgnoredOOOMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 123, 19, 2),
    _QsyncIIgnoredOOOMom_Type()
)
qsyncIIgnoredOOOMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qsyncIIgnoredOOOMom.setStatus("current")
_QsyncIIgnoredOOOMax_Type = CounterBasedGauge64
_QsyncIIgnoredOOOMax_Object = MibScalar
qsyncIIgnoredOOOMax = _QsyncIIgnoredOOOMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 123, 19, 3),
    _QsyncIIgnoredOOOMax_Type()
)
qsyncIIgnoredOOOMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qsyncIIgnoredOOOMax.setStatus("current")
_QsyncIIgnoredGenWrap_ObjectIdentity = ObjectIdentity
qsyncIIgnoredGenWrap = _QsyncIIgnoredGenWrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 123, 20)
)
_QsyncIIgnoredGenWrapVal_Type = Counter64
_QsyncIIgnoredGenWrapVal_Object = MibScalar
qsyncIIgnoredGenWrapVal = _QsyncIIgnoredGenWrapVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 123, 20, 1),
    _QsyncIIgnoredGenWrapVal_Type()
)
qsyncIIgnoredGenWrapVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qsyncIIgnoredGenWrapVal.setStatus("current")
_QsyncIIgnoredGenWrapMom_Type = CounterBasedGauge64
_QsyncIIgnoredGenWrapMom_Object = MibScalar
qsyncIIgnoredGenWrapMom = _QsyncIIgnoredGenWrapMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 123, 20, 2),
    _QsyncIIgnoredGenWrapMom_Type()
)
qsyncIIgnoredGenWrapMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qsyncIIgnoredGenWrapMom.setStatus("current")
_QsyncIIgnoredGenWrapMax_Type = CounterBasedGauge64
_QsyncIIgnoredGenWrapMax_Object = MibScalar
qsyncIIgnoredGenWrapMax = _QsyncIIgnoredGenWrapMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 123, 20, 3),
    _QsyncIIgnoredGenWrapMax_Type()
)
qsyncIIgnoredGenWrapMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qsyncIIgnoredGenWrapMax.setStatus("current")
_Shapingcounter_ObjectIdentity = ObjectIdentity
shapingcounter = _Shapingcounter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 124)
)
_ShapingcounterUpdates_ObjectIdentity = ObjectIdentity
shapingcounterUpdates = _ShapingcounterUpdates_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 124, 1)
)
_ShapingcounterUpdatesVal_Type = Counter64
_ShapingcounterUpdatesVal_Object = MibScalar
shapingcounterUpdatesVal = _ShapingcounterUpdatesVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 124, 1, 1),
    _ShapingcounterUpdatesVal_Type()
)
shapingcounterUpdatesVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingcounterUpdatesVal.setStatus("current")
_ShapingcounterUpdatesMom_Type = CounterBasedGauge64
_ShapingcounterUpdatesMom_Object = MibScalar
shapingcounterUpdatesMom = _ShapingcounterUpdatesMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 124, 1, 2),
    _ShapingcounterUpdatesMom_Type()
)
shapingcounterUpdatesMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingcounterUpdatesMom.setStatus("current")
_ShapingcounterUpdatesMax_Type = CounterBasedGauge64
_ShapingcounterUpdatesMax_Object = MibScalar
shapingcounterUpdatesMax = _ShapingcounterUpdatesMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 124, 1, 3),
    _ShapingcounterUpdatesMax_Type()
)
shapingcounterUpdatesMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingcounterUpdatesMax.setStatus("current")
_ShapingcounterActive_ObjectIdentity = ObjectIdentity
shapingcounterActive = _ShapingcounterActive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 124, 2)
)
_ShapingcounterActiveVal_Type = CounterBasedGauge64
_ShapingcounterActiveVal_Object = MibScalar
shapingcounterActiveVal = _ShapingcounterActiveVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 124, 2, 1),
    _ShapingcounterActiveVal_Type()
)
shapingcounterActiveVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingcounterActiveVal.setStatus("current")
_ShapingcounterActiveMax_Type = CounterBasedGauge64
_ShapingcounterActiveMax_Object = MibScalar
shapingcounterActiveMax = _ShapingcounterActiveMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 124, 2, 3),
    _ShapingcounterActiveMax_Type()
)
shapingcounterActiveMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingcounterActiveMax.setStatus("current")
_ShapingcounterClients_ObjectIdentity = ObjectIdentity
shapingcounterClients = _ShapingcounterClients_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 124, 3)
)
_ShapingcounterClientsVal_Type = CounterBasedGauge64
_ShapingcounterClientsVal_Object = MibScalar
shapingcounterClientsVal = _ShapingcounterClientsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 124, 3, 1),
    _ShapingcounterClientsVal_Type()
)
shapingcounterClientsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingcounterClientsVal.setStatus("current")
_ShapingcounterClientsMax_Type = CounterBasedGauge64
_ShapingcounterClientsMax_Object = MibScalar
shapingcounterClientsMax = _ShapingcounterClientsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 124, 3, 3),
    _ShapingcounterClientsMax_Type()
)
shapingcounterClientsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingcounterClientsMax.setStatus("current")
_ShapingcounterRecycle_ObjectIdentity = ObjectIdentity
shapingcounterRecycle = _ShapingcounterRecycle_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 124, 4)
)
_ShapingcounterRecycleVal_Type = Counter64
_ShapingcounterRecycleVal_Object = MibScalar
shapingcounterRecycleVal = _ShapingcounterRecycleVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 124, 4, 1),
    _ShapingcounterRecycleVal_Type()
)
shapingcounterRecycleVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingcounterRecycleVal.setStatus("current")
_ShapingcounterRecycleMom_Type = CounterBasedGauge64
_ShapingcounterRecycleMom_Object = MibScalar
shapingcounterRecycleMom = _ShapingcounterRecycleMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 124, 4, 2),
    _ShapingcounterRecycleMom_Type()
)
shapingcounterRecycleMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingcounterRecycleMom.setStatus("current")
_ShapingcounterRecycleMax_Type = CounterBasedGauge64
_ShapingcounterRecycleMax_Object = MibScalar
shapingcounterRecycleMax = _ShapingcounterRecycleMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 124, 4, 3),
    _ShapingcounterRecycleMax_Type()
)
shapingcounterRecycleMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingcounterRecycleMax.setStatus("current")
_ShapingcounterUpdatesInteresting_ObjectIdentity = ObjectIdentity
shapingcounterUpdatesInteresting = _ShapingcounterUpdatesInteresting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 124, 5)
)
_ShapingcounterUpdatesInterestingVal_Type = Counter64
_ShapingcounterUpdatesInterestingVal_Object = MibScalar
shapingcounterUpdatesInterestingVal = _ShapingcounterUpdatesInterestingVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 124, 5, 1),
    _ShapingcounterUpdatesInterestingVal_Type()
)
shapingcounterUpdatesInterestingVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingcounterUpdatesInterestingVal.setStatus("current")
_ShapingcounterUpdatesInterestingMom_Type = CounterBasedGauge64
_ShapingcounterUpdatesInterestingMom_Object = MibScalar
shapingcounterUpdatesInterestingMom = _ShapingcounterUpdatesInterestingMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 124, 5, 2),
    _ShapingcounterUpdatesInterestingMom_Type()
)
shapingcounterUpdatesInterestingMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingcounterUpdatesInterestingMom.setStatus("current")
_ShapingcounterUpdatesInterestingMax_Type = CounterBasedGauge64
_ShapingcounterUpdatesInterestingMax_Object = MibScalar
shapingcounterUpdatesInterestingMax = _ShapingcounterUpdatesInterestingMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 124, 5, 3),
    _ShapingcounterUpdatesInterestingMax_Type()
)
shapingcounterUpdatesInterestingMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shapingcounterUpdatesInterestingMax.setStatus("current")
_Divert_ObjectIdentity = ObjectIdentity
divert = _Divert_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 125)
)
_DivertOutOfHosts_ObjectIdentity = ObjectIdentity
divertOutOfHosts = _DivertOutOfHosts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 125, 2)
)
_DivertOutOfHostsVal_Type = Counter64
_DivertOutOfHostsVal_Object = MibScalar
divertOutOfHostsVal = _DivertOutOfHostsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 125, 2, 1),
    _DivertOutOfHostsVal_Type()
)
divertOutOfHostsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    divertOutOfHostsVal.setStatus("current")
_DivertOutOfHostsMom_Type = CounterBasedGauge64
_DivertOutOfHostsMom_Object = MibScalar
divertOutOfHostsMom = _DivertOutOfHostsMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 125, 2, 2),
    _DivertOutOfHostsMom_Type()
)
divertOutOfHostsMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    divertOutOfHostsMom.setStatus("current")
_DivertOutOfHostsMax_Type = CounterBasedGauge64
_DivertOutOfHostsMax_Object = MibScalar
divertOutOfHostsMax = _DivertOutOfHostsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 125, 2, 3),
    _DivertOutOfHostsMax_Type()
)
divertOutOfHostsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    divertOutOfHostsMax.setStatus("current")
_DivertOversizeL2_ObjectIdentity = ObjectIdentity
divertOversizeL2 = _DivertOversizeL2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 125, 3)
)
_DivertOversizeL2Val_Type = Counter64
_DivertOversizeL2Val_Object = MibScalar
divertOversizeL2Val = _DivertOversizeL2Val_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 125, 3, 1),
    _DivertOversizeL2Val_Type()
)
divertOversizeL2Val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    divertOversizeL2Val.setStatus("current")
_DivertOversizeL2Mom_Type = CounterBasedGauge64
_DivertOversizeL2Mom_Object = MibScalar
divertOversizeL2Mom = _DivertOversizeL2Mom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 125, 3, 2),
    _DivertOversizeL2Mom_Type()
)
divertOversizeL2Mom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    divertOversizeL2Mom.setStatus("current")
_DivertOversizeL2Max_Type = CounterBasedGauge64
_DivertOversizeL2Max_Object = MibScalar
divertOversizeL2Max = _DivertOversizeL2Max_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 125, 3, 3),
    _DivertOversizeL2Max_Type()
)
divertOversizeL2Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    divertOversizeL2Max.setStatus("current")
_DivertEgressPackets_ObjectIdentity = ObjectIdentity
divertEgressPackets = _DivertEgressPackets_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 125, 4)
)
_DivertEgressPacketsVal_Type = Counter64
_DivertEgressPacketsVal_Object = MibScalar
divertEgressPacketsVal = _DivertEgressPacketsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 125, 4, 1),
    _DivertEgressPacketsVal_Type()
)
divertEgressPacketsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    divertEgressPacketsVal.setStatus("current")
_DivertEgressPacketsMom_Type = CounterBasedGauge64
_DivertEgressPacketsMom_Object = MibScalar
divertEgressPacketsMom = _DivertEgressPacketsMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 125, 4, 2),
    _DivertEgressPacketsMom_Type()
)
divertEgressPacketsMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    divertEgressPacketsMom.setStatus("current")
_DivertEgressPacketsMax_Type = CounterBasedGauge64
_DivertEgressPacketsMax_Object = MibScalar
divertEgressPacketsMax = _DivertEgressPacketsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 125, 4, 3),
    _DivertEgressPacketsMax_Type()
)
divertEgressPacketsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    divertEgressPacketsMax.setStatus("current")
_DivertEgressBytes_ObjectIdentity = ObjectIdentity
divertEgressBytes = _DivertEgressBytes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 125, 5)
)
_DivertEgressBytesVal_Type = Counter64
_DivertEgressBytesVal_Object = MibScalar
divertEgressBytesVal = _DivertEgressBytesVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 125, 5, 1),
    _DivertEgressBytesVal_Type()
)
divertEgressBytesVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    divertEgressBytesVal.setStatus("current")
_DivertEgressBytesMom_Type = CounterBasedGauge64
_DivertEgressBytesMom_Object = MibScalar
divertEgressBytesMom = _DivertEgressBytesMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 125, 5, 2),
    _DivertEgressBytesMom_Type()
)
divertEgressBytesMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    divertEgressBytesMom.setStatus("current")
_DivertEgressBytesMax_Type = CounterBasedGauge64
_DivertEgressBytesMax_Object = MibScalar
divertEgressBytesMax = _DivertEgressBytesMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 125, 5, 3),
    _DivertEgressBytesMax_Type()
)
divertEgressBytesMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    divertEgressBytesMax.setStatus("current")
_DivertIngressPackets_ObjectIdentity = ObjectIdentity
divertIngressPackets = _DivertIngressPackets_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 125, 6)
)
_DivertIngressPacketsVal_Type = Counter64
_DivertIngressPacketsVal_Object = MibScalar
divertIngressPacketsVal = _DivertIngressPacketsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 125, 6, 1),
    _DivertIngressPacketsVal_Type()
)
divertIngressPacketsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    divertIngressPacketsVal.setStatus("current")
_DivertIngressPacketsMom_Type = CounterBasedGauge64
_DivertIngressPacketsMom_Object = MibScalar
divertIngressPacketsMom = _DivertIngressPacketsMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 125, 6, 2),
    _DivertIngressPacketsMom_Type()
)
divertIngressPacketsMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    divertIngressPacketsMom.setStatus("current")
_DivertIngressPacketsMax_Type = CounterBasedGauge64
_DivertIngressPacketsMax_Object = MibScalar
divertIngressPacketsMax = _DivertIngressPacketsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 125, 6, 3),
    _DivertIngressPacketsMax_Type()
)
divertIngressPacketsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    divertIngressPacketsMax.setStatus("current")
_DivertIngressBytes_ObjectIdentity = ObjectIdentity
divertIngressBytes = _DivertIngressBytes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 125, 7)
)
_DivertIngressBytesVal_Type = Counter64
_DivertIngressBytesVal_Object = MibScalar
divertIngressBytesVal = _DivertIngressBytesVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 125, 7, 1),
    _DivertIngressBytesVal_Type()
)
divertIngressBytesVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    divertIngressBytesVal.setStatus("current")
_DivertIngressBytesMom_Type = CounterBasedGauge64
_DivertIngressBytesMom_Object = MibScalar
divertIngressBytesMom = _DivertIngressBytesMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 125, 7, 2),
    _DivertIngressBytesMom_Type()
)
divertIngressBytesMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    divertIngressBytesMom.setStatus("current")
_DivertIngressBytesMax_Type = CounterBasedGauge64
_DivertIngressBytesMax_Object = MibScalar
divertIngressBytesMax = _DivertIngressBytesMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 125, 7, 3),
    _DivertIngressBytesMax_Type()
)
divertIngressBytesMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    divertIngressBytesMax.setStatus("current")
_DivertIngressPacketsNohost_ObjectIdentity = ObjectIdentity
divertIngressPacketsNohost = _DivertIngressPacketsNohost_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 125, 8)
)
_DivertIngressPacketsNohostVal_Type = Counter64
_DivertIngressPacketsNohostVal_Object = MibScalar
divertIngressPacketsNohostVal = _DivertIngressPacketsNohostVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 125, 8, 1),
    _DivertIngressPacketsNohostVal_Type()
)
divertIngressPacketsNohostVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    divertIngressPacketsNohostVal.setStatus("current")
_DivertIngressPacketsNohostMom_Type = CounterBasedGauge64
_DivertIngressPacketsNohostMom_Object = MibScalar
divertIngressPacketsNohostMom = _DivertIngressPacketsNohostMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 125, 8, 2),
    _DivertIngressPacketsNohostMom_Type()
)
divertIngressPacketsNohostMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    divertIngressPacketsNohostMom.setStatus("current")
_DivertIngressPacketsNohostMax_Type = CounterBasedGauge64
_DivertIngressPacketsNohostMax_Object = MibScalar
divertIngressPacketsNohostMax = _DivertIngressPacketsNohostMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 125, 8, 3),
    _DivertIngressPacketsNohostMax_Type()
)
divertIngressPacketsNohostMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    divertIngressPacketsNohostMax.setStatus("current")
_DivertIngressPacketsNol2_ObjectIdentity = ObjectIdentity
divertIngressPacketsNol2 = _DivertIngressPacketsNol2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 125, 9)
)
_DivertIngressPacketsNol2Val_Type = Counter64
_DivertIngressPacketsNol2Val_Object = MibScalar
divertIngressPacketsNol2Val = _DivertIngressPacketsNol2Val_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 125, 9, 1),
    _DivertIngressPacketsNol2Val_Type()
)
divertIngressPacketsNol2Val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    divertIngressPacketsNol2Val.setStatus("current")
_DivertIngressPacketsNol2Mom_Type = CounterBasedGauge64
_DivertIngressPacketsNol2Mom_Object = MibScalar
divertIngressPacketsNol2Mom = _DivertIngressPacketsNol2Mom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 125, 9, 2),
    _DivertIngressPacketsNol2Mom_Type()
)
divertIngressPacketsNol2Mom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    divertIngressPacketsNol2Mom.setStatus("current")
_DivertIngressPacketsNol2Max_Type = CounterBasedGauge64
_DivertIngressPacketsNol2Max_Object = MibScalar
divertIngressPacketsNol2Max = _DivertIngressPacketsNol2Max_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 125, 9, 3),
    _DivertIngressPacketsNol2Max_Type()
)
divertIngressPacketsNol2Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    divertIngressPacketsNol2Max.setStatus("current")
_DivertHostsUse_ObjectIdentity = ObjectIdentity
divertHostsUse = _DivertHostsUse_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 125, 10)
)
_DivertHostsUseVal_Type = CounterBasedGauge64
_DivertHostsUseVal_Object = MibScalar
divertHostsUseVal = _DivertHostsUseVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 125, 10, 1),
    _DivertHostsUseVal_Type()
)
divertHostsUseVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    divertHostsUseVal.setStatus("current")
_DivertHostsUseMax_Type = CounterBasedGauge64
_DivertHostsUseMax_Object = MibScalar
divertHostsUseMax = _DivertHostsUseMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 125, 10, 3),
    _DivertHostsUseMax_Type()
)
divertHostsUseMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    divertHostsUseMax.setStatus("current")
_DivertConnections_ObjectIdentity = ObjectIdentity
divertConnections = _DivertConnections_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 125, 11)
)
_DivertConnectionsVal_Type = CounterBasedGauge64
_DivertConnectionsVal_Object = MibScalar
divertConnectionsVal = _DivertConnectionsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 125, 11, 1),
    _DivertConnectionsVal_Type()
)
divertConnectionsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    divertConnectionsVal.setStatus("current")
_DivertConnectionsMax_Type = CounterBasedGauge64
_DivertConnectionsMax_Object = MibScalar
divertConnectionsMax = _DivertConnectionsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 125, 11, 3),
    _DivertConnectionsMax_Type()
)
divertConnectionsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    divertConnectionsMax.setStatus("current")
_DivertHbReqSent_ObjectIdentity = ObjectIdentity
divertHbReqSent = _DivertHbReqSent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 125, 12)
)
_DivertHbReqSentVal_Type = Counter64
_DivertHbReqSentVal_Object = MibScalar
divertHbReqSentVal = _DivertHbReqSentVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 125, 12, 1),
    _DivertHbReqSentVal_Type()
)
divertHbReqSentVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    divertHbReqSentVal.setStatus("current")
_DivertHbReqSentMom_Type = CounterBasedGauge64
_DivertHbReqSentMom_Object = MibScalar
divertHbReqSentMom = _DivertHbReqSentMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 125, 12, 2),
    _DivertHbReqSentMom_Type()
)
divertHbReqSentMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    divertHbReqSentMom.setStatus("current")
_DivertHbReqSentMax_Type = CounterBasedGauge64
_DivertHbReqSentMax_Object = MibScalar
divertHbReqSentMax = _DivertHbReqSentMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 125, 12, 3),
    _DivertHbReqSentMax_Type()
)
divertHbReqSentMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    divertHbReqSentMax.setStatus("current")
_DivertHbReqRecv_ObjectIdentity = ObjectIdentity
divertHbReqRecv = _DivertHbReqRecv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 125, 13)
)
_DivertHbReqRecvVal_Type = Counter64
_DivertHbReqRecvVal_Object = MibScalar
divertHbReqRecvVal = _DivertHbReqRecvVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 125, 13, 1),
    _DivertHbReqRecvVal_Type()
)
divertHbReqRecvVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    divertHbReqRecvVal.setStatus("current")
_DivertHbReqRecvMom_Type = CounterBasedGauge64
_DivertHbReqRecvMom_Object = MibScalar
divertHbReqRecvMom = _DivertHbReqRecvMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 125, 13, 2),
    _DivertHbReqRecvMom_Type()
)
divertHbReqRecvMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    divertHbReqRecvMom.setStatus("current")
_DivertHbReqRecvMax_Type = CounterBasedGauge64
_DivertHbReqRecvMax_Object = MibScalar
divertHbReqRecvMax = _DivertHbReqRecvMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 125, 13, 3),
    _DivertHbReqRecvMax_Type()
)
divertHbReqRecvMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    divertHbReqRecvMax.setStatus("current")
_DivertHbRepSent_ObjectIdentity = ObjectIdentity
divertHbRepSent = _DivertHbRepSent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 125, 14)
)
_DivertHbRepSentVal_Type = Counter64
_DivertHbRepSentVal_Object = MibScalar
divertHbRepSentVal = _DivertHbRepSentVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 125, 14, 1),
    _DivertHbRepSentVal_Type()
)
divertHbRepSentVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    divertHbRepSentVal.setStatus("current")
_DivertHbRepSentMom_Type = CounterBasedGauge64
_DivertHbRepSentMom_Object = MibScalar
divertHbRepSentMom = _DivertHbRepSentMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 125, 14, 2),
    _DivertHbRepSentMom_Type()
)
divertHbRepSentMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    divertHbRepSentMom.setStatus("current")
_DivertHbRepSentMax_Type = CounterBasedGauge64
_DivertHbRepSentMax_Object = MibScalar
divertHbRepSentMax = _DivertHbRepSentMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 125, 14, 3),
    _DivertHbRepSentMax_Type()
)
divertHbRepSentMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    divertHbRepSentMax.setStatus("current")
_DivertHbRepRecv_ObjectIdentity = ObjectIdentity
divertHbRepRecv = _DivertHbRepRecv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 125, 15)
)
_DivertHbRepRecvVal_Type = Counter64
_DivertHbRepRecvVal_Object = MibScalar
divertHbRepRecvVal = _DivertHbRepRecvVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 125, 15, 1),
    _DivertHbRepRecvVal_Type()
)
divertHbRepRecvVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    divertHbRepRecvVal.setStatus("current")
_DivertHbRepRecvMom_Type = CounterBasedGauge64
_DivertHbRepRecvMom_Object = MibScalar
divertHbRepRecvMom = _DivertHbRepRecvMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 125, 15, 2),
    _DivertHbRepRecvMom_Type()
)
divertHbRepRecvMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    divertHbRepRecvMom.setStatus("current")
_DivertHbRepRecvMax_Type = CounterBasedGauge64
_DivertHbRepRecvMax_Object = MibScalar
divertHbRepRecvMax = _DivertHbRepRecvMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 125, 15, 3),
    _DivertHbRepRecvMax_Type()
)
divertHbRepRecvMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    divertHbRepRecvMax.setStatus("current")
_DivertHbLost_ObjectIdentity = ObjectIdentity
divertHbLost = _DivertHbLost_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 125, 16)
)
_DivertHbLostVal_Type = Counter64
_DivertHbLostVal_Object = MibScalar
divertHbLostVal = _DivertHbLostVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 125, 16, 1),
    _DivertHbLostVal_Type()
)
divertHbLostVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    divertHbLostVal.setStatus("current")
_DivertHbLostMom_Type = CounterBasedGauge64
_DivertHbLostMom_Object = MibScalar
divertHbLostMom = _DivertHbLostMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 125, 16, 2),
    _DivertHbLostMom_Type()
)
divertHbLostMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    divertHbLostMom.setStatus("current")
_DivertHbLostMax_Type = CounterBasedGauge64
_DivertHbLostMax_Object = MibScalar
divertHbLostMax = _DivertHbLostMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 125, 16, 3),
    _DivertHbLostMax_Type()
)
divertHbLostMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    divertHbLostMax.setStatus("current")
_DivertBypassPackets_ObjectIdentity = ObjectIdentity
divertBypassPackets = _DivertBypassPackets_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 125, 17)
)
_DivertBypassPacketsVal_Type = Counter64
_DivertBypassPacketsVal_Object = MibScalar
divertBypassPacketsVal = _DivertBypassPacketsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 125, 17, 1),
    _DivertBypassPacketsVal_Type()
)
divertBypassPacketsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    divertBypassPacketsVal.setStatus("current")
_DivertBypassPacketsMom_Type = CounterBasedGauge64
_DivertBypassPacketsMom_Object = MibScalar
divertBypassPacketsMom = _DivertBypassPacketsMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 125, 17, 2),
    _DivertBypassPacketsMom_Type()
)
divertBypassPacketsMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    divertBypassPacketsMom.setStatus("current")
_DivertBypassPacketsMax_Type = CounterBasedGauge64
_DivertBypassPacketsMax_Object = MibScalar
divertBypassPacketsMax = _DivertBypassPacketsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 125, 17, 3),
    _DivertBypassPacketsMax_Type()
)
divertBypassPacketsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    divertBypassPacketsMax.setStatus("current")
_DivertDroppedPackets_ObjectIdentity = ObjectIdentity
divertDroppedPackets = _DivertDroppedPackets_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 125, 18)
)
_DivertDroppedPacketsVal_Type = Counter64
_DivertDroppedPacketsVal_Object = MibScalar
divertDroppedPacketsVal = _DivertDroppedPacketsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 125, 18, 1),
    _DivertDroppedPacketsVal_Type()
)
divertDroppedPacketsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    divertDroppedPacketsVal.setStatus("current")
_DivertDroppedPacketsMom_Type = CounterBasedGauge64
_DivertDroppedPacketsMom_Object = MibScalar
divertDroppedPacketsMom = _DivertDroppedPacketsMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 125, 18, 2),
    _DivertDroppedPacketsMom_Type()
)
divertDroppedPacketsMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    divertDroppedPacketsMom.setStatus("current")
_DivertDroppedPacketsMax_Type = CounterBasedGauge64
_DivertDroppedPacketsMax_Object = MibScalar
divertDroppedPacketsMax = _DivertDroppedPacketsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 125, 18, 3),
    _DivertDroppedPacketsMax_Type()
)
divertDroppedPacketsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    divertDroppedPacketsMax.setStatus("current")
_Ipv6_ObjectIdentity = ObjectIdentity
ipv6 = _Ipv6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 126)
)
_Ipv6Packets_ObjectIdentity = ObjectIdentity
ipv6Packets = _Ipv6Packets_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 126, 1)
)
_Ipv6PacketsVal_Type = Counter64
_Ipv6PacketsVal_Object = MibScalar
ipv6PacketsVal = _Ipv6PacketsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 126, 1, 1),
    _Ipv6PacketsVal_Type()
)
ipv6PacketsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6PacketsVal.setStatus("current")
_Ipv6PacketsMom_Type = CounterBasedGauge64
_Ipv6PacketsMom_Object = MibScalar
ipv6PacketsMom = _Ipv6PacketsMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 126, 1, 2),
    _Ipv6PacketsMom_Type()
)
ipv6PacketsMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6PacketsMom.setStatus("current")
_Ipv6PacketsMax_Type = CounterBasedGauge64
_Ipv6PacketsMax_Object = MibScalar
ipv6PacketsMax = _Ipv6PacketsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 126, 1, 3),
    _Ipv6PacketsMax_Type()
)
ipv6PacketsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6PacketsMax.setStatus("current")
_Ipv6Bytes_ObjectIdentity = ObjectIdentity
ipv6Bytes = _Ipv6Bytes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 126, 2)
)
_Ipv6BytesVal_Type = Counter64
_Ipv6BytesVal_Object = MibScalar
ipv6BytesVal = _Ipv6BytesVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 126, 2, 1),
    _Ipv6BytesVal_Type()
)
ipv6BytesVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6BytesVal.setStatus("current")
_Ipv6BytesMom_Type = CounterBasedGauge64
_Ipv6BytesMom_Object = MibScalar
ipv6BytesMom = _Ipv6BytesMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 126, 2, 2),
    _Ipv6BytesMom_Type()
)
ipv6BytesMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6BytesMom.setStatus("current")
_Ipv6BytesMax_Type = CounterBasedGauge64
_Ipv6BytesMax_Object = MibScalar
ipv6BytesMax = _Ipv6BytesMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 126, 2, 3),
    _Ipv6BytesMax_Type()
)
ipv6BytesMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6BytesMax.setStatus("current")
_Ipv6RefusedShort_ObjectIdentity = ObjectIdentity
ipv6RefusedShort = _Ipv6RefusedShort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 126, 3)
)
_Ipv6RefusedShortVal_Type = Counter64
_Ipv6RefusedShortVal_Object = MibScalar
ipv6RefusedShortVal = _Ipv6RefusedShortVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 126, 3, 1),
    _Ipv6RefusedShortVal_Type()
)
ipv6RefusedShortVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6RefusedShortVal.setStatus("current")
_Ipv6RefusedShortMom_Type = CounterBasedGauge64
_Ipv6RefusedShortMom_Object = MibScalar
ipv6RefusedShortMom = _Ipv6RefusedShortMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 126, 3, 2),
    _Ipv6RefusedShortMom_Type()
)
ipv6RefusedShortMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6RefusedShortMom.setStatus("current")
_Ipv6RefusedShortMax_Type = CounterBasedGauge64
_Ipv6RefusedShortMax_Object = MibScalar
ipv6RefusedShortMax = _Ipv6RefusedShortMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 126, 3, 3),
    _Ipv6RefusedShortMax_Type()
)
ipv6RefusedShortMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6RefusedShortMax.setStatus("current")
_Ipv6RefusedVersion_ObjectIdentity = ObjectIdentity
ipv6RefusedVersion = _Ipv6RefusedVersion_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 126, 4)
)
_Ipv6RefusedVersionVal_Type = Counter64
_Ipv6RefusedVersionVal_Object = MibScalar
ipv6RefusedVersionVal = _Ipv6RefusedVersionVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 126, 4, 1),
    _Ipv6RefusedVersionVal_Type()
)
ipv6RefusedVersionVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6RefusedVersionVal.setStatus("current")
_Ipv6RefusedVersionMom_Type = CounterBasedGauge64
_Ipv6RefusedVersionMom_Object = MibScalar
ipv6RefusedVersionMom = _Ipv6RefusedVersionMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 126, 4, 2),
    _Ipv6RefusedVersionMom_Type()
)
ipv6RefusedVersionMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6RefusedVersionMom.setStatus("current")
_Ipv6RefusedVersionMax_Type = CounterBasedGauge64
_Ipv6RefusedVersionMax_Object = MibScalar
ipv6RefusedVersionMax = _Ipv6RefusedVersionMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 126, 4, 3),
    _Ipv6RefusedVersionMax_Type()
)
ipv6RefusedVersionMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6RefusedVersionMax.setStatus("current")
_Ipv6RefusedSelf_ObjectIdentity = ObjectIdentity
ipv6RefusedSelf = _Ipv6RefusedSelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 126, 5)
)
_Ipv6RefusedSelfVal_Type = Counter64
_Ipv6RefusedSelfVal_Object = MibScalar
ipv6RefusedSelfVal = _Ipv6RefusedSelfVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 126, 5, 1),
    _Ipv6RefusedSelfVal_Type()
)
ipv6RefusedSelfVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6RefusedSelfVal.setStatus("current")
_Ipv6RefusedSelfMom_Type = CounterBasedGauge64
_Ipv6RefusedSelfMom_Object = MibScalar
ipv6RefusedSelfMom = _Ipv6RefusedSelfMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 126, 5, 2),
    _Ipv6RefusedSelfMom_Type()
)
ipv6RefusedSelfMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6RefusedSelfMom.setStatus("current")
_Ipv6RefusedSelfMax_Type = CounterBasedGauge64
_Ipv6RefusedSelfMax_Object = MibScalar
ipv6RefusedSelfMax = _Ipv6RefusedSelfMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 126, 5, 3),
    _Ipv6RefusedSelfMax_Type()
)
ipv6RefusedSelfMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6RefusedSelfMax.setStatus("current")
_Ipv6Fragmented_ObjectIdentity = ObjectIdentity
ipv6Fragmented = _Ipv6Fragmented_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 126, 7)
)
_Ipv6FragmentedVal_Type = Counter64
_Ipv6FragmentedVal_Object = MibScalar
ipv6FragmentedVal = _Ipv6FragmentedVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 126, 7, 1),
    _Ipv6FragmentedVal_Type()
)
ipv6FragmentedVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6FragmentedVal.setStatus("current")
_Ipv6FragmentedMom_Type = CounterBasedGauge64
_Ipv6FragmentedMom_Object = MibScalar
ipv6FragmentedMom = _Ipv6FragmentedMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 126, 7, 2),
    _Ipv6FragmentedMom_Type()
)
ipv6FragmentedMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6FragmentedMom.setStatus("current")
_Ipv6FragmentedMax_Type = CounterBasedGauge64
_Ipv6FragmentedMax_Object = MibScalar
ipv6FragmentedMax = _Ipv6FragmentedMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 126, 7, 3),
    _Ipv6FragmentedMax_Type()
)
ipv6FragmentedMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6FragmentedMax.setStatus("current")
_Ipv6FragmentedIds_ObjectIdentity = ObjectIdentity
ipv6FragmentedIds = _Ipv6FragmentedIds_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 126, 10)
)
_Ipv6FragmentedIdsVal_Type = CounterBasedGauge64
_Ipv6FragmentedIdsVal_Object = MibScalar
ipv6FragmentedIdsVal = _Ipv6FragmentedIdsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 126, 10, 1),
    _Ipv6FragmentedIdsVal_Type()
)
ipv6FragmentedIdsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6FragmentedIdsVal.setStatus("current")
_Ipv6FragmentedIdsMax_Type = CounterBasedGauge64
_Ipv6FragmentedIdsMax_Object = MibScalar
ipv6FragmentedIdsMax = _Ipv6FragmentedIdsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 126, 10, 3),
    _Ipv6FragmentedIdsMax_Type()
)
ipv6FragmentedIdsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6FragmentedIdsMax.setStatus("current")
_Ipv6Fragments_ObjectIdentity = ObjectIdentity
ipv6Fragments = _Ipv6Fragments_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 126, 11)
)
_Ipv6FragmentsVal_Type = CounterBasedGauge64
_Ipv6FragmentsVal_Object = MibScalar
ipv6FragmentsVal = _Ipv6FragmentsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 126, 11, 1),
    _Ipv6FragmentsVal_Type()
)
ipv6FragmentsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6FragmentsVal.setStatus("current")
_Ipv6FragmentsMax_Type = CounterBasedGauge64
_Ipv6FragmentsMax_Object = MibScalar
ipv6FragmentsMax = _Ipv6FragmentsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 126, 11, 3),
    _Ipv6FragmentsMax_Type()
)
ipv6FragmentsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6FragmentsMax.setStatus("current")
_Ipv6RefusedOof_ObjectIdentity = ObjectIdentity
ipv6RefusedOof = _Ipv6RefusedOof_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 126, 14)
)
_Ipv6RefusedOofVal_Type = Counter64
_Ipv6RefusedOofVal_Object = MibScalar
ipv6RefusedOofVal = _Ipv6RefusedOofVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 126, 14, 1),
    _Ipv6RefusedOofVal_Type()
)
ipv6RefusedOofVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6RefusedOofVal.setStatus("current")
_Ipv6RefusedOofMom_Type = CounterBasedGauge64
_Ipv6RefusedOofMom_Object = MibScalar
ipv6RefusedOofMom = _Ipv6RefusedOofMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 126, 14, 2),
    _Ipv6RefusedOofMom_Type()
)
ipv6RefusedOofMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6RefusedOofMom.setStatus("current")
_Ipv6RefusedOofMax_Type = CounterBasedGauge64
_Ipv6RefusedOofMax_Object = MibScalar
ipv6RefusedOofMax = _Ipv6RefusedOofMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 126, 14, 3),
    _Ipv6RefusedOofMax_Type()
)
ipv6RefusedOofMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6RefusedOofMax.setStatus("current")
_Ipv6FragmentAllocationFailures_ObjectIdentity = ObjectIdentity
ipv6FragmentAllocationFailures = _Ipv6FragmentAllocationFailures_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 126, 15)
)
_Ipv6FragmentAllocationFailuresVal_Type = Counter64
_Ipv6FragmentAllocationFailuresVal_Object = MibScalar
ipv6FragmentAllocationFailuresVal = _Ipv6FragmentAllocationFailuresVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 126, 15, 1),
    _Ipv6FragmentAllocationFailuresVal_Type()
)
ipv6FragmentAllocationFailuresVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6FragmentAllocationFailuresVal.setStatus("current")
_Ipv6FragmentAllocationFailuresMom_Type = CounterBasedGauge64
_Ipv6FragmentAllocationFailuresMom_Object = MibScalar
ipv6FragmentAllocationFailuresMom = _Ipv6FragmentAllocationFailuresMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 126, 15, 2),
    _Ipv6FragmentAllocationFailuresMom_Type()
)
ipv6FragmentAllocationFailuresMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6FragmentAllocationFailuresMom.setStatus("current")
_Ipv6FragmentAllocationFailuresMax_Type = CounterBasedGauge64
_Ipv6FragmentAllocationFailuresMax_Object = MibScalar
ipv6FragmentAllocationFailuresMax = _Ipv6FragmentAllocationFailuresMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 126, 15, 3),
    _Ipv6FragmentAllocationFailuresMax_Type()
)
ipv6FragmentAllocationFailuresMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6FragmentAllocationFailuresMax.setStatus("current")
_Ipv6FragmentReassFail_ObjectIdentity = ObjectIdentity
ipv6FragmentReassFail = _Ipv6FragmentReassFail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 126, 16)
)
_Ipv6FragmentReassFailVal_Type = Counter64
_Ipv6FragmentReassFailVal_Object = MibScalar
ipv6FragmentReassFailVal = _Ipv6FragmentReassFailVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 126, 16, 1),
    _Ipv6FragmentReassFailVal_Type()
)
ipv6FragmentReassFailVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6FragmentReassFailVal.setStatus("current")
_Ipv6FragmentReassFailMom_Type = CounterBasedGauge64
_Ipv6FragmentReassFailMom_Object = MibScalar
ipv6FragmentReassFailMom = _Ipv6FragmentReassFailMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 126, 16, 2),
    _Ipv6FragmentReassFailMom_Type()
)
ipv6FragmentReassFailMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6FragmentReassFailMom.setStatus("current")
_Ipv6FragmentReassFailMax_Type = CounterBasedGauge64
_Ipv6FragmentReassFailMax_Object = MibScalar
ipv6FragmentReassFailMax = _Ipv6FragmentReassFailMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 126, 16, 3),
    _Ipv6FragmentReassFailMax_Type()
)
ipv6FragmentReassFailMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6FragmentReassFailMax.setStatus("current")
_Ipv6FragmentTooNoisy_ObjectIdentity = ObjectIdentity
ipv6FragmentTooNoisy = _Ipv6FragmentTooNoisy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 126, 19)
)
_Ipv6FragmentTooNoisyVal_Type = Counter64
_Ipv6FragmentTooNoisyVal_Object = MibScalar
ipv6FragmentTooNoisyVal = _Ipv6FragmentTooNoisyVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 126, 19, 1),
    _Ipv6FragmentTooNoisyVal_Type()
)
ipv6FragmentTooNoisyVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6FragmentTooNoisyVal.setStatus("current")
_Ipv6FragmentTooNoisyMom_Type = CounterBasedGauge64
_Ipv6FragmentTooNoisyMom_Object = MibScalar
ipv6FragmentTooNoisyMom = _Ipv6FragmentTooNoisyMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 126, 19, 2),
    _Ipv6FragmentTooNoisyMom_Type()
)
ipv6FragmentTooNoisyMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6FragmentTooNoisyMom.setStatus("current")
_Ipv6FragmentTooNoisyMax_Type = CounterBasedGauge64
_Ipv6FragmentTooNoisyMax_Object = MibScalar
ipv6FragmentTooNoisyMax = _Ipv6FragmentTooNoisyMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 126, 19, 3),
    _Ipv6FragmentTooNoisyMax_Type()
)
ipv6FragmentTooNoisyMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6FragmentTooNoisyMax.setStatus("current")
_Ipv6Reassembled_ObjectIdentity = ObjectIdentity
ipv6Reassembled = _Ipv6Reassembled_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 126, 20)
)
_Ipv6ReassembledVal_Type = Counter64
_Ipv6ReassembledVal_Object = MibScalar
ipv6ReassembledVal = _Ipv6ReassembledVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 126, 20, 1),
    _Ipv6ReassembledVal_Type()
)
ipv6ReassembledVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6ReassembledVal.setStatus("current")
_Ipv6ReassembledMom_Type = CounterBasedGauge64
_Ipv6ReassembledMom_Object = MibScalar
ipv6ReassembledMom = _Ipv6ReassembledMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 126, 20, 2),
    _Ipv6ReassembledMom_Type()
)
ipv6ReassembledMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6ReassembledMom.setStatus("current")
_Ipv6ReassembledMax_Type = CounterBasedGauge64
_Ipv6ReassembledMax_Object = MibScalar
ipv6ReassembledMax = _Ipv6ReassembledMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 126, 20, 3),
    _Ipv6ReassembledMax_Type()
)
ipv6ReassembledMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6ReassembledMax.setStatus("current")
_Ipv6FragmentOverlap_ObjectIdentity = ObjectIdentity
ipv6FragmentOverlap = _Ipv6FragmentOverlap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 126, 21)
)
_Ipv6FragmentOverlapVal_Type = Counter64
_Ipv6FragmentOverlapVal_Object = MibScalar
ipv6FragmentOverlapVal = _Ipv6FragmentOverlapVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 126, 21, 1),
    _Ipv6FragmentOverlapVal_Type()
)
ipv6FragmentOverlapVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6FragmentOverlapVal.setStatus("current")
_Ipv6FragmentOverlapMom_Type = CounterBasedGauge64
_Ipv6FragmentOverlapMom_Object = MibScalar
ipv6FragmentOverlapMom = _Ipv6FragmentOverlapMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 126, 21, 2),
    _Ipv6FragmentOverlapMom_Type()
)
ipv6FragmentOverlapMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6FragmentOverlapMom.setStatus("current")
_Ipv6FragmentOverlapMax_Type = CounterBasedGauge64
_Ipv6FragmentOverlapMax_Object = MibScalar
ipv6FragmentOverlapMax = _Ipv6FragmentOverlapMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 126, 21, 3),
    _Ipv6FragmentOverlapMax_Type()
)
ipv6FragmentOverlapMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6FragmentOverlapMax.setStatus("current")
_Ipv6ExtDest_ObjectIdentity = ObjectIdentity
ipv6ExtDest = _Ipv6ExtDest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 126, 22)
)
_Ipv6ExtDestVal_Type = Counter64
_Ipv6ExtDestVal_Object = MibScalar
ipv6ExtDestVal = _Ipv6ExtDestVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 126, 22, 1),
    _Ipv6ExtDestVal_Type()
)
ipv6ExtDestVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6ExtDestVal.setStatus("current")
_Ipv6ExtDestMom_Type = CounterBasedGauge64
_Ipv6ExtDestMom_Object = MibScalar
ipv6ExtDestMom = _Ipv6ExtDestMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 126, 22, 2),
    _Ipv6ExtDestMom_Type()
)
ipv6ExtDestMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6ExtDestMom.setStatus("current")
_Ipv6ExtDestMax_Type = CounterBasedGauge64
_Ipv6ExtDestMax_Object = MibScalar
ipv6ExtDestMax = _Ipv6ExtDestMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 126, 22, 3),
    _Ipv6ExtDestMax_Type()
)
ipv6ExtDestMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6ExtDestMax.setStatus("current")
_Ipv6ExtHbh_ObjectIdentity = ObjectIdentity
ipv6ExtHbh = _Ipv6ExtHbh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 126, 23)
)
_Ipv6ExtHbhVal_Type = Counter64
_Ipv6ExtHbhVal_Object = MibScalar
ipv6ExtHbhVal = _Ipv6ExtHbhVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 126, 23, 1),
    _Ipv6ExtHbhVal_Type()
)
ipv6ExtHbhVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6ExtHbhVal.setStatus("current")
_Ipv6ExtHbhMom_Type = CounterBasedGauge64
_Ipv6ExtHbhMom_Object = MibScalar
ipv6ExtHbhMom = _Ipv6ExtHbhMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 126, 23, 2),
    _Ipv6ExtHbhMom_Type()
)
ipv6ExtHbhMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6ExtHbhMom.setStatus("current")
_Ipv6ExtHbhMax_Type = CounterBasedGauge64
_Ipv6ExtHbhMax_Object = MibScalar
ipv6ExtHbhMax = _Ipv6ExtHbhMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 126, 23, 3),
    _Ipv6ExtHbhMax_Type()
)
ipv6ExtHbhMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6ExtHbhMax.setStatus("current")
_Ipv6ExtRoute_ObjectIdentity = ObjectIdentity
ipv6ExtRoute = _Ipv6ExtRoute_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 126, 24)
)
_Ipv6ExtRouteVal_Type = Counter64
_Ipv6ExtRouteVal_Object = MibScalar
ipv6ExtRouteVal = _Ipv6ExtRouteVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 126, 24, 1),
    _Ipv6ExtRouteVal_Type()
)
ipv6ExtRouteVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6ExtRouteVal.setStatus("current")
_Ipv6ExtRouteMom_Type = CounterBasedGauge64
_Ipv6ExtRouteMom_Object = MibScalar
ipv6ExtRouteMom = _Ipv6ExtRouteMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 126, 24, 2),
    _Ipv6ExtRouteMom_Type()
)
ipv6ExtRouteMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6ExtRouteMom.setStatus("current")
_Ipv6ExtRouteMax_Type = CounterBasedGauge64
_Ipv6ExtRouteMax_Object = MibScalar
ipv6ExtRouteMax = _Ipv6ExtRouteMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 126, 24, 3),
    _Ipv6ExtRouteMax_Type()
)
ipv6ExtRouteMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6ExtRouteMax.setStatus("current")
_Ipv6ExtInvl_ObjectIdentity = ObjectIdentity
ipv6ExtInvl = _Ipv6ExtInvl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 126, 25)
)
_Ipv6ExtInvlVal_Type = Counter64
_Ipv6ExtInvlVal_Object = MibScalar
ipv6ExtInvlVal = _Ipv6ExtInvlVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 126, 25, 1),
    _Ipv6ExtInvlVal_Type()
)
ipv6ExtInvlVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6ExtInvlVal.setStatus("current")
_Ipv6ExtInvlMom_Type = CounterBasedGauge64
_Ipv6ExtInvlMom_Object = MibScalar
ipv6ExtInvlMom = _Ipv6ExtInvlMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 126, 25, 2),
    _Ipv6ExtInvlMom_Type()
)
ipv6ExtInvlMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6ExtInvlMom.setStatus("current")
_Ipv6ExtInvlMax_Type = CounterBasedGauge64
_Ipv6ExtInvlMax_Object = MibScalar
ipv6ExtInvlMax = _Ipv6ExtInvlMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 126, 25, 3),
    _Ipv6ExtInvlMax_Type()
)
ipv6ExtInvlMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6ExtInvlMax.setStatus("current")
_Ipv6FragnentTimeout_ObjectIdentity = ObjectIdentity
ipv6FragnentTimeout = _Ipv6FragnentTimeout_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 126, 26)
)
_Ipv6FragnentTimeoutVal_Type = Counter64
_Ipv6FragnentTimeoutVal_Object = MibScalar
ipv6FragnentTimeoutVal = _Ipv6FragnentTimeoutVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 126, 26, 1),
    _Ipv6FragnentTimeoutVal_Type()
)
ipv6FragnentTimeoutVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6FragnentTimeoutVal.setStatus("current")
_Ipv6FragnentTimeoutMom_Type = CounterBasedGauge64
_Ipv6FragnentTimeoutMom_Object = MibScalar
ipv6FragnentTimeoutMom = _Ipv6FragnentTimeoutMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 126, 26, 2),
    _Ipv6FragnentTimeoutMom_Type()
)
ipv6FragnentTimeoutMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6FragnentTimeoutMom.setStatus("current")
_Ipv6FragnentTimeoutMax_Type = CounterBasedGauge64
_Ipv6FragnentTimeoutMax_Object = MibScalar
ipv6FragnentTimeoutMax = _Ipv6FragnentTimeoutMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 126, 26, 3),
    _Ipv6FragnentTimeoutMax_Type()
)
ipv6FragnentTimeoutMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6FragnentTimeoutMax.setStatus("current")
_Ipv6FragmentDrops_ObjectIdentity = ObjectIdentity
ipv6FragmentDrops = _Ipv6FragmentDrops_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 126, 27)
)
_Ipv6FragmentDropsVal_Type = Counter64
_Ipv6FragmentDropsVal_Object = MibScalar
ipv6FragmentDropsVal = _Ipv6FragmentDropsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 126, 27, 1),
    _Ipv6FragmentDropsVal_Type()
)
ipv6FragmentDropsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6FragmentDropsVal.setStatus("current")
_Ipv6FragmentDropsMom_Type = CounterBasedGauge64
_Ipv6FragmentDropsMom_Object = MibScalar
ipv6FragmentDropsMom = _Ipv6FragmentDropsMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 126, 27, 2),
    _Ipv6FragmentDropsMom_Type()
)
ipv6FragmentDropsMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6FragmentDropsMom.setStatus("current")
_Ipv6FragmentDropsMax_Type = CounterBasedGauge64
_Ipv6FragmentDropsMax_Object = MibScalar
ipv6FragmentDropsMax = _Ipv6FragmentDropsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 126, 27, 3),
    _Ipv6FragmentDropsMax_Type()
)
ipv6FragmentDropsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6FragmentDropsMax.setStatus("current")
_Ipv6ShuntAddressPackets_ObjectIdentity = ObjectIdentity
ipv6ShuntAddressPackets = _Ipv6ShuntAddressPackets_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 126, 28)
)
_Ipv6ShuntAddressPacketsVal_Type = Counter64
_Ipv6ShuntAddressPacketsVal_Object = MibScalar
ipv6ShuntAddressPacketsVal = _Ipv6ShuntAddressPacketsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 126, 28, 1),
    _Ipv6ShuntAddressPacketsVal_Type()
)
ipv6ShuntAddressPacketsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6ShuntAddressPacketsVal.setStatus("current")
_Ipv6ShuntAddressPacketsMom_Type = CounterBasedGauge64
_Ipv6ShuntAddressPacketsMom_Object = MibScalar
ipv6ShuntAddressPacketsMom = _Ipv6ShuntAddressPacketsMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 126, 28, 2),
    _Ipv6ShuntAddressPacketsMom_Type()
)
ipv6ShuntAddressPacketsMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6ShuntAddressPacketsMom.setStatus("current")
_Ipv6ShuntAddressPacketsMax_Type = CounterBasedGauge64
_Ipv6ShuntAddressPacketsMax_Object = MibScalar
ipv6ShuntAddressPacketsMax = _Ipv6ShuntAddressPacketsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 126, 28, 3),
    _Ipv6ShuntAddressPacketsMax_Type()
)
ipv6ShuntAddressPacketsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6ShuntAddressPacketsMax.setStatus("current")
_Ipv6ShuntAddressBytes_ObjectIdentity = ObjectIdentity
ipv6ShuntAddressBytes = _Ipv6ShuntAddressBytes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 126, 29)
)
_Ipv6ShuntAddressBytesVal_Type = Counter64
_Ipv6ShuntAddressBytesVal_Object = MibScalar
ipv6ShuntAddressBytesVal = _Ipv6ShuntAddressBytesVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 126, 29, 1),
    _Ipv6ShuntAddressBytesVal_Type()
)
ipv6ShuntAddressBytesVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6ShuntAddressBytesVal.setStatus("current")
_Ipv6ShuntAddressBytesMom_Type = CounterBasedGauge64
_Ipv6ShuntAddressBytesMom_Object = MibScalar
ipv6ShuntAddressBytesMom = _Ipv6ShuntAddressBytesMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 126, 29, 2),
    _Ipv6ShuntAddressBytesMom_Type()
)
ipv6ShuntAddressBytesMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6ShuntAddressBytesMom.setStatus("current")
_Ipv6ShuntAddressBytesMax_Type = CounterBasedGauge64
_Ipv6ShuntAddressBytesMax_Object = MibScalar
ipv6ShuntAddressBytesMax = _Ipv6ShuntAddressBytesMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 126, 29, 3),
    _Ipv6ShuntAddressBytesMax_Type()
)
ipv6ShuntAddressBytesMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6ShuntAddressBytesMax.setStatus("current")
_Ipv6ShuntProtoPackets_ObjectIdentity = ObjectIdentity
ipv6ShuntProtoPackets = _Ipv6ShuntProtoPackets_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 126, 30)
)
_Ipv6ShuntProtoPacketsVal_Type = Counter64
_Ipv6ShuntProtoPacketsVal_Object = MibScalar
ipv6ShuntProtoPacketsVal = _Ipv6ShuntProtoPacketsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 126, 30, 1),
    _Ipv6ShuntProtoPacketsVal_Type()
)
ipv6ShuntProtoPacketsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6ShuntProtoPacketsVal.setStatus("current")
_Ipv6ShuntProtoPacketsMom_Type = CounterBasedGauge64
_Ipv6ShuntProtoPacketsMom_Object = MibScalar
ipv6ShuntProtoPacketsMom = _Ipv6ShuntProtoPacketsMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 126, 30, 2),
    _Ipv6ShuntProtoPacketsMom_Type()
)
ipv6ShuntProtoPacketsMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6ShuntProtoPacketsMom.setStatus("current")
_Ipv6ShuntProtoPacketsMax_Type = CounterBasedGauge64
_Ipv6ShuntProtoPacketsMax_Object = MibScalar
ipv6ShuntProtoPacketsMax = _Ipv6ShuntProtoPacketsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 126, 30, 3),
    _Ipv6ShuntProtoPacketsMax_Type()
)
ipv6ShuntProtoPacketsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6ShuntProtoPacketsMax.setStatus("current")
_Ipv6ShuntProtoBytes_ObjectIdentity = ObjectIdentity
ipv6ShuntProtoBytes = _Ipv6ShuntProtoBytes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 126, 31)
)
_Ipv6ShuntProtoBytesVal_Type = Counter64
_Ipv6ShuntProtoBytesVal_Object = MibScalar
ipv6ShuntProtoBytesVal = _Ipv6ShuntProtoBytesVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 126, 31, 1),
    _Ipv6ShuntProtoBytesVal_Type()
)
ipv6ShuntProtoBytesVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6ShuntProtoBytesVal.setStatus("current")
_Ipv6ShuntProtoBytesMom_Type = CounterBasedGauge64
_Ipv6ShuntProtoBytesMom_Object = MibScalar
ipv6ShuntProtoBytesMom = _Ipv6ShuntProtoBytesMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 126, 31, 2),
    _Ipv6ShuntProtoBytesMom_Type()
)
ipv6ShuntProtoBytesMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6ShuntProtoBytesMom.setStatus("current")
_Ipv6ShuntProtoBytesMax_Type = CounterBasedGauge64
_Ipv6ShuntProtoBytesMax_Object = MibScalar
ipv6ShuntProtoBytesMax = _Ipv6ShuntProtoBytesMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 126, 31, 3),
    _Ipv6ShuntProtoBytesMax_Type()
)
ipv6ShuntProtoBytesMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6ShuntProtoBytesMax.setStatus("current")
_Ipv6FragInFrag_ObjectIdentity = ObjectIdentity
ipv6FragInFrag = _Ipv6FragInFrag_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 126, 32)
)
_Ipv6FragInFragVal_Type = Counter64
_Ipv6FragInFragVal_Object = MibScalar
ipv6FragInFragVal = _Ipv6FragInFragVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 126, 32, 1),
    _Ipv6FragInFragVal_Type()
)
ipv6FragInFragVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6FragInFragVal.setStatus("current")
_Ipv6FragInFragMom_Type = CounterBasedGauge64
_Ipv6FragInFragMom_Object = MibScalar
ipv6FragInFragMom = _Ipv6FragInFragMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 126, 32, 2),
    _Ipv6FragInFragMom_Type()
)
ipv6FragInFragMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6FragInFragMom.setStatus("current")
_Ipv6FragInFragMax_Type = CounterBasedGauge64
_Ipv6FragInFragMax_Object = MibScalar
ipv6FragInFragMax = _Ipv6FragInFragMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 126, 32, 3),
    _Ipv6FragInFragMax_Type()
)
ipv6FragInFragMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6FragInFragMax.setStatus("current")
_Ipv6EcnEct0_ObjectIdentity = ObjectIdentity
ipv6EcnEct0 = _Ipv6EcnEct0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 126, 33)
)
_Ipv6EcnEct0Val_Type = Counter64
_Ipv6EcnEct0Val_Object = MibScalar
ipv6EcnEct0Val = _Ipv6EcnEct0Val_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 126, 33, 1),
    _Ipv6EcnEct0Val_Type()
)
ipv6EcnEct0Val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6EcnEct0Val.setStatus("current")
_Ipv6EcnEct0Mom_Type = CounterBasedGauge64
_Ipv6EcnEct0Mom_Object = MibScalar
ipv6EcnEct0Mom = _Ipv6EcnEct0Mom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 126, 33, 2),
    _Ipv6EcnEct0Mom_Type()
)
ipv6EcnEct0Mom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6EcnEct0Mom.setStatus("current")
_Ipv6EcnEct0Max_Type = CounterBasedGauge64
_Ipv6EcnEct0Max_Object = MibScalar
ipv6EcnEct0Max = _Ipv6EcnEct0Max_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 126, 33, 3),
    _Ipv6EcnEct0Max_Type()
)
ipv6EcnEct0Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6EcnEct0Max.setStatus("current")
_Ipv6EcnEct1_ObjectIdentity = ObjectIdentity
ipv6EcnEct1 = _Ipv6EcnEct1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 126, 34)
)
_Ipv6EcnEct1Val_Type = Counter64
_Ipv6EcnEct1Val_Object = MibScalar
ipv6EcnEct1Val = _Ipv6EcnEct1Val_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 126, 34, 1),
    _Ipv6EcnEct1Val_Type()
)
ipv6EcnEct1Val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6EcnEct1Val.setStatus("current")
_Ipv6EcnEct1Mom_Type = CounterBasedGauge64
_Ipv6EcnEct1Mom_Object = MibScalar
ipv6EcnEct1Mom = _Ipv6EcnEct1Mom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 126, 34, 2),
    _Ipv6EcnEct1Mom_Type()
)
ipv6EcnEct1Mom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6EcnEct1Mom.setStatus("current")
_Ipv6EcnEct1Max_Type = CounterBasedGauge64
_Ipv6EcnEct1Max_Object = MibScalar
ipv6EcnEct1Max = _Ipv6EcnEct1Max_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 126, 34, 3),
    _Ipv6EcnEct1Max_Type()
)
ipv6EcnEct1Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6EcnEct1Max.setStatus("current")
_Ipv6EcnCn_ObjectIdentity = ObjectIdentity
ipv6EcnCn = _Ipv6EcnCn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 126, 35)
)
_Ipv6EcnCnVal_Type = Counter64
_Ipv6EcnCnVal_Object = MibScalar
ipv6EcnCnVal = _Ipv6EcnCnVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 126, 35, 1),
    _Ipv6EcnCnVal_Type()
)
ipv6EcnCnVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6EcnCnVal.setStatus("current")
_Ipv6EcnCnMom_Type = CounterBasedGauge64
_Ipv6EcnCnMom_Object = MibScalar
ipv6EcnCnMom = _Ipv6EcnCnMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 126, 35, 2),
    _Ipv6EcnCnMom_Type()
)
ipv6EcnCnMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6EcnCnMom.setStatus("current")
_Ipv6EcnCnMax_Type = CounterBasedGauge64
_Ipv6EcnCnMax_Object = MibScalar
ipv6EcnCnMax = _Ipv6EcnCnMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 126, 35, 3),
    _Ipv6EcnCnMax_Type()
)
ipv6EcnCnMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6EcnCnMax.setStatus("current")
_Tcpv6_ObjectIdentity = ObjectIdentity
tcpv6 = _Tcpv6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127)
)
_Tcpv6Packets_ObjectIdentity = ObjectIdentity
tcpv6Packets = _Tcpv6Packets_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 1)
)
_Tcpv6PacketsVal_Type = Counter64
_Tcpv6PacketsVal_Object = MibScalar
tcpv6PacketsVal = _Tcpv6PacketsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 1, 1),
    _Tcpv6PacketsVal_Type()
)
tcpv6PacketsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv6PacketsVal.setStatus("current")
_Tcpv6PacketsMom_Type = CounterBasedGauge64
_Tcpv6PacketsMom_Object = MibScalar
tcpv6PacketsMom = _Tcpv6PacketsMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 1, 2),
    _Tcpv6PacketsMom_Type()
)
tcpv6PacketsMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv6PacketsMom.setStatus("current")
_Tcpv6PacketsMax_Type = CounterBasedGauge64
_Tcpv6PacketsMax_Object = MibScalar
tcpv6PacketsMax = _Tcpv6PacketsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 1, 3),
    _Tcpv6PacketsMax_Type()
)
tcpv6PacketsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv6PacketsMax.setStatus("current")
_Tcpv6Bytes_ObjectIdentity = ObjectIdentity
tcpv6Bytes = _Tcpv6Bytes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 2)
)
_Tcpv6BytesVal_Type = Counter64
_Tcpv6BytesVal_Object = MibScalar
tcpv6BytesVal = _Tcpv6BytesVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 2, 1),
    _Tcpv6BytesVal_Type()
)
tcpv6BytesVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv6BytesVal.setStatus("current")
_Tcpv6BytesMom_Type = CounterBasedGauge64
_Tcpv6BytesMom_Object = MibScalar
tcpv6BytesMom = _Tcpv6BytesMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 2, 2),
    _Tcpv6BytesMom_Type()
)
tcpv6BytesMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv6BytesMom.setStatus("current")
_Tcpv6BytesMax_Type = CounterBasedGauge64
_Tcpv6BytesMax_Object = MibScalar
tcpv6BytesMax = _Tcpv6BytesMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 2, 3),
    _Tcpv6BytesMax_Type()
)
tcpv6BytesMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv6BytesMax.setStatus("current")
_Tcpv6CreateAttempts_ObjectIdentity = ObjectIdentity
tcpv6CreateAttempts = _Tcpv6CreateAttempts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 4)
)
_Tcpv6CreateAttemptsVal_Type = Counter64
_Tcpv6CreateAttemptsVal_Object = MibScalar
tcpv6CreateAttemptsVal = _Tcpv6CreateAttemptsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 4, 1),
    _Tcpv6CreateAttemptsVal_Type()
)
tcpv6CreateAttemptsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv6CreateAttemptsVal.setStatus("current")
_Tcpv6CreateAttemptsMom_Type = CounterBasedGauge64
_Tcpv6CreateAttemptsMom_Object = MibScalar
tcpv6CreateAttemptsMom = _Tcpv6CreateAttemptsMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 4, 2),
    _Tcpv6CreateAttemptsMom_Type()
)
tcpv6CreateAttemptsMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv6CreateAttemptsMom.setStatus("current")
_Tcpv6CreateAttemptsMax_Type = CounterBasedGauge64
_Tcpv6CreateAttemptsMax_Object = MibScalar
tcpv6CreateAttemptsMax = _Tcpv6CreateAttemptsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 4, 3),
    _Tcpv6CreateAttemptsMax_Type()
)
tcpv6CreateAttemptsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv6CreateAttemptsMax.setStatus("current")
_Tcpv6Created_ObjectIdentity = ObjectIdentity
tcpv6Created = _Tcpv6Created_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 5)
)
_Tcpv6CreatedVal_Type = Counter64
_Tcpv6CreatedVal_Object = MibScalar
tcpv6CreatedVal = _Tcpv6CreatedVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 5, 1),
    _Tcpv6CreatedVal_Type()
)
tcpv6CreatedVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv6CreatedVal.setStatus("current")
_Tcpv6CreatedMom_Type = CounterBasedGauge64
_Tcpv6CreatedMom_Object = MibScalar
tcpv6CreatedMom = _Tcpv6CreatedMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 5, 2),
    _Tcpv6CreatedMom_Type()
)
tcpv6CreatedMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv6CreatedMom.setStatus("current")
_Tcpv6CreatedMax_Type = CounterBasedGauge64
_Tcpv6CreatedMax_Object = MibScalar
tcpv6CreatedMax = _Tcpv6CreatedMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 5, 3),
    _Tcpv6CreatedMax_Type()
)
tcpv6CreatedMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv6CreatedMax.setStatus("current")
_Tcpv6RefusedRuleset_ObjectIdentity = ObjectIdentity
tcpv6RefusedRuleset = _Tcpv6RefusedRuleset_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 6)
)
_Tcpv6RefusedRulesetVal_Type = Counter64
_Tcpv6RefusedRulesetVal_Object = MibScalar
tcpv6RefusedRulesetVal = _Tcpv6RefusedRulesetVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 6, 1),
    _Tcpv6RefusedRulesetVal_Type()
)
tcpv6RefusedRulesetVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv6RefusedRulesetVal.setStatus("current")
_Tcpv6RefusedRulesetMom_Type = CounterBasedGauge64
_Tcpv6RefusedRulesetMom_Object = MibScalar
tcpv6RefusedRulesetMom = _Tcpv6RefusedRulesetMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 6, 2),
    _Tcpv6RefusedRulesetMom_Type()
)
tcpv6RefusedRulesetMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv6RefusedRulesetMom.setStatus("current")
_Tcpv6RefusedRulesetMax_Type = CounterBasedGauge64
_Tcpv6RefusedRulesetMax_Object = MibScalar
tcpv6RefusedRulesetMax = _Tcpv6RefusedRulesetMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 6, 3),
    _Tcpv6RefusedRulesetMax_Type()
)
tcpv6RefusedRulesetMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv6RefusedRulesetMax.setStatus("current")
_Tcpv6RefusedShort_ObjectIdentity = ObjectIdentity
tcpv6RefusedShort = _Tcpv6RefusedShort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 7)
)
_Tcpv6RefusedShortVal_Type = Counter64
_Tcpv6RefusedShortVal_Object = MibScalar
tcpv6RefusedShortVal = _Tcpv6RefusedShortVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 7, 1),
    _Tcpv6RefusedShortVal_Type()
)
tcpv6RefusedShortVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv6RefusedShortVal.setStatus("current")
_Tcpv6RefusedShortMom_Type = CounterBasedGauge64
_Tcpv6RefusedShortMom_Object = MibScalar
tcpv6RefusedShortMom = _Tcpv6RefusedShortMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 7, 2),
    _Tcpv6RefusedShortMom_Type()
)
tcpv6RefusedShortMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv6RefusedShortMom.setStatus("current")
_Tcpv6RefusedShortMax_Type = CounterBasedGauge64
_Tcpv6RefusedShortMax_Object = MibScalar
tcpv6RefusedShortMax = _Tcpv6RefusedShortMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 7, 3),
    _Tcpv6RefusedShortMax_Type()
)
tcpv6RefusedShortMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv6RefusedShortMax.setStatus("current")
_Tcpv6RefusedBroadcast_ObjectIdentity = ObjectIdentity
tcpv6RefusedBroadcast = _Tcpv6RefusedBroadcast_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 8)
)
_Tcpv6RefusedBroadcastVal_Type = Counter64
_Tcpv6RefusedBroadcastVal_Object = MibScalar
tcpv6RefusedBroadcastVal = _Tcpv6RefusedBroadcastVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 8, 1),
    _Tcpv6RefusedBroadcastVal_Type()
)
tcpv6RefusedBroadcastVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv6RefusedBroadcastVal.setStatus("current")
_Tcpv6RefusedBroadcastMom_Type = CounterBasedGauge64
_Tcpv6RefusedBroadcastMom_Object = MibScalar
tcpv6RefusedBroadcastMom = _Tcpv6RefusedBroadcastMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 8, 2),
    _Tcpv6RefusedBroadcastMom_Type()
)
tcpv6RefusedBroadcastMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv6RefusedBroadcastMom.setStatus("current")
_Tcpv6RefusedBroadcastMax_Type = CounterBasedGauge64
_Tcpv6RefusedBroadcastMax_Object = MibScalar
tcpv6RefusedBroadcastMax = _Tcpv6RefusedBroadcastMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 8, 3),
    _Tcpv6RefusedBroadcastMax_Type()
)
tcpv6RefusedBroadcastMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv6RefusedBroadcastMax.setStatus("current")
_Tcpv6RefusedOffset_ObjectIdentity = ObjectIdentity
tcpv6RefusedOffset = _Tcpv6RefusedOffset_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 9)
)
_Tcpv6RefusedOffsetVal_Type = Counter64
_Tcpv6RefusedOffsetVal_Object = MibScalar
tcpv6RefusedOffsetVal = _Tcpv6RefusedOffsetVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 9, 1),
    _Tcpv6RefusedOffsetVal_Type()
)
tcpv6RefusedOffsetVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv6RefusedOffsetVal.setStatus("current")
_Tcpv6RefusedOffsetMom_Type = CounterBasedGauge64
_Tcpv6RefusedOffsetMom_Object = MibScalar
tcpv6RefusedOffsetMom = _Tcpv6RefusedOffsetMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 9, 2),
    _Tcpv6RefusedOffsetMom_Type()
)
tcpv6RefusedOffsetMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv6RefusedOffsetMom.setStatus("current")
_Tcpv6RefusedOffsetMax_Type = CounterBasedGauge64
_Tcpv6RefusedOffsetMax_Object = MibScalar
tcpv6RefusedOffsetMax = _Tcpv6RefusedOffsetMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 9, 3),
    _Tcpv6RefusedOffsetMax_Type()
)
tcpv6RefusedOffsetMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv6RefusedOffsetMax.setStatus("current")
_Tcpv6Rejected_ObjectIdentity = ObjectIdentity
tcpv6Rejected = _Tcpv6Rejected_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 10)
)
_Tcpv6RejectedVal_Type = Counter64
_Tcpv6RejectedVal_Object = MibScalar
tcpv6RejectedVal = _Tcpv6RejectedVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 10, 1),
    _Tcpv6RejectedVal_Type()
)
tcpv6RejectedVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv6RejectedVal.setStatus("current")
_Tcpv6RejectedMom_Type = CounterBasedGauge64
_Tcpv6RejectedMom_Object = MibScalar
tcpv6RejectedMom = _Tcpv6RejectedMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 10, 2),
    _Tcpv6RejectedMom_Type()
)
tcpv6RejectedMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv6RejectedMom.setStatus("current")
_Tcpv6RejectedMax_Type = CounterBasedGauge64
_Tcpv6RejectedMax_Object = MibScalar
tcpv6RejectedMax = _Tcpv6RejectedMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 10, 3),
    _Tcpv6RejectedMax_Type()
)
tcpv6RejectedMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv6RejectedMax.setStatus("current")
_Tcpv6Lostsync_ObjectIdentity = ObjectIdentity
tcpv6Lostsync = _Tcpv6Lostsync_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 12)
)
_Tcpv6LostsyncVal_Type = CounterBasedGauge64
_Tcpv6LostsyncVal_Object = MibScalar
tcpv6LostsyncVal = _Tcpv6LostsyncVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 12, 1),
    _Tcpv6LostsyncVal_Type()
)
tcpv6LostsyncVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv6LostsyncVal.setStatus("current")
_Tcpv6LostsyncMax_Type = CounterBasedGauge64
_Tcpv6LostsyncMax_Object = MibScalar
tcpv6LostsyncMax = _Tcpv6LostsyncMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 12, 3),
    _Tcpv6LostsyncMax_Type()
)
tcpv6LostsyncMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv6LostsyncMax.setStatus("current")
_Tcpv6UntrackedPackets_ObjectIdentity = ObjectIdentity
tcpv6UntrackedPackets = _Tcpv6UntrackedPackets_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 13)
)
_Tcpv6UntrackedPacketsVal_Type = Counter64
_Tcpv6UntrackedPacketsVal_Object = MibScalar
tcpv6UntrackedPacketsVal = _Tcpv6UntrackedPacketsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 13, 1),
    _Tcpv6UntrackedPacketsVal_Type()
)
tcpv6UntrackedPacketsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv6UntrackedPacketsVal.setStatus("current")
_Tcpv6UntrackedPacketsMom_Type = CounterBasedGauge64
_Tcpv6UntrackedPacketsMom_Object = MibScalar
tcpv6UntrackedPacketsMom = _Tcpv6UntrackedPacketsMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 13, 2),
    _Tcpv6UntrackedPacketsMom_Type()
)
tcpv6UntrackedPacketsMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv6UntrackedPacketsMom.setStatus("current")
_Tcpv6UntrackedPacketsMax_Type = CounterBasedGauge64
_Tcpv6UntrackedPacketsMax_Object = MibScalar
tcpv6UntrackedPacketsMax = _Tcpv6UntrackedPacketsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 13, 3),
    _Tcpv6UntrackedPacketsMax_Type()
)
tcpv6UntrackedPacketsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv6UntrackedPacketsMax.setStatus("current")
_Tcpv6GoodputPackets_ObjectIdentity = ObjectIdentity
tcpv6GoodputPackets = _Tcpv6GoodputPackets_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 14)
)
_Tcpv6GoodputPacketsVal_Type = Counter64
_Tcpv6GoodputPacketsVal_Object = MibScalar
tcpv6GoodputPacketsVal = _Tcpv6GoodputPacketsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 14, 1),
    _Tcpv6GoodputPacketsVal_Type()
)
tcpv6GoodputPacketsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv6GoodputPacketsVal.setStatus("current")
_Tcpv6GoodputPacketsMom_Type = CounterBasedGauge64
_Tcpv6GoodputPacketsMom_Object = MibScalar
tcpv6GoodputPacketsMom = _Tcpv6GoodputPacketsMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 14, 2),
    _Tcpv6GoodputPacketsMom_Type()
)
tcpv6GoodputPacketsMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv6GoodputPacketsMom.setStatus("current")
_Tcpv6GoodputPacketsMax_Type = CounterBasedGauge64
_Tcpv6GoodputPacketsMax_Object = MibScalar
tcpv6GoodputPacketsMax = _Tcpv6GoodputPacketsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 14, 3),
    _Tcpv6GoodputPacketsMax_Type()
)
tcpv6GoodputPacketsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv6GoodputPacketsMax.setStatus("current")
_Tcpv6GoodputBytes_ObjectIdentity = ObjectIdentity
tcpv6GoodputBytes = _Tcpv6GoodputBytes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 15)
)
_Tcpv6GoodputBytesVal_Type = Counter64
_Tcpv6GoodputBytesVal_Object = MibScalar
tcpv6GoodputBytesVal = _Tcpv6GoodputBytesVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 15, 1),
    _Tcpv6GoodputBytesVal_Type()
)
tcpv6GoodputBytesVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv6GoodputBytesVal.setStatus("current")
_Tcpv6GoodputBytesMom_Type = CounterBasedGauge64
_Tcpv6GoodputBytesMom_Object = MibScalar
tcpv6GoodputBytesMom = _Tcpv6GoodputBytesMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 15, 2),
    _Tcpv6GoodputBytesMom_Type()
)
tcpv6GoodputBytesMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv6GoodputBytesMom.setStatus("current")
_Tcpv6GoodputBytesMax_Type = CounterBasedGauge64
_Tcpv6GoodputBytesMax_Object = MibScalar
tcpv6GoodputBytesMax = _Tcpv6GoodputBytesMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 15, 3),
    _Tcpv6GoodputBytesMax_Type()
)
tcpv6GoodputBytesMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv6GoodputBytesMax.setStatus("current")
_Tcpv6Segments_ObjectIdentity = ObjectIdentity
tcpv6Segments = _Tcpv6Segments_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 16)
)
_Tcpv6SegmentsVal_Type = CounterBasedGauge64
_Tcpv6SegmentsVal_Object = MibScalar
tcpv6SegmentsVal = _Tcpv6SegmentsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 16, 1),
    _Tcpv6SegmentsVal_Type()
)
tcpv6SegmentsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv6SegmentsVal.setStatus("current")
_Tcpv6SegmentsMax_Type = CounterBasedGauge64
_Tcpv6SegmentsMax_Object = MibScalar
tcpv6SegmentsMax = _Tcpv6SegmentsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 16, 3),
    _Tcpv6SegmentsMax_Type()
)
tcpv6SegmentsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv6SegmentsMax.setStatus("current")
_Tcpv6SegmentsPayload_ObjectIdentity = ObjectIdentity
tcpv6SegmentsPayload = _Tcpv6SegmentsPayload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 17)
)
_Tcpv6SegmentsPayloadVal_Type = CounterBasedGauge64
_Tcpv6SegmentsPayloadVal_Object = MibScalar
tcpv6SegmentsPayloadVal = _Tcpv6SegmentsPayloadVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 17, 1),
    _Tcpv6SegmentsPayloadVal_Type()
)
tcpv6SegmentsPayloadVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv6SegmentsPayloadVal.setStatus("current")
_Tcpv6SegmentsPayloadMax_Type = CounterBasedGauge64
_Tcpv6SegmentsPayloadMax_Object = MibScalar
tcpv6SegmentsPayloadMax = _Tcpv6SegmentsPayloadMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 17, 3),
    _Tcpv6SegmentsPayloadMax_Type()
)
tcpv6SegmentsPayloadMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv6SegmentsPayloadMax.setStatus("current")
_Tcpv6SegmentsDropped_ObjectIdentity = ObjectIdentity
tcpv6SegmentsDropped = _Tcpv6SegmentsDropped_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 18)
)
_Tcpv6SegmentsDroppedVal_Type = Counter64
_Tcpv6SegmentsDroppedVal_Object = MibScalar
tcpv6SegmentsDroppedVal = _Tcpv6SegmentsDroppedVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 18, 1),
    _Tcpv6SegmentsDroppedVal_Type()
)
tcpv6SegmentsDroppedVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv6SegmentsDroppedVal.setStatus("current")
_Tcpv6SegmentsDroppedMom_Type = CounterBasedGauge64
_Tcpv6SegmentsDroppedMom_Object = MibScalar
tcpv6SegmentsDroppedMom = _Tcpv6SegmentsDroppedMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 18, 2),
    _Tcpv6SegmentsDroppedMom_Type()
)
tcpv6SegmentsDroppedMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv6SegmentsDroppedMom.setStatus("current")
_Tcpv6SegmentsDroppedMax_Type = CounterBasedGauge64
_Tcpv6SegmentsDroppedMax_Object = MibScalar
tcpv6SegmentsDroppedMax = _Tcpv6SegmentsDroppedMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 18, 3),
    _Tcpv6SegmentsDroppedMax_Type()
)
tcpv6SegmentsDroppedMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv6SegmentsDroppedMax.setStatus("current")
_Tcpv6PacketAllocFail_ObjectIdentity = ObjectIdentity
tcpv6PacketAllocFail = _Tcpv6PacketAllocFail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 19)
)
_Tcpv6PacketAllocFailVal_Type = Counter64
_Tcpv6PacketAllocFailVal_Object = MibScalar
tcpv6PacketAllocFailVal = _Tcpv6PacketAllocFailVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 19, 1),
    _Tcpv6PacketAllocFailVal_Type()
)
tcpv6PacketAllocFailVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv6PacketAllocFailVal.setStatus("current")
_Tcpv6PacketAllocFailMom_Type = CounterBasedGauge64
_Tcpv6PacketAllocFailMom_Object = MibScalar
tcpv6PacketAllocFailMom = _Tcpv6PacketAllocFailMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 19, 2),
    _Tcpv6PacketAllocFailMom_Type()
)
tcpv6PacketAllocFailMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv6PacketAllocFailMom.setStatus("current")
_Tcpv6PacketAllocFailMax_Type = CounterBasedGauge64
_Tcpv6PacketAllocFailMax_Object = MibScalar
tcpv6PacketAllocFailMax = _Tcpv6PacketAllocFailMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 19, 3),
    _Tcpv6PacketAllocFailMax_Type()
)
tcpv6PacketAllocFailMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv6PacketAllocFailMax.setStatus("current")
_Tcpv6UntrackedGoodput_ObjectIdentity = ObjectIdentity
tcpv6UntrackedGoodput = _Tcpv6UntrackedGoodput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 23)
)
_Tcpv6UntrackedGoodputVal_Type = Counter64
_Tcpv6UntrackedGoodputVal_Object = MibScalar
tcpv6UntrackedGoodputVal = _Tcpv6UntrackedGoodputVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 23, 1),
    _Tcpv6UntrackedGoodputVal_Type()
)
tcpv6UntrackedGoodputVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv6UntrackedGoodputVal.setStatus("current")
_Tcpv6UntrackedGoodputMom_Type = CounterBasedGauge64
_Tcpv6UntrackedGoodputMom_Object = MibScalar
tcpv6UntrackedGoodputMom = _Tcpv6UntrackedGoodputMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 23, 2),
    _Tcpv6UntrackedGoodputMom_Type()
)
tcpv6UntrackedGoodputMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv6UntrackedGoodputMom.setStatus("current")
_Tcpv6UntrackedGoodputMax_Type = CounterBasedGauge64
_Tcpv6UntrackedGoodputMax_Object = MibScalar
tcpv6UntrackedGoodputMax = _Tcpv6UntrackedGoodputMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 23, 3),
    _Tcpv6UntrackedGoodputMax_Type()
)
tcpv6UntrackedGoodputMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv6UntrackedGoodputMax.setStatus("current")
_Tcpv6UntrackedBytes_ObjectIdentity = ObjectIdentity
tcpv6UntrackedBytes = _Tcpv6UntrackedBytes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 24)
)
_Tcpv6UntrackedBytesVal_Type = Counter64
_Tcpv6UntrackedBytesVal_Object = MibScalar
tcpv6UntrackedBytesVal = _Tcpv6UntrackedBytesVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 24, 1),
    _Tcpv6UntrackedBytesVal_Type()
)
tcpv6UntrackedBytesVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv6UntrackedBytesVal.setStatus("current")
_Tcpv6UntrackedBytesMom_Type = CounterBasedGauge64
_Tcpv6UntrackedBytesMom_Object = MibScalar
tcpv6UntrackedBytesMom = _Tcpv6UntrackedBytesMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 24, 2),
    _Tcpv6UntrackedBytesMom_Type()
)
tcpv6UntrackedBytesMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv6UntrackedBytesMom.setStatus("current")
_Tcpv6UntrackedBytesMax_Type = CounterBasedGauge64
_Tcpv6UntrackedBytesMax_Object = MibScalar
tcpv6UntrackedBytesMax = _Tcpv6UntrackedBytesMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 24, 3),
    _Tcpv6UntrackedBytesMax_Type()
)
tcpv6UntrackedBytesMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv6UntrackedBytesMax.setStatus("current")
_Tcpv6CorruptOptions_ObjectIdentity = ObjectIdentity
tcpv6CorruptOptions = _Tcpv6CorruptOptions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 25)
)
_Tcpv6CorruptOptionsVal_Type = Counter64
_Tcpv6CorruptOptionsVal_Object = MibScalar
tcpv6CorruptOptionsVal = _Tcpv6CorruptOptionsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 25, 1),
    _Tcpv6CorruptOptionsVal_Type()
)
tcpv6CorruptOptionsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv6CorruptOptionsVal.setStatus("current")
_Tcpv6CorruptOptionsMom_Type = CounterBasedGauge64
_Tcpv6CorruptOptionsMom_Object = MibScalar
tcpv6CorruptOptionsMom = _Tcpv6CorruptOptionsMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 25, 2),
    _Tcpv6CorruptOptionsMom_Type()
)
tcpv6CorruptOptionsMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv6CorruptOptionsMom.setStatus("current")
_Tcpv6CorruptOptionsMax_Type = CounterBasedGauge64
_Tcpv6CorruptOptionsMax_Object = MibScalar
tcpv6CorruptOptionsMax = _Tcpv6CorruptOptionsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 25, 3),
    _Tcpv6CorruptOptionsMax_Type()
)
tcpv6CorruptOptionsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv6CorruptOptionsMax.setStatus("current")
_Tcpv6CorruptConn_ObjectIdentity = ObjectIdentity
tcpv6CorruptConn = _Tcpv6CorruptConn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 26)
)
_Tcpv6CorruptConnVal_Type = Counter64
_Tcpv6CorruptConnVal_Object = MibScalar
tcpv6CorruptConnVal = _Tcpv6CorruptConnVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 26, 1),
    _Tcpv6CorruptConnVal_Type()
)
tcpv6CorruptConnVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv6CorruptConnVal.setStatus("current")
_Tcpv6CorruptConnMom_Type = CounterBasedGauge64
_Tcpv6CorruptConnMom_Object = MibScalar
tcpv6CorruptConnMom = _Tcpv6CorruptConnMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 26, 2),
    _Tcpv6CorruptConnMom_Type()
)
tcpv6CorruptConnMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv6CorruptConnMom.setStatus("current")
_Tcpv6CorruptConnMax_Type = CounterBasedGauge64
_Tcpv6CorruptConnMax_Object = MibScalar
tcpv6CorruptConnMax = _Tcpv6CorruptConnMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 26, 3),
    _Tcpv6CorruptConnMax_Type()
)
tcpv6CorruptConnMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv6CorruptConnMax.setStatus("current")
_Tcpv6SegmentedConnections_ObjectIdentity = ObjectIdentity
tcpv6SegmentedConnections = _Tcpv6SegmentedConnections_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 27)
)
_Tcpv6SegmentedConnectionsVal_Type = CounterBasedGauge64
_Tcpv6SegmentedConnectionsVal_Object = MibScalar
tcpv6SegmentedConnectionsVal = _Tcpv6SegmentedConnectionsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 27, 1),
    _Tcpv6SegmentedConnectionsVal_Type()
)
tcpv6SegmentedConnectionsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv6SegmentedConnectionsVal.setStatus("current")
_Tcpv6SegmentedConnectionsMax_Type = CounterBasedGauge64
_Tcpv6SegmentedConnectionsMax_Object = MibScalar
tcpv6SegmentedConnectionsMax = _Tcpv6SegmentedConnectionsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 27, 3),
    _Tcpv6SegmentedConnectionsMax_Type()
)
tcpv6SegmentedConnectionsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv6SegmentedConnectionsMax.setStatus("current")
_Tcpv6OutOfWindowPackets_ObjectIdentity = ObjectIdentity
tcpv6OutOfWindowPackets = _Tcpv6OutOfWindowPackets_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 28)
)
_Tcpv6OutOfWindowPacketsVal_Type = Counter64
_Tcpv6OutOfWindowPacketsVal_Object = MibScalar
tcpv6OutOfWindowPacketsVal = _Tcpv6OutOfWindowPacketsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 28, 1),
    _Tcpv6OutOfWindowPacketsVal_Type()
)
tcpv6OutOfWindowPacketsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv6OutOfWindowPacketsVal.setStatus("current")
_Tcpv6OutOfWindowPacketsMom_Type = CounterBasedGauge64
_Tcpv6OutOfWindowPacketsMom_Object = MibScalar
tcpv6OutOfWindowPacketsMom = _Tcpv6OutOfWindowPacketsMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 28, 2),
    _Tcpv6OutOfWindowPacketsMom_Type()
)
tcpv6OutOfWindowPacketsMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv6OutOfWindowPacketsMom.setStatus("current")
_Tcpv6OutOfWindowPacketsMax_Type = CounterBasedGauge64
_Tcpv6OutOfWindowPacketsMax_Object = MibScalar
tcpv6OutOfWindowPacketsMax = _Tcpv6OutOfWindowPacketsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 28, 3),
    _Tcpv6OutOfWindowPacketsMax_Type()
)
tcpv6OutOfWindowPacketsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv6OutOfWindowPacketsMax.setStatus("current")
_Tcpv6RefusedFilter_ObjectIdentity = ObjectIdentity
tcpv6RefusedFilter = _Tcpv6RefusedFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 29)
)
_Tcpv6RefusedFilterVal_Type = Counter64
_Tcpv6RefusedFilterVal_Object = MibScalar
tcpv6RefusedFilterVal = _Tcpv6RefusedFilterVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 29, 1),
    _Tcpv6RefusedFilterVal_Type()
)
tcpv6RefusedFilterVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv6RefusedFilterVal.setStatus("current")
_Tcpv6RefusedFilterMom_Type = CounterBasedGauge64
_Tcpv6RefusedFilterMom_Object = MibScalar
tcpv6RefusedFilterMom = _Tcpv6RefusedFilterMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 29, 2),
    _Tcpv6RefusedFilterMom_Type()
)
tcpv6RefusedFilterMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv6RefusedFilterMom.setStatus("current")
_Tcpv6RefusedFilterMax_Type = CounterBasedGauge64
_Tcpv6RefusedFilterMax_Object = MibScalar
tcpv6RefusedFilterMax = _Tcpv6RefusedFilterMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 29, 3),
    _Tcpv6RefusedFilterMax_Type()
)
tcpv6RefusedFilterMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv6RefusedFilterMax.setStatus("current")
_Tcpv6SynExisting_ObjectIdentity = ObjectIdentity
tcpv6SynExisting = _Tcpv6SynExisting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 32)
)
_Tcpv6SynExistingVal_Type = Counter64
_Tcpv6SynExistingVal_Object = MibScalar
tcpv6SynExistingVal = _Tcpv6SynExistingVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 32, 1),
    _Tcpv6SynExistingVal_Type()
)
tcpv6SynExistingVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv6SynExistingVal.setStatus("current")
_Tcpv6SynExistingMom_Type = CounterBasedGauge64
_Tcpv6SynExistingMom_Object = MibScalar
tcpv6SynExistingMom = _Tcpv6SynExistingMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 32, 2),
    _Tcpv6SynExistingMom_Type()
)
tcpv6SynExistingMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv6SynExistingMom.setStatus("current")
_Tcpv6SynExistingMax_Type = CounterBasedGauge64
_Tcpv6SynExistingMax_Object = MibScalar
tcpv6SynExistingMax = _Tcpv6SynExistingMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 32, 3),
    _Tcpv6SynExistingMax_Type()
)
tcpv6SynExistingMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv6SynExistingMax.setStatus("current")
_Tcpv6SegmentAllocFail_ObjectIdentity = ObjectIdentity
tcpv6SegmentAllocFail = _Tcpv6SegmentAllocFail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 33)
)
_Tcpv6SegmentAllocFailVal_Type = Counter64
_Tcpv6SegmentAllocFailVal_Object = MibScalar
tcpv6SegmentAllocFailVal = _Tcpv6SegmentAllocFailVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 33, 1),
    _Tcpv6SegmentAllocFailVal_Type()
)
tcpv6SegmentAllocFailVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv6SegmentAllocFailVal.setStatus("current")
_Tcpv6SegmentAllocFailMom_Type = CounterBasedGauge64
_Tcpv6SegmentAllocFailMom_Object = MibScalar
tcpv6SegmentAllocFailMom = _Tcpv6SegmentAllocFailMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 33, 2),
    _Tcpv6SegmentAllocFailMom_Type()
)
tcpv6SegmentAllocFailMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv6SegmentAllocFailMom.setStatus("current")
_Tcpv6SegmentAllocFailMax_Type = CounterBasedGauge64
_Tcpv6SegmentAllocFailMax_Object = MibScalar
tcpv6SegmentAllocFailMax = _Tcpv6SegmentAllocFailMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 33, 3),
    _Tcpv6SegmentAllocFailMax_Type()
)
tcpv6SegmentAllocFailMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv6SegmentAllocFailMax.setStatus("current")
_Tcpv6EnqueuedSegments_ObjectIdentity = ObjectIdentity
tcpv6EnqueuedSegments = _Tcpv6EnqueuedSegments_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 34)
)
_Tcpv6EnqueuedSegmentsVal_Type = Counter64
_Tcpv6EnqueuedSegmentsVal_Object = MibScalar
tcpv6EnqueuedSegmentsVal = _Tcpv6EnqueuedSegmentsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 34, 1),
    _Tcpv6EnqueuedSegmentsVal_Type()
)
tcpv6EnqueuedSegmentsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv6EnqueuedSegmentsVal.setStatus("current")
_Tcpv6EnqueuedSegmentsMom_Type = CounterBasedGauge64
_Tcpv6EnqueuedSegmentsMom_Object = MibScalar
tcpv6EnqueuedSegmentsMom = _Tcpv6EnqueuedSegmentsMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 34, 2),
    _Tcpv6EnqueuedSegmentsMom_Type()
)
tcpv6EnqueuedSegmentsMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv6EnqueuedSegmentsMom.setStatus("current")
_Tcpv6EnqueuedSegmentsMax_Type = CounterBasedGauge64
_Tcpv6EnqueuedSegmentsMax_Object = MibScalar
tcpv6EnqueuedSegmentsMax = _Tcpv6EnqueuedSegmentsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 34, 3),
    _Tcpv6EnqueuedSegmentsMax_Type()
)
tcpv6EnqueuedSegmentsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv6EnqueuedSegmentsMax.setStatus("current")
_Tcpv6DequeuedSegments_ObjectIdentity = ObjectIdentity
tcpv6DequeuedSegments = _Tcpv6DequeuedSegments_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 35)
)
_Tcpv6DequeuedSegmentsVal_Type = Counter64
_Tcpv6DequeuedSegmentsVal_Object = MibScalar
tcpv6DequeuedSegmentsVal = _Tcpv6DequeuedSegmentsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 35, 1),
    _Tcpv6DequeuedSegmentsVal_Type()
)
tcpv6DequeuedSegmentsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv6DequeuedSegmentsVal.setStatus("current")
_Tcpv6DequeuedSegmentsMom_Type = CounterBasedGauge64
_Tcpv6DequeuedSegmentsMom_Object = MibScalar
tcpv6DequeuedSegmentsMom = _Tcpv6DequeuedSegmentsMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 35, 2),
    _Tcpv6DequeuedSegmentsMom_Type()
)
tcpv6DequeuedSegmentsMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv6DequeuedSegmentsMom.setStatus("current")
_Tcpv6DequeuedSegmentsMax_Type = CounterBasedGauge64
_Tcpv6DequeuedSegmentsMax_Object = MibScalar
tcpv6DequeuedSegmentsMax = _Tcpv6DequeuedSegmentsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 35, 3),
    _Tcpv6DequeuedSegmentsMax_Type()
)
tcpv6DequeuedSegmentsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv6DequeuedSegmentsMax.setStatus("current")
_Tcpv6DiscardedSegments_ObjectIdentity = ObjectIdentity
tcpv6DiscardedSegments = _Tcpv6DiscardedSegments_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 36)
)
_Tcpv6DiscardedSegmentsVal_Type = Counter64
_Tcpv6DiscardedSegmentsVal_Object = MibScalar
tcpv6DiscardedSegmentsVal = _Tcpv6DiscardedSegmentsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 36, 1),
    _Tcpv6DiscardedSegmentsVal_Type()
)
tcpv6DiscardedSegmentsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv6DiscardedSegmentsVal.setStatus("current")
_Tcpv6DiscardedSegmentsMom_Type = CounterBasedGauge64
_Tcpv6DiscardedSegmentsMom_Object = MibScalar
tcpv6DiscardedSegmentsMom = _Tcpv6DiscardedSegmentsMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 36, 2),
    _Tcpv6DiscardedSegmentsMom_Type()
)
tcpv6DiscardedSegmentsMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv6DiscardedSegmentsMom.setStatus("current")
_Tcpv6DiscardedSegmentsMax_Type = CounterBasedGauge64
_Tcpv6DiscardedSegmentsMax_Object = MibScalar
tcpv6DiscardedSegmentsMax = _Tcpv6DiscardedSegmentsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 36, 3),
    _Tcpv6DiscardedSegmentsMax_Type()
)
tcpv6DiscardedSegmentsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv6DiscardedSegmentsMax.setStatus("current")
_Tcpv6EmptyPackets_ObjectIdentity = ObjectIdentity
tcpv6EmptyPackets = _Tcpv6EmptyPackets_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 37)
)
_Tcpv6EmptyPacketsVal_Type = Counter64
_Tcpv6EmptyPacketsVal_Object = MibScalar
tcpv6EmptyPacketsVal = _Tcpv6EmptyPacketsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 37, 1),
    _Tcpv6EmptyPacketsVal_Type()
)
tcpv6EmptyPacketsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv6EmptyPacketsVal.setStatus("current")
_Tcpv6EmptyPacketsMom_Type = CounterBasedGauge64
_Tcpv6EmptyPacketsMom_Object = MibScalar
tcpv6EmptyPacketsMom = _Tcpv6EmptyPacketsMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 37, 2),
    _Tcpv6EmptyPacketsMom_Type()
)
tcpv6EmptyPacketsMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv6EmptyPacketsMom.setStatus("current")
_Tcpv6EmptyPacketsMax_Type = CounterBasedGauge64
_Tcpv6EmptyPacketsMax_Object = MibScalar
tcpv6EmptyPacketsMax = _Tcpv6EmptyPacketsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 37, 3),
    _Tcpv6EmptyPacketsMax_Type()
)
tcpv6EmptyPacketsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv6EmptyPacketsMax.setStatus("current")
_Tcpv6OosPackets_ObjectIdentity = ObjectIdentity
tcpv6OosPackets = _Tcpv6OosPackets_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 38)
)
_Tcpv6OosPacketsVal_Type = Counter64
_Tcpv6OosPacketsVal_Object = MibScalar
tcpv6OosPacketsVal = _Tcpv6OosPacketsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 38, 1),
    _Tcpv6OosPacketsVal_Type()
)
tcpv6OosPacketsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv6OosPacketsVal.setStatus("current")
_Tcpv6OosPacketsMom_Type = CounterBasedGauge64
_Tcpv6OosPacketsMom_Object = MibScalar
tcpv6OosPacketsMom = _Tcpv6OosPacketsMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 38, 2),
    _Tcpv6OosPacketsMom_Type()
)
tcpv6OosPacketsMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv6OosPacketsMom.setStatus("current")
_Tcpv6OosPacketsMax_Type = CounterBasedGauge64
_Tcpv6OosPacketsMax_Object = MibScalar
tcpv6OosPacketsMax = _Tcpv6OosPacketsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 38, 3),
    _Tcpv6OosPacketsMax_Type()
)
tcpv6OosPacketsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv6OosPacketsMax.setStatus("current")
_Tcpv6OosBytes_ObjectIdentity = ObjectIdentity
tcpv6OosBytes = _Tcpv6OosBytes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 39)
)
_Tcpv6OosBytesVal_Type = Counter64
_Tcpv6OosBytesVal_Object = MibScalar
tcpv6OosBytesVal = _Tcpv6OosBytesVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 39, 1),
    _Tcpv6OosBytesVal_Type()
)
tcpv6OosBytesVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv6OosBytesVal.setStatus("current")
_Tcpv6OosBytesMom_Type = CounterBasedGauge64
_Tcpv6OosBytesMom_Object = MibScalar
tcpv6OosBytesMom = _Tcpv6OosBytesMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 39, 2),
    _Tcpv6OosBytesMom_Type()
)
tcpv6OosBytesMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv6OosBytesMom.setStatus("current")
_Tcpv6OosBytesMax_Type = CounterBasedGauge64
_Tcpv6OosBytesMax_Object = MibScalar
tcpv6OosBytesMax = _Tcpv6OosBytesMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 39, 3),
    _Tcpv6OosBytesMax_Type()
)
tcpv6OosBytesMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv6OosBytesMax.setStatus("current")
_Tcpv6Retransmits_ObjectIdentity = ObjectIdentity
tcpv6Retransmits = _Tcpv6Retransmits_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 40)
)
_Tcpv6RetransmitsVal_Type = Counter64
_Tcpv6RetransmitsVal_Object = MibScalar
tcpv6RetransmitsVal = _Tcpv6RetransmitsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 40, 1),
    _Tcpv6RetransmitsVal_Type()
)
tcpv6RetransmitsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv6RetransmitsVal.setStatus("current")
_Tcpv6RetransmitsMom_Type = CounterBasedGauge64
_Tcpv6RetransmitsMom_Object = MibScalar
tcpv6RetransmitsMom = _Tcpv6RetransmitsMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 40, 2),
    _Tcpv6RetransmitsMom_Type()
)
tcpv6RetransmitsMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv6RetransmitsMom.setStatus("current")
_Tcpv6RetransmitsMax_Type = CounterBasedGauge64
_Tcpv6RetransmitsMax_Object = MibScalar
tcpv6RetransmitsMax = _Tcpv6RetransmitsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 40, 3),
    _Tcpv6RetransmitsMax_Type()
)
tcpv6RetransmitsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv6RetransmitsMax.setStatus("current")
_Tcpv6Cwr_ObjectIdentity = ObjectIdentity
tcpv6Cwr = _Tcpv6Cwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 41)
)
_Tcpv6CwrVal_Type = Counter64
_Tcpv6CwrVal_Object = MibScalar
tcpv6CwrVal = _Tcpv6CwrVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 41, 1),
    _Tcpv6CwrVal_Type()
)
tcpv6CwrVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv6CwrVal.setStatus("current")
_Tcpv6CwrMom_Type = CounterBasedGauge64
_Tcpv6CwrMom_Object = MibScalar
tcpv6CwrMom = _Tcpv6CwrMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 41, 2),
    _Tcpv6CwrMom_Type()
)
tcpv6CwrMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv6CwrMom.setStatus("current")
_Tcpv6CwrMax_Type = CounterBasedGauge64
_Tcpv6CwrMax_Object = MibScalar
tcpv6CwrMax = _Tcpv6CwrMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 41, 3),
    _Tcpv6CwrMax_Type()
)
tcpv6CwrMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv6CwrMax.setStatus("current")
_Tcpv6Ecne_ObjectIdentity = ObjectIdentity
tcpv6Ecne = _Tcpv6Ecne_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 42)
)
_Tcpv6EcneVal_Type = Counter64
_Tcpv6EcneVal_Object = MibScalar
tcpv6EcneVal = _Tcpv6EcneVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 42, 1),
    _Tcpv6EcneVal_Type()
)
tcpv6EcneVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv6EcneVal.setStatus("current")
_Tcpv6EcneMom_Type = CounterBasedGauge64
_Tcpv6EcneMom_Object = MibScalar
tcpv6EcneMom = _Tcpv6EcneMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 42, 2),
    _Tcpv6EcneMom_Type()
)
tcpv6EcneMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv6EcneMom.setStatus("current")
_Tcpv6EcneMax_Type = CounterBasedGauge64
_Tcpv6EcneMax_Object = MibScalar
tcpv6EcneMax = _Tcpv6EcneMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 42, 3),
    _Tcpv6EcneMax_Type()
)
tcpv6EcneMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv6EcneMax.setStatus("current")
_Tcpv6SimOpen_ObjectIdentity = ObjectIdentity
tcpv6SimOpen = _Tcpv6SimOpen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 43)
)
_Tcpv6SimOpenVal_Type = Counter64
_Tcpv6SimOpenVal_Object = MibScalar
tcpv6SimOpenVal = _Tcpv6SimOpenVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 43, 1),
    _Tcpv6SimOpenVal_Type()
)
tcpv6SimOpenVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv6SimOpenVal.setStatus("current")
_Tcpv6SimOpenMom_Type = CounterBasedGauge64
_Tcpv6SimOpenMom_Object = MibScalar
tcpv6SimOpenMom = _Tcpv6SimOpenMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 43, 2),
    _Tcpv6SimOpenMom_Type()
)
tcpv6SimOpenMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv6SimOpenMom.setStatus("current")
_Tcpv6SimOpenMax_Type = CounterBasedGauge64
_Tcpv6SimOpenMax_Object = MibScalar
tcpv6SimOpenMax = _Tcpv6SimOpenMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 127, 43, 3),
    _Tcpv6SimOpenMax_Type()
)
tcpv6SimOpenMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpv6SimOpenMax.setStatus("current")
_Teredo_ObjectIdentity = ObjectIdentity
teredo = _Teredo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 128)
)
_TeredoPackets_ObjectIdentity = ObjectIdentity
teredoPackets = _TeredoPackets_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 128, 2)
)
_TeredoPacketsVal_Type = Counter64
_TeredoPacketsVal_Object = MibScalar
teredoPacketsVal = _TeredoPacketsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 128, 2, 1),
    _TeredoPacketsVal_Type()
)
teredoPacketsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teredoPacketsVal.setStatus("current")
_TeredoPacketsMom_Type = CounterBasedGauge64
_TeredoPacketsMom_Object = MibScalar
teredoPacketsMom = _TeredoPacketsMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 128, 2, 2),
    _TeredoPacketsMom_Type()
)
teredoPacketsMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teredoPacketsMom.setStatus("current")
_TeredoPacketsMax_Type = CounterBasedGauge64
_TeredoPacketsMax_Object = MibScalar
teredoPacketsMax = _TeredoPacketsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 128, 2, 3),
    _TeredoPacketsMax_Type()
)
teredoPacketsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teredoPacketsMax.setStatus("current")
_TeredoBytes_ObjectIdentity = ObjectIdentity
teredoBytes = _TeredoBytes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 128, 3)
)
_TeredoBytesVal_Type = Counter64
_TeredoBytesVal_Object = MibScalar
teredoBytesVal = _TeredoBytesVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 128, 3, 1),
    _TeredoBytesVal_Type()
)
teredoBytesVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teredoBytesVal.setStatus("current")
_TeredoBytesMom_Type = CounterBasedGauge64
_TeredoBytesMom_Object = MibScalar
teredoBytesMom = _TeredoBytesMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 128, 3, 2),
    _TeredoBytesMom_Type()
)
teredoBytesMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teredoBytesMom.setStatus("current")
_TeredoBytesMax_Type = CounterBasedGauge64
_TeredoBytesMax_Object = MibScalar
teredoBytesMax = _TeredoBytesMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 128, 3, 3),
    _TeredoBytesMax_Type()
)
teredoBytesMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teredoBytesMax.setStatus("current")
_TeredoOrgHeaders_ObjectIdentity = ObjectIdentity
teredoOrgHeaders = _TeredoOrgHeaders_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 128, 4)
)
_TeredoOrgHeadersVal_Type = Counter64
_TeredoOrgHeadersVal_Object = MibScalar
teredoOrgHeadersVal = _TeredoOrgHeadersVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 128, 4, 1),
    _TeredoOrgHeadersVal_Type()
)
teredoOrgHeadersVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teredoOrgHeadersVal.setStatus("current")
_TeredoOrgHeadersMom_Type = CounterBasedGauge64
_TeredoOrgHeadersMom_Object = MibScalar
teredoOrgHeadersMom = _TeredoOrgHeadersMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 128, 4, 2),
    _TeredoOrgHeadersMom_Type()
)
teredoOrgHeadersMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teredoOrgHeadersMom.setStatus("current")
_TeredoOrgHeadersMax_Type = CounterBasedGauge64
_TeredoOrgHeadersMax_Object = MibScalar
teredoOrgHeadersMax = _TeredoOrgHeadersMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 128, 4, 3),
    _TeredoOrgHeadersMax_Type()
)
teredoOrgHeadersMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teredoOrgHeadersMax.setStatus("current")
_TeredoAuthHeaders_ObjectIdentity = ObjectIdentity
teredoAuthHeaders = _TeredoAuthHeaders_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 128, 5)
)
_TeredoAuthHeadersVal_Type = Counter64
_TeredoAuthHeadersVal_Object = MibScalar
teredoAuthHeadersVal = _TeredoAuthHeadersVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 128, 5, 1),
    _TeredoAuthHeadersVal_Type()
)
teredoAuthHeadersVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teredoAuthHeadersVal.setStatus("current")
_TeredoAuthHeadersMom_Type = CounterBasedGauge64
_TeredoAuthHeadersMom_Object = MibScalar
teredoAuthHeadersMom = _TeredoAuthHeadersMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 128, 5, 2),
    _TeredoAuthHeadersMom_Type()
)
teredoAuthHeadersMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teredoAuthHeadersMom.setStatus("current")
_TeredoAuthHeadersMax_Type = CounterBasedGauge64
_TeredoAuthHeadersMax_Object = MibScalar
teredoAuthHeadersMax = _TeredoAuthHeadersMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 128, 5, 3),
    _TeredoAuthHeadersMax_Type()
)
teredoAuthHeadersMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teredoAuthHeadersMax.setStatus("current")
_TeredoFrags_ObjectIdentity = ObjectIdentity
teredoFrags = _TeredoFrags_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 128, 6)
)
_TeredoFragsVal_Type = Counter64
_TeredoFragsVal_Object = MibScalar
teredoFragsVal = _TeredoFragsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 128, 6, 1),
    _TeredoFragsVal_Type()
)
teredoFragsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teredoFragsVal.setStatus("current")
_TeredoFragsMom_Type = CounterBasedGauge64
_TeredoFragsMom_Object = MibScalar
teredoFragsMom = _TeredoFragsMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 128, 6, 2),
    _TeredoFragsMom_Type()
)
teredoFragsMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teredoFragsMom.setStatus("current")
_TeredoFragsMax_Type = CounterBasedGauge64
_TeredoFragsMax_Object = MibScalar
teredoFragsMax = _TeredoFragsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 128, 6, 3),
    _TeredoFragsMax_Type()
)
teredoFragsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teredoFragsMax.setStatus("current")
_Gtp_ObjectIdentity = ObjectIdentity
gtp = _Gtp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 129)
)
_GtpPackets_ObjectIdentity = ObjectIdentity
gtpPackets = _GtpPackets_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 129, 2)
)
_GtpPacketsVal_Type = Counter64
_GtpPacketsVal_Object = MibScalar
gtpPacketsVal = _GtpPacketsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 129, 2, 1),
    _GtpPacketsVal_Type()
)
gtpPacketsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtpPacketsVal.setStatus("current")
_GtpPacketsMom_Type = CounterBasedGauge64
_GtpPacketsMom_Object = MibScalar
gtpPacketsMom = _GtpPacketsMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 129, 2, 2),
    _GtpPacketsMom_Type()
)
gtpPacketsMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtpPacketsMom.setStatus("current")
_GtpPacketsMax_Type = CounterBasedGauge64
_GtpPacketsMax_Object = MibScalar
gtpPacketsMax = _GtpPacketsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 129, 2, 3),
    _GtpPacketsMax_Type()
)
gtpPacketsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtpPacketsMax.setStatus("current")
_GtpBytes_ObjectIdentity = ObjectIdentity
gtpBytes = _GtpBytes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 129, 3)
)
_GtpBytesVal_Type = Counter64
_GtpBytesVal_Object = MibScalar
gtpBytesVal = _GtpBytesVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 129, 3, 1),
    _GtpBytesVal_Type()
)
gtpBytesVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtpBytesVal.setStatus("current")
_GtpBytesMom_Type = CounterBasedGauge64
_GtpBytesMom_Object = MibScalar
gtpBytesMom = _GtpBytesMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 129, 3, 2),
    _GtpBytesMom_Type()
)
gtpBytesMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtpBytesMom.setStatus("current")
_GtpBytesMax_Type = CounterBasedGauge64
_GtpBytesMax_Object = MibScalar
gtpBytesMax = _GtpBytesMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 129, 3, 3),
    _GtpBytesMax_Type()
)
gtpBytesMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtpBytesMax.setStatus("current")
_GtpGpdus_ObjectIdentity = ObjectIdentity
gtpGpdus = _GtpGpdus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 129, 4)
)
_GtpGpdusVal_Type = Counter64
_GtpGpdusVal_Object = MibScalar
gtpGpdusVal = _GtpGpdusVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 129, 4, 1),
    _GtpGpdusVal_Type()
)
gtpGpdusVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtpGpdusVal.setStatus("current")
_GtpGpdusMom_Type = CounterBasedGauge64
_GtpGpdusMom_Object = MibScalar
gtpGpdusMom = _GtpGpdusMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 129, 4, 2),
    _GtpGpdusMom_Type()
)
gtpGpdusMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtpGpdusMom.setStatus("current")
_GtpGpdusMax_Type = CounterBasedGauge64
_GtpGpdusMax_Object = MibScalar
gtpGpdusMax = _GtpGpdusMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 129, 4, 3),
    _GtpGpdusMax_Type()
)
gtpGpdusMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtpGpdusMax.setStatus("current")
_GtpCreatePdpReq_ObjectIdentity = ObjectIdentity
gtpCreatePdpReq = _GtpCreatePdpReq_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 129, 5)
)
_GtpCreatePdpReqVal_Type = Counter64
_GtpCreatePdpReqVal_Object = MibScalar
gtpCreatePdpReqVal = _GtpCreatePdpReqVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 129, 5, 1),
    _GtpCreatePdpReqVal_Type()
)
gtpCreatePdpReqVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtpCreatePdpReqVal.setStatus("current")
_GtpCreatePdpReqMom_Type = CounterBasedGauge64
_GtpCreatePdpReqMom_Object = MibScalar
gtpCreatePdpReqMom = _GtpCreatePdpReqMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 129, 5, 2),
    _GtpCreatePdpReqMom_Type()
)
gtpCreatePdpReqMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtpCreatePdpReqMom.setStatus("current")
_GtpCreatePdpReqMax_Type = CounterBasedGauge64
_GtpCreatePdpReqMax_Object = MibScalar
gtpCreatePdpReqMax = _GtpCreatePdpReqMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 129, 5, 3),
    _GtpCreatePdpReqMax_Type()
)
gtpCreatePdpReqMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtpCreatePdpReqMax.setStatus("current")
_GtpCreatePdpRsp_ObjectIdentity = ObjectIdentity
gtpCreatePdpRsp = _GtpCreatePdpRsp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 129, 6)
)
_GtpCreatePdpRspVal_Type = Counter64
_GtpCreatePdpRspVal_Object = MibScalar
gtpCreatePdpRspVal = _GtpCreatePdpRspVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 129, 6, 1),
    _GtpCreatePdpRspVal_Type()
)
gtpCreatePdpRspVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtpCreatePdpRspVal.setStatus("current")
_GtpCreatePdpRspMom_Type = CounterBasedGauge64
_GtpCreatePdpRspMom_Object = MibScalar
gtpCreatePdpRspMom = _GtpCreatePdpRspMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 129, 6, 2),
    _GtpCreatePdpRspMom_Type()
)
gtpCreatePdpRspMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtpCreatePdpRspMom.setStatus("current")
_GtpCreatePdpRspMax_Type = CounterBasedGauge64
_GtpCreatePdpRspMax_Object = MibScalar
gtpCreatePdpRspMax = _GtpCreatePdpRspMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 129, 6, 3),
    _GtpCreatePdpRspMax_Type()
)
gtpCreatePdpRspMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtpCreatePdpRspMax.setStatus("current")
_GtpDeletePdpReq_ObjectIdentity = ObjectIdentity
gtpDeletePdpReq = _GtpDeletePdpReq_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 129, 7)
)
_GtpDeletePdpReqVal_Type = Counter64
_GtpDeletePdpReqVal_Object = MibScalar
gtpDeletePdpReqVal = _GtpDeletePdpReqVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 129, 7, 1),
    _GtpDeletePdpReqVal_Type()
)
gtpDeletePdpReqVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtpDeletePdpReqVal.setStatus("current")
_GtpDeletePdpReqMom_Type = CounterBasedGauge64
_GtpDeletePdpReqMom_Object = MibScalar
gtpDeletePdpReqMom = _GtpDeletePdpReqMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 129, 7, 2),
    _GtpDeletePdpReqMom_Type()
)
gtpDeletePdpReqMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtpDeletePdpReqMom.setStatus("current")
_GtpDeletePdpReqMax_Type = CounterBasedGauge64
_GtpDeletePdpReqMax_Object = MibScalar
gtpDeletePdpReqMax = _GtpDeletePdpReqMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 129, 7, 3),
    _GtpDeletePdpReqMax_Type()
)
gtpDeletePdpReqMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtpDeletePdpReqMax.setStatus("current")
_GtpDeletePdpRsp_ObjectIdentity = ObjectIdentity
gtpDeletePdpRsp = _GtpDeletePdpRsp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 129, 8)
)
_GtpDeletePdpRspVal_Type = Counter64
_GtpDeletePdpRspVal_Object = MibScalar
gtpDeletePdpRspVal = _GtpDeletePdpRspVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 129, 8, 1),
    _GtpDeletePdpRspVal_Type()
)
gtpDeletePdpRspVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtpDeletePdpRspVal.setStatus("current")
_GtpDeletePdpRspMom_Type = CounterBasedGauge64
_GtpDeletePdpRspMom_Object = MibScalar
gtpDeletePdpRspMom = _GtpDeletePdpRspMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 129, 8, 2),
    _GtpDeletePdpRspMom_Type()
)
gtpDeletePdpRspMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtpDeletePdpRspMom.setStatus("current")
_GtpDeletePdpRspMax_Type = CounterBasedGauge64
_GtpDeletePdpRspMax_Object = MibScalar
gtpDeletePdpRspMax = _GtpDeletePdpRspMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 129, 8, 3),
    _GtpDeletePdpRspMax_Type()
)
gtpDeletePdpRspMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtpDeletePdpRspMax.setStatus("current")
_GtpErrorInd_ObjectIdentity = ObjectIdentity
gtpErrorInd = _GtpErrorInd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 129, 9)
)
_GtpErrorIndVal_Type = Counter64
_GtpErrorIndVal_Object = MibScalar
gtpErrorIndVal = _GtpErrorIndVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 129, 9, 1),
    _GtpErrorIndVal_Type()
)
gtpErrorIndVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtpErrorIndVal.setStatus("current")
_GtpErrorIndMom_Type = CounterBasedGauge64
_GtpErrorIndMom_Object = MibScalar
gtpErrorIndMom = _GtpErrorIndMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 129, 9, 2),
    _GtpErrorIndMom_Type()
)
gtpErrorIndMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtpErrorIndMom.setStatus("current")
_GtpErrorIndMax_Type = CounterBasedGauge64
_GtpErrorIndMax_Object = MibScalar
gtpErrorIndMax = _GtpErrorIndMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 129, 9, 3),
    _GtpErrorIndMax_Type()
)
gtpErrorIndMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtpErrorIndMax.setStatus("current")
_GtpUnknown_ObjectIdentity = ObjectIdentity
gtpUnknown = _GtpUnknown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 129, 10)
)
_GtpUnknownVal_Type = Counter64
_GtpUnknownVal_Object = MibScalar
gtpUnknownVal = _GtpUnknownVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 129, 10, 1),
    _GtpUnknownVal_Type()
)
gtpUnknownVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtpUnknownVal.setStatus("current")
_GtpUnknownMom_Type = CounterBasedGauge64
_GtpUnknownMom_Object = MibScalar
gtpUnknownMom = _GtpUnknownMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 129, 10, 2),
    _GtpUnknownMom_Type()
)
gtpUnknownMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtpUnknownMom.setStatus("current")
_GtpUnknownMax_Type = CounterBasedGauge64
_GtpUnknownMax_Object = MibScalar
gtpUnknownMax = _GtpUnknownMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 129, 10, 3),
    _GtpUnknownMax_Type()
)
gtpUnknownMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtpUnknownMax.setStatus("current")
_GtpUpdatePdpReq_ObjectIdentity = ObjectIdentity
gtpUpdatePdpReq = _GtpUpdatePdpReq_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 129, 11)
)
_GtpUpdatePdpReqVal_Type = Counter64
_GtpUpdatePdpReqVal_Object = MibScalar
gtpUpdatePdpReqVal = _GtpUpdatePdpReqVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 129, 11, 1),
    _GtpUpdatePdpReqVal_Type()
)
gtpUpdatePdpReqVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtpUpdatePdpReqVal.setStatus("current")
_GtpUpdatePdpReqMom_Type = CounterBasedGauge64
_GtpUpdatePdpReqMom_Object = MibScalar
gtpUpdatePdpReqMom = _GtpUpdatePdpReqMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 129, 11, 2),
    _GtpUpdatePdpReqMom_Type()
)
gtpUpdatePdpReqMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtpUpdatePdpReqMom.setStatus("current")
_GtpUpdatePdpReqMax_Type = CounterBasedGauge64
_GtpUpdatePdpReqMax_Object = MibScalar
gtpUpdatePdpReqMax = _GtpUpdatePdpReqMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 129, 11, 3),
    _GtpUpdatePdpReqMax_Type()
)
gtpUpdatePdpReqMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtpUpdatePdpReqMax.setStatus("current")
_GtpUpdatePdpRsp_ObjectIdentity = ObjectIdentity
gtpUpdatePdpRsp = _GtpUpdatePdpRsp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 129, 12)
)
_GtpUpdatePdpRspVal_Type = Counter64
_GtpUpdatePdpRspVal_Object = MibScalar
gtpUpdatePdpRspVal = _GtpUpdatePdpRspVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 129, 12, 1),
    _GtpUpdatePdpRspVal_Type()
)
gtpUpdatePdpRspVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtpUpdatePdpRspVal.setStatus("current")
_GtpUpdatePdpRspMom_Type = CounterBasedGauge64
_GtpUpdatePdpRspMom_Object = MibScalar
gtpUpdatePdpRspMom = _GtpUpdatePdpRspMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 129, 12, 2),
    _GtpUpdatePdpRspMom_Type()
)
gtpUpdatePdpRspMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtpUpdatePdpRspMom.setStatus("current")
_GtpUpdatePdpRspMax_Type = CounterBasedGauge64
_GtpUpdatePdpRspMax_Object = MibScalar
gtpUpdatePdpRspMax = _GtpUpdatePdpRspMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 129, 12, 3),
    _GtpUpdatePdpRspMax_Type()
)
gtpUpdatePdpRspMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtpUpdatePdpRspMax.setStatus("current")
_GtpEchoPdpReq_ObjectIdentity = ObjectIdentity
gtpEchoPdpReq = _GtpEchoPdpReq_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 129, 13)
)
_GtpEchoPdpReqVal_Type = Counter64
_GtpEchoPdpReqVal_Object = MibScalar
gtpEchoPdpReqVal = _GtpEchoPdpReqVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 129, 13, 1),
    _GtpEchoPdpReqVal_Type()
)
gtpEchoPdpReqVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtpEchoPdpReqVal.setStatus("current")
_GtpEchoPdpReqMom_Type = CounterBasedGauge64
_GtpEchoPdpReqMom_Object = MibScalar
gtpEchoPdpReqMom = _GtpEchoPdpReqMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 129, 13, 2),
    _GtpEchoPdpReqMom_Type()
)
gtpEchoPdpReqMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtpEchoPdpReqMom.setStatus("current")
_GtpEchoPdpReqMax_Type = CounterBasedGauge64
_GtpEchoPdpReqMax_Object = MibScalar
gtpEchoPdpReqMax = _GtpEchoPdpReqMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 129, 13, 3),
    _GtpEchoPdpReqMax_Type()
)
gtpEchoPdpReqMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtpEchoPdpReqMax.setStatus("current")
_GtpEchoPdpRsp_ObjectIdentity = ObjectIdentity
gtpEchoPdpRsp = _GtpEchoPdpRsp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 129, 14)
)
_GtpEchoPdpRspVal_Type = Counter64
_GtpEchoPdpRspVal_Object = MibScalar
gtpEchoPdpRspVal = _GtpEchoPdpRspVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 129, 14, 1),
    _GtpEchoPdpRspVal_Type()
)
gtpEchoPdpRspVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtpEchoPdpRspVal.setStatus("current")
_GtpEchoPdpRspMom_Type = CounterBasedGauge64
_GtpEchoPdpRspMom_Object = MibScalar
gtpEchoPdpRspMom = _GtpEchoPdpRspMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 129, 14, 2),
    _GtpEchoPdpRspMom_Type()
)
gtpEchoPdpRspMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtpEchoPdpRspMom.setStatus("current")
_GtpEchoPdpRspMax_Type = CounterBasedGauge64
_GtpEchoPdpRspMax_Object = MibScalar
gtpEchoPdpRspMax = _GtpEchoPdpRspMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 129, 14, 3),
    _GtpEchoPdpRspMax_Type()
)
gtpEchoPdpRspMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtpEchoPdpRspMax.setStatus("current")
_GtpSgsnReq_ObjectIdentity = ObjectIdentity
gtpSgsnReq = _GtpSgsnReq_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 129, 15)
)
_GtpSgsnReqVal_Type = Counter64
_GtpSgsnReqVal_Object = MibScalar
gtpSgsnReqVal = _GtpSgsnReqVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 129, 15, 1),
    _GtpSgsnReqVal_Type()
)
gtpSgsnReqVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtpSgsnReqVal.setStatus("current")
_GtpSgsnReqMom_Type = CounterBasedGauge64
_GtpSgsnReqMom_Object = MibScalar
gtpSgsnReqMom = _GtpSgsnReqMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 129, 15, 2),
    _GtpSgsnReqMom_Type()
)
gtpSgsnReqMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtpSgsnReqMom.setStatus("current")
_GtpSgsnReqMax_Type = CounterBasedGauge64
_GtpSgsnReqMax_Object = MibScalar
gtpSgsnReqMax = _GtpSgsnReqMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 129, 15, 3),
    _GtpSgsnReqMax_Type()
)
gtpSgsnReqMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtpSgsnReqMax.setStatus("current")
_GtpSgsnRsp_ObjectIdentity = ObjectIdentity
gtpSgsnRsp = _GtpSgsnRsp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 129, 16)
)
_GtpSgsnRspVal_Type = Counter64
_GtpSgsnRspVal_Object = MibScalar
gtpSgsnRspVal = _GtpSgsnRspVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 129, 16, 1),
    _GtpSgsnRspVal_Type()
)
gtpSgsnRspVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtpSgsnRspVal.setStatus("current")
_GtpSgsnRspMom_Type = CounterBasedGauge64
_GtpSgsnRspMom_Object = MibScalar
gtpSgsnRspMom = _GtpSgsnRspMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 129, 16, 2),
    _GtpSgsnRspMom_Type()
)
gtpSgsnRspMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtpSgsnRspMom.setStatus("current")
_GtpSgsnRspMax_Type = CounterBasedGauge64
_GtpSgsnRspMax_Object = MibScalar
gtpSgsnRspMax = _GtpSgsnRspMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 129, 16, 3),
    _GtpSgsnRspMax_Type()
)
gtpSgsnRspMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtpSgsnRspMax.setStatus("current")
_Tunnel_ObjectIdentity = ObjectIdentity
tunnel = _Tunnel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 130)
)
_TunnelGtp_ObjectIdentity = ObjectIdentity
tunnelGtp = _TunnelGtp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 130, 2)
)
_TunnelGtpVal_Type = CounterBasedGauge64
_TunnelGtpVal_Object = MibScalar
tunnelGtpVal = _TunnelGtpVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 130, 2, 1),
    _TunnelGtpVal_Type()
)
tunnelGtpVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelGtpVal.setStatus("current")
_TunnelGtpMax_Type = CounterBasedGauge64
_TunnelGtpMax_Object = MibScalar
tunnelGtpMax = _TunnelGtpMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 130, 2, 3),
    _TunnelGtpMax_Type()
)
tunnelGtpMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelGtpMax.setStatus("current")
_TunnelEsp_ObjectIdentity = ObjectIdentity
tunnelEsp = _TunnelEsp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 130, 3)
)
_TunnelEspVal_Type = CounterBasedGauge64
_TunnelEspVal_Object = MibScalar
tunnelEspVal = _TunnelEspVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 130, 3, 1),
    _TunnelEspVal_Type()
)
tunnelEspVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelEspVal.setStatus("current")
_TunnelEspMax_Type = CounterBasedGauge64
_TunnelEspMax_Object = MibScalar
tunnelEspMax = _TunnelEspMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 130, 3, 3),
    _TunnelEspMax_Type()
)
tunnelEspMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelEspMax.setStatus("current")
_TunnelTeredo_ObjectIdentity = ObjectIdentity
tunnelTeredo = _TunnelTeredo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 130, 4)
)
_TunnelTeredoVal_Type = CounterBasedGauge64
_TunnelTeredoVal_Object = MibScalar
tunnelTeredoVal = _TunnelTeredoVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 130, 4, 1),
    _TunnelTeredoVal_Type()
)
tunnelTeredoVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelTeredoVal.setStatus("current")
_TunnelTeredoMax_Type = CounterBasedGauge64
_TunnelTeredoMax_Object = MibScalar
tunnelTeredoMax = _TunnelTeredoMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 130, 4, 3),
    _TunnelTeredoMax_Type()
)
tunnelTeredoMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelTeredoMax.setStatus("current")
_TunnelGre_ObjectIdentity = ObjectIdentity
tunnelGre = _TunnelGre_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 130, 5)
)
_TunnelGreVal_Type = CounterBasedGauge64
_TunnelGreVal_Object = MibScalar
tunnelGreVal = _TunnelGreVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 130, 5, 1),
    _TunnelGreVal_Type()
)
tunnelGreVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelGreVal.setStatus("current")
_TunnelGreMax_Type = CounterBasedGauge64
_TunnelGreMax_Object = MibScalar
tunnelGreMax = _TunnelGreMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 130, 5, 3),
    _TunnelGreMax_Type()
)
tunnelGreMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelGreMax.setStatus("current")
_TunnelUnknownPkts_ObjectIdentity = ObjectIdentity
tunnelUnknownPkts = _TunnelUnknownPkts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 130, 6)
)
_TunnelUnknownPktsVal_Type = Counter64
_TunnelUnknownPktsVal_Object = MibScalar
tunnelUnknownPktsVal = _TunnelUnknownPktsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 130, 6, 1),
    _TunnelUnknownPktsVal_Type()
)
tunnelUnknownPktsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelUnknownPktsVal.setStatus("current")
_TunnelUnknownPktsMom_Type = CounterBasedGauge64
_TunnelUnknownPktsMom_Object = MibScalar
tunnelUnknownPktsMom = _TunnelUnknownPktsMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 130, 6, 2),
    _TunnelUnknownPktsMom_Type()
)
tunnelUnknownPktsMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelUnknownPktsMom.setStatus("current")
_TunnelUnknownPktsMax_Type = CounterBasedGauge64
_TunnelUnknownPktsMax_Object = MibScalar
tunnelUnknownPktsMax = _TunnelUnknownPktsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 130, 6, 3),
    _TunnelUnknownPktsMax_Type()
)
tunnelUnknownPktsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelUnknownPktsMax.setStatus("current")
_TunnelDuplicates_ObjectIdentity = ObjectIdentity
tunnelDuplicates = _TunnelDuplicates_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 130, 7)
)
_TunnelDuplicatesVal_Type = Counter64
_TunnelDuplicatesVal_Object = MibScalar
tunnelDuplicatesVal = _TunnelDuplicatesVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 130, 7, 1),
    _TunnelDuplicatesVal_Type()
)
tunnelDuplicatesVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelDuplicatesVal.setStatus("current")
_TunnelDuplicatesMom_Type = CounterBasedGauge64
_TunnelDuplicatesMom_Object = MibScalar
tunnelDuplicatesMom = _TunnelDuplicatesMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 130, 7, 2),
    _TunnelDuplicatesMom_Type()
)
tunnelDuplicatesMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelDuplicatesMom.setStatus("current")
_TunnelDuplicatesMax_Type = CounterBasedGauge64
_TunnelDuplicatesMax_Object = MibScalar
tunnelDuplicatesMax = _TunnelDuplicatesMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 130, 7, 3),
    _TunnelDuplicatesMax_Type()
)
tunnelDuplicatesMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelDuplicatesMax.setStatus("current")
_TunnelGeneric_ObjectIdentity = ObjectIdentity
tunnelGeneric = _TunnelGeneric_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 130, 8)
)
_TunnelGenericVal_Type = CounterBasedGauge64
_TunnelGenericVal_Object = MibScalar
tunnelGenericVal = _TunnelGenericVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 130, 8, 1),
    _TunnelGenericVal_Type()
)
tunnelGenericVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelGenericVal.setStatus("current")
_TunnelGenericMax_Type = CounterBasedGauge64
_TunnelGenericMax_Object = MibScalar
tunnelGenericMax = _TunnelGenericMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 130, 8, 3),
    _TunnelGenericMax_Type()
)
tunnelGenericMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelGenericMax.setStatus("current")
_TunnelKnownPkts_ObjectIdentity = ObjectIdentity
tunnelKnownPkts = _TunnelKnownPkts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 130, 9)
)
_TunnelKnownPktsVal_Type = Counter64
_TunnelKnownPktsVal_Object = MibScalar
tunnelKnownPktsVal = _TunnelKnownPktsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 130, 9, 1),
    _TunnelKnownPktsVal_Type()
)
tunnelKnownPktsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelKnownPktsVal.setStatus("current")
_TunnelKnownPktsMom_Type = CounterBasedGauge64
_TunnelKnownPktsMom_Object = MibScalar
tunnelKnownPktsMom = _TunnelKnownPktsMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 130, 9, 2),
    _TunnelKnownPktsMom_Type()
)
tunnelKnownPktsMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelKnownPktsMom.setStatus("current")
_TunnelKnownPktsMax_Type = CounterBasedGauge64
_TunnelKnownPktsMax_Object = MibScalar
tunnelKnownPktsMax = _TunnelKnownPktsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 130, 9, 3),
    _TunnelKnownPktsMax_Type()
)
tunnelKnownPktsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelKnownPktsMax.setStatus("current")
_TunnelL2tp_ObjectIdentity = ObjectIdentity
tunnelL2tp = _TunnelL2tp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 130, 10)
)
_TunnelL2tpVal_Type = CounterBasedGauge64
_TunnelL2tpVal_Object = MibScalar
tunnelL2tpVal = _TunnelL2tpVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 130, 10, 1),
    _TunnelL2tpVal_Type()
)
tunnelL2tpVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelL2tpVal.setStatus("current")
_TunnelL2tpMax_Type = CounterBasedGauge64
_TunnelL2tpMax_Object = MibScalar
tunnelL2tpMax = _TunnelL2tpMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 130, 10, 3),
    _TunnelL2tpMax_Type()
)
tunnelL2tpMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelL2tpMax.setStatus("current")
_Gre_ObjectIdentity = ObjectIdentity
gre = _Gre_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 131)
)
_GrePackets_ObjectIdentity = ObjectIdentity
grePackets = _GrePackets_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 131, 2)
)
_GrePacketsVal_Type = Counter64
_GrePacketsVal_Object = MibScalar
grePacketsVal = _GrePacketsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 131, 2, 1),
    _GrePacketsVal_Type()
)
grePacketsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grePacketsVal.setStatus("current")
_GrePacketsMom_Type = CounterBasedGauge64
_GrePacketsMom_Object = MibScalar
grePacketsMom = _GrePacketsMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 131, 2, 2),
    _GrePacketsMom_Type()
)
grePacketsMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grePacketsMom.setStatus("current")
_GrePacketsMax_Type = CounterBasedGauge64
_GrePacketsMax_Object = MibScalar
grePacketsMax = _GrePacketsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 131, 2, 3),
    _GrePacketsMax_Type()
)
grePacketsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grePacketsMax.setStatus("current")
_GreBytes_ObjectIdentity = ObjectIdentity
greBytes = _GreBytes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 131, 3)
)
_GreBytesVal_Type = Counter64
_GreBytesVal_Object = MibScalar
greBytesVal = _GreBytesVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 131, 3, 1),
    _GreBytesVal_Type()
)
greBytesVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    greBytesVal.setStatus("current")
_GreBytesMom_Type = CounterBasedGauge64
_GreBytesMom_Object = MibScalar
greBytesMom = _GreBytesMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 131, 3, 2),
    _GreBytesMom_Type()
)
greBytesMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    greBytesMom.setStatus("current")
_GreBytesMax_Type = CounterBasedGauge64
_GreBytesMax_Object = MibScalar
greBytesMax = _GreBytesMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 131, 3, 3),
    _GreBytesMax_Type()
)
greBytesMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    greBytesMax.setStatus("current")
_GreUnknownVersion_ObjectIdentity = ObjectIdentity
greUnknownVersion = _GreUnknownVersion_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 131, 4)
)
_GreUnknownVersionVal_Type = Counter64
_GreUnknownVersionVal_Object = MibScalar
greUnknownVersionVal = _GreUnknownVersionVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 131, 4, 1),
    _GreUnknownVersionVal_Type()
)
greUnknownVersionVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    greUnknownVersionVal.setStatus("current")
_GreUnknownVersionMom_Type = CounterBasedGauge64
_GreUnknownVersionMom_Object = MibScalar
greUnknownVersionMom = _GreUnknownVersionMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 131, 4, 2),
    _GreUnknownVersionMom_Type()
)
greUnknownVersionMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    greUnknownVersionMom.setStatus("current")
_GreUnknownVersionMax_Type = CounterBasedGauge64
_GreUnknownVersionMax_Object = MibScalar
greUnknownVersionMax = _GreUnknownVersionMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 131, 4, 3),
    _GreUnknownVersionMax_Type()
)
greUnknownVersionMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    greUnknownVersionMax.setStatus("current")
_GreShortPackets_ObjectIdentity = ObjectIdentity
greShortPackets = _GreShortPackets_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 131, 5)
)
_GreShortPacketsVal_Type = Counter64
_GreShortPacketsVal_Object = MibScalar
greShortPacketsVal = _GreShortPacketsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 131, 5, 1),
    _GreShortPacketsVal_Type()
)
greShortPacketsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    greShortPacketsVal.setStatus("current")
_GreShortPacketsMom_Type = CounterBasedGauge64
_GreShortPacketsMom_Object = MibScalar
greShortPacketsMom = _GreShortPacketsMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 131, 5, 2),
    _GreShortPacketsMom_Type()
)
greShortPacketsMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    greShortPacketsMom.setStatus("current")
_GreShortPacketsMax_Type = CounterBasedGauge64
_GreShortPacketsMax_Object = MibScalar
greShortPacketsMax = _GreShortPacketsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 131, 5, 3),
    _GreShortPacketsMax_Type()
)
greShortPacketsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    greShortPacketsMax.setStatus("current")
_GreUnknownType_ObjectIdentity = ObjectIdentity
greUnknownType = _GreUnknownType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 131, 6)
)
_GreUnknownTypeVal_Type = Counter64
_GreUnknownTypeVal_Object = MibScalar
greUnknownTypeVal = _GreUnknownTypeVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 131, 6, 1),
    _GreUnknownTypeVal_Type()
)
greUnknownTypeVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    greUnknownTypeVal.setStatus("current")
_GreUnknownTypeMom_Type = CounterBasedGauge64
_GreUnknownTypeMom_Object = MibScalar
greUnknownTypeMom = _GreUnknownTypeMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 131, 6, 2),
    _GreUnknownTypeMom_Type()
)
greUnknownTypeMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    greUnknownTypeMom.setStatus("current")
_GreUnknownTypeMax_Type = CounterBasedGauge64
_GreUnknownTypeMax_Object = MibScalar
greUnknownTypeMax = _GreUnknownTypeMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 131, 6, 3),
    _GreUnknownTypeMax_Type()
)
greUnknownTypeMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    greUnknownTypeMax.setStatus("current")
_GreRouteFlag_ObjectIdentity = ObjectIdentity
greRouteFlag = _GreRouteFlag_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 131, 7)
)
_GreRouteFlagVal_Type = Counter64
_GreRouteFlagVal_Object = MibScalar
greRouteFlagVal = _GreRouteFlagVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 131, 7, 1),
    _GreRouteFlagVal_Type()
)
greRouteFlagVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    greRouteFlagVal.setStatus("current")
_GreRouteFlagMom_Type = CounterBasedGauge64
_GreRouteFlagMom_Object = MibScalar
greRouteFlagMom = _GreRouteFlagMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 131, 7, 2),
    _GreRouteFlagMom_Type()
)
greRouteFlagMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    greRouteFlagMom.setStatus("current")
_GreRouteFlagMax_Type = CounterBasedGauge64
_GreRouteFlagMax_Object = MibScalar
greRouteFlagMax = _GreRouteFlagMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 131, 7, 3),
    _GreRouteFlagMax_Type()
)
greRouteFlagMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    greRouteFlagMax.setStatus("current")
_GreIpv4Packets_ObjectIdentity = ObjectIdentity
greIpv4Packets = _GreIpv4Packets_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 131, 8)
)
_GreIpv4PacketsVal_Type = Counter64
_GreIpv4PacketsVal_Object = MibScalar
greIpv4PacketsVal = _GreIpv4PacketsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 131, 8, 1),
    _GreIpv4PacketsVal_Type()
)
greIpv4PacketsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    greIpv4PacketsVal.setStatus("current")
_GreIpv4PacketsMom_Type = CounterBasedGauge64
_GreIpv4PacketsMom_Object = MibScalar
greIpv4PacketsMom = _GreIpv4PacketsMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 131, 8, 2),
    _GreIpv4PacketsMom_Type()
)
greIpv4PacketsMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    greIpv4PacketsMom.setStatus("current")
_GreIpv4PacketsMax_Type = CounterBasedGauge64
_GreIpv4PacketsMax_Object = MibScalar
greIpv4PacketsMax = _GreIpv4PacketsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 131, 8, 3),
    _GreIpv4PacketsMax_Type()
)
greIpv4PacketsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    greIpv4PacketsMax.setStatus("current")
_GreIpv6Packets_ObjectIdentity = ObjectIdentity
greIpv6Packets = _GreIpv6Packets_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 131, 9)
)
_GreIpv6PacketsVal_Type = Counter64
_GreIpv6PacketsVal_Object = MibScalar
greIpv6PacketsVal = _GreIpv6PacketsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 131, 9, 1),
    _GreIpv6PacketsVal_Type()
)
greIpv6PacketsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    greIpv6PacketsVal.setStatus("current")
_GreIpv6PacketsMom_Type = CounterBasedGauge64
_GreIpv6PacketsMom_Object = MibScalar
greIpv6PacketsMom = _GreIpv6PacketsMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 131, 9, 2),
    _GreIpv6PacketsMom_Type()
)
greIpv6PacketsMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    greIpv6PacketsMom.setStatus("current")
_GreIpv6PacketsMax_Type = CounterBasedGauge64
_GreIpv6PacketsMax_Object = MibScalar
greIpv6PacketsMax = _GreIpv6PacketsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 131, 9, 3),
    _GreIpv6PacketsMax_Type()
)
greIpv6PacketsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    greIpv6PacketsMax.setStatus("current")
_GreFfffPackets_ObjectIdentity = ObjectIdentity
greFfffPackets = _GreFfffPackets_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 131, 10)
)
_GreFfffPacketsVal_Type = Counter64
_GreFfffPacketsVal_Object = MibScalar
greFfffPacketsVal = _GreFfffPacketsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 131, 10, 1),
    _GreFfffPacketsVal_Type()
)
greFfffPacketsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    greFfffPacketsVal.setStatus("current")
_GreFfffPacketsMom_Type = CounterBasedGauge64
_GreFfffPacketsMom_Object = MibScalar
greFfffPacketsMom = _GreFfffPacketsMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 131, 10, 2),
    _GreFfffPacketsMom_Type()
)
greFfffPacketsMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    greFfffPacketsMom.setStatus("current")
_GreFfffPacketsMax_Type = CounterBasedGauge64
_GreFfffPacketsMax_Object = MibScalar
greFfffPacketsMax = _GreFfffPacketsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 131, 10, 3),
    _GreFfffPacketsMax_Type()
)
greFfffPacketsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    greFfffPacketsMax.setStatus("current")
_GrePptpPackets_ObjectIdentity = ObjectIdentity
grePptpPackets = _GrePptpPackets_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 131, 11)
)
_GrePptpPacketsVal_Type = Counter64
_GrePptpPacketsVal_Object = MibScalar
grePptpPacketsVal = _GrePptpPacketsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 131, 11, 1),
    _GrePptpPacketsVal_Type()
)
grePptpPacketsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grePptpPacketsVal.setStatus("current")
_GrePptpPacketsMom_Type = CounterBasedGauge64
_GrePptpPacketsMom_Object = MibScalar
grePptpPacketsMom = _GrePptpPacketsMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 131, 11, 2),
    _GrePptpPacketsMom_Type()
)
grePptpPacketsMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grePptpPacketsMom.setStatus("current")
_GrePptpPacketsMax_Type = CounterBasedGauge64
_GrePptpPacketsMax_Object = MibScalar
grePptpPacketsMax = _GrePptpPacketsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 131, 11, 3),
    _GrePptpPacketsMax_Type()
)
grePptpPacketsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grePptpPacketsMax.setStatus("current")
_GrePppPackets_ObjectIdentity = ObjectIdentity
grePppPackets = _GrePppPackets_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 131, 12)
)
_GrePppPacketsVal_Type = Counter64
_GrePppPacketsVal_Object = MibScalar
grePppPacketsVal = _GrePppPacketsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 131, 12, 1),
    _GrePppPacketsVal_Type()
)
grePppPacketsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grePppPacketsVal.setStatus("current")
_GrePppPacketsMom_Type = CounterBasedGauge64
_GrePppPacketsMom_Object = MibScalar
grePppPacketsMom = _GrePppPacketsMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 131, 12, 2),
    _GrePppPacketsMom_Type()
)
grePppPacketsMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grePppPacketsMom.setStatus("current")
_GrePppPacketsMax_Type = CounterBasedGauge64
_GrePppPacketsMax_Object = MibScalar
grePppPacketsMax = _GrePppPacketsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 131, 12, 3),
    _GrePppPacketsMax_Type()
)
grePppPacketsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grePppPacketsMax.setStatus("current")
_GrePppUnknownPackets_ObjectIdentity = ObjectIdentity
grePppUnknownPackets = _GrePppUnknownPackets_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 131, 13)
)
_GrePppUnknownPacketsVal_Type = Counter64
_GrePppUnknownPacketsVal_Object = MibScalar
grePppUnknownPacketsVal = _GrePppUnknownPacketsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 131, 13, 1),
    _GrePppUnknownPacketsVal_Type()
)
grePppUnknownPacketsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grePppUnknownPacketsVal.setStatus("current")
_GrePppUnknownPacketsMom_Type = CounterBasedGauge64
_GrePppUnknownPacketsMom_Object = MibScalar
grePppUnknownPacketsMom = _GrePppUnknownPacketsMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 131, 13, 2),
    _GrePppUnknownPacketsMom_Type()
)
grePppUnknownPacketsMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grePppUnknownPacketsMom.setStatus("current")
_GrePppUnknownPacketsMax_Type = CounterBasedGauge64
_GrePppUnknownPacketsMax_Object = MibScalar
grePppUnknownPacketsMax = _GrePppUnknownPacketsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 131, 13, 3),
    _GrePppUnknownPacketsMax_Type()
)
grePppUnknownPacketsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grePppUnknownPacketsMax.setStatus("current")
_L2tp_ObjectIdentity = ObjectIdentity
l2tp = _L2tp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 132)
)
_L2tpPackets_ObjectIdentity = ObjectIdentity
l2tpPackets = _L2tpPackets_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 132, 2)
)
_L2tpPacketsVal_Type = Counter64
_L2tpPacketsVal_Object = MibScalar
l2tpPacketsVal = _L2tpPacketsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 132, 2, 1),
    _L2tpPacketsVal_Type()
)
l2tpPacketsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpPacketsVal.setStatus("current")
_L2tpPacketsMom_Type = CounterBasedGauge64
_L2tpPacketsMom_Object = MibScalar
l2tpPacketsMom = _L2tpPacketsMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 132, 2, 2),
    _L2tpPacketsMom_Type()
)
l2tpPacketsMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpPacketsMom.setStatus("current")
_L2tpPacketsMax_Type = CounterBasedGauge64
_L2tpPacketsMax_Object = MibScalar
l2tpPacketsMax = _L2tpPacketsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 132, 2, 3),
    _L2tpPacketsMax_Type()
)
l2tpPacketsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpPacketsMax.setStatus("current")
_L2tpBytes_ObjectIdentity = ObjectIdentity
l2tpBytes = _L2tpBytes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 132, 3)
)
_L2tpBytesVal_Type = Counter64
_L2tpBytesVal_Object = MibScalar
l2tpBytesVal = _L2tpBytesVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 132, 3, 1),
    _L2tpBytesVal_Type()
)
l2tpBytesVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpBytesVal.setStatus("current")
_L2tpBytesMom_Type = CounterBasedGauge64
_L2tpBytesMom_Object = MibScalar
l2tpBytesMom = _L2tpBytesMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 132, 3, 2),
    _L2tpBytesMom_Type()
)
l2tpBytesMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpBytesMom.setStatus("current")
_L2tpBytesMax_Type = CounterBasedGauge64
_L2tpBytesMax_Object = MibScalar
l2tpBytesMax = _L2tpBytesMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 132, 3, 3),
    _L2tpBytesMax_Type()
)
l2tpBytesMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpBytesMax.setStatus("current")
_L2tpIpv4Packets_ObjectIdentity = ObjectIdentity
l2tpIpv4Packets = _L2tpIpv4Packets_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 132, 4)
)
_L2tpIpv4PacketsVal_Type = Counter64
_L2tpIpv4PacketsVal_Object = MibScalar
l2tpIpv4PacketsVal = _L2tpIpv4PacketsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 132, 4, 1),
    _L2tpIpv4PacketsVal_Type()
)
l2tpIpv4PacketsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpIpv4PacketsVal.setStatus("current")
_L2tpIpv4PacketsMom_Type = CounterBasedGauge64
_L2tpIpv4PacketsMom_Object = MibScalar
l2tpIpv4PacketsMom = _L2tpIpv4PacketsMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 132, 4, 2),
    _L2tpIpv4PacketsMom_Type()
)
l2tpIpv4PacketsMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpIpv4PacketsMom.setStatus("current")
_L2tpIpv4PacketsMax_Type = CounterBasedGauge64
_L2tpIpv4PacketsMax_Object = MibScalar
l2tpIpv4PacketsMax = _L2tpIpv4PacketsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 132, 4, 3),
    _L2tpIpv4PacketsMax_Type()
)
l2tpIpv4PacketsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpIpv4PacketsMax.setStatus("current")
_L2tpIpv6Packets_ObjectIdentity = ObjectIdentity
l2tpIpv6Packets = _L2tpIpv6Packets_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 132, 5)
)
_L2tpIpv6PacketsVal_Type = Counter64
_L2tpIpv6PacketsVal_Object = MibScalar
l2tpIpv6PacketsVal = _L2tpIpv6PacketsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 132, 5, 1),
    _L2tpIpv6PacketsVal_Type()
)
l2tpIpv6PacketsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpIpv6PacketsVal.setStatus("current")
_L2tpIpv6PacketsMom_Type = CounterBasedGauge64
_L2tpIpv6PacketsMom_Object = MibScalar
l2tpIpv6PacketsMom = _L2tpIpv6PacketsMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 132, 5, 2),
    _L2tpIpv6PacketsMom_Type()
)
l2tpIpv6PacketsMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpIpv6PacketsMom.setStatus("current")
_L2tpIpv6PacketsMax_Type = CounterBasedGauge64
_L2tpIpv6PacketsMax_Object = MibScalar
l2tpIpv6PacketsMax = _L2tpIpv6PacketsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 132, 5, 3),
    _L2tpIpv6PacketsMax_Type()
)
l2tpIpv6PacketsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpIpv6PacketsMax.setStatus("current")
_L2tplcpPackets_ObjectIdentity = ObjectIdentity
l2tplcpPackets = _L2tplcpPackets_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 132, 6)
)
_L2tplcpPacketsVal_Type = Counter64
_L2tplcpPacketsVal_Object = MibScalar
l2tplcpPacketsVal = _L2tplcpPacketsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 132, 6, 1),
    _L2tplcpPacketsVal_Type()
)
l2tplcpPacketsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tplcpPacketsVal.setStatus("current")
_L2tplcpPacketsMom_Type = CounterBasedGauge64
_L2tplcpPacketsMom_Object = MibScalar
l2tplcpPacketsMom = _L2tplcpPacketsMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 132, 6, 2),
    _L2tplcpPacketsMom_Type()
)
l2tplcpPacketsMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tplcpPacketsMom.setStatus("current")
_L2tplcpPacketsMax_Type = CounterBasedGauge64
_L2tplcpPacketsMax_Object = MibScalar
l2tplcpPacketsMax = _L2tplcpPacketsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 132, 6, 3),
    _L2tplcpPacketsMax_Type()
)
l2tplcpPacketsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tplcpPacketsMax.setStatus("current")
_L2tpcipv4Packets_ObjectIdentity = ObjectIdentity
l2tpcipv4Packets = _L2tpcipv4Packets_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 132, 7)
)
_L2tpcipv4PacketsVal_Type = Counter64
_L2tpcipv4PacketsVal_Object = MibScalar
l2tpcipv4PacketsVal = _L2tpcipv4PacketsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 132, 7, 1),
    _L2tpcipv4PacketsVal_Type()
)
l2tpcipv4PacketsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpcipv4PacketsVal.setStatus("current")
_L2tpcipv4PacketsMom_Type = CounterBasedGauge64
_L2tpcipv4PacketsMom_Object = MibScalar
l2tpcipv4PacketsMom = _L2tpcipv4PacketsMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 132, 7, 2),
    _L2tpcipv4PacketsMom_Type()
)
l2tpcipv4PacketsMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpcipv4PacketsMom.setStatus("current")
_L2tpcipv4PacketsMax_Type = CounterBasedGauge64
_L2tpcipv4PacketsMax_Object = MibScalar
l2tpcipv4PacketsMax = _L2tpcipv4PacketsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 132, 7, 3),
    _L2tpcipv4PacketsMax_Type()
)
l2tpcipv4PacketsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpcipv4PacketsMax.setStatus("current")
_L2tpcipv6Packets_ObjectIdentity = ObjectIdentity
l2tpcipv6Packets = _L2tpcipv6Packets_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 132, 8)
)
_L2tpcipv6PacketsVal_Type = Counter64
_L2tpcipv6PacketsVal_Object = MibScalar
l2tpcipv6PacketsVal = _L2tpcipv6PacketsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 132, 8, 1),
    _L2tpcipv6PacketsVal_Type()
)
l2tpcipv6PacketsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpcipv6PacketsVal.setStatus("current")
_L2tpcipv6PacketsMom_Type = CounterBasedGauge64
_L2tpcipv6PacketsMom_Object = MibScalar
l2tpcipv6PacketsMom = _L2tpcipv6PacketsMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 132, 8, 2),
    _L2tpcipv6PacketsMom_Type()
)
l2tpcipv6PacketsMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpcipv6PacketsMom.setStatus("current")
_L2tpcipv6PacketsMax_Type = CounterBasedGauge64
_L2tpcipv6PacketsMax_Object = MibScalar
l2tpcipv6PacketsMax = _L2tpcipv6PacketsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 132, 8, 3),
    _L2tpcipv6PacketsMax_Type()
)
l2tpcipv6PacketsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpcipv6PacketsMax.setStatus("current")
_L2tpchap6Packets_ObjectIdentity = ObjectIdentity
l2tpchap6Packets = _L2tpchap6Packets_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 132, 9)
)
_L2tpchap6PacketsVal_Type = Counter64
_L2tpchap6PacketsVal_Object = MibScalar
l2tpchap6PacketsVal = _L2tpchap6PacketsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 132, 9, 1),
    _L2tpchap6PacketsVal_Type()
)
l2tpchap6PacketsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpchap6PacketsVal.setStatus("current")
_L2tpchap6PacketsMom_Type = CounterBasedGauge64
_L2tpchap6PacketsMom_Object = MibScalar
l2tpchap6PacketsMom = _L2tpchap6PacketsMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 132, 9, 2),
    _L2tpchap6PacketsMom_Type()
)
l2tpchap6PacketsMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpchap6PacketsMom.setStatus("current")
_L2tpchap6PacketsMax_Type = CounterBasedGauge64
_L2tpchap6PacketsMax_Object = MibScalar
l2tpchap6PacketsMax = _L2tpchap6PacketsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 132, 9, 3),
    _L2tpchap6PacketsMax_Type()
)
l2tpchap6PacketsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpchap6PacketsMax.setStatus("current")
_System_ObjectIdentity = ObjectIdentity
system = _System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 133)
)
_SystemCPULoad_ObjectIdentity = ObjectIdentity
systemCPULoad = _SystemCPULoad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 133, 1)
)
_SystemCPULoadVal_Type = Unsigned32
_SystemCPULoadVal_Object = MibScalar
systemCPULoadVal = _SystemCPULoadVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 133, 1, 1),
    _SystemCPULoadVal_Type()
)
systemCPULoadVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemCPULoadVal.setStatus("current")
_SystemCPULoadMax_Type = Unsigned32
_SystemCPULoadMax_Object = MibScalar
systemCPULoadMax = _SystemCPULoadMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 133, 1, 3),
    _SystemCPULoadMax_Type()
)
systemCPULoadMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemCPULoadMax.setStatus("current")
_SystemMemTotal_ObjectIdentity = ObjectIdentity
systemMemTotal = _SystemMemTotal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 133, 2)
)
_SystemMemTotalVal_Type = CounterBasedGauge64
_SystemMemTotalVal_Object = MibScalar
systemMemTotalVal = _SystemMemTotalVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 133, 2, 1),
    _SystemMemTotalVal_Type()
)
systemMemTotalVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemMemTotalVal.setStatus("current")
_SystemMemTotalMax_Type = CounterBasedGauge64
_SystemMemTotalMax_Object = MibScalar
systemMemTotalMax = _SystemMemTotalMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 133, 2, 3),
    _SystemMemTotalMax_Type()
)
systemMemTotalMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemMemTotalMax.setStatus("current")
_SystemMemFree_ObjectIdentity = ObjectIdentity
systemMemFree = _SystemMemFree_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 133, 3)
)
_SystemMemFreeVal_Type = CounterBasedGauge64
_SystemMemFreeVal_Object = MibScalar
systemMemFreeVal = _SystemMemFreeVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 133, 3, 1),
    _SystemMemFreeVal_Type()
)
systemMemFreeVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemMemFreeVal.setStatus("current")
_SystemMemFreeMax_Type = CounterBasedGauge64
_SystemMemFreeMax_Object = MibScalar
systemMemFreeMax = _SystemMemFreeMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 133, 3, 3),
    _SystemMemFreeMax_Type()
)
systemMemFreeMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemMemFreeMax.setStatus("current")
_SystemSwapTotal_ObjectIdentity = ObjectIdentity
systemSwapTotal = _SystemSwapTotal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 133, 4)
)
_SystemSwapTotalVal_Type = CounterBasedGauge64
_SystemSwapTotalVal_Object = MibScalar
systemSwapTotalVal = _SystemSwapTotalVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 133, 4, 1),
    _SystemSwapTotalVal_Type()
)
systemSwapTotalVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemSwapTotalVal.setStatus("current")
_SystemSwapTotalMax_Type = CounterBasedGauge64
_SystemSwapTotalMax_Object = MibScalar
systemSwapTotalMax = _SystemSwapTotalMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 133, 4, 3),
    _SystemSwapTotalMax_Type()
)
systemSwapTotalMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemSwapTotalMax.setStatus("current")
_SystemSwapFree_ObjectIdentity = ObjectIdentity
systemSwapFree = _SystemSwapFree_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 133, 5)
)
_SystemSwapFreeVal_Type = CounterBasedGauge64
_SystemSwapFreeVal_Object = MibScalar
systemSwapFreeVal = _SystemSwapFreeVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 133, 5, 1),
    _SystemSwapFreeVal_Type()
)
systemSwapFreeVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemSwapFreeVal.setStatus("current")
_SystemSwapFreeMax_Type = CounterBasedGauge64
_SystemSwapFreeMax_Object = MibScalar
systemSwapFreeMax = _SystemSwapFreeMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 133, 5, 3),
    _SystemSwapFreeMax_Type()
)
systemSwapFreeMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemSwapFreeMax.setStatus("current")
_SystemUptime_ObjectIdentity = ObjectIdentity
systemUptime = _SystemUptime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 133, 6)
)
_SystemUptimeVal_Type = TimeTicks
_SystemUptimeVal_Object = MibScalar
systemUptimeVal = _SystemUptimeVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 133, 6, 1),
    _SystemUptimeVal_Type()
)
systemUptimeVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemUptimeVal.setStatus("current")
_SystemHdUsage_ObjectIdentity = ObjectIdentity
systemHdUsage = _SystemHdUsage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 133, 7)
)
_SystemHdUsageVal_Type = Unsigned32
_SystemHdUsageVal_Object = MibScalar
systemHdUsageVal = _SystemHdUsageVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 133, 7, 1),
    _SystemHdUsageVal_Type()
)
systemHdUsageVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemHdUsageVal.setStatus("current")
_SystemHdUsageMax_Type = Unsigned32
_SystemHdUsageMax_Object = MibScalar
systemHdUsageMax = _SystemHdUsageMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 133, 7, 3),
    _SystemHdUsageMax_Type()
)
systemHdUsageMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemHdUsageMax.setStatus("current")
_SystemHdSize_ObjectIdentity = ObjectIdentity
systemHdSize = _SystemHdSize_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 133, 8)
)
_SystemHdSizeVal_Type = CounterBasedGauge64
_SystemHdSizeVal_Object = MibScalar
systemHdSizeVal = _SystemHdSizeVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 133, 8, 1),
    _SystemHdSizeVal_Type()
)
systemHdSizeVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemHdSizeVal.setStatus("current")
_SystemHdSizeMax_Type = CounterBasedGauge64
_SystemHdSizeMax_Object = MibScalar
systemHdSizeMax = _SystemHdSizeMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 133, 8, 3),
    _SystemHdSizeMax_Type()
)
systemHdSizeMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemHdSizeMax.setStatus("current")
_Liveview_ObjectIdentity = ObjectIdentity
liveview = _Liveview_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 134)
)
_LiveviewUptime_ObjectIdentity = ObjectIdentity
liveviewUptime = _LiveviewUptime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 134, 1)
)
_LiveviewUptimeVal_Type = TimeTicks
_LiveviewUptimeVal_Object = MibScalar
liveviewUptimeVal = _LiveviewUptimeVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 134, 1, 1),
    _LiveviewUptimeVal_Type()
)
liveviewUptimeVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    liveviewUptimeVal.setStatus("current")
_LiveviewClients_ObjectIdentity = ObjectIdentity
liveviewClients = _LiveviewClients_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 134, 2)
)
_LiveviewClientsVal_Type = CounterBasedGauge64
_LiveviewClientsVal_Object = MibScalar
liveviewClientsVal = _LiveviewClientsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 134, 2, 1),
    _LiveviewClientsVal_Type()
)
liveviewClientsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    liveviewClientsVal.setStatus("current")
_LiveviewClientsMax_Type = CounterBasedGauge64
_LiveviewClientsMax_Object = MibScalar
liveviewClientsMax = _LiveviewClientsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 134, 2, 3),
    _LiveviewClientsMax_Type()
)
liveviewClientsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    liveviewClientsMax.setStatus("current")
_LiveviewPLSDClients_ObjectIdentity = ObjectIdentity
liveviewPLSDClients = _LiveviewPLSDClients_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 134, 3)
)
_LiveviewPLSDClientsVal_Type = CounterBasedGauge64
_LiveviewPLSDClientsVal_Object = MibScalar
liveviewPLSDClientsVal = _LiveviewPLSDClientsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 134, 3, 1),
    _LiveviewPLSDClientsVal_Type()
)
liveviewPLSDClientsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    liveviewPLSDClientsVal.setStatus("current")
_LiveviewPLSDClientsMax_Type = CounterBasedGauge64
_LiveviewPLSDClientsMax_Object = MibScalar
liveviewPLSDClientsMax = _LiveviewPLSDClientsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 134, 3, 3),
    _LiveviewPLSDClientsMax_Type()
)
liveviewPLSDClientsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    liveviewPLSDClientsMax.setStatus("current")
_LiveviewHosts_ObjectIdentity = ObjectIdentity
liveviewHosts = _LiveviewHosts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 134, 4)
)
_LiveviewHostsVal_Type = CounterBasedGauge64
_LiveviewHostsVal_Object = MibScalar
liveviewHostsVal = _LiveviewHostsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 134, 4, 1),
    _LiveviewHostsVal_Type()
)
liveviewHostsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    liveviewHostsVal.setStatus("current")
_LiveviewHostsMax_Type = CounterBasedGauge64
_LiveviewHostsMax_Object = MibScalar
liveviewHostsMax = _LiveviewHostsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 134, 4, 3),
    _LiveviewHostsMax_Type()
)
liveviewHostsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    liveviewHostsMax.setStatus("current")
_LiveviewVNOs_ObjectIdentity = ObjectIdentity
liveviewVNOs = _LiveviewVNOs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 134, 5)
)
_LiveviewVNOsVal_Type = CounterBasedGauge64
_LiveviewVNOsVal_Object = MibScalar
liveviewVNOsVal = _LiveviewVNOsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 134, 5, 1),
    _LiveviewVNOsVal_Type()
)
liveviewVNOsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    liveviewVNOsVal.setStatus("current")
_LiveviewVNOsMax_Type = CounterBasedGauge64
_LiveviewVNOsMax_Object = MibScalar
liveviewVNOsMax = _LiveviewVNOsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 134, 5, 3),
    _LiveviewVNOsMax_Type()
)
liveviewVNOsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    liveviewVNOsMax.setStatus("current")
_LiveviewActiveVNOs_ObjectIdentity = ObjectIdentity
liveviewActiveVNOs = _LiveviewActiveVNOs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 134, 6)
)
_LiveviewActiveVNOsVal_Type = CounterBasedGauge64
_LiveviewActiveVNOsVal_Object = MibScalar
liveviewActiveVNOsVal = _LiveviewActiveVNOsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 134, 6, 1),
    _LiveviewActiveVNOsVal_Type()
)
liveviewActiveVNOsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    liveviewActiveVNOsVal.setStatus("current")
_LiveviewActiveVNOsMax_Type = CounterBasedGauge64
_LiveviewActiveVNOsMax_Object = MibScalar
liveviewActiveVNOsMax = _LiveviewActiveVNOsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 134, 6, 3),
    _LiveviewActiveVNOsMax_Type()
)
liveviewActiveVNOsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    liveviewActiveVNOsMax.setStatus("current")
_LiveviewDrdlRevision_ObjectIdentity = ObjectIdentity
liveviewDrdlRevision = _LiveviewDrdlRevision_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 134, 7)
)
_LiveviewDrdlRevisionVal_Type = CounterBasedGauge64
_LiveviewDrdlRevisionVal_Object = MibScalar
liveviewDrdlRevisionVal = _LiveviewDrdlRevisionVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 134, 7, 1),
    _LiveviewDrdlRevisionVal_Type()
)
liveviewDrdlRevisionVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    liveviewDrdlRevisionVal.setStatus("current")
_LiveviewDrdlRevisionMax_Type = CounterBasedGauge64
_LiveviewDrdlRevisionMax_Object = MibScalar
liveviewDrdlRevisionMax = _LiveviewDrdlRevisionMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 134, 7, 3),
    _LiveviewDrdlRevisionMax_Type()
)
liveviewDrdlRevisionMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    liveviewDrdlRevisionMax.setStatus("current")
_LiveviewFailedNetobjects_ObjectIdentity = ObjectIdentity
liveviewFailedNetobjects = _LiveviewFailedNetobjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 134, 8)
)
_LiveviewFailedNetobjectsVal_Type = Counter64
_LiveviewFailedNetobjectsVal_Object = MibScalar
liveviewFailedNetobjectsVal = _LiveviewFailedNetobjectsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 134, 8, 1),
    _LiveviewFailedNetobjectsVal_Type()
)
liveviewFailedNetobjectsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    liveviewFailedNetobjectsVal.setStatus("current")
_LiveviewFailedNetobjectsMom_Type = CounterBasedGauge64
_LiveviewFailedNetobjectsMom_Object = MibScalar
liveviewFailedNetobjectsMom = _LiveviewFailedNetobjectsMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 134, 8, 2),
    _LiveviewFailedNetobjectsMom_Type()
)
liveviewFailedNetobjectsMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    liveviewFailedNetobjectsMom.setStatus("current")
_LiveviewFailedNetobjectsMax_Type = CounterBasedGauge64
_LiveviewFailedNetobjectsMax_Object = MibScalar
liveviewFailedNetobjectsMax = _LiveviewFailedNetobjectsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 134, 8, 3),
    _LiveviewFailedNetobjectsMax_Type()
)
liveviewFailedNetobjectsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    liveviewFailedNetobjectsMax.setStatus("current")
_LiveviewFailedFullNetobjects_ObjectIdentity = ObjectIdentity
liveviewFailedFullNetobjects = _LiveviewFailedFullNetobjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 134, 9)
)
_LiveviewFailedFullNetobjectsVal_Type = Counter64
_LiveviewFailedFullNetobjectsVal_Object = MibScalar
liveviewFailedFullNetobjectsVal = _LiveviewFailedFullNetobjectsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 134, 9, 1),
    _LiveviewFailedFullNetobjectsVal_Type()
)
liveviewFailedFullNetobjectsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    liveviewFailedFullNetobjectsVal.setStatus("current")
_LiveviewFailedFullNetobjectsMom_Type = CounterBasedGauge64
_LiveviewFailedFullNetobjectsMom_Object = MibScalar
liveviewFailedFullNetobjectsMom = _LiveviewFailedFullNetobjectsMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 134, 9, 2),
    _LiveviewFailedFullNetobjectsMom_Type()
)
liveviewFailedFullNetobjectsMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    liveviewFailedFullNetobjectsMom.setStatus("current")
_LiveviewFailedFullNetobjectsMax_Type = CounterBasedGauge64
_LiveviewFailedFullNetobjectsMax_Object = MibScalar
liveviewFailedFullNetobjectsMax = _LiveviewFailedFullNetobjectsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 134, 9, 3),
    _LiveviewFailedFullNetobjectsMax_Type()
)
liveviewFailedFullNetobjectsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    liveviewFailedFullNetobjectsMax.setStatus("current")
_LiveviewStringCacheUsage_ObjectIdentity = ObjectIdentity
liveviewStringCacheUsage = _LiveviewStringCacheUsage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 134, 10)
)
_LiveviewStringCacheUsageVal_Type = CounterBasedGauge64
_LiveviewStringCacheUsageVal_Object = MibScalar
liveviewStringCacheUsageVal = _LiveviewStringCacheUsageVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 134, 10, 1),
    _LiveviewStringCacheUsageVal_Type()
)
liveviewStringCacheUsageVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    liveviewStringCacheUsageVal.setStatus("current")
_LiveviewStringCacheUsageMax_Type = CounterBasedGauge64
_LiveviewStringCacheUsageMax_Object = MibScalar
liveviewStringCacheUsageMax = _LiveviewStringCacheUsageMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 134, 10, 3),
    _LiveviewStringCacheUsageMax_Type()
)
liveviewStringCacheUsageMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    liveviewStringCacheUsageMax.setStatus("current")
_LiveviewUnaccountedPlsdIn_ObjectIdentity = ObjectIdentity
liveviewUnaccountedPlsdIn = _LiveviewUnaccountedPlsdIn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 134, 11)
)
_LiveviewUnaccountedPlsdInVal_Type = Counter64
_LiveviewUnaccountedPlsdInVal_Object = MibScalar
liveviewUnaccountedPlsdInVal = _LiveviewUnaccountedPlsdInVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 134, 11, 1),
    _LiveviewUnaccountedPlsdInVal_Type()
)
liveviewUnaccountedPlsdInVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    liveviewUnaccountedPlsdInVal.setStatus("current")
_LiveviewUnaccountedPlsdInMom_Type = CounterBasedGauge64
_LiveviewUnaccountedPlsdInMom_Object = MibScalar
liveviewUnaccountedPlsdInMom = _LiveviewUnaccountedPlsdInMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 134, 11, 2),
    _LiveviewUnaccountedPlsdInMom_Type()
)
liveviewUnaccountedPlsdInMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    liveviewUnaccountedPlsdInMom.setStatus("current")
_LiveviewUnaccountedPlsdInMax_Type = CounterBasedGauge64
_LiveviewUnaccountedPlsdInMax_Object = MibScalar
liveviewUnaccountedPlsdInMax = _LiveviewUnaccountedPlsdInMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 134, 11, 3),
    _LiveviewUnaccountedPlsdInMax_Type()
)
liveviewUnaccountedPlsdInMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    liveviewUnaccountedPlsdInMax.setStatus("current")
_LiveviewUnaccountedPlsdOut_ObjectIdentity = ObjectIdentity
liveviewUnaccountedPlsdOut = _LiveviewUnaccountedPlsdOut_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 134, 12)
)
_LiveviewUnaccountedPlsdOutVal_Type = Counter64
_LiveviewUnaccountedPlsdOutVal_Object = MibScalar
liveviewUnaccountedPlsdOutVal = _LiveviewUnaccountedPlsdOutVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 134, 12, 1),
    _LiveviewUnaccountedPlsdOutVal_Type()
)
liveviewUnaccountedPlsdOutVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    liveviewUnaccountedPlsdOutVal.setStatus("current")
_LiveviewUnaccountedPlsdOutMom_Type = CounterBasedGauge64
_LiveviewUnaccountedPlsdOutMom_Object = MibScalar
liveviewUnaccountedPlsdOutMom = _LiveviewUnaccountedPlsdOutMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 134, 12, 2),
    _LiveviewUnaccountedPlsdOutMom_Type()
)
liveviewUnaccountedPlsdOutMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    liveviewUnaccountedPlsdOutMom.setStatus("current")
_LiveviewUnaccountedPlsdOutMax_Type = CounterBasedGauge64
_LiveviewUnaccountedPlsdOutMax_Object = MibScalar
liveviewUnaccountedPlsdOutMax = _LiveviewUnaccountedPlsdOutMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 134, 12, 3),
    _LiveviewUnaccountedPlsdOutMax_Type()
)
liveviewUnaccountedPlsdOutMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    liveviewUnaccountedPlsdOutMax.setStatus("current")
_LiveviewUnaccountedPlsdFlows_ObjectIdentity = ObjectIdentity
liveviewUnaccountedPlsdFlows = _LiveviewUnaccountedPlsdFlows_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 134, 13)
)
_LiveviewUnaccountedPlsdFlowsVal_Type = Counter64
_LiveviewUnaccountedPlsdFlowsVal_Object = MibScalar
liveviewUnaccountedPlsdFlowsVal = _LiveviewUnaccountedPlsdFlowsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 134, 13, 1),
    _LiveviewUnaccountedPlsdFlowsVal_Type()
)
liveviewUnaccountedPlsdFlowsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    liveviewUnaccountedPlsdFlowsVal.setStatus("current")
_LiveviewUnaccountedPlsdFlowsMom_Type = CounterBasedGauge64
_LiveviewUnaccountedPlsdFlowsMom_Object = MibScalar
liveviewUnaccountedPlsdFlowsMom = _LiveviewUnaccountedPlsdFlowsMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 134, 13, 2),
    _LiveviewUnaccountedPlsdFlowsMom_Type()
)
liveviewUnaccountedPlsdFlowsMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    liveviewUnaccountedPlsdFlowsMom.setStatus("current")
_LiveviewUnaccountedPlsdFlowsMax_Type = CounterBasedGauge64
_LiveviewUnaccountedPlsdFlowsMax_Object = MibScalar
liveviewUnaccountedPlsdFlowsMax = _LiveviewUnaccountedPlsdFlowsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 134, 13, 3),
    _LiveviewUnaccountedPlsdFlowsMax_Type()
)
liveviewUnaccountedPlsdFlowsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    liveviewUnaccountedPlsdFlowsMax.setStatus("current")
_LiveviewHostCacheExhausted_ObjectIdentity = ObjectIdentity
liveviewHostCacheExhausted = _LiveviewHostCacheExhausted_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 134, 14)
)
_LiveviewHostCacheExhaustedVal_Type = Counter64
_LiveviewHostCacheExhaustedVal_Object = MibScalar
liveviewHostCacheExhaustedVal = _LiveviewHostCacheExhaustedVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 134, 14, 1),
    _LiveviewHostCacheExhaustedVal_Type()
)
liveviewHostCacheExhaustedVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    liveviewHostCacheExhaustedVal.setStatus("current")
_LiveviewHostCacheExhaustedMom_Type = CounterBasedGauge64
_LiveviewHostCacheExhaustedMom_Object = MibScalar
liveviewHostCacheExhaustedMom = _LiveviewHostCacheExhaustedMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 134, 14, 2),
    _LiveviewHostCacheExhaustedMom_Type()
)
liveviewHostCacheExhaustedMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    liveviewHostCacheExhaustedMom.setStatus("current")
_LiveviewHostCacheExhaustedMax_Type = CounterBasedGauge64
_LiveviewHostCacheExhaustedMax_Object = MibScalar
liveviewHostCacheExhaustedMax = _LiveviewHostCacheExhaustedMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 134, 14, 3),
    _LiveviewHostCacheExhaustedMax_Type()
)
liveviewHostCacheExhaustedMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    liveviewHostCacheExhaustedMax.setStatus("current")
_LiveviewPropEntryUsage_ObjectIdentity = ObjectIdentity
liveviewPropEntryUsage = _LiveviewPropEntryUsage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 134, 15)
)
_LiveviewPropEntryUsageVal_Type = CounterBasedGauge64
_LiveviewPropEntryUsageVal_Object = MibScalar
liveviewPropEntryUsageVal = _LiveviewPropEntryUsageVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 134, 15, 1),
    _LiveviewPropEntryUsageVal_Type()
)
liveviewPropEntryUsageVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    liveviewPropEntryUsageVal.setStatus("current")
_LiveviewPropEntryUsageMax_Type = CounterBasedGauge64
_LiveviewPropEntryUsageMax_Object = MibScalar
liveviewPropEntryUsageMax = _LiveviewPropEntryUsageMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 134, 15, 3),
    _LiveviewPropEntryUsageMax_Type()
)
liveviewPropEntryUsageMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    liveviewPropEntryUsageMax.setStatus("current")
_LiveviewPropArrayUsage_ObjectIdentity = ObjectIdentity
liveviewPropArrayUsage = _LiveviewPropArrayUsage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 134, 16)
)
_LiveviewPropArrayUsageVal_Type = CounterBasedGauge64
_LiveviewPropArrayUsageVal_Object = MibScalar
liveviewPropArrayUsageVal = _LiveviewPropArrayUsageVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 134, 16, 1),
    _LiveviewPropArrayUsageVal_Type()
)
liveviewPropArrayUsageVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    liveviewPropArrayUsageVal.setStatus("current")
_LiveviewPropArrayUsageMax_Type = CounterBasedGauge64
_LiveviewPropArrayUsageMax_Object = MibScalar
liveviewPropArrayUsageMax = _LiveviewPropArrayUsageMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 134, 16, 3),
    _LiveviewPropArrayUsageMax_Type()
)
liveviewPropArrayUsageMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    liveviewPropArrayUsageMax.setStatus("current")
_LiveviewPropUsage_ObjectIdentity = ObjectIdentity
liveviewPropUsage = _LiveviewPropUsage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 134, 17)
)
_LiveviewPropUsageVal_Type = CounterBasedGauge64
_LiveviewPropUsageVal_Object = MibScalar
liveviewPropUsageVal = _LiveviewPropUsageVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 134, 17, 1),
    _LiveviewPropUsageVal_Type()
)
liveviewPropUsageVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    liveviewPropUsageVal.setStatus("current")
_LiveviewPropUsageMax_Type = CounterBasedGauge64
_LiveviewPropUsageMax_Object = MibScalar
liveviewPropUsageMax = _LiveviewPropUsageMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 134, 17, 3),
    _LiveviewPropUsageMax_Type()
)
liveviewPropUsageMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    liveviewPropUsageMax.setStatus("current")
_LiveviewTooManyNetobjectsOnHost_ObjectIdentity = ObjectIdentity
liveviewTooManyNetobjectsOnHost = _LiveviewTooManyNetobjectsOnHost_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 134, 18)
)
_LiveviewTooManyNetobjectsOnHostVal_Type = CounterBasedGauge64
_LiveviewTooManyNetobjectsOnHostVal_Object = MibScalar
liveviewTooManyNetobjectsOnHostVal = _LiveviewTooManyNetobjectsOnHostVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 134, 18, 1),
    _LiveviewTooManyNetobjectsOnHostVal_Type()
)
liveviewTooManyNetobjectsOnHostVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    liveviewTooManyNetobjectsOnHostVal.setStatus("current")
_LiveviewTooManyNetobjectsOnHostMax_Type = CounterBasedGauge64
_LiveviewTooManyNetobjectsOnHostMax_Object = MibScalar
liveviewTooManyNetobjectsOnHostMax = _LiveviewTooManyNetobjectsOnHostMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 134, 18, 3),
    _LiveviewTooManyNetobjectsOnHostMax_Type()
)
liveviewTooManyNetobjectsOnHostMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    liveviewTooManyNetobjectsOnHostMax.setStatus("current")
_LiveviewHostnameAllocs_ObjectIdentity = ObjectIdentity
liveviewHostnameAllocs = _LiveviewHostnameAllocs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 134, 19)
)
_LiveviewHostnameAllocsVal_Type = CounterBasedGauge64
_LiveviewHostnameAllocsVal_Object = MibScalar
liveviewHostnameAllocsVal = _LiveviewHostnameAllocsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 134, 19, 1),
    _LiveviewHostnameAllocsVal_Type()
)
liveviewHostnameAllocsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    liveviewHostnameAllocsVal.setStatus("current")
_LiveviewHostnameAllocsMax_Type = CounterBasedGauge64
_LiveviewHostnameAllocsMax_Object = MibScalar
liveviewHostnameAllocsMax = _LiveviewHostnameAllocsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 134, 19, 3),
    _LiveviewHostnameAllocsMax_Type()
)
liveviewHostnameAllocsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    liveviewHostnameAllocsMax.setStatus("current")
_LiveviewHostnameAllocFail_ObjectIdentity = ObjectIdentity
liveviewHostnameAllocFail = _LiveviewHostnameAllocFail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 134, 20)
)
_LiveviewHostnameAllocFailVal_Type = CounterBasedGauge64
_LiveviewHostnameAllocFailVal_Object = MibScalar
liveviewHostnameAllocFailVal = _LiveviewHostnameAllocFailVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 134, 20, 1),
    _LiveviewHostnameAllocFailVal_Type()
)
liveviewHostnameAllocFailVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    liveviewHostnameAllocFailVal.setStatus("current")
_LiveviewHostnameAllocFailMax_Type = CounterBasedGauge64
_LiveviewHostnameAllocFailMax_Object = MibScalar
liveviewHostnameAllocFailMax = _LiveviewHostnameAllocFailMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 134, 20, 3),
    _LiveviewHostnameAllocFailMax_Type()
)
liveviewHostnameAllocFailMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    liveviewHostnameAllocFailMax.setStatus("current")
_LiveviewReaperRecvBuf_ObjectIdentity = ObjectIdentity
liveviewReaperRecvBuf = _LiveviewReaperRecvBuf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 134, 21)
)
_LiveviewReaperRecvBufVal_Type = CounterBasedGauge64
_LiveviewReaperRecvBufVal_Object = MibScalar
liveviewReaperRecvBufVal = _LiveviewReaperRecvBufVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 134, 21, 1),
    _LiveviewReaperRecvBufVal_Type()
)
liveviewReaperRecvBufVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    liveviewReaperRecvBufVal.setStatus("current")
_LiveviewReaperRecvBufMax_Type = CounterBasedGauge64
_LiveviewReaperRecvBufMax_Object = MibScalar
liveviewReaperRecvBufMax = _LiveviewReaperRecvBufMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 134, 21, 3),
    _LiveviewReaperRecvBufMax_Type()
)
liveviewReaperRecvBufMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    liveviewReaperRecvBufMax.setStatus("current")
_LiveviewReaperSendBuf_ObjectIdentity = ObjectIdentity
liveviewReaperSendBuf = _LiveviewReaperSendBuf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 134, 22)
)
_LiveviewReaperSendBufVal_Type = CounterBasedGauge64
_LiveviewReaperSendBufVal_Object = MibScalar
liveviewReaperSendBufVal = _LiveviewReaperSendBufVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 134, 22, 1),
    _LiveviewReaperSendBufVal_Type()
)
liveviewReaperSendBufVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    liveviewReaperSendBufVal.setStatus("current")
_LiveviewReaperSendBufMax_Type = CounterBasedGauge64
_LiveviewReaperSendBufMax_Object = MibScalar
liveviewReaperSendBufMax = _LiveviewReaperSendBufMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 134, 22, 3),
    _LiveviewReaperSendBufMax_Type()
)
liveviewReaperSendBufMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    liveviewReaperSendBufMax.setStatus("current")
_LiveviewPLSDBuf_ObjectIdentity = ObjectIdentity
liveviewPLSDBuf = _LiveviewPLSDBuf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 134, 23)
)
_LiveviewPLSDBufVal_Type = CounterBasedGauge64
_LiveviewPLSDBufVal_Object = MibScalar
liveviewPLSDBufVal = _LiveviewPLSDBufVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 134, 23, 1),
    _LiveviewPLSDBufVal_Type()
)
liveviewPLSDBufVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    liveviewPLSDBufVal.setStatus("current")
_LiveviewPLSDBufMax_Type = CounterBasedGauge64
_LiveviewPLSDBufMax_Object = MibScalar
liveviewPLSDBufMax = _LiveviewPLSDBufMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 134, 23, 3),
    _LiveviewPLSDBufMax_Type()
)
liveviewPLSDBufMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    liveviewPLSDBufMax.setStatus("current")
_Lb_ObjectIdentity = ObjectIdentity
lb = _Lb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135)
)
_LbNumFp_ObjectIdentity = ObjectIdentity
lbNumFp = _LbNumFp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 1)
)
_LbNumFpVal_Type = CounterBasedGauge64
_LbNumFpVal_Object = MibScalar
lbNumFpVal = _LbNumFpVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 1, 1),
    _LbNumFpVal_Type()
)
lbNumFpVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbNumFpVal.setStatus("current")
_LbNumFpMax_Type = CounterBasedGauge64
_LbNumFpMax_Object = MibScalar
lbNumFpMax = _LbNumFpMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 1, 3),
    _LbNumFpMax_Type()
)
lbNumFpMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbNumFpMax.setStatus("current")
_LbActiveFp_ObjectIdentity = ObjectIdentity
lbActiveFp = _LbActiveFp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 2)
)
_LbActiveFpVal_Type = CounterBasedGauge64
_LbActiveFpVal_Object = MibScalar
lbActiveFpVal = _LbActiveFpVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 2, 1),
    _LbActiveFpVal_Type()
)
lbActiveFpVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbActiveFpVal.setStatus("current")
_LbActiveFpMax_Type = CounterBasedGauge64
_LbActiveFpMax_Object = MibScalar
lbActiveFpMax = _LbActiveFpMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 2, 3),
    _LbActiveFpMax_Type()
)
lbActiveFpMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbActiveFpMax.setStatus("current")
_LbRunningFp_ObjectIdentity = ObjectIdentity
lbRunningFp = _LbRunningFp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 3)
)
_LbRunningFpVal_Type = Unsigned32
_LbRunningFpVal_Object = MibScalar
lbRunningFpVal = _LbRunningFpVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 3, 1),
    _LbRunningFpVal_Type()
)
lbRunningFpVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbRunningFpVal.setStatus("current")
_LbRunningFpMax_Type = Unsigned32
_LbRunningFpMax_Object = MibScalar
lbRunningFpMax = _LbRunningFpMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 3, 3),
    _LbRunningFpMax_Type()
)
lbRunningFpMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbRunningFpMax.setStatus("current")
_LbRxPktsInt_ObjectIdentity = ObjectIdentity
lbRxPktsInt = _LbRxPktsInt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 4)
)
_LbRxPktsIntVal_Type = Counter64
_LbRxPktsIntVal_Object = MibScalar
lbRxPktsIntVal = _LbRxPktsIntVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 4, 1),
    _LbRxPktsIntVal_Type()
)
lbRxPktsIntVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbRxPktsIntVal.setStatus("current")
_LbRxPktsIntMom_Type = CounterBasedGauge64
_LbRxPktsIntMom_Object = MibScalar
lbRxPktsIntMom = _LbRxPktsIntMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 4, 2),
    _LbRxPktsIntMom_Type()
)
lbRxPktsIntMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbRxPktsIntMom.setStatus("current")
_LbRxPktsIntMax_Type = CounterBasedGauge64
_LbRxPktsIntMax_Object = MibScalar
lbRxPktsIntMax = _LbRxPktsIntMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 4, 3),
    _LbRxPktsIntMax_Type()
)
lbRxPktsIntMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbRxPktsIntMax.setStatus("current")
_LbRxPktsExt_ObjectIdentity = ObjectIdentity
lbRxPktsExt = _LbRxPktsExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 5)
)
_LbRxPktsExtVal_Type = Counter64
_LbRxPktsExtVal_Object = MibScalar
lbRxPktsExtVal = _LbRxPktsExtVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 5, 1),
    _LbRxPktsExtVal_Type()
)
lbRxPktsExtVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbRxPktsExtVal.setStatus("current")
_LbRxPktsExtMom_Type = CounterBasedGauge64
_LbRxPktsExtMom_Object = MibScalar
lbRxPktsExtMom = _LbRxPktsExtMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 5, 2),
    _LbRxPktsExtMom_Type()
)
lbRxPktsExtMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbRxPktsExtMom.setStatus("current")
_LbRxPktsExtMax_Type = CounterBasedGauge64
_LbRxPktsExtMax_Object = MibScalar
lbRxPktsExtMax = _LbRxPktsExtMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 5, 3),
    _LbRxPktsExtMax_Type()
)
lbRxPktsExtMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbRxPktsExtMax.setStatus("current")
_LbRxBytesInt_ObjectIdentity = ObjectIdentity
lbRxBytesInt = _LbRxBytesInt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 6)
)
_LbRxBytesIntVal_Type = Counter64
_LbRxBytesIntVal_Object = MibScalar
lbRxBytesIntVal = _LbRxBytesIntVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 6, 1),
    _LbRxBytesIntVal_Type()
)
lbRxBytesIntVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbRxBytesIntVal.setStatus("current")
_LbRxBytesIntMom_Type = CounterBasedGauge64
_LbRxBytesIntMom_Object = MibScalar
lbRxBytesIntMom = _LbRxBytesIntMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 6, 2),
    _LbRxBytesIntMom_Type()
)
lbRxBytesIntMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbRxBytesIntMom.setStatus("current")
_LbRxBytesIntMax_Type = CounterBasedGauge64
_LbRxBytesIntMax_Object = MibScalar
lbRxBytesIntMax = _LbRxBytesIntMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 6, 3),
    _LbRxBytesIntMax_Type()
)
lbRxBytesIntMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbRxBytesIntMax.setStatus("current")
_LbRxBytesExt_ObjectIdentity = ObjectIdentity
lbRxBytesExt = _LbRxBytesExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 7)
)
_LbRxBytesExtVal_Type = Counter64
_LbRxBytesExtVal_Object = MibScalar
lbRxBytesExtVal = _LbRxBytesExtVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 7, 1),
    _LbRxBytesExtVal_Type()
)
lbRxBytesExtVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbRxBytesExtVal.setStatus("current")
_LbRxBytesExtMom_Type = CounterBasedGauge64
_LbRxBytesExtMom_Object = MibScalar
lbRxBytesExtMom = _LbRxBytesExtMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 7, 2),
    _LbRxBytesExtMom_Type()
)
lbRxBytesExtMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbRxBytesExtMom.setStatus("current")
_LbRxBytesExtMax_Type = CounterBasedGauge64
_LbRxBytesExtMax_Object = MibScalar
lbRxBytesExtMax = _LbRxBytesExtMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 7, 3),
    _LbRxBytesExtMax_Type()
)
lbRxBytesExtMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbRxBytesExtMax.setStatus("current")
_LbRxErrorsInt_ObjectIdentity = ObjectIdentity
lbRxErrorsInt = _LbRxErrorsInt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 8)
)
_LbRxErrorsIntVal_Type = Counter64
_LbRxErrorsIntVal_Object = MibScalar
lbRxErrorsIntVal = _LbRxErrorsIntVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 8, 1),
    _LbRxErrorsIntVal_Type()
)
lbRxErrorsIntVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbRxErrorsIntVal.setStatus("current")
_LbRxErrorsIntMom_Type = CounterBasedGauge64
_LbRxErrorsIntMom_Object = MibScalar
lbRxErrorsIntMom = _LbRxErrorsIntMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 8, 2),
    _LbRxErrorsIntMom_Type()
)
lbRxErrorsIntMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbRxErrorsIntMom.setStatus("current")
_LbRxErrorsIntMax_Type = CounterBasedGauge64
_LbRxErrorsIntMax_Object = MibScalar
lbRxErrorsIntMax = _LbRxErrorsIntMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 8, 3),
    _LbRxErrorsIntMax_Type()
)
lbRxErrorsIntMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbRxErrorsIntMax.setStatus("current")
_LbRxErrorsExt_ObjectIdentity = ObjectIdentity
lbRxErrorsExt = _LbRxErrorsExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 9)
)
_LbRxErrorsExtVal_Type = Counter64
_LbRxErrorsExtVal_Object = MibScalar
lbRxErrorsExtVal = _LbRxErrorsExtVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 9, 1),
    _LbRxErrorsExtVal_Type()
)
lbRxErrorsExtVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbRxErrorsExtVal.setStatus("current")
_LbRxErrorsExtMom_Type = CounterBasedGauge64
_LbRxErrorsExtMom_Object = MibScalar
lbRxErrorsExtMom = _LbRxErrorsExtMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 9, 2),
    _LbRxErrorsExtMom_Type()
)
lbRxErrorsExtMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbRxErrorsExtMom.setStatus("current")
_LbRxErrorsExtMax_Type = CounterBasedGauge64
_LbRxErrorsExtMax_Object = MibScalar
lbRxErrorsExtMax = _LbRxErrorsExtMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 9, 3),
    _LbRxErrorsExtMax_Type()
)
lbRxErrorsExtMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbRxErrorsExtMax.setStatus("current")
_LbTxDirectInt_ObjectIdentity = ObjectIdentity
lbTxDirectInt = _LbTxDirectInt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 10)
)
_LbTxDirectIntVal_Type = Counter64
_LbTxDirectIntVal_Object = MibScalar
lbTxDirectIntVal = _LbTxDirectIntVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 10, 1),
    _LbTxDirectIntVal_Type()
)
lbTxDirectIntVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbTxDirectIntVal.setStatus("current")
_LbTxDirectIntMom_Type = CounterBasedGauge64
_LbTxDirectIntMom_Object = MibScalar
lbTxDirectIntMom = _LbTxDirectIntMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 10, 2),
    _LbTxDirectIntMom_Type()
)
lbTxDirectIntMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbTxDirectIntMom.setStatus("current")
_LbTxDirectIntMax_Type = CounterBasedGauge64
_LbTxDirectIntMax_Object = MibScalar
lbTxDirectIntMax = _LbTxDirectIntMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 10, 3),
    _LbTxDirectIntMax_Type()
)
lbTxDirectIntMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbTxDirectIntMax.setStatus("current")
_LbTxDirectExt_ObjectIdentity = ObjectIdentity
lbTxDirectExt = _LbTxDirectExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 11)
)
_LbTxDirectExtVal_Type = Counter64
_LbTxDirectExtVal_Object = MibScalar
lbTxDirectExtVal = _LbTxDirectExtVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 11, 1),
    _LbTxDirectExtVal_Type()
)
lbTxDirectExtVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbTxDirectExtVal.setStatus("current")
_LbTxDirectExtMom_Type = CounterBasedGauge64
_LbTxDirectExtMom_Object = MibScalar
lbTxDirectExtMom = _LbTxDirectExtMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 11, 2),
    _LbTxDirectExtMom_Type()
)
lbTxDirectExtMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbTxDirectExtMom.setStatus("current")
_LbTxDirectExtMax_Type = CounterBasedGauge64
_LbTxDirectExtMax_Object = MibScalar
lbTxDirectExtMax = _LbTxDirectExtMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 11, 3),
    _LbTxDirectExtMax_Type()
)
lbTxDirectExtMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbTxDirectExtMax.setStatus("current")
_LbTxDropsInt_ObjectIdentity = ObjectIdentity
lbTxDropsInt = _LbTxDropsInt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 12)
)
_LbTxDropsIntVal_Type = Counter64
_LbTxDropsIntVal_Object = MibScalar
lbTxDropsIntVal = _LbTxDropsIntVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 12, 1),
    _LbTxDropsIntVal_Type()
)
lbTxDropsIntVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbTxDropsIntVal.setStatus("current")
_LbTxDropsIntMom_Type = CounterBasedGauge64
_LbTxDropsIntMom_Object = MibScalar
lbTxDropsIntMom = _LbTxDropsIntMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 12, 2),
    _LbTxDropsIntMom_Type()
)
lbTxDropsIntMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbTxDropsIntMom.setStatus("current")
_LbTxDropsIntMax_Type = CounterBasedGauge64
_LbTxDropsIntMax_Object = MibScalar
lbTxDropsIntMax = _LbTxDropsIntMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 12, 3),
    _LbTxDropsIntMax_Type()
)
lbTxDropsIntMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbTxDropsIntMax.setStatus("current")
_LbTxDropsExt_ObjectIdentity = ObjectIdentity
lbTxDropsExt = _LbTxDropsExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 13)
)
_LbTxDropsExtVal_Type = Counter64
_LbTxDropsExtVal_Object = MibScalar
lbTxDropsExtVal = _LbTxDropsExtVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 13, 1),
    _LbTxDropsExtVal_Type()
)
lbTxDropsExtVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbTxDropsExtVal.setStatus("current")
_LbTxDropsExtMom_Type = CounterBasedGauge64
_LbTxDropsExtMom_Object = MibScalar
lbTxDropsExtMom = _LbTxDropsExtMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 13, 2),
    _LbTxDropsExtMom_Type()
)
lbTxDropsExtMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbTxDropsExtMom.setStatus("current")
_LbTxDropsExtMax_Type = CounterBasedGauge64
_LbTxDropsExtMax_Object = MibScalar
lbTxDropsExtMax = _LbTxDropsExtMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 13, 3),
    _LbTxDropsExtMax_Type()
)
lbTxDropsExtMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbTxDropsExtMax.setStatus("current")
_LbRxFsInvalidVer_ObjectIdentity = ObjectIdentity
lbRxFsInvalidVer = _LbRxFsInvalidVer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 14)
)
_LbRxFsInvalidVerVal_Type = Counter64
_LbRxFsInvalidVerVal_Object = MibScalar
lbRxFsInvalidVerVal = _LbRxFsInvalidVerVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 14, 1),
    _LbRxFsInvalidVerVal_Type()
)
lbRxFsInvalidVerVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbRxFsInvalidVerVal.setStatus("current")
_LbRxFsInvalidVerMom_Type = CounterBasedGauge64
_LbRxFsInvalidVerMom_Object = MibScalar
lbRxFsInvalidVerMom = _LbRxFsInvalidVerMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 14, 2),
    _LbRxFsInvalidVerMom_Type()
)
lbRxFsInvalidVerMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbRxFsInvalidVerMom.setStatus("current")
_LbRxFsInvalidVerMax_Type = CounterBasedGauge64
_LbRxFsInvalidVerMax_Object = MibScalar
lbRxFsInvalidVerMax = _LbRxFsInvalidVerMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 14, 3),
    _LbRxFsInvalidVerMax_Type()
)
lbRxFsInvalidVerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbRxFsInvalidVerMax.setStatus("current")
_LbShuntPktIpv4AddrInt_ObjectIdentity = ObjectIdentity
lbShuntPktIpv4AddrInt = _LbShuntPktIpv4AddrInt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 15)
)
_LbShuntPktIpv4AddrIntVal_Type = Counter64
_LbShuntPktIpv4AddrIntVal_Object = MibScalar
lbShuntPktIpv4AddrIntVal = _LbShuntPktIpv4AddrIntVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 15, 1),
    _LbShuntPktIpv4AddrIntVal_Type()
)
lbShuntPktIpv4AddrIntVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbShuntPktIpv4AddrIntVal.setStatus("current")
_LbShuntPktIpv4AddrIntMom_Type = CounterBasedGauge64
_LbShuntPktIpv4AddrIntMom_Object = MibScalar
lbShuntPktIpv4AddrIntMom = _LbShuntPktIpv4AddrIntMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 15, 2),
    _LbShuntPktIpv4AddrIntMom_Type()
)
lbShuntPktIpv4AddrIntMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbShuntPktIpv4AddrIntMom.setStatus("current")
_LbShuntPktIpv4AddrIntMax_Type = CounterBasedGauge64
_LbShuntPktIpv4AddrIntMax_Object = MibScalar
lbShuntPktIpv4AddrIntMax = _LbShuntPktIpv4AddrIntMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 15, 3),
    _LbShuntPktIpv4AddrIntMax_Type()
)
lbShuntPktIpv4AddrIntMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbShuntPktIpv4AddrIntMax.setStatus("current")
_LbShuntPktIpv4AddrExt_ObjectIdentity = ObjectIdentity
lbShuntPktIpv4AddrExt = _LbShuntPktIpv4AddrExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 16)
)
_LbShuntPktIpv4AddrExtVal_Type = Counter64
_LbShuntPktIpv4AddrExtVal_Object = MibScalar
lbShuntPktIpv4AddrExtVal = _LbShuntPktIpv4AddrExtVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 16, 1),
    _LbShuntPktIpv4AddrExtVal_Type()
)
lbShuntPktIpv4AddrExtVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbShuntPktIpv4AddrExtVal.setStatus("current")
_LbShuntPktIpv4AddrExtMom_Type = CounterBasedGauge64
_LbShuntPktIpv4AddrExtMom_Object = MibScalar
lbShuntPktIpv4AddrExtMom = _LbShuntPktIpv4AddrExtMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 16, 2),
    _LbShuntPktIpv4AddrExtMom_Type()
)
lbShuntPktIpv4AddrExtMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbShuntPktIpv4AddrExtMom.setStatus("current")
_LbShuntPktIpv4AddrExtMax_Type = CounterBasedGauge64
_LbShuntPktIpv4AddrExtMax_Object = MibScalar
lbShuntPktIpv4AddrExtMax = _LbShuntPktIpv4AddrExtMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 16, 3),
    _LbShuntPktIpv4AddrExtMax_Type()
)
lbShuntPktIpv4AddrExtMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbShuntPktIpv4AddrExtMax.setStatus("current")
_LbShuntByteIpv4AddrInt_ObjectIdentity = ObjectIdentity
lbShuntByteIpv4AddrInt = _LbShuntByteIpv4AddrInt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 17)
)
_LbShuntByteIpv4AddrIntVal_Type = Counter64
_LbShuntByteIpv4AddrIntVal_Object = MibScalar
lbShuntByteIpv4AddrIntVal = _LbShuntByteIpv4AddrIntVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 17, 1),
    _LbShuntByteIpv4AddrIntVal_Type()
)
lbShuntByteIpv4AddrIntVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbShuntByteIpv4AddrIntVal.setStatus("current")
_LbShuntByteIpv4AddrIntMom_Type = CounterBasedGauge64
_LbShuntByteIpv4AddrIntMom_Object = MibScalar
lbShuntByteIpv4AddrIntMom = _LbShuntByteIpv4AddrIntMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 17, 2),
    _LbShuntByteIpv4AddrIntMom_Type()
)
lbShuntByteIpv4AddrIntMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbShuntByteIpv4AddrIntMom.setStatus("current")
_LbShuntByteIpv4AddrIntMax_Type = CounterBasedGauge64
_LbShuntByteIpv4AddrIntMax_Object = MibScalar
lbShuntByteIpv4AddrIntMax = _LbShuntByteIpv4AddrIntMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 17, 3),
    _LbShuntByteIpv4AddrIntMax_Type()
)
lbShuntByteIpv4AddrIntMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbShuntByteIpv4AddrIntMax.setStatus("current")
_LbShuntByteIpv4AddrExt_ObjectIdentity = ObjectIdentity
lbShuntByteIpv4AddrExt = _LbShuntByteIpv4AddrExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 18)
)
_LbShuntByteIpv4AddrExtVal_Type = Counter64
_LbShuntByteIpv4AddrExtVal_Object = MibScalar
lbShuntByteIpv4AddrExtVal = _LbShuntByteIpv4AddrExtVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 18, 1),
    _LbShuntByteIpv4AddrExtVal_Type()
)
lbShuntByteIpv4AddrExtVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbShuntByteIpv4AddrExtVal.setStatus("current")
_LbShuntByteIpv4AddrExtMom_Type = CounterBasedGauge64
_LbShuntByteIpv4AddrExtMom_Object = MibScalar
lbShuntByteIpv4AddrExtMom = _LbShuntByteIpv4AddrExtMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 18, 2),
    _LbShuntByteIpv4AddrExtMom_Type()
)
lbShuntByteIpv4AddrExtMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbShuntByteIpv4AddrExtMom.setStatus("current")
_LbShuntByteIpv4AddrExtMax_Type = CounterBasedGauge64
_LbShuntByteIpv4AddrExtMax_Object = MibScalar
lbShuntByteIpv4AddrExtMax = _LbShuntByteIpv4AddrExtMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 18, 3),
    _LbShuntByteIpv4AddrExtMax_Type()
)
lbShuntByteIpv4AddrExtMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbShuntByteIpv4AddrExtMax.setStatus("current")
_LbShuntPktIpv4ProtoInt_ObjectIdentity = ObjectIdentity
lbShuntPktIpv4ProtoInt = _LbShuntPktIpv4ProtoInt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 19)
)
_LbShuntPktIpv4ProtoIntVal_Type = Counter64
_LbShuntPktIpv4ProtoIntVal_Object = MibScalar
lbShuntPktIpv4ProtoIntVal = _LbShuntPktIpv4ProtoIntVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 19, 1),
    _LbShuntPktIpv4ProtoIntVal_Type()
)
lbShuntPktIpv4ProtoIntVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbShuntPktIpv4ProtoIntVal.setStatus("current")
_LbShuntPktIpv4ProtoIntMom_Type = CounterBasedGauge64
_LbShuntPktIpv4ProtoIntMom_Object = MibScalar
lbShuntPktIpv4ProtoIntMom = _LbShuntPktIpv4ProtoIntMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 19, 2),
    _LbShuntPktIpv4ProtoIntMom_Type()
)
lbShuntPktIpv4ProtoIntMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbShuntPktIpv4ProtoIntMom.setStatus("current")
_LbShuntPktIpv4ProtoIntMax_Type = CounterBasedGauge64
_LbShuntPktIpv4ProtoIntMax_Object = MibScalar
lbShuntPktIpv4ProtoIntMax = _LbShuntPktIpv4ProtoIntMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 19, 3),
    _LbShuntPktIpv4ProtoIntMax_Type()
)
lbShuntPktIpv4ProtoIntMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbShuntPktIpv4ProtoIntMax.setStatus("current")
_LbShuntPktIpv4ProtoExt_ObjectIdentity = ObjectIdentity
lbShuntPktIpv4ProtoExt = _LbShuntPktIpv4ProtoExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 20)
)
_LbShuntPktIpv4ProtoExtVal_Type = Counter64
_LbShuntPktIpv4ProtoExtVal_Object = MibScalar
lbShuntPktIpv4ProtoExtVal = _LbShuntPktIpv4ProtoExtVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 20, 1),
    _LbShuntPktIpv4ProtoExtVal_Type()
)
lbShuntPktIpv4ProtoExtVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbShuntPktIpv4ProtoExtVal.setStatus("current")
_LbShuntPktIpv4ProtoExtMom_Type = CounterBasedGauge64
_LbShuntPktIpv4ProtoExtMom_Object = MibScalar
lbShuntPktIpv4ProtoExtMom = _LbShuntPktIpv4ProtoExtMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 20, 2),
    _LbShuntPktIpv4ProtoExtMom_Type()
)
lbShuntPktIpv4ProtoExtMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbShuntPktIpv4ProtoExtMom.setStatus("current")
_LbShuntPktIpv4ProtoExtMax_Type = CounterBasedGauge64
_LbShuntPktIpv4ProtoExtMax_Object = MibScalar
lbShuntPktIpv4ProtoExtMax = _LbShuntPktIpv4ProtoExtMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 20, 3),
    _LbShuntPktIpv4ProtoExtMax_Type()
)
lbShuntPktIpv4ProtoExtMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbShuntPktIpv4ProtoExtMax.setStatus("current")
_LbShuntByteIpv4ProtoInt_ObjectIdentity = ObjectIdentity
lbShuntByteIpv4ProtoInt = _LbShuntByteIpv4ProtoInt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 21)
)
_LbShuntByteIpv4ProtoIntVal_Type = Counter64
_LbShuntByteIpv4ProtoIntVal_Object = MibScalar
lbShuntByteIpv4ProtoIntVal = _LbShuntByteIpv4ProtoIntVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 21, 1),
    _LbShuntByteIpv4ProtoIntVal_Type()
)
lbShuntByteIpv4ProtoIntVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbShuntByteIpv4ProtoIntVal.setStatus("current")
_LbShuntByteIpv4ProtoIntMom_Type = CounterBasedGauge64
_LbShuntByteIpv4ProtoIntMom_Object = MibScalar
lbShuntByteIpv4ProtoIntMom = _LbShuntByteIpv4ProtoIntMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 21, 2),
    _LbShuntByteIpv4ProtoIntMom_Type()
)
lbShuntByteIpv4ProtoIntMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbShuntByteIpv4ProtoIntMom.setStatus("current")
_LbShuntByteIpv4ProtoIntMax_Type = CounterBasedGauge64
_LbShuntByteIpv4ProtoIntMax_Object = MibScalar
lbShuntByteIpv4ProtoIntMax = _LbShuntByteIpv4ProtoIntMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 21, 3),
    _LbShuntByteIpv4ProtoIntMax_Type()
)
lbShuntByteIpv4ProtoIntMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbShuntByteIpv4ProtoIntMax.setStatus("current")
_LbShuntByteIpv4ProtoExt_ObjectIdentity = ObjectIdentity
lbShuntByteIpv4ProtoExt = _LbShuntByteIpv4ProtoExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 22)
)
_LbShuntByteIpv4ProtoExtVal_Type = Counter64
_LbShuntByteIpv4ProtoExtVal_Object = MibScalar
lbShuntByteIpv4ProtoExtVal = _LbShuntByteIpv4ProtoExtVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 22, 1),
    _LbShuntByteIpv4ProtoExtVal_Type()
)
lbShuntByteIpv4ProtoExtVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbShuntByteIpv4ProtoExtVal.setStatus("current")
_LbShuntByteIpv4ProtoExtMom_Type = CounterBasedGauge64
_LbShuntByteIpv4ProtoExtMom_Object = MibScalar
lbShuntByteIpv4ProtoExtMom = _LbShuntByteIpv4ProtoExtMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 22, 2),
    _LbShuntByteIpv4ProtoExtMom_Type()
)
lbShuntByteIpv4ProtoExtMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbShuntByteIpv4ProtoExtMom.setStatus("current")
_LbShuntByteIpv4ProtoExtMax_Type = CounterBasedGauge64
_LbShuntByteIpv4ProtoExtMax_Object = MibScalar
lbShuntByteIpv4ProtoExtMax = _LbShuntByteIpv4ProtoExtMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 22, 3),
    _LbShuntByteIpv4ProtoExtMax_Type()
)
lbShuntByteIpv4ProtoExtMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbShuntByteIpv4ProtoExtMax.setStatus("current")
_LbShuntPktEthertypeInt_ObjectIdentity = ObjectIdentity
lbShuntPktEthertypeInt = _LbShuntPktEthertypeInt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 23)
)
_LbShuntPktEthertypeIntVal_Type = Counter64
_LbShuntPktEthertypeIntVal_Object = MibScalar
lbShuntPktEthertypeIntVal = _LbShuntPktEthertypeIntVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 23, 1),
    _LbShuntPktEthertypeIntVal_Type()
)
lbShuntPktEthertypeIntVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbShuntPktEthertypeIntVal.setStatus("current")
_LbShuntPktEthertypeIntMom_Type = CounterBasedGauge64
_LbShuntPktEthertypeIntMom_Object = MibScalar
lbShuntPktEthertypeIntMom = _LbShuntPktEthertypeIntMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 23, 2),
    _LbShuntPktEthertypeIntMom_Type()
)
lbShuntPktEthertypeIntMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbShuntPktEthertypeIntMom.setStatus("current")
_LbShuntPktEthertypeIntMax_Type = CounterBasedGauge64
_LbShuntPktEthertypeIntMax_Object = MibScalar
lbShuntPktEthertypeIntMax = _LbShuntPktEthertypeIntMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 23, 3),
    _LbShuntPktEthertypeIntMax_Type()
)
lbShuntPktEthertypeIntMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbShuntPktEthertypeIntMax.setStatus("current")
_LbShuntPktEthertypeExt_ObjectIdentity = ObjectIdentity
lbShuntPktEthertypeExt = _LbShuntPktEthertypeExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 24)
)
_LbShuntPktEthertypeExtVal_Type = Counter64
_LbShuntPktEthertypeExtVal_Object = MibScalar
lbShuntPktEthertypeExtVal = _LbShuntPktEthertypeExtVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 24, 1),
    _LbShuntPktEthertypeExtVal_Type()
)
lbShuntPktEthertypeExtVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbShuntPktEthertypeExtVal.setStatus("current")
_LbShuntPktEthertypeExtMom_Type = CounterBasedGauge64
_LbShuntPktEthertypeExtMom_Object = MibScalar
lbShuntPktEthertypeExtMom = _LbShuntPktEthertypeExtMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 24, 2),
    _LbShuntPktEthertypeExtMom_Type()
)
lbShuntPktEthertypeExtMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbShuntPktEthertypeExtMom.setStatus("current")
_LbShuntPktEthertypeExtMax_Type = CounterBasedGauge64
_LbShuntPktEthertypeExtMax_Object = MibScalar
lbShuntPktEthertypeExtMax = _LbShuntPktEthertypeExtMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 24, 3),
    _LbShuntPktEthertypeExtMax_Type()
)
lbShuntPktEthertypeExtMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbShuntPktEthertypeExtMax.setStatus("current")
_LbShuntByteEthertypeInt_ObjectIdentity = ObjectIdentity
lbShuntByteEthertypeInt = _LbShuntByteEthertypeInt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 25)
)
_LbShuntByteEthertypeIntVal_Type = Counter64
_LbShuntByteEthertypeIntVal_Object = MibScalar
lbShuntByteEthertypeIntVal = _LbShuntByteEthertypeIntVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 25, 1),
    _LbShuntByteEthertypeIntVal_Type()
)
lbShuntByteEthertypeIntVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbShuntByteEthertypeIntVal.setStatus("current")
_LbShuntByteEthertypeIntMom_Type = CounterBasedGauge64
_LbShuntByteEthertypeIntMom_Object = MibScalar
lbShuntByteEthertypeIntMom = _LbShuntByteEthertypeIntMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 25, 2),
    _LbShuntByteEthertypeIntMom_Type()
)
lbShuntByteEthertypeIntMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbShuntByteEthertypeIntMom.setStatus("current")
_LbShuntByteEthertypeIntMax_Type = CounterBasedGauge64
_LbShuntByteEthertypeIntMax_Object = MibScalar
lbShuntByteEthertypeIntMax = _LbShuntByteEthertypeIntMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 25, 3),
    _LbShuntByteEthertypeIntMax_Type()
)
lbShuntByteEthertypeIntMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbShuntByteEthertypeIntMax.setStatus("current")
_LbShuntByteEthertypeExt_ObjectIdentity = ObjectIdentity
lbShuntByteEthertypeExt = _LbShuntByteEthertypeExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 26)
)
_LbShuntByteEthertypeExtVal_Type = Counter64
_LbShuntByteEthertypeExtVal_Object = MibScalar
lbShuntByteEthertypeExtVal = _LbShuntByteEthertypeExtVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 26, 1),
    _LbShuntByteEthertypeExtVal_Type()
)
lbShuntByteEthertypeExtVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbShuntByteEthertypeExtVal.setStatus("current")
_LbShuntByteEthertypeExtMom_Type = CounterBasedGauge64
_LbShuntByteEthertypeExtMom_Object = MibScalar
lbShuntByteEthertypeExtMom = _LbShuntByteEthertypeExtMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 26, 2),
    _LbShuntByteEthertypeExtMom_Type()
)
lbShuntByteEthertypeExtMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbShuntByteEthertypeExtMom.setStatus("current")
_LbShuntByteEthertypeExtMax_Type = CounterBasedGauge64
_LbShuntByteEthertypeExtMax_Object = MibScalar
lbShuntByteEthertypeExtMax = _LbShuntByteEthertypeExtMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 26, 3),
    _LbShuntByteEthertypeExtMax_Type()
)
lbShuntByteEthertypeExtMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbShuntByteEthertypeExtMax.setStatus("current")
_LbShuntPktDot1qInt_ObjectIdentity = ObjectIdentity
lbShuntPktDot1qInt = _LbShuntPktDot1qInt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 27)
)
_LbShuntPktDot1qIntVal_Type = Counter64
_LbShuntPktDot1qIntVal_Object = MibScalar
lbShuntPktDot1qIntVal = _LbShuntPktDot1qIntVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 27, 1),
    _LbShuntPktDot1qIntVal_Type()
)
lbShuntPktDot1qIntVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbShuntPktDot1qIntVal.setStatus("current")
_LbShuntPktDot1qIntMom_Type = CounterBasedGauge64
_LbShuntPktDot1qIntMom_Object = MibScalar
lbShuntPktDot1qIntMom = _LbShuntPktDot1qIntMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 27, 2),
    _LbShuntPktDot1qIntMom_Type()
)
lbShuntPktDot1qIntMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbShuntPktDot1qIntMom.setStatus("current")
_LbShuntPktDot1qIntMax_Type = CounterBasedGauge64
_LbShuntPktDot1qIntMax_Object = MibScalar
lbShuntPktDot1qIntMax = _LbShuntPktDot1qIntMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 27, 3),
    _LbShuntPktDot1qIntMax_Type()
)
lbShuntPktDot1qIntMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbShuntPktDot1qIntMax.setStatus("current")
_LbShuntPktDot1qExt_ObjectIdentity = ObjectIdentity
lbShuntPktDot1qExt = _LbShuntPktDot1qExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 28)
)
_LbShuntPktDot1qExtVal_Type = Counter64
_LbShuntPktDot1qExtVal_Object = MibScalar
lbShuntPktDot1qExtVal = _LbShuntPktDot1qExtVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 28, 1),
    _LbShuntPktDot1qExtVal_Type()
)
lbShuntPktDot1qExtVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbShuntPktDot1qExtVal.setStatus("current")
_LbShuntPktDot1qExtMom_Type = CounterBasedGauge64
_LbShuntPktDot1qExtMom_Object = MibScalar
lbShuntPktDot1qExtMom = _LbShuntPktDot1qExtMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 28, 2),
    _LbShuntPktDot1qExtMom_Type()
)
lbShuntPktDot1qExtMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbShuntPktDot1qExtMom.setStatus("current")
_LbShuntPktDot1qExtMax_Type = CounterBasedGauge64
_LbShuntPktDot1qExtMax_Object = MibScalar
lbShuntPktDot1qExtMax = _LbShuntPktDot1qExtMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 28, 3),
    _LbShuntPktDot1qExtMax_Type()
)
lbShuntPktDot1qExtMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbShuntPktDot1qExtMax.setStatus("current")
_LbShuntByteDot1qInt_ObjectIdentity = ObjectIdentity
lbShuntByteDot1qInt = _LbShuntByteDot1qInt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 29)
)
_LbShuntByteDot1qIntVal_Type = Counter64
_LbShuntByteDot1qIntVal_Object = MibScalar
lbShuntByteDot1qIntVal = _LbShuntByteDot1qIntVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 29, 1),
    _LbShuntByteDot1qIntVal_Type()
)
lbShuntByteDot1qIntVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbShuntByteDot1qIntVal.setStatus("current")
_LbShuntByteDot1qIntMom_Type = CounterBasedGauge64
_LbShuntByteDot1qIntMom_Object = MibScalar
lbShuntByteDot1qIntMom = _LbShuntByteDot1qIntMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 29, 2),
    _LbShuntByteDot1qIntMom_Type()
)
lbShuntByteDot1qIntMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbShuntByteDot1qIntMom.setStatus("current")
_LbShuntByteDot1qIntMax_Type = CounterBasedGauge64
_LbShuntByteDot1qIntMax_Object = MibScalar
lbShuntByteDot1qIntMax = _LbShuntByteDot1qIntMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 29, 3),
    _LbShuntByteDot1qIntMax_Type()
)
lbShuntByteDot1qIntMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbShuntByteDot1qIntMax.setStatus("current")
_LbShuntByteDot1qExt_ObjectIdentity = ObjectIdentity
lbShuntByteDot1qExt = _LbShuntByteDot1qExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 30)
)
_LbShuntByteDot1qExtVal_Type = Counter64
_LbShuntByteDot1qExtVal_Object = MibScalar
lbShuntByteDot1qExtVal = _LbShuntByteDot1qExtVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 30, 1),
    _LbShuntByteDot1qExtVal_Type()
)
lbShuntByteDot1qExtVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbShuntByteDot1qExtVal.setStatus("current")
_LbShuntByteDot1qExtMom_Type = CounterBasedGauge64
_LbShuntByteDot1qExtMom_Object = MibScalar
lbShuntByteDot1qExtMom = _LbShuntByteDot1qExtMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 30, 2),
    _LbShuntByteDot1qExtMom_Type()
)
lbShuntByteDot1qExtMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbShuntByteDot1qExtMom.setStatus("current")
_LbShuntByteDot1qExtMax_Type = CounterBasedGauge64
_LbShuntByteDot1qExtMax_Object = MibScalar
lbShuntByteDot1qExtMax = _LbShuntByteDot1qExtMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 30, 3),
    _LbShuntByteDot1qExtMax_Type()
)
lbShuntByteDot1qExtMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbShuntByteDot1qExtMax.setStatus("current")
_LbShuntPktMplsInt_ObjectIdentity = ObjectIdentity
lbShuntPktMplsInt = _LbShuntPktMplsInt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 31)
)
_LbShuntPktMplsIntVal_Type = Counter64
_LbShuntPktMplsIntVal_Object = MibScalar
lbShuntPktMplsIntVal = _LbShuntPktMplsIntVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 31, 1),
    _LbShuntPktMplsIntVal_Type()
)
lbShuntPktMplsIntVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbShuntPktMplsIntVal.setStatus("current")
_LbShuntPktMplsIntMom_Type = CounterBasedGauge64
_LbShuntPktMplsIntMom_Object = MibScalar
lbShuntPktMplsIntMom = _LbShuntPktMplsIntMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 31, 2),
    _LbShuntPktMplsIntMom_Type()
)
lbShuntPktMplsIntMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbShuntPktMplsIntMom.setStatus("current")
_LbShuntPktMplsIntMax_Type = CounterBasedGauge64
_LbShuntPktMplsIntMax_Object = MibScalar
lbShuntPktMplsIntMax = _LbShuntPktMplsIntMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 31, 3),
    _LbShuntPktMplsIntMax_Type()
)
lbShuntPktMplsIntMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbShuntPktMplsIntMax.setStatus("current")
_LbShuntPktMplsExt_ObjectIdentity = ObjectIdentity
lbShuntPktMplsExt = _LbShuntPktMplsExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 32)
)
_LbShuntPktMplsExtVal_Type = Counter64
_LbShuntPktMplsExtVal_Object = MibScalar
lbShuntPktMplsExtVal = _LbShuntPktMplsExtVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 32, 1),
    _LbShuntPktMplsExtVal_Type()
)
lbShuntPktMplsExtVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbShuntPktMplsExtVal.setStatus("current")
_LbShuntPktMplsExtMom_Type = CounterBasedGauge64
_LbShuntPktMplsExtMom_Object = MibScalar
lbShuntPktMplsExtMom = _LbShuntPktMplsExtMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 32, 2),
    _LbShuntPktMplsExtMom_Type()
)
lbShuntPktMplsExtMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbShuntPktMplsExtMom.setStatus("current")
_LbShuntPktMplsExtMax_Type = CounterBasedGauge64
_LbShuntPktMplsExtMax_Object = MibScalar
lbShuntPktMplsExtMax = _LbShuntPktMplsExtMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 32, 3),
    _LbShuntPktMplsExtMax_Type()
)
lbShuntPktMplsExtMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbShuntPktMplsExtMax.setStatus("current")
_LbShuntByteMplsInt_ObjectIdentity = ObjectIdentity
lbShuntByteMplsInt = _LbShuntByteMplsInt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 33)
)
_LbShuntByteMplsIntVal_Type = Counter64
_LbShuntByteMplsIntVal_Object = MibScalar
lbShuntByteMplsIntVal = _LbShuntByteMplsIntVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 33, 1),
    _LbShuntByteMplsIntVal_Type()
)
lbShuntByteMplsIntVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbShuntByteMplsIntVal.setStatus("current")
_LbShuntByteMplsIntMom_Type = CounterBasedGauge64
_LbShuntByteMplsIntMom_Object = MibScalar
lbShuntByteMplsIntMom = _LbShuntByteMplsIntMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 33, 2),
    _LbShuntByteMplsIntMom_Type()
)
lbShuntByteMplsIntMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbShuntByteMplsIntMom.setStatus("current")
_LbShuntByteMplsIntMax_Type = CounterBasedGauge64
_LbShuntByteMplsIntMax_Object = MibScalar
lbShuntByteMplsIntMax = _LbShuntByteMplsIntMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 33, 3),
    _LbShuntByteMplsIntMax_Type()
)
lbShuntByteMplsIntMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbShuntByteMplsIntMax.setStatus("current")
_LbShuntByteMplsExt_ObjectIdentity = ObjectIdentity
lbShuntByteMplsExt = _LbShuntByteMplsExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 34)
)
_LbShuntByteMplsExtVal_Type = Counter64
_LbShuntByteMplsExtVal_Object = MibScalar
lbShuntByteMplsExtVal = _LbShuntByteMplsExtVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 34, 1),
    _LbShuntByteMplsExtVal_Type()
)
lbShuntByteMplsExtVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbShuntByteMplsExtVal.setStatus("current")
_LbShuntByteMplsExtMom_Type = CounterBasedGauge64
_LbShuntByteMplsExtMom_Object = MibScalar
lbShuntByteMplsExtMom = _LbShuntByteMplsExtMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 34, 2),
    _LbShuntByteMplsExtMom_Type()
)
lbShuntByteMplsExtMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbShuntByteMplsExtMom.setStatus("current")
_LbShuntByteMplsExtMax_Type = CounterBasedGauge64
_LbShuntByteMplsExtMax_Object = MibScalar
lbShuntByteMplsExtMax = _LbShuntByteMplsExtMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 34, 3),
    _LbShuntByteMplsExtMax_Type()
)
lbShuntByteMplsExtMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbShuntByteMplsExtMax.setStatus("current")
_LbShuntPktEomplsInt_ObjectIdentity = ObjectIdentity
lbShuntPktEomplsInt = _LbShuntPktEomplsInt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 35)
)
_LbShuntPktEomplsIntVal_Type = Counter64
_LbShuntPktEomplsIntVal_Object = MibScalar
lbShuntPktEomplsIntVal = _LbShuntPktEomplsIntVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 35, 1),
    _LbShuntPktEomplsIntVal_Type()
)
lbShuntPktEomplsIntVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbShuntPktEomplsIntVal.setStatus("current")
_LbShuntPktEomplsIntMom_Type = CounterBasedGauge64
_LbShuntPktEomplsIntMom_Object = MibScalar
lbShuntPktEomplsIntMom = _LbShuntPktEomplsIntMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 35, 2),
    _LbShuntPktEomplsIntMom_Type()
)
lbShuntPktEomplsIntMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbShuntPktEomplsIntMom.setStatus("current")
_LbShuntPktEomplsIntMax_Type = CounterBasedGauge64
_LbShuntPktEomplsIntMax_Object = MibScalar
lbShuntPktEomplsIntMax = _LbShuntPktEomplsIntMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 35, 3),
    _LbShuntPktEomplsIntMax_Type()
)
lbShuntPktEomplsIntMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbShuntPktEomplsIntMax.setStatus("current")
_LbShuntPktEomplsExt_ObjectIdentity = ObjectIdentity
lbShuntPktEomplsExt = _LbShuntPktEomplsExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 36)
)
_LbShuntPktEomplsExtVal_Type = Counter64
_LbShuntPktEomplsExtVal_Object = MibScalar
lbShuntPktEomplsExtVal = _LbShuntPktEomplsExtVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 36, 1),
    _LbShuntPktEomplsExtVal_Type()
)
lbShuntPktEomplsExtVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbShuntPktEomplsExtVal.setStatus("current")
_LbShuntPktEomplsExtMom_Type = CounterBasedGauge64
_LbShuntPktEomplsExtMom_Object = MibScalar
lbShuntPktEomplsExtMom = _LbShuntPktEomplsExtMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 36, 2),
    _LbShuntPktEomplsExtMom_Type()
)
lbShuntPktEomplsExtMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbShuntPktEomplsExtMom.setStatus("current")
_LbShuntPktEomplsExtMax_Type = CounterBasedGauge64
_LbShuntPktEomplsExtMax_Object = MibScalar
lbShuntPktEomplsExtMax = _LbShuntPktEomplsExtMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 36, 3),
    _LbShuntPktEomplsExtMax_Type()
)
lbShuntPktEomplsExtMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbShuntPktEomplsExtMax.setStatus("current")
_LbShuntByteEomplsInt_ObjectIdentity = ObjectIdentity
lbShuntByteEomplsInt = _LbShuntByteEomplsInt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 37)
)
_LbShuntByteEomplsIntVal_Type = Counter64
_LbShuntByteEomplsIntVal_Object = MibScalar
lbShuntByteEomplsIntVal = _LbShuntByteEomplsIntVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 37, 1),
    _LbShuntByteEomplsIntVal_Type()
)
lbShuntByteEomplsIntVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbShuntByteEomplsIntVal.setStatus("current")
_LbShuntByteEomplsIntMom_Type = CounterBasedGauge64
_LbShuntByteEomplsIntMom_Object = MibScalar
lbShuntByteEomplsIntMom = _LbShuntByteEomplsIntMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 37, 2),
    _LbShuntByteEomplsIntMom_Type()
)
lbShuntByteEomplsIntMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbShuntByteEomplsIntMom.setStatus("current")
_LbShuntByteEomplsIntMax_Type = CounterBasedGauge64
_LbShuntByteEomplsIntMax_Object = MibScalar
lbShuntByteEomplsIntMax = _LbShuntByteEomplsIntMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 37, 3),
    _LbShuntByteEomplsIntMax_Type()
)
lbShuntByteEomplsIntMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbShuntByteEomplsIntMax.setStatus("current")
_LbShuntByteEomplsExt_ObjectIdentity = ObjectIdentity
lbShuntByteEomplsExt = _LbShuntByteEomplsExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 38)
)
_LbShuntByteEomplsExtVal_Type = Counter64
_LbShuntByteEomplsExtVal_Object = MibScalar
lbShuntByteEomplsExtVal = _LbShuntByteEomplsExtVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 38, 1),
    _LbShuntByteEomplsExtVal_Type()
)
lbShuntByteEomplsExtVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbShuntByteEomplsExtVal.setStatus("current")
_LbShuntByteEomplsExtMom_Type = CounterBasedGauge64
_LbShuntByteEomplsExtMom_Object = MibScalar
lbShuntByteEomplsExtMom = _LbShuntByteEomplsExtMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 38, 2),
    _LbShuntByteEomplsExtMom_Type()
)
lbShuntByteEomplsExtMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbShuntByteEomplsExtMom.setStatus("current")
_LbShuntByteEomplsExtMax_Type = CounterBasedGauge64
_LbShuntByteEomplsExtMax_Object = MibScalar
lbShuntByteEomplsExtMax = _LbShuntByteEomplsExtMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 38, 3),
    _LbShuntByteEomplsExtMax_Type()
)
lbShuntByteEomplsExtMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbShuntByteEomplsExtMax.setStatus("current")
_LbLbUptime_ObjectIdentity = ObjectIdentity
lbLbUptime = _LbLbUptime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 39)
)
_LbLbUptimeVal_Type = TimeTicks
_LbLbUptimeVal_Object = MibScalar
lbLbUptimeVal = _LbLbUptimeVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 39, 1),
    _LbLbUptimeVal_Type()
)
lbLbUptimeVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbLbUptimeVal.setStatus("current")
_LbCpuLoad_ObjectIdentity = ObjectIdentity
lbCpuLoad = _LbCpuLoad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 40)
)
_LbCpuLoadVal_Type = Unsigned32
_LbCpuLoadVal_Object = MibScalar
lbCpuLoadVal = _LbCpuLoadVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 40, 1),
    _LbCpuLoadVal_Type()
)
lbCpuLoadVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbCpuLoadVal.setStatus("current")
_LbCpuLoadMax_Type = Unsigned32
_LbCpuLoadMax_Object = MibScalar
lbCpuLoadMax = _LbCpuLoadMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 40, 3),
    _LbCpuLoadMax_Type()
)
lbCpuLoadMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbCpuLoadMax.setStatus("current")
_LbShuntPktIpv6AddrInt_ObjectIdentity = ObjectIdentity
lbShuntPktIpv6AddrInt = _LbShuntPktIpv6AddrInt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 41)
)
_LbShuntPktIpv6AddrIntVal_Type = Counter64
_LbShuntPktIpv6AddrIntVal_Object = MibScalar
lbShuntPktIpv6AddrIntVal = _LbShuntPktIpv6AddrIntVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 41, 1),
    _LbShuntPktIpv6AddrIntVal_Type()
)
lbShuntPktIpv6AddrIntVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbShuntPktIpv6AddrIntVal.setStatus("current")
_LbShuntPktIpv6AddrIntMom_Type = CounterBasedGauge64
_LbShuntPktIpv6AddrIntMom_Object = MibScalar
lbShuntPktIpv6AddrIntMom = _LbShuntPktIpv6AddrIntMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 41, 2),
    _LbShuntPktIpv6AddrIntMom_Type()
)
lbShuntPktIpv6AddrIntMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbShuntPktIpv6AddrIntMom.setStatus("current")
_LbShuntPktIpv6AddrIntMax_Type = CounterBasedGauge64
_LbShuntPktIpv6AddrIntMax_Object = MibScalar
lbShuntPktIpv6AddrIntMax = _LbShuntPktIpv6AddrIntMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 41, 3),
    _LbShuntPktIpv6AddrIntMax_Type()
)
lbShuntPktIpv6AddrIntMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbShuntPktIpv6AddrIntMax.setStatus("current")
_LbShuntPktIpv6AddrExt_ObjectIdentity = ObjectIdentity
lbShuntPktIpv6AddrExt = _LbShuntPktIpv6AddrExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 42)
)
_LbShuntPktIpv6AddrExtVal_Type = Counter64
_LbShuntPktIpv6AddrExtVal_Object = MibScalar
lbShuntPktIpv6AddrExtVal = _LbShuntPktIpv6AddrExtVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 42, 1),
    _LbShuntPktIpv6AddrExtVal_Type()
)
lbShuntPktIpv6AddrExtVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbShuntPktIpv6AddrExtVal.setStatus("current")
_LbShuntPktIpv6AddrExtMom_Type = CounterBasedGauge64
_LbShuntPktIpv6AddrExtMom_Object = MibScalar
lbShuntPktIpv6AddrExtMom = _LbShuntPktIpv6AddrExtMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 42, 2),
    _LbShuntPktIpv6AddrExtMom_Type()
)
lbShuntPktIpv6AddrExtMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbShuntPktIpv6AddrExtMom.setStatus("current")
_LbShuntPktIpv6AddrExtMax_Type = CounterBasedGauge64
_LbShuntPktIpv6AddrExtMax_Object = MibScalar
lbShuntPktIpv6AddrExtMax = _LbShuntPktIpv6AddrExtMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 42, 3),
    _LbShuntPktIpv6AddrExtMax_Type()
)
lbShuntPktIpv6AddrExtMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbShuntPktIpv6AddrExtMax.setStatus("current")
_LbShuntByteIpv6AddrInt_ObjectIdentity = ObjectIdentity
lbShuntByteIpv6AddrInt = _LbShuntByteIpv6AddrInt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 43)
)
_LbShuntByteIpv6AddrIntVal_Type = Counter64
_LbShuntByteIpv6AddrIntVal_Object = MibScalar
lbShuntByteIpv6AddrIntVal = _LbShuntByteIpv6AddrIntVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 43, 1),
    _LbShuntByteIpv6AddrIntVal_Type()
)
lbShuntByteIpv6AddrIntVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbShuntByteIpv6AddrIntVal.setStatus("current")
_LbShuntByteIpv6AddrIntMom_Type = CounterBasedGauge64
_LbShuntByteIpv6AddrIntMom_Object = MibScalar
lbShuntByteIpv6AddrIntMom = _LbShuntByteIpv6AddrIntMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 43, 2),
    _LbShuntByteIpv6AddrIntMom_Type()
)
lbShuntByteIpv6AddrIntMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbShuntByteIpv6AddrIntMom.setStatus("current")
_LbShuntByteIpv6AddrIntMax_Type = CounterBasedGauge64
_LbShuntByteIpv6AddrIntMax_Object = MibScalar
lbShuntByteIpv6AddrIntMax = _LbShuntByteIpv6AddrIntMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 43, 3),
    _LbShuntByteIpv6AddrIntMax_Type()
)
lbShuntByteIpv6AddrIntMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbShuntByteIpv6AddrIntMax.setStatus("current")
_LbShuntByteIpv6AddrExt_ObjectIdentity = ObjectIdentity
lbShuntByteIpv6AddrExt = _LbShuntByteIpv6AddrExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 44)
)
_LbShuntByteIpv6AddrExtVal_Type = Counter64
_LbShuntByteIpv6AddrExtVal_Object = MibScalar
lbShuntByteIpv6AddrExtVal = _LbShuntByteIpv6AddrExtVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 44, 1),
    _LbShuntByteIpv6AddrExtVal_Type()
)
lbShuntByteIpv6AddrExtVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbShuntByteIpv6AddrExtVal.setStatus("current")
_LbShuntByteIpv6AddrExtMom_Type = CounterBasedGauge64
_LbShuntByteIpv6AddrExtMom_Object = MibScalar
lbShuntByteIpv6AddrExtMom = _LbShuntByteIpv6AddrExtMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 44, 2),
    _LbShuntByteIpv6AddrExtMom_Type()
)
lbShuntByteIpv6AddrExtMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbShuntByteIpv6AddrExtMom.setStatus("current")
_LbShuntByteIpv6AddrExtMax_Type = CounterBasedGauge64
_LbShuntByteIpv6AddrExtMax_Object = MibScalar
lbShuntByteIpv6AddrExtMax = _LbShuntByteIpv6AddrExtMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 44, 3),
    _LbShuntByteIpv6AddrExtMax_Type()
)
lbShuntByteIpv6AddrExtMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbShuntByteIpv6AddrExtMax.setStatus("current")
_LbLogicalFp_ObjectIdentity = ObjectIdentity
lbLogicalFp = _LbLogicalFp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 45)
)
_LbLogicalFpVal_Type = Unsigned32
_LbLogicalFpVal_Object = MibScalar
lbLogicalFpVal = _LbLogicalFpVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 45, 1),
    _LbLogicalFpVal_Type()
)
lbLogicalFpVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbLogicalFpVal.setStatus("current")
_LbLogicalFpMax_Type = Unsigned32
_LbLogicalFpMax_Object = MibScalar
lbLogicalFpMax = _LbLogicalFpMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 45, 3),
    _LbLogicalFpMax_Type()
)
lbLogicalFpMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbLogicalFpMax.setStatus("current")
_LbTxFs_ObjectIdentity = ObjectIdentity
lbTxFs = _LbTxFs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 46)
)
_LbTxFsVal_Type = Counter64
_LbTxFsVal_Object = MibScalar
lbTxFsVal = _LbTxFsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 46, 1),
    _LbTxFsVal_Type()
)
lbTxFsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbTxFsVal.setStatus("current")
_LbTxFsMom_Type = CounterBasedGauge64
_LbTxFsMom_Object = MibScalar
lbTxFsMom = _LbTxFsMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 46, 2),
    _LbTxFsMom_Type()
)
lbTxFsMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbTxFsMom.setStatus("current")
_LbTxFsMax_Type = CounterBasedGauge64
_LbTxFsMax_Object = MibScalar
lbTxFsMax = _LbTxFsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 46, 3),
    _LbTxFsMax_Type()
)
lbTxFsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbTxFsMax.setStatus("current")
_LbTxFpInt_ObjectIdentity = ObjectIdentity
lbTxFpInt = _LbTxFpInt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 47)
)
_LbTxFpIntVal_Type = Counter64
_LbTxFpIntVal_Object = MibScalar
lbTxFpIntVal = _LbTxFpIntVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 47, 1),
    _LbTxFpIntVal_Type()
)
lbTxFpIntVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbTxFpIntVal.setStatus("current")
_LbTxFpIntMom_Type = CounterBasedGauge64
_LbTxFpIntMom_Object = MibScalar
lbTxFpIntMom = _LbTxFpIntMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 47, 2),
    _LbTxFpIntMom_Type()
)
lbTxFpIntMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbTxFpIntMom.setStatus("current")
_LbTxFpIntMax_Type = CounterBasedGauge64
_LbTxFpIntMax_Object = MibScalar
lbTxFpIntMax = _LbTxFpIntMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 47, 3),
    _LbTxFpIntMax_Type()
)
lbTxFpIntMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbTxFpIntMax.setStatus("current")
_LbTxFpExt_ObjectIdentity = ObjectIdentity
lbTxFpExt = _LbTxFpExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 48)
)
_LbTxFpExtVal_Type = Counter64
_LbTxFpExtVal_Object = MibScalar
lbTxFpExtVal = _LbTxFpExtVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 48, 1),
    _LbTxFpExtVal_Type()
)
lbTxFpExtVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbTxFpExtVal.setStatus("current")
_LbTxFpExtMom_Type = CounterBasedGauge64
_LbTxFpExtMom_Object = MibScalar
lbTxFpExtMom = _LbTxFpExtMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 48, 2),
    _LbTxFpExtMom_Type()
)
lbTxFpExtMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbTxFpExtMom.setStatus("current")
_LbTxFpExtMax_Type = CounterBasedGauge64
_LbTxFpExtMax_Object = MibScalar
lbTxFpExtMax = _LbTxFpExtMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 48, 3),
    _LbTxFpExtMax_Type()
)
lbTxFpExtMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbTxFpExtMax.setStatus("current")
_LbHbLost_ObjectIdentity = ObjectIdentity
lbHbLost = _LbHbLost_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 49)
)
_LbHbLostVal_Type = Counter64
_LbHbLostVal_Object = MibScalar
lbHbLostVal = _LbHbLostVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 49, 1),
    _LbHbLostVal_Type()
)
lbHbLostVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbHbLostVal.setStatus("current")
_LbHbLostMom_Type = CounterBasedGauge64
_LbHbLostMom_Object = MibScalar
lbHbLostMom = _LbHbLostMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 49, 2),
    _LbHbLostMom_Type()
)
lbHbLostMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbHbLostMom.setStatus("current")
_LbHbLostMax_Type = CounterBasedGauge64
_LbHbLostMax_Object = MibScalar
lbHbLostMax = _LbHbLostMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 49, 3),
    _LbHbLostMax_Type()
)
lbHbLostMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbHbLostMax.setStatus("current")
_LbBucketMoves_ObjectIdentity = ObjectIdentity
lbBucketMoves = _LbBucketMoves_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 50)
)
_LbBucketMovesVal_Type = Counter64
_LbBucketMovesVal_Object = MibScalar
lbBucketMovesVal = _LbBucketMovesVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 50, 1),
    _LbBucketMovesVal_Type()
)
lbBucketMovesVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbBucketMovesVal.setStatus("current")
_LbBucketMovesMom_Type = CounterBasedGauge64
_LbBucketMovesMom_Object = MibScalar
lbBucketMovesMom = _LbBucketMovesMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 50, 2),
    _LbBucketMovesMom_Type()
)
lbBucketMovesMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbBucketMovesMom.setStatus("current")
_LbBucketMovesMax_Type = CounterBasedGauge64
_LbBucketMovesMax_Object = MibScalar
lbBucketMovesMax = _LbBucketMovesMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 50, 3),
    _LbBucketMovesMax_Type()
)
lbBucketMovesMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbBucketMovesMax.setStatus("current")
_LbBlacklistedBuckets_ObjectIdentity = ObjectIdentity
lbBlacklistedBuckets = _LbBlacklistedBuckets_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 51)
)
_LbBlacklistedBucketsVal_Type = CounterBasedGauge64
_LbBlacklistedBucketsVal_Object = MibScalar
lbBlacklistedBucketsVal = _LbBlacklistedBucketsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 51, 1),
    _LbBlacklistedBucketsVal_Type()
)
lbBlacklistedBucketsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbBlacklistedBucketsVal.setStatus("current")
_LbBlacklistedBucketsMax_Type = CounterBasedGauge64
_LbBlacklistedBucketsMax_Object = MibScalar
lbBlacklistedBucketsMax = _LbBlacklistedBucketsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 51, 3),
    _LbBlacklistedBucketsMax_Type()
)
lbBlacklistedBucketsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbBlacklistedBucketsMax.setStatus("current")
_LbBlacklistedPackets_ObjectIdentity = ObjectIdentity
lbBlacklistedPackets = _LbBlacklistedPackets_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 52)
)
_LbBlacklistedPacketsVal_Type = Counter64
_LbBlacklistedPacketsVal_Object = MibScalar
lbBlacklistedPacketsVal = _LbBlacklistedPacketsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 52, 1),
    _LbBlacklistedPacketsVal_Type()
)
lbBlacklistedPacketsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbBlacklistedPacketsVal.setStatus("current")
_LbBlacklistedPacketsMom_Type = CounterBasedGauge64
_LbBlacklistedPacketsMom_Object = MibScalar
lbBlacklistedPacketsMom = _LbBlacklistedPacketsMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 52, 2),
    _LbBlacklistedPacketsMom_Type()
)
lbBlacklistedPacketsMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbBlacklistedPacketsMom.setStatus("current")
_LbBlacklistedPacketsMax_Type = CounterBasedGauge64
_LbBlacklistedPacketsMax_Object = MibScalar
lbBlacklistedPacketsMax = _LbBlacklistedPacketsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 135, 52, 3),
    _LbBlacklistedPacketsMax_Type()
)
lbBlacklistedPacketsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbBlacklistedPacketsMax.setStatus("current")
_Plsd_ObjectIdentity = ObjectIdentity
plsd = _Plsd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 136)
)
_PlsdDumptime_ObjectIdentity = ObjectIdentity
plsdDumptime = _PlsdDumptime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 136, 1)
)
_PlsdDumptimeVal_Type = TimeTicks
_PlsdDumptimeVal_Object = MibScalar
plsdDumptimeVal = _PlsdDumptimeVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 136, 1, 1),
    _PlsdDumptimeVal_Type()
)
plsdDumptimeVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plsdDumptimeVal.setStatus("current")
_PlsdValuesDataset_ObjectIdentity = ObjectIdentity
plsdValuesDataset = _PlsdValuesDataset_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 136, 2)
)
_PlsdValuesDatasetVal_Type = CounterBasedGauge64
_PlsdValuesDatasetVal_Object = MibScalar
plsdValuesDatasetVal = _PlsdValuesDatasetVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 136, 2, 1),
    _PlsdValuesDatasetVal_Type()
)
plsdValuesDatasetVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plsdValuesDatasetVal.setStatus("current")
_PlsdValuesDatasetMax_Type = CounterBasedGauge64
_PlsdValuesDatasetMax_Object = MibScalar
plsdValuesDatasetMax = _PlsdValuesDatasetMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 136, 2, 3),
    _PlsdValuesDatasetMax_Type()
)
plsdValuesDatasetMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plsdValuesDatasetMax.setStatus("current")
_PlsdValuesDelayedExpand_ObjectIdentity = ObjectIdentity
plsdValuesDelayedExpand = _PlsdValuesDelayedExpand_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 136, 3)
)
_PlsdValuesDelayedExpandVal_Type = CounterBasedGauge64
_PlsdValuesDelayedExpandVal_Object = MibScalar
plsdValuesDelayedExpandVal = _PlsdValuesDelayedExpandVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 136, 3, 1),
    _PlsdValuesDelayedExpandVal_Type()
)
plsdValuesDelayedExpandVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plsdValuesDelayedExpandVal.setStatus("current")
_PlsdValuesDelayedExpandMax_Type = CounterBasedGauge64
_PlsdValuesDelayedExpandMax_Object = MibScalar
plsdValuesDelayedExpandMax = _PlsdValuesDelayedExpandMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 136, 3, 3),
    _PlsdValuesDelayedExpandMax_Type()
)
plsdValuesDelayedExpandMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plsdValuesDelayedExpandMax.setStatus("current")
_PlsdLinksDataset_ObjectIdentity = ObjectIdentity
plsdLinksDataset = _PlsdLinksDataset_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 136, 4)
)
_PlsdLinksDatasetVal_Type = CounterBasedGauge64
_PlsdLinksDatasetVal_Object = MibScalar
plsdLinksDatasetVal = _PlsdLinksDatasetVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 136, 4, 1),
    _PlsdLinksDatasetVal_Type()
)
plsdLinksDatasetVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plsdLinksDatasetVal.setStatus("current")
_PlsdLinksDatasetMax_Type = CounterBasedGauge64
_PlsdLinksDatasetMax_Object = MibScalar
plsdLinksDatasetMax = _PlsdLinksDatasetMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 136, 4, 3),
    _PlsdLinksDatasetMax_Type()
)
plsdLinksDatasetMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plsdLinksDatasetMax.setStatus("current")
_PlsdValuesAggrDataset_ObjectIdentity = ObjectIdentity
plsdValuesAggrDataset = _PlsdValuesAggrDataset_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 136, 5)
)
_PlsdValuesAggrDatasetVal_Type = CounterBasedGauge64
_PlsdValuesAggrDatasetVal_Object = MibScalar
plsdValuesAggrDatasetVal = _PlsdValuesAggrDatasetVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 136, 5, 1),
    _PlsdValuesAggrDatasetVal_Type()
)
plsdValuesAggrDatasetVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plsdValuesAggrDatasetVal.setStatus("current")
_PlsdValuesAggrDatasetMax_Type = CounterBasedGauge64
_PlsdValuesAggrDatasetMax_Object = MibScalar
plsdValuesAggrDatasetMax = _PlsdValuesAggrDatasetMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 136, 5, 3),
    _PlsdValuesAggrDatasetMax_Type()
)
plsdValuesAggrDatasetMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plsdValuesAggrDatasetMax.setStatus("current")
_PlsdValueReject_ObjectIdentity = ObjectIdentity
plsdValueReject = _PlsdValueReject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 136, 6)
)
_PlsdValueRejectVal_Type = Counter64
_PlsdValueRejectVal_Object = MibScalar
plsdValueRejectVal = _PlsdValueRejectVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 136, 6, 1),
    _PlsdValueRejectVal_Type()
)
plsdValueRejectVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plsdValueRejectVal.setStatus("current")
_PlsdValueRejectMom_Type = CounterBasedGauge64
_PlsdValueRejectMom_Object = MibScalar
plsdValueRejectMom = _PlsdValueRejectMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 136, 6, 2),
    _PlsdValueRejectMom_Type()
)
plsdValueRejectMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plsdValueRejectMom.setStatus("current")
_PlsdValueRejectMax_Type = CounterBasedGauge64
_PlsdValueRejectMax_Object = MibScalar
plsdValueRejectMax = _PlsdValueRejectMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 136, 6, 3),
    _PlsdValueRejectMax_Type()
)
plsdValueRejectMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plsdValueRejectMax.setStatus("current")
_PlsdValueRejectPrior_ObjectIdentity = ObjectIdentity
plsdValueRejectPrior = _PlsdValueRejectPrior_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 136, 7)
)
_PlsdValueRejectPriorVal_Type = Counter64
_PlsdValueRejectPriorVal_Object = MibScalar
plsdValueRejectPriorVal = _PlsdValueRejectPriorVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 136, 7, 1),
    _PlsdValueRejectPriorVal_Type()
)
plsdValueRejectPriorVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plsdValueRejectPriorVal.setStatus("current")
_PlsdValueRejectPriorMom_Type = CounterBasedGauge64
_PlsdValueRejectPriorMom_Object = MibScalar
plsdValueRejectPriorMom = _PlsdValueRejectPriorMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 136, 7, 2),
    _PlsdValueRejectPriorMom_Type()
)
plsdValueRejectPriorMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plsdValueRejectPriorMom.setStatus("current")
_PlsdValueRejectPriorMax_Type = CounterBasedGauge64
_PlsdValueRejectPriorMax_Object = MibScalar
plsdValueRejectPriorMax = _PlsdValueRejectPriorMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 136, 7, 3),
    _PlsdValueRejectPriorMax_Type()
)
plsdValueRejectPriorMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plsdValueRejectPriorMax.setStatus("current")
_PlsdValuesFiltered_ObjectIdentity = ObjectIdentity
plsdValuesFiltered = _PlsdValuesFiltered_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 136, 8)
)
_PlsdValuesFilteredVal_Type = CounterBasedGauge64
_PlsdValuesFilteredVal_Object = MibScalar
plsdValuesFilteredVal = _PlsdValuesFilteredVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 136, 8, 1),
    _PlsdValuesFilteredVal_Type()
)
plsdValuesFilteredVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plsdValuesFilteredVal.setStatus("current")
_PlsdValuesFilteredMax_Type = CounterBasedGauge64
_PlsdValuesFilteredMax_Object = MibScalar
plsdValuesFilteredMax = _PlsdValuesFilteredMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 136, 8, 3),
    _PlsdValuesFilteredMax_Type()
)
plsdValuesFilteredMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plsdValuesFilteredMax.setStatus("current")
_PlsdValuesSent_ObjectIdentity = ObjectIdentity
plsdValuesSent = _PlsdValuesSent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 136, 9)
)
_PlsdValuesSentVal_Type = CounterBasedGauge64
_PlsdValuesSentVal_Object = MibScalar
plsdValuesSentVal = _PlsdValuesSentVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 136, 9, 1),
    _PlsdValuesSentVal_Type()
)
plsdValuesSentVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plsdValuesSentVal.setStatus("current")
_PlsdValuesSentMax_Type = CounterBasedGauge64
_PlsdValuesSentMax_Object = MibScalar
plsdValuesSentMax = _PlsdValuesSentMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 136, 9, 3),
    _PlsdValuesSentMax_Type()
)
plsdValuesSentMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plsdValuesSentMax.setStatus("current")
_PlsdValueLookups_ObjectIdentity = ObjectIdentity
plsdValueLookups = _PlsdValueLookups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 136, 10)
)
_PlsdValueLookupsVal_Type = Counter64
_PlsdValueLookupsVal_Object = MibScalar
plsdValueLookupsVal = _PlsdValueLookupsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 136, 10, 1),
    _PlsdValueLookupsVal_Type()
)
plsdValueLookupsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plsdValueLookupsVal.setStatus("current")
_PlsdValueLookupsMom_Type = CounterBasedGauge64
_PlsdValueLookupsMom_Object = MibScalar
plsdValueLookupsMom = _PlsdValueLookupsMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 136, 10, 2),
    _PlsdValueLookupsMom_Type()
)
plsdValueLookupsMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plsdValueLookupsMom.setStatus("current")
_PlsdValueLookupsMax_Type = CounterBasedGauge64
_PlsdValueLookupsMax_Object = MibScalar
plsdValueLookupsMax = _PlsdValueLookupsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 136, 10, 3),
    _PlsdValueLookupsMax_Type()
)
plsdValueLookupsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plsdValueLookupsMax.setStatus("current")
_PlsdValueUpdatesBytes_ObjectIdentity = ObjectIdentity
plsdValueUpdatesBytes = _PlsdValueUpdatesBytes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 136, 11)
)
_PlsdValueUpdatesBytesVal_Type = Counter64
_PlsdValueUpdatesBytesVal_Object = MibScalar
plsdValueUpdatesBytesVal = _PlsdValueUpdatesBytesVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 136, 11, 1),
    _PlsdValueUpdatesBytesVal_Type()
)
plsdValueUpdatesBytesVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plsdValueUpdatesBytesVal.setStatus("current")
_PlsdValueUpdatesBytesMom_Type = CounterBasedGauge64
_PlsdValueUpdatesBytesMom_Object = MibScalar
plsdValueUpdatesBytesMom = _PlsdValueUpdatesBytesMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 136, 11, 2),
    _PlsdValueUpdatesBytesMom_Type()
)
plsdValueUpdatesBytesMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plsdValueUpdatesBytesMom.setStatus("current")
_PlsdValueUpdatesBytesMax_Type = CounterBasedGauge64
_PlsdValueUpdatesBytesMax_Object = MibScalar
plsdValueUpdatesBytesMax = _PlsdValueUpdatesBytesMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 136, 11, 3),
    _PlsdValueUpdatesBytesMax_Type()
)
plsdValueUpdatesBytesMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plsdValueUpdatesBytesMax.setStatus("current")
_PlsdValueUpdatesBytesHp_ObjectIdentity = ObjectIdentity
plsdValueUpdatesBytesHp = _PlsdValueUpdatesBytesHp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 136, 12)
)
_PlsdValueUpdatesBytesHpVal_Type = Counter64
_PlsdValueUpdatesBytesHpVal_Object = MibScalar
plsdValueUpdatesBytesHpVal = _PlsdValueUpdatesBytesHpVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 136, 12, 1),
    _PlsdValueUpdatesBytesHpVal_Type()
)
plsdValueUpdatesBytesHpVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plsdValueUpdatesBytesHpVal.setStatus("current")
_PlsdValueUpdatesBytesHpMom_Type = CounterBasedGauge64
_PlsdValueUpdatesBytesHpMom_Object = MibScalar
plsdValueUpdatesBytesHpMom = _PlsdValueUpdatesBytesHpMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 136, 12, 2),
    _PlsdValueUpdatesBytesHpMom_Type()
)
plsdValueUpdatesBytesHpMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plsdValueUpdatesBytesHpMom.setStatus("current")
_PlsdValueUpdatesBytesHpMax_Type = CounterBasedGauge64
_PlsdValueUpdatesBytesHpMax_Object = MibScalar
plsdValueUpdatesBytesHpMax = _PlsdValueUpdatesBytesHpMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 136, 12, 3),
    _PlsdValueUpdatesBytesHpMax_Type()
)
plsdValueUpdatesBytesHpMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plsdValueUpdatesBytesHpMax.setStatus("current")
_PlsdValueUpdatesConns_ObjectIdentity = ObjectIdentity
plsdValueUpdatesConns = _PlsdValueUpdatesConns_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 136, 13)
)
_PlsdValueUpdatesConnsVal_Type = Counter64
_PlsdValueUpdatesConnsVal_Object = MibScalar
plsdValueUpdatesConnsVal = _PlsdValueUpdatesConnsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 136, 13, 1),
    _PlsdValueUpdatesConnsVal_Type()
)
plsdValueUpdatesConnsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plsdValueUpdatesConnsVal.setStatus("current")
_PlsdValueUpdatesConnsMom_Type = CounterBasedGauge64
_PlsdValueUpdatesConnsMom_Object = MibScalar
plsdValueUpdatesConnsMom = _PlsdValueUpdatesConnsMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 136, 13, 2),
    _PlsdValueUpdatesConnsMom_Type()
)
plsdValueUpdatesConnsMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plsdValueUpdatesConnsMom.setStatus("current")
_PlsdValueUpdatesConnsMax_Type = CounterBasedGauge64
_PlsdValueUpdatesConnsMax_Object = MibScalar
plsdValueUpdatesConnsMax = _PlsdValueUpdatesConnsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 136, 13, 3),
    _PlsdValueUpdatesConnsMax_Type()
)
plsdValueUpdatesConnsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plsdValueUpdatesConnsMax.setStatus("current")
_PlsdValueUpdatesConnsHp_ObjectIdentity = ObjectIdentity
plsdValueUpdatesConnsHp = _PlsdValueUpdatesConnsHp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 136, 14)
)
_PlsdValueUpdatesConnsHpVal_Type = Counter64
_PlsdValueUpdatesConnsHpVal_Object = MibScalar
plsdValueUpdatesConnsHpVal = _PlsdValueUpdatesConnsHpVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 136, 14, 1),
    _PlsdValueUpdatesConnsHpVal_Type()
)
plsdValueUpdatesConnsHpVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plsdValueUpdatesConnsHpVal.setStatus("current")
_PlsdValueUpdatesConnsHpMom_Type = CounterBasedGauge64
_PlsdValueUpdatesConnsHpMom_Object = MibScalar
plsdValueUpdatesConnsHpMom = _PlsdValueUpdatesConnsHpMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 136, 14, 2),
    _PlsdValueUpdatesConnsHpMom_Type()
)
plsdValueUpdatesConnsHpMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plsdValueUpdatesConnsHpMom.setStatus("current")
_PlsdValueUpdatesConnsHpMax_Type = CounterBasedGauge64
_PlsdValueUpdatesConnsHpMax_Object = MibScalar
plsdValueUpdatesConnsHpMax = _PlsdValueUpdatesConnsHpMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 136, 14, 3),
    _PlsdValueUpdatesConnsHpMax_Type()
)
plsdValueUpdatesConnsHpMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plsdValueUpdatesConnsHpMax.setStatus("current")
_PlsdConnections_ObjectIdentity = ObjectIdentity
plsdConnections = _PlsdConnections_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 136, 15)
)
_PlsdConnectionsVal_Type = CounterBasedGauge64
_PlsdConnectionsVal_Object = MibScalar
plsdConnectionsVal = _PlsdConnectionsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 136, 15, 1),
    _PlsdConnectionsVal_Type()
)
plsdConnectionsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plsdConnectionsVal.setStatus("current")
_PlsdConnectionsMax_Type = CounterBasedGauge64
_PlsdConnectionsMax_Object = MibScalar
plsdConnectionsMax = _PlsdConnectionsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 136, 15, 3),
    _PlsdConnectionsMax_Type()
)
plsdConnectionsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plsdConnectionsMax.setStatus("current")
_PlsdHosts_ObjectIdentity = ObjectIdentity
plsdHosts = _PlsdHosts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 136, 16)
)
_PlsdHostsVal_Type = CounterBasedGauge64
_PlsdHostsVal_Object = MibScalar
plsdHostsVal = _PlsdHostsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 136, 16, 1),
    _PlsdHostsVal_Type()
)
plsdHostsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plsdHostsVal.setStatus("current")
_PlsdHostsMax_Type = CounterBasedGauge64
_PlsdHostsMax_Object = MibScalar
plsdHostsMax = _PlsdHostsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 136, 16, 3),
    _PlsdHostsMax_Type()
)
plsdHostsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plsdHostsMax.setStatus("current")
_PlsdConnUpdates_ObjectIdentity = ObjectIdentity
plsdConnUpdates = _PlsdConnUpdates_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 136, 17)
)
_PlsdConnUpdatesVal_Type = Counter64
_PlsdConnUpdatesVal_Object = MibScalar
plsdConnUpdatesVal = _PlsdConnUpdatesVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 136, 17, 1),
    _PlsdConnUpdatesVal_Type()
)
plsdConnUpdatesVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plsdConnUpdatesVal.setStatus("current")
_PlsdConnUpdatesMom_Type = CounterBasedGauge64
_PlsdConnUpdatesMom_Object = MibScalar
plsdConnUpdatesMom = _PlsdConnUpdatesMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 136, 17, 2),
    _PlsdConnUpdatesMom_Type()
)
plsdConnUpdatesMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plsdConnUpdatesMom.setStatus("current")
_PlsdConnUpdatesMax_Type = CounterBasedGauge64
_PlsdConnUpdatesMax_Object = MibScalar
plsdConnUpdatesMax = _PlsdConnUpdatesMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 136, 17, 3),
    _PlsdConnUpdatesMax_Type()
)
plsdConnUpdatesMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plsdConnUpdatesMax.setStatus("current")
_PlsdConnUpdatesFull_ObjectIdentity = ObjectIdentity
plsdConnUpdatesFull = _PlsdConnUpdatesFull_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 136, 18)
)
_PlsdConnUpdatesFullVal_Type = Counter64
_PlsdConnUpdatesFullVal_Object = MibScalar
plsdConnUpdatesFullVal = _PlsdConnUpdatesFullVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 136, 18, 1),
    _PlsdConnUpdatesFullVal_Type()
)
plsdConnUpdatesFullVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plsdConnUpdatesFullVal.setStatus("current")
_PlsdConnUpdatesFullMom_Type = CounterBasedGauge64
_PlsdConnUpdatesFullMom_Object = MibScalar
plsdConnUpdatesFullMom = _PlsdConnUpdatesFullMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 136, 18, 2),
    _PlsdConnUpdatesFullMom_Type()
)
plsdConnUpdatesFullMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plsdConnUpdatesFullMom.setStatus("current")
_PlsdConnUpdatesFullMax_Type = CounterBasedGauge64
_PlsdConnUpdatesFullMax_Object = MibScalar
plsdConnUpdatesFullMax = _PlsdConnUpdatesFullMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 136, 18, 3),
    _PlsdConnUpdatesFullMax_Type()
)
plsdConnUpdatesFullMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plsdConnUpdatesFullMax.setStatus("current")
_PlsdConnUpdatesNew_ObjectIdentity = ObjectIdentity
plsdConnUpdatesNew = _PlsdConnUpdatesNew_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 136, 19)
)
_PlsdConnUpdatesNewVal_Type = Counter64
_PlsdConnUpdatesNewVal_Object = MibScalar
plsdConnUpdatesNewVal = _PlsdConnUpdatesNewVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 136, 19, 1),
    _PlsdConnUpdatesNewVal_Type()
)
plsdConnUpdatesNewVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plsdConnUpdatesNewVal.setStatus("current")
_PlsdConnUpdatesNewMom_Type = CounterBasedGauge64
_PlsdConnUpdatesNewMom_Object = MibScalar
plsdConnUpdatesNewMom = _PlsdConnUpdatesNewMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 136, 19, 2),
    _PlsdConnUpdatesNewMom_Type()
)
plsdConnUpdatesNewMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plsdConnUpdatesNewMom.setStatus("current")
_PlsdConnUpdatesNewMax_Type = CounterBasedGauge64
_PlsdConnUpdatesNewMax_Object = MibScalar
plsdConnUpdatesNewMax = _PlsdConnUpdatesNewMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 136, 19, 3),
    _PlsdConnUpdatesNewMax_Type()
)
plsdConnUpdatesNewMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plsdConnUpdatesNewMax.setStatus("current")
_PlsdConnUpdatesFiltered_ObjectIdentity = ObjectIdentity
plsdConnUpdatesFiltered = _PlsdConnUpdatesFiltered_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 136, 20)
)
_PlsdConnUpdatesFilteredVal_Type = Counter64
_PlsdConnUpdatesFilteredVal_Object = MibScalar
plsdConnUpdatesFilteredVal = _PlsdConnUpdatesFilteredVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 136, 20, 1),
    _PlsdConnUpdatesFilteredVal_Type()
)
plsdConnUpdatesFilteredVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plsdConnUpdatesFilteredVal.setStatus("current")
_PlsdConnUpdatesFilteredMom_Type = CounterBasedGauge64
_PlsdConnUpdatesFilteredMom_Object = MibScalar
plsdConnUpdatesFilteredMom = _PlsdConnUpdatesFilteredMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 136, 20, 2),
    _PlsdConnUpdatesFilteredMom_Type()
)
plsdConnUpdatesFilteredMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plsdConnUpdatesFilteredMom.setStatus("current")
_PlsdConnUpdatesFilteredMax_Type = CounterBasedGauge64
_PlsdConnUpdatesFilteredMax_Object = MibScalar
plsdConnUpdatesFilteredMax = _PlsdConnUpdatesFilteredMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 136, 20, 3),
    _PlsdConnUpdatesFilteredMax_Type()
)
plsdConnUpdatesFilteredMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plsdConnUpdatesFilteredMax.setStatus("current")
_PlsdConnsDropped_ObjectIdentity = ObjectIdentity
plsdConnsDropped = _PlsdConnsDropped_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 136, 21)
)
_PlsdConnsDroppedVal_Type = Counter64
_PlsdConnsDroppedVal_Object = MibScalar
plsdConnsDroppedVal = _PlsdConnsDroppedVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 136, 21, 1),
    _PlsdConnsDroppedVal_Type()
)
plsdConnsDroppedVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plsdConnsDroppedVal.setStatus("current")
_PlsdConnsDroppedMom_Type = CounterBasedGauge64
_PlsdConnsDroppedMom_Object = MibScalar
plsdConnsDroppedMom = _PlsdConnsDroppedMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 136, 21, 2),
    _PlsdConnsDroppedMom_Type()
)
plsdConnsDroppedMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plsdConnsDroppedMom.setStatus("current")
_PlsdConnsDroppedMax_Type = CounterBasedGauge64
_PlsdConnsDroppedMax_Object = MibScalar
plsdConnsDroppedMax = _PlsdConnsDroppedMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 136, 21, 3),
    _PlsdConnsDroppedMax_Type()
)
plsdConnsDroppedMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plsdConnsDroppedMax.setStatus("current")
_PlsdConnlogConns_ObjectIdentity = ObjectIdentity
plsdConnlogConns = _PlsdConnlogConns_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 136, 22)
)
_PlsdConnlogConnsVal_Type = CounterBasedGauge64
_PlsdConnlogConnsVal_Object = MibScalar
plsdConnlogConnsVal = _PlsdConnlogConnsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 136, 22, 1),
    _PlsdConnlogConnsVal_Type()
)
plsdConnlogConnsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plsdConnlogConnsVal.setStatus("current")
_PlsdConnlogConnsMax_Type = CounterBasedGauge64
_PlsdConnlogConnsMax_Object = MibScalar
plsdConnlogConnsMax = _PlsdConnlogConnsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 136, 22, 3),
    _PlsdConnlogConnsMax_Type()
)
plsdConnlogConnsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plsdConnlogConnsMax.setStatus("current")
_PlsdConnlogConnsAdded_ObjectIdentity = ObjectIdentity
plsdConnlogConnsAdded = _PlsdConnlogConnsAdded_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 136, 23)
)
_PlsdConnlogConnsAddedVal_Type = Counter64
_PlsdConnlogConnsAddedVal_Object = MibScalar
plsdConnlogConnsAddedVal = _PlsdConnlogConnsAddedVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 136, 23, 1),
    _PlsdConnlogConnsAddedVal_Type()
)
plsdConnlogConnsAddedVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plsdConnlogConnsAddedVal.setStatus("current")
_PlsdConnlogConnsAddedMom_Type = CounterBasedGauge64
_PlsdConnlogConnsAddedMom_Object = MibScalar
plsdConnlogConnsAddedMom = _PlsdConnlogConnsAddedMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 136, 23, 2),
    _PlsdConnlogConnsAddedMom_Type()
)
plsdConnlogConnsAddedMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plsdConnlogConnsAddedMom.setStatus("current")
_PlsdConnlogConnsAddedMax_Type = CounterBasedGauge64
_PlsdConnlogConnsAddedMax_Object = MibScalar
plsdConnlogConnsAddedMax = _PlsdConnlogConnsAddedMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 136, 23, 3),
    _PlsdConnlogConnsAddedMax_Type()
)
plsdConnlogConnsAddedMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plsdConnlogConnsAddedMax.setStatus("current")
_PlsdConnlogDumptimeRemaining_ObjectIdentity = ObjectIdentity
plsdConnlogDumptimeRemaining = _PlsdConnlogDumptimeRemaining_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 136, 24)
)
_PlsdConnlogDumptimeRemainingVal_Type = TimeTicks
_PlsdConnlogDumptimeRemainingVal_Object = MibScalar
plsdConnlogDumptimeRemainingVal = _PlsdConnlogDumptimeRemainingVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 136, 24, 1),
    _PlsdConnlogDumptimeRemainingVal_Type()
)
plsdConnlogDumptimeRemainingVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plsdConnlogDumptimeRemainingVal.setStatus("current")
_PlsdConnlogConnsDumped_ObjectIdentity = ObjectIdentity
plsdConnlogConnsDumped = _PlsdConnlogConnsDumped_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 136, 25)
)
_PlsdConnlogConnsDumpedVal_Type = CounterBasedGauge64
_PlsdConnlogConnsDumpedVal_Object = MibScalar
plsdConnlogConnsDumpedVal = _PlsdConnlogConnsDumpedVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 136, 25, 1),
    _PlsdConnlogConnsDumpedVal_Type()
)
plsdConnlogConnsDumpedVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plsdConnlogConnsDumpedVal.setStatus("current")
_PlsdConnlogConnsDumpedMax_Type = CounterBasedGauge64
_PlsdConnlogConnsDumpedMax_Object = MibScalar
plsdConnlogConnsDumpedMax = _PlsdConnlogConnsDumpedMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 136, 25, 3),
    _PlsdConnlogConnsDumpedMax_Type()
)
plsdConnlogConnsDumpedMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plsdConnlogConnsDumpedMax.setStatus("current")
_PlsdConnlogDumptime_ObjectIdentity = ObjectIdentity
plsdConnlogDumptime = _PlsdConnlogDumptime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 136, 26)
)
_PlsdConnlogDumptimeVal_Type = TimeTicks
_PlsdConnlogDumptimeVal_Object = MibScalar
plsdConnlogDumptimeVal = _PlsdConnlogDumptimeVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 136, 26, 1),
    _PlsdConnlogDumptimeVal_Type()
)
plsdConnlogDumptimeVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plsdConnlogDumptimeVal.setStatus("current")
_PlsdLastdump_ObjectIdentity = ObjectIdentity
plsdLastdump = _PlsdLastdump_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 136, 27)
)
_PlsdLastdumpVal_Type = DateAndTime
_PlsdLastdumpVal_Object = MibScalar
plsdLastdumpVal = _PlsdLastdumpVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 136, 27, 1),
    _PlsdLastdumpVal_Type()
)
plsdLastdumpVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plsdLastdumpVal.setStatus("current")
_PlsdRingbufUsage_ObjectIdentity = ObjectIdentity
plsdRingbufUsage = _PlsdRingbufUsage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 136, 28)
)
_PlsdRingbufUsageVal_Type = CounterBasedGauge64
_PlsdRingbufUsageVal_Object = MibScalar
plsdRingbufUsageVal = _PlsdRingbufUsageVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 136, 28, 1),
    _PlsdRingbufUsageVal_Type()
)
plsdRingbufUsageVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plsdRingbufUsageVal.setStatus("current")
_PlsdRingbufUsageMax_Type = CounterBasedGauge64
_PlsdRingbufUsageMax_Object = MibScalar
plsdRingbufUsageMax = _PlsdRingbufUsageMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 136, 28, 3),
    _PlsdRingbufUsageMax_Type()
)
plsdRingbufUsageMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plsdRingbufUsageMax.setStatus("current")
_PlsdConnlogDrops_ObjectIdentity = ObjectIdentity
plsdConnlogDrops = _PlsdConnlogDrops_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 136, 30)
)
_PlsdConnlogDropsVal_Type = CounterBasedGauge64
_PlsdConnlogDropsVal_Object = MibScalar
plsdConnlogDropsVal = _PlsdConnlogDropsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 136, 30, 1),
    _PlsdConnlogDropsVal_Type()
)
plsdConnlogDropsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plsdConnlogDropsVal.setStatus("current")
_PlsdConnlogDropsMax_Type = CounterBasedGauge64
_PlsdConnlogDropsMax_Object = MibScalar
plsdConnlogDropsMax = _PlsdConnlogDropsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 136, 30, 3),
    _PlsdConnlogDropsMax_Type()
)
plsdConnlogDropsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plsdConnlogDropsMax.setStatus("current")
_PlsdBwUsed_ObjectIdentity = ObjectIdentity
plsdBwUsed = _PlsdBwUsed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 136, 31)
)
_PlsdBwUsedVal_Type = Counter64
_PlsdBwUsedVal_Object = MibScalar
plsdBwUsedVal = _PlsdBwUsedVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 136, 31, 1),
    _PlsdBwUsedVal_Type()
)
plsdBwUsedVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plsdBwUsedVal.setStatus("current")
_PlsdBwUsedMom_Type = CounterBasedGauge64
_PlsdBwUsedMom_Object = MibScalar
plsdBwUsedMom = _PlsdBwUsedMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 136, 31, 2),
    _PlsdBwUsedMom_Type()
)
plsdBwUsedMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plsdBwUsedMom.setStatus("current")
_PlsdBwUsedMax_Type = CounterBasedGauge64
_PlsdBwUsedMax_Object = MibScalar
plsdBwUsedMax = _PlsdBwUsedMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 136, 31, 3),
    _PlsdBwUsedMax_Type()
)
plsdBwUsedMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plsdBwUsedMax.setStatus("current")
_PlsdTimeConnected_ObjectIdentity = ObjectIdentity
plsdTimeConnected = _PlsdTimeConnected_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 136, 32)
)
_PlsdTimeConnectedVal_Type = TimeTicks
_PlsdTimeConnectedVal_Object = MibScalar
plsdTimeConnectedVal = _PlsdTimeConnectedVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 136, 32, 1),
    _PlsdTimeConnectedVal_Type()
)
plsdTimeConnectedVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plsdTimeConnectedVal.setStatus("current")
_PlsdConnects_ObjectIdentity = ObjectIdentity
plsdConnects = _PlsdConnects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 136, 33)
)
_PlsdConnectsVal_Type = CounterBasedGauge64
_PlsdConnectsVal_Object = MibScalar
plsdConnectsVal = _PlsdConnectsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 136, 33, 1),
    _PlsdConnectsVal_Type()
)
plsdConnectsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plsdConnectsVal.setStatus("current")
_PlsdConnectsMax_Type = CounterBasedGauge64
_PlsdConnectsMax_Object = MibScalar
plsdConnectsMax = _PlsdConnectsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 136, 33, 3),
    _PlsdConnectsMax_Type()
)
plsdConnectsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plsdConnectsMax.setStatus("current")
_PlsdVmsize_ObjectIdentity = ObjectIdentity
plsdVmsize = _PlsdVmsize_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 136, 34)
)
_PlsdVmsizeVal_Type = CounterBasedGauge64
_PlsdVmsizeVal_Object = MibScalar
plsdVmsizeVal = _PlsdVmsizeVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 136, 34, 1),
    _PlsdVmsizeVal_Type()
)
plsdVmsizeVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plsdVmsizeVal.setStatus("current")
_PlsdVmsizeMax_Type = CounterBasedGauge64
_PlsdVmsizeMax_Object = MibScalar
plsdVmsizeMax = _PlsdVmsizeMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 136, 34, 3),
    _PlsdVmsizeMax_Type()
)
plsdVmsizeMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plsdVmsizeMax.setStatus("current")
_PlsdVmrss_ObjectIdentity = ObjectIdentity
plsdVmrss = _PlsdVmrss_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 136, 35)
)
_PlsdVmrssVal_Type = CounterBasedGauge64
_PlsdVmrssVal_Object = MibScalar
plsdVmrssVal = _PlsdVmrssVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 136, 35, 1),
    _PlsdVmrssVal_Type()
)
plsdVmrssVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plsdVmrssVal.setStatus("current")
_PlsdVmrssMax_Type = CounterBasedGauge64
_PlsdVmrssMax_Object = MibScalar
plsdVmrssMax = _PlsdVmrssMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 136, 35, 3),
    _PlsdVmrssMax_Type()
)
plsdVmrssMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plsdVmrssMax.setStatus("current")
_PlsdConnlogIncomplete_ObjectIdentity = ObjectIdentity
plsdConnlogIncomplete = _PlsdConnlogIncomplete_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 136, 36)
)
_PlsdConnlogIncompleteVal_Type = CounterBasedGauge64
_PlsdConnlogIncompleteVal_Object = MibScalar
plsdConnlogIncompleteVal = _PlsdConnlogIncompleteVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 136, 36, 1),
    _PlsdConnlogIncompleteVal_Type()
)
plsdConnlogIncompleteVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plsdConnlogIncompleteVal.setStatus("current")
_PlsdConnlogIncompleteMax_Type = CounterBasedGauge64
_PlsdConnlogIncompleteMax_Object = MibScalar
plsdConnlogIncompleteMax = _PlsdConnlogIncompleteMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 136, 36, 3),
    _PlsdConnlogIncompleteMax_Type()
)
plsdConnlogIncompleteMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plsdConnlogIncompleteMax.setStatus("current")
_PlsdConnProp_ObjectIdentity = ObjectIdentity
plsdConnProp = _PlsdConnProp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 136, 37)
)
_PlsdConnPropVal_Type = CounterBasedGauge64
_PlsdConnPropVal_Object = MibScalar
plsdConnPropVal = _PlsdConnPropVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 136, 37, 1),
    _PlsdConnPropVal_Type()
)
plsdConnPropVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plsdConnPropVal.setStatus("current")
_PlsdConnPropMax_Type = CounterBasedGauge64
_PlsdConnPropMax_Object = MibScalar
plsdConnPropMax = _PlsdConnPropMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 136, 37, 3),
    _PlsdConnPropMax_Type()
)
plsdConnPropMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plsdConnPropMax.setStatus("current")
_PlsdConnPropHash_ObjectIdentity = ObjectIdentity
plsdConnPropHash = _PlsdConnPropHash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 136, 38)
)
_PlsdConnPropHashVal_Type = CounterBasedGauge64
_PlsdConnPropHashVal_Object = MibScalar
plsdConnPropHashVal = _PlsdConnPropHashVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 136, 38, 1),
    _PlsdConnPropHashVal_Type()
)
plsdConnPropHashVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plsdConnPropHashVal.setStatus("current")
_PlsdConnPropHashMax_Type = CounterBasedGauge64
_PlsdConnPropHashMax_Object = MibScalar
plsdConnPropHashMax = _PlsdConnPropHashMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 136, 38, 3),
    _PlsdConnPropHashMax_Type()
)
plsdConnPropHashMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plsdConnPropHashMax.setStatus("current")
_Plsw_ObjectIdentity = ObjectIdentity
plsw = _Plsw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 137)
)
_PlswDatasetStart_ObjectIdentity = ObjectIdentity
plswDatasetStart = _PlswDatasetStart_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 137, 1)
)
_PlswDatasetStartVal_Type = DateAndTime
_PlswDatasetStartVal_Object = MibScalar
plswDatasetStartVal = _PlswDatasetStartVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 137, 1, 1),
    _PlswDatasetStartVal_Type()
)
plswDatasetStartVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plswDatasetStartVal.setStatus("current")
_PlswDatasetEnd_ObjectIdentity = ObjectIdentity
plswDatasetEnd = _PlswDatasetEnd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 137, 2)
)
_PlswDatasetEndVal_Type = DateAndTime
_PlswDatasetEndVal_Object = MibScalar
plswDatasetEndVal = _PlswDatasetEndVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 137, 2, 1),
    _PlswDatasetEndVal_Type()
)
plswDatasetEndVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plswDatasetEndVal.setStatus("current")
_PlswSessions_ObjectIdentity = ObjectIdentity
plswSessions = _PlswSessions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 137, 3)
)
_PlswSessionsVal_Type = CounterBasedGauge64
_PlswSessionsVal_Object = MibScalar
plswSessionsVal = _PlswSessionsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 137, 3, 1),
    _PlswSessionsVal_Type()
)
plswSessionsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plswSessionsVal.setStatus("current")
_PlswSessionsMax_Type = CounterBasedGauge64
_PlswSessionsMax_Object = MibScalar
plswSessionsMax = _PlswSessionsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 137, 3, 3),
    _PlswSessionsMax_Type()
)
plswSessionsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plswSessionsMax.setStatus("current")
_PlswValues_ObjectIdentity = ObjectIdentity
plswValues = _PlswValues_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 137, 4)
)
_PlswValuesVal_Type = CounterBasedGauge64
_PlswValuesVal_Object = MibScalar
plswValuesVal = _PlswValuesVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 137, 4, 1),
    _PlswValuesVal_Type()
)
plswValuesVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plswValuesVal.setStatus("current")
_PlswValuesMax_Type = CounterBasedGauge64
_PlswValuesMax_Object = MibScalar
plswValuesMax = _PlswValuesMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 137, 4, 3),
    _PlswValuesMax_Type()
)
plswValuesMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plswValuesMax.setStatus("current")
_PlswValuesDropped1_ObjectIdentity = ObjectIdentity
plswValuesDropped1 = _PlswValuesDropped1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 137, 5)
)
_PlswValuesDropped1Val_Type = CounterBasedGauge64
_PlswValuesDropped1Val_Object = MibScalar
plswValuesDropped1Val = _PlswValuesDropped1Val_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 137, 5, 1),
    _PlswValuesDropped1Val_Type()
)
plswValuesDropped1Val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plswValuesDropped1Val.setStatus("current")
_PlswValuesDropped1Max_Type = CounterBasedGauge64
_PlswValuesDropped1Max_Object = MibScalar
plswValuesDropped1Max = _PlswValuesDropped1Max_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 137, 5, 3),
    _PlswValuesDropped1Max_Type()
)
plswValuesDropped1Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plswValuesDropped1Max.setStatus("current")
_PlswValuesDropped2_ObjectIdentity = ObjectIdentity
plswValuesDropped2 = _PlswValuesDropped2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 137, 6)
)
_PlswValuesDropped2Val_Type = CounterBasedGauge64
_PlswValuesDropped2Val_Object = MibScalar
plswValuesDropped2Val = _PlswValuesDropped2Val_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 137, 6, 1),
    _PlswValuesDropped2Val_Type()
)
plswValuesDropped2Val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plswValuesDropped2Val.setStatus("current")
_PlswValuesDropped2Max_Type = CounterBasedGauge64
_PlswValuesDropped2Max_Object = MibScalar
plswValuesDropped2Max = _PlswValuesDropped2Max_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 137, 6, 3),
    _PlswValuesDropped2Max_Type()
)
plswValuesDropped2Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plswValuesDropped2Max.setStatus("current")
_PlswValuesDropped3_ObjectIdentity = ObjectIdentity
plswValuesDropped3 = _PlswValuesDropped3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 137, 7)
)
_PlswValuesDropped3Val_Type = CounterBasedGauge64
_PlswValuesDropped3Val_Object = MibScalar
plswValuesDropped3Val = _PlswValuesDropped3Val_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 137, 7, 1),
    _PlswValuesDropped3Val_Type()
)
plswValuesDropped3Val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plswValuesDropped3Val.setStatus("current")
_PlswValuesDropped3Max_Type = CounterBasedGauge64
_PlswValuesDropped3Max_Object = MibScalar
plswValuesDropped3Max = _PlswValuesDropped3Max_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 137, 7, 3),
    _PlswValuesDropped3Max_Type()
)
plswValuesDropped3Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plswValuesDropped3Max.setStatus("current")
_PlswValuesDropped4_ObjectIdentity = ObjectIdentity
plswValuesDropped4 = _PlswValuesDropped4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 137, 8)
)
_PlswValuesDropped4Val_Type = CounterBasedGauge64
_PlswValuesDropped4Val_Object = MibScalar
plswValuesDropped4Val = _PlswValuesDropped4Val_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 137, 8, 1),
    _PlswValuesDropped4Val_Type()
)
plswValuesDropped4Val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plswValuesDropped4Val.setStatus("current")
_PlswValuesDropped4Max_Type = CounterBasedGauge64
_PlswValuesDropped4Max_Object = MibScalar
plswValuesDropped4Max = _PlswValuesDropped4Max_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 137, 8, 3),
    _PlswValuesDropped4Max_Type()
)
plswValuesDropped4Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plswValuesDropped4Max.setStatus("current")
_PlswNewglobal_ObjectIdentity = ObjectIdentity
plswNewglobal = _PlswNewglobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 137, 9)
)
_PlswNewglobalVal_Type = CounterBasedGauge64
_PlswNewglobalVal_Object = MibScalar
plswNewglobalVal = _PlswNewglobalVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 137, 9, 1),
    _PlswNewglobalVal_Type()
)
plswNewglobalVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plswNewglobalVal.setStatus("current")
_PlswNewglobalMax_Type = CounterBasedGauge64
_PlswNewglobalMax_Object = MibScalar
plswNewglobalMax = _PlswNewglobalMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 137, 9, 3),
    _PlswNewglobalMax_Type()
)
plswNewglobalMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plswNewglobalMax.setStatus("current")
_PlswNewcoll_ObjectIdentity = ObjectIdentity
plswNewcoll = _PlswNewcoll_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 137, 10)
)
_PlswNewcollVal_Type = CounterBasedGauge64
_PlswNewcollVal_Object = MibScalar
plswNewcollVal = _PlswNewcollVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 137, 10, 1),
    _PlswNewcollVal_Type()
)
plswNewcollVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plswNewcollVal.setStatus("current")
_PlswNewcollMax_Type = CounterBasedGauge64
_PlswNewcollMax_Object = MibScalar
plswNewcollMax = _PlswNewcollMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 137, 10, 3),
    _PlswNewcollMax_Type()
)
plswNewcollMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plswNewcollMax.setStatus("current")
_PlswNewdaily_ObjectIdentity = ObjectIdentity
plswNewdaily = _PlswNewdaily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 137, 11)
)
_PlswNewdailyVal_Type = CounterBasedGauge64
_PlswNewdailyVal_Object = MibScalar
plswNewdailyVal = _PlswNewdailyVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 137, 11, 1),
    _PlswNewdailyVal_Type()
)
plswNewdailyVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plswNewdailyVal.setStatus("current")
_PlswNewdailyMax_Type = CounterBasedGauge64
_PlswNewdailyMax_Object = MibScalar
plswNewdailyMax = _PlswNewdailyMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 137, 11, 3),
    _PlswNewdailyMax_Type()
)
plswNewdailyMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plswNewdailyMax.setStatus("current")
_PlswTupdate_ObjectIdentity = ObjectIdentity
plswTupdate = _PlswTupdate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 137, 12)
)
_PlswTupdateVal_Type = CounterBasedGauge64
_PlswTupdateVal_Object = MibScalar
plswTupdateVal = _PlswTupdateVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 137, 12, 1),
    _PlswTupdateVal_Type()
)
plswTupdateVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plswTupdateVal.setStatus("current")
_PlswTupdateMax_Type = CounterBasedGauge64
_PlswTupdateMax_Object = MibScalar
plswTupdateMax = _PlswTupdateMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 137, 12, 3),
    _PlswTupdateMax_Type()
)
plswTupdateMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plswTupdateMax.setStatus("current")
_PlswGupdate_ObjectIdentity = ObjectIdentity
plswGupdate = _PlswGupdate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 137, 13)
)
_PlswGupdateVal_Type = CounterBasedGauge64
_PlswGupdateVal_Object = MibScalar
plswGupdateVal = _PlswGupdateVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 137, 13, 1),
    _PlswGupdateVal_Type()
)
plswGupdateVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plswGupdateVal.setStatus("current")
_PlswGupdateMax_Type = CounterBasedGauge64
_PlswGupdateMax_Object = MibScalar
plswGupdateMax = _PlswGupdateMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 137, 13, 3),
    _PlswGupdateMax_Type()
)
plswGupdateMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plswGupdateMax.setStatus("current")
_PlswTimeDataset_ObjectIdentity = ObjectIdentity
plswTimeDataset = _PlswTimeDataset_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 137, 14)
)
_PlswTimeDatasetVal_Type = TimeTicks
_PlswTimeDatasetVal_Object = MibScalar
plswTimeDatasetVal = _PlswTimeDatasetVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 137, 14, 1),
    _PlswTimeDatasetVal_Type()
)
plswTimeDatasetVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plswTimeDatasetVal.setStatus("current")
_PlswTimeGlobal_ObjectIdentity = ObjectIdentity
plswTimeGlobal = _PlswTimeGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 137, 15)
)
_PlswTimeGlobalVal_Type = TimeTicks
_PlswTimeGlobalVal_Object = MibScalar
plswTimeGlobalVal = _PlswTimeGlobalVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 137, 15, 1),
    _PlswTimeGlobalVal_Type()
)
plswTimeGlobalVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plswTimeGlobalVal.setStatus("current")
_PlswTimeDaily_ObjectIdentity = ObjectIdentity
plswTimeDaily = _PlswTimeDaily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 137, 16)
)
_PlswTimeDailyVal_Type = TimeTicks
_PlswTimeDailyVal_Object = MibScalar
plswTimeDailyVal = _PlswTimeDailyVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 137, 16, 1),
    _PlswTimeDailyVal_Type()
)
plswTimeDailyVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plswTimeDailyVal.setStatus("current")
_PlswTimeTotal_ObjectIdentity = ObjectIdentity
plswTimeTotal = _PlswTimeTotal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 137, 17)
)
_PlswTimeTotalVal_Type = TimeTicks
_PlswTimeTotalVal_Object = MibScalar
plswTimeTotalVal = _PlswTimeTotalVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 137, 17, 1),
    _PlswTimeTotalVal_Type()
)
plswTimeTotalVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plswTimeTotalVal.setStatus("current")
_PlswTimeGraph_ObjectIdentity = ObjectIdentity
plswTimeGraph = _PlswTimeGraph_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 137, 18)
)
_PlswTimeGraphVal_Type = TimeTicks
_PlswTimeGraphVal_Object = MibScalar
plswTimeGraphVal = _PlswTimeGraphVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 137, 18, 1),
    _PlswTimeGraphVal_Type()
)
plswTimeGraphVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plswTimeGraphVal.setStatus("current")
_PlswGlobals_ObjectIdentity = ObjectIdentity
plswGlobals = _PlswGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 137, 19)
)
_PlswGlobalsVal_Type = CounterBasedGauge64
_PlswGlobalsVal_Object = MibScalar
plswGlobalsVal = _PlswGlobalsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 137, 19, 1),
    _PlswGlobalsVal_Type()
)
plswGlobalsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plswGlobalsVal.setStatus("current")
_PlswGlobalsMax_Type = CounterBasedGauge64
_PlswGlobalsMax_Object = MibScalar
plswGlobalsMax = _PlswGlobalsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 137, 19, 3),
    _PlswGlobalsMax_Type()
)
plswGlobalsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plswGlobalsMax.setStatus("current")
_PlswColls_ObjectIdentity = ObjectIdentity
plswColls = _PlswColls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 137, 20)
)
_PlswCollsVal_Type = CounterBasedGauge64
_PlswCollsVal_Object = MibScalar
plswCollsVal = _PlswCollsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 137, 20, 1),
    _PlswCollsVal_Type()
)
plswCollsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plswCollsVal.setStatus("current")
_PlswCollsMax_Type = CounterBasedGauge64
_PlswCollsMax_Object = MibScalar
plswCollsMax = _PlswCollsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 137, 20, 3),
    _PlswCollsMax_Type()
)
plswCollsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plswCollsMax.setStatus("current")
_PlswDailys_ObjectIdentity = ObjectIdentity
plswDailys = _PlswDailys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 137, 21)
)
_PlswDailysVal_Type = CounterBasedGauge64
_PlswDailysVal_Object = MibScalar
plswDailysVal = _PlswDailysVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 137, 21, 1),
    _PlswDailysVal_Type()
)
plswDailysVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plswDailysVal.setStatus("current")
_PlswDailysMax_Type = CounterBasedGauge64
_PlswDailysMax_Object = MibScalar
plswDailysMax = _PlswDailysMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 137, 21, 3),
    _PlswDailysMax_Type()
)
plswDailysMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plswDailysMax.setStatus("current")
_PlswBlocks_ObjectIdentity = ObjectIdentity
plswBlocks = _PlswBlocks_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 137, 22)
)
_PlswBlocksVal_Type = CounterBasedGauge64
_PlswBlocksVal_Object = MibScalar
plswBlocksVal = _PlswBlocksVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 137, 22, 1),
    _PlswBlocksVal_Type()
)
plswBlocksVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plswBlocksVal.setStatus("current")
_PlswBlocksMax_Type = CounterBasedGauge64
_PlswBlocksMax_Object = MibScalar
plswBlocksMax = _PlswBlocksMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 137, 22, 3),
    _PlswBlocksMax_Type()
)
plswBlocksMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plswBlocksMax.setStatus("current")
_PlswGraphs_ObjectIdentity = ObjectIdentity
plswGraphs = _PlswGraphs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 137, 23)
)
_PlswGraphsVal_Type = CounterBasedGauge64
_PlswGraphsVal_Object = MibScalar
plswGraphsVal = _PlswGraphsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 137, 23, 1),
    _PlswGraphsVal_Type()
)
plswGraphsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plswGraphsVal.setStatus("current")
_PlswGraphsMax_Type = CounterBasedGauge64
_PlswGraphsMax_Object = MibScalar
plswGraphsMax = _PlswGraphsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 137, 23, 3),
    _PlswGraphsMax_Type()
)
plswGraphsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plswGraphsMax.setStatus("current")
_PlswSysdiagHdUsage_ObjectIdentity = ObjectIdentity
plswSysdiagHdUsage = _PlswSysdiagHdUsage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 137, 24)
)
_PlswSysdiagHdUsageVal_Type = Unsigned32
_PlswSysdiagHdUsageVal_Object = MibScalar
plswSysdiagHdUsageVal = _PlswSysdiagHdUsageVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 137, 24, 1),
    _PlswSysdiagHdUsageVal_Type()
)
plswSysdiagHdUsageVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plswSysdiagHdUsageVal.setStatus("current")
_PlswSysdiagHdUsageMax_Type = Unsigned32
_PlswSysdiagHdUsageMax_Object = MibScalar
plswSysdiagHdUsageMax = _PlswSysdiagHdUsageMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 137, 24, 3),
    _PlswSysdiagHdUsageMax_Type()
)
plswSysdiagHdUsageMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plswSysdiagHdUsageMax.setStatus("current")
_PlswSysdiagHdSize_ObjectIdentity = ObjectIdentity
plswSysdiagHdSize = _PlswSysdiagHdSize_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 137, 25)
)
_PlswSysdiagHdSizeVal_Type = CounterBasedGauge64
_PlswSysdiagHdSizeVal_Object = MibScalar
plswSysdiagHdSizeVal = _PlswSysdiagHdSizeVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 137, 25, 1),
    _PlswSysdiagHdSizeVal_Type()
)
plswSysdiagHdSizeVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plswSysdiagHdSizeVal.setStatus("current")
_PlswSysdiagHdSizeMax_Type = CounterBasedGauge64
_PlswSysdiagHdSizeMax_Object = MibScalar
plswSysdiagHdSizeMax = _PlswSysdiagHdSizeMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 137, 25, 3),
    _PlswSysdiagHdSizeMax_Type()
)
plswSysdiagHdSizeMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plswSysdiagHdSizeMax.setStatus("current")
_PlswSystemHdUsage_ObjectIdentity = ObjectIdentity
plswSystemHdUsage = _PlswSystemHdUsage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 137, 26)
)
_PlswSystemHdUsageVal_Type = Unsigned32
_PlswSystemHdUsageVal_Object = MibScalar
plswSystemHdUsageVal = _PlswSystemHdUsageVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 137, 26, 1),
    _PlswSystemHdUsageVal_Type()
)
plswSystemHdUsageVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plswSystemHdUsageVal.setStatus("current")
_PlswSystemHdUsageMax_Type = Unsigned32
_PlswSystemHdUsageMax_Object = MibScalar
plswSystemHdUsageMax = _PlswSystemHdUsageMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 137, 26, 3),
    _PlswSystemHdUsageMax_Type()
)
plswSystemHdUsageMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plswSystemHdUsageMax.setStatus("current")
_PlswSystemHdSize_ObjectIdentity = ObjectIdentity
plswSystemHdSize = _PlswSystemHdSize_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 137, 27)
)
_PlswSystemHdSizeVal_Type = CounterBasedGauge64
_PlswSystemHdSizeVal_Object = MibScalar
plswSystemHdSizeVal = _PlswSystemHdSizeVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 137, 27, 1),
    _PlswSystemHdSizeVal_Type()
)
plswSystemHdSizeVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plswSystemHdSizeVal.setStatus("current")
_PlswSystemHdSizeMax_Type = CounterBasedGauge64
_PlswSystemHdSizeMax_Object = MibScalar
plswSystemHdSizeMax = _PlswSystemHdSizeMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 137, 27, 3),
    _PlswSystemHdSizeMax_Type()
)
plswSystemHdSizeMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plswSystemHdSizeMax.setStatus("current")
_PlswSysdiagDaySize_ObjectIdentity = ObjectIdentity
plswSysdiagDaySize = _PlswSysdiagDaySize_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 137, 28)
)
_PlswSysdiagDaySizeVal_Type = CounterBasedGauge64
_PlswSysdiagDaySizeVal_Object = MibScalar
plswSysdiagDaySizeVal = _PlswSysdiagDaySizeVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 137, 28, 1),
    _PlswSysdiagDaySizeVal_Type()
)
plswSysdiagDaySizeVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plswSysdiagDaySizeVal.setStatus("current")
_PlswSysdiagDaySizeMax_Type = CounterBasedGauge64
_PlswSysdiagDaySizeMax_Object = MibScalar
plswSysdiagDaySizeMax = _PlswSysdiagDaySizeMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 137, 28, 3),
    _PlswSysdiagDaySizeMax_Type()
)
plswSysdiagDaySizeMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plswSysdiagDaySizeMax.setStatus("current")
_PlswMemused_ObjectIdentity = ObjectIdentity
plswMemused = _PlswMemused_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 137, 29)
)
_PlswMemusedVal_Type = CounterBasedGauge64
_PlswMemusedVal_Object = MibScalar
plswMemusedVal = _PlswMemusedVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 137, 29, 1),
    _PlswMemusedVal_Type()
)
plswMemusedVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plswMemusedVal.setStatus("current")
_PlswMemusedMax_Type = CounterBasedGauge64
_PlswMemusedMax_Object = MibScalar
plswMemusedMax = _PlswMemusedMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 137, 29, 3),
    _PlswMemusedMax_Type()
)
plswMemusedMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plswMemusedMax.setStatus("current")
_RulesetCompiler_ObjectIdentity = ObjectIdentity
rulesetCompiler = _RulesetCompiler_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 138)
)
_RulesetCompilerReaperRecvBuf_ObjectIdentity = ObjectIdentity
rulesetCompilerReaperRecvBuf = _RulesetCompilerReaperRecvBuf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 138, 1)
)
_RulesetCompilerReaperRecvBufVal_Type = CounterBasedGauge64
_RulesetCompilerReaperRecvBufVal_Object = MibScalar
rulesetCompilerReaperRecvBufVal = _RulesetCompilerReaperRecvBufVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 138, 1, 1),
    _RulesetCompilerReaperRecvBufVal_Type()
)
rulesetCompilerReaperRecvBufVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rulesetCompilerReaperRecvBufVal.setStatus("current")
_RulesetCompilerReaperRecvBufMax_Type = CounterBasedGauge64
_RulesetCompilerReaperRecvBufMax_Object = MibScalar
rulesetCompilerReaperRecvBufMax = _RulesetCompilerReaperRecvBufMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 138, 1, 3),
    _RulesetCompilerReaperRecvBufMax_Type()
)
rulesetCompilerReaperRecvBufMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rulesetCompilerReaperRecvBufMax.setStatus("current")
_RulesetCompilerReaperSendBuf_ObjectIdentity = ObjectIdentity
rulesetCompilerReaperSendBuf = _RulesetCompilerReaperSendBuf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 138, 2)
)
_RulesetCompilerReaperSendBufVal_Type = CounterBasedGauge64
_RulesetCompilerReaperSendBufVal_Object = MibScalar
rulesetCompilerReaperSendBufVal = _RulesetCompilerReaperSendBufVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 138, 2, 1),
    _RulesetCompilerReaperSendBufVal_Type()
)
rulesetCompilerReaperSendBufVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rulesetCompilerReaperSendBufVal.setStatus("current")
_RulesetCompilerReaperSendBufMax_Type = CounterBasedGauge64
_RulesetCompilerReaperSendBufMax_Object = MibScalar
rulesetCompilerReaperSendBufMax = _RulesetCompilerReaperSendBufMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 138, 2, 3),
    _RulesetCompilerReaperSendBufMax_Type()
)
rulesetCompilerReaperSendBufMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rulesetCompilerReaperSendBufMax.setStatus("current")
_Ipfix_ObjectIdentity = ObjectIdentity
ipfix = _Ipfix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 139)
)
_IpfixConnections_ObjectIdentity = ObjectIdentity
ipfixConnections = _IpfixConnections_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 139, 1)
)
_IpfixConnectionsVal_Type = CounterBasedGauge64
_IpfixConnectionsVal_Object = MibScalar
ipfixConnectionsVal = _IpfixConnectionsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 139, 1, 1),
    _IpfixConnectionsVal_Type()
)
ipfixConnectionsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfixConnectionsVal.setStatus("current")
_IpfixConnectionsMax_Type = CounterBasedGauge64
_IpfixConnectionsMax_Object = MibScalar
ipfixConnectionsMax = _IpfixConnectionsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 139, 1, 3),
    _IpfixConnectionsMax_Type()
)
ipfixConnectionsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfixConnectionsMax.setStatus("current")
_IpfixConnUpdates_ObjectIdentity = ObjectIdentity
ipfixConnUpdates = _IpfixConnUpdates_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 139, 2)
)
_IpfixConnUpdatesVal_Type = Counter64
_IpfixConnUpdatesVal_Object = MibScalar
ipfixConnUpdatesVal = _IpfixConnUpdatesVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 139, 2, 1),
    _IpfixConnUpdatesVal_Type()
)
ipfixConnUpdatesVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfixConnUpdatesVal.setStatus("current")
_IpfixConnUpdatesMom_Type = CounterBasedGauge64
_IpfixConnUpdatesMom_Object = MibScalar
ipfixConnUpdatesMom = _IpfixConnUpdatesMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 139, 2, 2),
    _IpfixConnUpdatesMom_Type()
)
ipfixConnUpdatesMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfixConnUpdatesMom.setStatus("current")
_IpfixConnUpdatesMax_Type = CounterBasedGauge64
_IpfixConnUpdatesMax_Object = MibScalar
ipfixConnUpdatesMax = _IpfixConnUpdatesMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 139, 2, 3),
    _IpfixConnUpdatesMax_Type()
)
ipfixConnUpdatesMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfixConnUpdatesMax.setStatus("current")
_IpfixExportedIpv4Records_ObjectIdentity = ObjectIdentity
ipfixExportedIpv4Records = _IpfixExportedIpv4Records_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 139, 3)
)
_IpfixExportedIpv4RecordsVal_Type = Counter64
_IpfixExportedIpv4RecordsVal_Object = MibScalar
ipfixExportedIpv4RecordsVal = _IpfixExportedIpv4RecordsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 139, 3, 1),
    _IpfixExportedIpv4RecordsVal_Type()
)
ipfixExportedIpv4RecordsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfixExportedIpv4RecordsVal.setStatus("current")
_IpfixExportedIpv4RecordsMom_Type = CounterBasedGauge64
_IpfixExportedIpv4RecordsMom_Object = MibScalar
ipfixExportedIpv4RecordsMom = _IpfixExportedIpv4RecordsMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 139, 3, 2),
    _IpfixExportedIpv4RecordsMom_Type()
)
ipfixExportedIpv4RecordsMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfixExportedIpv4RecordsMom.setStatus("current")
_IpfixExportedIpv4RecordsMax_Type = CounterBasedGauge64
_IpfixExportedIpv4RecordsMax_Object = MibScalar
ipfixExportedIpv4RecordsMax = _IpfixExportedIpv4RecordsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 139, 3, 3),
    _IpfixExportedIpv4RecordsMax_Type()
)
ipfixExportedIpv4RecordsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfixExportedIpv4RecordsMax.setStatus("current")
_IpfixExportedIpv6Records_ObjectIdentity = ObjectIdentity
ipfixExportedIpv6Records = _IpfixExportedIpv6Records_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 139, 4)
)
_IpfixExportedIpv6RecordsVal_Type = Counter64
_IpfixExportedIpv6RecordsVal_Object = MibScalar
ipfixExportedIpv6RecordsVal = _IpfixExportedIpv6RecordsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 139, 4, 1),
    _IpfixExportedIpv6RecordsVal_Type()
)
ipfixExportedIpv6RecordsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfixExportedIpv6RecordsVal.setStatus("current")
_IpfixExportedIpv6RecordsMom_Type = CounterBasedGauge64
_IpfixExportedIpv6RecordsMom_Object = MibScalar
ipfixExportedIpv6RecordsMom = _IpfixExportedIpv6RecordsMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 139, 4, 2),
    _IpfixExportedIpv6RecordsMom_Type()
)
ipfixExportedIpv6RecordsMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfixExportedIpv6RecordsMom.setStatus("current")
_IpfixExportedIpv6RecordsMax_Type = CounterBasedGauge64
_IpfixExportedIpv6RecordsMax_Object = MibScalar
ipfixExportedIpv6RecordsMax = _IpfixExportedIpv6RecordsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 139, 4, 3),
    _IpfixExportedIpv6RecordsMax_Type()
)
ipfixExportedIpv6RecordsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfixExportedIpv6RecordsMax.setStatus("current")
_IpfixExportedIpv4Sets_ObjectIdentity = ObjectIdentity
ipfixExportedIpv4Sets = _IpfixExportedIpv4Sets_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 139, 5)
)
_IpfixExportedIpv4SetsVal_Type = Counter64
_IpfixExportedIpv4SetsVal_Object = MibScalar
ipfixExportedIpv4SetsVal = _IpfixExportedIpv4SetsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 139, 5, 1),
    _IpfixExportedIpv4SetsVal_Type()
)
ipfixExportedIpv4SetsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfixExportedIpv4SetsVal.setStatus("current")
_IpfixExportedIpv4SetsMom_Type = CounterBasedGauge64
_IpfixExportedIpv4SetsMom_Object = MibScalar
ipfixExportedIpv4SetsMom = _IpfixExportedIpv4SetsMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 139, 5, 2),
    _IpfixExportedIpv4SetsMom_Type()
)
ipfixExportedIpv4SetsMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfixExportedIpv4SetsMom.setStatus("current")
_IpfixExportedIpv4SetsMax_Type = CounterBasedGauge64
_IpfixExportedIpv4SetsMax_Object = MibScalar
ipfixExportedIpv4SetsMax = _IpfixExportedIpv4SetsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 139, 5, 3),
    _IpfixExportedIpv4SetsMax_Type()
)
ipfixExportedIpv4SetsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfixExportedIpv4SetsMax.setStatus("current")
_IpfixExportedIpv6Sets_ObjectIdentity = ObjectIdentity
ipfixExportedIpv6Sets = _IpfixExportedIpv6Sets_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 139, 6)
)
_IpfixExportedIpv6SetsVal_Type = Counter64
_IpfixExportedIpv6SetsVal_Object = MibScalar
ipfixExportedIpv6SetsVal = _IpfixExportedIpv6SetsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 139, 6, 1),
    _IpfixExportedIpv6SetsVal_Type()
)
ipfixExportedIpv6SetsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfixExportedIpv6SetsVal.setStatus("current")
_IpfixExportedIpv6SetsMom_Type = CounterBasedGauge64
_IpfixExportedIpv6SetsMom_Object = MibScalar
ipfixExportedIpv6SetsMom = _IpfixExportedIpv6SetsMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 139, 6, 2),
    _IpfixExportedIpv6SetsMom_Type()
)
ipfixExportedIpv6SetsMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfixExportedIpv6SetsMom.setStatus("current")
_IpfixExportedIpv6SetsMax_Type = CounterBasedGauge64
_IpfixExportedIpv6SetsMax_Object = MibScalar
ipfixExportedIpv6SetsMax = _IpfixExportedIpv6SetsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 139, 6, 3),
    _IpfixExportedIpv6SetsMax_Type()
)
ipfixExportedIpv6SetsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfixExportedIpv6SetsMax.setStatus("current")
_IpfixExportedMsgs_ObjectIdentity = ObjectIdentity
ipfixExportedMsgs = _IpfixExportedMsgs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 139, 7)
)
_IpfixExportedMsgsVal_Type = Counter64
_IpfixExportedMsgsVal_Object = MibScalar
ipfixExportedMsgsVal = _IpfixExportedMsgsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 139, 7, 1),
    _IpfixExportedMsgsVal_Type()
)
ipfixExportedMsgsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfixExportedMsgsVal.setStatus("current")
_IpfixExportedMsgsMom_Type = CounterBasedGauge64
_IpfixExportedMsgsMom_Object = MibScalar
ipfixExportedMsgsMom = _IpfixExportedMsgsMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 139, 7, 2),
    _IpfixExportedMsgsMom_Type()
)
ipfixExportedMsgsMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfixExportedMsgsMom.setStatus("current")
_IpfixExportedMsgsMax_Type = CounterBasedGauge64
_IpfixExportedMsgsMax_Object = MibScalar
ipfixExportedMsgsMax = _IpfixExportedMsgsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 1, 139, 7, 3),
    _IpfixExportedMsgsMax_Type()
)
ipfixExportedMsgsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfixExportedMsgsMax.setStatus("current")
_Channelstats_ObjectIdentity = ObjectIdentity
channelstats = _Channelstats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 2)
)
_Pl2Trap_ObjectIdentity = ObjectIdentity
pl2Trap = _Pl2Trap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 8)
)
_Snoopers_ObjectIdentity = ObjectIdentity
snoopers = _Snoopers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 10)
)
_Dynamiczones_ObjectIdentity = ObjectIdentity
dynamiczones = _Dynamiczones_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 20)
)
_Psm_ObjectIdentity = ObjectIdentity
psm = _Psm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 3)
)
_Pbs_ObjectIdentity = ObjectIdentity
pbs = _Pbs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 4)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PACKETLOGIC-MIB",
    **{"procera": procera,
       "packetlogic2": packetlogic2,
       "sysdiag": sysdiag,
       "packetprocessing": packetprocessing,
       "packetprocessingRx": packetprocessingRx,
       "packetprocessingRxVal": packetprocessingRxVal,
       "packetprocessingRxMom": packetprocessingRxMom,
       "packetprocessingRxMax": packetprocessingRxMax,
       "packetprocessingRxDrops": packetprocessingRxDrops,
       "packetprocessingRxDropsVal": packetprocessingRxDropsVal,
       "packetprocessingRxDropsMom": packetprocessingRxDropsMom,
       "packetprocessingRxDropsMax": packetprocessingRxDropsMax,
       "packetprocessingTx": packetprocessingTx,
       "packetprocessingTxVal": packetprocessingTxVal,
       "packetprocessingTxMom": packetprocessingTxMom,
       "packetprocessingTxMax": packetprocessingTxMax,
       "packetprocessingTxDrops": packetprocessingTxDrops,
       "packetprocessingTxDropsVal": packetprocessingTxDropsVal,
       "packetprocessingTxDropsMom": packetprocessingTxDropsMom,
       "packetprocessingTxDropsMax": packetprocessingTxDropsMax,
       "packetprocessingPacketPoolSize": packetprocessingPacketPoolSize,
       "packetprocessingPacketPoolSizeVal": packetprocessingPacketPoolSizeVal,
       "packetprocessingPacketPoolSizeMax": packetprocessingPacketPoolSizeMax,
       "packetprocessingDmaAllocs": packetprocessingDmaAllocs,
       "packetprocessingDmaAllocsVal": packetprocessingDmaAllocsVal,
       "packetprocessingDmaAllocsMax": packetprocessingDmaAllocsMax,
       "packetprocessingLoad": packetprocessingLoad,
       "packetprocessingLoadVal": packetprocessingLoadVal,
       "packetprocessingLoadMax": packetprocessingLoadMax,
       "packetprocessingHeapfree": packetprocessingHeapfree,
       "packetprocessingHeapfreeVal": packetprocessingHeapfreeVal,
       "packetprocessingHeapfreeMax": packetprocessingHeapfreeMax,
       "packetprocessingUptime": packetprocessingUptime,
       "packetprocessingUptimeVal": packetprocessingUptimeVal,
       "packetprocessingPushbackQueueFull": packetprocessingPushbackQueueFull,
       "packetprocessingPushbackQueueFullVal": packetprocessingPushbackQueueFullVal,
       "packetprocessingPushbackQueueFullMom": packetprocessingPushbackQueueFullMom,
       "packetprocessingPushbackQueueFullMax": packetprocessingPushbackQueueFullMax,
       "packetprocessingPushbackPackets": packetprocessingPushbackPackets,
       "packetprocessingPushbackPacketsVal": packetprocessingPushbackPacketsVal,
       "packetprocessingPushbackPacketsMom": packetprocessingPushbackPacketsMom,
       "packetprocessingPushbackPacketsMax": packetprocessingPushbackPacketsMax,
       "packetprocessingPushbackQueueSize": packetprocessingPushbackQueueSize,
       "packetprocessingPushbackQueueSizeVal": packetprocessingPushbackQueueSizeVal,
       "packetprocessingPushbackQueueSizeMax": packetprocessingPushbackQueueSizeMax,
       "packetprocessingPushbackRequeues": packetprocessingPushbackRequeues,
       "packetprocessingPushbackRequeuesVal": packetprocessingPushbackRequeuesVal,
       "packetprocessingPushbackRequeuesMom": packetprocessingPushbackRequeuesMom,
       "packetprocessingPushbackRequeuesMax": packetprocessingPushbackRequeuesMax,
       "packetprocessingBalancerDrops": packetprocessingBalancerDrops,
       "packetprocessingBalancerDropsVal": packetprocessingBalancerDropsVal,
       "packetprocessingBalancerDropsMom": packetprocessingBalancerDropsMom,
       "packetprocessingBalancerDropsMax": packetprocessingBalancerDropsMax,
       "packetprocessingNICRXDrops": packetprocessingNICRXDrops,
       "packetprocessingNICRXDropsVal": packetprocessingNICRXDropsVal,
       "packetprocessingNICRXDropsMom": packetprocessingNICRXDropsMom,
       "packetprocessingNICRXDropsMax": packetprocessingNICRXDropsMax,
       "packetprocessingBalancerQueueLength": packetprocessingBalancerQueueLength,
       "packetprocessingBalancerQueueLengthVal": packetprocessingBalancerQueueLengthVal,
       "packetprocessingBalancerQueueLengthMax": packetprocessingBalancerQueueLengthMax,
       "packetprocessingOverLoad": packetprocessingOverLoad,
       "packetprocessingOverLoadVal": packetprocessingOverLoadVal,
       "packetprocessingOverLoadMax": packetprocessingOverLoadMax,
       "drdl": drdl,
       "drdlWaitingChildren": drdlWaitingChildren,
       "drdlWaitingChildrenVal": drdlWaitingChildrenVal,
       "drdlWaitingChildrenMax": drdlWaitingChildrenMax,
       "drdlAddedChildren": drdlAddedChildren,
       "drdlAddedChildrenVal": drdlAddedChildrenVal,
       "drdlAddedChildrenMom": drdlAddedChildrenMom,
       "drdlAddedChildrenMax": drdlAddedChildrenMax,
       "drdlChildAbuses": drdlChildAbuses,
       "drdlChildAbusesVal": drdlChildAbusesVal,
       "drdlChildAbusesMom": drdlChildAbusesMom,
       "drdlChildAbusesMax": drdlChildAbusesMax,
       "drdlChildEmpty": drdlChildEmpty,
       "drdlChildEmptyVal": drdlChildEmptyVal,
       "drdlChildEmptyMom": drdlChildEmptyMom,
       "drdlChildEmptyMax": drdlChildEmptyMax,
       "drdlProp32Fail": drdlProp32Fail,
       "drdlProp32FailVal": drdlProp32FailVal,
       "drdlProp32FailMom": drdlProp32FailMom,
       "drdlProp32FailMax": drdlProp32FailMax,
       "drdlProp64Fail": drdlProp64Fail,
       "drdlProp64FailVal": drdlProp64FailVal,
       "drdlProp64FailMom": drdlProp64FailMom,
       "drdlProp64FailMax": drdlProp64FailMax,
       "drdlProp256Fail": drdlProp256Fail,
       "drdlProp256FailVal": drdlProp256FailVal,
       "drdlProp256FailMom": drdlProp256FailMom,
       "drdlProp256FailMax": drdlProp256FailMax,
       "drdlProp32Used": drdlProp32Used,
       "drdlProp32UsedVal": drdlProp32UsedVal,
       "drdlProp32UsedMax": drdlProp32UsedMax,
       "drdlProp64Used": drdlProp64Used,
       "drdlProp64UsedVal": drdlProp64UsedVal,
       "drdlProp64UsedMom": drdlProp64UsedMom,
       "drdlProp64UsedMax": drdlProp64UsedMax,
       "drdlProp256Used": drdlProp256Used,
       "drdlProp256UsedVal": drdlProp256UsedVal,
       "drdlProp256UsedMax": drdlProp256UsedMax,
       "drdlAnalyzerChecks": drdlAnalyzerChecks,
       "drdlAnalyzerChecksVal": drdlAnalyzerChecksVal,
       "drdlAnalyzerChecksMom": drdlAnalyzerChecksMom,
       "drdlAnalyzerChecksMax": drdlAnalyzerChecksMax,
       "drdlAnalyzerCheckedBytes": drdlAnalyzerCheckedBytes,
       "drdlAnalyzerCheckedBytesVal": drdlAnalyzerCheckedBytesVal,
       "drdlAnalyzerCheckedBytesMom": drdlAnalyzerCheckedBytesMom,
       "drdlAnalyzerCheckedBytesMax": drdlAnalyzerCheckedBytesMax,
       "drdlAnalyzerSkippedBytes": drdlAnalyzerSkippedBytes,
       "drdlAnalyzerSkippedBytesVal": drdlAnalyzerSkippedBytesVal,
       "drdlAnalyzerSkippedBytesMom": drdlAnalyzerSkippedBytesMom,
       "drdlAnalyzerSkippedBytesMax": drdlAnalyzerSkippedBytesMax,
       "drdlAnalyzerActions": drdlAnalyzerActions,
       "drdlAnalyzerActionsVal": drdlAnalyzerActionsVal,
       "drdlAnalyzerActionsMom": drdlAnalyzerActionsMom,
       "drdlAnalyzerActionsMax": drdlAnalyzerActionsMax,
       "drdlPropertySet": drdlPropertySet,
       "drdlPropertySetVal": drdlPropertySetVal,
       "drdlPropertySetMom": drdlPropertySetMom,
       "drdlPropertySetMax": drdlPropertySetMax,
       "drdlOrphans": drdlOrphans,
       "drdlOrphansVal": drdlOrphansVal,
       "drdlOrphansMom": drdlOrphansMom,
       "drdlOrphansMax": drdlOrphansMax,
       "drdlAutoAccepts": drdlAutoAccepts,
       "drdlAutoAcceptsVal": drdlAutoAcceptsVal,
       "drdlAutoAcceptsMom": drdlAutoAcceptsMom,
       "drdlAutoAcceptsMax": drdlAutoAcceptsMax,
       "drdlBuffersUsed": drdlBuffersUsed,
       "drdlBuffersUsedVal": drdlBuffersUsedVal,
       "drdlBuffersUsedMax": drdlBuffersUsedMax,
       "drdlBufferAllocationFailures": drdlBufferAllocationFailures,
       "drdlBufferAllocationFailuresVal": drdlBufferAllocationFailuresVal,
       "drdlBufferAllocationFailuresMom": drdlBufferAllocationFailuresMom,
       "drdlBufferAllocationFailuresMax": drdlBufferAllocationFailuresMax,
       "drdlFullPackets": drdlFullPackets,
       "drdlFullPacketsVal": drdlFullPacketsVal,
       "drdlFullPacketsMom": drdlFullPacketsMom,
       "drdlFullPacketsMax": drdlFullPacketsMax,
       "drdlProp0Fail": drdlProp0Fail,
       "drdlProp0FailVal": drdlProp0FailVal,
       "drdlProp0FailMax": drdlProp0FailMax,
       "drdlProp0Used": drdlProp0Used,
       "drdlProp0UsedVal": drdlProp0UsedVal,
       "drdlProp0UsedMax": drdlProp0UsedMax,
       "drdlSliceStateUsed": drdlSliceStateUsed,
       "drdlSliceStateUsedVal": drdlSliceStateUsedVal,
       "drdlSliceStateUsedMax": drdlSliceStateUsedMax,
       "drdlSliceStateFail": drdlSliceStateFail,
       "drdlSliceStateFailVal": drdlSliceStateFailVal,
       "drdlSliceStateFailMom": drdlSliceStateFailMom,
       "drdlSliceStateFailMax": drdlSliceStateFailMax,
       "drdlLiteralSet": drdlLiteralSet,
       "drdlLiteralSetVal": drdlLiteralSetVal,
       "drdlLiteralSetMom": drdlLiteralSetMom,
       "drdlLiteralSetMax": drdlLiteralSetMax,
       "drdlPropertyFail": drdlPropertyFail,
       "drdlPropertyFailVal": drdlPropertyFailVal,
       "drdlPropertyFailMom": drdlPropertyFailMom,
       "drdlPropertyFailMax": drdlPropertyFailMax,
       "drdlChildIterateMax": drdlChildIterateMax,
       "drdlChildIterateMaxVal": drdlChildIterateMaxVal,
       "drdlChildIterateMaxMax": drdlChildIterateMaxMax,
       "drdlVsRangeTests": drdlVsRangeTests,
       "drdlVsRangeTestsVal": drdlVsRangeTestsVal,
       "drdlVsRangeTestsMom": drdlVsRangeTestsMom,
       "drdlVsRangeTestsMax": drdlVsRangeTestsMax,
       "drdlVsRangeSteps": drdlVsRangeSteps,
       "drdlVsRangeStepsVal": drdlVsRangeStepsVal,
       "drdlVsRangeStepsMom": drdlVsRangeStepsMom,
       "drdlVsRangeStepsMax": drdlVsRangeStepsMax,
       "drdlVsRegexTests": drdlVsRegexTests,
       "drdlVsRegexTestsVal": drdlVsRegexTestsVal,
       "drdlVsRegexTestsMom": drdlVsRegexTestsMom,
       "drdlVsRegexTestsMax": drdlVsRegexTestsMax,
       "drdlVsRegexSteps": drdlVsRegexSteps,
       "drdlVsRegexStepsVal": drdlVsRegexStepsVal,
       "drdlVsRegexStepsMom": drdlVsRegexStepsMom,
       "drdlVsRegexStepsMax": drdlVsRegexStepsMax,
       "drdlTaintFill": drdlTaintFill,
       "drdlTaintFillVal": drdlTaintFillVal,
       "drdlTaintFillMax": drdlTaintFillMax,
       "drdlTaintFillPercent": drdlTaintFillPercent,
       "drdlTaintFillPercentVal": drdlTaintFillPercentVal,
       "drdlTaintFillPercentMax": drdlTaintFillPercentMax,
       "ethernet": ethernet,
       "ethernetUnicast": ethernetUnicast,
       "ethernetUnicastVal": ethernetUnicastVal,
       "ethernetUnicastMom": ethernetUnicastMom,
       "ethernetUnicastMax": ethernetUnicastMax,
       "ethernetBroadcast": ethernetBroadcast,
       "ethernetBroadcastVal": ethernetBroadcastVal,
       "ethernetBroadcastMom": ethernetBroadcastMom,
       "ethernetBroadcastMax": ethernetBroadcastMax,
       "ethernetMulticast": ethernetMulticast,
       "ethernetMulticastVal": ethernetMulticastVal,
       "ethernetMulticastMom": ethernetMulticastMom,
       "ethernetMulticastMax": ethernetMulticastMax,
       "ethernet8021q": ethernet8021q,
       "ethernet8021qVal": ethernet8021qVal,
       "ethernet8021qMom": ethernet8021qMom,
       "ethernet8021qMax": ethernet8021qMax,
       "ethernetMpls": ethernetMpls,
       "ethernetMplsVal": ethernetMplsVal,
       "ethernetMplsMom": ethernetMplsMom,
       "ethernetMplsMax": ethernetMplsMax,
       "ethernetMplsOoh": ethernetMplsOoh,
       "ethernetMplsOohVal": ethernetMplsOohVal,
       "ethernetMplsOohMom": ethernetMplsOohMom,
       "ethernetMplsOohMax": ethernetMplsOohMax,
       "ethernetNonIp": ethernetNonIp,
       "ethernetNonIpVal": ethernetNonIpVal,
       "ethernetNonIpMom": ethernetNonIpMom,
       "ethernetNonIpMax": ethernetNonIpMax,
       "ethernetDivert": ethernetDivert,
       "ethernetDivertVal": ethernetDivertVal,
       "ethernetDivertMom": ethernetDivertMom,
       "ethernetDivertMax": ethernetDivertMax,
       "ethernetHBResetDrops": ethernetHBResetDrops,
       "ethernetHBResetDropsVal": ethernetHBResetDropsVal,
       "ethernetHBResetDropsMom": ethernetHBResetDropsMom,
       "ethernetHBResetDropsMax": ethernetHBResetDropsMax,
       "ethernetShuntEthertypePackets": ethernetShuntEthertypePackets,
       "ethernetShuntEthertypePacketsVal": ethernetShuntEthertypePacketsVal,
       "ethernetShuntEthertypePacketsMom": ethernetShuntEthertypePacketsMom,
       "ethernetShuntEthertypePacketsMax": ethernetShuntEthertypePacketsMax,
       "ethernetShuntEthertypeBytes": ethernetShuntEthertypeBytes,
       "ethernetShuntEthertypeBytesVal": ethernetShuntEthertypeBytesVal,
       "ethernetShuntEthertypeBytesMom": ethernetShuntEthertypeBytesMom,
       "ethernetShuntEthertypeBytesMax": ethernetShuntEthertypeBytesMax,
       "ethernetShuntMplsPackets": ethernetShuntMplsPackets,
       "ethernetShuntMplsPacketsVal": ethernetShuntMplsPacketsVal,
       "ethernetShuntMplsPacketsMom": ethernetShuntMplsPacketsMom,
       "ethernetShuntMplsPacketsMax": ethernetShuntMplsPacketsMax,
       "ethernetShuntMplsBytes": ethernetShuntMplsBytes,
       "ethernetShuntMplsBytesVal": ethernetShuntMplsBytesVal,
       "ethernetShuntMplsBytesMom": ethernetShuntMplsBytesMom,
       "ethernetShuntMplsBytesMax": ethernetShuntMplsBytesMax,
       "ethernetShuntEoMplsPackets": ethernetShuntEoMplsPackets,
       "ethernetShuntEoMplsPacketsVal": ethernetShuntEoMplsPacketsVal,
       "ethernetShuntEoMplsPacketsMom": ethernetShuntEoMplsPacketsMom,
       "ethernetShuntEoMplsPacketsMax": ethernetShuntEoMplsPacketsMax,
       "ethernetShuntEoMplsBytes": ethernetShuntEoMplsBytes,
       "ethernetShuntEoMplsBytesVal": ethernetShuntEoMplsBytesVal,
       "ethernetShuntEoMplsBytesMom": ethernetShuntEoMplsBytesMom,
       "ethernetShuntEoMplsBytesMax": ethernetShuntEoMplsBytesMax,
       "ethernetShuntDot1qPackets": ethernetShuntDot1qPackets,
       "ethernetShuntDot1qPacketsVal": ethernetShuntDot1qPacketsVal,
       "ethernetShuntDot1qPacketsMom": ethernetShuntDot1qPacketsMom,
       "ethernetShuntDot1qPacketsMax": ethernetShuntDot1qPacketsMax,
       "ethernetShuntDot1qBytes": ethernetShuntDot1qBytes,
       "ethernetShuntDot1qBytesVal": ethernetShuntDot1qBytesVal,
       "ethernetShuntDot1qBytesMom": ethernetShuntDot1qBytesMom,
       "ethernetShuntDot1qBytesMax": ethernetShuntDot1qBytesMax,
       "ethernetCountBytesIPv4IPv6": ethernetCountBytesIPv4IPv6,
       "ethernetCountBytesIPv4IPv6Val": ethernetCountBytesIPv4IPv6Val,
       "ethernetCountBytesIPv4IPv6Mom": ethernetCountBytesIPv4IPv6Mom,
       "ethernetCountBytesIPv4IPv6Max": ethernetCountBytesIPv4IPv6Max,
       "ipv4": ipv4,
       "ipv4Packets": ipv4Packets,
       "ipv4PacketsVal": ipv4PacketsVal,
       "ipv4PacketsMom": ipv4PacketsMom,
       "ipv4PacketsMax": ipv4PacketsMax,
       "ipv4Bytes": ipv4Bytes,
       "ipv4BytesVal": ipv4BytesVal,
       "ipv4BytesMom": ipv4BytesMom,
       "ipv4BytesMax": ipv4BytesMax,
       "ipv4RefusedShort": ipv4RefusedShort,
       "ipv4RefusedShortVal": ipv4RefusedShortVal,
       "ipv4RefusedShortMom": ipv4RefusedShortMom,
       "ipv4RefusedShortMax": ipv4RefusedShortMax,
       "ipv4RefusedVersion": ipv4RefusedVersion,
       "ipv4RefusedVersionVal": ipv4RefusedVersionVal,
       "ipv4RefusedVersionMom": ipv4RefusedVersionMom,
       "ipv4RefusedVersionMax": ipv4RefusedVersionMax,
       "ipv4RefusedSelf": ipv4RefusedSelf,
       "ipv4RefusedSelfVal": ipv4RefusedSelfVal,
       "ipv4RefusedSelfMom": ipv4RefusedSelfMom,
       "ipv4RefusedSelfMax": ipv4RefusedSelfMax,
       "ipv4Unfragmented": ipv4Unfragmented,
       "ipv4UnfragmentedVal": ipv4UnfragmentedVal,
       "ipv4UnfragmentedMom": ipv4UnfragmentedMom,
       "ipv4UnfragmentedMax": ipv4UnfragmentedMax,
       "ipv4Fragmented": ipv4Fragmented,
       "ipv4FragmentedVal": ipv4FragmentedVal,
       "ipv4FragmentedMom": ipv4FragmentedMom,
       "ipv4FragmentedMax": ipv4FragmentedMax,
       "ipv4FragmentedIds": ipv4FragmentedIds,
       "ipv4FragmentedIdsVal": ipv4FragmentedIdsVal,
       "ipv4FragmentedIdsMax": ipv4FragmentedIdsMax,
       "ipv4Fragments": ipv4Fragments,
       "ipv4FragmentsVal": ipv4FragmentsVal,
       "ipv4FragmentsMax": ipv4FragmentsMax,
       "ipv4RefusedOof": ipv4RefusedOof,
       "ipv4RefusedOofVal": ipv4RefusedOofVal,
       "ipv4RefusedOofMom": ipv4RefusedOofMom,
       "ipv4RefusedOofMax": ipv4RefusedOofMax,
       "ipv4FragmentAllocationFailures": ipv4FragmentAllocationFailures,
       "ipv4FragmentAllocationFailuresVal": ipv4FragmentAllocationFailuresVal,
       "ipv4FragmentAllocationFailuresMom": ipv4FragmentAllocationFailuresMom,
       "ipv4FragmentAllocationFailuresMax": ipv4FragmentAllocationFailuresMax,
       "ipv4FragmentReassFail": ipv4FragmentReassFail,
       "ipv4FragmentReassFailVal": ipv4FragmentReassFailVal,
       "ipv4FragmentReassFailMom": ipv4FragmentReassFailMom,
       "ipv4FragmentReassFailMax": ipv4FragmentReassFailMax,
       "ipv4RefusedFilter": ipv4RefusedFilter,
       "ipv4RefusedFilterVal": ipv4RefusedFilterVal,
       "ipv4RefusedFilterMom": ipv4RefusedFilterMom,
       "ipv4RefusedFilterMax": ipv4RefusedFilterMax,
       "ipv4FragmentTooNoisy": ipv4FragmentTooNoisy,
       "ipv4FragmentTooNoisyVal": ipv4FragmentTooNoisyVal,
       "ipv4FragmentTooNoisyMom": ipv4FragmentTooNoisyMom,
       "ipv4FragmentTooNoisyMax": ipv4FragmentTooNoisyMax,
       "ipv4Reassembled": ipv4Reassembled,
       "ipv4ReassembledVal": ipv4ReassembledVal,
       "ipv4ReassembledMom": ipv4ReassembledMom,
       "ipv4ReassembledMax": ipv4ReassembledMax,
       "ipv4FragmentDrops": ipv4FragmentDrops,
       "ipv4FragmentDropsVal": ipv4FragmentDropsVal,
       "ipv4FragmentDropsMom": ipv4FragmentDropsMom,
       "ipv4FragmentDropsMax": ipv4FragmentDropsMax,
       "ipv4ShuntAddressPackets": ipv4ShuntAddressPackets,
       "ipv4ShuntAddressPacketsVal": ipv4ShuntAddressPacketsVal,
       "ipv4ShuntAddressPacketsMom": ipv4ShuntAddressPacketsMom,
       "ipv4ShuntAddressPacketsMax": ipv4ShuntAddressPacketsMax,
       "ipv4ShuntAddressBytes": ipv4ShuntAddressBytes,
       "ipv4ShuntAddressBytesVal": ipv4ShuntAddressBytesVal,
       "ipv4ShuntAddressBytesMom": ipv4ShuntAddressBytesMom,
       "ipv4ShuntAddressBytesMax": ipv4ShuntAddressBytesMax,
       "ipv4ShuntProtoPackets": ipv4ShuntProtoPackets,
       "ipv4ShuntProtoPacketsVal": ipv4ShuntProtoPacketsVal,
       "ipv4ShuntProtoPacketsMom": ipv4ShuntProtoPacketsMom,
       "ipv4ShuntProtoPacketsMax": ipv4ShuntProtoPacketsMax,
       "ipv4ShuntProtoBytes": ipv4ShuntProtoBytes,
       "ipv4ShuntProtoBytesVal": ipv4ShuntProtoBytesVal,
       "ipv4ShuntProtoBytesMom": ipv4ShuntProtoBytesMom,
       "ipv4ShuntProtoBytesMax": ipv4ShuntProtoBytesMax,
       "ipv4EcnEct0": ipv4EcnEct0,
       "ipv4EcnEct0Val": ipv4EcnEct0Val,
       "ipv4EcnEct0Mom": ipv4EcnEct0Mom,
       "ipv4EcnEct0Max": ipv4EcnEct0Max,
       "ipv4EcnEct1": ipv4EcnEct1,
       "ipv4EcnEct1Val": ipv4EcnEct1Val,
       "ipv4EcnEct1Mom": ipv4EcnEct1Mom,
       "ipv4EcnEct1Max": ipv4EcnEct1Max,
       "ipv4EcnCn": ipv4EcnCn,
       "ipv4EcnCnVal": ipv4EcnCnVal,
       "ipv4EcnCnMom": ipv4EcnCnMom,
       "ipv4EcnCnMax": ipv4EcnCnMax,
       "tcpv4": tcpv4,
       "tcpv4Packets": tcpv4Packets,
       "tcpv4PacketsVal": tcpv4PacketsVal,
       "tcpv4PacketsMom": tcpv4PacketsMom,
       "tcpv4PacketsMax": tcpv4PacketsMax,
       "tcpv4Bytes": tcpv4Bytes,
       "tcpv4BytesVal": tcpv4BytesVal,
       "tcpv4BytesMom": tcpv4BytesMom,
       "tcpv4BytesMax": tcpv4BytesMax,
       "tcpv4CreateAttempts": tcpv4CreateAttempts,
       "tcpv4CreateAttemptsVal": tcpv4CreateAttemptsVal,
       "tcpv4CreateAttemptsMom": tcpv4CreateAttemptsMom,
       "tcpv4CreateAttemptsMax": tcpv4CreateAttemptsMax,
       "tcpv4Created": tcpv4Created,
       "tcpv4CreatedVal": tcpv4CreatedVal,
       "tcpv4CreatedMom": tcpv4CreatedMom,
       "tcpv4CreatedMax": tcpv4CreatedMax,
       "tcpv4RefusedRuleset": tcpv4RefusedRuleset,
       "tcpv4RefusedRulesetVal": tcpv4RefusedRulesetVal,
       "tcpv4RefusedRulesetMom": tcpv4RefusedRulesetMom,
       "tcpv4RefusedRulesetMax": tcpv4RefusedRulesetMax,
       "tcpv4RefusedShort": tcpv4RefusedShort,
       "tcpv4RefusedShortVal": tcpv4RefusedShortVal,
       "tcpv4RefusedShortMom": tcpv4RefusedShortMom,
       "tcpv4RefusedShortMax": tcpv4RefusedShortMax,
       "tcpv4RefusedBroadcast": tcpv4RefusedBroadcast,
       "tcpv4RefusedBroadcastVal": tcpv4RefusedBroadcastVal,
       "tcpv4RefusedBroadcastMom": tcpv4RefusedBroadcastMom,
       "tcpv4RefusedBroadcastMax": tcpv4RefusedBroadcastMax,
       "tcpv4RefusedOffset": tcpv4RefusedOffset,
       "tcpv4RefusedOffsetVal": tcpv4RefusedOffsetVal,
       "tcpv4RefusedOffsetMom": tcpv4RefusedOffsetMom,
       "tcpv4RefusedOffsetMax": tcpv4RefusedOffsetMax,
       "tcpv4Rejected": tcpv4Rejected,
       "tcpv4RejectedVal": tcpv4RejectedVal,
       "tcpv4RejectedMom": tcpv4RejectedMom,
       "tcpv4RejectedMax": tcpv4RejectedMax,
       "tcpv4Lostsync": tcpv4Lostsync,
       "tcpv4LostsyncVal": tcpv4LostsyncVal,
       "tcpv4LostsyncMax": tcpv4LostsyncMax,
       "tcpv4UntrackedPackets": tcpv4UntrackedPackets,
       "tcpv4UntrackedPacketsVal": tcpv4UntrackedPacketsVal,
       "tcpv4UntrackedPacketsMom": tcpv4UntrackedPacketsMom,
       "tcpv4UntrackedPacketsMax": tcpv4UntrackedPacketsMax,
       "tcpv4GoodputPackets": tcpv4GoodputPackets,
       "tcpv4GoodputPacketsVal": tcpv4GoodputPacketsVal,
       "tcpv4GoodputPacketsMom": tcpv4GoodputPacketsMom,
       "tcpv4GoodputPacketsMax": tcpv4GoodputPacketsMax,
       "tcpv4GoodputBytes": tcpv4GoodputBytes,
       "tcpv4GoodputBytesVal": tcpv4GoodputBytesVal,
       "tcpv4GoodputBytesMom": tcpv4GoodputBytesMom,
       "tcpv4GoodputBytesMax": tcpv4GoodputBytesMax,
       "tcpv4Segments": tcpv4Segments,
       "tcpv4SegmentsVal": tcpv4SegmentsVal,
       "tcpv4SegmentsMax": tcpv4SegmentsMax,
       "tcpv4SegmentsPayload": tcpv4SegmentsPayload,
       "tcpv4SegmentsPayloadVal": tcpv4SegmentsPayloadVal,
       "tcpv4SegmentsPayloadMax": tcpv4SegmentsPayloadMax,
       "tcpv4SegmentsDropped": tcpv4SegmentsDropped,
       "tcpv4SegmentsDroppedVal": tcpv4SegmentsDroppedVal,
       "tcpv4SegmentsDroppedMom": tcpv4SegmentsDroppedMom,
       "tcpv4SegmentsDroppedMax": tcpv4SegmentsDroppedMax,
       "tcpv4PacketAllocFail": tcpv4PacketAllocFail,
       "tcpv4PacketAllocFailVal": tcpv4PacketAllocFailVal,
       "tcpv4PacketAllocFailMom": tcpv4PacketAllocFailMom,
       "tcpv4PacketAllocFailMax": tcpv4PacketAllocFailMax,
       "tcpv4UntrackedGoodput": tcpv4UntrackedGoodput,
       "tcpv4UntrackedGoodputVal": tcpv4UntrackedGoodputVal,
       "tcpv4UntrackedGoodputMom": tcpv4UntrackedGoodputMom,
       "tcpv4UntrackedGoodputMax": tcpv4UntrackedGoodputMax,
       "tcpv4UntrackedBytes": tcpv4UntrackedBytes,
       "tcpv4UntrackedBytesVal": tcpv4UntrackedBytesVal,
       "tcpv4UntrackedBytesMom": tcpv4UntrackedBytesMom,
       "tcpv4UntrackedBytesMax": tcpv4UntrackedBytesMax,
       "tcpv4CorruptOptions": tcpv4CorruptOptions,
       "tcpv4CorruptOptionsVal": tcpv4CorruptOptionsVal,
       "tcpv4CorruptOptionsMom": tcpv4CorruptOptionsMom,
       "tcpv4CorruptOptionsMax": tcpv4CorruptOptionsMax,
       "tcpv4CorruptConn": tcpv4CorruptConn,
       "tcpv4CorruptConnVal": tcpv4CorruptConnVal,
       "tcpv4CorruptConnMom": tcpv4CorruptConnMom,
       "tcpv4CorruptConnMax": tcpv4CorruptConnMax,
       "tcpv4SegmentedConnections": tcpv4SegmentedConnections,
       "tcpv4SegmentedConnectionsVal": tcpv4SegmentedConnectionsVal,
       "tcpv4SegmentedConnectionsMax": tcpv4SegmentedConnectionsMax,
       "tcpv4OutOfWindowPackets": tcpv4OutOfWindowPackets,
       "tcpv4OutOfWindowPacketsVal": tcpv4OutOfWindowPacketsVal,
       "tcpv4OutOfWindowPacketsMom": tcpv4OutOfWindowPacketsMom,
       "tcpv4OutOfWindowPacketsMax": tcpv4OutOfWindowPacketsMax,
       "tcpv4RefusedFilter": tcpv4RefusedFilter,
       "tcpv4RefusedFilterVal": tcpv4RefusedFilterVal,
       "tcpv4RefusedFilterMom": tcpv4RefusedFilterMom,
       "tcpv4RefusedFilterMax": tcpv4RefusedFilterMax,
       "tcpv4SynExisting": tcpv4SynExisting,
       "tcpv4SynExistingVal": tcpv4SynExistingVal,
       "tcpv4SynExistingMom": tcpv4SynExistingMom,
       "tcpv4SynExistingMax": tcpv4SynExistingMax,
       "tcpv4SegmentAllocFail": tcpv4SegmentAllocFail,
       "tcpv4SegmentAllocFailVal": tcpv4SegmentAllocFailVal,
       "tcpv4SegmentAllocFailMom": tcpv4SegmentAllocFailMom,
       "tcpv4SegmentAllocFailMax": tcpv4SegmentAllocFailMax,
       "tcpv4EnqueuedSegments": tcpv4EnqueuedSegments,
       "tcpv4EnqueuedSegmentsVal": tcpv4EnqueuedSegmentsVal,
       "tcpv4EnqueuedSegmentsMom": tcpv4EnqueuedSegmentsMom,
       "tcpv4EnqueuedSegmentsMax": tcpv4EnqueuedSegmentsMax,
       "tcpv4DequeuedSegments": tcpv4DequeuedSegments,
       "tcpv4DequeuedSegmentsVal": tcpv4DequeuedSegmentsVal,
       "tcpv4DequeuedSegmentsMom": tcpv4DequeuedSegmentsMom,
       "tcpv4DequeuedSegmentsMax": tcpv4DequeuedSegmentsMax,
       "tcpv4DiscardedSegments": tcpv4DiscardedSegments,
       "tcpv4DiscardedSegmentsVal": tcpv4DiscardedSegmentsVal,
       "tcpv4DiscardedSegmentsMom": tcpv4DiscardedSegmentsMom,
       "tcpv4DiscardedSegmentsMax": tcpv4DiscardedSegmentsMax,
       "tcpv4EmptyPackets": tcpv4EmptyPackets,
       "tcpv4EmptyPacketsVal": tcpv4EmptyPacketsVal,
       "tcpv4EmptyPacketsMom": tcpv4EmptyPacketsMom,
       "tcpv4EmptyPacketsMax": tcpv4EmptyPacketsMax,
       "tcpv4OosPackets": tcpv4OosPackets,
       "tcpv4OosPacketsVal": tcpv4OosPacketsVal,
       "tcpv4OosPacketsMom": tcpv4OosPacketsMom,
       "tcpv4OosPacketsMax": tcpv4OosPacketsMax,
       "tcpv4OosBytes": tcpv4OosBytes,
       "tcpv4OosBytesVal": tcpv4OosBytesVal,
       "tcpv4OosBytesMom": tcpv4OosBytesMom,
       "tcpv4OosBytesMax": tcpv4OosBytesMax,
       "tcpv4Retransmits": tcpv4Retransmits,
       "tcpv4RetransmitsVal": tcpv4RetransmitsVal,
       "tcpv4RetransmitsMom": tcpv4RetransmitsMom,
       "tcpv4RetransmitsMax": tcpv4RetransmitsMax,
       "tcpv4Cwr": tcpv4Cwr,
       "tcpv4CwrVal": tcpv4CwrVal,
       "tcpv4CwrMom": tcpv4CwrMom,
       "tcpv4CwrMax": tcpv4CwrMax,
       "tcpv4Ecne": tcpv4Ecne,
       "tcpv4EcneVal": tcpv4EcneVal,
       "tcpv4EcneMom": tcpv4EcneMom,
       "tcpv4EcneMax": tcpv4EcneMax,
       "tcpv4SimOpen": tcpv4SimOpen,
       "tcpv4SimOpenVal": tcpv4SimOpenVal,
       "tcpv4SimOpenMom": tcpv4SimOpenMom,
       "tcpv4SimOpenMax": tcpv4SimOpenMax,
       "connection": connection,
       "connectionCount": connectionCount,
       "connectionCountVal": connectionCountVal,
       "connectionCountMax": connectionCountMax,
       "connectionEstCount": connectionEstCount,
       "connectionEstCountVal": connectionEstCountVal,
       "connectionEstCountMax": connectionEstCountMax,
       "connectionCreateAttemptsInbound": connectionCreateAttemptsInbound,
       "connectionCreateAttemptsInboundVal": connectionCreateAttemptsInboundVal,
       "connectionCreateAttemptsInboundMom": connectionCreateAttemptsInboundMom,
       "connectionCreateAttemptsInboundMax": connectionCreateAttemptsInboundMax,
       "connectionCreateAttemptsOutbound": connectionCreateAttemptsOutbound,
       "connectionCreateAttemptsOutboundVal": connectionCreateAttemptsOutboundVal,
       "connectionCreateAttemptsOutboundMom": connectionCreateAttemptsOutboundMom,
       "connectionCreateAttemptsOutboundMax": connectionCreateAttemptsOutboundMax,
       "connectionRefusedProt": connectionRefusedProt,
       "connectionRefusedProtVal": connectionRefusedProtVal,
       "connectionRefusedProtMom": connectionRefusedProtMom,
       "connectionRefusedProtMax": connectionRefusedProtMax,
       "connectionRefusedFull": connectionRefusedFull,
       "connectionRefusedFullVal": connectionRefusedFullVal,
       "connectionRefusedFullMom": connectionRefusedFullMom,
       "connectionRefusedFullMax": connectionRefusedFullMax,
       "connectionCreatedInbound": connectionCreatedInbound,
       "connectionCreatedInboundVal": connectionCreatedInboundVal,
       "connectionCreatedInboundMom": connectionCreatedInboundMom,
       "connectionCreatedInboundMax": connectionCreatedInboundMax,
       "connectionCreatedOutbound": connectionCreatedOutbound,
       "connectionCreatedOutboundVal": connectionCreatedOutboundVal,
       "connectionCreatedOutboundMom": connectionCreatedOutboundMom,
       "connectionCreatedOutboundMax": connectionCreatedOutboundMax,
       "connectionLruAllocs": connectionLruAllocs,
       "connectionLruAllocsVal": connectionLruAllocsVal,
       "connectionLruAllocsMom": connectionLruAllocsMom,
       "connectionLruAllocsMax": connectionLruAllocsMax,
       "connectionLookups": connectionLookups,
       "connectionLookupsVal": connectionLookupsVal,
       "connectionLookupsMom": connectionLookupsMom,
       "connectionLookupsMax": connectionLookupsMax,
       "connectionEstablished": connectionEstablished,
       "connectionEstablishedVal": connectionEstablishedVal,
       "connectionEstablishedMom": connectionEstablishedMom,
       "connectionEstablishedMax": connectionEstablishedMax,
       "connectionUpdates": connectionUpdates,
       "connectionUpdatesVal": connectionUpdatesVal,
       "connectionUpdatesMom": connectionUpdatesMom,
       "connectionUpdatesMax": connectionUpdatesMax,
       "connectionTtlTimeouts": connectionTtlTimeouts,
       "connectionTtlTimeoutsVal": connectionTtlTimeoutsVal,
       "connectionTtlTimeoutsMom": connectionTtlTimeoutsMom,
       "connectionTtlTimeoutsMax": connectionTtlTimeoutsMax,
       "connectionProtEnables": connectionProtEnables,
       "connectionProtEnablesVal": connectionProtEnablesVal,
       "connectionProtEnablesMom": connectionProtEnablesMom,
       "connectionProtEnablesMax": connectionProtEnablesMax,
       "connectionNotFound": connectionNotFound,
       "connectionNotFoundVal": connectionNotFoundVal,
       "connectionNotFoundMom": connectionNotFoundMom,
       "connectionNotFoundMax": connectionNotFoundMax,
       "connectionRefusedExisting": connectionRefusedExisting,
       "connectionRefusedExistingVal": connectionRefusedExistingVal,
       "connectionRefusedExistingMom": connectionRefusedExistingMom,
       "connectionRefusedExistingMax": connectionRefusedExistingMax,
       "connectionRefusedRuleset": connectionRefusedRuleset,
       "connectionRefusedRulesetVal": connectionRefusedRulesetVal,
       "connectionRefusedRulesetMom": connectionRefusedRulesetMom,
       "connectionRefusedRulesetMax": connectionRefusedRulesetMax,
       "connectionRedirected": connectionRedirected,
       "connectionRedirectedVal": connectionRedirectedVal,
       "connectionRedirectedMax": connectionRedirectedMax,
       "connectionRedirectCollisions": connectionRedirectCollisions,
       "connectionRedirectCollisionsVal": connectionRedirectCollisionsVal,
       "connectionRedirectCollisionsMax": connectionRedirectCollisionsMax,
       "connectionUnestablished": connectionUnestablished,
       "connectionUnestablishedVal": connectionUnestablishedVal,
       "connectionUnestablishedMom": connectionUnestablishedMom,
       "connectionUnestablishedMax": connectionUnestablishedMax,
       "connectionDestroyedEst": connectionDestroyedEst,
       "connectionDestroyedEstVal": connectionDestroyedEstVal,
       "connectionDestroyedEstMax": connectionDestroyedEstMax,
       "connectionInvalidRulesetUpdate": connectionInvalidRulesetUpdate,
       "connectionInvalidRulesetUpdateVal": connectionInvalidRulesetUpdateVal,
       "connectionInvalidRulesetUpdateMom": connectionInvalidRulesetUpdateMom,
       "connectionInvalidRulesetUpdateMax": connectionInvalidRulesetUpdateMax,
       "connectionOrphaned": connectionOrphaned,
       "connectionOrphanedVal": connectionOrphanedVal,
       "connectionOrphanedMax": connectionOrphanedMax,
       "connectionFailureShuntPackets": connectionFailureShuntPackets,
       "connectionFailureShuntPacketsVal": connectionFailureShuntPacketsVal,
       "connectionFailureShuntPacketsMom": connectionFailureShuntPacketsMom,
       "connectionFailureShuntPacketsMax": connectionFailureShuntPacketsMax,
       "connectionFailureShuntBytes": connectionFailureShuntBytes,
       "connectionFailureShuntBytesVal": connectionFailureShuntBytesVal,
       "connectionFailureShuntBytesMom": connectionFailureShuntBytesMom,
       "connectionFailureShuntBytesMax": connectionFailureShuntBytesMax,
       "connsync": connsync,
       "connsyncSeenSnt": connsyncSeenSnt,
       "connsyncSeenSntVal": connsyncSeenSntVal,
       "connsyncSeenSntMom": connsyncSeenSntMom,
       "connsyncSeenSntMax": connsyncSeenSntMax,
       "connsyncSeenRcv": connsyncSeenRcv,
       "connsyncSeenRcvVal": connsyncSeenRcvVal,
       "connsyncSeenRcvMom": connsyncSeenRcvMom,
       "connsyncSeenRcvMax": connsyncSeenRcvMax,
       "connsyncUpdateSnt": connsyncUpdateSnt,
       "connsyncUpdateSntVal": connsyncUpdateSntVal,
       "connsyncUpdateSntMom": connsyncUpdateSntMom,
       "connsyncUpdateSntMax": connsyncUpdateSntMax,
       "connsyncSeenackRcv": connsyncSeenackRcv,
       "connsyncSeenackRcvVal": connsyncSeenackRcvVal,
       "connsyncSeenackRcvMom": connsyncSeenackRcvMom,
       "connsyncSeenackRcvMax": connsyncSeenackRcvMax,
       "connsyncUpdateRcv": connsyncUpdateRcv,
       "connsyncUpdateRcvVal": connsyncUpdateRcvVal,
       "connsyncUpdateRcvMom": connsyncUpdateRcvMom,
       "connsyncUpdateRcvMax": connsyncUpdateRcvMax,
       "connsyncUnknownUpdateRcv": connsyncUnknownUpdateRcv,
       "connsyncUnknownUpdateRcvVal": connsyncUnknownUpdateRcvVal,
       "connsyncUnknownUpdateRcvMom": connsyncUnknownUpdateRcvMom,
       "connsyncUnknownUpdateRcvMax": connsyncUnknownUpdateRcvMax,
       "connsyncOutofsync": connsyncOutofsync,
       "connsyncOutofsyncVal": connsyncOutofsyncVal,
       "connsyncOutofsyncMom": connsyncOutofsyncMom,
       "connsyncOutofsyncMax": connsyncOutofsyncMax,
       "connsyncSynced": connsyncSynced,
       "connsyncSyncedVal": connsyncSyncedVal,
       "connsyncSyncedMax": connsyncSyncedMax,
       "connsyncDoubleSeen": connsyncDoubleSeen,
       "connsyncDoubleSeenVal": connsyncDoubleSeenVal,
       "connsyncDoubleSeenMom": connsyncDoubleSeenMom,
       "connsyncDoubleSeenMax": connsyncDoubleSeenMax,
       "connsyncHelloRcv": connsyncHelloRcv,
       "connsyncHelloRcvVal": connsyncHelloRcvVal,
       "connsyncHelloRcvMom": connsyncHelloRcvMom,
       "connsyncHelloRcvMax": connsyncHelloRcvMax,
       "connsyncOutofsyncMissedRcv": connsyncOutofsyncMissedRcv,
       "connsyncOutofsyncMissedRcvVal": connsyncOutofsyncMissedRcvVal,
       "connsyncOutofsyncMissedRcvMom": connsyncOutofsyncMissedRcvMom,
       "connsyncOutofsyncMissedRcvMax": connsyncOutofsyncMissedRcvMax,
       "connsyncOutofsyncCollision": connsyncOutofsyncCollision,
       "connsyncOutofsyncCollisionVal": connsyncOutofsyncCollisionVal,
       "connsyncOutofsyncCollisionMom": connsyncOutofsyncCollisionMom,
       "connsyncOutofsyncCollisionMax": connsyncOutofsyncCollisionMax,
       "connsyncBadAdler": connsyncBadAdler,
       "connsyncBadAdlerVal": connsyncBadAdlerVal,
       "connsyncBadAdlerMom": connsyncBadAdlerMom,
       "connsyncBadAdlerMax": connsyncBadAdlerMax,
       "connsyncPktOverflow": connsyncPktOverflow,
       "connsyncPktOverflowVal": connsyncPktOverflowVal,
       "connsyncPktOverflowMom": connsyncPktOverflowMom,
       "connsyncPktOverflowMax": connsyncPktOverflowMax,
       "connsyncCorruptPkt": connsyncCorruptPkt,
       "connsyncCorruptPktVal": connsyncCorruptPktVal,
       "connsyncCorruptPktMom": connsyncCorruptPktMom,
       "connsyncCorruptPktMax": connsyncCorruptPktMax,
       "connsyncConnNotfound": connsyncConnNotfound,
       "connsyncConnNotfoundVal": connsyncConnNotfoundVal,
       "connsyncConnNotfoundMom": connsyncConnNotfoundMom,
       "connsyncConnNotfoundMax": connsyncConnNotfoundMax,
       "connsyncBadVer": connsyncBadVer,
       "connsyncBadVerVal": connsyncBadVerVal,
       "connsyncBadVerMom": connsyncBadVerMom,
       "connsyncBadVerMax": connsyncBadVerMax,
       "connsyncBadType": connsyncBadType,
       "connsyncBadTypeVal": connsyncBadTypeVal,
       "connsyncBadTypeMom": connsyncBadTypeMom,
       "connsyncBadTypeMax": connsyncBadTypeMax,
       "connsyncBadEngineid": connsyncBadEngineid,
       "connsyncBadEngineidVal": connsyncBadEngineidVal,
       "connsyncBadEngineidMom": connsyncBadEngineidMom,
       "connsyncBadEngineidMax": connsyncBadEngineidMax,
       "connsyncUdpSnt": connsyncUdpSnt,
       "connsyncUdpSntVal": connsyncUdpSntVal,
       "connsyncUdpSntMom": connsyncUdpSntMom,
       "connsyncUdpSntMax": connsyncUdpSntMax,
       "connsyncUdpRcv": connsyncUdpRcv,
       "connsyncUdpRcvVal": connsyncUdpRcvVal,
       "connsyncUdpRcvMom": connsyncUdpRcvMom,
       "connsyncUdpRcvMax": connsyncUdpRcvMax,
       "ruleset": ruleset,
       "rulesetReceived": rulesetReceived,
       "rulesetReceivedVal": rulesetReceivedVal,
       "rulesetReceivedMom": rulesetReceivedMom,
       "rulesetReceivedMax": rulesetReceivedMax,
       "rulesetFwrules": rulesetFwrules,
       "rulesetFwrulesVal": rulesetFwrulesVal,
       "rulesetFwrulesMax": rulesetFwrulesMax,
       "rulesetShapingrules": rulesetShapingrules,
       "rulesetShapingrulesVal": rulesetShapingrulesVal,
       "rulesetShapingrulesMax": rulesetShapingrulesMax,
       "rulesetClienttreeSize": rulesetClienttreeSize,
       "rulesetClienttreeSizeVal": rulesetClienttreeSizeVal,
       "rulesetClienttreeSizeMax": rulesetClienttreeSizeMax,
       "rulesetServertreeSize": rulesetServertreeSize,
       "rulesetServertreeSizeVal": rulesetServertreeSizeVal,
       "rulesetServertreeSizeMax": rulesetServertreeSizeMax,
       "rulesetBgpNumpaths": rulesetBgpNumpaths,
       "rulesetBgpNumpathsVal": rulesetBgpNumpathsVal,
       "rulesetBgpNumpathsMax": rulesetBgpNumpathsMax,
       "rulesetBgpTreesize": rulesetBgpTreesize,
       "rulesetBgpTreesizeVal": rulesetBgpTreesizeVal,
       "rulesetBgpTreesizeMax": rulesetBgpTreesizeMax,
       "rulesetBgpNumLookup": rulesetBgpNumLookup,
       "rulesetBgpNumLookupVal": rulesetBgpNumLookupVal,
       "rulesetBgpNumLookupMom": rulesetBgpNumLookupMom,
       "rulesetBgpNumLookupMax": rulesetBgpNumLookupMax,
       "rulesetPropChecks": rulesetPropChecks,
       "rulesetPropChecksVal": rulesetPropChecksVal,
       "rulesetPropChecksMom": rulesetPropChecksMom,
       "rulesetPropChecksMax": rulesetPropChecksMax,
       "rulesetBitmasksAvg": rulesetBitmasksAvg,
       "rulesetBitmasksAvgVal": rulesetBitmasksAvgVal,
       "rulesetBitmasksAvgMax": rulesetBitmasksAvgMax,
       "rulesetBitmasksMax": rulesetBitmasksMax,
       "rulesetBitmasksMaxVal": rulesetBitmasksMaxVal,
       "rulesetBitmasksMaxMax": rulesetBitmasksMaxMax,
       "rulesetDynipAdd": rulesetDynipAdd,
       "rulesetDynipAddVal": rulesetDynipAddVal,
       "rulesetDynipAddMom": rulesetDynipAddMom,
       "rulesetDynipAddMax": rulesetDynipAddMax,
       "rulesetDynipRemove": rulesetDynipRemove,
       "rulesetDynipRemoveVal": rulesetDynipRemoveVal,
       "rulesetDynipRemoveMom": rulesetDynipRemoveMom,
       "rulesetDynipRemoveMax": rulesetDynipRemoveMax,
       "rulesetLastUpdate": rulesetLastUpdate,
       "rulesetLastUpdateVal": rulesetLastUpdateVal,
       "rulesetDynipNum": rulesetDynipNum,
       "rulesetDynipNumVal": rulesetDynipNumVal,
       "rulesetDynipNumMax": rulesetDynipNumMax,
       "rulesetStatisticsrules": rulesetStatisticsrules,
       "rulesetStatisticsrulesVal": rulesetStatisticsrulesVal,
       "rulesetStatisticsrulesMax": rulesetStatisticsrulesMax,
       "rulesetLocaltreeSize": rulesetLocaltreeSize,
       "rulesetLocaltreeSizeVal": rulesetLocaltreeSizeVal,
       "rulesetLocaltreeSizeMax": rulesetLocaltreeSizeMax,
       "rulesetStatisticsRuleOverflow": rulesetStatisticsRuleOverflow,
       "rulesetStatisticsRuleOverflowVal": rulesetStatisticsRuleOverflowVal,
       "rulesetStatisticsRuleOverflowMom": rulesetStatisticsRuleOverflowMom,
       "rulesetStatisticsRuleOverflowMax": rulesetStatisticsRuleOverflowMax,
       "rulesetConnStatechange": rulesetConnStatechange,
       "rulesetConnStatechangeVal": rulesetConnStatechangeVal,
       "rulesetConnStatechangeMom": rulesetConnStatechangeMom,
       "rulesetConnStatechangeMax": rulesetConnStatechangeMax,
       "rulesetConnStatechangeProp": rulesetConnStatechangeProp,
       "rulesetConnStatechangePropVal": rulesetConnStatechangePropVal,
       "rulesetConnStatechangePropMom": rulesetConnStatechangePropMom,
       "rulesetConnStatechangePropMax": rulesetConnStatechangePropMax,
       "rulesetConnStatechangeService": rulesetConnStatechangeService,
       "rulesetConnStatechangeServiceVal": rulesetConnStatechangeServiceVal,
       "rulesetConnStatechangeServiceMom": rulesetConnStatechangeServiceMom,
       "rulesetConnStatechangeServiceMax": rulesetConnStatechangeServiceMax,
       "rulesetConnStatechangeFlags": rulesetConnStatechangeFlags,
       "rulesetConnStatechangeFlagsVal": rulesetConnStatechangeFlagsVal,
       "rulesetConnStatechangeFlagsMom": rulesetConnStatechangeFlagsMom,
       "rulesetConnStatechangeFlagsMax": rulesetConnStatechangeFlagsMax,
       "rulesetConnStatechangeAspath": rulesetConnStatechangeAspath,
       "rulesetConnStatechangeAspathVal": rulesetConnStatechangeAspathVal,
       "rulesetConnStatechangeAspathMom": rulesetConnStatechangeAspathMom,
       "rulesetConnStatechangeAspathMax": rulesetConnStatechangeAspathMax,
       "rulesetRecalcVersion": rulesetRecalcVersion,
       "rulesetRecalcVersionVal": rulesetRecalcVersionVal,
       "rulesetRecalcVersionMom": rulesetRecalcVersionMom,
       "rulesetRecalcVersionMax": rulesetRecalcVersionMax,
       "rulesetRecalcTime": rulesetRecalcTime,
       "rulesetRecalcTimeVal": rulesetRecalcTimeVal,
       "rulesetRecalcTimeMom": rulesetRecalcTimeMom,
       "rulesetRecalcTimeMax": rulesetRecalcTimeMax,
       "rulesetRecalcBgp": rulesetRecalcBgp,
       "rulesetRecalcBgpVal": rulesetRecalcBgpVal,
       "rulesetRecalcBgpMom": rulesetRecalcBgpMom,
       "rulesetRecalcBgpMax": rulesetRecalcBgpMax,
       "rulesetRecalcUnknown": rulesetRecalcUnknown,
       "rulesetRecalcUnknownVal": rulesetRecalcUnknownVal,
       "rulesetRecalcUnknownMom": rulesetRecalcUnknownMom,
       "rulesetRecalcUnknownMax": rulesetRecalcUnknownMax,
       "rulesetOutdatedService": rulesetOutdatedService,
       "rulesetOutdatedServiceVal": rulesetOutdatedServiceVal,
       "rulesetOutdatedServiceMom": rulesetOutdatedServiceMom,
       "rulesetOutdatedServiceMax": rulesetOutdatedServiceMax,
       "rulesetSubscribers": rulesetSubscribers,
       "rulesetSubscribersVal": rulesetSubscribersVal,
       "rulesetSubscribersMax": rulesetSubscribersMax,
       "rulesetBadAspath": rulesetBadAspath,
       "rulesetBadAspathVal": rulesetBadAspathVal,
       "rulesetBadAspathMom": rulesetBadAspathMom,
       "rulesetBadAspathMax": rulesetBadAspathMax,
       "rulesetConnStatechangeLinklevel": rulesetConnStatechangeLinklevel,
       "rulesetConnStatechangeLinklevelVal": rulesetConnStatechangeLinklevelVal,
       "rulesetConnStatechangeLinklevelMom": rulesetConnStatechangeLinklevelMom,
       "rulesetConnStatechangeLinklevelMax": rulesetConnStatechangeLinklevelMax,
       "rulesetSubscriberAllocFail": rulesetSubscriberAllocFail,
       "rulesetSubscriberAllocFailVal": rulesetSubscriberAllocFailVal,
       "rulesetSubscriberAllocFailMom": rulesetSubscriberAllocFailMom,
       "rulesetSubscriberAllocFailMax": rulesetSubscriberAllocFailMax,
       "rulesetDynipAllocFail": rulesetDynipAllocFail,
       "rulesetDynipAllocFailVal": rulesetDynipAllocFailVal,
       "rulesetDynipAllocFailMom": rulesetDynipAllocFailMom,
       "rulesetDynipAllocFailMax": rulesetDynipAllocFailMax,
       "rulesetDynipOversized": rulesetDynipOversized,
       "rulesetDynipOversizedVal": rulesetDynipOversizedVal,
       "rulesetDynipOversizedMom": rulesetDynipOversizedMom,
       "rulesetDynipOversizedMax": rulesetDynipOversizedMax,
       "rulesetNonexistentSubscriber": rulesetNonexistentSubscriber,
       "rulesetNonexistentSubscriberVal": rulesetNonexistentSubscriberVal,
       "rulesetNonexistentSubscriberMom": rulesetNonexistentSubscriberMom,
       "rulesetNonexistentSubscriberMax": rulesetNonexistentSubscriberMax,
       "rulesetConnStatechangeTtl": rulesetConnStatechangeTtl,
       "rulesetConnStatechangeTtlVal": rulesetConnStatechangeTtlVal,
       "rulesetConnStatechangeTtlMom": rulesetConnStatechangeTtlMom,
       "rulesetConnStatechangeTtlMax": rulesetConnStatechangeTtlMax,
       "firewall": firewall,
       "fwAccepts": fwAccepts,
       "fwAcceptsVal": fwAcceptsVal,
       "fwAcceptsMom": fwAcceptsMom,
       "fwAcceptsMax": fwAcceptsMax,
       "fwRejects": fwRejects,
       "fwRejectsVal": fwRejectsVal,
       "fwRejectsMom": fwRejectsMom,
       "fwRejectsMax": fwRejectsMax,
       "fwDrops": fwDrops,
       "fwDropsVal": fwDropsVal,
       "fwDropsMom": fwDropsMom,
       "fwDropsMax": fwDropsMax,
       "fwRewites": fwRewites,
       "fwRewitesVal": fwRewitesVal,
       "fwRewitesMom": fwRewitesMom,
       "fwRewitesMax": fwRewitesMax,
       "fwDiverts": fwDiverts,
       "fwDivertsVal": fwDivertsVal,
       "fwDivertsMom": fwDivertsMom,
       "fwDivertsMax": fwDivertsMax,
       "fwRuleSets": fwRuleSets,
       "fwRuleSetsVal": fwRuleSetsVal,
       "fwRuleSetsMom": fwRuleSetsMom,
       "fwRuleSetsMax": fwRuleSetsMax,
       "fwLogs": fwLogs,
       "fwLogsVal": fwLogsVal,
       "fwLogsMom": fwLogsMom,
       "fwLogsMax": fwLogsMax,
       "fwMonitor": fwMonitor,
       "fwMonitorVal": fwMonitorVal,
       "fwMonitorMom": fwMonitorMom,
       "fwMonitorMax": fwMonitorMax,
       "fwMonitorFailures": fwMonitorFailures,
       "fwMonitorFailuresVal": fwMonitorFailuresVal,
       "fwMonitorFailuresMom": fwMonitorFailuresMom,
       "fwMonitorFailuresMax": fwMonitorFailuresMax,
       "fwInjects": fwInjects,
       "fwInjectsVal": fwInjectsVal,
       "fwInjectsMom": fwInjectsMom,
       "fwInjectsMax": fwInjectsMax,
       "fwInjectsFailures": fwInjectsFailures,
       "fwInjectsFailuresVal": fwInjectsFailuresVal,
       "fwInjectsFailuresMom": fwInjectsFailuresMom,
       "fwInjectsFailuresMax": fwInjectsFailuresMax,
       "fwInjectsFailuresProp": fwInjectsFailuresProp,
       "fwInjectsFailuresPropVal": fwInjectsFailuresPropVal,
       "fwInjectsFailuresPropMom": fwInjectsFailuresPropMom,
       "fwInjectsFailuresPropMax": fwInjectsFailuresPropMax,
       "fwMidconnRewrite": fwMidconnRewrite,
       "fwMidconnRewriteVal": fwMidconnRewriteVal,
       "fwMidconnRewriteMom": fwMidconnRewriteMom,
       "fwMidconnRewriteMax": fwMidconnRewriteMax,
       "shaping": shaping,
       "shapingEnqueued": shapingEnqueued,
       "shapingEnqueuedVal": shapingEnqueuedVal,
       "shapingEnqueuedMom": shapingEnqueuedMom,
       "shapingEnqueuedMax": shapingEnqueuedMax,
       "shapingDequeued": shapingDequeued,
       "shapingDequeuedVal": shapingDequeuedVal,
       "shapingDequeuedMom": shapingDequeuedMom,
       "shapingDequeuedMax": shapingDequeuedMax,
       "shapingBrownConnDrops": shapingBrownConnDrops,
       "shapingBrownConnDropsVal": shapingBrownConnDropsVal,
       "shapingBrownConnDropsMom": shapingBrownConnDropsMom,
       "shapingBrownConnDropsMax": shapingBrownConnDropsMax,
       "shapingQueueSize": shapingQueueSize,
       "shapingQueueSizeVal": shapingQueueSizeVal,
       "shapingQueueSizeMax": shapingQueueSizeMax,
       "shapingRulesSetCount": shapingRulesSetCount,
       "shapingRulesSetCountVal": shapingRulesSetCountVal,
       "shapingRulesSetCountMom": shapingRulesSetCountMom,
       "shapingRulesSetCountMax": shapingRulesSetCountMax,
       "shapingEnqueuedBytes": shapingEnqueuedBytes,
       "shapingEnqueuedBytesVal": shapingEnqueuedBytesVal,
       "shapingEnqueuedBytesMom": shapingEnqueuedBytesMom,
       "shapingEnqueuedBytesMax": shapingEnqueuedBytesMax,
       "shapingDequeuedBytes": shapingDequeuedBytes,
       "shapingDequeuedBytesVal": shapingDequeuedBytesVal,
       "shapingDequeuedBytesMom": shapingDequeuedBytesMom,
       "shapingDequeuedBytesMax": shapingDequeuedBytesMax,
       "shapingObjectCopies": shapingObjectCopies,
       "shapingObjectCopiesVal": shapingObjectCopiesVal,
       "shapingObjectCopiesMax": shapingObjectCopiesMax,
       "shapingOutofpacketsDrops": shapingOutofpacketsDrops,
       "shapingOutofpacketsDropsVal": shapingOutofpacketsDropsVal,
       "shapingOutofpacketsDropsMom": shapingOutofpacketsDropsMom,
       "shapingOutofpacketsDropsMax": shapingOutofpacketsDropsMax,
       "shapingReceived": shapingReceived,
       "shapingReceivedVal": shapingReceivedVal,
       "shapingReceivedMom": shapingReceivedMom,
       "shapingReceivedMax": shapingReceivedMax,
       "shapingObjectChecks": shapingObjectChecks,
       "shapingObjectChecksVal": shapingObjectChecksVal,
       "shapingObjectChecksMom": shapingObjectChecksMom,
       "shapingObjectChecksMax": shapingObjectChecksMax,
       "shapingObjectPoolExhausted": shapingObjectPoolExhausted,
       "shapingObjectPoolExhaustedVal": shapingObjectPoolExhaustedVal,
       "shapingObjectPoolExhaustedMom": shapingObjectPoolExhaustedMom,
       "shapingObjectPoolExhaustedMax": shapingObjectPoolExhaustedMax,
       "shapingOutOfCreditsDrops": shapingOutOfCreditsDrops,
       "shapingOutOfCreditsDropsVal": shapingOutOfCreditsDropsVal,
       "shapingOutOfCreditsDropsMom": shapingOutOfCreditsDropsMom,
       "shapingOutOfCreditsDropsMax": shapingOutOfCreditsDropsMax,
       "shapingObjectOverflow": shapingObjectOverflow,
       "shapingObjectOverflowVal": shapingObjectOverflowVal,
       "shapingObjectOverflowMom": shapingObjectOverflowMom,
       "shapingObjectOverflowMax": shapingObjectOverflowMax,
       "shapingRuleOverflow": shapingRuleOverflow,
       "shapingRuleOverflowVal": shapingRuleOverflowVal,
       "shapingRuleOverflowMom": shapingRuleOverflowMom,
       "shapingRuleOverflowMax": shapingRuleOverflowMax,
       "shapingDrops": shapingDrops,
       "shapingDropsVal": shapingDropsVal,
       "shapingDropsMom": shapingDropsMom,
       "shapingDropsMax": shapingDropsMax,
       "shapingObjectFull": shapingObjectFull,
       "shapingObjectFullVal": shapingObjectFullVal,
       "shapingObjectFullMom": shapingObjectFullMom,
       "shapingObjectFullMax": shapingObjectFullMax,
       "shapingUnshaped": shapingUnshaped,
       "shapingUnshapedVal": shapingUnshapedVal,
       "shapingUnshapedMom": shapingUnshapedMom,
       "shapingUnshapedMax": shapingUnshapedMax,
       "shapingUnshapedBytes": shapingUnshapedBytes,
       "shapingUnshapedBytesVal": shapingUnshapedBytesVal,
       "shapingUnshapedBytesMom": shapingUnshapedBytesMom,
       "shapingUnshapedBytesMax": shapingUnshapedBytesMax,
       "shapingDequeueCalls": shapingDequeueCalls,
       "shapingDequeueCallsVal": shapingDequeueCallsVal,
       "shapingDequeueCallsMom": shapingDequeueCallsMom,
       "shapingDequeueCallsMax": shapingDequeueCallsMax,
       "shapingRecycleObjects": shapingRecycleObjects,
       "shapingRecycleObjectsVal": shapingRecycleObjectsVal,
       "shapingRecycleObjectsMax": shapingRecycleObjectsMax,
       "shapingDirect": shapingDirect,
       "shapingDirectVal": shapingDirectVal,
       "shapingDirectMom": shapingDirectMom,
       "shapingDirectMax": shapingDirectMax,
       "shapingDirectBytes": shapingDirectBytes,
       "shapingDirectBytesVal": shapingDirectBytesVal,
       "shapingDirectBytesMom": shapingDirectBytesMom,
       "shapingDirectBytesMax": shapingDirectBytesMax,
       "shapingBorrowDequeues": shapingBorrowDequeues,
       "shapingBorrowDequeuesVal": shapingBorrowDequeuesVal,
       "shapingBorrowDequeuesMom": shapingBorrowDequeuesMom,
       "shapingBorrowDequeuesMax": shapingBorrowDequeuesMax,
       "shapingVbsSplitError": shapingVbsSplitError,
       "shapingVbsSplitErrorVal": shapingVbsSplitErrorVal,
       "shapingVbsSplitErrorMom": shapingVbsSplitErrorMom,
       "shapingVbsSplitErrorMax": shapingVbsSplitErrorMax,
       "shapingBrownHostDrops": shapingBrownHostDrops,
       "shapingBrownHostDropsVal": shapingBrownHostDropsVal,
       "shapingBrownHostDropsMom": shapingBrownHostDropsMom,
       "shapingBrownHostDropsMax": shapingBrownHostDropsMax,
       "shapingMaxConnDrops": shapingMaxConnDrops,
       "shapingMaxConnDropsVal": shapingMaxConnDropsVal,
       "shapingMaxConnDropsMom": shapingMaxConnDropsMom,
       "shapingMaxConnDropsMax": shapingMaxConnDropsMax,
       "shapingScheduledOdirs": shapingScheduledOdirs,
       "shapingScheduledOdirsVal": shapingScheduledOdirsVal,
       "shapingScheduledOdirsMax": shapingScheduledOdirsMax,
       "shapingQueuePoolExhausted": shapingQueuePoolExhausted,
       "shapingQueuePoolExhaustedVal": shapingQueuePoolExhaustedVal,
       "shapingQueuePoolExhaustedMom": shapingQueuePoolExhaustedMom,
       "shapingQueuePoolExhaustedMax": shapingQueuePoolExhaustedMax,
       "shapingActiveQueues": shapingActiveQueues,
       "shapingActiveQueuesVal": shapingActiveQueuesVal,
       "shapingActiveQueuesMax": shapingActiveQueuesMax,
       "shapingQueueAllocations": shapingQueueAllocations,
       "shapingQueueAllocationsVal": shapingQueueAllocationsVal,
       "shapingQueueAllocationsMom": shapingQueueAllocationsMom,
       "shapingQueueAllocationsMax": shapingQueueAllocationsMax,
       "shapingDropsPrio1": shapingDropsPrio1,
       "shapingDropsPrio1Val": shapingDropsPrio1Val,
       "shapingDropsPrio1Mom": shapingDropsPrio1Mom,
       "shapingDropsPrio1Max": shapingDropsPrio1Max,
       "shapingDropsPrio2": shapingDropsPrio2,
       "shapingDropsPrio2Val": shapingDropsPrio2Val,
       "shapingDropsPrio2Mom": shapingDropsPrio2Mom,
       "shapingDropsPrio2Max": shapingDropsPrio2Max,
       "shapingDropsPrio3": shapingDropsPrio3,
       "shapingDropsPrio3Val": shapingDropsPrio3Val,
       "shapingDropsPrio3Mom": shapingDropsPrio3Mom,
       "shapingDropsPrio3Max": shapingDropsPrio3Max,
       "shapingDropsPrio4": shapingDropsPrio4,
       "shapingDropsPrio4Val": shapingDropsPrio4Val,
       "shapingDropsPrio4Mom": shapingDropsPrio4Mom,
       "shapingDropsPrio4Max": shapingDropsPrio4Max,
       "shapingDropsPrio5": shapingDropsPrio5,
       "shapingDropsPrio5Val": shapingDropsPrio5Val,
       "shapingDropsPrio5Mom": shapingDropsPrio5Mom,
       "shapingDropsPrio5Max": shapingDropsPrio5Max,
       "shapingDropsPrio6": shapingDropsPrio6,
       "shapingDropsPrio6Val": shapingDropsPrio6Val,
       "shapingDropsPrio6Mom": shapingDropsPrio6Mom,
       "shapingDropsPrio6Max": shapingDropsPrio6Max,
       "shapingDropsPrio7": shapingDropsPrio7,
       "shapingDropsPrio7Val": shapingDropsPrio7Val,
       "shapingDropsPrio7Mom": shapingDropsPrio7Mom,
       "shapingDropsPrio7Max": shapingDropsPrio7Max,
       "shapingDropsPrio8": shapingDropsPrio8,
       "shapingDropsPrio8Val": shapingDropsPrio8Val,
       "shapingDropsPrio8Mom": shapingDropsPrio8Mom,
       "shapingDropsPrio8Max": shapingDropsPrio8Max,
       "shapingDropsPrio9": shapingDropsPrio9,
       "shapingDropsPrio9Val": shapingDropsPrio9Val,
       "shapingDropsPrio9Mom": shapingDropsPrio9Mom,
       "shapingDropsPrio9Max": shapingDropsPrio9Max,
       "shapingDropsPrioOther": shapingDropsPrioOther,
       "shapingDropsPrioOtherVal": shapingDropsPrioOtherVal,
       "shapingDropsPrioOtherMom": shapingDropsPrioOtherMom,
       "shapingDropsPrioOtherMax": shapingDropsPrioOtherMax,
       "shapingDropsCps": shapingDropsCps,
       "shapingDropsCpsVal": shapingDropsCpsVal,
       "shapingDropsCpsMom": shapingDropsCpsMom,
       "shapingDropsCpsMax": shapingDropsCpsMax,
       "shapingFailedFairnessObjects": shapingFailedFairnessObjects,
       "shapingFailedFairnessObjectsVal": shapingFailedFairnessObjectsVal,
       "shapingFailedFairnessObjectsMom": shapingFailedFairnessObjectsMom,
       "shapingFailedFairnessObjectsMax": shapingFailedFairnessObjectsMax,
       "shapingUsedFairnessObjects": shapingUsedFairnessObjects,
       "shapingUsedFairnessObjectsVal": shapingUsedFairnessObjectsVal,
       "shapingUsedFairnessObjectsMax": shapingUsedFairnessObjectsMax,
       "shapingReloadDrops": shapingReloadDrops,
       "shapingReloadDropsVal": shapingReloadDropsVal,
       "shapingReloadDropsMom": shapingReloadDropsMom,
       "shapingReloadDropsMax": shapingReloadDropsMax,
       "shapingRequeueQueueUsed": shapingRequeueQueueUsed,
       "shapingRequeueQueueUsedVal": shapingRequeueQueueUsedVal,
       "shapingRequeueQueueUsedMax": shapingRequeueQueueUsedMax,
       "shapingDirectBytesPrio0": shapingDirectBytesPrio0,
       "shapingDirectBytesPrio0Val": shapingDirectBytesPrio0Val,
       "shapingDirectBytesPrio0Mom": shapingDirectBytesPrio0Mom,
       "shapingDirectBytesPrio0Max": shapingDirectBytesPrio0Max,
       "shapingDequeuedOdirs": shapingDequeuedOdirs,
       "shapingDequeuedOdirsVal": shapingDequeuedOdirsVal,
       "shapingDequeuedOdirsMom": shapingDequeuedOdirsMom,
       "shapingDequeuedOdirsMax": shapingDequeuedOdirsMax,
       "shapingSkippedQsyncUpdates": shapingSkippedQsyncUpdates,
       "shapingSkippedQsyncUpdatesVal": shapingSkippedQsyncUpdatesVal,
       "shapingSkippedQsyncUpdatesMom": shapingSkippedQsyncUpdatesMom,
       "shapingSkippedQsyncUpdatesMax": shapingSkippedQsyncUpdatesMax,
       "shapingObjectCopiesCreated": shapingObjectCopiesCreated,
       "shapingObjectCopiesCreatedVal": shapingObjectCopiesCreatedVal,
       "shapingObjectCopiesCreatedMom": shapingObjectCopiesCreatedMom,
       "shapingObjectCopiesCreatedMax": shapingObjectCopiesCreatedMax,
       "shapingEcnMarks": shapingEcnMarks,
       "shapingEcnMarksVal": shapingEcnMarksVal,
       "shapingEcnMarksMom": shapingEcnMarksMom,
       "shapingEcnMarksMax": shapingEcnMarksMax,
       "pppoe": pppoe,
       "pppoeShortPackets": pppoeShortPackets,
       "pppoeShortPacketsVal": pppoeShortPacketsVal,
       "pppoeShortPacketsMom": pppoeShortPacketsMom,
       "pppoeShortPacketsMax": pppoeShortPacketsMax,
       "pppoeBadversionPackets": pppoeBadversionPackets,
       "pppoeBadversionPacketsVal": pppoeBadversionPacketsVal,
       "pppoeBadversionPacketsMom": pppoeBadversionPacketsMom,
       "pppoeBadversionPacketsMax": pppoeBadversionPacketsMax,
       "pppoeControlPackets": pppoeControlPackets,
       "pppoeControlPacketsVal": pppoeControlPacketsVal,
       "pppoeControlPacketsMom": pppoeControlPacketsMom,
       "pppoeControlPacketsMax": pppoeControlPacketsMax,
       "pppoeTruncatedPackets": pppoeTruncatedPackets,
       "pppoeTruncatedPacketsVal": pppoeTruncatedPacketsVal,
       "pppoeTruncatedPacketsMom": pppoeTruncatedPacketsMom,
       "pppoeTruncatedPacketsMax": pppoeTruncatedPacketsMax,
       "pppoePaddedPackets": pppoePaddedPackets,
       "pppoePaddedPacketsVal": pppoePaddedPacketsVal,
       "pppoePaddedPacketsMom": pppoePaddedPacketsMom,
       "pppoePaddedPacketsMax": pppoePaddedPacketsMax,
       "pppoeIpv4Packets": pppoeIpv4Packets,
       "pppoeIpv4PacketsVal": pppoeIpv4PacketsVal,
       "pppoeIpv4PacketsMom": pppoeIpv4PacketsMom,
       "pppoeIpv4PacketsMax": pppoeIpv4PacketsMax,
       "pppoeNonIpPackets": pppoeNonIpPackets,
       "pppoeNonIpPacketsVal": pppoeNonIpPacketsVal,
       "pppoeNonIpPacketsMom": pppoeNonIpPacketsMom,
       "pppoeNonIpPacketsMax": pppoeNonIpPacketsMax,
       "pppoeIpv6Packets": pppoeIpv6Packets,
       "pppoeIpv6PacketsVal": pppoeIpv6PacketsVal,
       "pppoeIpv6PacketsMom": pppoeIpv6PacketsMom,
       "pppoeIpv6PacketsMax": pppoeIpv6PacketsMax,
       "interface": interface,
       "interfaceBytesToEngine": interfaceBytesToEngine,
       "interfaceBytesToEngineVal": interfaceBytesToEngineVal,
       "interfaceBytesToEngineMom": interfaceBytesToEngineMom,
       "interfaceBytesToEngineMax": interfaceBytesToEngineMax,
       "interfaceBytesFromEngine": interfaceBytesFromEngine,
       "interfaceBytesFromEngineVal": interfaceBytesFromEngineVal,
       "interfaceBytesFromEngineMom": interfaceBytesFromEngineMom,
       "interfaceBytesFromEngineMax": interfaceBytesFromEngineMax,
       "interfaceFlowNewMissed": interfaceFlowNewMissed,
       "interfaceFlowNewMissedVal": interfaceFlowNewMissedVal,
       "interfaceFlowNewMissedMom": interfaceFlowNewMissedMom,
       "interfaceFlowNewMissedMax": interfaceFlowNewMissedMax,
       "interfaceFlowUpdMissed": interfaceFlowUpdMissed,
       "interfaceFlowUpdMissedVal": interfaceFlowUpdMissedVal,
       "interfaceFlowUpdMissedMom": interfaceFlowUpdMissedMom,
       "interfaceFlowUpdMissedMax": interfaceFlowUpdMissedMax,
       "interfaceFlowNew": interfaceFlowNew,
       "interfaceFlowNewVal": interfaceFlowNewVal,
       "interfaceFlowNewMom": interfaceFlowNewMom,
       "interfaceFlowNewMax": interfaceFlowNewMax,
       "interfaceFlowHostnameAllocFail": interfaceFlowHostnameAllocFail,
       "interfaceFlowHostnameAllocFailVal": interfaceFlowHostnameAllocFailVal,
       "interfaceFlowHostnameAllocFailMom": interfaceFlowHostnameAllocFailMom,
       "interfaceFlowHostnameAllocFailMax": interfaceFlowHostnameAllocFailMax,
       "interfaceFlowUpdReordered": interfaceFlowUpdReordered,
       "interfaceFlowUpdReorderedVal": interfaceFlowUpdReorderedVal,
       "interfaceFlowUpdReorderedMom": interfaceFlowUpdReorderedMom,
       "interfaceFlowUpdReorderedMax": interfaceFlowUpdReorderedMax,
       "dynnetobjs": dynnetobjs,
       "dynamicnetobjectFailedInserts": dynamicnetobjectFailedInserts,
       "dynamicnetobjectFailedInsertsVal": dynamicnetobjectFailedInsertsVal,
       "dynamicnetobjectFailedInsertsMom": dynamicnetobjectFailedInsertsMom,
       "dynamicnetobjectFailedInsertsMax": dynamicnetobjectFailedInsertsMax,
       "dynamicnetobjectListItems": dynamicnetobjectListItems,
       "dynamicnetobjectListItemsVal": dynamicnetobjectListItemsVal,
       "dynamicnetobjectListItemsMax": dynamicnetobjectListItemsMax,
       "dynamicnetobjectRemoveSucceeded": dynamicnetobjectRemoveSucceeded,
       "dynamicnetobjectRemoveSucceededVal": dynamicnetobjectRemoveSucceededVal,
       "dynamicnetobjectRemoveSucceededMom": dynamicnetobjectRemoveSucceededMom,
       "dynamicnetobjectRemoveSucceededMax": dynamicnetobjectRemoveSucceededMax,
       "dynamicnetobjectRemoveFailed": dynamicnetobjectRemoveFailed,
       "dynamicnetobjectRemoveFailedVal": dynamicnetobjectRemoveFailedVal,
       "dynamicnetobjectRemoveFailedMom": dynamicnetobjectRemoveFailedMom,
       "dynamicnetobjectRemoveFailedMax": dynamicnetobjectRemoveFailedMax,
       "dynamicnetobjectCurrentIpCount": dynamicnetobjectCurrentIpCount,
       "dynamicnetobjectCurrentIpCountVal": dynamicnetobjectCurrentIpCountVal,
       "dynamicnetobjectCurrentIpCountMax": dynamicnetobjectCurrentIpCountMax,
       "dynamicnetobjectCurrentCount": dynamicnetobjectCurrentCount,
       "dynamicnetobjectCurrentCountVal": dynamicnetobjectCurrentCountVal,
       "dynamicnetobjectCurrentCountMax": dynamicnetobjectCurrentCountMax,
       "dynamicnetobjectAddSucceeded": dynamicnetobjectAddSucceeded,
       "dynamicnetobjectAddSucceededVal": dynamicnetobjectAddSucceededVal,
       "dynamicnetobjectAddSucceededMom": dynamicnetobjectAddSucceededMom,
       "dynamicnetobjectAddSucceededMax": dynamicnetobjectAddSucceededMax,
       "dynamicnetobjectAddFailed": dynamicnetobjectAddFailed,
       "dynamicnetobjectAddFailedVal": dynamicnetobjectAddFailedVal,
       "dynamicnetobjectAddFailedMom": dynamicnetobjectAddFailedMom,
       "dynamicnetobjectAddFailedMax": dynamicnetobjectAddFailedMax,
       "dynamicnetobjectInsertPldbFailed": dynamicnetobjectInsertPldbFailed,
       "dynamicnetobjectInsertPldbFailedVal": dynamicnetobjectInsertPldbFailedVal,
       "dynamicnetobjectInsertPldbFailedMom": dynamicnetobjectInsertPldbFailedMom,
       "dynamicnetobjectInsertPldbFailedMax": dynamicnetobjectInsertPldbFailedMax,
       "dynamicnetobjectAddCalls": dynamicnetobjectAddCalls,
       "dynamicnetobjectAddCallsVal": dynamicnetobjectAddCallsVal,
       "dynamicnetobjectAddCallsMom": dynamicnetobjectAddCallsMom,
       "dynamicnetobjectAddCallsMax": dynamicnetobjectAddCallsMax,
       "dynamicnetobjectRemoveCalls": dynamicnetobjectRemoveCalls,
       "dynamicnetobjectRemoveCallsVal": dynamicnetobjectRemoveCallsVal,
       "dynamicnetobjectRemoveCallsMom": dynamicnetobjectRemoveCallsMom,
       "dynamicnetobjectRemoveCallsMax": dynamicnetobjectRemoveCallsMax,
       "dynamicnetobjectListCalls": dynamicnetobjectListCalls,
       "dynamicnetobjectListCallsVal": dynamicnetobjectListCallsVal,
       "dynamicnetobjectListCallsMom": dynamicnetobjectListCallsMom,
       "dynamicnetobjectListCallsMax": dynamicnetobjectListCallsMax,
       "dynamicnetobjectListItemsReturned": dynamicnetobjectListItemsReturned,
       "dynamicnetobjectListItemsReturnedVal": dynamicnetobjectListItemsReturnedVal,
       "dynamicnetobjectListItemsReturnedMom": dynamicnetobjectListItemsReturnedMom,
       "dynamicnetobjectListItemsReturnedMax": dynamicnetobjectListItemsReturnedMax,
       "dynamicnetobjectSubscriberConflicts": dynamicnetobjectSubscriberConflicts,
       "dynamicnetobjectSubscriberConflictsVal": dynamicnetobjectSubscriberConflictsVal,
       "dynamicnetobjectSubscriberConflictsMom": dynamicnetobjectSubscriberConflictsMom,
       "dynamicnetobjectSubscriberConflictsMax": dynamicnetobjectSubscriberConflictsMax,
       "dynamicnetobjectSubscriberCount": dynamicnetobjectSubscriberCount,
       "dynamicnetobjectSubscriberCountVal": dynamicnetobjectSubscriberCountVal,
       "dynamicnetobjectSubscriberCountMax": dynamicnetobjectSubscriberCountMax,
       "dynamicnetobjectSubscriberTooMany": dynamicnetobjectSubscriberTooMany,
       "dynamicnetobjectSubscriberTooManyVal": dynamicnetobjectSubscriberTooManyVal,
       "dynamicnetobjectSubscriberTooManyMom": dynamicnetobjectSubscriberTooManyMom,
       "dynamicnetobjectSubscriberTooManyMax": dynamicnetobjectSubscriberTooManyMax,
       "dynamicnetobjectSqliteMemoryUsed": dynamicnetobjectSqliteMemoryUsed,
       "dynamicnetobjectSqliteMemoryUsedVal": dynamicnetobjectSqliteMemoryUsedVal,
       "dynamicnetobjectSqliteMemoryUsedMax": dynamicnetobjectSqliteMemoryUsedMax,
       "dynamicnetobjectPendingAdds": dynamicnetobjectPendingAdds,
       "dynamicnetobjectPendingAddsVal": dynamicnetobjectPendingAddsVal,
       "dynamicnetobjectPendingAddsMax": dynamicnetobjectPendingAddsMax,
       "bgp": bgp,
       "bgpUpdates": bgpUpdates,
       "bgpUpdatesVal": bgpUpdatesVal,
       "bgpUpdatesMax": bgpUpdatesMax,
       "bgpPrefixes": bgpPrefixes,
       "bgpPrefixesVal": bgpPrefixesVal,
       "bgpPrefixesMax": bgpPrefixesMax,
       "bgpPaths": bgpPaths,
       "bgpPathsVal": bgpPathsVal,
       "bgpPathsMax": bgpPathsMax,
       "bgpUptime": bgpUptime,
       "bgpUptimeVal": bgpUptimeVal,
       "bgpConvresionTime": bgpConvresionTime,
       "bgpConvresionTimeVal": bgpConvresionTimeVal,
       "bgpConvresionTimeMax": bgpConvresionTimeMax,
       "bgpSendTime": bgpSendTime,
       "bgpSendTimeVal": bgpSendTimeVal,
       "bgpSendTimeMax": bgpSendTimeMax,
       "bgpReplaces": bgpReplaces,
       "bgpReplacesVal": bgpReplacesVal,
       "bgpReplacesMax": bgpReplacesMax,
       "bgpWithdraws": bgpWithdraws,
       "bgpWithdrawsVal": bgpWithdrawsVal,
       "bgpWithdrawsMax": bgpWithdrawsMax,
       "bgpAnnounces": bgpAnnounces,
       "bgpAnnouncesVal": bgpAnnouncesVal,
       "bgpAnnouncesMax": bgpAnnouncesMax,
       "bgpReconnects": bgpReconnects,
       "bgpReconnectsVal": bgpReconnectsVal,
       "bgpReconnectsMax": bgpReconnectsMax,
       "bgpRecyclePaths": bgpRecyclePaths,
       "bgpRecyclePathsVal": bgpRecyclePathsVal,
       "bgpRecyclePathsMax": bgpRecyclePathsMax,
       "bgpFreelistPaths": bgpFreelistPaths,
       "bgpFreelistPathsVal": bgpFreelistPathsVal,
       "bgpFreelistPathsMax": bgpFreelistPathsMax,
       "bgpBalanceTime": bgpBalanceTime,
       "bgpBalanceTimeVal": bgpBalanceTimeVal,
       "bgpBalanceTimeMax": bgpBalanceTimeMax,
       "bgpCommunityTooSmall": bgpCommunityTooSmall,
       "bgpCommunityTooSmallVal": bgpCommunityTooSmallVal,
       "bgpCommunityTooSmallMax": bgpCommunityTooSmallMax,
       "bgpCommunityMaxSeen": bgpCommunityMaxSeen,
       "bgpCommunityMaxSeenVal": bgpCommunityMaxSeenVal,
       "bgpCommunityMaxSeenMax": bgpCommunityMaxSeenMax,
       "qsync": qsync,
       "qsyncIUpdates": qsyncIUpdates,
       "qsyncIUpdatesVal": qsyncIUpdatesVal,
       "qsyncIUpdatesMom": qsyncIUpdatesMom,
       "qsyncIUpdatesMax": qsyncIUpdatesMax,
       "qsyncIUpdatesOldRuleset": qsyncIUpdatesOldRuleset,
       "qsyncIUpdatesOldRulesetVal": qsyncIUpdatesOldRulesetVal,
       "qsyncIUpdatesOldRulesetMom": qsyncIUpdatesOldRulesetMom,
       "qsyncIUpdatesOldRulesetMax": qsyncIUpdatesOldRulesetMax,
       "qsyncIUpdatesUnknownObject": qsyncIUpdatesUnknownObject,
       "qsyncIUpdatesUnknownObjectVal": qsyncIUpdatesUnknownObjectVal,
       "qsyncIUpdatesUnknownObjectMom": qsyncIUpdatesUnknownObjectMom,
       "qsyncIUpdatesUnknownObjectMax": qsyncIUpdatesUnknownObjectMax,
       "qsyncIReaperSplitsCreated": qsyncIReaperSplitsCreated,
       "qsyncIReaperSplitsCreatedVal": qsyncIReaperSplitsCreatedVal,
       "qsyncIReaperSplitsCreatedMom": qsyncIReaperSplitsCreatedMom,
       "qsyncIReaperSplitsCreatedMax": qsyncIReaperSplitsCreatedMax,
       "qsyncIReaperSplitsActive": qsyncIReaperSplitsActive,
       "qsyncIReaperSplitsActiveVal": qsyncIReaperSplitsActiveVal,
       "qsyncIReaperSplitsActiveMax": qsyncIReaperSplitsActiveMax,
       "qsyncISumFreelistSize": qsyncISumFreelistSize,
       "qsyncISumFreelistSizeVal": qsyncISumFreelistSizeVal,
       "qsyncISumFreelistSizeMax": qsyncISumFreelistSizeMax,
       "qsyncISumSplitsActive": qsyncISumSplitsActive,
       "qsyncISumSplitsActiveVal": qsyncISumSplitsActiveVal,
       "qsyncISumSplitsActiveMax": qsyncISumSplitsActiveMax,
       "qsyncIAdjustmentsSent": qsyncIAdjustmentsSent,
       "qsyncIAdjustmentsSentVal": qsyncIAdjustmentsSentVal,
       "qsyncIAdjustmentsSentMom": qsyncIAdjustmentsSentMom,
       "qsyncIAdjustmentsSentMax": qsyncIAdjustmentsSentMax,
       "qsyncENumPeers": qsyncENumPeers,
       "qsyncENumPeersVal": qsyncENumPeersVal,
       "qsyncENumPeersMax": qsyncENumPeersMax,
       "qsyncEUpdatesMismatch": qsyncEUpdatesMismatch,
       "qsyncEUpdatesMismatchVal": qsyncEUpdatesMismatchVal,
       "qsyncEUpdatesMismatchMom": qsyncEUpdatesMismatchMom,
       "qsyncEUpdatesMismatchMax": qsyncEUpdatesMismatchMax,
       "qsyncEUpdatePackets": qsyncEUpdatePackets,
       "qsyncEUpdatePacketsVal": qsyncEUpdatePacketsVal,
       "qsyncEUpdatePacketsMom": qsyncEUpdatePacketsMom,
       "qsyncEUpdatePacketsMax": qsyncEUpdatePacketsMax,
       "qsyncESplitTimeout": qsyncESplitTimeout,
       "qsyncESplitTimeoutVal": qsyncESplitTimeoutVal,
       "qsyncESplitTimeoutMom": qsyncESplitTimeoutMom,
       "qsyncESplitTimeoutMax": qsyncESplitTimeoutMax,
       "qsyncERecvUpdateEntries": qsyncERecvUpdateEntries,
       "qsyncERecvUpdateEntriesVal": qsyncERecvUpdateEntriesVal,
       "qsyncERecvUpdateEntriesMom": qsyncERecvUpdateEntriesMom,
       "qsyncERecvUpdateEntriesMax": qsyncERecvUpdateEntriesMax,
       "qsyncESendUpdateEntries": qsyncESendUpdateEntries,
       "qsyncESendUpdateEntriesVal": qsyncESendUpdateEntriesVal,
       "qsyncESendUpdateEntriesMom": qsyncESendUpdateEntriesMom,
       "qsyncESendUpdateEntriesMax": qsyncESendUpdateEntriesMax,
       "qsyncESendUpdatePackets": qsyncESendUpdatePackets,
       "qsyncESendUpdatePacketsVal": qsyncESendUpdatePacketsVal,
       "qsyncESendUpdatePacketsMom": qsyncESendUpdatePacketsMom,
       "qsyncESendUpdatePacketsMax": qsyncESendUpdatePacketsMax,
       "qsyncIUnsync": qsyncIUnsync,
       "qsyncIUnsyncVal": qsyncIUnsyncVal,
       "qsyncIUnsyncMom": qsyncIUnsyncMom,
       "qsyncIUnsyncMax": qsyncIUnsyncMax,
       "qsyncESendbufFull": qsyncESendbufFull,
       "qsyncESendbufFullVal": qsyncESendbufFullVal,
       "qsyncESendbufFullMom": qsyncESendbufFullMom,
       "qsyncESendbufFullMax": qsyncESendbufFullMax,
       "qsyncESendbufUsage": qsyncESendbufUsage,
       "qsyncESendbufUsageVal": qsyncESendbufUsageVal,
       "qsyncESendbufUsageMax": qsyncESendbufUsageMax,
       "qsyncIIgnoredOOO": qsyncIIgnoredOOO,
       "qsyncIIgnoredOOOVal": qsyncIIgnoredOOOVal,
       "qsyncIIgnoredOOOMom": qsyncIIgnoredOOOMom,
       "qsyncIIgnoredOOOMax": qsyncIIgnoredOOOMax,
       "qsyncIIgnoredGenWrap": qsyncIIgnoredGenWrap,
       "qsyncIIgnoredGenWrapVal": qsyncIIgnoredGenWrapVal,
       "qsyncIIgnoredGenWrapMom": qsyncIIgnoredGenWrapMom,
       "qsyncIIgnoredGenWrapMax": qsyncIIgnoredGenWrapMax,
       "shapingcounter": shapingcounter,
       "shapingcounterUpdates": shapingcounterUpdates,
       "shapingcounterUpdatesVal": shapingcounterUpdatesVal,
       "shapingcounterUpdatesMom": shapingcounterUpdatesMom,
       "shapingcounterUpdatesMax": shapingcounterUpdatesMax,
       "shapingcounterActive": shapingcounterActive,
       "shapingcounterActiveVal": shapingcounterActiveVal,
       "shapingcounterActiveMax": shapingcounterActiveMax,
       "shapingcounterClients": shapingcounterClients,
       "shapingcounterClientsVal": shapingcounterClientsVal,
       "shapingcounterClientsMax": shapingcounterClientsMax,
       "shapingcounterRecycle": shapingcounterRecycle,
       "shapingcounterRecycleVal": shapingcounterRecycleVal,
       "shapingcounterRecycleMom": shapingcounterRecycleMom,
       "shapingcounterRecycleMax": shapingcounterRecycleMax,
       "shapingcounterUpdatesInteresting": shapingcounterUpdatesInteresting,
       "shapingcounterUpdatesInterestingVal": shapingcounterUpdatesInterestingVal,
       "shapingcounterUpdatesInterestingMom": shapingcounterUpdatesInterestingMom,
       "shapingcounterUpdatesInterestingMax": shapingcounterUpdatesInterestingMax,
       "divert": divert,
       "divertOutOfHosts": divertOutOfHosts,
       "divertOutOfHostsVal": divertOutOfHostsVal,
       "divertOutOfHostsMom": divertOutOfHostsMom,
       "divertOutOfHostsMax": divertOutOfHostsMax,
       "divertOversizeL2": divertOversizeL2,
       "divertOversizeL2Val": divertOversizeL2Val,
       "divertOversizeL2Mom": divertOversizeL2Mom,
       "divertOversizeL2Max": divertOversizeL2Max,
       "divertEgressPackets": divertEgressPackets,
       "divertEgressPacketsVal": divertEgressPacketsVal,
       "divertEgressPacketsMom": divertEgressPacketsMom,
       "divertEgressPacketsMax": divertEgressPacketsMax,
       "divertEgressBytes": divertEgressBytes,
       "divertEgressBytesVal": divertEgressBytesVal,
       "divertEgressBytesMom": divertEgressBytesMom,
       "divertEgressBytesMax": divertEgressBytesMax,
       "divertIngressPackets": divertIngressPackets,
       "divertIngressPacketsVal": divertIngressPacketsVal,
       "divertIngressPacketsMom": divertIngressPacketsMom,
       "divertIngressPacketsMax": divertIngressPacketsMax,
       "divertIngressBytes": divertIngressBytes,
       "divertIngressBytesVal": divertIngressBytesVal,
       "divertIngressBytesMom": divertIngressBytesMom,
       "divertIngressBytesMax": divertIngressBytesMax,
       "divertIngressPacketsNohost": divertIngressPacketsNohost,
       "divertIngressPacketsNohostVal": divertIngressPacketsNohostVal,
       "divertIngressPacketsNohostMom": divertIngressPacketsNohostMom,
       "divertIngressPacketsNohostMax": divertIngressPacketsNohostMax,
       "divertIngressPacketsNol2": divertIngressPacketsNol2,
       "divertIngressPacketsNol2Val": divertIngressPacketsNol2Val,
       "divertIngressPacketsNol2Mom": divertIngressPacketsNol2Mom,
       "divertIngressPacketsNol2Max": divertIngressPacketsNol2Max,
       "divertHostsUse": divertHostsUse,
       "divertHostsUseVal": divertHostsUseVal,
       "divertHostsUseMax": divertHostsUseMax,
       "divertConnections": divertConnections,
       "divertConnectionsVal": divertConnectionsVal,
       "divertConnectionsMax": divertConnectionsMax,
       "divertHbReqSent": divertHbReqSent,
       "divertHbReqSentVal": divertHbReqSentVal,
       "divertHbReqSentMom": divertHbReqSentMom,
       "divertHbReqSentMax": divertHbReqSentMax,
       "divertHbReqRecv": divertHbReqRecv,
       "divertHbReqRecvVal": divertHbReqRecvVal,
       "divertHbReqRecvMom": divertHbReqRecvMom,
       "divertHbReqRecvMax": divertHbReqRecvMax,
       "divertHbRepSent": divertHbRepSent,
       "divertHbRepSentVal": divertHbRepSentVal,
       "divertHbRepSentMom": divertHbRepSentMom,
       "divertHbRepSentMax": divertHbRepSentMax,
       "divertHbRepRecv": divertHbRepRecv,
       "divertHbRepRecvVal": divertHbRepRecvVal,
       "divertHbRepRecvMom": divertHbRepRecvMom,
       "divertHbRepRecvMax": divertHbRepRecvMax,
       "divertHbLost": divertHbLost,
       "divertHbLostVal": divertHbLostVal,
       "divertHbLostMom": divertHbLostMom,
       "divertHbLostMax": divertHbLostMax,
       "divertBypassPackets": divertBypassPackets,
       "divertBypassPacketsVal": divertBypassPacketsVal,
       "divertBypassPacketsMom": divertBypassPacketsMom,
       "divertBypassPacketsMax": divertBypassPacketsMax,
       "divertDroppedPackets": divertDroppedPackets,
       "divertDroppedPacketsVal": divertDroppedPacketsVal,
       "divertDroppedPacketsMom": divertDroppedPacketsMom,
       "divertDroppedPacketsMax": divertDroppedPacketsMax,
       "ipv6": ipv6,
       "ipv6Packets": ipv6Packets,
       "ipv6PacketsVal": ipv6PacketsVal,
       "ipv6PacketsMom": ipv6PacketsMom,
       "ipv6PacketsMax": ipv6PacketsMax,
       "ipv6Bytes": ipv6Bytes,
       "ipv6BytesVal": ipv6BytesVal,
       "ipv6BytesMom": ipv6BytesMom,
       "ipv6BytesMax": ipv6BytesMax,
       "ipv6RefusedShort": ipv6RefusedShort,
       "ipv6RefusedShortVal": ipv6RefusedShortVal,
       "ipv6RefusedShortMom": ipv6RefusedShortMom,
       "ipv6RefusedShortMax": ipv6RefusedShortMax,
       "ipv6RefusedVersion": ipv6RefusedVersion,
       "ipv6RefusedVersionVal": ipv6RefusedVersionVal,
       "ipv6RefusedVersionMom": ipv6RefusedVersionMom,
       "ipv6RefusedVersionMax": ipv6RefusedVersionMax,
       "ipv6RefusedSelf": ipv6RefusedSelf,
       "ipv6RefusedSelfVal": ipv6RefusedSelfVal,
       "ipv6RefusedSelfMom": ipv6RefusedSelfMom,
       "ipv6RefusedSelfMax": ipv6RefusedSelfMax,
       "ipv6Fragmented": ipv6Fragmented,
       "ipv6FragmentedVal": ipv6FragmentedVal,
       "ipv6FragmentedMom": ipv6FragmentedMom,
       "ipv6FragmentedMax": ipv6FragmentedMax,
       "ipv6FragmentedIds": ipv6FragmentedIds,
       "ipv6FragmentedIdsVal": ipv6FragmentedIdsVal,
       "ipv6FragmentedIdsMax": ipv6FragmentedIdsMax,
       "ipv6Fragments": ipv6Fragments,
       "ipv6FragmentsVal": ipv6FragmentsVal,
       "ipv6FragmentsMax": ipv6FragmentsMax,
       "ipv6RefusedOof": ipv6RefusedOof,
       "ipv6RefusedOofVal": ipv6RefusedOofVal,
       "ipv6RefusedOofMom": ipv6RefusedOofMom,
       "ipv6RefusedOofMax": ipv6RefusedOofMax,
       "ipv6FragmentAllocationFailures": ipv6FragmentAllocationFailures,
       "ipv6FragmentAllocationFailuresVal": ipv6FragmentAllocationFailuresVal,
       "ipv6FragmentAllocationFailuresMom": ipv6FragmentAllocationFailuresMom,
       "ipv6FragmentAllocationFailuresMax": ipv6FragmentAllocationFailuresMax,
       "ipv6FragmentReassFail": ipv6FragmentReassFail,
       "ipv6FragmentReassFailVal": ipv6FragmentReassFailVal,
       "ipv6FragmentReassFailMom": ipv6FragmentReassFailMom,
       "ipv6FragmentReassFailMax": ipv6FragmentReassFailMax,
       "ipv6FragmentTooNoisy": ipv6FragmentTooNoisy,
       "ipv6FragmentTooNoisyVal": ipv6FragmentTooNoisyVal,
       "ipv6FragmentTooNoisyMom": ipv6FragmentTooNoisyMom,
       "ipv6FragmentTooNoisyMax": ipv6FragmentTooNoisyMax,
       "ipv6Reassembled": ipv6Reassembled,
       "ipv6ReassembledVal": ipv6ReassembledVal,
       "ipv6ReassembledMom": ipv6ReassembledMom,
       "ipv6ReassembledMax": ipv6ReassembledMax,
       "ipv6FragmentOverlap": ipv6FragmentOverlap,
       "ipv6FragmentOverlapVal": ipv6FragmentOverlapVal,
       "ipv6FragmentOverlapMom": ipv6FragmentOverlapMom,
       "ipv6FragmentOverlapMax": ipv6FragmentOverlapMax,
       "ipv6ExtDest": ipv6ExtDest,
       "ipv6ExtDestVal": ipv6ExtDestVal,
       "ipv6ExtDestMom": ipv6ExtDestMom,
       "ipv6ExtDestMax": ipv6ExtDestMax,
       "ipv6ExtHbh": ipv6ExtHbh,
       "ipv6ExtHbhVal": ipv6ExtHbhVal,
       "ipv6ExtHbhMom": ipv6ExtHbhMom,
       "ipv6ExtHbhMax": ipv6ExtHbhMax,
       "ipv6ExtRoute": ipv6ExtRoute,
       "ipv6ExtRouteVal": ipv6ExtRouteVal,
       "ipv6ExtRouteMom": ipv6ExtRouteMom,
       "ipv6ExtRouteMax": ipv6ExtRouteMax,
       "ipv6ExtInvl": ipv6ExtInvl,
       "ipv6ExtInvlVal": ipv6ExtInvlVal,
       "ipv6ExtInvlMom": ipv6ExtInvlMom,
       "ipv6ExtInvlMax": ipv6ExtInvlMax,
       "ipv6FragnentTimeout": ipv6FragnentTimeout,
       "ipv6FragnentTimeoutVal": ipv6FragnentTimeoutVal,
       "ipv6FragnentTimeoutMom": ipv6FragnentTimeoutMom,
       "ipv6FragnentTimeoutMax": ipv6FragnentTimeoutMax,
       "ipv6FragmentDrops": ipv6FragmentDrops,
       "ipv6FragmentDropsVal": ipv6FragmentDropsVal,
       "ipv6FragmentDropsMom": ipv6FragmentDropsMom,
       "ipv6FragmentDropsMax": ipv6FragmentDropsMax,
       "ipv6ShuntAddressPackets": ipv6ShuntAddressPackets,
       "ipv6ShuntAddressPacketsVal": ipv6ShuntAddressPacketsVal,
       "ipv6ShuntAddressPacketsMom": ipv6ShuntAddressPacketsMom,
       "ipv6ShuntAddressPacketsMax": ipv6ShuntAddressPacketsMax,
       "ipv6ShuntAddressBytes": ipv6ShuntAddressBytes,
       "ipv6ShuntAddressBytesVal": ipv6ShuntAddressBytesVal,
       "ipv6ShuntAddressBytesMom": ipv6ShuntAddressBytesMom,
       "ipv6ShuntAddressBytesMax": ipv6ShuntAddressBytesMax,
       "ipv6ShuntProtoPackets": ipv6ShuntProtoPackets,
       "ipv6ShuntProtoPacketsVal": ipv6ShuntProtoPacketsVal,
       "ipv6ShuntProtoPacketsMom": ipv6ShuntProtoPacketsMom,
       "ipv6ShuntProtoPacketsMax": ipv6ShuntProtoPacketsMax,
       "ipv6ShuntProtoBytes": ipv6ShuntProtoBytes,
       "ipv6ShuntProtoBytesVal": ipv6ShuntProtoBytesVal,
       "ipv6ShuntProtoBytesMom": ipv6ShuntProtoBytesMom,
       "ipv6ShuntProtoBytesMax": ipv6ShuntProtoBytesMax,
       "ipv6FragInFrag": ipv6FragInFrag,
       "ipv6FragInFragVal": ipv6FragInFragVal,
       "ipv6FragInFragMom": ipv6FragInFragMom,
       "ipv6FragInFragMax": ipv6FragInFragMax,
       "ipv6EcnEct0": ipv6EcnEct0,
       "ipv6EcnEct0Val": ipv6EcnEct0Val,
       "ipv6EcnEct0Mom": ipv6EcnEct0Mom,
       "ipv6EcnEct0Max": ipv6EcnEct0Max,
       "ipv6EcnEct1": ipv6EcnEct1,
       "ipv6EcnEct1Val": ipv6EcnEct1Val,
       "ipv6EcnEct1Mom": ipv6EcnEct1Mom,
       "ipv6EcnEct1Max": ipv6EcnEct1Max,
       "ipv6EcnCn": ipv6EcnCn,
       "ipv6EcnCnVal": ipv6EcnCnVal,
       "ipv6EcnCnMom": ipv6EcnCnMom,
       "ipv6EcnCnMax": ipv6EcnCnMax,
       "tcpv6": tcpv6,
       "tcpv6Packets": tcpv6Packets,
       "tcpv6PacketsVal": tcpv6PacketsVal,
       "tcpv6PacketsMom": tcpv6PacketsMom,
       "tcpv6PacketsMax": tcpv6PacketsMax,
       "tcpv6Bytes": tcpv6Bytes,
       "tcpv6BytesVal": tcpv6BytesVal,
       "tcpv6BytesMom": tcpv6BytesMom,
       "tcpv6BytesMax": tcpv6BytesMax,
       "tcpv6CreateAttempts": tcpv6CreateAttempts,
       "tcpv6CreateAttemptsVal": tcpv6CreateAttemptsVal,
       "tcpv6CreateAttemptsMom": tcpv6CreateAttemptsMom,
       "tcpv6CreateAttemptsMax": tcpv6CreateAttemptsMax,
       "tcpv6Created": tcpv6Created,
       "tcpv6CreatedVal": tcpv6CreatedVal,
       "tcpv6CreatedMom": tcpv6CreatedMom,
       "tcpv6CreatedMax": tcpv6CreatedMax,
       "tcpv6RefusedRuleset": tcpv6RefusedRuleset,
       "tcpv6RefusedRulesetVal": tcpv6RefusedRulesetVal,
       "tcpv6RefusedRulesetMom": tcpv6RefusedRulesetMom,
       "tcpv6RefusedRulesetMax": tcpv6RefusedRulesetMax,
       "tcpv6RefusedShort": tcpv6RefusedShort,
       "tcpv6RefusedShortVal": tcpv6RefusedShortVal,
       "tcpv6RefusedShortMom": tcpv6RefusedShortMom,
       "tcpv6RefusedShortMax": tcpv6RefusedShortMax,
       "tcpv6RefusedBroadcast": tcpv6RefusedBroadcast,
       "tcpv6RefusedBroadcastVal": tcpv6RefusedBroadcastVal,
       "tcpv6RefusedBroadcastMom": tcpv6RefusedBroadcastMom,
       "tcpv6RefusedBroadcastMax": tcpv6RefusedBroadcastMax,
       "tcpv6RefusedOffset": tcpv6RefusedOffset,
       "tcpv6RefusedOffsetVal": tcpv6RefusedOffsetVal,
       "tcpv6RefusedOffsetMom": tcpv6RefusedOffsetMom,
       "tcpv6RefusedOffsetMax": tcpv6RefusedOffsetMax,
       "tcpv6Rejected": tcpv6Rejected,
       "tcpv6RejectedVal": tcpv6RejectedVal,
       "tcpv6RejectedMom": tcpv6RejectedMom,
       "tcpv6RejectedMax": tcpv6RejectedMax,
       "tcpv6Lostsync": tcpv6Lostsync,
       "tcpv6LostsyncVal": tcpv6LostsyncVal,
       "tcpv6LostsyncMax": tcpv6LostsyncMax,
       "tcpv6UntrackedPackets": tcpv6UntrackedPackets,
       "tcpv6UntrackedPacketsVal": tcpv6UntrackedPacketsVal,
       "tcpv6UntrackedPacketsMom": tcpv6UntrackedPacketsMom,
       "tcpv6UntrackedPacketsMax": tcpv6UntrackedPacketsMax,
       "tcpv6GoodputPackets": tcpv6GoodputPackets,
       "tcpv6GoodputPacketsVal": tcpv6GoodputPacketsVal,
       "tcpv6GoodputPacketsMom": tcpv6GoodputPacketsMom,
       "tcpv6GoodputPacketsMax": tcpv6GoodputPacketsMax,
       "tcpv6GoodputBytes": tcpv6GoodputBytes,
       "tcpv6GoodputBytesVal": tcpv6GoodputBytesVal,
       "tcpv6GoodputBytesMom": tcpv6GoodputBytesMom,
       "tcpv6GoodputBytesMax": tcpv6GoodputBytesMax,
       "tcpv6Segments": tcpv6Segments,
       "tcpv6SegmentsVal": tcpv6SegmentsVal,
       "tcpv6SegmentsMax": tcpv6SegmentsMax,
       "tcpv6SegmentsPayload": tcpv6SegmentsPayload,
       "tcpv6SegmentsPayloadVal": tcpv6SegmentsPayloadVal,
       "tcpv6SegmentsPayloadMax": tcpv6SegmentsPayloadMax,
       "tcpv6SegmentsDropped": tcpv6SegmentsDropped,
       "tcpv6SegmentsDroppedVal": tcpv6SegmentsDroppedVal,
       "tcpv6SegmentsDroppedMom": tcpv6SegmentsDroppedMom,
       "tcpv6SegmentsDroppedMax": tcpv6SegmentsDroppedMax,
       "tcpv6PacketAllocFail": tcpv6PacketAllocFail,
       "tcpv6PacketAllocFailVal": tcpv6PacketAllocFailVal,
       "tcpv6PacketAllocFailMom": tcpv6PacketAllocFailMom,
       "tcpv6PacketAllocFailMax": tcpv6PacketAllocFailMax,
       "tcpv6UntrackedGoodput": tcpv6UntrackedGoodput,
       "tcpv6UntrackedGoodputVal": tcpv6UntrackedGoodputVal,
       "tcpv6UntrackedGoodputMom": tcpv6UntrackedGoodputMom,
       "tcpv6UntrackedGoodputMax": tcpv6UntrackedGoodputMax,
       "tcpv6UntrackedBytes": tcpv6UntrackedBytes,
       "tcpv6UntrackedBytesVal": tcpv6UntrackedBytesVal,
       "tcpv6UntrackedBytesMom": tcpv6UntrackedBytesMom,
       "tcpv6UntrackedBytesMax": tcpv6UntrackedBytesMax,
       "tcpv6CorruptOptions": tcpv6CorruptOptions,
       "tcpv6CorruptOptionsVal": tcpv6CorruptOptionsVal,
       "tcpv6CorruptOptionsMom": tcpv6CorruptOptionsMom,
       "tcpv6CorruptOptionsMax": tcpv6CorruptOptionsMax,
       "tcpv6CorruptConn": tcpv6CorruptConn,
       "tcpv6CorruptConnVal": tcpv6CorruptConnVal,
       "tcpv6CorruptConnMom": tcpv6CorruptConnMom,
       "tcpv6CorruptConnMax": tcpv6CorruptConnMax,
       "tcpv6SegmentedConnections": tcpv6SegmentedConnections,
       "tcpv6SegmentedConnectionsVal": tcpv6SegmentedConnectionsVal,
       "tcpv6SegmentedConnectionsMax": tcpv6SegmentedConnectionsMax,
       "tcpv6OutOfWindowPackets": tcpv6OutOfWindowPackets,
       "tcpv6OutOfWindowPacketsVal": tcpv6OutOfWindowPacketsVal,
       "tcpv6OutOfWindowPacketsMom": tcpv6OutOfWindowPacketsMom,
       "tcpv6OutOfWindowPacketsMax": tcpv6OutOfWindowPacketsMax,
       "tcpv6RefusedFilter": tcpv6RefusedFilter,
       "tcpv6RefusedFilterVal": tcpv6RefusedFilterVal,
       "tcpv6RefusedFilterMom": tcpv6RefusedFilterMom,
       "tcpv6RefusedFilterMax": tcpv6RefusedFilterMax,
       "tcpv6SynExisting": tcpv6SynExisting,
       "tcpv6SynExistingVal": tcpv6SynExistingVal,
       "tcpv6SynExistingMom": tcpv6SynExistingMom,
       "tcpv6SynExistingMax": tcpv6SynExistingMax,
       "tcpv6SegmentAllocFail": tcpv6SegmentAllocFail,
       "tcpv6SegmentAllocFailVal": tcpv6SegmentAllocFailVal,
       "tcpv6SegmentAllocFailMom": tcpv6SegmentAllocFailMom,
       "tcpv6SegmentAllocFailMax": tcpv6SegmentAllocFailMax,
       "tcpv6EnqueuedSegments": tcpv6EnqueuedSegments,
       "tcpv6EnqueuedSegmentsVal": tcpv6EnqueuedSegmentsVal,
       "tcpv6EnqueuedSegmentsMom": tcpv6EnqueuedSegmentsMom,
       "tcpv6EnqueuedSegmentsMax": tcpv6EnqueuedSegmentsMax,
       "tcpv6DequeuedSegments": tcpv6DequeuedSegments,
       "tcpv6DequeuedSegmentsVal": tcpv6DequeuedSegmentsVal,
       "tcpv6DequeuedSegmentsMom": tcpv6DequeuedSegmentsMom,
       "tcpv6DequeuedSegmentsMax": tcpv6DequeuedSegmentsMax,
       "tcpv6DiscardedSegments": tcpv6DiscardedSegments,
       "tcpv6DiscardedSegmentsVal": tcpv6DiscardedSegmentsVal,
       "tcpv6DiscardedSegmentsMom": tcpv6DiscardedSegmentsMom,
       "tcpv6DiscardedSegmentsMax": tcpv6DiscardedSegmentsMax,
       "tcpv6EmptyPackets": tcpv6EmptyPackets,
       "tcpv6EmptyPacketsVal": tcpv6EmptyPacketsVal,
       "tcpv6EmptyPacketsMom": tcpv6EmptyPacketsMom,
       "tcpv6EmptyPacketsMax": tcpv6EmptyPacketsMax,
       "tcpv6OosPackets": tcpv6OosPackets,
       "tcpv6OosPacketsVal": tcpv6OosPacketsVal,
       "tcpv6OosPacketsMom": tcpv6OosPacketsMom,
       "tcpv6OosPacketsMax": tcpv6OosPacketsMax,
       "tcpv6OosBytes": tcpv6OosBytes,
       "tcpv6OosBytesVal": tcpv6OosBytesVal,
       "tcpv6OosBytesMom": tcpv6OosBytesMom,
       "tcpv6OosBytesMax": tcpv6OosBytesMax,
       "tcpv6Retransmits": tcpv6Retransmits,
       "tcpv6RetransmitsVal": tcpv6RetransmitsVal,
       "tcpv6RetransmitsMom": tcpv6RetransmitsMom,
       "tcpv6RetransmitsMax": tcpv6RetransmitsMax,
       "tcpv6Cwr": tcpv6Cwr,
       "tcpv6CwrVal": tcpv6CwrVal,
       "tcpv6CwrMom": tcpv6CwrMom,
       "tcpv6CwrMax": tcpv6CwrMax,
       "tcpv6Ecne": tcpv6Ecne,
       "tcpv6EcneVal": tcpv6EcneVal,
       "tcpv6EcneMom": tcpv6EcneMom,
       "tcpv6EcneMax": tcpv6EcneMax,
       "tcpv6SimOpen": tcpv6SimOpen,
       "tcpv6SimOpenVal": tcpv6SimOpenVal,
       "tcpv6SimOpenMom": tcpv6SimOpenMom,
       "tcpv6SimOpenMax": tcpv6SimOpenMax,
       "teredo": teredo,
       "teredoPackets": teredoPackets,
       "teredoPacketsVal": teredoPacketsVal,
       "teredoPacketsMom": teredoPacketsMom,
       "teredoPacketsMax": teredoPacketsMax,
       "teredoBytes": teredoBytes,
       "teredoBytesVal": teredoBytesVal,
       "teredoBytesMom": teredoBytesMom,
       "teredoBytesMax": teredoBytesMax,
       "teredoOrgHeaders": teredoOrgHeaders,
       "teredoOrgHeadersVal": teredoOrgHeadersVal,
       "teredoOrgHeadersMom": teredoOrgHeadersMom,
       "teredoOrgHeadersMax": teredoOrgHeadersMax,
       "teredoAuthHeaders": teredoAuthHeaders,
       "teredoAuthHeadersVal": teredoAuthHeadersVal,
       "teredoAuthHeadersMom": teredoAuthHeadersMom,
       "teredoAuthHeadersMax": teredoAuthHeadersMax,
       "teredoFrags": teredoFrags,
       "teredoFragsVal": teredoFragsVal,
       "teredoFragsMom": teredoFragsMom,
       "teredoFragsMax": teredoFragsMax,
       "gtp": gtp,
       "gtpPackets": gtpPackets,
       "gtpPacketsVal": gtpPacketsVal,
       "gtpPacketsMom": gtpPacketsMom,
       "gtpPacketsMax": gtpPacketsMax,
       "gtpBytes": gtpBytes,
       "gtpBytesVal": gtpBytesVal,
       "gtpBytesMom": gtpBytesMom,
       "gtpBytesMax": gtpBytesMax,
       "gtpGpdus": gtpGpdus,
       "gtpGpdusVal": gtpGpdusVal,
       "gtpGpdusMom": gtpGpdusMom,
       "gtpGpdusMax": gtpGpdusMax,
       "gtpCreatePdpReq": gtpCreatePdpReq,
       "gtpCreatePdpReqVal": gtpCreatePdpReqVal,
       "gtpCreatePdpReqMom": gtpCreatePdpReqMom,
       "gtpCreatePdpReqMax": gtpCreatePdpReqMax,
       "gtpCreatePdpRsp": gtpCreatePdpRsp,
       "gtpCreatePdpRspVal": gtpCreatePdpRspVal,
       "gtpCreatePdpRspMom": gtpCreatePdpRspMom,
       "gtpCreatePdpRspMax": gtpCreatePdpRspMax,
       "gtpDeletePdpReq": gtpDeletePdpReq,
       "gtpDeletePdpReqVal": gtpDeletePdpReqVal,
       "gtpDeletePdpReqMom": gtpDeletePdpReqMom,
       "gtpDeletePdpReqMax": gtpDeletePdpReqMax,
       "gtpDeletePdpRsp": gtpDeletePdpRsp,
       "gtpDeletePdpRspVal": gtpDeletePdpRspVal,
       "gtpDeletePdpRspMom": gtpDeletePdpRspMom,
       "gtpDeletePdpRspMax": gtpDeletePdpRspMax,
       "gtpErrorInd": gtpErrorInd,
       "gtpErrorIndVal": gtpErrorIndVal,
       "gtpErrorIndMom": gtpErrorIndMom,
       "gtpErrorIndMax": gtpErrorIndMax,
       "gtpUnknown": gtpUnknown,
       "gtpUnknownVal": gtpUnknownVal,
       "gtpUnknownMom": gtpUnknownMom,
       "gtpUnknownMax": gtpUnknownMax,
       "gtpUpdatePdpReq": gtpUpdatePdpReq,
       "gtpUpdatePdpReqVal": gtpUpdatePdpReqVal,
       "gtpUpdatePdpReqMom": gtpUpdatePdpReqMom,
       "gtpUpdatePdpReqMax": gtpUpdatePdpReqMax,
       "gtpUpdatePdpRsp": gtpUpdatePdpRsp,
       "gtpUpdatePdpRspVal": gtpUpdatePdpRspVal,
       "gtpUpdatePdpRspMom": gtpUpdatePdpRspMom,
       "gtpUpdatePdpRspMax": gtpUpdatePdpRspMax,
       "gtpEchoPdpReq": gtpEchoPdpReq,
       "gtpEchoPdpReqVal": gtpEchoPdpReqVal,
       "gtpEchoPdpReqMom": gtpEchoPdpReqMom,
       "gtpEchoPdpReqMax": gtpEchoPdpReqMax,
       "gtpEchoPdpRsp": gtpEchoPdpRsp,
       "gtpEchoPdpRspVal": gtpEchoPdpRspVal,
       "gtpEchoPdpRspMom": gtpEchoPdpRspMom,
       "gtpEchoPdpRspMax": gtpEchoPdpRspMax,
       "gtpSgsnReq": gtpSgsnReq,
       "gtpSgsnReqVal": gtpSgsnReqVal,
       "gtpSgsnReqMom": gtpSgsnReqMom,
       "gtpSgsnReqMax": gtpSgsnReqMax,
       "gtpSgsnRsp": gtpSgsnRsp,
       "gtpSgsnRspVal": gtpSgsnRspVal,
       "gtpSgsnRspMom": gtpSgsnRspMom,
       "gtpSgsnRspMax": gtpSgsnRspMax,
       "tunnel": tunnel,
       "tunnelGtp": tunnelGtp,
       "tunnelGtpVal": tunnelGtpVal,
       "tunnelGtpMax": tunnelGtpMax,
       "tunnelEsp": tunnelEsp,
       "tunnelEspVal": tunnelEspVal,
       "tunnelEspMax": tunnelEspMax,
       "tunnelTeredo": tunnelTeredo,
       "tunnelTeredoVal": tunnelTeredoVal,
       "tunnelTeredoMax": tunnelTeredoMax,
       "tunnelGre": tunnelGre,
       "tunnelGreVal": tunnelGreVal,
       "tunnelGreMax": tunnelGreMax,
       "tunnelUnknownPkts": tunnelUnknownPkts,
       "tunnelUnknownPktsVal": tunnelUnknownPktsVal,
       "tunnelUnknownPktsMom": tunnelUnknownPktsMom,
       "tunnelUnknownPktsMax": tunnelUnknownPktsMax,
       "tunnelDuplicates": tunnelDuplicates,
       "tunnelDuplicatesVal": tunnelDuplicatesVal,
       "tunnelDuplicatesMom": tunnelDuplicatesMom,
       "tunnelDuplicatesMax": tunnelDuplicatesMax,
       "tunnelGeneric": tunnelGeneric,
       "tunnelGenericVal": tunnelGenericVal,
       "tunnelGenericMax": tunnelGenericMax,
       "tunnelKnownPkts": tunnelKnownPkts,
       "tunnelKnownPktsVal": tunnelKnownPktsVal,
       "tunnelKnownPktsMom": tunnelKnownPktsMom,
       "tunnelKnownPktsMax": tunnelKnownPktsMax,
       "tunnelL2tp": tunnelL2tp,
       "tunnelL2tpVal": tunnelL2tpVal,
       "tunnelL2tpMax": tunnelL2tpMax,
       "gre": gre,
       "grePackets": grePackets,
       "grePacketsVal": grePacketsVal,
       "grePacketsMom": grePacketsMom,
       "grePacketsMax": grePacketsMax,
       "greBytes": greBytes,
       "greBytesVal": greBytesVal,
       "greBytesMom": greBytesMom,
       "greBytesMax": greBytesMax,
       "greUnknownVersion": greUnknownVersion,
       "greUnknownVersionVal": greUnknownVersionVal,
       "greUnknownVersionMom": greUnknownVersionMom,
       "greUnknownVersionMax": greUnknownVersionMax,
       "greShortPackets": greShortPackets,
       "greShortPacketsVal": greShortPacketsVal,
       "greShortPacketsMom": greShortPacketsMom,
       "greShortPacketsMax": greShortPacketsMax,
       "greUnknownType": greUnknownType,
       "greUnknownTypeVal": greUnknownTypeVal,
       "greUnknownTypeMom": greUnknownTypeMom,
       "greUnknownTypeMax": greUnknownTypeMax,
       "greRouteFlag": greRouteFlag,
       "greRouteFlagVal": greRouteFlagVal,
       "greRouteFlagMom": greRouteFlagMom,
       "greRouteFlagMax": greRouteFlagMax,
       "greIpv4Packets": greIpv4Packets,
       "greIpv4PacketsVal": greIpv4PacketsVal,
       "greIpv4PacketsMom": greIpv4PacketsMom,
       "greIpv4PacketsMax": greIpv4PacketsMax,
       "greIpv6Packets": greIpv6Packets,
       "greIpv6PacketsVal": greIpv6PacketsVal,
       "greIpv6PacketsMom": greIpv6PacketsMom,
       "greIpv6PacketsMax": greIpv6PacketsMax,
       "greFfffPackets": greFfffPackets,
       "greFfffPacketsVal": greFfffPacketsVal,
       "greFfffPacketsMom": greFfffPacketsMom,
       "greFfffPacketsMax": greFfffPacketsMax,
       "grePptpPackets": grePptpPackets,
       "grePptpPacketsVal": grePptpPacketsVal,
       "grePptpPacketsMom": grePptpPacketsMom,
       "grePptpPacketsMax": grePptpPacketsMax,
       "grePppPackets": grePppPackets,
       "grePppPacketsVal": grePppPacketsVal,
       "grePppPacketsMom": grePppPacketsMom,
       "grePppPacketsMax": grePppPacketsMax,
       "grePppUnknownPackets": grePppUnknownPackets,
       "grePppUnknownPacketsVal": grePppUnknownPacketsVal,
       "grePppUnknownPacketsMom": grePppUnknownPacketsMom,
       "grePppUnknownPacketsMax": grePppUnknownPacketsMax,
       "l2tp": l2tp,
       "l2tpPackets": l2tpPackets,
       "l2tpPacketsVal": l2tpPacketsVal,
       "l2tpPacketsMom": l2tpPacketsMom,
       "l2tpPacketsMax": l2tpPacketsMax,
       "l2tpBytes": l2tpBytes,
       "l2tpBytesVal": l2tpBytesVal,
       "l2tpBytesMom": l2tpBytesMom,
       "l2tpBytesMax": l2tpBytesMax,
       "l2tpIpv4Packets": l2tpIpv4Packets,
       "l2tpIpv4PacketsVal": l2tpIpv4PacketsVal,
       "l2tpIpv4PacketsMom": l2tpIpv4PacketsMom,
       "l2tpIpv4PacketsMax": l2tpIpv4PacketsMax,
       "l2tpIpv6Packets": l2tpIpv6Packets,
       "l2tpIpv6PacketsVal": l2tpIpv6PacketsVal,
       "l2tpIpv6PacketsMom": l2tpIpv6PacketsMom,
       "l2tpIpv6PacketsMax": l2tpIpv6PacketsMax,
       "l2tplcpPackets": l2tplcpPackets,
       "l2tplcpPacketsVal": l2tplcpPacketsVal,
       "l2tplcpPacketsMom": l2tplcpPacketsMom,
       "l2tplcpPacketsMax": l2tplcpPacketsMax,
       "l2tpcipv4Packets": l2tpcipv4Packets,
       "l2tpcipv4PacketsVal": l2tpcipv4PacketsVal,
       "l2tpcipv4PacketsMom": l2tpcipv4PacketsMom,
       "l2tpcipv4PacketsMax": l2tpcipv4PacketsMax,
       "l2tpcipv6Packets": l2tpcipv6Packets,
       "l2tpcipv6PacketsVal": l2tpcipv6PacketsVal,
       "l2tpcipv6PacketsMom": l2tpcipv6PacketsMom,
       "l2tpcipv6PacketsMax": l2tpcipv6PacketsMax,
       "l2tpchap6Packets": l2tpchap6Packets,
       "l2tpchap6PacketsVal": l2tpchap6PacketsVal,
       "l2tpchap6PacketsMom": l2tpchap6PacketsMom,
       "l2tpchap6PacketsMax": l2tpchap6PacketsMax,
       "system": system,
       "systemCPULoad": systemCPULoad,
       "systemCPULoadVal": systemCPULoadVal,
       "systemCPULoadMax": systemCPULoadMax,
       "systemMemTotal": systemMemTotal,
       "systemMemTotalVal": systemMemTotalVal,
       "systemMemTotalMax": systemMemTotalMax,
       "systemMemFree": systemMemFree,
       "systemMemFreeVal": systemMemFreeVal,
       "systemMemFreeMax": systemMemFreeMax,
       "systemSwapTotal": systemSwapTotal,
       "systemSwapTotalVal": systemSwapTotalVal,
       "systemSwapTotalMax": systemSwapTotalMax,
       "systemSwapFree": systemSwapFree,
       "systemSwapFreeVal": systemSwapFreeVal,
       "systemSwapFreeMax": systemSwapFreeMax,
       "systemUptime": systemUptime,
       "systemUptimeVal": systemUptimeVal,
       "systemHdUsage": systemHdUsage,
       "systemHdUsageVal": systemHdUsageVal,
       "systemHdUsageMax": systemHdUsageMax,
       "systemHdSize": systemHdSize,
       "systemHdSizeVal": systemHdSizeVal,
       "systemHdSizeMax": systemHdSizeMax,
       "liveview": liveview,
       "liveviewUptime": liveviewUptime,
       "liveviewUptimeVal": liveviewUptimeVal,
       "liveviewClients": liveviewClients,
       "liveviewClientsVal": liveviewClientsVal,
       "liveviewClientsMax": liveviewClientsMax,
       "liveviewPLSDClients": liveviewPLSDClients,
       "liveviewPLSDClientsVal": liveviewPLSDClientsVal,
       "liveviewPLSDClientsMax": liveviewPLSDClientsMax,
       "liveviewHosts": liveviewHosts,
       "liveviewHostsVal": liveviewHostsVal,
       "liveviewHostsMax": liveviewHostsMax,
       "liveviewVNOs": liveviewVNOs,
       "liveviewVNOsVal": liveviewVNOsVal,
       "liveviewVNOsMax": liveviewVNOsMax,
       "liveviewActiveVNOs": liveviewActiveVNOs,
       "liveviewActiveVNOsVal": liveviewActiveVNOsVal,
       "liveviewActiveVNOsMax": liveviewActiveVNOsMax,
       "liveviewDrdlRevision": liveviewDrdlRevision,
       "liveviewDrdlRevisionVal": liveviewDrdlRevisionVal,
       "liveviewDrdlRevisionMax": liveviewDrdlRevisionMax,
       "liveviewFailedNetobjects": liveviewFailedNetobjects,
       "liveviewFailedNetobjectsVal": liveviewFailedNetobjectsVal,
       "liveviewFailedNetobjectsMom": liveviewFailedNetobjectsMom,
       "liveviewFailedNetobjectsMax": liveviewFailedNetobjectsMax,
       "liveviewFailedFullNetobjects": liveviewFailedFullNetobjects,
       "liveviewFailedFullNetobjectsVal": liveviewFailedFullNetobjectsVal,
       "liveviewFailedFullNetobjectsMom": liveviewFailedFullNetobjectsMom,
       "liveviewFailedFullNetobjectsMax": liveviewFailedFullNetobjectsMax,
       "liveviewStringCacheUsage": liveviewStringCacheUsage,
       "liveviewStringCacheUsageVal": liveviewStringCacheUsageVal,
       "liveviewStringCacheUsageMax": liveviewStringCacheUsageMax,
       "liveviewUnaccountedPlsdIn": liveviewUnaccountedPlsdIn,
       "liveviewUnaccountedPlsdInVal": liveviewUnaccountedPlsdInVal,
       "liveviewUnaccountedPlsdInMom": liveviewUnaccountedPlsdInMom,
       "liveviewUnaccountedPlsdInMax": liveviewUnaccountedPlsdInMax,
       "liveviewUnaccountedPlsdOut": liveviewUnaccountedPlsdOut,
       "liveviewUnaccountedPlsdOutVal": liveviewUnaccountedPlsdOutVal,
       "liveviewUnaccountedPlsdOutMom": liveviewUnaccountedPlsdOutMom,
       "liveviewUnaccountedPlsdOutMax": liveviewUnaccountedPlsdOutMax,
       "liveviewUnaccountedPlsdFlows": liveviewUnaccountedPlsdFlows,
       "liveviewUnaccountedPlsdFlowsVal": liveviewUnaccountedPlsdFlowsVal,
       "liveviewUnaccountedPlsdFlowsMom": liveviewUnaccountedPlsdFlowsMom,
       "liveviewUnaccountedPlsdFlowsMax": liveviewUnaccountedPlsdFlowsMax,
       "liveviewHostCacheExhausted": liveviewHostCacheExhausted,
       "liveviewHostCacheExhaustedVal": liveviewHostCacheExhaustedVal,
       "liveviewHostCacheExhaustedMom": liveviewHostCacheExhaustedMom,
       "liveviewHostCacheExhaustedMax": liveviewHostCacheExhaustedMax,
       "liveviewPropEntryUsage": liveviewPropEntryUsage,
       "liveviewPropEntryUsageVal": liveviewPropEntryUsageVal,
       "liveviewPropEntryUsageMax": liveviewPropEntryUsageMax,
       "liveviewPropArrayUsage": liveviewPropArrayUsage,
       "liveviewPropArrayUsageVal": liveviewPropArrayUsageVal,
       "liveviewPropArrayUsageMax": liveviewPropArrayUsageMax,
       "liveviewPropUsage": liveviewPropUsage,
       "liveviewPropUsageVal": liveviewPropUsageVal,
       "liveviewPropUsageMax": liveviewPropUsageMax,
       "liveviewTooManyNetobjectsOnHost": liveviewTooManyNetobjectsOnHost,
       "liveviewTooManyNetobjectsOnHostVal": liveviewTooManyNetobjectsOnHostVal,
       "liveviewTooManyNetobjectsOnHostMax": liveviewTooManyNetobjectsOnHostMax,
       "liveviewHostnameAllocs": liveviewHostnameAllocs,
       "liveviewHostnameAllocsVal": liveviewHostnameAllocsVal,
       "liveviewHostnameAllocsMax": liveviewHostnameAllocsMax,
       "liveviewHostnameAllocFail": liveviewHostnameAllocFail,
       "liveviewHostnameAllocFailVal": liveviewHostnameAllocFailVal,
       "liveviewHostnameAllocFailMax": liveviewHostnameAllocFailMax,
       "liveviewReaperRecvBuf": liveviewReaperRecvBuf,
       "liveviewReaperRecvBufVal": liveviewReaperRecvBufVal,
       "liveviewReaperRecvBufMax": liveviewReaperRecvBufMax,
       "liveviewReaperSendBuf": liveviewReaperSendBuf,
       "liveviewReaperSendBufVal": liveviewReaperSendBufVal,
       "liveviewReaperSendBufMax": liveviewReaperSendBufMax,
       "liveviewPLSDBuf": liveviewPLSDBuf,
       "liveviewPLSDBufVal": liveviewPLSDBufVal,
       "liveviewPLSDBufMax": liveviewPLSDBufMax,
       "lb": lb,
       "lbNumFp": lbNumFp,
       "lbNumFpVal": lbNumFpVal,
       "lbNumFpMax": lbNumFpMax,
       "lbActiveFp": lbActiveFp,
       "lbActiveFpVal": lbActiveFpVal,
       "lbActiveFpMax": lbActiveFpMax,
       "lbRunningFp": lbRunningFp,
       "lbRunningFpVal": lbRunningFpVal,
       "lbRunningFpMax": lbRunningFpMax,
       "lbRxPktsInt": lbRxPktsInt,
       "lbRxPktsIntVal": lbRxPktsIntVal,
       "lbRxPktsIntMom": lbRxPktsIntMom,
       "lbRxPktsIntMax": lbRxPktsIntMax,
       "lbRxPktsExt": lbRxPktsExt,
       "lbRxPktsExtVal": lbRxPktsExtVal,
       "lbRxPktsExtMom": lbRxPktsExtMom,
       "lbRxPktsExtMax": lbRxPktsExtMax,
       "lbRxBytesInt": lbRxBytesInt,
       "lbRxBytesIntVal": lbRxBytesIntVal,
       "lbRxBytesIntMom": lbRxBytesIntMom,
       "lbRxBytesIntMax": lbRxBytesIntMax,
       "lbRxBytesExt": lbRxBytesExt,
       "lbRxBytesExtVal": lbRxBytesExtVal,
       "lbRxBytesExtMom": lbRxBytesExtMom,
       "lbRxBytesExtMax": lbRxBytesExtMax,
       "lbRxErrorsInt": lbRxErrorsInt,
       "lbRxErrorsIntVal": lbRxErrorsIntVal,
       "lbRxErrorsIntMom": lbRxErrorsIntMom,
       "lbRxErrorsIntMax": lbRxErrorsIntMax,
       "lbRxErrorsExt": lbRxErrorsExt,
       "lbRxErrorsExtVal": lbRxErrorsExtVal,
       "lbRxErrorsExtMom": lbRxErrorsExtMom,
       "lbRxErrorsExtMax": lbRxErrorsExtMax,
       "lbTxDirectInt": lbTxDirectInt,
       "lbTxDirectIntVal": lbTxDirectIntVal,
       "lbTxDirectIntMom": lbTxDirectIntMom,
       "lbTxDirectIntMax": lbTxDirectIntMax,
       "lbTxDirectExt": lbTxDirectExt,
       "lbTxDirectExtVal": lbTxDirectExtVal,
       "lbTxDirectExtMom": lbTxDirectExtMom,
       "lbTxDirectExtMax": lbTxDirectExtMax,
       "lbTxDropsInt": lbTxDropsInt,
       "lbTxDropsIntVal": lbTxDropsIntVal,
       "lbTxDropsIntMom": lbTxDropsIntMom,
       "lbTxDropsIntMax": lbTxDropsIntMax,
       "lbTxDropsExt": lbTxDropsExt,
       "lbTxDropsExtVal": lbTxDropsExtVal,
       "lbTxDropsExtMom": lbTxDropsExtMom,
       "lbTxDropsExtMax": lbTxDropsExtMax,
       "lbRxFsInvalidVer": lbRxFsInvalidVer,
       "lbRxFsInvalidVerVal": lbRxFsInvalidVerVal,
       "lbRxFsInvalidVerMom": lbRxFsInvalidVerMom,
       "lbRxFsInvalidVerMax": lbRxFsInvalidVerMax,
       "lbShuntPktIpv4AddrInt": lbShuntPktIpv4AddrInt,
       "lbShuntPktIpv4AddrIntVal": lbShuntPktIpv4AddrIntVal,
       "lbShuntPktIpv4AddrIntMom": lbShuntPktIpv4AddrIntMom,
       "lbShuntPktIpv4AddrIntMax": lbShuntPktIpv4AddrIntMax,
       "lbShuntPktIpv4AddrExt": lbShuntPktIpv4AddrExt,
       "lbShuntPktIpv4AddrExtVal": lbShuntPktIpv4AddrExtVal,
       "lbShuntPktIpv4AddrExtMom": lbShuntPktIpv4AddrExtMom,
       "lbShuntPktIpv4AddrExtMax": lbShuntPktIpv4AddrExtMax,
       "lbShuntByteIpv4AddrInt": lbShuntByteIpv4AddrInt,
       "lbShuntByteIpv4AddrIntVal": lbShuntByteIpv4AddrIntVal,
       "lbShuntByteIpv4AddrIntMom": lbShuntByteIpv4AddrIntMom,
       "lbShuntByteIpv4AddrIntMax": lbShuntByteIpv4AddrIntMax,
       "lbShuntByteIpv4AddrExt": lbShuntByteIpv4AddrExt,
       "lbShuntByteIpv4AddrExtVal": lbShuntByteIpv4AddrExtVal,
       "lbShuntByteIpv4AddrExtMom": lbShuntByteIpv4AddrExtMom,
       "lbShuntByteIpv4AddrExtMax": lbShuntByteIpv4AddrExtMax,
       "lbShuntPktIpv4ProtoInt": lbShuntPktIpv4ProtoInt,
       "lbShuntPktIpv4ProtoIntVal": lbShuntPktIpv4ProtoIntVal,
       "lbShuntPktIpv4ProtoIntMom": lbShuntPktIpv4ProtoIntMom,
       "lbShuntPktIpv4ProtoIntMax": lbShuntPktIpv4ProtoIntMax,
       "lbShuntPktIpv4ProtoExt": lbShuntPktIpv4ProtoExt,
       "lbShuntPktIpv4ProtoExtVal": lbShuntPktIpv4ProtoExtVal,
       "lbShuntPktIpv4ProtoExtMom": lbShuntPktIpv4ProtoExtMom,
       "lbShuntPktIpv4ProtoExtMax": lbShuntPktIpv4ProtoExtMax,
       "lbShuntByteIpv4ProtoInt": lbShuntByteIpv4ProtoInt,
       "lbShuntByteIpv4ProtoIntVal": lbShuntByteIpv4ProtoIntVal,
       "lbShuntByteIpv4ProtoIntMom": lbShuntByteIpv4ProtoIntMom,
       "lbShuntByteIpv4ProtoIntMax": lbShuntByteIpv4ProtoIntMax,
       "lbShuntByteIpv4ProtoExt": lbShuntByteIpv4ProtoExt,
       "lbShuntByteIpv4ProtoExtVal": lbShuntByteIpv4ProtoExtVal,
       "lbShuntByteIpv4ProtoExtMom": lbShuntByteIpv4ProtoExtMom,
       "lbShuntByteIpv4ProtoExtMax": lbShuntByteIpv4ProtoExtMax,
       "lbShuntPktEthertypeInt": lbShuntPktEthertypeInt,
       "lbShuntPktEthertypeIntVal": lbShuntPktEthertypeIntVal,
       "lbShuntPktEthertypeIntMom": lbShuntPktEthertypeIntMom,
       "lbShuntPktEthertypeIntMax": lbShuntPktEthertypeIntMax,
       "lbShuntPktEthertypeExt": lbShuntPktEthertypeExt,
       "lbShuntPktEthertypeExtVal": lbShuntPktEthertypeExtVal,
       "lbShuntPktEthertypeExtMom": lbShuntPktEthertypeExtMom,
       "lbShuntPktEthertypeExtMax": lbShuntPktEthertypeExtMax,
       "lbShuntByteEthertypeInt": lbShuntByteEthertypeInt,
       "lbShuntByteEthertypeIntVal": lbShuntByteEthertypeIntVal,
       "lbShuntByteEthertypeIntMom": lbShuntByteEthertypeIntMom,
       "lbShuntByteEthertypeIntMax": lbShuntByteEthertypeIntMax,
       "lbShuntByteEthertypeExt": lbShuntByteEthertypeExt,
       "lbShuntByteEthertypeExtVal": lbShuntByteEthertypeExtVal,
       "lbShuntByteEthertypeExtMom": lbShuntByteEthertypeExtMom,
       "lbShuntByteEthertypeExtMax": lbShuntByteEthertypeExtMax,
       "lbShuntPktDot1qInt": lbShuntPktDot1qInt,
       "lbShuntPktDot1qIntVal": lbShuntPktDot1qIntVal,
       "lbShuntPktDot1qIntMom": lbShuntPktDot1qIntMom,
       "lbShuntPktDot1qIntMax": lbShuntPktDot1qIntMax,
       "lbShuntPktDot1qExt": lbShuntPktDot1qExt,
       "lbShuntPktDot1qExtVal": lbShuntPktDot1qExtVal,
       "lbShuntPktDot1qExtMom": lbShuntPktDot1qExtMom,
       "lbShuntPktDot1qExtMax": lbShuntPktDot1qExtMax,
       "lbShuntByteDot1qInt": lbShuntByteDot1qInt,
       "lbShuntByteDot1qIntVal": lbShuntByteDot1qIntVal,
       "lbShuntByteDot1qIntMom": lbShuntByteDot1qIntMom,
       "lbShuntByteDot1qIntMax": lbShuntByteDot1qIntMax,
       "lbShuntByteDot1qExt": lbShuntByteDot1qExt,
       "lbShuntByteDot1qExtVal": lbShuntByteDot1qExtVal,
       "lbShuntByteDot1qExtMom": lbShuntByteDot1qExtMom,
       "lbShuntByteDot1qExtMax": lbShuntByteDot1qExtMax,
       "lbShuntPktMplsInt": lbShuntPktMplsInt,
       "lbShuntPktMplsIntVal": lbShuntPktMplsIntVal,
       "lbShuntPktMplsIntMom": lbShuntPktMplsIntMom,
       "lbShuntPktMplsIntMax": lbShuntPktMplsIntMax,
       "lbShuntPktMplsExt": lbShuntPktMplsExt,
       "lbShuntPktMplsExtVal": lbShuntPktMplsExtVal,
       "lbShuntPktMplsExtMom": lbShuntPktMplsExtMom,
       "lbShuntPktMplsExtMax": lbShuntPktMplsExtMax,
       "lbShuntByteMplsInt": lbShuntByteMplsInt,
       "lbShuntByteMplsIntVal": lbShuntByteMplsIntVal,
       "lbShuntByteMplsIntMom": lbShuntByteMplsIntMom,
       "lbShuntByteMplsIntMax": lbShuntByteMplsIntMax,
       "lbShuntByteMplsExt": lbShuntByteMplsExt,
       "lbShuntByteMplsExtVal": lbShuntByteMplsExtVal,
       "lbShuntByteMplsExtMom": lbShuntByteMplsExtMom,
       "lbShuntByteMplsExtMax": lbShuntByteMplsExtMax,
       "lbShuntPktEomplsInt": lbShuntPktEomplsInt,
       "lbShuntPktEomplsIntVal": lbShuntPktEomplsIntVal,
       "lbShuntPktEomplsIntMom": lbShuntPktEomplsIntMom,
       "lbShuntPktEomplsIntMax": lbShuntPktEomplsIntMax,
       "lbShuntPktEomplsExt": lbShuntPktEomplsExt,
       "lbShuntPktEomplsExtVal": lbShuntPktEomplsExtVal,
       "lbShuntPktEomplsExtMom": lbShuntPktEomplsExtMom,
       "lbShuntPktEomplsExtMax": lbShuntPktEomplsExtMax,
       "lbShuntByteEomplsInt": lbShuntByteEomplsInt,
       "lbShuntByteEomplsIntVal": lbShuntByteEomplsIntVal,
       "lbShuntByteEomplsIntMom": lbShuntByteEomplsIntMom,
       "lbShuntByteEomplsIntMax": lbShuntByteEomplsIntMax,
       "lbShuntByteEomplsExt": lbShuntByteEomplsExt,
       "lbShuntByteEomplsExtVal": lbShuntByteEomplsExtVal,
       "lbShuntByteEomplsExtMom": lbShuntByteEomplsExtMom,
       "lbShuntByteEomplsExtMax": lbShuntByteEomplsExtMax,
       "lbLbUptime": lbLbUptime,
       "lbLbUptimeVal": lbLbUptimeVal,
       "lbCpuLoad": lbCpuLoad,
       "lbCpuLoadVal": lbCpuLoadVal,
       "lbCpuLoadMax": lbCpuLoadMax,
       "lbShuntPktIpv6AddrInt": lbShuntPktIpv6AddrInt,
       "lbShuntPktIpv6AddrIntVal": lbShuntPktIpv6AddrIntVal,
       "lbShuntPktIpv6AddrIntMom": lbShuntPktIpv6AddrIntMom,
       "lbShuntPktIpv6AddrIntMax": lbShuntPktIpv6AddrIntMax,
       "lbShuntPktIpv6AddrExt": lbShuntPktIpv6AddrExt,
       "lbShuntPktIpv6AddrExtVal": lbShuntPktIpv6AddrExtVal,
       "lbShuntPktIpv6AddrExtMom": lbShuntPktIpv6AddrExtMom,
       "lbShuntPktIpv6AddrExtMax": lbShuntPktIpv6AddrExtMax,
       "lbShuntByteIpv6AddrInt": lbShuntByteIpv6AddrInt,
       "lbShuntByteIpv6AddrIntVal": lbShuntByteIpv6AddrIntVal,
       "lbShuntByteIpv6AddrIntMom": lbShuntByteIpv6AddrIntMom,
       "lbShuntByteIpv6AddrIntMax": lbShuntByteIpv6AddrIntMax,
       "lbShuntByteIpv6AddrExt": lbShuntByteIpv6AddrExt,
       "lbShuntByteIpv6AddrExtVal": lbShuntByteIpv6AddrExtVal,
       "lbShuntByteIpv6AddrExtMom": lbShuntByteIpv6AddrExtMom,
       "lbShuntByteIpv6AddrExtMax": lbShuntByteIpv6AddrExtMax,
       "lbLogicalFp": lbLogicalFp,
       "lbLogicalFpVal": lbLogicalFpVal,
       "lbLogicalFpMax": lbLogicalFpMax,
       "lbTxFs": lbTxFs,
       "lbTxFsVal": lbTxFsVal,
       "lbTxFsMom": lbTxFsMom,
       "lbTxFsMax": lbTxFsMax,
       "lbTxFpInt": lbTxFpInt,
       "lbTxFpIntVal": lbTxFpIntVal,
       "lbTxFpIntMom": lbTxFpIntMom,
       "lbTxFpIntMax": lbTxFpIntMax,
       "lbTxFpExt": lbTxFpExt,
       "lbTxFpExtVal": lbTxFpExtVal,
       "lbTxFpExtMom": lbTxFpExtMom,
       "lbTxFpExtMax": lbTxFpExtMax,
       "lbHbLost": lbHbLost,
       "lbHbLostVal": lbHbLostVal,
       "lbHbLostMom": lbHbLostMom,
       "lbHbLostMax": lbHbLostMax,
       "lbBucketMoves": lbBucketMoves,
       "lbBucketMovesVal": lbBucketMovesVal,
       "lbBucketMovesMom": lbBucketMovesMom,
       "lbBucketMovesMax": lbBucketMovesMax,
       "lbBlacklistedBuckets": lbBlacklistedBuckets,
       "lbBlacklistedBucketsVal": lbBlacklistedBucketsVal,
       "lbBlacklistedBucketsMax": lbBlacklistedBucketsMax,
       "lbBlacklistedPackets": lbBlacklistedPackets,
       "lbBlacklistedPacketsVal": lbBlacklistedPacketsVal,
       "lbBlacklistedPacketsMom": lbBlacklistedPacketsMom,
       "lbBlacklistedPacketsMax": lbBlacklistedPacketsMax,
       "plsd": plsd,
       "plsdDumptime": plsdDumptime,
       "plsdDumptimeVal": plsdDumptimeVal,
       "plsdValuesDataset": plsdValuesDataset,
       "plsdValuesDatasetVal": plsdValuesDatasetVal,
       "plsdValuesDatasetMax": plsdValuesDatasetMax,
       "plsdValuesDelayedExpand": plsdValuesDelayedExpand,
       "plsdValuesDelayedExpandVal": plsdValuesDelayedExpandVal,
       "plsdValuesDelayedExpandMax": plsdValuesDelayedExpandMax,
       "plsdLinksDataset": plsdLinksDataset,
       "plsdLinksDatasetVal": plsdLinksDatasetVal,
       "plsdLinksDatasetMax": plsdLinksDatasetMax,
       "plsdValuesAggrDataset": plsdValuesAggrDataset,
       "plsdValuesAggrDatasetVal": plsdValuesAggrDatasetVal,
       "plsdValuesAggrDatasetMax": plsdValuesAggrDatasetMax,
       "plsdValueReject": plsdValueReject,
       "plsdValueRejectVal": plsdValueRejectVal,
       "plsdValueRejectMom": plsdValueRejectMom,
       "plsdValueRejectMax": plsdValueRejectMax,
       "plsdValueRejectPrior": plsdValueRejectPrior,
       "plsdValueRejectPriorVal": plsdValueRejectPriorVal,
       "plsdValueRejectPriorMom": plsdValueRejectPriorMom,
       "plsdValueRejectPriorMax": plsdValueRejectPriorMax,
       "plsdValuesFiltered": plsdValuesFiltered,
       "plsdValuesFilteredVal": plsdValuesFilteredVal,
       "plsdValuesFilteredMax": plsdValuesFilteredMax,
       "plsdValuesSent": plsdValuesSent,
       "plsdValuesSentVal": plsdValuesSentVal,
       "plsdValuesSentMax": plsdValuesSentMax,
       "plsdValueLookups": plsdValueLookups,
       "plsdValueLookupsVal": plsdValueLookupsVal,
       "plsdValueLookupsMom": plsdValueLookupsMom,
       "plsdValueLookupsMax": plsdValueLookupsMax,
       "plsdValueUpdatesBytes": plsdValueUpdatesBytes,
       "plsdValueUpdatesBytesVal": plsdValueUpdatesBytesVal,
       "plsdValueUpdatesBytesMom": plsdValueUpdatesBytesMom,
       "plsdValueUpdatesBytesMax": plsdValueUpdatesBytesMax,
       "plsdValueUpdatesBytesHp": plsdValueUpdatesBytesHp,
       "plsdValueUpdatesBytesHpVal": plsdValueUpdatesBytesHpVal,
       "plsdValueUpdatesBytesHpMom": plsdValueUpdatesBytesHpMom,
       "plsdValueUpdatesBytesHpMax": plsdValueUpdatesBytesHpMax,
       "plsdValueUpdatesConns": plsdValueUpdatesConns,
       "plsdValueUpdatesConnsVal": plsdValueUpdatesConnsVal,
       "plsdValueUpdatesConnsMom": plsdValueUpdatesConnsMom,
       "plsdValueUpdatesConnsMax": plsdValueUpdatesConnsMax,
       "plsdValueUpdatesConnsHp": plsdValueUpdatesConnsHp,
       "plsdValueUpdatesConnsHpVal": plsdValueUpdatesConnsHpVal,
       "plsdValueUpdatesConnsHpMom": plsdValueUpdatesConnsHpMom,
       "plsdValueUpdatesConnsHpMax": plsdValueUpdatesConnsHpMax,
       "plsdConnections": plsdConnections,
       "plsdConnectionsVal": plsdConnectionsVal,
       "plsdConnectionsMax": plsdConnectionsMax,
       "plsdHosts": plsdHosts,
       "plsdHostsVal": plsdHostsVal,
       "plsdHostsMax": plsdHostsMax,
       "plsdConnUpdates": plsdConnUpdates,
       "plsdConnUpdatesVal": plsdConnUpdatesVal,
       "plsdConnUpdatesMom": plsdConnUpdatesMom,
       "plsdConnUpdatesMax": plsdConnUpdatesMax,
       "plsdConnUpdatesFull": plsdConnUpdatesFull,
       "plsdConnUpdatesFullVal": plsdConnUpdatesFullVal,
       "plsdConnUpdatesFullMom": plsdConnUpdatesFullMom,
       "plsdConnUpdatesFullMax": plsdConnUpdatesFullMax,
       "plsdConnUpdatesNew": plsdConnUpdatesNew,
       "plsdConnUpdatesNewVal": plsdConnUpdatesNewVal,
       "plsdConnUpdatesNewMom": plsdConnUpdatesNewMom,
       "plsdConnUpdatesNewMax": plsdConnUpdatesNewMax,
       "plsdConnUpdatesFiltered": plsdConnUpdatesFiltered,
       "plsdConnUpdatesFilteredVal": plsdConnUpdatesFilteredVal,
       "plsdConnUpdatesFilteredMom": plsdConnUpdatesFilteredMom,
       "plsdConnUpdatesFilteredMax": plsdConnUpdatesFilteredMax,
       "plsdConnsDropped": plsdConnsDropped,
       "plsdConnsDroppedVal": plsdConnsDroppedVal,
       "plsdConnsDroppedMom": plsdConnsDroppedMom,
       "plsdConnsDroppedMax": plsdConnsDroppedMax,
       "plsdConnlogConns": plsdConnlogConns,
       "plsdConnlogConnsVal": plsdConnlogConnsVal,
       "plsdConnlogConnsMax": plsdConnlogConnsMax,
       "plsdConnlogConnsAdded": plsdConnlogConnsAdded,
       "plsdConnlogConnsAddedVal": plsdConnlogConnsAddedVal,
       "plsdConnlogConnsAddedMom": plsdConnlogConnsAddedMom,
       "plsdConnlogConnsAddedMax": plsdConnlogConnsAddedMax,
       "plsdConnlogDumptimeRemaining": plsdConnlogDumptimeRemaining,
       "plsdConnlogDumptimeRemainingVal": plsdConnlogDumptimeRemainingVal,
       "plsdConnlogConnsDumped": plsdConnlogConnsDumped,
       "plsdConnlogConnsDumpedVal": plsdConnlogConnsDumpedVal,
       "plsdConnlogConnsDumpedMax": plsdConnlogConnsDumpedMax,
       "plsdConnlogDumptime": plsdConnlogDumptime,
       "plsdConnlogDumptimeVal": plsdConnlogDumptimeVal,
       "plsdLastdump": plsdLastdump,
       "plsdLastdumpVal": plsdLastdumpVal,
       "plsdRingbufUsage": plsdRingbufUsage,
       "plsdRingbufUsageVal": plsdRingbufUsageVal,
       "plsdRingbufUsageMax": plsdRingbufUsageMax,
       "plsdConnlogDrops": plsdConnlogDrops,
       "plsdConnlogDropsVal": plsdConnlogDropsVal,
       "plsdConnlogDropsMax": plsdConnlogDropsMax,
       "plsdBwUsed": plsdBwUsed,
       "plsdBwUsedVal": plsdBwUsedVal,
       "plsdBwUsedMom": plsdBwUsedMom,
       "plsdBwUsedMax": plsdBwUsedMax,
       "plsdTimeConnected": plsdTimeConnected,
       "plsdTimeConnectedVal": plsdTimeConnectedVal,
       "plsdConnects": plsdConnects,
       "plsdConnectsVal": plsdConnectsVal,
       "plsdConnectsMax": plsdConnectsMax,
       "plsdVmsize": plsdVmsize,
       "plsdVmsizeVal": plsdVmsizeVal,
       "plsdVmsizeMax": plsdVmsizeMax,
       "plsdVmrss": plsdVmrss,
       "plsdVmrssVal": plsdVmrssVal,
       "plsdVmrssMax": plsdVmrssMax,
       "plsdConnlogIncomplete": plsdConnlogIncomplete,
       "plsdConnlogIncompleteVal": plsdConnlogIncompleteVal,
       "plsdConnlogIncompleteMax": plsdConnlogIncompleteMax,
       "plsdConnProp": plsdConnProp,
       "plsdConnPropVal": plsdConnPropVal,
       "plsdConnPropMax": plsdConnPropMax,
       "plsdConnPropHash": plsdConnPropHash,
       "plsdConnPropHashVal": plsdConnPropHashVal,
       "plsdConnPropHashMax": plsdConnPropHashMax,
       "plsw": plsw,
       "plswDatasetStart": plswDatasetStart,
       "plswDatasetStartVal": plswDatasetStartVal,
       "plswDatasetEnd": plswDatasetEnd,
       "plswDatasetEndVal": plswDatasetEndVal,
       "plswSessions": plswSessions,
       "plswSessionsVal": plswSessionsVal,
       "plswSessionsMax": plswSessionsMax,
       "plswValues": plswValues,
       "plswValuesVal": plswValuesVal,
       "plswValuesMax": plswValuesMax,
       "plswValuesDropped1": plswValuesDropped1,
       "plswValuesDropped1Val": plswValuesDropped1Val,
       "plswValuesDropped1Max": plswValuesDropped1Max,
       "plswValuesDropped2": plswValuesDropped2,
       "plswValuesDropped2Val": plswValuesDropped2Val,
       "plswValuesDropped2Max": plswValuesDropped2Max,
       "plswValuesDropped3": plswValuesDropped3,
       "plswValuesDropped3Val": plswValuesDropped3Val,
       "plswValuesDropped3Max": plswValuesDropped3Max,
       "plswValuesDropped4": plswValuesDropped4,
       "plswValuesDropped4Val": plswValuesDropped4Val,
       "plswValuesDropped4Max": plswValuesDropped4Max,
       "plswNewglobal": plswNewglobal,
       "plswNewglobalVal": plswNewglobalVal,
       "plswNewglobalMax": plswNewglobalMax,
       "plswNewcoll": plswNewcoll,
       "plswNewcollVal": plswNewcollVal,
       "plswNewcollMax": plswNewcollMax,
       "plswNewdaily": plswNewdaily,
       "plswNewdailyVal": plswNewdailyVal,
       "plswNewdailyMax": plswNewdailyMax,
       "plswTupdate": plswTupdate,
       "plswTupdateVal": plswTupdateVal,
       "plswTupdateMax": plswTupdateMax,
       "plswGupdate": plswGupdate,
       "plswGupdateVal": plswGupdateVal,
       "plswGupdateMax": plswGupdateMax,
       "plswTimeDataset": plswTimeDataset,
       "plswTimeDatasetVal": plswTimeDatasetVal,
       "plswTimeGlobal": plswTimeGlobal,
       "plswTimeGlobalVal": plswTimeGlobalVal,
       "plswTimeDaily": plswTimeDaily,
       "plswTimeDailyVal": plswTimeDailyVal,
       "plswTimeTotal": plswTimeTotal,
       "plswTimeTotalVal": plswTimeTotalVal,
       "plswTimeGraph": plswTimeGraph,
       "plswTimeGraphVal": plswTimeGraphVal,
       "plswGlobals": plswGlobals,
       "plswGlobalsVal": plswGlobalsVal,
       "plswGlobalsMax": plswGlobalsMax,
       "plswColls": plswColls,
       "plswCollsVal": plswCollsVal,
       "plswCollsMax": plswCollsMax,
       "plswDailys": plswDailys,
       "plswDailysVal": plswDailysVal,
       "plswDailysMax": plswDailysMax,
       "plswBlocks": plswBlocks,
       "plswBlocksVal": plswBlocksVal,
       "plswBlocksMax": plswBlocksMax,
       "plswGraphs": plswGraphs,
       "plswGraphsVal": plswGraphsVal,
       "plswGraphsMax": plswGraphsMax,
       "plswSysdiagHdUsage": plswSysdiagHdUsage,
       "plswSysdiagHdUsageVal": plswSysdiagHdUsageVal,
       "plswSysdiagHdUsageMax": plswSysdiagHdUsageMax,
       "plswSysdiagHdSize": plswSysdiagHdSize,
       "plswSysdiagHdSizeVal": plswSysdiagHdSizeVal,
       "plswSysdiagHdSizeMax": plswSysdiagHdSizeMax,
       "plswSystemHdUsage": plswSystemHdUsage,
       "plswSystemHdUsageVal": plswSystemHdUsageVal,
       "plswSystemHdUsageMax": plswSystemHdUsageMax,
       "plswSystemHdSize": plswSystemHdSize,
       "plswSystemHdSizeVal": plswSystemHdSizeVal,
       "plswSystemHdSizeMax": plswSystemHdSizeMax,
       "plswSysdiagDaySize": plswSysdiagDaySize,
       "plswSysdiagDaySizeVal": plswSysdiagDaySizeVal,
       "plswSysdiagDaySizeMax": plswSysdiagDaySizeMax,
       "plswMemused": plswMemused,
       "plswMemusedVal": plswMemusedVal,
       "plswMemusedMax": plswMemusedMax,
       "rulesetCompiler": rulesetCompiler,
       "rulesetCompilerReaperRecvBuf": rulesetCompilerReaperRecvBuf,
       "rulesetCompilerReaperRecvBufVal": rulesetCompilerReaperRecvBufVal,
       "rulesetCompilerReaperRecvBufMax": rulesetCompilerReaperRecvBufMax,
       "rulesetCompilerReaperSendBuf": rulesetCompilerReaperSendBuf,
       "rulesetCompilerReaperSendBufVal": rulesetCompilerReaperSendBufVal,
       "rulesetCompilerReaperSendBufMax": rulesetCompilerReaperSendBufMax,
       "ipfix": ipfix,
       "ipfixConnections": ipfixConnections,
       "ipfixConnectionsVal": ipfixConnectionsVal,
       "ipfixConnectionsMax": ipfixConnectionsMax,
       "ipfixConnUpdates": ipfixConnUpdates,
       "ipfixConnUpdatesVal": ipfixConnUpdatesVal,
       "ipfixConnUpdatesMom": ipfixConnUpdatesMom,
       "ipfixConnUpdatesMax": ipfixConnUpdatesMax,
       "ipfixExportedIpv4Records": ipfixExportedIpv4Records,
       "ipfixExportedIpv4RecordsVal": ipfixExportedIpv4RecordsVal,
       "ipfixExportedIpv4RecordsMom": ipfixExportedIpv4RecordsMom,
       "ipfixExportedIpv4RecordsMax": ipfixExportedIpv4RecordsMax,
       "ipfixExportedIpv6Records": ipfixExportedIpv6Records,
       "ipfixExportedIpv6RecordsVal": ipfixExportedIpv6RecordsVal,
       "ipfixExportedIpv6RecordsMom": ipfixExportedIpv6RecordsMom,
       "ipfixExportedIpv6RecordsMax": ipfixExportedIpv6RecordsMax,
       "ipfixExportedIpv4Sets": ipfixExportedIpv4Sets,
       "ipfixExportedIpv4SetsVal": ipfixExportedIpv4SetsVal,
       "ipfixExportedIpv4SetsMom": ipfixExportedIpv4SetsMom,
       "ipfixExportedIpv4SetsMax": ipfixExportedIpv4SetsMax,
       "ipfixExportedIpv6Sets": ipfixExportedIpv6Sets,
       "ipfixExportedIpv6SetsVal": ipfixExportedIpv6SetsVal,
       "ipfixExportedIpv6SetsMom": ipfixExportedIpv6SetsMom,
       "ipfixExportedIpv6SetsMax": ipfixExportedIpv6SetsMax,
       "ipfixExportedMsgs": ipfixExportedMsgs,
       "ipfixExportedMsgsVal": ipfixExportedMsgsVal,
       "ipfixExportedMsgsMom": ipfixExportedMsgsMom,
       "ipfixExportedMsgsMax": ipfixExportedMsgsMax,
       "channelstats": channelstats,
       "pl2Trap": pl2Trap,
       "snoopers": snoopers,
       "dynamiczones": dynamiczones,
       "psm": psm,
       "pbs": pbs}
)
