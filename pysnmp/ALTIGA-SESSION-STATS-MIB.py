# SNMP MIB module (ALTIGA-SESSION-STATS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALTIGA-SESSION-STATS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:38:13 2024
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

(alSessionMibModule,) = mibBuilder.importSymbols(
    "ALTIGA-GLOBAL-REG",
    "alSessionMibModule")

(alSessionGroup,
 alStatsSession) = mibBuilder.importSymbols(
    "ALTIGA-MIB",
    "alSessionGroup",
    "alStatsSession")

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
 MacAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

altigaSessionStatsMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 22, 2)
)
altigaSessionStatsMibModule.setRevisions(
        ("2005-01-26 00:00",
         "2003-09-09 00:00",
         "2003-03-17 00:00",
         "2002-09-05 13:00",
         "2002-07-10 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class SessionProtocol(Integer32, TextualConvention):
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
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28)
        )
    )
    namedValues = NamedValues(
        *(("console", 9),
          ("debugConsole", 11),
          ("debugTelnet", 10),
          ("ftp", 5),
          ("http", 4),
          ("httpsTunnel", 28),
          ("ike", 13),
          ("imap4s", 26),
          ("ipsec", 3),
          ("ipsecLan2LanOverNatT", 22),
          ("ipsecLanToLan", 15),
          ("ipsecOverNatT", 21),
          ("ipsecOverTcp", 19),
          ("ipsecOverUdp", 16),
          ("l2tp", 2),
          ("l2tpOverIpSec", 14),
          ("l2tpOverIpsecOverNatT", 23),
          ("other", 12),
          ("pop3s", 25),
          ("pppoe", 20),
          ("pptp", 1),
          ("smtps", 27),
          ("snmp", 7),
          ("ssh", 17),
          ("telnet", 6),
          ("tftp", 8),
          ("userHttps", 24),
          ("vcaLanToLan", 18))
    )



class EncryptionAlgorithm(Integer32, TextualConvention):
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
              10,
              11,
              64,
              66,
              68,
              72,
              128,
              130,
              132,
              136)
        )
    )
    namedValues = NamedValues(
        *(("aes128", 9),
          ("aes192", 10),
          ("aes256", 11),
          ("des168", 4),
          ("des40", 3),
          ("des56", 2),
          ("none", 1),
          ("rc4Statefull128", 8),
          ("rc4Statefull40", 6),
          ("rc4Stateless128", 7),
          ("rc4Stateless40", 5),
          ("sslv3", 64),
          ("sslv3des168", 68),
          ("sslv3des56", 66),
          ("sslv3rc4Statefull128", 72),
          ("tlsv1", 128),
          ("tlsv1des168", 132),
          ("tlsv1des56", 130),
          ("tlsv1rc4Statefull128", 136))
    )



class CompressionAlgorithm(Integer32, TextualConvention):
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
        *(("deflate", 2),
          ("lz", 3),
          ("lzs", 1),
          ("none", 0))
    )



class NacResult(Integer32, TextualConvention):
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
              6)
        )
    )
    namedValues = NamedValues(
        *(("accepted", 1),
          ("exempted", 3),
          ("holdoff", 6),
          ("nonResponsive", 4),
          ("notApplicable", 5),
          ("rejected", 2),
          ("unknown", 0))
    )



# MIB Managed Objects in the order of their OIDs

_AltigaSessionStatsMibConformance_ObjectIdentity = ObjectIdentity
altigaSessionStatsMibConformance = _AltigaSessionStatsMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 22, 2, 1)
)
_AltigaSessionStatsMibCompliances_ObjectIdentity = ObjectIdentity
altigaSessionStatsMibCompliances = _AltigaSessionStatsMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 22, 2, 1, 1)
)
_AlStatsSessionGlobal_ObjectIdentity = ObjectIdentity
alStatsSessionGlobal = _AlStatsSessionGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 1)
)
_AlActiveSessionCount_Type = Gauge32
_AlActiveSessionCount_Object = MibScalar
alActiveSessionCount = _AlActiveSessionCount_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 1, 1),
    _AlActiveSessionCount_Type()
)
alActiveSessionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alActiveSessionCount.setStatus("current")
_AlTotalSessionCount_Type = Counter32
_AlTotalSessionCount_Object = MibScalar
alTotalSessionCount = _AlTotalSessionCount_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 1, 2),
    _AlTotalSessionCount_Type()
)
alTotalSessionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alTotalSessionCount.setStatus("current")
_AlActiveSessionLastUpdate_Type = TimeTicks
_AlActiveSessionLastUpdate_Object = MibScalar
alActiveSessionLastUpdate = _AlActiveSessionLastUpdate_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 1, 3),
    _AlActiveSessionLastUpdate_Type()
)
alActiveSessionLastUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alActiveSessionLastUpdate.setStatus("current")
_AlActiveSessionMaxUsers_Type = Gauge32
_AlActiveSessionMaxUsers_Object = MibScalar
alActiveSessionMaxUsers = _AlActiveSessionMaxUsers_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 1, 4),
    _AlActiveSessionMaxUsers_Type()
)
alActiveSessionMaxUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alActiveSessionMaxUsers.setStatus("current")
_AlActiveSessionGroupIdLock_Type = Integer32
_AlActiveSessionGroupIdLock_Object = MibScalar
alActiveSessionGroupIdLock = _AlActiveSessionGroupIdLock_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 1, 5),
    _AlActiveSessionGroupIdLock_Type()
)
alActiveSessionGroupIdLock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alActiveSessionGroupIdLock.setStatus("current")
_AlMaxSessionCount_Type = Counter32
_AlMaxSessionCount_Object = MibScalar
alMaxSessionCount = _AlMaxSessionCount_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 1, 6),
    _AlMaxSessionCount_Type()
)
alMaxSessionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMaxSessionCount.setStatus("current")
_AlActiveLanToLanSessionCount_Type = Gauge32
_AlActiveLanToLanSessionCount_Object = MibScalar
alActiveLanToLanSessionCount = _AlActiveLanToLanSessionCount_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 1, 7),
    _AlActiveLanToLanSessionCount_Type()
)
alActiveLanToLanSessionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alActiveLanToLanSessionCount.setStatus("current")
_AlActiveManagementSessionCount_Type = Gauge32
_AlActiveManagementSessionCount_Object = MibScalar
alActiveManagementSessionCount = _AlActiveManagementSessionCount_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 1, 8),
    _AlActiveManagementSessionCount_Type()
)
alActiveManagementSessionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alActiveManagementSessionCount.setStatus("current")
_AlActiveRemoteAccessSessionCount_Type = Gauge32
_AlActiveRemoteAccessSessionCount_Object = MibScalar
alActiveRemoteAccessSessionCount = _AlActiveRemoteAccessSessionCount_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 1, 9),
    _AlActiveRemoteAccessSessionCount_Type()
)
alActiveRemoteAccessSessionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alActiveRemoteAccessSessionCount.setStatus("current")
_AlActiveSessionMaxWebVpnUsers_Type = Gauge32
_AlActiveSessionMaxWebVpnUsers_Object = MibScalar
alActiveSessionMaxWebVpnUsers = _AlActiveSessionMaxWebVpnUsers_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 1, 10),
    _AlActiveSessionMaxWebVpnUsers_Type()
)
alActiveSessionMaxWebVpnUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alActiveSessionMaxWebVpnUsers.setStatus("current")
_AlWeightedSessionCount_Type = Gauge32
_AlWeightedSessionCount_Object = MibScalar
alWeightedSessionCount = _AlWeightedSessionCount_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 1, 11),
    _AlWeightedSessionCount_Type()
)
alWeightedSessionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alWeightedSessionCount.setStatus("current")
_AlActiveNacAcceptedSessions_Type = Gauge32
_AlActiveNacAcceptedSessions_Object = MibScalar
alActiveNacAcceptedSessions = _AlActiveNacAcceptedSessions_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 1, 12),
    _AlActiveNacAcceptedSessions_Type()
)
alActiveNacAcceptedSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alActiveNacAcceptedSessions.setStatus("current")
_AlTotalNacAcceptedSessions_Type = Gauge32
_AlTotalNacAcceptedSessions_Object = MibScalar
alTotalNacAcceptedSessions = _AlTotalNacAcceptedSessions_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 1, 13),
    _AlTotalNacAcceptedSessions_Type()
)
alTotalNacAcceptedSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alTotalNacAcceptedSessions.setStatus("current")
_AlActiveNacRejectedSessions_Type = Gauge32
_AlActiveNacRejectedSessions_Object = MibScalar
alActiveNacRejectedSessions = _AlActiveNacRejectedSessions_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 1, 14),
    _AlActiveNacRejectedSessions_Type()
)
alActiveNacRejectedSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alActiveNacRejectedSessions.setStatus("current")
_AlTotalNacRejectedSessions_Type = Gauge32
_AlTotalNacRejectedSessions_Object = MibScalar
alTotalNacRejectedSessions = _AlTotalNacRejectedSessions_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 1, 15),
    _AlTotalNacRejectedSessions_Type()
)
alTotalNacRejectedSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alTotalNacRejectedSessions.setStatus("current")
_AlActiveNacExemptedSessions_Type = Gauge32
_AlActiveNacExemptedSessions_Object = MibScalar
alActiveNacExemptedSessions = _AlActiveNacExemptedSessions_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 1, 16),
    _AlActiveNacExemptedSessions_Type()
)
alActiveNacExemptedSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alActiveNacExemptedSessions.setStatus("current")
_AlTotalNacExemptedSessions_Type = Gauge32
_AlTotalNacExemptedSessions_Object = MibScalar
alTotalNacExemptedSessions = _AlTotalNacExemptedSessions_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 1, 17),
    _AlTotalNacExemptedSessions_Type()
)
alTotalNacExemptedSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alTotalNacExemptedSessions.setStatus("current")
_AlActiveNacNonresponsiveSessions_Type = Gauge32
_AlActiveNacNonresponsiveSessions_Object = MibScalar
alActiveNacNonresponsiveSessions = _AlActiveNacNonresponsiveSessions_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 1, 18),
    _AlActiveNacNonresponsiveSessions_Type()
)
alActiveNacNonresponsiveSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alActiveNacNonresponsiveSessions.setStatus("current")
_AlTotalNacNonresponsiveSessions_Type = Gauge32
_AlTotalNacNonresponsiveSessions_Object = MibScalar
alTotalNacNonresponsiveSessions = _AlTotalNacNonresponsiveSessions_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 1, 19),
    _AlTotalNacNonresponsiveSessions_Type()
)
alTotalNacNonresponsiveSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alTotalNacNonresponsiveSessions.setStatus("current")
_AlActiveNacDisabledSessions_Type = Gauge32
_AlActiveNacDisabledSessions_Object = MibScalar
alActiveNacDisabledSessions = _AlActiveNacDisabledSessions_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 1, 20),
    _AlActiveNacDisabledSessions_Type()
)
alActiveNacDisabledSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alActiveNacDisabledSessions.setStatus("current")
_AlTotalNacDisabledSessions_Type = Gauge32
_AlTotalNacDisabledSessions_Object = MibScalar
alTotalNacDisabledSessions = _AlTotalNacDisabledSessions_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 1, 21),
    _AlTotalNacDisabledSessions_Type()
)
alTotalNacDisabledSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alTotalNacDisabledSessions.setStatus("current")
_AlActiveNacHoldoffSessions_Type = Gauge32
_AlActiveNacHoldoffSessions_Object = MibScalar
alActiveNacHoldoffSessions = _AlActiveNacHoldoffSessions_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 1, 22),
    _AlActiveNacHoldoffSessions_Type()
)
alActiveNacHoldoffSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alActiveNacHoldoffSessions.setStatus("current")
_AlTotalNacHoldoffSessions_Type = Gauge32
_AlTotalNacHoldoffSessions_Object = MibScalar
alTotalNacHoldoffSessions = _AlTotalNacHoldoffSessions_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 1, 23),
    _AlTotalNacHoldoffSessions_Type()
)
alTotalNacHoldoffSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alTotalNacHoldoffSessions.setStatus("current")
_AlActiveSessionTable_Object = MibTable
alActiveSessionTable = _AlActiveSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 2)
)
if mibBuilder.loadTexts:
    alActiveSessionTable.setStatus("current")
