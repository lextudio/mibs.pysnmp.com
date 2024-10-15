# SNMP MIB module (JUNIPER-DFC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/JUNIPER-DFC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:12:57 2024
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(jnxDfcNotifications,
 jnxMibs) = mibBuilder.importSymbols(
    "JUNIPER-SMI",
    "jnxDfcNotifications",
    "jnxMibs")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

jnxDfc = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 33)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JnxDfcCSTable_Object = MibTable
jnxDfcCSTable = _JnxDfcCSTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 33, 1)
)
if mibBuilder.loadTexts:
    jnxDfcCSTable.setStatus("current")
_JnxDfcCSEntry_Object = MibTableRow
jnxDfcCSEntry = _JnxDfcCSEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 33, 1, 1)
)
jnxDfcCSEntry.setIndexNames(
    (0, "JUNIPER-DFC-MIB", "jnxDfcGrpName"),
    (0, "JUNIPER-DFC-MIB", "jnxDfcCSId"),
)
if mibBuilder.loadTexts:
    jnxDfcCSEntry.setStatus("current")


class _JnxDfcGrpName_Type(DisplayString):
    """Custom type jnxDfcGrpName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_JnxDfcGrpName_Type.__name__ = "DisplayString"
_JnxDfcGrpName_Object = MibTableColumn
jnxDfcGrpName = _JnxDfcGrpName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 33, 1, 1, 1),
    _JnxDfcGrpName_Type()
)
jnxDfcGrpName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxDfcGrpName.setStatus("current")


class _JnxDfcCSId_Type(DisplayString):
    """Custom type jnxDfcCSId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_JnxDfcCSId_Type.__name__ = "DisplayString"
