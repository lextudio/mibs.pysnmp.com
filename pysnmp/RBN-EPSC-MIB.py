# SNMP MIB module (RBN-EPSC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RBN-EPSC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:45:07 2024
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

(rbnMgmt,) = mibBuilder.importSymbols(
    "RBN-SMI",
    "rbnMgmt")

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

rbnEpscMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44)
)
rbnEpscMIB.setRevisions(
        ("2011-05-11 14:56",
         "2011-05-02 14:09",
         "2011-03-11 12:03",
         "2011-02-01 12:04",
         "2011-01-26 15:00",
         "2011-01-26 13:22",
         "2010-12-16 11:00",
         "2010-03-11 15:35")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RbnEpscMIBObjects_ObjectIdentity = ObjectIdentity
rbnEpscMIBObjects = _RbnEpscMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1)
)
_RbnEpscCommonStats_ObjectIdentity = ObjectIdentity
rbnEpscCommonStats = _RbnEpscCommonStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 1)
)
_RbnEpscCommonGeneral_ObjectIdentity = ObjectIdentity
rbnEpscCommonGeneral = _RbnEpscCommonGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 1, 1)
)
_RbnEpscConnectionsEstablished_Type = Gauge32
_RbnEpscConnectionsEstablished_Object = MibScalar
rbnEpscConnectionsEstablished = _RbnEpscConnectionsEstablished_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 1, 1, 1),
    _RbnEpscConnectionsEstablished_Type()
)
rbnEpscConnectionsEstablished.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscConnectionsEstablished.setStatus("current")
_RbnEpscPdnConnectionTimeout_Type = Counter64
_RbnEpscPdnConnectionTimeout_Object = MibScalar
rbnEpscPdnConnectionTimeout = _RbnEpscPdnConnectionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 1, 1, 2),
    _RbnEpscPdnConnectionTimeout_Type()
)
rbnEpscPdnConnectionTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscPdnConnectionTimeout.setStatus("current")
_RbnEpscBearersEstablished_Type = Gauge32
_RbnEpscBearersEstablished_Object = MibScalar
rbnEpscBearersEstablished = _RbnEpscBearersEstablished_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 1, 1, 3),
    _RbnEpscBearersEstablished_Type()
)
rbnEpscBearersEstablished.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscBearersEstablished.setStatus("current")
_RbnEpscUeAttached_Type = Gauge32
_RbnEpscUeAttached_Object = MibScalar
rbnEpscUeAttached = _RbnEpscUeAttached_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 1, 1, 4),
    _RbnEpscUeAttached_Type()
)
rbnEpscUeAttached.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscUeAttached.setStatus("current")
_RbnEpscCommonCharging_ObjectIdentity = ObjectIdentity
rbnEpscCommonCharging = _RbnEpscCommonCharging_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 1, 2)
)
_RbnEpscClosedCdrFiles_Type = Counter64
_RbnEpscClosedCdrFiles_Object = MibScalar
rbnEpscClosedCdrFiles = _RbnEpscClosedCdrFiles_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 1, 2, 1),
    _RbnEpscClosedCdrFiles_Type()
)
rbnEpscClosedCdrFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscClosedCdrFiles.setStatus("current")
_RbnEpscRfAcrSent_Type = Counter64
_RbnEpscRfAcrSent_Object = MibScalar
rbnEpscRfAcrSent = _RbnEpscRfAcrSent_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 1, 2, 2),
    _RbnEpscRfAcrSent_Type()
)
rbnEpscRfAcrSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscRfAcrSent.setStatus("current")
_RbnEpscRfAcaSuccRcvd_Type = Counter64
_RbnEpscRfAcaSuccRcvd_Object = MibScalar
rbnEpscRfAcaSuccRcvd = _RbnEpscRfAcaSuccRcvd_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 1, 2, 3),
    _RbnEpscRfAcaSuccRcvd_Type()
)
rbnEpscRfAcaSuccRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscRfAcaSuccRcvd.setStatus("current")
_RbnEpscRfAcaFailRcvd_Type = Counter64
_RbnEpscRfAcaFailRcvd_Object = MibScalar
rbnEpscRfAcaFailRcvd = _RbnEpscRfAcaFailRcvd_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 1, 2, 4),
    _RbnEpscRfAcaFailRcvd_Type()
)
rbnEpscRfAcaFailRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscRfAcaFailRcvd.setStatus("current")
_RbnEpscRfAcrWrittenToDisk_Type = Counter64
_RbnEpscRfAcrWrittenToDisk_Object = MibScalar
rbnEpscRfAcrWrittenToDisk = _RbnEpscRfAcrWrittenToDisk_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 1, 2, 5),
    _RbnEpscRfAcrWrittenToDisk_Type()
)
rbnEpscRfAcrWrittenToDisk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscRfAcrWrittenToDisk.setStatus("current")
_RbnEpscCommonDiameter_ObjectIdentity = ObjectIdentity
rbnEpscCommonDiameter = _RbnEpscCommonDiameter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 1, 3)
)
_RbnEpscDiameterMsgInvalidRcvd_Type = Counter64
_RbnEpscDiameterMsgInvalidRcvd_Object = MibScalar
rbnEpscDiameterMsgInvalidRcvd = _RbnEpscDiameterMsgInvalidRcvd_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 1, 3, 1),
    _RbnEpscDiameterMsgInvalidRcvd_Type()
)
rbnEpscDiameterMsgInvalidRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscDiameterMsgInvalidRcvd.setStatus("current")
_RbnEpscCommonIcr_ObjectIdentity = ObjectIdentity
rbnEpscCommonIcr = _RbnEpscCommonIcr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 1, 4)
)
_RbnEpscIcrCreateSessionSyncRcvd_Type = Counter64
_RbnEpscIcrCreateSessionSyncRcvd_Object = MibScalar
rbnEpscIcrCreateSessionSyncRcvd = _RbnEpscIcrCreateSessionSyncRcvd_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 1, 4, 1),
    _RbnEpscIcrCreateSessionSyncRcvd_Type()
)
rbnEpscIcrCreateSessionSyncRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscIcrCreateSessionSyncRcvd.setStatus("current")
_RbnEpscIcrCreateSessionSyncSent_Type = Counter64
_RbnEpscIcrCreateSessionSyncSent_Object = MibScalar
rbnEpscIcrCreateSessionSyncSent = _RbnEpscIcrCreateSessionSyncSent_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 1, 4, 2),
    _RbnEpscIcrCreateSessionSyncSent_Type()
)
rbnEpscIcrCreateSessionSyncSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscIcrCreateSessionSyncSent.setStatus("current")
_RbnEpscIcrDeleteSessionSyncRcvd_Type = Counter64
_RbnEpscIcrDeleteSessionSyncRcvd_Object = MibScalar
rbnEpscIcrDeleteSessionSyncRcvd = _RbnEpscIcrDeleteSessionSyncRcvd_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 1, 4, 3),
    _RbnEpscIcrDeleteSessionSyncRcvd_Type()
)
rbnEpscIcrDeleteSessionSyncRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscIcrDeleteSessionSyncRcvd.setStatus("current")
_RbnEpscIcrDeleteSessionSyncSent_Type = Counter64
_RbnEpscIcrDeleteSessionSyncSent_Object = MibScalar
rbnEpscIcrDeleteSessionSyncSent = _RbnEpscIcrDeleteSessionSyncSent_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 1, 4, 4),
    _RbnEpscIcrDeleteSessionSyncSent_Type()
)
rbnEpscIcrDeleteSessionSyncSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscIcrDeleteSessionSyncSent.setStatus("current")
_RbnEpscSgwStats_ObjectIdentity = ObjectIdentity
rbnEpscSgwStats = _RbnEpscSgwStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 2)
)
_RbnEpscSgwGeneral_ObjectIdentity = ObjectIdentity
rbnEpscSgwGeneral = _RbnEpscSgwGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 2, 1)
)
_RbnEpscSgwUeEcmConnected_Type = Gauge32
_RbnEpscSgwUeEcmConnected_Object = MibScalar
rbnEpscSgwUeEcmConnected = _RbnEpscSgwUeEcmConnected_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 2, 1, 2),
    _RbnEpscSgwUeEcmConnected_Type()
)
rbnEpscSgwUeEcmConnected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscSgwUeEcmConnected.setStatus("current")
_RbnEpscSgwS5S8Gtp_ObjectIdentity = ObjectIdentity
rbnEpscSgwS5S8Gtp = _RbnEpscSgwS5S8Gtp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 2, 3)
)
_RbnEpscS5S8CreateSessionReqSent_Type = Counter64
_RbnEpscS5S8CreateSessionReqSent_Object = MibScalar
rbnEpscS5S8CreateSessionReqSent = _RbnEpscS5S8CreateSessionReqSent_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 2, 3, 1),
    _RbnEpscS5S8CreateSessionReqSent_Type()
)
rbnEpscS5S8CreateSessionReqSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscS5S8CreateSessionReqSent.setStatus("current")
_RbnEpscS5S8CreateSessionRespAccRcvd_Type = Counter64
_RbnEpscS5S8CreateSessionRespAccRcvd_Object = MibScalar
rbnEpscS5S8CreateSessionRespAccRcvd = _RbnEpscS5S8CreateSessionRespAccRcvd_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 2, 3, 2),
    _RbnEpscS5S8CreateSessionRespAccRcvd_Type()
)
rbnEpscS5S8CreateSessionRespAccRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscS5S8CreateSessionRespAccRcvd.setStatus("current")
_RbnEpscS5S8CreateSessionRespRejRcvd_Type = Counter64
_RbnEpscS5S8CreateSessionRespRejRcvd_Object = MibScalar
rbnEpscS5S8CreateSessionRespRejRcvd = _RbnEpscS5S8CreateSessionRespRejRcvd_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 2, 3, 3),
    _RbnEpscS5S8CreateSessionRespRejRcvd_Type()
)
rbnEpscS5S8CreateSessionRespRejRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscS5S8CreateSessionRespRejRcvd.setStatus("current")
_RbnEpscS5S8DeleteSessionReqSent_Type = Counter64
_RbnEpscS5S8DeleteSessionReqSent_Object = MibScalar
rbnEpscS5S8DeleteSessionReqSent = _RbnEpscS5S8DeleteSessionReqSent_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 2, 3, 4),
    _RbnEpscS5S8DeleteSessionReqSent_Type()
)
rbnEpscS5S8DeleteSessionReqSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscS5S8DeleteSessionReqSent.setStatus("current")
_RbnEpscS5S8DeleteSessionRespAccRcvd_Type = Counter64
_RbnEpscS5S8DeleteSessionRespAccRcvd_Object = MibScalar
rbnEpscS5S8DeleteSessionRespAccRcvd = _RbnEpscS5S8DeleteSessionRespAccRcvd_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 2, 3, 5),
    _RbnEpscS5S8DeleteSessionRespAccRcvd_Type()
)
rbnEpscS5S8DeleteSessionRespAccRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscS5S8DeleteSessionRespAccRcvd.setStatus("current")
_RbnEpscS5S8DeleteSessionRespRejRcvd_Type = Counter64
_RbnEpscS5S8DeleteSessionRespRejRcvd_Object = MibScalar
rbnEpscS5S8DeleteSessionRespRejRcvd = _RbnEpscS5S8DeleteSessionRespRejRcvd_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 2, 3, 6),
    _RbnEpscS5S8DeleteSessionRespRejRcvd_Type()
)
rbnEpscS5S8DeleteSessionRespRejRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscS5S8DeleteSessionRespRejRcvd.setStatus("current")
_RbnEpscS5S8DeleteBearerReqRcvd_Type = Counter64
_RbnEpscS5S8DeleteBearerReqRcvd_Object = MibScalar
rbnEpscS5S8DeleteBearerReqRcvd = _RbnEpscS5S8DeleteBearerReqRcvd_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 2, 3, 7),
    _RbnEpscS5S8DeleteBearerReqRcvd_Type()
)
rbnEpscS5S8DeleteBearerReqRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscS5S8DeleteBearerReqRcvd.setStatus("current")
_RbnEpscS5S8DeleteBearerRespAccSent_Type = Counter64
_RbnEpscS5S8DeleteBearerRespAccSent_Object = MibScalar
rbnEpscS5S8DeleteBearerRespAccSent = _RbnEpscS5S8DeleteBearerRespAccSent_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 2, 3, 8),
    _RbnEpscS5S8DeleteBearerRespAccSent_Type()
)
rbnEpscS5S8DeleteBearerRespAccSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscS5S8DeleteBearerRespAccSent.setStatus("current")
_RbnEpscS5S8DeleteBearerRespRejSent_Type = Counter64
_RbnEpscS5S8DeleteBearerRespRejSent_Object = MibScalar
rbnEpscS5S8DeleteBearerRespRejSent = _RbnEpscS5S8DeleteBearerRespRejSent_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 2, 3, 9),
    _RbnEpscS5S8DeleteBearerRespRejSent_Type()
)
rbnEpscS5S8DeleteBearerRespRejSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscS5S8DeleteBearerRespRejSent.setStatus("current")
_RbnEpscS5S8CreateBearerReqRcvd_Type = Counter64
_RbnEpscS5S8CreateBearerReqRcvd_Object = MibScalar
rbnEpscS5S8CreateBearerReqRcvd = _RbnEpscS5S8CreateBearerReqRcvd_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 2, 3, 10),
    _RbnEpscS5S8CreateBearerReqRcvd_Type()
)
rbnEpscS5S8CreateBearerReqRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscS5S8CreateBearerReqRcvd.setStatus("current")
_RbnEpscS5S8CreateBearerRespAccSent_Type = Counter64
_RbnEpscS5S8CreateBearerRespAccSent_Object = MibScalar
rbnEpscS5S8CreateBearerRespAccSent = _RbnEpscS5S8CreateBearerRespAccSent_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 2, 3, 11),
    _RbnEpscS5S8CreateBearerRespAccSent_Type()
)
rbnEpscS5S8CreateBearerRespAccSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscS5S8CreateBearerRespAccSent.setStatus("current")
_RbnEpscS5S8CreateBearerRespRejSent_Type = Counter64
_RbnEpscS5S8CreateBearerRespRejSent_Object = MibScalar
rbnEpscS5S8CreateBearerRespRejSent = _RbnEpscS5S8CreateBearerRespRejSent_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 2, 3, 12),
    _RbnEpscS5S8CreateBearerRespRejSent_Type()
)
rbnEpscS5S8CreateBearerRespRejSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscS5S8CreateBearerRespRejSent.setStatus("current")
_RbnEpscS5S8DeleteBearerCmdSent_Type = Counter64
_RbnEpscS5S8DeleteBearerCmdSent_Object = MibScalar
rbnEpscS5S8DeleteBearerCmdSent = _RbnEpscS5S8DeleteBearerCmdSent_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 2, 3, 13),
    _RbnEpscS5S8DeleteBearerCmdSent_Type()
)
rbnEpscS5S8DeleteBearerCmdSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscS5S8DeleteBearerCmdSent.setStatus("current")
_RbnEpscS5S8DeleteBearerFailureIndRcvd_Type = Counter64
_RbnEpscS5S8DeleteBearerFailureIndRcvd_Object = MibScalar
rbnEpscS5S8DeleteBearerFailureIndRcvd = _RbnEpscS5S8DeleteBearerFailureIndRcvd_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 2, 3, 14),
    _RbnEpscS5S8DeleteBearerFailureIndRcvd_Type()
)
rbnEpscS5S8DeleteBearerFailureIndRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscS5S8DeleteBearerFailureIndRcvd.setStatus("current")
_RbnEpscS5S8UpdateBearerReqRcvd_Type = Counter64
_RbnEpscS5S8UpdateBearerReqRcvd_Object = MibScalar
rbnEpscS5S8UpdateBearerReqRcvd = _RbnEpscS5S8UpdateBearerReqRcvd_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 2, 3, 15),
    _RbnEpscS5S8UpdateBearerReqRcvd_Type()
)
rbnEpscS5S8UpdateBearerReqRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscS5S8UpdateBearerReqRcvd.setStatus("current")
_RbnEpscS5S8UpdateBearerRespAccSent_Type = Counter64
_RbnEpscS5S8UpdateBearerRespAccSent_Object = MibScalar
rbnEpscS5S8UpdateBearerRespAccSent = _RbnEpscS5S8UpdateBearerRespAccSent_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 2, 3, 16),
    _RbnEpscS5S8UpdateBearerRespAccSent_Type()
)
rbnEpscS5S8UpdateBearerRespAccSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscS5S8UpdateBearerRespAccSent.setStatus("current")
_RbnEpscS5S8UpdateBearerRespRejSent_Type = Counter64
_RbnEpscS5S8UpdateBearerRespRejSent_Object = MibScalar
rbnEpscS5S8UpdateBearerRespRejSent = _RbnEpscS5S8UpdateBearerRespRejSent_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 2, 3, 17),
    _RbnEpscS5S8UpdateBearerRespRejSent_Type()
)
rbnEpscS5S8UpdateBearerRespRejSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscS5S8UpdateBearerRespRejSent.setStatus("current")
_RbnEpscS5S8ModifyBearerReqSent_Type = Counter64
_RbnEpscS5S8ModifyBearerReqSent_Object = MibScalar
rbnEpscS5S8ModifyBearerReqSent = _RbnEpscS5S8ModifyBearerReqSent_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 2, 3, 18),
    _RbnEpscS5S8ModifyBearerReqSent_Type()
)
rbnEpscS5S8ModifyBearerReqSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscS5S8ModifyBearerReqSent.setStatus("current")
_RbnEpscS5S8ModifyBearerRespAccRcvd_Type = Counter64
_RbnEpscS5S8ModifyBearerRespAccRcvd_Object = MibScalar
rbnEpscS5S8ModifyBearerRespAccRcvd = _RbnEpscS5S8ModifyBearerRespAccRcvd_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 2, 3, 19),
    _RbnEpscS5S8ModifyBearerRespAccRcvd_Type()
)
rbnEpscS5S8ModifyBearerRespAccRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscS5S8ModifyBearerRespAccRcvd.setStatus("current")
_RbnEpscS5S8ModifyBearerRespRejRcvd_Type = Counter64
_RbnEpscS5S8ModifyBearerRespRejRcvd_Object = MibScalar
rbnEpscS5S8ModifyBearerRespRejRcvd = _RbnEpscS5S8ModifyBearerRespRejRcvd_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 2, 3, 20),
    _RbnEpscS5S8ModifyBearerRespRejRcvd_Type()
)
rbnEpscS5S8ModifyBearerRespRejRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscS5S8ModifyBearerRespRejRcvd.setStatus("current")
_RbnEpscSgwS11S4_ObjectIdentity = ObjectIdentity
rbnEpscSgwS11S4 = _RbnEpscSgwS11S4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 2, 4)
)
_RbnEpscS11S4CreateSessionReqRcvd_Type = Counter64
_RbnEpscS11S4CreateSessionReqRcvd_Object = MibScalar
rbnEpscS11S4CreateSessionReqRcvd = _RbnEpscS11S4CreateSessionReqRcvd_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 2, 4, 1),
    _RbnEpscS11S4CreateSessionReqRcvd_Type()
)
rbnEpscS11S4CreateSessionReqRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscS11S4CreateSessionReqRcvd.setStatus("current")
_RbnEpscS11S4CreateSessionRespAccSent_Type = Counter64
_RbnEpscS11S4CreateSessionRespAccSent_Object = MibScalar
rbnEpscS11S4CreateSessionRespAccSent = _RbnEpscS11S4CreateSessionRespAccSent_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 2, 4, 2),
    _RbnEpscS11S4CreateSessionRespAccSent_Type()
)
rbnEpscS11S4CreateSessionRespAccSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscS11S4CreateSessionRespAccSent.setStatus("current")
_RbnEpscS11S4CreateSessionRespRejSent_Type = Counter64
_RbnEpscS11S4CreateSessionRespRejSent_Object = MibScalar
rbnEpscS11S4CreateSessionRespRejSent = _RbnEpscS11S4CreateSessionRespRejSent_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 2, 4, 3),
    _RbnEpscS11S4CreateSessionRespRejSent_Type()
)
rbnEpscS11S4CreateSessionRespRejSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscS11S4CreateSessionRespRejSent.setStatus("current")
_RbnEpscS11S4ModifyBearerReqRcvd_Type = Counter64
_RbnEpscS11S4ModifyBearerReqRcvd_Object = MibScalar
rbnEpscS11S4ModifyBearerReqRcvd = _RbnEpscS11S4ModifyBearerReqRcvd_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 2, 4, 4),
    _RbnEpscS11S4ModifyBearerReqRcvd_Type()
)
rbnEpscS11S4ModifyBearerReqRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscS11S4ModifyBearerReqRcvd.setStatus("current")
_RbnEpscS11S4ModifyBearerRespAccSent_Type = Counter64
_RbnEpscS11S4ModifyBearerRespAccSent_Object = MibScalar
rbnEpscS11S4ModifyBearerRespAccSent = _RbnEpscS11S4ModifyBearerRespAccSent_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 2, 4, 5),
    _RbnEpscS11S4ModifyBearerRespAccSent_Type()
)
rbnEpscS11S4ModifyBearerRespAccSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscS11S4ModifyBearerRespAccSent.setStatus("current")
_RbnEpscS11S4ModifyBearerRespRejSent_Type = Counter64
_RbnEpscS11S4ModifyBearerRespRejSent_Object = MibScalar
rbnEpscS11S4ModifyBearerRespRejSent = _RbnEpscS11S4ModifyBearerRespRejSent_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 2, 4, 6),
    _RbnEpscS11S4ModifyBearerRespRejSent_Type()
)
rbnEpscS11S4ModifyBearerRespRejSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscS11S4ModifyBearerRespRejSent.setStatus("current")
_RbnEpscS11S4DeleteSessionReqRcvd_Type = Counter64
_RbnEpscS11S4DeleteSessionReqRcvd_Object = MibScalar
rbnEpscS11S4DeleteSessionReqRcvd = _RbnEpscS11S4DeleteSessionReqRcvd_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 2, 4, 7),
    _RbnEpscS11S4DeleteSessionReqRcvd_Type()
)
rbnEpscS11S4DeleteSessionReqRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscS11S4DeleteSessionReqRcvd.setStatus("current")
_RbnEpscS11S4DeleteSessionRespAccSent_Type = Counter64
_RbnEpscS11S4DeleteSessionRespAccSent_Object = MibScalar
rbnEpscS11S4DeleteSessionRespAccSent = _RbnEpscS11S4DeleteSessionRespAccSent_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 2, 4, 8),
    _RbnEpscS11S4DeleteSessionRespAccSent_Type()
)
rbnEpscS11S4DeleteSessionRespAccSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscS11S4DeleteSessionRespAccSent.setStatus("current")
_RbnEpscS11S4DeleteSessionRespRejSent_Type = Counter64
_RbnEpscS11S4DeleteSessionRespRejSent_Object = MibScalar
rbnEpscS11S4DeleteSessionRespRejSent = _RbnEpscS11S4DeleteSessionRespRejSent_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 2, 4, 9),
    _RbnEpscS11S4DeleteSessionRespRejSent_Type()
)
rbnEpscS11S4DeleteSessionRespRejSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscS11S4DeleteSessionRespRejSent.setStatus("current")
_RbnEpscS11S4DlDataNotificationSent_Type = Counter64
_RbnEpscS11S4DlDataNotificationSent_Object = MibScalar
rbnEpscS11S4DlDataNotificationSent = _RbnEpscS11S4DlDataNotificationSent_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 2, 4, 10),
    _RbnEpscS11S4DlDataNotificationSent_Type()
)
rbnEpscS11S4DlDataNotificationSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscS11S4DlDataNotificationSent.setStatus("current")
_RbnEpscS11S4DlDataNotificationAckRcvd_Type = Counter64
_RbnEpscS11S4DlDataNotificationAckRcvd_Object = MibScalar
rbnEpscS11S4DlDataNotificationAckRcvd = _RbnEpscS11S4DlDataNotificationAckRcvd_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 2, 4, 11),
    _RbnEpscS11S4DlDataNotificationAckRcvd_Type()
)
rbnEpscS11S4DlDataNotificationAckRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscS11S4DlDataNotificationAckRcvd.setStatus("current")
_RbnEpscS11S4DlDataNotifFailureIndRcvd_Type = Counter64
_RbnEpscS11S4DlDataNotifFailureIndRcvd_Object = MibScalar
rbnEpscS11S4DlDataNotifFailureIndRcvd = _RbnEpscS11S4DlDataNotifFailureIndRcvd_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 2, 4, 12),
    _RbnEpscS11S4DlDataNotifFailureIndRcvd_Type()
)
rbnEpscS11S4DlDataNotifFailureIndRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscS11S4DlDataNotifFailureIndRcvd.setStatus("current")
_RbnEpscS11S4DeleteBearerReqSent_Type = Counter64
_RbnEpscS11S4DeleteBearerReqSent_Object = MibScalar
rbnEpscS11S4DeleteBearerReqSent = _RbnEpscS11S4DeleteBearerReqSent_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 2, 4, 13),
    _RbnEpscS11S4DeleteBearerReqSent_Type()
)
rbnEpscS11S4DeleteBearerReqSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscS11S4DeleteBearerReqSent.setStatus("current")
_RbnEpscS11S4DeleteBearerRespAccRcvd_Type = Counter64
_RbnEpscS11S4DeleteBearerRespAccRcvd_Object = MibScalar
rbnEpscS11S4DeleteBearerRespAccRcvd = _RbnEpscS11S4DeleteBearerRespAccRcvd_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 2, 4, 14),
    _RbnEpscS11S4DeleteBearerRespAccRcvd_Type()
)
rbnEpscS11S4DeleteBearerRespAccRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscS11S4DeleteBearerRespAccRcvd.setStatus("current")
_RbnEpscS11S4DeleteBearerRespRejRcvd_Type = Counter64
_RbnEpscS11S4DeleteBearerRespRejRcvd_Object = MibScalar
rbnEpscS11S4DeleteBearerRespRejRcvd = _RbnEpscS11S4DeleteBearerRespRejRcvd_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 2, 4, 15),
    _RbnEpscS11S4DeleteBearerRespRejRcvd_Type()
)
rbnEpscS11S4DeleteBearerRespRejRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscS11S4DeleteBearerRespRejRcvd.setStatus("current")
_RbnEpscS11S4RelAccessBearersReqRcvd_Type = Counter64
_RbnEpscS11S4RelAccessBearersReqRcvd_Object = MibScalar
rbnEpscS11S4RelAccessBearersReqRcvd = _RbnEpscS11S4RelAccessBearersReqRcvd_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 2, 4, 16),
    _RbnEpscS11S4RelAccessBearersReqRcvd_Type()
)
rbnEpscS11S4RelAccessBearersReqRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscS11S4RelAccessBearersReqRcvd.setStatus("current")
_RbnEpscS11S4RelAccessBearersRespAccSent_Type = Counter64
_RbnEpscS11S4RelAccessBearersRespAccSent_Object = MibScalar
rbnEpscS11S4RelAccessBearersRespAccSent = _RbnEpscS11S4RelAccessBearersRespAccSent_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 2, 4, 17),
    _RbnEpscS11S4RelAccessBearersRespAccSent_Type()
)
rbnEpscS11S4RelAccessBearersRespAccSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscS11S4RelAccessBearersRespAccSent.setStatus("current")
_RbnEpscS11S4RelAccessBearersRespRejSent_Type = Counter64
_RbnEpscS11S4RelAccessBearersRespRejSent_Object = MibScalar
rbnEpscS11S4RelAccessBearersRespRejSent = _RbnEpscS11S4RelAccessBearersRespRejSent_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 2, 4, 18),
    _RbnEpscS11S4RelAccessBearersRespRejSent_Type()
)
rbnEpscS11S4RelAccessBearersRespRejSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscS11S4RelAccessBearersRespRejSent.setStatus("current")
_RbnEpscS11S4CreateBearerReqSent_Type = Counter64
_RbnEpscS11S4CreateBearerReqSent_Object = MibScalar
rbnEpscS11S4CreateBearerReqSent = _RbnEpscS11S4CreateBearerReqSent_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 2, 4, 19),
    _RbnEpscS11S4CreateBearerReqSent_Type()
)
rbnEpscS11S4CreateBearerReqSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscS11S4CreateBearerReqSent.setStatus("current")
_RbnEpscS11S4CreateBearerRespAccRcvd_Type = Counter64
_RbnEpscS11S4CreateBearerRespAccRcvd_Object = MibScalar
rbnEpscS11S4CreateBearerRespAccRcvd = _RbnEpscS11S4CreateBearerRespAccRcvd_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 2, 4, 20),
    _RbnEpscS11S4CreateBearerRespAccRcvd_Type()
)
rbnEpscS11S4CreateBearerRespAccRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscS11S4CreateBearerRespAccRcvd.setStatus("current")
_RbnEpscS11S4CreateBearerRespRejRcvd_Type = Counter64
_RbnEpscS11S4CreateBearerRespRejRcvd_Object = MibScalar
rbnEpscS11S4CreateBearerRespRejRcvd = _RbnEpscS11S4CreateBearerRespRejRcvd_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 2, 4, 21),
    _RbnEpscS11S4CreateBearerRespRejRcvd_Type()
)
rbnEpscS11S4CreateBearerRespRejRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscS11S4CreateBearerRespRejRcvd.setStatus("current")
_RbnEpscS11S4DeleteBearerCmdRcvd_Type = Counter64
_RbnEpscS11S4DeleteBearerCmdRcvd_Object = MibScalar
rbnEpscS11S4DeleteBearerCmdRcvd = _RbnEpscS11S4DeleteBearerCmdRcvd_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 2, 4, 22),
    _RbnEpscS11S4DeleteBearerCmdRcvd_Type()
)
rbnEpscS11S4DeleteBearerCmdRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscS11S4DeleteBearerCmdRcvd.setStatus("current")
_RbnEpscS11S4DeleteBearerFailureIndSent_Type = Counter64
_RbnEpscS11S4DeleteBearerFailureIndSent_Object = MibScalar
rbnEpscS11S4DeleteBearerFailureIndSent = _RbnEpscS11S4DeleteBearerFailureIndSent_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 2, 4, 23),
    _RbnEpscS11S4DeleteBearerFailureIndSent_Type()
)
rbnEpscS11S4DeleteBearerFailureIndSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscS11S4DeleteBearerFailureIndSent.setStatus("current")
_RbnEpscS11S4UpdateBearerReqSent_Type = Counter64
_RbnEpscS11S4UpdateBearerReqSent_Object = MibScalar
rbnEpscS11S4UpdateBearerReqSent = _RbnEpscS11S4UpdateBearerReqSent_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 2, 4, 24),
    _RbnEpscS11S4UpdateBearerReqSent_Type()
)
rbnEpscS11S4UpdateBearerReqSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscS11S4UpdateBearerReqSent.setStatus("current")
_RbnEpscS11S4UpdateBearerRespAccRcvd_Type = Counter64
_RbnEpscS11S4UpdateBearerRespAccRcvd_Object = MibScalar
rbnEpscS11S4UpdateBearerRespAccRcvd = _RbnEpscS11S4UpdateBearerRespAccRcvd_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 2, 4, 25),
    _RbnEpscS11S4UpdateBearerRespAccRcvd_Type()
)
rbnEpscS11S4UpdateBearerRespAccRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscS11S4UpdateBearerRespAccRcvd.setStatus("current")
_RbnEpscS11S4UpdateBearerRespRejRcvd_Type = Counter64
_RbnEpscS11S4UpdateBearerRespRejRcvd_Object = MibScalar
rbnEpscS11S4UpdateBearerRespRejRcvd = _RbnEpscS11S4UpdateBearerRespRejRcvd_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 2, 4, 26),
    _RbnEpscS11S4UpdateBearerRespRejRcvd_Type()
)
rbnEpscS11S4UpdateBearerRespRejRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscS11S4UpdateBearerRespRejRcvd.setStatus("current")
_RbnEpscSgwCharging_ObjectIdentity = ObjectIdentity
rbnEpscSgwCharging = _RbnEpscSgwCharging_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 2, 5)
)
_RbnEpscSgwCdrsEncoded_Type = Counter64
_RbnEpscSgwCdrsEncoded_Object = MibScalar
rbnEpscSgwCdrsEncoded = _RbnEpscSgwCdrsEncoded_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 2, 5, 1),
    _RbnEpscSgwCdrsEncoded_Type()
)
rbnEpscSgwCdrsEncoded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscSgwCdrsEncoded.setStatus("current")
_RbnEpscPgwStats_ObjectIdentity = ObjectIdentity
rbnEpscPgwStats = _RbnEpscPgwStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 3)
)
_RbnEpscPgwGeneral_ObjectIdentity = ObjectIdentity
rbnEpscPgwGeneral = _RbnEpscPgwGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 3, 1)
)
_RbnEpscPgwGx_ObjectIdentity = ObjectIdentity
rbnEpscPgwGx = _RbnEpscPgwGx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 3, 2)
)
_RbnEpscGxCcrInitialSent_Type = Counter64
_RbnEpscGxCcrInitialSent_Object = MibScalar
rbnEpscGxCcrInitialSent = _RbnEpscGxCcrInitialSent_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 3, 2, 1),
    _RbnEpscGxCcrInitialSent_Type()
)
rbnEpscGxCcrInitialSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscGxCcrInitialSent.setStatus("current")
_RbnEpscGxCcaInitialSuccRcvd_Type = Counter64
_RbnEpscGxCcaInitialSuccRcvd_Object = MibScalar
rbnEpscGxCcaInitialSuccRcvd = _RbnEpscGxCcaInitialSuccRcvd_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 3, 2, 2),
    _RbnEpscGxCcaInitialSuccRcvd_Type()
)
rbnEpscGxCcaInitialSuccRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscGxCcaInitialSuccRcvd.setStatus("current")
_RbnEpscGxCcaInitialFailRcvd_Type = Counter64
_RbnEpscGxCcaInitialFailRcvd_Object = MibScalar
rbnEpscGxCcaInitialFailRcvd = _RbnEpscGxCcaInitialFailRcvd_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 3, 2, 3),
    _RbnEpscGxCcaInitialFailRcvd_Type()
)
rbnEpscGxCcaInitialFailRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscGxCcaInitialFailRcvd.setStatus("current")
_RbnEpscGxCcrUpdateSent_Type = Counter64
_RbnEpscGxCcrUpdateSent_Object = MibScalar
rbnEpscGxCcrUpdateSent = _RbnEpscGxCcrUpdateSent_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 3, 2, 4),
    _RbnEpscGxCcrUpdateSent_Type()
)
rbnEpscGxCcrUpdateSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscGxCcrUpdateSent.setStatus("current")
_RbnEpscGxCcaUpdateSuccRcvd_Type = Counter64
_RbnEpscGxCcaUpdateSuccRcvd_Object = MibScalar
rbnEpscGxCcaUpdateSuccRcvd = _RbnEpscGxCcaUpdateSuccRcvd_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 3, 2, 5),
    _RbnEpscGxCcaUpdateSuccRcvd_Type()
)
rbnEpscGxCcaUpdateSuccRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscGxCcaUpdateSuccRcvd.setStatus("current")
_RbnEpscGxCcaUpdateFailRcvd_Type = Counter64
_RbnEpscGxCcaUpdateFailRcvd_Object = MibScalar
rbnEpscGxCcaUpdateFailRcvd = _RbnEpscGxCcaUpdateFailRcvd_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 3, 2, 6),
    _RbnEpscGxCcaUpdateFailRcvd_Type()
)
rbnEpscGxCcaUpdateFailRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscGxCcaUpdateFailRcvd.setStatus("current")
_RbnEpscGxCcrTerminateSent_Type = Counter64
_RbnEpscGxCcrTerminateSent_Object = MibScalar
rbnEpscGxCcrTerminateSent = _RbnEpscGxCcrTerminateSent_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 3, 2, 7),
    _RbnEpscGxCcrTerminateSent_Type()
)
rbnEpscGxCcrTerminateSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscGxCcrTerminateSent.setStatus("current")
_RbnEpscGxCcaTerminateSuccRcvd_Type = Counter64
_RbnEpscGxCcaTerminateSuccRcvd_Object = MibScalar
rbnEpscGxCcaTerminateSuccRcvd = _RbnEpscGxCcaTerminateSuccRcvd_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 3, 2, 8),
    _RbnEpscGxCcaTerminateSuccRcvd_Type()
)
rbnEpscGxCcaTerminateSuccRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscGxCcaTerminateSuccRcvd.setStatus("current")
_RbnEpscGxCcaTerminateFailRcvd_Type = Counter64
_RbnEpscGxCcaTerminateFailRcvd_Object = MibScalar
rbnEpscGxCcaTerminateFailRcvd = _RbnEpscGxCcaTerminateFailRcvd_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 3, 2, 9),
    _RbnEpscGxCcaTerminateFailRcvd_Type()
)
rbnEpscGxCcaTerminateFailRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscGxCcaTerminateFailRcvd.setStatus("current")
_RbnEpscGxRarRcvd_Type = Counter64
_RbnEpscGxRarRcvd_Object = MibScalar
rbnEpscGxRarRcvd = _RbnEpscGxRarRcvd_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 3, 2, 10),
    _RbnEpscGxRarRcvd_Type()
)
rbnEpscGxRarRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscGxRarRcvd.setStatus("current")
_RbnEpscGxRaaSuccSent_Type = Counter64
_RbnEpscGxRaaSuccSent_Object = MibScalar
rbnEpscGxRaaSuccSent = _RbnEpscGxRaaSuccSent_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 3, 2, 11),
    _RbnEpscGxRaaSuccSent_Type()
)
rbnEpscGxRaaSuccSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscGxRaaSuccSent.setStatus("current")
_RbnEpscGxRaaFailSent_Type = Counter64
_RbnEpscGxRaaFailSent_Object = MibScalar
rbnEpscGxRaaFailSent = _RbnEpscGxRaaFailSent_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 3, 2, 12),
    _RbnEpscGxRaaFailSent_Type()
)
rbnEpscGxRaaFailSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscGxRaaFailSent.setStatus("current")
_RbnEpscPgwCharging_ObjectIdentity = ObjectIdentity
rbnEpscPgwCharging = _RbnEpscPgwCharging_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 3, 3)
)
_RbnEpscPgwCdrsEncoded_Type = Counter64
_RbnEpscPgwCdrsEncoded_Object = MibScalar
rbnEpscPgwCdrsEncoded = _RbnEpscPgwCdrsEncoded_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 3, 3, 1),
    _RbnEpscPgwCdrsEncoded_Type()
)
rbnEpscPgwCdrsEncoded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscPgwCdrsEncoded.setStatus("current")
_RbnEpscPgwGnGp_ObjectIdentity = ObjectIdentity
rbnEpscPgwGnGp = _RbnEpscPgwGnGp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 3, 4)
)
_RbnEpscGnGpDeletePdpCtxReqRcvd_Type = Counter64
_RbnEpscGnGpDeletePdpCtxReqRcvd_Object = MibScalar
rbnEpscGnGpDeletePdpCtxReqRcvd = _RbnEpscGnGpDeletePdpCtxReqRcvd_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 3, 4, 1),
    _RbnEpscGnGpDeletePdpCtxReqRcvd_Type()
)
rbnEpscGnGpDeletePdpCtxReqRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscGnGpDeletePdpCtxReqRcvd.setStatus("current")
_RbnEpscGnGpDeletePdpCtxRespAccSent_Type = Counter64
_RbnEpscGnGpDeletePdpCtxRespAccSent_Object = MibScalar
rbnEpscGnGpDeletePdpCtxRespAccSent = _RbnEpscGnGpDeletePdpCtxRespAccSent_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 3, 4, 2),
    _RbnEpscGnGpDeletePdpCtxRespAccSent_Type()
)
rbnEpscGnGpDeletePdpCtxRespAccSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscGnGpDeletePdpCtxRespAccSent.setStatus("current")
_RbnEpscGnGpUpdatePdpCtxReqRcvd_Type = Counter64
_RbnEpscGnGpUpdatePdpCtxReqRcvd_Object = MibScalar
rbnEpscGnGpUpdatePdpCtxReqRcvd = _RbnEpscGnGpUpdatePdpCtxReqRcvd_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 3, 4, 3),
    _RbnEpscGnGpUpdatePdpCtxReqRcvd_Type()
)
rbnEpscGnGpUpdatePdpCtxReqRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscGnGpUpdatePdpCtxReqRcvd.setStatus("current")
_RbnEpscGnGpUpdatePdpCtxRespAccSent_Type = Counter64
_RbnEpscGnGpUpdatePdpCtxRespAccSent_Object = MibScalar
rbnEpscGnGpUpdatePdpCtxRespAccSent = _RbnEpscGnGpUpdatePdpCtxRespAccSent_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 3, 4, 4),
    _RbnEpscGnGpUpdatePdpCtxRespAccSent_Type()
)
rbnEpscGnGpUpdatePdpCtxRespAccSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscGnGpUpdatePdpCtxRespAccSent.setStatus("current")
_RbnEpscGnGpCreatePdpCtxReqRcvd_Type = Counter64
_RbnEpscGnGpCreatePdpCtxReqRcvd_Object = MibScalar
rbnEpscGnGpCreatePdpCtxReqRcvd = _RbnEpscGnGpCreatePdpCtxReqRcvd_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 3, 4, 5),
    _RbnEpscGnGpCreatePdpCtxReqRcvd_Type()
)
rbnEpscGnGpCreatePdpCtxReqRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscGnGpCreatePdpCtxReqRcvd.setStatus("current")
_RbnEpscGnGpCreatePdpCtxRespAccSent_Type = Counter64
_RbnEpscGnGpCreatePdpCtxRespAccSent_Object = MibScalar
rbnEpscGnGpCreatePdpCtxRespAccSent = _RbnEpscGnGpCreatePdpCtxRespAccSent_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 3, 4, 6),
    _RbnEpscGnGpCreatePdpCtxRespAccSent_Type()
)
rbnEpscGnGpCreatePdpCtxRespAccSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscGnGpCreatePdpCtxRespAccSent.setStatus("current")
_RbnEpscGnGpUpdatePdpCtxRespRejSent_Type = Counter64
_RbnEpscGnGpUpdatePdpCtxRespRejSent_Object = MibScalar
rbnEpscGnGpUpdatePdpCtxRespRejSent = _RbnEpscGnGpUpdatePdpCtxRespRejSent_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 3, 4, 7),
    _RbnEpscGnGpUpdatePdpCtxRespRejSent_Type()
)
rbnEpscGnGpUpdatePdpCtxRespRejSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscGnGpUpdatePdpCtxRespRejSent.setStatus("current")
_RbnEpscGnGpDeletePdpCtxRespRejSent_Type = Counter64
_RbnEpscGnGpDeletePdpCtxRespRejSent_Object = MibScalar
rbnEpscGnGpDeletePdpCtxRespRejSent = _RbnEpscGnGpDeletePdpCtxRespRejSent_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 3, 4, 8),
    _RbnEpscGnGpDeletePdpCtxRespRejSent_Type()
)
rbnEpscGnGpDeletePdpCtxRespRejSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscGnGpDeletePdpCtxRespRejSent.setStatus("current")
_RbnEpscGnGpCreatePdpCtxRespRejSent_Type = Counter64
_RbnEpscGnGpCreatePdpCtxRespRejSent_Object = MibScalar
rbnEpscGnGpCreatePdpCtxRespRejSent = _RbnEpscGnGpCreatePdpCtxRespRejSent_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 3, 4, 9),
    _RbnEpscGnGpCreatePdpCtxRespRejSent_Type()
)
rbnEpscGnGpCreatePdpCtxRespRejSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscGnGpCreatePdpCtxRespRejSent.setStatus("current")
_RbnEpscGnGpUpdatePdpCtxReqSent_Type = Counter64
_RbnEpscGnGpUpdatePdpCtxReqSent_Object = MibScalar
rbnEpscGnGpUpdatePdpCtxReqSent = _RbnEpscGnGpUpdatePdpCtxReqSent_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 3, 4, 10),
    _RbnEpscGnGpUpdatePdpCtxReqSent_Type()
)
rbnEpscGnGpUpdatePdpCtxReqSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscGnGpUpdatePdpCtxReqSent.setStatus("current")
_RbnEpscGnGpUpdatePdpCtxRespAccRcvd_Type = Counter64
_RbnEpscGnGpUpdatePdpCtxRespAccRcvd_Object = MibScalar
rbnEpscGnGpUpdatePdpCtxRespAccRcvd = _RbnEpscGnGpUpdatePdpCtxRespAccRcvd_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 3, 4, 11),
    _RbnEpscGnGpUpdatePdpCtxRespAccRcvd_Type()
)
rbnEpscGnGpUpdatePdpCtxRespAccRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscGnGpUpdatePdpCtxRespAccRcvd.setStatus("current")
_RbnEpscGnGpUpdatePdpCtxRespRejRcvd_Type = Counter64
_RbnEpscGnGpUpdatePdpCtxRespRejRcvd_Object = MibScalar
rbnEpscGnGpUpdatePdpCtxRespRejRcvd = _RbnEpscGnGpUpdatePdpCtxRespRejRcvd_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 3, 4, 12),
    _RbnEpscGnGpUpdatePdpCtxRespRejRcvd_Type()
)
rbnEpscGnGpUpdatePdpCtxRespRejRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscGnGpUpdatePdpCtxRespRejRcvd.setStatus("current")
_RbnEpscGnGpDeletePdpCtxReqSent_Type = Counter64
_RbnEpscGnGpDeletePdpCtxReqSent_Object = MibScalar
rbnEpscGnGpDeletePdpCtxReqSent = _RbnEpscGnGpDeletePdpCtxReqSent_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 3, 4, 13),
    _RbnEpscGnGpDeletePdpCtxReqSent_Type()
)
rbnEpscGnGpDeletePdpCtxReqSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscGnGpDeletePdpCtxReqSent.setStatus("current")
_RbnEpscGnGpDeletePdpCtxRespAccRcvd_Type = Counter64
_RbnEpscGnGpDeletePdpCtxRespAccRcvd_Object = MibScalar
rbnEpscGnGpDeletePdpCtxRespAccRcvd = _RbnEpscGnGpDeletePdpCtxRespAccRcvd_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 3, 4, 14),
    _RbnEpscGnGpDeletePdpCtxRespAccRcvd_Type()
)
rbnEpscGnGpDeletePdpCtxRespAccRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscGnGpDeletePdpCtxRespAccRcvd.setStatus("current")
_RbnEpscGnGpDeletePdpCtxRespRejRcvd_Type = Counter64
_RbnEpscGnGpDeletePdpCtxRespRejRcvd_Object = MibScalar
rbnEpscGnGpDeletePdpCtxRespRejRcvd = _RbnEpscGnGpDeletePdpCtxRespRejRcvd_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 3, 4, 15),
    _RbnEpscGnGpDeletePdpCtxRespRejRcvd_Type()
)
rbnEpscGnGpDeletePdpCtxRespRejRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscGnGpDeletePdpCtxRespRejRcvd.setStatus("current")
_RbnEpscPgwS5S8Gtp_ObjectIdentity = ObjectIdentity
rbnEpscPgwS5S8Gtp = _RbnEpscPgwS5S8Gtp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 3, 5)
)
_RbnEpscS5S8CreateSessionReqRcvd_Type = Counter64
_RbnEpscS5S8CreateSessionReqRcvd_Object = MibScalar
rbnEpscS5S8CreateSessionReqRcvd = _RbnEpscS5S8CreateSessionReqRcvd_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 3, 5, 1),
    _RbnEpscS5S8CreateSessionReqRcvd_Type()
)
rbnEpscS5S8CreateSessionReqRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscS5S8CreateSessionReqRcvd.setStatus("current")
_RbnEpscS5S8CreateSessionRespAccSent_Type = Counter64
_RbnEpscS5S8CreateSessionRespAccSent_Object = MibScalar
rbnEpscS5S8CreateSessionRespAccSent = _RbnEpscS5S8CreateSessionRespAccSent_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 3, 5, 2),
    _RbnEpscS5S8CreateSessionRespAccSent_Type()
)
rbnEpscS5S8CreateSessionRespAccSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscS5S8CreateSessionRespAccSent.setStatus("current")
_RbnEpscS5S8CreateSessionRespRejSent_Type = Counter64
_RbnEpscS5S8CreateSessionRespRejSent_Object = MibScalar
rbnEpscS5S8CreateSessionRespRejSent = _RbnEpscS5S8CreateSessionRespRejSent_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 3, 5, 3),
    _RbnEpscS5S8CreateSessionRespRejSent_Type()
)
rbnEpscS5S8CreateSessionRespRejSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscS5S8CreateSessionRespRejSent.setStatus("current")
_RbnEpscS5S8ModifyBearerReqRcvd_Type = Counter64
_RbnEpscS5S8ModifyBearerReqRcvd_Object = MibScalar
rbnEpscS5S8ModifyBearerReqRcvd = _RbnEpscS5S8ModifyBearerReqRcvd_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 3, 5, 4),
    _RbnEpscS5S8ModifyBearerReqRcvd_Type()
)
rbnEpscS5S8ModifyBearerReqRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscS5S8ModifyBearerReqRcvd.setStatus("current")
_RbnEpscS5S8ModifyBearerRespAccSent_Type = Counter64
_RbnEpscS5S8ModifyBearerRespAccSent_Object = MibScalar
rbnEpscS5S8ModifyBearerRespAccSent = _RbnEpscS5S8ModifyBearerRespAccSent_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 3, 5, 5),
    _RbnEpscS5S8ModifyBearerRespAccSent_Type()
)
rbnEpscS5S8ModifyBearerRespAccSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscS5S8ModifyBearerRespAccSent.setStatus("current")
_RbnEpscS5S8ModifyBearerRespRejSent_Type = Counter64
_RbnEpscS5S8ModifyBearerRespRejSent_Object = MibScalar
rbnEpscS5S8ModifyBearerRespRejSent = _RbnEpscS5S8ModifyBearerRespRejSent_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 3, 5, 6),
    _RbnEpscS5S8ModifyBearerRespRejSent_Type()
)
rbnEpscS5S8ModifyBearerRespRejSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscS5S8ModifyBearerRespRejSent.setStatus("current")
_RbnEpscS5S8DeleteSessionReqRcvd_Type = Counter64
_RbnEpscS5S8DeleteSessionReqRcvd_Object = MibScalar
rbnEpscS5S8DeleteSessionReqRcvd = _RbnEpscS5S8DeleteSessionReqRcvd_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 3, 5, 7),
    _RbnEpscS5S8DeleteSessionReqRcvd_Type()
)
rbnEpscS5S8DeleteSessionReqRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscS5S8DeleteSessionReqRcvd.setStatus("current")
_RbnEpscS5S8DeleteSessionRespAccSent_Type = Counter64
_RbnEpscS5S8DeleteSessionRespAccSent_Object = MibScalar
rbnEpscS5S8DeleteSessionRespAccSent = _RbnEpscS5S8DeleteSessionRespAccSent_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 3, 5, 8),
    _RbnEpscS5S8DeleteSessionRespAccSent_Type()
)
rbnEpscS5S8DeleteSessionRespAccSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscS5S8DeleteSessionRespAccSent.setStatus("current")
_RbnEpscS5S8DeleteSessionRespRejSent_Type = Counter64
_RbnEpscS5S8DeleteSessionRespRejSent_Object = MibScalar
rbnEpscS5S8DeleteSessionRespRejSent = _RbnEpscS5S8DeleteSessionRespRejSent_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 3, 5, 9),
    _RbnEpscS5S8DeleteSessionRespRejSent_Type()
)
rbnEpscS5S8DeleteSessionRespRejSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscS5S8DeleteSessionRespRejSent.setStatus("current")
_RbnEpscS5S8CreateBearerReqSent_Type = Counter64
_RbnEpscS5S8CreateBearerReqSent_Object = MibScalar
rbnEpscS5S8CreateBearerReqSent = _RbnEpscS5S8CreateBearerReqSent_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 3, 5, 10),
    _RbnEpscS5S8CreateBearerReqSent_Type()
)
rbnEpscS5S8CreateBearerReqSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscS5S8CreateBearerReqSent.setStatus("current")
_RbnEpscS5S8CreateBearerRespAccRcvd_Type = Counter64
_RbnEpscS5S8CreateBearerRespAccRcvd_Object = MibScalar
rbnEpscS5S8CreateBearerRespAccRcvd = _RbnEpscS5S8CreateBearerRespAccRcvd_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 3, 5, 11),
    _RbnEpscS5S8CreateBearerRespAccRcvd_Type()
)
rbnEpscS5S8CreateBearerRespAccRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscS5S8CreateBearerRespAccRcvd.setStatus("current")
_RbnEpscS5S8CreateBearerRespRejRcvd_Type = Counter64
_RbnEpscS5S8CreateBearerRespRejRcvd_Object = MibScalar
rbnEpscS5S8CreateBearerRespRejRcvd = _RbnEpscS5S8CreateBearerRespRejRcvd_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 3, 5, 12),
    _RbnEpscS5S8CreateBearerRespRejRcvd_Type()
)
rbnEpscS5S8CreateBearerRespRejRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscS5S8CreateBearerRespRejRcvd.setStatus("current")
_RbnEpscS5S8DeleteBearerCmdRcvd_Type = Counter64
_RbnEpscS5S8DeleteBearerCmdRcvd_Object = MibScalar
rbnEpscS5S8DeleteBearerCmdRcvd = _RbnEpscS5S8DeleteBearerCmdRcvd_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 3, 5, 13),
    _RbnEpscS5S8DeleteBearerCmdRcvd_Type()
)
rbnEpscS5S8DeleteBearerCmdRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscS5S8DeleteBearerCmdRcvd.setStatus("current")
_RbnEpscS5S8DeleteBearerFailureIndSent_Type = Counter64
_RbnEpscS5S8DeleteBearerFailureIndSent_Object = MibScalar
rbnEpscS5S8DeleteBearerFailureIndSent = _RbnEpscS5S8DeleteBearerFailureIndSent_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 3, 5, 14),
    _RbnEpscS5S8DeleteBearerFailureIndSent_Type()
)
rbnEpscS5S8DeleteBearerFailureIndSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscS5S8DeleteBearerFailureIndSent.setStatus("current")
_RbnEpscS5S8DeleteBearerReqSent_Type = Counter64
_RbnEpscS5S8DeleteBearerReqSent_Object = MibScalar
rbnEpscS5S8DeleteBearerReqSent = _RbnEpscS5S8DeleteBearerReqSent_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 3, 5, 15),
    _RbnEpscS5S8DeleteBearerReqSent_Type()
)
rbnEpscS5S8DeleteBearerReqSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscS5S8DeleteBearerReqSent.setStatus("current")
_RbnEpscS5S8DeleteBearerRespAccRcvd_Type = Counter64
_RbnEpscS5S8DeleteBearerRespAccRcvd_Object = MibScalar
rbnEpscS5S8DeleteBearerRespAccRcvd = _RbnEpscS5S8DeleteBearerRespAccRcvd_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 3, 5, 16),
    _RbnEpscS5S8DeleteBearerRespAccRcvd_Type()
)
rbnEpscS5S8DeleteBearerRespAccRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscS5S8DeleteBearerRespAccRcvd.setStatus("current")
_RbnEpscS5S8DeleteBearerRespRejRcvd_Type = Counter64
_RbnEpscS5S8DeleteBearerRespRejRcvd_Object = MibScalar
rbnEpscS5S8DeleteBearerRespRejRcvd = _RbnEpscS5S8DeleteBearerRespRejRcvd_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 3, 5, 17),
    _RbnEpscS5S8DeleteBearerRespRejRcvd_Type()
)
rbnEpscS5S8DeleteBearerRespRejRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscS5S8DeleteBearerRespRejRcvd.setStatus("current")
_RbnEpscS5S8UpdateBearerReqSent_Type = Counter64
_RbnEpscS5S8UpdateBearerReqSent_Object = MibScalar
rbnEpscS5S8UpdateBearerReqSent = _RbnEpscS5S8UpdateBearerReqSent_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 3, 5, 18),
    _RbnEpscS5S8UpdateBearerReqSent_Type()
)
rbnEpscS5S8UpdateBearerReqSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscS5S8UpdateBearerReqSent.setStatus("current")
_RbnEpscS5S8UpdateBearerRespAccRcvd_Type = Counter64
_RbnEpscS5S8UpdateBearerRespAccRcvd_Object = MibScalar
rbnEpscS5S8UpdateBearerRespAccRcvd = _RbnEpscS5S8UpdateBearerRespAccRcvd_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 3, 5, 19),
    _RbnEpscS5S8UpdateBearerRespAccRcvd_Type()
)
rbnEpscS5S8UpdateBearerRespAccRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscS5S8UpdateBearerRespAccRcvd.setStatus("current")
_RbnEpscS5S8UpdateBearerRespRejRcvd_Type = Counter64
_RbnEpscS5S8UpdateBearerRespRejRcvd_Object = MibScalar
rbnEpscS5S8UpdateBearerRespRejRcvd = _RbnEpscS5S8UpdateBearerRespRejRcvd_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 3, 5, 20),
    _RbnEpscS5S8UpdateBearerRespRejRcvd_Type()
)
rbnEpscS5S8UpdateBearerRespRejRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscS5S8UpdateBearerRespRejRcvd.setStatus("current")
_RbnEpscPgwGy_ObjectIdentity = ObjectIdentity
rbnEpscPgwGy = _RbnEpscPgwGy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 3, 6)
)
_RbnEpscGyCcrInitialSent_Type = Counter64
_RbnEpscGyCcrInitialSent_Object = MibScalar
rbnEpscGyCcrInitialSent = _RbnEpscGyCcrInitialSent_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 3, 6, 1),
    _RbnEpscGyCcrInitialSent_Type()
)
rbnEpscGyCcrInitialSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscGyCcrInitialSent.setStatus("current")
_RbnEpscGyCcaInitialSuccRcvd_Type = Counter64
_RbnEpscGyCcaInitialSuccRcvd_Object = MibScalar
rbnEpscGyCcaInitialSuccRcvd = _RbnEpscGyCcaInitialSuccRcvd_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 3, 6, 2),
    _RbnEpscGyCcaInitialSuccRcvd_Type()
)
rbnEpscGyCcaInitialSuccRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscGyCcaInitialSuccRcvd.setStatus("current")
_RbnEpscGyCcrTerminateSent_Type = Counter64
_RbnEpscGyCcrTerminateSent_Object = MibScalar
rbnEpscGyCcrTerminateSent = _RbnEpscGyCcrTerminateSent_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 3, 6, 3),
    _RbnEpscGyCcrTerminateSent_Type()
)
rbnEpscGyCcrTerminateSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscGyCcrTerminateSent.setStatus("current")
_RbnEpscGyCcaTerminateSuccRcvd_Type = Counter64
_RbnEpscGyCcaTerminateSuccRcvd_Object = MibScalar
rbnEpscGyCcaTerminateSuccRcvd = _RbnEpscGyCcaTerminateSuccRcvd_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 3, 6, 4),
    _RbnEpscGyCcaTerminateSuccRcvd_Type()
)
rbnEpscGyCcaTerminateSuccRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscGyCcaTerminateSuccRcvd.setStatus("current")
_RbnEpscGyCcaInitialFailRcvd_Type = Counter64
_RbnEpscGyCcaInitialFailRcvd_Object = MibScalar
rbnEpscGyCcaInitialFailRcvd = _RbnEpscGyCcaInitialFailRcvd_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 3, 6, 5),
    _RbnEpscGyCcaInitialFailRcvd_Type()
)
rbnEpscGyCcaInitialFailRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscGyCcaInitialFailRcvd.setStatus("current")
_RbnEpscGyCcaTerminateFailRcvd_Type = Counter64
_RbnEpscGyCcaTerminateFailRcvd_Object = MibScalar
rbnEpscGyCcaTerminateFailRcvd = _RbnEpscGyCcaTerminateFailRcvd_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 3, 6, 6),
    _RbnEpscGyCcaTerminateFailRcvd_Type()
)
rbnEpscGyCcaTerminateFailRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscGyCcaTerminateFailRcvd.setStatus("current")
_RbnEpscPgwS2aPmip_ObjectIdentity = ObjectIdentity
rbnEpscPgwS2aPmip = _RbnEpscPgwS2aPmip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 3, 7)
)
_RbnEpscS2aPmipMsgInvalidRcvd_Type = Counter64
_RbnEpscS2aPmipMsgInvalidRcvd_Object = MibScalar
rbnEpscS2aPmipMsgInvalidRcvd = _RbnEpscS2aPmipMsgInvalidRcvd_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 3, 7, 1),
    _RbnEpscS2aPmipMsgInvalidRcvd_Type()
)
rbnEpscS2aPmipMsgInvalidRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscS2aPmipMsgInvalidRcvd.setStatus("current")
_RbnEpscS2aPbuPdnConnCreateRcvd_Type = Counter64
_RbnEpscS2aPbuPdnConnCreateRcvd_Object = MibScalar
rbnEpscS2aPbuPdnConnCreateRcvd = _RbnEpscS2aPbuPdnConnCreateRcvd_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 3, 7, 2),
    _RbnEpscS2aPbuPdnConnCreateRcvd_Type()
)
rbnEpscS2aPbuPdnConnCreateRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscS2aPbuPdnConnCreateRcvd.setStatus("current")
_RbnEpscS2aPbaPdnConnCreateAccSent_Type = Counter64
_RbnEpscS2aPbaPdnConnCreateAccSent_Object = MibScalar
rbnEpscS2aPbaPdnConnCreateAccSent = _RbnEpscS2aPbaPdnConnCreateAccSent_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 3, 7, 3),
    _RbnEpscS2aPbaPdnConnCreateAccSent_Type()
)
rbnEpscS2aPbaPdnConnCreateAccSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscS2aPbaPdnConnCreateAccSent.setStatus("current")
_RbnEpscS2aPbaPdnConnCreateRejSent_Type = Counter64
_RbnEpscS2aPbaPdnConnCreateRejSent_Object = MibScalar
rbnEpscS2aPbaPdnConnCreateRejSent = _RbnEpscS2aPbaPdnConnCreateRejSent_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 3, 7, 4),
    _RbnEpscS2aPbaPdnConnCreateRejSent_Type()
)
rbnEpscS2aPbaPdnConnCreateRejSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscS2aPbaPdnConnCreateRejSent.setStatus("current")
_RbnEpscS2aPbuPdnConnLifeExtRcvd_Type = Counter64
_RbnEpscS2aPbuPdnConnLifeExtRcvd_Object = MibScalar
rbnEpscS2aPbuPdnConnLifeExtRcvd = _RbnEpscS2aPbuPdnConnLifeExtRcvd_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 3, 7, 5),
    _RbnEpscS2aPbuPdnConnLifeExtRcvd_Type()
)
rbnEpscS2aPbuPdnConnLifeExtRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscS2aPbuPdnConnLifeExtRcvd.setStatus("current")
_RbnEpscS2aPbaPdnConnLifeExtAccSent_Type = Counter64
_RbnEpscS2aPbaPdnConnLifeExtAccSent_Object = MibScalar
rbnEpscS2aPbaPdnConnLifeExtAccSent = _RbnEpscS2aPbaPdnConnLifeExtAccSent_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 3, 7, 6),
    _RbnEpscS2aPbaPdnConnLifeExtAccSent_Type()
)
rbnEpscS2aPbaPdnConnLifeExtAccSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscS2aPbaPdnConnLifeExtAccSent.setStatus("current")
_RbnEpscS2aPbaPdnConnLifeExtRejSent_Type = Counter64
_RbnEpscS2aPbaPdnConnLifeExtRejSent_Object = MibScalar
rbnEpscS2aPbaPdnConnLifeExtRejSent = _RbnEpscS2aPbaPdnConnLifeExtRejSent_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 3, 7, 7),
    _RbnEpscS2aPbaPdnConnLifeExtRejSent_Type()
)
rbnEpscS2aPbaPdnConnLifeExtRejSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscS2aPbaPdnConnLifeExtRejSent.setStatus("current")
_RbnEpscS2aPbuPdnConnDeletionRcvd_Type = Counter64
_RbnEpscS2aPbuPdnConnDeletionRcvd_Object = MibScalar
rbnEpscS2aPbuPdnConnDeletionRcvd = _RbnEpscS2aPbuPdnConnDeletionRcvd_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 3, 7, 8),
    _RbnEpscS2aPbuPdnConnDeletionRcvd_Type()
)
rbnEpscS2aPbuPdnConnDeletionRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscS2aPbuPdnConnDeletionRcvd.setStatus("current")
_RbnEpscS2aPbaPdnConnDeletionAccSent_Type = Counter64
_RbnEpscS2aPbaPdnConnDeletionAccSent_Object = MibScalar
rbnEpscS2aPbaPdnConnDeletionAccSent = _RbnEpscS2aPbaPdnConnDeletionAccSent_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 3, 7, 9),
    _RbnEpscS2aPbaPdnConnDeletionAccSent_Type()
)
rbnEpscS2aPbaPdnConnDeletionAccSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscS2aPbaPdnConnDeletionAccSent.setStatus("current")
_RbnEpscS2aPbaPdnConnDeletionRejSent_Type = Counter64
_RbnEpscS2aPbaPdnConnDeletionRejSent_Object = MibScalar
rbnEpscS2aPbaPdnConnDeletionRejSent = _RbnEpscS2aPbaPdnConnDeletionRejSent_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 3, 7, 10),
    _RbnEpscS2aPbaPdnConnDeletionRejSent_Type()
)
rbnEpscS2aPbaPdnConnDeletionRejSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscS2aPbaPdnConnDeletionRejSent.setStatus("current")
_RbnEpscS2aBriPdnConnDeletionSent_Type = Counter64
_RbnEpscS2aBriPdnConnDeletionSent_Object = MibScalar
rbnEpscS2aBriPdnConnDeletionSent = _RbnEpscS2aBriPdnConnDeletionSent_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 3, 7, 11),
    _RbnEpscS2aBriPdnConnDeletionSent_Type()
)
rbnEpscS2aBriPdnConnDeletionSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscS2aBriPdnConnDeletionSent.setStatus("current")
_RbnEpscS2aBraPdnConnDeletionAccRcvd_Type = Counter64
_RbnEpscS2aBraPdnConnDeletionAccRcvd_Object = MibScalar
rbnEpscS2aBraPdnConnDeletionAccRcvd = _RbnEpscS2aBraPdnConnDeletionAccRcvd_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 3, 7, 12),
    _RbnEpscS2aBraPdnConnDeletionAccRcvd_Type()
)
rbnEpscS2aBraPdnConnDeletionAccRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscS2aBraPdnConnDeletionAccRcvd.setStatus("current")
_RbnEpscS2aBraPdnConnDeletionRejRcvd_Type = Counter64
_RbnEpscS2aBraPdnConnDeletionRejRcvd_Object = MibScalar
rbnEpscS2aBraPdnConnDeletionRejRcvd = _RbnEpscS2aBraPdnConnDeletionRejRcvd_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 3, 7, 13),
    _RbnEpscS2aBraPdnConnDeletionRejRcvd_Type()
)
rbnEpscS2aBraPdnConnDeletionRejRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscS2aBraPdnConnDeletionRejRcvd.setStatus("current")
_RbnEpscS2aPbuPdnConnHoIntraRcvd_Type = Counter64
_RbnEpscS2aPbuPdnConnHoIntraRcvd_Object = MibScalar
rbnEpscS2aPbuPdnConnHoIntraRcvd = _RbnEpscS2aPbuPdnConnHoIntraRcvd_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 3, 7, 14),
    _RbnEpscS2aPbuPdnConnHoIntraRcvd_Type()
)
rbnEpscS2aPbuPdnConnHoIntraRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscS2aPbuPdnConnHoIntraRcvd.setStatus("current")
_RbnEpscS2aPbaPdnConnHoIntraAccSent_Type = Counter64
_RbnEpscS2aPbaPdnConnHoIntraAccSent_Object = MibScalar
rbnEpscS2aPbaPdnConnHoIntraAccSent = _RbnEpscS2aPbaPdnConnHoIntraAccSent_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 3, 7, 15),
    _RbnEpscS2aPbaPdnConnHoIntraAccSent_Type()
)
rbnEpscS2aPbaPdnConnHoIntraAccSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscS2aPbaPdnConnHoIntraAccSent.setStatus("current")
_RbnEpscS2aPbaPdnConnHoIntraRejSent_Type = Counter64
_RbnEpscS2aPbaPdnConnHoIntraRejSent_Object = MibScalar
rbnEpscS2aPbaPdnConnHoIntraRejSent = _RbnEpscS2aPbaPdnConnHoIntraRejSent_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 3, 7, 16),
    _RbnEpscS2aPbaPdnConnHoIntraRejSent_Type()
)
rbnEpscS2aPbaPdnConnHoIntraRejSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscS2aPbaPdnConnHoIntraRejSent.setStatus("current")
_RbnEpscS2aBraPdnConnDeletionInvalidRcvd_Type = Counter64
_RbnEpscS2aBraPdnConnDeletionInvalidRcvd_Object = MibScalar
rbnEpscS2aBraPdnConnDeletionInvalidRcvd = _RbnEpscS2aBraPdnConnDeletionInvalidRcvd_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 3, 7, 17),
    _RbnEpscS2aBraPdnConnDeletionInvalidRcvd_Type()
)
rbnEpscS2aBraPdnConnDeletionInvalidRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscS2aBraPdnConnDeletionInvalidRcvd.setStatus("current")
_RbnEpscPgwS6b_ObjectIdentity = ObjectIdentity
rbnEpscPgwS6b = _RbnEpscPgwS6b_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 3, 8)
)
_RbnEpscS6bAarSent_Type = Counter64
_RbnEpscS6bAarSent_Object = MibScalar
rbnEpscS6bAarSent = _RbnEpscS6bAarSent_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 3, 8, 1),
    _RbnEpscS6bAarSent_Type()
)
rbnEpscS6bAarSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscS6bAarSent.setStatus("current")
_RbnEpscS6bAaaSuccRcvd_Type = Counter64
_RbnEpscS6bAaaSuccRcvd_Object = MibScalar
rbnEpscS6bAaaSuccRcvd = _RbnEpscS6bAaaSuccRcvd_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 3, 8, 2),
    _RbnEpscS6bAaaSuccRcvd_Type()
)
rbnEpscS6bAaaSuccRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscS6bAaaSuccRcvd.setStatus("current")
_RbnEpscS6bAaaFailRcvd_Type = Counter64
_RbnEpscS6bAaaFailRcvd_Object = MibScalar
rbnEpscS6bAaaFailRcvd = _RbnEpscS6bAaaFailRcvd_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 3, 8, 3),
    _RbnEpscS6bAaaFailRcvd_Type()
)
rbnEpscS6bAaaFailRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscS6bAaaFailRcvd.setStatus("current")
_RbnEpscS6bAaaInvalidRcvd_Type = Counter64
_RbnEpscS6bAaaInvalidRcvd_Object = MibScalar
rbnEpscS6bAaaInvalidRcvd = _RbnEpscS6bAaaInvalidRcvd_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 3, 8, 4),
    _RbnEpscS6bAaaInvalidRcvd_Type()
)
rbnEpscS6bAaaInvalidRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscS6bAaaInvalidRcvd.setStatus("current")
_RbnEpscS6bStrSent_Type = Counter64
_RbnEpscS6bStrSent_Object = MibScalar
rbnEpscS6bStrSent = _RbnEpscS6bStrSent_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 3, 8, 5),
    _RbnEpscS6bStrSent_Type()
)
rbnEpscS6bStrSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscS6bStrSent.setStatus("current")
_RbnEpscS6bStaSuccRcvd_Type = Counter64
_RbnEpscS6bStaSuccRcvd_Object = MibScalar
rbnEpscS6bStaSuccRcvd = _RbnEpscS6bStaSuccRcvd_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 3, 8, 6),
    _RbnEpscS6bStaSuccRcvd_Type()
)
rbnEpscS6bStaSuccRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscS6bStaSuccRcvd.setStatus("current")
_RbnEpscS6bStaFailRcvd_Type = Counter64
_RbnEpscS6bStaFailRcvd_Object = MibScalar
rbnEpscS6bStaFailRcvd = _RbnEpscS6bStaFailRcvd_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 1, 3, 8, 7),
    _RbnEpscS6bStaFailRcvd_Type()
)
rbnEpscS6bStaFailRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpscS6bStaFailRcvd.setStatus("current")
_RbnEpscMIBConformance_ObjectIdentity = ObjectIdentity
rbnEpscMIBConformance = _RbnEpscMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 2)
)
_RbnEpscMIBGroups_ObjectIdentity = ObjectIdentity
rbnEpscMIBGroups = _RbnEpscMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 2, 1)
)
_RbnEpscMIBCompliances_ObjectIdentity = ObjectIdentity
rbnEpscMIBCompliances = _RbnEpscMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 2, 2)
)

