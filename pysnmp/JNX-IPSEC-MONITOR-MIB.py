# SNMP MIB module (JNX-IPSEC-MONITOR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/JNX-IPSEC-MONITOR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:12:39 2024
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(jnxMibs,) = mibBuilder.importSymbols(
    "JUNIPER-SMI",
    "jnxMibs")

(jnxSpSvcSetName,) = mibBuilder.importSymbols(
    "JUNIPER-SP-MIB",
    "jnxSpSvcSetName")

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
 TextualConvention,
 TimeInterval) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeInterval")


# MODULE-IDENTITY

jnxIpSecMonitorMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 22)
)
jnxIpSecMonitorMIB.setRevisions(
        ("2012-02-10 21:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class JnxIkePeerType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("idDn", 3),
          ("idFqdn", 2),
          ("idIpv4Addr", 1),
          ("unknown", 0))
    )



class JnxIkeNegoMode(Integer32, TextualConvention):
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
        *(("aggressive", 2),
          ("ikev2", 3),
          ("main", 1))
    )



class JnxIkeHashAlgo(Integer32, TextualConvention):
    status = "current"
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
        *(("md5", 1),
          ("sha", 2),
          ("sha256", 3),
          ("sha384", 4))
    )



class JnxIkeAuthMethod(Integer32, TextualConvention):
    status = "current"
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
        *(("dssSignature", 2),
          ("preSharedKey", 1),
          ("revRsaEncryption", 5),
          ("rsaEncryption", 4),
          ("rsaSignature", 3))
    )



class JnxIkePeerRole(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("initiator", 1),
          ("responder", 2))
    )



class JnxIkeNegState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("matured", 1),
          ("notmatured", 2))
    )



class JnxDiffHellmanGrp(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              5,
              14,
              19,
              20)
        )
    )
    namedValues = NamedValues(
        *(("ecmodp256", 19),
          ("ecmodp384", 20),
          ("modp1024", 2),
          ("modp1536", 5),
          ("modp2048", 14),
          ("modp768", 1),
          ("unknown", 0))
    )



class JnxKeyType(Integer32, TextualConvention):
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
        *(("keyIke", 1),
          ("keyManual", 2),
          ("unknown", 0))
    )



class JnxEncapMode(Integer32, TextualConvention):
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
        *(("transport", 2),
          ("tunnel", 1),
          ("unknown", 0))
    )



class JnxEncryptAlgo(Integer32, TextualConvention):
    status = "current"
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
        *(("esp3des", 2),
          ("espAes128", 4),
          ("espAes192", 5),
          ("espAes256", 6),
          ("espDes", 1),
          ("espNull", 3))
    )



class JnxSpi(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 4294967295),
    )



class JnxAuthAlgo(Integer32, TextualConvention):
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
        *(("hmacMd5", 2),
          ("hmacSha", 3),
          ("hmacSha256", 4),
          ("unknown", 0))
    )



class JnxRemotePeerType(Integer32, TextualConvention):
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
        *(("dynamic", 2),
          ("static", 1),
          ("unknown", 0))
    )



class JnxSAType(Integer32, TextualConvention):
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
        *(("dynamic", 2),
          ("manual", 1),
          ("unknown", 0))
    )



# MIB Managed Objects in the order of their OIDs

_JnxIpSecMIBObjects_ObjectIdentity = ObjectIdentity
jnxIpSecMIBObjects = _JnxIpSecMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 22, 1)
)
_JnxIpSecLevels_ObjectIdentity = ObjectIdentity
jnxIpSecLevels = _JnxIpSecLevels_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 22, 1, 1)
)


class _JnxIpSecMibLevel_Type(Integer32):
    """Custom type jnxIpSecMibLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_JnxIpSecMibLevel_Type.__name__ = "Integer32"
_JnxIpSecMibLevel_Object = MibScalar
jnxIpSecMibLevel = _JnxIpSecMibLevel_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 22, 1, 1, 1),
    _JnxIpSecMibLevel_Type()
)
jnxIpSecMibLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecMibLevel.setStatus("current")
_JnxIpSecPhaseOne_ObjectIdentity = ObjectIdentity
jnxIpSecPhaseOne = _JnxIpSecPhaseOne_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 22, 1, 2)
)
_JnxIkeTunnelTable_Object = MibTable
jnxIkeTunnelTable = _JnxIkeTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 22, 1, 2, 1)
)
if mibBuilder.loadTexts:
    jnxIkeTunnelTable.setStatus("current")
_JnxIkeTunnelEntry_Object = MibTableRow
jnxIkeTunnelEntry = _JnxIkeTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 22, 1, 2, 1, 1)
)
jnxIkeTunnelEntry.setIndexNames(
    (0, "JUNIPER-SP-MIB", "jnxSpSvcSetName"),
    (0, "JNX-IPSEC-MONITOR-MIB", "jnxIkeTunRemoteGwAddrType"),
    (0, "JNX-IPSEC-MONITOR-MIB", "jnxIkeTunRemoteGwAddr"),
    (0, "JNX-IPSEC-MONITOR-MIB", "jnxIkeTunIndex"),
)
if mibBuilder.loadTexts:
    jnxIkeTunnelEntry.setStatus("current")


class _JnxIkeTunIndex_Type(Integer32):
    """Custom type jnxIkeTunIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_JnxIkeTunIndex_Type.__name__ = "Integer32"
