# SNMP MIB module (IPsecT1-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IPsecT1-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:11:38 2024
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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ipsecMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class IPSIpAddress(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )



class IkePeerType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipAddrPeer", 1),
          ("namePeer", 2))
    )



class IkeNegoMode(Integer32, TextualConvention):
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



class IkeHashAlgo(Integer32, TextualConvention):
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
        *(("md5", 2),
          ("none", 1),
          ("sha", 3))
    )



class IkeAuthMethod(Integer32, TextualConvention):
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
        *(("none", 1),
          ("preSharedKey", 2),
          ("revPublicKey", 5),
          ("rsaEncrypt", 4),
          ("rsaSig", 3))
    )



class DiffHellmanGrp(Integer32, TextualConvention):
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
        *(("dhGroup1", 2),
          ("dhGroup2", 3),
          ("none", 1))
    )



class KeyType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ike", 1),
          ("manual", 2))
    )



class EncapMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("transport", 2),
          ("tunnel", 1))
    )



class EncryptAlgo(Integer32, TextualConvention):
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
        *(("des", 2),
          ("des3", 3),
          ("none", 1))
    )



class AuthAlgo(Integer32, TextualConvention):
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
        *(("hmacMd5", 2),
          ("hmacSha", 3),
          ("none", 1))
    )



class CompAlgo(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ldf", 2),
          ("none", 1))
    )



class EndPtType(Integer32, TextualConvention):
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
        *(("ipAddrRange", 2),
          ("ipSubnet", 3),
          ("singleIpAddr", 1))
    )



class TunnelStatus(Integer32, TextualConvention):
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
          ("destroy", 2))
    )



class TrapStatus(Integer32, TextualConvention):
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



# MIB Managed Objects in the order of their OIDs

_IpsecMIBNotifications_ObjectIdentity = ObjectIdentity
ipsecMIBNotifications = _IpsecMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 0)
)
_IpsecMIBObjects_ObjectIdentity = ObjectIdentity
ipsecMIBObjects = _IpsecMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1)
)
_IpsecLevels_ObjectIdentity = ObjectIdentity
ipsecLevels = _IpsecLevels_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 1)
)
_IpsecMibLevel_Type = Integer32
_IpsecMibLevel_Object = MibScalar
ipsecMibLevel = _IpsecMibLevel_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 1, 1),
    _IpsecMibLevel_Type()
)
ipsecMibLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecMibLevel.setStatus("current")
_IpsecPhaseOne_ObjectIdentity = ObjectIdentity
ipsecPhaseOne = _IpsecPhaseOne_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 2)
)
_IkeGlobalStats_ObjectIdentity = ObjectIdentity
ikeGlobalStats = _IkeGlobalStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 2, 1)
)
_IkeGlobalActiveTunnels_Type = Gauge32
_IkeGlobalActiveTunnels_Object = MibScalar
ikeGlobalActiveTunnels = _IkeGlobalActiveTunnels_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 2, 1, 1),
    _IkeGlobalActiveTunnels_Type()
)
ikeGlobalActiveTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeGlobalActiveTunnels.setStatus("current")
_IkeGlobalPreviousTunnels_Type = Counter32
_IkeGlobalPreviousTunnels_Object = MibScalar
ikeGlobalPreviousTunnels = _IkeGlobalPreviousTunnels_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 2, 1, 2),
    _IkeGlobalPreviousTunnels_Type()
)
ikeGlobalPreviousTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeGlobalPreviousTunnels.setStatus("current")
_IkeGlobalInOctets_Type = Counter32
_IkeGlobalInOctets_Object = MibScalar
ikeGlobalInOctets = _IkeGlobalInOctets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 2, 1, 3),
    _IkeGlobalInOctets_Type()
)
ikeGlobalInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeGlobalInOctets.setStatus("current")
_IkeGlobalInPkts_Type = Counter32
_IkeGlobalInPkts_Object = MibScalar
ikeGlobalInPkts = _IkeGlobalInPkts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 2, 1, 4),
    _IkeGlobalInPkts_Type()
)
ikeGlobalInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeGlobalInPkts.setStatus("current")
_IkeGlobalInDropPkts_Type = Counter32
_IkeGlobalInDropPkts_Object = MibScalar
ikeGlobalInDropPkts = _IkeGlobalInDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 2, 1, 5),
    _IkeGlobalInDropPkts_Type()
)
ikeGlobalInDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeGlobalInDropPkts.setStatus("current")
_IkeGlobalInNotifys_Type = Counter32
_IkeGlobalInNotifys_Object = MibScalar
ikeGlobalInNotifys = _IkeGlobalInNotifys_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 2, 1, 6),
    _IkeGlobalInNotifys_Type()
)
ikeGlobalInNotifys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeGlobalInNotifys.setStatus("current")
_IkeGlobalInP2Exchgs_Type = Counter32
_IkeGlobalInP2Exchgs_Object = MibScalar
ikeGlobalInP2Exchgs = _IkeGlobalInP2Exchgs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 2, 1, 7),
    _IkeGlobalInP2Exchgs_Type()
)
ikeGlobalInP2Exchgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeGlobalInP2Exchgs.setStatus("current")
_IkeGlobalInP2ExchgInvalids_Type = Counter32
_IkeGlobalInP2ExchgInvalids_Object = MibScalar
ikeGlobalInP2ExchgInvalids = _IkeGlobalInP2ExchgInvalids_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 2, 1, 8),
    _IkeGlobalInP2ExchgInvalids_Type()
)
ikeGlobalInP2ExchgInvalids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeGlobalInP2ExchgInvalids.setStatus("current")
_IkeGlobalInP2ExchgRejects_Type = Counter32
_IkeGlobalInP2ExchgRejects_Object = MibScalar
ikeGlobalInP2ExchgRejects = _IkeGlobalInP2ExchgRejects_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 2, 1, 9),
    _IkeGlobalInP2ExchgRejects_Type()
)
ikeGlobalInP2ExchgRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeGlobalInP2ExchgRejects.setStatus("current")
_IkeGlobalInP2SaDelRequests_Type = Counter32
_IkeGlobalInP2SaDelRequests_Object = MibScalar
ikeGlobalInP2SaDelRequests = _IkeGlobalInP2SaDelRequests_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 2, 1, 10),
    _IkeGlobalInP2SaDelRequests_Type()
)
ikeGlobalInP2SaDelRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeGlobalInP2SaDelRequests.setStatus("current")
_IkeGlobalOutOctets_Type = Counter32
_IkeGlobalOutOctets_Object = MibScalar
ikeGlobalOutOctets = _IkeGlobalOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 2, 1, 11),
    _IkeGlobalOutOctets_Type()
)
ikeGlobalOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeGlobalOutOctets.setStatus("current")
_IkeGlobalOutPkts_Type = Counter32
_IkeGlobalOutPkts_Object = MibScalar
ikeGlobalOutPkts = _IkeGlobalOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 2, 1, 12),
    _IkeGlobalOutPkts_Type()
)
ikeGlobalOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeGlobalOutPkts.setStatus("current")
_IkeGlobalOutDropPkts_Type = Counter32
_IkeGlobalOutDropPkts_Object = MibScalar
ikeGlobalOutDropPkts = _IkeGlobalOutDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 2, 1, 13),
    _IkeGlobalOutDropPkts_Type()
)
ikeGlobalOutDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeGlobalOutDropPkts.setStatus("current")
_IkeGlobalOutNotifys_Type = Counter32
_IkeGlobalOutNotifys_Object = MibScalar
ikeGlobalOutNotifys = _IkeGlobalOutNotifys_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 2, 1, 14),
    _IkeGlobalOutNotifys_Type()
)
ikeGlobalOutNotifys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeGlobalOutNotifys.setStatus("current")
_IkeGlobalOutP2Exchgs_Type = Counter32
_IkeGlobalOutP2Exchgs_Object = MibScalar
ikeGlobalOutP2Exchgs = _IkeGlobalOutP2Exchgs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 2, 1, 15),
    _IkeGlobalOutP2Exchgs_Type()
)
ikeGlobalOutP2Exchgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeGlobalOutP2Exchgs.setStatus("current")
_IkeGlobalOutP2ExchgInvalids_Type = Counter32
_IkeGlobalOutP2ExchgInvalids_Object = MibScalar
ikeGlobalOutP2ExchgInvalids = _IkeGlobalOutP2ExchgInvalids_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 2, 1, 16),
    _IkeGlobalOutP2ExchgInvalids_Type()
)
ikeGlobalOutP2ExchgInvalids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeGlobalOutP2ExchgInvalids.setStatus("current")
_IkeGlobalOutP2ExchgRejects_Type = Counter32
_IkeGlobalOutP2ExchgRejects_Object = MibScalar
ikeGlobalOutP2ExchgRejects = _IkeGlobalOutP2ExchgRejects_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 2, 1, 17),
    _IkeGlobalOutP2ExchgRejects_Type()
)
ikeGlobalOutP2ExchgRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeGlobalOutP2ExchgRejects.setStatus("current")
_IkeGlobalOutP2SaDelRequests_Type = Counter32
_IkeGlobalOutP2SaDelRequests_Object = MibScalar
ikeGlobalOutP2SaDelRequests = _IkeGlobalOutP2SaDelRequests_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 2, 1, 18),
    _IkeGlobalOutP2SaDelRequests_Type()
)
ikeGlobalOutP2SaDelRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeGlobalOutP2SaDelRequests.setStatus("current")
_IkeGlobalInitTunnels_Type = Counter32
_IkeGlobalInitTunnels_Object = MibScalar
ikeGlobalInitTunnels = _IkeGlobalInitTunnels_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 2, 1, 19),
    _IkeGlobalInitTunnels_Type()
)
ikeGlobalInitTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeGlobalInitTunnels.setStatus("current")
_IkeGlobalInitTunnelFails_Type = Counter32
_IkeGlobalInitTunnelFails_Object = MibScalar
ikeGlobalInitTunnelFails = _IkeGlobalInitTunnelFails_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 2, 1, 20),
    _IkeGlobalInitTunnelFails_Type()
)
ikeGlobalInitTunnelFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeGlobalInitTunnelFails.setStatus("current")
_IkeGlobalRespTunnelFails_Type = Counter32
_IkeGlobalRespTunnelFails_Object = MibScalar
ikeGlobalRespTunnelFails = _IkeGlobalRespTunnelFails_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 2, 1, 21),
    _IkeGlobalRespTunnelFails_Type()
)
ikeGlobalRespTunnelFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeGlobalRespTunnelFails.setStatus("current")
_IkeGlobalSysCapFails_Type = Counter32
_IkeGlobalSysCapFails_Object = MibScalar
ikeGlobalSysCapFails = _IkeGlobalSysCapFails_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 2, 1, 22),
    _IkeGlobalSysCapFails_Type()
)
ikeGlobalSysCapFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeGlobalSysCapFails.setStatus("current")
_IkeGlobalAuthFails_Type = Counter32
_IkeGlobalAuthFails_Object = MibScalar
ikeGlobalAuthFails = _IkeGlobalAuthFails_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 2, 1, 23),
    _IkeGlobalAuthFails_Type()
)
ikeGlobalAuthFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeGlobalAuthFails.setStatus("current")
_IkeGlobalDecryptFails_Type = Counter32
_IkeGlobalDecryptFails_Object = MibScalar
ikeGlobalDecryptFails = _IkeGlobalDecryptFails_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 2, 1, 24),
    _IkeGlobalDecryptFails_Type()
)
ikeGlobalDecryptFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeGlobalDecryptFails.setStatus("current")
_IkeGlobalHashValidFails_Type = Counter32
_IkeGlobalHashValidFails_Object = MibScalar
ikeGlobalHashValidFails = _IkeGlobalHashValidFails_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 2, 1, 25),
    _IkeGlobalHashValidFails_Type()
)
ikeGlobalHashValidFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeGlobalHashValidFails.setStatus("current")
_IkeGlobalNoSaFails_Type = Counter32
_IkeGlobalNoSaFails_Object = MibScalar
ikeGlobalNoSaFails = _IkeGlobalNoSaFails_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 2, 1, 26),
    _IkeGlobalNoSaFails_Type()
)
ikeGlobalNoSaFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeGlobalNoSaFails.setStatus("current")
_IpsecGlobalProtocolUseFails_Type = Counter32
_IpsecGlobalProtocolUseFails_Object = MibScalar
ipsecGlobalProtocolUseFails = _IpsecGlobalProtocolUseFails_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 2, 1, 28),
    _IpsecGlobalProtocolUseFails_Type()
)
ipsecGlobalProtocolUseFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecGlobalProtocolUseFails.setStatus("current")
_IpsecGlobalNoSaFails_Type = Counter32
_IpsecGlobalNoSaFails_Object = MibScalar
ipsecGlobalNoSaFails = _IpsecGlobalNoSaFails_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 2, 1, 29),
    _IpsecGlobalNoSaFails_Type()
)
ipsecGlobalNoSaFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecGlobalNoSaFails.setStatus("current")
_IpsecGlobalSysCapFails_Type = Counter32
_IpsecGlobalSysCapFails_Object = MibScalar
ipsecGlobalSysCapFails = _IpsecGlobalSysCapFails_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 2, 1, 30),
    _IpsecGlobalSysCapFails_Type()
)
ipsecGlobalSysCapFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecGlobalSysCapFails.setStatus("current")
_IkePeerTable_Object = MibTable
ikePeerTable = _IkePeerTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    ikePeerTable.setStatus("current")
_IkePeerEntry_Object = MibTableRow
ikePeerEntry = _IkePeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 2, 2, 1)
)
ikePeerEntry.setIndexNames(
    (0, "IPsecT1-MIB", "ikePeerLocalType"),
    (0, "IPsecT1-MIB", "ikePeerLocalValue"),
    (0, "IPsecT1-MIB", "ikePeerRemoteType"),
    (0, "IPsecT1-MIB", "ikePeerRemoteValue"),
    (0, "IPsecT1-MIB", "ikePeerIntIndex"),
)
if mibBuilder.loadTexts:
    ikePeerEntry.setStatus("current")
_IkePeerLocalType_Type = IkePeerType
_IkePeerLocalType_Object = MibTableColumn
ikePeerLocalType = _IkePeerLocalType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 2, 2, 1, 1),
    _IkePeerLocalType_Type()
)
ikePeerLocalType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ikePeerLocalType.setStatus("current")
_IkePeerLocalValue_Type = DisplayString
_IkePeerLocalValue_Object = MibTableColumn
ikePeerLocalValue = _IkePeerLocalValue_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 2, 2, 1, 2),
    _IkePeerLocalValue_Type()
)
ikePeerLocalValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ikePeerLocalValue.setStatus("current")
_IkePeerRemoteType_Type = IkePeerType
_IkePeerRemoteType_Object = MibTableColumn
ikePeerRemoteType = _IkePeerRemoteType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 2, 2, 1, 3),
    _IkePeerRemoteType_Type()
)
ikePeerRemoteType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ikePeerRemoteType.setStatus("current")
_IkePeerRemoteValue_Type = DisplayString
_IkePeerRemoteValue_Object = MibTableColumn
ikePeerRemoteValue = _IkePeerRemoteValue_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 2, 2, 1, 4),
    _IkePeerRemoteValue_Type()
)
ikePeerRemoteValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ikePeerRemoteValue.setStatus("current")
_IkePeerIntIndex_Type = Integer32
_IkePeerIntIndex_Object = MibTableColumn
ikePeerIntIndex = _IkePeerIntIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 2, 2, 1, 5),
    _IkePeerIntIndex_Type()
)
ikePeerIntIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ikePeerIntIndex.setStatus("current")
_IkePeerLocalAddr_Type = IPSIpAddress
_IkePeerLocalAddr_Object = MibTableColumn
ikePeerLocalAddr = _IkePeerLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 2, 2, 1, 6),
    _IkePeerLocalAddr_Type()
)
ikePeerLocalAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikePeerLocalAddr.setStatus("current")
_IkePeerRemoteAddr_Type = IPSIpAddress
_IkePeerRemoteAddr_Object = MibTableColumn
ikePeerRemoteAddr = _IkePeerRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 2, 2, 1, 7),
    _IkePeerRemoteAddr_Type()
)
ikePeerRemoteAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikePeerRemoteAddr.setStatus("current")
_IkePeerActiveTime_Type = TimeInterval
_IkePeerActiveTime_Object = MibTableColumn
ikePeerActiveTime = _IkePeerActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 2, 2, 1, 8),
    _IkePeerActiveTime_Type()
)
ikePeerActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikePeerActiveTime.setStatus("current")
_IkePeerActiveTunnelIndex_Type = Integer32
_IkePeerActiveTunnelIndex_Object = MibTableColumn
ikePeerActiveTunnelIndex = _IkePeerActiveTunnelIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 2, 2, 1, 9),
    _IkePeerActiveTunnelIndex_Type()
)
ikePeerActiveTunnelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikePeerActiveTunnelIndex.setStatus("current")
_IkeTunnelTable_Object = MibTable
ikeTunnelTable = _IkeTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 2, 3)
)
if mibBuilder.loadTexts:
    ikeTunnelTable.setStatus("current")
_IkeTunnelEntry_Object = MibTableRow
ikeTunnelEntry = _IkeTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 2, 3, 1)
)
ikeTunnelEntry.setIndexNames(
    (0, "IPsecT1-MIB", "ikeTunIndex"),
)
if mibBuilder.loadTexts:
    ikeTunnelEntry.setStatus("current")
_IkeTunIndex_Type = Integer32
_IkeTunIndex_Object = MibTableColumn
ikeTunIndex = _IkeTunIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 2, 3, 1, 1),
    _IkeTunIndex_Type()
)
ikeTunIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ikeTunIndex.setStatus("current")
_IkeTunLocalType_Type = IkePeerType
_IkeTunLocalType_Object = MibTableColumn
ikeTunLocalType = _IkeTunLocalType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 2, 3, 1, 2),
    _IkeTunLocalType_Type()
)
ikeTunLocalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeTunLocalType.setStatus("current")
_IkeTunLocalValue_Type = DisplayString
_IkeTunLocalValue_Object = MibTableColumn
ikeTunLocalValue = _IkeTunLocalValue_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 2, 3, 1, 3),
    _IkeTunLocalValue_Type()
)
ikeTunLocalValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeTunLocalValue.setStatus("current")
_IkeTunLocalAddr_Type = IPSIpAddress
_IkeTunLocalAddr_Object = MibTableColumn
ikeTunLocalAddr = _IkeTunLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 2, 3, 1, 4),
    _IkeTunLocalAddr_Type()
)
ikeTunLocalAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeTunLocalAddr.setStatus("current")
_IkeTunLocalName_Type = DisplayString
_IkeTunLocalName_Object = MibTableColumn
ikeTunLocalName = _IkeTunLocalName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 2, 3, 1, 5),
    _IkeTunLocalName_Type()
)
ikeTunLocalName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeTunLocalName.setStatus("current")
_IkeTunRemoteType_Type = IkePeerType
_IkeTunRemoteType_Object = MibTableColumn
ikeTunRemoteType = _IkeTunRemoteType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 2, 3, 1, 6),
    _IkeTunRemoteType_Type()
)
ikeTunRemoteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeTunRemoteType.setStatus("current")
_IkeTunRemoteValue_Type = DisplayString
_IkeTunRemoteValue_Object = MibTableColumn
ikeTunRemoteValue = _IkeTunRemoteValue_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 2, 3, 1, 7),
    _IkeTunRemoteValue_Type()
)
ikeTunRemoteValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeTunRemoteValue.setStatus("current")
_IkeTunRemoteAddr_Type = IPSIpAddress
_IkeTunRemoteAddr_Object = MibTableColumn
ikeTunRemoteAddr = _IkeTunRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 2, 3, 1, 8),
    _IkeTunRemoteAddr_Type()
)
ikeTunRemoteAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeTunRemoteAddr.setStatus("current")
_IkeTunRemoteName_Type = DisplayString
_IkeTunRemoteName_Object = MibTableColumn
ikeTunRemoteName = _IkeTunRemoteName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 2, 3, 1, 9),
    _IkeTunRemoteName_Type()
)
ikeTunRemoteName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeTunRemoteName.setStatus("current")
_IkeTunNegoMode_Type = IkeNegoMode
_IkeTunNegoMode_Object = MibTableColumn
ikeTunNegoMode = _IkeTunNegoMode_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 2, 3, 1, 10),
    _IkeTunNegoMode_Type()
)
ikeTunNegoMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeTunNegoMode.setStatus("current")
_IkeTunDiffHellmanGrp_Type = DiffHellmanGrp
_IkeTunDiffHellmanGrp_Object = MibTableColumn
ikeTunDiffHellmanGrp = _IkeTunDiffHellmanGrp_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 2, 3, 1, 11),
    _IkeTunDiffHellmanGrp_Type()
)
ikeTunDiffHellmanGrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeTunDiffHellmanGrp.setStatus("current")
_IkeTunEncryptAlgo_Type = EncryptAlgo
_IkeTunEncryptAlgo_Object = MibTableColumn
ikeTunEncryptAlgo = _IkeTunEncryptAlgo_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 2, 3, 1, 12),
    _IkeTunEncryptAlgo_Type()
)
ikeTunEncryptAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeTunEncryptAlgo.setStatus("current")
_IkeTunHashAlgo_Type = IkeHashAlgo
_IkeTunHashAlgo_Object = MibTableColumn
ikeTunHashAlgo = _IkeTunHashAlgo_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 2, 3, 1, 13),
    _IkeTunHashAlgo_Type()
)
ikeTunHashAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeTunHashAlgo.setStatus("current")
_IkeTunAuthMethod_Type = IkeAuthMethod
_IkeTunAuthMethod_Object = MibTableColumn
ikeTunAuthMethod = _IkeTunAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 2, 3, 1, 14),
    _IkeTunAuthMethod_Type()
)
ikeTunAuthMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeTunAuthMethod.setStatus("current")
_IkeTunLifeTime_Type = Integer32
_IkeTunLifeTime_Object = MibTableColumn
ikeTunLifeTime = _IkeTunLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 2, 3, 1, 15),
    _IkeTunLifeTime_Type()
)
ikeTunLifeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeTunLifeTime.setStatus("current")
_IkeTunActiveTime_Type = TimeInterval
_IkeTunActiveTime_Object = MibTableColumn
ikeTunActiveTime = _IkeTunActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 2, 3, 1, 16),
    _IkeTunActiveTime_Type()
)
ikeTunActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeTunActiveTime.setStatus("current")
_IkeTunSaRefreshThreshold_Type = Integer32
_IkeTunSaRefreshThreshold_Object = MibTableColumn
ikeTunSaRefreshThreshold = _IkeTunSaRefreshThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 2, 3, 1, 17),
    _IkeTunSaRefreshThreshold_Type()
)
ikeTunSaRefreshThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeTunSaRefreshThreshold.setStatus("current")
_IkeTunTotalRefreshes_Type = Counter32
_IkeTunTotalRefreshes_Object = MibTableColumn
ikeTunTotalRefreshes = _IkeTunTotalRefreshes_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 2, 3, 1, 18),
    _IkeTunTotalRefreshes_Type()
)
ikeTunTotalRefreshes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeTunTotalRefreshes.setStatus("current")
_IkeTunInOctets_Type = Counter32
_IkeTunInOctets_Object = MibTableColumn
ikeTunInOctets = _IkeTunInOctets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 2, 3, 1, 19),
    _IkeTunInOctets_Type()
)
ikeTunInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeTunInOctets.setStatus("current")
_IkeTunInPkts_Type = Counter32
_IkeTunInPkts_Object = MibTableColumn
ikeTunInPkts = _IkeTunInPkts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 2, 3, 1, 20),
    _IkeTunInPkts_Type()
)
ikeTunInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeTunInPkts.setStatus("current")
_IkeTunInDropPkts_Type = Counter32
_IkeTunInDropPkts_Object = MibTableColumn
ikeTunInDropPkts = _IkeTunInDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 2, 3, 1, 21),
    _IkeTunInDropPkts_Type()
)
ikeTunInDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeTunInDropPkts.setStatus("current")
_IkeTunInNotifys_Type = Counter32
_IkeTunInNotifys_Object = MibTableColumn
ikeTunInNotifys = _IkeTunInNotifys_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 2, 3, 1, 22),
    _IkeTunInNotifys_Type()
)
ikeTunInNotifys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeTunInNotifys.setStatus("current")
_IkeTunInP2Exchgs_Type = Counter32
_IkeTunInP2Exchgs_Object = MibTableColumn
ikeTunInP2Exchgs = _IkeTunInP2Exchgs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 2, 3, 1, 23),
    _IkeTunInP2Exchgs_Type()
)
ikeTunInP2Exchgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeTunInP2Exchgs.setStatus("current")
_IkeTunInP2ExchgInvalids_Type = Counter32
_IkeTunInP2ExchgInvalids_Object = MibTableColumn
ikeTunInP2ExchgInvalids = _IkeTunInP2ExchgInvalids_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 2, 3, 1, 24),
    _IkeTunInP2ExchgInvalids_Type()
)
ikeTunInP2ExchgInvalids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeTunInP2ExchgInvalids.setStatus("current")
_IkeTunInP2ExchgRejects_Type = Counter32
_IkeTunInP2ExchgRejects_Object = MibTableColumn
ikeTunInP2ExchgRejects = _IkeTunInP2ExchgRejects_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 2, 3, 1, 25),
    _IkeTunInP2ExchgRejects_Type()
)
ikeTunInP2ExchgRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeTunInP2ExchgRejects.setStatus("current")
_IkeTunInP2SaDelRequests_Type = Counter32
_IkeTunInP2SaDelRequests_Object = MibTableColumn
ikeTunInP2SaDelRequests = _IkeTunInP2SaDelRequests_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 2, 3, 1, 26),
    _IkeTunInP2SaDelRequests_Type()
)
ikeTunInP2SaDelRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeTunInP2SaDelRequests.setStatus("current")
_IkeTunOutOctets_Type = Counter32
_IkeTunOutOctets_Object = MibTableColumn
ikeTunOutOctets = _IkeTunOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 2, 3, 1, 27),
    _IkeTunOutOctets_Type()
)
ikeTunOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeTunOutOctets.setStatus("current")
_IkeTunOutPkts_Type = Counter32
_IkeTunOutPkts_Object = MibTableColumn
ikeTunOutPkts = _IkeTunOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 2, 3, 1, 28),
    _IkeTunOutPkts_Type()
)
ikeTunOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeTunOutPkts.setStatus("current")
_IkeTunOutDropPkts_Type = Counter32
_IkeTunOutDropPkts_Object = MibTableColumn
ikeTunOutDropPkts = _IkeTunOutDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 2, 3, 1, 29),
    _IkeTunOutDropPkts_Type()
)
ikeTunOutDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeTunOutDropPkts.setStatus("current")
_IkeTunOutNotifys_Type = Counter32
_IkeTunOutNotifys_Object = MibTableColumn
ikeTunOutNotifys = _IkeTunOutNotifys_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 2, 3, 1, 30),
    _IkeTunOutNotifys_Type()
)
ikeTunOutNotifys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeTunOutNotifys.setStatus("current")
_IkeTunOutP2Exchgs_Type = Counter32
_IkeTunOutP2Exchgs_Object = MibTableColumn
ikeTunOutP2Exchgs = _IkeTunOutP2Exchgs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 2, 3, 1, 31),
    _IkeTunOutP2Exchgs_Type()
)
ikeTunOutP2Exchgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeTunOutP2Exchgs.setStatus("current")
_IkeTunOutP2ExchgInvalids_Type = Counter32
_IkeTunOutP2ExchgInvalids_Object = MibTableColumn
ikeTunOutP2ExchgInvalids = _IkeTunOutP2ExchgInvalids_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 2, 3, 1, 32),
    _IkeTunOutP2ExchgInvalids_Type()
)
ikeTunOutP2ExchgInvalids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeTunOutP2ExchgInvalids.setStatus("current")
_IkeTunOutP2ExchgRejects_Type = Counter32
_IkeTunOutP2ExchgRejects_Object = MibTableColumn
ikeTunOutP2ExchgRejects = _IkeTunOutP2ExchgRejects_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 2, 3, 1, 33),
    _IkeTunOutP2ExchgRejects_Type()
)
ikeTunOutP2ExchgRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeTunOutP2ExchgRejects.setStatus("current")
_IkeTunOutP2SaDelRequests_Type = Counter32
_IkeTunOutP2SaDelRequests_Object = MibTableColumn
ikeTunOutP2SaDelRequests = _IkeTunOutP2SaDelRequests_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 2, 3, 1, 34),
    _IkeTunOutP2SaDelRequests_Type()
)
ikeTunOutP2SaDelRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeTunOutP2SaDelRequests.setStatus("current")
_IkeTunStatus_Type = TunnelStatus
_IkeTunStatus_Object = MibTableColumn
ikeTunStatus = _IkeTunStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 2, 3, 1, 35),
    _IkeTunStatus_Type()
)
ikeTunStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ikeTunStatus.setStatus("current")
_IkePeerCorrTable_Object = MibTable
ikePeerCorrTable = _IkePeerCorrTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 2, 4)
)
if mibBuilder.loadTexts:
    ikePeerCorrTable.setStatus("current")
