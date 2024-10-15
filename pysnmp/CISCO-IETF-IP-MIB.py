# SNMP MIB module (CISCO-IETF-IP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-IETF-IP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:01:35 2024
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

(ciscoExperiment,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoExperiment")

(InterfaceIndex,
 InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero",
    "ifIndex")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
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
 PhysAddress,
 RowPointer,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowPointer",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoIetfIpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 86)
)
ciscoIetfIpMIB.setRevisions(
        ("2002-03-04 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Ipv6AddrIfIdentifier(OctetString, TextualConvention):
    status = "current"
    displayHint = "2x:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )



class ScopeId(Unsigned32, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_CiscoIetfIpMIBObjects_ObjectIdentity = ObjectIdentity
ciscoIetfIpMIBObjects = _CiscoIetfIpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 86, 1)
)
_CIp_ObjectIdentity = ObjectIdentity
cIp = _CIp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 86, 1, 1)
)
_CIpAddressPfxTable_Object = MibTable
cIpAddressPfxTable = _CIpAddressPfxTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 86, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cIpAddressPfxTable.setStatus("current")
_CIpAddressPfxEntry_Object = MibTableRow
cIpAddressPfxEntry = _CIpAddressPfxEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 86, 1, 1, 1, 1)
)
cIpAddressPfxEntry.setIndexNames(
    (0, "CISCO-IETF-IP-MIB", "cIpAddressPfxIfIndex"),
    (0, "CISCO-IETF-IP-MIB", "cIpAddressPfxType"),
    (0, "CISCO-IETF-IP-MIB", "cIpAddressPfxPfx"),
    (0, "CISCO-IETF-IP-MIB", "cIpAddressPfxLength"),
)
if mibBuilder.loadTexts:
    cIpAddressPfxEntry.setStatus("current")
_CIpAddressPfxIfIndex_Type = InterfaceIndex
_CIpAddressPfxIfIndex_Object = MibTableColumn
cIpAddressPfxIfIndex = _CIpAddressPfxIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 86, 1, 1, 1, 1, 1),
    _CIpAddressPfxIfIndex_Type()
)
cIpAddressPfxIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cIpAddressPfxIfIndex.setStatus("current")
_CIpAddressPfxType_Type = InetAddressType
_CIpAddressPfxType_Object = MibTableColumn
cIpAddressPfxType = _CIpAddressPfxType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 86, 1, 1, 1, 1, 2),
    _CIpAddressPfxType_Type()
)
cIpAddressPfxType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cIpAddressPfxType.setStatus("current")


class _CIpAddressPfxPfx_Type(InetAddress):
    """Custom type cIpAddressPfxPfx based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 36),
    )


_CIpAddressPfxPfx_Type.__name__ = "InetAddress"
_CIpAddressPfxPfx_Object = MibTableColumn
cIpAddressPfxPfx = _CIpAddressPfxPfx_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 86, 1, 1, 1, 1, 3),
    _CIpAddressPfxPfx_Type()
)
cIpAddressPfxPfx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cIpAddressPfxPfx.setStatus("current")
_CIpAddressPfxLength_Type = InetAddressPrefixLength
_CIpAddressPfxLength_Object = MibTableColumn
cIpAddressPfxLength = _CIpAddressPfxLength_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 86, 1, 1, 1, 1, 4),
    _CIpAddressPfxLength_Type()
)
cIpAddressPfxLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cIpAddressPfxLength.setStatus("current")


class _CIpAddressPfxOrigin_Type(Integer32):
    """Custom type cIpAddressPfxOrigin based on Integer32"""
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
        *(("dhcp", 4),
          ("manual", 2),
          ("other", 1),
          ("routeradv", 5),
          ("wellknown", 3))
    )


_CIpAddressPfxOrigin_Type.__name__ = "Integer32"
_CIpAddressPfxOrigin_Object = MibTableColumn
cIpAddressPfxOrigin = _CIpAddressPfxOrigin_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 86, 1, 1, 1, 1, 5),
    _CIpAddressPfxOrigin_Type()
)
cIpAddressPfxOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIpAddressPfxOrigin.setStatus("current")
_CIpAddressPfxOnLinkFlag_Type = TruthValue
_CIpAddressPfxOnLinkFlag_Object = MibTableColumn
cIpAddressPfxOnLinkFlag = _CIpAddressPfxOnLinkFlag_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 86, 1, 1, 1, 1, 6),
    _CIpAddressPfxOnLinkFlag_Type()
)
cIpAddressPfxOnLinkFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIpAddressPfxOnLinkFlag.setStatus("current")
_CIpAddressPfxAutonomousFlag_Type = TruthValue
_CIpAddressPfxAutonomousFlag_Object = MibTableColumn
cIpAddressPfxAutonomousFlag = _CIpAddressPfxAutonomousFlag_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 86, 1, 1, 1, 1, 7),
    _CIpAddressPfxAutonomousFlag_Type()
)
cIpAddressPfxAutonomousFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIpAddressPfxAutonomousFlag.setStatus("current")
_CIpAddressPfxAdvPfdLifetime_Type = Unsigned32
_CIpAddressPfxAdvPfdLifetime_Object = MibTableColumn
cIpAddressPfxAdvPfdLifetime = _CIpAddressPfxAdvPfdLifetime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 86, 1, 1, 1, 1, 8),
    _CIpAddressPfxAdvPfdLifetime_Type()
)
cIpAddressPfxAdvPfdLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIpAddressPfxAdvPfdLifetime.setStatus("current")
if mibBuilder.loadTexts:
    cIpAddressPfxAdvPfdLifetime.setUnits("seconds")
_CIpAddressPfxAdvValidLifetime_Type = Unsigned32
_CIpAddressPfxAdvValidLifetime_Object = MibTableColumn
cIpAddressPfxAdvValidLifetime = _CIpAddressPfxAdvValidLifetime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 86, 1, 1, 1, 1, 9),
    _CIpAddressPfxAdvValidLifetime_Type()
)
cIpAddressPfxAdvValidLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIpAddressPfxAdvValidLifetime.setStatus("current")
if mibBuilder.loadTexts:
    cIpAddressPfxAdvValidLifetime.setUnits("seconds")
_CIpAddressTable_Object = MibTable
cIpAddressTable = _CIpAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 86, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cIpAddressTable.setStatus("current")
_CIpAddressEntry_Object = MibTableRow
cIpAddressEntry = _CIpAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 86, 1, 1, 2, 1)
)
cIpAddressEntry.setIndexNames(
    (0, "CISCO-IETF-IP-MIB", "cIpAddressAddrType"),
    (0, "CISCO-IETF-IP-MIB", "cIpAddressAddr"),
)
if mibBuilder.loadTexts:
    cIpAddressEntry.setStatus("current")
_CIpAddressAddrType_Type = InetAddressType
_CIpAddressAddrType_Object = MibTableColumn
cIpAddressAddrType = _CIpAddressAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 86, 1, 1, 2, 1, 1),
    _CIpAddressAddrType_Type()
)
cIpAddressAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cIpAddressAddrType.setStatus("current")


class _CIpAddressAddr_Type(InetAddress):
    """Custom type cIpAddressAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 36),
    )