_JnxIkeTunIndex_Object = MibTableColumn
jnxIkeTunIndex = _JnxIkeTunIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 22, 1, 2, 1, 1, 1),
    _JnxIkeTunIndex_Type()
)
jnxIkeTunIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxIkeTunIndex.setStatus("current")
_JnxIkeTunLocalRole_Type = JnxIkePeerRole
_JnxIkeTunLocalRole_Object = MibTableColumn
jnxIkeTunLocalRole = _JnxIkeTunLocalRole_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 22, 1, 2, 1, 1, 2),
    _JnxIkeTunLocalRole_Type()
)
jnxIkeTunLocalRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeTunLocalRole.setStatus("current")
_JnxIkeTunNegState_Type = JnxIkeNegState
_JnxIkeTunNegState_Object = MibTableColumn
jnxIkeTunNegState = _JnxIkeTunNegState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 22, 1, 2, 1, 1, 3),
    _JnxIkeTunNegState_Type()
)
jnxIkeTunNegState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeTunNegState.setStatus("current")
_JnxIkeTunInitiatorCookie_Type = DisplayString
_JnxIkeTunInitiatorCookie_Object = MibTableColumn
jnxIkeTunInitiatorCookie = _JnxIkeTunInitiatorCookie_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 22, 1, 2, 1, 1, 4),
    _JnxIkeTunInitiatorCookie_Type()
)
jnxIkeTunInitiatorCookie.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeTunInitiatorCookie.setStatus("current")
_JnxIkeTunResponderCookie_Type = DisplayString
_JnxIkeTunResponderCookie_Object = MibTableColumn
jnxIkeTunResponderCookie = _JnxIkeTunResponderCookie_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 22, 1, 2, 1, 1, 5),
    _JnxIkeTunResponderCookie_Type()
)
jnxIkeTunResponderCookie.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeTunResponderCookie.setStatus("current")
_JnxIkeTunLocalIdType_Type = JnxIkePeerType
_JnxIkeTunLocalIdType_Object = MibTableColumn
jnxIkeTunLocalIdType = _JnxIkeTunLocalIdType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 22, 1, 2, 1, 1, 6),
    _JnxIkeTunLocalIdType_Type()
)
jnxIkeTunLocalIdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeTunLocalIdType.setStatus("current")
_JnxIkeTunLocalIdValue_Type = DisplayString
_JnxIkeTunLocalIdValue_Object = MibTableColumn
jnxIkeTunLocalIdValue = _JnxIkeTunLocalIdValue_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 22, 1, 2, 1, 1, 7),
    _JnxIkeTunLocalIdValue_Type()
)
jnxIkeTunLocalIdValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeTunLocalIdValue.setStatus("current")
_JnxIkeTunLocalGwAddrType_Type = InetAddressType
_JnxIkeTunLocalGwAddrType_Object = MibTableColumn
jnxIkeTunLocalGwAddrType = _JnxIkeTunLocalGwAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 22, 1, 2, 1, 1, 8),
    _JnxIkeTunLocalGwAddrType_Type()
)
jnxIkeTunLocalGwAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeTunLocalGwAddrType.setStatus("current")
_JnxIkeTunLocalGwAddr_Type = InetAddress
_JnxIkeTunLocalGwAddr_Object = MibTableColumn
jnxIkeTunLocalGwAddr = _JnxIkeTunLocalGwAddr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 22, 1, 2, 1, 1, 9),
    _JnxIkeTunLocalGwAddr_Type()
)
jnxIkeTunLocalGwAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeTunLocalGwAddr.setStatus("current")
_JnxIkeTunLocalCertName_Type = DisplayString
_JnxIkeTunLocalCertName_Object = MibTableColumn
jnxIkeTunLocalCertName = _JnxIkeTunLocalCertName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 22, 1, 2, 1, 1, 10),
    _JnxIkeTunLocalCertName_Type()
)
jnxIkeTunLocalCertName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeTunLocalCertName.setStatus("current")
_JnxIkeTunRemoteIdType_Type = JnxIkePeerType
_JnxIkeTunRemoteIdType_Object = MibTableColumn
jnxIkeTunRemoteIdType = _JnxIkeTunRemoteIdType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 22, 1, 2, 1, 1, 11),
    _JnxIkeTunRemoteIdType_Type()
)
jnxIkeTunRemoteIdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeTunRemoteIdType.setStatus("current")
_JnxIkeTunRemoteIdValue_Type = DisplayString
_JnxIkeTunRemoteIdValue_Object = MibTableColumn
jnxIkeTunRemoteIdValue = _JnxIkeTunRemoteIdValue_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 22, 1, 2, 1, 1, 12),
    _JnxIkeTunRemoteIdValue_Type()
)
jnxIkeTunRemoteIdValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeTunRemoteIdValue.setStatus("current")
_JnxIkeTunRemoteGwAddrType_Type = InetAddressType
_JnxIkeTunRemoteGwAddrType_Object = MibTableColumn
jnxIkeTunRemoteGwAddrType = _JnxIkeTunRemoteGwAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 22, 1, 2, 1, 1, 13),
    _JnxIkeTunRemoteGwAddrType_Type()
)
jnxIkeTunRemoteGwAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeTunRemoteGwAddrType.setStatus("current")
_JnxIkeTunRemoteGwAddr_Type = InetAddress
_JnxIkeTunRemoteGwAddr_Object = MibTableColumn
jnxIkeTunRemoteGwAddr = _JnxIkeTunRemoteGwAddr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 22, 1, 2, 1, 1, 14),
    _JnxIkeTunRemoteGwAddr_Type()
)
jnxIkeTunRemoteGwAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeTunRemoteGwAddr.setStatus("current")
_JnxIkeTunNegoMode_Type = JnxIkeNegoMode
_JnxIkeTunNegoMode_Object = MibTableColumn
jnxIkeTunNegoMode = _JnxIkeTunNegoMode_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 22, 1, 2, 1, 1, 15),
    _JnxIkeTunNegoMode_Type()
)
jnxIkeTunNegoMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeTunNegoMode.setStatus("current")
_JnxIkeTunDiffHellmanGrp_Type = JnxDiffHellmanGrp
_JnxIkeTunDiffHellmanGrp_Object = MibTableColumn
jnxIkeTunDiffHellmanGrp = _JnxIkeTunDiffHellmanGrp_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 22, 1, 2, 1, 1, 16),
    _JnxIkeTunDiffHellmanGrp_Type()
)
jnxIkeTunDiffHellmanGrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeTunDiffHellmanGrp.setStatus("current")
_JnxIkeTunEncryptAlgo_Type = JnxEncryptAlgo
_JnxIkeTunEncryptAlgo_Object = MibTableColumn
jnxIkeTunEncryptAlgo = _JnxIkeTunEncryptAlgo_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 22, 1, 2, 1, 1, 17),
    _JnxIkeTunEncryptAlgo_Type()
)
jnxIkeTunEncryptAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeTunEncryptAlgo.setStatus("current")
_JnxIkeTunHashAlgo_Type = JnxIkeHashAlgo
_JnxIkeTunHashAlgo_Object = MibTableColumn
jnxIkeTunHashAlgo = _JnxIkeTunHashAlgo_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 22, 1, 2, 1, 1, 18),
    _JnxIkeTunHashAlgo_Type()
)
jnxIkeTunHashAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeTunHashAlgo.setStatus("current")
_JnxIkeTunAuthMethod_Type = JnxIkeAuthMethod
_JnxIkeTunAuthMethod_Object = MibTableColumn
jnxIkeTunAuthMethod = _JnxIkeTunAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 22, 1, 2, 1, 1, 19),
    _JnxIkeTunAuthMethod_Type()
)
jnxIkeTunAuthMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeTunAuthMethod.setStatus("current")


