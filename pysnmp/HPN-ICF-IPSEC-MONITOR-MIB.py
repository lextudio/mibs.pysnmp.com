# SNMP MIB module (HPN-ICF-IPSEC-MONITOR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-IPSEC-MONITOR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:00:38 2024
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

hpnicfIPSecMonitor = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class HpnicfDiffHellmanGrp(Integer32, TextualConvention):
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



class HpnicfEncapMode(Integer32, TextualConvention):
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



class HpnicfEncryptAlgo(Integer32, TextualConvention):
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



class HpnicfAuthAlgo(Integer32, TextualConvention):
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



class HpnicfSaProtocol(Integer32, TextualConvention):
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



class HpnicfTrapStatus(Integer32, TextualConvention):
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



class HpnicfIPSecIDType(Integer32, TextualConvention):
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



class HpnicfTrafficType(Integer32, TextualConvention):
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



class HpnicfIPSecNegoType(Integer32, TextualConvention):
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



class HpnicfIPSecTunnelState(Integer32, TextualConvention):
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

_HpnicfIPSecObjects_ObjectIdentity = ObjectIdentity
hpnicfIPSecObjects = _HpnicfIPSecObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 1)
)
_HpnicfIPSecTunnelTable_Object = MibTable
hpnicfIPSecTunnelTable = _HpnicfIPSecTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 1, 1)
)
if mibBuilder.loadTexts:
    hpnicfIPSecTunnelTable.setStatus("current")
_HpnicfIPSecTunnelEntry_Object = MibTableRow
hpnicfIPSecTunnelEntry = _HpnicfIPSecTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 1, 1, 1)
)
hpnicfIPSecTunnelEntry.setIndexNames(
    (0, "HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecTunIfIndex"),
    (0, "HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecTunEntryIndex"),
    (0, "HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecTunIndex"),
)
if mibBuilder.loadTexts:
    hpnicfIPSecTunnelEntry.setStatus("current")


class _HpnicfIPSecTunIfIndex_Type(Integer32):
    """Custom type hpnicfIPSecTunIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpnicfIPSecTunIfIndex_Type.__name__ = "Integer32"
_HpnicfIPSecTunIfIndex_Object = MibTableColumn
hpnicfIPSecTunIfIndex = _HpnicfIPSecTunIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 1, 1, 1, 1),
    _HpnicfIPSecTunIfIndex_Type()
)
hpnicfIPSecTunIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfIPSecTunIfIndex.setStatus("current")


class _HpnicfIPSecTunEntryIndex_Type(Integer32):
    """Custom type hpnicfIPSecTunEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpnicfIPSecTunEntryIndex_Type.__name__ = "Integer32"
_HpnicfIPSecTunEntryIndex_Object = MibTableColumn
hpnicfIPSecTunEntryIndex = _HpnicfIPSecTunEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 1, 1, 1, 2),
    _HpnicfIPSecTunEntryIndex_Type()
)
hpnicfIPSecTunEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfIPSecTunEntryIndex.setStatus("current")


class _HpnicfIPSecTunIndex_Type(Integer32):
    """Custom type hpnicfIPSecTunIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpnicfIPSecTunIndex_Type.__name__ = "Integer32"
_HpnicfIPSecTunIndex_Object = MibTableColumn
hpnicfIPSecTunIndex = _HpnicfIPSecTunIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 1, 1, 1, 3),
    _HpnicfIPSecTunIndex_Type()
)
hpnicfIPSecTunIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfIPSecTunIndex.setStatus("current")


class _HpnicfIPSecTunIKETunnelIndex_Type(Integer32):
    """Custom type hpnicfIPSecTunIKETunnelIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpnicfIPSecTunIKETunnelIndex_Type.__name__ = "Integer32"
_HpnicfIPSecTunIKETunnelIndex_Object = MibTableColumn
hpnicfIPSecTunIKETunnelIndex = _HpnicfIPSecTunIKETunnelIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 1, 1, 1, 4),
    _HpnicfIPSecTunIKETunnelIndex_Type()
)
hpnicfIPSecTunIKETunnelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPSecTunIKETunnelIndex.setStatus("current")
_HpnicfIPSecTunLocalAddr_Type = IpAddress
_HpnicfIPSecTunLocalAddr_Object = MibTableColumn
hpnicfIPSecTunLocalAddr = _HpnicfIPSecTunLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 1, 1, 1, 5),
    _HpnicfIPSecTunLocalAddr_Type()
)
hpnicfIPSecTunLocalAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPSecTunLocalAddr.setStatus("current")
_HpnicfIPSecTunRemoteAddr_Type = IpAddress
_HpnicfIPSecTunRemoteAddr_Object = MibTableColumn
hpnicfIPSecTunRemoteAddr = _HpnicfIPSecTunRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 1, 1, 1, 6),
    _HpnicfIPSecTunRemoteAddr_Type()
)
hpnicfIPSecTunRemoteAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPSecTunRemoteAddr.setStatus("current")
_HpnicfIPSecTunKeyType_Type = HpnicfIPSecNegoType
_HpnicfIPSecTunKeyType_Object = MibTableColumn
hpnicfIPSecTunKeyType = _HpnicfIPSecTunKeyType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 1, 1, 1, 7),
    _HpnicfIPSecTunKeyType_Type()
)
hpnicfIPSecTunKeyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPSecTunKeyType.setStatus("current")
_HpnicfIPSecTunEncapMode_Type = HpnicfEncapMode
_HpnicfIPSecTunEncapMode_Object = MibTableColumn
hpnicfIPSecTunEncapMode = _HpnicfIPSecTunEncapMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 1, 1, 1, 8),
    _HpnicfIPSecTunEncapMode_Type()
)
hpnicfIPSecTunEncapMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPSecTunEncapMode.setStatus("current")


class _HpnicfIPSecTunInitiator_Type(Integer32):
    """Custom type hpnicfIPSecTunInitiator based on Integer32"""
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


_HpnicfIPSecTunInitiator_Type.__name__ = "Integer32"
_HpnicfIPSecTunInitiator_Object = MibTableColumn
hpnicfIPSecTunInitiator = _HpnicfIPSecTunInitiator_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 1, 1, 1, 9),
    _HpnicfIPSecTunInitiator_Type()
)
hpnicfIPSecTunInitiator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPSecTunInitiator.setStatus("current")
_HpnicfIPSecTunLifeSize_Type = Gauge32
_HpnicfIPSecTunLifeSize_Object = MibTableColumn
hpnicfIPSecTunLifeSize = _HpnicfIPSecTunLifeSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 1, 1, 1, 10),
    _HpnicfIPSecTunLifeSize_Type()
)
hpnicfIPSecTunLifeSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPSecTunLifeSize.setStatus("current")


class _HpnicfIPSecTunLifeTime_Type(Integer32):
    """Custom type hpnicfIPSecTunLifeTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpnicfIPSecTunLifeTime_Type.__name__ = "Integer32"
_HpnicfIPSecTunLifeTime_Object = MibTableColumn
hpnicfIPSecTunLifeTime = _HpnicfIPSecTunLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 1, 1, 1, 11),
    _HpnicfIPSecTunLifeTime_Type()
)
hpnicfIPSecTunLifeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPSecTunLifeTime.setStatus("current")


class _HpnicfIPSecTunRemainTime_Type(Integer32):
    """Custom type hpnicfIPSecTunRemainTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HpnicfIPSecTunRemainTime_Type.__name__ = "Integer32"
_HpnicfIPSecTunRemainTime_Object = MibTableColumn
hpnicfIPSecTunRemainTime = _HpnicfIPSecTunRemainTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 1, 1, 1, 12),
    _HpnicfIPSecTunRemainTime_Type()
)
hpnicfIPSecTunRemainTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPSecTunRemainTime.setStatus("current")