_CIpAddressAddr_Type.__name__ = "InetAddress"
_CIpAddressAddr_Object = MibTableColumn
cIpAddressAddr = _CIpAddressAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 86, 1, 1, 2, 1, 2),
    _CIpAddressAddr_Type()
)
cIpAddressAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cIpAddressAddr.setStatus("current")
_CIpAddressIfIndex_Type = InterfaceIndex
_CIpAddressIfIndex_Object = MibTableColumn
cIpAddressIfIndex = _CIpAddressIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 86, 1, 1, 2, 1, 3),
    _CIpAddressIfIndex_Type()
)
cIpAddressIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIpAddressIfIndex.setStatus("current")


class _CIpAddressType_Type(Integer32):
    """Custom type cIpAddressType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("anycast", 2),
          ("broadcast", 3),
          ("unicast", 1))
    )


_CIpAddressType_Type.__name__ = "Integer32"
_CIpAddressType_Object = MibTableColumn
cIpAddressType = _CIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 86, 1, 1, 2, 1, 4),
    _CIpAddressType_Type()
)
cIpAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIpAddressType.setStatus("current")
_CIpAddressPrefix_Type = RowPointer
_CIpAddressPrefix_Object = MibTableColumn
cIpAddressPrefix = _CIpAddressPrefix_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 86, 1, 1, 2, 1, 5),
    _CIpAddressPrefix_Type()
)
cIpAddressPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIpAddressPrefix.setStatus("current")


class _CIpAddressOrigin_Type(Integer32):
    """Custom type cIpAddressOrigin based on Integer32"""
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
        *(("dhcp", 4),
          ("linklayer", 5),
          ("manual", 2),
          ("other", 1),
          ("random", 6),
          ("wellknown", 3))
    )


_CIpAddressOrigin_Type.__name__ = "Integer32"
_CIpAddressOrigin_Object = MibTableColumn
cIpAddressOrigin = _CIpAddressOrigin_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 86, 1, 1, 2, 1, 6),
    _CIpAddressOrigin_Type()
)
cIpAddressOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIpAddressOrigin.setStatus("current")


class _CIpAddressStatus_Type(Integer32):
    """Custom type cIpAddressStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("deprecated", 2),
          ("duplicate", 7),
          ("inaccessible", 4),
          ("invalid", 3),
          ("preferred", 1),
          ("tentative", 6),
          ("unknown", 5))
    )


_CIpAddressStatus_Type.__name__ = "Integer32"
_CIpAddressStatus_Object = MibTableColumn
cIpAddressStatus = _CIpAddressStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 86, 1, 1, 2, 1, 7),
    _CIpAddressStatus_Type()
)
cIpAddressStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIpAddressStatus.setStatus("current")
_CInetNetToMediaTable_Object = MibTable
cInetNetToMediaTable = _CInetNetToMediaTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 86, 1, 1, 3)
)
if mibBuilder.loadTexts:
    cInetNetToMediaTable.setStatus("current")
_CInetNetToMediaEntry_Object = MibTableRow
cInetNetToMediaEntry = _CInetNetToMediaEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 86, 1, 1, 3, 1)
)
cInetNetToMediaEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-IETF-IP-MIB", "cInetNetToMediaNetAddressType"),
    (0, "CISCO-IETF-IP-MIB", "cInetNetToMediaNetAddress"),
)
if mibBuilder.loadTexts:
    cInetNetToMediaEntry.setStatus("current")
_CInetNetToMediaNetAddressType_Type = InetAddressType
_CInetNetToMediaNetAddressType_Object = MibTableColumn
cInetNetToMediaNetAddressType = _CInetNetToMediaNetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 86, 1, 1, 3, 1, 1),
    _CInetNetToMediaNetAddressType_Type()
)
cInetNetToMediaNetAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cInetNetToMediaNetAddressType.setStatus("current")


