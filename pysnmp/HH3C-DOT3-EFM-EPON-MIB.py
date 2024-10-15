# SNMP MIB module (HH3C-DOT3-EFM-EPON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-DOT3-EFM-EPON-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:52:59 2024
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

(hh3cEpon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cEpon")

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

hh3cDot3EfmeponMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 2)
)
hh3cDot3EfmeponMIB.setRevisions(
        ("2004-09-21 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cDot3MpcpMIB_ObjectIdentity = ObjectIdentity
hh3cDot3MpcpMIB = _Hh3cDot3MpcpMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 2, 1)
)
_Hh3cDot3MpcpObjects_ObjectIdentity = ObjectIdentity
hh3cDot3MpcpObjects = _Hh3cDot3MpcpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 2, 1, 1)
)
_Hh3cDot3MpcpTable_Object = MibTable
hh3cDot3MpcpTable = _Hh3cDot3MpcpTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cDot3MpcpTable.setStatus("current")
_Hh3cDot3MpcpEntry_Object = MibTableRow
hh3cDot3MpcpEntry = _Hh3cDot3MpcpEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 2, 1, 1, 1, 1)
)
hh3cDot3MpcpEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cDot3MpcpEntry.setStatus("current")
_Hh3cDot3MpcpID_Type = Integer32
_Hh3cDot3MpcpID_Object = MibTableColumn
hh3cDot3MpcpID = _Hh3cDot3MpcpID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 2, 1, 1, 1, 1, 1),
    _Hh3cDot3MpcpID_Type()
)
hh3cDot3MpcpID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot3MpcpID.setStatus("current")
_Hh3cDot3MpcpOperStatus_Type = TruthValue
_Hh3cDot3MpcpOperStatus_Object = MibTableColumn
hh3cDot3MpcpOperStatus = _Hh3cDot3MpcpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 2, 1, 1, 1, 1, 2),
    _Hh3cDot3MpcpOperStatus_Type()
)
hh3cDot3MpcpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot3MpcpOperStatus.setStatus("current")


class _Hh3cDot3MpcpMode_Type(Integer32):
    """Custom type hh3cDot3MpcpMode based on Integer32"""
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


_Hh3cDot3MpcpMode_Type.__name__ = "Integer32"
_Hh3cDot3MpcpMode_Object = MibTableColumn
hh3cDot3MpcpMode = _Hh3cDot3MpcpMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 2, 1, 1, 1, 1, 3),
    _Hh3cDot3MpcpMode_Type()
)
hh3cDot3MpcpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot3MpcpMode.setStatus("current")
_Hh3cDot3MpcpLinkID_Type = Integer32
_Hh3cDot3MpcpLinkID_Object = MibTableColumn
hh3cDot3MpcpLinkID = _Hh3cDot3MpcpLinkID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 2, 1, 1, 1, 1, 4),
    _Hh3cDot3MpcpLinkID_Type()
)
hh3cDot3MpcpLinkID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot3MpcpLinkID.setStatus("current")
_Hh3cDot3MpcpRemoteMACAddress_Type = MacAddress
_Hh3cDot3MpcpRemoteMACAddress_Object = MibTableColumn
hh3cDot3MpcpRemoteMACAddress = _Hh3cDot3MpcpRemoteMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 2, 1, 1, 1, 1, 5),
    _Hh3cDot3MpcpRemoteMACAddress_Type()
)
hh3cDot3MpcpRemoteMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot3MpcpRemoteMACAddress.setStatus("current")


class _Hh3cDot3MpcpRegistrationState_Type(Integer32):
    """Custom type hh3cDot3MpcpRegistrationState based on Integer32"""
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


_Hh3cDot3MpcpRegistrationState_Type.__name__ = "Integer32"
_Hh3cDot3MpcpRegistrationState_Object = MibTableColumn
hh3cDot3MpcpRegistrationState = _Hh3cDot3MpcpRegistrationState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 2, 1, 1, 1, 1, 6),
    _Hh3cDot3MpcpRegistrationState_Type()
)
hh3cDot3MpcpRegistrationState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot3MpcpRegistrationState.setStatus("current")
_Hh3cDot3MpcpTransmitElapsed_Type = Integer32
_Hh3cDot3MpcpTransmitElapsed_Object = MibTableColumn
hh3cDot3MpcpTransmitElapsed = _Hh3cDot3MpcpTransmitElapsed_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 2, 1, 1, 1, 1, 7),
    _Hh3cDot3MpcpTransmitElapsed_Type()
)
hh3cDot3MpcpTransmitElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot3MpcpTransmitElapsed.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot3MpcpTransmitElapsed.setUnits("TQ (16nsec)")
_Hh3cDot3MpcpReceiveElapsed_Type = Integer32
_Hh3cDot3MpcpReceiveElapsed_Object = MibTableColumn
hh3cDot3MpcpReceiveElapsed = _Hh3cDot3MpcpReceiveElapsed_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 2, 1, 1, 1, 1, 8),
    _Hh3cDot3MpcpReceiveElapsed_Type()
)
hh3cDot3MpcpReceiveElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot3MpcpReceiveElapsed.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot3MpcpReceiveElapsed.setUnits("TQ (16nsec)")
_Hh3cDot3MpcpRoundTripTime_Type = Integer32
_Hh3cDot3MpcpRoundTripTime_Object = MibTableColumn
hh3cDot3MpcpRoundTripTime = _Hh3cDot3MpcpRoundTripTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 2, 1, 1, 1, 1, 9),
    _Hh3cDot3MpcpRoundTripTime_Type()
)
hh3cDot3MpcpRoundTripTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot3MpcpRoundTripTime.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot3MpcpRoundTripTime.setUnits("TQ (16nsec)")


