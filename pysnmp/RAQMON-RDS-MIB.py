# SNMP MIB module (RAQMON-RDS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RAQMON-RDS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:44:45 2024
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

(Dscp,) = mibBuilder.importSymbols(
    "DIFFSERV-DSCP-TC",
    "Dscp")

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

(rmon,) = mibBuilder.importSymbols(
    "RMON-MIB",
    "rmon")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

raqmonDsMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 16, 32)
)
raqmonDsMIB.setRevisions(
        ("2006-10-10 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RaqmonDsNotifications_ObjectIdentity = ObjectIdentity
raqmonDsNotifications = _RaqmonDsNotifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 32, 0)
)
_RaqmonDsMIBObjects_ObjectIdentity = ObjectIdentity
raqmonDsMIBObjects = _RaqmonDsMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 32, 1)
)
_RaqmonDsNotificationTable_Object = MibTable
raqmonDsNotificationTable = _RaqmonDsNotificationTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 32, 1, 1)
)
if mibBuilder.loadTexts:
    raqmonDsNotificationTable.setStatus("current")
_RaqmonDsNotificationEntry_Object = MibTableRow
raqmonDsNotificationEntry = _RaqmonDsNotificationEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 32, 1, 1, 1)
)
raqmonDsNotificationEntry.setIndexNames(
    (0, "RAQMON-RDS-MIB", "raqmonDsDSRC"),
    (0, "RAQMON-RDS-MIB", "raqmonDsRCN"),
    (0, "RAQMON-RDS-MIB", "raqmonDsPeerAddrType"),
    (0, "RAQMON-RDS-MIB", "raqmonDsPeerAddr"),
)
if mibBuilder.loadTexts:
    raqmonDsNotificationEntry.setStatus("current")
_RaqmonDsDSRC_Type = Unsigned32
_RaqmonDsDSRC_Object = MibTableColumn
raqmonDsDSRC = _RaqmonDsDSRC_Object(
    (1, 3, 6, 1, 2, 1, 16, 32, 1, 1, 1, 1),
    _RaqmonDsDSRC_Type()
)
raqmonDsDSRC.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    raqmonDsDSRC.setStatus("current")


class _RaqmonDsRCN_Type(Unsigned32):
    """Custom type raqmonDsRCN based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_RaqmonDsRCN_Type.__name__ = "Unsigned32"
_RaqmonDsRCN_Object = MibTableColumn
raqmonDsRCN = _RaqmonDsRCN_Object(
    (1, 3, 6, 1, 2, 1, 16, 32, 1, 1, 1, 2),
    _RaqmonDsRCN_Type()
)
raqmonDsRCN.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    raqmonDsRCN.setStatus("current")
_RaqmonDsPeerAddrType_Type = InetAddressType
_RaqmonDsPeerAddrType_Object = MibTableColumn
raqmonDsPeerAddrType = _RaqmonDsPeerAddrType_Object(
    (1, 3, 6, 1, 2, 1, 16, 32, 1, 1, 1, 3),
    _RaqmonDsPeerAddrType_Type()
)
raqmonDsPeerAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    raqmonDsPeerAddrType.setStatus("current")
_RaqmonDsPeerAddr_Type = InetAddress
_RaqmonDsPeerAddr_Object = MibTableColumn
raqmonDsPeerAddr = _RaqmonDsPeerAddr_Object(
    (1, 3, 6, 1, 2, 1, 16, 32, 1, 1, 1, 4),
    _RaqmonDsPeerAddr_Type()
)
raqmonDsPeerAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    raqmonDsPeerAddr.setStatus("current")
_RaqmonDsAppName_Type = SnmpAdminString
_RaqmonDsAppName_Object = MibTableColumn
raqmonDsAppName = _RaqmonDsAppName_Object(
    (1, 3, 6, 1, 2, 1, 16, 32, 1, 1, 1, 5),
    _RaqmonDsAppName_Type()
)
raqmonDsAppName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    raqmonDsAppName.setStatus("current")
_RaqmonDsDataSourceDevicePort_Type = InetPortNumber
_RaqmonDsDataSourceDevicePort_Object = MibTableColumn
raqmonDsDataSourceDevicePort = _RaqmonDsDataSourceDevicePort_Object(
    (1, 3, 6, 1, 2, 1, 16, 32, 1, 1, 1, 6),
    _RaqmonDsDataSourceDevicePort_Type()
)
raqmonDsDataSourceDevicePort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    raqmonDsDataSourceDevicePort.setStatus("current")
_RaqmonDsReceiverDevicePort_Type = InetPortNumber
_RaqmonDsReceiverDevicePort_Object = MibTableColumn
raqmonDsReceiverDevicePort = _RaqmonDsReceiverDevicePort_Object(
    (1, 3, 6, 1, 2, 1, 16, 32, 1, 1, 1, 7),
    _RaqmonDsReceiverDevicePort_Type()
)
raqmonDsReceiverDevicePort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    raqmonDsReceiverDevicePort.setStatus("current")
_RaqmonDsSessionSetupDateTime_Type = DateAndTime
_RaqmonDsSessionSetupDateTime_Object = MibTableColumn
raqmonDsSessionSetupDateTime = _RaqmonDsSessionSetupDateTime_Object(
    (1, 3, 6, 1, 2, 1, 16, 32, 1, 1, 1, 8),
    _RaqmonDsSessionSetupDateTime_Type()
)
raqmonDsSessionSetupDateTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    raqmonDsSessionSetupDateTime.setStatus("current")


class _RaqmonDsSessionSetupDelay_Type(Unsigned32):
    """Custom type raqmonDsSessionSetupDelay based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RaqmonDsSessionSetupDelay_Type.__name__ = "Unsigned32"
