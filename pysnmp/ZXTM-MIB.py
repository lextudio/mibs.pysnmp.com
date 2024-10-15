# SNMP MIB module (ZXTM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZXTM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:21:15 2024
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
 NotificationType,
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
    "NotificationType",
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
_Zxtm_ObjectIdentity = ObjectIdentity
zxtm = _Zxtm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2)
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
    version.setStatus("mandatory")
_NumberChildProcesses_Type = Integer32
_NumberChildProcesses_Object = MibScalar
numberChildProcesses = _NumberChildProcesses_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 2),
    _NumberChildProcesses_Type()
)
numberChildProcesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numberChildProcesses.setStatus("mandatory")
_UpTime_Type = TimeTicks
_UpTime_Object = MibScalar
upTime = _UpTime_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 3),
    _UpTime_Type()
)
upTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upTime.setStatus("mandatory")
_TimeLastConfigUpdate_Type = TimeTicks
_TimeLastConfigUpdate_Object = MibScalar
timeLastConfigUpdate = _TimeLastConfigUpdate_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 4),
    _TimeLastConfigUpdate_Type()
)
timeLastConfigUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timeLastConfigUpdate.setStatus("mandatory")
_TotalBytesInLo_Type = Counter32
_TotalBytesInLo_Object = MibScalar
totalBytesInLo = _TotalBytesInLo_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 5),
    _TotalBytesInLo_Type()
)
totalBytesInLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalBytesInLo.setStatus("mandatory")
_TotalBytesInHi_Type = Counter32
_TotalBytesInHi_Object = MibScalar
totalBytesInHi = _TotalBytesInHi_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 6),
    _TotalBytesInHi_Type()
)
totalBytesInHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalBytesInHi.setStatus("mandatory")
_TotalBytesOutLo_Type = Counter32
_TotalBytesOutLo_Object = MibScalar
totalBytesOutLo = _TotalBytesOutLo_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 7),
    _TotalBytesOutLo_Type()
)
totalBytesOutLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalBytesOutLo.setStatus("mandatory")
_TotalBytesOutHi_Type = Counter32
_TotalBytesOutHi_Object = MibScalar
totalBytesOutHi = _TotalBytesOutHi_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 8),
    _TotalBytesOutHi_Type()
)
totalBytesOutHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalBytesOutHi.setStatus("mandatory")
_TotalCurrentConn_Type = Gauge32
_TotalCurrentConn_Object = MibScalar
totalCurrentConn = _TotalCurrentConn_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 9),
    _TotalCurrentConn_Type()
)
totalCurrentConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalCurrentConn.setStatus("mandatory")
_TotalConn_Type = Counter32
_TotalConn_Object = MibScalar
totalConn = _TotalConn_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 10),
    _TotalConn_Type()
)
totalConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalConn.setStatus("mandatory")
_NumberDNSARequests_Type = Counter32
_NumberDNSARequests_Object = MibScalar
numberDNSARequests = _NumberDNSARequests_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 11),
    _NumberDNSARequests_Type()
)
numberDNSARequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numberDNSARequests.setStatus("mandatory")
_NumberDNSACacheHits_Type = Counter32
_NumberDNSACacheHits_Object = MibScalar
numberDNSACacheHits = _NumberDNSACacheHits_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 12),
    _NumberDNSACacheHits_Type()
)
numberDNSACacheHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numberDNSACacheHits.setStatus("mandatory")
_NumberDNSPTRRequests_Type = Counter32
_NumberDNSPTRRequests_Object = MibScalar
numberDNSPTRRequests = _NumberDNSPTRRequests_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 13),
    _NumberDNSPTRRequests_Type()
)
numberDNSPTRRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numberDNSPTRRequests.setStatus("mandatory")
_NumberDNSPTRCacheHits_Type = Counter32
_NumberDNSPTRCacheHits_Object = MibScalar
numberDNSPTRCacheHits = _NumberDNSPTRCacheHits_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 14),
    _NumberDNSPTRCacheHits_Type()
)
numberDNSPTRCacheHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numberDNSPTRCacheHits.setStatus("mandatory")
_NumberSNMPUnauthorisedRequests_Type = Counter32
_NumberSNMPUnauthorisedRequests_Object = MibScalar
numberSNMPUnauthorisedRequests = _NumberSNMPUnauthorisedRequests_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 15),
    _NumberSNMPUnauthorisedRequests_Type()
)
numberSNMPUnauthorisedRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numberSNMPUnauthorisedRequests.setStatus("mandatory")
_NumberSNMPBadRequests_Type = Counter32
_NumberSNMPBadRequests_Object = MibScalar
numberSNMPBadRequests = _NumberSNMPBadRequests_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 16),
    _NumberSNMPBadRequests_Type()
)
numberSNMPBadRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numberSNMPBadRequests.setStatus("mandatory")
_NumberSNMPGetRequests_Type = Counter32
_NumberSNMPGetRequests_Object = MibScalar
numberSNMPGetRequests = _NumberSNMPGetRequests_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 17),
    _NumberSNMPGetRequests_Type()
)
numberSNMPGetRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numberSNMPGetRequests.setStatus("mandatory")
_NumberSNMPGetNextRequests_Type = Counter32
_NumberSNMPGetNextRequests_Object = MibScalar
numberSNMPGetNextRequests = _NumberSNMPGetNextRequests_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 18),
    _NumberSNMPGetNextRequests_Type()
)
numberSNMPGetNextRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numberSNMPGetNextRequests.setStatus("mandatory")
_SslCipherEncrypts_Type = Counter32
_SslCipherEncrypts_Object = MibScalar
sslCipherEncrypts = _SslCipherEncrypts_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 19),
    _SslCipherEncrypts_Type()
)
sslCipherEncrypts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslCipherEncrypts.setStatus("mandatory")
_SslCipherDecrypts_Type = Counter32
_SslCipherDecrypts_Object = MibScalar
sslCipherDecrypts = _SslCipherDecrypts_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 20),
    _SslCipherDecrypts_Type()
)
sslCipherDecrypts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslCipherDecrypts.setStatus("mandatory")
_SslCipherRC4Encrypts_Type = Counter32
_SslCipherRC4Encrypts_Object = MibScalar
sslCipherRC4Encrypts = _SslCipherRC4Encrypts_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 21),
    _SslCipherRC4Encrypts_Type()
)
sslCipherRC4Encrypts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslCipherRC4Encrypts.setStatus("mandatory")
_SslCipherRC4Decrypts_Type = Counter32
_SslCipherRC4Decrypts_Object = MibScalar
sslCipherRC4Decrypts = _SslCipherRC4Decrypts_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 22),
    _SslCipherRC4Decrypts_Type()
)
sslCipherRC4Decrypts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslCipherRC4Decrypts.setStatus("mandatory")
_SslCipherDESEncrypts_Type = Counter32
_SslCipherDESEncrypts_Object = MibScalar
sslCipherDESEncrypts = _SslCipherDESEncrypts_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 23),
    _SslCipherDESEncrypts_Type()
)
sslCipherDESEncrypts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslCipherDESEncrypts.setStatus("mandatory")
_SslCipherDESDecrypts_Type = Counter32
_SslCipherDESDecrypts_Object = MibScalar
sslCipherDESDecrypts = _SslCipherDESDecrypts_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 24),
    _SslCipherDESDecrypts_Type()
)
sslCipherDESDecrypts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslCipherDESDecrypts.setStatus("mandatory")
_SslCipher3DESEncrypts_Type = Counter32
_SslCipher3DESEncrypts_Object = MibScalar
sslCipher3DESEncrypts = _SslCipher3DESEncrypts_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 25),
    _SslCipher3DESEncrypts_Type()
)
sslCipher3DESEncrypts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslCipher3DESEncrypts.setStatus("mandatory")
_SslCipher3DESDecrypts_Type = Counter32
_SslCipher3DESDecrypts_Object = MibScalar
sslCipher3DESDecrypts = _SslCipher3DESDecrypts_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 26),
    _SslCipher3DESDecrypts_Type()
)
sslCipher3DESDecrypts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslCipher3DESDecrypts.setStatus("mandatory")
_SslCipherAESEncrypts_Type = Counter32
_SslCipherAESEncrypts_Object = MibScalar
sslCipherAESEncrypts = _SslCipherAESEncrypts_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 27),
    _SslCipherAESEncrypts_Type()
)
sslCipherAESEncrypts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslCipherAESEncrypts.setStatus("mandatory")
_SslCipherAESDecrypts_Type = Counter32
_SslCipherAESDecrypts_Object = MibScalar
sslCipherAESDecrypts = _SslCipherAESDecrypts_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 28),
    _SslCipherAESDecrypts_Type()
)
sslCipherAESDecrypts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslCipherAESDecrypts.setStatus("mandatory")
_SslCipherRSAEncrypts_Type = Counter32
_SslCipherRSAEncrypts_Object = MibScalar
sslCipherRSAEncrypts = _SslCipherRSAEncrypts_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 29),
    _SslCipherRSAEncrypts_Type()
)
sslCipherRSAEncrypts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslCipherRSAEncrypts.setStatus("mandatory")
_SslCipherRSADecrypts_Type = Counter32
_SslCipherRSADecrypts_Object = MibScalar
sslCipherRSADecrypts = _SslCipherRSADecrypts_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 30),
    _SslCipherRSADecrypts_Type()
)
sslCipherRSADecrypts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslCipherRSADecrypts.setStatus("mandatory")
_SslCipherRSADecryptsExternal_Type = Counter32
_SslCipherRSADecryptsExternal_Object = MibScalar
sslCipherRSADecryptsExternal = _SslCipherRSADecryptsExternal_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 31),
    _SslCipherRSADecryptsExternal_Type()
)
sslCipherRSADecryptsExternal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslCipherRSADecryptsExternal.setStatus("mandatory")
_SslHandshakeSSLv2_Type = Counter32
_SslHandshakeSSLv2_Object = MibScalar
sslHandshakeSSLv2 = _SslHandshakeSSLv2_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 32),
    _SslHandshakeSSLv2_Type()
)
sslHandshakeSSLv2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslHandshakeSSLv2.setStatus("mandatory")
_SslHandshakeSSLv3_Type = Counter32
_SslHandshakeSSLv3_Object = MibScalar
sslHandshakeSSLv3 = _SslHandshakeSSLv3_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 33),
    _SslHandshakeSSLv3_Type()
)
sslHandshakeSSLv3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslHandshakeSSLv3.setStatus("mandatory")
_SslHandshakeTLSv1_Type = Counter32
_SslHandshakeTLSv1_Object = MibScalar
sslHandshakeTLSv1 = _SslHandshakeTLSv1_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 34),
    _SslHandshakeTLSv1_Type()
)
sslHandshakeTLSv1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslHandshakeTLSv1.setStatus("mandatory")
_SslClientCertNotSent_Type = Counter32
_SslClientCertNotSent_Object = MibScalar
sslClientCertNotSent = _SslClientCertNotSent_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 35),
    _SslClientCertNotSent_Type()
)
sslClientCertNotSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslClientCertNotSent.setStatus("mandatory")
_SslClientCertInvalid_Type = Counter32
_SslClientCertInvalid_Object = MibScalar
sslClientCertInvalid = _SslClientCertInvalid_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 36),
    _SslClientCertInvalid_Type()
)
sslClientCertInvalid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslClientCertInvalid.setStatus("mandatory")
_SslClientCertExpired_Type = Counter32
_SslClientCertExpired_Object = MibScalar
sslClientCertExpired = _SslClientCertExpired_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 37),
    _SslClientCertExpired_Type()
)
sslClientCertExpired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslClientCertExpired.setStatus("mandatory")
_SslClientCertRevoked_Type = Counter32
_SslClientCertRevoked_Object = MibScalar
sslClientCertRevoked = _SslClientCertRevoked_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 38),
    _SslClientCertRevoked_Type()
)
sslClientCertRevoked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslClientCertRevoked.setStatus("mandatory")
_SslSessionIDMemCacheHit_Type = Counter32
_SslSessionIDMemCacheHit_Object = MibScalar
sslSessionIDMemCacheHit = _SslSessionIDMemCacheHit_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 39),
    _SslSessionIDMemCacheHit_Type()
)
sslSessionIDMemCacheHit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslSessionIDMemCacheHit.setStatus("mandatory")
_SslSessionIDMemCacheMiss_Type = Counter32
_SslSessionIDMemCacheMiss_Object = MibScalar
sslSessionIDMemCacheMiss = _SslSessionIDMemCacheMiss_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 40),
    _SslSessionIDMemCacheMiss_Type()
)
sslSessionIDMemCacheMiss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslSessionIDMemCacheMiss.setStatus("mandatory")
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
    sslHandshakeTLSv11.setStatus("mandatory")
_SslConnections_Type = Counter32
_SslConnections_Object = MibScalar
sslConnections = _SslConnections_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 44),
    _SslConnections_Type()
)
sslConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslConnections.setStatus("mandatory")
_SysCPUIdlePercent_Type = Gauge32
_SysCPUIdlePercent_Object = MibScalar
sysCPUIdlePercent = _SysCPUIdlePercent_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 45),
    _SysCPUIdlePercent_Type()
)
sysCPUIdlePercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysCPUIdlePercent.setStatus("mandatory")
_SysCPUBusyPercent_Type = Gauge32
_SysCPUBusyPercent_Object = MibScalar
sysCPUBusyPercent = _SysCPUBusyPercent_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 46),
    _SysCPUBusyPercent_Type()
)
sysCPUBusyPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysCPUBusyPercent.setStatus("mandatory")
_SysCPUUserBusyPercent_Type = Gauge32
_SysCPUUserBusyPercent_Object = MibScalar
sysCPUUserBusyPercent = _SysCPUUserBusyPercent_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 47),
    _SysCPUUserBusyPercent_Type()
)
sysCPUUserBusyPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysCPUUserBusyPercent.setStatus("mandatory")
_SysCPUSystemBusyPercent_Type = Gauge32
_SysCPUSystemBusyPercent_Object = MibScalar
sysCPUSystemBusyPercent = _SysCPUSystemBusyPercent_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 48),
    _SysCPUSystemBusyPercent_Type()
)
sysCPUSystemBusyPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysCPUSystemBusyPercent.setStatus("mandatory")
_SysFDsFree_Type = Gauge32
_SysFDsFree_Object = MibScalar
sysFDsFree = _SysFDsFree_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 49),
    _SysFDsFree_Type()
)
sysFDsFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysFDsFree.setStatus("mandatory")
_SysMemTotal_Type = Gauge32
_SysMemTotal_Object = MibScalar
sysMemTotal = _SysMemTotal_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 50),
    _SysMemTotal_Type()
)
sysMemTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysMemTotal.setStatus("mandatory")
_SysMemFree_Type = Gauge32
_SysMemFree_Object = MibScalar
sysMemFree = _SysMemFree_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 51),
    _SysMemFree_Type()
)
sysMemFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysMemFree.setStatus("mandatory")
_SysMemInUse_Type = Gauge32
_SysMemInUse_Object = MibScalar
sysMemInUse = _SysMemInUse_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 52),
    _SysMemInUse_Type()
)
sysMemInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysMemInUse.setStatus("mandatory")
_SysMemBuffered_Type = Gauge32
_SysMemBuffered_Object = MibScalar
sysMemBuffered = _SysMemBuffered_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 53),
    _SysMemBuffered_Type()
)
sysMemBuffered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysMemBuffered.setStatus("mandatory")
_SysMemSwapped_Type = Gauge32
_SysMemSwapped_Object = MibScalar
sysMemSwapped = _SysMemSwapped_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 54),
    _SysMemSwapped_Type()
)
sysMemSwapped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysMemSwapped.setStatus("mandatory")
_SysMemSwapTotal_Type = Gauge32
_SysMemSwapTotal_Object = MibScalar
sysMemSwapTotal = _SysMemSwapTotal_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 55),
    _SysMemSwapTotal_Type()
)
sysMemSwapTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysMemSwapTotal.setStatus("mandatory")
_NumIdleConnections_Type = Gauge32
_NumIdleConnections_Object = MibScalar
numIdleConnections = _NumIdleConnections_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 56),
    _NumIdleConnections_Type()
)
numIdleConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numIdleConnections.setStatus("mandatory")
_SslCipherRSAEncryptsExternal_Type = Counter32
_SslCipherRSAEncryptsExternal_Object = MibScalar
sslCipherRSAEncryptsExternal = _SslCipherRSAEncryptsExternal_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 57),
    _SslCipherRSAEncryptsExternal_Type()
)
sslCipherRSAEncryptsExternal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslCipherRSAEncryptsExternal.setStatus("mandatory")
_DataEntries_Type = Gauge32
_DataEntries_Object = MibScalar
dataEntries = _DataEntries_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 58),
    _DataEntries_Type()
)
dataEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataEntries.setStatus("mandatory")
_DataMemoryUsage_Type = Gauge32
_DataMemoryUsage_Object = MibScalar
dataMemoryUsage = _DataMemoryUsage_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 59),
    _DataMemoryUsage_Type()
)
dataMemoryUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataMemoryUsage.setStatus("mandatory")
_EventsSeen_Type = Counter32
_EventsSeen_Object = MibScalar
eventsSeen = _EventsSeen_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 60),
    _EventsSeen_Type()
)
eventsSeen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventsSeen.setStatus("mandatory")
_TotalDNSResponses_Type = Counter32
_TotalDNSResponses_Object = MibScalar
totalDNSResponses = _TotalDNSResponses_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 61),
    _TotalDNSResponses_Type()
)
totalDNSResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalDNSResponses.setStatus("mandatory")
_TotalBadDNSPackets_Type = Counter32
_TotalBadDNSPackets_Object = MibScalar
totalBadDNSPackets = _TotalBadDNSPackets_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 62),
    _TotalBadDNSPackets_Type()
)
totalBadDNSPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalBadDNSPackets.setStatus("mandatory")
_TotalBackendServerErrors_Type = Counter32
_TotalBackendServerErrors_Object = MibScalar
totalBackendServerErrors = _TotalBackendServerErrors_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 63),
    _TotalBackendServerErrors_Type()
)
totalBackendServerErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalBackendServerErrors.setStatus("mandatory")
_TotalRequests_Type = Counter32
_TotalRequests_Object = MibScalar
totalRequests = _TotalRequests_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 127),
    _TotalRequests_Type()
)
totalRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalRequests.setStatus("mandatory")
_TotalTransactions_Type = Counter32
_TotalTransactions_Object = MibScalar
totalTransactions = _TotalTransactions_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 1, 128),
    _TotalTransactions_Type()
)
totalTransactions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalTransactions.setStatus("mandatory")
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
    virtualserverNumber.setStatus("mandatory")
_VirtualserverTable_Object = MibTable
virtualserverTable = _VirtualserverTable_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 2, 2)
)
if mibBuilder.loadTexts:
    virtualserverTable.setStatus("mandatory")
_VirtualserverEntry_Object = MibTableRow
virtualserverEntry = _VirtualserverEntry_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 2, 2, 1)
)
virtualserverEntry.setIndexNames(
    (0, "ZXTM-MIB", "virtualserverName"),
)
if mibBuilder.loadTexts:
    virtualserverEntry.setStatus("mandatory")


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
    virtualserverName.setStatus("mandatory")


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
    virtualserverPort.setStatus("mandatory")


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
              23)
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
          ("ldap", 11),
          ("ldaps", 12),
          ("pop3", 8),
          ("pop3s", 9),
          ("rtsp", 23),
          ("siptcp", 22),
          ("sipudp", 21),
          ("smtp", 10),
          ("sslforwarding", 14),
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
    virtualserverProtocol.setStatus("mandatory")


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
    virtualserverDefaultTrafficPool.setStatus("mandatory")