# Managed Objects groups

rbnEpscCommonGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 2, 1, 1)
)
rbnEpscCommonGeneralGroup.setObjects(
      *(("RBN-EPSC-MIB", "rbnEpscConnectionsEstablished"),
        ("RBN-EPSC-MIB", "rbnEpscPdnConnectionTimeout"),
        ("RBN-EPSC-MIB", "rbnEpscBearersEstablished"),
        ("RBN-EPSC-MIB", "rbnEpscUeAttached"))
)
if mibBuilder.loadTexts:
    rbnEpscCommonGeneralGroup.setStatus("current")

rbnEpscCommonChargingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 2, 1, 2)
)
rbnEpscCommonChargingGroup.setObjects(
      *(("RBN-EPSC-MIB", "rbnEpscClosedCdrFiles"),
        ("RBN-EPSC-MIB", "rbnEpscRfAcrSent"),
        ("RBN-EPSC-MIB", "rbnEpscRfAcaSuccRcvd"),
        ("RBN-EPSC-MIB", "rbnEpscRfAcaFailRcvd"),
        ("RBN-EPSC-MIB", "rbnEpscRfAcrWrittenToDisk"))
)
if mibBuilder.loadTexts:
    rbnEpscCommonChargingGroup.setStatus("current")

rbnEpscSgwGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 2, 1, 3)
)
rbnEpscSgwGeneralGroup.setObjects(
    ("RBN-EPSC-MIB", "rbnEpscSgwUeEcmConnected")
)
if mibBuilder.loadTexts:
    rbnEpscSgwGeneralGroup.setStatus("current")