class _HpnicfIPSecTunActiveTime_Type(Integer32):
    """Custom type hpnicfIPSecTunActiveTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HpnicfIPSecTunActiveTime_Type.__name__ = "Integer32"
_HpnicfIPSecTunActiveTime_Object = MibTableColumn
hpnicfIPSecTunActiveTime = _HpnicfIPSecTunActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 1, 1, 1, 13),
    _HpnicfIPSecTunActiveTime_Type()
)
hpnicfIPSecTunActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPSecTunActiveTime.setStatus("current")
_HpnicfIPSecTunRemainSize_Type = Gauge32
_HpnicfIPSecTunRemainSize_Object = MibTableColumn
hpnicfIPSecTunRemainSize = _HpnicfIPSecTunRemainSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 1, 1, 1, 14),
    _HpnicfIPSecTunRemainSize_Type()
)
hpnicfIPSecTunRemainSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPSecTunRemainSize.setStatus("current")
_HpnicfIPSecTunTotalRefreshes_Type = Counter32
_HpnicfIPSecTunTotalRefreshes_Object = MibTableColumn
hpnicfIPSecTunTotalRefreshes = _HpnicfIPSecTunTotalRefreshes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 1, 1, 1, 15),
    _HpnicfIPSecTunTotalRefreshes_Type()
)
hpnicfIPSecTunTotalRefreshes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPSecTunTotalRefreshes.setStatus("current")
_HpnicfIPSecTunCurrentSaInstances_Type = Gauge32
_HpnicfIPSecTunCurrentSaInstances_Object = MibTableColumn
hpnicfIPSecTunCurrentSaInstances = _HpnicfIPSecTunCurrentSaInstances_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 1, 1, 1, 16),
    _HpnicfIPSecTunCurrentSaInstances_Type()
)
hpnicfIPSecTunCurrentSaInstances.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPSecTunCurrentSaInstances.setStatus("current")
_HpnicfIPSecTunInSaEncryptAlgo_Type = HpnicfEncryptAlgo
_HpnicfIPSecTunInSaEncryptAlgo_Object = MibTableColumn
hpnicfIPSecTunInSaEncryptAlgo = _HpnicfIPSecTunInSaEncryptAlgo_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 1, 1, 1, 17),
    _HpnicfIPSecTunInSaEncryptAlgo_Type()
)
hpnicfIPSecTunInSaEncryptAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPSecTunInSaEncryptAlgo.setStatus("current")
_HpnicfIPSecTunInSaAhAuthAlgo_Type = HpnicfAuthAlgo
_HpnicfIPSecTunInSaAhAuthAlgo_Object = MibTableColumn
hpnicfIPSecTunInSaAhAuthAlgo = _HpnicfIPSecTunInSaAhAuthAlgo_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 1, 1, 1, 18),
    _HpnicfIPSecTunInSaAhAuthAlgo_Type()
)
hpnicfIPSecTunInSaAhAuthAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPSecTunInSaAhAuthAlgo.setStatus("current")
_HpnicfIPSecTunInSaEspAuthAlgo_Type = HpnicfAuthAlgo
_HpnicfIPSecTunInSaEspAuthAlgo_Object = MibTableColumn
hpnicfIPSecTunInSaEspAuthAlgo = _HpnicfIPSecTunInSaEspAuthAlgo_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 1, 1, 1, 19),
    _HpnicfIPSecTunInSaEspAuthAlgo_Type()
)
hpnicfIPSecTunInSaEspAuthAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPSecTunInSaEspAuthAlgo.setStatus("current")
_HpnicfIPSecTunDiffHellmanGrp_Type = HpnicfDiffHellmanGrp
_HpnicfIPSecTunDiffHellmanGrp_Object = MibTableColumn
hpnicfIPSecTunDiffHellmanGrp = _HpnicfIPSecTunDiffHellmanGrp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 1, 1, 1, 20),
    _HpnicfIPSecTunDiffHellmanGrp_Type()
)
hpnicfIPSecTunDiffHellmanGrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPSecTunDiffHellmanGrp.setStatus("current")
_HpnicfIPSecTunOutSaEncryptAlgo_Type = HpnicfEncryptAlgo
_HpnicfIPSecTunOutSaEncryptAlgo_Object = MibTableColumn
hpnicfIPSecTunOutSaEncryptAlgo = _HpnicfIPSecTunOutSaEncryptAlgo_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 1, 1, 1, 21),
    _HpnicfIPSecTunOutSaEncryptAlgo_Type()
)
hpnicfIPSecTunOutSaEncryptAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPSecTunOutSaEncryptAlgo.setStatus("current")
_HpnicfIPSecTunOutSaAhAuthAlgo_Type = HpnicfAuthAlgo
_HpnicfIPSecTunOutSaAhAuthAlgo_Object = MibTableColumn
hpnicfIPSecTunOutSaAhAuthAlgo = _HpnicfIPSecTunOutSaAhAuthAlgo_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 1, 1, 1, 22),
    _HpnicfIPSecTunOutSaAhAuthAlgo_Type()
)
hpnicfIPSecTunOutSaAhAuthAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPSecTunOutSaAhAuthAlgo.setStatus("current")
_HpnicfIPSecTunOutSaEspAuthAlgo_Type = HpnicfAuthAlgo
_HpnicfIPSecTunOutSaEspAuthAlgo_Object = MibTableColumn
hpnicfIPSecTunOutSaEspAuthAlgo = _HpnicfIPSecTunOutSaEspAuthAlgo_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 1, 1, 1, 23),
    _HpnicfIPSecTunOutSaEspAuthAlgo_Type()
)
hpnicfIPSecTunOutSaEspAuthAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPSecTunOutSaEspAuthAlgo.setStatus("current")
_HpnicfIPSecTunPolicyName_Type = DisplayString
_HpnicfIPSecTunPolicyName_Object = MibTableColumn
hpnicfIPSecTunPolicyName = _HpnicfIPSecTunPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 1, 1, 1, 24),
    _HpnicfIPSecTunPolicyName_Type()
)
hpnicfIPSecTunPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPSecTunPolicyName.setStatus("current")


class _HpnicfIPSecTunPolicyNum_Type(Integer32):
    """Custom type hpnicfIPSecTunPolicyNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpnicfIPSecTunPolicyNum_Type.__name__ = "Integer32"
_HpnicfIPSecTunPolicyNum_Object = MibTableColumn
hpnicfIPSecTunPolicyNum = _HpnicfIPSecTunPolicyNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 1, 1, 1, 25),
    _HpnicfIPSecTunPolicyNum_Type()
)
hpnicfIPSecTunPolicyNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPSecTunPolicyNum.setStatus("current")


class _HpnicfIPSecTunStatus_Type(Integer32):
    """Custom type hpnicfIPSecTunStatus based on Integer32"""
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


_HpnicfIPSecTunStatus_Type.__name__ = "Integer32"
_HpnicfIPSecTunStatus_Object = MibTableColumn
hpnicfIPSecTunStatus = _HpnicfIPSecTunStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 1, 1, 1, 26),
    _HpnicfIPSecTunStatus_Type()
)
hpnicfIPSecTunStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPSecTunStatus.setStatus("current")
_HpnicfIPSecTunnelStatTable_Object = MibTable
hpnicfIPSecTunnelStatTable = _HpnicfIPSecTunnelStatTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 1, 2)
)
if mibBuilder.loadTexts:
    hpnicfIPSecTunnelStatTable.setStatus("current")
_HpnicfIPSecTunnelStatEntry_Object = MibTableRow
hpnicfIPSecTunnelStatEntry = _HpnicfIPSecTunnelStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 1, 2, 1)
)
hpnicfIPSecTunnelStatEntry.setIndexNames(
    (0, "HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecTunIfIndex"),
    (0, "HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecTunEntryIndex"),
    (0, "HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecTunIndex"),
)
if mibBuilder.loadTexts:
    hpnicfIPSecTunnelStatEntry.setStatus("current")