_IkePeerCorrEntry_Object = MibTableRow
ikePeerCorrEntry = _IkePeerCorrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 2, 4, 1)
)
ikePeerCorrEntry.setIndexNames(
    (0, "IPsecT1-MIB", "ikePeerCorrLocalType"),
    (0, "IPsecT1-MIB", "ikePeerCorrLocalValue"),
    (0, "IPsecT1-MIB", "ikePeerCorrRemoteType"),
    (0, "IPsecT1-MIB", "ikePeerCorrRemoteValue"),
    (0, "IPsecT1-MIB", "ikePeerCorrIntIndex"),
    (0, "IPsecT1-MIB", "ikePeerCorrSeqNum"),
)
if mibBuilder.loadTexts:
    ikePeerCorrEntry.setStatus("current")
_IkePeerCorrLocalType_Type = IkePeerType
_IkePeerCorrLocalType_Object = MibTableColumn
ikePeerCorrLocalType = _IkePeerCorrLocalType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 2, 4, 1, 1),
    _IkePeerCorrLocalType_Type()
)
ikePeerCorrLocalType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ikePeerCorrLocalType.setStatus("current")
_IkePeerCorrLocalValue_Type = DisplayString
_IkePeerCorrLocalValue_Object = MibTableColumn
ikePeerCorrLocalValue = _IkePeerCorrLocalValue_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 2, 4, 1, 2),
    _IkePeerCorrLocalValue_Type()
)
ikePeerCorrLocalValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ikePeerCorrLocalValue.setStatus("current")
_IkePeerCorrRemoteType_Type = IkePeerType
_IkePeerCorrRemoteType_Object = MibTableColumn
ikePeerCorrRemoteType = _IkePeerCorrRemoteType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 2, 4, 1, 3),
    _IkePeerCorrRemoteType_Type()
)
ikePeerCorrRemoteType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ikePeerCorrRemoteType.setStatus("current")
_IkePeerCorrRemoteValue_Type = DisplayString
_IkePeerCorrRemoteValue_Object = MibTableColumn
ikePeerCorrRemoteValue = _IkePeerCorrRemoteValue_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 2, 4, 1, 4),
    _IkePeerCorrRemoteValue_Type()
)
ikePeerCorrRemoteValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ikePeerCorrRemoteValue.setStatus("current")
_IkePeerCorrIntIndex_Type = Integer32
_IkePeerCorrIntIndex_Object = MibTableColumn
ikePeerCorrIntIndex = _IkePeerCorrIntIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 2, 4, 1, 5),
    _IkePeerCorrIntIndex_Type()
)
ikePeerCorrIntIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ikePeerCorrIntIndex.setStatus("current")
_IkePeerCorrSeqNum_Type = Integer32
_IkePeerCorrSeqNum_Object = MibTableColumn
ikePeerCorrSeqNum = _IkePeerCorrSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 2, 4, 1, 6),
    _IkePeerCorrSeqNum_Type()
)
ikePeerCorrSeqNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ikePeerCorrSeqNum.setStatus("current")
_IkePeerCorripsecTunIndex_Type = Integer32
_IkePeerCorripsecTunIndex_Object = MibTableColumn
ikePeerCorripsecTunIndex = _IkePeerCorripsecTunIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 2, 4, 1, 7),
    _IkePeerCorripsecTunIndex_Type()
)
ikePeerCorripsecTunIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikePeerCorripsecTunIndex.setStatus("current")
_IpsecPhaseTwo_ObjectIdentity = ObjectIdentity
ipsecPhaseTwo = _IpsecPhaseTwo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 3)
)
_IpsecGlobalStats_ObjectIdentity = ObjectIdentity
ipsecGlobalStats = _IpsecGlobalStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 3, 1)
)
_IpsecGlobalActiveTunnels_Type = Gauge32
_IpsecGlobalActiveTunnels_Object = MibScalar
ipsecGlobalActiveTunnels = _IpsecGlobalActiveTunnels_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 3, 1, 1),
    _IpsecGlobalActiveTunnels_Type()
)
ipsecGlobalActiveTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecGlobalActiveTunnels.setStatus("current")
_IpsecGlobalPreviousTunnels_Type = Counter32
_IpsecGlobalPreviousTunnels_Object = MibScalar
ipsecGlobalPreviousTunnels = _IpsecGlobalPreviousTunnels_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 3, 1, 2),
    _IpsecGlobalPreviousTunnels_Type()
)
ipsecGlobalPreviousTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecGlobalPreviousTunnels.setStatus("current")
_IpsecGlobalInOctets_Type = Counter32
_IpsecGlobalInOctets_Object = MibScalar
ipsecGlobalInOctets = _IpsecGlobalInOctets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 3, 1, 3),
    _IpsecGlobalInOctets_Type()
)
ipsecGlobalInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecGlobalInOctets.setStatus("current")
_IpsecGlobalHcInOctets_Type = Counter64
_IpsecGlobalHcInOctets_Object = MibScalar
ipsecGlobalHcInOctets = _IpsecGlobalHcInOctets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 3, 1, 4),
    _IpsecGlobalHcInOctets_Type()
)
ipsecGlobalHcInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecGlobalHcInOctets.setStatus("current")
_IpsecGlobalInOctWraps_Type = Counter32
_IpsecGlobalInOctWraps_Object = MibScalar
ipsecGlobalInOctWraps = _IpsecGlobalInOctWraps_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 3, 1, 5),
    _IpsecGlobalInOctWraps_Type()
)
ipsecGlobalInOctWraps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecGlobalInOctWraps.setStatus("current")
_IpsecGlobalInDecompOctets_Type = Counter32
_IpsecGlobalInDecompOctets_Object = MibScalar
ipsecGlobalInDecompOctets = _IpsecGlobalInDecompOctets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 3, 1, 6),
    _IpsecGlobalInDecompOctets_Type()
)
ipsecGlobalInDecompOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecGlobalInDecompOctets.setStatus("current")
_IpsecGlobalHcInDecompOctets_Type = Counter64
_IpsecGlobalHcInDecompOctets_Object = MibScalar
ipsecGlobalHcInDecompOctets = _IpsecGlobalHcInDecompOctets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 3, 1, 7),
    _IpsecGlobalHcInDecompOctets_Type()
)
ipsecGlobalHcInDecompOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecGlobalHcInDecompOctets.setStatus("current")
_IpsecGlobalInDecompOctWraps_Type = Counter32
_IpsecGlobalInDecompOctWraps_Object = MibScalar
ipsecGlobalInDecompOctWraps = _IpsecGlobalInDecompOctWraps_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 3, 1, 8),
    _IpsecGlobalInDecompOctWraps_Type()
)
ipsecGlobalInDecompOctWraps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecGlobalInDecompOctWraps.setStatus("current")
_IpsecGlobalInPkts_Type = Counter32
_IpsecGlobalInPkts_Object = MibScalar
ipsecGlobalInPkts = _IpsecGlobalInPkts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 3, 1, 9),
    _IpsecGlobalInPkts_Type()
)
ipsecGlobalInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecGlobalInPkts.setStatus("current")
_IpsecGlobalInDrops_Type = Counter32
_IpsecGlobalInDrops_Object = MibScalar
ipsecGlobalInDrops = _IpsecGlobalInDrops_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 3, 1, 10),
    _IpsecGlobalInDrops_Type()
)
ipsecGlobalInDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecGlobalInDrops.setStatus("current")
_IpsecGlobalInReplayDrops_Type = Counter32
_IpsecGlobalInReplayDrops_Object = MibScalar
ipsecGlobalInReplayDrops = _IpsecGlobalInReplayDrops_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 3, 1, 11),
    _IpsecGlobalInReplayDrops_Type()
)
ipsecGlobalInReplayDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecGlobalInReplayDrops.setStatus("current")
_IpsecGlobalInAuths_Type = Counter32
_IpsecGlobalInAuths_Object = MibScalar
ipsecGlobalInAuths = _IpsecGlobalInAuths_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 3, 1, 12),
    _IpsecGlobalInAuths_Type()
)
ipsecGlobalInAuths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecGlobalInAuths.setStatus("current")
_IpsecGlobalInAuthFails_Type = Counter32
_IpsecGlobalInAuthFails_Object = MibScalar
ipsecGlobalInAuthFails = _IpsecGlobalInAuthFails_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 3, 1, 13),
    _IpsecGlobalInAuthFails_Type()
)
ipsecGlobalInAuthFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecGlobalInAuthFails.setStatus("current")
_IpsecGlobalInDecrypts_Type = Counter32
_IpsecGlobalInDecrypts_Object = MibScalar
ipsecGlobalInDecrypts = _IpsecGlobalInDecrypts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 3, 1, 14),
    _IpsecGlobalInDecrypts_Type()
)
ipsecGlobalInDecrypts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecGlobalInDecrypts.setStatus("current")
_IpsecGlobalInDecryptFails_Type = Counter32
_IpsecGlobalInDecryptFails_Object = MibScalar
ipsecGlobalInDecryptFails = _IpsecGlobalInDecryptFails_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 3, 1, 15),
    _IpsecGlobalInDecryptFails_Type()
)
ipsecGlobalInDecryptFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecGlobalInDecryptFails.setStatus("current")
_IpsecGlobalOutOctets_Type = Counter32
_IpsecGlobalOutOctets_Object = MibScalar
ipsecGlobalOutOctets = _IpsecGlobalOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 3, 1, 16),
    _IpsecGlobalOutOctets_Type()
)
ipsecGlobalOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecGlobalOutOctets.setStatus("current")
_IpsecGlobalHcOutOctets_Type = Counter64
_IpsecGlobalHcOutOctets_Object = MibScalar
ipsecGlobalHcOutOctets = _IpsecGlobalHcOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 3, 1, 17),
    _IpsecGlobalHcOutOctets_Type()
)
ipsecGlobalHcOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecGlobalHcOutOctets.setStatus("current")
_IpsecGlobalOutOctWraps_Type = Counter32
_IpsecGlobalOutOctWraps_Object = MibScalar
ipsecGlobalOutOctWraps = _IpsecGlobalOutOctWraps_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 3, 1, 18),
    _IpsecGlobalOutOctWraps_Type()
)
ipsecGlobalOutOctWraps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecGlobalOutOctWraps.setStatus("current")
_IpsecGlobalOutUncompOctets_Type = Counter32
_IpsecGlobalOutUncompOctets_Object = MibScalar
ipsecGlobalOutUncompOctets = _IpsecGlobalOutUncompOctets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 3, 1, 19),
    _IpsecGlobalOutUncompOctets_Type()
)
ipsecGlobalOutUncompOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecGlobalOutUncompOctets.setStatus("current")
_IpsecGlobalHcOutUncompOctets_Type = Counter64
_IpsecGlobalHcOutUncompOctets_Object = MibScalar
ipsecGlobalHcOutUncompOctets = _IpsecGlobalHcOutUncompOctets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 3, 1, 20),
    _IpsecGlobalHcOutUncompOctets_Type()
)
ipsecGlobalHcOutUncompOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecGlobalHcOutUncompOctets.setStatus("current")
_IpsecGlobalOutUncompOctWraps_Type = Counter32
_IpsecGlobalOutUncompOctWraps_Object = MibScalar
ipsecGlobalOutUncompOctWraps = _IpsecGlobalOutUncompOctWraps_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 3, 1, 21),
    _IpsecGlobalOutUncompOctWraps_Type()
)
ipsecGlobalOutUncompOctWraps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecGlobalOutUncompOctWraps.setStatus("current")
_IpsecGlobalOutPkts_Type = Counter32
_IpsecGlobalOutPkts_Object = MibScalar
ipsecGlobalOutPkts = _IpsecGlobalOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 3, 1, 22),
    _IpsecGlobalOutPkts_Type()
)
ipsecGlobalOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecGlobalOutPkts.setStatus("current")
_IpsecGlobalOutDrops_Type = Counter32
_IpsecGlobalOutDrops_Object = MibScalar
ipsecGlobalOutDrops = _IpsecGlobalOutDrops_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 3, 1, 23),
    _IpsecGlobalOutDrops_Type()
)
ipsecGlobalOutDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecGlobalOutDrops.setStatus("current")
_IpsecGlobalOutAuths_Type = Counter32
_IpsecGlobalOutAuths_Object = MibScalar
ipsecGlobalOutAuths = _IpsecGlobalOutAuths_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 3, 1, 24),
    _IpsecGlobalOutAuths_Type()
)
ipsecGlobalOutAuths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecGlobalOutAuths.setStatus("current")
_IpsecGlobalOutAuthFails_Type = Counter32
_IpsecGlobalOutAuthFails_Object = MibScalar
ipsecGlobalOutAuthFails = _IpsecGlobalOutAuthFails_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 3, 1, 25),
    _IpsecGlobalOutAuthFails_Type()
)
ipsecGlobalOutAuthFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecGlobalOutAuthFails.setStatus("current")
_IpsecGlobalOutEncrypts_Type = Counter32
_IpsecGlobalOutEncrypts_Object = MibScalar
ipsecGlobalOutEncrypts = _IpsecGlobalOutEncrypts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 3, 1, 26),
    _IpsecGlobalOutEncrypts_Type()
)
ipsecGlobalOutEncrypts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecGlobalOutEncrypts.setStatus("current")
_IpsecGlobalOutEncryptFails_Type = Counter32
_IpsecGlobalOutEncryptFails_Object = MibScalar
ipsecGlobalOutEncryptFails = _IpsecGlobalOutEncryptFails_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 3, 1, 27),
    _IpsecGlobalOutEncryptFails_Type()
)
ipsecGlobalOutEncryptFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecGlobalOutEncryptFails.setStatus("current")
_IpsecTunnelTable_Object = MibTable
ipsecTunnelTable = _IpsecTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 3, 2)
)
if mibBuilder.loadTexts:
    ipsecTunnelTable.setStatus("current")
_IpsecTunnelEntry_Object = MibTableRow
ipsecTunnelEntry = _IpsecTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 3, 2, 1)
)
ipsecTunnelEntry.setIndexNames(
    (0, "IPsecT1-MIB", "ipsecTunIndex"),
)
if mibBuilder.loadTexts:
    ipsecTunnelEntry.setStatus("current")
