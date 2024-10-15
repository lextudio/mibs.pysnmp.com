# SNMP MIB module (HPN-ICF-IPSEC-MONITOR-V2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-IPSEC-MONITOR-V2-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:00:39 2024
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

(hpnicfCommon,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfCommon")

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

hpnicfIPsecMonitorV2 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126)
)
hpnicfIPsecMonitorV2.setRevisions(
        ("2012-06-27 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class HpnicfIPsecDiffHellmanGrpV2(Integer32, TextualConvention):
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



class HpnicfIPsecEncapModeV2(Integer32, TextualConvention):
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



class HpnicfIPsecEncryptAlgoV2(Integer32, TextualConvention):
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



class HpnicfIPsecAuthAlgoV2(Integer32, TextualConvention):
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



class HpnicfIPsecSaProtocolV2(Integer32, TextualConvention):
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



class HpnicfIPsecIDTypeV2(Integer32, TextualConvention):
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



class HpnicfIPsecTrafficTypeV2(Integer32, TextualConvention):
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



class HpnicfIPsecNegoTypeV2(Integer32, TextualConvention):
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



class HpnicfIPsecTunnelStateV2(Integer32, TextualConvention):
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

_HpnicfIPsecObjectsV2_ObjectIdentity = ObjectIdentity
hpnicfIPsecObjectsV2 = _HpnicfIPsecObjectsV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1)
)
_HpnicfIPsecScalarObjectsV2_ObjectIdentity = ObjectIdentity
hpnicfIPsecScalarObjectsV2 = _HpnicfIPsecScalarObjectsV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 1)
)
_HpnicfIPsecMIBVersion_Type = DisplayString
_HpnicfIPsecMIBVersion_Object = MibScalar
hpnicfIPsecMIBVersion = _HpnicfIPsecMIBVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 1, 1),
    _HpnicfIPsecMIBVersion_Type()
)
hpnicfIPsecMIBVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPsecMIBVersion.setStatus("current")
_HpnicfIPsecTunnelV2Table_Object = MibTable
hpnicfIPsecTunnelV2Table = _HpnicfIPsecTunnelV2Table_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 2)
)
if mibBuilder.loadTexts:
    hpnicfIPsecTunnelV2Table.setStatus("current")
_HpnicfIPsecTunnelV2Entry_Object = MibTableRow
hpnicfIPsecTunnelV2Entry = _HpnicfIPsecTunnelV2Entry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 2, 1)
)
hpnicfIPsecTunnelV2Entry.setIndexNames(
    (0, "HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecTunIndexV2"),
)
if mibBuilder.loadTexts:
    hpnicfIPsecTunnelV2Entry.setStatus("current")


class _HpnicfIPsecTunIndexV2_Type(Integer32):
    """Custom type hpnicfIPsecTunIndexV2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpnicfIPsecTunIndexV2_Type.__name__ = "Integer32"
_HpnicfIPsecTunIndexV2_Object = MibTableColumn
hpnicfIPsecTunIndexV2 = _HpnicfIPsecTunIndexV2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 2, 1, 1),
    _HpnicfIPsecTunIndexV2_Type()
)
hpnicfIPsecTunIndexV2.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfIPsecTunIndexV2.setStatus("current")
_HpnicfIPsecTunIfIndexV2_Type = InterfaceIndex
_HpnicfIPsecTunIfIndexV2_Object = MibTableColumn
hpnicfIPsecTunIfIndexV2 = _HpnicfIPsecTunIfIndexV2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 2, 1, 2),
    _HpnicfIPsecTunIfIndexV2_Type()
)
hpnicfIPsecTunIfIndexV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPsecTunIfIndexV2.setStatus("current")


class _HpnicfIPsecTunIKETunnelIndexV2_Type(Integer32):
    """Custom type hpnicfIPsecTunIKETunnelIndexV2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpnicfIPsecTunIKETunnelIndexV2_Type.__name__ = "Integer32"
_HpnicfIPsecTunIKETunnelIndexV2_Object = MibTableColumn
hpnicfIPsecTunIKETunnelIndexV2 = _HpnicfIPsecTunIKETunnelIndexV2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 2, 1, 3),
    _HpnicfIPsecTunIKETunnelIndexV2_Type()
)
hpnicfIPsecTunIKETunnelIndexV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPsecTunIKETunnelIndexV2.setStatus("current")
_HpnicfIPsecTunIKETunLocalIDTypeV2_Type = HpnicfIPsecIDTypeV2
_HpnicfIPsecTunIKETunLocalIDTypeV2_Object = MibTableColumn
hpnicfIPsecTunIKETunLocalIDTypeV2 = _HpnicfIPsecTunIKETunLocalIDTypeV2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 2, 1, 4),
    _HpnicfIPsecTunIKETunLocalIDTypeV2_Type()
)
hpnicfIPsecTunIKETunLocalIDTypeV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPsecTunIKETunLocalIDTypeV2.setStatus("current")
_HpnicfIPsecTunIKETunLocalIDVal1V2_Type = DisplayString
_HpnicfIPsecTunIKETunLocalIDVal1V2_Object = MibTableColumn
hpnicfIPsecTunIKETunLocalIDVal1V2 = _HpnicfIPsecTunIKETunLocalIDVal1V2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 2, 1, 5),
    _HpnicfIPsecTunIKETunLocalIDVal1V2_Type()
)
hpnicfIPsecTunIKETunLocalIDVal1V2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPsecTunIKETunLocalIDVal1V2.setStatus("current")
_HpnicfIPsecTunIKETunLocalIDVal2V2_Type = DisplayString
_HpnicfIPsecTunIKETunLocalIDVal2V2_Object = MibTableColumn
hpnicfIPsecTunIKETunLocalIDVal2V2 = _HpnicfIPsecTunIKETunLocalIDVal2V2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 2, 1, 6),
    _HpnicfIPsecTunIKETunLocalIDVal2V2_Type()
)
hpnicfIPsecTunIKETunLocalIDVal2V2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPsecTunIKETunLocalIDVal2V2.setStatus("current")
_HpnicfIPsecTunIKETunRemoteIDTypeV2_Type = HpnicfIPsecIDTypeV2
_HpnicfIPsecTunIKETunRemoteIDTypeV2_Object = MibTableColumn
hpnicfIPsecTunIKETunRemoteIDTypeV2 = _HpnicfIPsecTunIKETunRemoteIDTypeV2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 2, 1, 7),
    _HpnicfIPsecTunIKETunRemoteIDTypeV2_Type()
)
hpnicfIPsecTunIKETunRemoteIDTypeV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPsecTunIKETunRemoteIDTypeV2.setStatus("current")
_HpnicfIPsecTunIKETunRemoteIDVal1V2_Type = DisplayString
_HpnicfIPsecTunIKETunRemoteIDVal1V2_Object = MibTableColumn
hpnicfIPsecTunIKETunRemoteIDVal1V2 = _HpnicfIPsecTunIKETunRemoteIDVal1V2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 2, 1, 8),
    _HpnicfIPsecTunIKETunRemoteIDVal1V2_Type()
)
hpnicfIPsecTunIKETunRemoteIDVal1V2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPsecTunIKETunRemoteIDVal1V2.setStatus("current")
_HpnicfIPsecTunIKETunRemoteIDVal2V2_Type = DisplayString
_HpnicfIPsecTunIKETunRemoteIDVal2V2_Object = MibTableColumn
hpnicfIPsecTunIKETunRemoteIDVal2V2 = _HpnicfIPsecTunIKETunRemoteIDVal2V2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 2, 1, 9),
    _HpnicfIPsecTunIKETunRemoteIDVal2V2_Type()
)
hpnicfIPsecTunIKETunRemoteIDVal2V2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPsecTunIKETunRemoteIDVal2V2.setStatus("current")
_HpnicfIPsecTunLocalAddrTypeV2_Type = InetAddressType
_HpnicfIPsecTunLocalAddrTypeV2_Object = MibTableColumn
hpnicfIPsecTunLocalAddrTypeV2 = _HpnicfIPsecTunLocalAddrTypeV2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 2, 1, 10),
    _HpnicfIPsecTunLocalAddrTypeV2_Type()
)
hpnicfIPsecTunLocalAddrTypeV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPsecTunLocalAddrTypeV2.setStatus("current")
_HpnicfIPsecTunLocalAddrV2_Type = InetAddress
_HpnicfIPsecTunLocalAddrV2_Object = MibTableColumn
hpnicfIPsecTunLocalAddrV2 = _HpnicfIPsecTunLocalAddrV2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 2, 1, 11),
    _HpnicfIPsecTunLocalAddrV2_Type()
)
hpnicfIPsecTunLocalAddrV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPsecTunLocalAddrV2.setStatus("current")
_HpnicfIPsecTunRemoteAddrTypeV2_Type = InetAddressType
_HpnicfIPsecTunRemoteAddrTypeV2_Object = MibTableColumn
hpnicfIPsecTunRemoteAddrTypeV2 = _HpnicfIPsecTunRemoteAddrTypeV2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 2, 1, 12),
    _HpnicfIPsecTunRemoteAddrTypeV2_Type()
)
hpnicfIPsecTunRemoteAddrTypeV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPsecTunRemoteAddrTypeV2.setStatus("current")
_HpnicfIPsecTunRemoteAddrV2_Type = InetAddress
_HpnicfIPsecTunRemoteAddrV2_Object = MibTableColumn
hpnicfIPsecTunRemoteAddrV2 = _HpnicfIPsecTunRemoteAddrV2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 2, 1, 13),
    _HpnicfIPsecTunRemoteAddrV2_Type()
)
hpnicfIPsecTunRemoteAddrV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPsecTunRemoteAddrV2.setStatus("current")
_HpnicfIPsecTunKeyTypeV2_Type = HpnicfIPsecNegoTypeV2
_HpnicfIPsecTunKeyTypeV2_Object = MibTableColumn
hpnicfIPsecTunKeyTypeV2 = _HpnicfIPsecTunKeyTypeV2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 2, 1, 14),
    _HpnicfIPsecTunKeyTypeV2_Type()
)
hpnicfIPsecTunKeyTypeV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPsecTunKeyTypeV2.setStatus("current")
_HpnicfIPsecTunEncapModeV2_Type = HpnicfIPsecEncapModeV2
_HpnicfIPsecTunEncapModeV2_Object = MibTableColumn
hpnicfIPsecTunEncapModeV2 = _HpnicfIPsecTunEncapModeV2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 2, 1, 15),
    _HpnicfIPsecTunEncapModeV2_Type()
)
hpnicfIPsecTunEncapModeV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPsecTunEncapModeV2.setStatus("current")


class _HpnicfIPsecTunInitiatorV2_Type(Integer32):
    """Custom type hpnicfIPsecTunInitiatorV2 based on Integer32"""
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


_HpnicfIPsecTunInitiatorV2_Type.__name__ = "Integer32"
_HpnicfIPsecTunInitiatorV2_Object = MibTableColumn
hpnicfIPsecTunInitiatorV2 = _HpnicfIPsecTunInitiatorV2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 2, 1, 16),
    _HpnicfIPsecTunInitiatorV2_Type()
)
hpnicfIPsecTunInitiatorV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPsecTunInitiatorV2.setStatus("current")
_HpnicfIPsecTunLifeSizeV2_Type = Gauge32
_HpnicfIPsecTunLifeSizeV2_Object = MibTableColumn
hpnicfIPsecTunLifeSizeV2 = _HpnicfIPsecTunLifeSizeV2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 2, 1, 17),
    _HpnicfIPsecTunLifeSizeV2_Type()
)
hpnicfIPsecTunLifeSizeV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPsecTunLifeSizeV2.setStatus("current")


