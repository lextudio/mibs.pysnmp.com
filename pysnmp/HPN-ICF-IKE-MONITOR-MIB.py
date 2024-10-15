# SNMP MIB module (HPN-ICF-IKE-MONITOR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-IKE-MONITOR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:00:33 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

hpnicfIKEMonitor = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class HpnicfIKENegoMode(Integer32, TextualConvention):
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



class HpnicfIKEAuthMethod(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dsaSignatures", 2),
          ("preSharedKey", 1),
          ("rsaSignatures", 3))
    )



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
              12,
              13,
              2147483647)
        )
    )
    namedValues = NamedValues(
        *(("aesCamelliaCbc", 12),
          ("aesCbc", 7),
          ("aesCbc128", 8),
          ("aesCbc192", 9),
          ("aesCbc256", 10),
          ("aesCtr", 11),
          ("blowfishCbc", 3),
          ("castCbc", 6),
          ("desCbc", 1),
          ("ideaCbc", 2),
          ("invalidAlg", 2147483647),
          ("none", 0),
          ("rc4", 13),
          ("rc5R16B64Cbc", 4),
          ("tripleDesCbc", 5))
    )



class HpnicfAuthAlgo(Integer32, TextualConvention):
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



class HpnicfIKEIDType(Integer32, TextualConvention):
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



class HpnicfIKETunnelState(Integer32, TextualConvention):
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

_HpnicfIKEObjects_ObjectIdentity = ObjectIdentity
hpnicfIKEObjects = _HpnicfIKEObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 1)
)
_HpnicfIKETunnelTable_Object = MibTable
hpnicfIKETunnelTable = _HpnicfIKETunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 1, 1)
)
if mibBuilder.loadTexts:
    hpnicfIKETunnelTable.setStatus("current")
_HpnicfIKETunnelEntry_Object = MibTableRow
hpnicfIKETunnelEntry = _HpnicfIKETunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 1, 1, 1)
)
hpnicfIKETunnelEntry.setIndexNames(
    (0, "HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunIndex"),
)
if mibBuilder.loadTexts:
    hpnicfIKETunnelEntry.setStatus("current")


class _HpnicfIKETunIndex_Type(Integer32):
    """Custom type hpnicfIKETunIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpnicfIKETunIndex_Type.__name__ = "Integer32"
_HpnicfIKETunIndex_Object = MibTableColumn
hpnicfIKETunIndex = _HpnicfIKETunIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 1, 1, 1, 1),
    _HpnicfIKETunIndex_Type()
)
hpnicfIKETunIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfIKETunIndex.setStatus("current")
_HpnicfIKETunLocalType_Type = HpnicfIKEIDType
_HpnicfIKETunLocalType_Object = MibTableColumn
hpnicfIKETunLocalType = _HpnicfIKETunLocalType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 1, 1, 1, 2),
    _HpnicfIKETunLocalType_Type()
)
hpnicfIKETunLocalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIKETunLocalType.setStatus("current")
_HpnicfIKETunLocalValue1_Type = DisplayString
_HpnicfIKETunLocalValue1_Object = MibTableColumn
hpnicfIKETunLocalValue1 = _HpnicfIKETunLocalValue1_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 1, 1, 1, 3),
    _HpnicfIKETunLocalValue1_Type()
)
hpnicfIKETunLocalValue1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIKETunLocalValue1.setStatus("current")
_HpnicfIKETunLocalValue2_Type = DisplayString
_HpnicfIKETunLocalValue2_Object = MibTableColumn
hpnicfIKETunLocalValue2 = _HpnicfIKETunLocalValue2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 1, 1, 1, 4),
    _HpnicfIKETunLocalValue2_Type()
)
hpnicfIKETunLocalValue2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIKETunLocalValue2.setStatus("current")
_HpnicfIKETunLocalAddr_Type = IpAddress
_HpnicfIKETunLocalAddr_Object = MibTableColumn
hpnicfIKETunLocalAddr = _HpnicfIKETunLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 1, 1, 1, 5),
    _HpnicfIKETunLocalAddr_Type()
)
hpnicfIKETunLocalAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIKETunLocalAddr.setStatus("deprecated")
_HpnicfIKETunRemoteType_Type = HpnicfIKEIDType
_HpnicfIKETunRemoteType_Object = MibTableColumn
hpnicfIKETunRemoteType = _HpnicfIKETunRemoteType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 1, 1, 1, 6),
    _HpnicfIKETunRemoteType_Type()
)
hpnicfIKETunRemoteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIKETunRemoteType.setStatus("current")
_HpnicfIKETunRemoteValue1_Type = DisplayString
_HpnicfIKETunRemoteValue1_Object = MibTableColumn
hpnicfIKETunRemoteValue1 = _HpnicfIKETunRemoteValue1_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 1, 1, 1, 7),
    _HpnicfIKETunRemoteValue1_Type()
)
hpnicfIKETunRemoteValue1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIKETunRemoteValue1.setStatus("current")
_HpnicfIKETunRemoteValue2_Type = DisplayString
_HpnicfIKETunRemoteValue2_Object = MibTableColumn
hpnicfIKETunRemoteValue2 = _HpnicfIKETunRemoteValue2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 1, 1, 1, 8),
    _HpnicfIKETunRemoteValue2_Type()
)
hpnicfIKETunRemoteValue2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIKETunRemoteValue2.setStatus("current")
_HpnicfIKETunRemoteAddr_Type = IpAddress
_HpnicfIKETunRemoteAddr_Object = MibTableColumn
hpnicfIKETunRemoteAddr = _HpnicfIKETunRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 1, 1, 1, 9),
    _HpnicfIKETunRemoteAddr_Type()
)
hpnicfIKETunRemoteAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIKETunRemoteAddr.setStatus("deprecated")


class _HpnicfIKETunInitiator_Type(Integer32):
    """Custom type hpnicfIKETunInitiator based on Integer32"""
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


_HpnicfIKETunInitiator_Type.__name__ = "Integer32"
_HpnicfIKETunInitiator_Object = MibTableColumn
hpnicfIKETunInitiator = _HpnicfIKETunInitiator_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 1, 1, 1, 10),
    _HpnicfIKETunInitiator_Type()
)
hpnicfIKETunInitiator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIKETunInitiator.setStatus("current")
_HpnicfIKETunNegoMode_Type = HpnicfIKENegoMode
_HpnicfIKETunNegoMode_Object = MibTableColumn
hpnicfIKETunNegoMode = _HpnicfIKETunNegoMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 1, 1, 1, 11),
    _HpnicfIKETunNegoMode_Type()
)
hpnicfIKETunNegoMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIKETunNegoMode.setStatus("current")
_HpnicfIKETunDiffHellmanGrp_Type = HpnicfDiffHellmanGrp
_HpnicfIKETunDiffHellmanGrp_Object = MibTableColumn
hpnicfIKETunDiffHellmanGrp = _HpnicfIKETunDiffHellmanGrp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 1, 1, 1, 12),
    _HpnicfIKETunDiffHellmanGrp_Type()
)
hpnicfIKETunDiffHellmanGrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIKETunDiffHellmanGrp.setStatus("current")
_HpnicfIKETunEncryptAlgo_Type = HpnicfEncryptAlgo
_HpnicfIKETunEncryptAlgo_Object = MibTableColumn
hpnicfIKETunEncryptAlgo = _HpnicfIKETunEncryptAlgo_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 1, 1, 1, 13),
    _HpnicfIKETunEncryptAlgo_Type()
)
hpnicfIKETunEncryptAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIKETunEncryptAlgo.setStatus("current")
_HpnicfIKETunHashAlgo_Type = HpnicfAuthAlgo
_HpnicfIKETunHashAlgo_Object = MibTableColumn
hpnicfIKETunHashAlgo = _HpnicfIKETunHashAlgo_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 1, 1, 1, 14),
    _HpnicfIKETunHashAlgo_Type()
)
hpnicfIKETunHashAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIKETunHashAlgo.setStatus("current")
_HpnicfIKETunAuthMethod_Type = HpnicfIKEAuthMethod
_HpnicfIKETunAuthMethod_Object = MibTableColumn
hpnicfIKETunAuthMethod = _HpnicfIKETunAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 1, 1, 1, 15),
    _HpnicfIKETunAuthMethod_Type()
)
hpnicfIKETunAuthMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIKETunAuthMethod.setStatus("current")


class _HpnicfIKETunLifeTime_Type(Integer32):
    """Custom type hpnicfIKETunLifeTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpnicfIKETunLifeTime_Type.__name__ = "Integer32"
_HpnicfIKETunLifeTime_Object = MibTableColumn
hpnicfIKETunLifeTime = _HpnicfIKETunLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 1, 1, 1, 16),
    _HpnicfIKETunLifeTime_Type()
)
hpnicfIKETunLifeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIKETunLifeTime.setStatus("current")


class _HpnicfIKETunActiveTime_Type(Integer32):
    """Custom type hpnicfIKETunActiveTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpnicfIKETunActiveTime_Type.__name__ = "Integer32"
_HpnicfIKETunActiveTime_Object = MibTableColumn
hpnicfIKETunActiveTime = _HpnicfIKETunActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 1, 1, 1, 17),
    _HpnicfIKETunActiveTime_Type()
)
hpnicfIKETunActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIKETunActiveTime.setStatus("current")


class _HpnicfIKETunRemainTime_Type(Integer32):
    """Custom type hpnicfIKETunRemainTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpnicfIKETunRemainTime_Type.__name__ = "Integer32"
