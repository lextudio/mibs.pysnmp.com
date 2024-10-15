# SNMP MIB module (RADLAN-UDP) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RADLAN-UDP
# Produced by pysmi-1.5.4 at Mon Oct 14 22:43:52 2024
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

(ipCidrRouteDest,
 ipCidrRouteEntry,
 ipCidrRouteMask,
 ipCidrRouteNextHop,
 ipCidrRouteTos) = mibBuilder.importSymbols(
    "IP-FORWARD-MIB",
    "ipCidrRouteDest",
    "ipCidrRouteEntry",
    "ipCidrRouteMask",
    "ipCidrRouteNextHop",
    "ipCidrRouteTos")

(ipAddrEntry,) = mibBuilder.importSymbols(
    "IP-MIB",
    "ipAddrEntry")

(rnd,) = mibBuilder.importSymbols(
    "RADLAN-MIB",
    "rnd")

(rip2IfConfEntry,) = mibBuilder.importSymbols(
    "RFC1389-MIB",
    "rip2IfConfEntry")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(DisplayString,) = mibBuilder.importSymbols(
    "SNMPv2-TC-v1",
    "DisplayString")


# MODULE-IDENTITY

rsUDP = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 89, 42)
)
rsUDP.setRevisions(
        ("2004-06-01 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RsUdpRelayTable_Object = MibTable
rsUdpRelayTable = _RsUdpRelayTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 42, 1)
)
if mibBuilder.loadTexts:
    rsUdpRelayTable.setStatus("current")
_RsUdpRelayEntry_Object = MibTableRow
rsUdpRelayEntry = _RsUdpRelayEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 42, 1, 1)
)
rsUdpRelayEntry.setIndexNames(
    (0, "RADLAN-UDP", "rsUdpRelayDstPort"),
    (0, "RADLAN-UDP", "rsUdpRelaySrcIpInf"),
    (0, "RADLAN-UDP", "rsUdpRelayDstIpAddr"),
)
if mibBuilder.loadTexts:
    rsUdpRelayEntry.setStatus("current")
_RsUdpRelayDstPort_Type = Integer32
_RsUdpRelayDstPort_Object = MibTableColumn
rsUdpRelayDstPort = _RsUdpRelayDstPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 42, 1, 1, 1),
    _RsUdpRelayDstPort_Type()
)
rsUdpRelayDstPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsUdpRelayDstPort.setStatus("current")
_RsUdpRelaySrcIpInf_Type = IpAddress
_RsUdpRelaySrcIpInf_Object = MibTableColumn
rsUdpRelaySrcIpInf = _RsUdpRelaySrcIpInf_Object(
    (1, 3, 6, 1, 4, 1, 89, 42, 1, 1, 2),
    _RsUdpRelaySrcIpInf_Type()
)
rsUdpRelaySrcIpInf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsUdpRelaySrcIpInf.setStatus("current")
_RsUdpRelayDstIpAddr_Type = IpAddress
_RsUdpRelayDstIpAddr_Object = MibTableColumn
rsUdpRelayDstIpAddr = _RsUdpRelayDstIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 42, 1, 1, 3),
    _RsUdpRelayDstIpAddr_Type()
)
rsUdpRelayDstIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsUdpRelayDstIpAddr.setStatus("current")
_RsUdpRelayStatus_Type = RowStatus
_RsUdpRelayStatus_Object = MibTableColumn
rsUdpRelayStatus = _RsUdpRelayStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 42, 1, 1, 4),
    _RsUdpRelayStatus_Type()
)
rsUdpRelayStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsUdpRelayStatus.setStatus("current")


class _RsUdpRelayUserInfo_Type(Integer32):
    """Custom type rsUdpRelayUserInfo based on Integer32"""
    defaultValue = 0


_RsUdpRelayUserInfo_Object = MibTableColumn
rsUdpRelayUserInfo = _RsUdpRelayUserInfo_Object(
    (1, 3, 6, 1, 4, 1, 89, 42, 1, 1, 5),
    _RsUdpRelayUserInfo_Type()
)
rsUdpRelayUserInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsUdpRelayUserInfo.setStatus("current")
_RsUdpRelayMibVersion_Type = Integer32
_RsUdpRelayMibVersion_Object = MibScalar
rsUdpRelayMibVersion = _RsUdpRelayMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 89, 42, 2),
    _RsUdpRelayMibVersion_Type()
)
rsUdpRelayMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsUdpRelayMibVersion.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RADLAN-UDP",
    **{"rsUDP": rsUDP,
       "rsUdpRelayTable": rsUdpRelayTable,
       "rsUdpRelayEntry": rsUdpRelayEntry,
       "rsUdpRelayDstPort": rsUdpRelayDstPort,
       "rsUdpRelaySrcIpInf": rsUdpRelaySrcIpInf,
       "rsUdpRelayDstIpAddr": rsUdpRelayDstIpAddr,
       "rsUdpRelayStatus": rsUdpRelayStatus,
       "rsUdpRelayUserInfo": rsUdpRelayUserInfo,
       "rsUdpRelayMibVersion": rsUdpRelayMibVersion}
)
