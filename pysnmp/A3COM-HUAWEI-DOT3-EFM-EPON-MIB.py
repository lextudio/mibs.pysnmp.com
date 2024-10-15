# SNMP MIB module (A3COM-HUAWEI-DOT3-EFM-EPON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/A3COM-HUAWEI-DOT3-EFM-EPON-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:27:45 2024
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

(h3cEpon,) = mibBuilder.importSymbols(
    "A3COM-HUAWEI-OID-MIB",
    "h3cEpon")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 MacAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

h3cDot3EfmeponMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 2)
)
h3cDot3EfmeponMIB.setRevisions(
        ("2004-09-21 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cDot3MpcpMIB_ObjectIdentity = ObjectIdentity
h3cDot3MpcpMIB = _H3cDot3MpcpMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 2, 1)
)
_H3cDot3MpcpObjects_ObjectIdentity = ObjectIdentity
h3cDot3MpcpObjects = _H3cDot3MpcpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 2, 1, 1)
)
_H3cDot3MpcpTable_Object = MibTable
h3cDot3MpcpTable = _H3cDot3MpcpTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    h3cDot3MpcpTable.setStatus("current")
_H3cDot3MpcpEntry_Object = MibTableRow
h3cDot3MpcpEntry = _H3cDot3MpcpEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 2, 1, 1, 1, 1)
)
h3cDot3MpcpEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    h3cDot3MpcpEntry.setStatus("current")
_H3cDot3MpcpID_Type = Integer32
_H3cDot3MpcpID_Object = MibTableColumn
h3cDot3MpcpID = _H3cDot3MpcpID_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 2, 1, 1, 1, 1, 1),
    _H3cDot3MpcpID_Type()
)
h3cDot3MpcpID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot3MpcpID.setStatus("current")
_H3cDot3MpcpOperStatus_Type = TruthValue
_H3cDot3MpcpOperStatus_Object = MibTableColumn
h3cDot3MpcpOperStatus = _H3cDot3MpcpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 2, 1, 1, 1, 1, 2),
    _H3cDot3MpcpOperStatus_Type()
)
h3cDot3MpcpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot3MpcpOperStatus.setStatus("current")


class _H3cDot3MpcpMode_Type(Integer32):
    """Custom type h3cDot3MpcpMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("olt", 1),
          ("onu", 2))
    )


_H3cDot3MpcpMode_Type.__name__ = "Integer32"
_H3cDot3MpcpMode_Object = MibTableColumn
h3cDot3MpcpMode = _H3cDot3MpcpMode_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 2, 1, 1, 1, 1, 3),
    _H3cDot3MpcpMode_Type()
)
h3cDot3MpcpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot3MpcpMode.setStatus("current")
_H3cDot3MpcpLinkID_Type = Integer32
_H3cDot3MpcpLinkID_Object = MibTableColumn
h3cDot3MpcpLinkID = _H3cDot3MpcpLinkID_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 2, 1, 1, 1, 1, 4),
    _H3cDot3MpcpLinkID_Type()
)
h3cDot3MpcpLinkID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot3MpcpLinkID.setStatus("current")
_H3cDot3MpcpRemoteMACAddress_Type = MacAddress
_H3cDot3MpcpRemoteMACAddress_Object = MibTableColumn
h3cDot3MpcpRemoteMACAddress = _H3cDot3MpcpRemoteMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 2, 1, 1, 1, 1, 5),
    _H3cDot3MpcpRemoteMACAddress_Type()
)
h3cDot3MpcpRemoteMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot3MpcpRemoteMACAddress.setStatus("current")


class _H3cDot3MpcpRegistrationState_Type(Integer32):
    """Custom type h3cDot3MpcpRegistrationState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("registered", 3),
          ("registering", 2),
          ("unregistered", 1))
    )


_H3cDot3MpcpRegistrationState_Type.__name__ = "Integer32"
_H3cDot3MpcpRegistrationState_Object = MibTableColumn
h3cDot3MpcpRegistrationState = _H3cDot3MpcpRegistrationState_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 2, 1, 1, 1, 1, 6),
    _H3cDot3MpcpRegistrationState_Type()
)
h3cDot3MpcpRegistrationState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot3MpcpRegistrationState.setStatus("current")
_H3cDot3MpcpTransmitElapsed_Type = Integer32
_H3cDot3MpcpTransmitElapsed_Object = MibTableColumn
h3cDot3MpcpTransmitElapsed = _H3cDot3MpcpTransmitElapsed_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 2, 1, 1, 1, 1, 7),
    _H3cDot3MpcpTransmitElapsed_Type()
)
h3cDot3MpcpTransmitElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot3MpcpTransmitElapsed.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot3MpcpTransmitElapsed.setUnits("TQ (16nsec)")
_H3cDot3MpcpReceiveElapsed_Type = Integer32
_H3cDot3MpcpReceiveElapsed_Object = MibTableColumn
h3cDot3MpcpReceiveElapsed = _H3cDot3MpcpReceiveElapsed_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 2, 1, 1, 1, 1, 8),
    _H3cDot3MpcpReceiveElapsed_Type()
)
h3cDot3MpcpReceiveElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot3MpcpReceiveElapsed.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot3MpcpReceiveElapsed.setUnits("TQ (16nsec)")
_H3cDot3MpcpRoundTripTime_Type = Integer32
_H3cDot3MpcpRoundTripTime_Object = MibTableColumn
h3cDot3MpcpRoundTripTime = _H3cDot3MpcpRoundTripTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 2, 1, 1, 1, 1, 9),
    _H3cDot3MpcpRoundTripTime_Type()
)
h3cDot3MpcpRoundTripTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot3MpcpRoundTripTime.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot3MpcpRoundTripTime.setUnits("TQ (16nsec)")


