# SNMP MIB module (CADANT-MPLS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CADANT-MPLS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:53:06 2024
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

(cadMpls,) = mibBuilder.importSymbols(
    "CADANT-PRODUCTS-MIB",
    "cadMpls")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 MacAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

cadMplsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 130, 1)
)
cadMplsMIB.setRevisions(
        ("2014-01-24 00:00",
         "2013-12-04 00:00",
         "2013-11-04 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CadMplsMIBObjects_ObjectIdentity = ObjectIdentity
cadMplsMIBObjects = _CadMplsMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 130, 1, 1)
)
_CadMplsParams_ObjectIdentity = ObjectIdentity
cadMplsParams = _CadMplsParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 130, 1, 1, 1)
)


class _CadMplsLdpHelloHoldTimer_Type(Unsigned32):
    """Custom type cadMplsLdpHelloHoldTimer based on Unsigned32"""
    defaultValue = 15

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CadMplsLdpHelloHoldTimer_Type.__name__ = "Unsigned32"
_CadMplsLdpHelloHoldTimer_Object = MibScalar
cadMplsLdpHelloHoldTimer = _CadMplsLdpHelloHoldTimer_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 130, 1, 1, 1, 1),
    _CadMplsLdpHelloHoldTimer_Type()
)
cadMplsLdpHelloHoldTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadMplsLdpHelloHoldTimer.setStatus("current")
if mibBuilder.loadTexts:
    cadMplsLdpHelloHoldTimer.setUnits("second")


class _CadMplsLdpTargetedHelloHoldTimer_Type(Unsigned32):
    """Custom type cadMplsLdpTargetedHelloHoldTimer based on Unsigned32"""
    defaultValue = 45

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CadMplsLdpTargetedHelloHoldTimer_Type.__name__ = "Unsigned32"
_CadMplsLdpTargetedHelloHoldTimer_Object = MibScalar
cadMplsLdpTargetedHelloHoldTimer = _CadMplsLdpTargetedHelloHoldTimer_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 130, 1, 1, 1, 2),
    _CadMplsLdpTargetedHelloHoldTimer_Type()
)
cadMplsLdpTargetedHelloHoldTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadMplsLdpTargetedHelloHoldTimer.setStatus("current")


class _CadMplsLdpKeepAliveHoldTimer_Type(Unsigned32):
    """Custom type cadMplsLdpKeepAliveHoldTimer based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CadMplsLdpKeepAliveHoldTimer_Type.__name__ = "Unsigned32"
_CadMplsLdpKeepAliveHoldTimer_Object = MibScalar
cadMplsLdpKeepAliveHoldTimer = _CadMplsLdpKeepAliveHoldTimer_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 130, 1, 1, 1, 3),
    _CadMplsLdpKeepAliveHoldTimer_Type()
)
cadMplsLdpKeepAliveHoldTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadMplsLdpKeepAliveHoldTimer.setStatus("current")


class _CadMplsLdpVcDescription_Type(DisplayString):
    """Custom type cadMplsLdpVcDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CadMplsLdpVcDescription_Type.__name__ = "DisplayString"
_CadMplsLdpVcDescription_Object = MibScalar
cadMplsLdpVcDescription = _CadMplsLdpVcDescription_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 130, 1, 1, 1, 4),
    _CadMplsLdpVcDescription_Type()
)
cadMplsLdpVcDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadMplsLdpVcDescription.setStatus("current")
_CadMplsLdpNeighborTable_Object = MibTable
cadMplsLdpNeighborTable = _CadMplsLdpNeighborTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 130, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cadMplsLdpNeighborTable.setStatus("current")
_CadMplsLdpNeighborEntry_Object = MibTableRow
cadMplsLdpNeighborEntry = _CadMplsLdpNeighborEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 130, 1, 1, 2, 1)
)
cadMplsLdpNeighborEntry.setIndexNames(
    (0, "CADANT-MPLS-MIB", "cadMplsLdpNeighborAddressType"),
    (0, "CADANT-MPLS-MIB", "cadMplsLdpNeighborIpAddress"),
)
if mibBuilder.loadTexts:
    cadMplsLdpNeighborEntry.setStatus("current")
