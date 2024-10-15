# SNMP MIB module (INFORMANT-WMI-EXCHANGE) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/INFORMANT-WMI-EXCHANGE
# Produced by pysmi-1.5.4 at Mon Oct 14 22:09:22 2024
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention",
    "TruthValue")

(WtcsDisplayString,
 informant) = mibBuilder.importSymbols(
    "WTCS",
    "WtcsDisplayString",
    "informant")


# MODULE-IDENTITY

wmiExchange = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23)
)
wmiExchange.setRevisions(
        ("2008-04-14 17:17",
         "2005-04-11 04:09")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ExchangeClusterResourceTable_Object = MibTable
exchangeClusterResourceTable = _ExchangeClusterResourceTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 1)
)
if mibBuilder.loadTexts:
    exchangeClusterResourceTable.setStatus("current")
_ExchangeClusterResourceEntry_Object = MibTableRow
exchangeClusterResourceEntry = _ExchangeClusterResourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 1, 1)
)
exchangeClusterResourceEntry.setIndexNames(
    (0, "INFORMANT-WMI-EXCHANGE", "excrIndex"),
)
if mibBuilder.loadTexts:
    exchangeClusterResourceEntry.setStatus("current")


class _ExcrIndex_Type(Integer32):
    """Custom type excrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ExcrIndex_Type.__name__ = "Integer32"
_ExcrIndex_Object = MibTableColumn
excrIndex = _ExcrIndex_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 1, 1, 1),
    _ExcrIndex_Type()
)
excrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excrIndex.setStatus("current")
_ExcrName_Type = WtcsDisplayString
_ExcrName_Object = MibTableColumn
excrName = _ExcrName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 1, 1, 2),
    _ExcrName_Type()
)
excrName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excrName.setStatus("current")
_ExcrOwner_Type = WtcsDisplayString
_ExcrOwner_Object = MibTableColumn
excrOwner = _ExcrOwner_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 1, 1, 3),
    _ExcrOwner_Type()
)
excrOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excrOwner.setStatus("current")
_ExcrState_Type = Gauge32
_ExcrState_Object = MibTableColumn
excrState = _ExcrState_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 1, 1, 4),
    _ExcrState_Type()
)
excrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excrState.setStatus("current")
_ExcrType_Type = WtcsDisplayString
_ExcrType_Object = MibTableColumn
excrType = _ExcrType_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 1, 1, 5),
    _ExcrType_Type()
)
excrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excrType.setStatus("current")
_ExcrVirtualMachine_Type = WtcsDisplayString
_ExcrVirtualMachine_Object = MibTableColumn
excrVirtualMachine = _ExcrVirtualMachine_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 1, 1, 6),
    _ExcrVirtualMachine_Type()
)
excrVirtualMachine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excrVirtualMachine.setStatus("current")
_ExchangeConnectorStateTable_Object = MibTable
exchangeConnectorStateTable = _ExchangeConnectorStateTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 2)
)
if mibBuilder.loadTexts:
    exchangeConnectorStateTable.setStatus("current")
_ExchangeConnectorStateEntry_Object = MibTableRow
exchangeConnectorStateEntry = _ExchangeConnectorStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 2, 1)
)
exchangeConnectorStateEntry.setIndexNames(
    (0, "INFORMANT-WMI-EXCHANGE", "excsIndex"),
)
if mibBuilder.loadTexts:
    exchangeConnectorStateEntry.setStatus("current")


class _ExcsIndex_Type(Integer32):
    """Custom type excsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ExcsIndex_Type.__name__ = "Integer32"
_ExcsIndex_Object = MibTableColumn
excsIndex = _ExcsIndex_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 2, 1, 1),
    _ExcsIndex_Type()
)
excsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excsIndex.setStatus("current")
_ExcsDN_Type = WtcsDisplayString
_ExcsDN_Object = MibTableColumn
excsDN = _ExcsDN_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 2, 1, 2),
    _ExcsDN_Type()
)
excsDN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excsDN.setStatus("current")
_ExcsGroupDN_Type = WtcsDisplayString
_ExcsGroupDN_Object = MibTableColumn
excsGroupDN = _ExcsGroupDN_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 2, 1, 3),
    _ExcsGroupDN_Type()
)
excsGroupDN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excsGroupDN.setStatus("current")
_ExcsGroupGUID_Type = WtcsDisplayString
_ExcsGroupGUID_Object = MibTableColumn
excsGroupGUID = _ExcsGroupGUID_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 2, 1, 4),
    _ExcsGroupGUID_Type()
)
excsGroupGUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excsGroupGUID.setStatus("current")
_ExcsGUID_Type = WtcsDisplayString
_ExcsGUID_Object = MibTableColumn
excsGUID = _ExcsGUID_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 2, 1, 5),
    _ExcsGUID_Type()
)
excsGUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excsGUID.setStatus("current")
_ExcsIsUp_Type = TruthValue
_ExcsIsUp_Object = MibTableColumn
excsIsUp = _ExcsIsUp_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 2, 1, 6),
    _ExcsIsUp_Type()
)
excsIsUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excsIsUp.setStatus("current")
_ExcsName_Type = WtcsDisplayString
_ExcsName_Object = MibTableColumn
excsName = _ExcsName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 2, 1, 7),
    _ExcsName_Type()
)
excsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excsName.setStatus("current")
_ExchangeLinkTable_Object = MibTable
exchangeLinkTable = _ExchangeLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 3)
)
if mibBuilder.loadTexts:
    exchangeLinkTable.setStatus("current")
_ExchangeLinkEntry_Object = MibTableRow
exchangeLinkEntry = _ExchangeLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 3, 1)
)
exchangeLinkEntry.setIndexNames(
    (0, "INFORMANT-WMI-EXCHANGE", "exlIndex"),
)
if mibBuilder.loadTexts:
    exchangeLinkEntry.setStatus("current")


class _ExlIndex_Type(Integer32):
    """Custom type exlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ExlIndex_Type.__name__ = "Integer32"
_ExlIndex_Object = MibTableColumn
exlIndex = _ExlIndex_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 3, 1, 1),
    _ExlIndex_Type()
)
exlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exlIndex.setStatus("current")
_ExlActionFreeze_Type = TruthValue
_ExlActionFreeze_Object = MibTableColumn
exlActionFreeze = _ExlActionFreeze_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 3, 1, 2),
    _ExlActionFreeze_Type()
)
exlActionFreeze.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exlActionFreeze.setStatus("current")
_ExlActionKick_Type = TruthValue
_ExlActionKick_Object = MibTableColumn
exlActionKick = _ExlActionKick_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 3, 1, 3),
    _ExlActionKick_Type()
)
exlActionKick.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exlActionKick.setStatus("current")
_ExlActionThaw_Type = TruthValue
_ExlActionThaw_Object = MibTableColumn
exlActionThaw = _ExlActionThaw_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 3, 1, 4),
    _ExlActionThaw_Type()
)
exlActionThaw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exlActionThaw.setStatus("current")
_ExlExtendedStateInfo_Type = WtcsDisplayString
_ExlExtendedStateInfo_Object = MibTableColumn
exlExtendedStateInfo = _ExlExtendedStateInfo_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 3, 1, 5),
    _ExlExtendedStateInfo_Type()
)
exlExtendedStateInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exlExtendedStateInfo.setStatus("current")
_ExlGlobalStop_Type = TruthValue
_ExlGlobalStop_Object = MibTableColumn
exlGlobalStop = _ExlGlobalStop_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 3, 1, 6),
    _ExlGlobalStop_Type()
)
exlGlobalStop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exlGlobalStop.setStatus("current")
_ExlIncreasingTime_Type = Gauge32
_ExlIncreasingTime_Object = MibTableColumn
exlIncreasingTime = _ExlIncreasingTime_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 3, 1, 7),
    _ExlIncreasingTime_Type()
)
exlIncreasingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exlIncreasingTime.setStatus("current")
_ExlLinkDN_Type = WtcsDisplayString
_ExlLinkDN_Object = MibTableColumn
exlLinkDN = _ExlLinkDN_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 3, 1, 8),
    _ExlLinkDN_Type()
)
exlLinkDN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exlLinkDN.setStatus("current")
_ExlLinkName_Type = WtcsDisplayString
_ExlLinkName_Object = MibTableColumn
exlLinkName = _ExlLinkName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 3, 1, 9),
    _ExlLinkName_Type()
)
exlLinkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exlLinkName.setStatus("current")
_ExlNextScheduledConnection_Type = DateAndTime
_ExlNextScheduledConnection_Object = MibTableColumn
exlNextScheduledConnection = _ExlNextScheduledConnection_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 3, 1, 10),
    _ExlNextScheduledConnection_Type()
)
exlNextScheduledConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exlNextScheduledConnection.setStatus("current")
_ExlNumberOfMessages_Type = Gauge32
_ExlNumberOfMessages_Object = MibTableColumn
exlNumberOfMessages = _ExlNumberOfMessages_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 3, 1, 11),
    _ExlNumberOfMessages_Type()
)
exlNumberOfMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exlNumberOfMessages.setStatus("current")
_ExlOldestMessage_Type = DateAndTime
_ExlOldestMessage_Object = MibTableColumn
exlOldestMessage = _ExlOldestMessage_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 3, 1, 12),
    _ExlOldestMessage_Type()
)
exlOldestMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exlOldestMessage.setStatus("current")
_ExlProtocolName_Type = WtcsDisplayString
_ExlProtocolName_Object = MibTableColumn
exlProtocolName = _ExlProtocolName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 3, 1, 13),
    _ExlProtocolName_Type()
)
exlProtocolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exlProtocolName.setStatus("current")
_ExlSizeOfQueue_Type = WtcsDisplayString
_ExlSizeOfQueue_Object = MibTableColumn
exlSizeOfQueue = _ExlSizeOfQueue_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 3, 1, 14),
    _ExlSizeOfQueue_Type()
)
exlSizeOfQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exlSizeOfQueue.setStatus("current")
_ExlStateActive_Type = TruthValue
_ExlStateActive_Object = MibTableColumn
exlStateActive = _ExlStateActive_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 3, 1, 15),
    _ExlStateActive_Type()
)
exlStateActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exlStateActive.setStatus("current")
_ExlStateFlags_Type = Gauge32
_ExlStateFlags_Object = MibTableColumn
exlStateFlags = _ExlStateFlags_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 3, 1, 16),
    _ExlStateFlags_Type()
)
exlStateFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exlStateFlags.setStatus("current")
_ExlStateFrozen_Type = TruthValue
_ExlStateFrozen_Object = MibTableColumn
exlStateFrozen = _ExlStateFrozen_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 3, 1, 17),
    _ExlStateFrozen_Type()
)
exlStateFrozen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exlStateFrozen.setStatus("current")
_ExlStateReady_Type = TruthValue
_ExlStateReady_Object = MibTableColumn
exlStateReady = _ExlStateReady_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 3, 1, 18),
    _ExlStateReady_Type()
)
exlStateReady.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exlStateReady.setStatus("current")
_ExlStateRemote_Type = TruthValue
_ExlStateRemote_Object = MibTableColumn
exlStateRemote = _ExlStateRemote_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 3, 1, 19),
    _ExlStateRemote_Type()
)
exlStateRemote.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exlStateRemote.setStatus("current")
_ExlStateRetry_Type = TruthValue
_ExlStateRetry_Object = MibTableColumn
exlStateRetry = _ExlStateRetry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 3, 1, 20),
    _ExlStateRetry_Type()
)
exlStateRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exlStateRetry.setStatus("current")
_ExlStateScheduled_Type = TruthValue
_ExlStateScheduled_Object = MibTableColumn
exlStateScheduled = _ExlStateScheduled_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 3, 1, 21),
    _ExlStateScheduled_Type()
)
exlStateScheduled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exlStateScheduled.setStatus("current")
_ExlSupportedLinkActions_Type = Gauge32
_ExlSupportedLinkActions_Object = MibTableColumn
exlSupportedLinkActions = _ExlSupportedLinkActions_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 3, 1, 22),
    _ExlSupportedLinkActions_Type()
)
exlSupportedLinkActions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exlSupportedLinkActions.setStatus("current")
_ExlTypeCurrentlyUnreachable_Type = TruthValue
_ExlTypeCurrentlyUnreachable_Object = MibTableColumn
exlTypeCurrentlyUnreachable = _ExlTypeCurrentlyUnreachable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 3, 1, 23),
    _ExlTypeCurrentlyUnreachable_Type()
)
exlTypeCurrentlyUnreachable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exlTypeCurrentlyUnreachable.setStatus("current")
_ExlTypeDeferredDelivery_Type = TruthValue
_ExlTypeDeferredDelivery_Object = MibTableColumn
exlTypeDeferredDelivery = _ExlTypeDeferredDelivery_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 3, 1, 24),
    _ExlTypeDeferredDelivery_Type()
)
exlTypeDeferredDelivery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exlTypeDeferredDelivery.setStatus("current")
_ExlTypeInternal_Type = TruthValue
_ExlTypeInternal_Object = MibTableColumn
exlTypeInternal = _ExlTypeInternal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 3, 1, 25),
    _ExlTypeInternal_Type()
)
exlTypeInternal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exlTypeInternal.setStatus("current")
_ExlTypeLocalDelivery_Type = TruthValue
_ExlTypeLocalDelivery_Object = MibTableColumn
exlTypeLocalDelivery = _ExlTypeLocalDelivery_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 3, 1, 26),
    _ExlTypeLocalDelivery_Type()
)
exlTypeLocalDelivery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exlTypeLocalDelivery.setStatus("current")
_ExlTypePendingCategorization_Type = TruthValue
_ExlTypePendingCategorization_Object = MibTableColumn
exlTypePendingCategorization = _ExlTypePendingCategorization_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 3, 1, 27),
    _ExlTypePendingCategorization_Type()
)
exlTypePendingCategorization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exlTypePendingCategorization.setStatus("current")
_ExlTypePendingRouting_Type = TruthValue
_ExlTypePendingRouting_Object = MibTableColumn
exlTypePendingRouting = _ExlTypePendingRouting_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 3, 1, 28),
    _ExlTypePendingRouting_Type()
)
exlTypePendingRouting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exlTypePendingRouting.setStatus("current")
_ExlTypePendingSubmission_Type = TruthValue
_ExlTypePendingSubmission_Object = MibTableColumn
exlTypePendingSubmission = _ExlTypePendingSubmission_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 3, 1, 29),
    _ExlTypePendingSubmission_Type()
)
exlTypePendingSubmission.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exlTypePendingSubmission.setStatus("current")
_ExlTypeRemoteDelivery_Type = TruthValue
_ExlTypeRemoteDelivery_Object = MibTableColumn
exlTypeRemoteDelivery = _ExlTypeRemoteDelivery_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 3, 1, 30),
    _ExlTypeRemoteDelivery_Type()
)
exlTypeRemoteDelivery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exlTypeRemoteDelivery.setStatus("current")
_ExlVersion_Type = Gauge32
_ExlVersion_Object = MibTableColumn
exlVersion = _ExlVersion_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 3, 1, 31),
    _ExlVersion_Type()
)
exlVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exlVersion.setStatus("current")
_ExlVirtualMachine_Type = Gauge32
_ExlVirtualMachine_Object = MibTableColumn
exlVirtualMachine = _ExlVirtualMachine_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 3, 1, 32),
    _ExlVirtualMachine_Type()
)
exlVirtualMachine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exlVirtualMachine.setStatus("current")
_ExlVirtualServerName_Type = WtcsDisplayString
_ExlVirtualServerName_Object = MibTableColumn
exlVirtualServerName = _ExlVirtualServerName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 3, 1, 33),
    _ExlVirtualServerName_Type()
)
exlVirtualServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exlVirtualServerName.setStatus("current")
_ExchangeQueueTable_Object = MibTable
exchangeQueueTable = _ExchangeQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 4)
)
if mibBuilder.loadTexts:
    exchangeQueueTable.setStatus("current")
_ExchangeQueueEntry_Object = MibTableRow
exchangeQueueEntry = _ExchangeQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 4, 1)
)
exchangeQueueEntry.setIndexNames(
    (0, "INFORMANT-WMI-EXCHANGE", "exqIndex"),
)
if mibBuilder.loadTexts:
    exchangeQueueEntry.setStatus("current")


class _ExqIndex_Type(Integer32):
    """Custom type exqIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ExqIndex_Type.__name__ = "Integer32"
_ExqIndex_Object = MibTableColumn
exqIndex = _ExqIndex_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 4, 1, 1),
    _ExqIndex_Type()
)
exqIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exqIndex.setStatus("current")
_ExqCanEnumAll_Type = TruthValue
_ExqCanEnumAll_Object = MibTableColumn
exqCanEnumAll = _ExqCanEnumAll_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 4, 1, 2),
    _ExqCanEnumAll_Type()
)
exqCanEnumAll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exqCanEnumAll.setStatus("current")
_ExqCanEnumFailed_Type = TruthValue
_ExqCanEnumFailed_Object = MibTableColumn
exqCanEnumFailed = _ExqCanEnumFailed_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 4, 1, 3),
    _ExqCanEnumFailed_Type()
)
exqCanEnumFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exqCanEnumFailed.setStatus("current")
_ExqCanEnumFirstNMessages_Type = TruthValue
_ExqCanEnumFirstNMessages_Object = MibTableColumn
exqCanEnumFirstNMessages = _ExqCanEnumFirstNMessages_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 4, 1, 4),
    _ExqCanEnumFirstNMessages_Type()
)
exqCanEnumFirstNMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exqCanEnumFirstNMessages.setStatus("current")
_ExqCanEnumFrozen_Type = TruthValue
_ExqCanEnumFrozen_Object = MibTableColumn
exqCanEnumFrozen = _ExqCanEnumFrozen_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 4, 1, 5),
    _ExqCanEnumFrozen_Type()
)
exqCanEnumFrozen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exqCanEnumFrozen.setStatus("current")
_ExqCanEnumInvertSense_Type = TruthValue
_ExqCanEnumInvertSense_Object = MibTableColumn
exqCanEnumInvertSense = _ExqCanEnumInvertSense_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 4, 1, 6),
    _ExqCanEnumInvertSense_Type()
)
exqCanEnumInvertSense.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exqCanEnumInvertSense.setStatus("current")
_ExqCanEnumLargerThan_Type = TruthValue
_ExqCanEnumLargerThan_Object = MibTableColumn
exqCanEnumLargerThan = _ExqCanEnumLargerThan_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 4, 1, 7),
    _ExqCanEnumLargerThan_Type()
)
exqCanEnumLargerThan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exqCanEnumLargerThan.setStatus("current")
_ExqCanEnumNLargestMessages_Type = TruthValue
_ExqCanEnumNLargestMessages_Object = MibTableColumn
exqCanEnumNLargestMessages = _ExqCanEnumNLargestMessages_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 4, 1, 8),
    _ExqCanEnumNLargestMessages_Type()
)
exqCanEnumNLargestMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exqCanEnumNLargestMessages.setStatus("current")
_ExqCanEnumNOldestMessages_Type = TruthValue
_ExqCanEnumNOldestMessages_Object = MibTableColumn
exqCanEnumNOldestMessages = _ExqCanEnumNOldestMessages_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 4, 1, 9),
    _ExqCanEnumNOldestMessages_Type()
)
exqCanEnumNOldestMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exqCanEnumNOldestMessages.setStatus("current")
_ExqCanEnumOlderThan_Type = TruthValue
_ExqCanEnumOlderThan_Object = MibTableColumn
exqCanEnumOlderThan = _ExqCanEnumOlderThan_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 4, 1, 10),
    _ExqCanEnumOlderThan_Type()
)
exqCanEnumOlderThan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exqCanEnumOlderThan.setStatus("current")
_ExqCanEnumRecipient_Type = TruthValue
_ExqCanEnumRecipient_Object = MibTableColumn
exqCanEnumRecipient = _ExqCanEnumRecipient_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 4, 1, 11),
    _ExqCanEnumRecipient_Type()
)
exqCanEnumRecipient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exqCanEnumRecipient.setStatus("current")
_ExqCanEnumSender_Type = TruthValue
_ExqCanEnumSender_Object = MibTableColumn
exqCanEnumSender = _ExqCanEnumSender_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 4, 1, 12),
    _ExqCanEnumSender_Type()
)
exqCanEnumSender.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exqCanEnumSender.setStatus("current")
_ExqGlobalStop_Type = TruthValue
_ExqGlobalStop_Object = MibTableColumn
exqGlobalStop = _ExqGlobalStop_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 4, 1, 13),
    _ExqGlobalStop_Type()
)
exqGlobalStop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exqGlobalStop.setStatus("current")
_ExqIncreasingTime_Type = Gauge32
_ExqIncreasingTime_Object = MibTableColumn
exqIncreasingTime = _ExqIncreasingTime_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 4, 1, 14),
    _ExqIncreasingTime_Type()
)
exqIncreasingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exqIncreasingTime.setStatus("current")
_ExqLinkName_Type = WtcsDisplayString
_ExqLinkName_Object = MibTableColumn
exqLinkName = _ExqLinkName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 4, 1, 15),
    _ExqLinkName_Type()
)
exqLinkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exqLinkName.setStatus("current")
_ExqMsgEnumFlagsSupported_Type = Gauge32
_ExqMsgEnumFlagsSupported_Object = MibTableColumn
exqMsgEnumFlagsSupported = _ExqMsgEnumFlagsSupported_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 4, 1, 16),
    _ExqMsgEnumFlagsSupported_Type()
)
exqMsgEnumFlagsSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exqMsgEnumFlagsSupported.setStatus("current")
_ExqNumberOfMessages_Type = Gauge32
_ExqNumberOfMessages_Object = MibTableColumn
exqNumberOfMessages = _ExqNumberOfMessages_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 4, 1, 17),
    _ExqNumberOfMessages_Type()
)
exqNumberOfMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exqNumberOfMessages.setStatus("current")
_ExqProtocolName_Type = WtcsDisplayString
_ExqProtocolName_Object = MibTableColumn
exqProtocolName = _ExqProtocolName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 4, 1, 18),
    _ExqProtocolName_Type()
)
exqProtocolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exqProtocolName.setStatus("current")
_ExqQueueName_Type = WtcsDisplayString
_ExqQueueName_Object = MibTableColumn
exqQueueName = _ExqQueueName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 4, 1, 19),
    _ExqQueueName_Type()
)
exqQueueName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exqQueueName.setStatus("current")
_ExqSizeOfQueue_Type = WtcsDisplayString
_ExqSizeOfQueue_Object = MibTableColumn
exqSizeOfQueue = _ExqSizeOfQueue_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 4, 1, 20),
    _ExqSizeOfQueue_Type()
)
exqSizeOfQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exqSizeOfQueue.setStatus("current")
_ExqVersion_Type = Gauge32
_ExqVersion_Object = MibTableColumn
exqVersion = _ExqVersion_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 4, 1, 21),
    _ExqVersion_Type()
)
exqVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exqVersion.setStatus("current")
_ExqVirtualMachine_Type = WtcsDisplayString
_ExqVirtualMachine_Object = MibTableColumn
exqVirtualMachine = _ExqVirtualMachine_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 4, 1, 22),
    _ExqVirtualMachine_Type()
)
exqVirtualMachine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exqVirtualMachine.setStatus("current")
_ExqVirtualServerName_Type = WtcsDisplayString
_ExqVirtualServerName_Object = MibTableColumn
exqVirtualServerName = _ExqVirtualServerName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 4, 1, 23),
    _ExqVirtualServerName_Type()
)
exqVirtualServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exqVirtualServerName.setStatus("current")
_ExchangeServerStateTable_Object = MibTable
exchangeServerStateTable = _ExchangeServerStateTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 5)
)
if mibBuilder.loadTexts:
    exchangeServerStateTable.setStatus("current")
_ExchangeServerStateEntry_Object = MibTableRow
exchangeServerStateEntry = _ExchangeServerStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 5, 1)
)
exchangeServerStateEntry.setIndexNames(
    (0, "INFORMANT-WMI-EXCHANGE", "exssIndex"),
)
if mibBuilder.loadTexts:
    exchangeServerStateEntry.setStatus("current")