_VirtualserverBytesInLo_Type = Counter32
_VirtualserverBytesInLo_Object = MibTableColumn
virtualserverBytesInLo = _VirtualserverBytesInLo_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 2, 2, 1, 5),
    _VirtualserverBytesInLo_Type()
)
virtualserverBytesInLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualserverBytesInLo.setStatus("mandatory")
_VirtualserverBytesInHi_Type = Counter32
_VirtualserverBytesInHi_Object = MibTableColumn
virtualserverBytesInHi = _VirtualserverBytesInHi_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 2, 2, 1, 6),
    _VirtualserverBytesInHi_Type()
)
virtualserverBytesInHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualserverBytesInHi.setStatus("mandatory")
_VirtualserverBytesOutLo_Type = Counter32
_VirtualserverBytesOutLo_Object = MibTableColumn
virtualserverBytesOutLo = _VirtualserverBytesOutLo_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 2, 2, 1, 7),
    _VirtualserverBytesOutLo_Type()
)
virtualserverBytesOutLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualserverBytesOutLo.setStatus("mandatory")
_VirtualserverBytesOutHi_Type = Counter32
_VirtualserverBytesOutHi_Object = MibTableColumn
virtualserverBytesOutHi = _VirtualserverBytesOutHi_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 2, 2, 1, 8),
    _VirtualserverBytesOutHi_Type()
)
virtualserverBytesOutHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualserverBytesOutHi.setStatus("mandatory")
_VirtualserverCurrentConn_Type = Gauge32
_VirtualserverCurrentConn_Object = MibTableColumn
virtualserverCurrentConn = _VirtualserverCurrentConn_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 2, 2, 1, 9),
    _VirtualserverCurrentConn_Type()
)
virtualserverCurrentConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualserverCurrentConn.setStatus("mandatory")
_VirtualserverMaxConn_Type = Gauge32
_VirtualserverMaxConn_Object = MibTableColumn
virtualserverMaxConn = _VirtualserverMaxConn_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 2, 2, 1, 10),
    _VirtualserverMaxConn_Type()
)
virtualserverMaxConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualserverMaxConn.setStatus("mandatory")
_VirtualserverTotalConn_Type = Counter32
_VirtualserverTotalConn_Object = MibTableColumn
virtualserverTotalConn = _VirtualserverTotalConn_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 2, 2, 1, 11),
    _VirtualserverTotalConn_Type()
)
virtualserverTotalConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualserverTotalConn.setStatus("mandatory")
_VirtualserverDiscard_Type = Counter32
_VirtualserverDiscard_Object = MibTableColumn
virtualserverDiscard = _VirtualserverDiscard_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 2, 2, 1, 12),
    _VirtualserverDiscard_Type()
)
virtualserverDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualserverDiscard.setStatus("mandatory")
_VirtualserverDirectReplies_Type = Counter32
_VirtualserverDirectReplies_Object = MibTableColumn
virtualserverDirectReplies = _VirtualserverDirectReplies_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 2, 2, 1, 13),
    _VirtualserverDirectReplies_Type()
)
virtualserverDirectReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualserverDirectReplies.setStatus("mandatory")
_VirtualserverConnectTimedOut_Type = Counter32
_VirtualserverConnectTimedOut_Object = MibTableColumn
virtualserverConnectTimedOut = _VirtualserverConnectTimedOut_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 2, 2, 1, 14),
    _VirtualserverConnectTimedOut_Type()
)
virtualserverConnectTimedOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualserverConnectTimedOut.setStatus("mandatory")
_VirtualserverDataTimedOut_Type = Counter32
_VirtualserverDataTimedOut_Object = MibTableColumn
virtualserverDataTimedOut = _VirtualserverDataTimedOut_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 2, 2, 1, 15),
    _VirtualserverDataTimedOut_Type()
)
virtualserverDataTimedOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualserverDataTimedOut.setStatus("mandatory")
_VirtualserverKeepaliveTimedOut_Type = Counter32
_VirtualserverKeepaliveTimedOut_Object = MibTableColumn
virtualserverKeepaliveTimedOut = _VirtualserverKeepaliveTimedOut_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 2, 2, 1, 16),
    _VirtualserverKeepaliveTimedOut_Type()
)
virtualserverKeepaliveTimedOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualserverKeepaliveTimedOut.setStatus("mandatory")
_VirtualserverUdpTimedOut_Type = Counter32
_VirtualserverUdpTimedOut_Object = MibTableColumn
virtualserverUdpTimedOut = _VirtualserverUdpTimedOut_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 2, 2, 1, 17),
    _VirtualserverUdpTimedOut_Type()
)
virtualserverUdpTimedOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualserverUdpTimedOut.setStatus("mandatory")
_VirtualserverTotalDgram_Type = Counter32
_VirtualserverTotalDgram_Object = MibTableColumn
virtualserverTotalDgram = _VirtualserverTotalDgram_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 2, 2, 1, 18),
    _VirtualserverTotalDgram_Type()
)
virtualserverTotalDgram.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualserverTotalDgram.setStatus("mandatory")
_VirtualserverGzip_Type = Counter32
_VirtualserverGzip_Object = MibTableColumn
virtualserverGzip = _VirtualserverGzip_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 2, 2, 1, 19),
    _VirtualserverGzip_Type()
)
virtualserverGzip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualserverGzip.setStatus("mandatory")
_VirtualserverGzipBytesSavedLo_Type = Counter32
_VirtualserverGzipBytesSavedLo_Object = MibTableColumn
virtualserverGzipBytesSavedLo = _VirtualserverGzipBytesSavedLo_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 2, 2, 1, 20),
    _VirtualserverGzipBytesSavedLo_Type()
)
virtualserverGzipBytesSavedLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualserverGzipBytesSavedLo.setStatus("mandatory")
_VirtualserverGzipBytesSavedHi_Type = Counter32
_VirtualserverGzipBytesSavedHi_Object = MibTableColumn
virtualserverGzipBytesSavedHi = _VirtualserverGzipBytesSavedHi_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 2, 2, 1, 21),
    _VirtualserverGzipBytesSavedHi_Type()
)
virtualserverGzipBytesSavedHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualserverGzipBytesSavedHi.setStatus("mandatory")
_VirtualserverHttpRewriteLocation_Type = Counter32
_VirtualserverHttpRewriteLocation_Object = MibTableColumn
virtualserverHttpRewriteLocation = _VirtualserverHttpRewriteLocation_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 2, 2, 1, 22),
    _VirtualserverHttpRewriteLocation_Type()
)
virtualserverHttpRewriteLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualserverHttpRewriteLocation.setStatus("mandatory")
_VirtualserverHttpRewriteCookie_Type = Counter32
_VirtualserverHttpRewriteCookie_Object = MibTableColumn
virtualserverHttpRewriteCookie = _VirtualserverHttpRewriteCookie_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 2, 2, 1, 23),
    _VirtualserverHttpRewriteCookie_Type()
)
virtualserverHttpRewriteCookie.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualserverHttpRewriteCookie.setStatus("mandatory")
_VirtualserverHttpCacheHits_Type = Counter32
_VirtualserverHttpCacheHits_Object = MibTableColumn
virtualserverHttpCacheHits = _VirtualserverHttpCacheHits_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 2, 2, 1, 24),
    _VirtualserverHttpCacheHits_Type()
)
virtualserverHttpCacheHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualserverHttpCacheHits.setStatus("mandatory")
_VirtualserverHttpCacheLookups_Type = Counter32
_VirtualserverHttpCacheLookups_Object = MibTableColumn
virtualserverHttpCacheLookups = _VirtualserverHttpCacheLookups_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 2, 2, 1, 25),
    _VirtualserverHttpCacheLookups_Type()
)
virtualserverHttpCacheLookups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualserverHttpCacheLookups.setStatus("mandatory")
_VirtualserverHttpCacheHitRate_Type = Gauge32
_VirtualserverHttpCacheHitRate_Object = MibTableColumn
virtualserverHttpCacheHitRate = _VirtualserverHttpCacheHitRate_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 2, 2, 1, 26),
    _VirtualserverHttpCacheHitRate_Type()
)
virtualserverHttpCacheHitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualserverHttpCacheHitRate.setStatus("mandatory")
_VirtualserverSIPTotalCalls_Type = Counter32
_VirtualserverSIPTotalCalls_Object = MibTableColumn
virtualserverSIPTotalCalls = _VirtualserverSIPTotalCalls_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 2, 2, 1, 27),
    _VirtualserverSIPTotalCalls_Type()
)
virtualserverSIPTotalCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualserverSIPTotalCalls.setStatus("mandatory")
_VirtualserverSIPRejectedRequests_Type = Counter32
_VirtualserverSIPRejectedRequests_Object = MibTableColumn
virtualserverSIPRejectedRequests = _VirtualserverSIPRejectedRequests_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 2, 2, 1, 28),
    _VirtualserverSIPRejectedRequests_Type()
)
virtualserverSIPRejectedRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualserverSIPRejectedRequests.setStatus("mandatory")
_VirtualserverConnectionErrors_Type = Counter32
_VirtualserverConnectionErrors_Object = MibTableColumn
virtualserverConnectionErrors = _VirtualserverConnectionErrors_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 2, 2, 1, 29),
    _VirtualserverConnectionErrors_Type()
)
virtualserverConnectionErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualserverConnectionErrors.setStatus("mandatory")
_VirtualserverConnectionFailures_Type = Counter32
_VirtualserverConnectionFailures_Object = MibTableColumn
virtualserverConnectionFailures = _VirtualserverConnectionFailures_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 2, 2, 1, 30),
    _VirtualserverConnectionFailures_Type()
)
virtualserverConnectionFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualserverConnectionFailures.setStatus("mandatory")
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
    poolNumber.setStatus("mandatory")
_PoolTable_Object = MibTable
poolTable = _PoolTable_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 3, 2)
)
if mibBuilder.loadTexts:
    poolTable.setStatus("mandatory")
_PoolEntry_Object = MibTableRow
poolEntry = _PoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 3, 2, 1)
)
poolEntry.setIndexNames(
    (0, "ZXTM-MIB", "poolName"),
)
if mibBuilder.loadTexts:
    poolEntry.setStatus("mandatory")


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
    poolName.setStatus("mandatory")


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
    poolAlgorithm.setStatus("mandatory")
_PoolNodes_Type = Integer32
_PoolNodes_Object = MibTableColumn
poolNodes = _PoolNodes_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 3, 2, 1, 3),
    _PoolNodes_Type()
)
poolNodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolNodes.setStatus("mandatory")
_PoolDraining_Type = Integer32
_PoolDraining_Object = MibTableColumn
poolDraining = _PoolDraining_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 3, 2, 1, 4),
    _PoolDraining_Type()
)
poolDraining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolDraining.setStatus("mandatory")


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
    poolFailPool.setStatus("mandatory")
_PoolBytesInLo_Type = Counter32
_PoolBytesInLo_Object = MibTableColumn
poolBytesInLo = _PoolBytesInLo_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 3, 2, 1, 6),
    _PoolBytesInLo_Type()
)
poolBytesInLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolBytesInLo.setStatus("mandatory")
_PoolBytesInHi_Type = Counter32
_PoolBytesInHi_Object = MibTableColumn
poolBytesInHi = _PoolBytesInHi_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 3, 2, 1, 7),
    _PoolBytesInHi_Type()
)
poolBytesInHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolBytesInHi.setStatus("mandatory")
_PoolBytesOutLo_Type = Counter32
_PoolBytesOutLo_Object = MibTableColumn
poolBytesOutLo = _PoolBytesOutLo_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 3, 2, 1, 8),
    _PoolBytesOutLo_Type()
)
poolBytesOutLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolBytesOutLo.setStatus("mandatory")
_PoolBytesOutHi_Type = Counter32
_PoolBytesOutHi_Object = MibTableColumn
poolBytesOutHi = _PoolBytesOutHi_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 3, 2, 1, 9),
    _PoolBytesOutHi_Type()
)
poolBytesOutHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolBytesOutHi.setStatus("mandatory")
_PoolTotalConn_Type = Counter32
_PoolTotalConn_Object = MibTableColumn
poolTotalConn = _PoolTotalConn_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 3, 2, 1, 10),
    _PoolTotalConn_Type()
)
poolTotalConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolTotalConn.setStatus("mandatory")


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
    poolPersistence.setStatus("mandatory")
_PoolSessionMigrated_Type = Counter32
_PoolSessionMigrated_Object = MibTableColumn
poolSessionMigrated = _PoolSessionMigrated_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 3, 2, 1, 12),
    _PoolSessionMigrated_Type()
)
poolSessionMigrated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolSessionMigrated.setStatus("mandatory")
_PoolDisabled_Type = Integer32
_PoolDisabled_Object = MibTableColumn
poolDisabled = _PoolDisabled_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 3, 2, 1, 13),
    _PoolDisabled_Type()
)
poolDisabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolDisabled.setStatus("mandatory")


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
    poolState.setStatus("mandatory")
_PoolConnsQueued_Type = Gauge32
_PoolConnsQueued_Object = MibTableColumn
poolConnsQueued = _PoolConnsQueued_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 3, 2, 1, 17),
    _PoolConnsQueued_Type()
)
poolConnsQueued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolConnsQueued.setStatus("mandatory")
_PoolQueueTimeouts_Type = Counter32
_PoolQueueTimeouts_Object = MibTableColumn
poolQueueTimeouts = _PoolQueueTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 3, 2, 1, 18),
    _PoolQueueTimeouts_Type()
)
poolQueueTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolQueueTimeouts.setStatus("mandatory")
_PoolMinQueueTime_Type = Gauge32
_PoolMinQueueTime_Object = MibTableColumn
poolMinQueueTime = _PoolMinQueueTime_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 3, 2, 1, 19),
    _PoolMinQueueTime_Type()
)
poolMinQueueTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolMinQueueTime.setStatus("mandatory")
_PoolMaxQueueTime_Type = Gauge32
_PoolMaxQueueTime_Object = MibTableColumn
poolMaxQueueTime = _PoolMaxQueueTime_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 3, 2, 1, 20),
    _PoolMaxQueueTime_Type()
)
poolMaxQueueTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolMaxQueueTime.setStatus("mandatory")
_PoolMeanQueueTime_Type = Gauge32
_PoolMeanQueueTime_Object = MibTableColumn
poolMeanQueueTime = _PoolMeanQueueTime_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 3, 2, 1, 21),
    _PoolMeanQueueTime_Type()
)
poolMeanQueueTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolMeanQueueTime.setStatus("mandatory")
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
    (0, "ZXTM-MIB", "nodeIPAddress"),
    (0, "ZXTM-MIB", "nodePort"),
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
    nodeNumberInet46.setStatus("mandatory")
_NodeInet46Table_Object = MibTable
nodeInet46Table = _NodeInet46Table_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 4, 4)
)
if mibBuilder.loadTexts:
    nodeInet46Table.setStatus("mandatory")
_NodeInet46Entry_Object = MibTableRow
nodeInet46Entry = _NodeInet46Entry_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 4, 4, 1)
)
nodeInet46Entry.setIndexNames(
    (0, "ZXTM-MIB", "nodeInet46AddressType"),
    (0, "ZXTM-MIB", "nodeInet46Address"),
    (0, "ZXTM-MIB", "nodeInet46Port"),
)
if mibBuilder.loadTexts:
    nodeInet46Entry.setStatus("mandatory")
_NodeInet46AddressType_Type = InetAddressType
_NodeInet46AddressType_Object = MibTableColumn
nodeInet46AddressType = _NodeInet46AddressType_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 4, 4, 1, 1),
    _NodeInet46AddressType_Type()
)
nodeInet46AddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeInet46AddressType.setStatus("mandatory")


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
    nodeInet46Address.setStatus("mandatory")


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
    nodeInet46Port.setStatus("mandatory")


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
    nodeInet46HostName.setStatus("mandatory")


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
    nodeInet46State.setStatus("mandatory")
_NodeInet46BytesToNodeLo_Type = Counter32
_NodeInet46BytesToNodeLo_Object = MibTableColumn
nodeInet46BytesToNodeLo = _NodeInet46BytesToNodeLo_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 4, 4, 1, 6),
    _NodeInet46BytesToNodeLo_Type()
)
nodeInet46BytesToNodeLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeInet46BytesToNodeLo.setStatus("mandatory")
_NodeInet46BytesToNodeHi_Type = Counter32
_NodeInet46BytesToNodeHi_Object = MibTableColumn
nodeInet46BytesToNodeHi = _NodeInet46BytesToNodeHi_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 4, 4, 1, 7),
    _NodeInet46BytesToNodeHi_Type()
)
nodeInet46BytesToNodeHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeInet46BytesToNodeHi.setStatus("mandatory")
_NodeInet46BytesFromNodeLo_Type = Counter32
_NodeInet46BytesFromNodeLo_Object = MibTableColumn
nodeInet46BytesFromNodeLo = _NodeInet46BytesFromNodeLo_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 4, 4, 1, 8),
    _NodeInet46BytesFromNodeLo_Type()
)
nodeInet46BytesFromNodeLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeInet46BytesFromNodeLo.setStatus("mandatory")
_NodeInet46BytesFromNodeHi_Type = Counter32
_NodeInet46BytesFromNodeHi_Object = MibTableColumn
nodeInet46BytesFromNodeHi = _NodeInet46BytesFromNodeHi_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 4, 4, 1, 9),
    _NodeInet46BytesFromNodeHi_Type()
)
nodeInet46BytesFromNodeHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeInet46BytesFromNodeHi.setStatus("mandatory")
_NodeInet46CurrentRequests_Type = Gauge32
_NodeInet46CurrentRequests_Object = MibTableColumn
nodeInet46CurrentRequests = _NodeInet46CurrentRequests_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 4, 4, 1, 10),
    _NodeInet46CurrentRequests_Type()
)
nodeInet46CurrentRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeInet46CurrentRequests.setStatus("mandatory")
_NodeInet46TotalConn_Type = Counter32
_NodeInet46TotalConn_Object = MibTableColumn
nodeInet46TotalConn = _NodeInet46TotalConn_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 4, 4, 1, 11),
    _NodeInet46TotalConn_Type()
)
nodeInet46TotalConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeInet46TotalConn.setStatus("mandatory")
_NodeInet46PooledConn_Type = Counter32
_NodeInet46PooledConn_Object = MibTableColumn
nodeInet46PooledConn = _NodeInet46PooledConn_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 4, 4, 1, 12),
    _NodeInet46PooledConn_Type()
)
nodeInet46PooledConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeInet46PooledConn.setStatus("mandatory")
_NodeInet46Failures_Type = Counter32
_NodeInet46Failures_Object = MibTableColumn
nodeInet46Failures = _NodeInet46Failures_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 4, 4, 1, 13),
    _NodeInet46Failures_Type()
)
nodeInet46Failures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeInet46Failures.setStatus("mandatory")
_NodeInet46NewConn_Type = Counter32
_NodeInet46NewConn_Object = MibTableColumn
nodeInet46NewConn = _NodeInet46NewConn_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 4, 4, 1, 14),
    _NodeInet46NewConn_Type()
)
nodeInet46NewConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeInet46NewConn.setStatus("mandatory")
_NodeInet46Errors_Type = Counter32
_NodeInet46Errors_Object = MibTableColumn
nodeInet46Errors = _NodeInet46Errors_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 4, 4, 1, 15),
    _NodeInet46Errors_Type()
)
nodeInet46Errors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeInet46Errors.setStatus("mandatory")
_NodeInet46ResponseMin_Type = Gauge32
_NodeInet46ResponseMin_Object = MibTableColumn
nodeInet46ResponseMin = _NodeInet46ResponseMin_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 4, 4, 1, 16),
    _NodeInet46ResponseMin_Type()
)
nodeInet46ResponseMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeInet46ResponseMin.setStatus("mandatory")
_NodeInet46ResponseMax_Type = Gauge32
_NodeInet46ResponseMax_Object = MibTableColumn
nodeInet46ResponseMax = _NodeInet46ResponseMax_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 4, 4, 1, 17),
    _NodeInet46ResponseMax_Type()
)
nodeInet46ResponseMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeInet46ResponseMax.setStatus("mandatory")
_NodeInet46ResponseMean_Type = Gauge32
_NodeInet46ResponseMean_Object = MibTableColumn
nodeInet46ResponseMean = _NodeInet46ResponseMean_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 4, 4, 1, 18),
    _NodeInet46ResponseMean_Type()
)
nodeInet46ResponseMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeInet46ResponseMean.setStatus("mandatory")
_NodeInet46IdleConns_Type = Gauge32
_NodeInet46IdleConns_Object = MibTableColumn
nodeInet46IdleConns = _NodeInet46IdleConns_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 4, 4, 1, 19),
    _NodeInet46IdleConns_Type()
)
nodeInet46IdleConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeInet46IdleConns.setStatus("mandatory")
_NodeInet46CurrentConn_Type = Gauge32
_NodeInet46CurrentConn_Object = MibTableColumn
nodeInet46CurrentConn = _NodeInet46CurrentConn_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 4, 4, 1, 20),
    _NodeInet46CurrentConn_Type()
)
nodeInet46CurrentConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeInet46CurrentConn.setStatus("mandatory")


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
    perPoolNodeNumber.setStatus("mandatory")