_CadMplsLdpNeighborAddressType_Type = InetAddressType
_CadMplsLdpNeighborAddressType_Object = MibTableColumn
cadMplsLdpNeighborAddressType = _CadMplsLdpNeighborAddressType_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 130, 1, 1, 2, 1, 1),
    _CadMplsLdpNeighborAddressType_Type()
)
cadMplsLdpNeighborAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadMplsLdpNeighborAddressType.setStatus("current")
_CadMplsLdpNeighborIpAddress_Type = InetAddress
_CadMplsLdpNeighborIpAddress_Object = MibTableColumn
cadMplsLdpNeighborIpAddress = _CadMplsLdpNeighborIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 130, 1, 1, 2, 1, 2),
    _CadMplsLdpNeighborIpAddress_Type()
)
cadMplsLdpNeighborIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadMplsLdpNeighborIpAddress.setStatus("current")


class _CadMplsLdpNeighborPassword_Type(OctetString):
    """Custom type cadMplsLdpNeighborPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CadMplsLdpNeighborPassword_Type.__name__ = "OctetString"
_CadMplsLdpNeighborPassword_Object = MibTableColumn
cadMplsLdpNeighborPassword = _CadMplsLdpNeighborPassword_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 130, 1, 1, 2, 1, 3),
    _CadMplsLdpNeighborPassword_Type()
)
cadMplsLdpNeighborPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadMplsLdpNeighborPassword.setStatus("current")


class _CadMplsLdpNeighborTargetedPeer_Type(TruthValue):
    """Custom type cadMplsLdpNeighborTargetedPeer based on TruthValue"""


_CadMplsLdpNeighborTargetedPeer_Object = MibTableColumn
cadMplsLdpNeighborTargetedPeer = _CadMplsLdpNeighborTargetedPeer_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 130, 1, 1, 2, 1, 4),
    _CadMplsLdpNeighborTargetedPeer_Type()
)
cadMplsLdpNeighborTargetedPeer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadMplsLdpNeighborTargetedPeer.setStatus("current")
_CadMplsLdpNeighborRowStatus_Type = RowStatus
_CadMplsLdpNeighborRowStatus_Object = MibTableColumn
cadMplsLdpNeighborRowStatus = _CadMplsLdpNeighborRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 130, 1, 1, 2, 1, 5),
    _CadMplsLdpNeighborRowStatus_Type()
)
cadMplsLdpNeighborRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadMplsLdpNeighborRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CADANT-MPLS-MIB",
    **{"cadMplsMIB": cadMplsMIB,
       "cadMplsMIBObjects": cadMplsMIBObjects,
       "cadMplsParams": cadMplsParams,
       "cadMplsLdpHelloHoldTimer": cadMplsLdpHelloHoldTimer,
       "cadMplsLdpTargetedHelloHoldTimer": cadMplsLdpTargetedHelloHoldTimer,
       "cadMplsLdpKeepAliveHoldTimer": cadMplsLdpKeepAliveHoldTimer,
       "cadMplsLdpVcDescription": cadMplsLdpVcDescription,
       "cadMplsLdpNeighborTable": cadMplsLdpNeighborTable,
       "cadMplsLdpNeighborEntry": cadMplsLdpNeighborEntry,
       "cadMplsLdpNeighborAddressType": cadMplsLdpNeighborAddressType,
       "cadMplsLdpNeighborIpAddress": cadMplsLdpNeighborIpAddress,
       "cadMplsLdpNeighborPassword": cadMplsLdpNeighborPassword,
       "cadMplsLdpNeighborTargetedPeer": cadMplsLdpNeighborTargetedPeer,
       "cadMplsLdpNeighborRowStatus": cadMplsLdpNeighborRowStatus}
)