class _CInetNetToMediaNetAddress_Type(InetAddress):
    """Custom type cInetNetToMediaNetAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 36),
    )


_CInetNetToMediaNetAddress_Type.__name__ = "InetAddress"
_CInetNetToMediaNetAddress_Object = MibTableColumn
cInetNetToMediaNetAddress = _CInetNetToMediaNetAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 86, 1, 1, 3, 1, 2),
    _CInetNetToMediaNetAddress_Type()
)
cInetNetToMediaNetAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cInetNetToMediaNetAddress.setStatus("current")
_CInetNetToMediaPhysAddress_Type = PhysAddress
_CInetNetToMediaPhysAddress_Object = MibTableColumn
cInetNetToMediaPhysAddress = _CInetNetToMediaPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 86, 1, 1, 3, 1, 3),
    _CInetNetToMediaPhysAddress_Type()
)
cInetNetToMediaPhysAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cInetNetToMediaPhysAddress.setStatus("current")
_CInetNetToMediaLastUpdated_Type = TimeStamp
_CInetNetToMediaLastUpdated_Object = MibTableColumn
cInetNetToMediaLastUpdated = _CInetNetToMediaLastUpdated_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 86, 1, 1, 3, 1, 4),
    _CInetNetToMediaLastUpdated_Type()
)
cInetNetToMediaLastUpdated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cInetNetToMediaLastUpdated.setStatus("current")


class _CInetNetToMediaType_Type(Integer32):
    """Custom type cInetNetToMediaType based on Integer32"""
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
        *(("dynamic", 3),
          ("invalid", 2),
          ("local", 5),
          ("other", 1),
          ("static", 4))
    )


_CInetNetToMediaType_Type.__name__ = "Integer32"
_CInetNetToMediaType_Object = MibTableColumn
cInetNetToMediaType = _CInetNetToMediaType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 86, 1, 1, 3, 1, 5),
    _CInetNetToMediaType_Type()
)
cInetNetToMediaType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cInetNetToMediaType.setStatus("current")


class _CInetNetToMediaState_Type(Integer32):
    """Custom type cInetNetToMediaState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("delay", 3),
          ("incomplete", 7),
          ("invalid", 5),
          ("probe", 4),
          ("reachable", 1),
          ("stale", 2),
          ("unknown", 6))
    )


_CInetNetToMediaState_Type.__name__ = "Integer32"
_CInetNetToMediaState_Object = MibTableColumn
cInetNetToMediaState = _CInetNetToMediaState_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 86, 1, 1, 3, 1, 6),
    _CInetNetToMediaState_Type()
)
cInetNetToMediaState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cInetNetToMediaState.setStatus("current")
_CIpv6ScopeIdTable_Object = MibTable
cIpv6ScopeIdTable = _CIpv6ScopeIdTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 86, 1, 1, 4)
)
if mibBuilder.loadTexts:
    cIpv6ScopeIdTable.setStatus("current")
_CIpv6ScopeIdEntry_Object = MibTableRow
cIpv6ScopeIdEntry = _CIpv6ScopeIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 86, 1, 1, 4, 1)
)
cIpv6ScopeIdEntry.setIndexNames(
    (0, "CISCO-IETF-IP-MIB", "cIpv6ScopeIdIfIndex"),
)
if mibBuilder.loadTexts:
    cIpv6ScopeIdEntry.setStatus("current")