_HpnicfIPSecTunInOctets_Type = Counter64
_HpnicfIPSecTunInOctets_Object = MibTableColumn
hpnicfIPSecTunInOctets = _HpnicfIPSecTunInOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 1, 2, 1, 1),
    _HpnicfIPSecTunInOctets_Type()
)
hpnicfIPSecTunInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPSecTunInOctets.setStatus("current")
_HpnicfIPSecTunInDecompOctets_Type = Counter64
_HpnicfIPSecTunInDecompOctets_Object = MibTableColumn
hpnicfIPSecTunInDecompOctets = _HpnicfIPSecTunInDecompOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 1, 2, 1, 2),
    _HpnicfIPSecTunInDecompOctets_Type()
)
hpnicfIPSecTunInDecompOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPSecTunInDecompOctets.setStatus("current")
_HpnicfIPSecTunInPkts_Type = Counter64
_HpnicfIPSecTunInPkts_Object = MibTableColumn
hpnicfIPSecTunInPkts = _HpnicfIPSecTunInPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 1, 2, 1, 3),
    _HpnicfIPSecTunInPkts_Type()
)
hpnicfIPSecTunInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPSecTunInPkts.setStatus("current")
_HpnicfIPSecTunInDropPkts_Type = Counter64
_HpnicfIPSecTunInDropPkts_Object = MibTableColumn
hpnicfIPSecTunInDropPkts = _HpnicfIPSecTunInDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 1, 2, 1, 4),
    _HpnicfIPSecTunInDropPkts_Type()
)
hpnicfIPSecTunInDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPSecTunInDropPkts.setStatus("current")
_HpnicfIPSecTunInReplayDropPkts_Type = Counter32
_HpnicfIPSecTunInReplayDropPkts_Object = MibTableColumn
hpnicfIPSecTunInReplayDropPkts = _HpnicfIPSecTunInReplayDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 1, 2, 1, 5),
    _HpnicfIPSecTunInReplayDropPkts_Type()
)
hpnicfIPSecTunInReplayDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPSecTunInReplayDropPkts.setStatus("current")
_HpnicfIPSecTunInAuthFails_Type = Counter32
_HpnicfIPSecTunInAuthFails_Object = MibTableColumn
hpnicfIPSecTunInAuthFails = _HpnicfIPSecTunInAuthFails_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 1, 2, 1, 6),
    _HpnicfIPSecTunInAuthFails_Type()
)
hpnicfIPSecTunInAuthFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPSecTunInAuthFails.setStatus("current")
_HpnicfIPSecTunInDecryptFails_Type = Counter32
_HpnicfIPSecTunInDecryptFails_Object = MibTableColumn
hpnicfIPSecTunInDecryptFails = _HpnicfIPSecTunInDecryptFails_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 1, 2, 1, 7),
    _HpnicfIPSecTunInDecryptFails_Type()
)
hpnicfIPSecTunInDecryptFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPSecTunInDecryptFails.setStatus("current")
_HpnicfIPSecTunOutOctets_Type = Counter64
_HpnicfIPSecTunOutOctets_Object = MibTableColumn
hpnicfIPSecTunOutOctets = _HpnicfIPSecTunOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 1, 2, 1, 8),
    _HpnicfIPSecTunOutOctets_Type()
)
hpnicfIPSecTunOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPSecTunOutOctets.setStatus("current")
_HpnicfIPSecTunOutUncompOctets_Type = Counter64
_HpnicfIPSecTunOutUncompOctets_Object = MibTableColumn
hpnicfIPSecTunOutUncompOctets = _HpnicfIPSecTunOutUncompOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 1, 2, 1, 9),
    _HpnicfIPSecTunOutUncompOctets_Type()
)
hpnicfIPSecTunOutUncompOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPSecTunOutUncompOctets.setStatus("current")
_HpnicfIPSecTunOutPkts_Type = Counter64
_HpnicfIPSecTunOutPkts_Object = MibTableColumn
hpnicfIPSecTunOutPkts = _HpnicfIPSecTunOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 1, 2, 1, 10),
    _HpnicfIPSecTunOutPkts_Type()
)
hpnicfIPSecTunOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPSecTunOutPkts.setStatus("current")
_HpnicfIPSecTunOutDropPkts_Type = Counter64
_HpnicfIPSecTunOutDropPkts_Object = MibTableColumn
hpnicfIPSecTunOutDropPkts = _HpnicfIPSecTunOutDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 1, 2, 1, 11),
    _HpnicfIPSecTunOutDropPkts_Type()
)
hpnicfIPSecTunOutDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPSecTunOutDropPkts.setStatus("current")
_HpnicfIPSecTunOutEncryptFails_Type = Counter32
_HpnicfIPSecTunOutEncryptFails_Object = MibTableColumn
hpnicfIPSecTunOutEncryptFails = _HpnicfIPSecTunOutEncryptFails_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 1, 2, 1, 12),
    _HpnicfIPSecTunOutEncryptFails_Type()
)
hpnicfIPSecTunOutEncryptFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPSecTunOutEncryptFails.setStatus("current")
_HpnicfIPSecTunNoMemoryDropPkts_Type = Counter32
_HpnicfIPSecTunNoMemoryDropPkts_Object = MibTableColumn
hpnicfIPSecTunNoMemoryDropPkts = _HpnicfIPSecTunNoMemoryDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 1, 2, 1, 13),
    _HpnicfIPSecTunNoMemoryDropPkts_Type()
)
hpnicfIPSecTunNoMemoryDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPSecTunNoMemoryDropPkts.setStatus("current")
_HpnicfIPSecTunQueueFullDropPkts_Type = Counter32
_HpnicfIPSecTunQueueFullDropPkts_Object = MibTableColumn
hpnicfIPSecTunQueueFullDropPkts = _HpnicfIPSecTunQueueFullDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 1, 2, 1, 14),
    _HpnicfIPSecTunQueueFullDropPkts_Type()
)
hpnicfIPSecTunQueueFullDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPSecTunQueueFullDropPkts.setStatus("current")
_HpnicfIPSecTunInvalidLenDropPkts_Type = Counter32
_HpnicfIPSecTunInvalidLenDropPkts_Object = MibTableColumn
hpnicfIPSecTunInvalidLenDropPkts = _HpnicfIPSecTunInvalidLenDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 1, 2, 1, 15),
    _HpnicfIPSecTunInvalidLenDropPkts_Type()
)
hpnicfIPSecTunInvalidLenDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPSecTunInvalidLenDropPkts.setStatus("current")
_HpnicfIPSecTunTooLongDropPkts_Type = Counter32
_HpnicfIPSecTunTooLongDropPkts_Object = MibTableColumn
hpnicfIPSecTunTooLongDropPkts = _HpnicfIPSecTunTooLongDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 1, 2, 1, 16),
    _HpnicfIPSecTunTooLongDropPkts_Type()
)
hpnicfIPSecTunTooLongDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPSecTunTooLongDropPkts.setStatus("current")
_HpnicfIPSecTunInvalidSaDropPkts_Type = Counter32
_HpnicfIPSecTunInvalidSaDropPkts_Object = MibTableColumn
hpnicfIPSecTunInvalidSaDropPkts = _HpnicfIPSecTunInvalidSaDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 1, 2, 1, 17),
    _HpnicfIPSecTunInvalidSaDropPkts_Type()
)
hpnicfIPSecTunInvalidSaDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPSecTunInvalidSaDropPkts.setStatus("current")
_HpnicfIPSecSaTable_Object = MibTable
hpnicfIPSecSaTable = _HpnicfIPSecSaTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 1, 3)
)
if mibBuilder.loadTexts:
    hpnicfIPSecSaTable.setStatus("current")
_HpnicfIPSecSaEntry_Object = MibTableRow
hpnicfIPSecSaEntry = _HpnicfIPSecSaEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 1, 3, 1)
)
hpnicfIPSecSaEntry.setIndexNames(
    (0, "HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecTunIfIndex"),
    (0, "HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecTunEntryIndex"),
    (0, "HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecTunIndex"),
    (0, "HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecSaIndex"),
)
if mibBuilder.loadTexts:
    hpnicfIPSecSaEntry.setStatus("current")


class _HpnicfIPSecSaIndex_Type(Integer32):
    """Custom type hpnicfIPSecSaIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpnicfIPSecSaIndex_Type.__name__ = "Integer32"
_HpnicfIPSecSaIndex_Object = MibTableColumn
hpnicfIPSecSaIndex = _HpnicfIPSecSaIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 1, 3, 1, 1),
    _HpnicfIPSecSaIndex_Type()
)
hpnicfIPSecSaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfIPSecSaIndex.setStatus("current")


class _HpnicfIPSecSaDirection_Type(Integer32):
    """Custom type hpnicfIPSecSaDirection based on Integer32"""
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


_HpnicfIPSecSaDirection_Type.__name__ = "Integer32"
_HpnicfIPSecSaDirection_Object = MibTableColumn
hpnicfIPSecSaDirection = _HpnicfIPSecSaDirection_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 1, 3, 1, 2),
    _HpnicfIPSecSaDirection_Type()
)
hpnicfIPSecSaDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPSecSaDirection.setStatus("current")


class _HpnicfIPSecSaValue_Type(Unsigned32):
    """Custom type hpnicfIPSecSaValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_HpnicfIPSecSaValue_Type.__name__ = "Unsigned32"
_HpnicfIPSecSaValue_Object = MibTableColumn
hpnicfIPSecSaValue = _HpnicfIPSecSaValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 1, 3, 1, 3),
    _HpnicfIPSecSaValue_Type()
)
hpnicfIPSecSaValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPSecSaValue.setStatus("current")
_HpnicfIPSecSaProtocol_Type = HpnicfSaProtocol
_HpnicfIPSecSaProtocol_Object = MibTableColumn
hpnicfIPSecSaProtocol = _HpnicfIPSecSaProtocol_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 1, 3, 1, 4),
    _HpnicfIPSecSaProtocol_Type()
)
hpnicfIPSecSaProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPSecSaProtocol.setStatus("current")
_HpnicfIPSecSaEncryptAlgo_Type = HpnicfEncryptAlgo
_HpnicfIPSecSaEncryptAlgo_Object = MibTableColumn
hpnicfIPSecSaEncryptAlgo = _HpnicfIPSecSaEncryptAlgo_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 1, 3, 1, 5),
    _HpnicfIPSecSaEncryptAlgo_Type()
)
hpnicfIPSecSaEncryptAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPSecSaEncryptAlgo.setStatus("current")
_HpnicfIPSecSaAuthAlgo_Type = HpnicfAuthAlgo
_HpnicfIPSecSaAuthAlgo_Object = MibTableColumn
hpnicfIPSecSaAuthAlgo = _HpnicfIPSecSaAuthAlgo_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 1, 3, 1, 6),
    _HpnicfIPSecSaAuthAlgo_Type()
)
hpnicfIPSecSaAuthAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPSecSaAuthAlgo.setStatus("current")


class _HpnicfIPSecSaStatus_Type(Integer32):
    """Custom type hpnicfIPSecSaStatus based on Integer32"""
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


_HpnicfIPSecSaStatus_Type.__name__ = "Integer32"
_HpnicfIPSecSaStatus_Object = MibTableColumn
hpnicfIPSecSaStatus = _HpnicfIPSecSaStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 1, 3, 1, 7),
    _HpnicfIPSecSaStatus_Type()
)
hpnicfIPSecSaStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPSecSaStatus.setStatus("current")
_HpnicfIPSecTrafficTable_Object = MibTable
hpnicfIPSecTrafficTable = _HpnicfIPSecTrafficTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 1, 4)
)
if mibBuilder.loadTexts:
    hpnicfIPSecTrafficTable.setStatus("current")
_HpnicfIPSecTrafficEntry_Object = MibTableRow
hpnicfIPSecTrafficEntry = _HpnicfIPSecTrafficEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 1, 4, 1)
)
hpnicfIPSecTrafficEntry.setIndexNames(
    (0, "HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecTunIfIndex"),
    (0, "HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecTunEntryIndex"),
    (0, "HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecTunIndex"),
)
if mibBuilder.loadTexts:
    hpnicfIPSecTrafficEntry.setStatus("current")
_HpnicfIPSecTrafficLocalType_Type = HpnicfTrafficType
_HpnicfIPSecTrafficLocalType_Object = MibTableColumn
hpnicfIPSecTrafficLocalType = _HpnicfIPSecTrafficLocalType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 1, 4, 1, 1),
    _HpnicfIPSecTrafficLocalType_Type()
)
hpnicfIPSecTrafficLocalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPSecTrafficLocalType.setStatus("current")
_HpnicfIPSecTrafficLocalAddr1_Type = IpAddress
_HpnicfIPSecTrafficLocalAddr1_Object = MibTableColumn
hpnicfIPSecTrafficLocalAddr1 = _HpnicfIPSecTrafficLocalAddr1_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 1, 4, 1, 2),
    _HpnicfIPSecTrafficLocalAddr1_Type()
)
hpnicfIPSecTrafficLocalAddr1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPSecTrafficLocalAddr1.setStatus("current")
_HpnicfIPSecTrafficLocalAddr2_Type = IpAddress
_HpnicfIPSecTrafficLocalAddr2_Object = MibTableColumn
hpnicfIPSecTrafficLocalAddr2 = _HpnicfIPSecTrafficLocalAddr2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 1, 4, 1, 3),
    _HpnicfIPSecTrafficLocalAddr2_Type()
)
hpnicfIPSecTrafficLocalAddr2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPSecTrafficLocalAddr2.setStatus("current")