_RaqmonDsSessionSetupDelay_Object = MibTableColumn
raqmonDsSessionSetupDelay = _RaqmonDsSessionSetupDelay_Object(
    (1, 3, 6, 1, 2, 1, 16, 32, 1, 1, 1, 9),
    _RaqmonDsSessionSetupDelay_Type()
)
raqmonDsSessionSetupDelay.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    raqmonDsSessionSetupDelay.setStatus("current")
if mibBuilder.loadTexts:
    raqmonDsSessionSetupDelay.setUnits("milliseconds")
_RaqmonDsSessionDuration_Type = Unsigned32
_RaqmonDsSessionDuration_Object = MibTableColumn
raqmonDsSessionDuration = _RaqmonDsSessionDuration_Object(
    (1, 3, 6, 1, 2, 1, 16, 32, 1, 1, 1, 10),
    _RaqmonDsSessionDuration_Type()
)
raqmonDsSessionDuration.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    raqmonDsSessionDuration.setStatus("current")
if mibBuilder.loadTexts:
    raqmonDsSessionDuration.setUnits("seconds")
_RaqmonDsSessionSetupStatus_Type = SnmpAdminString
_RaqmonDsSessionSetupStatus_Object = MibTableColumn
raqmonDsSessionSetupStatus = _RaqmonDsSessionSetupStatus_Object(
    (1, 3, 6, 1, 2, 1, 16, 32, 1, 1, 1, 11),
    _RaqmonDsSessionSetupStatus_Type()
)
raqmonDsSessionSetupStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    raqmonDsSessionSetupStatus.setStatus("current")
_RaqmonDsRoundTripEndToEndNetDelay_Type = Unsigned32
_RaqmonDsRoundTripEndToEndNetDelay_Object = MibTableColumn
raqmonDsRoundTripEndToEndNetDelay = _RaqmonDsRoundTripEndToEndNetDelay_Object(
    (1, 3, 6, 1, 2, 1, 16, 32, 1, 1, 1, 12),
    _RaqmonDsRoundTripEndToEndNetDelay_Type()
)
raqmonDsRoundTripEndToEndNetDelay.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    raqmonDsRoundTripEndToEndNetDelay.setStatus("current")
if mibBuilder.loadTexts:
    raqmonDsRoundTripEndToEndNetDelay.setUnits("milliseconds")
_RaqmonDsOneWayEndToEndNetDelay_Type = Unsigned32
_RaqmonDsOneWayEndToEndNetDelay_Object = MibTableColumn
raqmonDsOneWayEndToEndNetDelay = _RaqmonDsOneWayEndToEndNetDelay_Object(
    (1, 3, 6, 1, 2, 1, 16, 32, 1, 1, 1, 13),
    _RaqmonDsOneWayEndToEndNetDelay_Type()
)
raqmonDsOneWayEndToEndNetDelay.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    raqmonDsOneWayEndToEndNetDelay.setStatus("current")
if mibBuilder.loadTexts:
    raqmonDsOneWayEndToEndNetDelay.setUnits("milliseconds")


