# SNMP MIB module (H225-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/H225-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:49:36 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(MmAliasAddress,
 MmAliasTag,
 MmCallType,
 MmGlobalIdentifier,
 MmH225Crv,
 MmH323EndpointType,
 MmTAddressTag,
 mmH323Root) = mibBuilder.importSymbols(
    "MULTI-MEDIA-MIB-TC",
    "MmAliasAddress",
    "MmAliasTag",
    "MmCallType",
    "MmGlobalIdentifier",
    "MmH225Crv",
    "MmH323EndpointType",
    "MmTAddressTag",
    "mmH323Root")

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

(DateAndTime,
 DisplayString,
 TAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TAddress",
    "TextualConvention")


# MODULE-IDENTITY

h225CallSignaling = ModuleIdentity(
    (0, 0, 8, 341, 1, 1, 1)
)
h225CallSignaling.setRevisions(
        ("1998-12-14 12:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CallSignalConfig_ObjectIdentity = ObjectIdentity
callSignalConfig = _CallSignalConfig_ObjectIdentity(
    (0, 0, 8, 341, 1, 1, 1, 1)
)
_CallSignalConfigTable_Object = MibTable
callSignalConfigTable = _CallSignalConfigTable_Object(
    (0, 0, 8, 341, 1, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    callSignalConfigTable.setStatus("current")
_CallSignalConfigEntry_Object = MibTableRow
callSignalConfigEntry = _CallSignalConfigEntry_Object(
    (0, 0, 8, 341, 1, 1, 1, 1, 1, 1)
)
callSignalConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    callSignalConfigEntry.setStatus("current")
_CallSignalConfigMaxConnections_Type = Integer32
_CallSignalConfigMaxConnections_Object = MibTableColumn
callSignalConfigMaxConnections = _CallSignalConfigMaxConnections_Object(
    (0, 0, 8, 341, 1, 1, 1, 1, 1, 1, 1),
    _CallSignalConfigMaxConnections_Type()
)
callSignalConfigMaxConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callSignalConfigMaxConnections.setStatus("current")
_CallSignalConfigAvailableConnections_Type = Integer32
_CallSignalConfigAvailableConnections_Object = MibTableColumn
callSignalConfigAvailableConnections = _CallSignalConfigAvailableConnections_Object(
    (0, 0, 8, 341, 1, 1, 1, 1, 1, 1, 2),
    _CallSignalConfigAvailableConnections_Type()
)
callSignalConfigAvailableConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callSignalConfigAvailableConnections.setStatus("current")
_CallSignalConfigT303_Type = Integer32
_CallSignalConfigT303_Object = MibTableColumn
callSignalConfigT303 = _CallSignalConfigT303_Object(
    (0, 0, 8, 341, 1, 1, 1, 1, 1, 1, 3),
    _CallSignalConfigT303_Type()
)
callSignalConfigT303.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    callSignalConfigT303.setStatus("current")
_CallSignalConfigT301_Type = Integer32
_CallSignalConfigT301_Object = MibTableColumn
callSignalConfigT301 = _CallSignalConfigT301_Object(
    (0, 0, 8, 341, 1, 1, 1, 1, 1, 1, 4),
    _CallSignalConfigT301_Type()
)
callSignalConfigT301.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    callSignalConfigT301.setStatus("current")


class _CallSignalConfigEnableNotifications_Type(Integer32):
    """Custom type callSignalConfigEnableNotifications based on Integer32"""
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


_CallSignalConfigEnableNotifications_Type.__name__ = "Integer32"
_CallSignalConfigEnableNotifications_Object = MibTableColumn
callSignalConfigEnableNotifications = _CallSignalConfigEnableNotifications_Object(
    (0, 0, 8, 341, 1, 1, 1, 1, 1, 1, 5),
    _CallSignalConfigEnableNotifications_Type()
)
callSignalConfigEnableNotifications.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    callSignalConfigEnableNotifications.setStatus("current")
_CallSignalStats_ObjectIdentity = ObjectIdentity
callSignalStats = _CallSignalStats_ObjectIdentity(
    (0, 0, 8, 341, 1, 1, 1, 2)
)
_CallSignalStatsTable_Object = MibTable
callSignalStatsTable = _CallSignalStatsTable_Object(
    (0, 0, 8, 341, 1, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    callSignalStatsTable.setStatus("current")
_CallSignalStatsEntry_Object = MibTableRow
callSignalStatsEntry = _CallSignalStatsEntry_Object(
    (0, 0, 8, 341, 1, 1, 1, 2, 1, 1)
)
callSignalStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    callSignalStatsEntry.setStatus("current")
_CallSignalStatsCallConnectionsIn_Type = Counter32
_CallSignalStatsCallConnectionsIn_Object = MibScalar
callSignalStatsCallConnectionsIn = _CallSignalStatsCallConnectionsIn_Object(
    (0, 0, 8, 341, 1, 1, 1, 2, 1, 1, 1),
    _CallSignalStatsCallConnectionsIn_Type()
)
callSignalStatsCallConnectionsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callSignalStatsCallConnectionsIn.setStatus("current")
_CallSignalStatsCallConnectionsOut_Type = Counter32
_CallSignalStatsCallConnectionsOut_Object = MibScalar
callSignalStatsCallConnectionsOut = _CallSignalStatsCallConnectionsOut_Object(
    (0, 0, 8, 341, 1, 1, 1, 2, 1, 1, 2),
    _CallSignalStatsCallConnectionsOut_Type()
)
callSignalStatsCallConnectionsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callSignalStatsCallConnectionsOut.setStatus("current")
_CallSignalStatsAlertingMsgsIn_Type = Counter32
_CallSignalStatsAlertingMsgsIn_Object = MibScalar
callSignalStatsAlertingMsgsIn = _CallSignalStatsAlertingMsgsIn_Object(
    (0, 0, 8, 341, 1, 1, 1, 2, 1, 1, 3),
    _CallSignalStatsAlertingMsgsIn_Type()
)
callSignalStatsAlertingMsgsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callSignalStatsAlertingMsgsIn.setStatus("current")
_CallSignalStatsAlertingMsgsOut_Type = Counter32
_CallSignalStatsAlertingMsgsOut_Object = MibScalar
callSignalStatsAlertingMsgsOut = _CallSignalStatsAlertingMsgsOut_Object(
    (0, 0, 8, 341, 1, 1, 1, 2, 1, 1, 4),
    _CallSignalStatsAlertingMsgsOut_Type()
)
callSignalStatsAlertingMsgsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callSignalStatsAlertingMsgsOut.setStatus("current")
_CallSignalStatsCallProceedingsIn_Type = Counter32
_CallSignalStatsCallProceedingsIn_Object = MibScalar
callSignalStatsCallProceedingsIn = _CallSignalStatsCallProceedingsIn_Object(
    (0, 0, 8, 341, 1, 1, 1, 2, 1, 1, 5),
    _CallSignalStatsCallProceedingsIn_Type()
)
callSignalStatsCallProceedingsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callSignalStatsCallProceedingsIn.setStatus("current")
_CallSignalStatsCallProceedingsOut_Type = Counter32
_CallSignalStatsCallProceedingsOut_Object = MibScalar
callSignalStatsCallProceedingsOut = _CallSignalStatsCallProceedingsOut_Object(
    (0, 0, 8, 341, 1, 1, 1, 2, 1, 1, 6),
    _CallSignalStatsCallProceedingsOut_Type()
)
callSignalStatsCallProceedingsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callSignalStatsCallProceedingsOut.setStatus("current")
_CallSignalStatsSetupMsgsIn_Type = Counter32
_CallSignalStatsSetupMsgsIn_Object = MibScalar
callSignalStatsSetupMsgsIn = _CallSignalStatsSetupMsgsIn_Object(
    (0, 0, 8, 341, 1, 1, 1, 2, 1, 1, 7),
    _CallSignalStatsSetupMsgsIn_Type()
)
callSignalStatsSetupMsgsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callSignalStatsSetupMsgsIn.setStatus("current")
_CallSignalStatsSetupMsgsOut_Type = Counter32
_CallSignalStatsSetupMsgsOut_Object = MibScalar
callSignalStatsSetupMsgsOut = _CallSignalStatsSetupMsgsOut_Object(
    (0, 0, 8, 341, 1, 1, 1, 2, 1, 1, 8),
    _CallSignalStatsSetupMsgsOut_Type()
)
callSignalStatsSetupMsgsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callSignalStatsSetupMsgsOut.setStatus("current")
_CallSignalStatsSetupAckMsgsIn_Type = Counter32
_CallSignalStatsSetupAckMsgsIn_Object = MibScalar
callSignalStatsSetupAckMsgsIn = _CallSignalStatsSetupAckMsgsIn_Object(
    (0, 0, 8, 341, 1, 1, 1, 2, 1, 1, 9),
    _CallSignalStatsSetupAckMsgsIn_Type()
)
callSignalStatsSetupAckMsgsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callSignalStatsSetupAckMsgsIn.setStatus("current")
_CallSignalStatsSetupAckMsgsOut_Type = Counter32
_CallSignalStatsSetupAckMsgsOut_Object = MibScalar
callSignalStatsSetupAckMsgsOut = _CallSignalStatsSetupAckMsgsOut_Object(
    (0, 0, 8, 341, 1, 1, 1, 2, 1, 1, 10),
    _CallSignalStatsSetupAckMsgsOut_Type()
)
callSignalStatsSetupAckMsgsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callSignalStatsSetupAckMsgsOut.setStatus("current")
_CallSignalStatsProgressMsgsIn_Type = Counter32
_CallSignalStatsProgressMsgsIn_Object = MibScalar
callSignalStatsProgressMsgsIn = _CallSignalStatsProgressMsgsIn_Object(
    (0, 0, 8, 341, 1, 1, 1, 2, 1, 1, 11),
    _CallSignalStatsProgressMsgsIn_Type()
)
callSignalStatsProgressMsgsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callSignalStatsProgressMsgsIn.setStatus("current")
_CallSignalStatsProgressMsgsOut_Type = Counter32
_CallSignalStatsProgressMsgsOut_Object = MibScalar
callSignalStatsProgressMsgsOut = _CallSignalStatsProgressMsgsOut_Object(
    (0, 0, 8, 341, 1, 1, 1, 2, 1, 1, 12),
    _CallSignalStatsProgressMsgsOut_Type()
)
callSignalStatsProgressMsgsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callSignalStatsProgressMsgsOut.setStatus("current")
_CallSignalStatsReleaseCompleteMsgsIn_Type = Counter32
_CallSignalStatsReleaseCompleteMsgsIn_Object = MibScalar
callSignalStatsReleaseCompleteMsgsIn = _CallSignalStatsReleaseCompleteMsgsIn_Object(
    (0, 0, 8, 341, 1, 1, 1, 2, 1, 1, 13),
    _CallSignalStatsReleaseCompleteMsgsIn_Type()
)
callSignalStatsReleaseCompleteMsgsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callSignalStatsReleaseCompleteMsgsIn.setStatus("current")
_CallSignalStatsReleaseCompleteMsgsOut_Type = Counter32
_CallSignalStatsReleaseCompleteMsgsOut_Object = MibScalar
callSignalStatsReleaseCompleteMsgsOut = _CallSignalStatsReleaseCompleteMsgsOut_Object(
    (0, 0, 8, 341, 1, 1, 1, 2, 1, 1, 14),
    _CallSignalStatsReleaseCompleteMsgsOut_Type()
)
callSignalStatsReleaseCompleteMsgsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callSignalStatsReleaseCompleteMsgsOut.setStatus("current")
_CallSignalStatsStatusMsgsIn_Type = Counter32
_CallSignalStatsStatusMsgsIn_Object = MibScalar
callSignalStatsStatusMsgsIn = _CallSignalStatsStatusMsgsIn_Object(
    (0, 0, 8, 341, 1, 1, 1, 2, 1, 1, 15),
    _CallSignalStatsStatusMsgsIn_Type()
)
callSignalStatsStatusMsgsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callSignalStatsStatusMsgsIn.setStatus("current")
_CallSignalStatsStatusMsgsOut_Type = Counter32
_CallSignalStatsStatusMsgsOut_Object = MibScalar
callSignalStatsStatusMsgsOut = _CallSignalStatsStatusMsgsOut_Object(
    (0, 0, 8, 341, 1, 1, 1, 2, 1, 1, 16),
    _CallSignalStatsStatusMsgsOut_Type()
)
callSignalStatsStatusMsgsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callSignalStatsStatusMsgsOut.setStatus("current")
_CallSignalStatsStatusInquiryMsgsIn_Type = Counter32
_CallSignalStatsStatusInquiryMsgsIn_Object = MibScalar
callSignalStatsStatusInquiryMsgsIn = _CallSignalStatsStatusInquiryMsgsIn_Object(
    (0, 0, 8, 341, 1, 1, 1, 2, 1, 1, 17),
    _CallSignalStatsStatusInquiryMsgsIn_Type()
)
callSignalStatsStatusInquiryMsgsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callSignalStatsStatusInquiryMsgsIn.setStatus("current")
_CallSignalStatsStatusInquiryMsgsOut_Type = Counter32
_CallSignalStatsStatusInquiryMsgsOut_Object = MibScalar
callSignalStatsStatusInquiryMsgsOut = _CallSignalStatsStatusInquiryMsgsOut_Object(
    (0, 0, 8, 341, 1, 1, 1, 2, 1, 1, 18),
    _CallSignalStatsStatusInquiryMsgsOut_Type()
)
callSignalStatsStatusInquiryMsgsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callSignalStatsStatusInquiryMsgsOut.setStatus("current")
_CallSignalStatsFacilityMsgsIn_Type = Counter32
_CallSignalStatsFacilityMsgsIn_Object = MibScalar
callSignalStatsFacilityMsgsIn = _CallSignalStatsFacilityMsgsIn_Object(
    (0, 0, 8, 341, 1, 1, 1, 2, 1, 1, 19),
    _CallSignalStatsFacilityMsgsIn_Type()
)
callSignalStatsFacilityMsgsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callSignalStatsFacilityMsgsIn.setStatus("current")
_CallSignalStatsFacilityMsgsOut_Type = Counter32
_CallSignalStatsFacilityMsgsOut_Object = MibScalar
callSignalStatsFacilityMsgsOut = _CallSignalStatsFacilityMsgsOut_Object(
    (0, 0, 8, 341, 1, 1, 1, 2, 1, 1, 20),
    _CallSignalStatsFacilityMsgsOut_Type()
)
callSignalStatsFacilityMsgsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callSignalStatsFacilityMsgsOut.setStatus("current")
_CallSignalStatsInfoMsgsIn_Type = Counter32
_CallSignalStatsInfoMsgsIn_Object = MibScalar
callSignalStatsInfoMsgsIn = _CallSignalStatsInfoMsgsIn_Object(
    (0, 0, 8, 341, 1, 1, 1, 2, 1, 1, 21),
    _CallSignalStatsInfoMsgsIn_Type()
)
callSignalStatsInfoMsgsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callSignalStatsInfoMsgsIn.setStatus("current")
_CallSignalStatsInfoMsgsOut_Type = Counter32
_CallSignalStatsInfoMsgsOut_Object = MibScalar
callSignalStatsInfoMsgsOut = _CallSignalStatsInfoMsgsOut_Object(
    (0, 0, 8, 341, 1, 1, 1, 2, 1, 1, 22),
    _CallSignalStatsInfoMsgsOut_Type()
)
callSignalStatsInfoMsgsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callSignalStatsInfoMsgsOut.setStatus("current")
_CallSignalStatsNotifyMsgsIn_Type = Counter32
_CallSignalStatsNotifyMsgsIn_Object = MibScalar
callSignalStatsNotifyMsgsIn = _CallSignalStatsNotifyMsgsIn_Object(
    (0, 0, 8, 341, 1, 1, 1, 2, 1, 1, 23),
    _CallSignalStatsNotifyMsgsIn_Type()
)
callSignalStatsNotifyMsgsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callSignalStatsNotifyMsgsIn.setStatus("current")
_CallSignalStatsNotifyMsgsOut_Type = Counter32
_CallSignalStatsNotifyMsgsOut_Object = MibScalar
callSignalStatsNotifyMsgsOut = _CallSignalStatsNotifyMsgsOut_Object(
    (0, 0, 8, 341, 1, 1, 1, 2, 1, 1, 24),
    _CallSignalStatsNotifyMsgsOut_Type()
)
callSignalStatsNotifyMsgsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callSignalStatsNotifyMsgsOut.setStatus("current")
_CallSignalStatsAverageCallDuration_Type = Integer32
_CallSignalStatsAverageCallDuration_Object = MibTableColumn
callSignalStatsAverageCallDuration = _CallSignalStatsAverageCallDuration_Object(
    (0, 0, 8, 341, 1, 1, 1, 2, 1, 1, 25),
    _CallSignalStatsAverageCallDuration_Type()
)
callSignalStatsAverageCallDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callSignalStatsAverageCallDuration.setStatus("current")
_Connections_ObjectIdentity = ObjectIdentity
connections = _Connections_ObjectIdentity(
    (0, 0, 8, 341, 1, 1, 1, 3)
)
_ConnectionsActiveConnections_Type = Integer32
_ConnectionsActiveConnections_Object = MibScalar
connectionsActiveConnections = _ConnectionsActiveConnections_Object(
    (0, 0, 8, 341, 1, 1, 1, 3, 1),
    _ConnectionsActiveConnections_Type()
)
connectionsActiveConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionsActiveConnections.setStatus("current")
_ConnectionsTable_Object = MibTable
connectionsTable = _ConnectionsTable_Object(
    (0, 0, 8, 341, 1, 1, 1, 3, 2)
)
if mibBuilder.loadTexts:
    connectionsTable.setStatus("current")
_ConnectionsTableEntry_Object = MibTableRow
connectionsTableEntry = _ConnectionsTableEntry_Object(
    (0, 0, 8, 341, 1, 1, 1, 3, 2, 1)
)
connectionsTableEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "H225-MIB", "connectionsSrcTransporTAddressTag"),
    (0, "H225-MIB", "connectionsSrcTransporTAddress"),
    (0, "H225-MIB", "connectionsCallIdentifier"),
)
if mibBuilder.loadTexts:
    connectionsTableEntry.setStatus("current")
_ConnectionsSrcTransporTAddressTag_Type = MmTAddressTag
_ConnectionsSrcTransporTAddressTag_Object = MibTableColumn
connectionsSrcTransporTAddressTag = _ConnectionsSrcTransporTAddressTag_Object(
    (0, 0, 8, 341, 1, 1, 1, 3, 2, 1, 1),
    _ConnectionsSrcTransporTAddressTag_Type()
)
connectionsSrcTransporTAddressTag.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    connectionsSrcTransporTAddressTag.setStatus("current")
_ConnectionsSrcTransporTAddress_Type = TAddress
_ConnectionsSrcTransporTAddress_Object = MibTableColumn
connectionsSrcTransporTAddress = _ConnectionsSrcTransporTAddress_Object(
    (0, 0, 8, 341, 1, 1, 1, 3, 2, 1, 2),
    _ConnectionsSrcTransporTAddress_Type()
)
connectionsSrcTransporTAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    connectionsSrcTransporTAddress.setStatus("current")
_ConnectionsCallIdentifier_Type = MmGlobalIdentifier
_ConnectionsCallIdentifier_Object = MibTableColumn
connectionsCallIdentifier = _ConnectionsCallIdentifier_Object(
    (0, 0, 8, 341, 1, 1, 1, 3, 2, 1, 3),
    _ConnectionsCallIdentifier_Type()
)
connectionsCallIdentifier.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    connectionsCallIdentifier.setStatus("current")


class _ConnectionsRole_Type(Integer32):
    """Custom type connectionsRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("callee", 2),
          ("caller", 1))
    )


_ConnectionsRole_Type.__name__ = "Integer32"
_ConnectionsRole_Object = MibTableColumn
connectionsRole = _ConnectionsRole_Object(
    (0, 0, 8, 341, 1, 1, 1, 3, 2, 1, 4),
    _ConnectionsRole_Type()
)
connectionsRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionsRole.setStatus("current")


class _ConnectionsState_Type(Integer32):
    """Custom type connectionsState based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("active", 7),
          ("callDelivered", 2),
          ("callInitiated", 1),
          ("callPresent", 3),
          ("callProceeding", 6),
          ("callReceived", 4),
          ("connectRequest", 5),
          ("disconnectIndication", 9),
          ("disconnectRequest", 8),
          ("releaseRequest", 10))
    )


_ConnectionsState_Type.__name__ = "Integer32"
_ConnectionsState_Object = MibTableColumn
connectionsState = _ConnectionsState_Object(
    (0, 0, 8, 341, 1, 1, 1, 3, 2, 1, 5),
    _ConnectionsState_Type()
)
connectionsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionsState.setStatus("current")
_ConnectionsDestTransporTAddressTag_Type = MmTAddressTag
_ConnectionsDestTransporTAddressTag_Object = MibTableColumn
connectionsDestTransporTAddressTag = _ConnectionsDestTransporTAddressTag_Object(
    (0, 0, 8, 341, 1, 1, 1, 3, 2, 1, 6),
    _ConnectionsDestTransporTAddressTag_Type()
)
connectionsDestTransporTAddressTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionsDestTransporTAddressTag.setStatus("current")
_ConnectionsDestTransporTAddress_Type = TAddress
_ConnectionsDestTransporTAddress_Object = MibTableColumn
connectionsDestTransporTAddress = _ConnectionsDestTransporTAddress_Object(
    (0, 0, 8, 341, 1, 1, 1, 3, 2, 1, 7),
    _ConnectionsDestTransporTAddress_Type()
)
connectionsDestTransporTAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionsDestTransporTAddress.setStatus("current")
_ConnectionsDestAliasTag_Type = MmAliasTag
_ConnectionsDestAliasTag_Object = MibTableColumn
connectionsDestAliasTag = _ConnectionsDestAliasTag_Object(
    (0, 0, 8, 341, 1, 1, 1, 3, 2, 1, 8),
    _ConnectionsDestAliasTag_Type()
)
connectionsDestAliasTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionsDestAliasTag.setStatus("current")
_ConnectionsDestAlias_Type = MmAliasAddress
_ConnectionsDestAlias_Object = MibTableColumn
connectionsDestAlias = _ConnectionsDestAlias_Object(
    (0, 0, 8, 341, 1, 1, 1, 3, 2, 1, 9),
    _ConnectionsDestAlias_Type()
)
connectionsDestAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionsDestAlias.setStatus("current")
_ConnectionsSrcH245SigTransporTAddressTag_Type = MmTAddressTag
_ConnectionsSrcH245SigTransporTAddressTag_Object = MibTableColumn
connectionsSrcH245SigTransporTAddressTag = _ConnectionsSrcH245SigTransporTAddressTag_Object(
    (0, 0, 8, 341, 1, 1, 1, 3, 2, 1, 10),
    _ConnectionsSrcH245SigTransporTAddressTag_Type()
)
connectionsSrcH245SigTransporTAddressTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionsSrcH245SigTransporTAddressTag.setStatus("current")
_ConnectionsSrcH245SigTransporTAddress_Type = TAddress
_ConnectionsSrcH245SigTransporTAddress_Object = MibTableColumn
connectionsSrcH245SigTransporTAddress = _ConnectionsSrcH245SigTransporTAddress_Object(
    (0, 0, 8, 341, 1, 1, 1, 3, 2, 1, 11),
    _ConnectionsSrcH245SigTransporTAddress_Type()
)
connectionsSrcH245SigTransporTAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionsSrcH245SigTransporTAddress.setStatus("current")
_ConnectionsDestH245SigTransporTAddressTag_Type = MmTAddressTag
_ConnectionsDestH245SigTransporTAddressTag_Object = MibTableColumn
connectionsDestH245SigTransporTAddressTag = _ConnectionsDestH245SigTransporTAddressTag_Object(
    (0, 0, 8, 341, 1, 1, 1, 3, 2, 1, 12),
    _ConnectionsDestH245SigTransporTAddressTag_Type()
)
connectionsDestH245SigTransporTAddressTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionsDestH245SigTransporTAddressTag.setStatus("current")
_ConnectionsDestH245SigTransporTAddress_Type = TAddress
_ConnectionsDestH245SigTransporTAddress_Object = MibTableColumn
connectionsDestH245SigTransporTAddress = _ConnectionsDestH245SigTransporTAddress_Object(
    (0, 0, 8, 341, 1, 1, 1, 3, 2, 1, 13),
    _ConnectionsDestH245SigTransporTAddress_Type()
)
connectionsDestH245SigTransporTAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionsDestH245SigTransporTAddress.setStatus("current")
_ConnectionsConfId_Type = MmGlobalIdentifier
_ConnectionsConfId_Object = MibTableColumn
connectionsConfId = _ConnectionsConfId_Object(
    (0, 0, 8, 341, 1, 1, 1, 3, 2, 1, 14),
    _ConnectionsConfId_Type()
)
connectionsConfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionsConfId.setStatus("current")
_ConnectionsCalledPartyNumber_Type = DisplayString
_ConnectionsCalledPartyNumber_Object = MibTableColumn
connectionsCalledPartyNumber = _ConnectionsCalledPartyNumber_Object(
    (0, 0, 8, 341, 1, 1, 1, 3, 2, 1, 15),
    _ConnectionsCalledPartyNumber_Type()
)
connectionsCalledPartyNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionsCalledPartyNumber.setStatus("current")
_ConnectionsDestXtraCallingNumber1_Type = DisplayString
_ConnectionsDestXtraCallingNumber1_Object = MibTableColumn
connectionsDestXtraCallingNumber1 = _ConnectionsDestXtraCallingNumber1_Object(
    (0, 0, 8, 341, 1, 1, 1, 3, 2, 1, 16),
    _ConnectionsDestXtraCallingNumber1_Type()
)
connectionsDestXtraCallingNumber1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionsDestXtraCallingNumber1.setStatus("current")
_ConnectionsDestXtraCallingNumber2_Type = DisplayString
_ConnectionsDestXtraCallingNumber2_Object = MibTableColumn
connectionsDestXtraCallingNumber2 = _ConnectionsDestXtraCallingNumber2_Object(
    (0, 0, 8, 341, 1, 1, 1, 3, 2, 1, 17),
    _ConnectionsDestXtraCallingNumber2_Type()
)
connectionsDestXtraCallingNumber2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionsDestXtraCallingNumber2.setStatus("current")
_ConnectionsDestXtraCallingNumber3_Type = DisplayString
_ConnectionsDestXtraCallingNumber3_Object = MibTableColumn
connectionsDestXtraCallingNumber3 = _ConnectionsDestXtraCallingNumber3_Object(
    (0, 0, 8, 341, 1, 1, 1, 3, 2, 1, 18),
    _ConnectionsDestXtraCallingNumber3_Type()
)
connectionsDestXtraCallingNumber3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionsDestXtraCallingNumber3.setStatus("current")
_ConnectionsDestXtraCallingNumber4_Type = DisplayString
_ConnectionsDestXtraCallingNumber4_Object = MibTableColumn
connectionsDestXtraCallingNumber4 = _ConnectionsDestXtraCallingNumber4_Object(
    (0, 0, 8, 341, 1, 1, 1, 3, 2, 1, 19),
    _ConnectionsDestXtraCallingNumber4_Type()
)
connectionsDestXtraCallingNumber4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionsDestXtraCallingNumber4.setStatus("current")
_ConnectionsDestXtraCallingNumber5_Type = DisplayString
_ConnectionsDestXtraCallingNumber5_Object = MibTableColumn
connectionsDestXtraCallingNumber5 = _ConnectionsDestXtraCallingNumber5_Object(
    (0, 0, 8, 341, 1, 1, 1, 3, 2, 1, 20),
    _ConnectionsDestXtraCallingNumber5_Type()
)
connectionsDestXtraCallingNumber5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionsDestXtraCallingNumber5.setStatus("current")


class _ConnectionsFastCall_Type(Integer32):
    """Custom type connectionsFastCall based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_ConnectionsFastCall_Type.__name__ = "Integer32"
_ConnectionsFastCall_Object = MibTableColumn
connectionsFastCall = _ConnectionsFastCall_Object(
    (0, 0, 8, 341, 1, 1, 1, 3, 2, 1, 21),
    _ConnectionsFastCall_Type()
)
connectionsFastCall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionsFastCall.setStatus("current")


class _ConnectionsSecurity_Type(Integer32):
    """Custom type connectionsSecurity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_ConnectionsSecurity_Type.__name__ = "Integer32"
_ConnectionsSecurity_Object = MibTableColumn
connectionsSecurity = _ConnectionsSecurity_Object(
    (0, 0, 8, 341, 1, 1, 1, 3, 2, 1, 22),
    _ConnectionsSecurity_Type()
)
connectionsSecurity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionsSecurity.setStatus("current")


class _ConnectionsH245Tunneling_Type(Integer32):
    """Custom type connectionsH245Tunneling based on Integer32"""
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
        *(("active", 3),
          ("available", 2),
          ("closed", 5),
          ("closing", 4),
          ("notSupported", 1))
    )


_ConnectionsH245Tunneling_Type.__name__ = "Integer32"
_ConnectionsH245Tunneling_Object = MibTableColumn
connectionsH245Tunneling = _ConnectionsH245Tunneling_Object(
    (0, 0, 8, 341, 1, 1, 1, 3, 2, 1, 23),
    _ConnectionsH245Tunneling_Type()
)
connectionsH245Tunneling.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionsH245Tunneling.setStatus("current")


class _ConnectionsCanOverlapSend_Type(Integer32):
    """Custom type connectionsCanOverlapSend based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_ConnectionsCanOverlapSend_Type.__name__ = "Integer32"
_ConnectionsCanOverlapSend_Object = MibTableColumn
connectionsCanOverlapSend = _ConnectionsCanOverlapSend_Object(
    (0, 0, 8, 341, 1, 1, 1, 3, 2, 1, 24),
    _ConnectionsCanOverlapSend_Type()
)
connectionsCanOverlapSend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionsCanOverlapSend.setStatus("current")
_ConnectionsCRV_Type = MmH225Crv
_ConnectionsCRV_Object = MibTableColumn
connectionsCRV = _ConnectionsCRV_Object(
    (0, 0, 8, 341, 1, 1, 1, 3, 2, 1, 25),
    _ConnectionsCRV_Type()
)
connectionsCRV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionsCRV.setStatus("current")
_ConnectionsCallType_Type = MmCallType
_ConnectionsCallType_Object = MibTableColumn
connectionsCallType = _ConnectionsCallType_Object(
    (0, 0, 8, 341, 1, 1, 1, 3, 2, 1, 26),
    _ConnectionsCallType_Type()
)
connectionsCallType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionsCallType.setStatus("current")
_ConnectionsRemoteExtensionAddress_Type = OctetString
_ConnectionsRemoteExtensionAddress_Object = MibTableColumn
connectionsRemoteExtensionAddress = _ConnectionsRemoteExtensionAddress_Object(
    (0, 0, 8, 341, 1, 1, 1, 3, 2, 1, 27),
    _ConnectionsRemoteExtensionAddress_Type()
)
connectionsRemoteExtensionAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionsRemoteExtensionAddress.setStatus("current")
_ConnectionsExtraCRV1_Type = MmH225Crv
_ConnectionsExtraCRV1_Object = MibTableColumn
connectionsExtraCRV1 = _ConnectionsExtraCRV1_Object(
    (0, 0, 8, 341, 1, 1, 1, 3, 2, 1, 28),
    _ConnectionsExtraCRV1_Type()
)
connectionsExtraCRV1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionsExtraCRV1.setStatus("current")
_ConnectionsExtraCRV2_Type = MmH225Crv
_ConnectionsExtraCRV2_Object = MibTableColumn
connectionsExtraCRV2 = _ConnectionsExtraCRV2_Object(
    (0, 0, 8, 341, 1, 1, 1, 3, 2, 1, 29),
    _ConnectionsExtraCRV2_Type()
)
connectionsExtraCRV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionsExtraCRV2.setStatus("current")
_ConnectionsConnectionStartTime_Type = DateAndTime
_ConnectionsConnectionStartTime_Object = MibTableColumn
connectionsConnectionStartTime = _ConnectionsConnectionStartTime_Object(
    (0, 0, 8, 341, 1, 1, 1, 3, 2, 1, 30),
    _ConnectionsConnectionStartTime_Type()
)
connectionsConnectionStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionsConnectionStartTime.setStatus("current")
_ConnectionsEndpointType_Type = MmH323EndpointType
_ConnectionsEndpointType_Object = MibTableColumn
connectionsEndpointType = _ConnectionsEndpointType_Object(
    (0, 0, 8, 341, 1, 1, 1, 3, 2, 1, 31),
    _ConnectionsEndpointType_Type()
)
connectionsEndpointType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionsEndpointType.setStatus("current")


class _ConnectionsReleaseCompleteReason_Type(Integer32):
    """Custom type connectionsReleaseCompleteReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              16,
              17,
              28,
              31,
              34,
              38,
              41,
              42,
              47,
              88,
              111)
        )
    )
    namedValues = NamedValues(
        *(("adaptiveBusy", 41),
          ("badFormaTAddress", 28),
          ("destinationReject", 16),
          ("gatekeeperResourcesUnavailable", 47),
          ("gatewayResources", 42),
          ("inConference", 17),
          ("invalidRevision", 88),
          ("noBandwidth", 34),
          ("noPermission", 111),
          ("undefined", 31),
          ("unreachableDestination", 3),
          ("unreachableGatekeeper", 38))
    )


