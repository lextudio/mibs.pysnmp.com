# SNMP MIB module (CISCO-IPSEC-FLOW-MONITOR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-IPSEC-FLOW-MONITOR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:02:51 2024
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

(cmgwIndex,) = mibBuilder.importSymbols(
    "CISCO-MEDIA-GATEWAY-MIB",
    "cmgwIndex")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

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

ciscoIpSecFlowMonitorMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 171)
)
ciscoIpSecFlowMonitorMIB.setRevisions(
        ("2007-10-24 00:00",
         "2004-10-12 00:00",
         "2000-10-13 18:00",
         "2000-08-17 12:59")
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

_CipSecMIBObjects_ObjectIdentity = ObjectIdentity
cipSecMIBObjects = _CipSecMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1)
)
_CipSecLevels_ObjectIdentity = ObjectIdentity
cipSecLevels = _CipSecLevels_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 1)
)


class _CipSecMibLevel_Type(Integer32):
    """Custom type cipSecMibLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_CipSecMibLevel_Type.__name__ = "Integer32"
_CipSecMibLevel_Object = MibScalar
cipSecMibLevel = _CipSecMibLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 1, 1),
    _CipSecMibLevel_Type()
)
cipSecMibLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecMibLevel.setStatus("current")
_CipSecPhaseOne_ObjectIdentity = ObjectIdentity
cipSecPhaseOne = _CipSecPhaseOne_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 2)
)
_CikeGlobalStats_ObjectIdentity = ObjectIdentity
cikeGlobalStats = _CikeGlobalStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 2, 1)
)
_CikeGlobalActiveTunnels_Type = Gauge32
_CikeGlobalActiveTunnels_Object = MibScalar
cikeGlobalActiveTunnels = _CikeGlobalActiveTunnels_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 2, 1, 1),
    _CikeGlobalActiveTunnels_Type()
)
cikeGlobalActiveTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikeGlobalActiveTunnels.setStatus("current")
_CikeGlobalPreviousTunnels_Type = Counter32
_CikeGlobalPreviousTunnels_Object = MibScalar
cikeGlobalPreviousTunnels = _CikeGlobalPreviousTunnels_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 2, 1, 2),
    _CikeGlobalPreviousTunnels_Type()
)
cikeGlobalPreviousTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikeGlobalPreviousTunnels.setStatus("current")
if mibBuilder.loadTexts:
    cikeGlobalPreviousTunnels.setUnits("SAs")
_CikeGlobalInOctets_Type = Counter32
_CikeGlobalInOctets_Object = MibScalar
cikeGlobalInOctets = _CikeGlobalInOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 2, 1, 3),
    _CikeGlobalInOctets_Type()
)
cikeGlobalInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikeGlobalInOctets.setStatus("current")
if mibBuilder.loadTexts:
    cikeGlobalInOctets.setUnits("Octets")
_CikeGlobalInPkts_Type = Counter32
_CikeGlobalInPkts_Object = MibScalar
cikeGlobalInPkts = _CikeGlobalInPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 2, 1, 4),
    _CikeGlobalInPkts_Type()
)
cikeGlobalInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikeGlobalInPkts.setStatus("current")
if mibBuilder.loadTexts:
    cikeGlobalInPkts.setUnits("Packets")
_CikeGlobalInDropPkts_Type = Counter32
_CikeGlobalInDropPkts_Object = MibScalar
cikeGlobalInDropPkts = _CikeGlobalInDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 2, 1, 5),
    _CikeGlobalInDropPkts_Type()
)
cikeGlobalInDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikeGlobalInDropPkts.setStatus("current")
if mibBuilder.loadTexts:
    cikeGlobalInDropPkts.setUnits("Packets")
_CikeGlobalInNotifys_Type = Counter32
_CikeGlobalInNotifys_Object = MibScalar
cikeGlobalInNotifys = _CikeGlobalInNotifys_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 2, 1, 6),
    _CikeGlobalInNotifys_Type()
)
cikeGlobalInNotifys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikeGlobalInNotifys.setStatus("current")
if mibBuilder.loadTexts:
    cikeGlobalInNotifys.setUnits("Notification Payloads")
_CikeGlobalInP2Exchgs_Type = Counter32
_CikeGlobalInP2Exchgs_Object = MibScalar
cikeGlobalInP2Exchgs = _CikeGlobalInP2Exchgs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 2, 1, 7),
    _CikeGlobalInP2Exchgs_Type()
)
cikeGlobalInP2Exchgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikeGlobalInP2Exchgs.setStatus("current")
if mibBuilder.loadTexts:
    cikeGlobalInP2Exchgs.setUnits("SA Payloads")
_CikeGlobalInP2ExchgInvalids_Type = Counter32
_CikeGlobalInP2ExchgInvalids_Object = MibScalar
cikeGlobalInP2ExchgInvalids = _CikeGlobalInP2ExchgInvalids_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 2, 1, 8),
    _CikeGlobalInP2ExchgInvalids_Type()
)
cikeGlobalInP2ExchgInvalids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikeGlobalInP2ExchgInvalids.setStatus("current")
if mibBuilder.loadTexts:
    cikeGlobalInP2ExchgInvalids.setUnits("SA Payloads")
_CikeGlobalInP2ExchgRejects_Type = Counter32
_CikeGlobalInP2ExchgRejects_Object = MibScalar
cikeGlobalInP2ExchgRejects = _CikeGlobalInP2ExchgRejects_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 2, 1, 9),
    _CikeGlobalInP2ExchgRejects_Type()
)
cikeGlobalInP2ExchgRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikeGlobalInP2ExchgRejects.setStatus("current")
if mibBuilder.loadTexts:
    cikeGlobalInP2ExchgRejects.setUnits("SA Payloads")
_CikeGlobalInP2SaDelRequests_Type = Counter32
_CikeGlobalInP2SaDelRequests_Object = MibScalar
cikeGlobalInP2SaDelRequests = _CikeGlobalInP2SaDelRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 2, 1, 10),
    _CikeGlobalInP2SaDelRequests_Type()
)
cikeGlobalInP2SaDelRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikeGlobalInP2SaDelRequests.setStatus("current")
if mibBuilder.loadTexts:
    cikeGlobalInP2SaDelRequests.setUnits("Notification Payloads")
_CikeGlobalOutOctets_Type = Counter32
_CikeGlobalOutOctets_Object = MibScalar
cikeGlobalOutOctets = _CikeGlobalOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 2, 1, 11),
    _CikeGlobalOutOctets_Type()
)
cikeGlobalOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikeGlobalOutOctets.setStatus("current")
if mibBuilder.loadTexts:
    cikeGlobalOutOctets.setUnits("Octets")
_CikeGlobalOutPkts_Type = Counter32
_CikeGlobalOutPkts_Object = MibScalar
cikeGlobalOutPkts = _CikeGlobalOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 2, 1, 12),
    _CikeGlobalOutPkts_Type()
)
cikeGlobalOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikeGlobalOutPkts.setStatus("current")
if mibBuilder.loadTexts:
    cikeGlobalOutPkts.setUnits("Packets")
_CikeGlobalOutDropPkts_Type = Counter32
_CikeGlobalOutDropPkts_Object = MibScalar
cikeGlobalOutDropPkts = _CikeGlobalOutDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 2, 1, 13),
    _CikeGlobalOutDropPkts_Type()
)
cikeGlobalOutDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikeGlobalOutDropPkts.setStatus("current")
if mibBuilder.loadTexts:
    cikeGlobalOutDropPkts.setUnits("Packets")
_CikeGlobalOutNotifys_Type = Counter32
_CikeGlobalOutNotifys_Object = MibScalar
cikeGlobalOutNotifys = _CikeGlobalOutNotifys_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 2, 1, 14),
    _CikeGlobalOutNotifys_Type()
)
cikeGlobalOutNotifys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikeGlobalOutNotifys.setStatus("current")
if mibBuilder.loadTexts:
    cikeGlobalOutNotifys.setUnits("Notification Payloads")
_CikeGlobalOutP2Exchgs_Type = Counter32
_CikeGlobalOutP2Exchgs_Object = MibScalar
cikeGlobalOutP2Exchgs = _CikeGlobalOutP2Exchgs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 2, 1, 15),
    _CikeGlobalOutP2Exchgs_Type()
)
cikeGlobalOutP2Exchgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikeGlobalOutP2Exchgs.setStatus("current")
if mibBuilder.loadTexts:
    cikeGlobalOutP2Exchgs.setUnits("SA Payloads")
_CikeGlobalOutP2ExchgInvalids_Type = Counter32
_CikeGlobalOutP2ExchgInvalids_Object = MibScalar
cikeGlobalOutP2ExchgInvalids = _CikeGlobalOutP2ExchgInvalids_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 2, 1, 16),
    _CikeGlobalOutP2ExchgInvalids_Type()
)
cikeGlobalOutP2ExchgInvalids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikeGlobalOutP2ExchgInvalids.setStatus("current")
if mibBuilder.loadTexts:
    cikeGlobalOutP2ExchgInvalids.setUnits("SA Payloads")
_CikeGlobalOutP2ExchgRejects_Type = Counter32
_CikeGlobalOutP2ExchgRejects_Object = MibScalar
cikeGlobalOutP2ExchgRejects = _CikeGlobalOutP2ExchgRejects_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 2, 1, 17),
    _CikeGlobalOutP2ExchgRejects_Type()
)
cikeGlobalOutP2ExchgRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikeGlobalOutP2ExchgRejects.setStatus("current")
if mibBuilder.loadTexts:
    cikeGlobalOutP2ExchgRejects.setUnits("SA Payloads")
_CikeGlobalOutP2SaDelRequests_Type = Counter32
_CikeGlobalOutP2SaDelRequests_Object = MibScalar
cikeGlobalOutP2SaDelRequests = _CikeGlobalOutP2SaDelRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 2, 1, 18),
    _CikeGlobalOutP2SaDelRequests_Type()
)
cikeGlobalOutP2SaDelRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikeGlobalOutP2SaDelRequests.setStatus("current")
if mibBuilder.loadTexts:
    cikeGlobalOutP2SaDelRequests.setUnits("Notification Payloads")
_CikeGlobalInitTunnels_Type = Counter32
_CikeGlobalInitTunnels_Object = MibScalar
cikeGlobalInitTunnels = _CikeGlobalInitTunnels_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 2, 1, 19),
    _CikeGlobalInitTunnels_Type()
)
cikeGlobalInitTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikeGlobalInitTunnels.setStatus("current")
if mibBuilder.loadTexts:
    cikeGlobalInitTunnels.setUnits("SAs")
_CikeGlobalInitTunnelFails_Type = Counter32
_CikeGlobalInitTunnelFails_Object = MibScalar
cikeGlobalInitTunnelFails = _CikeGlobalInitTunnelFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 2, 1, 20),
    _CikeGlobalInitTunnelFails_Type()
)
cikeGlobalInitTunnelFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikeGlobalInitTunnelFails.setStatus("current")
if mibBuilder.loadTexts:
    cikeGlobalInitTunnelFails.setUnits("SAs")
_CikeGlobalRespTunnelFails_Type = Counter32
_CikeGlobalRespTunnelFails_Object = MibScalar
cikeGlobalRespTunnelFails = _CikeGlobalRespTunnelFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 2, 1, 21),
    _CikeGlobalRespTunnelFails_Type()
)
cikeGlobalRespTunnelFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikeGlobalRespTunnelFails.setStatus("current")
if mibBuilder.loadTexts:
    cikeGlobalRespTunnelFails.setUnits("SAs")
_CikeGlobalSysCapFails_Type = Counter32
_CikeGlobalSysCapFails_Object = MibScalar
cikeGlobalSysCapFails = _CikeGlobalSysCapFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 2, 1, 22),
    _CikeGlobalSysCapFails_Type()
)
cikeGlobalSysCapFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikeGlobalSysCapFails.setStatus("current")
if mibBuilder.loadTexts:
    cikeGlobalSysCapFails.setUnits("Failures")
_CikeGlobalAuthFails_Type = Counter32
_CikeGlobalAuthFails_Object = MibScalar
cikeGlobalAuthFails = _CikeGlobalAuthFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 2, 1, 23),
    _CikeGlobalAuthFails_Type()
)
cikeGlobalAuthFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikeGlobalAuthFails.setStatus("current")
if mibBuilder.loadTexts:
    cikeGlobalAuthFails.setUnits("Failures")
_CikeGlobalDecryptFails_Type = Counter32
_CikeGlobalDecryptFails_Object = MibScalar
cikeGlobalDecryptFails = _CikeGlobalDecryptFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 2, 1, 24),
    _CikeGlobalDecryptFails_Type()
)
cikeGlobalDecryptFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikeGlobalDecryptFails.setStatus("current")
if mibBuilder.loadTexts:
    cikeGlobalDecryptFails.setUnits("Failures")
_CikeGlobalHashValidFails_Type = Counter32
_CikeGlobalHashValidFails_Object = MibScalar
cikeGlobalHashValidFails = _CikeGlobalHashValidFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 2, 1, 25),
    _CikeGlobalHashValidFails_Type()
)
cikeGlobalHashValidFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikeGlobalHashValidFails.setStatus("current")
if mibBuilder.loadTexts:
    cikeGlobalHashValidFails.setUnits("Failures")
_CikeGlobalNoSaFails_Type = Counter32
_CikeGlobalNoSaFails_Object = MibScalar
cikeGlobalNoSaFails = _CikeGlobalNoSaFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 2, 1, 26),
    _CikeGlobalNoSaFails_Type()
)
cikeGlobalNoSaFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikeGlobalNoSaFails.setStatus("current")
if mibBuilder.loadTexts:
    cikeGlobalNoSaFails.setUnits("Failures")
_CikePeerTable_Object = MibTable
cikePeerTable = _CikePeerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cikePeerTable.setStatus("current")
_CikePeerEntry_Object = MibTableRow
cikePeerEntry = _CikePeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 2, 2, 1)
)
cikePeerEntry.setIndexNames(
    (0, "CISCO-IPSEC-FLOW-MONITOR-MIB", "cikePeerLocalType"),
    (0, "CISCO-IPSEC-FLOW-MONITOR-MIB", "cikePeerLocalValue"),
    (0, "CISCO-IPSEC-FLOW-MONITOR-MIB", "cikePeerRemoteType"),
    (0, "CISCO-IPSEC-FLOW-MONITOR-MIB", "cikePeerRemoteValue"),
    (0, "CISCO-IPSEC-FLOW-MONITOR-MIB", "cikePeerIntIndex"),
)
if mibBuilder.loadTexts:
    cikePeerEntry.setStatus("current")
_CikePeerLocalType_Type = IkePeerType
_CikePeerLocalType_Object = MibTableColumn
cikePeerLocalType = _CikePeerLocalType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 2, 2, 1, 1),
    _CikePeerLocalType_Type()
)
cikePeerLocalType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cikePeerLocalType.setStatus("current")
_CikePeerLocalValue_Type = DisplayString
_CikePeerLocalValue_Object = MibTableColumn
cikePeerLocalValue = _CikePeerLocalValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 2, 2, 1, 2),
    _CikePeerLocalValue_Type()
)
cikePeerLocalValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cikePeerLocalValue.setStatus("current")
_CikePeerRemoteType_Type = IkePeerType
_CikePeerRemoteType_Object = MibTableColumn
cikePeerRemoteType = _CikePeerRemoteType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 2, 2, 1, 3),
    _CikePeerRemoteType_Type()
)
cikePeerRemoteType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cikePeerRemoteType.setStatus("current")
_CikePeerRemoteValue_Type = DisplayString
_CikePeerRemoteValue_Object = MibTableColumn
cikePeerRemoteValue = _CikePeerRemoteValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 2, 2, 1, 4),
    _CikePeerRemoteValue_Type()
)
cikePeerRemoteValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cikePeerRemoteValue.setStatus("current")


class _CikePeerIntIndex_Type(Integer32):
    """Custom type cikePeerIntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CikePeerIntIndex_Type.__name__ = "Integer32"
_CikePeerIntIndex_Object = MibTableColumn
cikePeerIntIndex = _CikePeerIntIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 2, 2, 1, 5),
    _CikePeerIntIndex_Type()
)
cikePeerIntIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cikePeerIntIndex.setStatus("current")
_CikePeerLocalAddr_Type = IPSIpAddress
_CikePeerLocalAddr_Object = MibTableColumn
cikePeerLocalAddr = _CikePeerLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 2, 2, 1, 6),
    _CikePeerLocalAddr_Type()
)
cikePeerLocalAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikePeerLocalAddr.setStatus("current")
_CikePeerRemoteAddr_Type = IPSIpAddress
_CikePeerRemoteAddr_Object = MibTableColumn
cikePeerRemoteAddr = _CikePeerRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 2, 2, 1, 7),
    _CikePeerRemoteAddr_Type()
)
cikePeerRemoteAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikePeerRemoteAddr.setStatus("current")
_CikePeerActiveTime_Type = TimeInterval
_CikePeerActiveTime_Object = MibTableColumn
cikePeerActiveTime = _CikePeerActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 2, 2, 1, 8),
    _CikePeerActiveTime_Type()
)
cikePeerActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikePeerActiveTime.setStatus("current")


class _CikePeerActiveTunnelIndex_Type(Integer32):
    """Custom type cikePeerActiveTunnelIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CikePeerActiveTunnelIndex_Type.__name__ = "Integer32"
_CikePeerActiveTunnelIndex_Object = MibTableColumn
cikePeerActiveTunnelIndex = _CikePeerActiveTunnelIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 2, 2, 1, 9),
    _CikePeerActiveTunnelIndex_Type()
)
cikePeerActiveTunnelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikePeerActiveTunnelIndex.setStatus("current")
_CikeTunnelTable_Object = MibTable
cikeTunnelTable = _CikeTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 2, 3)
)
if mibBuilder.loadTexts:
    cikeTunnelTable.setStatus("current")
_CikeTunnelEntry_Object = MibTableRow
cikeTunnelEntry = _CikeTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 2, 3, 1)
)
cikeTunnelEntry.setIndexNames(
    (0, "CISCO-IPSEC-FLOW-MONITOR-MIB", "cikeTunIndex"),
)
if mibBuilder.loadTexts:
    cikeTunnelEntry.setStatus("current")


class _CikeTunIndex_Type(Integer32):
    """Custom type cikeTunIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CikeTunIndex_Type.__name__ = "Integer32"
_CikeTunIndex_Object = MibTableColumn
cikeTunIndex = _CikeTunIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 2, 3, 1, 1),
    _CikeTunIndex_Type()
)
cikeTunIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cikeTunIndex.setStatus("current")
_CikeTunLocalType_Type = IkePeerType
_CikeTunLocalType_Object = MibTableColumn
cikeTunLocalType = _CikeTunLocalType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 2, 3, 1, 2),
    _CikeTunLocalType_Type()
)
cikeTunLocalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikeTunLocalType.setStatus("current")
_CikeTunLocalValue_Type = DisplayString
_CikeTunLocalValue_Object = MibTableColumn
cikeTunLocalValue = _CikeTunLocalValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 2, 3, 1, 3),
    _CikeTunLocalValue_Type()
)
cikeTunLocalValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikeTunLocalValue.setStatus("current")
_CikeTunLocalAddr_Type = IPSIpAddress
_CikeTunLocalAddr_Object = MibTableColumn
cikeTunLocalAddr = _CikeTunLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 2, 3, 1, 4),
    _CikeTunLocalAddr_Type()
)
cikeTunLocalAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikeTunLocalAddr.setStatus("current")
_CikeTunLocalName_Type = DisplayString
_CikeTunLocalName_Object = MibTableColumn
cikeTunLocalName = _CikeTunLocalName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 2, 3, 1, 5),
    _CikeTunLocalName_Type()
)
cikeTunLocalName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikeTunLocalName.setStatus("current")
_CikeTunRemoteType_Type = IkePeerType
_CikeTunRemoteType_Object = MibTableColumn
cikeTunRemoteType = _CikeTunRemoteType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 2, 3, 1, 6),
    _CikeTunRemoteType_Type()
)
cikeTunRemoteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikeTunRemoteType.setStatus("current")
_CikeTunRemoteValue_Type = DisplayString
_CikeTunRemoteValue_Object = MibTableColumn
cikeTunRemoteValue = _CikeTunRemoteValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 2, 3, 1, 7),
    _CikeTunRemoteValue_Type()
)
cikeTunRemoteValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikeTunRemoteValue.setStatus("current")
_CikeTunRemoteAddr_Type = IPSIpAddress
_CikeTunRemoteAddr_Object = MibTableColumn
cikeTunRemoteAddr = _CikeTunRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 2, 3, 1, 8),
    _CikeTunRemoteAddr_Type()
)
cikeTunRemoteAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikeTunRemoteAddr.setStatus("current")
_CikeTunRemoteName_Type = DisplayString
_CikeTunRemoteName_Object = MibTableColumn
cikeTunRemoteName = _CikeTunRemoteName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 2, 3, 1, 9),
    _CikeTunRemoteName_Type()
)
cikeTunRemoteName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikeTunRemoteName.setStatus("current")
_CikeTunNegoMode_Type = IkeNegoMode
_CikeTunNegoMode_Object = MibTableColumn
cikeTunNegoMode = _CikeTunNegoMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 2, 3, 1, 10),
    _CikeTunNegoMode_Type()
)
cikeTunNegoMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikeTunNegoMode.setStatus("current")
_CikeTunDiffHellmanGrp_Type = DiffHellmanGrp
_CikeTunDiffHellmanGrp_Object = MibTableColumn
cikeTunDiffHellmanGrp = _CikeTunDiffHellmanGrp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 2, 3, 1, 11),
    _CikeTunDiffHellmanGrp_Type()
)
cikeTunDiffHellmanGrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikeTunDiffHellmanGrp.setStatus("current")
_CikeTunEncryptAlgo_Type = EncryptAlgo
_CikeTunEncryptAlgo_Object = MibTableColumn
cikeTunEncryptAlgo = _CikeTunEncryptAlgo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 2, 3, 1, 12),
    _CikeTunEncryptAlgo_Type()
)
cikeTunEncryptAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikeTunEncryptAlgo.setStatus("current")
_CikeTunHashAlgo_Type = IkeHashAlgo
_CikeTunHashAlgo_Object = MibTableColumn
cikeTunHashAlgo = _CikeTunHashAlgo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 2, 3, 1, 13),
    _CikeTunHashAlgo_Type()
)
cikeTunHashAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikeTunHashAlgo.setStatus("current")
_CikeTunAuthMethod_Type = IkeAuthMethod
_CikeTunAuthMethod_Object = MibTableColumn
cikeTunAuthMethod = _CikeTunAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 2, 3, 1, 14),
    _CikeTunAuthMethod_Type()
)
cikeTunAuthMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikeTunAuthMethod.setStatus("current")


class _CikeTunLifeTime_Type(Integer32):
    """Custom type cikeTunLifeTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CikeTunLifeTime_Type.__name__ = "Integer32"
_CikeTunLifeTime_Object = MibTableColumn
cikeTunLifeTime = _CikeTunLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 2, 3, 1, 15),
    _CikeTunLifeTime_Type()
)
cikeTunLifeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikeTunLifeTime.setStatus("current")
if mibBuilder.loadTexts:
    cikeTunLifeTime.setUnits("seconds")
_CikeTunActiveTime_Type = TimeInterval
_CikeTunActiveTime_Object = MibTableColumn
cikeTunActiveTime = _CikeTunActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 2, 3, 1, 16),
    _CikeTunActiveTime_Type()
)
cikeTunActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikeTunActiveTime.setStatus("current")


class _CikeTunSaRefreshThreshold_Type(Integer32):
    """Custom type cikeTunSaRefreshThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CikeTunSaRefreshThreshold_Type.__name__ = "Integer32"
_CikeTunSaRefreshThreshold_Object = MibTableColumn
cikeTunSaRefreshThreshold = _CikeTunSaRefreshThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 2, 3, 1, 17),
    _CikeTunSaRefreshThreshold_Type()
)
cikeTunSaRefreshThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikeTunSaRefreshThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cikeTunSaRefreshThreshold.setUnits("seconds")
_CikeTunTotalRefreshes_Type = Counter32
_CikeTunTotalRefreshes_Object = MibTableColumn
cikeTunTotalRefreshes = _CikeTunTotalRefreshes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 2, 3, 1, 18),
    _CikeTunTotalRefreshes_Type()
)
cikeTunTotalRefreshes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikeTunTotalRefreshes.setStatus("current")
if mibBuilder.loadTexts:
    cikeTunTotalRefreshes.setUnits("QM Exchanges")
_CikeTunInOctets_Type = Counter32
_CikeTunInOctets_Object = MibTableColumn
cikeTunInOctets = _CikeTunInOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 2, 3, 1, 19),
    _CikeTunInOctets_Type()
)
cikeTunInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikeTunInOctets.setStatus("current")
if mibBuilder.loadTexts:
    cikeTunInOctets.setUnits("Octets")
_CikeTunInPkts_Type = Counter32
_CikeTunInPkts_Object = MibTableColumn
cikeTunInPkts = _CikeTunInPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 2, 3, 1, 20),
    _CikeTunInPkts_Type()
)
cikeTunInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikeTunInPkts.setStatus("current")
if mibBuilder.loadTexts:
    cikeTunInPkts.setUnits("Packets")
_CikeTunInDropPkts_Type = Counter32
_CikeTunInDropPkts_Object = MibTableColumn
cikeTunInDropPkts = _CikeTunInDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 2, 3, 1, 21),
    _CikeTunInDropPkts_Type()
)
cikeTunInDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikeTunInDropPkts.setStatus("current")
if mibBuilder.loadTexts:
    cikeTunInDropPkts.setUnits("Packets")
_CikeTunInNotifys_Type = Counter32
_CikeTunInNotifys_Object = MibTableColumn
cikeTunInNotifys = _CikeTunInNotifys_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 2, 3, 1, 22),
    _CikeTunInNotifys_Type()
)
cikeTunInNotifys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikeTunInNotifys.setStatus("current")
if mibBuilder.loadTexts:
    cikeTunInNotifys.setUnits("Notification Payloads")
_CikeTunInP2Exchgs_Type = Counter32
_CikeTunInP2Exchgs_Object = MibTableColumn
cikeTunInP2Exchgs = _CikeTunInP2Exchgs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 2, 3, 1, 23),
    _CikeTunInP2Exchgs_Type()
)
cikeTunInP2Exchgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikeTunInP2Exchgs.setStatus("current")
if mibBuilder.loadTexts:
    cikeTunInP2Exchgs.setUnits("SA Payloads")
_CikeTunInP2ExchgInvalids_Type = Counter32
_CikeTunInP2ExchgInvalids_Object = MibTableColumn
cikeTunInP2ExchgInvalids = _CikeTunInP2ExchgInvalids_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 2, 3, 1, 24),
    _CikeTunInP2ExchgInvalids_Type()
)
cikeTunInP2ExchgInvalids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikeTunInP2ExchgInvalids.setStatus("current")
if mibBuilder.loadTexts:
    cikeTunInP2ExchgInvalids.setUnits("SA Payloads")
_CikeTunInP2ExchgRejects_Type = Counter32
_CikeTunInP2ExchgRejects_Object = MibTableColumn
cikeTunInP2ExchgRejects = _CikeTunInP2ExchgRejects_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 2, 3, 1, 25),
    _CikeTunInP2ExchgRejects_Type()
)
cikeTunInP2ExchgRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikeTunInP2ExchgRejects.setStatus("current")
if mibBuilder.loadTexts:
    cikeTunInP2ExchgRejects.setUnits("SA Payloads")
_CikeTunInP2SaDelRequests_Type = Counter32
_CikeTunInP2SaDelRequests_Object = MibTableColumn
cikeTunInP2SaDelRequests = _CikeTunInP2SaDelRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 2, 3, 1, 26),
    _CikeTunInP2SaDelRequests_Type()
)
cikeTunInP2SaDelRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikeTunInP2SaDelRequests.setStatus("current")
if mibBuilder.loadTexts:
    cikeTunInP2SaDelRequests.setUnits("Notification Payloads")
_CikeTunOutOctets_Type = Counter32
_CikeTunOutOctets_Object = MibTableColumn
cikeTunOutOctets = _CikeTunOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 2, 3, 1, 27),
    _CikeTunOutOctets_Type()
)
cikeTunOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikeTunOutOctets.setStatus("current")
if mibBuilder.loadTexts:
    cikeTunOutOctets.setUnits("Octets")