class _RaqmonDsApplicationDelay_Type(Unsigned32):
    """Custom type raqmonDsApplicationDelay based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RaqmonDsApplicationDelay_Type.__name__ = "Unsigned32"
_RaqmonDsApplicationDelay_Object = MibTableColumn
raqmonDsApplicationDelay = _RaqmonDsApplicationDelay_Object(
    (1, 3, 6, 1, 2, 1, 16, 32, 1, 1, 1, 14),
    _RaqmonDsApplicationDelay_Type()
)
raqmonDsApplicationDelay.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    raqmonDsApplicationDelay.setStatus("current")
if mibBuilder.loadTexts:
    raqmonDsApplicationDelay.setUnits("milliseconds")


class _RaqmonDsInterArrivalJitter_Type(Unsigned32):
    """Custom type raqmonDsInterArrivalJitter based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RaqmonDsInterArrivalJitter_Type.__name__ = "Unsigned32"
_RaqmonDsInterArrivalJitter_Object = MibTableColumn
raqmonDsInterArrivalJitter = _RaqmonDsInterArrivalJitter_Object(
    (1, 3, 6, 1, 2, 1, 16, 32, 1, 1, 1, 15),
    _RaqmonDsInterArrivalJitter_Type()
)
raqmonDsInterArrivalJitter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    raqmonDsInterArrivalJitter.setStatus("current")
if mibBuilder.loadTexts:
    raqmonDsInterArrivalJitter.setUnits("milliseconds")


class _RaqmonDsIPPacketDelayVariation_Type(Unsigned32):
    """Custom type raqmonDsIPPacketDelayVariation based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RaqmonDsIPPacketDelayVariation_Type.__name__ = "Unsigned32"
_RaqmonDsIPPacketDelayVariation_Object = MibTableColumn
raqmonDsIPPacketDelayVariation = _RaqmonDsIPPacketDelayVariation_Object(
    (1, 3, 6, 1, 2, 1, 16, 32, 1, 1, 1, 16),
    _RaqmonDsIPPacketDelayVariation_Type()
)
raqmonDsIPPacketDelayVariation.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    raqmonDsIPPacketDelayVariation.setStatus("current")
if mibBuilder.loadTexts:
    raqmonDsIPPacketDelayVariation.setUnits("milliseconds")
_RaqmonDsTotalPacketsReceived_Type = Counter32
_RaqmonDsTotalPacketsReceived_Object = MibTableColumn
raqmonDsTotalPacketsReceived = _RaqmonDsTotalPacketsReceived_Object(
    (1, 3, 6, 1, 2, 1, 16, 32, 1, 1, 1, 17),
    _RaqmonDsTotalPacketsReceived_Type()
)
raqmonDsTotalPacketsReceived.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    raqmonDsTotalPacketsReceived.setStatus("current")
if mibBuilder.loadTexts:
    raqmonDsTotalPacketsReceived.setUnits("packets")
_RaqmonDsTotalPacketsSent_Type = Counter32
_RaqmonDsTotalPacketsSent_Object = MibTableColumn
raqmonDsTotalPacketsSent = _RaqmonDsTotalPacketsSent_Object(
    (1, 3, 6, 1, 2, 1, 16, 32, 1, 1, 1, 18),
    _RaqmonDsTotalPacketsSent_Type()
)
raqmonDsTotalPacketsSent.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    raqmonDsTotalPacketsSent.setStatus("current")
if mibBuilder.loadTexts:
    raqmonDsTotalPacketsSent.setUnits("packets")
_RaqmonDsTotalOctetsReceived_Type = Counter32
_RaqmonDsTotalOctetsReceived_Object = MibTableColumn
raqmonDsTotalOctetsReceived = _RaqmonDsTotalOctetsReceived_Object(
    (1, 3, 6, 1, 2, 1, 16, 32, 1, 1, 1, 19),
    _RaqmonDsTotalOctetsReceived_Type()
)
raqmonDsTotalOctetsReceived.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    raqmonDsTotalOctetsReceived.setStatus("current")
if mibBuilder.loadTexts:
    raqmonDsTotalOctetsReceived.setUnits("octets")
_RaqmonDsTotalOctetsSent_Type = Counter32
_RaqmonDsTotalOctetsSent_Object = MibTableColumn
raqmonDsTotalOctetsSent = _RaqmonDsTotalOctetsSent_Object(
    (1, 3, 6, 1, 2, 1, 16, 32, 1, 1, 1, 20),
    _RaqmonDsTotalOctetsSent_Type()
)
raqmonDsTotalOctetsSent.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    raqmonDsTotalOctetsSent.setStatus("current")
if mibBuilder.loadTexts:
    raqmonDsTotalOctetsSent.setUnits("octets")
_RaqmonDsCumulativePacketLoss_Type = Counter32
_RaqmonDsCumulativePacketLoss_Object = MibTableColumn
raqmonDsCumulativePacketLoss = _RaqmonDsCumulativePacketLoss_Object(
    (1, 3, 6, 1, 2, 1, 16, 32, 1, 1, 1, 21),
    _RaqmonDsCumulativePacketLoss_Type()
)
raqmonDsCumulativePacketLoss.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    raqmonDsCumulativePacketLoss.setStatus("current")
if mibBuilder.loadTexts:
    raqmonDsCumulativePacketLoss.setUnits("packets")


class _RaqmonDsPacketLossFraction_Type(Unsigned32):
    """Custom type raqmonDsPacketLossFraction based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RaqmonDsPacketLossFraction_Type.__name__ = "Unsigned32"