class _HpnicfIPsecTunLifeTimeV2_Type(Integer32):
    """Custom type hpnicfIPsecTunLifeTimeV2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpnicfIPsecTunLifeTimeV2_Type.__name__ = "Integer32"
_HpnicfIPsecTunLifeTimeV2_Object = MibTableColumn
hpnicfIPsecTunLifeTimeV2 = _HpnicfIPsecTunLifeTimeV2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 2, 1, 18),
    _HpnicfIPsecTunLifeTimeV2_Type()
)
hpnicfIPsecTunLifeTimeV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPsecTunLifeTimeV2.setStatus("current")


class _HpnicfIPsecTunRemainTimeV2_Type(Integer32):
    """Custom type hpnicfIPsecTunRemainTimeV2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HpnicfIPsecTunRemainTimeV2_Type.__name__ = "Integer32"
_HpnicfIPsecTunRemainTimeV2_Object = MibTableColumn
hpnicfIPsecTunRemainTimeV2 = _HpnicfIPsecTunRemainTimeV2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 2, 1, 19),
    _HpnicfIPsecTunRemainTimeV2_Type()
)
hpnicfIPsecTunRemainTimeV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPsecTunRemainTimeV2.setStatus("current")


class _HpnicfIPsecTunActiveTimeV2_Type(Integer32):
    """Custom type hpnicfIPsecTunActiveTimeV2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HpnicfIPsecTunActiveTimeV2_Type.__name__ = "Integer32"
_HpnicfIPsecTunActiveTimeV2_Object = MibTableColumn
hpnicfIPsecTunActiveTimeV2 = _HpnicfIPsecTunActiveTimeV2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 2, 1, 20),
    _HpnicfIPsecTunActiveTimeV2_Type()
)
hpnicfIPsecTunActiveTimeV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPsecTunActiveTimeV2.setStatus("current")
_HpnicfIPsecTunRemainSizeV2_Type = Gauge32
_HpnicfIPsecTunRemainSizeV2_Object = MibTableColumn
hpnicfIPsecTunRemainSizeV2 = _HpnicfIPsecTunRemainSizeV2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 2, 1, 21),
    _HpnicfIPsecTunRemainSizeV2_Type()
)
hpnicfIPsecTunRemainSizeV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPsecTunRemainSizeV2.setStatus("current")
_HpnicfIPsecTunTotalRefreshesV2_Type = Counter32
_HpnicfIPsecTunTotalRefreshesV2_Object = MibTableColumn
hpnicfIPsecTunTotalRefreshesV2 = _HpnicfIPsecTunTotalRefreshesV2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 2, 1, 22),
    _HpnicfIPsecTunTotalRefreshesV2_Type()
)
hpnicfIPsecTunTotalRefreshesV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPsecTunTotalRefreshesV2.setStatus("current")
_HpnicfIPsecTunCurrentSaInstancesV2_Type = Gauge32
_HpnicfIPsecTunCurrentSaInstancesV2_Object = MibTableColumn
hpnicfIPsecTunCurrentSaInstancesV2 = _HpnicfIPsecTunCurrentSaInstancesV2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 2, 1, 23),
    _HpnicfIPsecTunCurrentSaInstancesV2_Type()
)
hpnicfIPsecTunCurrentSaInstancesV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPsecTunCurrentSaInstancesV2.setStatus("current")
_HpnicfIPsecTunInSaEncryptAlgoV2_Type = HpnicfIPsecEncryptAlgoV2
_HpnicfIPsecTunInSaEncryptAlgoV2_Object = MibTableColumn
hpnicfIPsecTunInSaEncryptAlgoV2 = _HpnicfIPsecTunInSaEncryptAlgoV2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 2, 1, 24),
    _HpnicfIPsecTunInSaEncryptAlgoV2_Type()
)
hpnicfIPsecTunInSaEncryptAlgoV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPsecTunInSaEncryptAlgoV2.setStatus("current")
_HpnicfIPsecTunInSaAhAuthAlgoV2_Type = HpnicfIPsecAuthAlgoV2
_HpnicfIPsecTunInSaAhAuthAlgoV2_Object = MibTableColumn
hpnicfIPsecTunInSaAhAuthAlgoV2 = _HpnicfIPsecTunInSaAhAuthAlgoV2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 2, 1, 25),
    _HpnicfIPsecTunInSaAhAuthAlgoV2_Type()
)
hpnicfIPsecTunInSaAhAuthAlgoV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPsecTunInSaAhAuthAlgoV2.setStatus("current")
_HpnicfIPsecTunInSaEspAuthAlgoV2_Type = HpnicfIPsecAuthAlgoV2
_HpnicfIPsecTunInSaEspAuthAlgoV2_Object = MibTableColumn
hpnicfIPsecTunInSaEspAuthAlgoV2 = _HpnicfIPsecTunInSaEspAuthAlgoV2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 2, 1, 26),
    _HpnicfIPsecTunInSaEspAuthAlgoV2_Type()
)
hpnicfIPsecTunInSaEspAuthAlgoV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPsecTunInSaEspAuthAlgoV2.setStatus("current")
_HpnicfIPsecTunDiffHellmanGrpV2_Type = HpnicfIPsecDiffHellmanGrpV2
_HpnicfIPsecTunDiffHellmanGrpV2_Object = MibTableColumn
hpnicfIPsecTunDiffHellmanGrpV2 = _HpnicfIPsecTunDiffHellmanGrpV2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 2, 1, 27),
    _HpnicfIPsecTunDiffHellmanGrpV2_Type()
)
hpnicfIPsecTunDiffHellmanGrpV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPsecTunDiffHellmanGrpV2.setStatus("current")
_HpnicfIPsecTunOutSaEncryptAlgoV2_Type = HpnicfIPsecEncryptAlgoV2
_HpnicfIPsecTunOutSaEncryptAlgoV2_Object = MibTableColumn
hpnicfIPsecTunOutSaEncryptAlgoV2 = _HpnicfIPsecTunOutSaEncryptAlgoV2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 2, 1, 28),
    _HpnicfIPsecTunOutSaEncryptAlgoV2_Type()
)
hpnicfIPsecTunOutSaEncryptAlgoV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPsecTunOutSaEncryptAlgoV2.setStatus("current")
_HpnicfIPsecTunOutSaAhAuthAlgoV2_Type = HpnicfIPsecAuthAlgoV2
_HpnicfIPsecTunOutSaAhAuthAlgoV2_Object = MibTableColumn
hpnicfIPsecTunOutSaAhAuthAlgoV2 = _HpnicfIPsecTunOutSaAhAuthAlgoV2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 2, 1, 29),
    _HpnicfIPsecTunOutSaAhAuthAlgoV2_Type()
)
hpnicfIPsecTunOutSaAhAuthAlgoV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPsecTunOutSaAhAuthAlgoV2.setStatus("current")
_HpnicfIPsecTunOutSaEspAuthAlgoV2_Type = HpnicfIPsecAuthAlgoV2
_HpnicfIPsecTunOutSaEspAuthAlgoV2_Object = MibTableColumn
hpnicfIPsecTunOutSaEspAuthAlgoV2 = _HpnicfIPsecTunOutSaEspAuthAlgoV2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 2, 1, 30),
    _HpnicfIPsecTunOutSaEspAuthAlgoV2_Type()
)
hpnicfIPsecTunOutSaEspAuthAlgoV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPsecTunOutSaEspAuthAlgoV2.setStatus("current")
_HpnicfIPsecTunPolicyNameV2_Type = DisplayString
_HpnicfIPsecTunPolicyNameV2_Object = MibTableColumn
hpnicfIPsecTunPolicyNameV2 = _HpnicfIPsecTunPolicyNameV2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 2, 1, 31),
    _HpnicfIPsecTunPolicyNameV2_Type()
)
hpnicfIPsecTunPolicyNameV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPsecTunPolicyNameV2.setStatus("current")


class _HpnicfIPsecTunPolicyNumV2_Type(Integer32):
    """Custom type hpnicfIPsecTunPolicyNumV2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpnicfIPsecTunPolicyNumV2_Type.__name__ = "Integer32"
_HpnicfIPsecTunPolicyNumV2_Object = MibTableColumn
hpnicfIPsecTunPolicyNumV2 = _HpnicfIPsecTunPolicyNumV2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 2, 1, 32),
    _HpnicfIPsecTunPolicyNumV2_Type()
)
hpnicfIPsecTunPolicyNumV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPsecTunPolicyNumV2.setStatus("current")


class _HpnicfIPsecTunStatusV2_Type(Integer32):
    """Custom type hpnicfIPsecTunStatusV2 based on Integer32"""
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


_HpnicfIPsecTunStatusV2_Type.__name__ = "Integer32"
_HpnicfIPsecTunStatusV2_Object = MibTableColumn
hpnicfIPsecTunStatusV2 = _HpnicfIPsecTunStatusV2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 2, 1, 33),
    _HpnicfIPsecTunStatusV2_Type()
)
hpnicfIPsecTunStatusV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPsecTunStatusV2.setStatus("current")
_HpnicfIPsecTunnelStatV2Table_Object = MibTable
hpnicfIPsecTunnelStatV2Table = _HpnicfIPsecTunnelStatV2Table_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 3)
)
if mibBuilder.loadTexts:
    hpnicfIPsecTunnelStatV2Table.setStatus("current")
_HpnicfIPsecTunnelStatV2Entry_Object = MibTableRow
hpnicfIPsecTunnelStatV2Entry = _HpnicfIPsecTunnelStatV2Entry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 3, 1)
)
hpnicfIPsecTunnelStatV2Entry.setIndexNames(
    (0, "HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecTunIndexV2"),
)
if mibBuilder.loadTexts:
    hpnicfIPsecTunnelStatV2Entry.setStatus("current")