_AlActiveSessionEntry_Object = MibTableRow
alActiveSessionEntry = _AlActiveSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 2, 1)
)
alActiveSessionEntry.setIndexNames(
    (0, "ALTIGA-SESSION-STATS-MIB", "alActiveSessionIndex"),
)
if mibBuilder.loadTexts:
    alActiveSessionEntry.setStatus("current")
_AlActiveSessionRowStatus_Type = RowStatus
_AlActiveSessionRowStatus_Object = MibTableColumn
alActiveSessionRowStatus = _AlActiveSessionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 2, 1, 1),
    _AlActiveSessionRowStatus_Type()
)
alActiveSessionRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alActiveSessionRowStatus.setStatus("current")


class _AlActiveSessionIndex_Type(Integer32):
    """Custom type alActiveSessionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_AlActiveSessionIndex_Type.__name__ = "Integer32"
_AlActiveSessionIndex_Object = MibTableColumn
alActiveSessionIndex = _AlActiveSessionIndex_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 2, 1, 2),
    _AlActiveSessionIndex_Type()
)
alActiveSessionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alActiveSessionIndex.setStatus("current")
_AlActiveSessionUserName_Type = DisplayString
_AlActiveSessionUserName_Object = MibTableColumn
alActiveSessionUserName = _AlActiveSessionUserName_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 2, 1, 3),
    _AlActiveSessionUserName_Type()
)
alActiveSessionUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alActiveSessionUserName.setStatus("current")
_AlActiveSessionIpAddress_Type = IpAddress
_AlActiveSessionIpAddress_Object = MibTableColumn
alActiveSessionIpAddress = _AlActiveSessionIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 2, 1, 4),
    _AlActiveSessionIpAddress_Type()
)
alActiveSessionIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alActiveSessionIpAddress.setStatus("current")
_AlActiveSessionProtocol_Type = SessionProtocol
_AlActiveSessionProtocol_Object = MibTableColumn
alActiveSessionProtocol = _AlActiveSessionProtocol_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 2, 1, 5),
    _AlActiveSessionProtocol_Type()
)
alActiveSessionProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alActiveSessionProtocol.setStatus("current")
_AlActiveSessionEncrType_Type = EncryptionAlgorithm
_AlActiveSessionEncrType_Object = MibTableColumn
alActiveSessionEncrType = _AlActiveSessionEncrType_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 2, 1, 6),
    _AlActiveSessionEncrType_Type()
)
alActiveSessionEncrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alActiveSessionEncrType.setStatus("current")
_AlActiveSessionStartTime_Type = TimeTicks
_AlActiveSessionStartTime_Object = MibTableColumn
alActiveSessionStartTime = _AlActiveSessionStartTime_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 2, 1, 7),
    _AlActiveSessionStartTime_Type()
)
alActiveSessionStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alActiveSessionStartTime.setStatus("current")
_AlActiveSessionConnectTime_Type = Unsigned32
_AlActiveSessionConnectTime_Object = MibTableColumn
alActiveSessionConnectTime = _AlActiveSessionConnectTime_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 2, 1, 8),
    _AlActiveSessionConnectTime_Type()
)
alActiveSessionConnectTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alActiveSessionConnectTime.setStatus("current")
_AlActiveSessionOctetsSent_Type = Counter32
_AlActiveSessionOctetsSent_Object = MibTableColumn
alActiveSessionOctetsSent = _AlActiveSessionOctetsSent_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 2, 1, 9),
    _AlActiveSessionOctetsSent_Type()
)
alActiveSessionOctetsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alActiveSessionOctetsSent.setStatus("current")
_AlActiveSessionOctetsRcvd_Type = Counter32
_AlActiveSessionOctetsRcvd_Object = MibTableColumn
alActiveSessionOctetsRcvd = _AlActiveSessionOctetsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 2, 1, 10),
    _AlActiveSessionOctetsRcvd_Type()
)
alActiveSessionOctetsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alActiveSessionOctetsRcvd.setStatus("current")
_AlActiveSessionSepId_Type = Integer32
_AlActiveSessionSepId_Object = MibTableColumn
alActiveSessionSepId = _AlActiveSessionSepId_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 2, 1, 11),
    _AlActiveSessionSepId_Type()
)
alActiveSessionSepId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alActiveSessionSepId.setStatus("current")
_AlActiveSessionGroupName_Type = DisplayString
_AlActiveSessionGroupName_Object = MibTableColumn
alActiveSessionGroupName = _AlActiveSessionGroupName_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 2, 1, 12),
    _AlActiveSessionGroupName_Type()
)
alActiveSessionGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alActiveSessionGroupName.setStatus("current")
_AlActiveSessionGroupId_Type = Integer32
_AlActiveSessionGroupId_Object = MibTableColumn
alActiveSessionGroupId = _AlActiveSessionGroupId_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 2, 1, 13),
    _AlActiveSessionGroupId_Type()
)
alActiveSessionGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alActiveSessionGroupId.setStatus("current")
_AlActiveSessionPublicIpAddress_Type = IpAddress
_AlActiveSessionPublicIpAddress_Object = MibTableColumn
alActiveSessionPublicIpAddress = _AlActiveSessionPublicIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 2, 1, 14),
    _AlActiveSessionPublicIpAddress_Type()
)
alActiveSessionPublicIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alActiveSessionPublicIpAddress.setStatus("current")
_AlActiveSessionTopTenData_Type = Gauge32
_AlActiveSessionTopTenData_Object = MibTableColumn
alActiveSessionTopTenData = _AlActiveSessionTopTenData_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 2, 1, 15),
    _AlActiveSessionTopTenData_Type()
)
alActiveSessionTopTenData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alActiveSessionTopTenData.setStatus("current")
_AlActiveSessionLoginTime_Type = Unsigned32
_AlActiveSessionLoginTime_Object = MibTableColumn
alActiveSessionLoginTime = _AlActiveSessionLoginTime_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 2, 1, 16),
    _AlActiveSessionLoginTime_Type()
)
alActiveSessionLoginTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alActiveSessionLoginTime.setStatus("current")
_AlActiveSessionOS_Type = DisplayString
_AlActiveSessionOS_Object = MibTableColumn
alActiveSessionOS = _AlActiveSessionOS_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 2, 1, 17),
    _AlActiveSessionOS_Type()
)
alActiveSessionOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alActiveSessionOS.setStatus("current")
_AlActiveSessionVersion_Type = DisplayString
_AlActiveSessionVersion_Object = MibTableColumn
alActiveSessionVersion = _AlActiveSessionVersion_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 2, 1, 18),
    _AlActiveSessionVersion_Type()
)
alActiveSessionVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alActiveSessionVersion.setStatus("current")
_AlActiveSessionFilterId_Type = Integer32
_AlActiveSessionFilterId_Object = MibTableColumn
alActiveSessionFilterId = _AlActiveSessionFilterId_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 2, 1, 19),
    _AlActiveSessionFilterId_Type()
)
alActiveSessionFilterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alActiveSessionFilterId.setStatus("current")
_AlActiveSessionNacResult_Type = NacResult
_AlActiveSessionNacResult_Object = MibTableColumn
alActiveSessionNacResult = _AlActiveSessionNacResult_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 2, 1, 20),
    _AlActiveSessionNacResult_Type()
)
alActiveSessionNacResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alActiveSessionNacResult.setStatus("current")
_AlActiveSessionThroughputTable_Object = MibTable
alActiveSessionThroughputTable = _AlActiveSessionThroughputTable_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 3)
)
if mibBuilder.loadTexts:
    alActiveSessionThroughputTable.setStatus("current")
_AlActiveSessionThroughputEntry_Object = MibTableRow
alActiveSessionThroughputEntry = _AlActiveSessionThroughputEntry_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 3, 1)
)
alActiveSessionThroughputEntry.setIndexNames(
    (0, "ALTIGA-SESSION-STATS-MIB", "alActiveSessionThroughputIndex"),
)
if mibBuilder.loadTexts:
    alActiveSessionThroughputEntry.setStatus("current")
_AlActiveSessionThroughputRowStatus_Type = RowStatus
_AlActiveSessionThroughputRowStatus_Object = MibTableColumn
alActiveSessionThroughputRowStatus = _AlActiveSessionThroughputRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 3, 1, 1),
    _AlActiveSessionThroughputRowStatus_Type()
)
alActiveSessionThroughputRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alActiveSessionThroughputRowStatus.setStatus("current")


class _AlActiveSessionThroughputIndex_Type(Integer32):
    """Custom type alActiveSessionThroughputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_AlActiveSessionThroughputIndex_Type.__name__ = "Integer32"
_AlActiveSessionThroughputIndex_Object = MibTableColumn
alActiveSessionThroughputIndex = _AlActiveSessionThroughputIndex_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 3, 1, 2),
    _AlActiveSessionThroughputIndex_Type()
)
alActiveSessionThroughputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alActiveSessionThroughputIndex.setStatus("current")
_AlActiveSessionThroughputUserName_Type = DisplayString
_AlActiveSessionThroughputUserName_Object = MibTableColumn
alActiveSessionThroughputUserName = _AlActiveSessionThroughputUserName_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 3, 1, 3),
    _AlActiveSessionThroughputUserName_Type()
)
alActiveSessionThroughputUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alActiveSessionThroughputUserName.setStatus("current")
_AlActiveSessionThroughputIpAddress_Type = IpAddress
_AlActiveSessionThroughputIpAddress_Object = MibTableColumn
alActiveSessionThroughputIpAddress = _AlActiveSessionThroughputIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 3, 1, 4),
    _AlActiveSessionThroughputIpAddress_Type()
)
alActiveSessionThroughputIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alActiveSessionThroughputIpAddress.setStatus("current")
_AlActiveSessionThroughputProtocol_Type = SessionProtocol
_AlActiveSessionThroughputProtocol_Object = MibTableColumn
alActiveSessionThroughputProtocol = _AlActiveSessionThroughputProtocol_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 3, 1, 5),
    _AlActiveSessionThroughputProtocol_Type()
)
alActiveSessionThroughputProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alActiveSessionThroughputProtocol.setStatus("current")
_AlActiveSessionThroughputEncrType_Type = EncryptionAlgorithm
_AlActiveSessionThroughputEncrType_Object = MibTableColumn
alActiveSessionThroughputEncrType = _AlActiveSessionThroughputEncrType_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 3, 1, 6),
    _AlActiveSessionThroughputEncrType_Type()
)
alActiveSessionThroughputEncrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alActiveSessionThroughputEncrType.setStatus("current")
_AlActiveSessionThroughputStartTime_Type = TimeTicks
_AlActiveSessionThroughputStartTime_Object = MibTableColumn
alActiveSessionThroughputStartTime = _AlActiveSessionThroughputStartTime_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 3, 1, 7),
    _AlActiveSessionThroughputStartTime_Type()
)
alActiveSessionThroughputStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alActiveSessionThroughputStartTime.setStatus("current")
_AlActiveSessionThroughputConnectTime_Type = Counter32
_AlActiveSessionThroughputConnectTime_Object = MibTableColumn
alActiveSessionThroughputConnectTime = _AlActiveSessionThroughputConnectTime_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 3, 1, 8),
    _AlActiveSessionThroughputConnectTime_Type()
)
alActiveSessionThroughputConnectTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alActiveSessionThroughputConnectTime.setStatus("current")
_AlActiveSessionThroughputOctetsSent_Type = Counter32
_AlActiveSessionThroughputOctetsSent_Object = MibTableColumn
alActiveSessionThroughputOctetsSent = _AlActiveSessionThroughputOctetsSent_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 3, 1, 9),
    _AlActiveSessionThroughputOctetsSent_Type()
)
alActiveSessionThroughputOctetsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alActiveSessionThroughputOctetsSent.setStatus("current")
_AlActiveSessionThroughputOctetsRcvd_Type = Counter32
_AlActiveSessionThroughputOctetsRcvd_Object = MibTableColumn
alActiveSessionThroughputOctetsRcvd = _AlActiveSessionThroughputOctetsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 3, 1, 10),
    _AlActiveSessionThroughputOctetsRcvd_Type()
)
alActiveSessionThroughputOctetsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alActiveSessionThroughputOctetsRcvd.setStatus("current")
_AlActiveSessionThroughputSepId_Type = Integer32
_AlActiveSessionThroughputSepId_Object = MibTableColumn
alActiveSessionThroughputSepId = _AlActiveSessionThroughputSepId_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 3, 1, 11),
    _AlActiveSessionThroughputSepId_Type()
)
alActiveSessionThroughputSepId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alActiveSessionThroughputSepId.setStatus("current")
_AlActiveSessionThroughputGroupName_Type = DisplayString
_AlActiveSessionThroughputGroupName_Object = MibTableColumn
alActiveSessionThroughputGroupName = _AlActiveSessionThroughputGroupName_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 3, 1, 12),
    _AlActiveSessionThroughputGroupName_Type()
)
alActiveSessionThroughputGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alActiveSessionThroughputGroupName.setStatus("current")
_AlActiveSessionThroughputGroupId_Type = Integer32
_AlActiveSessionThroughputGroupId_Object = MibTableColumn
alActiveSessionThroughputGroupId = _AlActiveSessionThroughputGroupId_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 3, 1, 13),
    _AlActiveSessionThroughputGroupId_Type()
)
alActiveSessionThroughputGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alActiveSessionThroughputGroupId.setStatus("current")
_AlActiveSessionThroughputPublicIpAddress_Type = IpAddress
_AlActiveSessionThroughputPublicIpAddress_Object = MibTableColumn
alActiveSessionThroughputPublicIpAddress = _AlActiveSessionThroughputPublicIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 3, 1, 14),
    _AlActiveSessionThroughputPublicIpAddress_Type()
)
alActiveSessionThroughputPublicIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alActiveSessionThroughputPublicIpAddress.setStatus("current")
_AlActiveSessionThroughputTopTenData_Type = Gauge32
_AlActiveSessionThroughputTopTenData_Object = MibTableColumn
alActiveSessionThroughputTopTenData = _AlActiveSessionThroughputTopTenData_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 3, 1, 15),
    _AlActiveSessionThroughputTopTenData_Type()
)
alActiveSessionThroughputTopTenData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alActiveSessionThroughputTopTenData.setStatus("current")
_AlActiveSessionThroughputLoginTime_Type = Unsigned32
_AlActiveSessionThroughputLoginTime_Object = MibTableColumn
alActiveSessionThroughputLoginTime = _AlActiveSessionThroughputLoginTime_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 3, 1, 16),
    _AlActiveSessionThroughputLoginTime_Type()
)
alActiveSessionThroughputLoginTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alActiveSessionThroughputLoginTime.setStatus("current")
_AlActiveSessionDataTable_Object = MibTable
alActiveSessionDataTable = _AlActiveSessionDataTable_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 4)
)
if mibBuilder.loadTexts:
    alActiveSessionDataTable.setStatus("current")
