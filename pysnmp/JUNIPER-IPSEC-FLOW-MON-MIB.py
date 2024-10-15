# SNMP MIB module (JUNIPER-IPSEC-FLOW-MON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/JUNIPER-IPSEC-FLOW-MON-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:13:10 2024
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

(jnxIpSecMibRoot,) = mibBuilder.importSymbols(
    "JUNIPER-SMI",
    "jnxIpSecMibRoot")

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

jnxIpSecFlowMonMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1)
)
jnxIpSecFlowMonMIB.setRevisions(
        ("2007-05-16 00:00",)
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
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("idDn", 3),
          ("idFqdn", 2),
          ("idIpv4Addr", 1),
          ("idUfqdn", 4),
          ("unknown", 0))
    )



class JnxIkeNegoMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aggressive", 2),
          ("main", 1))
    )



class JnxIkeHashAlgo(Integer32, TextualConvention):
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
        *(("md5", 1),
          ("sha", 2),
          ("sha256", 3))
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
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("dssSignature", 2),
          ("preSharedKey", 1),
          ("revRsaEncryption", 5),
          ("rsaEncryption", 4),
          ("rsaSignature", 3),
          ("xauthDssSignature", 7),
          ("xauthPreSharedKey", 6),
          ("xauthRevRsaEncryption", 10),
          ("xauthRsaEncryption", 9),
          ("xauthRsaSignature", 8))
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



class JnxIkeTunStateType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )



class JnxDiffHellmanGrp(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              5)
        )
    )
    namedValues = NamedValues(
        *(("modp1024", 2),
          ("modp1536", 5),
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



class JnxAuthAlgo(Integer32, TextualConvention):
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
        *(("hmacMd5", 1),
          ("hmacSha", 2),
          ("hmacSha256", 3),
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



class JnxSpiType(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 4294967295),
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

_JnxIpSecFlowMonNotifications_ObjectIdentity = ObjectIdentity
jnxIpSecFlowMonNotifications = _JnxIpSecFlowMonNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 0)
)
_JnxIpSecFlowMonPhaseOne_ObjectIdentity = ObjectIdentity
jnxIpSecFlowMonPhaseOne = _JnxIpSecFlowMonPhaseOne_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1)
)
_JnxIkeNumOfTunnels_Type = Integer32
_JnxIkeNumOfTunnels_Object = MibScalar
jnxIkeNumOfTunnels = _JnxIkeNumOfTunnels_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 1),
    _JnxIkeNumOfTunnels_Type()
)
jnxIkeNumOfTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeNumOfTunnels.setStatus("current")
_JnxIkeTunnelMonTable_Object = MibTable
jnxIkeTunnelMonTable = _JnxIkeTunnelMonTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 2)
)
if mibBuilder.loadTexts:
    jnxIkeTunnelMonTable.setStatus("current")
_JnxIkeTunnelMonEntry_Object = MibTableRow
jnxIkeTunnelMonEntry = _JnxIkeTunnelMonEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 2, 1)
)
jnxIkeTunnelMonEntry.setIndexNames(
    (0, "JUNIPER-IPSEC-FLOW-MON-MIB", "jnxIkeTunMonRemoteGwAddrType"),
    (0, "JUNIPER-IPSEC-FLOW-MON-MIB", "jnxIkeTunMonRemoteGwAddr"),
    (0, "JUNIPER-IPSEC-FLOW-MON-MIB", "jnxIkeTunMonIndex"),
)
if mibBuilder.loadTexts:
    jnxIkeTunnelMonEntry.setStatus("current")
_JnxIkeTunMonRemoteGwAddrType_Type = InetAddressType
_JnxIkeTunMonRemoteGwAddrType_Object = MibTableColumn
jnxIkeTunMonRemoteGwAddrType = _JnxIkeTunMonRemoteGwAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 2, 1, 1),
    _JnxIkeTunMonRemoteGwAddrType_Type()
)
jnxIkeTunMonRemoteGwAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxIkeTunMonRemoteGwAddrType.setStatus("current")
_JnxIkeTunMonRemoteGwAddr_Type = InetAddress
_JnxIkeTunMonRemoteGwAddr_Object = MibTableColumn
jnxIkeTunMonRemoteGwAddr = _JnxIkeTunMonRemoteGwAddr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 2, 1, 2),
    _JnxIkeTunMonRemoteGwAddr_Type()
)
jnxIkeTunMonRemoteGwAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxIkeTunMonRemoteGwAddr.setStatus("current")


