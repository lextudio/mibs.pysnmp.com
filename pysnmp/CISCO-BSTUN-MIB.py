# SNMP MIB module (CISCO-BSTUN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-BSTUN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:56:25 2024
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

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoBstunMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 35)
)
ciscoBstunMIB.setRevisions(
        ("2003-02-10 00:00",
         "2001-06-19 00:00",
         "1997-01-22 00:00",
         "1995-08-21 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BstunObjects_ObjectIdentity = ObjectIdentity
bstunObjects = _BstunObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 35, 1)
)
_BstunGlobal_ObjectIdentity = ObjectIdentity
bstunGlobal = _BstunGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 35, 1, 1)
)
_BstunIPAddr_Type = IpAddress
_BstunIPAddr_Object = MibScalar
bstunIPAddr = _BstunIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 35, 1, 1, 1),
    _BstunIPAddr_Type()
)
bstunIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bstunIPAddr.setStatus("current")


class _BstunLisnSap_Type(Integer32):
    """Custom type bstunLisnSap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_BstunLisnSap_Type.__name__ = "Integer32"
_BstunLisnSap_Object = MibScalar
bstunLisnSap = _BstunLisnSap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 35, 1, 1, 2),
    _BstunLisnSap_Type()
)
bstunLisnSap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bstunLisnSap.setStatus("current")


class _BstunPeerKeepaliveInterval_Type(Integer32):
    """Custom type bstunPeerKeepaliveInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_BstunPeerKeepaliveInterval_Type.__name__ = "Integer32"
_BstunPeerKeepaliveInterval_Object = MibScalar
bstunPeerKeepaliveInterval = _BstunPeerKeepaliveInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 35, 1, 1, 3),
    _BstunPeerKeepaliveInterval_Type()
)
bstunPeerKeepaliveInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bstunPeerKeepaliveInterval.setStatus("current")
if mibBuilder.loadTexts:
    bstunPeerKeepaliveInterval.setUnits("deciseconds")


class _BstunPeerKeepaliveLimit_Type(Integer32):
    """Custom type bstunPeerKeepaliveLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_BstunPeerKeepaliveLimit_Type.__name__ = "Integer32"
_BstunPeerKeepaliveLimit_Object = MibScalar
bstunPeerKeepaliveLimit = _BstunPeerKeepaliveLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 35, 1, 1, 4),
    _BstunPeerKeepaliveLimit_Type()
)
bstunPeerKeepaliveLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bstunPeerKeepaliveLimit.setStatus("current")
_BstunGroups_ObjectIdentity = ObjectIdentity
bstunGroups = _BstunGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 35, 1, 2)
)
_BstunGroupTable_Object = MibTable
bstunGroupTable = _BstunGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 35, 1, 2, 1)
)
if mibBuilder.loadTexts:
    bstunGroupTable.setStatus("current")
_BstunGroupEntry_Object = MibTableRow
bstunGroupEntry = _BstunGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 35, 1, 2, 1, 1)
)
bstunGroupEntry.setIndexNames(
    (0, "CISCO-BSTUN-MIB", "bstunGroupIndex"),
)
if mibBuilder.loadTexts:
    bstunGroupEntry.setStatus("current")


class _BstunGroupIndex_Type(Integer32):
    """Custom type bstunGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_BstunGroupIndex_Type.__name__ = "Integer32"
_BstunGroupIndex_Object = MibTableColumn
bstunGroupIndex = _BstunGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 35, 1, 2, 1, 1, 1),
    _BstunGroupIndex_Type()
)
bstunGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bstunGroupIndex.setStatus("current")


class _BstunProtocolType_Type(Integer32):
    """Custom type bstunProtocolType based on Integer32"""
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
        *(("adplex", 4),
          ("adtPollSelect", 3),
          ("adtVariPoll", 2),
          ("apos", 10),
          ("asyncGeneric", 6),
          ("bsc", 1),
          ("diebold", 5),
          ("gddb", 9),
          ("mdi", 7),
          ("mosec", 8))
    )