_AlActiveSessionDataEntry_Object = MibTableRow
alActiveSessionDataEntry = _AlActiveSessionDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 4, 1)
)
alActiveSessionDataEntry.setIndexNames(
    (0, "ALTIGA-SESSION-STATS-MIB", "alActiveSessionDataIndex"),
)
if mibBuilder.loadTexts:
    alActiveSessionDataEntry.setStatus("current")
_AlActiveSessionDataRowStatus_Type = RowStatus
_AlActiveSessionDataRowStatus_Object = MibTableColumn
alActiveSessionDataRowStatus = _AlActiveSessionDataRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 4, 1, 1),
    _AlActiveSessionDataRowStatus_Type()
)
alActiveSessionDataRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alActiveSessionDataRowStatus.setStatus("current")


class _AlActiveSessionDataIndex_Type(Integer32):
    """Custom type alActiveSessionDataIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_AlActiveSessionDataIndex_Type.__name__ = "Integer32"
_AlActiveSessionDataIndex_Object = MibTableColumn
alActiveSessionDataIndex = _AlActiveSessionDataIndex_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 4, 1, 2),
    _AlActiveSessionDataIndex_Type()
)
alActiveSessionDataIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alActiveSessionDataIndex.setStatus("current")
_AlActiveSessionDataUserName_Type = DisplayString
_AlActiveSessionDataUserName_Object = MibTableColumn
alActiveSessionDataUserName = _AlActiveSessionDataUserName_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 4, 1, 3),
    _AlActiveSessionDataUserName_Type()
)
alActiveSessionDataUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alActiveSessionDataUserName.setStatus("current")
_AlActiveSessionDataIpAddress_Type = IpAddress
_AlActiveSessionDataIpAddress_Object = MibTableColumn
alActiveSessionDataIpAddress = _AlActiveSessionDataIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 4, 1, 4),
    _AlActiveSessionDataIpAddress_Type()
)
alActiveSessionDataIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alActiveSessionDataIpAddress.setStatus("current")
_AlActiveSessionDataProtocol_Type = SessionProtocol
_AlActiveSessionDataProtocol_Object = MibTableColumn
alActiveSessionDataProtocol = _AlActiveSessionDataProtocol_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 4, 1, 5),
    _AlActiveSessionDataProtocol_Type()
)
alActiveSessionDataProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alActiveSessionDataProtocol.setStatus("current")
_AlActiveSessionDataEncrType_Type = EncryptionAlgorithm
_AlActiveSessionDataEncrType_Object = MibTableColumn
alActiveSessionDataEncrType = _AlActiveSessionDataEncrType_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 4, 1, 6),
    _AlActiveSessionDataEncrType_Type()
)
alActiveSessionDataEncrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alActiveSessionDataEncrType.setStatus("current")
_AlActiveSessionDataStartTime_Type = TimeTicks
_AlActiveSessionDataStartTime_Object = MibTableColumn
alActiveSessionDataStartTime = _AlActiveSessionDataStartTime_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 4, 1, 7),
    _AlActiveSessionDataStartTime_Type()
)
alActiveSessionDataStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alActiveSessionDataStartTime.setStatus("current")
_AlActiveSessionDataConnectTime_Type = Counter32
_AlActiveSessionDataConnectTime_Object = MibTableColumn
alActiveSessionDataConnectTime = _AlActiveSessionDataConnectTime_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 4, 1, 8),
    _AlActiveSessionDataConnectTime_Type()
)
alActiveSessionDataConnectTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alActiveSessionDataConnectTime.setStatus("current")
_AlActiveSessionDataOctetsSent_Type = Counter32
_AlActiveSessionDataOctetsSent_Object = MibTableColumn
alActiveSessionDataOctetsSent = _AlActiveSessionDataOctetsSent_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 4, 1, 9),
    _AlActiveSessionDataOctetsSent_Type()
)
alActiveSessionDataOctetsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alActiveSessionDataOctetsSent.setStatus("current")
_AlActiveSessionDataOctetsRcvd_Type = Counter32
_AlActiveSessionDataOctetsRcvd_Object = MibTableColumn
alActiveSessionDataOctetsRcvd = _AlActiveSessionDataOctetsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 4, 1, 10),
    _AlActiveSessionDataOctetsRcvd_Type()
)
alActiveSessionDataOctetsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alActiveSessionDataOctetsRcvd.setStatus("current")
_AlActiveSessionDataSepId_Type = Integer32
_AlActiveSessionDataSepId_Object = MibTableColumn
alActiveSessionDataSepId = _AlActiveSessionDataSepId_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 4, 1, 11),
    _AlActiveSessionDataSepId_Type()
)
alActiveSessionDataSepId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alActiveSessionDataSepId.setStatus("current")
_AlActiveSessionDataGroupName_Type = DisplayString
_AlActiveSessionDataGroupName_Object = MibTableColumn
alActiveSessionDataGroupName = _AlActiveSessionDataGroupName_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 4, 1, 12),
    _AlActiveSessionDataGroupName_Type()
)
alActiveSessionDataGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alActiveSessionDataGroupName.setStatus("current")
_AlActiveSessionDataGroupId_Type = Integer32
_AlActiveSessionDataGroupId_Object = MibTableColumn
alActiveSessionDataGroupId = _AlActiveSessionDataGroupId_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 4, 1, 13),
    _AlActiveSessionDataGroupId_Type()
)
alActiveSessionDataGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alActiveSessionDataGroupId.setStatus("current")
_AlActiveSessionDataPublicIpAddress_Type = IpAddress
_AlActiveSessionDataPublicIpAddress_Object = MibTableColumn
alActiveSessionDataPublicIpAddress = _AlActiveSessionDataPublicIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 4, 1, 14),
    _AlActiveSessionDataPublicIpAddress_Type()
)
alActiveSessionDataPublicIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alActiveSessionDataPublicIpAddress.setStatus("current")
_AlActiveSessionDataTopTenData_Type = Gauge32
_AlActiveSessionDataTopTenData_Object = MibTableColumn
alActiveSessionDataTopTenData = _AlActiveSessionDataTopTenData_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 4, 1, 15),
    _AlActiveSessionDataTopTenData_Type()
)
alActiveSessionDataTopTenData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alActiveSessionDataTopTenData.setStatus("current")
_AlActiveSessionDataLoginTime_Type = Unsigned32
_AlActiveSessionDataLoginTime_Object = MibTableColumn
alActiveSessionDataLoginTime = _AlActiveSessionDataLoginTime_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 4, 1, 16),
    _AlActiveSessionDataLoginTime_Type()
)
alActiveSessionDataLoginTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alActiveSessionDataLoginTime.setStatus("current")
_AlActiveSessionDurationTable_Object = MibTable
alActiveSessionDurationTable = _AlActiveSessionDurationTable_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 5)
)
if mibBuilder.loadTexts:
    alActiveSessionDurationTable.setStatus("current")
_AlActiveSessionDurationEntry_Object = MibTableRow
alActiveSessionDurationEntry = _AlActiveSessionDurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 5, 1)
)
alActiveSessionDurationEntry.setIndexNames(
    (0, "ALTIGA-SESSION-STATS-MIB", "alActiveSessionDurationIndex"),
)
if mibBuilder.loadTexts:
    alActiveSessionDurationEntry.setStatus("current")
_AlActiveSessionDurationRowStatus_Type = RowStatus
_AlActiveSessionDurationRowStatus_Object = MibTableColumn
alActiveSessionDurationRowStatus = _AlActiveSessionDurationRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 5, 1, 1),
    _AlActiveSessionDurationRowStatus_Type()
)
alActiveSessionDurationRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alActiveSessionDurationRowStatus.setStatus("current")


class _AlActiveSessionDurationIndex_Type(Integer32):
    """Custom type alActiveSessionDurationIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_AlActiveSessionDurationIndex_Type.__name__ = "Integer32"
