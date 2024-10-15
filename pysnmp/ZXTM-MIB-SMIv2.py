# SNMP MIB module (ZXTM-MIB-SMIv2) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZXTM-MIB-SMIv2
# Produced by pysmi-1.5.4 at Mon Oct 14 23:21:16 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

zxtm = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2)
)
zxtm.setRevisions(
        ("2016-12-05 11:00",
         "2016-09-29 01:00",
         "2016-05-09 19:00",
         "2015-11-18 09:00",
         "2015-11-16 17:03",
         "2015-11-09 09:00",
         "2015-09-23 14:00",
         "2015-07-07 15:00",
         "2015-06-16 14:00",
         "2015-01-23 14:00",
         "2014-12-04 11:00",
         "2014-10-29 11:00",
         "2014-09-21 10:00",
         "2014-08-19 12:00",
         "2014-07-01 14:00",
         "2014-02-24 17:00",
         "2014-02-03 16:00",
         "2014-02-03 11:00",
         "2013-11-11 11:00",
         "2011-11-22 11:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Zeus_ObjectIdentity = ObjectIdentity
zeus = _Zeus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7146)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7146, 1)
)
_Globals_ObjectIdentity = ObjectIdentity
globals = _Globals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1)
)


class _Version_Type(DisplayString):
    """Custom type version based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Version_Type.__name__ = "DisplayString"
_Version_Object = MibScalar
version = _Version_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 1),
    _Version_Type()
)
version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    version.setStatus("current")
_NumberChildProcesses_Type = Integer32
_NumberChildProcesses_Object = MibScalar
numberChildProcesses = _NumberChildProcesses_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 2),
    _NumberChildProcesses_Type()
)
numberChildProcesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numberChildProcesses.setStatus("current")
_UpTime_Type = TimeTicks
_UpTime_Object = MibScalar
upTime = _UpTime_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 3),
    _UpTime_Type()
)
upTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upTime.setStatus("current")
_TimeLastConfigUpdate_Type = TimeTicks
_TimeLastConfigUpdate_Object = MibScalar
timeLastConfigUpdate = _TimeLastConfigUpdate_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 4),
    _TimeLastConfigUpdate_Type()
)
timeLastConfigUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timeLastConfigUpdate.setStatus("current")
_TotalBytesInLo_Type = Counter32
_TotalBytesInLo_Object = MibScalar
totalBytesInLo = _TotalBytesInLo_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 5),
    _TotalBytesInLo_Type()
)
totalBytesInLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalBytesInLo.setStatus("obsolete")
_TotalBytesInHi_Type = Counter32
_TotalBytesInHi_Object = MibScalar
totalBytesInHi = _TotalBytesInHi_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 6),
    _TotalBytesInHi_Type()
)
totalBytesInHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalBytesInHi.setStatus("obsolete")
_TotalBytesOutLo_Type = Counter32
_TotalBytesOutLo_Object = MibScalar
totalBytesOutLo = _TotalBytesOutLo_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 7),
    _TotalBytesOutLo_Type()
)
totalBytesOutLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalBytesOutLo.setStatus("obsolete")
_TotalBytesOutHi_Type = Counter32
_TotalBytesOutHi_Object = MibScalar
totalBytesOutHi = _TotalBytesOutHi_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 8),
    _TotalBytesOutHi_Type()
)
totalBytesOutHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalBytesOutHi.setStatus("obsolete")
_TotalCurrentConn_Type = Gauge32
_TotalCurrentConn_Object = MibScalar
totalCurrentConn = _TotalCurrentConn_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 9),
    _TotalCurrentConn_Type()
)
totalCurrentConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalCurrentConn.setStatus("current")
_TotalConn_Type = Counter32
_TotalConn_Object = MibScalar
totalConn = _TotalConn_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 10),
    _TotalConn_Type()
)
totalConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalConn.setStatus("current")
_NumberDNSARequests_Type = Counter32
_NumberDNSARequests_Object = MibScalar
numberDNSARequests = _NumberDNSARequests_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 11),
    _NumberDNSARequests_Type()
)
numberDNSARequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numberDNSARequests.setStatus("current")
_NumberDNSACacheHits_Type = Counter32
_NumberDNSACacheHits_Object = MibScalar
numberDNSACacheHits = _NumberDNSACacheHits_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 12),
    _NumberDNSACacheHits_Type()
)
numberDNSACacheHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numberDNSACacheHits.setStatus("current")
_NumberDNSPTRRequests_Type = Counter32
_NumberDNSPTRRequests_Object = MibScalar
numberDNSPTRRequests = _NumberDNSPTRRequests_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 13),
    _NumberDNSPTRRequests_Type()
)
numberDNSPTRRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numberDNSPTRRequests.setStatus("current")
_NumberDNSPTRCacheHits_Type = Counter32
_NumberDNSPTRCacheHits_Object = MibScalar
numberDNSPTRCacheHits = _NumberDNSPTRCacheHits_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 14),
    _NumberDNSPTRCacheHits_Type()
)
numberDNSPTRCacheHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numberDNSPTRCacheHits.setStatus("current")
_NumberSNMPUnauthorisedRequests_Type = Counter32
_NumberSNMPUnauthorisedRequests_Object = MibScalar
numberSNMPUnauthorisedRequests = _NumberSNMPUnauthorisedRequests_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 15),
    _NumberSNMPUnauthorisedRequests_Type()
)
numberSNMPUnauthorisedRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numberSNMPUnauthorisedRequests.setStatus("current")
_NumberSNMPBadRequests_Type = Counter32
_NumberSNMPBadRequests_Object = MibScalar
numberSNMPBadRequests = _NumberSNMPBadRequests_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 16),
    _NumberSNMPBadRequests_Type()
)
numberSNMPBadRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numberSNMPBadRequests.setStatus("current")
_NumberSNMPGetRequests_Type = Counter32
_NumberSNMPGetRequests_Object = MibScalar
numberSNMPGetRequests = _NumberSNMPGetRequests_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 17),
    _NumberSNMPGetRequests_Type()
)
numberSNMPGetRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numberSNMPGetRequests.setStatus("current")
_NumberSNMPGetNextRequests_Type = Counter32
_NumberSNMPGetNextRequests_Object = MibScalar
numberSNMPGetNextRequests = _NumberSNMPGetNextRequests_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 18),
    _NumberSNMPGetNextRequests_Type()
)
numberSNMPGetNextRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numberSNMPGetNextRequests.setStatus("current")
_SslCipherEncrypts_Type = Counter32
_SslCipherEncrypts_Object = MibScalar
sslCipherEncrypts = _SslCipherEncrypts_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 19),
    _SslCipherEncrypts_Type()
)
sslCipherEncrypts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslCipherEncrypts.setStatus("current")
_SslCipherDecrypts_Type = Counter32
_SslCipherDecrypts_Object = MibScalar
sslCipherDecrypts = _SslCipherDecrypts_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 20),
    _SslCipherDecrypts_Type()
)
sslCipherDecrypts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslCipherDecrypts.setStatus("current")
_SslCipherRC4Encrypts_Type = Counter32
_SslCipherRC4Encrypts_Object = MibScalar
sslCipherRC4Encrypts = _SslCipherRC4Encrypts_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 21),
    _SslCipherRC4Encrypts_Type()
)
sslCipherRC4Encrypts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslCipherRC4Encrypts.setStatus("current")
_SslCipherRC4Decrypts_Type = Counter32
_SslCipherRC4Decrypts_Object = MibScalar
sslCipherRC4Decrypts = _SslCipherRC4Decrypts_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 22),
    _SslCipherRC4Decrypts_Type()
)
sslCipherRC4Decrypts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslCipherRC4Decrypts.setStatus("current")
_SslCipherDESEncrypts_Type = Counter32
_SslCipherDESEncrypts_Object = MibScalar
sslCipherDESEncrypts = _SslCipherDESEncrypts_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 23),
    _SslCipherDESEncrypts_Type()
)
sslCipherDESEncrypts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslCipherDESEncrypts.setStatus("current")
_SslCipherDESDecrypts_Type = Counter32
_SslCipherDESDecrypts_Object = MibScalar
sslCipherDESDecrypts = _SslCipherDESDecrypts_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 24),
    _SslCipherDESDecrypts_Type()
)
sslCipherDESDecrypts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslCipherDESDecrypts.setStatus("current")
_SslCipher3DESEncrypts_Type = Counter32
_SslCipher3DESEncrypts_Object = MibScalar
sslCipher3DESEncrypts = _SslCipher3DESEncrypts_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 25),
    _SslCipher3DESEncrypts_Type()
)
sslCipher3DESEncrypts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslCipher3DESEncrypts.setStatus("current")
_SslCipher3DESDecrypts_Type = Counter32
_SslCipher3DESDecrypts_Object = MibScalar
sslCipher3DESDecrypts = _SslCipher3DESDecrypts_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 26),
    _SslCipher3DESDecrypts_Type()
)
sslCipher3DESDecrypts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslCipher3DESDecrypts.setStatus("current")
_SslCipherAESEncrypts_Type = Counter32
_SslCipherAESEncrypts_Object = MibScalar
sslCipherAESEncrypts = _SslCipherAESEncrypts_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 27),
    _SslCipherAESEncrypts_Type()
)
sslCipherAESEncrypts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslCipherAESEncrypts.setStatus("current")
_SslCipherAESDecrypts_Type = Counter32
_SslCipherAESDecrypts_Object = MibScalar
sslCipherAESDecrypts = _SslCipherAESDecrypts_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 28),
    _SslCipherAESDecrypts_Type()
)
sslCipherAESDecrypts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslCipherAESDecrypts.setStatus("current")
_SslCipherRSAEncrypts_Type = Counter32
_SslCipherRSAEncrypts_Object = MibScalar
sslCipherRSAEncrypts = _SslCipherRSAEncrypts_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 29),
    _SslCipherRSAEncrypts_Type()
)
sslCipherRSAEncrypts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslCipherRSAEncrypts.setStatus("current")
_SslCipherRSADecrypts_Type = Counter32
_SslCipherRSADecrypts_Object = MibScalar
sslCipherRSADecrypts = _SslCipherRSADecrypts_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 30),
    _SslCipherRSADecrypts_Type()
)
sslCipherRSADecrypts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslCipherRSADecrypts.setStatus("current")
_SslCipherRSADecryptsExternal_Type = Counter32
_SslCipherRSADecryptsExternal_Object = MibScalar
sslCipherRSADecryptsExternal = _SslCipherRSADecryptsExternal_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 31),
    _SslCipherRSADecryptsExternal_Type()
)
sslCipherRSADecryptsExternal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslCipherRSADecryptsExternal.setStatus("current")
_SslHandshakeSSLv2_Type = Counter32
_SslHandshakeSSLv2_Object = MibScalar
sslHandshakeSSLv2 = _SslHandshakeSSLv2_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 32),
    _SslHandshakeSSLv2_Type()
)
sslHandshakeSSLv2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslHandshakeSSLv2.setStatus("obsolete")
_SslHandshakeSSLv3_Type = Counter32
_SslHandshakeSSLv3_Object = MibScalar
sslHandshakeSSLv3 = _SslHandshakeSSLv3_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 33),
    _SslHandshakeSSLv3_Type()
)
sslHandshakeSSLv3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslHandshakeSSLv3.setStatus("current")
_SslHandshakeTLSv1_Type = Counter32
_SslHandshakeTLSv1_Object = MibScalar
sslHandshakeTLSv1 = _SslHandshakeTLSv1_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 34),
    _SslHandshakeTLSv1_Type()
)
sslHandshakeTLSv1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslHandshakeTLSv1.setStatus("current")
_SslClientCertNotSent_Type = Counter32
_SslClientCertNotSent_Object = MibScalar
sslClientCertNotSent = _SslClientCertNotSent_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 35),
    _SslClientCertNotSent_Type()
)
sslClientCertNotSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslClientCertNotSent.setStatus("current")
_SslClientCertInvalid_Type = Counter32
_SslClientCertInvalid_Object = MibScalar
sslClientCertInvalid = _SslClientCertInvalid_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 36),
    _SslClientCertInvalid_Type()
)
sslClientCertInvalid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslClientCertInvalid.setStatus("current")
_SslClientCertExpired_Type = Counter32
_SslClientCertExpired_Object = MibScalar
sslClientCertExpired = _SslClientCertExpired_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 37),
    _SslClientCertExpired_Type()
)
sslClientCertExpired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslClientCertExpired.setStatus("current")
_SslClientCertRevoked_Type = Counter32
_SslClientCertRevoked_Object = MibScalar
sslClientCertRevoked = _SslClientCertRevoked_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 38),
    _SslClientCertRevoked_Type()
)
sslClientCertRevoked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslClientCertRevoked.setStatus("current")
_SslSessionIDMemCacheHit_Type = Counter32
_SslSessionIDMemCacheHit_Object = MibScalar
sslSessionIDMemCacheHit = _SslSessionIDMemCacheHit_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 39),
    _SslSessionIDMemCacheHit_Type()
)
sslSessionIDMemCacheHit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslSessionIDMemCacheHit.setStatus("current")
_SslSessionIDMemCacheMiss_Type = Counter32
_SslSessionIDMemCacheMiss_Object = MibScalar
sslSessionIDMemCacheMiss = _SslSessionIDMemCacheMiss_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 40),
    _SslSessionIDMemCacheMiss_Type()
)
sslSessionIDMemCacheMiss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslSessionIDMemCacheMiss.setStatus("current")
_SslSessionIDDiskCacheHit_Type = Counter32
_SslSessionIDDiskCacheHit_Object = MibScalar
sslSessionIDDiskCacheHit = _SslSessionIDDiskCacheHit_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 41),
    _SslSessionIDDiskCacheHit_Type()
)
sslSessionIDDiskCacheHit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslSessionIDDiskCacheHit.setStatus("deprecated")
_SslSessionIDDiskCacheMiss_Type = Counter32
_SslSessionIDDiskCacheMiss_Object = MibScalar
sslSessionIDDiskCacheMiss = _SslSessionIDDiskCacheMiss_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 42),
    _SslSessionIDDiskCacheMiss_Type()
)
sslSessionIDDiskCacheMiss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslSessionIDDiskCacheMiss.setStatus("deprecated")
_SslHandshakeTLSv11_Type = Counter32
_SslHandshakeTLSv11_Object = MibScalar
sslHandshakeTLSv11 = _SslHandshakeTLSv11_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 43),
    _SslHandshakeTLSv11_Type()
)
sslHandshakeTLSv11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslHandshakeTLSv11.setStatus("current")
_SslConnections_Type = Counter32
_SslConnections_Object = MibScalar
sslConnections = _SslConnections_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 44),
    _SslConnections_Type()
)
sslConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslConnections.setStatus("current")
_SysCPUIdlePercent_Type = Gauge32
_SysCPUIdlePercent_Object = MibScalar
sysCPUIdlePercent = _SysCPUIdlePercent_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 45),
    _SysCPUIdlePercent_Type()
)
sysCPUIdlePercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysCPUIdlePercent.setStatus("current")
_SysCPUBusyPercent_Type = Gauge32
_SysCPUBusyPercent_Object = MibScalar
sysCPUBusyPercent = _SysCPUBusyPercent_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 46),
    _SysCPUBusyPercent_Type()
)
sysCPUBusyPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysCPUBusyPercent.setStatus("current")
_SysCPUUserBusyPercent_Type = Gauge32
_SysCPUUserBusyPercent_Object = MibScalar
sysCPUUserBusyPercent = _SysCPUUserBusyPercent_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 47),
    _SysCPUUserBusyPercent_Type()
)
sysCPUUserBusyPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysCPUUserBusyPercent.setStatus("current")
_SysCPUSystemBusyPercent_Type = Gauge32
_SysCPUSystemBusyPercent_Object = MibScalar
sysCPUSystemBusyPercent = _SysCPUSystemBusyPercent_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 48),
    _SysCPUSystemBusyPercent_Type()
)
sysCPUSystemBusyPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysCPUSystemBusyPercent.setStatus("current")
_SysFDsFree_Type = Gauge32
_SysFDsFree_Object = MibScalar
sysFDsFree = _SysFDsFree_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 49),
    _SysFDsFree_Type()
)
sysFDsFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysFDsFree.setStatus("current")
_SysMemTotal_Type = Gauge32
_SysMemTotal_Object = MibScalar
sysMemTotal = _SysMemTotal_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 50),
    _SysMemTotal_Type()
)
sysMemTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysMemTotal.setStatus("current")
_SysMemFree_Type = Gauge32
_SysMemFree_Object = MibScalar
sysMemFree = _SysMemFree_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 51),
    _SysMemFree_Type()
)
sysMemFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysMemFree.setStatus("current")
_SysMemInUse_Type = Gauge32
_SysMemInUse_Object = MibScalar
sysMemInUse = _SysMemInUse_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 52),
    _SysMemInUse_Type()
)
sysMemInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysMemInUse.setStatus("current")
_SysMemBuffered_Type = Gauge32
_SysMemBuffered_Object = MibScalar
sysMemBuffered = _SysMemBuffered_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 53),
    _SysMemBuffered_Type()
)
sysMemBuffered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysMemBuffered.setStatus("current")
_SysMemSwapped_Type = Gauge32
_SysMemSwapped_Object = MibScalar
sysMemSwapped = _SysMemSwapped_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 54),
    _SysMemSwapped_Type()
)
sysMemSwapped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysMemSwapped.setStatus("current")
_SysMemSwapTotal_Type = Gauge32
_SysMemSwapTotal_Object = MibScalar
sysMemSwapTotal = _SysMemSwapTotal_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 55),
    _SysMemSwapTotal_Type()
)
sysMemSwapTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysMemSwapTotal.setStatus("current")
_NumIdleConnections_Type = Gauge32
_NumIdleConnections_Object = MibScalar
numIdleConnections = _NumIdleConnections_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 56),
    _NumIdleConnections_Type()
)
numIdleConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numIdleConnections.setStatus("current")
_SslCipherRSAEncryptsExternal_Type = Counter32
_SslCipherRSAEncryptsExternal_Object = MibScalar
sslCipherRSAEncryptsExternal = _SslCipherRSAEncryptsExternal_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 57),
    _SslCipherRSAEncryptsExternal_Type()
)
sslCipherRSAEncryptsExternal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslCipherRSAEncryptsExternal.setStatus("current")
_DataEntries_Type = Gauge32
_DataEntries_Object = MibScalar
dataEntries = _DataEntries_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 58),
    _DataEntries_Type()
)
dataEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataEntries.setStatus("current")
_DataMemoryUsage_Type = Gauge32
_DataMemoryUsage_Object = MibScalar
dataMemoryUsage = _DataMemoryUsage_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 59),
    _DataMemoryUsage_Type()
)
dataMemoryUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataMemoryUsage.setStatus("current")
_EventsSeen_Type = Counter32
_EventsSeen_Object = MibScalar
eventsSeen = _EventsSeen_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 60),
    _EventsSeen_Type()
)
eventsSeen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventsSeen.setStatus("current")
_TotalDNSResponses_Type = Counter32
_TotalDNSResponses_Object = MibScalar
totalDNSResponses = _TotalDNSResponses_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 61),
    _TotalDNSResponses_Type()
)
totalDNSResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalDNSResponses.setStatus("current")
_TotalBadDNSPackets_Type = Counter32
_TotalBadDNSPackets_Object = MibScalar
totalBadDNSPackets = _TotalBadDNSPackets_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 62),
    _TotalBadDNSPackets_Type()
)
totalBadDNSPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalBadDNSPackets.setStatus("current")
_TotalBackendServerErrors_Type = Counter32
_TotalBackendServerErrors_Object = MibScalar
totalBackendServerErrors = _TotalBackendServerErrors_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 63),
    _TotalBackendServerErrors_Type()
)
totalBackendServerErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalBackendServerErrors.setStatus("current")
_TotalBytesIn_Type = Counter64
_TotalBytesIn_Object = MibScalar
totalBytesIn = _TotalBytesIn_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 64),
    _TotalBytesIn_Type()
)
totalBytesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalBytesIn.setStatus("current")
_TotalBytesOut_Type = Counter64
_TotalBytesOut_Object = MibScalar
totalBytesOut = _TotalBytesOut_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 65),
    _TotalBytesOut_Type()
)
totalBytesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalBytesOut.setStatus("current")
_NumberSNMPGetBulkRequests_Type = Counter32
_NumberSNMPGetBulkRequests_Object = MibScalar
numberSNMPGetBulkRequests = _NumberSNMPGetBulkRequests_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 66),
    _NumberSNMPGetBulkRequests_Type()
)
numberSNMPGetBulkRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numberSNMPGetBulkRequests.setStatus("current")
_SslCipherDSASigns_Type = Counter32
_SslCipherDSASigns_Object = MibScalar
sslCipherDSASigns = _SslCipherDSASigns_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 67),
    _SslCipherDSASigns_Type()
)
sslCipherDSASigns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslCipherDSASigns.setStatus("current")
_SslCipherDSAVerifies_Type = Counter32
_SslCipherDSAVerifies_Object = MibScalar
sslCipherDSAVerifies = _SslCipherDSAVerifies_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 68),
    _SslCipherDSAVerifies_Type()
)
sslCipherDSAVerifies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslCipherDSAVerifies.setStatus("current")
_SslHandshakeTLSv12_Type = Counter32
_SslHandshakeTLSv12_Object = MibScalar
sslHandshakeTLSv12 = _SslHandshakeTLSv12_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 69),
    _SslHandshakeTLSv12_Type()
)
sslHandshakeTLSv12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslHandshakeTLSv12.setStatus("current")
_SslCipherDHGenerates_Type = Counter32
_SslCipherDHGenerates_Object = MibScalar
sslCipherDHGenerates = _SslCipherDHGenerates_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 70),
    _SslCipherDHGenerates_Type()
)
sslCipherDHGenerates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslCipherDHGenerates.setStatus("current")
_SslCipherDHAgreements_Type = Counter32
_SslCipherDHAgreements_Object = MibScalar
sslCipherDHAgreements = _SslCipherDHAgreements_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 71),
    _SslCipherDHAgreements_Type()
)
sslCipherDHAgreements.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslCipherDHAgreements.setStatus("current")
_SslCipherAESGCMEncrypts_Type = Counter32
_SslCipherAESGCMEncrypts_Object = MibScalar
sslCipherAESGCMEncrypts = _SslCipherAESGCMEncrypts_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 72),
    _SslCipherAESGCMEncrypts_Type()
)
sslCipherAESGCMEncrypts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslCipherAESGCMEncrypts.setStatus("current")
_SslCipherAESGCMDecrypts_Type = Counter32
_SslCipherAESGCMDecrypts_Object = MibScalar
sslCipherAESGCMDecrypts = _SslCipherAESGCMDecrypts_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 73),
    _SslCipherAESGCMDecrypts_Type()
)
sslCipherAESGCMDecrypts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslCipherAESGCMDecrypts.setStatus("current")
_SslCipherECDHGenerates_Type = Counter32
_SslCipherECDHGenerates_Object = MibScalar
sslCipherECDHGenerates = _SslCipherECDHGenerates_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 74),
    _SslCipherECDHGenerates_Type()
)
sslCipherECDHGenerates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslCipherECDHGenerates.setStatus("current")
_SslCipherECDHAgreements_Type = Counter32
_SslCipherECDHAgreements_Object = MibScalar
sslCipherECDHAgreements = _SslCipherECDHAgreements_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 75),
    _SslCipherECDHAgreements_Type()
)
sslCipherECDHAgreements.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslCipherECDHAgreements.setStatus("current")
_SslCipherECDSASigns_Type = Counter32
_SslCipherECDSASigns_Object = MibScalar
sslCipherECDSASigns = _SslCipherECDSASigns_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 76),
    _SslCipherECDSASigns_Type()
)
sslCipherECDSASigns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslCipherECDSASigns.setStatus("current")
_SslCipherECDSAVerifies_Type = Counter32
_SslCipherECDSAVerifies_Object = MibScalar
sslCipherECDSAVerifies = _SslCipherECDSAVerifies_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 77),
    _SslCipherECDSAVerifies_Type()
)
sslCipherECDSAVerifies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslCipherECDSAVerifies.setStatus("current")
_TotalRequests_Type = Counter32
_TotalRequests_Object = MibScalar
totalRequests = _TotalRequests_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 127),
    _TotalRequests_Type()
)
totalRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalRequests.setStatus("current")
_TotalTransactions_Type = Counter32
_TotalTransactions_Object = MibScalar
totalTransactions = _TotalTransactions_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 128),
    _TotalTransactions_Type()
)
totalTransactions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalTransactions.setStatus("current")
_HourlyPeakBytesInPerSecond_Type = Gauge32
_HourlyPeakBytesInPerSecond_Object = MibScalar
hourlyPeakBytesInPerSecond = _HourlyPeakBytesInPerSecond_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 129),
    _HourlyPeakBytesInPerSecond_Type()
)
hourlyPeakBytesInPerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hourlyPeakBytesInPerSecond.setStatus("current")
_HourlyPeakBytesOutPerSecond_Type = Gauge32
_HourlyPeakBytesOutPerSecond_Object = MibScalar
hourlyPeakBytesOutPerSecond = _HourlyPeakBytesOutPerSecond_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 130),
    _HourlyPeakBytesOutPerSecond_Type()
)
hourlyPeakBytesOutPerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hourlyPeakBytesOutPerSecond.setStatus("current")
_HourlyPeakRequestsPerSecond_Type = Gauge32
_HourlyPeakRequestsPerSecond_Object = MibScalar
hourlyPeakRequestsPerSecond = _HourlyPeakRequestsPerSecond_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 131),
    _HourlyPeakRequestsPerSecond_Type()
)
hourlyPeakRequestsPerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hourlyPeakRequestsPerSecond.setStatus("current")
_HourlyPeakSSLConnectionsPerSecond_Type = Gauge32
_HourlyPeakSSLConnectionsPerSecond_Object = MibScalar
hourlyPeakSSLConnectionsPerSecond = _HourlyPeakSSLConnectionsPerSecond_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 132),
    _HourlyPeakSSLConnectionsPerSecond_Type()
)
hourlyPeakSSLConnectionsPerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hourlyPeakSSLConnectionsPerSecond.setStatus("current")
_Virtualservers_ObjectIdentity = ObjectIdentity
virtualservers = _Virtualservers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 2)
)
_VirtualserverNumber_Type = Integer32
_VirtualserverNumber_Object = MibScalar
virtualserverNumber = _VirtualserverNumber_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 2, 1),
    _VirtualserverNumber_Type()
)
virtualserverNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualserverNumber.setStatus("current")
_VirtualserverTable_Object = MibTable
virtualserverTable = _VirtualserverTable_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 2, 2)
)
if mibBuilder.loadTexts:
    virtualserverTable.setStatus("current")
_VirtualserverEntry_Object = MibTableRow
virtualserverEntry = _VirtualserverEntry_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 2, 2, 1)
)
virtualserverEntry.setIndexNames(
    (0, "ZXTM-MIB-SMIv2", "virtualserverName"),
)
if mibBuilder.loadTexts:
    virtualserverEntry.setStatus("current")


class _VirtualserverName_Type(DisplayString):
    """Custom type virtualserverName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VirtualserverName_Type.__name__ = "DisplayString"
_VirtualserverName_Object = MibTableColumn
virtualserverName = _VirtualserverName_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 2, 2, 1, 1),
    _VirtualserverName_Type()
)
virtualserverName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualserverName.setStatus("current")


class _VirtualserverPort_Type(Integer32):
    """Custom type virtualserverPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VirtualserverPort_Type.__name__ = "Integer32"
_VirtualserverPort_Object = MibTableColumn
virtualserverPort = _VirtualserverPort_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 2, 2, 1, 2),
    _VirtualserverPort_Type()
)
virtualserverPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualserverPort.setStatus("current")


class _VirtualserverProtocol_Type(Integer32):
    """Custom type virtualserverProtocol based on Integer32"""
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
        *(("dns", 17),
          ("dnstcp", 20),
          ("ftp", 3),
          ("genericclientfirst", 19),
          ("genericserverfirst", 18),
          ("http", 1),
          ("https", 2),
          ("imaps", 4),
          ("imapv2", 5),
          ("imapv3", 6),
          ("imapv4", 7),
          ("l4accelgeneric", 27),
          ("l4accelstateless", 28),
          ("l4acceltcp", 25),
          ("l4acceludp", 26),
          ("ldap", 11),
          ("ldaps", 12),
          ("pop3", 8),
          ("pop3s", 9),
          ("rtsp", 23),
          ("siptcp", 22),
          ("sipudp", 21),
          ("smtp", 10),
          ("sslforwarding", 14),
          ("stream", 24),
          ("telnet", 13),
          ("udp", 16),
          ("udpstreaming", 15))
    )


_VirtualserverProtocol_Type.__name__ = "Integer32"
_VirtualserverProtocol_Object = MibTableColumn
virtualserverProtocol = _VirtualserverProtocol_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 2, 2, 1, 3),
    _VirtualserverProtocol_Type()
)
virtualserverProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualserverProtocol.setStatus("current")


class _VirtualserverDefaultTrafficPool_Type(DisplayString):
    """Custom type virtualserverDefaultTrafficPool based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VirtualserverDefaultTrafficPool_Type.__name__ = "DisplayString"
_VirtualserverDefaultTrafficPool_Object = MibTableColumn
virtualserverDefaultTrafficPool = _VirtualserverDefaultTrafficPool_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 2, 2, 1, 4),
    _VirtualserverDefaultTrafficPool_Type()
)
virtualserverDefaultTrafficPool.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualserverDefaultTrafficPool.setStatus("current")
_VirtualserverBytesInLo_Type = Counter32
_VirtualserverBytesInLo_Object = MibTableColumn
virtualserverBytesInLo = _VirtualserverBytesInLo_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 2, 2, 1, 5),
    _VirtualserverBytesInLo_Type()
)
virtualserverBytesInLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualserverBytesInLo.setStatus("obsolete")
_VirtualserverBytesInHi_Type = Counter32
_VirtualserverBytesInHi_Object = MibTableColumn
virtualserverBytesInHi = _VirtualserverBytesInHi_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 2, 2, 1, 6),
    _VirtualserverBytesInHi_Type()
)
virtualserverBytesInHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualserverBytesInHi.setStatus("obsolete")
_VirtualserverBytesOutLo_Type = Counter32
_VirtualserverBytesOutLo_Object = MibTableColumn
virtualserverBytesOutLo = _VirtualserverBytesOutLo_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 2, 2, 1, 7),
    _VirtualserverBytesOutLo_Type()
)
virtualserverBytesOutLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualserverBytesOutLo.setStatus("obsolete")
_VirtualserverBytesOutHi_Type = Counter32
_VirtualserverBytesOutHi_Object = MibTableColumn
virtualserverBytesOutHi = _VirtualserverBytesOutHi_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 2, 2, 1, 8),
    _VirtualserverBytesOutHi_Type()
)
virtualserverBytesOutHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualserverBytesOutHi.setStatus("obsolete")
_VirtualserverCurrentConn_Type = Gauge32
_VirtualserverCurrentConn_Object = MibTableColumn
virtualserverCurrentConn = _VirtualserverCurrentConn_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 2, 2, 1, 9),
    _VirtualserverCurrentConn_Type()
)
virtualserverCurrentConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualserverCurrentConn.setStatus("current")
_VirtualserverMaxConn_Type = Gauge32
_VirtualserverMaxConn_Object = MibTableColumn
virtualserverMaxConn = _VirtualserverMaxConn_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 2, 2, 1, 10),
    _VirtualserverMaxConn_Type()
)
virtualserverMaxConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualserverMaxConn.setStatus("current")
_VirtualserverTotalConn_Type = Counter32
_VirtualserverTotalConn_Object = MibTableColumn
virtualserverTotalConn = _VirtualserverTotalConn_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 2, 2, 1, 11),
    _VirtualserverTotalConn_Type()
)
virtualserverTotalConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualserverTotalConn.setStatus("obsolete")
_VirtualserverDiscard_Type = Counter32
_VirtualserverDiscard_Object = MibTableColumn
virtualserverDiscard = _VirtualserverDiscard_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 2, 2, 1, 12),
    _VirtualserverDiscard_Type()
)
virtualserverDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualserverDiscard.setStatus("current")
_VirtualserverDirectReplies_Type = Counter32
_VirtualserverDirectReplies_Object = MibTableColumn
virtualserverDirectReplies = _VirtualserverDirectReplies_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 2, 2, 1, 13),
    _VirtualserverDirectReplies_Type()
)
virtualserverDirectReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualserverDirectReplies.setStatus("current")
_VirtualserverConnectTimedOut_Type = Counter32
_VirtualserverConnectTimedOut_Object = MibTableColumn
virtualserverConnectTimedOut = _VirtualserverConnectTimedOut_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 2, 2, 1, 14),
    _VirtualserverConnectTimedOut_Type()
)
virtualserverConnectTimedOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualserverConnectTimedOut.setStatus("current")
_VirtualserverDataTimedOut_Type = Counter32
_VirtualserverDataTimedOut_Object = MibTableColumn
virtualserverDataTimedOut = _VirtualserverDataTimedOut_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 2, 2, 1, 15),
    _VirtualserverDataTimedOut_Type()
)
virtualserverDataTimedOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualserverDataTimedOut.setStatus("current")
_VirtualserverKeepaliveTimedOut_Type = Counter32
_VirtualserverKeepaliveTimedOut_Object = MibTableColumn
virtualserverKeepaliveTimedOut = _VirtualserverKeepaliveTimedOut_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 2, 2, 1, 16),
    _VirtualserverKeepaliveTimedOut_Type()
)
virtualserverKeepaliveTimedOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualserverKeepaliveTimedOut.setStatus("current")
_VirtualserverUdpTimedOut_Type = Counter32
_VirtualserverUdpTimedOut_Object = MibTableColumn
virtualserverUdpTimedOut = _VirtualserverUdpTimedOut_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 2, 2, 1, 17),
    _VirtualserverUdpTimedOut_Type()
)
virtualserverUdpTimedOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualserverUdpTimedOut.setStatus("current")
_VirtualserverTotalDgram_Type = Counter32
_VirtualserverTotalDgram_Object = MibTableColumn
virtualserverTotalDgram = _VirtualserverTotalDgram_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 2, 2, 1, 18),
    _VirtualserverTotalDgram_Type()
)
virtualserverTotalDgram.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualserverTotalDgram.setStatus("current")
_VirtualserverGzip_Type = Counter32
_VirtualserverGzip_Object = MibTableColumn
virtualserverGzip = _VirtualserverGzip_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 2, 2, 1, 19),
    _VirtualserverGzip_Type()
)
virtualserverGzip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualserverGzip.setStatus("current")
_VirtualserverGzipBytesSavedLo_Type = Counter32
_VirtualserverGzipBytesSavedLo_Object = MibTableColumn
virtualserverGzipBytesSavedLo = _VirtualserverGzipBytesSavedLo_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 2, 2, 1, 20),
    _VirtualserverGzipBytesSavedLo_Type()
)
virtualserverGzipBytesSavedLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualserverGzipBytesSavedLo.setStatus("obsolete")
_VirtualserverGzipBytesSavedHi_Type = Counter32
_VirtualserverGzipBytesSavedHi_Object = MibTableColumn
virtualserverGzipBytesSavedHi = _VirtualserverGzipBytesSavedHi_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 2, 2, 1, 21),
    _VirtualserverGzipBytesSavedHi_Type()
)
virtualserverGzipBytesSavedHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualserverGzipBytesSavedHi.setStatus("obsolete")
_VirtualserverHttpRewriteLocation_Type = Counter32
_VirtualserverHttpRewriteLocation_Object = MibTableColumn
virtualserverHttpRewriteLocation = _VirtualserverHttpRewriteLocation_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 2, 2, 1, 22),
    _VirtualserverHttpRewriteLocation_Type()
)
virtualserverHttpRewriteLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualserverHttpRewriteLocation.setStatus("current")
_VirtualserverHttpRewriteCookie_Type = Counter32
_VirtualserverHttpRewriteCookie_Object = MibTableColumn
virtualserverHttpRewriteCookie = _VirtualserverHttpRewriteCookie_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 2, 2, 1, 23),
    _VirtualserverHttpRewriteCookie_Type()
)
virtualserverHttpRewriteCookie.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualserverHttpRewriteCookie.setStatus("current")
_VirtualserverHttpCacheHits_Type = Counter32
_VirtualserverHttpCacheHits_Object = MibTableColumn
virtualserverHttpCacheHits = _VirtualserverHttpCacheHits_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 2, 2, 1, 24),
    _VirtualserverHttpCacheHits_Type()
)
virtualserverHttpCacheHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualserverHttpCacheHits.setStatus("current")
_VirtualserverHttpCacheLookups_Type = Counter32
_VirtualserverHttpCacheLookups_Object = MibTableColumn
virtualserverHttpCacheLookups = _VirtualserverHttpCacheLookups_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 2, 2, 1, 25),
    _VirtualserverHttpCacheLookups_Type()
)
virtualserverHttpCacheLookups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualserverHttpCacheLookups.setStatus("current")
_VirtualserverHttpCacheHitRate_Type = Gauge32
_VirtualserverHttpCacheHitRate_Object = MibTableColumn
virtualserverHttpCacheHitRate = _VirtualserverHttpCacheHitRate_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 2, 2, 1, 26),
    _VirtualserverHttpCacheHitRate_Type()
)
virtualserverHttpCacheHitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualserverHttpCacheHitRate.setStatus("current")
_VirtualserverSIPTotalCalls_Type = Counter32
_VirtualserverSIPTotalCalls_Object = MibTableColumn
virtualserverSIPTotalCalls = _VirtualserverSIPTotalCalls_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 2, 2, 1, 27),
    _VirtualserverSIPTotalCalls_Type()
)
virtualserverSIPTotalCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualserverSIPTotalCalls.setStatus("current")
_VirtualserverSIPRejectedRequests_Type = Counter32
_VirtualserverSIPRejectedRequests_Object = MibTableColumn
virtualserverSIPRejectedRequests = _VirtualserverSIPRejectedRequests_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 2, 2, 1, 28),
    _VirtualserverSIPRejectedRequests_Type()
)
virtualserverSIPRejectedRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualserverSIPRejectedRequests.setStatus("current")
_VirtualserverConnectionErrors_Type = Counter32
_VirtualserverConnectionErrors_Object = MibTableColumn
virtualserverConnectionErrors = _VirtualserverConnectionErrors_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 2, 2, 1, 29),
    _VirtualserverConnectionErrors_Type()
)
virtualserverConnectionErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualserverConnectionErrors.setStatus("current")
_VirtualserverConnectionFailures_Type = Counter32
_VirtualserverConnectionFailures_Object = MibTableColumn
virtualserverConnectionFailures = _VirtualserverConnectionFailures_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 2, 2, 1, 30),
    _VirtualserverConnectionFailures_Type()
)
virtualserverConnectionFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualserverConnectionFailures.setStatus("current")
_VirtualserverBytesIn_Type = Counter64
_VirtualserverBytesIn_Object = MibTableColumn
virtualserverBytesIn = _VirtualserverBytesIn_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 2, 2, 1, 31),
    _VirtualserverBytesIn_Type()
)
virtualserverBytesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualserverBytesIn.setStatus("current")
_VirtualserverBytesOut_Type = Counter64
_VirtualserverBytesOut_Object = MibTableColumn
virtualserverBytesOut = _VirtualserverBytesOut_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 2, 2, 1, 32),
    _VirtualserverBytesOut_Type()
)
virtualserverBytesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualserverBytesOut.setStatus("current")
_VirtualserverGzipBytesSaved_Type = Counter64
_VirtualserverGzipBytesSaved_Object = MibTableColumn
virtualserverGzipBytesSaved = _VirtualserverGzipBytesSaved_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 2, 2, 1, 33),
    _VirtualserverGzipBytesSaved_Type()
)
virtualserverGzipBytesSaved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualserverGzipBytesSaved.setStatus("current")
_VirtualserverCertStatusRequests_Type = Counter32
_VirtualserverCertStatusRequests_Object = MibTableColumn
virtualserverCertStatusRequests = _VirtualserverCertStatusRequests_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 2, 2, 1, 34),
    _VirtualserverCertStatusRequests_Type()
)
virtualserverCertStatusRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualserverCertStatusRequests.setStatus("current")
_VirtualserverCertStatusResponses_Type = Counter32
_VirtualserverCertStatusResponses_Object = MibTableColumn
virtualserverCertStatusResponses = _VirtualserverCertStatusResponses_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 2, 2, 1, 35),
    _VirtualserverCertStatusResponses_Type()
)
virtualserverCertStatusResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualserverCertStatusResponses.setStatus("current")
_VirtualserverMaxDurationTimedOut_Type = Counter32
_VirtualserverMaxDurationTimedOut_Object = MibTableColumn
virtualserverMaxDurationTimedOut = _VirtualserverMaxDurationTimedOut_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 2, 2, 1, 36),
    _VirtualserverMaxDurationTimedOut_Type()
)
virtualserverMaxDurationTimedOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualserverMaxDurationTimedOut.setStatus("current")
_VirtualserverProcessingTimedOut_Type = Counter32
_VirtualserverProcessingTimedOut_Object = MibTableColumn
virtualserverProcessingTimedOut = _VirtualserverProcessingTimedOut_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 2, 2, 1, 37),
    _VirtualserverProcessingTimedOut_Type()
)
virtualserverProcessingTimedOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualserverProcessingTimedOut.setStatus("current")
_VirtualserverTotalRequestsLo_Type = Counter32
_VirtualserverTotalRequestsLo_Object = MibTableColumn
virtualserverTotalRequestsLo = _VirtualserverTotalRequestsLo_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 2, 2, 1, 38),
    _VirtualserverTotalRequestsLo_Type()
)
virtualserverTotalRequestsLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualserverTotalRequestsLo.setStatus("obsolete")
_VirtualserverTotalRequestsHi_Type = Counter32
_VirtualserverTotalRequestsHi_Object = MibTableColumn
virtualserverTotalRequestsHi = _VirtualserverTotalRequestsHi_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 2, 2, 1, 39),
    _VirtualserverTotalRequestsHi_Type()
)
virtualserverTotalRequestsHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualserverTotalRequestsHi.setStatus("obsolete")
_VirtualserverTotalRequests_Type = Counter64
_VirtualserverTotalRequests_Object = MibTableColumn
virtualserverTotalRequests = _VirtualserverTotalRequests_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 2, 2, 1, 40),
    _VirtualserverTotalRequests_Type()
)
virtualserverTotalRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualserverTotalRequests.setStatus("current")
_VirtualserverTotalHTTPRequestsLo_Type = Counter32
_VirtualserverTotalHTTPRequestsLo_Object = MibTableColumn
virtualserverTotalHTTPRequestsLo = _VirtualserverTotalHTTPRequestsLo_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 2, 2, 1, 41),
    _VirtualserverTotalHTTPRequestsLo_Type()
)
virtualserverTotalHTTPRequestsLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualserverTotalHTTPRequestsLo.setStatus("obsolete")
_VirtualserverTotalHTTPRequestsHi_Type = Counter32
_VirtualserverTotalHTTPRequestsHi_Object = MibTableColumn
virtualserverTotalHTTPRequestsHi = _VirtualserverTotalHTTPRequestsHi_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 2, 2, 1, 42),
    _VirtualserverTotalHTTPRequestsHi_Type()
)
virtualserverTotalHTTPRequestsHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualserverTotalHTTPRequestsHi.setStatus("obsolete")
_VirtualserverTotalHTTPRequests_Type = Counter64
_VirtualserverTotalHTTPRequests_Object = MibTableColumn
virtualserverTotalHTTPRequests = _VirtualserverTotalHTTPRequests_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 2, 2, 1, 43),
    _VirtualserverTotalHTTPRequests_Type()
)
virtualserverTotalHTTPRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualserverTotalHTTPRequests.setStatus("current")
_VirtualserverTotalHTTP1RequestsLo_Type = Counter32
_VirtualserverTotalHTTP1RequestsLo_Object = MibTableColumn
virtualserverTotalHTTP1RequestsLo = _VirtualserverTotalHTTP1RequestsLo_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 2, 2, 1, 44),
    _VirtualserverTotalHTTP1RequestsLo_Type()
)
virtualserverTotalHTTP1RequestsLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualserverTotalHTTP1RequestsLo.setStatus("obsolete")
_VirtualserverTotalHTTP1RequestsHi_Type = Counter32
_VirtualserverTotalHTTP1RequestsHi_Object = MibTableColumn
virtualserverTotalHTTP1RequestsHi = _VirtualserverTotalHTTP1RequestsHi_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 2, 2, 1, 45),
    _VirtualserverTotalHTTP1RequestsHi_Type()
)
virtualserverTotalHTTP1RequestsHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualserverTotalHTTP1RequestsHi.setStatus("obsolete")
_VirtualserverTotalHTTP1Requests_Type = Counter64
_VirtualserverTotalHTTP1Requests_Object = MibTableColumn
virtualserverTotalHTTP1Requests = _VirtualserverTotalHTTP1Requests_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 2, 2, 1, 46),
    _VirtualserverTotalHTTP1Requests_Type()
)
virtualserverTotalHTTP1Requests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualserverTotalHTTP1Requests.setStatus("current")
_VirtualserverTotalHTTP2RequestsLo_Type = Counter32
_VirtualserverTotalHTTP2RequestsLo_Object = MibTableColumn
virtualserverTotalHTTP2RequestsLo = _VirtualserverTotalHTTP2RequestsLo_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 2, 2, 1, 47),
    _VirtualserverTotalHTTP2RequestsLo_Type()
)
virtualserverTotalHTTP2RequestsLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualserverTotalHTTP2RequestsLo.setStatus("obsolete")
_VirtualserverTotalHTTP2RequestsHi_Type = Counter32
_VirtualserverTotalHTTP2RequestsHi_Object = MibTableColumn
virtualserverTotalHTTP2RequestsHi = _VirtualserverTotalHTTP2RequestsHi_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 2, 2, 1, 48),
    _VirtualserverTotalHTTP2RequestsHi_Type()
)
virtualserverTotalHTTP2RequestsHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualserverTotalHTTP2RequestsHi.setStatus("obsolete")
_VirtualserverTotalHTTP2Requests_Type = Counter64
_VirtualserverTotalHTTP2Requests_Object = MibTableColumn
virtualserverTotalHTTP2Requests = _VirtualserverTotalHTTP2Requests_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 2, 2, 1, 49),
    _VirtualserverTotalHTTP2Requests_Type()
)
virtualserverTotalHTTP2Requests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualserverTotalHTTP2Requests.setStatus("current")
_VirtualserverPktsInLo_Type = Counter32
_VirtualserverPktsInLo_Object = MibTableColumn
virtualserverPktsInLo = _VirtualserverPktsInLo_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 2, 2, 1, 50),
    _VirtualserverPktsInLo_Type()
)
virtualserverPktsInLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualserverPktsInLo.setStatus("obsolete")
_VirtualserverPktsInHi_Type = Counter32
_VirtualserverPktsInHi_Object = MibTableColumn
virtualserverPktsInHi = _VirtualserverPktsInHi_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 2, 2, 1, 51),
    _VirtualserverPktsInHi_Type()
)
virtualserverPktsInHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualserverPktsInHi.setStatus("obsolete")
_VirtualserverPktsOutLo_Type = Counter32
_VirtualserverPktsOutLo_Object = MibTableColumn
virtualserverPktsOutLo = _VirtualserverPktsOutLo_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 2, 2, 1, 52),
    _VirtualserverPktsOutLo_Type()
)
virtualserverPktsOutLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualserverPktsOutLo.setStatus("obsolete")
_VirtualserverPktsOutHi_Type = Counter32
_VirtualserverPktsOutHi_Object = MibTableColumn
virtualserverPktsOutHi = _VirtualserverPktsOutHi_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 2, 2, 1, 53),
    _VirtualserverPktsOutHi_Type()
)
virtualserverPktsOutHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualserverPktsOutHi.setStatus("obsolete")
_VirtualserverPktsIn_Type = Counter64
_VirtualserverPktsIn_Object = MibTableColumn
virtualserverPktsIn = _VirtualserverPktsIn_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 2, 2, 1, 54),
    _VirtualserverPktsIn_Type()
)
virtualserverPktsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualserverPktsIn.setStatus("current")
_VirtualserverPktsOut_Type = Counter64
_VirtualserverPktsOut_Object = MibTableColumn
virtualserverPktsOut = _VirtualserverPktsOut_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 2, 2, 1, 55),
    _VirtualserverPktsOut_Type()
)
virtualserverPktsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualserverPktsOut.setStatus("current")
_VirtualserverL4TCPConnectResets_Type = Counter32
_VirtualserverL4TCPConnectResets_Object = MibTableColumn
virtualserverL4TCPConnectResets = _VirtualserverL4TCPConnectResets_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 2, 2, 1, 56),
    _VirtualserverL4TCPConnectResets_Type()
)
virtualserverL4TCPConnectResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualserverL4TCPConnectResets.setStatus("current")
_VirtualserverL4UDPUnreachables_Type = Counter32
_VirtualserverL4UDPUnreachables_Object = MibTableColumn
virtualserverL4UDPUnreachables = _VirtualserverL4UDPUnreachables_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 2, 2, 1, 57),
    _VirtualserverL4UDPUnreachables_Type()
)
virtualserverL4UDPUnreachables.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualserverL4UDPUnreachables.setStatus("current")
_VirtualserverBwLimitPktsDrop_Type = Counter64
_VirtualserverBwLimitPktsDrop_Object = MibTableColumn
virtualserverBwLimitPktsDrop = _VirtualserverBwLimitPktsDrop_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 2, 2, 1, 58),
    _VirtualserverBwLimitPktsDrop_Type()
)
virtualserverBwLimitPktsDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualserverBwLimitPktsDrop.setStatus("current")
_VirtualserverBwLimitPktsDropLo_Type = Counter32
_VirtualserverBwLimitPktsDropLo_Object = MibTableColumn
virtualserverBwLimitPktsDropLo = _VirtualserverBwLimitPktsDropLo_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 2, 2, 1, 59),
    _VirtualserverBwLimitPktsDropLo_Type()
)
virtualserverBwLimitPktsDropLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualserverBwLimitPktsDropLo.setStatus("obsolete")
_VirtualserverBwLimitPktsDropHi_Type = Counter32
_VirtualserverBwLimitPktsDropHi_Object = MibTableColumn
virtualserverBwLimitPktsDropHi = _VirtualserverBwLimitPktsDropHi_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 2, 2, 1, 60),
    _VirtualserverBwLimitPktsDropHi_Type()
)
virtualserverBwLimitPktsDropHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualserverBwLimitPktsDropHi.setStatus("obsolete")
_VirtualserverBwLimitBytesDrop_Type = Counter64
_VirtualserverBwLimitBytesDrop_Object = MibTableColumn
virtualserverBwLimitBytesDrop = _VirtualserverBwLimitBytesDrop_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 2, 2, 1, 61),
    _VirtualserverBwLimitBytesDrop_Type()
)
virtualserverBwLimitBytesDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualserverBwLimitBytesDrop.setStatus("current")
_VirtualserverBwLimitBytesDropLo_Type = Counter32
_VirtualserverBwLimitBytesDropLo_Object = MibTableColumn
virtualserverBwLimitBytesDropLo = _VirtualserverBwLimitBytesDropLo_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 2, 2, 1, 62),
    _VirtualserverBwLimitBytesDropLo_Type()
)
virtualserverBwLimitBytesDropLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualserverBwLimitBytesDropLo.setStatus("obsolete")
_VirtualserverBwLimitBytesDropHi_Type = Counter32
_VirtualserverBwLimitBytesDropHi_Object = MibTableColumn
virtualserverBwLimitBytesDropHi = _VirtualserverBwLimitBytesDropHi_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 2, 2, 1, 63),
    _VirtualserverBwLimitBytesDropHi_Type()
)
virtualserverBwLimitBytesDropHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualserverBwLimitBytesDropHi.setStatus("obsolete")
_Pools_ObjectIdentity = ObjectIdentity
pools = _Pools_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 3)
)


class _PoolNumber_Type(Integer32):
    """Custom type poolNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PoolNumber_Type.__name__ = "Integer32"
_PoolNumber_Object = MibScalar
poolNumber = _PoolNumber_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 3, 1),
    _PoolNumber_Type()
)
poolNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolNumber.setStatus("current")
_PoolTable_Object = MibTable
poolTable = _PoolTable_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 3, 2)
)
if mibBuilder.loadTexts:
    poolTable.setStatus("current")
_PoolEntry_Object = MibTableRow
poolEntry = _PoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 3, 2, 1)
)
poolEntry.setIndexNames(
    (0, "ZXTM-MIB-SMIv2", "poolName"),
)
if mibBuilder.loadTexts:
    poolEntry.setStatus("current")


class _PoolName_Type(DisplayString):
    """Custom type poolName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PoolName_Type.__name__ = "DisplayString"
_PoolName_Object = MibTableColumn
poolName = _PoolName_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 3, 2, 1, 1),
    _PoolName_Type()
)
poolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolName.setStatus("current")


class _PoolAlgorithm_Type(Integer32):
    """Custom type poolAlgorithm based on Integer32"""
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
        *(("fastestResponseTime", 5),
          ("leastConnections", 4),
          ("perceptive", 3),
          ("random", 6),
          ("roundrobin", 1),
          ("weightedLeastConnections", 7),
          ("weightedRoundRobin", 2))
    )


_PoolAlgorithm_Type.__name__ = "Integer32"
_PoolAlgorithm_Object = MibTableColumn
poolAlgorithm = _PoolAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 3, 2, 1, 2),
    _PoolAlgorithm_Type()
)
poolAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolAlgorithm.setStatus("current")
_PoolNodes_Type = Integer32
_PoolNodes_Object = MibTableColumn
poolNodes = _PoolNodes_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 3, 2, 1, 3),
    _PoolNodes_Type()
)
poolNodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolNodes.setStatus("current")
_PoolDraining_Type = Integer32
_PoolDraining_Object = MibTableColumn
poolDraining = _PoolDraining_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 3, 2, 1, 4),
    _PoolDraining_Type()
)
poolDraining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolDraining.setStatus("current")


class _PoolFailPool_Type(DisplayString):
    """Custom type poolFailPool based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PoolFailPool_Type.__name__ = "DisplayString"
_PoolFailPool_Object = MibTableColumn
poolFailPool = _PoolFailPool_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 3, 2, 1, 5),
    _PoolFailPool_Type()
)
poolFailPool.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolFailPool.setStatus("current")
_PoolBytesInLo_Type = Counter32
_PoolBytesInLo_Object = MibTableColumn
poolBytesInLo = _PoolBytesInLo_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 3, 2, 1, 6),
    _PoolBytesInLo_Type()
)
poolBytesInLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolBytesInLo.setStatus("obsolete")
_PoolBytesInHi_Type = Counter32
_PoolBytesInHi_Object = MibTableColumn
poolBytesInHi = _PoolBytesInHi_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 3, 2, 1, 7),
    _PoolBytesInHi_Type()
)
poolBytesInHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolBytesInHi.setStatus("obsolete")
_PoolBytesOutLo_Type = Counter32
_PoolBytesOutLo_Object = MibTableColumn
poolBytesOutLo = _PoolBytesOutLo_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 3, 2, 1, 8),
    _PoolBytesOutLo_Type()
)
poolBytesOutLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolBytesOutLo.setStatus("obsolete")
_PoolBytesOutHi_Type = Counter32
_PoolBytesOutHi_Object = MibTableColumn
poolBytesOutHi = _PoolBytesOutHi_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 3, 2, 1, 9),
    _PoolBytesOutHi_Type()
)
poolBytesOutHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolBytesOutHi.setStatus("obsolete")
_PoolTotalConn_Type = Counter32
_PoolTotalConn_Object = MibTableColumn
poolTotalConn = _PoolTotalConn_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 3, 2, 1, 10),
    _PoolTotalConn_Type()
)
poolTotalConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolTotalConn.setStatus("current")


class _PoolPersistence_Type(Integer32):
    """Custom type poolPersistence based on Integer32"""
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
        *(("applicationCookie", 5),
          ("ip", 2),
          ("none", 1),
          ("rule", 3),
          ("ssl", 7),
          ("transparent", 4),
          ("xZeusBackend", 6))
    )


_PoolPersistence_Type.__name__ = "Integer32"
_PoolPersistence_Object = MibTableColumn
poolPersistence = _PoolPersistence_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 3, 2, 1, 11),
    _PoolPersistence_Type()
)
poolPersistence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolPersistence.setStatus("current")
_PoolSessionMigrated_Type = Counter32
_PoolSessionMigrated_Object = MibTableColumn
poolSessionMigrated = _PoolSessionMigrated_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 3, 2, 1, 12),
    _PoolSessionMigrated_Type()
)
poolSessionMigrated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolSessionMigrated.setStatus("current")
_PoolDisabled_Type = Integer32
_PoolDisabled_Object = MibTableColumn
poolDisabled = _PoolDisabled_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 3, 2, 1, 13),
    _PoolDisabled_Type()
)
poolDisabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolDisabled.setStatus("current")


class _PoolState_Type(Integer32):
    """Custom type poolState based on Integer32"""
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
        *(("active", 1),
          ("disabled", 2),
          ("draining", 3),
          ("unknown", 5),
          ("unused", 4))
    )


_PoolState_Type.__name__ = "Integer32"
_PoolState_Object = MibTableColumn
poolState = _PoolState_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 3, 2, 1, 14),
    _PoolState_Type()
)
poolState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolState.setStatus("current")
_PoolConnsQueued_Type = Gauge32
_PoolConnsQueued_Object = MibTableColumn
poolConnsQueued = _PoolConnsQueued_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 3, 2, 1, 17),
    _PoolConnsQueued_Type()
)
poolConnsQueued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolConnsQueued.setStatus("current")
_PoolQueueTimeouts_Type = Counter32
_PoolQueueTimeouts_Object = MibTableColumn
poolQueueTimeouts = _PoolQueueTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 3, 2, 1, 18),
    _PoolQueueTimeouts_Type()
)
poolQueueTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolQueueTimeouts.setStatus("current")
_PoolMinQueueTime_Type = Gauge32
_PoolMinQueueTime_Object = MibTableColumn
poolMinQueueTime = _PoolMinQueueTime_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 3, 2, 1, 19),
    _PoolMinQueueTime_Type()
)
poolMinQueueTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolMinQueueTime.setStatus("current")
_PoolMaxQueueTime_Type = Gauge32
_PoolMaxQueueTime_Object = MibTableColumn
poolMaxQueueTime = _PoolMaxQueueTime_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 3, 2, 1, 20),
    _PoolMaxQueueTime_Type()
)
poolMaxQueueTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolMaxQueueTime.setStatus("current")
_PoolMeanQueueTime_Type = Gauge32
_PoolMeanQueueTime_Object = MibTableColumn
poolMeanQueueTime = _PoolMeanQueueTime_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 3, 2, 1, 21),
    _PoolMeanQueueTime_Type()
)
poolMeanQueueTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolMeanQueueTime.setStatus("current")
_PoolBytesIn_Type = Counter64
_PoolBytesIn_Object = MibTableColumn
poolBytesIn = _PoolBytesIn_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 3, 2, 1, 22),
    _PoolBytesIn_Type()
)
poolBytesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolBytesIn.setStatus("current")
_PoolBytesOut_Type = Counter64
_PoolBytesOut_Object = MibTableColumn
poolBytesOut = _PoolBytesOut_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 3, 2, 1, 23),
    _PoolBytesOut_Type()
)
poolBytesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolBytesOut.setStatus("current")
_PoolBwLimitPktsDrop_Type = Counter64
_PoolBwLimitPktsDrop_Object = MibTableColumn
poolBwLimitPktsDrop = _PoolBwLimitPktsDrop_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 3, 2, 1, 24),
    _PoolBwLimitPktsDrop_Type()
)
poolBwLimitPktsDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolBwLimitPktsDrop.setStatus("current")
_PoolBwLimitPktsDropLo_Type = Counter32
_PoolBwLimitPktsDropLo_Object = MibTableColumn
poolBwLimitPktsDropLo = _PoolBwLimitPktsDropLo_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 3, 2, 1, 25),
    _PoolBwLimitPktsDropLo_Type()
)
poolBwLimitPktsDropLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolBwLimitPktsDropLo.setStatus("obsolete")
_PoolBwLimitPktsDropHi_Type = Counter32
_PoolBwLimitPktsDropHi_Object = MibTableColumn
poolBwLimitPktsDropHi = _PoolBwLimitPktsDropHi_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 3, 2, 1, 26),
    _PoolBwLimitPktsDropHi_Type()
)
poolBwLimitPktsDropHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolBwLimitPktsDropHi.setStatus("obsolete")
_PoolBwLimitBytesDrop_Type = Counter64
_PoolBwLimitBytesDrop_Object = MibTableColumn
poolBwLimitBytesDrop = _PoolBwLimitBytesDrop_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 3, 2, 1, 27),
    _PoolBwLimitBytesDrop_Type()
)
poolBwLimitBytesDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolBwLimitBytesDrop.setStatus("current")
_PoolBwLimitBytesDropLo_Type = Counter32
_PoolBwLimitBytesDropLo_Object = MibTableColumn
poolBwLimitBytesDropLo = _PoolBwLimitBytesDropLo_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 3, 2, 1, 28),
    _PoolBwLimitBytesDropLo_Type()
)
poolBwLimitBytesDropLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolBwLimitBytesDropLo.setStatus("obsolete")
_PoolBwLimitBytesDropHi_Type = Counter32
_PoolBwLimitBytesDropHi_Object = MibTableColumn
poolBwLimitBytesDropHi = _PoolBwLimitBytesDropHi_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 3, 2, 1, 29),
    _PoolBwLimitBytesDropHi_Type()
)
poolBwLimitBytesDropHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolBwLimitBytesDropHi.setStatus("obsolete")
_Nodes_ObjectIdentity = ObjectIdentity
nodes = _Nodes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 4)
)


class _NodeNumber_Type(Integer32):
    """Custom type nodeNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NodeNumber_Type.__name__ = "Integer32"
_NodeNumber_Object = MibScalar
nodeNumber = _NodeNumber_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 4, 1),
    _NodeNumber_Type()
)
nodeNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeNumber.setStatus("obsolete")
_NodeTable_Object = MibTable
nodeTable = _NodeTable_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 4, 2)
)
if mibBuilder.loadTexts:
    nodeTable.setStatus("obsolete")
_NodeEntry_Object = MibTableRow
nodeEntry = _NodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 4, 2, 1)
)
nodeEntry.setIndexNames(
    (0, "ZXTM-MIB-SMIv2", "nodeIPAddress"),
    (0, "ZXTM-MIB-SMIv2", "nodePort"),
)
if mibBuilder.loadTexts:
    nodeEntry.setStatus("obsolete")
_NodeIPAddress_Type = IpAddress
_NodeIPAddress_Object = MibTableColumn
nodeIPAddress = _NodeIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 4, 2, 1, 1),
    _NodeIPAddress_Type()
)
nodeIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeIPAddress.setStatus("obsolete")


class _NodePort_Type(Integer32):
    """Custom type nodePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NodePort_Type.__name__ = "Integer32"
_NodePort_Object = MibTableColumn
nodePort = _NodePort_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 4, 2, 1, 2),
    _NodePort_Type()
)
nodePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodePort.setStatus("obsolete")


class _NodeHostName_Type(DisplayString):
    """Custom type nodeHostName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NodeHostName_Type.__name__ = "DisplayString"
_NodeHostName_Object = MibTableColumn
nodeHostName = _NodeHostName_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 4, 2, 1, 3),
    _NodeHostName_Type()
)
nodeHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeHostName.setStatus("obsolete")


class _NodeState_Type(Integer32):
    """Custom type nodeState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("alive", 1),
          ("dead", 2),
          ("unknown", 3))
    )


_NodeState_Type.__name__ = "Integer32"
_NodeState_Object = MibTableColumn
nodeState = _NodeState_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 4, 2, 1, 4),
    _NodeState_Type()
)
nodeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeState.setStatus("obsolete")
_NodeBytesToNodeLo_Type = Counter32
_NodeBytesToNodeLo_Object = MibTableColumn
nodeBytesToNodeLo = _NodeBytesToNodeLo_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 4, 2, 1, 5),
    _NodeBytesToNodeLo_Type()
)
nodeBytesToNodeLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeBytesToNodeLo.setStatus("obsolete")
_NodeBytesToNodeHi_Type = Counter32
_NodeBytesToNodeHi_Object = MibTableColumn
nodeBytesToNodeHi = _NodeBytesToNodeHi_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 4, 2, 1, 6),
    _NodeBytesToNodeHi_Type()
)
nodeBytesToNodeHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeBytesToNodeHi.setStatus("obsolete")
_NodeBytesFromNodeLo_Type = Counter32
_NodeBytesFromNodeLo_Object = MibTableColumn
nodeBytesFromNodeLo = _NodeBytesFromNodeLo_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 4, 2, 1, 7),
    _NodeBytesFromNodeLo_Type()
)
nodeBytesFromNodeLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeBytesFromNodeLo.setStatus("obsolete")
_NodeBytesFromNodeHi_Type = Counter32
_NodeBytesFromNodeHi_Object = MibTableColumn
nodeBytesFromNodeHi = _NodeBytesFromNodeHi_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 4, 2, 1, 8),
    _NodeBytesFromNodeHi_Type()
)
nodeBytesFromNodeHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeBytesFromNodeHi.setStatus("obsolete")
_NodeCurrentRequests_Type = Gauge32
_NodeCurrentRequests_Object = MibTableColumn
nodeCurrentRequests = _NodeCurrentRequests_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 4, 2, 1, 9),
    _NodeCurrentRequests_Type()
)
nodeCurrentRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeCurrentRequests.setStatus("obsolete")
_NodeTotalConn_Type = Counter32
_NodeTotalConn_Object = MibTableColumn
nodeTotalConn = _NodeTotalConn_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 4, 2, 1, 10),
    _NodeTotalConn_Type()
)
nodeTotalConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeTotalConn.setStatus("obsolete")
_NodePooledConn_Type = Counter32
_NodePooledConn_Object = MibTableColumn
nodePooledConn = _NodePooledConn_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 4, 2, 1, 11),
    _NodePooledConn_Type()
)
nodePooledConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodePooledConn.setStatus("obsolete")
_NodeFailures_Type = Counter32
_NodeFailures_Object = MibTableColumn
nodeFailures = _NodeFailures_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 4, 2, 1, 12),
    _NodeFailures_Type()
)
nodeFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeFailures.setStatus("obsolete")
_NodeNewConn_Type = Counter32
_NodeNewConn_Object = MibTableColumn
nodeNewConn = _NodeNewConn_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 4, 2, 1, 13),
    _NodeNewConn_Type()
)
nodeNewConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeNewConn.setStatus("obsolete")
_NodeErrors_Type = Counter32
_NodeErrors_Object = MibTableColumn
nodeErrors = _NodeErrors_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 4, 2, 1, 14),
    _NodeErrors_Type()
)
nodeErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeErrors.setStatus("obsolete")
_NodeResponseMin_Type = Gauge32
_NodeResponseMin_Object = MibTableColumn
nodeResponseMin = _NodeResponseMin_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 4, 2, 1, 15),
    _NodeResponseMin_Type()
)
nodeResponseMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeResponseMin.setStatus("obsolete")
_NodeResponseMax_Type = Gauge32
_NodeResponseMax_Object = MibTableColumn
nodeResponseMax = _NodeResponseMax_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 4, 2, 1, 16),
    _NodeResponseMax_Type()
)
nodeResponseMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeResponseMax.setStatus("obsolete")
_NodeResponseMean_Type = Gauge32
_NodeResponseMean_Object = MibTableColumn
nodeResponseMean = _NodeResponseMean_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 4, 2, 1, 17),
    _NodeResponseMean_Type()
)
nodeResponseMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeResponseMean.setStatus("obsolete")
_NodeCurrentConn_Type = Gauge32
_NodeCurrentConn_Object = MibTableColumn
nodeCurrentConn = _NodeCurrentConn_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 4, 2, 1, 18),
    _NodeCurrentConn_Type()
)
nodeCurrentConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeCurrentConn.setStatus("obsolete")


class _NodeNumberInet46_Type(Integer32):
    """Custom type nodeNumberInet46 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NodeNumberInet46_Type.__name__ = "Integer32"
_NodeNumberInet46_Object = MibScalar
nodeNumberInet46 = _NodeNumberInet46_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 4, 3),
    _NodeNumberInet46_Type()
)
nodeNumberInet46.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeNumberInet46.setStatus("current")
_NodeInet46Table_Object = MibTable
nodeInet46Table = _NodeInet46Table_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 4, 4)
)
if mibBuilder.loadTexts:
    nodeInet46Table.setStatus("current")
_NodeInet46Entry_Object = MibTableRow
nodeInet46Entry = _NodeInet46Entry_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 4, 4, 1)
)
nodeInet46Entry.setIndexNames(
    (0, "ZXTM-MIB-SMIv2", "nodeInet46AddressType"),
    (0, "ZXTM-MIB-SMIv2", "nodeInet46Address"),
    (0, "ZXTM-MIB-SMIv2", "nodeInet46Port"),
)
if mibBuilder.loadTexts:
    nodeInet46Entry.setStatus("current")
_NodeInet46AddressType_Type = InetAddressType
_NodeInet46AddressType_Object = MibTableColumn
nodeInet46AddressType = _NodeInet46AddressType_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 4, 4, 1, 1),
    _NodeInet46AddressType_Type()
)
nodeInet46AddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeInet46AddressType.setStatus("current")


class _NodeInet46Address_Type(InetAddress):
    """Custom type nodeInet46Address based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_NodeInet46Address_Type.__name__ = "InetAddress"
_NodeInet46Address_Object = MibTableColumn
nodeInet46Address = _NodeInet46Address_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 4, 4, 1, 2),
    _NodeInet46Address_Type()
)
nodeInet46Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeInet46Address.setStatus("current")


class _NodeInet46Port_Type(Integer32):
    """Custom type nodeInet46Port based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NodeInet46Port_Type.__name__ = "Integer32"
_NodeInet46Port_Object = MibTableColumn
nodeInet46Port = _NodeInet46Port_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 4, 4, 1, 3),
    _NodeInet46Port_Type()
)
nodeInet46Port.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeInet46Port.setStatus("current")


class _NodeInet46HostName_Type(DisplayString):
    """Custom type nodeInet46HostName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NodeInet46HostName_Type.__name__ = "DisplayString"
_NodeInet46HostName_Object = MibTableColumn
nodeInet46HostName = _NodeInet46HostName_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 4, 4, 1, 4),
    _NodeInet46HostName_Type()
)
nodeInet46HostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeInet46HostName.setStatus("current")


class _NodeInet46State_Type(Integer32):
    """Custom type nodeInet46State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("alive", 1),
          ("dead", 2),
          ("unknown", 3))
    )


_NodeInet46State_Type.__name__ = "Integer32"
_NodeInet46State_Object = MibTableColumn
nodeInet46State = _NodeInet46State_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 4, 4, 1, 5),
    _NodeInet46State_Type()
)
nodeInet46State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeInet46State.setStatus("current")
_NodeInet46BytesToNodeLo_Type = Counter32
_NodeInet46BytesToNodeLo_Object = MibTableColumn
nodeInet46BytesToNodeLo = _NodeInet46BytesToNodeLo_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 4, 4, 1, 6),
    _NodeInet46BytesToNodeLo_Type()
)
nodeInet46BytesToNodeLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeInet46BytesToNodeLo.setStatus("obsolete")
_NodeInet46BytesToNodeHi_Type = Counter32
_NodeInet46BytesToNodeHi_Object = MibTableColumn
nodeInet46BytesToNodeHi = _NodeInet46BytesToNodeHi_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 4, 4, 1, 7),
    _NodeInet46BytesToNodeHi_Type()
)
nodeInet46BytesToNodeHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeInet46BytesToNodeHi.setStatus("obsolete")
_NodeInet46BytesFromNodeLo_Type = Counter32
_NodeInet46BytesFromNodeLo_Object = MibTableColumn
nodeInet46BytesFromNodeLo = _NodeInet46BytesFromNodeLo_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 4, 4, 1, 8),
    _NodeInet46BytesFromNodeLo_Type()
)
nodeInet46BytesFromNodeLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeInet46BytesFromNodeLo.setStatus("obsolete")
_NodeInet46BytesFromNodeHi_Type = Counter32
_NodeInet46BytesFromNodeHi_Object = MibTableColumn
nodeInet46BytesFromNodeHi = _NodeInet46BytesFromNodeHi_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 4, 4, 1, 9),
    _NodeInet46BytesFromNodeHi_Type()
)
nodeInet46BytesFromNodeHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeInet46BytesFromNodeHi.setStatus("obsolete")
_NodeInet46CurrentRequests_Type = Gauge32
_NodeInet46CurrentRequests_Object = MibTableColumn
nodeInet46CurrentRequests = _NodeInet46CurrentRequests_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 4, 4, 1, 10),
    _NodeInet46CurrentRequests_Type()
)
nodeInet46CurrentRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeInet46CurrentRequests.setStatus("current")
_NodeInet46TotalConn_Type = Counter32
_NodeInet46TotalConn_Object = MibTableColumn
nodeInet46TotalConn = _NodeInet46TotalConn_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 4, 4, 1, 11),
    _NodeInet46TotalConn_Type()
)
nodeInet46TotalConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeInet46TotalConn.setStatus("current")
_NodeInet46PooledConn_Type = Counter32
_NodeInet46PooledConn_Object = MibTableColumn
nodeInet46PooledConn = _NodeInet46PooledConn_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 4, 4, 1, 12),
    _NodeInet46PooledConn_Type()
)
nodeInet46PooledConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeInet46PooledConn.setStatus("current")
_NodeInet46Failures_Type = Counter32
_NodeInet46Failures_Object = MibTableColumn
nodeInet46Failures = _NodeInet46Failures_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 4, 4, 1, 13),
    _NodeInet46Failures_Type()
)
nodeInet46Failures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeInet46Failures.setStatus("current")
_NodeInet46NewConn_Type = Counter32
_NodeInet46NewConn_Object = MibTableColumn
nodeInet46NewConn = _NodeInet46NewConn_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 4, 4, 1, 14),
    _NodeInet46NewConn_Type()
)
nodeInet46NewConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeInet46NewConn.setStatus("current")
_NodeInet46Errors_Type = Counter32
_NodeInet46Errors_Object = MibTableColumn
nodeInet46Errors = _NodeInet46Errors_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 4, 4, 1, 15),
    _NodeInet46Errors_Type()
)
nodeInet46Errors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeInet46Errors.setStatus("current")
_NodeInet46ResponseMin_Type = Gauge32
_NodeInet46ResponseMin_Object = MibTableColumn
nodeInet46ResponseMin = _NodeInet46ResponseMin_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 4, 4, 1, 16),
    _NodeInet46ResponseMin_Type()
)
nodeInet46ResponseMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeInet46ResponseMin.setStatus("current")
_NodeInet46ResponseMax_Type = Gauge32
_NodeInet46ResponseMax_Object = MibTableColumn
nodeInet46ResponseMax = _NodeInet46ResponseMax_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 4, 4, 1, 17),
    _NodeInet46ResponseMax_Type()
)
nodeInet46ResponseMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeInet46ResponseMax.setStatus("current")
_NodeInet46ResponseMean_Type = Gauge32
_NodeInet46ResponseMean_Object = MibTableColumn
nodeInet46ResponseMean = _NodeInet46ResponseMean_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 4, 4, 1, 18),
    _NodeInet46ResponseMean_Type()
)
nodeInet46ResponseMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeInet46ResponseMean.setStatus("current")
_NodeInet46IdleConns_Type = Gauge32
_NodeInet46IdleConns_Object = MibTableColumn
nodeInet46IdleConns = _NodeInet46IdleConns_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 4, 4, 1, 19),
    _NodeInet46IdleConns_Type()
)
nodeInet46IdleConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeInet46IdleConns.setStatus("current")
_NodeInet46CurrentConn_Type = Gauge32
_NodeInet46CurrentConn_Object = MibTableColumn
nodeInet46CurrentConn = _NodeInet46CurrentConn_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 4, 4, 1, 20),
    _NodeInet46CurrentConn_Type()
)
nodeInet46CurrentConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeInet46CurrentConn.setStatus("current")
_NodeInet46BytesToNode_Type = Counter64
_NodeInet46BytesToNode_Object = MibTableColumn
nodeInet46BytesToNode = _NodeInet46BytesToNode_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 4, 4, 1, 21),
    _NodeInet46BytesToNode_Type()
)
nodeInet46BytesToNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeInet46BytesToNode.setStatus("current")
_NodeInet46BytesFromNode_Type = Counter64
_NodeInet46BytesFromNode_Object = MibTableColumn
nodeInet46BytesFromNode = _NodeInet46BytesFromNode_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 4, 4, 1, 22),
    _NodeInet46BytesFromNode_Type()
)
nodeInet46BytesFromNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeInet46BytesFromNode.setStatus("current")


class _PerPoolNodeNumber_Type(Integer32):
    """Custom type perPoolNodeNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PerPoolNodeNumber_Type.__name__ = "Integer32"
_PerPoolNodeNumber_Object = MibScalar
perPoolNodeNumber = _PerPoolNodeNumber_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 4, 5),
    _PerPoolNodeNumber_Type()
)
perPoolNodeNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perPoolNodeNumber.setStatus("current")
_PerPoolNodeTable_Object = MibTable
perPoolNodeTable = _PerPoolNodeTable_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 4, 6)
)
if mibBuilder.loadTexts:
    perPoolNodeTable.setStatus("current")
_PerPoolNodeEntry_Object = MibTableRow
perPoolNodeEntry = _PerPoolNodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 4, 6, 1)
)
perPoolNodeEntry.setIndexNames(
    (0, "ZXTM-MIB-SMIv2", "perPoolNodePoolName"),
    (0, "ZXTM-MIB-SMIv2", "perPoolNodeNodeAddressType"),
    (0, "ZXTM-MIB-SMIv2", "perPoolNodeNodeAddress"),
    (0, "ZXTM-MIB-SMIv2", "perPoolNodeNodePort"),
)
if mibBuilder.loadTexts:
    perPoolNodeEntry.setStatus("current")


class _PerPoolNodePoolName_Type(DisplayString):
    """Custom type perPoolNodePoolName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PerPoolNodePoolName_Type.__name__ = "DisplayString"
_PerPoolNodePoolName_Object = MibTableColumn
perPoolNodePoolName = _PerPoolNodePoolName_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 4, 6, 1, 1),
    _PerPoolNodePoolName_Type()
)
perPoolNodePoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perPoolNodePoolName.setStatus("current")
_PerPoolNodeNodeAddressType_Type = InetAddressType
_PerPoolNodeNodeAddressType_Object = MibTableColumn
perPoolNodeNodeAddressType = _PerPoolNodeNodeAddressType_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 4, 6, 1, 2),
    _PerPoolNodeNodeAddressType_Type()
)
perPoolNodeNodeAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perPoolNodeNodeAddressType.setStatus("current")


class _PerPoolNodeNodeAddress_Type(InetAddress):
    """Custom type perPoolNodeNodeAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_PerPoolNodeNodeAddress_Type.__name__ = "InetAddress"
_PerPoolNodeNodeAddress_Object = MibTableColumn
perPoolNodeNodeAddress = _PerPoolNodeNodeAddress_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 4, 6, 1, 3),
    _PerPoolNodeNodeAddress_Type()
)
perPoolNodeNodeAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perPoolNodeNodeAddress.setStatus("current")


class _PerPoolNodeNodePort_Type(Integer32):
    """Custom type perPoolNodeNodePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PerPoolNodeNodePort_Type.__name__ = "Integer32"
_PerPoolNodeNodePort_Object = MibTableColumn
perPoolNodeNodePort = _PerPoolNodeNodePort_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 4, 6, 1, 4),
    _PerPoolNodeNodePort_Type()
)
perPoolNodeNodePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perPoolNodeNodePort.setStatus("current")


class _PerPoolNodeNodeHostName_Type(DisplayString):
    """Custom type perPoolNodeNodeHostName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PerPoolNodeNodeHostName_Type.__name__ = "DisplayString"
_PerPoolNodeNodeHostName_Object = MibTableColumn
perPoolNodeNodeHostName = _PerPoolNodeNodeHostName_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 4, 6, 1, 5),
    _PerPoolNodeNodeHostName_Type()
)
perPoolNodeNodeHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perPoolNodeNodeHostName.setStatus("current")


class _PerPoolNodeState_Type(Integer32):
    """Custom type perPoolNodeState based on Integer32"""
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
        *(("alive", 1),
          ("dead", 2),
          ("draining", 4),
          ("drainingtodelete", 5),
          ("unknown", 3))
    )


_PerPoolNodeState_Type.__name__ = "Integer32"
_PerPoolNodeState_Object = MibTableColumn
perPoolNodeState = _PerPoolNodeState_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 4, 6, 1, 6),
    _PerPoolNodeState_Type()
)
perPoolNodeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perPoolNodeState.setStatus("current")
_PerPoolNodeBytesToNodeLo_Type = Counter32
_PerPoolNodeBytesToNodeLo_Object = MibTableColumn
perPoolNodeBytesToNodeLo = _PerPoolNodeBytesToNodeLo_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 4, 6, 1, 7),
    _PerPoolNodeBytesToNodeLo_Type()
)
perPoolNodeBytesToNodeLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perPoolNodeBytesToNodeLo.setStatus("obsolete")
_PerPoolNodeBytesToNodeHi_Type = Counter32
_PerPoolNodeBytesToNodeHi_Object = MibTableColumn
perPoolNodeBytesToNodeHi = _PerPoolNodeBytesToNodeHi_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 4, 6, 1, 8),
    _PerPoolNodeBytesToNodeHi_Type()
)
perPoolNodeBytesToNodeHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perPoolNodeBytesToNodeHi.setStatus("obsolete")
_PerPoolNodeBytesFromNodeLo_Type = Counter32
_PerPoolNodeBytesFromNodeLo_Object = MibTableColumn
perPoolNodeBytesFromNodeLo = _PerPoolNodeBytesFromNodeLo_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 4, 6, 1, 9),
    _PerPoolNodeBytesFromNodeLo_Type()
)
perPoolNodeBytesFromNodeLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perPoolNodeBytesFromNodeLo.setStatus("obsolete")
_PerPoolNodeBytesFromNodeHi_Type = Counter32
_PerPoolNodeBytesFromNodeHi_Object = MibTableColumn
perPoolNodeBytesFromNodeHi = _PerPoolNodeBytesFromNodeHi_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 4, 6, 1, 10),
    _PerPoolNodeBytesFromNodeHi_Type()
)
perPoolNodeBytesFromNodeHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perPoolNodeBytesFromNodeHi.setStatus("obsolete")
_PerPoolNodeCurrentRequests_Type = Gauge32
_PerPoolNodeCurrentRequests_Object = MibTableColumn
perPoolNodeCurrentRequests = _PerPoolNodeCurrentRequests_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 4, 6, 1, 11),
    _PerPoolNodeCurrentRequests_Type()
)
perPoolNodeCurrentRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perPoolNodeCurrentRequests.setStatus("current")
_PerPoolNodeTotalConn_Type = Counter32
_PerPoolNodeTotalConn_Object = MibTableColumn
perPoolNodeTotalConn = _PerPoolNodeTotalConn_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 4, 6, 1, 12),
    _PerPoolNodeTotalConn_Type()
)
perPoolNodeTotalConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perPoolNodeTotalConn.setStatus("current")
_PerPoolNodePooledConn_Type = Counter32
_PerPoolNodePooledConn_Object = MibTableColumn
perPoolNodePooledConn = _PerPoolNodePooledConn_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 4, 6, 1, 13),
    _PerPoolNodePooledConn_Type()
)
perPoolNodePooledConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perPoolNodePooledConn.setStatus("current")
_PerPoolNodeFailures_Type = Counter32
_PerPoolNodeFailures_Object = MibTableColumn
perPoolNodeFailures = _PerPoolNodeFailures_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 4, 6, 1, 14),
    _PerPoolNodeFailures_Type()
)
perPoolNodeFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perPoolNodeFailures.setStatus("current")
_PerPoolNodeNewConn_Type = Counter32
_PerPoolNodeNewConn_Object = MibTableColumn
perPoolNodeNewConn = _PerPoolNodeNewConn_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 4, 6, 1, 15),
    _PerPoolNodeNewConn_Type()
)
perPoolNodeNewConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perPoolNodeNewConn.setStatus("current")
_PerPoolNodeErrors_Type = Counter32
_PerPoolNodeErrors_Object = MibTableColumn
perPoolNodeErrors = _PerPoolNodeErrors_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 4, 6, 1, 16),
    _PerPoolNodeErrors_Type()
)
perPoolNodeErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perPoolNodeErrors.setStatus("current")
_PerPoolNodeResponseMin_Type = Gauge32
_PerPoolNodeResponseMin_Object = MibTableColumn
perPoolNodeResponseMin = _PerPoolNodeResponseMin_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 4, 6, 1, 17),
    _PerPoolNodeResponseMin_Type()
)
perPoolNodeResponseMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perPoolNodeResponseMin.setStatus("current")
_PerPoolNodeResponseMax_Type = Gauge32
_PerPoolNodeResponseMax_Object = MibTableColumn
perPoolNodeResponseMax = _PerPoolNodeResponseMax_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 4, 6, 1, 18),
    _PerPoolNodeResponseMax_Type()
)
perPoolNodeResponseMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perPoolNodeResponseMax.setStatus("current")
_PerPoolNodeResponseMean_Type = Gauge32
_PerPoolNodeResponseMean_Object = MibTableColumn
perPoolNodeResponseMean = _PerPoolNodeResponseMean_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 4, 6, 1, 19),
    _PerPoolNodeResponseMean_Type()
)
perPoolNodeResponseMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perPoolNodeResponseMean.setStatus("current")
_PerPoolNodeIdleConns_Type = Gauge32
_PerPoolNodeIdleConns_Object = MibTableColumn
perPoolNodeIdleConns = _PerPoolNodeIdleConns_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 4, 6, 1, 20),
    _PerPoolNodeIdleConns_Type()
)
perPoolNodeIdleConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perPoolNodeIdleConns.setStatus("current")
_PerPoolNodeCurrentConn_Type = Gauge32
_PerPoolNodeCurrentConn_Object = MibTableColumn
perPoolNodeCurrentConn = _PerPoolNodeCurrentConn_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 4, 6, 1, 21),
    _PerPoolNodeCurrentConn_Type()
)
perPoolNodeCurrentConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perPoolNodeCurrentConn.setStatus("current")
_PerPoolNodePktsToNodeLo_Type = Counter32
_PerPoolNodePktsToNodeLo_Object = MibTableColumn
perPoolNodePktsToNodeLo = _PerPoolNodePktsToNodeLo_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 4, 6, 1, 22),
    _PerPoolNodePktsToNodeLo_Type()
)
perPoolNodePktsToNodeLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perPoolNodePktsToNodeLo.setStatus("obsolete")
_PerPoolNodePktsToNodeHi_Type = Counter32
_PerPoolNodePktsToNodeHi_Object = MibTableColumn
perPoolNodePktsToNodeHi = _PerPoolNodePktsToNodeHi_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 4, 6, 1, 23),
    _PerPoolNodePktsToNodeHi_Type()
)
perPoolNodePktsToNodeHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perPoolNodePktsToNodeHi.setStatus("obsolete")
_PerPoolNodePktsFromNodeLo_Type = Counter32
_PerPoolNodePktsFromNodeLo_Object = MibTableColumn
perPoolNodePktsFromNodeLo = _PerPoolNodePktsFromNodeLo_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 4, 6, 1, 24),
    _PerPoolNodePktsFromNodeLo_Type()
)
perPoolNodePktsFromNodeLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perPoolNodePktsFromNodeLo.setStatus("obsolete")
_PerPoolNodePktsFromNodeHi_Type = Counter32
_PerPoolNodePktsFromNodeHi_Object = MibTableColumn
perPoolNodePktsFromNodeHi = _PerPoolNodePktsFromNodeHi_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 4, 6, 1, 25),
    _PerPoolNodePktsFromNodeHi_Type()
)
perPoolNodePktsFromNodeHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perPoolNodePktsFromNodeHi.setStatus("obsolete")
_PerPoolNodeL4StatelessBuckets_Type = Gauge32
_PerPoolNodeL4StatelessBuckets_Object = MibTableColumn
perPoolNodeL4StatelessBuckets = _PerPoolNodeL4StatelessBuckets_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 4, 6, 1, 26),
    _PerPoolNodeL4StatelessBuckets_Type()
)
perPoolNodeL4StatelessBuckets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perPoolNodeL4StatelessBuckets.setStatus("current")
_PerPoolNodeBytesToNode_Type = Counter64
_PerPoolNodeBytesToNode_Object = MibTableColumn
perPoolNodeBytesToNode = _PerPoolNodeBytesToNode_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 4, 6, 1, 27),
    _PerPoolNodeBytesToNode_Type()
)
perPoolNodeBytesToNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perPoolNodeBytesToNode.setStatus("current")
_PerPoolNodeBytesFromNode_Type = Counter64
_PerPoolNodeBytesFromNode_Object = MibTableColumn
perPoolNodeBytesFromNode = _PerPoolNodeBytesFromNode_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 4, 6, 1, 28),
    _PerPoolNodeBytesFromNode_Type()
)
perPoolNodeBytesFromNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perPoolNodeBytesFromNode.setStatus("current")
_PerPoolNodePktsToNode_Type = Counter64
_PerPoolNodePktsToNode_Object = MibTableColumn
perPoolNodePktsToNode = _PerPoolNodePktsToNode_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 4, 6, 1, 29),
    _PerPoolNodePktsToNode_Type()
)
perPoolNodePktsToNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perPoolNodePktsToNode.setStatus("current")
_PerPoolNodePktsFromNode_Type = Counter64
_PerPoolNodePktsFromNode_Object = MibTableColumn
perPoolNodePktsFromNode = _PerPoolNodePktsFromNode_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 4, 6, 1, 30),
    _PerPoolNodePktsFromNode_Type()
)
perPoolNodePktsFromNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perPoolNodePktsFromNode.setStatus("current")
_Serviceprotection_ObjectIdentity = ObjectIdentity
serviceprotection = _Serviceprotection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 5)
)
_ServiceProtNumber_Type = Integer32
_ServiceProtNumber_Object = MibScalar
serviceProtNumber = _ServiceProtNumber_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 5, 1),
    _ServiceProtNumber_Type()
)
serviceProtNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serviceProtNumber.setStatus("current")
_ServiceProtTable_Object = MibTable
serviceProtTable = _ServiceProtTable_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 5, 2)
)
if mibBuilder.loadTexts:
    serviceProtTable.setStatus("current")
_ServiceProtEntry_Object = MibTableRow
serviceProtEntry = _ServiceProtEntry_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 5, 2, 1)
)
serviceProtEntry.setIndexNames(
    (0, "ZXTM-MIB-SMIv2", "serviceProtName"),
)
if mibBuilder.loadTexts:
    serviceProtEntry.setStatus("current")


class _ServiceProtName_Type(DisplayString):
    """Custom type serviceProtName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ServiceProtName_Type.__name__ = "DisplayString"
_ServiceProtName_Object = MibTableColumn
serviceProtName = _ServiceProtName_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 5, 2, 1, 1),
    _ServiceProtName_Type()
)
serviceProtName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serviceProtName.setStatus("current")
_ServiceProtTotalRefusal_Type = Counter32
_ServiceProtTotalRefusal_Object = MibTableColumn
serviceProtTotalRefusal = _ServiceProtTotalRefusal_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 5, 2, 1, 2),
    _ServiceProtTotalRefusal_Type()
)
serviceProtTotalRefusal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serviceProtTotalRefusal.setStatus("current")
_ServiceProtLastRefusalTime_Type = TimeTicks
_ServiceProtLastRefusalTime_Object = MibTableColumn
serviceProtLastRefusalTime = _ServiceProtLastRefusalTime_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 5, 2, 1, 3),
    _ServiceProtLastRefusalTime_Type()
)
serviceProtLastRefusalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serviceProtLastRefusalTime.setStatus("current")
_ServiceProtRefusalIP_Type = Counter32
_ServiceProtRefusalIP_Object = MibTableColumn
serviceProtRefusalIP = _ServiceProtRefusalIP_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 5, 2, 1, 4),
    _ServiceProtRefusalIP_Type()
)
serviceProtRefusalIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serviceProtRefusalIP.setStatus("current")
_ServiceProtRefusalConc1IP_Type = Counter32
_ServiceProtRefusalConc1IP_Object = MibTableColumn
serviceProtRefusalConc1IP = _ServiceProtRefusalConc1IP_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 5, 2, 1, 5),
    _ServiceProtRefusalConc1IP_Type()
)
serviceProtRefusalConc1IP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serviceProtRefusalConc1IP.setStatus("current")
_ServiceProtRefusalConc10IP_Type = Counter32
_ServiceProtRefusalConc10IP_Object = MibTableColumn
serviceProtRefusalConc10IP = _ServiceProtRefusalConc10IP_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 5, 2, 1, 6),
    _ServiceProtRefusalConc10IP_Type()
)
serviceProtRefusalConc10IP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serviceProtRefusalConc10IP.setStatus("current")
_ServiceProtRefusalConnRate_Type = Counter32
_ServiceProtRefusalConnRate_Object = MibTableColumn
serviceProtRefusalConnRate = _ServiceProtRefusalConnRate_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 5, 2, 1, 7),
    _ServiceProtRefusalConnRate_Type()
)
serviceProtRefusalConnRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serviceProtRefusalConnRate.setStatus("current")
_ServiceProtRefusalRFC2396_Type = Counter32
_ServiceProtRefusalRFC2396_Object = MibTableColumn
serviceProtRefusalRFC2396 = _ServiceProtRefusalRFC2396_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 5, 2, 1, 8),
    _ServiceProtRefusalRFC2396_Type()
)
serviceProtRefusalRFC2396.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serviceProtRefusalRFC2396.setStatus("current")
_ServiceProtRefusalSize_Type = Counter32
_ServiceProtRefusalSize_Object = MibTableColumn
serviceProtRefusalSize = _ServiceProtRefusalSize_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 5, 2, 1, 9),
    _ServiceProtRefusalSize_Type()
)
serviceProtRefusalSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serviceProtRefusalSize.setStatus("current")
_ServiceProtRefusalBinary_Type = Counter32
_ServiceProtRefusalBinary_Object = MibTableColumn
serviceProtRefusalBinary = _ServiceProtRefusalBinary_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 5, 2, 1, 10),
    _ServiceProtRefusalBinary_Type()
)
serviceProtRefusalBinary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serviceProtRefusalBinary.setStatus("current")
_Trafficips_ObjectIdentity = ObjectIdentity
trafficips = _Trafficips_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 6)
)
_TrafficIPNumber_Type = Integer32
_TrafficIPNumber_Object = MibScalar
trafficIPNumber = _TrafficIPNumber_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 6, 1),
    _TrafficIPNumber_Type()
)
trafficIPNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trafficIPNumber.setStatus("obsolete")
_TrafficIPNumberRaised_Type = Integer32
_TrafficIPNumberRaised_Object = MibScalar
trafficIPNumberRaised = _TrafficIPNumberRaised_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 6, 2),
    _TrafficIPNumberRaised_Type()
)
trafficIPNumberRaised.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trafficIPNumberRaised.setStatus("obsolete")
_TrafficIPTable_Object = MibTable
trafficIPTable = _TrafficIPTable_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 6, 3)
)
if mibBuilder.loadTexts:
    trafficIPTable.setStatus("obsolete")
_TrafficIPEntry_Object = MibTableRow
trafficIPEntry = _TrafficIPEntry_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 6, 3, 1)
)
trafficIPEntry.setIndexNames(
    (0, "ZXTM-MIB-SMIv2", "trafficIPAddress"),
)
if mibBuilder.loadTexts:
    trafficIPEntry.setStatus("obsolete")
_TrafficIPAddress_Type = IpAddress
_TrafficIPAddress_Object = MibTableColumn
trafficIPAddress = _TrafficIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 6, 3, 1, 1),
    _TrafficIPAddress_Type()
)
trafficIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trafficIPAddress.setStatus("obsolete")


class _TrafficIPState_Type(Integer32):
    """Custom type trafficIPState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lowered", 2),
          ("raised", 1))
    )


_TrafficIPState_Type.__name__ = "Integer32"
_TrafficIPState_Object = MibTableColumn
trafficIPState = _TrafficIPState_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 6, 3, 1, 2),
    _TrafficIPState_Type()
)
trafficIPState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trafficIPState.setStatus("obsolete")
_TrafficIPTime_Type = TimeTicks
_TrafficIPTime_Object = MibTableColumn
trafficIPTime = _TrafficIPTime_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 6, 3, 1, 3),
    _TrafficIPTime_Type()
)
trafficIPTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trafficIPTime.setStatus("obsolete")
_TrafficIPGatewayPingRequests_Type = Counter32
_TrafficIPGatewayPingRequests_Object = MibScalar
trafficIPGatewayPingRequests = _TrafficIPGatewayPingRequests_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 6, 4),
    _TrafficIPGatewayPingRequests_Type()
)
trafficIPGatewayPingRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trafficIPGatewayPingRequests.setStatus("current")
_TrafficIPGatewayPingResponses_Type = Counter32
_TrafficIPGatewayPingResponses_Object = MibScalar
trafficIPGatewayPingResponses = _TrafficIPGatewayPingResponses_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 6, 5),
    _TrafficIPGatewayPingResponses_Type()
)
trafficIPGatewayPingResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trafficIPGatewayPingResponses.setStatus("current")
_TrafficIPNodePingRequests_Type = Counter32
_TrafficIPNodePingRequests_Object = MibScalar
trafficIPNodePingRequests = _TrafficIPNodePingRequests_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 6, 6),
    _TrafficIPNodePingRequests_Type()
)
trafficIPNodePingRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trafficIPNodePingRequests.setStatus("current")
_TrafficIPNodePingResponses_Type = Counter32
_TrafficIPNodePingResponses_Object = MibScalar
trafficIPNodePingResponses = _TrafficIPNodePingResponses_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 6, 7),
    _TrafficIPNodePingResponses_Type()
)
trafficIPNodePingResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trafficIPNodePingResponses.setStatus("current")
_TrafficIPPingResponseErrors_Type = Counter32
_TrafficIPPingResponseErrors_Object = MibScalar
trafficIPPingResponseErrors = _TrafficIPPingResponseErrors_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 6, 8),
    _TrafficIPPingResponseErrors_Type()
)
trafficIPPingResponseErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trafficIPPingResponseErrors.setStatus("current")
_TrafficIPARPMessage_Type = Counter32
_TrafficIPARPMessage_Object = MibScalar
trafficIPARPMessage = _TrafficIPARPMessage_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 6, 9),
    _TrafficIPARPMessage_Type()
)
trafficIPARPMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trafficIPARPMessage.setStatus("current")
_TrafficIPNumberInet46_Type = Integer32
_TrafficIPNumberInet46_Object = MibScalar
trafficIPNumberInet46 = _TrafficIPNumberInet46_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 6, 10),
    _TrafficIPNumberInet46_Type()
)
trafficIPNumberInet46.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trafficIPNumberInet46.setStatus("current")
_TrafficIPNumberRaisedInet46_Type = Integer32
_TrafficIPNumberRaisedInet46_Object = MibScalar
trafficIPNumberRaisedInet46 = _TrafficIPNumberRaisedInet46_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 6, 11),
    _TrafficIPNumberRaisedInet46_Type()
)
trafficIPNumberRaisedInet46.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trafficIPNumberRaisedInet46.setStatus("current")
_TrafficIPInet46Table_Object = MibTable
trafficIPInet46Table = _TrafficIPInet46Table_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 6, 12)
)
if mibBuilder.loadTexts:
    trafficIPInet46Table.setStatus("current")
_TrafficIPInet46Entry_Object = MibTableRow
trafficIPInet46Entry = _TrafficIPInet46Entry_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 6, 12, 1)
)
trafficIPInet46Entry.setIndexNames(
    (0, "ZXTM-MIB-SMIv2", "trafficIPInet46AddressType"),
    (0, "ZXTM-MIB-SMIv2", "trafficIPInet46Address"),
)
if mibBuilder.loadTexts:
    trafficIPInet46Entry.setStatus("current")
_TrafficIPInet46AddressType_Type = InetAddressType
_TrafficIPInet46AddressType_Object = MibTableColumn
trafficIPInet46AddressType = _TrafficIPInet46AddressType_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 6, 12, 1, 1),
    _TrafficIPInet46AddressType_Type()
)
trafficIPInet46AddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trafficIPInet46AddressType.setStatus("current")


class _TrafficIPInet46Address_Type(InetAddress):
    """Custom type trafficIPInet46Address based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_TrafficIPInet46Address_Type.__name__ = "InetAddress"
_TrafficIPInet46Address_Object = MibTableColumn
trafficIPInet46Address = _TrafficIPInet46Address_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 6, 12, 1, 2),
    _TrafficIPInet46Address_Type()
)
trafficIPInet46Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trafficIPInet46Address.setStatus("current")


class _TrafficIPInet46State_Type(Integer32):
    """Custom type trafficIPInet46State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lowered", 2),
          ("raised", 1))
    )


_TrafficIPInet46State_Type.__name__ = "Integer32"
_TrafficIPInet46State_Object = MibTableColumn
trafficIPInet46State = _TrafficIPInet46State_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 6, 12, 1, 3),
    _TrafficIPInet46State_Type()
)
trafficIPInet46State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trafficIPInet46State.setStatus("current")
_TrafficIPInet46Time_Type = TimeTicks
_TrafficIPInet46Time_Object = MibTableColumn
trafficIPInet46Time = _TrafficIPInet46Time_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 6, 12, 1, 4),
    _TrafficIPInet46Time_Type()
)
trafficIPInet46Time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trafficIPInet46Time.setStatus("current")
_Servicelevelmonitoring_ObjectIdentity = ObjectIdentity
servicelevelmonitoring = _Servicelevelmonitoring_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 7)
)
_ServiceLevelNumber_Type = Integer32
_ServiceLevelNumber_Object = MibScalar
serviceLevelNumber = _ServiceLevelNumber_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 7, 1),
    _ServiceLevelNumber_Type()
)
serviceLevelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serviceLevelNumber.setStatus("current")
_ServiceLevelTable_Object = MibTable
serviceLevelTable = _ServiceLevelTable_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 7, 2)
)
if mibBuilder.loadTexts:
    serviceLevelTable.setStatus("current")
_ServiceLevelEntry_Object = MibTableRow
serviceLevelEntry = _ServiceLevelEntry_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 7, 2, 1)
)
serviceLevelEntry.setIndexNames(
    (0, "ZXTM-MIB-SMIv2", "serviceLevelName"),
)
if mibBuilder.loadTexts:
    serviceLevelEntry.setStatus("current")


class _ServiceLevelName_Type(DisplayString):
    """Custom type serviceLevelName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ServiceLevelName_Type.__name__ = "DisplayString"
_ServiceLevelName_Object = MibTableColumn
serviceLevelName = _ServiceLevelName_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 7, 2, 1, 1),
    _ServiceLevelName_Type()
)
serviceLevelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serviceLevelName.setStatus("current")
_ServiceLevelTotalConn_Type = Counter32
_ServiceLevelTotalConn_Object = MibTableColumn
serviceLevelTotalConn = _ServiceLevelTotalConn_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 7, 2, 1, 2),
    _ServiceLevelTotalConn_Type()
)
serviceLevelTotalConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serviceLevelTotalConn.setStatus("current")
_ServiceLevelTotalNonConf_Type = Counter32
_ServiceLevelTotalNonConf_Object = MibTableColumn
serviceLevelTotalNonConf = _ServiceLevelTotalNonConf_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 7, 2, 1, 3),
    _ServiceLevelTotalNonConf_Type()
)
serviceLevelTotalNonConf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serviceLevelTotalNonConf.setStatus("current")
_ServiceLevelResponseMin_Type = Gauge32
_ServiceLevelResponseMin_Object = MibTableColumn
serviceLevelResponseMin = _ServiceLevelResponseMin_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 7, 2, 1, 4),
    _ServiceLevelResponseMin_Type()
)
serviceLevelResponseMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serviceLevelResponseMin.setStatus("current")
_ServiceLevelResponseMax_Type = Gauge32
_ServiceLevelResponseMax_Object = MibTableColumn
serviceLevelResponseMax = _ServiceLevelResponseMax_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 7, 2, 1, 5),
    _ServiceLevelResponseMax_Type()
)
serviceLevelResponseMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serviceLevelResponseMax.setStatus("current")
_ServiceLevelResponseMean_Type = Gauge32
_ServiceLevelResponseMean_Object = MibTableColumn
serviceLevelResponseMean = _ServiceLevelResponseMean_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 7, 2, 1, 6),
    _ServiceLevelResponseMean_Type()
)
serviceLevelResponseMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serviceLevelResponseMean.setStatus("current")


class _ServiceLevelIsOK_Type(Integer32):
    """Custom type serviceLevelIsOK based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notok", 1),
          ("ok", 2))
    )


_ServiceLevelIsOK_Type.__name__ = "Integer32"
_ServiceLevelIsOK_Object = MibTableColumn
serviceLevelIsOK = _ServiceLevelIsOK_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 7, 2, 1, 7),
    _ServiceLevelIsOK_Type()
)
serviceLevelIsOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serviceLevelIsOK.setStatus("current")
_ServiceLevelConforming_Type = Gauge32
_ServiceLevelConforming_Object = MibTableColumn
serviceLevelConforming = _ServiceLevelConforming_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 7, 2, 1, 8),
    _ServiceLevelConforming_Type()
)
serviceLevelConforming.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serviceLevelConforming.setStatus("current")
_ServiceLevelCurrentConns_Type = Gauge32
_ServiceLevelCurrentConns_Object = MibTableColumn
serviceLevelCurrentConns = _ServiceLevelCurrentConns_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 7, 2, 1, 9),
    _ServiceLevelCurrentConns_Type()
)
serviceLevelCurrentConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serviceLevelCurrentConns.setStatus("current")
_Pernodeservicelevelmon_ObjectIdentity = ObjectIdentity
pernodeservicelevelmon = _Pernodeservicelevelmon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 8)
)
_PerNodeServiceLevelTable_Object = MibTable
perNodeServiceLevelTable = _PerNodeServiceLevelTable_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 8, 1)
)
if mibBuilder.loadTexts:
    perNodeServiceLevelTable.setStatus("obsolete")
_PerNodeServiceLevelEntry_Object = MibTableRow
perNodeServiceLevelEntry = _PerNodeServiceLevelEntry_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 8, 1, 1)
)
perNodeServiceLevelEntry.setIndexNames(
    (0, "ZXTM-MIB-SMIv2", "perNodeServiceLevelSLMName"),
    (0, "ZXTM-MIB-SMIv2", "perNodeServiceLevelNodeIPAddr"),
    (0, "ZXTM-MIB-SMIv2", "perNodeServiceLevelNodePort"),
)
if mibBuilder.loadTexts:
    perNodeServiceLevelEntry.setStatus("obsolete")


class _PerNodeServiceLevelSLMName_Type(DisplayString):
    """Custom type perNodeServiceLevelSLMName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PerNodeServiceLevelSLMName_Type.__name__ = "DisplayString"
_PerNodeServiceLevelSLMName_Object = MibTableColumn
perNodeServiceLevelSLMName = _PerNodeServiceLevelSLMName_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 8, 1, 1, 1),
    _PerNodeServiceLevelSLMName_Type()
)
perNodeServiceLevelSLMName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perNodeServiceLevelSLMName.setStatus("obsolete")
_PerNodeServiceLevelNodeIPAddr_Type = IpAddress
_PerNodeServiceLevelNodeIPAddr_Object = MibTableColumn
perNodeServiceLevelNodeIPAddr = _PerNodeServiceLevelNodeIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 8, 1, 1, 2),
    _PerNodeServiceLevelNodeIPAddr_Type()
)
perNodeServiceLevelNodeIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perNodeServiceLevelNodeIPAddr.setStatus("obsolete")


class _PerNodeServiceLevelNodePort_Type(Integer32):
    """Custom type perNodeServiceLevelNodePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PerNodeServiceLevelNodePort_Type.__name__ = "Integer32"
_PerNodeServiceLevelNodePort_Object = MibTableColumn
perNodeServiceLevelNodePort = _PerNodeServiceLevelNodePort_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 8, 1, 1, 3),
    _PerNodeServiceLevelNodePort_Type()
)
perNodeServiceLevelNodePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perNodeServiceLevelNodePort.setStatus("obsolete")
_PerNodeServiceLevelTotalConn_Type = Counter32
_PerNodeServiceLevelTotalConn_Object = MibTableColumn
perNodeServiceLevelTotalConn = _PerNodeServiceLevelTotalConn_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 8, 1, 1, 4),
    _PerNodeServiceLevelTotalConn_Type()
)
perNodeServiceLevelTotalConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perNodeServiceLevelTotalConn.setStatus("obsolete")
_PerNodeServiceLevelTotalNonConf_Type = Counter32
_PerNodeServiceLevelTotalNonConf_Object = MibTableColumn
perNodeServiceLevelTotalNonConf = _PerNodeServiceLevelTotalNonConf_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 8, 1, 1, 5),
    _PerNodeServiceLevelTotalNonConf_Type()
)
perNodeServiceLevelTotalNonConf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perNodeServiceLevelTotalNonConf.setStatus("obsolete")
_PerNodeServiceLevelResponseMin_Type = Gauge32
_PerNodeServiceLevelResponseMin_Object = MibTableColumn
perNodeServiceLevelResponseMin = _PerNodeServiceLevelResponseMin_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 8, 1, 1, 6),
    _PerNodeServiceLevelResponseMin_Type()
)
perNodeServiceLevelResponseMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perNodeServiceLevelResponseMin.setStatus("obsolete")
_PerNodeServiceLevelResponseMax_Type = Gauge32
_PerNodeServiceLevelResponseMax_Object = MibTableColumn
perNodeServiceLevelResponseMax = _PerNodeServiceLevelResponseMax_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 8, 1, 1, 7),
    _PerNodeServiceLevelResponseMax_Type()
)
perNodeServiceLevelResponseMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perNodeServiceLevelResponseMax.setStatus("obsolete")
_PerNodeServiceLevelResponseMean_Type = Gauge32
_PerNodeServiceLevelResponseMean_Object = MibTableColumn
perNodeServiceLevelResponseMean = _PerNodeServiceLevelResponseMean_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 8, 1, 1, 8),
    _PerNodeServiceLevelResponseMean_Type()
)
perNodeServiceLevelResponseMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perNodeServiceLevelResponseMean.setStatus("obsolete")
_PerNodeServiceLevelInet46Table_Object = MibTable
perNodeServiceLevelInet46Table = _PerNodeServiceLevelInet46Table_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 8, 2)
)
if mibBuilder.loadTexts:
    perNodeServiceLevelInet46Table.setStatus("current")
_PerNodeServiceLevelInet46Entry_Object = MibTableRow
perNodeServiceLevelInet46Entry = _PerNodeServiceLevelInet46Entry_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 8, 2, 1)
)
perNodeServiceLevelInet46Entry.setIndexNames(
    (0, "ZXTM-MIB-SMIv2", "perNodeServiceLevelInet46SLMName"),
    (0, "ZXTM-MIB-SMIv2", "perNodeServiceLevelInet46NodeAddressType"),
    (0, "ZXTM-MIB-SMIv2", "perNodeServiceLevelInet46NodeAddress"),
    (0, "ZXTM-MIB-SMIv2", "perNodeServiceLevelInet46NodePort"),
)
if mibBuilder.loadTexts:
    perNodeServiceLevelInet46Entry.setStatus("current")


class _PerNodeServiceLevelInet46SLMName_Type(DisplayString):
    """Custom type perNodeServiceLevelInet46SLMName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PerNodeServiceLevelInet46SLMName_Type.__name__ = "DisplayString"
_PerNodeServiceLevelInet46SLMName_Object = MibTableColumn
perNodeServiceLevelInet46SLMName = _PerNodeServiceLevelInet46SLMName_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 8, 2, 1, 1),
    _PerNodeServiceLevelInet46SLMName_Type()
)
perNodeServiceLevelInet46SLMName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perNodeServiceLevelInet46SLMName.setStatus("current")
_PerNodeServiceLevelInet46NodeAddressType_Type = InetAddressType
_PerNodeServiceLevelInet46NodeAddressType_Object = MibTableColumn
perNodeServiceLevelInet46NodeAddressType = _PerNodeServiceLevelInet46NodeAddressType_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 8, 2, 1, 2),
    _PerNodeServiceLevelInet46NodeAddressType_Type()
)
perNodeServiceLevelInet46NodeAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perNodeServiceLevelInet46NodeAddressType.setStatus("current")


class _PerNodeServiceLevelInet46NodeAddress_Type(InetAddress):
    """Custom type perNodeServiceLevelInet46NodeAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_PerNodeServiceLevelInet46NodeAddress_Type.__name__ = "InetAddress"
_PerNodeServiceLevelInet46NodeAddress_Object = MibTableColumn
perNodeServiceLevelInet46NodeAddress = _PerNodeServiceLevelInet46NodeAddress_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 8, 2, 1, 3),
    _PerNodeServiceLevelInet46NodeAddress_Type()
)
perNodeServiceLevelInet46NodeAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perNodeServiceLevelInet46NodeAddress.setStatus("current")


class _PerNodeServiceLevelInet46NodePort_Type(Integer32):
    """Custom type perNodeServiceLevelInet46NodePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PerNodeServiceLevelInet46NodePort_Type.__name__ = "Integer32"
_PerNodeServiceLevelInet46NodePort_Object = MibTableColumn
perNodeServiceLevelInet46NodePort = _PerNodeServiceLevelInet46NodePort_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 8, 2, 1, 4),
    _PerNodeServiceLevelInet46NodePort_Type()
)
perNodeServiceLevelInet46NodePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perNodeServiceLevelInet46NodePort.setStatus("current")
_PerNodeServiceLevelInet46TotalConn_Type = Counter32
_PerNodeServiceLevelInet46TotalConn_Object = MibTableColumn
perNodeServiceLevelInet46TotalConn = _PerNodeServiceLevelInet46TotalConn_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 8, 2, 1, 5),
    _PerNodeServiceLevelInet46TotalConn_Type()
)
perNodeServiceLevelInet46TotalConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perNodeServiceLevelInet46TotalConn.setStatus("current")
_PerNodeServiceLevelInet46TotalNonConf_Type = Counter32
_PerNodeServiceLevelInet46TotalNonConf_Object = MibTableColumn
perNodeServiceLevelInet46TotalNonConf = _PerNodeServiceLevelInet46TotalNonConf_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 8, 2, 1, 6),
    _PerNodeServiceLevelInet46TotalNonConf_Type()
)
perNodeServiceLevelInet46TotalNonConf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perNodeServiceLevelInet46TotalNonConf.setStatus("current")
_PerNodeServiceLevelInet46ResponseMin_Type = Gauge32
_PerNodeServiceLevelInet46ResponseMin_Object = MibTableColumn
perNodeServiceLevelInet46ResponseMin = _PerNodeServiceLevelInet46ResponseMin_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 8, 2, 1, 7),
    _PerNodeServiceLevelInet46ResponseMin_Type()
)
perNodeServiceLevelInet46ResponseMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perNodeServiceLevelInet46ResponseMin.setStatus("current")
_PerNodeServiceLevelInet46ResponseMax_Type = Gauge32
_PerNodeServiceLevelInet46ResponseMax_Object = MibTableColumn
perNodeServiceLevelInet46ResponseMax = _PerNodeServiceLevelInet46ResponseMax_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 8, 2, 1, 8),
    _PerNodeServiceLevelInet46ResponseMax_Type()
)
perNodeServiceLevelInet46ResponseMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perNodeServiceLevelInet46ResponseMax.setStatus("current")
_PerNodeServiceLevelInet46ResponseMean_Type = Gauge32
_PerNodeServiceLevelInet46ResponseMean_Object = MibTableColumn
perNodeServiceLevelInet46ResponseMean = _PerNodeServiceLevelInet46ResponseMean_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 8, 2, 1, 9),
    _PerNodeServiceLevelInet46ResponseMean_Type()
)
perNodeServiceLevelInet46ResponseMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perNodeServiceLevelInet46ResponseMean.setStatus("current")
_Bandwidthmgt_ObjectIdentity = ObjectIdentity
bandwidthmgt = _Bandwidthmgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 9)
)
_BandwidthClassNumber_Type = Integer32
_BandwidthClassNumber_Object = MibScalar
bandwidthClassNumber = _BandwidthClassNumber_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 9, 1),
    _BandwidthClassNumber_Type()
)
bandwidthClassNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandwidthClassNumber.setStatus("current")
_BandwidthClassTable_Object = MibTable
bandwidthClassTable = _BandwidthClassTable_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 9, 2)
)
if mibBuilder.loadTexts:
    bandwidthClassTable.setStatus("current")
_BandwidthClassEntry_Object = MibTableRow
bandwidthClassEntry = _BandwidthClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 9, 2, 1)
)
bandwidthClassEntry.setIndexNames(
    (0, "ZXTM-MIB-SMIv2", "bandwidthClassName"),
)
if mibBuilder.loadTexts:
    bandwidthClassEntry.setStatus("current")


class _BandwidthClassName_Type(DisplayString):
    """Custom type bandwidthClassName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_BandwidthClassName_Type.__name__ = "DisplayString"
_BandwidthClassName_Object = MibTableColumn
bandwidthClassName = _BandwidthClassName_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 9, 2, 1, 1),
    _BandwidthClassName_Type()
)
bandwidthClassName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandwidthClassName.setStatus("current")
_BandwidthClassMaximum_Type = Integer32
_BandwidthClassMaximum_Object = MibTableColumn
bandwidthClassMaximum = _BandwidthClassMaximum_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 9, 2, 1, 2),
    _BandwidthClassMaximum_Type()
)
bandwidthClassMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandwidthClassMaximum.setStatus("current")
_BandwidthClassGuarantee_Type = Integer32
_BandwidthClassGuarantee_Object = MibTableColumn
bandwidthClassGuarantee = _BandwidthClassGuarantee_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 9, 2, 1, 3),
    _BandwidthClassGuarantee_Type()
)
bandwidthClassGuarantee.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandwidthClassGuarantee.setStatus("current")
_BandwidthClassBytesOutLo_Type = Counter32
_BandwidthClassBytesOutLo_Object = MibTableColumn
bandwidthClassBytesOutLo = _BandwidthClassBytesOutLo_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 9, 2, 1, 4),
    _BandwidthClassBytesOutLo_Type()
)
bandwidthClassBytesOutLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandwidthClassBytesOutLo.setStatus("obsolete")
_BandwidthClassBytesOutHi_Type = Counter32
_BandwidthClassBytesOutHi_Object = MibTableColumn
bandwidthClassBytesOutHi = _BandwidthClassBytesOutHi_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 9, 2, 1, 5),
    _BandwidthClassBytesOutHi_Type()
)
bandwidthClassBytesOutHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandwidthClassBytesOutHi.setStatus("obsolete")
_BandwidthClassBytesOut_Type = Counter64
_BandwidthClassBytesOut_Object = MibTableColumn
bandwidthClassBytesOut = _BandwidthClassBytesOut_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 9, 2, 1, 6),
    _BandwidthClassBytesOut_Type()
)
bandwidthClassBytesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandwidthClassBytesOut.setStatus("current")
_BandwidthClassPktsDrop_Type = Counter64
_BandwidthClassPktsDrop_Object = MibTableColumn
bandwidthClassPktsDrop = _BandwidthClassPktsDrop_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 9, 2, 1, 7),
    _BandwidthClassPktsDrop_Type()
)
bandwidthClassPktsDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandwidthClassPktsDrop.setStatus("current")
_BandwidthClassPktsDropLo_Type = Counter32
_BandwidthClassPktsDropLo_Object = MibTableColumn
bandwidthClassPktsDropLo = _BandwidthClassPktsDropLo_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 9, 2, 1, 8),
    _BandwidthClassPktsDropLo_Type()
)
bandwidthClassPktsDropLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandwidthClassPktsDropLo.setStatus("obsolete")
_BandwidthClassPktsDropHi_Type = Counter32
_BandwidthClassPktsDropHi_Object = MibTableColumn
bandwidthClassPktsDropHi = _BandwidthClassPktsDropHi_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 9, 2, 1, 9),
    _BandwidthClassPktsDropHi_Type()
)
bandwidthClassPktsDropHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandwidthClassPktsDropHi.setStatus("obsolete")
_BandwidthClassBytesDrop_Type = Counter64
_BandwidthClassBytesDrop_Object = MibTableColumn
bandwidthClassBytesDrop = _BandwidthClassBytesDrop_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 9, 2, 1, 10),
    _BandwidthClassBytesDrop_Type()
)
bandwidthClassBytesDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandwidthClassBytesDrop.setStatus("current")
_BandwidthClassBytesDropLo_Type = Counter32
_BandwidthClassBytesDropLo_Object = MibTableColumn
bandwidthClassBytesDropLo = _BandwidthClassBytesDropLo_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 9, 2, 1, 11),
    _BandwidthClassBytesDropLo_Type()
)
bandwidthClassBytesDropLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandwidthClassBytesDropLo.setStatus("obsolete")
_BandwidthClassBytesDropHi_Type = Counter32
_BandwidthClassBytesDropHi_Object = MibTableColumn
bandwidthClassBytesDropHi = _BandwidthClassBytesDropHi_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 9, 2, 1, 12),
    _BandwidthClassBytesDropHi_Type()
)
bandwidthClassBytesDropHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandwidthClassBytesDropHi.setStatus("obsolete")
_Connratelimit_ObjectIdentity = ObjectIdentity
connratelimit = _Connratelimit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 10)
)
_RateClassNumber_Type = Integer32
_RateClassNumber_Object = MibScalar
rateClassNumber = _RateClassNumber_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 10, 1),
    _RateClassNumber_Type()
)
rateClassNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rateClassNumber.setStatus("current")
_RateClassTable_Object = MibTable
rateClassTable = _RateClassTable_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 10, 2)
)
if mibBuilder.loadTexts:
    rateClassTable.setStatus("current")
_RateClassEntry_Object = MibTableRow
rateClassEntry = _RateClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 10, 2, 1)
)
rateClassEntry.setIndexNames(
    (0, "ZXTM-MIB-SMIv2", "rateClassName"),
)
if mibBuilder.loadTexts:
    rateClassEntry.setStatus("current")


class _RateClassName_Type(DisplayString):
    """Custom type rateClassName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RateClassName_Type.__name__ = "DisplayString"
_RateClassName_Object = MibTableColumn
rateClassName = _RateClassName_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 10, 2, 1, 1),
    _RateClassName_Type()
)
rateClassName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rateClassName.setStatus("current")
_RateClassMaxRatePerMin_Type = Integer32
_RateClassMaxRatePerMin_Object = MibTableColumn
rateClassMaxRatePerMin = _RateClassMaxRatePerMin_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 10, 2, 1, 2),
    _RateClassMaxRatePerMin_Type()
)
rateClassMaxRatePerMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rateClassMaxRatePerMin.setStatus("current")
_RateClassMaxRatePerSec_Type = Integer32
_RateClassMaxRatePerSec_Object = MibTableColumn
rateClassMaxRatePerSec = _RateClassMaxRatePerSec_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 10, 2, 1, 3),
    _RateClassMaxRatePerSec_Type()
)
rateClassMaxRatePerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rateClassMaxRatePerSec.setStatus("current")
_RateClassQueueLength_Type = Gauge32
_RateClassQueueLength_Object = MibTableColumn
rateClassQueueLength = _RateClassQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 10, 2, 1, 4),
    _RateClassQueueLength_Type()
)
rateClassQueueLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rateClassQueueLength.setStatus("current")
_RateClassCurrentRate_Type = Gauge32
_RateClassCurrentRate_Object = MibTableColumn
rateClassCurrentRate = _RateClassCurrentRate_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 10, 2, 1, 5),
    _RateClassCurrentRate_Type()
)
rateClassCurrentRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rateClassCurrentRate.setStatus("current")
_RateClassDropped_Type = Counter32
_RateClassDropped_Object = MibTableColumn
rateClassDropped = _RateClassDropped_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 10, 2, 1, 6),
    _RateClassDropped_Type()
)
rateClassDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rateClassDropped.setStatus("current")
_RateClassConnsEntered_Type = Counter32
_RateClassConnsEntered_Object = MibTableColumn
rateClassConnsEntered = _RateClassConnsEntered_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 10, 2, 1, 7),
    _RateClassConnsEntered_Type()
)
rateClassConnsEntered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rateClassConnsEntered.setStatus("current")
_RateClassConnsLeft_Type = Counter32
_RateClassConnsLeft_Object = MibTableColumn
rateClassConnsLeft = _RateClassConnsLeft_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 10, 2, 1, 8),
    _RateClassConnsLeft_Type()
)
rateClassConnsLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rateClassConnsLeft.setStatus("current")
_Extra_ObjectIdentity = ObjectIdentity
extra = _Extra_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 11)
)
_UserCounterNumber_Type = Integer32
_UserCounterNumber_Object = MibScalar
userCounterNumber = _UserCounterNumber_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 11, 1),
    _UserCounterNumber_Type()
)
userCounterNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userCounterNumber.setStatus("current")
_UserCounterTable_Object = MibTable
userCounterTable = _UserCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 11, 2)
)
if mibBuilder.loadTexts:
    userCounterTable.setStatus("current")
_UserCounterEntry_Object = MibTableRow
userCounterEntry = _UserCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 11, 2, 1)
)
userCounterEntry.setIndexNames(
    (0, "ZXTM-MIB-SMIv2", "userCounterName"),
)
if mibBuilder.loadTexts:
    userCounterEntry.setStatus("current")


class _UserCounterName_Type(DisplayString):
    """Custom type userCounterName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_UserCounterName_Type.__name__ = "DisplayString"
_UserCounterName_Object = MibTableColumn
userCounterName = _UserCounterName_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 11, 2, 1, 1),
    _UserCounterName_Type()
)
userCounterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userCounterName.setStatus("current")
_UserCounterValue_Type = Counter32
_UserCounterValue_Object = MibTableColumn
userCounterValue = _UserCounterValue_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 11, 2, 1, 2),
    _UserCounterValue_Type()
)
userCounterValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userCounterValue.setStatus("current")
_UserCounter64Table_Object = MibTable
userCounter64Table = _UserCounter64Table_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 11, 3)
)
if mibBuilder.loadTexts:
    userCounter64Table.setStatus("current")
_UserCounter64Entry_Object = MibTableRow
userCounter64Entry = _UserCounter64Entry_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 11, 3, 1)
)
userCounter64Entry.setIndexNames(
    (0, "ZXTM-MIB-SMIv2", "userCounter64Name"),
)
if mibBuilder.loadTexts:
    userCounter64Entry.setStatus("current")


class _UserCounter64Name_Type(DisplayString):
    """Custom type userCounter64Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_UserCounter64Name_Type.__name__ = "DisplayString"
_UserCounter64Name_Object = MibTableColumn
userCounter64Name = _UserCounter64Name_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 11, 3, 1, 1),
    _UserCounter64Name_Type()
)
userCounter64Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userCounter64Name.setStatus("current")
_UserCounter64Value_Type = Counter64
_UserCounter64Value_Object = MibTableColumn
userCounter64Value = _UserCounter64Value_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 11, 3, 1, 2),
    _UserCounter64Value_Type()
)
userCounter64Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userCounter64Value.setStatus("current")
_Netinterfaces_ObjectIdentity = ObjectIdentity
netinterfaces = _Netinterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 12)
)
_InterfaceNumber_Type = Integer32
_InterfaceNumber_Object = MibScalar
interfaceNumber = _InterfaceNumber_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 12, 1),
    _InterfaceNumber_Type()
)
interfaceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceNumber.setStatus("current")
_InterfaceTable_Object = MibTable
interfaceTable = _InterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 12, 2)
)
if mibBuilder.loadTexts:
    interfaceTable.setStatus("current")
_InterfaceEntry_Object = MibTableRow
interfaceEntry = _InterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 12, 2, 1)
)
interfaceEntry.setIndexNames(
    (0, "ZXTM-MIB-SMIv2", "interfaceName"),
)
if mibBuilder.loadTexts:
    interfaceEntry.setStatus("current")


class _InterfaceName_Type(DisplayString):
    """Custom type interfaceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_InterfaceName_Type.__name__ = "DisplayString"
_InterfaceName_Object = MibTableColumn
interfaceName = _InterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 12, 2, 1, 1),
    _InterfaceName_Type()
)
interfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceName.setStatus("current")
_InterfaceRxPackets_Type = Counter32
_InterfaceRxPackets_Object = MibTableColumn
interfaceRxPackets = _InterfaceRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 12, 2, 1, 2),
    _InterfaceRxPackets_Type()
)
interfaceRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceRxPackets.setStatus("current")
_InterfaceTxPackets_Type = Counter32
_InterfaceTxPackets_Object = MibTableColumn
interfaceTxPackets = _InterfaceTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 12, 2, 1, 3),
    _InterfaceTxPackets_Type()
)
interfaceTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTxPackets.setStatus("current")
_InterfaceRxErrors_Type = Counter32
_InterfaceRxErrors_Object = MibTableColumn
interfaceRxErrors = _InterfaceRxErrors_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 12, 2, 1, 4),
    _InterfaceRxErrors_Type()
)
interfaceRxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceRxErrors.setStatus("current")
_InterfaceTxErrors_Type = Counter32
_InterfaceTxErrors_Object = MibTableColumn
interfaceTxErrors = _InterfaceTxErrors_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 12, 2, 1, 5),
    _InterfaceTxErrors_Type()
)
interfaceTxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTxErrors.setStatus("current")
_InterfaceCollisions_Type = Counter32
_InterfaceCollisions_Object = MibTableColumn
interfaceCollisions = _InterfaceCollisions_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 12, 2, 1, 6),
    _InterfaceCollisions_Type()
)
interfaceCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceCollisions.setStatus("current")
_InterfaceRxBytesLo_Type = Counter32
_InterfaceRxBytesLo_Object = MibTableColumn
interfaceRxBytesLo = _InterfaceRxBytesLo_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 12, 2, 1, 7),
    _InterfaceRxBytesLo_Type()
)
interfaceRxBytesLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceRxBytesLo.setStatus("obsolete")
_InterfaceRxBytesHi_Type = Counter32
_InterfaceRxBytesHi_Object = MibTableColumn
interfaceRxBytesHi = _InterfaceRxBytesHi_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 12, 2, 1, 8),
    _InterfaceRxBytesHi_Type()
)
interfaceRxBytesHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceRxBytesHi.setStatus("obsolete")
_InterfaceTxBytesLo_Type = Counter32
_InterfaceTxBytesLo_Object = MibTableColumn
interfaceTxBytesLo = _InterfaceTxBytesLo_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 12, 2, 1, 9),
    _InterfaceTxBytesLo_Type()
)
interfaceTxBytesLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTxBytesLo.setStatus("obsolete")
_InterfaceTxBytesHi_Type = Counter32
_InterfaceTxBytesHi_Object = MibTableColumn
interfaceTxBytesHi = _InterfaceTxBytesHi_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 12, 2, 1, 10),
    _InterfaceTxBytesHi_Type()
)
interfaceTxBytesHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTxBytesHi.setStatus("obsolete")
_InterfaceRxBytes_Type = Counter64
_InterfaceRxBytes_Object = MibTableColumn
interfaceRxBytes = _InterfaceRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 12, 2, 1, 11),
    _InterfaceRxBytes_Type()
)
interfaceRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceRxBytes.setStatus("current")
_InterfaceTxBytes_Type = Counter64
_InterfaceTxBytes_Object = MibTableColumn
interfaceTxBytes = _InterfaceTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 12, 2, 1, 12),
    _InterfaceTxBytes_Type()
)
interfaceTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTxBytes.setStatus("current")
_Events_ObjectIdentity = ObjectIdentity
events = _Events_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 13)
)
_EventNumber_Type = Integer32
_EventNumber_Object = MibScalar
eventNumber = _EventNumber_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 13, 1),
    _EventNumber_Type()
)
eventNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventNumber.setStatus("current")
_EventTable_Object = MibTable
eventTable = _EventTable_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 13, 2)
)
if mibBuilder.loadTexts:
    eventTable.setStatus("current")
_EventEntry_Object = MibTableRow
eventEntry = _EventEntry_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 13, 2, 1)
)
eventEntry.setIndexNames(
    (0, "ZXTM-MIB-SMIv2", "eventName"),
)
if mibBuilder.loadTexts:
    eventEntry.setStatus("current")


class _EventName_Type(DisplayString):
    """Custom type eventName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EventName_Type.__name__ = "DisplayString"
_EventName_Object = MibTableColumn
eventName = _EventName_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 13, 2, 1, 1),
    _EventName_Type()
)
eventName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventName.setStatus("current")
_EventsMatched_Type = Counter32
_EventsMatched_Object = MibTableColumn
eventsMatched = _EventsMatched_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 13, 2, 1, 2),
    _EventsMatched_Type()
)
eventsMatched.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventsMatched.setStatus("current")
_Actions_ObjectIdentity = ObjectIdentity
actions = _Actions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 14)
)
_ActionNumber_Type = Integer32
_ActionNumber_Object = MibScalar
actionNumber = _ActionNumber_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 14, 1),
    _ActionNumber_Type()
)
actionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actionNumber.setStatus("current")
_ActionTable_Object = MibTable
actionTable = _ActionTable_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 14, 2)
)
if mibBuilder.loadTexts:
    actionTable.setStatus("current")
_ActionEntry_Object = MibTableRow
actionEntry = _ActionEntry_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 14, 2, 1)
)
actionEntry.setIndexNames(
    (0, "ZXTM-MIB-SMIv2", "actionName"),
)
if mibBuilder.loadTexts:
    actionEntry.setStatus("current")


class _ActionName_Type(DisplayString):
    """Custom type actionName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ActionName_Type.__name__ = "DisplayString"
_ActionName_Object = MibTableColumn
actionName = _ActionName_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 14, 2, 1, 1),
    _ActionName_Type()
)
actionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actionName.setStatus("current")
_ActionsProcessed_Type = Counter32
_ActionsProcessed_Object = MibTableColumn
actionsProcessed = _ActionsProcessed_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 14, 2, 1, 2),
    _ActionsProcessed_Type()
)
actionsProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actionsProcessed.setStatus("current")
_Zxtmtraps_ObjectIdentity = ObjectIdentity
zxtmtraps = _Zxtmtraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15)
)
_TrapsZero_ObjectIdentity = ObjectIdentity
trapsZero = _TrapsZero_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0)
)
_Persistence_ObjectIdentity = ObjectIdentity
persistence = _Persistence_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 16)
)
_Cache_ObjectIdentity = ObjectIdentity
cache = _Cache_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 17)
)
_Webcache_ObjectIdentity = ObjectIdentity
webcache = _Webcache_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 17, 1)
)
_WebCacheHitsLo_Type = Counter32
_WebCacheHitsLo_Object = MibScalar
webCacheHitsLo = _WebCacheHitsLo_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 17, 1, 1),
    _WebCacheHitsLo_Type()
)
webCacheHitsLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webCacheHitsLo.setStatus("obsolete")
_WebCacheHitsHi_Type = Counter32
_WebCacheHitsHi_Object = MibScalar
webCacheHitsHi = _WebCacheHitsHi_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 17, 1, 2),
    _WebCacheHitsHi_Type()
)
webCacheHitsHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webCacheHitsHi.setStatus("obsolete")
_WebCacheMissesLo_Type = Counter32
_WebCacheMissesLo_Object = MibScalar
webCacheMissesLo = _WebCacheMissesLo_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 17, 1, 3),
    _WebCacheMissesLo_Type()
)
webCacheMissesLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webCacheMissesLo.setStatus("obsolete")
_WebCacheMissesHi_Type = Counter32
_WebCacheMissesHi_Object = MibScalar
webCacheMissesHi = _WebCacheMissesHi_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 17, 1, 4),
    _WebCacheMissesHi_Type()
)
webCacheMissesHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webCacheMissesHi.setStatus("obsolete")
_WebCacheLookupsLo_Type = Counter32
_WebCacheLookupsLo_Object = MibScalar
webCacheLookupsLo = _WebCacheLookupsLo_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 17, 1, 5),
    _WebCacheLookupsLo_Type()
)
webCacheLookupsLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webCacheLookupsLo.setStatus("obsolete")
_WebCacheLookupsHi_Type = Counter32
_WebCacheLookupsHi_Object = MibScalar
webCacheLookupsHi = _WebCacheLookupsHi_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 17, 1, 6),
    _WebCacheLookupsHi_Type()
)
webCacheLookupsHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webCacheLookupsHi.setStatus("obsolete")
_WebCacheMemUsed_Type = Gauge32
_WebCacheMemUsed_Object = MibScalar
webCacheMemUsed = _WebCacheMemUsed_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 17, 1, 7),
    _WebCacheMemUsed_Type()
)
webCacheMemUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webCacheMemUsed.setStatus("current")
_WebCacheMemMaximum_Type = Gauge32
_WebCacheMemMaximum_Object = MibScalar
webCacheMemMaximum = _WebCacheMemMaximum_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 17, 1, 8),
    _WebCacheMemMaximum_Type()
)
webCacheMemMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webCacheMemMaximum.setStatus("current")
_WebCacheHitRate_Type = Gauge32
_WebCacheHitRate_Object = MibScalar
webCacheHitRate = _WebCacheHitRate_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 17, 1, 9),
    _WebCacheHitRate_Type()
)
webCacheHitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webCacheHitRate.setStatus("current")
_WebCacheEntries_Type = Gauge32
_WebCacheEntries_Object = MibScalar
webCacheEntries = _WebCacheEntries_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 17, 1, 10),
    _WebCacheEntries_Type()
)
webCacheEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webCacheEntries.setStatus("current")
_WebCacheMaxEntries_Type = Gauge32
_WebCacheMaxEntries_Object = MibScalar
webCacheMaxEntries = _WebCacheMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 17, 1, 11),
    _WebCacheMaxEntries_Type()
)
webCacheMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webCacheMaxEntries.setStatus("current")
_WebCacheOldest_Type = Gauge32
_WebCacheOldest_Object = MibScalar
webCacheOldest = _WebCacheOldest_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 17, 1, 12),
    _WebCacheOldest_Type()
)
webCacheOldest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webCacheOldest.setStatus("current")
_WebCacheHits_Type = Counter64
_WebCacheHits_Object = MibScalar
webCacheHits = _WebCacheHits_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 17, 1, 13),
    _WebCacheHits_Type()
)
webCacheHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webCacheHits.setStatus("current")
_WebCacheMisses_Type = Counter64
_WebCacheMisses_Object = MibScalar
webCacheMisses = _WebCacheMisses_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 17, 1, 14),
    _WebCacheMisses_Type()
)
webCacheMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webCacheMisses.setStatus("current")
_WebCacheLookups_Type = Counter64
_WebCacheLookups_Object = MibScalar
webCacheLookups = _WebCacheLookups_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 17, 1, 15),
    _WebCacheLookups_Type()
)
webCacheLookups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webCacheLookups.setStatus("current")
_WebCacheURLStoreAllocated_Type = Counter64
_WebCacheURLStoreAllocated_Object = MibScalar
webCacheURLStoreAllocated = _WebCacheURLStoreAllocated_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 17, 1, 16),
    _WebCacheURLStoreAllocated_Type()
)
webCacheURLStoreAllocated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webCacheURLStoreAllocated.setStatus("current")
_WebCacheURLStoreFree_Type = Counter64
_WebCacheURLStoreFree_Object = MibScalar
webCacheURLStoreFree = _WebCacheURLStoreFree_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 17, 1, 17),
    _WebCacheURLStoreFree_Type()
)
webCacheURLStoreFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webCacheURLStoreFree.setStatus("current")
_WebCacheURLStoreSize_Type = Counter64
_WebCacheURLStoreSize_Object = MibScalar
webCacheURLStoreSize = _WebCacheURLStoreSize_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 17, 1, 18),
    _WebCacheURLStoreSize_Type()
)
webCacheURLStoreSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webCacheURLStoreSize.setStatus("current")
_WebCacheURLStoreTotalAllocations_Type = Counter64
_WebCacheURLStoreTotalAllocations_Object = MibScalar
webCacheURLStoreTotalAllocations = _WebCacheURLStoreTotalAllocations_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 17, 1, 19),
    _WebCacheURLStoreTotalAllocations_Type()
)
webCacheURLStoreTotalAllocations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webCacheURLStoreTotalAllocations.setStatus("current")
_WebCacheURLStoreTotalFailures_Type = Counter64
_WebCacheURLStoreTotalFailures_Object = MibScalar
webCacheURLStoreTotalFailures = _WebCacheURLStoreTotalFailures_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 17, 1, 20),
    _WebCacheURLStoreTotalFailures_Type()
)
webCacheURLStoreTotalFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webCacheURLStoreTotalFailures.setStatus("current")
_WebCacheURLStoreTotalFrees_Type = Counter64
_WebCacheURLStoreTotalFrees_Object = MibScalar
webCacheURLStoreTotalFrees = _WebCacheURLStoreTotalFrees_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 17, 1, 21),
    _WebCacheURLStoreTotalFrees_Type()
)
webCacheURLStoreTotalFrees.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webCacheURLStoreTotalFrees.setStatus("current")
_Sslcache_ObjectIdentity = ObjectIdentity
sslcache = _Sslcache_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 17, 2)
)
_SslCacheHits_Type = Counter32
_SslCacheHits_Object = MibScalar
sslCacheHits = _SslCacheHits_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 17, 2, 1),
    _SslCacheHits_Type()
)
sslCacheHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslCacheHits.setStatus("current")
_SslCacheMisses_Type = Counter32
_SslCacheMisses_Object = MibScalar
sslCacheMisses = _SslCacheMisses_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 17, 2, 2),
    _SslCacheMisses_Type()
)
sslCacheMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslCacheMisses.setStatus("current")
_SslCacheLookups_Type = Counter32
_SslCacheLookups_Object = MibScalar
sslCacheLookups = _SslCacheLookups_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 17, 2, 3),
    _SslCacheLookups_Type()
)
sslCacheLookups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslCacheLookups.setStatus("current")
_SslCacheHitRate_Type = Gauge32
_SslCacheHitRate_Object = MibScalar
sslCacheHitRate = _SslCacheHitRate_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 17, 2, 4),
    _SslCacheHitRate_Type()
)
sslCacheHitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslCacheHitRate.setStatus("current")
_SslCacheEntries_Type = Gauge32
_SslCacheEntries_Object = MibScalar
sslCacheEntries = _SslCacheEntries_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 17, 2, 5),
    _SslCacheEntries_Type()
)
sslCacheEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslCacheEntries.setStatus("current")
_SslCacheEntriesMax_Type = Gauge32
_SslCacheEntriesMax_Object = MibScalar
sslCacheEntriesMax = _SslCacheEntriesMax_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 17, 2, 6),
    _SslCacheEntriesMax_Type()
)
sslCacheEntriesMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslCacheEntriesMax.setStatus("current")
_SslCacheOldest_Type = Gauge32
_SslCacheOldest_Object = MibScalar
sslCacheOldest = _SslCacheOldest_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 17, 2, 7),
    _SslCacheOldest_Type()
)
sslCacheOldest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslCacheOldest.setStatus("current")
_Aspsessioncache_ObjectIdentity = ObjectIdentity
aspsessioncache = _Aspsessioncache_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 17, 3)
)
_AspSessionCacheHits_Type = Counter32
_AspSessionCacheHits_Object = MibScalar
aspSessionCacheHits = _AspSessionCacheHits_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 17, 3, 1),
    _AspSessionCacheHits_Type()
)
aspSessionCacheHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aspSessionCacheHits.setStatus("current")
_AspSessionCacheMisses_Type = Counter32
_AspSessionCacheMisses_Object = MibScalar
aspSessionCacheMisses = _AspSessionCacheMisses_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 17, 3, 2),
    _AspSessionCacheMisses_Type()
)
aspSessionCacheMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aspSessionCacheMisses.setStatus("current")
_AspSessionCacheLookups_Type = Counter32
_AspSessionCacheLookups_Object = MibScalar
aspSessionCacheLookups = _AspSessionCacheLookups_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 17, 3, 3),
    _AspSessionCacheLookups_Type()
)
aspSessionCacheLookups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aspSessionCacheLookups.setStatus("current")
_AspSessionCacheHitRate_Type = Gauge32
_AspSessionCacheHitRate_Object = MibScalar
aspSessionCacheHitRate = _AspSessionCacheHitRate_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 17, 3, 4),
    _AspSessionCacheHitRate_Type()
)
aspSessionCacheHitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aspSessionCacheHitRate.setStatus("current")
_AspSessionCacheEntries_Type = Gauge32
_AspSessionCacheEntries_Object = MibScalar
aspSessionCacheEntries = _AspSessionCacheEntries_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 17, 3, 5),
    _AspSessionCacheEntries_Type()
)
aspSessionCacheEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aspSessionCacheEntries.setStatus("current")
_AspSessionCacheEntriesMax_Type = Gauge32
_AspSessionCacheEntriesMax_Object = MibScalar
aspSessionCacheEntriesMax = _AspSessionCacheEntriesMax_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 17, 3, 6),
    _AspSessionCacheEntriesMax_Type()
)
aspSessionCacheEntriesMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aspSessionCacheEntriesMax.setStatus("current")
_AspSessionCacheOldest_Type = Gauge32
_AspSessionCacheOldest_Object = MibScalar
aspSessionCacheOldest = _AspSessionCacheOldest_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 17, 3, 7),
    _AspSessionCacheOldest_Type()
)
aspSessionCacheOldest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aspSessionCacheOldest.setStatus("current")
_Ipsessioncache_ObjectIdentity = ObjectIdentity
ipsessioncache = _Ipsessioncache_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 17, 4)
)
_IpSessionCacheHits_Type = Counter32
_IpSessionCacheHits_Object = MibScalar
ipSessionCacheHits = _IpSessionCacheHits_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 17, 4, 1),
    _IpSessionCacheHits_Type()
)
ipSessionCacheHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSessionCacheHits.setStatus("current")
_IpSessionCacheMisses_Type = Counter32
_IpSessionCacheMisses_Object = MibScalar
ipSessionCacheMisses = _IpSessionCacheMisses_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 17, 4, 2),
    _IpSessionCacheMisses_Type()
)
ipSessionCacheMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSessionCacheMisses.setStatus("current")
_IpSessionCacheLookups_Type = Counter32
_IpSessionCacheLookups_Object = MibScalar
ipSessionCacheLookups = _IpSessionCacheLookups_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 17, 4, 3),
    _IpSessionCacheLookups_Type()
)
ipSessionCacheLookups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSessionCacheLookups.setStatus("current")
_IpSessionCacheHitRate_Type = Gauge32
_IpSessionCacheHitRate_Object = MibScalar
ipSessionCacheHitRate = _IpSessionCacheHitRate_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 17, 4, 4),
    _IpSessionCacheHitRate_Type()
)
ipSessionCacheHitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSessionCacheHitRate.setStatus("current")
_IpSessionCacheEntries_Type = Gauge32
_IpSessionCacheEntries_Object = MibScalar
ipSessionCacheEntries = _IpSessionCacheEntries_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 17, 4, 5),
    _IpSessionCacheEntries_Type()
)
ipSessionCacheEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSessionCacheEntries.setStatus("current")
_IpSessionCacheEntriesMax_Type = Gauge32
_IpSessionCacheEntriesMax_Object = MibScalar
ipSessionCacheEntriesMax = _IpSessionCacheEntriesMax_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 17, 4, 6),
    _IpSessionCacheEntriesMax_Type()
)
ipSessionCacheEntriesMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSessionCacheEntriesMax.setStatus("current")
_IpSessionCacheOldest_Type = Gauge32
_IpSessionCacheOldest_Object = MibScalar
ipSessionCacheOldest = _IpSessionCacheOldest_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 17, 4, 7),
    _IpSessionCacheOldest_Type()
)
ipSessionCacheOldest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSessionCacheOldest.setStatus("current")
_J2eesessioncache_ObjectIdentity = ObjectIdentity
j2eesessioncache = _J2eesessioncache_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 17, 5)
)
_J2eeSessionCacheHits_Type = Counter32
_J2eeSessionCacheHits_Object = MibScalar
j2eeSessionCacheHits = _J2eeSessionCacheHits_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 17, 5, 1),
    _J2eeSessionCacheHits_Type()
)
j2eeSessionCacheHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    j2eeSessionCacheHits.setStatus("current")
_J2eeSessionCacheMisses_Type = Counter32
_J2eeSessionCacheMisses_Object = MibScalar
j2eeSessionCacheMisses = _J2eeSessionCacheMisses_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 17, 5, 2),
    _J2eeSessionCacheMisses_Type()
)
j2eeSessionCacheMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    j2eeSessionCacheMisses.setStatus("current")
_J2eeSessionCacheLookups_Type = Counter32
_J2eeSessionCacheLookups_Object = MibScalar
j2eeSessionCacheLookups = _J2eeSessionCacheLookups_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 17, 5, 3),
    _J2eeSessionCacheLookups_Type()
)
j2eeSessionCacheLookups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    j2eeSessionCacheLookups.setStatus("current")
_J2eeSessionCacheHitRate_Type = Gauge32
_J2eeSessionCacheHitRate_Object = MibScalar
j2eeSessionCacheHitRate = _J2eeSessionCacheHitRate_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 17, 5, 4),
    _J2eeSessionCacheHitRate_Type()
)
j2eeSessionCacheHitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    j2eeSessionCacheHitRate.setStatus("current")
_J2eeSessionCacheEntries_Type = Gauge32
_J2eeSessionCacheEntries_Object = MibScalar
j2eeSessionCacheEntries = _J2eeSessionCacheEntries_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 17, 5, 5),
    _J2eeSessionCacheEntries_Type()
)
j2eeSessionCacheEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    j2eeSessionCacheEntries.setStatus("current")
_J2eeSessionCacheEntriesMax_Type = Gauge32
_J2eeSessionCacheEntriesMax_Object = MibScalar
j2eeSessionCacheEntriesMax = _J2eeSessionCacheEntriesMax_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 17, 5, 6),
    _J2eeSessionCacheEntriesMax_Type()
)
j2eeSessionCacheEntriesMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    j2eeSessionCacheEntriesMax.setStatus("current")
_J2eeSessionCacheOldest_Type = Gauge32
_J2eeSessionCacheOldest_Object = MibScalar
j2eeSessionCacheOldest = _J2eeSessionCacheOldest_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 17, 5, 7),
    _J2eeSessionCacheOldest_Type()
)
j2eeSessionCacheOldest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    j2eeSessionCacheOldest.setStatus("current")
_Unisessioncache_ObjectIdentity = ObjectIdentity
unisessioncache = _Unisessioncache_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 17, 6)
)
_UniSessionCacheHits_Type = Counter32
_UniSessionCacheHits_Object = MibScalar
uniSessionCacheHits = _UniSessionCacheHits_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 17, 6, 1),
    _UniSessionCacheHits_Type()
)
uniSessionCacheHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uniSessionCacheHits.setStatus("current")
_UniSessionCacheMisses_Type = Counter32
_UniSessionCacheMisses_Object = MibScalar
uniSessionCacheMisses = _UniSessionCacheMisses_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 17, 6, 2),
    _UniSessionCacheMisses_Type()
)
uniSessionCacheMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uniSessionCacheMisses.setStatus("current")
_UniSessionCacheLookups_Type = Counter32
_UniSessionCacheLookups_Object = MibScalar
uniSessionCacheLookups = _UniSessionCacheLookups_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 17, 6, 3),
    _UniSessionCacheLookups_Type()
)
uniSessionCacheLookups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uniSessionCacheLookups.setStatus("current")
_UniSessionCacheHitRate_Type = Gauge32
_UniSessionCacheHitRate_Object = MibScalar
uniSessionCacheHitRate = _UniSessionCacheHitRate_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 17, 6, 4),
    _UniSessionCacheHitRate_Type()
)
uniSessionCacheHitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uniSessionCacheHitRate.setStatus("current")
_UniSessionCacheEntries_Type = Gauge32
_UniSessionCacheEntries_Object = MibScalar
uniSessionCacheEntries = _UniSessionCacheEntries_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 17, 6, 5),
    _UniSessionCacheEntries_Type()
)
uniSessionCacheEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uniSessionCacheEntries.setStatus("current")
_UniSessionCacheEntriesMax_Type = Gauge32
_UniSessionCacheEntriesMax_Object = MibScalar
uniSessionCacheEntriesMax = _UniSessionCacheEntriesMax_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 17, 6, 6),
    _UniSessionCacheEntriesMax_Type()
)
uniSessionCacheEntriesMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uniSessionCacheEntriesMax.setStatus("current")
_UniSessionCacheOldest_Type = Gauge32
_UniSessionCacheOldest_Object = MibScalar
uniSessionCacheOldest = _UniSessionCacheOldest_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 17, 6, 7),
    _UniSessionCacheOldest_Type()
)
uniSessionCacheOldest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uniSessionCacheOldest.setStatus("current")
_Sslsessioncache_ObjectIdentity = ObjectIdentity
sslsessioncache = _Sslsessioncache_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 17, 7)
)
_SslSessionCacheHits_Type = Counter32
_SslSessionCacheHits_Object = MibScalar
sslSessionCacheHits = _SslSessionCacheHits_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 17, 7, 1),
    _SslSessionCacheHits_Type()
)
sslSessionCacheHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslSessionCacheHits.setStatus("current")
_SslSessionCacheMisses_Type = Counter32
_SslSessionCacheMisses_Object = MibScalar
sslSessionCacheMisses = _SslSessionCacheMisses_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 17, 7, 2),
    _SslSessionCacheMisses_Type()
)
sslSessionCacheMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslSessionCacheMisses.setStatus("current")
_SslSessionCacheLookups_Type = Counter32
_SslSessionCacheLookups_Object = MibScalar
sslSessionCacheLookups = _SslSessionCacheLookups_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 17, 7, 3),
    _SslSessionCacheLookups_Type()
)
sslSessionCacheLookups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslSessionCacheLookups.setStatus("current")
_SslSessionCacheHitRate_Type = Gauge32
_SslSessionCacheHitRate_Object = MibScalar
sslSessionCacheHitRate = _SslSessionCacheHitRate_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 17, 7, 4),
    _SslSessionCacheHitRate_Type()
)
sslSessionCacheHitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslSessionCacheHitRate.setStatus("current")
_SslSessionCacheEntries_Type = Gauge32
_SslSessionCacheEntries_Object = MibScalar
sslSessionCacheEntries = _SslSessionCacheEntries_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 17, 7, 5),
    _SslSessionCacheEntries_Type()
)
sslSessionCacheEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslSessionCacheEntries.setStatus("current")
_SslSessionCacheEntriesMax_Type = Gauge32
_SslSessionCacheEntriesMax_Object = MibScalar
sslSessionCacheEntriesMax = _SslSessionCacheEntriesMax_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 17, 7, 6),
    _SslSessionCacheEntriesMax_Type()
)
sslSessionCacheEntriesMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslSessionCacheEntriesMax.setStatus("current")
_SslSessionCacheOldest_Type = Gauge32
_SslSessionCacheOldest_Object = MibScalar
sslSessionCacheOldest = _SslSessionCacheOldest_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 17, 7, 7),
    _SslSessionCacheOldest_Type()
)
sslSessionCacheOldest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslSessionCacheOldest.setStatus("current")
_Rules_ObjectIdentity = ObjectIdentity
rules = _Rules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 18)
)
_RuleNumber_Type = Integer32
_RuleNumber_Object = MibScalar
ruleNumber = _RuleNumber_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 18, 1),
    _RuleNumber_Type()
)
ruleNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruleNumber.setStatus("current")
_RuleTable_Object = MibTable
ruleTable = _RuleTable_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 18, 2)
)
if mibBuilder.loadTexts:
    ruleTable.setStatus("current")
_RuleEntry_Object = MibTableRow
ruleEntry = _RuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 18, 2, 1)
)
ruleEntry.setIndexNames(
    (0, "ZXTM-MIB-SMIv2", "ruleName"),
)
if mibBuilder.loadTexts:
    ruleEntry.setStatus("current")


class _RuleName_Type(DisplayString):
    """Custom type ruleName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RuleName_Type.__name__ = "DisplayString"
_RuleName_Object = MibTableColumn
ruleName = _RuleName_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 18, 2, 1, 1),
    _RuleName_Type()
)
ruleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruleName.setStatus("current")
_RuleExecutions_Type = Counter32
_RuleExecutions_Object = MibTableColumn
ruleExecutions = _RuleExecutions_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 18, 2, 1, 2),
    _RuleExecutions_Type()
)
ruleExecutions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruleExecutions.setStatus("current")
_RuleAborts_Type = Counter32
_RuleAborts_Object = MibTableColumn
ruleAborts = _RuleAborts_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 18, 2, 1, 3),
    _RuleAborts_Type()
)
ruleAborts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruleAborts.setStatus("current")
_RuleResponds_Type = Counter32
_RuleResponds_Object = MibTableColumn
ruleResponds = _RuleResponds_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 18, 2, 1, 4),
    _RuleResponds_Type()
)
ruleResponds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruleResponds.setStatus("current")
_RulePoolSelect_Type = Counter32
_RulePoolSelect_Object = MibTableColumn
rulePoolSelect = _RulePoolSelect_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 18, 2, 1, 5),
    _RulePoolSelect_Type()
)
rulePoolSelect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rulePoolSelect.setStatus("current")
_RuleRetries_Type = Counter32
_RuleRetries_Object = MibTableColumn
ruleRetries = _RuleRetries_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 18, 2, 1, 6),
    _RuleRetries_Type()
)
ruleRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruleRetries.setStatus("current")
_RuleDiscards_Type = Counter32
_RuleDiscards_Object = MibTableColumn
ruleDiscards = _RuleDiscards_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 18, 2, 1, 7),
    _RuleDiscards_Type()
)
ruleDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruleDiscards.setStatus("current")
_RuleExecutionTimeWarnings_Type = Counter32
_RuleExecutionTimeWarnings_Object = MibTableColumn
ruleExecutionTimeWarnings = _RuleExecutionTimeWarnings_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 18, 2, 1, 8),
    _RuleExecutionTimeWarnings_Type()
)
ruleExecutionTimeWarnings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruleExecutionTimeWarnings.setStatus("current")
_Monitors_ObjectIdentity = ObjectIdentity
monitors = _Monitors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 19)
)
_MonitorNumber_Type = Integer32
_MonitorNumber_Object = MibScalar
monitorNumber = _MonitorNumber_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 19, 1),
    _MonitorNumber_Type()
)
monitorNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorNumber.setStatus("current")
_MonitorTable_Object = MibTable
monitorTable = _MonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 19, 2)
)
if mibBuilder.loadTexts:
    monitorTable.setStatus("current")
_MonitorEntry_Object = MibTableRow
monitorEntry = _MonitorEntry_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 19, 2, 1)
)
monitorEntry.setIndexNames(
    (0, "ZXTM-MIB-SMIv2", "monitorName"),
)
if mibBuilder.loadTexts:
    monitorEntry.setStatus("current")


class _MonitorName_Type(DisplayString):
    """Custom type monitorName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MonitorName_Type.__name__ = "DisplayString"
_MonitorName_Object = MibTableColumn
monitorName = _MonitorName_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 19, 2, 1, 1),
    _MonitorName_Type()
)
monitorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorName.setStatus("current")
_Licensekeys_ObjectIdentity = ObjectIdentity
licensekeys = _Licensekeys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 20)
)
_LicensekeyNumber_Type = Integer32
_LicensekeyNumber_Object = MibScalar
licensekeyNumber = _LicensekeyNumber_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 20, 1),
    _LicensekeyNumber_Type()
)
licensekeyNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licensekeyNumber.setStatus("current")
_LicensekeyTable_Object = MibTable
licensekeyTable = _LicensekeyTable_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 20, 2)
)
if mibBuilder.loadTexts:
    licensekeyTable.setStatus("current")
_LicensekeyEntry_Object = MibTableRow
licensekeyEntry = _LicensekeyEntry_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 20, 2, 1)
)
licensekeyEntry.setIndexNames(
    (0, "ZXTM-MIB-SMIv2", "licensekeyName"),
)
if mibBuilder.loadTexts:
    licensekeyEntry.setStatus("current")


class _LicensekeyName_Type(DisplayString):
    """Custom type licensekeyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LicensekeyName_Type.__name__ = "DisplayString"
_LicensekeyName_Object = MibTableColumn
licensekeyName = _LicensekeyName_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 20, 2, 1, 1),
    _LicensekeyName_Type()
)
licensekeyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licensekeyName.setStatus("current")
_Zxtms_ObjectIdentity = ObjectIdentity
zxtms = _Zxtms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 21)
)
_ZxtmNumber_Type = Integer32
_ZxtmNumber_Object = MibScalar
zxtmNumber = _ZxtmNumber_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 21, 1),
    _ZxtmNumber_Type()
)
zxtmNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxtmNumber.setStatus("current")
_ZxtmTable_Object = MibTable
zxtmTable = _ZxtmTable_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 21, 2)
)
if mibBuilder.loadTexts:
    zxtmTable.setStatus("current")
_ZxtmEntry_Object = MibTableRow
zxtmEntry = _ZxtmEntry_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 21, 2, 1)
)
zxtmEntry.setIndexNames(
    (0, "ZXTM-MIB-SMIv2", "zxtmName"),
)
if mibBuilder.loadTexts:
    zxtmEntry.setStatus("current")


class _ZxtmName_Type(DisplayString):
    """Custom type zxtmName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ZxtmName_Type.__name__ = "DisplayString"
_ZxtmName_Object = MibTableColumn
zxtmName = _ZxtmName_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 21, 2, 1, 1),
    _ZxtmName_Type()
)
zxtmName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxtmName.setStatus("current")
_Trapobjects_ObjectIdentity = ObjectIdentity
trapobjects = _Trapobjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 22)
)


class _FullLogLine_Type(DisplayString):
    """Custom type fullLogLine based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FullLogLine_Type.__name__ = "DisplayString"
_FullLogLine_Object = MibScalar
fullLogLine = _FullLogLine_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 22, 1),
    _FullLogLine_Type()
)
fullLogLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fullLogLine.setStatus("current")


class _ConfName_Type(DisplayString):
    """Custom type confName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ConfName_Type.__name__ = "DisplayString"
_ConfName_Object = MibScalar
confName = _ConfName_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 22, 2),
    _ConfName_Type()
)
confName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    confName.setStatus("current")


class _CustomEventName_Type(DisplayString):
    """Custom type customEventName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CustomEventName_Type.__name__ = "DisplayString"
_CustomEventName_Object = MibScalar
customEventName = _CustomEventName_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 22, 3),
    _CustomEventName_Type()
)
customEventName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    customEventName.setStatus("current")


class _DomainName_Type(DisplayString):
    """Custom type domainName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DomainName_Type.__name__ = "DisplayString"
_DomainName_Object = MibScalar
domainName = _DomainName_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 22, 4),
    _DomainName_Type()
)
domainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    domainName.setStatus("current")
_Cloudcredentials_ObjectIdentity = ObjectIdentity
cloudcredentials = _Cloudcredentials_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 23)
)
_CloudcredentialsClassNumber_Type = Integer32
_CloudcredentialsClassNumber_Object = MibScalar
cloudcredentialsClassNumber = _CloudcredentialsClassNumber_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 23, 1),
    _CloudcredentialsClassNumber_Type()
)
cloudcredentialsClassNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cloudcredentialsClassNumber.setStatus("current")
_CloudcredentialsTable_Object = MibTable
cloudcredentialsTable = _CloudcredentialsTable_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 23, 2)
)
if mibBuilder.loadTexts:
    cloudcredentialsTable.setStatus("current")
_CloudcredentialsEntry_Object = MibTableRow
cloudcredentialsEntry = _CloudcredentialsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 23, 2, 1)
)
cloudcredentialsEntry.setIndexNames(
    (0, "ZXTM-MIB-SMIv2", "cloudcredentialsName"),
)
if mibBuilder.loadTexts:
    cloudcredentialsEntry.setStatus("current")


class _CloudcredentialsName_Type(DisplayString):
    """Custom type cloudcredentialsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CloudcredentialsName_Type.__name__ = "DisplayString"
_CloudcredentialsName_Object = MibTableColumn
cloudcredentialsName = _CloudcredentialsName_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 23, 2, 1, 1),
    _CloudcredentialsName_Type()
)
cloudcredentialsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cloudcredentialsName.setStatus("current")
_CloudcredentialsStatusRequests_Type = Counter32
_CloudcredentialsStatusRequests_Object = MibTableColumn
cloudcredentialsStatusRequests = _CloudcredentialsStatusRequests_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 23, 2, 1, 2),
    _CloudcredentialsStatusRequests_Type()
)
cloudcredentialsStatusRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cloudcredentialsStatusRequests.setStatus("current")
_CloudcredentialsNodeCreations_Type = Counter32
_CloudcredentialsNodeCreations_Object = MibTableColumn
cloudcredentialsNodeCreations = _CloudcredentialsNodeCreations_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 23, 2, 1, 3),
    _CloudcredentialsNodeCreations_Type()
)
cloudcredentialsNodeCreations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cloudcredentialsNodeCreations.setStatus("current")
_CloudcredentialsNodeDeletions_Type = Counter32
_CloudcredentialsNodeDeletions_Object = MibTableColumn
cloudcredentialsNodeDeletions = _CloudcredentialsNodeDeletions_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 23, 2, 1, 4),
    _CloudcredentialsNodeDeletions_Type()
)
cloudcredentialsNodeDeletions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cloudcredentialsNodeDeletions.setStatus("current")
_Glbservices_ObjectIdentity = ObjectIdentity
glbservices = _Glbservices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 24)
)


class _GlbServiceNumber_Type(Integer32):
    """Custom type glbServiceNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_GlbServiceNumber_Type.__name__ = "Integer32"
_GlbServiceNumber_Object = MibScalar
glbServiceNumber = _GlbServiceNumber_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 24, 1),
    _GlbServiceNumber_Type()
)
glbServiceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    glbServiceNumber.setStatus("current")
_GlbServiceTable_Object = MibTable
glbServiceTable = _GlbServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 24, 2)
)
if mibBuilder.loadTexts:
    glbServiceTable.setStatus("current")
_GlbServiceEntry_Object = MibTableRow
glbServiceEntry = _GlbServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 24, 2, 1)
)
glbServiceEntry.setIndexNames(
    (0, "ZXTM-MIB-SMIv2", "glbServiceName"),
)
if mibBuilder.loadTexts:
    glbServiceEntry.setStatus("current")


class _GlbServiceName_Type(DisplayString):
    """Custom type glbServiceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_GlbServiceName_Type.__name__ = "DisplayString"
_GlbServiceName_Object = MibTableColumn
glbServiceName = _GlbServiceName_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 24, 2, 1, 1),
    _GlbServiceName_Type()
)
glbServiceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    glbServiceName.setStatus("current")
_GlbServiceResponses_Type = Counter32
_GlbServiceResponses_Object = MibTableColumn
glbServiceResponses = _GlbServiceResponses_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 24, 2, 1, 2),
    _GlbServiceResponses_Type()
)
glbServiceResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    glbServiceResponses.setStatus("current")
_GlbServiceUnmodified_Type = Counter32
_GlbServiceUnmodified_Object = MibTableColumn
glbServiceUnmodified = _GlbServiceUnmodified_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 24, 2, 1, 3),
    _GlbServiceUnmodified_Type()
)
glbServiceUnmodified.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    glbServiceUnmodified.setStatus("current")
_GlbServiceDiscarded_Type = Counter32
_GlbServiceDiscarded_Object = MibTableColumn
glbServiceDiscarded = _GlbServiceDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 24, 2, 1, 4),
    _GlbServiceDiscarded_Type()
)
glbServiceDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    glbServiceDiscarded.setStatus("current")
_Perlocationservices_ObjectIdentity = ObjectIdentity
perlocationservices = _Perlocationservices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 25)
)
_PerLocationServiceTable_Object = MibTable
perLocationServiceTable = _PerLocationServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 25, 1)
)
if mibBuilder.loadTexts:
    perLocationServiceTable.setStatus("current")
_PerLocationServiceEntry_Object = MibTableRow
perLocationServiceEntry = _PerLocationServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 25, 1, 1)
)
perLocationServiceEntry.setIndexNames(
    (0, "ZXTM-MIB-SMIv2", "perLocationServiceLocationName"),
    (0, "ZXTM-MIB-SMIv2", "perLocationServiceName"),
)
if mibBuilder.loadTexts:
    perLocationServiceEntry.setStatus("current")


class _PerLocationServiceLocationName_Type(DisplayString):
    """Custom type perLocationServiceLocationName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PerLocationServiceLocationName_Type.__name__ = "DisplayString"
_PerLocationServiceLocationName_Object = MibTableColumn
perLocationServiceLocationName = _PerLocationServiceLocationName_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 25, 1, 1, 1),
    _PerLocationServiceLocationName_Type()
)
perLocationServiceLocationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perLocationServiceLocationName.setStatus("current")


class _PerLocationServiceLocationCode_Type(DisplayString):
    """Custom type perLocationServiceLocationCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PerLocationServiceLocationCode_Type.__name__ = "DisplayString"
_PerLocationServiceLocationCode_Object = MibTableColumn
perLocationServiceLocationCode = _PerLocationServiceLocationCode_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 25, 1, 1, 2),
    _PerLocationServiceLocationCode_Type()
)
perLocationServiceLocationCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perLocationServiceLocationCode.setStatus("current")


class _PerLocationServiceName_Type(DisplayString):
    """Custom type perLocationServiceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PerLocationServiceName_Type.__name__ = "DisplayString"
_PerLocationServiceName_Object = MibTableColumn
perLocationServiceName = _PerLocationServiceName_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 25, 1, 1, 3),
    _PerLocationServiceName_Type()
)
perLocationServiceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perLocationServiceName.setStatus("current")


class _PerLocationServiceDraining_Type(Integer32):
    """Custom type perLocationServiceDraining based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("draining", 1))
    )


_PerLocationServiceDraining_Type.__name__ = "Integer32"
_PerLocationServiceDraining_Object = MibTableColumn
perLocationServiceDraining = _PerLocationServiceDraining_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 25, 1, 1, 4),
    _PerLocationServiceDraining_Type()
)
perLocationServiceDraining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perLocationServiceDraining.setStatus("current")


class _PerLocationServiceState_Type(Integer32):
    """Custom type perLocationServiceState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alive", 1),
          ("dead", 2))
    )


_PerLocationServiceState_Type.__name__ = "Integer32"
_PerLocationServiceState_Object = MibTableColumn
perLocationServiceState = _PerLocationServiceState_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 25, 1, 1, 5),
    _PerLocationServiceState_Type()
)
perLocationServiceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perLocationServiceState.setStatus("current")


class _PerLocationServiceFrontendState_Type(Integer32):
    """Custom type perLocationServiceFrontendState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alive", 1),
          ("dead", 2))
    )


_PerLocationServiceFrontendState_Type.__name__ = "Integer32"
_PerLocationServiceFrontendState_Object = MibTableColumn
perLocationServiceFrontendState = _PerLocationServiceFrontendState_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 25, 1, 1, 6),
    _PerLocationServiceFrontendState_Type()
)
perLocationServiceFrontendState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perLocationServiceFrontendState.setStatus("current")


class _PerLocationServiceMonitorState_Type(Integer32):
    """Custom type perLocationServiceMonitorState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alive", 1),
          ("dead", 2))
    )


_PerLocationServiceMonitorState_Type.__name__ = "Integer32"
_PerLocationServiceMonitorState_Object = MibTableColumn
perLocationServiceMonitorState = _PerLocationServiceMonitorState_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 25, 1, 1, 7),
    _PerLocationServiceMonitorState_Type()
)
perLocationServiceMonitorState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perLocationServiceMonitorState.setStatus("current")
_PerLocationServiceLoad_Type = Gauge32
_PerLocationServiceLoad_Object = MibTableColumn
perLocationServiceLoad = _PerLocationServiceLoad_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 25, 1, 1, 8),
    _PerLocationServiceLoad_Type()
)
perLocationServiceLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perLocationServiceLoad.setStatus("current")
_PerLocationServiceResponses_Type = Counter32
_PerLocationServiceResponses_Object = MibTableColumn
perLocationServiceResponses = _PerLocationServiceResponses_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 25, 1, 1, 9),
    _PerLocationServiceResponses_Type()
)
perLocationServiceResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perLocationServiceResponses.setStatus("current")
_Locations_ObjectIdentity = ObjectIdentity
locations = _Locations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 26)
)
_LocationTable_Object = MibTable
locationTable = _LocationTable_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 26, 1)
)
if mibBuilder.loadTexts:
    locationTable.setStatus("current")
_LocationEntry_Object = MibTableRow
locationEntry = _LocationEntry_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 26, 1, 1)
)
locationEntry.setIndexNames(
    (0, "ZXTM-MIB-SMIv2", "locationName"),
)
if mibBuilder.loadTexts:
    locationEntry.setStatus("current")


class _LocationName_Type(DisplayString):
    """Custom type locationName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LocationName_Type.__name__ = "DisplayString"
_LocationName_Object = MibTableColumn
locationName = _LocationName_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 26, 1, 1, 1),
    _LocationName_Type()
)
locationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locationName.setStatus("current")


class _LocationCode_Type(DisplayString):
    """Custom type locationCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LocationCode_Type.__name__ = "DisplayString"
_LocationCode_Object = MibTableColumn
locationCode = _LocationCode_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 26, 1, 1, 2),
    _LocationCode_Type()
)
locationCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locationCode.setStatus("current")
_LocationLoad_Type = Gauge32
_LocationLoad_Object = MibTableColumn
locationLoad = _LocationLoad_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 26, 1, 1, 3),
    _LocationLoad_Type()
)
locationLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locationLoad.setStatus("current")
_LocationResponses_Type = Counter32
_LocationResponses_Object = MibTableColumn
locationResponses = _LocationResponses_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 26, 1, 1, 4),
    _LocationResponses_Type()
)
locationResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locationResponses.setStatus("current")
_Listenips_ObjectIdentity = ObjectIdentity
listenips = _Listenips_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 27)
)
_ListenIPTable_Object = MibTable
listenIPTable = _ListenIPTable_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 27, 2)
)
if mibBuilder.loadTexts:
    listenIPTable.setStatus("current")
_ListenIPEntry_Object = MibTableRow
listenIPEntry = _ListenIPEntry_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 27, 2, 1)
)
listenIPEntry.setIndexNames(
    (0, "ZXTM-MIB-SMIv2", "listenIPAddressType"),
    (0, "ZXTM-MIB-SMIv2", "listenIPAddress"),
)
if mibBuilder.loadTexts:
    listenIPEntry.setStatus("current")
_ListenIPAddressType_Type = InetAddressType
_ListenIPAddressType_Object = MibTableColumn
listenIPAddressType = _ListenIPAddressType_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 27, 2, 1, 1),
    _ListenIPAddressType_Type()
)
listenIPAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    listenIPAddressType.setStatus("current")


class _ListenIPAddress_Type(InetAddress):
    """Custom type listenIPAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ListenIPAddress_Type.__name__ = "InetAddress"
_ListenIPAddress_Object = MibTableColumn
listenIPAddress = _ListenIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 27, 2, 1, 2),
    _ListenIPAddress_Type()
)
listenIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    listenIPAddress.setStatus("current")
_ListenIPBytesInLo_Type = Counter32
_ListenIPBytesInLo_Object = MibTableColumn
listenIPBytesInLo = _ListenIPBytesInLo_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 27, 2, 1, 3),
    _ListenIPBytesInLo_Type()
)
listenIPBytesInLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    listenIPBytesInLo.setStatus("obsolete")
_ListenIPBytesInHi_Type = Counter32
_ListenIPBytesInHi_Object = MibTableColumn
listenIPBytesInHi = _ListenIPBytesInHi_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 27, 2, 1, 4),
    _ListenIPBytesInHi_Type()
)
listenIPBytesInHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    listenIPBytesInHi.setStatus("obsolete")
_ListenIPBytesOutLo_Type = Counter32
_ListenIPBytesOutLo_Object = MibTableColumn
listenIPBytesOutLo = _ListenIPBytesOutLo_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 27, 2, 1, 5),
    _ListenIPBytesOutLo_Type()
)
listenIPBytesOutLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    listenIPBytesOutLo.setStatus("obsolete")
_ListenIPBytesOutHi_Type = Counter32
_ListenIPBytesOutHi_Object = MibTableColumn
listenIPBytesOutHi = _ListenIPBytesOutHi_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 27, 2, 1, 6),
    _ListenIPBytesOutHi_Type()
)
listenIPBytesOutHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    listenIPBytesOutHi.setStatus("obsolete")
_ListenIPCurrentConn_Type = Gauge32
_ListenIPCurrentConn_Object = MibTableColumn
listenIPCurrentConn = _ListenIPCurrentConn_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 27, 2, 1, 7),
    _ListenIPCurrentConn_Type()
)
listenIPCurrentConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    listenIPCurrentConn.setStatus("current")
_ListenIPTotalConn_Type = Counter32
_ListenIPTotalConn_Object = MibTableColumn
listenIPTotalConn = _ListenIPTotalConn_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 27, 2, 1, 8),
    _ListenIPTotalConn_Type()
)
listenIPTotalConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    listenIPTotalConn.setStatus("obsolete")
_ListenIPMaxConn_Type = Gauge32
_ListenIPMaxConn_Object = MibTableColumn
listenIPMaxConn = _ListenIPMaxConn_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 27, 2, 1, 9),
    _ListenIPMaxConn_Type()
)
listenIPMaxConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    listenIPMaxConn.setStatus("current")
_ListenIPBytesIn_Type = Counter64
_ListenIPBytesIn_Object = MibTableColumn
listenIPBytesIn = _ListenIPBytesIn_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 27, 2, 1, 10),
    _ListenIPBytesIn_Type()
)
listenIPBytesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    listenIPBytesIn.setStatus("current")
_ListenIPBytesOut_Type = Counter64
_ListenIPBytesOut_Object = MibTableColumn
listenIPBytesOut = _ListenIPBytesOut_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 27, 2, 1, 11),
    _ListenIPBytesOut_Type()
)
listenIPBytesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    listenIPBytesOut.setStatus("current")
_ListenIPTotalRequestsLo_Type = Counter32
_ListenIPTotalRequestsLo_Object = MibTableColumn
listenIPTotalRequestsLo = _ListenIPTotalRequestsLo_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 27, 2, 1, 12),
    _ListenIPTotalRequestsLo_Type()
)
listenIPTotalRequestsLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    listenIPTotalRequestsLo.setStatus("obsolete")
_ListenIPTotalRequestsHi_Type = Counter32
_ListenIPTotalRequestsHi_Object = MibTableColumn
listenIPTotalRequestsHi = _ListenIPTotalRequestsHi_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 27, 2, 1, 13),
    _ListenIPTotalRequestsHi_Type()
)
listenIPTotalRequestsHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    listenIPTotalRequestsHi.setStatus("obsolete")
_ListenIPTotalRequests_Type = Counter64
_ListenIPTotalRequests_Object = MibTableColumn
listenIPTotalRequests = _ListenIPTotalRequests_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 27, 2, 1, 14),
    _ListenIPTotalRequests_Type()
)
listenIPTotalRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    listenIPTotalRequests.setStatus("current")
_Authenticators_ObjectIdentity = ObjectIdentity
authenticators = _Authenticators_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 28)
)
_AuthenticatorNumber_Type = Integer32
_AuthenticatorNumber_Object = MibScalar
authenticatorNumber = _AuthenticatorNumber_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 28, 1),
    _AuthenticatorNumber_Type()
)
authenticatorNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authenticatorNumber.setStatus("current")
_AuthenticatorTable_Object = MibTable
authenticatorTable = _AuthenticatorTable_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 28, 2)
)
if mibBuilder.loadTexts:
    authenticatorTable.setStatus("current")
_AuthenticatorEntry_Object = MibTableRow
authenticatorEntry = _AuthenticatorEntry_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 28, 2, 1)
)
authenticatorEntry.setIndexNames(
    (0, "ZXTM-MIB-SMIv2", "authenticatorName"),
)
if mibBuilder.loadTexts:
    authenticatorEntry.setStatus("current")


class _AuthenticatorName_Type(DisplayString):
    """Custom type authenticatorName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AuthenticatorName_Type.__name__ = "DisplayString"
_AuthenticatorName_Object = MibTableColumn
authenticatorName = _AuthenticatorName_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 28, 2, 1, 1),
    _AuthenticatorName_Type()
)
authenticatorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authenticatorName.setStatus("current")
_AuthenticatorRequests_Type = Counter32
_AuthenticatorRequests_Object = MibTableColumn
authenticatorRequests = _AuthenticatorRequests_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 28, 2, 1, 2),
    _AuthenticatorRequests_Type()
)
authenticatorRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authenticatorRequests.setStatus("current")
_AuthenticatorPasses_Type = Counter32
_AuthenticatorPasses_Object = MibTableColumn
authenticatorPasses = _AuthenticatorPasses_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 28, 2, 1, 3),
    _AuthenticatorPasses_Type()
)
authenticatorPasses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authenticatorPasses.setStatus("current")
_AuthenticatorFails_Type = Counter32
_AuthenticatorFails_Object = MibTableColumn
authenticatorFails = _AuthenticatorFails_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 28, 2, 1, 4),
    _AuthenticatorFails_Type()
)
authenticatorFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authenticatorFails.setStatus("current")
_AuthenticatorErrors_Type = Counter32
_AuthenticatorErrors_Object = MibTableColumn
authenticatorErrors = _AuthenticatorErrors_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 28, 2, 1, 5),
    _AuthenticatorErrors_Type()
)
authenticatorErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authenticatorErrors.setStatus("current")
_ConformanceGroups_ObjectIdentity = ObjectIdentity
conformanceGroups = _ConformanceGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 29)
)
_ComplianceStatements_ObjectIdentity = ObjectIdentity
complianceStatements = _ComplianceStatements_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 30)
)
_Steelheads_ObjectIdentity = ObjectIdentity
steelheads = _Steelheads_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 31)
)
_SteelheadNumber_Type = Integer32
_SteelheadNumber_Object = MibScalar
steelheadNumber = _SteelheadNumber_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 31, 1),
    _SteelheadNumber_Type()
)
steelheadNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    steelheadNumber.setStatus("current")
_SteelheadTable_Object = MibTable
steelheadTable = _SteelheadTable_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 31, 2)
)
if mibBuilder.loadTexts:
    steelheadTable.setStatus("current")
_SteelheadEntry_Object = MibTableRow
steelheadEntry = _SteelheadEntry_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 31, 2, 1)
)
steelheadEntry.setIndexNames(
    (0, "ZXTM-MIB-SMIv2", "steelheadName"),
)
if mibBuilder.loadTexts:
    steelheadEntry.setStatus("current")


class _SteelheadName_Type(DisplayString):
    """Custom type steelheadName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SteelheadName_Type.__name__ = "DisplayString"
_SteelheadName_Object = MibTableColumn
steelheadName = _SteelheadName_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 31, 2, 1, 1),
    _SteelheadName_Type()
)
steelheadName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    steelheadName.setStatus("current")
_SteelheadOptimized_Type = Gauge32
_SteelheadOptimized_Object = MibTableColumn
steelheadOptimized = _SteelheadOptimized_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 31, 2, 1, 2),
    _SteelheadOptimized_Type()
)
steelheadOptimized.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    steelheadOptimized.setStatus("current")
_Sslocspstapling_ObjectIdentity = ObjectIdentity
sslocspstapling = _Sslocspstapling_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 32)
)
_SslOcspStaplingCacheCount_Type = Gauge32
_SslOcspStaplingCacheCount_Object = MibScalar
sslOcspStaplingCacheCount = _SslOcspStaplingCacheCount_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 32, 1),
    _SslOcspStaplingCacheCount_Type()
)
sslOcspStaplingCacheCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslOcspStaplingCacheCount.setStatus("current")
_SslOcspStaplingCount_Type = Counter32
_SslOcspStaplingCount_Object = MibScalar
sslOcspStaplingCount = _SslOcspStaplingCount_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 32, 2),
    _SslOcspStaplingCount_Type()
)
sslOcspStaplingCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslOcspStaplingCount.setStatus("current")
_SslOcspStaplingSuccessCount_Type = Counter32
_SslOcspStaplingSuccessCount_Object = MibScalar
sslOcspStaplingSuccessCount = _SslOcspStaplingSuccessCount_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 32, 3),
    _SslOcspStaplingSuccessCount_Type()
)
sslOcspStaplingSuccessCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslOcspStaplingSuccessCount.setStatus("current")
_SslOcspStaplingFailureCount_Type = Counter32
_SslOcspStaplingFailureCount_Object = MibScalar
sslOcspStaplingFailureCount = _SslOcspStaplingFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 32, 4),
    _SslOcspStaplingFailureCount_Type()
)
sslOcspStaplingFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslOcspStaplingFailureCount.setStatus("current")
_SslOcspStaplingGoodCount_Type = Counter32
_SslOcspStaplingGoodCount_Object = MibScalar
sslOcspStaplingGoodCount = _SslOcspStaplingGoodCount_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 32, 5),
    _SslOcspStaplingGoodCount_Type()
)
sslOcspStaplingGoodCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslOcspStaplingGoodCount.setStatus("current")
_SslOcspStaplingRevokedCount_Type = Counter32
_SslOcspStaplingRevokedCount_Object = MibScalar
sslOcspStaplingRevokedCount = _SslOcspStaplingRevokedCount_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 32, 6),
    _SslOcspStaplingRevokedCount_Type()
)
sslOcspStaplingRevokedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslOcspStaplingRevokedCount.setStatus("current")
_SslOcspStaplingUnknownCount_Type = Counter32
_SslOcspStaplingUnknownCount_Object = MibScalar
sslOcspStaplingUnknownCount = _SslOcspStaplingUnknownCount_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 32, 7),
    _SslOcspStaplingUnknownCount_Type()
)
sslOcspStaplingUnknownCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslOcspStaplingUnknownCount.setStatus("current")
_DpaCoreUtilization_ObjectIdentity = ObjectIdentity
dpaCoreUtilization = _DpaCoreUtilization_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 33)
)
_DataPlaneAccelCoreNumber_Type = Integer32
_DataPlaneAccelCoreNumber_Object = MibScalar
dataPlaneAccelCoreNumber = _DataPlaneAccelCoreNumber_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 33, 1),
    _DataPlaneAccelCoreNumber_Type()
)
dataPlaneAccelCoreNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataPlaneAccelCoreNumber.setStatus("current")
_DpaCoreUtilizationTable_Object = MibTable
dpaCoreUtilizationTable = _DpaCoreUtilizationTable_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 33, 2)
)
if mibBuilder.loadTexts:
    dpaCoreUtilizationTable.setStatus("current")
_DpaCoreUtilizationEntry_Object = MibTableRow
dpaCoreUtilizationEntry = _DpaCoreUtilizationEntry_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 33, 2, 1)
)
dpaCoreUtilizationEntry.setIndexNames(
    (0, "ZXTM-MIB-SMIv2", "coreId"),
)
if mibBuilder.loadTexts:
    dpaCoreUtilizationEntry.setStatus("current")


class _CoreId_Type(DisplayString):
    """Custom type coreId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CoreId_Type.__name__ = "DisplayString"
_CoreId_Object = MibTableColumn
coreId = _CoreId_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 33, 2, 1, 1),
    _CoreId_Type()
)
coreId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coreId.setStatus("current")
_CoreUtilizationPercent_Type = Gauge32
_CoreUtilizationPercent_Object = MibTableColumn
coreUtilizationPercent = _CoreUtilizationPercent_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 33, 2, 1, 2),
    _CoreUtilizationPercent_Type()
)
coreUtilizationPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coreUtilizationPercent.setStatus("current")

# Managed Objects groups

mainGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 29, 1)
)
mainGroup.setObjects(
      *(("ZXTM-MIB-SMIv2", "version"),
        ("ZXTM-MIB-SMIv2", "numberChildProcesses"),
        ("ZXTM-MIB-SMIv2", "upTime"),
        ("ZXTM-MIB-SMIv2", "timeLastConfigUpdate"),
        ("ZXTM-MIB-SMIv2", "totalBytesIn"),
        ("ZXTM-MIB-SMIv2", "totalBytesOut"),
        ("ZXTM-MIB-SMIv2", "totalCurrentConn"),
        ("ZXTM-MIB-SMIv2", "totalConn"),
        ("ZXTM-MIB-SMIv2", "totalRequests"),
        ("ZXTM-MIB-SMIv2", "totalTransactions"),
        ("ZXTM-MIB-SMIv2", "numberDNSARequests"),
        ("ZXTM-MIB-SMIv2", "numberDNSACacheHits"),
        ("ZXTM-MIB-SMIv2", "numberDNSPTRRequests"),
        ("ZXTM-MIB-SMIv2", "numberDNSPTRCacheHits"),
        ("ZXTM-MIB-SMIv2", "numberSNMPUnauthorisedRequests"),
        ("ZXTM-MIB-SMIv2", "numberSNMPBadRequests"),
        ("ZXTM-MIB-SMIv2", "numberSNMPGetRequests"),
        ("ZXTM-MIB-SMIv2", "numberSNMPGetNextRequests"),
        ("ZXTM-MIB-SMIv2", "sslCipherEncrypts"),
        ("ZXTM-MIB-SMIv2", "sslCipherDecrypts"),
        ("ZXTM-MIB-SMIv2", "sslCipherRC4Encrypts"),
        ("ZXTM-MIB-SMIv2", "sslCipherRC4Decrypts"),
        ("ZXTM-MIB-SMIv2", "sslCipherDESEncrypts"),
        ("ZXTM-MIB-SMIv2", "sslCipherDESDecrypts"),
        ("ZXTM-MIB-SMIv2", "sslCipher3DESEncrypts"),
        ("ZXTM-MIB-SMIv2", "sslCipher3DESDecrypts"),
        ("ZXTM-MIB-SMIv2", "sslCipherAESEncrypts"),
        ("ZXTM-MIB-SMIv2", "sslCipherAESDecrypts"),
        ("ZXTM-MIB-SMIv2", "sslCipherRSAEncrypts"),
        ("ZXTM-MIB-SMIv2", "sslCipherRSADecrypts"),
        ("ZXTM-MIB-SMIv2", "sslCipherRSADecryptsExternal"),
        ("ZXTM-MIB-SMIv2", "sslHandshakeSSLv3"),
        ("ZXTM-MIB-SMIv2", "sslHandshakeTLSv1"),
        ("ZXTM-MIB-SMIv2", "sslClientCertNotSent"),
        ("ZXTM-MIB-SMIv2", "sslClientCertInvalid"),
        ("ZXTM-MIB-SMIv2", "sslClientCertExpired"),
        ("ZXTM-MIB-SMIv2", "sslClientCertRevoked"),
        ("ZXTM-MIB-SMIv2", "sslSessionIDMemCacheHit"),
        ("ZXTM-MIB-SMIv2", "sslSessionIDMemCacheMiss"),
        ("ZXTM-MIB-SMIv2", "sslHandshakeTLSv11"),
        ("ZXTM-MIB-SMIv2", "sslConnections"),
        ("ZXTM-MIB-SMIv2", "sslCipherRSAEncryptsExternal"),
        ("ZXTM-MIB-SMIv2", "sysCPUIdlePercent"),
        ("ZXTM-MIB-SMIv2", "sysCPUBusyPercent"),
        ("ZXTM-MIB-SMIv2", "sysCPUUserBusyPercent"),
        ("ZXTM-MIB-SMIv2", "sysCPUSystemBusyPercent"),
        ("ZXTM-MIB-SMIv2", "sysFDsFree"),
        ("ZXTM-MIB-SMIv2", "sysMemTotal"),
        ("ZXTM-MIB-SMIv2", "sysMemFree"),
        ("ZXTM-MIB-SMIv2", "sysMemInUse"),
        ("ZXTM-MIB-SMIv2", "sysMemBuffered"),
        ("ZXTM-MIB-SMIv2", "sysMemSwapped"),
        ("ZXTM-MIB-SMIv2", "sysMemSwapTotal"),
        ("ZXTM-MIB-SMIv2", "numIdleConnections"),
        ("ZXTM-MIB-SMIv2", "dataEntries"),
        ("ZXTM-MIB-SMIv2", "dataMemoryUsage"),
        ("ZXTM-MIB-SMIv2", "eventsSeen"),
        ("ZXTM-MIB-SMIv2", "totalDNSResponses"),
        ("ZXTM-MIB-SMIv2", "totalBadDNSPackets"),
        ("ZXTM-MIB-SMIv2", "totalBackendServerErrors"),
        ("ZXTM-MIB-SMIv2", "virtualserverNumber"),
        ("ZXTM-MIB-SMIv2", "virtualserverName"),
        ("ZXTM-MIB-SMIv2", "virtualserverPort"),
        ("ZXTM-MIB-SMIv2", "virtualserverProtocol"),
        ("ZXTM-MIB-SMIv2", "virtualserverDefaultTrafficPool"),
        ("ZXTM-MIB-SMIv2", "virtualserverBytesIn"),
        ("ZXTM-MIB-SMIv2", "virtualserverBytesOut"),
        ("ZXTM-MIB-SMIv2", "virtualserverCurrentConn"),
        ("ZXTM-MIB-SMIv2", "virtualserverMaxConn"),
        ("ZXTM-MIB-SMIv2", "virtualserverDiscard"),
        ("ZXTM-MIB-SMIv2", "virtualserverDirectReplies"),
        ("ZXTM-MIB-SMIv2", "virtualserverConnectTimedOut"),
        ("ZXTM-MIB-SMIv2", "virtualserverDataTimedOut"),
        ("ZXTM-MIB-SMIv2", "virtualserverKeepaliveTimedOut"),
        ("ZXTM-MIB-SMIv2", "virtualserverMaxDurationTimedOut"),
        ("ZXTM-MIB-SMIv2", "virtualserverUdpTimedOut"),
        ("ZXTM-MIB-SMIv2", "virtualserverTotalDgram"),
        ("ZXTM-MIB-SMIv2", "virtualserverGzip"),
        ("ZXTM-MIB-SMIv2", "virtualserverGzipBytesSaved"),
        ("ZXTM-MIB-SMIv2", "virtualserverHttpRewriteLocation"),
        ("ZXTM-MIB-SMIv2", "virtualserverHttpRewriteCookie"),
        ("ZXTM-MIB-SMIv2", "virtualserverHttpCacheHits"),
        ("ZXTM-MIB-SMIv2", "virtualserverHttpCacheLookups"),
        ("ZXTM-MIB-SMIv2", "virtualserverHttpCacheHitRate"),
        ("ZXTM-MIB-SMIv2", "virtualserverSIPTotalCalls"),
        ("ZXTM-MIB-SMIv2", "virtualserverSIPRejectedRequests"),
        ("ZXTM-MIB-SMIv2", "virtualserverConnectionErrors"),
        ("ZXTM-MIB-SMIv2", "virtualserverConnectionFailures"),
        ("ZXTM-MIB-SMIv2", "virtualserverCertStatusRequests"),
        ("ZXTM-MIB-SMIv2", "virtualserverCertStatusResponses"),
        ("ZXTM-MIB-SMIv2", "virtualserverProcessingTimedOut"),
        ("ZXTM-MIB-SMIv2", "virtualserverTotalRequests"),
        ("ZXTM-MIB-SMIv2", "virtualserverTotalHTTPRequests"),
        ("ZXTM-MIB-SMIv2", "virtualserverTotalHTTP1Requests"),
        ("ZXTM-MIB-SMIv2", "virtualserverTotalHTTP2Requests"),
        ("ZXTM-MIB-SMIv2", "virtualserverPktsIn"),
        ("ZXTM-MIB-SMIv2", "virtualserverPktsOut"),
        ("ZXTM-MIB-SMIv2", "virtualserverL4TCPConnectResets"),
        ("ZXTM-MIB-SMIv2", "virtualserverL4UDPUnreachables"),
        ("ZXTM-MIB-SMIv2", "virtualserverBwLimitPktsDrop"),
        ("ZXTM-MIB-SMIv2", "virtualserverBwLimitBytesDrop"),
        ("ZXTM-MIB-SMIv2", "poolNumber"),
        ("ZXTM-MIB-SMIv2", "poolName"),
        ("ZXTM-MIB-SMIv2", "poolAlgorithm"),
        ("ZXTM-MIB-SMIv2", "poolNodes"),
        ("ZXTM-MIB-SMIv2", "poolDraining"),
        ("ZXTM-MIB-SMIv2", "poolFailPool"),
        ("ZXTM-MIB-SMIv2", "poolBytesIn"),
        ("ZXTM-MIB-SMIv2", "poolBytesOut"),
        ("ZXTM-MIB-SMIv2", "poolTotalConn"),
        ("ZXTM-MIB-SMIv2", "poolPersistence"),
        ("ZXTM-MIB-SMIv2", "poolSessionMigrated"),
        ("ZXTM-MIB-SMIv2", "poolDisabled"),
        ("ZXTM-MIB-SMIv2", "poolState"),
        ("ZXTM-MIB-SMIv2", "poolConnsQueued"),
        ("ZXTM-MIB-SMIv2", "poolQueueTimeouts"),
        ("ZXTM-MIB-SMIv2", "poolMinQueueTime"),
        ("ZXTM-MIB-SMIv2", "poolMaxQueueTime"),
        ("ZXTM-MIB-SMIv2", "poolMeanQueueTime"),
        ("ZXTM-MIB-SMIv2", "poolBwLimitPktsDrop"),
        ("ZXTM-MIB-SMIv2", "poolBwLimitBytesDrop"),
        ("ZXTM-MIB-SMIv2", "nodeNumberInet46"),
        ("ZXTM-MIB-SMIv2", "nodeInet46AddressType"),
        ("ZXTM-MIB-SMIv2", "nodeInet46Address"),
        ("ZXTM-MIB-SMIv2", "nodeInet46Port"),
        ("ZXTM-MIB-SMIv2", "nodeInet46HostName"),
        ("ZXTM-MIB-SMIv2", "nodeInet46State"),
        ("ZXTM-MIB-SMIv2", "nodeInet46BytesToNode"),
        ("ZXTM-MIB-SMIv2", "nodeInet46BytesFromNode"),
        ("ZXTM-MIB-SMIv2", "nodeInet46CurrentRequests"),
        ("ZXTM-MIB-SMIv2", "nodeInet46TotalConn"),
        ("ZXTM-MIB-SMIv2", "nodeInet46PooledConn"),
        ("ZXTM-MIB-SMIv2", "nodeInet46Failures"),
        ("ZXTM-MIB-SMIv2", "nodeInet46NewConn"),
        ("ZXTM-MIB-SMIv2", "nodeInet46Errors"),
        ("ZXTM-MIB-SMIv2", "nodeInet46ResponseMin"),
        ("ZXTM-MIB-SMIv2", "nodeInet46ResponseMax"),
        ("ZXTM-MIB-SMIv2", "nodeInet46ResponseMean"),
        ("ZXTM-MIB-SMIv2", "nodeInet46IdleConns"),
        ("ZXTM-MIB-SMIv2", "nodeInet46CurrentConn"),
        ("ZXTM-MIB-SMIv2", "perPoolNodeNumber"),
        ("ZXTM-MIB-SMIv2", "perPoolNodePoolName"),
        ("ZXTM-MIB-SMIv2", "perPoolNodeNodeAddressType"),
        ("ZXTM-MIB-SMIv2", "perPoolNodeNodeAddress"),
        ("ZXTM-MIB-SMIv2", "perPoolNodeNodePort"),
        ("ZXTM-MIB-SMIv2", "perPoolNodeNodeHostName"),
        ("ZXTM-MIB-SMIv2", "perPoolNodeState"),
        ("ZXTM-MIB-SMIv2", "perPoolNodeBytesToNode"),
        ("ZXTM-MIB-SMIv2", "perPoolNodeBytesFromNode"),
        ("ZXTM-MIB-SMIv2", "perPoolNodePktsToNode"),
        ("ZXTM-MIB-SMIv2", "perPoolNodePktsFromNode"),
        ("ZXTM-MIB-SMIv2", "perPoolNodeL4StatelessBuckets"),
        ("ZXTM-MIB-SMIv2", "perPoolNodeCurrentRequests"),
        ("ZXTM-MIB-SMIv2", "perPoolNodeTotalConn"),
        ("ZXTM-MIB-SMIv2", "perPoolNodePooledConn"),
        ("ZXTM-MIB-SMIv2", "perPoolNodeFailures"),
        ("ZXTM-MIB-SMIv2", "perPoolNodeNewConn"),
        ("ZXTM-MIB-SMIv2", "perPoolNodeErrors"),
        ("ZXTM-MIB-SMIv2", "perPoolNodeResponseMin"),
        ("ZXTM-MIB-SMIv2", "perPoolNodeResponseMax"),
        ("ZXTM-MIB-SMIv2", "perPoolNodeResponseMean"),
        ("ZXTM-MIB-SMIv2", "perPoolNodeIdleConns"),
        ("ZXTM-MIB-SMIv2", "perPoolNodeCurrentConn"),
        ("ZXTM-MIB-SMIv2", "trafficIPGatewayPingRequests"),
        ("ZXTM-MIB-SMIv2", "trafficIPGatewayPingResponses"),
        ("ZXTM-MIB-SMIv2", "trafficIPNodePingRequests"),
        ("ZXTM-MIB-SMIv2", "trafficIPNodePingResponses"),
        ("ZXTM-MIB-SMIv2", "trafficIPPingResponseErrors"),
        ("ZXTM-MIB-SMIv2", "trafficIPARPMessage"),
        ("ZXTM-MIB-SMIv2", "trafficIPNumberInet46"),
        ("ZXTM-MIB-SMIv2", "trafficIPNumberRaisedInet46"),
        ("ZXTM-MIB-SMIv2", "trafficIPInet46AddressType"),
        ("ZXTM-MIB-SMIv2", "trafficIPInet46Address"),
        ("ZXTM-MIB-SMIv2", "trafficIPInet46State"),
        ("ZXTM-MIB-SMIv2", "trafficIPInet46Time"),
        ("ZXTM-MIB-SMIv2", "serviceProtNumber"),
        ("ZXTM-MIB-SMIv2", "serviceProtName"),
        ("ZXTM-MIB-SMIv2", "serviceProtTotalRefusal"),
        ("ZXTM-MIB-SMIv2", "serviceProtLastRefusalTime"),
        ("ZXTM-MIB-SMIv2", "serviceProtRefusalIP"),
        ("ZXTM-MIB-SMIv2", "serviceProtRefusalConc1IP"),
        ("ZXTM-MIB-SMIv2", "serviceProtRefusalConc10IP"),
        ("ZXTM-MIB-SMIv2", "serviceProtRefusalConnRate"),
        ("ZXTM-MIB-SMIv2", "serviceProtRefusalRFC2396"),
        ("ZXTM-MIB-SMIv2", "serviceProtRefusalSize"),
        ("ZXTM-MIB-SMIv2", "serviceProtRefusalBinary"),
        ("ZXTM-MIB-SMIv2", "serviceLevelNumber"),
        ("ZXTM-MIB-SMIv2", "serviceLevelName"),
        ("ZXTM-MIB-SMIv2", "serviceLevelTotalConn"),
        ("ZXTM-MIB-SMIv2", "serviceLevelTotalNonConf"),
        ("ZXTM-MIB-SMIv2", "serviceLevelResponseMin"),
        ("ZXTM-MIB-SMIv2", "serviceLevelResponseMax"),
        ("ZXTM-MIB-SMIv2", "serviceLevelResponseMean"),
        ("ZXTM-MIB-SMIv2", "serviceLevelIsOK"),
        ("ZXTM-MIB-SMIv2", "serviceLevelConforming"),
        ("ZXTM-MIB-SMIv2", "serviceLevelCurrentConns"),
        ("ZXTM-MIB-SMIv2", "perNodeServiceLevelInet46SLMName"),
        ("ZXTM-MIB-SMIv2", "perNodeServiceLevelInet46NodeAddressType"),
        ("ZXTM-MIB-SMIv2", "perNodeServiceLevelInet46NodeAddress"),
        ("ZXTM-MIB-SMIv2", "perNodeServiceLevelInet46NodePort"),
        ("ZXTM-MIB-SMIv2", "perNodeServiceLevelInet46TotalConn"),
        ("ZXTM-MIB-SMIv2", "perNodeServiceLevelInet46TotalNonConf"),
        ("ZXTM-MIB-SMIv2", "perNodeServiceLevelInet46ResponseMin"),
        ("ZXTM-MIB-SMIv2", "perNodeServiceLevelInet46ResponseMax"),
        ("ZXTM-MIB-SMIv2", "perNodeServiceLevelInet46ResponseMean"),
        ("ZXTM-MIB-SMIv2", "bandwidthClassNumber"),
        ("ZXTM-MIB-SMIv2", "bandwidthClassName"),
        ("ZXTM-MIB-SMIv2", "bandwidthClassMaximum"),
        ("ZXTM-MIB-SMIv2", "bandwidthClassGuarantee"),
        ("ZXTM-MIB-SMIv2", "bandwidthClassBytesOut"),
        ("ZXTM-MIB-SMIv2", "bandwidthClassPktsDrop"),
        ("ZXTM-MIB-SMIv2", "bandwidthClassBytesDrop"),
        ("ZXTM-MIB-SMIv2", "rateClassNumber"),
        ("ZXTM-MIB-SMIv2", "rateClassName"),
        ("ZXTM-MIB-SMIv2", "rateClassMaxRatePerMin"),
        ("ZXTM-MIB-SMIv2", "rateClassMaxRatePerSec"),
        ("ZXTM-MIB-SMIv2", "rateClassQueueLength"),
        ("ZXTM-MIB-SMIv2", "rateClassCurrentRate"),
        ("ZXTM-MIB-SMIv2", "rateClassDropped"),
        ("ZXTM-MIB-SMIv2", "rateClassConnsEntered"),
        ("ZXTM-MIB-SMIv2", "rateClassConnsLeft"),
        ("ZXTM-MIB-SMIv2", "userCounterNumber"),
        ("ZXTM-MIB-SMIv2", "userCounterName"),
        ("ZXTM-MIB-SMIv2", "userCounterValue"),
        ("ZXTM-MIB-SMIv2", "userCounter64Name"),
        ("ZXTM-MIB-SMIv2", "userCounter64Value"),
        ("ZXTM-MIB-SMIv2", "interfaceNumber"),
        ("ZXTM-MIB-SMIv2", "interfaceName"),
        ("ZXTM-MIB-SMIv2", "interfaceRxPackets"),
        ("ZXTM-MIB-SMIv2", "interfaceTxPackets"),
        ("ZXTM-MIB-SMIv2", "interfaceRxErrors"),
        ("ZXTM-MIB-SMIv2", "interfaceTxErrors"),
        ("ZXTM-MIB-SMIv2", "interfaceCollisions"),
        ("ZXTM-MIB-SMIv2", "interfaceRxBytes"),
        ("ZXTM-MIB-SMIv2", "interfaceTxBytes"),
        ("ZXTM-MIB-SMIv2", "webCacheHits"),
        ("ZXTM-MIB-SMIv2", "webCacheMisses"),
        ("ZXTM-MIB-SMIv2", "webCacheLookups"),
        ("ZXTM-MIB-SMIv2", "webCacheMemUsed"),
        ("ZXTM-MIB-SMIv2", "webCacheMemMaximum"),
        ("ZXTM-MIB-SMIv2", "webCacheHitRate"),
        ("ZXTM-MIB-SMIv2", "webCacheEntries"),
        ("ZXTM-MIB-SMIv2", "webCacheMaxEntries"),
        ("ZXTM-MIB-SMIv2", "webCacheOldest"),
        ("ZXTM-MIB-SMIv2", "webCacheURLStoreAllocated"),
        ("ZXTM-MIB-SMIv2", "webCacheURLStoreFree"),
        ("ZXTM-MIB-SMIv2", "webCacheURLStoreSize"),
        ("ZXTM-MIB-SMIv2", "webCacheURLStoreTotalAllocations"),
        ("ZXTM-MIB-SMIv2", "webCacheURLStoreTotalFailures"),
        ("ZXTM-MIB-SMIv2", "webCacheURLStoreTotalFrees"),
        ("ZXTM-MIB-SMIv2", "sslCacheHits"),
        ("ZXTM-MIB-SMIv2", "sslCacheMisses"),
        ("ZXTM-MIB-SMIv2", "sslCacheLookups"),
        ("ZXTM-MIB-SMIv2", "sslCacheHitRate"),
        ("ZXTM-MIB-SMIv2", "sslCacheEntries"),
        ("ZXTM-MIB-SMIv2", "sslCacheEntriesMax"),
        ("ZXTM-MIB-SMIv2", "sslCacheOldest"),
        ("ZXTM-MIB-SMIv2", "aspSessionCacheHits"),
        ("ZXTM-MIB-SMIv2", "aspSessionCacheMisses"),
        ("ZXTM-MIB-SMIv2", "aspSessionCacheLookups"),
        ("ZXTM-MIB-SMIv2", "aspSessionCacheHitRate"),
        ("ZXTM-MIB-SMIv2", "aspSessionCacheEntries"),
        ("ZXTM-MIB-SMIv2", "aspSessionCacheEntriesMax"),
        ("ZXTM-MIB-SMIv2", "aspSessionCacheOldest"),
        ("ZXTM-MIB-SMIv2", "ipSessionCacheHits"),
        ("ZXTM-MIB-SMIv2", "ipSessionCacheMisses"),
        ("ZXTM-MIB-SMIv2", "ipSessionCacheLookups"),
        ("ZXTM-MIB-SMIv2", "ipSessionCacheHitRate"),
        ("ZXTM-MIB-SMIv2", "ipSessionCacheEntries"),
        ("ZXTM-MIB-SMIv2", "ipSessionCacheEntriesMax"),
        ("ZXTM-MIB-SMIv2", "ipSessionCacheOldest"),
        ("ZXTM-MIB-SMIv2", "j2eeSessionCacheHits"),
        ("ZXTM-MIB-SMIv2", "j2eeSessionCacheMisses"),
        ("ZXTM-MIB-SMIv2", "j2eeSessionCacheLookups"),
        ("ZXTM-MIB-SMIv2", "j2eeSessionCacheHitRate"),
        ("ZXTM-MIB-SMIv2", "j2eeSessionCacheEntries"),
        ("ZXTM-MIB-SMIv2", "j2eeSessionCacheEntriesMax"),
        ("ZXTM-MIB-SMIv2", "j2eeSessionCacheOldest"),
        ("ZXTM-MIB-SMIv2", "uniSessionCacheHits"),
        ("ZXTM-MIB-SMIv2", "uniSessionCacheMisses"),
        ("ZXTM-MIB-SMIv2", "uniSessionCacheLookups"),
        ("ZXTM-MIB-SMIv2", "uniSessionCacheHitRate"),
        ("ZXTM-MIB-SMIv2", "uniSessionCacheEntries"),
        ("ZXTM-MIB-SMIv2", "uniSessionCacheEntriesMax"),
        ("ZXTM-MIB-SMIv2", "uniSessionCacheOldest"),
        ("ZXTM-MIB-SMIv2", "sslSessionCacheHits"),
        ("ZXTM-MIB-SMIv2", "sslSessionCacheMisses"),
        ("ZXTM-MIB-SMIv2", "sslSessionCacheLookups"),
        ("ZXTM-MIB-SMIv2", "sslSessionCacheHitRate"),
        ("ZXTM-MIB-SMIv2", "sslSessionCacheEntries"),
        ("ZXTM-MIB-SMIv2", "sslSessionCacheEntriesMax"),
        ("ZXTM-MIB-SMIv2", "sslSessionCacheOldest"),
        ("ZXTM-MIB-SMIv2", "ruleNumber"),
        ("ZXTM-MIB-SMIv2", "ruleName"),
        ("ZXTM-MIB-SMIv2", "ruleExecutions"),
        ("ZXTM-MIB-SMIv2", "ruleAborts"),
        ("ZXTM-MIB-SMIv2", "ruleResponds"),
        ("ZXTM-MIB-SMIv2", "rulePoolSelect"),
        ("ZXTM-MIB-SMIv2", "ruleRetries"),
        ("ZXTM-MIB-SMIv2", "ruleDiscards"),
        ("ZXTM-MIB-SMIv2", "ruleExecutionTimeWarnings"),
        ("ZXTM-MIB-SMIv2", "monitorNumber"),
        ("ZXTM-MIB-SMIv2", "monitorName"),
        ("ZXTM-MIB-SMIv2", "licensekeyNumber"),
        ("ZXTM-MIB-SMIv2", "licensekeyName"),
        ("ZXTM-MIB-SMIv2", "zxtmNumber"),
        ("ZXTM-MIB-SMIv2", "zxtmName"),
        ("ZXTM-MIB-SMIv2", "glbServiceNumber"),
        ("ZXTM-MIB-SMIv2", "glbServiceName"),
        ("ZXTM-MIB-SMIv2", "glbServiceResponses"),
        ("ZXTM-MIB-SMIv2", "glbServiceUnmodified"),
        ("ZXTM-MIB-SMIv2", "glbServiceDiscarded"),
        ("ZXTM-MIB-SMIv2", "perLocationServiceLocationName"),
        ("ZXTM-MIB-SMIv2", "perLocationServiceLocationCode"),
        ("ZXTM-MIB-SMIv2", "perLocationServiceName"),
        ("ZXTM-MIB-SMIv2", "perLocationServiceDraining"),
        ("ZXTM-MIB-SMIv2", "perLocationServiceState"),
        ("ZXTM-MIB-SMIv2", "perLocationServiceFrontendState"),
        ("ZXTM-MIB-SMIv2", "perLocationServiceMonitorState"),
        ("ZXTM-MIB-SMIv2", "perLocationServiceLoad"),
        ("ZXTM-MIB-SMIv2", "perLocationServiceResponses"),
        ("ZXTM-MIB-SMIv2", "locationName"),
        ("ZXTM-MIB-SMIv2", "locationCode"),
        ("ZXTM-MIB-SMIv2", "locationLoad"),
        ("ZXTM-MIB-SMIv2", "locationResponses"),
        ("ZXTM-MIB-SMIv2", "eventNumber"),
        ("ZXTM-MIB-SMIv2", "eventName"),
        ("ZXTM-MIB-SMIv2", "eventsMatched"),
        ("ZXTM-MIB-SMIv2", "actionNumber"),
        ("ZXTM-MIB-SMIv2", "actionName"),
        ("ZXTM-MIB-SMIv2", "actionsProcessed"),
        ("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "confName"),
        ("ZXTM-MIB-SMIv2", "customEventName"),
        ("ZXTM-MIB-SMIv2", "cloudcredentialsClassNumber"),
        ("ZXTM-MIB-SMIv2", "cloudcredentialsName"),
        ("ZXTM-MIB-SMIv2", "cloudcredentialsStatusRequests"),
        ("ZXTM-MIB-SMIv2", "cloudcredentialsNodeCreations"),
        ("ZXTM-MIB-SMIv2", "cloudcredentialsNodeDeletions"),
        ("ZXTM-MIB-SMIv2", "domainName"),
        ("ZXTM-MIB-SMIv2", "listenIPAddressType"),
        ("ZXTM-MIB-SMIv2", "listenIPAddress"),
        ("ZXTM-MIB-SMIv2", "listenIPBytesIn"),
        ("ZXTM-MIB-SMIv2", "listenIPBytesOut"),
        ("ZXTM-MIB-SMIv2", "listenIPCurrentConn"),
        ("ZXTM-MIB-SMIv2", "listenIPTotalRequests"),
        ("ZXTM-MIB-SMIv2", "listenIPMaxConn"),
        ("ZXTM-MIB-SMIv2", "hourlyPeakBytesInPerSecond"),
        ("ZXTM-MIB-SMIv2", "hourlyPeakBytesOutPerSecond"),
        ("ZXTM-MIB-SMIv2", "hourlyPeakRequestsPerSecond"),
        ("ZXTM-MIB-SMIv2", "hourlyPeakSSLConnectionsPerSecond"),
        ("ZXTM-MIB-SMIv2", "numberSNMPGetBulkRequests"),
        ("ZXTM-MIB-SMIv2", "authenticatorNumber"),
        ("ZXTM-MIB-SMIv2", "authenticatorName"),
        ("ZXTM-MIB-SMIv2", "authenticatorRequests"),
        ("ZXTM-MIB-SMIv2", "authenticatorPasses"),
        ("ZXTM-MIB-SMIv2", "authenticatorFails"),
        ("ZXTM-MIB-SMIv2", "authenticatorErrors"),
        ("ZXTM-MIB-SMIv2", "steelheadNumber"),
        ("ZXTM-MIB-SMIv2", "steelheadName"),
        ("ZXTM-MIB-SMIv2", "steelheadOptimized"),
        ("ZXTM-MIB-SMIv2", "virtualserverCertStatusRequests"),
        ("ZXTM-MIB-SMIv2", "virtualserverCertStatusResponses"),
        ("ZXTM-MIB-SMIv2", "sslOcspStaplingCacheCount"),
        ("ZXTM-MIB-SMIv2", "sslOcspStaplingCount"),
        ("ZXTM-MIB-SMIv2", "sslOcspStaplingSuccessCount"),
        ("ZXTM-MIB-SMIv2", "sslOcspStaplingFailureCount"),
        ("ZXTM-MIB-SMIv2", "sslOcspStaplingGoodCount"),
        ("ZXTM-MIB-SMIv2", "sslOcspStaplingRevokedCount"),
        ("ZXTM-MIB-SMIv2", "sslOcspStaplingUnknownCount"),
        ("ZXTM-MIB-SMIv2", "sslCipherDSASigns"),
        ("ZXTM-MIB-SMIv2", "sslCipherDSAVerifies"),
        ("ZXTM-MIB-SMIv2", "sslHandshakeTLSv12"),
        ("ZXTM-MIB-SMIv2", "sslCipherDHGenerates"),
        ("ZXTM-MIB-SMIv2", "sslCipherDHAgreements"),
        ("ZXTM-MIB-SMIv2", "sslCipherAESGCMEncrypts"),
        ("ZXTM-MIB-SMIv2", "sslCipherAESGCMDecrypts"),
        ("ZXTM-MIB-SMIv2", "sslCipherECDHGenerates"),
        ("ZXTM-MIB-SMIv2", "sslCipherECDHAgreements"),
        ("ZXTM-MIB-SMIv2", "sslCipherECDSASigns"),
        ("ZXTM-MIB-SMIv2", "sslCipherECDSAVerifies"),
        ("ZXTM-MIB-SMIv2", "dataPlaneAccelCoreNumber"),
        ("ZXTM-MIB-SMIv2", "coreId"),
        ("ZXTM-MIB-SMIv2", "coreUtilizationPercent"))
)
if mibBuilder.loadTexts:
    mainGroup.setStatus("current")

deprecatedGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 29, 2)
)
deprecatedGroup.setObjects(
      *(("ZXTM-MIB-SMIv2", "sslSessionIDDiskCacheHit"),
        ("ZXTM-MIB-SMIv2", "sslSessionIDDiskCacheMiss"))
)
if mibBuilder.loadTexts:
    deprecatedGroup.setStatus("deprecated")

obsoleteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 29, 3)
)
obsoleteGroup.setObjects(
      *(("ZXTM-MIB-SMIv2", "nodeNumber"),
        ("ZXTM-MIB-SMIv2", "nodeIPAddress"),
        ("ZXTM-MIB-SMIv2", "nodePort"),
        ("ZXTM-MIB-SMIv2", "nodeHostName"),
        ("ZXTM-MIB-SMIv2", "nodeState"),
        ("ZXTM-MIB-SMIv2", "nodeBytesToNodeLo"),
        ("ZXTM-MIB-SMIv2", "nodeBytesToNodeHi"),
        ("ZXTM-MIB-SMIv2", "nodeBytesFromNodeLo"),
        ("ZXTM-MIB-SMIv2", "nodeBytesFromNodeHi"),
        ("ZXTM-MIB-SMIv2", "nodeCurrentRequests"),
        ("ZXTM-MIB-SMIv2", "nodeTotalConn"),
        ("ZXTM-MIB-SMIv2", "nodePooledConn"),
        ("ZXTM-MIB-SMIv2", "nodeFailures"),
        ("ZXTM-MIB-SMIv2", "nodeNewConn"),
        ("ZXTM-MIB-SMIv2", "nodeErrors"),
        ("ZXTM-MIB-SMIv2", "nodeResponseMin"),
        ("ZXTM-MIB-SMIv2", "nodeResponseMax"),
        ("ZXTM-MIB-SMIv2", "nodeResponseMean"),
        ("ZXTM-MIB-SMIv2", "nodeCurrentConn"),
        ("ZXTM-MIB-SMIv2", "trafficIPNumber"),
        ("ZXTM-MIB-SMIv2", "trafficIPNumberRaised"),
        ("ZXTM-MIB-SMIv2", "trafficIPAddress"),
        ("ZXTM-MIB-SMIv2", "trafficIPTime"),
        ("ZXTM-MIB-SMIv2", "trafficIPState"),
        ("ZXTM-MIB-SMIv2", "perNodeServiceLevelSLMName"),
        ("ZXTM-MIB-SMIv2", "perNodeServiceLevelNodeIPAddr"),
        ("ZXTM-MIB-SMIv2", "perNodeServiceLevelNodePort"),
        ("ZXTM-MIB-SMIv2", "perNodeServiceLevelTotalConn"),
        ("ZXTM-MIB-SMIv2", "perNodeServiceLevelTotalNonConf"),
        ("ZXTM-MIB-SMIv2", "perNodeServiceLevelResponseMin"),
        ("ZXTM-MIB-SMIv2", "perNodeServiceLevelResponseMax"),
        ("ZXTM-MIB-SMIv2", "perNodeServiceLevelResponseMean"),
        ("ZXTM-MIB-SMIv2", "totalBytesInLo"),
        ("ZXTM-MIB-SMIv2", "totalBytesInHi"),
        ("ZXTM-MIB-SMIv2", "totalBytesOutLo"),
        ("ZXTM-MIB-SMIv2", "totalBytesOutHi"),
        ("ZXTM-MIB-SMIv2", "virtualserverBytesInLo"),
        ("ZXTM-MIB-SMIv2", "virtualserverBytesInHi"),
        ("ZXTM-MIB-SMIv2", "virtualserverBytesOutLo"),
        ("ZXTM-MIB-SMIv2", "virtualserverBytesOutHi"),
        ("ZXTM-MIB-SMIv2", "virtualserverPktsInLo"),
        ("ZXTM-MIB-SMIv2", "virtualserverPktsInHi"),
        ("ZXTM-MIB-SMIv2", "virtualserverPktsOutLo"),
        ("ZXTM-MIB-SMIv2", "virtualserverPktsOutHi"),
        ("ZXTM-MIB-SMIv2", "virtualserverGzipBytesSavedLo"),
        ("ZXTM-MIB-SMIv2", "virtualserverGzipBytesSavedHi"),
        ("ZXTM-MIB-SMIv2", "virtualserverTotalConn"),
        ("ZXTM-MIB-SMIv2", "virtualserverTotalRequestsLo"),
        ("ZXTM-MIB-SMIv2", "virtualserverTotalRequestsHi"),
        ("ZXTM-MIB-SMIv2", "virtualserverTotalHTTPRequestsLo"),
        ("ZXTM-MIB-SMIv2", "virtualserverTotalHTTPRequestsHi"),
        ("ZXTM-MIB-SMIv2", "virtualserverTotalHTTP1RequestsLo"),
        ("ZXTM-MIB-SMIv2", "virtualserverTotalHTTP1RequestsHi"),
        ("ZXTM-MIB-SMIv2", "virtualserverTotalHTTP2RequestsLo"),
        ("ZXTM-MIB-SMIv2", "virtualserverTotalHTTP2RequestsHi"),
        ("ZXTM-MIB-SMIv2", "virtualserverBwLimitPktsDropLo"),
        ("ZXTM-MIB-SMIv2", "virtualserverBwLimitPktsDropHi"),
        ("ZXTM-MIB-SMIv2", "virtualserverBwLimitBytesDropLo"),
        ("ZXTM-MIB-SMIv2", "virtualserverBwLimitBytesDropHi"),
        ("ZXTM-MIB-SMIv2", "poolBytesInLo"),
        ("ZXTM-MIB-SMIv2", "poolBytesInHi"),
        ("ZXTM-MIB-SMIv2", "poolBytesOutLo"),
        ("ZXTM-MIB-SMIv2", "poolBytesOutHi"),
        ("ZXTM-MIB-SMIv2", "poolBwLimitPktsDropLo"),
        ("ZXTM-MIB-SMIv2", "poolBwLimitPktsDropHi"),
        ("ZXTM-MIB-SMIv2", "poolBwLimitBytesDropLo"),
        ("ZXTM-MIB-SMIv2", "poolBwLimitBytesDropHi"),
        ("ZXTM-MIB-SMIv2", "nodeInet46BytesToNodeLo"),
        ("ZXTM-MIB-SMIv2", "nodeInet46BytesToNodeHi"),
        ("ZXTM-MIB-SMIv2", "nodeInet46BytesFromNodeLo"),
        ("ZXTM-MIB-SMIv2", "nodeInet46BytesFromNodeHi"),
        ("ZXTM-MIB-SMIv2", "perPoolNodeBytesToNodeLo"),
        ("ZXTM-MIB-SMIv2", "perPoolNodeBytesToNodeHi"),
        ("ZXTM-MIB-SMIv2", "perPoolNodeBytesFromNodeLo"),
        ("ZXTM-MIB-SMIv2", "perPoolNodeBytesFromNodeHi"),
        ("ZXTM-MIB-SMIv2", "perPoolNodePktsToNodeLo"),
        ("ZXTM-MIB-SMIv2", "perPoolNodePktsToNodeHi"),
        ("ZXTM-MIB-SMIv2", "perPoolNodePktsFromNodeLo"),
        ("ZXTM-MIB-SMIv2", "perPoolNodePktsFromNodeHi"),
        ("ZXTM-MIB-SMIv2", "bandwidthClassBytesOutLo"),
        ("ZXTM-MIB-SMIv2", "bandwidthClassBytesOutHi"),
        ("ZXTM-MIB-SMIv2", "bandwidthClassPktsDropLo"),
        ("ZXTM-MIB-SMIv2", "bandwidthClassPktsDropHi"),
        ("ZXTM-MIB-SMIv2", "bandwidthClassBytesDropLo"),
        ("ZXTM-MIB-SMIv2", "bandwidthClassBytesDropHi"),
        ("ZXTM-MIB-SMIv2", "interfaceRxBytesLo"),
        ("ZXTM-MIB-SMIv2", "interfaceRxBytesHi"),
        ("ZXTM-MIB-SMIv2", "interfaceTxBytesLo"),
        ("ZXTM-MIB-SMIv2", "interfaceTxBytesHi"),
        ("ZXTM-MIB-SMIv2", "webCacheHitsLo"),
        ("ZXTM-MIB-SMIv2", "webCacheHitsHi"),
        ("ZXTM-MIB-SMIv2", "webCacheMissesLo"),
        ("ZXTM-MIB-SMIv2", "webCacheMissesHi"),
        ("ZXTM-MIB-SMIv2", "webCacheLookupsLo"),
        ("ZXTM-MIB-SMIv2", "webCacheLookupsHi"),
        ("ZXTM-MIB-SMIv2", "listenIPBytesInLo"),
        ("ZXTM-MIB-SMIv2", "listenIPBytesInHi"),
        ("ZXTM-MIB-SMIv2", "listenIPBytesOutLo"),
        ("ZXTM-MIB-SMIv2", "listenIPBytesOutHi"),
        ("ZXTM-MIB-SMIv2", "listenIPTotalConn"),
        ("ZXTM-MIB-SMIv2", "listenIPTotalRequestsLo"),
        ("ZXTM-MIB-SMIv2", "listenIPTotalRequestsHi"),
        ("ZXTM-MIB-SMIv2", "sslHandshakeSSLv2"))
)
if mibBuilder.loadTexts:
    obsoleteGroup.setStatus("obsolete")


# Notification objects

testaction = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 1)
)
testaction.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "actionName"))
)
if mibBuilder.loadTexts:
    testaction.setStatus(
        "current"
    )

running = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 2)
)
running.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    running.setStatus(
        "current"
    )

fewfreefds = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 3)
)
fewfreefds.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    fewfreefds.setStatus(
        "current"
    )

restartrequired = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 4)
)
restartrequired.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    restartrequired.setStatus(
        "current"
    )

timemovedback = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 5)
)
timemovedback.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    timemovedback.setStatus(
        "current"
    )

sslfail = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 6)
)
sslfail.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    sslfail.setStatus(
        "current"
    )

hardware = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 7)
)
hardware.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    hardware.setStatus(
        "deprecated"
    )

zxtmswerror = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 8)
)
zxtmswerror.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    zxtmswerror.setStatus(
        "current"
    )

customevent = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 9)
)
customevent.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "customEventName"))
)
if mibBuilder.loadTexts:
    customevent.setStatus(
        "current"
    )

versionmismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 10)
)
versionmismatch.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    versionmismatch.setStatus(
        "current"
    )

machineok = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 11)
)
machineok.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "zxtmName"))
)
if mibBuilder.loadTexts:
    machineok.setStatus(
        "current"
    )

machinetimeout = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 12)
)
machinetimeout.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "zxtmName"))
)
if mibBuilder.loadTexts:
    machinetimeout.setStatus(
        "current"
    )

machinefail = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 13)
)
machinefail.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "zxtmName"))
)
if mibBuilder.loadTexts:
    machinefail.setStatus(
        "current"
    )

allmachinesok = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 14)
)
allmachinesok.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    allmachinesok.setStatus(
        "current"
    )

flipperbackendsworking = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 15)
)
flipperbackendsworking.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    flipperbackendsworking.setStatus(
        "current"
    )

flipperfrontendsworking = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 16)
)
flipperfrontendsworking.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    flipperfrontendsworking.setStatus(
        "current"
    )

pingbackendfail = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 17)
)
pingbackendfail.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    pingbackendfail.setStatus(
        "current"
    )

pingfrontendfail = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 18)
)
pingfrontendfail.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    pingfrontendfail.setStatus(
        "current"
    )

pinggwfail = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 19)
)
pinggwfail.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    pinggwfail.setStatus(
        "current"
    )

statebaddata = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 20)
)
statebaddata.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    statebaddata.setStatus(
        "current"
    )

stateconnfail = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 21)
)
stateconnfail.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    stateconnfail.setStatus(
        "current"
    )

stateok = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 22)
)
stateok.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    stateok.setStatus(
        "current"
    )

statereadfail = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 23)
)
statereadfail.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    statereadfail.setStatus(
        "current"
    )

statetimeout = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 24)
)
statetimeout.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    statetimeout.setStatus(
        "current"
    )

stateunexpected = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 25)
)
stateunexpected.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    stateunexpected.setStatus(
        "current"
    )

statewritefail = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 26)
)
statewritefail.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    statewritefail.setStatus(
        "current"
    )

sslhwfail = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 27)
)
sslhwfail.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    sslhwfail.setStatus(
        "current"
    )

sslhwrestart = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 28)
)
sslhwrestart.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    sslhwrestart.setStatus(
        "current"
    )

sslhwstart = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 29)
)
sslhwstart.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    sslhwstart.setStatus(
        "current"
    )

confdel = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 30)
)
confdel.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "confName"))
)
if mibBuilder.loadTexts:
    confdel.setStatus(
        "current"
    )

confmod = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 31)
)
confmod.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "confName"))
)
if mibBuilder.loadTexts:
    confmod.setStatus(
        "current"
    )

confadd = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 32)
)
confadd.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "confName"))
)
if mibBuilder.loadTexts:
    confadd.setStatus(
        "current"
    )

confok = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 33)
)
confok.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "confName"))
)
if mibBuilder.loadTexts:
    confok.setStatus(
        "current"
    )

javadied = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 34)
)
javadied.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    javadied.setStatus(
        "current"
    )

javastop = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 35)
)
javastop.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    javastop.setStatus(
        "current"
    )

javastartfail = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 36)
)
javastartfail.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    javastartfail.setStatus(
        "current"
    )

javaterminatefail = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 37)
)
javaterminatefail.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    javaterminatefail.setStatus(
        "current"
    )

javanotfound = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 38)
)
javanotfound.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    javanotfound.setStatus(
        "current"
    )

javastarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 39)
)
javastarted.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    javastarted.setStatus(
        "current"
    )

servleterror = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 40)
)
servleterror.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    servleterror.setStatus(
        "current"
    )

monitorfail = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 41)
)
monitorfail.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "monitorName"))
)
if mibBuilder.loadTexts:
    monitorfail.setStatus(
        "current"
    )

monitorok = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 42)
)
monitorok.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "monitorName"))
)
if mibBuilder.loadTexts:
    monitorok.setStatus(
        "current"
    )

rulexmlerr = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 43)
)
rulexmlerr.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "ruleName"))
)
if mibBuilder.loadTexts:
    rulexmlerr.setStatus(
        "current"
    )

pooluseunknown = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 44)
)
pooluseunknown.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "ruleName"))
)
if mibBuilder.loadTexts:
    pooluseunknown.setStatus(
        "current"
    )

ruleabort = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 45)
)
ruleabort.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "ruleName"))
)
if mibBuilder.loadTexts:
    ruleabort.setStatus(
        "current"
    )

rulebufferlarge = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 46)
)
rulebufferlarge.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "ruleName"))
)
if mibBuilder.loadTexts:
    rulebufferlarge.setStatus(
        "current"
    )

rulebodycomperror = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 47)
)
rulebodycomperror.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "ruleName"))
)
if mibBuilder.loadTexts:
    rulebodycomperror.setStatus(
        "current"
    )

forwardproxybadhost = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 48)
)
forwardproxybadhost.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "ruleName"))
)
if mibBuilder.loadTexts:
    forwardproxybadhost.setStatus(
        "current"
    )

invalidemit = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 49)
)
invalidemit.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "ruleName"))
)
if mibBuilder.loadTexts:
    invalidemit.setStatus(
        "current"
    )

rulenopersistence = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 50)
)
rulenopersistence.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "ruleName"))
)
if mibBuilder.loadTexts:
    rulenopersistence.setStatus(
        "current"
    )

rulelogmsginfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 51)
)
rulelogmsginfo.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "ruleName"))
)
if mibBuilder.loadTexts:
    rulelogmsginfo.setStatus(
        "current"
    )

rulelogmsgwarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 52)
)
rulelogmsgwarn.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "ruleName"))
)
if mibBuilder.loadTexts:
    rulelogmsgwarn.setStatus(
        "current"
    )

rulelogmsgserious = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 53)
)
rulelogmsgserious.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "ruleName"))
)
if mibBuilder.loadTexts:
    rulelogmsgserious.setStatus(
        "current"
    )

norate = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 54)
)
norate.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "ruleName"))
)
if mibBuilder.loadTexts:
    norate.setStatus(
        "current"
    )

poolactivenodesunknown = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 55)
)
poolactivenodesunknown.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "ruleName"))
)
if mibBuilder.loadTexts:
    poolactivenodesunknown.setStatus(
        "current"
    )

datastorefull = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 56)
)
datastorefull.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    datastorefull.setStatus(
        "current"
    )

expired = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 57)
)
expired.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "licensekeyName"))
)
if mibBuilder.loadTexts:
    expired.setStatus(
        "current"
    )

licensecorrupt = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 58)
)
licensecorrupt.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "licensekeyName"))
)
if mibBuilder.loadTexts:
    licensecorrupt.setStatus(
        "current"
    )

expiresoon = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 59)
)
expiresoon.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "licensekeyName"))
)
if mibBuilder.loadTexts:
    expiresoon.setStatus(
        "current"
    )

usinglicense = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 60)
)
usinglicense.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "licensekeyName"))
)
if mibBuilder.loadTexts:
    usinglicense.setStatus(
        "current"
    )

licenseclustertoobig = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 61)
)
licenseclustertoobig.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    licenseclustertoobig.setStatus(
        "current"
    )

unlicensed = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 62)
)
unlicensed.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    unlicensed.setStatus(
        "current"
    )

usingdevlicense = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 63)
)
usingdevlicense.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    usingdevlicense.setStatus(
        "current"
    )

poolnonodes = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 64)
)
poolnonodes.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "poolName"))
)
if mibBuilder.loadTexts:
    poolnonodes.setStatus(
        "current"
    )

poolok = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 65)
)
poolok.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "poolName"))
)
if mibBuilder.loadTexts:
    poolok.setStatus(
        "current"
    )

pooldied = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 66)
)
pooldied.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "poolName"))
)
if mibBuilder.loadTexts:
    pooldied.setStatus(
        "current"
    )

noderesolvefailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 67)
)
noderesolvefailure.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "poolName"))
)
if mibBuilder.loadTexts:
    noderesolvefailure.setStatus(
        "current"
    )

noderesolvemultiple = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 68)
)
noderesolvemultiple.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "poolName"))
)
if mibBuilder.loadTexts:
    noderesolvemultiple.setStatus(
        "current"
    )

nodeworking = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 69)
)
nodeworking.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "perPoolNodePoolName"),
        ("ZXTM-MIB-SMIv2", "perPoolNodeNodeAddressType"),
        ("ZXTM-MIB-SMIv2", "perPoolNodeNodeAddress"),
        ("ZXTM-MIB-SMIv2", "perPoolNodeNodePort"))
)
if mibBuilder.loadTexts:
    nodeworking.setStatus(
        "current"
    )

nostarttls = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 70)
)
nostarttls.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "perPoolNodePoolName"),
        ("ZXTM-MIB-SMIv2", "perPoolNodeNodeAddressType"),
        ("ZXTM-MIB-SMIv2", "perPoolNodeNodeAddress"),
        ("ZXTM-MIB-SMIv2", "perPoolNodeNodePort"))
)
if mibBuilder.loadTexts:
    nostarttls.setStatus(
        "current"
    )

nodefail = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 71)
)
nodefail.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "perPoolNodePoolName"),
        ("ZXTM-MIB-SMIv2", "perPoolNodeNodeAddressType"),
        ("ZXTM-MIB-SMIv2", "perPoolNodeNodeAddress"),
        ("ZXTM-MIB-SMIv2", "perPoolNodeNodePort"))
)
if mibBuilder.loadTexts:
    nodefail.setStatus(
        "current"
    )

starttlsinvalid = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 72)
)
starttlsinvalid.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "perPoolNodePoolName"),
        ("ZXTM-MIB-SMIv2", "perPoolNodeNodeAddressType"),
        ("ZXTM-MIB-SMIv2", "perPoolNodeNodeAddress"),
        ("ZXTM-MIB-SMIv2", "perPoolNodeNodePort"))
)
if mibBuilder.loadTexts:
    starttlsinvalid.setStatus(
        "current"
    )

ehloinvalid = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 73)
)
ehloinvalid.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "perPoolNodePoolName"),
        ("ZXTM-MIB-SMIv2", "perPoolNodeNodeAddressType"),
        ("ZXTM-MIB-SMIv2", "perPoolNodeNodeAddress"),
        ("ZXTM-MIB-SMIv2", "perPoolNodeNodePort"))
)
if mibBuilder.loadTexts:
    ehloinvalid.setStatus(
        "current"
    )

flipperraiselocalworking = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 74)
)
flipperraiselocalworking.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "trafficIPInet46AddressType"),
        ("ZXTM-MIB-SMIv2", "trafficIPInet46Address"))
)
if mibBuilder.loadTexts:
    flipperraiselocalworking.setStatus(
        "current"
    )

flipperraiseothersdead = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 75)
)
flipperraiseothersdead.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "trafficIPInet46AddressType"),
        ("ZXTM-MIB-SMIv2", "trafficIPInet46Address"))
)
if mibBuilder.loadTexts:
    flipperraiseothersdead.setStatus(
        "current"
    )

flipperraiseosdrop = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 76)
)
flipperraiseosdrop.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "trafficIPInet46AddressType"),
        ("ZXTM-MIB-SMIv2", "trafficIPInet46Address"))
)
if mibBuilder.loadTexts:
    flipperraiseosdrop.setStatus(
        "current"
    )

dropipinfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 77)
)
dropipinfo.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "trafficIPInet46AddressType"),
        ("ZXTM-MIB-SMIv2", "trafficIPInet46Address"))
)
if mibBuilder.loadTexts:
    dropipinfo.setStatus(
        "current"
    )

dropipwarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 78)
)
dropipwarn.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "trafficIPInet46AddressType"),
        ("ZXTM-MIB-SMIv2", "trafficIPInet46Address"))
)
if mibBuilder.loadTexts:
    dropipwarn.setStatus(
        "current"
    )

flipperdadreraise = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 79)
)
flipperdadreraise.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "trafficIPInet46AddressType"),
        ("ZXTM-MIB-SMIv2", "trafficIPInet46Address"))
)
if mibBuilder.loadTexts:
    flipperdadreraise.setStatus(
        "current"
    )

flipperipexists = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 80)
)
flipperipexists.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "trafficIPInet46AddressType"),
        ("ZXTM-MIB-SMIv2", "trafficIPInet46Address"))
)
if mibBuilder.loadTexts:
    flipperipexists.setStatus(
        "current"
    )

triggersummary = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 81)
)
triggersummary.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "serviceProtName"))
)
if mibBuilder.loadTexts:
    triggersummary.setStatus(
        "current"
    )

slmclasslimitexceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 82)
)
slmclasslimitexceeded.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    slmclasslimitexceeded.setStatus(
        "current"
    )

slmrecoveredwarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 83)
)
slmrecoveredwarn.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "serviceLevelName"))
)
if mibBuilder.loadTexts:
    slmrecoveredwarn.setStatus(
        "current"
    )

slmrecoveredserious = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 84)
)
slmrecoveredserious.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "serviceLevelName"))
)
if mibBuilder.loadTexts:
    slmrecoveredserious.setStatus(
        "current"
    )

slmfallenbelowwarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 85)
)
slmfallenbelowwarn.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "serviceLevelName"))
)
if mibBuilder.loadTexts:
    slmfallenbelowwarn.setStatus(
        "current"
    )

slmfallenbelowserious = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 86)
)
slmfallenbelowserious.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "serviceLevelName"))
)
if mibBuilder.loadTexts:
    slmfallenbelowserious.setStatus(
        "current"
    )

vscrloutofdate = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 87)
)
vscrloutofdate.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    vscrloutofdate.setStatus(
        "current"
    )

vsstart = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 88)
)
vsstart.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "virtualserverName"))
)
if mibBuilder.loadTexts:
    vsstart.setStatus(
        "current"
    )

vsstop = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 89)
)
vsstop.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "virtualserverName"))
)
if mibBuilder.loadTexts:
    vsstop.setStatus(
        "current"
    )

privkeyok = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 90)
)
privkeyok.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "virtualserverName"))
)
if mibBuilder.loadTexts:
    privkeyok.setStatus(
        "current"
    )

ssldrop = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 91)
)
ssldrop.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "virtualserverName"))
)
if mibBuilder.loadTexts:
    ssldrop.setStatus(
        "current"
    )

vslogwritefail = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 92)
)
vslogwritefail.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "virtualserverName"))
)
if mibBuilder.loadTexts:
    vslogwritefail.setStatus(
        "current"
    )

vssslcertexpired = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 93)
)
vssslcertexpired.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "virtualserverName"))
)
if mibBuilder.loadTexts:
    vssslcertexpired.setStatus(
        "current"
    )

vssslcerttoexpire = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 94)
)
vssslcerttoexpire.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "virtualserverName"))
)
if mibBuilder.loadTexts:
    vssslcerttoexpire.setStatus(
        "current"
    )

vscacertexpired = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 95)
)
vscacertexpired.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "virtualserverName"))
)
if mibBuilder.loadTexts:
    vscacertexpired.setStatus(
        "current"
    )

vscacerttoexpire = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 96)
)
vscacerttoexpire.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "virtualserverName"))
)
if mibBuilder.loadTexts:
    vscacerttoexpire.setStatus(
        "current"
    )

maxclientbufferdrop = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 97)
)
maxclientbufferdrop.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    maxclientbufferdrop.setStatus(
        "current"
    )

respcompfail = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 98)
)
respcompfail.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    respcompfail.setStatus(
        "current"
    )

responsetoolarge = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 99)
)
responsetoolarge.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    responsetoolarge.setStatus(
        "current"
    )

sipstreamnoports = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 100)
)
sipstreamnoports.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    sipstreamnoports.setStatus(
        "current"
    )

rtspstreamnoports = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 101)
)
rtspstreamnoports.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    rtspstreamnoports.setStatus(
        "current"
    )

geodataloadfail = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 102)
)
geodataloadfail.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    geodataloadfail.setStatus(
        "current"
    )

poolpersistencemismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 103)
)
poolpersistencemismatch.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    poolpersistencemismatch.setStatus(
        "current"
    )

connerror = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 104)
)
connerror.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "virtualserverName"))
)
if mibBuilder.loadTexts:
    connerror.setStatus(
        "current"
    )

connfail = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 105)
)
connfail.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "virtualserverName"))
)
if mibBuilder.loadTexts:
    connfail.setStatus(
        "current"
    )

badcontentlen = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 106)
)
badcontentlen.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "perPoolNodePoolName"),
        ("ZXTM-MIB-SMIv2", "perPoolNodeNodeAddressType"),
        ("ZXTM-MIB-SMIv2", "perPoolNodeNodeAddress"),
        ("ZXTM-MIB-SMIv2", "perPoolNodeNodePort"))
)
if mibBuilder.loadTexts:
    badcontentlen.setStatus(
        "current"
    )

activatealldead = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 107)
)
activatealldead.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    activatealldead.setStatus(
        "current"
    )

machinerecovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 108)
)
machinerecovered.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    machinerecovered.setStatus(
        "current"
    )

flipperrecovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 109)
)
flipperrecovered.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    flipperrecovered.setStatus(
        "current"
    )

activatedautomatically = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 110)
)
activatedautomatically.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    activatedautomatically.setStatus(
        "current"
    )

zclustermoderr = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 111)
)
zclustermoderr.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    zclustermoderr.setStatus(
        "current"
    )

ec2flipperraiselocalworking = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 112)
)
ec2flipperraiselocalworking.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    ec2flipperraiselocalworking.setStatus(
        "current"
    )

ec2flipperraiseothersdead = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 113)
)
ec2flipperraiseothersdead.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    ec2flipperraiseothersdead.setStatus(
        "current"
    )

autherror = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 114)
)
autherror.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    autherror.setStatus(
        "current"
    )

logfiledeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 115)
)
logfiledeleted.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "virtualserverName"))
)
if mibBuilder.loadTexts:
    logfiledeleted.setStatus(
        "current"
    )

license_graceperiodexpired = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 116)
)
license_graceperiodexpired.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "licensekeyName"))
)
if mibBuilder.loadTexts:
    license_graceperiodexpired.setStatus(
        "current"
    )

license_authorized = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 117)
)
license_authorized.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "licensekeyName"))
)
if mibBuilder.loadTexts:
    license_authorized.setStatus(
        "current"
    )

license_rejected_authorized = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 118)
)
license_rejected_authorized.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "licensekeyName"))
)
if mibBuilder.loadTexts:
    license_rejected_authorized.setStatus(
        "current"
    )

license_rejected_unauthorized = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 119)
)
license_rejected_unauthorized.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "licensekeyName"))
)
if mibBuilder.loadTexts:
    license_rejected_unauthorized.setStatus(
        "current"
    )

license_timedout_authorized = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 120)
)
license_timedout_authorized.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "licensekeyName"))
)
if mibBuilder.loadTexts:
    license_timedout_authorized.setStatus(
        "current"
    )

license_timedout_unauthorized = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 121)
)
license_timedout_unauthorized.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "licensekeyName"))
)
if mibBuilder.loadTexts:
    license_timedout_unauthorized.setStatus(
        "current"
    )

license_unauthorized = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 122)
)
license_unauthorized.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "licensekeyName"))
)
if mibBuilder.loadTexts:
    license_unauthorized.setStatus(
        "current"
    )

cachesizereduced = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 123)
)
cachesizereduced.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    cachesizereduced.setStatus(
        "current"
    )

morememallowed = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 124)
)
morememallowed.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    morememallowed.setStatus(
        "current"
    )

lessmemallowed = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 125)
)
lessmemallowed.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    lessmemallowed.setStatus(
        "current"
    )

usedcredsdeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 126)
)
usedcredsdeleted.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "cloudcredentialsName"))
)
if mibBuilder.loadTexts:
    usedcredsdeleted.setStatus(
        "current"
    )

apistatusprocesshanging = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 127)
)
apistatusprocesshanging.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "cloudcredentialsName"))
)
if mibBuilder.loadTexts:
    apistatusprocesshanging.setStatus(
        "current"
    )

autonodedestroyed = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 128)
)
autonodedestroyed.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "poolName"))
)
if mibBuilder.loadTexts:
    autonodedestroyed.setStatus(
        "current"
    )

autoscalestatusupdateerror = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 129)
)
autoscalestatusupdateerror.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "cloudcredentialsName"))
)
if mibBuilder.loadTexts:
    autoscalestatusupdateerror.setStatus(
        "current"
    )

ec2iperr = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 130)
)
ec2iperr.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    ec2iperr.setStatus(
        "current"
    )

dropec2ipwarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 131)
)
dropec2ipwarn.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    dropec2ipwarn.setStatus(
        "current"
    )

ec2nopublicip = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 132)
)
ec2nopublicip.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    ec2nopublicip.setStatus(
        "current"
    )

multihostload = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 133)
)
multihostload.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    multihostload.setStatus(
        "current"
    )

tpslimited = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 134)
)
tpslimited.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    tpslimited.setStatus(
        "current"
    )

ssltpslimited = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 135)
)
ssltpslimited.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    ssltpslimited.setStatus(
        "current"
    )

bwlimited = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 136)
)
bwlimited.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    bwlimited.setStatus(
        "current"
    )

licensetoomanylocations = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 137)
)
licensetoomanylocations.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    licensetoomanylocations.setStatus(
        "current"
    )

autonodedestructioncomplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 138)
)
autonodedestructioncomplete.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "poolName"))
)
if mibBuilder.loadTexts:
    autonodedestructioncomplete.setStatus(
        "current"
    )

autonodeexisted = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 139)
)
autonodeexisted.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "poolName"))
)
if mibBuilder.loadTexts:
    autonodeexisted.setStatus(
        "current"
    )

autoscaledpooltoosmall = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 140)
)
autoscaledpooltoosmall.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "poolName"))
)
if mibBuilder.loadTexts:
    autoscaledpooltoosmall.setStatus(
        "current"
    )

autoscaleinvalidargforcreatenode = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 141)
)
autoscaleinvalidargforcreatenode.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "poolName"))
)
if mibBuilder.loadTexts:
    autoscaleinvalidargforcreatenode.setStatus(
        "current"
    )

autonodedisappeared = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 142)
)
autonodedisappeared.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "poolName"))
)
if mibBuilder.loadTexts:
    autonodedisappeared.setStatus(
        "current"
    )

autoscaledpoolrefractory = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 143)
)
autoscaledpoolrefractory.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "poolName"))
)
if mibBuilder.loadTexts:
    autoscaledpoolrefractory.setStatus(
        "current"
    )

cannotshrinkemptypool = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 144)
)
cannotshrinkemptypool.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "poolName"))
)
if mibBuilder.loadTexts:
    cannotshrinkemptypool.setStatus(
        "current"
    )

autoscalinghysteresiscantgrow = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 145)
)
autoscalinghysteresiscantgrow.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "poolName"))
)
if mibBuilder.loadTexts:
    autoscalinghysteresiscantgrow.setStatus(
        "current"
    )

autonodecreationcomplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 146)
)
autonodecreationcomplete.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "poolName"))
)
if mibBuilder.loadTexts:
    autonodecreationcomplete.setStatus(
        "current"
    )

autonodestatuschange = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 147)
)
autonodestatuschange.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "poolName"))
)
if mibBuilder.loadTexts:
    autonodestatuschange.setStatus(
        "current"
    )

autoscalinghysteresiscantshrink = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 148)
)
autoscalinghysteresiscantshrink.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "poolName"))
)
if mibBuilder.loadTexts:
    autoscalinghysteresiscantshrink.setStatus(
        "current"
    )

autoscalingpoolstatechange = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 149)
)
autoscalingpoolstatechange.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "poolName"))
)
if mibBuilder.loadTexts:
    autoscalingpoolstatechange.setStatus(
        "current"
    )

glbmissingips = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 150)
)
glbmissingips.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    glbmissingips.setStatus(
        "current"
    )

glbnolocations = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 151)
)
glbnolocations.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    glbnolocations.setStatus(
        "current"
    )

locationmonitorok = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 152)
)
locationmonitorok.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "locationName"),
        ("ZXTM-MIB-SMIv2", "glbServiceName"))
)
if mibBuilder.loadTexts:
    locationmonitorok.setStatus(
        "current"
    )

locationmonitorfail = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 153)
)
locationmonitorfail.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "locationName"),
        ("ZXTM-MIB-SMIv2", "glbServiceName"))
)
if mibBuilder.loadTexts:
    locationmonitorfail.setStatus(
        "current"
    )

locationok = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 154)
)
locationok.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "locationName"),
        ("ZXTM-MIB-SMIv2", "glbServiceName"))
)
if mibBuilder.loadTexts:
    locationok.setStatus(
        "current"
    )

locationfail = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 155)
)
locationfail.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "locationName"),
        ("ZXTM-MIB-SMIv2", "glbServiceName"))
)
if mibBuilder.loadTexts:
    locationfail.setStatus(
        "current"
    )

locationsoapok = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 156)
)
locationsoapok.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "locationName"),
        ("ZXTM-MIB-SMIv2", "glbServiceName"))
)
if mibBuilder.loadTexts:
    locationsoapok.setStatus(
        "current"
    )

locationsoapfail = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 157)
)
locationsoapfail.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "locationName"),
        ("ZXTM-MIB-SMIv2", "glbServiceName"))
)
if mibBuilder.loadTexts:
    locationsoapfail.setStatus(
        "current"
    )

glbdeadlocmissingips = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 158)
)
glbdeadlocmissingips.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    glbdeadlocmissingips.setStatus(
        "current"
    )

autoscaleresponseparseerror = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 159)
)
autoscaleresponseparseerror.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "cloudcredentialsName"))
)
if mibBuilder.loadTexts:
    autoscaleresponseparseerror.setStatus(
        "current"
    )

glbnewmaster = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 160)
)
glbnewmaster.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "locationName"),
        ("ZXTM-MIB-SMIv2", "glbServiceName"))
)
if mibBuilder.loadTexts:
    glbnewmaster.setStatus(
        "current"
    )

glblogwritefail = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 161)
)
glblogwritefail.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "glbServiceName"))
)
if mibBuilder.loadTexts:
    glblogwritefail.setStatus(
        "current"
    )

glbfailalter = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 162)
)
glbfailalter.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "glbServiceName"))
)
if mibBuilder.loadTexts:
    glbfailalter.setStatus(
        "current"
    )

autoscalednodecontested = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 163)
)
autoscalednodecontested.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "poolName"))
)
if mibBuilder.loadTexts:
    autoscalednodecontested.setStatus(
        "current"
    )

autoscalepoolconfupdate = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 164)
)
autoscalepoolconfupdate.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "poolName"))
)
if mibBuilder.loadTexts:
    autoscalepoolconfupdate.setStatus(
        "current"
    )

autonodecreationstarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 165)
)
autonodecreationstarted.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "poolName"))
)
if mibBuilder.loadTexts:
    autonodecreationstarted.setStatus(
        "current"
    )

autoscaleinvalidargfordeletenode = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 166)
)
autoscaleinvalidargfordeletenode.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "poolName"))
)
if mibBuilder.loadTexts:
    autoscaleinvalidargfordeletenode.setStatus(
        "current"
    )

autoscalinghitroof = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 167)
)
autoscalinghitroof.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "poolName"))
)
if mibBuilder.loadTexts:
    autoscalinghitroof.setStatus(
        "current"
    )

autoscalinghitfloor = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 168)
)
autoscalinghitfloor.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "poolName"))
)
if mibBuilder.loadTexts:
    autoscalinghitfloor.setStatus(
        "current"
    )

apichangeprocesshanging = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 169)
)
apichangeprocesshanging.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "poolName"))
)
if mibBuilder.loadTexts:
    apichangeprocesshanging.setStatus(
        "current"
    )

autoscaledpooltoobig = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 170)
)
autoscaledpooltoobig.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "poolName"))
)
if mibBuilder.loadTexts:
    autoscaledpooltoobig.setStatus(
        "current"
    )

autoscalingprocesstimedout = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 171)
)
autoscalingprocesstimedout.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "cloudcredentialsName"))
)
if mibBuilder.loadTexts:
    autoscalingprocesstimedout.setStatus(
        "current"
    )

autoscalingdisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 172)
)
autoscalingdisabled.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "poolName"))
)
if mibBuilder.loadTexts:
    autoscalingdisabled.setStatus(
        "current"
    )

locmovemachine = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 173)
)
locmovemachine.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "locationName"),
        ("ZXTM-MIB-SMIv2", "zxtmName"))
)
if mibBuilder.loadTexts:
    locmovemachine.setStatus(
        "current"
    )

locempty = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 174)
)
locempty.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "locationName"))
)
if mibBuilder.loadTexts:
    locempty.setStatus(
        "current"
    )

autoscalinglicenseerror = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 175)
)
autoscalinglicenseerror.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    autoscalinglicenseerror.setStatus(
        "current"
    )

autoscalinglicenseenabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 176)
)
autoscalinglicenseenabled.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    autoscalinglicenseenabled.setStatus(
        "current"
    )

autoscalinglicensedisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 177)
)
autoscalinglicensedisabled.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    autoscalinglicensedisabled.setStatus(
        "current"
    )

confreptimeout = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 178)
)
confreptimeout.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    confreptimeout.setStatus(
        "current"
    )

confrepfailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 179)
)
confrepfailed.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    confrepfailed.setStatus(
        "current"
    )

analyticslicenseenabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 180)
)
analyticslicenseenabled.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    analyticslicenseenabled.setStatus(
        "current"
    )

analyticslicensedisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 181)
)
analyticslicensedisabled.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    analyticslicensedisabled.setStatus(
        "current"
    )

autoscalingchangeprocessfailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 182)
)
autoscalingchangeprocessfailure.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "poolName"))
)
if mibBuilder.loadTexts:
    autoscalingchangeprocessfailure.setStatus(
        "current"
    )

autoscalewrongimageid = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 183)
)
autoscalewrongimageid.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "poolName"))
)
if mibBuilder.loadTexts:
    autoscalewrongimageid.setStatus(
        "current"
    )

autoscalewrongname = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 184)
)
autoscalewrongname.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "poolName"))
)
if mibBuilder.loadTexts:
    autoscalewrongname.setStatus(
        "current"
    )

autoscalewrongsizeid = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 185)
)
autoscalewrongsizeid.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "poolName"))
)
if mibBuilder.loadTexts:
    autoscalewrongsizeid.setStatus(
        "current"
    )

logdiskoverload = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 186)
)
logdiskoverload.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    logdiskoverload.setStatus(
        "current"
    )

logdiskfull = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 187)
)
logdiskfull.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    logdiskfull.setStatus(
        "current"
    )

autoscalingresuscitatepool = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 188)
)
autoscalingresuscitatepool.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "poolName"))
)
if mibBuilder.loadTexts:
    autoscalingresuscitatepool.setStatus(
        "current"
    )

zxtmhighload = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 189)
)
zxtmhighload.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    zxtmhighload.setStatus(
        "current"
    )

glbservicedied = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 190)
)
glbservicedied.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "glbServiceName"))
)
if mibBuilder.loadTexts:
    glbservicedied.setStatus(
        "current"
    )

glbserviceok = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 191)
)
glbserviceok.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "glbServiceName"))
)
if mibBuilder.loadTexts:
    glbserviceok.setStatus(
        "current"
    )

license_rejected_unauthorized_ts = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 192)
)
license_rejected_unauthorized_ts.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "licensekeyName"))
)
if mibBuilder.loadTexts:
    license_rejected_unauthorized_ts.setStatus(
        "current"
    )

license_authorized_ts = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 193)
)
license_authorized_ts.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "licensekeyName"))
)
if mibBuilder.loadTexts:
    license_authorized_ts.setStatus(
        "current"
    )

license_rejected_authorized_ts = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 194)
)
license_rejected_authorized_ts.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "licensekeyName"))
)
if mibBuilder.loadTexts:
    license_rejected_authorized_ts.setStatus(
        "current"
    )

license_timedout_authorized_ts = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 195)
)
license_timedout_authorized_ts.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "licensekeyName"))
)
if mibBuilder.loadTexts:
    license_timedout_authorized_ts.setStatus(
        "current"
    )

license_timedout_unauthorized_ts = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 196)
)
license_timedout_unauthorized_ts.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "licensekeyName"))
)
if mibBuilder.loadTexts:
    license_timedout_unauthorized_ts.setStatus(
        "current"
    )

license_graceperiodexpired_ts = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 197)
)
license_graceperiodexpired_ts.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "licensekeyName"))
)
if mibBuilder.loadTexts:
    license_graceperiodexpired_ts.setStatus(
        "current"
    )

flipperraiseremotedropped = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 198)
)
flipperraiseremotedropped.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    flipperraiseremotedropped.setStatus(
        "current"
    )

sslrehandshakemininterval = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 199)
)
sslrehandshakemininterval.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "virtualserverName"))
)
if mibBuilder.loadTexts:
    sslrehandshakemininterval.setStatus(
        "current"
    )

sslhandshakemsgsizelimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 200)
)
sslhandshakemsgsizelimit.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "virtualserverName"))
)
if mibBuilder.loadTexts:
    sslhandshakemsgsizelimit.setStatus(
        "current"
    )

sslcrltoobig = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 201)
)
sslcrltoobig.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    sslcrltoobig.setStatus(
        "current"
    )

numpools_exceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 202)
)
numpools_exceeded.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    numpools_exceeded.setStatus(
        "current"
    )

numlocations_exceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 203)
)
numlocations_exceeded.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    numlocations_exceeded.setStatus(
        "current"
    )

numtipg_exceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 204)
)
numtipg_exceeded.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    numtipg_exceeded.setStatus(
        "current"
    )

numnodes_exceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 205)
)
numnodes_exceeded.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    numnodes_exceeded.setStatus(
        "current"
    )

ec2nosecondaryprivateip = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 206)
)
ec2nosecondaryprivateip.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    ec2nosecondaryprivateip.setStatus(
        "current"
    )

ec2vpceipassocerr = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 207)
)
ec2vpceipassocerr.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    ec2vpceipassocerr.setStatus(
        "obsolete"
    )

ec2vpciderr = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 208)
)
ec2vpciderr.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    ec2vpciderr.setStatus(
        "obsolete"
    )

license_explicitlydisabled_ts = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 209)
)
license_explicitlydisabled_ts.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "licensekeyName"))
)
if mibBuilder.loadTexts:
    license_explicitlydisabled_ts.setStatus(
        "current"
    )

rulestreamerrortoomuch = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 210)
)
rulestreamerrortoomuch.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "ruleName"))
)
if mibBuilder.loadTexts:
    rulestreamerrortoomuch.setStatus(
        "current"
    )

rulestreamerrornotenough = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 211)
)
rulestreamerrornotenough.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "ruleName"))
)
if mibBuilder.loadTexts:
    rulestreamerrornotenough.setStatus(
        "current"
    )

rulestreamerrorprocessfailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 212)
)
rulestreamerrorprocessfailure.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "ruleName"))
)
if mibBuilder.loadTexts:
    rulestreamerrorprocessfailure.setStatus(
        "current"
    )

rulestreamerrornotstarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 213)
)
rulestreamerrornotstarted.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "ruleName"))
)
if mibBuilder.loadTexts:
    rulestreamerrornotstarted.setStatus(
        "current"
    )

rulestreamerrornotfinished = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 214)
)
rulestreamerrornotfinished.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "ruleName"))
)
if mibBuilder.loadTexts:
    rulestreamerrornotfinished.setStatus(
        "current"
    )

rulestreamerrorinternal = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 215)
)
rulestreamerrorinternal.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "ruleName"))
)
if mibBuilder.loadTexts:
    rulestreamerrorinternal.setStatus(
        "current"
    )

rulestreamerrorgetresponse = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 216)
)
rulestreamerrorgetresponse.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "ruleName"))
)
if mibBuilder.loadTexts:
    rulestreamerrorgetresponse.setStatus(
        "current"
    )

rulesinvalidrequestbody = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 217)
)
rulesinvalidrequestbody.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "ruleName"),
        ("ZXTM-MIB-SMIv2", "virtualserverName"))
)
if mibBuilder.loadTexts:
    rulesinvalidrequestbody.setStatus(
        "current"
    )

serviceruleabort = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 218)
)
serviceruleabort.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "glbServiceName"),
        ("ZXTM-MIB-SMIv2", "ruleName"))
)
if mibBuilder.loadTexts:
    serviceruleabort.setStatus(
        "current"
    )

servicerulelocunknown = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 219)
)
servicerulelocunknown.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "glbServiceName"),
        ("ZXTM-MIB-SMIv2", "ruleName"))
)
if mibBuilder.loadTexts:
    servicerulelocunknown.setStatus(
        "current"
    )

servicerulelocnotconfigured = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 220)
)
servicerulelocnotconfigured.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "glbServiceName"),
        ("ZXTM-MIB-SMIv2", "ruleName"))
)
if mibBuilder.loadTexts:
    servicerulelocnotconfigured.setStatus(
        "current"
    )

servicerulelocdead = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 221)
)
servicerulelocdead.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "glbServiceName"),
        ("ZXTM-MIB-SMIv2", "ruleName"))
)
if mibBuilder.loadTexts:
    servicerulelocdead.setStatus(
        "current"
    )

aptimizeuseunknownprofile = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 222)
)
aptimizeuseunknownprofile.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "ruleName"))
)
if mibBuilder.loadTexts:
    aptimizeuseunknownprofile.setStatus(
        "current"
    )

aptimizedisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 223)
)
aptimizedisabled.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "ruleName"))
)
if mibBuilder.loadTexts:
    aptimizedisabled.setStatus(
        "current"
    )

aptimizeuseunknownscope = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 224)
)
aptimizeuseunknownscope.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "ruleName"))
)
if mibBuilder.loadTexts:
    aptimizeuseunknownscope.setStatus(
        "current"
    )

childcommsfail = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 225)
)
childcommsfail.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    childcommsfail.setStatus(
        "current"
    )

childhung = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 226)
)
childhung.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    childhung.setStatus(
        "deprecated"
    )

childkilled = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 227)
)
childkilled.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    childkilled.setStatus(
        "deprecated"
    )

datalocalstorefull = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 228)
)
datalocalstorefull.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "ruleName"))
)
if mibBuilder.loadTexts:
    datalocalstorefull.setStatus(
        "current"
    )

fipsfailinit = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 229)
)
fipsfailinit.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    fipsfailinit.setStatus(
        "current"
    )

fipsfailops = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 230)
)
fipsfailops.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    fipsfailops.setStatus(
        "current"
    )

clocknotmonotonic = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 231)
)
clocknotmonotonic.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    clocknotmonotonic.setStatus(
        "current"
    )

clockjump = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 232)
)
clockjump.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    clockjump.setStatus(
        "current"
    )

rebootrequired = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 233)
)
rebootrequired.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    rebootrequired.setStatus(
        "obsolete"
    )

ocspstaplingfail = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 234)
)
ocspstaplingfail.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    ocspstaplingfail.setStatus(
        "current"
    )

ocspstaplingnomem = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 235)
)
ocspstaplingnomem.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    ocspstaplingnomem.setStatus(
        "current"
    )

appliance = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 236)
)
appliance.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    appliance.setStatus(
        "current"
    )

pingsendfail = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 237)
)
pingsendfail.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    pingsendfail.setStatus(
        "current"
    )

autonodenopublicip = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 238)
)
autonodenopublicip.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "poolName"))
)
if mibBuilder.loadTexts:
    autonodenopublicip.setStatus(
        "current"
    )

ocspstaplingrevoked = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 239)
)
ocspstaplingrevoked.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    ocspstaplingrevoked.setStatus(
        "current"
    )

ocspstaplingunknown = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 240)
)
ocspstaplingunknown.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    ocspstaplingunknown.setStatus(
        "current"
    )

ocspstaplingunrevoked = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 241)
)
ocspstaplingunrevoked.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    ocspstaplingunrevoked.setStatus(
        "current"
    )

ruleoverrun = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 242)
)
ruleoverrun.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "ruleName"))
)
if mibBuilder.loadTexts:
    ruleoverrun.setStatus(
        "current"
    )

appfirewallcontrolstarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 243)
)
appfirewallcontrolstarted.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    appfirewallcontrolstarted.setStatus(
        "current"
    )

autonoderemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 244)
)
autonoderemoved.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "poolName"))
)
if mibBuilder.loadTexts:
    autonoderemoved.setStatus(
        "current"
    )

routingswoperational = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 245)
)
routingswoperational.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    routingswoperational.setStatus(
        "current"
    )

routingswfailurelimitreached = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 246)
)
routingswfailurelimitreached.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    routingswfailurelimitreached.setStatus(
        "current"
    )

routingswfailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 247)
)
routingswfailed.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    routingswfailed.setStatus(
        "current"
    )

routingswstartfailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 248)
)
routingswstartfailed.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    routingswstartfailed.setStatus(
        "current"
    )

appfirewallcontrolstopped = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 249)
)
appfirewallcontrolstopped.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    appfirewallcontrolstopped.setStatus(
        "current"
    )

appfirewallcontrolrestarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 250)
)
appfirewallcontrolrestarted.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    appfirewallcontrolrestarted.setStatus(
        "current"
    )

appfirewallcontroltimeout = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 251)
)
appfirewallcontroltimeout.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    appfirewallcontroltimeout.setStatus(
        "current"
    )

appfirewallcontrolerror = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 252)
)
appfirewallcontrolerror.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    appfirewallcontrolerror.setStatus(
        "current"
    )

ospfneighborsok = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 253)
)
ospfneighborsok.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    ospfneighborsok.setStatus(
        "current"
    )

ospfneighborsdegraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 254)
)
ospfneighborsdegraded.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    ospfneighborsdegraded.setStatus(
        "current"
    )

ospfneighborsfailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 255)
)
ospfneighborsfailed.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    ospfneighborsfailed.setStatus(
        "current"
    )

nameserverunavailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 256)
)
nameserverunavailable.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "poolName"))
)
if mibBuilder.loadTexts:
    nameserverunavailable.setStatus(
        "current"
    )

nameserveravailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 257)
)
nameserveravailable.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "poolName"))
)
if mibBuilder.loadTexts:
    nameserveravailable.setStatus(
        "current"
    )

autoscaleresolvefailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 258)
)
autoscaleresolvefailure.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "poolName"))
)
if mibBuilder.loadTexts:
    autoscaleresolvefailure.setStatus(
        "current"
    )

glbtoomanylocations = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 259)
)
glbtoomanylocations.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "glbServiceName"))
)
if mibBuilder.loadTexts:
    glbtoomanylocations.setStatus(
        "current"
    )

dnszonevalidate = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 260)
)
dnszonevalidate.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    dnszonevalidate.setStatus(
        "current"
    )

dnszonecreaterecord = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 261)
)
dnszonecreaterecord.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    dnszonecreaterecord.setStatus(
        "current"
    )

dnszoneparsechild = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 262)
)
dnszoneparsechild.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    dnszoneparsechild.setStatus(
        "obsolete"
    )

dnserroraddzone = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 263)
)
dnserroraddzone.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "confName"),
        ("ZXTM-MIB-SMIv2", "domainName"))
)
if mibBuilder.loadTexts:
    dnserroraddzone.setStatus(
        "current"
    )

dnsaddzone = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 264)
)
dnsaddzone.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "confName"),
        ("ZXTM-MIB-SMIv2", "domainName"))
)
if mibBuilder.loadTexts:
    dnsaddzone.setStatus(
        "current"
    )

dnszoneparse = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 265)
)
dnszoneparse.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    dnszoneparse.setStatus(
        "current"
    )

ec2dataretrievalfailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 266)
)
ec2dataretrievalfailed.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    ec2dataretrievalfailed.setStatus(
        "current"
    )

ec2dataretrievalsuccessful = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 267)
)
ec2dataretrievalsuccessful.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    ec2dataretrievalsuccessful.setStatus(
        "current"
    )

dnszonedelete = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 268)
)
dnszonedelete.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "confName"),
        ("ZXTM-MIB-SMIv2", "domainName"))
)
if mibBuilder.loadTexts:
    dnszonedelete.setStatus(
        "current"
    )

dnserrordeletezone = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 269)
)
dnserrordeletezone.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "confName"),
        ("ZXTM-MIB-SMIv2", "domainName"))
)
if mibBuilder.loadTexts:
    dnserrordeletezone.setStatus(
        "current"
    )

dnssecexpired = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 270)
)
dnssecexpired.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "confName"),
        ("ZXTM-MIB-SMIv2", "domainName"))
)
if mibBuilder.loadTexts:
    dnssecexpired.setStatus(
        "current"
    )

dnssecexpires = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 271)
)
dnssecexpires.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "confName"),
        ("ZXTM-MIB-SMIv2", "domainName"))
)
if mibBuilder.loadTexts:
    dnssecexpires.setStatus(
        "current"
    )

glbactivedcmismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 272)
)
glbactivedcmismatch.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    glbactivedcmismatch.setStatus(
        "current"
    )

locationdraining = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 273)
)
locationdraining.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "locationName"),
        ("ZXTM-MIB-SMIv2", "glbServiceName"))
)
if mibBuilder.loadTexts:
    locationdraining.setStatus(
        "current"
    )

locationnotdraining = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 274)
)
locationnotdraining.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "locationName"),
        ("ZXTM-MIB-SMIv2", "glbServiceName"))
)
if mibBuilder.loadTexts:
    locationnotdraining.setStatus(
        "current"
    )

locationdisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 275)
)
locationdisabled.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "locationName"),
        ("ZXTM-MIB-SMIv2", "glbServiceName"))
)
if mibBuilder.loadTexts:
    locationdisabled.setStatus(
        "current"
    )

locationenabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 276)
)
locationenabled.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "locationName"),
        ("ZXTM-MIB-SMIv2", "glbServiceName"))
)
if mibBuilder.loadTexts:
    locationenabled.setStatus(
        "current"
    )

locationunavailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 277)
)
locationunavailable.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "locationName"),
        ("ZXTM-MIB-SMIv2", "glbServiceName"))
)
if mibBuilder.loadTexts:
    locationunavailable.setStatus(
        "current"
    )

locationavailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 278)
)
locationavailable.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "locationName"),
        ("ZXTM-MIB-SMIv2", "glbServiceName"))
)
if mibBuilder.loadTexts:
    locationavailable.setStatus(
        "current"
    )

glbmanualfailback = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 279)
)
glbmanualfailback.setObjects(
      *(("ZXTM-MIB-SMIv2", "fullLogLine"),
        ("ZXTM-MIB-SMIv2", "glbServiceName"))
)
if mibBuilder.loadTexts:
    glbmanualfailback.setStatus(
        "current"
    )

nodedrainingtodelete = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 280)
)
nodedrainingtodelete.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    nodedrainingtodelete.setStatus(
        "current"
    )

nodedrainingtodeletetimeout = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 281)
)
nodedrainingtodeletetimeout.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    nodedrainingtodeletetimeout.setStatus(
        "current"
    )

bgpneighborsok = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 282)
)
bgpneighborsok.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    bgpneighborsok.setStatus(
        "current"
    )

bgpneighborsdegraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 283)
)
bgpneighborsdegraded.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    bgpneighborsdegraded.setStatus(
        "current"
    )

bgpneighborsfailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 284)
)
bgpneighborsfailed.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    bgpneighborsfailed.setStatus(
        "current"
    )

bgpnoneighbors = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 285)
)
bgpnoneighbors.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    bgpnoneighbors.setStatus(
        "current"
    )

zxtmcpustarvation = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 286)
)
zxtmcpustarvation.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    zxtmcpustarvation.setStatus(
        "current"
    )

ec2initialized = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 287)
)
ec2initialized.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    ec2initialized.setStatus(
        "current"
    )

upgradereboot = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 288)
)
upgradereboot.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    upgradereboot.setStatus(
        "current"
    )

sysctlreboot = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 289)
)
sysctlreboot.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    sysctlreboot.setStatus(
        "current"
    )

upgraderestart = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 290)
)
upgraderestart.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    upgraderestart.setStatus(
        "current"
    )

unspecifiedreboot = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 291)
)
unspecifiedreboot.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    unspecifiedreboot.setStatus(
        "current"
    )

gcedataretrievalfailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 292)
)
gcedataretrievalfailed.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    gcedataretrievalfailed.setStatus(
        "current"
    )

gcedataretrievalsuccessful = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 293)
)
gcedataretrievalsuccessful.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    gcedataretrievalsuccessful.setStatus(
        "current"
    )

autofailbacktimerstarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 294)
)
autofailbacktimerstarted.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    autofailbacktimerstarted.setStatus(
        "current"
    )

autofailbacktimerstopped = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 295)
)
autofailbacktimerstopped.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    autofailbacktimerstopped.setStatus(
        "current"
    )

autofailbackafterdelay = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 296)
)
autofailbackafterdelay.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    autofailbackafterdelay.setStatus(
        "current"
    )

autofailbacktimercancelled = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 297)
)
autofailbacktimercancelled.setObjects(
    ("ZXTM-MIB-SMIv2", "fullLogLine")
)
if mibBuilder.loadTexts:
    autofailbacktimercancelled.setStatus(
        "current"
    )


# Notifications groups

notificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 29, 4)
)
notificationGroup.setObjects(
      *(("ZXTM-MIB-SMIv2", "testaction"),
        ("ZXTM-MIB-SMIv2", "running"),
        ("ZXTM-MIB-SMIv2", "fewfreefds"),
        ("ZXTM-MIB-SMIv2", "restartrequired"),
        ("ZXTM-MIB-SMIv2", "upgradereboot"),
        ("ZXTM-MIB-SMIv2", "sysctlreboot"),
        ("ZXTM-MIB-SMIv2", "upgraderestart"),
        ("ZXTM-MIB-SMIv2", "unspecifiedreboot"),
        ("ZXTM-MIB-SMIv2", "timemovedback"),
        ("ZXTM-MIB-SMIv2", "sslfail"),
        ("ZXTM-MIB-SMIv2", "appliance"),
        ("ZXTM-MIB-SMIv2", "zxtmswerror"),
        ("ZXTM-MIB-SMIv2", "customevent"),
        ("ZXTM-MIB-SMIv2", "versionmismatch"),
        ("ZXTM-MIB-SMIv2", "autherror"),
        ("ZXTM-MIB-SMIv2", "machineok"),
        ("ZXTM-MIB-SMIv2", "machinetimeout"),
        ("ZXTM-MIB-SMIv2", "machinefail"),
        ("ZXTM-MIB-SMIv2", "allmachinesok"),
        ("ZXTM-MIB-SMIv2", "flipperbackendsworking"),
        ("ZXTM-MIB-SMIv2", "flipperfrontendsworking"),
        ("ZXTM-MIB-SMIv2", "pingbackendfail"),
        ("ZXTM-MIB-SMIv2", "pingfrontendfail"),
        ("ZXTM-MIB-SMIv2", "pinggwfail"),
        ("ZXTM-MIB-SMIv2", "statebaddata"),
        ("ZXTM-MIB-SMIv2", "stateconnfail"),
        ("ZXTM-MIB-SMIv2", "stateok"),
        ("ZXTM-MIB-SMIv2", "statereadfail"),
        ("ZXTM-MIB-SMIv2", "statetimeout"),
        ("ZXTM-MIB-SMIv2", "stateunexpected"),
        ("ZXTM-MIB-SMIv2", "statewritefail"),
        ("ZXTM-MIB-SMIv2", "activatealldead"),
        ("ZXTM-MIB-SMIv2", "machinerecovered"),
        ("ZXTM-MIB-SMIv2", "flipperrecovered"),
        ("ZXTM-MIB-SMIv2", "activatedautomatically"),
        ("ZXTM-MIB-SMIv2", "zclustermoderr"),
        ("ZXTM-MIB-SMIv2", "ec2flipperraiselocalworking"),
        ("ZXTM-MIB-SMIv2", "ec2flipperraiseothersdead"),
        ("ZXTM-MIB-SMIv2", "ec2iperr"),
        ("ZXTM-MIB-SMIv2", "dropec2ipwarn"),
        ("ZXTM-MIB-SMIv2", "ec2nopublicip"),
        ("ZXTM-MIB-SMIv2", "ec2nosecondaryprivateip"),
        ("ZXTM-MIB-SMIv2", "ec2dataretrievalfailed"),
        ("ZXTM-MIB-SMIv2", "ec2dataretrievalsuccessful"),
        ("ZXTM-MIB-SMIv2", "ec2initialized"),
        ("ZXTM-MIB-SMIv2", "gcedataretrievalfailed"),
        ("ZXTM-MIB-SMIv2", "gcedataretrievalsuccessful"),
        ("ZXTM-MIB-SMIv2", "multihostload"),
        ("ZXTM-MIB-SMIv2", "sslhwfail"),
        ("ZXTM-MIB-SMIv2", "sslhwrestart"),
        ("ZXTM-MIB-SMIv2", "sslhwstart"),
        ("ZXTM-MIB-SMIv2", "confdel"),
        ("ZXTM-MIB-SMIv2", "confmod"),
        ("ZXTM-MIB-SMIv2", "confadd"),
        ("ZXTM-MIB-SMIv2", "confok"),
        ("ZXTM-MIB-SMIv2", "confreptimeout"),
        ("ZXTM-MIB-SMIv2", "confrepfailed"),
        ("ZXTM-MIB-SMIv2", "javadied"),
        ("ZXTM-MIB-SMIv2", "javastop"),
        ("ZXTM-MIB-SMIv2", "javastartfail"),
        ("ZXTM-MIB-SMIv2", "javaterminatefail"),
        ("ZXTM-MIB-SMIv2", "javanotfound"),
        ("ZXTM-MIB-SMIv2", "javastarted"),
        ("ZXTM-MIB-SMIv2", "servleterror"),
        ("ZXTM-MIB-SMIv2", "monitorfail"),
        ("ZXTM-MIB-SMIv2", "monitorok"),
        ("ZXTM-MIB-SMIv2", "rulexmlerr"),
        ("ZXTM-MIB-SMIv2", "pooluseunknown"),
        ("ZXTM-MIB-SMIv2", "ruleabort"),
        ("ZXTM-MIB-SMIv2", "rulebufferlarge"),
        ("ZXTM-MIB-SMIv2", "rulebodycomperror"),
        ("ZXTM-MIB-SMIv2", "forwardproxybadhost"),
        ("ZXTM-MIB-SMIv2", "invalidemit"),
        ("ZXTM-MIB-SMIv2", "rulenopersistence"),
        ("ZXTM-MIB-SMIv2", "rulelogmsginfo"),
        ("ZXTM-MIB-SMIv2", "rulelogmsgwarn"),
        ("ZXTM-MIB-SMIv2", "rulelogmsgserious"),
        ("ZXTM-MIB-SMIv2", "norate"),
        ("ZXTM-MIB-SMIv2", "poolactivenodesunknown"),
        ("ZXTM-MIB-SMIv2", "datastorefull"),
        ("ZXTM-MIB-SMIv2", "ruleoverrun"),
        ("ZXTM-MIB-SMIv2", "rulestreamerrortoomuch"),
        ("ZXTM-MIB-SMIv2", "rulestreamerrornotenough"),
        ("ZXTM-MIB-SMIv2", "rulestreamerrorprocessfailure"),
        ("ZXTM-MIB-SMIv2", "rulestreamerrornotstarted"),
        ("ZXTM-MIB-SMIv2", "rulestreamerrornotfinished"),
        ("ZXTM-MIB-SMIv2", "rulestreamerrorinternal"),
        ("ZXTM-MIB-SMIv2", "rulestreamerrorgetresponse"),
        ("ZXTM-MIB-SMIv2", "rulesinvalidrequestbody"),
        ("ZXTM-MIB-SMIv2", "serviceruleabort"),
        ("ZXTM-MIB-SMIv2", "servicerulelocunknown"),
        ("ZXTM-MIB-SMIv2", "servicerulelocnotconfigured"),
        ("ZXTM-MIB-SMIv2", "servicerulelocdead"),
        ("ZXTM-MIB-SMIv2", "expired"),
        ("ZXTM-MIB-SMIv2", "licensecorrupt"),
        ("ZXTM-MIB-SMIv2", "expiresoon"),
        ("ZXTM-MIB-SMIv2", "usinglicense"),
        ("ZXTM-MIB-SMIv2", "licenseclustertoobig"),
        ("ZXTM-MIB-SMIv2", "unlicensed"),
        ("ZXTM-MIB-SMIv2", "usingdevlicense"),
        ("ZXTM-MIB-SMIv2", "morememallowed"),
        ("ZXTM-MIB-SMIv2", "lessmemallowed"),
        ("ZXTM-MIB-SMIv2", "cachesizereduced"),
        ("ZXTM-MIB-SMIv2", "tpslimited"),
        ("ZXTM-MIB-SMIv2", "ssltpslimited"),
        ("ZXTM-MIB-SMIv2", "bwlimited"),
        ("ZXTM-MIB-SMIv2", "licensetoomanylocations"),
        ("ZXTM-MIB-SMIv2", "autoscalinglicenseerror"),
        ("ZXTM-MIB-SMIv2", "autoscalinglicenseenabled"),
        ("ZXTM-MIB-SMIv2", "autoscalinglicensedisabled"),
        ("ZXTM-MIB-SMIv2", "analyticslicenseenabled"),
        ("ZXTM-MIB-SMIv2", "analyticslicensedisabled"),
        ("ZXTM-MIB-SMIv2", "poolnonodes"),
        ("ZXTM-MIB-SMIv2", "poolok"),
        ("ZXTM-MIB-SMIv2", "pooldied"),
        ("ZXTM-MIB-SMIv2", "noderesolvefailure"),
        ("ZXTM-MIB-SMIv2", "noderesolvemultiple"),
        ("ZXTM-MIB-SMIv2", "nodeworking"),
        ("ZXTM-MIB-SMIv2", "nostarttls"),
        ("ZXTM-MIB-SMIv2", "nodefail"),
        ("ZXTM-MIB-SMIv2", "starttlsinvalid"),
        ("ZXTM-MIB-SMIv2", "ehloinvalid"),
        ("ZXTM-MIB-SMIv2", "usedcredsdeleted"),
        ("ZXTM-MIB-SMIv2", "autoscalestatusupdateerror"),
        ("ZXTM-MIB-SMIv2", "autoscaleresponseparseerror"),
        ("ZXTM-MIB-SMIv2", "autoscalingchangeprocessfailure"),
        ("ZXTM-MIB-SMIv2", "autoscalewrongimageid"),
        ("ZXTM-MIB-SMIv2", "autoscalewrongname"),
        ("ZXTM-MIB-SMIv2", "autoscalewrongsizeid"),
        ("ZXTM-MIB-SMIv2", "apistatusprocesshanging"),
        ("ZXTM-MIB-SMIv2", "autonodedestructioncomplete"),
        ("ZXTM-MIB-SMIv2", "autonodeexisted"),
        ("ZXTM-MIB-SMIv2", "autoscaledpooltoosmall"),
        ("ZXTM-MIB-SMIv2", "autoscaleinvalidargforcreatenode"),
        ("ZXTM-MIB-SMIv2", "autonodedisappeared"),
        ("ZXTM-MIB-SMIv2", "autonoderemoved"),
        ("ZXTM-MIB-SMIv2", "nameserverunavailable"),
        ("ZXTM-MIB-SMIv2", "nameserveravailable"),
        ("ZXTM-MIB-SMIv2", "autoscaleresolvefailure"),
        ("ZXTM-MIB-SMIv2", "autoscaledpoolrefractory"),
        ("ZXTM-MIB-SMIv2", "cannotshrinkemptypool"),
        ("ZXTM-MIB-SMIv2", "autoscalinghysteresiscantgrow"),
        ("ZXTM-MIB-SMIv2", "autonodecreationcomplete"),
        ("ZXTM-MIB-SMIv2", "autonodestatuschange"),
        ("ZXTM-MIB-SMIv2", "autoscalinghysteresiscantshrink"),
        ("ZXTM-MIB-SMIv2", "autoscalingpoolstatechange"),
        ("ZXTM-MIB-SMIv2", "autonodedestroyed"),
        ("ZXTM-MIB-SMIv2", "autonodecreationstarted"),
        ("ZXTM-MIB-SMIv2", "autoscaleinvalidargfordeletenode"),
        ("ZXTM-MIB-SMIv2", "autoscalinghitroof"),
        ("ZXTM-MIB-SMIv2", "autoscalinghitfloor"),
        ("ZXTM-MIB-SMIv2", "apichangeprocesshanging"),
        ("ZXTM-MIB-SMIv2", "autoscaledpooltoobig"),
        ("ZXTM-MIB-SMIv2", "autoscalingprocesstimedout"),
        ("ZXTM-MIB-SMIv2", "autoscalingdisabled"),
        ("ZXTM-MIB-SMIv2", "autoscalednodecontested"),
        ("ZXTM-MIB-SMIv2", "autoscalepoolconfupdate"),
        ("ZXTM-MIB-SMIv2", "flipperraiselocalworking"),
        ("ZXTM-MIB-SMIv2", "flipperraiseothersdead"),
        ("ZXTM-MIB-SMIv2", "flipperraiseosdrop"),
        ("ZXTM-MIB-SMIv2", "dropipinfo"),
        ("ZXTM-MIB-SMIv2", "dropipwarn"),
        ("ZXTM-MIB-SMIv2", "flipperdadreraise"),
        ("ZXTM-MIB-SMIv2", "flipperipexists"),
        ("ZXTM-MIB-SMIv2", "triggersummary"),
        ("ZXTM-MIB-SMIv2", "slmclasslimitexceeded"),
        ("ZXTM-MIB-SMIv2", "slmrecoveredwarn"),
        ("ZXTM-MIB-SMIv2", "slmrecoveredserious"),
        ("ZXTM-MIB-SMIv2", "slmfallenbelowwarn"),
        ("ZXTM-MIB-SMIv2", "slmfallenbelowserious"),
        ("ZXTM-MIB-SMIv2", "vscrloutofdate"),
        ("ZXTM-MIB-SMIv2", "vsstart"),
        ("ZXTM-MIB-SMIv2", "vsstop"),
        ("ZXTM-MIB-SMIv2", "privkeyok"),
        ("ZXTM-MIB-SMIv2", "ssldrop"),
        ("ZXTM-MIB-SMIv2", "vslogwritefail"),
        ("ZXTM-MIB-SMIv2", "vssslcertexpired"),
        ("ZXTM-MIB-SMIv2", "vssslcerttoexpire"),
        ("ZXTM-MIB-SMIv2", "vscacertexpired"),
        ("ZXTM-MIB-SMIv2", "vscacerttoexpire"),
        ("ZXTM-MIB-SMIv2", "glbmissingips"),
        ("ZXTM-MIB-SMIv2", "glbdeadlocmissingips"),
        ("ZXTM-MIB-SMIv2", "glbnolocations"),
        ("ZXTM-MIB-SMIv2", "locationmonitorok"),
        ("ZXTM-MIB-SMIv2", "locationmonitorfail"),
        ("ZXTM-MIB-SMIv2", "locationok"),
        ("ZXTM-MIB-SMIv2", "locationfail"),
        ("ZXTM-MIB-SMIv2", "locationsoapok"),
        ("ZXTM-MIB-SMIv2", "locationsoapfail"),
        ("ZXTM-MIB-SMIv2", "glbnewmaster"),
        ("ZXTM-MIB-SMIv2", "glblogwritefail"),
        ("ZXTM-MIB-SMIv2", "glbfailalter"),
        ("ZXTM-MIB-SMIv2", "glbservicedied"),
        ("ZXTM-MIB-SMIv2", "glbserviceok"),
        ("ZXTM-MIB-SMIv2", "locmovemachine"),
        ("ZXTM-MIB-SMIv2", "locempty"),
        ("ZXTM-MIB-SMIv2", "glbtoomanylocations"),
        ("ZXTM-MIB-SMIv2", "dnszonevalidate"),
        ("ZXTM-MIB-SMIv2", "dnszonecreaterecord"),
        ("ZXTM-MIB-SMIv2", "dnserroraddzone"),
        ("ZXTM-MIB-SMIv2", "dnsaddzone"),
        ("ZXTM-MIB-SMIv2", "dnszoneparse"),
        ("ZXTM-MIB-SMIv2", "dnszonedelete"),
        ("ZXTM-MIB-SMIv2", "dnserrordeletezone"),
        ("ZXTM-MIB-SMIv2", "maxclientbufferdrop"),
        ("ZXTM-MIB-SMIv2", "respcompfail"),
        ("ZXTM-MIB-SMIv2", "responsetoolarge"),
        ("ZXTM-MIB-SMIv2", "sipstreamnoports"),
        ("ZXTM-MIB-SMIv2", "rtspstreamnoports"),
        ("ZXTM-MIB-SMIv2", "geodataloadfail"),
        ("ZXTM-MIB-SMIv2", "poolpersistencemismatch"),
        ("ZXTM-MIB-SMIv2", "connerror"),
        ("ZXTM-MIB-SMIv2", "connfail"),
        ("ZXTM-MIB-SMIv2", "badcontentlen"),
        ("ZXTM-MIB-SMIv2", "logfiledeleted"),
        ("ZXTM-MIB-SMIv2", "license_graceperiodexpired"),
        ("ZXTM-MIB-SMIv2", "license_authorized"),
        ("ZXTM-MIB-SMIv2", "license_rejected_authorized"),
        ("ZXTM-MIB-SMIv2", "license_rejected_unauthorized"),
        ("ZXTM-MIB-SMIv2", "license_timedout_authorized"),
        ("ZXTM-MIB-SMIv2", "license_timedout_unauthorized"),
        ("ZXTM-MIB-SMIv2", "license_unauthorized"),
        ("ZXTM-MIB-SMIv2", "logdiskoverload"),
        ("ZXTM-MIB-SMIv2", "logdiskfull"),
        ("ZXTM-MIB-SMIv2", "aptimizeuseunknownprofile"),
        ("ZXTM-MIB-SMIv2", "aptimizedisabled"),
        ("ZXTM-MIB-SMIv2", "aptimizeuseunknownscope"),
        ("ZXTM-MIB-SMIv2", "sslhandshakemsgsizelimit"),
        ("ZXTM-MIB-SMIv2", "sslcrltoobig"),
        ("ZXTM-MIB-SMIv2", "childcommsfail"),
        ("ZXTM-MIB-SMIv2", "sslrehandshakemininterval"),
        ("ZXTM-MIB-SMIv2", "datalocalstorefull"),
        ("ZXTM-MIB-SMIv2", "fipsfailinit"),
        ("ZXTM-MIB-SMIv2", "fipsfailops"),
        ("ZXTM-MIB-SMIv2", "ocspstaplingfail"),
        ("ZXTM-MIB-SMIv2", "ocspstaplingnomem"),
        ("ZXTM-MIB-SMIv2", "ocspstaplingrevoked"),
        ("ZXTM-MIB-SMIv2", "ocspstaplingunknown"),
        ("ZXTM-MIB-SMIv2", "ocspstaplingunrevoked"),
        ("ZXTM-MIB-SMIv2", "flipperraiseremotedropped"),
        ("ZXTM-MIB-SMIv2", "autofailbacktimerstarted"),
        ("ZXTM-MIB-SMIv2", "autofailbacktimerstopped"),
        ("ZXTM-MIB-SMIv2", "autofailbackafterdelay"),
        ("ZXTM-MIB-SMIv2", "autofailbacktimercancelled"),
        ("ZXTM-MIB-SMIv2", "autoscalingresuscitatepool"),
        ("ZXTM-MIB-SMIv2", "license_rejected_unauthorized_ts"),
        ("ZXTM-MIB-SMIv2", "license_authorized_ts"),
        ("ZXTM-MIB-SMIv2", "license_rejected_authorized_ts"),
        ("ZXTM-MIB-SMIv2", "license_timedout_authorized_ts"),
        ("ZXTM-MIB-SMIv2", "license_timedout_unauthorized_ts"),
        ("ZXTM-MIB-SMIv2", "license_graceperiodexpired_ts"),
        ("ZXTM-MIB-SMIv2", "license_explicitlydisabled_ts"),
        ("ZXTM-MIB-SMIv2", "numnodes_exceeded"),
        ("ZXTM-MIB-SMIv2", "numpools_exceeded"),
        ("ZXTM-MIB-SMIv2", "numlocations_exceeded"),
        ("ZXTM-MIB-SMIv2", "numtipg_exceeded"),
        ("ZXTM-MIB-SMIv2", "zxtmhighload"),
        ("ZXTM-MIB-SMIv2", "clocknotmonotonic"),
        ("ZXTM-MIB-SMIv2", "clockjump"),
        ("ZXTM-MIB-SMIv2", "pingsendfail"),
        ("ZXTM-MIB-SMIv2", "autonodenopublicip"),
        ("ZXTM-MIB-SMIv2", "routingswoperational"),
        ("ZXTM-MIB-SMIv2", "routingswfailurelimitreached"),
        ("ZXTM-MIB-SMIv2", "routingswfailed"),
        ("ZXTM-MIB-SMIv2", "routingswstartfailed"),
        ("ZXTM-MIB-SMIv2", "appfirewallcontrolstarted"),
        ("ZXTM-MIB-SMIv2", "appfirewallcontrolstopped"),
        ("ZXTM-MIB-SMIv2", "appfirewallcontrolrestarted"),
        ("ZXTM-MIB-SMIv2", "appfirewallcontroltimeout"),
        ("ZXTM-MIB-SMIv2", "appfirewallcontrolerror"),
        ("ZXTM-MIB-SMIv2", "ospfneighborsok"),
        ("ZXTM-MIB-SMIv2", "ospfneighborsdegraded"),
        ("ZXTM-MIB-SMIv2", "ospfneighborsfailed"),
        ("ZXTM-MIB-SMIv2", "bgpneighborsok"),
        ("ZXTM-MIB-SMIv2", "bgpneighborsdegraded"),
        ("ZXTM-MIB-SMIv2", "bgpneighborsfailed"),
        ("ZXTM-MIB-SMIv2", "bgpnoneighbors"),
        ("ZXTM-MIB-SMIv2", "dnssecexpired"),
        ("ZXTM-MIB-SMIv2", "dnssecexpires"),
        ("ZXTM-MIB-SMIv2", "glbactivedcmismatch"),
        ("ZXTM-MIB-SMIv2", "locationdraining"),
        ("ZXTM-MIB-SMIv2", "locationnotdraining"),
        ("ZXTM-MIB-SMIv2", "locationdisabled"),
        ("ZXTM-MIB-SMIv2", "locationenabled"),
        ("ZXTM-MIB-SMIv2", "locationunavailable"),
        ("ZXTM-MIB-SMIv2", "locationavailable"),
        ("ZXTM-MIB-SMIv2", "glbmanualfailback"),
        ("ZXTM-MIB-SMIv2", "nodedrainingtodelete"),
        ("ZXTM-MIB-SMIv2", "nodedrainingtodeletetimeout"),
        ("ZXTM-MIB-SMIv2", "zxtmcpustarvation"))
)
if mibBuilder.loadTexts:
    notificationGroup.setStatus(
        "current"
    )

obsoleteNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 29, 5)
)
obsoleteNotificationGroup.setObjects(
      *(("ZXTM-MIB-SMIv2", "ec2vpceipassocerr"),
        ("ZXTM-MIB-SMIv2", "ec2vpciderr"),
        ("ZXTM-MIB-SMIv2", "rebootrequired"),
        ("ZXTM-MIB-SMIv2", "dnszoneparsechild"))
)
if mibBuilder.loadTexts:
    obsoleteNotificationGroup.setStatus(
        "obsolete"
    )

deprecatedNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 29, 6)
)
deprecatedNotificationGroup.setObjects(
      *(("ZXTM-MIB-SMIv2", "hardware"),
        ("ZXTM-MIB-SMIv2", "childhung"),
        ("ZXTM-MIB-SMIv2", "childkilled"))
)
if mibBuilder.loadTexts:
    deprecatedNotificationGroup.setStatus(
        "deprecated"
    )


# Agent capabilities


# Module compliance

compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 30, 1)
)
if mibBuilder.loadTexts:
    compliance.setStatus(
        "current"
    )

deprecatedCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 30, 2)
)
if mibBuilder.loadTexts:
    deprecatedCompliance.setStatus(
        "deprecated"
    )

obsoleteCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 30, 3)
)
if mibBuilder.loadTexts:
    obsoleteCompliance.setStatus(
        "obsolete"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZXTM-MIB-SMIv2",
    **{"zeus": zeus,
       "products": products,
       "zxtm": zxtm,
       "globals": globals,
       "version": version,
       "numberChildProcesses": numberChildProcesses,
       "upTime": upTime,
       "timeLastConfigUpdate": timeLastConfigUpdate,
       "totalBytesInLo": totalBytesInLo,
       "totalBytesInHi": totalBytesInHi,
       "totalBytesOutLo": totalBytesOutLo,
       "totalBytesOutHi": totalBytesOutHi,
       "totalCurrentConn": totalCurrentConn,
       "totalConn": totalConn,
       "numberDNSARequests": numberDNSARequests,
       "numberDNSACacheHits": numberDNSACacheHits,
       "numberDNSPTRRequests": numberDNSPTRRequests,
       "numberDNSPTRCacheHits": numberDNSPTRCacheHits,
       "numberSNMPUnauthorisedRequests": numberSNMPUnauthorisedRequests,
       "numberSNMPBadRequests": numberSNMPBadRequests,
       "numberSNMPGetRequests": numberSNMPGetRequests,
       "numberSNMPGetNextRequests": numberSNMPGetNextRequests,
       "sslCipherEncrypts": sslCipherEncrypts,
       "sslCipherDecrypts": sslCipherDecrypts,
       "sslCipherRC4Encrypts": sslCipherRC4Encrypts,
       "sslCipherRC4Decrypts": sslCipherRC4Decrypts,
       "sslCipherDESEncrypts": sslCipherDESEncrypts,
       "sslCipherDESDecrypts": sslCipherDESDecrypts,
       "sslCipher3DESEncrypts": sslCipher3DESEncrypts,
       "sslCipher3DESDecrypts": sslCipher3DESDecrypts,
       "sslCipherAESEncrypts": sslCipherAESEncrypts,
       "sslCipherAESDecrypts": sslCipherAESDecrypts,
       "sslCipherRSAEncrypts": sslCipherRSAEncrypts,
       "sslCipherRSADecrypts": sslCipherRSADecrypts,
       "sslCipherRSADecryptsExternal": sslCipherRSADecryptsExternal,
       "sslHandshakeSSLv2": sslHandshakeSSLv2,
       "sslHandshakeSSLv3": sslHandshakeSSLv3,
       "sslHandshakeTLSv1": sslHandshakeTLSv1,
       "sslClientCertNotSent": sslClientCertNotSent,
       "sslClientCertInvalid": sslClientCertInvalid,
       "sslClientCertExpired": sslClientCertExpired,
       "sslClientCertRevoked": sslClientCertRevoked,
       "sslSessionIDMemCacheHit": sslSessionIDMemCacheHit,
       "sslSessionIDMemCacheMiss": sslSessionIDMemCacheMiss,
       "sslSessionIDDiskCacheHit": sslSessionIDDiskCacheHit,
       "sslSessionIDDiskCacheMiss": sslSessionIDDiskCacheMiss,
       "sslHandshakeTLSv11": sslHandshakeTLSv11,
       "sslConnections": sslConnections,
       "sysCPUIdlePercent": sysCPUIdlePercent,
       "sysCPUBusyPercent": sysCPUBusyPercent,
       "sysCPUUserBusyPercent": sysCPUUserBusyPercent,
       "sysCPUSystemBusyPercent": sysCPUSystemBusyPercent,
       "sysFDsFree": sysFDsFree,
       "sysMemTotal": sysMemTotal,
       "sysMemFree": sysMemFree,
       "sysMemInUse": sysMemInUse,
       "sysMemBuffered": sysMemBuffered,
       "sysMemSwapped": sysMemSwapped,
       "sysMemSwapTotal": sysMemSwapTotal,
       "numIdleConnections": numIdleConnections,
       "sslCipherRSAEncryptsExternal": sslCipherRSAEncryptsExternal,
       "dataEntries": dataEntries,
       "dataMemoryUsage": dataMemoryUsage,
       "eventsSeen": eventsSeen,
       "totalDNSResponses": totalDNSResponses,
       "totalBadDNSPackets": totalBadDNSPackets,
       "totalBackendServerErrors": totalBackendServerErrors,
       "totalBytesIn": totalBytesIn,
       "totalBytesOut": totalBytesOut,
       "numberSNMPGetBulkRequests": numberSNMPGetBulkRequests,
       "sslCipherDSASigns": sslCipherDSASigns,
       "sslCipherDSAVerifies": sslCipherDSAVerifies,
       "sslHandshakeTLSv12": sslHandshakeTLSv12,
       "sslCipherDHGenerates": sslCipherDHGenerates,
       "sslCipherDHAgreements": sslCipherDHAgreements,
       "sslCipherAESGCMEncrypts": sslCipherAESGCMEncrypts,
       "sslCipherAESGCMDecrypts": sslCipherAESGCMDecrypts,
       "sslCipherECDHGenerates": sslCipherECDHGenerates,
       "sslCipherECDHAgreements": sslCipherECDHAgreements,
       "sslCipherECDSASigns": sslCipherECDSASigns,
       "sslCipherECDSAVerifies": sslCipherECDSAVerifies,
       "totalRequests": totalRequests,
       "totalTransactions": totalTransactions,
       "hourlyPeakBytesInPerSecond": hourlyPeakBytesInPerSecond,
       "hourlyPeakBytesOutPerSecond": hourlyPeakBytesOutPerSecond,
       "hourlyPeakRequestsPerSecond": hourlyPeakRequestsPerSecond,
       "hourlyPeakSSLConnectionsPerSecond": hourlyPeakSSLConnectionsPerSecond,
       "virtualservers": virtualservers,
       "virtualserverNumber": virtualserverNumber,
       "virtualserverTable": virtualserverTable,
       "virtualserverEntry": virtualserverEntry,
       "virtualserverName": virtualserverName,
       "virtualserverPort": virtualserverPort,
       "virtualserverProtocol": virtualserverProtocol,
       "virtualserverDefaultTrafficPool": virtualserverDefaultTrafficPool,
       "virtualserverBytesInLo": virtualserverBytesInLo,
       "virtualserverBytesInHi": virtualserverBytesInHi,
       "virtualserverBytesOutLo": virtualserverBytesOutLo,
       "virtualserverBytesOutHi": virtualserverBytesOutHi,
       "virtualserverCurrentConn": virtualserverCurrentConn,
       "virtualserverMaxConn": virtualserverMaxConn,
       "virtualserverTotalConn": virtualserverTotalConn,
       "virtualserverDiscard": virtualserverDiscard,
       "virtualserverDirectReplies": virtualserverDirectReplies,
       "virtualserverConnectTimedOut": virtualserverConnectTimedOut,
       "virtualserverDataTimedOut": virtualserverDataTimedOut,
       "virtualserverKeepaliveTimedOut": virtualserverKeepaliveTimedOut,
       "virtualserverUdpTimedOut": virtualserverUdpTimedOut,
       "virtualserverTotalDgram": virtualserverTotalDgram,
       "virtualserverGzip": virtualserverGzip,
       "virtualserverGzipBytesSavedLo": virtualserverGzipBytesSavedLo,
       "virtualserverGzipBytesSavedHi": virtualserverGzipBytesSavedHi,
       "virtualserverHttpRewriteLocation": virtualserverHttpRewriteLocation,
       "virtualserverHttpRewriteCookie": virtualserverHttpRewriteCookie,
       "virtualserverHttpCacheHits": virtualserverHttpCacheHits,
       "virtualserverHttpCacheLookups": virtualserverHttpCacheLookups,
       "virtualserverHttpCacheHitRate": virtualserverHttpCacheHitRate,
       "virtualserverSIPTotalCalls": virtualserverSIPTotalCalls,
       "virtualserverSIPRejectedRequests": virtualserverSIPRejectedRequests,
       "virtualserverConnectionErrors": virtualserverConnectionErrors,
       "virtualserverConnectionFailures": virtualserverConnectionFailures,
       "virtualserverBytesIn": virtualserverBytesIn,
       "virtualserverBytesOut": virtualserverBytesOut,
       "virtualserverGzipBytesSaved": virtualserverGzipBytesSaved,
       "virtualserverCertStatusRequests": virtualserverCertStatusRequests,
       "virtualserverCertStatusResponses": virtualserverCertStatusResponses,
       "virtualserverMaxDurationTimedOut": virtualserverMaxDurationTimedOut,
       "virtualserverProcessingTimedOut": virtualserverProcessingTimedOut,
       "virtualserverTotalRequestsLo": virtualserverTotalRequestsLo,
       "virtualserverTotalRequestsHi": virtualserverTotalRequestsHi,
       "virtualserverTotalRequests": virtualserverTotalRequests,
       "virtualserverTotalHTTPRequestsLo": virtualserverTotalHTTPRequestsLo,
       "virtualserverTotalHTTPRequestsHi": virtualserverTotalHTTPRequestsHi,
       "virtualserverTotalHTTPRequests": virtualserverTotalHTTPRequests,
       "virtualserverTotalHTTP1RequestsLo": virtualserverTotalHTTP1RequestsLo,
       "virtualserverTotalHTTP1RequestsHi": virtualserverTotalHTTP1RequestsHi,
       "virtualserverTotalHTTP1Requests": virtualserverTotalHTTP1Requests,
       "virtualserverTotalHTTP2RequestsLo": virtualserverTotalHTTP2RequestsLo,
       "virtualserverTotalHTTP2RequestsHi": virtualserverTotalHTTP2RequestsHi,
       "virtualserverTotalHTTP2Requests": virtualserverTotalHTTP2Requests,
       "virtualserverPktsInLo": virtualserverPktsInLo,
       "virtualserverPktsInHi": virtualserverPktsInHi,
       "virtualserverPktsOutLo": virtualserverPktsOutLo,
       "virtualserverPktsOutHi": virtualserverPktsOutHi,
       "virtualserverPktsIn": virtualserverPktsIn,
       "virtualserverPktsOut": virtualserverPktsOut,
       "virtualserverL4TCPConnectResets": virtualserverL4TCPConnectResets,
       "virtualserverL4UDPUnreachables": virtualserverL4UDPUnreachables,
       "virtualserverBwLimitPktsDrop": virtualserverBwLimitPktsDrop,
       "virtualserverBwLimitPktsDropLo": virtualserverBwLimitPktsDropLo,
       "virtualserverBwLimitPktsDropHi": virtualserverBwLimitPktsDropHi,
       "virtualserverBwLimitBytesDrop": virtualserverBwLimitBytesDrop,
       "virtualserverBwLimitBytesDropLo": virtualserverBwLimitBytesDropLo,
       "virtualserverBwLimitBytesDropHi": virtualserverBwLimitBytesDropHi,
       "pools": pools,
       "poolNumber": poolNumber,
       "poolTable": poolTable,
       "poolEntry": poolEntry,
       "poolName": poolName,
       "poolAlgorithm": poolAlgorithm,
       "poolNodes": poolNodes,
       "poolDraining": poolDraining,
       "poolFailPool": poolFailPool,
       "poolBytesInLo": poolBytesInLo,
       "poolBytesInHi": poolBytesInHi,
       "poolBytesOutLo": poolBytesOutLo,
       "poolBytesOutHi": poolBytesOutHi,
       "poolTotalConn": poolTotalConn,
       "poolPersistence": poolPersistence,
       "poolSessionMigrated": poolSessionMigrated,
       "poolDisabled": poolDisabled,
       "poolState": poolState,
       "poolConnsQueued": poolConnsQueued,
       "poolQueueTimeouts": poolQueueTimeouts,
       "poolMinQueueTime": poolMinQueueTime,
       "poolMaxQueueTime": poolMaxQueueTime,
       "poolMeanQueueTime": poolMeanQueueTime,
       "poolBytesIn": poolBytesIn,
       "poolBytesOut": poolBytesOut,
       "poolBwLimitPktsDrop": poolBwLimitPktsDrop,
       "poolBwLimitPktsDropLo": poolBwLimitPktsDropLo,
       "poolBwLimitPktsDropHi": poolBwLimitPktsDropHi,
       "poolBwLimitBytesDrop": poolBwLimitBytesDrop,
       "poolBwLimitBytesDropLo": poolBwLimitBytesDropLo,
       "poolBwLimitBytesDropHi": poolBwLimitBytesDropHi,
       "nodes": nodes,
       "nodeNumber": nodeNumber,
       "nodeTable": nodeTable,
       "nodeEntry": nodeEntry,
       "nodeIPAddress": nodeIPAddress,
       "nodePort": nodePort,
       "nodeHostName": nodeHostName,
       "nodeState": nodeState,
       "nodeBytesToNodeLo": nodeBytesToNodeLo,
       "nodeBytesToNodeHi": nodeBytesToNodeHi,
       "nodeBytesFromNodeLo": nodeBytesFromNodeLo,
       "nodeBytesFromNodeHi": nodeBytesFromNodeHi,
       "nodeCurrentRequests": nodeCurrentRequests,
       "nodeTotalConn": nodeTotalConn,
       "nodePooledConn": nodePooledConn,
       "nodeFailures": nodeFailures,
       "nodeNewConn": nodeNewConn,
       "nodeErrors": nodeErrors,
       "nodeResponseMin": nodeResponseMin,
       "nodeResponseMax": nodeResponseMax,
       "nodeResponseMean": nodeResponseMean,
       "nodeCurrentConn": nodeCurrentConn,
       "nodeNumberInet46": nodeNumberInet46,
       "nodeInet46Table": nodeInet46Table,
       "nodeInet46Entry": nodeInet46Entry,
       "nodeInet46AddressType": nodeInet46AddressType,
       "nodeInet46Address": nodeInet46Address,
       "nodeInet46Port": nodeInet46Port,
       "nodeInet46HostName": nodeInet46HostName,
       "nodeInet46State": nodeInet46State,
       "nodeInet46BytesToNodeLo": nodeInet46BytesToNodeLo,
       "nodeInet46BytesToNodeHi": nodeInet46BytesToNodeHi,
       "nodeInet46BytesFromNodeLo": nodeInet46BytesFromNodeLo,
       "nodeInet46BytesFromNodeHi": nodeInet46BytesFromNodeHi,
       "nodeInet46CurrentRequests": nodeInet46CurrentRequests,
       "nodeInet46TotalConn": nodeInet46TotalConn,
       "nodeInet46PooledConn": nodeInet46PooledConn,
       "nodeInet46Failures": nodeInet46Failures,
       "nodeInet46NewConn": nodeInet46NewConn,
       "nodeInet46Errors": nodeInet46Errors,
       "nodeInet46ResponseMin": nodeInet46ResponseMin,
       "nodeInet46ResponseMax": nodeInet46ResponseMax,
       "nodeInet46ResponseMean": nodeInet46ResponseMean,
       "nodeInet46IdleConns": nodeInet46IdleConns,
       "nodeInet46CurrentConn": nodeInet46CurrentConn,
       "nodeInet46BytesToNode": nodeInet46BytesToNode,
       "nodeInet46BytesFromNode": nodeInet46BytesFromNode,
       "perPoolNodeNumber": perPoolNodeNumber,
       "perPoolNodeTable": perPoolNodeTable,
       "perPoolNodeEntry": perPoolNodeEntry,
       "perPoolNodePoolName": perPoolNodePoolName,
       "perPoolNodeNodeAddressType": perPoolNodeNodeAddressType,
       "perPoolNodeNodeAddress": perPoolNodeNodeAddress,
       "perPoolNodeNodePort": perPoolNodeNodePort,
       "perPoolNodeNodeHostName": perPoolNodeNodeHostName,
       "perPoolNodeState": perPoolNodeState,
       "perPoolNodeBytesToNodeLo": perPoolNodeBytesToNodeLo,
       "perPoolNodeBytesToNodeHi": perPoolNodeBytesToNodeHi,
       "perPoolNodeBytesFromNodeLo": perPoolNodeBytesFromNodeLo,
       "perPoolNodeBytesFromNodeHi": perPoolNodeBytesFromNodeHi,
       "perPoolNodeCurrentRequests": perPoolNodeCurrentRequests,
       "perPoolNodeTotalConn": perPoolNodeTotalConn,
       "perPoolNodePooledConn": perPoolNodePooledConn,
       "perPoolNodeFailures": perPoolNodeFailures,
       "perPoolNodeNewConn": perPoolNodeNewConn,
       "perPoolNodeErrors": perPoolNodeErrors,
       "perPoolNodeResponseMin": perPoolNodeResponseMin,
       "perPoolNodeResponseMax": perPoolNodeResponseMax,
       "perPoolNodeResponseMean": perPoolNodeResponseMean,
       "perPoolNodeIdleConns": perPoolNodeIdleConns,
       "perPoolNodeCurrentConn": perPoolNodeCurrentConn,
       "perPoolNodePktsToNodeLo": perPoolNodePktsToNodeLo,
       "perPoolNodePktsToNodeHi": perPoolNodePktsToNodeHi,
       "perPoolNodePktsFromNodeLo": perPoolNodePktsFromNodeLo,
       "perPoolNodePktsFromNodeHi": perPoolNodePktsFromNodeHi,
       "perPoolNodeL4StatelessBuckets": perPoolNodeL4StatelessBuckets,
       "perPoolNodeBytesToNode": perPoolNodeBytesToNode,
       "perPoolNodeBytesFromNode": perPoolNodeBytesFromNode,
       "perPoolNodePktsToNode": perPoolNodePktsToNode,
       "perPoolNodePktsFromNode": perPoolNodePktsFromNode,
       "serviceprotection": serviceprotection,
       "serviceProtNumber": serviceProtNumber,
       "serviceProtTable": serviceProtTable,
       "serviceProtEntry": serviceProtEntry,
       "serviceProtName": serviceProtName,
       "serviceProtTotalRefusal": serviceProtTotalRefusal,
       "serviceProtLastRefusalTime": serviceProtLastRefusalTime,
       "serviceProtRefusalIP": serviceProtRefusalIP,
       "serviceProtRefusalConc1IP": serviceProtRefusalConc1IP,
       "serviceProtRefusalConc10IP": serviceProtRefusalConc10IP,
       "serviceProtRefusalConnRate": serviceProtRefusalConnRate,
       "serviceProtRefusalRFC2396": serviceProtRefusalRFC2396,
       "serviceProtRefusalSize": serviceProtRefusalSize,
       "serviceProtRefusalBinary": serviceProtRefusalBinary,
       "trafficips": trafficips,
       "trafficIPNumber": trafficIPNumber,
       "trafficIPNumberRaised": trafficIPNumberRaised,
       "trafficIPTable": trafficIPTable,
       "trafficIPEntry": trafficIPEntry,
       "trafficIPAddress": trafficIPAddress,
       "trafficIPState": trafficIPState,
       "trafficIPTime": trafficIPTime,
       "trafficIPGatewayPingRequests": trafficIPGatewayPingRequests,
       "trafficIPGatewayPingResponses": trafficIPGatewayPingResponses,
       "trafficIPNodePingRequests": trafficIPNodePingRequests,
       "trafficIPNodePingResponses": trafficIPNodePingResponses,
       "trafficIPPingResponseErrors": trafficIPPingResponseErrors,
       "trafficIPARPMessage": trafficIPARPMessage,
       "trafficIPNumberInet46": trafficIPNumberInet46,
       "trafficIPNumberRaisedInet46": trafficIPNumberRaisedInet46,
       "trafficIPInet46Table": trafficIPInet46Table,
       "trafficIPInet46Entry": trafficIPInet46Entry,
       "trafficIPInet46AddressType": trafficIPInet46AddressType,
       "trafficIPInet46Address": trafficIPInet46Address,
       "trafficIPInet46State": trafficIPInet46State,
       "trafficIPInet46Time": trafficIPInet46Time,
       "servicelevelmonitoring": servicelevelmonitoring,
       "serviceLevelNumber": serviceLevelNumber,
       "serviceLevelTable": serviceLevelTable,
       "serviceLevelEntry": serviceLevelEntry,
       "serviceLevelName": serviceLevelName,
       "serviceLevelTotalConn": serviceLevelTotalConn,
       "serviceLevelTotalNonConf": serviceLevelTotalNonConf,
       "serviceLevelResponseMin": serviceLevelResponseMin,
       "serviceLevelResponseMax": serviceLevelResponseMax,
       "serviceLevelResponseMean": serviceLevelResponseMean,
       "serviceLevelIsOK": serviceLevelIsOK,
       "serviceLevelConforming": serviceLevelConforming,
       "serviceLevelCurrentConns": serviceLevelCurrentConns,
       "pernodeservicelevelmon": pernodeservicelevelmon,
       "perNodeServiceLevelTable": perNodeServiceLevelTable,
       "perNodeServiceLevelEntry": perNodeServiceLevelEntry,
       "perNodeServiceLevelSLMName": perNodeServiceLevelSLMName,
       "perNodeServiceLevelNodeIPAddr": perNodeServiceLevelNodeIPAddr,
       "perNodeServiceLevelNodePort": perNodeServiceLevelNodePort,
       "perNodeServiceLevelTotalConn": perNodeServiceLevelTotalConn,
       "perNodeServiceLevelTotalNonConf": perNodeServiceLevelTotalNonConf,
       "perNodeServiceLevelResponseMin": perNodeServiceLevelResponseMin,
       "perNodeServiceLevelResponseMax": perNodeServiceLevelResponseMax,
       "perNodeServiceLevelResponseMean": perNodeServiceLevelResponseMean,
       "perNodeServiceLevelInet46Table": perNodeServiceLevelInet46Table,
       "perNodeServiceLevelInet46Entry": perNodeServiceLevelInet46Entry,
       "perNodeServiceLevelInet46SLMName": perNodeServiceLevelInet46SLMName,
       "perNodeServiceLevelInet46NodeAddressType": perNodeServiceLevelInet46NodeAddressType,
       "perNodeServiceLevelInet46NodeAddress": perNodeServiceLevelInet46NodeAddress,
       "perNodeServiceLevelInet46NodePort": perNodeServiceLevelInet46NodePort,
       "perNodeServiceLevelInet46TotalConn": perNodeServiceLevelInet46TotalConn,
       "perNodeServiceLevelInet46TotalNonConf": perNodeServiceLevelInet46TotalNonConf,
       "perNodeServiceLevelInet46ResponseMin": perNodeServiceLevelInet46ResponseMin,
       "perNodeServiceLevelInet46ResponseMax": perNodeServiceLevelInet46ResponseMax,
       "perNodeServiceLevelInet46ResponseMean": perNodeServiceLevelInet46ResponseMean,
       "bandwidthmgt": bandwidthmgt,
       "bandwidthClassNumber": bandwidthClassNumber,
       "bandwidthClassTable": bandwidthClassTable,
       "bandwidthClassEntry": bandwidthClassEntry,
       "bandwidthClassName": bandwidthClassName,
       "bandwidthClassMaximum": bandwidthClassMaximum,
       "bandwidthClassGuarantee": bandwidthClassGuarantee,
       "bandwidthClassBytesOutLo": bandwidthClassBytesOutLo,
       "bandwidthClassBytesOutHi": bandwidthClassBytesOutHi,
       "bandwidthClassBytesOut": bandwidthClassBytesOut,
       "bandwidthClassPktsDrop": bandwidthClassPktsDrop,
       "bandwidthClassPktsDropLo": bandwidthClassPktsDropLo,
       "bandwidthClassPktsDropHi": bandwidthClassPktsDropHi,
       "bandwidthClassBytesDrop": bandwidthClassBytesDrop,
       "bandwidthClassBytesDropLo": bandwidthClassBytesDropLo,
       "bandwidthClassBytesDropHi": bandwidthClassBytesDropHi,
       "connratelimit": connratelimit,
       "rateClassNumber": rateClassNumber,
       "rateClassTable": rateClassTable,
       "rateClassEntry": rateClassEntry,
       "rateClassName": rateClassName,
       "rateClassMaxRatePerMin": rateClassMaxRatePerMin,
       "rateClassMaxRatePerSec": rateClassMaxRatePerSec,
       "rateClassQueueLength": rateClassQueueLength,
       "rateClassCurrentRate": rateClassCurrentRate,
       "rateClassDropped": rateClassDropped,
       "rateClassConnsEntered": rateClassConnsEntered,
       "rateClassConnsLeft": rateClassConnsLeft,
       "extra": extra,
       "userCounterNumber": userCounterNumber,
       "userCounterTable": userCounterTable,
       "userCounterEntry": userCounterEntry,
       "userCounterName": userCounterName,
       "userCounterValue": userCounterValue,
       "userCounter64Table": userCounter64Table,
       "userCounter64Entry": userCounter64Entry,
       "userCounter64Name": userCounter64Name,
       "userCounter64Value": userCounter64Value,
       "netinterfaces": netinterfaces,
       "interfaceNumber": interfaceNumber,
       "interfaceTable": interfaceTable,
       "interfaceEntry": interfaceEntry,
       "interfaceName": interfaceName,
       "interfaceRxPackets": interfaceRxPackets,
       "interfaceTxPackets": interfaceTxPackets,
       "interfaceRxErrors": interfaceRxErrors,
       "interfaceTxErrors": interfaceTxErrors,
       "interfaceCollisions": interfaceCollisions,
       "interfaceRxBytesLo": interfaceRxBytesLo,
       "interfaceRxBytesHi": interfaceRxBytesHi,
       "interfaceTxBytesLo": interfaceTxBytesLo,
       "interfaceTxBytesHi": interfaceTxBytesHi,
       "interfaceRxBytes": interfaceRxBytes,
       "interfaceTxBytes": interfaceTxBytes,
       "events": events,
       "eventNumber": eventNumber,
       "eventTable": eventTable,
       "eventEntry": eventEntry,
       "eventName": eventName,
       "eventsMatched": eventsMatched,
       "actions": actions,
       "actionNumber": actionNumber,
       "actionTable": actionTable,
       "actionEntry": actionEntry,
       "actionName": actionName,
       "actionsProcessed": actionsProcessed,
       "zxtmtraps": zxtmtraps,
       "trapsZero": trapsZero,
       "testaction": testaction,
       "running": running,
       "fewfreefds": fewfreefds,
       "restartrequired": restartrequired,
       "timemovedback": timemovedback,
       "sslfail": sslfail,
       "hardware": hardware,
       "zxtmswerror": zxtmswerror,
       "customevent": customevent,
       "versionmismatch": versionmismatch,
       "machineok": machineok,
       "machinetimeout": machinetimeout,
       "machinefail": machinefail,
       "allmachinesok": allmachinesok,
       "flipperbackendsworking": flipperbackendsworking,
       "flipperfrontendsworking": flipperfrontendsworking,
       "pingbackendfail": pingbackendfail,
       "pingfrontendfail": pingfrontendfail,
       "pinggwfail": pinggwfail,
       "statebaddata": statebaddata,
       "stateconnfail": stateconnfail,
       "stateok": stateok,
       "statereadfail": statereadfail,
       "statetimeout": statetimeout,
       "stateunexpected": stateunexpected,
       "statewritefail": statewritefail,
       "sslhwfail": sslhwfail,
       "sslhwrestart": sslhwrestart,
       "sslhwstart": sslhwstart,
       "confdel": confdel,
       "confmod": confmod,
       "confadd": confadd,
       "confok": confok,
       "javadied": javadied,
       "javastop": javastop,
       "javastartfail": javastartfail,
       "javaterminatefail": javaterminatefail,
       "javanotfound": javanotfound,
       "javastarted": javastarted,
       "servleterror": servleterror,
       "monitorfail": monitorfail,
       "monitorok": monitorok,
       "rulexmlerr": rulexmlerr,
       "pooluseunknown": pooluseunknown,
       "ruleabort": ruleabort,
       "rulebufferlarge": rulebufferlarge,
       "rulebodycomperror": rulebodycomperror,
       "forwardproxybadhost": forwardproxybadhost,
       "invalidemit": invalidemit,
       "rulenopersistence": rulenopersistence,
       "rulelogmsginfo": rulelogmsginfo,
       "rulelogmsgwarn": rulelogmsgwarn,
       "rulelogmsgserious": rulelogmsgserious,
       "norate": norate,
       "poolactivenodesunknown": poolactivenodesunknown,
       "datastorefull": datastorefull,
       "expired": expired,
       "licensecorrupt": licensecorrupt,
       "expiresoon": expiresoon,
       "usinglicense": usinglicense,
       "licenseclustertoobig": licenseclustertoobig,
       "unlicensed": unlicensed,
       "usingdevlicense": usingdevlicense,
       "poolnonodes": poolnonodes,
       "poolok": poolok,
       "pooldied": pooldied,
       "noderesolvefailure": noderesolvefailure,
       "noderesolvemultiple": noderesolvemultiple,
       "nodeworking": nodeworking,
       "nostarttls": nostarttls,
       "nodefail": nodefail,
       "starttlsinvalid": starttlsinvalid,
       "ehloinvalid": ehloinvalid,
       "flipperraiselocalworking": flipperraiselocalworking,
       "flipperraiseothersdead": flipperraiseothersdead,
       "flipperraiseosdrop": flipperraiseosdrop,
       "dropipinfo": dropipinfo,
       "dropipwarn": dropipwarn,
       "flipperdadreraise": flipperdadreraise,
       "flipperipexists": flipperipexists,
       "triggersummary": triggersummary,
       "slmclasslimitexceeded": slmclasslimitexceeded,
       "slmrecoveredwarn": slmrecoveredwarn,
       "slmrecoveredserious": slmrecoveredserious,
       "slmfallenbelowwarn": slmfallenbelowwarn,
       "slmfallenbelowserious": slmfallenbelowserious,
       "vscrloutofdate": vscrloutofdate,
       "vsstart": vsstart,
       "vsstop": vsstop,
       "privkeyok": privkeyok,
       "ssldrop": ssldrop,
       "vslogwritefail": vslogwritefail,
       "vssslcertexpired": vssslcertexpired,
       "vssslcerttoexpire": vssslcerttoexpire,
       "vscacertexpired": vscacertexpired,
       "vscacerttoexpire": vscacerttoexpire,
       "maxclientbufferdrop": maxclientbufferdrop,
       "respcompfail": respcompfail,
       "responsetoolarge": responsetoolarge,
       "sipstreamnoports": sipstreamnoports,
       "rtspstreamnoports": rtspstreamnoports,
       "geodataloadfail": geodataloadfail,
       "poolpersistencemismatch": poolpersistencemismatch,
       "connerror": connerror,
       "connfail": connfail,
       "badcontentlen": badcontentlen,
       "activatealldead": activatealldead,
       "machinerecovered": machinerecovered,
       "flipperrecovered": flipperrecovered,
       "activatedautomatically": activatedautomatically,
       "zclustermoderr": zclustermoderr,
       "ec2flipperraiselocalworking": ec2flipperraiselocalworking,
       "ec2flipperraiseothersdead": ec2flipperraiseothersdead,
       "autherror": autherror,
       "logfiledeleted": logfiledeleted,
       "license-graceperiodexpired": license_graceperiodexpired,
       "license-authorized": license_authorized,
       "license-rejected-authorized": license_rejected_authorized,
       "license-rejected-unauthorized": license_rejected_unauthorized,
       "license-timedout-authorized": license_timedout_authorized,
       "license-timedout-unauthorized": license_timedout_unauthorized,
       "license-unauthorized": license_unauthorized,
       "cachesizereduced": cachesizereduced,
       "morememallowed": morememallowed,
       "lessmemallowed": lessmemallowed,
       "usedcredsdeleted": usedcredsdeleted,
       "apistatusprocesshanging": apistatusprocesshanging,
       "autonodedestroyed": autonodedestroyed,
       "autoscalestatusupdateerror": autoscalestatusupdateerror,
       "ec2iperr": ec2iperr,
       "dropec2ipwarn": dropec2ipwarn,
       "ec2nopublicip": ec2nopublicip,
       "multihostload": multihostload,
       "tpslimited": tpslimited,
       "ssltpslimited": ssltpslimited,
       "bwlimited": bwlimited,
       "licensetoomanylocations": licensetoomanylocations,
       "autonodedestructioncomplete": autonodedestructioncomplete,
       "autonodeexisted": autonodeexisted,
       "autoscaledpooltoosmall": autoscaledpooltoosmall,
       "autoscaleinvalidargforcreatenode": autoscaleinvalidargforcreatenode,
       "autonodedisappeared": autonodedisappeared,
       "autoscaledpoolrefractory": autoscaledpoolrefractory,
       "cannotshrinkemptypool": cannotshrinkemptypool,
       "autoscalinghysteresiscantgrow": autoscalinghysteresiscantgrow,
       "autonodecreationcomplete": autonodecreationcomplete,
       "autonodestatuschange": autonodestatuschange,
       "autoscalinghysteresiscantshrink": autoscalinghysteresiscantshrink,
       "autoscalingpoolstatechange": autoscalingpoolstatechange,
       "glbmissingips": glbmissingips,
       "glbnolocations": glbnolocations,
       "locationmonitorok": locationmonitorok,
       "locationmonitorfail": locationmonitorfail,
       "locationok": locationok,
       "locationfail": locationfail,
       "locationsoapok": locationsoapok,
       "locationsoapfail": locationsoapfail,
       "glbdeadlocmissingips": glbdeadlocmissingips,
       "autoscaleresponseparseerror": autoscaleresponseparseerror,
       "glbnewmaster": glbnewmaster,
       "glblogwritefail": glblogwritefail,
       "glbfailalter": glbfailalter,
       "autoscalednodecontested": autoscalednodecontested,
       "autoscalepoolconfupdate": autoscalepoolconfupdate,
       "autonodecreationstarted": autonodecreationstarted,
       "autoscaleinvalidargfordeletenode": autoscaleinvalidargfordeletenode,
       "autoscalinghitroof": autoscalinghitroof,
       "autoscalinghitfloor": autoscalinghitfloor,
       "apichangeprocesshanging": apichangeprocesshanging,
       "autoscaledpooltoobig": autoscaledpooltoobig,
       "autoscalingprocesstimedout": autoscalingprocesstimedout,
       "autoscalingdisabled": autoscalingdisabled,
       "locmovemachine": locmovemachine,
       "locempty": locempty,
       "autoscalinglicenseerror": autoscalinglicenseerror,
       "autoscalinglicenseenabled": autoscalinglicenseenabled,
       "autoscalinglicensedisabled": autoscalinglicensedisabled,
       "confreptimeout": confreptimeout,
       "confrepfailed": confrepfailed,
       "analyticslicenseenabled": analyticslicenseenabled,
       "analyticslicensedisabled": analyticslicensedisabled,
       "autoscalingchangeprocessfailure": autoscalingchangeprocessfailure,
       "autoscalewrongimageid": autoscalewrongimageid,
       "autoscalewrongname": autoscalewrongname,
       "autoscalewrongsizeid": autoscalewrongsizeid,
       "logdiskoverload": logdiskoverload,
       "logdiskfull": logdiskfull,
       "autoscalingresuscitatepool": autoscalingresuscitatepool,
       "zxtmhighload": zxtmhighload,
       "glbservicedied": glbservicedied,
       "glbserviceok": glbserviceok,
       "license-rejected-unauthorized-ts": license_rejected_unauthorized_ts,
       "license-authorized-ts": license_authorized_ts,
       "license-rejected-authorized-ts": license_rejected_authorized_ts,
       "license-timedout-authorized-ts": license_timedout_authorized_ts,
       "license-timedout-unauthorized-ts": license_timedout_unauthorized_ts,
       "license-graceperiodexpired-ts": license_graceperiodexpired_ts,
       "flipperraiseremotedropped": flipperraiseremotedropped,
       "sslrehandshakemininterval": sslrehandshakemininterval,
       "sslhandshakemsgsizelimit": sslhandshakemsgsizelimit,
       "sslcrltoobig": sslcrltoobig,
       "numpools-exceeded": numpools_exceeded,
       "numlocations-exceeded": numlocations_exceeded,
       "numtipg-exceeded": numtipg_exceeded,
       "numnodes-exceeded": numnodes_exceeded,
       "ec2nosecondaryprivateip": ec2nosecondaryprivateip,
       "ec2vpceipassocerr": ec2vpceipassocerr,
       "ec2vpciderr": ec2vpciderr,
       "license-explicitlydisabled-ts": license_explicitlydisabled_ts,
       "rulestreamerrortoomuch": rulestreamerrortoomuch,
       "rulestreamerrornotenough": rulestreamerrornotenough,
       "rulestreamerrorprocessfailure": rulestreamerrorprocessfailure,
       "rulestreamerrornotstarted": rulestreamerrornotstarted,
       "rulestreamerrornotfinished": rulestreamerrornotfinished,
       "rulestreamerrorinternal": rulestreamerrorinternal,
       "rulestreamerrorgetresponse": rulestreamerrorgetresponse,
       "rulesinvalidrequestbody": rulesinvalidrequestbody,
       "serviceruleabort": serviceruleabort,
       "servicerulelocunknown": servicerulelocunknown,
       "servicerulelocnotconfigured": servicerulelocnotconfigured,
       "servicerulelocdead": servicerulelocdead,
       "aptimizeuseunknownprofile": aptimizeuseunknownprofile,
       "aptimizedisabled": aptimizedisabled,
       "aptimizeuseunknownscope": aptimizeuseunknownscope,
       "childcommsfail": childcommsfail,
       "childhung": childhung,
       "childkilled": childkilled,
       "datalocalstorefull": datalocalstorefull,
       "fipsfailinit": fipsfailinit,
       "fipsfailops": fipsfailops,
       "clocknotmonotonic": clocknotmonotonic,
       "clockjump": clockjump,
       "rebootrequired": rebootrequired,
       "ocspstaplingfail": ocspstaplingfail,
       "ocspstaplingnomem": ocspstaplingnomem,
       "appliance": appliance,
       "pingsendfail": pingsendfail,
       "autonodenopublicip": autonodenopublicip,
       "ocspstaplingrevoked": ocspstaplingrevoked,
       "ocspstaplingunknown": ocspstaplingunknown,
       "ocspstaplingunrevoked": ocspstaplingunrevoked,
       "ruleoverrun": ruleoverrun,
       "appfirewallcontrolstarted": appfirewallcontrolstarted,
       "autonoderemoved": autonoderemoved,
       "routingswoperational": routingswoperational,
       "routingswfailurelimitreached": routingswfailurelimitreached,
       "routingswfailed": routingswfailed,
       "routingswstartfailed": routingswstartfailed,
       "appfirewallcontrolstopped": appfirewallcontrolstopped,
       "appfirewallcontrolrestarted": appfirewallcontrolrestarted,
       "appfirewallcontroltimeout": appfirewallcontroltimeout,
       "appfirewallcontrolerror": appfirewallcontrolerror,
       "ospfneighborsok": ospfneighborsok,
       "ospfneighborsdegraded": ospfneighborsdegraded,
       "ospfneighborsfailed": ospfneighborsfailed,
       "nameserverunavailable": nameserverunavailable,
       "nameserveravailable": nameserveravailable,
       "autoscaleresolvefailure": autoscaleresolvefailure,
       "glbtoomanylocations": glbtoomanylocations,
       "dnszonevalidate": dnszonevalidate,
       "dnszonecreaterecord": dnszonecreaterecord,
       "dnszoneparsechild": dnszoneparsechild,
       "dnserroraddzone": dnserroraddzone,
       "dnsaddzone": dnsaddzone,
       "dnszoneparse": dnszoneparse,
       "ec2dataretrievalfailed": ec2dataretrievalfailed,
       "ec2dataretrievalsuccessful": ec2dataretrievalsuccessful,
       "dnszonedelete": dnszonedelete,
       "dnserrordeletezone": dnserrordeletezone,
       "dnssecexpired": dnssecexpired,
       "dnssecexpires": dnssecexpires,
       "glbactivedcmismatch": glbactivedcmismatch,
       "locationdraining": locationdraining,
       "locationnotdraining": locationnotdraining,
       "locationdisabled": locationdisabled,
       "locationenabled": locationenabled,
       "locationunavailable": locationunavailable,
       "locationavailable": locationavailable,
       "glbmanualfailback": glbmanualfailback,
       "nodedrainingtodelete": nodedrainingtodelete,
       "nodedrainingtodeletetimeout": nodedrainingtodeletetimeout,
       "bgpneighborsok": bgpneighborsok,
       "bgpneighborsdegraded": bgpneighborsdegraded,
       "bgpneighborsfailed": bgpneighborsfailed,
       "bgpnoneighbors": bgpnoneighbors,
       "zxtmcpustarvation": zxtmcpustarvation,
       "ec2initialized": ec2initialized,
       "upgradereboot": upgradereboot,
       "sysctlreboot": sysctlreboot,
       "upgraderestart": upgraderestart,
       "unspecifiedreboot": unspecifiedreboot,
       "gcedataretrievalfailed": gcedataretrievalfailed,
       "gcedataretrievalsuccessful": gcedataretrievalsuccessful,
       "autofailbacktimerstarted": autofailbacktimerstarted,
       "autofailbacktimerstopped": autofailbacktimerstopped,
       "autofailbackafterdelay": autofailbackafterdelay,
       "autofailbacktimercancelled": autofailbacktimercancelled,
       "persistence": persistence,
       "cache": cache,
       "webcache": webcache,
       "webCacheHitsLo": webCacheHitsLo,
       "webCacheHitsHi": webCacheHitsHi,
       "webCacheMissesLo": webCacheMissesLo,
       "webCacheMissesHi": webCacheMissesHi,
       "webCacheLookupsLo": webCacheLookupsLo,
       "webCacheLookupsHi": webCacheLookupsHi,
       "webCacheMemUsed": webCacheMemUsed,
       "webCacheMemMaximum": webCacheMemMaximum,
       "webCacheHitRate": webCacheHitRate,
       "webCacheEntries": webCacheEntries,
       "webCacheMaxEntries": webCacheMaxEntries,
       "webCacheOldest": webCacheOldest,
       "webCacheHits": webCacheHits,
       "webCacheMisses": webCacheMisses,
       "webCacheLookups": webCacheLookups,
       "webCacheURLStoreAllocated": webCacheURLStoreAllocated,
       "webCacheURLStoreFree": webCacheURLStoreFree,
       "webCacheURLStoreSize": webCacheURLStoreSize,
       "webCacheURLStoreTotalAllocations": webCacheURLStoreTotalAllocations,
       "webCacheURLStoreTotalFailures": webCacheURLStoreTotalFailures,
       "webCacheURLStoreTotalFrees": webCacheURLStoreTotalFrees,
       "sslcache": sslcache,
       "sslCacheHits": sslCacheHits,
       "sslCacheMisses": sslCacheMisses,
       "sslCacheLookups": sslCacheLookups,
       "sslCacheHitRate": sslCacheHitRate,
       "sslCacheEntries": sslCacheEntries,
       "sslCacheEntriesMax": sslCacheEntriesMax,
       "sslCacheOldest": sslCacheOldest,
       "aspsessioncache": aspsessioncache,
       "aspSessionCacheHits": aspSessionCacheHits,
       "aspSessionCacheMisses": aspSessionCacheMisses,
       "aspSessionCacheLookups": aspSessionCacheLookups,
       "aspSessionCacheHitRate": aspSessionCacheHitRate,
       "aspSessionCacheEntries": aspSessionCacheEntries,
       "aspSessionCacheEntriesMax": aspSessionCacheEntriesMax,
       "aspSessionCacheOldest": aspSessionCacheOldest,
       "ipsessioncache": ipsessioncache,
       "ipSessionCacheHits": ipSessionCacheHits,
       "ipSessionCacheMisses": ipSessionCacheMisses,
       "ipSessionCacheLookups": ipSessionCacheLookups,
       "ipSessionCacheHitRate": ipSessionCacheHitRate,
       "ipSessionCacheEntries": ipSessionCacheEntries,
       "ipSessionCacheEntriesMax": ipSessionCacheEntriesMax,
       "ipSessionCacheOldest": ipSessionCacheOldest,
       "j2eesessioncache": j2eesessioncache,
       "j2eeSessionCacheHits": j2eeSessionCacheHits,
       "j2eeSessionCacheMisses": j2eeSessionCacheMisses,
       "j2eeSessionCacheLookups": j2eeSessionCacheLookups,
       "j2eeSessionCacheHitRate": j2eeSessionCacheHitRate,
       "j2eeSessionCacheEntries": j2eeSessionCacheEntries,
       "j2eeSessionCacheEntriesMax": j2eeSessionCacheEntriesMax,
       "j2eeSessionCacheOldest": j2eeSessionCacheOldest,
       "unisessioncache": unisessioncache,
       "uniSessionCacheHits": uniSessionCacheHits,
       "uniSessionCacheMisses": uniSessionCacheMisses,
       "uniSessionCacheLookups": uniSessionCacheLookups,
       "uniSessionCacheHitRate": uniSessionCacheHitRate,
       "uniSessionCacheEntries": uniSessionCacheEntries,
       "uniSessionCacheEntriesMax": uniSessionCacheEntriesMax,
       "uniSessionCacheOldest": uniSessionCacheOldest,
       "sslsessioncache": sslsessioncache,
       "sslSessionCacheHits": sslSessionCacheHits,
       "sslSessionCacheMisses": sslSessionCacheMisses,
       "sslSessionCacheLookups": sslSessionCacheLookups,
       "sslSessionCacheHitRate": sslSessionCacheHitRate,
       "sslSessionCacheEntries": sslSessionCacheEntries,
       "sslSessionCacheEntriesMax": sslSessionCacheEntriesMax,
       "sslSessionCacheOldest": sslSessionCacheOldest,
       "rules": rules,
       "ruleNumber": ruleNumber,
       "ruleTable": ruleTable,
       "ruleEntry": ruleEntry,
       "ruleName": ruleName,
       "ruleExecutions": ruleExecutions,
       "ruleAborts": ruleAborts,
       "ruleResponds": ruleResponds,
       "rulePoolSelect": rulePoolSelect,
       "ruleRetries": ruleRetries,
       "ruleDiscards": ruleDiscards,
       "ruleExecutionTimeWarnings": ruleExecutionTimeWarnings,
       "monitors": monitors,
       "monitorNumber": monitorNumber,
       "monitorTable": monitorTable,
       "monitorEntry": monitorEntry,
       "monitorName": monitorName,
       "licensekeys": licensekeys,
       "licensekeyNumber": licensekeyNumber,
       "licensekeyTable": licensekeyTable,
       "licensekeyEntry": licensekeyEntry,
       "licensekeyName": licensekeyName,
       "zxtms": zxtms,
       "zxtmNumber": zxtmNumber,
       "zxtmTable": zxtmTable,
       "zxtmEntry": zxtmEntry,
       "zxtmName": zxtmName,
       "trapobjects": trapobjects,
       "fullLogLine": fullLogLine,
       "confName": confName,
       "customEventName": customEventName,
       "domainName": domainName,
       "cloudcredentials": cloudcredentials,
       "cloudcredentialsClassNumber": cloudcredentialsClassNumber,
       "cloudcredentialsTable": cloudcredentialsTable,
       "cloudcredentialsEntry": cloudcredentialsEntry,
       "cloudcredentialsName": cloudcredentialsName,
       "cloudcredentialsStatusRequests": cloudcredentialsStatusRequests,
       "cloudcredentialsNodeCreations": cloudcredentialsNodeCreations,
       "cloudcredentialsNodeDeletions": cloudcredentialsNodeDeletions,
       "glbservices": glbservices,
       "glbServiceNumber": glbServiceNumber,
       "glbServiceTable": glbServiceTable,
       "glbServiceEntry": glbServiceEntry,
       "glbServiceName": glbServiceName,
       "glbServiceResponses": glbServiceResponses,
       "glbServiceUnmodified": glbServiceUnmodified,
       "glbServiceDiscarded": glbServiceDiscarded,
       "perlocationservices": perlocationservices,
       "perLocationServiceTable": perLocationServiceTable,
       "perLocationServiceEntry": perLocationServiceEntry,
       "perLocationServiceLocationName": perLocationServiceLocationName,
       "perLocationServiceLocationCode": perLocationServiceLocationCode,
       "perLocationServiceName": perLocationServiceName,
       "perLocationServiceDraining": perLocationServiceDraining,
       "perLocationServiceState": perLocationServiceState,
       "perLocationServiceFrontendState": perLocationServiceFrontendState,
       "perLocationServiceMonitorState": perLocationServiceMonitorState,
       "perLocationServiceLoad": perLocationServiceLoad,
       "perLocationServiceResponses": perLocationServiceResponses,
       "locations": locations,
       "locationTable": locationTable,
       "locationEntry": locationEntry,
       "locationName": locationName,
       "locationCode": locationCode,
       "locationLoad": locationLoad,
       "locationResponses": locationResponses,
       "listenips": listenips,
       "listenIPTable": listenIPTable,
       "listenIPEntry": listenIPEntry,
       "listenIPAddressType": listenIPAddressType,
       "listenIPAddress": listenIPAddress,
       "listenIPBytesInLo": listenIPBytesInLo,
       "listenIPBytesInHi": listenIPBytesInHi,
       "listenIPBytesOutLo": listenIPBytesOutLo,
       "listenIPBytesOutHi": listenIPBytesOutHi,
       "listenIPCurrentConn": listenIPCurrentConn,
       "listenIPTotalConn": listenIPTotalConn,
       "listenIPMaxConn": listenIPMaxConn,
       "listenIPBytesIn": listenIPBytesIn,
       "listenIPBytesOut": listenIPBytesOut,
       "listenIPTotalRequestsLo": listenIPTotalRequestsLo,
       "listenIPTotalRequestsHi": listenIPTotalRequestsHi,
       "listenIPTotalRequests": listenIPTotalRequests,
       "authenticators": authenticators,
       "authenticatorNumber": authenticatorNumber,
       "authenticatorTable": authenticatorTable,
       "authenticatorEntry": authenticatorEntry,
       "authenticatorName": authenticatorName,
       "authenticatorRequests": authenticatorRequests,
       "authenticatorPasses": authenticatorPasses,
       "authenticatorFails": authenticatorFails,
       "authenticatorErrors": authenticatorErrors,
       "conformanceGroups": conformanceGroups,
       "mainGroup": mainGroup,
       "deprecatedGroup": deprecatedGroup,
       "obsoleteGroup": obsoleteGroup,
       "notificationGroup": notificationGroup,
       "obsoleteNotificationGroup": obsoleteNotificationGroup,
       "deprecatedNotificationGroup": deprecatedNotificationGroup,
       "complianceStatements": complianceStatements,
       "compliance": compliance,
       "deprecatedCompliance": deprecatedCompliance,
       "obsoleteCompliance": obsoleteCompliance,
       "steelheads": steelheads,
       "steelheadNumber": steelheadNumber,
       "steelheadTable": steelheadTable,
       "steelheadEntry": steelheadEntry,
       "steelheadName": steelheadName,
       "steelheadOptimized": steelheadOptimized,
       "sslocspstapling": sslocspstapling,
       "sslOcspStaplingCacheCount": sslOcspStaplingCacheCount,
       "sslOcspStaplingCount": sslOcspStaplingCount,
       "sslOcspStaplingSuccessCount": sslOcspStaplingSuccessCount,
       "sslOcspStaplingFailureCount": sslOcspStaplingFailureCount,
       "sslOcspStaplingGoodCount": sslOcspStaplingGoodCount,
       "sslOcspStaplingRevokedCount": sslOcspStaplingRevokedCount,
       "sslOcspStaplingUnknownCount": sslOcspStaplingUnknownCount,
       "dpaCoreUtilization": dpaCoreUtilization,
       "dataPlaneAccelCoreNumber": dataPlaneAccelCoreNumber,
       "dpaCoreUtilizationTable": dpaCoreUtilizationTable,
       "dpaCoreUtilizationEntry": dpaCoreUtilizationEntry,
       "coreId": coreId,
       "coreUtilizationPercent": coreUtilizationPercent}
)