_HpnicfIPsecTunInOctetsV2_Type = Counter64
_HpnicfIPsecTunInOctetsV2_Object = MibTableColumn
hpnicfIPsecTunInOctetsV2 = _HpnicfIPsecTunInOctetsV2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 3, 1, 1),
    _HpnicfIPsecTunInOctetsV2_Type()
)
hpnicfIPsecTunInOctetsV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPsecTunInOctetsV2.setStatus("current")
_HpnicfIPsecTunInDecompOctetsV2_Type = Counter64
_HpnicfIPsecTunInDecompOctetsV2_Object = MibTableColumn
hpnicfIPsecTunInDecompOctetsV2 = _HpnicfIPsecTunInDecompOctetsV2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 3, 1, 2),
    _HpnicfIPsecTunInDecompOctetsV2_Type()
)
hpnicfIPsecTunInDecompOctetsV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPsecTunInDecompOctetsV2.setStatus("current")
_HpnicfIPsecTunInPktsV2_Type = Counter64
_HpnicfIPsecTunInPktsV2_Object = MibTableColumn
hpnicfIPsecTunInPktsV2 = _HpnicfIPsecTunInPktsV2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 3, 1, 3),
    _HpnicfIPsecTunInPktsV2_Type()
)
hpnicfIPsecTunInPktsV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPsecTunInPktsV2.setStatus("current")
_HpnicfIPsecTunInDropPktsV2_Type = Counter64
_HpnicfIPsecTunInDropPktsV2_Object = MibTableColumn
hpnicfIPsecTunInDropPktsV2 = _HpnicfIPsecTunInDropPktsV2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 3, 1, 4),
    _HpnicfIPsecTunInDropPktsV2_Type()
)
hpnicfIPsecTunInDropPktsV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPsecTunInDropPktsV2.setStatus("current")
_HpnicfIPsecTunInReplayDropPktsV2_Type = Counter64
_HpnicfIPsecTunInReplayDropPktsV2_Object = MibTableColumn
hpnicfIPsecTunInReplayDropPktsV2 = _HpnicfIPsecTunInReplayDropPktsV2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 3, 1, 5),
    _HpnicfIPsecTunInReplayDropPktsV2_Type()
)
hpnicfIPsecTunInReplayDropPktsV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPsecTunInReplayDropPktsV2.setStatus("current")
_HpnicfIPsecTunInAuthFailsV2_Type = Counter64
_HpnicfIPsecTunInAuthFailsV2_Object = MibTableColumn
hpnicfIPsecTunInAuthFailsV2 = _HpnicfIPsecTunInAuthFailsV2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 3, 1, 6),
    _HpnicfIPsecTunInAuthFailsV2_Type()
)
hpnicfIPsecTunInAuthFailsV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPsecTunInAuthFailsV2.setStatus("current")
_HpnicfIPsecTunInDecryptFailsV2_Type = Counter64
_HpnicfIPsecTunInDecryptFailsV2_Object = MibTableColumn
hpnicfIPsecTunInDecryptFailsV2 = _HpnicfIPsecTunInDecryptFailsV2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 3, 1, 7),
    _HpnicfIPsecTunInDecryptFailsV2_Type()
)
hpnicfIPsecTunInDecryptFailsV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPsecTunInDecryptFailsV2.setStatus("current")
_HpnicfIPsecTunOutOctetsV2_Type = Counter64
_HpnicfIPsecTunOutOctetsV2_Object = MibTableColumn
hpnicfIPsecTunOutOctetsV2 = _HpnicfIPsecTunOutOctetsV2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 3, 1, 8),
    _HpnicfIPsecTunOutOctetsV2_Type()
)
hpnicfIPsecTunOutOctetsV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPsecTunOutOctetsV2.setStatus("current")
_HpnicfIPsecTunOutUncompOctetsV2_Type = Counter64
_HpnicfIPsecTunOutUncompOctetsV2_Object = MibTableColumn
hpnicfIPsecTunOutUncompOctetsV2 = _HpnicfIPsecTunOutUncompOctetsV2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 3, 1, 9),
    _HpnicfIPsecTunOutUncompOctetsV2_Type()
)
hpnicfIPsecTunOutUncompOctetsV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPsecTunOutUncompOctetsV2.setStatus("current")
_HpnicfIPsecTunOutPktsV2_Type = Counter64
_HpnicfIPsecTunOutPktsV2_Object = MibTableColumn
hpnicfIPsecTunOutPktsV2 = _HpnicfIPsecTunOutPktsV2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 3, 1, 10),
    _HpnicfIPsecTunOutPktsV2_Type()
)
hpnicfIPsecTunOutPktsV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPsecTunOutPktsV2.setStatus("current")
_HpnicfIPsecTunOutDropPktsV2_Type = Counter64
_HpnicfIPsecTunOutDropPktsV2_Object = MibTableColumn
hpnicfIPsecTunOutDropPktsV2 = _HpnicfIPsecTunOutDropPktsV2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 3, 1, 11),
    _HpnicfIPsecTunOutDropPktsV2_Type()
)
hpnicfIPsecTunOutDropPktsV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPsecTunOutDropPktsV2.setStatus("current")
_HpnicfIPsecTunOutEncryptFailsV2_Type = Counter64
_HpnicfIPsecTunOutEncryptFailsV2_Object = MibTableColumn
hpnicfIPsecTunOutEncryptFailsV2 = _HpnicfIPsecTunOutEncryptFailsV2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 3, 1, 12),
    _HpnicfIPsecTunOutEncryptFailsV2_Type()
)
hpnicfIPsecTunOutEncryptFailsV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPsecTunOutEncryptFailsV2.setStatus("current")
_HpnicfIPsecTunNoMemoryDropPktsV2_Type = Counter64
_HpnicfIPsecTunNoMemoryDropPktsV2_Object = MibTableColumn
hpnicfIPsecTunNoMemoryDropPktsV2 = _HpnicfIPsecTunNoMemoryDropPktsV2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 3, 1, 13),
    _HpnicfIPsecTunNoMemoryDropPktsV2_Type()
)
hpnicfIPsecTunNoMemoryDropPktsV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPsecTunNoMemoryDropPktsV2.setStatus("current")
_HpnicfIPsecTunQueueFullDropPktsV2_Type = Counter64
_HpnicfIPsecTunQueueFullDropPktsV2_Object = MibTableColumn
hpnicfIPsecTunQueueFullDropPktsV2 = _HpnicfIPsecTunQueueFullDropPktsV2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 3, 1, 14),
    _HpnicfIPsecTunQueueFullDropPktsV2_Type()
)
hpnicfIPsecTunQueueFullDropPktsV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPsecTunQueueFullDropPktsV2.setStatus("current")
_HpnicfIPsecTunInvalidLenDropPktsV2_Type = Counter64
_HpnicfIPsecTunInvalidLenDropPktsV2_Object = MibTableColumn
hpnicfIPsecTunInvalidLenDropPktsV2 = _HpnicfIPsecTunInvalidLenDropPktsV2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 3, 1, 15),
    _HpnicfIPsecTunInvalidLenDropPktsV2_Type()
)
hpnicfIPsecTunInvalidLenDropPktsV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPsecTunInvalidLenDropPktsV2.setStatus("current")
_HpnicfIPsecTunTooLongDropPktsV2_Type = Counter64
_HpnicfIPsecTunTooLongDropPktsV2_Object = MibTableColumn
hpnicfIPsecTunTooLongDropPktsV2 = _HpnicfIPsecTunTooLongDropPktsV2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 3, 1, 16),
    _HpnicfIPsecTunTooLongDropPktsV2_Type()
)
hpnicfIPsecTunTooLongDropPktsV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPsecTunTooLongDropPktsV2.setStatus("current")
_HpnicfIPsecTunInvalidSaDropPktsV2_Type = Counter64
_HpnicfIPsecTunInvalidSaDropPktsV2_Object = MibTableColumn
hpnicfIPsecTunInvalidSaDropPktsV2 = _HpnicfIPsecTunInvalidSaDropPktsV2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 3, 1, 17),
    _HpnicfIPsecTunInvalidSaDropPktsV2_Type()
)
hpnicfIPsecTunInvalidSaDropPktsV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPsecTunInvalidSaDropPktsV2.setStatus("current")
_HpnicfIPsecSaV2Table_Object = MibTable
hpnicfIPsecSaV2Table = _HpnicfIPsecSaV2Table_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 4)
)
if mibBuilder.loadTexts:
    hpnicfIPsecSaV2Table.setStatus("current")
_HpnicfIPsecSaV2Entry_Object = MibTableRow
hpnicfIPsecSaV2Entry = _HpnicfIPsecSaV2Entry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 4, 1)
)
hpnicfIPsecSaV2Entry.setIndexNames(
    (0, "HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecTunIndexV2"),
    (0, "HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecSaIndexV2"),
)
if mibBuilder.loadTexts:
    hpnicfIPsecSaV2Entry.setStatus("current")


class _HpnicfIPsecSaIndexV2_Type(Integer32):
    """Custom type hpnicfIPsecSaIndexV2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpnicfIPsecSaIndexV2_Type.__name__ = "Integer32"
_HpnicfIPsecSaIndexV2_Object = MibTableColumn
hpnicfIPsecSaIndexV2 = _HpnicfIPsecSaIndexV2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 4, 1, 1),
    _HpnicfIPsecSaIndexV2_Type()
)
hpnicfIPsecSaIndexV2.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfIPsecSaIndexV2.setStatus("current")


class _HpnicfIPsecSaDirectionV2_Type(Integer32):
    """Custom type hpnicfIPsecSaDirectionV2 based on Integer32"""
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


_HpnicfIPsecSaDirectionV2_Type.__name__ = "Integer32"
_HpnicfIPsecSaDirectionV2_Object = MibTableColumn
hpnicfIPsecSaDirectionV2 = _HpnicfIPsecSaDirectionV2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 4, 1, 2),
    _HpnicfIPsecSaDirectionV2_Type()
)
hpnicfIPsecSaDirectionV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPsecSaDirectionV2.setStatus("current")


class _HpnicfIPsecSaSpiValueV2_Type(Unsigned32):
    """Custom type hpnicfIPsecSaSpiValueV2 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_HpnicfIPsecSaSpiValueV2_Type.__name__ = "Unsigned32"
_HpnicfIPsecSaSpiValueV2_Object = MibTableColumn
hpnicfIPsecSaSpiValueV2 = _HpnicfIPsecSaSpiValueV2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 4, 1, 3),
    _HpnicfIPsecSaSpiValueV2_Type()
)
hpnicfIPsecSaSpiValueV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPsecSaSpiValueV2.setStatus("current")
_HpnicfIPsecSaSecProtocolV2_Type = HpnicfIPsecSaProtocolV2
_HpnicfIPsecSaSecProtocolV2_Object = MibTableColumn
hpnicfIPsecSaSecProtocolV2 = _HpnicfIPsecSaSecProtocolV2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 4, 1, 4),
    _HpnicfIPsecSaSecProtocolV2_Type()
)
hpnicfIPsecSaSecProtocolV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPsecSaSecProtocolV2.setStatus("current")
_HpnicfIPsecSaEncryptAlgoV2_Type = HpnicfIPsecEncryptAlgoV2
_HpnicfIPsecSaEncryptAlgoV2_Object = MibTableColumn
hpnicfIPsecSaEncryptAlgoV2 = _HpnicfIPsecSaEncryptAlgoV2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 4, 1, 5),
    _HpnicfIPsecSaEncryptAlgoV2_Type()
)
hpnicfIPsecSaEncryptAlgoV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPsecSaEncryptAlgoV2.setStatus("current")
_HpnicfIPsecSaAuthAlgoV2_Type = HpnicfIPsecAuthAlgoV2
_HpnicfIPsecSaAuthAlgoV2_Object = MibTableColumn
hpnicfIPsecSaAuthAlgoV2 = _HpnicfIPsecSaAuthAlgoV2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 4, 1, 6),
    _HpnicfIPsecSaAuthAlgoV2_Type()
)
hpnicfIPsecSaAuthAlgoV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPsecSaAuthAlgoV2.setStatus("current")


class _HpnicfIPsecSaStatusV2_Type(Integer32):
    """Custom type hpnicfIPsecSaStatusV2 based on Integer32"""
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


_HpnicfIPsecSaStatusV2_Type.__name__ = "Integer32"
_HpnicfIPsecSaStatusV2_Object = MibTableColumn
hpnicfIPsecSaStatusV2 = _HpnicfIPsecSaStatusV2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 4, 1, 7),
    _HpnicfIPsecSaStatusV2_Type()
)
hpnicfIPsecSaStatusV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPsecSaStatusV2.setStatus("current")
_HpnicfIPsecTrafficV2Table_Object = MibTable
hpnicfIPsecTrafficV2Table = _HpnicfIPsecTrafficV2Table_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 5)
)
if mibBuilder.loadTexts:
    hpnicfIPsecTrafficV2Table.setStatus("current")
_HpnicfIPsecTrafficV2Entry_Object = MibTableRow
hpnicfIPsecTrafficV2Entry = _HpnicfIPsecTrafficV2Entry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 5, 1)
)
hpnicfIPsecTrafficV2Entry.setIndexNames(
    (0, "HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecTunIndexV2"),
)
if mibBuilder.loadTexts:
    hpnicfIPsecTrafficV2Entry.setStatus("current")