class _ExssIndex_Type(Integer32):
    """Custom type exssIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ExssIndex_Type.__name__ = "Integer32"
_ExssIndex_Object = MibTableColumn
exssIndex = _ExssIndex_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 5, 1, 1),
    _ExssIndex_Type()
)
exssIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exssIndex.setStatus("current")


class _ExssClusterState_Type(Integer32):
    """Custom type exssClusterState based on Integer32"""
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
        *(("error", 3),
          ("ok", 1),
          ("unknown", 0),
          ("warning", 2))
    )


_ExssClusterState_Type.__name__ = "Integer32"
_ExssClusterState_Object = MibTableColumn
exssClusterState = _ExssClusterState_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 5, 1, 2),
    _ExssClusterState_Type()
)
exssClusterState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exssClusterState.setStatus("current")
_ExssClusterStateString_Type = WtcsDisplayString
_ExssClusterStateString_Object = MibTableColumn
exssClusterStateString = _ExssClusterStateString_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 5, 1, 3),
    _ExssClusterStateString_Type()
)
exssClusterStateString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exssClusterStateString.setStatus("current")


class _ExssCPUState_Type(Integer32):
    """Custom type exssCPUState based on Integer32"""
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
        *(("error", 3),
          ("ok", 1),
          ("unknown", 0),
          ("warning", 2))
    )


_ExssCPUState_Type.__name__ = "Integer32"
_ExssCPUState_Object = MibTableColumn
exssCPUState = _ExssCPUState_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 5, 1, 4),
    _ExssCPUState_Type()
)
exssCPUState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exssCPUState.setStatus("current")
_ExssCPUStateString_Type = WtcsDisplayString
_ExssCPUStateString_Object = MibTableColumn
exssCPUStateString = _ExssCPUStateString_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 5, 1, 5),
    _ExssCPUStateString_Type()
)
exssCPUStateString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exssCPUStateString.setStatus("current")


class _ExssDisksState_Type(Integer32):
    """Custom type exssDisksState based on Integer32"""
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
        *(("error", 3),
          ("ok", 1),
          ("unknown", 0),
          ("warning", 2))
    )


_ExssDisksState_Type.__name__ = "Integer32"
_ExssDisksState_Object = MibTableColumn
exssDisksState = _ExssDisksState_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 5, 1, 6),
    _ExssDisksState_Type()
)
exssDisksState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exssDisksState.setStatus("current")
_ExssDisksStateString_Type = WtcsDisplayString
_ExssDisksStateString_Object = MibTableColumn
exssDisksStateString = _ExssDisksStateString_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 5, 1, 7),
    _ExssDisksStateString_Type()
)
exssDisksStateString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exssDisksStateString.setStatus("current")
_ExssDN_Type = WtcsDisplayString
_ExssDN_Object = MibTableColumn
exssDN = _ExssDN_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 5, 1, 8),
    _ExssDN_Type()
)
exssDN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exssDN.setStatus("current")
_ExssGroupDN_Type = WtcsDisplayString
_ExssGroupDN_Object = MibTableColumn
exssGroupDN = _ExssGroupDN_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 5, 1, 9),
    _ExssGroupDN_Type()
)
exssGroupDN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exssGroupDN.setStatus("current")
_ExssGroupGUID_Type = WtcsDisplayString
_ExssGroupGUID_Object = MibTableColumn
exssGroupGUID = _ExssGroupGUID_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 5, 1, 10),
    _ExssGroupGUID_Type()
)
exssGroupGUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exssGroupGUID.setStatus("current")
_ExssGUID_Type = WtcsDisplayString
_ExssGUID_Object = MibTableColumn
exssGUID = _ExssGUID_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 5, 1, 11),
    _ExssGUID_Type()
)
exssGUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exssGUID.setStatus("current")


class _ExssMemoryState_Type(Integer32):
    """Custom type exssMemoryState based on Integer32"""
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
        *(("error", 3),
          ("ok", 1),
          ("unknown", 0),
          ("warning", 2))
    )


_ExssMemoryState_Type.__name__ = "Integer32"
_ExssMemoryState_Object = MibTableColumn
exssMemoryState = _ExssMemoryState_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 5, 1, 12),
    _ExssMemoryState_Type()
)
exssMemoryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exssMemoryState.setStatus("current")
_ExssMemoryStateString_Type = WtcsDisplayString
_ExssMemoryStateString_Object = MibTableColumn
exssMemoryStateString = _ExssMemoryStateString_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 5, 1, 13),
    _ExssMemoryStateString_Type()
)
exssMemoryStateString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exssMemoryStateString.setStatus("current")
_ExssName_Type = WtcsDisplayString
_ExssName_Object = MibTableColumn
exssName = _ExssName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 5, 1, 14),
    _ExssName_Type()
)
exssName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exssName.setStatus("current")


class _ExssQueuesState_Type(Integer32):
    """Custom type exssQueuesState based on Integer32"""
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
        *(("error", 3),
          ("ok", 1),
          ("unknown", 0),
          ("warning", 2))
    )


_ExssQueuesState_Type.__name__ = "Integer32"
_ExssQueuesState_Object = MibTableColumn
exssQueuesState = _ExssQueuesState_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 5, 1, 15),
    _ExssQueuesState_Type()
)
exssQueuesState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exssQueuesState.setStatus("current")
_ExssQueuesStateString_Type = WtcsDisplayString
_ExssQueuesStateString_Object = MibTableColumn
exssQueuesStateString = _ExssQueuesStateString_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 5, 1, 16),
    _ExssQueuesStateString_Type()
)
exssQueuesStateString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exssQueuesStateString.setStatus("current")
_ExssServerMaintenance_Type = TruthValue
_ExssServerMaintenance_Object = MibTableColumn
exssServerMaintenance = _ExssServerMaintenance_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 5, 1, 17),
    _ExssServerMaintenance_Type()
)
exssServerMaintenance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exssServerMaintenance.setStatus("current")


class _ExssServerState_Type(Integer32):
    """Custom type exssServerState based on Integer32"""
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
        *(("error", 3),
          ("ok", 1),
          ("unknown", 0),
          ("warning", 2))
    )


_ExssServerState_Type.__name__ = "Integer32"
_ExssServerState_Object = MibTableColumn
exssServerState = _ExssServerState_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 5, 1, 18),
    _ExssServerState_Type()
)
exssServerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exssServerState.setStatus("current")
_ExssServerStateString_Type = WtcsDisplayString
_ExssServerStateString_Object = MibTableColumn
exssServerStateString = _ExssServerStateString_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 5, 1, 19),
    _ExssServerStateString_Type()
)
exssServerStateString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exssServerStateString.setStatus("current")


class _ExssServicesState_Type(Integer32):
    """Custom type exssServicesState based on Integer32"""
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
        *(("error", 3),
          ("ok", 1),
          ("unknown", 0),
          ("warning", 2))
    )


_ExssServicesState_Type.__name__ = "Integer32"
_ExssServicesState_Object = MibTableColumn
exssServicesState = _ExssServicesState_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 5, 1, 20),
    _ExssServicesState_Type()
)
exssServicesState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exssServicesState.setStatus("current")
_ExssServicesStateString_Type = WtcsDisplayString
_ExssServicesStateString_Object = MibTableColumn
exssServicesStateString = _ExssServicesStateString_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 5, 1, 21),
    _ExssServicesStateString_Type()
)
exssServicesStateString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exssServicesStateString.setStatus("current")
_ExssUnreachable_Type = TruthValue
_ExssUnreachable_Object = MibTableColumn
exssUnreachable = _ExssUnreachable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 5, 1, 22),
    _ExssUnreachable_Type()
)
exssUnreachable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exssUnreachable.setStatus("current")
_ExssVersion_Type = Gauge32
_ExssVersion_Object = MibTableColumn
exssVersion = _ExssVersion_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 5, 1, 23),
    _ExssVersion_Type()
)
exssVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exssVersion.setStatus("current")
_ExchangeDSAccessDCTable_Object = MibTable
exchangeDSAccessDCTable = _ExchangeDSAccessDCTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 6)
)
if mibBuilder.loadTexts:
    exchangeDSAccessDCTable.setStatus("current")
_ExchangeDSAccessDCEntry_Object = MibTableRow
exchangeDSAccessDCEntry = _ExchangeDSAccessDCEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 6, 1)
)
exchangeDSAccessDCEntry.setIndexNames(
    (0, "INFORMANT-WMI-EXCHANGE", "exdsIndex"),
)
if mibBuilder.loadTexts:
    exchangeDSAccessDCEntry.setStatus("current")


class _ExdsIndex_Type(Integer32):
    """Custom type exdsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ExdsIndex_Type.__name__ = "Integer32"
_ExdsIndex_Object = MibTableColumn
exdsIndex = _ExdsIndex_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 6, 1, 1),
    _ExdsIndex_Type()
)
exdsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exdsIndex.setStatus("current")


class _ExdsConfigurationType_Type(Integer32):
    """Custom type exdsConfigurationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 1),
          ("manual", 0))
    )


_ExdsConfigurationType_Type.__name__ = "Integer32"
_ExdsConfigurationType_Object = MibTableColumn
exdsConfigurationType = _ExdsConfigurationType_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 6, 1, 2),
    _ExdsConfigurationType_Type()
)
exdsConfigurationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exdsConfigurationType.setStatus("current")
_ExdsIsFast_Type = TruthValue
_ExdsIsFast_Object = MibTableColumn
exdsIsFast = _ExdsIsFast_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 6, 1, 3),
    _ExdsIsFast_Type()
)
exdsIsFast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exdsIsFast.setStatus("current")
_ExdsIsInSync_Type = TruthValue
_ExdsIsInSync_Object = MibTableColumn
exdsIsInSync = _ExdsIsInSync_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 6, 1, 4),
    _ExdsIsInSync_Type()
)
exdsIsInSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exdsIsInSync.setStatus("current")
_ExdsIsUp_Type = TruthValue
_ExdsIsUp_Object = MibTableColumn
exdsIsUp = _ExdsIsUp_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 6, 1, 5),
    _ExdsIsUp_Type()
)
exdsIsUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exdsIsUp.setStatus("current")
_ExdsLDAPPort_Type = Gauge32
_ExdsLDAPPort_Object = MibTableColumn
exdsLDAPPort = _ExdsLDAPPort_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 6, 1, 6),
    _ExdsLDAPPort_Type()
)
exdsLDAPPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exdsLDAPPort.setStatus("current")
_ExdsName_Type = WtcsDisplayString
_ExdsName_Object = MibTableColumn
exdsName = _ExdsName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 6, 1, 7),
    _ExdsName_Type()
)
exdsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exdsName.setStatus("current")


class _ExdsType_Type(Integer32):
    """Custom type exdsType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("configurationDomainController", 0),
          ("globalCatalog", 2),
          ("localDomainController", 1))
    )


_ExdsType_Type.__name__ = "Integer32"
_ExdsType_Object = MibTableColumn
exdsType = _ExdsType_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 6, 1, 8),
    _ExdsType_Type()
)
exdsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exdsType.setStatus("current")
_ExchangeFolderTreeTable_Object = MibTable
exchangeFolderTreeTable = _ExchangeFolderTreeTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 7)
)
if mibBuilder.loadTexts:
    exchangeFolderTreeTable.setStatus("current")
_ExchangeFolderTreeEntry_Object = MibTableRow
exchangeFolderTreeEntry = _ExchangeFolderTreeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 7, 1)
)
exchangeFolderTreeEntry.setIndexNames(
    (0, "INFORMANT-WMI-EXCHANGE", "exftIndex"),
)
if mibBuilder.loadTexts:
    exchangeFolderTreeEntry.setStatus("current")


class _ExftIndex_Type(Integer32):
    """Custom type exftIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ExftIndex_Type.__name__ = "Integer32"
_ExftIndex_Object = MibTableColumn
exftIndex = _ExftIndex_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 7, 1, 1),
    _ExftIndex_Type()
)
exftIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exftIndex.setStatus("current")
_ExftAdministrativeGroup_Type = WtcsDisplayString
_ExftAdministrativeGroup_Object = MibTableColumn
exftAdministrativeGroup = _ExftAdministrativeGroup_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 7, 1, 2),
    _ExftAdministrativeGroup_Type()
)
exftAdministrativeGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exftAdministrativeGroup.setStatus("current")
_ExftAdministrativeNote_Type = WtcsDisplayString
_ExftAdministrativeNote_Object = MibTableColumn
exftAdministrativeNote = _ExftAdministrativeNote_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 7, 1, 3),
    _ExftAdministrativeNote_Type()
)
exftAdministrativeNote.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exftAdministrativeNote.setStatus("current")
_ExftAssociatedPublicStores_Type = WtcsDisplayString
_ExftAssociatedPublicStores_Object = MibTableColumn
exftAssociatedPublicStores = _ExftAssociatedPublicStores_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 7, 1, 4),
    _ExftAssociatedPublicStores_Type()
)
exftAssociatedPublicStores.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exftAssociatedPublicStores.setStatus("current")
_ExftCreationTime_Type = DateAndTime
_ExftCreationTime_Object = MibTableColumn
exftCreationTime = _ExftCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 7, 1, 5),
    _ExftCreationTime_Type()
)
exftCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exftCreationTime.setStatus("current")
_ExftGUID_Type = WtcsDisplayString
_ExftGUID_Object = MibTableColumn
exftGUID = _ExftGUID_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 7, 1, 6),
    _ExftGUID_Type()
)
exftGUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exftGUID.setStatus("current")
_ExftHasLocalPublicStore_Type = TruthValue
_ExftHasLocalPublicStore_Object = MibTableColumn
exftHasLocalPublicStore = _ExftHasLocalPublicStore_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 7, 1, 7),
    _ExftHasLocalPublicStore_Type()
)
exftHasLocalPublicStore.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exftHasLocalPublicStore.setStatus("current")
_ExftLastModificationTime_Type = DateAndTime
_ExftLastModificationTime_Object = MibTableColumn
exftLastModificationTime = _ExftLastModificationTime_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 7, 1, 8),
    _ExftLastModificationTime_Type()
)
exftLastModificationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exftLastModificationTime.setStatus("current")
_ExftMapiFolderTree_Type = TruthValue
_ExftMapiFolderTree_Object = MibTableColumn
exftMapiFolderTree = _ExftMapiFolderTree_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 7, 1, 9),
    _ExftMapiFolderTree_Type()
)
exftMapiFolderTree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exftMapiFolderTree.setStatus("current")
_ExftName_Type = WtcsDisplayString
_ExftName_Object = MibTableColumn
exftName = _ExftName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 7, 1, 10),
    _ExftName_Type()
)
exftName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exftName.setStatus("current")
_ExftRootFolderURL_Type = WtcsDisplayString
_ExftRootFolderURL_Object = MibTableColumn
exftRootFolderURL = _ExftRootFolderURL_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 7, 1, 11),
    _ExftRootFolderURL_Type()
)
exftRootFolderURL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exftRootFolderURL.setStatus("current")
_ExchangeLinkV2Table_Object = MibTable
exchangeLinkV2Table = _ExchangeLinkV2Table_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 8)
)
if mibBuilder.loadTexts:
    exchangeLinkV2Table.setStatus("current")
_ExchangeLinkV2Entry_Object = MibTableRow
exchangeLinkV2Entry = _ExchangeLinkV2Entry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 8, 1)
)
exchangeLinkV2Entry.setIndexNames(
    (0, "INFORMANT-WMI-EXCHANGE", "exl2Index"),
)
if mibBuilder.loadTexts:
    exchangeLinkV2Entry.setStatus("current")


class _Exl2Index_Type(Integer32):
    """Custom type exl2Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Exl2Index_Type.__name__ = "Integer32"
_Exl2Index_Object = MibTableColumn
exl2Index = _Exl2Index_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 8, 1, 1),
    _Exl2Index_Type()
)
exl2Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exl2Index.setStatus("current")
_Exl2ActionFreeze_Type = TruthValue
_Exl2ActionFreeze_Object = MibTableColumn
exl2ActionFreeze = _Exl2ActionFreeze_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 8, 1, 2),
    _Exl2ActionFreeze_Type()
)
exl2ActionFreeze.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exl2ActionFreeze.setStatus("current")
_Exl2ActionKick_Type = TruthValue
_Exl2ActionKick_Object = MibTableColumn
exl2ActionKick = _Exl2ActionKick_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 8, 1, 3),
    _Exl2ActionKick_Type()
)
exl2ActionKick.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exl2ActionKick.setStatus("current")
_Exl2ActionThaw_Type = TruthValue
_Exl2ActionThaw_Object = MibTableColumn
exl2ActionThaw = _Exl2ActionThaw_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 8, 1, 4),
    _Exl2ActionThaw_Type()
)
exl2ActionThaw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exl2ActionThaw.setStatus("current")
_Exl2ExtendedStateInfo_Type = WtcsDisplayString
_Exl2ExtendedStateInfo_Object = MibTableColumn
exl2ExtendedStateInfo = _Exl2ExtendedStateInfo_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 8, 1, 5),
    _Exl2ExtendedStateInfo_Type()
)
exl2ExtendedStateInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exl2ExtendedStateInfo.setStatus("current")
_Exl2GlobalStop_Type = TruthValue
_Exl2GlobalStop_Object = MibTableColumn
exl2GlobalStop = _Exl2GlobalStop_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 8, 1, 6),
    _Exl2GlobalStop_Type()
)
exl2GlobalStop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exl2GlobalStop.setStatus("current")
_Exl2LinkDN_Type = WtcsDisplayString
_Exl2LinkDN_Object = MibTableColumn
exl2LinkDN = _Exl2LinkDN_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 8, 1, 7),
    _Exl2LinkDN_Type()
)
exl2LinkDN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exl2LinkDN.setStatus("current")
_Exl2LinkId_Type = WtcsDisplayString
_Exl2LinkId_Object = MibTableColumn
exl2LinkId = _Exl2LinkId_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 8, 1, 8),
    _Exl2LinkId_Type()
)
exl2LinkId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exl2LinkId.setStatus("current")
_Exl2LinkName_Type = WtcsDisplayString
_Exl2LinkName_Object = MibTableColumn
exl2LinkName = _Exl2LinkName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 8, 1, 9),
    _Exl2LinkName_Type()
)
exl2LinkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exl2LinkName.setStatus("current")
_Exl2MessageCount_Type = Gauge32
_Exl2MessageCount_Object = MibTableColumn
exl2MessageCount = _Exl2MessageCount_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 8, 1, 10),
    _Exl2MessageCount_Type()
)
exl2MessageCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exl2MessageCount.setStatus("current")
_Exl2NextScheduledConnection_Type = DateAndTime
_Exl2NextScheduledConnection_Object = MibTableColumn
exl2NextScheduledConnection = _Exl2NextScheduledConnection_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 8, 1, 11),
    _Exl2NextScheduledConnection_Type()
)
exl2NextScheduledConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exl2NextScheduledConnection.setStatus("current")
_Exl2OldestMessage_Type = DateAndTime
_Exl2OldestMessage_Object = MibTableColumn
exl2OldestMessage = _Exl2OldestMessage_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 8, 1, 12),
    _Exl2OldestMessage_Type()
)
exl2OldestMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exl2OldestMessage.setStatus("current")
_Exl2ProtocolName_Type = WtcsDisplayString
_Exl2ProtocolName_Object = MibTableColumn
exl2ProtocolName = _Exl2ProtocolName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 8, 1, 13),
    _Exl2ProtocolName_Type()
)
exl2ProtocolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exl2ProtocolName.setStatus("current")
_Exl2Size_Type = WtcsDisplayString
_Exl2Size_Object = MibTableColumn
exl2Size = _Exl2Size_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 8, 1, 14),
    _Exl2Size_Type()
)
exl2Size.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exl2Size.setStatus("current")
_Exl2StateActive_Type = TruthValue
_Exl2StateActive_Object = MibTableColumn
exl2StateActive = _Exl2StateActive_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 8, 1, 15),
    _Exl2StateActive_Type()
)
exl2StateActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exl2StateActive.setStatus("current")
_Exl2StateFlags_Type = Gauge32
_Exl2StateFlags_Object = MibTableColumn
exl2StateFlags = _Exl2StateFlags_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 8, 1, 16),
    _Exl2StateFlags_Type()
)
exl2StateFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exl2StateFlags.setStatus("current")
_Exl2StateFrozen_Type = TruthValue
_Exl2StateFrozen_Object = MibTableColumn
exl2StateFrozen = _Exl2StateFrozen_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 8, 1, 17),
    _Exl2StateFrozen_Type()
)
exl2StateFrozen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exl2StateFrozen.setStatus("current")
_Exl2StateReady_Type = TruthValue
_Exl2StateReady_Object = MibTableColumn
exl2StateReady = _Exl2StateReady_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 8, 1, 18),
    _Exl2StateReady_Type()
)
exl2StateReady.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exl2StateReady.setStatus("current")
_Exl2StateRemote_Type = TruthValue
_Exl2StateRemote_Object = MibTableColumn
exl2StateRemote = _Exl2StateRemote_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 8, 1, 19),
    _Exl2StateRemote_Type()
)
exl2StateRemote.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exl2StateRemote.setStatus("current")
_Exl2StateRetry_Type = TruthValue
_Exl2StateRetry_Object = MibTableColumn
exl2StateRetry = _Exl2StateRetry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 8, 1, 20),
    _Exl2StateRetry_Type()
)
exl2StateRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exl2StateRetry.setStatus("current")
_Exl2StateScheduled_Type = TruthValue
_Exl2StateScheduled_Object = MibTableColumn
exl2StateScheduled = _Exl2StateScheduled_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 8, 1, 21),
    _Exl2StateScheduled_Type()
)
exl2StateScheduled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exl2StateScheduled.setStatus("current")
_Exl2SupportedLinkActions_Type = Gauge32
_Exl2SupportedLinkActions_Object = MibTableColumn
exl2SupportedLinkActions = _Exl2SupportedLinkActions_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 8, 1, 22),
    _Exl2SupportedLinkActions_Type()
)
exl2SupportedLinkActions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exl2SupportedLinkActions.setStatus("current")
_Exl2TypeCurrentlyUnreachable_Type = TruthValue
_Exl2TypeCurrentlyUnreachable_Object = MibTableColumn
exl2TypeCurrentlyUnreachable = _Exl2TypeCurrentlyUnreachable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 8, 1, 23),
    _Exl2TypeCurrentlyUnreachable_Type()
)
exl2TypeCurrentlyUnreachable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exl2TypeCurrentlyUnreachable.setStatus("current")
_Exl2TypeDeferredDelivery_Type = TruthValue
_Exl2TypeDeferredDelivery_Object = MibTableColumn
exl2TypeDeferredDelivery = _Exl2TypeDeferredDelivery_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 8, 1, 24),
    _Exl2TypeDeferredDelivery_Type()
)
exl2TypeDeferredDelivery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exl2TypeDeferredDelivery.setStatus("current")
_Exl2TypeInternal_Type = TruthValue
_Exl2TypeInternal_Object = MibTableColumn
exl2TypeInternal = _Exl2TypeInternal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 8, 1, 25),
    _Exl2TypeInternal_Type()
)
exl2TypeInternal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exl2TypeInternal.setStatus("current")
_Exl2TypeLocalDelivery_Type = TruthValue
_Exl2TypeLocalDelivery_Object = MibTableColumn
exl2TypeLocalDelivery = _Exl2TypeLocalDelivery_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 8, 1, 26),
    _Exl2TypeLocalDelivery_Type()
)
exl2TypeLocalDelivery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exl2TypeLocalDelivery.setStatus("current")
_Exl2TypePendingCategorization_Type = TruthValue
_Exl2TypePendingCategorization_Object = MibTableColumn
exl2TypePendingCategorization = _Exl2TypePendingCategorization_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 8, 1, 27),
    _Exl2TypePendingCategorization_Type()
)
exl2TypePendingCategorization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exl2TypePendingCategorization.setStatus("current")
_Exl2TypePendingRouting_Type = TruthValue
_Exl2TypePendingRouting_Object = MibTableColumn
exl2TypePendingRouting = _Exl2TypePendingRouting_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 8, 1, 28),
    _Exl2TypePendingRouting_Type()
)
exl2TypePendingRouting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exl2TypePendingRouting.setStatus("current")
_Exl2TypePendingSubmission_Type = TruthValue
_Exl2TypePendingSubmission_Object = MibTableColumn
exl2TypePendingSubmission = _Exl2TypePendingSubmission_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 8, 1, 29),
    _Exl2TypePendingSubmission_Type()
)
exl2TypePendingSubmission.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exl2TypePendingSubmission.setStatus("current")
_Exl2TypeRemoteDelivery_Type = TruthValue
_Exl2TypeRemoteDelivery_Object = MibTableColumn
exl2TypeRemoteDelivery = _Exl2TypeRemoteDelivery_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 8, 1, 30),
    _Exl2TypeRemoteDelivery_Type()
)
exl2TypeRemoteDelivery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exl2TypeRemoteDelivery.setStatus("current")
_Exl2Version_Type = Gauge32
_Exl2Version_Object = MibTableColumn
exl2Version = _Exl2Version_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 8, 1, 31),
    _Exl2Version_Type()
)
exl2Version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exl2Version.setStatus("current")
_Exl2VirtualMachine_Type = WtcsDisplayString
_Exl2VirtualMachine_Object = MibTableColumn
exl2VirtualMachine = _Exl2VirtualMachine_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 8, 1, 32),
    _Exl2VirtualMachine_Type()
)
exl2VirtualMachine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exl2VirtualMachine.setStatus("current")
_Exl2VirtualServerName_Type = WtcsDisplayString
_Exl2VirtualServerName_Object = MibTableColumn
exl2VirtualServerName = _Exl2VirtualServerName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 8, 1, 33),
    _Exl2VirtualServerName_Type()
)
exl2VirtualServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exl2VirtualServerName.setStatus("current")
_ExchangeLogonTable_Object = MibTable
exchangeLogonTable = _ExchangeLogonTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 9)
)
if mibBuilder.loadTexts:
    exchangeLogonTable.setStatus("current")
_ExchangeLogonEntry_Object = MibTableRow
exchangeLogonEntry = _ExchangeLogonEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 9, 1)
)
exchangeLogonEntry.setIndexNames(
    (0, "INFORMANT-WMI-EXCHANGE", "exloIndex"),
)
if mibBuilder.loadTexts:
    exchangeLogonEntry.setStatus("current")


class _ExloIndex_Type(Integer32):
    """Custom type exloIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ExloIndex_Type.__name__ = "Integer32"
_ExloIndex_Object = MibTableColumn
exloIndex = _ExloIndex_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 9, 1, 1),
    _ExloIndex_Type()
)
exloIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exloIndex.setStatus("current")
_ExloAdapterSpeed_Type = Gauge32
_ExloAdapterSpeed_Object = MibTableColumn
exloAdapterSpeed = _ExloAdapterSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 9, 1, 2),
    _ExloAdapterSpeed_Type()
)
exloAdapterSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exloAdapterSpeed.setStatus("current")
if mibBuilder.loadTexts:
    exloAdapterSpeed.setUnits("Kbits/s")
_ExloClientIP_Type = WtcsDisplayString
_ExloClientIP_Object = MibTableColumn
exloClientIP = _ExloClientIP_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 9, 1, 3),
    _ExloClientIP_Type()
)
exloClientIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exloClientIP.setStatus("current")


class _ExloClientMode_Type(Integer32):
    """Custom type exloClientMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cached", 2),
          ("classicOnline", 1))
    )