_RaqmonDsPacketLossFraction_Object = MibTableColumn
raqmonDsPacketLossFraction = _RaqmonDsPacketLossFraction_Object(
    (1, 3, 6, 1, 2, 1, 16, 32, 1, 1, 1, 22),
    _RaqmonDsPacketLossFraction_Type()
)
raqmonDsPacketLossFraction.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    raqmonDsPacketLossFraction.setStatus("current")
if mibBuilder.loadTexts:
    raqmonDsPacketLossFraction.setUnits("percentage of packets sent")
_RaqmonDsCumulativeDiscards_Type = Counter32
_RaqmonDsCumulativeDiscards_Object = MibTableColumn
raqmonDsCumulativeDiscards = _RaqmonDsCumulativeDiscards_Object(
    (1, 3, 6, 1, 2, 1, 16, 32, 1, 1, 1, 23),
    _RaqmonDsCumulativeDiscards_Type()
)
raqmonDsCumulativeDiscards.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    raqmonDsCumulativeDiscards.setStatus("current")
if mibBuilder.loadTexts:
    raqmonDsCumulativeDiscards.setUnits("packets")


class _RaqmonDsDiscardsFraction_Type(Unsigned32):
    """Custom type raqmonDsDiscardsFraction based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RaqmonDsDiscardsFraction_Type.__name__ = "Unsigned32"
_RaqmonDsDiscardsFraction_Object = MibTableColumn
raqmonDsDiscardsFraction = _RaqmonDsDiscardsFraction_Object(
    (1, 3, 6, 1, 2, 1, 16, 32, 1, 1, 1, 24),
    _RaqmonDsDiscardsFraction_Type()
)
raqmonDsDiscardsFraction.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    raqmonDsDiscardsFraction.setStatus("current")
if mibBuilder.loadTexts:
    raqmonDsDiscardsFraction.setUnits("percentage of packets sent")


class _RaqmonDsSourcePayloadType_Type(Unsigned32):
    """Custom type raqmonDsSourcePayloadType based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_RaqmonDsSourcePayloadType_Type.__name__ = "Unsigned32"
_RaqmonDsSourcePayloadType_Object = MibTableColumn
raqmonDsSourcePayloadType = _RaqmonDsSourcePayloadType_Object(
    (1, 3, 6, 1, 2, 1, 16, 32, 1, 1, 1, 25),
    _RaqmonDsSourcePayloadType_Type()
)
raqmonDsSourcePayloadType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    raqmonDsSourcePayloadType.setStatus("current")