class _JnxIkeTunMonIndex_Type(Integer32):
    """Custom type jnxIkeTunMonIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_JnxIkeTunMonIndex_Type.__name__ = "Integer32"
_JnxIkeTunMonIndex_Object = MibTableColumn
jnxIkeTunMonIndex = _JnxIkeTunMonIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 2, 1, 3),
    _JnxIkeTunMonIndex_Type()
)
jnxIkeTunMonIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxIkeTunMonIndex.setStatus("current")
_JnxIkeTunMonLocalGwAddr_Type = InetAddress
_JnxIkeTunMonLocalGwAddr_Object = MibTableColumn
jnxIkeTunMonLocalGwAddr = _JnxIkeTunMonLocalGwAddr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 2, 1, 4),
    _JnxIkeTunMonLocalGwAddr_Type()
)
jnxIkeTunMonLocalGwAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeTunMonLocalGwAddr.setStatus("current")
_JnxIkeTunMonLocalGwAddrType_Type = InetAddressType
_JnxIkeTunMonLocalGwAddrType_Object = MibTableColumn
jnxIkeTunMonLocalGwAddrType = _JnxIkeTunMonLocalGwAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 2, 1, 5),
    _JnxIkeTunMonLocalGwAddrType_Type()
)
jnxIkeTunMonLocalGwAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeTunMonLocalGwAddrType.setStatus("current")
_JnxIkeTunMonState_Type = JnxIkeTunStateType
_JnxIkeTunMonState_Object = MibTableColumn
jnxIkeTunMonState = _JnxIkeTunMonState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 2, 1, 6),
    _JnxIkeTunMonState_Type()
)
jnxIkeTunMonState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeTunMonState.setStatus("current")
_JnxIkeTunMonInitiatorCookie_Type = DisplayString
_JnxIkeTunMonInitiatorCookie_Object = MibTableColumn
jnxIkeTunMonInitiatorCookie = _JnxIkeTunMonInitiatorCookie_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 2, 1, 7),
    _JnxIkeTunMonInitiatorCookie_Type()
)
jnxIkeTunMonInitiatorCookie.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeTunMonInitiatorCookie.setStatus("current")
_JnxIkeTunMonResponderCookie_Type = DisplayString
_JnxIkeTunMonResponderCookie_Object = MibTableColumn
jnxIkeTunMonResponderCookie = _JnxIkeTunMonResponderCookie_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 2, 1, 8),
    _JnxIkeTunMonResponderCookie_Type()
)
jnxIkeTunMonResponderCookie.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeTunMonResponderCookie.setStatus("current")
_JnxIkeTunMonLocalRole_Type = JnxIkePeerRole
_JnxIkeTunMonLocalRole_Object = MibTableColumn
jnxIkeTunMonLocalRole = _JnxIkeTunMonLocalRole_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 2, 1, 9),
    _JnxIkeTunMonLocalRole_Type()
)
jnxIkeTunMonLocalRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeTunMonLocalRole.setStatus("current")
_JnxIkeTunMonLocalIdType_Type = JnxIkePeerType
_JnxIkeTunMonLocalIdType_Object = MibTableColumn
jnxIkeTunMonLocalIdType = _JnxIkeTunMonLocalIdType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 2, 1, 10),
    _JnxIkeTunMonLocalIdType_Type()
)
jnxIkeTunMonLocalIdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeTunMonLocalIdType.setStatus("current")
_JnxIkeTunMonLocalIdValue_Type = DisplayString
_JnxIkeTunMonLocalIdValue_Object = MibTableColumn
jnxIkeTunMonLocalIdValue = _JnxIkeTunMonLocalIdValue_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 2, 1, 11),
    _JnxIkeTunMonLocalIdValue_Type()
)
jnxIkeTunMonLocalIdValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeTunMonLocalIdValue.setStatus("current")
_JnxIkeTunMonLocalCertName_Type = DisplayString
_JnxIkeTunMonLocalCertName_Object = MibTableColumn
jnxIkeTunMonLocalCertName = _JnxIkeTunMonLocalCertName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 2, 1, 12),
    _JnxIkeTunMonLocalCertName_Type()
)
jnxIkeTunMonLocalCertName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeTunMonLocalCertName.setStatus("current")
_JnxIkeTunMonRemoteIdType_Type = JnxIkePeerType
_JnxIkeTunMonRemoteIdType_Object = MibTableColumn
jnxIkeTunMonRemoteIdType = _JnxIkeTunMonRemoteIdType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 2, 1, 13),
    _JnxIkeTunMonRemoteIdType_Type()
)
jnxIkeTunMonRemoteIdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeTunMonRemoteIdType.setStatus("current")
_JnxIkeTunMonRemoteIdValue_Type = DisplayString
_JnxIkeTunMonRemoteIdValue_Object = MibTableColumn
jnxIkeTunMonRemoteIdValue = _JnxIkeTunMonRemoteIdValue_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 2, 1, 14),
    _JnxIkeTunMonRemoteIdValue_Type()
)
jnxIkeTunMonRemoteIdValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeTunMonRemoteIdValue.setStatus("current")
_JnxIkeTunMonNegoMode_Type = JnxIkeNegoMode
_JnxIkeTunMonNegoMode_Object = MibTableColumn
jnxIkeTunMonNegoMode = _JnxIkeTunMonNegoMode_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 2, 1, 15),
    _JnxIkeTunMonNegoMode_Type()
)
jnxIkeTunMonNegoMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeTunMonNegoMode.setStatus("current")
_JnxIkeTunMonDiffHellmanGrp_Type = JnxDiffHellmanGrp
_JnxIkeTunMonDiffHellmanGrp_Object = MibTableColumn
jnxIkeTunMonDiffHellmanGrp = _JnxIkeTunMonDiffHellmanGrp_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 2, 1, 16),
    _JnxIkeTunMonDiffHellmanGrp_Type()
)
jnxIkeTunMonDiffHellmanGrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeTunMonDiffHellmanGrp.setStatus("current")
_JnxIkeTunMonEncryptAlgo_Type = JnxEncryptAlgo
_JnxIkeTunMonEncryptAlgo_Object = MibTableColumn
jnxIkeTunMonEncryptAlgo = _JnxIkeTunMonEncryptAlgo_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 2, 1, 17),
    _JnxIkeTunMonEncryptAlgo_Type()
)
jnxIkeTunMonEncryptAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeTunMonEncryptAlgo.setStatus("current")
_JnxIkeTunMonHashAlgo_Type = JnxIkeHashAlgo
_JnxIkeTunMonHashAlgo_Object = MibTableColumn
jnxIkeTunMonHashAlgo = _JnxIkeTunMonHashAlgo_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 2, 1, 18),
    _JnxIkeTunMonHashAlgo_Type()
)
jnxIkeTunMonHashAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeTunMonHashAlgo.setStatus("current")
_JnxIkeTunMonAuthMethod_Type = JnxIkeAuthMethod
_JnxIkeTunMonAuthMethod_Object = MibTableColumn
jnxIkeTunMonAuthMethod = _JnxIkeTunMonAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 2, 1, 19),
    _JnxIkeTunMonAuthMethod_Type()
)
jnxIkeTunMonAuthMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeTunMonAuthMethod.setStatus("current")


class _JnxIkeTunMonLifeTime_Type(Integer32):
    """Custom type jnxIkeTunMonLifeTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_JnxIkeTunMonLifeTime_Type.__name__ = "Integer32"
