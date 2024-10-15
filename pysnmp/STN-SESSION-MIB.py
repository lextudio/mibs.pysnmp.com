# SNMP MIB module (STN-SESSION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/STN-SESSION-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:58:17 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(stnNotification,
 stnSystems) = mibBuilder.importSymbols(
    "SPRING-TIDE-NETWORKS-SMI",
    "stnNotification",
    "stnSystems")

(StnConfigFailureType,
 StnUserFailureType) = mibBuilder.importSymbols(
    "SPRING-TIDE-NETWORKS-TC",
    "StnConfigFailureType",
    "StnUserFailureType")

(stnEngineCpu,
 stnEngineIndex,
 stnEngineSlot) = mibBuilder.importSymbols(
    "STN-CHASSIS-MIB",
    "stnEngineCpu",
    "stnEngineIndex",
    "stnEngineSlot")

(stnRouterIndex,) = mibBuilder.importSymbols(
    "STN-ROUTER-MIB",
    "stnRouterIndex")


# MODULE-IDENTITY

stnSessions = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 5)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class SessionOperStatus(Integer32, TextualConvention):
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
        *(("active", 4),
          ("inactive", 2),
          ("pend-active", 3),
          ("pend-inactive", 5),
          ("unknown", 1))
    )



# MIB Managed Objects in the order of their OIDs

_StnSessionObjects_ObjectIdentity = ObjectIdentity
stnSessionObjects = _StnSessionObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 5, 1)
)
_StnSession_ObjectIdentity = ObjectIdentity
stnSession = _StnSession_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 5, 1, 1)
)
_StnSessionTable_Object = MibTable
stnSessionTable = _StnSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 5, 1, 1, 1)
)
if mibBuilder.loadTexts:
    stnSessionTable.setStatus("current")
_StnSessionEntry_Object = MibTableRow
stnSessionEntry = _StnSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 5, 1, 1, 1, 1)
)
stnSessionEntry.setIndexNames(
    (0, "STN-SESSION-MIB", "stnSessionIndex"),
)
if mibBuilder.loadTexts:
    stnSessionEntry.setStatus("current")
_StnSessionIndex_Type = Unsigned32
_StnSessionIndex_Object = MibTableColumn
stnSessionIndex = _StnSessionIndex_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 5, 1, 1, 1, 1, 1),
    _StnSessionIndex_Type()
)
stnSessionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnSessionIndex.setStatus("current")


class _StnSessionType_Type(Integer32):
    """Custom type stnSessionType based on Integer32"""
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("console", 10),
          ("encaps", 11),
          ("ftp", 8),
          ("ftp-alg", 9),
          ("ike", 6),
          ("ipsec", 5),
          ("l2tp-tunnel", 3),
          ("ppp", 2),
          ("pptp-tunnel", 4),
          ("remote-config", 13),
          ("secure-user", 12),
          ("telnet", 7),
          ("unknown", 1))
    )


_StnSessionType_Type.__name__ = "Integer32"
_StnSessionType_Object = MibTableColumn
stnSessionType = _StnSessionType_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 5, 1, 1, 1, 1, 2),
    _StnSessionType_Type()
)
stnSessionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnSessionType.setStatus("current")