_CIpv6ScopeIdIfIndex_Type = InterfaceIndex
_CIpv6ScopeIdIfIndex_Object = MibTableColumn
cIpv6ScopeIdIfIndex = _CIpv6ScopeIdIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 86, 1, 1, 4, 1, 1),
    _CIpv6ScopeIdIfIndex_Type()
)
cIpv6ScopeIdIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cIpv6ScopeIdIfIndex.setStatus("current")
_CIpv6ScopeIdLinkLocal_Type = ScopeId
_CIpv6ScopeIdLinkLocal_Object = MibTableColumn
cIpv6ScopeIdLinkLocal = _CIpv6ScopeIdLinkLocal_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 86, 1, 1, 4, 1, 2),
    _CIpv6ScopeIdLinkLocal_Type()
)
cIpv6ScopeIdLinkLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIpv6ScopeIdLinkLocal.setStatus("current")
_CIpv6ScopeIdSubnetLocal_Type = ScopeId
_CIpv6ScopeIdSubnetLocal_Object = MibTableColumn
cIpv6ScopeIdSubnetLocal = _CIpv6ScopeIdSubnetLocal_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 86, 1, 1, 4, 1, 3),
    _CIpv6ScopeIdSubnetLocal_Type()
)
cIpv6ScopeIdSubnetLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIpv6ScopeIdSubnetLocal.setStatus("current")
_CIpv6ScopeIdAdminLocal_Type = ScopeId
_CIpv6ScopeIdAdminLocal_Object = MibTableColumn
cIpv6ScopeIdAdminLocal = _CIpv6ScopeIdAdminLocal_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 86, 1, 1, 4, 1, 4),
    _CIpv6ScopeIdAdminLocal_Type()
)
cIpv6ScopeIdAdminLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIpv6ScopeIdAdminLocal.setStatus("current")
_CIpv6ScopeIdSiteLocal_Type = ScopeId
_CIpv6ScopeIdSiteLocal_Object = MibTableColumn
cIpv6ScopeIdSiteLocal = _CIpv6ScopeIdSiteLocal_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 86, 1, 1, 4, 1, 5),
    _CIpv6ScopeIdSiteLocal_Type()
)
cIpv6ScopeIdSiteLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIpv6ScopeIdSiteLocal.setStatus("current")
_CIpv6ScopeId6_Type = ScopeId
_CIpv6ScopeId6_Object = MibTableColumn
cIpv6ScopeId6 = _CIpv6ScopeId6_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 86, 1, 1, 4, 1, 6),
    _CIpv6ScopeId6_Type()
)
cIpv6ScopeId6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIpv6ScopeId6.setStatus("current")
_CIpv6ScopeId7_Type = ScopeId
_CIpv6ScopeId7_Object = MibTableColumn
cIpv6ScopeId7 = _CIpv6ScopeId7_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 86, 1, 1, 4, 1, 7),
    _CIpv6ScopeId7_Type()
)
cIpv6ScopeId7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIpv6ScopeId7.setStatus("current")
_CIpv6ScopeIdOrganizationLocal_Type = ScopeId
_CIpv6ScopeIdOrganizationLocal_Object = MibTableColumn
cIpv6ScopeIdOrganizationLocal = _CIpv6ScopeIdOrganizationLocal_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 86, 1, 1, 4, 1, 8),
    _CIpv6ScopeIdOrganizationLocal_Type()
)
cIpv6ScopeIdOrganizationLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIpv6ScopeIdOrganizationLocal.setStatus("current")
_CIpv6ScopeId9_Type = ScopeId
_CIpv6ScopeId9_Object = MibTableColumn
cIpv6ScopeId9 = _CIpv6ScopeId9_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 86, 1, 1, 4, 1, 9),
    _CIpv6ScopeId9_Type()
)
cIpv6ScopeId9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIpv6ScopeId9.setStatus("current")
_CIpv6ScopeIdA_Type = ScopeId
_CIpv6ScopeIdA_Object = MibTableColumn
cIpv6ScopeIdA = _CIpv6ScopeIdA_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 86, 1, 1, 4, 1, 10),
    _CIpv6ScopeIdA_Type()
)
cIpv6ScopeIdA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIpv6ScopeIdA.setStatus("current")
_CIpv6ScopeIdB_Type = ScopeId
_CIpv6ScopeIdB_Object = MibTableColumn
cIpv6ScopeIdB = _CIpv6ScopeIdB_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 86, 1, 1, 4, 1, 11),
    _CIpv6ScopeIdB_Type()
)
cIpv6ScopeIdB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIpv6ScopeIdB.setStatus("current")
_CIpv6ScopeIdC_Type = ScopeId
_CIpv6ScopeIdC_Object = MibTableColumn
cIpv6ScopeIdC = _CIpv6ScopeIdC_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 86, 1, 1, 4, 1, 12),
    _CIpv6ScopeIdC_Type()
)
cIpv6ScopeIdC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIpv6ScopeIdC.setStatus("current")
_CIpv6ScopeIdD_Type = ScopeId
_CIpv6ScopeIdD_Object = MibTableColumn
cIpv6ScopeIdD = _CIpv6ScopeIdD_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 86, 1, 1, 4, 1, 13),
    _CIpv6ScopeIdD_Type()
)
cIpv6ScopeIdD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIpv6ScopeIdD.setStatus("current")
_CIpv6_ObjectIdentity = ObjectIdentity
cIpv6 = _CIpv6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 86, 1, 2)
)


class _CIpv6Forwarding_Type(Integer32):
    """Custom type cIpv6Forwarding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forwarding", 1),
          ("notForwarding", 2))
    )


_CIpv6Forwarding_Type.__name__ = "Integer32"
_CIpv6Forwarding_Object = MibScalar
cIpv6Forwarding = _CIpv6Forwarding_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 86, 1, 2, 1),
    _CIpv6Forwarding_Type()
)
cIpv6Forwarding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cIpv6Forwarding.setStatus("current")


class _CIpv6DefaultHopLimit_Type(Integer32):
    """Custom type cIpv6DefaultHopLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CIpv6DefaultHopLimit_Type.__name__ = "Integer32"
_CIpv6DefaultHopLimit_Object = MibScalar
cIpv6DefaultHopLimit = _CIpv6DefaultHopLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 86, 1, 2, 2),
    _CIpv6DefaultHopLimit_Type()
)
cIpv6DefaultHopLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cIpv6DefaultHopLimit.setStatus("current")
_CIpv6InterfaceTable_Object = MibTable
cIpv6InterfaceTable = _CIpv6InterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 86, 1, 2, 3)
)
if mibBuilder.loadTexts:
    cIpv6InterfaceTable.setStatus("current")
_CIpv6InterfaceEntry_Object = MibTableRow
cIpv6InterfaceEntry = _CIpv6InterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 86, 1, 2, 3, 1)
)
cIpv6InterfaceEntry.setIndexNames(
    (0, "CISCO-IETF-IP-MIB", "cIpv6InterfaceIfIndex"),
)
if mibBuilder.loadTexts:
    cIpv6InterfaceEntry.setStatus("current")
