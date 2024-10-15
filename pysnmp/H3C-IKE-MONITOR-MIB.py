# SNMP MIB module (H3C-IKE-MONITOR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/H3C-IKE-MONITOR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:50:41 2024
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

(h3cCommon,) = mibBuilder.importSymbols(
    "HUAWEI-3COM-OID-MIB",
    "h3cCommon")

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

h3cIKEMonitor = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class H3cIKENegoMode(Integer32, TextualConvention):
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



class H3cIKEAuthMethod(Integer32, TextualConvention):
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



class H3cDiffHellmanGrp(Integer32, TextualConvention):
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



class H3cEncryptAlgo(Integer32, TextualConvention):
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



class H3cAuthAlgo(Integer32, TextualConvention):
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



class H3cSaProtocol(Integer32, TextualConvention):
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



class H3cTrapStatus(Integer32, TextualConvention):
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



class H3cIKEIDType(Integer32, TextualConvention):
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



class H3cTrafficType(Integer32, TextualConvention):
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



class H3cIKETunnelState(Integer32, TextualConvention):
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

_H3cIKEObjects_ObjectIdentity = ObjectIdentity
h3cIKEObjects = _H3cIKEObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 1)
)
_H3cIKETunnelTable_Object = MibTable
h3cIKETunnelTable = _H3cIKETunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 1, 1)
)
if mibBuilder.loadTexts:
    h3cIKETunnelTable.setStatus("current")
_H3cIKETunnelEntry_Object = MibTableRow
h3cIKETunnelEntry = _H3cIKETunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 1, 1, 1)
)
h3cIKETunnelEntry.setIndexNames(
    (0, "H3C-IKE-MONITOR-MIB", "h3cIKETunIndex"),
)
if mibBuilder.loadTexts:
    h3cIKETunnelEntry.setStatus("current")


class _H3cIKETunIndex_Type(Integer32):
    """Custom type h3cIKETunIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_H3cIKETunIndex_Type.__name__ = "Integer32"
_H3cIKETunIndex_Object = MibTableColumn
h3cIKETunIndex = _H3cIKETunIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 1, 1, 1, 1),
    _H3cIKETunIndex_Type()
)
h3cIKETunIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cIKETunIndex.setStatus("current")
_H3cIKETunLocalType_Type = H3cIKEIDType
_H3cIKETunLocalType_Object = MibTableColumn
h3cIKETunLocalType = _H3cIKETunLocalType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 1, 1, 1, 2),
    _H3cIKETunLocalType_Type()
)
h3cIKETunLocalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIKETunLocalType.setStatus("current")
_H3cIKETunLocalValue1_Type = DisplayString
_H3cIKETunLocalValue1_Object = MibTableColumn
h3cIKETunLocalValue1 = _H3cIKETunLocalValue1_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 1, 1, 1, 3),
    _H3cIKETunLocalValue1_Type()
)
h3cIKETunLocalValue1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIKETunLocalValue1.setStatus("current")
_H3cIKETunLocalValue2_Type = DisplayString
_H3cIKETunLocalValue2_Object = MibTableColumn
h3cIKETunLocalValue2 = _H3cIKETunLocalValue2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 1, 1, 1, 4),
    _H3cIKETunLocalValue2_Type()
)
h3cIKETunLocalValue2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIKETunLocalValue2.setStatus("current")
_H3cIKETunLocalAddr_Type = IpAddress
_H3cIKETunLocalAddr_Object = MibTableColumn
h3cIKETunLocalAddr = _H3cIKETunLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 1, 1, 1, 5),
    _H3cIKETunLocalAddr_Type()
)
h3cIKETunLocalAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIKETunLocalAddr.setStatus("current")
_H3cIKETunRemoteType_Type = H3cIKEIDType
_H3cIKETunRemoteType_Object = MibTableColumn
h3cIKETunRemoteType = _H3cIKETunRemoteType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 1, 1, 1, 6),
    _H3cIKETunRemoteType_Type()
)
h3cIKETunRemoteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIKETunRemoteType.setStatus("current")
_H3cIKETunRemoteValue1_Type = DisplayString
_H3cIKETunRemoteValue1_Object = MibTableColumn
h3cIKETunRemoteValue1 = _H3cIKETunRemoteValue1_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 1, 1, 1, 7),
    _H3cIKETunRemoteValue1_Type()
)
h3cIKETunRemoteValue1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIKETunRemoteValue1.setStatus("current")
_H3cIKETunRemoteValue2_Type = DisplayString
_H3cIKETunRemoteValue2_Object = MibTableColumn
h3cIKETunRemoteValue2 = _H3cIKETunRemoteValue2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 1, 1, 1, 8),
    _H3cIKETunRemoteValue2_Type()
)
h3cIKETunRemoteValue2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIKETunRemoteValue2.setStatus("current")
_H3cIKETunRemoteAddr_Type = IpAddress
_H3cIKETunRemoteAddr_Object = MibTableColumn
h3cIKETunRemoteAddr = _H3cIKETunRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 1, 1, 1, 9),
    _H3cIKETunRemoteAddr_Type()
)
h3cIKETunRemoteAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIKETunRemoteAddr.setStatus("current")


class _H3cIKETunInitiator_Type(Integer32):
    """Custom type h3cIKETunInitiator based on Integer32"""
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


_H3cIKETunInitiator_Type.__name__ = "Integer32"
_H3cIKETunInitiator_Object = MibTableColumn
h3cIKETunInitiator = _H3cIKETunInitiator_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 1, 1, 1, 10),
    _H3cIKETunInitiator_Type()
)
h3cIKETunInitiator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIKETunInitiator.setStatus("current")
_H3cIKETunNegoMode_Type = H3cIKENegoMode
_H3cIKETunNegoMode_Object = MibTableColumn
h3cIKETunNegoMode = _H3cIKETunNegoMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 1, 1, 1, 11),
    _H3cIKETunNegoMode_Type()
)
h3cIKETunNegoMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIKETunNegoMode.setStatus("current")
_H3cIKETunDiffHellmanGrp_Type = H3cDiffHellmanGrp
_H3cIKETunDiffHellmanGrp_Object = MibTableColumn
h3cIKETunDiffHellmanGrp = _H3cIKETunDiffHellmanGrp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 1, 1, 1, 12),
    _H3cIKETunDiffHellmanGrp_Type()
)
h3cIKETunDiffHellmanGrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIKETunDiffHellmanGrp.setStatus("current")
_H3cIKETunEncryptAlgo_Type = H3cEncryptAlgo
_H3cIKETunEncryptAlgo_Object = MibTableColumn
h3cIKETunEncryptAlgo = _H3cIKETunEncryptAlgo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 1, 1, 1, 13),
    _H3cIKETunEncryptAlgo_Type()
)
h3cIKETunEncryptAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIKETunEncryptAlgo.setStatus("current")
_H3cIKETunHashAlgo_Type = H3cAuthAlgo
_H3cIKETunHashAlgo_Object = MibTableColumn
h3cIKETunHashAlgo = _H3cIKETunHashAlgo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 1, 1, 1, 14),
    _H3cIKETunHashAlgo_Type()
)
h3cIKETunHashAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIKETunHashAlgo.setStatus("current")
_H3cIKETunAuthMethod_Type = H3cIKEAuthMethod
_H3cIKETunAuthMethod_Object = MibTableColumn
h3cIKETunAuthMethod = _H3cIKETunAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 1, 1, 1, 15),
    _H3cIKETunAuthMethod_Type()
)
h3cIKETunAuthMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIKETunAuthMethod.setStatus("current")


class _H3cIKETunLifeTime_Type(Integer32):
    """Custom type h3cIKETunLifeTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_H3cIKETunLifeTime_Type.__name__ = "Integer32"
_H3cIKETunLifeTime_Object = MibTableColumn
h3cIKETunLifeTime = _H3cIKETunLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 1, 1, 1, 16),
    _H3cIKETunLifeTime_Type()
)
h3cIKETunLifeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIKETunLifeTime.setStatus("current")


class _H3cIKETunActiveTime_Type(Integer32):
    """Custom type h3cIKETunActiveTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_H3cIKETunActiveTime_Type.__name__ = "Integer32"
_H3cIKETunActiveTime_Object = MibTableColumn
h3cIKETunActiveTime = _H3cIKETunActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 1, 1, 1, 17),
    _H3cIKETunActiveTime_Type()
)
h3cIKETunActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIKETunActiveTime.setStatus("current")


class _H3cIKETunRemainTime_Type(Integer32):
    """Custom type h3cIKETunRemainTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_H3cIKETunRemainTime_Type.__name__ = "Integer32"
_H3cIKETunRemainTime_Object = MibTableColumn
h3cIKETunRemainTime = _H3cIKETunRemainTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 1, 1, 1, 18),
    _H3cIKETunRemainTime_Type()
)
h3cIKETunRemainTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIKETunRemainTime.setStatus("current")
_H3cIKETunTotalRefreshes_Type = Counter32
_H3cIKETunTotalRefreshes_Object = MibTableColumn
h3cIKETunTotalRefreshes = _H3cIKETunTotalRefreshes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 1, 1, 1, 19),
    _H3cIKETunTotalRefreshes_Type()
)
h3cIKETunTotalRefreshes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIKETunTotalRefreshes.setStatus("current")
_H3cIKETunState_Type = H3cIKETunnelState
_H3cIKETunState_Object = MibTableColumn
h3cIKETunState = _H3cIKETunState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 1, 1, 1, 20),
    _H3cIKETunState_Type()
)
h3cIKETunState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIKETunState.setStatus("current")


