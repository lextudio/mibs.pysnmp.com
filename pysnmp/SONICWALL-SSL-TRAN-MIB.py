# SNMP MIB module (SONICWALL-SSL-TRAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SONICWALL-SSL-TRAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:56:38 2024
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

sonicSSLTran = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8714, 2, 1, 7)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SonicWALL_ObjectIdentity = ObjectIdentity
sonicWALL = _SonicWALL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8714)
)
_SonicSEC_ObjectIdentity = ObjectIdentity
sonicSEC = _SonicSEC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8714, 2)
)
_SonicSSL_ObjectIdentity = ObjectIdentity
sonicSSL = _SonicSSL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8714, 2, 1)
)
_SslTranStats_ObjectIdentity = ObjectIdentity
sslTranStats = _SslTranStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8714, 2, 1, 7, 2)
)
_TotalRSAOperations_Type = Integer32
_TotalRSAOperations_Object = MibScalar
totalRSAOperations = _TotalRSAOperations_Object(
    (1, 3, 6, 1, 4, 1, 8714, 2, 1, 7, 2, 20),
    _TotalRSAOperations_Type()
)
totalRSAOperations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalRSAOperations.setStatus("mandatory")
_ConnRejNoRes_Type = Integer32
_ConnRejNoRes_Object = MibScalar
connRejNoRes = _ConnRejNoRes_Object(
    (1, 3, 6, 1, 4, 1, 8714, 2, 1, 7, 2, 21),
    _ConnRejNoRes_Type()
)
connRejNoRes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connRejNoRes.setStatus("mandatory")
_ActiveConnBlock_Type = Integer32
_ActiveConnBlock_Object = MibScalar
activeConnBlock = _ActiveConnBlock_Object(
    (1, 3, 6, 1, 4, 1, 8714, 2, 1, 7, 2, 22),
    _ActiveConnBlock_Type()
)
activeConnBlock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeConnBlock.setStatus("mandatory")
_ActiveClientConns_Type = Integer32
_ActiveClientConns_Object = MibScalar
activeClientConns = _ActiveClientConns_Object(
    (1, 3, 6, 1, 4, 1, 8714, 2, 1, 7, 2, 23),
    _ActiveClientConns_Type()
)
activeClientConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeClientConns.setStatus("mandatory")
_ConnAccepted_Type = Integer32
_ConnAccepted_Object = MibScalar
connAccepted = _ConnAccepted_Object(
    (1, 3, 6, 1, 4, 1, 8714, 2, 1, 7, 2, 24),
    _ConnAccepted_Type()
)
connAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connAccepted.setStatus("mandatory")
_ActiveServerConns_Type = Integer32
_ActiveServerConns_Object = MibScalar
activeServerConns = _ActiveServerConns_Object(
    (1, 3, 6, 1, 4, 1, 8714, 2, 1, 7, 2, 25),
    _ActiveServerConns_Type()
)
activeServerConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeServerConns.setStatus("mandatory")
_SslNegRefused_Type = Integer32
_SslNegRefused_Object = MibScalar
sslNegRefused = _SslNegRefused_Object(
    (1, 3, 6, 1, 4, 1, 8714, 2, 1, 7, 2, 31),
    _SslNegRefused_Type()
)
sslNegRefused.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslNegRefused.setStatus("mandatory")
_SslNegAccept_Type = Integer32
_SslNegAccept_Object = MibScalar
sslNegAccept = _SslNegAccept_Object(
    (1, 3, 6, 1, 4, 1, 8714, 2, 1, 7, 2, 32),
    _SslNegAccept_Type()
)
sslNegAccept.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslNegAccept.setStatus("mandatory")
_ActiveOpenSockets_Type = Integer32
_ActiveOpenSockets_Object = MibScalar
activeOpenSockets = _ActiveOpenSockets_Object(
    (1, 3, 6, 1, 4, 1, 8714, 2, 1, 7, 2, 33),
    _ActiveOpenSockets_Type()
)
activeOpenSockets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeOpenSockets.setStatus("mandatory")
_SslTranErrs_ObjectIdentity = ObjectIdentity
sslTranErrs = _SslTranErrs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8714, 2, 1, 7, 3)
)
_ConnErrs_Type = Integer32
_ConnErrs_Object = MibScalar
connErrs = _ConnErrs_Object(
    (1, 3, 6, 1, 4, 1, 8714, 2, 1, 7, 3, 26),
    _ConnErrs_Type()
)
connErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connErrs.setStatus("mandatory")
_ConnBlockErrs_Type = Integer32
_ConnBlockErrs_Object = MibScalar
connBlockErrs = _ConnBlockErrs_Object(
    (1, 3, 6, 1, 4, 1, 8714, 2, 1, 7, 3, 27),
    _ConnBlockErrs_Type()
)
connBlockErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connBlockErrs.setStatus("mandatory")
_SslNegErrs_Type = Integer32
_SslNegErrs_Object = MibScalar
sslNegErrs = _SslNegErrs_Object(
    (1, 3, 6, 1, 4, 1, 8714, 2, 1, 7, 3, 34),
    _SslNegErrs_Type()
)
sslNegErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslNegErrs.setStatus("mandatory")
_SslErrors_Type = Integer32
_SslErrors_Object = MibScalar
sslErrors = _SslErrors_Object(
    (1, 3, 6, 1, 4, 1, 8714, 2, 1, 7, 3, 35),
    _SslErrors_Type()
)
sslErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslErrors.setStatus("mandatory")
_OpenSSLAcceptErrs_Type = Integer32
_OpenSSLAcceptErrs_Object = MibScalar
openSSLAcceptErrs = _OpenSSLAcceptErrs_Object(
    (1, 3, 6, 1, 4, 1, 8714, 2, 1, 7, 3, 36),
    _OpenSSLAcceptErrs_Type()
)
openSSLAcceptErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    openSSLAcceptErrs.setStatus("mandatory")
_OpenSSLConnErrs_Type = Integer32
_OpenSSLConnErrs_Object = MibScalar
openSSLConnErrs = _OpenSSLConnErrs_Object(
    (1, 3, 6, 1, 4, 1, 8714, 2, 1, 7, 3, 37),
    _OpenSSLConnErrs_Type()
)
openSSLConnErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    openSSLConnErrs.setStatus("mandatory")
_TotSocketErrs_Type = Integer32
_TotSocketErrs_Object = MibScalar
totSocketErrs = _TotSocketErrs_Object(
    (1, 3, 6, 1, 4, 1, 8714, 2, 1, 7, 3, 38),
    _TotSocketErrs_Type()
)
totSocketErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totSocketErrs.setStatus("mandatory")
_OpenSSLWriteErr_Type = Integer32
_OpenSSLWriteErr_Object = MibScalar
openSSLWriteErr = _OpenSSLWriteErr_Object(
    (1, 3, 6, 1, 4, 1, 8714, 2, 1, 7, 3, 41),
    _OpenSSLWriteErr_Type()
)
openSSLWriteErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    openSSLWriteErr.setStatus("mandatory")
_SslPipeWriteErr_Type = Integer32
_SslPipeWriteErr_Object = MibScalar
sslPipeWriteErr = _SslPipeWriteErr_Object(
    (1, 3, 6, 1, 4, 1, 8714, 2, 1, 7, 3, 42),
    _SslPipeWriteErr_Type()
)
sslPipeWriteErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslPipeWriteErr.setStatus("mandatory")
_ToServerWriteErr_Type = Integer32
_ToServerWriteErr_Object = MibScalar
toServerWriteErr = _ToServerWriteErr_Object(
    (1, 3, 6, 1, 4, 1, 8714, 2, 1, 7, 3, 43),
    _ToServerWriteErr_Type()
)
toServerWriteErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    toServerWriteErr.setStatus("mandatory")
_ToServerPipeWriteErr_Type = Integer32
_ToServerPipeWriteErr_Object = MibScalar
toServerPipeWriteErr = _ToServerPipeWriteErr_Object(
    (1, 3, 6, 1, 4, 1, 8714, 2, 1, 7, 3, 44),
    _ToServerPipeWriteErr_Type()
)
toServerPipeWriteErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    toServerPipeWriteErr.setStatus("mandatory")
_OpenSSLReadErr_Type = Integer32
_OpenSSLReadErr_Object = MibScalar
openSSLReadErr = _OpenSSLReadErr_Object(
    (1, 3, 6, 1, 4, 1, 8714, 2, 1, 7, 3, 45),
    _OpenSSLReadErr_Type()
)
openSSLReadErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    openSSLReadErr.setStatus("mandatory")
_SslPipeReadErr_Type = Integer32
_SslPipeReadErr_Object = MibScalar
sslPipeReadErr = _SslPipeReadErr_Object(
    (1, 3, 6, 1, 4, 1, 8714, 2, 1, 7, 3, 46),
    _SslPipeReadErr_Type()
)
sslPipeReadErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslPipeReadErr.setStatus("mandatory")
_ToServerReadErr_Type = Integer32
_ToServerReadErr_Object = MibScalar
toServerReadErr = _ToServerReadErr_Object(
    (1, 3, 6, 1, 4, 1, 8714, 2, 1, 7, 3, 47),
    _ToServerReadErr_Type()
)
toServerReadErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    toServerReadErr.setStatus("mandatory")
_ToServerPipeReadErr_Type = Integer32
_ToServerPipeReadErr_Object = MibScalar
toServerPipeReadErr = _ToServerPipeReadErr_Object(
    (1, 3, 6, 1, 4, 1, 8714, 2, 1, 7, 3, 48),
    _ToServerPipeReadErr_Type()
)
toServerPipeReadErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    toServerPipeReadErr.setStatus("mandatory")
_SslTranEvents_ObjectIdentity = ObjectIdentity
sslTranEvents = _SslTranEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8714, 2, 1, 7, 10)
)