_AlActiveSessionDurationIndex_Object = MibTableColumn
alActiveSessionDurationIndex = _AlActiveSessionDurationIndex_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 5, 1, 2),
    _AlActiveSessionDurationIndex_Type()
)
alActiveSessionDurationIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alActiveSessionDurationIndex.setStatus("current")
_AlActiveSessionDurationUserName_Type = DisplayString
_AlActiveSessionDurationUserName_Object = MibTableColumn
alActiveSessionDurationUserName = _AlActiveSessionDurationUserName_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 5, 1, 3),
    _AlActiveSessionDurationUserName_Type()
)
alActiveSessionDurationUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alActiveSessionDurationUserName.setStatus("current")
_AlActiveSessionDurationIpAddress_Type = IpAddress
_AlActiveSessionDurationIpAddress_Object = MibTableColumn
alActiveSessionDurationIpAddress = _AlActiveSessionDurationIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 5, 1, 4),
    _AlActiveSessionDurationIpAddress_Type()
)
alActiveSessionDurationIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alActiveSessionDurationIpAddress.setStatus("current")
_AlActiveSessionDurationProtocol_Type = SessionProtocol
_AlActiveSessionDurationProtocol_Object = MibTableColumn
alActiveSessionDurationProtocol = _AlActiveSessionDurationProtocol_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 5, 1, 5),
    _AlActiveSessionDurationProtocol_Type()
)
alActiveSessionDurationProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alActiveSessionDurationProtocol.setStatus("current")
_AlActiveSessionDurationEncrType_Type = EncryptionAlgorithm
_AlActiveSessionDurationEncrType_Object = MibTableColumn
alActiveSessionDurationEncrType = _AlActiveSessionDurationEncrType_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 5, 1, 6),
    _AlActiveSessionDurationEncrType_Type()
)
alActiveSessionDurationEncrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alActiveSessionDurationEncrType.setStatus("current")
_AlActiveSessionDurationStartTime_Type = TimeTicks
_AlActiveSessionDurationStartTime_Object = MibTableColumn
alActiveSessionDurationStartTime = _AlActiveSessionDurationStartTime_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 5, 1, 7),
    _AlActiveSessionDurationStartTime_Type()
)
alActiveSessionDurationStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alActiveSessionDurationStartTime.setStatus("current")
_AlActiveSessionDurationConnectTime_Type = Counter32
_AlActiveSessionDurationConnectTime_Object = MibTableColumn
alActiveSessionDurationConnectTime = _AlActiveSessionDurationConnectTime_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 5, 1, 8),
    _AlActiveSessionDurationConnectTime_Type()
)
alActiveSessionDurationConnectTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alActiveSessionDurationConnectTime.setStatus("current")
_AlActiveSessionDurationOctetsSent_Type = Counter32
_AlActiveSessionDurationOctetsSent_Object = MibTableColumn
alActiveSessionDurationOctetsSent = _AlActiveSessionDurationOctetsSent_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 5, 1, 9),
    _AlActiveSessionDurationOctetsSent_Type()
)
alActiveSessionDurationOctetsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alActiveSessionDurationOctetsSent.setStatus("current")
_AlActiveSessionDurationOctetsRcvd_Type = Counter32
_AlActiveSessionDurationOctetsRcvd_Object = MibTableColumn
alActiveSessionDurationOctetsRcvd = _AlActiveSessionDurationOctetsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 5, 1, 10),
    _AlActiveSessionDurationOctetsRcvd_Type()
)
alActiveSessionDurationOctetsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alActiveSessionDurationOctetsRcvd.setStatus("current")
_AlActiveSessionDurationSepId_Type = Integer32
_AlActiveSessionDurationSepId_Object = MibTableColumn
alActiveSessionDurationSepId = _AlActiveSessionDurationSepId_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 5, 1, 11),
    _AlActiveSessionDurationSepId_Type()
)
alActiveSessionDurationSepId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alActiveSessionDurationSepId.setStatus("current")
_AlActiveSessionDurationGroupName_Type = DisplayString
_AlActiveSessionDurationGroupName_Object = MibTableColumn
alActiveSessionDurationGroupName = _AlActiveSessionDurationGroupName_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 5, 1, 12),
    _AlActiveSessionDurationGroupName_Type()
)
alActiveSessionDurationGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alActiveSessionDurationGroupName.setStatus("current")
_AlActiveSessionDurationGroupId_Type = Integer32
_AlActiveSessionDurationGroupId_Object = MibTableColumn
alActiveSessionDurationGroupId = _AlActiveSessionDurationGroupId_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 5, 1, 13),
    _AlActiveSessionDurationGroupId_Type()
)
alActiveSessionDurationGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alActiveSessionDurationGroupId.setStatus("current")
_AlActiveSessionDurationPublicIpAddress_Type = IpAddress
_AlActiveSessionDurationPublicIpAddress_Object = MibTableColumn
alActiveSessionDurationPublicIpAddress = _AlActiveSessionDurationPublicIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 5, 1, 14),
    _AlActiveSessionDurationPublicIpAddress_Type()
)
alActiveSessionDurationPublicIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alActiveSessionDurationPublicIpAddress.setStatus("current")
_AlActiveSessionDurationTopTenData_Type = Gauge32
_AlActiveSessionDurationTopTenData_Object = MibTableColumn
alActiveSessionDurationTopTenData = _AlActiveSessionDurationTopTenData_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 5, 1, 15),
    _AlActiveSessionDurationTopTenData_Type()
)
alActiveSessionDurationTopTenData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alActiveSessionDurationTopTenData.setStatus("current")
_AlActiveSessionDurationLoginTime_Type = Unsigned32
_AlActiveSessionDurationLoginTime_Object = MibTableColumn
alActiveSessionDurationLoginTime = _AlActiveSessionDurationLoginTime_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 5, 1, 16),
    _AlActiveSessionDurationLoginTime_Type()
)
alActiveSessionDurationLoginTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alActiveSessionDurationLoginTime.setStatus("current")
_AlActiveSessionSubTable_Object = MibTable
alActiveSessionSubTable = _AlActiveSessionSubTable_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 6)
)
if mibBuilder.loadTexts:
    alActiveSessionSubTable.setStatus("current")
_AlActiveSessionSubEntry_Object = MibTableRow
alActiveSessionSubEntry = _AlActiveSessionSubEntry_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 6, 1)
)
alActiveSessionSubEntry.setIndexNames(
    (0, "ALTIGA-SESSION-STATS-MIB", "alActiveSessionSubEntryIndex"),
    (0, "ALTIGA-SESSION-STATS-MIB", "alActiveSessionSubEntryInstance"),
)
if mibBuilder.loadTexts:
    alActiveSessionSubEntry.setStatus("current")
_AlActiveSessionSubEntryRowStatus_Type = RowStatus
_AlActiveSessionSubEntryRowStatus_Object = MibTableColumn
alActiveSessionSubEntryRowStatus = _AlActiveSessionSubEntryRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 6, 1, 1),
    _AlActiveSessionSubEntryRowStatus_Type()
)
alActiveSessionSubEntryRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alActiveSessionSubEntryRowStatus.setStatus("current")


class _AlActiveSessionSubEntryIndex_Type(Integer32):
    """Custom type alActiveSessionSubEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_AlActiveSessionSubEntryIndex_Type.__name__ = "Integer32"
_AlActiveSessionSubEntryIndex_Object = MibTableColumn
alActiveSessionSubEntryIndex = _AlActiveSessionSubEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 6, 1, 2),
    _AlActiveSessionSubEntryIndex_Type()
)
alActiveSessionSubEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alActiveSessionSubEntryIndex.setStatus("current")


class _AlActiveSessionSubEntryInstance_Type(Integer32):
    """Custom type alActiveSessionSubEntryInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_AlActiveSessionSubEntryInstance_Type.__name__ = "Integer32"
_AlActiveSessionSubEntryInstance_Object = MibTableColumn
alActiveSessionSubEntryInstance = _AlActiveSessionSubEntryInstance_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 6, 1, 3),
    _AlActiveSessionSubEntryInstance_Type()
)
alActiveSessionSubEntryInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alActiveSessionSubEntryInstance.setStatus("current")
_AlActiveSessionSubEntryProtocol_Type = SessionProtocol
_AlActiveSessionSubEntryProtocol_Object = MibTableColumn
alActiveSessionSubEntryProtocol = _AlActiveSessionSubEntryProtocol_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 6, 1, 4),
    _AlActiveSessionSubEntryProtocol_Type()
)
alActiveSessionSubEntryProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alActiveSessionSubEntryProtocol.setStatus("current")
_AlActiveSessionSubEntryEncrAlg_Type = EncryptionAlgorithm
_AlActiveSessionSubEntryEncrAlg_Object = MibTableColumn
alActiveSessionSubEntryEncrAlg = _AlActiveSessionSubEntryEncrAlg_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 6, 1, 5),
    _AlActiveSessionSubEntryEncrAlg_Type()
)
alActiveSessionSubEntryEncrAlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alActiveSessionSubEntryEncrAlg.setStatus("current")


class _AlActiveSessionSubEntryHashAlg_Type(Integer32):
    """Custom type alActiveSessionSubEntryHashAlg based on Integer32"""
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
          ("sha1", 2))
    )


_AlActiveSessionSubEntryHashAlg_Type.__name__ = "Integer32"
_AlActiveSessionSubEntryHashAlg_Object = MibTableColumn
alActiveSessionSubEntryHashAlg = _AlActiveSessionSubEntryHashAlg_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 6, 1, 6),
    _AlActiveSessionSubEntryHashAlg_Type()
)
alActiveSessionSubEntryHashAlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alActiveSessionSubEntryHashAlg.setStatus("current")


class _AlActiveSessionSubEntryDiffHelmanGrp_Type(Integer32):
    """Custom type alActiveSessionSubEntryDiffHelmanGrp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              7)
        )
    )
    namedValues = NamedValues(
        *(("group1", 1),
          ("group2", 2),
          ("group3", 3),
          ("group4", 4),
          ("group5", 5),
          ("group7", 7),
          ("none", 0))
    )


_AlActiveSessionSubEntryDiffHelmanGrp_Type.__name__ = "Integer32"
_AlActiveSessionSubEntryDiffHelmanGrp_Object = MibTableColumn
alActiveSessionSubEntryDiffHelmanGrp = _AlActiveSessionSubEntryDiffHelmanGrp_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 6, 1, 7),
    _AlActiveSessionSubEntryDiffHelmanGrp_Type()
)
alActiveSessionSubEntryDiffHelmanGrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alActiveSessionSubEntryDiffHelmanGrp.setStatus("current")


class _AlActiveSessionSubEntryAuthMode_Type(Integer32):
    """Custom type alActiveSessionSubEntryAuthMode based on Integer32"""
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
              14,
              15,
              16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("chap", 5),
          ("crack", 17),
          ("dsaCert", 3),
          ("dsaCertHybrid", 16),
          ("dsaCertXauth", 12),
          ("eap", 13),
          ("eapGtc", 7),
          ("eapMd5", 6),
          ("msChapV1", 8),
          ("msChapV2", 9),
          ("none", 0),
          ("pap", 4),
          ("preSharedKeys", 1),
          ("preSharedKeysXauth", 10),
          ("rsaCert", 2),
          ("rsaCertHybrid", 15),
          ("rsaCertXauth", 11),
          ("usernamePassword", 14))
    )


_AlActiveSessionSubEntryAuthMode_Type.__name__ = "Integer32"
_AlActiveSessionSubEntryAuthMode_Object = MibTableColumn
alActiveSessionSubEntryAuthMode = _AlActiveSessionSubEntryAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 6, 1, 8),
    _AlActiveSessionSubEntryAuthMode_Type()
)
alActiveSessionSubEntryAuthMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alActiveSessionSubEntryAuthMode.setStatus("current")


class _AlActiveSessionSubEntryEncapMode_Type(Integer32):
    """Custom type alActiveSessionSubEntryEncapMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("transport", 1),
          ("tunnel", 2))
    )


_AlActiveSessionSubEntryEncapMode_Type.__name__ = "Integer32"
_AlActiveSessionSubEntryEncapMode_Object = MibTableColumn
alActiveSessionSubEntryEncapMode = _AlActiveSessionSubEntryEncapMode_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 6, 1, 9),
    _AlActiveSessionSubEntryEncapMode_Type()
)
alActiveSessionSubEntryEncapMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alActiveSessionSubEntryEncapMode.setStatus("current")
_AlActiveSessionSubEntryRekeyTime_Type = Unsigned32
_AlActiveSessionSubEntryRekeyTime_Object = MibTableColumn
alActiveSessionSubEntryRekeyTime = _AlActiveSessionSubEntryRekeyTime_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 6, 1, 10),
    _AlActiveSessionSubEntryRekeyTime_Type()
)
alActiveSessionSubEntryRekeyTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alActiveSessionSubEntryRekeyTime.setStatus("current")
_AlActiveSessionSubEntryRekeyKBytes_Type = Unsigned32
_AlActiveSessionSubEntryRekeyKBytes_Object = MibTableColumn
alActiveSessionSubEntryRekeyKBytes = _AlActiveSessionSubEntryRekeyKBytes_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 6, 1, 11),
    _AlActiveSessionSubEntryRekeyKBytes_Type()
)
alActiveSessionSubEntryRekeyKBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alActiveSessionSubEntryRekeyKBytes.setStatus("current")