_HpnicfIKETunRemainTime_Object = MibTableColumn
hpnicfIKETunRemainTime = _HpnicfIKETunRemainTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 1, 1, 1, 18),
    _HpnicfIKETunRemainTime_Type()
)
hpnicfIKETunRemainTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIKETunRemainTime.setStatus("current")
_HpnicfIKETunTotalRefreshes_Type = Counter32
_HpnicfIKETunTotalRefreshes_Object = MibTableColumn
hpnicfIKETunTotalRefreshes = _HpnicfIKETunTotalRefreshes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 1, 1, 1, 19),
    _HpnicfIKETunTotalRefreshes_Type()
)
hpnicfIKETunTotalRefreshes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIKETunTotalRefreshes.setStatus("current")
_HpnicfIKETunState_Type = HpnicfIKETunnelState
_HpnicfIKETunState_Object = MibTableColumn
hpnicfIKETunState = _HpnicfIKETunState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 1, 1, 1, 20),
    _HpnicfIKETunState_Type()
)
hpnicfIKETunState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIKETunState.setStatus("current")


class _HpnicfIKETunDpdIntervalTime_Type(Integer32):
    """Custom type hpnicfIKETunDpdIntervalTime based on Integer32"""
    defaultValue = 10


_HpnicfIKETunDpdIntervalTime_Object = MibTableColumn
hpnicfIKETunDpdIntervalTime = _HpnicfIKETunDpdIntervalTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 1, 1, 1, 21),
    _HpnicfIKETunDpdIntervalTime_Type()
)
hpnicfIKETunDpdIntervalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIKETunDpdIntervalTime.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfIKETunDpdIntervalTime.setUnits("second")


class _HpnicfIKETunDpdTimeOut_Type(Integer32):
    """Custom type hpnicfIKETunDpdTimeOut based on Integer32"""
    defaultValue = 5


_HpnicfIKETunDpdTimeOut_Object = MibTableColumn
hpnicfIKETunDpdTimeOut = _HpnicfIKETunDpdTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 1, 1, 1, 22),
    _HpnicfIKETunDpdTimeOut_Type()
)
hpnicfIKETunDpdTimeOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIKETunDpdTimeOut.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfIKETunDpdTimeOut.setUnits("second")
_HpnicfIKETunLocalInetAddrType_Type = InetAddressType
_HpnicfIKETunLocalInetAddrType_Object = MibTableColumn
hpnicfIKETunLocalInetAddrType = _HpnicfIKETunLocalInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 1, 1, 1, 23),
    _HpnicfIKETunLocalInetAddrType_Type()
)
hpnicfIKETunLocalInetAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIKETunLocalInetAddrType.setStatus("current")
_HpnicfIKETunLocalInetAddr_Type = InetAddress
_HpnicfIKETunLocalInetAddr_Object = MibTableColumn
hpnicfIKETunLocalInetAddr = _HpnicfIKETunLocalInetAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 1, 1, 1, 24),
    _HpnicfIKETunLocalInetAddr_Type()
)
hpnicfIKETunLocalInetAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIKETunLocalInetAddr.setStatus("current")
_HpnicfIKETunRemoteInetAddrType_Type = InetAddressType
_HpnicfIKETunRemoteInetAddrType_Object = MibTableColumn
hpnicfIKETunRemoteInetAddrType = _HpnicfIKETunRemoteInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 1, 1, 1, 25),
    _HpnicfIKETunRemoteInetAddrType_Type()
)
hpnicfIKETunRemoteInetAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIKETunRemoteInetAddrType.setStatus("current")
_HpnicfIKETunRemoteInetAddr_Type = InetAddress
_HpnicfIKETunRemoteInetAddr_Object = MibTableColumn
hpnicfIKETunRemoteInetAddr = _HpnicfIKETunRemoteInetAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 1, 1, 1, 26),
    _HpnicfIKETunRemoteInetAddr_Type()
)
hpnicfIKETunRemoteInetAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIKETunRemoteInetAddr.setStatus("current")
_HpnicfIKETunnelStatTable_Object = MibTable
hpnicfIKETunnelStatTable = _HpnicfIKETunnelStatTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 1, 2)
)
if mibBuilder.loadTexts:
    hpnicfIKETunnelStatTable.setStatus("current")
_HpnicfIKETunnelStatEntry_Object = MibTableRow
hpnicfIKETunnelStatEntry = _HpnicfIKETunnelStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 1, 2, 1)
)
hpnicfIKETunnelStatEntry.setIndexNames(
    (0, "HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunIndex"),
)
if mibBuilder.loadTexts:
    hpnicfIKETunnelStatEntry.setStatus("current")
