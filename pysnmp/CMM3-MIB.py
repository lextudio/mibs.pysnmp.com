# SNMP MIB module (CMM3-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CMM3-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:15:51 2024
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

(whispBox,
 whispCMM,
 whispModules) = mibBuilder.importSymbols(
    "WHISP-GLOBAL-REG-MIB",
    "whispBox",
    "whispCMM",
    "whispModules")

(EventString,
 WhispLUID,
 WhispMACAddress) = mibBuilder.importSymbols(
    "WHISP-TC-MIB",
    "EventString",
    "WhispLUID",
    "WhispMACAddress")


# MODULE-IDENTITY

cmmIIIMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 1, 1, 15)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CmmGroups_ObjectIdentity = ObjectIdentity
cmmGroups = _CmmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 1)
)
_CmmSwitch_ObjectIdentity = ObjectIdentity
cmmSwitch = _CmmSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 2)
)
_CmmSwitchTable_Object = MibTable
cmmSwitchTable = _CmmSwitchTable_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 2, 1)
)
if mibBuilder.loadTexts:
    cmmSwitchTable.setStatus("current")
_CmmSwitchEntry_Object = MibTableRow
cmmSwitchEntry = _CmmSwitchEntry_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 2, 1, 1)
)
cmmSwitchEntry.setIndexNames(
    (0, "CMM3-MIB", "portNumber"),
)
if mibBuilder.loadTexts:
    cmmSwitchEntry.setStatus("current")


class _PortNumber_Type(Integer32):
    """Custom type portNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PortNumber_Type.__name__ = "Integer32"
_PortNumber_Object = MibTableColumn
portNumber = _PortNumber_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 2, 1, 1, 1),
    _PortNumber_Type()
)
portNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portNumber.setStatus("current")
_RxDropPkts_Type = Counter32
_RxDropPkts_Object = MibTableColumn
rxDropPkts = _RxDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 2, 1, 1, 2),
    _RxDropPkts_Type()
)
rxDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxDropPkts.setStatus("current")
_RxOctets_Type = Counter64
_RxOctets_Object = MibTableColumn
rxOctets = _RxOctets_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 2, 1, 1, 3),
    _RxOctets_Type()
)
rxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxOctets.setStatus("current")
_RxBroadcastPkts_Type = Counter32
_RxBroadcastPkts_Object = MibTableColumn
rxBroadcastPkts = _RxBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 2, 1, 1, 4),
    _RxBroadcastPkts_Type()
)
rxBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxBroadcastPkts.setStatus("current")
_RxMulticastPkts_Type = Counter32
_RxMulticastPkts_Object = MibTableColumn
rxMulticastPkts = _RxMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 2, 1, 1, 5),
    _RxMulticastPkts_Type()
)
rxMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxMulticastPkts.setStatus("current")
_RxSAChanges_Type = Counter32
_RxSAChanges_Object = MibTableColumn
rxSAChanges = _RxSAChanges_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 2, 1, 1, 6),
    _RxSAChanges_Type()
)
rxSAChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxSAChanges.setStatus("current")
_RxUndersizePkts_Type = Counter32
_RxUndersizePkts_Object = MibTableColumn
rxUndersizePkts = _RxUndersizePkts_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 2, 1, 1, 7),
    _RxUndersizePkts_Type()
)
rxUndersizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxUndersizePkts.setStatus("current")
_RxOversizePkts_Type = Counter32
_RxOversizePkts_Object = MibTableColumn
rxOversizePkts = _RxOversizePkts_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 2, 1, 1, 8),
    _RxOversizePkts_Type()
)
rxOversizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxOversizePkts.setStatus("current")
_RxFragments_Type = Counter32
_RxFragments_Object = MibTableColumn
rxFragments = _RxFragments_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 2, 1, 1, 9),
    _RxFragments_Type()
)
rxFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxFragments.setStatus("current")
_RxJabbers_Type = Counter32
_RxJabbers_Object = MibTableColumn
rxJabbers = _RxJabbers_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 2, 1, 1, 10),
    _RxJabbers_Type()
)
rxJabbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxJabbers.setStatus("current")
_RxUnicastPkts_Type = Counter32
_RxUnicastPkts_Object = MibTableColumn
rxUnicastPkts = _RxUnicastPkts_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 2, 1, 1, 11),
    _RxUnicastPkts_Type()
)
rxUnicastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxUnicastPkts.setStatus("current")
_RxAlignmentErrors_Type = Counter32
_RxAlignmentErrors_Object = MibTableColumn
rxAlignmentErrors = _RxAlignmentErrors_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 2, 1, 1, 12),
    _RxAlignmentErrors_Type()
)
rxAlignmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxAlignmentErrors.setStatus("current")
_RxFCSErrors_Type = Counter32
_RxFCSErrors_Object = MibTableColumn
rxFCSErrors = _RxFCSErrors_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 2, 1, 1, 13),
    _RxFCSErrors_Type()
)
rxFCSErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxFCSErrors.setStatus("current")
_RxGoodOctets_Type = Counter64
_RxGoodOctets_Object = MibTableColumn
rxGoodOctets = _RxGoodOctets_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 2, 1, 1, 14),
    _RxGoodOctets_Type()
)
rxGoodOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxGoodOctets.setStatus("current")
_RxExcessSizeDisc_Type = Counter32
_RxExcessSizeDisc_Object = MibTableColumn
rxExcessSizeDisc = _RxExcessSizeDisc_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 2, 1, 1, 15),
    _RxExcessSizeDisc_Type()
)
rxExcessSizeDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxExcessSizeDisc.setStatus("current")
_RxPausePkts_Type = Counter32
_RxPausePkts_Object = MibTableColumn
rxPausePkts = _RxPausePkts_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 2, 1, 1, 16),
    _RxPausePkts_Type()
)
rxPausePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxPausePkts.setStatus("current")
_RxSymbolErrors_Type = Counter32
_RxSymbolErrors_Object = MibTableColumn
rxSymbolErrors = _RxSymbolErrors_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 2, 1, 1, 17),
    _RxSymbolErrors_Type()
)
rxSymbolErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxSymbolErrors.setStatus("current")
_TxDropPkts_Type = Counter32
_TxDropPkts_Object = MibTableColumn
txDropPkts = _TxDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 2, 1, 1, 18),
    _TxDropPkts_Type()
)
txDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txDropPkts.setStatus("current")
_TxOctets_Type = Counter64
_TxOctets_Object = MibTableColumn
txOctets = _TxOctets_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 2, 1, 1, 19),
    _TxOctets_Type()
)
txOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txOctets.setStatus("current")
_TxBroadcastPkts_Type = Counter32
_TxBroadcastPkts_Object = MibTableColumn
txBroadcastPkts = _TxBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 2, 1, 1, 20),
    _TxBroadcastPkts_Type()
)
txBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txBroadcastPkts.setStatus("current")
_TxMulticastPkts_Type = Counter32
_TxMulticastPkts_Object = MibTableColumn
txMulticastPkts = _TxMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 2, 1, 1, 21),
    _TxMulticastPkts_Type()
)
txMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txMulticastPkts.setStatus("current")
_TxCollisions_Type = Counter32
_TxCollisions_Object = MibTableColumn
txCollisions = _TxCollisions_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 2, 1, 1, 22),
    _TxCollisions_Type()
)
txCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txCollisions.setStatus("current")
_TxUnicastPkts_Type = Counter32
_TxUnicastPkts_Object = MibTableColumn
txUnicastPkts = _TxUnicastPkts_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 2, 1, 1, 23),
    _TxUnicastPkts_Type()
)
txUnicastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txUnicastPkts.setStatus("current")
_TxSingleCollision_Type = Counter32
_TxSingleCollision_Object = MibTableColumn
txSingleCollision = _TxSingleCollision_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 2, 1, 1, 24),
    _TxSingleCollision_Type()
)
txSingleCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txSingleCollision.setStatus("current")
_TxMultipleCollision_Type = Counter32
_TxMultipleCollision_Object = MibTableColumn
txMultipleCollision = _TxMultipleCollision_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 2, 1, 1, 25),
    _TxMultipleCollision_Type()
)
txMultipleCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txMultipleCollision.setStatus("current")
_TxDeferredTransmit_Type = Counter32
_TxDeferredTransmit_Object = MibTableColumn
txDeferredTransmit = _TxDeferredTransmit_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 2, 1, 1, 26),
    _TxDeferredTransmit_Type()
)
txDeferredTransmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txDeferredTransmit.setStatus("current")
_TxLateCollision_Type = Counter32
_TxLateCollision_Object = MibTableColumn
txLateCollision = _TxLateCollision_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 2, 1, 1, 27),
    _TxLateCollision_Type()
)
txLateCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txLateCollision.setStatus("current")
_TxExcessiveCollision_Type = Counter32
_TxExcessiveCollision_Object = MibTableColumn
txExcessiveCollision = _TxExcessiveCollision_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 2, 1, 1, 28),
    _TxExcessiveCollision_Type()
)
txExcessiveCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txExcessiveCollision.setStatus("current")
_TxPausePkts_Type = Counter32
_TxPausePkts_Object = MibTableColumn
txPausePkts = _TxPausePkts_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 2, 1, 1, 29),
    _TxPausePkts_Type()
)
txPausePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txPausePkts.setStatus("current")
_TxFrameInDisc_Type = Counter32
_TxFrameInDisc_Object = MibTableColumn
txFrameInDisc = _TxFrameInDisc_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 2, 1, 1, 30),
    _TxFrameInDisc_Type()
)
txFrameInDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txFrameInDisc.setStatus("current")
_Pkts64Octets_Type = Counter32
_Pkts64Octets_Object = MibTableColumn
pkts64Octets = _Pkts64Octets_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 2, 1, 1, 31),
    _Pkts64Octets_Type()
)
pkts64Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pkts64Octets.setStatus("current")
_Pkts65to127Octets_Type = Counter32
_Pkts65to127Octets_Object = MibTableColumn
pkts65to127Octets = _Pkts65to127Octets_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 2, 1, 1, 32),
    _Pkts65to127Octets_Type()
)
pkts65to127Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pkts65to127Octets.setStatus("current")
_Pkts128to255Octets_Type = Counter32
_Pkts128to255Octets_Object = MibTableColumn
pkts128to255Octets = _Pkts128to255Octets_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 2, 1, 1, 33),
    _Pkts128to255Octets_Type()
)
pkts128to255Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pkts128to255Octets.setStatus("current")
_Pkts256to511Octets_Type = Counter32
_Pkts256to511Octets_Object = MibTableColumn
pkts256to511Octets = _Pkts256to511Octets_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 2, 1, 1, 34),
    _Pkts256to511Octets_Type()
)
pkts256to511Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pkts256to511Octets.setStatus("current")
_Pkts512to1023Octets_Type = Counter32
_Pkts512to1023Octets_Object = MibTableColumn
pkts512to1023Octets = _Pkts512to1023Octets_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 2, 1, 1, 35),
    _Pkts512to1023Octets_Type()
)
pkts512to1023Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pkts512to1023Octets.setStatus("current")
_Pkts1024to1522Octets_Type = Counter32
_Pkts1024to1522Octets_Object = MibTableColumn
pkts1024to1522Octets = _Pkts1024to1522Octets_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 2, 1, 1, 36),
    _Pkts1024to1522Octets_Type()
)
pkts1024to1522Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pkts1024to1522Octets.setStatus("current")
_CmmConfig_ObjectIdentity = ObjectIdentity
cmmConfig = _CmmConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3)
)


class _GpsTimingPulse_Type(Integer32):
    """Custom type gpsTimingPulse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("master", 1),
          ("slave", 0))
    )