_ExloClientMode_Type.__name__ = "Integer32"
_ExloClientMode_Object = MibTableColumn
exloClientMode = _ExloClientMode_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 9, 1, 4),
    _ExloClientMode_Type()
)
exloClientMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exloClientMode.setStatus("current")
_ExloClientName_Type = WtcsDisplayString
_ExloClientName_Object = MibTableColumn
exloClientName = _ExloClientName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 9, 1, 5),
    _ExloClientName_Type()
)
exloClientName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exloClientName.setStatus("current")
_ExloClientVersion_Type = WtcsDisplayString
_ExloClientVersion_Object = MibTableColumn
exloClientVersion = _ExloClientVersion_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 9, 1, 6),
    _ExloClientVersion_Type()
)
exloClientVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exloClientVersion.setStatus("current")
_ExloCodePageID_Type = Gauge32
_ExloCodePageID_Object = MibTableColumn
exloCodePageID = _ExloCodePageID_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 9, 1, 7),
    _ExloCodePageID_Type()
)
exloCodePageID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exloCodePageID.setStatus("current")
_ExloFolderOperationRate_Type = Gauge32
_ExloFolderOperationRate_Object = MibTableColumn
exloFolderOperationRate = _ExloFolderOperationRate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 9, 1, 8),
    _ExloFolderOperationRate_Type()
)
exloFolderOperationRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exloFolderOperationRate.setStatus("current")
if mibBuilder.loadTexts:
    exloFolderOperationRate.setUnits("per second")
_ExloHostAddress_Type = WtcsDisplayString
_ExloHostAddress_Object = MibTableColumn
exloHostAddress = _ExloHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 9, 1, 9),
    _ExloHostAddress_Type()
)
exloHostAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exloHostAddress.setStatus("current")
_ExloLastOperationTime_Type = DateAndTime
_ExloLastOperationTime_Object = MibTableColumn
exloLastOperationTime = _ExloLastOperationTime_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 9, 1, 10),
    _ExloLastOperationTime_Type()
)
exloLastOperationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exloLastOperationTime.setStatus("current")
_ExloLatency_Type = Gauge32
_ExloLatency_Object = MibTableColumn
exloLatency = _ExloLatency_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 9, 1, 11),
    _ExloLatency_Type()
)
exloLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exloLatency.setStatus("current")
if mibBuilder.loadTexts:
    exloLatency.setUnits("msec")
_ExloLocaleID_Type = Gauge32
_ExloLocaleID_Object = MibTableColumn
exloLocaleID = _ExloLocaleID_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 9, 1, 12),
    _ExloLocaleID_Type()
)
exloLocaleID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exloLocaleID.setStatus("current")
_ExloLoggedOnUserAccount_Type = WtcsDisplayString
_ExloLoggedOnUserAccount_Object = MibTableColumn
exloLoggedOnUserAccount = _ExloLoggedOnUserAccount_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 9, 1, 13),
    _ExloLoggedOnUserAccount_Type()
)
exloLoggedOnUserAccount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exloLoggedOnUserAccount.setStatus("current")
_ExloLoggedOnUsersMailboxLegacyDN_Type = WtcsDisplayString
_ExloLoggedOnUsersMailboxLegacyDN_Object = MibTableColumn
exloLoggedOnUsersMailboxLegacyDN = _ExloLoggedOnUsersMailboxLegacyDN_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 9, 1, 14),
    _ExloLoggedOnUsersMailboxLegacyDN_Type()
)
exloLoggedOnUsersMailboxLegacyDN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exloLoggedOnUsersMailboxLegacyDN.setStatus("current")
_ExloLogonTime_Type = DateAndTime
_ExloLogonTime_Object = MibTableColumn
exloLogonTime = _ExloLogonTime_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 9, 1, 15),
    _ExloLogonTime_Type()
)
exloLogonTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exloLogonTime.setStatus("current")
_ExloMacAddress_Type = WtcsDisplayString
_ExloMacAddress_Object = MibTableColumn
exloMacAddress = _ExloMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 9, 1, 16),
    _ExloMacAddress_Type()
)
exloMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exloMacAddress.setStatus("current")
_ExloMailboxDisplayName_Type = WtcsDisplayString
_ExloMailboxDisplayName_Object = MibTableColumn
exloMailboxDisplayName = _ExloMailboxDisplayName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 9, 1, 17),
    _ExloMailboxDisplayName_Type()
)
exloMailboxDisplayName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exloMailboxDisplayName.setStatus("current")
_ExloMailboxLegacyDN_Type = WtcsDisplayString
_ExloMailboxLegacyDN_Object = MibTableColumn
exloMailboxLegacyDN = _ExloMailboxLegacyDN_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 9, 1, 18),
    _ExloMailboxLegacyDN_Type()
)
exloMailboxLegacyDN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exloMailboxLegacyDN.setStatus("current")
_ExloMessagingOperationRate_Type = Gauge32
_ExloMessagingOperationRate_Object = MibTableColumn
exloMessagingOperationRate = _ExloMessagingOperationRate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 9, 1, 19),
    _ExloMessagingOperationRate_Type()
)
exloMessagingOperationRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exloMessagingOperationRate.setStatus("current")
if mibBuilder.loadTexts:
    exloMessagingOperationRate.setUnits("per second")
_ExloOpenAttachmentCount_Type = Gauge32
_ExloOpenAttachmentCount_Object = MibTableColumn
exloOpenAttachmentCount = _ExloOpenAttachmentCount_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 9, 1, 20),
    _ExloOpenAttachmentCount_Type()
)
exloOpenAttachmentCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exloOpenAttachmentCount.setStatus("current")
_ExloOpenFolderCount_Type = Gauge32
_ExloOpenFolderCount_Object = MibTableColumn
exloOpenFolderCount = _ExloOpenFolderCount_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 9, 1, 21),
    _ExloOpenFolderCount_Type()
)
exloOpenFolderCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exloOpenFolderCount.setStatus("current")
_ExloOpenMessageCount_Type = Gauge32
_ExloOpenMessageCount_Object = MibTableColumn
exloOpenMessageCount = _ExloOpenMessageCount_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 9, 1, 22),
    _ExloOpenMessageCount_Type()
)
exloOpenMessageCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exloOpenMessageCount.setStatus("current")
_ExloOtherOperationRate_Type = Gauge32
_ExloOtherOperationRate_Object = MibTableColumn
exloOtherOperationRate = _ExloOtherOperationRate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 9, 1, 23),
    _ExloOtherOperationRate_Type()
)
exloOtherOperationRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exloOtherOperationRate.setStatus("current")
if mibBuilder.loadTexts:
    exloOtherOperationRate.setUnits("per second")
_ExloProgressOperationRate_Type = Gauge32
_ExloProgressOperationRate_Object = MibTableColumn
exloProgressOperationRate = _ExloProgressOperationRate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 9, 1, 24),
    _ExloProgressOperationRate_Type()
)
exloProgressOperationRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exloProgressOperationRate.setStatus("current")
if mibBuilder.loadTexts:
    exloProgressOperationRate.setUnits("per second")
_ExloRowID_Type = Gauge32
_ExloRowID_Object = MibTableColumn
exloRowID = _ExloRowID_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 9, 1, 25),
    _ExloRowID_Type()
)
exloRowID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exloRowID.setStatus("current")
_ExloRPCSucceeded_Type = Integer32
_ExloRPCSucceeded_Object = MibTableColumn
exloRPCSucceeded = _ExloRPCSucceeded_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 9, 1, 26),
    _ExloRPCSucceeded_Type()
)
exloRPCSucceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exloRPCSucceeded.setStatus("current")
_ExloServerName_Type = WtcsDisplayString
_ExloServerName_Object = MibTableColumn
exloServerName = _ExloServerName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 9, 1, 27),
    _ExloServerName_Type()
)
exloServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exloServerName.setStatus("current")
_ExloStorageGroupName_Type = WtcsDisplayString
_ExloStorageGroupName_Object = MibTableColumn
exloStorageGroupName = _ExloStorageGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 9, 1, 28),
    _ExloStorageGroupName_Type()
)
exloStorageGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exloStorageGroupName.setStatus("current")
_ExloStoreName_Type = WtcsDisplayString
_ExloStoreName_Object = MibTableColumn
exloStoreName = _ExloStoreName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 9, 1, 29),
    _ExloStoreName_Type()
)
exloStoreName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exloStoreName.setStatus("current")


class _ExloStoreType_Type(Integer32):
    """Custom type exloStoreType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mailboxStore", 1),
          ("publicStore", 2))
    )


_ExloStoreType_Type.__name__ = "Integer32"
_ExloStoreType_Object = MibTableColumn
exloStoreType = _ExloStoreType_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 9, 1, 30),
    _ExloStoreType_Type()
)
exloStoreType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exloStoreType.setStatus("current")
_ExloStreamOperationRate_Type = Gauge32
_ExloStreamOperationRate_Object = MibTableColumn
exloStreamOperationRate = _ExloStreamOperationRate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 9, 1, 31),
    _ExloStreamOperationRate_Type()
)
exloStreamOperationRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exloStreamOperationRate.setStatus("current")
if mibBuilder.loadTexts:
    exloStreamOperationRate.setUnits("per second")
_ExloTableOperationRate_Type = Gauge32
_ExloTableOperationRate_Object = MibTableColumn
exloTableOperationRate = _ExloTableOperationRate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 9, 1, 32),
    _ExloTableOperationRate_Type()
)
exloTableOperationRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exloTableOperationRate.setStatus("current")
if mibBuilder.loadTexts:
    exloTableOperationRate.setUnits("per second")
_ExloTotalOperationRate_Type = Gauge32
_ExloTotalOperationRate_Object = MibTableColumn
exloTotalOperationRate = _ExloTotalOperationRate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 9, 1, 33),
    _ExloTotalOperationRate_Type()
)
exloTotalOperationRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exloTotalOperationRate.setStatus("current")
if mibBuilder.loadTexts:
    exloTotalOperationRate.setUnits("per second")
_ExloTransferOperationRate_Type = Gauge32
_ExloTransferOperationRate_Object = MibTableColumn
exloTransferOperationRate = _ExloTransferOperationRate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 9, 1, 34),
    _ExloTransferOperationRate_Type()
)
exloTransferOperationRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exloTransferOperationRate.setStatus("current")
if mibBuilder.loadTexts:
    exloTransferOperationRate.setUnits("per second")
_ExchangeMailboxTable_Object = MibTable
exchangeMailboxTable = _ExchangeMailboxTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 10)
)
if mibBuilder.loadTexts:
    exchangeMailboxTable.setStatus("current")
_ExchangeMailboxEntry_Object = MibTableRow
exchangeMailboxEntry = _ExchangeMailboxEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 10, 1)
)
exchangeMailboxEntry.setIndexNames(
    (0, "INFORMANT-WMI-EXCHANGE", "exmIndex"),
)
if mibBuilder.loadTexts:
    exchangeMailboxEntry.setStatus("current")


class _ExmIndex_Type(Integer32):
    """Custom type exmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ExmIndex_Type.__name__ = "Integer32"
_ExmIndex_Object = MibTableColumn
exmIndex = _ExmIndex_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 10, 1, 1),
    _ExmIndex_Type()
)
exmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exmIndex.setStatus("current")
_ExmAssocContentCount_Type = Gauge32
_ExmAssocContentCount_Object = MibTableColumn
exmAssocContentCount = _ExmAssocContentCount_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 10, 1, 2),
    _ExmAssocContentCount_Type()
)
exmAssocContentCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exmAssocContentCount.setStatus("current")
_ExmDateDiscoveredAbsentInDS_Type = DateAndTime
_ExmDateDiscoveredAbsentInDS_Object = MibTableColumn
exmDateDiscoveredAbsentInDS = _ExmDateDiscoveredAbsentInDS_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 10, 1, 3),
    _ExmDateDiscoveredAbsentInDS_Type()
)
exmDateDiscoveredAbsentInDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exmDateDiscoveredAbsentInDS.setStatus("current")
_ExmDeletedMessageSizeExtended_Type = WtcsDisplayString
_ExmDeletedMessageSizeExtended_Object = MibTableColumn
exmDeletedMessageSizeExtended = _ExmDeletedMessageSizeExtended_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 10, 1, 4),
    _ExmDeletedMessageSizeExtended_Type()
)
exmDeletedMessageSizeExtended.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exmDeletedMessageSizeExtended.setStatus("current")
if mibBuilder.loadTexts:
    exmDeletedMessageSizeExtended.setUnits("Bytes")
_ExmLastLoggedOnUserAccount_Type = WtcsDisplayString
_ExmLastLoggedOnUserAccount_Object = MibTableColumn
exmLastLoggedOnUserAccount = _ExmLastLoggedOnUserAccount_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 10, 1, 5),
    _ExmLastLoggedOnUserAccount_Type()
)
exmLastLoggedOnUserAccount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exmLastLoggedOnUserAccount.setStatus("current")
_ExmLastLogoffTime_Type = DateAndTime
_ExmLastLogoffTime_Object = MibTableColumn
exmLastLogoffTime = _ExmLastLogoffTime_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 10, 1, 6),
    _ExmLastLogoffTime_Type()
)
exmLastLogoffTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exmLastLogoffTime.setStatus("current")
_ExmLastLogonTime_Type = DateAndTime
_ExmLastLogonTime_Object = MibTableColumn
exmLastLogonTime = _ExmLastLogonTime_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 10, 1, 7),
    _ExmLastLogonTime_Type()
)
exmLastLogonTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exmLastLogonTime.setStatus("current")
_ExmLegacyDN_Type = WtcsDisplayString
_ExmLegacyDN_Object = MibTableColumn
exmLegacyDN = _ExmLegacyDN_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 10, 1, 8),
    _ExmLegacyDN_Type()
)
exmLegacyDN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exmLegacyDN.setStatus("current")
_ExmMailboxDisplayName_Type = WtcsDisplayString
_ExmMailboxDisplayName_Object = MibTableColumn
exmMailboxDisplayName = _ExmMailboxDisplayName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 10, 1, 9),
    _ExmMailboxDisplayName_Type()
)
exmMailboxDisplayName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exmMailboxDisplayName.setStatus("current")
_ExmMailboxGUID_Type = WtcsDisplayString
_ExmMailboxGUID_Object = MibTableColumn
exmMailboxGUID = _ExmMailboxGUID_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 10, 1, 10),
    _ExmMailboxGUID_Type()
)
exmMailboxGUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exmMailboxGUID.setStatus("current")
_ExmServerName_Type = WtcsDisplayString
_ExmServerName_Object = MibTableColumn
exmServerName = _ExmServerName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 10, 1, 11),
    _ExmServerName_Type()
)
exmServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exmServerName.setStatus("current")
_ExmSize_Type = WtcsDisplayString
_ExmSize_Object = MibTableColumn
exmSize = _ExmSize_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 10, 1, 12),
    _ExmSize_Type()
)
exmSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exmSize.setStatus("current")
if mibBuilder.loadTexts:
    exmSize.setUnits("Bytes")
_ExmStorageGroupName_Type = WtcsDisplayString
_ExmStorageGroupName_Object = MibTableColumn
exmStorageGroupName = _ExmStorageGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 10, 1, 13),
    _ExmStorageGroupName_Type()
)
exmStorageGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exmStorageGroupName.setStatus("current")


class _ExmStorageLimitInfo_Type(Integer32):
    """Custom type exmStorageLimitInfo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16)
        )
    )
    namedValues = NamedValues(
        *(("belowLimit", 1),
          ("issueWarning", 2),
          ("mailboxDisabled", 16),
          ("noChecking", 8),
          ("prohibitSend", 4))
    )


_ExmStorageLimitInfo_Type.__name__ = "Integer32"
_ExmStorageLimitInfo_Object = MibTableColumn
exmStorageLimitInfo = _ExmStorageLimitInfo_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 10, 1, 14),
    _ExmStorageLimitInfo_Type()
)
exmStorageLimitInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exmStorageLimitInfo.setStatus("current")
_ExmStoreName_Type = WtcsDisplayString
_ExmStoreName_Object = MibTableColumn
exmStoreName = _ExmStoreName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 10, 1, 15),
    _ExmStoreName_Type()
)
exmStoreName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exmStoreName.setStatus("current")
_ExmTotalItems_Type = Gauge32
_ExmTotalItems_Object = MibTableColumn
exmTotalItems = _ExmTotalItems_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 10, 1, 16),
    _ExmTotalItems_Type()
)
exmTotalItems.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exmTotalItems.setStatus("current")
_ExchangeMessageTrackingTable_Object = MibTable
exchangeMessageTrackingTable = _ExchangeMessageTrackingTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 11)
)
if mibBuilder.loadTexts:
    exchangeMessageTrackingTable.setStatus("current")
_ExchangeMessageTrackingEntry_Object = MibTableRow
exchangeMessageTrackingEntry = _ExchangeMessageTrackingEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 11, 1)
)
exchangeMessageTrackingEntry.setIndexNames(
    (0, "INFORMANT-WMI-EXCHANGE", "exmtIndex"),
)
if mibBuilder.loadTexts:
    exchangeMessageTrackingEntry.setStatus("current")


class _ExmtIndex_Type(Integer32):
    """Custom type exmtIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ExmtIndex_Type.__name__ = "Integer32"
_ExmtIndex_Object = MibTableColumn
exmtIndex = _ExmtIndex_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 11, 1, 1),
    _ExmtIndex_Type()
)
exmtIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exmtIndex.setStatus("current")
_ExmtAttemptedPartnerServer_Type = WtcsDisplayString
_ExmtAttemptedPartnerServer_Object = MibTableColumn
exmtAttemptedPartnerServer = _ExmtAttemptedPartnerServer_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 11, 1, 2),
    _ExmtAttemptedPartnerServer_Type()
)
exmtAttemptedPartnerServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exmtAttemptedPartnerServer.setStatus("current")
_ExmtClientIP_Type = WtcsDisplayString
_ExmtClientIP_Object = MibTableColumn
exmtClientIP = _ExmtClientIP_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 11, 1, 3),
    _ExmtClientIP_Type()
)
exmtClientIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exmtClientIP.setStatus("current")
_ExmtClientName_Type = WtcsDisplayString
_ExmtClientName_Object = MibTableColumn
exmtClientName = _ExmtClientName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 11, 1, 4),
    _ExmtClientName_Type()
)
exmtClientName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exmtClientName.setStatus("current")
_ExmtCost_Type = Gauge32
_ExmtCost_Object = MibTableColumn
exmtCost = _ExmtCost_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 11, 1, 5),
    _ExmtCost_Type()
)
exmtCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exmtCost.setStatus("current")
_ExmtDeliveryTime_Type = Gauge32
_ExmtDeliveryTime_Object = MibTableColumn
exmtDeliveryTime = _ExmtDeliveryTime_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 11, 1, 6),
    _ExmtDeliveryTime_Type()
)
exmtDeliveryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exmtDeliveryTime.setStatus("current")
if mibBuilder.loadTexts:
    exmtDeliveryTime.setUnits("seconds")
_ExmtEncrypted_Type = TruthValue
_ExmtEncrypted_Object = MibTableColumn
exmtEncrypted = _ExmtEncrypted_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 11, 1, 7),
    _ExmtEncrypted_Type()
)
exmtEncrypted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exmtEncrypted.setStatus("current")
_ExmtEntryType_Type = Gauge32
_ExmtEntryType_Object = MibTableColumn
exmtEntryType = _ExmtEntryType_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 11, 1, 8),
    _ExmtEntryType_Type()
)
exmtEntryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exmtEntryType.setStatus("current")
_ExmtExpansionDL_Type = WtcsDisplayString
_ExmtExpansionDL_Object = MibTableColumn
exmtExpansionDL = _ExmtExpansionDL_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 11, 1, 9),
    _ExmtExpansionDL_Type()
)
exmtExpansionDL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exmtExpansionDL.setStatus("current")
_ExmtKeyID_Type = WtcsDisplayString
_ExmtKeyID_Object = MibTableColumn
exmtKeyID = _ExmtKeyID_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 11, 1, 10),
    _ExmtKeyID_Type()
)
exmtKeyID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exmtKeyID.setStatus("current")
_ExmtLinkedMessageID_Type = WtcsDisplayString
_ExmtLinkedMessageID_Object = MibTableColumn
exmtLinkedMessageID = _ExmtLinkedMessageID_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 11, 1, 11),
    _ExmtLinkedMessageID_Type()
)
exmtLinkedMessageID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exmtLinkedMessageID.setStatus("current")
_ExmtMessageID_Type = WtcsDisplayString
_ExmtMessageID_Object = MibTableColumn
exmtMessageID = _ExmtMessageID_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 11, 1, 12),
    _ExmtMessageID_Type()
)
exmtMessageID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exmtMessageID.setStatus("current")
_ExmtOriginationTime_Type = DateAndTime
_ExmtOriginationTime_Object = MibTableColumn
exmtOriginationTime = _ExmtOriginationTime_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 11, 1, 13),
    _ExmtOriginationTime_Type()
)
exmtOriginationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exmtOriginationTime.setStatus("current")
_ExmtPartnerServer_Type = WtcsDisplayString
_ExmtPartnerServer_Object = MibTableColumn
exmtPartnerServer = _ExmtPartnerServer_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 11, 1, 14),
    _ExmtPartnerServer_Type()
)
exmtPartnerServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exmtPartnerServer.setStatus("current")
_ExmtPriority_Type = Gauge32
_ExmtPriority_Object = MibTableColumn
exmtPriority = _ExmtPriority_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 11, 1, 15),
    _ExmtPriority_Type()
)
exmtPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exmtPriority.setStatus("current")
_ExmtRecipientAddress_Type = WtcsDisplayString
_ExmtRecipientAddress_Object = MibTableColumn
exmtRecipientAddress = _ExmtRecipientAddress_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 11, 1, 16),
    _ExmtRecipientAddress_Type()
)
exmtRecipientAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exmtRecipientAddress.setStatus("current")
_ExmtRecipientCount_Type = Gauge32
_ExmtRecipientCount_Object = MibTableColumn
exmtRecipientCount = _ExmtRecipientCount_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 11, 1, 17),
    _ExmtRecipientCount_Type()
)
exmtRecipientCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exmtRecipientCount.setStatus("current")
_ExmtRecipientStatus_Type = Gauge32
_ExmtRecipientStatus_Object = MibTableColumn
exmtRecipientStatus = _ExmtRecipientStatus_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 11, 1, 18),
    _ExmtRecipientStatus_Type()
)
exmtRecipientStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exmtRecipientStatus.setStatus("current")
_ExmtSenderAddress_Type = WtcsDisplayString
_ExmtSenderAddress_Object = MibTableColumn
exmtSenderAddress = _ExmtSenderAddress_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 11, 1, 19),
    _ExmtSenderAddress_Type()
)
exmtSenderAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exmtSenderAddress.setStatus("current")
_ExmtServerIP_Type = WtcsDisplayString
_ExmtServerIP_Object = MibTableColumn
exmtServerIP = _ExmtServerIP_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 11, 1, 20),
    _ExmtServerIP_Type()
)
exmtServerIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exmtServerIP.setStatus("current")
_ExmtServerName_Type = WtcsDisplayString
_ExmtServerName_Object = MibTableColumn
exmtServerName = _ExmtServerName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 11, 1, 21),
    _ExmtServerName_Type()
)
exmtServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exmtServerName.setStatus("current")
_ExmtSize_Type = Gauge32
_ExmtSize_Object = MibTableColumn
exmtSize = _ExmtSize_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 11, 1, 22),
    _ExmtSize_Type()
)
exmtSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exmtSize.setStatus("current")
_ExmtSubject_Type = WtcsDisplayString
_ExmtSubject_Object = MibTableColumn
exmtSubject = _ExmtSubject_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 11, 1, 23),
    _ExmtSubject_Type()
)
exmtSubject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exmtSubject.setStatus("current")
_ExmtSubjectID_Type = WtcsDisplayString
_ExmtSubjectID_Object = MibTableColumn
exmtSubjectID = _ExmtSubjectID_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 11, 1, 24),
    _ExmtSubjectID_Type()
)
exmtSubjectID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exmtSubjectID.setStatus("current")
_ExmtTimeLogged_Type = DateAndTime
_ExmtTimeLogged_Object = MibTableColumn
exmtTimeLogged = _ExmtTimeLogged_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 11, 1, 25),
    _ExmtTimeLogged_Type()
)
exmtTimeLogged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exmtTimeLogged.setStatus("current")
_ExmtVersion_Type = WtcsDisplayString
_ExmtVersion_Object = MibTableColumn
exmtVersion = _ExmtVersion_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 11, 1, 26),
    _ExmtVersion_Type()
)
exmtVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exmtVersion.setStatus("current")
_ExchangePublicFolderTable_Object = MibTable
exchangePublicFolderTable = _ExchangePublicFolderTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 12)
)
if mibBuilder.loadTexts:
    exchangePublicFolderTable.setStatus("current")
_ExchangePublicFolderEntry_Object = MibTableRow
exchangePublicFolderEntry = _ExchangePublicFolderEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 12, 1)
)
exchangePublicFolderEntry.setIndexNames(
    (0, "INFORMANT-WMI-EXCHANGE", "expfIndex"),
)
if mibBuilder.loadTexts:
    exchangePublicFolderEntry.setStatus("current")