class _AlActiveSessionSubEntryRemAddrType_Type(Integer32):
    """Custom type alActiveSessionSubEntryRemAddrType based on Integer32"""
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
        *(("addrWithSubNet", 1),
          ("hostAddress", 3),
          ("none", 0),
          ("range", 2))
    )


_AlActiveSessionSubEntryRemAddrType_Type.__name__ = "Integer32"
_AlActiveSessionSubEntryRemAddrType_Object = MibTableColumn
alActiveSessionSubEntryRemAddrType = _AlActiveSessionSubEntryRemAddrType_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 6, 1, 12),
    _AlActiveSessionSubEntryRemAddrType_Type()
)
alActiveSessionSubEntryRemAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alActiveSessionSubEntryRemAddrType.setStatus("current")
_AlActiveSessionSubEntryRemAddr1_Type = IpAddress
_AlActiveSessionSubEntryRemAddr1_Object = MibTableColumn
alActiveSessionSubEntryRemAddr1 = _AlActiveSessionSubEntryRemAddr1_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 6, 1, 13),
    _AlActiveSessionSubEntryRemAddr1_Type()
)
alActiveSessionSubEntryRemAddr1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alActiveSessionSubEntryRemAddr1.setStatus("current")
_AlActiveSessionSubEntryRemAddr2_Type = IpAddress
_AlActiveSessionSubEntryRemAddr2_Object = MibTableColumn
alActiveSessionSubEntryRemAddr2 = _AlActiveSessionSubEntryRemAddr2_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 6, 1, 14),
    _AlActiveSessionSubEntryRemAddr2_Type()
)
alActiveSessionSubEntryRemAddr2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alActiveSessionSubEntryRemAddr2.setStatus("current")


class _AlActiveSessionSubEntryLocAddrType_Type(Integer32):
    """Custom type alActiveSessionSubEntryLocAddrType based on Integer32"""
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
        *(("addrWithSubNet", 1),
          ("hostAddress", 3),
          ("none", 0),
          ("range", 2))
    )


_AlActiveSessionSubEntryLocAddrType_Type.__name__ = "Integer32"
_AlActiveSessionSubEntryLocAddrType_Object = MibTableColumn
alActiveSessionSubEntryLocAddrType = _AlActiveSessionSubEntryLocAddrType_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 6, 1, 15),
    _AlActiveSessionSubEntryLocAddrType_Type()
)
alActiveSessionSubEntryLocAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alActiveSessionSubEntryLocAddrType.setStatus("current")
_AlActiveSessionSubEntryLocAddr1_Type = IpAddress
_AlActiveSessionSubEntryLocAddr1_Object = MibTableColumn
alActiveSessionSubEntryLocAddr1 = _AlActiveSessionSubEntryLocAddr1_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 6, 1, 16),
    _AlActiveSessionSubEntryLocAddr1_Type()
)
alActiveSessionSubEntryLocAddr1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alActiveSessionSubEntryLocAddr1.setStatus("current")
_AlActiveSessionSubEntryLocAddr2_Type = IpAddress
_AlActiveSessionSubEntryLocAddr2_Object = MibTableColumn
alActiveSessionSubEntryLocAddr2 = _AlActiveSessionSubEntryLocAddr2_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 6, 1, 17),
    _AlActiveSessionSubEntryLocAddr2_Type()
)
alActiveSessionSubEntryLocAddr2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alActiveSessionSubEntryLocAddr2.setStatus("current")
_AlActiveSessionSubEntryRcvdOctets_Type = Counter32
_AlActiveSessionSubEntryRcvdOctets_Object = MibTableColumn
alActiveSessionSubEntryRcvdOctets = _AlActiveSessionSubEntryRcvdOctets_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 6, 1, 18),
    _AlActiveSessionSubEntryRcvdOctets_Type()
)
alActiveSessionSubEntryRcvdOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alActiveSessionSubEntryRcvdOctets.setStatus("current")
_AlActiveSessionSubEntrySentOctets_Type = Counter32
_AlActiveSessionSubEntrySentOctets_Object = MibTableColumn
alActiveSessionSubEntrySentOctets = _AlActiveSessionSubEntrySentOctets_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 6, 1, 19),
    _AlActiveSessionSubEntrySentOctets_Type()
)
alActiveSessionSubEntrySentOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alActiveSessionSubEntrySentOctets.setStatus("current")
_AlActiveSessionSubEntrySep_Type = Integer32
_AlActiveSessionSubEntrySep_Object = MibTableColumn
alActiveSessionSubEntrySep = _AlActiveSessionSubEntrySep_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 6, 1, 20),
    _AlActiveSessionSubEntrySep_Type()
)
alActiveSessionSubEntrySep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alActiveSessionSubEntrySep.setStatus("current")
_AlActiveSessionSubEntryUserName_Type = DisplayString
_AlActiveSessionSubEntryUserName_Object = MibTableColumn
alActiveSessionSubEntryUserName = _AlActiveSessionSubEntryUserName_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 6, 1, 21),
    _AlActiveSessionSubEntryUserName_Type()
)
alActiveSessionSubEntryUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alActiveSessionSubEntryUserName.setStatus("current")
_AlActiveSessionSubEntryClientIpAddr_Type = IpAddress
_AlActiveSessionSubEntryClientIpAddr_Object = MibTableColumn
alActiveSessionSubEntryClientIpAddr = _AlActiveSessionSubEntryClientIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 6, 1, 22),
    _AlActiveSessionSubEntryClientIpAddr_Type()
)
alActiveSessionSubEntryClientIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alActiveSessionSubEntryClientIpAddr.setStatus("current")


class _AlActiveSessionSubEntryUdpPort_Type(Integer32):
    """Custom type alActiveSessionSubEntryUdpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlActiveSessionSubEntryUdpPort_Type.__name__ = "Integer32"
_AlActiveSessionSubEntryUdpPort_Object = MibTableColumn
alActiveSessionSubEntryUdpPort = _AlActiveSessionSubEntryUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 6, 1, 23),
    _AlActiveSessionSubEntryUdpPort_Type()
)
alActiveSessionSubEntryUdpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alActiveSessionSubEntryUdpPort.setStatus("current")
_AlActiveSessionSubEntryTotalIdleTime_Type = Counter32
_AlActiveSessionSubEntryTotalIdleTime_Object = MibTableColumn
alActiveSessionSubEntryTotalIdleTime = _AlActiveSessionSubEntryTotalIdleTime_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 6, 1, 24),
    _AlActiveSessionSubEntryTotalIdleTime_Type()
)
alActiveSessionSubEntryTotalIdleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alActiveSessionSubEntryTotalIdleTime.setStatus("current")


class _AlActiveSessionSubEntryIkeNegMode_Type(Integer32):
    """Custom type alActiveSessionSubEntryIkeNegMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aggressive", 2),
          ("main", 1),
          ("none", 0))
    )


_AlActiveSessionSubEntryIkeNegMode_Type.__name__ = "Integer32"
_AlActiveSessionSubEntryIkeNegMode_Object = MibTableColumn
alActiveSessionSubEntryIkeNegMode = _AlActiveSessionSubEntryIkeNegMode_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 6, 1, 25),
    _AlActiveSessionSubEntryIkeNegMode_Type()
)
alActiveSessionSubEntryIkeNegMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alActiveSessionSubEntryIkeNegMode.setStatus("current")
_AlActiveSessionSubEntryCompression_Type = CompressionAlgorithm
_AlActiveSessionSubEntryCompression_Object = MibTableColumn
alActiveSessionSubEntryCompression = _AlActiveSessionSubEntryCompression_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 6, 1, 26),
    _AlActiveSessionSubEntryCompression_Type()
)
alActiveSessionSubEntryCompression.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alActiveSessionSubEntryCompression.setStatus("current")
_AlActiveSessionSubEntryInstId_Type = Integer32
_AlActiveSessionSubEntryInstId_Object = MibTableColumn
alActiveSessionSubEntryInstId = _AlActiveSessionSubEntryInstId_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 6, 1, 27),
    _AlActiveSessionSubEntryInstId_Type()
)
alActiveSessionSubEntryInstId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alActiveSessionSubEntryInstId.setStatus("current")


class _AlActiveSessionSubEntryPfsGroup_Type(Integer32):
    """Custom type alActiveSessionSubEntryPfsGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              7)
        )
    )
    namedValues = NamedValues(
        *(("group1", 1),
          ("group2", 2),
          ("group3", 3),
          ("group4", 4),
          ("group7", 7),
          ("none", 0))
    )


_AlActiveSessionSubEntryPfsGroup_Type.__name__ = "Integer32"
_AlActiveSessionSubEntryPfsGroup_Object = MibTableColumn
alActiveSessionSubEntryPfsGroup = _AlActiveSessionSubEntryPfsGroup_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 6, 1, 28),
    _AlActiveSessionSubEntryPfsGroup_Type()
)
alActiveSessionSubEntryPfsGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alActiveSessionSubEntryPfsGroup.setStatus("current")


class _AlActiveSessionSubEntryTcpSrcPort_Type(Integer32):
    """Custom type alActiveSessionSubEntryTcpSrcPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlActiveSessionSubEntryTcpSrcPort_Type.__name__ = "Integer32"
_AlActiveSessionSubEntryTcpSrcPort_Object = MibTableColumn
alActiveSessionSubEntryTcpSrcPort = _AlActiveSessionSubEntryTcpSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 6, 1, 29),
    _AlActiveSessionSubEntryTcpSrcPort_Type()
)
alActiveSessionSubEntryTcpSrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alActiveSessionSubEntryTcpSrcPort.setStatus("current")


class _AlActiveSessionSubEntryTcpDstPort_Type(Integer32):
    """Custom type alActiveSessionSubEntryTcpDstPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlActiveSessionSubEntryTcpDstPort_Type.__name__ = "Integer32"
_AlActiveSessionSubEntryTcpDstPort_Object = MibTableColumn
alActiveSessionSubEntryTcpDstPort = _AlActiveSessionSubEntryTcpDstPort_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 6, 1, 30),
    _AlActiveSessionSubEntryTcpDstPort_Type()
)
alActiveSessionSubEntryTcpDstPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alActiveSessionSubEntryTcpDstPort.setStatus("current")


class _AlActiveSessionSubEntryUdpSrcPort_Type(Integer32):
    """Custom type alActiveSessionSubEntryUdpSrcPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlActiveSessionSubEntryUdpSrcPort_Type.__name__ = "Integer32"
_AlActiveSessionSubEntryUdpSrcPort_Object = MibTableColumn
alActiveSessionSubEntryUdpSrcPort = _AlActiveSessionSubEntryUdpSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 6, 1, 31),
    _AlActiveSessionSubEntryUdpSrcPort_Type()
)
alActiveSessionSubEntryUdpSrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alActiveSessionSubEntryUdpSrcPort.setStatus("current")


class _AlActiveSessionSubEntryIkeUdpSrcPort_Type(Integer32):
    """Custom type alActiveSessionSubEntryIkeUdpSrcPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlActiveSessionSubEntryIkeUdpSrcPort_Type.__name__ = "Integer32"
_AlActiveSessionSubEntryIkeUdpSrcPort_Object = MibTableColumn
alActiveSessionSubEntryIkeUdpSrcPort = _AlActiveSessionSubEntryIkeUdpSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 6, 1, 32),
    _AlActiveSessionSubEntryIkeUdpSrcPort_Type()
)
alActiveSessionSubEntryIkeUdpSrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alActiveSessionSubEntryIkeUdpSrcPort.setStatus("current")


class _AlActiveSessionSubEntryIkeUdpDstPort_Type(Integer32):
    """Custom type alActiveSessionSubEntryIkeUdpDstPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlActiveSessionSubEntryIkeUdpDstPort_Type.__name__ = "Integer32"
_AlActiveSessionSubEntryIkeUdpDstPort_Object = MibTableColumn
alActiveSessionSubEntryIkeUdpDstPort = _AlActiveSessionSubEntryIkeUdpDstPort_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 6, 1, 33),
    _AlActiveSessionSubEntryIkeUdpDstPort_Type()
)
alActiveSessionSubEntryIkeUdpDstPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alActiveSessionSubEntryIkeUdpDstPort.setStatus("current")