_CIpv6InterfaceIfIndex_Type = InterfaceIndex
_CIpv6InterfaceIfIndex_Object = MibTableColumn
cIpv6InterfaceIfIndex = _CIpv6InterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 86, 1, 2, 3, 1, 1),
    _CIpv6InterfaceIfIndex_Type()
)
cIpv6InterfaceIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cIpv6InterfaceIfIndex.setStatus("current")
_CIpv6InterfaceEffectiveMtu_Type = Unsigned32
_CIpv6InterfaceEffectiveMtu_Object = MibTableColumn
cIpv6InterfaceEffectiveMtu = _CIpv6InterfaceEffectiveMtu_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 86, 1, 2, 3, 1, 2),
    _CIpv6InterfaceEffectiveMtu_Type()
)
cIpv6InterfaceEffectiveMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIpv6InterfaceEffectiveMtu.setStatus("current")
if mibBuilder.loadTexts:
    cIpv6InterfaceEffectiveMtu.setUnits("octets")


class _CIpv6InterfaceReasmMaxSize_Type(Unsigned32):
    """Custom type cIpv6InterfaceReasmMaxSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CIpv6InterfaceReasmMaxSize_Type.__name__ = "Unsigned32"
_CIpv6InterfaceReasmMaxSize_Object = MibTableColumn
cIpv6InterfaceReasmMaxSize = _CIpv6InterfaceReasmMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 86, 1, 2, 3, 1, 3),
    _CIpv6InterfaceReasmMaxSize_Type()
)
cIpv6InterfaceReasmMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIpv6InterfaceReasmMaxSize.setStatus("current")
if mibBuilder.loadTexts:
    cIpv6InterfaceReasmMaxSize.setUnits("octets")
_CIpv6InterfaceIdentifier_Type = Ipv6AddrIfIdentifier
_CIpv6InterfaceIdentifier_Object = MibTableColumn
cIpv6InterfaceIdentifier = _CIpv6InterfaceIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 86, 1, 2, 3, 1, 4),
    _CIpv6InterfaceIdentifier_Type()
)
cIpv6InterfaceIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cIpv6InterfaceIdentifier.setStatus("current")


class _CIpv6InterfaceIdentifierLength_Type(Integer32):
    """Custom type cIpv6InterfaceIdentifierLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_CIpv6InterfaceIdentifierLength_Type.__name__ = "Integer32"
_CIpv6InterfaceIdentifierLength_Object = MibTableColumn
cIpv6InterfaceIdentifierLength = _CIpv6InterfaceIdentifierLength_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 86, 1, 2, 3, 1, 5),
    _CIpv6InterfaceIdentifierLength_Type()
)
cIpv6InterfaceIdentifierLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cIpv6InterfaceIdentifierLength.setStatus("current")
if mibBuilder.loadTexts:
    cIpv6InterfaceIdentifierLength.setUnits("bits")
_CIpv6InterfacePhysicalAddress_Type = PhysAddress
_CIpv6InterfacePhysicalAddress_Object = MibTableColumn
cIpv6InterfacePhysicalAddress = _CIpv6InterfacePhysicalAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 86, 1, 2, 3, 1, 6),
    _CIpv6InterfacePhysicalAddress_Type()
)
cIpv6InterfacePhysicalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIpv6InterfacePhysicalAddress.setStatus("current")
_CIcmp_ObjectIdentity = ObjectIdentity
cIcmp = _CIcmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 86, 1, 3)
)
_CInetIcmpTable_Object = MibTable
cInetIcmpTable = _CInetIcmpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 86, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cInetIcmpTable.setStatus("current")
_CInetIcmpEntry_Object = MibTableRow
cInetIcmpEntry = _CInetIcmpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 86, 1, 3, 1, 1)
)
cInetIcmpEntry.setIndexNames(
    (0, "CISCO-IETF-IP-MIB", "cInetIcmpAFType"),
    (0, "CISCO-IETF-IP-MIB", "cInetIcmpIfIndex"),
)
if mibBuilder.loadTexts:
    cInetIcmpEntry.setStatus("current")
_CInetIcmpAFType_Type = InetAddressType
_CInetIcmpAFType_Object = MibTableColumn
cInetIcmpAFType = _CInetIcmpAFType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 86, 1, 3, 1, 1, 1),
    _CInetIcmpAFType_Type()
)
cInetIcmpAFType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cInetIcmpAFType.setStatus("current")
_CInetIcmpIfIndex_Type = InterfaceIndexOrZero
_CInetIcmpIfIndex_Object = MibTableColumn
cInetIcmpIfIndex = _CInetIcmpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 86, 1, 3, 1, 1, 2),
    _CInetIcmpIfIndex_Type()
)
cInetIcmpIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cInetIcmpIfIndex.setStatus("current")
_CInetIcmpInMsgs_Type = Counter32
_CInetIcmpInMsgs_Object = MibTableColumn
cInetIcmpInMsgs = _CInetIcmpInMsgs_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 86, 1, 3, 1, 1, 3),
    _CInetIcmpInMsgs_Type()
)
cInetIcmpInMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cInetIcmpInMsgs.setStatus("current")
_CInetIcmpInErrors_Type = Counter32
_CInetIcmpInErrors_Object = MibTableColumn
cInetIcmpInErrors = _CInetIcmpInErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 86, 1, 3, 1, 1, 4),
    _CInetIcmpInErrors_Type()
)
cInetIcmpInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cInetIcmpInErrors.setStatus("current")
_CInetIcmpOutMsgs_Type = Counter32
_CInetIcmpOutMsgs_Object = MibTableColumn
cInetIcmpOutMsgs = _CInetIcmpOutMsgs_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 86, 1, 3, 1, 1, 5),
    _CInetIcmpOutMsgs_Type()
)
cInetIcmpOutMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cInetIcmpOutMsgs.setStatus("current")
_CInetIcmpOutErrors_Type = Counter32
_CInetIcmpOutErrors_Object = MibTableColumn
cInetIcmpOutErrors = _CInetIcmpOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 86, 1, 3, 1, 1, 6),
    _CInetIcmpOutErrors_Type()
)
cInetIcmpOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cInetIcmpOutErrors.setStatus("current")
_CInetIcmpMsgTable_Object = MibTable
cInetIcmpMsgTable = _CInetIcmpMsgTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 86, 1, 3, 2)
)
if mibBuilder.loadTexts:
    cInetIcmpMsgTable.setStatus("current")
