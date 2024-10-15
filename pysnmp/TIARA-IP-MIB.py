# SNMP MIB module (TIARA-IP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TIARA-IP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:01:36 2024
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

(tiaraMgmt,) = mibBuilder.importSymbols(
    "TIARA-NETWORKS-SMI",
    "tiaraMgmt")


# MODULE-IDENTITY

tiaraIpMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3174, 2, 23)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TiaraIpRoutingEnable_Type = TruthValue
_TiaraIpRoutingEnable_Object = MibScalar
tiaraIpRoutingEnable = _TiaraIpRoutingEnable_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 23, 1),
    _TiaraIpRoutingEnable_Type()
)
tiaraIpRoutingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tiaraIpRoutingEnable.setStatus("current")
_TiaraIpIfTable_Object = MibTable
tiaraIpIfTable = _TiaraIpIfTable_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 23, 2)
)
if mibBuilder.loadTexts:
    tiaraIpIfTable.setStatus("current")
_TiaraIpIfTableEntry_Object = MibTableRow
tiaraIpIfTableEntry = _TiaraIpIfTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 23, 2, 1)
)
tiaraIpIfTableEntry.setIndexNames(
    (0, "TIARA-IP-MIB", "tiaraIpIfIndex"),
)
if mibBuilder.loadTexts:
    tiaraIpIfTableEntry.setStatus("current")
_TiaraIpIfIndex_Type = Integer32
_TiaraIpIfIndex_Object = MibTableColumn
tiaraIpIfIndex = _TiaraIpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 23, 2, 1, 1),
    _TiaraIpIfIndex_Type()
)
tiaraIpIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tiaraIpIfIndex.setStatus("current")
_TiaraIpIfName_Type = DisplayString
_TiaraIpIfName_Object = MibTableColumn
tiaraIpIfName = _TiaraIpIfName_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 23, 2, 1, 2),
    _TiaraIpIfName_Type()
)
tiaraIpIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tiaraIpIfName.setStatus("current")
_TiaraIpIfAddr_Type = IpAddress
_TiaraIpIfAddr_Object = MibTableColumn
tiaraIpIfAddr = _TiaraIpIfAddr_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 23, 2, 1, 3),
    _TiaraIpIfAddr_Type()
)
tiaraIpIfAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tiaraIpIfAddr.setStatus("current")
_TiaraIpIfMask_Type = IpAddress
_TiaraIpIfMask_Object = MibTableColumn
tiaraIpIfMask = _TiaraIpIfMask_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 23, 2, 1, 4),
    _TiaraIpIfMask_Type()
)
tiaraIpIfMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tiaraIpIfMask.setStatus("current")
_TiaraIpIfPeerAddr_Type = IpAddress
_TiaraIpIfPeerAddr_Object = MibTableColumn
tiaraIpIfPeerAddr = _TiaraIpIfPeerAddr_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 23, 2, 1, 5),
    _TiaraIpIfPeerAddr_Type()
)
tiaraIpIfPeerAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tiaraIpIfPeerAddr.setStatus("current")