rbnEpscSgwS5S8GtpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 2, 1, 4)
)
rbnEpscSgwS5S8GtpGroup.setObjects(
      *(("RBN-EPSC-MIB", "rbnEpscS5S8CreateSessionReqSent"),
        ("RBN-EPSC-MIB", "rbnEpscS5S8CreateSessionRespAccRcvd"),
        ("RBN-EPSC-MIB", "rbnEpscS5S8CreateSessionRespRejRcvd"),
        ("RBN-EPSC-MIB", "rbnEpscS5S8DeleteBearerReqRcvd"),
        ("RBN-EPSC-MIB", "rbnEpscS5S8DeleteBearerRespAccSent"),
        ("RBN-EPSC-MIB", "rbnEpscS5S8DeleteBearerRespRejSent"),
        ("RBN-EPSC-MIB", "rbnEpscS5S8DeleteSessionReqSent"),
        ("RBN-EPSC-MIB", "rbnEpscS5S8DeleteSessionRespAccRcvd"),
        ("RBN-EPSC-MIB", "rbnEpscS5S8DeleteSessionRespRejRcvd"),
        ("RBN-EPSC-MIB", "rbnEpscS5S8ModifyBearerReqSent"),
        ("RBN-EPSC-MIB", "rbnEpscS5S8ModifyBearerRespAccRcvd"),
        ("RBN-EPSC-MIB", "rbnEpscS5S8ModifyBearerRespRejRcvd"),
        ("RBN-EPSC-MIB", "rbnEpscS5S8CreateBearerReqRcvd"),
        ("RBN-EPSC-MIB", "rbnEpscS5S8CreateBearerRespAccSent"),
        ("RBN-EPSC-MIB", "rbnEpscS5S8CreateBearerRespRejSent"),
        ("RBN-EPSC-MIB", "rbnEpscS5S8DeleteBearerCmdSent"),
        ("RBN-EPSC-MIB", "rbnEpscS5S8DeleteBearerFailureIndRcvd"),
        ("RBN-EPSC-MIB", "rbnEpscS5S8UpdateBearerReqRcvd"),
        ("RBN-EPSC-MIB", "rbnEpscS5S8UpdateBearerRespAccSent"),
        ("RBN-EPSC-MIB", "rbnEpscS5S8UpdateBearerRespRejSent"))
)
if mibBuilder.loadTexts:
    rbnEpscSgwS5S8GtpGroup.setStatus("current")