class _H3cIKETunDpdIntervalTime_Type(Integer32):
    """Custom type h3cIKETunDpdIntervalTime based on Integer32"""
    defaultValue = 10


_H3cIKETunDpdIntervalTime_Object = MibTableColumn
h3cIKETunDpdIntervalTime = _H3cIKETunDpdIntervalTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 1, 1, 1, 21),
    _H3cIKETunDpdIntervalTime_Type()
)
h3cIKETunDpdIntervalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIKETunDpdIntervalTime.setStatus("current")
if mibBuilder.loadTexts:
    h3cIKETunDpdIntervalTime.setUnits("second")


class _H3cIKETunDpdTimeOut_Type(Integer32):
    """Custom type h3cIKETunDpdTimeOut based on Integer32"""
    defaultValue = 5


_H3cIKETunDpdTimeOut_Object = MibTableColumn
h3cIKETunDpdTimeOut = _H3cIKETunDpdTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 1, 1, 1, 22),
    _H3cIKETunDpdTimeOut_Type()
)
h3cIKETunDpdTimeOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIKETunDpdTimeOut.setStatus("current")
if mibBuilder.loadTexts:
    h3cIKETunDpdTimeOut.setUnits("second")
_H3cIKETunnelStatTable_Object = MibTable
h3cIKETunnelStatTable = _H3cIKETunnelStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 1, 2)
)
if mibBuilder.loadTexts:
    h3cIKETunnelStatTable.setStatus("current")
_H3cIKETunnelStatEntry_Object = MibTableRow
h3cIKETunnelStatEntry = _H3cIKETunnelStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 1, 2, 1)
)
h3cIKETunnelStatEntry.setIndexNames(
    (0, "H3C-IKE-MONITOR-MIB", "h3cIKETunIndex"),
)
if mibBuilder.loadTexts:
    h3cIKETunnelStatEntry.setStatus("current")
