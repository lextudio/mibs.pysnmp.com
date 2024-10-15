# SNMP MIB module (AcPerfMediaServices) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AcPerfMediaServices
# Produced by pysmi-1.5.4 at Mon Oct 14 20:45:03 2024
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

acPerfMediaServices = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 10, 2)
)
acPerfMediaServices.setRevisions(
        ("2003-11-20 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AudioCodes_ObjectIdentity = ObjectIdentity
audioCodes = _AudioCodes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003)
)
_AcRegistrations_ObjectIdentity = ObjectIdentity
acRegistrations = _AcRegistrations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 7)
)
_AcGeneric_ObjectIdentity = ObjectIdentity
acGeneric = _AcGeneric_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8)
)
_AcProducts_ObjectIdentity = ObjectIdentity
acProducts = _AcProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9)
)
_AcPerformance_ObjectIdentity = ObjectIdentity
acPerformance = _AcPerformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 10)
)
_AcPerfIvr_ObjectIdentity = ObjectIdentity
acPerfIvr = _AcPerfIvr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 10, 2, 1)
)
_AcPerfIvrPlayRequests_Type = Counter32
_AcPerfIvrPlayRequests_Object = MibScalar
acPerfIvrPlayRequests = _AcPerfIvrPlayRequests_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 2, 1, 1),
    _AcPerfIvrPlayRequests_Type()
)
acPerfIvrPlayRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPerfIvrPlayRequests.setStatus("deprecated")
_AcPerfIvrPlaySuccessful_Type = Counter32
_AcPerfIvrPlaySuccessful_Object = MibScalar
acPerfIvrPlaySuccessful = _AcPerfIvrPlaySuccessful_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 2, 1, 2),
    _AcPerfIvrPlaySuccessful_Type()
)
acPerfIvrPlaySuccessful.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPerfIvrPlaySuccessful.setStatus("deprecated")
_AcPerfIvrPlayFailedDueToLackOfResources_Type = Counter32
_AcPerfIvrPlayFailedDueToLackOfResources_Object = MibScalar
acPerfIvrPlayFailedDueToLackOfResources = _AcPerfIvrPlayFailedDueToLackOfResources_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 2, 1, 3),
    _AcPerfIvrPlayFailedDueToLackOfResources_Type()
)
acPerfIvrPlayFailedDueToLackOfResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPerfIvrPlayFailedDueToLackOfResources.setStatus("deprecated")
_AcPerfIvrPlayInProgress_Type = Gauge32
_AcPerfIvrPlayInProgress_Object = MibScalar
acPerfIvrPlayInProgress = _AcPerfIvrPlayInProgress_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 2, 1, 4),
    _AcPerfIvrPlayInProgress_Type()
)
acPerfIvrPlayInProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPerfIvrPlayInProgress.setStatus("deprecated")
_AcPerfIvrPlayDuration_Type = Counter32
_AcPerfIvrPlayDuration_Object = MibScalar
acPerfIvrPlayDuration = _AcPerfIvrPlayDuration_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 2, 1, 5),
    _AcPerfIvrPlayDuration_Type()
)
acPerfIvrPlayDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPerfIvrPlayDuration.setStatus("deprecated")
_AcPerfIvrPlayFailedDueToProvMismatch_Type = Counter32
_AcPerfIvrPlayFailedDueToProvMismatch_Object = MibScalar
acPerfIvrPlayFailedDueToProvMismatch = _AcPerfIvrPlayFailedDueToProvMismatch_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 2, 1, 6),
    _AcPerfIvrPlayFailedDueToProvMismatch_Type()
)
acPerfIvrPlayFailedDueToProvMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPerfIvrPlayFailedDueToProvMismatch.setStatus("deprecated")
_AcPerfIvrPlayCollectRequests_Type = Counter32
_AcPerfIvrPlayCollectRequests_Object = MibScalar
acPerfIvrPlayCollectRequests = _AcPerfIvrPlayCollectRequests_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 2, 1, 7),
    _AcPerfIvrPlayCollectRequests_Type()
)
acPerfIvrPlayCollectRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPerfIvrPlayCollectRequests.setStatus("deprecated")
_AcPerfIvrPlayCollectSuccessful_Type = Counter32
_AcPerfIvrPlayCollectSuccessful_Object = MibScalar
acPerfIvrPlayCollectSuccessful = _AcPerfIvrPlayCollectSuccessful_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 2, 1, 8),
    _AcPerfIvrPlayCollectSuccessful_Type()
)
acPerfIvrPlayCollectSuccessful.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPerfIvrPlayCollectSuccessful.setStatus("deprecated")
_AcPerfIvrPlayCollectFailedDueToLackOfResources_Type = Counter32
_AcPerfIvrPlayCollectFailedDueToLackOfResources_Object = MibScalar
acPerfIvrPlayCollectFailedDueToLackOfResources = _AcPerfIvrPlayCollectFailedDueToLackOfResources_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 2, 1, 9),
    _AcPerfIvrPlayCollectFailedDueToLackOfResources_Type()
)
acPerfIvrPlayCollectFailedDueToLackOfResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPerfIvrPlayCollectFailedDueToLackOfResources.setStatus("deprecated")
_AcPerfIvrPlayCollectFailedDueToProvMismatch_Type = Counter32
_AcPerfIvrPlayCollectFailedDueToProvMismatch_Object = MibScalar
acPerfIvrPlayCollectFailedDueToProvMismatch = _AcPerfIvrPlayCollectFailedDueToProvMismatch_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 2, 1, 10),
    _AcPerfIvrPlayCollectFailedDueToProvMismatch_Type()
)
acPerfIvrPlayCollectFailedDueToProvMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPerfIvrPlayCollectFailedDueToProvMismatch.setStatus("deprecated")
_AcPerfIvrPlayCollectInProgress_Type = Gauge32
_AcPerfIvrPlayCollectInProgress_Object = MibScalar
acPerfIvrPlayCollectInProgress = _AcPerfIvrPlayCollectInProgress_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 2, 1, 11),
    _AcPerfIvrPlayCollectInProgress_Type()
)
acPerfIvrPlayCollectInProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPerfIvrPlayCollectInProgress.setStatus("deprecated")
_AcPerfIvrPlayCollectDuration_Type = Counter32
_AcPerfIvrPlayCollectDuration_Object = MibScalar
acPerfIvrPlayCollectDuration = _AcPerfIvrPlayCollectDuration_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 2, 1, 12),
    _AcPerfIvrPlayCollectDuration_Type()
)
acPerfIvrPlayCollectDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPerfIvrPlayCollectDuration.setStatus("deprecated")
_AcPerfIvrContDigitCollectRequests_Type = Counter32
_AcPerfIvrContDigitCollectRequests_Object = MibScalar
acPerfIvrContDigitCollectRequests = _AcPerfIvrContDigitCollectRequests_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 2, 1, 13),
    _AcPerfIvrContDigitCollectRequests_Type()
)
acPerfIvrContDigitCollectRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPerfIvrContDigitCollectRequests.setStatus("deprecated")
_AcPerfIvrContDigitCollectSuccessful_Type = Counter32
_AcPerfIvrContDigitCollectSuccessful_Object = MibScalar
acPerfIvrContDigitCollectSuccessful = _AcPerfIvrContDigitCollectSuccessful_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 2, 1, 14),
    _AcPerfIvrContDigitCollectSuccessful_Type()
)
acPerfIvrContDigitCollectSuccessful.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPerfIvrContDigitCollectSuccessful.setStatus("deprecated")
_AcPerfIvrContDigitCollectFailedDueToLackOfResources_Type = Counter32
_AcPerfIvrContDigitCollectFailedDueToLackOfResources_Object = MibScalar
acPerfIvrContDigitCollectFailedDueToLackOfResources = _AcPerfIvrContDigitCollectFailedDueToLackOfResources_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 2, 1, 15),
    _AcPerfIvrContDigitCollectFailedDueToLackOfResources_Type()
)
acPerfIvrContDigitCollectFailedDueToLackOfResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPerfIvrContDigitCollectFailedDueToLackOfResources.setStatus("deprecated")
_AcPerfIvrContDigitCollectInProgress_Type = Gauge32
_AcPerfIvrContDigitCollectInProgress_Object = MibScalar
acPerfIvrContDigitCollectInProgress = _AcPerfIvrContDigitCollectInProgress_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 2, 1, 16),
    _AcPerfIvrContDigitCollectInProgress_Type()
)
acPerfIvrContDigitCollectInProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPerfIvrContDigitCollectInProgress.setStatus("deprecated")
_AcPerfIvrContDigitCollectDuration_Type = Counter32
_AcPerfIvrContDigitCollectDuration_Object = MibScalar
acPerfIvrContDigitCollectDuration = _AcPerfIvrContDigitCollectDuration_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 2, 1, 17),
    _AcPerfIvrContDigitCollectDuration_Type()
)
acPerfIvrContDigitCollectDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPerfIvrContDigitCollectDuration.setStatus("deprecated")
_AcPerfBct_ObjectIdentity = ObjectIdentity
acPerfBct = _AcPerfBct_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 10, 2, 2)
)
_AcPerfBctRequests_Type = Counter32
_AcPerfBctRequests_Object = MibScalar
acPerfBctRequests = _AcPerfBctRequests_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 2, 2, 1),
    _AcPerfBctRequests_Type()
)
acPerfBctRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPerfBctRequests.setStatus("deprecated")
_AcPerfBctSuccessful_Type = Counter32
_AcPerfBctSuccessful_Object = MibScalar
acPerfBctSuccessful = _AcPerfBctSuccessful_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 2, 2, 2),
    _AcPerfBctSuccessful_Type()
)
acPerfBctSuccessful.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPerfBctSuccessful.setStatus("deprecated")
_AcPerfBctFailedDueToLackOfResources_Type = Counter32
_AcPerfBctFailedDueToLackOfResources_Object = MibScalar
acPerfBctFailedDueToLackOfResources = _AcPerfBctFailedDueToLackOfResources_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 2, 2, 3),
    _AcPerfBctFailedDueToLackOfResources_Type()
)
acPerfBctFailedDueToLackOfResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPerfBctFailedDueToLackOfResources.setStatus("deprecated")
_AcPerfBctInProgress_Type = Gauge32
_AcPerfBctInProgress_Object = MibScalar
acPerfBctInProgress = _AcPerfBctInProgress_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 2, 2, 4),
    _AcPerfBctInProgress_Type()
)
acPerfBctInProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPerfBctInProgress.setStatus("deprecated")
_AcPerfBctDuration_Type = Counter32
_AcPerfBctDuration_Object = MibScalar
acPerfBctDuration = _AcPerfBctDuration_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 2, 2, 5),
    _AcPerfBctDuration_Type()
)
acPerfBctDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPerfBctDuration.setStatus("deprecated")
_AcPerfBctTotalParticipants_Type = Counter32
_AcPerfBctTotalParticipants_Object = MibScalar
acPerfBctTotalParticipants = _AcPerfBctTotalParticipants_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 2, 2, 6),
    _AcPerfBctTotalParticipants_Type()
)
acPerfBctTotalParticipants.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPerfBctTotalParticipants.setStatus("deprecated")
_AcPerfBctCurrentNumberOfParticipants_Type = Gauge32
_AcPerfBctCurrentNumberOfParticipants_Object = MibScalar
acPerfBctCurrentNumberOfParticipants = _AcPerfBctCurrentNumberOfParticipants_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 2, 2, 7),
    _AcPerfBctCurrentNumberOfParticipants_Type()
)
acPerfBctCurrentNumberOfParticipants.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPerfBctCurrentNumberOfParticipants.setStatus("deprecated")
_AcPerfConf_ObjectIdentity = ObjectIdentity
acPerfConf = _AcPerfConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 10, 2, 3)
)
_AcPerfConfRequests_Type = Counter32
_AcPerfConfRequests_Object = MibScalar
acPerfConfRequests = _AcPerfConfRequests_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 2, 3, 1),
    _AcPerfConfRequests_Type()
)
acPerfConfRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPerfConfRequests.setStatus("deprecated")
_AcPerfConfSuccessful_Type = Counter32
_AcPerfConfSuccessful_Object = MibScalar
acPerfConfSuccessful = _AcPerfConfSuccessful_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 2, 3, 2),
    _AcPerfConfSuccessful_Type()
)
acPerfConfSuccessful.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPerfConfSuccessful.setStatus("deprecated")
_AcPerfConfInProgress_Type = Gauge32
_AcPerfConfInProgress_Object = MibScalar
acPerfConfInProgress = _AcPerfConfInProgress_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 2, 3, 3),
    _AcPerfConfInProgress_Type()
)
acPerfConfInProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPerfConfInProgress.setStatus("deprecated")
_AcPerfConfDuration_Type = Counter32
_AcPerfConfDuration_Object = MibScalar
acPerfConfDuration = _AcPerfConfDuration_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 2, 3, 4),
    _AcPerfConfDuration_Type()
)
acPerfConfDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPerfConfDuration.setStatus("deprecated")
_AcPerfConfFailedDueToLackOfResources_Type = Counter32
_AcPerfConfFailedDueToLackOfResources_Object = MibScalar
acPerfConfFailedDueToLackOfResources = _AcPerfConfFailedDueToLackOfResources_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 2, 3, 5),
    _AcPerfConfFailedDueToLackOfResources_Type()
)
acPerfConfFailedDueToLackOfResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPerfConfFailedDueToLackOfResources.setStatus("deprecated")
_AcPerfConfAddRequests_Type = Counter32
_AcPerfConfAddRequests_Object = MibScalar
acPerfConfAddRequests = _AcPerfConfAddRequests_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 2, 3, 6),
    _AcPerfConfAddRequests_Type()
)
acPerfConfAddRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPerfConfAddRequests.setStatus("deprecated")
_AcPerfConfAddSuccessful_Type = Counter32
_AcPerfConfAddSuccessful_Object = MibScalar
acPerfConfAddSuccessful = _AcPerfConfAddSuccessful_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 2, 3, 7),
    _AcPerfConfAddSuccessful_Type()
)
acPerfConfAddSuccessful.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPerfConfAddSuccessful.setStatus("deprecated")
_AcPerfConfAddFailedDueToLackOfResources_Type = Counter32
_AcPerfConfAddFailedDueToLackOfResources_Object = MibScalar
acPerfConfAddFailedDueToLackOfResources = _AcPerfConfAddFailedDueToLackOfResources_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 2, 3, 8),
    _AcPerfConfAddFailedDueToLackOfResources_Type()
)
acPerfConfAddFailedDueToLackOfResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPerfConfAddFailedDueToLackOfResources.setStatus("deprecated")
_AcPerfConfPortsUsed_Type = Counter32
_AcPerfConfPortsUsed_Object = MibScalar
acPerfConfPortsUsed = _AcPerfConfPortsUsed_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 2, 3, 9),
    _AcPerfConfPortsUsed_Type()
)
acPerfConfPortsUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPerfConfPortsUsed.setStatus("deprecated")
_AcPerfConfPortsReserved_Type = Gauge32
_AcPerfConfPortsReserved_Object = MibScalar
acPerfConfPortsReserved = _AcPerfConfPortsReserved_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 2, 3, 10),
    _AcPerfConfPortsReserved_Type()
)
acPerfConfPortsReserved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPerfConfPortsReserved.setStatus("deprecated")
_AcPerfTt_ObjectIdentity = ObjectIdentity
acPerfTt = _AcPerfTt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 10, 2, 4)
)
_AcPerfTtRequests_Type = Counter32
_AcPerfTtRequests_Object = MibScalar
acPerfTtRequests = _AcPerfTtRequests_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 2, 4, 1),
    _AcPerfTtRequests_Type()
)
acPerfTtRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPerfTtRequests.setStatus("deprecated")
_AcPerfTtSuccessful_Type = Counter32
_AcPerfTtSuccessful_Object = MibScalar
acPerfTtSuccessful = _AcPerfTtSuccessful_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 2, 4, 2),
    _AcPerfTtSuccessful_Type()
)
acPerfTtSuccessful.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPerfTtSuccessful.setStatus("deprecated")
_AcPerfTtInProgress_Type = Gauge32
_AcPerfTtInProgress_Object = MibScalar
acPerfTtInProgress = _AcPerfTtInProgress_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 2, 4, 3),
    _AcPerfTtInProgress_Type()
)
acPerfTtInProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPerfTtInProgress.setStatus("deprecated")
_AcPerfTtDuration_Type = Counter32
_AcPerfTtDuration_Object = MibScalar
acPerfTtDuration = _AcPerfTtDuration_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 2, 4, 4),
    _AcPerfTtDuration_Type()
)
acPerfTtDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPerfTtDuration.setStatus("deprecated")
_AcPerfTtFailedDueToLackOfResources_Type = Counter32
_AcPerfTtFailedDueToLackOfResources_Object = MibScalar
acPerfTtFailedDueToLackOfResources = _AcPerfTtFailedDueToLackOfResources_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 2, 4, 5),
    _AcPerfTtFailedDueToLackOfResources_Type()
)
acPerfTtFailedDueToLackOfResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPerfTtFailedDueToLackOfResources.setStatus("deprecated")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AcPerfMediaServices",
    **{"audioCodes": audioCodes,
       "acRegistrations": acRegistrations,
       "acGeneric": acGeneric,
       "acProducts": acProducts,
       "acPerformance": acPerformance,
       "acPerfMediaServices": acPerfMediaServices,
       "acPerfIvr": acPerfIvr,
       "acPerfIvrPlayRequests": acPerfIvrPlayRequests,
       "acPerfIvrPlaySuccessful": acPerfIvrPlaySuccessful,
       "acPerfIvrPlayFailedDueToLackOfResources": acPerfIvrPlayFailedDueToLackOfResources,
       "acPerfIvrPlayInProgress": acPerfIvrPlayInProgress,
       "acPerfIvrPlayDuration": acPerfIvrPlayDuration,
       "acPerfIvrPlayFailedDueToProvMismatch": acPerfIvrPlayFailedDueToProvMismatch,
       "acPerfIvrPlayCollectRequests": acPerfIvrPlayCollectRequests,
       "acPerfIvrPlayCollectSuccessful": acPerfIvrPlayCollectSuccessful,
       "acPerfIvrPlayCollectFailedDueToLackOfResources": acPerfIvrPlayCollectFailedDueToLackOfResources,
       "acPerfIvrPlayCollectFailedDueToProvMismatch": acPerfIvrPlayCollectFailedDueToProvMismatch,
       "acPerfIvrPlayCollectInProgress": acPerfIvrPlayCollectInProgress,
       "acPerfIvrPlayCollectDuration": acPerfIvrPlayCollectDuration,
       "acPerfIvrContDigitCollectRequests": acPerfIvrContDigitCollectRequests,
       "acPerfIvrContDigitCollectSuccessful": acPerfIvrContDigitCollectSuccessful,
       "acPerfIvrContDigitCollectFailedDueToLackOfResources": acPerfIvrContDigitCollectFailedDueToLackOfResources,
       "acPerfIvrContDigitCollectInProgress": acPerfIvrContDigitCollectInProgress,
       "acPerfIvrContDigitCollectDuration": acPerfIvrContDigitCollectDuration,
       "acPerfBct": acPerfBct,
       "acPerfBctRequests": acPerfBctRequests,
       "acPerfBctSuccessful": acPerfBctSuccessful,
       "acPerfBctFailedDueToLackOfResources": acPerfBctFailedDueToLackOfResources,
       "acPerfBctInProgress": acPerfBctInProgress,
       "acPerfBctDuration": acPerfBctDuration,
       "acPerfBctTotalParticipants": acPerfBctTotalParticipants,
       "acPerfBctCurrentNumberOfParticipants": acPerfBctCurrentNumberOfParticipants,
       "acPerfConf": acPerfConf,
       "acPerfConfRequests": acPerfConfRequests,
       "acPerfConfSuccessful": acPerfConfSuccessful,
       "acPerfConfInProgress": acPerfConfInProgress,
       "acPerfConfDuration": acPerfConfDuration,
       "acPerfConfFailedDueToLackOfResources": acPerfConfFailedDueToLackOfResources,
       "acPerfConfAddRequests": acPerfConfAddRequests,
       "acPerfConfAddSuccessful": acPerfConfAddSuccessful,
       "acPerfConfAddFailedDueToLackOfResources": acPerfConfAddFailedDueToLackOfResources,
       "acPerfConfPortsUsed": acPerfConfPortsUsed,
       "acPerfConfPortsReserved": acPerfConfPortsReserved,
       "acPerfTt": acPerfTt,
       "acPerfTtRequests": acPerfTtRequests,
       "acPerfTtSuccessful": acPerfTtSuccessful,
       "acPerfTtInProgress": acPerfTtInProgress,
       "acPerfTtDuration": acPerfTtDuration,
       "acPerfTtFailedDueToLackOfResources": acPerfTtFailedDueToLackOfResources}
)
