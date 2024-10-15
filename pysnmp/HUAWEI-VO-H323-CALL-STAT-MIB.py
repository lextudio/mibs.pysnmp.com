# SNMP MIB module (HUAWEI-VO-H323-CALL-STAT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-VO-H323-CALL-STAT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:06:32 2024
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

(voice,) = mibBuilder.importSymbols(
    "HUAWEI-3COM-OID-MIB",
    "voice")

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


# MODULE-IDENTITY

hwVoiceH323CallStatMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11)
)
hwVoiceH323CallStatMIB.setRevisions(
        ("2004-04-08 13:45",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwVoH323CallStatObjects_ObjectIdentity = ObjectIdentity
hwVoH323CallStatObjects = _HwVoH323CallStatObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1)
)
_HwVoIPPH225StatObjects_ObjectIdentity = ObjectIdentity
hwVoIPPH225StatObjects = _HwVoIPPH225StatObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 1)
)
_HwVoSend_Setup_Type = Counter32
_HwVoSend_Setup_Object = MibScalar
hwVoSend_Setup = _HwVoSend_Setup_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 1, 1),
    _HwVoSend_Setup_Type()
)
hwVoSend_Setup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoSend_Setup.setStatus("current")
_HwVoSend_CallProceeding_Type = Counter32
_HwVoSend_CallProceeding_Object = MibScalar
hwVoSend_CallProceeding = _HwVoSend_CallProceeding_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 1, 2),
    _HwVoSend_CallProceeding_Type()
)
hwVoSend_CallProceeding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoSend_CallProceeding.setStatus("current")
_HwVoSend_Alerting_Type = Counter32
_HwVoSend_Alerting_Object = MibScalar
hwVoSend_Alerting = _HwVoSend_Alerting_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 1, 3),
    _HwVoSend_Alerting_Type()
)
hwVoSend_Alerting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoSend_Alerting.setStatus("current")
_HwVoSend_Connect_Type = Counter32
_HwVoSend_Connect_Object = MibScalar
hwVoSend_Connect = _HwVoSend_Connect_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 1, 4),
    _HwVoSend_Connect_Type()
)
hwVoSend_Connect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoSend_Connect.setStatus("current")
_HwVoSend_ReleaseComplete_Type = Counter32
_HwVoSend_ReleaseComplete_Object = MibScalar
hwVoSend_ReleaseComplete = _HwVoSend_ReleaseComplete_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 1, 5),
    _HwVoSend_ReleaseComplete_Type()
)
hwVoSend_ReleaseComplete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoSend_ReleaseComplete.setStatus("current")
_HwVoSend_FacilityIndUserInput_Type = Counter32
_HwVoSend_FacilityIndUserInput_Object = MibScalar
hwVoSend_FacilityIndUserInput = _HwVoSend_FacilityIndUserInput_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 1, 6),
    _HwVoSend_FacilityIndUserInput_Type()
)
hwVoSend_FacilityIndUserInput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoSend_FacilityIndUserInput.setStatus("current")
_HwVoSend_FacilityTCSRequest_Type = Counter32
_HwVoSend_FacilityTCSRequest_Object = MibScalar
hwVoSend_FacilityTCSRequest = _HwVoSend_FacilityTCSRequest_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 1, 7),
    _HwVoSend_FacilityTCSRequest_Type()
)
hwVoSend_FacilityTCSRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoSend_FacilityTCSRequest.setStatus("current")
_HwVoSend_FacilityTCSAck_Type = Counter32
_HwVoSend_FacilityTCSAck_Object = MibScalar
hwVoSend_FacilityTCSAck = _HwVoSend_FacilityTCSAck_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 1, 8),
    _HwVoSend_FacilityTCSAck_Type()
)
hwVoSend_FacilityTCSAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoSend_FacilityTCSAck.setStatus("current")
_HwVoSend_FacilityTCSReject_Type = Counter32
_HwVoSend_FacilityTCSReject_Object = MibScalar
hwVoSend_FacilityTCSReject = _HwVoSend_FacilityTCSReject_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 1, 9),
    _HwVoSend_FacilityTCSReject_Type()
)
hwVoSend_FacilityTCSReject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoSend_FacilityTCSReject.setStatus("current")
_HwVoSend_FacilityOLCRequest_Type = Counter32
_HwVoSend_FacilityOLCRequest_Object = MibScalar
hwVoSend_FacilityOLCRequest = _HwVoSend_FacilityOLCRequest_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 1, 10),
    _HwVoSend_FacilityOLCRequest_Type()
)
hwVoSend_FacilityOLCRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoSend_FacilityOLCRequest.setStatus("current")
_HwVoSend_FacilityOLCAck_Type = Counter32
_HwVoSend_FacilityOLCAck_Object = MibScalar
hwVoSend_FacilityOLCAck = _HwVoSend_FacilityOLCAck_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 1, 11),
    _HwVoSend_FacilityOLCAck_Type()
)
hwVoSend_FacilityOLCAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoSend_FacilityOLCAck.setStatus("current")
_HwVoSend_FacilityOLCReject_Type = Counter32
_HwVoSend_FacilityOLCReject_Object = MibScalar
hwVoSend_FacilityOLCReject = _HwVoSend_FacilityOLCReject_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 1, 12),
    _HwVoSend_FacilityOLCReject_Type()
)
hwVoSend_FacilityOLCReject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoSend_FacilityOLCReject.setStatus("current")
_HwVoSend_FacilityMSDRequest_Type = Counter32
_HwVoSend_FacilityMSDRequest_Object = MibScalar
hwVoSend_FacilityMSDRequest = _HwVoSend_FacilityMSDRequest_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 1, 13),
    _HwVoSend_FacilityMSDRequest_Type()
)
hwVoSend_FacilityMSDRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoSend_FacilityMSDRequest.setStatus("current")
_HwVoSend_FacilityMSDAck_Type = Counter32
_HwVoSend_FacilityMSDAck_Object = MibScalar
hwVoSend_FacilityMSDAck = _HwVoSend_FacilityMSDAck_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 1, 14),
    _HwVoSend_FacilityMSDAck_Type()
)
hwVoSend_FacilityMSDAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoSend_FacilityMSDAck.setStatus("current")
_HwVoSend_FacilityMSDReject_Type = Counter32
_HwVoSend_FacilityMSDReject_Object = MibScalar
hwVoSend_FacilityMSDReject = _HwVoSend_FacilityMSDReject_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 1, 15),
    _HwVoSend_FacilityMSDReject_Type()
)
hwVoSend_FacilityMSDReject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoSend_FacilityMSDReject.setStatus("current")
_HwVoSend_FacilityCLCRequest_Type = Counter32
_HwVoSend_FacilityCLCRequest_Object = MibScalar
hwVoSend_FacilityCLCRequest = _HwVoSend_FacilityCLCRequest_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 1, 16),
    _HwVoSend_FacilityCLCRequest_Type()
)
hwVoSend_FacilityCLCRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoSend_FacilityCLCRequest.setStatus("current")
_HwVoSend_FacilityCLCAck_Type = Counter32
_HwVoSend_FacilityCLCAck_Object = MibScalar
hwVoSend_FacilityCLCAck = _HwVoSend_FacilityCLCAck_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 1, 17),
    _HwVoSend_FacilityCLCAck_Type()
)
hwVoSend_FacilityCLCAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoSend_FacilityCLCAck.setStatus("current")
_HwVoSend_FacilityStartH245_Type = Counter32
_HwVoSend_FacilityStartH245_Object = MibScalar
hwVoSend_FacilityStartH245 = _HwVoSend_FacilityStartH245_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 1, 18),
    _HwVoSend_FacilityStartH245_Type()
)
hwVoSend_FacilityStartH245.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoSend_FacilityStartH245.setStatus("current")
_HwVoSend_ErrorH225Msg_Type = Counter32
_HwVoSend_ErrorH225Msg_Object = MibScalar
hwVoSend_ErrorH225Msg = _HwVoSend_ErrorH225Msg_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 1, 19),
    _HwVoSend_ErrorH225Msg_Type()
)
hwVoSend_ErrorH225Msg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoSend_ErrorH225Msg.setStatus("current")
_HwVoRecv_Setup_Type = Counter32
_HwVoRecv_Setup_Object = MibScalar
hwVoRecv_Setup = _HwVoRecv_Setup_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 1, 20),
    _HwVoRecv_Setup_Type()
)
hwVoRecv_Setup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoRecv_Setup.setStatus("current")
_HwVoRecv_CallProceeding_Type = Counter32
_HwVoRecv_CallProceeding_Object = MibScalar
hwVoRecv_CallProceeding = _HwVoRecv_CallProceeding_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 1, 21),
    _HwVoRecv_CallProceeding_Type()
)
hwVoRecv_CallProceeding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoRecv_CallProceeding.setStatus("current")
_HwVoRecv_Alerting_Type = Counter32
_HwVoRecv_Alerting_Object = MibScalar
hwVoRecv_Alerting = _HwVoRecv_Alerting_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 1, 22),
    _HwVoRecv_Alerting_Type()
)
hwVoRecv_Alerting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoRecv_Alerting.setStatus("current")
_HwVoRecv_Connect_Type = Counter32
_HwVoRecv_Connect_Object = MibScalar
hwVoRecv_Connect = _HwVoRecv_Connect_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 1, 23),
    _HwVoRecv_Connect_Type()
)
hwVoRecv_Connect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoRecv_Connect.setStatus("current")
_HwVoRecv_ReleaseComplete_Type = Counter32
_HwVoRecv_ReleaseComplete_Object = MibScalar
hwVoRecv_ReleaseComplete = _HwVoRecv_ReleaseComplete_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 1, 24),
    _HwVoRecv_ReleaseComplete_Type()
)
hwVoRecv_ReleaseComplete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoRecv_ReleaseComplete.setStatus("current")
_HwVoRecv_Progress_Type = Counter32
_HwVoRecv_Progress_Object = MibScalar
hwVoRecv_Progress = _HwVoRecv_Progress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 1, 25),
    _HwVoRecv_Progress_Type()
)
hwVoRecv_Progress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoRecv_Progress.setStatus("current")
_HwVoRecv_FacilityTCSRequest_Type = Counter32
_HwVoRecv_FacilityTCSRequest_Object = MibScalar
hwVoRecv_FacilityTCSRequest = _HwVoRecv_FacilityTCSRequest_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 1, 26),
    _HwVoRecv_FacilityTCSRequest_Type()
)
hwVoRecv_FacilityTCSRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoRecv_FacilityTCSRequest.setStatus("current")
_HwVoRecv_FacilityTCSAck_Type = Counter32
_HwVoRecv_FacilityTCSAck_Object = MibScalar
hwVoRecv_FacilityTCSAck = _HwVoRecv_FacilityTCSAck_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 1, 27),
    _HwVoRecv_FacilityTCSAck_Type()
)
hwVoRecv_FacilityTCSAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoRecv_FacilityTCSAck.setStatus("current")
_HwVoRecv_FacilityTCSReject_Type = Counter32
_HwVoRecv_FacilityTCSReject_Object = MibScalar
hwVoRecv_FacilityTCSReject = _HwVoRecv_FacilityTCSReject_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 1, 28),
    _HwVoRecv_FacilityTCSReject_Type()
)
hwVoRecv_FacilityTCSReject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoRecv_FacilityTCSReject.setStatus("current")
_HwVoRecv_FacilityOLCRequest_Type = Counter32
_HwVoRecv_FacilityOLCRequest_Object = MibScalar
hwVoRecv_FacilityOLCRequest = _HwVoRecv_FacilityOLCRequest_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 1, 29),
    _HwVoRecv_FacilityOLCRequest_Type()
)
hwVoRecv_FacilityOLCRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoRecv_FacilityOLCRequest.setStatus("current")
_HwVoRecv_FacilityOLCAck_Type = Counter32
_HwVoRecv_FacilityOLCAck_Object = MibScalar
hwVoRecv_FacilityOLCAck = _HwVoRecv_FacilityOLCAck_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 1, 30),
    _HwVoRecv_FacilityOLCAck_Type()
)
hwVoRecv_FacilityOLCAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoRecv_FacilityOLCAck.setStatus("current")
_HwVoRecv_FacilityOLCReject_Type = Counter32
_HwVoRecv_FacilityOLCReject_Object = MibScalar
hwVoRecv_FacilityOLCReject = _HwVoRecv_FacilityOLCReject_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 1, 31),
    _HwVoRecv_FacilityOLCReject_Type()
)
hwVoRecv_FacilityOLCReject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoRecv_FacilityOLCReject.setStatus("current")
_HwVoRecv_FacilityMSDRequest_Type = Counter32
_HwVoRecv_FacilityMSDRequest_Object = MibScalar
hwVoRecv_FacilityMSDRequest = _HwVoRecv_FacilityMSDRequest_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 1, 32),
    _HwVoRecv_FacilityMSDRequest_Type()
)
hwVoRecv_FacilityMSDRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoRecv_FacilityMSDRequest.setStatus("current")
_HwVoRecv_FacilityMSDAck_Type = Counter32
_HwVoRecv_FacilityMSDAck_Object = MibScalar
hwVoRecv_FacilityMSDAck = _HwVoRecv_FacilityMSDAck_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 1, 33),
    _HwVoRecv_FacilityMSDAck_Type()
)
hwVoRecv_FacilityMSDAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoRecv_FacilityMSDAck.setStatus("current")
_HwVoRecv_FacilityMSDReject_Type = Counter32
_HwVoRecv_FacilityMSDReject_Object = MibScalar
hwVoRecv_FacilityMSDReject = _HwVoRecv_FacilityMSDReject_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 1, 34),
    _HwVoRecv_FacilityMSDReject_Type()
)
hwVoRecv_FacilityMSDReject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoRecv_FacilityMSDReject.setStatus("current")
_HwVoRecv_FacilityCLCRequest_Type = Counter32
_HwVoRecv_FacilityCLCRequest_Object = MibScalar
hwVoRecv_FacilityCLCRequest = _HwVoRecv_FacilityCLCRequest_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 1, 35),
    _HwVoRecv_FacilityCLCRequest_Type()
)
hwVoRecv_FacilityCLCRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoRecv_FacilityCLCRequest.setStatus("current")
_HwVoRecv_FacilityCLCAck_Type = Counter32
_HwVoRecv_FacilityCLCAck_Object = MibScalar
hwVoRecv_FacilityCLCAck = _HwVoRecv_FacilityCLCAck_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 1, 36),
    _HwVoRecv_FacilityCLCAck_Type()
)
hwVoRecv_FacilityCLCAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoRecv_FacilityCLCAck.setStatus("current")
_HwVoRecv_UnknownH225Msg_Type = Counter32
_HwVoRecv_UnknownH225Msg_Object = MibScalar
hwVoRecv_UnknownH225Msg = _HwVoRecv_UnknownH225Msg_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 1, 37),
    _HwVoRecv_UnknownH225Msg_Type()
)
hwVoRecv_UnknownH225Msg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoRecv_UnknownH225Msg.setStatus("current")
_HwVoIPPH245StatObjects_ObjectIdentity = ObjectIdentity
hwVoIPPH245StatObjects = _HwVoIPPH245StatObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 2)
)
_HwVoSend_TCSRequest_Type = Counter32
_HwVoSend_TCSRequest_Object = MibScalar
hwVoSend_TCSRequest = _HwVoSend_TCSRequest_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 2, 1),
    _HwVoSend_TCSRequest_Type()
)
hwVoSend_TCSRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoSend_TCSRequest.setStatus("current")
_HwVoSend_TCSAck_Type = Counter32
_HwVoSend_TCSAck_Object = MibScalar
hwVoSend_TCSAck = _HwVoSend_TCSAck_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 2, 2),
    _HwVoSend_TCSAck_Type()
)
hwVoSend_TCSAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoSend_TCSAck.setStatus("current")
_HwVoSend_TCSReject_Type = Counter32
_HwVoSend_TCSReject_Object = MibScalar
hwVoSend_TCSReject = _HwVoSend_TCSReject_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 2, 3),
    _HwVoSend_TCSReject_Type()
)
hwVoSend_TCSReject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoSend_TCSReject.setStatus("current")
_HwVoSend_MSDRequest_Type = Counter32
_HwVoSend_MSDRequest_Object = MibScalar
hwVoSend_MSDRequest = _HwVoSend_MSDRequest_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 2, 4),
    _HwVoSend_MSDRequest_Type()
)
hwVoSend_MSDRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoSend_MSDRequest.setStatus("current")
_HwVoSend_MSDAck_Type = Counter32
_HwVoSend_MSDAck_Object = MibScalar
hwVoSend_MSDAck = _HwVoSend_MSDAck_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 2, 5),
    _HwVoSend_MSDAck_Type()
)
hwVoSend_MSDAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoSend_MSDAck.setStatus("current")
_HwVoSend_MSDReject_Type = Counter32
_HwVoSend_MSDReject_Object = MibScalar
hwVoSend_MSDReject = _HwVoSend_MSDReject_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 2, 6),
    _HwVoSend_MSDReject_Type()
)
hwVoSend_MSDReject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoSend_MSDReject.setStatus("current")
_HwVoSend_OLCRequest_Type = Counter32
_HwVoSend_OLCRequest_Object = MibScalar
hwVoSend_OLCRequest = _HwVoSend_OLCRequest_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 2, 7),
    _HwVoSend_OLCRequest_Type()
)
hwVoSend_OLCRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoSend_OLCRequest.setStatus("current")
_HwVoSend_OLCAck_Type = Counter32
_HwVoSend_OLCAck_Object = MibScalar
hwVoSend_OLCAck = _HwVoSend_OLCAck_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 2, 8),
    _HwVoSend_OLCAck_Type()
)
hwVoSend_OLCAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoSend_OLCAck.setStatus("current")
_HwVoSend_OLCReject_Type = Counter32
_HwVoSend_OLCReject_Object = MibScalar
hwVoSend_OLCReject = _HwVoSend_OLCReject_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 2, 9),
    _HwVoSend_OLCReject_Type()
)
hwVoSend_OLCReject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoSend_OLCReject.setStatus("current")
_HwVoSend_CLCRequest_Type = Counter32
_HwVoSend_CLCRequest_Object = MibScalar
hwVoSend_CLCRequest = _HwVoSend_CLCRequest_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 2, 10),
    _HwVoSend_CLCRequest_Type()
)
hwVoSend_CLCRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoSend_CLCRequest.setStatus("current")
_HwVoSend_CLCAck_Type = Counter32
_HwVoSend_CLCAck_Object = MibScalar
hwVoSend_CLCAck = _HwVoSend_CLCAck_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 2, 11),
    _HwVoSend_CLCAck_Type()
)
hwVoSend_CLCAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoSend_CLCAck.setStatus("current")
_HwVoSend_UserInput_Type = Counter32
_HwVoSend_UserInput_Object = MibScalar
hwVoSend_UserInput = _HwVoSend_UserInput_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 2, 12),
    _HwVoSend_UserInput_Type()
)
hwVoSend_UserInput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoSend_UserInput.setStatus("current")
_HwVoSend_ErrorH245Msg_Type = Counter32
_HwVoSend_ErrorH245Msg_Object = MibScalar
hwVoSend_ErrorH245Msg = _HwVoSend_ErrorH245Msg_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 2, 13),
    _HwVoSend_ErrorH245Msg_Type()
)
hwVoSend_ErrorH245Msg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoSend_ErrorH245Msg.setStatus("current")
_HwVoRecv_TCSRequest_Type = Counter32
_HwVoRecv_TCSRequest_Object = MibScalar
hwVoRecv_TCSRequest = _HwVoRecv_TCSRequest_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 2, 14),
    _HwVoRecv_TCSRequest_Type()
)
hwVoRecv_TCSRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoRecv_TCSRequest.setStatus("current")
_HwVoRecv_TCSAck_Type = Counter32
_HwVoRecv_TCSAck_Object = MibScalar
hwVoRecv_TCSAck = _HwVoRecv_TCSAck_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 2, 15),
    _HwVoRecv_TCSAck_Type()
)
hwVoRecv_TCSAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoRecv_TCSAck.setStatus("current")
_HwVoRecv_TCSReject_Type = Counter32
_HwVoRecv_TCSReject_Object = MibScalar
hwVoRecv_TCSReject = _HwVoRecv_TCSReject_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 2, 16),
    _HwVoRecv_TCSReject_Type()
)
hwVoRecv_TCSReject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoRecv_TCSReject.setStatus("current")
_HwVoRecv_MSDRequest_Type = Counter32
_HwVoRecv_MSDRequest_Object = MibScalar
hwVoRecv_MSDRequest = _HwVoRecv_MSDRequest_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 2, 17),
    _HwVoRecv_MSDRequest_Type()
)
hwVoRecv_MSDRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoRecv_MSDRequest.setStatus("current")
_HwVoRecv_MSDAck_Type = Counter32
_HwVoRecv_MSDAck_Object = MibScalar
hwVoRecv_MSDAck = _HwVoRecv_MSDAck_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 2, 18),
    _HwVoRecv_MSDAck_Type()
)
hwVoRecv_MSDAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoRecv_MSDAck.setStatus("current")
_HwVoRecv_MSDReject_Type = Counter32
_HwVoRecv_MSDReject_Object = MibScalar
hwVoRecv_MSDReject = _HwVoRecv_MSDReject_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 2, 19),
    _HwVoRecv_MSDReject_Type()
)
hwVoRecv_MSDReject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoRecv_MSDReject.setStatus("current")
_HwVoRecv_OLCRequest_Type = Counter32
_HwVoRecv_OLCRequest_Object = MibScalar
hwVoRecv_OLCRequest = _HwVoRecv_OLCRequest_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 2, 20),
    _HwVoRecv_OLCRequest_Type()
)
hwVoRecv_OLCRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoRecv_OLCRequest.setStatus("current")
_HwVoRecv_OLCAck_Type = Counter32
_HwVoRecv_OLCAck_Object = MibScalar
hwVoRecv_OLCAck = _HwVoRecv_OLCAck_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 2, 21),
    _HwVoRecv_OLCAck_Type()
)
hwVoRecv_OLCAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoRecv_OLCAck.setStatus("current")
_HwVoRecv_OLCReject_Type = Counter32
_HwVoRecv_OLCReject_Object = MibScalar
hwVoRecv_OLCReject = _HwVoRecv_OLCReject_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 2, 22),
    _HwVoRecv_OLCReject_Type()
)
hwVoRecv_OLCReject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoRecv_OLCReject.setStatus("current")
_HwVoRecv_CLCRequest_Type = Counter32
_HwVoRecv_CLCRequest_Object = MibScalar
hwVoRecv_CLCRequest = _HwVoRecv_CLCRequest_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 2, 23),
    _HwVoRecv_CLCRequest_Type()
)
hwVoRecv_CLCRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoRecv_CLCRequest.setStatus("current")
_HwVoRecv_CLCAck_Type = Counter32
_HwVoRecv_CLCAck_Object = MibScalar
hwVoRecv_CLCAck = _HwVoRecv_CLCAck_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 2, 24),
    _HwVoRecv_CLCAck_Type()
)
hwVoRecv_CLCAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoRecv_CLCAck.setStatus("current")
_HwVoRecv_UserInput_Type = Counter32
_HwVoRecv_UserInput_Object = MibScalar
hwVoRecv_UserInput = _HwVoRecv_UserInput_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 2, 25),
    _HwVoRecv_UserInput_Type()
)
hwVoRecv_UserInput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoRecv_UserInput.setStatus("current")
_HwVoRecv_UnknownH245Msg_Type = Counter32
_HwVoRecv_UnknownH245Msg_Object = MibScalar
hwVoRecv_UnknownH245Msg = _HwVoRecv_UnknownH245Msg_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 2, 26),
    _HwVoRecv_UnknownH245Msg_Type()
)
hwVoRecv_UnknownH245Msg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoRecv_UnknownH245Msg.setStatus("current")
_HwVoIPPRASStatObjects_ObjectIdentity = ObjectIdentity
hwVoIPPRASStatObjects = _HwVoIPPRASStatObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 3)
)
_HwVoSend_GRQ_Type = Counter32
_HwVoSend_GRQ_Object = MibScalar
hwVoSend_GRQ = _HwVoSend_GRQ_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 3, 1),
    _HwVoSend_GRQ_Type()
)
hwVoSend_GRQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoSend_GRQ.setStatus("current")
_HwVoSend_RRQ_Type = Counter32
_HwVoSend_RRQ_Object = MibScalar
hwVoSend_RRQ = _HwVoSend_RRQ_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 3, 2),
    _HwVoSend_RRQ_Type()
)
hwVoSend_RRQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoSend_RRQ.setStatus("current")
_HwVoSend_ARQ_Type = Counter32
_HwVoSend_ARQ_Object = MibScalar
hwVoSend_ARQ = _HwVoSend_ARQ_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 3, 3),
    _HwVoSend_ARQ_Type()
)
hwVoSend_ARQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoSend_ARQ.setStatus("current")
_HwVoSend_BRQ_Type = Counter32
_HwVoSend_BRQ_Object = MibScalar
hwVoSend_BRQ = _HwVoSend_BRQ_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 3, 4),
    _HwVoSend_BRQ_Type()
)
hwVoSend_BRQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoSend_BRQ.setStatus("current")
_HwVoSend_DRQ_Type = Counter32
_HwVoSend_DRQ_Object = MibScalar
hwVoSend_DRQ = _HwVoSend_DRQ_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 3, 5),
    _HwVoSend_DRQ_Type()
)
hwVoSend_DRQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoSend_DRQ.setStatus("current")
_HwVoSend_URQ_Type = Counter32
_HwVoSend_URQ_Object = MibScalar
hwVoSend_URQ = _HwVoSend_URQ_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 3, 6),
    _HwVoSend_URQ_Type()
)
hwVoSend_URQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoSend_URQ.setStatus("current")
_HwVoSend_UCF_Type = Counter32
_HwVoSend_UCF_Object = MibScalar
hwVoSend_UCF = _HwVoSend_UCF_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 3, 7),
    _HwVoSend_UCF_Type()
)
hwVoSend_UCF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoSend_UCF.setStatus("current")
_HwVoSend_IRR_Type = Counter32
_HwVoSend_IRR_Object = MibScalar
hwVoSend_IRR = _HwVoSend_IRR_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 3, 8),
    _HwVoSend_IRR_Type()
)
hwVoSend_IRR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoSend_IRR.setStatus("current")
_HwVoSend_ErrorRASMsg_Type = Counter32
_HwVoSend_ErrorRASMsg_Object = MibScalar
hwVoSend_ErrorRASMsg = _HwVoSend_ErrorRASMsg_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 3, 9),
    _HwVoSend_ErrorRASMsg_Type()
)
hwVoSend_ErrorRASMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoSend_ErrorRASMsg.setStatus("current")
_HwVoRecv_GCF_Type = Counter32
_HwVoRecv_GCF_Object = MibScalar
hwVoRecv_GCF = _HwVoRecv_GCF_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 3, 10),
    _HwVoRecv_GCF_Type()
)
hwVoRecv_GCF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoRecv_GCF.setStatus("current")
_HwVoRecv_RCF_Type = Counter32
_HwVoRecv_RCF_Object = MibScalar
hwVoRecv_RCF = _HwVoRecv_RCF_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 3, 11),
    _HwVoRecv_RCF_Type()
)
hwVoRecv_RCF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoRecv_RCF.setStatus("current")
_HwVoRecv_ACF_Type = Counter32
_HwVoRecv_ACF_Object = MibScalar
hwVoRecv_ACF = _HwVoRecv_ACF_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 3, 12),
    _HwVoRecv_ACF_Type()
)
hwVoRecv_ACF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoRecv_ACF.setStatus("current")
_HwVoRecv_BCF_Type = Counter32
_HwVoRecv_BCF_Object = MibScalar
hwVoRecv_BCF = _HwVoRecv_BCF_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 3, 13),
    _HwVoRecv_BCF_Type()
)
hwVoRecv_BCF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoRecv_BCF.setStatus("current")
_HwVoRecv_DCF_Type = Counter32
_HwVoRecv_DCF_Object = MibScalar
hwVoRecv_DCF = _HwVoRecv_DCF_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 3, 14),
    _HwVoRecv_DCF_Type()
)
hwVoRecv_DCF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoRecv_DCF.setStatus("current")
_HwVoRecv_GRJ_Type = Counter32
_HwVoRecv_GRJ_Object = MibScalar
hwVoRecv_GRJ = _HwVoRecv_GRJ_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 3, 15),
    _HwVoRecv_GRJ_Type()
)
hwVoRecv_GRJ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoRecv_GRJ.setStatus("current")
_HwVoRecv_RRJ_Type = Counter32
_HwVoRecv_RRJ_Object = MibScalar
hwVoRecv_RRJ = _HwVoRecv_RRJ_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 3, 16),
    _HwVoRecv_RRJ_Type()
)
hwVoRecv_RRJ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoRecv_RRJ.setStatus("current")
_HwVoRecv_ARJ_Type = Counter32
_HwVoRecv_ARJ_Object = MibScalar
hwVoRecv_ARJ = _HwVoRecv_ARJ_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 3, 17),
    _HwVoRecv_ARJ_Type()
)
hwVoRecv_ARJ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoRecv_ARJ.setStatus("current")
_HwVoRecv_BRJ_Type = Counter32
_HwVoRecv_BRJ_Object = MibScalar
hwVoRecv_BRJ = _HwVoRecv_BRJ_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 3, 18),
    _HwVoRecv_BRJ_Type()
)
hwVoRecv_BRJ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoRecv_BRJ.setStatus("current")
_HwVoRecv_DRJ_Type = Counter32
_HwVoRecv_DRJ_Object = MibScalar
hwVoRecv_DRJ = _HwVoRecv_DRJ_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 3, 19),
    _HwVoRecv_DRJ_Type()
)
hwVoRecv_DRJ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoRecv_DRJ.setStatus("current")
_HwVoRecv_URQ_Type = Counter32
_HwVoRecv_URQ_Object = MibScalar
hwVoRecv_URQ = _HwVoRecv_URQ_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 3, 20),
    _HwVoRecv_URQ_Type()
)
hwVoRecv_URQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoRecv_URQ.setStatus("current")
_HwVoRecv_UCF_Type = Counter32
_HwVoRecv_UCF_Object = MibScalar
hwVoRecv_UCF = _HwVoRecv_UCF_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 3, 21),
    _HwVoRecv_UCF_Type()
)
hwVoRecv_UCF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoRecv_UCF.setStatus("current")
_HwVoRecv_URJ_Type = Counter32
_HwVoRecv_URJ_Object = MibScalar
hwVoRecv_URJ = _HwVoRecv_URJ_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 3, 22),
    _HwVoRecv_URJ_Type()
)
hwVoRecv_URJ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoRecv_URJ.setStatus("current")
_HwVoRecv_IRQ_Type = Counter32
_HwVoRecv_IRQ_Object = MibScalar
hwVoRecv_IRQ = _HwVoRecv_IRQ_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 3, 23),
    _HwVoRecv_IRQ_Type()
)
hwVoRecv_IRQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoRecv_IRQ.setStatus("current")
_HwVoRecv_UnknownRASMsg_Type = Counter32
_HwVoRecv_UnknownRASMsg_Object = MibScalar
hwVoRecv_UnknownRASMsg = _HwVoRecv_UnknownRASMsg_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 3, 24),
    _HwVoRecv_UnknownRASMsg_Type()
)
hwVoRecv_UnknownRASMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoRecv_UnknownRASMsg.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-VO-H323-CALL-STAT-MIB",
    **{"hwVoiceH323CallStatMIB": hwVoiceH323CallStatMIB,
       "hwVoH323CallStatObjects": hwVoH323CallStatObjects,
       "hwVoIPPH225StatObjects": hwVoIPPH225StatObjects,
       "hwVoSend-Setup": hwVoSend_Setup,
       "hwVoSend-CallProceeding": hwVoSend_CallProceeding,
       "hwVoSend-Alerting": hwVoSend_Alerting,
       "hwVoSend-Connect": hwVoSend_Connect,
       "hwVoSend-ReleaseComplete": hwVoSend_ReleaseComplete,
       "hwVoSend-FacilityIndUserInput": hwVoSend_FacilityIndUserInput,
       "hwVoSend-FacilityTCSRequest": hwVoSend_FacilityTCSRequest,
       "hwVoSend-FacilityTCSAck": hwVoSend_FacilityTCSAck,
       "hwVoSend-FacilityTCSReject": hwVoSend_FacilityTCSReject,
       "hwVoSend-FacilityOLCRequest": hwVoSend_FacilityOLCRequest,
       "hwVoSend-FacilityOLCAck": hwVoSend_FacilityOLCAck,
       "hwVoSend-FacilityOLCReject": hwVoSend_FacilityOLCReject,
       "hwVoSend-FacilityMSDRequest": hwVoSend_FacilityMSDRequest,
       "hwVoSend-FacilityMSDAck": hwVoSend_FacilityMSDAck,
       "hwVoSend-FacilityMSDReject": hwVoSend_FacilityMSDReject,
       "hwVoSend-FacilityCLCRequest": hwVoSend_FacilityCLCRequest,
       "hwVoSend-FacilityCLCAck": hwVoSend_FacilityCLCAck,
       "hwVoSend-FacilityStartH245": hwVoSend_FacilityStartH245,
       "hwVoSend-ErrorH225Msg": hwVoSend_ErrorH225Msg,
       "hwVoRecv-Setup": hwVoRecv_Setup,
       "hwVoRecv-CallProceeding": hwVoRecv_CallProceeding,
       "hwVoRecv-Alerting": hwVoRecv_Alerting,
       "hwVoRecv-Connect": hwVoRecv_Connect,
       "hwVoRecv-ReleaseComplete": hwVoRecv_ReleaseComplete,
       "hwVoRecv-Progress": hwVoRecv_Progress,
       "hwVoRecv-FacilityTCSRequest": hwVoRecv_FacilityTCSRequest,
       "hwVoRecv-FacilityTCSAck": hwVoRecv_FacilityTCSAck,
       "hwVoRecv-FacilityTCSReject": hwVoRecv_FacilityTCSReject,
       "hwVoRecv-FacilityOLCRequest": hwVoRecv_FacilityOLCRequest,
       "hwVoRecv-FacilityOLCAck": hwVoRecv_FacilityOLCAck,
       "hwVoRecv-FacilityOLCReject": hwVoRecv_FacilityOLCReject,
       "hwVoRecv-FacilityMSDRequest": hwVoRecv_FacilityMSDRequest,
       "hwVoRecv-FacilityMSDAck": hwVoRecv_FacilityMSDAck,
       "hwVoRecv-FacilityMSDReject": hwVoRecv_FacilityMSDReject,
       "hwVoRecv-FacilityCLCRequest": hwVoRecv_FacilityCLCRequest,
       "hwVoRecv-FacilityCLCAck": hwVoRecv_FacilityCLCAck,
       "hwVoRecv-UnknownH225Msg": hwVoRecv_UnknownH225Msg,
       "hwVoIPPH245StatObjects": hwVoIPPH245StatObjects,
       "hwVoSend-TCSRequest": hwVoSend_TCSRequest,
       "hwVoSend-TCSAck": hwVoSend_TCSAck,
       "hwVoSend-TCSReject": hwVoSend_TCSReject,
       "hwVoSend-MSDRequest": hwVoSend_MSDRequest,
       "hwVoSend-MSDAck": hwVoSend_MSDAck,
       "hwVoSend-MSDReject": hwVoSend_MSDReject,
       "hwVoSend-OLCRequest": hwVoSend_OLCRequest,
       "hwVoSend-OLCAck": hwVoSend_OLCAck,
       "hwVoSend-OLCReject": hwVoSend_OLCReject,
       "hwVoSend-CLCRequest": hwVoSend_CLCRequest,
       "hwVoSend-CLCAck": hwVoSend_CLCAck,
       "hwVoSend-UserInput": hwVoSend_UserInput,
       "hwVoSend-ErrorH245Msg": hwVoSend_ErrorH245Msg,
       "hwVoRecv-TCSRequest": hwVoRecv_TCSRequest,
       "hwVoRecv-TCSAck": hwVoRecv_TCSAck,
       "hwVoRecv-TCSReject": hwVoRecv_TCSReject,
       "hwVoRecv-MSDRequest": hwVoRecv_MSDRequest,
       "hwVoRecv-MSDAck": hwVoRecv_MSDAck,
       "hwVoRecv-MSDReject": hwVoRecv_MSDReject,
       "hwVoRecv-OLCRequest": hwVoRecv_OLCRequest,
       "hwVoRecv-OLCAck": hwVoRecv_OLCAck,
       "hwVoRecv-OLCReject": hwVoRecv_OLCReject,
       "hwVoRecv-CLCRequest": hwVoRecv_CLCRequest,
       "hwVoRecv-CLCAck": hwVoRecv_CLCAck,
       "hwVoRecv-UserInput": hwVoRecv_UserInput,
       "hwVoRecv-UnknownH245Msg": hwVoRecv_UnknownH245Msg,
       "hwVoIPPRASStatObjects": hwVoIPPRASStatObjects,
       "hwVoSend-GRQ": hwVoSend_GRQ,
       "hwVoSend-RRQ": hwVoSend_RRQ,
       "hwVoSend-ARQ": hwVoSend_ARQ,
       "hwVoSend-BRQ": hwVoSend_BRQ,
       "hwVoSend-DRQ": hwVoSend_DRQ,
       "hwVoSend-URQ": hwVoSend_URQ,
       "hwVoSend-UCF": hwVoSend_UCF,
       "hwVoSend-IRR": hwVoSend_IRR,
       "hwVoSend-ErrorRASMsg": hwVoSend_ErrorRASMsg,
       "hwVoRecv-GCF": hwVoRecv_GCF,
       "hwVoRecv-RCF": hwVoRecv_RCF,
       "hwVoRecv-ACF": hwVoRecv_ACF,
       "hwVoRecv-BCF": hwVoRecv_BCF,
       "hwVoRecv-DCF": hwVoRecv_DCF,
       "hwVoRecv-GRJ": hwVoRecv_GRJ,
       "hwVoRecv-RRJ": hwVoRecv_RRJ,
       "hwVoRecv-ARJ": hwVoRecv_ARJ,
       "hwVoRecv-BRJ": hwVoRecv_BRJ,
       "hwVoRecv-DRJ": hwVoRecv_DRJ,
       "hwVoRecv-URQ": hwVoRecv_URQ,
       "hwVoRecv-UCF": hwVoRecv_UCF,
       "hwVoRecv-URJ": hwVoRecv_URJ,
       "hwVoRecv-IRQ": hwVoRecv_IRQ,
       "hwVoRecv-UnknownRASMsg": hwVoRecv_UnknownRASMsg}
)