class _JnxIkeTunLifeTime_Type(Integer32):
    """Custom type jnxIkeTunLifeTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_JnxIkeTunLifeTime_Type.__name__ = "Integer32"
_JnxIkeTunLifeTime_Object = MibTableColumn
jnxIkeTunLifeTime = _JnxIkeTunLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 22, 1, 2, 1, 1, 20),
    _JnxIkeTunLifeTime_Type()
)
jnxIkeTunLifeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeTunLifeTime.setStatus("current")
if mibBuilder.loadTexts:
    jnxIkeTunLifeTime.setUnits("seconds")
_JnxIkeTunActiveTime_Type = TimeInterval
_JnxIkeTunActiveTime_Object = MibTableColumn
jnxIkeTunActiveTime = _JnxIkeTunActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 22, 1, 2, 1, 1, 21),
    _JnxIkeTunActiveTime_Type()
)
jnxIkeTunActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeTunActiveTime.setStatus("current")
_JnxIkeTunInOctets_Type = Counter64
_JnxIkeTunInOctets_Object = MibTableColumn
jnxIkeTunInOctets = _JnxIkeTunInOctets_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 22, 1, 2, 1, 1, 22),
    _JnxIkeTunInOctets_Type()
)
jnxIkeTunInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeTunInOctets.setStatus("current")
if mibBuilder.loadTexts:
    jnxIkeTunInOctets.setUnits("Octets")
_JnxIkeTunInPkts_Type = Counter32
_JnxIkeTunInPkts_Object = MibTableColumn
jnxIkeTunInPkts = _JnxIkeTunInPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 22, 1, 2, 1, 1, 23),
    _JnxIkeTunInPkts_Type()
)
jnxIkeTunInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeTunInPkts.setStatus("current")
if mibBuilder.loadTexts:
    jnxIkeTunInPkts.setUnits("Packets")
_JnxIkeTunOutOctets_Type = Counter64
_JnxIkeTunOutOctets_Object = MibTableColumn
jnxIkeTunOutOctets = _JnxIkeTunOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 22, 1, 2, 1, 1, 24),
    _JnxIkeTunOutOctets_Type()
)
jnxIkeTunOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeTunOutOctets.setStatus("current")
if mibBuilder.loadTexts:
    jnxIkeTunOutOctets.setUnits("Octets")
_JnxIkeTunOutPkts_Type = Counter32
_JnxIkeTunOutPkts_Object = MibTableColumn
jnxIkeTunOutPkts = _JnxIkeTunOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 22, 1, 2, 1, 1, 25),
    _JnxIkeTunOutPkts_Type()
)
jnxIkeTunOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeTunOutPkts.setStatus("current")
if mibBuilder.loadTexts:
    jnxIkeTunOutPkts.setUnits("Packets")
_JnxIpSecPhaseTwo_ObjectIdentity = ObjectIdentity
jnxIpSecPhaseTwo = _JnxIpSecPhaseTwo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 22, 1, 3)
)
_JnxIpSecTunnelTable_Object = MibTable
jnxIpSecTunnelTable = _JnxIpSecTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 22, 1, 3, 1)
)
if mibBuilder.loadTexts:
    jnxIpSecTunnelTable.setStatus("current")
_JnxIpSecTunnelEntry_Object = MibTableRow
jnxIpSecTunnelEntry = _JnxIpSecTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 22, 1, 3, 1, 1)
)
jnxIpSecTunnelEntry.setIndexNames(
    (0, "JUNIPER-SP-MIB", "jnxSpSvcSetName"),
    (0, "JNX-IPSEC-MONITOR-MIB", "jnxIpSecTunRemoteGwAddrType"),
    (0, "JNX-IPSEC-MONITOR-MIB", "jnxIpSecTunRemoteGwAddr"),
    (0, "JNX-IPSEC-MONITOR-MIB", "jnxIpSecTunIndex"),
)
if mibBuilder.loadTexts:
    jnxIpSecTunnelEntry.setStatus("current")


class _JnxIpSecTunIndex_Type(Integer32):
    """Custom type jnxIpSecTunIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_JnxIpSecTunIndex_Type.__name__ = "Integer32"