_JnxDfcCSId_Object = MibTableColumn
jnxDfcCSId = _JnxDfcCSId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 33, 1, 1, 2),
    _JnxDfcCSId_Type()
)
jnxDfcCSId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxDfcCSId.setStatus("current")
_JnxDfcCSControlProtocolAddRequests_Type = Counter64
_JnxDfcCSControlProtocolAddRequests_Object = MibTableColumn
jnxDfcCSControlProtocolAddRequests = _JnxDfcCSControlProtocolAddRequests_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 33, 1, 1, 3),
    _JnxDfcCSControlProtocolAddRequests_Type()
)
jnxDfcCSControlProtocolAddRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxDfcCSControlProtocolAddRequests.setStatus("current")
_JnxDfcCSCriteriaAdded_Type = Counter64
_JnxDfcCSCriteriaAdded_Object = MibTableColumn
jnxDfcCSCriteriaAdded = _JnxDfcCSCriteriaAdded_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 33, 1, 1, 4),
    _JnxDfcCSCriteriaAdded_Type()
)
jnxDfcCSCriteriaAdded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxDfcCSCriteriaAdded.setStatus("current")
_JnxDfcCSCriteriaAdditionFailed_Type = Counter64
_JnxDfcCSCriteriaAdditionFailed_Object = MibTableColumn
jnxDfcCSCriteriaAdditionFailed = _JnxDfcCSCriteriaAdditionFailed_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 33, 1, 1, 5),
    _JnxDfcCSCriteriaAdditionFailed_Type()
)
jnxDfcCSCriteriaAdditionFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxDfcCSCriteriaAdditionFailed.setStatus("current")
_JnxDfcCSControlProtocolDeleteRequests_Type = Counter64
_JnxDfcCSControlProtocolDeleteRequests_Object = MibTableColumn
jnxDfcCSControlProtocolDeleteRequests = _JnxDfcCSControlProtocolDeleteRequests_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 33, 1, 1, 6),
    _JnxDfcCSControlProtocolDeleteRequests_Type()
)
jnxDfcCSControlProtocolDeleteRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxDfcCSControlProtocolDeleteRequests.setStatus("current")
_JnxDfcCSCriteriaDeleted_Type = Counter64
_JnxDfcCSCriteriaDeleted_Object = MibTableColumn
jnxDfcCSCriteriaDeleted = _JnxDfcCSCriteriaDeleted_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 33, 1, 1, 7),
    _JnxDfcCSCriteriaDeleted_Type()
)
jnxDfcCSCriteriaDeleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxDfcCSCriteriaDeleted.setStatus("current")
_JnxDfcCSCriteriaDeletionFailed_Type = Counter64
_JnxDfcCSCriteriaDeletionFailed_Object = MibTableColumn
jnxDfcCSCriteriaDeletionFailed = _JnxDfcCSCriteriaDeletionFailed_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 33, 1, 1, 8),
    _JnxDfcCSCriteriaDeletionFailed_Type()
)
jnxDfcCSCriteriaDeletionFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxDfcCSCriteriaDeletionFailed.setStatus("current")
_JnxDfcCSCriteriaDeletedTimeoutIdle_Type = Counter64
_JnxDfcCSCriteriaDeletedTimeoutIdle_Object = MibTableColumn
jnxDfcCSCriteriaDeletedTimeoutIdle = _JnxDfcCSCriteriaDeletedTimeoutIdle_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 33, 1, 1, 9),
    _JnxDfcCSCriteriaDeletedTimeoutIdle_Type()
)
jnxDfcCSCriteriaDeletedTimeoutIdle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxDfcCSCriteriaDeletedTimeoutIdle.setStatus("current")
_JnxDfcCSCriteriaDeletedTimeoutTotal_Type = Counter64
_JnxDfcCSCriteriaDeletedTimeoutTotal_Object = MibTableColumn
jnxDfcCSCriteriaDeletedTimeoutTotal = _JnxDfcCSCriteriaDeletedTimeoutTotal_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 33, 1, 1, 10),
    _JnxDfcCSCriteriaDeletedTimeoutTotal_Type()
)
jnxDfcCSCriteriaDeletedTimeoutTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxDfcCSCriteriaDeletedTimeoutTotal.setStatus("current")
_JnxDfcCSCriteriaDeletedPackets_Type = Counter64
_JnxDfcCSCriteriaDeletedPackets_Object = MibTableColumn
jnxDfcCSCriteriaDeletedPackets = _JnxDfcCSCriteriaDeletedPackets_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 33, 1, 1, 11),
    _JnxDfcCSCriteriaDeletedPackets_Type()
)
jnxDfcCSCriteriaDeletedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxDfcCSCriteriaDeletedPackets.setStatus("current")
_JnxDfcCSCriteriaDeletedBytes_Type = Counter64
_JnxDfcCSCriteriaDeletedBytes_Object = MibTableColumn
jnxDfcCSCriteriaDeletedBytes = _JnxDfcCSCriteriaDeletedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 33, 1, 1, 12),
    _JnxDfcCSCriteriaDeletedBytes_Type()
)
jnxDfcCSCriteriaDeletedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxDfcCSCriteriaDeletedBytes.setStatus("current")
_JnxDfcCSControlProtocolRefreshRequests_Type = Counter64
_JnxDfcCSControlProtocolRefreshRequests_Object = MibTableColumn
jnxDfcCSControlProtocolRefreshRequests = _JnxDfcCSControlProtocolRefreshRequests_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 33, 1, 1, 13),
    _JnxDfcCSControlProtocolRefreshRequests_Type()
)
jnxDfcCSControlProtocolRefreshRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxDfcCSControlProtocolRefreshRequests.setStatus("current")
_JnxDfcCSCriteriaRefreshed_Type = Counter64
_JnxDfcCSCriteriaRefreshed_Object = MibTableColumn
jnxDfcCSCriteriaRefreshed = _JnxDfcCSCriteriaRefreshed_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 33, 1, 1, 14),
    _JnxDfcCSCriteriaRefreshed_Type()
)
jnxDfcCSCriteriaRefreshed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxDfcCSCriteriaRefreshed.setStatus("current")
_JnxDfcCSCriteriaRefreshFailed_Type = Counter64
_JnxDfcCSCriteriaRefreshFailed_Object = MibTableColumn
jnxDfcCSCriteriaRefreshFailed = _JnxDfcCSCriteriaRefreshFailed_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 33, 1, 1, 15),
    _JnxDfcCSCriteriaRefreshFailed_Type()
)
jnxDfcCSCriteriaRefreshFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxDfcCSCriteriaRefreshFailed.setStatus("current")
_JnxDfcCSControlProtocolListRequests_Type = Counter64
_JnxDfcCSControlProtocolListRequests_Object = MibTableColumn
jnxDfcCSControlProtocolListRequests = _JnxDfcCSControlProtocolListRequests_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 33, 1, 1, 16),
    _JnxDfcCSControlProtocolListRequests_Type()
)
jnxDfcCSControlProtocolListRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxDfcCSControlProtocolListRequests.setStatus("current")
_JnxDfcCSListSuccess_Type = Counter64
_JnxDfcCSListSuccess_Object = MibTableColumn
jnxDfcCSListSuccess = _JnxDfcCSListSuccess_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 33, 1, 1, 17),
    _JnxDfcCSListSuccess_Type()
)
jnxDfcCSListSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxDfcCSListSuccess.setStatus("current")
_JnxDfcCSListFailed_Type = Counter64
_JnxDfcCSListFailed_Object = MibTableColumn
jnxDfcCSListFailed = _JnxDfcCSListFailed_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 33, 1, 1, 18),
    _JnxDfcCSListFailed_Type()
)
jnxDfcCSListFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxDfcCSListFailed.setStatus("current")
_JnxDfcCSControlProtocolNoopRequests_Type = Counter64
_JnxDfcCSControlProtocolNoopRequests_Object = MibTableColumn
jnxDfcCSControlProtocolNoopRequests = _JnxDfcCSControlProtocolNoopRequests_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 33, 1, 1, 19),
    _JnxDfcCSControlProtocolNoopRequests_Type()
)
jnxDfcCSControlProtocolNoopRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxDfcCSControlProtocolNoopRequests.setStatus("current")
_JnxDfcCSNoopSuccess_Type = Counter64
_JnxDfcCSNoopSuccess_Object = MibTableColumn
jnxDfcCSNoopSuccess = _JnxDfcCSNoopSuccess_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 33, 1, 1, 20),
    _JnxDfcCSNoopSuccess_Type()
)
jnxDfcCSNoopSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxDfcCSNoopSuccess.setStatus("current")
_JnxDfcCSNoopFailed_Type = Counter64
_JnxDfcCSNoopFailed_Object = MibTableColumn
jnxDfcCSNoopFailed = _JnxDfcCSNoopFailed_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 33, 1, 1, 21),
    _JnxDfcCSNoopFailed_Type()
)
jnxDfcCSNoopFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxDfcCSNoopFailed.setStatus("current")
_JnxDfcCSDynamicCriteriaActive_Type = Counter64
_JnxDfcCSDynamicCriteriaActive_Object = MibTableColumn
jnxDfcCSDynamicCriteriaActive = _JnxDfcCSDynamicCriteriaActive_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 33, 1, 1, 22),
    _JnxDfcCSDynamicCriteriaActive_Type()
)
jnxDfcCSDynamicCriteriaActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxDfcCSDynamicCriteriaActive.setStatus("current")
_JnxDfcCSStaticCriteriaActive_Type = Counter64
_JnxDfcCSStaticCriteriaActive_Object = MibTableColumn
jnxDfcCSStaticCriteriaActive = _JnxDfcCSStaticCriteriaActive_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 33, 1, 1, 23),
    _JnxDfcCSStaticCriteriaActive_Type()
)
jnxDfcCSStaticCriteriaActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxDfcCSStaticCriteriaActive.setStatus("current")
_JnxDfcCSBadRequest_Type = Counter64
_JnxDfcCSBadRequest_Object = MibTableColumn
jnxDfcCSBadRequest = _JnxDfcCSBadRequest_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 33, 1, 1, 24),
    _JnxDfcCSBadRequest_Type()
)
jnxDfcCSBadRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxDfcCSBadRequest.setStatus("current")
_JnxDfcCSResponseSuccessful_Type = Counter64
_JnxDfcCSResponseSuccessful_Object = MibTableColumn
jnxDfcCSResponseSuccessful = _JnxDfcCSResponseSuccessful_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 33, 1, 1, 25),
    _JnxDfcCSResponseSuccessful_Type()
)
jnxDfcCSResponseSuccessful.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxDfcCSResponseSuccessful.setStatus("current")
_JnxDfcCSResponseImproperCriteria_Type = Counter64
_JnxDfcCSResponseImproperCriteria_Object = MibTableColumn
jnxDfcCSResponseImproperCriteria = _JnxDfcCSResponseImproperCriteria_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 33, 1, 1, 26),
    _JnxDfcCSResponseImproperCriteria_Type()
)
jnxDfcCSResponseImproperCriteria.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxDfcCSResponseImproperCriteria.setStatus("current")
_JnxDfcCSResponseUnknownContentDest_Type = Counter64
_JnxDfcCSResponseUnknownContentDest_Object = MibTableColumn
jnxDfcCSResponseUnknownContentDest = _JnxDfcCSResponseUnknownContentDest_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 33, 1, 1, 27),
    _JnxDfcCSResponseUnknownContentDest_Type()
)
jnxDfcCSResponseUnknownContentDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxDfcCSResponseUnknownContentDest.setStatus("current")
_JnxDfcCSResponseUnknownCriteriaId_Type = Counter64
_JnxDfcCSResponseUnknownCriteriaId_Object = MibTableColumn
jnxDfcCSResponseUnknownCriteriaId = _JnxDfcCSResponseUnknownCriteriaId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 33, 1, 1, 28),
    _JnxDfcCSResponseUnknownCriteriaId_Type()
)
jnxDfcCSResponseUnknownCriteriaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxDfcCSResponseUnknownCriteriaId.setStatus("current")
_JnxDfcCSResponseImproperTimeout_Type = Counter64
_JnxDfcCSResponseImproperTimeout_Object = MibTableColumn
jnxDfcCSResponseImproperTimeout = _JnxDfcCSResponseImproperTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 33, 1, 1, 29),
    _JnxDfcCSResponseImproperTimeout_Type()
)
jnxDfcCSResponseImproperTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxDfcCSResponseImproperTimeout.setStatus("current")
_JnxDfcCSResponseInvalidAuthentication_Type = Counter64
_JnxDfcCSResponseInvalidAuthentication_Object = MibTableColumn
jnxDfcCSResponseInvalidAuthentication = _JnxDfcCSResponseInvalidAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 33, 1, 1, 30),
    _JnxDfcCSResponseInvalidAuthentication_Type()
)
jnxDfcCSResponseInvalidAuthentication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxDfcCSResponseInvalidAuthentication.setStatus("current")
_JnxDfcCSResponseInvalidSequenceNumber_Type = Counter64
_JnxDfcCSResponseInvalidSequenceNumber_Object = MibTableColumn
jnxDfcCSResponseInvalidSequenceNumber = _JnxDfcCSResponseInvalidSequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 33, 1, 1, 31),
    _JnxDfcCSResponseInvalidSequenceNumber_Type()
)
jnxDfcCSResponseInvalidSequenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxDfcCSResponseInvalidSequenceNumber.setStatus("current")
_JnxDfcCSResponseInternalError_Type = Counter64
_JnxDfcCSResponseInternalError_Object = MibTableColumn
jnxDfcCSResponseInternalError = _JnxDfcCSResponseInternalError_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 33, 1, 1, 32),
    _JnxDfcCSResponseInternalError_Type()
)
jnxDfcCSResponseInternalError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxDfcCSResponseInternalError.setStatus("current")
_JnxDfcCSNotificationRestart_Type = Counter64
_JnxDfcCSNotificationRestart_Object = MibTableColumn
jnxDfcCSNotificationRestart = _JnxDfcCSNotificationRestart_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 33, 1, 1, 33),
    _JnxDfcCSNotificationRestart_Type()
)
jnxDfcCSNotificationRestart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxDfcCSNotificationRestart.setStatus("current")
_JnxDfcCSNotificationRollover_Type = Counter64
_JnxDfcCSNotificationRollover_Object = MibTableColumn
jnxDfcCSNotificationRollover = _JnxDfcCSNotificationRollover_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 33, 1, 1, 34),
    _JnxDfcCSNotificationRollover_Type()
)
jnxDfcCSNotificationRollover.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxDfcCSNotificationRollover.setStatus("current")
_JnxDfcCSNotificationNoop_Type = Counter64
_JnxDfcCSNotificationNoop_Object = MibTableColumn
jnxDfcCSNotificationNoop = _JnxDfcCSNotificationNoop_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 33, 1, 1, 35),
    _JnxDfcCSNotificationNoop_Type()
)
jnxDfcCSNotificationNoop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxDfcCSNotificationNoop.setStatus("current")
_JnxDfcCSNotificationTimeout_Type = Counter64
_JnxDfcCSNotificationTimeout_Object = MibTableColumn
jnxDfcCSNotificationTimeout = _JnxDfcCSNotificationTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 33, 1, 1, 36),
    _JnxDfcCSNotificationTimeout_Type()
)
jnxDfcCSNotificationTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxDfcCSNotificationTimeout.setStatus("current")
_JnxDfcCSNotificationCongestion_Type = Counter64
_JnxDfcCSNotificationCongestion_Object = MibTableColumn
jnxDfcCSNotificationCongestion = _JnxDfcCSNotificationCongestion_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 33, 1, 1, 37),
    _JnxDfcCSNotificationCongestion_Type()
)
jnxDfcCSNotificationCongestion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxDfcCSNotificationCongestion.setStatus("current")
_JnxDfcCSNotificationCongestionDelete_Type = Counter64
_JnxDfcCSNotificationCongestionDelete_Object = MibTableColumn
jnxDfcCSNotificationCongestionDelete = _JnxDfcCSNotificationCongestionDelete_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 33, 1, 1, 38),
    _JnxDfcCSNotificationCongestionDelete_Type()
)
jnxDfcCSNotificationCongestionDelete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxDfcCSNotificationCongestionDelete.setStatus("current")
_JnxDfcCSNotificationDuplicatesDropped_Type = Counter64
_JnxDfcCSNotificationDuplicatesDropped_Object = MibTableColumn
jnxDfcCSNotificationDuplicatesDropped = _JnxDfcCSNotificationDuplicatesDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 33, 1, 1, 39),
    _JnxDfcCSNotificationDuplicatesDropped_Type()
)
jnxDfcCSNotificationDuplicatesDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxDfcCSNotificationDuplicatesDropped.setStatus("current")
_JnxDfcCSAddRequestRate_Type = Counter64
_JnxDfcCSAddRequestRate_Object = MibTableColumn
jnxDfcCSAddRequestRate = _JnxDfcCSAddRequestRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 33, 1, 1, 40),
    _JnxDfcCSAddRequestRate_Type()
)
jnxDfcCSAddRequestRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxDfcCSAddRequestRate.setStatus("current")
_JnxDfcCSAddRequestPeakRate_Type = Counter64
_JnxDfcCSAddRequestPeakRate_Object = MibTableColumn
jnxDfcCSAddRequestPeakRate = _JnxDfcCSAddRequestPeakRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 33, 1, 1, 41),
    _JnxDfcCSAddRequestPeakRate_Type()
)
jnxDfcCSAddRequestPeakRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxDfcCSAddRequestPeakRate.setStatus("current")
_JnxDfcCSAggrCriteriaBandwidth_Type = Counter64
_JnxDfcCSAggrCriteriaBandwidth_Object = MibTableColumn
jnxDfcCSAggrCriteriaBandwidth = _JnxDfcCSAggrCriteriaBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 33, 1, 1, 42),
    _JnxDfcCSAggrCriteriaBandwidth_Type()
)
jnxDfcCSAggrCriteriaBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxDfcCSAggrCriteriaBandwidth.setStatus("current")
_JnxDfcCSSequenceNumber_Type = Counter64
_JnxDfcCSSequenceNumber_Object = MibTableColumn
jnxDfcCSSequenceNumber = _JnxDfcCSSequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 33, 1, 1, 43),
    _JnxDfcCSSequenceNumber_Type()
)
jnxDfcCSSequenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxDfcCSSequenceNumber.setStatus("current")
_JnxDfcCDTable_Object = MibTable
jnxDfcCDTable = _JnxDfcCDTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 33, 2)
)
if mibBuilder.loadTexts:
    jnxDfcCDTable.setStatus("current")