class _ExpfIndex_Type(Integer32):
    """Custom type expfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ExpfIndex_Type.__name__ = "Integer32"
_ExpfIndex_Object = MibTableColumn
expfIndex = _ExpfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 12, 1, 1),
    _ExpfIndex_Type()
)
expfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expfIndex.setStatus("current")
_ExpfAddressBookName_Type = WtcsDisplayString
_ExpfAddressBookName_Object = MibTableColumn
expfAddressBookName = _ExpfAddressBookName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 12, 1, 2),
    _ExpfAddressBookName_Type()
)
expfAddressBookName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expfAddressBookName.setStatus("current")
_ExpfAdministrativeNote_Type = WtcsDisplayString
_ExpfAdministrativeNote_Object = MibTableColumn
expfAdministrativeNote = _ExpfAdministrativeNote_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 12, 1, 3),
    _ExpfAdministrativeNote_Type()
)
expfAdministrativeNote.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expfAdministrativeNote.setStatus("current")
_ExpfAdminSecurityDescriptor_Type = WtcsDisplayString
_ExpfAdminSecurityDescriptor_Object = MibTableColumn
expfAdminSecurityDescriptor = _ExpfAdminSecurityDescriptor_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 12, 1, 4),
    _ExpfAdminSecurityDescriptor_Type()
)
expfAdminSecurityDescriptor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expfAdminSecurityDescriptor.setStatus("current")
_ExpfADProxyPath_Type = WtcsDisplayString
_ExpfADProxyPath_Object = MibTableColumn
expfADProxyPath = _ExpfADProxyPath_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 12, 1, 5),
    _ExpfADProxyPath_Type()
)
expfADProxyPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expfADProxyPath.setStatus("current")
_ExpfAssociatedMessageCount_Type = Gauge32
_ExpfAssociatedMessageCount_Object = MibTableColumn
expfAssociatedMessageCount = _ExpfAssociatedMessageCount_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 12, 1, 6),
    _ExpfAssociatedMessageCount_Type()
)
expfAssociatedMessageCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expfAssociatedMessageCount.setStatus("current")
_ExpfAttachmentCount_Type = Gauge32
_ExpfAttachmentCount_Object = MibTableColumn
expfAttachmentCount = _ExpfAttachmentCount_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 12, 1, 7),
    _ExpfAttachmentCount_Type()
)
expfAttachmentCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expfAttachmentCount.setStatus("current")
_ExpfCategorizationCount_Type = Gauge32
_ExpfCategorizationCount_Object = MibTableColumn
expfCategorizationCount = _ExpfCategorizationCount_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 12, 1, 8),
    _ExpfCategorizationCount_Type()
)
expfCategorizationCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expfCategorizationCount.setStatus("current")
_ExpfComment_Type = WtcsDisplayString
_ExpfComment_Object = MibTableColumn
expfComment = _ExpfComment_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 12, 1, 9),
    _ExpfComment_Type()
)
expfComment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expfComment.setStatus("current")
_ExpfContactCount_Type = Gauge32
_ExpfContactCount_Object = MibTableColumn
expfContactCount = _ExpfContactCount_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 12, 1, 10),
    _ExpfContactCount_Type()
)
expfContactCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expfContactCount.setStatus("current")
_ExpfContainsRules_Type = TruthValue
_ExpfContainsRules_Object = MibTableColumn
expfContainsRules = _ExpfContainsRules_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 12, 1, 11),
    _ExpfContainsRules_Type()
)
expfContainsRules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expfContainsRules.setStatus("current")
_ExpfCreationTime_Type = DateAndTime
_ExpfCreationTime_Object = MibTableColumn
expfCreationTime = _ExpfCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 12, 1, 12),
    _ExpfCreationTime_Type()
)
expfCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expfCreationTime.setStatus("current")
_ExpfDeletedItemLifetime_Type = Gauge32
_ExpfDeletedItemLifetime_Object = MibTableColumn
expfDeletedItemLifetime = _ExpfDeletedItemLifetime_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 12, 1, 13),
    _ExpfDeletedItemLifetime_Type()
)
expfDeletedItemLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expfDeletedItemLifetime.setStatus("current")
if mibBuilder.loadTexts:
    expfDeletedItemLifetime.setUnits("days")
_ExpfFolderTree_Type = WtcsDisplayString
_ExpfFolderTree_Object = MibTableColumn
expfFolderTree = _ExpfFolderTree_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 12, 1, 14),
    _ExpfFolderTree_Type()
)
expfFolderTree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expfFolderTree.setStatus("current")
_ExpfFriendlyUrl_Type = WtcsDisplayString
_ExpfFriendlyUrl_Object = MibTableColumn
expfFriendlyUrl = _ExpfFriendlyUrl_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 12, 1, 15),
    _ExpfFriendlyUrl_Type()
)
expfFriendlyUrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expfFriendlyUrl.setStatus("current")
_ExpfHasChildren_Type = TruthValue
_ExpfHasChildren_Object = MibTableColumn
expfHasChildren = _ExpfHasChildren_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 12, 1, 16),
    _ExpfHasChildren_Type()
)
expfHasChildren.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expfHasChildren.setStatus("current")
_ExpfHasLocalReplica_Type = TruthValue
_ExpfHasLocalReplica_Object = MibTableColumn
expfHasLocalReplica = _ExpfHasLocalReplica_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 12, 1, 17),
    _ExpfHasLocalReplica_Type()
)
expfHasLocalReplica.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expfHasLocalReplica.setStatus("current")
_ExpfIsMailEnabled_Type = TruthValue
_ExpfIsMailEnabled_Object = MibTableColumn
expfIsMailEnabled = _ExpfIsMailEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 12, 1, 18),
    _ExpfIsMailEnabled_Type()
)
expfIsMailEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expfIsMailEnabled.setStatus("current")
_ExpfIsNormalFolder_Type = TruthValue
_ExpfIsNormalFolder_Object = MibTableColumn
expfIsNormalFolder = _ExpfIsNormalFolder_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 12, 1, 19),
    _ExpfIsNormalFolder_Type()
)
expfIsNormalFolder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expfIsNormalFolder.setStatus("current")
_ExpfIsPerUserReadDisabled_Type = TruthValue
_ExpfIsPerUserReadDisabled_Object = MibTableColumn
expfIsPerUserReadDisabled = _ExpfIsPerUserReadDisabled_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 12, 1, 20),
    _ExpfIsPerUserReadDisabled_Type()
)
expfIsPerUserReadDisabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expfIsPerUserReadDisabled.setStatus("current")
_ExpfIsSearchFolder_Type = TruthValue
_ExpfIsSearchFolder_Object = MibTableColumn
expfIsSearchFolder = _ExpfIsSearchFolder_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 12, 1, 21),
    _ExpfIsSearchFolder_Type()
)
expfIsSearchFolder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expfIsSearchFolder.setStatus("current")
_ExpfIsSecureInSite_Type = TruthValue
_ExpfIsSecureInSite_Object = MibTableColumn
expfIsSecureInSite = _ExpfIsSecureInSite_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 12, 1, 22),
    _ExpfIsSecureInSite_Type()
)
expfIsSecureInSite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expfIsSecureInSite.setStatus("current")
_ExpfLastAccessTime_Type = DateAndTime
_ExpfLastAccessTime_Object = MibTableColumn
expfLastAccessTime = _ExpfLastAccessTime_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 12, 1, 23),
    _ExpfLastAccessTime_Type()
)
expfLastAccessTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expfLastAccessTime.setStatus("current")
_ExpfLastModificationTime_Type = DateAndTime
_ExpfLastModificationTime_Object = MibTableColumn
expfLastModificationTime = _ExpfLastModificationTime_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 12, 1, 24),
    _ExpfLastModificationTime_Type()
)
expfLastModificationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expfLastModificationTime.setStatus("current")
_ExpfMaximumItemSize_Type = Gauge32
_ExpfMaximumItemSize_Object = MibTableColumn
expfMaximumItemSize = _ExpfMaximumItemSize_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 12, 1, 25),
    _ExpfMaximumItemSize_Type()
)
expfMaximumItemSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expfMaximumItemSize.setStatus("current")
if mibBuilder.loadTexts:
    expfMaximumItemSize.setUnits("KB")
_ExpfMessageCount_Type = Gauge32
_ExpfMessageCount_Object = MibTableColumn
expfMessageCount = _ExpfMessageCount_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 12, 1, 26),
    _ExpfMessageCount_Type()
)
expfMessageCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expfMessageCount.setStatus("current")
_ExpfMessageWithAttachmentsCount_Type = Gauge32
_ExpfMessageWithAttachmentsCount_Object = MibTableColumn
expfMessageWithAttachmentsCount = _ExpfMessageWithAttachmentsCount_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 12, 1, 27),
    _ExpfMessageWithAttachmentsCount_Type()
)
expfMessageWithAttachmentsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expfMessageWithAttachmentsCount.setStatus("current")
_ExpfName_Type = WtcsDisplayString
_ExpfName_Object = MibTableColumn
expfName = _ExpfName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 12, 1, 28),
    _ExpfName_Type()
)
expfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expfName.setStatus("current")
_ExpfNormalMessageSize_Type = Gauge32
_ExpfNormalMessageSize_Object = MibTableColumn
expfNormalMessageSize = _ExpfNormalMessageSize_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 12, 1, 29),
    _ExpfNormalMessageSize_Type()
)
expfNormalMessageSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expfNormalMessageSize.setStatus("current")
if mibBuilder.loadTexts:
    expfNormalMessageSize.setUnits("bytes")
_ExpfOwnerCount_Type = Gauge32
_ExpfOwnerCount_Object = MibTableColumn
expfOwnerCount = _ExpfOwnerCount_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 12, 1, 30),
    _ExpfOwnerCount_Type()
)
expfOwnerCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expfOwnerCount.setStatus("current")
_ExpfParentFriendlyUrl_Type = WtcsDisplayString
_ExpfParentFriendlyUrl_Object = MibTableColumn
expfParentFriendlyUrl = _ExpfParentFriendlyUrl_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 12, 1, 31),
    _ExpfParentFriendlyUrl_Type()
)
expfParentFriendlyUrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expfParentFriendlyUrl.setStatus("current")
_ExpfPath_Type = WtcsDisplayString
_ExpfPath_Object = MibTableColumn
expfPath = _ExpfPath_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 12, 1, 32),
    _ExpfPath_Type()
)
expfPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expfPath.setStatus("current")
_ExpfProhibitPostLimit_Type = Gauge32
_ExpfProhibitPostLimit_Object = MibTableColumn
expfProhibitPostLimit = _ExpfProhibitPostLimit_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 12, 1, 33),
    _ExpfProhibitPostLimit_Type()
)
expfProhibitPostLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expfProhibitPostLimit.setStatus("current")
if mibBuilder.loadTexts:
    expfProhibitPostLimit.setUnits("KB")
_ExpfPublishInAddressBook_Type = TruthValue
_ExpfPublishInAddressBook_Object = MibTableColumn
expfPublishInAddressBook = _ExpfPublishInAddressBook_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 12, 1, 34),
    _ExpfPublishInAddressBook_Type()
)
expfPublishInAddressBook.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expfPublishInAddressBook.setStatus("current")
_ExpfRecipientCountOnAssociateMsg_Type = Gauge32
_ExpfRecipientCountOnAssociateMsg_Object = MibTableColumn
expfRecipientCountOnAssociateMsg = _ExpfRecipientCountOnAssociateMsg_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 12, 1, 35),
    _ExpfRecipientCountOnAssociateMsg_Type()
)
expfRecipientCountOnAssociateMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expfRecipientCountOnAssociateMsg.setStatus("current")
_ExpfRecipientCountOnNormalMsg_Type = Gauge32
_ExpfRecipientCountOnNormalMsg_Object = MibTableColumn
expfRecipientCountOnNormalMsg = _ExpfRecipientCountOnNormalMsg_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 12, 1, 36),
    _ExpfRecipientCountOnNormalMsg_Type()
)
expfRecipientCountOnNormalMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expfRecipientCountOnNormalMsg.setStatus("current")
_ExpfReplicaAgeLimit_Type = Gauge32
_ExpfReplicaAgeLimit_Object = MibTableColumn
expfReplicaAgeLimit = _ExpfReplicaAgeLimit_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 12, 1, 37),
    _ExpfReplicaAgeLimit_Type()
)
expfReplicaAgeLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expfReplicaAgeLimit.setStatus("current")
if mibBuilder.loadTexts:
    expfReplicaAgeLimit.setUnits("days")
_ExpfReplicaList_Type = WtcsDisplayString
_ExpfReplicaList_Object = MibTableColumn
expfReplicaList = _ExpfReplicaList_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 12, 1, 38),
    _ExpfReplicaList_Type()
)
expfReplicaList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expfReplicaList.setStatus("current")


class _ExpfReplicationMessagePriority_Type(Integer32):
    """Custom type expfReplicationMessagePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("notUrgent", 0),
          ("urgent", 2))
    )


_ExpfReplicationMessagePriority_Type.__name__ = "Integer32"
_ExpfReplicationMessagePriority_Object = MibTableColumn
expfReplicationMessagePriority = _ExpfReplicationMessagePriority_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 12, 1, 39),
    _ExpfReplicationMessagePriority_Type()
)
expfReplicationMessagePriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expfReplicationMessagePriority.setStatus("current")
_ExpfReplicationSchedule_Type = WtcsDisplayString
_ExpfReplicationSchedule_Object = MibTableColumn
expfReplicationSchedule = _ExpfReplicationSchedule_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 12, 1, 40),
    _ExpfReplicationSchedule_Type()
)
expfReplicationSchedule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expfReplicationSchedule.setStatus("current")


class _ExpfReplicationStyle_Type(Integer32):
    """Custom type expfReplicationStyle based on Integer32"""
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
        *(("always", 2),
          ("custom", 0),
          ("everyFourHours", 5),
          ("everyHour", 3),
          ("everyTwoHours", 4),
          ("never", 1),
          ("usePublicStoreSchedule", 6))
    )


_ExpfReplicationStyle_Type.__name__ = "Integer32"
_ExpfReplicationStyle_Object = MibTableColumn
expfReplicationStyle = _ExpfReplicationStyle_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 12, 1, 41),
    _ExpfReplicationStyle_Type()
)
expfReplicationStyle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expfReplicationStyle.setStatus("current")
_ExpfRestrictionCount_Type = Gauge32
_ExpfRestrictionCount_Object = MibTableColumn
expfRestrictionCount = _ExpfRestrictionCount_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 12, 1, 42),
    _ExpfRestrictionCount_Type()
)
expfRestrictionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expfRestrictionCount.setStatus("current")
_ExpfSecurityDescriptor_Type = WtcsDisplayString
_ExpfSecurityDescriptor_Object = MibTableColumn
expfSecurityDescriptor = _ExpfSecurityDescriptor_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 12, 1, 43),
    _ExpfSecurityDescriptor_Type()
)
expfSecurityDescriptor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expfSecurityDescriptor.setStatus("current")


class _ExpfStorageLimitStyle_Type(Integer32):
    """Custom type expfStorageLimitStyle based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noQuota", 2),
          ("usePublicStoreStyle", 0),
          ("useSpecifiedQuota", 1))
    )


_ExpfStorageLimitStyle_Type.__name__ = "Integer32"
_ExpfStorageLimitStyle_Object = MibTableColumn
expfStorageLimitStyle = _ExpfStorageLimitStyle_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 12, 1, 44),
    _ExpfStorageLimitStyle_Type()
)
expfStorageLimitStyle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expfStorageLimitStyle.setStatus("current")
_ExpfTargetAddress_Type = WtcsDisplayString
_ExpfTargetAddress_Object = MibTableColumn
expfTargetAddress = _ExpfTargetAddress_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 12, 1, 45),
    _ExpfTargetAddress_Type()
)
expfTargetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expfTargetAddress.setStatus("current")
_ExpfTotalMessageSize_Type = Gauge32
_ExpfTotalMessageSize_Object = MibTableColumn
expfTotalMessageSize = _ExpfTotalMessageSize_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 12, 1, 46),
    _ExpfTotalMessageSize_Type()
)
expfTotalMessageSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expfTotalMessageSize.setStatus("current")
if mibBuilder.loadTexts:
    expfTotalMessageSize.setUnits("bytes")
_ExpfUrl_Type = WtcsDisplayString
_ExpfUrl_Object = MibTableColumn
expfUrl = _ExpfUrl_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 12, 1, 47),
    _ExpfUrl_Type()
)
expfUrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expfUrl.setStatus("current")
_ExpfUsePublicStoreAgeLimits_Type = TruthValue
_ExpfUsePublicStoreAgeLimits_Object = MibTableColumn
expfUsePublicStoreAgeLimits = _ExpfUsePublicStoreAgeLimits_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 12, 1, 48),
    _ExpfUsePublicStoreAgeLimits_Type()
)
expfUsePublicStoreAgeLimits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expfUsePublicStoreAgeLimits.setStatus("current")
_ExpfUsePublicStoreDelItemLifetm_Type = TruthValue
_ExpfUsePublicStoreDelItemLifetm_Object = MibTableColumn
expfUsePublicStoreDelItemLifetm = _ExpfUsePublicStoreDelItemLifetm_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 12, 1, 49),
    _ExpfUsePublicStoreDelItemLifetm_Type()
)
expfUsePublicStoreDelItemLifetm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expfUsePublicStoreDelItemLifetm.setStatus("current")
_ExpfWarningLimit_Type = Gauge32
_ExpfWarningLimit_Object = MibTableColumn
expfWarningLimit = _ExpfWarningLimit_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 12, 1, 50),
    _ExpfWarningLimit_Type()
)
expfWarningLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expfWarningLimit.setStatus("current")
if mibBuilder.loadTexts:
    expfWarningLimit.setUnits("KB")
_ExchangeQueueV2Table_Object = MibTable
exchangeQueueV2Table = _ExchangeQueueV2Table_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 13)
)
if mibBuilder.loadTexts:
    exchangeQueueV2Table.setStatus("current")
_ExchangeQueueV2Entry_Object = MibTableRow
exchangeQueueV2Entry = _ExchangeQueueV2Entry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 13, 1)
)
exchangeQueueV2Entry.setIndexNames(
    (0, "INFORMANT-WMI-EXCHANGE", "exq2Index"),
)
if mibBuilder.loadTexts:
    exchangeQueueV2Entry.setStatus("current")


class _Exq2Index_Type(Integer32):
    """Custom type exq2Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Exq2Index_Type.__name__ = "Integer32"
_Exq2Index_Object = MibTableColumn
exq2Index = _Exq2Index_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 13, 1, 1),
    _Exq2Index_Type()
)
exq2Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exq2Index.setStatus("current")
_Exq2CanEnumAll_Type = TruthValue
_Exq2CanEnumAll_Object = MibTableColumn
exq2CanEnumAll = _Exq2CanEnumAll_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 13, 1, 2),
    _Exq2CanEnumAll_Type()
)
exq2CanEnumAll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exq2CanEnumAll.setStatus("current")
_Exq2GlobalStop_Type = TruthValue
_Exq2GlobalStop_Object = MibTableColumn
exq2GlobalStop = _Exq2GlobalStop_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 13, 1, 3),
    _Exq2GlobalStop_Type()
)
exq2GlobalStop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exq2GlobalStop.setStatus("current")
_Exq2LinkId_Type = WtcsDisplayString
_Exq2LinkId_Object = MibTableColumn
exq2LinkId = _Exq2LinkId_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 13, 1, 4),
    _Exq2LinkId_Type()
)
exq2LinkId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exq2LinkId.setStatus("current")
_Exq2LinkName_Type = WtcsDisplayString
_Exq2LinkName_Object = MibTableColumn
exq2LinkName = _Exq2LinkName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 13, 1, 5),
    _Exq2LinkName_Type()
)
exq2LinkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exq2LinkName.setStatus("current")
_Exq2MessageCount_Type = Gauge32
_Exq2MessageCount_Object = MibTableColumn
exq2MessageCount = _Exq2MessageCount_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 13, 1, 6),
    _Exq2MessageCount_Type()
)
exq2MessageCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exq2MessageCount.setStatus("current")
_Exq2MsgEnumFlagsSupported_Type = Gauge32
_Exq2MsgEnumFlagsSupported_Object = MibTableColumn
exq2MsgEnumFlagsSupported = _Exq2MsgEnumFlagsSupported_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 13, 1, 7),
    _Exq2MsgEnumFlagsSupported_Type()
)
exq2MsgEnumFlagsSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exq2MsgEnumFlagsSupported.setStatus("current")
_Exq2ProtocolName_Type = WtcsDisplayString
_Exq2ProtocolName_Object = MibTableColumn
exq2ProtocolName = _Exq2ProtocolName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 13, 1, 8),
    _Exq2ProtocolName_Type()
)
exq2ProtocolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exq2ProtocolName.setStatus("current")
_Exq2QueueId_Type = WtcsDisplayString
_Exq2QueueId_Object = MibTableColumn
exq2QueueId = _Exq2QueueId_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 13, 1, 9),
    _Exq2QueueId_Type()
)
exq2QueueId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exq2QueueId.setStatus("current")
_Exq2QueueName_Type = WtcsDisplayString
_Exq2QueueName_Object = MibTableColumn
exq2QueueName = _Exq2QueueName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 13, 1, 10),
    _Exq2QueueName_Type()
)
exq2QueueName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exq2QueueName.setStatus("current")
_Exq2Size_Type = WtcsDisplayString
_Exq2Size_Object = MibTableColumn
exq2Size = _Exq2Size_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 13, 1, 11),
    _Exq2Size_Type()
)
exq2Size.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exq2Size.setStatus("current")
_Exq2Version_Type = Gauge32
_Exq2Version_Object = MibTableColumn
exq2Version = _Exq2Version_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 13, 1, 12),
    _Exq2Version_Type()
)
exq2Version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exq2Version.setStatus("current")
_Exq2VirtualMachine_Type = WtcsDisplayString
_Exq2VirtualMachine_Object = MibTableColumn
exq2VirtualMachine = _Exq2VirtualMachine_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 13, 1, 13),
    _Exq2VirtualMachine_Type()
)
exq2VirtualMachine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exq2VirtualMachine.setStatus("current")
_Exq2VirtualServerName_Type = WtcsDisplayString
_Exq2VirtualServerName_Object = MibTableColumn
exq2VirtualServerName = _Exq2VirtualServerName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 13, 1, 14),
    _Exq2VirtualServerName_Type()
)
exq2VirtualServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exq2VirtualServerName.setStatus("current")
_ExchangeQueueCacheReloadEvtTable_Object = MibTable
exchangeQueueCacheReloadEvtTable = _ExchangeQueueCacheReloadEvtTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 14)
)
if mibBuilder.loadTexts:
    exchangeQueueCacheReloadEvtTable.setStatus("current")
_ExchangeQueueCacheReloadEvtEntry_Object = MibTableRow
exchangeQueueCacheReloadEvtEntry = _ExchangeQueueCacheReloadEvtEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 14, 1)
)
exchangeQueueCacheReloadEvtEntry.setIndexNames(
    (0, "INFORMANT-WMI-EXCHANGE", "exqcreIndex"),
)
if mibBuilder.loadTexts:
    exchangeQueueCacheReloadEvtEntry.setStatus("current")


class _ExqcreIndex_Type(Integer32):
    """Custom type exqcreIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ExqcreIndex_Type.__name__ = "Integer32"
_ExqcreIndex_Object = MibTableColumn
exqcreIndex = _ExqcreIndex_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 14, 1, 1),
    _ExqcreIndex_Type()
)
exqcreIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exqcreIndex.setStatus("current")
_ExqcreReloadTime_Type = DateAndTime
_ExqcreReloadTime_Object = MibTableColumn
exqcreReloadTime = _ExqcreReloadTime_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 14, 1, 2),
    _ExqcreReloadTime_Type()
)
exqcreReloadTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exqcreReloadTime.setStatus("current")
_ExchangeQueuedMessageTable_Object = MibTable
exchangeQueuedMessageTable = _ExchangeQueuedMessageTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 15)
)
if mibBuilder.loadTexts:
    exchangeQueuedMessageTable.setStatus("current")
_ExchangeQueuedMessageEntry_Object = MibTableRow
exchangeQueuedMessageEntry = _ExchangeQueuedMessageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 15, 1)
)
exchangeQueuedMessageEntry.setIndexNames(
    (0, "INFORMANT-WMI-EXCHANGE", "exqmIndex"),
)
if mibBuilder.loadTexts:
    exchangeQueuedMessageEntry.setStatus("current")


class _ExqmIndex_Type(Integer32):
    """Custom type exqmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ExqmIndex_Type.__name__ = "Integer32"
_ExqmIndex_Object = MibTableColumn
exqmIndex = _ExqmIndex_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 15, 1, 1),
    _ExqmIndex_Type()
)
exqmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exqmIndex.setStatus("current")
_ExqmActionDeleteNDR_Type = TruthValue
_ExqmActionDeleteNDR_Object = MibTableColumn
exqmActionDeleteNDR = _ExqmActionDeleteNDR_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 15, 1, 2),
    _ExqmActionDeleteNDR_Type()
)
exqmActionDeleteNDR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exqmActionDeleteNDR.setStatus("current")
_ExqmActionDeleteNoNDR_Type = TruthValue
_ExqmActionDeleteNoNDR_Object = MibTableColumn
exqmActionDeleteNoNDR = _ExqmActionDeleteNoNDR_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 15, 1, 3),
    _ExqmActionDeleteNoNDR_Type()
)
exqmActionDeleteNoNDR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exqmActionDeleteNoNDR.setStatus("current")
_ExqmActionFreeze_Type = TruthValue
_ExqmActionFreeze_Object = MibTableColumn
exqmActionFreeze = _ExqmActionFreeze_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 15, 1, 4),
    _ExqmActionFreeze_Type()
)
exqmActionFreeze.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exqmActionFreeze.setStatus("current")
_ExqmActionThaw_Type = TruthValue
_ExqmActionThaw_Object = MibTableColumn
exqmActionThaw = _ExqmActionThaw_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 15, 1, 5),
    _ExqmActionThaw_Type()
)
exqmActionThaw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exqmActionThaw.setStatus("current")
_ExqmExpiry_Type = DateAndTime
_ExqmExpiry_Object = MibTableColumn
exqmExpiry = _ExqmExpiry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 15, 1, 6),
    _ExqmExpiry_Type()
)
exqmExpiry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exqmExpiry.setStatus("current")
_ExqmHighPriority_Type = TruthValue
_ExqmHighPriority_Object = MibTableColumn
exqmHighPriority = _ExqmHighPriority_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 15, 1, 7),
    _ExqmHighPriority_Type()
)
exqmHighPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exqmHighPriority.setStatus("current")
_ExqmLinkId_Type = WtcsDisplayString
_ExqmLinkId_Object = MibTableColumn
exqmLinkId = _ExqmLinkId_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 15, 1, 8),
    _ExqmLinkId_Type()
)
exqmLinkId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exqmLinkId.setStatus("current")
_ExqmLinkName_Type = WtcsDisplayString
_ExqmLinkName_Object = MibTableColumn
exqmLinkName = _ExqmLinkName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 15, 1, 9),
    _ExqmLinkName_Type()
)
exqmLinkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exqmLinkName.setStatus("current")
_ExqmLowPriority_Type = TruthValue
_ExqmLowPriority_Object = MibTableColumn
exqmLowPriority = _ExqmLowPriority_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 15, 1, 10),
    _ExqmLowPriority_Type()
)
exqmLowPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exqmLowPriority.setStatus("current")
_ExqmMessageId_Type = WtcsDisplayString
_ExqmMessageId_Object = MibTableColumn
exqmMessageId = _ExqmMessageId_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 15, 1, 11),
    _ExqmMessageId_Type()
)
exqmMessageId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exqmMessageId.setStatus("current")
_ExqmNormalPriority_Type = TruthValue
_ExqmNormalPriority_Object = MibTableColumn
exqmNormalPriority = _ExqmNormalPriority_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 15, 1, 12),
    _ExqmNormalPriority_Type()
)
exqmNormalPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exqmNormalPriority.setStatus("current")
_ExqmProtocolName_Type = WtcsDisplayString
_ExqmProtocolName_Object = MibTableColumn
exqmProtocolName = _ExqmProtocolName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 15, 1, 13),
    _ExqmProtocolName_Type()
)
exqmProtocolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exqmProtocolName.setStatus("current")
_ExqmQueueId_Type = WtcsDisplayString
_ExqmQueueId_Object = MibTableColumn
exqmQueueId = _ExqmQueueId_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 15, 1, 14),
    _ExqmQueueId_Type()
)
exqmQueueId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exqmQueueId.setStatus("current")
_ExqmQueueName_Type = WtcsDisplayString
_ExqmQueueName_Object = MibTableColumn
exqmQueueName = _ExqmQueueName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 15, 1, 15),
    _ExqmQueueName_Type()
)
exqmQueueName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exqmQueueName.setStatus("current")
_ExqmReceived_Type = DateAndTime
_ExqmReceived_Object = MibTableColumn
exqmReceived = _ExqmReceived_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 15, 1, 16),
    _ExqmReceived_Type()
)
exqmReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exqmReceived.setStatus("current")
_ExqmRecipientCount_Type = Gauge32
_ExqmRecipientCount_Object = MibTableColumn
exqmRecipientCount = _ExqmRecipientCount_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 15, 1, 17),
    _ExqmRecipientCount_Type()
)
exqmRecipientCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exqmRecipientCount.setStatus("current")
_ExqmRecipients_Type = WtcsDisplayString
_ExqmRecipients_Object = MibTableColumn
exqmRecipients = _ExqmRecipients_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 15, 1, 18),
    _ExqmRecipients_Type()
)
exqmRecipients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exqmRecipients.setStatus("current")
_ExqmSender_Type = WtcsDisplayString
_ExqmSender_Object = MibTableColumn
exqmSender = _ExqmSender_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 15, 1, 19),
    _ExqmSender_Type()
)
exqmSender.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exqmSender.setStatus("current")
_ExqmSize_Type = Gauge32
_ExqmSize_Object = MibTableColumn
exqmSize = _ExqmSize_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 15, 1, 20),
    _ExqmSize_Type()
)
exqmSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exqmSize.setStatus("current")
if mibBuilder.loadTexts:
    exqmSize.setUnits("KB")