_IpsecTunIndex_Type = Integer32
_IpsecTunIndex_Object = MibTableColumn
ipsecTunIndex = _IpsecTunIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 3, 2, 1, 1),
    _IpsecTunIndex_Type()
)
ipsecTunIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipsecTunIndex.setStatus("current")
_IpsecTunIkeTunnelIndex_Type = Integer32
_IpsecTunIkeTunnelIndex_Object = MibTableColumn
ipsecTunIkeTunnelIndex = _IpsecTunIkeTunnelIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 3, 2, 1, 2),
    _IpsecTunIkeTunnelIndex_Type()
)
ipsecTunIkeTunnelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTunIkeTunnelIndex.setStatus("current")
_IpsecTunIkeTunnelAlive_Type = TruthValue
_IpsecTunIkeTunnelAlive_Object = MibTableColumn
ipsecTunIkeTunnelAlive = _IpsecTunIkeTunnelAlive_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 3, 2, 1, 3),
    _IpsecTunIkeTunnelAlive_Type()
)
ipsecTunIkeTunnelAlive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTunIkeTunnelAlive.setStatus("current")
_IpsecTunLocalAddr_Type = IPSIpAddress
_IpsecTunLocalAddr_Object = MibTableColumn
ipsecTunLocalAddr = _IpsecTunLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 3, 2, 1, 4),
    _IpsecTunLocalAddr_Type()
)
ipsecTunLocalAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTunLocalAddr.setStatus("current")
_IpsecTunRemoteAddr_Type = IPSIpAddress
_IpsecTunRemoteAddr_Object = MibTableColumn
ipsecTunRemoteAddr = _IpsecTunRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 3, 2, 1, 5),
    _IpsecTunRemoteAddr_Type()
)
ipsecTunRemoteAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTunRemoteAddr.setStatus("current")
_IpsecTunKeyType_Type = KeyType
_IpsecTunKeyType_Object = MibTableColumn
ipsecTunKeyType = _IpsecTunKeyType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 3, 2, 1, 6),
    _IpsecTunKeyType_Type()
)
ipsecTunKeyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTunKeyType.setStatus("current")
_IpsecTunEncapMode_Type = EncapMode
_IpsecTunEncapMode_Object = MibTableColumn
ipsecTunEncapMode = _IpsecTunEncapMode_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 3, 2, 1, 7),
    _IpsecTunEncapMode_Type()
)
ipsecTunEncapMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTunEncapMode.setStatus("current")
_IpsecTunLifeSize_Type = Integer32
_IpsecTunLifeSize_Object = MibTableColumn
ipsecTunLifeSize = _IpsecTunLifeSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 3, 2, 1, 8),
    _IpsecTunLifeSize_Type()
)
ipsecTunLifeSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTunLifeSize.setStatus("current")
_IpsecTunLifeTime_Type = Integer32
_IpsecTunLifeTime_Object = MibTableColumn
ipsecTunLifeTime = _IpsecTunLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 3, 2, 1, 9),
    _IpsecTunLifeTime_Type()
)
ipsecTunLifeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTunLifeTime.setStatus("current")
_IpsecTunActiveTime_Type = TimeInterval
_IpsecTunActiveTime_Object = MibTableColumn
ipsecTunActiveTime = _IpsecTunActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 3, 2, 1, 10),
    _IpsecTunActiveTime_Type()
)
ipsecTunActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTunActiveTime.setStatus("current")
_IpsecTunSaLifeSizeThreshold_Type = Integer32
_IpsecTunSaLifeSizeThreshold_Object = MibTableColumn
ipsecTunSaLifeSizeThreshold = _IpsecTunSaLifeSizeThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 3, 2, 1, 11),
    _IpsecTunSaLifeSizeThreshold_Type()
)
ipsecTunSaLifeSizeThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTunSaLifeSizeThreshold.setStatus("current")
_IpsecTunSaLifeTimeThreshold_Type = Integer32
_IpsecTunSaLifeTimeThreshold_Object = MibTableColumn
ipsecTunSaLifeTimeThreshold = _IpsecTunSaLifeTimeThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 3, 2, 1, 12),
    _IpsecTunSaLifeTimeThreshold_Type()
)
ipsecTunSaLifeTimeThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTunSaLifeTimeThreshold.setStatus("current")
_IpsecTunTotalRefreshes_Type = Counter32
_IpsecTunTotalRefreshes_Object = MibTableColumn
ipsecTunTotalRefreshes = _IpsecTunTotalRefreshes_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 3, 2, 1, 13),
    _IpsecTunTotalRefreshes_Type()
)
ipsecTunTotalRefreshes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTunTotalRefreshes.setStatus("current")
_IpsecTunExpiredSaInstances_Type = Counter32
_IpsecTunExpiredSaInstances_Object = MibTableColumn
ipsecTunExpiredSaInstances = _IpsecTunExpiredSaInstances_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 3, 2, 1, 14),
    _IpsecTunExpiredSaInstances_Type()
)
ipsecTunExpiredSaInstances.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTunExpiredSaInstances.setStatus("current")
_IpsecTunCurrentSaInstances_Type = Gauge32
_IpsecTunCurrentSaInstances_Object = MibTableColumn
ipsecTunCurrentSaInstances = _IpsecTunCurrentSaInstances_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 3, 2, 1, 15),
    _IpsecTunCurrentSaInstances_Type()
)
ipsecTunCurrentSaInstances.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTunCurrentSaInstances.setStatus("current")
_IpsecTunInSaDiffHellmanGrp_Type = DiffHellmanGrp
_IpsecTunInSaDiffHellmanGrp_Object = MibTableColumn
ipsecTunInSaDiffHellmanGrp = _IpsecTunInSaDiffHellmanGrp_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 3, 2, 1, 16),
    _IpsecTunInSaDiffHellmanGrp_Type()
)
ipsecTunInSaDiffHellmanGrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTunInSaDiffHellmanGrp.setStatus("current")
_IpsecTunInSaEncryptAlgo_Type = EncryptAlgo
_IpsecTunInSaEncryptAlgo_Object = MibTableColumn
ipsecTunInSaEncryptAlgo = _IpsecTunInSaEncryptAlgo_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 3, 2, 1, 17),
    _IpsecTunInSaEncryptAlgo_Type()
)
ipsecTunInSaEncryptAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTunInSaEncryptAlgo.setStatus("current")
_IpsecTunInSaAhAuthAlgo_Type = AuthAlgo
_IpsecTunInSaAhAuthAlgo_Object = MibTableColumn
ipsecTunInSaAhAuthAlgo = _IpsecTunInSaAhAuthAlgo_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 3, 2, 1, 18),
    _IpsecTunInSaAhAuthAlgo_Type()
)
ipsecTunInSaAhAuthAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTunInSaAhAuthAlgo.setStatus("current")
_IpsecTunInSaEspAuthAlgo_Type = AuthAlgo
_IpsecTunInSaEspAuthAlgo_Object = MibTableColumn
ipsecTunInSaEspAuthAlgo = _IpsecTunInSaEspAuthAlgo_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 3, 2, 1, 19),
    _IpsecTunInSaEspAuthAlgo_Type()
)
ipsecTunInSaEspAuthAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTunInSaEspAuthAlgo.setStatus("current")
_IpsecTunInSaDecompAlgo_Type = CompAlgo
_IpsecTunInSaDecompAlgo_Object = MibTableColumn
ipsecTunInSaDecompAlgo = _IpsecTunInSaDecompAlgo_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 3, 2, 1, 20),
    _IpsecTunInSaDecompAlgo_Type()
)
ipsecTunInSaDecompAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTunInSaDecompAlgo.setStatus("current")
_IpsecTunOutSaDiffHellmanGrp_Type = DiffHellmanGrp
_IpsecTunOutSaDiffHellmanGrp_Object = MibTableColumn
ipsecTunOutSaDiffHellmanGrp = _IpsecTunOutSaDiffHellmanGrp_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 3, 2, 1, 21),
    _IpsecTunOutSaDiffHellmanGrp_Type()
)
ipsecTunOutSaDiffHellmanGrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTunOutSaDiffHellmanGrp.setStatus("current")
_IpsecTunOutSaEncryptAlgo_Type = EncryptAlgo
_IpsecTunOutSaEncryptAlgo_Object = MibTableColumn
ipsecTunOutSaEncryptAlgo = _IpsecTunOutSaEncryptAlgo_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 3, 2, 1, 22),
    _IpsecTunOutSaEncryptAlgo_Type()
)
ipsecTunOutSaEncryptAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTunOutSaEncryptAlgo.setStatus("current")
_IpsecTunOutSaAhAuthAlgo_Type = AuthAlgo
_IpsecTunOutSaAhAuthAlgo_Object = MibTableColumn
ipsecTunOutSaAhAuthAlgo = _IpsecTunOutSaAhAuthAlgo_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 3, 2, 1, 23),
    _IpsecTunOutSaAhAuthAlgo_Type()
)
ipsecTunOutSaAhAuthAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTunOutSaAhAuthAlgo.setStatus("current")
_IpsecTunOutSaEspAuthAlgo_Type = AuthAlgo
_IpsecTunOutSaEspAuthAlgo_Object = MibTableColumn
ipsecTunOutSaEspAuthAlgo = _IpsecTunOutSaEspAuthAlgo_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 3, 2, 1, 24),
    _IpsecTunOutSaEspAuthAlgo_Type()
)
ipsecTunOutSaEspAuthAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTunOutSaEspAuthAlgo.setStatus("current")
_IpsecTunOutSaCompAlgo_Type = CompAlgo
_IpsecTunOutSaCompAlgo_Object = MibTableColumn
ipsecTunOutSaCompAlgo = _IpsecTunOutSaCompAlgo_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 3, 2, 1, 25),
    _IpsecTunOutSaCompAlgo_Type()
)
ipsecTunOutSaCompAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTunOutSaCompAlgo.setStatus("current")
_IpsecTunInOctets_Type = Counter32
_IpsecTunInOctets_Object = MibTableColumn
ipsecTunInOctets = _IpsecTunInOctets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 3, 2, 1, 26),
    _IpsecTunInOctets_Type()
)
ipsecTunInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTunInOctets.setStatus("current")
_IpsecTunHcInOctets_Type = Counter64
_IpsecTunHcInOctets_Object = MibTableColumn
ipsecTunHcInOctets = _IpsecTunHcInOctets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 3, 2, 1, 27),
    _IpsecTunHcInOctets_Type()
)
ipsecTunHcInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTunHcInOctets.setStatus("current")
_IpsecTunInOctWraps_Type = Counter32
_IpsecTunInOctWraps_Object = MibTableColumn
ipsecTunInOctWraps = _IpsecTunInOctWraps_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 3, 2, 1, 28),
    _IpsecTunInOctWraps_Type()
)
ipsecTunInOctWraps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTunInOctWraps.setStatus("current")
_IpsecTunInDecompOctets_Type = Counter32
_IpsecTunInDecompOctets_Object = MibTableColumn
ipsecTunInDecompOctets = _IpsecTunInDecompOctets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 3, 2, 1, 29),
    _IpsecTunInDecompOctets_Type()
)
ipsecTunInDecompOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTunInDecompOctets.setStatus("current")
_IpsecTunHcInDecompOctets_Type = Counter64
_IpsecTunHcInDecompOctets_Object = MibTableColumn
ipsecTunHcInDecompOctets = _IpsecTunHcInDecompOctets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 3, 2, 1, 30),
    _IpsecTunHcInDecompOctets_Type()
)
ipsecTunHcInDecompOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTunHcInDecompOctets.setStatus("current")
_IpsecTunInDecompOctWraps_Type = Counter32
_IpsecTunInDecompOctWraps_Object = MibTableColumn
ipsecTunInDecompOctWraps = _IpsecTunInDecompOctWraps_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 3, 2, 1, 31),
    _IpsecTunInDecompOctWraps_Type()
)
ipsecTunInDecompOctWraps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTunInDecompOctWraps.setStatus("current")
_IpsecTunInPkts_Type = Counter32
_IpsecTunInPkts_Object = MibTableColumn
ipsecTunInPkts = _IpsecTunInPkts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 3, 2, 1, 32),
    _IpsecTunInPkts_Type()
)
ipsecTunInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTunInPkts.setStatus("current")
_IpsecTunInDropPkts_Type = Counter32
_IpsecTunInDropPkts_Object = MibTableColumn
ipsecTunInDropPkts = _IpsecTunInDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 3, 2, 1, 33),
    _IpsecTunInDropPkts_Type()
)
ipsecTunInDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTunInDropPkts.setStatus("current")
_IpsecTunInReplayDropPkts_Type = Counter32
_IpsecTunInReplayDropPkts_Object = MibTableColumn
ipsecTunInReplayDropPkts = _IpsecTunInReplayDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 3, 2, 1, 34),
    _IpsecTunInReplayDropPkts_Type()
)
ipsecTunInReplayDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTunInReplayDropPkts.setStatus("current")
_IpsecTunInAuths_Type = Counter32
_IpsecTunInAuths_Object = MibTableColumn
ipsecTunInAuths = _IpsecTunInAuths_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 3, 2, 1, 35),
    _IpsecTunInAuths_Type()
)
ipsecTunInAuths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTunInAuths.setStatus("current")
_IpsecTunInAuthFails_Type = Counter32
_IpsecTunInAuthFails_Object = MibTableColumn
ipsecTunInAuthFails = _IpsecTunInAuthFails_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 3, 2, 1, 36),
    _IpsecTunInAuthFails_Type()
)
ipsecTunInAuthFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTunInAuthFails.setStatus("current")
_IpsecTunInDecrypts_Type = Counter32
_IpsecTunInDecrypts_Object = MibTableColumn
ipsecTunInDecrypts = _IpsecTunInDecrypts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 3, 2, 1, 37),
    _IpsecTunInDecrypts_Type()
)
ipsecTunInDecrypts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTunInDecrypts.setStatus("current")
_IpsecTunInDecryptFails_Type = Counter32
_IpsecTunInDecryptFails_Object = MibTableColumn
ipsecTunInDecryptFails = _IpsecTunInDecryptFails_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 3, 2, 1, 38),
    _IpsecTunInDecryptFails_Type()
)
ipsecTunInDecryptFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTunInDecryptFails.setStatus("current")
_IpsecTunOutOctets_Type = Counter32
_IpsecTunOutOctets_Object = MibTableColumn
ipsecTunOutOctets = _IpsecTunOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 3, 2, 1, 39),
    _IpsecTunOutOctets_Type()
)
ipsecTunOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTunOutOctets.setStatus("current")
_IpsecTunHcOutOctets_Type = Counter64
_IpsecTunHcOutOctets_Object = MibTableColumn
ipsecTunHcOutOctets = _IpsecTunHcOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 3, 2, 1, 40),
    _IpsecTunHcOutOctets_Type()
)
ipsecTunHcOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTunHcOutOctets.setStatus("current")
_IpsecTunOutOctWraps_Type = Counter32
_IpsecTunOutOctWraps_Object = MibTableColumn
ipsecTunOutOctWraps = _IpsecTunOutOctWraps_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 3, 2, 1, 41),
    _IpsecTunOutOctWraps_Type()
)
ipsecTunOutOctWraps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTunOutOctWraps.setStatus("current")
_IpsecTunOutUncompOctets_Type = Counter32
_IpsecTunOutUncompOctets_Object = MibTableColumn
ipsecTunOutUncompOctets = _IpsecTunOutUncompOctets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 3, 2, 1, 42),
    _IpsecTunOutUncompOctets_Type()
)
ipsecTunOutUncompOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTunOutUncompOctets.setStatus("current")
_IpsecTunHcOutUncompOctets_Type = Counter64
_IpsecTunHcOutUncompOctets_Object = MibTableColumn
ipsecTunHcOutUncompOctets = _IpsecTunHcOutUncompOctets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 3, 2, 1, 43),
    _IpsecTunHcOutUncompOctets_Type()
)
ipsecTunHcOutUncompOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTunHcOutUncompOctets.setStatus("current")
_IpsecTunOutUncompOctWraps_Type = Counter32
_IpsecTunOutUncompOctWraps_Object = MibTableColumn
ipsecTunOutUncompOctWraps = _IpsecTunOutUncompOctWraps_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 3, 2, 1, 44),
    _IpsecTunOutUncompOctWraps_Type()
)
ipsecTunOutUncompOctWraps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTunOutUncompOctWraps.setStatus("current")
_IpsecTunOutPkts_Type = Counter32
_IpsecTunOutPkts_Object = MibTableColumn
ipsecTunOutPkts = _IpsecTunOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 3, 2, 1, 45),
    _IpsecTunOutPkts_Type()
)
ipsecTunOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTunOutPkts.setStatus("current")
_IpsecTunOutDropPkts_Type = Counter32
_IpsecTunOutDropPkts_Object = MibTableColumn
ipsecTunOutDropPkts = _IpsecTunOutDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 3, 2, 1, 46),
    _IpsecTunOutDropPkts_Type()
)
ipsecTunOutDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTunOutDropPkts.setStatus("current")
_IpsecTunOutAuths_Type = Counter32
_IpsecTunOutAuths_Object = MibTableColumn
ipsecTunOutAuths = _IpsecTunOutAuths_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 3, 2, 1, 47),
    _IpsecTunOutAuths_Type()
)
ipsecTunOutAuths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTunOutAuths.setStatus("current")
_IpsecTunOutAuthFails_Type = Counter32
_IpsecTunOutAuthFails_Object = MibTableColumn
ipsecTunOutAuthFails = _IpsecTunOutAuthFails_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 3, 2, 1, 48),
    _IpsecTunOutAuthFails_Type()
)
ipsecTunOutAuthFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTunOutAuthFails.setStatus("current")
_IpsecTunOutEncrypts_Type = Counter32
_IpsecTunOutEncrypts_Object = MibTableColumn
ipsecTunOutEncrypts = _IpsecTunOutEncrypts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 3, 2, 1, 49),
    _IpsecTunOutEncrypts_Type()
)
ipsecTunOutEncrypts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTunOutEncrypts.setStatus("current")
_IpsecTunOutEncryptFails_Type = Counter32
_IpsecTunOutEncryptFails_Object = MibTableColumn
ipsecTunOutEncryptFails = _IpsecTunOutEncryptFails_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 3, 2, 1, 50),
    _IpsecTunOutEncryptFails_Type()
)
ipsecTunOutEncryptFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTunOutEncryptFails.setStatus("current")
_IpsecTunStatus_Type = TunnelStatus
_IpsecTunStatus_Object = MibTableColumn
ipsecTunStatus = _IpsecTunStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 3, 2, 1, 51),
    _IpsecTunStatus_Type()
)
ipsecTunStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecTunStatus.setStatus("current")
_IpsecEndPtTable_Object = MibTable
ipsecEndPtTable = _IpsecEndPtTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 3, 3)
)
if mibBuilder.loadTexts:
    ipsecEndPtTable.setStatus("current")
_IpsecEndPtEntry_Object = MibTableRow
ipsecEndPtEntry = _IpsecEndPtEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 3, 3, 1)
)
ipsecEndPtEntry.setIndexNames(
    (0, "IPsecT1-MIB", "ipsecTunIndex"),
    (0, "IPsecT1-MIB", "ipsecEndPtIndex"),
)
if mibBuilder.loadTexts:
    ipsecEndPtEntry.setStatus("current")
_IpsecEndPtIndex_Type = Integer32
_IpsecEndPtIndex_Object = MibTableColumn
ipsecEndPtIndex = _IpsecEndPtIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 3, 3, 1, 1),
    _IpsecEndPtIndex_Type()
)
ipsecEndPtIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipsecEndPtIndex.setStatus("current")
_IpsecEndPtLocalName_Type = DisplayString
_IpsecEndPtLocalName_Object = MibTableColumn
ipsecEndPtLocalName = _IpsecEndPtLocalName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 3, 3, 1, 2),
    _IpsecEndPtLocalName_Type()
)
ipsecEndPtLocalName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecEndPtLocalName.setStatus("current")
_IpsecEndPtLocalType_Type = EndPtType
_IpsecEndPtLocalType_Object = MibTableColumn
ipsecEndPtLocalType = _IpsecEndPtLocalType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 3, 3, 1, 3),
    _IpsecEndPtLocalType_Type()
)
ipsecEndPtLocalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecEndPtLocalType.setStatus("current")
_IpsecEndPtLocalAddr1_Type = IPSIpAddress
_IpsecEndPtLocalAddr1_Object = MibTableColumn
ipsecEndPtLocalAddr1 = _IpsecEndPtLocalAddr1_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 3, 3, 1, 4),
    _IpsecEndPtLocalAddr1_Type()
)
ipsecEndPtLocalAddr1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecEndPtLocalAddr1.setStatus("current")
_IpsecEndPtLocalAddr2_Type = IPSIpAddress
_IpsecEndPtLocalAddr2_Object = MibTableColumn
ipsecEndPtLocalAddr2 = _IpsecEndPtLocalAddr2_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 3, 3, 1, 5),
    _IpsecEndPtLocalAddr2_Type()
)
ipsecEndPtLocalAddr2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecEndPtLocalAddr2.setStatus("current")


class _IpsecEndPtLocalProtocol_Type(Integer32):
    """Custom type ipsecEndPtLocalProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_IpsecEndPtLocalProtocol_Type.__name__ = "Integer32"
_IpsecEndPtLocalProtocol_Object = MibTableColumn
ipsecEndPtLocalProtocol = _IpsecEndPtLocalProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 3, 3, 1, 6),
    _IpsecEndPtLocalProtocol_Type()
)
ipsecEndPtLocalProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecEndPtLocalProtocol.setStatus("current")


class _IpsecEndPtLocalPort_Type(Integer32):
    """Custom type ipsecEndPtLocalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpsecEndPtLocalPort_Type.__name__ = "Integer32"
_IpsecEndPtLocalPort_Object = MibTableColumn
ipsecEndPtLocalPort = _IpsecEndPtLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 3, 3, 1, 7),
    _IpsecEndPtLocalPort_Type()
)
ipsecEndPtLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecEndPtLocalPort.setStatus("current")
_IpsecEndPtRemoteName_Type = DisplayString
_IpsecEndPtRemoteName_Object = MibTableColumn
ipsecEndPtRemoteName = _IpsecEndPtRemoteName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 3, 3, 1, 8),
    _IpsecEndPtRemoteName_Type()
)
ipsecEndPtRemoteName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecEndPtRemoteName.setStatus("current")
_IpsecEndPtRemoteType_Type = EndPtType
_IpsecEndPtRemoteType_Object = MibTableColumn
ipsecEndPtRemoteType = _IpsecEndPtRemoteType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 3, 3, 1, 9),
    _IpsecEndPtRemoteType_Type()
)
ipsecEndPtRemoteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecEndPtRemoteType.setStatus("current")
_IpsecEndPtRemoteAddr1_Type = IPSIpAddress
_IpsecEndPtRemoteAddr1_Object = MibTableColumn
ipsecEndPtRemoteAddr1 = _IpsecEndPtRemoteAddr1_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 3, 3, 1, 10),
    _IpsecEndPtRemoteAddr1_Type()
)
ipsecEndPtRemoteAddr1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecEndPtRemoteAddr1.setStatus("current")
_IpsecEndPtRemoteAddr2_Type = IPSIpAddress
_IpsecEndPtRemoteAddr2_Object = MibTableColumn
ipsecEndPtRemoteAddr2 = _IpsecEndPtRemoteAddr2_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 3, 3, 1, 11),
    _IpsecEndPtRemoteAddr2_Type()
)
ipsecEndPtRemoteAddr2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecEndPtRemoteAddr2.setStatus("current")


class _IpsecEndPtRemoteProtocol_Type(Integer32):
    """Custom type ipsecEndPtRemoteProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_IpsecEndPtRemoteProtocol_Type.__name__ = "Integer32"
_IpsecEndPtRemoteProtocol_Object = MibTableColumn
ipsecEndPtRemoteProtocol = _IpsecEndPtRemoteProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 3, 3, 1, 12),
    _IpsecEndPtRemoteProtocol_Type()
)
ipsecEndPtRemoteProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecEndPtRemoteProtocol.setStatus("current")


class _IpsecEndPtRemotePort_Type(Integer32):
    """Custom type ipsecEndPtRemotePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpsecEndPtRemotePort_Type.__name__ = "Integer32"
_IpsecEndPtRemotePort_Object = MibTableColumn
ipsecEndPtRemotePort = _IpsecEndPtRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 3, 3, 1, 13),
    _IpsecEndPtRemotePort_Type()
)
ipsecEndPtRemotePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecEndPtRemotePort.setStatus("current")
_IpsecSpiTable_Object = MibTable
ipsecSpiTable = _IpsecSpiTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 3, 4)
)
if mibBuilder.loadTexts:
    ipsecSpiTable.setStatus("current")
_IpsecSpiEntry_Object = MibTableRow
ipsecSpiEntry = _IpsecSpiEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 3, 4, 1)
)
ipsecSpiEntry.setIndexNames(
    (0, "IPsecT1-MIB", "ipsecTunIndex"),
    (0, "IPsecT1-MIB", "ipsecSpiIndex"),
)
if mibBuilder.loadTexts:
    ipsecSpiEntry.setStatus("current")
_IpsecSpiIndex_Type = Integer32
_IpsecSpiIndex_Object = MibTableColumn
ipsecSpiIndex = _IpsecSpiIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 3, 4, 1, 1),
    _IpsecSpiIndex_Type()
)
ipsecSpiIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipsecSpiIndex.setStatus("current")


class _IpsecSpiDirection_Type(Integer32):
    """Custom type ipsecSpiDirection based on Integer32"""
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


_IpsecSpiDirection_Type.__name__ = "Integer32"
_IpsecSpiDirection_Object = MibTableColumn
ipsecSpiDirection = _IpsecSpiDirection_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 3, 4, 1, 2),
    _IpsecSpiDirection_Type()
)
ipsecSpiDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSpiDirection.setStatus("current")
_IpsecSpiValue_Type = Integer32
_IpsecSpiValue_Object = MibTableColumn
ipsecSpiValue = _IpsecSpiValue_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 3, 4, 1, 3),
    _IpsecSpiValue_Type()
)
ipsecSpiValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSpiValue.setStatus("current")


class _IpsecSpiProtocol_Type(Integer32):
    """Custom type ipsecSpiProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ah", 1),
          ("esp", 2),
          ("ipcomp", 3))
    )


_IpsecSpiProtocol_Type.__name__ = "Integer32"
_IpsecSpiProtocol_Object = MibTableColumn
ipsecSpiProtocol = _IpsecSpiProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 3, 4, 1, 4),
    _IpsecSpiProtocol_Type()
)
ipsecSpiProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSpiProtocol.setStatus("current")


class _IpsecSpiStatus_Type(Integer32):
    """Custom type ipsecSpiStatus based on Integer32"""
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


_IpsecSpiStatus_Type.__name__ = "Integer32"
_IpsecSpiStatus_Object = MibTableColumn
ipsecSpiStatus = _IpsecSpiStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 3, 4, 1, 5),
    _IpsecSpiStatus_Type()
)
ipsecSpiStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSpiStatus.setStatus("current")
_IpsecHistory_ObjectIdentity = ObjectIdentity
ipsecHistory = _IpsecHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 4)
)
_IpsecHistGlobal_ObjectIdentity = ObjectIdentity
ipsecHistGlobal = _IpsecHistGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 4, 1)
)
_IpsecHistGlobalCntl_ObjectIdentity = ObjectIdentity
ipsecHistGlobalCntl = _IpsecHistGlobalCntl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 4, 1, 1)
)
_IpsecHistTableSize_Type = Integer32
_IpsecHistTableSize_Object = MibScalar
ipsecHistTableSize = _IpsecHistTableSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 4, 1, 1, 1),
    _IpsecHistTableSize_Type()
)
ipsecHistTableSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecHistTableSize.setStatus("current")
_IpsecHistPhaseOne_ObjectIdentity = ObjectIdentity
ipsecHistPhaseOne = _IpsecHistPhaseOne_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 4, 2)
)
_IkeTunnelHistTable_Object = MibTable
ikeTunnelHistTable = _IkeTunnelHistTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 4, 2, 1)
)
if mibBuilder.loadTexts:
    ikeTunnelHistTable.setStatus("current")
_IkeTunnelHistEntry_Object = MibTableRow
ikeTunnelHistEntry = _IkeTunnelHistEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 4, 2, 1, 1)
)
ikeTunnelHistEntry.setIndexNames(
    (0, "IPsecT1-MIB", "ikeTunHistIndex"),
)
if mibBuilder.loadTexts:
    ikeTunnelHistEntry.setStatus("current")
_IkeTunHistIndex_Type = Integer32
_IkeTunHistIndex_Object = MibTableColumn
ikeTunHistIndex = _IkeTunHistIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 4, 2, 1, 1, 1),
    _IkeTunHistIndex_Type()
)
ikeTunHistIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ikeTunHistIndex.setStatus("current")


class _IkeTunHistTermReason_Type(Integer32):
    """Custom type ikeTunHistTermReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("localFailure", 7),
          ("normal", 2),
          ("operRequest", 3),
          ("other", 1),
          ("peerDelRequest", 4),
          ("peerLost", 5),
          ("seqNumRollOver", 6))
    )