class _H3cDot3MpcpMaximumPendingGrants_Type(Integer32):
    """Custom type h3cDot3MpcpMaximumPendingGrants based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_H3cDot3MpcpMaximumPendingGrants_Type.__name__ = "Integer32"
_H3cDot3MpcpMaximumPendingGrants_Object = MibTableColumn
h3cDot3MpcpMaximumPendingGrants = _H3cDot3MpcpMaximumPendingGrants_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 2, 1, 1, 1, 1, 10),
    _H3cDot3MpcpMaximumPendingGrants_Type()
)
h3cDot3MpcpMaximumPendingGrants.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot3MpcpMaximumPendingGrants.setStatus("current")


class _H3cDot3MpcpAdminState_Type(TruthValue):
    """Custom type h3cDot3MpcpAdminState based on TruthValue"""


_H3cDot3MpcpAdminState_Object = MibTableColumn
h3cDot3MpcpAdminState = _H3cDot3MpcpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 2, 1, 1, 1, 1, 11),
    _H3cDot3MpcpAdminState_Type()
)
h3cDot3MpcpAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot3MpcpAdminState.setStatus("current")
_H3cDot3MpcpOnTime_Type = Integer32
_H3cDot3MpcpOnTime_Object = MibTableColumn
h3cDot3MpcpOnTime = _H3cDot3MpcpOnTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 2, 1, 1, 1, 1, 12),
    _H3cDot3MpcpOnTime_Type()
)
h3cDot3MpcpOnTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot3MpcpOnTime.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot3MpcpOnTime.setUnits("TQ (16nsec)")
_H3cDot3MpcpOffTime_Type = Integer32
_H3cDot3MpcpOffTime_Object = MibTableColumn
h3cDot3MpcpOffTime = _H3cDot3MpcpOffTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 2, 1, 1, 1, 1, 13),
    _H3cDot3MpcpOffTime_Type()
)
h3cDot3MpcpOffTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot3MpcpOffTime.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot3MpcpOffTime.setUnits("TQ (16nsec)")
_H3cDot3MpcpSyncTime_Type = Integer32
_H3cDot3MpcpSyncTime_Object = MibTableColumn
h3cDot3MpcpSyncTime = _H3cDot3MpcpSyncTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 2, 1, 1, 1, 1, 14),
    _H3cDot3MpcpSyncTime_Type()
)
h3cDot3MpcpSyncTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot3MpcpSyncTime.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot3MpcpSyncTime.setUnits("TQ (16nsec)")
_H3cDot3MpcpStatTable_Object = MibTable
h3cDot3MpcpStatTable = _H3cDot3MpcpStatTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 2, 1, 1, 2)
)
if mibBuilder.loadTexts:
    h3cDot3MpcpStatTable.setStatus("current")
_H3cDot3MpcpStatEntry_Object = MibTableRow
h3cDot3MpcpStatEntry = _H3cDot3MpcpStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 2, 1, 1, 2, 1)
)
h3cDot3MpcpStatEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    h3cDot3MpcpStatEntry.setStatus("current")
_H3cDot3MpcpMACCtrlFramesTransmitted_Type = Counter32
_H3cDot3MpcpMACCtrlFramesTransmitted_Object = MibTableColumn
h3cDot3MpcpMACCtrlFramesTransmitted = _H3cDot3MpcpMACCtrlFramesTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 2, 1, 1, 2, 1, 1),
    _H3cDot3MpcpMACCtrlFramesTransmitted_Type()
)
h3cDot3MpcpMACCtrlFramesTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot3MpcpMACCtrlFramesTransmitted.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot3MpcpMACCtrlFramesTransmitted.setUnits("frames")
_H3cDot3MpcpMACCtrlFramesReceived_Type = Counter32
_H3cDot3MpcpMACCtrlFramesReceived_Object = MibTableColumn
h3cDot3MpcpMACCtrlFramesReceived = _H3cDot3MpcpMACCtrlFramesReceived_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 2, 1, 1, 2, 1, 2),
    _H3cDot3MpcpMACCtrlFramesReceived_Type()
)
h3cDot3MpcpMACCtrlFramesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot3MpcpMACCtrlFramesReceived.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot3MpcpMACCtrlFramesReceived.setUnits("frames")
_H3cDot3MpcpDiscoveryWindowsSent_Type = Counter32
_H3cDot3MpcpDiscoveryWindowsSent_Object = MibTableColumn
h3cDot3MpcpDiscoveryWindowsSent = _H3cDot3MpcpDiscoveryWindowsSent_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 2, 1, 1, 2, 1, 3),
    _H3cDot3MpcpDiscoveryWindowsSent_Type()
)
h3cDot3MpcpDiscoveryWindowsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot3MpcpDiscoveryWindowsSent.setStatus("current")
_H3cDot3MpcpDiscoveryTimeout_Type = Counter32
_H3cDot3MpcpDiscoveryTimeout_Object = MibTableColumn
h3cDot3MpcpDiscoveryTimeout = _H3cDot3MpcpDiscoveryTimeout_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 2, 1, 1, 2, 1, 4),
    _H3cDot3MpcpDiscoveryTimeout_Type()
)
h3cDot3MpcpDiscoveryTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot3MpcpDiscoveryTimeout.setStatus("current")
_H3cDot3MpcpTxRegRequest_Type = Counter32
_H3cDot3MpcpTxRegRequest_Object = MibTableColumn
h3cDot3MpcpTxRegRequest = _H3cDot3MpcpTxRegRequest_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 2, 1, 1, 2, 1, 5),
    _H3cDot3MpcpTxRegRequest_Type()
)
h3cDot3MpcpTxRegRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot3MpcpTxRegRequest.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot3MpcpTxRegRequest.setUnits("frames")
_H3cDot3MpcpRxRegRequest_Type = Counter32
_H3cDot3MpcpRxRegRequest_Object = MibTableColumn
h3cDot3MpcpRxRegRequest = _H3cDot3MpcpRxRegRequest_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 2, 1, 1, 2, 1, 6),
    _H3cDot3MpcpRxRegRequest_Type()
)
h3cDot3MpcpRxRegRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot3MpcpRxRegRequest.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot3MpcpRxRegRequest.setUnits("frames")
_H3cDot3MpcpTxRegAck_Type = Counter32
_H3cDot3MpcpTxRegAck_Object = MibTableColumn
h3cDot3MpcpTxRegAck = _H3cDot3MpcpTxRegAck_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 2, 1, 1, 2, 1, 7),
    _H3cDot3MpcpTxRegAck_Type()
)
h3cDot3MpcpTxRegAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot3MpcpTxRegAck.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot3MpcpTxRegAck.setUnits("frames")
_H3cDot3MpcpRxRegAck_Type = Counter32
_H3cDot3MpcpRxRegAck_Object = MibTableColumn
h3cDot3MpcpRxRegAck = _H3cDot3MpcpRxRegAck_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 2, 1, 1, 2, 1, 8),
    _H3cDot3MpcpRxRegAck_Type()
)
h3cDot3MpcpRxRegAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot3MpcpRxRegAck.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot3MpcpRxRegAck.setUnits("frames")
_H3cDot3MpcpTxReport_Type = Counter32
_H3cDot3MpcpTxReport_Object = MibTableColumn
h3cDot3MpcpTxReport = _H3cDot3MpcpTxReport_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 2, 1, 1, 2, 1, 9),
    _H3cDot3MpcpTxReport_Type()
)
h3cDot3MpcpTxReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot3MpcpTxReport.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot3MpcpTxReport.setUnits("frames")
_H3cDot3MpcpRxReport_Type = Counter32
_H3cDot3MpcpRxReport_Object = MibTableColumn
h3cDot3MpcpRxReport = _H3cDot3MpcpRxReport_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 2, 1, 1, 2, 1, 10),
    _H3cDot3MpcpRxReport_Type()
)
h3cDot3MpcpRxReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot3MpcpRxReport.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot3MpcpRxReport.setUnits("frames")
_H3cDot3MpcpTxGate_Type = Counter32
_H3cDot3MpcpTxGate_Object = MibTableColumn
h3cDot3MpcpTxGate = _H3cDot3MpcpTxGate_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 2, 1, 1, 2, 1, 11),
    _H3cDot3MpcpTxGate_Type()
)
h3cDot3MpcpTxGate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot3MpcpTxGate.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot3MpcpTxGate.setUnits("frames")
_H3cDot3MpcpRxGate_Type = Counter32
_H3cDot3MpcpRxGate_Object = MibTableColumn
h3cDot3MpcpRxGate = _H3cDot3MpcpRxGate_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 2, 1, 1, 2, 1, 12),
    _H3cDot3MpcpRxGate_Type()
)
h3cDot3MpcpRxGate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot3MpcpRxGate.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot3MpcpRxGate.setUnits("frames")
_H3cDot3MpcpTxRegister_Type = Counter32
_H3cDot3MpcpTxRegister_Object = MibTableColumn
h3cDot3MpcpTxRegister = _H3cDot3MpcpTxRegister_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 2, 1, 1, 2, 1, 13),
    _H3cDot3MpcpTxRegister_Type()
)
h3cDot3MpcpTxRegister.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot3MpcpTxRegister.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot3MpcpTxRegister.setUnits("frames")
_H3cDot3MpcpRxRegister_Type = Counter32
_H3cDot3MpcpRxRegister_Object = MibTableColumn
h3cDot3MpcpRxRegister = _H3cDot3MpcpRxRegister_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 2, 1, 1, 2, 1, 14),
    _H3cDot3MpcpRxRegister_Type()
)
h3cDot3MpcpRxRegister.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot3MpcpRxRegister.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot3MpcpRxRegister.setUnits("frames")
_H3cDot3MpcpRxNotSupportedMPCP_Type = Counter32
_H3cDot3MpcpRxNotSupportedMPCP_Object = MibTableColumn
h3cDot3MpcpRxNotSupportedMPCP = _H3cDot3MpcpRxNotSupportedMPCP_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 2, 1, 1, 2, 1, 15),
    _H3cDot3MpcpRxNotSupportedMPCP_Type()
)
h3cDot3MpcpRxNotSupportedMPCP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot3MpcpRxNotSupportedMPCP.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot3MpcpRxNotSupportedMPCP.setUnits("frames")
_H3cDot3MpcpConformance_ObjectIdentity = ObjectIdentity
h3cDot3MpcpConformance = _H3cDot3MpcpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 2, 1, 2)
)
_H3cDot3MpcpGroups_ObjectIdentity = ObjectIdentity
h3cDot3MpcpGroups = _H3cDot3MpcpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 2, 1, 2, 1)
)
_H3cDot3MpcpCompliances_ObjectIdentity = ObjectIdentity
h3cDot3MpcpCompliances = _H3cDot3MpcpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 2, 1, 2, 2)
)
_H3cDot3OmpEmulationMIB_ObjectIdentity = ObjectIdentity
h3cDot3OmpEmulationMIB = _H3cDot3OmpEmulationMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 2, 2)
)
_H3cDot3OmpEmulationObjects_ObjectIdentity = ObjectIdentity
h3cDot3OmpEmulationObjects = _H3cDot3OmpEmulationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 2, 2, 1)
)
_H3cDot3OmpEmulationTable_Object = MibTable
h3cDot3OmpEmulationTable = _H3cDot3OmpEmulationTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    h3cDot3OmpEmulationTable.setStatus("current")
_H3cDot3OmpEmulationEntry_Object = MibTableRow
h3cDot3OmpEmulationEntry = _H3cDot3OmpEmulationEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 2, 2, 1, 1, 1)
)
h3cDot3OmpEmulationEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    h3cDot3OmpEmulationEntry.setStatus("current")
_H3cDot3OmpEmulationID_Type = Integer32
_H3cDot3OmpEmulationID_Object = MibTableColumn
h3cDot3OmpEmulationID = _H3cDot3OmpEmulationID_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 2, 2, 1, 1, 1, 1),
    _H3cDot3OmpEmulationID_Type()
)
h3cDot3OmpEmulationID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot3OmpEmulationID.setStatus("current")


class _H3cDot3OmpEmulationType_Type(Integer32):
    """Custom type h3cDot3OmpEmulationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("olt", 2),
          ("onu", 3),
          ("unknown", 1))
    )