_ConnectionsReleaseCompleteReason_Type.__name__ = "Integer32"
_ConnectionsReleaseCompleteReason_Object = MibTableColumn
connectionsReleaseCompleteReason = _ConnectionsReleaseCompleteReason_Object(
    (0, 0, 8, 341, 1, 1, 1, 3, 2, 1, 32),
    _ConnectionsReleaseCompleteReason_Type()
)
connectionsReleaseCompleteReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionsReleaseCompleteReason.setStatus("current")
_CallSignalEvents_ObjectIdentity = ObjectIdentity
callSignalEvents = _CallSignalEvents_ObjectIdentity(
    (0, 0, 8, 341, 1, 1, 1, 4, 0)
)
_CallSignalingMIBConformance_ObjectIdentity = ObjectIdentity
callSignalingMIBConformance = _CallSignalingMIBConformance_ObjectIdentity(
    (0, 0, 8, 341, 1, 1, 1, 5)
)
_CallSignalingMIBGroups_ObjectIdentity = ObjectIdentity
callSignalingMIBGroups = _CallSignalingMIBGroups_ObjectIdentity(
    (0, 0, 8, 341, 1, 1, 1, 5, 1)
)

# Managed Objects groups

callSignalConfigGroup = ObjectGroup(
    (0, 0, 8, 341, 1, 1, 1, 5, 1, 1)
)
callSignalConfigGroup.setObjects(
      *(("H225-MIB", "callSignalConfigMaxConnections"),
        ("H225-MIB", "callSignalConfigAvailableConnections"),
        ("H225-MIB", "callSignalConfigT303"),
        ("H225-MIB", "callSignalConfigT301"),
        ("H225-MIB", "callSignalConfigEnableNotifications"))
)
if mibBuilder.loadTexts:
    callSignalConfigGroup.setStatus("current")