_CikeTunOutPkts_Type = Counter32
_CikeTunOutPkts_Object = MibTableColumn
cikeTunOutPkts = _CikeTunOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 2, 3, 1, 28),
    _CikeTunOutPkts_Type()
)
cikeTunOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikeTunOutPkts.setStatus("current")
if mibBuilder.loadTexts:
    cikeTunOutPkts.setUnits("Packets")
_CikeTunOutDropPkts_Type = Counter32
_CikeTunOutDropPkts_Object = MibTableColumn
cikeTunOutDropPkts = _CikeTunOutDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 2, 3, 1, 29),
    _CikeTunOutDropPkts_Type()
)
cikeTunOutDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikeTunOutDropPkts.setStatus("current")
if mibBuilder.loadTexts:
    cikeTunOutDropPkts.setUnits("Packets")
_CikeTunOutNotifys_Type = Counter32
_CikeTunOutNotifys_Object = MibTableColumn
cikeTunOutNotifys = _CikeTunOutNotifys_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 2, 3, 1, 30),
    _CikeTunOutNotifys_Type()
)
cikeTunOutNotifys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikeTunOutNotifys.setStatus("current")
if mibBuilder.loadTexts:
    cikeTunOutNotifys.setUnits("Notification Payloads")
_CikeTunOutP2Exchgs_Type = Counter32
_CikeTunOutP2Exchgs_Object = MibTableColumn
cikeTunOutP2Exchgs = _CikeTunOutP2Exchgs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 2, 3, 1, 31),
    _CikeTunOutP2Exchgs_Type()
)
cikeTunOutP2Exchgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikeTunOutP2Exchgs.setStatus("current")
if mibBuilder.loadTexts:
    cikeTunOutP2Exchgs.setUnits("SA Payloads")
_CikeTunOutP2ExchgInvalids_Type = Counter32
_CikeTunOutP2ExchgInvalids_Object = MibTableColumn
cikeTunOutP2ExchgInvalids = _CikeTunOutP2ExchgInvalids_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 2, 3, 1, 32),
    _CikeTunOutP2ExchgInvalids_Type()
)
cikeTunOutP2ExchgInvalids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikeTunOutP2ExchgInvalids.setStatus("current")
if mibBuilder.loadTexts:
    cikeTunOutP2ExchgInvalids.setUnits("SA Payloads")
_CikeTunOutP2ExchgRejects_Type = Counter32
_CikeTunOutP2ExchgRejects_Object = MibTableColumn
cikeTunOutP2ExchgRejects = _CikeTunOutP2ExchgRejects_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 2, 3, 1, 33),
    _CikeTunOutP2ExchgRejects_Type()
)
cikeTunOutP2ExchgRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikeTunOutP2ExchgRejects.setStatus("current")
if mibBuilder.loadTexts:
    cikeTunOutP2ExchgRejects.setUnits("SA Payloads")
_CikeTunOutP2SaDelRequests_Type = Counter32
_CikeTunOutP2SaDelRequests_Object = MibTableColumn
cikeTunOutP2SaDelRequests = _CikeTunOutP2SaDelRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 2, 3, 1, 34),
    _CikeTunOutP2SaDelRequests_Type()
)
cikeTunOutP2SaDelRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikeTunOutP2SaDelRequests.setStatus("current")
if mibBuilder.loadTexts:
    cikeTunOutP2SaDelRequests.setUnits("Notification Payloads")
_CikeTunStatus_Type = TunnelStatus
_CikeTunStatus_Object = MibTableColumn
cikeTunStatus = _CikeTunStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 2, 3, 1, 35),
    _CikeTunStatus_Type()
)
cikeTunStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cikeTunStatus.setStatus("current")
_CikePeerCorrTable_Object = MibTable
cikePeerCorrTable = _CikePeerCorrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 2, 4)
)
if mibBuilder.loadTexts:
    cikePeerCorrTable.setStatus("current")
_CikePeerCorrEntry_Object = MibTableRow
cikePeerCorrEntry = _CikePeerCorrEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 2, 4, 1)
)
cikePeerCorrEntry.setIndexNames(
    (0, "CISCO-IPSEC-FLOW-MONITOR-MIB", "cikePeerCorrLocalType"),
    (0, "CISCO-IPSEC-FLOW-MONITOR-MIB", "cikePeerCorrLocalValue"),
    (0, "CISCO-IPSEC-FLOW-MONITOR-MIB", "cikePeerCorrRemoteType"),
    (0, "CISCO-IPSEC-FLOW-MONITOR-MIB", "cikePeerCorrRemoteValue"),
    (0, "CISCO-IPSEC-FLOW-MONITOR-MIB", "cikePeerCorrIntIndex"),
    (0, "CISCO-IPSEC-FLOW-MONITOR-MIB", "cikePeerCorrSeqNum"),
)
if mibBuilder.loadTexts:
    cikePeerCorrEntry.setStatus("current")
_CikePeerCorrLocalType_Type = IkePeerType
_CikePeerCorrLocalType_Object = MibTableColumn
cikePeerCorrLocalType = _CikePeerCorrLocalType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 2, 4, 1, 1),
    _CikePeerCorrLocalType_Type()
)
cikePeerCorrLocalType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cikePeerCorrLocalType.setStatus("current")
_CikePeerCorrLocalValue_Type = DisplayString
_CikePeerCorrLocalValue_Object = MibTableColumn
cikePeerCorrLocalValue = _CikePeerCorrLocalValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 2, 4, 1, 2),
    _CikePeerCorrLocalValue_Type()
)
cikePeerCorrLocalValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cikePeerCorrLocalValue.setStatus("current")
_CikePeerCorrRemoteType_Type = IkePeerType
_CikePeerCorrRemoteType_Object = MibTableColumn
cikePeerCorrRemoteType = _CikePeerCorrRemoteType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 2, 4, 1, 3),
    _CikePeerCorrRemoteType_Type()
)
cikePeerCorrRemoteType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cikePeerCorrRemoteType.setStatus("current")
_CikePeerCorrRemoteValue_Type = DisplayString
_CikePeerCorrRemoteValue_Object = MibTableColumn
cikePeerCorrRemoteValue = _CikePeerCorrRemoteValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 2, 4, 1, 4),
    _CikePeerCorrRemoteValue_Type()
)
cikePeerCorrRemoteValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cikePeerCorrRemoteValue.setStatus("current")


class _CikePeerCorrIntIndex_Type(Integer32):
    """Custom type cikePeerCorrIntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CikePeerCorrIntIndex_Type.__name__ = "Integer32"
_CikePeerCorrIntIndex_Object = MibTableColumn
cikePeerCorrIntIndex = _CikePeerCorrIntIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 2, 4, 1, 5),
    _CikePeerCorrIntIndex_Type()
)
cikePeerCorrIntIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cikePeerCorrIntIndex.setStatus("current")


class _CikePeerCorrSeqNum_Type(Integer32):
    """Custom type cikePeerCorrSeqNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CikePeerCorrSeqNum_Type.__name__ = "Integer32"
_CikePeerCorrSeqNum_Object = MibTableColumn
cikePeerCorrSeqNum = _CikePeerCorrSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 2, 4, 1, 6),
    _CikePeerCorrSeqNum_Type()
)
cikePeerCorrSeqNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cikePeerCorrSeqNum.setStatus("current")


class _CikePeerCorrIpSecTunIndex_Type(Integer32):
    """Custom type cikePeerCorrIpSecTunIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CikePeerCorrIpSecTunIndex_Type.__name__ = "Integer32"
_CikePeerCorrIpSecTunIndex_Object = MibTableColumn
cikePeerCorrIpSecTunIndex = _CikePeerCorrIpSecTunIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 2, 4, 1, 7),
    _CikePeerCorrIpSecTunIndex_Type()
)
cikePeerCorrIpSecTunIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikePeerCorrIpSecTunIndex.setStatus("current")
_CikePhase1GWStatsTable_Object = MibTable
cikePhase1GWStatsTable = _CikePhase1GWStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 2, 5)
)
if mibBuilder.loadTexts:
    cikePhase1GWStatsTable.setStatus("current")
_CikePhase1GWStatsEntry_Object = MibTableRow
cikePhase1GWStatsEntry = _CikePhase1GWStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 2, 5, 1)
)
cikePhase1GWStatsEntry.setIndexNames(
    (0, "CISCO-MEDIA-GATEWAY-MIB", "cmgwIndex"),
)
if mibBuilder.loadTexts:
    cikePhase1GWStatsEntry.setStatus("current")
_CikePhase1GWActiveTunnels_Type = Gauge32
_CikePhase1GWActiveTunnels_Object = MibTableColumn
cikePhase1GWActiveTunnels = _CikePhase1GWActiveTunnels_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 2, 5, 1, 1),
    _CikePhase1GWActiveTunnels_Type()
)
cikePhase1GWActiveTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikePhase1GWActiveTunnels.setStatus("current")
_CikePhase1GWPreviousTunnels_Type = Counter32
_CikePhase1GWPreviousTunnels_Object = MibTableColumn
cikePhase1GWPreviousTunnels = _CikePhase1GWPreviousTunnels_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 2, 5, 1, 2),
    _CikePhase1GWPreviousTunnels_Type()
)
cikePhase1GWPreviousTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikePhase1GWPreviousTunnels.setStatus("current")
if mibBuilder.loadTexts:
    cikePhase1GWPreviousTunnels.setUnits("SAs")
_CikePhase1GWInOctets_Type = Counter32
_CikePhase1GWInOctets_Object = MibTableColumn
cikePhase1GWInOctets = _CikePhase1GWInOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 2, 5, 1, 3),
    _CikePhase1GWInOctets_Type()
)
cikePhase1GWInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikePhase1GWInOctets.setStatus("current")
if mibBuilder.loadTexts:
    cikePhase1GWInOctets.setUnits("Octets")
_CikePhase1GWInPkts_Type = Counter32
_CikePhase1GWInPkts_Object = MibTableColumn
cikePhase1GWInPkts = _CikePhase1GWInPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 2, 5, 1, 4),
    _CikePhase1GWInPkts_Type()
)
cikePhase1GWInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikePhase1GWInPkts.setStatus("current")
if mibBuilder.loadTexts:
    cikePhase1GWInPkts.setUnits("Packets")
_CikePhase1GWInDropPkts_Type = Counter32
_CikePhase1GWInDropPkts_Object = MibTableColumn
cikePhase1GWInDropPkts = _CikePhase1GWInDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 2, 5, 1, 5),
    _CikePhase1GWInDropPkts_Type()
)
cikePhase1GWInDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikePhase1GWInDropPkts.setStatus("current")
if mibBuilder.loadTexts:
    cikePhase1GWInDropPkts.setUnits("Packets")
_CikePhase1GWInNotifys_Type = Counter32
_CikePhase1GWInNotifys_Object = MibTableColumn
cikePhase1GWInNotifys = _CikePhase1GWInNotifys_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 2, 5, 1, 6),
    _CikePhase1GWInNotifys_Type()
)
cikePhase1GWInNotifys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikePhase1GWInNotifys.setStatus("current")
if mibBuilder.loadTexts:
    cikePhase1GWInNotifys.setUnits("Notification Payloads")
_CikePhase1GWInP2Exchgs_Type = Counter32
_CikePhase1GWInP2Exchgs_Object = MibTableColumn
cikePhase1GWInP2Exchgs = _CikePhase1GWInP2Exchgs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 2, 5, 1, 7),
    _CikePhase1GWInP2Exchgs_Type()
)
cikePhase1GWInP2Exchgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikePhase1GWInP2Exchgs.setStatus("current")
if mibBuilder.loadTexts:
    cikePhase1GWInP2Exchgs.setUnits("SA Payloads")
_CikePhase1GWInP2ExchgInvalids_Type = Counter32
_CikePhase1GWInP2ExchgInvalids_Object = MibTableColumn
cikePhase1GWInP2ExchgInvalids = _CikePhase1GWInP2ExchgInvalids_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 2, 5, 1, 8),
    _CikePhase1GWInP2ExchgInvalids_Type()
)
cikePhase1GWInP2ExchgInvalids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikePhase1GWInP2ExchgInvalids.setStatus("current")
if mibBuilder.loadTexts:
    cikePhase1GWInP2ExchgInvalids.setUnits("SA Payloads")
_CikePhase1GWInP2ExchgRejects_Type = Counter32
_CikePhase1GWInP2ExchgRejects_Object = MibTableColumn
cikePhase1GWInP2ExchgRejects = _CikePhase1GWInP2ExchgRejects_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 2, 5, 1, 9),
    _CikePhase1GWInP2ExchgRejects_Type()
)
cikePhase1GWInP2ExchgRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikePhase1GWInP2ExchgRejects.setStatus("current")
if mibBuilder.loadTexts:
    cikePhase1GWInP2ExchgRejects.setUnits("SA Payloads")
_CikePhase1GWInP2SaDelRequests_Type = Counter32
_CikePhase1GWInP2SaDelRequests_Object = MibTableColumn
cikePhase1GWInP2SaDelRequests = _CikePhase1GWInP2SaDelRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 2, 5, 1, 10),
    _CikePhase1GWInP2SaDelRequests_Type()
)
cikePhase1GWInP2SaDelRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikePhase1GWInP2SaDelRequests.setStatus("current")
if mibBuilder.loadTexts:
    cikePhase1GWInP2SaDelRequests.setUnits("Notification Payloads")
_CikePhase1GWOutOctets_Type = Counter32
_CikePhase1GWOutOctets_Object = MibTableColumn
cikePhase1GWOutOctets = _CikePhase1GWOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 2, 5, 1, 11),
    _CikePhase1GWOutOctets_Type()
)
cikePhase1GWOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikePhase1GWOutOctets.setStatus("current")
if mibBuilder.loadTexts:
    cikePhase1GWOutOctets.setUnits("Octets")
_CikePhase1GWOutPkts_Type = Counter32
_CikePhase1GWOutPkts_Object = MibTableColumn
cikePhase1GWOutPkts = _CikePhase1GWOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 2, 5, 1, 12),
    _CikePhase1GWOutPkts_Type()
)
cikePhase1GWOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikePhase1GWOutPkts.setStatus("current")
if mibBuilder.loadTexts:
    cikePhase1GWOutPkts.setUnits("Packets")
_CikePhase1GWOutDropPkts_Type = Counter32
_CikePhase1GWOutDropPkts_Object = MibTableColumn
cikePhase1GWOutDropPkts = _CikePhase1GWOutDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 2, 5, 1, 13),
    _CikePhase1GWOutDropPkts_Type()
)
cikePhase1GWOutDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikePhase1GWOutDropPkts.setStatus("current")
if mibBuilder.loadTexts:
    cikePhase1GWOutDropPkts.setUnits("Packets")
_CikePhase1GWOutNotifys_Type = Counter32
_CikePhase1GWOutNotifys_Object = MibTableColumn
cikePhase1GWOutNotifys = _CikePhase1GWOutNotifys_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 2, 5, 1, 14),
    _CikePhase1GWOutNotifys_Type()
)
cikePhase1GWOutNotifys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikePhase1GWOutNotifys.setStatus("current")
if mibBuilder.loadTexts:
    cikePhase1GWOutNotifys.setUnits("Notification Payloads")
_CikePhase1GWOutP2Exchgs_Type = Counter32
_CikePhase1GWOutP2Exchgs_Object = MibTableColumn
cikePhase1GWOutP2Exchgs = _CikePhase1GWOutP2Exchgs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 2, 5, 1, 15),
    _CikePhase1GWOutP2Exchgs_Type()
)
cikePhase1GWOutP2Exchgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikePhase1GWOutP2Exchgs.setStatus("current")
if mibBuilder.loadTexts:
    cikePhase1GWOutP2Exchgs.setUnits("SA Payloads")
_CikePhase1GWOutP2ExchgInvalids_Type = Counter32
_CikePhase1GWOutP2ExchgInvalids_Object = MibTableColumn
cikePhase1GWOutP2ExchgInvalids = _CikePhase1GWOutP2ExchgInvalids_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 2, 5, 1, 16),
    _CikePhase1GWOutP2ExchgInvalids_Type()
)
cikePhase1GWOutP2ExchgInvalids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikePhase1GWOutP2ExchgInvalids.setStatus("current")
if mibBuilder.loadTexts:
    cikePhase1GWOutP2ExchgInvalids.setUnits("SA Payloads")
_CikePhase1GWOutP2ExchgRejects_Type = Counter32
_CikePhase1GWOutP2ExchgRejects_Object = MibTableColumn
cikePhase1GWOutP2ExchgRejects = _CikePhase1GWOutP2ExchgRejects_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 2, 5, 1, 17),
    _CikePhase1GWOutP2ExchgRejects_Type()
)
cikePhase1GWOutP2ExchgRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikePhase1GWOutP2ExchgRejects.setStatus("current")
if mibBuilder.loadTexts:
    cikePhase1GWOutP2ExchgRejects.setUnits("SA Payloads")
_CikePhase1GWOutP2SaDelRequests_Type = Counter32
_CikePhase1GWOutP2SaDelRequests_Object = MibTableColumn
cikePhase1GWOutP2SaDelRequests = _CikePhase1GWOutP2SaDelRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 2, 5, 1, 18),
    _CikePhase1GWOutP2SaDelRequests_Type()
)
cikePhase1GWOutP2SaDelRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikePhase1GWOutP2SaDelRequests.setStatus("current")
if mibBuilder.loadTexts:
    cikePhase1GWOutP2SaDelRequests.setUnits("Notification Payloads")
_CikePhase1GWInitTunnels_Type = Counter32
_CikePhase1GWInitTunnels_Object = MibTableColumn
cikePhase1GWInitTunnels = _CikePhase1GWInitTunnels_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 2, 5, 1, 19),
    _CikePhase1GWInitTunnels_Type()
)
cikePhase1GWInitTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikePhase1GWInitTunnels.setStatus("current")
if mibBuilder.loadTexts:
    cikePhase1GWInitTunnels.setUnits("SAs")
_CikePhase1GWInitTunnelFails_Type = Counter32
_CikePhase1GWInitTunnelFails_Object = MibTableColumn
cikePhase1GWInitTunnelFails = _CikePhase1GWInitTunnelFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 2, 5, 1, 20),
    _CikePhase1GWInitTunnelFails_Type()
)
cikePhase1GWInitTunnelFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikePhase1GWInitTunnelFails.setStatus("current")
if mibBuilder.loadTexts:
    cikePhase1GWInitTunnelFails.setUnits("SAs")
_CikePhase1GWRespTunnelFails_Type = Counter32
_CikePhase1GWRespTunnelFails_Object = MibTableColumn
cikePhase1GWRespTunnelFails = _CikePhase1GWRespTunnelFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 2, 5, 1, 21),
    _CikePhase1GWRespTunnelFails_Type()
)
cikePhase1GWRespTunnelFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikePhase1GWRespTunnelFails.setStatus("current")
if mibBuilder.loadTexts:
    cikePhase1GWRespTunnelFails.setUnits("SAs")
_CikePhase1GWSysCapFails_Type = Counter32
_CikePhase1GWSysCapFails_Object = MibTableColumn
cikePhase1GWSysCapFails = _CikePhase1GWSysCapFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 2, 5, 1, 22),
    _CikePhase1GWSysCapFails_Type()
)
cikePhase1GWSysCapFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikePhase1GWSysCapFails.setStatus("current")
if mibBuilder.loadTexts:
    cikePhase1GWSysCapFails.setUnits("Failures")
_CikePhase1GWAuthFails_Type = Counter32
_CikePhase1GWAuthFails_Object = MibTableColumn
cikePhase1GWAuthFails = _CikePhase1GWAuthFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 2, 5, 1, 23),
    _CikePhase1GWAuthFails_Type()
)
cikePhase1GWAuthFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikePhase1GWAuthFails.setStatus("current")
if mibBuilder.loadTexts:
    cikePhase1GWAuthFails.setUnits("Failures")
_CikePhase1GWDecryptFails_Type = Counter32
_CikePhase1GWDecryptFails_Object = MibTableColumn
cikePhase1GWDecryptFails = _CikePhase1GWDecryptFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 2, 5, 1, 24),
    _CikePhase1GWDecryptFails_Type()
)
cikePhase1GWDecryptFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikePhase1GWDecryptFails.setStatus("current")
if mibBuilder.loadTexts:
    cikePhase1GWDecryptFails.setUnits("Failures")
_CikePhase1GWHashValidFails_Type = Counter32
_CikePhase1GWHashValidFails_Object = MibTableColumn
cikePhase1GWHashValidFails = _CikePhase1GWHashValidFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 2, 5, 1, 25),
    _CikePhase1GWHashValidFails_Type()
)
cikePhase1GWHashValidFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikePhase1GWHashValidFails.setStatus("current")
if mibBuilder.loadTexts:
    cikePhase1GWHashValidFails.setUnits("Failures")
_CikePhase1GWNoSaFails_Type = Counter32
_CikePhase1GWNoSaFails_Object = MibTableColumn
cikePhase1GWNoSaFails = _CikePhase1GWNoSaFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 2, 5, 1, 26),
    _CikePhase1GWNoSaFails_Type()
)
cikePhase1GWNoSaFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikePhase1GWNoSaFails.setStatus("current")
if mibBuilder.loadTexts:
    cikePhase1GWNoSaFails.setUnits("Failures")
_CipSecPhaseTwo_ObjectIdentity = ObjectIdentity
cipSecPhaseTwo = _CipSecPhaseTwo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3)
)
_CipSecGlobalStats_ObjectIdentity = ObjectIdentity
cipSecGlobalStats = _CipSecGlobalStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 1)
)
_CipSecGlobalActiveTunnels_Type = Gauge32
_CipSecGlobalActiveTunnels_Object = MibScalar
cipSecGlobalActiveTunnels = _CipSecGlobalActiveTunnels_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 1, 1),
    _CipSecGlobalActiveTunnels_Type()
)
cipSecGlobalActiveTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecGlobalActiveTunnels.setStatus("current")
_CipSecGlobalPreviousTunnels_Type = Counter32
_CipSecGlobalPreviousTunnels_Object = MibScalar
cipSecGlobalPreviousTunnels = _CipSecGlobalPreviousTunnels_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 1, 2),
    _CipSecGlobalPreviousTunnels_Type()
)
cipSecGlobalPreviousTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecGlobalPreviousTunnels.setStatus("current")
if mibBuilder.loadTexts:
    cipSecGlobalPreviousTunnels.setUnits("Phase-2 Tunnels")
_CipSecGlobalInOctets_Type = Counter32
_CipSecGlobalInOctets_Object = MibScalar
cipSecGlobalInOctets = _CipSecGlobalInOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 1, 3),
    _CipSecGlobalInOctets_Type()
)
cipSecGlobalInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecGlobalInOctets.setStatus("current")
if mibBuilder.loadTexts:
    cipSecGlobalInOctets.setUnits("Octets")
_CipSecGlobalHcInOctets_Type = Counter64
_CipSecGlobalHcInOctets_Object = MibScalar
cipSecGlobalHcInOctets = _CipSecGlobalHcInOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 1, 4),
    _CipSecGlobalHcInOctets_Type()
)
cipSecGlobalHcInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecGlobalHcInOctets.setStatus("current")
_CipSecGlobalInOctWraps_Type = Counter32
_CipSecGlobalInOctWraps_Object = MibScalar
cipSecGlobalInOctWraps = _CipSecGlobalInOctWraps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 1, 5),
    _CipSecGlobalInOctWraps_Type()
)
cipSecGlobalInOctWraps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecGlobalInOctWraps.setStatus("current")
if mibBuilder.loadTexts:
    cipSecGlobalInOctWraps.setUnits("Integral units")
_CipSecGlobalInDecompOctets_Type = Counter32
_CipSecGlobalInDecompOctets_Object = MibScalar
cipSecGlobalInDecompOctets = _CipSecGlobalInDecompOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 1, 6),
    _CipSecGlobalInDecompOctets_Type()
)
cipSecGlobalInDecompOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecGlobalInDecompOctets.setStatus("current")
if mibBuilder.loadTexts:
    cipSecGlobalInDecompOctets.setUnits("Octets")
_CipSecGlobalHcInDecompOctets_Type = Counter64
_CipSecGlobalHcInDecompOctets_Object = MibScalar
cipSecGlobalHcInDecompOctets = _CipSecGlobalHcInDecompOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 1, 7),
    _CipSecGlobalHcInDecompOctets_Type()
)
cipSecGlobalHcInDecompOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecGlobalHcInDecompOctets.setStatus("current")
_CipSecGlobalInDecompOctWraps_Type = Counter32
_CipSecGlobalInDecompOctWraps_Object = MibScalar
cipSecGlobalInDecompOctWraps = _CipSecGlobalInDecompOctWraps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 1, 8),
    _CipSecGlobalInDecompOctWraps_Type()
)
cipSecGlobalInDecompOctWraps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecGlobalInDecompOctWraps.setStatus("current")
if mibBuilder.loadTexts:
    cipSecGlobalInDecompOctWraps.setUnits("Integral units")
_CipSecGlobalInPkts_Type = Counter32
_CipSecGlobalInPkts_Object = MibScalar
cipSecGlobalInPkts = _CipSecGlobalInPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 1, 9),
    _CipSecGlobalInPkts_Type()
)
cipSecGlobalInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecGlobalInPkts.setStatus("current")
if mibBuilder.loadTexts:
    cipSecGlobalInPkts.setUnits("Packets")
_CipSecGlobalInDrops_Type = Counter32
_CipSecGlobalInDrops_Object = MibScalar
cipSecGlobalInDrops = _CipSecGlobalInDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 1, 10),
    _CipSecGlobalInDrops_Type()
)
cipSecGlobalInDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecGlobalInDrops.setStatus("current")
if mibBuilder.loadTexts:
    cipSecGlobalInDrops.setUnits("Packets")
_CipSecGlobalInReplayDrops_Type = Counter32
_CipSecGlobalInReplayDrops_Object = MibScalar
cipSecGlobalInReplayDrops = _CipSecGlobalInReplayDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 1, 11),
    _CipSecGlobalInReplayDrops_Type()
)
cipSecGlobalInReplayDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecGlobalInReplayDrops.setStatus("current")
if mibBuilder.loadTexts:
    cipSecGlobalInReplayDrops.setUnits("Packets")
_CipSecGlobalInAuths_Type = Counter32
_CipSecGlobalInAuths_Object = MibScalar
cipSecGlobalInAuths = _CipSecGlobalInAuths_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 1, 12),
    _CipSecGlobalInAuths_Type()
)
cipSecGlobalInAuths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecGlobalInAuths.setStatus("current")
if mibBuilder.loadTexts:
    cipSecGlobalInAuths.setUnits("Events")
_CipSecGlobalInAuthFails_Type = Counter32
_CipSecGlobalInAuthFails_Object = MibScalar
cipSecGlobalInAuthFails = _CipSecGlobalInAuthFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 1, 13),
    _CipSecGlobalInAuthFails_Type()
)
cipSecGlobalInAuthFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecGlobalInAuthFails.setStatus("current")
if mibBuilder.loadTexts:
    cipSecGlobalInAuthFails.setUnits("Failures")
_CipSecGlobalInDecrypts_Type = Counter32
_CipSecGlobalInDecrypts_Object = MibScalar
cipSecGlobalInDecrypts = _CipSecGlobalInDecrypts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 1, 14),
    _CipSecGlobalInDecrypts_Type()
)
cipSecGlobalInDecrypts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecGlobalInDecrypts.setStatus("current")
if mibBuilder.loadTexts:
    cipSecGlobalInDecrypts.setUnits("Packets")
_CipSecGlobalInDecryptFails_Type = Counter32
_CipSecGlobalInDecryptFails_Object = MibScalar
cipSecGlobalInDecryptFails = _CipSecGlobalInDecryptFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 1, 15),
    _CipSecGlobalInDecryptFails_Type()
)
cipSecGlobalInDecryptFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecGlobalInDecryptFails.setStatus("current")
if mibBuilder.loadTexts:
    cipSecGlobalInDecryptFails.setUnits("Packets")
_CipSecGlobalOutOctets_Type = Counter32
_CipSecGlobalOutOctets_Object = MibScalar
cipSecGlobalOutOctets = _CipSecGlobalOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 1, 16),
    _CipSecGlobalOutOctets_Type()
)
cipSecGlobalOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecGlobalOutOctets.setStatus("current")
if mibBuilder.loadTexts:
    cipSecGlobalOutOctets.setUnits("Octets")
_CipSecGlobalHcOutOctets_Type = Counter64
_CipSecGlobalHcOutOctets_Object = MibScalar
cipSecGlobalHcOutOctets = _CipSecGlobalHcOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 1, 17),
    _CipSecGlobalHcOutOctets_Type()
)
cipSecGlobalHcOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecGlobalHcOutOctets.setStatus("current")
_CipSecGlobalOutOctWraps_Type = Counter32
_CipSecGlobalOutOctWraps_Object = MibScalar
cipSecGlobalOutOctWraps = _CipSecGlobalOutOctWraps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 1, 18),
    _CipSecGlobalOutOctWraps_Type()
)
cipSecGlobalOutOctWraps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecGlobalOutOctWraps.setStatus("current")
if mibBuilder.loadTexts:
    cipSecGlobalOutOctWraps.setUnits("Integral units")
_CipSecGlobalOutUncompOctets_Type = Counter32
_CipSecGlobalOutUncompOctets_Object = MibScalar
cipSecGlobalOutUncompOctets = _CipSecGlobalOutUncompOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 1, 19),
    _CipSecGlobalOutUncompOctets_Type()
)
cipSecGlobalOutUncompOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecGlobalOutUncompOctets.setStatus("current")
if mibBuilder.loadTexts:
    cipSecGlobalOutUncompOctets.setUnits("Octets")
_CipSecGlobalHcOutUncompOctets_Type = Counter64
_CipSecGlobalHcOutUncompOctets_Object = MibScalar
cipSecGlobalHcOutUncompOctets = _CipSecGlobalHcOutUncompOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 1, 20),
    _CipSecGlobalHcOutUncompOctets_Type()
)
cipSecGlobalHcOutUncompOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecGlobalHcOutUncompOctets.setStatus("current")
if mibBuilder.loadTexts:
    cipSecGlobalHcOutUncompOctets.setUnits("Octets")
_CipSecGlobalOutUncompOctWraps_Type = Counter32
_CipSecGlobalOutUncompOctWraps_Object = MibScalar
cipSecGlobalOutUncompOctWraps = _CipSecGlobalOutUncompOctWraps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 1, 21),
    _CipSecGlobalOutUncompOctWraps_Type()
)
cipSecGlobalOutUncompOctWraps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecGlobalOutUncompOctWraps.setStatus("current")
if mibBuilder.loadTexts:
    cipSecGlobalOutUncompOctWraps.setUnits("Integral units")
_CipSecGlobalOutPkts_Type = Counter32
_CipSecGlobalOutPkts_Object = MibScalar
cipSecGlobalOutPkts = _CipSecGlobalOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 1, 22),
    _CipSecGlobalOutPkts_Type()
)
cipSecGlobalOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecGlobalOutPkts.setStatus("current")
if mibBuilder.loadTexts:
    cipSecGlobalOutPkts.setUnits("Packets")
_CipSecGlobalOutDrops_Type = Counter32
_CipSecGlobalOutDrops_Object = MibScalar
cipSecGlobalOutDrops = _CipSecGlobalOutDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 1, 23),
    _CipSecGlobalOutDrops_Type()
)
cipSecGlobalOutDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecGlobalOutDrops.setStatus("current")
if mibBuilder.loadTexts:
    cipSecGlobalOutDrops.setUnits("Packets")
_CipSecGlobalOutAuths_Type = Counter32
_CipSecGlobalOutAuths_Object = MibScalar
cipSecGlobalOutAuths = _CipSecGlobalOutAuths_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 1, 24),
    _CipSecGlobalOutAuths_Type()
)
cipSecGlobalOutAuths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecGlobalOutAuths.setStatus("current")
if mibBuilder.loadTexts:
    cipSecGlobalOutAuths.setUnits("Events")
_CipSecGlobalOutAuthFails_Type = Counter32
_CipSecGlobalOutAuthFails_Object = MibScalar
cipSecGlobalOutAuthFails = _CipSecGlobalOutAuthFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 1, 25),
    _CipSecGlobalOutAuthFails_Type()
)
cipSecGlobalOutAuthFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecGlobalOutAuthFails.setStatus("current")
if mibBuilder.loadTexts:
    cipSecGlobalOutAuthFails.setUnits("Failures")
_CipSecGlobalOutEncrypts_Type = Counter32
_CipSecGlobalOutEncrypts_Object = MibScalar
cipSecGlobalOutEncrypts = _CipSecGlobalOutEncrypts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 1, 26),
    _CipSecGlobalOutEncrypts_Type()
)
cipSecGlobalOutEncrypts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecGlobalOutEncrypts.setStatus("current")
if mibBuilder.loadTexts:
    cipSecGlobalOutEncrypts.setUnits("Packets")
_CipSecGlobalOutEncryptFails_Type = Counter32
_CipSecGlobalOutEncryptFails_Object = MibScalar
cipSecGlobalOutEncryptFails = _CipSecGlobalOutEncryptFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 1, 27),
    _CipSecGlobalOutEncryptFails_Type()
)
cipSecGlobalOutEncryptFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecGlobalOutEncryptFails.setStatus("current")
if mibBuilder.loadTexts:
    cipSecGlobalOutEncryptFails.setUnits("Failures")
_CipSecGlobalProtocolUseFails_Type = Counter32
_CipSecGlobalProtocolUseFails_Object = MibScalar
cipSecGlobalProtocolUseFails = _CipSecGlobalProtocolUseFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 1, 28),
    _CipSecGlobalProtocolUseFails_Type()
)
cipSecGlobalProtocolUseFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecGlobalProtocolUseFails.setStatus("current")
if mibBuilder.loadTexts:
    cipSecGlobalProtocolUseFails.setUnits("Failures")
_CipSecGlobalNoSaFails_Type = Counter32
_CipSecGlobalNoSaFails_Object = MibScalar
cipSecGlobalNoSaFails = _CipSecGlobalNoSaFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 1, 29),
    _CipSecGlobalNoSaFails_Type()
)
cipSecGlobalNoSaFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecGlobalNoSaFails.setStatus("current")
if mibBuilder.loadTexts:
    cipSecGlobalNoSaFails.setUnits("Failures")
_CipSecGlobalSysCapFails_Type = Counter32
_CipSecGlobalSysCapFails_Object = MibScalar
cipSecGlobalSysCapFails = _CipSecGlobalSysCapFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 1, 30),
    _CipSecGlobalSysCapFails_Type()
)
cipSecGlobalSysCapFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecGlobalSysCapFails.setStatus("current")
if mibBuilder.loadTexts:
    cipSecGlobalSysCapFails.setUnits("Failures")
_CipSecTunnelTable_Object = MibTable
cipSecTunnelTable = _CipSecTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 2)
)
if mibBuilder.loadTexts:
    cipSecTunnelTable.setStatus("current")
_CipSecTunnelEntry_Object = MibTableRow
cipSecTunnelEntry = _CipSecTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 2, 1)
)
cipSecTunnelEntry.setIndexNames(
    (0, "CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecTunIndex"),
)
if mibBuilder.loadTexts:
    cipSecTunnelEntry.setStatus("current")


class _CipSecTunIndex_Type(Integer32):
    """Custom type cipSecTunIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CipSecTunIndex_Type.__name__ = "Integer32"