class _HpnicfIPSecTrafficLocalProtocol_Type(Integer32):
    """Custom type hpnicfIPSecTrafficLocalProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpnicfIPSecTrafficLocalProtocol_Type.__name__ = "Integer32"
_HpnicfIPSecTrafficLocalProtocol_Object = MibTableColumn
hpnicfIPSecTrafficLocalProtocol = _HpnicfIPSecTrafficLocalProtocol_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 1, 4, 1, 4),
    _HpnicfIPSecTrafficLocalProtocol_Type()
)
hpnicfIPSecTrafficLocalProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPSecTrafficLocalProtocol.setStatus("current")


class _HpnicfIPSecTrafficLocalPort_Type(Integer32):
    """Custom type hpnicfIPSecTrafficLocalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfIPSecTrafficLocalPort_Type.__name__ = "Integer32"
_HpnicfIPSecTrafficLocalPort_Object = MibTableColumn
hpnicfIPSecTrafficLocalPort = _HpnicfIPSecTrafficLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 1, 4, 1, 5),
    _HpnicfIPSecTrafficLocalPort_Type()
)
hpnicfIPSecTrafficLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPSecTrafficLocalPort.setStatus("current")
_HpnicfIPSecTrafficRemoteType_Type = HpnicfTrafficType
_HpnicfIPSecTrafficRemoteType_Object = MibTableColumn
hpnicfIPSecTrafficRemoteType = _HpnicfIPSecTrafficRemoteType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 1, 4, 1, 6),
    _HpnicfIPSecTrafficRemoteType_Type()
)
hpnicfIPSecTrafficRemoteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPSecTrafficRemoteType.setStatus("current")
_HpnicfIPSecTrafficRemoteAddr1_Type = IpAddress
_HpnicfIPSecTrafficRemoteAddr1_Object = MibTableColumn
hpnicfIPSecTrafficRemoteAddr1 = _HpnicfIPSecTrafficRemoteAddr1_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 1, 4, 1, 7),
    _HpnicfIPSecTrafficRemoteAddr1_Type()
)
hpnicfIPSecTrafficRemoteAddr1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPSecTrafficRemoteAddr1.setStatus("current")
_HpnicfIPSecTrafficRemoteAddr2_Type = IpAddress
_HpnicfIPSecTrafficRemoteAddr2_Object = MibTableColumn
hpnicfIPSecTrafficRemoteAddr2 = _HpnicfIPSecTrafficRemoteAddr2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 1, 4, 1, 8),
    _HpnicfIPSecTrafficRemoteAddr2_Type()
)
hpnicfIPSecTrafficRemoteAddr2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPSecTrafficRemoteAddr2.setStatus("current")


class _HpnicfIPSecTrafficRemoteProtocol_Type(Integer32):
    """Custom type hpnicfIPSecTrafficRemoteProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpnicfIPSecTrafficRemoteProtocol_Type.__name__ = "Integer32"
_HpnicfIPSecTrafficRemoteProtocol_Object = MibTableColumn
hpnicfIPSecTrafficRemoteProtocol = _HpnicfIPSecTrafficRemoteProtocol_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 1, 4, 1, 9),
    _HpnicfIPSecTrafficRemoteProtocol_Type()
)
hpnicfIPSecTrafficRemoteProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPSecTrafficRemoteProtocol.setStatus("current")


class _HpnicfIPSecTrafficRemotePort_Type(Integer32):
    """Custom type hpnicfIPSecTrafficRemotePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfIPSecTrafficRemotePort_Type.__name__ = "Integer32"