_H3cIKETunInOctets_Type = Counter64
_H3cIKETunInOctets_Object = MibTableColumn
h3cIKETunInOctets = _H3cIKETunInOctets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 1, 2, 1, 1),
    _H3cIKETunInOctets_Type()
)
h3cIKETunInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIKETunInOctets.setStatus("current")
_H3cIKETunInPkts_Type = Counter64
_H3cIKETunInPkts_Object = MibTableColumn
h3cIKETunInPkts = _H3cIKETunInPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 1, 2, 1, 2),
    _H3cIKETunInPkts_Type()
)
h3cIKETunInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIKETunInPkts.setStatus("current")
_H3cIKETunInDropPkts_Type = Counter64
_H3cIKETunInDropPkts_Object = MibTableColumn
h3cIKETunInDropPkts = _H3cIKETunInDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 1, 2, 1, 3),
    _H3cIKETunInDropPkts_Type()
)
h3cIKETunInDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIKETunInDropPkts.setStatus("current")
_H3cIKETunInP2Exchgs_Type = Counter64
_H3cIKETunInP2Exchgs_Object = MibTableColumn
h3cIKETunInP2Exchgs = _H3cIKETunInP2Exchgs_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 1, 2, 1, 4),
    _H3cIKETunInP2Exchgs_Type()
)
h3cIKETunInP2Exchgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIKETunInP2Exchgs.setStatus("current")
_H3cIKETunInP2ExchgRejets_Type = Counter64
_H3cIKETunInP2ExchgRejets_Object = MibTableColumn
h3cIKETunInP2ExchgRejets = _H3cIKETunInP2ExchgRejets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 1, 2, 1, 5),
    _H3cIKETunInP2ExchgRejets_Type()
)
h3cIKETunInP2ExchgRejets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIKETunInP2ExchgRejets.setStatus("current")
_H3cIKETunInP2SaDelRequests_Type = Counter64
_H3cIKETunInP2SaDelRequests_Object = MibTableColumn
h3cIKETunInP2SaDelRequests = _H3cIKETunInP2SaDelRequests_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 1, 2, 1, 6),
    _H3cIKETunInP2SaDelRequests_Type()
)
h3cIKETunInP2SaDelRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIKETunInP2SaDelRequests.setStatus("current")
_H3cIKETunInP1SaDelRequests_Type = Counter64
_H3cIKETunInP1SaDelRequests_Object = MibTableColumn
h3cIKETunInP1SaDelRequests = _H3cIKETunInP1SaDelRequests_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 1, 2, 1, 7),
    _H3cIKETunInP1SaDelRequests_Type()
)
h3cIKETunInP1SaDelRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIKETunInP1SaDelRequests.setStatus("current")
_H3cIKETunInNotifys_Type = Counter32
_H3cIKETunInNotifys_Object = MibTableColumn
h3cIKETunInNotifys = _H3cIKETunInNotifys_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 1, 2, 1, 8),
    _H3cIKETunInNotifys_Type()
)
h3cIKETunInNotifys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIKETunInNotifys.setStatus("current")
_H3cIKETunOutOctets_Type = Counter64
_H3cIKETunOutOctets_Object = MibTableColumn
h3cIKETunOutOctets = _H3cIKETunOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 1, 2, 1, 9),
    _H3cIKETunOutOctets_Type()
)
h3cIKETunOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIKETunOutOctets.setStatus("current")
_H3cIKETunOutPkts_Type = Counter64
_H3cIKETunOutPkts_Object = MibTableColumn
h3cIKETunOutPkts = _H3cIKETunOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 1, 2, 1, 10),
    _H3cIKETunOutPkts_Type()
)
h3cIKETunOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIKETunOutPkts.setStatus("current")
_H3cIKETunOutDropPkts_Type = Counter64
_H3cIKETunOutDropPkts_Object = MibTableColumn
h3cIKETunOutDropPkts = _H3cIKETunOutDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 1, 2, 1, 11),
    _H3cIKETunOutDropPkts_Type()
)
h3cIKETunOutDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIKETunOutDropPkts.setStatus("current")
_H3cIKETunOutP2Exchgs_Type = Counter64
_H3cIKETunOutP2Exchgs_Object = MibTableColumn
h3cIKETunOutP2Exchgs = _H3cIKETunOutP2Exchgs_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 1, 2, 1, 12),
    _H3cIKETunOutP2Exchgs_Type()
)
h3cIKETunOutP2Exchgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIKETunOutP2Exchgs.setStatus("current")
_H3cIKETunOutP2ExchgRejects_Type = Counter64
_H3cIKETunOutP2ExchgRejects_Object = MibTableColumn
h3cIKETunOutP2ExchgRejects = _H3cIKETunOutP2ExchgRejects_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 1, 2, 1, 13),
    _H3cIKETunOutP2ExchgRejects_Type()
)
h3cIKETunOutP2ExchgRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIKETunOutP2ExchgRejects.setStatus("current")
_H3cIKETunOutP2SaDelRequests_Type = Counter64
_H3cIKETunOutP2SaDelRequests_Object = MibTableColumn
h3cIKETunOutP2SaDelRequests = _H3cIKETunOutP2SaDelRequests_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 1, 2, 1, 14),
    _H3cIKETunOutP2SaDelRequests_Type()
)
h3cIKETunOutP2SaDelRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIKETunOutP2SaDelRequests.setStatus("current")
_H3cIKETunOutP1SaDelRequests_Type = Counter64
_H3cIKETunOutP1SaDelRequests_Object = MibTableColumn
h3cIKETunOutP1SaDelRequests = _H3cIKETunOutP1SaDelRequests_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 1, 2, 1, 15),
    _H3cIKETunOutP1SaDelRequests_Type()
)
h3cIKETunOutP1SaDelRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIKETunOutP1SaDelRequests.setStatus("current")
_H3cIKETunOutNotifys_Type = Counter32
_H3cIKETunOutNotifys_Object = MibTableColumn
h3cIKETunOutNotifys = _H3cIKETunOutNotifys_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 1, 2, 1, 16),
    _H3cIKETunOutNotifys_Type()
)
h3cIKETunOutNotifys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIKETunOutNotifys.setStatus("current")
_H3cIKEGlobalStats_ObjectIdentity = ObjectIdentity
h3cIKEGlobalStats = _H3cIKEGlobalStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 1, 3)
)
_H3cIKEGlobalActiveTunnels_Type = Gauge32
_H3cIKEGlobalActiveTunnels_Object = MibScalar
h3cIKEGlobalActiveTunnels = _H3cIKEGlobalActiveTunnels_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 1, 3, 1),
    _H3cIKEGlobalActiveTunnels_Type()
)
h3cIKEGlobalActiveTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIKEGlobalActiveTunnels.setStatus("current")
_H3cIKEGlobalInOctets_Type = Counter64
_H3cIKEGlobalInOctets_Object = MibScalar
h3cIKEGlobalInOctets = _H3cIKEGlobalInOctets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 1, 3, 2),
    _H3cIKEGlobalInOctets_Type()
)
h3cIKEGlobalInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIKEGlobalInOctets.setStatus("current")
_H3cIKEGlobalInPkts_Type = Counter64
_H3cIKEGlobalInPkts_Object = MibScalar
h3cIKEGlobalInPkts = _H3cIKEGlobalInPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 1, 3, 3),
    _H3cIKEGlobalInPkts_Type()
)
h3cIKEGlobalInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIKEGlobalInPkts.setStatus("current")
_H3cIKEGlobalInDropPkts_Type = Counter64
_H3cIKEGlobalInDropPkts_Object = MibScalar
h3cIKEGlobalInDropPkts = _H3cIKEGlobalInDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 1, 3, 4),
    _H3cIKEGlobalInDropPkts_Type()
)
h3cIKEGlobalInDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIKEGlobalInDropPkts.setStatus("current")
_H3cIKEGlobalInP2Exchgs_Type = Counter64
_H3cIKEGlobalInP2Exchgs_Object = MibScalar
h3cIKEGlobalInP2Exchgs = _H3cIKEGlobalInP2Exchgs_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 1, 3, 5),
    _H3cIKEGlobalInP2Exchgs_Type()
)
h3cIKEGlobalInP2Exchgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIKEGlobalInP2Exchgs.setStatus("current")
_H3cIKEGlobalInP2ExchgRejects_Type = Counter64
_H3cIKEGlobalInP2ExchgRejects_Object = MibScalar
h3cIKEGlobalInP2ExchgRejects = _H3cIKEGlobalInP2ExchgRejects_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 1, 3, 6),
    _H3cIKEGlobalInP2ExchgRejects_Type()
)
h3cIKEGlobalInP2ExchgRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIKEGlobalInP2ExchgRejects.setStatus("current")
_H3cIKEGlobalInP2SaDelRequests_Type = Counter64
_H3cIKEGlobalInP2SaDelRequests_Object = MibScalar
h3cIKEGlobalInP2SaDelRequests = _H3cIKEGlobalInP2SaDelRequests_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 1, 3, 7),
    _H3cIKEGlobalInP2SaDelRequests_Type()
)
h3cIKEGlobalInP2SaDelRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIKEGlobalInP2SaDelRequests.setStatus("current")
_H3cIKEGlobalInNotifys_Type = Counter32
_H3cIKEGlobalInNotifys_Object = MibScalar
h3cIKEGlobalInNotifys = _H3cIKEGlobalInNotifys_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 1, 3, 8),
    _H3cIKEGlobalInNotifys_Type()
)
h3cIKEGlobalInNotifys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIKEGlobalInNotifys.setStatus("current")
_H3cIKEGlobalOutOctets_Type = Counter64
_H3cIKEGlobalOutOctets_Object = MibScalar
h3cIKEGlobalOutOctets = _H3cIKEGlobalOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 1, 3, 9),
    _H3cIKEGlobalOutOctets_Type()
)
h3cIKEGlobalOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIKEGlobalOutOctets.setStatus("current")
_H3cIKEGlobalOutPkts_Type = Counter64
_H3cIKEGlobalOutPkts_Object = MibScalar
h3cIKEGlobalOutPkts = _H3cIKEGlobalOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 1, 3, 10),
    _H3cIKEGlobalOutPkts_Type()
)
h3cIKEGlobalOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIKEGlobalOutPkts.setStatus("current")
_H3cIKEGlobalOutDropPkts_Type = Counter64
_H3cIKEGlobalOutDropPkts_Object = MibScalar
h3cIKEGlobalOutDropPkts = _H3cIKEGlobalOutDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 1, 3, 11),
    _H3cIKEGlobalOutDropPkts_Type()
)
h3cIKEGlobalOutDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIKEGlobalOutDropPkts.setStatus("current")
_H3cIKEGlobalOutP2Exchgs_Type = Counter64
_H3cIKEGlobalOutP2Exchgs_Object = MibScalar
h3cIKEGlobalOutP2Exchgs = _H3cIKEGlobalOutP2Exchgs_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 1, 3, 12),
    _H3cIKEGlobalOutP2Exchgs_Type()
)
h3cIKEGlobalOutP2Exchgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIKEGlobalOutP2Exchgs.setStatus("current")
_H3cIKEGlobalOutP2ExchgRejects_Type = Counter64
_H3cIKEGlobalOutP2ExchgRejects_Object = MibScalar
h3cIKEGlobalOutP2ExchgRejects = _H3cIKEGlobalOutP2ExchgRejects_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 1, 3, 13),
    _H3cIKEGlobalOutP2ExchgRejects_Type()
)
h3cIKEGlobalOutP2ExchgRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIKEGlobalOutP2ExchgRejects.setStatus("current")
_H3cIKEGlobalOutP2SaDelRequests_Type = Counter64
_H3cIKEGlobalOutP2SaDelRequests_Object = MibScalar
h3cIKEGlobalOutP2SaDelRequests = _H3cIKEGlobalOutP2SaDelRequests_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 1, 3, 14),
    _H3cIKEGlobalOutP2SaDelRequests_Type()
)
h3cIKEGlobalOutP2SaDelRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIKEGlobalOutP2SaDelRequests.setStatus("current")
_H3cIKEGlobalOutNotifys_Type = Counter32
_H3cIKEGlobalOutNotifys_Object = MibScalar
h3cIKEGlobalOutNotifys = _H3cIKEGlobalOutNotifys_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 1, 3, 15),
    _H3cIKEGlobalOutNotifys_Type()
)
h3cIKEGlobalOutNotifys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIKEGlobalOutNotifys.setStatus("current")
_H3cIKEGlobalInitTunnels_Type = Counter32
_H3cIKEGlobalInitTunnels_Object = MibScalar
h3cIKEGlobalInitTunnels = _H3cIKEGlobalInitTunnels_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 1, 3, 16),
    _H3cIKEGlobalInitTunnels_Type()
)
h3cIKEGlobalInitTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIKEGlobalInitTunnels.setStatus("current")
_H3cIKEGlobalInitTunnelFails_Type = Counter32
_H3cIKEGlobalInitTunnelFails_Object = MibScalar
h3cIKEGlobalInitTunnelFails = _H3cIKEGlobalInitTunnelFails_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 1, 3, 17),
    _H3cIKEGlobalInitTunnelFails_Type()
)
h3cIKEGlobalInitTunnelFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIKEGlobalInitTunnelFails.setStatus("current")
_H3cIKEGlobalRespTunnels_Type = Counter32
_H3cIKEGlobalRespTunnels_Object = MibScalar
h3cIKEGlobalRespTunnels = _H3cIKEGlobalRespTunnels_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 1, 3, 18),
    _H3cIKEGlobalRespTunnels_Type()
)
h3cIKEGlobalRespTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIKEGlobalRespTunnels.setStatus("current")
_H3cIKEGlobalRespTunnelFails_Type = Counter32
_H3cIKEGlobalRespTunnelFails_Object = MibScalar
h3cIKEGlobalRespTunnelFails = _H3cIKEGlobalRespTunnelFails_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 1, 3, 19),
    _H3cIKEGlobalRespTunnelFails_Type()
)
h3cIKEGlobalRespTunnelFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIKEGlobalRespTunnelFails.setStatus("current")
_H3cIKEGlobalAuthFails_Type = Counter32
_H3cIKEGlobalAuthFails_Object = MibScalar
h3cIKEGlobalAuthFails = _H3cIKEGlobalAuthFails_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 1, 3, 20),
    _H3cIKEGlobalAuthFails_Type()
)
h3cIKEGlobalAuthFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIKEGlobalAuthFails.setStatus("current")
_H3cIKEGlobalNoSaFails_Type = Counter32
_H3cIKEGlobalNoSaFails_Object = MibScalar
h3cIKEGlobalNoSaFails = _H3cIKEGlobalNoSaFails_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 1, 3, 21),
    _H3cIKEGlobalNoSaFails_Type()
)
h3cIKEGlobalNoSaFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIKEGlobalNoSaFails.setStatus("current")
_H3cIKEGlobalInvalidCookieFails_Type = Counter32
_H3cIKEGlobalInvalidCookieFails_Object = MibScalar
h3cIKEGlobalInvalidCookieFails = _H3cIKEGlobalInvalidCookieFails_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 1, 3, 22),
    _H3cIKEGlobalInvalidCookieFails_Type()
)
h3cIKEGlobalInvalidCookieFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIKEGlobalInvalidCookieFails.setStatus("current")
_H3cIKEGlobalAttrNotSuppFails_Type = Counter32
_H3cIKEGlobalAttrNotSuppFails_Object = MibScalar
h3cIKEGlobalAttrNotSuppFails = _H3cIKEGlobalAttrNotSuppFails_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 1, 3, 23),
    _H3cIKEGlobalAttrNotSuppFails_Type()
)
h3cIKEGlobalAttrNotSuppFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIKEGlobalAttrNotSuppFails.setStatus("current")
_H3cIKEGlobalNoProposalChosenFails_Type = Counter32
_H3cIKEGlobalNoProposalChosenFails_Object = MibScalar
h3cIKEGlobalNoProposalChosenFails = _H3cIKEGlobalNoProposalChosenFails_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 1, 3, 24),
    _H3cIKEGlobalNoProposalChosenFails_Type()
)
h3cIKEGlobalNoProposalChosenFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIKEGlobalNoProposalChosenFails.setStatus("current")
_H3cIKEGlobalUnsportExchTypeFails_Type = Counter32
_H3cIKEGlobalUnsportExchTypeFails_Object = MibScalar
h3cIKEGlobalUnsportExchTypeFails = _H3cIKEGlobalUnsportExchTypeFails_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 1, 3, 25),
    _H3cIKEGlobalUnsportExchTypeFails_Type()
)
h3cIKEGlobalUnsportExchTypeFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIKEGlobalUnsportExchTypeFails.setStatus("current")
_H3cIKEGlobalInvalidIdFails_Type = Counter32
_H3cIKEGlobalInvalidIdFails_Object = MibScalar
h3cIKEGlobalInvalidIdFails = _H3cIKEGlobalInvalidIdFails_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 1, 3, 26),
    _H3cIKEGlobalInvalidIdFails_Type()
)
h3cIKEGlobalInvalidIdFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIKEGlobalInvalidIdFails.setStatus("current")
_H3cIKEGlobalInvalidProFails_Type = Counter32
_H3cIKEGlobalInvalidProFails_Object = MibScalar
h3cIKEGlobalInvalidProFails = _H3cIKEGlobalInvalidProFails_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 1, 3, 27),
    _H3cIKEGlobalInvalidProFails_Type()
)
h3cIKEGlobalInvalidProFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIKEGlobalInvalidProFails.setStatus("current")
_H3cIKEGlobalCertTypeUnsuppFails_Type = Counter32
_H3cIKEGlobalCertTypeUnsuppFails_Object = MibScalar
h3cIKEGlobalCertTypeUnsuppFails = _H3cIKEGlobalCertTypeUnsuppFails_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 1, 3, 28),
    _H3cIKEGlobalCertTypeUnsuppFails_Type()
)
h3cIKEGlobalCertTypeUnsuppFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIKEGlobalCertTypeUnsuppFails.setStatus("current")
_H3cIKEGlobalInvalidCertAuthFails_Type = Counter32
_H3cIKEGlobalInvalidCertAuthFails_Object = MibScalar
h3cIKEGlobalInvalidCertAuthFails = _H3cIKEGlobalInvalidCertAuthFails_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 1, 3, 29),
    _H3cIKEGlobalInvalidCertAuthFails_Type()
)
h3cIKEGlobalInvalidCertAuthFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIKEGlobalInvalidCertAuthFails.setStatus("current")
_H3cIKEGlobalInvalidSignFails_Type = Counter32
_H3cIKEGlobalInvalidSignFails_Object = MibScalar
h3cIKEGlobalInvalidSignFails = _H3cIKEGlobalInvalidSignFails_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 1, 3, 30),
    _H3cIKEGlobalInvalidSignFails_Type()
)
h3cIKEGlobalInvalidSignFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIKEGlobalInvalidSignFails.setStatus("current")
_H3cIKEGlobalCertUnavailableFails_Type = Counter32
_H3cIKEGlobalCertUnavailableFails_Object = MibScalar
h3cIKEGlobalCertUnavailableFails = _H3cIKEGlobalCertUnavailableFails_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 1, 3, 31),
    _H3cIKEGlobalCertUnavailableFails_Type()
)
h3cIKEGlobalCertUnavailableFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIKEGlobalCertUnavailableFails.setStatus("current")
_H3cIKETrapObject_ObjectIdentity = ObjectIdentity
h3cIKETrapObject = _H3cIKETrapObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 1, 4)
)
_H3cIKEProposalNumber_Type = Integer32
_H3cIKEProposalNumber_Object = MibScalar
h3cIKEProposalNumber = _H3cIKEProposalNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 1, 4, 1),
    _H3cIKEProposalNumber_Type()
)
h3cIKEProposalNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cIKEProposalNumber.setStatus("current")
_H3cIKEProposalSize_Type = Integer32
_H3cIKEProposalSize_Object = MibScalar
h3cIKEProposalSize = _H3cIKEProposalSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 1, 4, 2),
    _H3cIKEProposalSize_Type()
)
h3cIKEProposalSize.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cIKEProposalSize.setStatus("current")
_H3cIKEIdInformation_Type = DisplayString
_H3cIKEIdInformation_Object = MibScalar
h3cIKEIdInformation = _H3cIKEIdInformation_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 1, 4, 3),
    _H3cIKEIdInformation_Type()
)
h3cIKEIdInformation.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cIKEIdInformation.setStatus("current")
_H3cIKEProtocolNum_Type = Integer32
_H3cIKEProtocolNum_Object = MibScalar
h3cIKEProtocolNum = _H3cIKEProtocolNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 1, 4, 4),
    _H3cIKEProtocolNum_Type()
)
h3cIKEProtocolNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cIKEProtocolNum.setStatus("current")
_H3cIKECertInformation_Type = DisplayString
_H3cIKECertInformation_Object = MibScalar
h3cIKECertInformation = _H3cIKECertInformation_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 1, 4, 5),
    _H3cIKECertInformation_Type()
)
h3cIKECertInformation.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cIKECertInformation.setStatus("current")
_H3cIKETrapCntl_ObjectIdentity = ObjectIdentity
h3cIKETrapCntl = _H3cIKETrapCntl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 1, 5)
)
_H3cIKETrapGlobalCntl_Type = H3cTrapStatus
_H3cIKETrapGlobalCntl_Object = MibScalar
h3cIKETrapGlobalCntl = _H3cIKETrapGlobalCntl_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 1, 5, 1),
    _H3cIKETrapGlobalCntl_Type()
)
h3cIKETrapGlobalCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIKETrapGlobalCntl.setStatus("current")
_H3cIKETunnelStartTrapCntl_Type = H3cTrapStatus
_H3cIKETunnelStartTrapCntl_Object = MibScalar
h3cIKETunnelStartTrapCntl = _H3cIKETunnelStartTrapCntl_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 1, 5, 2),
    _H3cIKETunnelStartTrapCntl_Type()
)
h3cIKETunnelStartTrapCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIKETunnelStartTrapCntl.setStatus("current")
_H3cIKETunnelStopTrapCntl_Type = H3cTrapStatus
_H3cIKETunnelStopTrapCntl_Object = MibScalar
h3cIKETunnelStopTrapCntl = _H3cIKETunnelStopTrapCntl_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 1, 5, 3),
    _H3cIKETunnelStopTrapCntl_Type()
)
h3cIKETunnelStopTrapCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIKETunnelStopTrapCntl.setStatus("current")
_H3cIKENoSaTrapCntl_Type = H3cTrapStatus
_H3cIKENoSaTrapCntl_Object = MibScalar
h3cIKENoSaTrapCntl = _H3cIKENoSaTrapCntl_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 1, 5, 4),
    _H3cIKENoSaTrapCntl_Type()
)
h3cIKENoSaTrapCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIKENoSaTrapCntl.setStatus("current")
_H3cIKEEncryFailureTrapCntl_Type = H3cTrapStatus
_H3cIKEEncryFailureTrapCntl_Object = MibScalar
h3cIKEEncryFailureTrapCntl = _H3cIKEEncryFailureTrapCntl_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 1, 5, 5),
    _H3cIKEEncryFailureTrapCntl_Type()
)
h3cIKEEncryFailureTrapCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIKEEncryFailureTrapCntl.setStatus("current")
_H3cIKEDecryFailureTrapCntl_Type = H3cTrapStatus
_H3cIKEDecryFailureTrapCntl_Object = MibScalar
h3cIKEDecryFailureTrapCntl = _H3cIKEDecryFailureTrapCntl_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 1, 5, 6),
    _H3cIKEDecryFailureTrapCntl_Type()
)
h3cIKEDecryFailureTrapCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIKEDecryFailureTrapCntl.setStatus("current")
_H3cIKEInvalidProposalTrapCntl_Type = H3cTrapStatus
_H3cIKEInvalidProposalTrapCntl_Object = MibScalar
h3cIKEInvalidProposalTrapCntl = _H3cIKEInvalidProposalTrapCntl_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 1, 5, 7),
    _H3cIKEInvalidProposalTrapCntl_Type()
)
h3cIKEInvalidProposalTrapCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIKEInvalidProposalTrapCntl.setStatus("current")
_H3cIKEAuthFailTrapCntl_Type = H3cTrapStatus
_H3cIKEAuthFailTrapCntl_Object = MibScalar
h3cIKEAuthFailTrapCntl = _H3cIKEAuthFailTrapCntl_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 1, 5, 8),
    _H3cIKEAuthFailTrapCntl_Type()
)
h3cIKEAuthFailTrapCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIKEAuthFailTrapCntl.setStatus("current")
_H3cIKEInvalidCookieTrapCntl_Type = H3cTrapStatus
_H3cIKEInvalidCookieTrapCntl_Object = MibScalar
h3cIKEInvalidCookieTrapCntl = _H3cIKEInvalidCookieTrapCntl_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 1, 5, 9),
    _H3cIKEInvalidCookieTrapCntl_Type()
)
h3cIKEInvalidCookieTrapCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIKEInvalidCookieTrapCntl.setStatus("current")
_H3cIKEInvalidSpiTrapCntl_Type = H3cTrapStatus
_H3cIKEInvalidSpiTrapCntl_Object = MibScalar
h3cIKEInvalidSpiTrapCntl = _H3cIKEInvalidSpiTrapCntl_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 1, 5, 10),
    _H3cIKEInvalidSpiTrapCntl_Type()
)
h3cIKEInvalidSpiTrapCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIKEInvalidSpiTrapCntl.setStatus("current")
_H3cIKEAttrNotSuppTrapCntl_Type = H3cTrapStatus
_H3cIKEAttrNotSuppTrapCntl_Object = MibScalar
h3cIKEAttrNotSuppTrapCntl = _H3cIKEAttrNotSuppTrapCntl_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 1, 5, 11),
    _H3cIKEAttrNotSuppTrapCntl_Type()
)
h3cIKEAttrNotSuppTrapCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIKEAttrNotSuppTrapCntl.setStatus("current")
_H3cIKEUnsportExchTypeTrapCntl_Type = H3cTrapStatus
_H3cIKEUnsportExchTypeTrapCntl_Object = MibScalar
h3cIKEUnsportExchTypeTrapCntl = _H3cIKEUnsportExchTypeTrapCntl_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 1, 5, 12),
    _H3cIKEUnsportExchTypeTrapCntl_Type()
)
h3cIKEUnsportExchTypeTrapCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIKEUnsportExchTypeTrapCntl.setStatus("current")
_H3cIKEInvalidIdTrapCntl_Type = H3cTrapStatus
_H3cIKEInvalidIdTrapCntl_Object = MibScalar
h3cIKEInvalidIdTrapCntl = _H3cIKEInvalidIdTrapCntl_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 1, 5, 13),
    _H3cIKEInvalidIdTrapCntl_Type()
)
h3cIKEInvalidIdTrapCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIKEInvalidIdTrapCntl.setStatus("current")
_H3cIKEInvalidProtocolTrapCntl_Type = H3cTrapStatus
_H3cIKEInvalidProtocolTrapCntl_Object = MibScalar
h3cIKEInvalidProtocolTrapCntl = _H3cIKEInvalidProtocolTrapCntl_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 1, 5, 14),
    _H3cIKEInvalidProtocolTrapCntl_Type()
)
h3cIKEInvalidProtocolTrapCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIKEInvalidProtocolTrapCntl.setStatus("current")
_H3cIKECertTypeUnsuppTrapCntl_Type = H3cTrapStatus
_H3cIKECertTypeUnsuppTrapCntl_Object = MibScalar
h3cIKECertTypeUnsuppTrapCntl = _H3cIKECertTypeUnsuppTrapCntl_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 1, 5, 15),
    _H3cIKECertTypeUnsuppTrapCntl_Type()
)
h3cIKECertTypeUnsuppTrapCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIKECertTypeUnsuppTrapCntl.setStatus("current")
_H3cIKEInvalidCertAuthTrapCntl_Type = H3cTrapStatus
_H3cIKEInvalidCertAuthTrapCntl_Object = MibScalar
h3cIKEInvalidCertAuthTrapCntl = _H3cIKEInvalidCertAuthTrapCntl_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 1, 5, 16),
    _H3cIKEInvalidCertAuthTrapCntl_Type()
)
h3cIKEInvalidCertAuthTrapCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIKEInvalidCertAuthTrapCntl.setStatus("current")
_H3cIKEInvalidSignTrapCntl_Type = H3cTrapStatus
_H3cIKEInvalidSignTrapCntl_Object = MibScalar
h3cIKEInvalidSignTrapCntl = _H3cIKEInvalidSignTrapCntl_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 1, 5, 17),
    _H3cIKEInvalidSignTrapCntl_Type()
)
h3cIKEInvalidSignTrapCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIKEInvalidSignTrapCntl.setStatus("current")
_H3cIKECertUnavailableTrapCntl_Type = H3cTrapStatus
_H3cIKECertUnavailableTrapCntl_Object = MibScalar
h3cIKECertUnavailableTrapCntl = _H3cIKECertUnavailableTrapCntl_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 1, 5, 18),
    _H3cIKECertUnavailableTrapCntl_Type()
)
h3cIKECertUnavailableTrapCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIKECertUnavailableTrapCntl.setStatus("current")
_H3cIKEProposalAddTrapCntl_Type = H3cTrapStatus
_H3cIKEProposalAddTrapCntl_Object = MibScalar
h3cIKEProposalAddTrapCntl = _H3cIKEProposalAddTrapCntl_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 1, 5, 19),
    _H3cIKEProposalAddTrapCntl_Type()
)
h3cIKEProposalAddTrapCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIKEProposalAddTrapCntl.setStatus("current")
_H3cIKEProposalDelTrapCntl_Type = H3cTrapStatus
_H3cIKEProposalDelTrapCntl_Object = MibScalar
h3cIKEProposalDelTrapCntl = _H3cIKEProposalDelTrapCntl_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 1, 5, 20),
    _H3cIKEProposalDelTrapCntl_Type()
)
h3cIKEProposalDelTrapCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIKEProposalDelTrapCntl.setStatus("current")
_H3cIKETrap_ObjectIdentity = ObjectIdentity
h3cIKETrap = _H3cIKETrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 1, 6)
)
_H3cIKENotifications_ObjectIdentity = ObjectIdentity
h3cIKENotifications = _H3cIKENotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 1, 6, 1)
)
_H3cIKEConformance_ObjectIdentity = ObjectIdentity
h3cIKEConformance = _H3cIKEConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 2)
)
_H3cIKECompliances_ObjectIdentity = ObjectIdentity
h3cIKECompliances = _H3cIKECompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 2, 1)
)
_H3cIKEGroups_ObjectIdentity = ObjectIdentity
h3cIKEGroups = _H3cIKEGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 2, 2)
)