_JnxIpSecTunIndex_Object = MibTableColumn
jnxIpSecTunIndex = _JnxIpSecTunIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 22, 1, 3, 1, 1, 1),
    _JnxIpSecTunIndex_Type()
)
jnxIpSecTunIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxIpSecTunIndex.setStatus("current")
_JnxIpSecRuleName_Type = DisplayString
_JnxIpSecRuleName_Object = MibTableColumn
jnxIpSecRuleName = _JnxIpSecRuleName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 22, 1, 3, 1, 1, 2),
    _JnxIpSecRuleName_Type()
)
jnxIpSecRuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecRuleName.setStatus("current")
_JnxIpSecTermName_Type = DisplayString
_JnxIpSecTermName_Object = MibTableColumn
jnxIpSecTermName = _JnxIpSecTermName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 22, 1, 3, 1, 1, 3),
    _JnxIpSecTermName_Type()
)
jnxIpSecTermName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecTermName.setStatus("current")
_JnxIpSecTunLocalGwAddrType_Type = InetAddressType
_JnxIpSecTunLocalGwAddrType_Object = MibTableColumn
jnxIpSecTunLocalGwAddrType = _JnxIpSecTunLocalGwAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 22, 1, 3, 1, 1, 4),
    _JnxIpSecTunLocalGwAddrType_Type()
)
jnxIpSecTunLocalGwAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecTunLocalGwAddrType.setStatus("current")
_JnxIpSecTunLocalGwAddr_Type = InetAddress
_JnxIpSecTunLocalGwAddr_Object = MibTableColumn
jnxIpSecTunLocalGwAddr = _JnxIpSecTunLocalGwAddr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 22, 1, 3, 1, 1, 5),
    _JnxIpSecTunLocalGwAddr_Type()
)
jnxIpSecTunLocalGwAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecTunLocalGwAddr.setStatus("current")
_JnxIpSecTunRemoteGwAddrType_Type = InetAddressType
_JnxIpSecTunRemoteGwAddrType_Object = MibTableColumn
jnxIpSecTunRemoteGwAddrType = _JnxIpSecTunRemoteGwAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 22, 1, 3, 1, 1, 6),
    _JnxIpSecTunRemoteGwAddrType_Type()
)
jnxIpSecTunRemoteGwAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecTunRemoteGwAddrType.setStatus("current")
_JnxIpSecTunRemoteGwAddr_Type = InetAddress
_JnxIpSecTunRemoteGwAddr_Object = MibTableColumn
jnxIpSecTunRemoteGwAddr = _JnxIpSecTunRemoteGwAddr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 22, 1, 3, 1, 1, 7),
    _JnxIpSecTunRemoteGwAddr_Type()
)
jnxIpSecTunRemoteGwAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecTunRemoteGwAddr.setStatus("current")
_JnxIpSecTunLocalProxyId_Type = DisplayString
_JnxIpSecTunLocalProxyId_Object = MibTableColumn
jnxIpSecTunLocalProxyId = _JnxIpSecTunLocalProxyId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 22, 1, 3, 1, 1, 8),
    _JnxIpSecTunLocalProxyId_Type()
)
jnxIpSecTunLocalProxyId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecTunLocalProxyId.setStatus("current")
_JnxIpSecTunRemoteProxyId_Type = DisplayString
_JnxIpSecTunRemoteProxyId_Object = MibTableColumn
jnxIpSecTunRemoteProxyId = _JnxIpSecTunRemoteProxyId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 22, 1, 3, 1, 1, 9),
    _JnxIpSecTunRemoteProxyId_Type()
)
jnxIpSecTunRemoteProxyId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecTunRemoteProxyId.setStatus("current")
_JnxIpSecTunKeyType_Type = JnxKeyType
_JnxIpSecTunKeyType_Object = MibTableColumn
jnxIpSecTunKeyType = _JnxIpSecTunKeyType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 22, 1, 3, 1, 1, 10),
    _JnxIpSecTunKeyType_Type()
)
jnxIpSecTunKeyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecTunKeyType.setStatus("current")
_JnxIpSecRemotePeerType_Type = JnxRemotePeerType
_JnxIpSecRemotePeerType_Object = MibTableColumn
jnxIpSecRemotePeerType = _JnxIpSecRemotePeerType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 22, 1, 3, 1, 1, 11),
    _JnxIpSecRemotePeerType_Type()
)
jnxIpSecRemotePeerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecRemotePeerType.setStatus("current")
_JnxIpSecTunMtu_Type = Integer32
_JnxIpSecTunMtu_Object = MibTableColumn
jnxIpSecTunMtu = _JnxIpSecTunMtu_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 22, 1, 3, 1, 1, 12),
    _JnxIpSecTunMtu_Type()
)
jnxIpSecTunMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecTunMtu.setStatus("current")
_JnxIpSecTunOutEncryptedBytes_Type = Counter64
_JnxIpSecTunOutEncryptedBytes_Object = MibTableColumn
jnxIpSecTunOutEncryptedBytes = _JnxIpSecTunOutEncryptedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 22, 1, 3, 1, 1, 13),
    _JnxIpSecTunOutEncryptedBytes_Type()
)
jnxIpSecTunOutEncryptedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecTunOutEncryptedBytes.setStatus("current")
_JnxIpSecTunOutEncryptedPkts_Type = Counter64
_JnxIpSecTunOutEncryptedPkts_Object = MibTableColumn
jnxIpSecTunOutEncryptedPkts = _JnxIpSecTunOutEncryptedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 22, 1, 3, 1, 1, 14),
    _JnxIpSecTunOutEncryptedPkts_Type()
)
jnxIpSecTunOutEncryptedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecTunOutEncryptedPkts.setStatus("current")
_JnxIpSecTunInDecryptedBytes_Type = Counter64
_JnxIpSecTunInDecryptedBytes_Object = MibTableColumn
jnxIpSecTunInDecryptedBytes = _JnxIpSecTunInDecryptedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 22, 1, 3, 1, 1, 15),
    _JnxIpSecTunInDecryptedBytes_Type()
)
jnxIpSecTunInDecryptedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecTunInDecryptedBytes.setStatus("current")
_JnxIpSecTunInDecryptedPkts_Type = Counter64
_JnxIpSecTunInDecryptedPkts_Object = MibTableColumn
jnxIpSecTunInDecryptedPkts = _JnxIpSecTunInDecryptedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 22, 1, 3, 1, 1, 16),
    _JnxIpSecTunInDecryptedPkts_Type()
)
jnxIpSecTunInDecryptedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecTunInDecryptedPkts.setStatus("current")
_JnxIpsSecTunAHInBytes_Type = Counter64
_JnxIpsSecTunAHInBytes_Object = MibTableColumn
jnxIpsSecTunAHInBytes = _JnxIpsSecTunAHInBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 22, 1, 3, 1, 1, 17),
    _JnxIpsSecTunAHInBytes_Type()
)
jnxIpsSecTunAHInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpsSecTunAHInBytes.setStatus("current")
_JnxIpsSecTunAHInPkts_Type = Counter64
_JnxIpsSecTunAHInPkts_Object = MibTableColumn
jnxIpsSecTunAHInPkts = _JnxIpsSecTunAHInPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 22, 1, 3, 1, 1, 18),
    _JnxIpsSecTunAHInPkts_Type()
)
jnxIpsSecTunAHInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpsSecTunAHInPkts.setStatus("current")
_JnxIpsSecTunAHOutBytes_Type = Counter64
_JnxIpsSecTunAHOutBytes_Object = MibTableColumn
jnxIpsSecTunAHOutBytes = _JnxIpsSecTunAHOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 22, 1, 3, 1, 1, 19),
    _JnxIpsSecTunAHOutBytes_Type()
)
jnxIpsSecTunAHOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpsSecTunAHOutBytes.setStatus("current")
_JnxIpsSecTunAHOutPkts_Type = Counter64
_JnxIpsSecTunAHOutPkts_Object = MibTableColumn
jnxIpsSecTunAHOutPkts = _JnxIpsSecTunAHOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 22, 1, 3, 1, 1, 20),
    _JnxIpsSecTunAHOutPkts_Type()
)
jnxIpsSecTunAHOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpsSecTunAHOutPkts.setStatus("current")
_JnxIpSecTunReplayDropPkts_Type = Counter64
_JnxIpSecTunReplayDropPkts_Object = MibTableColumn
jnxIpSecTunReplayDropPkts = _JnxIpSecTunReplayDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 22, 1, 3, 1, 1, 21),
    _JnxIpSecTunReplayDropPkts_Type()
)
jnxIpSecTunReplayDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecTunReplayDropPkts.setStatus("current")
_JnxIpSecTunAhAuthFails_Type = Counter64
_JnxIpSecTunAhAuthFails_Object = MibTableColumn
jnxIpSecTunAhAuthFails = _JnxIpSecTunAhAuthFails_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 22, 1, 3, 1, 1, 22),
    _JnxIpSecTunAhAuthFails_Type()
)
jnxIpSecTunAhAuthFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecTunAhAuthFails.setStatus("current")
_JnxIpSecTunEspAuthFails_Type = Counter64
_JnxIpSecTunEspAuthFails_Object = MibTableColumn
jnxIpSecTunEspAuthFails = _JnxIpSecTunEspAuthFails_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 22, 1, 3, 1, 1, 23),
    _JnxIpSecTunEspAuthFails_Type()
)
jnxIpSecTunEspAuthFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecTunEspAuthFails.setStatus("current")
_JnxIpSecTunDecryptFails_Type = Counter64
_JnxIpSecTunDecryptFails_Object = MibTableColumn
jnxIpSecTunDecryptFails = _JnxIpSecTunDecryptFails_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 22, 1, 3, 1, 1, 24),
    _JnxIpSecTunDecryptFails_Type()
)
jnxIpSecTunDecryptFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecTunDecryptFails.setStatus("current")
_JnxIpSecTunBadHeaders_Type = Counter64
_JnxIpSecTunBadHeaders_Object = MibTableColumn
jnxIpSecTunBadHeaders = _JnxIpSecTunBadHeaders_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 22, 1, 3, 1, 1, 25),
    _JnxIpSecTunBadHeaders_Type()
)
jnxIpSecTunBadHeaders.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecTunBadHeaders.setStatus("current")
_JnxIpSecTunBadTrailers_Type = Counter64
_JnxIpSecTunBadTrailers_Object = MibTableColumn
jnxIpSecTunBadTrailers = _JnxIpSecTunBadTrailers_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 22, 1, 3, 1, 1, 26),
    _JnxIpSecTunBadTrailers_Type()
)
jnxIpSecTunBadTrailers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecTunBadTrailers.setStatus("current")
_JnxIpSecTunDroppedPkts_Type = Counter64
_JnxIpSecTunDroppedPkts_Object = MibTableColumn
jnxIpSecTunDroppedPkts = _JnxIpSecTunDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 22, 1, 3, 1, 1, 27),
    _JnxIpSecTunDroppedPkts_Type()
)
jnxIpSecTunDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecTunDroppedPkts.setStatus("current")
_JnxIpSecSaTable_Object = MibTable
jnxIpSecSaTable = _JnxIpSecSaTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 22, 1, 3, 2)
)
if mibBuilder.loadTexts:
    jnxIpSecSaTable.setStatus("current")