_H3cDot3OmpEmulationType_Type.__name__ = "Integer32"
_H3cDot3OmpEmulationType_Object = MibTableColumn
h3cDot3OmpEmulationType = _H3cDot3OmpEmulationType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 2, 2, 1, 1, 1, 2),
    _H3cDot3OmpEmulationType_Type()
)
h3cDot3OmpEmulationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot3OmpEmulationType.setStatus("current")
_H3cDot3OmpEmulationStatTable_Object = MibTable
h3cDot3OmpEmulationStatTable = _H3cDot3OmpEmulationStatTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 2, 2, 1, 2)
)
if mibBuilder.loadTexts:
    h3cDot3OmpEmulationStatTable.setStatus("current")
_H3cDot3OmpEmulationStatEntry_Object = MibTableRow
h3cDot3OmpEmulationStatEntry = _H3cDot3OmpEmulationStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 2, 2, 1, 2, 1)
)
h3cDot3OmpEmulationStatEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    h3cDot3OmpEmulationStatEntry.setStatus("current")
_H3cDot3OmpEmulationSLDErrors_Type = Counter32
_H3cDot3OmpEmulationSLDErrors_Object = MibTableColumn
h3cDot3OmpEmulationSLDErrors = _H3cDot3OmpEmulationSLDErrors_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 2, 2, 1, 2, 1, 1),
    _H3cDot3OmpEmulationSLDErrors_Type()
)
h3cDot3OmpEmulationSLDErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot3OmpEmulationSLDErrors.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot3OmpEmulationSLDErrors.setUnits("frames")
_H3cDot3OmpEmulationCRC8Errors_Type = Counter32
_H3cDot3OmpEmulationCRC8Errors_Object = MibTableColumn
h3cDot3OmpEmulationCRC8Errors = _H3cDot3OmpEmulationCRC8Errors_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 2, 2, 1, 2, 1, 2),
    _H3cDot3OmpEmulationCRC8Errors_Type()
)
h3cDot3OmpEmulationCRC8Errors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot3OmpEmulationCRC8Errors.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot3OmpEmulationCRC8Errors.setUnits("frames")
_H3cDot3OmpEmulationBadLLID_Type = Counter32
_H3cDot3OmpEmulationBadLLID_Object = MibTableColumn
h3cDot3OmpEmulationBadLLID = _H3cDot3OmpEmulationBadLLID_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 2, 2, 1, 2, 1, 3),
    _H3cDot3OmpEmulationBadLLID_Type()
)
h3cDot3OmpEmulationBadLLID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot3OmpEmulationBadLLID.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot3OmpEmulationBadLLID.setUnits("frames")
_H3cDot3OmpEmulationGoodLLID_Type = Counter32
_H3cDot3OmpEmulationGoodLLID_Object = MibTableColumn
h3cDot3OmpEmulationGoodLLID = _H3cDot3OmpEmulationGoodLLID_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 2, 2, 1, 2, 1, 4),
    _H3cDot3OmpEmulationGoodLLID_Type()
)
h3cDot3OmpEmulationGoodLLID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot3OmpEmulationGoodLLID.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot3OmpEmulationGoodLLID.setUnits("frames")
_H3cDot3OmpEmulationOnuPonCastLLID_Type = Counter32
_H3cDot3OmpEmulationOnuPonCastLLID_Object = MibTableColumn
h3cDot3OmpEmulationOnuPonCastLLID = _H3cDot3OmpEmulationOnuPonCastLLID_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 2, 2, 1, 2, 1, 5),
    _H3cDot3OmpEmulationOnuPonCastLLID_Type()
)
h3cDot3OmpEmulationOnuPonCastLLID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot3OmpEmulationOnuPonCastLLID.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot3OmpEmulationOnuPonCastLLID.setUnits("frames")
_H3cDot3OmpEmulationOltPonCastLLID_Type = Counter32
_H3cDot3OmpEmulationOltPonCastLLID_Object = MibTableColumn
h3cDot3OmpEmulationOltPonCastLLID = _H3cDot3OmpEmulationOltPonCastLLID_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 2, 2, 1, 2, 1, 6),
    _H3cDot3OmpEmulationOltPonCastLLID_Type()
)
h3cDot3OmpEmulationOltPonCastLLID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot3OmpEmulationOltPonCastLLID.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot3OmpEmulationOltPonCastLLID.setUnits("frames")
_H3cDot3OmpEmulationBroadcastLLIDNotOnuID_Type = Counter32
_H3cDot3OmpEmulationBroadcastLLIDNotOnuID_Object = MibTableColumn
h3cDot3OmpEmulationBroadcastLLIDNotOnuID = _H3cDot3OmpEmulationBroadcastLLIDNotOnuID_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 2, 2, 1, 2, 1, 7),
    _H3cDot3OmpEmulationBroadcastLLIDNotOnuID_Type()
)
h3cDot3OmpEmulationBroadcastLLIDNotOnuID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot3OmpEmulationBroadcastLLIDNotOnuID.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot3OmpEmulationBroadcastLLIDNotOnuID.setUnits("frames")
_H3cDot3OmpEmulationOnuLLIDNotBroadcast_Type = Counter32
_H3cDot3OmpEmulationOnuLLIDNotBroadcast_Object = MibTableColumn
h3cDot3OmpEmulationOnuLLIDNotBroadcast = _H3cDot3OmpEmulationOnuLLIDNotBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 2, 2, 1, 2, 1, 8),
    _H3cDot3OmpEmulationOnuLLIDNotBroadcast_Type()
)
h3cDot3OmpEmulationOnuLLIDNotBroadcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot3OmpEmulationOnuLLIDNotBroadcast.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot3OmpEmulationOnuLLIDNotBroadcast.setUnits("frames")
_H3cDot3OmpEmulationBroadcastLLIDPlusOnuId_Type = Counter32
_H3cDot3OmpEmulationBroadcastLLIDPlusOnuId_Object = MibTableColumn
h3cDot3OmpEmulationBroadcastLLIDPlusOnuId = _H3cDot3OmpEmulationBroadcastLLIDPlusOnuId_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 2, 2, 1, 2, 1, 9),
    _H3cDot3OmpEmulationBroadcastLLIDPlusOnuId_Type()
)
h3cDot3OmpEmulationBroadcastLLIDPlusOnuId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot3OmpEmulationBroadcastLLIDPlusOnuId.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot3OmpEmulationBroadcastLLIDPlusOnuId.setUnits("frames")
_H3cDot3OmpEmulationNotBroadcastLLIDNotOnuId_Type = Counter32
_H3cDot3OmpEmulationNotBroadcastLLIDNotOnuId_Object = MibTableColumn
h3cDot3OmpEmulationNotBroadcastLLIDNotOnuId = _H3cDot3OmpEmulationNotBroadcastLLIDNotOnuId_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 2, 2, 1, 2, 1, 10),
    _H3cDot3OmpEmulationNotBroadcastLLIDNotOnuId_Type()
)
h3cDot3OmpEmulationNotBroadcastLLIDNotOnuId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot3OmpEmulationNotBroadcastLLIDNotOnuId.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot3OmpEmulationNotBroadcastLLIDNotOnuId.setUnits("frames")
_H3cDot3OmpeConformance_ObjectIdentity = ObjectIdentity
h3cDot3OmpeConformance = _H3cDot3OmpeConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 2, 2, 2)
)
_H3cDot3OmpeGroups_ObjectIdentity = ObjectIdentity
h3cDot3OmpeGroups = _H3cDot3OmpeGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 2, 2, 2, 1)
)
_H3cDot3OmpeCompliances_ObjectIdentity = ObjectIdentity
h3cDot3OmpeCompliances = _H3cDot3OmpeCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 2, 2, 2, 2)
)
_H3cDot3EponMauMIB_ObjectIdentity = ObjectIdentity
h3cDot3EponMauMIB = _H3cDot3EponMauMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 2, 3)
)
_H3cDot3EponMauObjects_ObjectIdentity = ObjectIdentity
h3cDot3EponMauObjects = _H3cDot3EponMauObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 2, 3, 1)
)
_H3cDot3EponMauTable_Object = MibTable
h3cDot3EponMauTable = _H3cDot3EponMauTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 2, 3, 1, 1)
)
if mibBuilder.loadTexts:
    h3cDot3EponMauTable.setStatus("current")
