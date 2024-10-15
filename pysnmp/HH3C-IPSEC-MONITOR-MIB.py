# SNMP MIB module (HH3C-IPSEC-MONITOR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-IPSEC-MONITOR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:53:38 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

hh3cIPSecMonitor = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Hh3cDiffHellmanGrp(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              5,
              14,
              2147483647)
        )
    )
    namedValues = NamedValues(
        *(("invalidGroup", 2147483647),
          ("modp1024", 2),
          ("modp1536", 5),
          ("modp2048", 14),
          ("modp768", 1),
          ("none", 0))
    )



class Hh3cEncapMode(Integer32, TextualConvention):
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



class Hh3cEncryptAlgo(Integer32, TextualConvention):
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
              2147483647)
        )
    )
    namedValues = NamedValues(
        *(("aesCbc", 7),
          ("aesCbc128", 9),
          ("aesCbc192", 10),
          ("aesCbc256", 11),
          ("blowfishCbc", 3),
          ("castCbc", 6),
          ("desCbc", 1),
          ("ideaCbc", 2),
          ("invalidAlg", 2147483647),
          ("none", 0),
          ("nsaCbc", 8),
          ("rc5R16B64Cbc", 4),
          ("tripledesCbc", 5))
    )



class Hh3cAuthAlgo(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              2147483647)
        )
    )
    namedValues = NamedValues(
        *(("invalidAlg", 2147483647),
          ("md5", 1),
          ("none", 0),
          ("sha", 2))
    )



class Hh3cSaProtocol(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("ah", 2),
          ("esp", 3),
          ("ipcomp", 4),
          ("isakmp", 1),
          ("reserved", 0))
    )



class Hh3cTrapStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )



class Hh3cIPSecIDType(Integer32, TextualConvention):
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



class Hh3cTrafficType(Integer32, TextualConvention):
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



class Hh3cIPSecNegoType(Integer32, TextualConvention):
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



class Hh3cIPSecTunnelState(Integer32, TextualConvention):
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

_Hh3cIPSecObjects_ObjectIdentity = ObjectIdentity
hh3cIPSecObjects = _Hh3cIPSecObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 1)
)
_Hh3cIPSecTunnelTable_Object = MibTable
hh3cIPSecTunnelTable = _Hh3cIPSecTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cIPSecTunnelTable.setStatus("current")
_Hh3cIPSecTunnelEntry_Object = MibTableRow
hh3cIPSecTunnelEntry = _Hh3cIPSecTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 1, 1, 1)
)
hh3cIPSecTunnelEntry.setIndexNames(
    (0, "HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecTunIfIndex"),
    (0, "HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecTunEntryIndex"),
    (0, "HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecTunIndex"),
)
if mibBuilder.loadTexts:
    hh3cIPSecTunnelEntry.setStatus("current")


class _Hh3cIPSecTunIfIndex_Type(Integer32):
    """Custom type hh3cIPSecTunIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cIPSecTunIfIndex_Type.__name__ = "Integer32"
_Hh3cIPSecTunIfIndex_Object = MibTableColumn
hh3cIPSecTunIfIndex = _Hh3cIPSecTunIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 1, 1, 1, 1),
    _Hh3cIPSecTunIfIndex_Type()
)
hh3cIPSecTunIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cIPSecTunIfIndex.setStatus("current")


class _Hh3cIPSecTunEntryIndex_Type(Integer32):
    """Custom type hh3cIPSecTunEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cIPSecTunEntryIndex_Type.__name__ = "Integer32"
_Hh3cIPSecTunEntryIndex_Object = MibTableColumn
hh3cIPSecTunEntryIndex = _Hh3cIPSecTunEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 1, 1, 1, 2),
    _Hh3cIPSecTunEntryIndex_Type()
)
hh3cIPSecTunEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cIPSecTunEntryIndex.setStatus("current")


class _Hh3cIPSecTunIndex_Type(Integer32):
    """Custom type hh3cIPSecTunIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cIPSecTunIndex_Type.__name__ = "Integer32"
_Hh3cIPSecTunIndex_Object = MibTableColumn
hh3cIPSecTunIndex = _Hh3cIPSecTunIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 1, 1, 1, 3),
    _Hh3cIPSecTunIndex_Type()
)
hh3cIPSecTunIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cIPSecTunIndex.setStatus("current")


class _Hh3cIPSecTunIKETunnelIndex_Type(Integer32):
    """Custom type hh3cIPSecTunIKETunnelIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cIPSecTunIKETunnelIndex_Type.__name__ = "Integer32"
_Hh3cIPSecTunIKETunnelIndex_Object = MibTableColumn
hh3cIPSecTunIKETunnelIndex = _Hh3cIPSecTunIKETunnelIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 1, 1, 1, 4),
    _Hh3cIPSecTunIKETunnelIndex_Type()
)
hh3cIPSecTunIKETunnelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPSecTunIKETunnelIndex.setStatus("current")
_Hh3cIPSecTunLocalAddr_Type = IpAddress
_Hh3cIPSecTunLocalAddr_Object = MibTableColumn
hh3cIPSecTunLocalAddr = _Hh3cIPSecTunLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 1, 1, 1, 5),
    _Hh3cIPSecTunLocalAddr_Type()
)
hh3cIPSecTunLocalAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPSecTunLocalAddr.setStatus("current")
_Hh3cIPSecTunRemoteAddr_Type = IpAddress
_Hh3cIPSecTunRemoteAddr_Object = MibTableColumn
hh3cIPSecTunRemoteAddr = _Hh3cIPSecTunRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 1, 1, 1, 6),
    _Hh3cIPSecTunRemoteAddr_Type()
)
hh3cIPSecTunRemoteAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPSecTunRemoteAddr.setStatus("current")
_Hh3cIPSecTunKeyType_Type = Hh3cIPSecNegoType
_Hh3cIPSecTunKeyType_Object = MibTableColumn
hh3cIPSecTunKeyType = _Hh3cIPSecTunKeyType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 1, 1, 1, 7),
    _Hh3cIPSecTunKeyType_Type()
)
hh3cIPSecTunKeyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPSecTunKeyType.setStatus("current")
_Hh3cIPSecTunEncapMode_Type = Hh3cEncapMode
_Hh3cIPSecTunEncapMode_Object = MibTableColumn
hh3cIPSecTunEncapMode = _Hh3cIPSecTunEncapMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 1, 1, 1, 8),
    _Hh3cIPSecTunEncapMode_Type()
)
hh3cIPSecTunEncapMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPSecTunEncapMode.setStatus("current")


class _Hh3cIPSecTunInitiator_Type(Integer32):
    """Custom type hh3cIPSecTunInitiator based on Integer32"""
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


_Hh3cIPSecTunInitiator_Type.__name__ = "Integer32"
_Hh3cIPSecTunInitiator_Object = MibTableColumn
hh3cIPSecTunInitiator = _Hh3cIPSecTunInitiator_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 1, 1, 1, 9),
    _Hh3cIPSecTunInitiator_Type()
)
hh3cIPSecTunInitiator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPSecTunInitiator.setStatus("current")
_Hh3cIPSecTunLifeSize_Type = Gauge32
_Hh3cIPSecTunLifeSize_Object = MibTableColumn
hh3cIPSecTunLifeSize = _Hh3cIPSecTunLifeSize_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 1, 1, 1, 10),
    _Hh3cIPSecTunLifeSize_Type()
)
hh3cIPSecTunLifeSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPSecTunLifeSize.setStatus("current")


class _Hh3cIPSecTunLifeTime_Type(Integer32):
    """Custom type hh3cIPSecTunLifeTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cIPSecTunLifeTime_Type.__name__ = "Integer32"
_Hh3cIPSecTunLifeTime_Object = MibTableColumn
hh3cIPSecTunLifeTime = _Hh3cIPSecTunLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 1, 1, 1, 11),
    _Hh3cIPSecTunLifeTime_Type()
)
hh3cIPSecTunLifeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPSecTunLifeTime.setStatus("current")


class _Hh3cIPSecTunRemainTime_Type(Integer32):
    """Custom type hh3cIPSecTunRemainTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hh3cIPSecTunRemainTime_Type.__name__ = "Integer32"
_Hh3cIPSecTunRemainTime_Object = MibTableColumn
hh3cIPSecTunRemainTime = _Hh3cIPSecTunRemainTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 1, 1, 1, 12),
    _Hh3cIPSecTunRemainTime_Type()
)
hh3cIPSecTunRemainTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPSecTunRemainTime.setStatus("current")