# Managed Objects groups


# Notification objects

sslTpsChangeHi = NotificationType(
    (1, 3, 6, 1, 4, 1, 8714, 2, 1, 7, 10, 0, 4)
)
if mibBuilder.loadTexts:
    sslTpsChangeHi.setStatus(
        ""
    )

sslTpsChangeLo = NotificationType(
    (1, 3, 6, 1, 4, 1, 8714, 2, 1, 7, 10, 0, 5)
)
if mibBuilder.loadTexts:
    sslTpsChangeLo.setStatus(
        ""
    )

sslTotalConnectsChangeHi = NotificationType(
    (1, 3, 6, 1, 4, 1, 8714, 2, 1, 7, 10, 0, 6)
)
if mibBuilder.loadTexts:
    sslTotalConnectsChangeHi.setStatus(
        ""
    )

sslTotalConnectsChangeLo = NotificationType(
    (1, 3, 6, 1, 4, 1, 8714, 2, 1, 7, 10, 0, 7)
)
if mibBuilder.loadTexts:
    sslTotalConnectsChangeLo.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SONICWALL-SSL-TRAN-MIB",
    **{"sonicWALL": sonicWALL,
       "sonicSEC": sonicSEC,
       "sonicSSL": sonicSSL,
       "sonicSSLTran": sonicSSLTran,
       "sslTranStats": sslTranStats,
       "totalRSAOperations": totalRSAOperations,
       "connRejNoRes": connRejNoRes,
       "activeConnBlock": activeConnBlock,
       "activeClientConns": activeClientConns,
       "connAccepted": connAccepted,
       "activeServerConns": activeServerConns,
       "sslNegRefused": sslNegRefused,
       "sslNegAccept": sslNegAccept,
       "activeOpenSockets": activeOpenSockets,
       "sslTranErrs": sslTranErrs,
       "connErrs": connErrs,
       "connBlockErrs": connBlockErrs,
       "sslNegErrs": sslNegErrs,
       "sslErrors": sslErrors,
       "openSSLAcceptErrs": openSSLAcceptErrs,
       "openSSLConnErrs": openSSLConnErrs,
       "totSocketErrs": totSocketErrs,
       "openSSLWriteErr": openSSLWriteErr,
       "sslPipeWriteErr": sslPipeWriteErr,
       "toServerWriteErr": toServerWriteErr,
       "toServerPipeWriteErr": toServerPipeWriteErr,
       "openSSLReadErr": openSSLReadErr,
       "sslPipeReadErr": sslPipeReadErr,
       "toServerReadErr": toServerReadErr,
       "toServerPipeReadErr": toServerPipeReadErr,
       "sslTranEvents": sslTranEvents,
       "sslTpsChangeHi": sslTpsChangeHi,
       "sslTpsChangeLo": sslTpsChangeLo,
       "sslTotalConnectsChangeHi": sslTotalConnectsChangeHi,
       "sslTotalConnectsChangeLo": sslTotalConnectsChangeLo}
)