_HpnicfIPSecTrafficRemotePort_Object = MibTableColumn
hpnicfIPSecTrafficRemotePort = _HpnicfIPSecTrafficRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 1, 4, 1, 10),
    _HpnicfIPSecTrafficRemotePort_Type()
)
hpnicfIPSecTrafficRemotePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPSecTrafficRemotePort.setStatus("current")
_HpnicfIPSecGlobalStats_ObjectIdentity = ObjectIdentity
hpnicfIPSecGlobalStats = _HpnicfIPSecGlobalStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 1, 5)
)
_HpnicfIPSecGlobalActiveTunnels_Type = Gauge32
_HpnicfIPSecGlobalActiveTunnels_Object = MibScalar
hpnicfIPSecGlobalActiveTunnels = _HpnicfIPSecGlobalActiveTunnels_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 1, 5, 1),
    _HpnicfIPSecGlobalActiveTunnels_Type()
)
hpnicfIPSecGlobalActiveTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPSecGlobalActiveTunnels.setStatus("current")
_HpnicfIPSecGlobalActiveSas_Type = Gauge32
_HpnicfIPSecGlobalActiveSas_Object = MibScalar
hpnicfIPSecGlobalActiveSas = _HpnicfIPSecGlobalActiveSas_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 1, 5, 2),
    _HpnicfIPSecGlobalActiveSas_Type()
)
hpnicfIPSecGlobalActiveSas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPSecGlobalActiveSas.setStatus("current")
_HpnicfIPSecGlobalInOctets_Type = Counter64
_HpnicfIPSecGlobalInOctets_Object = MibScalar
hpnicfIPSecGlobalInOctets = _HpnicfIPSecGlobalInOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 1, 5, 3),
    _HpnicfIPSecGlobalInOctets_Type()
)
hpnicfIPSecGlobalInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPSecGlobalInOctets.setStatus("current")
_HpnicfIPSecGlobalInDecompOctets_Type = Counter64
_HpnicfIPSecGlobalInDecompOctets_Object = MibScalar
hpnicfIPSecGlobalInDecompOctets = _HpnicfIPSecGlobalInDecompOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 1, 5, 4),
    _HpnicfIPSecGlobalInDecompOctets_Type()
)
hpnicfIPSecGlobalInDecompOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPSecGlobalInDecompOctets.setStatus("current")
_HpnicfIPSecGlobalInPkts_Type = Counter64
_HpnicfIPSecGlobalInPkts_Object = MibScalar
hpnicfIPSecGlobalInPkts = _HpnicfIPSecGlobalInPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 1, 5, 5),
    _HpnicfIPSecGlobalInPkts_Type()
)
hpnicfIPSecGlobalInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPSecGlobalInPkts.setStatus("current")
_HpnicfIPSecGlobalInDrops_Type = Counter64
_HpnicfIPSecGlobalInDrops_Object = MibScalar
hpnicfIPSecGlobalInDrops = _HpnicfIPSecGlobalInDrops_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 1, 5, 6),
    _HpnicfIPSecGlobalInDrops_Type()
)
hpnicfIPSecGlobalInDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPSecGlobalInDrops.setStatus("current")
_HpnicfIPSecGlobalInReplayDrops_Type = Counter32
_HpnicfIPSecGlobalInReplayDrops_Object = MibScalar
hpnicfIPSecGlobalInReplayDrops = _HpnicfIPSecGlobalInReplayDrops_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 1, 5, 7),
    _HpnicfIPSecGlobalInReplayDrops_Type()
)
hpnicfIPSecGlobalInReplayDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPSecGlobalInReplayDrops.setStatus("current")
_HpnicfIPSecGlobalInAuthFails_Type = Counter32
_HpnicfIPSecGlobalInAuthFails_Object = MibScalar
hpnicfIPSecGlobalInAuthFails = _HpnicfIPSecGlobalInAuthFails_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 1, 5, 8),
    _HpnicfIPSecGlobalInAuthFails_Type()
)
hpnicfIPSecGlobalInAuthFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPSecGlobalInAuthFails.setStatus("current")
_HpnicfIPSecGlobalInDecryptFails_Type = Counter32
_HpnicfIPSecGlobalInDecryptFails_Object = MibScalar
hpnicfIPSecGlobalInDecryptFails = _HpnicfIPSecGlobalInDecryptFails_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 1, 5, 9),
    _HpnicfIPSecGlobalInDecryptFails_Type()
)
hpnicfIPSecGlobalInDecryptFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPSecGlobalInDecryptFails.setStatus("current")
_HpnicfIPSecGlobalOutOctets_Type = Counter64
_HpnicfIPSecGlobalOutOctets_Object = MibScalar
hpnicfIPSecGlobalOutOctets = _HpnicfIPSecGlobalOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 1, 5, 10),
    _HpnicfIPSecGlobalOutOctets_Type()
)
hpnicfIPSecGlobalOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPSecGlobalOutOctets.setStatus("current")
_HpnicfIPSecGlobalOutUncompOctets_Type = Counter64
_HpnicfIPSecGlobalOutUncompOctets_Object = MibScalar
hpnicfIPSecGlobalOutUncompOctets = _HpnicfIPSecGlobalOutUncompOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 1, 5, 11),
    _HpnicfIPSecGlobalOutUncompOctets_Type()
)
hpnicfIPSecGlobalOutUncompOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPSecGlobalOutUncompOctets.setStatus("current")
_HpnicfIPSecGlobalOutPkts_Type = Counter64
_HpnicfIPSecGlobalOutPkts_Object = MibScalar
hpnicfIPSecGlobalOutPkts = _HpnicfIPSecGlobalOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 1, 5, 12),
    _HpnicfIPSecGlobalOutPkts_Type()
)
hpnicfIPSecGlobalOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPSecGlobalOutPkts.setStatus("current")
_HpnicfIPSecGlobalOutDrops_Type = Counter64
_HpnicfIPSecGlobalOutDrops_Object = MibScalar
hpnicfIPSecGlobalOutDrops = _HpnicfIPSecGlobalOutDrops_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 1, 5, 13),
    _HpnicfIPSecGlobalOutDrops_Type()
)
hpnicfIPSecGlobalOutDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPSecGlobalOutDrops.setStatus("current")
_HpnicfIPSecGlobalOutEncryptFails_Type = Counter32
_HpnicfIPSecGlobalOutEncryptFails_Object = MibScalar
hpnicfIPSecGlobalOutEncryptFails = _HpnicfIPSecGlobalOutEncryptFails_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 1, 5, 14),
    _HpnicfIPSecGlobalOutEncryptFails_Type()
)
hpnicfIPSecGlobalOutEncryptFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPSecGlobalOutEncryptFails.setStatus("current")
_HpnicfIPSecGlobalNoMemoryDropPkts_Type = Counter32
_HpnicfIPSecGlobalNoMemoryDropPkts_Object = MibScalar
hpnicfIPSecGlobalNoMemoryDropPkts = _HpnicfIPSecGlobalNoMemoryDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 1, 5, 15),
    _HpnicfIPSecGlobalNoMemoryDropPkts_Type()
)
hpnicfIPSecGlobalNoMemoryDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPSecGlobalNoMemoryDropPkts.setStatus("current")
_HpnicfIPSecGlobalNoFindSaDropPkts_Type = Counter32
_HpnicfIPSecGlobalNoFindSaDropPkts_Object = MibScalar
hpnicfIPSecGlobalNoFindSaDropPkts = _HpnicfIPSecGlobalNoFindSaDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 1, 5, 16),
    _HpnicfIPSecGlobalNoFindSaDropPkts_Type()
)
hpnicfIPSecGlobalNoFindSaDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPSecGlobalNoFindSaDropPkts.setStatus("current")
_HpnicfIPSecGlobalQueueFullDropPkts_Type = Counter32
_HpnicfIPSecGlobalQueueFullDropPkts_Object = MibScalar
hpnicfIPSecGlobalQueueFullDropPkts = _HpnicfIPSecGlobalQueueFullDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 1, 5, 17),
    _HpnicfIPSecGlobalQueueFullDropPkts_Type()
)
hpnicfIPSecGlobalQueueFullDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPSecGlobalQueueFullDropPkts.setStatus("current")
_HpnicfIPSecGlobalInvalidLenDropPkts_Type = Counter32
_HpnicfIPSecGlobalInvalidLenDropPkts_Object = MibScalar
hpnicfIPSecGlobalInvalidLenDropPkts = _HpnicfIPSecGlobalInvalidLenDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 1, 5, 18),
    _HpnicfIPSecGlobalInvalidLenDropPkts_Type()
)
hpnicfIPSecGlobalInvalidLenDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPSecGlobalInvalidLenDropPkts.setStatus("current")
_HpnicfIPSecGlobalTooLongDropPkts_Type = Counter32
_HpnicfIPSecGlobalTooLongDropPkts_Object = MibScalar
hpnicfIPSecGlobalTooLongDropPkts = _HpnicfIPSecGlobalTooLongDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 1, 5, 19),
    _HpnicfIPSecGlobalTooLongDropPkts_Type()
)
hpnicfIPSecGlobalTooLongDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPSecGlobalTooLongDropPkts.setStatus("current")
_HpnicfIPSecGlobalInvalidSaDropPkts_Type = Counter32
_HpnicfIPSecGlobalInvalidSaDropPkts_Object = MibScalar
hpnicfIPSecGlobalInvalidSaDropPkts = _HpnicfIPSecGlobalInvalidSaDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 1, 5, 20),
    _HpnicfIPSecGlobalInvalidSaDropPkts_Type()
)
hpnicfIPSecGlobalInvalidSaDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIPSecGlobalInvalidSaDropPkts.setStatus("current")
_HpnicfIPSecTrapObject_ObjectIdentity = ObjectIdentity
hpnicfIPSecTrapObject = _HpnicfIPSecTrapObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 1, 6)
)
_HpnicfIPSecPolicyName_Type = DisplayString
_HpnicfIPSecPolicyName_Object = MibScalar
hpnicfIPSecPolicyName = _HpnicfIPSecPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 1, 6, 1),
    _HpnicfIPSecPolicyName_Type()
)
hpnicfIPSecPolicyName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfIPSecPolicyName.setStatus("current")
_HpnicfIPSecPolicySeqNum_Type = Integer32
_HpnicfIPSecPolicySeqNum_Object = MibScalar
hpnicfIPSecPolicySeqNum = _HpnicfIPSecPolicySeqNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 1, 6, 2),
    _HpnicfIPSecPolicySeqNum_Type()
)
hpnicfIPSecPolicySeqNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfIPSecPolicySeqNum.setStatus("current")
_HpnicfIPSecPolicySize_Type = Integer32
_HpnicfIPSecPolicySize_Object = MibScalar
hpnicfIPSecPolicySize = _HpnicfIPSecPolicySize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 1, 6, 3),
    _HpnicfIPSecPolicySize_Type()
)
hpnicfIPSecPolicySize.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfIPSecPolicySize.setStatus("current")
_HpnicfIPSecSpiValue_Type = Integer32
_HpnicfIPSecSpiValue_Object = MibScalar
hpnicfIPSecSpiValue = _HpnicfIPSecSpiValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 1, 6, 4),
    _HpnicfIPSecSpiValue_Type()
)
hpnicfIPSecSpiValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfIPSecSpiValue.setStatus("current")
_HpnicfIPSecTrapCntl_ObjectIdentity = ObjectIdentity
hpnicfIPSecTrapCntl = _HpnicfIPSecTrapCntl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 1, 7)
)
_HpnicfIPSecTrapGlobalCntl_Type = HpnicfTrapStatus
_HpnicfIPSecTrapGlobalCntl_Object = MibScalar
hpnicfIPSecTrapGlobalCntl = _HpnicfIPSecTrapGlobalCntl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 1, 7, 1),
    _HpnicfIPSecTrapGlobalCntl_Type()
)
hpnicfIPSecTrapGlobalCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfIPSecTrapGlobalCntl.setStatus("current")
_HpnicfIPSecTunnelStartTrapCntl_Type = HpnicfTrapStatus
_HpnicfIPSecTunnelStartTrapCntl_Object = MibScalar
hpnicfIPSecTunnelStartTrapCntl = _HpnicfIPSecTunnelStartTrapCntl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 1, 7, 2),
    _HpnicfIPSecTunnelStartTrapCntl_Type()
)
hpnicfIPSecTunnelStartTrapCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfIPSecTunnelStartTrapCntl.setStatus("current")
_HpnicfIPSecTunnelStopTrapCntl_Type = HpnicfTrapStatus
_HpnicfIPSecTunnelStopTrapCntl_Object = MibScalar
hpnicfIPSecTunnelStopTrapCntl = _HpnicfIPSecTunnelStopTrapCntl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 1, 7, 3),
    _HpnicfIPSecTunnelStopTrapCntl_Type()
)
hpnicfIPSecTunnelStopTrapCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfIPSecTunnelStopTrapCntl.setStatus("current")
_HpnicfIPSecNoSaTrapCntl_Type = HpnicfTrapStatus
_HpnicfIPSecNoSaTrapCntl_Object = MibScalar
hpnicfIPSecNoSaTrapCntl = _HpnicfIPSecNoSaTrapCntl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 1, 7, 4),
    _HpnicfIPSecNoSaTrapCntl_Type()
)
hpnicfIPSecNoSaTrapCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfIPSecNoSaTrapCntl.setStatus("current")
_HpnicfIPSecAuthFailureTrapCntl_Type = HpnicfTrapStatus
_HpnicfIPSecAuthFailureTrapCntl_Object = MibScalar
hpnicfIPSecAuthFailureTrapCntl = _HpnicfIPSecAuthFailureTrapCntl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 1, 7, 5),
    _HpnicfIPSecAuthFailureTrapCntl_Type()
)
hpnicfIPSecAuthFailureTrapCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfIPSecAuthFailureTrapCntl.setStatus("current")
_HpnicfIPSecEncryFailureTrapCntl_Type = HpnicfTrapStatus
_HpnicfIPSecEncryFailureTrapCntl_Object = MibScalar
hpnicfIPSecEncryFailureTrapCntl = _HpnicfIPSecEncryFailureTrapCntl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 1, 7, 6),
    _HpnicfIPSecEncryFailureTrapCntl_Type()
)
hpnicfIPSecEncryFailureTrapCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfIPSecEncryFailureTrapCntl.setStatus("current")
_HpnicfIPSecDecryFailureTrapCntl_Type = HpnicfTrapStatus
_HpnicfIPSecDecryFailureTrapCntl_Object = MibScalar
hpnicfIPSecDecryFailureTrapCntl = _HpnicfIPSecDecryFailureTrapCntl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 1, 7, 7),
    _HpnicfIPSecDecryFailureTrapCntl_Type()
)
hpnicfIPSecDecryFailureTrapCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfIPSecDecryFailureTrapCntl.setStatus("current")
_HpnicfIPSecInvalidSaTrapCntl_Type = HpnicfTrapStatus
_HpnicfIPSecInvalidSaTrapCntl_Object = MibScalar
hpnicfIPSecInvalidSaTrapCntl = _HpnicfIPSecInvalidSaTrapCntl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 1, 7, 8),
    _HpnicfIPSecInvalidSaTrapCntl_Type()
)
hpnicfIPSecInvalidSaTrapCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfIPSecInvalidSaTrapCntl.setStatus("current")
_HpnicfIPSecPolicyAddTrapCntl_Type = HpnicfTrapStatus
_HpnicfIPSecPolicyAddTrapCntl_Object = MibScalar
hpnicfIPSecPolicyAddTrapCntl = _HpnicfIPSecPolicyAddTrapCntl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 1, 7, 9),
    _HpnicfIPSecPolicyAddTrapCntl_Type()
)
hpnicfIPSecPolicyAddTrapCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfIPSecPolicyAddTrapCntl.setStatus("current")
_HpnicfIPSecPolicyDelTrapCntl_Type = HpnicfTrapStatus
_HpnicfIPSecPolicyDelTrapCntl_Object = MibScalar
hpnicfIPSecPolicyDelTrapCntl = _HpnicfIPSecPolicyDelTrapCntl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 1, 7, 10),
    _HpnicfIPSecPolicyDelTrapCntl_Type()
)
hpnicfIPSecPolicyDelTrapCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfIPSecPolicyDelTrapCntl.setStatus("current")
_HpnicfIPSecPolicyAttachTrapCntl_Type = HpnicfTrapStatus
_HpnicfIPSecPolicyAttachTrapCntl_Object = MibScalar
hpnicfIPSecPolicyAttachTrapCntl = _HpnicfIPSecPolicyAttachTrapCntl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 1, 7, 11),
    _HpnicfIPSecPolicyAttachTrapCntl_Type()
)
hpnicfIPSecPolicyAttachTrapCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfIPSecPolicyAttachTrapCntl.setStatus("current")
_HpnicfIPSecPolicyDetachTrapCntl_Type = HpnicfTrapStatus
_HpnicfIPSecPolicyDetachTrapCntl_Object = MibScalar
hpnicfIPSecPolicyDetachTrapCntl = _HpnicfIPSecPolicyDetachTrapCntl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 1, 7, 12),
    _HpnicfIPSecPolicyDetachTrapCntl_Type()
)
hpnicfIPSecPolicyDetachTrapCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfIPSecPolicyDetachTrapCntl.setStatus("current")
_HpnicfIPSecTrap_ObjectIdentity = ObjectIdentity
hpnicfIPSecTrap = _HpnicfIPSecTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 1, 8)
)
_HpnicfIPSecNotifications_ObjectIdentity = ObjectIdentity
hpnicfIPSecNotifications = _HpnicfIPSecNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 1, 8, 1)
)
_HpnicfIPSecConformance_ObjectIdentity = ObjectIdentity
hpnicfIPSecConformance = _HpnicfIPSecConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 2)
)
_HpnicfIPSecCompliances_ObjectIdentity = ObjectIdentity
hpnicfIPSecCompliances = _HpnicfIPSecCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 2, 1)
)
_HpnicfIPSecGroups_ObjectIdentity = ObjectIdentity
hpnicfIPSecGroups = _HpnicfIPSecGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 2, 2)
)

