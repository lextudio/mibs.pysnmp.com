# SNMP MIB module (HPN-ICF-DOT3-EFM-EPON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-DOT3-EFM-EPON-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:59:58 2024
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

(hpnicfEpon,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfEpon")

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

hpnicfDot3EfmeponMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2)
)
hpnicfDot3EfmeponMIB.setRevisions(
        ("2004-09-21 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpnicfDot3MpcpMIB_ObjectIdentity = ObjectIdentity
hpnicfDot3MpcpMIB = _HpnicfDot3MpcpMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 1)
)
_HpnicfDot3MpcpObjects_ObjectIdentity = ObjectIdentity
hpnicfDot3MpcpObjects = _HpnicfDot3MpcpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 1, 1)
)
_HpnicfDot3MpcpTable_Object = MibTable
hpnicfDot3MpcpTable = _HpnicfDot3MpcpTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hpnicfDot3MpcpTable.setStatus("current")
_HpnicfDot3MpcpEntry_Object = MibTableRow
hpnicfDot3MpcpEntry = _HpnicfDot3MpcpEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 1, 1, 1, 1)
)
hpnicfDot3MpcpEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpnicfDot3MpcpEntry.setStatus("current")
_HpnicfDot3MpcpID_Type = Integer32
_HpnicfDot3MpcpID_Object = MibTableColumn
hpnicfDot3MpcpID = _HpnicfDot3MpcpID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 1, 1, 1, 1, 1),
    _HpnicfDot3MpcpID_Type()
)
hpnicfDot3MpcpID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot3MpcpID.setStatus("current")
_HpnicfDot3MpcpOperStatus_Type = TruthValue
_HpnicfDot3MpcpOperStatus_Object = MibTableColumn
hpnicfDot3MpcpOperStatus = _HpnicfDot3MpcpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 1, 1, 1, 1, 2),
    _HpnicfDot3MpcpOperStatus_Type()
)
hpnicfDot3MpcpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot3MpcpOperStatus.setStatus("current")


class _HpnicfDot3MpcpMode_Type(Integer32):
    """Custom type hpnicfDot3MpcpMode based on Integer32"""
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


_HpnicfDot3MpcpMode_Type.__name__ = "Integer32"
_HpnicfDot3MpcpMode_Object = MibTableColumn
hpnicfDot3MpcpMode = _HpnicfDot3MpcpMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 1, 1, 1, 1, 3),
    _HpnicfDot3MpcpMode_Type()
)
hpnicfDot3MpcpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot3MpcpMode.setStatus("current")
_HpnicfDot3MpcpLinkID_Type = Integer32
_HpnicfDot3MpcpLinkID_Object = MibTableColumn
hpnicfDot3MpcpLinkID = _HpnicfDot3MpcpLinkID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 1, 1, 1, 1, 4),
    _HpnicfDot3MpcpLinkID_Type()
)
hpnicfDot3MpcpLinkID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot3MpcpLinkID.setStatus("current")
_HpnicfDot3MpcpRemoteMACAddress_Type = MacAddress
_HpnicfDot3MpcpRemoteMACAddress_Object = MibTableColumn
hpnicfDot3MpcpRemoteMACAddress = _HpnicfDot3MpcpRemoteMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 1, 1, 1, 1, 5),
    _HpnicfDot3MpcpRemoteMACAddress_Type()
)
hpnicfDot3MpcpRemoteMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot3MpcpRemoteMACAddress.setStatus("current")


class _HpnicfDot3MpcpRegistrationState_Type(Integer32):
    """Custom type hpnicfDot3MpcpRegistrationState based on Integer32"""
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


_HpnicfDot3MpcpRegistrationState_Type.__name__ = "Integer32"
_HpnicfDot3MpcpRegistrationState_Object = MibTableColumn
hpnicfDot3MpcpRegistrationState = _HpnicfDot3MpcpRegistrationState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 1, 1, 1, 1, 6),
    _HpnicfDot3MpcpRegistrationState_Type()
)
hpnicfDot3MpcpRegistrationState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot3MpcpRegistrationState.setStatus("current")
_HpnicfDot3MpcpTransmitElapsed_Type = Integer32
_HpnicfDot3MpcpTransmitElapsed_Object = MibTableColumn
hpnicfDot3MpcpTransmitElapsed = _HpnicfDot3MpcpTransmitElapsed_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 1, 1, 1, 1, 7),
    _HpnicfDot3MpcpTransmitElapsed_Type()
)
hpnicfDot3MpcpTransmitElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot3MpcpTransmitElapsed.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot3MpcpTransmitElapsed.setUnits("TQ (16nsec)")
_HpnicfDot3MpcpReceiveElapsed_Type = Integer32
_HpnicfDot3MpcpReceiveElapsed_Object = MibTableColumn
hpnicfDot3MpcpReceiveElapsed = _HpnicfDot3MpcpReceiveElapsed_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 1, 1, 1, 1, 8),
    _HpnicfDot3MpcpReceiveElapsed_Type()
)
hpnicfDot3MpcpReceiveElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot3MpcpReceiveElapsed.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot3MpcpReceiveElapsed.setUnits("TQ (16nsec)")
_HpnicfDot3MpcpRoundTripTime_Type = Integer32
_HpnicfDot3MpcpRoundTripTime_Object = MibTableColumn
hpnicfDot3MpcpRoundTripTime = _HpnicfDot3MpcpRoundTripTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 1, 1, 1, 1, 9),
    _HpnicfDot3MpcpRoundTripTime_Type()
)
hpnicfDot3MpcpRoundTripTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot3MpcpRoundTripTime.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot3MpcpRoundTripTime.setUnits("TQ (16nsec)")