_GpsTimingPulse_Type.__name__ = "Integer32"
_GpsTimingPulse_Object = MibScalar
gpsTimingPulse = _GpsTimingPulse_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 1),
    _GpsTimingPulse_Type()
)
gpsTimingPulse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gpsTimingPulse.setStatus("current")
_Lan1Ip_Type = IpAddress
_Lan1Ip_Object = MibScalar
lan1Ip = _Lan1Ip_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 2),
    _Lan1Ip_Type()
)
lan1Ip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lan1Ip.setStatus("current")
_Lan1SubnetMask_Type = IpAddress
_Lan1SubnetMask_Object = MibScalar
lan1SubnetMask = _Lan1SubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 3),
    _Lan1SubnetMask_Type()
)
lan1SubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lan1SubnetMask.setStatus("current")
_DefaultGateWay_Type = IpAddress
_DefaultGateWay_Object = MibScalar
defaultGateWay = _DefaultGateWay_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 4),
    _DefaultGateWay_Type()
)
defaultGateWay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultGateWay.setStatus("current")


class _Port1PowerCtr_Type(Integer32):
    """Custom type port1PowerCtr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Port1PowerCtr_Type.__name__ = "Integer32"
_Port1PowerCtr_Object = MibScalar
port1PowerCtr = _Port1PowerCtr_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 5),
    _Port1PowerCtr_Type()
)
port1PowerCtr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port1PowerCtr.setStatus("current")


class _Port2PowerCtr_Type(Integer32):
    """Custom type port2PowerCtr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Port2PowerCtr_Type.__name__ = "Integer32"
_Port2PowerCtr_Object = MibScalar
port2PowerCtr = _Port2PowerCtr_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 6),
    _Port2PowerCtr_Type()
)
port2PowerCtr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port2PowerCtr.setStatus("current")


class _Port3PowerCtr_Type(Integer32):
    """Custom type port3PowerCtr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Port3PowerCtr_Type.__name__ = "Integer32"
_Port3PowerCtr_Object = MibScalar
port3PowerCtr = _Port3PowerCtr_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 7),
    _Port3PowerCtr_Type()
)
port3PowerCtr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port3PowerCtr.setStatus("current")


class _Port4PowerCtr_Type(Integer32):
    """Custom type port4PowerCtr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Port4PowerCtr_Type.__name__ = "Integer32"
_Port4PowerCtr_Object = MibScalar
port4PowerCtr = _Port4PowerCtr_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 8),
    _Port4PowerCtr_Type()
)
port4PowerCtr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port4PowerCtr.setStatus("current")


class _Port5PowerCtr_Type(Integer32):
    """Custom type port5PowerCtr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Port5PowerCtr_Type.__name__ = "Integer32"
_Port5PowerCtr_Object = MibScalar
port5PowerCtr = _Port5PowerCtr_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 9),
    _Port5PowerCtr_Type()
)
port5PowerCtr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port5PowerCtr.setStatus("current")


class _Port6PowerCtr_Type(Integer32):
    """Custom type port6PowerCtr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Port6PowerCtr_Type.__name__ = "Integer32"