_CipSecTunIndex_Object = MibTableColumn
cipSecTunIndex = _CipSecTunIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 2, 1, 1),
    _CipSecTunIndex_Type()
)
cipSecTunIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cipSecTunIndex.setStatus("current")


class _CipSecTunIkeTunnelIndex_Type(Integer32):
    """Custom type cipSecTunIkeTunnelIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CipSecTunIkeTunnelIndex_Type.__name__ = "Integer32"
_CipSecTunIkeTunnelIndex_Object = MibTableColumn
cipSecTunIkeTunnelIndex = _CipSecTunIkeTunnelIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 2, 1, 2),
    _CipSecTunIkeTunnelIndex_Type()
)
cipSecTunIkeTunnelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecTunIkeTunnelIndex.setStatus("current")
_CipSecTunIkeTunnelAlive_Type = TruthValue
_CipSecTunIkeTunnelAlive_Object = MibTableColumn
cipSecTunIkeTunnelAlive = _CipSecTunIkeTunnelAlive_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 2, 1, 3),
    _CipSecTunIkeTunnelAlive_Type()
)
cipSecTunIkeTunnelAlive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecTunIkeTunnelAlive.setStatus("current")
_CipSecTunLocalAddr_Type = IPSIpAddress
_CipSecTunLocalAddr_Object = MibTableColumn
cipSecTunLocalAddr = _CipSecTunLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 2, 1, 4),
    _CipSecTunLocalAddr_Type()
)
cipSecTunLocalAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecTunLocalAddr.setStatus("current")
_CipSecTunRemoteAddr_Type = IPSIpAddress
_CipSecTunRemoteAddr_Object = MibTableColumn
cipSecTunRemoteAddr = _CipSecTunRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 2, 1, 5),
    _CipSecTunRemoteAddr_Type()
)
cipSecTunRemoteAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecTunRemoteAddr.setStatus("current")
_CipSecTunKeyType_Type = KeyType
_CipSecTunKeyType_Object = MibTableColumn
cipSecTunKeyType = _CipSecTunKeyType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 2, 1, 6),
    _CipSecTunKeyType_Type()
)
cipSecTunKeyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecTunKeyType.setStatus("current")
_CipSecTunEncapMode_Type = EncapMode
_CipSecTunEncapMode_Object = MibTableColumn
cipSecTunEncapMode = _CipSecTunEncapMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 2, 1, 7),
    _CipSecTunEncapMode_Type()
)
cipSecTunEncapMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecTunEncapMode.setStatus("current")


class _CipSecTunLifeSize_Type(Integer32):
    """Custom type cipSecTunLifeSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CipSecTunLifeSize_Type.__name__ = "Integer32"
_CipSecTunLifeSize_Object = MibTableColumn
cipSecTunLifeSize = _CipSecTunLifeSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 2, 1, 8),
    _CipSecTunLifeSize_Type()
)
cipSecTunLifeSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecTunLifeSize.setStatus("current")
if mibBuilder.loadTexts:
    cipSecTunLifeSize.setUnits("KBytes")


class _CipSecTunLifeTime_Type(Integer32):
    """Custom type cipSecTunLifeTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CipSecTunLifeTime_Type.__name__ = "Integer32"
_CipSecTunLifeTime_Object = MibTableColumn
cipSecTunLifeTime = _CipSecTunLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 2, 1, 9),
    _CipSecTunLifeTime_Type()
)
cipSecTunLifeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecTunLifeTime.setStatus("current")
if mibBuilder.loadTexts:
    cipSecTunLifeTime.setUnits("Seconds")
_CipSecTunActiveTime_Type = TimeInterval
_CipSecTunActiveTime_Object = MibTableColumn
cipSecTunActiveTime = _CipSecTunActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 2, 1, 10),
    _CipSecTunActiveTime_Type()
)
cipSecTunActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecTunActiveTime.setStatus("current")


class _CipSecTunSaLifeSizeThreshold_Type(Integer32):
    """Custom type cipSecTunSaLifeSizeThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CipSecTunSaLifeSizeThreshold_Type.__name__ = "Integer32"
_CipSecTunSaLifeSizeThreshold_Object = MibTableColumn
cipSecTunSaLifeSizeThreshold = _CipSecTunSaLifeSizeThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 2, 1, 11),
    _CipSecTunSaLifeSizeThreshold_Type()
)
cipSecTunSaLifeSizeThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecTunSaLifeSizeThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cipSecTunSaLifeSizeThreshold.setUnits("KBytes")


class _CipSecTunSaLifeTimeThreshold_Type(Integer32):
    """Custom type cipSecTunSaLifeTimeThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CipSecTunSaLifeTimeThreshold_Type.__name__ = "Integer32"
_CipSecTunSaLifeTimeThreshold_Object = MibTableColumn
cipSecTunSaLifeTimeThreshold = _CipSecTunSaLifeTimeThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 2, 1, 12),
    _CipSecTunSaLifeTimeThreshold_Type()
)
cipSecTunSaLifeTimeThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecTunSaLifeTimeThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cipSecTunSaLifeTimeThreshold.setUnits("Seconds")
_CipSecTunTotalRefreshes_Type = Counter32
_CipSecTunTotalRefreshes_Object = MibTableColumn
cipSecTunTotalRefreshes = _CipSecTunTotalRefreshes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 2, 1, 13),
    _CipSecTunTotalRefreshes_Type()
)
cipSecTunTotalRefreshes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecTunTotalRefreshes.setStatus("current")
if mibBuilder.loadTexts:
    cipSecTunTotalRefreshes.setUnits("QM Exchanges")
_CipSecTunExpiredSaInstances_Type = Counter32
_CipSecTunExpiredSaInstances_Object = MibTableColumn
cipSecTunExpiredSaInstances = _CipSecTunExpiredSaInstances_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 2, 1, 14),
    _CipSecTunExpiredSaInstances_Type()
)
cipSecTunExpiredSaInstances.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecTunExpiredSaInstances.setStatus("current")
if mibBuilder.loadTexts:
    cipSecTunExpiredSaInstances.setUnits("SAs")
_CipSecTunCurrentSaInstances_Type = Gauge32
_CipSecTunCurrentSaInstances_Object = MibTableColumn
cipSecTunCurrentSaInstances = _CipSecTunCurrentSaInstances_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 2, 1, 15),
    _CipSecTunCurrentSaInstances_Type()
)
cipSecTunCurrentSaInstances.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecTunCurrentSaInstances.setStatus("current")
_CipSecTunInSaDiffHellmanGrp_Type = DiffHellmanGrp
_CipSecTunInSaDiffHellmanGrp_Object = MibTableColumn
cipSecTunInSaDiffHellmanGrp = _CipSecTunInSaDiffHellmanGrp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 2, 1, 16),
    _CipSecTunInSaDiffHellmanGrp_Type()
)
cipSecTunInSaDiffHellmanGrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecTunInSaDiffHellmanGrp.setStatus("current")
_CipSecTunInSaEncryptAlgo_Type = EncryptAlgo
_CipSecTunInSaEncryptAlgo_Object = MibTableColumn
cipSecTunInSaEncryptAlgo = _CipSecTunInSaEncryptAlgo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 2, 1, 17),
    _CipSecTunInSaEncryptAlgo_Type()
)
cipSecTunInSaEncryptAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecTunInSaEncryptAlgo.setStatus("current")
_CipSecTunInSaAhAuthAlgo_Type = AuthAlgo
_CipSecTunInSaAhAuthAlgo_Object = MibTableColumn
cipSecTunInSaAhAuthAlgo = _CipSecTunInSaAhAuthAlgo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 2, 1, 18),
    _CipSecTunInSaAhAuthAlgo_Type()
)
cipSecTunInSaAhAuthAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecTunInSaAhAuthAlgo.setStatus("current")
_CipSecTunInSaEspAuthAlgo_Type = AuthAlgo
_CipSecTunInSaEspAuthAlgo_Object = MibTableColumn
cipSecTunInSaEspAuthAlgo = _CipSecTunInSaEspAuthAlgo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 2, 1, 19),
    _CipSecTunInSaEspAuthAlgo_Type()
)
cipSecTunInSaEspAuthAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecTunInSaEspAuthAlgo.setStatus("current")
_CipSecTunInSaDecompAlgo_Type = CompAlgo
_CipSecTunInSaDecompAlgo_Object = MibTableColumn
cipSecTunInSaDecompAlgo = _CipSecTunInSaDecompAlgo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 2, 1, 20),
    _CipSecTunInSaDecompAlgo_Type()
)
cipSecTunInSaDecompAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecTunInSaDecompAlgo.setStatus("current")
_CipSecTunOutSaDiffHellmanGrp_Type = DiffHellmanGrp
_CipSecTunOutSaDiffHellmanGrp_Object = MibTableColumn
cipSecTunOutSaDiffHellmanGrp = _CipSecTunOutSaDiffHellmanGrp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 2, 1, 21),
    _CipSecTunOutSaDiffHellmanGrp_Type()
)
cipSecTunOutSaDiffHellmanGrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecTunOutSaDiffHellmanGrp.setStatus("current")
_CipSecTunOutSaEncryptAlgo_Type = EncryptAlgo
_CipSecTunOutSaEncryptAlgo_Object = MibTableColumn
cipSecTunOutSaEncryptAlgo = _CipSecTunOutSaEncryptAlgo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 2, 1, 22),
    _CipSecTunOutSaEncryptAlgo_Type()
)
cipSecTunOutSaEncryptAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecTunOutSaEncryptAlgo.setStatus("current")
_CipSecTunOutSaAhAuthAlgo_Type = AuthAlgo
_CipSecTunOutSaAhAuthAlgo_Object = MibTableColumn
cipSecTunOutSaAhAuthAlgo = _CipSecTunOutSaAhAuthAlgo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 2, 1, 23),
    _CipSecTunOutSaAhAuthAlgo_Type()
)
cipSecTunOutSaAhAuthAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecTunOutSaAhAuthAlgo.setStatus("current")
_CipSecTunOutSaEspAuthAlgo_Type = AuthAlgo
_CipSecTunOutSaEspAuthAlgo_Object = MibTableColumn
cipSecTunOutSaEspAuthAlgo = _CipSecTunOutSaEspAuthAlgo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 2, 1, 24),
    _CipSecTunOutSaEspAuthAlgo_Type()
)
cipSecTunOutSaEspAuthAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecTunOutSaEspAuthAlgo.setStatus("current")
_CipSecTunOutSaCompAlgo_Type = CompAlgo
_CipSecTunOutSaCompAlgo_Object = MibTableColumn
cipSecTunOutSaCompAlgo = _CipSecTunOutSaCompAlgo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 2, 1, 25),
    _CipSecTunOutSaCompAlgo_Type()
)
cipSecTunOutSaCompAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecTunOutSaCompAlgo.setStatus("current")
_CipSecTunInOctets_Type = Counter32
_CipSecTunInOctets_Object = MibTableColumn
cipSecTunInOctets = _CipSecTunInOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 2, 1, 26),
    _CipSecTunInOctets_Type()
)
cipSecTunInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecTunInOctets.setStatus("current")
if mibBuilder.loadTexts:
    cipSecTunInOctets.setUnits("Octets")
_CipSecTunHcInOctets_Type = Counter64
_CipSecTunHcInOctets_Object = MibTableColumn
cipSecTunHcInOctets = _CipSecTunHcInOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 2, 1, 27),
    _CipSecTunHcInOctets_Type()
)
cipSecTunHcInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecTunHcInOctets.setStatus("current")
if mibBuilder.loadTexts:
    cipSecTunHcInOctets.setUnits("Octets")
_CipSecTunInOctWraps_Type = Counter32
_CipSecTunInOctWraps_Object = MibTableColumn
cipSecTunInOctWraps = _CipSecTunInOctWraps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 2, 1, 28),
    _CipSecTunInOctWraps_Type()
)
cipSecTunInOctWraps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecTunInOctWraps.setStatus("current")
if mibBuilder.loadTexts:
    cipSecTunInOctWraps.setUnits("Integral units")
_CipSecTunInDecompOctets_Type = Counter32
_CipSecTunInDecompOctets_Object = MibTableColumn
cipSecTunInDecompOctets = _CipSecTunInDecompOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 2, 1, 29),
    _CipSecTunInDecompOctets_Type()
)
cipSecTunInDecompOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecTunInDecompOctets.setStatus("current")
if mibBuilder.loadTexts:
    cipSecTunInDecompOctets.setUnits("Octets")
_CipSecTunHcInDecompOctets_Type = Counter64
_CipSecTunHcInDecompOctets_Object = MibTableColumn
cipSecTunHcInDecompOctets = _CipSecTunHcInDecompOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 2, 1, 30),
    _CipSecTunHcInDecompOctets_Type()
)
cipSecTunHcInDecompOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecTunHcInDecompOctets.setStatus("current")
_CipSecTunInDecompOctWraps_Type = Counter32
_CipSecTunInDecompOctWraps_Object = MibTableColumn
cipSecTunInDecompOctWraps = _CipSecTunInDecompOctWraps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 2, 1, 31),
    _CipSecTunInDecompOctWraps_Type()
)
cipSecTunInDecompOctWraps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecTunInDecompOctWraps.setStatus("current")
if mibBuilder.loadTexts:
    cipSecTunInDecompOctWraps.setUnits("Integral units")
_CipSecTunInPkts_Type = Counter32
_CipSecTunInPkts_Object = MibTableColumn
cipSecTunInPkts = _CipSecTunInPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 2, 1, 32),
    _CipSecTunInPkts_Type()
)
cipSecTunInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecTunInPkts.setStatus("current")
if mibBuilder.loadTexts:
    cipSecTunInPkts.setUnits("Packets")
_CipSecTunInDropPkts_Type = Counter32
_CipSecTunInDropPkts_Object = MibTableColumn
cipSecTunInDropPkts = _CipSecTunInDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 2, 1, 33),
    _CipSecTunInDropPkts_Type()
)
cipSecTunInDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecTunInDropPkts.setStatus("current")
if mibBuilder.loadTexts:
    cipSecTunInDropPkts.setUnits("Packets")
_CipSecTunInReplayDropPkts_Type = Counter32
_CipSecTunInReplayDropPkts_Object = MibTableColumn
cipSecTunInReplayDropPkts = _CipSecTunInReplayDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 2, 1, 34),
    _CipSecTunInReplayDropPkts_Type()
)
cipSecTunInReplayDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecTunInReplayDropPkts.setStatus("current")
if mibBuilder.loadTexts:
    cipSecTunInReplayDropPkts.setUnits("Packets")
_CipSecTunInAuths_Type = Counter32
_CipSecTunInAuths_Object = MibTableColumn
cipSecTunInAuths = _CipSecTunInAuths_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 2, 1, 35),
    _CipSecTunInAuths_Type()
)
cipSecTunInAuths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecTunInAuths.setStatus("current")
if mibBuilder.loadTexts:
    cipSecTunInAuths.setUnits("Events")
_CipSecTunInAuthFails_Type = Counter32
_CipSecTunInAuthFails_Object = MibTableColumn
cipSecTunInAuthFails = _CipSecTunInAuthFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 2, 1, 36),
    _CipSecTunInAuthFails_Type()
)
cipSecTunInAuthFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecTunInAuthFails.setStatus("current")
if mibBuilder.loadTexts:
    cipSecTunInAuthFails.setUnits("Failures")
_CipSecTunInDecrypts_Type = Counter32
_CipSecTunInDecrypts_Object = MibTableColumn
cipSecTunInDecrypts = _CipSecTunInDecrypts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 2, 1, 37),
    _CipSecTunInDecrypts_Type()
)
cipSecTunInDecrypts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecTunInDecrypts.setStatus("current")
if mibBuilder.loadTexts:
    cipSecTunInDecrypts.setUnits("Packets")
_CipSecTunInDecryptFails_Type = Counter32
_CipSecTunInDecryptFails_Object = MibTableColumn
cipSecTunInDecryptFails = _CipSecTunInDecryptFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 2, 1, 38),
    _CipSecTunInDecryptFails_Type()
)
cipSecTunInDecryptFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecTunInDecryptFails.setStatus("current")
if mibBuilder.loadTexts:
    cipSecTunInDecryptFails.setUnits("Failures")
_CipSecTunOutOctets_Type = Counter32
_CipSecTunOutOctets_Object = MibTableColumn
cipSecTunOutOctets = _CipSecTunOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 2, 1, 39),
    _CipSecTunOutOctets_Type()
)
cipSecTunOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecTunOutOctets.setStatus("current")
if mibBuilder.loadTexts:
    cipSecTunOutOctets.setUnits("Octets")
_CipSecTunHcOutOctets_Type = Counter64
_CipSecTunHcOutOctets_Object = MibTableColumn
cipSecTunHcOutOctets = _CipSecTunHcOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 2, 1, 40),
    _CipSecTunHcOutOctets_Type()
)
cipSecTunHcOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecTunHcOutOctets.setStatus("current")
_CipSecTunOutOctWraps_Type = Counter32
_CipSecTunOutOctWraps_Object = MibTableColumn
cipSecTunOutOctWraps = _CipSecTunOutOctWraps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 2, 1, 41),
    _CipSecTunOutOctWraps_Type()
)
cipSecTunOutOctWraps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecTunOutOctWraps.setStatus("current")
if mibBuilder.loadTexts:
    cipSecTunOutOctWraps.setUnits("Integral units")
_CipSecTunOutUncompOctets_Type = Counter32
_CipSecTunOutUncompOctets_Object = MibTableColumn
cipSecTunOutUncompOctets = _CipSecTunOutUncompOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 2, 1, 42),
    _CipSecTunOutUncompOctets_Type()
)
cipSecTunOutUncompOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecTunOutUncompOctets.setStatus("current")
if mibBuilder.loadTexts:
    cipSecTunOutUncompOctets.setUnits("Octets")
_CipSecTunHcOutUncompOctets_Type = Counter64
_CipSecTunHcOutUncompOctets_Object = MibTableColumn
cipSecTunHcOutUncompOctets = _CipSecTunHcOutUncompOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 2, 1, 43),
    _CipSecTunHcOutUncompOctets_Type()
)
cipSecTunHcOutUncompOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecTunHcOutUncompOctets.setStatus("current")
_CipSecTunOutUncompOctWraps_Type = Counter32
_CipSecTunOutUncompOctWraps_Object = MibTableColumn
cipSecTunOutUncompOctWraps = _CipSecTunOutUncompOctWraps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 2, 1, 44),
    _CipSecTunOutUncompOctWraps_Type()
)
cipSecTunOutUncompOctWraps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecTunOutUncompOctWraps.setStatus("current")
if mibBuilder.loadTexts:
    cipSecTunOutUncompOctWraps.setUnits("Integral units")
_CipSecTunOutPkts_Type = Counter32
_CipSecTunOutPkts_Object = MibTableColumn
cipSecTunOutPkts = _CipSecTunOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 2, 1, 45),
    _CipSecTunOutPkts_Type()
)
cipSecTunOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecTunOutPkts.setStatus("current")
if mibBuilder.loadTexts:
    cipSecTunOutPkts.setUnits("Packets")
_CipSecTunOutDropPkts_Type = Counter32
_CipSecTunOutDropPkts_Object = MibTableColumn
cipSecTunOutDropPkts = _CipSecTunOutDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 2, 1, 46),
    _CipSecTunOutDropPkts_Type()
)
cipSecTunOutDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecTunOutDropPkts.setStatus("current")
if mibBuilder.loadTexts:
    cipSecTunOutDropPkts.setUnits("Packets")
_CipSecTunOutAuths_Type = Counter32
_CipSecTunOutAuths_Object = MibTableColumn
cipSecTunOutAuths = _CipSecTunOutAuths_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 2, 1, 47),
    _CipSecTunOutAuths_Type()
)
cipSecTunOutAuths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecTunOutAuths.setStatus("current")
if mibBuilder.loadTexts:
    cipSecTunOutAuths.setUnits("Events")
_CipSecTunOutAuthFails_Type = Counter32
_CipSecTunOutAuthFails_Object = MibTableColumn
cipSecTunOutAuthFails = _CipSecTunOutAuthFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 2, 1, 48),
    _CipSecTunOutAuthFails_Type()
)
cipSecTunOutAuthFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecTunOutAuthFails.setStatus("current")
if mibBuilder.loadTexts:
    cipSecTunOutAuthFails.setUnits("Failures")
_CipSecTunOutEncrypts_Type = Counter32
_CipSecTunOutEncrypts_Object = MibTableColumn
cipSecTunOutEncrypts = _CipSecTunOutEncrypts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 2, 1, 49),
    _CipSecTunOutEncrypts_Type()
)
cipSecTunOutEncrypts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecTunOutEncrypts.setStatus("current")
if mibBuilder.loadTexts:
    cipSecTunOutEncrypts.setUnits("Packets")
_CipSecTunOutEncryptFails_Type = Counter32
_CipSecTunOutEncryptFails_Object = MibTableColumn
cipSecTunOutEncryptFails = _CipSecTunOutEncryptFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 2, 1, 50),
    _CipSecTunOutEncryptFails_Type()
)
cipSecTunOutEncryptFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecTunOutEncryptFails.setStatus("current")
if mibBuilder.loadTexts:
    cipSecTunOutEncryptFails.setUnits("Failures")
_CipSecTunStatus_Type = TunnelStatus
_CipSecTunStatus_Object = MibTableColumn
cipSecTunStatus = _CipSecTunStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 2, 1, 51),
    _CipSecTunStatus_Type()
)
cipSecTunStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cipSecTunStatus.setStatus("current")
_CipSecEndPtTable_Object = MibTable
cipSecEndPtTable = _CipSecEndPtTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 3)
)
if mibBuilder.loadTexts:
    cipSecEndPtTable.setStatus("current")
_CipSecEndPtEntry_Object = MibTableRow
cipSecEndPtEntry = _CipSecEndPtEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 3, 1)
)
cipSecEndPtEntry.setIndexNames(
    (0, "CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecTunIndex"),
    (0, "CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecEndPtIndex"),
)
if mibBuilder.loadTexts:
    cipSecEndPtEntry.setStatus("current")


class _CipSecEndPtIndex_Type(Integer32):
    """Custom type cipSecEndPtIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CipSecEndPtIndex_Type.__name__ = "Integer32"