_HpnicfIPsecTrafficLocalTypeV2_Type = HpnicfIPsecTrafficTypeV2
_HpnicfIPsecTrafficLocalTypeV2_Object = MibTableColumn
hpnicfIPsecTrafficLocalTypeV2 = _HpnicfIPsecTrafficLocalTypeV2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 5, 1, 1),
    _HpnicfIPsecTrafficLocalTypeV2_Type()
)
hpnicfIPsecTrafficLocalTypeV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPsecTrafficLocalTypeV2.setStatus("current")
_HpnicfIPsecTrafficLocalAddr1TypeV2_Type = InetAddressType
_HpnicfIPsecTrafficLocalAddr1TypeV2_Object = MibTableColumn
hpnicfIPsecTrafficLocalAddr1TypeV2 = _HpnicfIPsecTrafficLocalAddr1TypeV2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 5, 1, 2),
    _HpnicfIPsecTrafficLocalAddr1TypeV2_Type()
)
hpnicfIPsecTrafficLocalAddr1TypeV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPsecTrafficLocalAddr1TypeV2.setStatus("current")
_HpnicfIPsecTrafficLocalAddr1V2_Type = InetAddress
_HpnicfIPsecTrafficLocalAddr1V2_Object = MibTableColumn
hpnicfIPsecTrafficLocalAddr1V2 = _HpnicfIPsecTrafficLocalAddr1V2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 5, 1, 3),
    _HpnicfIPsecTrafficLocalAddr1V2_Type()
)
hpnicfIPsecTrafficLocalAddr1V2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPsecTrafficLocalAddr1V2.setStatus("current")
_HpnicfIPsecTrafficLocalAddr2TypeV2_Type = InetAddressType
_HpnicfIPsecTrafficLocalAddr2TypeV2_Object = MibTableColumn
hpnicfIPsecTrafficLocalAddr2TypeV2 = _HpnicfIPsecTrafficLocalAddr2TypeV2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 5, 1, 4),
    _HpnicfIPsecTrafficLocalAddr2TypeV2_Type()
)
hpnicfIPsecTrafficLocalAddr2TypeV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPsecTrafficLocalAddr2TypeV2.setStatus("current")
_HpnicfIPsecTrafficLocalAddr2V2_Type = InetAddress
_HpnicfIPsecTrafficLocalAddr2V2_Object = MibTableColumn
hpnicfIPsecTrafficLocalAddr2V2 = _HpnicfIPsecTrafficLocalAddr2V2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 5, 1, 5),
    _HpnicfIPsecTrafficLocalAddr2V2_Type()
)
hpnicfIPsecTrafficLocalAddr2V2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPsecTrafficLocalAddr2V2.setStatus("current")


class _HpnicfIPsecTrafficLocalProtocol1V2_Type(Integer32):
    """Custom type hpnicfIPsecTrafficLocalProtocol1V2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpnicfIPsecTrafficLocalProtocol1V2_Type.__name__ = "Integer32"
_HpnicfIPsecTrafficLocalProtocol1V2_Object = MibTableColumn
hpnicfIPsecTrafficLocalProtocol1V2 = _HpnicfIPsecTrafficLocalProtocol1V2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 5, 1, 6),
    _HpnicfIPsecTrafficLocalProtocol1V2_Type()
)
hpnicfIPsecTrafficLocalProtocol1V2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPsecTrafficLocalProtocol1V2.setStatus("current")


class _HpnicfIPsecTrafficLocalProtocol2V2_Type(Integer32):
    """Custom type hpnicfIPsecTrafficLocalProtocol2V2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpnicfIPsecTrafficLocalProtocol2V2_Type.__name__ = "Integer32"
_HpnicfIPsecTrafficLocalProtocol2V2_Object = MibTableColumn
hpnicfIPsecTrafficLocalProtocol2V2 = _HpnicfIPsecTrafficLocalProtocol2V2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 5, 1, 7),
    _HpnicfIPsecTrafficLocalProtocol2V2_Type()
)
hpnicfIPsecTrafficLocalProtocol2V2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPsecTrafficLocalProtocol2V2.setStatus("current")


class _HpnicfIPsecTrafficLocalPort1V2_Type(Integer32):
    """Custom type hpnicfIPsecTrafficLocalPort1V2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfIPsecTrafficLocalPort1V2_Type.__name__ = "Integer32"
_HpnicfIPsecTrafficLocalPort1V2_Object = MibTableColumn
hpnicfIPsecTrafficLocalPort1V2 = _HpnicfIPsecTrafficLocalPort1V2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 5, 1, 8),
    _HpnicfIPsecTrafficLocalPort1V2_Type()
)
hpnicfIPsecTrafficLocalPort1V2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPsecTrafficLocalPort1V2.setStatus("current")


class _HpnicfIPsecTrafficLocalPort2V2_Type(Integer32):
    """Custom type hpnicfIPsecTrafficLocalPort2V2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfIPsecTrafficLocalPort2V2_Type.__name__ = "Integer32"
_HpnicfIPsecTrafficLocalPort2V2_Object = MibTableColumn
hpnicfIPsecTrafficLocalPort2V2 = _HpnicfIPsecTrafficLocalPort2V2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 5, 1, 9),
    _HpnicfIPsecTrafficLocalPort2V2_Type()
)
hpnicfIPsecTrafficLocalPort2V2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPsecTrafficLocalPort2V2.setStatus("current")
_HpnicfIPsecTrafficRemoteTypeV2_Type = HpnicfIPsecTrafficTypeV2
_HpnicfIPsecTrafficRemoteTypeV2_Object = MibTableColumn
hpnicfIPsecTrafficRemoteTypeV2 = _HpnicfIPsecTrafficRemoteTypeV2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 5, 1, 10),
    _HpnicfIPsecTrafficRemoteTypeV2_Type()
)
hpnicfIPsecTrafficRemoteTypeV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPsecTrafficRemoteTypeV2.setStatus("current")
_HpnicfIPsecTrafficRemAddr1TypeV2_Type = InetAddressType
_HpnicfIPsecTrafficRemAddr1TypeV2_Object = MibTableColumn
hpnicfIPsecTrafficRemAddr1TypeV2 = _HpnicfIPsecTrafficRemAddr1TypeV2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 5, 1, 11),
    _HpnicfIPsecTrafficRemAddr1TypeV2_Type()
)
hpnicfIPsecTrafficRemAddr1TypeV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPsecTrafficRemAddr1TypeV2.setStatus("current")
_HpnicfIPsecTrafficRemAddr1V2_Type = InetAddress
_HpnicfIPsecTrafficRemAddr1V2_Object = MibTableColumn
hpnicfIPsecTrafficRemAddr1V2 = _HpnicfIPsecTrafficRemAddr1V2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 5, 1, 12),
    _HpnicfIPsecTrafficRemAddr1V2_Type()
)
hpnicfIPsecTrafficRemAddr1V2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPsecTrafficRemAddr1V2.setStatus("current")
_HpnicfIPsecTrafficRemAddr2TypeV2_Type = InetAddressType
_HpnicfIPsecTrafficRemAddr2TypeV2_Object = MibTableColumn
hpnicfIPsecTrafficRemAddr2TypeV2 = _HpnicfIPsecTrafficRemAddr2TypeV2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 5, 1, 13),
    _HpnicfIPsecTrafficRemAddr2TypeV2_Type()
)
hpnicfIPsecTrafficRemAddr2TypeV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPsecTrafficRemAddr2TypeV2.setStatus("current")
_HpnicfIPsecTrafficRemAddr2V2_Type = InetAddress
_HpnicfIPsecTrafficRemAddr2V2_Object = MibTableColumn
hpnicfIPsecTrafficRemAddr2V2 = _HpnicfIPsecTrafficRemAddr2V2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 5, 1, 14),
    _HpnicfIPsecTrafficRemAddr2V2_Type()
)
hpnicfIPsecTrafficRemAddr2V2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPsecTrafficRemAddr2V2.setStatus("current")


class _HpnicfIPsecTrafficRemoPro1V2_Type(Integer32):
    """Custom type hpnicfIPsecTrafficRemoPro1V2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpnicfIPsecTrafficRemoPro1V2_Type.__name__ = "Integer32"
_HpnicfIPsecTrafficRemoPro1V2_Object = MibTableColumn
hpnicfIPsecTrafficRemoPro1V2 = _HpnicfIPsecTrafficRemoPro1V2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 5, 1, 15),
    _HpnicfIPsecTrafficRemoPro1V2_Type()
)
hpnicfIPsecTrafficRemoPro1V2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPsecTrafficRemoPro1V2.setStatus("current")


class _HpnicfIPsecTrafficRemoPro2V2_Type(Integer32):
    """Custom type hpnicfIPsecTrafficRemoPro2V2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpnicfIPsecTrafficRemoPro2V2_Type.__name__ = "Integer32"
_HpnicfIPsecTrafficRemoPro2V2_Object = MibTableColumn
hpnicfIPsecTrafficRemoPro2V2 = _HpnicfIPsecTrafficRemoPro2V2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 5, 1, 16),
    _HpnicfIPsecTrafficRemoPro2V2_Type()
)
hpnicfIPsecTrafficRemoPro2V2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPsecTrafficRemoPro2V2.setStatus("current")


class _HpnicfIPsecTrafficRemPort1V2_Type(Integer32):
    """Custom type hpnicfIPsecTrafficRemPort1V2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfIPsecTrafficRemPort1V2_Type.__name__ = "Integer32"
_HpnicfIPsecTrafficRemPort1V2_Object = MibTableColumn
hpnicfIPsecTrafficRemPort1V2 = _HpnicfIPsecTrafficRemPort1V2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 5, 1, 17),
    _HpnicfIPsecTrafficRemPort1V2_Type()
)
hpnicfIPsecTrafficRemPort1V2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPsecTrafficRemPort1V2.setStatus("current")


class _HpnicfIPsecTrafficRemPort2V2_Type(Integer32):
    """Custom type hpnicfIPsecTrafficRemPort2V2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfIPsecTrafficRemPort2V2_Type.__name__ = "Integer32"