_Port6PowerCtr_Object = MibScalar
port6PowerCtr = _Port6PowerCtr_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 10),
    _Port6PowerCtr_Type()
)
port6PowerCtr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port6PowerCtr.setStatus("current")


class _Port7PowerCtr_Type(Integer32):
    """Custom type port7PowerCtr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Port7PowerCtr_Type.__name__ = "Integer32"
_Port7PowerCtr_Object = MibScalar
port7PowerCtr = _Port7PowerCtr_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 11),
    _Port7PowerCtr_Type()
)
port7PowerCtr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port7PowerCtr.setStatus("current")


class _Port8PowerCtr_Type(Integer32):
    """Custom type port8PowerCtr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Port8PowerCtr_Type.__name__ = "Integer32"
_Port8PowerCtr_Object = MibScalar
port8PowerCtr = _Port8PowerCtr_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 12),
    _Port8PowerCtr_Type()
)
port8PowerCtr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port8PowerCtr.setStatus("current")
_DisplayOnlyAccess_Type = DisplayString
_DisplayOnlyAccess_Object = MibScalar
displayOnlyAccess = _DisplayOnlyAccess_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 13),
    _DisplayOnlyAccess_Type()
)
displayOnlyAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    displayOnlyAccess.setStatus("current")
_FullAccess_Type = DisplayString
_FullAccess_Object = MibScalar
fullAccess = _FullAccess_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 14),
    _FullAccess_Type()
)
fullAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fullAccess.setStatus("current")
_DisplayOnlyStatus_Type = DisplayString
_DisplayOnlyStatus_Object = MibScalar
displayOnlyStatus = _DisplayOnlyStatus_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 15),
    _DisplayOnlyStatus_Type()
)
displayOnlyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    displayOnlyStatus.setStatus("current")
_FullAccessStatus_Type = DisplayString
_FullAccessStatus_Object = MibScalar
fullAccessStatus = _FullAccessStatus_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 16),
    _FullAccessStatus_Type()
)
fullAccessStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fullAccessStatus.setStatus("current")
_WebAutoUpdate_Type = Integer32
_WebAutoUpdate_Object = MibScalar
webAutoUpdate = _WebAutoUpdate_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 17),
    _WebAutoUpdate_Type()
)
webAutoUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    webAutoUpdate.setStatus("current")
if mibBuilder.loadTexts:
    webAutoUpdate.setUnits("Seconds")


class _Port1Config_Type(Integer32):
    """Custom type port1Config based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("hundredFDX", 2),
          ("hundredHDX", 3),
          ("tenFDX", 4),
          ("tenHDX", 5))
    )


_Port1Config_Type.__name__ = "Integer32"
_Port1Config_Object = MibScalar
port1Config = _Port1Config_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 18),
    _Port1Config_Type()
)
port1Config.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port1Config.setStatus("current")


class _Port2Config_Type(Integer32):
    """Custom type port2Config based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("hundredFDX", 2),
          ("hundredHDX", 3),
          ("tenFDX", 4),
          ("tenHDX", 5))
    )


_Port2Config_Type.__name__ = "Integer32"
_Port2Config_Object = MibScalar
port2Config = _Port2Config_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 19),
    _Port2Config_Type()
)
port2Config.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port2Config.setStatus("current")


class _Port3Config_Type(Integer32):
    """Custom type port3Config based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("hundredFDX", 2),
          ("hundredHDX", 3),
          ("tenFDX", 4),
          ("tenHDX", 5))
    )


_Port3Config_Type.__name__ = "Integer32"
_Port3Config_Object = MibScalar
port3Config = _Port3Config_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 20),
    _Port3Config_Type()
)
port3Config.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port3Config.setStatus("current")


class _Port4Config_Type(Integer32):
    """Custom type port4Config based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("hundredFDX", 2),
          ("hundredHDX", 3),
          ("tenFDX", 4),
          ("tenHDX", 5))
    )


_Port4Config_Type.__name__ = "Integer32"
_Port4Config_Object = MibScalar
port4Config = _Port4Config_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 21),
    _Port4Config_Type()
)
port4Config.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port4Config.setStatus("current")


class _Port5Config_Type(Integer32):
    """Custom type port5Config based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("hundredFDX", 2),
          ("hundredHDX", 3),
          ("tenFDX", 4),
          ("tenHDX", 5))
    )


_Port5Config_Type.__name__ = "Integer32"
_Port5Config_Object = MibScalar
port5Config = _Port5Config_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 22),
    _Port5Config_Type()
)
port5Config.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port5Config.setStatus("current")


class _Port6Config_Type(Integer32):
    """Custom type port6Config based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("hundredFDX", 2),
          ("hundredHDX", 3),
          ("tenFDX", 4),
          ("tenHDX", 5))
    )


_Port6Config_Type.__name__ = "Integer32"
_Port6Config_Object = MibScalar
port6Config = _Port6Config_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 23),
    _Port6Config_Type()
)
port6Config.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port6Config.setStatus("current")


class _Port7Config_Type(Integer32):
    """Custom type port7Config based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("hundredFDX", 2),
          ("hundredHDX", 3),
          ("tenFDX", 4),
          ("tenHDX", 5))
    )


_Port7Config_Type.__name__ = "Integer32"
_Port7Config_Object = MibScalar
port7Config = _Port7Config_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 24),
    _Port7Config_Type()
)
port7Config.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port7Config.setStatus("current")


class _Port8Config_Type(Integer32):
    """Custom type port8Config based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("hundredFDX", 2),
          ("hundredHDX", 3),
          ("tenFDX", 4),
          ("tenHDX", 5))
    )