_HpnicfIKETunInOctets_Type = Counter64
_HpnicfIKETunInOctets_Object = MibTableColumn
hpnicfIKETunInOctets = _HpnicfIKETunInOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 1, 2, 1, 1),
    _HpnicfIKETunInOctets_Type()
)
hpnicfIKETunInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIKETunInOctets.setStatus("current")
_HpnicfIKETunInPkts_Type = Counter64
_HpnicfIKETunInPkts_Object = MibTableColumn
hpnicfIKETunInPkts = _HpnicfIKETunInPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 1, 2, 1, 2),
    _HpnicfIKETunInPkts_Type()
)
hpnicfIKETunInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIKETunInPkts.setStatus("current")
_HpnicfIKETunInDropPkts_Type = Counter64
_HpnicfIKETunInDropPkts_Object = MibTableColumn
hpnicfIKETunInDropPkts = _HpnicfIKETunInDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 1, 2, 1, 3),
    _HpnicfIKETunInDropPkts_Type()
)
hpnicfIKETunInDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIKETunInDropPkts.setStatus("current")
_HpnicfIKETunInP2Exchgs_Type = Counter64
_HpnicfIKETunInP2Exchgs_Object = MibTableColumn
hpnicfIKETunInP2Exchgs = _HpnicfIKETunInP2Exchgs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 1, 2, 1, 4),
    _HpnicfIKETunInP2Exchgs_Type()
)
hpnicfIKETunInP2Exchgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIKETunInP2Exchgs.setStatus("current")
_HpnicfIKETunInP2ExchgRejets_Type = Counter64
_HpnicfIKETunInP2ExchgRejets_Object = MibTableColumn
hpnicfIKETunInP2ExchgRejets = _HpnicfIKETunInP2ExchgRejets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 1, 2, 1, 5),
    _HpnicfIKETunInP2ExchgRejets_Type()
)
hpnicfIKETunInP2ExchgRejets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIKETunInP2ExchgRejets.setStatus("current")
_HpnicfIKETunInP2SaDelRequests_Type = Counter64
_HpnicfIKETunInP2SaDelRequests_Object = MibTableColumn
hpnicfIKETunInP2SaDelRequests = _HpnicfIKETunInP2SaDelRequests_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 1, 2, 1, 6),
    _HpnicfIKETunInP2SaDelRequests_Type()
)
hpnicfIKETunInP2SaDelRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIKETunInP2SaDelRequests.setStatus("current")
_HpnicfIKETunInP1SaDelRequests_Type = Counter64
_HpnicfIKETunInP1SaDelRequests_Object = MibTableColumn
hpnicfIKETunInP1SaDelRequests = _HpnicfIKETunInP1SaDelRequests_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 1, 2, 1, 7),
    _HpnicfIKETunInP1SaDelRequests_Type()
)
hpnicfIKETunInP1SaDelRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIKETunInP1SaDelRequests.setStatus("current")
_HpnicfIKETunInNotifys_Type = Counter32
_HpnicfIKETunInNotifys_Object = MibTableColumn
hpnicfIKETunInNotifys = _HpnicfIKETunInNotifys_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 1, 2, 1, 8),
    _HpnicfIKETunInNotifys_Type()
)
hpnicfIKETunInNotifys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIKETunInNotifys.setStatus("current")
_HpnicfIKETunOutOctets_Type = Counter64
_HpnicfIKETunOutOctets_Object = MibTableColumn
hpnicfIKETunOutOctets = _HpnicfIKETunOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 1, 2, 1, 9),
    _HpnicfIKETunOutOctets_Type()
)
hpnicfIKETunOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIKETunOutOctets.setStatus("current")
_HpnicfIKETunOutPkts_Type = Counter64
_HpnicfIKETunOutPkts_Object = MibTableColumn
hpnicfIKETunOutPkts = _HpnicfIKETunOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 1, 2, 1, 10),
    _HpnicfIKETunOutPkts_Type()
)
hpnicfIKETunOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIKETunOutPkts.setStatus("current")
_HpnicfIKETunOutDropPkts_Type = Counter64
_HpnicfIKETunOutDropPkts_Object = MibTableColumn
hpnicfIKETunOutDropPkts = _HpnicfIKETunOutDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 1, 2, 1, 11),
    _HpnicfIKETunOutDropPkts_Type()
)
hpnicfIKETunOutDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIKETunOutDropPkts.setStatus("current")
_HpnicfIKETunOutP2Exchgs_Type = Counter64
_HpnicfIKETunOutP2Exchgs_Object = MibTableColumn
hpnicfIKETunOutP2Exchgs = _HpnicfIKETunOutP2Exchgs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 1, 2, 1, 12),
    _HpnicfIKETunOutP2Exchgs_Type()
)
hpnicfIKETunOutP2Exchgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIKETunOutP2Exchgs.setStatus("current")
_HpnicfIKETunOutP2ExchgRejects_Type = Counter64
_HpnicfIKETunOutP2ExchgRejects_Object = MibTableColumn
hpnicfIKETunOutP2ExchgRejects = _HpnicfIKETunOutP2ExchgRejects_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 1, 2, 1, 13),
    _HpnicfIKETunOutP2ExchgRejects_Type()
)
hpnicfIKETunOutP2ExchgRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIKETunOutP2ExchgRejects.setStatus("current")
_HpnicfIKETunOutP2SaDelRequests_Type = Counter64
_HpnicfIKETunOutP2SaDelRequests_Object = MibTableColumn
hpnicfIKETunOutP2SaDelRequests = _HpnicfIKETunOutP2SaDelRequests_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 1, 2, 1, 14),
    _HpnicfIKETunOutP2SaDelRequests_Type()
)
hpnicfIKETunOutP2SaDelRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIKETunOutP2SaDelRequests.setStatus("current")
_HpnicfIKETunOutP1SaDelRequests_Type = Counter64
_HpnicfIKETunOutP1SaDelRequests_Object = MibTableColumn
hpnicfIKETunOutP1SaDelRequests = _HpnicfIKETunOutP1SaDelRequests_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 1, 2, 1, 15),
    _HpnicfIKETunOutP1SaDelRequests_Type()
)
hpnicfIKETunOutP1SaDelRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIKETunOutP1SaDelRequests.setStatus("current")
_HpnicfIKETunOutNotifys_Type = Counter32
_HpnicfIKETunOutNotifys_Object = MibTableColumn
hpnicfIKETunOutNotifys = _HpnicfIKETunOutNotifys_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 1, 2, 1, 16),
    _HpnicfIKETunOutNotifys_Type()
)
hpnicfIKETunOutNotifys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIKETunOutNotifys.setStatus("current")
_HpnicfIKEGlobalStats_ObjectIdentity = ObjectIdentity
hpnicfIKEGlobalStats = _HpnicfIKEGlobalStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 1, 3)
)
_HpnicfIKEGlobalActiveTunnels_Type = Gauge32
_HpnicfIKEGlobalActiveTunnels_Object = MibScalar
hpnicfIKEGlobalActiveTunnels = _HpnicfIKEGlobalActiveTunnels_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 1, 3, 1),
    _HpnicfIKEGlobalActiveTunnels_Type()
)
hpnicfIKEGlobalActiveTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIKEGlobalActiveTunnels.setStatus("current")
_HpnicfIKEGlobalInOctets_Type = Counter64
_HpnicfIKEGlobalInOctets_Object = MibScalar
hpnicfIKEGlobalInOctets = _HpnicfIKEGlobalInOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 1, 3, 2),
    _HpnicfIKEGlobalInOctets_Type()
)
hpnicfIKEGlobalInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIKEGlobalInOctets.setStatus("current")
_HpnicfIKEGlobalInPkts_Type = Counter64
_HpnicfIKEGlobalInPkts_Object = MibScalar
hpnicfIKEGlobalInPkts = _HpnicfIKEGlobalInPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 1, 3, 3),
    _HpnicfIKEGlobalInPkts_Type()
)
hpnicfIKEGlobalInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIKEGlobalInPkts.setStatus("current")
_HpnicfIKEGlobalInDropPkts_Type = Counter64
_HpnicfIKEGlobalInDropPkts_Object = MibScalar
hpnicfIKEGlobalInDropPkts = _HpnicfIKEGlobalInDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 1, 3, 4),
    _HpnicfIKEGlobalInDropPkts_Type()
)
hpnicfIKEGlobalInDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIKEGlobalInDropPkts.setStatus("current")
_HpnicfIKEGlobalInP2Exchgs_Type = Counter64
_HpnicfIKEGlobalInP2Exchgs_Object = MibScalar
hpnicfIKEGlobalInP2Exchgs = _HpnicfIKEGlobalInP2Exchgs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 1, 3, 5),
    _HpnicfIKEGlobalInP2Exchgs_Type()
)
hpnicfIKEGlobalInP2Exchgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIKEGlobalInP2Exchgs.setStatus("current")
_HpnicfIKEGlobalInP2ExchgRejects_Type = Counter64
_HpnicfIKEGlobalInP2ExchgRejects_Object = MibScalar
hpnicfIKEGlobalInP2ExchgRejects = _HpnicfIKEGlobalInP2ExchgRejects_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 1, 3, 6),
    _HpnicfIKEGlobalInP2ExchgRejects_Type()
)
hpnicfIKEGlobalInP2ExchgRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIKEGlobalInP2ExchgRejects.setStatus("current")
_HpnicfIKEGlobalInP2SaDelRequests_Type = Counter64
_HpnicfIKEGlobalInP2SaDelRequests_Object = MibScalar
hpnicfIKEGlobalInP2SaDelRequests = _HpnicfIKEGlobalInP2SaDelRequests_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 1, 3, 7),
    _HpnicfIKEGlobalInP2SaDelRequests_Type()
)
hpnicfIKEGlobalInP2SaDelRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIKEGlobalInP2SaDelRequests.setStatus("current")
_HpnicfIKEGlobalInNotifys_Type = Counter32
_HpnicfIKEGlobalInNotifys_Object = MibScalar
hpnicfIKEGlobalInNotifys = _HpnicfIKEGlobalInNotifys_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 1, 3, 8),
    _HpnicfIKEGlobalInNotifys_Type()
)
hpnicfIKEGlobalInNotifys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIKEGlobalInNotifys.setStatus("current")
_HpnicfIKEGlobalOutOctets_Type = Counter64
_HpnicfIKEGlobalOutOctets_Object = MibScalar
hpnicfIKEGlobalOutOctets = _HpnicfIKEGlobalOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 1, 3, 9),
    _HpnicfIKEGlobalOutOctets_Type()
)
hpnicfIKEGlobalOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIKEGlobalOutOctets.setStatus("current")
_HpnicfIKEGlobalOutPkts_Type = Counter64
_HpnicfIKEGlobalOutPkts_Object = MibScalar
hpnicfIKEGlobalOutPkts = _HpnicfIKEGlobalOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 1, 3, 10),
    _HpnicfIKEGlobalOutPkts_Type()
)
hpnicfIKEGlobalOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIKEGlobalOutPkts.setStatus("current")
_HpnicfIKEGlobalOutDropPkts_Type = Counter64
_HpnicfIKEGlobalOutDropPkts_Object = MibScalar
hpnicfIKEGlobalOutDropPkts = _HpnicfIKEGlobalOutDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 1, 3, 11),
    _HpnicfIKEGlobalOutDropPkts_Type()
)
hpnicfIKEGlobalOutDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIKEGlobalOutDropPkts.setStatus("current")
_HpnicfIKEGlobalOutP2Exchgs_Type = Counter64
_HpnicfIKEGlobalOutP2Exchgs_Object = MibScalar
hpnicfIKEGlobalOutP2Exchgs = _HpnicfIKEGlobalOutP2Exchgs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 1, 3, 12),
    _HpnicfIKEGlobalOutP2Exchgs_Type()
)
hpnicfIKEGlobalOutP2Exchgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIKEGlobalOutP2Exchgs.setStatus("current")
_HpnicfIKEGlobalOutP2ExchgRejects_Type = Counter64
_HpnicfIKEGlobalOutP2ExchgRejects_Object = MibScalar
hpnicfIKEGlobalOutP2ExchgRejects = _HpnicfIKEGlobalOutP2ExchgRejects_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 1, 3, 13),
    _HpnicfIKEGlobalOutP2ExchgRejects_Type()
)
hpnicfIKEGlobalOutP2ExchgRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIKEGlobalOutP2ExchgRejects.setStatus("current")
_HpnicfIKEGlobalOutP2SaDelRequests_Type = Counter64
_HpnicfIKEGlobalOutP2SaDelRequests_Object = MibScalar
hpnicfIKEGlobalOutP2SaDelRequests = _HpnicfIKEGlobalOutP2SaDelRequests_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 1, 3, 14),
    _HpnicfIKEGlobalOutP2SaDelRequests_Type()
)
hpnicfIKEGlobalOutP2SaDelRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIKEGlobalOutP2SaDelRequests.setStatus("current")
_HpnicfIKEGlobalOutNotifys_Type = Counter32
_HpnicfIKEGlobalOutNotifys_Object = MibScalar
hpnicfIKEGlobalOutNotifys = _HpnicfIKEGlobalOutNotifys_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 1, 3, 15),
    _HpnicfIKEGlobalOutNotifys_Type()
)
hpnicfIKEGlobalOutNotifys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIKEGlobalOutNotifys.setStatus("current")
_HpnicfIKEGlobalInitTunnels_Type = Counter32
_HpnicfIKEGlobalInitTunnels_Object = MibScalar
hpnicfIKEGlobalInitTunnels = _HpnicfIKEGlobalInitTunnels_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 1, 3, 16),
    _HpnicfIKEGlobalInitTunnels_Type()
)
hpnicfIKEGlobalInitTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIKEGlobalInitTunnels.setStatus("current")
_HpnicfIKEGlobalInitTunnelFails_Type = Counter32
_HpnicfIKEGlobalInitTunnelFails_Object = MibScalar
hpnicfIKEGlobalInitTunnelFails = _HpnicfIKEGlobalInitTunnelFails_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 1, 3, 17),
    _HpnicfIKEGlobalInitTunnelFails_Type()
)
hpnicfIKEGlobalInitTunnelFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIKEGlobalInitTunnelFails.setStatus("current")
_HpnicfIKEGlobalRespTunnels_Type = Counter32
_HpnicfIKEGlobalRespTunnels_Object = MibScalar
hpnicfIKEGlobalRespTunnels = _HpnicfIKEGlobalRespTunnels_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 1, 3, 18),
    _HpnicfIKEGlobalRespTunnels_Type()
)
hpnicfIKEGlobalRespTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIKEGlobalRespTunnels.setStatus("current")
_HpnicfIKEGlobalRespTunnelFails_Type = Counter32
_HpnicfIKEGlobalRespTunnelFails_Object = MibScalar
hpnicfIKEGlobalRespTunnelFails = _HpnicfIKEGlobalRespTunnelFails_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 1, 3, 19),
    _HpnicfIKEGlobalRespTunnelFails_Type()
)
hpnicfIKEGlobalRespTunnelFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIKEGlobalRespTunnelFails.setStatus("current")
_HpnicfIKEGlobalAuthFails_Type = Counter32
_HpnicfIKEGlobalAuthFails_Object = MibScalar
hpnicfIKEGlobalAuthFails = _HpnicfIKEGlobalAuthFails_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 1, 3, 20),
    _HpnicfIKEGlobalAuthFails_Type()
)
hpnicfIKEGlobalAuthFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIKEGlobalAuthFails.setStatus("current")
_HpnicfIKEGlobalNoSaFails_Type = Counter32
_HpnicfIKEGlobalNoSaFails_Object = MibScalar
hpnicfIKEGlobalNoSaFails = _HpnicfIKEGlobalNoSaFails_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 1, 3, 21),
    _HpnicfIKEGlobalNoSaFails_Type()
)
hpnicfIKEGlobalNoSaFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIKEGlobalNoSaFails.setStatus("current")
_HpnicfIKEGlobalInvalidCookieFails_Type = Counter32
_HpnicfIKEGlobalInvalidCookieFails_Object = MibScalar
hpnicfIKEGlobalInvalidCookieFails = _HpnicfIKEGlobalInvalidCookieFails_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 1, 3, 22),
    _HpnicfIKEGlobalInvalidCookieFails_Type()
)
hpnicfIKEGlobalInvalidCookieFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIKEGlobalInvalidCookieFails.setStatus("current")
_HpnicfIKEGlobalAttrNotSuppFails_Type = Counter32
_HpnicfIKEGlobalAttrNotSuppFails_Object = MibScalar
hpnicfIKEGlobalAttrNotSuppFails = _HpnicfIKEGlobalAttrNotSuppFails_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 1, 3, 23),
    _HpnicfIKEGlobalAttrNotSuppFails_Type()
)
hpnicfIKEGlobalAttrNotSuppFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIKEGlobalAttrNotSuppFails.setStatus("current")
_HpnicfIKEGlobalNoProposalChosenFails_Type = Counter32
_HpnicfIKEGlobalNoProposalChosenFails_Object = MibScalar
hpnicfIKEGlobalNoProposalChosenFails = _HpnicfIKEGlobalNoProposalChosenFails_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 1, 3, 24),
    _HpnicfIKEGlobalNoProposalChosenFails_Type()
)
hpnicfIKEGlobalNoProposalChosenFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIKEGlobalNoProposalChosenFails.setStatus("current")
_HpnicfIKEGlobalUnsportExchTypeFails_Type = Counter32
_HpnicfIKEGlobalUnsportExchTypeFails_Object = MibScalar
hpnicfIKEGlobalUnsportExchTypeFails = _HpnicfIKEGlobalUnsportExchTypeFails_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 1, 3, 25),
    _HpnicfIKEGlobalUnsportExchTypeFails_Type()
)
hpnicfIKEGlobalUnsportExchTypeFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIKEGlobalUnsportExchTypeFails.setStatus("current")
_HpnicfIKEGlobalInvalidIdFails_Type = Counter32
_HpnicfIKEGlobalInvalidIdFails_Object = MibScalar
hpnicfIKEGlobalInvalidIdFails = _HpnicfIKEGlobalInvalidIdFails_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 1, 3, 26),
    _HpnicfIKEGlobalInvalidIdFails_Type()
)
hpnicfIKEGlobalInvalidIdFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIKEGlobalInvalidIdFails.setStatus("current")
_HpnicfIKEGlobalInvalidProFails_Type = Counter32
_HpnicfIKEGlobalInvalidProFails_Object = MibScalar
hpnicfIKEGlobalInvalidProFails = _HpnicfIKEGlobalInvalidProFails_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 1, 3, 27),
    _HpnicfIKEGlobalInvalidProFails_Type()
)
hpnicfIKEGlobalInvalidProFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIKEGlobalInvalidProFails.setStatus("current")
_HpnicfIKEGlobalCertTypeUnsuppFails_Type = Counter32
_HpnicfIKEGlobalCertTypeUnsuppFails_Object = MibScalar
hpnicfIKEGlobalCertTypeUnsuppFails = _HpnicfIKEGlobalCertTypeUnsuppFails_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 1, 3, 28),
    _HpnicfIKEGlobalCertTypeUnsuppFails_Type()
)
hpnicfIKEGlobalCertTypeUnsuppFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIKEGlobalCertTypeUnsuppFails.setStatus("current")
_HpnicfIKEGlobalInvalidCertAuthFails_Type = Counter32
_HpnicfIKEGlobalInvalidCertAuthFails_Object = MibScalar
hpnicfIKEGlobalInvalidCertAuthFails = _HpnicfIKEGlobalInvalidCertAuthFails_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 1, 3, 29),
    _HpnicfIKEGlobalInvalidCertAuthFails_Type()
)
hpnicfIKEGlobalInvalidCertAuthFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIKEGlobalInvalidCertAuthFails.setStatus("current")
_HpnicfIKEGlobalInvalidSignFails_Type = Counter32
_HpnicfIKEGlobalInvalidSignFails_Object = MibScalar
hpnicfIKEGlobalInvalidSignFails = _HpnicfIKEGlobalInvalidSignFails_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 1, 3, 30),
    _HpnicfIKEGlobalInvalidSignFails_Type()
)
hpnicfIKEGlobalInvalidSignFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIKEGlobalInvalidSignFails.setStatus("current")
_HpnicfIKEGlobalCertUnavailableFails_Type = Counter32
_HpnicfIKEGlobalCertUnavailableFails_Object = MibScalar
hpnicfIKEGlobalCertUnavailableFails = _HpnicfIKEGlobalCertUnavailableFails_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 1, 3, 31),
    _HpnicfIKEGlobalCertUnavailableFails_Type()
)
hpnicfIKEGlobalCertUnavailableFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIKEGlobalCertUnavailableFails.setStatus("current")
_HpnicfIKETrapObject_ObjectIdentity = ObjectIdentity
hpnicfIKETrapObject = _HpnicfIKETrapObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 1, 4)
)
_HpnicfIKEProposalNumber_Type = Integer32
_HpnicfIKEProposalNumber_Object = MibScalar
hpnicfIKEProposalNumber = _HpnicfIKEProposalNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 1, 4, 1),
    _HpnicfIKEProposalNumber_Type()
)
hpnicfIKEProposalNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfIKEProposalNumber.setStatus("current")
_HpnicfIKEProposalSize_Type = Integer32
_HpnicfIKEProposalSize_Object = MibScalar
hpnicfIKEProposalSize = _HpnicfIKEProposalSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 1, 4, 2),
    _HpnicfIKEProposalSize_Type()
)
hpnicfIKEProposalSize.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfIKEProposalSize.setStatus("current")
_HpnicfIKEIdInformation_Type = DisplayString
_HpnicfIKEIdInformation_Object = MibScalar
hpnicfIKEIdInformation = _HpnicfIKEIdInformation_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 1, 4, 3),
    _HpnicfIKEIdInformation_Type()
)
hpnicfIKEIdInformation.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfIKEIdInformation.setStatus("current")
_HpnicfIKEProtocolNum_Type = Integer32
_HpnicfIKEProtocolNum_Object = MibScalar
hpnicfIKEProtocolNum = _HpnicfIKEProtocolNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 1, 4, 4),
    _HpnicfIKEProtocolNum_Type()
)
hpnicfIKEProtocolNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfIKEProtocolNum.setStatus("current")
_HpnicfIKECertInformation_Type = DisplayString
_HpnicfIKECertInformation_Object = MibScalar
hpnicfIKECertInformation = _HpnicfIKECertInformation_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 1, 4, 5),
    _HpnicfIKECertInformation_Type()
)
hpnicfIKECertInformation.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfIKECertInformation.setStatus("current")
_HpnicfIKETrapCntl_ObjectIdentity = ObjectIdentity
hpnicfIKETrapCntl = _HpnicfIKETrapCntl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 1, 5)
)
_HpnicfIKETrapGlobalCntl_Type = HpnicfTrapStatus
_HpnicfIKETrapGlobalCntl_Object = MibScalar
hpnicfIKETrapGlobalCntl = _HpnicfIKETrapGlobalCntl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 1, 5, 1),
    _HpnicfIKETrapGlobalCntl_Type()
)
hpnicfIKETrapGlobalCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfIKETrapGlobalCntl.setStatus("current")
_HpnicfIKETunnelStartTrapCntl_Type = HpnicfTrapStatus
_HpnicfIKETunnelStartTrapCntl_Object = MibScalar
hpnicfIKETunnelStartTrapCntl = _HpnicfIKETunnelStartTrapCntl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 1, 5, 2),
    _HpnicfIKETunnelStartTrapCntl_Type()
)
hpnicfIKETunnelStartTrapCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfIKETunnelStartTrapCntl.setStatus("current")
_HpnicfIKETunnelStopTrapCntl_Type = HpnicfTrapStatus
_HpnicfIKETunnelStopTrapCntl_Object = MibScalar
hpnicfIKETunnelStopTrapCntl = _HpnicfIKETunnelStopTrapCntl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 1, 5, 3),
    _HpnicfIKETunnelStopTrapCntl_Type()
)
hpnicfIKETunnelStopTrapCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfIKETunnelStopTrapCntl.setStatus("current")
_HpnicfIKENoSaTrapCntl_Type = HpnicfTrapStatus
_HpnicfIKENoSaTrapCntl_Object = MibScalar
hpnicfIKENoSaTrapCntl = _HpnicfIKENoSaTrapCntl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 1, 5, 4),
    _HpnicfIKENoSaTrapCntl_Type()
)
hpnicfIKENoSaTrapCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfIKENoSaTrapCntl.setStatus("current")
_HpnicfIKEEncryFailureTrapCntl_Type = HpnicfTrapStatus
_HpnicfIKEEncryFailureTrapCntl_Object = MibScalar
hpnicfIKEEncryFailureTrapCntl = _HpnicfIKEEncryFailureTrapCntl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 1, 5, 5),
    _HpnicfIKEEncryFailureTrapCntl_Type()
)
hpnicfIKEEncryFailureTrapCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfIKEEncryFailureTrapCntl.setStatus("current")
_HpnicfIKEDecryFailureTrapCntl_Type = HpnicfTrapStatus
_HpnicfIKEDecryFailureTrapCntl_Object = MibScalar
hpnicfIKEDecryFailureTrapCntl = _HpnicfIKEDecryFailureTrapCntl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 1, 5, 6),
    _HpnicfIKEDecryFailureTrapCntl_Type()
)
hpnicfIKEDecryFailureTrapCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfIKEDecryFailureTrapCntl.setStatus("current")
_HpnicfIKEInvalidProposalTrapCntl_Type = HpnicfTrapStatus
_HpnicfIKEInvalidProposalTrapCntl_Object = MibScalar
hpnicfIKEInvalidProposalTrapCntl = _HpnicfIKEInvalidProposalTrapCntl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 1, 5, 7),
    _HpnicfIKEInvalidProposalTrapCntl_Type()
)
hpnicfIKEInvalidProposalTrapCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfIKEInvalidProposalTrapCntl.setStatus("current")
_HpnicfIKEAuthFailTrapCntl_Type = HpnicfTrapStatus
_HpnicfIKEAuthFailTrapCntl_Object = MibScalar
hpnicfIKEAuthFailTrapCntl = _HpnicfIKEAuthFailTrapCntl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 1, 5, 8),
    _HpnicfIKEAuthFailTrapCntl_Type()
)
hpnicfIKEAuthFailTrapCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfIKEAuthFailTrapCntl.setStatus("current")
_HpnicfIKEInvalidCookieTrapCntl_Type = HpnicfTrapStatus
_HpnicfIKEInvalidCookieTrapCntl_Object = MibScalar
hpnicfIKEInvalidCookieTrapCntl = _HpnicfIKEInvalidCookieTrapCntl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 1, 5, 9),
    _HpnicfIKEInvalidCookieTrapCntl_Type()
)
hpnicfIKEInvalidCookieTrapCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfIKEInvalidCookieTrapCntl.setStatus("current")
_HpnicfIKEInvalidSpiTrapCntl_Type = HpnicfTrapStatus
_HpnicfIKEInvalidSpiTrapCntl_Object = MibScalar
hpnicfIKEInvalidSpiTrapCntl = _HpnicfIKEInvalidSpiTrapCntl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 1, 5, 10),
    _HpnicfIKEInvalidSpiTrapCntl_Type()
)
hpnicfIKEInvalidSpiTrapCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfIKEInvalidSpiTrapCntl.setStatus("current")
_HpnicfIKEAttrNotSuppTrapCntl_Type = HpnicfTrapStatus
_HpnicfIKEAttrNotSuppTrapCntl_Object = MibScalar
hpnicfIKEAttrNotSuppTrapCntl = _HpnicfIKEAttrNotSuppTrapCntl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 1, 5, 11),
    _HpnicfIKEAttrNotSuppTrapCntl_Type()
)
hpnicfIKEAttrNotSuppTrapCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfIKEAttrNotSuppTrapCntl.setStatus("current")
_HpnicfIKEUnsportExchTypeTrapCntl_Type = HpnicfTrapStatus
_HpnicfIKEUnsportExchTypeTrapCntl_Object = MibScalar
hpnicfIKEUnsportExchTypeTrapCntl = _HpnicfIKEUnsportExchTypeTrapCntl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 1, 5, 12),
    _HpnicfIKEUnsportExchTypeTrapCntl_Type()
)
hpnicfIKEUnsportExchTypeTrapCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfIKEUnsportExchTypeTrapCntl.setStatus("current")
_HpnicfIKEInvalidIdTrapCntl_Type = HpnicfTrapStatus
_HpnicfIKEInvalidIdTrapCntl_Object = MibScalar
hpnicfIKEInvalidIdTrapCntl = _HpnicfIKEInvalidIdTrapCntl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 1, 5, 13),
    _HpnicfIKEInvalidIdTrapCntl_Type()
)
hpnicfIKEInvalidIdTrapCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfIKEInvalidIdTrapCntl.setStatus("current")
_HpnicfIKEInvalidProtocolTrapCntl_Type = HpnicfTrapStatus
_HpnicfIKEInvalidProtocolTrapCntl_Object = MibScalar
hpnicfIKEInvalidProtocolTrapCntl = _HpnicfIKEInvalidProtocolTrapCntl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 1, 5, 14),
    _HpnicfIKEInvalidProtocolTrapCntl_Type()
)
hpnicfIKEInvalidProtocolTrapCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfIKEInvalidProtocolTrapCntl.setStatus("current")
_HpnicfIKECertTypeUnsuppTrapCntl_Type = HpnicfTrapStatus
_HpnicfIKECertTypeUnsuppTrapCntl_Object = MibScalar
hpnicfIKECertTypeUnsuppTrapCntl = _HpnicfIKECertTypeUnsuppTrapCntl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 1, 5, 15),
    _HpnicfIKECertTypeUnsuppTrapCntl_Type()
)
hpnicfIKECertTypeUnsuppTrapCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfIKECertTypeUnsuppTrapCntl.setStatus("current")
_HpnicfIKEInvalidCertAuthTrapCntl_Type = HpnicfTrapStatus
_HpnicfIKEInvalidCertAuthTrapCntl_Object = MibScalar
hpnicfIKEInvalidCertAuthTrapCntl = _HpnicfIKEInvalidCertAuthTrapCntl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 1, 5, 16),
    _HpnicfIKEInvalidCertAuthTrapCntl_Type()
)
hpnicfIKEInvalidCertAuthTrapCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfIKEInvalidCertAuthTrapCntl.setStatus("current")
_HpnicfIKEInvalidSignTrapCntl_Type = HpnicfTrapStatus
_HpnicfIKEInvalidSignTrapCntl_Object = MibScalar
hpnicfIKEInvalidSignTrapCntl = _HpnicfIKEInvalidSignTrapCntl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 1, 5, 17),
    _HpnicfIKEInvalidSignTrapCntl_Type()
)
hpnicfIKEInvalidSignTrapCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfIKEInvalidSignTrapCntl.setStatus("current")
_HpnicfIKECertUnavailableTrapCntl_Type = HpnicfTrapStatus
_HpnicfIKECertUnavailableTrapCntl_Object = MibScalar
hpnicfIKECertUnavailableTrapCntl = _HpnicfIKECertUnavailableTrapCntl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 1, 5, 18),
    _HpnicfIKECertUnavailableTrapCntl_Type()
)
hpnicfIKECertUnavailableTrapCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfIKECertUnavailableTrapCntl.setStatus("current")
_HpnicfIKEProposalAddTrapCntl_Type = HpnicfTrapStatus
_HpnicfIKEProposalAddTrapCntl_Object = MibScalar
hpnicfIKEProposalAddTrapCntl = _HpnicfIKEProposalAddTrapCntl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 1, 5, 19),
    _HpnicfIKEProposalAddTrapCntl_Type()
)
hpnicfIKEProposalAddTrapCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfIKEProposalAddTrapCntl.setStatus("current")
_HpnicfIKEProposalDelTrapCntl_Type = HpnicfTrapStatus
_HpnicfIKEProposalDelTrapCntl_Object = MibScalar
hpnicfIKEProposalDelTrapCntl = _HpnicfIKEProposalDelTrapCntl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 1, 5, 20),
    _HpnicfIKEProposalDelTrapCntl_Type()
)
hpnicfIKEProposalDelTrapCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfIKEProposalDelTrapCntl.setStatus("current")
_HpnicfIKETrap_ObjectIdentity = ObjectIdentity
hpnicfIKETrap = _HpnicfIKETrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 1, 6)
)
_HpnicfIKENotifications_ObjectIdentity = ObjectIdentity
hpnicfIKENotifications = _HpnicfIKENotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 1, 6, 1)
)
_HpnicfIKEScalarObjects_ObjectIdentity = ObjectIdentity
hpnicfIKEScalarObjects = _HpnicfIKEScalarObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 1, 7)
)
_HpnicfIKEMIBVersion_Type = DisplayString
_HpnicfIKEMIBVersion_Object = MibScalar
hpnicfIKEMIBVersion = _HpnicfIKEMIBVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 1, 7, 1),
    _HpnicfIKEMIBVersion_Type()
)
hpnicfIKEMIBVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIKEMIBVersion.setStatus("current")
_HpnicfIKEConformance_ObjectIdentity = ObjectIdentity
hpnicfIKEConformance = _HpnicfIKEConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 2)
)
_HpnicfIKECompliances_ObjectIdentity = ObjectIdentity
hpnicfIKECompliances = _HpnicfIKECompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 2, 1)
)
_HpnicfIKEGroups_ObjectIdentity = ObjectIdentity
hpnicfIKEGroups = _HpnicfIKEGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 2, 2)
)