_H3cDot3EponMauEntry_Object = MibTableRow
h3cDot3EponMauEntry = _H3cDot3EponMauEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 2, 3, 1, 1, 1)
)
h3cDot3EponMauEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    h3cDot3EponMauEntry.setStatus("current")
_H3cDot3EponMauPCSCodingViolation_Type = Counter32
_H3cDot3EponMauPCSCodingViolation_Object = MibTableColumn
h3cDot3EponMauPCSCodingViolation = _H3cDot3EponMauPCSCodingViolation_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 2, 3, 1, 1, 1, 1),
    _H3cDot3EponMauPCSCodingViolation_Type()
)
h3cDot3EponMauPCSCodingViolation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot3EponMauPCSCodingViolation.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot3EponMauPCSCodingViolation.setUnits("octets")


class _H3cDot3EponMauFecAbility_Type(Integer32):
    """Custom type h3cDot3EponMauFecAbility based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nonsupported", 2),
          ("supported", 3),
          ("unknown", 1))
    )


_H3cDot3EponMauFecAbility_Type.__name__ = "Integer32"
_H3cDot3EponMauFecAbility_Object = MibTableColumn
h3cDot3EponMauFecAbility = _H3cDot3EponMauFecAbility_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 2, 3, 1, 1, 1, 2),
    _H3cDot3EponMauFecAbility_Type()
)
h3cDot3EponMauFecAbility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot3EponMauFecAbility.setStatus("current")


class _H3cDot3EponMauFecMode_Type(Integer32):
    """Custom type h3cDot3EponMauFecMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("unknown", 1))
    )