_BstunProtocolType_Type.__name__ = "Integer32"
_BstunProtocolType_Object = MibTableColumn
bstunProtocolType = _BstunProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 35, 1, 2, 1, 1, 2),
    _BstunProtocolType_Type()
)
bstunProtocolType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bstunProtocolType.setStatus("current")
_BstunLocalAck_Type = TruthValue
_BstunLocalAck_Object = MibTableColumn
bstunLocalAck = _BstunLocalAck_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 35, 1, 2, 1, 1, 3),
    _BstunLocalAck_Type()
)
bstunLocalAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bstunLocalAck.setStatus("current")
_BstunGroupUnroutableTransmit_Type = Counter32
_BstunGroupUnroutableTransmit_Object = MibTableColumn
bstunGroupUnroutableTransmit = _BstunGroupUnroutableTransmit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 35, 1, 2, 1, 1, 4),
    _BstunGroupUnroutableTransmit_Type()
)
bstunGroupUnroutableTransmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bstunGroupUnroutableTransmit.setStatus("current")
_BstunGroupUnroutableReceive_Type = Counter32
_BstunGroupUnroutableReceive_Object = MibTableColumn
bstunGroupUnroutableReceive = _BstunGroupUnroutableReceive_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 35, 1, 2, 1, 1, 5),
    _BstunGroupUnroutableReceive_Type()
)
bstunGroupUnroutableReceive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bstunGroupUnroutableReceive.setStatus("current")
_BstunPorts_ObjectIdentity = ObjectIdentity
bstunPorts = _BstunPorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 35, 1, 3)
)
_BstunPortTable_Object = MibTable
bstunPortTable = _BstunPortTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 35, 1, 3, 1)
)
if mibBuilder.loadTexts:
    bstunPortTable.setStatus("current")
_BstunPortEntry_Object = MibTableRow
bstunPortEntry = _BstunPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 35, 1, 3, 1, 1)
)
bstunPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    bstunPortEntry.setStatus("current")


class _BstunPortGroupNumber_Type(Integer32):
    """Custom type bstunPortGroupNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_BstunPortGroupNumber_Type.__name__ = "Integer32"
_BstunPortGroupNumber_Object = MibTableColumn
bstunPortGroupNumber = _BstunPortGroupNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 35, 1, 3, 1, 1, 1),
    _BstunPortGroupNumber_Type()
)
bstunPortGroupNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bstunPortGroupNumber.setStatus("current")


class _BstunPortDefaultPeerType_Type(Integer32):
    """Custom type bstunPortDefaultPeerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("ip", 2),
          ("none", 1),
          ("serial", 3),
          ("serialDirect", 4),
          ("serialFrameRelay", 5),
          ("serialLLC2", 6))
    )


_BstunPortDefaultPeerType_Type.__name__ = "Integer32"
_BstunPortDefaultPeerType_Object = MibTableColumn
bstunPortDefaultPeerType = _BstunPortDefaultPeerType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 35, 1, 3, 1, 1, 2),
    _BstunPortDefaultPeerType_Type()
)
bstunPortDefaultPeerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bstunPortDefaultPeerType.setStatus("current")
_BstunPortDefaultPeerIP_Type = IpAddress
_BstunPortDefaultPeerIP_Object = MibTableColumn
bstunPortDefaultPeerIP = _BstunPortDefaultPeerIP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 35, 1, 3, 1, 1, 3),
    _BstunPortDefaultPeerIP_Type()
)
bstunPortDefaultPeerIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bstunPortDefaultPeerIP.setStatus("current")
_BstunPortDefaultPeerSerial_Type = InterfaceIndex
_BstunPortDefaultPeerSerial_Object = MibTableColumn
bstunPortDefaultPeerSerial = _BstunPortDefaultPeerSerial_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 35, 1, 3, 1, 1, 4),
    _BstunPortDefaultPeerSerial_Type()
)
bstunPortDefaultPeerSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bstunPortDefaultPeerSerial.setStatus("current")
_BstunRoutes_ObjectIdentity = ObjectIdentity
bstunRoutes = _BstunRoutes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 35, 1, 4)
)
_BstunRouteTable_Object = MibTable
bstunRouteTable = _BstunRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 35, 1, 4, 1)
)
if mibBuilder.loadTexts:
    bstunRouteTable.setStatus("current")