_JnxIkeTunMonLifeTime_Object = MibTableColumn
jnxIkeTunMonLifeTime = _JnxIkeTunMonLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 2, 1, 20),
    _JnxIkeTunMonLifeTime_Type()
)
jnxIkeTunMonLifeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeTunMonLifeTime.setStatus("current")
if mibBuilder.loadTexts:
    jnxIkeTunMonLifeTime.setUnits("seconds")
_JnxIkeTunMonActiveTime_Type = TimeInterval
_JnxIkeTunMonActiveTime_Object = MibTableColumn
jnxIkeTunMonActiveTime = _JnxIkeTunMonActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 2, 1, 21),
    _JnxIkeTunMonActiveTime_Type()
)
jnxIkeTunMonActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeTunMonActiveTime.setStatus("current")
_JnxIkeTunMonInOctets_Type = Counter64
_JnxIkeTunMonInOctets_Object = MibTableColumn
jnxIkeTunMonInOctets = _JnxIkeTunMonInOctets_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 2, 1, 22),
    _JnxIkeTunMonInOctets_Type()
)
jnxIkeTunMonInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeTunMonInOctets.setStatus("current")
if mibBuilder.loadTexts:
    jnxIkeTunMonInOctets.setUnits("Octets")
_JnxIkeTunMonInPkts_Type = Counter32
_JnxIkeTunMonInPkts_Object = MibTableColumn
jnxIkeTunMonInPkts = _JnxIkeTunMonInPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 2, 1, 23),
    _JnxIkeTunMonInPkts_Type()
)
jnxIkeTunMonInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeTunMonInPkts.setStatus("current")
if mibBuilder.loadTexts:
    jnxIkeTunMonInPkts.setUnits("Packets")
_JnxIkeTunMonOutOctets_Type = Counter64
_JnxIkeTunMonOutOctets_Object = MibTableColumn
jnxIkeTunMonOutOctets = _JnxIkeTunMonOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 2, 1, 24),
    _JnxIkeTunMonOutOctets_Type()
)
jnxIkeTunMonOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeTunMonOutOctets.setStatus("current")
if mibBuilder.loadTexts:
    jnxIkeTunMonOutOctets.setUnits("Octets")
_JnxIkeTunMonOutPkts_Type = Counter32
_JnxIkeTunMonOutPkts_Object = MibTableColumn
jnxIkeTunMonOutPkts = _JnxIkeTunMonOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 2, 1, 25),
    _JnxIkeTunMonOutPkts_Type()
)
jnxIkeTunMonOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeTunMonOutPkts.setStatus("current")
if mibBuilder.loadTexts:
    jnxIkeTunMonOutPkts.setUnits("Packets")
_JnxIkeTunMonXAuthUserId_Type = DisplayString
_JnxIkeTunMonXAuthUserId_Object = MibTableColumn
jnxIkeTunMonXAuthUserId = _JnxIkeTunMonXAuthUserId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 2, 1, 26),
    _JnxIkeTunMonXAuthUserId_Type()
)
jnxIkeTunMonXAuthUserId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeTunMonXAuthUserId.setStatus("current")
_JnxIkeTunMonDPDDownCount_Type = Counter32
_JnxIkeTunMonDPDDownCount_Object = MibTableColumn
jnxIkeTunMonDPDDownCount = _JnxIkeTunMonDPDDownCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 2, 1, 27),
    _JnxIkeTunMonDPDDownCount_Type()
)
jnxIkeTunMonDPDDownCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeTunMonDPDDownCount.setStatus("obsolete")
if mibBuilder.loadTexts:
    jnxIkeTunMonDPDDownCount.setUnits("Packets")
_JnxIpSecFlowMonPhaseTwo_ObjectIdentity = ObjectIdentity
jnxIpSecFlowMonPhaseTwo = _JnxIpSecFlowMonPhaseTwo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2)
)
_JnxIpSecNumOfTunnels_Type = Integer32
_JnxIpSecNumOfTunnels_Object = MibScalar
jnxIpSecNumOfTunnels = _JnxIpSecNumOfTunnels_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 1),
    _JnxIpSecNumOfTunnels_Type()
)
jnxIpSecNumOfTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecNumOfTunnels.setStatus("current")
_JnxIpSecTunnelMonTable_Object = MibTable
jnxIpSecTunnelMonTable = _JnxIpSecTunnelMonTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 2)
)
if mibBuilder.loadTexts:
    jnxIpSecTunnelMonTable.setStatus("current")