class _Hh3cIPSecTunActiveTime_Type(Integer32):
    """Custom type hh3cIPSecTunActiveTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hh3cIPSecTunActiveTime_Type.__name__ = "Integer32"
_Hh3cIPSecTunActiveTime_Object = MibTableColumn
hh3cIPSecTunActiveTime = _Hh3cIPSecTunActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 1, 1, 1, 13),
    _Hh3cIPSecTunActiveTime_Type()
)
hh3cIPSecTunActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPSecTunActiveTime.setStatus("current")
_Hh3cIPSecTunRemainSize_Type = Gauge32
_Hh3cIPSecTunRemainSize_Object = MibTableColumn
hh3cIPSecTunRemainSize = _Hh3cIPSecTunRemainSize_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 1, 1, 1, 14),
    _Hh3cIPSecTunRemainSize_Type()
)
hh3cIPSecTunRemainSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPSecTunRemainSize.setStatus("current")
_Hh3cIPSecTunTotalRefreshes_Type = Counter32
_Hh3cIPSecTunTotalRefreshes_Object = MibTableColumn
hh3cIPSecTunTotalRefreshes = _Hh3cIPSecTunTotalRefreshes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 1, 1, 1, 15),
    _Hh3cIPSecTunTotalRefreshes_Type()
)
hh3cIPSecTunTotalRefreshes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPSecTunTotalRefreshes.setStatus("current")
_Hh3cIPSecTunCurrentSaInstances_Type = Gauge32
_Hh3cIPSecTunCurrentSaInstances_Object = MibTableColumn
hh3cIPSecTunCurrentSaInstances = _Hh3cIPSecTunCurrentSaInstances_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 1, 1, 1, 16),
    _Hh3cIPSecTunCurrentSaInstances_Type()
)
hh3cIPSecTunCurrentSaInstances.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPSecTunCurrentSaInstances.setStatus("current")
_Hh3cIPSecTunInSaEncryptAlgo_Type = Hh3cEncryptAlgo
_Hh3cIPSecTunInSaEncryptAlgo_Object = MibTableColumn
hh3cIPSecTunInSaEncryptAlgo = _Hh3cIPSecTunInSaEncryptAlgo_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 1, 1, 1, 17),
    _Hh3cIPSecTunInSaEncryptAlgo_Type()
)
hh3cIPSecTunInSaEncryptAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPSecTunInSaEncryptAlgo.setStatus("current")
_Hh3cIPSecTunInSaAhAuthAlgo_Type = Hh3cAuthAlgo
_Hh3cIPSecTunInSaAhAuthAlgo_Object = MibTableColumn
hh3cIPSecTunInSaAhAuthAlgo = _Hh3cIPSecTunInSaAhAuthAlgo_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 1, 1, 1, 18),
    _Hh3cIPSecTunInSaAhAuthAlgo_Type()
)
hh3cIPSecTunInSaAhAuthAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPSecTunInSaAhAuthAlgo.setStatus("current")
_Hh3cIPSecTunInSaEspAuthAlgo_Type = Hh3cAuthAlgo
_Hh3cIPSecTunInSaEspAuthAlgo_Object = MibTableColumn
hh3cIPSecTunInSaEspAuthAlgo = _Hh3cIPSecTunInSaEspAuthAlgo_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 1, 1, 1, 19),
    _Hh3cIPSecTunInSaEspAuthAlgo_Type()
)
hh3cIPSecTunInSaEspAuthAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPSecTunInSaEspAuthAlgo.setStatus("current")
_Hh3cIPSecTunDiffHellmanGrp_Type = Hh3cDiffHellmanGrp
_Hh3cIPSecTunDiffHellmanGrp_Object = MibTableColumn
hh3cIPSecTunDiffHellmanGrp = _Hh3cIPSecTunDiffHellmanGrp_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 1, 1, 1, 20),
    _Hh3cIPSecTunDiffHellmanGrp_Type()
)
hh3cIPSecTunDiffHellmanGrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPSecTunDiffHellmanGrp.setStatus("current")
_Hh3cIPSecTunOutSaEncryptAlgo_Type = Hh3cEncryptAlgo
_Hh3cIPSecTunOutSaEncryptAlgo_Object = MibTableColumn
hh3cIPSecTunOutSaEncryptAlgo = _Hh3cIPSecTunOutSaEncryptAlgo_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 1, 1, 1, 21),
    _Hh3cIPSecTunOutSaEncryptAlgo_Type()
)
hh3cIPSecTunOutSaEncryptAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPSecTunOutSaEncryptAlgo.setStatus("current")
_Hh3cIPSecTunOutSaAhAuthAlgo_Type = Hh3cAuthAlgo
_Hh3cIPSecTunOutSaAhAuthAlgo_Object = MibTableColumn
hh3cIPSecTunOutSaAhAuthAlgo = _Hh3cIPSecTunOutSaAhAuthAlgo_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 1, 1, 1, 22),
    _Hh3cIPSecTunOutSaAhAuthAlgo_Type()
)
hh3cIPSecTunOutSaAhAuthAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPSecTunOutSaAhAuthAlgo.setStatus("current")
_Hh3cIPSecTunOutSaEspAuthAlgo_Type = Hh3cAuthAlgo
_Hh3cIPSecTunOutSaEspAuthAlgo_Object = MibTableColumn
hh3cIPSecTunOutSaEspAuthAlgo = _Hh3cIPSecTunOutSaEspAuthAlgo_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 1, 1, 1, 23),
    _Hh3cIPSecTunOutSaEspAuthAlgo_Type()
)
hh3cIPSecTunOutSaEspAuthAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPSecTunOutSaEspAuthAlgo.setStatus("current")
_Hh3cIPSecTunPolicyName_Type = DisplayString
_Hh3cIPSecTunPolicyName_Object = MibTableColumn
hh3cIPSecTunPolicyName = _Hh3cIPSecTunPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 1, 1, 1, 24),
    _Hh3cIPSecTunPolicyName_Type()
)
hh3cIPSecTunPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPSecTunPolicyName.setStatus("current")


class _Hh3cIPSecTunPolicyNum_Type(Integer32):
    """Custom type hh3cIPSecTunPolicyNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cIPSecTunPolicyNum_Type.__name__ = "Integer32"
_Hh3cIPSecTunPolicyNum_Object = MibTableColumn
hh3cIPSecTunPolicyNum = _Hh3cIPSecTunPolicyNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 1, 1, 1, 25),
    _Hh3cIPSecTunPolicyNum_Type()
)
hh3cIPSecTunPolicyNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPSecTunPolicyNum.setStatus("current")


class _Hh3cIPSecTunStatus_Type(Integer32):
    """Custom type hh3cIPSecTunStatus based on Integer32"""
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


_Hh3cIPSecTunStatus_Type.__name__ = "Integer32"
_Hh3cIPSecTunStatus_Object = MibTableColumn
hh3cIPSecTunStatus = _Hh3cIPSecTunStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 1, 1, 1, 26),
    _Hh3cIPSecTunStatus_Type()
)
hh3cIPSecTunStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPSecTunStatus.setStatus("current")
_Hh3cIPSecTunnelStatTable_Object = MibTable
hh3cIPSecTunnelStatTable = _Hh3cIPSecTunnelStatTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 1, 2)
)
if mibBuilder.loadTexts:
    hh3cIPSecTunnelStatTable.setStatus("current")
_Hh3cIPSecTunnelStatEntry_Object = MibTableRow
hh3cIPSecTunnelStatEntry = _Hh3cIPSecTunnelStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 1, 2, 1)
)
hh3cIPSecTunnelStatEntry.setIndexNames(
    (0, "HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecTunIfIndex"),
    (0, "HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecTunEntryIndex"),
    (0, "HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecTunIndex"),
)
if mibBuilder.loadTexts:
    hh3cIPSecTunnelStatEntry.setStatus("current")