# Managed Objects groups

h3cIKETunnelTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 2, 2, 1)
)
h3cIKETunnelTableGroup.setObjects(
      *(("H3C-IKE-MONITOR-MIB", "h3cIKETunLocalType"),
        ("H3C-IKE-MONITOR-MIB", "h3cIKETunLocalValue1"),
        ("H3C-IKE-MONITOR-MIB", "h3cIKETunLocalValue2"),
        ("H3C-IKE-MONITOR-MIB", "h3cIKETunLocalAddr"),
        ("H3C-IKE-MONITOR-MIB", "h3cIKETunRemoteType"),
        ("H3C-IKE-MONITOR-MIB", "h3cIKETunRemoteValue1"),
        ("H3C-IKE-MONITOR-MIB", "h3cIKETunRemoteValue2"),
        ("H3C-IKE-MONITOR-MIB", "h3cIKETunRemoteAddr"),
        ("H3C-IKE-MONITOR-MIB", "h3cIKETunInitiator"),
        ("H3C-IKE-MONITOR-MIB", "h3cIKETunNegoMode"),
        ("H3C-IKE-MONITOR-MIB", "h3cIKETunDiffHellmanGrp"),
        ("H3C-IKE-MONITOR-MIB", "h3cIKETunEncryptAlgo"),
        ("H3C-IKE-MONITOR-MIB", "h3cIKETunHashAlgo"),
        ("H3C-IKE-MONITOR-MIB", "h3cIKETunAuthMethod"),
        ("H3C-IKE-MONITOR-MIB", "h3cIKETunLifeTime"),
        ("H3C-IKE-MONITOR-MIB", "h3cIKETunActiveTime"),
        ("H3C-IKE-MONITOR-MIB", "h3cIKETunRemainTime"),
        ("H3C-IKE-MONITOR-MIB", "h3cIKETunTotalRefreshes"),
        ("H3C-IKE-MONITOR-MIB", "h3cIKETunState"),
        ("H3C-IKE-MONITOR-MIB", "h3cIKETunDpdIntervalTime"),
        ("H3C-IKE-MONITOR-MIB", "h3cIKETunDpdTimeOut"))
)
if mibBuilder.loadTexts:
    h3cIKETunnelTableGroup.setStatus("current")