# Managed Objects groups

hpnicfIPSecTunnelTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 2, 2, 1)
)
hpnicfIPSecTunnelTableGroup.setObjects(
      *(("HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecTunIKETunnelIndex"),
        ("HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecTunLocalAddr"),
        ("HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecTunRemoteAddr"),
        ("HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecTunKeyType"),
        ("HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecTunEncapMode"),
        ("HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecTunInitiator"),
        ("HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecTunLifeSize"),
        ("HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecTunLifeTime"),
        ("HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecTunRemainTime"),
        ("HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecTunActiveTime"),
        ("HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecTunRemainSize"),
        ("HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecTunTotalRefreshes"),
        ("HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecTunCurrentSaInstances"),
        ("HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecTunInSaEncryptAlgo"),
        ("HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecTunInSaAhAuthAlgo"),
        ("HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecTunInSaEspAuthAlgo"),
        ("HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecTunDiffHellmanGrp"),
        ("HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecTunOutSaEncryptAlgo"),
        ("HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecTunOutSaAhAuthAlgo"),
        ("HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecTunOutSaEspAuthAlgo"),
        ("HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecTunPolicyName"),
        ("HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecTunPolicyNum"),
        ("HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecTunStatus"))
)
if mibBuilder.loadTexts:
    hpnicfIPSecTunnelTableGroup.setStatus("current")

hpnicfIPSecTunnelStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 2, 2, 2)
)
hpnicfIPSecTunnelStatGroup.setObjects(
      *(("HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecTunInOctets"),
        ("HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecTunInDecompOctets"),
        ("HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecTunInPkts"),
        ("HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecTunInDropPkts"),
        ("HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecTunInReplayDropPkts"),
        ("HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecTunInAuthFails"),
        ("HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecTunInDecryptFails"),
        ("HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecTunOutOctets"),
        ("HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecTunOutUncompOctets"),
        ("HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecTunOutPkts"),
        ("HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecTunOutDropPkts"),
        ("HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecTunOutEncryptFails"),
        ("HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecTunNoMemoryDropPkts"),
        ("HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecTunQueueFullDropPkts"),
        ("HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecTunInvalidLenDropPkts"),
        ("HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecTunTooLongDropPkts"),
        ("HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecTunInvalidSaDropPkts"))
)
if mibBuilder.loadTexts:
    hpnicfIPSecTunnelStatGroup.setStatus("current")

hpnicfIPSecSaGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 2, 2, 3)
)
hpnicfIPSecSaGroup.setObjects(
      *(("HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecSaDirection"),
        ("HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecSaValue"),
        ("HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecSaProtocol"),
        ("HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecSaEncryptAlgo"),
        ("HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecSaAuthAlgo"),
        ("HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecSaStatus"))
)
if mibBuilder.loadTexts:
    hpnicfIPSecSaGroup.setStatus("current")

hpnicfIPSecTrafficTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 2, 2, 4)
)
hpnicfIPSecTrafficTableGroup.setObjects(
      *(("HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecTrafficLocalType"),
        ("HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecTrafficLocalAddr1"),
        ("HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecTrafficLocalAddr2"),
        ("HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecTrafficLocalProtocol"),
        ("HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecTrafficLocalPort"),
        ("HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecTrafficRemoteType"),
        ("HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecTrafficRemoteAddr1"),
        ("HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecTrafficRemoteAddr2"),
        ("HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecTrafficRemoteProtocol"),
        ("HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecTrafficRemotePort"))
)
if mibBuilder.loadTexts:
    hpnicfIPSecTrafficTableGroup.setStatus("current")

hpnicfIPSecGlobalStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 2, 2, 5)
)
hpnicfIPSecGlobalStatsGroup.setObjects(
      *(("HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecGlobalActiveTunnels"),
        ("HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecGlobalActiveSas"),
        ("HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecGlobalInOctets"),
        ("HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecGlobalInDecompOctets"),
        ("HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecGlobalInPkts"),
        ("HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecGlobalInDrops"),
        ("HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecGlobalInReplayDrops"),
        ("HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecGlobalInAuthFails"),
        ("HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecGlobalInDecryptFails"),
        ("HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecGlobalOutOctets"),
        ("HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecGlobalOutUncompOctets"),
        ("HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecGlobalOutPkts"),
        ("HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecGlobalOutDrops"),
        ("HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecGlobalOutEncryptFails"),
        ("HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecGlobalNoMemoryDropPkts"),
        ("HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecGlobalNoFindSaDropPkts"),
        ("HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecGlobalQueueFullDropPkts"),
        ("HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecGlobalInvalidLenDropPkts"),
        ("HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecGlobalTooLongDropPkts"),
        ("HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecGlobalInvalidSaDropPkts"))
)
if mibBuilder.loadTexts:
    hpnicfIPSecGlobalStatsGroup.setStatus("current")

hpnicfIPSecTrapObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 2, 2, 6)
)
hpnicfIPSecTrapObjectGroup.setObjects(
      *(("HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecPolicyName"),
        ("HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecPolicySeqNum"),
        ("HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecPolicySize"),
        ("HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecSpiValue"))
)
if mibBuilder.loadTexts:
    hpnicfIPSecTrapObjectGroup.setStatus("current")

hpnicfIPSecTrapCntlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 2, 2, 7)
)
hpnicfIPSecTrapCntlGroup.setObjects(
      *(("HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecTrapGlobalCntl"),
        ("HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecTunnelStartTrapCntl"),
        ("HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecTunnelStopTrapCntl"),
        ("HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecNoSaTrapCntl"),
        ("HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecAuthFailureTrapCntl"),
        ("HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecEncryFailureTrapCntl"),
        ("HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecDecryFailureTrapCntl"),
        ("HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecInvalidSaTrapCntl"),
        ("HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecPolicyAddTrapCntl"),
        ("HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecPolicyDelTrapCntl"),
        ("HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecPolicyAttachTrapCntl"),
        ("HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecPolicyDetachTrapCntl"))
)
if mibBuilder.loadTexts:
    hpnicfIPSecTrapCntlGroup.setStatus("current")