_CipSecEndPtIndex_Object = MibTableColumn
cipSecEndPtIndex = _CipSecEndPtIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 3, 1, 1),
    _CipSecEndPtIndex_Type()
)
cipSecEndPtIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cipSecEndPtIndex.setStatus("current")
_CipSecEndPtLocalName_Type = DisplayString
_CipSecEndPtLocalName_Object = MibTableColumn
cipSecEndPtLocalName = _CipSecEndPtLocalName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 3, 1, 2),
    _CipSecEndPtLocalName_Type()
)
cipSecEndPtLocalName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecEndPtLocalName.setStatus("current")
_CipSecEndPtLocalType_Type = EndPtType
_CipSecEndPtLocalType_Object = MibTableColumn
cipSecEndPtLocalType = _CipSecEndPtLocalType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 3, 1, 3),
    _CipSecEndPtLocalType_Type()
)
cipSecEndPtLocalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecEndPtLocalType.setStatus("current")
_CipSecEndPtLocalAddr1_Type = IPSIpAddress
_CipSecEndPtLocalAddr1_Object = MibTableColumn
cipSecEndPtLocalAddr1 = _CipSecEndPtLocalAddr1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 3, 1, 4),
    _CipSecEndPtLocalAddr1_Type()
)
cipSecEndPtLocalAddr1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecEndPtLocalAddr1.setStatus("current")
_CipSecEndPtLocalAddr2_Type = IPSIpAddress
_CipSecEndPtLocalAddr2_Object = MibTableColumn
cipSecEndPtLocalAddr2 = _CipSecEndPtLocalAddr2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 3, 1, 5),
    _CipSecEndPtLocalAddr2_Type()
)
cipSecEndPtLocalAddr2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecEndPtLocalAddr2.setStatus("current")


class _CipSecEndPtLocalProtocol_Type(Integer32):
    """Custom type cipSecEndPtLocalProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CipSecEndPtLocalProtocol_Type.__name__ = "Integer32"
_CipSecEndPtLocalProtocol_Object = MibTableColumn
cipSecEndPtLocalProtocol = _CipSecEndPtLocalProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 3, 1, 6),
    _CipSecEndPtLocalProtocol_Type()
)
cipSecEndPtLocalProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecEndPtLocalProtocol.setStatus("current")


class _CipSecEndPtLocalPort_Type(Integer32):
    """Custom type cipSecEndPtLocalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CipSecEndPtLocalPort_Type.__name__ = "Integer32"
_CipSecEndPtLocalPort_Object = MibTableColumn
cipSecEndPtLocalPort = _CipSecEndPtLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 3, 1, 7),
    _CipSecEndPtLocalPort_Type()
)
cipSecEndPtLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecEndPtLocalPort.setStatus("current")
_CipSecEndPtRemoteName_Type = DisplayString
_CipSecEndPtRemoteName_Object = MibTableColumn
cipSecEndPtRemoteName = _CipSecEndPtRemoteName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 3, 1, 8),
    _CipSecEndPtRemoteName_Type()
)
cipSecEndPtRemoteName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecEndPtRemoteName.setStatus("current")
_CipSecEndPtRemoteType_Type = EndPtType
_CipSecEndPtRemoteType_Object = MibTableColumn
cipSecEndPtRemoteType = _CipSecEndPtRemoteType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 3, 1, 9),
    _CipSecEndPtRemoteType_Type()
)
cipSecEndPtRemoteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecEndPtRemoteType.setStatus("current")
_CipSecEndPtRemoteAddr1_Type = IPSIpAddress
_CipSecEndPtRemoteAddr1_Object = MibTableColumn
cipSecEndPtRemoteAddr1 = _CipSecEndPtRemoteAddr1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 3, 1, 10),
    _CipSecEndPtRemoteAddr1_Type()
)
cipSecEndPtRemoteAddr1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecEndPtRemoteAddr1.setStatus("current")
_CipSecEndPtRemoteAddr2_Type = IPSIpAddress
_CipSecEndPtRemoteAddr2_Object = MibTableColumn
cipSecEndPtRemoteAddr2 = _CipSecEndPtRemoteAddr2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 3, 1, 11),
    _CipSecEndPtRemoteAddr2_Type()
)
cipSecEndPtRemoteAddr2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecEndPtRemoteAddr2.setStatus("current")


class _CipSecEndPtRemoteProtocol_Type(Integer32):
    """Custom type cipSecEndPtRemoteProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CipSecEndPtRemoteProtocol_Type.__name__ = "Integer32"
_CipSecEndPtRemoteProtocol_Object = MibTableColumn
cipSecEndPtRemoteProtocol = _CipSecEndPtRemoteProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 3, 1, 12),
    _CipSecEndPtRemoteProtocol_Type()
)
cipSecEndPtRemoteProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecEndPtRemoteProtocol.setStatus("current")


class _CipSecEndPtRemotePort_Type(Integer32):
    """Custom type cipSecEndPtRemotePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CipSecEndPtRemotePort_Type.__name__ = "Integer32"
_CipSecEndPtRemotePort_Object = MibTableColumn
cipSecEndPtRemotePort = _CipSecEndPtRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 3, 1, 13),
    _CipSecEndPtRemotePort_Type()
)
cipSecEndPtRemotePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecEndPtRemotePort.setStatus("current")
_CipSecSpiTable_Object = MibTable
cipSecSpiTable = _CipSecSpiTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 4)
)
if mibBuilder.loadTexts:
    cipSecSpiTable.setStatus("current")
_CipSecSpiEntry_Object = MibTableRow
cipSecSpiEntry = _CipSecSpiEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 4, 1)
)
cipSecSpiEntry.setIndexNames(
    (0, "CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecTunIndex"),
    (0, "CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecSpiIndex"),
)
if mibBuilder.loadTexts:
    cipSecSpiEntry.setStatus("current")


class _CipSecSpiIndex_Type(Integer32):
    """Custom type cipSecSpiIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CipSecSpiIndex_Type.__name__ = "Integer32"
_CipSecSpiIndex_Object = MibTableColumn
cipSecSpiIndex = _CipSecSpiIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 4, 1, 1),
    _CipSecSpiIndex_Type()
)
cipSecSpiIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cipSecSpiIndex.setStatus("current")


class _CipSecSpiDirection_Type(Integer32):
    """Custom type cipSecSpiDirection based on Integer32"""
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


_CipSecSpiDirection_Type.__name__ = "Integer32"
_CipSecSpiDirection_Object = MibTableColumn
cipSecSpiDirection = _CipSecSpiDirection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 4, 1, 2),
    _CipSecSpiDirection_Type()
)
cipSecSpiDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecSpiDirection.setStatus("current")


class _CipSecSpiValue_Type(Unsigned32):
    """Custom type cipSecSpiValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CipSecSpiValue_Type.__name__ = "Unsigned32"
_CipSecSpiValue_Object = MibTableColumn
cipSecSpiValue = _CipSecSpiValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 4, 1, 3),
    _CipSecSpiValue_Type()
)
cipSecSpiValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecSpiValue.setStatus("current")


class _CipSecSpiProtocol_Type(Integer32):
    """Custom type cipSecSpiProtocol based on Integer32"""
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


_CipSecSpiProtocol_Type.__name__ = "Integer32"
_CipSecSpiProtocol_Object = MibTableColumn
cipSecSpiProtocol = _CipSecSpiProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 4, 1, 4),
    _CipSecSpiProtocol_Type()
)
cipSecSpiProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecSpiProtocol.setStatus("current")


class _CipSecSpiStatus_Type(Integer32):
    """Custom type cipSecSpiStatus based on Integer32"""
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


_CipSecSpiStatus_Type.__name__ = "Integer32"
_CipSecSpiStatus_Object = MibTableColumn
cipSecSpiStatus = _CipSecSpiStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 4, 1, 5),
    _CipSecSpiStatus_Type()
)
cipSecSpiStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecSpiStatus.setStatus("current")
_CipSecPhase2GWStatsTable_Object = MibTable
cipSecPhase2GWStatsTable = _CipSecPhase2GWStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 5)
)
if mibBuilder.loadTexts:
    cipSecPhase2GWStatsTable.setStatus("current")
_CipSecPhase2GWStatsEntry_Object = MibTableRow
cipSecPhase2GWStatsEntry = _CipSecPhase2GWStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 5, 1)
)
cipSecPhase2GWStatsEntry.setIndexNames(
    (0, "CISCO-MEDIA-GATEWAY-MIB", "cmgwIndex"),
)
if mibBuilder.loadTexts:
    cipSecPhase2GWStatsEntry.setStatus("current")
_CipSecPhase2GWActiveTunnels_Type = Gauge32
_CipSecPhase2GWActiveTunnels_Object = MibTableColumn
cipSecPhase2GWActiveTunnels = _CipSecPhase2GWActiveTunnels_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 5, 1, 1),
    _CipSecPhase2GWActiveTunnels_Type()
)
cipSecPhase2GWActiveTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecPhase2GWActiveTunnels.setStatus("current")
_CipSecPhase2GWPreviousTunnels_Type = Counter32
_CipSecPhase2GWPreviousTunnels_Object = MibTableColumn
cipSecPhase2GWPreviousTunnels = _CipSecPhase2GWPreviousTunnels_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 5, 1, 2),
    _CipSecPhase2GWPreviousTunnels_Type()
)
cipSecPhase2GWPreviousTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecPhase2GWPreviousTunnels.setStatus("current")
if mibBuilder.loadTexts:
    cipSecPhase2GWPreviousTunnels.setUnits("Phase-2 Tunnels")
_CipSecPhase2GWInOctets_Type = Counter32
_CipSecPhase2GWInOctets_Object = MibTableColumn
cipSecPhase2GWInOctets = _CipSecPhase2GWInOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 5, 1, 3),
    _CipSecPhase2GWInOctets_Type()
)
cipSecPhase2GWInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecPhase2GWInOctets.setStatus("current")
if mibBuilder.loadTexts:
    cipSecPhase2GWInOctets.setUnits("Octets")
_CipSecPhase2GWInOctWraps_Type = Counter32
_CipSecPhase2GWInOctWraps_Object = MibTableColumn
cipSecPhase2GWInOctWraps = _CipSecPhase2GWInOctWraps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 5, 1, 4),
    _CipSecPhase2GWInOctWraps_Type()
)
cipSecPhase2GWInOctWraps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecPhase2GWInOctWraps.setStatus("current")
if mibBuilder.loadTexts:
    cipSecPhase2GWInOctWraps.setUnits("Integral units")
_CipSecPhase2GWInDecompOctets_Type = Counter32
_CipSecPhase2GWInDecompOctets_Object = MibTableColumn
cipSecPhase2GWInDecompOctets = _CipSecPhase2GWInDecompOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 5, 1, 5),
    _CipSecPhase2GWInDecompOctets_Type()
)
cipSecPhase2GWInDecompOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecPhase2GWInDecompOctets.setStatus("current")
if mibBuilder.loadTexts:
    cipSecPhase2GWInDecompOctets.setUnits("Octets")
_CipSecPhase2GWInDecompOctWraps_Type = Counter32
_CipSecPhase2GWInDecompOctWraps_Object = MibTableColumn
cipSecPhase2GWInDecompOctWraps = _CipSecPhase2GWInDecompOctWraps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 5, 1, 6),
    _CipSecPhase2GWInDecompOctWraps_Type()
)
cipSecPhase2GWInDecompOctWraps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecPhase2GWInDecompOctWraps.setStatus("current")
if mibBuilder.loadTexts:
    cipSecPhase2GWInDecompOctWraps.setUnits("Integral units")
_CipSecPhase2GWInPkts_Type = Counter32
_CipSecPhase2GWInPkts_Object = MibTableColumn
cipSecPhase2GWInPkts = _CipSecPhase2GWInPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 5, 1, 7),
    _CipSecPhase2GWInPkts_Type()
)
cipSecPhase2GWInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecPhase2GWInPkts.setStatus("current")
if mibBuilder.loadTexts:
    cipSecPhase2GWInPkts.setUnits("Packets")
_CipSecPhase2GWInDrops_Type = Counter32
_CipSecPhase2GWInDrops_Object = MibTableColumn
cipSecPhase2GWInDrops = _CipSecPhase2GWInDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 5, 1, 8),
    _CipSecPhase2GWInDrops_Type()
)
cipSecPhase2GWInDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecPhase2GWInDrops.setStatus("current")
if mibBuilder.loadTexts:
    cipSecPhase2GWInDrops.setUnits("Packets")
_CipSecPhase2GWInReplayDrops_Type = Counter32
_CipSecPhase2GWInReplayDrops_Object = MibTableColumn
cipSecPhase2GWInReplayDrops = _CipSecPhase2GWInReplayDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 5, 1, 9),
    _CipSecPhase2GWInReplayDrops_Type()
)
cipSecPhase2GWInReplayDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecPhase2GWInReplayDrops.setStatus("current")
if mibBuilder.loadTexts:
    cipSecPhase2GWInReplayDrops.setUnits("Packets")
_CipSecPhase2GWInAuths_Type = Counter32
_CipSecPhase2GWInAuths_Object = MibTableColumn
cipSecPhase2GWInAuths = _CipSecPhase2GWInAuths_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 5, 1, 10),
    _CipSecPhase2GWInAuths_Type()
)
cipSecPhase2GWInAuths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecPhase2GWInAuths.setStatus("current")
if mibBuilder.loadTexts:
    cipSecPhase2GWInAuths.setUnits("Events")
_CipSecPhase2GWInAuthFails_Type = Counter32
_CipSecPhase2GWInAuthFails_Object = MibTableColumn
cipSecPhase2GWInAuthFails = _CipSecPhase2GWInAuthFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 5, 1, 11),
    _CipSecPhase2GWInAuthFails_Type()
)
cipSecPhase2GWInAuthFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecPhase2GWInAuthFails.setStatus("current")
if mibBuilder.loadTexts:
    cipSecPhase2GWInAuthFails.setUnits("Failures")
_CipSecPhase2GWInDecrypts_Type = Counter32
_CipSecPhase2GWInDecrypts_Object = MibTableColumn
cipSecPhase2GWInDecrypts = _CipSecPhase2GWInDecrypts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 5, 1, 12),
    _CipSecPhase2GWInDecrypts_Type()
)
cipSecPhase2GWInDecrypts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecPhase2GWInDecrypts.setStatus("current")
if mibBuilder.loadTexts:
    cipSecPhase2GWInDecrypts.setUnits("Packets")
_CipSecPhase2GWInDecryptFails_Type = Counter32
_CipSecPhase2GWInDecryptFails_Object = MibTableColumn
cipSecPhase2GWInDecryptFails = _CipSecPhase2GWInDecryptFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 5, 1, 13),
    _CipSecPhase2GWInDecryptFails_Type()
)
cipSecPhase2GWInDecryptFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecPhase2GWInDecryptFails.setStatus("current")
if mibBuilder.loadTexts:
    cipSecPhase2GWInDecryptFails.setUnits("Packets")
_CipSecPhase2GWOutOctets_Type = Counter32
_CipSecPhase2GWOutOctets_Object = MibTableColumn
cipSecPhase2GWOutOctets = _CipSecPhase2GWOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 5, 1, 14),
    _CipSecPhase2GWOutOctets_Type()
)
cipSecPhase2GWOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecPhase2GWOutOctets.setStatus("current")
if mibBuilder.loadTexts:
    cipSecPhase2GWOutOctets.setUnits("Octets")
_CipSecPhase2GWOutOctWraps_Type = Counter32
_CipSecPhase2GWOutOctWraps_Object = MibTableColumn
cipSecPhase2GWOutOctWraps = _CipSecPhase2GWOutOctWraps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 5, 1, 15),
    _CipSecPhase2GWOutOctWraps_Type()
)
cipSecPhase2GWOutOctWraps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecPhase2GWOutOctWraps.setStatus("current")
if mibBuilder.loadTexts:
    cipSecPhase2GWOutOctWraps.setUnits("Integral units")
_CipSecPhase2GWOutUncompOctets_Type = Counter32
_CipSecPhase2GWOutUncompOctets_Object = MibTableColumn
cipSecPhase2GWOutUncompOctets = _CipSecPhase2GWOutUncompOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 5, 1, 16),
    _CipSecPhase2GWOutUncompOctets_Type()
)
cipSecPhase2GWOutUncompOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecPhase2GWOutUncompOctets.setStatus("current")
if mibBuilder.loadTexts:
    cipSecPhase2GWOutUncompOctets.setUnits("Octets")
_CipSecPhase2GWOutUncompOctWraps_Type = Counter32
_CipSecPhase2GWOutUncompOctWraps_Object = MibTableColumn
cipSecPhase2GWOutUncompOctWraps = _CipSecPhase2GWOutUncompOctWraps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 5, 1, 17),
    _CipSecPhase2GWOutUncompOctWraps_Type()
)
cipSecPhase2GWOutUncompOctWraps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecPhase2GWOutUncompOctWraps.setStatus("current")
if mibBuilder.loadTexts:
    cipSecPhase2GWOutUncompOctWraps.setUnits("Integral units")
_CipSecPhase2GWOutPkts_Type = Counter32
_CipSecPhase2GWOutPkts_Object = MibTableColumn
cipSecPhase2GWOutPkts = _CipSecPhase2GWOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 5, 1, 18),
    _CipSecPhase2GWOutPkts_Type()
)
cipSecPhase2GWOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecPhase2GWOutPkts.setStatus("current")
if mibBuilder.loadTexts:
    cipSecPhase2GWOutPkts.setUnits("Packets")
_CipSecPhase2GWOutDrops_Type = Counter32
_CipSecPhase2GWOutDrops_Object = MibTableColumn
cipSecPhase2GWOutDrops = _CipSecPhase2GWOutDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 5, 1, 19),
    _CipSecPhase2GWOutDrops_Type()
)
cipSecPhase2GWOutDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecPhase2GWOutDrops.setStatus("current")
if mibBuilder.loadTexts:
    cipSecPhase2GWOutDrops.setUnits("Packets")
_CipSecPhase2GWOutAuths_Type = Counter32
_CipSecPhase2GWOutAuths_Object = MibTableColumn
cipSecPhase2GWOutAuths = _CipSecPhase2GWOutAuths_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 5, 1, 20),
    _CipSecPhase2GWOutAuths_Type()
)
cipSecPhase2GWOutAuths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecPhase2GWOutAuths.setStatus("current")
if mibBuilder.loadTexts:
    cipSecPhase2GWOutAuths.setUnits("Events")
_CipSecPhase2GWOutAuthFails_Type = Counter32
_CipSecPhase2GWOutAuthFails_Object = MibTableColumn
cipSecPhase2GWOutAuthFails = _CipSecPhase2GWOutAuthFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 5, 1, 21),
    _CipSecPhase2GWOutAuthFails_Type()
)
cipSecPhase2GWOutAuthFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecPhase2GWOutAuthFails.setStatus("current")
if mibBuilder.loadTexts:
    cipSecPhase2GWOutAuthFails.setUnits("Failures")
_CipSecPhase2GWOutEncrypts_Type = Counter32
_CipSecPhase2GWOutEncrypts_Object = MibTableColumn
cipSecPhase2GWOutEncrypts = _CipSecPhase2GWOutEncrypts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 5, 1, 22),
    _CipSecPhase2GWOutEncrypts_Type()
)
cipSecPhase2GWOutEncrypts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecPhase2GWOutEncrypts.setStatus("current")
if mibBuilder.loadTexts:
    cipSecPhase2GWOutEncrypts.setUnits("Packets")
_CipSecPhase2GWOutEncryptFails_Type = Counter32
_CipSecPhase2GWOutEncryptFails_Object = MibTableColumn
cipSecPhase2GWOutEncryptFails = _CipSecPhase2GWOutEncryptFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 5, 1, 23),
    _CipSecPhase2GWOutEncryptFails_Type()
)
cipSecPhase2GWOutEncryptFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecPhase2GWOutEncryptFails.setStatus("current")
if mibBuilder.loadTexts:
    cipSecPhase2GWOutEncryptFails.setUnits("Failures")
_CipSecPhase2GWProtocolUseFails_Type = Counter32
_CipSecPhase2GWProtocolUseFails_Object = MibTableColumn
cipSecPhase2GWProtocolUseFails = _CipSecPhase2GWProtocolUseFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 5, 1, 24),
    _CipSecPhase2GWProtocolUseFails_Type()
)
cipSecPhase2GWProtocolUseFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecPhase2GWProtocolUseFails.setStatus("current")
if mibBuilder.loadTexts:
    cipSecPhase2GWProtocolUseFails.setUnits("Failures")
_CipSecPhase2GWNoSaFails_Type = Counter32
_CipSecPhase2GWNoSaFails_Object = MibTableColumn
cipSecPhase2GWNoSaFails = _CipSecPhase2GWNoSaFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 5, 1, 25),
    _CipSecPhase2GWNoSaFails_Type()
)
cipSecPhase2GWNoSaFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecPhase2GWNoSaFails.setStatus("current")
if mibBuilder.loadTexts:
    cipSecPhase2GWNoSaFails.setUnits("Failures")
_CipSecPhase2GWSysCapFails_Type = Counter32
_CipSecPhase2GWSysCapFails_Object = MibTableColumn
cipSecPhase2GWSysCapFails = _CipSecPhase2GWSysCapFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 3, 5, 1, 26),
    _CipSecPhase2GWSysCapFails_Type()
)
cipSecPhase2GWSysCapFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecPhase2GWSysCapFails.setStatus("current")
if mibBuilder.loadTexts:
    cipSecPhase2GWSysCapFails.setUnits("Failures")
_CipSecHistory_ObjectIdentity = ObjectIdentity
cipSecHistory = _CipSecHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 4)
)
_CipSecHistGlobal_ObjectIdentity = ObjectIdentity
cipSecHistGlobal = _CipSecHistGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 4, 1)
)
_CipSecHistGlobalCntl_ObjectIdentity = ObjectIdentity
cipSecHistGlobalCntl = _CipSecHistGlobalCntl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 4, 1, 1)
)


class _CipSecHistTableSize_Type(Integer32):
    """Custom type cipSecHistTableSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CipSecHistTableSize_Type.__name__ = "Integer32"
_CipSecHistTableSize_Object = MibScalar
cipSecHistTableSize = _CipSecHistTableSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 4, 1, 1, 1),
    _CipSecHistTableSize_Type()
)
cipSecHistTableSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cipSecHistTableSize.setStatus("current")


class _CipSecHistCheckPoint_Type(Integer32):
    """Custom type cipSecHistCheckPoint based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("checkPoint", 2),
          ("ready", 1))
    )


_CipSecHistCheckPoint_Type.__name__ = "Integer32"
_CipSecHistCheckPoint_Object = MibScalar
cipSecHistCheckPoint = _CipSecHistCheckPoint_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 4, 1, 1, 2),
    _CipSecHistCheckPoint_Type()
)
cipSecHistCheckPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cipSecHistCheckPoint.setStatus("current")
_CipSecHistPhaseOne_ObjectIdentity = ObjectIdentity
cipSecHistPhaseOne = _CipSecHistPhaseOne_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 4, 2)
)
_CikeTunnelHistTable_Object = MibTable
cikeTunnelHistTable = _CikeTunnelHistTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 4, 2, 1)
)
if mibBuilder.loadTexts:
    cikeTunnelHistTable.setStatus("current")
_CikeTunnelHistEntry_Object = MibTableRow
cikeTunnelHistEntry = _CikeTunnelHistEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 4, 2, 1, 1)
)
cikeTunnelHistEntry.setIndexNames(
    (0, "CISCO-IPSEC-FLOW-MONITOR-MIB", "cikeTunHistIndex"),
)
if mibBuilder.loadTexts:
    cikeTunnelHistEntry.setStatus("current")


class _CikeTunHistIndex_Type(Integer32):
    """Custom type cikeTunHistIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CikeTunHistIndex_Type.__name__ = "Integer32"
_CikeTunHistIndex_Object = MibTableColumn
cikeTunHistIndex = _CikeTunHistIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 4, 2, 1, 1, 1),
    _CikeTunHistIndex_Type()
)
cikeTunHistIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cikeTunHistIndex.setStatus("current")


class _CikeTunHistTermReason_Type(Integer32):
    """Custom type cikeTunHistTermReason based on Integer32"""
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
        *(("checkPointReg", 7),
          ("localFailure", 6),
          ("normal", 2),
          ("operRequest", 3),
          ("other", 1),
          ("peerDelRequest", 4),
          ("peerLost", 5))
    )


_CikeTunHistTermReason_Type.__name__ = "Integer32"
_CikeTunHistTermReason_Object = MibTableColumn
cikeTunHistTermReason = _CikeTunHistTermReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 4, 2, 1, 1, 2),
    _CikeTunHistTermReason_Type()
)
cikeTunHistTermReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikeTunHistTermReason.setStatus("current")


class _CikeTunHistActiveIndex_Type(Integer32):
    """Custom type cikeTunHistActiveIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CikeTunHistActiveIndex_Type.__name__ = "Integer32"
_CikeTunHistActiveIndex_Object = MibTableColumn
cikeTunHistActiveIndex = _CikeTunHistActiveIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 4, 2, 1, 1, 3),
    _CikeTunHistActiveIndex_Type()
)
cikeTunHistActiveIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikeTunHistActiveIndex.setStatus("current")
_CikeTunHistPeerLocalType_Type = IkePeerType
_CikeTunHistPeerLocalType_Object = MibTableColumn
cikeTunHistPeerLocalType = _CikeTunHistPeerLocalType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 4, 2, 1, 1, 4),
    _CikeTunHistPeerLocalType_Type()
)
cikeTunHistPeerLocalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikeTunHistPeerLocalType.setStatus("current")
_CikeTunHistPeerLocalValue_Type = DisplayString
_CikeTunHistPeerLocalValue_Object = MibTableColumn
cikeTunHistPeerLocalValue = _CikeTunHistPeerLocalValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 4, 2, 1, 1, 5),
    _CikeTunHistPeerLocalValue_Type()
)
cikeTunHistPeerLocalValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikeTunHistPeerLocalValue.setStatus("current")


