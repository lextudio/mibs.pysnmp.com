# SNMP MIB module (HH3C-IPSEC-MONITOR-V2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-IPSEC-MONITOR-V2-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:53:39 2024
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

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hh3cIPsecMonitorV2 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126)
)
hh3cIPsecMonitorV2.setRevisions(
        ("2012-06-27 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Hh3cIPsecDiffHellmanGrpV2(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              5,
              14,
              24,
              2147483647)
        )
    )
    namedValues = NamedValues(
        *(("dhGroup1", 1),
          ("dhGroup14", 14),
          ("dhGroup2", 2),
          ("dhGroup24", 24),
          ("dhGroup5", 5),
          ("invalidGroup", 2147483647),
          ("none", 0))
    )



class Hh3cIPsecEncapModeV2(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              2147483647)
        )
    )
    namedValues = NamedValues(
        *(("invalidMode", 2147483647),
          ("transport", 2),
          ("tunnel", 1))
    )



class Hh3cIPsecEncryptAlgoV2(Integer32, TextualConvention):
    status = "current"
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
              10,
              11,
              12,
              13,
              14,
              2147483647)
        )
    )
    namedValues = NamedValues(
        *(("aesCamelliaCbc", 13),
          ("aesCbc", 7),
          ("aesCbc128", 9),
          ("aesCbc192", 10),
          ("aesCbc256", 11),
          ("aesCtr", 12),
          ("blowfishCbc", 3),
          ("castCbc", 6),
          ("desCbc", 1),
          ("ideaCbc", 2),
          ("invalidAlg", 2147483647),
          ("none", 0),
          ("nsaCbc", 8),
          ("rc4", 14),
          ("rc5R16B64Cbc", 4),
          ("tripleDesCbc", 5))
    )



class Hh3cIPsecAuthAlgoV2(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              2147483647)
        )
    )
    namedValues = NamedValues(
        *(("invalidAlg", 2147483647),
          ("md5", 1),
          ("none", 0),
          ("sha1", 2),
          ("sha256", 3),
          ("sha384", 4),
          ("sha512", 5))
    )



class Hh3cIPsecSaProtocolV2(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("ah", 2),
          ("esp", 3),
          ("ipcomp", 4),
          ("reserved", 0))
    )



class Hh3cIPsecIDTypeV2(Integer32, TextualConvention):
    status = "current"
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
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("derAsn1Dn", 9),
          ("derAsn1Gn", 10),
          ("fqdn", 2),
          ("ipv4Addr", 1),
          ("ipv4AddrRange", 7),
          ("ipv4AddrSubnet", 4),
          ("ipv6Addr", 5),
          ("ipv6AddrRange", 8),
          ("ipv6AddrSubnet", 6),
          ("keyId", 11),
          ("reserved", 0),
          ("userFqdn", 3))
    )



class Hh3cIPsecTrafficTypeV2(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("ipv4Addr", 1),
          ("ipv4AddrRange", 7),
          ("ipv4AddrSubnet", 4),
          ("ipv6Addr", 5),
          ("ipv6AddrRange", 8),
          ("ipv6AddrSubnet", 6))
    )



class Hh3cIPsecNegoTypeV2(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              2147483647)
        )
    )
    namedValues = NamedValues(
        *(("ike", 1),
          ("invalidType", 2147483647),
          ("manual", 2))
    )



class Hh3cIPsecTunnelStateV2(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("timeout", 2))
    )



# MIB Managed Objects in the order of their OIDs

_Hh3cIPsecObjectsV2_ObjectIdentity = ObjectIdentity
hh3cIPsecObjectsV2 = _Hh3cIPsecObjectsV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1)
)
_Hh3cIPsecScalarObjectsV2_ObjectIdentity = ObjectIdentity
hh3cIPsecScalarObjectsV2 = _Hh3cIPsecScalarObjectsV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 1)
)
_Hh3cIPsecMIBVersion_Type = DisplayString
_Hh3cIPsecMIBVersion_Object = MibScalar
hh3cIPsecMIBVersion = _Hh3cIPsecMIBVersion_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 1, 1),
    _Hh3cIPsecMIBVersion_Type()
)
hh3cIPsecMIBVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPsecMIBVersion.setStatus("current")
_Hh3cIPsecTunnelV2Table_Object = MibTable
hh3cIPsecTunnelV2Table = _Hh3cIPsecTunnelV2Table_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 2)
)
if mibBuilder.loadTexts:
    hh3cIPsecTunnelV2Table.setStatus("current")
_Hh3cIPsecTunnelV2Entry_Object = MibTableRow
hh3cIPsecTunnelV2Entry = _Hh3cIPsecTunnelV2Entry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 2, 1)
)
hh3cIPsecTunnelV2Entry.setIndexNames(
    (0, "HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecTunIndexV2"),
)
if mibBuilder.loadTexts:
    hh3cIPsecTunnelV2Entry.setStatus("current")


class _Hh3cIPsecTunIndexV2_Type(Integer32):
    """Custom type hh3cIPsecTunIndexV2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cIPsecTunIndexV2_Type.__name__ = "Integer32"
_Hh3cIPsecTunIndexV2_Object = MibTableColumn
hh3cIPsecTunIndexV2 = _Hh3cIPsecTunIndexV2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 2, 1, 1),
    _Hh3cIPsecTunIndexV2_Type()
)
hh3cIPsecTunIndexV2.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cIPsecTunIndexV2.setStatus("current")
_Hh3cIPsecTunIfIndexV2_Type = InterfaceIndex
_Hh3cIPsecTunIfIndexV2_Object = MibTableColumn
hh3cIPsecTunIfIndexV2 = _Hh3cIPsecTunIfIndexV2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 2, 1, 2),
    _Hh3cIPsecTunIfIndexV2_Type()
)
hh3cIPsecTunIfIndexV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPsecTunIfIndexV2.setStatus("current")


class _Hh3cIPsecTunIKETunnelIndexV2_Type(Integer32):
    """Custom type hh3cIPsecTunIKETunnelIndexV2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cIPsecTunIKETunnelIndexV2_Type.__name__ = "Integer32"
_Hh3cIPsecTunIKETunnelIndexV2_Object = MibTableColumn
hh3cIPsecTunIKETunnelIndexV2 = _Hh3cIPsecTunIKETunnelIndexV2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 2, 1, 3),
    _Hh3cIPsecTunIKETunnelIndexV2_Type()
)
hh3cIPsecTunIKETunnelIndexV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPsecTunIKETunnelIndexV2.setStatus("current")
_Hh3cIPsecTunIKETunLocalIDTypeV2_Type = Hh3cIPsecIDTypeV2
_Hh3cIPsecTunIKETunLocalIDTypeV2_Object = MibTableColumn
hh3cIPsecTunIKETunLocalIDTypeV2 = _Hh3cIPsecTunIKETunLocalIDTypeV2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 2, 1, 4),
    _Hh3cIPsecTunIKETunLocalIDTypeV2_Type()
)
hh3cIPsecTunIKETunLocalIDTypeV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPsecTunIKETunLocalIDTypeV2.setStatus("current")
_Hh3cIPsecTunIKETunLocalIDVal1V2_Type = DisplayString
_Hh3cIPsecTunIKETunLocalIDVal1V2_Object = MibTableColumn
hh3cIPsecTunIKETunLocalIDVal1V2 = _Hh3cIPsecTunIKETunLocalIDVal1V2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 2, 1, 5),
    _Hh3cIPsecTunIKETunLocalIDVal1V2_Type()
)
hh3cIPsecTunIKETunLocalIDVal1V2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPsecTunIKETunLocalIDVal1V2.setStatus("current")
_Hh3cIPsecTunIKETunLocalIDVal2V2_Type = DisplayString
_Hh3cIPsecTunIKETunLocalIDVal2V2_Object = MibTableColumn
hh3cIPsecTunIKETunLocalIDVal2V2 = _Hh3cIPsecTunIKETunLocalIDVal2V2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 2, 1, 6),
    _Hh3cIPsecTunIKETunLocalIDVal2V2_Type()
)
hh3cIPsecTunIKETunLocalIDVal2V2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPsecTunIKETunLocalIDVal2V2.setStatus("current")
_Hh3cIPsecTunIKETunRemoteIDTypeV2_Type = Hh3cIPsecIDTypeV2
_Hh3cIPsecTunIKETunRemoteIDTypeV2_Object = MibTableColumn
hh3cIPsecTunIKETunRemoteIDTypeV2 = _Hh3cIPsecTunIKETunRemoteIDTypeV2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 2, 1, 7),
    _Hh3cIPsecTunIKETunRemoteIDTypeV2_Type()
)
hh3cIPsecTunIKETunRemoteIDTypeV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPsecTunIKETunRemoteIDTypeV2.setStatus("current")
_Hh3cIPsecTunIKETunRemoteIDVal1V2_Type = DisplayString
_Hh3cIPsecTunIKETunRemoteIDVal1V2_Object = MibTableColumn
hh3cIPsecTunIKETunRemoteIDVal1V2 = _Hh3cIPsecTunIKETunRemoteIDVal1V2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 2, 1, 8),
    _Hh3cIPsecTunIKETunRemoteIDVal1V2_Type()
)
hh3cIPsecTunIKETunRemoteIDVal1V2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPsecTunIKETunRemoteIDVal1V2.setStatus("current")
_Hh3cIPsecTunIKETunRemoteIDVal2V2_Type = DisplayString
_Hh3cIPsecTunIKETunRemoteIDVal2V2_Object = MibTableColumn
hh3cIPsecTunIKETunRemoteIDVal2V2 = _Hh3cIPsecTunIKETunRemoteIDVal2V2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 2, 1, 9),
    _Hh3cIPsecTunIKETunRemoteIDVal2V2_Type()
)
hh3cIPsecTunIKETunRemoteIDVal2V2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPsecTunIKETunRemoteIDVal2V2.setStatus("current")
_Hh3cIPsecTunLocalAddrTypeV2_Type = InetAddressType
_Hh3cIPsecTunLocalAddrTypeV2_Object = MibTableColumn
hh3cIPsecTunLocalAddrTypeV2 = _Hh3cIPsecTunLocalAddrTypeV2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 2, 1, 10),
    _Hh3cIPsecTunLocalAddrTypeV2_Type()
)
hh3cIPsecTunLocalAddrTypeV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPsecTunLocalAddrTypeV2.setStatus("current")
_Hh3cIPsecTunLocalAddrV2_Type = InetAddress
_Hh3cIPsecTunLocalAddrV2_Object = MibTableColumn
hh3cIPsecTunLocalAddrV2 = _Hh3cIPsecTunLocalAddrV2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 2, 1, 11),
    _Hh3cIPsecTunLocalAddrV2_Type()
)
hh3cIPsecTunLocalAddrV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPsecTunLocalAddrV2.setStatus("current")
_Hh3cIPsecTunRemoteAddrTypeV2_Type = InetAddressType
_Hh3cIPsecTunRemoteAddrTypeV2_Object = MibTableColumn
hh3cIPsecTunRemoteAddrTypeV2 = _Hh3cIPsecTunRemoteAddrTypeV2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 2, 1, 12),
    _Hh3cIPsecTunRemoteAddrTypeV2_Type()
)
hh3cIPsecTunRemoteAddrTypeV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPsecTunRemoteAddrTypeV2.setStatus("current")
_Hh3cIPsecTunRemoteAddrV2_Type = InetAddress
_Hh3cIPsecTunRemoteAddrV2_Object = MibTableColumn
hh3cIPsecTunRemoteAddrV2 = _Hh3cIPsecTunRemoteAddrV2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 2, 1, 13),
    _Hh3cIPsecTunRemoteAddrV2_Type()
)
hh3cIPsecTunRemoteAddrV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPsecTunRemoteAddrV2.setStatus("current")
_Hh3cIPsecTunKeyTypeV2_Type = Hh3cIPsecNegoTypeV2
_Hh3cIPsecTunKeyTypeV2_Object = MibTableColumn
hh3cIPsecTunKeyTypeV2 = _Hh3cIPsecTunKeyTypeV2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 2, 1, 14),
    _Hh3cIPsecTunKeyTypeV2_Type()
)
hh3cIPsecTunKeyTypeV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPsecTunKeyTypeV2.setStatus("current")
_Hh3cIPsecTunEncapModeV2_Type = Hh3cIPsecEncapModeV2
_Hh3cIPsecTunEncapModeV2_Object = MibTableColumn
hh3cIPsecTunEncapModeV2 = _Hh3cIPsecTunEncapModeV2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 2, 1, 15),
    _Hh3cIPsecTunEncapModeV2_Type()
)
hh3cIPsecTunEncapModeV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPsecTunEncapModeV2.setStatus("current")