_H3cDot3EponMauFecMode_Type.__name__ = "Integer32"
_H3cDot3EponMauFecMode_Object = MibTableColumn
h3cDot3EponMauFecMode = _H3cDot3EponMauFecMode_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 2, 3, 1, 1, 1, 3),
    _H3cDot3EponMauFecMode_Type()
)
h3cDot3EponMauFecMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot3EponMauFecMode.setStatus("current")
_H3cDot3EponMauFECCorrectedBlocks_Type = Counter32
_H3cDot3EponMauFECCorrectedBlocks_Object = MibTableColumn
h3cDot3EponMauFECCorrectedBlocks = _H3cDot3EponMauFECCorrectedBlocks_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 2, 3, 1, 1, 1, 4),
    _H3cDot3EponMauFECCorrectedBlocks_Type()
)
h3cDot3EponMauFECCorrectedBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot3EponMauFECCorrectedBlocks.setStatus("current")
_H3cDot3EponMauFECUncorrectableBlocks_Type = Counter32
_H3cDot3EponMauFECUncorrectableBlocks_Object = MibTableColumn
h3cDot3EponMauFECUncorrectableBlocks = _H3cDot3EponMauFECUncorrectableBlocks_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 2, 3, 1, 1, 1, 5),
    _H3cDot3EponMauFECUncorrectableBlocks_Type()
)
h3cDot3EponMauFECUncorrectableBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot3EponMauFECUncorrectableBlocks.setStatus("current")
_H3cDot3EponMauBufferHeadCodingViolation_Type = Counter32
_H3cDot3EponMauBufferHeadCodingViolation_Object = MibTableColumn
h3cDot3EponMauBufferHeadCodingViolation = _H3cDot3EponMauBufferHeadCodingViolation_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 2, 3, 1, 1, 1, 6),
    _H3cDot3EponMauBufferHeadCodingViolation_Type()
)
h3cDot3EponMauBufferHeadCodingViolation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot3EponMauBufferHeadCodingViolation.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot3EponMauBufferHeadCodingViolation.setUnits("octets")
_H3cDot3EponMauConformance_ObjectIdentity = ObjectIdentity
h3cDot3EponMauConformance = _H3cDot3EponMauConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 2, 3, 2)
)
_H3cDot3EponMauGroups_ObjectIdentity = ObjectIdentity
h3cDot3EponMauGroups = _H3cDot3EponMauGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 2, 3, 2, 1)
)
_H3cDot3EponMauCompliances_ObjectIdentity = ObjectIdentity
h3cDot3EponMauCompliances = _H3cDot3EponMauCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 2, 3, 2, 2)
)
_H3cDot3EponMauType_ObjectIdentity = ObjectIdentity
h3cDot3EponMauType = _H3cDot3EponMauType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 2, 3, 3)
)
_H3cEponMauType1000BasePXOLT_ObjectIdentity = ObjectIdentity
h3cEponMauType1000BasePXOLT = _H3cEponMauType1000BasePXOLT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 2, 3, 3, 1)
)
if mibBuilder.loadTexts:
    h3cEponMauType1000BasePXOLT.setStatus("current")
_H3cEponMauType1000BasePXONU_ObjectIdentity = ObjectIdentity
h3cEponMauType1000BasePXONU = _H3cEponMauType1000BasePXONU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 2, 3, 3, 2)
)
if mibBuilder.loadTexts:
    h3cEponMauType1000BasePXONU.setStatus("current")
_H3cEponMauType1000BasePX10DOLT_ObjectIdentity = ObjectIdentity
h3cEponMauType1000BasePX10DOLT = _H3cEponMauType1000BasePX10DOLT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 2, 3, 3, 3)
)
if mibBuilder.loadTexts:
    h3cEponMauType1000BasePX10DOLT.setStatus("current")
_H3cEponMauType1000BasePX10DONU_ObjectIdentity = ObjectIdentity
h3cEponMauType1000BasePX10DONU = _H3cEponMauType1000BasePX10DONU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 2, 3, 3, 4)
)
if mibBuilder.loadTexts:
    h3cEponMauType1000BasePX10DONU.setStatus("current")