class _Hh3cDot3MpcpMaximumPendingGrants_Type(Integer32):
    """Custom type hh3cDot3MpcpMaximumPendingGrants based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Hh3cDot3MpcpMaximumPendingGrants_Type.__name__ = "Integer32"
_Hh3cDot3MpcpMaximumPendingGrants_Object = MibTableColumn
hh3cDot3MpcpMaximumPendingGrants = _Hh3cDot3MpcpMaximumPendingGrants_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 2, 1, 1, 1, 1, 10),
    _Hh3cDot3MpcpMaximumPendingGrants_Type()
)
hh3cDot3MpcpMaximumPendingGrants.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot3MpcpMaximumPendingGrants.setStatus("current")


class _Hh3cDot3MpcpAdminState_Type(TruthValue):
    """Custom type hh3cDot3MpcpAdminState based on TruthValue"""


_Hh3cDot3MpcpAdminState_Object = MibTableColumn
hh3cDot3MpcpAdminState = _Hh3cDot3MpcpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 2, 1, 1, 1, 1, 11),
    _Hh3cDot3MpcpAdminState_Type()
)
hh3cDot3MpcpAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot3MpcpAdminState.setStatus("current")
_Hh3cDot3MpcpOnTime_Type = Integer32
_Hh3cDot3MpcpOnTime_Object = MibTableColumn
hh3cDot3MpcpOnTime = _Hh3cDot3MpcpOnTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 2, 1, 1, 1, 1, 12),
    _Hh3cDot3MpcpOnTime_Type()
)
hh3cDot3MpcpOnTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot3MpcpOnTime.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot3MpcpOnTime.setUnits("TQ (16nsec)")
_Hh3cDot3MpcpOffTime_Type = Integer32
_Hh3cDot3MpcpOffTime_Object = MibTableColumn
hh3cDot3MpcpOffTime = _Hh3cDot3MpcpOffTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 2, 1, 1, 1, 1, 13),
    _Hh3cDot3MpcpOffTime_Type()
)
hh3cDot3MpcpOffTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot3MpcpOffTime.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot3MpcpOffTime.setUnits("TQ (16nsec)")
_Hh3cDot3MpcpSyncTime_Type = Integer32
_Hh3cDot3MpcpSyncTime_Object = MibTableColumn
hh3cDot3MpcpSyncTime = _Hh3cDot3MpcpSyncTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 2, 1, 1, 1, 1, 14),
    _Hh3cDot3MpcpSyncTime_Type()
)
hh3cDot3MpcpSyncTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot3MpcpSyncTime.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot3MpcpSyncTime.setUnits("TQ (16nsec)")
_Hh3cDot3MpcpStatTable_Object = MibTable
hh3cDot3MpcpStatTable = _Hh3cDot3MpcpStatTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 2, 1, 1, 2)
)
if mibBuilder.loadTexts:
    hh3cDot3MpcpStatTable.setStatus("current")
_Hh3cDot3MpcpStatEntry_Object = MibTableRow
hh3cDot3MpcpStatEntry = _Hh3cDot3MpcpStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 2, 1, 1, 2, 1)
)
hh3cDot3MpcpStatEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cDot3MpcpStatEntry.setStatus("current")
_Hh3cDot3MpcpMACCtrlFramesTransmitted_Type = Counter32
_Hh3cDot3MpcpMACCtrlFramesTransmitted_Object = MibTableColumn
hh3cDot3MpcpMACCtrlFramesTransmitted = _Hh3cDot3MpcpMACCtrlFramesTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 2, 1, 1, 2, 1, 1),
    _Hh3cDot3MpcpMACCtrlFramesTransmitted_Type()
)
hh3cDot3MpcpMACCtrlFramesTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot3MpcpMACCtrlFramesTransmitted.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot3MpcpMACCtrlFramesTransmitted.setUnits("frames")
_Hh3cDot3MpcpMACCtrlFramesReceived_Type = Counter32
_Hh3cDot3MpcpMACCtrlFramesReceived_Object = MibTableColumn
hh3cDot3MpcpMACCtrlFramesReceived = _Hh3cDot3MpcpMACCtrlFramesReceived_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 2, 1, 1, 2, 1, 2),
    _Hh3cDot3MpcpMACCtrlFramesReceived_Type()
)
hh3cDot3MpcpMACCtrlFramesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot3MpcpMACCtrlFramesReceived.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot3MpcpMACCtrlFramesReceived.setUnits("frames")
_Hh3cDot3MpcpDiscoveryWindowsSent_Type = Counter32
_Hh3cDot3MpcpDiscoveryWindowsSent_Object = MibTableColumn
hh3cDot3MpcpDiscoveryWindowsSent = _Hh3cDot3MpcpDiscoveryWindowsSent_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 2, 1, 1, 2, 1, 3),
    _Hh3cDot3MpcpDiscoveryWindowsSent_Type()
)
hh3cDot3MpcpDiscoveryWindowsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot3MpcpDiscoveryWindowsSent.setStatus("current")
_Hh3cDot3MpcpDiscoveryTimeout_Type = Counter32
_Hh3cDot3MpcpDiscoveryTimeout_Object = MibTableColumn
hh3cDot3MpcpDiscoveryTimeout = _Hh3cDot3MpcpDiscoveryTimeout_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 2, 1, 1, 2, 1, 4),
    _Hh3cDot3MpcpDiscoveryTimeout_Type()
)
hh3cDot3MpcpDiscoveryTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot3MpcpDiscoveryTimeout.setStatus("current")
_Hh3cDot3MpcpTxRegRequest_Type = Counter32
_Hh3cDot3MpcpTxRegRequest_Object = MibTableColumn
hh3cDot3MpcpTxRegRequest = _Hh3cDot3MpcpTxRegRequest_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 2, 1, 1, 2, 1, 5),
    _Hh3cDot3MpcpTxRegRequest_Type()
)
hh3cDot3MpcpTxRegRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot3MpcpTxRegRequest.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot3MpcpTxRegRequest.setUnits("frames")
_Hh3cDot3MpcpRxRegRequest_Type = Counter32
_Hh3cDot3MpcpRxRegRequest_Object = MibTableColumn
hh3cDot3MpcpRxRegRequest = _Hh3cDot3MpcpRxRegRequest_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 2, 1, 1, 2, 1, 6),
    _Hh3cDot3MpcpRxRegRequest_Type()
)
hh3cDot3MpcpRxRegRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot3MpcpRxRegRequest.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot3MpcpRxRegRequest.setUnits("frames")
_Hh3cDot3MpcpTxRegAck_Type = Counter32
_Hh3cDot3MpcpTxRegAck_Object = MibTableColumn
hh3cDot3MpcpTxRegAck = _Hh3cDot3MpcpTxRegAck_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 2, 1, 1, 2, 1, 7),
    _Hh3cDot3MpcpTxRegAck_Type()
)
hh3cDot3MpcpTxRegAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot3MpcpTxRegAck.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot3MpcpTxRegAck.setUnits("frames")
_Hh3cDot3MpcpRxRegAck_Type = Counter32
_Hh3cDot3MpcpRxRegAck_Object = MibTableColumn
hh3cDot3MpcpRxRegAck = _Hh3cDot3MpcpRxRegAck_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 2, 1, 1, 2, 1, 8),
    _Hh3cDot3MpcpRxRegAck_Type()
)
hh3cDot3MpcpRxRegAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot3MpcpRxRegAck.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot3MpcpRxRegAck.setUnits("frames")
_Hh3cDot3MpcpTxReport_Type = Counter32
_Hh3cDot3MpcpTxReport_Object = MibTableColumn
hh3cDot3MpcpTxReport = _Hh3cDot3MpcpTxReport_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 2, 1, 1, 2, 1, 9),
    _Hh3cDot3MpcpTxReport_Type()
)
hh3cDot3MpcpTxReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot3MpcpTxReport.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot3MpcpTxReport.setUnits("frames")
_Hh3cDot3MpcpRxReport_Type = Counter32
_Hh3cDot3MpcpRxReport_Object = MibTableColumn
hh3cDot3MpcpRxReport = _Hh3cDot3MpcpRxReport_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 2, 1, 1, 2, 1, 10),
    _Hh3cDot3MpcpRxReport_Type()
)
hh3cDot3MpcpRxReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot3MpcpRxReport.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot3MpcpRxReport.setUnits("frames")
_Hh3cDot3MpcpTxGate_Type = Counter32
_Hh3cDot3MpcpTxGate_Object = MibTableColumn
hh3cDot3MpcpTxGate = _Hh3cDot3MpcpTxGate_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 2, 1, 1, 2, 1, 11),
    _Hh3cDot3MpcpTxGate_Type()
)
hh3cDot3MpcpTxGate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot3MpcpTxGate.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot3MpcpTxGate.setUnits("frames")
_Hh3cDot3MpcpRxGate_Type = Counter32
_Hh3cDot3MpcpRxGate_Object = MibTableColumn
hh3cDot3MpcpRxGate = _Hh3cDot3MpcpRxGate_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 2, 1, 1, 2, 1, 12),
    _Hh3cDot3MpcpRxGate_Type()
)
hh3cDot3MpcpRxGate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot3MpcpRxGate.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot3MpcpRxGate.setUnits("frames")
_Hh3cDot3MpcpTxRegister_Type = Counter32
_Hh3cDot3MpcpTxRegister_Object = MibTableColumn
hh3cDot3MpcpTxRegister = _Hh3cDot3MpcpTxRegister_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 2, 1, 1, 2, 1, 13),
    _Hh3cDot3MpcpTxRegister_Type()
)
hh3cDot3MpcpTxRegister.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot3MpcpTxRegister.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot3MpcpTxRegister.setUnits("frames")
_Hh3cDot3MpcpRxRegister_Type = Counter32
_Hh3cDot3MpcpRxRegister_Object = MibTableColumn
hh3cDot3MpcpRxRegister = _Hh3cDot3MpcpRxRegister_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 2, 1, 1, 2, 1, 14),
    _Hh3cDot3MpcpRxRegister_Type()
)
hh3cDot3MpcpRxRegister.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot3MpcpRxRegister.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot3MpcpRxRegister.setUnits("frames")
_Hh3cDot3MpcpRxNotSupportedMPCP_Type = Counter32
_Hh3cDot3MpcpRxNotSupportedMPCP_Object = MibTableColumn
hh3cDot3MpcpRxNotSupportedMPCP = _Hh3cDot3MpcpRxNotSupportedMPCP_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 2, 1, 1, 2, 1, 15),
    _Hh3cDot3MpcpRxNotSupportedMPCP_Type()
)
hh3cDot3MpcpRxNotSupportedMPCP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot3MpcpRxNotSupportedMPCP.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot3MpcpRxNotSupportedMPCP.setUnits("frames")
_Hh3cDot3MpcpConformance_ObjectIdentity = ObjectIdentity
hh3cDot3MpcpConformance = _Hh3cDot3MpcpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 2, 1, 2)
)
_Hh3cDot3MpcpGroups_ObjectIdentity = ObjectIdentity
hh3cDot3MpcpGroups = _Hh3cDot3MpcpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 2, 1, 2, 1)
)
_Hh3cDot3MpcpCompliances_ObjectIdentity = ObjectIdentity
hh3cDot3MpcpCompliances = _Hh3cDot3MpcpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 2, 1, 2, 2)
)
_Hh3cDot3OmpEmulationMIB_ObjectIdentity = ObjectIdentity
hh3cDot3OmpEmulationMIB = _Hh3cDot3OmpEmulationMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 2, 2)
)
_Hh3cDot3OmpEmulationObjects_ObjectIdentity = ObjectIdentity
hh3cDot3OmpEmulationObjects = _Hh3cDot3OmpEmulationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 2, 2, 1)
)
_Hh3cDot3OmpEmulationTable_Object = MibTable
hh3cDot3OmpEmulationTable = _Hh3cDot3OmpEmulationTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cDot3OmpEmulationTable.setStatus("current")
_Hh3cDot3OmpEmulationEntry_Object = MibTableRow
hh3cDot3OmpEmulationEntry = _Hh3cDot3OmpEmulationEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 2, 2, 1, 1, 1)
)
hh3cDot3OmpEmulationEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cDot3OmpEmulationEntry.setStatus("current")
_Hh3cDot3OmpEmulationID_Type = Integer32
_Hh3cDot3OmpEmulationID_Object = MibTableColumn
hh3cDot3OmpEmulationID = _Hh3cDot3OmpEmulationID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 2, 2, 1, 1, 1, 1),
    _Hh3cDot3OmpEmulationID_Type()
)
hh3cDot3OmpEmulationID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot3OmpEmulationID.setStatus("current")


class _Hh3cDot3OmpEmulationType_Type(Integer32):
    """Custom type hh3cDot3OmpEmulationType based on Integer32"""
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


_Hh3cDot3OmpEmulationType_Type.__name__ = "Integer32"
_Hh3cDot3OmpEmulationType_Object = MibTableColumn
hh3cDot3OmpEmulationType = _Hh3cDot3OmpEmulationType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 2, 2, 1, 1, 1, 2),
    _Hh3cDot3OmpEmulationType_Type()
)
hh3cDot3OmpEmulationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot3OmpEmulationType.setStatus("current")
_Hh3cDot3OmpEmulationStatTable_Object = MibTable
hh3cDot3OmpEmulationStatTable = _Hh3cDot3OmpEmulationStatTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 2, 2, 1, 2)
)
if mibBuilder.loadTexts:
    hh3cDot3OmpEmulationStatTable.setStatus("current")
_Hh3cDot3OmpEmulationStatEntry_Object = MibTableRow
hh3cDot3OmpEmulationStatEntry = _Hh3cDot3OmpEmulationStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 2, 2, 1, 2, 1)
)
hh3cDot3OmpEmulationStatEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cDot3OmpEmulationStatEntry.setStatus("current")
_Hh3cDot3OmpEmulationSLDErrors_Type = Counter32
_Hh3cDot3OmpEmulationSLDErrors_Object = MibTableColumn
hh3cDot3OmpEmulationSLDErrors = _Hh3cDot3OmpEmulationSLDErrors_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 2, 2, 1, 2, 1, 1),
    _Hh3cDot3OmpEmulationSLDErrors_Type()
)
hh3cDot3OmpEmulationSLDErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot3OmpEmulationSLDErrors.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot3OmpEmulationSLDErrors.setUnits("frames")
_Hh3cDot3OmpEmulationCRC8Errors_Type = Counter32
_Hh3cDot3OmpEmulationCRC8Errors_Object = MibTableColumn
hh3cDot3OmpEmulationCRC8Errors = _Hh3cDot3OmpEmulationCRC8Errors_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 2, 2, 1, 2, 1, 2),
    _Hh3cDot3OmpEmulationCRC8Errors_Type()
)
hh3cDot3OmpEmulationCRC8Errors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot3OmpEmulationCRC8Errors.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot3OmpEmulationCRC8Errors.setUnits("frames")
_Hh3cDot3OmpEmulationBadLLID_Type = Counter32
_Hh3cDot3OmpEmulationBadLLID_Object = MibTableColumn
hh3cDot3OmpEmulationBadLLID = _Hh3cDot3OmpEmulationBadLLID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 2, 2, 1, 2, 1, 3),
    _Hh3cDot3OmpEmulationBadLLID_Type()
)
hh3cDot3OmpEmulationBadLLID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot3OmpEmulationBadLLID.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot3OmpEmulationBadLLID.setUnits("frames")
_Hh3cDot3OmpEmulationGoodLLID_Type = Counter32
_Hh3cDot3OmpEmulationGoodLLID_Object = MibTableColumn
hh3cDot3OmpEmulationGoodLLID = _Hh3cDot3OmpEmulationGoodLLID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 2, 2, 1, 2, 1, 4),
    _Hh3cDot3OmpEmulationGoodLLID_Type()
)
hh3cDot3OmpEmulationGoodLLID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot3OmpEmulationGoodLLID.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot3OmpEmulationGoodLLID.setUnits("frames")
_Hh3cDot3OmpEmulationOnuPonCastLLID_Type = Counter32
_Hh3cDot3OmpEmulationOnuPonCastLLID_Object = MibTableColumn
hh3cDot3OmpEmulationOnuPonCastLLID = _Hh3cDot3OmpEmulationOnuPonCastLLID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 2, 2, 1, 2, 1, 5),
    _Hh3cDot3OmpEmulationOnuPonCastLLID_Type()
)
hh3cDot3OmpEmulationOnuPonCastLLID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot3OmpEmulationOnuPonCastLLID.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot3OmpEmulationOnuPonCastLLID.setUnits("frames")
_Hh3cDot3OmpEmulationOltPonCastLLID_Type = Counter32
_Hh3cDot3OmpEmulationOltPonCastLLID_Object = MibTableColumn
hh3cDot3OmpEmulationOltPonCastLLID = _Hh3cDot3OmpEmulationOltPonCastLLID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 2, 2, 1, 2, 1, 6),
    _Hh3cDot3OmpEmulationOltPonCastLLID_Type()
)
hh3cDot3OmpEmulationOltPonCastLLID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot3OmpEmulationOltPonCastLLID.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot3OmpEmulationOltPonCastLLID.setUnits("frames")
_Hh3cDot3OmpEmulationBroadcastLLIDNotOnuID_Type = Counter32
_Hh3cDot3OmpEmulationBroadcastLLIDNotOnuID_Object = MibTableColumn
hh3cDot3OmpEmulationBroadcastLLIDNotOnuID = _Hh3cDot3OmpEmulationBroadcastLLIDNotOnuID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 2, 2, 1, 2, 1, 7),
    _Hh3cDot3OmpEmulationBroadcastLLIDNotOnuID_Type()
)
hh3cDot3OmpEmulationBroadcastLLIDNotOnuID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot3OmpEmulationBroadcastLLIDNotOnuID.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot3OmpEmulationBroadcastLLIDNotOnuID.setUnits("frames")
_Hh3cDot3OmpEmulationOnuLLIDNotBroadcast_Type = Counter32
_Hh3cDot3OmpEmulationOnuLLIDNotBroadcast_Object = MibTableColumn
hh3cDot3OmpEmulationOnuLLIDNotBroadcast = _Hh3cDot3OmpEmulationOnuLLIDNotBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 2, 2, 1, 2, 1, 8),
    _Hh3cDot3OmpEmulationOnuLLIDNotBroadcast_Type()
)
hh3cDot3OmpEmulationOnuLLIDNotBroadcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot3OmpEmulationOnuLLIDNotBroadcast.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot3OmpEmulationOnuLLIDNotBroadcast.setUnits("frames")
_Hh3cDot3OmpEmulationBroadcastLLIDPlusOnuId_Type = Counter32
_Hh3cDot3OmpEmulationBroadcastLLIDPlusOnuId_Object = MibTableColumn
hh3cDot3OmpEmulationBroadcastLLIDPlusOnuId = _Hh3cDot3OmpEmulationBroadcastLLIDPlusOnuId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 2, 2, 1, 2, 1, 9),
    _Hh3cDot3OmpEmulationBroadcastLLIDPlusOnuId_Type()
)
hh3cDot3OmpEmulationBroadcastLLIDPlusOnuId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot3OmpEmulationBroadcastLLIDPlusOnuId.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot3OmpEmulationBroadcastLLIDPlusOnuId.setUnits("frames")
_Hh3cDot3OmpEmulationNotBroadcastLLIDNotOnuId_Type = Counter32
_Hh3cDot3OmpEmulationNotBroadcastLLIDNotOnuId_Object = MibTableColumn
hh3cDot3OmpEmulationNotBroadcastLLIDNotOnuId = _Hh3cDot3OmpEmulationNotBroadcastLLIDNotOnuId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 2, 2, 1, 2, 1, 10),
    _Hh3cDot3OmpEmulationNotBroadcastLLIDNotOnuId_Type()
)
hh3cDot3OmpEmulationNotBroadcastLLIDNotOnuId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot3OmpEmulationNotBroadcastLLIDNotOnuId.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot3OmpEmulationNotBroadcastLLIDNotOnuId.setUnits("frames")
_Hh3cDot3OmpeConformance_ObjectIdentity = ObjectIdentity
hh3cDot3OmpeConformance = _Hh3cDot3OmpeConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 2, 2, 2)
)
_Hh3cDot3OmpeGroups_ObjectIdentity = ObjectIdentity
hh3cDot3OmpeGroups = _Hh3cDot3OmpeGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 2, 2, 2, 1)
)
_Hh3cDot3OmpeCompliances_ObjectIdentity = ObjectIdentity
hh3cDot3OmpeCompliances = _Hh3cDot3OmpeCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 2, 2, 2, 2)
)
_Hh3cDot3EponMauMIB_ObjectIdentity = ObjectIdentity
hh3cDot3EponMauMIB = _Hh3cDot3EponMauMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 2, 3)
)
_Hh3cDot3EponMauObjects_ObjectIdentity = ObjectIdentity
hh3cDot3EponMauObjects = _Hh3cDot3EponMauObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 2, 3, 1)
)
_Hh3cDot3EponMauTable_Object = MibTable
hh3cDot3EponMauTable = _Hh3cDot3EponMauTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 2, 3, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cDot3EponMauTable.setStatus("current")
_Hh3cDot3EponMauEntry_Object = MibTableRow
hh3cDot3EponMauEntry = _Hh3cDot3EponMauEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 2, 3, 1, 1, 1)
)
hh3cDot3EponMauEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cDot3EponMauEntry.setStatus("current")
_Hh3cDot3EponMauPCSCodingViolation_Type = Counter32
_Hh3cDot3EponMauPCSCodingViolation_Object = MibTableColumn
hh3cDot3EponMauPCSCodingViolation = _Hh3cDot3EponMauPCSCodingViolation_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 2, 3, 1, 1, 1, 1),
    _Hh3cDot3EponMauPCSCodingViolation_Type()
)
hh3cDot3EponMauPCSCodingViolation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot3EponMauPCSCodingViolation.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot3EponMauPCSCodingViolation.setUnits("octets")


class _Hh3cDot3EponMauFecAbility_Type(Integer32):
    """Custom type hh3cDot3EponMauFecAbility based on Integer32"""
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


_Hh3cDot3EponMauFecAbility_Type.__name__ = "Integer32"
_Hh3cDot3EponMauFecAbility_Object = MibTableColumn
hh3cDot3EponMauFecAbility = _Hh3cDot3EponMauFecAbility_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 2, 3, 1, 1, 1, 2),
    _Hh3cDot3EponMauFecAbility_Type()
)
hh3cDot3EponMauFecAbility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot3EponMauFecAbility.setStatus("current")


class _Hh3cDot3EponMauFecMode_Type(Integer32):
    """Custom type hh3cDot3EponMauFecMode based on Integer32"""
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


_Hh3cDot3EponMauFecMode_Type.__name__ = "Integer32"
_Hh3cDot3EponMauFecMode_Object = MibTableColumn
hh3cDot3EponMauFecMode = _Hh3cDot3EponMauFecMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 2, 3, 1, 1, 1, 3),
    _Hh3cDot3EponMauFecMode_Type()
)
hh3cDot3EponMauFecMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot3EponMauFecMode.setStatus("current")
_Hh3cDot3EponMauFECCorrectedBlocks_Type = Counter32
_Hh3cDot3EponMauFECCorrectedBlocks_Object = MibTableColumn
hh3cDot3EponMauFECCorrectedBlocks = _Hh3cDot3EponMauFECCorrectedBlocks_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 2, 3, 1, 1, 1, 4),
    _Hh3cDot3EponMauFECCorrectedBlocks_Type()
)
hh3cDot3EponMauFECCorrectedBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot3EponMauFECCorrectedBlocks.setStatus("current")
_Hh3cDot3EponMauFECUncorrectableBlocks_Type = Counter32
_Hh3cDot3EponMauFECUncorrectableBlocks_Object = MibTableColumn
hh3cDot3EponMauFECUncorrectableBlocks = _Hh3cDot3EponMauFECUncorrectableBlocks_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 2, 3, 1, 1, 1, 5),
    _Hh3cDot3EponMauFECUncorrectableBlocks_Type()
)
hh3cDot3EponMauFECUncorrectableBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot3EponMauFECUncorrectableBlocks.setStatus("current")
_Hh3cDot3EponMauBufferHeadCodingViolation_Type = Counter32
_Hh3cDot3EponMauBufferHeadCodingViolation_Object = MibTableColumn
hh3cDot3EponMauBufferHeadCodingViolation = _Hh3cDot3EponMauBufferHeadCodingViolation_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 2, 3, 1, 1, 1, 6),
    _Hh3cDot3EponMauBufferHeadCodingViolation_Type()
)
hh3cDot3EponMauBufferHeadCodingViolation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot3EponMauBufferHeadCodingViolation.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot3EponMauBufferHeadCodingViolation.setUnits("octets")
_Hh3cDot3EponMauConformance_ObjectIdentity = ObjectIdentity
hh3cDot3EponMauConformance = _Hh3cDot3EponMauConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 2, 3, 2)
)
_Hh3cDot3EponMauGroups_ObjectIdentity = ObjectIdentity
hh3cDot3EponMauGroups = _Hh3cDot3EponMauGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 2, 3, 2, 1)
)
_Hh3cDot3EponMauCompliances_ObjectIdentity = ObjectIdentity
hh3cDot3EponMauCompliances = _Hh3cDot3EponMauCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 2, 3, 2, 2)
)
_Hh3cDot3EponMauType_ObjectIdentity = ObjectIdentity
hh3cDot3EponMauType = _Hh3cDot3EponMauType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 2, 3, 3)
)
_Hh3cEponMauType1000BasePXOLT_ObjectIdentity = ObjectIdentity
hh3cEponMauType1000BasePXOLT = _Hh3cEponMauType1000BasePXOLT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 2, 3, 3, 1)
)
if mibBuilder.loadTexts:
    hh3cEponMauType1000BasePXOLT.setStatus("current")
_Hh3cEponMauType1000BasePXONU_ObjectIdentity = ObjectIdentity
hh3cEponMauType1000BasePXONU = _Hh3cEponMauType1000BasePXONU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 2, 3, 3, 2)
)
if mibBuilder.loadTexts:
    hh3cEponMauType1000BasePXONU.setStatus("current")
_Hh3cEponMauType1000BasePX10DOLT_ObjectIdentity = ObjectIdentity
hh3cEponMauType1000BasePX10DOLT = _Hh3cEponMauType1000BasePX10DOLT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 2, 3, 3, 3)
)
if mibBuilder.loadTexts:
    hh3cEponMauType1000BasePX10DOLT.setStatus("current")
_Hh3cEponMauType1000BasePX10DONU_ObjectIdentity = ObjectIdentity
hh3cEponMauType1000BasePX10DONU = _Hh3cEponMauType1000BasePX10DONU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 2, 3, 3, 4)
)
if mibBuilder.loadTexts:
    hh3cEponMauType1000BasePX10DONU.setStatus("current")
_Hh3cEponMauType1000BasePX10UOLT_ObjectIdentity = ObjectIdentity
hh3cEponMauType1000BasePX10UOLT = _Hh3cEponMauType1000BasePX10UOLT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 2, 3, 3, 5)
)
if mibBuilder.loadTexts:
    hh3cEponMauType1000BasePX10UOLT.setStatus("current")
_Hh3cEponMauType1000BasePX10UONU_ObjectIdentity = ObjectIdentity
hh3cEponMauType1000BasePX10UONU = _Hh3cEponMauType1000BasePX10UONU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 2, 3, 3, 6)
)
if mibBuilder.loadTexts:
    hh3cEponMauType1000BasePX10UONU.setStatus("current")
_Hh3cEponMauType1000BasePX20DOLT_ObjectIdentity = ObjectIdentity
hh3cEponMauType1000BasePX20DOLT = _Hh3cEponMauType1000BasePX20DOLT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 2, 3, 3, 7)
)
if mibBuilder.loadTexts:
    hh3cEponMauType1000BasePX20DOLT.setStatus("current")
_Hh3cEponMauType1000BasePX20DONU_ObjectIdentity = ObjectIdentity
hh3cEponMauType1000BasePX20DONU = _Hh3cEponMauType1000BasePX20DONU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 2, 3, 3, 8)
)
if mibBuilder.loadTexts:
    hh3cEponMauType1000BasePX20DONU.setStatus("current")
_Hh3cEponMauType1000BasePX20UOLT_ObjectIdentity = ObjectIdentity
hh3cEponMauType1000BasePX20UOLT = _Hh3cEponMauType1000BasePX20UOLT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 2, 3, 3, 9)
)
if mibBuilder.loadTexts:
    hh3cEponMauType1000BasePX20UOLT.setStatus("current")
_Hh3cEponMauType1000BasePX20UONU_ObjectIdentity = ObjectIdentity
hh3cEponMauType1000BasePX20UONU = _Hh3cEponMauType1000BasePX20UONU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 2, 3, 3, 10)
)
if mibBuilder.loadTexts:
    hh3cEponMauType1000BasePX20UONU.setStatus("current")

# Managed Objects groups

hh3cDot3MpcpGroupBase = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 2, 1, 2, 1, 1)
)
hh3cDot3MpcpGroupBase.setObjects(
      *(("HH3C-DOT3-EFM-EPON-MIB", "hh3cDot3MpcpID"),
        ("HH3C-DOT3-EFM-EPON-MIB", "hh3cDot3MpcpOperStatus"),
        ("HH3C-DOT3-EFM-EPON-MIB", "hh3cDot3MpcpMode"),
        ("HH3C-DOT3-EFM-EPON-MIB", "hh3cDot3MpcpLinkID"),
        ("HH3C-DOT3-EFM-EPON-MIB", "hh3cDot3MpcpRemoteMACAddress"),
        ("HH3C-DOT3-EFM-EPON-MIB", "hh3cDot3MpcpRegistrationState"),
        ("HH3C-DOT3-EFM-EPON-MIB", "hh3cDot3MpcpMaximumPendingGrants"),
        ("HH3C-DOT3-EFM-EPON-MIB", "hh3cDot3MpcpAdminState"))
)
if mibBuilder.loadTexts:
    hh3cDot3MpcpGroupBase.setStatus("current")

hh3cDot3MpcpGroupParam = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 2, 1, 2, 1, 2)
)
hh3cDot3MpcpGroupParam.setObjects(
      *(("HH3C-DOT3-EFM-EPON-MIB", "hh3cDot3MpcpTransmitElapsed"),
        ("HH3C-DOT3-EFM-EPON-MIB", "hh3cDot3MpcpReceiveElapsed"),
        ("HH3C-DOT3-EFM-EPON-MIB", "hh3cDot3MpcpRoundTripTime"),
        ("HH3C-DOT3-EFM-EPON-MIB", "hh3cDot3MpcpOnTime"),
        ("HH3C-DOT3-EFM-EPON-MIB", "hh3cDot3MpcpOffTime"),
        ("HH3C-DOT3-EFM-EPON-MIB", "hh3cDot3MpcpSyncTime"))
)
if mibBuilder.loadTexts:
    hh3cDot3MpcpGroupParam.setStatus("current")

hh3cDot3MpcpGroupStat = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 2, 1, 2, 1, 3)
)
hh3cDot3MpcpGroupStat.setObjects(
      *(("HH3C-DOT3-EFM-EPON-MIB", "hh3cDot3MpcpMACCtrlFramesTransmitted"),
        ("HH3C-DOT3-EFM-EPON-MIB", "hh3cDot3MpcpMACCtrlFramesReceived"),
        ("HH3C-DOT3-EFM-EPON-MIB", "hh3cDot3MpcpDiscoveryWindowsSent"),
        ("HH3C-DOT3-EFM-EPON-MIB", "hh3cDot3MpcpDiscoveryTimeout"),
        ("HH3C-DOT3-EFM-EPON-MIB", "hh3cDot3MpcpTxRegRequest"),
        ("HH3C-DOT3-EFM-EPON-MIB", "hh3cDot3MpcpRxRegRequest"),
        ("HH3C-DOT3-EFM-EPON-MIB", "hh3cDot3MpcpTxRegAck"),
        ("HH3C-DOT3-EFM-EPON-MIB", "hh3cDot3MpcpRxRegAck"),
        ("HH3C-DOT3-EFM-EPON-MIB", "hh3cDot3MpcpTxReport"),
        ("HH3C-DOT3-EFM-EPON-MIB", "hh3cDot3MpcpRxReport"),
        ("HH3C-DOT3-EFM-EPON-MIB", "hh3cDot3MpcpTxGate"),
        ("HH3C-DOT3-EFM-EPON-MIB", "hh3cDot3MpcpRxGate"),
        ("HH3C-DOT3-EFM-EPON-MIB", "hh3cDot3MpcpTxRegister"),
        ("HH3C-DOT3-EFM-EPON-MIB", "hh3cDot3MpcpRxRegister"),
        ("HH3C-DOT3-EFM-EPON-MIB", "hh3cDot3MpcpRxNotSupportedMPCP"))
)
if mibBuilder.loadTexts:
    hh3cDot3MpcpGroupStat.setStatus("current")

hh3cDot3OmpeGroupID = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 2, 2, 2, 1, 1)
)
hh3cDot3OmpeGroupID.setObjects(
      *(("HH3C-DOT3-EFM-EPON-MIB", "hh3cDot3OmpEmulationID"),
        ("HH3C-DOT3-EFM-EPON-MIB", "hh3cDot3OmpEmulationType"))
)
if mibBuilder.loadTexts:
    hh3cDot3OmpeGroupID.setStatus("current")

hh3cDot3OmpeGroupStat = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 2, 2, 2, 1, 2)
)
hh3cDot3OmpeGroupStat.setObjects(
      *(("HH3C-DOT3-EFM-EPON-MIB", "hh3cDot3OmpEmulationSLDErrors"),
        ("HH3C-DOT3-EFM-EPON-MIB", "hh3cDot3OmpEmulationCRC8Errors"),
        ("HH3C-DOT3-EFM-EPON-MIB", "hh3cDot3OmpEmulationBadLLID"),
        ("HH3C-DOT3-EFM-EPON-MIB", "hh3cDot3OmpEmulationGoodLLID"),
        ("HH3C-DOT3-EFM-EPON-MIB", "hh3cDot3OmpEmulationOnuPonCastLLID"),
        ("HH3C-DOT3-EFM-EPON-MIB", "hh3cDot3OmpEmulationOltPonCastLLID"),
        ("HH3C-DOT3-EFM-EPON-MIB", "hh3cDot3OmpEmulationBroadcastLLIDNotOnuID"),
        ("HH3C-DOT3-EFM-EPON-MIB", "hh3cDot3OmpEmulationOnuLLIDNotBroadcast"),
        ("HH3C-DOT3-EFM-EPON-MIB", "hh3cDot3OmpEmulationBroadcastLLIDPlusOnuId"),
        ("HH3C-DOT3-EFM-EPON-MIB", "hh3cDot3OmpEmulationNotBroadcastLLIDNotOnuId"))
)
if mibBuilder.loadTexts:
    hh3cDot3OmpeGroupStat.setStatus("current")

hh3cDot3EponMauGroupAll = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 2, 3, 2, 1, 1)
)
hh3cDot3EponMauGroupAll.setObjects(
    ("HH3C-DOT3-EFM-EPON-MIB", "hh3cDot3EponMauPCSCodingViolation")
)
if mibBuilder.loadTexts:
    hh3cDot3EponMauGroupAll.setStatus("current")

hh3cDot3EponMauGroupFEC = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 2, 3, 2, 1, 2)
)
hh3cDot3EponMauGroupFEC.setObjects(
      *(("HH3C-DOT3-EFM-EPON-MIB", "hh3cDot3EponMauFecAbility"),
        ("HH3C-DOT3-EFM-EPON-MIB", "hh3cDot3EponMauFecMode"),
        ("HH3C-DOT3-EFM-EPON-MIB", "hh3cDot3EponMauFECCorrectedBlocks"),
        ("HH3C-DOT3-EFM-EPON-MIB", "hh3cDot3EponMauFECUncorrectableBlocks"),
        ("HH3C-DOT3-EFM-EPON-MIB", "hh3cDot3EponMauBufferHeadCodingViolation"))
)
if mibBuilder.loadTexts:
    hh3cDot3EponMauGroupFEC.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hh3cDot3MpcpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 2, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    hh3cDot3MpcpCompliance.setStatus(
        "current"
    )

hh3cDot3OmpeCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 2, 2, 2, 2, 1)
)
if mibBuilder.loadTexts:
    hh3cDot3OmpeCompliance.setStatus(
        "current"
    )

hh3cDot3EponMauCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 2, 3, 2, 2, 1)
)
if mibBuilder.loadTexts:
    hh3cDot3EponMauCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-DOT3-EFM-EPON-MIB",
    **{"hh3cDot3EfmeponMIB": hh3cDot3EfmeponMIB,
       "hh3cDot3MpcpMIB": hh3cDot3MpcpMIB,
       "hh3cDot3MpcpObjects": hh3cDot3MpcpObjects,
       "hh3cDot3MpcpTable": hh3cDot3MpcpTable,
       "hh3cDot3MpcpEntry": hh3cDot3MpcpEntry,
       "hh3cDot3MpcpID": hh3cDot3MpcpID,
       "hh3cDot3MpcpOperStatus": hh3cDot3MpcpOperStatus,
       "hh3cDot3MpcpMode": hh3cDot3MpcpMode,
       "hh3cDot3MpcpLinkID": hh3cDot3MpcpLinkID,
       "hh3cDot3MpcpRemoteMACAddress": hh3cDot3MpcpRemoteMACAddress,
       "hh3cDot3MpcpRegistrationState": hh3cDot3MpcpRegistrationState,
       "hh3cDot3MpcpTransmitElapsed": hh3cDot3MpcpTransmitElapsed,
       "hh3cDot3MpcpReceiveElapsed": hh3cDot3MpcpReceiveElapsed,
       "hh3cDot3MpcpRoundTripTime": hh3cDot3MpcpRoundTripTime,
       "hh3cDot3MpcpMaximumPendingGrants": hh3cDot3MpcpMaximumPendingGrants,
       "hh3cDot3MpcpAdminState": hh3cDot3MpcpAdminState,
       "hh3cDot3MpcpOnTime": hh3cDot3MpcpOnTime,
       "hh3cDot3MpcpOffTime": hh3cDot3MpcpOffTime,
       "hh3cDot3MpcpSyncTime": hh3cDot3MpcpSyncTime,
       "hh3cDot3MpcpStatTable": hh3cDot3MpcpStatTable,
       "hh3cDot3MpcpStatEntry": hh3cDot3MpcpStatEntry,
       "hh3cDot3MpcpMACCtrlFramesTransmitted": hh3cDot3MpcpMACCtrlFramesTransmitted,
       "hh3cDot3MpcpMACCtrlFramesReceived": hh3cDot3MpcpMACCtrlFramesReceived,
       "hh3cDot3MpcpDiscoveryWindowsSent": hh3cDot3MpcpDiscoveryWindowsSent,
       "hh3cDot3MpcpDiscoveryTimeout": hh3cDot3MpcpDiscoveryTimeout,
       "hh3cDot3MpcpTxRegRequest": hh3cDot3MpcpTxRegRequest,
       "hh3cDot3MpcpRxRegRequest": hh3cDot3MpcpRxRegRequest,
       "hh3cDot3MpcpTxRegAck": hh3cDot3MpcpTxRegAck,
       "hh3cDot3MpcpRxRegAck": hh3cDot3MpcpRxRegAck,
       "hh3cDot3MpcpTxReport": hh3cDot3MpcpTxReport,
       "hh3cDot3MpcpRxReport": hh3cDot3MpcpRxReport,
       "hh3cDot3MpcpTxGate": hh3cDot3MpcpTxGate,
       "hh3cDot3MpcpRxGate": hh3cDot3MpcpRxGate,
       "hh3cDot3MpcpTxRegister": hh3cDot3MpcpTxRegister,
       "hh3cDot3MpcpRxRegister": hh3cDot3MpcpRxRegister,
       "hh3cDot3MpcpRxNotSupportedMPCP": hh3cDot3MpcpRxNotSupportedMPCP,
       "hh3cDot3MpcpConformance": hh3cDot3MpcpConformance,
       "hh3cDot3MpcpGroups": hh3cDot3MpcpGroups,
       "hh3cDot3MpcpGroupBase": hh3cDot3MpcpGroupBase,
       "hh3cDot3MpcpGroupParam": hh3cDot3MpcpGroupParam,
       "hh3cDot3MpcpGroupStat": hh3cDot3MpcpGroupStat,
       "hh3cDot3MpcpCompliances": hh3cDot3MpcpCompliances,
       "hh3cDot3MpcpCompliance": hh3cDot3MpcpCompliance,
       "hh3cDot3OmpEmulationMIB": hh3cDot3OmpEmulationMIB,
       "hh3cDot3OmpEmulationObjects": hh3cDot3OmpEmulationObjects,
       "hh3cDot3OmpEmulationTable": hh3cDot3OmpEmulationTable,
       "hh3cDot3OmpEmulationEntry": hh3cDot3OmpEmulationEntry,
       "hh3cDot3OmpEmulationID": hh3cDot3OmpEmulationID,
       "hh3cDot3OmpEmulationType": hh3cDot3OmpEmulationType,
       "hh3cDot3OmpEmulationStatTable": hh3cDot3OmpEmulationStatTable,
       "hh3cDot3OmpEmulationStatEntry": hh3cDot3OmpEmulationStatEntry,
       "hh3cDot3OmpEmulationSLDErrors": hh3cDot3OmpEmulationSLDErrors,
       "hh3cDot3OmpEmulationCRC8Errors": hh3cDot3OmpEmulationCRC8Errors,
       "hh3cDot3OmpEmulationBadLLID": hh3cDot3OmpEmulationBadLLID,
       "hh3cDot3OmpEmulationGoodLLID": hh3cDot3OmpEmulationGoodLLID,
       "hh3cDot3OmpEmulationOnuPonCastLLID": hh3cDot3OmpEmulationOnuPonCastLLID,
       "hh3cDot3OmpEmulationOltPonCastLLID": hh3cDot3OmpEmulationOltPonCastLLID,
       "hh3cDot3OmpEmulationBroadcastLLIDNotOnuID": hh3cDot3OmpEmulationBroadcastLLIDNotOnuID,
       "hh3cDot3OmpEmulationOnuLLIDNotBroadcast": hh3cDot3OmpEmulationOnuLLIDNotBroadcast,
       "hh3cDot3OmpEmulationBroadcastLLIDPlusOnuId": hh3cDot3OmpEmulationBroadcastLLIDPlusOnuId,
       "hh3cDot3OmpEmulationNotBroadcastLLIDNotOnuId": hh3cDot3OmpEmulationNotBroadcastLLIDNotOnuId,
       "hh3cDot3OmpeConformance": hh3cDot3OmpeConformance,
       "hh3cDot3OmpeGroups": hh3cDot3OmpeGroups,
       "hh3cDot3OmpeGroupID": hh3cDot3OmpeGroupID,
       "hh3cDot3OmpeGroupStat": hh3cDot3OmpeGroupStat,
       "hh3cDot3OmpeCompliances": hh3cDot3OmpeCompliances,
       "hh3cDot3OmpeCompliance": hh3cDot3OmpeCompliance,
       "hh3cDot3EponMauMIB": hh3cDot3EponMauMIB,
       "hh3cDot3EponMauObjects": hh3cDot3EponMauObjects,
       "hh3cDot3EponMauTable": hh3cDot3EponMauTable,
       "hh3cDot3EponMauEntry": hh3cDot3EponMauEntry,
       "hh3cDot3EponMauPCSCodingViolation": hh3cDot3EponMauPCSCodingViolation,
       "hh3cDot3EponMauFecAbility": hh3cDot3EponMauFecAbility,
       "hh3cDot3EponMauFecMode": hh3cDot3EponMauFecMode,
       "hh3cDot3EponMauFECCorrectedBlocks": hh3cDot3EponMauFECCorrectedBlocks,
       "hh3cDot3EponMauFECUncorrectableBlocks": hh3cDot3EponMauFECUncorrectableBlocks,
       "hh3cDot3EponMauBufferHeadCodingViolation": hh3cDot3EponMauBufferHeadCodingViolation,
       "hh3cDot3EponMauConformance": hh3cDot3EponMauConformance,
       "hh3cDot3EponMauGroups": hh3cDot3EponMauGroups,
       "hh3cDot3EponMauGroupAll": hh3cDot3EponMauGroupAll,
       "hh3cDot3EponMauGroupFEC": hh3cDot3EponMauGroupFEC,
       "hh3cDot3EponMauCompliances": hh3cDot3EponMauCompliances,
       "hh3cDot3EponMauCompliance": hh3cDot3EponMauCompliance,
       "hh3cDot3EponMauType": hh3cDot3EponMauType,
       "hh3cEponMauType1000BasePXOLT": hh3cEponMauType1000BasePXOLT,
       "hh3cEponMauType1000BasePXONU": hh3cEponMauType1000BasePXONU,
       "hh3cEponMauType1000BasePX10DOLT": hh3cEponMauType1000BasePX10DOLT,
       "hh3cEponMauType1000BasePX10DONU": hh3cEponMauType1000BasePX10DONU,
       "hh3cEponMauType1000BasePX10UOLT": hh3cEponMauType1000BasePX10UOLT,
       "hh3cEponMauType1000BasePX10UONU": hh3cEponMauType1000BasePX10UONU,
       "hh3cEponMauType1000BasePX20DOLT": hh3cEponMauType1000BasePX20DOLT,
       "hh3cEponMauType1000BasePX20DONU": hh3cEponMauType1000BasePX20DONU,
       "hh3cEponMauType1000BasePX20UOLT": hh3cEponMauType1000BasePX20UOLT,
       "hh3cEponMauType1000BasePX20UONU": hh3cEponMauType1000BasePX20UONU}
)