_JnxIpSecSaEntry_Object = MibTableRow
jnxIpSecSaEntry = _JnxIpSecSaEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 22, 1, 3, 2, 1)
)
jnxIpSecSaEntry.setIndexNames(
    (0, "JUNIPER-SP-MIB", "jnxSpSvcSetName"),
    (0, "JNX-IPSEC-MONITOR-MIB", "jnxIpSecTunRemoteGwAddrType"),
    (0, "JNX-IPSEC-MONITOR-MIB", "jnxIpSecTunRemoteGwAddr"),
    (0, "JNX-IPSEC-MONITOR-MIB", "jnxIpSecTunIndex"),
    (0, "JNX-IPSEC-MONITOR-MIB", "jnxIpSecSaIndex"),
)
if mibBuilder.loadTexts:
    jnxIpSecSaEntry.setStatus("current")


class _JnxIpSecSaProtocol_Type(Integer32):
    """Custom type jnxIpSecSaProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ah", 1),
          ("esp", 2))
    )


_JnxIpSecSaProtocol_Type.__name__ = "Integer32"
_JnxIpSecSaProtocol_Object = MibTableColumn
jnxIpSecSaProtocol = _JnxIpSecSaProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 22, 1, 3, 2, 1, 1),
    _JnxIpSecSaProtocol_Type()
)
jnxIpSecSaProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxIpSecSaProtocol.setStatus("current")


class _JnxIpSecSaIndex_Type(Integer32):
    """Custom type jnxIpSecSaIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_JnxIpSecSaIndex_Type.__name__ = "Integer32"
