# SNMP MIB module (HH3C-IKE-MONITOR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-IKE-MONITOR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:53:33 2024
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

hh3cIKEMonitor = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Hh3cIKENegoMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              4,
              32)
        )
    )
    namedValues = NamedValues(
        *(("aggressiveMode", 4),
          ("mainMode", 2),
          ("quickMode", 32))
    )



class Hh3cIKEAuthMethod(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("preSharedKey", 1),
          ("rsaSignatures", 3))
    )



class Hh3cDiffHellmanGrp(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              5,
              14)
        )
    )
    namedValues = NamedValues(
        *(("modp1024", 2),
          ("modp1536", 5),
          ("modp2048", 14),
          ("modp768", 1))
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("aesCbc", 7),
          ("aesCbc128", 8),
          ("aesCbc192", 9),
          ("aesCbc256", 10),
          ("blowfishCbc", 3),
          ("castCbc", 6),
          ("desCbc", 1),
          ("ideaCbc", 2),
          ("none", 0),
          ("rc5R16B64Cbc", 4),
          ("tripleDesCbc", 5))
    )



class Hh3cAuthAlgo(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("md5", 1),
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



class Hh3cIKEIDType(Integer32, TextualConvention):
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



class Hh3cIKETunnelState(Integer32, TextualConvention):
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

_Hh3cIKEObjects_ObjectIdentity = ObjectIdentity
hh3cIKEObjects = _Hh3cIKEObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 1)
)
_Hh3cIKETunnelTable_Object = MibTable
hh3cIKETunnelTable = _Hh3cIKETunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cIKETunnelTable.setStatus("current")
_Hh3cIKETunnelEntry_Object = MibTableRow
hh3cIKETunnelEntry = _Hh3cIKETunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 1, 1, 1)
)
hh3cIKETunnelEntry.setIndexNames(
    (0, "HH3C-IKE-MONITOR-MIB", "hh3cIKETunIndex"),
)
if mibBuilder.loadTexts:
    hh3cIKETunnelEntry.setStatus("current")


class _Hh3cIKETunIndex_Type(Integer32):
    """Custom type hh3cIKETunIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cIKETunIndex_Type.__name__ = "Integer32"
_Hh3cIKETunIndex_Object = MibTableColumn
hh3cIKETunIndex = _Hh3cIKETunIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 1, 1, 1, 1),
    _Hh3cIKETunIndex_Type()
)
hh3cIKETunIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cIKETunIndex.setStatus("current")
_Hh3cIKETunLocalType_Type = Hh3cIKEIDType
_Hh3cIKETunLocalType_Object = MibTableColumn
hh3cIKETunLocalType = _Hh3cIKETunLocalType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 1, 1, 1, 2),
    _Hh3cIKETunLocalType_Type()
)
hh3cIKETunLocalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIKETunLocalType.setStatus("current")
_Hh3cIKETunLocalValue1_Type = DisplayString
_Hh3cIKETunLocalValue1_Object = MibTableColumn
hh3cIKETunLocalValue1 = _Hh3cIKETunLocalValue1_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 1, 1, 1, 3),
    _Hh3cIKETunLocalValue1_Type()
)
hh3cIKETunLocalValue1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIKETunLocalValue1.setStatus("current")
_Hh3cIKETunLocalValue2_Type = DisplayString
_Hh3cIKETunLocalValue2_Object = MibTableColumn
hh3cIKETunLocalValue2 = _Hh3cIKETunLocalValue2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 1, 1, 1, 4),
    _Hh3cIKETunLocalValue2_Type()
)
hh3cIKETunLocalValue2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIKETunLocalValue2.setStatus("current")
_Hh3cIKETunLocalAddr_Type = IpAddress
_Hh3cIKETunLocalAddr_Object = MibTableColumn
hh3cIKETunLocalAddr = _Hh3cIKETunLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 1, 1, 1, 5),
    _Hh3cIKETunLocalAddr_Type()
)
hh3cIKETunLocalAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIKETunLocalAddr.setStatus("current")
_Hh3cIKETunRemoteType_Type = Hh3cIKEIDType
_Hh3cIKETunRemoteType_Object = MibTableColumn
hh3cIKETunRemoteType = _Hh3cIKETunRemoteType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 1, 1, 1, 6),
    _Hh3cIKETunRemoteType_Type()
)
hh3cIKETunRemoteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIKETunRemoteType.setStatus("current")
_Hh3cIKETunRemoteValue1_Type = DisplayString
_Hh3cIKETunRemoteValue1_Object = MibTableColumn
hh3cIKETunRemoteValue1 = _Hh3cIKETunRemoteValue1_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 1, 1, 1, 7),
    _Hh3cIKETunRemoteValue1_Type()
)
hh3cIKETunRemoteValue1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIKETunRemoteValue1.setStatus("current")
_Hh3cIKETunRemoteValue2_Type = DisplayString
_Hh3cIKETunRemoteValue2_Object = MibTableColumn
hh3cIKETunRemoteValue2 = _Hh3cIKETunRemoteValue2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 1, 1, 1, 8),
    _Hh3cIKETunRemoteValue2_Type()
)
hh3cIKETunRemoteValue2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIKETunRemoteValue2.setStatus("current")
_Hh3cIKETunRemoteAddr_Type = IpAddress
_Hh3cIKETunRemoteAddr_Object = MibTableColumn
hh3cIKETunRemoteAddr = _Hh3cIKETunRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 1, 1, 1, 9),
    _Hh3cIKETunRemoteAddr_Type()
)
hh3cIKETunRemoteAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIKETunRemoteAddr.setStatus("current")


class _Hh3cIKETunInitiator_Type(Integer32):
    """Custom type hh3cIKETunInitiator based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("remote", 2))
    )


_Hh3cIKETunInitiator_Type.__name__ = "Integer32"
_Hh3cIKETunInitiator_Object = MibTableColumn
hh3cIKETunInitiator = _Hh3cIKETunInitiator_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 1, 1, 1, 10),
    _Hh3cIKETunInitiator_Type()
)
hh3cIKETunInitiator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIKETunInitiator.setStatus("current")
_Hh3cIKETunNegoMode_Type = Hh3cIKENegoMode
_Hh3cIKETunNegoMode_Object = MibTableColumn
hh3cIKETunNegoMode = _Hh3cIKETunNegoMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 1, 1, 1, 11),
    _Hh3cIKETunNegoMode_Type()
)
hh3cIKETunNegoMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIKETunNegoMode.setStatus("current")
_Hh3cIKETunDiffHellmanGrp_Type = Hh3cDiffHellmanGrp
_Hh3cIKETunDiffHellmanGrp_Object = MibTableColumn
hh3cIKETunDiffHellmanGrp = _Hh3cIKETunDiffHellmanGrp_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 1, 1, 1, 12),
    _Hh3cIKETunDiffHellmanGrp_Type()
)
hh3cIKETunDiffHellmanGrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIKETunDiffHellmanGrp.setStatus("current")
_Hh3cIKETunEncryptAlgo_Type = Hh3cEncryptAlgo
_Hh3cIKETunEncryptAlgo_Object = MibTableColumn
hh3cIKETunEncryptAlgo = _Hh3cIKETunEncryptAlgo_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 1, 1, 1, 13),
    _Hh3cIKETunEncryptAlgo_Type()
)
hh3cIKETunEncryptAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIKETunEncryptAlgo.setStatus("current")
_Hh3cIKETunHashAlgo_Type = Hh3cAuthAlgo
_Hh3cIKETunHashAlgo_Object = MibTableColumn
hh3cIKETunHashAlgo = _Hh3cIKETunHashAlgo_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 1, 1, 1, 14),
    _Hh3cIKETunHashAlgo_Type()
)
hh3cIKETunHashAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIKETunHashAlgo.setStatus("current")
_Hh3cIKETunAuthMethod_Type = Hh3cIKEAuthMethod
_Hh3cIKETunAuthMethod_Object = MibTableColumn
hh3cIKETunAuthMethod = _Hh3cIKETunAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 1, 1, 1, 15),
    _Hh3cIKETunAuthMethod_Type()
)
hh3cIKETunAuthMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIKETunAuthMethod.setStatus("current")


class _Hh3cIKETunLifeTime_Type(Integer32):
    """Custom type hh3cIKETunLifeTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cIKETunLifeTime_Type.__name__ = "Integer32"
_Hh3cIKETunLifeTime_Object = MibTableColumn
hh3cIKETunLifeTime = _Hh3cIKETunLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 1, 1, 1, 16),
    _Hh3cIKETunLifeTime_Type()
)
hh3cIKETunLifeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIKETunLifeTime.setStatus("current")


class _Hh3cIKETunActiveTime_Type(Integer32):
    """Custom type hh3cIKETunActiveTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cIKETunActiveTime_Type.__name__ = "Integer32"
_Hh3cIKETunActiveTime_Object = MibTableColumn
hh3cIKETunActiveTime = _Hh3cIKETunActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 1, 1, 1, 17),
    _Hh3cIKETunActiveTime_Type()
)
hh3cIKETunActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIKETunActiveTime.setStatus("current")