class _RaqmonDsReceiverPayloadType_Type(Unsigned32):
    """Custom type raqmonDsReceiverPayloadType based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_RaqmonDsReceiverPayloadType_Type.__name__ = "Unsigned32"
_RaqmonDsReceiverPayloadType_Object = MibTableColumn
raqmonDsReceiverPayloadType = _RaqmonDsReceiverPayloadType_Object(
    (1, 3, 6, 1, 2, 1, 16, 32, 1, 1, 1, 26),
    _RaqmonDsReceiverPayloadType_Type()
)
raqmonDsReceiverPayloadType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    raqmonDsReceiverPayloadType.setStatus("current")


class _RaqmonDsSourceLayer2Priority_Type(Unsigned32):
    """Custom type raqmonDsSourceLayer2Priority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RaqmonDsSourceLayer2Priority_Type.__name__ = "Unsigned32"
_RaqmonDsSourceLayer2Priority_Object = MibTableColumn
raqmonDsSourceLayer2Priority = _RaqmonDsSourceLayer2Priority_Object(
    (1, 3, 6, 1, 2, 1, 16, 32, 1, 1, 1, 27),
    _RaqmonDsSourceLayer2Priority_Type()
)
raqmonDsSourceLayer2Priority.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    raqmonDsSourceLayer2Priority.setStatus("current")
_RaqmonDsSourceDscp_Type = Dscp
_RaqmonDsSourceDscp_Object = MibTableColumn
raqmonDsSourceDscp = _RaqmonDsSourceDscp_Object(
    (1, 3, 6, 1, 2, 1, 16, 32, 1, 1, 1, 28),
    _RaqmonDsSourceDscp_Type()
)
raqmonDsSourceDscp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    raqmonDsSourceDscp.setStatus("current")


class _RaqmonDsDestinationLayer2Priority_Type(Unsigned32):
    """Custom type raqmonDsDestinationLayer2Priority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RaqmonDsDestinationLayer2Priority_Type.__name__ = "Unsigned32"
_RaqmonDsDestinationLayer2Priority_Object = MibTableColumn
raqmonDsDestinationLayer2Priority = _RaqmonDsDestinationLayer2Priority_Object(
    (1, 3, 6, 1, 2, 1, 16, 32, 1, 1, 1, 29),
    _RaqmonDsDestinationLayer2Priority_Type()
)
raqmonDsDestinationLayer2Priority.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    raqmonDsDestinationLayer2Priority.setStatus("current")
_RaqmonDsDestinationDscp_Type = Dscp
_RaqmonDsDestinationDscp_Object = MibTableColumn
raqmonDsDestinationDscp = _RaqmonDsDestinationDscp_Object(
    (1, 3, 6, 1, 2, 1, 16, 32, 1, 1, 1, 30),
    _RaqmonDsDestinationDscp_Type()
)
raqmonDsDestinationDscp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    raqmonDsDestinationDscp.setStatus("current")


class _RaqmonDsCpuUtilization_Type(Unsigned32):
    """Custom type raqmonDsCpuUtilization based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RaqmonDsCpuUtilization_Type.__name__ = "Unsigned32"
_RaqmonDsCpuUtilization_Object = MibTableColumn
raqmonDsCpuUtilization = _RaqmonDsCpuUtilization_Object(
    (1, 3, 6, 1, 2, 1, 16, 32, 1, 1, 1, 31),
    _RaqmonDsCpuUtilization_Type()
)
raqmonDsCpuUtilization.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    raqmonDsCpuUtilization.setStatus("current")
if mibBuilder.loadTexts:
    raqmonDsCpuUtilization.setUnits("percent")