_ExqmStateFlags_Type = Gauge32
_ExqmStateFlags_Object = MibTableColumn
exqmStateFlags = _ExqmStateFlags_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 15, 1, 21),
    _ExqmStateFlags_Type()
)
exqmStateFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exqmStateFlags.setStatus("current")
_ExqmStateFrozen_Type = TruthValue
_ExqmStateFrozen_Object = MibTableColumn
exqmStateFrozen = _ExqmStateFrozen_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 15, 1, 22),
    _ExqmStateFrozen_Type()
)
exqmStateFrozen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exqmStateFrozen.setStatus("current")
_ExqmStateRetry_Type = TruthValue
_ExqmStateRetry_Object = MibTableColumn
exqmStateRetry = _ExqmStateRetry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 15, 1, 23),
    _ExqmStateRetry_Type()
)
exqmStateRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exqmStateRetry.setStatus("current")
_ExqmSubject_Type = WtcsDisplayString
_ExqmSubject_Object = MibTableColumn
exqmSubject = _ExqmSubject_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 15, 1, 24),
    _ExqmSubject_Type()
)
exqmSubject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exqmSubject.setStatus("current")
_ExqmSubmission_Type = DateAndTime
_ExqmSubmission_Object = MibTableColumn
exqmSubmission = _ExqmSubmission_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 15, 1, 25),
    _ExqmSubmission_Type()
)
exqmSubmission.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exqmSubmission.setStatus("current")
_ExqmVersion_Type = Gauge32
_ExqmVersion_Object = MibTableColumn
exqmVersion = _ExqmVersion_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 15, 1, 26),
    _ExqmVersion_Type()
)
exqmVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exqmVersion.setStatus("current")
_ExqmVirtualMachine_Type = WtcsDisplayString
_ExqmVirtualMachine_Object = MibTableColumn
exqmVirtualMachine = _ExqmVirtualMachine_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 15, 1, 27),
    _ExqmVirtualMachine_Type()
)
exqmVirtualMachine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exqmVirtualMachine.setStatus("current")
_ExqmVirtualServerName_Type = WtcsDisplayString
_ExqmVirtualServerName_Object = MibTableColumn
exqmVirtualServerName = _ExqmVirtualServerName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 15, 1, 28),
    _ExqmVirtualServerName_Type()
)
exqmVirtualServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exqmVirtualServerName.setStatus("current")
_ExchangeQueueVirtualServerTable_Object = MibTable
exchangeQueueVirtualServerTable = _ExchangeQueueVirtualServerTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 16)
)
if mibBuilder.loadTexts:
    exchangeQueueVirtualServerTable.setStatus("current")
_ExchangeQueueVirtualServerEntry_Object = MibTableRow
exchangeQueueVirtualServerEntry = _ExchangeQueueVirtualServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 16, 1)
)
exchangeQueueVirtualServerEntry.setIndexNames(
    (0, "INFORMANT-WMI-EXCHANGE", "exvsIndex"),
)
if mibBuilder.loadTexts:
    exchangeQueueVirtualServerEntry.setStatus("current")


class _ExvsIndex_Type(Integer32):
    """Custom type exvsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ExvsIndex_Type.__name__ = "Integer32"
_ExvsIndex_Object = MibTableColumn
exvsIndex = _ExvsIndex_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 16, 1, 1),
    _ExvsIndex_Type()
)
exvsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exvsIndex.setStatus("current")
_ExvsGlobalActionsSupported_Type = TruthValue
_ExvsGlobalActionsSupported_Object = MibTableColumn
exvsGlobalActionsSupported = _ExvsGlobalActionsSupported_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 16, 1, 2),
    _ExvsGlobalActionsSupported_Type()
)
exvsGlobalActionsSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exvsGlobalActionsSupported.setStatus("current")
_ExvsGlobalStop_Type = TruthValue
_ExvsGlobalStop_Object = MibTableColumn
exvsGlobalStop = _ExvsGlobalStop_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 16, 1, 3),
    _ExvsGlobalStop_Type()
)
exvsGlobalStop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exvsGlobalStop.setStatus("current")
_ExvsProtocolName_Type = WtcsDisplayString
_ExvsProtocolName_Object = MibTableColumn
exvsProtocolName = _ExvsProtocolName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 16, 1, 4),
    _ExvsProtocolName_Type()
)
exvsProtocolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exvsProtocolName.setStatus("current")
_ExvsVirtualMachine_Type = WtcsDisplayString
_ExvsVirtualMachine_Object = MibTableColumn
exvsVirtualMachine = _ExvsVirtualMachine_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 16, 1, 5),
    _ExvsVirtualMachine_Type()
)
exvsVirtualMachine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exvsVirtualMachine.setStatus("current")
_ExvsVirtualServerName_Type = WtcsDisplayString
_ExvsVirtualServerName_Object = MibTableColumn
exvsVirtualServerName = _ExvsVirtualServerName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 16, 1, 6),
    _ExvsVirtualServerName_Type()
)
exvsVirtualServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exvsVirtualServerName.setStatus("current")
_ExchangeServerTable_Object = MibTable
exchangeServerTable = _ExchangeServerTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 17)
)
if mibBuilder.loadTexts:
    exchangeServerTable.setStatus("current")
_ExchangeServerEntry_Object = MibTableRow
exchangeServerEntry = _ExchangeServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 17, 1)
)
exchangeServerEntry.setIndexNames(
    (0, "INFORMANT-WMI-EXCHANGE", "exsIndex"),
)
if mibBuilder.loadTexts:
    exchangeServerEntry.setStatus("current")


class _ExsIndex_Type(Integer32):
    """Custom type exsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ExsIndex_Type.__name__ = "Integer32"
_ExsIndex_Object = MibTableColumn
exsIndex = _ExsIndex_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 17, 1, 1),
    _ExsIndex_Type()
)
exsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exsIndex.setStatus("current")
_ExsAdministrativeGroup_Type = WtcsDisplayString
_ExsAdministrativeGroup_Object = MibTableColumn
exsAdministrativeGroup = _ExsAdministrativeGroup_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 17, 1, 2),
    _ExsAdministrativeGroup_Type()
)
exsAdministrativeGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exsAdministrativeGroup.setStatus("current")
_ExsAdministrativeNote_Type = WtcsDisplayString
_ExsAdministrativeNote_Object = MibTableColumn
exsAdministrativeNote = _ExsAdministrativeNote_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 17, 1, 3),
    _ExsAdministrativeNote_Type()
)
exsAdministrativeNote.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exsAdministrativeNote.setStatus("current")
_ExsCreationTime_Type = DateAndTime
_ExsCreationTime_Object = MibTableColumn
exsCreationTime = _ExsCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 17, 1, 4),
    _ExsCreationTime_Type()
)
exsCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exsCreationTime.setStatus("current")
_ExsDN_Type = WtcsDisplayString
_ExsDN_Object = MibTableColumn
exsDN = _ExsDN_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 17, 1, 5),
    _ExsDN_Type()
)
exsDN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exsDN.setStatus("current")
_ExsExchangeVersion_Type = WtcsDisplayString
_ExsExchangeVersion_Object = MibTableColumn
exsExchangeVersion = _ExsExchangeVersion_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 17, 1, 6),
    _ExsExchangeVersion_Type()
)
exsExchangeVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exsExchangeVersion.setStatus("current")
_ExsFQDN_Type = WtcsDisplayString
_ExsFQDN_Object = MibTableColumn
exsFQDN = _ExsFQDN_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 17, 1, 7),
    _ExsFQDN_Type()
)
exsFQDN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exsFQDN.setStatus("current")
_ExsGUID_Type = WtcsDisplayString
_ExsGUID_Object = MibTableColumn
exsGUID = _ExsGUID_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 17, 1, 8),
    _ExsGUID_Type()
)
exsGUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exsGUID.setStatus("current")
_ExsIsFrontEndServer_Type = TruthValue
_ExsIsFrontEndServer_Object = MibTableColumn
exsIsFrontEndServer = _ExsIsFrontEndServer_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 17, 1, 9),
    _ExsIsFrontEndServer_Type()
)
exsIsFrontEndServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exsIsFrontEndServer.setStatus("current")
_ExsLastModificationTime_Type = DateAndTime
_ExsLastModificationTime_Object = MibTableColumn
exsLastModificationTime = _ExsLastModificationTime_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 17, 1, 10),
    _ExsLastModificationTime_Type()
)
exsLastModificationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exsLastModificationTime.setStatus("current")
_ExsMessageTrackingEnabled_Type = TruthValue
_ExsMessageTrackingEnabled_Object = MibTableColumn
exsMessageTrackingEnabled = _ExsMessageTrackingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 17, 1, 11),
    _ExsMessageTrackingEnabled_Type()
)
exsMessageTrackingEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exsMessageTrackingEnabled.setStatus("current")
_ExsMessageTrackingLogFileLifetm_Type = Gauge32
_ExsMessageTrackingLogFileLifetm_Object = MibTableColumn
exsMessageTrackingLogFileLifetm = _ExsMessageTrackingLogFileLifetm_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 17, 1, 12),
    _ExsMessageTrackingLogFileLifetm_Type()
)
exsMessageTrackingLogFileLifetm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exsMessageTrackingLogFileLifetm.setStatus("current")
if mibBuilder.loadTexts:
    exsMessageTrackingLogFileLifetm.setUnits("days")
_ExsMessageTrackingLogFilePath_Type = WtcsDisplayString
_ExsMessageTrackingLogFilePath_Object = MibTableColumn
exsMessageTrackingLogFilePath = _ExsMessageTrackingLogFilePath_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 17, 1, 13),
    _ExsMessageTrackingLogFilePath_Type()
)
exsMessageTrackingLogFilePath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exsMessageTrackingLogFilePath.setStatus("current")
_ExsMonitoringEnabled_Type = TruthValue
_ExsMonitoringEnabled_Object = MibTableColumn
exsMonitoringEnabled = _ExsMonitoringEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 17, 1, 14),
    _ExsMonitoringEnabled_Type()
)
exsMonitoringEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exsMonitoringEnabled.setStatus("current")
_ExsMTADataPath_Type = WtcsDisplayString
_ExsMTADataPath_Object = MibTableColumn
exsMTADataPath = _ExsMTADataPath_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 17, 1, 15),
    _ExsMTADataPath_Type()
)
exsMTADataPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exsMTADataPath.setStatus("current")
_ExsName_Type = WtcsDisplayString
_ExsName_Object = MibTableColumn
exsName = _ExsName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 17, 1, 16),
    _ExsName_Type()
)
exsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exsName.setStatus("current")
_ExsRoutingGroup_Type = WtcsDisplayString
_ExsRoutingGroup_Object = MibTableColumn
exsRoutingGroup = _ExsRoutingGroup_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 17, 1, 17),
    _ExsRoutingGroup_Type()
)
exsRoutingGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exsRoutingGroup.setStatus("current")
_ExsSubjectLoggingEnabled_Type = TruthValue
_ExsSubjectLoggingEnabled_Object = MibTableColumn
exsSubjectLoggingEnabled = _ExsSubjectLoggingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 17, 1, 18),
    _ExsSubjectLoggingEnabled_Type()
)
exsSubjectLoggingEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exsSubjectLoggingEnabled.setStatus("current")


class _ExsType_Type(Integer32):
    """Custom type exsType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("conferencing", 2),
          ("enterprise", 1),
          ("standard", 0))
    )


_ExsType_Type.__name__ = "Integer32"
_ExsType_Object = MibTableColumn
exsType = _ExsType_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 17, 1, 19),
    _ExsType_Type()
)
exsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exsType.setStatus("current")
_ExchangeQueuedSMTPMessageTable_Object = MibTable
exchangeQueuedSMTPMessageTable = _ExchangeQueuedSMTPMessageTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 18)
)
if mibBuilder.loadTexts:
    exchangeQueuedSMTPMessageTable.setStatus("current")
_ExchangeQueuedSMTPMessageEntry_Object = MibTableRow
exchangeQueuedSMTPMessageEntry = _ExchangeQueuedSMTPMessageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 18, 1)
)
exchangeQueuedSMTPMessageEntry.setIndexNames(
    (0, "INFORMANT-WMI-EXCHANGE", "exqsmIndex"),
)
if mibBuilder.loadTexts:
    exchangeQueuedSMTPMessageEntry.setStatus("current")


class _ExqsmIndex_Type(Integer32):
    """Custom type exqsmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ExqsmIndex_Type.__name__ = "Integer32"
_ExqsmIndex_Object = MibTableColumn
exqsmIndex = _ExqsmIndex_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 18, 1, 1),
    _ExqsmIndex_Type()
)
exqsmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exqsmIndex.setStatus("current")
_ExqsmActionDeleteNDR_Type = TruthValue
_ExqsmActionDeleteNDR_Object = MibTableColumn
exqsmActionDeleteNDR = _ExqsmActionDeleteNDR_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 18, 1, 2),
    _ExqsmActionDeleteNDR_Type()
)
exqsmActionDeleteNDR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exqsmActionDeleteNDR.setStatus("current")
_ExqsmActionDeleteNoNDR_Type = TruthValue
_ExqsmActionDeleteNoNDR_Object = MibTableColumn
exqsmActionDeleteNoNDR = _ExqsmActionDeleteNoNDR_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 18, 1, 3),
    _ExqsmActionDeleteNoNDR_Type()
)
exqsmActionDeleteNoNDR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exqsmActionDeleteNoNDR.setStatus("current")
_ExqsmActionFreeze_Type = TruthValue
_ExqsmActionFreeze_Object = MibTableColumn
exqsmActionFreeze = _ExqsmActionFreeze_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 18, 1, 4),
    _ExqsmActionFreeze_Type()
)
exqsmActionFreeze.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exqsmActionFreeze.setStatus("current")
_ExqsmActionThaw_Type = TruthValue
_ExqsmActionThaw_Object = MibTableColumn
exqsmActionThaw = _ExqsmActionThaw_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 18, 1, 5),
    _ExqsmActionThaw_Type()
)
exqsmActionThaw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exqsmActionThaw.setStatus("current")
_ExqsmExpiry_Type = DateAndTime
_ExqsmExpiry_Object = MibTableColumn
exqsmExpiry = _ExqsmExpiry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 18, 1, 6),
    _ExqsmExpiry_Type()
)
exqsmExpiry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exqsmExpiry.setStatus("current")
_ExqsmHighPriority_Type = TruthValue
_ExqsmHighPriority_Object = MibTableColumn
exqsmHighPriority = _ExqsmHighPriority_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 18, 1, 7),
    _ExqsmHighPriority_Type()
)
exqsmHighPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exqsmHighPriority.setStatus("current")
_ExqsmLinkId_Type = WtcsDisplayString
_ExqsmLinkId_Object = MibTableColumn
exqsmLinkId = _ExqsmLinkId_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 18, 1, 8),
    _ExqsmLinkId_Type()
)
exqsmLinkId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exqsmLinkId.setStatus("current")
_ExqsmLinkName_Type = WtcsDisplayString
_ExqsmLinkName_Object = MibTableColumn
exqsmLinkName = _ExqsmLinkName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 18, 1, 9),
    _ExqsmLinkName_Type()
)
exqsmLinkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exqsmLinkName.setStatus("current")
_ExqsmLowPriority_Type = TruthValue
_ExqsmLowPriority_Object = MibTableColumn
exqsmLowPriority = _ExqsmLowPriority_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 18, 1, 10),
    _ExqsmLowPriority_Type()
)
exqsmLowPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exqsmLowPriority.setStatus("current")
_ExqsmMessageId_Type = WtcsDisplayString
_ExqsmMessageId_Object = MibTableColumn
exqsmMessageId = _ExqsmMessageId_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 18, 1, 11),
    _ExqsmMessageId_Type()
)
exqsmMessageId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exqsmMessageId.setStatus("current")
_ExqsmNormalPriority_Type = TruthValue
_ExqsmNormalPriority_Object = MibTableColumn
exqsmNormalPriority = _ExqsmNormalPriority_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 18, 1, 12),
    _ExqsmNormalPriority_Type()
)
exqsmNormalPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exqsmNormalPriority.setStatus("current")
_ExqsmProtocolName_Type = WtcsDisplayString
_ExqsmProtocolName_Object = MibTableColumn
exqsmProtocolName = _ExqsmProtocolName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 18, 1, 13),
    _ExqsmProtocolName_Type()
)
exqsmProtocolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exqsmProtocolName.setStatus("current")
_ExqsmQueueId_Type = WtcsDisplayString
_ExqsmQueueId_Object = MibTableColumn
exqsmQueueId = _ExqsmQueueId_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 18, 1, 14),
    _ExqsmQueueId_Type()
)
exqsmQueueId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exqsmQueueId.setStatus("current")
_ExqsmQueueName_Type = WtcsDisplayString
_ExqsmQueueName_Object = MibTableColumn
exqsmQueueName = _ExqsmQueueName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 18, 1, 15),
    _ExqsmQueueName_Type()
)
exqsmQueueName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exqsmQueueName.setStatus("current")
_ExqsmReceived_Type = DateAndTime
_ExqsmReceived_Object = MibTableColumn
exqsmReceived = _ExqsmReceived_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 18, 1, 16),
    _ExqsmReceived_Type()
)
exqsmReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exqsmReceived.setStatus("current")
_ExqsmRecipientCount_Type = Gauge32
_ExqsmRecipientCount_Object = MibTableColumn
exqsmRecipientCount = _ExqsmRecipientCount_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 18, 1, 17),
    _ExqsmRecipientCount_Type()
)
exqsmRecipientCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exqsmRecipientCount.setStatus("current")
_ExqsmRecipients_Type = WtcsDisplayString
_ExqsmRecipients_Object = MibTableColumn
exqsmRecipients = _ExqsmRecipients_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 18, 1, 18),
    _ExqsmRecipients_Type()
)
exqsmRecipients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exqsmRecipients.setStatus("current")
_ExqsmSender_Type = WtcsDisplayString
_ExqsmSender_Object = MibTableColumn
exqsmSender = _ExqsmSender_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 18, 1, 19),
    _ExqsmSender_Type()
)
exqsmSender.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exqsmSender.setStatus("current")
_ExqsmSize_Type = Gauge32
_ExqsmSize_Object = MibTableColumn
exqsmSize = _ExqsmSize_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 18, 1, 20),
    _ExqsmSize_Type()
)
exqsmSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exqsmSize.setStatus("current")
if mibBuilder.loadTexts:
    exqsmSize.setUnits("KB")
_ExqsmStateFlags_Type = Gauge32
_ExqsmStateFlags_Object = MibTableColumn
exqsmStateFlags = _ExqsmStateFlags_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 18, 1, 21),
    _ExqsmStateFlags_Type()
)
exqsmStateFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exqsmStateFlags.setStatus("current")
_ExqsmStateFrozen_Type = TruthValue
_ExqsmStateFrozen_Object = MibTableColumn
exqsmStateFrozen = _ExqsmStateFrozen_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 18, 1, 22),
    _ExqsmStateFrozen_Type()
)
exqsmStateFrozen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exqsmStateFrozen.setStatus("current")
_ExqsmStateRetry_Type = TruthValue
_ExqsmStateRetry_Object = MibTableColumn
exqsmStateRetry = _ExqsmStateRetry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 18, 1, 23),
    _ExqsmStateRetry_Type()
)
exqsmStateRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exqsmStateRetry.setStatus("current")
_ExqsmSubject_Type = WtcsDisplayString
_ExqsmSubject_Object = MibTableColumn
exqsmSubject = _ExqsmSubject_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 18, 1, 24),
    _ExqsmSubject_Type()
)
exqsmSubject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exqsmSubject.setStatus("current")
_ExqsmSubmission_Type = DateAndTime
_ExqsmSubmission_Object = MibTableColumn
exqsmSubmission = _ExqsmSubmission_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 18, 1, 25),
    _ExqsmSubmission_Type()
)
exqsmSubmission.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exqsmSubmission.setStatus("current")
_ExqsmVersion_Type = Gauge32
_ExqsmVersion_Object = MibTableColumn
exqsmVersion = _ExqsmVersion_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 18, 1, 26),
    _ExqsmVersion_Type()
)
exqsmVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exqsmVersion.setStatus("current")
_ExqsmVirtualMachine_Type = WtcsDisplayString
_ExqsmVirtualMachine_Object = MibTableColumn
exqsmVirtualMachine = _ExqsmVirtualMachine_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 18, 1, 27),
    _ExqsmVirtualMachine_Type()
)
exqsmVirtualMachine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exqsmVirtualMachine.setStatus("current")
_ExqsmVirtualServerName_Type = WtcsDisplayString
_ExqsmVirtualServerName_Object = MibTableColumn
exqsmVirtualServerName = _ExqsmVirtualServerName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 18, 1, 28),
    _ExqsmVirtualServerName_Type()
)
exqsmVirtualServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exqsmVirtualServerName.setStatus("current")
_ExchangeQueuedX400MessageTable_Object = MibTable
exchangeQueuedX400MessageTable = _ExchangeQueuedX400MessageTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 19)
)
if mibBuilder.loadTexts:
    exchangeQueuedX400MessageTable.setStatus("current")
_ExchangeQueuedX400MessageEntry_Object = MibTableRow
exchangeQueuedX400MessageEntry = _ExchangeQueuedX400MessageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 19, 1)
)
exchangeQueuedX400MessageEntry.setIndexNames(
    (0, "INFORMANT-WMI-EXCHANGE", "exqxmIndex"),
)
if mibBuilder.loadTexts:
    exchangeQueuedX400MessageEntry.setStatus("current")