h3cIKETunnelStatTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 2, 2, 2)
)
h3cIKETunnelStatTableGroup.setObjects(
      *(("H3C-IKE-MONITOR-MIB", "h3cIKETunInOctets"),
        ("H3C-IKE-MONITOR-MIB", "h3cIKETunInPkts"),
        ("H3C-IKE-MONITOR-MIB", "h3cIKETunInDropPkts"),
        ("H3C-IKE-MONITOR-MIB", "h3cIKETunInP2Exchgs"),
        ("H3C-IKE-MONITOR-MIB", "h3cIKETunInP2ExchgRejets"),
        ("H3C-IKE-MONITOR-MIB", "h3cIKETunInP2SaDelRequests"),
        ("H3C-IKE-MONITOR-MIB", "h3cIKETunInP1SaDelRequests"),
        ("H3C-IKE-MONITOR-MIB", "h3cIKETunInNotifys"),
        ("H3C-IKE-MONITOR-MIB", "h3cIKETunOutOctets"),
        ("H3C-IKE-MONITOR-MIB", "h3cIKETunOutPkts"),
        ("H3C-IKE-MONITOR-MIB", "h3cIKETunOutDropPkts"),
        ("H3C-IKE-MONITOR-MIB", "h3cIKETunOutP2Exchgs"),
        ("H3C-IKE-MONITOR-MIB", "h3cIKETunOutP2ExchgRejects"),
        ("H3C-IKE-MONITOR-MIB", "h3cIKETunOutP2SaDelRequests"),
        ("H3C-IKE-MONITOR-MIB", "h3cIKETunOutP1SaDelRequests"),
        ("H3C-IKE-MONITOR-MIB", "h3cIKETunOutNotifys"))
)
if mibBuilder.loadTexts:
    h3cIKETunnelStatTableGroup.setStatus("current")