_Port8Config_Type.__name__ = "Integer32"
_Port8Config_Object = MibScalar
port8Config = _Port8Config_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 25),
    _Port8Config_Type()
)
port8Config.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port8Config.setStatus("current")
_Port1Description_Type = DisplayString
_Port1Description_Object = MibScalar
port1Description = _Port1Description_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 26),
    _Port1Description_Type()
)
port1Description.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port1Description.setStatus("current")
_Port2Description_Type = DisplayString
_Port2Description_Object = MibScalar
port2Description = _Port2Description_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 27),
    _Port2Description_Type()
)
port2Description.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port2Description.setStatus("current")
_Port3Description_Type = DisplayString
_Port3Description_Object = MibScalar
port3Description = _Port3Description_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 28),
    _Port3Description_Type()
)
port3Description.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port3Description.setStatus("current")
_Port4Description_Type = DisplayString
_Port4Description_Object = MibScalar
port4Description = _Port4Description_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 29),
    _Port4Description_Type()
)
port4Description.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port4Description.setStatus("current")
_Port5Description_Type = DisplayString
_Port5Description_Object = MibScalar
port5Description = _Port5Description_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 30),
    _Port5Description_Type()
)
port5Description.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port5Description.setStatus("current")
_Port6Description_Type = DisplayString
_Port6Description_Object = MibScalar
port6Description = _Port6Description_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 31),
    _Port6Description_Type()
)
port6Description.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port6Description.setStatus("current")
_Port7Description_Type = DisplayString
_Port7Description_Object = MibScalar
port7Description = _Port7Description_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 32),
    _Port7Description_Type()
)
port7Description.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port7Description.setStatus("current")
_Port8Description_Type = DisplayString
_Port8Description_Object = MibScalar
port8Description = _Port8Description_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 33),
    _Port8Description_Type()
)
port8Description.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port8Description.setStatus("current")
_SnmpTrap1_Type = IpAddress
_SnmpTrap1_Object = MibScalar
snmpTrap1 = _SnmpTrap1_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 34),
    _SnmpTrap1_Type()
)
snmpTrap1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrap1.setStatus("current")
_SnmpTrap2_Type = IpAddress
_SnmpTrap2_Object = MibScalar
snmpTrap2 = _SnmpTrap2_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 35),
    _SnmpTrap2_Type()
)
snmpTrap2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrap2.setStatus("current")
_SnmpTrap3_Type = IpAddress
_SnmpTrap3_Object = MibScalar
snmpTrap3 = _SnmpTrap3_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 36),
    _SnmpTrap3_Type()
)
snmpTrap3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrap3.setStatus("current")
_SnmpTrap4_Type = IpAddress
_SnmpTrap4_Object = MibScalar
snmpTrap4 = _SnmpTrap4_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 37),
    _SnmpTrap4_Type()
)
snmpTrap4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrap4.setStatus("current")
_SnmpTrap5_Type = IpAddress
_SnmpTrap5_Object = MibScalar
snmpTrap5 = _SnmpTrap5_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 38),
    _SnmpTrap5_Type()
)
snmpTrap5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrap5.setStatus("current")
_SnmpTrap6_Type = IpAddress
_SnmpTrap6_Object = MibScalar
snmpTrap6 = _SnmpTrap6_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 39),
    _SnmpTrap6_Type()
)
snmpTrap6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrap6.setStatus("current")
_SnmpTrap7_Type = IpAddress
_SnmpTrap7_Object = MibScalar
snmpTrap7 = _SnmpTrap7_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 40),
    _SnmpTrap7_Type()
)
snmpTrap7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrap7.setStatus("current")
_SnmpTrap8_Type = IpAddress
_SnmpTrap8_Object = MibScalar
snmpTrap8 = _SnmpTrap8_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 41),
    _SnmpTrap8_Type()
)
snmpTrap8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrap8.setStatus("current")
_SnmpTrap9_Type = IpAddress
_SnmpTrap9_Object = MibScalar
snmpTrap9 = _SnmpTrap9_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 42),
    _SnmpTrap9_Type()
)
snmpTrap9.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrap9.setStatus("current")
_SnmpTrap10_Type = IpAddress
_SnmpTrap10_Object = MibScalar
snmpTrap10 = _SnmpTrap10_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 43),
    _SnmpTrap10_Type()
)
snmpTrap10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrap10.setStatus("current")


class _VlanTagEnable_Type(Integer32):
    """Custom type vlanTagEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_VlanTagEnable_Type.__name__ = "Integer32"
_VlanTagEnable_Object = MibScalar
vlanTagEnable = _VlanTagEnable_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 44),
    _VlanTagEnable_Type()
)
vlanTagEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanTagEnable.setStatus("current")


class _VlanTagId_Type(Integer32):
    """Custom type vlanTagId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_VlanTagId_Type.__name__ = "Integer32"
_VlanTagId_Object = MibScalar
vlanTagId = _VlanTagId_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 45),
    _VlanTagId_Type()
)
vlanTagId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanTagId.setStatus("current")


class _Port1Uplink_Type(Integer32):
    """Custom type port1Uplink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Port1Uplink_Type.__name__ = "Integer32"
_Port1Uplink_Object = MibScalar
port1Uplink = _Port1Uplink_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 46),
    _Port1Uplink_Type()
)
port1Uplink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port1Uplink.setStatus("current")


class _Port2Uplink_Type(Integer32):
    """Custom type port2Uplink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Port2Uplink_Type.__name__ = "Integer32"
_Port2Uplink_Object = MibScalar
port2Uplink = _Port2Uplink_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 47),
    _Port2Uplink_Type()
)
port2Uplink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port2Uplink.setStatus("current")


class _Port3Uplink_Type(Integer32):
    """Custom type port3Uplink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Port3Uplink_Type.__name__ = "Integer32"
_Port3Uplink_Object = MibScalar
port3Uplink = _Port3Uplink_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 48),
    _Port3Uplink_Type()
)
port3Uplink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port3Uplink.setStatus("current")


class _Port4Uplink_Type(Integer32):
    """Custom type port4Uplink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Port4Uplink_Type.__name__ = "Integer32"
_Port4Uplink_Object = MibScalar
port4Uplink = _Port4Uplink_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 49),
    _Port4Uplink_Type()
)
port4Uplink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port4Uplink.setStatus("current")


class _Port5Uplink_Type(Integer32):
    """Custom type port5Uplink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Port5Uplink_Type.__name__ = "Integer32"
_Port5Uplink_Object = MibScalar
port5Uplink = _Port5Uplink_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 50),
    _Port5Uplink_Type()
)
port5Uplink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port5Uplink.setStatus("current")


class _Port6Uplink_Type(Integer32):
    """Custom type port6Uplink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Port6Uplink_Type.__name__ = "Integer32"
_Port6Uplink_Object = MibScalar
port6Uplink = _Port6Uplink_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 51),
    _Port6Uplink_Type()
)
port6Uplink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port6Uplink.setStatus("current")


class _Port7Uplink_Type(Integer32):
    """Custom type port7Uplink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Port7Uplink_Type.__name__ = "Integer32"
_Port7Uplink_Object = MibScalar
port7Uplink = _Port7Uplink_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 52),
    _Port7Uplink_Type()
)
port7Uplink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port7Uplink.setStatus("current")


class _Port8Uplink_Type(Integer32):
    """Custom type port8Uplink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Port8Uplink_Type.__name__ = "Integer32"
_Port8Uplink_Object = MibScalar
port8Uplink = _Port8Uplink_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 53),
    _Port8Uplink_Type()
)
port8Uplink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port8Uplink.setStatus("current")


class _RebootIfRequired_Type(Integer32):
    """Custom type rebootIfRequired based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_RebootIfRequired_Type.__name__ = "Integer32"
_RebootIfRequired_Object = MibScalar
rebootIfRequired = _RebootIfRequired_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 54),
    _RebootIfRequired_Type()
)
rebootIfRequired.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rebootIfRequired.setStatus("current")


class _Port1VlanConf_Type(Integer32):
    """Custom type port1VlanConf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Port1VlanConf_Type.__name__ = "Integer32"
_Port1VlanConf_Object = MibScalar
port1VlanConf = _Port1VlanConf_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 55),
    _Port1VlanConf_Type()
)
port1VlanConf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port1VlanConf.setStatus("current")


class _Port2VlanConf_Type(Integer32):
    """Custom type port2VlanConf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Port2VlanConf_Type.__name__ = "Integer32"
_Port2VlanConf_Object = MibScalar
port2VlanConf = _Port2VlanConf_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 56),
    _Port2VlanConf_Type()
)
port2VlanConf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port2VlanConf.setStatus("current")


class _Port3VlanConf_Type(Integer32):
    """Custom type port3VlanConf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Port3VlanConf_Type.__name__ = "Integer32"
_Port3VlanConf_Object = MibScalar
port3VlanConf = _Port3VlanConf_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 57),
    _Port3VlanConf_Type()
)
port3VlanConf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port3VlanConf.setStatus("current")