_BstunRouteEntry_Object = MibTableRow
bstunRouteEntry = _BstunRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 35, 1, 4, 1, 1)
)
bstunRouteEntry.setIndexNames(
    (0, "CISCO-BSTUN-MIB", "bstunRouteGroupIndex"),
    (0, "CISCO-BSTUN-MIB", "bstunRouteStationAddress"),
)
if mibBuilder.loadTexts:
    bstunRouteEntry.setStatus("current")


class _BstunRouteGroupIndex_Type(Integer32):
    """Custom type bstunRouteGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_BstunRouteGroupIndex_Type.__name__ = "Integer32"
_BstunRouteGroupIndex_Object = MibTableColumn
bstunRouteGroupIndex = _BstunRouteGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 35, 1, 4, 1, 1, 1),
    _BstunRouteGroupIndex_Type()
)
bstunRouteGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bstunRouteGroupIndex.setStatus("current")


class _BstunRouteStationAddress_Type(Integer32):
    """Custom type bstunRouteStationAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_BstunRouteStationAddress_Type.__name__ = "Integer32"
_BstunRouteStationAddress_Object = MibTableColumn
bstunRouteStationAddress = _BstunRouteStationAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 35, 1, 4, 1, 1, 2),
    _BstunRouteStationAddress_Type()
)
bstunRouteStationAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bstunRouteStationAddress.setStatus("current")


class _BstunRouteType_Type(Integer32):
    """Custom type bstunRouteType based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("apip", 8),
          ("bip", 7),
          ("ip", 2),
          ("none", 1),
          ("serial", 3),
          ("serialDirect", 4),
          ("serialFrameRelay", 5),
          ("serialLLC2", 6))
    )


_BstunRouteType_Type.__name__ = "Integer32"
_BstunRouteType_Object = MibTableColumn
bstunRouteType = _BstunRouteType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 35, 1, 4, 1, 1, 3),
    _BstunRouteType_Type()
)
bstunRouteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bstunRouteType.setStatus("current")
_BstunRouteIP_Type = IpAddress
_BstunRouteIP_Object = MibTableColumn
bstunRouteIP = _BstunRouteIP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 35, 1, 4, 1, 1, 4),
    _BstunRouteIP_Type()
)
bstunRouteIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bstunRouteIP.setStatus("current")
_BstunRouteSerial_Type = InterfaceIndex
_BstunRouteSerial_Object = MibTableColumn
bstunRouteSerial = _BstunRouteSerial_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 35, 1, 4, 1, 1, 5),
    _BstunRouteSerial_Type()
)
bstunRouteSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bstunRouteSerial.setStatus("current")


class _BstunRoutePriority_Type(Integer32):
    """Custom type bstunRoutePriority based on Integer32"""
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
        *(("high", 4),
          ("low", 1),
          ("medium", 3),
          ("normal", 2))
    )


_BstunRoutePriority_Type.__name__ = "Integer32"
_BstunRoutePriority_Object = MibTableColumn
bstunRoutePriority = _BstunRoutePriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 35, 1, 4, 1, 1, 6),
    _BstunRoutePriority_Type()
)
bstunRoutePriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bstunRoutePriority.setStatus("current")


class _BstunRoutePeerState_Type(Integer32):
    """Custom type bstunRoutePeerState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("closed", 2),
          ("connected", 5),
          ("dead", 1),
          ("direct", 6),
          ("openWait", 4),
          ("opening", 3))
    )