class _AlActiveSessionSubEntryNacRevalTimer_Type(Integer32):
    """Custom type alActiveSessionSubEntryNacRevalTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_AlActiveSessionSubEntryNacRevalTimer_Type.__name__ = "Integer32"
_AlActiveSessionSubEntryNacRevalTimer_Object = MibTableColumn
alActiveSessionSubEntryNacRevalTimer = _AlActiveSessionSubEntryNacRevalTimer_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 6, 1, 34),
    _AlActiveSessionSubEntryNacRevalTimer_Type()
)
alActiveSessionSubEntryNacRevalTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alActiveSessionSubEntryNacRevalTimer.setStatus("current")
if mibBuilder.loadTexts:
    alActiveSessionSubEntryNacRevalTimer.setUnits("seconds")


class _AlActiveSessionSubEntryNacTimetoReval_Type(Integer32):
    """Custom type alActiveSessionSubEntryNacTimetoReval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_AlActiveSessionSubEntryNacTimetoReval_Type.__name__ = "Integer32"
_AlActiveSessionSubEntryNacTimetoReval_Object = MibTableColumn
alActiveSessionSubEntryNacTimetoReval = _AlActiveSessionSubEntryNacTimetoReval_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 6, 1, 35),
    _AlActiveSessionSubEntryNacTimetoReval_Type()
)
alActiveSessionSubEntryNacTimetoReval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alActiveSessionSubEntryNacTimetoReval.setStatus("current")
if mibBuilder.loadTexts:
    alActiveSessionSubEntryNacTimetoReval.setUnits("seconds")


class _AlActiveSessionSubEntryNacSqTimer_Type(Integer32):
    """Custom type alActiveSessionSubEntryNacSqTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1800),
    )


_AlActiveSessionSubEntryNacSqTimer_Type.__name__ = "Integer32"
_AlActiveSessionSubEntryNacSqTimer_Object = MibTableColumn
alActiveSessionSubEntryNacSqTimer = _AlActiveSessionSubEntryNacSqTimer_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 6, 1, 36),
    _AlActiveSessionSubEntryNacSqTimer_Type()
)
alActiveSessionSubEntryNacSqTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alActiveSessionSubEntryNacSqTimer.setStatus("current")
if mibBuilder.loadTexts:
    alActiveSessionSubEntryNacSqTimer.setUnits("seconds")


class _AlActiveSessionSubEntryNacSessionAge_Type(Integer32):
    """Custom type alActiveSessionSubEntryNacSessionAge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_AlActiveSessionSubEntryNacSessionAge_Type.__name__ = "Integer32"
_AlActiveSessionSubEntryNacSessionAge_Object = MibTableColumn
alActiveSessionSubEntryNacSessionAge = _AlActiveSessionSubEntryNacSessionAge_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 6, 1, 37),
    _AlActiveSessionSubEntryNacSessionAge_Type()
)
alActiveSessionSubEntryNacSessionAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alActiveSessionSubEntryNacSessionAge.setStatus("current")
if mibBuilder.loadTexts:
    alActiveSessionSubEntryNacSessionAge.setUnits("seconds")
_AlActiveSessionSubEntryNacPosture_Type = DisplayString
_AlActiveSessionSubEntryNacPosture_Object = MibTableColumn
alActiveSessionSubEntryNacPosture = _AlActiveSessionSubEntryNacPosture_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 6, 1, 38),
    _AlActiveSessionSubEntryNacPosture_Type()
)
alActiveSessionSubEntryNacPosture.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alActiveSessionSubEntryNacPosture.setStatus("current")
_AlActiveSessionSubEntryNacRedirectUrl_Type = DisplayString
_AlActiveSessionSubEntryNacRedirectUrl_Object = MibTableColumn
alActiveSessionSubEntryNacRedirectUrl = _AlActiveSessionSubEntryNacRedirectUrl_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 6, 1, 39),
    _AlActiveSessionSubEntryNacRedirectUrl_Type()
)
alActiveSessionSubEntryNacRedirectUrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alActiveSessionSubEntryNacRedirectUrl.setStatus("current")


class _AlActiveSessionSubEntryNacHoldTimer_Type(Integer32):
    """Custom type alActiveSessionSubEntryNacHoldTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_AlActiveSessionSubEntryNacHoldTimer_Type.__name__ = "Integer32"
_AlActiveSessionSubEntryNacHoldTimer_Object = MibTableColumn
alActiveSessionSubEntryNacHoldTimer = _AlActiveSessionSubEntryNacHoldTimer_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 6, 1, 40),
    _AlActiveSessionSubEntryNacHoldTimer_Type()
)
alActiveSessionSubEntryNacHoldTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alActiveSessionSubEntryNacHoldTimer.setStatus("current")
if mibBuilder.loadTexts:
    alActiveSessionSubEntryNacHoldTimer.setUnits("seconds")
_AlActiveHWClientUserTable_Object = MibTable
alActiveHWClientUserTable = _AlActiveHWClientUserTable_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 7)
)
if mibBuilder.loadTexts:
    alActiveHWClientUserTable.setStatus("current")
_AlActiveHWClientUserEntry_Object = MibTableRow
alActiveHWClientUserEntry = _AlActiveHWClientUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 7, 1)
)
alActiveHWClientUserEntry.setIndexNames(
    (0, "ALTIGA-SESSION-STATS-MIB", "alActiveHWClientUserSessionIndex"),
    (0, "ALTIGA-SESSION-STATS-MIB", "alActiveHWClientUserIpAddr"),
)
if mibBuilder.loadTexts:
    alActiveHWClientUserEntry.setStatus("current")
_AlActiveHWClientUserRowStatus_Type = RowStatus
_AlActiveHWClientUserRowStatus_Object = MibTableColumn
alActiveHWClientUserRowStatus = _AlActiveHWClientUserRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 7, 1, 1),
    _AlActiveHWClientUserRowStatus_Type()
)
alActiveHWClientUserRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alActiveHWClientUserRowStatus.setStatus("current")


class _AlActiveHWClientUserSessionIndex_Type(Integer32):
    """Custom type alActiveHWClientUserSessionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_AlActiveHWClientUserSessionIndex_Type.__name__ = "Integer32"
_AlActiveHWClientUserSessionIndex_Object = MibTableColumn
alActiveHWClientUserSessionIndex = _AlActiveHWClientUserSessionIndex_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 7, 1, 2),
    _AlActiveHWClientUserSessionIndex_Type()
)
alActiveHWClientUserSessionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alActiveHWClientUserSessionIndex.setStatus("current")
_AlActiveHWClientUserIpAddr_Type = IpAddress
_AlActiveHWClientUserIpAddr_Object = MibTableColumn
alActiveHWClientUserIpAddr = _AlActiveHWClientUserIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 7, 1, 3),
    _AlActiveHWClientUserIpAddr_Type()
)
alActiveHWClientUserIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alActiveHWClientUserIpAddr.setStatus("current")
_AlActiveHWClientUserName_Type = DisplayString
_AlActiveHWClientUserName_Object = MibTableColumn
alActiveHWClientUserName = _AlActiveHWClientUserName_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 7, 1, 4),
    _AlActiveHWClientUserName_Type()
)
alActiveHWClientUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alActiveHWClientUserName.setStatus("current")
_AlActiveHWClientUserMacAddr_Type = MacAddress
_AlActiveHWClientUserMacAddr_Object = MibTableColumn
alActiveHWClientUserMacAddr = _AlActiveHWClientUserMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 7, 1, 5),
    _AlActiveHWClientUserMacAddr_Type()
)
alActiveHWClientUserMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alActiveHWClientUserMacAddr.setStatus("current")
_AlActiveHWClientUserLoginTime_Type = Unsigned32
_AlActiveHWClientUserLoginTime_Object = MibTableColumn
alActiveHWClientUserLoginTime = _AlActiveHWClientUserLoginTime_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 7, 1, 6),
    _AlActiveHWClientUserLoginTime_Type()
)
alActiveHWClientUserLoginTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alActiveHWClientUserLoginTime.setStatus("current")
_AlActiveHWClientUserUpTime_Type = TimeTicks
_AlActiveHWClientUserUpTime_Object = MibTableColumn
alActiveHWClientUserUpTime = _AlActiveHWClientUserUpTime_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 17, 7, 1, 7),
    _AlActiveHWClientUserUpTime_Type()
)
alActiveHWClientUserUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alActiveHWClientUserUpTime.setStatus("current")

# Managed Objects groups

altigaSessionStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1, 17, 2)
)
altigaSessionStatsGroup.setObjects(
      *(("ALTIGA-SESSION-STATS-MIB", "alActiveSessionCount"),
        ("ALTIGA-SESSION-STATS-MIB", "alTotalSessionCount"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionLastUpdate"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionMaxUsers"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionGroupIdLock"),
        ("ALTIGA-SESSION-STATS-MIB", "alMaxSessionCount"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveLanToLanSessionCount"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveManagementSessionCount"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveRemoteAccessSessionCount"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionRowStatus"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionIndex"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionUserName"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionIpAddress"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionProtocol"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionEncrType"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionStartTime"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionConnectTime"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionOctetsSent"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionOctetsRcvd"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionSepId"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionGroupName"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionGroupId"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionPublicIpAddress"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionTopTenData"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionLoginTime"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionOS"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionVersion"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionThroughputRowStatus"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionThroughputIndex"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionThroughputUserName"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionThroughputIpAddress"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionThroughputProtocol"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionThroughputEncrType"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionThroughputStartTime"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionThroughputConnectTime"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionThroughputOctetsSent"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionThroughputOctetsRcvd"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionThroughputSepId"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionThroughputGroupName"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionThroughputGroupId"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionThroughputPublicIpAddress"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionThroughputTopTenData"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionThroughputLoginTime"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionDataRowStatus"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionDataIndex"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionDataUserName"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionDataIpAddress"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionDataProtocol"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionDataEncrType"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionDataStartTime"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionDataConnectTime"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionDataOctetsSent"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionDataOctetsRcvd"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionDataSepId"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionDataGroupName"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionDataGroupId"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionDataPublicIpAddress"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionDataTopTenData"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionDataLoginTime"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionDurationRowStatus"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionDurationIndex"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionDurationUserName"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionDurationIpAddress"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionDurationProtocol"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionDurationEncrType"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionDurationStartTime"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionDurationConnectTime"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionDurationOctetsSent"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionDurationOctetsRcvd"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionDurationSepId"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionDurationGroupName"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionDurationGroupId"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionDurationPublicIpAddress"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionDurationTopTenData"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionDurationLoginTime"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionSubEntryRowStatus"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionSubEntryIndex"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionSubEntryInstance"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionSubEntryProtocol"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionSubEntryEncrAlg"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionSubEntryHashAlg"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionSubEntryDiffHelmanGrp"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionSubEntryAuthMode"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionSubEntryEncapMode"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionSubEntryRekeyTime"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionSubEntryRekeyKBytes"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionSubEntryRemAddrType"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionSubEntryRemAddr1"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionSubEntryRemAddr2"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionSubEntryLocAddrType"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionSubEntryLocAddr1"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionSubEntryLocAddr2"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionSubEntryRcvdOctets"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionSubEntrySentOctets"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionSubEntrySep"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionSubEntryUserName"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionSubEntryClientIpAddr"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionSubEntryUdpPort"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionSubEntryTotalIdleTime"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionSubEntryIkeNegMode"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionSubEntryCompression"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionSubEntryInstId"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionSubEntryPfsGroup"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionSubEntryTcpSrcPort"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionSubEntryTcpDstPort"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionSubEntryUdpSrcPort"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionSubEntryIkeUdpSrcPort"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionSubEntryIkeUdpDstPort"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveHWClientUserRowStatus"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveHWClientUserSessionIndex"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveHWClientUserName"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveHWClientUserIpAddr"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveHWClientUserMacAddr"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveHWClientUserLoginTime"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveHWClientUserUpTime"))
)
if mibBuilder.loadTexts:
    altigaSessionStatsGroup.setStatus("deprecated")

altigaSessionStatsGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1, 17, 3)
)
altigaSessionStatsGroupRev1.setObjects(
      *(("ALTIGA-SESSION-STATS-MIB", "alActiveSessionCount"),
        ("ALTIGA-SESSION-STATS-MIB", "alTotalSessionCount"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionLastUpdate"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionMaxUsers"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionGroupIdLock"),
        ("ALTIGA-SESSION-STATS-MIB", "alMaxSessionCount"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveLanToLanSessionCount"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveManagementSessionCount"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveRemoteAccessSessionCount"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionRowStatus"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionIndex"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionUserName"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionIpAddress"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionProtocol"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionEncrType"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionStartTime"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionConnectTime"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionOctetsSent"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionOctetsRcvd"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionSepId"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionGroupName"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionGroupId"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionPublicIpAddress"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionTopTenData"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionLoginTime"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionOS"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionVersion"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionFilterId"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionThroughputRowStatus"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionThroughputIndex"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionThroughputUserName"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionThroughputIpAddress"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionThroughputProtocol"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionThroughputEncrType"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionThroughputStartTime"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionThroughputConnectTime"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionThroughputOctetsSent"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionThroughputOctetsRcvd"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionThroughputSepId"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionThroughputGroupName"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionThroughputGroupId"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionThroughputPublicIpAddress"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionThroughputTopTenData"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionThroughputLoginTime"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionDataRowStatus"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionDataIndex"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionDataUserName"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionDataIpAddress"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionDataProtocol"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionDataEncrType"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionDataStartTime"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionDataConnectTime"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionDataOctetsSent"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionDataOctetsRcvd"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionDataSepId"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionDataGroupName"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionDataGroupId"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionDataPublicIpAddress"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionDataTopTenData"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionDataLoginTime"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionDurationRowStatus"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionDurationIndex"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionDurationUserName"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionDurationIpAddress"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionDurationProtocol"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionDurationEncrType"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionDurationStartTime"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionDurationConnectTime"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionDurationOctetsSent"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionDurationOctetsRcvd"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionDurationSepId"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionDurationGroupName"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionDurationGroupId"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionDurationPublicIpAddress"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionDurationTopTenData"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionDurationLoginTime"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionSubEntryRowStatus"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionSubEntryIndex"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionSubEntryInstance"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionSubEntryProtocol"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionSubEntryEncrAlg"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionSubEntryHashAlg"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionSubEntryDiffHelmanGrp"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionSubEntryAuthMode"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionSubEntryEncapMode"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionSubEntryRekeyTime"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionSubEntryRekeyKBytes"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionSubEntryRemAddrType"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionSubEntryRemAddr1"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionSubEntryRemAddr2"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionSubEntryLocAddrType"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionSubEntryLocAddr1"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionSubEntryLocAddr2"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionSubEntryRcvdOctets"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionSubEntrySentOctets"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionSubEntrySep"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionSubEntryUserName"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionSubEntryClientIpAddr"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionSubEntryUdpPort"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionSubEntryTotalIdleTime"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionSubEntryIkeNegMode"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionSubEntryCompression"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionSubEntryInstId"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionSubEntryPfsGroup"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionSubEntryTcpSrcPort"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionSubEntryTcpDstPort"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionSubEntryUdpSrcPort"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionSubEntryIkeUdpSrcPort"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionSubEntryIkeUdpDstPort"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveHWClientUserRowStatus"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveHWClientUserSessionIndex"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveHWClientUserName"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveHWClientUserIpAddr"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveHWClientUserMacAddr"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveHWClientUserLoginTime"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveHWClientUserUpTime"))
)
if mibBuilder.loadTexts:
    altigaSessionStatsGroupRev1.setStatus("deprecated")

altigaSessionStatsGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1, 17, 4)
)
altigaSessionStatsGroupRev2.setObjects(
      *(("ALTIGA-SESSION-STATS-MIB", "alActiveSessionCount"),
        ("ALTIGA-SESSION-STATS-MIB", "alTotalSessionCount"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionLastUpdate"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionMaxUsers"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionGroupIdLock"),
        ("ALTIGA-SESSION-STATS-MIB", "alMaxSessionCount"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveLanToLanSessionCount"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveManagementSessionCount"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveRemoteAccessSessionCount"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionRowStatus"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionIndex"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionUserName"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionIpAddress"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionProtocol"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionEncrType"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionStartTime"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionConnectTime"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionOctetsSent"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionOctetsRcvd"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionSepId"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionGroupName"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionGroupId"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionPublicIpAddress"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionTopTenData"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionLoginTime"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionOS"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionVersion"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionFilterId"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionThroughputRowStatus"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionThroughputIndex"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionThroughputUserName"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionThroughputIpAddress"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionThroughputProtocol"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionThroughputEncrType"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionThroughputStartTime"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionThroughputConnectTime"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionThroughputOctetsSent"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionThroughputOctetsRcvd"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionThroughputSepId"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionThroughputGroupName"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionThroughputGroupId"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionThroughputPublicIpAddress"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionThroughputTopTenData"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionThroughputLoginTime"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionDataRowStatus"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionDataIndex"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionDataUserName"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionDataIpAddress"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionDataProtocol"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionDataEncrType"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionDataStartTime"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionDataConnectTime"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionDataOctetsSent"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionDataOctetsRcvd"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionDataSepId"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionDataGroupName"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionDataGroupId"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionDataPublicIpAddress"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionDataTopTenData"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionDataLoginTime"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionDurationRowStatus"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionDurationIndex"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionDurationUserName"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionDurationIpAddress"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionDurationProtocol"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionDurationEncrType"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionDurationStartTime"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionDurationConnectTime"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionDurationOctetsSent"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionDurationOctetsRcvd"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionDurationSepId"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionDurationGroupName"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionDurationGroupId"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionDurationPublicIpAddress"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionDurationTopTenData"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionDurationLoginTime"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionSubEntryRowStatus"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionSubEntryIndex"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionSubEntryInstance"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionSubEntryProtocol"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionSubEntryEncrAlg"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionSubEntryHashAlg"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionSubEntryDiffHelmanGrp"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionSubEntryAuthMode"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionSubEntryEncapMode"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionSubEntryRekeyTime"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionSubEntryRekeyKBytes"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionSubEntryRemAddrType"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionSubEntryRemAddr1"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionSubEntryRemAddr2"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionSubEntryLocAddrType"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionSubEntryLocAddr1"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionSubEntryLocAddr2"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionSubEntryRcvdOctets"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionSubEntrySentOctets"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionSubEntrySep"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionSubEntryUserName"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionSubEntryClientIpAddr"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionSubEntryUdpPort"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionSubEntryTotalIdleTime"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionSubEntryIkeNegMode"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionSubEntryCompression"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionSubEntryInstId"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionSubEntryPfsGroup"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionSubEntryTcpSrcPort"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionSubEntryTcpDstPort"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionSubEntryUdpSrcPort"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionSubEntryIkeUdpSrcPort"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionSubEntryIkeUdpDstPort"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveHWClientUserRowStatus"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveHWClientUserSessionIndex"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveHWClientUserName"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveHWClientUserIpAddr"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveHWClientUserMacAddr"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveHWClientUserLoginTime"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveHWClientUserUpTime"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionMaxWebVpnUsers"),
        ("ALTIGA-SESSION-STATS-MIB", "alWeightedSessionCount"))
)
if mibBuilder.loadTexts:
    altigaSessionStatsGroupRev2.setStatus("current")

altigaSessionStatsGroupRev2Sup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1, 17, 5)
)
altigaSessionStatsGroupRev2Sup1.setObjects(
      *(("ALTIGA-SESSION-STATS-MIB", "alActiveSessionNacResult"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionSubEntryNacRevalTimer"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionSubEntryNacTimetoReval"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionSubEntryNacSqTimer"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionSubEntryNacSessionAge"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionSubEntryNacPosture"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionSubEntryNacRedirectUrl"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveSessionSubEntryNacHoldTimer"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveNacAcceptedSessions"),
        ("ALTIGA-SESSION-STATS-MIB", "alTotalNacAcceptedSessions"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveNacRejectedSessions"),
        ("ALTIGA-SESSION-STATS-MIB", "alTotalNacRejectedSessions"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveNacExemptedSessions"),
        ("ALTIGA-SESSION-STATS-MIB", "alTotalNacExemptedSessions"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveNacNonresponsiveSessions"),
        ("ALTIGA-SESSION-STATS-MIB", "alTotalNacNonresponsiveSessions"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveNacDisabledSessions"),
        ("ALTIGA-SESSION-STATS-MIB", "alTotalNacDisabledSessions"),
        ("ALTIGA-SESSION-STATS-MIB", "alActiveNacHoldoffSessions"),
        ("ALTIGA-SESSION-STATS-MIB", "alTotalNacHoldoffSessions"))
)
if mibBuilder.loadTexts:
    altigaSessionStatsGroupRev2Sup1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

altigaSessionStatsMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 22, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    altigaSessionStatsMibCompliance.setStatus(
        "deprecated"
    )

altigaSessionStatsMibComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 22, 2, 1, 1, 2)
)
if mibBuilder.loadTexts:
    altigaSessionStatsMibComplianceRev1.setStatus(
        "deprecated"
    )

altigaSessionStatsMibComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 22, 2, 1, 1, 3)
)
if mibBuilder.loadTexts:
    altigaSessionStatsMibComplianceRev2.setStatus(
        "deprecated"
    )