class _HpnicfDot3MpcpMaximumPendingGrants_Type(Integer32):
    """Custom type hpnicfDot3MpcpMaximumPendingGrants based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpnicfDot3MpcpMaximumPendingGrants_Type.__name__ = "Integer32"
_HpnicfDot3MpcpMaximumPendingGrants_Object = MibTableColumn
hpnicfDot3MpcpMaximumPendingGrants = _HpnicfDot3MpcpMaximumPendingGrants_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 1, 1, 1, 1, 10),
    _HpnicfDot3MpcpMaximumPendingGrants_Type()
)
hpnicfDot3MpcpMaximumPendingGrants.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot3MpcpMaximumPendingGrants.setStatus("current")


class _HpnicfDot3MpcpAdminState_Type(TruthValue):
    """Custom type hpnicfDot3MpcpAdminState based on TruthValue"""


_HpnicfDot3MpcpAdminState_Object = MibTableColumn
hpnicfDot3MpcpAdminState = _HpnicfDot3MpcpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 1, 1, 1, 1, 11),
    _HpnicfDot3MpcpAdminState_Type()
)
hpnicfDot3MpcpAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot3MpcpAdminState.setStatus("current")
_HpnicfDot3MpcpOnTime_Type = Integer32
_HpnicfDot3MpcpOnTime_Object = MibTableColumn
hpnicfDot3MpcpOnTime = _HpnicfDot3MpcpOnTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 1, 1, 1, 1, 12),
    _HpnicfDot3MpcpOnTime_Type()
)
hpnicfDot3MpcpOnTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot3MpcpOnTime.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot3MpcpOnTime.setUnits("TQ (16nsec)")
_HpnicfDot3MpcpOffTime_Type = Integer32
_HpnicfDot3MpcpOffTime_Object = MibTableColumn
hpnicfDot3MpcpOffTime = _HpnicfDot3MpcpOffTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 1, 1, 1, 1, 13),
    _HpnicfDot3MpcpOffTime_Type()
)
hpnicfDot3MpcpOffTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot3MpcpOffTime.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot3MpcpOffTime.setUnits("TQ (16nsec)")
_HpnicfDot3MpcpSyncTime_Type = Integer32
_HpnicfDot3MpcpSyncTime_Object = MibTableColumn
hpnicfDot3MpcpSyncTime = _HpnicfDot3MpcpSyncTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 1, 1, 1, 1, 14),
    _HpnicfDot3MpcpSyncTime_Type()
)
hpnicfDot3MpcpSyncTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot3MpcpSyncTime.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot3MpcpSyncTime.setUnits("TQ (16nsec)")
_HpnicfDot3MpcpStatTable_Object = MibTable
hpnicfDot3MpcpStatTable = _HpnicfDot3MpcpStatTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 1, 1, 2)
)
if mibBuilder.loadTexts:
    hpnicfDot3MpcpStatTable.setStatus("current")
_HpnicfDot3MpcpStatEntry_Object = MibTableRow
hpnicfDot3MpcpStatEntry = _HpnicfDot3MpcpStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 1, 1, 2, 1)
)
hpnicfDot3MpcpStatEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpnicfDot3MpcpStatEntry.setStatus("current")
_HpnicfDot3MpcpMACCtrlFramesTransmitted_Type = Counter32
_HpnicfDot3MpcpMACCtrlFramesTransmitted_Object = MibTableColumn
hpnicfDot3MpcpMACCtrlFramesTransmitted = _HpnicfDot3MpcpMACCtrlFramesTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 1, 1, 2, 1, 1),
    _HpnicfDot3MpcpMACCtrlFramesTransmitted_Type()
)
hpnicfDot3MpcpMACCtrlFramesTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot3MpcpMACCtrlFramesTransmitted.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot3MpcpMACCtrlFramesTransmitted.setUnits("frames")
_HpnicfDot3MpcpMACCtrlFramesReceived_Type = Counter32
_HpnicfDot3MpcpMACCtrlFramesReceived_Object = MibTableColumn
hpnicfDot3MpcpMACCtrlFramesReceived = _HpnicfDot3MpcpMACCtrlFramesReceived_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 1, 1, 2, 1, 2),
    _HpnicfDot3MpcpMACCtrlFramesReceived_Type()
)
hpnicfDot3MpcpMACCtrlFramesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot3MpcpMACCtrlFramesReceived.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot3MpcpMACCtrlFramesReceived.setUnits("frames")
_HpnicfDot3MpcpDiscoveryWindowsSent_Type = Counter32
_HpnicfDot3MpcpDiscoveryWindowsSent_Object = MibTableColumn
hpnicfDot3MpcpDiscoveryWindowsSent = _HpnicfDot3MpcpDiscoveryWindowsSent_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 1, 1, 2, 1, 3),
    _HpnicfDot3MpcpDiscoveryWindowsSent_Type()
)
hpnicfDot3MpcpDiscoveryWindowsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot3MpcpDiscoveryWindowsSent.setStatus("current")
_HpnicfDot3MpcpDiscoveryTimeout_Type = Counter32
_HpnicfDot3MpcpDiscoveryTimeout_Object = MibTableColumn
hpnicfDot3MpcpDiscoveryTimeout = _HpnicfDot3MpcpDiscoveryTimeout_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 1, 1, 2, 1, 4),
    _HpnicfDot3MpcpDiscoveryTimeout_Type()
)
hpnicfDot3MpcpDiscoveryTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot3MpcpDiscoveryTimeout.setStatus("current")
_HpnicfDot3MpcpTxRegRequest_Type = Counter32
_HpnicfDot3MpcpTxRegRequest_Object = MibTableColumn
hpnicfDot3MpcpTxRegRequest = _HpnicfDot3MpcpTxRegRequest_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 1, 1, 2, 1, 5),
    _HpnicfDot3MpcpTxRegRequest_Type()
)
hpnicfDot3MpcpTxRegRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot3MpcpTxRegRequest.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot3MpcpTxRegRequest.setUnits("frames")
_HpnicfDot3MpcpRxRegRequest_Type = Counter32
_HpnicfDot3MpcpRxRegRequest_Object = MibTableColumn
hpnicfDot3MpcpRxRegRequest = _HpnicfDot3MpcpRxRegRequest_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 1, 1, 2, 1, 6),
    _HpnicfDot3MpcpRxRegRequest_Type()
)
hpnicfDot3MpcpRxRegRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot3MpcpRxRegRequest.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot3MpcpRxRegRequest.setUnits("frames")
_HpnicfDot3MpcpTxRegAck_Type = Counter32
_HpnicfDot3MpcpTxRegAck_Object = MibTableColumn
hpnicfDot3MpcpTxRegAck = _HpnicfDot3MpcpTxRegAck_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 1, 1, 2, 1, 7),
    _HpnicfDot3MpcpTxRegAck_Type()
)
hpnicfDot3MpcpTxRegAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot3MpcpTxRegAck.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot3MpcpTxRegAck.setUnits("frames")
_HpnicfDot3MpcpRxRegAck_Type = Counter32
_HpnicfDot3MpcpRxRegAck_Object = MibTableColumn
hpnicfDot3MpcpRxRegAck = _HpnicfDot3MpcpRxRegAck_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 1, 1, 2, 1, 8),
    _HpnicfDot3MpcpRxRegAck_Type()
)
hpnicfDot3MpcpRxRegAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot3MpcpRxRegAck.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot3MpcpRxRegAck.setUnits("frames")
_HpnicfDot3MpcpTxReport_Type = Counter32
_HpnicfDot3MpcpTxReport_Object = MibTableColumn
hpnicfDot3MpcpTxReport = _HpnicfDot3MpcpTxReport_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 1, 1, 2, 1, 9),
    _HpnicfDot3MpcpTxReport_Type()
)
hpnicfDot3MpcpTxReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot3MpcpTxReport.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot3MpcpTxReport.setUnits("frames")
_HpnicfDot3MpcpRxReport_Type = Counter32
_HpnicfDot3MpcpRxReport_Object = MibTableColumn
hpnicfDot3MpcpRxReport = _HpnicfDot3MpcpRxReport_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 1, 1, 2, 1, 10),
    _HpnicfDot3MpcpRxReport_Type()
)
hpnicfDot3MpcpRxReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot3MpcpRxReport.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot3MpcpRxReport.setUnits("frames")
_HpnicfDot3MpcpTxGate_Type = Counter32
_HpnicfDot3MpcpTxGate_Object = MibTableColumn
hpnicfDot3MpcpTxGate = _HpnicfDot3MpcpTxGate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 1, 1, 2, 1, 11),
    _HpnicfDot3MpcpTxGate_Type()
)
hpnicfDot3MpcpTxGate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot3MpcpTxGate.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot3MpcpTxGate.setUnits("frames")
_HpnicfDot3MpcpRxGate_Type = Counter32
_HpnicfDot3MpcpRxGate_Object = MibTableColumn
hpnicfDot3MpcpRxGate = _HpnicfDot3MpcpRxGate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 1, 1, 2, 1, 12),
    _HpnicfDot3MpcpRxGate_Type()
)
hpnicfDot3MpcpRxGate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot3MpcpRxGate.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot3MpcpRxGate.setUnits("frames")
_HpnicfDot3MpcpTxRegister_Type = Counter32
_HpnicfDot3MpcpTxRegister_Object = MibTableColumn
hpnicfDot3MpcpTxRegister = _HpnicfDot3MpcpTxRegister_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 1, 1, 2, 1, 13),
    _HpnicfDot3MpcpTxRegister_Type()
)
hpnicfDot3MpcpTxRegister.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot3MpcpTxRegister.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot3MpcpTxRegister.setUnits("frames")
_HpnicfDot3MpcpRxRegister_Type = Counter32
_HpnicfDot3MpcpRxRegister_Object = MibTableColumn
hpnicfDot3MpcpRxRegister = _HpnicfDot3MpcpRxRegister_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 1, 1, 2, 1, 14),
    _HpnicfDot3MpcpRxRegister_Type()
)
hpnicfDot3MpcpRxRegister.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot3MpcpRxRegister.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot3MpcpRxRegister.setUnits("frames")
_HpnicfDot3MpcpRxNotSupportedMPCP_Type = Counter32
_HpnicfDot3MpcpRxNotSupportedMPCP_Object = MibTableColumn
hpnicfDot3MpcpRxNotSupportedMPCP = _HpnicfDot3MpcpRxNotSupportedMPCP_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 1, 1, 2, 1, 15),
    _HpnicfDot3MpcpRxNotSupportedMPCP_Type()
)
hpnicfDot3MpcpRxNotSupportedMPCP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot3MpcpRxNotSupportedMPCP.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot3MpcpRxNotSupportedMPCP.setUnits("frames")
_HpnicfDot3MpcpConformance_ObjectIdentity = ObjectIdentity
hpnicfDot3MpcpConformance = _HpnicfDot3MpcpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 1, 2)
)
_HpnicfDot3MpcpGroups_ObjectIdentity = ObjectIdentity
hpnicfDot3MpcpGroups = _HpnicfDot3MpcpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 1, 2, 1)
)
_HpnicfDot3MpcpCompliances_ObjectIdentity = ObjectIdentity
hpnicfDot3MpcpCompliances = _HpnicfDot3MpcpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 1, 2, 2)
)
_HpnicfDot3OmpEmulationMIB_ObjectIdentity = ObjectIdentity
hpnicfDot3OmpEmulationMIB = _HpnicfDot3OmpEmulationMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 2)
)
_HpnicfDot3OmpEmulationObjects_ObjectIdentity = ObjectIdentity
hpnicfDot3OmpEmulationObjects = _HpnicfDot3OmpEmulationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 2, 1)
)
_HpnicfDot3OmpEmulationTable_Object = MibTable
hpnicfDot3OmpEmulationTable = _HpnicfDot3OmpEmulationTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hpnicfDot3OmpEmulationTable.setStatus("current")
_HpnicfDot3OmpEmulationEntry_Object = MibTableRow
hpnicfDot3OmpEmulationEntry = _HpnicfDot3OmpEmulationEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 2, 1, 1, 1)
)
hpnicfDot3OmpEmulationEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpnicfDot3OmpEmulationEntry.setStatus("current")
_HpnicfDot3OmpEmulationID_Type = Integer32
_HpnicfDot3OmpEmulationID_Object = MibTableColumn
hpnicfDot3OmpEmulationID = _HpnicfDot3OmpEmulationID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 2, 1, 1, 1, 1),
    _HpnicfDot3OmpEmulationID_Type()
)
hpnicfDot3OmpEmulationID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot3OmpEmulationID.setStatus("current")


class _HpnicfDot3OmpEmulationType_Type(Integer32):
    """Custom type hpnicfDot3OmpEmulationType based on Integer32"""
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


_HpnicfDot3OmpEmulationType_Type.__name__ = "Integer32"
_HpnicfDot3OmpEmulationType_Object = MibTableColumn
hpnicfDot3OmpEmulationType = _HpnicfDot3OmpEmulationType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 2, 1, 1, 1, 2),
    _HpnicfDot3OmpEmulationType_Type()
)
hpnicfDot3OmpEmulationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot3OmpEmulationType.setStatus("current")
_HpnicfDot3OmpEmulationStatTable_Object = MibTable
hpnicfDot3OmpEmulationStatTable = _HpnicfDot3OmpEmulationStatTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 2, 1, 2)
)
if mibBuilder.loadTexts:
    hpnicfDot3OmpEmulationStatTable.setStatus("current")
_HpnicfDot3OmpEmulationStatEntry_Object = MibTableRow
hpnicfDot3OmpEmulationStatEntry = _HpnicfDot3OmpEmulationStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 2, 1, 2, 1)
)
hpnicfDot3OmpEmulationStatEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpnicfDot3OmpEmulationStatEntry.setStatus("current")
_HpnicfDot3OmpEmulationSLDErrors_Type = Counter32
_HpnicfDot3OmpEmulationSLDErrors_Object = MibTableColumn
hpnicfDot3OmpEmulationSLDErrors = _HpnicfDot3OmpEmulationSLDErrors_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 2, 1, 2, 1, 1),
    _HpnicfDot3OmpEmulationSLDErrors_Type()
)
hpnicfDot3OmpEmulationSLDErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot3OmpEmulationSLDErrors.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot3OmpEmulationSLDErrors.setUnits("frames")
_HpnicfDot3OmpEmulationCRC8Errors_Type = Counter32
_HpnicfDot3OmpEmulationCRC8Errors_Object = MibTableColumn
hpnicfDot3OmpEmulationCRC8Errors = _HpnicfDot3OmpEmulationCRC8Errors_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 2, 1, 2, 1, 2),
    _HpnicfDot3OmpEmulationCRC8Errors_Type()
)
hpnicfDot3OmpEmulationCRC8Errors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot3OmpEmulationCRC8Errors.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot3OmpEmulationCRC8Errors.setUnits("frames")
_HpnicfDot3OmpEmulationBadLLID_Type = Counter32
_HpnicfDot3OmpEmulationBadLLID_Object = MibTableColumn
hpnicfDot3OmpEmulationBadLLID = _HpnicfDot3OmpEmulationBadLLID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 2, 1, 2, 1, 3),
    _HpnicfDot3OmpEmulationBadLLID_Type()
)
hpnicfDot3OmpEmulationBadLLID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot3OmpEmulationBadLLID.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot3OmpEmulationBadLLID.setUnits("frames")
_HpnicfDot3OmpEmulationGoodLLID_Type = Counter32
_HpnicfDot3OmpEmulationGoodLLID_Object = MibTableColumn
hpnicfDot3OmpEmulationGoodLLID = _HpnicfDot3OmpEmulationGoodLLID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 2, 1, 2, 1, 4),
    _HpnicfDot3OmpEmulationGoodLLID_Type()
)
hpnicfDot3OmpEmulationGoodLLID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot3OmpEmulationGoodLLID.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot3OmpEmulationGoodLLID.setUnits("frames")
_HpnicfDot3OmpEmulationOnuPonCastLLID_Type = Counter32
_HpnicfDot3OmpEmulationOnuPonCastLLID_Object = MibTableColumn
hpnicfDot3OmpEmulationOnuPonCastLLID = _HpnicfDot3OmpEmulationOnuPonCastLLID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 2, 1, 2, 1, 5),
    _HpnicfDot3OmpEmulationOnuPonCastLLID_Type()
)
hpnicfDot3OmpEmulationOnuPonCastLLID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot3OmpEmulationOnuPonCastLLID.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot3OmpEmulationOnuPonCastLLID.setUnits("frames")
_HpnicfDot3OmpEmulationOltPonCastLLID_Type = Counter32
_HpnicfDot3OmpEmulationOltPonCastLLID_Object = MibTableColumn
hpnicfDot3OmpEmulationOltPonCastLLID = _HpnicfDot3OmpEmulationOltPonCastLLID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 2, 1, 2, 1, 6),
    _HpnicfDot3OmpEmulationOltPonCastLLID_Type()
)
hpnicfDot3OmpEmulationOltPonCastLLID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot3OmpEmulationOltPonCastLLID.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot3OmpEmulationOltPonCastLLID.setUnits("frames")
_HpnicfDot3OmpEmulationBroadcastLLIDNotOnuID_Type = Counter32
_HpnicfDot3OmpEmulationBroadcastLLIDNotOnuID_Object = MibTableColumn
hpnicfDot3OmpEmulationBroadcastLLIDNotOnuID = _HpnicfDot3OmpEmulationBroadcastLLIDNotOnuID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 2, 1, 2, 1, 7),
    _HpnicfDot3OmpEmulationBroadcastLLIDNotOnuID_Type()
)
hpnicfDot3OmpEmulationBroadcastLLIDNotOnuID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot3OmpEmulationBroadcastLLIDNotOnuID.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot3OmpEmulationBroadcastLLIDNotOnuID.setUnits("frames")
_HpnicfDot3OmpEmulationOnuLLIDNotBroadcast_Type = Counter32
_HpnicfDot3OmpEmulationOnuLLIDNotBroadcast_Object = MibTableColumn
hpnicfDot3OmpEmulationOnuLLIDNotBroadcast = _HpnicfDot3OmpEmulationOnuLLIDNotBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 2, 1, 2, 1, 8),
    _HpnicfDot3OmpEmulationOnuLLIDNotBroadcast_Type()
)
hpnicfDot3OmpEmulationOnuLLIDNotBroadcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot3OmpEmulationOnuLLIDNotBroadcast.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot3OmpEmulationOnuLLIDNotBroadcast.setUnits("frames")
_HpnicfDot3OmpEmulationBroadcastLLIDPlusOnuId_Type = Counter32
_HpnicfDot3OmpEmulationBroadcastLLIDPlusOnuId_Object = MibTableColumn
hpnicfDot3OmpEmulationBroadcastLLIDPlusOnuId = _HpnicfDot3OmpEmulationBroadcastLLIDPlusOnuId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 2, 1, 2, 1, 9),
    _HpnicfDot3OmpEmulationBroadcastLLIDPlusOnuId_Type()
)
hpnicfDot3OmpEmulationBroadcastLLIDPlusOnuId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot3OmpEmulationBroadcastLLIDPlusOnuId.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot3OmpEmulationBroadcastLLIDPlusOnuId.setUnits("frames")
_HpnicfDot3OmpEmulationNotBroadcastLLIDNotOnuId_Type = Counter32
_HpnicfDot3OmpEmulationNotBroadcastLLIDNotOnuId_Object = MibTableColumn
hpnicfDot3OmpEmulationNotBroadcastLLIDNotOnuId = _HpnicfDot3OmpEmulationNotBroadcastLLIDNotOnuId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 2, 1, 2, 1, 10),
    _HpnicfDot3OmpEmulationNotBroadcastLLIDNotOnuId_Type()
)
hpnicfDot3OmpEmulationNotBroadcastLLIDNotOnuId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot3OmpEmulationNotBroadcastLLIDNotOnuId.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot3OmpEmulationNotBroadcastLLIDNotOnuId.setUnits("frames")
_HpnicfDot3OmpeConformance_ObjectIdentity = ObjectIdentity
hpnicfDot3OmpeConformance = _HpnicfDot3OmpeConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 2, 2)
)
_HpnicfDot3OmpeGroups_ObjectIdentity = ObjectIdentity
hpnicfDot3OmpeGroups = _HpnicfDot3OmpeGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 2, 2, 1)
)
_HpnicfDot3OmpeCompliances_ObjectIdentity = ObjectIdentity
hpnicfDot3OmpeCompliances = _HpnicfDot3OmpeCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 2, 2, 2)
)
_HpnicfDot3EponMauMIB_ObjectIdentity = ObjectIdentity
hpnicfDot3EponMauMIB = _HpnicfDot3EponMauMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 3)
)
_HpnicfDot3EponMauObjects_ObjectIdentity = ObjectIdentity
hpnicfDot3EponMauObjects = _HpnicfDot3EponMauObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 3, 1)
)
_HpnicfDot3EponMauTable_Object = MibTable
hpnicfDot3EponMauTable = _HpnicfDot3EponMauTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 3, 1, 1)
)
if mibBuilder.loadTexts:
    hpnicfDot3EponMauTable.setStatus("current")
_HpnicfDot3EponMauEntry_Object = MibTableRow
hpnicfDot3EponMauEntry = _HpnicfDot3EponMauEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 3, 1, 1, 1)
)
hpnicfDot3EponMauEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpnicfDot3EponMauEntry.setStatus("current")
_HpnicfDot3EponMauPCSCodingViolation_Type = Counter32
_HpnicfDot3EponMauPCSCodingViolation_Object = MibTableColumn
hpnicfDot3EponMauPCSCodingViolation = _HpnicfDot3EponMauPCSCodingViolation_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 3, 1, 1, 1, 1),
    _HpnicfDot3EponMauPCSCodingViolation_Type()
)
hpnicfDot3EponMauPCSCodingViolation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot3EponMauPCSCodingViolation.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot3EponMauPCSCodingViolation.setUnits("octets")


class _HpnicfDot3EponMauFecAbility_Type(Integer32):
    """Custom type hpnicfDot3EponMauFecAbility based on Integer32"""
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


_HpnicfDot3EponMauFecAbility_Type.__name__ = "Integer32"
_HpnicfDot3EponMauFecAbility_Object = MibTableColumn
hpnicfDot3EponMauFecAbility = _HpnicfDot3EponMauFecAbility_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 3, 1, 1, 1, 2),
    _HpnicfDot3EponMauFecAbility_Type()
)
hpnicfDot3EponMauFecAbility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot3EponMauFecAbility.setStatus("current")


class _HpnicfDot3EponMauFecMode_Type(Integer32):
    """Custom type hpnicfDot3EponMauFecMode based on Integer32"""
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


_HpnicfDot3EponMauFecMode_Type.__name__ = "Integer32"
_HpnicfDot3EponMauFecMode_Object = MibTableColumn
hpnicfDot3EponMauFecMode = _HpnicfDot3EponMauFecMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 3, 1, 1, 1, 3),
    _HpnicfDot3EponMauFecMode_Type()
)
hpnicfDot3EponMauFecMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot3EponMauFecMode.setStatus("current")
_HpnicfDot3EponMauFECCorrectedBlocks_Type = Counter32
_HpnicfDot3EponMauFECCorrectedBlocks_Object = MibTableColumn
hpnicfDot3EponMauFECCorrectedBlocks = _HpnicfDot3EponMauFECCorrectedBlocks_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 3, 1, 1, 1, 4),
    _HpnicfDot3EponMauFECCorrectedBlocks_Type()
)
hpnicfDot3EponMauFECCorrectedBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot3EponMauFECCorrectedBlocks.setStatus("current")
_HpnicfDot3EponMauFECUncorrectableBlocks_Type = Counter32
_HpnicfDot3EponMauFECUncorrectableBlocks_Object = MibTableColumn
hpnicfDot3EponMauFECUncorrectableBlocks = _HpnicfDot3EponMauFECUncorrectableBlocks_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 3, 1, 1, 1, 5),
    _HpnicfDot3EponMauFECUncorrectableBlocks_Type()
)
hpnicfDot3EponMauFECUncorrectableBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot3EponMauFECUncorrectableBlocks.setStatus("current")
_HpnicfDot3EponMauBufferHeadCodingViolation_Type = Counter32
_HpnicfDot3EponMauBufferHeadCodingViolation_Object = MibTableColumn
hpnicfDot3EponMauBufferHeadCodingViolation = _HpnicfDot3EponMauBufferHeadCodingViolation_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 3, 1, 1, 1, 6),
    _HpnicfDot3EponMauBufferHeadCodingViolation_Type()
)
hpnicfDot3EponMauBufferHeadCodingViolation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot3EponMauBufferHeadCodingViolation.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot3EponMauBufferHeadCodingViolation.setUnits("octets")
_HpnicfDot3EponMauConformance_ObjectIdentity = ObjectIdentity
hpnicfDot3EponMauConformance = _HpnicfDot3EponMauConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 3, 2)
)
_HpnicfDot3EponMauGroups_ObjectIdentity = ObjectIdentity
hpnicfDot3EponMauGroups = _HpnicfDot3EponMauGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 3, 2, 1)
)
_HpnicfDot3EponMauCompliances_ObjectIdentity = ObjectIdentity
hpnicfDot3EponMauCompliances = _HpnicfDot3EponMauCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 3, 2, 2)
)
_HpnicfDot3EponMauType_ObjectIdentity = ObjectIdentity
hpnicfDot3EponMauType = _HpnicfDot3EponMauType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 3, 3)
)
_HpnicfEponMauType1000BasePXOLT_ObjectIdentity = ObjectIdentity
hpnicfEponMauType1000BasePXOLT = _HpnicfEponMauType1000BasePXOLT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 3, 3, 1)
)
if mibBuilder.loadTexts:
    hpnicfEponMauType1000BasePXOLT.setStatus("current")
_HpnicfEponMauType1000BasePXONU_ObjectIdentity = ObjectIdentity
hpnicfEponMauType1000BasePXONU = _HpnicfEponMauType1000BasePXONU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 3, 3, 2)
)
if mibBuilder.loadTexts:
    hpnicfEponMauType1000BasePXONU.setStatus("current")
_HpnicfEponMauType1000BasePX10DOLT_ObjectIdentity = ObjectIdentity
hpnicfEponMauType1000BasePX10DOLT = _HpnicfEponMauType1000BasePX10DOLT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 3, 3, 3)
)
if mibBuilder.loadTexts:
    hpnicfEponMauType1000BasePX10DOLT.setStatus("current")
_HpnicfEponMauType1000BasePX10DONU_ObjectIdentity = ObjectIdentity
hpnicfEponMauType1000BasePX10DONU = _HpnicfEponMauType1000BasePX10DONU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 3, 3, 4)
)
if mibBuilder.loadTexts:
    hpnicfEponMauType1000BasePX10DONU.setStatus("current")
_HpnicfEponMauType1000BasePX10UOLT_ObjectIdentity = ObjectIdentity
hpnicfEponMauType1000BasePX10UOLT = _HpnicfEponMauType1000BasePX10UOLT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 3, 3, 5)
)
if mibBuilder.loadTexts:
    hpnicfEponMauType1000BasePX10UOLT.setStatus("current")
_HpnicfEponMauType1000BasePX10UONU_ObjectIdentity = ObjectIdentity
hpnicfEponMauType1000BasePX10UONU = _HpnicfEponMauType1000BasePX10UONU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 3, 3, 6)
)
if mibBuilder.loadTexts:
    hpnicfEponMauType1000BasePX10UONU.setStatus("current")
_HpnicfEponMauType1000BasePX20DOLT_ObjectIdentity = ObjectIdentity
hpnicfEponMauType1000BasePX20DOLT = _HpnicfEponMauType1000BasePX20DOLT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 3, 3, 7)
)
if mibBuilder.loadTexts:
    hpnicfEponMauType1000BasePX20DOLT.setStatus("current")
_HpnicfEponMauType1000BasePX20DONU_ObjectIdentity = ObjectIdentity
hpnicfEponMauType1000BasePX20DONU = _HpnicfEponMauType1000BasePX20DONU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 3, 3, 8)
)
if mibBuilder.loadTexts:
    hpnicfEponMauType1000BasePX20DONU.setStatus("current")
_HpnicfEponMauType1000BasePX20UOLT_ObjectIdentity = ObjectIdentity
hpnicfEponMauType1000BasePX20UOLT = _HpnicfEponMauType1000BasePX20UOLT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 3, 3, 9)
)
if mibBuilder.loadTexts:
    hpnicfEponMauType1000BasePX20UOLT.setStatus("current")
_HpnicfEponMauType1000BasePX20UONU_ObjectIdentity = ObjectIdentity
hpnicfEponMauType1000BasePX20UONU = _HpnicfEponMauType1000BasePX20UONU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 3, 3, 10)
)
if mibBuilder.loadTexts:
    hpnicfEponMauType1000BasePX20UONU.setStatus("current")

# Managed Objects groups

hpnicfDot3MpcpGroupBase = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 1, 2, 1, 1)
)
hpnicfDot3MpcpGroupBase.setObjects(
      *(("HPN-ICF-DOT3-EFM-EPON-MIB", "hpnicfDot3MpcpID"),
        ("HPN-ICF-DOT3-EFM-EPON-MIB", "hpnicfDot3MpcpOperStatus"),
        ("HPN-ICF-DOT3-EFM-EPON-MIB", "hpnicfDot3MpcpMode"),
        ("HPN-ICF-DOT3-EFM-EPON-MIB", "hpnicfDot3MpcpLinkID"),
        ("HPN-ICF-DOT3-EFM-EPON-MIB", "hpnicfDot3MpcpRemoteMACAddress"),
        ("HPN-ICF-DOT3-EFM-EPON-MIB", "hpnicfDot3MpcpRegistrationState"),
        ("HPN-ICF-DOT3-EFM-EPON-MIB", "hpnicfDot3MpcpMaximumPendingGrants"),
        ("HPN-ICF-DOT3-EFM-EPON-MIB", "hpnicfDot3MpcpAdminState"))
)
if mibBuilder.loadTexts:
    hpnicfDot3MpcpGroupBase.setStatus("current")

hpnicfDot3MpcpGroupParam = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 1, 2, 1, 2)
)
hpnicfDot3MpcpGroupParam.setObjects(
      *(("HPN-ICF-DOT3-EFM-EPON-MIB", "hpnicfDot3MpcpTransmitElapsed"),
        ("HPN-ICF-DOT3-EFM-EPON-MIB", "hpnicfDot3MpcpReceiveElapsed"),
        ("HPN-ICF-DOT3-EFM-EPON-MIB", "hpnicfDot3MpcpRoundTripTime"),
        ("HPN-ICF-DOT3-EFM-EPON-MIB", "hpnicfDot3MpcpOnTime"),
        ("HPN-ICF-DOT3-EFM-EPON-MIB", "hpnicfDot3MpcpOffTime"),
        ("HPN-ICF-DOT3-EFM-EPON-MIB", "hpnicfDot3MpcpSyncTime"))
)
if mibBuilder.loadTexts:
    hpnicfDot3MpcpGroupParam.setStatus("current")

hpnicfDot3MpcpGroupStat = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 1, 2, 1, 3)
)
hpnicfDot3MpcpGroupStat.setObjects(
      *(("HPN-ICF-DOT3-EFM-EPON-MIB", "hpnicfDot3MpcpMACCtrlFramesTransmitted"),
        ("HPN-ICF-DOT3-EFM-EPON-MIB", "hpnicfDot3MpcpMACCtrlFramesReceived"),
        ("HPN-ICF-DOT3-EFM-EPON-MIB", "hpnicfDot3MpcpDiscoveryWindowsSent"),
        ("HPN-ICF-DOT3-EFM-EPON-MIB", "hpnicfDot3MpcpDiscoveryTimeout"),
        ("HPN-ICF-DOT3-EFM-EPON-MIB", "hpnicfDot3MpcpTxRegRequest"),
        ("HPN-ICF-DOT3-EFM-EPON-MIB", "hpnicfDot3MpcpRxRegRequest"),
        ("HPN-ICF-DOT3-EFM-EPON-MIB", "hpnicfDot3MpcpTxRegAck"),
        ("HPN-ICF-DOT3-EFM-EPON-MIB", "hpnicfDot3MpcpRxRegAck"),
        ("HPN-ICF-DOT3-EFM-EPON-MIB", "hpnicfDot3MpcpTxReport"),
        ("HPN-ICF-DOT3-EFM-EPON-MIB", "hpnicfDot3MpcpRxReport"),
        ("HPN-ICF-DOT3-EFM-EPON-MIB", "hpnicfDot3MpcpTxGate"),
        ("HPN-ICF-DOT3-EFM-EPON-MIB", "hpnicfDot3MpcpRxGate"),
        ("HPN-ICF-DOT3-EFM-EPON-MIB", "hpnicfDot3MpcpTxRegister"),
        ("HPN-ICF-DOT3-EFM-EPON-MIB", "hpnicfDot3MpcpRxRegister"),
        ("HPN-ICF-DOT3-EFM-EPON-MIB", "hpnicfDot3MpcpRxNotSupportedMPCP"))
)
if mibBuilder.loadTexts:
    hpnicfDot3MpcpGroupStat.setStatus("current")

hpnicfDot3OmpeGroupID = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 2, 2, 1, 1)
)
hpnicfDot3OmpeGroupID.setObjects(
      *(("HPN-ICF-DOT3-EFM-EPON-MIB", "hpnicfDot3OmpEmulationID"),
        ("HPN-ICF-DOT3-EFM-EPON-MIB", "hpnicfDot3OmpEmulationType"))
)
if mibBuilder.loadTexts:
    hpnicfDot3OmpeGroupID.setStatus("current")

hpnicfDot3OmpeGroupStat = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 2, 2, 1, 2)
)
hpnicfDot3OmpeGroupStat.setObjects(
      *(("HPN-ICF-DOT3-EFM-EPON-MIB", "hpnicfDot3OmpEmulationSLDErrors"),
        ("HPN-ICF-DOT3-EFM-EPON-MIB", "hpnicfDot3OmpEmulationCRC8Errors"),
        ("HPN-ICF-DOT3-EFM-EPON-MIB", "hpnicfDot3OmpEmulationBadLLID"),
        ("HPN-ICF-DOT3-EFM-EPON-MIB", "hpnicfDot3OmpEmulationGoodLLID"),
        ("HPN-ICF-DOT3-EFM-EPON-MIB", "hpnicfDot3OmpEmulationOnuPonCastLLID"),
        ("HPN-ICF-DOT3-EFM-EPON-MIB", "hpnicfDot3OmpEmulationOltPonCastLLID"),
        ("HPN-ICF-DOT3-EFM-EPON-MIB", "hpnicfDot3OmpEmulationBroadcastLLIDNotOnuID"),
        ("HPN-ICF-DOT3-EFM-EPON-MIB", "hpnicfDot3OmpEmulationOnuLLIDNotBroadcast"),
        ("HPN-ICF-DOT3-EFM-EPON-MIB", "hpnicfDot3OmpEmulationBroadcastLLIDPlusOnuId"),
        ("HPN-ICF-DOT3-EFM-EPON-MIB", "hpnicfDot3OmpEmulationNotBroadcastLLIDNotOnuId"))
)
if mibBuilder.loadTexts:
    hpnicfDot3OmpeGroupStat.setStatus("current")

hpnicfDot3EponMauGroupAll = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 3, 2, 1, 1)
)
hpnicfDot3EponMauGroupAll.setObjects(
    ("HPN-ICF-DOT3-EFM-EPON-MIB", "hpnicfDot3EponMauPCSCodingViolation")
)
if mibBuilder.loadTexts:
    hpnicfDot3EponMauGroupAll.setStatus("current")

hpnicfDot3EponMauGroupFEC = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 3, 2, 1, 2)
)
hpnicfDot3EponMauGroupFEC.setObjects(
      *(("HPN-ICF-DOT3-EFM-EPON-MIB", "hpnicfDot3EponMauFecAbility"),
        ("HPN-ICF-DOT3-EFM-EPON-MIB", "hpnicfDot3EponMauFecMode"),
        ("HPN-ICF-DOT3-EFM-EPON-MIB", "hpnicfDot3EponMauFECCorrectedBlocks"),
        ("HPN-ICF-DOT3-EFM-EPON-MIB", "hpnicfDot3EponMauFECUncorrectableBlocks"),
        ("HPN-ICF-DOT3-EFM-EPON-MIB", "hpnicfDot3EponMauBufferHeadCodingViolation"))
)
if mibBuilder.loadTexts:
    hpnicfDot3EponMauGroupFEC.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hpnicfDot3MpcpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    hpnicfDot3MpcpCompliance.setStatus(
        "current"
    )

hpnicfDot3OmpeCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 2, 2, 2, 1)
)
if mibBuilder.loadTexts:
    hpnicfDot3OmpeCompliance.setStatus(
        "current"
    )

hpnicfDot3EponMauCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 2, 3, 2, 2, 1)
)
if mibBuilder.loadTexts:
    hpnicfDot3EponMauCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-DOT3-EFM-EPON-MIB",
    **{"hpnicfDot3EfmeponMIB": hpnicfDot3EfmeponMIB,
       "hpnicfDot3MpcpMIB": hpnicfDot3MpcpMIB,
       "hpnicfDot3MpcpObjects": hpnicfDot3MpcpObjects,
       "hpnicfDot3MpcpTable": hpnicfDot3MpcpTable,
       "hpnicfDot3MpcpEntry": hpnicfDot3MpcpEntry,
       "hpnicfDot3MpcpID": hpnicfDot3MpcpID,
       "hpnicfDot3MpcpOperStatus": hpnicfDot3MpcpOperStatus,
       "hpnicfDot3MpcpMode": hpnicfDot3MpcpMode,
       "hpnicfDot3MpcpLinkID": hpnicfDot3MpcpLinkID,
       "hpnicfDot3MpcpRemoteMACAddress": hpnicfDot3MpcpRemoteMACAddress,
       "hpnicfDot3MpcpRegistrationState": hpnicfDot3MpcpRegistrationState,
       "hpnicfDot3MpcpTransmitElapsed": hpnicfDot3MpcpTransmitElapsed,
       "hpnicfDot3MpcpReceiveElapsed": hpnicfDot3MpcpReceiveElapsed,
       "hpnicfDot3MpcpRoundTripTime": hpnicfDot3MpcpRoundTripTime,
       "hpnicfDot3MpcpMaximumPendingGrants": hpnicfDot3MpcpMaximumPendingGrants,
       "hpnicfDot3MpcpAdminState": hpnicfDot3MpcpAdminState,
       "hpnicfDot3MpcpOnTime": hpnicfDot3MpcpOnTime,
       "hpnicfDot3MpcpOffTime": hpnicfDot3MpcpOffTime,
       "hpnicfDot3MpcpSyncTime": hpnicfDot3MpcpSyncTime,
       "hpnicfDot3MpcpStatTable": hpnicfDot3MpcpStatTable,
       "hpnicfDot3MpcpStatEntry": hpnicfDot3MpcpStatEntry,
       "hpnicfDot3MpcpMACCtrlFramesTransmitted": hpnicfDot3MpcpMACCtrlFramesTransmitted,
       "hpnicfDot3MpcpMACCtrlFramesReceived": hpnicfDot3MpcpMACCtrlFramesReceived,
       "hpnicfDot3MpcpDiscoveryWindowsSent": hpnicfDot3MpcpDiscoveryWindowsSent,
       "hpnicfDot3MpcpDiscoveryTimeout": hpnicfDot3MpcpDiscoveryTimeout,
       "hpnicfDot3MpcpTxRegRequest": hpnicfDot3MpcpTxRegRequest,
       "hpnicfDot3MpcpRxRegRequest": hpnicfDot3MpcpRxRegRequest,
       "hpnicfDot3MpcpTxRegAck": hpnicfDot3MpcpTxRegAck,
       "hpnicfDot3MpcpRxRegAck": hpnicfDot3MpcpRxRegAck,
       "hpnicfDot3MpcpTxReport": hpnicfDot3MpcpTxReport,
       "hpnicfDot3MpcpRxReport": hpnicfDot3MpcpRxReport,
       "hpnicfDot3MpcpTxGate": hpnicfDot3MpcpTxGate,
       "hpnicfDot3MpcpRxGate": hpnicfDot3MpcpRxGate,
       "hpnicfDot3MpcpTxRegister": hpnicfDot3MpcpTxRegister,
       "hpnicfDot3MpcpRxRegister": hpnicfDot3MpcpRxRegister,
       "hpnicfDot3MpcpRxNotSupportedMPCP": hpnicfDot3MpcpRxNotSupportedMPCP,
       "hpnicfDot3MpcpConformance": hpnicfDot3MpcpConformance,
       "hpnicfDot3MpcpGroups": hpnicfDot3MpcpGroups,
       "hpnicfDot3MpcpGroupBase": hpnicfDot3MpcpGroupBase,
       "hpnicfDot3MpcpGroupParam": hpnicfDot3MpcpGroupParam,
       "hpnicfDot3MpcpGroupStat": hpnicfDot3MpcpGroupStat,
       "hpnicfDot3MpcpCompliances": hpnicfDot3MpcpCompliances,
       "hpnicfDot3MpcpCompliance": hpnicfDot3MpcpCompliance,
       "hpnicfDot3OmpEmulationMIB": hpnicfDot3OmpEmulationMIB,
       "hpnicfDot3OmpEmulationObjects": hpnicfDot3OmpEmulationObjects,
       "hpnicfDot3OmpEmulationTable": hpnicfDot3OmpEmulationTable,
       "hpnicfDot3OmpEmulationEntry": hpnicfDot3OmpEmulationEntry,
       "hpnicfDot3OmpEmulationID": hpnicfDot3OmpEmulationID,
       "hpnicfDot3OmpEmulationType": hpnicfDot3OmpEmulationType,
       "hpnicfDot3OmpEmulationStatTable": hpnicfDot3OmpEmulationStatTable,
       "hpnicfDot3OmpEmulationStatEntry": hpnicfDot3OmpEmulationStatEntry,
       "hpnicfDot3OmpEmulationSLDErrors": hpnicfDot3OmpEmulationSLDErrors,
       "hpnicfDot3OmpEmulationCRC8Errors": hpnicfDot3OmpEmulationCRC8Errors,
       "hpnicfDot3OmpEmulationBadLLID": hpnicfDot3OmpEmulationBadLLID,
       "hpnicfDot3OmpEmulationGoodLLID": hpnicfDot3OmpEmulationGoodLLID,
       "hpnicfDot3OmpEmulationOnuPonCastLLID": hpnicfDot3OmpEmulationOnuPonCastLLID,
       "hpnicfDot3OmpEmulationOltPonCastLLID": hpnicfDot3OmpEmulationOltPonCastLLID,
       "hpnicfDot3OmpEmulationBroadcastLLIDNotOnuID": hpnicfDot3OmpEmulationBroadcastLLIDNotOnuID,
       "hpnicfDot3OmpEmulationOnuLLIDNotBroadcast": hpnicfDot3OmpEmulationOnuLLIDNotBroadcast,
       "hpnicfDot3OmpEmulationBroadcastLLIDPlusOnuId": hpnicfDot3OmpEmulationBroadcastLLIDPlusOnuId,
       "hpnicfDot3OmpEmulationNotBroadcastLLIDNotOnuId": hpnicfDot3OmpEmulationNotBroadcastLLIDNotOnuId,
       "hpnicfDot3OmpeConformance": hpnicfDot3OmpeConformance,
       "hpnicfDot3OmpeGroups": hpnicfDot3OmpeGroups,
       "hpnicfDot3OmpeGroupID": hpnicfDot3OmpeGroupID,
       "hpnicfDot3OmpeGroupStat": hpnicfDot3OmpeGroupStat,
       "hpnicfDot3OmpeCompliances": hpnicfDot3OmpeCompliances,
       "hpnicfDot3OmpeCompliance": hpnicfDot3OmpeCompliance,
       "hpnicfDot3EponMauMIB": hpnicfDot3EponMauMIB,
       "hpnicfDot3EponMauObjects": hpnicfDot3EponMauObjects,
       "hpnicfDot3EponMauTable": hpnicfDot3EponMauTable,
       "hpnicfDot3EponMauEntry": hpnicfDot3EponMauEntry,
       "hpnicfDot3EponMauPCSCodingViolation": hpnicfDot3EponMauPCSCodingViolation,
       "hpnicfDot3EponMauFecAbility": hpnicfDot3EponMauFecAbility,
       "hpnicfDot3EponMauFecMode": hpnicfDot3EponMauFecMode,
       "hpnicfDot3EponMauFECCorrectedBlocks": hpnicfDot3EponMauFECCorrectedBlocks,
       "hpnicfDot3EponMauFECUncorrectableBlocks": hpnicfDot3EponMauFECUncorrectableBlocks,
       "hpnicfDot3EponMauBufferHeadCodingViolation": hpnicfDot3EponMauBufferHeadCodingViolation,
       "hpnicfDot3EponMauConformance": hpnicfDot3EponMauConformance,
       "hpnicfDot3EponMauGroups": hpnicfDot3EponMauGroups,
       "hpnicfDot3EponMauGroupAll": hpnicfDot3EponMauGroupAll,
       "hpnicfDot3EponMauGroupFEC": hpnicfDot3EponMauGroupFEC,
       "hpnicfDot3EponMauCompliances": hpnicfDot3EponMauCompliances,
       "hpnicfDot3EponMauCompliance": hpnicfDot3EponMauCompliance,
       "hpnicfDot3EponMauType": hpnicfDot3EponMauType,
       "hpnicfEponMauType1000BasePXOLT": hpnicfEponMauType1000BasePXOLT,
       "hpnicfEponMauType1000BasePXONU": hpnicfEponMauType1000BasePXONU,
       "hpnicfEponMauType1000BasePX10DOLT": hpnicfEponMauType1000BasePX10DOLT,
       "hpnicfEponMauType1000BasePX10DONU": hpnicfEponMauType1000BasePX10DONU,
       "hpnicfEponMauType1000BasePX10UOLT": hpnicfEponMauType1000BasePX10UOLT,
       "hpnicfEponMauType1000BasePX10UONU": hpnicfEponMauType1000BasePX10UONU,
       "hpnicfEponMauType1000BasePX20DOLT": hpnicfEponMauType1000BasePX20DOLT,
       "hpnicfEponMauType1000BasePX20DONU": hpnicfEponMauType1000BasePX20DONU,
       "hpnicfEponMauType1000BasePX20UOLT": hpnicfEponMauType1000BasePX20UOLT,
       "hpnicfEponMauType1000BasePX20UONU": hpnicfEponMauType1000BasePX20UONU}
)