_JnxIpSecTunnelMonEntry_Object = MibTableRow
jnxIpSecTunnelMonEntry = _JnxIpSecTunnelMonEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 2, 1)
)
jnxIpSecTunnelMonEntry.setIndexNames(
    (0, "JUNIPER-IPSEC-FLOW-MON-MIB", "jnxIpSecTunMonRemoteGwAddrType"),
    (0, "JUNIPER-IPSEC-FLOW-MON-MIB", "jnxIpSecTunMonRemoteGwAddr"),
    (0, "JUNIPER-IPSEC-FLOW-MON-MIB", "jnxIpSecTunMonIndex"),
)
if mibBuilder.loadTexts:
    jnxIpSecTunnelMonEntry.setStatus("current")
_JnxIpSecTunMonRemoteGwAddrType_Type = InetAddressType
_JnxIpSecTunMonRemoteGwAddrType_Object = MibTableColumn
jnxIpSecTunMonRemoteGwAddrType = _JnxIpSecTunMonRemoteGwAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 2, 1, 1),
    _JnxIpSecTunMonRemoteGwAddrType_Type()
)
jnxIpSecTunMonRemoteGwAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxIpSecTunMonRemoteGwAddrType.setStatus("current")
_JnxIpSecTunMonRemoteGwAddr_Type = InetAddress
_JnxIpSecTunMonRemoteGwAddr_Object = MibTableColumn
jnxIpSecTunMonRemoteGwAddr = _JnxIpSecTunMonRemoteGwAddr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 2, 1, 2),
    _JnxIpSecTunMonRemoteGwAddr_Type()
)
jnxIpSecTunMonRemoteGwAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxIpSecTunMonRemoteGwAddr.setStatus("current")