# Notification objects

hpnicfIPSecTunnelStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 1, 8, 1, 1)
)
hpnicfIPSecTunnelStart.setObjects(
      *(("HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecTunLocalAddr"),
        ("HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecTunRemoteAddr"),
        ("HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecTunLifeTime"),
        ("HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecTunLifeSize"))
)
if mibBuilder.loadTexts:
    hpnicfIPSecTunnelStart.setStatus(
        "current"
    )

hpnicfIPSecTunnelStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 1, 8, 1, 2)
)
hpnicfIPSecTunnelStop.setObjects(
      *(("HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecTunLocalAddr"),
        ("HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecTunRemoteAddr"),
        ("HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecTunActiveTime"))
)
if mibBuilder.loadTexts:
    hpnicfIPSecTunnelStop.setStatus(
        "current"
    )

hpnicfIPSecNoSaFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 1, 8, 1, 3)
)
hpnicfIPSecNoSaFailure.setObjects(
      *(("HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecTunLocalAddr"),
        ("HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecTunRemoteAddr"))
)
if mibBuilder.loadTexts:
    hpnicfIPSecNoSaFailure.setStatus(
        "current"
    )

hpnicfIPSecAuthFailFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 1, 8, 1, 4)
)
hpnicfIPSecAuthFailFailure.setObjects(
      *(("HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecTunLocalAddr"),
        ("HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecTunRemoteAddr"))
)
if mibBuilder.loadTexts:
    hpnicfIPSecAuthFailFailure.setStatus(
        "current"
    )

hpnicfIPSecEncryFailFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 1, 8, 1, 5)
)
hpnicfIPSecEncryFailFailure.setObjects(
      *(("HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecTunLocalAddr"),
        ("HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecTunRemoteAddr"))
)
if mibBuilder.loadTexts:
    hpnicfIPSecEncryFailFailure.setStatus(
        "current"
    )

hpnicfIPSecDecryFailFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 1, 8, 1, 6)
)
hpnicfIPSecDecryFailFailure.setObjects(
      *(("HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecTunLocalAddr"),
        ("HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecTunRemoteAddr"))
)
if mibBuilder.loadTexts:
    hpnicfIPSecDecryFailFailure.setStatus(
        "current"
    )

hpnicfIPSecInvalidSaFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 1, 8, 1, 7)
)
hpnicfIPSecInvalidSaFailure.setObjects(
      *(("HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecTunLocalAddr"),
        ("HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecTunRemoteAddr"),
        ("HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecSpiValue"))
)
if mibBuilder.loadTexts:
    hpnicfIPSecInvalidSaFailure.setStatus(
        "current"
    )

hpnicfIPSecPolicyAdd = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 1, 8, 1, 8)
)
hpnicfIPSecPolicyAdd.setObjects(
      *(("HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecPolicyName"),
        ("HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecPolicySeqNum"),
        ("HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecPolicySize"))
)
if mibBuilder.loadTexts:
    hpnicfIPSecPolicyAdd.setStatus(
        "current"
    )

hpnicfIPSecPolicyDel = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 1, 8, 1, 9)
)
hpnicfIPSecPolicyDel.setObjects(
      *(("HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecPolicyName"),
        ("HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecPolicySeqNum"),
        ("HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecPolicySize"))
)
if mibBuilder.loadTexts:
    hpnicfIPSecPolicyDel.setStatus(
        "current"
    )