class _StnSessionContext_Type(OctetString):
    """Custom type stnSessionContext based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_StnSessionContext_Type.__name__ = "OctetString"
_StnSessionContext_Object = MibTableColumn
stnSessionContext = _StnSessionContext_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 5, 1, 1, 1, 1, 3),
    _StnSessionContext_Type()
)
stnSessionContext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnSessionContext.setStatus("current")
_StnSessionOperStatus_Type = SessionOperStatus
_StnSessionOperStatus_Object = MibTableColumn
stnSessionOperStatus = _StnSessionOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 5, 1, 1, 1, 1, 4),
    _StnSessionOperStatus_Type()
)
stnSessionOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnSessionOperStatus.setStatus("current")
_StnSessionLastChange_Type = TimeTicks
_StnSessionLastChange_Object = MibTableColumn
stnSessionLastChange = _StnSessionLastChange_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 5, 1, 1, 1, 1, 5),
    _StnSessionLastChange_Type()
)
stnSessionLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnSessionLastChange.setStatus("current")
_StnSessionsPpp_ObjectIdentity = ObjectIdentity
stnSessionsPpp = _StnSessionsPpp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 5, 1, 1, 2)
)
_StnSessionPppTotalCount_Type = Unsigned32
_StnSessionPppTotalCount_Object = MibScalar
stnSessionPppTotalCount = _StnSessionPppTotalCount_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 5, 1, 1, 2, 1),
    _StnSessionPppTotalCount_Type()
)
stnSessionPppTotalCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnSessionPppTotalCount.setStatus("current")
_StnSessionPppFailedCount_Type = Unsigned32
_StnSessionPppFailedCount_Object = MibScalar
stnSessionPppFailedCount = _StnSessionPppFailedCount_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 5, 1, 1, 2, 2),
    _StnSessionPppFailedCount_Type()
)
stnSessionPppFailedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnSessionPppFailedCount.setStatus("current")
_StnSessionPppCurrentCount_Type = Unsigned32
_StnSessionPppCurrentCount_Object = MibScalar
stnSessionPppCurrentCount = _StnSessionPppCurrentCount_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 5, 1, 1, 2, 3),
    _StnSessionPppCurrentCount_Type()
)
stnSessionPppCurrentCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnSessionPppCurrentCount.setStatus("current")
_StnSessionPppCurrentActiveCount_Type = Unsigned32
_StnSessionPppCurrentActiveCount_Object = MibScalar
stnSessionPppCurrentActiveCount = _StnSessionPppCurrentActiveCount_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 5, 1, 1, 2, 4),
    _StnSessionPppCurrentActiveCount_Type()
)
stnSessionPppCurrentActiveCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnSessionPppCurrentActiveCount.setStatus("current")
_StnSessionsL2tp_ObjectIdentity = ObjectIdentity
stnSessionsL2tp = _StnSessionsL2tp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 5, 1, 1, 3)
)
_StnSessionL2tpTunnelTotalCount_Type = Unsigned32
_StnSessionL2tpTunnelTotalCount_Object = MibScalar
stnSessionL2tpTunnelTotalCount = _StnSessionL2tpTunnelTotalCount_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 5, 1, 1, 3, 1),
    _StnSessionL2tpTunnelTotalCount_Type()
)
stnSessionL2tpTunnelTotalCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnSessionL2tpTunnelTotalCount.setStatus("current")
_StnSessionL2tpTunnelFailedCount_Type = Unsigned32
_StnSessionL2tpTunnelFailedCount_Object = MibScalar
stnSessionL2tpTunnelFailedCount = _StnSessionL2tpTunnelFailedCount_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 5, 1, 1, 3, 2),
    _StnSessionL2tpTunnelFailedCount_Type()
)
stnSessionL2tpTunnelFailedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnSessionL2tpTunnelFailedCount.setStatus("current")
_StnSessionL2tpTunnelCurrentCount_Type = Unsigned32
_StnSessionL2tpTunnelCurrentCount_Object = MibScalar
stnSessionL2tpTunnelCurrentCount = _StnSessionL2tpTunnelCurrentCount_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 5, 1, 1, 3, 3),
    _StnSessionL2tpTunnelCurrentCount_Type()
)
stnSessionL2tpTunnelCurrentCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnSessionL2tpTunnelCurrentCount.setStatus("current")
_StnSessionL2tpTunnelCurrentActiveCount_Type = Unsigned32
_StnSessionL2tpTunnelCurrentActiveCount_Object = MibScalar
stnSessionL2tpTunnelCurrentActiveCount = _StnSessionL2tpTunnelCurrentActiveCount_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 5, 1, 1, 3, 4),
    _StnSessionL2tpTunnelCurrentActiveCount_Type()
)
stnSessionL2tpTunnelCurrentActiveCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnSessionL2tpTunnelCurrentActiveCount.setStatus("current")
_StnSessionsPptp_ObjectIdentity = ObjectIdentity
stnSessionsPptp = _StnSessionsPptp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 5, 1, 1, 4)
)
_StnSessionPptpTunnelTotalCount_Type = Unsigned32
_StnSessionPptpTunnelTotalCount_Object = MibScalar
stnSessionPptpTunnelTotalCount = _StnSessionPptpTunnelTotalCount_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 5, 1, 1, 4, 1),
    _StnSessionPptpTunnelTotalCount_Type()
)
stnSessionPptpTunnelTotalCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnSessionPptpTunnelTotalCount.setStatus("current")
_StnSessionPptpTunnelFailedCount_Type = Unsigned32
_StnSessionPptpTunnelFailedCount_Object = MibScalar
stnSessionPptpTunnelFailedCount = _StnSessionPptpTunnelFailedCount_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 5, 1, 1, 4, 2),
    _StnSessionPptpTunnelFailedCount_Type()
)
stnSessionPptpTunnelFailedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnSessionPptpTunnelFailedCount.setStatus("current")
_StnSessionPptpTunnelCurrentCount_Type = Unsigned32
_StnSessionPptpTunnelCurrentCount_Object = MibScalar
stnSessionPptpTunnelCurrentCount = _StnSessionPptpTunnelCurrentCount_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 5, 1, 1, 4, 3),
    _StnSessionPptpTunnelCurrentCount_Type()
)
stnSessionPptpTunnelCurrentCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnSessionPptpTunnelCurrentCount.setStatus("current")
_StnSessionPptpTunnelCurrentActiveCount_Type = Unsigned32
_StnSessionPptpTunnelCurrentActiveCount_Object = MibScalar
stnSessionPptpTunnelCurrentActiveCount = _StnSessionPptpTunnelCurrentActiveCount_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 5, 1, 1, 4, 4),
    _StnSessionPptpTunnelCurrentActiveCount_Type()
)
stnSessionPptpTunnelCurrentActiveCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnSessionPptpTunnelCurrentActiveCount.setStatus("current")
_StnSessionsIpsec_ObjectIdentity = ObjectIdentity
stnSessionsIpsec = _StnSessionsIpsec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 5, 1, 1, 5)
)
_StnSessionIpsecTotalCount_Type = Unsigned32
_StnSessionIpsecTotalCount_Object = MibScalar
stnSessionIpsecTotalCount = _StnSessionIpsecTotalCount_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 5, 1, 1, 5, 1),
    _StnSessionIpsecTotalCount_Type()
)
stnSessionIpsecTotalCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnSessionIpsecTotalCount.setStatus("current")
_StnSessionIpsecFailedCount_Type = Unsigned32
_StnSessionIpsecFailedCount_Object = MibScalar
stnSessionIpsecFailedCount = _StnSessionIpsecFailedCount_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 5, 1, 1, 5, 2),
    _StnSessionIpsecFailedCount_Type()
)
stnSessionIpsecFailedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnSessionIpsecFailedCount.setStatus("current")
_StnSessionIpsecCurrentCount_Type = Unsigned32
_StnSessionIpsecCurrentCount_Object = MibScalar
stnSessionIpsecCurrentCount = _StnSessionIpsecCurrentCount_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 5, 1, 1, 5, 3),
    _StnSessionIpsecCurrentCount_Type()
)
stnSessionIpsecCurrentCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnSessionIpsecCurrentCount.setStatus("current")
_StnSessionIpsecCurrentActiveCount_Type = Unsigned32
_StnSessionIpsecCurrentActiveCount_Object = MibScalar
stnSessionIpsecCurrentActiveCount = _StnSessionIpsecCurrentActiveCount_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 5, 1, 1, 5, 4),
    _StnSessionIpsecCurrentActiveCount_Type()
)
stnSessionIpsecCurrentActiveCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnSessionIpsecCurrentActiveCount.setStatus("current")
_StnSessionsIke_ObjectIdentity = ObjectIdentity
stnSessionsIke = _StnSessionsIke_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 5, 1, 1, 6)
)
_StnSessionIkeTotalCount_Type = Unsigned32
_StnSessionIkeTotalCount_Object = MibScalar
stnSessionIkeTotalCount = _StnSessionIkeTotalCount_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 5, 1, 1, 6, 1),
    _StnSessionIkeTotalCount_Type()
)
stnSessionIkeTotalCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnSessionIkeTotalCount.setStatus("current")
_StnSessionIkeFailedCount_Type = Unsigned32
_StnSessionIkeFailedCount_Object = MibScalar
stnSessionIkeFailedCount = _StnSessionIkeFailedCount_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 5, 1, 1, 6, 2),
    _StnSessionIkeFailedCount_Type()
)
stnSessionIkeFailedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnSessionIkeFailedCount.setStatus("current")
_StnSessionIkeCurrentCount_Type = Unsigned32
_StnSessionIkeCurrentCount_Object = MibScalar
stnSessionIkeCurrentCount = _StnSessionIkeCurrentCount_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 5, 1, 1, 6, 3),
    _StnSessionIkeCurrentCount_Type()
)
stnSessionIkeCurrentCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnSessionIkeCurrentCount.setStatus("current")
_StnSessionIkeCurrentActiveCount_Type = Unsigned32
_StnSessionIkeCurrentActiveCount_Object = MibScalar
stnSessionIkeCurrentActiveCount = _StnSessionIkeCurrentActiveCount_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 5, 1, 1, 6, 4),
    _StnSessionIkeCurrentActiveCount_Type()
)
stnSessionIkeCurrentActiveCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnSessionIkeCurrentActiveCount.setStatus("current")
_StnSessionsTelnet_ObjectIdentity = ObjectIdentity
stnSessionsTelnet = _StnSessionsTelnet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 5, 1, 1, 7)
)
_StnSessionTelnetTotalCount_Type = Unsigned32
_StnSessionTelnetTotalCount_Object = MibScalar
stnSessionTelnetTotalCount = _StnSessionTelnetTotalCount_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 5, 1, 1, 7, 1),
    _StnSessionTelnetTotalCount_Type()
)
stnSessionTelnetTotalCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnSessionTelnetTotalCount.setStatus("current")
_StnSessionTelnetFailedCount_Type = Unsigned32
_StnSessionTelnetFailedCount_Object = MibScalar
stnSessionTelnetFailedCount = _StnSessionTelnetFailedCount_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 5, 1, 1, 7, 2),
    _StnSessionTelnetFailedCount_Type()
)
stnSessionTelnetFailedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnSessionTelnetFailedCount.setStatus("current")
_StnSessionTelnetCurrentCount_Type = Unsigned32
_StnSessionTelnetCurrentCount_Object = MibScalar
stnSessionTelnetCurrentCount = _StnSessionTelnetCurrentCount_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 5, 1, 1, 7, 3),
    _StnSessionTelnetCurrentCount_Type()
)
stnSessionTelnetCurrentCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnSessionTelnetCurrentCount.setStatus("current")
_StnSessionTelnetCurrentActiveCount_Type = Unsigned32
_StnSessionTelnetCurrentActiveCount_Object = MibScalar
stnSessionTelnetCurrentActiveCount = _StnSessionTelnetCurrentActiveCount_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 5, 1, 1, 7, 4),
    _StnSessionTelnetCurrentActiveCount_Type()
)
stnSessionTelnetCurrentActiveCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnSessionTelnetCurrentActiveCount.setStatus("current")
_StnSessionsFtp_ObjectIdentity = ObjectIdentity
stnSessionsFtp = _StnSessionsFtp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 5, 1, 1, 8)
)
_StnSessionFtpTotalCount_Type = Unsigned32
_StnSessionFtpTotalCount_Object = MibScalar
stnSessionFtpTotalCount = _StnSessionFtpTotalCount_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 5, 1, 1, 8, 1),
    _StnSessionFtpTotalCount_Type()
)
stnSessionFtpTotalCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnSessionFtpTotalCount.setStatus("current")
_StnSessionFtpFailedCount_Type = Unsigned32
_StnSessionFtpFailedCount_Object = MibScalar
stnSessionFtpFailedCount = _StnSessionFtpFailedCount_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 5, 1, 1, 8, 2),
    _StnSessionFtpFailedCount_Type()
)
stnSessionFtpFailedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnSessionFtpFailedCount.setStatus("current")
_StnSessionFtpCurrentCount_Type = Unsigned32
_StnSessionFtpCurrentCount_Object = MibScalar
stnSessionFtpCurrentCount = _StnSessionFtpCurrentCount_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 5, 1, 1, 8, 3),
    _StnSessionFtpCurrentCount_Type()
)
stnSessionFtpCurrentCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnSessionFtpCurrentCount.setStatus("current")
_StnSessionFtpCurrentActiveCount_Type = Unsigned32
_StnSessionFtpCurrentActiveCount_Object = MibScalar
stnSessionFtpCurrentActiveCount = _StnSessionFtpCurrentActiveCount_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 5, 1, 1, 8, 4),
    _StnSessionFtpCurrentActiveCount_Type()
)
stnSessionFtpCurrentActiveCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnSessionFtpCurrentActiveCount.setStatus("current")
_StnSessionsFtpAlg_ObjectIdentity = ObjectIdentity
stnSessionsFtpAlg = _StnSessionsFtpAlg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 5, 1, 1, 9)
)
_StnSessionFtpAlgTotalCount_Type = Unsigned32
_StnSessionFtpAlgTotalCount_Object = MibScalar
stnSessionFtpAlgTotalCount = _StnSessionFtpAlgTotalCount_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 5, 1, 1, 9, 1),
    _StnSessionFtpAlgTotalCount_Type()
)
stnSessionFtpAlgTotalCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnSessionFtpAlgTotalCount.setStatus("current")
_StnSessionFtpAlgFailedCount_Type = Unsigned32
_StnSessionFtpAlgFailedCount_Object = MibScalar
stnSessionFtpAlgFailedCount = _StnSessionFtpAlgFailedCount_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 5, 1, 1, 9, 2),
    _StnSessionFtpAlgFailedCount_Type()
)
stnSessionFtpAlgFailedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnSessionFtpAlgFailedCount.setStatus("current")
_StnSessionFtpAlgCurrentCount_Type = Unsigned32
_StnSessionFtpAlgCurrentCount_Object = MibScalar
stnSessionFtpAlgCurrentCount = _StnSessionFtpAlgCurrentCount_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 5, 1, 1, 9, 3),
    _StnSessionFtpAlgCurrentCount_Type()
)
stnSessionFtpAlgCurrentCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnSessionFtpAlgCurrentCount.setStatus("current")
_StnSessionFtpAlgCurrentActiveCount_Type = Unsigned32
_StnSessionFtpAlgCurrentActiveCount_Object = MibScalar
stnSessionFtpAlgCurrentActiveCount = _StnSessionFtpAlgCurrentActiveCount_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 5, 1, 1, 9, 4),
    _StnSessionFtpAlgCurrentActiveCount_Type()
)
stnSessionFtpAlgCurrentActiveCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnSessionFtpAlgCurrentActiveCount.setStatus("current")
_StnSessionsConsole_ObjectIdentity = ObjectIdentity
stnSessionsConsole = _StnSessionsConsole_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 5, 1, 1, 10)
)
_StnSessionConsoleTotalCount_Type = Unsigned32
_StnSessionConsoleTotalCount_Object = MibScalar
stnSessionConsoleTotalCount = _StnSessionConsoleTotalCount_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 5, 1, 1, 10, 1),
    _StnSessionConsoleTotalCount_Type()
)
stnSessionConsoleTotalCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnSessionConsoleTotalCount.setStatus("current")
_StnSessionConsoleFailedCount_Type = Unsigned32
_StnSessionConsoleFailedCount_Object = MibScalar
stnSessionConsoleFailedCount = _StnSessionConsoleFailedCount_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 5, 1, 1, 10, 2),
    _StnSessionConsoleFailedCount_Type()
)
stnSessionConsoleFailedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnSessionConsoleFailedCount.setStatus("current")
_StnSessionConsoleCurrentCount_Type = Unsigned32
_StnSessionConsoleCurrentCount_Object = MibScalar
stnSessionConsoleCurrentCount = _StnSessionConsoleCurrentCount_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 5, 1, 1, 10, 3),
    _StnSessionConsoleCurrentCount_Type()
)
stnSessionConsoleCurrentCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnSessionConsoleCurrentCount.setStatus("current")
_StnSessionConsoleCurrentActiveCount_Type = Unsigned32
_StnSessionConsoleCurrentActiveCount_Object = MibScalar
stnSessionConsoleCurrentActiveCount = _StnSessionConsoleCurrentActiveCount_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 5, 1, 1, 10, 4),
    _StnSessionConsoleCurrentActiveCount_Type()
)
stnSessionConsoleCurrentActiveCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnSessionConsoleCurrentActiveCount.setStatus("current")
_StnSessionsAggregate_ObjectIdentity = ObjectIdentity
stnSessionsAggregate = _StnSessionsAggregate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 5, 1, 1, 11)
)
_StnSessionAggregateTotalCount_Type = Unsigned32
_StnSessionAggregateTotalCount_Object = MibScalar
stnSessionAggregateTotalCount = _StnSessionAggregateTotalCount_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 5, 1, 1, 11, 1),
    _StnSessionAggregateTotalCount_Type()
)
stnSessionAggregateTotalCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnSessionAggregateTotalCount.setStatus("current")
_StnSessionAggregateFailedCount_Type = Unsigned32
_StnSessionAggregateFailedCount_Object = MibScalar
stnSessionAggregateFailedCount = _StnSessionAggregateFailedCount_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 5, 1, 1, 11, 2),
    _StnSessionAggregateFailedCount_Type()
)
stnSessionAggregateFailedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnSessionAggregateFailedCount.setStatus("current")
_StnSessionAggregateCurrentCount_Type = Unsigned32
_StnSessionAggregateCurrentCount_Object = MibScalar
stnSessionAggregateCurrentCount = _StnSessionAggregateCurrentCount_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 5, 1, 1, 11, 3),
    _StnSessionAggregateCurrentCount_Type()
)
stnSessionAggregateCurrentCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnSessionAggregateCurrentCount.setStatus("current")
_StnSessionAggregateCurrentActiveCount_Type = Unsigned32
_StnSessionAggregateCurrentActiveCount_Object = MibScalar
stnSessionAggregateCurrentActiveCount = _StnSessionAggregateCurrentActiveCount_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 5, 1, 1, 11, 4),
    _StnSessionAggregateCurrentActiveCount_Type()
)
stnSessionAggregateCurrentActiveCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnSessionAggregateCurrentActiveCount.setStatus("current")
_StnSessionsEncaps_ObjectIdentity = ObjectIdentity
stnSessionsEncaps = _StnSessionsEncaps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 5, 1, 1, 12)
)
_StnSessionEncapsTotalCount_Type = Unsigned32
_StnSessionEncapsTotalCount_Object = MibScalar
stnSessionEncapsTotalCount = _StnSessionEncapsTotalCount_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 5, 1, 1, 12, 1),
    _StnSessionEncapsTotalCount_Type()
)
stnSessionEncapsTotalCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnSessionEncapsTotalCount.setStatus("current")
_StnSessionEncapsFailedCount_Type = Unsigned32
_StnSessionEncapsFailedCount_Object = MibScalar
stnSessionEncapsFailedCount = _StnSessionEncapsFailedCount_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 5, 1, 1, 12, 2),
    _StnSessionEncapsFailedCount_Type()
)
stnSessionEncapsFailedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnSessionEncapsFailedCount.setStatus("current")
_StnSessionEncapsCurrentCount_Type = Unsigned32
_StnSessionEncapsCurrentCount_Object = MibScalar
stnSessionEncapsCurrentCount = _StnSessionEncapsCurrentCount_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 5, 1, 1, 12, 3),
    _StnSessionEncapsCurrentCount_Type()
)
stnSessionEncapsCurrentCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnSessionEncapsCurrentCount.setStatus("current")
_StnSessionEncapsCurrentActiveCount_Type = Unsigned32
_StnSessionEncapsCurrentActiveCount_Object = MibScalar
stnSessionEncapsCurrentActiveCount = _StnSessionEncapsCurrentActiveCount_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 5, 1, 1, 12, 4),
    _StnSessionEncapsCurrentActiveCount_Type()
)
stnSessionEncapsCurrentActiveCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnSessionEncapsCurrentActiveCount.setStatus("current")
_StnSessionsSecureUser_ObjectIdentity = ObjectIdentity
stnSessionsSecureUser = _StnSessionsSecureUser_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 5, 1, 1, 13)
)
_StnSessionSecureUserTotalCount_Type = Unsigned32
_StnSessionSecureUserTotalCount_Object = MibScalar
stnSessionSecureUserTotalCount = _StnSessionSecureUserTotalCount_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 5, 1, 1, 13, 1),
    _StnSessionSecureUserTotalCount_Type()
)
stnSessionSecureUserTotalCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnSessionSecureUserTotalCount.setStatus("current")
_StnSessionSecureUserFailedCount_Type = Unsigned32
_StnSessionSecureUserFailedCount_Object = MibScalar
stnSessionSecureUserFailedCount = _StnSessionSecureUserFailedCount_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 5, 1, 1, 13, 2),
    _StnSessionSecureUserFailedCount_Type()
)
stnSessionSecureUserFailedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnSessionSecureUserFailedCount.setStatus("current")
_StnSessionSecureUserCurrentCount_Type = Unsigned32
_StnSessionSecureUserCurrentCount_Object = MibScalar
stnSessionSecureUserCurrentCount = _StnSessionSecureUserCurrentCount_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 5, 1, 1, 13, 3),
    _StnSessionSecureUserCurrentCount_Type()
)
stnSessionSecureUserCurrentCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnSessionSecureUserCurrentCount.setStatus("current")
_StnSessionSecureUserCurrentActiveCount_Type = Unsigned32
_StnSessionSecureUserCurrentActiveCount_Object = MibScalar
stnSessionSecureUserCurrentActiveCount = _StnSessionSecureUserCurrentActiveCount_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 5, 1, 1, 13, 4),
    _StnSessionSecureUserCurrentActiveCount_Type()
)
stnSessionSecureUserCurrentActiveCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnSessionSecureUserCurrentActiveCount.setStatus("current")
_StnSessionsRemoteConfig_ObjectIdentity = ObjectIdentity
stnSessionsRemoteConfig = _StnSessionsRemoteConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 5, 1, 1, 14)
)
_StnSessionRemoteConfigTotalCount_Type = Unsigned32
_StnSessionRemoteConfigTotalCount_Object = MibScalar
stnSessionRemoteConfigTotalCount = _StnSessionRemoteConfigTotalCount_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 5, 1, 1, 14, 1),
    _StnSessionRemoteConfigTotalCount_Type()
)
stnSessionRemoteConfigTotalCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnSessionRemoteConfigTotalCount.setStatus("current")
_StnSessionRemoteConfigFailedCount_Type = Unsigned32
_StnSessionRemoteConfigFailedCount_Object = MibScalar
stnSessionRemoteConfigFailedCount = _StnSessionRemoteConfigFailedCount_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 5, 1, 1, 14, 2),
    _StnSessionRemoteConfigFailedCount_Type()
)
stnSessionRemoteConfigFailedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnSessionRemoteConfigFailedCount.setStatus("current")
_StnSessionRemoteConfigCurrentCount_Type = Unsigned32
_StnSessionRemoteConfigCurrentCount_Object = MibScalar
stnSessionRemoteConfigCurrentCount = _StnSessionRemoteConfigCurrentCount_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 5, 1, 1, 14, 3),
    _StnSessionRemoteConfigCurrentCount_Type()
)
stnSessionRemoteConfigCurrentCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnSessionRemoteConfigCurrentCount.setStatus("current")
_StnSessionRemoteConfigCurrentActiveCount_Type = Unsigned32
_StnSessionRemoteConfigCurrentActiveCount_Object = MibScalar
stnSessionRemoteConfigCurrentActiveCount = _StnSessionRemoteConfigCurrentActiveCount_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 5, 1, 1, 14, 4),
    _StnSessionRemoteConfigCurrentActiveCount_Type()
)
stnSessionRemoteConfigCurrentActiveCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnSessionRemoteConfigCurrentActiveCount.setStatus("current")
_StnGlobalSession_ObjectIdentity = ObjectIdentity
stnGlobalSession = _StnGlobalSession_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 5, 1, 2)
)
_StnGlobalSessionTable_Object = MibTable
stnGlobalSessionTable = _StnGlobalSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 5, 1, 2, 1)
)
if mibBuilder.loadTexts:
    stnGlobalSessionTable.setStatus("current")
_StnGlobalSessionEntry_Object = MibTableRow
stnGlobalSessionEntry = _StnGlobalSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 5, 1, 2, 1, 1)
)
stnGlobalSessionEntry.setIndexNames(
    (0, "STN-SESSION-MIB", "stnGlobalSessionIndex"),
)
if mibBuilder.loadTexts:
    stnGlobalSessionEntry.setStatus("current")
_StnGlobalSessionIndex_Type = Unsigned32
_StnGlobalSessionIndex_Object = MibTableColumn
stnGlobalSessionIndex = _StnGlobalSessionIndex_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 5, 1, 2, 1, 1, 1),
    _StnGlobalSessionIndex_Type()
)
stnGlobalSessionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    stnGlobalSessionIndex.setStatus("current")


class _StnGlobalSessionOperStatus_Type(Integer32):
    """Custom type stnGlobalSessionOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 1))
    )