class _Hh3cIPsecTunInitiatorV2_Type(Integer32):
    """Custom type hh3cIPsecTunInitiatorV2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              2147483647)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("none", 2147483647),
          ("remote", 2))
    )


_Hh3cIPsecTunInitiatorV2_Type.__name__ = "Integer32"
_Hh3cIPsecTunInitiatorV2_Object = MibTableColumn
hh3cIPsecTunInitiatorV2 = _Hh3cIPsecTunInitiatorV2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 2, 1, 16),
    _Hh3cIPsecTunInitiatorV2_Type()
)
hh3cIPsecTunInitiatorV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPsecTunInitiatorV2.setStatus("current")
_Hh3cIPsecTunLifeSizeV2_Type = Gauge32
_Hh3cIPsecTunLifeSizeV2_Object = MibTableColumn
hh3cIPsecTunLifeSizeV2 = _Hh3cIPsecTunLifeSizeV2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 2, 1, 17),
    _Hh3cIPsecTunLifeSizeV2_Type()
)
hh3cIPsecTunLifeSizeV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPsecTunLifeSizeV2.setStatus("current")


class _Hh3cIPsecTunLifeTimeV2_Type(Integer32):
    """Custom type hh3cIPsecTunLifeTimeV2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cIPsecTunLifeTimeV2_Type.__name__ = "Integer32"
_Hh3cIPsecTunLifeTimeV2_Object = MibTableColumn
hh3cIPsecTunLifeTimeV2 = _Hh3cIPsecTunLifeTimeV2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 2, 1, 18),
    _Hh3cIPsecTunLifeTimeV2_Type()
)
hh3cIPsecTunLifeTimeV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPsecTunLifeTimeV2.setStatus("current")


class _Hh3cIPsecTunRemainTimeV2_Type(Integer32):
    """Custom type hh3cIPsecTunRemainTimeV2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hh3cIPsecTunRemainTimeV2_Type.__name__ = "Integer32"
_Hh3cIPsecTunRemainTimeV2_Object = MibTableColumn
hh3cIPsecTunRemainTimeV2 = _Hh3cIPsecTunRemainTimeV2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 2, 1, 19),
    _Hh3cIPsecTunRemainTimeV2_Type()
)
hh3cIPsecTunRemainTimeV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPsecTunRemainTimeV2.setStatus("current")


class _Hh3cIPsecTunActiveTimeV2_Type(Integer32):
    """Custom type hh3cIPsecTunActiveTimeV2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hh3cIPsecTunActiveTimeV2_Type.__name__ = "Integer32"
_Hh3cIPsecTunActiveTimeV2_Object = MibTableColumn
hh3cIPsecTunActiveTimeV2 = _Hh3cIPsecTunActiveTimeV2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 2, 1, 20),
    _Hh3cIPsecTunActiveTimeV2_Type()
)
hh3cIPsecTunActiveTimeV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPsecTunActiveTimeV2.setStatus("current")
_Hh3cIPsecTunRemainSizeV2_Type = Gauge32
_Hh3cIPsecTunRemainSizeV2_Object = MibTableColumn
hh3cIPsecTunRemainSizeV2 = _Hh3cIPsecTunRemainSizeV2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 2, 1, 21),
    _Hh3cIPsecTunRemainSizeV2_Type()
)
hh3cIPsecTunRemainSizeV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPsecTunRemainSizeV2.setStatus("current")
_Hh3cIPsecTunTotalRefreshesV2_Type = Counter32
_Hh3cIPsecTunTotalRefreshesV2_Object = MibTableColumn
hh3cIPsecTunTotalRefreshesV2 = _Hh3cIPsecTunTotalRefreshesV2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 2, 1, 22),
    _Hh3cIPsecTunTotalRefreshesV2_Type()
)
hh3cIPsecTunTotalRefreshesV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPsecTunTotalRefreshesV2.setStatus("current")
_Hh3cIPsecTunCurrentSaInstancesV2_Type = Gauge32
_Hh3cIPsecTunCurrentSaInstancesV2_Object = MibTableColumn
hh3cIPsecTunCurrentSaInstancesV2 = _Hh3cIPsecTunCurrentSaInstancesV2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 2, 1, 23),
    _Hh3cIPsecTunCurrentSaInstancesV2_Type()
)
hh3cIPsecTunCurrentSaInstancesV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPsecTunCurrentSaInstancesV2.setStatus("current")
_Hh3cIPsecTunInSaEncryptAlgoV2_Type = Hh3cIPsecEncryptAlgoV2
_Hh3cIPsecTunInSaEncryptAlgoV2_Object = MibTableColumn
hh3cIPsecTunInSaEncryptAlgoV2 = _Hh3cIPsecTunInSaEncryptAlgoV2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 2, 1, 24),
    _Hh3cIPsecTunInSaEncryptAlgoV2_Type()
)
hh3cIPsecTunInSaEncryptAlgoV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPsecTunInSaEncryptAlgoV2.setStatus("current")
_Hh3cIPsecTunInSaAhAuthAlgoV2_Type = Hh3cIPsecAuthAlgoV2
_Hh3cIPsecTunInSaAhAuthAlgoV2_Object = MibTableColumn
hh3cIPsecTunInSaAhAuthAlgoV2 = _Hh3cIPsecTunInSaAhAuthAlgoV2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 2, 1, 25),
    _Hh3cIPsecTunInSaAhAuthAlgoV2_Type()
)
hh3cIPsecTunInSaAhAuthAlgoV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPsecTunInSaAhAuthAlgoV2.setStatus("current")
_Hh3cIPsecTunInSaEspAuthAlgoV2_Type = Hh3cIPsecAuthAlgoV2
_Hh3cIPsecTunInSaEspAuthAlgoV2_Object = MibTableColumn
hh3cIPsecTunInSaEspAuthAlgoV2 = _Hh3cIPsecTunInSaEspAuthAlgoV2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 2, 1, 26),
    _Hh3cIPsecTunInSaEspAuthAlgoV2_Type()
)
hh3cIPsecTunInSaEspAuthAlgoV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPsecTunInSaEspAuthAlgoV2.setStatus("current")
_Hh3cIPsecTunDiffHellmanGrpV2_Type = Hh3cIPsecDiffHellmanGrpV2
_Hh3cIPsecTunDiffHellmanGrpV2_Object = MibTableColumn
hh3cIPsecTunDiffHellmanGrpV2 = _Hh3cIPsecTunDiffHellmanGrpV2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 2, 1, 27),
    _Hh3cIPsecTunDiffHellmanGrpV2_Type()
)
hh3cIPsecTunDiffHellmanGrpV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPsecTunDiffHellmanGrpV2.setStatus("current")
_Hh3cIPsecTunOutSaEncryptAlgoV2_Type = Hh3cIPsecEncryptAlgoV2
_Hh3cIPsecTunOutSaEncryptAlgoV2_Object = MibTableColumn
hh3cIPsecTunOutSaEncryptAlgoV2 = _Hh3cIPsecTunOutSaEncryptAlgoV2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 2, 1, 28),
    _Hh3cIPsecTunOutSaEncryptAlgoV2_Type()
)
hh3cIPsecTunOutSaEncryptAlgoV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPsecTunOutSaEncryptAlgoV2.setStatus("current")
_Hh3cIPsecTunOutSaAhAuthAlgoV2_Type = Hh3cIPsecAuthAlgoV2
_Hh3cIPsecTunOutSaAhAuthAlgoV2_Object = MibTableColumn
hh3cIPsecTunOutSaAhAuthAlgoV2 = _Hh3cIPsecTunOutSaAhAuthAlgoV2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 2, 1, 29),
    _Hh3cIPsecTunOutSaAhAuthAlgoV2_Type()
)
hh3cIPsecTunOutSaAhAuthAlgoV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPsecTunOutSaAhAuthAlgoV2.setStatus("current")
_Hh3cIPsecTunOutSaEspAuthAlgoV2_Type = Hh3cIPsecAuthAlgoV2
_Hh3cIPsecTunOutSaEspAuthAlgoV2_Object = MibTableColumn
hh3cIPsecTunOutSaEspAuthAlgoV2 = _Hh3cIPsecTunOutSaEspAuthAlgoV2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 2, 1, 30),
    _Hh3cIPsecTunOutSaEspAuthAlgoV2_Type()
)
hh3cIPsecTunOutSaEspAuthAlgoV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPsecTunOutSaEspAuthAlgoV2.setStatus("current")
_Hh3cIPsecTunPolicyNameV2_Type = DisplayString
_Hh3cIPsecTunPolicyNameV2_Object = MibTableColumn
hh3cIPsecTunPolicyNameV2 = _Hh3cIPsecTunPolicyNameV2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 2, 1, 31),
    _Hh3cIPsecTunPolicyNameV2_Type()
)
hh3cIPsecTunPolicyNameV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPsecTunPolicyNameV2.setStatus("current")