_Hh3cIPSecTunInOctets_Type = Counter64
_Hh3cIPSecTunInOctets_Object = MibTableColumn
hh3cIPSecTunInOctets = _Hh3cIPSecTunInOctets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 1, 2, 1, 1),
    _Hh3cIPSecTunInOctets_Type()
)
hh3cIPSecTunInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPSecTunInOctets.setStatus("current")
_Hh3cIPSecTunInDecompOctets_Type = Counter64
_Hh3cIPSecTunInDecompOctets_Object = MibTableColumn
hh3cIPSecTunInDecompOctets = _Hh3cIPSecTunInDecompOctets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 1, 2, 1, 2),
    _Hh3cIPSecTunInDecompOctets_Type()
)
hh3cIPSecTunInDecompOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPSecTunInDecompOctets.setStatus("current")
_Hh3cIPSecTunInPkts_Type = Counter64
_Hh3cIPSecTunInPkts_Object = MibTableColumn
hh3cIPSecTunInPkts = _Hh3cIPSecTunInPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 1, 2, 1, 3),
    _Hh3cIPSecTunInPkts_Type()
)
hh3cIPSecTunInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPSecTunInPkts.setStatus("current")
_Hh3cIPSecTunInDropPkts_Type = Counter64
_Hh3cIPSecTunInDropPkts_Object = MibTableColumn
hh3cIPSecTunInDropPkts = _Hh3cIPSecTunInDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 1, 2, 1, 4),
    _Hh3cIPSecTunInDropPkts_Type()
)
hh3cIPSecTunInDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPSecTunInDropPkts.setStatus("current")
_Hh3cIPSecTunInReplayDropPkts_Type = Counter32
_Hh3cIPSecTunInReplayDropPkts_Object = MibTableColumn
hh3cIPSecTunInReplayDropPkts = _Hh3cIPSecTunInReplayDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 1, 2, 1, 5),
    _Hh3cIPSecTunInReplayDropPkts_Type()
)
hh3cIPSecTunInReplayDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPSecTunInReplayDropPkts.setStatus("current")
_Hh3cIPSecTunInAuthFails_Type = Counter32
_Hh3cIPSecTunInAuthFails_Object = MibTableColumn
hh3cIPSecTunInAuthFails = _Hh3cIPSecTunInAuthFails_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 1, 2, 1, 6),
    _Hh3cIPSecTunInAuthFails_Type()
)
hh3cIPSecTunInAuthFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPSecTunInAuthFails.setStatus("current")
_Hh3cIPSecTunInDecryptFails_Type = Counter32
_Hh3cIPSecTunInDecryptFails_Object = MibTableColumn
hh3cIPSecTunInDecryptFails = _Hh3cIPSecTunInDecryptFails_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 1, 2, 1, 7),
    _Hh3cIPSecTunInDecryptFails_Type()
)
hh3cIPSecTunInDecryptFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPSecTunInDecryptFails.setStatus("current")
_Hh3cIPSecTunOutOctets_Type = Counter64
_Hh3cIPSecTunOutOctets_Object = MibTableColumn
hh3cIPSecTunOutOctets = _Hh3cIPSecTunOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 1, 2, 1, 8),
    _Hh3cIPSecTunOutOctets_Type()
)
hh3cIPSecTunOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPSecTunOutOctets.setStatus("current")
_Hh3cIPSecTunOutUncompOctets_Type = Counter64
_Hh3cIPSecTunOutUncompOctets_Object = MibTableColumn
hh3cIPSecTunOutUncompOctets = _Hh3cIPSecTunOutUncompOctets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 1, 2, 1, 9),
    _Hh3cIPSecTunOutUncompOctets_Type()
)
hh3cIPSecTunOutUncompOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPSecTunOutUncompOctets.setStatus("current")
_Hh3cIPSecTunOutPkts_Type = Counter64
_Hh3cIPSecTunOutPkts_Object = MibTableColumn
hh3cIPSecTunOutPkts = _Hh3cIPSecTunOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 1, 2, 1, 10),
    _Hh3cIPSecTunOutPkts_Type()
)
hh3cIPSecTunOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPSecTunOutPkts.setStatus("current")
_Hh3cIPSecTunOutDropPkts_Type = Counter64
_Hh3cIPSecTunOutDropPkts_Object = MibTableColumn
hh3cIPSecTunOutDropPkts = _Hh3cIPSecTunOutDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 1, 2, 1, 11),
    _Hh3cIPSecTunOutDropPkts_Type()
)
hh3cIPSecTunOutDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPSecTunOutDropPkts.setStatus("current")
_Hh3cIPSecTunOutEncryptFails_Type = Counter32
_Hh3cIPSecTunOutEncryptFails_Object = MibTableColumn
hh3cIPSecTunOutEncryptFails = _Hh3cIPSecTunOutEncryptFails_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 1, 2, 1, 12),
    _Hh3cIPSecTunOutEncryptFails_Type()
)
hh3cIPSecTunOutEncryptFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPSecTunOutEncryptFails.setStatus("current")
_Hh3cIPSecTunNoMemoryDropPkts_Type = Counter32
_Hh3cIPSecTunNoMemoryDropPkts_Object = MibTableColumn
hh3cIPSecTunNoMemoryDropPkts = _Hh3cIPSecTunNoMemoryDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 1, 2, 1, 13),
    _Hh3cIPSecTunNoMemoryDropPkts_Type()
)
hh3cIPSecTunNoMemoryDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPSecTunNoMemoryDropPkts.setStatus("current")
_Hh3cIPSecTunQueueFullDropPkts_Type = Counter32
_Hh3cIPSecTunQueueFullDropPkts_Object = MibTableColumn
hh3cIPSecTunQueueFullDropPkts = _Hh3cIPSecTunQueueFullDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 1, 2, 1, 14),
    _Hh3cIPSecTunQueueFullDropPkts_Type()
)
hh3cIPSecTunQueueFullDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPSecTunQueueFullDropPkts.setStatus("current")
_Hh3cIPSecTunInvalidLenDropPkts_Type = Counter32
_Hh3cIPSecTunInvalidLenDropPkts_Object = MibTableColumn
hh3cIPSecTunInvalidLenDropPkts = _Hh3cIPSecTunInvalidLenDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 1, 2, 1, 15),
    _Hh3cIPSecTunInvalidLenDropPkts_Type()
)
hh3cIPSecTunInvalidLenDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPSecTunInvalidLenDropPkts.setStatus("current")
_Hh3cIPSecTunTooLongDropPkts_Type = Counter32
_Hh3cIPSecTunTooLongDropPkts_Object = MibTableColumn
hh3cIPSecTunTooLongDropPkts = _Hh3cIPSecTunTooLongDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 1, 2, 1, 16),
    _Hh3cIPSecTunTooLongDropPkts_Type()
)
hh3cIPSecTunTooLongDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPSecTunTooLongDropPkts.setStatus("current")
_Hh3cIPSecTunInvalidSaDropPkts_Type = Counter32
_Hh3cIPSecTunInvalidSaDropPkts_Object = MibTableColumn
hh3cIPSecTunInvalidSaDropPkts = _Hh3cIPSecTunInvalidSaDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 1, 2, 1, 17),
    _Hh3cIPSecTunInvalidSaDropPkts_Type()
)
hh3cIPSecTunInvalidSaDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPSecTunInvalidSaDropPkts.setStatus("current")
_Hh3cIPSecSaTable_Object = MibTable
hh3cIPSecSaTable = _Hh3cIPSecSaTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 1, 3)
)
if mibBuilder.loadTexts:
    hh3cIPSecSaTable.setStatus("current")
_Hh3cIPSecSaEntry_Object = MibTableRow
hh3cIPSecSaEntry = _Hh3cIPSecSaEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 1, 3, 1)
)
hh3cIPSecSaEntry.setIndexNames(
    (0, "HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecTunIfIndex"),
    (0, "HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecTunEntryIndex"),
    (0, "HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecTunIndex"),
    (0, "HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecSaIndex"),
)
if mibBuilder.loadTexts:
    hh3cIPSecSaEntry.setStatus("current")


class _Hh3cIPSecSaIndex_Type(Integer32):
    """Custom type hh3cIPSecSaIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cIPSecSaIndex_Type.__name__ = "Integer32"
_Hh3cIPSecSaIndex_Object = MibTableColumn
hh3cIPSecSaIndex = _Hh3cIPSecSaIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 1, 3, 1, 1),
    _Hh3cIPSecSaIndex_Type()
)
hh3cIPSecSaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cIPSecSaIndex.setStatus("current")


class _Hh3cIPSecSaDirection_Type(Integer32):
    """Custom type hh3cIPSecSaDirection based on Integer32"""
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


_Hh3cIPSecSaDirection_Type.__name__ = "Integer32"
_Hh3cIPSecSaDirection_Object = MibTableColumn
hh3cIPSecSaDirection = _Hh3cIPSecSaDirection_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 1, 3, 1, 2),
    _Hh3cIPSecSaDirection_Type()
)
hh3cIPSecSaDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPSecSaDirection.setStatus("current")


class _Hh3cIPSecSaValue_Type(Unsigned32):
    """Custom type hh3cIPSecSaValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Hh3cIPSecSaValue_Type.__name__ = "Unsigned32"
_Hh3cIPSecSaValue_Object = MibTableColumn
hh3cIPSecSaValue = _Hh3cIPSecSaValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 1, 3, 1, 3),
    _Hh3cIPSecSaValue_Type()
)
hh3cIPSecSaValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPSecSaValue.setStatus("current")
_Hh3cIPSecSaProtocol_Type = Hh3cSaProtocol
_Hh3cIPSecSaProtocol_Object = MibTableColumn
hh3cIPSecSaProtocol = _Hh3cIPSecSaProtocol_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 1, 3, 1, 4),
    _Hh3cIPSecSaProtocol_Type()
)
hh3cIPSecSaProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPSecSaProtocol.setStatus("current")
_Hh3cIPSecSaEncryptAlgo_Type = Hh3cEncryptAlgo
_Hh3cIPSecSaEncryptAlgo_Object = MibTableColumn
hh3cIPSecSaEncryptAlgo = _Hh3cIPSecSaEncryptAlgo_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 1, 3, 1, 5),
    _Hh3cIPSecSaEncryptAlgo_Type()
)
hh3cIPSecSaEncryptAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPSecSaEncryptAlgo.setStatus("current")
_Hh3cIPSecSaAuthAlgo_Type = Hh3cAuthAlgo
_Hh3cIPSecSaAuthAlgo_Object = MibTableColumn
hh3cIPSecSaAuthAlgo = _Hh3cIPSecSaAuthAlgo_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 1, 3, 1, 6),
    _Hh3cIPSecSaAuthAlgo_Type()
)
hh3cIPSecSaAuthAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPSecSaAuthAlgo.setStatus("current")


class _Hh3cIPSecSaStatus_Type(Integer32):
    """Custom type hh3cIPSecSaStatus based on Integer32"""
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


_Hh3cIPSecSaStatus_Type.__name__ = "Integer32"
_Hh3cIPSecSaStatus_Object = MibTableColumn
hh3cIPSecSaStatus = _Hh3cIPSecSaStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 1, 3, 1, 7),
    _Hh3cIPSecSaStatus_Type()
)
hh3cIPSecSaStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPSecSaStatus.setStatus("current")
_Hh3cIPSecTrafficTable_Object = MibTable
hh3cIPSecTrafficTable = _Hh3cIPSecTrafficTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 1, 4)
)
if mibBuilder.loadTexts:
    hh3cIPSecTrafficTable.setStatus("current")
_Hh3cIPSecTrafficEntry_Object = MibTableRow
hh3cIPSecTrafficEntry = _Hh3cIPSecTrafficEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 1, 4, 1)
)
hh3cIPSecTrafficEntry.setIndexNames(
    (0, "HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecTunIfIndex"),
    (0, "HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecTunEntryIndex"),
    (0, "HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecTunIndex"),
)
if mibBuilder.loadTexts:
    hh3cIPSecTrafficEntry.setStatus("current")