callSignalStatsGroup = ObjectGroup(
    (0, 0, 8, 341, 1, 1, 1, 5, 1, 2)
)
callSignalStatsGroup.setObjects(
      *(("H225-MIB", "callSignalStatsCallConnectionsIn"),
        ("H225-MIB", "callSignalStatsCallConnectionsOut"),
        ("H225-MIB", "callSignalStatsAlertingMsgsIn"),
        ("H225-MIB", "callSignalStatsAlertingMsgsOut"),
        ("H225-MIB", "callSignalStatsCallProceedingsIn"),
        ("H225-MIB", "callSignalStatsCallProceedingsOut"),
        ("H225-MIB", "callSignalStatsSetupMsgsIn"),
        ("H225-MIB", "callSignalStatsSetupMsgsOut"),
        ("H225-MIB", "callSignalStatsSetupAckMsgsIn"),
        ("H225-MIB", "callSignalStatsSetupAckMsgsOut"),
        ("H225-MIB", "callSignalStatsProgressMsgsIn"),
        ("H225-MIB", "callSignalStatsProgressMsgsOut"),
        ("H225-MIB", "callSignalStatsReleaseCompleteMsgsIn"),
        ("H225-MIB", "callSignalStatsReleaseCompleteMsgsOut"),
        ("H225-MIB", "callSignalStatsStatusMsgsIn"),
        ("H225-MIB", "callSignalStatsStatusMsgsOut"),
        ("H225-MIB", "callSignalStatsStatusInquiryMsgsIn"),
        ("H225-MIB", "callSignalStatsStatusInquiryMsgsOut"),
        ("H225-MIB", "callSignalStatsFacilityMsgsIn"),
        ("H225-MIB", "callSignalStatsFacilityMsgsOut"),
        ("H225-MIB", "callSignalStatsInfoMsgsIn"),
        ("H225-MIB", "callSignalStatsInfoMsgsOut"),
        ("H225-MIB", "callSignalStatsNotifyMsgsIn"),
        ("H225-MIB", "callSignalStatsNotifyMsgsOut"),
        ("H225-MIB", "callSignalStatsAverageCallDuration"))
)
if mibBuilder.loadTexts:
    callSignalStatsGroup.setStatus("current")