_H3cEponMauType1000BasePX10UOLT_ObjectIdentity = ObjectIdentity
h3cEponMauType1000BasePX10UOLT = _H3cEponMauType1000BasePX10UOLT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 2, 3, 3, 5)
)
if mibBuilder.loadTexts:
    h3cEponMauType1000BasePX10UOLT.setStatus("current")
_H3cEponMauType1000BasePX10UONU_ObjectIdentity = ObjectIdentity
h3cEponMauType1000BasePX10UONU = _H3cEponMauType1000BasePX10UONU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 2, 3, 3, 6)
)
if mibBuilder.loadTexts:
    h3cEponMauType1000BasePX10UONU.setStatus("current")
_H3cEponMauType1000BasePX20DOLT_ObjectIdentity = ObjectIdentity
h3cEponMauType1000BasePX20DOLT = _H3cEponMauType1000BasePX20DOLT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 2, 3, 3, 7)
)
if mibBuilder.loadTexts:
    h3cEponMauType1000BasePX20DOLT.setStatus("current")
_H3cEponMauType1000BasePX20DONU_ObjectIdentity = ObjectIdentity
h3cEponMauType1000BasePX20DONU = _H3cEponMauType1000BasePX20DONU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 2, 3, 3, 8)
)
if mibBuilder.loadTexts:
    h3cEponMauType1000BasePX20DONU.setStatus("current")
_H3cEponMauType1000BasePX20UOLT_ObjectIdentity = ObjectIdentity
h3cEponMauType1000BasePX20UOLT = _H3cEponMauType1000BasePX20UOLT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 2, 3, 3, 9)
)
if mibBuilder.loadTexts:
    h3cEponMauType1000BasePX20UOLT.setStatus("current")
_H3cEponMauType1000BasePX20UONU_ObjectIdentity = ObjectIdentity
h3cEponMauType1000BasePX20UONU = _H3cEponMauType1000BasePX20UONU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 2, 3, 3, 10)
)
if mibBuilder.loadTexts:
    h3cEponMauType1000BasePX20UONU.setStatus("current")

# Managed Objects groups

h3cDot3MpcpGroupBase = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 2, 1, 2, 1, 1)
)
h3cDot3MpcpGroupBase.setObjects(
      *(("A3COM-HUAWEI-DOT3-EFM-EPON-MIB", "h3cDot3MpcpID"),
        ("A3COM-HUAWEI-DOT3-EFM-EPON-MIB", "h3cDot3MpcpOperStatus"),
        ("A3COM-HUAWEI-DOT3-EFM-EPON-MIB", "h3cDot3MpcpMode"),
        ("A3COM-HUAWEI-DOT3-EFM-EPON-MIB", "h3cDot3MpcpLinkID"),
        ("A3COM-HUAWEI-DOT3-EFM-EPON-MIB", "h3cDot3MpcpRemoteMACAddress"),
        ("A3COM-HUAWEI-DOT3-EFM-EPON-MIB", "h3cDot3MpcpRegistrationState"),
        ("A3COM-HUAWEI-DOT3-EFM-EPON-MIB", "h3cDot3MpcpMaximumPendingGrants"),
        ("A3COM-HUAWEI-DOT3-EFM-EPON-MIB", "h3cDot3MpcpAdminState"))
)
if mibBuilder.loadTexts:
    h3cDot3MpcpGroupBase.setStatus("current")

h3cDot3MpcpGroupParam = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 2, 1, 2, 1, 2)
)
h3cDot3MpcpGroupParam.setObjects(
      *(("A3COM-HUAWEI-DOT3-EFM-EPON-MIB", "h3cDot3MpcpTransmitElapsed"),
        ("A3COM-HUAWEI-DOT3-EFM-EPON-MIB", "h3cDot3MpcpReceiveElapsed"),
        ("A3COM-HUAWEI-DOT3-EFM-EPON-MIB", "h3cDot3MpcpRoundTripTime"),
        ("A3COM-HUAWEI-DOT3-EFM-EPON-MIB", "h3cDot3MpcpOnTime"),
        ("A3COM-HUAWEI-DOT3-EFM-EPON-MIB", "h3cDot3MpcpOffTime"),
        ("A3COM-HUAWEI-DOT3-EFM-EPON-MIB", "h3cDot3MpcpSyncTime"))
)
if mibBuilder.loadTexts:
    h3cDot3MpcpGroupParam.setStatus("current")

h3cDot3MpcpGroupStat = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 2, 1, 2, 1, 3)
)
h3cDot3MpcpGroupStat.setObjects(
      *(("A3COM-HUAWEI-DOT3-EFM-EPON-MIB", "h3cDot3MpcpMACCtrlFramesTransmitted"),
        ("A3COM-HUAWEI-DOT3-EFM-EPON-MIB", "h3cDot3MpcpMACCtrlFramesReceived"),
        ("A3COM-HUAWEI-DOT3-EFM-EPON-MIB", "h3cDot3MpcpDiscoveryWindowsSent"),
        ("A3COM-HUAWEI-DOT3-EFM-EPON-MIB", "h3cDot3MpcpDiscoveryTimeout"),
        ("A3COM-HUAWEI-DOT3-EFM-EPON-MIB", "h3cDot3MpcpTxRegRequest"),
        ("A3COM-HUAWEI-DOT3-EFM-EPON-MIB", "h3cDot3MpcpRxRegRequest"),
        ("A3COM-HUAWEI-DOT3-EFM-EPON-MIB", "h3cDot3MpcpTxRegAck"),
        ("A3COM-HUAWEI-DOT3-EFM-EPON-MIB", "h3cDot3MpcpRxRegAck"),
        ("A3COM-HUAWEI-DOT3-EFM-EPON-MIB", "h3cDot3MpcpTxReport"),
        ("A3COM-HUAWEI-DOT3-EFM-EPON-MIB", "h3cDot3MpcpRxReport"),
        ("A3COM-HUAWEI-DOT3-EFM-EPON-MIB", "h3cDot3MpcpTxGate"),
        ("A3COM-HUAWEI-DOT3-EFM-EPON-MIB", "h3cDot3MpcpRxGate"),
        ("A3COM-HUAWEI-DOT3-EFM-EPON-MIB", "h3cDot3MpcpTxRegister"),
        ("A3COM-HUAWEI-DOT3-EFM-EPON-MIB", "h3cDot3MpcpRxRegister"),
        ("A3COM-HUAWEI-DOT3-EFM-EPON-MIB", "h3cDot3MpcpRxNotSupportedMPCP"))
)
if mibBuilder.loadTexts:
    h3cDot3MpcpGroupStat.setStatus("current")