class _JnxIpSecTunMonIndex_Type(Integer32):
    """Custom type jnxIpSecTunMonIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_JnxIpSecTunMonIndex_Type.__name__ = "Integer32"
_JnxIpSecTunMonIndex_Object = MibTableColumn
jnxIpSecTunMonIndex = _JnxIpSecTunMonIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 2, 1, 3),
    _JnxIpSecTunMonIndex_Type()
)
jnxIpSecTunMonIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxIpSecTunMonIndex.setStatus("current")
_JnxIpSecTunMonLocalGwAddrType_Type = InetAddressType
_JnxIpSecTunMonLocalGwAddrType_Object = MibTableColumn
jnxIpSecTunMonLocalGwAddrType = _JnxIpSecTunMonLocalGwAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 2, 1, 4),
    _JnxIpSecTunMonLocalGwAddrType_Type()
)
jnxIpSecTunMonLocalGwAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecTunMonLocalGwAddrType.setStatus("current")
_JnxIpSecTunMonLocalGwAddr_Type = InetAddress
_JnxIpSecTunMonLocalGwAddr_Object = MibTableColumn
jnxIpSecTunMonLocalGwAddr = _JnxIpSecTunMonLocalGwAddr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 2, 1, 5),
    _JnxIpSecTunMonLocalGwAddr_Type()
)
jnxIpSecTunMonLocalGwAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecTunMonLocalGwAddr.setStatus("current")
_JnxIpSecTunMonLocalProxyId_Type = DisplayString
_JnxIpSecTunMonLocalProxyId_Object = MibTableColumn
jnxIpSecTunMonLocalProxyId = _JnxIpSecTunMonLocalProxyId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 2, 1, 6),
    _JnxIpSecTunMonLocalProxyId_Type()
)
jnxIpSecTunMonLocalProxyId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecTunMonLocalProxyId.setStatus("current")
_JnxIpSecTunMonRemoteProxyId_Type = DisplayString
_JnxIpSecTunMonRemoteProxyId_Object = MibTableColumn
jnxIpSecTunMonRemoteProxyId = _JnxIpSecTunMonRemoteProxyId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 2, 1, 7),
    _JnxIpSecTunMonRemoteProxyId_Type()
)
jnxIpSecTunMonRemoteProxyId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecTunMonRemoteProxyId.setStatus("current")
_JnxIpSecTunMonKeyType_Type = JnxKeyType
_JnxIpSecTunMonKeyType_Object = MibTableColumn
jnxIpSecTunMonKeyType = _JnxIpSecTunMonKeyType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 2, 1, 8),
    _JnxIpSecTunMonKeyType_Type()
)
jnxIpSecTunMonKeyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecTunMonKeyType.setStatus("current")
_JnxIpSecTunMonRemotePeerType_Type = JnxRemotePeerType
_JnxIpSecTunMonRemotePeerType_Object = MibTableColumn
jnxIpSecTunMonRemotePeerType = _JnxIpSecTunMonRemotePeerType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 2, 1, 9),
    _JnxIpSecTunMonRemotePeerType_Type()
)
jnxIpSecTunMonRemotePeerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecTunMonRemotePeerType.setStatus("current")
_JnxIpSecTunMonOutEncryptedBytes_Type = Counter64
_JnxIpSecTunMonOutEncryptedBytes_Object = MibTableColumn
jnxIpSecTunMonOutEncryptedBytes = _JnxIpSecTunMonOutEncryptedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 2, 1, 10),
    _JnxIpSecTunMonOutEncryptedBytes_Type()
)
jnxIpSecTunMonOutEncryptedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecTunMonOutEncryptedBytes.setStatus("current")
_JnxIpSecTunMonOutEncryptedPkts_Type = Counter64
_JnxIpSecTunMonOutEncryptedPkts_Object = MibTableColumn
jnxIpSecTunMonOutEncryptedPkts = _JnxIpSecTunMonOutEncryptedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 2, 1, 11),
    _JnxIpSecTunMonOutEncryptedPkts_Type()
)
jnxIpSecTunMonOutEncryptedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecTunMonOutEncryptedPkts.setStatus("current")
_JnxIpSecTunMonInDecryptedBytes_Type = Counter64
_JnxIpSecTunMonInDecryptedBytes_Object = MibTableColumn
jnxIpSecTunMonInDecryptedBytes = _JnxIpSecTunMonInDecryptedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 2, 1, 12),
    _JnxIpSecTunMonInDecryptedBytes_Type()
)
jnxIpSecTunMonInDecryptedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecTunMonInDecryptedBytes.setStatus("current")
_JnxIpSecTunMonInDecryptedPkts_Type = Counter64
_JnxIpSecTunMonInDecryptedPkts_Object = MibTableColumn
jnxIpSecTunMonInDecryptedPkts = _JnxIpSecTunMonInDecryptedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 2, 1, 13),
    _JnxIpSecTunMonInDecryptedPkts_Type()
)
jnxIpSecTunMonInDecryptedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecTunMonInDecryptedPkts.setStatus("current")
_JnxIpSecTunMonAHInBytes_Type = Counter64
_JnxIpSecTunMonAHInBytes_Object = MibTableColumn
jnxIpSecTunMonAHInBytes = _JnxIpSecTunMonAHInBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 2, 1, 14),
    _JnxIpSecTunMonAHInBytes_Type()
)
jnxIpSecTunMonAHInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecTunMonAHInBytes.setStatus("current")
_JnxIpSecTunMonAHInPkts_Type = Counter64
_JnxIpSecTunMonAHInPkts_Object = MibTableColumn
jnxIpSecTunMonAHInPkts = _JnxIpSecTunMonAHInPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 2, 1, 15),
    _JnxIpSecTunMonAHInPkts_Type()
)
jnxIpSecTunMonAHInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecTunMonAHInPkts.setStatus("current")
_JnxIpSecTunMonAHOutBytes_Type = Counter64
_JnxIpSecTunMonAHOutBytes_Object = MibTableColumn
jnxIpSecTunMonAHOutBytes = _JnxIpSecTunMonAHOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 2, 1, 16),
    _JnxIpSecTunMonAHOutBytes_Type()
)
jnxIpSecTunMonAHOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecTunMonAHOutBytes.setStatus("current")
_JnxIpSecTunMonAHOutPkts_Type = Counter64
_JnxIpSecTunMonAHOutPkts_Object = MibTableColumn
jnxIpSecTunMonAHOutPkts = _JnxIpSecTunMonAHOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 2, 1, 17),
    _JnxIpSecTunMonAHOutPkts_Type()
)
jnxIpSecTunMonAHOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecTunMonAHOutPkts.setStatus("current")
_JnxIpSecTunMonReplayDropPkts_Type = Counter64
_JnxIpSecTunMonReplayDropPkts_Object = MibTableColumn
jnxIpSecTunMonReplayDropPkts = _JnxIpSecTunMonReplayDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 2, 1, 18),
    _JnxIpSecTunMonReplayDropPkts_Type()
)
jnxIpSecTunMonReplayDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecTunMonReplayDropPkts.setStatus("current")
_JnxIpSecTunMonAhAuthFails_Type = Counter64
_JnxIpSecTunMonAhAuthFails_Object = MibTableColumn
jnxIpSecTunMonAhAuthFails = _JnxIpSecTunMonAhAuthFails_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 2, 1, 19),
    _JnxIpSecTunMonAhAuthFails_Type()
)
jnxIpSecTunMonAhAuthFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecTunMonAhAuthFails.setStatus("current")
_JnxIpSecTunMonEspAuthFails_Type = Counter64
_JnxIpSecTunMonEspAuthFails_Object = MibTableColumn
jnxIpSecTunMonEspAuthFails = _JnxIpSecTunMonEspAuthFails_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 2, 1, 20),
    _JnxIpSecTunMonEspAuthFails_Type()
)
jnxIpSecTunMonEspAuthFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecTunMonEspAuthFails.setStatus("current")
_JnxIpSecTunMonDecryptFails_Type = Counter64
_JnxIpSecTunMonDecryptFails_Object = MibTableColumn
jnxIpSecTunMonDecryptFails = _JnxIpSecTunMonDecryptFails_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 2, 1, 21),
    _JnxIpSecTunMonDecryptFails_Type()
)
jnxIpSecTunMonDecryptFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecTunMonDecryptFails.setStatus("current")
_JnxIpSecTunMonBadHeaders_Type = Counter64
_JnxIpSecTunMonBadHeaders_Object = MibTableColumn
jnxIpSecTunMonBadHeaders = _JnxIpSecTunMonBadHeaders_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 2, 1, 22),
    _JnxIpSecTunMonBadHeaders_Type()
)
jnxIpSecTunMonBadHeaders.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecTunMonBadHeaders.setStatus("current")
_JnxIpSecTunMonBadTrailers_Type = Counter64
_JnxIpSecTunMonBadTrailers_Object = MibTableColumn
jnxIpSecTunMonBadTrailers = _JnxIpSecTunMonBadTrailers_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 2, 1, 23),
    _JnxIpSecTunMonBadTrailers_Type()
)
jnxIpSecTunMonBadTrailers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecTunMonBadTrailers.setStatus("current")
_JnxIpSecTunMonDroppedPkts_Type = Counter64
_JnxIpSecTunMonDroppedPkts_Object = MibTableColumn
jnxIpSecTunMonDroppedPkts = _JnxIpSecTunMonDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 2, 1, 26),
    _JnxIpSecTunMonDroppedPkts_Type()
)
jnxIpSecTunMonDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecTunMonDroppedPkts.setStatus("obsolete")
_JnxIpSecSaMonTable_Object = MibTable
jnxIpSecSaMonTable = _JnxIpSecSaMonTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 3)
)
if mibBuilder.loadTexts:
    jnxIpSecSaMonTable.setStatus("current")
_JnxIpSecSaMonEntry_Object = MibTableRow
jnxIpSecSaMonEntry = _JnxIpSecSaMonEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 3, 1)
)
jnxIpSecSaMonEntry.setIndexNames(
    (0, "JUNIPER-IPSEC-FLOW-MON-MIB", "jnxIpSecTunMonRemoteGwAddrType"),
    (0, "JUNIPER-IPSEC-FLOW-MON-MIB", "jnxIpSecTunMonRemoteGwAddr"),
    (0, "JUNIPER-IPSEC-FLOW-MON-MIB", "jnxIpSecTunMonIndex"),
    (0, "JUNIPER-IPSEC-FLOW-MON-MIB", "jnxIpSecSaMonIndex"),
)
if mibBuilder.loadTexts:
    jnxIpSecSaMonEntry.setStatus("current")


class _JnxIpSecSaMonIndex_Type(Integer32):
    """Custom type jnxIpSecSaMonIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_JnxIpSecSaMonIndex_Type.__name__ = "Integer32"