class _Port4VlanConf_Type(Integer32):
    """Custom type port4VlanConf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Port4VlanConf_Type.__name__ = "Integer32"
_Port4VlanConf_Object = MibScalar
port4VlanConf = _Port4VlanConf_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 58),
    _Port4VlanConf_Type()
)
port4VlanConf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port4VlanConf.setStatus("current")


class _Port5VlanConf_Type(Integer32):
    """Custom type port5VlanConf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Port5VlanConf_Type.__name__ = "Integer32"
_Port5VlanConf_Object = MibScalar
port5VlanConf = _Port5VlanConf_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 59),
    _Port5VlanConf_Type()
)
port5VlanConf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port5VlanConf.setStatus("current")


class _Port6VlanConf_Type(Integer32):
    """Custom type port6VlanConf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Port6VlanConf_Type.__name__ = "Integer32"
_Port6VlanConf_Object = MibScalar
port6VlanConf = _Port6VlanConf_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 60),
    _Port6VlanConf_Type()
)
port6VlanConf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port6VlanConf.setStatus("current")


class _Port7VlanConf_Type(Integer32):
    """Custom type port7VlanConf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Port7VlanConf_Type.__name__ = "Integer32"
_Port7VlanConf_Object = MibScalar
port7VlanConf = _Port7VlanConf_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 61),
    _Port7VlanConf_Type()
)
port7VlanConf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port7VlanConf.setStatus("current")


class _Port8VlanConf_Type(Integer32):
    """Custom type port8VlanConf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Port8VlanConf_Type.__name__ = "Integer32"
_Port8VlanConf_Object = MibScalar
port8VlanConf = _Port8VlanConf_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 62),
    _Port8VlanConf_Type()
)
port8VlanConf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port8VlanConf.setStatus("current")


class _Port1PwrReset_Type(Integer32):
    """Custom type port1PwrReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Port1PwrReset_Type.__name__ = "Integer32"
_Port1PwrReset_Object = MibScalar
port1PwrReset = _Port1PwrReset_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 63),
    _Port1PwrReset_Type()
)
port1PwrReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port1PwrReset.setStatus("current")


class _Port2PwrReset_Type(Integer32):
    """Custom type port2PwrReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Port2PwrReset_Type.__name__ = "Integer32"
_Port2PwrReset_Object = MibScalar
port2PwrReset = _Port2PwrReset_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 64),
    _Port2PwrReset_Type()
)
port2PwrReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port2PwrReset.setStatus("current")


class _Port3PwrReset_Type(Integer32):
    """Custom type port3PwrReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Port3PwrReset_Type.__name__ = "Integer32"
_Port3PwrReset_Object = MibScalar
port3PwrReset = _Port3PwrReset_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 65),
    _Port3PwrReset_Type()
)
port3PwrReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port3PwrReset.setStatus("current")


class _Port4PwrReset_Type(Integer32):
    """Custom type port4PwrReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Port4PwrReset_Type.__name__ = "Integer32"
_Port4PwrReset_Object = MibScalar
port4PwrReset = _Port4PwrReset_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 66),
    _Port4PwrReset_Type()
)
port4PwrReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port4PwrReset.setStatus("current")


class _Port5PwrReset_Type(Integer32):
    """Custom type port5PwrReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Port5PwrReset_Type.__name__ = "Integer32"
_Port5PwrReset_Object = MibScalar
port5PwrReset = _Port5PwrReset_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 67),
    _Port5PwrReset_Type()
)
port5PwrReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port5PwrReset.setStatus("current")


class _Port6PwrReset_Type(Integer32):
    """Custom type port6PwrReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Port6PwrReset_Type.__name__ = "Integer32"
_Port6PwrReset_Object = MibScalar
port6PwrReset = _Port6PwrReset_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 68),
    _Port6PwrReset_Type()
)
port6PwrReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port6PwrReset.setStatus("current")


class _Port7PwrReset_Type(Integer32):
    """Custom type port7PwrReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Port7PwrReset_Type.__name__ = "Integer32"
_Port7PwrReset_Object = MibScalar
port7PwrReset = _Port7PwrReset_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 69),
    _Port7PwrReset_Type()
)
port7PwrReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port7PwrReset.setStatus("current")


class _Port8PwrReset_Type(Integer32):
    """Custom type port8PwrReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Port8PwrReset_Type.__name__ = "Integer32"
_Port8PwrReset_Object = MibScalar
port8PwrReset = _Port8PwrReset_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 70),
    _Port8PwrReset_Type()
)
port8PwrReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port8PwrReset.setStatus("current")
_CmmStatus_ObjectIdentity = ObjectIdentity
cmmStatus = _CmmStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 4)
)
_CmmPortTable_Object = MibTable
cmmPortTable = _CmmPortTable_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 4, 1)
)
if mibBuilder.loadTexts:
    cmmPortTable.setStatus("current")
_CmmPortEntry_Object = MibTableRow
cmmPortEntry = _CmmPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 4, 1, 1)
)
cmmPortEntry.setIndexNames(
    (0, "CMM3-MIB", "portIndex"),
)
if mibBuilder.loadTexts:
    cmmPortEntry.setStatus("current")


class _PortIndex_Type(Integer32):
    """Custom type portIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PortIndex_Type.__name__ = "Integer32"
_PortIndex_Object = MibTableColumn
portIndex = _PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 4, 1, 1, 1),
    _PortIndex_Type()
)
portIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portIndex.setStatus("current")


class _LinkStatus_Type(Integer32):
    """Custom type linkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_LinkStatus_Type.__name__ = "Integer32"
_LinkStatus_Object = MibTableColumn
linkStatus = _LinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 4, 1, 1, 2),
    _LinkStatus_Type()
)
linkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkStatus.setStatus("current")


class _LinkSpeed_Type(Integer32):
    """Custom type linkSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("hundredBaseT", 1),
          ("tenBaseT", 0))
    )


_LinkSpeed_Type.__name__ = "Integer32"
_LinkSpeed_Object = MibTableColumn
linkSpeed = _LinkSpeed_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 4, 1, 1, 3),
    _LinkSpeed_Type()
)
linkSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkSpeed.setStatus("current")


class _DuplexStatus_Type(Integer32):
    """Custom type duplexStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("fullDuplex", 1),
          ("halfDuplex", 0))
    )


_DuplexStatus_Type.__name__ = "Integer32"
_DuplexStatus_Object = MibTableColumn
duplexStatus = _DuplexStatus_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 4, 1, 1, 4),
    _DuplexStatus_Type()
)
duplexStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    duplexStatus.setStatus("current")


class _PowerStatus_Type(Integer32):
    """Custom type powerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_PowerStatus_Type.__name__ = "Integer32"
_PowerStatus_Object = MibTableColumn
powerStatus = _PowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 4, 1, 1, 5),
    _PowerStatus_Type()
)
powerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerStatus.setStatus("current")