altigaSessionStatsMibComplianceRev3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 22, 2, 1, 1, 4)
)
if mibBuilder.loadTexts:
    altigaSessionStatsMibComplianceRev3.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALTIGA-SESSION-STATS-MIB",
    **{"SessionProtocol": SessionProtocol,
       "EncryptionAlgorithm": EncryptionAlgorithm,
       "CompressionAlgorithm": CompressionAlgorithm,
       "NacResult": NacResult,
       "altigaSessionStatsMibModule": altigaSessionStatsMibModule,
       "altigaSessionStatsMibConformance": altigaSessionStatsMibConformance,
       "altigaSessionStatsMibCompliances": altigaSessionStatsMibCompliances,
       "altigaSessionStatsMibCompliance": altigaSessionStatsMibCompliance,
       "altigaSessionStatsMibComplianceRev1": altigaSessionStatsMibComplianceRev1,
       "altigaSessionStatsMibComplianceRev2": altigaSessionStatsMibComplianceRev2,
       "altigaSessionStatsMibComplianceRev3": altigaSessionStatsMibComplianceRev3,
       "altigaSessionStatsGroup": altigaSessionStatsGroup,
       "altigaSessionStatsGroupRev1": altigaSessionStatsGroupRev1,
       "altigaSessionStatsGroupRev2": altigaSessionStatsGroupRev2,
       "altigaSessionStatsGroupRev2Sup1": altigaSessionStatsGroupRev2Sup1,
       "alStatsSessionGlobal": alStatsSessionGlobal,
       "alActiveSessionCount": alActiveSessionCount,
       "alTotalSessionCount": alTotalSessionCount,
       "alActiveSessionLastUpdate": alActiveSessionLastUpdate,
       "alActiveSessionMaxUsers": alActiveSessionMaxUsers,
       "alActiveSessionGroupIdLock": alActiveSessionGroupIdLock,
       "alMaxSessionCount": alMaxSessionCount,
       "alActiveLanToLanSessionCount": alActiveLanToLanSessionCount,
       "alActiveManagementSessionCount": alActiveManagementSessionCount,
       "alActiveRemoteAccessSessionCount": alActiveRemoteAccessSessionCount,
       "alActiveSessionMaxWebVpnUsers": alActiveSessionMaxWebVpnUsers,
       "alWeightedSessionCount": alWeightedSessionCount,
       "alActiveNacAcceptedSessions": alActiveNacAcceptedSessions,
       "alTotalNacAcceptedSessions": alTotalNacAcceptedSessions,
       "alActiveNacRejectedSessions": alActiveNacRejectedSessions,
       "alTotalNacRejectedSessions": alTotalNacRejectedSessions,
       "alActiveNacExemptedSessions": alActiveNacExemptedSessions,
       "alTotalNacExemptedSessions": alTotalNacExemptedSessions,
       "alActiveNacNonresponsiveSessions": alActiveNacNonresponsiveSessions,
       "alTotalNacNonresponsiveSessions": alTotalNacNonresponsiveSessions,
       "alActiveNacDisabledSessions": alActiveNacDisabledSessions,
       "alTotalNacDisabledSessions": alTotalNacDisabledSessions,
       "alActiveNacHoldoffSessions": alActiveNacHoldoffSessions,
       "alTotalNacHoldoffSessions": alTotalNacHoldoffSessions,
       "alActiveSessionTable": alActiveSessionTable,
       "alActiveSessionEntry": alActiveSessionEntry,
       "alActiveSessionRowStatus": alActiveSessionRowStatus,
       "alActiveSessionIndex": alActiveSessionIndex,
       "alActiveSessionUserName": alActiveSessionUserName,
       "alActiveSessionIpAddress": alActiveSessionIpAddress,
       "alActiveSessionProtocol": alActiveSessionProtocol,
       "alActiveSessionEncrType": alActiveSessionEncrType,
       "alActiveSessionStartTime": alActiveSessionStartTime,
       "alActiveSessionConnectTime": alActiveSessionConnectTime,
       "alActiveSessionOctetsSent": alActiveSessionOctetsSent,
       "alActiveSessionOctetsRcvd": alActiveSessionOctetsRcvd,
       "alActiveSessionSepId": alActiveSessionSepId,
       "alActiveSessionGroupName": alActiveSessionGroupName,
       "alActiveSessionGroupId": alActiveSessionGroupId,
       "alActiveSessionPublicIpAddress": alActiveSessionPublicIpAddress,
       "alActiveSessionTopTenData": alActiveSessionTopTenData,
       "alActiveSessionLoginTime": alActiveSessionLoginTime,
       "alActiveSessionOS": alActiveSessionOS,
       "alActiveSessionVersion": alActiveSessionVersion,
       "alActiveSessionFilterId": alActiveSessionFilterId,
       "alActiveSessionNacResult": alActiveSessionNacResult,
       "alActiveSessionThroughputTable": alActiveSessionThroughputTable,
       "alActiveSessionThroughputEntry": alActiveSessionThroughputEntry,
       "alActiveSessionThroughputRowStatus": alActiveSessionThroughputRowStatus,
       "alActiveSessionThroughputIndex": alActiveSessionThroughputIndex,
       "alActiveSessionThroughputUserName": alActiveSessionThroughputUserName,
       "alActiveSessionThroughputIpAddress": alActiveSessionThroughputIpAddress,
       "alActiveSessionThroughputProtocol": alActiveSessionThroughputProtocol,
       "alActiveSessionThroughputEncrType": alActiveSessionThroughputEncrType,
       "alActiveSessionThroughputStartTime": alActiveSessionThroughputStartTime,
       "alActiveSessionThroughputConnectTime": alActiveSessionThroughputConnectTime,
       "alActiveSessionThroughputOctetsSent": alActiveSessionThroughputOctetsSent,
       "alActiveSessionThroughputOctetsRcvd": alActiveSessionThroughputOctetsRcvd,
       "alActiveSessionThroughputSepId": alActiveSessionThroughputSepId,
       "alActiveSessionThroughputGroupName": alActiveSessionThroughputGroupName,
       "alActiveSessionThroughputGroupId": alActiveSessionThroughputGroupId,
       "alActiveSessionThroughputPublicIpAddress": alActiveSessionThroughputPublicIpAddress,
       "alActiveSessionThroughputTopTenData": alActiveSessionThroughputTopTenData,
       "alActiveSessionThroughputLoginTime": alActiveSessionThroughputLoginTime,
       "alActiveSessionDataTable": alActiveSessionDataTable,
       "alActiveSessionDataEntry": alActiveSessionDataEntry,
       "alActiveSessionDataRowStatus": alActiveSessionDataRowStatus,
       "alActiveSessionDataIndex": alActiveSessionDataIndex,
       "alActiveSessionDataUserName": alActiveSessionDataUserName,
       "alActiveSessionDataIpAddress": alActiveSessionDataIpAddress,
       "alActiveSessionDataProtocol": alActiveSessionDataProtocol,
       "alActiveSessionDataEncrType": alActiveSessionDataEncrType,
       "alActiveSessionDataStartTime": alActiveSessionDataStartTime,
       "alActiveSessionDataConnectTime": alActiveSessionDataConnectTime,
       "alActiveSessionDataOctetsSent": alActiveSessionDataOctetsSent,
       "alActiveSessionDataOctetsRcvd": alActiveSessionDataOctetsRcvd,
       "alActiveSessionDataSepId": alActiveSessionDataSepId,
       "alActiveSessionDataGroupName": alActiveSessionDataGroupName,
       "alActiveSessionDataGroupId": alActiveSessionDataGroupId,
       "alActiveSessionDataPublicIpAddress": alActiveSessionDataPublicIpAddress,
       "alActiveSessionDataTopTenData": alActiveSessionDataTopTenData,
       "alActiveSessionDataLoginTime": alActiveSessionDataLoginTime,
       "alActiveSessionDurationTable": alActiveSessionDurationTable,
       "alActiveSessionDurationEntry": alActiveSessionDurationEntry,
       "alActiveSessionDurationRowStatus": alActiveSessionDurationRowStatus,
       "alActiveSessionDurationIndex": alActiveSessionDurationIndex,
       "alActiveSessionDurationUserName": alActiveSessionDurationUserName,
       "alActiveSessionDurationIpAddress": alActiveSessionDurationIpAddress,
       "alActiveSessionDurationProtocol": alActiveSessionDurationProtocol,
       "alActiveSessionDurationEncrType": alActiveSessionDurationEncrType,
       "alActiveSessionDurationStartTime": alActiveSessionDurationStartTime,
       "alActiveSessionDurationConnectTime": alActiveSessionDurationConnectTime,
       "alActiveSessionDurationOctetsSent": alActiveSessionDurationOctetsSent,
       "alActiveSessionDurationOctetsRcvd": alActiveSessionDurationOctetsRcvd,
       "alActiveSessionDurationSepId": alActiveSessionDurationSepId,
       "alActiveSessionDurationGroupName": alActiveSessionDurationGroupName,
       "alActiveSessionDurationGroupId": alActiveSessionDurationGroupId,
       "alActiveSessionDurationPublicIpAddress": alActiveSessionDurationPublicIpAddress,
       "alActiveSessionDurationTopTenData": alActiveSessionDurationTopTenData,
       "alActiveSessionDurationLoginTime": alActiveSessionDurationLoginTime,
       "alActiveSessionSubTable": alActiveSessionSubTable,
       "alActiveSessionSubEntry": alActiveSessionSubEntry,
       "alActiveSessionSubEntryRowStatus": alActiveSessionSubEntryRowStatus,
       "alActiveSessionSubEntryIndex": alActiveSessionSubEntryIndex,
       "alActiveSessionSubEntryInstance": alActiveSessionSubEntryInstance,
       "alActiveSessionSubEntryProtocol": alActiveSessionSubEntryProtocol,
       "alActiveSessionSubEntryEncrAlg": alActiveSessionSubEntryEncrAlg,
       "alActiveSessionSubEntryHashAlg": alActiveSessionSubEntryHashAlg,
       "alActiveSessionSubEntryDiffHelmanGrp": alActiveSessionSubEntryDiffHelmanGrp,
       "alActiveSessionSubEntryAuthMode": alActiveSessionSubEntryAuthMode,
       "alActiveSessionSubEntryEncapMode": alActiveSessionSubEntryEncapMode,
       "alActiveSessionSubEntryRekeyTime": alActiveSessionSubEntryRekeyTime,
       "alActiveSessionSubEntryRekeyKBytes": alActiveSessionSubEntryRekeyKBytes,
       "alActiveSessionSubEntryRemAddrType": alActiveSessionSubEntryRemAddrType,
       "alActiveSessionSubEntryRemAddr1": alActiveSessionSubEntryRemAddr1,
       "alActiveSessionSubEntryRemAddr2": alActiveSessionSubEntryRemAddr2,
       "alActiveSessionSubEntryLocAddrType": alActiveSessionSubEntryLocAddrType,
       "alActiveSessionSubEntryLocAddr1": alActiveSessionSubEntryLocAddr1,
       "alActiveSessionSubEntryLocAddr2": alActiveSessionSubEntryLocAddr2,
       "alActiveSessionSubEntryRcvdOctets": alActiveSessionSubEntryRcvdOctets,
       "alActiveSessionSubEntrySentOctets": alActiveSessionSubEntrySentOctets,
       "alActiveSessionSubEntrySep": alActiveSessionSubEntrySep,
       "alActiveSessionSubEntryUserName": alActiveSessionSubEntryUserName,
       "alActiveSessionSubEntryClientIpAddr": alActiveSessionSubEntryClientIpAddr,
       "alActiveSessionSubEntryUdpPort": alActiveSessionSubEntryUdpPort,
       "alActiveSessionSubEntryTotalIdleTime": alActiveSessionSubEntryTotalIdleTime,
       "alActiveSessionSubEntryIkeNegMode": alActiveSessionSubEntryIkeNegMode,
       "alActiveSessionSubEntryCompression": alActiveSessionSubEntryCompression,
       "alActiveSessionSubEntryInstId": alActiveSessionSubEntryInstId,
       "alActiveSessionSubEntryPfsGroup": alActiveSessionSubEntryPfsGroup,
       "alActiveSessionSubEntryTcpSrcPort": alActiveSessionSubEntryTcpSrcPort,
       "alActiveSessionSubEntryTcpDstPort": alActiveSessionSubEntryTcpDstPort,
       "alActiveSessionSubEntryUdpSrcPort": alActiveSessionSubEntryUdpSrcPort,
       "alActiveSessionSubEntryIkeUdpSrcPort": alActiveSessionSubEntryIkeUdpSrcPort,
       "alActiveSessionSubEntryIkeUdpDstPort": alActiveSessionSubEntryIkeUdpDstPort,
       "alActiveSessionSubEntryNacRevalTimer": alActiveSessionSubEntryNacRevalTimer,
       "alActiveSessionSubEntryNacTimetoReval": alActiveSessionSubEntryNacTimetoReval,
       "alActiveSessionSubEntryNacSqTimer": alActiveSessionSubEntryNacSqTimer,
       "alActiveSessionSubEntryNacSessionAge": alActiveSessionSubEntryNacSessionAge,
       "alActiveSessionSubEntryNacPosture": alActiveSessionSubEntryNacPosture,
       "alActiveSessionSubEntryNacRedirectUrl": alActiveSessionSubEntryNacRedirectUrl,
       "alActiveSessionSubEntryNacHoldTimer": alActiveSessionSubEntryNacHoldTimer,
       "alActiveHWClientUserTable": alActiveHWClientUserTable,
       "alActiveHWClientUserEntry": alActiveHWClientUserEntry,
       "alActiveHWClientUserRowStatus": alActiveHWClientUserRowStatus,
       "alActiveHWClientUserSessionIndex": alActiveHWClientUserSessionIndex,
       "alActiveHWClientUserIpAddr": alActiveHWClientUserIpAddr,
       "alActiveHWClientUserName": alActiveHWClientUserName,
       "alActiveHWClientUserMacAddr": alActiveHWClientUserMacAddr,
       "alActiveHWClientUserLoginTime": alActiveHWClientUserLoginTime,
       "alActiveHWClientUserUpTime": alActiveHWClientUserUpTime}
)