class _CikeTunHistPeerIntIndex_Type(Integer32):
    """Custom type cikeTunHistPeerIntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CikeTunHistPeerIntIndex_Type.__name__ = "Integer32"
_CikeTunHistPeerIntIndex_Object = MibTableColumn
cikeTunHistPeerIntIndex = _CikeTunHistPeerIntIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 4, 2, 1, 1, 6),
    _CikeTunHistPeerIntIndex_Type()
)
cikeTunHistPeerIntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikeTunHistPeerIntIndex.setStatus("current")
_CikeTunHistPeerRemoteType_Type = IkePeerType
_CikeTunHistPeerRemoteType_Object = MibTableColumn
cikeTunHistPeerRemoteType = _CikeTunHistPeerRemoteType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 4, 2, 1, 1, 7),
    _CikeTunHistPeerRemoteType_Type()
)
cikeTunHistPeerRemoteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikeTunHistPeerRemoteType.setStatus("current")
_CikeTunHistPeerRemoteValue_Type = DisplayString
_CikeTunHistPeerRemoteValue_Object = MibTableColumn
cikeTunHistPeerRemoteValue = _CikeTunHistPeerRemoteValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 4, 2, 1, 1, 8),
    _CikeTunHistPeerRemoteValue_Type()
)
cikeTunHistPeerRemoteValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikeTunHistPeerRemoteValue.setStatus("current")
_CikeTunHistLocalAddr_Type = IPSIpAddress
_CikeTunHistLocalAddr_Object = MibTableColumn
cikeTunHistLocalAddr = _CikeTunHistLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 4, 2, 1, 1, 9),
    _CikeTunHistLocalAddr_Type()
)
cikeTunHistLocalAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikeTunHistLocalAddr.setStatus("current")
_CikeTunHistLocalName_Type = DisplayString
_CikeTunHistLocalName_Object = MibTableColumn
cikeTunHistLocalName = _CikeTunHistLocalName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 4, 2, 1, 1, 10),
    _CikeTunHistLocalName_Type()
)
cikeTunHistLocalName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikeTunHistLocalName.setStatus("current")
_CikeTunHistRemoteAddr_Type = IPSIpAddress
_CikeTunHistRemoteAddr_Object = MibTableColumn
cikeTunHistRemoteAddr = _CikeTunHistRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 4, 2, 1, 1, 11),
    _CikeTunHistRemoteAddr_Type()
)
cikeTunHistRemoteAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikeTunHistRemoteAddr.setStatus("current")
_CikeTunHistRemoteName_Type = DisplayString
_CikeTunHistRemoteName_Object = MibTableColumn
cikeTunHistRemoteName = _CikeTunHistRemoteName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 4, 2, 1, 1, 12),
    _CikeTunHistRemoteName_Type()
)
cikeTunHistRemoteName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikeTunHistRemoteName.setStatus("current")
_CikeTunHistNegoMode_Type = IkeNegoMode
_CikeTunHistNegoMode_Object = MibTableColumn
cikeTunHistNegoMode = _CikeTunHistNegoMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 4, 2, 1, 1, 13),
    _CikeTunHistNegoMode_Type()
)
cikeTunHistNegoMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikeTunHistNegoMode.setStatus("current")
_CikeTunHistDiffHellmanGrp_Type = DiffHellmanGrp
_CikeTunHistDiffHellmanGrp_Object = MibTableColumn
cikeTunHistDiffHellmanGrp = _CikeTunHistDiffHellmanGrp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 4, 2, 1, 1, 14),
    _CikeTunHistDiffHellmanGrp_Type()
)
cikeTunHistDiffHellmanGrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikeTunHistDiffHellmanGrp.setStatus("current")
_CikeTunHistEncryptAlgo_Type = EncryptAlgo
_CikeTunHistEncryptAlgo_Object = MibTableColumn
cikeTunHistEncryptAlgo = _CikeTunHistEncryptAlgo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 4, 2, 1, 1, 15),
    _CikeTunHistEncryptAlgo_Type()
)
cikeTunHistEncryptAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikeTunHistEncryptAlgo.setStatus("current")
_CikeTunHistHashAlgo_Type = IkeHashAlgo
_CikeTunHistHashAlgo_Object = MibTableColumn
cikeTunHistHashAlgo = _CikeTunHistHashAlgo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 4, 2, 1, 1, 16),
    _CikeTunHistHashAlgo_Type()
)
cikeTunHistHashAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikeTunHistHashAlgo.setStatus("current")
_CikeTunHistAuthMethod_Type = IkeAuthMethod
_CikeTunHistAuthMethod_Object = MibTableColumn
cikeTunHistAuthMethod = _CikeTunHistAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 4, 2, 1, 1, 17),
    _CikeTunHistAuthMethod_Type()
)
cikeTunHistAuthMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikeTunHistAuthMethod.setStatus("current")


class _CikeTunHistLifeTime_Type(Integer32):
    """Custom type cikeTunHistLifeTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CikeTunHistLifeTime_Type.__name__ = "Integer32"
_CikeTunHistLifeTime_Object = MibTableColumn
cikeTunHistLifeTime = _CikeTunHistLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 4, 2, 1, 1, 18),
    _CikeTunHistLifeTime_Type()
)
cikeTunHistLifeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikeTunHistLifeTime.setStatus("current")
_CikeTunHistStartTime_Type = TimeStamp
_CikeTunHistStartTime_Object = MibTableColumn
cikeTunHistStartTime = _CikeTunHistStartTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 4, 2, 1, 1, 19),
    _CikeTunHistStartTime_Type()
)
cikeTunHistStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikeTunHistStartTime.setStatus("current")
_CikeTunHistActiveTime_Type = TimeInterval
_CikeTunHistActiveTime_Object = MibTableColumn
cikeTunHistActiveTime = _CikeTunHistActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 4, 2, 1, 1, 20),
    _CikeTunHistActiveTime_Type()
)
cikeTunHistActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikeTunHistActiveTime.setStatus("current")
_CikeTunHistTotalRefreshes_Type = Counter32
_CikeTunHistTotalRefreshes_Object = MibTableColumn
cikeTunHistTotalRefreshes = _CikeTunHistTotalRefreshes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 4, 2, 1, 1, 21),
    _CikeTunHistTotalRefreshes_Type()
)
cikeTunHistTotalRefreshes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikeTunHistTotalRefreshes.setStatus("current")
if mibBuilder.loadTexts:
    cikeTunHistTotalRefreshes.setUnits("QM Exchanges")
_CikeTunHistTotalSas_Type = Counter32
_CikeTunHistTotalSas_Object = MibTableColumn
cikeTunHistTotalSas = _CikeTunHistTotalSas_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 4, 2, 1, 1, 22),
    _CikeTunHistTotalSas_Type()
)
cikeTunHistTotalSas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikeTunHistTotalSas.setStatus("current")
if mibBuilder.loadTexts:
    cikeTunHistTotalSas.setUnits("SAs")
_CikeTunHistInOctets_Type = Counter32
_CikeTunHistInOctets_Object = MibTableColumn
cikeTunHistInOctets = _CikeTunHistInOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 4, 2, 1, 1, 23),
    _CikeTunHistInOctets_Type()
)
cikeTunHistInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikeTunHistInOctets.setStatus("current")
if mibBuilder.loadTexts:
    cikeTunHistInOctets.setUnits("Octets")
_CikeTunHistInPkts_Type = Counter32
_CikeTunHistInPkts_Object = MibTableColumn
cikeTunHistInPkts = _CikeTunHistInPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 4, 2, 1, 1, 24),
    _CikeTunHistInPkts_Type()
)
cikeTunHistInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikeTunHistInPkts.setStatus("current")
if mibBuilder.loadTexts:
    cikeTunHistInPkts.setUnits("Packets")
_CikeTunHistInDropPkts_Type = Counter32
_CikeTunHistInDropPkts_Object = MibTableColumn
cikeTunHistInDropPkts = _CikeTunHistInDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 4, 2, 1, 1, 25),
    _CikeTunHistInDropPkts_Type()
)
cikeTunHistInDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikeTunHistInDropPkts.setStatus("current")
if mibBuilder.loadTexts:
    cikeTunHistInDropPkts.setUnits("Packets")
_CikeTunHistInNotifys_Type = Counter32
_CikeTunHistInNotifys_Object = MibTableColumn
cikeTunHistInNotifys = _CikeTunHistInNotifys_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 4, 2, 1, 1, 26),
    _CikeTunHistInNotifys_Type()
)
cikeTunHistInNotifys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikeTunHistInNotifys.setStatus("current")
if mibBuilder.loadTexts:
    cikeTunHistInNotifys.setUnits("Notification Payloads")
_CikeTunHistInP2Exchgs_Type = Counter32
_CikeTunHistInP2Exchgs_Object = MibTableColumn
cikeTunHistInP2Exchgs = _CikeTunHistInP2Exchgs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 4, 2, 1, 1, 27),
    _CikeTunHistInP2Exchgs_Type()
)
cikeTunHistInP2Exchgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikeTunHistInP2Exchgs.setStatus("current")
if mibBuilder.loadTexts:
    cikeTunHistInP2Exchgs.setUnits("SA Payloads")
_CikeTunHistInP2ExchgInvalids_Type = Counter32
_CikeTunHistInP2ExchgInvalids_Object = MibTableColumn
cikeTunHistInP2ExchgInvalids = _CikeTunHistInP2ExchgInvalids_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 4, 2, 1, 1, 28),
    _CikeTunHistInP2ExchgInvalids_Type()
)
cikeTunHistInP2ExchgInvalids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikeTunHistInP2ExchgInvalids.setStatus("current")
if mibBuilder.loadTexts:
    cikeTunHistInP2ExchgInvalids.setUnits("SA Payloads")
_CikeTunHistInP2ExchgRejects_Type = Counter32
_CikeTunHistInP2ExchgRejects_Object = MibTableColumn
cikeTunHistInP2ExchgRejects = _CikeTunHistInP2ExchgRejects_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 4, 2, 1, 1, 29),
    _CikeTunHistInP2ExchgRejects_Type()
)
cikeTunHistInP2ExchgRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikeTunHistInP2ExchgRejects.setStatus("current")
if mibBuilder.loadTexts:
    cikeTunHistInP2ExchgRejects.setUnits("SA Payloads")
_CikeTunHistInP2SaDelRequests_Type = Counter32
_CikeTunHistInP2SaDelRequests_Object = MibTableColumn
cikeTunHistInP2SaDelRequests = _CikeTunHistInP2SaDelRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 4, 2, 1, 1, 30),
    _CikeTunHistInP2SaDelRequests_Type()
)
cikeTunHistInP2SaDelRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikeTunHistInP2SaDelRequests.setStatus("current")
if mibBuilder.loadTexts:
    cikeTunHistInP2SaDelRequests.setUnits("Notification Payloads")
_CikeTunHistOutOctets_Type = Counter32
_CikeTunHistOutOctets_Object = MibTableColumn
cikeTunHistOutOctets = _CikeTunHistOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 4, 2, 1, 1, 31),
    _CikeTunHistOutOctets_Type()
)
cikeTunHistOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikeTunHistOutOctets.setStatus("current")
if mibBuilder.loadTexts:
    cikeTunHistOutOctets.setUnits("Octets")
_CikeTunHistOutPkts_Type = Counter32
_CikeTunHistOutPkts_Object = MibTableColumn
cikeTunHistOutPkts = _CikeTunHistOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 4, 2, 1, 1, 32),
    _CikeTunHistOutPkts_Type()
)
cikeTunHistOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikeTunHistOutPkts.setStatus("current")
if mibBuilder.loadTexts:
    cikeTunHistOutPkts.setUnits("Packets")
_CikeTunHistOutDropPkts_Type = Counter32
_CikeTunHistOutDropPkts_Object = MibTableColumn
cikeTunHistOutDropPkts = _CikeTunHistOutDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 4, 2, 1, 1, 33),
    _CikeTunHistOutDropPkts_Type()
)
cikeTunHistOutDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikeTunHistOutDropPkts.setStatus("current")
if mibBuilder.loadTexts:
    cikeTunHistOutDropPkts.setUnits("Packets")
_CikeTunHistOutNotifys_Type = Counter32
_CikeTunHistOutNotifys_Object = MibTableColumn
cikeTunHistOutNotifys = _CikeTunHistOutNotifys_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 4, 2, 1, 1, 34),
    _CikeTunHistOutNotifys_Type()
)
cikeTunHistOutNotifys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikeTunHistOutNotifys.setStatus("current")
if mibBuilder.loadTexts:
    cikeTunHistOutNotifys.setUnits("Notification Payloads")
_CikeTunHistOutP2Exchgs_Type = Counter32
_CikeTunHistOutP2Exchgs_Object = MibTableColumn
cikeTunHistOutP2Exchgs = _CikeTunHistOutP2Exchgs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 4, 2, 1, 1, 35),
    _CikeTunHistOutP2Exchgs_Type()
)
cikeTunHistOutP2Exchgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikeTunHistOutP2Exchgs.setStatus("current")
if mibBuilder.loadTexts:
    cikeTunHistOutP2Exchgs.setUnits("SA Payloads")
_CikeTunHistOutP2ExchgInvalids_Type = Counter32
_CikeTunHistOutP2ExchgInvalids_Object = MibTableColumn
cikeTunHistOutP2ExchgInvalids = _CikeTunHistOutP2ExchgInvalids_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 4, 2, 1, 1, 36),
    _CikeTunHistOutP2ExchgInvalids_Type()
)
cikeTunHistOutP2ExchgInvalids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikeTunHistOutP2ExchgInvalids.setStatus("current")
if mibBuilder.loadTexts:
    cikeTunHistOutP2ExchgInvalids.setUnits("SA Payloads")
_CikeTunHistOutP2ExchgRejects_Type = Counter32
_CikeTunHistOutP2ExchgRejects_Object = MibTableColumn
cikeTunHistOutP2ExchgRejects = _CikeTunHistOutP2ExchgRejects_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 4, 2, 1, 1, 37),
    _CikeTunHistOutP2ExchgRejects_Type()
)
cikeTunHistOutP2ExchgRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikeTunHistOutP2ExchgRejects.setStatus("current")
if mibBuilder.loadTexts:
    cikeTunHistOutP2ExchgRejects.setUnits("SA Payloads")
_CikeTunHistOutP2SaDelRequests_Type = Counter32
_CikeTunHistOutP2SaDelRequests_Object = MibTableColumn
cikeTunHistOutP2SaDelRequests = _CikeTunHistOutP2SaDelRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 4, 2, 1, 1, 38),
    _CikeTunHistOutP2SaDelRequests_Type()
)
cikeTunHistOutP2SaDelRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikeTunHistOutP2SaDelRequests.setStatus("current")
if mibBuilder.loadTexts:
    cikeTunHistOutP2SaDelRequests.setUnits("Notification Payloads")
_CipSecHistPhaseTwo_ObjectIdentity = ObjectIdentity
cipSecHistPhaseTwo = _CipSecHistPhaseTwo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 4, 3)
)
_CipSecTunnelHistTable_Object = MibTable
cipSecTunnelHistTable = _CipSecTunnelHistTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 4, 3, 1)
)
if mibBuilder.loadTexts:
    cipSecTunnelHistTable.setStatus("current")
_CipSecTunnelHistEntry_Object = MibTableRow
cipSecTunnelHistEntry = _CipSecTunnelHistEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 4, 3, 1, 1)
)
cipSecTunnelHistEntry.setIndexNames(
    (0, "CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecTunHistIndex"),
)
if mibBuilder.loadTexts:
    cipSecTunnelHistEntry.setStatus("current")


class _CipSecTunHistIndex_Type(Integer32):
    """Custom type cipSecTunHistIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CipSecTunHistIndex_Type.__name__ = "Integer32"
_CipSecTunHistIndex_Object = MibTableColumn
cipSecTunHistIndex = _CipSecTunHistIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 4, 3, 1, 1, 1),
    _CipSecTunHistIndex_Type()
)
cipSecTunHistIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cipSecTunHistIndex.setStatus("current")


class _CipSecTunHistTermReason_Type(Integer32):
    """Custom type cipSecTunHistTermReason based on Integer32"""
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
        *(("checkPointReq", 7),
          ("normal", 2),
          ("operRequest", 3),
          ("other", 1),
          ("peerDelRequest", 4),
          ("peerLost", 5),
          ("seqNumRollOver", 6))
    )


_CipSecTunHistTermReason_Type.__name__ = "Integer32"
_CipSecTunHistTermReason_Object = MibTableColumn
cipSecTunHistTermReason = _CipSecTunHistTermReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 4, 3, 1, 1, 2),
    _CipSecTunHistTermReason_Type()
)
cipSecTunHistTermReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecTunHistTermReason.setStatus("current")


class _CipSecTunHistActiveIndex_Type(Integer32):
    """Custom type cipSecTunHistActiveIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CipSecTunHistActiveIndex_Type.__name__ = "Integer32"
_CipSecTunHistActiveIndex_Object = MibTableColumn
cipSecTunHistActiveIndex = _CipSecTunHistActiveIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 4, 3, 1, 1, 3),
    _CipSecTunHistActiveIndex_Type()
)
cipSecTunHistActiveIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecTunHistActiveIndex.setStatus("current")


class _CipSecTunHistIkeTunnelIndex_Type(Integer32):
    """Custom type cipSecTunHistIkeTunnelIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CipSecTunHistIkeTunnelIndex_Type.__name__ = "Integer32"
_CipSecTunHistIkeTunnelIndex_Object = MibTableColumn
cipSecTunHistIkeTunnelIndex = _CipSecTunHistIkeTunnelIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 4, 3, 1, 1, 4),
    _CipSecTunHistIkeTunnelIndex_Type()
)
cipSecTunHistIkeTunnelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecTunHistIkeTunnelIndex.setStatus("current")
_CipSecTunHistLocalAddr_Type = IPSIpAddress
_CipSecTunHistLocalAddr_Object = MibTableColumn
cipSecTunHistLocalAddr = _CipSecTunHistLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 4, 3, 1, 1, 5),
    _CipSecTunHistLocalAddr_Type()
)
cipSecTunHistLocalAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecTunHistLocalAddr.setStatus("current")
_CipSecTunHistRemoteAddr_Type = IPSIpAddress
_CipSecTunHistRemoteAddr_Object = MibTableColumn
cipSecTunHistRemoteAddr = _CipSecTunHistRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 4, 3, 1, 1, 6),
    _CipSecTunHistRemoteAddr_Type()
)
cipSecTunHistRemoteAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecTunHistRemoteAddr.setStatus("current")
_CipSecTunHistKeyType_Type = KeyType
_CipSecTunHistKeyType_Object = MibTableColumn
cipSecTunHistKeyType = _CipSecTunHistKeyType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 4, 3, 1, 1, 7),
    _CipSecTunHistKeyType_Type()
)
cipSecTunHistKeyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecTunHistKeyType.setStatus("current")
_CipSecTunHistEncapMode_Type = EncapMode
_CipSecTunHistEncapMode_Object = MibTableColumn
cipSecTunHistEncapMode = _CipSecTunHistEncapMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 4, 3, 1, 1, 8),
    _CipSecTunHistEncapMode_Type()
)
cipSecTunHistEncapMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecTunHistEncapMode.setStatus("current")


class _CipSecTunHistLifeSize_Type(Integer32):
    """Custom type cipSecTunHistLifeSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CipSecTunHistLifeSize_Type.__name__ = "Integer32"
_CipSecTunHistLifeSize_Object = MibTableColumn
cipSecTunHistLifeSize = _CipSecTunHistLifeSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 4, 3, 1, 1, 9),
    _CipSecTunHistLifeSize_Type()
)
cipSecTunHistLifeSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecTunHistLifeSize.setStatus("current")
if mibBuilder.loadTexts:
    cipSecTunHistLifeSize.setUnits("KBytes")


class _CipSecTunHistLifeTime_Type(Integer32):
    """Custom type cipSecTunHistLifeTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CipSecTunHistLifeTime_Type.__name__ = "Integer32"
_CipSecTunHistLifeTime_Object = MibTableColumn
cipSecTunHistLifeTime = _CipSecTunHistLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 4, 3, 1, 1, 10),
    _CipSecTunHistLifeTime_Type()
)
cipSecTunHistLifeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecTunHistLifeTime.setStatus("current")
if mibBuilder.loadTexts:
    cipSecTunHistLifeTime.setUnits("Seconds")
_CipSecTunHistStartTime_Type = TimeStamp
_CipSecTunHistStartTime_Object = MibTableColumn
cipSecTunHistStartTime = _CipSecTunHistStartTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 4, 3, 1, 1, 11),
    _CipSecTunHistStartTime_Type()
)
cipSecTunHistStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecTunHistStartTime.setStatus("current")
_CipSecTunHistActiveTime_Type = TimeInterval
_CipSecTunHistActiveTime_Object = MibTableColumn
cipSecTunHistActiveTime = _CipSecTunHistActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 4, 3, 1, 1, 12),
    _CipSecTunHistActiveTime_Type()
)
cipSecTunHistActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecTunHistActiveTime.setStatus("current")
_CipSecTunHistTotalRefreshes_Type = Counter32
_CipSecTunHistTotalRefreshes_Object = MibTableColumn
cipSecTunHistTotalRefreshes = _CipSecTunHistTotalRefreshes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 4, 3, 1, 1, 13),
    _CipSecTunHistTotalRefreshes_Type()
)
cipSecTunHistTotalRefreshes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecTunHistTotalRefreshes.setStatus("current")
if mibBuilder.loadTexts:
    cipSecTunHistTotalRefreshes.setUnits("QM Exchanges")
_CipSecTunHistTotalSas_Type = Counter32
_CipSecTunHistTotalSas_Object = MibTableColumn
cipSecTunHistTotalSas = _CipSecTunHistTotalSas_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 4, 3, 1, 1, 14),
    _CipSecTunHistTotalSas_Type()
)
cipSecTunHistTotalSas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecTunHistTotalSas.setStatus("current")
if mibBuilder.loadTexts:
    cipSecTunHistTotalSas.setUnits("SAs")
_CipSecTunHistInSaDiffHellmanGrp_Type = DiffHellmanGrp
_CipSecTunHistInSaDiffHellmanGrp_Object = MibTableColumn
cipSecTunHistInSaDiffHellmanGrp = _CipSecTunHistInSaDiffHellmanGrp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 4, 3, 1, 1, 15),
    _CipSecTunHistInSaDiffHellmanGrp_Type()
)
cipSecTunHistInSaDiffHellmanGrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecTunHistInSaDiffHellmanGrp.setStatus("current")
_CipSecTunHistInSaEncryptAlgo_Type = EncryptAlgo
_CipSecTunHistInSaEncryptAlgo_Object = MibTableColumn
cipSecTunHistInSaEncryptAlgo = _CipSecTunHistInSaEncryptAlgo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 4, 3, 1, 1, 16),
    _CipSecTunHistInSaEncryptAlgo_Type()
)
cipSecTunHistInSaEncryptAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecTunHistInSaEncryptAlgo.setStatus("current")
_CipSecTunHistInSaAhAuthAlgo_Type = AuthAlgo
_CipSecTunHistInSaAhAuthAlgo_Object = MibTableColumn
cipSecTunHistInSaAhAuthAlgo = _CipSecTunHistInSaAhAuthAlgo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 4, 3, 1, 1, 17),
    _CipSecTunHistInSaAhAuthAlgo_Type()
)
cipSecTunHistInSaAhAuthAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecTunHistInSaAhAuthAlgo.setStatus("current")
_CipSecTunHistInSaEspAuthAlgo_Type = AuthAlgo
_CipSecTunHistInSaEspAuthAlgo_Object = MibTableColumn
cipSecTunHistInSaEspAuthAlgo = _CipSecTunHistInSaEspAuthAlgo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 4, 3, 1, 1, 18),
    _CipSecTunHistInSaEspAuthAlgo_Type()
)
cipSecTunHistInSaEspAuthAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecTunHistInSaEspAuthAlgo.setStatus("current")
_CipSecTunHistInSaDecompAlgo_Type = CompAlgo
_CipSecTunHistInSaDecompAlgo_Object = MibTableColumn
cipSecTunHistInSaDecompAlgo = _CipSecTunHistInSaDecompAlgo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 4, 3, 1, 1, 19),
    _CipSecTunHistInSaDecompAlgo_Type()
)
cipSecTunHistInSaDecompAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecTunHistInSaDecompAlgo.setStatus("current")
_CipSecTunHistOutSaDiffHellmanGrp_Type = DiffHellmanGrp
_CipSecTunHistOutSaDiffHellmanGrp_Object = MibTableColumn
cipSecTunHistOutSaDiffHellmanGrp = _CipSecTunHistOutSaDiffHellmanGrp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 4, 3, 1, 1, 20),
    _CipSecTunHistOutSaDiffHellmanGrp_Type()
)
cipSecTunHistOutSaDiffHellmanGrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecTunHistOutSaDiffHellmanGrp.setStatus("current")
_CipSecTunHistOutSaEncryptAlgo_Type = EncryptAlgo
_CipSecTunHistOutSaEncryptAlgo_Object = MibTableColumn
cipSecTunHistOutSaEncryptAlgo = _CipSecTunHistOutSaEncryptAlgo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 4, 3, 1, 1, 21),
    _CipSecTunHistOutSaEncryptAlgo_Type()
)
cipSecTunHistOutSaEncryptAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecTunHistOutSaEncryptAlgo.setStatus("current")
_CipSecTunHistOutSaAhAuthAlgo_Type = AuthAlgo
_CipSecTunHistOutSaAhAuthAlgo_Object = MibTableColumn
cipSecTunHistOutSaAhAuthAlgo = _CipSecTunHistOutSaAhAuthAlgo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 4, 3, 1, 1, 22),
    _CipSecTunHistOutSaAhAuthAlgo_Type()
)
cipSecTunHistOutSaAhAuthAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecTunHistOutSaAhAuthAlgo.setStatus("current")
_CipSecTunHistOutSaEspAuthAlgo_Type = AuthAlgo
_CipSecTunHistOutSaEspAuthAlgo_Object = MibTableColumn
cipSecTunHistOutSaEspAuthAlgo = _CipSecTunHistOutSaEspAuthAlgo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 4, 3, 1, 1, 23),
    _CipSecTunHistOutSaEspAuthAlgo_Type()
)
cipSecTunHistOutSaEspAuthAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecTunHistOutSaEspAuthAlgo.setStatus("current")
_CipSecTunHistOutSaCompAlgo_Type = CompAlgo
_CipSecTunHistOutSaCompAlgo_Object = MibTableColumn
cipSecTunHistOutSaCompAlgo = _CipSecTunHistOutSaCompAlgo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 4, 3, 1, 1, 24),
    _CipSecTunHistOutSaCompAlgo_Type()
)
cipSecTunHistOutSaCompAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecTunHistOutSaCompAlgo.setStatus("current")
_CipSecTunHistInOctets_Type = Counter32
_CipSecTunHistInOctets_Object = MibTableColumn
cipSecTunHistInOctets = _CipSecTunHistInOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 4, 3, 1, 1, 25),
    _CipSecTunHistInOctets_Type()
)
cipSecTunHistInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecTunHistInOctets.setStatus("current")
if mibBuilder.loadTexts:
    cipSecTunHistInOctets.setUnits("Octets")
_CipSecTunHistHcInOctets_Type = Counter64
_CipSecTunHistHcInOctets_Object = MibTableColumn
cipSecTunHistHcInOctets = _CipSecTunHistHcInOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 4, 3, 1, 1, 26),
    _CipSecTunHistHcInOctets_Type()
)
cipSecTunHistHcInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecTunHistHcInOctets.setStatus("current")
_CipSecTunHistInOctWraps_Type = Counter32
_CipSecTunHistInOctWraps_Object = MibTableColumn
cipSecTunHistInOctWraps = _CipSecTunHistInOctWraps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 4, 3, 1, 1, 27),
    _CipSecTunHistInOctWraps_Type()
)
cipSecTunHistInOctWraps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecTunHistInOctWraps.setStatus("current")
if mibBuilder.loadTexts:
    cipSecTunHistInOctWraps.setUnits("Integral units")
_CipSecTunHistInDecompOctets_Type = Counter32
_CipSecTunHistInDecompOctets_Object = MibTableColumn
cipSecTunHistInDecompOctets = _CipSecTunHistInDecompOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 4, 3, 1, 1, 28),
    _CipSecTunHistInDecompOctets_Type()
)
cipSecTunHistInDecompOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecTunHistInDecompOctets.setStatus("current")
if mibBuilder.loadTexts:
    cipSecTunHistInDecompOctets.setUnits("Octets")
_CipSecTunHistHcInDecompOctets_Type = Counter64
_CipSecTunHistHcInDecompOctets_Object = MibTableColumn
cipSecTunHistHcInDecompOctets = _CipSecTunHistHcInDecompOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 4, 3, 1, 1, 29),
    _CipSecTunHistHcInDecompOctets_Type()
)
cipSecTunHistHcInDecompOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecTunHistHcInDecompOctets.setStatus("current")
_CipSecTunHistInDecompOctWraps_Type = Counter32
_CipSecTunHistInDecompOctWraps_Object = MibTableColumn
cipSecTunHistInDecompOctWraps = _CipSecTunHistInDecompOctWraps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 4, 3, 1, 1, 30),
    _CipSecTunHistInDecompOctWraps_Type()
)
cipSecTunHistInDecompOctWraps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecTunHistInDecompOctWraps.setStatus("current")
if mibBuilder.loadTexts:
    cipSecTunHistInDecompOctWraps.setUnits("Integral units")
_CipSecTunHistInPkts_Type = Counter32
_CipSecTunHistInPkts_Object = MibTableColumn
cipSecTunHistInPkts = _CipSecTunHistInPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 4, 3, 1, 1, 31),
    _CipSecTunHistInPkts_Type()
)
cipSecTunHistInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecTunHistInPkts.setStatus("current")
if mibBuilder.loadTexts:
    cipSecTunHistInPkts.setUnits("Packets")
_CipSecTunHistInDropPkts_Type = Counter32
_CipSecTunHistInDropPkts_Object = MibTableColumn
cipSecTunHistInDropPkts = _CipSecTunHistInDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 4, 3, 1, 1, 32),
    _CipSecTunHistInDropPkts_Type()
)
cipSecTunHistInDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecTunHistInDropPkts.setStatus("current")
if mibBuilder.loadTexts:
    cipSecTunHistInDropPkts.setUnits("Packets")
_CipSecTunHistInReplayDropPkts_Type = Counter32
_CipSecTunHistInReplayDropPkts_Object = MibTableColumn
cipSecTunHistInReplayDropPkts = _CipSecTunHistInReplayDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 4, 3, 1, 1, 33),
    _CipSecTunHistInReplayDropPkts_Type()
)
cipSecTunHistInReplayDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecTunHistInReplayDropPkts.setStatus("current")
if mibBuilder.loadTexts:
    cipSecTunHistInReplayDropPkts.setUnits("Packets")
_CipSecTunHistInAuths_Type = Counter32
_CipSecTunHistInAuths_Object = MibTableColumn
cipSecTunHistInAuths = _CipSecTunHistInAuths_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 4, 3, 1, 1, 34),
    _CipSecTunHistInAuths_Type()
)
cipSecTunHistInAuths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecTunHistInAuths.setStatus("current")
if mibBuilder.loadTexts:
    cipSecTunHistInAuths.setUnits("Events")
_CipSecTunHistInAuthFails_Type = Counter32
_CipSecTunHistInAuthFails_Object = MibTableColumn
cipSecTunHistInAuthFails = _CipSecTunHistInAuthFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 4, 3, 1, 1, 35),
    _CipSecTunHistInAuthFails_Type()
)
cipSecTunHistInAuthFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecTunHistInAuthFails.setStatus("current")
if mibBuilder.loadTexts:
    cipSecTunHistInAuthFails.setUnits("Failures")
_CipSecTunHistInDecrypts_Type = Counter32
_CipSecTunHistInDecrypts_Object = MibTableColumn
cipSecTunHistInDecrypts = _CipSecTunHistInDecrypts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 4, 3, 1, 1, 36),
    _CipSecTunHistInDecrypts_Type()
)
cipSecTunHistInDecrypts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecTunHistInDecrypts.setStatus("current")
if mibBuilder.loadTexts:
    cipSecTunHistInDecrypts.setUnits("Packets")
_CipSecTunHistInDecryptFails_Type = Counter32
_CipSecTunHistInDecryptFails_Object = MibTableColumn
cipSecTunHistInDecryptFails = _CipSecTunHistInDecryptFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 4, 3, 1, 1, 37),
    _CipSecTunHistInDecryptFails_Type()
)
cipSecTunHistInDecryptFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecTunHistInDecryptFails.setStatus("current")
if mibBuilder.loadTexts:
    cipSecTunHistInDecryptFails.setUnits("Failures")
_CipSecTunHistOutOctets_Type = Counter32
_CipSecTunHistOutOctets_Object = MibTableColumn
cipSecTunHistOutOctets = _CipSecTunHistOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 4, 3, 1, 1, 38),
    _CipSecTunHistOutOctets_Type()
)
cipSecTunHistOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecTunHistOutOctets.setStatus("current")
if mibBuilder.loadTexts:
    cipSecTunHistOutOctets.setUnits("Octets")
_CipSecTunHistHcOutOctets_Type = Counter64
_CipSecTunHistHcOutOctets_Object = MibTableColumn
cipSecTunHistHcOutOctets = _CipSecTunHistHcOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 4, 3, 1, 1, 39),
    _CipSecTunHistHcOutOctets_Type()
)
cipSecTunHistHcOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecTunHistHcOutOctets.setStatus("current")
_CipSecTunHistOutOctWraps_Type = Counter32
_CipSecTunHistOutOctWraps_Object = MibTableColumn
cipSecTunHistOutOctWraps = _CipSecTunHistOutOctWraps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 4, 3, 1, 1, 40),
    _CipSecTunHistOutOctWraps_Type()
)
cipSecTunHistOutOctWraps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecTunHistOutOctWraps.setStatus("current")
if mibBuilder.loadTexts:
    cipSecTunHistOutOctWraps.setUnits("Integral units")
_CipSecTunHistOutUncompOctets_Type = Counter32
_CipSecTunHistOutUncompOctets_Object = MibTableColumn
cipSecTunHistOutUncompOctets = _CipSecTunHistOutUncompOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 4, 3, 1, 1, 41),
    _CipSecTunHistOutUncompOctets_Type()
)
cipSecTunHistOutUncompOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecTunHistOutUncompOctets.setStatus("current")
if mibBuilder.loadTexts:
    cipSecTunHistOutUncompOctets.setUnits("Octets")
_CipSecTunHistHcOutUncompOctets_Type = Counter64
_CipSecTunHistHcOutUncompOctets_Object = MibTableColumn
cipSecTunHistHcOutUncompOctets = _CipSecTunHistHcOutUncompOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 4, 3, 1, 1, 42),
    _CipSecTunHistHcOutUncompOctets_Type()
)
cipSecTunHistHcOutUncompOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecTunHistHcOutUncompOctets.setStatus("current")
if mibBuilder.loadTexts:
    cipSecTunHistHcOutUncompOctets.setUnits("Octets")
_CipSecTunHistOutUncompOctWraps_Type = Counter32
_CipSecTunHistOutUncompOctWraps_Object = MibTableColumn
cipSecTunHistOutUncompOctWraps = _CipSecTunHistOutUncompOctWraps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 4, 3, 1, 1, 43),
    _CipSecTunHistOutUncompOctWraps_Type()
)
cipSecTunHistOutUncompOctWraps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecTunHistOutUncompOctWraps.setStatus("current")
if mibBuilder.loadTexts:
    cipSecTunHistOutUncompOctWraps.setUnits("Integral units")
_CipSecTunHistOutPkts_Type = Counter32
_CipSecTunHistOutPkts_Object = MibTableColumn
cipSecTunHistOutPkts = _CipSecTunHistOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 4, 3, 1, 1, 44),
    _CipSecTunHistOutPkts_Type()
)
cipSecTunHistOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecTunHistOutPkts.setStatus("current")
if mibBuilder.loadTexts:
    cipSecTunHistOutPkts.setUnits("Packets")
_CipSecTunHistOutDropPkts_Type = Counter32
_CipSecTunHistOutDropPkts_Object = MibTableColumn
cipSecTunHistOutDropPkts = _CipSecTunHistOutDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 4, 3, 1, 1, 45),
    _CipSecTunHistOutDropPkts_Type()
)
cipSecTunHistOutDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecTunHistOutDropPkts.setStatus("current")
if mibBuilder.loadTexts:
    cipSecTunHistOutDropPkts.setUnits("Packets")
_CipSecTunHistOutAuths_Type = Counter32
_CipSecTunHistOutAuths_Object = MibTableColumn
cipSecTunHistOutAuths = _CipSecTunHistOutAuths_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 4, 3, 1, 1, 46),
    _CipSecTunHistOutAuths_Type()
)
cipSecTunHistOutAuths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecTunHistOutAuths.setStatus("current")
if mibBuilder.loadTexts:
    cipSecTunHistOutAuths.setUnits("Events")
_CipSecTunHistOutAuthFails_Type = Counter32
_CipSecTunHistOutAuthFails_Object = MibTableColumn
cipSecTunHistOutAuthFails = _CipSecTunHistOutAuthFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 4, 3, 1, 1, 47),
    _CipSecTunHistOutAuthFails_Type()
)
cipSecTunHistOutAuthFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecTunHistOutAuthFails.setStatus("current")
if mibBuilder.loadTexts:
    cipSecTunHistOutAuthFails.setUnits("Failures")
_CipSecTunHistOutEncrypts_Type = Counter32
_CipSecTunHistOutEncrypts_Object = MibTableColumn
cipSecTunHistOutEncrypts = _CipSecTunHistOutEncrypts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 4, 3, 1, 1, 48),
    _CipSecTunHistOutEncrypts_Type()
)
cipSecTunHistOutEncrypts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecTunHistOutEncrypts.setStatus("current")
if mibBuilder.loadTexts:
    cipSecTunHistOutEncrypts.setUnits("Packets")
_CipSecTunHistOutEncryptFails_Type = Counter32
_CipSecTunHistOutEncryptFails_Object = MibTableColumn
cipSecTunHistOutEncryptFails = _CipSecTunHistOutEncryptFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 4, 3, 1, 1, 49),
    _CipSecTunHistOutEncryptFails_Type()
)
cipSecTunHistOutEncryptFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecTunHistOutEncryptFails.setStatus("current")
if mibBuilder.loadTexts:
    cipSecTunHistOutEncryptFails.setUnits("Failures")
_CipSecEndPtHistTable_Object = MibTable
cipSecEndPtHistTable = _CipSecEndPtHistTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 4, 3, 2)
)
if mibBuilder.loadTexts:
    cipSecEndPtHistTable.setStatus("current")
_CipSecEndPtHistEntry_Object = MibTableRow
cipSecEndPtHistEntry = _CipSecEndPtHistEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 4, 3, 2, 1)
)
cipSecEndPtHistEntry.setIndexNames(
    (0, "CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecEndPtHistIndex"),
)
if mibBuilder.loadTexts:
    cipSecEndPtHistEntry.setStatus("current")


class _CipSecEndPtHistIndex_Type(Integer32):
    """Custom type cipSecEndPtHistIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CipSecEndPtHistIndex_Type.__name__ = "Integer32"
