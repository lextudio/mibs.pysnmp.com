# SNMP MIB module (RFC1269-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RFC1269-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:47:16 2024
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
 NotificationType,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "iso",
    "mib-2")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Bgp_ObjectIdentity = ObjectIdentity
bgp = _Bgp_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 15)
)
_BgpVersion_Type = OctetString
_BgpVersion_Object = MibScalar
bgpVersion = _BgpVersion_Object(
    (1, 3, 6, 1, 2, 1, 15, 1),
    _BgpVersion_Type()
)
bgpVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpVersion.setStatus("mandatory")


class _BgpLocalAs_Type(Integer32):
    """Custom type bgpLocalAs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BgpLocalAs_Type.__name__ = "Integer32"
_BgpLocalAs_Object = MibScalar
bgpLocalAs = _BgpLocalAs_Object(
    (1, 3, 6, 1, 2, 1, 15, 2),
    _BgpLocalAs_Type()
)
bgpLocalAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpLocalAs.setStatus("mandatory")
_BgpPeerTable_Object = MibTable
bgpPeerTable = _BgpPeerTable_Object(
    (1, 3, 6, 1, 2, 1, 15, 3)
)
if mibBuilder.loadTexts:
    bgpPeerTable.setStatus("mandatory")
_BgpPeerEntry_Object = MibTableRow
bgpPeerEntry = _BgpPeerEntry_Object(
    (1, 3, 6, 1, 2, 1, 15, 3, 1)
)
bgpPeerEntry.setIndexNames(
    (0, "RFC1269-MIB", "bgpPeerRemoteAddr"),
)
if mibBuilder.loadTexts:
    bgpPeerEntry.setStatus("mandatory")
_BgpPeerIdentifier_Type = IpAddress
_BgpPeerIdentifier_Object = MibTableColumn
bgpPeerIdentifier = _BgpPeerIdentifier_Object(
    (1, 3, 6, 1, 2, 1, 15, 3, 1, 1),
    _BgpPeerIdentifier_Type()
)
bgpPeerIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPeerIdentifier.setStatus("mandatory")


class _BgpPeerState_Type(Integer32):
    """Custom type bgpPeerState based on Integer32"""
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
        *(("active", 3),
          ("connect", 2),
          ("established", 6),
          ("idle", 1),
          ("openconfirm", 5),
          ("opensent", 4))
    )


_BgpPeerState_Type.__name__ = "Integer32"
_BgpPeerState_Object = MibTableColumn
bgpPeerState = _BgpPeerState_Object(
    (1, 3, 6, 1, 2, 1, 15, 3, 1, 2),
    _BgpPeerState_Type()
)
bgpPeerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPeerState.setStatus("mandatory")
_BgpPeerAdminStatus_Type = Integer32
_BgpPeerAdminStatus_Object = MibTableColumn
bgpPeerAdminStatus = _BgpPeerAdminStatus_Object(
    (1, 3, 6, 1, 2, 1, 15, 3, 1, 3),
    _BgpPeerAdminStatus_Type()
)
bgpPeerAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bgpPeerAdminStatus.setStatus("mandatory")
_BgpPeerNegotiatedVersion_Type = Integer32
_BgpPeerNegotiatedVersion_Object = MibTableColumn
bgpPeerNegotiatedVersion = _BgpPeerNegotiatedVersion_Object(
    (1, 3, 6, 1, 2, 1, 15, 3, 1, 4),
    _BgpPeerNegotiatedVersion_Type()
)
bgpPeerNegotiatedVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPeerNegotiatedVersion.setStatus("mandatory")
_BgpPeerLocalAddr_Type = IpAddress
_BgpPeerLocalAddr_Object = MibTableColumn
bgpPeerLocalAddr = _BgpPeerLocalAddr_Object(
    (1, 3, 6, 1, 2, 1, 15, 3, 1, 5),
    _BgpPeerLocalAddr_Type()
)
bgpPeerLocalAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPeerLocalAddr.setStatus("mandatory")


class _BgpPeerLocalPort_Type(Integer32):
    """Custom type bgpPeerLocalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BgpPeerLocalPort_Type.__name__ = "Integer32"
_BgpPeerLocalPort_Object = MibTableColumn
bgpPeerLocalPort = _BgpPeerLocalPort_Object(
    (1, 3, 6, 1, 2, 1, 15, 3, 1, 6),
    _BgpPeerLocalPort_Type()
)
bgpPeerLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPeerLocalPort.setStatus("mandatory")
_BgpPeerRemoteAddr_Type = IpAddress
_BgpPeerRemoteAddr_Object = MibTableColumn
bgpPeerRemoteAddr = _BgpPeerRemoteAddr_Object(
    (1, 3, 6, 1, 2, 1, 15, 3, 1, 7),
    _BgpPeerRemoteAddr_Type()
)
bgpPeerRemoteAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPeerRemoteAddr.setStatus("mandatory")