_JnxIpSecSaIndex_Object = MibTableColumn
jnxIpSecSaIndex = _JnxIpSecSaIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 22, 1, 3, 2, 1, 2),
    _JnxIpSecSaIndex_Type()
)
jnxIpSecSaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxIpSecSaIndex.setStatus("current")
_JnxIpSecSaInSpi_Type = JnxSpi
_JnxIpSecSaInSpi_Object = MibTableColumn
jnxIpSecSaInSpi = _JnxIpSecSaInSpi_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 22, 1, 3, 2, 1, 3),
    _JnxIpSecSaInSpi_Type()
)
jnxIpSecSaInSpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecSaInSpi.setStatus("current")
_JnxIpSecSaOutSpi_Type = JnxSpi
_JnxIpSecSaOutSpi_Object = MibTableColumn
jnxIpSecSaOutSpi = _JnxIpSecSaOutSpi_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 22, 1, 3, 2, 1, 4),
    _JnxIpSecSaOutSpi_Type()
)
jnxIpSecSaOutSpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecSaOutSpi.setStatus("current")
_JnxIpSecSaInAuxSpi_Type = JnxSpi
_JnxIpSecSaInAuxSpi_Object = MibTableColumn
jnxIpSecSaInAuxSpi = _JnxIpSecSaInAuxSpi_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 22, 1, 3, 2, 1, 5),
    _JnxIpSecSaInAuxSpi_Type()
)
jnxIpSecSaInAuxSpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecSaInAuxSpi.setStatus("current")
_JnxIpSecSaOutAuxSpi_Type = JnxSpi
_JnxIpSecSaOutAuxSpi_Object = MibTableColumn
jnxIpSecSaOutAuxSpi = _JnxIpSecSaOutAuxSpi_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 22, 1, 3, 2, 1, 6),
    _JnxIpSecSaOutAuxSpi_Type()
)
jnxIpSecSaOutAuxSpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecSaOutAuxSpi.setStatus("current")
_JnxIpSecSaType_Type = JnxSAType
_JnxIpSecSaType_Object = MibTableColumn
jnxIpSecSaType = _JnxIpSecSaType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 22, 1, 3, 2, 1, 7),
    _JnxIpSecSaType_Type()
)
jnxIpSecSaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecSaType.setStatus("current")
_JnxIpSecSaEncapMode_Type = JnxEncapMode
_JnxIpSecSaEncapMode_Object = MibTableColumn
jnxIpSecSaEncapMode = _JnxIpSecSaEncapMode_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 22, 1, 3, 2, 1, 8),
    _JnxIpSecSaEncapMode_Type()
)
jnxIpSecSaEncapMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecSaEncapMode.setStatus("current")
_JnxIpSecSaLifeSize_Type = Integer32
_JnxIpSecSaLifeSize_Object = MibTableColumn
jnxIpSecSaLifeSize = _JnxIpSecSaLifeSize_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 22, 1, 3, 2, 1, 9),
    _JnxIpSecSaLifeSize_Type()
)
jnxIpSecSaLifeSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecSaLifeSize.setStatus("current")
_JnxIpSecSaLifeTime_Type = Integer32
_JnxIpSecSaLifeTime_Object = MibTableColumn
jnxIpSecSaLifeTime = _JnxIpSecSaLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 22, 1, 3, 2, 1, 10),
    _JnxIpSecSaLifeTime_Type()
)
jnxIpSecSaLifeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecSaLifeTime.setStatus("current")
_JnxIpSecSaActiveTime_Type = TimeInterval
_JnxIpSecSaActiveTime_Object = MibTableColumn
jnxIpSecSaActiveTime = _JnxIpSecSaActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 22, 1, 3, 2, 1, 11),
    _JnxIpSecSaActiveTime_Type()
)
jnxIpSecSaActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecSaActiveTime.setStatus("current")
_JnxIpSecSaLifeSizeThreshold_Type = Integer32
_JnxIpSecSaLifeSizeThreshold_Object = MibTableColumn
jnxIpSecSaLifeSizeThreshold = _JnxIpSecSaLifeSizeThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 22, 1, 3, 2, 1, 12),
    _JnxIpSecSaLifeSizeThreshold_Type()
)
jnxIpSecSaLifeSizeThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecSaLifeSizeThreshold.setStatus("current")
_JnxIpSecSaLifeTimeThreshold_Type = Integer32
_JnxIpSecSaLifeTimeThreshold_Object = MibTableColumn
jnxIpSecSaLifeTimeThreshold = _JnxIpSecSaLifeTimeThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 22, 1, 3, 2, 1, 13),
    _JnxIpSecSaLifeTimeThreshold_Type()
)
jnxIpSecSaLifeTimeThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecSaLifeTimeThreshold.setStatus("current")
_JnxIpSecSaEncryptAlgo_Type = JnxEncryptAlgo
_JnxIpSecSaEncryptAlgo_Object = MibTableColumn
jnxIpSecSaEncryptAlgo = _JnxIpSecSaEncryptAlgo_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 22, 1, 3, 2, 1, 14),
    _JnxIpSecSaEncryptAlgo_Type()
)
jnxIpSecSaEncryptAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecSaEncryptAlgo.setStatus("current")
_JnxIpSecSaAuthAlgo_Type = JnxAuthAlgo
_JnxIpSecSaAuthAlgo_Object = MibTableColumn
jnxIpSecSaAuthAlgo = _JnxIpSecSaAuthAlgo_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 22, 1, 3, 2, 1, 15),
    _JnxIpSecSaAuthAlgo_Type()
)
jnxIpSecSaAuthAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecSaAuthAlgo.setStatus("current")