_PerPoolNodeTable_Object = MibTable
perPoolNodeTable = _PerPoolNodeTable_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 4, 6)
)
if mibBuilder.loadTexts:
    perPoolNodeTable.setStatus("mandatory")
_PerPoolNodeEntry_Object = MibTableRow
perPoolNodeEntry = _PerPoolNodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 4, 6, 1)
)
perPoolNodeEntry.setIndexNames(
    (0, "ZXTM-MIB", "perPoolNodePoolName"),
    (0, "ZXTM-MIB", "perPoolNodeNodeAddressType"),
    (0, "ZXTM-MIB", "perPoolNodeNodeAddress"),
    (0, "ZXTM-MIB", "perPoolNodeNodePort"),
)
if mibBuilder.loadTexts:
    perPoolNodeEntry.setStatus("mandatory")


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
    perPoolNodePoolName.setStatus("mandatory")
_PerPoolNodeNodeAddressType_Type = InetAddressType
_PerPoolNodeNodeAddressType_Object = MibTableColumn
perPoolNodeNodeAddressType = _PerPoolNodeNodeAddressType_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 4, 6, 1, 2),
    _PerPoolNodeNodeAddressType_Type()
)
perPoolNodeNodeAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perPoolNodeNodeAddressType.setStatus("mandatory")


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
    perPoolNodeNodeAddress.setStatus("mandatory")


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
    perPoolNodeNodePort.setStatus("mandatory")


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
    perPoolNodeNodeHostName.setStatus("mandatory")


class _PerPoolNodeState_Type(Integer32):
    """Custom type perPoolNodeState based on Integer32"""
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
        *(("alive", 1),
          ("dead", 2),
          ("draining", 4),
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
    perPoolNodeState.setStatus("mandatory")
_PerPoolNodeBytesToNodeLo_Type = Counter32
_PerPoolNodeBytesToNodeLo_Object = MibTableColumn
perPoolNodeBytesToNodeLo = _PerPoolNodeBytesToNodeLo_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 4, 6, 1, 7),
    _PerPoolNodeBytesToNodeLo_Type()
)
perPoolNodeBytesToNodeLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perPoolNodeBytesToNodeLo.setStatus("mandatory")
_PerPoolNodeBytesToNodeHi_Type = Counter32
_PerPoolNodeBytesToNodeHi_Object = MibTableColumn
perPoolNodeBytesToNodeHi = _PerPoolNodeBytesToNodeHi_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 4, 6, 1, 8),
    _PerPoolNodeBytesToNodeHi_Type()
)
perPoolNodeBytesToNodeHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perPoolNodeBytesToNodeHi.setStatus("mandatory")
_PerPoolNodeBytesFromNodeLo_Type = Counter32
_PerPoolNodeBytesFromNodeLo_Object = MibTableColumn
perPoolNodeBytesFromNodeLo = _PerPoolNodeBytesFromNodeLo_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 4, 6, 1, 9),
    _PerPoolNodeBytesFromNodeLo_Type()
)
perPoolNodeBytesFromNodeLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perPoolNodeBytesFromNodeLo.setStatus("mandatory")
_PerPoolNodeBytesFromNodeHi_Type = Counter32
_PerPoolNodeBytesFromNodeHi_Object = MibTableColumn
perPoolNodeBytesFromNodeHi = _PerPoolNodeBytesFromNodeHi_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 4, 6, 1, 10),
    _PerPoolNodeBytesFromNodeHi_Type()
)
perPoolNodeBytesFromNodeHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perPoolNodeBytesFromNodeHi.setStatus("mandatory")
_PerPoolNodeCurrentRequests_Type = Gauge32
_PerPoolNodeCurrentRequests_Object = MibTableColumn
perPoolNodeCurrentRequests = _PerPoolNodeCurrentRequests_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 4, 6, 1, 11),
    _PerPoolNodeCurrentRequests_Type()
)
perPoolNodeCurrentRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perPoolNodeCurrentRequests.setStatus("mandatory")
_PerPoolNodeTotalConn_Type = Counter32
_PerPoolNodeTotalConn_Object = MibTableColumn
perPoolNodeTotalConn = _PerPoolNodeTotalConn_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 4, 6, 1, 12),
    _PerPoolNodeTotalConn_Type()
)
perPoolNodeTotalConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perPoolNodeTotalConn.setStatus("mandatory")
_PerPoolNodePooledConn_Type = Counter32
_PerPoolNodePooledConn_Object = MibTableColumn
perPoolNodePooledConn = _PerPoolNodePooledConn_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 4, 6, 1, 13),
    _PerPoolNodePooledConn_Type()
)
perPoolNodePooledConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perPoolNodePooledConn.setStatus("mandatory")
_PerPoolNodeFailures_Type = Counter32
_PerPoolNodeFailures_Object = MibTableColumn
perPoolNodeFailures = _PerPoolNodeFailures_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 4, 6, 1, 14),
    _PerPoolNodeFailures_Type()
)
perPoolNodeFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perPoolNodeFailures.setStatus("mandatory")
_PerPoolNodeNewConn_Type = Counter32
_PerPoolNodeNewConn_Object = MibTableColumn
perPoolNodeNewConn = _PerPoolNodeNewConn_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 4, 6, 1, 15),
    _PerPoolNodeNewConn_Type()
)
perPoolNodeNewConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perPoolNodeNewConn.setStatus("mandatory")
_PerPoolNodeErrors_Type = Counter32
_PerPoolNodeErrors_Object = MibTableColumn
perPoolNodeErrors = _PerPoolNodeErrors_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 4, 6, 1, 16),
    _PerPoolNodeErrors_Type()
)
perPoolNodeErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perPoolNodeErrors.setStatus("mandatory")
_PerPoolNodeResponseMin_Type = Gauge32
_PerPoolNodeResponseMin_Object = MibTableColumn
perPoolNodeResponseMin = _PerPoolNodeResponseMin_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 4, 6, 1, 17),
    _PerPoolNodeResponseMin_Type()
)
perPoolNodeResponseMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perPoolNodeResponseMin.setStatus("mandatory")
_PerPoolNodeResponseMax_Type = Gauge32
_PerPoolNodeResponseMax_Object = MibTableColumn
perPoolNodeResponseMax = _PerPoolNodeResponseMax_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 4, 6, 1, 18),
    _PerPoolNodeResponseMax_Type()
)
perPoolNodeResponseMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perPoolNodeResponseMax.setStatus("mandatory")
_PerPoolNodeResponseMean_Type = Gauge32
_PerPoolNodeResponseMean_Object = MibTableColumn
perPoolNodeResponseMean = _PerPoolNodeResponseMean_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 4, 6, 1, 19),
    _PerPoolNodeResponseMean_Type()
)
perPoolNodeResponseMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perPoolNodeResponseMean.setStatus("mandatory")
_PerPoolNodeIdleConns_Type = Gauge32
_PerPoolNodeIdleConns_Object = MibTableColumn
perPoolNodeIdleConns = _PerPoolNodeIdleConns_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 4, 6, 1, 20),
    _PerPoolNodeIdleConns_Type()
)
perPoolNodeIdleConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perPoolNodeIdleConns.setStatus("mandatory")
_PerPoolNodeCurrentConn_Type = Gauge32
_PerPoolNodeCurrentConn_Object = MibTableColumn
perPoolNodeCurrentConn = _PerPoolNodeCurrentConn_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 4, 6, 1, 21),
    _PerPoolNodeCurrentConn_Type()
)
perPoolNodeCurrentConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perPoolNodeCurrentConn.setStatus("mandatory")
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
    serviceProtNumber.setStatus("mandatory")
_ServiceProtTable_Object = MibTable
serviceProtTable = _ServiceProtTable_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 5, 2)
)
if mibBuilder.loadTexts:
    serviceProtTable.setStatus("mandatory")
_ServiceProtEntry_Object = MibTableRow
serviceProtEntry = _ServiceProtEntry_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 5, 2, 1)
)
serviceProtEntry.setIndexNames(
    (0, "ZXTM-MIB", "serviceProtName"),
)
if mibBuilder.loadTexts:
    serviceProtEntry.setStatus("mandatory")


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
    serviceProtName.setStatus("mandatory")
_ServiceProtTotalRefusal_Type = Counter32
_ServiceProtTotalRefusal_Object = MibTableColumn
serviceProtTotalRefusal = _ServiceProtTotalRefusal_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 5, 2, 1, 2),
    _ServiceProtTotalRefusal_Type()
)
serviceProtTotalRefusal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serviceProtTotalRefusal.setStatus("mandatory")
_ServiceProtLastRefusalTime_Type = TimeTicks
_ServiceProtLastRefusalTime_Object = MibTableColumn
serviceProtLastRefusalTime = _ServiceProtLastRefusalTime_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 5, 2, 1, 3),
    _ServiceProtLastRefusalTime_Type()
)
serviceProtLastRefusalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serviceProtLastRefusalTime.setStatus("mandatory")
_ServiceProtRefusalIP_Type = Counter32
_ServiceProtRefusalIP_Object = MibTableColumn
serviceProtRefusalIP = _ServiceProtRefusalIP_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 5, 2, 1, 4),
    _ServiceProtRefusalIP_Type()
)
serviceProtRefusalIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serviceProtRefusalIP.setStatus("mandatory")
_ServiceProtRefusalConc1IP_Type = Counter32
_ServiceProtRefusalConc1IP_Object = MibTableColumn
serviceProtRefusalConc1IP = _ServiceProtRefusalConc1IP_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 5, 2, 1, 5),
    _ServiceProtRefusalConc1IP_Type()
)
serviceProtRefusalConc1IP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serviceProtRefusalConc1IP.setStatus("mandatory")
_ServiceProtRefusalConc10IP_Type = Counter32
_ServiceProtRefusalConc10IP_Object = MibTableColumn
serviceProtRefusalConc10IP = _ServiceProtRefusalConc10IP_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 5, 2, 1, 6),
    _ServiceProtRefusalConc10IP_Type()
)
serviceProtRefusalConc10IP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serviceProtRefusalConc10IP.setStatus("mandatory")
_ServiceProtRefusalConnRate_Type = Counter32
_ServiceProtRefusalConnRate_Object = MibTableColumn
serviceProtRefusalConnRate = _ServiceProtRefusalConnRate_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 5, 2, 1, 7),
    _ServiceProtRefusalConnRate_Type()
)
serviceProtRefusalConnRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serviceProtRefusalConnRate.setStatus("mandatory")
_ServiceProtRefusalRFC2396_Type = Counter32
_ServiceProtRefusalRFC2396_Object = MibTableColumn
serviceProtRefusalRFC2396 = _ServiceProtRefusalRFC2396_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 5, 2, 1, 8),
    _ServiceProtRefusalRFC2396_Type()
)
serviceProtRefusalRFC2396.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serviceProtRefusalRFC2396.setStatus("mandatory")
_ServiceProtRefusalSize_Type = Counter32
_ServiceProtRefusalSize_Object = MibTableColumn
serviceProtRefusalSize = _ServiceProtRefusalSize_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 5, 2, 1, 9),
    _ServiceProtRefusalSize_Type()
)
serviceProtRefusalSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serviceProtRefusalSize.setStatus("mandatory")
_ServiceProtRefusalBinary_Type = Counter32
_ServiceProtRefusalBinary_Object = MibTableColumn
serviceProtRefusalBinary = _ServiceProtRefusalBinary_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 5, 2, 1, 10),
    _ServiceProtRefusalBinary_Type()
)
serviceProtRefusalBinary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serviceProtRefusalBinary.setStatus("mandatory")
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
    (0, "ZXTM-MIB", "trafficIPAddress"),
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
    trafficIPGatewayPingRequests.setStatus("mandatory")
_TrafficIPGatewayPingResponses_Type = Counter32
_TrafficIPGatewayPingResponses_Object = MibScalar
trafficIPGatewayPingResponses = _TrafficIPGatewayPingResponses_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 6, 5),
    _TrafficIPGatewayPingResponses_Type()
)
trafficIPGatewayPingResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trafficIPGatewayPingResponses.setStatus("mandatory")
_TrafficIPNodePingRequests_Type = Counter32
_TrafficIPNodePingRequests_Object = MibScalar
trafficIPNodePingRequests = _TrafficIPNodePingRequests_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 6, 6),
    _TrafficIPNodePingRequests_Type()
)
trafficIPNodePingRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trafficIPNodePingRequests.setStatus("mandatory")
_TrafficIPNodePingResponses_Type = Counter32
_TrafficIPNodePingResponses_Object = MibScalar
trafficIPNodePingResponses = _TrafficIPNodePingResponses_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 6, 7),
    _TrafficIPNodePingResponses_Type()
)
trafficIPNodePingResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trafficIPNodePingResponses.setStatus("mandatory")
_TrafficIPPingResponseErrors_Type = Counter32
_TrafficIPPingResponseErrors_Object = MibScalar
trafficIPPingResponseErrors = _TrafficIPPingResponseErrors_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 6, 8),
    _TrafficIPPingResponseErrors_Type()
)
trafficIPPingResponseErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trafficIPPingResponseErrors.setStatus("mandatory")
_TrafficIPARPMessage_Type = Counter32
_TrafficIPARPMessage_Object = MibScalar
trafficIPARPMessage = _TrafficIPARPMessage_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 6, 9),
    _TrafficIPARPMessage_Type()
)
trafficIPARPMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trafficIPARPMessage.setStatus("mandatory")
_TrafficIPNumberInet46_Type = Integer32
_TrafficIPNumberInet46_Object = MibScalar
trafficIPNumberInet46 = _TrafficIPNumberInet46_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 6, 10),
    _TrafficIPNumberInet46_Type()
)
trafficIPNumberInet46.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trafficIPNumberInet46.setStatus("mandatory")
_TrafficIPNumberRaisedInet46_Type = Integer32
_TrafficIPNumberRaisedInet46_Object = MibScalar
trafficIPNumberRaisedInet46 = _TrafficIPNumberRaisedInet46_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 6, 11),
    _TrafficIPNumberRaisedInet46_Type()
)
trafficIPNumberRaisedInet46.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trafficIPNumberRaisedInet46.setStatus("mandatory")
_TrafficIPInet46Table_Object = MibTable
trafficIPInet46Table = _TrafficIPInet46Table_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 6, 12)
)
if mibBuilder.loadTexts:
    trafficIPInet46Table.setStatus("mandatory")
_TrafficIPInet46Entry_Object = MibTableRow
trafficIPInet46Entry = _TrafficIPInet46Entry_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 6, 12, 1)
)
trafficIPInet46Entry.setIndexNames(
    (0, "ZXTM-MIB", "trafficIPInet46AddressType"),
    (0, "ZXTM-MIB", "trafficIPInet46Address"),
)
if mibBuilder.loadTexts:
    trafficIPInet46Entry.setStatus("mandatory")
_TrafficIPInet46AddressType_Type = InetAddressType
_TrafficIPInet46AddressType_Object = MibTableColumn
trafficIPInet46AddressType = _TrafficIPInet46AddressType_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 6, 12, 1, 1),
    _TrafficIPInet46AddressType_Type()
)
trafficIPInet46AddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trafficIPInet46AddressType.setStatus("mandatory")


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
    trafficIPInet46Address.setStatus("mandatory")


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
    trafficIPInet46State.setStatus("mandatory")
_TrafficIPInet46Time_Type = TimeTicks
_TrafficIPInet46Time_Object = MibTableColumn
trafficIPInet46Time = _TrafficIPInet46Time_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 6, 12, 1, 4),
    _TrafficIPInet46Time_Type()
)
trafficIPInet46Time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trafficIPInet46Time.setStatus("mandatory")
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
    serviceLevelNumber.setStatus("mandatory")
_ServiceLevelTable_Object = MibTable
serviceLevelTable = _ServiceLevelTable_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 7, 2)
)
if mibBuilder.loadTexts:
    serviceLevelTable.setStatus("mandatory")
_ServiceLevelEntry_Object = MibTableRow
serviceLevelEntry = _ServiceLevelEntry_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 7, 2, 1)
)
serviceLevelEntry.setIndexNames(
    (0, "ZXTM-MIB", "serviceLevelName"),
)
if mibBuilder.loadTexts:
    serviceLevelEntry.setStatus("mandatory")


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
    serviceLevelName.setStatus("mandatory")
_ServiceLevelTotalConn_Type = Counter32
_ServiceLevelTotalConn_Object = MibTableColumn
serviceLevelTotalConn = _ServiceLevelTotalConn_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 7, 2, 1, 2),
    _ServiceLevelTotalConn_Type()
)
serviceLevelTotalConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serviceLevelTotalConn.setStatus("mandatory")
_ServiceLevelTotalNonConf_Type = Counter32
_ServiceLevelTotalNonConf_Object = MibTableColumn
serviceLevelTotalNonConf = _ServiceLevelTotalNonConf_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 7, 2, 1, 3),
    _ServiceLevelTotalNonConf_Type()
)
serviceLevelTotalNonConf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serviceLevelTotalNonConf.setStatus("mandatory")
_ServiceLevelResponseMin_Type = Gauge32
_ServiceLevelResponseMin_Object = MibTableColumn
serviceLevelResponseMin = _ServiceLevelResponseMin_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 7, 2, 1, 4),
    _ServiceLevelResponseMin_Type()
)
serviceLevelResponseMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serviceLevelResponseMin.setStatus("mandatory")
_ServiceLevelResponseMax_Type = Gauge32
_ServiceLevelResponseMax_Object = MibTableColumn
serviceLevelResponseMax = _ServiceLevelResponseMax_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 7, 2, 1, 5),
    _ServiceLevelResponseMax_Type()
)
serviceLevelResponseMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serviceLevelResponseMax.setStatus("mandatory")
_ServiceLevelResponseMean_Type = Gauge32
_ServiceLevelResponseMean_Object = MibTableColumn
serviceLevelResponseMean = _ServiceLevelResponseMean_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 7, 2, 1, 6),
    _ServiceLevelResponseMean_Type()
)
serviceLevelResponseMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serviceLevelResponseMean.setStatus("mandatory")


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
    serviceLevelIsOK.setStatus("mandatory")
_ServiceLevelConforming_Type = Gauge32
_ServiceLevelConforming_Object = MibTableColumn
serviceLevelConforming = _ServiceLevelConforming_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 7, 2, 1, 8),
    _ServiceLevelConforming_Type()
)
serviceLevelConforming.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serviceLevelConforming.setStatus("mandatory")
_ServiceLevelCurrentConns_Type = Gauge32
_ServiceLevelCurrentConns_Object = MibTableColumn
serviceLevelCurrentConns = _ServiceLevelCurrentConns_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 7, 2, 1, 9),
    _ServiceLevelCurrentConns_Type()
)
serviceLevelCurrentConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serviceLevelCurrentConns.setStatus("mandatory")
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
    (0, "ZXTM-MIB", "perNodeServiceLevelSLMName"),
    (0, "ZXTM-MIB", "perNodeServiceLevelNodeIPAddr"),
    (0, "ZXTM-MIB", "perNodeServiceLevelNodePort"),
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
    perNodeServiceLevelInet46Table.setStatus("mandatory")
_PerNodeServiceLevelInet46Entry_Object = MibTableRow
perNodeServiceLevelInet46Entry = _PerNodeServiceLevelInet46Entry_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 8, 2, 1)
)
perNodeServiceLevelInet46Entry.setIndexNames(
    (0, "ZXTM-MIB", "perNodeServiceLevelInet46SLMName"),
    (0, "ZXTM-MIB", "perNodeServiceLevelInet46NodeAddressType"),
    (0, "ZXTM-MIB", "perNodeServiceLevelInet46NodeAddress"),
    (0, "ZXTM-MIB", "perNodeServiceLevelInet46NodePort"),
)
if mibBuilder.loadTexts:
    perNodeServiceLevelInet46Entry.setStatus("mandatory")


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
    perNodeServiceLevelInet46SLMName.setStatus("mandatory")