_CipSecEndPtHistIndex_Object = MibTableColumn
cipSecEndPtHistIndex = _CipSecEndPtHistIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 4, 3, 2, 1, 1),
    _CipSecEndPtHistIndex_Type()
)
cipSecEndPtHistIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cipSecEndPtHistIndex.setStatus("current")


class _CipSecEndPtHistTunIndex_Type(Integer32):
    """Custom type cipSecEndPtHistTunIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CipSecEndPtHistTunIndex_Type.__name__ = "Integer32"
_CipSecEndPtHistTunIndex_Object = MibTableColumn
cipSecEndPtHistTunIndex = _CipSecEndPtHistTunIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 4, 3, 2, 1, 2),
    _CipSecEndPtHistTunIndex_Type()
)
cipSecEndPtHistTunIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecEndPtHistTunIndex.setStatus("current")


class _CipSecEndPtHistActiveIndex_Type(Integer32):
    """Custom type cipSecEndPtHistActiveIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CipSecEndPtHistActiveIndex_Type.__name__ = "Integer32"
_CipSecEndPtHistActiveIndex_Object = MibTableColumn
cipSecEndPtHistActiveIndex = _CipSecEndPtHistActiveIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 4, 3, 2, 1, 3),
    _CipSecEndPtHistActiveIndex_Type()
)
cipSecEndPtHistActiveIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecEndPtHistActiveIndex.setStatus("current")
_CipSecEndPtHistLocalName_Type = DisplayString
_CipSecEndPtHistLocalName_Object = MibTableColumn
cipSecEndPtHistLocalName = _CipSecEndPtHistLocalName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 4, 3, 2, 1, 4),
    _CipSecEndPtHistLocalName_Type()
)
cipSecEndPtHistLocalName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecEndPtHistLocalName.setStatus("current")
_CipSecEndPtHistLocalType_Type = EndPtType
_CipSecEndPtHistLocalType_Object = MibTableColumn
cipSecEndPtHistLocalType = _CipSecEndPtHistLocalType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 4, 3, 2, 1, 5),
    _CipSecEndPtHistLocalType_Type()
)
cipSecEndPtHistLocalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecEndPtHistLocalType.setStatus("current")
_CipSecEndPtHistLocalAddr1_Type = IPSIpAddress
_CipSecEndPtHistLocalAddr1_Object = MibTableColumn
cipSecEndPtHistLocalAddr1 = _CipSecEndPtHistLocalAddr1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 4, 3, 2, 1, 6),
    _CipSecEndPtHistLocalAddr1_Type()
)
cipSecEndPtHistLocalAddr1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecEndPtHistLocalAddr1.setStatus("current")
_CipSecEndPtHistLocalAddr2_Type = IPSIpAddress
_CipSecEndPtHistLocalAddr2_Object = MibTableColumn
cipSecEndPtHistLocalAddr2 = _CipSecEndPtHistLocalAddr2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 4, 3, 2, 1, 7),
    _CipSecEndPtHistLocalAddr2_Type()
)
cipSecEndPtHistLocalAddr2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecEndPtHistLocalAddr2.setStatus("current")


class _CipSecEndPtHistLocalProtocol_Type(Integer32):
    """Custom type cipSecEndPtHistLocalProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CipSecEndPtHistLocalProtocol_Type.__name__ = "Integer32"
_CipSecEndPtHistLocalProtocol_Object = MibTableColumn
cipSecEndPtHistLocalProtocol = _CipSecEndPtHistLocalProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 4, 3, 2, 1, 8),
    _CipSecEndPtHistLocalProtocol_Type()
)
cipSecEndPtHistLocalProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecEndPtHistLocalProtocol.setStatus("current")


class _CipSecEndPtHistLocalPort_Type(Integer32):
    """Custom type cipSecEndPtHistLocalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CipSecEndPtHistLocalPort_Type.__name__ = "Integer32"
_CipSecEndPtHistLocalPort_Object = MibTableColumn
cipSecEndPtHistLocalPort = _CipSecEndPtHistLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 4, 3, 2, 1, 9),
    _CipSecEndPtHistLocalPort_Type()
)
cipSecEndPtHistLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecEndPtHistLocalPort.setStatus("current")
_CipSecEndPtHistRemoteName_Type = DisplayString
_CipSecEndPtHistRemoteName_Object = MibTableColumn
cipSecEndPtHistRemoteName = _CipSecEndPtHistRemoteName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 4, 3, 2, 1, 10),
    _CipSecEndPtHistRemoteName_Type()
)
cipSecEndPtHistRemoteName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecEndPtHistRemoteName.setStatus("current")
_CipSecEndPtHistRemoteType_Type = EndPtType
_CipSecEndPtHistRemoteType_Object = MibTableColumn
cipSecEndPtHistRemoteType = _CipSecEndPtHistRemoteType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 4, 3, 2, 1, 11),
    _CipSecEndPtHistRemoteType_Type()
)
cipSecEndPtHistRemoteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecEndPtHistRemoteType.setStatus("current")
_CipSecEndPtHistRemoteAddr1_Type = IPSIpAddress
_CipSecEndPtHistRemoteAddr1_Object = MibTableColumn
cipSecEndPtHistRemoteAddr1 = _CipSecEndPtHistRemoteAddr1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 4, 3, 2, 1, 12),
    _CipSecEndPtHistRemoteAddr1_Type()
)
cipSecEndPtHistRemoteAddr1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecEndPtHistRemoteAddr1.setStatus("current")
_CipSecEndPtHistRemoteAddr2_Type = IPSIpAddress
_CipSecEndPtHistRemoteAddr2_Object = MibTableColumn
cipSecEndPtHistRemoteAddr2 = _CipSecEndPtHistRemoteAddr2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 4, 3, 2, 1, 13),
    _CipSecEndPtHistRemoteAddr2_Type()
)
cipSecEndPtHistRemoteAddr2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecEndPtHistRemoteAddr2.setStatus("current")


class _CipSecEndPtHistRemoteProtocol_Type(Integer32):
    """Custom type cipSecEndPtHistRemoteProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CipSecEndPtHistRemoteProtocol_Type.__name__ = "Integer32"
_CipSecEndPtHistRemoteProtocol_Object = MibTableColumn
cipSecEndPtHistRemoteProtocol = _CipSecEndPtHistRemoteProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 4, 3, 2, 1, 14),
    _CipSecEndPtHistRemoteProtocol_Type()
)
cipSecEndPtHistRemoteProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecEndPtHistRemoteProtocol.setStatus("current")


class _CipSecEndPtHistRemotePort_Type(Integer32):
    """Custom type cipSecEndPtHistRemotePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CipSecEndPtHistRemotePort_Type.__name__ = "Integer32"
_CipSecEndPtHistRemotePort_Object = MibTableColumn
cipSecEndPtHistRemotePort = _CipSecEndPtHistRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 4, 3, 2, 1, 15),
    _CipSecEndPtHistRemotePort_Type()
)
cipSecEndPtHistRemotePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecEndPtHistRemotePort.setStatus("current")
_CipSecFailures_ObjectIdentity = ObjectIdentity
cipSecFailures = _CipSecFailures_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 5)
)
_CipSecFailGlobal_ObjectIdentity = ObjectIdentity
cipSecFailGlobal = _CipSecFailGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 5, 1)
)
_CipSecFailGlobalCntl_ObjectIdentity = ObjectIdentity
cipSecFailGlobalCntl = _CipSecFailGlobalCntl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 5, 1, 1)
)


class _CipSecFailTableSize_Type(Integer32):
    """Custom type cipSecFailTableSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CipSecFailTableSize_Type.__name__ = "Integer32"
_CipSecFailTableSize_Object = MibScalar
cipSecFailTableSize = _CipSecFailTableSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 5, 1, 1, 1),
    _CipSecFailTableSize_Type()
)
cipSecFailTableSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cipSecFailTableSize.setStatus("current")
_CipSecFailPhaseOne_ObjectIdentity = ObjectIdentity
cipSecFailPhaseOne = _CipSecFailPhaseOne_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 5, 2)
)
_CikeFailTable_Object = MibTable
cikeFailTable = _CikeFailTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 5, 2, 1)
)
if mibBuilder.loadTexts:
    cikeFailTable.setStatus("current")
_CikeFailEntry_Object = MibTableRow
cikeFailEntry = _CikeFailEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 5, 2, 1, 1)
)
cikeFailEntry.setIndexNames(
    (0, "CISCO-IPSEC-FLOW-MONITOR-MIB", "cikeFailIndex"),
)
if mibBuilder.loadTexts:
    cikeFailEntry.setStatus("current")


class _CikeFailIndex_Type(Integer32):
    """Custom type cikeFailIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CikeFailIndex_Type.__name__ = "Integer32"
_CikeFailIndex_Object = MibTableColumn
cikeFailIndex = _CikeFailIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 5, 2, 1, 1, 1),
    _CikeFailIndex_Type()
)
cikeFailIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cikeFailIndex.setStatus("current")


class _CikeFailReason_Type(Integer32):
    """Custom type cikeFailReason based on Integer32"""
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
              17)
        )
    )
    namedValues = NamedValues(
        *(("authFailure", 5),
          ("crlFailure", 14),
          ("encryptFailure", 7),
          ("hashValidation", 6),
          ("internalError", 8),
          ("localCertExpired", 13),
          ("localFailure", 4),
          ("nonExistentSa", 16),
          ("operRequest", 17),
          ("other", 1),
          ("peerCertNotValid", 12),
          ("peerCertUnavailable", 11),
          ("peerDelRequest", 2),
          ("peerEncodingError", 15),
          ("peerLost", 3),
          ("proposalFailure", 10),
          ("sysCapExceeded", 9))
    )


_CikeFailReason_Type.__name__ = "Integer32"
_CikeFailReason_Object = MibTableColumn
cikeFailReason = _CikeFailReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 5, 2, 1, 1, 2),
    _CikeFailReason_Type()
)
cikeFailReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikeFailReason.setStatus("current")
_CikeFailTime_Type = TimeStamp
_CikeFailTime_Object = MibTableColumn
cikeFailTime = _CikeFailTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 5, 2, 1, 1, 3),
    _CikeFailTime_Type()
)
cikeFailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikeFailTime.setStatus("current")
_CikeFailLocalType_Type = IkePeerType
_CikeFailLocalType_Object = MibTableColumn
cikeFailLocalType = _CikeFailLocalType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 5, 2, 1, 1, 4),
    _CikeFailLocalType_Type()
)
cikeFailLocalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikeFailLocalType.setStatus("current")
_CikeFailLocalValue_Type = DisplayString
_CikeFailLocalValue_Object = MibTableColumn
cikeFailLocalValue = _CikeFailLocalValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 5, 2, 1, 1, 5),
    _CikeFailLocalValue_Type()
)
cikeFailLocalValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikeFailLocalValue.setStatus("current")
_CikeFailRemoteType_Type = IkePeerType
_CikeFailRemoteType_Object = MibTableColumn
cikeFailRemoteType = _CikeFailRemoteType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 5, 2, 1, 1, 6),
    _CikeFailRemoteType_Type()
)
cikeFailRemoteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikeFailRemoteType.setStatus("current")
_CikeFailRemoteValue_Type = DisplayString
_CikeFailRemoteValue_Object = MibTableColumn
cikeFailRemoteValue = _CikeFailRemoteValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 5, 2, 1, 1, 7),
    _CikeFailRemoteValue_Type()
)
cikeFailRemoteValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikeFailRemoteValue.setStatus("current")
_CikeFailLocalAddr_Type = IPSIpAddress
_CikeFailLocalAddr_Object = MibTableColumn
cikeFailLocalAddr = _CikeFailLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 5, 2, 1, 1, 8),
    _CikeFailLocalAddr_Type()
)
cikeFailLocalAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikeFailLocalAddr.setStatus("current")
_CikeFailRemoteAddr_Type = IPSIpAddress
_CikeFailRemoteAddr_Object = MibTableColumn
cikeFailRemoteAddr = _CikeFailRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 5, 2, 1, 1, 9),
    _CikeFailRemoteAddr_Type()
)
cikeFailRemoteAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cikeFailRemoteAddr.setStatus("current")
_CipSecFailPhaseTwo_ObjectIdentity = ObjectIdentity
cipSecFailPhaseTwo = _CipSecFailPhaseTwo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 5, 3)
)
_CipSecFailTable_Object = MibTable
cipSecFailTable = _CipSecFailTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 5, 3, 1)
)
if mibBuilder.loadTexts:
    cipSecFailTable.setStatus("current")
_CipSecFailEntry_Object = MibTableRow
cipSecFailEntry = _CipSecFailEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 5, 3, 1, 1)
)
cipSecFailEntry.setIndexNames(
    (0, "CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecFailIndex"),
)
if mibBuilder.loadTexts:
    cipSecFailEntry.setStatus("current")


class _CipSecFailIndex_Type(Integer32):
    """Custom type cipSecFailIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CipSecFailIndex_Type.__name__ = "Integer32"
_CipSecFailIndex_Object = MibTableColumn
cipSecFailIndex = _CipSecFailIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 5, 3, 1, 1, 1),
    _CipSecFailIndex_Type()
)
cipSecFailIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cipSecFailIndex.setStatus("current")


class _CipSecFailReason_Type(Integer32):
    """Custom type cipSecFailReason based on Integer32"""
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


_CipSecFailReason_Type.__name__ = "Integer32"
_CipSecFailReason_Object = MibTableColumn
cipSecFailReason = _CipSecFailReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 5, 3, 1, 1, 2),
    _CipSecFailReason_Type()
)
cipSecFailReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecFailReason.setStatus("current")
_CipSecFailTime_Type = TimeStamp
_CipSecFailTime_Object = MibTableColumn
cipSecFailTime = _CipSecFailTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 5, 3, 1, 1, 3),
    _CipSecFailTime_Type()
)
cipSecFailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecFailTime.setStatus("current")


class _CipSecFailTunnelIndex_Type(Integer32):
    """Custom type cipSecFailTunnelIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CipSecFailTunnelIndex_Type.__name__ = "Integer32"
_CipSecFailTunnelIndex_Object = MibTableColumn
cipSecFailTunnelIndex = _CipSecFailTunnelIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 5, 3, 1, 1, 4),
    _CipSecFailTunnelIndex_Type()
)
cipSecFailTunnelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecFailTunnelIndex.setStatus("current")


