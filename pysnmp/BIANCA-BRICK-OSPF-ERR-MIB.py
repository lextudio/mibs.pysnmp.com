# SNMP MIB module (BIANCA-BRICK-OSPF-ERR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BIANCA-BRICK-OSPF-ERR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:47:36 2024
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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Bintec_ObjectIdentity = ObjectIdentity
bintec = _Bintec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272)
)
_Bibo_ObjectIdentity = ObjectIdentity
bibo = _Bibo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 4)
)
_Biboip_ObjectIdentity = ObjectIdentity
biboip = _Biboip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 4, 5)
)
_OspfErr_ObjectIdentity = ObjectIdentity
ospfErr = _OspfErr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 11)
)
_OspfErrOspfBadVersion_Type = Counter32
_OspfErrOspfBadVersion_Object = MibScalar
ospfErrOspfBadVersion = _OspfErrOspfBadVersion_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 11, 1),
    _OspfErrOspfBadVersion_Type()
)
ospfErrOspfBadVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfErrOspfBadVersion.setStatus("mandatory")
_OspfErrOspfBadPacketType_Type = Counter32
_OspfErrOspfBadPacketType_Object = MibScalar
ospfErrOspfBadPacketType = _OspfErrOspfBadPacketType_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 11, 2),
    _OspfErrOspfBadPacketType_Type()
)
ospfErrOspfBadPacketType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfErrOspfBadPacketType.setStatus("mandatory")
_OspfErrOspfBadChecksum_Type = Counter32
_OspfErrOspfBadChecksum_Object = MibScalar
ospfErrOspfBadChecksum = _OspfErrOspfBadChecksum_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 11, 3),
    _OspfErrOspfBadChecksum_Type()
)
ospfErrOspfBadChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfErrOspfBadChecksum.setStatus("mandatory")
_OspfErrIpBadDestination_Type = Counter32
_OspfErrIpBadDestination_Object = MibScalar
ospfErrIpBadDestination = _OspfErrIpBadDestination_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 11, 4),
    _OspfErrIpBadDestination_Type()
)
ospfErrIpBadDestination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfErrIpBadDestination.setStatus("mandatory")
_OspfErrOspfBadAreaId_Type = Counter32
_OspfErrOspfBadAreaId_Object = MibScalar
ospfErrOspfBadAreaId = _OspfErrOspfBadAreaId_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 11, 5),
    _OspfErrOspfBadAreaId_Type()
)
ospfErrOspfBadAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfErrOspfBadAreaId.setStatus("mandatory")
_OspfErrOspfAuthenticationFailed_Type = Counter32
_OspfErrOspfAuthenticationFailed_Object = MibScalar
ospfErrOspfAuthenticationFailed = _OspfErrOspfAuthenticationFailed_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 11, 6),
    _OspfErrOspfAuthenticationFailed_Type()
)
ospfErrOspfAuthenticationFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfErrOspfAuthenticationFailed.setStatus("mandatory")
_OspfErrOspfUnknownNeighbor_Type = Counter32
_OspfErrOspfUnknownNeighbor_Object = MibScalar
ospfErrOspfUnknownNeighbor = _OspfErrOspfUnknownNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 11, 7),
    _OspfErrOspfUnknownNeighbor_Type()
)
ospfErrOspfUnknownNeighbor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfErrOspfUnknownNeighbor.setStatus("mandatory")
_OspfErrHelloNetmaskMismatch_Type = Counter32
_OspfErrHelloNetmaskMismatch_Object = MibScalar
ospfErrHelloNetmaskMismatch = _OspfErrHelloNetmaskMismatch_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 11, 8),
    _OspfErrHelloNetmaskMismatch_Type()
)
ospfErrHelloNetmaskMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfErrHelloNetmaskMismatch.setStatus("mandatory")
_OspfErrHelloDeadTimerMismatch_Type = Counter32
_OspfErrHelloDeadTimerMismatch_Object = MibScalar
ospfErrHelloDeadTimerMismatch = _OspfErrHelloDeadTimerMismatch_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 11, 9),
    _OspfErrHelloDeadTimerMismatch_Type()
)
ospfErrHelloDeadTimerMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfErrHelloDeadTimerMismatch.setStatus("mandatory")
_OspfErrHelloTimerMismatch_Type = Counter32
_OspfErrHelloTimerMismatch_Object = MibScalar
ospfErrHelloTimerMismatch = _OspfErrHelloTimerMismatch_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 11, 10),
    _OspfErrHelloTimerMismatch_Type()
)
ospfErrHelloTimerMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfErrHelloTimerMismatch.setStatus("mandatory")
_OspfErrHelloOptionMismatch_Type = Counter32
_OspfErrHelloOptionMismatch_Object = MibScalar
ospfErrHelloOptionMismatch = _OspfErrHelloOptionMismatch_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 11, 11),
    _OspfErrHelloOptionMismatch_Type()
)
ospfErrHelloOptionMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfErrHelloOptionMismatch.setStatus("mandatory")
_OspfErrOspfRouterIdConfusion_Type = Counter32
_OspfErrOspfRouterIdConfusion_Object = MibScalar
ospfErrOspfRouterIdConfusion = _OspfErrOspfRouterIdConfusion_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 11, 12),
    _OspfErrOspfRouterIdConfusion_Type()
)
ospfErrOspfRouterIdConfusion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfErrOspfRouterIdConfusion.setStatus("mandatory")
_OspfErrOspfUnknownLsaType_Type = Counter32
_OspfErrOspfUnknownLsaType_Object = MibScalar
ospfErrOspfUnknownLsaType = _OspfErrOspfUnknownLsaType_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 11, 13),
    _OspfErrOspfUnknownLsaType_Type()
)
ospfErrOspfUnknownLsaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfErrOspfUnknownLsaType.setStatus("mandatory")
_OspfErrDdOptionMismatch_Type = Counter32
_OspfErrDdOptionMismatch_Object = MibScalar
ospfErrDdOptionMismatch = _OspfErrDdOptionMismatch_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 11, 14),
    _OspfErrDdOptionMismatch_Type()
)
ospfErrDdOptionMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfErrDdOptionMismatch.setStatus("mandatory")
_OspfErrDdNeighborStateLow_Type = Counter32
_OspfErrDdNeighborStateLow_Object = MibScalar
ospfErrDdNeighborStateLow = _OspfErrDdNeighborStateLow_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 11, 15),
    _OspfErrDdNeighborStateLow_Type()
)
ospfErrDdNeighborStateLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfErrDdNeighborStateLow.setStatus("mandatory")
_OspfErrLsackBadAck_Type = Counter32
_OspfErrLsackBadAck_Object = MibScalar
ospfErrLsackBadAck = _OspfErrLsackBadAck_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 11, 16),
    _OspfErrLsackBadAck_Type()
)
ospfErrLsackBadAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfErrLsackBadAck.setStatus("mandatory")
_OspfErrLsackDuplicateAck_Type = Counter32
_OspfErrLsackDuplicateAck_Object = MibScalar
ospfErrLsackDuplicateAck = _OspfErrLsackDuplicateAck_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 11, 17),
    _OspfErrLsackDuplicateAck_Type()
)
ospfErrLsackDuplicateAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfErrLsackDuplicateAck.setStatus("mandatory")
_OspfErrLsreqBadRequest_Type = Counter32
_OspfErrLsreqBadRequest_Object = MibScalar
ospfErrLsreqBadRequest = _OspfErrLsreqBadRequest_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 11, 18),
    _OspfErrLsreqBadRequest_Type()
)
ospfErrLsreqBadRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfErrLsreqBadRequest.setStatus("mandatory")
_OspfErrLsreqNeighborStateLow_Type = Counter32
_OspfErrLsreqNeighborStateLow_Object = MibScalar
ospfErrLsreqNeighborStateLow = _OspfErrLsreqNeighborStateLow_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 11, 19),
    _OspfErrLsreqNeighborStateLow_Type()
)
ospfErrLsreqNeighborStateLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfErrLsreqNeighborStateLow.setStatus("mandatory")
_OspfErrLsupdNeighborStateLow_Type = Counter32
_OspfErrLsupdNeighborStateLow_Object = MibScalar
ospfErrLsupdNeighborStateLow = _OspfErrLsupdNeighborStateLow_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 11, 20),
    _OspfErrLsupdNeighborStateLow_Type()
)
ospfErrLsupdNeighborStateLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfErrLsupdNeighborStateLow.setStatus("mandatory")
_OspfErrLsupdBadLsaChecksum_Type = Counter32
_OspfErrLsupdBadLsaChecksum_Object = MibScalar
ospfErrLsupdBadLsaChecksum = _OspfErrLsupdBadLsaChecksum_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 11, 21),
    _OspfErrLsupdBadLsaChecksum_Type()
)
ospfErrLsupdBadLsaChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfErrLsupdBadLsaChecksum.setStatus("mandatory")
_OspfErrLsupdNewerSelfgenLsa_Type = Counter32
_OspfErrLsupdNewerSelfgenLsa_Object = MibScalar
ospfErrLsupdNewerSelfgenLsa = _OspfErrLsupdNewerSelfgenLsa_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 11, 22),
    _OspfErrLsupdNewerSelfgenLsa_Type()
)
ospfErrLsupdNewerSelfgenLsa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfErrLsupdNewerSelfgenLsa.setStatus("mandatory")
_OspfErrLsupdLessRecentLsa_Type = Counter32
_OspfErrLsupdLessRecentLsa_Object = MibScalar
ospfErrLsupdLessRecentLsa = _OspfErrLsupdLessRecentLsa_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 11, 23),
    _OspfErrLsupdLessRecentLsa_Type()
)
ospfErrLsupdLessRecentLsa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfErrLsupdLessRecentLsa.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BIANCA-BRICK-OSPF-ERR-MIB",
    **{"bintec": bintec,
       "bibo": bibo,
       "biboip": biboip,
       "ospfErr": ospfErr,
       "ospfErrOspfBadVersion": ospfErrOspfBadVersion,
       "ospfErrOspfBadPacketType": ospfErrOspfBadPacketType,
       "ospfErrOspfBadChecksum": ospfErrOspfBadChecksum,
       "ospfErrIpBadDestination": ospfErrIpBadDestination,
       "ospfErrOspfBadAreaId": ospfErrOspfBadAreaId,
       "ospfErrOspfAuthenticationFailed": ospfErrOspfAuthenticationFailed,
       "ospfErrOspfUnknownNeighbor": ospfErrOspfUnknownNeighbor,
       "ospfErrHelloNetmaskMismatch": ospfErrHelloNetmaskMismatch,
       "ospfErrHelloDeadTimerMismatch": ospfErrHelloDeadTimerMismatch,
       "ospfErrHelloTimerMismatch": ospfErrHelloTimerMismatch,
       "ospfErrHelloOptionMismatch": ospfErrHelloOptionMismatch,
       "ospfErrOspfRouterIdConfusion": ospfErrOspfRouterIdConfusion,
       "ospfErrOspfUnknownLsaType": ospfErrOspfUnknownLsaType,
       "ospfErrDdOptionMismatch": ospfErrDdOptionMismatch,
       "ospfErrDdNeighborStateLow": ospfErrDdNeighborStateLow,
       "ospfErrLsackBadAck": ospfErrLsackBadAck,
       "ospfErrLsackDuplicateAck": ospfErrLsackDuplicateAck,
       "ospfErrLsreqBadRequest": ospfErrLsreqBadRequest,
       "ospfErrLsreqNeighborStateLow": ospfErrLsreqNeighborStateLow,
       "ospfErrLsupdNeighborStateLow": ospfErrLsupdNeighborStateLow,
       "ospfErrLsupdBadLsaChecksum": ospfErrLsupdBadLsaChecksum,
       "ospfErrLsupdNewerSelfgenLsa": ospfErrLsupdNewerSelfgenLsa,
       "ospfErrLsupdLessRecentLsa": ospfErrLsupdLessRecentLsa}
)