_PerNodeServiceLevelInet46NodeAddressType_Type = InetAddressType
_PerNodeServiceLevelInet46NodeAddressType_Object = MibTableColumn
perNodeServiceLevelInet46NodeAddressType = _PerNodeServiceLevelInet46NodeAddressType_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 8, 2, 1, 2),
    _PerNodeServiceLevelInet46NodeAddressType_Type()
)
perNodeServiceLevelInet46NodeAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perNodeServiceLevelInet46NodeAddressType.setStatus("mandatory")


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
    perNodeServiceLevelInet46NodeAddress.setStatus("mandatory")


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
    perNodeServiceLevelInet46NodePort.setStatus("mandatory")
_PerNodeServiceLevelInet46TotalConn_Type = Counter32
_PerNodeServiceLevelInet46TotalConn_Object = MibTableColumn
perNodeServiceLevelInet46TotalConn = _PerNodeServiceLevelInet46TotalConn_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 8, 2, 1, 5),
    _PerNodeServiceLevelInet46TotalConn_Type()
)
perNodeServiceLevelInet46TotalConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perNodeServiceLevelInet46TotalConn.setStatus("mandatory")
_PerNodeServiceLevelInet46TotalNonConf_Type = Counter32
_PerNodeServiceLevelInet46TotalNonConf_Object = MibTableColumn
perNodeServiceLevelInet46TotalNonConf = _PerNodeServiceLevelInet46TotalNonConf_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 8, 2, 1, 6),
    _PerNodeServiceLevelInet46TotalNonConf_Type()
)
perNodeServiceLevelInet46TotalNonConf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perNodeServiceLevelInet46TotalNonConf.setStatus("mandatory")
_PerNodeServiceLevelInet46ResponseMin_Type = Gauge32
_PerNodeServiceLevelInet46ResponseMin_Object = MibTableColumn
perNodeServiceLevelInet46ResponseMin = _PerNodeServiceLevelInet46ResponseMin_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 8, 2, 1, 7),
    _PerNodeServiceLevelInet46ResponseMin_Type()
)
perNodeServiceLevelInet46ResponseMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perNodeServiceLevelInet46ResponseMin.setStatus("mandatory")
_PerNodeServiceLevelInet46ResponseMax_Type = Gauge32
_PerNodeServiceLevelInet46ResponseMax_Object = MibTableColumn
perNodeServiceLevelInet46ResponseMax = _PerNodeServiceLevelInet46ResponseMax_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 8, 2, 1, 8),
    _PerNodeServiceLevelInet46ResponseMax_Type()
)
perNodeServiceLevelInet46ResponseMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perNodeServiceLevelInet46ResponseMax.setStatus("mandatory")
_PerNodeServiceLevelInet46ResponseMean_Type = Gauge32
_PerNodeServiceLevelInet46ResponseMean_Object = MibTableColumn
perNodeServiceLevelInet46ResponseMean = _PerNodeServiceLevelInet46ResponseMean_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 8, 2, 1, 9),
    _PerNodeServiceLevelInet46ResponseMean_Type()
)
perNodeServiceLevelInet46ResponseMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perNodeServiceLevelInet46ResponseMean.setStatus("mandatory")
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
    bandwidthClassNumber.setStatus("mandatory")
_BandwidthClassTable_Object = MibTable
bandwidthClassTable = _BandwidthClassTable_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 9, 2)
)
if mibBuilder.loadTexts:
    bandwidthClassTable.setStatus("mandatory")
_BandwidthClassEntry_Object = MibTableRow
bandwidthClassEntry = _BandwidthClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 9, 2, 1)
)
bandwidthClassEntry.setIndexNames(
    (0, "ZXTM-MIB", "bandwidthClassName"),
)
if mibBuilder.loadTexts:
    bandwidthClassEntry.setStatus("mandatory")


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
    bandwidthClassName.setStatus("mandatory")
_BandwidthClassMaximum_Type = Integer32
_BandwidthClassMaximum_Object = MibTableColumn
bandwidthClassMaximum = _BandwidthClassMaximum_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 9, 2, 1, 2),
    _BandwidthClassMaximum_Type()
)
bandwidthClassMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandwidthClassMaximum.setStatus("mandatory")
_BandwidthClassGuarantee_Type = Integer32
_BandwidthClassGuarantee_Object = MibTableColumn
bandwidthClassGuarantee = _BandwidthClassGuarantee_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 9, 2, 1, 3),
    _BandwidthClassGuarantee_Type()
)
bandwidthClassGuarantee.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandwidthClassGuarantee.setStatus("mandatory")
_BandwidthClassBytesOutLo_Type = Counter32
_BandwidthClassBytesOutLo_Object = MibTableColumn
bandwidthClassBytesOutLo = _BandwidthClassBytesOutLo_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 9, 2, 1, 4),
    _BandwidthClassBytesOutLo_Type()
)
bandwidthClassBytesOutLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandwidthClassBytesOutLo.setStatus("mandatory")
_BandwidthClassBytesOutHi_Type = Counter32
_BandwidthClassBytesOutHi_Object = MibTableColumn
bandwidthClassBytesOutHi = _BandwidthClassBytesOutHi_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 9, 2, 1, 5),
    _BandwidthClassBytesOutHi_Type()
)
bandwidthClassBytesOutHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandwidthClassBytesOutHi.setStatus("mandatory")
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
    rateClassNumber.setStatus("mandatory")
_RateClassTable_Object = MibTable
rateClassTable = _RateClassTable_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 10, 2)
)
if mibBuilder.loadTexts:
    rateClassTable.setStatus("mandatory")
_RateClassEntry_Object = MibTableRow
rateClassEntry = _RateClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 10, 2, 1)
)
rateClassEntry.setIndexNames(
    (0, "ZXTM-MIB", "rateClassName"),
)
if mibBuilder.loadTexts:
    rateClassEntry.setStatus("mandatory")


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
    rateClassName.setStatus("mandatory")
_RateClassMaxRatePerMin_Type = Integer32
_RateClassMaxRatePerMin_Object = MibTableColumn
rateClassMaxRatePerMin = _RateClassMaxRatePerMin_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 10, 2, 1, 2),
    _RateClassMaxRatePerMin_Type()
)
rateClassMaxRatePerMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rateClassMaxRatePerMin.setStatus("mandatory")
_RateClassMaxRatePerSec_Type = Integer32
_RateClassMaxRatePerSec_Object = MibTableColumn
rateClassMaxRatePerSec = _RateClassMaxRatePerSec_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 10, 2, 1, 3),
    _RateClassMaxRatePerSec_Type()
)
rateClassMaxRatePerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rateClassMaxRatePerSec.setStatus("mandatory")
_RateClassQueueLength_Type = Gauge32
_RateClassQueueLength_Object = MibTableColumn
rateClassQueueLength = _RateClassQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 10, 2, 1, 4),
    _RateClassQueueLength_Type()
)
rateClassQueueLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rateClassQueueLength.setStatus("mandatory")
_RateClassCurrentRate_Type = Gauge32
_RateClassCurrentRate_Object = MibTableColumn
rateClassCurrentRate = _RateClassCurrentRate_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 10, 2, 1, 5),
    _RateClassCurrentRate_Type()
)
rateClassCurrentRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rateClassCurrentRate.setStatus("mandatory")
_RateClassDropped_Type = Counter32
_RateClassDropped_Object = MibTableColumn
rateClassDropped = _RateClassDropped_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 10, 2, 1, 6),
    _RateClassDropped_Type()
)
rateClassDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rateClassDropped.setStatus("mandatory")
_RateClassConnsEntered_Type = Counter32
_RateClassConnsEntered_Object = MibTableColumn
rateClassConnsEntered = _RateClassConnsEntered_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 10, 2, 1, 7),
    _RateClassConnsEntered_Type()
)
rateClassConnsEntered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rateClassConnsEntered.setStatus("mandatory")
_RateClassConnsLeft_Type = Counter32
_RateClassConnsLeft_Object = MibTableColumn
rateClassConnsLeft = _RateClassConnsLeft_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 10, 2, 1, 8),
    _RateClassConnsLeft_Type()
)
rateClassConnsLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rateClassConnsLeft.setStatus("mandatory")
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
    userCounterNumber.setStatus("mandatory")
_UserCounterTable_Object = MibTable
userCounterTable = _UserCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 11, 2)
)
if mibBuilder.loadTexts:
    userCounterTable.setStatus("mandatory")
_UserCounterEntry_Object = MibTableRow
userCounterEntry = _UserCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 11, 2, 1)
)
userCounterEntry.setIndexNames(
    (0, "ZXTM-MIB", "userCounterName"),
)
if mibBuilder.loadTexts:
    userCounterEntry.setStatus("mandatory")


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
    userCounterName.setStatus("mandatory")
_UserCounterValue_Type = Counter32
_UserCounterValue_Object = MibTableColumn
userCounterValue = _UserCounterValue_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 11, 2, 1, 2),
    _UserCounterValue_Type()
)
userCounterValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userCounterValue.setStatus("mandatory")
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
    interfaceNumber.setStatus("mandatory")
_InterfaceTable_Object = MibTable
interfaceTable = _InterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 12, 2)
)
if mibBuilder.loadTexts:
    interfaceTable.setStatus("mandatory")
_InterfaceEntry_Object = MibTableRow
interfaceEntry = _InterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 12, 2, 1)
)
interfaceEntry.setIndexNames(
    (0, "ZXTM-MIB", "interfaceName"),
)
if mibBuilder.loadTexts:
    interfaceEntry.setStatus("mandatory")


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
    interfaceName.setStatus("mandatory")
_InterfaceRxPackets_Type = Counter32
_InterfaceRxPackets_Object = MibTableColumn
interfaceRxPackets = _InterfaceRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 12, 2, 1, 2),
    _InterfaceRxPackets_Type()
)
interfaceRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceRxPackets.setStatus("mandatory")
_InterfaceTxPackets_Type = Counter32
_InterfaceTxPackets_Object = MibTableColumn
interfaceTxPackets = _InterfaceTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 12, 2, 1, 3),
    _InterfaceTxPackets_Type()
)
interfaceTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTxPackets.setStatus("mandatory")
_InterfaceRxErrors_Type = Counter32
_InterfaceRxErrors_Object = MibTableColumn
interfaceRxErrors = _InterfaceRxErrors_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 12, 2, 1, 4),
    _InterfaceRxErrors_Type()
)
interfaceRxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceRxErrors.setStatus("mandatory")
_InterfaceTxErrors_Type = Counter32
_InterfaceTxErrors_Object = MibTableColumn
interfaceTxErrors = _InterfaceTxErrors_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 12, 2, 1, 5),
    _InterfaceTxErrors_Type()
)
interfaceTxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTxErrors.setStatus("mandatory")
_InterfaceCollisions_Type = Counter32
_InterfaceCollisions_Object = MibTableColumn
interfaceCollisions = _InterfaceCollisions_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 12, 2, 1, 6),
    _InterfaceCollisions_Type()
)
interfaceCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceCollisions.setStatus("mandatory")
_InterfaceRxBytesLo_Type = Counter32
_InterfaceRxBytesLo_Object = MibTableColumn
interfaceRxBytesLo = _InterfaceRxBytesLo_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 12, 2, 1, 7),
    _InterfaceRxBytesLo_Type()
)
interfaceRxBytesLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceRxBytesLo.setStatus("mandatory")
_InterfaceRxBytesHi_Type = Counter32
_InterfaceRxBytesHi_Object = MibTableColumn
interfaceRxBytesHi = _InterfaceRxBytesHi_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 12, 2, 1, 8),
    _InterfaceRxBytesHi_Type()
)
interfaceRxBytesHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceRxBytesHi.setStatus("mandatory")
_InterfaceTxBytesLo_Type = Counter32
_InterfaceTxBytesLo_Object = MibTableColumn
interfaceTxBytesLo = _InterfaceTxBytesLo_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 12, 2, 1, 9),
    _InterfaceTxBytesLo_Type()
)
interfaceTxBytesLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTxBytesLo.setStatus("mandatory")
_InterfaceTxBytesHi_Type = Counter32
_InterfaceTxBytesHi_Object = MibTableColumn
interfaceTxBytesHi = _InterfaceTxBytesHi_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 12, 2, 1, 10),
    _InterfaceTxBytesHi_Type()
)
interfaceTxBytesHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTxBytesHi.setStatus("mandatory")
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
    eventNumber.setStatus("mandatory")
_EventTable_Object = MibTable
eventTable = _EventTable_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 13, 2)
)
if mibBuilder.loadTexts:
    eventTable.setStatus("mandatory")
_EventEntry_Object = MibTableRow
eventEntry = _EventEntry_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 13, 2, 1)
)
eventEntry.setIndexNames(
    (0, "ZXTM-MIB", "eventName"),
)
if mibBuilder.loadTexts:
    eventEntry.setStatus("mandatory")


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
    eventName.setStatus("mandatory")
_EventsMatched_Type = Counter32
_EventsMatched_Object = MibTableColumn
eventsMatched = _EventsMatched_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 13, 2, 1, 2),
    _EventsMatched_Type()
)
eventsMatched.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventsMatched.setStatus("mandatory")
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
    actionNumber.setStatus("mandatory")
_ActionTable_Object = MibTable
actionTable = _ActionTable_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 14, 2)
)
if mibBuilder.loadTexts:
    actionTable.setStatus("mandatory")
_ActionEntry_Object = MibTableRow
actionEntry = _ActionEntry_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 14, 2, 1)
)
actionEntry.setIndexNames(
    (0, "ZXTM-MIB", "actionName"),
)
if mibBuilder.loadTexts:
    actionEntry.setStatus("mandatory")


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
    actionName.setStatus("mandatory")
_ActionsProcessed_Type = Counter32
_ActionsProcessed_Object = MibTableColumn
actionsProcessed = _ActionsProcessed_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 14, 2, 1, 2),
    _ActionsProcessed_Type()
)
actionsProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actionsProcessed.setStatus("mandatory")
_Zxtmtraps_ObjectIdentity = ObjectIdentity
zxtmtraps = _Zxtmtraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15)
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
    webCacheHitsLo.setStatus("mandatory")
_WebCacheHitsHi_Type = Counter32
_WebCacheHitsHi_Object = MibScalar
webCacheHitsHi = _WebCacheHitsHi_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 17, 1, 2),
    _WebCacheHitsHi_Type()
)
webCacheHitsHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webCacheHitsHi.setStatus("mandatory")
_WebCacheMissesLo_Type = Counter32
_WebCacheMissesLo_Object = MibScalar
webCacheMissesLo = _WebCacheMissesLo_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 17, 1, 3),
    _WebCacheMissesLo_Type()
)
webCacheMissesLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webCacheMissesLo.setStatus("mandatory")
_WebCacheMissesHi_Type = Counter32
_WebCacheMissesHi_Object = MibScalar
webCacheMissesHi = _WebCacheMissesHi_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 17, 1, 4),
    _WebCacheMissesHi_Type()
)
webCacheMissesHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webCacheMissesHi.setStatus("mandatory")
_WebCacheLookupsLo_Type = Counter32
_WebCacheLookupsLo_Object = MibScalar
webCacheLookupsLo = _WebCacheLookupsLo_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 17, 1, 5),
    _WebCacheLookupsLo_Type()
)
webCacheLookupsLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webCacheLookupsLo.setStatus("mandatory")
_WebCacheLookupsHi_Type = Counter32
_WebCacheLookupsHi_Object = MibScalar
webCacheLookupsHi = _WebCacheLookupsHi_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 17, 1, 6),
    _WebCacheLookupsHi_Type()
)
webCacheLookupsHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webCacheLookupsHi.setStatus("mandatory")
_WebCacheMemUsed_Type = Gauge32
_WebCacheMemUsed_Object = MibScalar
webCacheMemUsed = _WebCacheMemUsed_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 17, 1, 7),
    _WebCacheMemUsed_Type()
)
webCacheMemUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webCacheMemUsed.setStatus("mandatory")
_WebCacheMemMaximum_Type = Gauge32
_WebCacheMemMaximum_Object = MibScalar
webCacheMemMaximum = _WebCacheMemMaximum_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 17, 1, 8),
    _WebCacheMemMaximum_Type()
)
webCacheMemMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webCacheMemMaximum.setStatus("mandatory")
_WebCacheHitRate_Type = Gauge32
_WebCacheHitRate_Object = MibScalar
webCacheHitRate = _WebCacheHitRate_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 17, 1, 9),
    _WebCacheHitRate_Type()
)
webCacheHitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webCacheHitRate.setStatus("mandatory")
_WebCacheEntries_Type = Gauge32
_WebCacheEntries_Object = MibScalar
webCacheEntries = _WebCacheEntries_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 17, 1, 10),
    _WebCacheEntries_Type()
)
webCacheEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webCacheEntries.setStatus("mandatory")
_WebCacheMaxEntries_Type = Gauge32
_WebCacheMaxEntries_Object = MibScalar
webCacheMaxEntries = _WebCacheMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 17, 1, 11),
    _WebCacheMaxEntries_Type()
)
webCacheMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webCacheMaxEntries.setStatus("mandatory")
_WebCacheOldest_Type = Gauge32
_WebCacheOldest_Object = MibScalar
webCacheOldest = _WebCacheOldest_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 17, 1, 12),
    _WebCacheOldest_Type()
)
webCacheOldest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webCacheOldest.setStatus("mandatory")
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
    sslCacheHits.setStatus("mandatory")
_SslCacheMisses_Type = Counter32
_SslCacheMisses_Object = MibScalar
sslCacheMisses = _SslCacheMisses_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 17, 2, 2),
    _SslCacheMisses_Type()
)
sslCacheMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslCacheMisses.setStatus("mandatory")
_SslCacheLookups_Type = Counter32
_SslCacheLookups_Object = MibScalar
sslCacheLookups = _SslCacheLookups_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 17, 2, 3),
    _SslCacheLookups_Type()
)
sslCacheLookups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslCacheLookups.setStatus("mandatory")
_SslCacheHitRate_Type = Gauge32
_SslCacheHitRate_Object = MibScalar
sslCacheHitRate = _SslCacheHitRate_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 17, 2, 4),
    _SslCacheHitRate_Type()
)
sslCacheHitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslCacheHitRate.setStatus("mandatory")
_SslCacheEntries_Type = Gauge32
_SslCacheEntries_Object = MibScalar
sslCacheEntries = _SslCacheEntries_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 17, 2, 5),
    _SslCacheEntries_Type()
)
sslCacheEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslCacheEntries.setStatus("mandatory")
_SslCacheEntriesMax_Type = Gauge32
_SslCacheEntriesMax_Object = MibScalar
sslCacheEntriesMax = _SslCacheEntriesMax_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 17, 2, 6),
    _SslCacheEntriesMax_Type()
)
sslCacheEntriesMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslCacheEntriesMax.setStatus("mandatory")
_SslCacheOldest_Type = Gauge32
_SslCacheOldest_Object = MibScalar
sslCacheOldest = _SslCacheOldest_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 17, 2, 7),
    _SslCacheOldest_Type()
)
sslCacheOldest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslCacheOldest.setStatus("mandatory")
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
    aspSessionCacheHits.setStatus("mandatory")