_IkeTunHistTermReason_Type.__name__ = "Integer32"
_IkeTunHistTermReason_Object = MibTableColumn
ikeTunHistTermReason = _IkeTunHistTermReason_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 4, 2, 1, 1, 2),
    _IkeTunHistTermReason_Type()
)
ikeTunHistTermReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeTunHistTermReason.setStatus("current")
_IkeTunHistActiveIndex_Type = Integer32
_IkeTunHistActiveIndex_Object = MibTableColumn
ikeTunHistActiveIndex = _IkeTunHistActiveIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 4, 2, 1, 1, 3),
    _IkeTunHistActiveIndex_Type()
)
ikeTunHistActiveIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeTunHistActiveIndex.setStatus("current")
_IkeTunHistPeerLocalType_Type = IkePeerType
_IkeTunHistPeerLocalType_Object = MibTableColumn
ikeTunHistPeerLocalType = _IkeTunHistPeerLocalType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 4, 2, 1, 1, 4),
    _IkeTunHistPeerLocalType_Type()
)
ikeTunHistPeerLocalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeTunHistPeerLocalType.setStatus("current")
_IkeTunHistPeerLocalValue_Type = DisplayString
_IkeTunHistPeerLocalValue_Object = MibTableColumn
ikeTunHistPeerLocalValue = _IkeTunHistPeerLocalValue_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 4, 2, 1, 1, 5),
    _IkeTunHistPeerLocalValue_Type()
)
ikeTunHistPeerLocalValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeTunHistPeerLocalValue.setStatus("current")
_IkeTunHistPeerIntIndex_Type = Integer32
_IkeTunHistPeerIntIndex_Object = MibTableColumn
ikeTunHistPeerIntIndex = _IkeTunHistPeerIntIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 4, 2, 1, 1, 6),
    _IkeTunHistPeerIntIndex_Type()
)
ikeTunHistPeerIntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeTunHistPeerIntIndex.setStatus("current")
_IkeTunHistPeerRemoteType_Type = IkePeerType
_IkeTunHistPeerRemoteType_Object = MibTableColumn
ikeTunHistPeerRemoteType = _IkeTunHistPeerRemoteType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 4, 2, 1, 1, 7),
    _IkeTunHistPeerRemoteType_Type()
)
ikeTunHistPeerRemoteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeTunHistPeerRemoteType.setStatus("current")
_IkeTunHistPeerRemoteValue_Type = DisplayString
_IkeTunHistPeerRemoteValue_Object = MibTableColumn
ikeTunHistPeerRemoteValue = _IkeTunHistPeerRemoteValue_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 4, 2, 1, 1, 8),
    _IkeTunHistPeerRemoteValue_Type()
)
ikeTunHistPeerRemoteValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeTunHistPeerRemoteValue.setStatus("current")
_IkeTunHistLocalAddr_Type = IPSIpAddress
_IkeTunHistLocalAddr_Object = MibTableColumn
ikeTunHistLocalAddr = _IkeTunHistLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 4, 2, 1, 1, 9),
    _IkeTunHistLocalAddr_Type()
)
ikeTunHistLocalAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeTunHistLocalAddr.setStatus("current")
_IkeTunHistLocalName_Type = DisplayString
_IkeTunHistLocalName_Object = MibTableColumn
ikeTunHistLocalName = _IkeTunHistLocalName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 4, 2, 1, 1, 10),
    _IkeTunHistLocalName_Type()
)
ikeTunHistLocalName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeTunHistLocalName.setStatus("current")
_IkeTunHistRemoteAddr_Type = IPSIpAddress
_IkeTunHistRemoteAddr_Object = MibTableColumn
ikeTunHistRemoteAddr = _IkeTunHistRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 4, 2, 1, 1, 11),
    _IkeTunHistRemoteAddr_Type()
)
ikeTunHistRemoteAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeTunHistRemoteAddr.setStatus("current")
_IkeTunHistRemoteName_Type = DisplayString
_IkeTunHistRemoteName_Object = MibTableColumn
ikeTunHistRemoteName = _IkeTunHistRemoteName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 4, 2, 1, 1, 12),
    _IkeTunHistRemoteName_Type()
)
ikeTunHistRemoteName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeTunHistRemoteName.setStatus("current")
_IkeTunHistNegoMode_Type = IkeNegoMode
_IkeTunHistNegoMode_Object = MibTableColumn
ikeTunHistNegoMode = _IkeTunHistNegoMode_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 4, 2, 1, 1, 13),
    _IkeTunHistNegoMode_Type()
)
ikeTunHistNegoMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeTunHistNegoMode.setStatus("current")
_IkeTunHistDiffHellmanGrp_Type = DiffHellmanGrp
_IkeTunHistDiffHellmanGrp_Object = MibTableColumn
ikeTunHistDiffHellmanGrp = _IkeTunHistDiffHellmanGrp_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 4, 2, 1, 1, 14),
    _IkeTunHistDiffHellmanGrp_Type()
)
ikeTunHistDiffHellmanGrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeTunHistDiffHellmanGrp.setStatus("current")
_IkeTunHistEncryptAlgo_Type = EncryptAlgo
_IkeTunHistEncryptAlgo_Object = MibTableColumn
ikeTunHistEncryptAlgo = _IkeTunHistEncryptAlgo_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 4, 2, 1, 1, 15),
    _IkeTunHistEncryptAlgo_Type()
)
ikeTunHistEncryptAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeTunHistEncryptAlgo.setStatus("current")
_IkeTunHistHashAlgo_Type = IkeHashAlgo
_IkeTunHistHashAlgo_Object = MibTableColumn
ikeTunHistHashAlgo = _IkeTunHistHashAlgo_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 4, 2, 1, 1, 16),
    _IkeTunHistHashAlgo_Type()
)
ikeTunHistHashAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeTunHistHashAlgo.setStatus("current")
_IkeTunHistAuthMethod_Type = IkeAuthMethod
_IkeTunHistAuthMethod_Object = MibTableColumn
ikeTunHistAuthMethod = _IkeTunHistAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 4, 2, 1, 1, 17),
    _IkeTunHistAuthMethod_Type()
)
ikeTunHistAuthMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeTunHistAuthMethod.setStatus("current")
_IkeTunHistLifeTime_Type = Integer32
_IkeTunHistLifeTime_Object = MibTableColumn
ikeTunHistLifeTime = _IkeTunHistLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 4, 2, 1, 1, 18),
    _IkeTunHistLifeTime_Type()
)
ikeTunHistLifeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeTunHistLifeTime.setStatus("current")
_IkeTunHistStartTime_Type = TimeStamp
_IkeTunHistStartTime_Object = MibTableColumn
ikeTunHistStartTime = _IkeTunHistStartTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 4, 2, 1, 1, 19),
    _IkeTunHistStartTime_Type()
)
ikeTunHistStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeTunHistStartTime.setStatus("current")
_IkeTunHistActiveTime_Type = TimeInterval
_IkeTunHistActiveTime_Object = MibTableColumn
ikeTunHistActiveTime = _IkeTunHistActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 4, 2, 1, 1, 20),
    _IkeTunHistActiveTime_Type()
)
ikeTunHistActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeTunHistActiveTime.setStatus("current")
_IkeTunHistTotalRefreshes_Type = Counter32
_IkeTunHistTotalRefreshes_Object = MibTableColumn
ikeTunHistTotalRefreshes = _IkeTunHistTotalRefreshes_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 4, 2, 1, 1, 21),
    _IkeTunHistTotalRefreshes_Type()
)
ikeTunHistTotalRefreshes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeTunHistTotalRefreshes.setStatus("current")
_IkeTunHistTotalSas_Type = Counter32
_IkeTunHistTotalSas_Object = MibTableColumn
ikeTunHistTotalSas = _IkeTunHistTotalSas_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 4, 2, 1, 1, 22),
    _IkeTunHistTotalSas_Type()
)
ikeTunHistTotalSas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeTunHistTotalSas.setStatus("current")
_IkeTunHistInOctets_Type = Counter32
_IkeTunHistInOctets_Object = MibTableColumn
ikeTunHistInOctets = _IkeTunHistInOctets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 4, 2, 1, 1, 23),
    _IkeTunHistInOctets_Type()
)
ikeTunHistInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeTunHistInOctets.setStatus("current")
_IkeTunHistInPkts_Type = Counter32
_IkeTunHistInPkts_Object = MibTableColumn
ikeTunHistInPkts = _IkeTunHistInPkts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 4, 2, 1, 1, 24),
    _IkeTunHistInPkts_Type()
)
ikeTunHistInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeTunHistInPkts.setStatus("current")
_IkeTunHistInDropPkts_Type = Counter32
_IkeTunHistInDropPkts_Object = MibTableColumn
ikeTunHistInDropPkts = _IkeTunHistInDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 4, 2, 1, 1, 25),
    _IkeTunHistInDropPkts_Type()
)
ikeTunHistInDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeTunHistInDropPkts.setStatus("current")
_IkeTunHistInNotifys_Type = Counter32
_IkeTunHistInNotifys_Object = MibTableColumn
ikeTunHistInNotifys = _IkeTunHistInNotifys_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 4, 2, 1, 1, 26),
    _IkeTunHistInNotifys_Type()
)
ikeTunHistInNotifys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeTunHistInNotifys.setStatus("current")
_IkeTunHistInP2Exchgs_Type = Counter32
_IkeTunHistInP2Exchgs_Object = MibTableColumn
ikeTunHistInP2Exchgs = _IkeTunHistInP2Exchgs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 4, 2, 1, 1, 27),
    _IkeTunHistInP2Exchgs_Type()
)
ikeTunHistInP2Exchgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeTunHistInP2Exchgs.setStatus("current")
_IkeTunHistInP2ExchgInvalids_Type = Counter32
_IkeTunHistInP2ExchgInvalids_Object = MibTableColumn
ikeTunHistInP2ExchgInvalids = _IkeTunHistInP2ExchgInvalids_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 4, 2, 1, 1, 28),
    _IkeTunHistInP2ExchgInvalids_Type()
)
ikeTunHistInP2ExchgInvalids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeTunHistInP2ExchgInvalids.setStatus("current")
_IkeTunHistInP2ExchgRejects_Type = Counter32
_IkeTunHistInP2ExchgRejects_Object = MibTableColumn
ikeTunHistInP2ExchgRejects = _IkeTunHistInP2ExchgRejects_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 4, 2, 1, 1, 29),
    _IkeTunHistInP2ExchgRejects_Type()
)
ikeTunHistInP2ExchgRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeTunHistInP2ExchgRejects.setStatus("current")
_IkeTunHistInP2SaDelRequests_Type = Counter32
_IkeTunHistInP2SaDelRequests_Object = MibTableColumn
ikeTunHistInP2SaDelRequests = _IkeTunHistInP2SaDelRequests_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 4, 2, 1, 1, 30),
    _IkeTunHistInP2SaDelRequests_Type()
)
ikeTunHistInP2SaDelRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeTunHistInP2SaDelRequests.setStatus("current")
_IkeTunHistOutOctets_Type = Counter32
_IkeTunHistOutOctets_Object = MibTableColumn
ikeTunHistOutOctets = _IkeTunHistOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 4, 2, 1, 1, 31),
    _IkeTunHistOutOctets_Type()
)
ikeTunHistOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeTunHistOutOctets.setStatus("current")
_IkeTunHistOutPkts_Type = Counter32
_IkeTunHistOutPkts_Object = MibTableColumn
ikeTunHistOutPkts = _IkeTunHistOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 4, 2, 1, 1, 32),
    _IkeTunHistOutPkts_Type()
)
ikeTunHistOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeTunHistOutPkts.setStatus("current")
_IkeTunHistOutDropPkts_Type = Counter32
_IkeTunHistOutDropPkts_Object = MibTableColumn
ikeTunHistOutDropPkts = _IkeTunHistOutDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 4, 2, 1, 1, 33),
    _IkeTunHistOutDropPkts_Type()
)
ikeTunHistOutDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeTunHistOutDropPkts.setStatus("current")
_IkeTunHistOutNotifys_Type = Counter32
_IkeTunHistOutNotifys_Object = MibTableColumn
ikeTunHistOutNotifys = _IkeTunHistOutNotifys_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 4, 2, 1, 1, 34),
    _IkeTunHistOutNotifys_Type()
)
ikeTunHistOutNotifys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeTunHistOutNotifys.setStatus("current")
_IkeTunHistOutP2Exchgs_Type = Counter32
_IkeTunHistOutP2Exchgs_Object = MibTableColumn
ikeTunHistOutP2Exchgs = _IkeTunHistOutP2Exchgs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 4, 2, 1, 1, 35),
    _IkeTunHistOutP2Exchgs_Type()
)
ikeTunHistOutP2Exchgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeTunHistOutP2Exchgs.setStatus("current")
_IkeTunHistOutP2ExchgInvalids_Type = Counter32
_IkeTunHistOutP2ExchgInvalids_Object = MibTableColumn
ikeTunHistOutP2ExchgInvalids = _IkeTunHistOutP2ExchgInvalids_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 4, 2, 1, 1, 36),
    _IkeTunHistOutP2ExchgInvalids_Type()
)
ikeTunHistOutP2ExchgInvalids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeTunHistOutP2ExchgInvalids.setStatus("current")
_IkeTunHistOutP2ExchgRejects_Type = Counter32
_IkeTunHistOutP2ExchgRejects_Object = MibTableColumn
ikeTunHistOutP2ExchgRejects = _IkeTunHistOutP2ExchgRejects_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 4, 2, 1, 1, 37),
    _IkeTunHistOutP2ExchgRejects_Type()
)
ikeTunHistOutP2ExchgRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeTunHistOutP2ExchgRejects.setStatus("current")
_IkeTunHistOutP2SaDelRequests_Type = Counter32
_IkeTunHistOutP2SaDelRequests_Object = MibTableColumn
ikeTunHistOutP2SaDelRequests = _IkeTunHistOutP2SaDelRequests_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 4, 2, 1, 1, 38),
    _IkeTunHistOutP2SaDelRequests_Type()
)
ikeTunHistOutP2SaDelRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeTunHistOutP2SaDelRequests.setStatus("current")
_IpsecHistPhaseTwo_ObjectIdentity = ObjectIdentity
ipsecHistPhaseTwo = _IpsecHistPhaseTwo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 4, 3)
)
_IpsecTunnelHistTable_Object = MibTable
ipsecTunnelHistTable = _IpsecTunnelHistTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 4, 3, 1)
)
if mibBuilder.loadTexts:
    ipsecTunnelHistTable.setStatus("current")
_IpsecTunnelHistEntry_Object = MibTableRow
ipsecTunnelHistEntry = _IpsecTunnelHistEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 4, 3, 1, 1)
)
ipsecTunnelHistEntry.setIndexNames(
    (0, "IPsecT1-MIB", "ipsecTunHistIndex"),
)
if mibBuilder.loadTexts:
    ipsecTunnelHistEntry.setStatus("current")
_IpsecTunHistIndex_Type = Integer32
_IpsecTunHistIndex_Object = MibTableColumn
ipsecTunHistIndex = _IpsecTunHistIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 4, 3, 1, 1, 1),
    _IpsecTunHistIndex_Type()
)
ipsecTunHistIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipsecTunHistIndex.setStatus("current")


class _IpsecTunHistTermReason_Type(Integer32):
    """Custom type ipsecTunHistTermReason based on Integer32"""
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
        *(("normal", 2),
          ("operRequest", 3),
          ("other", 1),
          ("peerDelRequest", 4),
          ("peerLost", 5),
          ("seqNumRollOver", 6))
    )