class _JnxIpSecSaState_Type(Integer32):
    """Custom type jnxIpSecSaState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("expiring", 2),
          ("unknown", 0))
    )


_JnxIpSecSaState_Type.__name__ = "Integer32"
_JnxIpSecSaState_Object = MibTableColumn
jnxIpSecSaState = _JnxIpSecSaState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 22, 1, 3, 2, 1, 16),
    _JnxIpSecSaState_Type()
)
jnxIpSecSaState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecSaState.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JNX-IPSEC-MONITOR-MIB",
    **{"JnxIkePeerType": JnxIkePeerType,
       "JnxIkeNegoMode": JnxIkeNegoMode,
       "JnxIkeHashAlgo": JnxIkeHashAlgo,
       "JnxIkeAuthMethod": JnxIkeAuthMethod,
       "JnxIkePeerRole": JnxIkePeerRole,
       "JnxIkeNegState": JnxIkeNegState,
       "JnxDiffHellmanGrp": JnxDiffHellmanGrp,
       "JnxKeyType": JnxKeyType,
       "JnxEncapMode": JnxEncapMode,
       "JnxEncryptAlgo": JnxEncryptAlgo,
       "JnxSpi": JnxSpi,
       "JnxAuthAlgo": JnxAuthAlgo,
       "JnxRemotePeerType": JnxRemotePeerType,
       "JnxSAType": JnxSAType,
       "jnxIpSecMonitorMIB": jnxIpSecMonitorMIB,
       "jnxIpSecMIBObjects": jnxIpSecMIBObjects,
       "jnxIpSecLevels": jnxIpSecLevels,
       "jnxIpSecMibLevel": jnxIpSecMibLevel,
       "jnxIpSecPhaseOne": jnxIpSecPhaseOne,
       "jnxIkeTunnelTable": jnxIkeTunnelTable,
       "jnxIkeTunnelEntry": jnxIkeTunnelEntry,
       "jnxIkeTunIndex": jnxIkeTunIndex,
       "jnxIkeTunLocalRole": jnxIkeTunLocalRole,
       "jnxIkeTunNegState": jnxIkeTunNegState,
       "jnxIkeTunInitiatorCookie": jnxIkeTunInitiatorCookie,
       "jnxIkeTunResponderCookie": jnxIkeTunResponderCookie,
       "jnxIkeTunLocalIdType": jnxIkeTunLocalIdType,
       "jnxIkeTunLocalIdValue": jnxIkeTunLocalIdValue,
       "jnxIkeTunLocalGwAddrType": jnxIkeTunLocalGwAddrType,
       "jnxIkeTunLocalGwAddr": jnxIkeTunLocalGwAddr,
       "jnxIkeTunLocalCertName": jnxIkeTunLocalCertName,
       "jnxIkeTunRemoteIdType": jnxIkeTunRemoteIdType,
       "jnxIkeTunRemoteIdValue": jnxIkeTunRemoteIdValue,
       "jnxIkeTunRemoteGwAddrType": jnxIkeTunRemoteGwAddrType,
       "jnxIkeTunRemoteGwAddr": jnxIkeTunRemoteGwAddr,
       "jnxIkeTunNegoMode": jnxIkeTunNegoMode,
       "jnxIkeTunDiffHellmanGrp": jnxIkeTunDiffHellmanGrp,
       "jnxIkeTunEncryptAlgo": jnxIkeTunEncryptAlgo,
       "jnxIkeTunHashAlgo": jnxIkeTunHashAlgo,
       "jnxIkeTunAuthMethod": jnxIkeTunAuthMethod,
       "jnxIkeTunLifeTime": jnxIkeTunLifeTime,
       "jnxIkeTunActiveTime": jnxIkeTunActiveTime,
       "jnxIkeTunInOctets": jnxIkeTunInOctets,
       "jnxIkeTunInPkts": jnxIkeTunInPkts,
       "jnxIkeTunOutOctets": jnxIkeTunOutOctets,
       "jnxIkeTunOutPkts": jnxIkeTunOutPkts,
       "jnxIpSecPhaseTwo": jnxIpSecPhaseTwo,
       "jnxIpSecTunnelTable": jnxIpSecTunnelTable,
       "jnxIpSecTunnelEntry": jnxIpSecTunnelEntry,
       "jnxIpSecTunIndex": jnxIpSecTunIndex,
       "jnxIpSecRuleName": jnxIpSecRuleName,
       "jnxIpSecTermName": jnxIpSecTermName,
       "jnxIpSecTunLocalGwAddrType": jnxIpSecTunLocalGwAddrType,
       "jnxIpSecTunLocalGwAddr": jnxIpSecTunLocalGwAddr,
       "jnxIpSecTunRemoteGwAddrType": jnxIpSecTunRemoteGwAddrType,
       "jnxIpSecTunRemoteGwAddr": jnxIpSecTunRemoteGwAddr,
       "jnxIpSecTunLocalProxyId": jnxIpSecTunLocalProxyId,
       "jnxIpSecTunRemoteProxyId": jnxIpSecTunRemoteProxyId,
       "jnxIpSecTunKeyType": jnxIpSecTunKeyType,
       "jnxIpSecRemotePeerType": jnxIpSecRemotePeerType,
       "jnxIpSecTunMtu": jnxIpSecTunMtu,
       "jnxIpSecTunOutEncryptedBytes": jnxIpSecTunOutEncryptedBytes,
       "jnxIpSecTunOutEncryptedPkts": jnxIpSecTunOutEncryptedPkts,
       "jnxIpSecTunInDecryptedBytes": jnxIpSecTunInDecryptedBytes,
       "jnxIpSecTunInDecryptedPkts": jnxIpSecTunInDecryptedPkts,
       "jnxIpsSecTunAHInBytes": jnxIpsSecTunAHInBytes,
       "jnxIpsSecTunAHInPkts": jnxIpsSecTunAHInPkts,
       "jnxIpsSecTunAHOutBytes": jnxIpsSecTunAHOutBytes,
       "jnxIpsSecTunAHOutPkts": jnxIpsSecTunAHOutPkts,
       "jnxIpSecTunReplayDropPkts": jnxIpSecTunReplayDropPkts,
       "jnxIpSecTunAhAuthFails": jnxIpSecTunAhAuthFails,
       "jnxIpSecTunEspAuthFails": jnxIpSecTunEspAuthFails,
       "jnxIpSecTunDecryptFails": jnxIpSecTunDecryptFails,
       "jnxIpSecTunBadHeaders": jnxIpSecTunBadHeaders,
       "jnxIpSecTunBadTrailers": jnxIpSecTunBadTrailers,
       "jnxIpSecTunDroppedPkts": jnxIpSecTunDroppedPkts,
       "jnxIpSecSaTable": jnxIpSecSaTable,
       "jnxIpSecSaEntry": jnxIpSecSaEntry,
       "jnxIpSecSaProtocol": jnxIpSecSaProtocol,
       "jnxIpSecSaIndex": jnxIpSecSaIndex,
       "jnxIpSecSaInSpi": jnxIpSecSaInSpi,
       "jnxIpSecSaOutSpi": jnxIpSecSaOutSpi,
       "jnxIpSecSaInAuxSpi": jnxIpSecSaInAuxSpi,
       "jnxIpSecSaOutAuxSpi": jnxIpSecSaOutAuxSpi,
       "jnxIpSecSaType": jnxIpSecSaType,
       "jnxIpSecSaEncapMode": jnxIpSecSaEncapMode,
       "jnxIpSecSaLifeSize": jnxIpSecSaLifeSize,
       "jnxIpSecSaLifeTime": jnxIpSecSaLifeTime,
       "jnxIpSecSaActiveTime": jnxIpSecSaActiveTime,
       "jnxIpSecSaLifeSizeThreshold": jnxIpSecSaLifeSizeThreshold,
       "jnxIpSecSaLifeTimeThreshold": jnxIpSecSaLifeTimeThreshold,
       "jnxIpSecSaEncryptAlgo": jnxIpSecSaEncryptAlgo,
       "jnxIpSecSaAuthAlgo": jnxIpSecSaAuthAlgo,
       "jnxIpSecSaState": jnxIpSecSaState}
)