_AspSessionCacheMisses_Type = Counter32
_AspSessionCacheMisses_Object = MibScalar
aspSessionCacheMisses = _AspSessionCacheMisses_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 17, 3, 2),
    _AspSessionCacheMisses_Type()
)
aspSessionCacheMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aspSessionCacheMisses.setStatus("mandatory")
_AspSessionCacheLookups_Type = Counter32
_AspSessionCacheLookups_Object = MibScalar
aspSessionCacheLookups = _AspSessionCacheLookups_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 17, 3, 3),
    _AspSessionCacheLookups_Type()
)
aspSessionCacheLookups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aspSessionCacheLookups.setStatus("mandatory")
_AspSessionCacheHitRate_Type = Gauge32
_AspSessionCacheHitRate_Object = MibScalar
aspSessionCacheHitRate = _AspSessionCacheHitRate_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 17, 3, 4),
    _AspSessionCacheHitRate_Type()
)
aspSessionCacheHitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aspSessionCacheHitRate.setStatus("mandatory")
_AspSessionCacheEntries_Type = Gauge32
_AspSessionCacheEntries_Object = MibScalar
aspSessionCacheEntries = _AspSessionCacheEntries_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 17, 3, 5),
    _AspSessionCacheEntries_Type()
)
aspSessionCacheEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aspSessionCacheEntries.setStatus("mandatory")
_AspSessionCacheEntriesMax_Type = Gauge32
_AspSessionCacheEntriesMax_Object = MibScalar
aspSessionCacheEntriesMax = _AspSessionCacheEntriesMax_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 17, 3, 6),
    _AspSessionCacheEntriesMax_Type()
)
aspSessionCacheEntriesMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aspSessionCacheEntriesMax.setStatus("mandatory")
_AspSessionCacheOldest_Type = Gauge32
_AspSessionCacheOldest_Object = MibScalar
aspSessionCacheOldest = _AspSessionCacheOldest_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 17, 3, 7),
    _AspSessionCacheOldest_Type()
)
aspSessionCacheOldest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aspSessionCacheOldest.setStatus("mandatory")
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
    ipSessionCacheHits.setStatus("mandatory")
_IpSessionCacheMisses_Type = Counter32
_IpSessionCacheMisses_Object = MibScalar
ipSessionCacheMisses = _IpSessionCacheMisses_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 17, 4, 2),
    _IpSessionCacheMisses_Type()
)
ipSessionCacheMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSessionCacheMisses.setStatus("mandatory")
_IpSessionCacheLookups_Type = Counter32
_IpSessionCacheLookups_Object = MibScalar
ipSessionCacheLookups = _IpSessionCacheLookups_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 17, 4, 3),
    _IpSessionCacheLookups_Type()
)
ipSessionCacheLookups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSessionCacheLookups.setStatus("mandatory")
_IpSessionCacheHitRate_Type = Gauge32
_IpSessionCacheHitRate_Object = MibScalar
ipSessionCacheHitRate = _IpSessionCacheHitRate_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 17, 4, 4),
    _IpSessionCacheHitRate_Type()
)
ipSessionCacheHitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSessionCacheHitRate.setStatus("mandatory")
_IpSessionCacheEntries_Type = Gauge32
_IpSessionCacheEntries_Object = MibScalar
ipSessionCacheEntries = _IpSessionCacheEntries_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 17, 4, 5),
    _IpSessionCacheEntries_Type()
)
ipSessionCacheEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSessionCacheEntries.setStatus("mandatory")
_IpSessionCacheEntriesMax_Type = Gauge32
_IpSessionCacheEntriesMax_Object = MibScalar
ipSessionCacheEntriesMax = _IpSessionCacheEntriesMax_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 17, 4, 6),
    _IpSessionCacheEntriesMax_Type()
)
ipSessionCacheEntriesMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSessionCacheEntriesMax.setStatus("mandatory")
_IpSessionCacheOldest_Type = Gauge32
_IpSessionCacheOldest_Object = MibScalar
ipSessionCacheOldest = _IpSessionCacheOldest_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 17, 4, 7),
    _IpSessionCacheOldest_Type()
)
ipSessionCacheOldest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSessionCacheOldest.setStatus("mandatory")
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
    j2eeSessionCacheHits.setStatus("mandatory")
_J2eeSessionCacheMisses_Type = Counter32
_J2eeSessionCacheMisses_Object = MibScalar
j2eeSessionCacheMisses = _J2eeSessionCacheMisses_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 17, 5, 2),
    _J2eeSessionCacheMisses_Type()
)
j2eeSessionCacheMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    j2eeSessionCacheMisses.setStatus("mandatory")
_J2eeSessionCacheLookups_Type = Counter32
_J2eeSessionCacheLookups_Object = MibScalar
j2eeSessionCacheLookups = _J2eeSessionCacheLookups_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 17, 5, 3),
    _J2eeSessionCacheLookups_Type()
)
j2eeSessionCacheLookups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    j2eeSessionCacheLookups.setStatus("mandatory")
_J2eeSessionCacheHitRate_Type = Gauge32
_J2eeSessionCacheHitRate_Object = MibScalar
j2eeSessionCacheHitRate = _J2eeSessionCacheHitRate_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 17, 5, 4),
    _J2eeSessionCacheHitRate_Type()
)
j2eeSessionCacheHitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    j2eeSessionCacheHitRate.setStatus("mandatory")
_J2eeSessionCacheEntries_Type = Gauge32
_J2eeSessionCacheEntries_Object = MibScalar
j2eeSessionCacheEntries = _J2eeSessionCacheEntries_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 17, 5, 5),
    _J2eeSessionCacheEntries_Type()
)
j2eeSessionCacheEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    j2eeSessionCacheEntries.setStatus("mandatory")
_J2eeSessionCacheEntriesMax_Type = Gauge32
_J2eeSessionCacheEntriesMax_Object = MibScalar
j2eeSessionCacheEntriesMax = _J2eeSessionCacheEntriesMax_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 17, 5, 6),
    _J2eeSessionCacheEntriesMax_Type()
)
j2eeSessionCacheEntriesMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    j2eeSessionCacheEntriesMax.setStatus("mandatory")
_J2eeSessionCacheOldest_Type = Gauge32
_J2eeSessionCacheOldest_Object = MibScalar
j2eeSessionCacheOldest = _J2eeSessionCacheOldest_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 17, 5, 7),
    _J2eeSessionCacheOldest_Type()
)
j2eeSessionCacheOldest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    j2eeSessionCacheOldest.setStatus("mandatory")
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
    uniSessionCacheHits.setStatus("mandatory")
_UniSessionCacheMisses_Type = Counter32
_UniSessionCacheMisses_Object = MibScalar
uniSessionCacheMisses = _UniSessionCacheMisses_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 17, 6, 2),
    _UniSessionCacheMisses_Type()
)
uniSessionCacheMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uniSessionCacheMisses.setStatus("mandatory")
_UniSessionCacheLookups_Type = Counter32
_UniSessionCacheLookups_Object = MibScalar
uniSessionCacheLookups = _UniSessionCacheLookups_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 17, 6, 3),
    _UniSessionCacheLookups_Type()
)
uniSessionCacheLookups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uniSessionCacheLookups.setStatus("mandatory")
_UniSessionCacheHitRate_Type = Gauge32
_UniSessionCacheHitRate_Object = MibScalar
uniSessionCacheHitRate = _UniSessionCacheHitRate_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 17, 6, 4),
    _UniSessionCacheHitRate_Type()
)
uniSessionCacheHitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uniSessionCacheHitRate.setStatus("mandatory")
_UniSessionCacheEntries_Type = Gauge32
_UniSessionCacheEntries_Object = MibScalar
uniSessionCacheEntries = _UniSessionCacheEntries_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 17, 6, 5),
    _UniSessionCacheEntries_Type()
)
uniSessionCacheEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uniSessionCacheEntries.setStatus("mandatory")
_UniSessionCacheEntriesMax_Type = Gauge32
_UniSessionCacheEntriesMax_Object = MibScalar
uniSessionCacheEntriesMax = _UniSessionCacheEntriesMax_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 17, 6, 6),
    _UniSessionCacheEntriesMax_Type()
)
uniSessionCacheEntriesMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uniSessionCacheEntriesMax.setStatus("mandatory")
_UniSessionCacheOldest_Type = Gauge32
_UniSessionCacheOldest_Object = MibScalar
uniSessionCacheOldest = _UniSessionCacheOldest_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 17, 6, 7),
    _UniSessionCacheOldest_Type()
)
uniSessionCacheOldest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uniSessionCacheOldest.setStatus("mandatory")
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
    sslSessionCacheHits.setStatus("mandatory")
_SslSessionCacheMisses_Type = Counter32
_SslSessionCacheMisses_Object = MibScalar
sslSessionCacheMisses = _SslSessionCacheMisses_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 17, 7, 2),
    _SslSessionCacheMisses_Type()
)
sslSessionCacheMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslSessionCacheMisses.setStatus("mandatory")
_SslSessionCacheLookups_Type = Counter32
_SslSessionCacheLookups_Object = MibScalar
sslSessionCacheLookups = _SslSessionCacheLookups_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 17, 7, 3),
    _SslSessionCacheLookups_Type()
)
sslSessionCacheLookups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslSessionCacheLookups.setStatus("mandatory")
_SslSessionCacheHitRate_Type = Gauge32
_SslSessionCacheHitRate_Object = MibScalar
sslSessionCacheHitRate = _SslSessionCacheHitRate_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 17, 7, 4),
    _SslSessionCacheHitRate_Type()
)
sslSessionCacheHitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslSessionCacheHitRate.setStatus("mandatory")
_SslSessionCacheEntries_Type = Gauge32
_SslSessionCacheEntries_Object = MibScalar
sslSessionCacheEntries = _SslSessionCacheEntries_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 17, 7, 5),
    _SslSessionCacheEntries_Type()
)
sslSessionCacheEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslSessionCacheEntries.setStatus("mandatory")
_SslSessionCacheEntriesMax_Type = Gauge32
_SslSessionCacheEntriesMax_Object = MibScalar
sslSessionCacheEntriesMax = _SslSessionCacheEntriesMax_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 17, 7, 6),
    _SslSessionCacheEntriesMax_Type()
)
sslSessionCacheEntriesMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslSessionCacheEntriesMax.setStatus("mandatory")
_SslSessionCacheOldest_Type = Gauge32
_SslSessionCacheOldest_Object = MibScalar
sslSessionCacheOldest = _SslSessionCacheOldest_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 17, 7, 7),
    _SslSessionCacheOldest_Type()
)
sslSessionCacheOldest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslSessionCacheOldest.setStatus("mandatory")
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
    ruleNumber.setStatus("mandatory")
_RuleTable_Object = MibTable
ruleTable = _RuleTable_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 18, 2)
)
if mibBuilder.loadTexts:
    ruleTable.setStatus("mandatory")
_RuleEntry_Object = MibTableRow
ruleEntry = _RuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 18, 2, 1)
)
ruleEntry.setIndexNames(
    (0, "ZXTM-MIB", "ruleName"),
)
if mibBuilder.loadTexts:
    ruleEntry.setStatus("mandatory")


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
    ruleName.setStatus("mandatory")
_RuleExecutions_Type = Counter32
_RuleExecutions_Object = MibTableColumn
ruleExecutions = _RuleExecutions_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 18, 2, 1, 2),
    _RuleExecutions_Type()
)
ruleExecutions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruleExecutions.setStatus("mandatory")
_RuleAborts_Type = Counter32
_RuleAborts_Object = MibTableColumn
ruleAborts = _RuleAborts_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 18, 2, 1, 3),
    _RuleAborts_Type()
)
ruleAborts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruleAborts.setStatus("mandatory")
_RuleResponds_Type = Counter32
_RuleResponds_Object = MibTableColumn
ruleResponds = _RuleResponds_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 18, 2, 1, 4),
    _RuleResponds_Type()
)
ruleResponds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruleResponds.setStatus("mandatory")
_RulePoolSelect_Type = Counter32
_RulePoolSelect_Object = MibTableColumn
rulePoolSelect = _RulePoolSelect_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 18, 2, 1, 5),
    _RulePoolSelect_Type()
)
rulePoolSelect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rulePoolSelect.setStatus("mandatory")
_RuleRetries_Type = Counter32
_RuleRetries_Object = MibTableColumn
ruleRetries = _RuleRetries_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 18, 2, 1, 6),
    _RuleRetries_Type()
)
ruleRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruleRetries.setStatus("mandatory")
_RuleDiscards_Type = Counter32
_RuleDiscards_Object = MibTableColumn
ruleDiscards = _RuleDiscards_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 18, 2, 1, 7),
    _RuleDiscards_Type()
)
ruleDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruleDiscards.setStatus("mandatory")
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
    monitorNumber.setStatus("mandatory")
_MonitorTable_Object = MibTable
monitorTable = _MonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 19, 2)
)
if mibBuilder.loadTexts:
    monitorTable.setStatus("mandatory")
_MonitorEntry_Object = MibTableRow
monitorEntry = _MonitorEntry_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 19, 2, 1)
)
monitorEntry.setIndexNames(
    (0, "ZXTM-MIB", "monitorName"),
)
if mibBuilder.loadTexts:
    monitorEntry.setStatus("mandatory")


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
    monitorName.setStatus("mandatory")
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
    licensekeyNumber.setStatus("mandatory")
_LicensekeyTable_Object = MibTable
licensekeyTable = _LicensekeyTable_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 20, 2)
)
if mibBuilder.loadTexts:
    licensekeyTable.setStatus("mandatory")
_LicensekeyEntry_Object = MibTableRow
licensekeyEntry = _LicensekeyEntry_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 20, 2, 1)
)
licensekeyEntry.setIndexNames(
    (0, "ZXTM-MIB", "licensekeyName"),
)
if mibBuilder.loadTexts:
    licensekeyEntry.setStatus("mandatory")


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
    licensekeyName.setStatus("mandatory")
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
    zxtmNumber.setStatus("mandatory")
_ZxtmTable_Object = MibTable
zxtmTable = _ZxtmTable_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 21, 2)
)
if mibBuilder.loadTexts:
    zxtmTable.setStatus("mandatory")
_ZxtmEntry_Object = MibTableRow
zxtmEntry = _ZxtmEntry_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 21, 2, 1)
)
zxtmEntry.setIndexNames(
    (0, "ZXTM-MIB", "zxtmName"),
)
if mibBuilder.loadTexts:
    zxtmEntry.setStatus("mandatory")


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
    zxtmName.setStatus("mandatory")
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
    fullLogLine.setStatus("mandatory")


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
    confName.setStatus("mandatory")


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
    customEventName.setStatus("mandatory")
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
    cloudcredentialsClassNumber.setStatus("mandatory")
_CloudcredentialsTable_Object = MibTable
cloudcredentialsTable = _CloudcredentialsTable_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 23, 2)
)
if mibBuilder.loadTexts:
    cloudcredentialsTable.setStatus("mandatory")
_CloudcredentialsEntry_Object = MibTableRow
cloudcredentialsEntry = _CloudcredentialsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 23, 2, 1)
)
cloudcredentialsEntry.setIndexNames(
    (0, "ZXTM-MIB", "cloudcredentialsName"),
)
if mibBuilder.loadTexts:
    cloudcredentialsEntry.setStatus("mandatory")


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
    cloudcredentialsName.setStatus("mandatory")
_CloudcredentialsStatusRequests_Type = Counter32
_CloudcredentialsStatusRequests_Object = MibTableColumn
cloudcredentialsStatusRequests = _CloudcredentialsStatusRequests_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 23, 2, 1, 2),
    _CloudcredentialsStatusRequests_Type()
)
cloudcredentialsStatusRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cloudcredentialsStatusRequests.setStatus("mandatory")
_CloudcredentialsNodeCreations_Type = Counter32
_CloudcredentialsNodeCreations_Object = MibTableColumn
cloudcredentialsNodeCreations = _CloudcredentialsNodeCreations_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 23, 2, 1, 3),
    _CloudcredentialsNodeCreations_Type()
)
cloudcredentialsNodeCreations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cloudcredentialsNodeCreations.setStatus("mandatory")
_CloudcredentialsNodeDeletions_Type = Counter32
_CloudcredentialsNodeDeletions_Object = MibTableColumn
cloudcredentialsNodeDeletions = _CloudcredentialsNodeDeletions_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 23, 2, 1, 4),
    _CloudcredentialsNodeDeletions_Type()
)
cloudcredentialsNodeDeletions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cloudcredentialsNodeDeletions.setStatus("mandatory")
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
    glbServiceNumber.setStatus("mandatory")
_GlbServiceTable_Object = MibTable
glbServiceTable = _GlbServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 24, 2)
)
if mibBuilder.loadTexts:
    glbServiceTable.setStatus("mandatory")
_GlbServiceEntry_Object = MibTableRow
glbServiceEntry = _GlbServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 24, 2, 1)
)
glbServiceEntry.setIndexNames(
    (0, "ZXTM-MIB", "glbServiceName"),
)
if mibBuilder.loadTexts:
    glbServiceEntry.setStatus("mandatory")


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
    glbServiceName.setStatus("mandatory")
_GlbServiceResponses_Type = Counter32
_GlbServiceResponses_Object = MibTableColumn
glbServiceResponses = _GlbServiceResponses_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 24, 2, 1, 2),
    _GlbServiceResponses_Type()
)
glbServiceResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    glbServiceResponses.setStatus("mandatory")
_GlbServiceUnmodified_Type = Counter32
_GlbServiceUnmodified_Object = MibTableColumn
glbServiceUnmodified = _GlbServiceUnmodified_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 24, 2, 1, 3),
    _GlbServiceUnmodified_Type()
)
glbServiceUnmodified.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    glbServiceUnmodified.setStatus("mandatory")
_GlbServiceDiscarded_Type = Counter32
_GlbServiceDiscarded_Object = MibTableColumn
glbServiceDiscarded = _GlbServiceDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 24, 2, 1, 4),
    _GlbServiceDiscarded_Type()
)
glbServiceDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    glbServiceDiscarded.setStatus("mandatory")
_Perlocationservices_ObjectIdentity = ObjectIdentity
perlocationservices = _Perlocationservices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 25)
)
_PerLocationServiceTable_Object = MibTable
perLocationServiceTable = _PerLocationServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 25, 1)
)
if mibBuilder.loadTexts:
    perLocationServiceTable.setStatus("mandatory")
_PerLocationServiceEntry_Object = MibTableRow
perLocationServiceEntry = _PerLocationServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 25, 1, 1)
)
perLocationServiceEntry.setIndexNames(
    (0, "ZXTM-MIB", "perLocationServiceLocationName"),
    (0, "ZXTM-MIB", "perLocationServiceName"),
)
if mibBuilder.loadTexts:
    perLocationServiceEntry.setStatus("mandatory")


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
    perLocationServiceLocationName.setStatus("mandatory")


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
    perLocationServiceLocationCode.setStatus("mandatory")


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
    perLocationServiceName.setStatus("mandatory")


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
    perLocationServiceDraining.setStatus("mandatory")


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
    perLocationServiceState.setStatus("mandatory")


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
    perLocationServiceFrontendState.setStatus("mandatory")


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
    perLocationServiceMonitorState.setStatus("mandatory")
_PerLocationServiceLoad_Type = Gauge32
_PerLocationServiceLoad_Object = MibTableColumn
perLocationServiceLoad = _PerLocationServiceLoad_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 25, 1, 1, 8),
    _PerLocationServiceLoad_Type()
)
perLocationServiceLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perLocationServiceLoad.setStatus("mandatory")
_PerLocationServiceResponses_Type = Counter32
_PerLocationServiceResponses_Object = MibTableColumn
perLocationServiceResponses = _PerLocationServiceResponses_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 25, 1, 1, 9),
    _PerLocationServiceResponses_Type()
)
perLocationServiceResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perLocationServiceResponses.setStatus("mandatory")
_Locations_ObjectIdentity = ObjectIdentity
locations = _Locations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 26)
)
_LocationTable_Object = MibTable
locationTable = _LocationTable_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 26, 1)
)
if mibBuilder.loadTexts:
    locationTable.setStatus("mandatory")
_LocationEntry_Object = MibTableRow
locationEntry = _LocationEntry_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 26, 1, 1)
)
locationEntry.setIndexNames(
    (0, "ZXTM-MIB", "locationName"),
)
if mibBuilder.loadTexts:
    locationEntry.setStatus("mandatory")


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
    locationName.setStatus("mandatory")


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
    locationCode.setStatus("mandatory")
_LocationLoad_Type = Gauge32
_LocationLoad_Object = MibTableColumn
locationLoad = _LocationLoad_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 26, 1, 1, 3),
    _LocationLoad_Type()
)
locationLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locationLoad.setStatus("mandatory")
_LocationResponses_Type = Counter32
_LocationResponses_Object = MibTableColumn
locationResponses = _LocationResponses_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 26, 1, 1, 4),
    _LocationResponses_Type()
)
locationResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locationResponses.setStatus("mandatory")
_Listenips_ObjectIdentity = ObjectIdentity
listenips = _Listenips_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 27)
)
_ListenIPTable_Object = MibTable
listenIPTable = _ListenIPTable_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 27, 2)
)
if mibBuilder.loadTexts:
    listenIPTable.setStatus("mandatory")