_JnxDfcCDEntry_Object = MibTableRow
jnxDfcCDEntry = _JnxDfcCDEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 33, 2, 1)
)
jnxDfcCDEntry.setIndexNames(
    (0, "JUNIPER-DFC-MIB", "jnxDfcGrpName"),
    (0, "JUNIPER-DFC-MIB", "jnxDfcCDId"),
)
if mibBuilder.loadTexts:
    jnxDfcCDEntry.setStatus("current")


class _JnxDfcCDId_Type(DisplayString):
    """Custom type jnxDfcCDId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_JnxDfcCDId_Type.__name__ = "DisplayString"
_JnxDfcCDId_Object = MibTableColumn
jnxDfcCDId = _JnxDfcCDId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 33, 2, 1, 1),
    _JnxDfcCDId_Type()
)
jnxDfcCDId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxDfcCDId.setStatus("current")
_JnxDfcCDCriteria_Type = Counter64
_JnxDfcCDCriteria_Object = MibTableColumn
jnxDfcCDCriteria = _JnxDfcCDCriteria_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 33, 2, 1, 2),
    _JnxDfcCDCriteria_Type()
)
jnxDfcCDCriteria.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxDfcCDCriteria.setStatus("current")
_JnxDfcCDByteRate_Type = Counter64
_JnxDfcCDByteRate_Object = MibTableColumn
jnxDfcCDByteRate = _JnxDfcCDByteRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 33, 2, 1, 3),
    _JnxDfcCDByteRate_Type()
)
jnxDfcCDByteRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxDfcCDByteRate.setStatus("current")
_JnxDfcCDMatchedPackets_Type = Counter64
_JnxDfcCDMatchedPackets_Object = MibTableColumn
jnxDfcCDMatchedPackets = _JnxDfcCDMatchedPackets_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 33, 2, 1, 4),
    _JnxDfcCDMatchedPackets_Type()
)
jnxDfcCDMatchedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxDfcCDMatchedPackets.setStatus("current")
_JnxDfcCDMatchedBytes_Type = Counter64
_JnxDfcCDMatchedBytes_Object = MibTableColumn
jnxDfcCDMatchedBytes = _JnxDfcCDMatchedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 33, 2, 1, 5),
    _JnxDfcCDMatchedBytes_Type()
)
jnxDfcCDMatchedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxDfcCDMatchedBytes.setStatus("current")
_JnxDfcCDCongestionNotification_Type = Counter64
_JnxDfcCDCongestionNotification_Object = MibTableColumn
jnxDfcCDCongestionNotification = _JnxDfcCDCongestionNotification_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 33, 2, 1, 6),
    _JnxDfcCDCongestionNotification_Type()
)
jnxDfcCDCongestionNotification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxDfcCDCongestionNotification.setStatus("current")
_JnxDfcNotifyVars_ObjectIdentity = ObjectIdentity
jnxDfcNotifyVars = _JnxDfcNotifyVars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 33, 3)
)
if mibBuilder.loadTexts:
    jnxDfcNotifyVars.setStatus("current")
_JnxDfcInterfaceName_Type = DisplayString
_JnxDfcInterfaceName_Object = MibScalar
jnxDfcInterfaceName = _JnxDfcInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 33, 3, 1),
    _JnxDfcInterfaceName_Type()
)
jnxDfcInterfaceName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxDfcInterfaceName.setStatus("current")
_JnxDfcInputPktRate_Type = Unsigned32
_JnxDfcInputPktRate_Object = MibScalar
jnxDfcInputPktRate = _JnxDfcInputPktRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 33, 3, 2),
    _JnxDfcInputPktRate_Type()
)
jnxDfcInputPktRate.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxDfcInputPktRate.setStatus("current")
_JnxDfcPpsSoftOverloadLowWatermark_Type = Unsigned32
_JnxDfcPpsSoftOverloadLowWatermark_Object = MibScalar
jnxDfcPpsSoftOverloadLowWatermark = _JnxDfcPpsSoftOverloadLowWatermark_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 33, 3, 3),
    _JnxDfcPpsSoftOverloadLowWatermark_Type()
)
jnxDfcPpsSoftOverloadLowWatermark.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxDfcPpsSoftOverloadLowWatermark.setStatus("current")
_JnxDfcPpsSoftOverloadHighWatermark_Type = Unsigned32
_JnxDfcPpsSoftOverloadHighWatermark_Object = MibScalar
jnxDfcPpsSoftOverloadHighWatermark = _JnxDfcPpsSoftOverloadHighWatermark_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 33, 3, 4),
    _JnxDfcPpsSoftOverloadHighWatermark_Type()
)
jnxDfcPpsSoftOverloadHighWatermark.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxDfcPpsSoftOverloadHighWatermark.setStatus("current")
_JnxDfcPpsHardOverloadLowWatermark_Type = Unsigned32
_JnxDfcPpsHardOverloadLowWatermark_Object = MibScalar
jnxDfcPpsHardOverloadLowWatermark = _JnxDfcPpsHardOverloadLowWatermark_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 33, 3, 5),
    _JnxDfcPpsHardOverloadLowWatermark_Type()
)
jnxDfcPpsHardOverloadLowWatermark.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxDfcPpsHardOverloadLowWatermark.setStatus("current")
_JnxDfcPpsHardOverloadHighWatermark_Type = Unsigned32
_JnxDfcPpsHardOverloadHighWatermark_Object = MibScalar
jnxDfcPpsHardOverloadHighWatermark = _JnxDfcPpsHardOverloadHighWatermark_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 33, 3, 6),
    _JnxDfcPpsHardOverloadHighWatermark_Type()
)
jnxDfcPpsHardOverloadHighWatermark.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxDfcPpsHardOverloadHighWatermark.setStatus("current")
_JnxDfcFlowsUsage_Type = Unsigned32
_JnxDfcFlowsUsage_Object = MibScalar
jnxDfcFlowsUsage = _JnxDfcFlowsUsage_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 33, 3, 7),
    _JnxDfcFlowsUsage_Type()
)
jnxDfcFlowsUsage.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxDfcFlowsUsage.setStatus("current")
if mibBuilder.loadTexts:
    jnxDfcFlowsUsage.setUnits("percent")
_JnxDfcCriteriaUsage_Type = Unsigned32
_JnxDfcCriteriaUsage_Object = MibScalar
jnxDfcCriteriaUsage = _JnxDfcCriteriaUsage_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 33, 3, 8),
    _JnxDfcCriteriaUsage_Type()
)
jnxDfcCriteriaUsage.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxDfcCriteriaUsage.setStatus("current")
if mibBuilder.loadTexts:
    jnxDfcCriteriaUsage.setUnits("percent")
_JnxDfcMemSoftOverloadLowWatermark_Type = Unsigned32
_JnxDfcMemSoftOverloadLowWatermark_Object = MibScalar
jnxDfcMemSoftOverloadLowWatermark = _JnxDfcMemSoftOverloadLowWatermark_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 33, 3, 9),
    _JnxDfcMemSoftOverloadLowWatermark_Type()
)
jnxDfcMemSoftOverloadLowWatermark.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxDfcMemSoftOverloadLowWatermark.setStatus("current")
if mibBuilder.loadTexts:
    jnxDfcMemSoftOverloadLowWatermark.setUnits("percent")
_JnxDfcMemSoftOverloadHighWatermark_Type = Unsigned32
_JnxDfcMemSoftOverloadHighWatermark_Object = MibScalar
jnxDfcMemSoftOverloadHighWatermark = _JnxDfcMemSoftOverloadHighWatermark_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 33, 3, 10),
    _JnxDfcMemSoftOverloadHighWatermark_Type()
)
jnxDfcMemSoftOverloadHighWatermark.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxDfcMemSoftOverloadHighWatermark.setStatus("current")
if mibBuilder.loadTexts:
    jnxDfcMemSoftOverloadHighWatermark.setUnits("percent")
_JnxDfcFlowLowWatermark_Type = Unsigned32
_JnxDfcFlowLowWatermark_Object = MibScalar
jnxDfcFlowLowWatermark = _JnxDfcFlowLowWatermark_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 33, 3, 11),
    _JnxDfcFlowLowWatermark_Type()
)
jnxDfcFlowLowWatermark.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxDfcFlowLowWatermark.setStatus("current")
_JnxDfcFlowHighWatermark_Type = Unsigned32
_JnxDfcFlowHighWatermark_Object = MibScalar
jnxDfcFlowHighWatermark = _JnxDfcFlowHighWatermark_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 33, 3, 12),
    _JnxDfcFlowHighWatermark_Type()
)
jnxDfcFlowHighWatermark.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxDfcFlowHighWatermark.setStatus("current")
_JnxDfcCriteriaLowWatermark_Type = Unsigned32
_JnxDfcCriteriaLowWatermark_Object = MibScalar
jnxDfcCriteriaLowWatermark = _JnxDfcCriteriaLowWatermark_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 33, 3, 13),
    _JnxDfcCriteriaLowWatermark_Type()
)
jnxDfcCriteriaLowWatermark.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxDfcCriteriaLowWatermark.setStatus("current")
_JnxDfcCriteriaHighWatermark_Type = Unsigned32
_JnxDfcCriteriaHighWatermark_Object = MibScalar
jnxDfcCriteriaHighWatermark = _JnxDfcCriteriaHighWatermark_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 33, 3, 14),
    _JnxDfcCriteriaHighWatermark_Type()
)
jnxDfcCriteriaHighWatermark.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxDfcCriteriaHighWatermark.setStatus("current")
_JnxDfcNotificationPrefix_ObjectIdentity = ObjectIdentity
jnxDfcNotificationPrefix = _JnxDfcNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 4, 11, 0)
)
if mibBuilder.loadTexts:
    jnxDfcNotificationPrefix.setStatus("current")

# Managed Objects groups


# Notification objects

jnxDfcSoftPpsThresholdExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 11, 0, 1)
)
jnxDfcSoftPpsThresholdExceeded.setObjects(
      *(("JUNIPER-DFC-MIB", "jnxDfcInterfaceName"),
        ("JUNIPER-DFC-MIB", "jnxDfcInputPktRate"),
        ("JUNIPER-DFC-MIB", "jnxDfcPpsSoftOverloadLowWatermark"),
        ("JUNIPER-DFC-MIB", "jnxDfcPpsSoftOverloadHighWatermark"))
)
if mibBuilder.loadTexts:
    jnxDfcSoftPpsThresholdExceeded.setStatus(
        "current"
    )

jnxDfcSoftPpsUnderThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 11, 0, 2)
)
jnxDfcSoftPpsUnderThreshold.setObjects(
      *(("JUNIPER-DFC-MIB", "jnxDfcInterfaceName"),
        ("JUNIPER-DFC-MIB", "jnxDfcInputPktRate"),
        ("JUNIPER-DFC-MIB", "jnxDfcPpsSoftOverloadLowWatermark"),
        ("JUNIPER-DFC-MIB", "jnxDfcPpsSoftOverloadHighWatermark"))
)
if mibBuilder.loadTexts:
    jnxDfcSoftPpsUnderThreshold.setStatus(
        "current"
    )

jnxDfcHardPpsThresholdExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 11, 0, 3)
)
jnxDfcHardPpsThresholdExceeded.setObjects(
      *(("JUNIPER-DFC-MIB", "jnxDfcInterfaceName"),
        ("JUNIPER-DFC-MIB", "jnxDfcInputPktRate"),
        ("JUNIPER-DFC-MIB", "jnxDfcPpsHardOverloadLowWatermark"),
        ("JUNIPER-DFC-MIB", "jnxDfcPpsHardOverloadHighWatermark"))
)
if mibBuilder.loadTexts:
    jnxDfcHardPpsThresholdExceeded.setStatus(
        "current"
    )

jnxDfcHardPpsUnderThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 11, 0, 4)
)
jnxDfcHardPpsUnderThreshold.setObjects(
      *(("JUNIPER-DFC-MIB", "jnxDfcInterfaceName"),
        ("JUNIPER-DFC-MIB", "jnxDfcInputPktRate"),
        ("JUNIPER-DFC-MIB", "jnxDfcPpsHardOverloadLowWatermark"),
        ("JUNIPER-DFC-MIB", "jnxDfcPpsHardOverloadHighWatermark"))
)
if mibBuilder.loadTexts:
    jnxDfcHardPpsUnderThreshold.setStatus(
        "current"
    )

jnxDfcSoftMemThresholdExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 11, 0, 5)
)
jnxDfcSoftMemThresholdExceeded.setObjects(
      *(("JUNIPER-DFC-MIB", "jnxDfcInterfaceName"),
        ("JUNIPER-DFC-MIB", "jnxDfcFlowsUsage"),
        ("JUNIPER-DFC-MIB", "jnxDfcCriteriaUsage"),
        ("JUNIPER-DFC-MIB", "jnxDfcMemSoftOverloadLowWatermark"),
        ("JUNIPER-DFC-MIB", "jnxDfcMemSoftOverloadHighWatermark"))
)
if mibBuilder.loadTexts:
    jnxDfcSoftMemThresholdExceeded.setStatus(
        "current"
    )

jnxDfcSoftMemUnderThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 11, 0, 6)
)
jnxDfcSoftMemUnderThreshold.setObjects(
      *(("JUNIPER-DFC-MIB", "jnxDfcInterfaceName"),
        ("JUNIPER-DFC-MIB", "jnxDfcFlowsUsage"),
        ("JUNIPER-DFC-MIB", "jnxDfcCriteriaUsage"),
        ("JUNIPER-DFC-MIB", "jnxDfcMemSoftOverloadLowWatermark"),
        ("JUNIPER-DFC-MIB", "jnxDfcMemSoftOverloadHighWatermark"))
)
if mibBuilder.loadTexts:
    jnxDfcSoftMemUnderThreshold.setStatus(
        "current"
    )

jnxDfcHardMemThresholdExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 11, 0, 7)
)
jnxDfcHardMemThresholdExceeded.setObjects(
      *(("JUNIPER-DFC-MIB", "jnxDfcInterfaceName"),
        ("JUNIPER-DFC-MIB", "jnxDfcFlowsUsage"),
        ("JUNIPER-DFC-MIB", "jnxDfcFlowLowWatermark"),
        ("JUNIPER-DFC-MIB", "jnxDfcFlowHighWatermark"),
        ("JUNIPER-DFC-MIB", "jnxDfcCriteriaUsage"),
        ("JUNIPER-DFC-MIB", "jnxDfcCriteriaLowWatermark"),
        ("JUNIPER-DFC-MIB", "jnxDfcCriteriaHighWatermark"))
)
if mibBuilder.loadTexts:
    jnxDfcHardMemThresholdExceeded.setStatus(
        "current"
    )

jnxDfcHardMemUnderThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 11, 0, 8)
)
jnxDfcHardMemUnderThreshold.setObjects(
      *(("JUNIPER-DFC-MIB", "jnxDfcInterfaceName"),
        ("JUNIPER-DFC-MIB", "jnxDfcFlowsUsage"),
        ("JUNIPER-DFC-MIB", "jnxDfcFlowLowWatermark"),
        ("JUNIPER-DFC-MIB", "jnxDfcFlowHighWatermark"),
        ("JUNIPER-DFC-MIB", "jnxDfcCriteriaUsage"),
        ("JUNIPER-DFC-MIB", "jnxDfcCriteriaLowWatermark"),
        ("JUNIPER-DFC-MIB", "jnxDfcCriteriaHighWatermark"))
)
if mibBuilder.loadTexts:
    jnxDfcHardMemUnderThreshold.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-DFC-MIB",
    **{"jnxDfc": jnxDfc,
       "jnxDfcCSTable": jnxDfcCSTable,
       "jnxDfcCSEntry": jnxDfcCSEntry,
       "jnxDfcGrpName": jnxDfcGrpName,
       "jnxDfcCSId": jnxDfcCSId,
       "jnxDfcCSControlProtocolAddRequests": jnxDfcCSControlProtocolAddRequests,
       "jnxDfcCSCriteriaAdded": jnxDfcCSCriteriaAdded,
       "jnxDfcCSCriteriaAdditionFailed": jnxDfcCSCriteriaAdditionFailed,
       "jnxDfcCSControlProtocolDeleteRequests": jnxDfcCSControlProtocolDeleteRequests,
       "jnxDfcCSCriteriaDeleted": jnxDfcCSCriteriaDeleted,
       "jnxDfcCSCriteriaDeletionFailed": jnxDfcCSCriteriaDeletionFailed,
       "jnxDfcCSCriteriaDeletedTimeoutIdle": jnxDfcCSCriteriaDeletedTimeoutIdle,
       "jnxDfcCSCriteriaDeletedTimeoutTotal": jnxDfcCSCriteriaDeletedTimeoutTotal,
       "jnxDfcCSCriteriaDeletedPackets": jnxDfcCSCriteriaDeletedPackets,
       "jnxDfcCSCriteriaDeletedBytes": jnxDfcCSCriteriaDeletedBytes,
       "jnxDfcCSControlProtocolRefreshRequests": jnxDfcCSControlProtocolRefreshRequests,
       "jnxDfcCSCriteriaRefreshed": jnxDfcCSCriteriaRefreshed,
       "jnxDfcCSCriteriaRefreshFailed": jnxDfcCSCriteriaRefreshFailed,
       "jnxDfcCSControlProtocolListRequests": jnxDfcCSControlProtocolListRequests,
       "jnxDfcCSListSuccess": jnxDfcCSListSuccess,
       "jnxDfcCSListFailed": jnxDfcCSListFailed,
       "jnxDfcCSControlProtocolNoopRequests": jnxDfcCSControlProtocolNoopRequests,
       "jnxDfcCSNoopSuccess": jnxDfcCSNoopSuccess,
       "jnxDfcCSNoopFailed": jnxDfcCSNoopFailed,
       "jnxDfcCSDynamicCriteriaActive": jnxDfcCSDynamicCriteriaActive,
       "jnxDfcCSStaticCriteriaActive": jnxDfcCSStaticCriteriaActive,
       "jnxDfcCSBadRequest": jnxDfcCSBadRequest,
       "jnxDfcCSResponseSuccessful": jnxDfcCSResponseSuccessful,
       "jnxDfcCSResponseImproperCriteria": jnxDfcCSResponseImproperCriteria,
       "jnxDfcCSResponseUnknownContentDest": jnxDfcCSResponseUnknownContentDest,
       "jnxDfcCSResponseUnknownCriteriaId": jnxDfcCSResponseUnknownCriteriaId,
       "jnxDfcCSResponseImproperTimeout": jnxDfcCSResponseImproperTimeout,
       "jnxDfcCSResponseInvalidAuthentication": jnxDfcCSResponseInvalidAuthentication,
       "jnxDfcCSResponseInvalidSequenceNumber": jnxDfcCSResponseInvalidSequenceNumber,
       "jnxDfcCSResponseInternalError": jnxDfcCSResponseInternalError,
       "jnxDfcCSNotificationRestart": jnxDfcCSNotificationRestart,
       "jnxDfcCSNotificationRollover": jnxDfcCSNotificationRollover,
       "jnxDfcCSNotificationNoop": jnxDfcCSNotificationNoop,
       "jnxDfcCSNotificationTimeout": jnxDfcCSNotificationTimeout,
       "jnxDfcCSNotificationCongestion": jnxDfcCSNotificationCongestion,
       "jnxDfcCSNotificationCongestionDelete": jnxDfcCSNotificationCongestionDelete,
       "jnxDfcCSNotificationDuplicatesDropped": jnxDfcCSNotificationDuplicatesDropped,
       "jnxDfcCSAddRequestRate": jnxDfcCSAddRequestRate,
       "jnxDfcCSAddRequestPeakRate": jnxDfcCSAddRequestPeakRate,
       "jnxDfcCSAggrCriteriaBandwidth": jnxDfcCSAggrCriteriaBandwidth,
       "jnxDfcCSSequenceNumber": jnxDfcCSSequenceNumber,
       "jnxDfcCDTable": jnxDfcCDTable,
       "jnxDfcCDEntry": jnxDfcCDEntry,
       "jnxDfcCDId": jnxDfcCDId,
       "jnxDfcCDCriteria": jnxDfcCDCriteria,
       "jnxDfcCDByteRate": jnxDfcCDByteRate,
       "jnxDfcCDMatchedPackets": jnxDfcCDMatchedPackets,
       "jnxDfcCDMatchedBytes": jnxDfcCDMatchedBytes,
       "jnxDfcCDCongestionNotification": jnxDfcCDCongestionNotification,
       "jnxDfcNotifyVars": jnxDfcNotifyVars,
       "jnxDfcInterfaceName": jnxDfcInterfaceName,
       "jnxDfcInputPktRate": jnxDfcInputPktRate,
       "jnxDfcPpsSoftOverloadLowWatermark": jnxDfcPpsSoftOverloadLowWatermark,
       "jnxDfcPpsSoftOverloadHighWatermark": jnxDfcPpsSoftOverloadHighWatermark,
       "jnxDfcPpsHardOverloadLowWatermark": jnxDfcPpsHardOverloadLowWatermark,
       "jnxDfcPpsHardOverloadHighWatermark": jnxDfcPpsHardOverloadHighWatermark,
       "jnxDfcFlowsUsage": jnxDfcFlowsUsage,
       "jnxDfcCriteriaUsage": jnxDfcCriteriaUsage,
       "jnxDfcMemSoftOverloadLowWatermark": jnxDfcMemSoftOverloadLowWatermark,
       "jnxDfcMemSoftOverloadHighWatermark": jnxDfcMemSoftOverloadHighWatermark,
       "jnxDfcFlowLowWatermark": jnxDfcFlowLowWatermark,
       "jnxDfcFlowHighWatermark": jnxDfcFlowHighWatermark,
       "jnxDfcCriteriaLowWatermark": jnxDfcCriteriaLowWatermark,
       "jnxDfcCriteriaHighWatermark": jnxDfcCriteriaHighWatermark,
       "jnxDfcNotificationPrefix": jnxDfcNotificationPrefix,
       "jnxDfcSoftPpsThresholdExceeded": jnxDfcSoftPpsThresholdExceeded,
       "jnxDfcSoftPpsUnderThreshold": jnxDfcSoftPpsUnderThreshold,
       "jnxDfcHardPpsThresholdExceeded": jnxDfcHardPpsThresholdExceeded,
       "jnxDfcHardPpsUnderThreshold": jnxDfcHardPpsUnderThreshold,
       "jnxDfcSoftMemThresholdExceeded": jnxDfcSoftMemThresholdExceeded,
       "jnxDfcSoftMemUnderThreshold": jnxDfcSoftMemUnderThreshold,
       "jnxDfcHardMemThresholdExceeded": jnxDfcHardMemThresholdExceeded,
       "jnxDfcHardMemUnderThreshold": jnxDfcHardMemUnderThreshold}
)