class _RaqmonDsMemoryUtilization_Type(Unsigned32):
    """Custom type raqmonDsMemoryUtilization based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RaqmonDsMemoryUtilization_Type.__name__ = "Unsigned32"
_RaqmonDsMemoryUtilization_Object = MibTableColumn
raqmonDsMemoryUtilization = _RaqmonDsMemoryUtilization_Object(
    (1, 3, 6, 1, 2, 1, 16, 32, 1, 1, 1, 32),
    _RaqmonDsMemoryUtilization_Type()
)
raqmonDsMemoryUtilization.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    raqmonDsMemoryUtilization.setStatus("current")
if mibBuilder.loadTexts:
    raqmonDsMemoryUtilization.setUnits("percent")
_RaqmonDsConformance_ObjectIdentity = ObjectIdentity
raqmonDsConformance = _RaqmonDsConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 32, 2)
)
_RaqmonDsCompliance_ObjectIdentity = ObjectIdentity
raqmonDsCompliance = _RaqmonDsCompliance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 32, 2, 1)
)
_RaqmonDsGroups_ObjectIdentity = ObjectIdentity
raqmonDsGroups = _RaqmonDsGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 32, 2, 2)
)

# Managed Objects groups

raqmonDsPayloadGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 16, 32, 2, 2, 2)
)
raqmonDsPayloadGroup.setObjects(
      *(("RAQMON-RDS-MIB", "raqmonDsAppName"),
        ("RAQMON-RDS-MIB", "raqmonDsDataSourceDevicePort"),
        ("RAQMON-RDS-MIB", "raqmonDsReceiverDevicePort"),
        ("RAQMON-RDS-MIB", "raqmonDsSessionSetupDateTime"),
        ("RAQMON-RDS-MIB", "raqmonDsSessionSetupDelay"),
        ("RAQMON-RDS-MIB", "raqmonDsSessionDuration"),
        ("RAQMON-RDS-MIB", "raqmonDsSessionSetupStatus"),
        ("RAQMON-RDS-MIB", "raqmonDsRoundTripEndToEndNetDelay"),
        ("RAQMON-RDS-MIB", "raqmonDsOneWayEndToEndNetDelay"),
        ("RAQMON-RDS-MIB", "raqmonDsApplicationDelay"),
        ("RAQMON-RDS-MIB", "raqmonDsInterArrivalJitter"),
        ("RAQMON-RDS-MIB", "raqmonDsIPPacketDelayVariation"),
        ("RAQMON-RDS-MIB", "raqmonDsTotalPacketsReceived"),
        ("RAQMON-RDS-MIB", "raqmonDsTotalPacketsSent"),
        ("RAQMON-RDS-MIB", "raqmonDsTotalOctetsReceived"),
        ("RAQMON-RDS-MIB", "raqmonDsTotalOctetsSent"),
        ("RAQMON-RDS-MIB", "raqmonDsCumulativePacketLoss"),
        ("RAQMON-RDS-MIB", "raqmonDsPacketLossFraction"),
        ("RAQMON-RDS-MIB", "raqmonDsCumulativeDiscards"),
        ("RAQMON-RDS-MIB", "raqmonDsDiscardsFraction"),
        ("RAQMON-RDS-MIB", "raqmonDsSourcePayloadType"),
        ("RAQMON-RDS-MIB", "raqmonDsReceiverPayloadType"),
        ("RAQMON-RDS-MIB", "raqmonDsSourceLayer2Priority"),
        ("RAQMON-RDS-MIB", "raqmonDsSourceDscp"),
        ("RAQMON-RDS-MIB", "raqmonDsDestinationLayer2Priority"),
        ("RAQMON-RDS-MIB", "raqmonDsDestinationDscp"),
        ("RAQMON-RDS-MIB", "raqmonDsCpuUtilization"),
        ("RAQMON-RDS-MIB", "raqmonDsMemoryUtilization"))
)
if mibBuilder.loadTexts:
    raqmonDsPayloadGroup.setStatus("current")


# Notification objects

raqmonDsStaticNotification = NotificationType(
    (1, 3, 6, 1, 2, 1, 16, 32, 0, 1)
)
raqmonDsStaticNotification.setObjects(
    ("RAQMON-RDS-MIB", "raqmonDsAppName")
)
if mibBuilder.loadTexts:
    raqmonDsStaticNotification.setStatus(
        "current"
    )

raqmonDsDynamicNotification = NotificationType(
    (1, 3, 6, 1, 2, 1, 16, 32, 0, 2)
)
raqmonDsDynamicNotification.setObjects(
    ("RAQMON-RDS-MIB", "raqmonDsTotalPacketsReceived")
)
if mibBuilder.loadTexts:
    raqmonDsDynamicNotification.setStatus(
        "current"
    )

raqmonDsByeNotification = NotificationType(
    (1, 3, 6, 1, 2, 1, 16, 32, 0, 3)
)
raqmonDsByeNotification.setObjects(
    ("RAQMON-RDS-MIB", "raqmonDsAppName")
)
if mibBuilder.loadTexts:
    raqmonDsByeNotification.setStatus(
        "current"
    )


# Notifications groups

raqmonDsNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 16, 32, 2, 2, 1)
)
raqmonDsNotificationGroup.setObjects(
      *(("RAQMON-RDS-MIB", "raqmonDsStaticNotification"),
        ("RAQMON-RDS-MIB", "raqmonDsDynamicNotification"),
        ("RAQMON-RDS-MIB", "raqmonDsByeNotification"))
)
if mibBuilder.loadTexts:
    raqmonDsNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

raqmonDsBasicCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 16, 32, 2, 1, 1)
)
if mibBuilder.loadTexts:
    raqmonDsBasicCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RAQMON-RDS-MIB",
    **{"raqmonDsMIB": raqmonDsMIB,
       "raqmonDsNotifications": raqmonDsNotifications,
       "raqmonDsStaticNotification": raqmonDsStaticNotification,
       "raqmonDsDynamicNotification": raqmonDsDynamicNotification,
       "raqmonDsByeNotification": raqmonDsByeNotification,
       "raqmonDsMIBObjects": raqmonDsMIBObjects,
       "raqmonDsNotificationTable": raqmonDsNotificationTable,
       "raqmonDsNotificationEntry": raqmonDsNotificationEntry,
       "raqmonDsDSRC": raqmonDsDSRC,
       "raqmonDsRCN": raqmonDsRCN,
       "raqmonDsPeerAddrType": raqmonDsPeerAddrType,
       "raqmonDsPeerAddr": raqmonDsPeerAddr,
       "raqmonDsAppName": raqmonDsAppName,
       "raqmonDsDataSourceDevicePort": raqmonDsDataSourceDevicePort,
       "raqmonDsReceiverDevicePort": raqmonDsReceiverDevicePort,
       "raqmonDsSessionSetupDateTime": raqmonDsSessionSetupDateTime,
       "raqmonDsSessionSetupDelay": raqmonDsSessionSetupDelay,
       "raqmonDsSessionDuration": raqmonDsSessionDuration,
       "raqmonDsSessionSetupStatus": raqmonDsSessionSetupStatus,
       "raqmonDsRoundTripEndToEndNetDelay": raqmonDsRoundTripEndToEndNetDelay,
       "raqmonDsOneWayEndToEndNetDelay": raqmonDsOneWayEndToEndNetDelay,
       "raqmonDsApplicationDelay": raqmonDsApplicationDelay,
       "raqmonDsInterArrivalJitter": raqmonDsInterArrivalJitter,
       "raqmonDsIPPacketDelayVariation": raqmonDsIPPacketDelayVariation,
       "raqmonDsTotalPacketsReceived": raqmonDsTotalPacketsReceived,
       "raqmonDsTotalPacketsSent": raqmonDsTotalPacketsSent,
       "raqmonDsTotalOctetsReceived": raqmonDsTotalOctetsReceived,
       "raqmonDsTotalOctetsSent": raqmonDsTotalOctetsSent,
       "raqmonDsCumulativePacketLoss": raqmonDsCumulativePacketLoss,
       "raqmonDsPacketLossFraction": raqmonDsPacketLossFraction,
       "raqmonDsCumulativeDiscards": raqmonDsCumulativeDiscards,
       "raqmonDsDiscardsFraction": raqmonDsDiscardsFraction,
       "raqmonDsSourcePayloadType": raqmonDsSourcePayloadType,
       "raqmonDsReceiverPayloadType": raqmonDsReceiverPayloadType,
       "raqmonDsSourceLayer2Priority": raqmonDsSourceLayer2Priority,
       "raqmonDsSourceDscp": raqmonDsSourceDscp,
       "raqmonDsDestinationLayer2Priority": raqmonDsDestinationLayer2Priority,
       "raqmonDsDestinationDscp": raqmonDsDestinationDscp,
       "raqmonDsCpuUtilization": raqmonDsCpuUtilization,
       "raqmonDsMemoryUtilization": raqmonDsMemoryUtilization,
       "raqmonDsConformance": raqmonDsConformance,
       "raqmonDsCompliance": raqmonDsCompliance,
       "raqmonDsBasicCompliance": raqmonDsBasicCompliance,
       "raqmonDsGroups": raqmonDsGroups,
       "raqmonDsNotificationGroup": raqmonDsNotificationGroup,
       "raqmonDsPayloadGroup": raqmonDsPayloadGroup}
)