_ListenIPEntry_Object = MibTableRow
listenIPEntry = _ListenIPEntry_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 27, 2, 1)
)
listenIPEntry.setIndexNames(
    (0, "ZXTM-MIB", "listenIPAddressType"),
    (0, "ZXTM-MIB", "listenIPAddress"),
)
if mibBuilder.loadTexts:
    listenIPEntry.setStatus("mandatory")
_ListenIPAddressType_Type = InetAddressType
_ListenIPAddressType_Object = MibTableColumn
listenIPAddressType = _ListenIPAddressType_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 27, 2, 1, 1),
    _ListenIPAddressType_Type()
)
listenIPAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    listenIPAddressType.setStatus("mandatory")


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
    listenIPAddress.setStatus("mandatory")
_ListenIPBytesInLo_Type = Counter32
_ListenIPBytesInLo_Object = MibTableColumn
listenIPBytesInLo = _ListenIPBytesInLo_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 27, 2, 1, 3),
    _ListenIPBytesInLo_Type()
)
listenIPBytesInLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    listenIPBytesInLo.setStatus("mandatory")
_ListenIPBytesInHi_Type = Counter32
_ListenIPBytesInHi_Object = MibTableColumn
listenIPBytesInHi = _ListenIPBytesInHi_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 27, 2, 1, 4),
    _ListenIPBytesInHi_Type()
)
listenIPBytesInHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    listenIPBytesInHi.setStatus("mandatory")
_ListenIPBytesOutLo_Type = Counter32
_ListenIPBytesOutLo_Object = MibTableColumn
listenIPBytesOutLo = _ListenIPBytesOutLo_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 27, 2, 1, 5),
    _ListenIPBytesOutLo_Type()
)
listenIPBytesOutLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    listenIPBytesOutLo.setStatus("mandatory")
_ListenIPBytesOutHi_Type = Counter32
_ListenIPBytesOutHi_Object = MibTableColumn
listenIPBytesOutHi = _ListenIPBytesOutHi_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 27, 2, 1, 6),
    _ListenIPBytesOutHi_Type()
)
listenIPBytesOutHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    listenIPBytesOutHi.setStatus("mandatory")
_ListenIPCurrentConn_Type = Gauge32
_ListenIPCurrentConn_Object = MibTableColumn
listenIPCurrentConn = _ListenIPCurrentConn_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 27, 2, 1, 7),
    _ListenIPCurrentConn_Type()
)
listenIPCurrentConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    listenIPCurrentConn.setStatus("mandatory")
_ListenIPTotalConn_Type = Counter32
_ListenIPTotalConn_Object = MibTableColumn
listenIPTotalConn = _ListenIPTotalConn_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 27, 2, 1, 8),
    _ListenIPTotalConn_Type()
)
listenIPTotalConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    listenIPTotalConn.setStatus("mandatory")
_ListenIPMaxConn_Type = Gauge32
_ListenIPMaxConn_Object = MibTableColumn
listenIPMaxConn = _ListenIPMaxConn_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 27, 2, 1, 9),
    _ListenIPMaxConn_Type()
)
listenIPMaxConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    listenIPMaxConn.setStatus("mandatory")
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
    authenticatorNumber.setStatus("mandatory")
_AuthenticatorTable_Object = MibTable
authenticatorTable = _AuthenticatorTable_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 28, 2)
)
if mibBuilder.loadTexts:
    authenticatorTable.setStatus("mandatory")
_AuthenticatorEntry_Object = MibTableRow
authenticatorEntry = _AuthenticatorEntry_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 28, 2, 1)
)
authenticatorEntry.setIndexNames(
    (0, "ZXTM-MIB", "authenticatorName"),
)
if mibBuilder.loadTexts:
    authenticatorEntry.setStatus("mandatory")


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
    authenticatorName.setStatus("mandatory")
_AuthenticatorRequests_Type = Counter32
_AuthenticatorRequests_Object = MibTableColumn
authenticatorRequests = _AuthenticatorRequests_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 28, 2, 1, 2),
    _AuthenticatorRequests_Type()
)
authenticatorRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authenticatorRequests.setStatus("mandatory")
_AuthenticatorPasses_Type = Counter32
_AuthenticatorPasses_Object = MibTableColumn
authenticatorPasses = _AuthenticatorPasses_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 28, 2, 1, 3),
    _AuthenticatorPasses_Type()
)
authenticatorPasses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authenticatorPasses.setStatus("mandatory")
_AuthenticatorFails_Type = Counter32
_AuthenticatorFails_Object = MibTableColumn
authenticatorFails = _AuthenticatorFails_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 28, 2, 1, 4),
    _AuthenticatorFails_Type()
)
authenticatorFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authenticatorFails.setStatus("mandatory")
_AuthenticatorErrors_Type = Counter32
_AuthenticatorErrors_Object = MibTableColumn
authenticatorErrors = _AuthenticatorErrors_Object(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 28, 2, 1, 5),
    _AuthenticatorErrors_Type()
)
authenticatorErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authenticatorErrors.setStatus("mandatory")

# Managed Objects groups


# Notification objects

testaction = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 1)
)
testaction.setObjects(
      *(("ZXTM-MIB", "fullLogLine"),
        ("ZXTM-MIB", "actionName"))
)
if mibBuilder.loadTexts:
    testaction.setStatus(
        ""
    )

running = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 2)
)
running.setObjects(
    ("ZXTM-MIB", "fullLogLine")
)
if mibBuilder.loadTexts:
    running.setStatus(
        ""
    )

fewfreefds = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 3)
)
fewfreefds.setObjects(
    ("ZXTM-MIB", "fullLogLine")
)
if mibBuilder.loadTexts:
    fewfreefds.setStatus(
        ""
    )

restartrequired = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 4)
)
restartrequired.setObjects(
    ("ZXTM-MIB", "fullLogLine")
)
if mibBuilder.loadTexts:
    restartrequired.setStatus(
        ""
    )

timemovedback = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 5)
)
timemovedback.setObjects(
    ("ZXTM-MIB", "fullLogLine")
)
if mibBuilder.loadTexts:
    timemovedback.setStatus(
        ""
    )

sslfail = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 6)
)
sslfail.setObjects(
    ("ZXTM-MIB", "fullLogLine")
)
if mibBuilder.loadTexts:
    sslfail.setStatus(
        ""
    )

hardware = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 7)
)
hardware.setObjects(
    ("ZXTM-MIB", "fullLogLine")
)
if mibBuilder.loadTexts:
    hardware.setStatus(
        ""
    )

zxtmswerror = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 8)
)
zxtmswerror.setObjects(
    ("ZXTM-MIB", "fullLogLine")
)
if mibBuilder.loadTexts:
    zxtmswerror.setStatus(
        ""
    )

customevent = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 9)
)
customevent.setObjects(
      *(("ZXTM-MIB", "fullLogLine"),
        ("ZXTM-MIB", "customEventName"))
)
if mibBuilder.loadTexts:
    customevent.setStatus(
        ""
    )

versionmismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 10)
)
versionmismatch.setObjects(
    ("ZXTM-MIB", "fullLogLine")
)
if mibBuilder.loadTexts:
    versionmismatch.setStatus(
        ""
    )

machineok = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 11)
)
machineok.setObjects(
      *(("ZXTM-MIB", "fullLogLine"),
        ("ZXTM-MIB", "zxtmName"))
)
if mibBuilder.loadTexts:
    machineok.setStatus(
        ""
    )

machinetimeout = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 12)
)
machinetimeout.setObjects(
      *(("ZXTM-MIB", "fullLogLine"),
        ("ZXTM-MIB", "zxtmName"))
)
if mibBuilder.loadTexts:
    machinetimeout.setStatus(
        ""
    )

machinefail = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 13)
)
machinefail.setObjects(
      *(("ZXTM-MIB", "fullLogLine"),
        ("ZXTM-MIB", "zxtmName"))
)
if mibBuilder.loadTexts:
    machinefail.setStatus(
        ""
    )

allmachinesok = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 14)
)
allmachinesok.setObjects(
    ("ZXTM-MIB", "fullLogLine")
)
if mibBuilder.loadTexts:
    allmachinesok.setStatus(
        ""
    )

flipperbackendsworking = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 15)
)
flipperbackendsworking.setObjects(
    ("ZXTM-MIB", "fullLogLine")
)
if mibBuilder.loadTexts:
    flipperbackendsworking.setStatus(
        ""
    )

flipperfrontendsworking = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 16)
)
flipperfrontendsworking.setObjects(
    ("ZXTM-MIB", "fullLogLine")
)
if mibBuilder.loadTexts:
    flipperfrontendsworking.setStatus(
        ""
    )

pingbackendfail = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 17)
)
pingbackendfail.setObjects(
    ("ZXTM-MIB", "fullLogLine")
)
if mibBuilder.loadTexts:
    pingbackendfail.setStatus(
        ""
    )

pingfrontendfail = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 18)
)
pingfrontendfail.setObjects(
    ("ZXTM-MIB", "fullLogLine")
)
if mibBuilder.loadTexts:
    pingfrontendfail.setStatus(
        ""
    )

pinggwfail = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 19)
)
pinggwfail.setObjects(
    ("ZXTM-MIB", "fullLogLine")
)
if mibBuilder.loadTexts:
    pinggwfail.setStatus(
        ""
    )

statebaddata = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 20)
)
statebaddata.setObjects(
    ("ZXTM-MIB", "fullLogLine")
)
if mibBuilder.loadTexts:
    statebaddata.setStatus(
        ""
    )

stateconnfail = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 21)
)
stateconnfail.setObjects(
    ("ZXTM-MIB", "fullLogLine")
)
if mibBuilder.loadTexts:
    stateconnfail.setStatus(
        ""
    )

stateok = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 22)
)
stateok.setObjects(
    ("ZXTM-MIB", "fullLogLine")
)
if mibBuilder.loadTexts:
    stateok.setStatus(
        ""
    )

statereadfail = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 23)
)
statereadfail.setObjects(
    ("ZXTM-MIB", "fullLogLine")
)
if mibBuilder.loadTexts:
    statereadfail.setStatus(
        ""
    )

statetimeout = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 24)
)
statetimeout.setObjects(
    ("ZXTM-MIB", "fullLogLine")
)
if mibBuilder.loadTexts:
    statetimeout.setStatus(
        ""
    )

stateunexpected = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 25)
)
stateunexpected.setObjects(
    ("ZXTM-MIB", "fullLogLine")
)
if mibBuilder.loadTexts:
    stateunexpected.setStatus(
        ""
    )

statewritefail = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 26)
)
statewritefail.setObjects(
    ("ZXTM-MIB", "fullLogLine")
)
if mibBuilder.loadTexts:
    statewritefail.setStatus(
        ""
    )

sslhwfail = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 27)
)
sslhwfail.setObjects(
    ("ZXTM-MIB", "fullLogLine")
)
if mibBuilder.loadTexts:
    sslhwfail.setStatus(
        ""
    )

sslhwrestart = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 28)
)
sslhwrestart.setObjects(
    ("ZXTM-MIB", "fullLogLine")
)
if mibBuilder.loadTexts:
    sslhwrestart.setStatus(
        ""
    )

sslhwstart = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 29)
)
sslhwstart.setObjects(
    ("ZXTM-MIB", "fullLogLine")
)
if mibBuilder.loadTexts:
    sslhwstart.setStatus(
        ""
    )

confdel = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 30)
)
confdel.setObjects(
      *(("ZXTM-MIB", "fullLogLine"),
        ("ZXTM-MIB", "confName"))
)
if mibBuilder.loadTexts:
    confdel.setStatus(
        ""
    )

confmod = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 31)
)
confmod.setObjects(
      *(("ZXTM-MIB", "fullLogLine"),
        ("ZXTM-MIB", "confName"))
)
if mibBuilder.loadTexts:
    confmod.setStatus(
        ""
    )

confadd = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 32)
)
confadd.setObjects(
      *(("ZXTM-MIB", "fullLogLine"),
        ("ZXTM-MIB", "confName"))
)
if mibBuilder.loadTexts:
    confadd.setStatus(
        ""
    )

confok = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 33)
)
confok.setObjects(
      *(("ZXTM-MIB", "fullLogLine"),
        ("ZXTM-MIB", "confName"))
)
if mibBuilder.loadTexts:
    confok.setStatus(
        ""
    )

javadied = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 34)
)
javadied.setObjects(
    ("ZXTM-MIB", "fullLogLine")
)
if mibBuilder.loadTexts:
    javadied.setStatus(
        ""
    )

javastop = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 35)
)
javastop.setObjects(
    ("ZXTM-MIB", "fullLogLine")
)
if mibBuilder.loadTexts:
    javastop.setStatus(
        ""
    )

javastartfail = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 36)
)
javastartfail.setObjects(
    ("ZXTM-MIB", "fullLogLine")
)
if mibBuilder.loadTexts:
    javastartfail.setStatus(
        ""
    )

javaterminatefail = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 37)
)
javaterminatefail.setObjects(
    ("ZXTM-MIB", "fullLogLine")
)
if mibBuilder.loadTexts:
    javaterminatefail.setStatus(
        ""
    )

javanotfound = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 38)
)
javanotfound.setObjects(
    ("ZXTM-MIB", "fullLogLine")
)
if mibBuilder.loadTexts:
    javanotfound.setStatus(
        ""
    )

javastarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 39)
)
javastarted.setObjects(
    ("ZXTM-MIB", "fullLogLine")
)
if mibBuilder.loadTexts:
    javastarted.setStatus(
        ""
    )

servleterror = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 40)
)
servleterror.setObjects(
    ("ZXTM-MIB", "fullLogLine")
)
if mibBuilder.loadTexts:
    servleterror.setStatus(
        ""
    )

monitorfail = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 41)
)
monitorfail.setObjects(
      *(("ZXTM-MIB", "fullLogLine"),
        ("ZXTM-MIB", "monitorName"))
)
if mibBuilder.loadTexts:
    monitorfail.setStatus(
        ""
    )

monitorok = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 42)
)
monitorok.setObjects(
      *(("ZXTM-MIB", "fullLogLine"),
        ("ZXTM-MIB", "monitorName"))
)
if mibBuilder.loadTexts:
    monitorok.setStatus(
        ""
    )

rulexmlerr = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 43)
)
rulexmlerr.setObjects(
      *(("ZXTM-MIB", "fullLogLine"),
        ("ZXTM-MIB", "ruleName"))
)
if mibBuilder.loadTexts:
    rulexmlerr.setStatus(
        ""
    )

pooluseunknown = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 44)
)
pooluseunknown.setObjects(
      *(("ZXTM-MIB", "fullLogLine"),
        ("ZXTM-MIB", "ruleName"))
)
if mibBuilder.loadTexts:
    pooluseunknown.setStatus(
        ""
    )

ruleabort = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 45)
)
ruleabort.setObjects(
      *(("ZXTM-MIB", "fullLogLine"),
        ("ZXTM-MIB", "ruleName"))
)
if mibBuilder.loadTexts:
    ruleabort.setStatus(
        ""
    )

rulebufferlarge = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 46)
)
rulebufferlarge.setObjects(
      *(("ZXTM-MIB", "fullLogLine"),
        ("ZXTM-MIB", "ruleName"))
)
if mibBuilder.loadTexts:
    rulebufferlarge.setStatus(
        ""
    )

rulebodycomperror = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 47)
)
rulebodycomperror.setObjects(
      *(("ZXTM-MIB", "fullLogLine"),
        ("ZXTM-MIB", "ruleName"))
)
if mibBuilder.loadTexts:
    rulebodycomperror.setStatus(
        ""
    )

forwardproxybadhost = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 48)
)
forwardproxybadhost.setObjects(
      *(("ZXTM-MIB", "fullLogLine"),
        ("ZXTM-MIB", "ruleName"))
)
if mibBuilder.loadTexts:
    forwardproxybadhost.setStatus(
        ""
    )

invalidemit = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 49)
)
invalidemit.setObjects(
      *(("ZXTM-MIB", "fullLogLine"),
        ("ZXTM-MIB", "ruleName"))
)
if mibBuilder.loadTexts:
    invalidemit.setStatus(
        ""
    )

rulenopersistence = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 50)
)
rulenopersistence.setObjects(
      *(("ZXTM-MIB", "fullLogLine"),
        ("ZXTM-MIB", "ruleName"))
)
if mibBuilder.loadTexts:
    rulenopersistence.setStatus(
        ""
    )

rulelogmsginfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 51)
)
rulelogmsginfo.setObjects(
      *(("ZXTM-MIB", "fullLogLine"),
        ("ZXTM-MIB", "ruleName"))
)
if mibBuilder.loadTexts:
    rulelogmsginfo.setStatus(
        ""
    )

rulelogmsgwarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 52)
)
rulelogmsgwarn.setObjects(
      *(("ZXTM-MIB", "fullLogLine"),
        ("ZXTM-MIB", "ruleName"))
)
if mibBuilder.loadTexts:
    rulelogmsgwarn.setStatus(
        ""
    )

rulelogmsgserious = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 53)
)
rulelogmsgserious.setObjects(
      *(("ZXTM-MIB", "fullLogLine"),
        ("ZXTM-MIB", "ruleName"))
)
if mibBuilder.loadTexts:
    rulelogmsgserious.setStatus(
        ""
    )

norate = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 54)
)
norate.setObjects(
      *(("ZXTM-MIB", "fullLogLine"),
        ("ZXTM-MIB", "ruleName"))
)
if mibBuilder.loadTexts:
    norate.setStatus(
        ""
    )

poolactivenodesunknown = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 55)
)
poolactivenodesunknown.setObjects(
      *(("ZXTM-MIB", "fullLogLine"),
        ("ZXTM-MIB", "ruleName"))
)
if mibBuilder.loadTexts:
    poolactivenodesunknown.setStatus(
        ""
    )

datastorefull = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 56)
)
datastorefull.setObjects(
    ("ZXTM-MIB", "fullLogLine")
)
if mibBuilder.loadTexts:
    datastorefull.setStatus(
        ""
    )

expired = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 57)
)
expired.setObjects(
      *(("ZXTM-MIB", "fullLogLine"),
        ("ZXTM-MIB", "licensekeyName"))
)
if mibBuilder.loadTexts:
    expired.setStatus(
        ""
    )

licensecorrupt = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 58)
)
licensecorrupt.setObjects(
      *(("ZXTM-MIB", "fullLogLine"),
        ("ZXTM-MIB", "licensekeyName"))
)
if mibBuilder.loadTexts:
    licensecorrupt.setStatus(
        ""
    )

expiresoon = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 59)
)
expiresoon.setObjects(
      *(("ZXTM-MIB", "fullLogLine"),
        ("ZXTM-MIB", "licensekeyName"))
)
if mibBuilder.loadTexts:
    expiresoon.setStatus(
        ""
    )

usinglicense = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 60)
)
usinglicense.setObjects(
      *(("ZXTM-MIB", "fullLogLine"),
        ("ZXTM-MIB", "licensekeyName"))
)
if mibBuilder.loadTexts:
    usinglicense.setStatus(
        ""
    )

licenseclustertoobig = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 61)
)
licenseclustertoobig.setObjects(
    ("ZXTM-MIB", "fullLogLine")
)
if mibBuilder.loadTexts:
    licenseclustertoobig.setStatus(
        ""
    )

unlicensed = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 62)
)
unlicensed.setObjects(
    ("ZXTM-MIB", "fullLogLine")
)
if mibBuilder.loadTexts:
    unlicensed.setStatus(
        ""
    )

usingdevlicense = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 63)
)
usingdevlicense.setObjects(
    ("ZXTM-MIB", "fullLogLine")
)
if mibBuilder.loadTexts:
    usingdevlicense.setStatus(
        ""
    )

poolnonodes = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 64)
)
poolnonodes.setObjects(
      *(("ZXTM-MIB", "fullLogLine"),
        ("ZXTM-MIB", "poolName"))
)
if mibBuilder.loadTexts:
    poolnonodes.setStatus(
        ""
    )