_HpnicfIPsecTrafficRemPort2V2_Object = MibTableColumn
hpnicfIPsecTrafficRemPort2V2 = _HpnicfIPsecTrafficRemPort2V2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 5, 1, 18),
    _HpnicfIPsecTrafficRemPort2V2_Type()
)
hpnicfIPsecTrafficRemPort2V2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPsecTrafficRemPort2V2.setStatus("current")
_HpnicfIPsecGlobalStatsV2_ObjectIdentity = ObjectIdentity
hpnicfIPsecGlobalStatsV2 = _HpnicfIPsecGlobalStatsV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 6)
)
_HpnicfIPsecGlobalActiveTunnelsV2_Type = Gauge32
_HpnicfIPsecGlobalActiveTunnelsV2_Object = MibScalar
hpnicfIPsecGlobalActiveTunnelsV2 = _HpnicfIPsecGlobalActiveTunnelsV2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 6, 1),
    _HpnicfIPsecGlobalActiveTunnelsV2_Type()
)
hpnicfIPsecGlobalActiveTunnelsV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPsecGlobalActiveTunnelsV2.setStatus("current")
_HpnicfIPsecGlobalActiveSasV2_Type = Gauge32
_HpnicfIPsecGlobalActiveSasV2_Object = MibScalar
hpnicfIPsecGlobalActiveSasV2 = _HpnicfIPsecGlobalActiveSasV2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 6, 2),
    _HpnicfIPsecGlobalActiveSasV2_Type()
)
hpnicfIPsecGlobalActiveSasV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPsecGlobalActiveSasV2.setStatus("current")
_HpnicfIPsecGlobalInOctetsV2_Type = Counter64
_HpnicfIPsecGlobalInOctetsV2_Object = MibScalar
hpnicfIPsecGlobalInOctetsV2 = _HpnicfIPsecGlobalInOctetsV2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 6, 3),
    _HpnicfIPsecGlobalInOctetsV2_Type()
)
hpnicfIPsecGlobalInOctetsV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPsecGlobalInOctetsV2.setStatus("current")
_HpnicfIPsecGlobalInDecompOctetsV2_Type = Counter64
_HpnicfIPsecGlobalInDecompOctetsV2_Object = MibScalar
hpnicfIPsecGlobalInDecompOctetsV2 = _HpnicfIPsecGlobalInDecompOctetsV2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 6, 4),
    _HpnicfIPsecGlobalInDecompOctetsV2_Type()
)
hpnicfIPsecGlobalInDecompOctetsV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPsecGlobalInDecompOctetsV2.setStatus("current")
_HpnicfIPsecGlobalInPktsV2_Type = Counter64
_HpnicfIPsecGlobalInPktsV2_Object = MibScalar
hpnicfIPsecGlobalInPktsV2 = _HpnicfIPsecGlobalInPktsV2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 6, 5),
    _HpnicfIPsecGlobalInPktsV2_Type()
)
hpnicfIPsecGlobalInPktsV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPsecGlobalInPktsV2.setStatus("current")
_HpnicfIPsecGlobalInDropsV2_Type = Counter64
_HpnicfIPsecGlobalInDropsV2_Object = MibScalar
hpnicfIPsecGlobalInDropsV2 = _HpnicfIPsecGlobalInDropsV2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 6, 6),
    _HpnicfIPsecGlobalInDropsV2_Type()
)
hpnicfIPsecGlobalInDropsV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPsecGlobalInDropsV2.setStatus("current")
_HpnicfIPsecGlobalInReplayDropsV2_Type = Counter64
_HpnicfIPsecGlobalInReplayDropsV2_Object = MibScalar
hpnicfIPsecGlobalInReplayDropsV2 = _HpnicfIPsecGlobalInReplayDropsV2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 6, 7),
    _HpnicfIPsecGlobalInReplayDropsV2_Type()
)
hpnicfIPsecGlobalInReplayDropsV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPsecGlobalInReplayDropsV2.setStatus("current")
_HpnicfIPsecGlobalInAuthFailsV2_Type = Counter64
_HpnicfIPsecGlobalInAuthFailsV2_Object = MibScalar
hpnicfIPsecGlobalInAuthFailsV2 = _HpnicfIPsecGlobalInAuthFailsV2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 6, 8),
    _HpnicfIPsecGlobalInAuthFailsV2_Type()
)
hpnicfIPsecGlobalInAuthFailsV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPsecGlobalInAuthFailsV2.setStatus("current")
_HpnicfIPsecGlobalInDecryptFailsV2_Type = Counter64
_HpnicfIPsecGlobalInDecryptFailsV2_Object = MibScalar
hpnicfIPsecGlobalInDecryptFailsV2 = _HpnicfIPsecGlobalInDecryptFailsV2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 6, 9),
    _HpnicfIPsecGlobalInDecryptFailsV2_Type()
)
hpnicfIPsecGlobalInDecryptFailsV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPsecGlobalInDecryptFailsV2.setStatus("current")
_HpnicfIPsecGlobalOutOctetsV2_Type = Counter64
_HpnicfIPsecGlobalOutOctetsV2_Object = MibScalar
hpnicfIPsecGlobalOutOctetsV2 = _HpnicfIPsecGlobalOutOctetsV2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 6, 10),
    _HpnicfIPsecGlobalOutOctetsV2_Type()
)
hpnicfIPsecGlobalOutOctetsV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPsecGlobalOutOctetsV2.setStatus("current")
_HpnicfIPsecGlobalOutUncompOctetsV2_Type = Counter64
_HpnicfIPsecGlobalOutUncompOctetsV2_Object = MibScalar
hpnicfIPsecGlobalOutUncompOctetsV2 = _HpnicfIPsecGlobalOutUncompOctetsV2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 6, 11),
    _HpnicfIPsecGlobalOutUncompOctetsV2_Type()
)
hpnicfIPsecGlobalOutUncompOctetsV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPsecGlobalOutUncompOctetsV2.setStatus("current")
_HpnicfIPsecGlobalOutPktsV2_Type = Counter64
_HpnicfIPsecGlobalOutPktsV2_Object = MibScalar
hpnicfIPsecGlobalOutPktsV2 = _HpnicfIPsecGlobalOutPktsV2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 6, 12),
    _HpnicfIPsecGlobalOutPktsV2_Type()
)
hpnicfIPsecGlobalOutPktsV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPsecGlobalOutPktsV2.setStatus("current")
_HpnicfIPsecGlobalOutDropsV2_Type = Counter64
_HpnicfIPsecGlobalOutDropsV2_Object = MibScalar
hpnicfIPsecGlobalOutDropsV2 = _HpnicfIPsecGlobalOutDropsV2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 6, 13),
    _HpnicfIPsecGlobalOutDropsV2_Type()
)
hpnicfIPsecGlobalOutDropsV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPsecGlobalOutDropsV2.setStatus("current")
_HpnicfIPsecGlobalOutEncryptFailsV2_Type = Counter64
_HpnicfIPsecGlobalOutEncryptFailsV2_Object = MibScalar
hpnicfIPsecGlobalOutEncryptFailsV2 = _HpnicfIPsecGlobalOutEncryptFailsV2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 6, 14),
    _HpnicfIPsecGlobalOutEncryptFailsV2_Type()
)
hpnicfIPsecGlobalOutEncryptFailsV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPsecGlobalOutEncryptFailsV2.setStatus("current")
_HpnicfIPsecGlobalNoMemoryDropsV2_Type = Counter64
_HpnicfIPsecGlobalNoMemoryDropsV2_Object = MibScalar
hpnicfIPsecGlobalNoMemoryDropsV2 = _HpnicfIPsecGlobalNoMemoryDropsV2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 6, 15),
    _HpnicfIPsecGlobalNoMemoryDropsV2_Type()
)
hpnicfIPsecGlobalNoMemoryDropsV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPsecGlobalNoMemoryDropsV2.setStatus("current")
_HpnicfIPsecGlobalNoFindSaDropsV2_Type = Counter64
_HpnicfIPsecGlobalNoFindSaDropsV2_Object = MibScalar
hpnicfIPsecGlobalNoFindSaDropsV2 = _HpnicfIPsecGlobalNoFindSaDropsV2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 6, 16),
    _HpnicfIPsecGlobalNoFindSaDropsV2_Type()
)
hpnicfIPsecGlobalNoFindSaDropsV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPsecGlobalNoFindSaDropsV2.setStatus("current")
_HpnicfIPsecGlobalQueueFullDropsV2_Type = Counter64
_HpnicfIPsecGlobalQueueFullDropsV2_Object = MibScalar
hpnicfIPsecGlobalQueueFullDropsV2 = _HpnicfIPsecGlobalQueueFullDropsV2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 6, 17),
    _HpnicfIPsecGlobalQueueFullDropsV2_Type()
)
hpnicfIPsecGlobalQueueFullDropsV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPsecGlobalQueueFullDropsV2.setStatus("current")
_HpnicfIPsecGlobalInvalidLenDropsV2_Type = Counter64
_HpnicfIPsecGlobalInvalidLenDropsV2_Object = MibScalar
hpnicfIPsecGlobalInvalidLenDropsV2 = _HpnicfIPsecGlobalInvalidLenDropsV2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 6, 18),
    _HpnicfIPsecGlobalInvalidLenDropsV2_Type()
)
hpnicfIPsecGlobalInvalidLenDropsV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPsecGlobalInvalidLenDropsV2.setStatus("current")
_HpnicfIPsecGlobalTooLongDropsV2_Type = Counter64
_HpnicfIPsecGlobalTooLongDropsV2_Object = MibScalar
hpnicfIPsecGlobalTooLongDropsV2 = _HpnicfIPsecGlobalTooLongDropsV2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 6, 19),
    _HpnicfIPsecGlobalTooLongDropsV2_Type()
)
hpnicfIPsecGlobalTooLongDropsV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPsecGlobalTooLongDropsV2.setStatus("current")
_HpnicfIPsecGlobalInvalidSaDropsV2_Type = Counter64
_HpnicfIPsecGlobalInvalidSaDropsV2_Object = MibScalar
hpnicfIPsecGlobalInvalidSaDropsV2 = _HpnicfIPsecGlobalInvalidSaDropsV2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 6, 20),
    _HpnicfIPsecGlobalInvalidSaDropsV2_Type()
)
hpnicfIPsecGlobalInvalidSaDropsV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPsecGlobalInvalidSaDropsV2.setStatus("current")
_HpnicfIPsecTrapObjectV2_ObjectIdentity = ObjectIdentity
hpnicfIPsecTrapObjectV2 = _HpnicfIPsecTrapObjectV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 7)
)
_HpnicfIPsecPolicyNameV2_Type = DisplayString
_HpnicfIPsecPolicyNameV2_Object = MibScalar
hpnicfIPsecPolicyNameV2 = _HpnicfIPsecPolicyNameV2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 7, 1),
    _HpnicfIPsecPolicyNameV2_Type()
)
hpnicfIPsecPolicyNameV2.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfIPsecPolicyNameV2.setStatus("current")
_HpnicfIPsecPolicySeqNumV2_Type = Integer32
_HpnicfIPsecPolicySeqNumV2_Object = MibScalar
hpnicfIPsecPolicySeqNumV2 = _HpnicfIPsecPolicySeqNumV2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 7, 2),
    _HpnicfIPsecPolicySeqNumV2_Type()
)
hpnicfIPsecPolicySeqNumV2.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfIPsecPolicySeqNumV2.setStatus("current")
_HpnicfIPsecPolicySizeV2_Type = Integer32
_HpnicfIPsecPolicySizeV2_Object = MibScalar
hpnicfIPsecPolicySizeV2 = _HpnicfIPsecPolicySizeV2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 7, 3),
    _HpnicfIPsecPolicySizeV2_Type()
)
hpnicfIPsecPolicySizeV2.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfIPsecPolicySizeV2.setStatus("current")
_HpnicfIPsecTrapCntlV2_ObjectIdentity = ObjectIdentity
hpnicfIPsecTrapCntlV2 = _HpnicfIPsecTrapCntlV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 8)
)
_HpnicfIPsecTrapGlobalCntlV2_Type = TruthValue
_HpnicfIPsecTrapGlobalCntlV2_Object = MibScalar
hpnicfIPsecTrapGlobalCntlV2 = _HpnicfIPsecTrapGlobalCntlV2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 8, 1),
    _HpnicfIPsecTrapGlobalCntlV2_Type()
)
hpnicfIPsecTrapGlobalCntlV2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfIPsecTrapGlobalCntlV2.setStatus("current")
_HpnicfIPsecTunnelStartTrapCntlV2_Type = TruthValue
_HpnicfIPsecTunnelStartTrapCntlV2_Object = MibScalar
hpnicfIPsecTunnelStartTrapCntlV2 = _HpnicfIPsecTunnelStartTrapCntlV2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 8, 2),
    _HpnicfIPsecTunnelStartTrapCntlV2_Type()
)
hpnicfIPsecTunnelStartTrapCntlV2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfIPsecTunnelStartTrapCntlV2.setStatus("current")
_HpnicfIPsecTunnelStopTrapCntlV2_Type = TruthValue
_HpnicfIPsecTunnelStopTrapCntlV2_Object = MibScalar
hpnicfIPsecTunnelStopTrapCntlV2 = _HpnicfIPsecTunnelStopTrapCntlV2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 8, 3),
    _HpnicfIPsecTunnelStopTrapCntlV2_Type()
)
hpnicfIPsecTunnelStopTrapCntlV2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfIPsecTunnelStopTrapCntlV2.setStatus("current")
_HpnicfIPsecNoSaTrapCntlV2_Type = TruthValue
_HpnicfIPsecNoSaTrapCntlV2_Object = MibScalar
hpnicfIPsecNoSaTrapCntlV2 = _HpnicfIPsecNoSaTrapCntlV2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 8, 4),
    _HpnicfIPsecNoSaTrapCntlV2_Type()
)
hpnicfIPsecNoSaTrapCntlV2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfIPsecNoSaTrapCntlV2.setStatus("current")
_HpnicfIPsecAuthFailureTrapCntlV2_Type = TruthValue
_HpnicfIPsecAuthFailureTrapCntlV2_Object = MibScalar
hpnicfIPsecAuthFailureTrapCntlV2 = _HpnicfIPsecAuthFailureTrapCntlV2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 8, 5),
    _HpnicfIPsecAuthFailureTrapCntlV2_Type()
)
hpnicfIPsecAuthFailureTrapCntlV2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfIPsecAuthFailureTrapCntlV2.setStatus("current")
_HpnicfIPsecEncryFailureTrapCntlV2_Type = TruthValue
_HpnicfIPsecEncryFailureTrapCntlV2_Object = MibScalar
hpnicfIPsecEncryFailureTrapCntlV2 = _HpnicfIPsecEncryFailureTrapCntlV2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 8, 6),
    _HpnicfIPsecEncryFailureTrapCntlV2_Type()
)
hpnicfIPsecEncryFailureTrapCntlV2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfIPsecEncryFailureTrapCntlV2.setStatus("current")
_HpnicfIPsecDecryFailureTrapCntlV2_Type = TruthValue
_HpnicfIPsecDecryFailureTrapCntlV2_Object = MibScalar
hpnicfIPsecDecryFailureTrapCntlV2 = _HpnicfIPsecDecryFailureTrapCntlV2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 8, 7),
    _HpnicfIPsecDecryFailureTrapCntlV2_Type()
)
hpnicfIPsecDecryFailureTrapCntlV2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfIPsecDecryFailureTrapCntlV2.setStatus("current")
_HpnicfIPsecInvalidSaTrapCntlV2_Type = TruthValue
_HpnicfIPsecInvalidSaTrapCntlV2_Object = MibScalar
hpnicfIPsecInvalidSaTrapCntlV2 = _HpnicfIPsecInvalidSaTrapCntlV2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 8, 8),
    _HpnicfIPsecInvalidSaTrapCntlV2_Type()
)
hpnicfIPsecInvalidSaTrapCntlV2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfIPsecInvalidSaTrapCntlV2.setStatus("current")
_HpnicfIPsecPolicyAddTrapCntlV2_Type = TruthValue
_HpnicfIPsecPolicyAddTrapCntlV2_Object = MibScalar
hpnicfIPsecPolicyAddTrapCntlV2 = _HpnicfIPsecPolicyAddTrapCntlV2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 8, 9),
    _HpnicfIPsecPolicyAddTrapCntlV2_Type()
)
hpnicfIPsecPolicyAddTrapCntlV2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfIPsecPolicyAddTrapCntlV2.setStatus("current")
_HpnicfIPsecPolicyDelTrapCntlV2_Type = TruthValue
_HpnicfIPsecPolicyDelTrapCntlV2_Object = MibScalar
hpnicfIPsecPolicyDelTrapCntlV2 = _HpnicfIPsecPolicyDelTrapCntlV2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 8, 10),
    _HpnicfIPsecPolicyDelTrapCntlV2_Type()
)
hpnicfIPsecPolicyDelTrapCntlV2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfIPsecPolicyDelTrapCntlV2.setStatus("current")
_HpnicfIPsecPolicyAttachTrapCntlV2_Type = TruthValue
_HpnicfIPsecPolicyAttachTrapCntlV2_Object = MibScalar
hpnicfIPsecPolicyAttachTrapCntlV2 = _HpnicfIPsecPolicyAttachTrapCntlV2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 8, 11),
    _HpnicfIPsecPolicyAttachTrapCntlV2_Type()
)
hpnicfIPsecPolicyAttachTrapCntlV2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfIPsecPolicyAttachTrapCntlV2.setStatus("current")
_HpnicfIPsecPolicyDetachTrapCntlV2_Type = TruthValue
_HpnicfIPsecPolicyDetachTrapCntlV2_Object = MibScalar
hpnicfIPsecPolicyDetachTrapCntlV2 = _HpnicfIPsecPolicyDetachTrapCntlV2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 8, 12),
    _HpnicfIPsecPolicyDetachTrapCntlV2_Type()
)
hpnicfIPsecPolicyDetachTrapCntlV2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfIPsecPolicyDetachTrapCntlV2.setStatus("current")
_HpnicfIPsecTrapV2_ObjectIdentity = ObjectIdentity
hpnicfIPsecTrapV2 = _HpnicfIPsecTrapV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 9)
)
_HpnicfIPsecNotificationsV2_ObjectIdentity = ObjectIdentity
hpnicfIPsecNotificationsV2 = _HpnicfIPsecNotificationsV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 9, 0)
)
_HpnicfIPsecConformanceV2_ObjectIdentity = ObjectIdentity
hpnicfIPsecConformanceV2 = _HpnicfIPsecConformanceV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 2)
)
_HpnicfIPsecCompliancesV2_ObjectIdentity = ObjectIdentity
hpnicfIPsecCompliancesV2 = _HpnicfIPsecCompliancesV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 2, 1)
)
_HpnicfIPsecGroupsV2_ObjectIdentity = ObjectIdentity
hpnicfIPsecGroupsV2 = _HpnicfIPsecGroupsV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 2, 2)
)