h3cIKEGlobalStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 2, 2, 3)
)
h3cIKEGlobalStatsGroup.setObjects(
      *(("H3C-IKE-MONITOR-MIB", "h3cIKEGlobalActiveTunnels"),
        ("H3C-IKE-MONITOR-MIB", "h3cIKEGlobalInOctets"),
        ("H3C-IKE-MONITOR-MIB", "h3cIKEGlobalInPkts"),
        ("H3C-IKE-MONITOR-MIB", "h3cIKEGlobalInDropPkts"),
        ("H3C-IKE-MONITOR-MIB", "h3cIKEGlobalInP2Exchgs"),
        ("H3C-IKE-MONITOR-MIB", "h3cIKEGlobalInP2ExchgRejects"),
        ("H3C-IKE-MONITOR-MIB", "h3cIKEGlobalInP2SaDelRequests"),
        ("H3C-IKE-MONITOR-MIB", "h3cIKEGlobalInNotifys"),
        ("H3C-IKE-MONITOR-MIB", "h3cIKEGlobalOutOctets"),
        ("H3C-IKE-MONITOR-MIB", "h3cIKEGlobalOutPkts"),
        ("H3C-IKE-MONITOR-MIB", "h3cIKEGlobalOutDropPkts"),
        ("H3C-IKE-MONITOR-MIB", "h3cIKEGlobalOutP2Exchgs"),
        ("H3C-IKE-MONITOR-MIB", "h3cIKEGlobalOutP2ExchgRejects"),
        ("H3C-IKE-MONITOR-MIB", "h3cIKEGlobalOutP2SaDelRequests"),
        ("H3C-IKE-MONITOR-MIB", "h3cIKEGlobalOutNotifys"),
        ("H3C-IKE-MONITOR-MIB", "h3cIKEGlobalInitTunnels"),
        ("H3C-IKE-MONITOR-MIB", "h3cIKEGlobalInitTunnelFails"),
        ("H3C-IKE-MONITOR-MIB", "h3cIKEGlobalRespTunnels"),
        ("H3C-IKE-MONITOR-MIB", "h3cIKEGlobalRespTunnelFails"),
        ("H3C-IKE-MONITOR-MIB", "h3cIKEGlobalAuthFails"),
        ("H3C-IKE-MONITOR-MIB", "h3cIKEGlobalNoSaFails"),
        ("H3C-IKE-MONITOR-MIB", "h3cIKEGlobalInvalidCookieFails"),
        ("H3C-IKE-MONITOR-MIB", "h3cIKEGlobalAttrNotSuppFails"),
        ("H3C-IKE-MONITOR-MIB", "h3cIKEGlobalNoProposalChosenFails"),
        ("H3C-IKE-MONITOR-MIB", "h3cIKEGlobalUnsportExchTypeFails"),
        ("H3C-IKE-MONITOR-MIB", "h3cIKEGlobalInvalidIdFails"),
        ("H3C-IKE-MONITOR-MIB", "h3cIKEGlobalInvalidProFails"),
        ("H3C-IKE-MONITOR-MIB", "h3cIKEGlobalCertTypeUnsuppFails"),
        ("H3C-IKE-MONITOR-MIB", "h3cIKEGlobalInvalidCertAuthFails"),
        ("H3C-IKE-MONITOR-MIB", "h3cIKEGlobalInvalidSignFails"),
        ("H3C-IKE-MONITOR-MIB", "h3cIKEGlobalCertUnavailableFails"))
)
if mibBuilder.loadTexts:
    h3cIKEGlobalStatsGroup.setStatus("current")

h3cIKETrapObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 2, 2, 4)
)
h3cIKETrapObjectGroup.setObjects(
      *(("H3C-IKE-MONITOR-MIB", "h3cIKEProposalNumber"),
        ("H3C-IKE-MONITOR-MIB", "h3cIKEProposalSize"),
        ("H3C-IKE-MONITOR-MIB", "h3cIKEIdInformation"),
        ("H3C-IKE-MONITOR-MIB", "h3cIKEProtocolNum"),
        ("H3C-IKE-MONITOR-MIB", "h3cIKECertInformation"))
)
if mibBuilder.loadTexts:
    h3cIKETrapObjectGroup.setStatus("current")

h3cIKETrapCntlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 2, 2, 5)
)
h3cIKETrapCntlGroup.setObjects(
      *(("H3C-IKE-MONITOR-MIB", "h3cIKETrapGlobalCntl"),
        ("H3C-IKE-MONITOR-MIB", "h3cIKETunnelStartTrapCntl"),
        ("H3C-IKE-MONITOR-MIB", "h3cIKETunnelStopTrapCntl"),
        ("H3C-IKE-MONITOR-MIB", "h3cIKENoSaTrapCntl"),
        ("H3C-IKE-MONITOR-MIB", "h3cIKEEncryFailureTrapCntl"),
        ("H3C-IKE-MONITOR-MIB", "h3cIKEDecryFailureTrapCntl"),
        ("H3C-IKE-MONITOR-MIB", "h3cIKEInvalidProposalTrapCntl"),
        ("H3C-IKE-MONITOR-MIB", "h3cIKEAuthFailTrapCntl"),
        ("H3C-IKE-MONITOR-MIB", "h3cIKEInvalidCookieTrapCntl"),
        ("H3C-IKE-MONITOR-MIB", "h3cIKEInvalidSpiTrapCntl"),
        ("H3C-IKE-MONITOR-MIB", "h3cIKEAttrNotSuppTrapCntl"),
        ("H3C-IKE-MONITOR-MIB", "h3cIKEUnsportExchTypeTrapCntl"),
        ("H3C-IKE-MONITOR-MIB", "h3cIKEInvalidIdTrapCntl"),
        ("H3C-IKE-MONITOR-MIB", "h3cIKEInvalidProtocolTrapCntl"),
        ("H3C-IKE-MONITOR-MIB", "h3cIKECertTypeUnsuppTrapCntl"),
        ("H3C-IKE-MONITOR-MIB", "h3cIKEInvalidCertAuthTrapCntl"),
        ("H3C-IKE-MONITOR-MIB", "h3cIKEInvalidSignTrapCntl"),
        ("H3C-IKE-MONITOR-MIB", "h3cIKECertUnavailableTrapCntl"),
        ("H3C-IKE-MONITOR-MIB", "h3cIKEProposalAddTrapCntl"),
        ("H3C-IKE-MONITOR-MIB", "h3cIKEProposalDelTrapCntl"))
)
if mibBuilder.loadTexts:
    h3cIKETrapCntlGroup.setStatus("current")


# Notification objects

h3cIKETunnelStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 1, 6, 1, 1)
)
h3cIKETunnelStart.setObjects(
      *(("H3C-IKE-MONITOR-MIB", "h3cIKETunLocalAddr"),
        ("H3C-IKE-MONITOR-MIB", "h3cIKETunRemoteAddr"),
        ("H3C-IKE-MONITOR-MIB", "h3cIKETunLifeTime"))
)
if mibBuilder.loadTexts:
    h3cIKETunnelStart.setStatus(
        "current"
    )

h3cIKETunnelStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 1, 6, 1, 2)
)
h3cIKETunnelStop.setObjects(
      *(("H3C-IKE-MONITOR-MIB", "h3cIKETunLocalAddr"),
        ("H3C-IKE-MONITOR-MIB", "h3cIKETunRemoteAddr"),
        ("H3C-IKE-MONITOR-MIB", "h3cIKETunActiveTime"))
)
if mibBuilder.loadTexts:
    h3cIKETunnelStop.setStatus(
        "current"
    )

h3cIKENoSaFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 1, 6, 1, 3)
)
h3cIKENoSaFailure.setObjects(
      *(("H3C-IKE-MONITOR-MIB", "h3cIKETunLocalAddr"),
        ("H3C-IKE-MONITOR-MIB", "h3cIKETunRemoteAddr"))
)
if mibBuilder.loadTexts:
    h3cIKENoSaFailure.setStatus(
        "current"
    )

h3cIKEEncryFailFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 1, 6, 1, 4)
)
h3cIKEEncryFailFailure.setObjects(
      *(("H3C-IKE-MONITOR-MIB", "h3cIKETunLocalAddr"),
        ("H3C-IKE-MONITOR-MIB", "h3cIKETunRemoteAddr"))
)
if mibBuilder.loadTexts:
    h3cIKEEncryFailFailure.setStatus(
        "current"
    )

h3cIKEDecryFailFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 1, 6, 1, 5)
)
h3cIKEDecryFailFailure.setObjects(
      *(("H3C-IKE-MONITOR-MIB", "h3cIKETunLocalAddr"),
        ("H3C-IKE-MONITOR-MIB", "h3cIKETunRemoteAddr"))
)
if mibBuilder.loadTexts:
    h3cIKEDecryFailFailure.setStatus(
        "current"
    )

h3cIKEInvalidProposalFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 1, 6, 1, 6)
)
h3cIKEInvalidProposalFailure.setObjects(
      *(("H3C-IKE-MONITOR-MIB", "h3cIKETunLocalAddr"),
        ("H3C-IKE-MONITOR-MIB", "h3cIKETunRemoteAddr"))
)
if mibBuilder.loadTexts:
    h3cIKEInvalidProposalFailure.setStatus(
        "current"
    )

h3cIKEAuthFailFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 1, 6, 1, 7)
)
h3cIKEAuthFailFailure.setObjects(
      *(("H3C-IKE-MONITOR-MIB", "h3cIKETunLocalAddr"),
        ("H3C-IKE-MONITOR-MIB", "h3cIKETunRemoteAddr"))
)
if mibBuilder.loadTexts:
    h3cIKEAuthFailFailure.setStatus(
        "current"
    )

h3cIKEInvalidCookieFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 1, 6, 1, 8)
)
h3cIKEInvalidCookieFailure.setObjects(
      *(("H3C-IKE-MONITOR-MIB", "h3cIKETunLocalAddr"),
        ("H3C-IKE-MONITOR-MIB", "h3cIKETunRemoteAddr"))
)
if mibBuilder.loadTexts:
    h3cIKEInvalidCookieFailure.setStatus(
        "current"
    )

h3cIKEAttrNotSuppFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 1, 6, 1, 9)
)
h3cIKEAttrNotSuppFailure.setObjects(
      *(("H3C-IKE-MONITOR-MIB", "h3cIKETunLocalAddr"),
        ("H3C-IKE-MONITOR-MIB", "h3cIKETunRemoteAddr"))
)
if mibBuilder.loadTexts:
    h3cIKEAttrNotSuppFailure.setStatus(
        "current"
    )

h3cIKEUnsportExchTypeFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 1, 6, 1, 10)
)
h3cIKEUnsportExchTypeFailure.setObjects(
      *(("H3C-IKE-MONITOR-MIB", "h3cIKETunLocalAddr"),
        ("H3C-IKE-MONITOR-MIB", "h3cIKETunRemoteAddr"))
)
if mibBuilder.loadTexts:
    h3cIKEUnsportExchTypeFailure.setStatus(
        "current"
    )

h3cIKEInvalidIdFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 1, 6, 1, 11)
)
h3cIKEInvalidIdFailure.setObjects(
      *(("H3C-IKE-MONITOR-MIB", "h3cIKETunLocalAddr"),
        ("H3C-IKE-MONITOR-MIB", "h3cIKETunRemoteAddr"),
        ("H3C-IKE-MONITOR-MIB", "h3cIKEIdInformation"))
)
if mibBuilder.loadTexts:
    h3cIKEInvalidIdFailure.setStatus(
        "current"
    )

h3cIKEInvalidProtocolFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 1, 6, 1, 12)
)
h3cIKEInvalidProtocolFailure.setObjects(
      *(("H3C-IKE-MONITOR-MIB", "h3cIKETunLocalAddr"),
        ("H3C-IKE-MONITOR-MIB", "h3cIKETunRemoteAddr"),
        ("H3C-IKE-MONITOR-MIB", "h3cIKEProtocolNum"))
)
if mibBuilder.loadTexts:
    h3cIKEInvalidProtocolFailure.setStatus(
        "current"
    )

h3cIKECertTypeUnsuppFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 1, 6, 1, 13)
)
h3cIKECertTypeUnsuppFailure.setObjects(
      *(("H3C-IKE-MONITOR-MIB", "h3cIKETunLocalAddr"),
        ("H3C-IKE-MONITOR-MIB", "h3cIKETunRemoteAddr"),
        ("H3C-IKE-MONITOR-MIB", "h3cIKECertInformation"))
)
if mibBuilder.loadTexts:
    h3cIKECertTypeUnsuppFailure.setStatus(
        "current"
    )

h3cIKEInvalidCertAuthFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 1, 6, 1, 14)
)
h3cIKEInvalidCertAuthFailure.setObjects(
      *(("H3C-IKE-MONITOR-MIB", "h3cIKETunLocalAddr"),
        ("H3C-IKE-MONITOR-MIB", "h3cIKETunRemoteAddr"),
        ("H3C-IKE-MONITOR-MIB", "h3cIKECertInformation"))
)
if mibBuilder.loadTexts:
    h3cIKEInvalidCertAuthFailure.setStatus(
        "current"
    )

h3cIKElInvalidSignFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 1, 6, 1, 15)
)
h3cIKElInvalidSignFailure.setObjects(
      *(("H3C-IKE-MONITOR-MIB", "h3cIKETunLocalAddr"),
        ("H3C-IKE-MONITOR-MIB", "h3cIKETunRemoteAddr"),
        ("H3C-IKE-MONITOR-MIB", "h3cIKECertInformation"))
)
if mibBuilder.loadTexts:
    h3cIKElInvalidSignFailure.setStatus(
        "current"
    )

h3cIKECertUnavailableFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 1, 6, 1, 16)
)
h3cIKECertUnavailableFailure.setObjects(
      *(("H3C-IKE-MONITOR-MIB", "h3cIKETunLocalAddr"),
        ("H3C-IKE-MONITOR-MIB", "h3cIKETunRemoteAddr"),
        ("H3C-IKE-MONITOR-MIB", "h3cIKECertInformation"))
)
if mibBuilder.loadTexts:
    h3cIKECertUnavailableFailure.setStatus(
        "current"
    )

h3cIKEProposalAdd = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 1, 6, 1, 17)
)
h3cIKEProposalAdd.setObjects(
      *(("H3C-IKE-MONITOR-MIB", "h3cIKEProposalNumber"),
        ("H3C-IKE-MONITOR-MIB", "h3cIKEProposalSize"))
)
if mibBuilder.loadTexts:
    h3cIKEProposalAdd.setStatus(
        "current"
    )

h3cIKEProposalDel = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 1, 6, 1, 18)
)
h3cIKEProposalDel.setObjects(
      *(("H3C-IKE-MONITOR-MIB", "h3cIKEProposalNumber"),
        ("H3C-IKE-MONITOR-MIB", "h3cIKEProposalSize"))
)
if mibBuilder.loadTexts:
    h3cIKEProposalDel.setStatus(
        "current"
    )


# Notifications groups

h3cIKETrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 2, 2, 6)
)
h3cIKETrapGroup.setObjects(
      *(("H3C-IKE-MONITOR-MIB", "h3cIKETunnelStart"),
        ("H3C-IKE-MONITOR-MIB", "h3cIKETunnelStop"),
        ("H3C-IKE-MONITOR-MIB", "h3cIKENoSaFailure"),
        ("H3C-IKE-MONITOR-MIB", "h3cIKEEncryFailFailure"),
        ("H3C-IKE-MONITOR-MIB", "h3cIKEDecryFailFailure"),
        ("H3C-IKE-MONITOR-MIB", "h3cIKEInvalidProposalFailure"),
        ("H3C-IKE-MONITOR-MIB", "h3cIKEAuthFailFailure"),
        ("H3C-IKE-MONITOR-MIB", "h3cIKEInvalidCookieFailure"),
        ("H3C-IKE-MONITOR-MIB", "h3cIKEAttrNotSuppFailure"),
        ("H3C-IKE-MONITOR-MIB", "h3cIKEUnsportExchTypeFailure"),
        ("H3C-IKE-MONITOR-MIB", "h3cIKEInvalidIdFailure"),
        ("H3C-IKE-MONITOR-MIB", "h3cIKEInvalidProtocolFailure"),
        ("H3C-IKE-MONITOR-MIB", "h3cIKECertTypeUnsuppFailure"),
        ("H3C-IKE-MONITOR-MIB", "h3cIKEInvalidCertAuthFailure"),
        ("H3C-IKE-MONITOR-MIB", "h3cIKElInvalidSignFailure"),
        ("H3C-IKE-MONITOR-MIB", "h3cIKECertUnavailableFailure"),
        ("H3C-IKE-MONITOR-MIB", "h3cIKEProposalAdd"),
        ("H3C-IKE-MONITOR-MIB", "h3cIKEProposalDel"))
)
if mibBuilder.loadTexts:
    h3cIKETrapGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