poolok = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 65)
)
poolok.setObjects(
      *(("ZXTM-MIB", "fullLogLine"),
        ("ZXTM-MIB", "poolName"))
)
if mibBuilder.loadTexts:
    poolok.setStatus(
        ""
    )

pooldied = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 66)
)
pooldied.setObjects(
      *(("ZXTM-MIB", "fullLogLine"),
        ("ZXTM-MIB", "poolName"))
)
if mibBuilder.loadTexts:
    pooldied.setStatus(
        ""
    )

noderesolvefailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 67)
)
noderesolvefailure.setObjects(
      *(("ZXTM-MIB", "fullLogLine"),
        ("ZXTM-MIB", "poolName"))
)
if mibBuilder.loadTexts:
    noderesolvefailure.setStatus(
        ""
    )

noderesolvemultiple = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 68)
)
noderesolvemultiple.setObjects(
      *(("ZXTM-MIB", "fullLogLine"),
        ("ZXTM-MIB", "poolName"))
)
if mibBuilder.loadTexts:
    noderesolvemultiple.setStatus(
        ""
    )

nodeworking = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 69)
)
nodeworking.setObjects(
      *(("ZXTM-MIB", "fullLogLine"),
        ("ZXTM-MIB", "perPoolNodePoolName"),
        ("ZXTM-MIB", "perPoolNodeNodeAddressType"),
        ("ZXTM-MIB", "perPoolNodeNodeAddress"),
        ("ZXTM-MIB", "perPoolNodeNodePort"))
)
if mibBuilder.loadTexts:
    nodeworking.setStatus(
        ""
    )

nostarttls = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 70)
)
nostarttls.setObjects(
      *(("ZXTM-MIB", "fullLogLine"),
        ("ZXTM-MIB", "perPoolNodePoolName"),
        ("ZXTM-MIB", "perPoolNodeNodeAddressType"),
        ("ZXTM-MIB", "perPoolNodeNodeAddress"),
        ("ZXTM-MIB", "perPoolNodeNodePort"))
)
if mibBuilder.loadTexts:
    nostarttls.setStatus(
        ""
    )

nodefail = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 71)
)
nodefail.setObjects(
      *(("ZXTM-MIB", "fullLogLine"),
        ("ZXTM-MIB", "perPoolNodePoolName"),
        ("ZXTM-MIB", "perPoolNodeNodeAddressType"),
        ("ZXTM-MIB", "perPoolNodeNodeAddress"),
        ("ZXTM-MIB", "perPoolNodeNodePort"))
)
if mibBuilder.loadTexts:
    nodefail.setStatus(
        ""
    )

starttlsinvalid = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 72)
)
starttlsinvalid.setObjects(
      *(("ZXTM-MIB", "fullLogLine"),
        ("ZXTM-MIB", "perPoolNodePoolName"),
        ("ZXTM-MIB", "perPoolNodeNodeAddressType"),
        ("ZXTM-MIB", "perPoolNodeNodeAddress"),
        ("ZXTM-MIB", "perPoolNodeNodePort"))
)
if mibBuilder.loadTexts:
    starttlsinvalid.setStatus(
        ""
    )

ehloinvalid = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 73)
)
ehloinvalid.setObjects(
      *(("ZXTM-MIB", "fullLogLine"),
        ("ZXTM-MIB", "perPoolNodePoolName"),
        ("ZXTM-MIB", "perPoolNodeNodeAddressType"),
        ("ZXTM-MIB", "perPoolNodeNodeAddress"),
        ("ZXTM-MIB", "perPoolNodeNodePort"))
)
if mibBuilder.loadTexts:
    ehloinvalid.setStatus(
        ""
    )

flipperraiselocalworking = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 74)
)
flipperraiselocalworking.setObjects(
      *(("ZXTM-MIB", "fullLogLine"),
        ("ZXTM-MIB", "trafficIPInet46AddressType"),
        ("ZXTM-MIB", "trafficIPInet46Address"))
)
if mibBuilder.loadTexts:
    flipperraiselocalworking.setStatus(
        ""
    )

flipperraiseothersdead = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 75)
)
flipperraiseothersdead.setObjects(
      *(("ZXTM-MIB", "fullLogLine"),
        ("ZXTM-MIB", "trafficIPInet46AddressType"),
        ("ZXTM-MIB", "trafficIPInet46Address"))
)
if mibBuilder.loadTexts:
    flipperraiseothersdead.setStatus(
        ""
    )

flipperraiseosdrop = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 76)
)
flipperraiseosdrop.setObjects(
      *(("ZXTM-MIB", "fullLogLine"),
        ("ZXTM-MIB", "trafficIPInet46AddressType"),
        ("ZXTM-MIB", "trafficIPInet46Address"))
)
if mibBuilder.loadTexts:
    flipperraiseosdrop.setStatus(
        ""
    )

dropipinfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 77)
)
dropipinfo.setObjects(
      *(("ZXTM-MIB", "fullLogLine"),
        ("ZXTM-MIB", "trafficIPInet46AddressType"),
        ("ZXTM-MIB", "trafficIPInet46Address"))
)
if mibBuilder.loadTexts:
    dropipinfo.setStatus(
        ""
    )

dropipwarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 78)
)
dropipwarn.setObjects(
      *(("ZXTM-MIB", "fullLogLine"),
        ("ZXTM-MIB", "trafficIPInet46AddressType"),
        ("ZXTM-MIB", "trafficIPInet46Address"))
)
if mibBuilder.loadTexts:
    dropipwarn.setStatus(
        ""
    )

flipperdadreraise = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 79)
)
flipperdadreraise.setObjects(
      *(("ZXTM-MIB", "fullLogLine"),
        ("ZXTM-MIB", "trafficIPInet46AddressType"),
        ("ZXTM-MIB", "trafficIPInet46Address"))
)
if mibBuilder.loadTexts:
    flipperdadreraise.setStatus(
        ""
    )

flipperipexists = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 80)
)
flipperipexists.setObjects(
      *(("ZXTM-MIB", "fullLogLine"),
        ("ZXTM-MIB", "trafficIPInet46AddressType"),
        ("ZXTM-MIB", "trafficIPInet46Address"))
)
if mibBuilder.loadTexts:
    flipperipexists.setStatus(
        ""
    )

triggersummary = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 81)
)
triggersummary.setObjects(
      *(("ZXTM-MIB", "fullLogLine"),
        ("ZXTM-MIB", "serviceProtName"))
)
if mibBuilder.loadTexts:
    triggersummary.setStatus(
        ""
    )

slmclasslimitexceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 82)
)
slmclasslimitexceeded.setObjects(
    ("ZXTM-MIB", "fullLogLine")
)
if mibBuilder.loadTexts:
    slmclasslimitexceeded.setStatus(
        ""
    )

slmrecoveredwarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 83)
)
slmrecoveredwarn.setObjects(
      *(("ZXTM-MIB", "fullLogLine"),
        ("ZXTM-MIB", "serviceLevelName"))
)
if mibBuilder.loadTexts:
    slmrecoveredwarn.setStatus(
        ""
    )

slmrecoveredserious = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 84)
)
slmrecoveredserious.setObjects(
      *(("ZXTM-MIB", "fullLogLine"),
        ("ZXTM-MIB", "serviceLevelName"))
)
if mibBuilder.loadTexts:
    slmrecoveredserious.setStatus(
        ""
    )

slmfallenbelowwarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 85)
)
slmfallenbelowwarn.setObjects(
      *(("ZXTM-MIB", "fullLogLine"),
        ("ZXTM-MIB", "serviceLevelName"))
)
if mibBuilder.loadTexts:
    slmfallenbelowwarn.setStatus(
        ""
    )

slmfallenbelowserious = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 86)
)
slmfallenbelowserious.setObjects(
      *(("ZXTM-MIB", "fullLogLine"),
        ("ZXTM-MIB", "serviceLevelName"))
)
if mibBuilder.loadTexts:
    slmfallenbelowserious.setStatus(
        ""
    )

vscrloutofdate = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 87)
)
vscrloutofdate.setObjects(
    ("ZXTM-MIB", "fullLogLine")
)
if mibBuilder.loadTexts:
    vscrloutofdate.setStatus(
        ""
    )

vsstart = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 88)
)
vsstart.setObjects(
      *(("ZXTM-MIB", "fullLogLine"),
        ("ZXTM-MIB", "virtualserverName"))
)
if mibBuilder.loadTexts:
    vsstart.setStatus(
        ""
    )

vsstop = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 89)
)
vsstop.setObjects(
      *(("ZXTM-MIB", "fullLogLine"),
        ("ZXTM-MIB", "virtualserverName"))
)
if mibBuilder.loadTexts:
    vsstop.setStatus(
        ""
    )

privkeyok = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 90)
)
privkeyok.setObjects(
      *(("ZXTM-MIB", "fullLogLine"),
        ("ZXTM-MIB", "virtualserverName"))
)
if mibBuilder.loadTexts:
    privkeyok.setStatus(
        ""
    )

ssldrop = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 91)
)
ssldrop.setObjects(
      *(("ZXTM-MIB", "fullLogLine"),
        ("ZXTM-MIB", "virtualserverName"))
)
if mibBuilder.loadTexts:
    ssldrop.setStatus(
        ""
    )

vslogwritefail = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 92)
)
vslogwritefail.setObjects(
      *(("ZXTM-MIB", "fullLogLine"),
        ("ZXTM-MIB", "virtualserverName"))
)
if mibBuilder.loadTexts:
    vslogwritefail.setStatus(
        ""
    )

vssslcertexpired = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 93)
)
vssslcertexpired.setObjects(
      *(("ZXTM-MIB", "fullLogLine"),
        ("ZXTM-MIB", "virtualserverName"))
)
if mibBuilder.loadTexts:
    vssslcertexpired.setStatus(
        ""
    )

vssslcerttoexpire = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 94)
)
vssslcerttoexpire.setObjects(
      *(("ZXTM-MIB", "fullLogLine"),
        ("ZXTM-MIB", "virtualserverName"))
)
if mibBuilder.loadTexts:
    vssslcerttoexpire.setStatus(
        ""
    )

vscacertexpired = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 95)
)
vscacertexpired.setObjects(
      *(("ZXTM-MIB", "fullLogLine"),
        ("ZXTM-MIB", "virtualserverName"))
)
if mibBuilder.loadTexts:
    vscacertexpired.setStatus(
        ""
    )

vscacerttoexpire = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 96)
)
vscacerttoexpire.setObjects(
      *(("ZXTM-MIB", "fullLogLine"),
        ("ZXTM-MIB", "virtualserverName"))
)
if mibBuilder.loadTexts:
    vscacerttoexpire.setStatus(
        ""
    )

maxclientbufferdrop = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 97)
)
maxclientbufferdrop.setObjects(
    ("ZXTM-MIB", "fullLogLine")
)
if mibBuilder.loadTexts:
    maxclientbufferdrop.setStatus(
        ""
    )

respcompfail = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 98)
)
respcompfail.setObjects(
    ("ZXTM-MIB", "fullLogLine")
)
if mibBuilder.loadTexts:
    respcompfail.setStatus(
        ""
    )

responsetoolarge = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 99)
)
responsetoolarge.setObjects(
    ("ZXTM-MIB", "fullLogLine")
)
if mibBuilder.loadTexts:
    responsetoolarge.setStatus(
        ""
    )

sipstreamnoports = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 100)
)
sipstreamnoports.setObjects(
    ("ZXTM-MIB", "fullLogLine")
)
if mibBuilder.loadTexts:
    sipstreamnoports.setStatus(
        ""
    )

rtspstreamnoports = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 101)
)
rtspstreamnoports.setObjects(
    ("ZXTM-MIB", "fullLogLine")
)
if mibBuilder.loadTexts:
    rtspstreamnoports.setStatus(
        ""
    )

geodataloadfail = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 102)
)
geodataloadfail.setObjects(
    ("ZXTM-MIB", "fullLogLine")
)
if mibBuilder.loadTexts:
    geodataloadfail.setStatus(
        ""
    )

poolpersistencemismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 103)
)
poolpersistencemismatch.setObjects(
    ("ZXTM-MIB", "fullLogLine")
)
if mibBuilder.loadTexts:
    poolpersistencemismatch.setStatus(
        ""
    )

connerror = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 104)
)
connerror.setObjects(
      *(("ZXTM-MIB", "fullLogLine"),
        ("ZXTM-MIB", "virtualserverName"))
)
if mibBuilder.loadTexts:
    connerror.setStatus(
        ""
    )

connfail = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 105)
)
connfail.setObjects(
      *(("ZXTM-MIB", "fullLogLine"),
        ("ZXTM-MIB", "virtualserverName"))
)
if mibBuilder.loadTexts:
    connfail.setStatus(
        ""
    )

badcontentlen = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 106)
)
badcontentlen.setObjects(
      *(("ZXTM-MIB", "fullLogLine"),
        ("ZXTM-MIB", "poolName"))
)
if mibBuilder.loadTexts:
    badcontentlen.setStatus(
        ""
    )

activatealldead = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 107)
)
activatealldead.setObjects(
    ("ZXTM-MIB", "fullLogLine")
)
if mibBuilder.loadTexts:
    activatealldead.setStatus(
        ""
    )

machinerecovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 108)
)
machinerecovered.setObjects(
    ("ZXTM-MIB", "fullLogLine")
)
if mibBuilder.loadTexts:
    machinerecovered.setStatus(
        ""
    )

flipperrecovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 109)
)
flipperrecovered.setObjects(
    ("ZXTM-MIB", "fullLogLine")
)
if mibBuilder.loadTexts:
    flipperrecovered.setStatus(
        ""
    )

activatedautomatically = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 110)
)
activatedautomatically.setObjects(
    ("ZXTM-MIB", "fullLogLine")
)
if mibBuilder.loadTexts:
    activatedautomatically.setStatus(
        ""
    )

zclustermoderr = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 111)
)
zclustermoderr.setObjects(
    ("ZXTM-MIB", "fullLogLine")
)
if mibBuilder.loadTexts:
    zclustermoderr.setStatus(
        ""
    )

ec2flipperraiselocalworking = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 112)
)
ec2flipperraiselocalworking.setObjects(
    ("ZXTM-MIB", "fullLogLine")
)
if mibBuilder.loadTexts:
    ec2flipperraiselocalworking.setStatus(
        ""
    )

ec2flipperraiseothersdead = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 113)
)
ec2flipperraiseothersdead.setObjects(
    ("ZXTM-MIB", "fullLogLine")
)
if mibBuilder.loadTexts:
    ec2flipperraiseothersdead.setStatus(
        ""
    )

autherror = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 114)
)
autherror.setObjects(
    ("ZXTM-MIB", "fullLogLine")
)
if mibBuilder.loadTexts:
    autherror.setStatus(
        ""
    )

logfiledeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 115)
)
logfiledeleted.setObjects(
      *(("ZXTM-MIB", "fullLogLine"),
        ("ZXTM-MIB", "virtualserverName"))
)
if mibBuilder.loadTexts:
    logfiledeleted.setStatus(
        ""
    )

license_graceperiodexpired = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 116)
)
license_graceperiodexpired.setObjects(
      *(("ZXTM-MIB", "fullLogLine"),
        ("ZXTM-MIB", "licensekeyName"))
)
if mibBuilder.loadTexts:
    license_graceperiodexpired.setStatus(
        ""
    )

license_authorized = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 117)
)
license_authorized.setObjects(
      *(("ZXTM-MIB", "fullLogLine"),
        ("ZXTM-MIB", "licensekeyName"))
)
if mibBuilder.loadTexts:
    license_authorized.setStatus(
        ""
    )

license_rejected_authorized = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 118)
)
license_rejected_authorized.setObjects(
      *(("ZXTM-MIB", "fullLogLine"),
        ("ZXTM-MIB", "licensekeyName"))
)
if mibBuilder.loadTexts:
    license_rejected_authorized.setStatus(
        ""
    )

license_rejected_unauthorized = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 119)
)
license_rejected_unauthorized.setObjects(
      *(("ZXTM-MIB", "fullLogLine"),
        ("ZXTM-MIB", "licensekeyName"))
)
if mibBuilder.loadTexts:
    license_rejected_unauthorized.setStatus(
        ""
    )

license_timedout_authorized = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 120)
)
license_timedout_authorized.setObjects(
      *(("ZXTM-MIB", "fullLogLine"),
        ("ZXTM-MIB", "licensekeyName"))
)
if mibBuilder.loadTexts:
    license_timedout_authorized.setStatus(
        ""
    )

license_timedout_unauthorized = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 121)
)
license_timedout_unauthorized.setObjects(
      *(("ZXTM-MIB", "fullLogLine"),
        ("ZXTM-MIB", "licensekeyName"))
)
if mibBuilder.loadTexts:
    license_timedout_unauthorized.setStatus(
        ""
    )

license_unauthorized = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 122)
)
license_unauthorized.setObjects(
      *(("ZXTM-MIB", "fullLogLine"),
        ("ZXTM-MIB", "licensekeyName"))
)
if mibBuilder.loadTexts:
    license_unauthorized.setStatus(
        ""
    )

cachesizereduced = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 123)
)
cachesizereduced.setObjects(
    ("ZXTM-MIB", "fullLogLine")
)
if mibBuilder.loadTexts:
    cachesizereduced.setStatus(
        ""
    )

morememallowed = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 124)
)
morememallowed.setObjects(
    ("ZXTM-MIB", "fullLogLine")
)
if mibBuilder.loadTexts:
    morememallowed.setStatus(
        ""
    )

lessmemallowed = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 125)
)
lessmemallowed.setObjects(
    ("ZXTM-MIB", "fullLogLine")
)
if mibBuilder.loadTexts:
    lessmemallowed.setStatus(
        ""
    )

usedcredsdeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 126)
)
usedcredsdeleted.setObjects(
      *(("ZXTM-MIB", "fullLogLine"),
        ("ZXTM-MIB", "cloudcredentialsName"))
)
if mibBuilder.loadTexts:
    usedcredsdeleted.setStatus(
        ""
    )

apistatusprocesshanging = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 127)
)
apistatusprocesshanging.setObjects(
      *(("ZXTM-MIB", "fullLogLine"),
        ("ZXTM-MIB", "cloudcredentialsName"))
)
if mibBuilder.loadTexts:
    apistatusprocesshanging.setStatus(
        ""
    )

autonodedestroyed = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 128)
)
autonodedestroyed.setObjects(
      *(("ZXTM-MIB", "fullLogLine"),
        ("ZXTM-MIB", "poolName"))
)
if mibBuilder.loadTexts:
    autonodedestroyed.setStatus(
        ""
    )

autoscalestatusupdateerror = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 129)
)
autoscalestatusupdateerror.setObjects(
      *(("ZXTM-MIB", "fullLogLine"),
        ("ZXTM-MIB", "cloudcredentialsName"))
)
if mibBuilder.loadTexts:
    autoscalestatusupdateerror.setStatus(
        ""
    )

ec2iperr = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 130)
)
ec2iperr.setObjects(
    ("ZXTM-MIB", "fullLogLine")
)
if mibBuilder.loadTexts:
    ec2iperr.setStatus(
        ""
    )

dropec2ipwarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 131)
)
dropec2ipwarn.setObjects(
    ("ZXTM-MIB", "fullLogLine")
)
if mibBuilder.loadTexts:
    dropec2ipwarn.setStatus(
        ""
    )

ec2nopublicip = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 132)
)
ec2nopublicip.setObjects(
    ("ZXTM-MIB", "fullLogLine")
)
if mibBuilder.loadTexts:
    ec2nopublicip.setStatus(
        ""
    )

multihostload = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 133)
)
multihostload.setObjects(
    ("ZXTM-MIB", "fullLogLine")
)
if mibBuilder.loadTexts:
    multihostload.setStatus(
        ""
    )

tpslimited = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 134)
)
tpslimited.setObjects(
    ("ZXTM-MIB", "fullLogLine")
)
if mibBuilder.loadTexts:
    tpslimited.setStatus(
        ""
    )

ssltpslimited = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 135)
)
ssltpslimited.setObjects(
    ("ZXTM-MIB", "fullLogLine")
)
if mibBuilder.loadTexts:
    ssltpslimited.setStatus(
        ""
    )