hpnicfIPSecPolicyAttach = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 1, 8, 1, 10)
)
hpnicfIPSecPolicyAttach.setObjects(
      *(("HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecPolicyName"),
        ("HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecPolicySize"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    hpnicfIPSecPolicyAttach.setStatus(
        "current"
    )

hpnicfIPSecPolicyDetach = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 1, 8, 1, 11)
)
hpnicfIPSecPolicyDetach.setObjects(
      *(("HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecPolicyName"),
        ("HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecPolicySize"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    hpnicfIPSecPolicyDetach.setStatus(
        "current"
    )


# Notifications groups

hpnicfIPSecTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 2, 2, 8)
)
hpnicfIPSecTrapGroup.setObjects(
      *(("HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecTunnelStart"),
        ("HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecTunnelStop"),
        ("HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecNoSaFailure"),
        ("HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecAuthFailFailure"),
        ("HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecEncryFailFailure"),
        ("HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecDecryFailFailure"),
        ("HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecInvalidSaFailure"),
        ("HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecPolicyAdd"),
        ("HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecPolicyDel"),
        ("HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecPolicyAttach"),
        ("HPN-ICF-IPSEC-MONITOR-MIB", "hpnicfIPSecPolicyDetach"))
)
if mibBuilder.loadTexts:
    hpnicfIPSecTrapGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hpnicfIPSecCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hpnicfIPSecCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-IPSEC-MONITOR-MIB",
    **{"HpnicfDiffHellmanGrp": HpnicfDiffHellmanGrp,
       "HpnicfEncapMode": HpnicfEncapMode,
       "HpnicfEncryptAlgo": HpnicfEncryptAlgo,
       "HpnicfAuthAlgo": HpnicfAuthAlgo,
       "HpnicfSaProtocol": HpnicfSaProtocol,
       "HpnicfTrapStatus": HpnicfTrapStatus,
       "HpnicfIPSecIDType": HpnicfIPSecIDType,
       "HpnicfTrafficType": HpnicfTrafficType,
       "HpnicfIPSecNegoType": HpnicfIPSecNegoType,
       "HpnicfIPSecTunnelState": HpnicfIPSecTunnelState,
       "hpnicfIPSecMonitor": hpnicfIPSecMonitor,
       "hpnicfIPSecObjects": hpnicfIPSecObjects,
       "hpnicfIPSecTunnelTable": hpnicfIPSecTunnelTable,
       "hpnicfIPSecTunnelEntry": hpnicfIPSecTunnelEntry,
       "hpnicfIPSecTunIfIndex": hpnicfIPSecTunIfIndex,
       "hpnicfIPSecTunEntryIndex": hpnicfIPSecTunEntryIndex,
       "hpnicfIPSecTunIndex": hpnicfIPSecTunIndex,
       "hpnicfIPSecTunIKETunnelIndex": hpnicfIPSecTunIKETunnelIndex,
       "hpnicfIPSecTunLocalAddr": hpnicfIPSecTunLocalAddr,
       "hpnicfIPSecTunRemoteAddr": hpnicfIPSecTunRemoteAddr,
       "hpnicfIPSecTunKeyType": hpnicfIPSecTunKeyType,
       "hpnicfIPSecTunEncapMode": hpnicfIPSecTunEncapMode,
       "hpnicfIPSecTunInitiator": hpnicfIPSecTunInitiator,
       "hpnicfIPSecTunLifeSize": hpnicfIPSecTunLifeSize,
       "hpnicfIPSecTunLifeTime": hpnicfIPSecTunLifeTime,
       "hpnicfIPSecTunRemainTime": hpnicfIPSecTunRemainTime,
       "hpnicfIPSecTunActiveTime": hpnicfIPSecTunActiveTime,
       "hpnicfIPSecTunRemainSize": hpnicfIPSecTunRemainSize,
       "hpnicfIPSecTunTotalRefreshes": hpnicfIPSecTunTotalRefreshes,
       "hpnicfIPSecTunCurrentSaInstances": hpnicfIPSecTunCurrentSaInstances,
       "hpnicfIPSecTunInSaEncryptAlgo": hpnicfIPSecTunInSaEncryptAlgo,
       "hpnicfIPSecTunInSaAhAuthAlgo": hpnicfIPSecTunInSaAhAuthAlgo,
       "hpnicfIPSecTunInSaEspAuthAlgo": hpnicfIPSecTunInSaEspAuthAlgo,
       "hpnicfIPSecTunDiffHellmanGrp": hpnicfIPSecTunDiffHellmanGrp,
       "hpnicfIPSecTunOutSaEncryptAlgo": hpnicfIPSecTunOutSaEncryptAlgo,
       "hpnicfIPSecTunOutSaAhAuthAlgo": hpnicfIPSecTunOutSaAhAuthAlgo,
       "hpnicfIPSecTunOutSaEspAuthAlgo": hpnicfIPSecTunOutSaEspAuthAlgo,
       "hpnicfIPSecTunPolicyName": hpnicfIPSecTunPolicyName,
       "hpnicfIPSecTunPolicyNum": hpnicfIPSecTunPolicyNum,
       "hpnicfIPSecTunStatus": hpnicfIPSecTunStatus,
       "hpnicfIPSecTunnelStatTable": hpnicfIPSecTunnelStatTable,
       "hpnicfIPSecTunnelStatEntry": hpnicfIPSecTunnelStatEntry,
       "hpnicfIPSecTunInOctets": hpnicfIPSecTunInOctets,
       "hpnicfIPSecTunInDecompOctets": hpnicfIPSecTunInDecompOctets,
       "hpnicfIPSecTunInPkts": hpnicfIPSecTunInPkts,
       "hpnicfIPSecTunInDropPkts": hpnicfIPSecTunInDropPkts,
       "hpnicfIPSecTunInReplayDropPkts": hpnicfIPSecTunInReplayDropPkts,
       "hpnicfIPSecTunInAuthFails": hpnicfIPSecTunInAuthFails,
       "hpnicfIPSecTunInDecryptFails": hpnicfIPSecTunInDecryptFails,
       "hpnicfIPSecTunOutOctets": hpnicfIPSecTunOutOctets,
       "hpnicfIPSecTunOutUncompOctets": hpnicfIPSecTunOutUncompOctets,
       "hpnicfIPSecTunOutPkts": hpnicfIPSecTunOutPkts,
       "hpnicfIPSecTunOutDropPkts": hpnicfIPSecTunOutDropPkts,
       "hpnicfIPSecTunOutEncryptFails": hpnicfIPSecTunOutEncryptFails,
       "hpnicfIPSecTunNoMemoryDropPkts": hpnicfIPSecTunNoMemoryDropPkts,
       "hpnicfIPSecTunQueueFullDropPkts": hpnicfIPSecTunQueueFullDropPkts,
       "hpnicfIPSecTunInvalidLenDropPkts": hpnicfIPSecTunInvalidLenDropPkts,
       "hpnicfIPSecTunTooLongDropPkts": hpnicfIPSecTunTooLongDropPkts,
       "hpnicfIPSecTunInvalidSaDropPkts": hpnicfIPSecTunInvalidSaDropPkts,
       "hpnicfIPSecSaTable": hpnicfIPSecSaTable,
       "hpnicfIPSecSaEntry": hpnicfIPSecSaEntry,
       "hpnicfIPSecSaIndex": hpnicfIPSecSaIndex,
       "hpnicfIPSecSaDirection": hpnicfIPSecSaDirection,
       "hpnicfIPSecSaValue": hpnicfIPSecSaValue,
       "hpnicfIPSecSaProtocol": hpnicfIPSecSaProtocol,
       "hpnicfIPSecSaEncryptAlgo": hpnicfIPSecSaEncryptAlgo,
       "hpnicfIPSecSaAuthAlgo": hpnicfIPSecSaAuthAlgo,
       "hpnicfIPSecSaStatus": hpnicfIPSecSaStatus,
       "hpnicfIPSecTrafficTable": hpnicfIPSecTrafficTable,
       "hpnicfIPSecTrafficEntry": hpnicfIPSecTrafficEntry,
       "hpnicfIPSecTrafficLocalType": hpnicfIPSecTrafficLocalType,
       "hpnicfIPSecTrafficLocalAddr1": hpnicfIPSecTrafficLocalAddr1,
       "hpnicfIPSecTrafficLocalAddr2": hpnicfIPSecTrafficLocalAddr2,
       "hpnicfIPSecTrafficLocalProtocol": hpnicfIPSecTrafficLocalProtocol,
       "hpnicfIPSecTrafficLocalPort": hpnicfIPSecTrafficLocalPort,
       "hpnicfIPSecTrafficRemoteType": hpnicfIPSecTrafficRemoteType,
       "hpnicfIPSecTrafficRemoteAddr1": hpnicfIPSecTrafficRemoteAddr1,
       "hpnicfIPSecTrafficRemoteAddr2": hpnicfIPSecTrafficRemoteAddr2,
       "hpnicfIPSecTrafficRemoteProtocol": hpnicfIPSecTrafficRemoteProtocol,
       "hpnicfIPSecTrafficRemotePort": hpnicfIPSecTrafficRemotePort,
       "hpnicfIPSecGlobalStats": hpnicfIPSecGlobalStats,
       "hpnicfIPSecGlobalActiveTunnels": hpnicfIPSecGlobalActiveTunnels,
       "hpnicfIPSecGlobalActiveSas": hpnicfIPSecGlobalActiveSas,
       "hpnicfIPSecGlobalInOctets": hpnicfIPSecGlobalInOctets,
       "hpnicfIPSecGlobalInDecompOctets": hpnicfIPSecGlobalInDecompOctets,
       "hpnicfIPSecGlobalInPkts": hpnicfIPSecGlobalInPkts,
       "hpnicfIPSecGlobalInDrops": hpnicfIPSecGlobalInDrops,
       "hpnicfIPSecGlobalInReplayDrops": hpnicfIPSecGlobalInReplayDrops,
       "hpnicfIPSecGlobalInAuthFails": hpnicfIPSecGlobalInAuthFails,
       "hpnicfIPSecGlobalInDecryptFails": hpnicfIPSecGlobalInDecryptFails,
       "hpnicfIPSecGlobalOutOctets": hpnicfIPSecGlobalOutOctets,
       "hpnicfIPSecGlobalOutUncompOctets": hpnicfIPSecGlobalOutUncompOctets,
       "hpnicfIPSecGlobalOutPkts": hpnicfIPSecGlobalOutPkts,
       "hpnicfIPSecGlobalOutDrops": hpnicfIPSecGlobalOutDrops,
       "hpnicfIPSecGlobalOutEncryptFails": hpnicfIPSecGlobalOutEncryptFails,
       "hpnicfIPSecGlobalNoMemoryDropPkts": hpnicfIPSecGlobalNoMemoryDropPkts,
       "hpnicfIPSecGlobalNoFindSaDropPkts": hpnicfIPSecGlobalNoFindSaDropPkts,
       "hpnicfIPSecGlobalQueueFullDropPkts": hpnicfIPSecGlobalQueueFullDropPkts,
       "hpnicfIPSecGlobalInvalidLenDropPkts": hpnicfIPSecGlobalInvalidLenDropPkts,
       "hpnicfIPSecGlobalTooLongDropPkts": hpnicfIPSecGlobalTooLongDropPkts,
       "hpnicfIPSecGlobalInvalidSaDropPkts": hpnicfIPSecGlobalInvalidSaDropPkts,
       "hpnicfIPSecTrapObject": hpnicfIPSecTrapObject,
       "hpnicfIPSecPolicyName": hpnicfIPSecPolicyName,
       "hpnicfIPSecPolicySeqNum": hpnicfIPSecPolicySeqNum,
       "hpnicfIPSecPolicySize": hpnicfIPSecPolicySize,
       "hpnicfIPSecSpiValue": hpnicfIPSecSpiValue,
       "hpnicfIPSecTrapCntl": hpnicfIPSecTrapCntl,
       "hpnicfIPSecTrapGlobalCntl": hpnicfIPSecTrapGlobalCntl,
       "hpnicfIPSecTunnelStartTrapCntl": hpnicfIPSecTunnelStartTrapCntl,
       "hpnicfIPSecTunnelStopTrapCntl": hpnicfIPSecTunnelStopTrapCntl,
       "hpnicfIPSecNoSaTrapCntl": hpnicfIPSecNoSaTrapCntl,
       "hpnicfIPSecAuthFailureTrapCntl": hpnicfIPSecAuthFailureTrapCntl,
       "hpnicfIPSecEncryFailureTrapCntl": hpnicfIPSecEncryFailureTrapCntl,
       "hpnicfIPSecDecryFailureTrapCntl": hpnicfIPSecDecryFailureTrapCntl,
       "hpnicfIPSecInvalidSaTrapCntl": hpnicfIPSecInvalidSaTrapCntl,
       "hpnicfIPSecPolicyAddTrapCntl": hpnicfIPSecPolicyAddTrapCntl,
       "hpnicfIPSecPolicyDelTrapCntl": hpnicfIPSecPolicyDelTrapCntl,
       "hpnicfIPSecPolicyAttachTrapCntl": hpnicfIPSecPolicyAttachTrapCntl,
       "hpnicfIPSecPolicyDetachTrapCntl": hpnicfIPSecPolicyDetachTrapCntl,
       "hpnicfIPSecTrap": hpnicfIPSecTrap,
       "hpnicfIPSecNotifications": hpnicfIPSecNotifications,
       "hpnicfIPSecTunnelStart": hpnicfIPSecTunnelStart,
       "hpnicfIPSecTunnelStop": hpnicfIPSecTunnelStop,
       "hpnicfIPSecNoSaFailure": hpnicfIPSecNoSaFailure,
       "hpnicfIPSecAuthFailFailure": hpnicfIPSecAuthFailFailure,
       "hpnicfIPSecEncryFailFailure": hpnicfIPSecEncryFailFailure,
       "hpnicfIPSecDecryFailFailure": hpnicfIPSecDecryFailFailure,
       "hpnicfIPSecInvalidSaFailure": hpnicfIPSecInvalidSaFailure,
       "hpnicfIPSecPolicyAdd": hpnicfIPSecPolicyAdd,
       "hpnicfIPSecPolicyDel": hpnicfIPSecPolicyDel,
       "hpnicfIPSecPolicyAttach": hpnicfIPSecPolicyAttach,
       "hpnicfIPSecPolicyDetach": hpnicfIPSecPolicyDetach,
       "hpnicfIPSecConformance": hpnicfIPSecConformance,
       "hpnicfIPSecCompliances": hpnicfIPSecCompliances,
       "hpnicfIPSecCompliance": hpnicfIPSecCompliance,
       "hpnicfIPSecGroups": hpnicfIPSecGroups,
       "hpnicfIPSecTunnelTableGroup": hpnicfIPSecTunnelTableGroup,
       "hpnicfIPSecTunnelStatGroup": hpnicfIPSecTunnelStatGroup,
       "hpnicfIPSecSaGroup": hpnicfIPSecSaGroup,
       "hpnicfIPSecTrafficTableGroup": hpnicfIPSecTrafficTableGroup,
       "hpnicfIPSecGlobalStatsGroup": hpnicfIPSecGlobalStatsGroup,
       "hpnicfIPSecTrapObjectGroup": hpnicfIPSecTrapObjectGroup,
       "hpnicfIPSecTrapCntlGroup": hpnicfIPSecTrapCntlGroup,
       "hpnicfIPSecTrapGroup": hpnicfIPSecTrapGroup}
)