class _UplinkStatus_Type(Integer32):
    """Custom type uplinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_UplinkStatus_Type.__name__ = "Integer32"
_UplinkStatus_Object = MibScalar
uplinkStatus = _UplinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 4, 1, 1, 6),
    _UplinkStatus_Type()
)
uplinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplinkStatus.setStatus("current")
_DeviceType_Type = DisplayString
_DeviceType_Object = MibScalar
deviceType = _DeviceType_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 4, 2),
    _DeviceType_Type()
)
deviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceType.setStatus("current")
_PldVersion_Type = DisplayString
_PldVersion_Object = MibScalar
pldVersion = _PldVersion_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 4, 3),
    _PldVersion_Type()
)
pldVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pldVersion.setStatus("current")
_SoftwareVersion_Type = DisplayString
_SoftwareVersion_Object = MibScalar
softwareVersion = _SoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 4, 4),
    _SoftwareVersion_Type()
)
softwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareVersion.setStatus("current")
_SystemTime_Type = DisplayString
_SystemTime_Object = MibScalar
systemTime = _SystemTime_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 4, 5),
    _SystemTime_Type()
)
systemTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemTime.setStatus("current")
_UpTime_Type = DisplayString
_UpTime_Object = MibScalar
upTime = _UpTime_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 4, 6),
    _UpTime_Type()
)
upTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upTime.setStatus("current")
_SatellitesVisible_Type = DisplayString
_SatellitesVisible_Object = MibScalar
satellitesVisible = _SatellitesVisible_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 4, 7),
    _SatellitesVisible_Type()
)
satellitesVisible.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    satellitesVisible.setStatus("current")
_SatellitesTracked_Type = DisplayString
_SatellitesTracked_Object = MibScalar
satellitesTracked = _SatellitesTracked_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 4, 8),
    _SatellitesTracked_Type()
)
satellitesTracked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    satellitesTracked.setStatus("current")
_Latitude_Type = DisplayString
_Latitude_Object = MibScalar
latitude = _Latitude_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 4, 9),
    _Latitude_Type()
)
latitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    latitude.setStatus("current")
_Longitude_Type = DisplayString
_Longitude_Object = MibScalar
longitude = _Longitude_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 4, 10),
    _Longitude_Type()
)
longitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    longitude.setStatus("current")
_Height_Type = DisplayString
_Height_Object = MibScalar
height = _Height_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 4, 11),
    _Height_Type()
)
height.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    height.setStatus("current")
_TrackingMode_Type = DisplayString
_TrackingMode_Object = MibScalar
trackingMode = _TrackingMode_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 4, 12),
    _TrackingMode_Type()
)
trackingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trackingMode.setStatus("current")
_SyncStatus_Type = DisplayString
_SyncStatus_Object = MibScalar
syncStatus = _SyncStatus_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 4, 13),
    _SyncStatus_Type()
)
syncStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syncStatus.setStatus("current")
_MacAddress_Type = DisplayString
_MacAddress_Object = MibScalar
macAddress = _MacAddress_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 4, 14),
    _MacAddress_Type()
)
macAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macAddress.setStatus("current")
_CmmGps_ObjectIdentity = ObjectIdentity
cmmGps = _CmmGps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 5)
)
_GpsTrackingMode_Type = DisplayString
_GpsTrackingMode_Object = MibScalar
gpsTrackingMode = _GpsTrackingMode_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 5, 1),
    _GpsTrackingMode_Type()
)
gpsTrackingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsTrackingMode.setStatus("current")
_GpsTime_Type = DisplayString
_GpsTime_Object = MibScalar
gpsTime = _GpsTime_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 5, 2),
    _GpsTime_Type()
)
gpsTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsTime.setStatus("current")
_GpsDate_Type = DisplayString
_GpsDate_Object = MibScalar
gpsDate = _GpsDate_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 5, 3),
    _GpsDate_Type()
)
gpsDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsDate.setStatus("current")
_GpsSatellitesVisible_Type = DisplayString
_GpsSatellitesVisible_Object = MibScalar
gpsSatellitesVisible = _GpsSatellitesVisible_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 5, 4),
    _GpsSatellitesVisible_Type()
)
gpsSatellitesVisible.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsSatellitesVisible.setStatus("current")
_GpsSatellitesTracked_Type = DisplayString
_GpsSatellitesTracked_Object = MibScalar
gpsSatellitesTracked = _GpsSatellitesTracked_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 5, 5),
    _GpsSatellitesTracked_Type()
)
gpsSatellitesTracked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsSatellitesTracked.setStatus("current")
_GpsHeight_Type = DisplayString
_GpsHeight_Object = MibScalar
gpsHeight = _GpsHeight_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 5, 6),
    _GpsHeight_Type()
)
gpsHeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsHeight.setStatus("current")
_GpsAntennaConnection_Type = DisplayString
_GpsAntennaConnection_Object = MibScalar
gpsAntennaConnection = _GpsAntennaConnection_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 5, 7),
    _GpsAntennaConnection_Type()
)
gpsAntennaConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsAntennaConnection.setStatus("current")
_GpsLatitude_Type = DisplayString
_GpsLatitude_Object = MibScalar
gpsLatitude = _GpsLatitude_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 5, 8),
    _GpsLatitude_Type()
)
gpsLatitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsLatitude.setStatus("current")
_GpsLongitude_Type = DisplayString
_GpsLongitude_Object = MibScalar
gpsLongitude = _GpsLongitude_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 5, 9),
    _GpsLongitude_Type()
)
gpsLongitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsLongitude.setStatus("current")
_GpsInvalidMsg_Type = DisplayString
_GpsInvalidMsg_Object = MibScalar
gpsInvalidMsg = _GpsInvalidMsg_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 5, 10),
    _GpsInvalidMsg_Type()
)
gpsInvalidMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsInvalidMsg.setStatus("current")
_GpsRestartCount_Type = Integer32
_GpsRestartCount_Object = MibScalar
gpsRestartCount = _GpsRestartCount_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 5, 11),
    _GpsRestartCount_Type()
)
gpsRestartCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsRestartCount.setStatus("current")
_GpsReceiverInfo_Type = DisplayString
_GpsReceiverInfo_Object = MibScalar
gpsReceiverInfo = _GpsReceiverInfo_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 5, 12),
    _GpsReceiverInfo_Type()
)
gpsReceiverInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsReceiverInfo.setStatus("current")
_CmmEventLog_ObjectIdentity = ObjectIdentity
cmmEventLog = _CmmEventLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 6)
)
_EventLog_Type = EventString
_EventLog_Object = MibScalar
eventLog = _EventLog_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 6, 1),
    _EventLog_Type()
)
eventLog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventLog.setStatus("current")
_CmmControls_ObjectIdentity = ObjectIdentity
cmmControls = _CmmControls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 7)
)


class _Reboot_Type(Integer32):
    """Custom type reboot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("finishedReboot", 0),
          ("reboot", 1))
    )


_Reboot_Type.__name__ = "Integer32"
_Reboot_Object = MibScalar
reboot = _Reboot_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 7, 1),
    _Reboot_Type()
)
reboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reboot.setStatus("current")