# Managed Objects groups

hpnicfIKETunnelTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 2, 2, 1)
)
hpnicfIKETunnelTableGroup.setObjects(
      *(("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunLocalType"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunLocalValue1"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunLocalValue2"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunLocalAddr"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunRemoteType"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunRemoteValue1"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunRemoteValue2"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunRemoteAddr"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunInitiator"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunNegoMode"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunDiffHellmanGrp"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunEncryptAlgo"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunHashAlgo"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunAuthMethod"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunLifeTime"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunActiveTime"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunRemainTime"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunTotalRefreshes"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunState"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunDpdIntervalTime"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunDpdTimeOut"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunLocalInetAddrType"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunLocalInetAddr"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunRemoteInetAddrType"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunRemoteInetAddr"))
)
if mibBuilder.loadTexts:
    hpnicfIKETunnelTableGroup.setStatus("current")

hpnicfIKETunnelStatTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 2, 2, 2)
)
hpnicfIKETunnelStatTableGroup.setObjects(
      *(("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunInOctets"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunInPkts"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunInDropPkts"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunInP2Exchgs"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunInP2ExchgRejets"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunInP2SaDelRequests"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunInP1SaDelRequests"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunInNotifys"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunOutOctets"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunOutPkts"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunOutDropPkts"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunOutP2Exchgs"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunOutP2ExchgRejects"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunOutP2SaDelRequests"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunOutP1SaDelRequests"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunOutNotifys"))
)
if mibBuilder.loadTexts:
    hpnicfIKETunnelStatTableGroup.setStatus("current")

hpnicfIKEGlobalStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 2, 2, 3)
)
hpnicfIKEGlobalStatsGroup.setObjects(
      *(("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKEGlobalActiveTunnels"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKEGlobalInOctets"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKEGlobalInPkts"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKEGlobalInDropPkts"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKEGlobalInP2Exchgs"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKEGlobalInP2ExchgRejects"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKEGlobalInP2SaDelRequests"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKEGlobalInNotifys"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKEGlobalOutOctets"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKEGlobalOutPkts"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKEGlobalOutDropPkts"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKEGlobalOutP2Exchgs"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKEGlobalOutP2ExchgRejects"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKEGlobalOutP2SaDelRequests"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKEGlobalOutNotifys"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKEGlobalInitTunnels"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKEGlobalInitTunnelFails"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKEGlobalRespTunnels"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKEGlobalRespTunnelFails"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKEGlobalAuthFails"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKEGlobalNoSaFails"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKEGlobalInvalidCookieFails"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKEGlobalAttrNotSuppFails"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKEGlobalNoProposalChosenFails"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKEGlobalUnsportExchTypeFails"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKEGlobalInvalidIdFails"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKEGlobalInvalidProFails"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKEGlobalCertTypeUnsuppFails"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKEGlobalInvalidCertAuthFails"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKEGlobalInvalidSignFails"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKEGlobalCertUnavailableFails"))
)
if mibBuilder.loadTexts:
    hpnicfIKEGlobalStatsGroup.setStatus("current")

hpnicfIKETrapObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 2, 2, 4)
)
hpnicfIKETrapObjectGroup.setObjects(
      *(("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKEProposalNumber"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKEProposalSize"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKEIdInformation"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKEProtocolNum"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKECertInformation"))
)
if mibBuilder.loadTexts:
    hpnicfIKETrapObjectGroup.setStatus("current")

hpnicfIKETrapCntlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 2, 2, 5)
)
hpnicfIKETrapCntlGroup.setObjects(
      *(("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETrapGlobalCntl"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunnelStartTrapCntl"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunnelStopTrapCntl"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKENoSaTrapCntl"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKEEncryFailureTrapCntl"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKEDecryFailureTrapCntl"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKEInvalidProposalTrapCntl"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKEAuthFailTrapCntl"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKEInvalidCookieTrapCntl"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKEInvalidSpiTrapCntl"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKEAttrNotSuppTrapCntl"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKEUnsportExchTypeTrapCntl"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKEInvalidIdTrapCntl"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKEInvalidProtocolTrapCntl"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKECertTypeUnsuppTrapCntl"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKEInvalidCertAuthTrapCntl"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKEInvalidSignTrapCntl"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKECertUnavailableTrapCntl"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKEProposalAddTrapCntl"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKEProposalDelTrapCntl"))
)
if mibBuilder.loadTexts:
    hpnicfIKETrapCntlGroup.setStatus("current")

hpnicfIKEScalarObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 2, 2, 7)
)
hpnicfIKEScalarObjectsGroup.setObjects(
    ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKEMIBVersion")
)
if mibBuilder.loadTexts:
    hpnicfIKEScalarObjectsGroup.setStatus("current")