_JnxIpSecSaMonIndex_Object = MibTableColumn
jnxIpSecSaMonIndex = _JnxIpSecSaMonIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 3, 1, 1),
    _JnxIpSecSaMonIndex_Type()
)
jnxIpSecSaMonIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxIpSecSaMonIndex.setStatus("current")


class _JnxIpSecSaMonProtocol_Type(Integer32):
    """Custom type jnxIpSecSaMonProtocol based on Integer32"""
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


_JnxIpSecSaMonProtocol_Type.__name__ = "Integer32"
_JnxIpSecSaMonProtocol_Object = MibTableColumn
jnxIpSecSaMonProtocol = _JnxIpSecSaMonProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 3, 1, 2),
    _JnxIpSecSaMonProtocol_Type()
)
jnxIpSecSaMonProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecSaMonProtocol.setStatus("current")
_JnxIpSecSaMonInSpi_Type = JnxSpiType
_JnxIpSecSaMonInSpi_Object = MibTableColumn
jnxIpSecSaMonInSpi = _JnxIpSecSaMonInSpi_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 3, 1, 3),
    _JnxIpSecSaMonInSpi_Type()
)
jnxIpSecSaMonInSpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecSaMonInSpi.setStatus("current")
_JnxIpSecSaMonOutSpi_Type = JnxSpiType
_JnxIpSecSaMonOutSpi_Object = MibTableColumn
jnxIpSecSaMonOutSpi = _JnxIpSecSaMonOutSpi_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 3, 1, 4),
    _JnxIpSecSaMonOutSpi_Type()
)
jnxIpSecSaMonOutSpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecSaMonOutSpi.setStatus("current")
_JnxIpSecSaMonType_Type = JnxSAType
_JnxIpSecSaMonType_Object = MibTableColumn
jnxIpSecSaMonType = _JnxIpSecSaMonType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 3, 1, 5),
    _JnxIpSecSaMonType_Type()
)
jnxIpSecSaMonType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecSaMonType.setStatus("current")
_JnxIpSecSaMonEncapMode_Type = JnxEncapMode
_JnxIpSecSaMonEncapMode_Object = MibTableColumn
jnxIpSecSaMonEncapMode = _JnxIpSecSaMonEncapMode_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 3, 1, 6),
    _JnxIpSecSaMonEncapMode_Type()
)
jnxIpSecSaMonEncapMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecSaMonEncapMode.setStatus("current")
_JnxIpSecSaMonLifeSize_Type = Integer32
_JnxIpSecSaMonLifeSize_Object = MibTableColumn
jnxIpSecSaMonLifeSize = _JnxIpSecSaMonLifeSize_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 3, 1, 7),
    _JnxIpSecSaMonLifeSize_Type()
)
jnxIpSecSaMonLifeSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecSaMonLifeSize.setStatus("current")
_JnxIpSecSaMonLifeTime_Type = Integer32
_JnxIpSecSaMonLifeTime_Object = MibTableColumn
jnxIpSecSaMonLifeTime = _JnxIpSecSaMonLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 3, 1, 8),
    _JnxIpSecSaMonLifeTime_Type()
)
jnxIpSecSaMonLifeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecSaMonLifeTime.setStatus("current")
_JnxIpSecSaMonActiveTime_Type = TimeInterval
_JnxIpSecSaMonActiveTime_Object = MibTableColumn
jnxIpSecSaMonActiveTime = _JnxIpSecSaMonActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 3, 1, 9),
    _JnxIpSecSaMonActiveTime_Type()
)
jnxIpSecSaMonActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecSaMonActiveTime.setStatus("current")
_JnxIpSecSaMonLifeSizeThreshold_Type = Integer32
_JnxIpSecSaMonLifeSizeThreshold_Object = MibTableColumn
jnxIpSecSaMonLifeSizeThreshold = _JnxIpSecSaMonLifeSizeThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 3, 1, 10),
    _JnxIpSecSaMonLifeSizeThreshold_Type()
)
jnxIpSecSaMonLifeSizeThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecSaMonLifeSizeThreshold.setStatus("current")
_JnxIpSecSaMonLifeTimeThreshold_Type = Integer32
_JnxIpSecSaMonLifeTimeThreshold_Object = MibTableColumn
jnxIpSecSaMonLifeTimeThreshold = _JnxIpSecSaMonLifeTimeThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 3, 1, 11),
    _JnxIpSecSaMonLifeTimeThreshold_Type()
)
jnxIpSecSaMonLifeTimeThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecSaMonLifeTimeThreshold.setStatus("current")
_JnxIpSecSaMonEncryptAlgo_Type = JnxEncryptAlgo
_JnxIpSecSaMonEncryptAlgo_Object = MibTableColumn
jnxIpSecSaMonEncryptAlgo = _JnxIpSecSaMonEncryptAlgo_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 3, 1, 12),
    _JnxIpSecSaMonEncryptAlgo_Type()
)
jnxIpSecSaMonEncryptAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecSaMonEncryptAlgo.setStatus("current")
_JnxIpSecSaMonAuthAlgo_Type = JnxAuthAlgo
_JnxIpSecSaMonAuthAlgo_Object = MibTableColumn
jnxIpSecSaMonAuthAlgo = _JnxIpSecSaMonAuthAlgo_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 3, 1, 13),
    _JnxIpSecSaMonAuthAlgo_Type()
)
jnxIpSecSaMonAuthAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecSaMonAuthAlgo.setStatus("current")