_Hh3cIPSecTrafficLocalType_Type = Hh3cTrafficType
_Hh3cIPSecTrafficLocalType_Object = MibTableColumn
hh3cIPSecTrafficLocalType = _Hh3cIPSecTrafficLocalType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 1, 4, 1, 1),
    _Hh3cIPSecTrafficLocalType_Type()
)
hh3cIPSecTrafficLocalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPSecTrafficLocalType.setStatus("current")
_Hh3cIPSecTrafficLocalAddr1_Type = IpAddress
_Hh3cIPSecTrafficLocalAddr1_Object = MibTableColumn
hh3cIPSecTrafficLocalAddr1 = _Hh3cIPSecTrafficLocalAddr1_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 1, 4, 1, 2),
    _Hh3cIPSecTrafficLocalAddr1_Type()
)
hh3cIPSecTrafficLocalAddr1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPSecTrafficLocalAddr1.setStatus("current")
_Hh3cIPSecTrafficLocalAddr2_Type = IpAddress
_Hh3cIPSecTrafficLocalAddr2_Object = MibTableColumn
hh3cIPSecTrafficLocalAddr2 = _Hh3cIPSecTrafficLocalAddr2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 1, 4, 1, 3),
    _Hh3cIPSecTrafficLocalAddr2_Type()
)
hh3cIPSecTrafficLocalAddr2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPSecTrafficLocalAddr2.setStatus("current")


class _Hh3cIPSecTrafficLocalProtocol_Type(Integer32):
    """Custom type hh3cIPSecTrafficLocalProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Hh3cIPSecTrafficLocalProtocol_Type.__name__ = "Integer32"
_Hh3cIPSecTrafficLocalProtocol_Object = MibTableColumn
hh3cIPSecTrafficLocalProtocol = _Hh3cIPSecTrafficLocalProtocol_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 1, 4, 1, 4),
    _Hh3cIPSecTrafficLocalProtocol_Type()
)
hh3cIPSecTrafficLocalProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPSecTrafficLocalProtocol.setStatus("current")


class _Hh3cIPSecTrafficLocalPort_Type(Integer32):
    """Custom type hh3cIPSecTrafficLocalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cIPSecTrafficLocalPort_Type.__name__ = "Integer32"
_Hh3cIPSecTrafficLocalPort_Object = MibTableColumn
hh3cIPSecTrafficLocalPort = _Hh3cIPSecTrafficLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 1, 4, 1, 5),
    _Hh3cIPSecTrafficLocalPort_Type()
)
hh3cIPSecTrafficLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPSecTrafficLocalPort.setStatus("current")
_Hh3cIPSecTrafficRemoteType_Type = Hh3cTrafficType
_Hh3cIPSecTrafficRemoteType_Object = MibTableColumn
hh3cIPSecTrafficRemoteType = _Hh3cIPSecTrafficRemoteType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 1, 4, 1, 6),
    _Hh3cIPSecTrafficRemoteType_Type()
)
hh3cIPSecTrafficRemoteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPSecTrafficRemoteType.setStatus("current")
_Hh3cIPSecTrafficRemoteAddr1_Type = IpAddress
_Hh3cIPSecTrafficRemoteAddr1_Object = MibTableColumn
hh3cIPSecTrafficRemoteAddr1 = _Hh3cIPSecTrafficRemoteAddr1_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 1, 4, 1, 7),
    _Hh3cIPSecTrafficRemoteAddr1_Type()
)
hh3cIPSecTrafficRemoteAddr1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPSecTrafficRemoteAddr1.setStatus("current")
_Hh3cIPSecTrafficRemoteAddr2_Type = IpAddress
_Hh3cIPSecTrafficRemoteAddr2_Object = MibTableColumn
hh3cIPSecTrafficRemoteAddr2 = _Hh3cIPSecTrafficRemoteAddr2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 1, 4, 1, 8),
    _Hh3cIPSecTrafficRemoteAddr2_Type()
)
hh3cIPSecTrafficRemoteAddr2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPSecTrafficRemoteAddr2.setStatus("current")


class _Hh3cIPSecTrafficRemoteProtocol_Type(Integer32):
    """Custom type hh3cIPSecTrafficRemoteProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Hh3cIPSecTrafficRemoteProtocol_Type.__name__ = "Integer32"
_Hh3cIPSecTrafficRemoteProtocol_Object = MibTableColumn
hh3cIPSecTrafficRemoteProtocol = _Hh3cIPSecTrafficRemoteProtocol_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 1, 4, 1, 9),
    _Hh3cIPSecTrafficRemoteProtocol_Type()
)
hh3cIPSecTrafficRemoteProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPSecTrafficRemoteProtocol.setStatus("current")


class _Hh3cIPSecTrafficRemotePort_Type(Integer32):
    """Custom type hh3cIPSecTrafficRemotePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cIPSecTrafficRemotePort_Type.__name__ = "Integer32"