connectionsGroup = ObjectGroup(
    (0, 0, 8, 341, 1, 1, 1, 5, 1, 3)
)
connectionsGroup.setObjects(
      *(("H225-MIB", "connectionsActiveConnections"),
        ("H225-MIB", "connectionsRole"),
        ("H225-MIB", "connectionsState"),
        ("H225-MIB", "connectionsDestTransporTAddressTag"),
        ("H225-MIB", "connectionsDestTransporTAddress"),
        ("H225-MIB", "connectionsDestAliasTag"),
        ("H225-MIB", "connectionsDestAlias"),
        ("H225-MIB", "connectionsSrcH245SigTransporTAddressTag"),
        ("H225-MIB", "connectionsSrcH245SigTransporTAddress"),
        ("H225-MIB", "connectionsDestH245SigTransporTAddressTag"),
        ("H225-MIB", "connectionsDestH245SigTransporTAddress"),
        ("H225-MIB", "connectionsConfId"),
        ("H225-MIB", "connectionsCalledPartyNumber"),
        ("H225-MIB", "connectionsDestXtraCallingNumber1"),
        ("H225-MIB", "connectionsDestXtraCallingNumber2"),
        ("H225-MIB", "connectionsDestXtraCallingNumber3"),
        ("H225-MIB", "connectionsDestXtraCallingNumber4"),
        ("H225-MIB", "connectionsDestXtraCallingNumber5"),
        ("H225-MIB", "connectionsFastCall"),
        ("H225-MIB", "connectionsSecurity"),
        ("H225-MIB", "connectionsH245Tunneling"),
        ("H225-MIB", "connectionsCanOverlapSend"),
        ("H225-MIB", "connectionsCRV"),
        ("H225-MIB", "connectionsCallType"),
        ("H225-MIB", "connectionsRemoteExtensionAddress"),
        ("H225-MIB", "connectionsExtraCRV1"),
        ("H225-MIB", "connectionsExtraCRV2"),
        ("H225-MIB", "connectionsConnectionStartTime"),
        ("H225-MIB", "connectionsReleaseCompleteReason"))
)
if mibBuilder.loadTexts:
    connectionsGroup.setStatus("current")