h3cIKECompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 30, 2, 1, 1)
)
if mibBuilder.loadTexts:
    h3cIKECompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-IKE-MONITOR-MIB",
    **{"H3cIKENegoMode": H3cIKENegoMode,
       "H3cIKEAuthMethod": H3cIKEAuthMethod,
       "H3cDiffHellmanGrp": H3cDiffHellmanGrp,
       "H3cEncryptAlgo": H3cEncryptAlgo,
       "H3cAuthAlgo": H3cAuthAlgo,
       "H3cSaProtocol": H3cSaProtocol,
       "H3cTrapStatus": H3cTrapStatus,
       "H3cIKEIDType": H3cIKEIDType,
       "H3cTrafficType": H3cTrafficType,
       "H3cIKETunnelState": H3cIKETunnelState,
       "h3cIKEMonitor": h3cIKEMonitor,
       "h3cIKEObjects": h3cIKEObjects,
       "h3cIKETunnelTable": h3cIKETunnelTable,
       "h3cIKETunnelEntry": h3cIKETunnelEntry,
       "h3cIKETunIndex": h3cIKETunIndex,
       "h3cIKETunLocalType": h3cIKETunLocalType,
       "h3cIKETunLocalValue1": h3cIKETunLocalValue1,
       "h3cIKETunLocalValue2": h3cIKETunLocalValue2,
       "h3cIKETunLocalAddr": h3cIKETunLocalAddr,
       "h3cIKETunRemoteType": h3cIKETunRemoteType,
       "h3cIKETunRemoteValue1": h3cIKETunRemoteValue1,
       "h3cIKETunRemoteValue2": h3cIKETunRemoteValue2,
       "h3cIKETunRemoteAddr": h3cIKETunRemoteAddr,
       "h3cIKETunInitiator": h3cIKETunInitiator,
       "h3cIKETunNegoMode": h3cIKETunNegoMode,
       "h3cIKETunDiffHellmanGrp": h3cIKETunDiffHellmanGrp,
       "h3cIKETunEncryptAlgo": h3cIKETunEncryptAlgo,
       "h3cIKETunHashAlgo": h3cIKETunHashAlgo,
       "h3cIKETunAuthMethod": h3cIKETunAuthMethod,
       "h3cIKETunLifeTime": h3cIKETunLifeTime,
       "h3cIKETunActiveTime": h3cIKETunActiveTime,
       "h3cIKETunRemainTime": h3cIKETunRemainTime,
       "h3cIKETunTotalRefreshes": h3cIKETunTotalRefreshes,
       "h3cIKETunState": h3cIKETunState,
       "h3cIKETunDpdIntervalTime": h3cIKETunDpdIntervalTime,
       "h3cIKETunDpdTimeOut": h3cIKETunDpdTimeOut,
       "h3cIKETunnelStatTable": h3cIKETunnelStatTable,
       "h3cIKETunnelStatEntry": h3cIKETunnelStatEntry,
       "h3cIKETunInOctets": h3cIKETunInOctets,
       "h3cIKETunInPkts": h3cIKETunInPkts,
       "h3cIKETunInDropPkts": h3cIKETunInDropPkts,
       "h3cIKETunInP2Exchgs": h3cIKETunInP2Exchgs,
       "h3cIKETunInP2ExchgRejets": h3cIKETunInP2ExchgRejets,
       "h3cIKETunInP2SaDelRequests": h3cIKETunInP2SaDelRequests,
       "h3cIKETunInP1SaDelRequests": h3cIKETunInP1SaDelRequests,
       "h3cIKETunInNotifys": h3cIKETunInNotifys,
       "h3cIKETunOutOctets": h3cIKETunOutOctets,
       "h3cIKETunOutPkts": h3cIKETunOutPkts,
       "h3cIKETunOutDropPkts": h3cIKETunOutDropPkts,
       "h3cIKETunOutP2Exchgs": h3cIKETunOutP2Exchgs,
       "h3cIKETunOutP2ExchgRejects": h3cIKETunOutP2ExchgRejects,
       "h3cIKETunOutP2SaDelRequests": h3cIKETunOutP2SaDelRequests,
       "h3cIKETunOutP1SaDelRequests": h3cIKETunOutP1SaDelRequests,
       "h3cIKETunOutNotifys": h3cIKETunOutNotifys,
       "h3cIKEGlobalStats": h3cIKEGlobalStats,
       "h3cIKEGlobalActiveTunnels": h3cIKEGlobalActiveTunnels,
       "h3cIKEGlobalInOctets": h3cIKEGlobalInOctets,
       "h3cIKEGlobalInPkts": h3cIKEGlobalInPkts,
       "h3cIKEGlobalInDropPkts": h3cIKEGlobalInDropPkts,
       "h3cIKEGlobalInP2Exchgs": h3cIKEGlobalInP2Exchgs,
       "h3cIKEGlobalInP2ExchgRejects": h3cIKEGlobalInP2ExchgRejects,
       "h3cIKEGlobalInP2SaDelRequests": h3cIKEGlobalInP2SaDelRequests,
       "h3cIKEGlobalInNotifys": h3cIKEGlobalInNotifys,
       "h3cIKEGlobalOutOctets": h3cIKEGlobalOutOctets,
       "h3cIKEGlobalOutPkts": h3cIKEGlobalOutPkts,
       "h3cIKEGlobalOutDropPkts": h3cIKEGlobalOutDropPkts,
       "h3cIKEGlobalOutP2Exchgs": h3cIKEGlobalOutP2Exchgs,
       "h3cIKEGlobalOutP2ExchgRejects": h3cIKEGlobalOutP2ExchgRejects,
       "h3cIKEGlobalOutP2SaDelRequests": h3cIKEGlobalOutP2SaDelRequests,
       "h3cIKEGlobalOutNotifys": h3cIKEGlobalOutNotifys,
       "h3cIKEGlobalInitTunnels": h3cIKEGlobalInitTunnels,
       "h3cIKEGlobalInitTunnelFails": h3cIKEGlobalInitTunnelFails,
       "h3cIKEGlobalRespTunnels": h3cIKEGlobalRespTunnels,
       "h3cIKEGlobalRespTunnelFails": h3cIKEGlobalRespTunnelFails,
       "h3cIKEGlobalAuthFails": h3cIKEGlobalAuthFails,
       "h3cIKEGlobalNoSaFails": h3cIKEGlobalNoSaFails,
       "h3cIKEGlobalInvalidCookieFails": h3cIKEGlobalInvalidCookieFails,
       "h3cIKEGlobalAttrNotSuppFails": h3cIKEGlobalAttrNotSuppFails,
       "h3cIKEGlobalNoProposalChosenFails": h3cIKEGlobalNoProposalChosenFails,
       "h3cIKEGlobalUnsportExchTypeFails": h3cIKEGlobalUnsportExchTypeFails,
       "h3cIKEGlobalInvalidIdFails": h3cIKEGlobalInvalidIdFails,
       "h3cIKEGlobalInvalidProFails": h3cIKEGlobalInvalidProFails,
       "h3cIKEGlobalCertTypeUnsuppFails": h3cIKEGlobalCertTypeUnsuppFails,
       "h3cIKEGlobalInvalidCertAuthFails": h3cIKEGlobalInvalidCertAuthFails,
       "h3cIKEGlobalInvalidSignFails": h3cIKEGlobalInvalidSignFails,
       "h3cIKEGlobalCertUnavailableFails": h3cIKEGlobalCertUnavailableFails,
       "h3cIKETrapObject": h3cIKETrapObject,
       "h3cIKEProposalNumber": h3cIKEProposalNumber,
       "h3cIKEProposalSize": h3cIKEProposalSize,
       "h3cIKEIdInformation": h3cIKEIdInformation,
       "h3cIKEProtocolNum": h3cIKEProtocolNum,
       "h3cIKECertInformation": h3cIKECertInformation,
       "h3cIKETrapCntl": h3cIKETrapCntl,
       "h3cIKETrapGlobalCntl": h3cIKETrapGlobalCntl,
       "h3cIKETunnelStartTrapCntl": h3cIKETunnelStartTrapCntl,
       "h3cIKETunnelStopTrapCntl": h3cIKETunnelStopTrapCntl,
       "h3cIKENoSaTrapCntl": h3cIKENoSaTrapCntl,
       "h3cIKEEncryFailureTrapCntl": h3cIKEEncryFailureTrapCntl,
       "h3cIKEDecryFailureTrapCntl": h3cIKEDecryFailureTrapCntl,
       "h3cIKEInvalidProposalTrapCntl": h3cIKEInvalidProposalTrapCntl,
       "h3cIKEAuthFailTrapCntl": h3cIKEAuthFailTrapCntl,
       "h3cIKEInvalidCookieTrapCntl": h3cIKEInvalidCookieTrapCntl,
       "h3cIKEInvalidSpiTrapCntl": h3cIKEInvalidSpiTrapCntl,
       "h3cIKEAttrNotSuppTrapCntl": h3cIKEAttrNotSuppTrapCntl,
       "h3cIKEUnsportExchTypeTrapCntl": h3cIKEUnsportExchTypeTrapCntl,
       "h3cIKEInvalidIdTrapCntl": h3cIKEInvalidIdTrapCntl,
       "h3cIKEInvalidProtocolTrapCntl": h3cIKEInvalidProtocolTrapCntl,
       "h3cIKECertTypeUnsuppTrapCntl": h3cIKECertTypeUnsuppTrapCntl,
       "h3cIKEInvalidCertAuthTrapCntl": h3cIKEInvalidCertAuthTrapCntl,
       "h3cIKEInvalidSignTrapCntl": h3cIKEInvalidSignTrapCntl,
       "h3cIKECertUnavailableTrapCntl": h3cIKECertUnavailableTrapCntl,
       "h3cIKEProposalAddTrapCntl": h3cIKEProposalAddTrapCntl,
       "h3cIKEProposalDelTrapCntl": h3cIKEProposalDelTrapCntl,
       "h3cIKETrap": h3cIKETrap,
       "h3cIKENotifications": h3cIKENotifications,
       "h3cIKETunnelStart": h3cIKETunnelStart,
       "h3cIKETunnelStop": h3cIKETunnelStop,
       "h3cIKENoSaFailure": h3cIKENoSaFailure,
       "h3cIKEEncryFailFailure": h3cIKEEncryFailFailure,
       "h3cIKEDecryFailFailure": h3cIKEDecryFailFailure,
       "h3cIKEInvalidProposalFailure": h3cIKEInvalidProposalFailure,
       "h3cIKEAuthFailFailure": h3cIKEAuthFailFailure,
       "h3cIKEInvalidCookieFailure": h3cIKEInvalidCookieFailure,
       "h3cIKEAttrNotSuppFailure": h3cIKEAttrNotSuppFailure,
       "h3cIKEUnsportExchTypeFailure": h3cIKEUnsportExchTypeFailure,
       "h3cIKEInvalidIdFailure": h3cIKEInvalidIdFailure,
       "h3cIKEInvalidProtocolFailure": h3cIKEInvalidProtocolFailure,
       "h3cIKECertTypeUnsuppFailure": h3cIKECertTypeUnsuppFailure,
       "h3cIKEInvalidCertAuthFailure": h3cIKEInvalidCertAuthFailure,
       "h3cIKElInvalidSignFailure": h3cIKElInvalidSignFailure,
       "h3cIKECertUnavailableFailure": h3cIKECertUnavailableFailure,
       "h3cIKEProposalAdd": h3cIKEProposalAdd,
       "h3cIKEProposalDel": h3cIKEProposalDel,
       "h3cIKEConformance": h3cIKEConformance,
       "h3cIKECompliances": h3cIKECompliances,
       "h3cIKECompliance": h3cIKECompliance,
       "h3cIKEGroups": h3cIKEGroups,
       "h3cIKETunnelTableGroup": h3cIKETunnelTableGroup,
       "h3cIKETunnelStatTableGroup": h3cIKETunnelStatTableGroup,
       "h3cIKEGlobalStatsGroup": h3cIKEGlobalStatsGroup,
       "h3cIKETrapObjectGroup": h3cIKETrapObjectGroup,
       "h3cIKETrapCntlGroup": h3cIKETrapCntlGroup,
       "h3cIKETrapGroup": h3cIKETrapGroup}
)