_Hh3cIPSecTrafficRemotePort_Object = MibTableColumn
hh3cIPSecTrafficRemotePort = _Hh3cIPSecTrafficRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 1, 4, 1, 10),
    _Hh3cIPSecTrafficRemotePort_Type()
)
hh3cIPSecTrafficRemotePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPSecTrafficRemotePort.setStatus("current")
_Hh3cIPSecGlobalStats_ObjectIdentity = ObjectIdentity
hh3cIPSecGlobalStats = _Hh3cIPSecGlobalStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 1, 5)
)
_Hh3cIPSecGlobalActiveTunnels_Type = Gauge32
_Hh3cIPSecGlobalActiveTunnels_Object = MibScalar
hh3cIPSecGlobalActiveTunnels = _Hh3cIPSecGlobalActiveTunnels_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 1, 5, 1),
    _Hh3cIPSecGlobalActiveTunnels_Type()
)
hh3cIPSecGlobalActiveTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPSecGlobalActiveTunnels.setStatus("current")
_Hh3cIPSecGlobalActiveSas_Type = Gauge32
_Hh3cIPSecGlobalActiveSas_Object = MibScalar
hh3cIPSecGlobalActiveSas = _Hh3cIPSecGlobalActiveSas_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 1, 5, 2),
    _Hh3cIPSecGlobalActiveSas_Type()
)
hh3cIPSecGlobalActiveSas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPSecGlobalActiveSas.setStatus("current")
_Hh3cIPSecGlobalInOctets_Type = Counter64
_Hh3cIPSecGlobalInOctets_Object = MibScalar
hh3cIPSecGlobalInOctets = _Hh3cIPSecGlobalInOctets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 1, 5, 3),
    _Hh3cIPSecGlobalInOctets_Type()
)
hh3cIPSecGlobalInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPSecGlobalInOctets.setStatus("current")
_Hh3cIPSecGlobalInDecompOctets_Type = Counter64
_Hh3cIPSecGlobalInDecompOctets_Object = MibScalar
hh3cIPSecGlobalInDecompOctets = _Hh3cIPSecGlobalInDecompOctets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 1, 5, 4),
    _Hh3cIPSecGlobalInDecompOctets_Type()
)
hh3cIPSecGlobalInDecompOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPSecGlobalInDecompOctets.setStatus("current")
_Hh3cIPSecGlobalInPkts_Type = Counter64
_Hh3cIPSecGlobalInPkts_Object = MibScalar
hh3cIPSecGlobalInPkts = _Hh3cIPSecGlobalInPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 1, 5, 5),
    _Hh3cIPSecGlobalInPkts_Type()
)
hh3cIPSecGlobalInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPSecGlobalInPkts.setStatus("current")
_Hh3cIPSecGlobalInDrops_Type = Counter64
_Hh3cIPSecGlobalInDrops_Object = MibScalar
hh3cIPSecGlobalInDrops = _Hh3cIPSecGlobalInDrops_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 1, 5, 6),
    _Hh3cIPSecGlobalInDrops_Type()
)
hh3cIPSecGlobalInDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPSecGlobalInDrops.setStatus("current")
_Hh3cIPSecGlobalInReplayDrops_Type = Counter32
_Hh3cIPSecGlobalInReplayDrops_Object = MibScalar
hh3cIPSecGlobalInReplayDrops = _Hh3cIPSecGlobalInReplayDrops_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 1, 5, 7),
    _Hh3cIPSecGlobalInReplayDrops_Type()
)
hh3cIPSecGlobalInReplayDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPSecGlobalInReplayDrops.setStatus("current")
_Hh3cIPSecGlobalInAuthFails_Type = Counter32
_Hh3cIPSecGlobalInAuthFails_Object = MibScalar
hh3cIPSecGlobalInAuthFails = _Hh3cIPSecGlobalInAuthFails_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 1, 5, 8),
    _Hh3cIPSecGlobalInAuthFails_Type()
)
hh3cIPSecGlobalInAuthFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPSecGlobalInAuthFails.setStatus("current")
_Hh3cIPSecGlobalInDecryptFails_Type = Counter32
_Hh3cIPSecGlobalInDecryptFails_Object = MibScalar
hh3cIPSecGlobalInDecryptFails = _Hh3cIPSecGlobalInDecryptFails_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 1, 5, 9),
    _Hh3cIPSecGlobalInDecryptFails_Type()
)
hh3cIPSecGlobalInDecryptFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPSecGlobalInDecryptFails.setStatus("current")
_Hh3cIPSecGlobalOutOctets_Type = Counter64
_Hh3cIPSecGlobalOutOctets_Object = MibScalar
hh3cIPSecGlobalOutOctets = _Hh3cIPSecGlobalOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 1, 5, 10),
    _Hh3cIPSecGlobalOutOctets_Type()
)
hh3cIPSecGlobalOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPSecGlobalOutOctets.setStatus("current")
_Hh3cIPSecGlobalOutUncompOctets_Type = Counter64
_Hh3cIPSecGlobalOutUncompOctets_Object = MibScalar
hh3cIPSecGlobalOutUncompOctets = _Hh3cIPSecGlobalOutUncompOctets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 1, 5, 11),
    _Hh3cIPSecGlobalOutUncompOctets_Type()
)
hh3cIPSecGlobalOutUncompOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPSecGlobalOutUncompOctets.setStatus("current")
_Hh3cIPSecGlobalOutPkts_Type = Counter64
_Hh3cIPSecGlobalOutPkts_Object = MibScalar
hh3cIPSecGlobalOutPkts = _Hh3cIPSecGlobalOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 1, 5, 12),
    _Hh3cIPSecGlobalOutPkts_Type()
)
hh3cIPSecGlobalOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPSecGlobalOutPkts.setStatus("current")
_Hh3cIPSecGlobalOutDrops_Type = Counter64
_Hh3cIPSecGlobalOutDrops_Object = MibScalar
hh3cIPSecGlobalOutDrops = _Hh3cIPSecGlobalOutDrops_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 1, 5, 13),
    _Hh3cIPSecGlobalOutDrops_Type()
)
hh3cIPSecGlobalOutDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPSecGlobalOutDrops.setStatus("current")
_Hh3cIPSecGlobalOutEncryptFails_Type = Counter32
_Hh3cIPSecGlobalOutEncryptFails_Object = MibScalar
hh3cIPSecGlobalOutEncryptFails = _Hh3cIPSecGlobalOutEncryptFails_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 1, 5, 14),
    _Hh3cIPSecGlobalOutEncryptFails_Type()
)
hh3cIPSecGlobalOutEncryptFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPSecGlobalOutEncryptFails.setStatus("current")
_Hh3cIPSecGlobalNoMemoryDropPkts_Type = Counter32
_Hh3cIPSecGlobalNoMemoryDropPkts_Object = MibScalar
hh3cIPSecGlobalNoMemoryDropPkts = _Hh3cIPSecGlobalNoMemoryDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 1, 5, 15),
    _Hh3cIPSecGlobalNoMemoryDropPkts_Type()
)
hh3cIPSecGlobalNoMemoryDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPSecGlobalNoMemoryDropPkts.setStatus("current")
_Hh3cIPSecGlobalNoFindSaDropPkts_Type = Counter32
_Hh3cIPSecGlobalNoFindSaDropPkts_Object = MibScalar
hh3cIPSecGlobalNoFindSaDropPkts = _Hh3cIPSecGlobalNoFindSaDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 1, 5, 16),
    _Hh3cIPSecGlobalNoFindSaDropPkts_Type()
)
hh3cIPSecGlobalNoFindSaDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPSecGlobalNoFindSaDropPkts.setStatus("current")
_Hh3cIPSecGlobalQueueFullDropPkts_Type = Counter32
_Hh3cIPSecGlobalQueueFullDropPkts_Object = MibScalar
hh3cIPSecGlobalQueueFullDropPkts = _Hh3cIPSecGlobalQueueFullDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 1, 5, 17),
    _Hh3cIPSecGlobalQueueFullDropPkts_Type()
)
hh3cIPSecGlobalQueueFullDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPSecGlobalQueueFullDropPkts.setStatus("current")
_Hh3cIPSecGlobalInvalidLenDropPkts_Type = Counter32
_Hh3cIPSecGlobalInvalidLenDropPkts_Object = MibScalar
hh3cIPSecGlobalInvalidLenDropPkts = _Hh3cIPSecGlobalInvalidLenDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 1, 5, 18),
    _Hh3cIPSecGlobalInvalidLenDropPkts_Type()
)
hh3cIPSecGlobalInvalidLenDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPSecGlobalInvalidLenDropPkts.setStatus("current")
_Hh3cIPSecGlobalTooLongDropPkts_Type = Counter32
_Hh3cIPSecGlobalTooLongDropPkts_Object = MibScalar
hh3cIPSecGlobalTooLongDropPkts = _Hh3cIPSecGlobalTooLongDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 1, 5, 19),
    _Hh3cIPSecGlobalTooLongDropPkts_Type()
)
hh3cIPSecGlobalTooLongDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPSecGlobalTooLongDropPkts.setStatus("current")
_Hh3cIPSecGlobalInvalidSaDropPkts_Type = Counter32
_Hh3cIPSecGlobalInvalidSaDropPkts_Object = MibScalar
hh3cIPSecGlobalInvalidSaDropPkts = _Hh3cIPSecGlobalInvalidSaDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 1, 5, 20),
    _Hh3cIPSecGlobalInvalidSaDropPkts_Type()
)
hh3cIPSecGlobalInvalidSaDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIPSecGlobalInvalidSaDropPkts.setStatus("current")
_Hh3cIPSecTrapObject_ObjectIdentity = ObjectIdentity
hh3cIPSecTrapObject = _Hh3cIPSecTrapObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 1, 6)
)
_Hh3cIPSecPolicyName_Type = DisplayString
_Hh3cIPSecPolicyName_Object = MibScalar
hh3cIPSecPolicyName = _Hh3cIPSecPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 1, 6, 1),
    _Hh3cIPSecPolicyName_Type()
)
hh3cIPSecPolicyName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cIPSecPolicyName.setStatus("current")
_Hh3cIPSecPolicySeqNum_Type = Integer32
_Hh3cIPSecPolicySeqNum_Object = MibScalar
hh3cIPSecPolicySeqNum = _Hh3cIPSecPolicySeqNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 1, 6, 2),
    _Hh3cIPSecPolicySeqNum_Type()
)
hh3cIPSecPolicySeqNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cIPSecPolicySeqNum.setStatus("current")
_Hh3cIPSecPolicySize_Type = Integer32
_Hh3cIPSecPolicySize_Object = MibScalar
hh3cIPSecPolicySize = _Hh3cIPSecPolicySize_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 1, 6, 3),
    _Hh3cIPSecPolicySize_Type()
)
hh3cIPSecPolicySize.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cIPSecPolicySize.setStatus("current")
_Hh3cIPSecSpiValue_Type = Integer32
_Hh3cIPSecSpiValue_Object = MibScalar
hh3cIPSecSpiValue = _Hh3cIPSecSpiValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 1, 6, 4),
    _Hh3cIPSecSpiValue_Type()
)
hh3cIPSecSpiValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cIPSecSpiValue.setStatus("current")
_Hh3cIPSecTrapCntl_ObjectIdentity = ObjectIdentity
hh3cIPSecTrapCntl = _Hh3cIPSecTrapCntl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 1, 7)
)
_Hh3cIPSecTrapGlobalCntl_Type = Hh3cTrapStatus
_Hh3cIPSecTrapGlobalCntl_Object = MibScalar
hh3cIPSecTrapGlobalCntl = _Hh3cIPSecTrapGlobalCntl_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 1, 7, 1),
    _Hh3cIPSecTrapGlobalCntl_Type()
)
hh3cIPSecTrapGlobalCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIPSecTrapGlobalCntl.setStatus("current")
_Hh3cIPSecTunnelStartTrapCntl_Type = Hh3cTrapStatus
_Hh3cIPSecTunnelStartTrapCntl_Object = MibScalar
hh3cIPSecTunnelStartTrapCntl = _Hh3cIPSecTunnelStartTrapCntl_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 1, 7, 2),
    _Hh3cIPSecTunnelStartTrapCntl_Type()
)
hh3cIPSecTunnelStartTrapCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIPSecTunnelStartTrapCntl.setStatus("current")
_Hh3cIPSecTunnelStopTrapCntl_Type = Hh3cTrapStatus
_Hh3cIPSecTunnelStopTrapCntl_Object = MibScalar
hh3cIPSecTunnelStopTrapCntl = _Hh3cIPSecTunnelStopTrapCntl_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 1, 7, 3),
    _Hh3cIPSecTunnelStopTrapCntl_Type()
)
hh3cIPSecTunnelStopTrapCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIPSecTunnelStopTrapCntl.setStatus("current")
_Hh3cIPSecNoSaTrapCntl_Type = Hh3cTrapStatus
_Hh3cIPSecNoSaTrapCntl_Object = MibScalar
hh3cIPSecNoSaTrapCntl = _Hh3cIPSecNoSaTrapCntl_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 1, 7, 4),
    _Hh3cIPSecNoSaTrapCntl_Type()
)
hh3cIPSecNoSaTrapCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIPSecNoSaTrapCntl.setStatus("current")
_Hh3cIPSecAuthFailureTrapCntl_Type = Hh3cTrapStatus
_Hh3cIPSecAuthFailureTrapCntl_Object = MibScalar
hh3cIPSecAuthFailureTrapCntl = _Hh3cIPSecAuthFailureTrapCntl_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 1, 7, 5),
    _Hh3cIPSecAuthFailureTrapCntl_Type()
)
hh3cIPSecAuthFailureTrapCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIPSecAuthFailureTrapCntl.setStatus("current")
_Hh3cIPSecEncryFailureTrapCntl_Type = Hh3cTrapStatus
_Hh3cIPSecEncryFailureTrapCntl_Object = MibScalar
hh3cIPSecEncryFailureTrapCntl = _Hh3cIPSecEncryFailureTrapCntl_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 1, 7, 6),
    _Hh3cIPSecEncryFailureTrapCntl_Type()
)
hh3cIPSecEncryFailureTrapCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIPSecEncryFailureTrapCntl.setStatus("current")
_Hh3cIPSecDecryFailureTrapCntl_Type = Hh3cTrapStatus
_Hh3cIPSecDecryFailureTrapCntl_Object = MibScalar
hh3cIPSecDecryFailureTrapCntl = _Hh3cIPSecDecryFailureTrapCntl_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 1, 7, 7),
    _Hh3cIPSecDecryFailureTrapCntl_Type()
)
hh3cIPSecDecryFailureTrapCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIPSecDecryFailureTrapCntl.setStatus("current")
_Hh3cIPSecInvalidSaTrapCntl_Type = Hh3cTrapStatus
_Hh3cIPSecInvalidSaTrapCntl_Object = MibScalar
hh3cIPSecInvalidSaTrapCntl = _Hh3cIPSecInvalidSaTrapCntl_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 1, 7, 8),
    _Hh3cIPSecInvalidSaTrapCntl_Type()
)
hh3cIPSecInvalidSaTrapCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIPSecInvalidSaTrapCntl.setStatus("current")
_Hh3cIPSecPolicyAddTrapCntl_Type = Hh3cTrapStatus
_Hh3cIPSecPolicyAddTrapCntl_Object = MibScalar
hh3cIPSecPolicyAddTrapCntl = _Hh3cIPSecPolicyAddTrapCntl_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 1, 7, 9),
    _Hh3cIPSecPolicyAddTrapCntl_Type()
)
hh3cIPSecPolicyAddTrapCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIPSecPolicyAddTrapCntl.setStatus("current")
_Hh3cIPSecPolicyDelTrapCntl_Type = Hh3cTrapStatus
_Hh3cIPSecPolicyDelTrapCntl_Object = MibScalar
hh3cIPSecPolicyDelTrapCntl = _Hh3cIPSecPolicyDelTrapCntl_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 1, 7, 10),
    _Hh3cIPSecPolicyDelTrapCntl_Type()
)
hh3cIPSecPolicyDelTrapCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIPSecPolicyDelTrapCntl.setStatus("current")
_Hh3cIPSecPolicyAttachTrapCntl_Type = Hh3cTrapStatus
_Hh3cIPSecPolicyAttachTrapCntl_Object = MibScalar
hh3cIPSecPolicyAttachTrapCntl = _Hh3cIPSecPolicyAttachTrapCntl_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 1, 7, 11),
    _Hh3cIPSecPolicyAttachTrapCntl_Type()
)
hh3cIPSecPolicyAttachTrapCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIPSecPolicyAttachTrapCntl.setStatus("current")
_Hh3cIPSecPolicyDetachTrapCntl_Type = Hh3cTrapStatus
_Hh3cIPSecPolicyDetachTrapCntl_Object = MibScalar
hh3cIPSecPolicyDetachTrapCntl = _Hh3cIPSecPolicyDetachTrapCntl_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 1, 7, 12),
    _Hh3cIPSecPolicyDetachTrapCntl_Type()
)
hh3cIPSecPolicyDetachTrapCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIPSecPolicyDetachTrapCntl.setStatus("current")
_Hh3cIPSecTrap_ObjectIdentity = ObjectIdentity
hh3cIPSecTrap = _Hh3cIPSecTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 1, 8)
)
_Hh3cIPSecNotifications_ObjectIdentity = ObjectIdentity
hh3cIPSecNotifications = _Hh3cIPSecNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 1, 8, 1)
)
_Hh3cIPSecConformance_ObjectIdentity = ObjectIdentity
hh3cIPSecConformance = _Hh3cIPSecConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 2)
)
_Hh3cIPSecCompliances_ObjectIdentity = ObjectIdentity
hh3cIPSecCompliances = _Hh3cIPSecCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 2, 1)
)
_Hh3cIPSecGroups_ObjectIdentity = ObjectIdentity
hh3cIPSecGroups = _Hh3cIPSecGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 2, 2)
)