_BstunRoutePeerState_Type.__name__ = "Integer32"
_BstunRoutePeerState_Object = MibTableColumn
bstunRoutePeerState = _BstunRoutePeerState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 35, 1, 4, 1, 1, 7),
    _BstunRoutePeerState_Type()
)
bstunRoutePeerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bstunRoutePeerState.setStatus("current")
_BstunRouteRxPackets_Type = Counter32
_BstunRouteRxPackets_Object = MibTableColumn
bstunRouteRxPackets = _BstunRouteRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 35, 1, 4, 1, 1, 8),
    _BstunRouteRxPackets_Type()
)
bstunRouteRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bstunRouteRxPackets.setStatus("current")
_BstunRouteTxPackets_Type = Counter32
_BstunRouteTxPackets_Object = MibTableColumn
bstunRouteTxPackets = _BstunRouteTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 35, 1, 4, 1, 1, 9),
    _BstunRouteTxPackets_Type()
)
bstunRouteTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bstunRouteTxPackets.setStatus("current")
_BstunRouteRxBytes_Type = Counter32
_BstunRouteRxBytes_Object = MibTableColumn
bstunRouteRxBytes = _BstunRouteRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 35, 1, 4, 1, 1, 10),
    _BstunRouteRxBytes_Type()
)
bstunRouteRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bstunRouteRxBytes.setStatus("current")
_BstunRouteTxBytes_Type = Counter32
_BstunRouteTxBytes_Object = MibTableColumn
bstunRouteTxBytes = _BstunRouteTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 35, 1, 4, 1, 1, 11),
    _BstunRouteTxBytes_Type()
)
bstunRouteTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bstunRouteTxBytes.setStatus("current")


class _BstunRouteDLCI_Type(Integer32):
    """Custom type bstunRouteDLCI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1007),
    )


_BstunRouteDLCI_Type.__name__ = "Integer32"
_BstunRouteDLCI_Object = MibTableColumn
bstunRouteDLCI = _BstunRouteDLCI_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 35, 1, 4, 1, 1, 12),
    _BstunRouteDLCI_Type()
)
bstunRouteDLCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bstunRouteDLCI.setStatus("current")


class _BstunRouteRSAP_Type(Integer32):
    """Custom type bstunRouteRSAP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_BstunRouteRSAP_Type.__name__ = "Integer32"
_BstunRouteRSAP_Object = MibTableColumn
bstunRouteRSAP = _BstunRouteRSAP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 35, 1, 4, 1, 1, 13),
    _BstunRouteRSAP_Type()
)
bstunRouteRSAP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bstunRouteRSAP.setStatus("current")


class _BstunLLC2Priority_Type(Integer32):
    """Custom type bstunLLC2Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_BstunLLC2Priority_Type.__name__ = "Integer32"
_BstunLLC2Priority_Object = MibTableColumn
bstunLLC2Priority = _BstunLLC2Priority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 35, 1, 4, 1, 1, 14),
    _BstunLLC2Priority_Type()
)
bstunLLC2Priority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bstunLLC2Priority.setStatus("current")


class _BstunRouteBIPPassive_Type(TruthValue):
    """Custom type bstunRouteBIPPassive based on TruthValue"""


_BstunRouteBIPPassive_Object = MibTableColumn
bstunRouteBIPPassive = _BstunRouteBIPPassive_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 35, 1, 4, 1, 1, 15),
    _BstunRouteBIPPassive_Type()
)
bstunRouteBIPPassive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bstunRouteBIPPassive.setStatus("current")


class _BstunRouteBIPLocalPort_Type(Integer32):
    """Custom type bstunRouteBIPLocalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1025, 32000),
    )


_BstunRouteBIPLocalPort_Type.__name__ = "Integer32"
_BstunRouteBIPLocalPort_Object = MibTableColumn
bstunRouteBIPLocalPort = _BstunRouteBIPLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 35, 1, 4, 1, 1, 16),
    _BstunRouteBIPLocalPort_Type()
)
bstunRouteBIPLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bstunRouteBIPLocalPort.setStatus("current")