h3cDot3OmpeGroupID = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 2, 2, 2, 1, 1)
)
h3cDot3OmpeGroupID.setObjects(
      *(("A3COM-HUAWEI-DOT3-EFM-EPON-MIB", "h3cDot3OmpEmulationID"),
        ("A3COM-HUAWEI-DOT3-EFM-EPON-MIB", "h3cDot3OmpEmulationType"))
)
if mibBuilder.loadTexts:
    h3cDot3OmpeGroupID.setStatus("current")

h3cDot3OmpeGroupStat = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 2, 2, 2, 1, 2)
)
h3cDot3OmpeGroupStat.setObjects(
      *(("A3COM-HUAWEI-DOT3-EFM-EPON-MIB", "h3cDot3OmpEmulationSLDErrors"),
        ("A3COM-HUAWEI-DOT3-EFM-EPON-MIB", "h3cDot3OmpEmulationCRC8Errors"),
        ("A3COM-HUAWEI-DOT3-EFM-EPON-MIB", "h3cDot3OmpEmulationBadLLID"),
        ("A3COM-HUAWEI-DOT3-EFM-EPON-MIB", "h3cDot3OmpEmulationGoodLLID"),
        ("A3COM-HUAWEI-DOT3-EFM-EPON-MIB", "h3cDot3OmpEmulationOnuPonCastLLID"),
        ("A3COM-HUAWEI-DOT3-EFM-EPON-MIB", "h3cDot3OmpEmulationOltPonCastLLID"),
        ("A3COM-HUAWEI-DOT3-EFM-EPON-MIB", "h3cDot3OmpEmulationBroadcastLLIDNotOnuID"),
        ("A3COM-HUAWEI-DOT3-EFM-EPON-MIB", "h3cDot3OmpEmulationOnuLLIDNotBroadcast"),
        ("A3COM-HUAWEI-DOT3-EFM-EPON-MIB", "h3cDot3OmpEmulationBroadcastLLIDPlusOnuId"),
        ("A3COM-HUAWEI-DOT3-EFM-EPON-MIB", "h3cDot3OmpEmulationNotBroadcastLLIDNotOnuId"))
)
if mibBuilder.loadTexts:
    h3cDot3OmpeGroupStat.setStatus("current")

h3cDot3EponMauGroupAll = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 2, 3, 2, 1, 1)
)
h3cDot3EponMauGroupAll.setObjects(
    ("A3COM-HUAWEI-DOT3-EFM-EPON-MIB", "h3cDot3EponMauPCSCodingViolation")
)
if mibBuilder.loadTexts:
    h3cDot3EponMauGroupAll.setStatus("current")

h3cDot3EponMauGroupFEC = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 2, 3, 2, 1, 2)
)
h3cDot3EponMauGroupFEC.setObjects(
      *(("A3COM-HUAWEI-DOT3-EFM-EPON-MIB", "h3cDot3EponMauFecAbility"),
        ("A3COM-HUAWEI-DOT3-EFM-EPON-MIB", "h3cDot3EponMauFecMode"),
        ("A3COM-HUAWEI-DOT3-EFM-EPON-MIB", "h3cDot3EponMauFECCorrectedBlocks"),
        ("A3COM-HUAWEI-DOT3-EFM-EPON-MIB", "h3cDot3EponMauFECUncorrectableBlocks"),
        ("A3COM-HUAWEI-DOT3-EFM-EPON-MIB", "h3cDot3EponMauBufferHeadCodingViolation"))
)
if mibBuilder.loadTexts:
    h3cDot3EponMauGroupFEC.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

h3cDot3MpcpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 2, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    h3cDot3MpcpCompliance.setStatus(
        "current"
    )

h3cDot3OmpeCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 2, 2, 2, 2, 1)
)
if mibBuilder.loadTexts:
    h3cDot3OmpeCompliance.setStatus(
        "current"
    )