# Managed Objects groups

hh3cIPSecTunnelTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 2, 2, 1)
)
hh3cIPSecTunnelTableGroup.setObjects(
      *(("HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecTunIKETunnelIndex"),
        ("HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecTunLocalAddr"),
        ("HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecTunRemoteAddr"),
        ("HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecTunKeyType"),
        ("HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecTunEncapMode"),
        ("HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecTunInitiator"),
        ("HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecTunLifeSize"),
        ("HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecTunLifeTime"),
        ("HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecTunRemainTime"),
        ("HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecTunActiveTime"),
        ("HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecTunRemainSize"),
        ("HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecTunTotalRefreshes"),
        ("HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecTunCurrentSaInstances"),
        ("HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecTunInSaEncryptAlgo"),
        ("HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecTunInSaAhAuthAlgo"),
        ("HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecTunInSaEspAuthAlgo"),
        ("HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecTunDiffHellmanGrp"),
        ("HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecTunOutSaEncryptAlgo"),
        ("HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecTunOutSaAhAuthAlgo"),
        ("HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecTunOutSaEspAuthAlgo"),
        ("HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecTunPolicyName"),
        ("HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecTunPolicyNum"),
        ("HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecTunStatus"))
)
if mibBuilder.loadTexts:
    hh3cIPSecTunnelTableGroup.setStatus("current")

hh3cIPSecTunnelStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 2, 2, 2)
)
hh3cIPSecTunnelStatGroup.setObjects(
      *(("HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecTunInOctets"),
        ("HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecTunInDecompOctets"),
        ("HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecTunInPkts"),
        ("HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecTunInDropPkts"),
        ("HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecTunInReplayDropPkts"),
        ("HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecTunInAuthFails"),
        ("HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecTunInDecryptFails"),
        ("HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecTunOutOctets"),
        ("HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecTunOutUncompOctets"),
        ("HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecTunOutPkts"),
        ("HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecTunOutDropPkts"),
        ("HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecTunOutEncryptFails"),
        ("HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecTunNoMemoryDropPkts"),
        ("HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecTunQueueFullDropPkts"),
        ("HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecTunInvalidLenDropPkts"),
        ("HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecTunTooLongDropPkts"),
        ("HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecTunInvalidSaDropPkts"))
)
if mibBuilder.loadTexts:
    hh3cIPSecTunnelStatGroup.setStatus("current")

hh3cIPSecSaGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 2, 2, 3)
)
hh3cIPSecSaGroup.setObjects(
      *(("HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecSaDirection"),
        ("HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecSaValue"),
        ("HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecSaProtocol"),
        ("HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecSaEncryptAlgo"),
        ("HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecSaAuthAlgo"),
        ("HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecSaStatus"))
)
if mibBuilder.loadTexts:
    hh3cIPSecSaGroup.setStatus("current")

hh3cIPSecTrafficTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 2, 2, 4)
)
hh3cIPSecTrafficTableGroup.setObjects(
      *(("HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecTrafficLocalType"),
        ("HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecTrafficLocalAddr1"),
        ("HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecTrafficLocalAddr2"),
        ("HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecTrafficLocalProtocol"),
        ("HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecTrafficLocalPort"),
        ("HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecTrafficRemoteType"),
        ("HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecTrafficRemoteAddr1"),
        ("HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecTrafficRemoteAddr2"),
        ("HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecTrafficRemoteProtocol"),
        ("HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecTrafficRemotePort"))
)
if mibBuilder.loadTexts:
    hh3cIPSecTrafficTableGroup.setStatus("current")

hh3cIPSecGlobalStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 2, 2, 5)
)
hh3cIPSecGlobalStatsGroup.setObjects(
      *(("HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecGlobalActiveTunnels"),
        ("HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecGlobalActiveSas"),
        ("HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecGlobalInOctets"),
        ("HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecGlobalInDecompOctets"),
        ("HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecGlobalInPkts"),
        ("HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecGlobalInDrops"),
        ("HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecGlobalInReplayDrops"),
        ("HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecGlobalInAuthFails"),
        ("HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecGlobalInDecryptFails"),
        ("HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecGlobalOutOctets"),
        ("HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecGlobalOutUncompOctets"),
        ("HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecGlobalOutPkts"),
        ("HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecGlobalOutDrops"),
        ("HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecGlobalOutEncryptFails"),
        ("HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecGlobalNoMemoryDropPkts"),
        ("HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecGlobalNoFindSaDropPkts"),
        ("HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecGlobalQueueFullDropPkts"),
        ("HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecGlobalInvalidLenDropPkts"),
        ("HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecGlobalTooLongDropPkts"),
        ("HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecGlobalInvalidSaDropPkts"))
)
if mibBuilder.loadTexts:
    hh3cIPSecGlobalStatsGroup.setStatus("current")

hh3cIPSecTrapObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 2, 2, 6)
)
hh3cIPSecTrapObjectGroup.setObjects(
      *(("HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecPolicyName"),
        ("HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecPolicySeqNum"),
        ("HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecPolicySize"),
        ("HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecSpiValue"))
)
if mibBuilder.loadTexts:
    hh3cIPSecTrapObjectGroup.setStatus("current")