_StnGlobalSessionOperStatus_Type.__name__ = "Integer32"
_StnGlobalSessionOperStatus_Object = MibTableColumn
stnGlobalSessionOperStatus = _StnGlobalSessionOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 5, 1, 2, 1, 1, 2),
    _StnGlobalSessionOperStatus_Type()
)
stnGlobalSessionOperStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stnGlobalSessionOperStatus.setStatus("current")
_StnSessionMibConformance_ObjectIdentity = ObjectIdentity
stnSessionMibConformance = _StnSessionMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 5, 2)
)
_StnSessionTrapVars_ObjectIdentity = ObjectIdentity
stnSessionTrapVars = _StnSessionTrapVars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 5, 3)
)
_StnNotificationUsername_Type = DisplayString
_StnNotificationUsername_Object = MibScalar
stnNotificationUsername = _StnNotificationUsername_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 5, 3, 1),
    _StnNotificationUsername_Type()
)
stnNotificationUsername.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnNotificationUsername.setStatus("current")
_StnNotificationUserFailureType_Type = StnUserFailureType
_StnNotificationUserFailureType_Object = MibScalar
stnNotificationUserFailureType = _StnNotificationUserFailureType_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 5, 3, 2),
    _StnNotificationUserFailureType_Type()
)
stnNotificationUserFailureType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnNotificationUserFailureType.setStatus("current")
_StnNotificationConfigType_Type = StnConfigFailureType
_StnNotificationConfigType_Object = MibScalar
stnNotificationConfigType = _StnNotificationConfigType_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 5, 3, 3),
    _StnNotificationConfigType_Type()
)
stnNotificationConfigType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnNotificationConfigType.setStatus("current")

