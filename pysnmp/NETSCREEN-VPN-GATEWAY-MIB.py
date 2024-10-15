# SNMP MIB module (NETSCREEN-VPN-GATEWAY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NETSCREEN-VPN-GATEWAY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:27:02 2024
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

(netscreenVpn,
 netscreenVpnMibModule) = mibBuilder.importSymbols(
    "NETSCREEN-SMI",
    "netscreenVpn",
    "netscreenVpnMibModule")

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

netscreenVpnGatewayMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 4, 0, 4)
)
netscreenVpnGatewayMibModule.setRevisions(
        ("2004-05-03 00:00",
         "2004-03-03 00:00",
         "2003-11-13 00:00",
         "2001-09-28 00:00",
         "2001-05-14 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NsVpnGateway_ObjectIdentity = ObjectIdentity
nsVpnGateway = _NsVpnGateway_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 4, 4)
)
_NsVpnGwTable_Object = MibTable
nsVpnGwTable = _NsVpnGwTable_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 4, 1)
)
if mibBuilder.loadTexts:
    nsVpnGwTable.setStatus("current")
_NsVpnGwEntry_Object = MibTableRow
nsVpnGwEntry = _NsVpnGwEntry_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 4, 1, 1)
)
nsVpnGwEntry.setIndexNames(
    (0, "NETSCREEN-VPN-GATEWAY-MIB", "nsVpnGwIndex"),
)
if mibBuilder.loadTexts:
    nsVpnGwEntry.setStatus("current")


class _NsVpnGwIndex_Type(Integer32):
    """Custom type nsVpnGwIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_NsVpnGwIndex_Type.__name__ = "Integer32"
_NsVpnGwIndex_Object = MibTableColumn
nsVpnGwIndex = _NsVpnGwIndex_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 4, 1, 1, 1),
    _NsVpnGwIndex_Type()
)
nsVpnGwIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnGwIndex.setStatus("current")


class _NsVpnGwName_Type(DisplayString):
    """Custom type nsVpnGwName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NsVpnGwName_Type.__name__ = "DisplayString"
_NsVpnGwName_Object = MibTableColumn
nsVpnGwName = _NsVpnGwName_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 4, 1, 1, 2),
    _NsVpnGwName_Type()
)
nsVpnGwName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnGwName.setStatus("current")


class _NsVpnGwRemoteType_Type(Integer32):
    """Custom type nsVpnGwRemoteType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dialup-user", 3),
          ("dynamic-ip", 1),
          ("static-ip", 0))
    )


_NsVpnGwRemoteType_Type.__name__ = "Integer32"
_NsVpnGwRemoteType_Object = MibTableColumn
nsVpnGwRemoteType = _NsVpnGwRemoteType_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 4, 1, 1, 3),
    _NsVpnGwRemoteType_Type()
)
nsVpnGwRemoteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnGwRemoteType.setStatus("current")
_NsVpnGwRemoteStaticIp_Type = IpAddress
_NsVpnGwRemoteStaticIp_Object = MibTableColumn
nsVpnGwRemoteStaticIp = _NsVpnGwRemoteStaticIp_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 4, 1, 1, 4),
    _NsVpnGwRemoteStaticIp_Type()
)
nsVpnGwRemoteStaticIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnGwRemoteStaticIp.setStatus("current")


class _NsVpnGwRemotePeerId_Type(DisplayString):
    """Custom type nsVpnGwRemotePeerId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NsVpnGwRemotePeerId_Type.__name__ = "DisplayString"
_NsVpnGwRemotePeerId_Object = MibTableColumn
nsVpnGwRemotePeerId = _NsVpnGwRemotePeerId_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 4, 1, 1, 5),
    _NsVpnGwRemotePeerId_Type()
)
nsVpnGwRemotePeerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnGwRemotePeerId.setStatus("current")


class _NsVpnGwDialup_Type(DisplayString):
    """Custom type nsVpnGwDialup based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NsVpnGwDialup_Type.__name__ = "DisplayString"
_NsVpnGwDialup_Object = MibTableColumn
nsVpnGwDialup = _NsVpnGwDialup_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 4, 1, 1, 6),
    _NsVpnGwDialup_Type()
)
nsVpnGwDialup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnGwDialup.setStatus("current")


class _NsVpnGwInitMode_Type(Integer32):
    """Custom type nsVpnGwInitMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("aggressive", 1),
          ("main", 0))
    )


_NsVpnGwInitMode_Type.__name__ = "Integer32"
_NsVpnGwInitMode_Object = MibTableColumn
nsVpnGwInitMode = _NsVpnGwInitMode_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 4, 1, 1, 7),
    _NsVpnGwInitMode_Type()
)
nsVpnGwInitMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnGwInitMode.setStatus("current")


class _NsVpnGwPhOnePropOne_Type(DisplayString):
    """Custom type nsVpnGwPhOnePropOne based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NsVpnGwPhOnePropOne_Type.__name__ = "DisplayString"
_NsVpnGwPhOnePropOne_Object = MibTableColumn
nsVpnGwPhOnePropOne = _NsVpnGwPhOnePropOne_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 4, 1, 1, 8),
    _NsVpnGwPhOnePropOne_Type()
)
nsVpnGwPhOnePropOne.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnGwPhOnePropOne.setStatus("current")


class _NsVpnGwPhOnePropTwo_Type(DisplayString):
    """Custom type nsVpnGwPhOnePropTwo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NsVpnGwPhOnePropTwo_Type.__name__ = "DisplayString"