_IpsecTunHistTermReason_Type.__name__ = "Integer32"
_IpsecTunHistTermReason_Object = MibTableColumn
ipsecTunHistTermReason = _IpsecTunHistTermReason_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 4, 3, 1, 1, 2),
    _IpsecTunHistTermReason_Type()
)
ipsecTunHistTermReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTunHistTermReason.setStatus("current")
_IpsecTunHistActiveIndex_Type = Integer32
_IpsecTunHistActiveIndex_Object = MibTableColumn
ipsecTunHistActiveIndex = _IpsecTunHistActiveIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 4, 3, 1, 1, 3),
    _IpsecTunHistActiveIndex_Type()
)
ipsecTunHistActiveIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTunHistActiveIndex.setStatus("current")
_IpsecTunHistIkeTunnelIndex_Type = Integer32
_IpsecTunHistIkeTunnelIndex_Object = MibTableColumn
ipsecTunHistIkeTunnelIndex = _IpsecTunHistIkeTunnelIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 4, 3, 1, 1, 4),
    _IpsecTunHistIkeTunnelIndex_Type()
)
ipsecTunHistIkeTunnelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTunHistIkeTunnelIndex.setStatus("current")
_IpsecTunHistLocalAddr_Type = IPSIpAddress
_IpsecTunHistLocalAddr_Object = MibTableColumn
ipsecTunHistLocalAddr = _IpsecTunHistLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 4, 3, 1, 1, 5),
    _IpsecTunHistLocalAddr_Type()
)
ipsecTunHistLocalAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTunHistLocalAddr.setStatus("current")
_IpsecTunHistRemoteAddr_Type = IPSIpAddress
_IpsecTunHistRemoteAddr_Object = MibTableColumn
ipsecTunHistRemoteAddr = _IpsecTunHistRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 4, 3, 1, 1, 6),
    _IpsecTunHistRemoteAddr_Type()
)
ipsecTunHistRemoteAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTunHistRemoteAddr.setStatus("current")
_IpsecTunHistKeyType_Type = KeyType
_IpsecTunHistKeyType_Object = MibTableColumn
ipsecTunHistKeyType = _IpsecTunHistKeyType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 4, 3, 1, 1, 7),
    _IpsecTunHistKeyType_Type()
)
ipsecTunHistKeyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTunHistKeyType.setStatus("current")
_IpsecTunHistEncapMode_Type = EncapMode
_IpsecTunHistEncapMode_Object = MibTableColumn
ipsecTunHistEncapMode = _IpsecTunHistEncapMode_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 4, 3, 1, 1, 8),
    _IpsecTunHistEncapMode_Type()
)
ipsecTunHistEncapMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTunHistEncapMode.setStatus("current")
_IpsecTunHistLifeSize_Type = Integer32
_IpsecTunHistLifeSize_Object = MibTableColumn
ipsecTunHistLifeSize = _IpsecTunHistLifeSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 4, 3, 1, 1, 9),
    _IpsecTunHistLifeSize_Type()
)
ipsecTunHistLifeSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTunHistLifeSize.setStatus("current")
_IpsecTunHistLifeTime_Type = Integer32
_IpsecTunHistLifeTime_Object = MibTableColumn
ipsecTunHistLifeTime = _IpsecTunHistLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 4, 3, 1, 1, 10),
    _IpsecTunHistLifeTime_Type()
)
ipsecTunHistLifeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTunHistLifeTime.setStatus("current")
_IpsecTunHistStartTime_Type = TimeStamp
_IpsecTunHistStartTime_Object = MibTableColumn
ipsecTunHistStartTime = _IpsecTunHistStartTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 4, 3, 1, 1, 11),
    _IpsecTunHistStartTime_Type()
)
ipsecTunHistStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTunHistStartTime.setStatus("current")
_IpsecTunHistActiveTime_Type = TimeInterval
_IpsecTunHistActiveTime_Object = MibTableColumn
ipsecTunHistActiveTime = _IpsecTunHistActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 4, 3, 1, 1, 12),
    _IpsecTunHistActiveTime_Type()
)
ipsecTunHistActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTunHistActiveTime.setStatus("current")
_IpsecTunHistTotalRefreshes_Type = Counter32
_IpsecTunHistTotalRefreshes_Object = MibTableColumn
ipsecTunHistTotalRefreshes = _IpsecTunHistTotalRefreshes_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 4, 3, 1, 1, 13),
    _IpsecTunHistTotalRefreshes_Type()
)
ipsecTunHistTotalRefreshes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTunHistTotalRefreshes.setStatus("current")
_IpsecTunHistTotalSas_Type = Counter32
_IpsecTunHistTotalSas_Object = MibTableColumn
ipsecTunHistTotalSas = _IpsecTunHistTotalSas_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 4, 3, 1, 1, 14),
    _IpsecTunHistTotalSas_Type()
)
ipsecTunHistTotalSas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTunHistTotalSas.setStatus("current")
_IpsecTunHistInSaDiffHellmanGrp_Type = DiffHellmanGrp
_IpsecTunHistInSaDiffHellmanGrp_Object = MibTableColumn
ipsecTunHistInSaDiffHellmanGrp = _IpsecTunHistInSaDiffHellmanGrp_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 4, 3, 1, 1, 15),
    _IpsecTunHistInSaDiffHellmanGrp_Type()
)
ipsecTunHistInSaDiffHellmanGrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTunHistInSaDiffHellmanGrp.setStatus("current")
_IpsecTunHistInSaEncryptAlgo_Type = EncryptAlgo
_IpsecTunHistInSaEncryptAlgo_Object = MibTableColumn
ipsecTunHistInSaEncryptAlgo = _IpsecTunHistInSaEncryptAlgo_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 4, 3, 1, 1, 16),
    _IpsecTunHistInSaEncryptAlgo_Type()
)
ipsecTunHistInSaEncryptAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTunHistInSaEncryptAlgo.setStatus("current")
_IpsecTunHistInSaAhAuthAlgo_Type = AuthAlgo
_IpsecTunHistInSaAhAuthAlgo_Object = MibTableColumn
ipsecTunHistInSaAhAuthAlgo = _IpsecTunHistInSaAhAuthAlgo_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 4, 3, 1, 1, 17),
    _IpsecTunHistInSaAhAuthAlgo_Type()
)
ipsecTunHistInSaAhAuthAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTunHistInSaAhAuthAlgo.setStatus("current")
_IpsecTunHistInSaEspAuthAlgo_Type = AuthAlgo
_IpsecTunHistInSaEspAuthAlgo_Object = MibTableColumn
ipsecTunHistInSaEspAuthAlgo = _IpsecTunHistInSaEspAuthAlgo_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 4, 3, 1, 1, 18),
    _IpsecTunHistInSaEspAuthAlgo_Type()
)
ipsecTunHistInSaEspAuthAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTunHistInSaEspAuthAlgo.setStatus("current")
_IpsecTunHistInSaDecompAlgo_Type = CompAlgo
_IpsecTunHistInSaDecompAlgo_Object = MibTableColumn
ipsecTunHistInSaDecompAlgo = _IpsecTunHistInSaDecompAlgo_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 4, 3, 1, 1, 19),
    _IpsecTunHistInSaDecompAlgo_Type()
)
ipsecTunHistInSaDecompAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTunHistInSaDecompAlgo.setStatus("current")
_IpsecTunHistOutSaDiffHellmanGrp_Type = DiffHellmanGrp
_IpsecTunHistOutSaDiffHellmanGrp_Object = MibTableColumn
ipsecTunHistOutSaDiffHellmanGrp = _IpsecTunHistOutSaDiffHellmanGrp_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 4, 3, 1, 1, 20),
    _IpsecTunHistOutSaDiffHellmanGrp_Type()
)
ipsecTunHistOutSaDiffHellmanGrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTunHistOutSaDiffHellmanGrp.setStatus("current")
_IpsecTunHistOutSaEncryptAlgo_Type = EncryptAlgo
_IpsecTunHistOutSaEncryptAlgo_Object = MibTableColumn
ipsecTunHistOutSaEncryptAlgo = _IpsecTunHistOutSaEncryptAlgo_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 4, 3, 1, 1, 21),
    _IpsecTunHistOutSaEncryptAlgo_Type()
)
ipsecTunHistOutSaEncryptAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTunHistOutSaEncryptAlgo.setStatus("current")
_IpsecTunHistOutSaAhAuthAlgo_Type = AuthAlgo
_IpsecTunHistOutSaAhAuthAlgo_Object = MibTableColumn
ipsecTunHistOutSaAhAuthAlgo = _IpsecTunHistOutSaAhAuthAlgo_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 4, 3, 1, 1, 22),
    _IpsecTunHistOutSaAhAuthAlgo_Type()
)
ipsecTunHistOutSaAhAuthAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTunHistOutSaAhAuthAlgo.setStatus("current")
_IpsecTunHistOutSaEspAuthAlgo_Type = AuthAlgo
_IpsecTunHistOutSaEspAuthAlgo_Object = MibTableColumn
ipsecTunHistOutSaEspAuthAlgo = _IpsecTunHistOutSaEspAuthAlgo_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 4, 3, 1, 1, 23),
    _IpsecTunHistOutSaEspAuthAlgo_Type()
)
ipsecTunHistOutSaEspAuthAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTunHistOutSaEspAuthAlgo.setStatus("current")
_IpsecTunHistOutSaCompAlgo_Type = CompAlgo
_IpsecTunHistOutSaCompAlgo_Object = MibTableColumn
ipsecTunHistOutSaCompAlgo = _IpsecTunHistOutSaCompAlgo_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 4, 3, 1, 1, 24),
    _IpsecTunHistOutSaCompAlgo_Type()
)
ipsecTunHistOutSaCompAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTunHistOutSaCompAlgo.setStatus("current")
_IpsecTunHistInOctets_Type = Counter32
_IpsecTunHistInOctets_Object = MibTableColumn
ipsecTunHistInOctets = _IpsecTunHistInOctets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 4, 3, 1, 1, 25),
    _IpsecTunHistInOctets_Type()
)
ipsecTunHistInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTunHistInOctets.setStatus("current")
_IpsecTunHistHcInOctets_Type = Counter64
_IpsecTunHistHcInOctets_Object = MibTableColumn
ipsecTunHistHcInOctets = _IpsecTunHistHcInOctets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 4, 3, 1, 1, 26),
    _IpsecTunHistHcInOctets_Type()
)
ipsecTunHistHcInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTunHistHcInOctets.setStatus("current")
_IpsecTunHistInOctWraps_Type = Counter32
_IpsecTunHistInOctWraps_Object = MibTableColumn
ipsecTunHistInOctWraps = _IpsecTunHistInOctWraps_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 4, 3, 1, 1, 27),
    _IpsecTunHistInOctWraps_Type()
)
ipsecTunHistInOctWraps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTunHistInOctWraps.setStatus("current")
_IpsecTunHistInDecompOctets_Type = Counter32
_IpsecTunHistInDecompOctets_Object = MibTableColumn
ipsecTunHistInDecompOctets = _IpsecTunHistInDecompOctets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 4, 3, 1, 1, 28),
    _IpsecTunHistInDecompOctets_Type()
)
ipsecTunHistInDecompOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTunHistInDecompOctets.setStatus("current")
_IpsecTunHistHcInDecompOctets_Type = Counter64
_IpsecTunHistHcInDecompOctets_Object = MibTableColumn
ipsecTunHistHcInDecompOctets = _IpsecTunHistHcInDecompOctets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 4, 3, 1, 1, 29),
    _IpsecTunHistHcInDecompOctets_Type()
)
ipsecTunHistHcInDecompOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTunHistHcInDecompOctets.setStatus("current")
_IpsecTunHistInDecompOctWraps_Type = Counter32
_IpsecTunHistInDecompOctWraps_Object = MibTableColumn
ipsecTunHistInDecompOctWraps = _IpsecTunHistInDecompOctWraps_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 4, 3, 1, 1, 30),
    _IpsecTunHistInDecompOctWraps_Type()
)
ipsecTunHistInDecompOctWraps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTunHistInDecompOctWraps.setStatus("current")
_IpsecTunHistInPkts_Type = Counter32
_IpsecTunHistInPkts_Object = MibTableColumn
ipsecTunHistInPkts = _IpsecTunHistInPkts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 4, 3, 1, 1, 31),
    _IpsecTunHistInPkts_Type()
)
ipsecTunHistInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTunHistInPkts.setStatus("current")
_IpsecTunHistInDropPkts_Type = Counter32
_IpsecTunHistInDropPkts_Object = MibTableColumn
ipsecTunHistInDropPkts = _IpsecTunHistInDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 4, 3, 1, 1, 32),
    _IpsecTunHistInDropPkts_Type()
)
ipsecTunHistInDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTunHistInDropPkts.setStatus("current")
_IpsecTunHistInReplayDropPkts_Type = Counter32
_IpsecTunHistInReplayDropPkts_Object = MibTableColumn
ipsecTunHistInReplayDropPkts = _IpsecTunHistInReplayDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 4, 3, 1, 1, 33),
    _IpsecTunHistInReplayDropPkts_Type()
)
ipsecTunHistInReplayDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTunHistInReplayDropPkts.setStatus("current")
_IpsecTunHistInAuths_Type = Counter32
_IpsecTunHistInAuths_Object = MibTableColumn
ipsecTunHistInAuths = _IpsecTunHistInAuths_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 4, 3, 1, 1, 34),
    _IpsecTunHistInAuths_Type()
)
ipsecTunHistInAuths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTunHistInAuths.setStatus("current")
_IpsecTunHistInAuthFails_Type = Counter32
_IpsecTunHistInAuthFails_Object = MibTableColumn
ipsecTunHistInAuthFails = _IpsecTunHistInAuthFails_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 4, 3, 1, 1, 35),
    _IpsecTunHistInAuthFails_Type()
)
ipsecTunHistInAuthFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTunHistInAuthFails.setStatus("current")
_IpsecTunHistInDecrypts_Type = Counter32
_IpsecTunHistInDecrypts_Object = MibTableColumn
ipsecTunHistInDecrypts = _IpsecTunHistInDecrypts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 4, 3, 1, 1, 36),
    _IpsecTunHistInDecrypts_Type()
)
ipsecTunHistInDecrypts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTunHistInDecrypts.setStatus("current")
_IpsecTunHistInDecryptFails_Type = Counter32
_IpsecTunHistInDecryptFails_Object = MibTableColumn
ipsecTunHistInDecryptFails = _IpsecTunHistInDecryptFails_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 4, 3, 1, 1, 37),
    _IpsecTunHistInDecryptFails_Type()
)
ipsecTunHistInDecryptFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTunHistInDecryptFails.setStatus("current")
_IpsecTunHistOutOctets_Type = Counter32
_IpsecTunHistOutOctets_Object = MibTableColumn
ipsecTunHistOutOctets = _IpsecTunHistOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 4, 3, 1, 1, 38),
    _IpsecTunHistOutOctets_Type()
)
ipsecTunHistOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTunHistOutOctets.setStatus("current")
_IpsecTunHistHcOutOctets_Type = Counter64
_IpsecTunHistHcOutOctets_Object = MibTableColumn
ipsecTunHistHcOutOctets = _IpsecTunHistHcOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 4, 3, 1, 1, 39),
    _IpsecTunHistHcOutOctets_Type()
)
ipsecTunHistHcOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTunHistHcOutOctets.setStatus("current")
_IpsecTunHistOutOctWraps_Type = Counter32
_IpsecTunHistOutOctWraps_Object = MibTableColumn
ipsecTunHistOutOctWraps = _IpsecTunHistOutOctWraps_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 4, 3, 1, 1, 40),
    _IpsecTunHistOutOctWraps_Type()
)
ipsecTunHistOutOctWraps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTunHistOutOctWraps.setStatus("current")
_IpsecTunHistOutUncompOctets_Type = Counter32
_IpsecTunHistOutUncompOctets_Object = MibTableColumn
ipsecTunHistOutUncompOctets = _IpsecTunHistOutUncompOctets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 4, 3, 1, 1, 41),
    _IpsecTunHistOutUncompOctets_Type()
)
ipsecTunHistOutUncompOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTunHistOutUncompOctets.setStatus("current")
_IpsecTunHistHcOutUncompOctets_Type = Counter64
_IpsecTunHistHcOutUncompOctets_Object = MibTableColumn
ipsecTunHistHcOutUncompOctets = _IpsecTunHistHcOutUncompOctets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 4, 3, 1, 1, 42),
    _IpsecTunHistHcOutUncompOctets_Type()
)
ipsecTunHistHcOutUncompOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTunHistHcOutUncompOctets.setStatus("current")
_IpsecTunHistOutUncompOctWraps_Type = Counter32
_IpsecTunHistOutUncompOctWraps_Object = MibTableColumn
ipsecTunHistOutUncompOctWraps = _IpsecTunHistOutUncompOctWraps_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 4, 3, 1, 1, 43),
    _IpsecTunHistOutUncompOctWraps_Type()
)
ipsecTunHistOutUncompOctWraps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTunHistOutUncompOctWraps.setStatus("current")
_IpsecTunHistOutPkts_Type = Counter32
_IpsecTunHistOutPkts_Object = MibTableColumn
ipsecTunHistOutPkts = _IpsecTunHistOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 4, 3, 1, 1, 44),
    _IpsecTunHistOutPkts_Type()
)
ipsecTunHistOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTunHistOutPkts.setStatus("current")
_IpsecTunHistOutDropPkts_Type = Counter32
_IpsecTunHistOutDropPkts_Object = MibTableColumn
ipsecTunHistOutDropPkts = _IpsecTunHistOutDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 4, 3, 1, 1, 45),
    _IpsecTunHistOutDropPkts_Type()
)
ipsecTunHistOutDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTunHistOutDropPkts.setStatus("current")
_IpsecTunHistOutAuths_Type = Counter32
_IpsecTunHistOutAuths_Object = MibTableColumn
ipsecTunHistOutAuths = _IpsecTunHistOutAuths_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 4, 3, 1, 1, 46),
    _IpsecTunHistOutAuths_Type()
)
ipsecTunHistOutAuths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTunHistOutAuths.setStatus("current")
_IpsecTunHistOutAuthFails_Type = Counter32
_IpsecTunHistOutAuthFails_Object = MibTableColumn
ipsecTunHistOutAuthFails = _IpsecTunHistOutAuthFails_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 4, 3, 1, 1, 47),
    _IpsecTunHistOutAuthFails_Type()
)
ipsecTunHistOutAuthFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTunHistOutAuthFails.setStatus("current")
_IpsecTunHistOutEncrypts_Type = Counter32
_IpsecTunHistOutEncrypts_Object = MibTableColumn
ipsecTunHistOutEncrypts = _IpsecTunHistOutEncrypts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 4, 3, 1, 1, 48),
    _IpsecTunHistOutEncrypts_Type()
)
ipsecTunHistOutEncrypts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTunHistOutEncrypts.setStatus("current")
_IpsecTunHistOutEncryptFails_Type = Counter32
_IpsecTunHistOutEncryptFails_Object = MibTableColumn
ipsecTunHistOutEncryptFails = _IpsecTunHistOutEncryptFails_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 4, 3, 1, 1, 49),
    _IpsecTunHistOutEncryptFails_Type()
)
ipsecTunHistOutEncryptFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTunHistOutEncryptFails.setStatus("current")
_IpsecEndPtHistTable_Object = MibTable
ipsecEndPtHistTable = _IpsecEndPtHistTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 4, 3, 2)
)
if mibBuilder.loadTexts:
    ipsecEndPtHistTable.setStatus("current")
_IpsecEndPtHistEntry_Object = MibTableRow
ipsecEndPtHistEntry = _IpsecEndPtHistEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 4, 3, 2, 1)
)
ipsecEndPtHistEntry.setIndexNames(
    (0, "IPsecT1-MIB", "ipsecEndPtHistIndex"),
)
if mibBuilder.loadTexts:
    ipsecEndPtHistEntry.setStatus("current")
_IpsecEndPtHistIndex_Type = Integer32
_IpsecEndPtHistIndex_Object = MibTableColumn
ipsecEndPtHistIndex = _IpsecEndPtHistIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 4, 3, 2, 1, 1),
    _IpsecEndPtHistIndex_Type()
)
ipsecEndPtHistIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipsecEndPtHistIndex.setStatus("current")
_IpsecEndPtHistTunIndex_Type = Integer32
_IpsecEndPtHistTunIndex_Object = MibTableColumn
ipsecEndPtHistTunIndex = _IpsecEndPtHistTunIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 4, 3, 2, 1, 2),
    _IpsecEndPtHistTunIndex_Type()
)
ipsecEndPtHistTunIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecEndPtHistTunIndex.setStatus("current")
_IpsecEndPtHistActiveIndex_Type = Integer32
_IpsecEndPtHistActiveIndex_Object = MibTableColumn
ipsecEndPtHistActiveIndex = _IpsecEndPtHistActiveIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 4, 3, 2, 1, 3),
    _IpsecEndPtHistActiveIndex_Type()
)
ipsecEndPtHistActiveIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecEndPtHistActiveIndex.setStatus("current")
_IpsecEndPtHistLocalName_Type = DisplayString
_IpsecEndPtHistLocalName_Object = MibTableColumn
ipsecEndPtHistLocalName = _IpsecEndPtHistLocalName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 4, 3, 2, 1, 4),
    _IpsecEndPtHistLocalName_Type()
)
ipsecEndPtHistLocalName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecEndPtHistLocalName.setStatus("current")


class _IpsecEndPtHistLocalType_Type(Integer32):
    """Custom type ipsecEndPtHistLocalType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ipAddrRange", 2),
          ("ipSubnet", 3),
          ("singleIpAddr", 1))
    )


_IpsecEndPtHistLocalType_Type.__name__ = "Integer32"
_IpsecEndPtHistLocalType_Object = MibTableColumn
ipsecEndPtHistLocalType = _IpsecEndPtHistLocalType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 4, 3, 2, 1, 5),
    _IpsecEndPtHistLocalType_Type()
)
ipsecEndPtHistLocalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecEndPtHistLocalType.setStatus("current")
_IpsecEndPtHistLocalAddr1_Type = IPSIpAddress
_IpsecEndPtHistLocalAddr1_Object = MibTableColumn
ipsecEndPtHistLocalAddr1 = _IpsecEndPtHistLocalAddr1_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 4, 3, 2, 1, 6),
    _IpsecEndPtHistLocalAddr1_Type()
)
ipsecEndPtHistLocalAddr1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecEndPtHistLocalAddr1.setStatus("current")
_IpsecEndPtHistLocalAddr2_Type = IPSIpAddress
_IpsecEndPtHistLocalAddr2_Object = MibTableColumn
ipsecEndPtHistLocalAddr2 = _IpsecEndPtHistLocalAddr2_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 4, 3, 2, 1, 7),
    _IpsecEndPtHistLocalAddr2_Type()
)
ipsecEndPtHistLocalAddr2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecEndPtHistLocalAddr2.setStatus("current")


class _IpsecEndPtHistLocalProtocol_Type(Integer32):
    """Custom type ipsecEndPtHistLocalProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_IpsecEndPtHistLocalProtocol_Type.__name__ = "Integer32"
_IpsecEndPtHistLocalProtocol_Object = MibTableColumn
ipsecEndPtHistLocalProtocol = _IpsecEndPtHistLocalProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 4, 3, 2, 1, 8),
    _IpsecEndPtHistLocalProtocol_Type()
)
ipsecEndPtHistLocalProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecEndPtHistLocalProtocol.setStatus("current")


class _IpsecEndPtHistLocalPort_Type(Integer32):
    """Custom type ipsecEndPtHistLocalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpsecEndPtHistLocalPort_Type.__name__ = "Integer32"
_IpsecEndPtHistLocalPort_Object = MibTableColumn
ipsecEndPtHistLocalPort = _IpsecEndPtHistLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 4, 3, 2, 1, 9),
    _IpsecEndPtHistLocalPort_Type()
)
ipsecEndPtHistLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecEndPtHistLocalPort.setStatus("current")
_IpsecEndPtHistRemoteName_Type = DisplayString
_IpsecEndPtHistRemoteName_Object = MibTableColumn
ipsecEndPtHistRemoteName = _IpsecEndPtHistRemoteName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 4, 3, 2, 1, 10),
    _IpsecEndPtHistRemoteName_Type()
)
ipsecEndPtHistRemoteName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecEndPtHistRemoteName.setStatus("current")


class _IpsecEndPtHistRemoteType_Type(Integer32):
    """Custom type ipsecEndPtHistRemoteType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ipAddrRange", 2),
          ("ipSubnet", 3),
          ("singleIpAddr", 1))
    )


_IpsecEndPtHistRemoteType_Type.__name__ = "Integer32"
_IpsecEndPtHistRemoteType_Object = MibTableColumn
ipsecEndPtHistRemoteType = _IpsecEndPtHistRemoteType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 4, 3, 2, 1, 11),
    _IpsecEndPtHistRemoteType_Type()
)
ipsecEndPtHistRemoteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecEndPtHistRemoteType.setStatus("current")
_IpsecEndPtHistRemoteAddr1_Type = IPSIpAddress
_IpsecEndPtHistRemoteAddr1_Object = MibTableColumn
ipsecEndPtHistRemoteAddr1 = _IpsecEndPtHistRemoteAddr1_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 4, 3, 2, 1, 12),
    _IpsecEndPtHistRemoteAddr1_Type()
)
ipsecEndPtHistRemoteAddr1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecEndPtHistRemoteAddr1.setStatus("current")
_IpsecEndPtHistRemoteAddr2_Type = IPSIpAddress
_IpsecEndPtHistRemoteAddr2_Object = MibTableColumn
ipsecEndPtHistRemoteAddr2 = _IpsecEndPtHistRemoteAddr2_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 4, 3, 2, 1, 13),
    _IpsecEndPtHistRemoteAddr2_Type()
)
ipsecEndPtHistRemoteAddr2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecEndPtHistRemoteAddr2.setStatus("current")


class _IpsecEndPtHistRemoteProtocol_Type(Integer32):
    """Custom type ipsecEndPtHistRemoteProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_IpsecEndPtHistRemoteProtocol_Type.__name__ = "Integer32"
_IpsecEndPtHistRemoteProtocol_Object = MibTableColumn
ipsecEndPtHistRemoteProtocol = _IpsecEndPtHistRemoteProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 4, 3, 2, 1, 14),
    _IpsecEndPtHistRemoteProtocol_Type()
)
ipsecEndPtHistRemoteProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecEndPtHistRemoteProtocol.setStatus("current")


class _IpsecEndPtHistRemotePort_Type(Integer32):
    """Custom type ipsecEndPtHistRemotePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpsecEndPtHistRemotePort_Type.__name__ = "Integer32"
_IpsecEndPtHistRemotePort_Object = MibTableColumn
ipsecEndPtHistRemotePort = _IpsecEndPtHistRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 4, 3, 2, 1, 15),
    _IpsecEndPtHistRemotePort_Type()
)
ipsecEndPtHistRemotePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecEndPtHistRemotePort.setStatus("current")
_IpsecFailures_ObjectIdentity = ObjectIdentity
ipsecFailures = _IpsecFailures_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 5)
)
_IpsecFailGlobal_ObjectIdentity = ObjectIdentity
ipsecFailGlobal = _IpsecFailGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 5, 1)
)
_IpsecFailGlobalCntl_ObjectIdentity = ObjectIdentity
ipsecFailGlobalCntl = _IpsecFailGlobalCntl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 5, 1, 1)
)
_IpsecFailTableSize_Type = Integer32
_IpsecFailTableSize_Object = MibScalar
ipsecFailTableSize = _IpsecFailTableSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 5, 1, 1, 1),
    _IpsecFailTableSize_Type()
)
ipsecFailTableSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecFailTableSize.setStatus("current")
_IpsecFailPhaseOne_ObjectIdentity = ObjectIdentity
ipsecFailPhaseOne = _IpsecFailPhaseOne_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 5, 2)
)
_IkeFailTable_Object = MibTable
ikeFailTable = _IkeFailTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 5, 2, 1)
)
if mibBuilder.loadTexts:
    ikeFailTable.setStatus("current")
_IkeFailEntry_Object = MibTableRow
ikeFailEntry = _IkeFailEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 5, 2, 1, 1)
)
ikeFailEntry.setIndexNames(
    (0, "IPsecT1-MIB", "ikeFailIndex"),
)
if mibBuilder.loadTexts:
    ikeFailEntry.setStatus("current")
_IkeFailIndex_Type = Integer32
_IkeFailIndex_Object = MibTableColumn
ikeFailIndex = _IkeFailIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 5, 2, 1, 1, 1),
    _IkeFailIndex_Type()
)
ikeFailIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ikeFailIndex.setStatus("current")


class _IkeFailReason_Type(Integer32):
    """Custom type ikeFailReason based on Integer32"""
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
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18)
        )
    )
    namedValues = NamedValues(
        *(("authFailure", 6),
          ("crlFailure", 15),
          ("encryptFailure", 8),
          ("hashValidation", 7),
          ("internalError", 9),
          ("localCertExpired", 14),
          ("localFailure", 4),
          ("nonExistentSa", 17),
          ("operRequest", 18),
          ("other", 1),
          ("peerCertNotValid", 13),
          ("peerCertUnavailable", 12),
          ("peerDelRequest", 2),
          ("peerEncodingError", 16),
          ("peerLost", 3),
          ("proposalFailure", 11),
          ("seqNumRollOver", 5),
          ("sysCapExceeded", 10))
    )


_IkeFailReason_Type.__name__ = "Integer32"
_IkeFailReason_Object = MibTableColumn
ikeFailReason = _IkeFailReason_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 5, 2, 1, 1, 2),
    _IkeFailReason_Type()
)
ikeFailReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeFailReason.setStatus("current")
_IkeFailTime_Type = TimeStamp
_IkeFailTime_Object = MibTableColumn
ikeFailTime = _IkeFailTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 5, 2, 1, 1, 3),
    _IkeFailTime_Type()
)
ikeFailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeFailTime.setStatus("current")
_IkeFailLocalType_Type = IkePeerType
_IkeFailLocalType_Object = MibTableColumn
ikeFailLocalType = _IkeFailLocalType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 5, 2, 1, 1, 4),
    _IkeFailLocalType_Type()
)
ikeFailLocalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeFailLocalType.setStatus("current")
_IkeFailLocalValue_Type = DisplayString
_IkeFailLocalValue_Object = MibTableColumn
ikeFailLocalValue = _IkeFailLocalValue_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 5, 2, 1, 1, 5),
    _IkeFailLocalValue_Type()
)
ikeFailLocalValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeFailLocalValue.setStatus("current")
_IkeFailRemoteType_Type = IkePeerType
_IkeFailRemoteType_Object = MibTableColumn
ikeFailRemoteType = _IkeFailRemoteType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 5, 2, 1, 1, 6),
    _IkeFailRemoteType_Type()
)
ikeFailRemoteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeFailRemoteType.setStatus("current")
_IkeFailRemoteValue_Type = DisplayString
_IkeFailRemoteValue_Object = MibTableColumn
ikeFailRemoteValue = _IkeFailRemoteValue_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 5, 2, 1, 1, 7),
    _IkeFailRemoteValue_Type()
)
ikeFailRemoteValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeFailRemoteValue.setStatus("current")
_IkeFailLocalAddr_Type = IPSIpAddress
_IkeFailLocalAddr_Object = MibTableColumn
ikeFailLocalAddr = _IkeFailLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 5, 2, 1, 1, 8),
    _IkeFailLocalAddr_Type()
)
ikeFailLocalAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeFailLocalAddr.setStatus("current")
_IkeFailRemoteAddr_Type = IPSIpAddress
_IkeFailRemoteAddr_Object = MibTableColumn
ikeFailRemoteAddr = _IkeFailRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 5, 2, 1, 1, 9),
    _IkeFailRemoteAddr_Type()
)
ikeFailRemoteAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeFailRemoteAddr.setStatus("current")
_IpsecFailPhaseTwo_ObjectIdentity = ObjectIdentity
ipsecFailPhaseTwo = _IpsecFailPhaseTwo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 5, 3)
)
_IpsecFailTable_Object = MibTable
ipsecFailTable = _IpsecFailTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 5, 3, 1)
)
if mibBuilder.loadTexts:
    ipsecFailTable.setStatus("current")
_IpsecFailEntry_Object = MibTableRow
ipsecFailEntry = _IpsecFailEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 5, 3, 1, 1)
)
ipsecFailEntry.setIndexNames(
    (0, "IPsecT1-MIB", "ipsecFailIndex"),
)
if mibBuilder.loadTexts:
    ipsecFailEntry.setStatus("current")