class _Hh3cIKETunRemainTime_Type(Integer32):
    """Custom type hh3cIKETunRemainTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cIKETunRemainTime_Type.__name__ = "Integer32"
_Hh3cIKETunRemainTime_Object = MibTableColumn
hh3cIKETunRemainTime = _Hh3cIKETunRemainTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 1, 1, 1, 18),
    _Hh3cIKETunRemainTime_Type()
)
hh3cIKETunRemainTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIKETunRemainTime.setStatus("current")
_Hh3cIKETunTotalRefreshes_Type = Counter32
_Hh3cIKETunTotalRefreshes_Object = MibTableColumn
hh3cIKETunTotalRefreshes = _Hh3cIKETunTotalRefreshes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 1, 1, 1, 19),
    _Hh3cIKETunTotalRefreshes_Type()
)
hh3cIKETunTotalRefreshes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIKETunTotalRefreshes.setStatus("current")
_Hh3cIKETunState_Type = Hh3cIKETunnelState
_Hh3cIKETunState_Object = MibTableColumn
hh3cIKETunState = _Hh3cIKETunState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 1, 1, 1, 20),
    _Hh3cIKETunState_Type()
)
hh3cIKETunState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIKETunState.setStatus("current")


class _Hh3cIKETunDpdIntervalTime_Type(Integer32):
    """Custom type hh3cIKETunDpdIntervalTime based on Integer32"""
    defaultValue = 10


_Hh3cIKETunDpdIntervalTime_Object = MibTableColumn
hh3cIKETunDpdIntervalTime = _Hh3cIKETunDpdIntervalTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 1, 1, 1, 21),
    _Hh3cIKETunDpdIntervalTime_Type()
)
hh3cIKETunDpdIntervalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIKETunDpdIntervalTime.setStatus("current")
if mibBuilder.loadTexts:
    hh3cIKETunDpdIntervalTime.setUnits("second")


class _Hh3cIKETunDpdTimeOut_Type(Integer32):
    """Custom type hh3cIKETunDpdTimeOut based on Integer32"""
    defaultValue = 5


_Hh3cIKETunDpdTimeOut_Object = MibTableColumn
hh3cIKETunDpdTimeOut = _Hh3cIKETunDpdTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 1, 1, 1, 22),
    _Hh3cIKETunDpdTimeOut_Type()
)
hh3cIKETunDpdTimeOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIKETunDpdTimeOut.setStatus("current")
if mibBuilder.loadTexts:
    hh3cIKETunDpdTimeOut.setUnits("second")
_Hh3cIKETunnelStatTable_Object = MibTable
hh3cIKETunnelStatTable = _Hh3cIKETunnelStatTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 1, 2)
)
if mibBuilder.loadTexts:
    hh3cIKETunnelStatTable.setStatus("current")
_Hh3cIKETunnelStatEntry_Object = MibTableRow
hh3cIKETunnelStatEntry = _Hh3cIKETunnelStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 1, 2, 1)
)
hh3cIKETunnelStatEntry.setIndexNames(
    (0, "HH3C-IKE-MONITOR-MIB", "hh3cIKETunIndex"),
)
if mibBuilder.loadTexts:
    hh3cIKETunnelStatEntry.setStatus("current")
_Hh3cIKETunInOctets_Type = Counter64
_Hh3cIKETunInOctets_Object = MibTableColumn
hh3cIKETunInOctets = _Hh3cIKETunInOctets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 1, 2, 1, 1),
    _Hh3cIKETunInOctets_Type()
)
hh3cIKETunInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIKETunInOctets.setStatus("current")
_Hh3cIKETunInPkts_Type = Counter64
_Hh3cIKETunInPkts_Object = MibTableColumn
hh3cIKETunInPkts = _Hh3cIKETunInPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 1, 2, 1, 2),
    _Hh3cIKETunInPkts_Type()
)
hh3cIKETunInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIKETunInPkts.setStatus("current")
_Hh3cIKETunInDropPkts_Type = Counter64
_Hh3cIKETunInDropPkts_Object = MibTableColumn
hh3cIKETunInDropPkts = _Hh3cIKETunInDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 1, 2, 1, 3),
    _Hh3cIKETunInDropPkts_Type()
)
hh3cIKETunInDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIKETunInDropPkts.setStatus("current")
_Hh3cIKETunInP2Exchgs_Type = Counter64
_Hh3cIKETunInP2Exchgs_Object = MibTableColumn
hh3cIKETunInP2Exchgs = _Hh3cIKETunInP2Exchgs_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 1, 2, 1, 4),
    _Hh3cIKETunInP2Exchgs_Type()
)
hh3cIKETunInP2Exchgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIKETunInP2Exchgs.setStatus("current")
_Hh3cIKETunInP2ExchgRejets_Type = Counter64
_Hh3cIKETunInP2ExchgRejets_Object = MibTableColumn
hh3cIKETunInP2ExchgRejets = _Hh3cIKETunInP2ExchgRejets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 1, 2, 1, 5),
    _Hh3cIKETunInP2ExchgRejets_Type()
)
hh3cIKETunInP2ExchgRejets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIKETunInP2ExchgRejets.setStatus("current")
_Hh3cIKETunInP2SaDelRequests_Type = Counter64
_Hh3cIKETunInP2SaDelRequests_Object = MibTableColumn
hh3cIKETunInP2SaDelRequests = _Hh3cIKETunInP2SaDelRequests_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 1, 2, 1, 6),
    _Hh3cIKETunInP2SaDelRequests_Type()
)
hh3cIKETunInP2SaDelRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIKETunInP2SaDelRequests.setStatus("current")
_Hh3cIKETunInP1SaDelRequests_Type = Counter64
_Hh3cIKETunInP1SaDelRequests_Object = MibTableColumn
hh3cIKETunInP1SaDelRequests = _Hh3cIKETunInP1SaDelRequests_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 1, 2, 1, 7),
    _Hh3cIKETunInP1SaDelRequests_Type()
)
hh3cIKETunInP1SaDelRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIKETunInP1SaDelRequests.setStatus("current")
_Hh3cIKETunInNotifys_Type = Counter32
_Hh3cIKETunInNotifys_Object = MibTableColumn
hh3cIKETunInNotifys = _Hh3cIKETunInNotifys_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 1, 2, 1, 8),
    _Hh3cIKETunInNotifys_Type()
)
hh3cIKETunInNotifys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIKETunInNotifys.setStatus("current")
_Hh3cIKETunOutOctets_Type = Counter64
_Hh3cIKETunOutOctets_Object = MibTableColumn
hh3cIKETunOutOctets = _Hh3cIKETunOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 1, 2, 1, 9),
    _Hh3cIKETunOutOctets_Type()
)
hh3cIKETunOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIKETunOutOctets.setStatus("current")
_Hh3cIKETunOutPkts_Type = Counter64
_Hh3cIKETunOutPkts_Object = MibTableColumn
hh3cIKETunOutPkts = _Hh3cIKETunOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 1, 2, 1, 10),
    _Hh3cIKETunOutPkts_Type()
)
hh3cIKETunOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIKETunOutPkts.setStatus("current")
_Hh3cIKETunOutDropPkts_Type = Counter64
_Hh3cIKETunOutDropPkts_Object = MibTableColumn
hh3cIKETunOutDropPkts = _Hh3cIKETunOutDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 1, 2, 1, 11),
    _Hh3cIKETunOutDropPkts_Type()
)
hh3cIKETunOutDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIKETunOutDropPkts.setStatus("current")
_Hh3cIKETunOutP2Exchgs_Type = Counter64
_Hh3cIKETunOutP2Exchgs_Object = MibTableColumn
hh3cIKETunOutP2Exchgs = _Hh3cIKETunOutP2Exchgs_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 1, 2, 1, 12),
    _Hh3cIKETunOutP2Exchgs_Type()
)
hh3cIKETunOutP2Exchgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIKETunOutP2Exchgs.setStatus("current")
_Hh3cIKETunOutP2ExchgRejects_Type = Counter64
_Hh3cIKETunOutP2ExchgRejects_Object = MibTableColumn
hh3cIKETunOutP2ExchgRejects = _Hh3cIKETunOutP2ExchgRejects_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 1, 2, 1, 13),
    _Hh3cIKETunOutP2ExchgRejects_Type()
)
hh3cIKETunOutP2ExchgRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIKETunOutP2ExchgRejects.setStatus("current")
_Hh3cIKETunOutP2SaDelRequests_Type = Counter64
_Hh3cIKETunOutP2SaDelRequests_Object = MibTableColumn
hh3cIKETunOutP2SaDelRequests = _Hh3cIKETunOutP2SaDelRequests_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 1, 2, 1, 14),
    _Hh3cIKETunOutP2SaDelRequests_Type()
)
hh3cIKETunOutP2SaDelRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIKETunOutP2SaDelRequests.setStatus("current")
_Hh3cIKETunOutP1SaDelRequests_Type = Counter64
_Hh3cIKETunOutP1SaDelRequests_Object = MibTableColumn
hh3cIKETunOutP1SaDelRequests = _Hh3cIKETunOutP1SaDelRequests_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 1, 2, 1, 15),
    _Hh3cIKETunOutP1SaDelRequests_Type()
)
hh3cIKETunOutP1SaDelRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIKETunOutP1SaDelRequests.setStatus("current")
_Hh3cIKETunOutNotifys_Type = Counter32
_Hh3cIKETunOutNotifys_Object = MibTableColumn
hh3cIKETunOutNotifys = _Hh3cIKETunOutNotifys_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 1, 2, 1, 16),
    _Hh3cIKETunOutNotifys_Type()
)
hh3cIKETunOutNotifys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIKETunOutNotifys.setStatus("current")
_Hh3cIKEGlobalStats_ObjectIdentity = ObjectIdentity
hh3cIKEGlobalStats = _Hh3cIKEGlobalStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 1, 3)
)
_Hh3cIKEGlobalActiveTunnels_Type = Gauge32
_Hh3cIKEGlobalActiveTunnels_Object = MibScalar
hh3cIKEGlobalActiveTunnels = _Hh3cIKEGlobalActiveTunnels_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 1, 3, 1),
    _Hh3cIKEGlobalActiveTunnels_Type()
)
hh3cIKEGlobalActiveTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIKEGlobalActiveTunnels.setStatus("current")
_Hh3cIKEGlobalInOctets_Type = Counter64
_Hh3cIKEGlobalInOctets_Object = MibScalar
hh3cIKEGlobalInOctets = _Hh3cIKEGlobalInOctets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 1, 3, 2),
    _Hh3cIKEGlobalInOctets_Type()
)
hh3cIKEGlobalInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIKEGlobalInOctets.setStatus("current")
_Hh3cIKEGlobalInPkts_Type = Counter64
_Hh3cIKEGlobalInPkts_Object = MibScalar
hh3cIKEGlobalInPkts = _Hh3cIKEGlobalInPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 1, 3, 3),
    _Hh3cIKEGlobalInPkts_Type()
)
hh3cIKEGlobalInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIKEGlobalInPkts.setStatus("current")
_Hh3cIKEGlobalInDropPkts_Type = Counter64
_Hh3cIKEGlobalInDropPkts_Object = MibScalar
hh3cIKEGlobalInDropPkts = _Hh3cIKEGlobalInDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 1, 3, 4),
    _Hh3cIKEGlobalInDropPkts_Type()
)
hh3cIKEGlobalInDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIKEGlobalInDropPkts.setStatus("current")
_Hh3cIKEGlobalInP2Exchgs_Type = Counter64
_Hh3cIKEGlobalInP2Exchgs_Object = MibScalar
hh3cIKEGlobalInP2Exchgs = _Hh3cIKEGlobalInP2Exchgs_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 1, 3, 5),
    _Hh3cIKEGlobalInP2Exchgs_Type()
)
hh3cIKEGlobalInP2Exchgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIKEGlobalInP2Exchgs.setStatus("current")
_Hh3cIKEGlobalInP2ExchgRejects_Type = Counter64
_Hh3cIKEGlobalInP2ExchgRejects_Object = MibScalar
hh3cIKEGlobalInP2ExchgRejects = _Hh3cIKEGlobalInP2ExchgRejects_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 1, 3, 6),
    _Hh3cIKEGlobalInP2ExchgRejects_Type()
)
hh3cIKEGlobalInP2ExchgRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIKEGlobalInP2ExchgRejects.setStatus("current")
_Hh3cIKEGlobalInP2SaDelRequests_Type = Counter64
_Hh3cIKEGlobalInP2SaDelRequests_Object = MibScalar
hh3cIKEGlobalInP2SaDelRequests = _Hh3cIKEGlobalInP2SaDelRequests_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 1, 3, 7),
    _Hh3cIKEGlobalInP2SaDelRequests_Type()
)
hh3cIKEGlobalInP2SaDelRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIKEGlobalInP2SaDelRequests.setStatus("current")
_Hh3cIKEGlobalInNotifys_Type = Counter32
_Hh3cIKEGlobalInNotifys_Object = MibScalar
hh3cIKEGlobalInNotifys = _Hh3cIKEGlobalInNotifys_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 1, 3, 8),
    _Hh3cIKEGlobalInNotifys_Type()
)
hh3cIKEGlobalInNotifys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIKEGlobalInNotifys.setStatus("current")
_Hh3cIKEGlobalOutOctets_Type = Counter64
_Hh3cIKEGlobalOutOctets_Object = MibScalar
hh3cIKEGlobalOutOctets = _Hh3cIKEGlobalOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 1, 3, 9),
    _Hh3cIKEGlobalOutOctets_Type()
)
hh3cIKEGlobalOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIKEGlobalOutOctets.setStatus("current")
_Hh3cIKEGlobalOutPkts_Type = Counter64
_Hh3cIKEGlobalOutPkts_Object = MibScalar
hh3cIKEGlobalOutPkts = _Hh3cIKEGlobalOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 1, 3, 10),
    _Hh3cIKEGlobalOutPkts_Type()
)
hh3cIKEGlobalOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIKEGlobalOutPkts.setStatus("current")
_Hh3cIKEGlobalOutDropPkts_Type = Counter64
_Hh3cIKEGlobalOutDropPkts_Object = MibScalar
hh3cIKEGlobalOutDropPkts = _Hh3cIKEGlobalOutDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 1, 3, 11),
    _Hh3cIKEGlobalOutDropPkts_Type()
)
hh3cIKEGlobalOutDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIKEGlobalOutDropPkts.setStatus("current")
_Hh3cIKEGlobalOutP2Exchgs_Type = Counter64
_Hh3cIKEGlobalOutP2Exchgs_Object = MibScalar
hh3cIKEGlobalOutP2Exchgs = _Hh3cIKEGlobalOutP2Exchgs_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 1, 3, 12),
    _Hh3cIKEGlobalOutP2Exchgs_Type()
)
hh3cIKEGlobalOutP2Exchgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIKEGlobalOutP2Exchgs.setStatus("current")
_Hh3cIKEGlobalOutP2ExchgRejects_Type = Counter64
_Hh3cIKEGlobalOutP2ExchgRejects_Object = MibScalar
hh3cIKEGlobalOutP2ExchgRejects = _Hh3cIKEGlobalOutP2ExchgRejects_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 1, 3, 13),
    _Hh3cIKEGlobalOutP2ExchgRejects_Type()
)
hh3cIKEGlobalOutP2ExchgRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIKEGlobalOutP2ExchgRejects.setStatus("current")
_Hh3cIKEGlobalOutP2SaDelRequests_Type = Counter64
_Hh3cIKEGlobalOutP2SaDelRequests_Object = MibScalar
hh3cIKEGlobalOutP2SaDelRequests = _Hh3cIKEGlobalOutP2SaDelRequests_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 1, 3, 14),
    _Hh3cIKEGlobalOutP2SaDelRequests_Type()
)
hh3cIKEGlobalOutP2SaDelRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIKEGlobalOutP2SaDelRequests.setStatus("current")
_Hh3cIKEGlobalOutNotifys_Type = Counter32
_Hh3cIKEGlobalOutNotifys_Object = MibScalar
hh3cIKEGlobalOutNotifys = _Hh3cIKEGlobalOutNotifys_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 1, 3, 15),
    _Hh3cIKEGlobalOutNotifys_Type()
)
hh3cIKEGlobalOutNotifys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIKEGlobalOutNotifys.setStatus("current")
_Hh3cIKEGlobalInitTunnels_Type = Counter32
_Hh3cIKEGlobalInitTunnels_Object = MibScalar
hh3cIKEGlobalInitTunnels = _Hh3cIKEGlobalInitTunnels_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 1, 3, 16),
    _Hh3cIKEGlobalInitTunnels_Type()
)
hh3cIKEGlobalInitTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIKEGlobalInitTunnels.setStatus("current")
_Hh3cIKEGlobalInitTunnelFails_Type = Counter32
_Hh3cIKEGlobalInitTunnelFails_Object = MibScalar
hh3cIKEGlobalInitTunnelFails = _Hh3cIKEGlobalInitTunnelFails_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 1, 3, 17),
    _Hh3cIKEGlobalInitTunnelFails_Type()
)
hh3cIKEGlobalInitTunnelFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIKEGlobalInitTunnelFails.setStatus("current")
_Hh3cIKEGlobalRespTunnels_Type = Counter32
_Hh3cIKEGlobalRespTunnels_Object = MibScalar
hh3cIKEGlobalRespTunnels = _Hh3cIKEGlobalRespTunnels_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 1, 3, 18),
    _Hh3cIKEGlobalRespTunnels_Type()
)
hh3cIKEGlobalRespTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIKEGlobalRespTunnels.setStatus("current")
_Hh3cIKEGlobalRespTunnelFails_Type = Counter32
_Hh3cIKEGlobalRespTunnelFails_Object = MibScalar
hh3cIKEGlobalRespTunnelFails = _Hh3cIKEGlobalRespTunnelFails_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 1, 3, 19),
    _Hh3cIKEGlobalRespTunnelFails_Type()
)
hh3cIKEGlobalRespTunnelFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIKEGlobalRespTunnelFails.setStatus("current")
_Hh3cIKEGlobalAuthFails_Type = Counter32
_Hh3cIKEGlobalAuthFails_Object = MibScalar
hh3cIKEGlobalAuthFails = _Hh3cIKEGlobalAuthFails_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 1, 3, 20),
    _Hh3cIKEGlobalAuthFails_Type()
)
hh3cIKEGlobalAuthFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIKEGlobalAuthFails.setStatus("current")
_Hh3cIKEGlobalNoSaFails_Type = Counter32
_Hh3cIKEGlobalNoSaFails_Object = MibScalar
hh3cIKEGlobalNoSaFails = _Hh3cIKEGlobalNoSaFails_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 1, 3, 21),
    _Hh3cIKEGlobalNoSaFails_Type()
)
hh3cIKEGlobalNoSaFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIKEGlobalNoSaFails.setStatus("current")
_Hh3cIKEGlobalInvalidCookieFails_Type = Counter32
_Hh3cIKEGlobalInvalidCookieFails_Object = MibScalar
hh3cIKEGlobalInvalidCookieFails = _Hh3cIKEGlobalInvalidCookieFails_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 1, 3, 22),
    _Hh3cIKEGlobalInvalidCookieFails_Type()
)
hh3cIKEGlobalInvalidCookieFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIKEGlobalInvalidCookieFails.setStatus("current")
_Hh3cIKEGlobalAttrNotSuppFails_Type = Counter32
_Hh3cIKEGlobalAttrNotSuppFails_Object = MibScalar
hh3cIKEGlobalAttrNotSuppFails = _Hh3cIKEGlobalAttrNotSuppFails_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 1, 3, 23),
    _Hh3cIKEGlobalAttrNotSuppFails_Type()
)
hh3cIKEGlobalAttrNotSuppFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIKEGlobalAttrNotSuppFails.setStatus("current")
_Hh3cIKEGlobalNoProposalChosenFails_Type = Counter32
_Hh3cIKEGlobalNoProposalChosenFails_Object = MibScalar
hh3cIKEGlobalNoProposalChosenFails = _Hh3cIKEGlobalNoProposalChosenFails_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 1, 3, 24),
    _Hh3cIKEGlobalNoProposalChosenFails_Type()
)
hh3cIKEGlobalNoProposalChosenFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIKEGlobalNoProposalChosenFails.setStatus("current")
_Hh3cIKEGlobalUnsportExchTypeFails_Type = Counter32
_Hh3cIKEGlobalUnsportExchTypeFails_Object = MibScalar
hh3cIKEGlobalUnsportExchTypeFails = _Hh3cIKEGlobalUnsportExchTypeFails_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 1, 3, 25),
    _Hh3cIKEGlobalUnsportExchTypeFails_Type()
)
hh3cIKEGlobalUnsportExchTypeFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIKEGlobalUnsportExchTypeFails.setStatus("current")
_Hh3cIKEGlobalInvalidIdFails_Type = Counter32
_Hh3cIKEGlobalInvalidIdFails_Object = MibScalar
hh3cIKEGlobalInvalidIdFails = _Hh3cIKEGlobalInvalidIdFails_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 1, 3, 26),
    _Hh3cIKEGlobalInvalidIdFails_Type()
)
hh3cIKEGlobalInvalidIdFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIKEGlobalInvalidIdFails.setStatus("current")
_Hh3cIKEGlobalInvalidProFails_Type = Counter32
_Hh3cIKEGlobalInvalidProFails_Object = MibScalar
hh3cIKEGlobalInvalidProFails = _Hh3cIKEGlobalInvalidProFails_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 1, 3, 27),
    _Hh3cIKEGlobalInvalidProFails_Type()
)
hh3cIKEGlobalInvalidProFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIKEGlobalInvalidProFails.setStatus("current")
_Hh3cIKEGlobalCertTypeUnsuppFails_Type = Counter32
_Hh3cIKEGlobalCertTypeUnsuppFails_Object = MibScalar
hh3cIKEGlobalCertTypeUnsuppFails = _Hh3cIKEGlobalCertTypeUnsuppFails_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 1, 3, 28),
    _Hh3cIKEGlobalCertTypeUnsuppFails_Type()
)
hh3cIKEGlobalCertTypeUnsuppFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIKEGlobalCertTypeUnsuppFails.setStatus("current")
_Hh3cIKEGlobalInvalidCertAuthFails_Type = Counter32
_Hh3cIKEGlobalInvalidCertAuthFails_Object = MibScalar
hh3cIKEGlobalInvalidCertAuthFails = _Hh3cIKEGlobalInvalidCertAuthFails_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 1, 3, 29),
    _Hh3cIKEGlobalInvalidCertAuthFails_Type()
)
hh3cIKEGlobalInvalidCertAuthFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIKEGlobalInvalidCertAuthFails.setStatus("current")
_Hh3cIKEGlobalInvalidSignFails_Type = Counter32
_Hh3cIKEGlobalInvalidSignFails_Object = MibScalar
hh3cIKEGlobalInvalidSignFails = _Hh3cIKEGlobalInvalidSignFails_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 1, 3, 30),
    _Hh3cIKEGlobalInvalidSignFails_Type()
)
hh3cIKEGlobalInvalidSignFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIKEGlobalInvalidSignFails.setStatus("current")
_Hh3cIKEGlobalCertUnavailableFails_Type = Counter32
_Hh3cIKEGlobalCertUnavailableFails_Object = MibScalar
hh3cIKEGlobalCertUnavailableFails = _Hh3cIKEGlobalCertUnavailableFails_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 1, 3, 31),
    _Hh3cIKEGlobalCertUnavailableFails_Type()
)
hh3cIKEGlobalCertUnavailableFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIKEGlobalCertUnavailableFails.setStatus("current")
_Hh3cIKETrapObject_ObjectIdentity = ObjectIdentity
hh3cIKETrapObject = _Hh3cIKETrapObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 1, 4)
)
_Hh3cIKEProposalNumber_Type = Integer32
_Hh3cIKEProposalNumber_Object = MibScalar
hh3cIKEProposalNumber = _Hh3cIKEProposalNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 1, 4, 1),
    _Hh3cIKEProposalNumber_Type()
)
hh3cIKEProposalNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cIKEProposalNumber.setStatus("current")
_Hh3cIKEProposalSize_Type = Integer32
_Hh3cIKEProposalSize_Object = MibScalar
hh3cIKEProposalSize = _Hh3cIKEProposalSize_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 1, 4, 2),
    _Hh3cIKEProposalSize_Type()
)
hh3cIKEProposalSize.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cIKEProposalSize.setStatus("current")
_Hh3cIKEIdInformation_Type = DisplayString
_Hh3cIKEIdInformation_Object = MibScalar
hh3cIKEIdInformation = _Hh3cIKEIdInformation_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 1, 4, 3),
    _Hh3cIKEIdInformation_Type()
)
hh3cIKEIdInformation.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cIKEIdInformation.setStatus("current")
_Hh3cIKEProtocolNum_Type = Integer32
_Hh3cIKEProtocolNum_Object = MibScalar
hh3cIKEProtocolNum = _Hh3cIKEProtocolNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 1, 4, 4),
    _Hh3cIKEProtocolNum_Type()
)
hh3cIKEProtocolNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cIKEProtocolNum.setStatus("current")
_Hh3cIKECertInformation_Type = DisplayString
_Hh3cIKECertInformation_Object = MibScalar
hh3cIKECertInformation = _Hh3cIKECertInformation_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 1, 4, 5),
    _Hh3cIKECertInformation_Type()
)
hh3cIKECertInformation.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cIKECertInformation.setStatus("current")
_Hh3cIKETrapCntl_ObjectIdentity = ObjectIdentity
hh3cIKETrapCntl = _Hh3cIKETrapCntl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 1, 5)
)
_Hh3cIKETrapGlobalCntl_Type = Hh3cTrapStatus
_Hh3cIKETrapGlobalCntl_Object = MibScalar
hh3cIKETrapGlobalCntl = _Hh3cIKETrapGlobalCntl_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 1, 5, 1),
    _Hh3cIKETrapGlobalCntl_Type()
)
hh3cIKETrapGlobalCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIKETrapGlobalCntl.setStatus("current")
_Hh3cIKETunnelStartTrapCntl_Type = Hh3cTrapStatus
_Hh3cIKETunnelStartTrapCntl_Object = MibScalar
hh3cIKETunnelStartTrapCntl = _Hh3cIKETunnelStartTrapCntl_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 1, 5, 2),
    _Hh3cIKETunnelStartTrapCntl_Type()
)
hh3cIKETunnelStartTrapCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIKETunnelStartTrapCntl.setStatus("current")
_Hh3cIKETunnelStopTrapCntl_Type = Hh3cTrapStatus
_Hh3cIKETunnelStopTrapCntl_Object = MibScalar
hh3cIKETunnelStopTrapCntl = _Hh3cIKETunnelStopTrapCntl_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 1, 5, 3),
    _Hh3cIKETunnelStopTrapCntl_Type()
)
hh3cIKETunnelStopTrapCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIKETunnelStopTrapCntl.setStatus("current")
_Hh3cIKENoSaTrapCntl_Type = Hh3cTrapStatus
_Hh3cIKENoSaTrapCntl_Object = MibScalar
hh3cIKENoSaTrapCntl = _Hh3cIKENoSaTrapCntl_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 1, 5, 4),
    _Hh3cIKENoSaTrapCntl_Type()
)
hh3cIKENoSaTrapCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIKENoSaTrapCntl.setStatus("current")
_Hh3cIKEEncryFailureTrapCntl_Type = Hh3cTrapStatus
_Hh3cIKEEncryFailureTrapCntl_Object = MibScalar
hh3cIKEEncryFailureTrapCntl = _Hh3cIKEEncryFailureTrapCntl_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 1, 5, 5),
    _Hh3cIKEEncryFailureTrapCntl_Type()
)
hh3cIKEEncryFailureTrapCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIKEEncryFailureTrapCntl.setStatus("current")
_Hh3cIKEDecryFailureTrapCntl_Type = Hh3cTrapStatus
_Hh3cIKEDecryFailureTrapCntl_Object = MibScalar
hh3cIKEDecryFailureTrapCntl = _Hh3cIKEDecryFailureTrapCntl_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 1, 5, 6),
    _Hh3cIKEDecryFailureTrapCntl_Type()
)
hh3cIKEDecryFailureTrapCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIKEDecryFailureTrapCntl.setStatus("current")
_Hh3cIKEInvalidProposalTrapCntl_Type = Hh3cTrapStatus
_Hh3cIKEInvalidProposalTrapCntl_Object = MibScalar
hh3cIKEInvalidProposalTrapCntl = _Hh3cIKEInvalidProposalTrapCntl_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 1, 5, 7),
    _Hh3cIKEInvalidProposalTrapCntl_Type()
)
hh3cIKEInvalidProposalTrapCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIKEInvalidProposalTrapCntl.setStatus("current")
_Hh3cIKEAuthFailTrapCntl_Type = Hh3cTrapStatus
_Hh3cIKEAuthFailTrapCntl_Object = MibScalar
hh3cIKEAuthFailTrapCntl = _Hh3cIKEAuthFailTrapCntl_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 1, 5, 8),
    _Hh3cIKEAuthFailTrapCntl_Type()
)
hh3cIKEAuthFailTrapCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIKEAuthFailTrapCntl.setStatus("current")
_Hh3cIKEInvalidCookieTrapCntl_Type = Hh3cTrapStatus
_Hh3cIKEInvalidCookieTrapCntl_Object = MibScalar
hh3cIKEInvalidCookieTrapCntl = _Hh3cIKEInvalidCookieTrapCntl_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 1, 5, 9),
    _Hh3cIKEInvalidCookieTrapCntl_Type()
)
hh3cIKEInvalidCookieTrapCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIKEInvalidCookieTrapCntl.setStatus("current")
_Hh3cIKEInvalidSpiTrapCntl_Type = Hh3cTrapStatus
_Hh3cIKEInvalidSpiTrapCntl_Object = MibScalar
hh3cIKEInvalidSpiTrapCntl = _Hh3cIKEInvalidSpiTrapCntl_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 1, 5, 10),
    _Hh3cIKEInvalidSpiTrapCntl_Type()
)
hh3cIKEInvalidSpiTrapCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIKEInvalidSpiTrapCntl.setStatus("current")
_Hh3cIKEAttrNotSuppTrapCntl_Type = Hh3cTrapStatus
_Hh3cIKEAttrNotSuppTrapCntl_Object = MibScalar
hh3cIKEAttrNotSuppTrapCntl = _Hh3cIKEAttrNotSuppTrapCntl_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 1, 5, 11),
    _Hh3cIKEAttrNotSuppTrapCntl_Type()
)
hh3cIKEAttrNotSuppTrapCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIKEAttrNotSuppTrapCntl.setStatus("current")
_Hh3cIKEUnsportExchTypeTrapCntl_Type = Hh3cTrapStatus
_Hh3cIKEUnsportExchTypeTrapCntl_Object = MibScalar
hh3cIKEUnsportExchTypeTrapCntl = _Hh3cIKEUnsportExchTypeTrapCntl_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 1, 5, 12),
    _Hh3cIKEUnsportExchTypeTrapCntl_Type()
)
hh3cIKEUnsportExchTypeTrapCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIKEUnsportExchTypeTrapCntl.setStatus("current")
_Hh3cIKEInvalidIdTrapCntl_Type = Hh3cTrapStatus
_Hh3cIKEInvalidIdTrapCntl_Object = MibScalar
hh3cIKEInvalidIdTrapCntl = _Hh3cIKEInvalidIdTrapCntl_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 1, 5, 13),
    _Hh3cIKEInvalidIdTrapCntl_Type()
)
hh3cIKEInvalidIdTrapCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIKEInvalidIdTrapCntl.setStatus("current")
_Hh3cIKEInvalidProtocolTrapCntl_Type = Hh3cTrapStatus
_Hh3cIKEInvalidProtocolTrapCntl_Object = MibScalar
hh3cIKEInvalidProtocolTrapCntl = _Hh3cIKEInvalidProtocolTrapCntl_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 1, 5, 14),
    _Hh3cIKEInvalidProtocolTrapCntl_Type()
)
hh3cIKEInvalidProtocolTrapCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIKEInvalidProtocolTrapCntl.setStatus("current")
_Hh3cIKECertTypeUnsuppTrapCntl_Type = Hh3cTrapStatus
_Hh3cIKECertTypeUnsuppTrapCntl_Object = MibScalar
hh3cIKECertTypeUnsuppTrapCntl = _Hh3cIKECertTypeUnsuppTrapCntl_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 1, 5, 15),
    _Hh3cIKECertTypeUnsuppTrapCntl_Type()
)
hh3cIKECertTypeUnsuppTrapCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIKECertTypeUnsuppTrapCntl.setStatus("current")
_Hh3cIKEInvalidCertAuthTrapCntl_Type = Hh3cTrapStatus
_Hh3cIKEInvalidCertAuthTrapCntl_Object = MibScalar
hh3cIKEInvalidCertAuthTrapCntl = _Hh3cIKEInvalidCertAuthTrapCntl_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 1, 5, 16),
    _Hh3cIKEInvalidCertAuthTrapCntl_Type()
)
hh3cIKEInvalidCertAuthTrapCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIKEInvalidCertAuthTrapCntl.setStatus("current")
_Hh3cIKEInvalidSignTrapCntl_Type = Hh3cTrapStatus
_Hh3cIKEInvalidSignTrapCntl_Object = MibScalar
hh3cIKEInvalidSignTrapCntl = _Hh3cIKEInvalidSignTrapCntl_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 1, 5, 17),
    _Hh3cIKEInvalidSignTrapCntl_Type()
)
hh3cIKEInvalidSignTrapCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIKEInvalidSignTrapCntl.setStatus("current")
_Hh3cIKECertUnavailableTrapCntl_Type = Hh3cTrapStatus
_Hh3cIKECertUnavailableTrapCntl_Object = MibScalar
hh3cIKECertUnavailableTrapCntl = _Hh3cIKECertUnavailableTrapCntl_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 1, 5, 18),
    _Hh3cIKECertUnavailableTrapCntl_Type()
)
hh3cIKECertUnavailableTrapCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIKECertUnavailableTrapCntl.setStatus("current")
_Hh3cIKEProposalAddTrapCntl_Type = Hh3cTrapStatus
_Hh3cIKEProposalAddTrapCntl_Object = MibScalar
hh3cIKEProposalAddTrapCntl = _Hh3cIKEProposalAddTrapCntl_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 1, 5, 19),
    _Hh3cIKEProposalAddTrapCntl_Type()
)
hh3cIKEProposalAddTrapCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIKEProposalAddTrapCntl.setStatus("current")
_Hh3cIKEProposalDelTrapCntl_Type = Hh3cTrapStatus
_Hh3cIKEProposalDelTrapCntl_Object = MibScalar
hh3cIKEProposalDelTrapCntl = _Hh3cIKEProposalDelTrapCntl_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 1, 5, 20),
    _Hh3cIKEProposalDelTrapCntl_Type()
)
hh3cIKEProposalDelTrapCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIKEProposalDelTrapCntl.setStatus("current")
_Hh3cIKETrap_ObjectIdentity = ObjectIdentity
hh3cIKETrap = _Hh3cIKETrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 1, 6)
)
_Hh3cIKENotifications_ObjectIdentity = ObjectIdentity
hh3cIKENotifications = _Hh3cIKENotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 1, 6, 1)
)
_Hh3cIKEConformance_ObjectIdentity = ObjectIdentity
hh3cIKEConformance = _Hh3cIKEConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 2)
)
_Hh3cIKECompliances_ObjectIdentity = ObjectIdentity
hh3cIKECompliances = _Hh3cIKECompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 2, 1)
)
_Hh3cIKEGroups_ObjectIdentity = ObjectIdentity
hh3cIKEGroups = _Hh3cIKEGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 2, 2)
)

# Managed Objects groups

hh3cIKETunnelTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 2, 2, 1)
)
hh3cIKETunnelTableGroup.setObjects(
      *(("HH3C-IKE-MONITOR-MIB", "hh3cIKETunLocalType"),
        ("HH3C-IKE-MONITOR-MIB", "hh3cIKETunLocalValue1"),
        ("HH3C-IKE-MONITOR-MIB", "hh3cIKETunLocalValue2"),
        ("HH3C-IKE-MONITOR-MIB", "hh3cIKETunLocalAddr"),
        ("HH3C-IKE-MONITOR-MIB", "hh3cIKETunRemoteType"),
        ("HH3C-IKE-MONITOR-MIB", "hh3cIKETunRemoteValue1"),
        ("HH3C-IKE-MONITOR-MIB", "hh3cIKETunRemoteValue2"),
        ("HH3C-IKE-MONITOR-MIB", "hh3cIKETunRemoteAddr"),
        ("HH3C-IKE-MONITOR-MIB", "hh3cIKETunInitiator"),
        ("HH3C-IKE-MONITOR-MIB", "hh3cIKETunNegoMode"),
        ("HH3C-IKE-MONITOR-MIB", "hh3cIKETunDiffHellmanGrp"),
        ("HH3C-IKE-MONITOR-MIB", "hh3cIKETunEncryptAlgo"),
        ("HH3C-IKE-MONITOR-MIB", "hh3cIKETunHashAlgo"),
        ("HH3C-IKE-MONITOR-MIB", "hh3cIKETunAuthMethod"),
        ("HH3C-IKE-MONITOR-MIB", "hh3cIKETunLifeTime"),
        ("HH3C-IKE-MONITOR-MIB", "hh3cIKETunActiveTime"),
        ("HH3C-IKE-MONITOR-MIB", "hh3cIKETunRemainTime"),
        ("HH3C-IKE-MONITOR-MIB", "hh3cIKETunTotalRefreshes"),
        ("HH3C-IKE-MONITOR-MIB", "hh3cIKETunState"),
        ("HH3C-IKE-MONITOR-MIB", "hh3cIKETunDpdIntervalTime"),
        ("HH3C-IKE-MONITOR-MIB", "hh3cIKETunDpdTimeOut"))
)
if mibBuilder.loadTexts:
    hh3cIKETunnelTableGroup.setStatus("current")

hh3cIKETunnelStatTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 2, 2, 2)
)
hh3cIKETunnelStatTableGroup.setObjects(
      *(("HH3C-IKE-MONITOR-MIB", "hh3cIKETunInOctets"),
        ("HH3C-IKE-MONITOR-MIB", "hh3cIKETunInPkts"),
        ("HH3C-IKE-MONITOR-MIB", "hh3cIKETunInDropPkts"),
        ("HH3C-IKE-MONITOR-MIB", "hh3cIKETunInP2Exchgs"),
        ("HH3C-IKE-MONITOR-MIB", "hh3cIKETunInP2ExchgRejets"),
        ("HH3C-IKE-MONITOR-MIB", "hh3cIKETunInP2SaDelRequests"),
        ("HH3C-IKE-MONITOR-MIB", "hh3cIKETunInP1SaDelRequests"),
        ("HH3C-IKE-MONITOR-MIB", "hh3cIKETunInNotifys"),
        ("HH3C-IKE-MONITOR-MIB", "hh3cIKETunOutOctets"),
        ("HH3C-IKE-MONITOR-MIB", "hh3cIKETunOutPkts"),
        ("HH3C-IKE-MONITOR-MIB", "hh3cIKETunOutDropPkts"),
        ("HH3C-IKE-MONITOR-MIB", "hh3cIKETunOutP2Exchgs"),
        ("HH3C-IKE-MONITOR-MIB", "hh3cIKETunOutP2ExchgRejects"),
        ("HH3C-IKE-MONITOR-MIB", "hh3cIKETunOutP2SaDelRequests"),
        ("HH3C-IKE-MONITOR-MIB", "hh3cIKETunOutP1SaDelRequests"),
        ("HH3C-IKE-MONITOR-MIB", "hh3cIKETunOutNotifys"))
)
if mibBuilder.loadTexts:
    hh3cIKETunnelStatTableGroup.setStatus("current")

hh3cIKEGlobalStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 2, 2, 3)
)
hh3cIKEGlobalStatsGroup.setObjects(
      *(("HH3C-IKE-MONITOR-MIB", "hh3cIKEGlobalActiveTunnels"),
        ("HH3C-IKE-MONITOR-MIB", "hh3cIKEGlobalInOctets"),
        ("HH3C-IKE-MONITOR-MIB", "hh3cIKEGlobalInPkts"),
        ("HH3C-IKE-MONITOR-MIB", "hh3cIKEGlobalInDropPkts"),
        ("HH3C-IKE-MONITOR-MIB", "hh3cIKEGlobalInP2Exchgs"),
        ("HH3C-IKE-MONITOR-MIB", "hh3cIKEGlobalInP2ExchgRejects"),
        ("HH3C-IKE-MONITOR-MIB", "hh3cIKEGlobalInP2SaDelRequests"),
        ("HH3C-IKE-MONITOR-MIB", "hh3cIKEGlobalInNotifys"),
        ("HH3C-IKE-MONITOR-MIB", "hh3cIKEGlobalOutOctets"),
        ("HH3C-IKE-MONITOR-MIB", "hh3cIKEGlobalOutPkts"),
        ("HH3C-IKE-MONITOR-MIB", "hh3cIKEGlobalOutDropPkts"),
        ("HH3C-IKE-MONITOR-MIB", "hh3cIKEGlobalOutP2Exchgs"),
        ("HH3C-IKE-MONITOR-MIB", "hh3cIKEGlobalOutP2ExchgRejects"),
        ("HH3C-IKE-MONITOR-MIB", "hh3cIKEGlobalOutP2SaDelRequests"),
        ("HH3C-IKE-MONITOR-MIB", "hh3cIKEGlobalOutNotifys"),
        ("HH3C-IKE-MONITOR-MIB", "hh3cIKEGlobalInitTunnels"),
        ("HH3C-IKE-MONITOR-MIB", "hh3cIKEGlobalInitTunnelFails"),
        ("HH3C-IKE-MONITOR-MIB", "hh3cIKEGlobalRespTunnels"),
        ("HH3C-IKE-MONITOR-MIB", "hh3cIKEGlobalRespTunnelFails"),
        ("HH3C-IKE-MONITOR-MIB", "hh3cIKEGlobalAuthFails"),
        ("HH3C-IKE-MONITOR-MIB", "hh3cIKEGlobalNoSaFails"),
        ("HH3C-IKE-MONITOR-MIB", "hh3cIKEGlobalInvalidCookieFails"),
        ("HH3C-IKE-MONITOR-MIB", "hh3cIKEGlobalAttrNotSuppFails"),
        ("HH3C-IKE-MONITOR-MIB", "hh3cIKEGlobalNoProposalChosenFails"),
        ("HH3C-IKE-MONITOR-MIB", "hh3cIKEGlobalUnsportExchTypeFails"),
        ("HH3C-IKE-MONITOR-MIB", "hh3cIKEGlobalInvalidIdFails"),
        ("HH3C-IKE-MONITOR-MIB", "hh3cIKEGlobalInvalidProFails"),
        ("HH3C-IKE-MONITOR-MIB", "hh3cIKEGlobalCertTypeUnsuppFails"),
        ("HH3C-IKE-MONITOR-MIB", "hh3cIKEGlobalInvalidCertAuthFails"),
        ("HH3C-IKE-MONITOR-MIB", "hh3cIKEGlobalInvalidSignFails"),
        ("HH3C-IKE-MONITOR-MIB", "hh3cIKEGlobalCertUnavailableFails"))
)
if mibBuilder.loadTexts:
    hh3cIKEGlobalStatsGroup.setStatus("current")

hh3cIKETrapObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 2, 2, 4)
)
hh3cIKETrapObjectGroup.setObjects(
      *(("HH3C-IKE-MONITOR-MIB", "hh3cIKEProposalNumber"),
        ("HH3C-IKE-MONITOR-MIB", "hh3cIKEProposalSize"),
        ("HH3C-IKE-MONITOR-MIB", "hh3cIKEIdInformation"),
        ("HH3C-IKE-MONITOR-MIB", "hh3cIKEProtocolNum"),
        ("HH3C-IKE-MONITOR-MIB", "hh3cIKECertInformation"))
)
if mibBuilder.loadTexts:
    hh3cIKETrapObjectGroup.setStatus("current")

hh3cIKETrapCntlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 2, 2, 5)
)
hh3cIKETrapCntlGroup.setObjects(
      *(("HH3C-IKE-MONITOR-MIB", "hh3cIKETrapGlobalCntl"),
        ("HH3C-IKE-MONITOR-MIB", "hh3cIKETunnelStartTrapCntl"),
        ("HH3C-IKE-MONITOR-MIB", "hh3cIKETunnelStopTrapCntl"),
        ("HH3C-IKE-MONITOR-MIB", "hh3cIKENoSaTrapCntl"),
        ("HH3C-IKE-MONITOR-MIB", "hh3cIKEEncryFailureTrapCntl"),
        ("HH3C-IKE-MONITOR-MIB", "hh3cIKEDecryFailureTrapCntl"),
        ("HH3C-IKE-MONITOR-MIB", "hh3cIKEInvalidProposalTrapCntl"),
        ("HH3C-IKE-MONITOR-MIB", "hh3cIKEAuthFailTrapCntl"),
        ("HH3C-IKE-MONITOR-MIB", "hh3cIKEInvalidCookieTrapCntl"),
        ("HH3C-IKE-MONITOR-MIB", "hh3cIKEInvalidSpiTrapCntl"),
        ("HH3C-IKE-MONITOR-MIB", "hh3cIKEAttrNotSuppTrapCntl"),
        ("HH3C-IKE-MONITOR-MIB", "hh3cIKEUnsportExchTypeTrapCntl"),
        ("HH3C-IKE-MONITOR-MIB", "hh3cIKEInvalidIdTrapCntl"),
        ("HH3C-IKE-MONITOR-MIB", "hh3cIKEInvalidProtocolTrapCntl"),
        ("HH3C-IKE-MONITOR-MIB", "hh3cIKECertTypeUnsuppTrapCntl"),
        ("HH3C-IKE-MONITOR-MIB", "hh3cIKEInvalidCertAuthTrapCntl"),
        ("HH3C-IKE-MONITOR-MIB", "hh3cIKEInvalidSignTrapCntl"),
        ("HH3C-IKE-MONITOR-MIB", "hh3cIKECertUnavailableTrapCntl"),
        ("HH3C-IKE-MONITOR-MIB", "hh3cIKEProposalAddTrapCntl"),
        ("HH3C-IKE-MONITOR-MIB", "hh3cIKEProposalDelTrapCntl"))
)
if mibBuilder.loadTexts:
    hh3cIKETrapCntlGroup.setStatus("current")


# Notification objects

hh3cIKETunnelStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 1, 6, 1, 1)
)
hh3cIKETunnelStart.setObjects(
      *(("HH3C-IKE-MONITOR-MIB", "hh3cIKETunLocalAddr"),
        ("HH3C-IKE-MONITOR-MIB", "hh3cIKETunRemoteAddr"),
        ("HH3C-IKE-MONITOR-MIB", "hh3cIKETunLifeTime"))
)
if mibBuilder.loadTexts:
    hh3cIKETunnelStart.setStatus(
        "current"
    )

hh3cIKETunnelStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 1, 6, 1, 2)
)
hh3cIKETunnelStop.setObjects(
      *(("HH3C-IKE-MONITOR-MIB", "hh3cIKETunLocalAddr"),
        ("HH3C-IKE-MONITOR-MIB", "hh3cIKETunRemoteAddr"),
        ("HH3C-IKE-MONITOR-MIB", "hh3cIKETunActiveTime"))
)
if mibBuilder.loadTexts:
    hh3cIKETunnelStop.setStatus(
        "current"
    )

hh3cIKENoSaFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 1, 6, 1, 3)
)
hh3cIKENoSaFailure.setObjects(
      *(("HH3C-IKE-MONITOR-MIB", "hh3cIKETunLocalAddr"),
        ("HH3C-IKE-MONITOR-MIB", "hh3cIKETunRemoteAddr"))
)
if mibBuilder.loadTexts:
    hh3cIKENoSaFailure.setStatus(
        "current"
    )

hh3cIKEEncryFailFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 1, 6, 1, 4)
)
hh3cIKEEncryFailFailure.setObjects(
      *(("HH3C-IKE-MONITOR-MIB", "hh3cIKETunLocalAddr"),
        ("HH3C-IKE-MONITOR-MIB", "hh3cIKETunRemoteAddr"))
)
if mibBuilder.loadTexts:
    hh3cIKEEncryFailFailure.setStatus(
        "current"
    )

hh3cIKEDecryFailFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 1, 6, 1, 5)
)
hh3cIKEDecryFailFailure.setObjects(
      *(("HH3C-IKE-MONITOR-MIB", "hh3cIKETunLocalAddr"),
        ("HH3C-IKE-MONITOR-MIB", "hh3cIKETunRemoteAddr"))
)
if mibBuilder.loadTexts:
    hh3cIKEDecryFailFailure.setStatus(
        "current"
    )

hh3cIKEInvalidProposalFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 1, 6, 1, 6)
)
hh3cIKEInvalidProposalFailure.setObjects(
      *(("HH3C-IKE-MONITOR-MIB", "hh3cIKETunLocalAddr"),
        ("HH3C-IKE-MONITOR-MIB", "hh3cIKETunRemoteAddr"))
)
if mibBuilder.loadTexts:
    hh3cIKEInvalidProposalFailure.setStatus(
        "current"
    )

hh3cIKEAuthFailFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 1, 6, 1, 7)
)
hh3cIKEAuthFailFailure.setObjects(
      *(("HH3C-IKE-MONITOR-MIB", "hh3cIKETunLocalAddr"),
        ("HH3C-IKE-MONITOR-MIB", "hh3cIKETunRemoteAddr"))
)
if mibBuilder.loadTexts:
    hh3cIKEAuthFailFailure.setStatus(
        "current"
    )

hh3cIKEInvalidCookieFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 1, 6, 1, 8)
)
hh3cIKEInvalidCookieFailure.setObjects(
      *(("HH3C-IKE-MONITOR-MIB", "hh3cIKETunLocalAddr"),
        ("HH3C-IKE-MONITOR-MIB", "hh3cIKETunRemoteAddr"))
)
if mibBuilder.loadTexts:
    hh3cIKEInvalidCookieFailure.setStatus(
        "current"
    )

hh3cIKEAttrNotSuppFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 1, 6, 1, 9)
)
hh3cIKEAttrNotSuppFailure.setObjects(
      *(("HH3C-IKE-MONITOR-MIB", "hh3cIKETunLocalAddr"),
        ("HH3C-IKE-MONITOR-MIB", "hh3cIKETunRemoteAddr"))
)
if mibBuilder.loadTexts:
    hh3cIKEAttrNotSuppFailure.setStatus(
        "current"
    )

hh3cIKEUnsportExchTypeFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 1, 6, 1, 10)
)
hh3cIKEUnsportExchTypeFailure.setObjects(
      *(("HH3C-IKE-MONITOR-MIB", "hh3cIKETunLocalAddr"),
        ("HH3C-IKE-MONITOR-MIB", "hh3cIKETunRemoteAddr"))
)
if mibBuilder.loadTexts:
    hh3cIKEUnsportExchTypeFailure.setStatus(
        "current"
    )

hh3cIKEInvalidIdFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 1, 6, 1, 11)
)
hh3cIKEInvalidIdFailure.setObjects(
      *(("HH3C-IKE-MONITOR-MIB", "hh3cIKETunLocalAddr"),
        ("HH3C-IKE-MONITOR-MIB", "hh3cIKETunRemoteAddr"),
        ("HH3C-IKE-MONITOR-MIB", "hh3cIKEIdInformation"))
)
if mibBuilder.loadTexts:
    hh3cIKEInvalidIdFailure.setStatus(
        "current"
    )

hh3cIKEInvalidProtocolFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 1, 6, 1, 12)
)
hh3cIKEInvalidProtocolFailure.setObjects(
      *(("HH3C-IKE-MONITOR-MIB", "hh3cIKETunLocalAddr"),
        ("HH3C-IKE-MONITOR-MIB", "hh3cIKETunRemoteAddr"),
        ("HH3C-IKE-MONITOR-MIB", "hh3cIKEProtocolNum"))
)
if mibBuilder.loadTexts:
    hh3cIKEInvalidProtocolFailure.setStatus(
        "current"
    )

hh3cIKECertTypeUnsuppFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 1, 6, 1, 13)
)
hh3cIKECertTypeUnsuppFailure.setObjects(
      *(("HH3C-IKE-MONITOR-MIB", "hh3cIKETunLocalAddr"),
        ("HH3C-IKE-MONITOR-MIB", "hh3cIKETunRemoteAddr"),
        ("HH3C-IKE-MONITOR-MIB", "hh3cIKECertInformation"))
)
if mibBuilder.loadTexts:
    hh3cIKECertTypeUnsuppFailure.setStatus(
        "current"
    )

hh3cIKEInvalidCertAuthFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 1, 6, 1, 14)
)
hh3cIKEInvalidCertAuthFailure.setObjects(
      *(("HH3C-IKE-MONITOR-MIB", "hh3cIKETunLocalAddr"),
        ("HH3C-IKE-MONITOR-MIB", "hh3cIKETunRemoteAddr"),
        ("HH3C-IKE-MONITOR-MIB", "hh3cIKECertInformation"))
)
if mibBuilder.loadTexts:
    hh3cIKEInvalidCertAuthFailure.setStatus(
        "current"
    )

hh3cIKElInvalidSignFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 1, 6, 1, 15)
)
hh3cIKElInvalidSignFailure.setObjects(
      *(("HH3C-IKE-MONITOR-MIB", "hh3cIKETunLocalAddr"),
        ("HH3C-IKE-MONITOR-MIB", "hh3cIKETunRemoteAddr"),
        ("HH3C-IKE-MONITOR-MIB", "hh3cIKECertInformation"))
)
if mibBuilder.loadTexts:
    hh3cIKElInvalidSignFailure.setStatus(
        "current"
    )

hh3cIKECertUnavailableFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 1, 6, 1, 16)
)
hh3cIKECertUnavailableFailure.setObjects(
      *(("HH3C-IKE-MONITOR-MIB", "hh3cIKETunLocalAddr"),
        ("HH3C-IKE-MONITOR-MIB", "hh3cIKETunRemoteAddr"),
        ("HH3C-IKE-MONITOR-MIB", "hh3cIKECertInformation"))
)
if mibBuilder.loadTexts:
    hh3cIKECertUnavailableFailure.setStatus(
        "current"
    )

hh3cIKEProposalAdd = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 1, 6, 1, 17)
)
hh3cIKEProposalAdd.setObjects(
      *(("HH3C-IKE-MONITOR-MIB", "hh3cIKEProposalNumber"),
        ("HH3C-IKE-MONITOR-MIB", "hh3cIKEProposalSize"))
)
if mibBuilder.loadTexts:
    hh3cIKEProposalAdd.setStatus(
        "current"
    )

hh3cIKEProposalDel = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 1, 6, 1, 18)
)
hh3cIKEProposalDel.setObjects(
      *(("HH3C-IKE-MONITOR-MIB", "hh3cIKEProposalNumber"),
        ("HH3C-IKE-MONITOR-MIB", "hh3cIKEProposalSize"))
)
if mibBuilder.loadTexts:
    hh3cIKEProposalDel.setStatus(
        "current"
    )


# Notifications groups

hh3cIKETrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 2, 2, 6)
)
hh3cIKETrapGroup.setObjects(
      *(("HH3C-IKE-MONITOR-MIB", "hh3cIKETunnelStart"),
        ("HH3C-IKE-MONITOR-MIB", "hh3cIKETunnelStop"),
        ("HH3C-IKE-MONITOR-MIB", "hh3cIKENoSaFailure"),
        ("HH3C-IKE-MONITOR-MIB", "hh3cIKEEncryFailFailure"),
        ("HH3C-IKE-MONITOR-MIB", "hh3cIKEDecryFailFailure"),
        ("HH3C-IKE-MONITOR-MIB", "hh3cIKEInvalidProposalFailure"),
        ("HH3C-IKE-MONITOR-MIB", "hh3cIKEAuthFailFailure"),
        ("HH3C-IKE-MONITOR-MIB", "hh3cIKEInvalidCookieFailure"),
        ("HH3C-IKE-MONITOR-MIB", "hh3cIKEAttrNotSuppFailure"),
        ("HH3C-IKE-MONITOR-MIB", "hh3cIKEUnsportExchTypeFailure"),
        ("HH3C-IKE-MONITOR-MIB", "hh3cIKEInvalidIdFailure"),
        ("HH3C-IKE-MONITOR-MIB", "hh3cIKEInvalidProtocolFailure"),
        ("HH3C-IKE-MONITOR-MIB", "hh3cIKECertTypeUnsuppFailure"),
        ("HH3C-IKE-MONITOR-MIB", "hh3cIKEInvalidCertAuthFailure"),
        ("HH3C-IKE-MONITOR-MIB", "hh3cIKElInvalidSignFailure"),
        ("HH3C-IKE-MONITOR-MIB", "hh3cIKECertUnavailableFailure"),
        ("HH3C-IKE-MONITOR-MIB", "hh3cIKEProposalAdd"),
        ("HH3C-IKE-MONITOR-MIB", "hh3cIKEProposalDel"))
)
if mibBuilder.loadTexts:
    hh3cIKETrapGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hh3cIKECompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cIKECompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-IKE-MONITOR-MIB",
    **{"Hh3cIKENegoMode": Hh3cIKENegoMode,
       "Hh3cIKEAuthMethod": Hh3cIKEAuthMethod,
       "Hh3cDiffHellmanGrp": Hh3cDiffHellmanGrp,
       "Hh3cEncryptAlgo": Hh3cEncryptAlgo,
       "Hh3cAuthAlgo": Hh3cAuthAlgo,
       "Hh3cSaProtocol": Hh3cSaProtocol,
       "Hh3cTrapStatus": Hh3cTrapStatus,
       "Hh3cIKEIDType": Hh3cIKEIDType,
       "Hh3cTrafficType": Hh3cTrafficType,
       "Hh3cIKETunnelState": Hh3cIKETunnelState,
       "hh3cIKEMonitor": hh3cIKEMonitor,
       "hh3cIKEObjects": hh3cIKEObjects,
       "hh3cIKETunnelTable": hh3cIKETunnelTable,
       "hh3cIKETunnelEntry": hh3cIKETunnelEntry,
       "hh3cIKETunIndex": hh3cIKETunIndex,
       "hh3cIKETunLocalType": hh3cIKETunLocalType,
       "hh3cIKETunLocalValue1": hh3cIKETunLocalValue1,
       "hh3cIKETunLocalValue2": hh3cIKETunLocalValue2,
       "hh3cIKETunLocalAddr": hh3cIKETunLocalAddr,
       "hh3cIKETunRemoteType": hh3cIKETunRemoteType,
       "hh3cIKETunRemoteValue1": hh3cIKETunRemoteValue1,
       "hh3cIKETunRemoteValue2": hh3cIKETunRemoteValue2,
       "hh3cIKETunRemoteAddr": hh3cIKETunRemoteAddr,
       "hh3cIKETunInitiator": hh3cIKETunInitiator,
       "hh3cIKETunNegoMode": hh3cIKETunNegoMode,
       "hh3cIKETunDiffHellmanGrp": hh3cIKETunDiffHellmanGrp,
       "hh3cIKETunEncryptAlgo": hh3cIKETunEncryptAlgo,
       "hh3cIKETunHashAlgo": hh3cIKETunHashAlgo,
       "hh3cIKETunAuthMethod": hh3cIKETunAuthMethod,
       "hh3cIKETunLifeTime": hh3cIKETunLifeTime,
       "hh3cIKETunActiveTime": hh3cIKETunActiveTime,
       "hh3cIKETunRemainTime": hh3cIKETunRemainTime,
       "hh3cIKETunTotalRefreshes": hh3cIKETunTotalRefreshes,
       "hh3cIKETunState": hh3cIKETunState,
       "hh3cIKETunDpdIntervalTime": hh3cIKETunDpdIntervalTime,
       "hh3cIKETunDpdTimeOut": hh3cIKETunDpdTimeOut,
       "hh3cIKETunnelStatTable": hh3cIKETunnelStatTable,
       "hh3cIKETunnelStatEntry": hh3cIKETunnelStatEntry,
       "hh3cIKETunInOctets": hh3cIKETunInOctets,
       "hh3cIKETunInPkts": hh3cIKETunInPkts,
       "hh3cIKETunInDropPkts": hh3cIKETunInDropPkts,
       "hh3cIKETunInP2Exchgs": hh3cIKETunInP2Exchgs,
       "hh3cIKETunInP2ExchgRejets": hh3cIKETunInP2ExchgRejets,
       "hh3cIKETunInP2SaDelRequests": hh3cIKETunInP2SaDelRequests,
       "hh3cIKETunInP1SaDelRequests": hh3cIKETunInP1SaDelRequests,
       "hh3cIKETunInNotifys": hh3cIKETunInNotifys,
       "hh3cIKETunOutOctets": hh3cIKETunOutOctets,
       "hh3cIKETunOutPkts": hh3cIKETunOutPkts,
       "hh3cIKETunOutDropPkts": hh3cIKETunOutDropPkts,
       "hh3cIKETunOutP2Exchgs": hh3cIKETunOutP2Exchgs,
       "hh3cIKETunOutP2ExchgRejects": hh3cIKETunOutP2ExchgRejects,
       "hh3cIKETunOutP2SaDelRequests": hh3cIKETunOutP2SaDelRequests,
       "hh3cIKETunOutP1SaDelRequests": hh3cIKETunOutP1SaDelRequests,
       "hh3cIKETunOutNotifys": hh3cIKETunOutNotifys,
       "hh3cIKEGlobalStats": hh3cIKEGlobalStats,
       "hh3cIKEGlobalActiveTunnels": hh3cIKEGlobalActiveTunnels,
       "hh3cIKEGlobalInOctets": hh3cIKEGlobalInOctets,
       "hh3cIKEGlobalInPkts": hh3cIKEGlobalInPkts,
       "hh3cIKEGlobalInDropPkts": hh3cIKEGlobalInDropPkts,
       "hh3cIKEGlobalInP2Exchgs": hh3cIKEGlobalInP2Exchgs,
       "hh3cIKEGlobalInP2ExchgRejects": hh3cIKEGlobalInP2ExchgRejects,
       "hh3cIKEGlobalInP2SaDelRequests": hh3cIKEGlobalInP2SaDelRequests,
       "hh3cIKEGlobalInNotifys": hh3cIKEGlobalInNotifys,
       "hh3cIKEGlobalOutOctets": hh3cIKEGlobalOutOctets,
       "hh3cIKEGlobalOutPkts": hh3cIKEGlobalOutPkts,
       "hh3cIKEGlobalOutDropPkts": hh3cIKEGlobalOutDropPkts,
       "hh3cIKEGlobalOutP2Exchgs": hh3cIKEGlobalOutP2Exchgs,
       "hh3cIKEGlobalOutP2ExchgRejects": hh3cIKEGlobalOutP2ExchgRejects,
       "hh3cIKEGlobalOutP2SaDelRequests": hh3cIKEGlobalOutP2SaDelRequests,
       "hh3cIKEGlobalOutNotifys": hh3cIKEGlobalOutNotifys,
       "hh3cIKEGlobalInitTunnels": hh3cIKEGlobalInitTunnels,
       "hh3cIKEGlobalInitTunnelFails": hh3cIKEGlobalInitTunnelFails,
       "hh3cIKEGlobalRespTunnels": hh3cIKEGlobalRespTunnels,
       "hh3cIKEGlobalRespTunnelFails": hh3cIKEGlobalRespTunnelFails,
       "hh3cIKEGlobalAuthFails": hh3cIKEGlobalAuthFails,
       "hh3cIKEGlobalNoSaFails": hh3cIKEGlobalNoSaFails,
       "hh3cIKEGlobalInvalidCookieFails": hh3cIKEGlobalInvalidCookieFails,
       "hh3cIKEGlobalAttrNotSuppFails": hh3cIKEGlobalAttrNotSuppFails,
       "hh3cIKEGlobalNoProposalChosenFails": hh3cIKEGlobalNoProposalChosenFails,
       "hh3cIKEGlobalUnsportExchTypeFails": hh3cIKEGlobalUnsportExchTypeFails,
       "hh3cIKEGlobalInvalidIdFails": hh3cIKEGlobalInvalidIdFails,
       "hh3cIKEGlobalInvalidProFails": hh3cIKEGlobalInvalidProFails,
       "hh3cIKEGlobalCertTypeUnsuppFails": hh3cIKEGlobalCertTypeUnsuppFails,
       "hh3cIKEGlobalInvalidCertAuthFails": hh3cIKEGlobalInvalidCertAuthFails,
       "hh3cIKEGlobalInvalidSignFails": hh3cIKEGlobalInvalidSignFails,
       "hh3cIKEGlobalCertUnavailableFails": hh3cIKEGlobalCertUnavailableFails,
       "hh3cIKETrapObject": hh3cIKETrapObject,
       "hh3cIKEProposalNumber": hh3cIKEProposalNumber,
       "hh3cIKEProposalSize": hh3cIKEProposalSize,
       "hh3cIKEIdInformation": hh3cIKEIdInformation,
       "hh3cIKEProtocolNum": hh3cIKEProtocolNum,
       "hh3cIKECertInformation": hh3cIKECertInformation,
       "hh3cIKETrapCntl": hh3cIKETrapCntl,
       "hh3cIKETrapGlobalCntl": hh3cIKETrapGlobalCntl,
       "hh3cIKETunnelStartTrapCntl": hh3cIKETunnelStartTrapCntl,
       "hh3cIKETunnelStopTrapCntl": hh3cIKETunnelStopTrapCntl,
       "hh3cIKENoSaTrapCntl": hh3cIKENoSaTrapCntl,
       "hh3cIKEEncryFailureTrapCntl": hh3cIKEEncryFailureTrapCntl,
       "hh3cIKEDecryFailureTrapCntl": hh3cIKEDecryFailureTrapCntl,
       "hh3cIKEInvalidProposalTrapCntl": hh3cIKEInvalidProposalTrapCntl,
       "hh3cIKEAuthFailTrapCntl": hh3cIKEAuthFailTrapCntl,
       "hh3cIKEInvalidCookieTrapCntl": hh3cIKEInvalidCookieTrapCntl,
       "hh3cIKEInvalidSpiTrapCntl": hh3cIKEInvalidSpiTrapCntl,
       "hh3cIKEAttrNotSuppTrapCntl": hh3cIKEAttrNotSuppTrapCntl,
       "hh3cIKEUnsportExchTypeTrapCntl": hh3cIKEUnsportExchTypeTrapCntl,
       "hh3cIKEInvalidIdTrapCntl": hh3cIKEInvalidIdTrapCntl,
       "hh3cIKEInvalidProtocolTrapCntl": hh3cIKEInvalidProtocolTrapCntl,
       "hh3cIKECertTypeUnsuppTrapCntl": hh3cIKECertTypeUnsuppTrapCntl,
       "hh3cIKEInvalidCertAuthTrapCntl": hh3cIKEInvalidCertAuthTrapCntl,
       "hh3cIKEInvalidSignTrapCntl": hh3cIKEInvalidSignTrapCntl,
       "hh3cIKECertUnavailableTrapCntl": hh3cIKECertUnavailableTrapCntl,
       "hh3cIKEProposalAddTrapCntl": hh3cIKEProposalAddTrapCntl,
       "hh3cIKEProposalDelTrapCntl": hh3cIKEProposalDelTrapCntl,
       "hh3cIKETrap": hh3cIKETrap,
       "hh3cIKENotifications": hh3cIKENotifications,
       "hh3cIKETunnelStart": hh3cIKETunnelStart,
       "hh3cIKETunnelStop": hh3cIKETunnelStop,
       "hh3cIKENoSaFailure": hh3cIKENoSaFailure,
       "hh3cIKEEncryFailFailure": hh3cIKEEncryFailFailure,
       "hh3cIKEDecryFailFailure": hh3cIKEDecryFailFailure,
       "hh3cIKEInvalidProposalFailure": hh3cIKEInvalidProposalFailure,
       "hh3cIKEAuthFailFailure": hh3cIKEAuthFailFailure,
       "hh3cIKEInvalidCookieFailure": hh3cIKEInvalidCookieFailure,
       "hh3cIKEAttrNotSuppFailure": hh3cIKEAttrNotSuppFailure,
       "hh3cIKEUnsportExchTypeFailure": hh3cIKEUnsportExchTypeFailure,
       "hh3cIKEInvalidIdFailure": hh3cIKEInvalidIdFailure,
       "hh3cIKEInvalidProtocolFailure": hh3cIKEInvalidProtocolFailure,
       "hh3cIKECertTypeUnsuppFailure": hh3cIKECertTypeUnsuppFailure,
       "hh3cIKEInvalidCertAuthFailure": hh3cIKEInvalidCertAuthFailure,
       "hh3cIKElInvalidSignFailure": hh3cIKElInvalidSignFailure,
       "hh3cIKECertUnavailableFailure": hh3cIKECertUnavailableFailure,
       "hh3cIKEProposalAdd": hh3cIKEProposalAdd,
       "hh3cIKEProposalDel": hh3cIKEProposalDel,
       "hh3cIKEConformance": hh3cIKEConformance,
       "hh3cIKECompliances": hh3cIKECompliances,
       "hh3cIKECompliance": hh3cIKECompliance,
       "hh3cIKEGroups": hh3cIKEGroups,
       "hh3cIKETunnelTableGroup": hh3cIKETunnelTableGroup,
       "hh3cIKETunnelStatTableGroup": hh3cIKETunnelStatTableGroup,
       "hh3cIKEGlobalStatsGroup": hh3cIKEGlobalStatsGroup,
       "hh3cIKETrapObjectGroup": hh3cIKETrapObjectGroup,
       "hh3cIKETrapCntlGroup": hh3cIKETrapCntlGroup,
       "hh3cIKETrapGroup": hh3cIKETrapGroup}
)