class _Hh3cIPsecTunPolicyNumV2_Type(Integer32):
    """Custom type hh3cIPsecTunPolicyNumV2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cIPsecTunPolicyNumV2_Type.__name__ = "Integer32"
_Hh3cIPsecTunPolicyNumV2_Object = MibTableColumn
hh3cIPsecTunPolicyNumV2 = _Hh3cIPsecTunPolicyNumV2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 2, 1, 32),
    _Hh3cIPsecTunPolicyNumV2_Type()
)
hh3cIPsecTunPolicyNumV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPsecTunPolicyNumV2.setStatus("current")


class _Hh3cIPsecTunStatusV2_Type(Integer32):
    """Custom type hh3cIPsecTunStatusV2 based on Integer32"""
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
        *(("closed", 4),
          ("initial", 1),
          ("ready", 2),
          ("rekeyed", 3))
    )


_Hh3cIPsecTunStatusV2_Type.__name__ = "Integer32"
_Hh3cIPsecTunStatusV2_Object = MibTableColumn
hh3cIPsecTunStatusV2 = _Hh3cIPsecTunStatusV2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 2, 1, 33),
    _Hh3cIPsecTunStatusV2_Type()
)
hh3cIPsecTunStatusV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPsecTunStatusV2.setStatus("current")
_Hh3cIPsecTunnelStatV2Table_Object = MibTable
hh3cIPsecTunnelStatV2Table = _Hh3cIPsecTunnelStatV2Table_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 3)
)
if mibBuilder.loadTexts:
    hh3cIPsecTunnelStatV2Table.setStatus("current")
_Hh3cIPsecTunnelStatV2Entry_Object = MibTableRow
hh3cIPsecTunnelStatV2Entry = _Hh3cIPsecTunnelStatV2Entry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 3, 1)
)
hh3cIPsecTunnelStatV2Entry.setIndexNames(
    (0, "HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecTunIndexV2"),
)
if mibBuilder.loadTexts:
    hh3cIPsecTunnelStatV2Entry.setStatus("current")
_Hh3cIPsecTunInOctetsV2_Type = Counter64
_Hh3cIPsecTunInOctetsV2_Object = MibTableColumn
hh3cIPsecTunInOctetsV2 = _Hh3cIPsecTunInOctetsV2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 3, 1, 1),
    _Hh3cIPsecTunInOctetsV2_Type()
)
hh3cIPsecTunInOctetsV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPsecTunInOctetsV2.setStatus("current")
_Hh3cIPsecTunInDecompOctetsV2_Type = Counter64
_Hh3cIPsecTunInDecompOctetsV2_Object = MibTableColumn
hh3cIPsecTunInDecompOctetsV2 = _Hh3cIPsecTunInDecompOctetsV2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 3, 1, 2),
    _Hh3cIPsecTunInDecompOctetsV2_Type()
)
hh3cIPsecTunInDecompOctetsV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPsecTunInDecompOctetsV2.setStatus("current")
_Hh3cIPsecTunInPktsV2_Type = Counter64
_Hh3cIPsecTunInPktsV2_Object = MibTableColumn
hh3cIPsecTunInPktsV2 = _Hh3cIPsecTunInPktsV2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 3, 1, 3),
    _Hh3cIPsecTunInPktsV2_Type()
)
hh3cIPsecTunInPktsV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPsecTunInPktsV2.setStatus("current")
_Hh3cIPsecTunInDropPktsV2_Type = Counter64
_Hh3cIPsecTunInDropPktsV2_Object = MibTableColumn
hh3cIPsecTunInDropPktsV2 = _Hh3cIPsecTunInDropPktsV2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 3, 1, 4),
    _Hh3cIPsecTunInDropPktsV2_Type()
)
hh3cIPsecTunInDropPktsV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPsecTunInDropPktsV2.setStatus("current")
_Hh3cIPsecTunInReplayDropPktsV2_Type = Counter64
_Hh3cIPsecTunInReplayDropPktsV2_Object = MibTableColumn
hh3cIPsecTunInReplayDropPktsV2 = _Hh3cIPsecTunInReplayDropPktsV2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 3, 1, 5),
    _Hh3cIPsecTunInReplayDropPktsV2_Type()
)
hh3cIPsecTunInReplayDropPktsV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPsecTunInReplayDropPktsV2.setStatus("current")
_Hh3cIPsecTunInAuthFailsV2_Type = Counter64
_Hh3cIPsecTunInAuthFailsV2_Object = MibTableColumn
hh3cIPsecTunInAuthFailsV2 = _Hh3cIPsecTunInAuthFailsV2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 3, 1, 6),
    _Hh3cIPsecTunInAuthFailsV2_Type()
)
hh3cIPsecTunInAuthFailsV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPsecTunInAuthFailsV2.setStatus("current")
_Hh3cIPsecTunInDecryptFailsV2_Type = Counter64
_Hh3cIPsecTunInDecryptFailsV2_Object = MibTableColumn
hh3cIPsecTunInDecryptFailsV2 = _Hh3cIPsecTunInDecryptFailsV2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 3, 1, 7),
    _Hh3cIPsecTunInDecryptFailsV2_Type()
)
hh3cIPsecTunInDecryptFailsV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPsecTunInDecryptFailsV2.setStatus("current")
_Hh3cIPsecTunOutOctetsV2_Type = Counter64
_Hh3cIPsecTunOutOctetsV2_Object = MibTableColumn
hh3cIPsecTunOutOctetsV2 = _Hh3cIPsecTunOutOctetsV2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 3, 1, 8),
    _Hh3cIPsecTunOutOctetsV2_Type()
)
hh3cIPsecTunOutOctetsV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPsecTunOutOctetsV2.setStatus("current")
_Hh3cIPsecTunOutUncompOctetsV2_Type = Counter64
_Hh3cIPsecTunOutUncompOctetsV2_Object = MibTableColumn
hh3cIPsecTunOutUncompOctetsV2 = _Hh3cIPsecTunOutUncompOctetsV2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 3, 1, 9),
    _Hh3cIPsecTunOutUncompOctetsV2_Type()
)
hh3cIPsecTunOutUncompOctetsV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPsecTunOutUncompOctetsV2.setStatus("current")
_Hh3cIPsecTunOutPktsV2_Type = Counter64
_Hh3cIPsecTunOutPktsV2_Object = MibTableColumn
hh3cIPsecTunOutPktsV2 = _Hh3cIPsecTunOutPktsV2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 3, 1, 10),
    _Hh3cIPsecTunOutPktsV2_Type()
)
hh3cIPsecTunOutPktsV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPsecTunOutPktsV2.setStatus("current")
_Hh3cIPsecTunOutDropPktsV2_Type = Counter64
_Hh3cIPsecTunOutDropPktsV2_Object = MibTableColumn
hh3cIPsecTunOutDropPktsV2 = _Hh3cIPsecTunOutDropPktsV2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 3, 1, 11),
    _Hh3cIPsecTunOutDropPktsV2_Type()
)
hh3cIPsecTunOutDropPktsV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPsecTunOutDropPktsV2.setStatus("current")
_Hh3cIPsecTunOutEncryptFailsV2_Type = Counter64
_Hh3cIPsecTunOutEncryptFailsV2_Object = MibTableColumn
hh3cIPsecTunOutEncryptFailsV2 = _Hh3cIPsecTunOutEncryptFailsV2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 3, 1, 12),
    _Hh3cIPsecTunOutEncryptFailsV2_Type()
)
hh3cIPsecTunOutEncryptFailsV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPsecTunOutEncryptFailsV2.setStatus("current")
_Hh3cIPsecTunNoMemoryDropPktsV2_Type = Counter64
_Hh3cIPsecTunNoMemoryDropPktsV2_Object = MibTableColumn
hh3cIPsecTunNoMemoryDropPktsV2 = _Hh3cIPsecTunNoMemoryDropPktsV2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 3, 1, 13),
    _Hh3cIPsecTunNoMemoryDropPktsV2_Type()
)
hh3cIPsecTunNoMemoryDropPktsV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPsecTunNoMemoryDropPktsV2.setStatus("current")
_Hh3cIPsecTunQueueFullDropPktsV2_Type = Counter64
_Hh3cIPsecTunQueueFullDropPktsV2_Object = MibTableColumn
hh3cIPsecTunQueueFullDropPktsV2 = _Hh3cIPsecTunQueueFullDropPktsV2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 3, 1, 14),
    _Hh3cIPsecTunQueueFullDropPktsV2_Type()
)
hh3cIPsecTunQueueFullDropPktsV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPsecTunQueueFullDropPktsV2.setStatus("current")
_Hh3cIPsecTunInvalidLenDropPktsV2_Type = Counter64
_Hh3cIPsecTunInvalidLenDropPktsV2_Object = MibTableColumn
hh3cIPsecTunInvalidLenDropPktsV2 = _Hh3cIPsecTunInvalidLenDropPktsV2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 3, 1, 15),
    _Hh3cIPsecTunInvalidLenDropPktsV2_Type()
)
hh3cIPsecTunInvalidLenDropPktsV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPsecTunInvalidLenDropPktsV2.setStatus("current")
_Hh3cIPsecTunTooLongDropPktsV2_Type = Counter64
_Hh3cIPsecTunTooLongDropPktsV2_Object = MibTableColumn
hh3cIPsecTunTooLongDropPktsV2 = _Hh3cIPsecTunTooLongDropPktsV2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 3, 1, 16),
    _Hh3cIPsecTunTooLongDropPktsV2_Type()
)
hh3cIPsecTunTooLongDropPktsV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPsecTunTooLongDropPktsV2.setStatus("current")
_Hh3cIPsecTunInvalidSaDropPktsV2_Type = Counter64
_Hh3cIPsecTunInvalidSaDropPktsV2_Object = MibTableColumn
hh3cIPsecTunInvalidSaDropPktsV2 = _Hh3cIPsecTunInvalidSaDropPktsV2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 3, 1, 17),
    _Hh3cIPsecTunInvalidSaDropPktsV2_Type()
)
hh3cIPsecTunInvalidSaDropPktsV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPsecTunInvalidSaDropPktsV2.setStatus("current")
_Hh3cIPsecSaV2Table_Object = MibTable
hh3cIPsecSaV2Table = _Hh3cIPsecSaV2Table_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 4)
)
if mibBuilder.loadTexts:
    hh3cIPsecSaV2Table.setStatus("current")
_Hh3cIPsecSaV2Entry_Object = MibTableRow
hh3cIPsecSaV2Entry = _Hh3cIPsecSaV2Entry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 4, 1)
)
hh3cIPsecSaV2Entry.setIndexNames(
    (0, "HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecTunIndexV2"),
    (0, "HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecSaIndexV2"),
)
if mibBuilder.loadTexts:
    hh3cIPsecSaV2Entry.setStatus("current")


class _Hh3cIPsecSaIndexV2_Type(Integer32):
    """Custom type hh3cIPsecSaIndexV2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cIPsecSaIndexV2_Type.__name__ = "Integer32"
_Hh3cIPsecSaIndexV2_Object = MibTableColumn
hh3cIPsecSaIndexV2 = _Hh3cIPsecSaIndexV2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 4, 1, 1),
    _Hh3cIPsecSaIndexV2_Type()
)
hh3cIPsecSaIndexV2.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cIPsecSaIndexV2.setStatus("current")


class _Hh3cIPsecSaDirectionV2_Type(Integer32):
    """Custom type hh3cIPsecSaDirectionV2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("in", 1),
          ("out", 2))
    )


_Hh3cIPsecSaDirectionV2_Type.__name__ = "Integer32"
_Hh3cIPsecSaDirectionV2_Object = MibTableColumn
hh3cIPsecSaDirectionV2 = _Hh3cIPsecSaDirectionV2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 4, 1, 2),
    _Hh3cIPsecSaDirectionV2_Type()
)
hh3cIPsecSaDirectionV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPsecSaDirectionV2.setStatus("current")


class _Hh3cIPsecSaSpiValueV2_Type(Unsigned32):
    """Custom type hh3cIPsecSaSpiValueV2 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Hh3cIPsecSaSpiValueV2_Type.__name__ = "Unsigned32"
_Hh3cIPsecSaSpiValueV2_Object = MibTableColumn
hh3cIPsecSaSpiValueV2 = _Hh3cIPsecSaSpiValueV2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 4, 1, 3),
    _Hh3cIPsecSaSpiValueV2_Type()
)
hh3cIPsecSaSpiValueV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPsecSaSpiValueV2.setStatus("current")
_Hh3cIPsecSaSecProtocolV2_Type = Hh3cIPsecSaProtocolV2
_Hh3cIPsecSaSecProtocolV2_Object = MibTableColumn
hh3cIPsecSaSecProtocolV2 = _Hh3cIPsecSaSecProtocolV2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 4, 1, 4),
    _Hh3cIPsecSaSecProtocolV2_Type()
)
hh3cIPsecSaSecProtocolV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPsecSaSecProtocolV2.setStatus("current")
_Hh3cIPsecSaEncryptAlgoV2_Type = Hh3cIPsecEncryptAlgoV2
_Hh3cIPsecSaEncryptAlgoV2_Object = MibTableColumn
hh3cIPsecSaEncryptAlgoV2 = _Hh3cIPsecSaEncryptAlgoV2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 4, 1, 5),
    _Hh3cIPsecSaEncryptAlgoV2_Type()
)
hh3cIPsecSaEncryptAlgoV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPsecSaEncryptAlgoV2.setStatus("current")
_Hh3cIPsecSaAuthAlgoV2_Type = Hh3cIPsecAuthAlgoV2
_Hh3cIPsecSaAuthAlgoV2_Object = MibTableColumn
hh3cIPsecSaAuthAlgoV2 = _Hh3cIPsecSaAuthAlgoV2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 4, 1, 6),
    _Hh3cIPsecSaAuthAlgoV2_Type()
)
hh3cIPsecSaAuthAlgoV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPsecSaAuthAlgoV2.setStatus("current")