_CInetIcmpMsgEntry_Object = MibTableRow
cInetIcmpMsgEntry = _CInetIcmpMsgEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 86, 1, 3, 2, 1)
)
cInetIcmpMsgEntry.setIndexNames(
    (0, "CISCO-IETF-IP-MIB", "cInetIcmpMsgAFType"),
    (0, "CISCO-IETF-IP-MIB", "cInetIcmpMsgIfIndex"),
    (0, "CISCO-IETF-IP-MIB", "cInetIcmpMsgType"),
    (0, "CISCO-IETF-IP-MIB", "cInetIcmpMsgCode"),
)
if mibBuilder.loadTexts:
    cInetIcmpMsgEntry.setStatus("current")
_CInetIcmpMsgAFType_Type = InetAddressType
_CInetIcmpMsgAFType_Object = MibTableColumn
cInetIcmpMsgAFType = _CInetIcmpMsgAFType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 86, 1, 3, 2, 1, 1),
    _CInetIcmpMsgAFType_Type()
)
cInetIcmpMsgAFType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cInetIcmpMsgAFType.setStatus("current")
_CInetIcmpMsgIfIndex_Type = InterfaceIndexOrZero
_CInetIcmpMsgIfIndex_Object = MibTableColumn
cInetIcmpMsgIfIndex = _CInetIcmpMsgIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 86, 1, 3, 2, 1, 2),
    _CInetIcmpMsgIfIndex_Type()
)
cInetIcmpMsgIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cInetIcmpMsgIfIndex.setStatus("current")


class _CInetIcmpMsgType_Type(Integer32):
    """Custom type cInetIcmpMsgType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CInetIcmpMsgType_Type.__name__ = "Integer32"
_CInetIcmpMsgType_Object = MibTableColumn
cInetIcmpMsgType = _CInetIcmpMsgType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 86, 1, 3, 2, 1, 3),
    _CInetIcmpMsgType_Type()
)
cInetIcmpMsgType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cInetIcmpMsgType.setStatus("current")


class _CInetIcmpMsgCode_Type(Integer32):
    """Custom type cInetIcmpMsgCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_CInetIcmpMsgCode_Type.__name__ = "Integer32"
_CInetIcmpMsgCode_Object = MibTableColumn
cInetIcmpMsgCode = _CInetIcmpMsgCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 86, 1, 3, 2, 1, 4),
    _CInetIcmpMsgCode_Type()
)
cInetIcmpMsgCode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cInetIcmpMsgCode.setStatus("current")
_CInetIcmpMsgInPkts_Type = Counter32
_CInetIcmpMsgInPkts_Object = MibTableColumn
cInetIcmpMsgInPkts = _CInetIcmpMsgInPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 86, 1, 3, 2, 1, 5),
    _CInetIcmpMsgInPkts_Type()
)
cInetIcmpMsgInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cInetIcmpMsgInPkts.setStatus("current")
_CInetIcmpMsgOutPkts_Type = Counter32
_CInetIcmpMsgOutPkts_Object = MibTableColumn
cInetIcmpMsgOutPkts = _CInetIcmpMsgOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 86, 1, 3, 2, 1, 6),
    _CInetIcmpMsgOutPkts_Type()
)
cInetIcmpMsgOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cInetIcmpMsgOutPkts.setStatus("current")
_CiscoIpMIBConformance_ObjectIdentity = ObjectIdentity
ciscoIpMIBConformance = _CiscoIpMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 86, 2)
)
_CiscoIpMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoIpMIBCompliances = _CiscoIpMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 86, 2, 1)
)
_CiscoIpMIBGroups_ObjectIdentity = ObjectIdentity
ciscoIpMIBGroups = _CiscoIpMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 86, 2, 2)
)

# Managed Objects groups

ciscoIpAddressPfxGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 86, 2, 2, 1)
)
ciscoIpAddressPfxGroup.setObjects(
      *(("CISCO-IETF-IP-MIB", "cIpAddressPfxOrigin"),
        ("CISCO-IETF-IP-MIB", "cIpAddressPfxOnLinkFlag"),
        ("CISCO-IETF-IP-MIB", "cIpAddressPfxAutonomousFlag"),
        ("CISCO-IETF-IP-MIB", "cIpAddressPfxAdvPfdLifetime"),
        ("CISCO-IETF-IP-MIB", "cIpAddressPfxAdvValidLifetime"))
)
if mibBuilder.loadTexts:
    ciscoIpAddressPfxGroup.setStatus("current")

ciscoIpAddressGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 86, 2, 2, 2)
)
ciscoIpAddressGroup.setObjects(
      *(("CISCO-IETF-IP-MIB", "cIpAddressIfIndex"),
        ("CISCO-IETF-IP-MIB", "cIpAddressType"),
        ("CISCO-IETF-IP-MIB", "cIpAddressPrefix"),
        ("CISCO-IETF-IP-MIB", "cIpAddressOrigin"),
        ("CISCO-IETF-IP-MIB", "cIpAddressStatus"))
)
if mibBuilder.loadTexts:
    ciscoIpAddressGroup.setStatus("current")

ciscoInetNetToMediaGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 86, 2, 2, 3)
)
ciscoInetNetToMediaGroup.setObjects(
      *(("CISCO-IETF-IP-MIB", "cInetNetToMediaPhysAddress"),
        ("CISCO-IETF-IP-MIB", "cInetNetToMediaLastUpdated"),
        ("CISCO-IETF-IP-MIB", "cInetNetToMediaType"),
        ("CISCO-IETF-IP-MIB", "cInetNetToMediaState"))
)
if mibBuilder.loadTexts:
    ciscoInetNetToMediaGroup.setStatus("current")

ciscoInetIcmpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 86, 2, 2, 4)
)
ciscoInetIcmpGroup.setObjects(
      *(("CISCO-IETF-IP-MIB", "cInetIcmpInMsgs"),
        ("CISCO-IETF-IP-MIB", "cInetIcmpInErrors"),
        ("CISCO-IETF-IP-MIB", "cInetIcmpOutMsgs"),
        ("CISCO-IETF-IP-MIB", "cInetIcmpOutErrors"))
)
if mibBuilder.loadTexts:
    ciscoInetIcmpGroup.setStatus("current")

ciscoInetIcmpMsgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 86, 2, 2, 5)
)
ciscoInetIcmpMsgGroup.setObjects(
      *(("CISCO-IETF-IP-MIB", "cInetIcmpMsgInPkts"),
        ("CISCO-IETF-IP-MIB", "cInetIcmpMsgOutPkts"))
)
if mibBuilder.loadTexts:
    ciscoInetIcmpMsgGroup.setStatus("current")

ciscoIpv6GeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 86, 2, 2, 6)
)
ciscoIpv6GeneralGroup.setObjects(
      *(("CISCO-IETF-IP-MIB", "cIpv6Forwarding"),
        ("CISCO-IETF-IP-MIB", "cIpv6DefaultHopLimit"))
)
if mibBuilder.loadTexts:
    ciscoIpv6GeneralGroup.setStatus("current")

ciscoIpv6InterfaceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 86, 2, 2, 7)
)
ciscoIpv6InterfaceGroup.setObjects(
      *(("CISCO-IETF-IP-MIB", "cIpv6InterfaceEffectiveMtu"),
        ("CISCO-IETF-IP-MIB", "cIpv6InterfaceReasmMaxSize"),
        ("CISCO-IETF-IP-MIB", "cIpv6InterfaceIdentifier"),
        ("CISCO-IETF-IP-MIB", "cIpv6InterfaceIdentifierLength"),
        ("CISCO-IETF-IP-MIB", "cIpv6InterfacePhysicalAddress"))
)
if mibBuilder.loadTexts:
    ciscoIpv6InterfaceGroup.setStatus("current")