class _ExqxmIndex_Type(Integer32):
    """Custom type exqxmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ExqxmIndex_Type.__name__ = "Integer32"
_ExqxmIndex_Object = MibTableColumn
exqxmIndex = _ExqxmIndex_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 19, 1, 1),
    _ExqxmIndex_Type()
)
exqxmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exqxmIndex.setStatus("current")
_ExqxmActionDeleteNDR_Type = TruthValue
_ExqxmActionDeleteNDR_Object = MibTableColumn
exqxmActionDeleteNDR = _ExqxmActionDeleteNDR_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 19, 1, 2),
    _ExqxmActionDeleteNDR_Type()
)
exqxmActionDeleteNDR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exqxmActionDeleteNDR.setStatus("current")
_ExqxmActionDeleteNoNDR_Type = TruthValue
_ExqxmActionDeleteNoNDR_Object = MibTableColumn
exqxmActionDeleteNoNDR = _ExqxmActionDeleteNoNDR_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 19, 1, 3),
    _ExqxmActionDeleteNoNDR_Type()
)
exqxmActionDeleteNoNDR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exqxmActionDeleteNoNDR.setStatus("current")
_ExqxmActionFreeze_Type = TruthValue
_ExqxmActionFreeze_Object = MibTableColumn
exqxmActionFreeze = _ExqxmActionFreeze_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 19, 1, 4),
    _ExqxmActionFreeze_Type()
)
exqxmActionFreeze.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exqxmActionFreeze.setStatus("current")
_ExqxmActionThaw_Type = TruthValue
_ExqxmActionThaw_Object = MibTableColumn
exqxmActionThaw = _ExqxmActionThaw_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 19, 1, 5),
    _ExqxmActionThaw_Type()
)
exqxmActionThaw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exqxmActionThaw.setStatus("current")
_ExqxmExpiry_Type = DateAndTime
_ExqxmExpiry_Object = MibTableColumn
exqxmExpiry = _ExqxmExpiry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 19, 1, 6),
    _ExqxmExpiry_Type()
)
exqxmExpiry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exqxmExpiry.setStatus("current")
_ExqxmHighPriority_Type = TruthValue
_ExqxmHighPriority_Object = MibTableColumn
exqxmHighPriority = _ExqxmHighPriority_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 19, 1, 7),
    _ExqxmHighPriority_Type()
)
exqxmHighPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exqxmHighPriority.setStatus("current")
_ExqxmLinkId_Type = WtcsDisplayString
_ExqxmLinkId_Object = MibTableColumn
exqxmLinkId = _ExqxmLinkId_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 19, 1, 8),
    _ExqxmLinkId_Type()
)
exqxmLinkId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exqxmLinkId.setStatus("current")
_ExqxmLinkName_Type = WtcsDisplayString
_ExqxmLinkName_Object = MibTableColumn
exqxmLinkName = _ExqxmLinkName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 19, 1, 9),
    _ExqxmLinkName_Type()
)
exqxmLinkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exqxmLinkName.setStatus("current")
_ExqxmLowPriority_Type = TruthValue
_ExqxmLowPriority_Object = MibTableColumn
exqxmLowPriority = _ExqxmLowPriority_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 19, 1, 10),
    _ExqxmLowPriority_Type()
)
exqxmLowPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exqxmLowPriority.setStatus("current")
_ExqxmMessageId_Type = WtcsDisplayString
_ExqxmMessageId_Object = MibTableColumn
exqxmMessageId = _ExqxmMessageId_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 19, 1, 11),
    _ExqxmMessageId_Type()
)
exqxmMessageId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exqxmMessageId.setStatus("current")
_ExqxmNormalPriority_Type = TruthValue
_ExqxmNormalPriority_Object = MibTableColumn
exqxmNormalPriority = _ExqxmNormalPriority_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 19, 1, 12),
    _ExqxmNormalPriority_Type()
)
exqxmNormalPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exqxmNormalPriority.setStatus("current")
_ExqxmProtocolName_Type = WtcsDisplayString
_ExqxmProtocolName_Object = MibTableColumn
exqxmProtocolName = _ExqxmProtocolName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 19, 1, 13),
    _ExqxmProtocolName_Type()
)
exqxmProtocolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exqxmProtocolName.setStatus("current")
_ExqxmQueueId_Type = WtcsDisplayString
_ExqxmQueueId_Object = MibTableColumn
exqxmQueueId = _ExqxmQueueId_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 19, 1, 14),
    _ExqxmQueueId_Type()
)
exqxmQueueId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exqxmQueueId.setStatus("current")
_ExqxmQueueName_Type = WtcsDisplayString
_ExqxmQueueName_Object = MibTableColumn
exqxmQueueName = _ExqxmQueueName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 19, 1, 15),
    _ExqxmQueueName_Type()
)
exqxmQueueName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exqxmQueueName.setStatus("current")
_ExqxmReceived_Type = DateAndTime
_ExqxmReceived_Object = MibTableColumn
exqxmReceived = _ExqxmReceived_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 19, 1, 16),
    _ExqxmReceived_Type()
)
exqxmReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exqxmReceived.setStatus("current")
_ExqxmRecipientCount_Type = Gauge32
_ExqxmRecipientCount_Object = MibTableColumn
exqxmRecipientCount = _ExqxmRecipientCount_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 19, 1, 17),
    _ExqxmRecipientCount_Type()
)
exqxmRecipientCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exqxmRecipientCount.setStatus("current")
_ExqxmRecipients_Type = WtcsDisplayString
_ExqxmRecipients_Object = MibTableColumn
exqxmRecipients = _ExqxmRecipients_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 19, 1, 18),
    _ExqxmRecipients_Type()
)
exqxmRecipients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exqxmRecipients.setStatus("current")
_ExqxmSender_Type = WtcsDisplayString
_ExqxmSender_Object = MibTableColumn
exqxmSender = _ExqxmSender_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 19, 1, 19),
    _ExqxmSender_Type()
)
exqxmSender.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exqxmSender.setStatus("current")
_ExqxmSize_Type = Gauge32
_ExqxmSize_Object = MibTableColumn
exqxmSize = _ExqxmSize_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 19, 1, 20),
    _ExqxmSize_Type()
)
exqxmSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exqxmSize.setStatus("current")
if mibBuilder.loadTexts:
    exqxmSize.setUnits("KB")
_ExqxmStateFlags_Type = Gauge32
_ExqxmStateFlags_Object = MibTableColumn
exqxmStateFlags = _ExqxmStateFlags_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 19, 1, 21),
    _ExqxmStateFlags_Type()
)
exqxmStateFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exqxmStateFlags.setStatus("current")
_ExqxmStateFrozen_Type = TruthValue
_ExqxmStateFrozen_Object = MibTableColumn
exqxmStateFrozen = _ExqxmStateFrozen_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 19, 1, 22),
    _ExqxmStateFrozen_Type()
)
exqxmStateFrozen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exqxmStateFrozen.setStatus("current")
_ExqxmStateRetry_Type = TruthValue
_ExqxmStateRetry_Object = MibTableColumn
exqxmStateRetry = _ExqxmStateRetry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 19, 1, 23),
    _ExqxmStateRetry_Type()
)
exqxmStateRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exqxmStateRetry.setStatus("current")
_ExqxmSubject_Type = WtcsDisplayString
_ExqxmSubject_Object = MibTableColumn
exqxmSubject = _ExqxmSubject_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 19, 1, 24),
    _ExqxmSubject_Type()
)
exqxmSubject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exqxmSubject.setStatus("current")
_ExqxmSubmission_Type = DateAndTime
_ExqxmSubmission_Object = MibTableColumn
exqxmSubmission = _ExqxmSubmission_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 19, 1, 25),
    _ExqxmSubmission_Type()
)
exqxmSubmission.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exqxmSubmission.setStatus("current")
_ExqxmVersion_Type = Gauge32
_ExqxmVersion_Object = MibTableColumn
exqxmVersion = _ExqxmVersion_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 19, 1, 26),
    _ExqxmVersion_Type()
)
exqxmVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exqxmVersion.setStatus("current")
_ExqxmVirtualMachine_Type = WtcsDisplayString
_ExqxmVirtualMachine_Object = MibTableColumn
exqxmVirtualMachine = _ExqxmVirtualMachine_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 19, 1, 27),
    _ExqxmVirtualMachine_Type()
)
exqxmVirtualMachine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exqxmVirtualMachine.setStatus("current")
_ExqxmVirtualServerName_Type = WtcsDisplayString
_ExqxmVirtualServerName_Object = MibTableColumn
exqxmVirtualServerName = _ExqxmVirtualServerName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 19, 1, 28),
    _ExqxmVirtualServerName_Type()
)
exqxmVirtualServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exqxmVirtualServerName.setStatus("current")
_ExchangeQueueSMTPVirtualSrvTable_Object = MibTable
exchangeQueueSMTPVirtualSrvTable = _ExchangeQueueSMTPVirtualSrvTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 20)
)
if mibBuilder.loadTexts:
    exchangeQueueSMTPVirtualSrvTable.setStatus("current")
_ExchangeQueueSMTPVirtualSrvEntry_Object = MibTableRow
exchangeQueueSMTPVirtualSrvEntry = _ExchangeQueueSMTPVirtualSrvEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 20, 1)
)
exchangeQueueSMTPVirtualSrvEntry.setIndexNames(
    (0, "INFORMANT-WMI-EXCHANGE", "exqsvsIndex"),
)
if mibBuilder.loadTexts:
    exchangeQueueSMTPVirtualSrvEntry.setStatus("current")


class _ExqsvsIndex_Type(Integer32):
    """Custom type exqsvsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ExqsvsIndex_Type.__name__ = "Integer32"
_ExqsvsIndex_Object = MibTableColumn
exqsvsIndex = _ExqsvsIndex_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 20, 1, 1),
    _ExqsvsIndex_Type()
)
exqsvsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exqsvsIndex.setStatus("current")
_ExqsvsGlobalActionsSupported_Type = TruthValue
_ExqsvsGlobalActionsSupported_Object = MibTableColumn
exqsvsGlobalActionsSupported = _ExqsvsGlobalActionsSupported_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 20, 1, 2),
    _ExqsvsGlobalActionsSupported_Type()
)
exqsvsGlobalActionsSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exqsvsGlobalActionsSupported.setStatus("current")
_ExqsvsGlobalStop_Type = TruthValue
_ExqsvsGlobalStop_Object = MibTableColumn
exqsvsGlobalStop = _ExqsvsGlobalStop_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 20, 1, 3),
    _ExqsvsGlobalStop_Type()
)
exqsvsGlobalStop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exqsvsGlobalStop.setStatus("current")
_ExqsvsProtocolName_Type = WtcsDisplayString
_ExqsvsProtocolName_Object = MibTableColumn
exqsvsProtocolName = _ExqsvsProtocolName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 20, 1, 4),
    _ExqsvsProtocolName_Type()
)
exqsvsProtocolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exqsvsProtocolName.setStatus("current")
_ExqsvsVirtualMachine_Type = WtcsDisplayString
_ExqsvsVirtualMachine_Object = MibTableColumn
exqsvsVirtualMachine = _ExqsvsVirtualMachine_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 20, 1, 5),
    _ExqsvsVirtualMachine_Type()
)
exqsvsVirtualMachine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exqsvsVirtualMachine.setStatus("current")
_ExqsvsVirtualServerName_Type = WtcsDisplayString
_ExqsvsVirtualServerName_Object = MibTableColumn
exqsvsVirtualServerName = _ExqsvsVirtualServerName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 20, 1, 6),
    _ExqsvsVirtualServerName_Type()
)
exqsvsVirtualServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exqsvsVirtualServerName.setStatus("current")
_ExchangeQueueX400VirtualSrvTable_Object = MibTable
exchangeQueueX400VirtualSrvTable = _ExchangeQueueX400VirtualSrvTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 21)
)
if mibBuilder.loadTexts:
    exchangeQueueX400VirtualSrvTable.setStatus("current")
_ExchangeQueueX400VirtualSrvEntry_Object = MibTableRow
exchangeQueueX400VirtualSrvEntry = _ExchangeQueueX400VirtualSrvEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 21, 1)
)
exchangeQueueX400VirtualSrvEntry.setIndexNames(
    (0, "INFORMANT-WMI-EXCHANGE", "exqxvsIndex"),
)
if mibBuilder.loadTexts:
    exchangeQueueX400VirtualSrvEntry.setStatus("current")


class _ExqxvsIndex_Type(Integer32):
    """Custom type exqxvsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ExqxvsIndex_Type.__name__ = "Integer32"
_ExqxvsIndex_Object = MibTableColumn
exqxvsIndex = _ExqxvsIndex_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 21, 1, 1),
    _ExqxvsIndex_Type()
)
exqxvsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exqxvsIndex.setStatus("current")
_ExqxvsGlobalActionsSupported_Type = TruthValue
_ExqxvsGlobalActionsSupported_Object = MibTableColumn
exqxvsGlobalActionsSupported = _ExqxvsGlobalActionsSupported_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 21, 1, 2),
    _ExqxvsGlobalActionsSupported_Type()
)
exqxvsGlobalActionsSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exqxvsGlobalActionsSupported.setStatus("current")
_ExqxvsGlobalStop_Type = TruthValue
_ExqxvsGlobalStop_Object = MibTableColumn
exqxvsGlobalStop = _ExqxvsGlobalStop_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 21, 1, 3),
    _ExqxvsGlobalStop_Type()
)
exqxvsGlobalStop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exqxvsGlobalStop.setStatus("current")
_ExqxvsProtocolName_Type = WtcsDisplayString
_ExqxvsProtocolName_Object = MibTableColumn
exqxvsProtocolName = _ExqxvsProtocolName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 21, 1, 4),
    _ExqxvsProtocolName_Type()
)
exqxvsProtocolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exqxvsProtocolName.setStatus("current")
_ExqxvsVirtualMachine_Type = WtcsDisplayString
_ExqxvsVirtualMachine_Object = MibTableColumn
exqxvsVirtualMachine = _ExqxvsVirtualMachine_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 21, 1, 5),
    _ExqxvsVirtualMachine_Type()
)
exqxvsVirtualMachine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exqxvsVirtualMachine.setStatus("current")
_ExqxvsVirtualServerName_Type = WtcsDisplayString
_ExqxvsVirtualServerName_Object = MibTableColumn
exqxvsVirtualServerName = _ExqxvsVirtualServerName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 21, 1, 6),
    _ExqxvsVirtualServerName_Type()
)
exqxvsVirtualServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exqxvsVirtualServerName.setStatus("current")
_ExchangeScheduleIntervalTable_Object = MibTable
exchangeScheduleIntervalTable = _ExchangeScheduleIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 22)
)
if mibBuilder.loadTexts:
    exchangeScheduleIntervalTable.setStatus("current")
_ExchangeScheduleIntervalEntry_Object = MibTableRow
exchangeScheduleIntervalEntry = _ExchangeScheduleIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 22, 1)
)
exchangeScheduleIntervalEntry.setIndexNames(
    (0, "INFORMANT-WMI-EXCHANGE", "exsiIndex"),
)
if mibBuilder.loadTexts:
    exchangeScheduleIntervalEntry.setStatus("current")


class _ExsiIndex_Type(Integer32):
    """Custom type exsiIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ExsiIndex_Type.__name__ = "Integer32"
_ExsiIndex_Object = MibTableColumn
exsiIndex = _ExsiIndex_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 22, 1, 1),
    _ExsiIndex_Type()
)
exsiIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exsiIndex.setStatus("current")
_ExsiStartTime_Type = DateAndTime
_ExsiStartTime_Object = MibTableColumn
exsiStartTime = _ExsiStartTime_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 22, 1, 2),
    _ExsiStartTime_Type()
)
exsiStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exsiStartTime.setStatus("current")
_ExsiStopTime_Type = DateAndTime
_ExsiStopTime_Object = MibTableColumn
exsiStopTime = _ExsiStopTime_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 22, 1, 3),
    _ExsiStopTime_Type()
)
exsiStopTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exsiStopTime.setStatus("current")
_ExchangeSMTPLinkTable_Object = MibTable
exchangeSMTPLinkTable = _ExchangeSMTPLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 23)
)
if mibBuilder.loadTexts:
    exchangeSMTPLinkTable.setStatus("current")
_ExchangeSMTPLinkEntry_Object = MibTableRow
exchangeSMTPLinkEntry = _ExchangeSMTPLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 23, 1)
)
exchangeSMTPLinkEntry.setIndexNames(
    (0, "INFORMANT-WMI-EXCHANGE", "exslIndex"),
)
if mibBuilder.loadTexts:
    exchangeSMTPLinkEntry.setStatus("current")


class _ExslIndex_Type(Integer32):
    """Custom type exslIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ExslIndex_Type.__name__ = "Integer32"
_ExslIndex_Object = MibTableColumn
exslIndex = _ExslIndex_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 23, 1, 1),
    _ExslIndex_Type()
)
exslIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exslIndex.setStatus("current")
_ExslActionFreeze_Type = TruthValue
_ExslActionFreeze_Object = MibTableColumn
exslActionFreeze = _ExslActionFreeze_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 23, 1, 2),
    _ExslActionFreeze_Type()
)
exslActionFreeze.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exslActionFreeze.setStatus("current")
_ExslActionKick_Type = TruthValue
_ExslActionKick_Object = MibTableColumn
exslActionKick = _ExslActionKick_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 23, 1, 3),
    _ExslActionKick_Type()
)
exslActionKick.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exslActionKick.setStatus("current")
_ExslActionThaw_Type = TruthValue
_ExslActionThaw_Object = MibTableColumn
exslActionThaw = _ExslActionThaw_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 23, 1, 4),
    _ExslActionThaw_Type()
)
exslActionThaw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exslActionThaw.setStatus("current")
_ExslExtendedStateInfo_Type = WtcsDisplayString
_ExslExtendedStateInfo_Object = MibTableColumn
exslExtendedStateInfo = _ExslExtendedStateInfo_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 23, 1, 5),
    _ExslExtendedStateInfo_Type()
)
exslExtendedStateInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exslExtendedStateInfo.setStatus("current")
_ExslGlobalStop_Type = TruthValue
_ExslGlobalStop_Object = MibTableColumn
exslGlobalStop = _ExslGlobalStop_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 23, 1, 6),
    _ExslGlobalStop_Type()
)
exslGlobalStop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exslGlobalStop.setStatus("current")
_ExslLinkDN_Type = WtcsDisplayString
_ExslLinkDN_Object = MibTableColumn
exslLinkDN = _ExslLinkDN_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 23, 1, 7),
    _ExslLinkDN_Type()
)
exslLinkDN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exslLinkDN.setStatus("current")
_ExslLinkId_Type = WtcsDisplayString
_ExslLinkId_Object = MibTableColumn
exslLinkId = _ExslLinkId_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 23, 1, 8),
    _ExslLinkId_Type()
)
exslLinkId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exslLinkId.setStatus("current")
_ExslLinkName_Type = WtcsDisplayString
_ExslLinkName_Object = MibTableColumn
exslLinkName = _ExslLinkName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 23, 1, 9),
    _ExslLinkName_Type()
)
exslLinkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exslLinkName.setStatus("current")
_ExslMessageCount_Type = Gauge32
_ExslMessageCount_Object = MibTableColumn
exslMessageCount = _ExslMessageCount_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 23, 1, 10),
    _ExslMessageCount_Type()
)
exslMessageCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exslMessageCount.setStatus("current")
_ExslNextScheduledConnection_Type = DateAndTime
_ExslNextScheduledConnection_Object = MibTableColumn
exslNextScheduledConnection = _ExslNextScheduledConnection_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 23, 1, 11),
    _ExslNextScheduledConnection_Type()
)
exslNextScheduledConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exslNextScheduledConnection.setStatus("current")
_ExslOldestMessage_Type = DateAndTime
_ExslOldestMessage_Object = MibTableColumn
exslOldestMessage = _ExslOldestMessage_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 23, 1, 12),
    _ExslOldestMessage_Type()
)
exslOldestMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exslOldestMessage.setStatus("current")
_ExslProtocolName_Type = WtcsDisplayString
_ExslProtocolName_Object = MibTableColumn
exslProtocolName = _ExslProtocolName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 23, 1, 13),
    _ExslProtocolName_Type()
)
exslProtocolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exslProtocolName.setStatus("current")
_ExslKSize_Type = Gauge32
_ExslKSize_Object = MibTableColumn
exslKSize = _ExslKSize_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 23, 1, 14),
    _ExslKSize_Type()
)
exslKSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exslKSize.setStatus("current")
if mibBuilder.loadTexts:
    exslKSize.setUnits("KB")
_ExslMSize_Type = Gauge32
_ExslMSize_Object = MibTableColumn
exslMSize = _ExslMSize_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 23, 1, 15),
    _ExslMSize_Type()
)
exslMSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exslMSize.setStatus("current")
if mibBuilder.loadTexts:
    exslMSize.setUnits("MB")
_ExslStateActive_Type = TruthValue
_ExslStateActive_Object = MibTableColumn
exslStateActive = _ExslStateActive_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 23, 1, 16),
    _ExslStateActive_Type()
)
exslStateActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exslStateActive.setStatus("current")
_ExslStateFlags_Type = Gauge32
_ExslStateFlags_Object = MibTableColumn
exslStateFlags = _ExslStateFlags_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 23, 1, 17),
    _ExslStateFlags_Type()
)
exslStateFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exslStateFlags.setStatus("current")
_ExslStateFrozen_Type = TruthValue
_ExslStateFrozen_Object = MibTableColumn
exslStateFrozen = _ExslStateFrozen_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 23, 1, 18),
    _ExslStateFrozen_Type()
)
exslStateFrozen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exslStateFrozen.setStatus("current")
_ExslStateReady_Type = TruthValue
_ExslStateReady_Object = MibTableColumn
exslStateReady = _ExslStateReady_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 23, 1, 19),
    _ExslStateReady_Type()
)
exslStateReady.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exslStateReady.setStatus("current")
_ExslStateRemote_Type = TruthValue
_ExslStateRemote_Object = MibTableColumn
exslStateRemote = _ExslStateRemote_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 23, 1, 20),
    _ExslStateRemote_Type()
)
exslStateRemote.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exslStateRemote.setStatus("current")
_ExslStateRetry_Type = TruthValue
_ExslStateRetry_Object = MibTableColumn
exslStateRetry = _ExslStateRetry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 23, 1, 21),
    _ExslStateRetry_Type()
)
exslStateRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exslStateRetry.setStatus("current")
_ExslStateScheduled_Type = TruthValue
_ExslStateScheduled_Object = MibTableColumn
exslStateScheduled = _ExslStateScheduled_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 23, 1, 22),
    _ExslStateScheduled_Type()
)
exslStateScheduled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exslStateScheduled.setStatus("current")
_ExslSupportedLinkActions_Type = Gauge32
_ExslSupportedLinkActions_Object = MibTableColumn
exslSupportedLinkActions = _ExslSupportedLinkActions_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 23, 1, 23),
    _ExslSupportedLinkActions_Type()
)
exslSupportedLinkActions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exslSupportedLinkActions.setStatus("current")
_ExslTypeCurrentlyUnreachable_Type = TruthValue
_ExslTypeCurrentlyUnreachable_Object = MibTableColumn
exslTypeCurrentlyUnreachable = _ExslTypeCurrentlyUnreachable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 23, 1, 24),
    _ExslTypeCurrentlyUnreachable_Type()
)
exslTypeCurrentlyUnreachable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exslTypeCurrentlyUnreachable.setStatus("current")
_ExslTypeDeferredDelivery_Type = TruthValue
_ExslTypeDeferredDelivery_Object = MibTableColumn
exslTypeDeferredDelivery = _ExslTypeDeferredDelivery_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 23, 1, 25),
    _ExslTypeDeferredDelivery_Type()
)
exslTypeDeferredDelivery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exslTypeDeferredDelivery.setStatus("current")
_ExslTypeInternal_Type = TruthValue
_ExslTypeInternal_Object = MibTableColumn
exslTypeInternal = _ExslTypeInternal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 23, 1, 26),
    _ExslTypeInternal_Type()
)
exslTypeInternal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exslTypeInternal.setStatus("current")
_ExslTypeLocalDelivery_Type = TruthValue
_ExslTypeLocalDelivery_Object = MibTableColumn
exslTypeLocalDelivery = _ExslTypeLocalDelivery_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 23, 1, 27),
    _ExslTypeLocalDelivery_Type()
)
exslTypeLocalDelivery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exslTypeLocalDelivery.setStatus("current")
_ExslTypePendingCategorization_Type = TruthValue
_ExslTypePendingCategorization_Object = MibTableColumn
exslTypePendingCategorization = _ExslTypePendingCategorization_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 23, 1, 28),
    _ExslTypePendingCategorization_Type()
)
exslTypePendingCategorization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exslTypePendingCategorization.setStatus("current")
_ExslTypePendingRouting_Type = TruthValue
_ExslTypePendingRouting_Object = MibTableColumn
exslTypePendingRouting = _ExslTypePendingRouting_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 23, 1, 29),
    _ExslTypePendingRouting_Type()
)
exslTypePendingRouting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exslTypePendingRouting.setStatus("current")
_ExslTypePendingSubmission_Type = TruthValue
_ExslTypePendingSubmission_Object = MibTableColumn
exslTypePendingSubmission = _ExslTypePendingSubmission_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 23, 1, 30),
    _ExslTypePendingSubmission_Type()
)
exslTypePendingSubmission.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exslTypePendingSubmission.setStatus("current")
_ExslTypeRemoteDelivery_Type = TruthValue
_ExslTypeRemoteDelivery_Object = MibTableColumn
exslTypeRemoteDelivery = _ExslTypeRemoteDelivery_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 23, 1, 31),
    _ExslTypeRemoteDelivery_Type()
)
exslTypeRemoteDelivery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exslTypeRemoteDelivery.setStatus("current")
_ExslVersion_Type = Gauge32
_ExslVersion_Object = MibTableColumn
exslVersion = _ExslVersion_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 23, 1, 32),
    _ExslVersion_Type()
)
exslVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exslVersion.setStatus("current")
_ExslVirtualMachine_Type = WtcsDisplayString
_ExslVirtualMachine_Object = MibTableColumn
exslVirtualMachine = _ExslVirtualMachine_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 23, 1, 33),
    _ExslVirtualMachine_Type()
)
exslVirtualMachine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exslVirtualMachine.setStatus("current")
_ExslVirtualServerName_Type = WtcsDisplayString
_ExslVirtualServerName_Object = MibTableColumn
exslVirtualServerName = _ExslVirtualServerName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 23, 1, 34),
    _ExslVirtualServerName_Type()
)
exslVirtualServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exslVirtualServerName.setStatus("current")
_ExchangeSMTPQueueTable_Object = MibTable
exchangeSMTPQueueTable = _ExchangeSMTPQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 24)
)
if mibBuilder.loadTexts:
    exchangeSMTPQueueTable.setStatus("current")
_ExchangeSMTPQueueEntry_Object = MibTableRow
exchangeSMTPQueueEntry = _ExchangeSMTPQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 24, 1)
)
exchangeSMTPQueueEntry.setIndexNames(
    (0, "INFORMANT-WMI-EXCHANGE", "exsqIndex"),
)
if mibBuilder.loadTexts:
    exchangeSMTPQueueEntry.setStatus("current")


class _ExsqIndex_Type(Integer32):
    """Custom type exsqIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ExsqIndex_Type.__name__ = "Integer32"