_IpsecFailIndex_Type = Integer32
_IpsecFailIndex_Object = MibTableColumn
ipsecFailIndex = _IpsecFailIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 5, 3, 1, 1, 1),
    _IpsecFailIndex_Type()
)
ipsecFailIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipsecFailIndex.setStatus("current")


class _IpsecFailReason_Type(Integer32):
    """Custom type ipsecFailReason based on Integer32"""
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
              10,
              11,
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("compression", 11),
          ("decryptFailure", 7),
          ("encryptFailure", 8),
          ("inAuthFailure", 9),
          ("internalError", 2),
          ("nonExistentSa", 6),
          ("operRequest", 16),
          ("other", 1),
          ("outAuthFailure", 10),
          ("peerDelRequest", 13),
          ("peerEncodingError", 3),
          ("peerLost", 14),
          ("proposalFailure", 4),
          ("protocolUseFail", 5),
          ("seqNumRollOver", 15),
          ("sysCapExceeded", 12))
    )


_IpsecFailReason_Type.__name__ = "Integer32"
_IpsecFailReason_Object = MibTableColumn
ipsecFailReason = _IpsecFailReason_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 5, 3, 1, 1, 2),
    _IpsecFailReason_Type()
)
ipsecFailReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecFailReason.setStatus("current")
_IpsecFailTime_Type = TimeStamp
_IpsecFailTime_Object = MibTableColumn
ipsecFailTime = _IpsecFailTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 5, 3, 1, 1, 3),
    _IpsecFailTime_Type()
)
ipsecFailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecFailTime.setStatus("current")