# Notification objects

hpnicfIKETunnelStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 1, 6, 1, 1)
)
hpnicfIKETunnelStart.setObjects(
      *(("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunLocalAddr"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunRemoteAddr"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunLifeTime"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunIndex"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunLocalInetAddrType"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunLocalInetAddr"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunRemoteInetAddrType"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunRemoteInetAddr"))
)
if mibBuilder.loadTexts:
    hpnicfIKETunnelStart.setStatus(
        "current"
    )

hpnicfIKETunnelStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 1, 6, 1, 2)
)
hpnicfIKETunnelStop.setObjects(
      *(("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunLocalAddr"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunRemoteAddr"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunActiveTime"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunIndex"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunLocalInetAddrType"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunLocalInetAddr"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunRemoteInetAddrType"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunRemoteInetAddr"))
)
if mibBuilder.loadTexts:
    hpnicfIKETunnelStop.setStatus(
        "current"
    )

hpnicfIKENoSaFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 1, 6, 1, 3)
)
hpnicfIKENoSaFailure.setObjects(
      *(("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunLocalAddr"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunRemoteAddr"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunIndex"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunLocalInetAddrType"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunLocalInetAddr"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunRemoteInetAddrType"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunRemoteInetAddr"))
)
if mibBuilder.loadTexts:
    hpnicfIKENoSaFailure.setStatus(
        "current"
    )

hpnicfIKEEncryFailFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 1, 6, 1, 4)
)
hpnicfIKEEncryFailFailure.setObjects(
      *(("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunLocalAddr"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunRemoteAddr"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunIndex"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunLocalInetAddrType"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunLocalInetAddr"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunRemoteInetAddrType"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunRemoteInetAddr"))
)
if mibBuilder.loadTexts:
    hpnicfIKEEncryFailFailure.setStatus(
        "current"
    )

hpnicfIKEDecryFailFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 1, 6, 1, 5)
)
hpnicfIKEDecryFailFailure.setObjects(
      *(("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunLocalAddr"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunRemoteAddr"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunIndex"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunLocalInetAddrType"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunLocalInetAddr"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunRemoteInetAddrType"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunRemoteInetAddr"))
)
if mibBuilder.loadTexts:
    hpnicfIKEDecryFailFailure.setStatus(
        "current"
    )

hpnicfIKEInvalidProposalFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 1, 6, 1, 6)
)
hpnicfIKEInvalidProposalFailure.setObjects(
      *(("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunLocalAddr"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunRemoteAddr"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunIndex"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunLocalInetAddrType"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunLocalInetAddr"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunRemoteInetAddrType"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunRemoteInetAddr"))
)
if mibBuilder.loadTexts:
    hpnicfIKEInvalidProposalFailure.setStatus(
        "current"
    )

hpnicfIKEAuthFailFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 1, 6, 1, 7)
)
hpnicfIKEAuthFailFailure.setObjects(
      *(("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunLocalAddr"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunRemoteAddr"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunIndex"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunLocalInetAddrType"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunLocalInetAddr"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunRemoteInetAddrType"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunRemoteInetAddr"))
)
if mibBuilder.loadTexts:
    hpnicfIKEAuthFailFailure.setStatus(
        "current"
    )

hpnicfIKEInvalidCookieFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 1, 6, 1, 8)
)
hpnicfIKEInvalidCookieFailure.setObjects(
      *(("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunLocalAddr"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunRemoteAddr"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunIndex"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunLocalInetAddrType"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunLocalInetAddr"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunRemoteInetAddrType"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunRemoteInetAddr"))
)
if mibBuilder.loadTexts:
    hpnicfIKEInvalidCookieFailure.setStatus(
        "current"
    )

hpnicfIKEAttrNotSuppFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 1, 6, 1, 9)
)
hpnicfIKEAttrNotSuppFailure.setObjects(
      *(("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunLocalAddr"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunRemoteAddr"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunIndex"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunLocalInetAddrType"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunLocalInetAddr"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunRemoteInetAddrType"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunRemoteInetAddr"))
)
if mibBuilder.loadTexts:
    hpnicfIKEAttrNotSuppFailure.setStatus(
        "current"
    )

hpnicfIKEUnsportExchTypeFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 1, 6, 1, 10)
)
hpnicfIKEUnsportExchTypeFailure.setObjects(
      *(("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunLocalAddr"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunRemoteAddr"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunIndex"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunLocalInetAddrType"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunLocalInetAddr"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunRemoteInetAddrType"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunRemoteInetAddr"))
)
if mibBuilder.loadTexts:
    hpnicfIKEUnsportExchTypeFailure.setStatus(
        "current"
    )

hpnicfIKEInvalidIdFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 1, 6, 1, 11)
)
hpnicfIKEInvalidIdFailure.setObjects(
      *(("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunLocalAddr"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunRemoteAddr"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKEIdInformation"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunIndex"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunLocalInetAddrType"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunLocalInetAddr"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunRemoteInetAddrType"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunRemoteInetAddr"))
)
if mibBuilder.loadTexts:
    hpnicfIKEInvalidIdFailure.setStatus(
        "current"
    )

hpnicfIKEInvalidProtocolFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 1, 6, 1, 12)
)
hpnicfIKEInvalidProtocolFailure.setObjects(
      *(("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunLocalAddr"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunRemoteAddr"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKEProtocolNum"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunIndex"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunLocalInetAddrType"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunLocalInetAddr"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunRemoteInetAddrType"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunRemoteInetAddr"))
)
if mibBuilder.loadTexts:
    hpnicfIKEInvalidProtocolFailure.setStatus(
        "current"
    )

hpnicfIKECertTypeUnsuppFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 1, 6, 1, 13)
)
hpnicfIKECertTypeUnsuppFailure.setObjects(
      *(("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunLocalAddr"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunRemoteAddr"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKECertInformation"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunIndex"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunLocalInetAddrType"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunLocalInetAddr"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunRemoteInetAddrType"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunRemoteInetAddr"))
)
if mibBuilder.loadTexts:
    hpnicfIKECertTypeUnsuppFailure.setStatus(
        "current"
    )

hpnicfIKEInvalidCertAuthFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 1, 6, 1, 14)
)
hpnicfIKEInvalidCertAuthFailure.setObjects(
      *(("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunLocalAddr"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunRemoteAddr"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKECertInformation"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunIndex"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunLocalInetAddrType"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunLocalInetAddr"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunRemoteInetAddrType"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunRemoteInetAddr"))
)
if mibBuilder.loadTexts:
    hpnicfIKEInvalidCertAuthFailure.setStatus(
        "current"
    )

hpnicfIKElInvalidSignFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 1, 6, 1, 15)
)
hpnicfIKElInvalidSignFailure.setObjects(
      *(("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunLocalAddr"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunRemoteAddr"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKECertInformation"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunIndex"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunLocalInetAddrType"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunLocalInetAddr"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunRemoteInetAddrType"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunRemoteInetAddr"))
)
if mibBuilder.loadTexts:
    hpnicfIKElInvalidSignFailure.setStatus(
        "current"
    )

hpnicfIKECertUnavailableFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 1, 6, 1, 16)
)
hpnicfIKECertUnavailableFailure.setObjects(
      *(("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunLocalAddr"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunRemoteAddr"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKECertInformation"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunIndex"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunLocalInetAddrType"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunLocalInetAddr"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunRemoteInetAddrType"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunRemoteInetAddr"))
)
if mibBuilder.loadTexts:
    hpnicfIKECertUnavailableFailure.setStatus(
        "current"
    )

hpnicfIKEProposalAdd = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 1, 6, 1, 17)
)
hpnicfIKEProposalAdd.setObjects(
      *(("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKEProposalNumber"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKEProposalSize"))
)
if mibBuilder.loadTexts:
    hpnicfIKEProposalAdd.setStatus(
        "current"
    )

hpnicfIKEProposalDel = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 1, 6, 1, 18)
)
hpnicfIKEProposalDel.setObjects(
      *(("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKEProposalNumber"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKEProposalSize"))
)
if mibBuilder.loadTexts:
    hpnicfIKEProposalDel.setStatus(
        "current"
    )


# Notifications groups

hpnicfIKETrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 2, 2, 6)
)
hpnicfIKETrapGroup.setObjects(
      *(("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunnelStart"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKETunnelStop"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKENoSaFailure"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKEEncryFailFailure"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKEDecryFailFailure"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKEInvalidProposalFailure"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKEAuthFailFailure"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKEInvalidCookieFailure"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKEAttrNotSuppFailure"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKEUnsportExchTypeFailure"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKEInvalidIdFailure"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKEInvalidProtocolFailure"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKECertTypeUnsuppFailure"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKEInvalidCertAuthFailure"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKElInvalidSignFailure"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKECertUnavailableFailure"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKEProposalAdd"),
        ("HPN-ICF-IKE-MONITOR-MIB", "hpnicfIKEProposalDel"))
)
if mibBuilder.loadTexts:
    hpnicfIKETrapGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hpnicfIKECompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hpnicfIKECompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-IKE-MONITOR-MIB",
    **{"HpnicfIKENegoMode": HpnicfIKENegoMode,
       "HpnicfIKEAuthMethod": HpnicfIKEAuthMethod,
       "HpnicfDiffHellmanGrp": HpnicfDiffHellmanGrp,
       "HpnicfEncryptAlgo": HpnicfEncryptAlgo,
       "HpnicfAuthAlgo": HpnicfAuthAlgo,
       "HpnicfSaProtocol": HpnicfSaProtocol,
       "HpnicfTrapStatus": HpnicfTrapStatus,
       "HpnicfIKEIDType": HpnicfIKEIDType,
       "HpnicfTrafficType": HpnicfTrafficType,
       "HpnicfIKETunnelState": HpnicfIKETunnelState,
       "hpnicfIKEMonitor": hpnicfIKEMonitor,
       "hpnicfIKEObjects": hpnicfIKEObjects,
       "hpnicfIKETunnelTable": hpnicfIKETunnelTable,
       "hpnicfIKETunnelEntry": hpnicfIKETunnelEntry,
       "hpnicfIKETunIndex": hpnicfIKETunIndex,
       "hpnicfIKETunLocalType": hpnicfIKETunLocalType,
       "hpnicfIKETunLocalValue1": hpnicfIKETunLocalValue1,
       "hpnicfIKETunLocalValue2": hpnicfIKETunLocalValue2,
       "hpnicfIKETunLocalAddr": hpnicfIKETunLocalAddr,
       "hpnicfIKETunRemoteType": hpnicfIKETunRemoteType,
       "hpnicfIKETunRemoteValue1": hpnicfIKETunRemoteValue1,
       "hpnicfIKETunRemoteValue2": hpnicfIKETunRemoteValue2,
       "hpnicfIKETunRemoteAddr": hpnicfIKETunRemoteAddr,
       "hpnicfIKETunInitiator": hpnicfIKETunInitiator,
       "hpnicfIKETunNegoMode": hpnicfIKETunNegoMode,
       "hpnicfIKETunDiffHellmanGrp": hpnicfIKETunDiffHellmanGrp,
       "hpnicfIKETunEncryptAlgo": hpnicfIKETunEncryptAlgo,
       "hpnicfIKETunHashAlgo": hpnicfIKETunHashAlgo,
       "hpnicfIKETunAuthMethod": hpnicfIKETunAuthMethod,
       "hpnicfIKETunLifeTime": hpnicfIKETunLifeTime,
       "hpnicfIKETunActiveTime": hpnicfIKETunActiveTime,
       "hpnicfIKETunRemainTime": hpnicfIKETunRemainTime,
       "hpnicfIKETunTotalRefreshes": hpnicfIKETunTotalRefreshes,
       "hpnicfIKETunState": hpnicfIKETunState,
       "hpnicfIKETunDpdIntervalTime": hpnicfIKETunDpdIntervalTime,
       "hpnicfIKETunDpdTimeOut": hpnicfIKETunDpdTimeOut,
       "hpnicfIKETunLocalInetAddrType": hpnicfIKETunLocalInetAddrType,
       "hpnicfIKETunLocalInetAddr": hpnicfIKETunLocalInetAddr,
       "hpnicfIKETunRemoteInetAddrType": hpnicfIKETunRemoteInetAddrType,
       "hpnicfIKETunRemoteInetAddr": hpnicfIKETunRemoteInetAddr,
       "hpnicfIKETunnelStatTable": hpnicfIKETunnelStatTable,
       "hpnicfIKETunnelStatEntry": hpnicfIKETunnelStatEntry,
       "hpnicfIKETunInOctets": hpnicfIKETunInOctets,
       "hpnicfIKETunInPkts": hpnicfIKETunInPkts,
       "hpnicfIKETunInDropPkts": hpnicfIKETunInDropPkts,
       "hpnicfIKETunInP2Exchgs": hpnicfIKETunInP2Exchgs,
       "hpnicfIKETunInP2ExchgRejets": hpnicfIKETunInP2ExchgRejets,
       "hpnicfIKETunInP2SaDelRequests": hpnicfIKETunInP2SaDelRequests,
       "hpnicfIKETunInP1SaDelRequests": hpnicfIKETunInP1SaDelRequests,
       "hpnicfIKETunInNotifys": hpnicfIKETunInNotifys,
       "hpnicfIKETunOutOctets": hpnicfIKETunOutOctets,
       "hpnicfIKETunOutPkts": hpnicfIKETunOutPkts,
       "hpnicfIKETunOutDropPkts": hpnicfIKETunOutDropPkts,
       "hpnicfIKETunOutP2Exchgs": hpnicfIKETunOutP2Exchgs,
       "hpnicfIKETunOutP2ExchgRejects": hpnicfIKETunOutP2ExchgRejects,
       "hpnicfIKETunOutP2SaDelRequests": hpnicfIKETunOutP2SaDelRequests,
       "hpnicfIKETunOutP1SaDelRequests": hpnicfIKETunOutP1SaDelRequests,
       "hpnicfIKETunOutNotifys": hpnicfIKETunOutNotifys,
       "hpnicfIKEGlobalStats": hpnicfIKEGlobalStats,
       "hpnicfIKEGlobalActiveTunnels": hpnicfIKEGlobalActiveTunnels,
       "hpnicfIKEGlobalInOctets": hpnicfIKEGlobalInOctets,
       "hpnicfIKEGlobalInPkts": hpnicfIKEGlobalInPkts,
       "hpnicfIKEGlobalInDropPkts": hpnicfIKEGlobalInDropPkts,
       "hpnicfIKEGlobalInP2Exchgs": hpnicfIKEGlobalInP2Exchgs,
       "hpnicfIKEGlobalInP2ExchgRejects": hpnicfIKEGlobalInP2ExchgRejects,
       "hpnicfIKEGlobalInP2SaDelRequests": hpnicfIKEGlobalInP2SaDelRequests,
       "hpnicfIKEGlobalInNotifys": hpnicfIKEGlobalInNotifys,
       "hpnicfIKEGlobalOutOctets": hpnicfIKEGlobalOutOctets,
       "hpnicfIKEGlobalOutPkts": hpnicfIKEGlobalOutPkts,
       "hpnicfIKEGlobalOutDropPkts": hpnicfIKEGlobalOutDropPkts,
       "hpnicfIKEGlobalOutP2Exchgs": hpnicfIKEGlobalOutP2Exchgs,
       "hpnicfIKEGlobalOutP2ExchgRejects": hpnicfIKEGlobalOutP2ExchgRejects,
       "hpnicfIKEGlobalOutP2SaDelRequests": hpnicfIKEGlobalOutP2SaDelRequests,
       "hpnicfIKEGlobalOutNotifys": hpnicfIKEGlobalOutNotifys,
       "hpnicfIKEGlobalInitTunnels": hpnicfIKEGlobalInitTunnels,
       "hpnicfIKEGlobalInitTunnelFails": hpnicfIKEGlobalInitTunnelFails,
       "hpnicfIKEGlobalRespTunnels": hpnicfIKEGlobalRespTunnels,
       "hpnicfIKEGlobalRespTunnelFails": hpnicfIKEGlobalRespTunnelFails,
       "hpnicfIKEGlobalAuthFails": hpnicfIKEGlobalAuthFails,
       "hpnicfIKEGlobalNoSaFails": hpnicfIKEGlobalNoSaFails,
       "hpnicfIKEGlobalInvalidCookieFails": hpnicfIKEGlobalInvalidCookieFails,
       "hpnicfIKEGlobalAttrNotSuppFails": hpnicfIKEGlobalAttrNotSuppFails,
       "hpnicfIKEGlobalNoProposalChosenFails": hpnicfIKEGlobalNoProposalChosenFails,
       "hpnicfIKEGlobalUnsportExchTypeFails": hpnicfIKEGlobalUnsportExchTypeFails,
       "hpnicfIKEGlobalInvalidIdFails": hpnicfIKEGlobalInvalidIdFails,
       "hpnicfIKEGlobalInvalidProFails": hpnicfIKEGlobalInvalidProFails,
       "hpnicfIKEGlobalCertTypeUnsuppFails": hpnicfIKEGlobalCertTypeUnsuppFails,
       "hpnicfIKEGlobalInvalidCertAuthFails": hpnicfIKEGlobalInvalidCertAuthFails,
       "hpnicfIKEGlobalInvalidSignFails": hpnicfIKEGlobalInvalidSignFails,
       "hpnicfIKEGlobalCertUnavailableFails": hpnicfIKEGlobalCertUnavailableFails,
       "hpnicfIKETrapObject": hpnicfIKETrapObject,
       "hpnicfIKEProposalNumber": hpnicfIKEProposalNumber,
       "hpnicfIKEProposalSize": hpnicfIKEProposalSize,
       "hpnicfIKEIdInformation": hpnicfIKEIdInformation,
       "hpnicfIKEProtocolNum": hpnicfIKEProtocolNum,
       "hpnicfIKECertInformation": hpnicfIKECertInformation,
       "hpnicfIKETrapCntl": hpnicfIKETrapCntl,
       "hpnicfIKETrapGlobalCntl": hpnicfIKETrapGlobalCntl,
       "hpnicfIKETunnelStartTrapCntl": hpnicfIKETunnelStartTrapCntl,
       "hpnicfIKETunnelStopTrapCntl": hpnicfIKETunnelStopTrapCntl,
       "hpnicfIKENoSaTrapCntl": hpnicfIKENoSaTrapCntl,
       "hpnicfIKEEncryFailureTrapCntl": hpnicfIKEEncryFailureTrapCntl,
       "hpnicfIKEDecryFailureTrapCntl": hpnicfIKEDecryFailureTrapCntl,
       "hpnicfIKEInvalidProposalTrapCntl": hpnicfIKEInvalidProposalTrapCntl,
       "hpnicfIKEAuthFailTrapCntl": hpnicfIKEAuthFailTrapCntl,
       "hpnicfIKEInvalidCookieTrapCntl": hpnicfIKEInvalidCookieTrapCntl,
       "hpnicfIKEInvalidSpiTrapCntl": hpnicfIKEInvalidSpiTrapCntl,
       "hpnicfIKEAttrNotSuppTrapCntl": hpnicfIKEAttrNotSuppTrapCntl,
       "hpnicfIKEUnsportExchTypeTrapCntl": hpnicfIKEUnsportExchTypeTrapCntl,
       "hpnicfIKEInvalidIdTrapCntl": hpnicfIKEInvalidIdTrapCntl,
       "hpnicfIKEInvalidProtocolTrapCntl": hpnicfIKEInvalidProtocolTrapCntl,
       "hpnicfIKECertTypeUnsuppTrapCntl": hpnicfIKECertTypeUnsuppTrapCntl,
       "hpnicfIKEInvalidCertAuthTrapCntl": hpnicfIKEInvalidCertAuthTrapCntl,
       "hpnicfIKEInvalidSignTrapCntl": hpnicfIKEInvalidSignTrapCntl,
       "hpnicfIKECertUnavailableTrapCntl": hpnicfIKECertUnavailableTrapCntl,
       "hpnicfIKEProposalAddTrapCntl": hpnicfIKEProposalAddTrapCntl,
       "hpnicfIKEProposalDelTrapCntl": hpnicfIKEProposalDelTrapCntl,
       "hpnicfIKETrap": hpnicfIKETrap,
       "hpnicfIKENotifications": hpnicfIKENotifications,
       "hpnicfIKETunnelStart": hpnicfIKETunnelStart,
       "hpnicfIKETunnelStop": hpnicfIKETunnelStop,
       "hpnicfIKENoSaFailure": hpnicfIKENoSaFailure,
       "hpnicfIKEEncryFailFailure": hpnicfIKEEncryFailFailure,
       "hpnicfIKEDecryFailFailure": hpnicfIKEDecryFailFailure,
       "hpnicfIKEInvalidProposalFailure": hpnicfIKEInvalidProposalFailure,
       "hpnicfIKEAuthFailFailure": hpnicfIKEAuthFailFailure,
       "hpnicfIKEInvalidCookieFailure": hpnicfIKEInvalidCookieFailure,
       "hpnicfIKEAttrNotSuppFailure": hpnicfIKEAttrNotSuppFailure,
       "hpnicfIKEUnsportExchTypeFailure": hpnicfIKEUnsportExchTypeFailure,
       "hpnicfIKEInvalidIdFailure": hpnicfIKEInvalidIdFailure,
       "hpnicfIKEInvalidProtocolFailure": hpnicfIKEInvalidProtocolFailure,
       "hpnicfIKECertTypeUnsuppFailure": hpnicfIKECertTypeUnsuppFailure,
       "hpnicfIKEInvalidCertAuthFailure": hpnicfIKEInvalidCertAuthFailure,
       "hpnicfIKElInvalidSignFailure": hpnicfIKElInvalidSignFailure,
       "hpnicfIKECertUnavailableFailure": hpnicfIKECertUnavailableFailure,
       "hpnicfIKEProposalAdd": hpnicfIKEProposalAdd,
       "hpnicfIKEProposalDel": hpnicfIKEProposalDel,
       "hpnicfIKEScalarObjects": hpnicfIKEScalarObjects,
       "hpnicfIKEMIBVersion": hpnicfIKEMIBVersion,
       "hpnicfIKEConformance": hpnicfIKEConformance,
       "hpnicfIKECompliances": hpnicfIKECompliances,
       "hpnicfIKECompliance": hpnicfIKECompliance,
       "hpnicfIKEGroups": hpnicfIKEGroups,
       "hpnicfIKETunnelTableGroup": hpnicfIKETunnelTableGroup,
       "hpnicfIKETunnelStatTableGroup": hpnicfIKETunnelStatTableGroup,
       "hpnicfIKEGlobalStatsGroup": hpnicfIKEGlobalStatsGroup,
       "hpnicfIKETrapObjectGroup": hpnicfIKETrapObjectGroup,
       "hpnicfIKETrapCntlGroup": hpnicfIKETrapCntlGroup,
       "hpnicfIKETrapGroup": hpnicfIKETrapGroup,
       "hpnicfIKEScalarObjectsGroup": hpnicfIKEScalarObjectsGroup}
)