class _CipSecFailSaSpi_Type(Integer32):
    """Custom type cipSecFailSaSpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CipSecFailSaSpi_Type.__name__ = "Integer32"
_CipSecFailSaSpi_Object = MibTableColumn
cipSecFailSaSpi = _CipSecFailSaSpi_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 5, 3, 1, 1, 5),
    _CipSecFailSaSpi_Type()
)
cipSecFailSaSpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecFailSaSpi.setStatus("current")
_CipSecFailPktSrcAddr_Type = IPSIpAddress
_CipSecFailPktSrcAddr_Object = MibTableColumn
cipSecFailPktSrcAddr = _CipSecFailPktSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 5, 3, 1, 1, 6),
    _CipSecFailPktSrcAddr_Type()
)
cipSecFailPktSrcAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecFailPktSrcAddr.setStatus("current")
_CipSecFailPktDstAddr_Type = IPSIpAddress
_CipSecFailPktDstAddr_Object = MibTableColumn
cipSecFailPktDstAddr = _CipSecFailPktDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 5, 3, 1, 1, 7),
    _CipSecFailPktDstAddr_Type()
)
cipSecFailPktDstAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipSecFailPktDstAddr.setStatus("current")
_CipSecTrapCntl_ObjectIdentity = ObjectIdentity
cipSecTrapCntl = _CipSecTrapCntl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 6)
)


class _CipSecTrapCntlIkeTunnelStart_Type(TrapStatus):
    """Custom type cipSecTrapCntlIkeTunnelStart based on TrapStatus"""


_CipSecTrapCntlIkeTunnelStart_Object = MibScalar
cipSecTrapCntlIkeTunnelStart = _CipSecTrapCntlIkeTunnelStart_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 6, 1),
    _CipSecTrapCntlIkeTunnelStart_Type()
)
cipSecTrapCntlIkeTunnelStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cipSecTrapCntlIkeTunnelStart.setStatus("current")


class _CipSecTrapCntlIkeTunnelStop_Type(TrapStatus):
    """Custom type cipSecTrapCntlIkeTunnelStop based on TrapStatus"""


_CipSecTrapCntlIkeTunnelStop_Object = MibScalar
cipSecTrapCntlIkeTunnelStop = _CipSecTrapCntlIkeTunnelStop_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 6, 2),
    _CipSecTrapCntlIkeTunnelStop_Type()
)
cipSecTrapCntlIkeTunnelStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cipSecTrapCntlIkeTunnelStop.setStatus("current")


class _CipSecTrapCntlIkeSysFailure_Type(TrapStatus):
    """Custom type cipSecTrapCntlIkeSysFailure based on TrapStatus"""


_CipSecTrapCntlIkeSysFailure_Object = MibScalar
cipSecTrapCntlIkeSysFailure = _CipSecTrapCntlIkeSysFailure_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 6, 3),
    _CipSecTrapCntlIkeSysFailure_Type()
)
cipSecTrapCntlIkeSysFailure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cipSecTrapCntlIkeSysFailure.setStatus("current")


class _CipSecTrapCntlIkeCertCrlFailure_Type(TrapStatus):
    """Custom type cipSecTrapCntlIkeCertCrlFailure based on TrapStatus"""


_CipSecTrapCntlIkeCertCrlFailure_Object = MibScalar
cipSecTrapCntlIkeCertCrlFailure = _CipSecTrapCntlIkeCertCrlFailure_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 6, 4),
    _CipSecTrapCntlIkeCertCrlFailure_Type()
)
cipSecTrapCntlIkeCertCrlFailure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cipSecTrapCntlIkeCertCrlFailure.setStatus("current")


class _CipSecTrapCntlIkeProtocolFail_Type(TrapStatus):
    """Custom type cipSecTrapCntlIkeProtocolFail based on TrapStatus"""


_CipSecTrapCntlIkeProtocolFail_Object = MibScalar
cipSecTrapCntlIkeProtocolFail = _CipSecTrapCntlIkeProtocolFail_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 6, 5),
    _CipSecTrapCntlIkeProtocolFail_Type()
)
cipSecTrapCntlIkeProtocolFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cipSecTrapCntlIkeProtocolFail.setStatus("current")


class _CipSecTrapCntlIkeNoSa_Type(TrapStatus):
    """Custom type cipSecTrapCntlIkeNoSa based on TrapStatus"""


_CipSecTrapCntlIkeNoSa_Object = MibScalar
cipSecTrapCntlIkeNoSa = _CipSecTrapCntlIkeNoSa_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 6, 6),
    _CipSecTrapCntlIkeNoSa_Type()
)
cipSecTrapCntlIkeNoSa.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cipSecTrapCntlIkeNoSa.setStatus("current")


class _CipSecTrapCntlIpSecTunnelStart_Type(TrapStatus):
    """Custom type cipSecTrapCntlIpSecTunnelStart based on TrapStatus"""


_CipSecTrapCntlIpSecTunnelStart_Object = MibScalar
cipSecTrapCntlIpSecTunnelStart = _CipSecTrapCntlIpSecTunnelStart_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 6, 7),
    _CipSecTrapCntlIpSecTunnelStart_Type()
)
cipSecTrapCntlIpSecTunnelStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cipSecTrapCntlIpSecTunnelStart.setStatus("current")


class _CipSecTrapCntlIpSecTunnelStop_Type(TrapStatus):
    """Custom type cipSecTrapCntlIpSecTunnelStop based on TrapStatus"""


_CipSecTrapCntlIpSecTunnelStop_Object = MibScalar
cipSecTrapCntlIpSecTunnelStop = _CipSecTrapCntlIpSecTunnelStop_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 6, 8),
    _CipSecTrapCntlIpSecTunnelStop_Type()
)
cipSecTrapCntlIpSecTunnelStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cipSecTrapCntlIpSecTunnelStop.setStatus("current")


class _CipSecTrapCntlIpSecSysFailure_Type(TrapStatus):
    """Custom type cipSecTrapCntlIpSecSysFailure based on TrapStatus"""


_CipSecTrapCntlIpSecSysFailure_Object = MibScalar
cipSecTrapCntlIpSecSysFailure = _CipSecTrapCntlIpSecSysFailure_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 6, 9),
    _CipSecTrapCntlIpSecSysFailure_Type()
)
cipSecTrapCntlIpSecSysFailure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cipSecTrapCntlIpSecSysFailure.setStatus("current")


class _CipSecTrapCntlIpSecSetUpFailure_Type(TrapStatus):
    """Custom type cipSecTrapCntlIpSecSetUpFailure based on TrapStatus"""


_CipSecTrapCntlIpSecSetUpFailure_Object = MibScalar
cipSecTrapCntlIpSecSetUpFailure = _CipSecTrapCntlIpSecSetUpFailure_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 6, 10),
    _CipSecTrapCntlIpSecSetUpFailure_Type()
)
cipSecTrapCntlIpSecSetUpFailure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cipSecTrapCntlIpSecSetUpFailure.setStatus("current")


class _CipSecTrapCntlIpSecEarlyTunTerm_Type(TrapStatus):
    """Custom type cipSecTrapCntlIpSecEarlyTunTerm based on TrapStatus"""


_CipSecTrapCntlIpSecEarlyTunTerm_Object = MibScalar
cipSecTrapCntlIpSecEarlyTunTerm = _CipSecTrapCntlIpSecEarlyTunTerm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 6, 11),
    _CipSecTrapCntlIpSecEarlyTunTerm_Type()
)
cipSecTrapCntlIpSecEarlyTunTerm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cipSecTrapCntlIpSecEarlyTunTerm.setStatus("current")


class _CipSecTrapCntlIpSecProtocolFail_Type(TrapStatus):
    """Custom type cipSecTrapCntlIpSecProtocolFail based on TrapStatus"""


_CipSecTrapCntlIpSecProtocolFail_Object = MibScalar
cipSecTrapCntlIpSecProtocolFail = _CipSecTrapCntlIpSecProtocolFail_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 6, 12),
    _CipSecTrapCntlIpSecProtocolFail_Type()
)
cipSecTrapCntlIpSecProtocolFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cipSecTrapCntlIpSecProtocolFail.setStatus("current")


class _CipSecTrapCntlIpSecNoSa_Type(TrapStatus):
    """Custom type cipSecTrapCntlIpSecNoSa based on TrapStatus"""


_CipSecTrapCntlIpSecNoSa_Object = MibScalar
cipSecTrapCntlIpSecNoSa = _CipSecTrapCntlIpSecNoSa_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 1, 6, 13),
    _CipSecTrapCntlIpSecNoSa_Type()
)
cipSecTrapCntlIpSecNoSa.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cipSecTrapCntlIpSecNoSa.setStatus("current")
_CipSecMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
cipSecMIBNotificationPrefix = _CipSecMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 2)
)
_CipSecMIBNotifications_ObjectIdentity = ObjectIdentity
cipSecMIBNotifications = _CipSecMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 2, 0)
)
_CipSecMIBConformance_ObjectIdentity = ObjectIdentity
cipSecMIBConformance = _CipSecMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 3)
)
_CipSecMIBGroups_ObjectIdentity = ObjectIdentity
cipSecMIBGroups = _CipSecMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 3, 1)
)
_CipSecMIBCompliances_ObjectIdentity = ObjectIdentity
cipSecMIBCompliances = _CipSecMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 3, 2)
)

# Managed Objects groups

cipSecLevelsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 3, 1, 1)
)
cipSecLevelsGroup.setObjects(
    ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecMibLevel")
)
if mibBuilder.loadTexts:
    cipSecLevelsGroup.setStatus("current")

cipSecPhaseOneGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 3, 1, 2)
)
cipSecPhaseOneGroup.setObjects(
      *(("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikeGlobalActiveTunnels"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikeGlobalPreviousTunnels"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikeGlobalInOctets"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikeGlobalInPkts"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikeGlobalInDropPkts"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikeGlobalInNotifys"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikeGlobalInP2Exchgs"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikeGlobalInP2ExchgInvalids"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikeGlobalInP2ExchgRejects"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikeGlobalInP2SaDelRequests"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikeGlobalOutOctets"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikeGlobalOutPkts"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikeGlobalOutDropPkts"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikeGlobalOutNotifys"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikeGlobalOutP2Exchgs"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikeGlobalOutP2ExchgInvalids"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikeGlobalOutP2ExchgRejects"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikeGlobalOutP2SaDelRequests"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikeGlobalInitTunnels"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikeGlobalInitTunnelFails"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikeGlobalRespTunnelFails"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikeGlobalSysCapFails"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikeGlobalAuthFails"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikeGlobalDecryptFails"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikeGlobalHashValidFails"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikeGlobalNoSaFails"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikePeerLocalAddr"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikePeerRemoteAddr"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikePeerActiveTime"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikePeerActiveTunnelIndex"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikeTunLocalType"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikeTunLocalValue"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikeTunLocalAddr"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikeTunLocalName"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikeTunRemoteType"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikeTunRemoteValue"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikeTunRemoteAddr"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikeTunRemoteName"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikeTunNegoMode"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikeTunDiffHellmanGrp"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikeTunEncryptAlgo"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikeTunHashAlgo"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikeTunAuthMethod"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikeTunLifeTime"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikeTunActiveTime"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikeTunSaRefreshThreshold"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikeTunTotalRefreshes"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikeTunInOctets"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikeTunInPkts"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikeTunInDropPkts"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikeTunInNotifys"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikeTunInP2Exchgs"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikeTunInP2ExchgInvalids"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikeTunInP2ExchgRejects"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikeTunInP2SaDelRequests"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikeTunOutOctets"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikeTunOutPkts"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikeTunOutDropPkts"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikeTunOutNotifys"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikeTunOutP2Exchgs"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikeTunOutP2ExchgInvalids"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikeTunOutP2ExchgRejects"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikeTunOutP2SaDelRequests"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikeTunStatus"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikePeerCorrIpSecTunIndex"))
)
if mibBuilder.loadTexts:
    cipSecPhaseOneGroup.setStatus("current")

cipSecPhaseTwoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 3, 1, 3)
)
cipSecPhaseTwoGroup.setObjects(
      *(("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecGlobalActiveTunnels"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecGlobalPreviousTunnels"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecGlobalInOctets"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecGlobalHcInOctets"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecGlobalInOctWraps"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecGlobalInDecompOctets"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecGlobalHcInDecompOctets"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecGlobalInDecompOctWraps"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecGlobalInPkts"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecGlobalInDrops"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecGlobalInReplayDrops"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecGlobalInAuths"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecGlobalInAuthFails"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecGlobalInDecrypts"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecGlobalInDecryptFails"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecGlobalOutOctets"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecGlobalHcOutOctets"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecGlobalOutOctWraps"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecGlobalOutUncompOctets"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecGlobalHcOutUncompOctets"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecGlobalOutUncompOctWraps"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecGlobalOutPkts"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecGlobalOutDrops"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecGlobalOutAuths"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecGlobalOutAuthFails"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecGlobalOutEncrypts"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecGlobalOutEncryptFails"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecGlobalProtocolUseFails"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecGlobalNoSaFails"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecGlobalSysCapFails"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecTunIkeTunnelIndex"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecTunIkeTunnelAlive"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecTunLocalAddr"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecTunRemoteAddr"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecTunKeyType"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecTunEncapMode"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecTunLifeSize"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecTunLifeTime"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecTunActiveTime"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecTunSaLifeSizeThreshold"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecTunSaLifeTimeThreshold"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecTunTotalRefreshes"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecTunExpiredSaInstances"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecTunCurrentSaInstances"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecTunInSaDiffHellmanGrp"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecTunInSaEncryptAlgo"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecTunInSaAhAuthAlgo"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecTunInSaEspAuthAlgo"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecTunInSaDecompAlgo"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecTunOutSaDiffHellmanGrp"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecTunOutSaEncryptAlgo"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecTunOutSaAhAuthAlgo"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecTunOutSaEspAuthAlgo"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecTunOutSaCompAlgo"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecTunInOctets"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecTunHcInOctets"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecTunInOctWraps"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecTunInDecompOctets"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecTunHcInDecompOctets"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecTunInDecompOctWraps"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecTunInPkts"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecTunInDropPkts"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecTunInReplayDropPkts"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecTunInAuths"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecTunInAuthFails"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecTunInDecrypts"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecTunInDecryptFails"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecTunOutOctets"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecTunHcOutOctets"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecTunOutOctWraps"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecTunOutUncompOctets"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecTunHcOutUncompOctets"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecTunOutUncompOctWraps"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecTunOutPkts"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecTunOutDropPkts"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecTunOutAuths"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecTunOutAuthFails"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecTunOutEncrypts"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecTunOutEncryptFails"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecTunStatus"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecEndPtLocalName"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecEndPtLocalType"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecEndPtLocalAddr1"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecEndPtLocalAddr2"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecEndPtLocalProtocol"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecEndPtLocalPort"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecEndPtRemoteName"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecEndPtRemoteType"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecEndPtRemoteAddr1"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecEndPtRemoteAddr2"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecEndPtRemoteProtocol"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecEndPtRemotePort"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecSpiDirection"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecSpiValue"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecSpiProtocol"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecSpiStatus"))
)
if mibBuilder.loadTexts:
    cipSecPhaseTwoGroup.setStatus("current")

cipSecHistoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 3, 1, 4)
)
cipSecHistoryGroup.setObjects(
      *(("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecHistTableSize"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecHistCheckPoint"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikeTunHistTermReason"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikeTunHistActiveIndex"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikeTunHistPeerLocalType"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikeTunHistPeerLocalValue"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikeTunHistPeerIntIndex"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikeTunHistPeerRemoteType"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikeTunHistPeerRemoteValue"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikeTunHistLocalAddr"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikeTunHistLocalName"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikeTunHistRemoteAddr"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikeTunHistRemoteName"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikeTunHistNegoMode"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikeTunHistDiffHellmanGrp"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikeTunHistEncryptAlgo"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikeTunHistHashAlgo"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikeTunHistAuthMethod"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikeTunHistLifeTime"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikeTunHistStartTime"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikeTunHistActiveTime"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikeTunHistTotalRefreshes"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikeTunHistTotalSas"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikeTunHistInOctets"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikeTunHistInPkts"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikeTunHistInDropPkts"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikeTunHistInNotifys"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikeTunHistInP2Exchgs"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikeTunHistInP2ExchgInvalids"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikeTunHistInP2ExchgRejects"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikeTunHistInP2SaDelRequests"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikeTunHistOutOctets"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikeTunHistOutPkts"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikeTunHistOutDropPkts"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikeTunHistOutNotifys"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikeTunHistOutP2Exchgs"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikeTunHistOutP2ExchgInvalids"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikeTunHistOutP2ExchgRejects"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikeTunHistOutP2SaDelRequests"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecTunHistTermReason"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecTunHistActiveIndex"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecTunHistIkeTunnelIndex"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecTunHistLocalAddr"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecTunHistRemoteAddr"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecTunHistKeyType"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecTunHistEncapMode"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecTunHistLifeSize"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecTunHistLifeTime"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecTunHistStartTime"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecTunHistActiveTime"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecTunHistTotalRefreshes"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecTunHistTotalSas"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecTunHistInSaDiffHellmanGrp"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecTunHistInSaEncryptAlgo"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecTunHistInSaAhAuthAlgo"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecTunHistInSaEspAuthAlgo"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecTunHistInSaDecompAlgo"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecTunHistOutSaDiffHellmanGrp"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecTunHistOutSaEncryptAlgo"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecTunHistOutSaAhAuthAlgo"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecTunHistOutSaEspAuthAlgo"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecTunHistOutSaCompAlgo"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecTunHistInOctets"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecTunHistHcInOctets"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecTunHistInOctWraps"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecTunHistInDecompOctets"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecTunHistHcInDecompOctets"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecTunHistInDecompOctWraps"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecTunHistInPkts"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecTunHistInDropPkts"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecTunHistInReplayDropPkts"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecTunHistInAuths"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecTunHistInAuthFails"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecTunHistInDecrypts"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecTunHistInDecryptFails"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecTunHistOutOctets"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecTunHistHcOutOctets"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecTunHistOutOctWraps"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecTunHistOutUncompOctets"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecTunHistHcOutUncompOctets"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecTunHistOutUncompOctWraps"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecTunHistOutPkts"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecTunHistOutDropPkts"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecTunHistOutAuths"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecTunHistOutAuthFails"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecTunHistOutEncrypts"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecTunHistOutEncryptFails"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecEndPtHistTunIndex"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecEndPtHistActiveIndex"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecEndPtHistLocalName"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecEndPtHistLocalType"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecEndPtHistLocalAddr1"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecEndPtHistLocalAddr2"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecEndPtHistLocalProtocol"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecEndPtHistLocalPort"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecEndPtHistRemoteName"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecEndPtHistRemoteType"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecEndPtHistRemoteAddr1"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecEndPtHistRemoteAddr2"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecEndPtHistRemoteProtocol"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecEndPtHistRemotePort"))
)
if mibBuilder.loadTexts:
    cipSecHistoryGroup.setStatus("current")

cipSecFailuresGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 3, 1, 5)
)
cipSecFailuresGroup.setObjects(
      *(("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecFailTableSize"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikeFailReason"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikeFailTime"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikeFailLocalType"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikeFailLocalValue"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikeFailRemoteType"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikeFailRemoteValue"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikeFailLocalAddr"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikeFailRemoteAddr"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecFailReason"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecFailTime"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecFailTunnelIndex"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecFailSaSpi"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecFailPktSrcAddr"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecFailPktDstAddr"))
)
if mibBuilder.loadTexts:
    cipSecFailuresGroup.setStatus("current")

cipSecTrapCntlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 3, 1, 6)
)
cipSecTrapCntlGroup.setObjects(
      *(("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecTrapCntlIkeTunnelStart"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecTrapCntlIkeTunnelStop"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecTrapCntlIkeSysFailure"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecTrapCntlIkeCertCrlFailure"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecTrapCntlIkeProtocolFail"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecTrapCntlIkeNoSa"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecTrapCntlIpSecTunnelStart"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecTrapCntlIpSecTunnelStop"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecTrapCntlIpSecSysFailure"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecTrapCntlIpSecSetUpFailure"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecTrapCntlIpSecEarlyTunTerm"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecTrapCntlIpSecProtocolFail"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecTrapCntlIpSecNoSa"))
)
if mibBuilder.loadTexts:
    cipSecTrapCntlGroup.setStatus("current")

cipSecGWStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 3, 1, 8)
)
cipSecGWStatsGroup.setObjects(
      *(("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikePhase1GWActiveTunnels"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikePhase1GWPreviousTunnels"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikePhase1GWInOctets"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikePhase1GWInPkts"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikePhase1GWInDropPkts"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikePhase1GWInNotifys"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikePhase1GWInP2Exchgs"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikePhase1GWInP2ExchgInvalids"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikePhase1GWInP2ExchgRejects"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikePhase1GWInP2SaDelRequests"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikePhase1GWOutOctets"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikePhase1GWOutPkts"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikePhase1GWOutDropPkts"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikePhase1GWOutNotifys"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikePhase1GWOutP2Exchgs"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikePhase1GWOutP2ExchgInvalids"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikePhase1GWOutP2ExchgRejects"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikePhase1GWOutP2SaDelRequests"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikePhase1GWInitTunnels"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikePhase1GWInitTunnelFails"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikePhase1GWRespTunnelFails"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikePhase1GWSysCapFails"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikePhase1GWAuthFails"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikePhase1GWDecryptFails"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikePhase1GWHashValidFails"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikePhase1GWNoSaFails"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecPhase2GWActiveTunnels"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecPhase2GWPreviousTunnels"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecPhase2GWInOctets"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecPhase2GWInOctWraps"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecPhase2GWInDecompOctets"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecPhase2GWInDecompOctWraps"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecPhase2GWInPkts"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecPhase2GWInDrops"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecPhase2GWInReplayDrops"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecPhase2GWInAuths"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecPhase2GWInAuthFails"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecPhase2GWInDecrypts"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecPhase2GWInDecryptFails"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecPhase2GWOutOctets"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecPhase2GWOutOctWraps"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecPhase2GWOutUncompOctets"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecPhase2GWOutUncompOctWraps"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecPhase2GWOutPkts"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecPhase2GWOutDrops"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecPhase2GWOutAuths"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecPhase2GWOutAuthFails"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecPhase2GWOutEncrypts"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecPhase2GWOutEncryptFails"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecPhase2GWProtocolUseFails"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecPhase2GWNoSaFails"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecPhase2GWSysCapFails"))
)
if mibBuilder.loadTexts:
    cipSecGWStatsGroup.setStatus("current")


# Notification objects

cikeTunnelStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 2, 0, 1)
)
cikeTunnelStart.setObjects(
      *(("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikePeerLocalAddr"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikePeerRemoteAddr"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikeTunLifeTime"))
)
if mibBuilder.loadTexts:
    cikeTunnelStart.setStatus(
        "current"
    )

cikeTunnelStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 2, 0, 2)
)
cikeTunnelStop.setObjects(
      *(("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikePeerLocalAddr"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikePeerRemoteAddr"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikeTunActiveTime"))
)
if mibBuilder.loadTexts:
    cikeTunnelStop.setStatus(
        "current"
    )

cikeSysFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 2, 0, 3)
)
cikeSysFailure.setObjects(
      *(("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikePeerLocalAddr"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikePeerRemoteAddr"))
)
if mibBuilder.loadTexts:
    cikeSysFailure.setStatus(
        "current"
    )

cikeCertCrlFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 2, 0, 4)
)
cikeCertCrlFailure.setObjects(
      *(("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikePeerLocalAddr"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikePeerRemoteAddr"))
)
if mibBuilder.loadTexts:
    cikeCertCrlFailure.setStatus(
        "current"
    )

cikeProtocolFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 2, 0, 5)
)
cikeProtocolFailure.setObjects(
      *(("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikePeerLocalAddr"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikePeerRemoteAddr"))
)
if mibBuilder.loadTexts:
    cikeProtocolFailure.setStatus(
        "current"
    )

cikeNoSa = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 2, 0, 6)
)
cikeNoSa.setObjects(
      *(("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikePeerLocalAddr"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikePeerRemoteAddr"))
)
if mibBuilder.loadTexts:
    cikeNoSa.setStatus(
        "current"
    )

cipSecTunnelStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 2, 0, 7)
)
cipSecTunnelStart.setObjects(
      *(("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecTunLifeTime"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecTunLifeSize"))
)
if mibBuilder.loadTexts:
    cipSecTunnelStart.setStatus(
        "current"
    )

cipSecTunnelStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 2, 0, 8)
)
cipSecTunnelStop.setObjects(
    ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecTunActiveTime")
)
if mibBuilder.loadTexts:
    cipSecTunnelStop.setStatus(
        "current"
    )

cipSecSysFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 2, 0, 9)
)
cipSecSysFailure.setObjects(
      *(("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikePeerLocalAddr"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikePeerRemoteAddr"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecTunActiveTime"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecSpiProtocol"))
)
if mibBuilder.loadTexts:
    cipSecSysFailure.setStatus(
        "current"
    )

cipSecSetUpFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 2, 0, 10)
)
cipSecSetUpFailure.setObjects(
      *(("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikePeerLocalAddr"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikePeerRemoteAddr"))
)
if mibBuilder.loadTexts:
    cipSecSetUpFailure.setStatus(
        "current"
    )

cipSecEarlyTunTerm = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 2, 0, 11)
)
cipSecEarlyTunTerm.setObjects(
      *(("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecTunActiveTime"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecSpiProtocol"))
)
if mibBuilder.loadTexts:
    cipSecEarlyTunTerm.setStatus(
        "current"
    )

cipSecProtocolFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 2, 0, 12)
)
cipSecProtocolFailure.setObjects(
      *(("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecTunActiveTime"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecSpiProtocol"))
)
if mibBuilder.loadTexts:
    cipSecProtocolFailure.setStatus(
        "current"
    )

cipSecNoSa = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 2, 0, 13)
)
if mibBuilder.loadTexts:
    cipSecNoSa.setStatus(
        "current"
    )


# Notifications groups

cipSecNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 3, 1, 7)
)
cipSecNotificationGroup.setObjects(
      *(("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikeTunnelStart"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikeTunnelStop"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikeSysFailure"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikeCertCrlFailure"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikeProtocolFailure"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cikeNoSa"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecTunnelStart"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecTunnelStop"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecSysFailure"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecSetUpFailure"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecEarlyTunTerm"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecProtocolFailure"),
        ("CISCO-IPSEC-FLOW-MONITOR-MIB", "cipSecNoSa"))
)
if mibBuilder.loadTexts:
    cipSecNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

cipSecMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 3, 2, 1)
)
if mibBuilder.loadTexts:
    cipSecMIBCompliance.setStatus(
        "deprecated"
    )

cipSecMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 171, 3, 2, 2)
)
if mibBuilder.loadTexts:
    cipSecMIBComplianceRev1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-IPSEC-FLOW-MONITOR-MIB",
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
       "ciscoIpSecFlowMonitorMIB": ciscoIpSecFlowMonitorMIB,
       "cipSecMIBObjects": cipSecMIBObjects,
       "cipSecLevels": cipSecLevels,
       "cipSecMibLevel": cipSecMibLevel,
       "cipSecPhaseOne": cipSecPhaseOne,
       "cikeGlobalStats": cikeGlobalStats,
       "cikeGlobalActiveTunnels": cikeGlobalActiveTunnels,
       "cikeGlobalPreviousTunnels": cikeGlobalPreviousTunnels,
       "cikeGlobalInOctets": cikeGlobalInOctets,
       "cikeGlobalInPkts": cikeGlobalInPkts,
       "cikeGlobalInDropPkts": cikeGlobalInDropPkts,
       "cikeGlobalInNotifys": cikeGlobalInNotifys,
       "cikeGlobalInP2Exchgs": cikeGlobalInP2Exchgs,
       "cikeGlobalInP2ExchgInvalids": cikeGlobalInP2ExchgInvalids,
       "cikeGlobalInP2ExchgRejects": cikeGlobalInP2ExchgRejects,
       "cikeGlobalInP2SaDelRequests": cikeGlobalInP2SaDelRequests,
       "cikeGlobalOutOctets": cikeGlobalOutOctets,
       "cikeGlobalOutPkts": cikeGlobalOutPkts,
       "cikeGlobalOutDropPkts": cikeGlobalOutDropPkts,
       "cikeGlobalOutNotifys": cikeGlobalOutNotifys,
       "cikeGlobalOutP2Exchgs": cikeGlobalOutP2Exchgs,
       "cikeGlobalOutP2ExchgInvalids": cikeGlobalOutP2ExchgInvalids,
       "cikeGlobalOutP2ExchgRejects": cikeGlobalOutP2ExchgRejects,
       "cikeGlobalOutP2SaDelRequests": cikeGlobalOutP2SaDelRequests,
       "cikeGlobalInitTunnels": cikeGlobalInitTunnels,
       "cikeGlobalInitTunnelFails": cikeGlobalInitTunnelFails,
       "cikeGlobalRespTunnelFails": cikeGlobalRespTunnelFails,
       "cikeGlobalSysCapFails": cikeGlobalSysCapFails,
       "cikeGlobalAuthFails": cikeGlobalAuthFails,
       "cikeGlobalDecryptFails": cikeGlobalDecryptFails,
       "cikeGlobalHashValidFails": cikeGlobalHashValidFails,
       "cikeGlobalNoSaFails": cikeGlobalNoSaFails,
       "cikePeerTable": cikePeerTable,
       "cikePeerEntry": cikePeerEntry,
       "cikePeerLocalType": cikePeerLocalType,
       "cikePeerLocalValue": cikePeerLocalValue,
       "cikePeerRemoteType": cikePeerRemoteType,
       "cikePeerRemoteValue": cikePeerRemoteValue,
       "cikePeerIntIndex": cikePeerIntIndex,
       "cikePeerLocalAddr": cikePeerLocalAddr,
       "cikePeerRemoteAddr": cikePeerRemoteAddr,
       "cikePeerActiveTime": cikePeerActiveTime,
       "cikePeerActiveTunnelIndex": cikePeerActiveTunnelIndex,
       "cikeTunnelTable": cikeTunnelTable,
       "cikeTunnelEntry": cikeTunnelEntry,
       "cikeTunIndex": cikeTunIndex,
       "cikeTunLocalType": cikeTunLocalType,
       "cikeTunLocalValue": cikeTunLocalValue,
       "cikeTunLocalAddr": cikeTunLocalAddr,
       "cikeTunLocalName": cikeTunLocalName,
       "cikeTunRemoteType": cikeTunRemoteType,
       "cikeTunRemoteValue": cikeTunRemoteValue,
       "cikeTunRemoteAddr": cikeTunRemoteAddr,
       "cikeTunRemoteName": cikeTunRemoteName,
       "cikeTunNegoMode": cikeTunNegoMode,
       "cikeTunDiffHellmanGrp": cikeTunDiffHellmanGrp,
       "cikeTunEncryptAlgo": cikeTunEncryptAlgo,
       "cikeTunHashAlgo": cikeTunHashAlgo,
       "cikeTunAuthMethod": cikeTunAuthMethod,
       "cikeTunLifeTime": cikeTunLifeTime,
       "cikeTunActiveTime": cikeTunActiveTime,
       "cikeTunSaRefreshThreshold": cikeTunSaRefreshThreshold,
       "cikeTunTotalRefreshes": cikeTunTotalRefreshes,
       "cikeTunInOctets": cikeTunInOctets,
       "cikeTunInPkts": cikeTunInPkts,
       "cikeTunInDropPkts": cikeTunInDropPkts,
       "cikeTunInNotifys": cikeTunInNotifys,
       "cikeTunInP2Exchgs": cikeTunInP2Exchgs,
       "cikeTunInP2ExchgInvalids": cikeTunInP2ExchgInvalids,
       "cikeTunInP2ExchgRejects": cikeTunInP2ExchgRejects,
       "cikeTunInP2SaDelRequests": cikeTunInP2SaDelRequests,
       "cikeTunOutOctets": cikeTunOutOctets,
       "cikeTunOutPkts": cikeTunOutPkts,
       "cikeTunOutDropPkts": cikeTunOutDropPkts,
       "cikeTunOutNotifys": cikeTunOutNotifys,
       "cikeTunOutP2Exchgs": cikeTunOutP2Exchgs,
       "cikeTunOutP2ExchgInvalids": cikeTunOutP2ExchgInvalids,
       "cikeTunOutP2ExchgRejects": cikeTunOutP2ExchgRejects,
       "cikeTunOutP2SaDelRequests": cikeTunOutP2SaDelRequests,
       "cikeTunStatus": cikeTunStatus,
       "cikePeerCorrTable": cikePeerCorrTable,
       "cikePeerCorrEntry": cikePeerCorrEntry,
       "cikePeerCorrLocalType": cikePeerCorrLocalType,
       "cikePeerCorrLocalValue": cikePeerCorrLocalValue,
       "cikePeerCorrRemoteType": cikePeerCorrRemoteType,
       "cikePeerCorrRemoteValue": cikePeerCorrRemoteValue,
       "cikePeerCorrIntIndex": cikePeerCorrIntIndex,
       "cikePeerCorrSeqNum": cikePeerCorrSeqNum,
       "cikePeerCorrIpSecTunIndex": cikePeerCorrIpSecTunIndex,
       "cikePhase1GWStatsTable": cikePhase1GWStatsTable,
       "cikePhase1GWStatsEntry": cikePhase1GWStatsEntry,
       "cikePhase1GWActiveTunnels": cikePhase1GWActiveTunnels,
       "cikePhase1GWPreviousTunnels": cikePhase1GWPreviousTunnels,
       "cikePhase1GWInOctets": cikePhase1GWInOctets,
       "cikePhase1GWInPkts": cikePhase1GWInPkts,
       "cikePhase1GWInDropPkts": cikePhase1GWInDropPkts,
       "cikePhase1GWInNotifys": cikePhase1GWInNotifys,
       "cikePhase1GWInP2Exchgs": cikePhase1GWInP2Exchgs,
       "cikePhase1GWInP2ExchgInvalids": cikePhase1GWInP2ExchgInvalids,
       "cikePhase1GWInP2ExchgRejects": cikePhase1GWInP2ExchgRejects,
       "cikePhase1GWInP2SaDelRequests": cikePhase1GWInP2SaDelRequests,
       "cikePhase1GWOutOctets": cikePhase1GWOutOctets,
       "cikePhase1GWOutPkts": cikePhase1GWOutPkts,
       "cikePhase1GWOutDropPkts": cikePhase1GWOutDropPkts,
       "cikePhase1GWOutNotifys": cikePhase1GWOutNotifys,
       "cikePhase1GWOutP2Exchgs": cikePhase1GWOutP2Exchgs,
       "cikePhase1GWOutP2ExchgInvalids": cikePhase1GWOutP2ExchgInvalids,
       "cikePhase1GWOutP2ExchgRejects": cikePhase1GWOutP2ExchgRejects,
       "cikePhase1GWOutP2SaDelRequests": cikePhase1GWOutP2SaDelRequests,
       "cikePhase1GWInitTunnels": cikePhase1GWInitTunnels,
       "cikePhase1GWInitTunnelFails": cikePhase1GWInitTunnelFails,
       "cikePhase1GWRespTunnelFails": cikePhase1GWRespTunnelFails,
       "cikePhase1GWSysCapFails": cikePhase1GWSysCapFails,
       "cikePhase1GWAuthFails": cikePhase1GWAuthFails,
       "cikePhase1GWDecryptFails": cikePhase1GWDecryptFails,
       "cikePhase1GWHashValidFails": cikePhase1GWHashValidFails,
       "cikePhase1GWNoSaFails": cikePhase1GWNoSaFails,
       "cipSecPhaseTwo": cipSecPhaseTwo,
       "cipSecGlobalStats": cipSecGlobalStats,
       "cipSecGlobalActiveTunnels": cipSecGlobalActiveTunnels,
       "cipSecGlobalPreviousTunnels": cipSecGlobalPreviousTunnels,
       "cipSecGlobalInOctets": cipSecGlobalInOctets,
       "cipSecGlobalHcInOctets": cipSecGlobalHcInOctets,
       "cipSecGlobalInOctWraps": cipSecGlobalInOctWraps,
       "cipSecGlobalInDecompOctets": cipSecGlobalInDecompOctets,
       "cipSecGlobalHcInDecompOctets": cipSecGlobalHcInDecompOctets,
       "cipSecGlobalInDecompOctWraps": cipSecGlobalInDecompOctWraps,
       "cipSecGlobalInPkts": cipSecGlobalInPkts,
       "cipSecGlobalInDrops": cipSecGlobalInDrops,
       "cipSecGlobalInReplayDrops": cipSecGlobalInReplayDrops,
       "cipSecGlobalInAuths": cipSecGlobalInAuths,
       "cipSecGlobalInAuthFails": cipSecGlobalInAuthFails,
       "cipSecGlobalInDecrypts": cipSecGlobalInDecrypts,
       "cipSecGlobalInDecryptFails": cipSecGlobalInDecryptFails,
       "cipSecGlobalOutOctets": cipSecGlobalOutOctets,
       "cipSecGlobalHcOutOctets": cipSecGlobalHcOutOctets,
       "cipSecGlobalOutOctWraps": cipSecGlobalOutOctWraps,
       "cipSecGlobalOutUncompOctets": cipSecGlobalOutUncompOctets,
       "cipSecGlobalHcOutUncompOctets": cipSecGlobalHcOutUncompOctets,
       "cipSecGlobalOutUncompOctWraps": cipSecGlobalOutUncompOctWraps,
       "cipSecGlobalOutPkts": cipSecGlobalOutPkts,
       "cipSecGlobalOutDrops": cipSecGlobalOutDrops,
       "cipSecGlobalOutAuths": cipSecGlobalOutAuths,
       "cipSecGlobalOutAuthFails": cipSecGlobalOutAuthFails,
       "cipSecGlobalOutEncrypts": cipSecGlobalOutEncrypts,
       "cipSecGlobalOutEncryptFails": cipSecGlobalOutEncryptFails,
       "cipSecGlobalProtocolUseFails": cipSecGlobalProtocolUseFails,
       "cipSecGlobalNoSaFails": cipSecGlobalNoSaFails,
       "cipSecGlobalSysCapFails": cipSecGlobalSysCapFails,
       "cipSecTunnelTable": cipSecTunnelTable,
       "cipSecTunnelEntry": cipSecTunnelEntry,
       "cipSecTunIndex": cipSecTunIndex,
       "cipSecTunIkeTunnelIndex": cipSecTunIkeTunnelIndex,
       "cipSecTunIkeTunnelAlive": cipSecTunIkeTunnelAlive,
       "cipSecTunLocalAddr": cipSecTunLocalAddr,
       "cipSecTunRemoteAddr": cipSecTunRemoteAddr,
       "cipSecTunKeyType": cipSecTunKeyType,
       "cipSecTunEncapMode": cipSecTunEncapMode,
       "cipSecTunLifeSize": cipSecTunLifeSize,
       "cipSecTunLifeTime": cipSecTunLifeTime,
       "cipSecTunActiveTime": cipSecTunActiveTime,
       "cipSecTunSaLifeSizeThreshold": cipSecTunSaLifeSizeThreshold,
       "cipSecTunSaLifeTimeThreshold": cipSecTunSaLifeTimeThreshold,
       "cipSecTunTotalRefreshes": cipSecTunTotalRefreshes,
       "cipSecTunExpiredSaInstances": cipSecTunExpiredSaInstances,
       "cipSecTunCurrentSaInstances": cipSecTunCurrentSaInstances,
       "cipSecTunInSaDiffHellmanGrp": cipSecTunInSaDiffHellmanGrp,
       "cipSecTunInSaEncryptAlgo": cipSecTunInSaEncryptAlgo,
       "cipSecTunInSaAhAuthAlgo": cipSecTunInSaAhAuthAlgo,
       "cipSecTunInSaEspAuthAlgo": cipSecTunInSaEspAuthAlgo,
       "cipSecTunInSaDecompAlgo": cipSecTunInSaDecompAlgo,
       "cipSecTunOutSaDiffHellmanGrp": cipSecTunOutSaDiffHellmanGrp,
       "cipSecTunOutSaEncryptAlgo": cipSecTunOutSaEncryptAlgo,
       "cipSecTunOutSaAhAuthAlgo": cipSecTunOutSaAhAuthAlgo,
       "cipSecTunOutSaEspAuthAlgo": cipSecTunOutSaEspAuthAlgo,
       "cipSecTunOutSaCompAlgo": cipSecTunOutSaCompAlgo,
       "cipSecTunInOctets": cipSecTunInOctets,
       "cipSecTunHcInOctets": cipSecTunHcInOctets,
       "cipSecTunInOctWraps": cipSecTunInOctWraps,
       "cipSecTunInDecompOctets": cipSecTunInDecompOctets,
       "cipSecTunHcInDecompOctets": cipSecTunHcInDecompOctets,
       "cipSecTunInDecompOctWraps": cipSecTunInDecompOctWraps,
       "cipSecTunInPkts": cipSecTunInPkts,
       "cipSecTunInDropPkts": cipSecTunInDropPkts,
       "cipSecTunInReplayDropPkts": cipSecTunInReplayDropPkts,
       "cipSecTunInAuths": cipSecTunInAuths,
       "cipSecTunInAuthFails": cipSecTunInAuthFails,
       "cipSecTunInDecrypts": cipSecTunInDecrypts,
       "cipSecTunInDecryptFails": cipSecTunInDecryptFails,
       "cipSecTunOutOctets": cipSecTunOutOctets,
       "cipSecTunHcOutOctets": cipSecTunHcOutOctets,
       "cipSecTunOutOctWraps": cipSecTunOutOctWraps,
       "cipSecTunOutUncompOctets": cipSecTunOutUncompOctets,
       "cipSecTunHcOutUncompOctets": cipSecTunHcOutUncompOctets,
       "cipSecTunOutUncompOctWraps": cipSecTunOutUncompOctWraps,
       "cipSecTunOutPkts": cipSecTunOutPkts,
       "cipSecTunOutDropPkts": cipSecTunOutDropPkts,
       "cipSecTunOutAuths": cipSecTunOutAuths,
       "cipSecTunOutAuthFails": cipSecTunOutAuthFails,
       "cipSecTunOutEncrypts": cipSecTunOutEncrypts,
       "cipSecTunOutEncryptFails": cipSecTunOutEncryptFails,
       "cipSecTunStatus": cipSecTunStatus,
       "cipSecEndPtTable": cipSecEndPtTable,
       "cipSecEndPtEntry": cipSecEndPtEntry,
       "cipSecEndPtIndex": cipSecEndPtIndex,
       "cipSecEndPtLocalName": cipSecEndPtLocalName,
       "cipSecEndPtLocalType": cipSecEndPtLocalType,
       "cipSecEndPtLocalAddr1": cipSecEndPtLocalAddr1,
       "cipSecEndPtLocalAddr2": cipSecEndPtLocalAddr2,
       "cipSecEndPtLocalProtocol": cipSecEndPtLocalProtocol,
       "cipSecEndPtLocalPort": cipSecEndPtLocalPort,
       "cipSecEndPtRemoteName": cipSecEndPtRemoteName,
       "cipSecEndPtRemoteType": cipSecEndPtRemoteType,
       "cipSecEndPtRemoteAddr1": cipSecEndPtRemoteAddr1,
       "cipSecEndPtRemoteAddr2": cipSecEndPtRemoteAddr2,
       "cipSecEndPtRemoteProtocol": cipSecEndPtRemoteProtocol,
       "cipSecEndPtRemotePort": cipSecEndPtRemotePort,
       "cipSecSpiTable": cipSecSpiTable,
       "cipSecSpiEntry": cipSecSpiEntry,
       "cipSecSpiIndex": cipSecSpiIndex,
       "cipSecSpiDirection": cipSecSpiDirection,
       "cipSecSpiValue": cipSecSpiValue,
       "cipSecSpiProtocol": cipSecSpiProtocol,
       "cipSecSpiStatus": cipSecSpiStatus,
       "cipSecPhase2GWStatsTable": cipSecPhase2GWStatsTable,
       "cipSecPhase2GWStatsEntry": cipSecPhase2GWStatsEntry,
       "cipSecPhase2GWActiveTunnels": cipSecPhase2GWActiveTunnels,
       "cipSecPhase2GWPreviousTunnels": cipSecPhase2GWPreviousTunnels,
       "cipSecPhase2GWInOctets": cipSecPhase2GWInOctets,
       "cipSecPhase2GWInOctWraps": cipSecPhase2GWInOctWraps,
       "cipSecPhase2GWInDecompOctets": cipSecPhase2GWInDecompOctets,
       "cipSecPhase2GWInDecompOctWraps": cipSecPhase2GWInDecompOctWraps,
       "cipSecPhase2GWInPkts": cipSecPhase2GWInPkts,
       "cipSecPhase2GWInDrops": cipSecPhase2GWInDrops,
       "cipSecPhase2GWInReplayDrops": cipSecPhase2GWInReplayDrops,
       "cipSecPhase2GWInAuths": cipSecPhase2GWInAuths,
       "cipSecPhase2GWInAuthFails": cipSecPhase2GWInAuthFails,
       "cipSecPhase2GWInDecrypts": cipSecPhase2GWInDecrypts,
       "cipSecPhase2GWInDecryptFails": cipSecPhase2GWInDecryptFails,
       "cipSecPhase2GWOutOctets": cipSecPhase2GWOutOctets,
       "cipSecPhase2GWOutOctWraps": cipSecPhase2GWOutOctWraps,
       "cipSecPhase2GWOutUncompOctets": cipSecPhase2GWOutUncompOctets,
       "cipSecPhase2GWOutUncompOctWraps": cipSecPhase2GWOutUncompOctWraps,
       "cipSecPhase2GWOutPkts": cipSecPhase2GWOutPkts,
       "cipSecPhase2GWOutDrops": cipSecPhase2GWOutDrops,
       "cipSecPhase2GWOutAuths": cipSecPhase2GWOutAuths,
       "cipSecPhase2GWOutAuthFails": cipSecPhase2GWOutAuthFails,
       "cipSecPhase2GWOutEncrypts": cipSecPhase2GWOutEncrypts,
       "cipSecPhase2GWOutEncryptFails": cipSecPhase2GWOutEncryptFails,
       "cipSecPhase2GWProtocolUseFails": cipSecPhase2GWProtocolUseFails,
       "cipSecPhase2GWNoSaFails": cipSecPhase2GWNoSaFails,
       "cipSecPhase2GWSysCapFails": cipSecPhase2GWSysCapFails,
       "cipSecHistory": cipSecHistory,
       "cipSecHistGlobal": cipSecHistGlobal,
       "cipSecHistGlobalCntl": cipSecHistGlobalCntl,
       "cipSecHistTableSize": cipSecHistTableSize,
       "cipSecHistCheckPoint": cipSecHistCheckPoint,
       "cipSecHistPhaseOne": cipSecHistPhaseOne,
       "cikeTunnelHistTable": cikeTunnelHistTable,
       "cikeTunnelHistEntry": cikeTunnelHistEntry,
       "cikeTunHistIndex": cikeTunHistIndex,
       "cikeTunHistTermReason": cikeTunHistTermReason,
       "cikeTunHistActiveIndex": cikeTunHistActiveIndex,
       "cikeTunHistPeerLocalType": cikeTunHistPeerLocalType,
       "cikeTunHistPeerLocalValue": cikeTunHistPeerLocalValue,
       "cikeTunHistPeerIntIndex": cikeTunHistPeerIntIndex,
       "cikeTunHistPeerRemoteType": cikeTunHistPeerRemoteType,
       "cikeTunHistPeerRemoteValue": cikeTunHistPeerRemoteValue,
       "cikeTunHistLocalAddr": cikeTunHistLocalAddr,
       "cikeTunHistLocalName": cikeTunHistLocalName,
       "cikeTunHistRemoteAddr": cikeTunHistRemoteAddr,
       "cikeTunHistRemoteName": cikeTunHistRemoteName,
       "cikeTunHistNegoMode": cikeTunHistNegoMode,
       "cikeTunHistDiffHellmanGrp": cikeTunHistDiffHellmanGrp,
       "cikeTunHistEncryptAlgo": cikeTunHistEncryptAlgo,
       "cikeTunHistHashAlgo": cikeTunHistHashAlgo,
       "cikeTunHistAuthMethod": cikeTunHistAuthMethod,
       "cikeTunHistLifeTime": cikeTunHistLifeTime,
       "cikeTunHistStartTime": cikeTunHistStartTime,
       "cikeTunHistActiveTime": cikeTunHistActiveTime,
       "cikeTunHistTotalRefreshes": cikeTunHistTotalRefreshes,
       "cikeTunHistTotalSas": cikeTunHistTotalSas,
       "cikeTunHistInOctets": cikeTunHistInOctets,
       "cikeTunHistInPkts": cikeTunHistInPkts,
       "cikeTunHistInDropPkts": cikeTunHistInDropPkts,
       "cikeTunHistInNotifys": cikeTunHistInNotifys,
       "cikeTunHistInP2Exchgs": cikeTunHistInP2Exchgs,
       "cikeTunHistInP2ExchgInvalids": cikeTunHistInP2ExchgInvalids,
       "cikeTunHistInP2ExchgRejects": cikeTunHistInP2ExchgRejects,
       "cikeTunHistInP2SaDelRequests": cikeTunHistInP2SaDelRequests,
       "cikeTunHistOutOctets": cikeTunHistOutOctets,
       "cikeTunHistOutPkts": cikeTunHistOutPkts,
       "cikeTunHistOutDropPkts": cikeTunHistOutDropPkts,
       "cikeTunHistOutNotifys": cikeTunHistOutNotifys,
       "cikeTunHistOutP2Exchgs": cikeTunHistOutP2Exchgs,
       "cikeTunHistOutP2ExchgInvalids": cikeTunHistOutP2ExchgInvalids,
       "cikeTunHistOutP2ExchgRejects": cikeTunHistOutP2ExchgRejects,
       "cikeTunHistOutP2SaDelRequests": cikeTunHistOutP2SaDelRequests,
       "cipSecHistPhaseTwo": cipSecHistPhaseTwo,
       "cipSecTunnelHistTable": cipSecTunnelHistTable,
       "cipSecTunnelHistEntry": cipSecTunnelHistEntry,
       "cipSecTunHistIndex": cipSecTunHistIndex,
       "cipSecTunHistTermReason": cipSecTunHistTermReason,
       "cipSecTunHistActiveIndex": cipSecTunHistActiveIndex,
       "cipSecTunHistIkeTunnelIndex": cipSecTunHistIkeTunnelIndex,
       "cipSecTunHistLocalAddr": cipSecTunHistLocalAddr,
       "cipSecTunHistRemoteAddr": cipSecTunHistRemoteAddr,
       "cipSecTunHistKeyType": cipSecTunHistKeyType,
       "cipSecTunHistEncapMode": cipSecTunHistEncapMode,
       "cipSecTunHistLifeSize": cipSecTunHistLifeSize,
       "cipSecTunHistLifeTime": cipSecTunHistLifeTime,
       "cipSecTunHistStartTime": cipSecTunHistStartTime,
       "cipSecTunHistActiveTime": cipSecTunHistActiveTime,
       "cipSecTunHistTotalRefreshes": cipSecTunHistTotalRefreshes,
       "cipSecTunHistTotalSas": cipSecTunHistTotalSas,
       "cipSecTunHistInSaDiffHellmanGrp": cipSecTunHistInSaDiffHellmanGrp,
       "cipSecTunHistInSaEncryptAlgo": cipSecTunHistInSaEncryptAlgo,
       "cipSecTunHistInSaAhAuthAlgo": cipSecTunHistInSaAhAuthAlgo,
       "cipSecTunHistInSaEspAuthAlgo": cipSecTunHistInSaEspAuthAlgo,
       "cipSecTunHistInSaDecompAlgo": cipSecTunHistInSaDecompAlgo,
       "cipSecTunHistOutSaDiffHellmanGrp": cipSecTunHistOutSaDiffHellmanGrp,
       "cipSecTunHistOutSaEncryptAlgo": cipSecTunHistOutSaEncryptAlgo,
       "cipSecTunHistOutSaAhAuthAlgo": cipSecTunHistOutSaAhAuthAlgo,
       "cipSecTunHistOutSaEspAuthAlgo": cipSecTunHistOutSaEspAuthAlgo,
       "cipSecTunHistOutSaCompAlgo": cipSecTunHistOutSaCompAlgo,
       "cipSecTunHistInOctets": cipSecTunHistInOctets,
       "cipSecTunHistHcInOctets": cipSecTunHistHcInOctets,
       "cipSecTunHistInOctWraps": cipSecTunHistInOctWraps,
       "cipSecTunHistInDecompOctets": cipSecTunHistInDecompOctets,
       "cipSecTunHistHcInDecompOctets": cipSecTunHistHcInDecompOctets,
       "cipSecTunHistInDecompOctWraps": cipSecTunHistInDecompOctWraps,
       "cipSecTunHistInPkts": cipSecTunHistInPkts,
       "cipSecTunHistInDropPkts": cipSecTunHistInDropPkts,
       "cipSecTunHistInReplayDropPkts": cipSecTunHistInReplayDropPkts,
       "cipSecTunHistInAuths": cipSecTunHistInAuths,
       "cipSecTunHistInAuthFails": cipSecTunHistInAuthFails,
       "cipSecTunHistInDecrypts": cipSecTunHistInDecrypts,
       "cipSecTunHistInDecryptFails": cipSecTunHistInDecryptFails,
       "cipSecTunHistOutOctets": cipSecTunHistOutOctets,
       "cipSecTunHistHcOutOctets": cipSecTunHistHcOutOctets,
       "cipSecTunHistOutOctWraps": cipSecTunHistOutOctWraps,
       "cipSecTunHistOutUncompOctets": cipSecTunHistOutUncompOctets,
       "cipSecTunHistHcOutUncompOctets": cipSecTunHistHcOutUncompOctets,
       "cipSecTunHistOutUncompOctWraps": cipSecTunHistOutUncompOctWraps,
       "cipSecTunHistOutPkts": cipSecTunHistOutPkts,
       "cipSecTunHistOutDropPkts": cipSecTunHistOutDropPkts,
       "cipSecTunHistOutAuths": cipSecTunHistOutAuths,
       "cipSecTunHistOutAuthFails": cipSecTunHistOutAuthFails,
       "cipSecTunHistOutEncrypts": cipSecTunHistOutEncrypts,
       "cipSecTunHistOutEncryptFails": cipSecTunHistOutEncryptFails,
       "cipSecEndPtHistTable": cipSecEndPtHistTable,
       "cipSecEndPtHistEntry": cipSecEndPtHistEntry,
       "cipSecEndPtHistIndex": cipSecEndPtHistIndex,
       "cipSecEndPtHistTunIndex": cipSecEndPtHistTunIndex,
       "cipSecEndPtHistActiveIndex": cipSecEndPtHistActiveIndex,
       "cipSecEndPtHistLocalName": cipSecEndPtHistLocalName,
       "cipSecEndPtHistLocalType": cipSecEndPtHistLocalType,
       "cipSecEndPtHistLocalAddr1": cipSecEndPtHistLocalAddr1,
       "cipSecEndPtHistLocalAddr2": cipSecEndPtHistLocalAddr2,
       "cipSecEndPtHistLocalProtocol": cipSecEndPtHistLocalProtocol,
       "cipSecEndPtHistLocalPort": cipSecEndPtHistLocalPort,
       "cipSecEndPtHistRemoteName": cipSecEndPtHistRemoteName,
       "cipSecEndPtHistRemoteType": cipSecEndPtHistRemoteType,
       "cipSecEndPtHistRemoteAddr1": cipSecEndPtHistRemoteAddr1,
       "cipSecEndPtHistRemoteAddr2": cipSecEndPtHistRemoteAddr2,
       "cipSecEndPtHistRemoteProtocol": cipSecEndPtHistRemoteProtocol,
       "cipSecEndPtHistRemotePort": cipSecEndPtHistRemotePort,
       "cipSecFailures": cipSecFailures,
       "cipSecFailGlobal": cipSecFailGlobal,
       "cipSecFailGlobalCntl": cipSecFailGlobalCntl,
       "cipSecFailTableSize": cipSecFailTableSize,
       "cipSecFailPhaseOne": cipSecFailPhaseOne,
       "cikeFailTable": cikeFailTable,
       "cikeFailEntry": cikeFailEntry,
       "cikeFailIndex": cikeFailIndex,
       "cikeFailReason": cikeFailReason,
       "cikeFailTime": cikeFailTime,
       "cikeFailLocalType": cikeFailLocalType,
       "cikeFailLocalValue": cikeFailLocalValue,
       "cikeFailRemoteType": cikeFailRemoteType,
       "cikeFailRemoteValue": cikeFailRemoteValue,
       "cikeFailLocalAddr": cikeFailLocalAddr,
       "cikeFailRemoteAddr": cikeFailRemoteAddr,
       "cipSecFailPhaseTwo": cipSecFailPhaseTwo,
       "cipSecFailTable": cipSecFailTable,
       "cipSecFailEntry": cipSecFailEntry,
       "cipSecFailIndex": cipSecFailIndex,
       "cipSecFailReason": cipSecFailReason,
       "cipSecFailTime": cipSecFailTime,
       "cipSecFailTunnelIndex": cipSecFailTunnelIndex,
       "cipSecFailSaSpi": cipSecFailSaSpi,
       "cipSecFailPktSrcAddr": cipSecFailPktSrcAddr,
       "cipSecFailPktDstAddr": cipSecFailPktDstAddr,
       "cipSecTrapCntl": cipSecTrapCntl,
       "cipSecTrapCntlIkeTunnelStart": cipSecTrapCntlIkeTunnelStart,
       "cipSecTrapCntlIkeTunnelStop": cipSecTrapCntlIkeTunnelStop,
       "cipSecTrapCntlIkeSysFailure": cipSecTrapCntlIkeSysFailure,
       "cipSecTrapCntlIkeCertCrlFailure": cipSecTrapCntlIkeCertCrlFailure,
       "cipSecTrapCntlIkeProtocolFail": cipSecTrapCntlIkeProtocolFail,
       "cipSecTrapCntlIkeNoSa": cipSecTrapCntlIkeNoSa,
       "cipSecTrapCntlIpSecTunnelStart": cipSecTrapCntlIpSecTunnelStart,
       "cipSecTrapCntlIpSecTunnelStop": cipSecTrapCntlIpSecTunnelStop,
       "cipSecTrapCntlIpSecSysFailure": cipSecTrapCntlIpSecSysFailure,
       "cipSecTrapCntlIpSecSetUpFailure": cipSecTrapCntlIpSecSetUpFailure,
       "cipSecTrapCntlIpSecEarlyTunTerm": cipSecTrapCntlIpSecEarlyTunTerm,
       "cipSecTrapCntlIpSecProtocolFail": cipSecTrapCntlIpSecProtocolFail,
       "cipSecTrapCntlIpSecNoSa": cipSecTrapCntlIpSecNoSa,
       "cipSecMIBNotificationPrefix": cipSecMIBNotificationPrefix,
       "cipSecMIBNotifications": cipSecMIBNotifications,
       "cikeTunnelStart": cikeTunnelStart,
       "cikeTunnelStop": cikeTunnelStop,
       "cikeSysFailure": cikeSysFailure,
       "cikeCertCrlFailure": cikeCertCrlFailure,
       "cikeProtocolFailure": cikeProtocolFailure,
       "cikeNoSa": cikeNoSa,
       "cipSecTunnelStart": cipSecTunnelStart,
       "cipSecTunnelStop": cipSecTunnelStop,
       "cipSecSysFailure": cipSecSysFailure,
       "cipSecSetUpFailure": cipSecSetUpFailure,
       "cipSecEarlyTunTerm": cipSecEarlyTunTerm,
       "cipSecProtocolFailure": cipSecProtocolFailure,
       "cipSecNoSa": cipSecNoSa,
       "cipSecMIBConformance": cipSecMIBConformance,
       "cipSecMIBGroups": cipSecMIBGroups,
       "cipSecLevelsGroup": cipSecLevelsGroup,
       "cipSecPhaseOneGroup": cipSecPhaseOneGroup,
       "cipSecPhaseTwoGroup": cipSecPhaseTwoGroup,
       "cipSecHistoryGroup": cipSecHistoryGroup,
       "cipSecFailuresGroup": cipSecFailuresGroup,
       "cipSecTrapCntlGroup": cipSecTrapCntlGroup,
       "cipSecNotificationGroup": cipSecNotificationGroup,
       "cipSecGWStatsGroup": cipSecGWStatsGroup,
       "cipSecMIBCompliances": cipSecMIBCompliances,
       "cipSecMIBCompliance": cipSecMIBCompliance,
       "cipSecMIBComplianceRev1": cipSecMIBComplianceRev1}
)