bwlimited = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 136)
)
bwlimited.setObjects(
    ("ZXTM-MIB", "fullLogLine")
)
if mibBuilder.loadTexts:
    bwlimited.setStatus(
        ""
    )

licensetoomanylocations = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 137)
)
licensetoomanylocations.setObjects(
    ("ZXTM-MIB", "fullLogLine")
)
if mibBuilder.loadTexts:
    licensetoomanylocations.setStatus(
        ""
    )

autonodedestructioncomplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 138)
)
autonodedestructioncomplete.setObjects(
      *(("ZXTM-MIB", "fullLogLine"),
        ("ZXTM-MIB", "poolName"))
)
if mibBuilder.loadTexts:
    autonodedestructioncomplete.setStatus(
        ""
    )

autonodeexisted = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 139)
)
autonodeexisted.setObjects(
      *(("ZXTM-MIB", "fullLogLine"),
        ("ZXTM-MIB", "poolName"))
)
if mibBuilder.loadTexts:
    autonodeexisted.setStatus(
        ""
    )

autoscaledpooltoosmall = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 140)
)
autoscaledpooltoosmall.setObjects(
      *(("ZXTM-MIB", "fullLogLine"),
        ("ZXTM-MIB", "poolName"))
)
if mibBuilder.loadTexts:
    autoscaledpooltoosmall.setStatus(
        ""
    )

autoscaleinvalidargforcreatenode = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 141)
)
autoscaleinvalidargforcreatenode.setObjects(
      *(("ZXTM-MIB", "fullLogLine"),
        ("ZXTM-MIB", "poolName"))
)
if mibBuilder.loadTexts:
    autoscaleinvalidargforcreatenode.setStatus(
        ""
    )

autonodedisappeared = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 142)
)
autonodedisappeared.setObjects(
      *(("ZXTM-MIB", "fullLogLine"),
        ("ZXTM-MIB", "poolName"))
)
if mibBuilder.loadTexts:
    autonodedisappeared.setStatus(
        ""
    )

autoscaledpoolrefractory = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 143)
)
autoscaledpoolrefractory.setObjects(
      *(("ZXTM-MIB", "fullLogLine"),
        ("ZXTM-MIB", "poolName"))
)
if mibBuilder.loadTexts:
    autoscaledpoolrefractory.setStatus(
        ""
    )

cannotshrinkemptypool = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 144)
)
cannotshrinkemptypool.setObjects(
      *(("ZXTM-MIB", "fullLogLine"),
        ("ZXTM-MIB", "poolName"))
)
if mibBuilder.loadTexts:
    cannotshrinkemptypool.setStatus(
        ""
    )

autoscalinghysteresiscantgrow = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 145)
)
autoscalinghysteresiscantgrow.setObjects(
      *(("ZXTM-MIB", "fullLogLine"),
        ("ZXTM-MIB", "poolName"))
)
if mibBuilder.loadTexts:
    autoscalinghysteresiscantgrow.setStatus(
        ""
    )

autonodecreationcomplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 146)
)
autonodecreationcomplete.setObjects(
      *(("ZXTM-MIB", "fullLogLine"),
        ("ZXTM-MIB", "poolName"))
)
if mibBuilder.loadTexts:
    autonodecreationcomplete.setStatus(
        ""
    )

autonodestatuschange = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 147)
)
autonodestatuschange.setObjects(
      *(("ZXTM-MIB", "fullLogLine"),
        ("ZXTM-MIB", "poolName"))
)
if mibBuilder.loadTexts:
    autonodestatuschange.setStatus(
        ""
    )

autoscalinghysteresiscantshrink = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 148)
)
autoscalinghysteresiscantshrink.setObjects(
      *(("ZXTM-MIB", "fullLogLine"),
        ("ZXTM-MIB", "poolName"))
)
if mibBuilder.loadTexts:
    autoscalinghysteresiscantshrink.setStatus(
        ""
    )

autoscalingpoolstatechange = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 149)
)
autoscalingpoolstatechange.setObjects(
      *(("ZXTM-MIB", "fullLogLine"),
        ("ZXTM-MIB", "poolName"))
)
if mibBuilder.loadTexts:
    autoscalingpoolstatechange.setStatus(
        ""
    )

glbmissingips = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 150)
)
glbmissingips.setObjects(
    ("ZXTM-MIB", "fullLogLine")
)
if mibBuilder.loadTexts:
    glbmissingips.setStatus(
        ""
    )

glbnolocations = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 151)
)
glbnolocations.setObjects(
    ("ZXTM-MIB", "fullLogLine")
)
if mibBuilder.loadTexts:
    glbnolocations.setStatus(
        ""
    )

locationmonitorok = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 152)
)
locationmonitorok.setObjects(
      *(("ZXTM-MIB", "fullLogLine"),
        ("ZXTM-MIB", "locationName"),
        ("ZXTM-MIB", "glbServiceName"))
)
if mibBuilder.loadTexts:
    locationmonitorok.setStatus(
        ""
    )

locationmonitorfail = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 153)
)
locationmonitorfail.setObjects(
      *(("ZXTM-MIB", "fullLogLine"),
        ("ZXTM-MIB", "locationName"),
        ("ZXTM-MIB", "glbServiceName"))
)
if mibBuilder.loadTexts:
    locationmonitorfail.setStatus(
        ""
    )

locationok = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 154)
)
locationok.setObjects(
      *(("ZXTM-MIB", "fullLogLine"),
        ("ZXTM-MIB", "locationName"),
        ("ZXTM-MIB", "glbServiceName"))
)
if mibBuilder.loadTexts:
    locationok.setStatus(
        ""
    )

locationfail = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 155)
)
locationfail.setObjects(
      *(("ZXTM-MIB", "fullLogLine"),
        ("ZXTM-MIB", "locationName"),
        ("ZXTM-MIB", "glbServiceName"))
)
if mibBuilder.loadTexts:
    locationfail.setStatus(
        ""
    )

locationsoapok = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 156)
)
locationsoapok.setObjects(
      *(("ZXTM-MIB", "fullLogLine"),
        ("ZXTM-MIB", "locationName"),
        ("ZXTM-MIB", "glbServiceName"))
)
if mibBuilder.loadTexts:
    locationsoapok.setStatus(
        ""
    )

locationsoapfail = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 157)
)
locationsoapfail.setObjects(
      *(("ZXTM-MIB", "fullLogLine"),
        ("ZXTM-MIB", "locationName"),
        ("ZXTM-MIB", "glbServiceName"))
)
if mibBuilder.loadTexts:
    locationsoapfail.setStatus(
        ""
    )

glbdeadlocmissingips = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 158)
)
glbdeadlocmissingips.setObjects(
    ("ZXTM-MIB", "fullLogLine")
)
if mibBuilder.loadTexts:
    glbdeadlocmissingips.setStatus(
        ""
    )

autoscaleresponseparseerror = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 159)
)
autoscaleresponseparseerror.setObjects(
      *(("ZXTM-MIB", "fullLogLine"),
        ("ZXTM-MIB", "cloudcredentialsName"))
)
if mibBuilder.loadTexts:
    autoscaleresponseparseerror.setStatus(
        ""
    )

glbnewmaster = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 160)
)
glbnewmaster.setObjects(
      *(("ZXTM-MIB", "fullLogLine"),
        ("ZXTM-MIB", "locationName"),
        ("ZXTM-MIB", "glbServiceName"))
)
if mibBuilder.loadTexts:
    glbnewmaster.setStatus(
        ""
    )

glblogwritefail = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 161)
)
glblogwritefail.setObjects(
      *(("ZXTM-MIB", "fullLogLine"),
        ("ZXTM-MIB", "glbServiceName"))
)
if mibBuilder.loadTexts:
    glblogwritefail.setStatus(
        ""
    )

glbfailalter = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 162)
)
glbfailalter.setObjects(
      *(("ZXTM-MIB", "fullLogLine"),
        ("ZXTM-MIB", "glbServiceName"))
)
if mibBuilder.loadTexts:
    glbfailalter.setStatus(
        ""
    )

autoscalednodecontested = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 163)
)
autoscalednodecontested.setObjects(
      *(("ZXTM-MIB", "fullLogLine"),
        ("ZXTM-MIB", "poolName"))
)
if mibBuilder.loadTexts:
    autoscalednodecontested.setStatus(
        ""
    )

autoscalepoolconfupdate = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 164)
)
autoscalepoolconfupdate.setObjects(
      *(("ZXTM-MIB", "fullLogLine"),
        ("ZXTM-MIB", "poolName"))
)
if mibBuilder.loadTexts:
    autoscalepoolconfupdate.setStatus(
        ""
    )

autonodecreationstarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 165)
)
autonodecreationstarted.setObjects(
      *(("ZXTM-MIB", "fullLogLine"),
        ("ZXTM-MIB", "poolName"))
)
if mibBuilder.loadTexts:
    autonodecreationstarted.setStatus(
        ""
    )

autoscaleinvalidargfordeletenode = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 166)
)
autoscaleinvalidargfordeletenode.setObjects(
      *(("ZXTM-MIB", "fullLogLine"),
        ("ZXTM-MIB", "poolName"))
)
if mibBuilder.loadTexts:
    autoscaleinvalidargfordeletenode.setStatus(
        ""
    )

autoscalinghitroof = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 167)
)
autoscalinghitroof.setObjects(
      *(("ZXTM-MIB", "fullLogLine"),
        ("ZXTM-MIB", "poolName"))
)
if mibBuilder.loadTexts:
    autoscalinghitroof.setStatus(
        ""
    )

autoscalinghitfloor = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 168)
)
autoscalinghitfloor.setObjects(
      *(("ZXTM-MIB", "fullLogLine"),
        ("ZXTM-MIB", "poolName"))
)
if mibBuilder.loadTexts:
    autoscalinghitfloor.setStatus(
        ""
    )

apichangeprocesshanging = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 169)
)
apichangeprocesshanging.setObjects(
      *(("ZXTM-MIB", "fullLogLine"),
        ("ZXTM-MIB", "poolName"))
)
if mibBuilder.loadTexts:
    apichangeprocesshanging.setStatus(
        ""
    )

autoscaledpooltoobig = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 170)
)
autoscaledpooltoobig.setObjects(
      *(("ZXTM-MIB", "fullLogLine"),
        ("ZXTM-MIB", "poolName"))
)
if mibBuilder.loadTexts:
    autoscaledpooltoobig.setStatus(
        ""
    )

autoscalingprocesstimedout = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 171)
)
autoscalingprocesstimedout.setObjects(
      *(("ZXTM-MIB", "fullLogLine"),
        ("ZXTM-MIB", "cloudcredentialsName"))
)
if mibBuilder.loadTexts:
    autoscalingprocesstimedout.setStatus(
        ""
    )

autoscalingdisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 172)
)
autoscalingdisabled.setObjects(
      *(("ZXTM-MIB", "fullLogLine"),
        ("ZXTM-MIB", "poolName"))
)
if mibBuilder.loadTexts:
    autoscalingdisabled.setStatus(
        ""
    )

locmovemachine = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 173)
)
locmovemachine.setObjects(
      *(("ZXTM-MIB", "fullLogLine"),
        ("ZXTM-MIB", "locationName"),
        ("ZXTM-MIB", "zxtmName"))
)
if mibBuilder.loadTexts:
    locmovemachine.setStatus(
        ""
    )

locempty = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 174)
)
locempty.setObjects(
      *(("ZXTM-MIB", "fullLogLine"),
        ("ZXTM-MIB", "locationName"))
)
if mibBuilder.loadTexts:
    locempty.setStatus(
        ""
    )

autoscalinglicenseerror = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 175)
)
autoscalinglicenseerror.setObjects(
    ("ZXTM-MIB", "fullLogLine")
)
if mibBuilder.loadTexts:
    autoscalinglicenseerror.setStatus(
        ""
    )

autoscalinglicenseenabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 176)
)
autoscalinglicenseenabled.setObjects(
    ("ZXTM-MIB", "fullLogLine")
)
if mibBuilder.loadTexts:
    autoscalinglicenseenabled.setStatus(
        ""
    )

autoscalinglicensedisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 177)
)
autoscalinglicensedisabled.setObjects(
    ("ZXTM-MIB", "fullLogLine")
)
if mibBuilder.loadTexts:
    autoscalinglicensedisabled.setStatus(
        ""
    )

confreptimeout = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 178)
)
confreptimeout.setObjects(
    ("ZXTM-MIB", "fullLogLine")
)
if mibBuilder.loadTexts:
    confreptimeout.setStatus(
        ""
    )

confrepfailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 179)
)
confrepfailed.setObjects(
    ("ZXTM-MIB", "fullLogLine")
)
if mibBuilder.loadTexts:
    confrepfailed.setStatus(
        ""
    )

analyticslicenseenabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 180)
)
analyticslicenseenabled.setObjects(
    ("ZXTM-MIB", "fullLogLine")
)
if mibBuilder.loadTexts:
    analyticslicenseenabled.setStatus(
        ""
    )

analyticslicensedisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 181)
)
analyticslicensedisabled.setObjects(
    ("ZXTM-MIB", "fullLogLine")
)
if mibBuilder.loadTexts:
    analyticslicensedisabled.setStatus(
        ""
    )

autoscalingchangeprocessfailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 182)
)
autoscalingchangeprocessfailure.setObjects(
      *(("ZXTM-MIB", "fullLogLine"),
        ("ZXTM-MIB", "poolName"))
)
if mibBuilder.loadTexts:
    autoscalingchangeprocessfailure.setStatus(
        ""
    )

autoscalewrongimageid = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 183)
)
autoscalewrongimageid.setObjects(
      *(("ZXTM-MIB", "fullLogLine"),
        ("ZXTM-MIB", "poolName"))
)
if mibBuilder.loadTexts:
    autoscalewrongimageid.setStatus(
        ""
    )

autoscalewrongname = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 184)
)
autoscalewrongname.setObjects(
      *(("ZXTM-MIB", "fullLogLine"),
        ("ZXTM-MIB", "poolName"))
)
if mibBuilder.loadTexts:
    autoscalewrongname.setStatus(
        ""
    )

autoscalewrongsizeid = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 185)
)
autoscalewrongsizeid.setObjects(
      *(("ZXTM-MIB", "fullLogLine"),
        ("ZXTM-MIB", "poolName"))
)
if mibBuilder.loadTexts:
    autoscalewrongsizeid.setStatus(
        ""
    )

logdiskoverload = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 186)
)
logdiskoverload.setObjects(
    ("ZXTM-MIB", "fullLogLine")
)
if mibBuilder.loadTexts:
    logdiskoverload.setStatus(
        ""
    )

logdiskfull = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 187)
)
logdiskfull.setObjects(
    ("ZXTM-MIB", "fullLogLine")
)
if mibBuilder.loadTexts:
    logdiskfull.setStatus(
        ""
    )

autoscalingresuscitatepool = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 188)
)
autoscalingresuscitatepool.setObjects(
      *(("ZXTM-MIB", "fullLogLine"),
        ("ZXTM-MIB", "poolName"))
)
if mibBuilder.loadTexts:
    autoscalingresuscitatepool.setStatus(
        ""
    )

glbservicedied = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 190)
)
glbservicedied.setObjects(
      *(("ZXTM-MIB", "fullLogLine"),
        ("ZXTM-MIB", "glbServiceName"))
)
if mibBuilder.loadTexts:
    glbservicedied.setStatus(
        ""
    )

glbserviceok = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 191)
)
glbserviceok.setObjects(
      *(("ZXTM-MIB", "fullLogLine"),
        ("ZXTM-MIB", "glbServiceName"))
)
if mibBuilder.loadTexts:
    glbserviceok.setStatus(
        ""
    )

rulestreamerrortoomuch = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 210)
)
rulestreamerrortoomuch.setObjects(
      *(("ZXTM-MIB", "fullLogLine"),
        ("ZXTM-MIB", "ruleName"))
)
if mibBuilder.loadTexts:
    rulestreamerrortoomuch.setStatus(
        ""
    )

rulestreamerrornotenough = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 211)
)
rulestreamerrornotenough.setObjects(
      *(("ZXTM-MIB", "fullLogLine"),
        ("ZXTM-MIB", "ruleName"))
)
if mibBuilder.loadTexts:
    rulestreamerrornotenough.setStatus(
        ""
    )

rulestreamerrorprocessfailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 212)
)
rulestreamerrorprocessfailure.setObjects(
      *(("ZXTM-MIB", "fullLogLine"),
        ("ZXTM-MIB", "ruleName"))
)
if mibBuilder.loadTexts:
    rulestreamerrorprocessfailure.setStatus(
        ""
    )

rulestreamerrornotstarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 213)
)
rulestreamerrornotstarted.setObjects(
      *(("ZXTM-MIB", "fullLogLine"),
        ("ZXTM-MIB", "ruleName"))
)
if mibBuilder.loadTexts:
    rulestreamerrornotstarted.setStatus(
        ""
    )

rulestreamerrornotfinished = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 214)
)
rulestreamerrornotfinished.setObjects(
      *(("ZXTM-MIB", "fullLogLine"),
        ("ZXTM-MIB", "ruleName"))
)
if mibBuilder.loadTexts:
    rulestreamerrornotfinished.setStatus(
        ""
    )

rulestreamerrorinternal = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 215)
)
rulestreamerrorinternal.setObjects(
      *(("ZXTM-MIB", "fullLogLine"),
        ("ZXTM-MIB", "ruleName"))
)
if mibBuilder.loadTexts:
    rulestreamerrorinternal.setStatus(
        ""
    )

rulestreamerrorgetresponse = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 216)
)
rulestreamerrorgetresponse.setObjects(
      *(("ZXTM-MIB", "fullLogLine"),
        ("ZXTM-MIB", "ruleName"))
)
if mibBuilder.loadTexts:
    rulestreamerrorgetresponse.setStatus(
        ""
    )

rulesinvalidrequestbody = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 217)
)
rulesinvalidrequestbody.setObjects(
      *(("ZXTM-MIB", "fullLogLine"),
        ("ZXTM-MIB", "ruleName"),
        ("ZXTM-MIB", "virtualserverName"))
)
if mibBuilder.loadTexts:
    rulesinvalidrequestbody.setStatus(
        ""
    )

serviceruleabort = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 218)
)
serviceruleabort.setObjects(
      *(("ZXTM-MIB", "fullLogLine"),
        ("ZXTM-MIB", "glbServiceName"),
        ("ZXTM-MIB", "ruleName"))
)
if mibBuilder.loadTexts:
    serviceruleabort.setStatus(
        ""
    )

servicerulelocunknown = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 219)
)
servicerulelocunknown.setObjects(
      *(("ZXTM-MIB", "fullLogLine"),
        ("ZXTM-MIB", "glbServiceName"),
        ("ZXTM-MIB", "ruleName"))
)
if mibBuilder.loadTexts:
    servicerulelocunknown.setStatus(
        ""
    )

servicerulelocnotconfigured = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 220)
)
servicerulelocnotconfigured.setObjects(
      *(("ZXTM-MIB", "fullLogLine"),
        ("ZXTM-MIB", "glbServiceName"),
        ("ZXTM-MIB", "ruleName"))
)
if mibBuilder.loadTexts:
    servicerulelocnotconfigured.setStatus(
        ""
    )

servicerulelocdead = NotificationType(
    (1, 3, 6, 1, 4, 1, 7146, 1, 2, 15, 0, 221)
)
servicerulelocdead.setObjects(
      *(("ZXTM-MIB", "fullLogLine"),
        ("ZXTM-MIB", "glbServiceName"),
        ("ZXTM-MIB", "ruleName"))
)
if mibBuilder.loadTexts:
    servicerulelocdead.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZXTM-MIB",
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
       "totalRequests": totalRequests,
       "totalTransactions": totalTransactions,
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
       "glbservicedied": glbservicedied,
       "glbserviceok": glbserviceok,
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
       "authenticators": authenticators,
       "authenticatorNumber": authenticatorNumber,
       "authenticatorTable": authenticatorTable,
       "authenticatorEntry": authenticatorEntry,
       "authenticatorName": authenticatorName,
       "authenticatorRequests": authenticatorRequests,
       "authenticatorPasses": authenticatorPasses,
       "authenticatorFails": authenticatorFails,
       "authenticatorErrors": authenticatorErrors}
)