class _BgpPeerRemotePort_Type(Integer32):
    """Custom type bgpPeerRemotePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BgpPeerRemotePort_Type.__name__ = "Integer32"
_BgpPeerRemotePort_Object = MibTableColumn
bgpPeerRemotePort = _BgpPeerRemotePort_Object(
    (1, 3, 6, 1, 2, 1, 15, 3, 1, 8),
    _BgpPeerRemotePort_Type()
)
bgpPeerRemotePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPeerRemotePort.setStatus("mandatory")


class _BgpPeerRemoteAs_Type(Integer32):
    """Custom type bgpPeerRemoteAs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BgpPeerRemoteAs_Type.__name__ = "Integer32"
_BgpPeerRemoteAs_Object = MibTableColumn
bgpPeerRemoteAs = _BgpPeerRemoteAs_Object(
    (1, 3, 6, 1, 2, 1, 15, 3, 1, 9),
    _BgpPeerRemoteAs_Type()
)
bgpPeerRemoteAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPeerRemoteAs.setStatus("mandatory")
_BgpPeerInUpdates_Type = Counter32
_BgpPeerInUpdates_Object = MibTableColumn
bgpPeerInUpdates = _BgpPeerInUpdates_Object(
    (1, 3, 6, 1, 2, 1, 15, 3, 1, 10),
    _BgpPeerInUpdates_Type()
)
bgpPeerInUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPeerInUpdates.setStatus("mandatory")
_BgpPeerOutUpdates_Type = Counter32
_BgpPeerOutUpdates_Object = MibTableColumn
bgpPeerOutUpdates = _BgpPeerOutUpdates_Object(
    (1, 3, 6, 1, 2, 1, 15, 3, 1, 11),
    _BgpPeerOutUpdates_Type()
)
bgpPeerOutUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPeerOutUpdates.setStatus("mandatory")
_BgpPeerInTotalMessages_Type = Counter32
_BgpPeerInTotalMessages_Object = MibTableColumn
bgpPeerInTotalMessages = _BgpPeerInTotalMessages_Object(
    (1, 3, 6, 1, 2, 1, 15, 3, 1, 12),
    _BgpPeerInTotalMessages_Type()
)
bgpPeerInTotalMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPeerInTotalMessages.setStatus("mandatory")
_BgpPeerOutTotalMessages_Type = Counter32
_BgpPeerOutTotalMessages_Object = MibTableColumn
bgpPeerOutTotalMessages = _BgpPeerOutTotalMessages_Object(
    (1, 3, 6, 1, 2, 1, 15, 3, 1, 13),
    _BgpPeerOutTotalMessages_Type()
)
bgpPeerOutTotalMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPeerOutTotalMessages.setStatus("mandatory")


class _BgpPeerLastError_Type(OctetString):
    """Custom type bgpPeerLastError based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_BgpPeerLastError_Type.__name__ = "OctetString"
_BgpPeerLastError_Object = MibTableColumn
bgpPeerLastError = _BgpPeerLastError_Object(
    (1, 3, 6, 1, 2, 1, 15, 3, 1, 14),
    _BgpPeerLastError_Type()
)
bgpPeerLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPeerLastError.setStatus("mandatory")
_BgpIdentifier_Type = IpAddress
_BgpIdentifier_Object = MibScalar
bgpIdentifier = _BgpIdentifier_Object(
    (1, 3, 6, 1, 2, 1, 15, 4),
    _BgpIdentifier_Type()
)
bgpIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpIdentifier.setStatus("mandatory")
_BgpRcvdPathAttrTable_Object = MibTable
bgpRcvdPathAttrTable = _BgpRcvdPathAttrTable_Object(
    (1, 3, 6, 1, 2, 1, 15, 5)
)
if mibBuilder.loadTexts:
    bgpRcvdPathAttrTable.setStatus("mandatory")
_BgpPathAttrEntry_Object = MibTableRow
bgpPathAttrEntry = _BgpPathAttrEntry_Object(
    (1, 3, 6, 1, 2, 1, 15, 5, 1)
)
bgpPathAttrEntry.setIndexNames(
    (0, "RFC1269-MIB", "bgpPathAttrDestNetwork"),
    (0, "RFC1269-MIB", "bgpPathAttrPeer"),
)
if mibBuilder.loadTexts:
    bgpPathAttrEntry.setStatus("mandatory")
_BgpPathAttrPeer_Type = IpAddress
_BgpPathAttrPeer_Object = MibTableColumn
bgpPathAttrPeer = _BgpPathAttrPeer_Object(
    (1, 3, 6, 1, 2, 1, 15, 5, 1, 1),
    _BgpPathAttrPeer_Type()
)
bgpPathAttrPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPathAttrPeer.setStatus("mandatory")
_BgpPathAttrDestNetwork_Type = IpAddress
_BgpPathAttrDestNetwork_Object = MibTableColumn
bgpPathAttrDestNetwork = _BgpPathAttrDestNetwork_Object(
    (1, 3, 6, 1, 2, 1, 15, 5, 1, 2),
    _BgpPathAttrDestNetwork_Type()
)
bgpPathAttrDestNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPathAttrDestNetwork.setStatus("mandatory")


class _BgpPathAttrOrigin_Type(Integer32):
    """Custom type bgpPathAttrOrigin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("egp", 2),
          ("igp", 1),
          ("incomplete", 3))
    )