# Managed Objects groups

hpnicfIPsecScalarObjectsGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 2, 2, 1)
)
hpnicfIPsecScalarObjectsGroupV2.setObjects(
    ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecMIBVersion")
)
if mibBuilder.loadTexts:
    hpnicfIPsecScalarObjectsGroupV2.setStatus("current")

hpnicfIPsecTunnelTableGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 2, 2, 2)
)
hpnicfIPsecTunnelTableGroupV2.setObjects(
      *(("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecTunIfIndexV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecTunIKETunnelIndexV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecTunIKETunLocalIDTypeV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecTunIKETunLocalIDVal1V2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecTunIKETunLocalIDVal2V2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecTunIKETunRemoteIDTypeV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecTunIKETunRemoteIDVal1V2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecTunIKETunRemoteIDVal2V2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecTunLocalAddrTypeV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecTunLocalAddrV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecTunRemoteAddrTypeV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecTunRemoteAddrV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecTunKeyTypeV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecTunEncapModeV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecTunInitiatorV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecTunLifeSizeV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecTunLifeTimeV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecTunRemainTimeV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecTunActiveTimeV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecTunRemainSizeV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecTunTotalRefreshesV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecTunCurrentSaInstancesV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecTunInSaEncryptAlgoV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecTunInSaAhAuthAlgoV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecTunInSaEspAuthAlgoV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecTunDiffHellmanGrpV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecTunOutSaEncryptAlgoV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecTunOutSaAhAuthAlgoV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecTunOutSaEspAuthAlgoV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecTunPolicyNameV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecTunPolicyNumV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecTunStatusV2"))
)
if mibBuilder.loadTexts:
    hpnicfIPsecTunnelTableGroupV2.setStatus("current")

hpnicfIPsecTunnelStatGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 2, 2, 3)
)
hpnicfIPsecTunnelStatGroupV2.setObjects(
      *(("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecTunInOctetsV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecTunInDecompOctetsV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecTunInPktsV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecTunInDropPktsV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecTunInReplayDropPktsV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecTunInAuthFailsV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecTunInDecryptFailsV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecTunOutOctetsV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecTunOutUncompOctetsV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecTunOutPktsV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecTunOutDropPktsV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecTunOutEncryptFailsV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecTunNoMemoryDropPktsV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecTunQueueFullDropPktsV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecTunInvalidLenDropPktsV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecTunTooLongDropPktsV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecTunInvalidSaDropPktsV2"))
)
if mibBuilder.loadTexts:
    hpnicfIPsecTunnelStatGroupV2.setStatus("current")

hpnicfIPsecSaGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 2, 2, 4)
)
hpnicfIPsecSaGroupV2.setObjects(
      *(("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecSaDirectionV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecSaSpiValueV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecSaSecProtocolV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecSaEncryptAlgoV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecSaAuthAlgoV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecSaStatusV2"))
)
if mibBuilder.loadTexts:
    hpnicfIPsecSaGroupV2.setStatus("current")

hpnicfIPsecTrafficTableGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 2, 2, 5)
)
hpnicfIPsecTrafficTableGroupV2.setObjects(
      *(("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecTrafficLocalTypeV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecTrafficLocalAddr1TypeV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecTrafficLocalAddr1V2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecTrafficLocalAddr2TypeV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecTrafficLocalAddr2V2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecTrafficLocalProtocol1V2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecTrafficLocalProtocol2V2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecTrafficLocalPort1V2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecTrafficLocalPort2V2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecTrafficRemoteTypeV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecTrafficRemAddr1TypeV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecTrafficRemAddr1V2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecTrafficRemAddr2TypeV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecTrafficRemAddr2V2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecTrafficRemoPro1V2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecTrafficRemoPro2V2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecTrafficRemPort1V2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecTrafficRemPort2V2"))
)
if mibBuilder.loadTexts:
    hpnicfIPsecTrafficTableGroupV2.setStatus("current")

hpnicfIPsecGlobalStatsGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 2, 2, 6)
)
hpnicfIPsecGlobalStatsGroupV2.setObjects(
      *(("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecGlobalActiveTunnelsV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecGlobalActiveSasV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecGlobalInOctetsV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecGlobalInDecompOctetsV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecGlobalInPktsV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecGlobalInDropsV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecGlobalInReplayDropsV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecGlobalInAuthFailsV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecGlobalInDecryptFailsV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecGlobalOutOctetsV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecGlobalOutUncompOctetsV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecGlobalOutPktsV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecGlobalOutDropsV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecGlobalOutEncryptFailsV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecGlobalNoMemoryDropsV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecGlobalNoFindSaDropsV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecGlobalQueueFullDropsV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecGlobalInvalidLenDropsV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecGlobalTooLongDropsV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecGlobalInvalidSaDropsV2"))
)
if mibBuilder.loadTexts:
    hpnicfIPsecGlobalStatsGroupV2.setStatus("current")

hpnicfIPsecTrapObjectGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 2, 2, 7)
)
hpnicfIPsecTrapObjectGroupV2.setObjects(
      *(("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecPolicyNameV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecPolicySeqNumV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecPolicySizeV2"))
)
if mibBuilder.loadTexts:
    hpnicfIPsecTrapObjectGroupV2.setStatus("current")

hpnicfIPsecTrapCntlGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 2, 2, 8)
)
hpnicfIPsecTrapCntlGroupV2.setObjects(
      *(("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecTrapGlobalCntlV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecTunnelStartTrapCntlV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecTunnelStopTrapCntlV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecNoSaTrapCntlV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecAuthFailureTrapCntlV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecEncryFailureTrapCntlV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecDecryFailureTrapCntlV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecInvalidSaTrapCntlV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecPolicyAddTrapCntlV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecPolicyDelTrapCntlV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecPolicyAttachTrapCntlV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecPolicyDetachTrapCntlV2"))
)
if mibBuilder.loadTexts:
    hpnicfIPsecTrapCntlGroupV2.setStatus("current")