class _JnxIpSecSaMonState_Type(Integer32):
    """Custom type jnxIpSecSaMonState based on Integer32"""
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


_JnxIpSecSaMonState_Type.__name__ = "Integer32"
_JnxIpSecSaMonState_Object = MibTableColumn
jnxIpSecSaMonState = _JnxIpSecSaMonState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 3, 1, 14),
    _JnxIpSecSaMonState_Type()
)
jnxIpSecSaMonState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecSaMonState.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-IPSEC-FLOW-MON-MIB",
    **{"JnxIkePeerType": JnxIkePeerType,
       "JnxIkeNegoMode": JnxIkeNegoMode,
       "JnxIkeHashAlgo": JnxIkeHashAlgo,
       "JnxIkeAuthMethod": JnxIkeAuthMethod,
       "JnxIkePeerRole": JnxIkePeerRole,
       "JnxIkeTunStateType": JnxIkeTunStateType,
       "JnxDiffHellmanGrp": JnxDiffHellmanGrp,
       "JnxKeyType": JnxKeyType,
       "JnxEncapMode": JnxEncapMode,
       "JnxEncryptAlgo": JnxEncryptAlgo,
       "JnxAuthAlgo": JnxAuthAlgo,
       "JnxRemotePeerType": JnxRemotePeerType,
       "JnxSpiType": JnxSpiType,
       "JnxSAType": JnxSAType,
       "jnxIpSecFlowMonMIB": jnxIpSecFlowMonMIB,
       "jnxIpSecFlowMonNotifications": jnxIpSecFlowMonNotifications,
       "jnxIpSecFlowMonPhaseOne": jnxIpSecFlowMonPhaseOne,
       "jnxIkeNumOfTunnels": jnxIkeNumOfTunnels,
       "jnxIkeTunnelMonTable": jnxIkeTunnelMonTable,
       "jnxIkeTunnelMonEntry": jnxIkeTunnelMonEntry,
       "jnxIkeTunMonRemoteGwAddrType": jnxIkeTunMonRemoteGwAddrType,
       "jnxIkeTunMonRemoteGwAddr": jnxIkeTunMonRemoteGwAddr,
       "jnxIkeTunMonIndex": jnxIkeTunMonIndex,
       "jnxIkeTunMonLocalGwAddr": jnxIkeTunMonLocalGwAddr,
       "jnxIkeTunMonLocalGwAddrType": jnxIkeTunMonLocalGwAddrType,
       "jnxIkeTunMonState": jnxIkeTunMonState,
       "jnxIkeTunMonInitiatorCookie": jnxIkeTunMonInitiatorCookie,
       "jnxIkeTunMonResponderCookie": jnxIkeTunMonResponderCookie,
       "jnxIkeTunMonLocalRole": jnxIkeTunMonLocalRole,
       "jnxIkeTunMonLocalIdType": jnxIkeTunMonLocalIdType,
       "jnxIkeTunMonLocalIdValue": jnxIkeTunMonLocalIdValue,
       "jnxIkeTunMonLocalCertName": jnxIkeTunMonLocalCertName,
       "jnxIkeTunMonRemoteIdType": jnxIkeTunMonRemoteIdType,
       "jnxIkeTunMonRemoteIdValue": jnxIkeTunMonRemoteIdValue,
       "jnxIkeTunMonNegoMode": jnxIkeTunMonNegoMode,
       "jnxIkeTunMonDiffHellmanGrp": jnxIkeTunMonDiffHellmanGrp,
       "jnxIkeTunMonEncryptAlgo": jnxIkeTunMonEncryptAlgo,
       "jnxIkeTunMonHashAlgo": jnxIkeTunMonHashAlgo,
       "jnxIkeTunMonAuthMethod": jnxIkeTunMonAuthMethod,
       "jnxIkeTunMonLifeTime": jnxIkeTunMonLifeTime,
       "jnxIkeTunMonActiveTime": jnxIkeTunMonActiveTime,
       "jnxIkeTunMonInOctets": jnxIkeTunMonInOctets,
       "jnxIkeTunMonInPkts": jnxIkeTunMonInPkts,
       "jnxIkeTunMonOutOctets": jnxIkeTunMonOutOctets,
       "jnxIkeTunMonOutPkts": jnxIkeTunMonOutPkts,
       "jnxIkeTunMonXAuthUserId": jnxIkeTunMonXAuthUserId,
       "jnxIkeTunMonDPDDownCount": jnxIkeTunMonDPDDownCount,
       "jnxIpSecFlowMonPhaseTwo": jnxIpSecFlowMonPhaseTwo,
       "jnxIpSecNumOfTunnels": jnxIpSecNumOfTunnels,
       "jnxIpSecTunnelMonTable": jnxIpSecTunnelMonTable,
       "jnxIpSecTunnelMonEntry": jnxIpSecTunnelMonEntry,
       "jnxIpSecTunMonRemoteGwAddrType": jnxIpSecTunMonRemoteGwAddrType,
       "jnxIpSecTunMonRemoteGwAddr": jnxIpSecTunMonRemoteGwAddr,
       "jnxIpSecTunMonIndex": jnxIpSecTunMonIndex,
       "jnxIpSecTunMonLocalGwAddrType": jnxIpSecTunMonLocalGwAddrType,
       "jnxIpSecTunMonLocalGwAddr": jnxIpSecTunMonLocalGwAddr,
       "jnxIpSecTunMonLocalProxyId": jnxIpSecTunMonLocalProxyId,
       "jnxIpSecTunMonRemoteProxyId": jnxIpSecTunMonRemoteProxyId,
       "jnxIpSecTunMonKeyType": jnxIpSecTunMonKeyType,
       "jnxIpSecTunMonRemotePeerType": jnxIpSecTunMonRemotePeerType,
       "jnxIpSecTunMonOutEncryptedBytes": jnxIpSecTunMonOutEncryptedBytes,
       "jnxIpSecTunMonOutEncryptedPkts": jnxIpSecTunMonOutEncryptedPkts,
       "jnxIpSecTunMonInDecryptedBytes": jnxIpSecTunMonInDecryptedBytes,
       "jnxIpSecTunMonInDecryptedPkts": jnxIpSecTunMonInDecryptedPkts,
       "jnxIpSecTunMonAHInBytes": jnxIpSecTunMonAHInBytes,
       "jnxIpSecTunMonAHInPkts": jnxIpSecTunMonAHInPkts,
       "jnxIpSecTunMonAHOutBytes": jnxIpSecTunMonAHOutBytes,
       "jnxIpSecTunMonAHOutPkts": jnxIpSecTunMonAHOutPkts,
       "jnxIpSecTunMonReplayDropPkts": jnxIpSecTunMonReplayDropPkts,
       "jnxIpSecTunMonAhAuthFails": jnxIpSecTunMonAhAuthFails,
       "jnxIpSecTunMonEspAuthFails": jnxIpSecTunMonEspAuthFails,
       "jnxIpSecTunMonDecryptFails": jnxIpSecTunMonDecryptFails,
       "jnxIpSecTunMonBadHeaders": jnxIpSecTunMonBadHeaders,
       "jnxIpSecTunMonBadTrailers": jnxIpSecTunMonBadTrailers,
       "jnxIpSecTunMonDroppedPkts": jnxIpSecTunMonDroppedPkts,
       "jnxIpSecSaMonTable": jnxIpSecSaMonTable,
       "jnxIpSecSaMonEntry": jnxIpSecSaMonEntry,
       "jnxIpSecSaMonIndex": jnxIpSecSaMonIndex,
       "jnxIpSecSaMonProtocol": jnxIpSecSaMonProtocol,
       "jnxIpSecSaMonInSpi": jnxIpSecSaMonInSpi,
       "jnxIpSecSaMonOutSpi": jnxIpSecSaMonOutSpi,
       "jnxIpSecSaMonType": jnxIpSecSaMonType,
       "jnxIpSecSaMonEncapMode": jnxIpSecSaMonEncapMode,
       "jnxIpSecSaMonLifeSize": jnxIpSecSaMonLifeSize,
       "jnxIpSecSaMonLifeTime": jnxIpSecSaMonLifeTime,
       "jnxIpSecSaMonActiveTime": jnxIpSecSaMonActiveTime,
       "jnxIpSecSaMonLifeSizeThreshold": jnxIpSecSaMonLifeSizeThreshold,
       "jnxIpSecSaMonLifeTimeThreshold": jnxIpSecSaMonLifeTimeThreshold,
       "jnxIpSecSaMonEncryptAlgo": jnxIpSecSaMonEncryptAlgo,
       "jnxIpSecSaMonAuthAlgo": jnxIpSecSaMonAuthAlgo,
       "jnxIpSecSaMonState": jnxIpSecSaMonState}
)