rbnEpscSgwS11S4Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 2, 1, 5)
)
rbnEpscSgwS11S4Group.setObjects(
      *(("RBN-EPSC-MIB", "rbnEpscS11S4CreateSessionReqRcvd"),
        ("RBN-EPSC-MIB", "rbnEpscS11S4CreateSessionRespAccSent"),
        ("RBN-EPSC-MIB", "rbnEpscS11S4CreateSessionRespRejSent"),
        ("RBN-EPSC-MIB", "rbnEpscS11S4ModifyBearerReqRcvd"),
        ("RBN-EPSC-MIB", "rbnEpscS11S4ModifyBearerRespAccSent"),
        ("RBN-EPSC-MIB", "rbnEpscS11S4ModifyBearerRespRejSent"),
        ("RBN-EPSC-MIB", "rbnEpscS11S4DeleteSessionReqRcvd"),
        ("RBN-EPSC-MIB", "rbnEpscS11S4DeleteSessionRespAccSent"),
        ("RBN-EPSC-MIB", "rbnEpscS11S4DeleteSessionRespRejSent"),
        ("RBN-EPSC-MIB", "rbnEpscS11S4DlDataNotificationSent"),
        ("RBN-EPSC-MIB", "rbnEpscS11S4DlDataNotificationAckRcvd"),
        ("RBN-EPSC-MIB", "rbnEpscS11S4DlDataNotifFailureIndRcvd"),
        ("RBN-EPSC-MIB", "rbnEpscS11S4DeleteBearerReqSent"),
        ("RBN-EPSC-MIB", "rbnEpscS11S4DeleteBearerRespAccRcvd"),
        ("RBN-EPSC-MIB", "rbnEpscS11S4DeleteBearerRespRejRcvd"),
        ("RBN-EPSC-MIB", "rbnEpscS11S4RelAccessBearersReqRcvd"),
        ("RBN-EPSC-MIB", "rbnEpscS11S4RelAccessBearersRespAccSent"),
        ("RBN-EPSC-MIB", "rbnEpscS11S4RelAccessBearersRespRejSent"),
        ("RBN-EPSC-MIB", "rbnEpscS11S4CreateBearerReqSent"),
        ("RBN-EPSC-MIB", "rbnEpscS11S4CreateBearerRespAccRcvd"),
        ("RBN-EPSC-MIB", "rbnEpscS11S4CreateBearerRespRejRcvd"),
        ("RBN-EPSC-MIB", "rbnEpscS11S4DeleteBearerCmdRcvd"),
        ("RBN-EPSC-MIB", "rbnEpscS11S4DeleteBearerFailureIndSent"),
        ("RBN-EPSC-MIB", "rbnEpscS11S4UpdateBearerReqSent"),
        ("RBN-EPSC-MIB", "rbnEpscS11S4UpdateBearerRespAccRcvd"),
        ("RBN-EPSC-MIB", "rbnEpscS11S4UpdateBearerRespRejRcvd"))
)
if mibBuilder.loadTexts:
    rbnEpscSgwS11S4Group.setStatus("current")

rbnEpscSgwChargingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 2, 1, 6)
)
rbnEpscSgwChargingGroup.setObjects(
    ("RBN-EPSC-MIB", "rbnEpscSgwCdrsEncoded")
)
if mibBuilder.loadTexts:
    rbnEpscSgwChargingGroup.setStatus("current")

rbnEpscPgwGxGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 2, 1, 8)
)
rbnEpscPgwGxGroup.setObjects(
      *(("RBN-EPSC-MIB", "rbnEpscGxCcaInitialFailRcvd"),
        ("RBN-EPSC-MIB", "rbnEpscGxCcaInitialSuccRcvd"),
        ("RBN-EPSC-MIB", "rbnEpscGxCcaTerminateFailRcvd"),
        ("RBN-EPSC-MIB", "rbnEpscGxCcaTerminateSuccRcvd"),
        ("RBN-EPSC-MIB", "rbnEpscGxCcaUpdateFailRcvd"),
        ("RBN-EPSC-MIB", "rbnEpscGxCcaUpdateSuccRcvd"),
        ("RBN-EPSC-MIB", "rbnEpscGxCcrInitialSent"),
        ("RBN-EPSC-MIB", "rbnEpscGxCcrTerminateSent"),
        ("RBN-EPSC-MIB", "rbnEpscGxCcrUpdateSent"),
        ("RBN-EPSC-MIB", "rbnEpscGxRaaFailSent"),
        ("RBN-EPSC-MIB", "rbnEpscGxRaaSuccSent"),
        ("RBN-EPSC-MIB", "rbnEpscGxRarRcvd"))
)
if mibBuilder.loadTexts:
    rbnEpscPgwGxGroup.setStatus("current")

rbnEpscPgwChargingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 2, 1, 9)
)
rbnEpscPgwChargingGroup.setObjects(
    ("RBN-EPSC-MIB", "rbnEpscPgwCdrsEncoded")
)
if mibBuilder.loadTexts:
    rbnEpscPgwChargingGroup.setStatus("current")

rbnEpscPgwS5S8GtpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 2, 1, 11)
)
rbnEpscPgwS5S8GtpGroup.setObjects(
      *(("RBN-EPSC-MIB", "rbnEpscS5S8CreateSessionReqRcvd"),
        ("RBN-EPSC-MIB", "rbnEpscS5S8CreateSessionRespAccSent"),
        ("RBN-EPSC-MIB", "rbnEpscS5S8CreateSessionRespRejSent"),
        ("RBN-EPSC-MIB", "rbnEpscS5S8ModifyBearerReqRcvd"),
        ("RBN-EPSC-MIB", "rbnEpscS5S8ModifyBearerRespAccSent"),
        ("RBN-EPSC-MIB", "rbnEpscS5S8ModifyBearerRespRejSent"),
        ("RBN-EPSC-MIB", "rbnEpscS5S8DeleteSessionReqRcvd"),
        ("RBN-EPSC-MIB", "rbnEpscS5S8DeleteSessionRespAccSent"),
        ("RBN-EPSC-MIB", "rbnEpscS5S8DeleteSessionRespRejSent"),
        ("RBN-EPSC-MIB", "rbnEpscS5S8CreateBearerReqSent"),
        ("RBN-EPSC-MIB", "rbnEpscS5S8CreateBearerRespAccRcvd"),
        ("RBN-EPSC-MIB", "rbnEpscS5S8CreateBearerRespRejRcvd"),
        ("RBN-EPSC-MIB", "rbnEpscS5S8DeleteBearerCmdRcvd"),
        ("RBN-EPSC-MIB", "rbnEpscS5S8DeleteBearerFailureIndSent"),
        ("RBN-EPSC-MIB", "rbnEpscS5S8DeleteBearerReqSent"),
        ("RBN-EPSC-MIB", "rbnEpscS5S8DeleteBearerRespAccRcvd"),
        ("RBN-EPSC-MIB", "rbnEpscS5S8DeleteBearerRespRejRcvd"),
        ("RBN-EPSC-MIB", "rbnEpscS5S8UpdateBearerReqSent"),
        ("RBN-EPSC-MIB", "rbnEpscS5S8UpdateBearerRespAccRcvd"),
        ("RBN-EPSC-MIB", "rbnEpscS5S8UpdateBearerRespRejRcvd"))
)
if mibBuilder.loadTexts:
    rbnEpscPgwS5S8GtpGroup.setStatus("current")

rbnEpscPgwGnGpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 2, 1, 13)
)
rbnEpscPgwGnGpGroup.setObjects(
      *(("RBN-EPSC-MIB", "rbnEpscGnGpDeletePdpCtxReqRcvd"),
        ("RBN-EPSC-MIB", "rbnEpscGnGpDeletePdpCtxRespAccSent"),
        ("RBN-EPSC-MIB", "rbnEpscGnGpUpdatePdpCtxReqRcvd"),
        ("RBN-EPSC-MIB", "rbnEpscGnGpUpdatePdpCtxRespAccSent"),
        ("RBN-EPSC-MIB", "rbnEpscGnGpCreatePdpCtxReqRcvd"),
        ("RBN-EPSC-MIB", "rbnEpscGnGpCreatePdpCtxRespAccSent"),
        ("RBN-EPSC-MIB", "rbnEpscGnGpUpdatePdpCtxRespRejSent"),
        ("RBN-EPSC-MIB", "rbnEpscGnGpDeletePdpCtxRespRejSent"),
        ("RBN-EPSC-MIB", "rbnEpscGnGpCreatePdpCtxRespRejSent"),
        ("RBN-EPSC-MIB", "rbnEpscGnGpUpdatePdpCtxReqSent"),
        ("RBN-EPSC-MIB", "rbnEpscGnGpUpdatePdpCtxRespAccRcvd"),
        ("RBN-EPSC-MIB", "rbnEpscGnGpUpdatePdpCtxRespRejRcvd"),
        ("RBN-EPSC-MIB", "rbnEpscGnGpDeletePdpCtxReqSent"),
        ("RBN-EPSC-MIB", "rbnEpscGnGpDeletePdpCtxRespAccRcvd"),
        ("RBN-EPSC-MIB", "rbnEpscGnGpDeletePdpCtxRespRejRcvd"))
)
if mibBuilder.loadTexts:
    rbnEpscPgwGnGpGroup.setStatus("current")

rbnEpscPgwGyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 2, 1, 14)
)
rbnEpscPgwGyGroup.setObjects(
      *(("RBN-EPSC-MIB", "rbnEpscGyCcaInitialFailRcvd"),
        ("RBN-EPSC-MIB", "rbnEpscGyCcaInitialSuccRcvd"),
        ("RBN-EPSC-MIB", "rbnEpscGyCcaTerminateFailRcvd"),
        ("RBN-EPSC-MIB", "rbnEpscGyCcaTerminateSuccRcvd"),
        ("RBN-EPSC-MIB", "rbnEpscGyCcrInitialSent"),
        ("RBN-EPSC-MIB", "rbnEpscGyCcrTerminateSent"))
)
if mibBuilder.loadTexts:
    rbnEpscPgwGyGroup.setStatus("current")

rbnEpscPgwS2aPmipGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 2, 1, 15)
)
rbnEpscPgwS2aPmipGroup.setObjects(
      *(("RBN-EPSC-MIB", "rbnEpscS2aPmipMsgInvalidRcvd"),
        ("RBN-EPSC-MIB", "rbnEpscS2aPbuPdnConnCreateRcvd"),
        ("RBN-EPSC-MIB", "rbnEpscS2aPbaPdnConnCreateAccSent"),
        ("RBN-EPSC-MIB", "rbnEpscS2aPbaPdnConnCreateRejSent"),
        ("RBN-EPSC-MIB", "rbnEpscS2aPbuPdnConnLifeExtRcvd"),
        ("RBN-EPSC-MIB", "rbnEpscS2aPbaPdnConnLifeExtAccSent"),
        ("RBN-EPSC-MIB", "rbnEpscS2aPbaPdnConnLifeExtRejSent"),
        ("RBN-EPSC-MIB", "rbnEpscS2aPbuPdnConnDeletionRcvd"),
        ("RBN-EPSC-MIB", "rbnEpscS2aPbaPdnConnDeletionAccSent"),
        ("RBN-EPSC-MIB", "rbnEpscS2aPbaPdnConnDeletionRejSent"),
        ("RBN-EPSC-MIB", "rbnEpscS2aBriPdnConnDeletionSent"),
        ("RBN-EPSC-MIB", "rbnEpscS2aBraPdnConnDeletionAccRcvd"),
        ("RBN-EPSC-MIB", "rbnEpscS2aBraPdnConnDeletionRejRcvd"),
        ("RBN-EPSC-MIB", "rbnEpscS2aPbuPdnConnHoIntraRcvd"),
        ("RBN-EPSC-MIB", "rbnEpscS2aPbaPdnConnHoIntraAccSent"),
        ("RBN-EPSC-MIB", "rbnEpscS2aPbaPdnConnHoIntraRejSent"),
        ("RBN-EPSC-MIB", "rbnEpscS2aBraPdnConnDeletionInvalidRcvd"))
)
if mibBuilder.loadTexts:
    rbnEpscPgwS2aPmipGroup.setStatus("current")

rbnEpscPgwS6bGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 2, 1, 16)
)
rbnEpscPgwS6bGroup.setObjects(
      *(("RBN-EPSC-MIB", "rbnEpscS6bAarSent"),
        ("RBN-EPSC-MIB", "rbnEpscS6bAaaSuccRcvd"),
        ("RBN-EPSC-MIB", "rbnEpscS6bAaaFailRcvd"),
        ("RBN-EPSC-MIB", "rbnEpscS6bAaaInvalidRcvd"),
        ("RBN-EPSC-MIB", "rbnEpscS6bStrSent"),
        ("RBN-EPSC-MIB", "rbnEpscS6bStaSuccRcvd"),
        ("RBN-EPSC-MIB", "rbnEpscS6bStaFailRcvd"))
)
if mibBuilder.loadTexts:
    rbnEpscPgwS6bGroup.setStatus("current")

rbnEpscCommonDiameterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 2, 1, 17)
)
rbnEpscCommonDiameterGroup.setObjects(
    ("RBN-EPSC-MIB", "rbnEpscDiameterMsgInvalidRcvd")
)
if mibBuilder.loadTexts:
    rbnEpscCommonDiameterGroup.setStatus("current")

rbnEpscCommonIcrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 2, 1, 18)
)
rbnEpscCommonIcrGroup.setObjects(
      *(("RBN-EPSC-MIB", "rbnEpscIcrCreateSessionSyncRcvd"),
        ("RBN-EPSC-MIB", "rbnEpscIcrCreateSessionSyncSent"),
        ("RBN-EPSC-MIB", "rbnEpscIcrDeleteSessionSyncRcvd"),
        ("RBN-EPSC-MIB", "rbnEpscIcrDeleteSessionSyncSent"))
)
if mibBuilder.loadTexts:
    rbnEpscCommonIcrGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

rbnEpscMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2352, 2, 44, 2, 2, 1)
)
if mibBuilder.loadTexts:
    rbnEpscMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RBN-EPSC-MIB",
    **{"rbnEpscMIB": rbnEpscMIB,
       "rbnEpscMIBObjects": rbnEpscMIBObjects,
       "rbnEpscCommonStats": rbnEpscCommonStats,
       "rbnEpscCommonGeneral": rbnEpscCommonGeneral,
       "rbnEpscConnectionsEstablished": rbnEpscConnectionsEstablished,
       "rbnEpscPdnConnectionTimeout": rbnEpscPdnConnectionTimeout,
       "rbnEpscBearersEstablished": rbnEpscBearersEstablished,
       "rbnEpscUeAttached": rbnEpscUeAttached,
       "rbnEpscCommonCharging": rbnEpscCommonCharging,
       "rbnEpscClosedCdrFiles": rbnEpscClosedCdrFiles,
       "rbnEpscRfAcrSent": rbnEpscRfAcrSent,
       "rbnEpscRfAcaSuccRcvd": rbnEpscRfAcaSuccRcvd,
       "rbnEpscRfAcaFailRcvd": rbnEpscRfAcaFailRcvd,
       "rbnEpscRfAcrWrittenToDisk": rbnEpscRfAcrWrittenToDisk,
       "rbnEpscCommonDiameter": rbnEpscCommonDiameter,
       "rbnEpscDiameterMsgInvalidRcvd": rbnEpscDiameterMsgInvalidRcvd,
       "rbnEpscCommonIcr": rbnEpscCommonIcr,
       "rbnEpscIcrCreateSessionSyncRcvd": rbnEpscIcrCreateSessionSyncRcvd,
       "rbnEpscIcrCreateSessionSyncSent": rbnEpscIcrCreateSessionSyncSent,
       "rbnEpscIcrDeleteSessionSyncRcvd": rbnEpscIcrDeleteSessionSyncRcvd,
       "rbnEpscIcrDeleteSessionSyncSent": rbnEpscIcrDeleteSessionSyncSent,
       "rbnEpscSgwStats": rbnEpscSgwStats,
       "rbnEpscSgwGeneral": rbnEpscSgwGeneral,
       "rbnEpscSgwUeEcmConnected": rbnEpscSgwUeEcmConnected,
       "rbnEpscSgwS5S8Gtp": rbnEpscSgwS5S8Gtp,
       "rbnEpscS5S8CreateSessionReqSent": rbnEpscS5S8CreateSessionReqSent,
       "rbnEpscS5S8CreateSessionRespAccRcvd": rbnEpscS5S8CreateSessionRespAccRcvd,
       "rbnEpscS5S8CreateSessionRespRejRcvd": rbnEpscS5S8CreateSessionRespRejRcvd,
       "rbnEpscS5S8DeleteSessionReqSent": rbnEpscS5S8DeleteSessionReqSent,
       "rbnEpscS5S8DeleteSessionRespAccRcvd": rbnEpscS5S8DeleteSessionRespAccRcvd,
       "rbnEpscS5S8DeleteSessionRespRejRcvd": rbnEpscS5S8DeleteSessionRespRejRcvd,
       "rbnEpscS5S8DeleteBearerReqRcvd": rbnEpscS5S8DeleteBearerReqRcvd,
       "rbnEpscS5S8DeleteBearerRespAccSent": rbnEpscS5S8DeleteBearerRespAccSent,
       "rbnEpscS5S8DeleteBearerRespRejSent": rbnEpscS5S8DeleteBearerRespRejSent,
       "rbnEpscS5S8CreateBearerReqRcvd": rbnEpscS5S8CreateBearerReqRcvd,
       "rbnEpscS5S8CreateBearerRespAccSent": rbnEpscS5S8CreateBearerRespAccSent,
       "rbnEpscS5S8CreateBearerRespRejSent": rbnEpscS5S8CreateBearerRespRejSent,
       "rbnEpscS5S8DeleteBearerCmdSent": rbnEpscS5S8DeleteBearerCmdSent,
       "rbnEpscS5S8DeleteBearerFailureIndRcvd": rbnEpscS5S8DeleteBearerFailureIndRcvd,
       "rbnEpscS5S8UpdateBearerReqRcvd": rbnEpscS5S8UpdateBearerReqRcvd,
       "rbnEpscS5S8UpdateBearerRespAccSent": rbnEpscS5S8UpdateBearerRespAccSent,
       "rbnEpscS5S8UpdateBearerRespRejSent": rbnEpscS5S8UpdateBearerRespRejSent,
       "rbnEpscS5S8ModifyBearerReqSent": rbnEpscS5S8ModifyBearerReqSent,
       "rbnEpscS5S8ModifyBearerRespAccRcvd": rbnEpscS5S8ModifyBearerRespAccRcvd,
       "rbnEpscS5S8ModifyBearerRespRejRcvd": rbnEpscS5S8ModifyBearerRespRejRcvd,
       "rbnEpscSgwS11S4": rbnEpscSgwS11S4,
       "rbnEpscS11S4CreateSessionReqRcvd": rbnEpscS11S4CreateSessionReqRcvd,
       "rbnEpscS11S4CreateSessionRespAccSent": rbnEpscS11S4CreateSessionRespAccSent,
       "rbnEpscS11S4CreateSessionRespRejSent": rbnEpscS11S4CreateSessionRespRejSent,
       "rbnEpscS11S4ModifyBearerReqRcvd": rbnEpscS11S4ModifyBearerReqRcvd,
       "rbnEpscS11S4ModifyBearerRespAccSent": rbnEpscS11S4ModifyBearerRespAccSent,
       "rbnEpscS11S4ModifyBearerRespRejSent": rbnEpscS11S4ModifyBearerRespRejSent,
       "rbnEpscS11S4DeleteSessionReqRcvd": rbnEpscS11S4DeleteSessionReqRcvd,
       "rbnEpscS11S4DeleteSessionRespAccSent": rbnEpscS11S4DeleteSessionRespAccSent,
       "rbnEpscS11S4DeleteSessionRespRejSent": rbnEpscS11S4DeleteSessionRespRejSent,
       "rbnEpscS11S4DlDataNotificationSent": rbnEpscS11S4DlDataNotificationSent,
       "rbnEpscS11S4DlDataNotificationAckRcvd": rbnEpscS11S4DlDataNotificationAckRcvd,
       "rbnEpscS11S4DlDataNotifFailureIndRcvd": rbnEpscS11S4DlDataNotifFailureIndRcvd,
       "rbnEpscS11S4DeleteBearerReqSent": rbnEpscS11S4DeleteBearerReqSent,
       "rbnEpscS11S4DeleteBearerRespAccRcvd": rbnEpscS11S4DeleteBearerRespAccRcvd,
       "rbnEpscS11S4DeleteBearerRespRejRcvd": rbnEpscS11S4DeleteBearerRespRejRcvd,
       "rbnEpscS11S4RelAccessBearersReqRcvd": rbnEpscS11S4RelAccessBearersReqRcvd,
       "rbnEpscS11S4RelAccessBearersRespAccSent": rbnEpscS11S4RelAccessBearersRespAccSent,
       "rbnEpscS11S4RelAccessBearersRespRejSent": rbnEpscS11S4RelAccessBearersRespRejSent,
       "rbnEpscS11S4CreateBearerReqSent": rbnEpscS11S4CreateBearerReqSent,
       "rbnEpscS11S4CreateBearerRespAccRcvd": rbnEpscS11S4CreateBearerRespAccRcvd,
       "rbnEpscS11S4CreateBearerRespRejRcvd": rbnEpscS11S4CreateBearerRespRejRcvd,
       "rbnEpscS11S4DeleteBearerCmdRcvd": rbnEpscS11S4DeleteBearerCmdRcvd,
       "rbnEpscS11S4DeleteBearerFailureIndSent": rbnEpscS11S4DeleteBearerFailureIndSent,
       "rbnEpscS11S4UpdateBearerReqSent": rbnEpscS11S4UpdateBearerReqSent,
       "rbnEpscS11S4UpdateBearerRespAccRcvd": rbnEpscS11S4UpdateBearerRespAccRcvd,
       "rbnEpscS11S4UpdateBearerRespRejRcvd": rbnEpscS11S4UpdateBearerRespRejRcvd,
       "rbnEpscSgwCharging": rbnEpscSgwCharging,
       "rbnEpscSgwCdrsEncoded": rbnEpscSgwCdrsEncoded,
       "rbnEpscPgwStats": rbnEpscPgwStats,
       "rbnEpscPgwGeneral": rbnEpscPgwGeneral,
       "rbnEpscPgwGx": rbnEpscPgwGx,
       "rbnEpscGxCcrInitialSent": rbnEpscGxCcrInitialSent,
       "rbnEpscGxCcaInitialSuccRcvd": rbnEpscGxCcaInitialSuccRcvd,
       "rbnEpscGxCcaInitialFailRcvd": rbnEpscGxCcaInitialFailRcvd,
       "rbnEpscGxCcrUpdateSent": rbnEpscGxCcrUpdateSent,
       "rbnEpscGxCcaUpdateSuccRcvd": rbnEpscGxCcaUpdateSuccRcvd,
       "rbnEpscGxCcaUpdateFailRcvd": rbnEpscGxCcaUpdateFailRcvd,
       "rbnEpscGxCcrTerminateSent": rbnEpscGxCcrTerminateSent,
       "rbnEpscGxCcaTerminateSuccRcvd": rbnEpscGxCcaTerminateSuccRcvd,
       "rbnEpscGxCcaTerminateFailRcvd": rbnEpscGxCcaTerminateFailRcvd,
       "rbnEpscGxRarRcvd": rbnEpscGxRarRcvd,
       "rbnEpscGxRaaSuccSent": rbnEpscGxRaaSuccSent,
       "rbnEpscGxRaaFailSent": rbnEpscGxRaaFailSent,
       "rbnEpscPgwCharging": rbnEpscPgwCharging,
       "rbnEpscPgwCdrsEncoded": rbnEpscPgwCdrsEncoded,
       "rbnEpscPgwGnGp": rbnEpscPgwGnGp,
       "rbnEpscGnGpDeletePdpCtxReqRcvd": rbnEpscGnGpDeletePdpCtxReqRcvd,
       "rbnEpscGnGpDeletePdpCtxRespAccSent": rbnEpscGnGpDeletePdpCtxRespAccSent,
       "rbnEpscGnGpUpdatePdpCtxReqRcvd": rbnEpscGnGpUpdatePdpCtxReqRcvd,
       "rbnEpscGnGpUpdatePdpCtxRespAccSent": rbnEpscGnGpUpdatePdpCtxRespAccSent,
       "rbnEpscGnGpCreatePdpCtxReqRcvd": rbnEpscGnGpCreatePdpCtxReqRcvd,
       "rbnEpscGnGpCreatePdpCtxRespAccSent": rbnEpscGnGpCreatePdpCtxRespAccSent,
       "rbnEpscGnGpUpdatePdpCtxRespRejSent": rbnEpscGnGpUpdatePdpCtxRespRejSent,
       "rbnEpscGnGpDeletePdpCtxRespRejSent": rbnEpscGnGpDeletePdpCtxRespRejSent,
       "rbnEpscGnGpCreatePdpCtxRespRejSent": rbnEpscGnGpCreatePdpCtxRespRejSent,
       "rbnEpscGnGpUpdatePdpCtxReqSent": rbnEpscGnGpUpdatePdpCtxReqSent,
       "rbnEpscGnGpUpdatePdpCtxRespAccRcvd": rbnEpscGnGpUpdatePdpCtxRespAccRcvd,
       "rbnEpscGnGpUpdatePdpCtxRespRejRcvd": rbnEpscGnGpUpdatePdpCtxRespRejRcvd,
       "rbnEpscGnGpDeletePdpCtxReqSent": rbnEpscGnGpDeletePdpCtxReqSent,
       "rbnEpscGnGpDeletePdpCtxRespAccRcvd": rbnEpscGnGpDeletePdpCtxRespAccRcvd,
       "rbnEpscGnGpDeletePdpCtxRespRejRcvd": rbnEpscGnGpDeletePdpCtxRespRejRcvd,
       "rbnEpscPgwS5S8Gtp": rbnEpscPgwS5S8Gtp,
       "rbnEpscS5S8CreateSessionReqRcvd": rbnEpscS5S8CreateSessionReqRcvd,
       "rbnEpscS5S8CreateSessionRespAccSent": rbnEpscS5S8CreateSessionRespAccSent,
       "rbnEpscS5S8CreateSessionRespRejSent": rbnEpscS5S8CreateSessionRespRejSent,
       "rbnEpscS5S8ModifyBearerReqRcvd": rbnEpscS5S8ModifyBearerReqRcvd,
       "rbnEpscS5S8ModifyBearerRespAccSent": rbnEpscS5S8ModifyBearerRespAccSent,
       "rbnEpscS5S8ModifyBearerRespRejSent": rbnEpscS5S8ModifyBearerRespRejSent,
       "rbnEpscS5S8DeleteSessionReqRcvd": rbnEpscS5S8DeleteSessionReqRcvd,
       "rbnEpscS5S8DeleteSessionRespAccSent": rbnEpscS5S8DeleteSessionRespAccSent,
       "rbnEpscS5S8DeleteSessionRespRejSent": rbnEpscS5S8DeleteSessionRespRejSent,
       "rbnEpscS5S8CreateBearerReqSent": rbnEpscS5S8CreateBearerReqSent,
       "rbnEpscS5S8CreateBearerRespAccRcvd": rbnEpscS5S8CreateBearerRespAccRcvd,
       "rbnEpscS5S8CreateBearerRespRejRcvd": rbnEpscS5S8CreateBearerRespRejRcvd,
       "rbnEpscS5S8DeleteBearerCmdRcvd": rbnEpscS5S8DeleteBearerCmdRcvd,
       "rbnEpscS5S8DeleteBearerFailureIndSent": rbnEpscS5S8DeleteBearerFailureIndSent,
       "rbnEpscS5S8DeleteBearerReqSent": rbnEpscS5S8DeleteBearerReqSent,
       "rbnEpscS5S8DeleteBearerRespAccRcvd": rbnEpscS5S8DeleteBearerRespAccRcvd,
       "rbnEpscS5S8DeleteBearerRespRejRcvd": rbnEpscS5S8DeleteBearerRespRejRcvd,
       "rbnEpscS5S8UpdateBearerReqSent": rbnEpscS5S8UpdateBearerReqSent,
       "rbnEpscS5S8UpdateBearerRespAccRcvd": rbnEpscS5S8UpdateBearerRespAccRcvd,
       "rbnEpscS5S8UpdateBearerRespRejRcvd": rbnEpscS5S8UpdateBearerRespRejRcvd,
       "rbnEpscPgwGy": rbnEpscPgwGy,
       "rbnEpscGyCcrInitialSent": rbnEpscGyCcrInitialSent,
       "rbnEpscGyCcaInitialSuccRcvd": rbnEpscGyCcaInitialSuccRcvd,
       "rbnEpscGyCcrTerminateSent": rbnEpscGyCcrTerminateSent,
       "rbnEpscGyCcaTerminateSuccRcvd": rbnEpscGyCcaTerminateSuccRcvd,
       "rbnEpscGyCcaInitialFailRcvd": rbnEpscGyCcaInitialFailRcvd,
       "rbnEpscGyCcaTerminateFailRcvd": rbnEpscGyCcaTerminateFailRcvd,
       "rbnEpscPgwS2aPmip": rbnEpscPgwS2aPmip,
       "rbnEpscS2aPmipMsgInvalidRcvd": rbnEpscS2aPmipMsgInvalidRcvd,
       "rbnEpscS2aPbuPdnConnCreateRcvd": rbnEpscS2aPbuPdnConnCreateRcvd,
       "rbnEpscS2aPbaPdnConnCreateAccSent": rbnEpscS2aPbaPdnConnCreateAccSent,
       "rbnEpscS2aPbaPdnConnCreateRejSent": rbnEpscS2aPbaPdnConnCreateRejSent,
       "rbnEpscS2aPbuPdnConnLifeExtRcvd": rbnEpscS2aPbuPdnConnLifeExtRcvd,
       "rbnEpscS2aPbaPdnConnLifeExtAccSent": rbnEpscS2aPbaPdnConnLifeExtAccSent,
       "rbnEpscS2aPbaPdnConnLifeExtRejSent": rbnEpscS2aPbaPdnConnLifeExtRejSent,
       "rbnEpscS2aPbuPdnConnDeletionRcvd": rbnEpscS2aPbuPdnConnDeletionRcvd,
       "rbnEpscS2aPbaPdnConnDeletionAccSent": rbnEpscS2aPbaPdnConnDeletionAccSent,
       "rbnEpscS2aPbaPdnConnDeletionRejSent": rbnEpscS2aPbaPdnConnDeletionRejSent,
       "rbnEpscS2aBriPdnConnDeletionSent": rbnEpscS2aBriPdnConnDeletionSent,
       "rbnEpscS2aBraPdnConnDeletionAccRcvd": rbnEpscS2aBraPdnConnDeletionAccRcvd,
       "rbnEpscS2aBraPdnConnDeletionRejRcvd": rbnEpscS2aBraPdnConnDeletionRejRcvd,
       "rbnEpscS2aPbuPdnConnHoIntraRcvd": rbnEpscS2aPbuPdnConnHoIntraRcvd,
       "rbnEpscS2aPbaPdnConnHoIntraAccSent": rbnEpscS2aPbaPdnConnHoIntraAccSent,
       "rbnEpscS2aPbaPdnConnHoIntraRejSent": rbnEpscS2aPbaPdnConnHoIntraRejSent,
       "rbnEpscS2aBraPdnConnDeletionInvalidRcvd": rbnEpscS2aBraPdnConnDeletionInvalidRcvd,
       "rbnEpscPgwS6b": rbnEpscPgwS6b,
       "rbnEpscS6bAarSent": rbnEpscS6bAarSent,
       "rbnEpscS6bAaaSuccRcvd": rbnEpscS6bAaaSuccRcvd,
       "rbnEpscS6bAaaFailRcvd": rbnEpscS6bAaaFailRcvd,
       "rbnEpscS6bAaaInvalidRcvd": rbnEpscS6bAaaInvalidRcvd,
       "rbnEpscS6bStrSent": rbnEpscS6bStrSent,
       "rbnEpscS6bStaSuccRcvd": rbnEpscS6bStaSuccRcvd,
       "rbnEpscS6bStaFailRcvd": rbnEpscS6bStaFailRcvd,
       "rbnEpscMIBConformance": rbnEpscMIBConformance,
       "rbnEpscMIBGroups": rbnEpscMIBGroups,
       "rbnEpscCommonGeneralGroup": rbnEpscCommonGeneralGroup,
       "rbnEpscCommonChargingGroup": rbnEpscCommonChargingGroup,
       "rbnEpscSgwGeneralGroup": rbnEpscSgwGeneralGroup,
       "rbnEpscSgwS5S8GtpGroup": rbnEpscSgwS5S8GtpGroup,
       "rbnEpscSgwS11S4Group": rbnEpscSgwS11S4Group,
       "rbnEpscSgwChargingGroup": rbnEpscSgwChargingGroup,
       "rbnEpscPgwGxGroup": rbnEpscPgwGxGroup,
       "rbnEpscPgwChargingGroup": rbnEpscPgwChargingGroup,
       "rbnEpscPgwS5S8GtpGroup": rbnEpscPgwS5S8GtpGroup,
       "rbnEpscPgwGnGpGroup": rbnEpscPgwGnGpGroup,
       "rbnEpscPgwGyGroup": rbnEpscPgwGyGroup,
       "rbnEpscPgwS2aPmipGroup": rbnEpscPgwS2aPmipGroup,
       "rbnEpscPgwS6bGroup": rbnEpscPgwS6bGroup,
       "rbnEpscCommonDiameterGroup": rbnEpscCommonDiameterGroup,
       "rbnEpscCommonIcrGroup": rbnEpscCommonIcrGroup,
       "rbnEpscMIBCompliances": rbnEpscMIBCompliances,
       "rbnEpscMIBCompliance": rbnEpscMIBCompliance}
)