# Notification objects

hpnicfIPsecTunnelStartV2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 9, 0, 1)
)
hpnicfIPsecTunnelStartV2.setObjects(
      *(("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecTunIndexV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecTunLocalAddrTypeV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecTunLocalAddrV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecTunRemoteAddrTypeV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecTunRemoteAddrV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecTunLifeTimeV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecTunLifeSizeV2"))
)
if mibBuilder.loadTexts:
    hpnicfIPsecTunnelStartV2.setStatus(
        "current"
    )

hpnicfIPsecTunnelStopV2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 9, 0, 2)
)
hpnicfIPsecTunnelStopV2.setObjects(
      *(("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecTunIndexV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecTunLocalAddrTypeV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecTunLocalAddrV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecTunRemoteAddrTypeV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecTunRemoteAddrV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecTunActiveTimeV2"))
)
if mibBuilder.loadTexts:
    hpnicfIPsecTunnelStopV2.setStatus(
        "current"
    )

hpnicfIPsecNoSaFailureV2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 9, 0, 3)
)
hpnicfIPsecNoSaFailureV2.setObjects(
      *(("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecTunIndexV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecTunLocalAddrTypeV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecTunLocalAddrV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecTunRemoteAddrTypeV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecTunRemoteAddrV2"))
)
if mibBuilder.loadTexts:
    hpnicfIPsecNoSaFailureV2.setStatus(
        "current"
    )

hpnicfIPsecAuthFailFailureV2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 9, 0, 4)
)
hpnicfIPsecAuthFailFailureV2.setObjects(
      *(("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecTunIndexV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecTunLocalAddrTypeV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecTunLocalAddrV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecTunRemoteAddrTypeV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecTunRemoteAddrV2"))
)
if mibBuilder.loadTexts:
    hpnicfIPsecAuthFailFailureV2.setStatus(
        "current"
    )

hpnicfIPsecEncryFailFailureV2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 9, 0, 5)
)
hpnicfIPsecEncryFailFailureV2.setObjects(
      *(("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecTunIndexV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecTunLocalAddrTypeV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecTunLocalAddrV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecTunRemoteAddrTypeV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecTunRemoteAddrV2"))
)
if mibBuilder.loadTexts:
    hpnicfIPsecEncryFailFailureV2.setStatus(
        "current"
    )

hpnicfIPsecDecryFailFailureV2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 9, 0, 6)
)
hpnicfIPsecDecryFailFailureV2.setObjects(
      *(("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecTunIndexV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecTunLocalAddrTypeV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecTunLocalAddrV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecTunRemoteAddrTypeV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecTunRemoteAddrV2"))
)
if mibBuilder.loadTexts:
    hpnicfIPsecDecryFailFailureV2.setStatus(
        "current"
    )

hpnicfIPsecInvalidSaFailureV2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 9, 0, 7)
)
hpnicfIPsecInvalidSaFailureV2.setObjects(
      *(("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecTunIndexV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecSaIndexV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecTunLocalAddrTypeV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecTunLocalAddrV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecTunRemoteAddrTypeV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecTunRemoteAddrV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecSaSpiValueV2"))
)
if mibBuilder.loadTexts:
    hpnicfIPsecInvalidSaFailureV2.setStatus(
        "current"
    )

hpnicfIPsecPolicyAddV2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 9, 0, 8)
)
hpnicfIPsecPolicyAddV2.setObjects(
      *(("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecPolicyNameV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecPolicySeqNumV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecPolicySizeV2"))
)
if mibBuilder.loadTexts:
    hpnicfIPsecPolicyAddV2.setStatus(
        "current"
    )

hpnicfIPsecPolicyDelV2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 9, 0, 9)
)
hpnicfIPsecPolicyDelV2.setObjects(
      *(("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecPolicyNameV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecPolicySeqNumV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecPolicySizeV2"))
)
if mibBuilder.loadTexts:
    hpnicfIPsecPolicyDelV2.setStatus(
        "current"
    )