class _ClearEventLog_Type(Integer32):
    """Custom type clearEventLog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("notClear", 0))
    )


_ClearEventLog_Type.__name__ = "Integer32"
_ClearEventLog_Object = MibScalar
clearEventLog = _ClearEventLog_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 7, 2),
    _ClearEventLog_Type()
)
clearEventLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clearEventLog.setStatus("current")

# Managed Objects groups

cmmSwitchGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 1, 1)
)
cmmSwitchGroup.setObjects(
      *(("CMM3-MIB", "portNumber"),
        ("CMM3-MIB", "rxDropPkts"),
        ("CMM3-MIB", "rxOctets"),
        ("CMM3-MIB", "rxBroadcastPkts"),
        ("CMM3-MIB", "rxMulticastPkts"),
        ("CMM3-MIB", "rxSAChanges"),
        ("CMM3-MIB", "rxUndersizePkts"),
        ("CMM3-MIB", "rxOversizePkts"),
        ("CMM3-MIB", "rxFragments"),
        ("CMM3-MIB", "rxJabbers"),
        ("CMM3-MIB", "rxUnicastPkts"),
        ("CMM3-MIB", "rxAlignmentErrors"),
        ("CMM3-MIB", "rxFCSErrors"),
        ("CMM3-MIB", "rxGoodOctets"),
        ("CMM3-MIB", "rxExcessSizeDisc"),
        ("CMM3-MIB", "rxPausePkts"),
        ("CMM3-MIB", "rxSymbolErrors"),
        ("CMM3-MIB", "txDropPkts"),
        ("CMM3-MIB", "txOctets"),
        ("CMM3-MIB", "txBroadcastPkts"),
        ("CMM3-MIB", "txMulticastPkts"),
        ("CMM3-MIB", "txCollisions"),
        ("CMM3-MIB", "txUnicastPkts"),
        ("CMM3-MIB", "txSingleCollision"),
        ("CMM3-MIB", "txMultipleCollision"),
        ("CMM3-MIB", "txDeferredTransmit"),
        ("CMM3-MIB", "txLateCollision"),
        ("CMM3-MIB", "txExcessiveCollision"),
        ("CMM3-MIB", "txPausePkts"),
        ("CMM3-MIB", "txFrameInDisc"),
        ("CMM3-MIB", "pkts64Octets"),
        ("CMM3-MIB", "pkts65to127Octets"),
        ("CMM3-MIB", "pkts128to255Octets"),
        ("CMM3-MIB", "pkts256to511Octets"),
        ("CMM3-MIB", "pkts512to1023Octets"),
        ("CMM3-MIB", "pkts1024to1522Octets"))
)
if mibBuilder.loadTexts:
    cmmSwitchGroup.setStatus("current")

cmmConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 1, 2)
)
cmmConfigGroup.setObjects(
      *(("CMM3-MIB", "gpstimingpulse"),
        ("CMM3-MIB", "lan1ip"),
        ("CMM3-MIB", "lan1subnetmask"),
        ("CMM3-MIB", "defaultgateway"),
        ("CMM3-MIB", "port1powerctr"),
        ("CMM3-MIB", "port2powerctr"),
        ("CMM3-MIB", "port3powerctr"),
        ("CMM3-MIB", "port4powerctr"),
        ("CMM3-MIB", "port5powerctr"),
        ("CMM3-MIB", "port6powerctr"),
        ("CMM3-MIB", "port7powerctr"),
        ("CMM3-MIB", "port8powerctr"),
        ("CMM3-MIB", "displayonlyaccess"),
        ("CMM3-MIB", "fullaccess"),
        ("CMM3-MIB", "displayonlystatus"),
        ("CMM3-MIB", "fullaccessstatus"),
        ("CMM3-MIB", "webautoupdate"),
        ("CMM3-MIB", "port1config"),
        ("CMM3-MIB", "port2config"),
        ("CMM3-MIB", "port3config"),
        ("CMM3-MIB", "port4config"),
        ("CMM3-MIB", "port5config"),
        ("CMM3-MIB", "port6config"),
        ("CMM3-MIB", "port7config"),
        ("CMM3-MIB", "port8config"),
        ("CMM3-MIB", "port1description"),
        ("CMM3-MIB", "port2description"),
        ("CMM3-MIB", "port3description"),
        ("CMM3-MIB", "port4description"),
        ("CMM3-MIB", "port5description"),
        ("CMM3-MIB", "port6description"),
        ("CMM3-MIB", "port7description"),
        ("CMM3-MIB", "port8description"),
        ("CMM3-MIB", "snmptrap1"),
        ("CMM3-MIB", "snmptrap2"),
        ("CMM3-MIB", "snmptrap3"),
        ("CMM3-MIB", "snmptrap4"),
        ("CMM3-MIB", "snmptrap5"),
        ("CMM3-MIB", "snmptrap6"),
        ("CMM3-MIB", "snmptrap7"),
        ("CMM3-MIB", "snmptrap8"),
        ("CMM3-MIB", "snmptrap9"),
        ("CMM3-MIB", "snmptrap10"),
        ("CMM3-MIB", "vlantagenable"),
        ("CMM3-MIB", "vlantagid"),
        ("CMM3-MIB", "port1uplink"),
        ("CMM3-MIB", "port2uplink"),
        ("CMM3-MIB", "port3uplink"),
        ("CMM3-MIB", "port4uplink"),
        ("CMM3-MIB", "port5uplink"),
        ("CMM3-MIB", "port6uplink"),
        ("CMM3-MIB", "port7uplink"),
        ("CMM3-MIB", "port8uplink"),
        ("CMM3-MIB", "rebootifrequired"),
        ("CMM3-MIB", "port1vlanconf"),
        ("CMM3-MIB", "port2vlanconf"),
        ("CMM3-MIB", "port3vlanconf"),
        ("CMM3-MIB", "port4vlanconf"),
        ("CMM3-MIB", "port5vlanconf"),
        ("CMM3-MIB", "port6vlanconf"),
        ("CMM3-MIB", "port7vlanconf"),
        ("CMM3-MIB", "port8vlanconf"),
        ("CMM3-MIB", "port1pwrreset"),
        ("CMM3-MIB", "port2pwrreset"),
        ("CMM3-MIB", "port3pwrreset"),
        ("CMM3-MIB", "port4pwrreset"),
        ("CMM3-MIB", "port5pwrreset"),
        ("CMM3-MIB", "port6pwrreset"),
        ("CMM3-MIB", "port7pwrreset"),
        ("CMM3-MIB", "port8pwrreset"))
)
if mibBuilder.loadTexts:
    cmmConfigGroup.setStatus("current")

cmmStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 1, 3)
)
cmmStatusGroup.setObjects(
      *(("CMM3-MIB", "portindex"),
        ("CMM3-MIB", "linkstatus"),
        ("CMM3-MIB", "linkspeed"),
        ("CMM3-MIB", "duplexstatus"),
        ("CMM3-MIB", "powerstatus"),
        ("CMM3-MIB", "uplinkstatus"),
        ("CMM3-MIB", "devicetype"),
        ("CMM3-MIB", "pldversion"),
        ("CMM3-MIB", "softwareversion"),
        ("CMM3-MIB", "systemtime"),
        ("CMM3-MIB", "uptime"),
        ("CMM3-MIB", "satellitesvisible"),
        ("CMM3-MIB", "satellitestracked"),
        ("CMM3-MIB", "latitude"),
        ("CMM3-MIB", "longitude"),
        ("CMM3-MIB", "height"),
        ("CMM3-MIB", "trackingmode"),
        ("CMM3-MIB", "syncstatus"),
        ("CMM3-MIB", "macaddress"))
)
if mibBuilder.loadTexts:
    cmmStatusGroup.setStatus("current")

cmmGPSGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 1, 4)
)
cmmGPSGroup.setObjects(
      *(("CMM3-MIB", "gpsTrackingMode"),
        ("CMM3-MIB", "gpsTime"),
        ("CMM3-MIB", "gpsDate"),
        ("CMM3-MIB", "gpsSatellitesVisible"),
        ("CMM3-MIB", "gpsSatellitesTracked"),
        ("CMM3-MIB", "gpsHeight"),
        ("CMM3-MIB", "gpsAntennaConnection"),
        ("CMM3-MIB", "gpsLatitude"),
        ("CMM3-MIB", "gpsLongitude"),
        ("CMM3-MIB", "gpsInvalidMsg"),
        ("CMM3-MIB", "gpsRestartCount"),
        ("CMM3-MIB", "gpsReceiverInfo"))
)
if mibBuilder.loadTexts:
    cmmGPSGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CMM3-MIB",
    **{"cmmIIIMibModule": cmmIIIMibModule,
       "cmmGroups": cmmGroups,
       "cmmSwitchGroup": cmmSwitchGroup,
       "cmmConfigGroup": cmmConfigGroup,
       "cmmStatusGroup": cmmStatusGroup,
       "cmmGPSGroup": cmmGPSGroup,
       "cmmSwitch": cmmSwitch,
       "cmmSwitchTable": cmmSwitchTable,
       "cmmSwitchEntry": cmmSwitchEntry,
       "portNumber": portNumber,
       "rxDropPkts": rxDropPkts,
       "rxOctets": rxOctets,
       "rxBroadcastPkts": rxBroadcastPkts,
       "rxMulticastPkts": rxMulticastPkts,
       "rxSAChanges": rxSAChanges,
       "rxUndersizePkts": rxUndersizePkts,
       "rxOversizePkts": rxOversizePkts,
       "rxFragments": rxFragments,
       "rxJabbers": rxJabbers,
       "rxUnicastPkts": rxUnicastPkts,
       "rxAlignmentErrors": rxAlignmentErrors,
       "rxFCSErrors": rxFCSErrors,
       "rxGoodOctets": rxGoodOctets,
       "rxExcessSizeDisc": rxExcessSizeDisc,
       "rxPausePkts": rxPausePkts,
       "rxSymbolErrors": rxSymbolErrors,
       "txDropPkts": txDropPkts,
       "txOctets": txOctets,
       "txBroadcastPkts": txBroadcastPkts,
       "txMulticastPkts": txMulticastPkts,
       "txCollisions": txCollisions,
       "txUnicastPkts": txUnicastPkts,
       "txSingleCollision": txSingleCollision,
       "txMultipleCollision": txMultipleCollision,
       "txDeferredTransmit": txDeferredTransmit,
       "txLateCollision": txLateCollision,
       "txExcessiveCollision": txExcessiveCollision,
       "txPausePkts": txPausePkts,
       "txFrameInDisc": txFrameInDisc,
       "pkts64Octets": pkts64Octets,
       "pkts65to127Octets": pkts65to127Octets,
       "pkts128to255Octets": pkts128to255Octets,
       "pkts256to511Octets": pkts256to511Octets,
       "pkts512to1023Octets": pkts512to1023Octets,
       "pkts1024to1522Octets": pkts1024to1522Octets,
       "cmmConfig": cmmConfig,
       "gpsTimingPulse": gpsTimingPulse,
       "lan1Ip": lan1Ip,
       "lan1SubnetMask": lan1SubnetMask,
       "defaultGateWay": defaultGateWay,
       "port1PowerCtr": port1PowerCtr,
       "port2PowerCtr": port2PowerCtr,
       "port3PowerCtr": port3PowerCtr,
       "port4PowerCtr": port4PowerCtr,
       "port5PowerCtr": port5PowerCtr,
       "port6PowerCtr": port6PowerCtr,
       "port7PowerCtr": port7PowerCtr,
       "port8PowerCtr": port8PowerCtr,
       "displayOnlyAccess": displayOnlyAccess,
       "fullAccess": fullAccess,
       "displayOnlyStatus": displayOnlyStatus,
       "fullAccessStatus": fullAccessStatus,
       "webAutoUpdate": webAutoUpdate,
       "port1Config": port1Config,
       "port2Config": port2Config,
       "port3Config": port3Config,
       "port4Config": port4Config,
       "port5Config": port5Config,
       "port6Config": port6Config,
       "port7Config": port7Config,
       "port8Config": port8Config,
       "port1Description": port1Description,
       "port2Description": port2Description,
       "port3Description": port3Description,
       "port4Description": port4Description,
       "port5Description": port5Description,
       "port6Description": port6Description,
       "port7Description": port7Description,
       "port8Description": port8Description,
       "snmpTrap1": snmpTrap1,
       "snmpTrap2": snmpTrap2,
       "snmpTrap3": snmpTrap3,
       "snmpTrap4": snmpTrap4,
       "snmpTrap5": snmpTrap5,
       "snmpTrap6": snmpTrap6,
       "snmpTrap7": snmpTrap7,
       "snmpTrap8": snmpTrap8,
       "snmpTrap9": snmpTrap9,
       "snmpTrap10": snmpTrap10,
       "vlanTagEnable": vlanTagEnable,
       "vlanTagId": vlanTagId,
       "port1Uplink": port1Uplink,
       "port2Uplink": port2Uplink,
       "port3Uplink": port3Uplink,
       "port4Uplink": port4Uplink,
       "port5Uplink": port5Uplink,
       "port6Uplink": port6Uplink,
       "port7Uplink": port7Uplink,
       "port8Uplink": port8Uplink,
       "rebootIfRequired": rebootIfRequired,
       "port1VlanConf": port1VlanConf,
       "port2VlanConf": port2VlanConf,
       "port3VlanConf": port3VlanConf,
       "port4VlanConf": port4VlanConf,
       "port5VlanConf": port5VlanConf,
       "port6VlanConf": port6VlanConf,
       "port7VlanConf": port7VlanConf,
       "port8VlanConf": port8VlanConf,
       "port1PwrReset": port1PwrReset,
       "port2PwrReset": port2PwrReset,
       "port3PwrReset": port3PwrReset,
       "port4PwrReset": port4PwrReset,
       "port5PwrReset": port5PwrReset,
       "port6PwrReset": port6PwrReset,
       "port7PwrReset": port7PwrReset,
       "port8PwrReset": port8PwrReset,
       "cmmStatus": cmmStatus,
       "cmmPortTable": cmmPortTable,
       "cmmPortEntry": cmmPortEntry,
       "portIndex": portIndex,
       "linkStatus": linkStatus,
       "linkSpeed": linkSpeed,
       "duplexStatus": duplexStatus,
       "powerStatus": powerStatus,
       "uplinkStatus": uplinkStatus,
       "deviceType": deviceType,
       "pldVersion": pldVersion,
       "softwareVersion": softwareVersion,
       "systemTime": systemTime,
       "upTime": upTime,
       "satellitesVisible": satellitesVisible,
       "satellitesTracked": satellitesTracked,
       "latitude": latitude,
       "longitude": longitude,
       "height": height,
       "trackingMode": trackingMode,
       "syncStatus": syncStatus,
       "macAddress": macAddress,
       "cmmGps": cmmGps,
       "gpsTrackingMode": gpsTrackingMode,
       "gpsTime": gpsTime,
       "gpsDate": gpsDate,
       "gpsSatellitesVisible": gpsSatellitesVisible,
       "gpsSatellitesTracked": gpsSatellitesTracked,
       "gpsHeight": gpsHeight,
       "gpsAntennaConnection": gpsAntennaConnection,
       "gpsLatitude": gpsLatitude,
       "gpsLongitude": gpsLongitude,
       "gpsInvalidMsg": gpsInvalidMsg,
       "gpsRestartCount": gpsRestartCount,
       "gpsReceiverInfo": gpsReceiverInfo,
       "cmmEventLog": cmmEventLog,
       "eventLog": eventLog,
       "cmmControls": cmmControls,
       "reboot": reboot,
       "clearEventLog": clearEventLog}
)