_ExsqIndex_Object = MibTableColumn
exsqIndex = _ExsqIndex_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 24, 1, 1),
    _ExsqIndex_Type()
)
exsqIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exsqIndex.setStatus("current")
_ExsqCanEnumAll_Type = TruthValue
_ExsqCanEnumAll_Object = MibTableColumn
exsqCanEnumAll = _ExsqCanEnumAll_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 24, 1, 2),
    _ExsqCanEnumAll_Type()
)
exsqCanEnumAll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exsqCanEnumAll.setStatus("current")
_ExsqGlobalStop_Type = TruthValue
_ExsqGlobalStop_Object = MibTableColumn
exsqGlobalStop = _ExsqGlobalStop_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 24, 1, 3),
    _ExsqGlobalStop_Type()
)
exsqGlobalStop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exsqGlobalStop.setStatus("current")
_ExsqLinkId_Type = WtcsDisplayString
_ExsqLinkId_Object = MibTableColumn
exsqLinkId = _ExsqLinkId_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 24, 1, 4),
    _ExsqLinkId_Type()
)
exsqLinkId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exsqLinkId.setStatus("current")
_ExsqLinkName_Type = WtcsDisplayString
_ExsqLinkName_Object = MibTableColumn
exsqLinkName = _ExsqLinkName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 24, 1, 5),
    _ExsqLinkName_Type()
)
exsqLinkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exsqLinkName.setStatus("current")
_ExsqMessageCount_Type = Gauge32
_ExsqMessageCount_Object = MibTableColumn
exsqMessageCount = _ExsqMessageCount_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 24, 1, 6),
    _ExsqMessageCount_Type()
)
exsqMessageCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exsqMessageCount.setStatus("current")
_ExsqMsgEnumFlagsSupported_Type = Gauge32
_ExsqMsgEnumFlagsSupported_Object = MibTableColumn
exsqMsgEnumFlagsSupported = _ExsqMsgEnumFlagsSupported_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 24, 1, 7),
    _ExsqMsgEnumFlagsSupported_Type()
)
exsqMsgEnumFlagsSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exsqMsgEnumFlagsSupported.setStatus("current")
_ExsqProtocolName_Type = WtcsDisplayString
_ExsqProtocolName_Object = MibTableColumn
exsqProtocolName = _ExsqProtocolName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 24, 1, 8),
    _ExsqProtocolName_Type()
)
exsqProtocolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exsqProtocolName.setStatus("current")
_ExsqQueueId_Type = WtcsDisplayString
_ExsqQueueId_Object = MibTableColumn
exsqQueueId = _ExsqQueueId_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 24, 1, 9),
    _ExsqQueueId_Type()
)
exsqQueueId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exsqQueueId.setStatus("current")
_ExsqQueueName_Type = WtcsDisplayString
_ExsqQueueName_Object = MibTableColumn
exsqQueueName = _ExsqQueueName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 24, 1, 10),
    _ExsqQueueName_Type()
)
exsqQueueName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exsqQueueName.setStatus("current")
_ExsqKSize_Type = Gauge32
_ExsqKSize_Object = MibTableColumn
exsqKSize = _ExsqKSize_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 24, 1, 11),
    _ExsqKSize_Type()
)
exsqKSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exsqKSize.setStatus("current")
if mibBuilder.loadTexts:
    exsqKSize.setUnits("KB")
_ExsqMSize_Type = Gauge32
_ExsqMSize_Object = MibTableColumn
exsqMSize = _ExsqMSize_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 24, 1, 12),
    _ExsqMSize_Type()
)
exsqMSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exsqMSize.setStatus("current")
if mibBuilder.loadTexts:
    exsqMSize.setUnits("MB")
_ExsqVersion_Type = Gauge32
_ExsqVersion_Object = MibTableColumn
exsqVersion = _ExsqVersion_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 24, 1, 13),
    _ExsqVersion_Type()
)
exsqVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exsqVersion.setStatus("current")
_ExsqVirtualMachine_Type = WtcsDisplayString
_ExsqVirtualMachine_Object = MibTableColumn
exsqVirtualMachine = _ExsqVirtualMachine_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 24, 1, 14),
    _ExsqVirtualMachine_Type()
)
exsqVirtualMachine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exsqVirtualMachine.setStatus("current")
_ExsqVirtualServerName_Type = WtcsDisplayString
_ExsqVirtualServerName_Object = MibTableColumn
exsqVirtualServerName = _ExsqVirtualServerName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 24, 1, 15),
    _ExsqVirtualServerName_Type()
)
exsqVirtualServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exsqVirtualServerName.setStatus("current")
_ExchangeX400LinkTable_Object = MibTable
exchangeX400LinkTable = _ExchangeX400LinkTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 25)
)
if mibBuilder.loadTexts:
    exchangeX400LinkTable.setStatus("current")
_ExchangeX400LinkEntry_Object = MibTableRow
exchangeX400LinkEntry = _ExchangeX400LinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 25, 1)
)
exchangeX400LinkEntry.setIndexNames(
    (0, "INFORMANT-WMI-EXCHANGE", "exxlIndex"),
)
if mibBuilder.loadTexts:
    exchangeX400LinkEntry.setStatus("current")


class _ExxlIndex_Type(Integer32):
    """Custom type exxlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ExxlIndex_Type.__name__ = "Integer32"
_ExxlIndex_Object = MibTableColumn
exxlIndex = _ExxlIndex_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 25, 1, 1),
    _ExxlIndex_Type()
)
exxlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exxlIndex.setStatus("current")
_ExxlActionFreeze_Type = TruthValue
_ExxlActionFreeze_Object = MibTableColumn
exxlActionFreeze = _ExxlActionFreeze_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 25, 1, 2),
    _ExxlActionFreeze_Type()
)
exxlActionFreeze.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exxlActionFreeze.setStatus("current")
_ExxlActionKick_Type = TruthValue
_ExxlActionKick_Object = MibTableColumn
exxlActionKick = _ExxlActionKick_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 25, 1, 3),
    _ExxlActionKick_Type()
)
exxlActionKick.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exxlActionKick.setStatus("current")
_ExxlActionThaw_Type = TruthValue
_ExxlActionThaw_Object = MibTableColumn
exxlActionThaw = _ExxlActionThaw_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 25, 1, 4),
    _ExxlActionThaw_Type()
)
exxlActionThaw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exxlActionThaw.setStatus("current")
_ExxlExtendedStateInfo_Type = WtcsDisplayString
_ExxlExtendedStateInfo_Object = MibTableColumn
exxlExtendedStateInfo = _ExxlExtendedStateInfo_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 25, 1, 5),
    _ExxlExtendedStateInfo_Type()
)
exxlExtendedStateInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exxlExtendedStateInfo.setStatus("current")
_ExxlGlobalStop_Type = TruthValue
_ExxlGlobalStop_Object = MibTableColumn
exxlGlobalStop = _ExxlGlobalStop_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 25, 1, 6),
    _ExxlGlobalStop_Type()
)
exxlGlobalStop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exxlGlobalStop.setStatus("current")
_ExxlLinkDN_Type = WtcsDisplayString
_ExxlLinkDN_Object = MibTableColumn
exxlLinkDN = _ExxlLinkDN_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 25, 1, 7),
    _ExxlLinkDN_Type()
)
exxlLinkDN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exxlLinkDN.setStatus("current")
_ExxlLinkId_Type = WtcsDisplayString
_ExxlLinkId_Object = MibTableColumn
exxlLinkId = _ExxlLinkId_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 25, 1, 8),
    _ExxlLinkId_Type()
)
exxlLinkId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exxlLinkId.setStatus("current")
_ExxlLinkName_Type = WtcsDisplayString
_ExxlLinkName_Object = MibTableColumn
exxlLinkName = _ExxlLinkName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 25, 1, 9),
    _ExxlLinkName_Type()
)
exxlLinkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exxlLinkName.setStatus("current")
_ExxlMessageCount_Type = Gauge32
_ExxlMessageCount_Object = MibTableColumn
exxlMessageCount = _ExxlMessageCount_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 25, 1, 10),
    _ExxlMessageCount_Type()
)
exxlMessageCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exxlMessageCount.setStatus("current")
_ExxlNextScheduledConnection_Type = DateAndTime
_ExxlNextScheduledConnection_Object = MibTableColumn
exxlNextScheduledConnection = _ExxlNextScheduledConnection_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 25, 1, 11),
    _ExxlNextScheduledConnection_Type()
)
exxlNextScheduledConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exxlNextScheduledConnection.setStatus("current")
_ExxlOldestMessage_Type = DateAndTime
_ExxlOldestMessage_Object = MibTableColumn
exxlOldestMessage = _ExxlOldestMessage_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 25, 1, 12),
    _ExxlOldestMessage_Type()
)
exxlOldestMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exxlOldestMessage.setStatus("current")
_ExxlProtocolName_Type = WtcsDisplayString
_ExxlProtocolName_Object = MibTableColumn
exxlProtocolName = _ExxlProtocolName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 25, 1, 13),
    _ExxlProtocolName_Type()
)
exxlProtocolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exxlProtocolName.setStatus("current")
_ExxlKSize_Type = Gauge32
_ExxlKSize_Object = MibTableColumn
exxlKSize = _ExxlKSize_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 25, 1, 14),
    _ExxlKSize_Type()
)
exxlKSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exxlKSize.setStatus("current")
if mibBuilder.loadTexts:
    exxlKSize.setUnits("KB")
_ExxlMSize_Type = Gauge32
_ExxlMSize_Object = MibTableColumn
exxlMSize = _ExxlMSize_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 25, 1, 15),
    _ExxlMSize_Type()
)
exxlMSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exxlMSize.setStatus("current")
if mibBuilder.loadTexts:
    exxlMSize.setUnits("MB")
_ExxlStateActive_Type = TruthValue
_ExxlStateActive_Object = MibTableColumn
exxlStateActive = _ExxlStateActive_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 25, 1, 16),
    _ExxlStateActive_Type()
)
exxlStateActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exxlStateActive.setStatus("current")
_ExxlStateFlags_Type = Gauge32
_ExxlStateFlags_Object = MibTableColumn
exxlStateFlags = _ExxlStateFlags_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 25, 1, 17),
    _ExxlStateFlags_Type()
)
exxlStateFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exxlStateFlags.setStatus("current")
_ExxlStateFrozen_Type = TruthValue
_ExxlStateFrozen_Object = MibTableColumn
exxlStateFrozen = _ExxlStateFrozen_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 25, 1, 18),
    _ExxlStateFrozen_Type()
)
exxlStateFrozen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exxlStateFrozen.setStatus("current")
_ExxlStateReady_Type = TruthValue
_ExxlStateReady_Object = MibTableColumn
exxlStateReady = _ExxlStateReady_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 25, 1, 19),
    _ExxlStateReady_Type()
)
exxlStateReady.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exxlStateReady.setStatus("current")
_ExxlStateRemote_Type = TruthValue
_ExxlStateRemote_Object = MibTableColumn
exxlStateRemote = _ExxlStateRemote_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 25, 1, 20),
    _ExxlStateRemote_Type()
)
exxlStateRemote.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exxlStateRemote.setStatus("current")
_ExxlStateRetry_Type = TruthValue
_ExxlStateRetry_Object = MibTableColumn
exxlStateRetry = _ExxlStateRetry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 25, 1, 21),
    _ExxlStateRetry_Type()
)
exxlStateRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exxlStateRetry.setStatus("current")
_ExxlStateScheduled_Type = TruthValue
_ExxlStateScheduled_Object = MibTableColumn
exxlStateScheduled = _ExxlStateScheduled_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 25, 1, 22),
    _ExxlStateScheduled_Type()
)
exxlStateScheduled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exxlStateScheduled.setStatus("current")
_ExxlSupportedLinkActions_Type = Gauge32
_ExxlSupportedLinkActions_Object = MibTableColumn
exxlSupportedLinkActions = _ExxlSupportedLinkActions_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 25, 1, 23),
    _ExxlSupportedLinkActions_Type()
)
exxlSupportedLinkActions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exxlSupportedLinkActions.setStatus("current")
_ExxlTypeCurrentlyUnreachable_Type = TruthValue
_ExxlTypeCurrentlyUnreachable_Object = MibTableColumn
exxlTypeCurrentlyUnreachable = _ExxlTypeCurrentlyUnreachable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 25, 1, 24),
    _ExxlTypeCurrentlyUnreachable_Type()
)
exxlTypeCurrentlyUnreachable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exxlTypeCurrentlyUnreachable.setStatus("current")
_ExxlTypeDeferredDelivery_Type = TruthValue
_ExxlTypeDeferredDelivery_Object = MibTableColumn
exxlTypeDeferredDelivery = _ExxlTypeDeferredDelivery_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 25, 1, 25),
    _ExxlTypeDeferredDelivery_Type()
)
exxlTypeDeferredDelivery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exxlTypeDeferredDelivery.setStatus("current")
_ExxlTypeInternal_Type = TruthValue
_ExxlTypeInternal_Object = MibTableColumn
exxlTypeInternal = _ExxlTypeInternal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 25, 1, 26),
    _ExxlTypeInternal_Type()
)
exxlTypeInternal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exxlTypeInternal.setStatus("current")
_ExxlTypeLocalDelivery_Type = TruthValue
_ExxlTypeLocalDelivery_Object = MibTableColumn
exxlTypeLocalDelivery = _ExxlTypeLocalDelivery_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 25, 1, 27),
    _ExxlTypeLocalDelivery_Type()
)
exxlTypeLocalDelivery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exxlTypeLocalDelivery.setStatus("current")
_ExxlTypePendingCategorization_Type = TruthValue
_ExxlTypePendingCategorization_Object = MibTableColumn
exxlTypePendingCategorization = _ExxlTypePendingCategorization_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 25, 1, 28),
    _ExxlTypePendingCategorization_Type()
)
exxlTypePendingCategorization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exxlTypePendingCategorization.setStatus("current")
_ExxlTypePendingRouting_Type = TruthValue
_ExxlTypePendingRouting_Object = MibTableColumn
exxlTypePendingRouting = _ExxlTypePendingRouting_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 25, 1, 29),
    _ExxlTypePendingRouting_Type()
)
exxlTypePendingRouting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exxlTypePendingRouting.setStatus("current")
_ExxlTypePendingSubmission_Type = TruthValue
_ExxlTypePendingSubmission_Object = MibTableColumn
exxlTypePendingSubmission = _ExxlTypePendingSubmission_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 25, 1, 30),
    _ExxlTypePendingSubmission_Type()
)
exxlTypePendingSubmission.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exxlTypePendingSubmission.setStatus("current")
_ExxlTypeRemoteDelivery_Type = TruthValue
_ExxlTypeRemoteDelivery_Object = MibTableColumn
exxlTypeRemoteDelivery = _ExxlTypeRemoteDelivery_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 25, 1, 31),
    _ExxlTypeRemoteDelivery_Type()
)
exxlTypeRemoteDelivery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exxlTypeRemoteDelivery.setStatus("current")
_ExxlVersion_Type = Gauge32
_ExxlVersion_Object = MibTableColumn
exxlVersion = _ExxlVersion_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 25, 1, 32),
    _ExxlVersion_Type()
)
exxlVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exxlVersion.setStatus("current")
_ExxlVirtualMachine_Type = WtcsDisplayString
_ExxlVirtualMachine_Object = MibTableColumn
exxlVirtualMachine = _ExxlVirtualMachine_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 25, 1, 33),
    _ExxlVirtualMachine_Type()
)
exxlVirtualMachine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exxlVirtualMachine.setStatus("current")
_ExxlVirtualServerName_Type = WtcsDisplayString
_ExxlVirtualServerName_Object = MibTableColumn
exxlVirtualServerName = _ExxlVirtualServerName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 25, 1, 34),
    _ExxlVirtualServerName_Type()
)
exxlVirtualServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exxlVirtualServerName.setStatus("current")
_ExchangeX400QueueTable_Object = MibTable
exchangeX400QueueTable = _ExchangeX400QueueTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 26)
)
if mibBuilder.loadTexts:
    exchangeX400QueueTable.setStatus("current")
_ExchangeX400QueueEntry_Object = MibTableRow
exchangeX400QueueEntry = _ExchangeX400QueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 26, 1)
)
exchangeX400QueueEntry.setIndexNames(
    (0, "INFORMANT-WMI-EXCHANGE", "exxqIndex"),
)
if mibBuilder.loadTexts:
    exchangeX400QueueEntry.setStatus("current")


class _ExxqIndex_Type(Integer32):
    """Custom type exxqIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ExxqIndex_Type.__name__ = "Integer32"
_ExxqIndex_Object = MibTableColumn
exxqIndex = _ExxqIndex_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 26, 1, 1),
    _ExxqIndex_Type()
)
exxqIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exxqIndex.setStatus("current")
_ExxqCanEnumAll_Type = TruthValue
_ExxqCanEnumAll_Object = MibTableColumn
exxqCanEnumAll = _ExxqCanEnumAll_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 26, 1, 2),
    _ExxqCanEnumAll_Type()
)
exxqCanEnumAll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exxqCanEnumAll.setStatus("current")
_ExxqGlobalStop_Type = TruthValue
_ExxqGlobalStop_Object = MibTableColumn
exxqGlobalStop = _ExxqGlobalStop_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 26, 1, 3),
    _ExxqGlobalStop_Type()
)
exxqGlobalStop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exxqGlobalStop.setStatus("current")
_ExxqLinkId_Type = WtcsDisplayString
_ExxqLinkId_Object = MibTableColumn
exxqLinkId = _ExxqLinkId_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 26, 1, 4),
    _ExxqLinkId_Type()
)
exxqLinkId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exxqLinkId.setStatus("current")
_ExxqLinkName_Type = WtcsDisplayString
_ExxqLinkName_Object = MibTableColumn
exxqLinkName = _ExxqLinkName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 26, 1, 5),
    _ExxqLinkName_Type()
)
exxqLinkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exxqLinkName.setStatus("current")
_ExxqMessageCount_Type = Gauge32
_ExxqMessageCount_Object = MibTableColumn
exxqMessageCount = _ExxqMessageCount_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 26, 1, 6),
    _ExxqMessageCount_Type()
)
exxqMessageCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exxqMessageCount.setStatus("current")
_ExxqMsgEnumFlagsSupported_Type = Gauge32
_ExxqMsgEnumFlagsSupported_Object = MibTableColumn
exxqMsgEnumFlagsSupported = _ExxqMsgEnumFlagsSupported_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 26, 1, 7),
    _ExxqMsgEnumFlagsSupported_Type()
)
exxqMsgEnumFlagsSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exxqMsgEnumFlagsSupported.setStatus("current")
_ExxqProtocolName_Type = WtcsDisplayString
_ExxqProtocolName_Object = MibTableColumn
exxqProtocolName = _ExxqProtocolName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 26, 1, 8),
    _ExxqProtocolName_Type()
)
exxqProtocolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exxqProtocolName.setStatus("current")
_ExxqQueueId_Type = WtcsDisplayString
_ExxqQueueId_Object = MibTableColumn
exxqQueueId = _ExxqQueueId_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 26, 1, 9),
    _ExxqQueueId_Type()
)
exxqQueueId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exxqQueueId.setStatus("current")
_ExxqQueueName_Type = WtcsDisplayString
_ExxqQueueName_Object = MibTableColumn
exxqQueueName = _ExxqQueueName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 26, 1, 10),
    _ExxqQueueName_Type()
)
exxqQueueName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exxqQueueName.setStatus("current")
_ExxqKSize_Type = Gauge32
_ExxqKSize_Object = MibTableColumn
exxqKSize = _ExxqKSize_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 26, 1, 11),
    _ExxqKSize_Type()
)
exxqKSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exxqKSize.setStatus("current")
if mibBuilder.loadTexts:
    exxqKSize.setUnits("KB")
_ExxqMSize_Type = Gauge32
_ExxqMSize_Object = MibTableColumn
exxqMSize = _ExxqMSize_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 26, 1, 12),
    _ExxqMSize_Type()
)
exxqMSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exxqMSize.setStatus("current")
if mibBuilder.loadTexts:
    exxqMSize.setUnits("MB")