callSignalEventsGroup = ObjectGroup(
    (0, 0, 8, 341, 1, 1, 1, 5, 1, 4)
)
callSignalEventsGroup.setObjects(
    ("H225-MIB", "connectionsReleaseCompleteReason")
)
if mibBuilder.loadTexts:
    callSignalEventsGroup.setStatus("current")


# Notification objects

callReleaseComplete = NotificationType(
    (0, 0, 8, 341, 1, 1, 1, 4, 0, 1)
)
callReleaseComplete.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("H225-MIB", "connectionsReleaseCompleteReason"))
)
if mibBuilder.loadTexts:
    callReleaseComplete.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

callSignalingMIBCompliance = ModuleCompliance(
    (0, 0, 8, 341, 1, 1, 1, 5, 2)
)
if mibBuilder.loadTexts:
    callSignalingMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H225-MIB",
    **{"h225CallSignaling": h225CallSignaling,
       "callSignalConfig": callSignalConfig,
       "callSignalConfigTable": callSignalConfigTable,
       "callSignalConfigEntry": callSignalConfigEntry,
       "callSignalConfigMaxConnections": callSignalConfigMaxConnections,
       "callSignalConfigAvailableConnections": callSignalConfigAvailableConnections,
       "callSignalConfigT303": callSignalConfigT303,
       "callSignalConfigT301": callSignalConfigT301,
       "callSignalConfigEnableNotifications": callSignalConfigEnableNotifications,
       "callSignalStats": callSignalStats,
       "callSignalStatsTable": callSignalStatsTable,
       "callSignalStatsEntry": callSignalStatsEntry,
       "callSignalStatsCallConnectionsIn": callSignalStatsCallConnectionsIn,
       "callSignalStatsCallConnectionsOut": callSignalStatsCallConnectionsOut,
       "callSignalStatsAlertingMsgsIn": callSignalStatsAlertingMsgsIn,
       "callSignalStatsAlertingMsgsOut": callSignalStatsAlertingMsgsOut,
       "callSignalStatsCallProceedingsIn": callSignalStatsCallProceedingsIn,
       "callSignalStatsCallProceedingsOut": callSignalStatsCallProceedingsOut,
       "callSignalStatsSetupMsgsIn": callSignalStatsSetupMsgsIn,
       "callSignalStatsSetupMsgsOut": callSignalStatsSetupMsgsOut,
       "callSignalStatsSetupAckMsgsIn": callSignalStatsSetupAckMsgsIn,
       "callSignalStatsSetupAckMsgsOut": callSignalStatsSetupAckMsgsOut,
       "callSignalStatsProgressMsgsIn": callSignalStatsProgressMsgsIn,
       "callSignalStatsProgressMsgsOut": callSignalStatsProgressMsgsOut,
       "callSignalStatsReleaseCompleteMsgsIn": callSignalStatsReleaseCompleteMsgsIn,
       "callSignalStatsReleaseCompleteMsgsOut": callSignalStatsReleaseCompleteMsgsOut,
       "callSignalStatsStatusMsgsIn": callSignalStatsStatusMsgsIn,
       "callSignalStatsStatusMsgsOut": callSignalStatsStatusMsgsOut,
       "callSignalStatsStatusInquiryMsgsIn": callSignalStatsStatusInquiryMsgsIn,
       "callSignalStatsStatusInquiryMsgsOut": callSignalStatsStatusInquiryMsgsOut,
       "callSignalStatsFacilityMsgsIn": callSignalStatsFacilityMsgsIn,
       "callSignalStatsFacilityMsgsOut": callSignalStatsFacilityMsgsOut,
       "callSignalStatsInfoMsgsIn": callSignalStatsInfoMsgsIn,
       "callSignalStatsInfoMsgsOut": callSignalStatsInfoMsgsOut,
       "callSignalStatsNotifyMsgsIn": callSignalStatsNotifyMsgsIn,
       "callSignalStatsNotifyMsgsOut": callSignalStatsNotifyMsgsOut,
       "callSignalStatsAverageCallDuration": callSignalStatsAverageCallDuration,
       "connections": connections,
       "connectionsActiveConnections": connectionsActiveConnections,
       "connectionsTable": connectionsTable,
       "connectionsTableEntry": connectionsTableEntry,
       "connectionsSrcTransporTAddressTag": connectionsSrcTransporTAddressTag,
       "connectionsSrcTransporTAddress": connectionsSrcTransporTAddress,
       "connectionsCallIdentifier": connectionsCallIdentifier,
       "connectionsRole": connectionsRole,
       "connectionsState": connectionsState,
       "connectionsDestTransporTAddressTag": connectionsDestTransporTAddressTag,
       "connectionsDestTransporTAddress": connectionsDestTransporTAddress,
       "connectionsDestAliasTag": connectionsDestAliasTag,
       "connectionsDestAlias": connectionsDestAlias,
       "connectionsSrcH245SigTransporTAddressTag": connectionsSrcH245SigTransporTAddressTag,
       "connectionsSrcH245SigTransporTAddress": connectionsSrcH245SigTransporTAddress,
       "connectionsDestH245SigTransporTAddressTag": connectionsDestH245SigTransporTAddressTag,
       "connectionsDestH245SigTransporTAddress": connectionsDestH245SigTransporTAddress,
       "connectionsConfId": connectionsConfId,
       "connectionsCalledPartyNumber": connectionsCalledPartyNumber,
       "connectionsDestXtraCallingNumber1": connectionsDestXtraCallingNumber1,
       "connectionsDestXtraCallingNumber2": connectionsDestXtraCallingNumber2,
       "connectionsDestXtraCallingNumber3": connectionsDestXtraCallingNumber3,
       "connectionsDestXtraCallingNumber4": connectionsDestXtraCallingNumber4,
       "connectionsDestXtraCallingNumber5": connectionsDestXtraCallingNumber5,
       "connectionsFastCall": connectionsFastCall,
       "connectionsSecurity": connectionsSecurity,
       "connectionsH245Tunneling": connectionsH245Tunneling,
       "connectionsCanOverlapSend": connectionsCanOverlapSend,
       "connectionsCRV": connectionsCRV,
       "connectionsCallType": connectionsCallType,
       "connectionsRemoteExtensionAddress": connectionsRemoteExtensionAddress,
       "connectionsExtraCRV1": connectionsExtraCRV1,
       "connectionsExtraCRV2": connectionsExtraCRV2,
       "connectionsConnectionStartTime": connectionsConnectionStartTime,
       "connectionsEndpointType": connectionsEndpointType,
       "connectionsReleaseCompleteReason": connectionsReleaseCompleteReason,
       "callSignalEvents": callSignalEvents,
       "callReleaseComplete": callReleaseComplete,
       "callSignalingMIBConformance": callSignalingMIBConformance,
       "callSignalingMIBGroups": callSignalingMIBGroups,
       "callSignalConfigGroup": callSignalConfigGroup,
       "callSignalStatsGroup": callSignalStatsGroup,
       "connectionsGroup": connectionsGroup,
       "callSignalEventsGroup": callSignalEventsGroup,
       "callSignalingMIBCompliance": callSignalingMIBCompliance}
)