_NsVpnGwPhOnePropTwo_Object = MibTableColumn
nsVpnGwPhOnePropTwo = _NsVpnGwPhOnePropTwo_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 4, 1, 1, 9),
    _NsVpnGwPhOnePropTwo_Type()
)
nsVpnGwPhOnePropTwo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnGwPhOnePropTwo.setStatus("current")


class _NsVpnGwPhOnePropThree_Type(DisplayString):
    """Custom type nsVpnGwPhOnePropThree based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NsVpnGwPhOnePropThree_Type.__name__ = "DisplayString"
_NsVpnGwPhOnePropThree_Object = MibTableColumn
nsVpnGwPhOnePropThree = _NsVpnGwPhOnePropThree_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 4, 1, 1, 10),
    _NsVpnGwPhOnePropThree_Type()
)
nsVpnGwPhOnePropThree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnGwPhOnePropThree.setStatus("current")


class _NsVpnGwPhOnePropFour_Type(DisplayString):
    """Custom type nsVpnGwPhOnePropFour based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NsVpnGwPhOnePropFour_Type.__name__ = "DisplayString"
_NsVpnGwPhOnePropFour_Object = MibTableColumn
nsVpnGwPhOnePropFour = _NsVpnGwPhOnePropFour_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 4, 1, 1, 11),
    _NsVpnGwPhOnePropFour_Type()
)
nsVpnGwPhOnePropFour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnGwPhOnePropFour.setStatus("current")


class _NsVpnGwCertLocal_Type(DisplayString):
    """Custom type nsVpnGwCertLocal based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NsVpnGwCertLocal_Type.__name__ = "DisplayString"
_NsVpnGwCertLocal_Object = MibTableColumn
nsVpnGwCertLocal = _NsVpnGwCertLocal_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 4, 1, 1, 12),
    _NsVpnGwCertLocal_Type()
)
nsVpnGwCertLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnGwCertLocal.setStatus("current")


class _NsVpnGwPeerCa_Type(DisplayString):
    """Custom type nsVpnGwPeerCa based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NsVpnGwPeerCa_Type.__name__ = "DisplayString"
_NsVpnGwPeerCa_Object = MibTableColumn
nsVpnGwPeerCa = _NsVpnGwPeerCa_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 4, 1, 1, 13),
    _NsVpnGwPeerCa_Type()
)
nsVpnGwPeerCa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnGwPeerCa.setStatus("current")


class _NsVpnGwPeerType_Type(Integer32):
    """Custom type nsVpnGwPeerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
        *(("arl", 8),
          ("crl", 7),
          ("dns", 3),
          ("keerberos", 6),
          ("none", 0),
          ("pgp", 2),
          ("pkcs7", 1),
          ("spki", 9),
          ("x509-att", 10),
          ("x509-ke", 5),
          ("x509-sig", 4))
    )


_NsVpnGwPeerType_Type.__name__ = "Integer32"
_NsVpnGwPeerType_Object = MibTableColumn
nsVpnGwPeerType = _NsVpnGwPeerType_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 4, 1, 1, 14),
    _NsVpnGwPeerType_Type()
)
nsVpnGwPeerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnGwPeerType.setStatus("current")
_NsVpnGwVsys_Type = Integer32
_NsVpnGwVsys_Object = MibTableColumn
nsVpnGwVsys = _NsVpnGwVsys_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 4, 1, 1, 15),
    _NsVpnGwVsys_Type()
)
nsVpnGwVsys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnGwVsys.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NETSCREEN-VPN-GATEWAY-MIB",
    **{"netscreenVpnGatewayMibModule": netscreenVpnGatewayMibModule,
       "nsVpnGateway": nsVpnGateway,
       "nsVpnGwTable": nsVpnGwTable,
       "nsVpnGwEntry": nsVpnGwEntry,
       "nsVpnGwIndex": nsVpnGwIndex,
       "nsVpnGwName": nsVpnGwName,
       "nsVpnGwRemoteType": nsVpnGwRemoteType,
       "nsVpnGwRemoteStaticIp": nsVpnGwRemoteStaticIp,
       "nsVpnGwRemotePeerId": nsVpnGwRemotePeerId,
       "nsVpnGwDialup": nsVpnGwDialup,
       "nsVpnGwInitMode": nsVpnGwInitMode,
       "nsVpnGwPhOnePropOne": nsVpnGwPhOnePropOne,
       "nsVpnGwPhOnePropTwo": nsVpnGwPhOnePropTwo,
       "nsVpnGwPhOnePropThree": nsVpnGwPhOnePropThree,
       "nsVpnGwPhOnePropFour": nsVpnGwPhOnePropFour,
       "nsVpnGwCertLocal": nsVpnGwCertLocal,
       "nsVpnGwPeerCa": nsVpnGwPeerCa,
       "nsVpnGwPeerType": nsVpnGwPeerType,
       "nsVpnGwVsys": nsVpnGwVsys}
)