hpnicfIPsecPolicyAttachV2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 9, 0, 10)
)
hpnicfIPsecPolicyAttachV2.setObjects(
      *(("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecPolicyNameV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecPolicySizeV2"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    hpnicfIPsecPolicyAttachV2.setStatus(
        "current"
    )

hpnicfIPsecPolicyDetachV2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 1, 9, 0, 11)
)
hpnicfIPsecPolicyDetachV2.setObjects(
      *(("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecPolicyNameV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecPolicySizeV2"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    hpnicfIPsecPolicyDetachV2.setStatus(
        "current"
    )


# Notifications groups

hpnicfIPsecTrapGroupV2 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 2, 2, 9)
)
hpnicfIPsecTrapGroupV2.setObjects(
      *(("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecTunnelStartV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecTunnelStopV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecNoSaFailureV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecAuthFailFailureV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecEncryFailFailureV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecDecryFailFailureV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecInvalidSaFailureV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecPolicyAddV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecPolicyDelV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecPolicyAttachV2"),
        ("HPN-ICF-IPSEC-MONITOR-V2-MIB", "hpnicfIPsecPolicyDetachV2"))
)
if mibBuilder.loadTexts:
    hpnicfIPsecTrapGroupV2.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hpnicfIPsecComplianceV2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hpnicfIPsecComplianceV2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-IPSEC-MONITOR-V2-MIB",
    **{"HpnicfIPsecDiffHellmanGrpV2": HpnicfIPsecDiffHellmanGrpV2,
       "HpnicfIPsecEncapModeV2": HpnicfIPsecEncapModeV2,
       "HpnicfIPsecEncryptAlgoV2": HpnicfIPsecEncryptAlgoV2,
       "HpnicfIPsecAuthAlgoV2": HpnicfIPsecAuthAlgoV2,
       "HpnicfIPsecSaProtocolV2": HpnicfIPsecSaProtocolV2,
       "HpnicfIPsecIDTypeV2": HpnicfIPsecIDTypeV2,
       "HpnicfIPsecTrafficTypeV2": HpnicfIPsecTrafficTypeV2,
       "HpnicfIPsecNegoTypeV2": HpnicfIPsecNegoTypeV2,
       "HpnicfIPsecTunnelStateV2": HpnicfIPsecTunnelStateV2,
       "hpnicfIPsecMonitorV2": hpnicfIPsecMonitorV2,
       "hpnicfIPsecObjectsV2": hpnicfIPsecObjectsV2,
       "hpnicfIPsecScalarObjectsV2": hpnicfIPsecScalarObjectsV2,
       "hpnicfIPsecMIBVersion": hpnicfIPsecMIBVersion,
       "hpnicfIPsecTunnelV2Table": hpnicfIPsecTunnelV2Table,
       "hpnicfIPsecTunnelV2Entry": hpnicfIPsecTunnelV2Entry,
       "hpnicfIPsecTunIndexV2": hpnicfIPsecTunIndexV2,
       "hpnicfIPsecTunIfIndexV2": hpnicfIPsecTunIfIndexV2,
       "hpnicfIPsecTunIKETunnelIndexV2": hpnicfIPsecTunIKETunnelIndexV2,
       "hpnicfIPsecTunIKETunLocalIDTypeV2": hpnicfIPsecTunIKETunLocalIDTypeV2,
       "hpnicfIPsecTunIKETunLocalIDVal1V2": hpnicfIPsecTunIKETunLocalIDVal1V2,
       "hpnicfIPsecTunIKETunLocalIDVal2V2": hpnicfIPsecTunIKETunLocalIDVal2V2,
       "hpnicfIPsecTunIKETunRemoteIDTypeV2": hpnicfIPsecTunIKETunRemoteIDTypeV2,
       "hpnicfIPsecTunIKETunRemoteIDVal1V2": hpnicfIPsecTunIKETunRemoteIDVal1V2,
       "hpnicfIPsecTunIKETunRemoteIDVal2V2": hpnicfIPsecTunIKETunRemoteIDVal2V2,
       "hpnicfIPsecTunLocalAddrTypeV2": hpnicfIPsecTunLocalAddrTypeV2,
       "hpnicfIPsecTunLocalAddrV2": hpnicfIPsecTunLocalAddrV2,
       "hpnicfIPsecTunRemoteAddrTypeV2": hpnicfIPsecTunRemoteAddrTypeV2,
       "hpnicfIPsecTunRemoteAddrV2": hpnicfIPsecTunRemoteAddrV2,
       "hpnicfIPsecTunKeyTypeV2": hpnicfIPsecTunKeyTypeV2,
       "hpnicfIPsecTunEncapModeV2": hpnicfIPsecTunEncapModeV2,
       "hpnicfIPsecTunInitiatorV2": hpnicfIPsecTunInitiatorV2,
       "hpnicfIPsecTunLifeSizeV2": hpnicfIPsecTunLifeSizeV2,
       "hpnicfIPsecTunLifeTimeV2": hpnicfIPsecTunLifeTimeV2,
       "hpnicfIPsecTunRemainTimeV2": hpnicfIPsecTunRemainTimeV2,
       "hpnicfIPsecTunActiveTimeV2": hpnicfIPsecTunActiveTimeV2,
       "hpnicfIPsecTunRemainSizeV2": hpnicfIPsecTunRemainSizeV2,
       "hpnicfIPsecTunTotalRefreshesV2": hpnicfIPsecTunTotalRefreshesV2,
       "hpnicfIPsecTunCurrentSaInstancesV2": hpnicfIPsecTunCurrentSaInstancesV2,
       "hpnicfIPsecTunInSaEncryptAlgoV2": hpnicfIPsecTunInSaEncryptAlgoV2,
       "hpnicfIPsecTunInSaAhAuthAlgoV2": hpnicfIPsecTunInSaAhAuthAlgoV2,
       "hpnicfIPsecTunInSaEspAuthAlgoV2": hpnicfIPsecTunInSaEspAuthAlgoV2,
       "hpnicfIPsecTunDiffHellmanGrpV2": hpnicfIPsecTunDiffHellmanGrpV2,
       "hpnicfIPsecTunOutSaEncryptAlgoV2": hpnicfIPsecTunOutSaEncryptAlgoV2,
       "hpnicfIPsecTunOutSaAhAuthAlgoV2": hpnicfIPsecTunOutSaAhAuthAlgoV2,
       "hpnicfIPsecTunOutSaEspAuthAlgoV2": hpnicfIPsecTunOutSaEspAuthAlgoV2,
       "hpnicfIPsecTunPolicyNameV2": hpnicfIPsecTunPolicyNameV2,
       "hpnicfIPsecTunPolicyNumV2": hpnicfIPsecTunPolicyNumV2,
       "hpnicfIPsecTunStatusV2": hpnicfIPsecTunStatusV2,
       "hpnicfIPsecTunnelStatV2Table": hpnicfIPsecTunnelStatV2Table,
       "hpnicfIPsecTunnelStatV2Entry": hpnicfIPsecTunnelStatV2Entry,
       "hpnicfIPsecTunInOctetsV2": hpnicfIPsecTunInOctetsV2,
       "hpnicfIPsecTunInDecompOctetsV2": hpnicfIPsecTunInDecompOctetsV2,
       "hpnicfIPsecTunInPktsV2": hpnicfIPsecTunInPktsV2,
       "hpnicfIPsecTunInDropPktsV2": hpnicfIPsecTunInDropPktsV2,
       "hpnicfIPsecTunInReplayDropPktsV2": hpnicfIPsecTunInReplayDropPktsV2,
       "hpnicfIPsecTunInAuthFailsV2": hpnicfIPsecTunInAuthFailsV2,
       "hpnicfIPsecTunInDecryptFailsV2": hpnicfIPsecTunInDecryptFailsV2,
       "hpnicfIPsecTunOutOctetsV2": hpnicfIPsecTunOutOctetsV2,
       "hpnicfIPsecTunOutUncompOctetsV2": hpnicfIPsecTunOutUncompOctetsV2,
       "hpnicfIPsecTunOutPktsV2": hpnicfIPsecTunOutPktsV2,
       "hpnicfIPsecTunOutDropPktsV2": hpnicfIPsecTunOutDropPktsV2,
       "hpnicfIPsecTunOutEncryptFailsV2": hpnicfIPsecTunOutEncryptFailsV2,
       "hpnicfIPsecTunNoMemoryDropPktsV2": hpnicfIPsecTunNoMemoryDropPktsV2,
       "hpnicfIPsecTunQueueFullDropPktsV2": hpnicfIPsecTunQueueFullDropPktsV2,
       "hpnicfIPsecTunInvalidLenDropPktsV2": hpnicfIPsecTunInvalidLenDropPktsV2,
       "hpnicfIPsecTunTooLongDropPktsV2": hpnicfIPsecTunTooLongDropPktsV2,
       "hpnicfIPsecTunInvalidSaDropPktsV2": hpnicfIPsecTunInvalidSaDropPktsV2,
       "hpnicfIPsecSaV2Table": hpnicfIPsecSaV2Table,
       "hpnicfIPsecSaV2Entry": hpnicfIPsecSaV2Entry,
       "hpnicfIPsecSaIndexV2": hpnicfIPsecSaIndexV2,
       "hpnicfIPsecSaDirectionV2": hpnicfIPsecSaDirectionV2,
       "hpnicfIPsecSaSpiValueV2": hpnicfIPsecSaSpiValueV2,
       "hpnicfIPsecSaSecProtocolV2": hpnicfIPsecSaSecProtocolV2,
       "hpnicfIPsecSaEncryptAlgoV2": hpnicfIPsecSaEncryptAlgoV2,
       "hpnicfIPsecSaAuthAlgoV2": hpnicfIPsecSaAuthAlgoV2,
       "hpnicfIPsecSaStatusV2": hpnicfIPsecSaStatusV2,
       "hpnicfIPsecTrafficV2Table": hpnicfIPsecTrafficV2Table,
       "hpnicfIPsecTrafficV2Entry": hpnicfIPsecTrafficV2Entry,
       "hpnicfIPsecTrafficLocalTypeV2": hpnicfIPsecTrafficLocalTypeV2,
       "hpnicfIPsecTrafficLocalAddr1TypeV2": hpnicfIPsecTrafficLocalAddr1TypeV2,
       "hpnicfIPsecTrafficLocalAddr1V2": hpnicfIPsecTrafficLocalAddr1V2,
       "hpnicfIPsecTrafficLocalAddr2TypeV2": hpnicfIPsecTrafficLocalAddr2TypeV2,
       "hpnicfIPsecTrafficLocalAddr2V2": hpnicfIPsecTrafficLocalAddr2V2,
       "hpnicfIPsecTrafficLocalProtocol1V2": hpnicfIPsecTrafficLocalProtocol1V2,
       "hpnicfIPsecTrafficLocalProtocol2V2": hpnicfIPsecTrafficLocalProtocol2V2,
       "hpnicfIPsecTrafficLocalPort1V2": hpnicfIPsecTrafficLocalPort1V2,
       "hpnicfIPsecTrafficLocalPort2V2": hpnicfIPsecTrafficLocalPort2V2,
       "hpnicfIPsecTrafficRemoteTypeV2": hpnicfIPsecTrafficRemoteTypeV2,
       "hpnicfIPsecTrafficRemAddr1TypeV2": hpnicfIPsecTrafficRemAddr1TypeV2,
       "hpnicfIPsecTrafficRemAddr1V2": hpnicfIPsecTrafficRemAddr1V2,
       "hpnicfIPsecTrafficRemAddr2TypeV2": hpnicfIPsecTrafficRemAddr2TypeV2,
       "hpnicfIPsecTrafficRemAddr2V2": hpnicfIPsecTrafficRemAddr2V2,
       "hpnicfIPsecTrafficRemoPro1V2": hpnicfIPsecTrafficRemoPro1V2,
       "hpnicfIPsecTrafficRemoPro2V2": hpnicfIPsecTrafficRemoPro2V2,
       "hpnicfIPsecTrafficRemPort1V2": hpnicfIPsecTrafficRemPort1V2,
       "hpnicfIPsecTrafficRemPort2V2": hpnicfIPsecTrafficRemPort2V2,
       "hpnicfIPsecGlobalStatsV2": hpnicfIPsecGlobalStatsV2,
       "hpnicfIPsecGlobalActiveTunnelsV2": hpnicfIPsecGlobalActiveTunnelsV2,
       "hpnicfIPsecGlobalActiveSasV2": hpnicfIPsecGlobalActiveSasV2,
       "hpnicfIPsecGlobalInOctetsV2": hpnicfIPsecGlobalInOctetsV2,
       "hpnicfIPsecGlobalInDecompOctetsV2": hpnicfIPsecGlobalInDecompOctetsV2,
       "hpnicfIPsecGlobalInPktsV2": hpnicfIPsecGlobalInPktsV2,
       "hpnicfIPsecGlobalInDropsV2": hpnicfIPsecGlobalInDropsV2,
       "hpnicfIPsecGlobalInReplayDropsV2": hpnicfIPsecGlobalInReplayDropsV2,
       "hpnicfIPsecGlobalInAuthFailsV2": hpnicfIPsecGlobalInAuthFailsV2,
       "hpnicfIPsecGlobalInDecryptFailsV2": hpnicfIPsecGlobalInDecryptFailsV2,
       "hpnicfIPsecGlobalOutOctetsV2": hpnicfIPsecGlobalOutOctetsV2,
       "hpnicfIPsecGlobalOutUncompOctetsV2": hpnicfIPsecGlobalOutUncompOctetsV2,
       "hpnicfIPsecGlobalOutPktsV2": hpnicfIPsecGlobalOutPktsV2,
       "hpnicfIPsecGlobalOutDropsV2": hpnicfIPsecGlobalOutDropsV2,
       "hpnicfIPsecGlobalOutEncryptFailsV2": hpnicfIPsecGlobalOutEncryptFailsV2,
       "hpnicfIPsecGlobalNoMemoryDropsV2": hpnicfIPsecGlobalNoMemoryDropsV2,
       "hpnicfIPsecGlobalNoFindSaDropsV2": hpnicfIPsecGlobalNoFindSaDropsV2,
       "hpnicfIPsecGlobalQueueFullDropsV2": hpnicfIPsecGlobalQueueFullDropsV2,
       "hpnicfIPsecGlobalInvalidLenDropsV2": hpnicfIPsecGlobalInvalidLenDropsV2,
       "hpnicfIPsecGlobalTooLongDropsV2": hpnicfIPsecGlobalTooLongDropsV2,
       "hpnicfIPsecGlobalInvalidSaDropsV2": hpnicfIPsecGlobalInvalidSaDropsV2,
       "hpnicfIPsecTrapObjectV2": hpnicfIPsecTrapObjectV2,
       "hpnicfIPsecPolicyNameV2": hpnicfIPsecPolicyNameV2,
       "hpnicfIPsecPolicySeqNumV2": hpnicfIPsecPolicySeqNumV2,
       "hpnicfIPsecPolicySizeV2": hpnicfIPsecPolicySizeV2,
       "hpnicfIPsecTrapCntlV2": hpnicfIPsecTrapCntlV2,
       "hpnicfIPsecTrapGlobalCntlV2": hpnicfIPsecTrapGlobalCntlV2,
       "hpnicfIPsecTunnelStartTrapCntlV2": hpnicfIPsecTunnelStartTrapCntlV2,
       "hpnicfIPsecTunnelStopTrapCntlV2": hpnicfIPsecTunnelStopTrapCntlV2,
       "hpnicfIPsecNoSaTrapCntlV2": hpnicfIPsecNoSaTrapCntlV2,
       "hpnicfIPsecAuthFailureTrapCntlV2": hpnicfIPsecAuthFailureTrapCntlV2,
       "hpnicfIPsecEncryFailureTrapCntlV2": hpnicfIPsecEncryFailureTrapCntlV2,
       "hpnicfIPsecDecryFailureTrapCntlV2": hpnicfIPsecDecryFailureTrapCntlV2,
       "hpnicfIPsecInvalidSaTrapCntlV2": hpnicfIPsecInvalidSaTrapCntlV2,
       "hpnicfIPsecPolicyAddTrapCntlV2": hpnicfIPsecPolicyAddTrapCntlV2,
       "hpnicfIPsecPolicyDelTrapCntlV2": hpnicfIPsecPolicyDelTrapCntlV2,
       "hpnicfIPsecPolicyAttachTrapCntlV2": hpnicfIPsecPolicyAttachTrapCntlV2,
       "hpnicfIPsecPolicyDetachTrapCntlV2": hpnicfIPsecPolicyDetachTrapCntlV2,
       "hpnicfIPsecTrapV2": hpnicfIPsecTrapV2,
       "hpnicfIPsecNotificationsV2": hpnicfIPsecNotificationsV2,
       "hpnicfIPsecTunnelStartV2": hpnicfIPsecTunnelStartV2,
       "hpnicfIPsecTunnelStopV2": hpnicfIPsecTunnelStopV2,
       "hpnicfIPsecNoSaFailureV2": hpnicfIPsecNoSaFailureV2,
       "hpnicfIPsecAuthFailFailureV2": hpnicfIPsecAuthFailFailureV2,
       "hpnicfIPsecEncryFailFailureV2": hpnicfIPsecEncryFailFailureV2,
       "hpnicfIPsecDecryFailFailureV2": hpnicfIPsecDecryFailFailureV2,
       "hpnicfIPsecInvalidSaFailureV2": hpnicfIPsecInvalidSaFailureV2,
       "hpnicfIPsecPolicyAddV2": hpnicfIPsecPolicyAddV2,
       "hpnicfIPsecPolicyDelV2": hpnicfIPsecPolicyDelV2,
       "hpnicfIPsecPolicyAttachV2": hpnicfIPsecPolicyAttachV2,
       "hpnicfIPsecPolicyDetachV2": hpnicfIPsecPolicyDetachV2,
       "hpnicfIPsecConformanceV2": hpnicfIPsecConformanceV2,
       "hpnicfIPsecCompliancesV2": hpnicfIPsecCompliancesV2,
       "hpnicfIPsecComplianceV2": hpnicfIPsecComplianceV2,
       "hpnicfIPsecGroupsV2": hpnicfIPsecGroupsV2,
       "hpnicfIPsecScalarObjectsGroupV2": hpnicfIPsecScalarObjectsGroupV2,
       "hpnicfIPsecTunnelTableGroupV2": hpnicfIPsecTunnelTableGroupV2,
       "hpnicfIPsecTunnelStatGroupV2": hpnicfIPsecTunnelStatGroupV2,
       "hpnicfIPsecSaGroupV2": hpnicfIPsecSaGroupV2,
       "hpnicfIPsecTrafficTableGroupV2": hpnicfIPsecTrafficTableGroupV2,
       "hpnicfIPsecGlobalStatsGroupV2": hpnicfIPsecGlobalStatsGroupV2,
       "hpnicfIPsecTrapObjectGroupV2": hpnicfIPsecTrapObjectGroupV2,
       "hpnicfIPsecTrapCntlGroupV2": hpnicfIPsecTrapCntlGroupV2,
       "hpnicfIPsecTrapGroupV2": hpnicfIPsecTrapGroupV2}
)