class _BstunRouteBIPForeignPort_Type(Integer32):
    """Custom type bstunRouteBIPForeignPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1025, 32000),
    )


_BstunRouteBIPForeignPort_Type.__name__ = "Integer32"
_BstunRouteBIPForeignPort_Object = MibTableColumn
bstunRouteBIPForeignPort = _BstunRouteBIPForeignPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 35, 1, 4, 1, 1, 17),
    _BstunRouteBIPForeignPort_Type()
)
bstunRouteBIPForeignPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bstunRouteBIPForeignPort.setStatus("current")


class _BstunRouteBIPDeviceStatus_Type(Bits):
    """Custom type bstunRouteBIPDeviceStatus based on Bits"""
    namedValues = NamedValues(
        *(("commandreject", 5),
          ("datacheck", 2),
          ("deviceactive", 7),
          ("devicebusy", 11),
          ("deviceend", 9),
          ("deviceinactive", 6),
          ("equipmentcheck", 3),
          ("interventionrequired", 4),
          ("operationcheck", 0),
          ("reservedBit1", 1),
          ("reservedBit8", 8),
          ("unitspecify", 10))
    )

_BstunRouteBIPDeviceStatus_Type.__name__ = "Bits"
_BstunRouteBIPDeviceStatus_Object = MibTableColumn
bstunRouteBIPDeviceStatus = _BstunRouteBIPDeviceStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 35, 1, 4, 1, 1, 18),
    _BstunRouteBIPDeviceStatus_Type()
)
bstunRouteBIPDeviceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bstunRouteBIPDeviceStatus.setStatus("current")


class _BstunRouteAPIPHeaderVersion_Type(Integer32):
    """Custom type bstunRouteAPIPHeaderVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("v0", 1),
          ("v1", 2),
          ("v2", 3))
    )


_BstunRouteAPIPHeaderVersion_Type.__name__ = "Integer32"
_BstunRouteAPIPHeaderVersion_Object = MibTableColumn
bstunRouteAPIPHeaderVersion = _BstunRouteAPIPHeaderVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 35, 1, 4, 1, 1, 19),
    _BstunRouteAPIPHeaderVersion_Type()
)
bstunRouteAPIPHeaderVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bstunRouteAPIPHeaderVersion.setStatus("current")
_BstunNotificationPrefix_ObjectIdentity = ObjectIdentity
bstunNotificationPrefix = _BstunNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 35, 2)
)
_BstunNotifications_ObjectIdentity = ObjectIdentity
bstunNotifications = _BstunNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 35, 2, 0)
)
_BstunMibConformance_ObjectIdentity = ObjectIdentity
bstunMibConformance = _BstunMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 35, 3)
)
_BstunMibCompliances_ObjectIdentity = ObjectIdentity
bstunMibCompliances = _BstunMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 35, 3, 1)
)
_BstunMibGroups_ObjectIdentity = ObjectIdentity
bstunMibGroups = _BstunMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 35, 3, 2)
)

# Managed Objects groups

bstunGlobalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 35, 3, 2, 1)
)
bstunGlobalGroup.setObjects(
    ("CISCO-BSTUN-MIB", "bstunIPAddr")
)
if mibBuilder.loadTexts:
    bstunGlobalGroup.setStatus("obsolete")

bstunGroupGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 35, 3, 2, 2)
)
bstunGroupGroup.setObjects(
      *(("CISCO-BSTUN-MIB", "bstunProtocolType"),
        ("CISCO-BSTUN-MIB", "bstunLocalAck"),
        ("CISCO-BSTUN-MIB", "bstunGroupUnroutableTransmit"),
        ("CISCO-BSTUN-MIB", "bstunGroupUnroutableReceive"))
)
if mibBuilder.loadTexts:
    bstunGroupGroup.setStatus("current")

bstunPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 35, 3, 2, 3)
)
bstunPortGroup.setObjects(
      *(("CISCO-BSTUN-MIB", "bstunPortGroupNumber"),
        ("CISCO-BSTUN-MIB", "bstunPortDefaultPeerType"),
        ("CISCO-BSTUN-MIB", "bstunPortDefaultPeerIP"),
        ("CISCO-BSTUN-MIB", "bstunPortDefaultPeerSerial"))
)
if mibBuilder.loadTexts:
    bstunPortGroup.setStatus("current")

bstunRouteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 35, 3, 2, 4)
)
bstunRouteGroup.setObjects(
      *(("CISCO-BSTUN-MIB", "bstunRouteType"),
        ("CISCO-BSTUN-MIB", "bstunRouteIP"),
        ("CISCO-BSTUN-MIB", "bstunRouteSerial"),
        ("CISCO-BSTUN-MIB", "bstunRoutePriority"),
        ("CISCO-BSTUN-MIB", "bstunRoutePeerState"),
        ("CISCO-BSTUN-MIB", "bstunRouteRxPackets"),
        ("CISCO-BSTUN-MIB", "bstunRouteTxPackets"),
        ("CISCO-BSTUN-MIB", "bstunRouteRxBytes"),
        ("CISCO-BSTUN-MIB", "bstunRouteTxBytes"))
)
if mibBuilder.loadTexts:
    bstunRouteGroup.setStatus("obsolete")

bstunGlobalGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 35, 3, 2, 5)
)
bstunGlobalGroupRev1.setObjects(
      *(("CISCO-BSTUN-MIB", "bstunIPAddr"),
        ("CISCO-BSTUN-MIB", "bstunLisnSap"),
        ("CISCO-BSTUN-MIB", "bstunPeerKeepaliveInterval"),
        ("CISCO-BSTUN-MIB", "bstunPeerKeepaliveLimit"))
)
if mibBuilder.loadTexts:
    bstunGlobalGroupRev1.setStatus("current")

bstunRouteGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 35, 3, 2, 6)
)
bstunRouteGroupRev1.setObjects(
      *(("CISCO-BSTUN-MIB", "bstunRouteType"),
        ("CISCO-BSTUN-MIB", "bstunRouteIP"),
        ("CISCO-BSTUN-MIB", "bstunRouteSerial"),
        ("CISCO-BSTUN-MIB", "bstunRoutePriority"),
        ("CISCO-BSTUN-MIB", "bstunRoutePeerState"),
        ("CISCO-BSTUN-MIB", "bstunRouteRxPackets"),
        ("CISCO-BSTUN-MIB", "bstunRouteTxPackets"),
        ("CISCO-BSTUN-MIB", "bstunRouteRxBytes"),
        ("CISCO-BSTUN-MIB", "bstunRouteTxBytes"),
        ("CISCO-BSTUN-MIB", "bstunRouteDLCI"),
        ("CISCO-BSTUN-MIB", "bstunRouteRSAP"),
        ("CISCO-BSTUN-MIB", "bstunLLC2Priority"))
)
if mibBuilder.loadTexts:
    bstunRouteGroupRev1.setStatus("current")

bstunRouteGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 35, 3, 2, 7)
)
bstunRouteGroupRev2.setObjects(
      *(("CISCO-BSTUN-MIB", "bstunRouteType"),
        ("CISCO-BSTUN-MIB", "bstunRouteIP"),
        ("CISCO-BSTUN-MIB", "bstunRouteSerial"),
        ("CISCO-BSTUN-MIB", "bstunRoutePriority"),
        ("CISCO-BSTUN-MIB", "bstunRoutePeerState"),
        ("CISCO-BSTUN-MIB", "bstunRouteRxPackets"),
        ("CISCO-BSTUN-MIB", "bstunRouteTxPackets"),
        ("CISCO-BSTUN-MIB", "bstunRouteRxBytes"),
        ("CISCO-BSTUN-MIB", "bstunRouteTxBytes"),
        ("CISCO-BSTUN-MIB", "bstunRouteDLCI"),
        ("CISCO-BSTUN-MIB", "bstunRouteRSAP"),
        ("CISCO-BSTUN-MIB", "bstunLLC2Priority"),
        ("CISCO-BSTUN-MIB", "bstunRouteBIPPassive"),
        ("CISCO-BSTUN-MIB", "bstunRouteBIPLocalPort"),
        ("CISCO-BSTUN-MIB", "bstunRouteBIPForeignPort"),
        ("CISCO-BSTUN-MIB", "bstunRouteBIPDeviceStatus"))
)
if mibBuilder.loadTexts:
    bstunRouteGroupRev2.setStatus("deprecated")

bstunRouteBipGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 35, 3, 2, 10)
)
bstunRouteBipGroup.setObjects(
      *(("CISCO-BSTUN-MIB", "bstunRouteBIPPassive"),
        ("CISCO-BSTUN-MIB", "bstunRouteBIPDeviceStatus"))
)
if mibBuilder.loadTexts:
    bstunRouteBipGroup.setStatus("current")

bstunRoutePortsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 35, 3, 2, 11)
)
bstunRoutePortsGroup.setObjects(
      *(("CISCO-BSTUN-MIB", "bstunRouteBIPLocalPort"),
        ("CISCO-BSTUN-MIB", "bstunRouteBIPForeignPort"))
)
if mibBuilder.loadTexts:
    bstunRoutePortsGroup.setStatus("current")

bstunRouteApipGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 35, 3, 2, 12)
)
bstunRouteApipGroup.setObjects(
    ("CISCO-BSTUN-MIB", "bstunRouteAPIPHeaderVersion")
)
if mibBuilder.loadTexts:
    bstunRouteApipGroup.setStatus("current")


# Notification objects

bstunPeerStateChangeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 35, 2, 0, 1)
)
bstunPeerStateChangeNotification.setObjects(
    ("CISCO-BSTUN-MIB", "bstunRoutePeerState")
)
if mibBuilder.loadTexts:
    bstunPeerStateChangeNotification.setStatus(
        "deprecated"
    )

bstunPeerStateChangeNotification2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 35, 2, 0, 2)
)
bstunPeerStateChangeNotification2.setObjects(
      *(("CISCO-BSTUN-MIB", "bstunRoutePeerState"),
        ("CISCO-BSTUN-MIB", "bstunRouteType"),
        ("CISCO-BSTUN-MIB", "bstunRouteRxPackets"),
        ("CISCO-BSTUN-MIB", "bstunRouteTxPackets"))
)
if mibBuilder.loadTexts:
    bstunPeerStateChangeNotification2.setStatus(
        "current"
    )

bstunCUStatusChangeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 35, 2, 0, 3)
)
bstunCUStatusChangeNotification.setObjects(
      *(("CISCO-BSTUN-MIB", "bstunRouteIP"),
        ("CISCO-BSTUN-MIB", "bstunRouteBIPForeignPort"),
        ("CISCO-BSTUN-MIB", "bstunRouteBIPLocalPort"),
        ("CISCO-BSTUN-MIB", "bstunRouteBIPDeviceStatus"))
)
if mibBuilder.loadTexts:
    bstunCUStatusChangeNotification.setStatus(
        "current"
    )


# Notifications groups

bstunNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 35, 3, 2, 8)
)
bstunNotificationGroup.setObjects(
    ("CISCO-BSTUN-MIB", "bstunPeerStateChangeNotification")
)
if mibBuilder.loadTexts:
    bstunNotificationGroup.setStatus(
        "deprecated"
    )

bstunNotificationGroupRev1 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 35, 3, 2, 9)
)
bstunNotificationGroupRev1.setObjects(
      *(("CISCO-BSTUN-MIB", "bstunPeerStateChangeNotification2"),
        ("CISCO-BSTUN-MIB", "bstunCUStatusChangeNotification"))
)
if mibBuilder.loadTexts:
    bstunNotificationGroupRev1.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

bstunMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 35, 3, 1, 1)
)
if mibBuilder.loadTexts:
    bstunMibCompliance.setStatus(
        "obsolete"
    )

bstunMibComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 35, 3, 1, 2)
)
if mibBuilder.loadTexts:
    bstunMibComplianceRev1.setStatus(
        "obsolete"
    )

bstunMibComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 35, 3, 1, 3)
)
if mibBuilder.loadTexts:
    bstunMibComplianceRev2.setStatus(
        "deprecated"
    )