class _TiaraIpIfType_Type(Integer32):
    """Custom type tiaraIpIfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 1),
          ("wan", 2))
    )


_TiaraIpIfType_Type.__name__ = "Integer32"
_TiaraIpIfType_Object = MibTableColumn
tiaraIpIfType = _TiaraIpIfType_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 23, 2, 1, 6),
    _TiaraIpIfType_Type()
)
tiaraIpIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tiaraIpIfType.setStatus("current")
_TiaraStaticRouteTable_Object = MibTable
tiaraStaticRouteTable = _TiaraStaticRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 23, 3)
)
if mibBuilder.loadTexts:
    tiaraStaticRouteTable.setStatus("current")
_TiaraStaticRouteEntry_Object = MibTableRow
tiaraStaticRouteEntry = _TiaraStaticRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 23, 3, 1)
)
tiaraStaticRouteEntry.setIndexNames(
    (0, "TIARA-IP-MIB", "tiaraStaticRouteIndex"),
)
if mibBuilder.loadTexts:
    tiaraStaticRouteEntry.setStatus("current")
_TiaraStaticRouteIndex_Type = Integer32
_TiaraStaticRouteIndex_Object = MibTableColumn
tiaraStaticRouteIndex = _TiaraStaticRouteIndex_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 23, 3, 1, 1),
    _TiaraStaticRouteIndex_Type()
)
tiaraStaticRouteIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tiaraStaticRouteIndex.setStatus("current")
_TiaraStaticRouteNetworkAddr_Type = IpAddress
_TiaraStaticRouteNetworkAddr_Object = MibTableColumn
tiaraStaticRouteNetworkAddr = _TiaraStaticRouteNetworkAddr_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 23, 3, 1, 2),
    _TiaraStaticRouteNetworkAddr_Type()
)
tiaraStaticRouteNetworkAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tiaraStaticRouteNetworkAddr.setStatus("current")
_TiaraStaticRouteNetworkMask_Type = IpAddress
_TiaraStaticRouteNetworkMask_Object = MibTableColumn
tiaraStaticRouteNetworkMask = _TiaraStaticRouteNetworkMask_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 23, 3, 1, 3),
    _TiaraStaticRouteNetworkMask_Type()
)
tiaraStaticRouteNetworkMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tiaraStaticRouteNetworkMask.setStatus("current")
_TiaraStaticRouteGatewayAddr_Type = DisplayString
_TiaraStaticRouteGatewayAddr_Object = MibTableColumn
tiaraStaticRouteGatewayAddr = _TiaraStaticRouteGatewayAddr_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 23, 3, 1, 4),
    _TiaraStaticRouteGatewayAddr_Type()
)
tiaraStaticRouteGatewayAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tiaraStaticRouteGatewayAddr.setStatus("current")


class _TiaraStaticRouteNoOfHops_Type(Integer32):
    """Custom type tiaraStaticRouteNoOfHops based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_TiaraStaticRouteNoOfHops_Type.__name__ = "Integer32"
_TiaraStaticRouteNoOfHops_Object = MibTableColumn
tiaraStaticRouteNoOfHops = _TiaraStaticRouteNoOfHops_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 23, 3, 1, 5),
    _TiaraStaticRouteNoOfHops_Type()
)
tiaraStaticRouteNoOfHops.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tiaraStaticRouteNoOfHops.setStatus("current")
_TiaraStaticRouteRowStatus_Type = RowStatus
_TiaraStaticRouteRowStatus_Object = MibTableColumn
tiaraStaticRouteRowStatus = _TiaraStaticRouteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 23, 3, 1, 6),
    _TiaraStaticRouteRowStatus_Type()
)
tiaraStaticRouteRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tiaraStaticRouteRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIARA-IP-MIB",
    **{"tiaraIpMib": tiaraIpMib,
       "tiaraIpRoutingEnable": tiaraIpRoutingEnable,
       "tiaraIpIfTable": tiaraIpIfTable,
       "tiaraIpIfTableEntry": tiaraIpIfTableEntry,
       "tiaraIpIfIndex": tiaraIpIfIndex,
       "tiaraIpIfName": tiaraIpIfName,
       "tiaraIpIfAddr": tiaraIpIfAddr,
       "tiaraIpIfMask": tiaraIpIfMask,
       "tiaraIpIfPeerAddr": tiaraIpIfPeerAddr,
       "tiaraIpIfType": tiaraIpIfType,
       "tiaraStaticRouteTable": tiaraStaticRouteTable,
       "tiaraStaticRouteEntry": tiaraStaticRouteEntry,
       "tiaraStaticRouteIndex": tiaraStaticRouteIndex,
       "tiaraStaticRouteNetworkAddr": tiaraStaticRouteNetworkAddr,
       "tiaraStaticRouteNetworkMask": tiaraStaticRouteNetworkMask,
       "tiaraStaticRouteGatewayAddr": tiaraStaticRouteGatewayAddr,
       "tiaraStaticRouteNoOfHops": tiaraStaticRouteNoOfHops,
       "tiaraStaticRouteRowStatus": tiaraStaticRouteRowStatus}
)