ciscoIpv6ScopeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 86, 2, 2, 8)
)
ciscoIpv6ScopeGroup.setObjects(
      *(("CISCO-IETF-IP-MIB", "cIpv6ScopeIdLinkLocal"),
        ("CISCO-IETF-IP-MIB", "cIpv6ScopeIdSubnetLocal"),
        ("CISCO-IETF-IP-MIB", "cIpv6ScopeIdAdminLocal"),
        ("CISCO-IETF-IP-MIB", "cIpv6ScopeIdSiteLocal"),
        ("CISCO-IETF-IP-MIB", "cIpv6ScopeId6"),
        ("CISCO-IETF-IP-MIB", "cIpv6ScopeId7"),
        ("CISCO-IETF-IP-MIB", "cIpv6ScopeIdOrganizationLocal"),
        ("CISCO-IETF-IP-MIB", "cIpv6ScopeId9"),
        ("CISCO-IETF-IP-MIB", "cIpv6ScopeIdA"),
        ("CISCO-IETF-IP-MIB", "cIpv6ScopeIdB"),
        ("CISCO-IETF-IP-MIB", "cIpv6ScopeIdC"),
        ("CISCO-IETF-IP-MIB", "cIpv6ScopeIdD"))
)
if mibBuilder.loadTexts:
    ciscoIpv6ScopeGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoIpMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 86, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoIpMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-IETF-IP-MIB",
    **{"Ipv6AddrIfIdentifier": Ipv6AddrIfIdentifier,
       "ScopeId": ScopeId,
       "ciscoIetfIpMIB": ciscoIetfIpMIB,
       "ciscoIetfIpMIBObjects": ciscoIetfIpMIBObjects,
       "cIp": cIp,
       "cIpAddressPfxTable": cIpAddressPfxTable,
       "cIpAddressPfxEntry": cIpAddressPfxEntry,
       "cIpAddressPfxIfIndex": cIpAddressPfxIfIndex,
       "cIpAddressPfxType": cIpAddressPfxType,
       "cIpAddressPfxPfx": cIpAddressPfxPfx,
       "cIpAddressPfxLength": cIpAddressPfxLength,
       "cIpAddressPfxOrigin": cIpAddressPfxOrigin,
       "cIpAddressPfxOnLinkFlag": cIpAddressPfxOnLinkFlag,
       "cIpAddressPfxAutonomousFlag": cIpAddressPfxAutonomousFlag,
       "cIpAddressPfxAdvPfdLifetime": cIpAddressPfxAdvPfdLifetime,
       "cIpAddressPfxAdvValidLifetime": cIpAddressPfxAdvValidLifetime,
       "cIpAddressTable": cIpAddressTable,
       "cIpAddressEntry": cIpAddressEntry,
       "cIpAddressAddrType": cIpAddressAddrType,
       "cIpAddressAddr": cIpAddressAddr,
       "cIpAddressIfIndex": cIpAddressIfIndex,
       "cIpAddressType": cIpAddressType,
       "cIpAddressPrefix": cIpAddressPrefix,
       "cIpAddressOrigin": cIpAddressOrigin,
       "cIpAddressStatus": cIpAddressStatus,
       "cInetNetToMediaTable": cInetNetToMediaTable,
       "cInetNetToMediaEntry": cInetNetToMediaEntry,
       "cInetNetToMediaNetAddressType": cInetNetToMediaNetAddressType,
       "cInetNetToMediaNetAddress": cInetNetToMediaNetAddress,
       "cInetNetToMediaPhysAddress": cInetNetToMediaPhysAddress,
       "cInetNetToMediaLastUpdated": cInetNetToMediaLastUpdated,
       "cInetNetToMediaType": cInetNetToMediaType,
       "cInetNetToMediaState": cInetNetToMediaState,
       "cIpv6ScopeIdTable": cIpv6ScopeIdTable,
       "cIpv6ScopeIdEntry": cIpv6ScopeIdEntry,
       "cIpv6ScopeIdIfIndex": cIpv6ScopeIdIfIndex,
       "cIpv6ScopeIdLinkLocal": cIpv6ScopeIdLinkLocal,
       "cIpv6ScopeIdSubnetLocal": cIpv6ScopeIdSubnetLocal,
       "cIpv6ScopeIdAdminLocal": cIpv6ScopeIdAdminLocal,
       "cIpv6ScopeIdSiteLocal": cIpv6ScopeIdSiteLocal,
       "cIpv6ScopeId6": cIpv6ScopeId6,
       "cIpv6ScopeId7": cIpv6ScopeId7,
       "cIpv6ScopeIdOrganizationLocal": cIpv6ScopeIdOrganizationLocal,
       "cIpv6ScopeId9": cIpv6ScopeId9,
       "cIpv6ScopeIdA": cIpv6ScopeIdA,
       "cIpv6ScopeIdB": cIpv6ScopeIdB,
       "cIpv6ScopeIdC": cIpv6ScopeIdC,
       "cIpv6ScopeIdD": cIpv6ScopeIdD,
       "cIpv6": cIpv6,
       "cIpv6Forwarding": cIpv6Forwarding,
       "cIpv6DefaultHopLimit": cIpv6DefaultHopLimit,
       "cIpv6InterfaceTable": cIpv6InterfaceTable,
       "cIpv6InterfaceEntry": cIpv6InterfaceEntry,
       "cIpv6InterfaceIfIndex": cIpv6InterfaceIfIndex,
       "cIpv6InterfaceEffectiveMtu": cIpv6InterfaceEffectiveMtu,
       "cIpv6InterfaceReasmMaxSize": cIpv6InterfaceReasmMaxSize,
       "cIpv6InterfaceIdentifier": cIpv6InterfaceIdentifier,
       "cIpv6InterfaceIdentifierLength": cIpv6InterfaceIdentifierLength,
       "cIpv6InterfacePhysicalAddress": cIpv6InterfacePhysicalAddress,
       "cIcmp": cIcmp,
       "cInetIcmpTable": cInetIcmpTable,
       "cInetIcmpEntry": cInetIcmpEntry,
       "cInetIcmpAFType": cInetIcmpAFType,
       "cInetIcmpIfIndex": cInetIcmpIfIndex,
       "cInetIcmpInMsgs": cInetIcmpInMsgs,
       "cInetIcmpInErrors": cInetIcmpInErrors,
       "cInetIcmpOutMsgs": cInetIcmpOutMsgs,
       "cInetIcmpOutErrors": cInetIcmpOutErrors,
       "cInetIcmpMsgTable": cInetIcmpMsgTable,
       "cInetIcmpMsgEntry": cInetIcmpMsgEntry,
       "cInetIcmpMsgAFType": cInetIcmpMsgAFType,
       "cInetIcmpMsgIfIndex": cInetIcmpMsgIfIndex,
       "cInetIcmpMsgType": cInetIcmpMsgType,
       "cInetIcmpMsgCode": cInetIcmpMsgCode,
       "cInetIcmpMsgInPkts": cInetIcmpMsgInPkts,
       "cInetIcmpMsgOutPkts": cInetIcmpMsgOutPkts,
       "ciscoIpMIBConformance": ciscoIpMIBConformance,
       "ciscoIpMIBCompliances": ciscoIpMIBCompliances,
       "ciscoIpMIBCompliance": ciscoIpMIBCompliance,
       "ciscoIpMIBGroups": ciscoIpMIBGroups,
       "ciscoIpAddressPfxGroup": ciscoIpAddressPfxGroup,
       "ciscoIpAddressGroup": ciscoIpAddressGroup,
       "ciscoInetNetToMediaGroup": ciscoInetNetToMediaGroup,
       "ciscoInetIcmpGroup": ciscoInetIcmpGroup,
       "ciscoInetIcmpMsgGroup": ciscoInetIcmpMsgGroup,
       "ciscoIpv6GeneralGroup": ciscoIpv6GeneralGroup,
       "ciscoIpv6InterfaceGroup": ciscoIpv6InterfaceGroup,
       "ciscoIpv6ScopeGroup": ciscoIpv6ScopeGroup}
)