bstunMibComplianceRev3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 35, 3, 1, 4)
)
if mibBuilder.loadTexts:
    bstunMibComplianceRev3.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-BSTUN-MIB",
    **{"ciscoBstunMIB": ciscoBstunMIB,
       "bstunObjects": bstunObjects,
       "bstunGlobal": bstunGlobal,
       "bstunIPAddr": bstunIPAddr,
       "bstunLisnSap": bstunLisnSap,
       "bstunPeerKeepaliveInterval": bstunPeerKeepaliveInterval,
       "bstunPeerKeepaliveLimit": bstunPeerKeepaliveLimit,
       "bstunGroups": bstunGroups,
       "bstunGroupTable": bstunGroupTable,
       "bstunGroupEntry": bstunGroupEntry,
       "bstunGroupIndex": bstunGroupIndex,
       "bstunProtocolType": bstunProtocolType,
       "bstunLocalAck": bstunLocalAck,
       "bstunGroupUnroutableTransmit": bstunGroupUnroutableTransmit,
       "bstunGroupUnroutableReceive": bstunGroupUnroutableReceive,
       "bstunPorts": bstunPorts,
       "bstunPortTable": bstunPortTable,
       "bstunPortEntry": bstunPortEntry,
       "bstunPortGroupNumber": bstunPortGroupNumber,
       "bstunPortDefaultPeerType": bstunPortDefaultPeerType,
       "bstunPortDefaultPeerIP": bstunPortDefaultPeerIP,
       "bstunPortDefaultPeerSerial": bstunPortDefaultPeerSerial,
       "bstunRoutes": bstunRoutes,
       "bstunRouteTable": bstunRouteTable,
       "bstunRouteEntry": bstunRouteEntry,
       "bstunRouteGroupIndex": bstunRouteGroupIndex,
       "bstunRouteStationAddress": bstunRouteStationAddress,
       "bstunRouteType": bstunRouteType,
       "bstunRouteIP": bstunRouteIP,
       "bstunRouteSerial": bstunRouteSerial,
       "bstunRoutePriority": bstunRoutePriority,
       "bstunRoutePeerState": bstunRoutePeerState,
       "bstunRouteRxPackets": bstunRouteRxPackets,
       "bstunRouteTxPackets": bstunRouteTxPackets,
       "bstunRouteRxBytes": bstunRouteRxBytes,
       "bstunRouteTxBytes": bstunRouteTxBytes,
       "bstunRouteDLCI": bstunRouteDLCI,
       "bstunRouteRSAP": bstunRouteRSAP,
       "bstunLLC2Priority": bstunLLC2Priority,
       "bstunRouteBIPPassive": bstunRouteBIPPassive,
       "bstunRouteBIPLocalPort": bstunRouteBIPLocalPort,
       "bstunRouteBIPForeignPort": bstunRouteBIPForeignPort,
       "bstunRouteBIPDeviceStatus": bstunRouteBIPDeviceStatus,
       "bstunRouteAPIPHeaderVersion": bstunRouteAPIPHeaderVersion,
       "bstunNotificationPrefix": bstunNotificationPrefix,
       "bstunNotifications": bstunNotifications,
       "bstunPeerStateChangeNotification": bstunPeerStateChangeNotification,
       "bstunPeerStateChangeNotification2": bstunPeerStateChangeNotification2,
       "bstunCUStatusChangeNotification": bstunCUStatusChangeNotification,
       "bstunMibConformance": bstunMibConformance,
       "bstunMibCompliances": bstunMibCompliances,
       "bstunMibCompliance": bstunMibCompliance,
       "bstunMibComplianceRev1": bstunMibComplianceRev1,
       "bstunMibComplianceRev2": bstunMibComplianceRev2,
       "bstunMibComplianceRev3": bstunMibComplianceRev3,
       "bstunMibGroups": bstunMibGroups,
       "bstunGlobalGroup": bstunGlobalGroup,
       "bstunGroupGroup": bstunGroupGroup,
       "bstunPortGroup": bstunPortGroup,
       "bstunRouteGroup": bstunRouteGroup,
       "bstunGlobalGroupRev1": bstunGlobalGroupRev1,
       "bstunRouteGroupRev1": bstunRouteGroupRev1,
       "bstunRouteGroupRev2": bstunRouteGroupRev2,
       "bstunNotificationGroup": bstunNotificationGroup,
       "bstunNotificationGroupRev1": bstunNotificationGroupRev1,
       "bstunRouteBipGroup": bstunRouteBipGroup,
       "bstunRoutePortsGroup": bstunRoutePortsGroup,
       "bstunRouteApipGroup": bstunRouteApipGroup}
)