class _Hh3cIPsecSaStatusV2_Type(Integer32):
    """Custom type hh3cIPsecSaStatusV2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("expiring", 2))
    )


_Hh3cIPsecSaStatusV2_Type.__name__ = "Integer32"
_Hh3cIPsecSaStatusV2_Object = MibTableColumn
hh3cIPsecSaStatusV2 = _Hh3cIPsecSaStatusV2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 4, 1, 7),
    _Hh3cIPsecSaStatusV2_Type()
)
hh3cIPsecSaStatusV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPsecSaStatusV2.setStatus("current")
_Hh3cIPsecTrafficV2Table_Object = MibTable
hh3cIPsecTrafficV2Table = _Hh3cIPsecTrafficV2Table_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 5)
)
if mibBuilder.loadTexts:
    hh3cIPsecTrafficV2Table.setStatus("current")
_Hh3cIPsecTrafficV2Entry_Object = MibTableRow
hh3cIPsecTrafficV2Entry = _Hh3cIPsecTrafficV2Entry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 5, 1)
)
hh3cIPsecTrafficV2Entry.setIndexNames(
    (0, "HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecTunIndexV2"),
)
if mibBuilder.loadTexts:
    hh3cIPsecTrafficV2Entry.setStatus("current")
_Hh3cIPsecTrafficLocalTypeV2_Type = Hh3cIPsecTrafficTypeV2
_Hh3cIPsecTrafficLocalTypeV2_Object = MibTableColumn
hh3cIPsecTrafficLocalTypeV2 = _Hh3cIPsecTrafficLocalTypeV2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 5, 1, 1),
    _Hh3cIPsecTrafficLocalTypeV2_Type()
)
hh3cIPsecTrafficLocalTypeV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPsecTrafficLocalTypeV2.setStatus("current")
_Hh3cIPsecTrafficLocalAddr1TypeV2_Type = InetAddressType
_Hh3cIPsecTrafficLocalAddr1TypeV2_Object = MibTableColumn
hh3cIPsecTrafficLocalAddr1TypeV2 = _Hh3cIPsecTrafficLocalAddr1TypeV2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 5, 1, 2),
    _Hh3cIPsecTrafficLocalAddr1TypeV2_Type()
)
hh3cIPsecTrafficLocalAddr1TypeV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPsecTrafficLocalAddr1TypeV2.setStatus("current")
_Hh3cIPsecTrafficLocalAddr1V2_Type = InetAddress
_Hh3cIPsecTrafficLocalAddr1V2_Object = MibTableColumn
hh3cIPsecTrafficLocalAddr1V2 = _Hh3cIPsecTrafficLocalAddr1V2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 5, 1, 3),
    _Hh3cIPsecTrafficLocalAddr1V2_Type()
)
hh3cIPsecTrafficLocalAddr1V2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPsecTrafficLocalAddr1V2.setStatus("current")
_Hh3cIPsecTrafficLocalAddr2TypeV2_Type = InetAddressType
_Hh3cIPsecTrafficLocalAddr2TypeV2_Object = MibTableColumn
hh3cIPsecTrafficLocalAddr2TypeV2 = _Hh3cIPsecTrafficLocalAddr2TypeV2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 5, 1, 4),
    _Hh3cIPsecTrafficLocalAddr2TypeV2_Type()
)
hh3cIPsecTrafficLocalAddr2TypeV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPsecTrafficLocalAddr2TypeV2.setStatus("current")
_Hh3cIPsecTrafficLocalAddr2V2_Type = InetAddress
_Hh3cIPsecTrafficLocalAddr2V2_Object = MibTableColumn
hh3cIPsecTrafficLocalAddr2V2 = _Hh3cIPsecTrafficLocalAddr2V2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 5, 1, 5),
    _Hh3cIPsecTrafficLocalAddr2V2_Type()
)
hh3cIPsecTrafficLocalAddr2V2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPsecTrafficLocalAddr2V2.setStatus("current")


class _Hh3cIPsecTrafficLocalProtocol1V2_Type(Integer32):
    """Custom type hh3cIPsecTrafficLocalProtocol1V2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Hh3cIPsecTrafficLocalProtocol1V2_Type.__name__ = "Integer32"
_Hh3cIPsecTrafficLocalProtocol1V2_Object = MibTableColumn
hh3cIPsecTrafficLocalProtocol1V2 = _Hh3cIPsecTrafficLocalProtocol1V2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 5, 1, 6),
    _Hh3cIPsecTrafficLocalProtocol1V2_Type()
)
hh3cIPsecTrafficLocalProtocol1V2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPsecTrafficLocalProtocol1V2.setStatus("current")


class _Hh3cIPsecTrafficLocalProtocol2V2_Type(Integer32):
    """Custom type hh3cIPsecTrafficLocalProtocol2V2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Hh3cIPsecTrafficLocalProtocol2V2_Type.__name__ = "Integer32"
_Hh3cIPsecTrafficLocalProtocol2V2_Object = MibTableColumn
hh3cIPsecTrafficLocalProtocol2V2 = _Hh3cIPsecTrafficLocalProtocol2V2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 5, 1, 7),
    _Hh3cIPsecTrafficLocalProtocol2V2_Type()
)
hh3cIPsecTrafficLocalProtocol2V2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPsecTrafficLocalProtocol2V2.setStatus("current")


class _Hh3cIPsecTrafficLocalPort1V2_Type(Integer32):
    """Custom type hh3cIPsecTrafficLocalPort1V2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cIPsecTrafficLocalPort1V2_Type.__name__ = "Integer32"
_Hh3cIPsecTrafficLocalPort1V2_Object = MibTableColumn
hh3cIPsecTrafficLocalPort1V2 = _Hh3cIPsecTrafficLocalPort1V2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 5, 1, 8),
    _Hh3cIPsecTrafficLocalPort1V2_Type()
)
hh3cIPsecTrafficLocalPort1V2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPsecTrafficLocalPort1V2.setStatus("current")


class _Hh3cIPsecTrafficLocalPort2V2_Type(Integer32):
    """Custom type hh3cIPsecTrafficLocalPort2V2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cIPsecTrafficLocalPort2V2_Type.__name__ = "Integer32"
_Hh3cIPsecTrafficLocalPort2V2_Object = MibTableColumn
hh3cIPsecTrafficLocalPort2V2 = _Hh3cIPsecTrafficLocalPort2V2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 5, 1, 9),
    _Hh3cIPsecTrafficLocalPort2V2_Type()
)
hh3cIPsecTrafficLocalPort2V2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPsecTrafficLocalPort2V2.setStatus("current")
_Hh3cIPsecTrafficRemoteTypeV2_Type = Hh3cIPsecTrafficTypeV2
_Hh3cIPsecTrafficRemoteTypeV2_Object = MibTableColumn
hh3cIPsecTrafficRemoteTypeV2 = _Hh3cIPsecTrafficRemoteTypeV2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 5, 1, 10),
    _Hh3cIPsecTrafficRemoteTypeV2_Type()
)
hh3cIPsecTrafficRemoteTypeV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPsecTrafficRemoteTypeV2.setStatus("current")
_Hh3cIPsecTrafficRemAddr1TypeV2_Type = InetAddressType
_Hh3cIPsecTrafficRemAddr1TypeV2_Object = MibTableColumn
hh3cIPsecTrafficRemAddr1TypeV2 = _Hh3cIPsecTrafficRemAddr1TypeV2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 5, 1, 11),
    _Hh3cIPsecTrafficRemAddr1TypeV2_Type()
)
hh3cIPsecTrafficRemAddr1TypeV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPsecTrafficRemAddr1TypeV2.setStatus("current")
_Hh3cIPsecTrafficRemAddr1V2_Type = InetAddress
_Hh3cIPsecTrafficRemAddr1V2_Object = MibTableColumn
hh3cIPsecTrafficRemAddr1V2 = _Hh3cIPsecTrafficRemAddr1V2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 5, 1, 12),
    _Hh3cIPsecTrafficRemAddr1V2_Type()
)
hh3cIPsecTrafficRemAddr1V2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPsecTrafficRemAddr1V2.setStatus("current")
_Hh3cIPsecTrafficRemAddr2TypeV2_Type = InetAddressType
_Hh3cIPsecTrafficRemAddr2TypeV2_Object = MibTableColumn
hh3cIPsecTrafficRemAddr2TypeV2 = _Hh3cIPsecTrafficRemAddr2TypeV2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 5, 1, 13),
    _Hh3cIPsecTrafficRemAddr2TypeV2_Type()
)
hh3cIPsecTrafficRemAddr2TypeV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPsecTrafficRemAddr2TypeV2.setStatus("current")
_Hh3cIPsecTrafficRemAddr2V2_Type = InetAddress
_Hh3cIPsecTrafficRemAddr2V2_Object = MibTableColumn
hh3cIPsecTrafficRemAddr2V2 = _Hh3cIPsecTrafficRemAddr2V2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 5, 1, 14),
    _Hh3cIPsecTrafficRemAddr2V2_Type()
)
hh3cIPsecTrafficRemAddr2V2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPsecTrafficRemAddr2V2.setStatus("current")


class _Hh3cIPsecTrafficRemoPro1V2_Type(Integer32):
    """Custom type hh3cIPsecTrafficRemoPro1V2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Hh3cIPsecTrafficRemoPro1V2_Type.__name__ = "Integer32"
_Hh3cIPsecTrafficRemoPro1V2_Object = MibTableColumn
hh3cIPsecTrafficRemoPro1V2 = _Hh3cIPsecTrafficRemoPro1V2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 5, 1, 15),
    _Hh3cIPsecTrafficRemoPro1V2_Type()
)
hh3cIPsecTrafficRemoPro1V2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPsecTrafficRemoPro1V2.setStatus("current")


class _Hh3cIPsecTrafficRemoPro2V2_Type(Integer32):
    """Custom type hh3cIPsecTrafficRemoPro2V2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Hh3cIPsecTrafficRemoPro2V2_Type.__name__ = "Integer32"
_Hh3cIPsecTrafficRemoPro2V2_Object = MibTableColumn
hh3cIPsecTrafficRemoPro2V2 = _Hh3cIPsecTrafficRemoPro2V2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 5, 1, 16),
    _Hh3cIPsecTrafficRemoPro2V2_Type()
)
hh3cIPsecTrafficRemoPro2V2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPsecTrafficRemoPro2V2.setStatus("current")


class _Hh3cIPsecTrafficRemPort1V2_Type(Integer32):
    """Custom type hh3cIPsecTrafficRemPort1V2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cIPsecTrafficRemPort1V2_Type.__name__ = "Integer32"
_Hh3cIPsecTrafficRemPort1V2_Object = MibTableColumn
hh3cIPsecTrafficRemPort1V2 = _Hh3cIPsecTrafficRemPort1V2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 5, 1, 17),
    _Hh3cIPsecTrafficRemPort1V2_Type()
)
hh3cIPsecTrafficRemPort1V2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPsecTrafficRemPort1V2.setStatus("current")