_ExxqVersion_Type = Gauge32
_ExxqVersion_Object = MibTableColumn
exxqVersion = _ExxqVersion_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 26, 1, 13),
    _ExxqVersion_Type()
)
exxqVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exxqVersion.setStatus("current")
_ExxqVirtualMachine_Type = WtcsDisplayString
_ExxqVirtualMachine_Object = MibTableColumn
exxqVirtualMachine = _ExxqVirtualMachine_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 26, 1, 14),
    _ExxqVirtualMachine_Type()
)
exxqVirtualMachine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exxqVirtualMachine.setStatus("current")
_ExxqVirtualServerName_Type = WtcsDisplayString
_ExxqVirtualServerName_Object = MibTableColumn
exxqVirtualServerName = _ExxqVirtualServerName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 23, 26, 1, 15),
    _ExxqVirtualServerName_Type()
)
exxqVirtualServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exxqVirtualServerName.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFORMANT-WMI-EXCHANGE",
    **{"wmiExchange": wmiExchange,
       "exchangeClusterResourceTable": exchangeClusterResourceTable,
       "exchangeClusterResourceEntry": exchangeClusterResourceEntry,
       "excrIndex": excrIndex,
       "excrName": excrName,
       "excrOwner": excrOwner,
       "excrState": excrState,
       "excrType": excrType,
       "excrVirtualMachine": excrVirtualMachine,
       "exchangeConnectorStateTable": exchangeConnectorStateTable,
       "exchangeConnectorStateEntry": exchangeConnectorStateEntry,
       "excsIndex": excsIndex,
       "excsDN": excsDN,
       "excsGroupDN": excsGroupDN,
       "excsGroupGUID": excsGroupGUID,
       "excsGUID": excsGUID,
       "excsIsUp": excsIsUp,
       "excsName": excsName,
       "exchangeLinkTable": exchangeLinkTable,
       "exchangeLinkEntry": exchangeLinkEntry,
       "exlIndex": exlIndex,
       "exlActionFreeze": exlActionFreeze,
       "exlActionKick": exlActionKick,
       "exlActionThaw": exlActionThaw,
       "exlExtendedStateInfo": exlExtendedStateInfo,
       "exlGlobalStop": exlGlobalStop,
       "exlIncreasingTime": exlIncreasingTime,
       "exlLinkDN": exlLinkDN,
       "exlLinkName": exlLinkName,
       "exlNextScheduledConnection": exlNextScheduledConnection,
       "exlNumberOfMessages": exlNumberOfMessages,
       "exlOldestMessage": exlOldestMessage,
       "exlProtocolName": exlProtocolName,
       "exlSizeOfQueue": exlSizeOfQueue,
       "exlStateActive": exlStateActive,
       "exlStateFlags": exlStateFlags,
       "exlStateFrozen": exlStateFrozen,
       "exlStateReady": exlStateReady,
       "exlStateRemote": exlStateRemote,
       "exlStateRetry": exlStateRetry,
       "exlStateScheduled": exlStateScheduled,
       "exlSupportedLinkActions": exlSupportedLinkActions,
       "exlTypeCurrentlyUnreachable": exlTypeCurrentlyUnreachable,
       "exlTypeDeferredDelivery": exlTypeDeferredDelivery,
       "exlTypeInternal": exlTypeInternal,
       "exlTypeLocalDelivery": exlTypeLocalDelivery,
       "exlTypePendingCategorization": exlTypePendingCategorization,
       "exlTypePendingRouting": exlTypePendingRouting,
       "exlTypePendingSubmission": exlTypePendingSubmission,
       "exlTypeRemoteDelivery": exlTypeRemoteDelivery,
       "exlVersion": exlVersion,
       "exlVirtualMachine": exlVirtualMachine,
       "exlVirtualServerName": exlVirtualServerName,
       "exchangeQueueTable": exchangeQueueTable,
       "exchangeQueueEntry": exchangeQueueEntry,
       "exqIndex": exqIndex,
       "exqCanEnumAll": exqCanEnumAll,
       "exqCanEnumFailed": exqCanEnumFailed,
       "exqCanEnumFirstNMessages": exqCanEnumFirstNMessages,
       "exqCanEnumFrozen": exqCanEnumFrozen,
       "exqCanEnumInvertSense": exqCanEnumInvertSense,
       "exqCanEnumLargerThan": exqCanEnumLargerThan,
       "exqCanEnumNLargestMessages": exqCanEnumNLargestMessages,
       "exqCanEnumNOldestMessages": exqCanEnumNOldestMessages,
       "exqCanEnumOlderThan": exqCanEnumOlderThan,
       "exqCanEnumRecipient": exqCanEnumRecipient,
       "exqCanEnumSender": exqCanEnumSender,
       "exqGlobalStop": exqGlobalStop,
       "exqIncreasingTime": exqIncreasingTime,
       "exqLinkName": exqLinkName,
       "exqMsgEnumFlagsSupported": exqMsgEnumFlagsSupported,
       "exqNumberOfMessages": exqNumberOfMessages,
       "exqProtocolName": exqProtocolName,
       "exqQueueName": exqQueueName,
       "exqSizeOfQueue": exqSizeOfQueue,
       "exqVersion": exqVersion,
       "exqVirtualMachine": exqVirtualMachine,
       "exqVirtualServerName": exqVirtualServerName,
       "exchangeServerStateTable": exchangeServerStateTable,
       "exchangeServerStateEntry": exchangeServerStateEntry,
       "exssIndex": exssIndex,
       "exssClusterState": exssClusterState,
       "exssClusterStateString": exssClusterStateString,
       "exssCPUState": exssCPUState,
       "exssCPUStateString": exssCPUStateString,
       "exssDisksState": exssDisksState,
       "exssDisksStateString": exssDisksStateString,
       "exssDN": exssDN,
       "exssGroupDN": exssGroupDN,
       "exssGroupGUID": exssGroupGUID,
       "exssGUID": exssGUID,
       "exssMemoryState": exssMemoryState,
       "exssMemoryStateString": exssMemoryStateString,
       "exssName": exssName,
       "exssQueuesState": exssQueuesState,
       "exssQueuesStateString": exssQueuesStateString,
       "exssServerMaintenance": exssServerMaintenance,
       "exssServerState": exssServerState,
       "exssServerStateString": exssServerStateString,
       "exssServicesState": exssServicesState,
       "exssServicesStateString": exssServicesStateString,
       "exssUnreachable": exssUnreachable,
       "exssVersion": exssVersion,
       "exchangeDSAccessDCTable": exchangeDSAccessDCTable,
       "exchangeDSAccessDCEntry": exchangeDSAccessDCEntry,
       "exdsIndex": exdsIndex,
       "exdsConfigurationType": exdsConfigurationType,
       "exdsIsFast": exdsIsFast,
       "exdsIsInSync": exdsIsInSync,
       "exdsIsUp": exdsIsUp,
       "exdsLDAPPort": exdsLDAPPort,
       "exdsName": exdsName,
       "exdsType": exdsType,
       "exchangeFolderTreeTable": exchangeFolderTreeTable,
       "exchangeFolderTreeEntry": exchangeFolderTreeEntry,
       "exftIndex": exftIndex,
       "exftAdministrativeGroup": exftAdministrativeGroup,
       "exftAdministrativeNote": exftAdministrativeNote,
       "exftAssociatedPublicStores": exftAssociatedPublicStores,
       "exftCreationTime": exftCreationTime,
       "exftGUID": exftGUID,
       "exftHasLocalPublicStore": exftHasLocalPublicStore,
       "exftLastModificationTime": exftLastModificationTime,
       "exftMapiFolderTree": exftMapiFolderTree,
       "exftName": exftName,
       "exftRootFolderURL": exftRootFolderURL,
       "exchangeLinkV2Table": exchangeLinkV2Table,
       "exchangeLinkV2Entry": exchangeLinkV2Entry,
       "exl2Index": exl2Index,
       "exl2ActionFreeze": exl2ActionFreeze,
       "exl2ActionKick": exl2ActionKick,
       "exl2ActionThaw": exl2ActionThaw,
       "exl2ExtendedStateInfo": exl2ExtendedStateInfo,
       "exl2GlobalStop": exl2GlobalStop,
       "exl2LinkDN": exl2LinkDN,
       "exl2LinkId": exl2LinkId,
       "exl2LinkName": exl2LinkName,
       "exl2MessageCount": exl2MessageCount,
       "exl2NextScheduledConnection": exl2NextScheduledConnection,
       "exl2OldestMessage": exl2OldestMessage,
       "exl2ProtocolName": exl2ProtocolName,
       "exl2Size": exl2Size,
       "exl2StateActive": exl2StateActive,
       "exl2StateFlags": exl2StateFlags,
       "exl2StateFrozen": exl2StateFrozen,
       "exl2StateReady": exl2StateReady,
       "exl2StateRemote": exl2StateRemote,
       "exl2StateRetry": exl2StateRetry,
       "exl2StateScheduled": exl2StateScheduled,
       "exl2SupportedLinkActions": exl2SupportedLinkActions,
       "exl2TypeCurrentlyUnreachable": exl2TypeCurrentlyUnreachable,
       "exl2TypeDeferredDelivery": exl2TypeDeferredDelivery,
       "exl2TypeInternal": exl2TypeInternal,
       "exl2TypeLocalDelivery": exl2TypeLocalDelivery,
       "exl2TypePendingCategorization": exl2TypePendingCategorization,
       "exl2TypePendingRouting": exl2TypePendingRouting,
       "exl2TypePendingSubmission": exl2TypePendingSubmission,
       "exl2TypeRemoteDelivery": exl2TypeRemoteDelivery,
       "exl2Version": exl2Version,
       "exl2VirtualMachine": exl2VirtualMachine,
       "exl2VirtualServerName": exl2VirtualServerName,
       "exchangeLogonTable": exchangeLogonTable,
       "exchangeLogonEntry": exchangeLogonEntry,
       "exloIndex": exloIndex,
       "exloAdapterSpeed": exloAdapterSpeed,
       "exloClientIP": exloClientIP,
       "exloClientMode": exloClientMode,
       "exloClientName": exloClientName,
       "exloClientVersion": exloClientVersion,
       "exloCodePageID": exloCodePageID,
       "exloFolderOperationRate": exloFolderOperationRate,
       "exloHostAddress": exloHostAddress,
       "exloLastOperationTime": exloLastOperationTime,
       "exloLatency": exloLatency,
       "exloLocaleID": exloLocaleID,
       "exloLoggedOnUserAccount": exloLoggedOnUserAccount,
       "exloLoggedOnUsersMailboxLegacyDN": exloLoggedOnUsersMailboxLegacyDN,
       "exloLogonTime": exloLogonTime,
       "exloMacAddress": exloMacAddress,
       "exloMailboxDisplayName": exloMailboxDisplayName,
       "exloMailboxLegacyDN": exloMailboxLegacyDN,
       "exloMessagingOperationRate": exloMessagingOperationRate,
       "exloOpenAttachmentCount": exloOpenAttachmentCount,
       "exloOpenFolderCount": exloOpenFolderCount,
       "exloOpenMessageCount": exloOpenMessageCount,
       "exloOtherOperationRate": exloOtherOperationRate,
       "exloProgressOperationRate": exloProgressOperationRate,
       "exloRowID": exloRowID,
       "exloRPCSucceeded": exloRPCSucceeded,
       "exloServerName": exloServerName,
       "exloStorageGroupName": exloStorageGroupName,
       "exloStoreName": exloStoreName,
       "exloStoreType": exloStoreType,
       "exloStreamOperationRate": exloStreamOperationRate,
       "exloTableOperationRate": exloTableOperationRate,
       "exloTotalOperationRate": exloTotalOperationRate,
       "exloTransferOperationRate": exloTransferOperationRate,
       "exchangeMailboxTable": exchangeMailboxTable,
       "exchangeMailboxEntry": exchangeMailboxEntry,
       "exmIndex": exmIndex,
       "exmAssocContentCount": exmAssocContentCount,
       "exmDateDiscoveredAbsentInDS": exmDateDiscoveredAbsentInDS,
       "exmDeletedMessageSizeExtended": exmDeletedMessageSizeExtended,
       "exmLastLoggedOnUserAccount": exmLastLoggedOnUserAccount,
       "exmLastLogoffTime": exmLastLogoffTime,
       "exmLastLogonTime": exmLastLogonTime,
       "exmLegacyDN": exmLegacyDN,
       "exmMailboxDisplayName": exmMailboxDisplayName,
       "exmMailboxGUID": exmMailboxGUID,
       "exmServerName": exmServerName,
       "exmSize": exmSize,
       "exmStorageGroupName": exmStorageGroupName,
       "exmStorageLimitInfo": exmStorageLimitInfo,
       "exmStoreName": exmStoreName,
       "exmTotalItems": exmTotalItems,
       "exchangeMessageTrackingTable": exchangeMessageTrackingTable,
       "exchangeMessageTrackingEntry": exchangeMessageTrackingEntry,
       "exmtIndex": exmtIndex,
       "exmtAttemptedPartnerServer": exmtAttemptedPartnerServer,
       "exmtClientIP": exmtClientIP,
       "exmtClientName": exmtClientName,
       "exmtCost": exmtCost,
       "exmtDeliveryTime": exmtDeliveryTime,
       "exmtEncrypted": exmtEncrypted,
       "exmtEntryType": exmtEntryType,
       "exmtExpansionDL": exmtExpansionDL,
       "exmtKeyID": exmtKeyID,
       "exmtLinkedMessageID": exmtLinkedMessageID,
       "exmtMessageID": exmtMessageID,
       "exmtOriginationTime": exmtOriginationTime,
       "exmtPartnerServer": exmtPartnerServer,
       "exmtPriority": exmtPriority,
       "exmtRecipientAddress": exmtRecipientAddress,
       "exmtRecipientCount": exmtRecipientCount,
       "exmtRecipientStatus": exmtRecipientStatus,
       "exmtSenderAddress": exmtSenderAddress,
       "exmtServerIP": exmtServerIP,
       "exmtServerName": exmtServerName,
       "exmtSize": exmtSize,
       "exmtSubject": exmtSubject,
       "exmtSubjectID": exmtSubjectID,
       "exmtTimeLogged": exmtTimeLogged,
       "exmtVersion": exmtVersion,
       "exchangePublicFolderTable": exchangePublicFolderTable,
       "exchangePublicFolderEntry": exchangePublicFolderEntry,
       "expfIndex": expfIndex,
       "expfAddressBookName": expfAddressBookName,
       "expfAdministrativeNote": expfAdministrativeNote,
       "expfAdminSecurityDescriptor": expfAdminSecurityDescriptor,
       "expfADProxyPath": expfADProxyPath,
       "expfAssociatedMessageCount": expfAssociatedMessageCount,
       "expfAttachmentCount": expfAttachmentCount,
       "expfCategorizationCount": expfCategorizationCount,
       "expfComment": expfComment,
       "expfContactCount": expfContactCount,
       "expfContainsRules": expfContainsRules,
       "expfCreationTime": expfCreationTime,
       "expfDeletedItemLifetime": expfDeletedItemLifetime,
       "expfFolderTree": expfFolderTree,
       "expfFriendlyUrl": expfFriendlyUrl,
       "expfHasChildren": expfHasChildren,
       "expfHasLocalReplica": expfHasLocalReplica,
       "expfIsMailEnabled": expfIsMailEnabled,
       "expfIsNormalFolder": expfIsNormalFolder,
       "expfIsPerUserReadDisabled": expfIsPerUserReadDisabled,
       "expfIsSearchFolder": expfIsSearchFolder,
       "expfIsSecureInSite": expfIsSecureInSite,
       "expfLastAccessTime": expfLastAccessTime,
       "expfLastModificationTime": expfLastModificationTime,
       "expfMaximumItemSize": expfMaximumItemSize,
       "expfMessageCount": expfMessageCount,
       "expfMessageWithAttachmentsCount": expfMessageWithAttachmentsCount,
       "expfName": expfName,
       "expfNormalMessageSize": expfNormalMessageSize,
       "expfOwnerCount": expfOwnerCount,
       "expfParentFriendlyUrl": expfParentFriendlyUrl,
       "expfPath": expfPath,
       "expfProhibitPostLimit": expfProhibitPostLimit,
       "expfPublishInAddressBook": expfPublishInAddressBook,
       "expfRecipientCountOnAssociateMsg": expfRecipientCountOnAssociateMsg,
       "expfRecipientCountOnNormalMsg": expfRecipientCountOnNormalMsg,
       "expfReplicaAgeLimit": expfReplicaAgeLimit,
       "expfReplicaList": expfReplicaList,
       "expfReplicationMessagePriority": expfReplicationMessagePriority,
       "expfReplicationSchedule": expfReplicationSchedule,
       "expfReplicationStyle": expfReplicationStyle,
       "expfRestrictionCount": expfRestrictionCount,
       "expfSecurityDescriptor": expfSecurityDescriptor,
       "expfStorageLimitStyle": expfStorageLimitStyle,
       "expfTargetAddress": expfTargetAddress,
       "expfTotalMessageSize": expfTotalMessageSize,
       "expfUrl": expfUrl,
       "expfUsePublicStoreAgeLimits": expfUsePublicStoreAgeLimits,
       "expfUsePublicStoreDelItemLifetm": expfUsePublicStoreDelItemLifetm,
       "expfWarningLimit": expfWarningLimit,
       "exchangeQueueV2Table": exchangeQueueV2Table,
       "exchangeQueueV2Entry": exchangeQueueV2Entry,
       "exq2Index": exq2Index,
       "exq2CanEnumAll": exq2CanEnumAll,
       "exq2GlobalStop": exq2GlobalStop,
       "exq2LinkId": exq2LinkId,
       "exq2LinkName": exq2LinkName,
       "exq2MessageCount": exq2MessageCount,
       "exq2MsgEnumFlagsSupported": exq2MsgEnumFlagsSupported,
       "exq2ProtocolName": exq2ProtocolName,
       "exq2QueueId": exq2QueueId,
       "exq2QueueName": exq2QueueName,
       "exq2Size": exq2Size,
       "exq2Version": exq2Version,
       "exq2VirtualMachine": exq2VirtualMachine,
       "exq2VirtualServerName": exq2VirtualServerName,
       "exchangeQueueCacheReloadEvtTable": exchangeQueueCacheReloadEvtTable,
       "exchangeQueueCacheReloadEvtEntry": exchangeQueueCacheReloadEvtEntry,
       "exqcreIndex": exqcreIndex,
       "exqcreReloadTime": exqcreReloadTime,
       "exchangeQueuedMessageTable": exchangeQueuedMessageTable,
       "exchangeQueuedMessageEntry": exchangeQueuedMessageEntry,
       "exqmIndex": exqmIndex,
       "exqmActionDeleteNDR": exqmActionDeleteNDR,
       "exqmActionDeleteNoNDR": exqmActionDeleteNoNDR,
       "exqmActionFreeze": exqmActionFreeze,
       "exqmActionThaw": exqmActionThaw,
       "exqmExpiry": exqmExpiry,
       "exqmHighPriority": exqmHighPriority,
       "exqmLinkId": exqmLinkId,
       "exqmLinkName": exqmLinkName,
       "exqmLowPriority": exqmLowPriority,
       "exqmMessageId": exqmMessageId,
       "exqmNormalPriority": exqmNormalPriority,
       "exqmProtocolName": exqmProtocolName,
       "exqmQueueId": exqmQueueId,
       "exqmQueueName": exqmQueueName,
       "exqmReceived": exqmReceived,
       "exqmRecipientCount": exqmRecipientCount,
       "exqmRecipients": exqmRecipients,
       "exqmSender": exqmSender,
       "exqmSize": exqmSize,
       "exqmStateFlags": exqmStateFlags,
       "exqmStateFrozen": exqmStateFrozen,
       "exqmStateRetry": exqmStateRetry,
       "exqmSubject": exqmSubject,
       "exqmSubmission": exqmSubmission,
       "exqmVersion": exqmVersion,
       "exqmVirtualMachine": exqmVirtualMachine,
       "exqmVirtualServerName": exqmVirtualServerName,
       "exchangeQueueVirtualServerTable": exchangeQueueVirtualServerTable,
       "exchangeQueueVirtualServerEntry": exchangeQueueVirtualServerEntry,
       "exvsIndex": exvsIndex,
       "exvsGlobalActionsSupported": exvsGlobalActionsSupported,
       "exvsGlobalStop": exvsGlobalStop,
       "exvsProtocolName": exvsProtocolName,
       "exvsVirtualMachine": exvsVirtualMachine,
       "exvsVirtualServerName": exvsVirtualServerName,
       "exchangeServerTable": exchangeServerTable,
       "exchangeServerEntry": exchangeServerEntry,
       "exsIndex": exsIndex,
       "exsAdministrativeGroup": exsAdministrativeGroup,
       "exsAdministrativeNote": exsAdministrativeNote,
       "exsCreationTime": exsCreationTime,
       "exsDN": exsDN,
       "exsExchangeVersion": exsExchangeVersion,
       "exsFQDN": exsFQDN,
       "exsGUID": exsGUID,
       "exsIsFrontEndServer": exsIsFrontEndServer,
       "exsLastModificationTime": exsLastModificationTime,
       "exsMessageTrackingEnabled": exsMessageTrackingEnabled,
       "exsMessageTrackingLogFileLifetm": exsMessageTrackingLogFileLifetm,
       "exsMessageTrackingLogFilePath": exsMessageTrackingLogFilePath,
       "exsMonitoringEnabled": exsMonitoringEnabled,
       "exsMTADataPath": exsMTADataPath,
       "exsName": exsName,
       "exsRoutingGroup": exsRoutingGroup,
       "exsSubjectLoggingEnabled": exsSubjectLoggingEnabled,
       "exsType": exsType,
       "exchangeQueuedSMTPMessageTable": exchangeQueuedSMTPMessageTable,
       "exchangeQueuedSMTPMessageEntry": exchangeQueuedSMTPMessageEntry,
       "exqsmIndex": exqsmIndex,
       "exqsmActionDeleteNDR": exqsmActionDeleteNDR,
       "exqsmActionDeleteNoNDR": exqsmActionDeleteNoNDR,
       "exqsmActionFreeze": exqsmActionFreeze,
       "exqsmActionThaw": exqsmActionThaw,
       "exqsmExpiry": exqsmExpiry,
       "exqsmHighPriority": exqsmHighPriority,
       "exqsmLinkId": exqsmLinkId,
       "exqsmLinkName": exqsmLinkName,
       "exqsmLowPriority": exqsmLowPriority,
       "exqsmMessageId": exqsmMessageId,
       "exqsmNormalPriority": exqsmNormalPriority,
       "exqsmProtocolName": exqsmProtocolName,
       "exqsmQueueId": exqsmQueueId,
       "exqsmQueueName": exqsmQueueName,
       "exqsmReceived": exqsmReceived,
       "exqsmRecipientCount": exqsmRecipientCount,
       "exqsmRecipients": exqsmRecipients,
       "exqsmSender": exqsmSender,
       "exqsmSize": exqsmSize,
       "exqsmStateFlags": exqsmStateFlags,
       "exqsmStateFrozen": exqsmStateFrozen,
       "exqsmStateRetry": exqsmStateRetry,
       "exqsmSubject": exqsmSubject,
       "exqsmSubmission": exqsmSubmission,
       "exqsmVersion": exqsmVersion,
       "exqsmVirtualMachine": exqsmVirtualMachine,
       "exqsmVirtualServerName": exqsmVirtualServerName,
       "exchangeQueuedX400MessageTable": exchangeQueuedX400MessageTable,
       "exchangeQueuedX400MessageEntry": exchangeQueuedX400MessageEntry,
       "exqxmIndex": exqxmIndex,
       "exqxmActionDeleteNDR": exqxmActionDeleteNDR,
       "exqxmActionDeleteNoNDR": exqxmActionDeleteNoNDR,
       "exqxmActionFreeze": exqxmActionFreeze,
       "exqxmActionThaw": exqxmActionThaw,
       "exqxmExpiry": exqxmExpiry,
       "exqxmHighPriority": exqxmHighPriority,
       "exqxmLinkId": exqxmLinkId,
       "exqxmLinkName": exqxmLinkName,
       "exqxmLowPriority": exqxmLowPriority,
       "exqxmMessageId": exqxmMessageId,
       "exqxmNormalPriority": exqxmNormalPriority,
       "exqxmProtocolName": exqxmProtocolName,
       "exqxmQueueId": exqxmQueueId,
       "exqxmQueueName": exqxmQueueName,
       "exqxmReceived": exqxmReceived,
       "exqxmRecipientCount": exqxmRecipientCount,
       "exqxmRecipients": exqxmRecipients,
       "exqxmSender": exqxmSender,
       "exqxmSize": exqxmSize,
       "exqxmStateFlags": exqxmStateFlags,
       "exqxmStateFrozen": exqxmStateFrozen,
       "exqxmStateRetry": exqxmStateRetry,
       "exqxmSubject": exqxmSubject,
       "exqxmSubmission": exqxmSubmission,
       "exqxmVersion": exqxmVersion,
       "exqxmVirtualMachine": exqxmVirtualMachine,
       "exqxmVirtualServerName": exqxmVirtualServerName,
       "exchangeQueueSMTPVirtualSrvTable": exchangeQueueSMTPVirtualSrvTable,
       "exchangeQueueSMTPVirtualSrvEntry": exchangeQueueSMTPVirtualSrvEntry,
       "exqsvsIndex": exqsvsIndex,
       "exqsvsGlobalActionsSupported": exqsvsGlobalActionsSupported,
       "exqsvsGlobalStop": exqsvsGlobalStop,
       "exqsvsProtocolName": exqsvsProtocolName,
       "exqsvsVirtualMachine": exqsvsVirtualMachine,
       "exqsvsVirtualServerName": exqsvsVirtualServerName,
       "exchangeQueueX400VirtualSrvTable": exchangeQueueX400VirtualSrvTable,
       "exchangeQueueX400VirtualSrvEntry": exchangeQueueX400VirtualSrvEntry,
       "exqxvsIndex": exqxvsIndex,
       "exqxvsGlobalActionsSupported": exqxvsGlobalActionsSupported,
       "exqxvsGlobalStop": exqxvsGlobalStop,
       "exqxvsProtocolName": exqxvsProtocolName,
       "exqxvsVirtualMachine": exqxvsVirtualMachine,
       "exqxvsVirtualServerName": exqxvsVirtualServerName,
       "exchangeScheduleIntervalTable": exchangeScheduleIntervalTable,
       "exchangeScheduleIntervalEntry": exchangeScheduleIntervalEntry,
       "exsiIndex": exsiIndex,
       "exsiStartTime": exsiStartTime,
       "exsiStopTime": exsiStopTime,
       "exchangeSMTPLinkTable": exchangeSMTPLinkTable,
       "exchangeSMTPLinkEntry": exchangeSMTPLinkEntry,
       "exslIndex": exslIndex,
       "exslActionFreeze": exslActionFreeze,
       "exslActionKick": exslActionKick,
       "exslActionThaw": exslActionThaw,
       "exslExtendedStateInfo": exslExtendedStateInfo,
       "exslGlobalStop": exslGlobalStop,
       "exslLinkDN": exslLinkDN,
       "exslLinkId": exslLinkId,
       "exslLinkName": exslLinkName,
       "exslMessageCount": exslMessageCount,
       "exslNextScheduledConnection": exslNextScheduledConnection,
       "exslOldestMessage": exslOldestMessage,
       "exslProtocolName": exslProtocolName,
       "exslKSize": exslKSize,
       "exslMSize": exslMSize,
       "exslStateActive": exslStateActive,
       "exslStateFlags": exslStateFlags,
       "exslStateFrozen": exslStateFrozen,
       "exslStateReady": exslStateReady,
       "exslStateRemote": exslStateRemote,
       "exslStateRetry": exslStateRetry,
       "exslStateScheduled": exslStateScheduled,
       "exslSupportedLinkActions": exslSupportedLinkActions,
       "exslTypeCurrentlyUnreachable": exslTypeCurrentlyUnreachable,
       "exslTypeDeferredDelivery": exslTypeDeferredDelivery,
       "exslTypeInternal": exslTypeInternal,
       "exslTypeLocalDelivery": exslTypeLocalDelivery,
       "exslTypePendingCategorization": exslTypePendingCategorization,
       "exslTypePendingRouting": exslTypePendingRouting,
       "exslTypePendingSubmission": exslTypePendingSubmission,
       "exslTypeRemoteDelivery": exslTypeRemoteDelivery,
       "exslVersion": exslVersion,
       "exslVirtualMachine": exslVirtualMachine,
       "exslVirtualServerName": exslVirtualServerName,
       "exchangeSMTPQueueTable": exchangeSMTPQueueTable,
       "exchangeSMTPQueueEntry": exchangeSMTPQueueEntry,
       "exsqIndex": exsqIndex,
       "exsqCanEnumAll": exsqCanEnumAll,
       "exsqGlobalStop": exsqGlobalStop,
       "exsqLinkId": exsqLinkId,
       "exsqLinkName": exsqLinkName,
       "exsqMessageCount": exsqMessageCount,
       "exsqMsgEnumFlagsSupported": exsqMsgEnumFlagsSupported,
       "exsqProtocolName": exsqProtocolName,
       "exsqQueueId": exsqQueueId,
       "exsqQueueName": exsqQueueName,
       "exsqKSize": exsqKSize,
       "exsqMSize": exsqMSize,
       "exsqVersion": exsqVersion,
       "exsqVirtualMachine": exsqVirtualMachine,
       "exsqVirtualServerName": exsqVirtualServerName,
       "exchangeX400LinkTable": exchangeX400LinkTable,
       "exchangeX400LinkEntry": exchangeX400LinkEntry,
       "exxlIndex": exxlIndex,
       "exxlActionFreeze": exxlActionFreeze,
       "exxlActionKick": exxlActionKick,
       "exxlActionThaw": exxlActionThaw,
       "exxlExtendedStateInfo": exxlExtendedStateInfo,
       "exxlGlobalStop": exxlGlobalStop,
       "exxlLinkDN": exxlLinkDN,
       "exxlLinkId": exxlLinkId,
       "exxlLinkName": exxlLinkName,
       "exxlMessageCount": exxlMessageCount,
       "exxlNextScheduledConnection": exxlNextScheduledConnection,
       "exxlOldestMessage": exxlOldestMessage,
       "exxlProtocolName": exxlProtocolName,
       "exxlKSize": exxlKSize,
       "exxlMSize": exxlMSize,
       "exxlStateActive": exxlStateActive,
       "exxlStateFlags": exxlStateFlags,
       "exxlStateFrozen": exxlStateFrozen,
       "exxlStateReady": exxlStateReady,
       "exxlStateRemote": exxlStateRemote,
       "exxlStateRetry": exxlStateRetry,
       "exxlStateScheduled": exxlStateScheduled,
       "exxlSupportedLinkActions": exxlSupportedLinkActions,
       "exxlTypeCurrentlyUnreachable": exxlTypeCurrentlyUnreachable,
       "exxlTypeDeferredDelivery": exxlTypeDeferredDelivery,
       "exxlTypeInternal": exxlTypeInternal,
       "exxlTypeLocalDelivery": exxlTypeLocalDelivery,
       "exxlTypePendingCategorization": exxlTypePendingCategorization,
       "exxlTypePendingRouting": exxlTypePendingRouting,
       "exxlTypePendingSubmission": exxlTypePendingSubmission,
       "exxlTypeRemoteDelivery": exxlTypeRemoteDelivery,
       "exxlVersion": exxlVersion,
       "exxlVirtualMachine": exxlVirtualMachine,
       "exxlVirtualServerName": exxlVirtualServerName,
       "exchangeX400QueueTable": exchangeX400QueueTable,
       "exchangeX400QueueEntry": exchangeX400QueueEntry,
       "exxqIndex": exxqIndex,
       "exxqCanEnumAll": exxqCanEnumAll,
       "exxqGlobalStop": exxqGlobalStop,
       "exxqLinkId": exxqLinkId,
       "exxqLinkName": exxqLinkName,
       "exxqMessageCount": exxqMessageCount,
       "exxqMsgEnumFlagsSupported": exxqMsgEnumFlagsSupported,
       "exxqProtocolName": exxqProtocolName,
       "exxqQueueId": exxqQueueId,
       "exxqQueueName": exxqQueueName,
       "exxqKSize": exxqKSize,
       "exxqMSize": exxqMSize,
       "exxqVersion": exxqVersion,
       "exxqVirtualMachine": exxqVirtualMachine,
       "exxqVirtualServerName": exxqVirtualServerName}
)