hh3cIPSecTrapCntlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 2, 2, 7)
)
hh3cIPSecTrapCntlGroup.setObjects(
      *(("HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecTrapGlobalCntl"),
        ("HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecTunnelStartTrapCntl"),
        ("HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecTunnelStopTrapCntl"),
        ("HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecNoSaTrapCntl"),
        ("HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecAuthFailureTrapCntl"),
        ("HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecEncryFailureTrapCntl"),
        ("HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecDecryFailureTrapCntl"),
        ("HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecInvalidSaTrapCntl"),
        ("HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecPolicyAddTrapCntl"),
        ("HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecPolicyDelTrapCntl"),
        ("HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecPolicyAttachTrapCntl"),
        ("HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecPolicyDetachTrapCntl"))
)
if mibBuilder.loadTexts:
    hh3cIPSecTrapCntlGroup.setStatus("current")


# Notification objects

hh3cIPSecTunnelStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 1, 8, 1, 1)
)
hh3cIPSecTunnelStart.setObjects(
      *(("HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecTunLocalAddr"),
        ("HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecTunRemoteAddr"),
        ("HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecTunLifeTime"),
        ("HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecTunLifeSize"))
)
if mibBuilder.loadTexts:
    hh3cIPSecTunnelStart.setStatus(
        "current"
    )

hh3cIPSecTunnelStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 1, 8, 1, 2)
)
hh3cIPSecTunnelStop.setObjects(
      *(("HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecTunLocalAddr"),
        ("HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecTunRemoteAddr"),
        ("HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecTunActiveTime"))
)
if mibBuilder.loadTexts:
    hh3cIPSecTunnelStop.setStatus(
        "current"
    )

hh3cIPSecNoSaFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 1, 8, 1, 3)
)
hh3cIPSecNoSaFailure.setObjects(
      *(("HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecTunLocalAddr"),
        ("HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecTunRemoteAddr"))
)
if mibBuilder.loadTexts:
    hh3cIPSecNoSaFailure.setStatus(
        "current"
    )

hh3cIPSecAuthFailFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 1, 8, 1, 4)
)
hh3cIPSecAuthFailFailure.setObjects(
      *(("HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecTunLocalAddr"),
        ("HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecTunRemoteAddr"))
)
if mibBuilder.loadTexts:
    hh3cIPSecAuthFailFailure.setStatus(
        "current"
    )

hh3cIPSecEncryFailFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 1, 8, 1, 5)
)
hh3cIPSecEncryFailFailure.setObjects(
      *(("HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecTunLocalAddr"),
        ("HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecTunRemoteAddr"))
)
if mibBuilder.loadTexts:
    hh3cIPSecEncryFailFailure.setStatus(
        "current"
    )

hh3cIPSecDecryFailFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 1, 8, 1, 6)
)
hh3cIPSecDecryFailFailure.setObjects(
      *(("HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecTunLocalAddr"),
        ("HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecTunRemoteAddr"))
)
if mibBuilder.loadTexts:
    hh3cIPSecDecryFailFailure.setStatus(
        "current"
    )

hh3cIPSecInvalidSaFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 1, 8, 1, 7)
)
hh3cIPSecInvalidSaFailure.setObjects(
      *(("HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecTunLocalAddr"),
        ("HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecTunRemoteAddr"),
        ("HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecSpiValue"))
)
if mibBuilder.loadTexts:
    hh3cIPSecInvalidSaFailure.setStatus(
        "current"
    )

hh3cIPSecPolicyAdd = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 1, 8, 1, 8)
)
hh3cIPSecPolicyAdd.setObjects(
      *(("HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecPolicyName"),
        ("HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecPolicySeqNum"),
        ("HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecPolicySize"))
)
if mibBuilder.loadTexts:
    hh3cIPSecPolicyAdd.setStatus(
        "current"
    )

hh3cIPSecPolicyDel = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 1, 8, 1, 9)
)
hh3cIPSecPolicyDel.setObjects(
      *(("HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecPolicyName"),
        ("HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecPolicySeqNum"),
        ("HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecPolicySize"))
)
if mibBuilder.loadTexts:
    hh3cIPSecPolicyDel.setStatus(
        "current"
    )