class _Hh3cIPsecTrafficRemPort2V2_Type(Integer32):
    """Custom type hh3cIPsecTrafficRemPort2V2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cIPsecTrafficRemPort2V2_Type.__name__ = "Integer32"
_Hh3cIPsecTrafficRemPort2V2_Object = MibTableColumn
hh3cIPsecTrafficRemPort2V2 = _Hh3cIPsecTrafficRemPort2V2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 5, 1, 18),
    _Hh3cIPsecTrafficRemPort2V2_Type()
)
hh3cIPsecTrafficRemPort2V2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPsecTrafficRemPort2V2.setStatus("current")
_Hh3cIPsecGlobalStatsV2_ObjectIdentity = ObjectIdentity
hh3cIPsecGlobalStatsV2 = _Hh3cIPsecGlobalStatsV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 6)
)
_Hh3cIPsecGlobalActiveTunnelsV2_Type = Gauge32
_Hh3cIPsecGlobalActiveTunnelsV2_Object = MibScalar
hh3cIPsecGlobalActiveTunnelsV2 = _Hh3cIPsecGlobalActiveTunnelsV2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 6, 1),
    _Hh3cIPsecGlobalActiveTunnelsV2_Type()
)
hh3cIPsecGlobalActiveTunnelsV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPsecGlobalActiveTunnelsV2.setStatus("current")
_Hh3cIPsecGlobalActiveSasV2_Type = Gauge32
_Hh3cIPsecGlobalActiveSasV2_Object = MibScalar
hh3cIPsecGlobalActiveSasV2 = _Hh3cIPsecGlobalActiveSasV2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 6, 2),
    _Hh3cIPsecGlobalActiveSasV2_Type()
)
hh3cIPsecGlobalActiveSasV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPsecGlobalActiveSasV2.setStatus("current")
_Hh3cIPsecGlobalInOctetsV2_Type = Counter64
_Hh3cIPsecGlobalInOctetsV2_Object = MibScalar
hh3cIPsecGlobalInOctetsV2 = _Hh3cIPsecGlobalInOctetsV2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 6, 3),
    _Hh3cIPsecGlobalInOctetsV2_Type()
)
hh3cIPsecGlobalInOctetsV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPsecGlobalInOctetsV2.setStatus("current")
_Hh3cIPsecGlobalInDecompOctetsV2_Type = Counter64
_Hh3cIPsecGlobalInDecompOctetsV2_Object = MibScalar
hh3cIPsecGlobalInDecompOctetsV2 = _Hh3cIPsecGlobalInDecompOctetsV2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 6, 4),
    _Hh3cIPsecGlobalInDecompOctetsV2_Type()
)
hh3cIPsecGlobalInDecompOctetsV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPsecGlobalInDecompOctetsV2.setStatus("current")
_Hh3cIPsecGlobalInPktsV2_Type = Counter64
_Hh3cIPsecGlobalInPktsV2_Object = MibScalar
hh3cIPsecGlobalInPktsV2 = _Hh3cIPsecGlobalInPktsV2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 6, 5),
    _Hh3cIPsecGlobalInPktsV2_Type()
)
hh3cIPsecGlobalInPktsV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPsecGlobalInPktsV2.setStatus("current")
_Hh3cIPsecGlobalInDropsV2_Type = Counter64
_Hh3cIPsecGlobalInDropsV2_Object = MibScalar
hh3cIPsecGlobalInDropsV2 = _Hh3cIPsecGlobalInDropsV2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 6, 6),
    _Hh3cIPsecGlobalInDropsV2_Type()
)
hh3cIPsecGlobalInDropsV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPsecGlobalInDropsV2.setStatus("current")
_Hh3cIPsecGlobalInReplayDropsV2_Type = Counter64
_Hh3cIPsecGlobalInReplayDropsV2_Object = MibScalar
hh3cIPsecGlobalInReplayDropsV2 = _Hh3cIPsecGlobalInReplayDropsV2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 6, 7),
    _Hh3cIPsecGlobalInReplayDropsV2_Type()
)
hh3cIPsecGlobalInReplayDropsV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPsecGlobalInReplayDropsV2.setStatus("current")
_Hh3cIPsecGlobalInAuthFailsV2_Type = Counter64
_Hh3cIPsecGlobalInAuthFailsV2_Object = MibScalar
hh3cIPsecGlobalInAuthFailsV2 = _Hh3cIPsecGlobalInAuthFailsV2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 6, 8),
    _Hh3cIPsecGlobalInAuthFailsV2_Type()
)
hh3cIPsecGlobalInAuthFailsV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPsecGlobalInAuthFailsV2.setStatus("current")
_Hh3cIPsecGlobalInDecryptFailsV2_Type = Counter64
_Hh3cIPsecGlobalInDecryptFailsV2_Object = MibScalar
hh3cIPsecGlobalInDecryptFailsV2 = _Hh3cIPsecGlobalInDecryptFailsV2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 6, 9),
    _Hh3cIPsecGlobalInDecryptFailsV2_Type()
)
hh3cIPsecGlobalInDecryptFailsV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPsecGlobalInDecryptFailsV2.setStatus("current")
_Hh3cIPsecGlobalOutOctetsV2_Type = Counter64
_Hh3cIPsecGlobalOutOctetsV2_Object = MibScalar
hh3cIPsecGlobalOutOctetsV2 = _Hh3cIPsecGlobalOutOctetsV2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 6, 10),
    _Hh3cIPsecGlobalOutOctetsV2_Type()
)
hh3cIPsecGlobalOutOctetsV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPsecGlobalOutOctetsV2.setStatus("current")
_Hh3cIPsecGlobalOutUncompOctetsV2_Type = Counter64
_Hh3cIPsecGlobalOutUncompOctetsV2_Object = MibScalar
hh3cIPsecGlobalOutUncompOctetsV2 = _Hh3cIPsecGlobalOutUncompOctetsV2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 6, 11),
    _Hh3cIPsecGlobalOutUncompOctetsV2_Type()
)
hh3cIPsecGlobalOutUncompOctetsV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPsecGlobalOutUncompOctetsV2.setStatus("current")
_Hh3cIPsecGlobalOutPktsV2_Type = Counter64
_Hh3cIPsecGlobalOutPktsV2_Object = MibScalar
hh3cIPsecGlobalOutPktsV2 = _Hh3cIPsecGlobalOutPktsV2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 6, 12),
    _Hh3cIPsecGlobalOutPktsV2_Type()
)
hh3cIPsecGlobalOutPktsV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPsecGlobalOutPktsV2.setStatus("current")
_Hh3cIPsecGlobalOutDropsV2_Type = Counter64
_Hh3cIPsecGlobalOutDropsV2_Object = MibScalar
hh3cIPsecGlobalOutDropsV2 = _Hh3cIPsecGlobalOutDropsV2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 6, 13),
    _Hh3cIPsecGlobalOutDropsV2_Type()
)
hh3cIPsecGlobalOutDropsV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPsecGlobalOutDropsV2.setStatus("current")
_Hh3cIPsecGlobalOutEncryptFailsV2_Type = Counter64
_Hh3cIPsecGlobalOutEncryptFailsV2_Object = MibScalar
hh3cIPsecGlobalOutEncryptFailsV2 = _Hh3cIPsecGlobalOutEncryptFailsV2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 6, 14),
    _Hh3cIPsecGlobalOutEncryptFailsV2_Type()
)
hh3cIPsecGlobalOutEncryptFailsV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPsecGlobalOutEncryptFailsV2.setStatus("current")
_Hh3cIPsecGlobalNoMemoryDropsV2_Type = Counter64
_Hh3cIPsecGlobalNoMemoryDropsV2_Object = MibScalar
hh3cIPsecGlobalNoMemoryDropsV2 = _Hh3cIPsecGlobalNoMemoryDropsV2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 6, 15),
    _Hh3cIPsecGlobalNoMemoryDropsV2_Type()
)
hh3cIPsecGlobalNoMemoryDropsV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPsecGlobalNoMemoryDropsV2.setStatus("current")
_Hh3cIPsecGlobalNoFindSaDropsV2_Type = Counter64
_Hh3cIPsecGlobalNoFindSaDropsV2_Object = MibScalar
hh3cIPsecGlobalNoFindSaDropsV2 = _Hh3cIPsecGlobalNoFindSaDropsV2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 6, 16),
    _Hh3cIPsecGlobalNoFindSaDropsV2_Type()
)
hh3cIPsecGlobalNoFindSaDropsV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPsecGlobalNoFindSaDropsV2.setStatus("current")
_Hh3cIPsecGlobalQueueFullDropsV2_Type = Counter64
_Hh3cIPsecGlobalQueueFullDropsV2_Object = MibScalar
hh3cIPsecGlobalQueueFullDropsV2 = _Hh3cIPsecGlobalQueueFullDropsV2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 6, 17),
    _Hh3cIPsecGlobalQueueFullDropsV2_Type()
)
hh3cIPsecGlobalQueueFullDropsV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPsecGlobalQueueFullDropsV2.setStatus("current")
_Hh3cIPsecGlobalInvalidLenDropsV2_Type = Counter64
_Hh3cIPsecGlobalInvalidLenDropsV2_Object = MibScalar
hh3cIPsecGlobalInvalidLenDropsV2 = _Hh3cIPsecGlobalInvalidLenDropsV2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 6, 18),
    _Hh3cIPsecGlobalInvalidLenDropsV2_Type()
)
hh3cIPsecGlobalInvalidLenDropsV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPsecGlobalInvalidLenDropsV2.setStatus("current")
_Hh3cIPsecGlobalTooLongDropsV2_Type = Counter64
_Hh3cIPsecGlobalTooLongDropsV2_Object = MibScalar
hh3cIPsecGlobalTooLongDropsV2 = _Hh3cIPsecGlobalTooLongDropsV2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 6, 19),
    _Hh3cIPsecGlobalTooLongDropsV2_Type()
)
hh3cIPsecGlobalTooLongDropsV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPsecGlobalTooLongDropsV2.setStatus("current")
_Hh3cIPsecGlobalInvalidSaDropsV2_Type = Counter64
_Hh3cIPsecGlobalInvalidSaDropsV2_Object = MibScalar
hh3cIPsecGlobalInvalidSaDropsV2 = _Hh3cIPsecGlobalInvalidSaDropsV2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 6, 20),
    _Hh3cIPsecGlobalInvalidSaDropsV2_Type()
)
hh3cIPsecGlobalInvalidSaDropsV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPsecGlobalInvalidSaDropsV2.setStatus("current")
_Hh3cIPsecTrapObjectV2_ObjectIdentity = ObjectIdentity
hh3cIPsecTrapObjectV2 = _Hh3cIPsecTrapObjectV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 7)
)
_Hh3cIPsecPolicyNameV2_Type = DisplayString
_Hh3cIPsecPolicyNameV2_Object = MibScalar
hh3cIPsecPolicyNameV2 = _Hh3cIPsecPolicyNameV2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 7, 1),
    _Hh3cIPsecPolicyNameV2_Type()
)
hh3cIPsecPolicyNameV2.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cIPsecPolicyNameV2.setStatus("current")
_Hh3cIPsecPolicySeqNumV2_Type = Integer32
_Hh3cIPsecPolicySeqNumV2_Object = MibScalar
hh3cIPsecPolicySeqNumV2 = _Hh3cIPsecPolicySeqNumV2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 7, 2),
    _Hh3cIPsecPolicySeqNumV2_Type()
)
hh3cIPsecPolicySeqNumV2.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cIPsecPolicySeqNumV2.setStatus("current")
_Hh3cIPsecPolicySizeV2_Type = Integer32
_Hh3cIPsecPolicySizeV2_Object = MibScalar
hh3cIPsecPolicySizeV2 = _Hh3cIPsecPolicySizeV2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 7, 3),
    _Hh3cIPsecPolicySizeV2_Type()
)
hh3cIPsecPolicySizeV2.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cIPsecPolicySizeV2.setStatus("current")
_Hh3cIPsecTrapCntlV2_ObjectIdentity = ObjectIdentity
hh3cIPsecTrapCntlV2 = _Hh3cIPsecTrapCntlV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 8)
)
_Hh3cIPsecTrapGlobalCntlV2_Type = TruthValue
_Hh3cIPsecTrapGlobalCntlV2_Object = MibScalar
hh3cIPsecTrapGlobalCntlV2 = _Hh3cIPsecTrapGlobalCntlV2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 8, 1),
    _Hh3cIPsecTrapGlobalCntlV2_Type()
)
hh3cIPsecTrapGlobalCntlV2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIPsecTrapGlobalCntlV2.setStatus("current")
_Hh3cIPsecTunnelStartTrapCntlV2_Type = TruthValue
_Hh3cIPsecTunnelStartTrapCntlV2_Object = MibScalar
hh3cIPsecTunnelStartTrapCntlV2 = _Hh3cIPsecTunnelStartTrapCntlV2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 8, 2),
    _Hh3cIPsecTunnelStartTrapCntlV2_Type()
)
hh3cIPsecTunnelStartTrapCntlV2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIPsecTunnelStartTrapCntlV2.setStatus("current")
_Hh3cIPsecTunnelStopTrapCntlV2_Type = TruthValue
_Hh3cIPsecTunnelStopTrapCntlV2_Object = MibScalar
hh3cIPsecTunnelStopTrapCntlV2 = _Hh3cIPsecTunnelStopTrapCntlV2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 8, 3),
    _Hh3cIPsecTunnelStopTrapCntlV2_Type()
)
hh3cIPsecTunnelStopTrapCntlV2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIPsecTunnelStopTrapCntlV2.setStatus("current")
_Hh3cIPsecNoSaTrapCntlV2_Type = TruthValue
_Hh3cIPsecNoSaTrapCntlV2_Object = MibScalar
hh3cIPsecNoSaTrapCntlV2 = _Hh3cIPsecNoSaTrapCntlV2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 8, 4),
    _Hh3cIPsecNoSaTrapCntlV2_Type()
)
hh3cIPsecNoSaTrapCntlV2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIPsecNoSaTrapCntlV2.setStatus("current")
_Hh3cIPsecAuthFailureTrapCntlV2_Type = TruthValue
_Hh3cIPsecAuthFailureTrapCntlV2_Object = MibScalar
hh3cIPsecAuthFailureTrapCntlV2 = _Hh3cIPsecAuthFailureTrapCntlV2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 8, 5),
    _Hh3cIPsecAuthFailureTrapCntlV2_Type()
)
hh3cIPsecAuthFailureTrapCntlV2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIPsecAuthFailureTrapCntlV2.setStatus("current")
_Hh3cIPsecEncryFailureTrapCntlV2_Type = TruthValue
_Hh3cIPsecEncryFailureTrapCntlV2_Object = MibScalar
hh3cIPsecEncryFailureTrapCntlV2 = _Hh3cIPsecEncryFailureTrapCntlV2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 8, 6),
    _Hh3cIPsecEncryFailureTrapCntlV2_Type()
)
hh3cIPsecEncryFailureTrapCntlV2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIPsecEncryFailureTrapCntlV2.setStatus("current")
_Hh3cIPsecDecryFailureTrapCntlV2_Type = TruthValue
_Hh3cIPsecDecryFailureTrapCntlV2_Object = MibScalar
hh3cIPsecDecryFailureTrapCntlV2 = _Hh3cIPsecDecryFailureTrapCntlV2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 8, 7),
    _Hh3cIPsecDecryFailureTrapCntlV2_Type()
)
hh3cIPsecDecryFailureTrapCntlV2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIPsecDecryFailureTrapCntlV2.setStatus("current")
_Hh3cIPsecInvalidSaTrapCntlV2_Type = TruthValue
_Hh3cIPsecInvalidSaTrapCntlV2_Object = MibScalar
hh3cIPsecInvalidSaTrapCntlV2 = _Hh3cIPsecInvalidSaTrapCntlV2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 8, 8),
    _Hh3cIPsecInvalidSaTrapCntlV2_Type()
)
hh3cIPsecInvalidSaTrapCntlV2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIPsecInvalidSaTrapCntlV2.setStatus("current")
_Hh3cIPsecPolicyAddTrapCntlV2_Type = TruthValue
_Hh3cIPsecPolicyAddTrapCntlV2_Object = MibScalar
hh3cIPsecPolicyAddTrapCntlV2 = _Hh3cIPsecPolicyAddTrapCntlV2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 8, 9),
    _Hh3cIPsecPolicyAddTrapCntlV2_Type()
)
hh3cIPsecPolicyAddTrapCntlV2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIPsecPolicyAddTrapCntlV2.setStatus("current")
_Hh3cIPsecPolicyDelTrapCntlV2_Type = TruthValue
_Hh3cIPsecPolicyDelTrapCntlV2_Object = MibScalar
hh3cIPsecPolicyDelTrapCntlV2 = _Hh3cIPsecPolicyDelTrapCntlV2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 8, 10),
    _Hh3cIPsecPolicyDelTrapCntlV2_Type()
)
hh3cIPsecPolicyDelTrapCntlV2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIPsecPolicyDelTrapCntlV2.setStatus("current")
_Hh3cIPsecPolicyAttachTrapCntlV2_Type = TruthValue
_Hh3cIPsecPolicyAttachTrapCntlV2_Object = MibScalar
hh3cIPsecPolicyAttachTrapCntlV2 = _Hh3cIPsecPolicyAttachTrapCntlV2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 8, 11),
    _Hh3cIPsecPolicyAttachTrapCntlV2_Type()
)
hh3cIPsecPolicyAttachTrapCntlV2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIPsecPolicyAttachTrapCntlV2.setStatus("current")
_Hh3cIPsecPolicyDetachTrapCntlV2_Type = TruthValue
_Hh3cIPsecPolicyDetachTrapCntlV2_Object = MibScalar
hh3cIPsecPolicyDetachTrapCntlV2 = _Hh3cIPsecPolicyDetachTrapCntlV2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 8, 12),
    _Hh3cIPsecPolicyDetachTrapCntlV2_Type()
)
hh3cIPsecPolicyDetachTrapCntlV2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIPsecPolicyDetachTrapCntlV2.setStatus("current")
_Hh3cIPsecTrapV2_ObjectIdentity = ObjectIdentity
hh3cIPsecTrapV2 = _Hh3cIPsecTrapV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 9)
)
_Hh3cIPsecNotificationsV2_ObjectIdentity = ObjectIdentity
hh3cIPsecNotificationsV2 = _Hh3cIPsecNotificationsV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 9, 0)
)
_Hh3cIPsecConformanceV2_ObjectIdentity = ObjectIdentity
hh3cIPsecConformanceV2 = _Hh3cIPsecConformanceV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 2)
)
_Hh3cIPsecCompliancesV2_ObjectIdentity = ObjectIdentity
hh3cIPsecCompliancesV2 = _Hh3cIPsecCompliancesV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 2, 1)
)
_Hh3cIPsecGroupsV2_ObjectIdentity = ObjectIdentity
hh3cIPsecGroupsV2 = _Hh3cIPsecGroupsV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 2, 2)
)

# Managed Objects groups

hh3cIPsecScalarObjectsGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 2, 2, 1)
)
hh3cIPsecScalarObjectsGroupV2.setObjects(
    ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecMIBVersion")
)
if mibBuilder.loadTexts:
    hh3cIPsecScalarObjectsGroupV2.setStatus("current")

hh3cIPsecTunnelTableGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 2, 2, 2)
)
hh3cIPsecTunnelTableGroupV2.setObjects(
      *(("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecTunIfIndexV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecTunIKETunnelIndexV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecTunIKETunLocalIDTypeV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecTunIKETunLocalIDVal1V2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecTunIKETunLocalIDVal2V2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecTunIKETunRemoteIDTypeV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecTunIKETunRemoteIDVal1V2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecTunIKETunRemoteIDVal2V2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecTunLocalAddrTypeV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecTunLocalAddrV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecTunRemoteAddrTypeV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecTunRemoteAddrV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecTunKeyTypeV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecTunEncapModeV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecTunInitiatorV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecTunLifeSizeV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecTunLifeTimeV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecTunRemainTimeV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecTunActiveTimeV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecTunRemainSizeV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecTunTotalRefreshesV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecTunCurrentSaInstancesV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecTunInSaEncryptAlgoV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecTunInSaAhAuthAlgoV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecTunInSaEspAuthAlgoV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecTunDiffHellmanGrpV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecTunOutSaEncryptAlgoV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecTunOutSaAhAuthAlgoV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecTunOutSaEspAuthAlgoV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecTunPolicyNameV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecTunPolicyNumV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecTunStatusV2"))
)
if mibBuilder.loadTexts:
    hh3cIPsecTunnelTableGroupV2.setStatus("current")

hh3cIPsecTunnelStatGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 2, 2, 3)
)
hh3cIPsecTunnelStatGroupV2.setObjects(
      *(("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecTunInOctetsV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecTunInDecompOctetsV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecTunInPktsV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecTunInDropPktsV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecTunInReplayDropPktsV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecTunInAuthFailsV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecTunInDecryptFailsV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecTunOutOctetsV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecTunOutUncompOctetsV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecTunOutPktsV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecTunOutDropPktsV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecTunOutEncryptFailsV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecTunNoMemoryDropPktsV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecTunQueueFullDropPktsV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecTunInvalidLenDropPktsV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecTunTooLongDropPktsV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecTunInvalidSaDropPktsV2"))
)
if mibBuilder.loadTexts:
    hh3cIPsecTunnelStatGroupV2.setStatus("current")

hh3cIPsecSaGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 2, 2, 4)
)
hh3cIPsecSaGroupV2.setObjects(
      *(("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecSaDirectionV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecSaSpiValueV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecSaSecProtocolV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecSaEncryptAlgoV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecSaAuthAlgoV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecSaStatusV2"))
)
if mibBuilder.loadTexts:
    hh3cIPsecSaGroupV2.setStatus("current")

hh3cIPsecTrafficTableGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 2, 2, 5)
)
hh3cIPsecTrafficTableGroupV2.setObjects(
      *(("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecTrafficLocalTypeV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecTrafficLocalAddr1TypeV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecTrafficLocalAddr1V2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecTrafficLocalAddr2TypeV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecTrafficLocalAddr2V2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecTrafficLocalProtocol1V2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecTrafficLocalProtocol2V2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecTrafficLocalPort1V2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecTrafficLocalPort2V2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecTrafficRemoteTypeV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecTrafficRemAddr1TypeV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecTrafficRemAddr1V2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecTrafficRemAddr2TypeV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecTrafficRemAddr2V2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecTrafficRemoPro1V2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecTrafficRemoPro2V2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecTrafficRemPort1V2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecTrafficRemPort2V2"))
)
if mibBuilder.loadTexts:
    hh3cIPsecTrafficTableGroupV2.setStatus("current")

hh3cIPsecGlobalStatsGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 2, 2, 6)
)
hh3cIPsecGlobalStatsGroupV2.setObjects(
      *(("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecGlobalActiveTunnelsV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecGlobalActiveSasV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecGlobalInOctetsV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecGlobalInDecompOctetsV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecGlobalInPktsV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecGlobalInDropsV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecGlobalInReplayDropsV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecGlobalInAuthFailsV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecGlobalInDecryptFailsV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecGlobalOutOctetsV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecGlobalOutUncompOctetsV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecGlobalOutPktsV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecGlobalOutDropsV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecGlobalOutEncryptFailsV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecGlobalNoMemoryDropsV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecGlobalNoFindSaDropsV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecGlobalQueueFullDropsV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecGlobalInvalidLenDropsV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecGlobalTooLongDropsV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecGlobalInvalidSaDropsV2"))
)
if mibBuilder.loadTexts:
    hh3cIPsecGlobalStatsGroupV2.setStatus("current")

hh3cIPsecTrapObjectGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 2, 2, 7)
)
hh3cIPsecTrapObjectGroupV2.setObjects(
      *(("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecPolicyNameV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecPolicySeqNumV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecPolicySizeV2"))
)
if mibBuilder.loadTexts:
    hh3cIPsecTrapObjectGroupV2.setStatus("current")

hh3cIPsecTrapCntlGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 2, 2, 8)
)
hh3cIPsecTrapCntlGroupV2.setObjects(
      *(("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecTrapGlobalCntlV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecTunnelStartTrapCntlV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecTunnelStopTrapCntlV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecNoSaTrapCntlV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecAuthFailureTrapCntlV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecEncryFailureTrapCntlV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecDecryFailureTrapCntlV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecInvalidSaTrapCntlV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecPolicyAddTrapCntlV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecPolicyDelTrapCntlV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecPolicyAttachTrapCntlV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecPolicyDetachTrapCntlV2"))
)
if mibBuilder.loadTexts:
    hh3cIPsecTrapCntlGroupV2.setStatus("current")


# Notification objects

hh3cIPsecTunnelStartV2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 9, 0, 1)
)
hh3cIPsecTunnelStartV2.setObjects(
      *(("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecTunIndexV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecTunLocalAddrTypeV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecTunLocalAddrV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecTunRemoteAddrTypeV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecTunRemoteAddrV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecTunLifeTimeV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecTunLifeSizeV2"))
)
if mibBuilder.loadTexts:
    hh3cIPsecTunnelStartV2.setStatus(
        "current"
    )

hh3cIPsecTunnelStopV2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 9, 0, 2)
)
hh3cIPsecTunnelStopV2.setObjects(
      *(("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecTunIndexV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecTunLocalAddrTypeV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecTunLocalAddrV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecTunRemoteAddrTypeV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecTunRemoteAddrV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecTunActiveTimeV2"))
)
if mibBuilder.loadTexts:
    hh3cIPsecTunnelStopV2.setStatus(
        "current"
    )

hh3cIPsecNoSaFailureV2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 9, 0, 3)
)
hh3cIPsecNoSaFailureV2.setObjects(
      *(("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecTunIndexV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecTunLocalAddrTypeV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecTunLocalAddrV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecTunRemoteAddrTypeV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecTunRemoteAddrV2"))
)
if mibBuilder.loadTexts:
    hh3cIPsecNoSaFailureV2.setStatus(
        "current"
    )

hh3cIPsecAuthFailFailureV2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 9, 0, 4)
)
hh3cIPsecAuthFailFailureV2.setObjects(
      *(("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecTunIndexV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecTunLocalAddrTypeV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecTunLocalAddrV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecTunRemoteAddrTypeV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecTunRemoteAddrV2"))
)
if mibBuilder.loadTexts:
    hh3cIPsecAuthFailFailureV2.setStatus(
        "current"
    )

hh3cIPsecEncryFailFailureV2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 9, 0, 5)
)
hh3cIPsecEncryFailFailureV2.setObjects(
      *(("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecTunIndexV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecTunLocalAddrTypeV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecTunLocalAddrV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecTunRemoteAddrTypeV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecTunRemoteAddrV2"))
)
if mibBuilder.loadTexts:
    hh3cIPsecEncryFailFailureV2.setStatus(
        "current"
    )

hh3cIPsecDecryFailFailureV2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 9, 0, 6)
)
hh3cIPsecDecryFailFailureV2.setObjects(
      *(("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecTunIndexV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecTunLocalAddrTypeV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecTunLocalAddrV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecTunRemoteAddrTypeV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecTunRemoteAddrV2"))
)
if mibBuilder.loadTexts:
    hh3cIPsecDecryFailFailureV2.setStatus(
        "current"
    )

hh3cIPsecInvalidSaFailureV2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 9, 0, 7)
)
hh3cIPsecInvalidSaFailureV2.setObjects(
      *(("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecTunIndexV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecSaIndexV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecTunLocalAddrTypeV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecTunLocalAddrV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecTunRemoteAddrTypeV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecTunRemoteAddrV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecSaSpiValueV2"))
)
if mibBuilder.loadTexts:
    hh3cIPsecInvalidSaFailureV2.setStatus(
        "current"
    )

hh3cIPsecPolicyAddV2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 9, 0, 8)
)
hh3cIPsecPolicyAddV2.setObjects(
      *(("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecPolicyNameV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecPolicySeqNumV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecPolicySizeV2"))
)
if mibBuilder.loadTexts:
    hh3cIPsecPolicyAddV2.setStatus(
        "current"
    )

hh3cIPsecPolicyDelV2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 9, 0, 9)
)
hh3cIPsecPolicyDelV2.setObjects(
      *(("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecPolicyNameV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecPolicySeqNumV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecPolicySizeV2"))
)
if mibBuilder.loadTexts:
    hh3cIPsecPolicyDelV2.setStatus(
        "current"
    )

hh3cIPsecPolicyAttachV2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 9, 0, 10)
)
hh3cIPsecPolicyAttachV2.setObjects(
      *(("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecPolicyNameV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecPolicySizeV2"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    hh3cIPsecPolicyAttachV2.setStatus(
        "current"
    )

hh3cIPsecPolicyDetachV2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 1, 9, 0, 11)
)
hh3cIPsecPolicyDetachV2.setObjects(
      *(("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecPolicyNameV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecPolicySizeV2"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    hh3cIPsecPolicyDetachV2.setStatus(
        "current"
    )


# Notifications groups

hh3cIPsecTrapGroupV2 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 2, 2, 9)
)
hh3cIPsecTrapGroupV2.setObjects(
      *(("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecTunnelStartV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecTunnelStopV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecNoSaFailureV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecAuthFailFailureV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecEncryFailFailureV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecDecryFailFailureV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecInvalidSaFailureV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecPolicyAddV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecPolicyDelV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecPolicyAttachV2"),
        ("HH3C-IPSEC-MONITOR-V2-MIB", "hh3cIPsecPolicyDetachV2"))
)
if mibBuilder.loadTexts:
    hh3cIPsecTrapGroupV2.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hh3cIPsecComplianceV2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cIPsecComplianceV2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-IPSEC-MONITOR-V2-MIB",
    **{"Hh3cIPsecDiffHellmanGrpV2": Hh3cIPsecDiffHellmanGrpV2,
       "Hh3cIPsecEncapModeV2": Hh3cIPsecEncapModeV2,
       "Hh3cIPsecEncryptAlgoV2": Hh3cIPsecEncryptAlgoV2,
       "Hh3cIPsecAuthAlgoV2": Hh3cIPsecAuthAlgoV2,
       "Hh3cIPsecSaProtocolV2": Hh3cIPsecSaProtocolV2,
       "Hh3cIPsecIDTypeV2": Hh3cIPsecIDTypeV2,
       "Hh3cIPsecTrafficTypeV2": Hh3cIPsecTrafficTypeV2,
       "Hh3cIPsecNegoTypeV2": Hh3cIPsecNegoTypeV2,
       "Hh3cIPsecTunnelStateV2": Hh3cIPsecTunnelStateV2,
       "hh3cIPsecMonitorV2": hh3cIPsecMonitorV2,
       "hh3cIPsecObjectsV2": hh3cIPsecObjectsV2,
       "hh3cIPsecScalarObjectsV2": hh3cIPsecScalarObjectsV2,
       "hh3cIPsecMIBVersion": hh3cIPsecMIBVersion,
       "hh3cIPsecTunnelV2Table": hh3cIPsecTunnelV2Table,
       "hh3cIPsecTunnelV2Entry": hh3cIPsecTunnelV2Entry,
       "hh3cIPsecTunIndexV2": hh3cIPsecTunIndexV2,
       "hh3cIPsecTunIfIndexV2": hh3cIPsecTunIfIndexV2,
       "hh3cIPsecTunIKETunnelIndexV2": hh3cIPsecTunIKETunnelIndexV2,
       "hh3cIPsecTunIKETunLocalIDTypeV2": hh3cIPsecTunIKETunLocalIDTypeV2,
       "hh3cIPsecTunIKETunLocalIDVal1V2": hh3cIPsecTunIKETunLocalIDVal1V2,
       "hh3cIPsecTunIKETunLocalIDVal2V2": hh3cIPsecTunIKETunLocalIDVal2V2,
       "hh3cIPsecTunIKETunRemoteIDTypeV2": hh3cIPsecTunIKETunRemoteIDTypeV2,
       "hh3cIPsecTunIKETunRemoteIDVal1V2": hh3cIPsecTunIKETunRemoteIDVal1V2,
       "hh3cIPsecTunIKETunRemoteIDVal2V2": hh3cIPsecTunIKETunRemoteIDVal2V2,
       "hh3cIPsecTunLocalAddrTypeV2": hh3cIPsecTunLocalAddrTypeV2,
       "hh3cIPsecTunLocalAddrV2": hh3cIPsecTunLocalAddrV2,
       "hh3cIPsecTunRemoteAddrTypeV2": hh3cIPsecTunRemoteAddrTypeV2,
       "hh3cIPsecTunRemoteAddrV2": hh3cIPsecTunRemoteAddrV2,
       "hh3cIPsecTunKeyTypeV2": hh3cIPsecTunKeyTypeV2,
       "hh3cIPsecTunEncapModeV2": hh3cIPsecTunEncapModeV2,
       "hh3cIPsecTunInitiatorV2": hh3cIPsecTunInitiatorV2,
       "hh3cIPsecTunLifeSizeV2": hh3cIPsecTunLifeSizeV2,
       "hh3cIPsecTunLifeTimeV2": hh3cIPsecTunLifeTimeV2,
       "hh3cIPsecTunRemainTimeV2": hh3cIPsecTunRemainTimeV2,
       "hh3cIPsecTunActiveTimeV2": hh3cIPsecTunActiveTimeV2,
       "hh3cIPsecTunRemainSizeV2": hh3cIPsecTunRemainSizeV2,
       "hh3cIPsecTunTotalRefreshesV2": hh3cIPsecTunTotalRefreshesV2,
       "hh3cIPsecTunCurrentSaInstancesV2": hh3cIPsecTunCurrentSaInstancesV2,
       "hh3cIPsecTunInSaEncryptAlgoV2": hh3cIPsecTunInSaEncryptAlgoV2,
       "hh3cIPsecTunInSaAhAuthAlgoV2": hh3cIPsecTunInSaAhAuthAlgoV2,
       "hh3cIPsecTunInSaEspAuthAlgoV2": hh3cIPsecTunInSaEspAuthAlgoV2,
       "hh3cIPsecTunDiffHellmanGrpV2": hh3cIPsecTunDiffHellmanGrpV2,
       "hh3cIPsecTunOutSaEncryptAlgoV2": hh3cIPsecTunOutSaEncryptAlgoV2,
       "hh3cIPsecTunOutSaAhAuthAlgoV2": hh3cIPsecTunOutSaAhAuthAlgoV2,
       "hh3cIPsecTunOutSaEspAuthAlgoV2": hh3cIPsecTunOutSaEspAuthAlgoV2,
       "hh3cIPsecTunPolicyNameV2": hh3cIPsecTunPolicyNameV2,
       "hh3cIPsecTunPolicyNumV2": hh3cIPsecTunPolicyNumV2,
       "hh3cIPsecTunStatusV2": hh3cIPsecTunStatusV2,
       "hh3cIPsecTunnelStatV2Table": hh3cIPsecTunnelStatV2Table,
       "hh3cIPsecTunnelStatV2Entry": hh3cIPsecTunnelStatV2Entry,
       "hh3cIPsecTunInOctetsV2": hh3cIPsecTunInOctetsV2,
       "hh3cIPsecTunInDecompOctetsV2": hh3cIPsecTunInDecompOctetsV2,
       "hh3cIPsecTunInPktsV2": hh3cIPsecTunInPktsV2,
       "hh3cIPsecTunInDropPktsV2": hh3cIPsecTunInDropPktsV2,
       "hh3cIPsecTunInReplayDropPktsV2": hh3cIPsecTunInReplayDropPktsV2,
       "hh3cIPsecTunInAuthFailsV2": hh3cIPsecTunInAuthFailsV2,
       "hh3cIPsecTunInDecryptFailsV2": hh3cIPsecTunInDecryptFailsV2,
       "hh3cIPsecTunOutOctetsV2": hh3cIPsecTunOutOctetsV2,
       "hh3cIPsecTunOutUncompOctetsV2": hh3cIPsecTunOutUncompOctetsV2,
       "hh3cIPsecTunOutPktsV2": hh3cIPsecTunOutPktsV2,
       "hh3cIPsecTunOutDropPktsV2": hh3cIPsecTunOutDropPktsV2,
       "hh3cIPsecTunOutEncryptFailsV2": hh3cIPsecTunOutEncryptFailsV2,
       "hh3cIPsecTunNoMemoryDropPktsV2": hh3cIPsecTunNoMemoryDropPktsV2,
       "hh3cIPsecTunQueueFullDropPktsV2": hh3cIPsecTunQueueFullDropPktsV2,
       "hh3cIPsecTunInvalidLenDropPktsV2": hh3cIPsecTunInvalidLenDropPktsV2,
       "hh3cIPsecTunTooLongDropPktsV2": hh3cIPsecTunTooLongDropPktsV2,
       "hh3cIPsecTunInvalidSaDropPktsV2": hh3cIPsecTunInvalidSaDropPktsV2,
       "hh3cIPsecSaV2Table": hh3cIPsecSaV2Table,
       "hh3cIPsecSaV2Entry": hh3cIPsecSaV2Entry,
       "hh3cIPsecSaIndexV2": hh3cIPsecSaIndexV2,
       "hh3cIPsecSaDirectionV2": hh3cIPsecSaDirectionV2,
       "hh3cIPsecSaSpiValueV2": hh3cIPsecSaSpiValueV2,
       "hh3cIPsecSaSecProtocolV2": hh3cIPsecSaSecProtocolV2,
       "hh3cIPsecSaEncryptAlgoV2": hh3cIPsecSaEncryptAlgoV2,
       "hh3cIPsecSaAuthAlgoV2": hh3cIPsecSaAuthAlgoV2,
       "hh3cIPsecSaStatusV2": hh3cIPsecSaStatusV2,
       "hh3cIPsecTrafficV2Table": hh3cIPsecTrafficV2Table,
       "hh3cIPsecTrafficV2Entry": hh3cIPsecTrafficV2Entry,
       "hh3cIPsecTrafficLocalTypeV2": hh3cIPsecTrafficLocalTypeV2,
       "hh3cIPsecTrafficLocalAddr1TypeV2": hh3cIPsecTrafficLocalAddr1TypeV2,
       "hh3cIPsecTrafficLocalAddr1V2": hh3cIPsecTrafficLocalAddr1V2,
       "hh3cIPsecTrafficLocalAddr2TypeV2": hh3cIPsecTrafficLocalAddr2TypeV2,
       "hh3cIPsecTrafficLocalAddr2V2": hh3cIPsecTrafficLocalAddr2V2,
       "hh3cIPsecTrafficLocalProtocol1V2": hh3cIPsecTrafficLocalProtocol1V2,
       "hh3cIPsecTrafficLocalProtocol2V2": hh3cIPsecTrafficLocalProtocol2V2,
       "hh3cIPsecTrafficLocalPort1V2": hh3cIPsecTrafficLocalPort1V2,
       "hh3cIPsecTrafficLocalPort2V2": hh3cIPsecTrafficLocalPort2V2,
       "hh3cIPsecTrafficRemoteTypeV2": hh3cIPsecTrafficRemoteTypeV2,
       "hh3cIPsecTrafficRemAddr1TypeV2": hh3cIPsecTrafficRemAddr1TypeV2,
       "hh3cIPsecTrafficRemAddr1V2": hh3cIPsecTrafficRemAddr1V2,
       "hh3cIPsecTrafficRemAddr2TypeV2": hh3cIPsecTrafficRemAddr2TypeV2,
       "hh3cIPsecTrafficRemAddr2V2": hh3cIPsecTrafficRemAddr2V2,
       "hh3cIPsecTrafficRemoPro1V2": hh3cIPsecTrafficRemoPro1V2,
       "hh3cIPsecTrafficRemoPro2V2": hh3cIPsecTrafficRemoPro2V2,
       "hh3cIPsecTrafficRemPort1V2": hh3cIPsecTrafficRemPort1V2,
       "hh3cIPsecTrafficRemPort2V2": hh3cIPsecTrafficRemPort2V2,
       "hh3cIPsecGlobalStatsV2": hh3cIPsecGlobalStatsV2,
       "hh3cIPsecGlobalActiveTunnelsV2": hh3cIPsecGlobalActiveTunnelsV2,
       "hh3cIPsecGlobalActiveSasV2": hh3cIPsecGlobalActiveSasV2,
       "hh3cIPsecGlobalInOctetsV2": hh3cIPsecGlobalInOctetsV2,
       "hh3cIPsecGlobalInDecompOctetsV2": hh3cIPsecGlobalInDecompOctetsV2,
       "hh3cIPsecGlobalInPktsV2": hh3cIPsecGlobalInPktsV2,
       "hh3cIPsecGlobalInDropsV2": hh3cIPsecGlobalInDropsV2,
       "hh3cIPsecGlobalInReplayDropsV2": hh3cIPsecGlobalInReplayDropsV2,
       "hh3cIPsecGlobalInAuthFailsV2": hh3cIPsecGlobalInAuthFailsV2,
       "hh3cIPsecGlobalInDecryptFailsV2": hh3cIPsecGlobalInDecryptFailsV2,
       "hh3cIPsecGlobalOutOctetsV2": hh3cIPsecGlobalOutOctetsV2,
       "hh3cIPsecGlobalOutUncompOctetsV2": hh3cIPsecGlobalOutUncompOctetsV2,
       "hh3cIPsecGlobalOutPktsV2": hh3cIPsecGlobalOutPktsV2,
       "hh3cIPsecGlobalOutDropsV2": hh3cIPsecGlobalOutDropsV2,
       "hh3cIPsecGlobalOutEncryptFailsV2": hh3cIPsecGlobalOutEncryptFailsV2,
       "hh3cIPsecGlobalNoMemoryDropsV2": hh3cIPsecGlobalNoMemoryDropsV2,
       "hh3cIPsecGlobalNoFindSaDropsV2": hh3cIPsecGlobalNoFindSaDropsV2,
       "hh3cIPsecGlobalQueueFullDropsV2": hh3cIPsecGlobalQueueFullDropsV2,
       "hh3cIPsecGlobalInvalidLenDropsV2": hh3cIPsecGlobalInvalidLenDropsV2,
       "hh3cIPsecGlobalTooLongDropsV2": hh3cIPsecGlobalTooLongDropsV2,
       "hh3cIPsecGlobalInvalidSaDropsV2": hh3cIPsecGlobalInvalidSaDropsV2,
       "hh3cIPsecTrapObjectV2": hh3cIPsecTrapObjectV2,
       "hh3cIPsecPolicyNameV2": hh3cIPsecPolicyNameV2,
       "hh3cIPsecPolicySeqNumV2": hh3cIPsecPolicySeqNumV2,
       "hh3cIPsecPolicySizeV2": hh3cIPsecPolicySizeV2,
       "hh3cIPsecTrapCntlV2": hh3cIPsecTrapCntlV2,
       "hh3cIPsecTrapGlobalCntlV2": hh3cIPsecTrapGlobalCntlV2,
       "hh3cIPsecTunnelStartTrapCntlV2": hh3cIPsecTunnelStartTrapCntlV2,
       "hh3cIPsecTunnelStopTrapCntlV2": hh3cIPsecTunnelStopTrapCntlV2,
       "hh3cIPsecNoSaTrapCntlV2": hh3cIPsecNoSaTrapCntlV2,
       "hh3cIPsecAuthFailureTrapCntlV2": hh3cIPsecAuthFailureTrapCntlV2,
       "hh3cIPsecEncryFailureTrapCntlV2": hh3cIPsecEncryFailureTrapCntlV2,
       "hh3cIPsecDecryFailureTrapCntlV2": hh3cIPsecDecryFailureTrapCntlV2,
       "hh3cIPsecInvalidSaTrapCntlV2": hh3cIPsecInvalidSaTrapCntlV2,
       "hh3cIPsecPolicyAddTrapCntlV2": hh3cIPsecPolicyAddTrapCntlV2,
       "hh3cIPsecPolicyDelTrapCntlV2": hh3cIPsecPolicyDelTrapCntlV2,
       "hh3cIPsecPolicyAttachTrapCntlV2": hh3cIPsecPolicyAttachTrapCntlV2,
       "hh3cIPsecPolicyDetachTrapCntlV2": hh3cIPsecPolicyDetachTrapCntlV2,
       "hh3cIPsecTrapV2": hh3cIPsecTrapV2,
       "hh3cIPsecNotificationsV2": hh3cIPsecNotificationsV2,
       "hh3cIPsecTunnelStartV2": hh3cIPsecTunnelStartV2,
       "hh3cIPsecTunnelStopV2": hh3cIPsecTunnelStopV2,
       "hh3cIPsecNoSaFailureV2": hh3cIPsecNoSaFailureV2,
       "hh3cIPsecAuthFailFailureV2": hh3cIPsecAuthFailFailureV2,
       "hh3cIPsecEncryFailFailureV2": hh3cIPsecEncryFailFailureV2,
       "hh3cIPsecDecryFailFailureV2": hh3cIPsecDecryFailFailureV2,
       "hh3cIPsecInvalidSaFailureV2": hh3cIPsecInvalidSaFailureV2,
       "hh3cIPsecPolicyAddV2": hh3cIPsecPolicyAddV2,
       "hh3cIPsecPolicyDelV2": hh3cIPsecPolicyDelV2,
       "hh3cIPsecPolicyAttachV2": hh3cIPsecPolicyAttachV2,
       "hh3cIPsecPolicyDetachV2": hh3cIPsecPolicyDetachV2,
       "hh3cIPsecConformanceV2": hh3cIPsecConformanceV2,
       "hh3cIPsecCompliancesV2": hh3cIPsecCompliancesV2,
       "hh3cIPsecComplianceV2": hh3cIPsecComplianceV2,
       "hh3cIPsecGroupsV2": hh3cIPsecGroupsV2,
       "hh3cIPsecScalarObjectsGroupV2": hh3cIPsecScalarObjectsGroupV2,
       "hh3cIPsecTunnelTableGroupV2": hh3cIPsecTunnelTableGroupV2,
       "hh3cIPsecTunnelStatGroupV2": hh3cIPsecTunnelStatGroupV2,
       "hh3cIPsecSaGroupV2": hh3cIPsecSaGroupV2,
       "hh3cIPsecTrafficTableGroupV2": hh3cIPsecTrafficTableGroupV2,
       "hh3cIPsecGlobalStatsGroupV2": hh3cIPsecGlobalStatsGroupV2,
       "hh3cIPsecTrapObjectGroupV2": hh3cIPsecTrapObjectGroupV2,
       "hh3cIPsecTrapCntlGroupV2": hh3cIPsecTrapCntlGroupV2,
       "hh3cIPsecTrapGroupV2": hh3cIPsecTrapGroupV2}
)