_BgpPathAttrOrigin_Type.__name__ = "Integer32"
_BgpPathAttrOrigin_Object = MibTableColumn
bgpPathAttrOrigin = _BgpPathAttrOrigin_Object(
    (1, 3, 6, 1, 2, 1, 15, 5, 1, 3),
    _BgpPathAttrOrigin_Type()
)
bgpPathAttrOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPathAttrOrigin.setStatus("mandatory")
_BgpPathAttrASPath_Type = OctetString
_BgpPathAttrASPath_Object = MibTableColumn
bgpPathAttrASPath = _BgpPathAttrASPath_Object(
    (1, 3, 6, 1, 2, 1, 15, 5, 1, 4),
    _BgpPathAttrASPath_Type()
)
bgpPathAttrASPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPathAttrASPath.setStatus("mandatory")
_BgpPathAttrNextHop_Type = IpAddress
_BgpPathAttrNextHop_Object = MibTableColumn
bgpPathAttrNextHop = _BgpPathAttrNextHop_Object(
    (1, 3, 6, 1, 2, 1, 15, 5, 1, 5),
    _BgpPathAttrNextHop_Type()
)
bgpPathAttrNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPathAttrNextHop.setStatus("mandatory")
_BgpPathAttrInterASMetric_Type = IpAddress
_BgpPathAttrInterASMetric_Object = MibTableColumn
bgpPathAttrInterASMetric = _BgpPathAttrInterASMetric_Object(
    (1, 3, 6, 1, 2, 1, 15, 5, 1, 6),
    _BgpPathAttrInterASMetric_Type()
)
bgpPathAttrInterASMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPathAttrInterASMetric.setStatus("mandatory")

# Managed Objects groups


# Notification objects

bgpEstablished = NotificationType(
    (1, 3, 6, 1, 2, 1, 15, 0, 1)
)
bgpEstablished.setObjects(
      *(("RFC1269-MIB", "bgpPeerRemoteAddr"),
        ("RFC1269-MIB", "bgpPeerLastError"),
        ("RFC1269-MIB", "bgpPeerState"))
)
if mibBuilder.loadTexts:
    bgpEstablished.setStatus(
        ""
    )

bgpBackwardTransition = NotificationType(
    (1, 3, 6, 1, 2, 1, 15, 0, 2)
)
bgpBackwardTransition.setObjects(
      *(("RFC1269-MIB", "bgpPeerRemoteAddr"),
        ("RFC1269-MIB", "bgpPeerLastError"),
        ("RFC1269-MIB", "bgpPeerState"))
)
if mibBuilder.loadTexts:
    bgpBackwardTransition.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RFC1269-MIB",
    **{"bgp": bgp,
       "bgpEstablished": bgpEstablished,
       "bgpBackwardTransition": bgpBackwardTransition,
       "bgpVersion": bgpVersion,
       "bgpLocalAs": bgpLocalAs,
       "bgpPeerTable": bgpPeerTable,
       "bgpPeerEntry": bgpPeerEntry,
       "bgpPeerIdentifier": bgpPeerIdentifier,
       "bgpPeerState": bgpPeerState,
       "bgpPeerAdminStatus": bgpPeerAdminStatus,
       "bgpPeerNegotiatedVersion": bgpPeerNegotiatedVersion,
       "bgpPeerLocalAddr": bgpPeerLocalAddr,
       "bgpPeerLocalPort": bgpPeerLocalPort,
       "bgpPeerRemoteAddr": bgpPeerRemoteAddr,
       "bgpPeerRemotePort": bgpPeerRemotePort,
       "bgpPeerRemoteAs": bgpPeerRemoteAs,
       "bgpPeerInUpdates": bgpPeerInUpdates,
       "bgpPeerOutUpdates": bgpPeerOutUpdates,
       "bgpPeerInTotalMessages": bgpPeerInTotalMessages,
       "bgpPeerOutTotalMessages": bgpPeerOutTotalMessages,
       "bgpPeerLastError": bgpPeerLastError,
       "bgpIdentifier": bgpIdentifier,
       "bgpRcvdPathAttrTable": bgpRcvdPathAttrTable,
       "bgpPathAttrEntry": bgpPathAttrEntry,
       "bgpPathAttrPeer": bgpPathAttrPeer,
       "bgpPathAttrDestNetwork": bgpPathAttrDestNetwork,
       "bgpPathAttrOrigin": bgpPathAttrOrigin,
       "bgpPathAttrASPath": bgpPathAttrASPath,
       "bgpPathAttrNextHop": bgpPathAttrNextHop,
       "bgpPathAttrInterASMetric": bgpPathAttrInterASMetric}
)