hh3cIPSecPolicyAttach = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 1, 8, 1, 10)
)
hh3cIPSecPolicyAttach.setObjects(
      *(("HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecPolicyName"),
        ("HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecPolicySize"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    hh3cIPSecPolicyAttach.setStatus(
        "current"
    )

hh3cIPSecPolicyDetach = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 1, 8, 1, 11)
)
hh3cIPSecPolicyDetach.setObjects(
      *(("HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecPolicyName"),
        ("HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecPolicySize"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    hh3cIPSecPolicyDetach.setStatus(
        "current"
    )


# Notifications groups

hh3cIPSecTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 2, 2, 8)
)
hh3cIPSecTrapGroup.setObjects(
      *(("HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecTunnelStart"),
        ("HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecTunnelStop"),
        ("HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecNoSaFailure"),
        ("HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecAuthFailFailure"),
        ("HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecEncryFailFailure"),
        ("HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecDecryFailFailure"),
        ("HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecInvalidSaFailure"),
        ("HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecPolicyAdd"),
        ("HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecPolicyDel"),
        ("HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecPolicyAttach"),
        ("HH3C-IPSEC-MONITOR-MIB", "hh3cIPSecPolicyDetach"))
)
if mibBuilder.loadTexts:
    hh3cIPSecTrapGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hh3cIPSecCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cIPSecCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-IPSEC-MONITOR-MIB",
    **{"Hh3cDiffHellmanGrp": Hh3cDiffHellmanGrp,
       "Hh3cEncapMode": Hh3cEncapMode,
       "Hh3cEncryptAlgo": Hh3cEncryptAlgo,
       "Hh3cAuthAlgo": Hh3cAuthAlgo,
       "Hh3cSaProtocol": Hh3cSaProtocol,
       "Hh3cTrapStatus": Hh3cTrapStatus,
       "Hh3cIPSecIDType": Hh3cIPSecIDType,
       "Hh3cTrafficType": Hh3cTrafficType,
       "Hh3cIPSecNegoType": Hh3cIPSecNegoType,
       "Hh3cIPSecTunnelState": Hh3cIPSecTunnelState,
       "hh3cIPSecMonitor": hh3cIPSecMonitor,
       "hh3cIPSecObjects": hh3cIPSecObjects,
       "hh3cIPSecTunnelTable": hh3cIPSecTunnelTable,
       "hh3cIPSecTunnelEntry": hh3cIPSecTunnelEntry,
       "hh3cIPSecTunIfIndex": hh3cIPSecTunIfIndex,
       "hh3cIPSecTunEntryIndex": hh3cIPSecTunEntryIndex,
       "hh3cIPSecTunIndex": hh3cIPSecTunIndex,
       "hh3cIPSecTunIKETunnelIndex": hh3cIPSecTunIKETunnelIndex,
       "hh3cIPSecTunLocalAddr": hh3cIPSecTunLocalAddr,
       "hh3cIPSecTunRemoteAddr": hh3cIPSecTunRemoteAddr,
       "hh3cIPSecTunKeyType": hh3cIPSecTunKeyType,
       "hh3cIPSecTunEncapMode": hh3cIPSecTunEncapMode,
       "hh3cIPSecTunInitiator": hh3cIPSecTunInitiator,
       "hh3cIPSecTunLifeSize": hh3cIPSecTunLifeSize,
       "hh3cIPSecTunLifeTime": hh3cIPSecTunLifeTime,
       "hh3cIPSecTunRemainTime": hh3cIPSecTunRemainTime,
       "hh3cIPSecTunActiveTime": hh3cIPSecTunActiveTime,
       "hh3cIPSecTunRemainSize": hh3cIPSecTunRemainSize,
       "hh3cIPSecTunTotalRefreshes": hh3cIPSecTunTotalRefreshes,
       "hh3cIPSecTunCurrentSaInstances": hh3cIPSecTunCurrentSaInstances,
       "hh3cIPSecTunInSaEncryptAlgo": hh3cIPSecTunInSaEncryptAlgo,
       "hh3cIPSecTunInSaAhAuthAlgo": hh3cIPSecTunInSaAhAuthAlgo,
       "hh3cIPSecTunInSaEspAuthAlgo": hh3cIPSecTunInSaEspAuthAlgo,
       "hh3cIPSecTunDiffHellmanGrp": hh3cIPSecTunDiffHellmanGrp,
       "hh3cIPSecTunOutSaEncryptAlgo": hh3cIPSecTunOutSaEncryptAlgo,
       "hh3cIPSecTunOutSaAhAuthAlgo": hh3cIPSecTunOutSaAhAuthAlgo,
       "hh3cIPSecTunOutSaEspAuthAlgo": hh3cIPSecTunOutSaEspAuthAlgo,
       "hh3cIPSecTunPolicyName": hh3cIPSecTunPolicyName,
       "hh3cIPSecTunPolicyNum": hh3cIPSecTunPolicyNum,
       "hh3cIPSecTunStatus": hh3cIPSecTunStatus,
       "hh3cIPSecTunnelStatTable": hh3cIPSecTunnelStatTable,
       "hh3cIPSecTunnelStatEntry": hh3cIPSecTunnelStatEntry,
       "hh3cIPSecTunInOctets": hh3cIPSecTunInOctets,
       "hh3cIPSecTunInDecompOctets": hh3cIPSecTunInDecompOctets,
       "hh3cIPSecTunInPkts": hh3cIPSecTunInPkts,
       "hh3cIPSecTunInDropPkts": hh3cIPSecTunInDropPkts,
       "hh3cIPSecTunInReplayDropPkts": hh3cIPSecTunInReplayDropPkts,
       "hh3cIPSecTunInAuthFails": hh3cIPSecTunInAuthFails,
       "hh3cIPSecTunInDecryptFails": hh3cIPSecTunInDecryptFails,
       "hh3cIPSecTunOutOctets": hh3cIPSecTunOutOctets,
       "hh3cIPSecTunOutUncompOctets": hh3cIPSecTunOutUncompOctets,
       "hh3cIPSecTunOutPkts": hh3cIPSecTunOutPkts,
       "hh3cIPSecTunOutDropPkts": hh3cIPSecTunOutDropPkts,
       "hh3cIPSecTunOutEncryptFails": hh3cIPSecTunOutEncryptFails,
       "hh3cIPSecTunNoMemoryDropPkts": hh3cIPSecTunNoMemoryDropPkts,
       "hh3cIPSecTunQueueFullDropPkts": hh3cIPSecTunQueueFullDropPkts,
       "hh3cIPSecTunInvalidLenDropPkts": hh3cIPSecTunInvalidLenDropPkts,
       "hh3cIPSecTunTooLongDropPkts": hh3cIPSecTunTooLongDropPkts,
       "hh3cIPSecTunInvalidSaDropPkts": hh3cIPSecTunInvalidSaDropPkts,
       "hh3cIPSecSaTable": hh3cIPSecSaTable,
       "hh3cIPSecSaEntry": hh3cIPSecSaEntry,
       "hh3cIPSecSaIndex": hh3cIPSecSaIndex,
       "hh3cIPSecSaDirection": hh3cIPSecSaDirection,
       "hh3cIPSecSaValue": hh3cIPSecSaValue,
       "hh3cIPSecSaProtocol": hh3cIPSecSaProtocol,
       "hh3cIPSecSaEncryptAlgo": hh3cIPSecSaEncryptAlgo,
       "hh3cIPSecSaAuthAlgo": hh3cIPSecSaAuthAlgo,
       "hh3cIPSecSaStatus": hh3cIPSecSaStatus,
       "hh3cIPSecTrafficTable": hh3cIPSecTrafficTable,
       "hh3cIPSecTrafficEntry": hh3cIPSecTrafficEntry,
       "hh3cIPSecTrafficLocalType": hh3cIPSecTrafficLocalType,
       "hh3cIPSecTrafficLocalAddr1": hh3cIPSecTrafficLocalAddr1,
       "hh3cIPSecTrafficLocalAddr2": hh3cIPSecTrafficLocalAddr2,
       "hh3cIPSecTrafficLocalProtocol": hh3cIPSecTrafficLocalProtocol,
       "hh3cIPSecTrafficLocalPort": hh3cIPSecTrafficLocalPort,
       "hh3cIPSecTrafficRemoteType": hh3cIPSecTrafficRemoteType,
       "hh3cIPSecTrafficRemoteAddr1": hh3cIPSecTrafficRemoteAddr1,
       "hh3cIPSecTrafficRemoteAddr2": hh3cIPSecTrafficRemoteAddr2,
       "hh3cIPSecTrafficRemoteProtocol": hh3cIPSecTrafficRemoteProtocol,
       "hh3cIPSecTrafficRemotePort": hh3cIPSecTrafficRemotePort,
       "hh3cIPSecGlobalStats": hh3cIPSecGlobalStats,
       "hh3cIPSecGlobalActiveTunnels": hh3cIPSecGlobalActiveTunnels,
       "hh3cIPSecGlobalActiveSas": hh3cIPSecGlobalActiveSas,
       "hh3cIPSecGlobalInOctets": hh3cIPSecGlobalInOctets,
       "hh3cIPSecGlobalInDecompOctets": hh3cIPSecGlobalInDecompOctets,
       "hh3cIPSecGlobalInPkts": hh3cIPSecGlobalInPkts,
       "hh3cIPSecGlobalInDrops": hh3cIPSecGlobalInDrops,
       "hh3cIPSecGlobalInReplayDrops": hh3cIPSecGlobalInReplayDrops,
       "hh3cIPSecGlobalInAuthFails": hh3cIPSecGlobalInAuthFails,
       "hh3cIPSecGlobalInDecryptFails": hh3cIPSecGlobalInDecryptFails,
       "hh3cIPSecGlobalOutOctets": hh3cIPSecGlobalOutOctets,
       "hh3cIPSecGlobalOutUncompOctets": hh3cIPSecGlobalOutUncompOctets,
       "hh3cIPSecGlobalOutPkts": hh3cIPSecGlobalOutPkts,
       "hh3cIPSecGlobalOutDrops": hh3cIPSecGlobalOutDrops,
       "hh3cIPSecGlobalOutEncryptFails": hh3cIPSecGlobalOutEncryptFails,
       "hh3cIPSecGlobalNoMemoryDropPkts": hh3cIPSecGlobalNoMemoryDropPkts,
       "hh3cIPSecGlobalNoFindSaDropPkts": hh3cIPSecGlobalNoFindSaDropPkts,
       "hh3cIPSecGlobalQueueFullDropPkts": hh3cIPSecGlobalQueueFullDropPkts,
       "hh3cIPSecGlobalInvalidLenDropPkts": hh3cIPSecGlobalInvalidLenDropPkts,
       "hh3cIPSecGlobalTooLongDropPkts": hh3cIPSecGlobalTooLongDropPkts,
       "hh3cIPSecGlobalInvalidSaDropPkts": hh3cIPSecGlobalInvalidSaDropPkts,
       "hh3cIPSecTrapObject": hh3cIPSecTrapObject,
       "hh3cIPSecPolicyName": hh3cIPSecPolicyName,
       "hh3cIPSecPolicySeqNum": hh3cIPSecPolicySeqNum,
       "hh3cIPSecPolicySize": hh3cIPSecPolicySize,
       "hh3cIPSecSpiValue": hh3cIPSecSpiValue,
       "hh3cIPSecTrapCntl": hh3cIPSecTrapCntl,
       "hh3cIPSecTrapGlobalCntl": hh3cIPSecTrapGlobalCntl,
       "hh3cIPSecTunnelStartTrapCntl": hh3cIPSecTunnelStartTrapCntl,
       "hh3cIPSecTunnelStopTrapCntl": hh3cIPSecTunnelStopTrapCntl,
       "hh3cIPSecNoSaTrapCntl": hh3cIPSecNoSaTrapCntl,
       "hh3cIPSecAuthFailureTrapCntl": hh3cIPSecAuthFailureTrapCntl,
       "hh3cIPSecEncryFailureTrapCntl": hh3cIPSecEncryFailureTrapCntl,
       "hh3cIPSecDecryFailureTrapCntl": hh3cIPSecDecryFailureTrapCntl,
       "hh3cIPSecInvalidSaTrapCntl": hh3cIPSecInvalidSaTrapCntl,
       "hh3cIPSecPolicyAddTrapCntl": hh3cIPSecPolicyAddTrapCntl,
       "hh3cIPSecPolicyDelTrapCntl": hh3cIPSecPolicyDelTrapCntl,
       "hh3cIPSecPolicyAttachTrapCntl": hh3cIPSecPolicyAttachTrapCntl,
       "hh3cIPSecPolicyDetachTrapCntl": hh3cIPSecPolicyDetachTrapCntl,
       "hh3cIPSecTrap": hh3cIPSecTrap,
       "hh3cIPSecNotifications": hh3cIPSecNotifications,
       "hh3cIPSecTunnelStart": hh3cIPSecTunnelStart,
       "hh3cIPSecTunnelStop": hh3cIPSecTunnelStop,
       "hh3cIPSecNoSaFailure": hh3cIPSecNoSaFailure,
       "hh3cIPSecAuthFailFailure": hh3cIPSecAuthFailFailure,
       "hh3cIPSecEncryFailFailure": hh3cIPSecEncryFailFailure,
       "hh3cIPSecDecryFailFailure": hh3cIPSecDecryFailFailure,
       "hh3cIPSecInvalidSaFailure": hh3cIPSecInvalidSaFailure,
       "hh3cIPSecPolicyAdd": hh3cIPSecPolicyAdd,
       "hh3cIPSecPolicyDel": hh3cIPSecPolicyDel,
       "hh3cIPSecPolicyAttach": hh3cIPSecPolicyAttach,
       "hh3cIPSecPolicyDetach": hh3cIPSecPolicyDetach,
       "hh3cIPSecConformance": hh3cIPSecConformance,
       "hh3cIPSecCompliances": hh3cIPSecCompliances,
       "hh3cIPSecCompliance": hh3cIPSecCompliance,
       "hh3cIPSecGroups": hh3cIPSecGroups,
       "hh3cIPSecTunnelTableGroup": hh3cIPSecTunnelTableGroup,
       "hh3cIPSecTunnelStatGroup": hh3cIPSecTunnelStatGroup,
       "hh3cIPSecSaGroup": hh3cIPSecSaGroup,
       "hh3cIPSecTrafficTableGroup": hh3cIPSecTrafficTableGroup,
       "hh3cIPSecGlobalStatsGroup": hh3cIPSecGlobalStatsGroup,
       "hh3cIPSecTrapObjectGroup": hh3cIPSecTrapObjectGroup,
       "hh3cIPSecTrapCntlGroup": hh3cIPSecTrapCntlGroup,
       "hh3cIPSecTrapGroup": hh3cIPSecTrapGroup}
)