class _IpsecFailTunnelIndex_Type(Integer32):
    """Custom type ipsecFailTunnelIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpsecFailTunnelIndex_Type.__name__ = "Integer32"
_IpsecFailTunnelIndex_Object = MibTableColumn
ipsecFailTunnelIndex = _IpsecFailTunnelIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 5, 3, 1, 1, 4),
    _IpsecFailTunnelIndex_Type()
)
ipsecFailTunnelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecFailTunnelIndex.setStatus("current")
_IpsecFailSaSpi_Type = Integer32
_IpsecFailSaSpi_Object = MibTableColumn
ipsecFailSaSpi = _IpsecFailSaSpi_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 5, 3, 1, 1, 5),
    _IpsecFailSaSpi_Type()
)
ipsecFailSaSpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecFailSaSpi.setStatus("current")
_IpsecFailPktSrcAddr_Type = IPSIpAddress
_IpsecFailPktSrcAddr_Object = MibTableColumn
ipsecFailPktSrcAddr = _IpsecFailPktSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 5, 3, 1, 1, 6),
    _IpsecFailPktSrcAddr_Type()
)
ipsecFailPktSrcAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecFailPktSrcAddr.setStatus("current")
_IpsecFailPktDstAddr_Type = IPSIpAddress
_IpsecFailPktDstAddr_Object = MibTableColumn
ipsecFailPktDstAddr = _IpsecFailPktDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 5, 3, 1, 1, 7),
    _IpsecFailPktDstAddr_Type()
)
ipsecFailPktDstAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecFailPktDstAddr.setStatus("current")
_IpsecTrapCntl_ObjectIdentity = ObjectIdentity
ipsecTrapCntl = _IpsecTrapCntl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 6)
)


class _IpsecTrapCntlIkeTunnelStart_Type(TrapStatus):
    """Custom type ipsecTrapCntlIkeTunnelStart based on TrapStatus"""


_IpsecTrapCntlIkeTunnelStart_Object = MibScalar
ipsecTrapCntlIkeTunnelStart = _IpsecTrapCntlIkeTunnelStart_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 6, 1),
    _IpsecTrapCntlIkeTunnelStart_Type()
)
ipsecTrapCntlIkeTunnelStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecTrapCntlIkeTunnelStart.setStatus("current")


class _IpsecTrapCntlIkeTunnelStop_Type(TrapStatus):
    """Custom type ipsecTrapCntlIkeTunnelStop based on TrapStatus"""


_IpsecTrapCntlIkeTunnelStop_Object = MibScalar
ipsecTrapCntlIkeTunnelStop = _IpsecTrapCntlIkeTunnelStop_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 6, 2),
    _IpsecTrapCntlIkeTunnelStop_Type()
)
ipsecTrapCntlIkeTunnelStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecTrapCntlIkeTunnelStop.setStatus("current")


class _IpsecTrapCntlIkeSysFailure_Type(TrapStatus):
    """Custom type ipsecTrapCntlIkeSysFailure based on TrapStatus"""


_IpsecTrapCntlIkeSysFailure_Object = MibScalar
ipsecTrapCntlIkeSysFailure = _IpsecTrapCntlIkeSysFailure_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 6, 3),
    _IpsecTrapCntlIkeSysFailure_Type()
)
ipsecTrapCntlIkeSysFailure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecTrapCntlIkeSysFailure.setStatus("current")


class _IpsecTrapCntlIkeCertCrlFailure_Type(TrapStatus):
    """Custom type ipsecTrapCntlIkeCertCrlFailure based on TrapStatus"""


_IpsecTrapCntlIkeCertCrlFailure_Object = MibScalar
ipsecTrapCntlIkeCertCrlFailure = _IpsecTrapCntlIkeCertCrlFailure_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 6, 4),
    _IpsecTrapCntlIkeCertCrlFailure_Type()
)
ipsecTrapCntlIkeCertCrlFailure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecTrapCntlIkeCertCrlFailure.setStatus("current")


class _IpsecTrapCntlIkeProtocolFailure_Type(TrapStatus):
    """Custom type ipsecTrapCntlIkeProtocolFailure based on TrapStatus"""


_IpsecTrapCntlIkeProtocolFailure_Object = MibScalar
ipsecTrapCntlIkeProtocolFailure = _IpsecTrapCntlIkeProtocolFailure_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 6, 5),
    _IpsecTrapCntlIkeProtocolFailure_Type()
)
ipsecTrapCntlIkeProtocolFailure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecTrapCntlIkeProtocolFailure.setStatus("current")


class _IpsecTrapCntlIkeNoSa_Type(TrapStatus):
    """Custom type ipsecTrapCntlIkeNoSa based on TrapStatus"""


_IpsecTrapCntlIkeNoSa_Object = MibScalar
ipsecTrapCntlIkeNoSa = _IpsecTrapCntlIkeNoSa_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 6, 6),
    _IpsecTrapCntlIkeNoSa_Type()
)
ipsecTrapCntlIkeNoSa.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecTrapCntlIkeNoSa.setStatus("current")


class _IpsecTrapCntlipsecTunnelStart_Type(TrapStatus):
    """Custom type ipsecTrapCntlipsecTunnelStart based on TrapStatus"""


_IpsecTrapCntlipsecTunnelStart_Object = MibScalar
ipsecTrapCntlipsecTunnelStart = _IpsecTrapCntlipsecTunnelStart_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 6, 7),
    _IpsecTrapCntlipsecTunnelStart_Type()
)
ipsecTrapCntlipsecTunnelStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecTrapCntlipsecTunnelStart.setStatus("current")


class _IpsecTrapCntlipsecTunnelStop_Type(TrapStatus):
    """Custom type ipsecTrapCntlipsecTunnelStop based on TrapStatus"""


_IpsecTrapCntlipsecTunnelStop_Object = MibScalar
ipsecTrapCntlipsecTunnelStop = _IpsecTrapCntlipsecTunnelStop_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 6, 8),
    _IpsecTrapCntlipsecTunnelStop_Type()
)
ipsecTrapCntlipsecTunnelStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecTrapCntlipsecTunnelStop.setStatus("current")


class _IpsecTrapCntlipsecSysFailure_Type(TrapStatus):
    """Custom type ipsecTrapCntlipsecSysFailure based on TrapStatus"""


_IpsecTrapCntlipsecSysFailure_Object = MibScalar
ipsecTrapCntlipsecSysFailure = _IpsecTrapCntlipsecSysFailure_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 6, 9),
    _IpsecTrapCntlipsecSysFailure_Type()
)
ipsecTrapCntlipsecSysFailure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecTrapCntlipsecSysFailure.setStatus("current")


class _IpsecTrapCntlipsecSetUpFailure_Type(TrapStatus):
    """Custom type ipsecTrapCntlipsecSetUpFailure based on TrapStatus"""


_IpsecTrapCntlipsecSetUpFailure_Object = MibScalar
ipsecTrapCntlipsecSetUpFailure = _IpsecTrapCntlipsecSetUpFailure_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 6, 10),
    _IpsecTrapCntlipsecSetUpFailure_Type()
)
ipsecTrapCntlipsecSetUpFailure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecTrapCntlipsecSetUpFailure.setStatus("current")


class _IpsecTrapCntlipsecEarlyTunTerm_Type(TrapStatus):
    """Custom type ipsecTrapCntlipsecEarlyTunTerm based on TrapStatus"""


_IpsecTrapCntlipsecEarlyTunTerm_Object = MibScalar
ipsecTrapCntlipsecEarlyTunTerm = _IpsecTrapCntlipsecEarlyTunTerm_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 6, 11),
    _IpsecTrapCntlipsecEarlyTunTerm_Type()
)
ipsecTrapCntlipsecEarlyTunTerm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecTrapCntlipsecEarlyTunTerm.setStatus("current")


class _IpsecTrapCntlipsecProtocolFailure_Type(TrapStatus):
    """Custom type ipsecTrapCntlipsecProtocolFailure based on TrapStatus"""


_IpsecTrapCntlipsecProtocolFailure_Object = MibScalar
ipsecTrapCntlipsecProtocolFailure = _IpsecTrapCntlipsecProtocolFailure_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 6, 12),
    _IpsecTrapCntlipsecProtocolFailure_Type()
)
ipsecTrapCntlipsecProtocolFailure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecTrapCntlipsecProtocolFailure.setStatus("current")


class _IpsecTrapCntlipsecNoSa_Type(TrapStatus):
    """Custom type ipsecTrapCntlipsecNoSa based on TrapStatus"""


_IpsecTrapCntlipsecNoSa_Object = MibScalar
ipsecTrapCntlipsecNoSa = _IpsecTrapCntlipsecNoSa_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 1, 6, 13),
    _IpsecTrapCntlipsecNoSa_Type()
)
ipsecTrapCntlipsecNoSa.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecTrapCntlipsecNoSa.setStatus("current")
_IpsecMIBConformance_ObjectIdentity = ObjectIdentity
ipsecMIBConformance = _IpsecMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 2)
)
_IpsecMIBGroups_ObjectIdentity = ObjectIdentity
ipsecMIBGroups = _IpsecMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 2, 1)
)
_IpsecMIBCompliances_ObjectIdentity = ObjectIdentity
ipsecMIBCompliances = _IpsecMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 2, 2)
)

# Managed Objects groups

ipsecLevelsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 2, 1, 1)
)
ipsecLevelsGroup.setObjects(
    ("IPsecT1-MIB", "ipsecMibLevel")
)
if mibBuilder.loadTexts:
    ipsecLevelsGroup.setStatus("current")

ipsecPhaseOneGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 2, 1, 2)
)
ipsecPhaseOneGroup.setObjects(
      *(("IPsecT1-MIB", "ikeGlobalActiveTunnels"),
        ("IPsecT1-MIB", "ikeGlobalPreviousTunnels"),
        ("IPsecT1-MIB", "ikeGlobalInOctets"),
        ("IPsecT1-MIB", "ikeGlobalInPkts"),
        ("IPsecT1-MIB", "ikeGlobalInDropPkts"),
        ("IPsecT1-MIB", "ikeGlobalInNotifys"),
        ("IPsecT1-MIB", "ikeGlobalInP2Exchgs"),
        ("IPsecT1-MIB", "ikeGlobalInP2ExchgInvalids"),
        ("IPsecT1-MIB", "ikeGlobalInP2ExchgRejects"),
        ("IPsecT1-MIB", "ikeGlobalInP2SaDelRequests"),
        ("IPsecT1-MIB", "ikeGlobalOutOctets"),
        ("IPsecT1-MIB", "ikeGlobalOutPkts"),
        ("IPsecT1-MIB", "ikeGlobalOutDropPkts"),
        ("IPsecT1-MIB", "ikeGlobalOutNotifys"),
        ("IPsecT1-MIB", "ikeGlobalOutP2Exchgs"),
        ("IPsecT1-MIB", "ikeGlobalOutP2ExchgInvalids"),
        ("IPsecT1-MIB", "ikeGlobalOutP2ExchgRejects"),
        ("IPsecT1-MIB", "ikeGlobalOutP2SaDelRequests"),
        ("IPsecT1-MIB", "ikeGlobalInitTunnels"),
        ("IPsecT1-MIB", "ikeGlobalInitTunnelFails"),
        ("IPsecT1-MIB", "ikeGlobalRespTunnelFails"),
        ("IPsecT1-MIB", "ikeGlobalSysCapFails"),
        ("IPsecT1-MIB", "ikeGlobalAuthFails"),
        ("IPsecT1-MIB", "ikeGlobalDecryptFails"),
        ("IPsecT1-MIB", "ikeGlobalHashValidFails"),
        ("IPsecT1-MIB", "ikeGlobalNoSaFails"),
        ("IPsecT1-MIB", "ikePeerLocalAddr"),
        ("IPsecT1-MIB", "ikePeerRemoteAddr"),
        ("IPsecT1-MIB", "ikePeerActiveTime"),
        ("IPsecT1-MIB", "ikePeerActiveTunnelIndex"),
        ("IPsecT1-MIB", "ikeTunLocalType"),
        ("IPsecT1-MIB", "ikeTunLocalValue"),
        ("IPsecT1-MIB", "ikeTunLocalAddr"),
        ("IPsecT1-MIB", "ikeTunLocalName"),
        ("IPsecT1-MIB", "ikeTunRemoteType"),
        ("IPsecT1-MIB", "ikeTunRemoteValue"),
        ("IPsecT1-MIB", "ikeTunRemoteAddr"),
        ("IPsecT1-MIB", "ikeTunRemoteName"),
        ("IPsecT1-MIB", "ikeTunNegoMode"),
        ("IPsecT1-MIB", "ikeTunDiffHellmanGrp"),
        ("IPsecT1-MIB", "ikeTunEncryptAlgo"),
        ("IPsecT1-MIB", "ikeTunHashAlgo"),
        ("IPsecT1-MIB", "ikeTunAuthMethod"),
        ("IPsecT1-MIB", "ikeTunLifeTime"),
        ("IPsecT1-MIB", "ikeTunActiveTime"),
        ("IPsecT1-MIB", "ikeTunSaRefreshThreshold"),
        ("IPsecT1-MIB", "ikeTunTotalRefreshes"),
        ("IPsecT1-MIB", "ikeTunInOctets"),
        ("IPsecT1-MIB", "ikeTunInPkts"),
        ("IPsecT1-MIB", "ikeTunInDropPkts"),
        ("IPsecT1-MIB", "ikeTunInNotifys"),
        ("IPsecT1-MIB", "ikeTunInP2Exchgs"),
        ("IPsecT1-MIB", "ikeTunInP2ExchgInvalids"),
        ("IPsecT1-MIB", "ikeTunInP2ExchgRejects"),
        ("IPsecT1-MIB", "ikeTunInP2SaDelRequests"),
        ("IPsecT1-MIB", "ikeTunOutOctets"),
        ("IPsecT1-MIB", "ikeTunOutPkts"),
        ("IPsecT1-MIB", "ikeTunOutDropPkts"),
        ("IPsecT1-MIB", "ikeTunOutNotifys"),
        ("IPsecT1-MIB", "ikeTunOutP2Exchgs"),
        ("IPsecT1-MIB", "ikeTunOutP2ExchgInvalids"),
        ("IPsecT1-MIB", "ikeTunOutP2ExchgRejects"),
        ("IPsecT1-MIB", "ikeTunOutP2SaDelRequests"),
        ("IPsecT1-MIB", "ikeTunStatus"),
        ("IPsecT1-MIB", "ikePeerCorripsecTunIndex"))
)
if mibBuilder.loadTexts:
    ipsecPhaseOneGroup.setStatus("current")

ipsecPhaseTwoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 2, 1, 3)
)
ipsecPhaseTwoGroup.setObjects(
      *(("IPsecT1-MIB", "ipsecGlobalActiveTunnels"),
        ("IPsecT1-MIB", "ipsecGlobalPreviousTunnels"),
        ("IPsecT1-MIB", "ipsecGlobalInOctets"),
        ("IPsecT1-MIB", "ipsecGlobalHcInOctets"),
        ("IPsecT1-MIB", "ipsecGlobalInOctWraps"),
        ("IPsecT1-MIB", "ipsecGlobalInDecompOctets"),
        ("IPsecT1-MIB", "ipsecGlobalHcInDecompOctets"),
        ("IPsecT1-MIB", "ipsecGlobalInDecompOctWraps"),
        ("IPsecT1-MIB", "ipsecGlobalInPkts"),
        ("IPsecT1-MIB", "ipsecGlobalInDrops"),
        ("IPsecT1-MIB", "ipsecGlobalInReplayDrops"),
        ("IPsecT1-MIB", "ipsecGlobalInAuths"),
        ("IPsecT1-MIB", "ipsecGlobalInAuthFails"),
        ("IPsecT1-MIB", "ipsecGlobalInDecrypts"),
        ("IPsecT1-MIB", "ipsecGlobalInDecryptFails"),
        ("IPsecT1-MIB", "ipsecGlobalOutOctets"),
        ("IPsecT1-MIB", "ipsecGlobalHcOutOctets"),
        ("IPsecT1-MIB", "ipsecGlobalOutOctWraps"),
        ("IPsecT1-MIB", "ipsecGlobalOutUncompOctets"),
        ("IPsecT1-MIB", "ipsecGlobalHcOutUncompOctets"),
        ("IPsecT1-MIB", "ipsecGlobalOutUncompOctWraps"),
        ("IPsecT1-MIB", "ipsecGlobalOutPkts"),
        ("IPsecT1-MIB", "ipsecGlobalOutDrops"),
        ("IPsecT1-MIB", "ipsecGlobalOutAuths"),
        ("IPsecT1-MIB", "ipsecGlobalOutAuthFails"),
        ("IPsecT1-MIB", "ipsecGlobalOutEncrypts"),
        ("IPsecT1-MIB", "ipsecGlobalOutEncryptFails"),
        ("IPsecT1-MIB", "ipsecGlobalProtocolUseFails"),
        ("IPsecT1-MIB", "ipsecGlobalNoSaFails"),
        ("IPsecT1-MIB", "ipsecGlobalSysCapFails"),
        ("IPsecT1-MIB", "ipsecTunIkeTunnelIndex"),
        ("IPsecT1-MIB", "ipsecTunIkeTunnelAlive"),
        ("IPsecT1-MIB", "ipsecTunLocalAddr"),
        ("IPsecT1-MIB", "ipsecTunRemoteAddr"),
        ("IPsecT1-MIB", "ipsecTunKeyType"),
        ("IPsecT1-MIB", "ipsecTunEncapMode"),
        ("IPsecT1-MIB", "ipsecTunLifeSize"),
        ("IPsecT1-MIB", "ipsecTunLifeTime"),
        ("IPsecT1-MIB", "ipsecTunActiveTime"),
        ("IPsecT1-MIB", "ipsecTunSaLifeSizeThreshold"),
        ("IPsecT1-MIB", "ipsecTunSaLifeTimeThreshold"),
        ("IPsecT1-MIB", "ipsecTunTotalRefreshes"),
        ("IPsecT1-MIB", "ipsecTunExpiredSaInstances"),
        ("IPsecT1-MIB", "ipsecTunCurrentSaInstances"),
        ("IPsecT1-MIB", "ipsecTunInSaDiffHellmanGrp"),
        ("IPsecT1-MIB", "ipsecTunInSaEncryptAlgo"),
        ("IPsecT1-MIB", "ipsecTunInSaAhAuthAlgo"),
        ("IPsecT1-MIB", "ipsecTunInSaEspAuthAlgo"),
        ("IPsecT1-MIB", "ipsecTunInSaDecompAlgo"),
        ("IPsecT1-MIB", "ipsecTunOutSaDiffHellmanGrp"),
        ("IPsecT1-MIB", "ipsecTunOutSaEncryptAlgo"),
        ("IPsecT1-MIB", "ipsecTunOutSaAhAuthAlgo"),
        ("IPsecT1-MIB", "ipsecTunOutSaEspAuthAlgo"),
        ("IPsecT1-MIB", "ipsecTunOutSaCompAlgo"),
        ("IPsecT1-MIB", "ipsecTunInOctets"),
        ("IPsecT1-MIB", "ipsecTunHcInOctets"),
        ("IPsecT1-MIB", "ipsecTunInOctWraps"),
        ("IPsecT1-MIB", "ipsecTunInDecompOctets"),
        ("IPsecT1-MIB", "ipsecTunHcInDecompOctets"),
        ("IPsecT1-MIB", "ipsecTunInDecompOctWraps"),
        ("IPsecT1-MIB", "ipsecTunInPkts"),
        ("IPsecT1-MIB", "ipsecTunInDropPkts"),
        ("IPsecT1-MIB", "ipsecTunInReplayDropPkts"),
        ("IPsecT1-MIB", "ipsecTunInAuths"),
        ("IPsecT1-MIB", "ipsecTunInAuthFails"),
        ("IPsecT1-MIB", "ipsecTunInDecrypts"),
        ("IPsecT1-MIB", "ipsecTunInDecryptFails"),
        ("IPsecT1-MIB", "ipsecTunOutOctets"),
        ("IPsecT1-MIB", "ipsecTunHcOutOctets"),
        ("IPsecT1-MIB", "ipsecTunOutOctWraps"),
        ("IPsecT1-MIB", "ipsecTunOutUncompOctets"),
        ("IPsecT1-MIB", "ipsecTunHcOutUncompOctets"),
        ("IPsecT1-MIB", "ipsecTunOutUncompOctWraps"),
        ("IPsecT1-MIB", "ipsecTunOutPkts"),
        ("IPsecT1-MIB", "ipsecTunOutDropPkts"),
        ("IPsecT1-MIB", "ipsecTunOutAuths"),
        ("IPsecT1-MIB", "ipsecTunOutAuthFails"),
        ("IPsecT1-MIB", "ipsecTunOutEncrypts"),
        ("IPsecT1-MIB", "ipsecTunOutEncryptFails"),
        ("IPsecT1-MIB", "ipsecTunStatus"),
        ("IPsecT1-MIB", "ipsecEndPtLocalName"),
        ("IPsecT1-MIB", "ipsecEndPtLocalType"),
        ("IPsecT1-MIB", "ipsecEndPtLocalAddr1"),
        ("IPsecT1-MIB", "ipsecEndPtLocalAddr2"),
        ("IPsecT1-MIB", "ipsecEndPtLocalProtocol"),
        ("IPsecT1-MIB", "ipsecEndPtLocalPort"),
        ("IPsecT1-MIB", "ipsecEndPtRemoteName"),
        ("IPsecT1-MIB", "ipsecEndPtRemoteType"),
        ("IPsecT1-MIB", "ipsecEndPtRemoteAddr1"),
        ("IPsecT1-MIB", "ipsecEndPtRemoteAddr2"),
        ("IPsecT1-MIB", "ipsecEndPtRemoteProtocol"),
        ("IPsecT1-MIB", "ipsecEndPtRemotePort"),
        ("IPsecT1-MIB", "ipsecSpiDirection"),
        ("IPsecT1-MIB", "ipsecSpiValue"),
        ("IPsecT1-MIB", "ipsecSpiProtocol"),
        ("IPsecT1-MIB", "ipsecSpiStatus"))
)
if mibBuilder.loadTexts:
    ipsecPhaseTwoGroup.setStatus("current")

ipsecHistoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 2, 1, 4)
)
ipsecHistoryGroup.setObjects(
      *(("IPsecT1-MIB", "ipsecHistTableSize"),
        ("IPsecT1-MIB", "ikeTunHistTermReason"),
        ("IPsecT1-MIB", "ikeTunHistActiveIndex"),
        ("IPsecT1-MIB", "ikeTunHistPeerLocalType"),
        ("IPsecT1-MIB", "ikeTunHistPeerLocalValue"),
        ("IPsecT1-MIB", "ikeTunHistPeerIntIndex"),
        ("IPsecT1-MIB", "ikeTunHistPeerRemoteType"),
        ("IPsecT1-MIB", "ikeTunHistPeerRemoteValue"),
        ("IPsecT1-MIB", "ikeTunHistLocalAddr"),
        ("IPsecT1-MIB", "ikeTunHistLocalName"),
        ("IPsecT1-MIB", "ikeTunHistRemoteAddr"),
        ("IPsecT1-MIB", "ikeTunHistRemoteName"),
        ("IPsecT1-MIB", "ikeTunHistNegoMode"),
        ("IPsecT1-MIB", "ikeTunHistDiffHellmanGrp"),
        ("IPsecT1-MIB", "ikeTunHistEncryptAlgo"),
        ("IPsecT1-MIB", "ikeTunHistHashAlgo"),
        ("IPsecT1-MIB", "ikeTunHistAuthMethod"),
        ("IPsecT1-MIB", "ikeTunHistLifeTime"),
        ("IPsecT1-MIB", "ikeTunHistStartTime"),
        ("IPsecT1-MIB", "ikeTunHistActiveTime"),
        ("IPsecT1-MIB", "ikeTunHistTotalRefreshes"),
        ("IPsecT1-MIB", "ikeTunHistTotalSas"),
        ("IPsecT1-MIB", "ikeTunHistInOctets"),
        ("IPsecT1-MIB", "ikeTunHistInPkts"),
        ("IPsecT1-MIB", "ikeTunHistInDropPkts"),
        ("IPsecT1-MIB", "ikeTunHistInNotifys"),
        ("IPsecT1-MIB", "ikeTunHistInP2Exchgs"),
        ("IPsecT1-MIB", "ikeTunHistInP2ExchgInvalids"),
        ("IPsecT1-MIB", "ikeTunHistInP2ExchgRejects"),
        ("IPsecT1-MIB", "ikeTunHistInP2SaDelRequests"),
        ("IPsecT1-MIB", "ikeTunHistOutOctets"),
        ("IPsecT1-MIB", "ikeTunHistOutPkts"),
        ("IPsecT1-MIB", "ikeTunHistOutDropPkts"),
        ("IPsecT1-MIB", "ikeTunHistOutNotifys"),
        ("IPsecT1-MIB", "ikeTunHistOutP2Exchgs"),
        ("IPsecT1-MIB", "ikeTunHistOutP2ExchgInvalids"),
        ("IPsecT1-MIB", "ikeTunHistOutP2ExchgRejects"),
        ("IPsecT1-MIB", "ikeTunHistOutP2SaDelRequests"),
        ("IPsecT1-MIB", "ipsecTunHistTermReason"),
        ("IPsecT1-MIB", "ipsecTunHistActiveIndex"),
        ("IPsecT1-MIB", "ipsecTunHistIkeTunnelIndex"),
        ("IPsecT1-MIB", "ipsecTunHistLocalAddr"),
        ("IPsecT1-MIB", "ipsecTunHistRemoteAddr"),
        ("IPsecT1-MIB", "ipsecTunHistKeyType"),
        ("IPsecT1-MIB", "ipsecTunHistEncapMode"),
        ("IPsecT1-MIB", "ipsecTunHistLifeSize"),
        ("IPsecT1-MIB", "ipsecTunHistLifeTime"),
        ("IPsecT1-MIB", "ipsecTunHistStartTime"),
        ("IPsecT1-MIB", "ipsecTunHistActiveTime"),
        ("IPsecT1-MIB", "ipsecTunHistTotalRefreshes"),
        ("IPsecT1-MIB", "ipsecTunHistTotalSas"),
        ("IPsecT1-MIB", "ipsecTunHistInSaDiffHellmanGrp"),
        ("IPsecT1-MIB", "ipsecTunHistInSaEncryptAlgo"),
        ("IPsecT1-MIB", "ipsecTunHistInSaAhAuthAlgo"),
        ("IPsecT1-MIB", "ipsecTunHistInSaEspAuthAlgo"),
        ("IPsecT1-MIB", "ipsecTunHistInSaDecompAlgo"),
        ("IPsecT1-MIB", "ipsecTunHistOutSaDiffHellmanGrp"),
        ("IPsecT1-MIB", "ipsecTunHistOutSaEncryptAlgo"),
        ("IPsecT1-MIB", "ipsecTunHistOutSaAhAuthAlgo"),
        ("IPsecT1-MIB", "ipsecTunHistOutSaEspAuthAlgo"),
        ("IPsecT1-MIB", "ipsecTunHistOutSaCompAlgo"),
        ("IPsecT1-MIB", "ipsecTunHistInOctets"),
        ("IPsecT1-MIB", "ipsecTunHistHcInOctets"),
        ("IPsecT1-MIB", "ipsecTunHistInOctWraps"),
        ("IPsecT1-MIB", "ipsecTunHistInDecompOctets"),
        ("IPsecT1-MIB", "ipsecTunHistHcInDecompOctets"),
        ("IPsecT1-MIB", "ipsecTunHistInDecompOctWraps"),
        ("IPsecT1-MIB", "ipsecTunHistInPkts"),
        ("IPsecT1-MIB", "ipsecTunHistInDropPkts"),
        ("IPsecT1-MIB", "ipsecTunHistInReplayDropPkts"),
        ("IPsecT1-MIB", "ipsecTunHistInAuths"),
        ("IPsecT1-MIB", "ipsecTunHistInAuthFails"),
        ("IPsecT1-MIB", "ipsecTunHistInDecrypts"),
        ("IPsecT1-MIB", "ipsecTunHistInDecryptFails"),
        ("IPsecT1-MIB", "ipsecTunHistOutOctets"),
        ("IPsecT1-MIB", "ipsecTunHistHcOutOctets"),
        ("IPsecT1-MIB", "ipsecTunHistOutOctWraps"),
        ("IPsecT1-MIB", "ipsecTunHistOutUncompOctets"),
        ("IPsecT1-MIB", "ipsecTunHistHcOutUncompOctets"),
        ("IPsecT1-MIB", "ipsecTunHistOutUncompOctWraps"),
        ("IPsecT1-MIB", "ipsecTunHistOutPkts"),
        ("IPsecT1-MIB", "ipsecTunHistOutDropPkts"),
        ("IPsecT1-MIB", "ipsecTunHistOutAuths"),
        ("IPsecT1-MIB", "ipsecTunHistOutAuthFails"),
        ("IPsecT1-MIB", "ipsecTunHistOutEncrypts"),
        ("IPsecT1-MIB", "ipsecTunHistOutEncryptFails"),
        ("IPsecT1-MIB", "ipsecEndPtHistTunIndex"),
        ("IPsecT1-MIB", "ipsecEndPtHistActiveIndex"),
        ("IPsecT1-MIB", "ipsecEndPtHistLocalName"),
        ("IPsecT1-MIB", "ipsecEndPtHistLocalType"),
        ("IPsecT1-MIB", "ipsecEndPtHistLocalAddr1"),
        ("IPsecT1-MIB", "ipsecEndPtHistLocalAddr2"),
        ("IPsecT1-MIB", "ipsecEndPtHistLocalProtocol"),
        ("IPsecT1-MIB", "ipsecEndPtHistLocalPort"),
        ("IPsecT1-MIB", "ipsecEndPtHistRemoteName"),
        ("IPsecT1-MIB", "ipsecEndPtHistRemoteType"),
        ("IPsecT1-MIB", "ipsecEndPtHistRemoteAddr1"),
        ("IPsecT1-MIB", "ipsecEndPtHistRemoteAddr2"),
        ("IPsecT1-MIB", "ipsecEndPtHistRemoteProtocol"),
        ("IPsecT1-MIB", "ipsecEndPtHistRemotePort"))
)
if mibBuilder.loadTexts:
    ipsecHistoryGroup.setStatus("current")

ipsecFailuresGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 2, 1, 5)
)
ipsecFailuresGroup.setObjects(
      *(("IPsecT1-MIB", "ipsecFailTableSize"),
        ("IPsecT1-MIB", "ikeFailReason"),
        ("IPsecT1-MIB", "ikeFailTime"),
        ("IPsecT1-MIB", "ikeFailLocalType"),
        ("IPsecT1-MIB", "ikeFailLocalValue"),
        ("IPsecT1-MIB", "ikeFailRemoteType"),
        ("IPsecT1-MIB", "ikeFailRemoteValue"),
        ("IPsecT1-MIB", "ikeFailLocalAddr"),
        ("IPsecT1-MIB", "ikeFailRemoteAddr"),
        ("IPsecT1-MIB", "ipsecFailReason"),
        ("IPsecT1-MIB", "ipsecFailTime"),
        ("IPsecT1-MIB", "ipsecFailTunnelIndex"),
        ("IPsecT1-MIB", "ipsecFailSaSpi"),
        ("IPsecT1-MIB", "ipsecFailPktSrcAddr"),
        ("IPsecT1-MIB", "ipsecFailPktDstAddr"))
)
if mibBuilder.loadTexts:
    ipsecFailuresGroup.setStatus("current")

ipsecTrapCntlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 2, 1, 6)
)
ipsecTrapCntlGroup.setObjects(
      *(("IPsecT1-MIB", "ipsecTrapCntlIkeTunnelStart"),
        ("IPsecT1-MIB", "ipsecTrapCntlIkeTunnelStop"),
        ("IPsecT1-MIB", "ipsecTrapCntlIkeSysFailure"),
        ("IPsecT1-MIB", "ipsecTrapCntlIkeCertCrlFailure"),
        ("IPsecT1-MIB", "ipsecTrapCntlIkeProtocolFailure"),
        ("IPsecT1-MIB", "ipsecTrapCntlIkeNoSa"),
        ("IPsecT1-MIB", "ipsecTrapCntlipsecTunnelStart"),
        ("IPsecT1-MIB", "ipsecTrapCntlipsecTunnelStop"),
        ("IPsecT1-MIB", "ipsecTrapCntlipsecSysFailure"),
        ("IPsecT1-MIB", "ipsecTrapCntlipsecSetUpFailure"),
        ("IPsecT1-MIB", "ipsecTrapCntlipsecEarlyTunTerm"),
        ("IPsecT1-MIB", "ipsecTrapCntlipsecProtocolFailure"),
        ("IPsecT1-MIB", "ipsecTrapCntlipsecNoSa"))
)
if mibBuilder.loadTexts:
    ipsecTrapCntlGroup.setStatus("current")


# Notification objects

ikeTunnelStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 0, 1)
)
ikeTunnelStart.setObjects(
      *(("IPsecT1-MIB", "ikePeerLocalType"),
        ("IPsecT1-MIB", "ikePeerLocalValue"),
        ("IPsecT1-MIB", "ikePeerLocalAddr"),
        ("IPsecT1-MIB", "ikePeerRemoteType"),
        ("IPsecT1-MIB", "ikePeerRemoteValue"),
        ("IPsecT1-MIB", "ikePeerRemoteAddr"),
        ("IPsecT1-MIB", "ikePeerIntIndex"),
        ("IPsecT1-MIB", "ikeTunIndex"))
)
if mibBuilder.loadTexts:
    ikeTunnelStart.setStatus(
        "current"
    )

ikeTunnelStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 0, 2)
)
ikeTunnelStop.setObjects(
      *(("IPsecT1-MIB", "ikePeerLocalType"),
        ("IPsecT1-MIB", "ikePeerLocalValue"),
        ("IPsecT1-MIB", "ikePeerLocalAddr"),
        ("IPsecT1-MIB", "ikePeerRemoteType"),
        ("IPsecT1-MIB", "ikePeerRemoteValue"),
        ("IPsecT1-MIB", "ikePeerRemoteAddr"),
        ("IPsecT1-MIB", "ikePeerIntIndex"),
        ("IPsecT1-MIB", "ikeTunIndex"))
)
if mibBuilder.loadTexts:
    ikeTunnelStop.setStatus(
        "current"
    )

ikeSysFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 0, 3)
)
ikeSysFailure.setObjects(
      *(("IPsecT1-MIB", "ikePeerLocalType"),
        ("IPsecT1-MIB", "ikePeerLocalValue"),
        ("IPsecT1-MIB", "ikePeerLocalAddr"),
        ("IPsecT1-MIB", "ikePeerRemoteType"),
        ("IPsecT1-MIB", "ikePeerRemoteValue"),
        ("IPsecT1-MIB", "ikePeerRemoteAddr"),
        ("IPsecT1-MIB", "ikePeerIntIndex"))
)
if mibBuilder.loadTexts:
    ikeSysFailure.setStatus(
        "current"
    )

ikeCertCrlFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 0, 4)
)
ikeCertCrlFailure.setObjects(
      *(("IPsecT1-MIB", "ikePeerLocalType"),
        ("IPsecT1-MIB", "ikePeerLocalValue"),
        ("IPsecT1-MIB", "ikePeerLocalAddr"),
        ("IPsecT1-MIB", "ikePeerRemoteType"),
        ("IPsecT1-MIB", "ikePeerRemoteValue"),
        ("IPsecT1-MIB", "ikePeerRemoteAddr"),
        ("IPsecT1-MIB", "ikePeerIntIndex"))
)
if mibBuilder.loadTexts:
    ikeCertCrlFailure.setStatus(
        "current"
    )

ikeProtocolFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 0, 5)
)
ikeProtocolFailure.setObjects(
      *(("IPsecT1-MIB", "ikePeerLocalType"),
        ("IPsecT1-MIB", "ikePeerLocalValue"),
        ("IPsecT1-MIB", "ikePeerLocalAddr"),
        ("IPsecT1-MIB", "ikePeerRemoteType"),
        ("IPsecT1-MIB", "ikePeerRemoteValue"),
        ("IPsecT1-MIB", "ikePeerRemoteAddr"),
        ("IPsecT1-MIB", "ikePeerIntIndex"))
)
if mibBuilder.loadTexts:
    ikeProtocolFailure.setStatus(
        "current"
    )

ikeNoSa = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 0, 6)
)
ikeNoSa.setObjects(
      *(("IPsecT1-MIB", "ikePeerLocalType"),
        ("IPsecT1-MIB", "ikePeerLocalValue"),
        ("IPsecT1-MIB", "ikePeerLocalAddr"),
        ("IPsecT1-MIB", "ikePeerRemoteType"),
        ("IPsecT1-MIB", "ikePeerRemoteValue"),
        ("IPsecT1-MIB", "ikePeerRemoteAddr"),
        ("IPsecT1-MIB", "ikePeerIntIndex"))
)
if mibBuilder.loadTexts:
    ikeNoSa.setStatus(
        "current"
    )

ipsecTunnelStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 0, 7)
)
ipsecTunnelStart.setObjects(
    ("IPsecT1-MIB", "ipsecTunIndex")
)
if mibBuilder.loadTexts:
    ipsecTunnelStart.setStatus(
        "current"
    )

ipsecTunnelStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 0, 8)
)
ipsecTunnelStop.setObjects(
    ("IPsecT1-MIB", "ipsecTunIndex")
)
if mibBuilder.loadTexts:
    ipsecTunnelStop.setStatus(
        "current"
    )

ipsecSysFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 0, 9)
)
ipsecSysFailure.setObjects(
      *(("IPsecT1-MIB", "ikePeerLocalType"),
        ("IPsecT1-MIB", "ikePeerLocalValue"),
        ("IPsecT1-MIB", "ikePeerLocalAddr"),
        ("IPsecT1-MIB", "ikePeerRemoteType"),
        ("IPsecT1-MIB", "ikePeerRemoteValue"),
        ("IPsecT1-MIB", "ikePeerRemoteAddr"),
        ("IPsecT1-MIB", "ikePeerIntIndex"),
        ("IPsecT1-MIB", "ipsecTunIndex"),
        ("IPsecT1-MIB", "ipsecSpiIndex"))
)
if mibBuilder.loadTexts:
    ipsecSysFailure.setStatus(
        "current"
    )

ipsecSetUpFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 0, 10)
)
ipsecSetUpFailure.setObjects(
      *(("IPsecT1-MIB", "ikePeerLocalType"),
        ("IPsecT1-MIB", "ikePeerLocalValue"),
        ("IPsecT1-MIB", "ikePeerLocalAddr"),
        ("IPsecT1-MIB", "ikePeerRemoteType"),
        ("IPsecT1-MIB", "ikePeerRemoteValue"),
        ("IPsecT1-MIB", "ikePeerRemoteAddr"),
        ("IPsecT1-MIB", "ikePeerIntIndex"))
)
if mibBuilder.loadTexts:
    ipsecSetUpFailure.setStatus(
        "current"
    )

ipsecEarilyTunnelTerm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 0, 11)
)
ipsecEarilyTunnelTerm.setObjects(
      *(("IPsecT1-MIB", "ipsecTunIndex"),
        ("IPsecT1-MIB", "ipsecSpiIndex"))
)
if mibBuilder.loadTexts:
    ipsecEarilyTunnelTerm.setStatus(
        "current"
    )

ipsecProtocolFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 0, 12)
)
ipsecProtocolFailure.setObjects(
      *(("IPsecT1-MIB", "ipsecTunIndex"),
        ("IPsecT1-MIB", "ipsecSpiIndex"))
)
if mibBuilder.loadTexts:
    ipsecProtocolFailure.setStatus(
        "current"
    )

ipsecNoSa = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 0, 13)
)
ipsecNoSa.setObjects(
      *(("IPsecT1-MIB", "ipsecTunIndex"),
        ("IPsecT1-MIB", "ipsecSpiIndex"))
)
if mibBuilder.loadTexts:
    ipsecNoSa.setStatus(
        "current"
    )


# Notifications groups

ipsecNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 2, 1, 7)
)
ipsecNotificationGroup.setObjects(
      *(("IPsecT1-MIB", "ikeTunnelStart"),
        ("IPsecT1-MIB", "ikeTunnelStop"),
        ("IPsecT1-MIB", "ikeSysFailure"),
        ("IPsecT1-MIB", "ikeCertCrlFailure"),
        ("IPsecT1-MIB", "ikeProtocolFailure"),
        ("IPsecT1-MIB", "ikeNoSa"),
        ("IPsecT1-MIB", "ipsecTunnelStart"),
        ("IPsecT1-MIB", "ipsecTunnelStop"),
        ("IPsecT1-MIB", "ipsecSysFailure"),
        ("IPsecT1-MIB", "ipsecSetUpFailure"),
        ("IPsecT1-MIB", "ipsecEarilyTunTerm"),
        ("IPsecT1-MIB", "ipsecProtocolFailure"),
        ("IPsecT1-MIB", "ipsecNoSa"))
)
if mibBuilder.loadTexts:
    ipsecNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ipsecMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2, 6, 168, 1, 1, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    ipsecMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IPsecT1-MIB",
    **{"IPSIpAddress": IPSIpAddress,
       "IkePeerType": IkePeerType,
       "IkeNegoMode": IkeNegoMode,
       "IkeHashAlgo": IkeHashAlgo,
       "IkeAuthMethod": IkeAuthMethod,
       "DiffHellmanGrp": DiffHellmanGrp,
       "KeyType": KeyType,
       "EncapMode": EncapMode,
       "EncryptAlgo": EncryptAlgo,
       "AuthAlgo": AuthAlgo,
       "CompAlgo": CompAlgo,
       "EndPtType": EndPtType,
       "TunnelStatus": TunnelStatus,
       "TrapStatus": TrapStatus,
       "ipsecMIB": ipsecMIB,
       "ipsecMIBNotifications": ipsecMIBNotifications,
       "ikeTunnelStart": ikeTunnelStart,
       "ikeTunnelStop": ikeTunnelStop,
       "ikeSysFailure": ikeSysFailure,
       "ikeCertCrlFailure": ikeCertCrlFailure,
       "ikeProtocolFailure": ikeProtocolFailure,
       "ikeNoSa": ikeNoSa,
       "ipsecTunnelStart": ipsecTunnelStart,
       "ipsecTunnelStop": ipsecTunnelStop,
       "ipsecSysFailure": ipsecSysFailure,
       "ipsecSetUpFailure": ipsecSetUpFailure,
       "ipsecEarilyTunnelTerm": ipsecEarilyTunnelTerm,
       "ipsecProtocolFailure": ipsecProtocolFailure,
       "ipsecNoSa": ipsecNoSa,
       "ipsecMIBObjects": ipsecMIBObjects,
       "ipsecLevels": ipsecLevels,
       "ipsecMibLevel": ipsecMibLevel,
       "ipsecPhaseOne": ipsecPhaseOne,
       "ikeGlobalStats": ikeGlobalStats,
       "ikeGlobalActiveTunnels": ikeGlobalActiveTunnels,
       "ikeGlobalPreviousTunnels": ikeGlobalPreviousTunnels,
       "ikeGlobalInOctets": ikeGlobalInOctets,
       "ikeGlobalInPkts": ikeGlobalInPkts,
       "ikeGlobalInDropPkts": ikeGlobalInDropPkts,
       "ikeGlobalInNotifys": ikeGlobalInNotifys,
       "ikeGlobalInP2Exchgs": ikeGlobalInP2Exchgs,
       "ikeGlobalInP2ExchgInvalids": ikeGlobalInP2ExchgInvalids,
       "ikeGlobalInP2ExchgRejects": ikeGlobalInP2ExchgRejects,
       "ikeGlobalInP2SaDelRequests": ikeGlobalInP2SaDelRequests,
       "ikeGlobalOutOctets": ikeGlobalOutOctets,
       "ikeGlobalOutPkts": ikeGlobalOutPkts,
       "ikeGlobalOutDropPkts": ikeGlobalOutDropPkts,
       "ikeGlobalOutNotifys": ikeGlobalOutNotifys,
       "ikeGlobalOutP2Exchgs": ikeGlobalOutP2Exchgs,
       "ikeGlobalOutP2ExchgInvalids": ikeGlobalOutP2ExchgInvalids,
       "ikeGlobalOutP2ExchgRejects": ikeGlobalOutP2ExchgRejects,
       "ikeGlobalOutP2SaDelRequests": ikeGlobalOutP2SaDelRequests,
       "ikeGlobalInitTunnels": ikeGlobalInitTunnels,
       "ikeGlobalInitTunnelFails": ikeGlobalInitTunnelFails,
       "ikeGlobalRespTunnelFails": ikeGlobalRespTunnelFails,
       "ikeGlobalSysCapFails": ikeGlobalSysCapFails,
       "ikeGlobalAuthFails": ikeGlobalAuthFails,
       "ikeGlobalDecryptFails": ikeGlobalDecryptFails,
       "ikeGlobalHashValidFails": ikeGlobalHashValidFails,
       "ikeGlobalNoSaFails": ikeGlobalNoSaFails,
       "ipsecGlobalProtocolUseFails": ipsecGlobalProtocolUseFails,
       "ipsecGlobalNoSaFails": ipsecGlobalNoSaFails,
       "ipsecGlobalSysCapFails": ipsecGlobalSysCapFails,
       "ikePeerTable": ikePeerTable,
       "ikePeerEntry": ikePeerEntry,
       "ikePeerLocalType": ikePeerLocalType,
       "ikePeerLocalValue": ikePeerLocalValue,
       "ikePeerRemoteType": ikePeerRemoteType,
       "ikePeerRemoteValue": ikePeerRemoteValue,
       "ikePeerIntIndex": ikePeerIntIndex,
       "ikePeerLocalAddr": ikePeerLocalAddr,
       "ikePeerRemoteAddr": ikePeerRemoteAddr,
       "ikePeerActiveTime": ikePeerActiveTime,
       "ikePeerActiveTunnelIndex": ikePeerActiveTunnelIndex,
       "ikeTunnelTable": ikeTunnelTable,
       "ikeTunnelEntry": ikeTunnelEntry,
       "ikeTunIndex": ikeTunIndex,
       "ikeTunLocalType": ikeTunLocalType,
       "ikeTunLocalValue": ikeTunLocalValue,
       "ikeTunLocalAddr": ikeTunLocalAddr,
       "ikeTunLocalName": ikeTunLocalName,
       "ikeTunRemoteType": ikeTunRemoteType,
       "ikeTunRemoteValue": ikeTunRemoteValue,
       "ikeTunRemoteAddr": ikeTunRemoteAddr,
       "ikeTunRemoteName": ikeTunRemoteName,
       "ikeTunNegoMode": ikeTunNegoMode,
       "ikeTunDiffHellmanGrp": ikeTunDiffHellmanGrp,
       "ikeTunEncryptAlgo": ikeTunEncryptAlgo,
       "ikeTunHashAlgo": ikeTunHashAlgo,
       "ikeTunAuthMethod": ikeTunAuthMethod,
       "ikeTunLifeTime": ikeTunLifeTime,
       "ikeTunActiveTime": ikeTunActiveTime,
       "ikeTunSaRefreshThreshold": ikeTunSaRefreshThreshold,
       "ikeTunTotalRefreshes": ikeTunTotalRefreshes,
       "ikeTunInOctets": ikeTunInOctets,
       "ikeTunInPkts": ikeTunInPkts,
       "ikeTunInDropPkts": ikeTunInDropPkts,
       "ikeTunInNotifys": ikeTunInNotifys,
       "ikeTunInP2Exchgs": ikeTunInP2Exchgs,
       "ikeTunInP2ExchgInvalids": ikeTunInP2ExchgInvalids,
       "ikeTunInP2ExchgRejects": ikeTunInP2ExchgRejects,
       "ikeTunInP2SaDelRequests": ikeTunInP2SaDelRequests,
       "ikeTunOutOctets": ikeTunOutOctets,
       "ikeTunOutPkts": ikeTunOutPkts,
       "ikeTunOutDropPkts": ikeTunOutDropPkts,
       "ikeTunOutNotifys": ikeTunOutNotifys,
       "ikeTunOutP2Exchgs": ikeTunOutP2Exchgs,
       "ikeTunOutP2ExchgInvalids": ikeTunOutP2ExchgInvalids,
       "ikeTunOutP2ExchgRejects": ikeTunOutP2ExchgRejects,
       "ikeTunOutP2SaDelRequests": ikeTunOutP2SaDelRequests,
       "ikeTunStatus": ikeTunStatus,
       "ikePeerCorrTable": ikePeerCorrTable,
       "ikePeerCorrEntry": ikePeerCorrEntry,
       "ikePeerCorrLocalType": ikePeerCorrLocalType,
       "ikePeerCorrLocalValue": ikePeerCorrLocalValue,
       "ikePeerCorrRemoteType": ikePeerCorrRemoteType,
       "ikePeerCorrRemoteValue": ikePeerCorrRemoteValue,
       "ikePeerCorrIntIndex": ikePeerCorrIntIndex,
       "ikePeerCorrSeqNum": ikePeerCorrSeqNum,
       "ikePeerCorripsecTunIndex": ikePeerCorripsecTunIndex,
       "ipsecPhaseTwo": ipsecPhaseTwo,
       "ipsecGlobalStats": ipsecGlobalStats,
       "ipsecGlobalActiveTunnels": ipsecGlobalActiveTunnels,
       "ipsecGlobalPreviousTunnels": ipsecGlobalPreviousTunnels,
       "ipsecGlobalInOctets": ipsecGlobalInOctets,
       "ipsecGlobalHcInOctets": ipsecGlobalHcInOctets,
       "ipsecGlobalInOctWraps": ipsecGlobalInOctWraps,
       "ipsecGlobalInDecompOctets": ipsecGlobalInDecompOctets,
       "ipsecGlobalHcInDecompOctets": ipsecGlobalHcInDecompOctets,
       "ipsecGlobalInDecompOctWraps": ipsecGlobalInDecompOctWraps,
       "ipsecGlobalInPkts": ipsecGlobalInPkts,
       "ipsecGlobalInDrops": ipsecGlobalInDrops,
       "ipsecGlobalInReplayDrops": ipsecGlobalInReplayDrops,
       "ipsecGlobalInAuths": ipsecGlobalInAuths,
       "ipsecGlobalInAuthFails": ipsecGlobalInAuthFails,
       "ipsecGlobalInDecrypts": ipsecGlobalInDecrypts,
       "ipsecGlobalInDecryptFails": ipsecGlobalInDecryptFails,
       "ipsecGlobalOutOctets": ipsecGlobalOutOctets,
       "ipsecGlobalHcOutOctets": ipsecGlobalHcOutOctets,
       "ipsecGlobalOutOctWraps": ipsecGlobalOutOctWraps,
       "ipsecGlobalOutUncompOctets": ipsecGlobalOutUncompOctets,
       "ipsecGlobalHcOutUncompOctets": ipsecGlobalHcOutUncompOctets,
       "ipsecGlobalOutUncompOctWraps": ipsecGlobalOutUncompOctWraps,
       "ipsecGlobalOutPkts": ipsecGlobalOutPkts,
       "ipsecGlobalOutDrops": ipsecGlobalOutDrops,
       "ipsecGlobalOutAuths": ipsecGlobalOutAuths,
       "ipsecGlobalOutAuthFails": ipsecGlobalOutAuthFails,
       "ipsecGlobalOutEncrypts": ipsecGlobalOutEncrypts,
       "ipsecGlobalOutEncryptFails": ipsecGlobalOutEncryptFails,
       "ipsecTunnelTable": ipsecTunnelTable,
       "ipsecTunnelEntry": ipsecTunnelEntry,
       "ipsecTunIndex": ipsecTunIndex,
       "ipsecTunIkeTunnelIndex": ipsecTunIkeTunnelIndex,
       "ipsecTunIkeTunnelAlive": ipsecTunIkeTunnelAlive,
       "ipsecTunLocalAddr": ipsecTunLocalAddr,
       "ipsecTunRemoteAddr": ipsecTunRemoteAddr,
       "ipsecTunKeyType": ipsecTunKeyType,
       "ipsecTunEncapMode": ipsecTunEncapMode,
       "ipsecTunLifeSize": ipsecTunLifeSize,
       "ipsecTunLifeTime": ipsecTunLifeTime,
       "ipsecTunActiveTime": ipsecTunActiveTime,
       "ipsecTunSaLifeSizeThreshold": ipsecTunSaLifeSizeThreshold,
       "ipsecTunSaLifeTimeThreshold": ipsecTunSaLifeTimeThreshold,
       "ipsecTunTotalRefreshes": ipsecTunTotalRefreshes,
       "ipsecTunExpiredSaInstances": ipsecTunExpiredSaInstances,
       "ipsecTunCurrentSaInstances": ipsecTunCurrentSaInstances,
       "ipsecTunInSaDiffHellmanGrp": ipsecTunInSaDiffHellmanGrp,
       "ipsecTunInSaEncryptAlgo": ipsecTunInSaEncryptAlgo,
       "ipsecTunInSaAhAuthAlgo": ipsecTunInSaAhAuthAlgo,
       "ipsecTunInSaEspAuthAlgo": ipsecTunInSaEspAuthAlgo,
       "ipsecTunInSaDecompAlgo": ipsecTunInSaDecompAlgo,
       "ipsecTunOutSaDiffHellmanGrp": ipsecTunOutSaDiffHellmanGrp,
       "ipsecTunOutSaEncryptAlgo": ipsecTunOutSaEncryptAlgo,
       "ipsecTunOutSaAhAuthAlgo": ipsecTunOutSaAhAuthAlgo,
       "ipsecTunOutSaEspAuthAlgo": ipsecTunOutSaEspAuthAlgo,
       "ipsecTunOutSaCompAlgo": ipsecTunOutSaCompAlgo,
       "ipsecTunInOctets": ipsecTunInOctets,
       "ipsecTunHcInOctets": ipsecTunHcInOctets,
       "ipsecTunInOctWraps": ipsecTunInOctWraps,
       "ipsecTunInDecompOctets": ipsecTunInDecompOctets,
       "ipsecTunHcInDecompOctets": ipsecTunHcInDecompOctets,
       "ipsecTunInDecompOctWraps": ipsecTunInDecompOctWraps,
       "ipsecTunInPkts": ipsecTunInPkts,
       "ipsecTunInDropPkts": ipsecTunInDropPkts,
       "ipsecTunInReplayDropPkts": ipsecTunInReplayDropPkts,
       "ipsecTunInAuths": ipsecTunInAuths,
       "ipsecTunInAuthFails": ipsecTunInAuthFails,
       "ipsecTunInDecrypts": ipsecTunInDecrypts,
       "ipsecTunInDecryptFails": ipsecTunInDecryptFails,
       "ipsecTunOutOctets": ipsecTunOutOctets,
       "ipsecTunHcOutOctets": ipsecTunHcOutOctets,
       "ipsecTunOutOctWraps": ipsecTunOutOctWraps,
       "ipsecTunOutUncompOctets": ipsecTunOutUncompOctets,
       "ipsecTunHcOutUncompOctets": ipsecTunHcOutUncompOctets,
       "ipsecTunOutUncompOctWraps": ipsecTunOutUncompOctWraps,
       "ipsecTunOutPkts": ipsecTunOutPkts,
       "ipsecTunOutDropPkts": ipsecTunOutDropPkts,
       "ipsecTunOutAuths": ipsecTunOutAuths,
       "ipsecTunOutAuthFails": ipsecTunOutAuthFails,
       "ipsecTunOutEncrypts": ipsecTunOutEncrypts,
       "ipsecTunOutEncryptFails": ipsecTunOutEncryptFails,
       "ipsecTunStatus": ipsecTunStatus,
       "ipsecEndPtTable": ipsecEndPtTable,
       "ipsecEndPtEntry": ipsecEndPtEntry,
       "ipsecEndPtIndex": ipsecEndPtIndex,
       "ipsecEndPtLocalName": ipsecEndPtLocalName,
       "ipsecEndPtLocalType": ipsecEndPtLocalType,
       "ipsecEndPtLocalAddr1": ipsecEndPtLocalAddr1,
       "ipsecEndPtLocalAddr2": ipsecEndPtLocalAddr2,
       "ipsecEndPtLocalProtocol": ipsecEndPtLocalProtocol,
       "ipsecEndPtLocalPort": ipsecEndPtLocalPort,
       "ipsecEndPtRemoteName": ipsecEndPtRemoteName,
       "ipsecEndPtRemoteType": ipsecEndPtRemoteType,
       "ipsecEndPtRemoteAddr1": ipsecEndPtRemoteAddr1,
       "ipsecEndPtRemoteAddr2": ipsecEndPtRemoteAddr2,
       "ipsecEndPtRemoteProtocol": ipsecEndPtRemoteProtocol,
       "ipsecEndPtRemotePort": ipsecEndPtRemotePort,
       "ipsecSpiTable": ipsecSpiTable,
       "ipsecSpiEntry": ipsecSpiEntry,
       "ipsecSpiIndex": ipsecSpiIndex,
       "ipsecSpiDirection": ipsecSpiDirection,
       "ipsecSpiValue": ipsecSpiValue,
       "ipsecSpiProtocol": ipsecSpiProtocol,
       "ipsecSpiStatus": ipsecSpiStatus,
       "ipsecHistory": ipsecHistory,
       "ipsecHistGlobal": ipsecHistGlobal,
       "ipsecHistGlobalCntl": ipsecHistGlobalCntl,
       "ipsecHistTableSize": ipsecHistTableSize,
       "ipsecHistPhaseOne": ipsecHistPhaseOne,
       "ikeTunnelHistTable": ikeTunnelHistTable,
       "ikeTunnelHistEntry": ikeTunnelHistEntry,
       "ikeTunHistIndex": ikeTunHistIndex,
       "ikeTunHistTermReason": ikeTunHistTermReason,
       "ikeTunHistActiveIndex": ikeTunHistActiveIndex,
       "ikeTunHistPeerLocalType": ikeTunHistPeerLocalType,
       "ikeTunHistPeerLocalValue": ikeTunHistPeerLocalValue,
       "ikeTunHistPeerIntIndex": ikeTunHistPeerIntIndex,
       "ikeTunHistPeerRemoteType": ikeTunHistPeerRemoteType,
       "ikeTunHistPeerRemoteValue": ikeTunHistPeerRemoteValue,
       "ikeTunHistLocalAddr": ikeTunHistLocalAddr,
       "ikeTunHistLocalName": ikeTunHistLocalName,
       "ikeTunHistRemoteAddr": ikeTunHistRemoteAddr,
       "ikeTunHistRemoteName": ikeTunHistRemoteName,
       "ikeTunHistNegoMode": ikeTunHistNegoMode,
       "ikeTunHistDiffHellmanGrp": ikeTunHistDiffHellmanGrp,
       "ikeTunHistEncryptAlgo": ikeTunHistEncryptAlgo,
       "ikeTunHistHashAlgo": ikeTunHistHashAlgo,
       "ikeTunHistAuthMethod": ikeTunHistAuthMethod,
       "ikeTunHistLifeTime": ikeTunHistLifeTime,
       "ikeTunHistStartTime": ikeTunHistStartTime,
       "ikeTunHistActiveTime": ikeTunHistActiveTime,
       "ikeTunHistTotalRefreshes": ikeTunHistTotalRefreshes,
       "ikeTunHistTotalSas": ikeTunHistTotalSas,
       "ikeTunHistInOctets": ikeTunHistInOctets,
       "ikeTunHistInPkts": ikeTunHistInPkts,
       "ikeTunHistInDropPkts": ikeTunHistInDropPkts,
       "ikeTunHistInNotifys": ikeTunHistInNotifys,
       "ikeTunHistInP2Exchgs": ikeTunHistInP2Exchgs,
       "ikeTunHistInP2ExchgInvalids": ikeTunHistInP2ExchgInvalids,
       "ikeTunHistInP2ExchgRejects": ikeTunHistInP2ExchgRejects,
       "ikeTunHistInP2SaDelRequests": ikeTunHistInP2SaDelRequests,
       "ikeTunHistOutOctets": ikeTunHistOutOctets,
       "ikeTunHistOutPkts": ikeTunHistOutPkts,
       "ikeTunHistOutDropPkts": ikeTunHistOutDropPkts,
       "ikeTunHistOutNotifys": ikeTunHistOutNotifys,
       "ikeTunHistOutP2Exchgs": ikeTunHistOutP2Exchgs,
       "ikeTunHistOutP2ExchgInvalids": ikeTunHistOutP2ExchgInvalids,
       "ikeTunHistOutP2ExchgRejects": ikeTunHistOutP2ExchgRejects,
       "ikeTunHistOutP2SaDelRequests": ikeTunHistOutP2SaDelRequests,
       "ipsecHistPhaseTwo": ipsecHistPhaseTwo,
       "ipsecTunnelHistTable": ipsecTunnelHistTable,
       "ipsecTunnelHistEntry": ipsecTunnelHistEntry,
       "ipsecTunHistIndex": ipsecTunHistIndex,
       "ipsecTunHistTermReason": ipsecTunHistTermReason,
       "ipsecTunHistActiveIndex": ipsecTunHistActiveIndex,
       "ipsecTunHistIkeTunnelIndex": ipsecTunHistIkeTunnelIndex,
       "ipsecTunHistLocalAddr": ipsecTunHistLocalAddr,
       "ipsecTunHistRemoteAddr": ipsecTunHistRemoteAddr,
       "ipsecTunHistKeyType": ipsecTunHistKeyType,
       "ipsecTunHistEncapMode": ipsecTunHistEncapMode,
       "ipsecTunHistLifeSize": ipsecTunHistLifeSize,
       "ipsecTunHistLifeTime": ipsecTunHistLifeTime,
       "ipsecTunHistStartTime": ipsecTunHistStartTime,
       "ipsecTunHistActiveTime": ipsecTunHistActiveTime,
       "ipsecTunHistTotalRefreshes": ipsecTunHistTotalRefreshes,
       "ipsecTunHistTotalSas": ipsecTunHistTotalSas,
       "ipsecTunHistInSaDiffHellmanGrp": ipsecTunHistInSaDiffHellmanGrp,
       "ipsecTunHistInSaEncryptAlgo": ipsecTunHistInSaEncryptAlgo,
       "ipsecTunHistInSaAhAuthAlgo": ipsecTunHistInSaAhAuthAlgo,
       "ipsecTunHistInSaEspAuthAlgo": ipsecTunHistInSaEspAuthAlgo,
       "ipsecTunHistInSaDecompAlgo": ipsecTunHistInSaDecompAlgo,
       "ipsecTunHistOutSaDiffHellmanGrp": ipsecTunHistOutSaDiffHellmanGrp,
       "ipsecTunHistOutSaEncryptAlgo": ipsecTunHistOutSaEncryptAlgo,
       "ipsecTunHistOutSaAhAuthAlgo": ipsecTunHistOutSaAhAuthAlgo,
       "ipsecTunHistOutSaEspAuthAlgo": ipsecTunHistOutSaEspAuthAlgo,
       "ipsecTunHistOutSaCompAlgo": ipsecTunHistOutSaCompAlgo,
       "ipsecTunHistInOctets": ipsecTunHistInOctets,
       "ipsecTunHistHcInOctets": ipsecTunHistHcInOctets,
       "ipsecTunHistInOctWraps": ipsecTunHistInOctWraps,
       "ipsecTunHistInDecompOctets": ipsecTunHistInDecompOctets,
       "ipsecTunHistHcInDecompOctets": ipsecTunHistHcInDecompOctets,
       "ipsecTunHistInDecompOctWraps": ipsecTunHistInDecompOctWraps,
       "ipsecTunHistInPkts": ipsecTunHistInPkts,
       "ipsecTunHistInDropPkts": ipsecTunHistInDropPkts,
       "ipsecTunHistInReplayDropPkts": ipsecTunHistInReplayDropPkts,
       "ipsecTunHistInAuths": ipsecTunHistInAuths,
       "ipsecTunHistInAuthFails": ipsecTunHistInAuthFails,
       "ipsecTunHistInDecrypts": ipsecTunHistInDecrypts,
       "ipsecTunHistInDecryptFails": ipsecTunHistInDecryptFails,
       "ipsecTunHistOutOctets": ipsecTunHistOutOctets,
       "ipsecTunHistHcOutOctets": ipsecTunHistHcOutOctets,
       "ipsecTunHistOutOctWraps": ipsecTunHistOutOctWraps,
       "ipsecTunHistOutUncompOctets": ipsecTunHistOutUncompOctets,
       "ipsecTunHistHcOutUncompOctets": ipsecTunHistHcOutUncompOctets,
       "ipsecTunHistOutUncompOctWraps": ipsecTunHistOutUncompOctWraps,
       "ipsecTunHistOutPkts": ipsecTunHistOutPkts,
       "ipsecTunHistOutDropPkts": ipsecTunHistOutDropPkts,
       "ipsecTunHistOutAuths": ipsecTunHistOutAuths,
       "ipsecTunHistOutAuthFails": ipsecTunHistOutAuthFails,
       "ipsecTunHistOutEncrypts": ipsecTunHistOutEncrypts,
       "ipsecTunHistOutEncryptFails": ipsecTunHistOutEncryptFails,
       "ipsecEndPtHistTable": ipsecEndPtHistTable,
       "ipsecEndPtHistEntry": ipsecEndPtHistEntry,
       "ipsecEndPtHistIndex": ipsecEndPtHistIndex,
       "ipsecEndPtHistTunIndex": ipsecEndPtHistTunIndex,
       "ipsecEndPtHistActiveIndex": ipsecEndPtHistActiveIndex,
       "ipsecEndPtHistLocalName": ipsecEndPtHistLocalName,
       "ipsecEndPtHistLocalType": ipsecEndPtHistLocalType,
       "ipsecEndPtHistLocalAddr1": ipsecEndPtHistLocalAddr1,
       "ipsecEndPtHistLocalAddr2": ipsecEndPtHistLocalAddr2,
       "ipsecEndPtHistLocalProtocol": ipsecEndPtHistLocalProtocol,
       "ipsecEndPtHistLocalPort": ipsecEndPtHistLocalPort,
       "ipsecEndPtHistRemoteName": ipsecEndPtHistRemoteName,
       "ipsecEndPtHistRemoteType": ipsecEndPtHistRemoteType,
       "ipsecEndPtHistRemoteAddr1": ipsecEndPtHistRemoteAddr1,
       "ipsecEndPtHistRemoteAddr2": ipsecEndPtHistRemoteAddr2,
       "ipsecEndPtHistRemoteProtocol": ipsecEndPtHistRemoteProtocol,
       "ipsecEndPtHistRemotePort": ipsecEndPtHistRemotePort,
       "ipsecFailures": ipsecFailures,
       "ipsecFailGlobal": ipsecFailGlobal,
       "ipsecFailGlobalCntl": ipsecFailGlobalCntl,
       "ipsecFailTableSize": ipsecFailTableSize,
       "ipsecFailPhaseOne": ipsecFailPhaseOne,
       "ikeFailTable": ikeFailTable,
       "ikeFailEntry": ikeFailEntry,
       "ikeFailIndex": ikeFailIndex,
       "ikeFailReason": ikeFailReason,
       "ikeFailTime": ikeFailTime,
       "ikeFailLocalType": ikeFailLocalType,
       "ikeFailLocalValue": ikeFailLocalValue,
       "ikeFailRemoteType": ikeFailRemoteType,
       "ikeFailRemoteValue": ikeFailRemoteValue,
       "ikeFailLocalAddr": ikeFailLocalAddr,
       "ikeFailRemoteAddr": ikeFailRemoteAddr,
       "ipsecFailPhaseTwo": ipsecFailPhaseTwo,
       "ipsecFailTable": ipsecFailTable,
       "ipsecFailEntry": ipsecFailEntry,
       "ipsecFailIndex": ipsecFailIndex,
       "ipsecFailReason": ipsecFailReason,
       "ipsecFailTime": ipsecFailTime,
       "ipsecFailTunnelIndex": ipsecFailTunnelIndex,
       "ipsecFailSaSpi": ipsecFailSaSpi,
       "ipsecFailPktSrcAddr": ipsecFailPktSrcAddr,
       "ipsecFailPktDstAddr": ipsecFailPktDstAddr,
       "ipsecTrapCntl": ipsecTrapCntl,
       "ipsecTrapCntlIkeTunnelStart": ipsecTrapCntlIkeTunnelStart,
       "ipsecTrapCntlIkeTunnelStop": ipsecTrapCntlIkeTunnelStop,
       "ipsecTrapCntlIkeSysFailure": ipsecTrapCntlIkeSysFailure,
       "ipsecTrapCntlIkeCertCrlFailure": ipsecTrapCntlIkeCertCrlFailure,
       "ipsecTrapCntlIkeProtocolFailure": ipsecTrapCntlIkeProtocolFailure,
       "ipsecTrapCntlIkeNoSa": ipsecTrapCntlIkeNoSa,
       "ipsecTrapCntlipsecTunnelStart": ipsecTrapCntlipsecTunnelStart,
       "ipsecTrapCntlipsecTunnelStop": ipsecTrapCntlipsecTunnelStop,
       "ipsecTrapCntlipsecSysFailure": ipsecTrapCntlipsecSysFailure,
       "ipsecTrapCntlipsecSetUpFailure": ipsecTrapCntlipsecSetUpFailure,
       "ipsecTrapCntlipsecEarlyTunTerm": ipsecTrapCntlipsecEarlyTunTerm,
       "ipsecTrapCntlipsecProtocolFailure": ipsecTrapCntlipsecProtocolFailure,
       "ipsecTrapCntlipsecNoSa": ipsecTrapCntlipsecNoSa,
       "ipsecMIBConformance": ipsecMIBConformance,
       "ipsecMIBGroups": ipsecMIBGroups,
       "ipsecLevelsGroup": ipsecLevelsGroup,
       "ipsecPhaseOneGroup": ipsecPhaseOneGroup,
       "ipsecPhaseTwoGroup": ipsecPhaseTwoGroup,
       "ipsecHistoryGroup": ipsecHistoryGroup,
       "ipsecFailuresGroup": ipsecFailuresGroup,
       "ipsecTrapCntlGroup": ipsecTrapCntlGroup,
       "ipsecNotificationGroup": ipsecNotificationGroup,
       "ipsecMIBCompliances": ipsecMIBCompliances,
       "ipsecMIBCompliance": ipsecMIBCompliance}
)