# Managed Objects groups


# Notification objects

stnUserFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3551, 2, 100, 0, 17)
)
stnUserFailure.setObjects(
      *(("STN-ROUTER-MIB", "stnRouterIndex"),
        ("STN-SESSION-MIB", "stnNotificationUsername"),
        ("STN-SESSION-MIB", "stnNotificationUserFailureType"),
        ("STN-SESSION-MIB", "stnSessionType"))
)
if mibBuilder.loadTexts:
    stnUserFailure.setStatus(
        "current"
    )

stnConfigFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3551, 2, 100, 0, 18)
)
stnConfigFailure.setObjects(
      *(("STN-ROUTER-MIB", "stnRouterIndex"),
        ("STN-SESSION-MIB", "stnNotificationUsername"),
        ("STN-SESSION-MIB", "stnNotificationConfigType"))
)
if mibBuilder.loadTexts:
    stnConfigFailure.setStatus(
        "current"
    )

stnNoFlowEntriesAvailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 3551, 2, 100, 0, 57)
)
stnNoFlowEntriesAvailable.setObjects(
      *(("STN-CHASSIS-MIB", "stnEngineIndex"),
        ("STN-CHASSIS-MIB", "stnEngineSlot"),
        ("STN-CHASSIS-MIB", "stnEngineCpu"))
)
if mibBuilder.loadTexts:
    stnNoFlowEntriesAvailable.setStatus(
        "current"
    )

stnNoLayerIfsAvailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 3551, 2, 100, 0, 58)
)
stnNoLayerIfsAvailable.setObjects(
      *(("STN-CHASSIS-MIB", "stnEngineIndex"),
        ("STN-CHASSIS-MIB", "stnEngineSlot"),
        ("STN-CHASSIS-MIB", "stnEngineCpu"))
)
if mibBuilder.loadTexts:
    stnNoLayerIfsAvailable.setStatus(
        "current"
    )

stnMaxSessionLimitExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 3551, 2, 100, 0, 59)
)
stnMaxSessionLimitExceeded.setObjects(
      *(("STN-CHASSIS-MIB", "stnEngineIndex"),
        ("STN-CHASSIS-MIB", "stnEngineSlot"),
        ("STN-CHASSIS-MIB", "stnEngineCpu"))
)
if mibBuilder.loadTexts:
    stnMaxSessionLimitExceeded.setStatus(
        "current"
    )

stnTunnelEngineLimitExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 3551, 2, 100, 0, 60)
)
stnTunnelEngineLimitExceeded.setObjects(
      *(("STN-CHASSIS-MIB", "stnEngineIndex"),
        ("STN-CHASSIS-MIB", "stnEngineSlot"),
        ("STN-CHASSIS-MIB", "stnEngineCpu"))
)
if mibBuilder.loadTexts:
    stnTunnelEngineLimitExceeded.setStatus(
        "current"
    )

stnCallEngineLimitExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 3551, 2, 100, 0, 61)
)
stnCallEngineLimitExceeded.setObjects(
      *(("STN-CHASSIS-MIB", "stnEngineIndex"),
        ("STN-CHASSIS-MIB", "stnEngineSlot"),
        ("STN-CHASSIS-MIB", "stnEngineCpu"))
)
if mibBuilder.loadTexts:
    stnCallEngineLimitExceeded.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "STN-SESSION-MIB",
    **{"SessionOperStatus": SessionOperStatus,
       "stnSessions": stnSessions,
       "stnSessionObjects": stnSessionObjects,
       "stnSession": stnSession,
       "stnSessionTable": stnSessionTable,
       "stnSessionEntry": stnSessionEntry,
       "stnSessionIndex": stnSessionIndex,
       "stnSessionType": stnSessionType,
       "stnSessionContext": stnSessionContext,
       "stnSessionOperStatus": stnSessionOperStatus,
       "stnSessionLastChange": stnSessionLastChange,
       "stnSessionsPpp": stnSessionsPpp,
       "stnSessionPppTotalCount": stnSessionPppTotalCount,
       "stnSessionPppFailedCount": stnSessionPppFailedCount,
       "stnSessionPppCurrentCount": stnSessionPppCurrentCount,
       "stnSessionPppCurrentActiveCount": stnSessionPppCurrentActiveCount,
       "stnSessionsL2tp": stnSessionsL2tp,
       "stnSessionL2tpTunnelTotalCount": stnSessionL2tpTunnelTotalCount,
       "stnSessionL2tpTunnelFailedCount": stnSessionL2tpTunnelFailedCount,
       "stnSessionL2tpTunnelCurrentCount": stnSessionL2tpTunnelCurrentCount,
       "stnSessionL2tpTunnelCurrentActiveCount": stnSessionL2tpTunnelCurrentActiveCount,
       "stnSessionsPptp": stnSessionsPptp,
       "stnSessionPptpTunnelTotalCount": stnSessionPptpTunnelTotalCount,
       "stnSessionPptpTunnelFailedCount": stnSessionPptpTunnelFailedCount,
       "stnSessionPptpTunnelCurrentCount": stnSessionPptpTunnelCurrentCount,
       "stnSessionPptpTunnelCurrentActiveCount": stnSessionPptpTunnelCurrentActiveCount,
       "stnSessionsIpsec": stnSessionsIpsec,
       "stnSessionIpsecTotalCount": stnSessionIpsecTotalCount,
       "stnSessionIpsecFailedCount": stnSessionIpsecFailedCount,
       "stnSessionIpsecCurrentCount": stnSessionIpsecCurrentCount,
       "stnSessionIpsecCurrentActiveCount": stnSessionIpsecCurrentActiveCount,
       "stnSessionsIke": stnSessionsIke,
       "stnSessionIkeTotalCount": stnSessionIkeTotalCount,
       "stnSessionIkeFailedCount": stnSessionIkeFailedCount,
       "stnSessionIkeCurrentCount": stnSessionIkeCurrentCount,
       "stnSessionIkeCurrentActiveCount": stnSessionIkeCurrentActiveCount,
       "stnSessionsTelnet": stnSessionsTelnet,
       "stnSessionTelnetTotalCount": stnSessionTelnetTotalCount,
       "stnSessionTelnetFailedCount": stnSessionTelnetFailedCount,
       "stnSessionTelnetCurrentCount": stnSessionTelnetCurrentCount,
       "stnSessionTelnetCurrentActiveCount": stnSessionTelnetCurrentActiveCount,
       "stnSessionsFtp": stnSessionsFtp,
       "stnSessionFtpTotalCount": stnSessionFtpTotalCount,
       "stnSessionFtpFailedCount": stnSessionFtpFailedCount,
       "stnSessionFtpCurrentCount": stnSessionFtpCurrentCount,
       "stnSessionFtpCurrentActiveCount": stnSessionFtpCurrentActiveCount,
       "stnSessionsFtpAlg": stnSessionsFtpAlg,
       "stnSessionFtpAlgTotalCount": stnSessionFtpAlgTotalCount,
       "stnSessionFtpAlgFailedCount": stnSessionFtpAlgFailedCount,
       "stnSessionFtpAlgCurrentCount": stnSessionFtpAlgCurrentCount,
       "stnSessionFtpAlgCurrentActiveCount": stnSessionFtpAlgCurrentActiveCount,
       "stnSessionsConsole": stnSessionsConsole,
       "stnSessionConsoleTotalCount": stnSessionConsoleTotalCount,
       "stnSessionConsoleFailedCount": stnSessionConsoleFailedCount,
       "stnSessionConsoleCurrentCount": stnSessionConsoleCurrentCount,
       "stnSessionConsoleCurrentActiveCount": stnSessionConsoleCurrentActiveCount,
       "stnSessionsAggregate": stnSessionsAggregate,
       "stnSessionAggregateTotalCount": stnSessionAggregateTotalCount,
       "stnSessionAggregateFailedCount": stnSessionAggregateFailedCount,
       "stnSessionAggregateCurrentCount": stnSessionAggregateCurrentCount,
       "stnSessionAggregateCurrentActiveCount": stnSessionAggregateCurrentActiveCount,
       "stnSessionsEncaps": stnSessionsEncaps,
       "stnSessionEncapsTotalCount": stnSessionEncapsTotalCount,
       "stnSessionEncapsFailedCount": stnSessionEncapsFailedCount,
       "stnSessionEncapsCurrentCount": stnSessionEncapsCurrentCount,
       "stnSessionEncapsCurrentActiveCount": stnSessionEncapsCurrentActiveCount,
       "stnSessionsSecureUser": stnSessionsSecureUser,
       "stnSessionSecureUserTotalCount": stnSessionSecureUserTotalCount,
       "stnSessionSecureUserFailedCount": stnSessionSecureUserFailedCount,
       "stnSessionSecureUserCurrentCount": stnSessionSecureUserCurrentCount,
       "stnSessionSecureUserCurrentActiveCount": stnSessionSecureUserCurrentActiveCount,
       "stnSessionsRemoteConfig": stnSessionsRemoteConfig,
       "stnSessionRemoteConfigTotalCount": stnSessionRemoteConfigTotalCount,
       "stnSessionRemoteConfigFailedCount": stnSessionRemoteConfigFailedCount,
       "stnSessionRemoteConfigCurrentCount": stnSessionRemoteConfigCurrentCount,
       "stnSessionRemoteConfigCurrentActiveCount": stnSessionRemoteConfigCurrentActiveCount,
       "stnGlobalSession": stnGlobalSession,
       "stnGlobalSessionTable": stnGlobalSessionTable,
       "stnGlobalSessionEntry": stnGlobalSessionEntry,
       "stnGlobalSessionIndex": stnGlobalSessionIndex,
       "stnGlobalSessionOperStatus": stnGlobalSessionOperStatus,
       "stnSessionMibConformance": stnSessionMibConformance,
       "stnSessionTrapVars": stnSessionTrapVars,
       "stnNotificationUsername": stnNotificationUsername,
       "stnNotificationUserFailureType": stnNotificationUserFailureType,
       "stnNotificationConfigType": stnNotificationConfigType,
       "stnUserFailure": stnUserFailure,
       "stnConfigFailure": stnConfigFailure,
       "stnNoFlowEntriesAvailable": stnNoFlowEntriesAvailable,
       "stnNoLayerIfsAvailable": stnNoLayerIfsAvailable,
       "stnMaxSessionLimitExceeded": stnMaxSessionLimitExceeded,
       "stnTunnelEngineLimitExceeded": stnTunnelEngineLimitExceeded,
       "stnCallEngineLimitExceeded": stnCallEngineLimitExceeded}
)