h3cDot3EponMauCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 2, 3, 2, 2, 1)
)
if mibBuilder.loadTexts:
    h3cDot3EponMauCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM-HUAWEI-DOT3-EFM-EPON-MIB",
    **{"h3cDot3EfmeponMIB": h3cDot3EfmeponMIB,
       "h3cDot3MpcpMIB": h3cDot3MpcpMIB,
       "h3cDot3MpcpObjects": h3cDot3MpcpObjects,
       "h3cDot3MpcpTable": h3cDot3MpcpTable,
       "h3cDot3MpcpEntry": h3cDot3MpcpEntry,
       "h3cDot3MpcpID": h3cDot3MpcpID,
       "h3cDot3MpcpOperStatus": h3cDot3MpcpOperStatus,
       "h3cDot3MpcpMode": h3cDot3MpcpMode,
       "h3cDot3MpcpLinkID": h3cDot3MpcpLinkID,
       "h3cDot3MpcpRemoteMACAddress": h3cDot3MpcpRemoteMACAddress,
       "h3cDot3MpcpRegistrationState": h3cDot3MpcpRegistrationState,
       "h3cDot3MpcpTransmitElapsed": h3cDot3MpcpTransmitElapsed,
       "h3cDot3MpcpReceiveElapsed": h3cDot3MpcpReceiveElapsed,
       "h3cDot3MpcpRoundTripTime": h3cDot3MpcpRoundTripTime,
       "h3cDot3MpcpMaximumPendingGrants": h3cDot3MpcpMaximumPendingGrants,
       "h3cDot3MpcpAdminState": h3cDot3MpcpAdminState,
       "h3cDot3MpcpOnTime": h3cDot3MpcpOnTime,
       "h3cDot3MpcpOffTime": h3cDot3MpcpOffTime,
       "h3cDot3MpcpSyncTime": h3cDot3MpcpSyncTime,
       "h3cDot3MpcpStatTable": h3cDot3MpcpStatTable,
       "h3cDot3MpcpStatEntry": h3cDot3MpcpStatEntry,
       "h3cDot3MpcpMACCtrlFramesTransmitted": h3cDot3MpcpMACCtrlFramesTransmitted,
       "h3cDot3MpcpMACCtrlFramesReceived": h3cDot3MpcpMACCtrlFramesReceived,
       "h3cDot3MpcpDiscoveryWindowsSent": h3cDot3MpcpDiscoveryWindowsSent,
       "h3cDot3MpcpDiscoveryTimeout": h3cDot3MpcpDiscoveryTimeout,
       "h3cDot3MpcpTxRegRequest": h3cDot3MpcpTxRegRequest,
       "h3cDot3MpcpRxRegRequest": h3cDot3MpcpRxRegRequest,
       "h3cDot3MpcpTxRegAck": h3cDot3MpcpTxRegAck,
       "h3cDot3MpcpRxRegAck": h3cDot3MpcpRxRegAck,
       "h3cDot3MpcpTxReport": h3cDot3MpcpTxReport,
       "h3cDot3MpcpRxReport": h3cDot3MpcpRxReport,
       "h3cDot3MpcpTxGate": h3cDot3MpcpTxGate,
       "h3cDot3MpcpRxGate": h3cDot3MpcpRxGate,
       "h3cDot3MpcpTxRegister": h3cDot3MpcpTxRegister,
       "h3cDot3MpcpRxRegister": h3cDot3MpcpRxRegister,
       "h3cDot3MpcpRxNotSupportedMPCP": h3cDot3MpcpRxNotSupportedMPCP,
       "h3cDot3MpcpConformance": h3cDot3MpcpConformance,
       "h3cDot3MpcpGroups": h3cDot3MpcpGroups,
       "h3cDot3MpcpGroupBase": h3cDot3MpcpGroupBase,
       "h3cDot3MpcpGroupParam": h3cDot3MpcpGroupParam,
       "h3cDot3MpcpGroupStat": h3cDot3MpcpGroupStat,
       "h3cDot3MpcpCompliances": h3cDot3MpcpCompliances,
       "h3cDot3MpcpCompliance": h3cDot3MpcpCompliance,
       "h3cDot3OmpEmulationMIB": h3cDot3OmpEmulationMIB,
       "h3cDot3OmpEmulationObjects": h3cDot3OmpEmulationObjects,
       "h3cDot3OmpEmulationTable": h3cDot3OmpEmulationTable,
       "h3cDot3OmpEmulationEntry": h3cDot3OmpEmulationEntry,
       "h3cDot3OmpEmulationID": h3cDot3OmpEmulationID,
       "h3cDot3OmpEmulationType": h3cDot3OmpEmulationType,
       "h3cDot3OmpEmulationStatTable": h3cDot3OmpEmulationStatTable,
       "h3cDot3OmpEmulationStatEntry": h3cDot3OmpEmulationStatEntry,
       "h3cDot3OmpEmulationSLDErrors": h3cDot3OmpEmulationSLDErrors,
       "h3cDot3OmpEmulationCRC8Errors": h3cDot3OmpEmulationCRC8Errors,
       "h3cDot3OmpEmulationBadLLID": h3cDot3OmpEmulationBadLLID,
       "h3cDot3OmpEmulationGoodLLID": h3cDot3OmpEmulationGoodLLID,
       "h3cDot3OmpEmulationOnuPonCastLLID": h3cDot3OmpEmulationOnuPonCastLLID,
       "h3cDot3OmpEmulationOltPonCastLLID": h3cDot3OmpEmulationOltPonCastLLID,
       "h3cDot3OmpEmulationBroadcastLLIDNotOnuID": h3cDot3OmpEmulationBroadcastLLIDNotOnuID,
       "h3cDot3OmpEmulationOnuLLIDNotBroadcast": h3cDot3OmpEmulationOnuLLIDNotBroadcast,
       "h3cDot3OmpEmulationBroadcastLLIDPlusOnuId": h3cDot3OmpEmulationBroadcastLLIDPlusOnuId,
       "h3cDot3OmpEmulationNotBroadcastLLIDNotOnuId": h3cDot3OmpEmulationNotBroadcastLLIDNotOnuId,
       "h3cDot3OmpeConformance": h3cDot3OmpeConformance,
       "h3cDot3OmpeGroups": h3cDot3OmpeGroups,
       "h3cDot3OmpeGroupID": h3cDot3OmpeGroupID,
       "h3cDot3OmpeGroupStat": h3cDot3OmpeGroupStat,
       "h3cDot3OmpeCompliances": h3cDot3OmpeCompliances,
       "h3cDot3OmpeCompliance": h3cDot3OmpeCompliance,
       "h3cDot3EponMauMIB": h3cDot3EponMauMIB,
       "h3cDot3EponMauObjects": h3cDot3EponMauObjects,
       "h3cDot3EponMauTable": h3cDot3EponMauTable,
       "h3cDot3EponMauEntry": h3cDot3EponMauEntry,
       "h3cDot3EponMauPCSCodingViolation": h3cDot3EponMauPCSCodingViolation,
       "h3cDot3EponMauFecAbility": h3cDot3EponMauFecAbility,
       "h3cDot3EponMauFecMode": h3cDot3EponMauFecMode,
       "h3cDot3EponMauFECCorrectedBlocks": h3cDot3EponMauFECCorrectedBlocks,
       "h3cDot3EponMauFECUncorrectableBlocks": h3cDot3EponMauFECUncorrectableBlocks,
       "h3cDot3EponMauBufferHeadCodingViolation": h3cDot3EponMauBufferHeadCodingViolation,
       "h3cDot3EponMauConformance": h3cDot3EponMauConformance,
       "h3cDot3EponMauGroups": h3cDot3EponMauGroups,
       "h3cDot3EponMauGroupAll": h3cDot3EponMauGroupAll,
       "h3cDot3EponMauGroupFEC": h3cDot3EponMauGroupFEC,
       "h3cDot3EponMauCompliances": h3cDot3EponMauCompliances,
       "h3cDot3EponMauCompliance": h3cDot3EponMauCompliance,
       "h3cDot3EponMauType": h3cDot3EponMauType,
       "h3cEponMauType1000BasePXOLT": h3cEponMauType1000BasePXOLT,
       "h3cEponMauType1000BasePXONU": h3cEponMauType1000BasePXONU,
       "h3cEponMauType1000BasePX10DOLT": h3cEponMauType1000BasePX10DOLT,
       "h3cEponMauType1000BasePX10DONU": h3cEponMauType1000BasePX10DONU,
       "h3cEponMauType1000BasePX10UOLT": h3cEponMauType1000BasePX10UOLT,
       "h3cEponMauType1000BasePX10UONU": h3cEponMauType1000BasePX10UONU,
       "h3cEponMauType1000BasePX20DOLT": h3cEponMauType1000BasePX20DOLT,
       "h3cEponMauType1000BasePX20DONU": h3cEponMauType1000BasePX20DONU,
       "h3cEponMauType1000BasePX20UOLT": h3cEponMauType1000BasePX20UOLT,
       "h3cEponMauType1000BasePX20UONU": h3cEponMauType1000BasePX20UONU}
)
