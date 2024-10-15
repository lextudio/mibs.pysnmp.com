# SNMP MIB module (DOT3-EPON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DOT3-EPON-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:33:15 2024
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

dot3EponMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 155)
)
dot3EponMIB.setRevisions(
        ("2007-03-29 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Dot3EponObjects_ObjectIdentity = ObjectIdentity
dot3EponObjects = _Dot3EponObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 155, 1)
)
_Dot3EponMpcpObjects_ObjectIdentity = ObjectIdentity
dot3EponMpcpObjects = _Dot3EponMpcpObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 155, 1, 1)
)
_Dot3MpcpControlTable_Object = MibTable
dot3MpcpControlTable = _Dot3MpcpControlTable_Object(
    (1, 3, 6, 1, 2, 1, 155, 1, 1, 1)
)
if mibBuilder.loadTexts:
    dot3MpcpControlTable.setStatus("current")
_Dot3MpcpControlEntry_Object = MibTableRow
dot3MpcpControlEntry = _Dot3MpcpControlEntry_Object(
    (1, 3, 6, 1, 2, 1, 155, 1, 1, 1, 1)
)
dot3MpcpControlEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dot3MpcpControlEntry.setStatus("current")
_Dot3MpcpOperStatus_Type = TruthValue
_Dot3MpcpOperStatus_Object = MibTableColumn
dot3MpcpOperStatus = _Dot3MpcpOperStatus_Object(
    (1, 3, 6, 1, 2, 1, 155, 1, 1, 1, 1, 1),
    _Dot3MpcpOperStatus_Type()
)
dot3MpcpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3MpcpOperStatus.setStatus("current")


class _Dot3MpcpAdminState_Type(TruthValue):
    """Custom type dot3MpcpAdminState based on TruthValue"""


_Dot3MpcpAdminState_Object = MibTableColumn
dot3MpcpAdminState = _Dot3MpcpAdminState_Object(
    (1, 3, 6, 1, 2, 1, 155, 1, 1, 1, 1, 2),
    _Dot3MpcpAdminState_Type()
)
dot3MpcpAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot3MpcpAdminState.setStatus("current")


class _Dot3MpcpMode_Type(Integer32):
    """Custom type dot3MpcpMode based on Integer32"""
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


_Dot3MpcpMode_Type.__name__ = "Integer32"
_Dot3MpcpMode_Object = MibTableColumn
dot3MpcpMode = _Dot3MpcpMode_Object(
    (1, 3, 6, 1, 2, 1, 155, 1, 1, 1, 1, 3),
    _Dot3MpcpMode_Type()
)
dot3MpcpMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3MpcpMode.setStatus("current")
_Dot3MpcpSyncTime_Type = Unsigned32
_Dot3MpcpSyncTime_Object = MibTableColumn
dot3MpcpSyncTime = _Dot3MpcpSyncTime_Object(
    (1, 3, 6, 1, 2, 1, 155, 1, 1, 1, 1, 4),
    _Dot3MpcpSyncTime_Type()
)
dot3MpcpSyncTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3MpcpSyncTime.setStatus("current")
if mibBuilder.loadTexts:
    dot3MpcpSyncTime.setUnits("TQ (16nsec)")
_Dot3MpcpLinkID_Type = Unsigned32
_Dot3MpcpLinkID_Object = MibTableColumn
dot3MpcpLinkID = _Dot3MpcpLinkID_Object(
    (1, 3, 6, 1, 2, 1, 155, 1, 1, 1, 1, 5),
    _Dot3MpcpLinkID_Type()
)
dot3MpcpLinkID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3MpcpLinkID.setStatus("current")
_Dot3MpcpRemoteMACAddress_Type = MacAddress
_Dot3MpcpRemoteMACAddress_Object = MibTableColumn
dot3MpcpRemoteMACAddress = _Dot3MpcpRemoteMACAddress_Object(
    (1, 3, 6, 1, 2, 1, 155, 1, 1, 1, 1, 6),
    _Dot3MpcpRemoteMACAddress_Type()
)
dot3MpcpRemoteMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3MpcpRemoteMACAddress.setStatus("current")


class _Dot3MpcpRegistrationState_Type(Integer32):
    """Custom type dot3MpcpRegistrationState based on Integer32"""
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


_Dot3MpcpRegistrationState_Type.__name__ = "Integer32"
_Dot3MpcpRegistrationState_Object = MibTableColumn
dot3MpcpRegistrationState = _Dot3MpcpRegistrationState_Object(
    (1, 3, 6, 1, 2, 1, 155, 1, 1, 1, 1, 7),
    _Dot3MpcpRegistrationState_Type()
)
dot3MpcpRegistrationState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3MpcpRegistrationState.setStatus("current")
_Dot3MpcpTransmitElapsed_Type = Unsigned32
_Dot3MpcpTransmitElapsed_Object = MibTableColumn
dot3MpcpTransmitElapsed = _Dot3MpcpTransmitElapsed_Object(
    (1, 3, 6, 1, 2, 1, 155, 1, 1, 1, 1, 8),
    _Dot3MpcpTransmitElapsed_Type()
)
dot3MpcpTransmitElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3MpcpTransmitElapsed.setStatus("current")
if mibBuilder.loadTexts:
    dot3MpcpTransmitElapsed.setUnits("TQ (16nsec)")
_Dot3MpcpReceiveElapsed_Type = Unsigned32
_Dot3MpcpReceiveElapsed_Object = MibTableColumn
dot3MpcpReceiveElapsed = _Dot3MpcpReceiveElapsed_Object(
    (1, 3, 6, 1, 2, 1, 155, 1, 1, 1, 1, 9),
    _Dot3MpcpReceiveElapsed_Type()
)
dot3MpcpReceiveElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3MpcpReceiveElapsed.setStatus("current")
if mibBuilder.loadTexts:
    dot3MpcpReceiveElapsed.setUnits("TQ (16nsec)")


class _Dot3MpcpRoundTripTime_Type(Unsigned32):
    """Custom type dot3MpcpRoundTripTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Dot3MpcpRoundTripTime_Type.__name__ = "Unsigned32"
_Dot3MpcpRoundTripTime_Object = MibTableColumn
dot3MpcpRoundTripTime = _Dot3MpcpRoundTripTime_Object(
    (1, 3, 6, 1, 2, 1, 155, 1, 1, 1, 1, 10),
    _Dot3MpcpRoundTripTime_Type()
)
dot3MpcpRoundTripTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3MpcpRoundTripTime.setStatus("current")
if mibBuilder.loadTexts:
    dot3MpcpRoundTripTime.setUnits("TQ (16nsec)")


class _Dot3MpcpMaximumPendingGrants_Type(Unsigned32):
    """Custom type dot3MpcpMaximumPendingGrants based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Dot3MpcpMaximumPendingGrants_Type.__name__ = "Unsigned32"
_Dot3MpcpMaximumPendingGrants_Object = MibTableColumn
dot3MpcpMaximumPendingGrants = _Dot3MpcpMaximumPendingGrants_Object(
    (1, 3, 6, 1, 2, 1, 155, 1, 1, 1, 1, 11),
    _Dot3MpcpMaximumPendingGrants_Type()
)
dot3MpcpMaximumPendingGrants.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3MpcpMaximumPendingGrants.setStatus("current")
_Dot3MpcpStatTable_Object = MibTable
dot3MpcpStatTable = _Dot3MpcpStatTable_Object(
    (1, 3, 6, 1, 2, 1, 155, 1, 1, 2)
)
if mibBuilder.loadTexts:
    dot3MpcpStatTable.setStatus("current")
_Dot3MpcpStatEntry_Object = MibTableRow
dot3MpcpStatEntry = _Dot3MpcpStatEntry_Object(
    (1, 3, 6, 1, 2, 1, 155, 1, 1, 2, 1)
)
dot3MpcpStatEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dot3MpcpStatEntry.setStatus("current")
_Dot3MpcpMACCtrlFramesTransmitted_Type = Counter64
_Dot3MpcpMACCtrlFramesTransmitted_Object = MibTableColumn
dot3MpcpMACCtrlFramesTransmitted = _Dot3MpcpMACCtrlFramesTransmitted_Object(
    (1, 3, 6, 1, 2, 1, 155, 1, 1, 2, 1, 1),
    _Dot3MpcpMACCtrlFramesTransmitted_Type()
)
dot3MpcpMACCtrlFramesTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3MpcpMACCtrlFramesTransmitted.setStatus("current")
if mibBuilder.loadTexts:
    dot3MpcpMACCtrlFramesTransmitted.setUnits("frames")
_Dot3MpcpMACCtrlFramesReceived_Type = Counter64
_Dot3MpcpMACCtrlFramesReceived_Object = MibTableColumn
dot3MpcpMACCtrlFramesReceived = _Dot3MpcpMACCtrlFramesReceived_Object(
    (1, 3, 6, 1, 2, 1, 155, 1, 1, 2, 1, 2),
    _Dot3MpcpMACCtrlFramesReceived_Type()
)
dot3MpcpMACCtrlFramesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3MpcpMACCtrlFramesReceived.setStatus("current")
if mibBuilder.loadTexts:
    dot3MpcpMACCtrlFramesReceived.setUnits("frames")
_Dot3MpcpDiscoveryWindowsSent_Type = Counter32
_Dot3MpcpDiscoveryWindowsSent_Object = MibTableColumn
dot3MpcpDiscoveryWindowsSent = _Dot3MpcpDiscoveryWindowsSent_Object(
    (1, 3, 6, 1, 2, 1, 155, 1, 1, 2, 1, 3),
    _Dot3MpcpDiscoveryWindowsSent_Type()
)
dot3MpcpDiscoveryWindowsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3MpcpDiscoveryWindowsSent.setStatus("current")
_Dot3MpcpDiscoveryTimeout_Type = Counter32
_Dot3MpcpDiscoveryTimeout_Object = MibTableColumn
dot3MpcpDiscoveryTimeout = _Dot3MpcpDiscoveryTimeout_Object(
    (1, 3, 6, 1, 2, 1, 155, 1, 1, 2, 1, 4),
    _Dot3MpcpDiscoveryTimeout_Type()
)
dot3MpcpDiscoveryTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3MpcpDiscoveryTimeout.setStatus("current")
_Dot3MpcpTxRegRequest_Type = Counter64
_Dot3MpcpTxRegRequest_Object = MibTableColumn
dot3MpcpTxRegRequest = _Dot3MpcpTxRegRequest_Object(
    (1, 3, 6, 1, 2, 1, 155, 1, 1, 2, 1, 5),
    _Dot3MpcpTxRegRequest_Type()
)
dot3MpcpTxRegRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3MpcpTxRegRequest.setStatus("current")
if mibBuilder.loadTexts:
    dot3MpcpTxRegRequest.setUnits("frames")
_Dot3MpcpRxRegRequest_Type = Counter64
_Dot3MpcpRxRegRequest_Object = MibTableColumn
dot3MpcpRxRegRequest = _Dot3MpcpRxRegRequest_Object(
    (1, 3, 6, 1, 2, 1, 155, 1, 1, 2, 1, 6),
    _Dot3MpcpRxRegRequest_Type()
)
dot3MpcpRxRegRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3MpcpRxRegRequest.setStatus("current")
if mibBuilder.loadTexts:
    dot3MpcpRxRegRequest.setUnits("frames")
_Dot3MpcpTxRegAck_Type = Counter64
_Dot3MpcpTxRegAck_Object = MibTableColumn
dot3MpcpTxRegAck = _Dot3MpcpTxRegAck_Object(
    (1, 3, 6, 1, 2, 1, 155, 1, 1, 2, 1, 7),
    _Dot3MpcpTxRegAck_Type()
)
dot3MpcpTxRegAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3MpcpTxRegAck.setStatus("current")
if mibBuilder.loadTexts:
    dot3MpcpTxRegAck.setUnits("frames")
_Dot3MpcpRxRegAck_Type = Counter64
_Dot3MpcpRxRegAck_Object = MibTableColumn
dot3MpcpRxRegAck = _Dot3MpcpRxRegAck_Object(
    (1, 3, 6, 1, 2, 1, 155, 1, 1, 2, 1, 8),
    _Dot3MpcpRxRegAck_Type()
)
dot3MpcpRxRegAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3MpcpRxRegAck.setStatus("current")
if mibBuilder.loadTexts:
    dot3MpcpRxRegAck.setUnits("frames")
_Dot3MpcpTxReport_Type = Counter64
_Dot3MpcpTxReport_Object = MibTableColumn
dot3MpcpTxReport = _Dot3MpcpTxReport_Object(
    (1, 3, 6, 1, 2, 1, 155, 1, 1, 2, 1, 9),
    _Dot3MpcpTxReport_Type()
)
dot3MpcpTxReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3MpcpTxReport.setStatus("current")
if mibBuilder.loadTexts:
    dot3MpcpTxReport.setUnits("frames")
_Dot3MpcpRxReport_Type = Counter64
_Dot3MpcpRxReport_Object = MibTableColumn
dot3MpcpRxReport = _Dot3MpcpRxReport_Object(
    (1, 3, 6, 1, 2, 1, 155, 1, 1, 2, 1, 10),
    _Dot3MpcpRxReport_Type()
)
dot3MpcpRxReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3MpcpRxReport.setStatus("current")
if mibBuilder.loadTexts:
    dot3MpcpRxReport.setUnits("frames")
_Dot3MpcpTxGate_Type = Counter64
_Dot3MpcpTxGate_Object = MibTableColumn
dot3MpcpTxGate = _Dot3MpcpTxGate_Object(
    (1, 3, 6, 1, 2, 1, 155, 1, 1, 2, 1, 11),
    _Dot3MpcpTxGate_Type()
)
dot3MpcpTxGate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3MpcpTxGate.setStatus("current")
if mibBuilder.loadTexts:
    dot3MpcpTxGate.setUnits("frames")
_Dot3MpcpRxGate_Type = Counter64
_Dot3MpcpRxGate_Object = MibTableColumn
dot3MpcpRxGate = _Dot3MpcpRxGate_Object(
    (1, 3, 6, 1, 2, 1, 155, 1, 1, 2, 1, 12),
    _Dot3MpcpRxGate_Type()
)
dot3MpcpRxGate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3MpcpRxGate.setStatus("current")
if mibBuilder.loadTexts:
    dot3MpcpRxGate.setUnits("frames")
_Dot3MpcpTxRegister_Type = Counter64
_Dot3MpcpTxRegister_Object = MibTableColumn
dot3MpcpTxRegister = _Dot3MpcpTxRegister_Object(
    (1, 3, 6, 1, 2, 1, 155, 1, 1, 2, 1, 13),
    _Dot3MpcpTxRegister_Type()
)
dot3MpcpTxRegister.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3MpcpTxRegister.setStatus("current")
if mibBuilder.loadTexts:
    dot3MpcpTxRegister.setUnits("frames")
_Dot3MpcpRxRegister_Type = Counter64
_Dot3MpcpRxRegister_Object = MibTableColumn
dot3MpcpRxRegister = _Dot3MpcpRxRegister_Object(
    (1, 3, 6, 1, 2, 1, 155, 1, 1, 2, 1, 14),
    _Dot3MpcpRxRegister_Type()
)
dot3MpcpRxRegister.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3MpcpRxRegister.setStatus("current")
if mibBuilder.loadTexts:
    dot3MpcpRxRegister.setUnits("frames")
_Dot3OmpEmulationObjects_ObjectIdentity = ObjectIdentity
dot3OmpEmulationObjects = _Dot3OmpEmulationObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 155, 1, 2)
)
_Dot3OmpEmulationTable_Object = MibTable
dot3OmpEmulationTable = _Dot3OmpEmulationTable_Object(
    (1, 3, 6, 1, 2, 1, 155, 1, 2, 1)
)
if mibBuilder.loadTexts:
    dot3OmpEmulationTable.setStatus("current")
_Dot3OmpEmulationEntry_Object = MibTableRow
dot3OmpEmulationEntry = _Dot3OmpEmulationEntry_Object(
    (1, 3, 6, 1, 2, 1, 155, 1, 2, 1, 1)
)
dot3OmpEmulationEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dot3OmpEmulationEntry.setStatus("current")


class _Dot3OmpEmulationType_Type(Integer32):
    """Custom type dot3OmpEmulationType based on Integer32"""
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


_Dot3OmpEmulationType_Type.__name__ = "Integer32"
_Dot3OmpEmulationType_Object = MibTableColumn
dot3OmpEmulationType = _Dot3OmpEmulationType_Object(
    (1, 3, 6, 1, 2, 1, 155, 1, 2, 1, 1, 1),
    _Dot3OmpEmulationType_Type()
)
dot3OmpEmulationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3OmpEmulationType.setStatus("current")
_Dot3OmpEmulationStatTable_Object = MibTable
dot3OmpEmulationStatTable = _Dot3OmpEmulationStatTable_Object(
    (1, 3, 6, 1, 2, 1, 155, 1, 2, 2)
)
if mibBuilder.loadTexts:
    dot3OmpEmulationStatTable.setStatus("current")
_Dot3OmpEmulationStatEntry_Object = MibTableRow
dot3OmpEmulationStatEntry = _Dot3OmpEmulationStatEntry_Object(
    (1, 3, 6, 1, 2, 1, 155, 1, 2, 2, 1)
)
dot3OmpEmulationStatEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dot3OmpEmulationStatEntry.setStatus("current")
_Dot3OmpEmulationSLDErrors_Type = Counter64
_Dot3OmpEmulationSLDErrors_Object = MibTableColumn
dot3OmpEmulationSLDErrors = _Dot3OmpEmulationSLDErrors_Object(
    (1, 3, 6, 1, 2, 1, 155, 1, 2, 2, 1, 1),
    _Dot3OmpEmulationSLDErrors_Type()
)
dot3OmpEmulationSLDErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3OmpEmulationSLDErrors.setStatus("current")
if mibBuilder.loadTexts:
    dot3OmpEmulationSLDErrors.setUnits("frames")
_Dot3OmpEmulationCRC8Errors_Type = Counter64
_Dot3OmpEmulationCRC8Errors_Object = MibTableColumn
dot3OmpEmulationCRC8Errors = _Dot3OmpEmulationCRC8Errors_Object(
    (1, 3, 6, 1, 2, 1, 155, 1, 2, 2, 1, 2),
    _Dot3OmpEmulationCRC8Errors_Type()
)
dot3OmpEmulationCRC8Errors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3OmpEmulationCRC8Errors.setStatus("current")
if mibBuilder.loadTexts:
    dot3OmpEmulationCRC8Errors.setUnits("frames")
_Dot3OmpEmulationBadLLID_Type = Counter64
_Dot3OmpEmulationBadLLID_Object = MibTableColumn
dot3OmpEmulationBadLLID = _Dot3OmpEmulationBadLLID_Object(
    (1, 3, 6, 1, 2, 1, 155, 1, 2, 2, 1, 3),
    _Dot3OmpEmulationBadLLID_Type()
)
dot3OmpEmulationBadLLID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3OmpEmulationBadLLID.setStatus("current")
if mibBuilder.loadTexts:
    dot3OmpEmulationBadLLID.setUnits("frames")
_Dot3OmpEmulationGoodLLID_Type = Counter64
_Dot3OmpEmulationGoodLLID_Object = MibTableColumn
dot3OmpEmulationGoodLLID = _Dot3OmpEmulationGoodLLID_Object(
    (1, 3, 6, 1, 2, 1, 155, 1, 2, 2, 1, 4),
    _Dot3OmpEmulationGoodLLID_Type()
)
dot3OmpEmulationGoodLLID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3OmpEmulationGoodLLID.setStatus("current")
if mibBuilder.loadTexts:
    dot3OmpEmulationGoodLLID.setUnits("frames")
_Dot3OmpEmulationOnuPonCastLLID_Type = Counter64
_Dot3OmpEmulationOnuPonCastLLID_Object = MibTableColumn
dot3OmpEmulationOnuPonCastLLID = _Dot3OmpEmulationOnuPonCastLLID_Object(
    (1, 3, 6, 1, 2, 1, 155, 1, 2, 2, 1, 5),
    _Dot3OmpEmulationOnuPonCastLLID_Type()
)
dot3OmpEmulationOnuPonCastLLID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3OmpEmulationOnuPonCastLLID.setStatus("current")
if mibBuilder.loadTexts:
    dot3OmpEmulationOnuPonCastLLID.setUnits("frames")
_Dot3OmpEmulationOltPonCastLLID_Type = Counter64
_Dot3OmpEmulationOltPonCastLLID_Object = MibTableColumn
dot3OmpEmulationOltPonCastLLID = _Dot3OmpEmulationOltPonCastLLID_Object(
    (1, 3, 6, 1, 2, 1, 155, 1, 2, 2, 1, 6),
    _Dot3OmpEmulationOltPonCastLLID_Type()
)
dot3OmpEmulationOltPonCastLLID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3OmpEmulationOltPonCastLLID.setStatus("current")
if mibBuilder.loadTexts:
    dot3OmpEmulationOltPonCastLLID.setUnits("frames")
_Dot3OmpEmulationBroadcastBitNotOnuLlid_Type = Counter64
_Dot3OmpEmulationBroadcastBitNotOnuLlid_Object = MibTableColumn
dot3OmpEmulationBroadcastBitNotOnuLlid = _Dot3OmpEmulationBroadcastBitNotOnuLlid_Object(
    (1, 3, 6, 1, 2, 1, 155, 1, 2, 2, 1, 7),
    _Dot3OmpEmulationBroadcastBitNotOnuLlid_Type()
)
dot3OmpEmulationBroadcastBitNotOnuLlid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3OmpEmulationBroadcastBitNotOnuLlid.setStatus("current")
if mibBuilder.loadTexts:
    dot3OmpEmulationBroadcastBitNotOnuLlid.setUnits("frames")
_Dot3OmpEmulationOnuLLIDNotBroadcast_Type = Counter64
_Dot3OmpEmulationOnuLLIDNotBroadcast_Object = MibTableColumn
dot3OmpEmulationOnuLLIDNotBroadcast = _Dot3OmpEmulationOnuLLIDNotBroadcast_Object(
    (1, 3, 6, 1, 2, 1, 155, 1, 2, 2, 1, 8),
    _Dot3OmpEmulationOnuLLIDNotBroadcast_Type()
)
dot3OmpEmulationOnuLLIDNotBroadcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3OmpEmulationOnuLLIDNotBroadcast.setStatus("current")
if mibBuilder.loadTexts:
    dot3OmpEmulationOnuLLIDNotBroadcast.setUnits("frames")
_Dot3OmpEmulationBroadcastBitPlusOnuLlid_Type = Counter64
_Dot3OmpEmulationBroadcastBitPlusOnuLlid_Object = MibTableColumn
dot3OmpEmulationBroadcastBitPlusOnuLlid = _Dot3OmpEmulationBroadcastBitPlusOnuLlid_Object(
    (1, 3, 6, 1, 2, 1, 155, 1, 2, 2, 1, 9),
    _Dot3OmpEmulationBroadcastBitPlusOnuLlid_Type()
)
dot3OmpEmulationBroadcastBitPlusOnuLlid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3OmpEmulationBroadcastBitPlusOnuLlid.setStatus("current")
if mibBuilder.loadTexts:
    dot3OmpEmulationBroadcastBitPlusOnuLlid.setUnits("frames")
_Dot3OmpEmulationNotBroadcastBitNotOnuLlid_Type = Counter64
_Dot3OmpEmulationNotBroadcastBitNotOnuLlid_Object = MibTableColumn
dot3OmpEmulationNotBroadcastBitNotOnuLlid = _Dot3OmpEmulationNotBroadcastBitNotOnuLlid_Object(
    (1, 3, 6, 1, 2, 1, 155, 1, 2, 2, 1, 10),
    _Dot3OmpEmulationNotBroadcastBitNotOnuLlid_Type()
)
dot3OmpEmulationNotBroadcastBitNotOnuLlid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3OmpEmulationNotBroadcastBitNotOnuLlid.setStatus("current")
if mibBuilder.loadTexts:
    dot3OmpEmulationNotBroadcastBitNotOnuLlid.setUnits("frames")
_Dot3EponFecObjects_ObjectIdentity = ObjectIdentity
dot3EponFecObjects = _Dot3EponFecObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 155, 1, 3)
)
_Dot3EponFecTable_Object = MibTable
dot3EponFecTable = _Dot3EponFecTable_Object(
    (1, 3, 6, 1, 2, 1, 155, 1, 3, 1)
)
if mibBuilder.loadTexts:
    dot3EponFecTable.setStatus("current")
_Dot3EponFecEntry_Object = MibTableRow
dot3EponFecEntry = _Dot3EponFecEntry_Object(
    (1, 3, 6, 1, 2, 1, 155, 1, 3, 1, 1)
)
dot3EponFecEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dot3EponFecEntry.setStatus("current")
_Dot3EponFecPCSCodingViolation_Type = Counter64
_Dot3EponFecPCSCodingViolation_Object = MibTableColumn
dot3EponFecPCSCodingViolation = _Dot3EponFecPCSCodingViolation_Object(
    (1, 3, 6, 1, 2, 1, 155, 1, 3, 1, 1, 1),
    _Dot3EponFecPCSCodingViolation_Type()
)
dot3EponFecPCSCodingViolation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3EponFecPCSCodingViolation.setStatus("current")
if mibBuilder.loadTexts:
    dot3EponFecPCSCodingViolation.setUnits("octets")


class _Dot3EponFecAbility_Type(Integer32):
    """Custom type dot3EponFecAbility based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("supported", 2),
          ("unknown", 1),
          ("unsupported", 3))
    )


_Dot3EponFecAbility_Type.__name__ = "Integer32"
_Dot3EponFecAbility_Object = MibTableColumn
dot3EponFecAbility = _Dot3EponFecAbility_Object(
    (1, 3, 6, 1, 2, 1, 155, 1, 3, 1, 1, 2),
    _Dot3EponFecAbility_Type()
)
dot3EponFecAbility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3EponFecAbility.setStatus("current")


class _Dot3EponFecMode_Type(Integer32):
    """Custom type dot3EponFecMode based on Integer32"""
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


_Dot3EponFecMode_Type.__name__ = "Integer32"
_Dot3EponFecMode_Object = MibTableColumn
dot3EponFecMode = _Dot3EponFecMode_Object(
    (1, 3, 6, 1, 2, 1, 155, 1, 3, 1, 1, 3),
    _Dot3EponFecMode_Type()
)
dot3EponFecMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot3EponFecMode.setStatus("current")
_Dot3EponFecCorrectedBlocks_Type = Counter64
_Dot3EponFecCorrectedBlocks_Object = MibTableColumn
dot3EponFecCorrectedBlocks = _Dot3EponFecCorrectedBlocks_Object(
    (1, 3, 6, 1, 2, 1, 155, 1, 3, 1, 1, 4),
    _Dot3EponFecCorrectedBlocks_Type()
)
dot3EponFecCorrectedBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3EponFecCorrectedBlocks.setStatus("current")
_Dot3EponFecUncorrectableBlocks_Type = Counter64
_Dot3EponFecUncorrectableBlocks_Object = MibTableColumn
dot3EponFecUncorrectableBlocks = _Dot3EponFecUncorrectableBlocks_Object(
    (1, 3, 6, 1, 2, 1, 155, 1, 3, 1, 1, 5),
    _Dot3EponFecUncorrectableBlocks_Type()
)
dot3EponFecUncorrectableBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3EponFecUncorrectableBlocks.setStatus("current")
_Dot3EponFecBufferHeadCodingViolation_Type = Counter64
_Dot3EponFecBufferHeadCodingViolation_Object = MibTableColumn
dot3EponFecBufferHeadCodingViolation = _Dot3EponFecBufferHeadCodingViolation_Object(
    (1, 3, 6, 1, 2, 1, 155, 1, 3, 1, 1, 6),
    _Dot3EponFecBufferHeadCodingViolation_Type()
)
dot3EponFecBufferHeadCodingViolation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3EponFecBufferHeadCodingViolation.setStatus("current")
if mibBuilder.loadTexts:
    dot3EponFecBufferHeadCodingViolation.setUnits("octets")
_Dot3ExtPkgObjects_ObjectIdentity = ObjectIdentity
dot3ExtPkgObjects = _Dot3ExtPkgObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 155, 1, 4)
)
_Dot3ExtPkgControlObjects_ObjectIdentity = ObjectIdentity
dot3ExtPkgControlObjects = _Dot3ExtPkgControlObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 155, 1, 4, 1)
)
_Dot3ExtPkgControlTable_Object = MibTable
dot3ExtPkgControlTable = _Dot3ExtPkgControlTable_Object(
    (1, 3, 6, 1, 2, 1, 155, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    dot3ExtPkgControlTable.setStatus("current")
_Dot3ExtPkgControlEntry_Object = MibTableRow
dot3ExtPkgControlEntry = _Dot3ExtPkgControlEntry_Object(
    (1, 3, 6, 1, 2, 1, 155, 1, 4, 1, 1, 1)
)
dot3ExtPkgControlEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dot3ExtPkgControlEntry.setStatus("current")


class _Dot3ExtPkgObjectReset_Type(Integer32):
    """Custom type dot3ExtPkgObjectReset based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("reset", 2),
          ("running", 1))
    )


_Dot3ExtPkgObjectReset_Type.__name__ = "Integer32"
_Dot3ExtPkgObjectReset_Object = MibTableColumn
dot3ExtPkgObjectReset = _Dot3ExtPkgObjectReset_Object(
    (1, 3, 6, 1, 2, 1, 155, 1, 4, 1, 1, 1, 1),
    _Dot3ExtPkgObjectReset_Type()
)
dot3ExtPkgObjectReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot3ExtPkgObjectReset.setStatus("current")


class _Dot3ExtPkgObjectPowerDown_Type(TruthValue):
    """Custom type dot3ExtPkgObjectPowerDown based on TruthValue"""


_Dot3ExtPkgObjectPowerDown_Object = MibTableColumn
dot3ExtPkgObjectPowerDown = _Dot3ExtPkgObjectPowerDown_Object(
    (1, 3, 6, 1, 2, 1, 155, 1, 4, 1, 1, 1, 2),
    _Dot3ExtPkgObjectPowerDown_Type()
)
dot3ExtPkgObjectPowerDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot3ExtPkgObjectPowerDown.setStatus("current")
_Dot3ExtPkgObjectNumberOfLLIDs_Type = Unsigned32
_Dot3ExtPkgObjectNumberOfLLIDs_Object = MibTableColumn
dot3ExtPkgObjectNumberOfLLIDs = _Dot3ExtPkgObjectNumberOfLLIDs_Object(
    (1, 3, 6, 1, 2, 1, 155, 1, 4, 1, 1, 1, 3),
    _Dot3ExtPkgObjectNumberOfLLIDs_Type()
)
dot3ExtPkgObjectNumberOfLLIDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3ExtPkgObjectNumberOfLLIDs.setStatus("current")


class _Dot3ExtPkgObjectFecEnabled_Type(Integer32):
    """Custom type dot3ExtPkgObjectFecEnabled based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("fecRxEnabled", 3),
          ("fecTxEnabled", 2),
          ("fecTxRxEnabled", 4),
          ("noFecEnabled", 1))
    )


_Dot3ExtPkgObjectFecEnabled_Type.__name__ = "Integer32"
_Dot3ExtPkgObjectFecEnabled_Object = MibTableColumn
dot3ExtPkgObjectFecEnabled = _Dot3ExtPkgObjectFecEnabled_Object(
    (1, 3, 6, 1, 2, 1, 155, 1, 4, 1, 1, 1, 4),
    _Dot3ExtPkgObjectFecEnabled_Type()
)
dot3ExtPkgObjectFecEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot3ExtPkgObjectFecEnabled.setStatus("current")


class _Dot3ExtPkgObjectReportMaximumNumQueues_Type(Unsigned32):
    """Custom type dot3ExtPkgObjectReportMaximumNumQueues based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Dot3ExtPkgObjectReportMaximumNumQueues_Type.__name__ = "Unsigned32"
_Dot3ExtPkgObjectReportMaximumNumQueues_Object = MibTableColumn
dot3ExtPkgObjectReportMaximumNumQueues = _Dot3ExtPkgObjectReportMaximumNumQueues_Object(
    (1, 3, 6, 1, 2, 1, 155, 1, 4, 1, 1, 1, 5),
    _Dot3ExtPkgObjectReportMaximumNumQueues_Type()
)
dot3ExtPkgObjectReportMaximumNumQueues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3ExtPkgObjectReportMaximumNumQueues.setStatus("current")


class _Dot3ExtPkgObjectRegisterAction_Type(Integer32):
    """Custom type dot3ExtPkgObjectRegisterAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("deregister", 3),
          ("none", 1),
          ("register", 2),
          ("reregister", 4))
    )


_Dot3ExtPkgObjectRegisterAction_Type.__name__ = "Integer32"
_Dot3ExtPkgObjectRegisterAction_Object = MibTableColumn
dot3ExtPkgObjectRegisterAction = _Dot3ExtPkgObjectRegisterAction_Object(
    (1, 3, 6, 1, 2, 1, 155, 1, 4, 1, 1, 1, 6),
    _Dot3ExtPkgObjectRegisterAction_Type()
)
dot3ExtPkgObjectRegisterAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot3ExtPkgObjectRegisterAction.setStatus("current")
_Dot3ExtPkgQueueTable_Object = MibTable
dot3ExtPkgQueueTable = _Dot3ExtPkgQueueTable_Object(
    (1, 3, 6, 1, 2, 1, 155, 1, 4, 1, 2)
)
if mibBuilder.loadTexts:
    dot3ExtPkgQueueTable.setStatus("current")
_Dot3ExtPkgQueueEntry_Object = MibTableRow
dot3ExtPkgQueueEntry = _Dot3ExtPkgQueueEntry_Object(
    (1, 3, 6, 1, 2, 1, 155, 1, 4, 1, 2, 1)
)
dot3ExtPkgQueueEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DOT3-EPON-MIB", "dot3QueueIndex"),
)
if mibBuilder.loadTexts:
    dot3ExtPkgQueueEntry.setStatus("current")


class _Dot3QueueIndex_Type(Unsigned32):
    """Custom type dot3QueueIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Dot3QueueIndex_Type.__name__ = "Unsigned32"
_Dot3QueueIndex_Object = MibTableColumn
dot3QueueIndex = _Dot3QueueIndex_Object(
    (1, 3, 6, 1, 2, 1, 155, 1, 4, 1, 2, 1, 1),
    _Dot3QueueIndex_Type()
)
dot3QueueIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot3QueueIndex.setStatus("current")


class _Dot3ExtPkgObjectReportNumThreshold_Type(Unsigned32):
    """Custom type dot3ExtPkgObjectReportNumThreshold based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Dot3ExtPkgObjectReportNumThreshold_Type.__name__ = "Unsigned32"
_Dot3ExtPkgObjectReportNumThreshold_Object = MibTableColumn
dot3ExtPkgObjectReportNumThreshold = _Dot3ExtPkgObjectReportNumThreshold_Object(
    (1, 3, 6, 1, 2, 1, 155, 1, 4, 1, 2, 1, 2),
    _Dot3ExtPkgObjectReportNumThreshold_Type()
)
dot3ExtPkgObjectReportNumThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot3ExtPkgObjectReportNumThreshold.setStatus("current")


class _Dot3ExtPkgObjectReportMaximumNumThreshold_Type(Unsigned32):
    """Custom type dot3ExtPkgObjectReportMaximumNumThreshold based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Dot3ExtPkgObjectReportMaximumNumThreshold_Type.__name__ = "Unsigned32"
_Dot3ExtPkgObjectReportMaximumNumThreshold_Object = MibTableColumn
dot3ExtPkgObjectReportMaximumNumThreshold = _Dot3ExtPkgObjectReportMaximumNumThreshold_Object(
    (1, 3, 6, 1, 2, 1, 155, 1, 4, 1, 2, 1, 3),
    _Dot3ExtPkgObjectReportMaximumNumThreshold_Type()
)
dot3ExtPkgObjectReportMaximumNumThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3ExtPkgObjectReportMaximumNumThreshold.setStatus("current")
_Dot3ExtPkgStatTxFramesQueue_Type = Counter64
_Dot3ExtPkgStatTxFramesQueue_Object = MibTableColumn
dot3ExtPkgStatTxFramesQueue = _Dot3ExtPkgStatTxFramesQueue_Object(
    (1, 3, 6, 1, 2, 1, 155, 1, 4, 1, 2, 1, 4),
    _Dot3ExtPkgStatTxFramesQueue_Type()
)
dot3ExtPkgStatTxFramesQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3ExtPkgStatTxFramesQueue.setStatus("current")
if mibBuilder.loadTexts:
    dot3ExtPkgStatTxFramesQueue.setUnits("frames")
_Dot3ExtPkgStatRxFramesQueue_Type = Counter64
_Dot3ExtPkgStatRxFramesQueue_Object = MibTableColumn
dot3ExtPkgStatRxFramesQueue = _Dot3ExtPkgStatRxFramesQueue_Object(
    (1, 3, 6, 1, 2, 1, 155, 1, 4, 1, 2, 1, 5),
    _Dot3ExtPkgStatRxFramesQueue_Type()
)
dot3ExtPkgStatRxFramesQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3ExtPkgStatRxFramesQueue.setStatus("current")
if mibBuilder.loadTexts:
    dot3ExtPkgStatRxFramesQueue.setUnits("frames")
_Dot3ExtPkgStatDroppedFramesQueue_Type = Counter64
_Dot3ExtPkgStatDroppedFramesQueue_Object = MibTableColumn
dot3ExtPkgStatDroppedFramesQueue = _Dot3ExtPkgStatDroppedFramesQueue_Object(
    (1, 3, 6, 1, 2, 1, 155, 1, 4, 1, 2, 1, 6),
    _Dot3ExtPkgStatDroppedFramesQueue_Type()
)
dot3ExtPkgStatDroppedFramesQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3ExtPkgStatDroppedFramesQueue.setStatus("current")
if mibBuilder.loadTexts:
    dot3ExtPkgStatDroppedFramesQueue.setUnits("frames")
_Dot3ExtPkgQueueSetsTable_Object = MibTable
dot3ExtPkgQueueSetsTable = _Dot3ExtPkgQueueSetsTable_Object(
    (1, 3, 6, 1, 2, 1, 155, 1, 4, 1, 3)
)
if mibBuilder.loadTexts:
    dot3ExtPkgQueueSetsTable.setStatus("current")
_Dot3ExtPkgQueueSetsEntry_Object = MibTableRow
dot3ExtPkgQueueSetsEntry = _Dot3ExtPkgQueueSetsEntry_Object(
    (1, 3, 6, 1, 2, 1, 155, 1, 4, 1, 3, 1)
)
dot3ExtPkgQueueSetsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DOT3-EPON-MIB", "dot3QueueSetQueueIndex"),
    (0, "DOT3-EPON-MIB", "dot3QueueSetIndex"),
)
if mibBuilder.loadTexts:
    dot3ExtPkgQueueSetsEntry.setStatus("current")


class _Dot3QueueSetQueueIndex_Type(Unsigned32):
    """Custom type dot3QueueSetQueueIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Dot3QueueSetQueueIndex_Type.__name__ = "Unsigned32"
_Dot3QueueSetQueueIndex_Object = MibTableColumn
dot3QueueSetQueueIndex = _Dot3QueueSetQueueIndex_Object(
    (1, 3, 6, 1, 2, 1, 155, 1, 4, 1, 3, 1, 1),
    _Dot3QueueSetQueueIndex_Type()
)
dot3QueueSetQueueIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot3QueueSetQueueIndex.setStatus("current")


class _Dot3QueueSetIndex_Type(Unsigned32):
    """Custom type dot3QueueSetIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Dot3QueueSetIndex_Type.__name__ = "Unsigned32"
_Dot3QueueSetIndex_Object = MibTableColumn
dot3QueueSetIndex = _Dot3QueueSetIndex_Object(
    (1, 3, 6, 1, 2, 1, 155, 1, 4, 1, 3, 1, 2),
    _Dot3QueueSetIndex_Type()
)
dot3QueueSetIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot3QueueSetIndex.setStatus("current")


class _Dot3ExtPkgObjectReportThreshold_Type(Unsigned32):
    """Custom type dot3ExtPkgObjectReportThreshold based on Unsigned32"""
    defaultValue = 0


_Dot3ExtPkgObjectReportThreshold_Object = MibTableColumn
dot3ExtPkgObjectReportThreshold = _Dot3ExtPkgObjectReportThreshold_Object(
    (1, 3, 6, 1, 2, 1, 155, 1, 4, 1, 3, 1, 3),
    _Dot3ExtPkgObjectReportThreshold_Type()
)
dot3ExtPkgObjectReportThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot3ExtPkgObjectReportThreshold.setStatus("current")
if mibBuilder.loadTexts:
    dot3ExtPkgObjectReportThreshold.setUnits("TQ (16nsec)")
_Dot3ExtPkgOptIfTable_Object = MibTable
dot3ExtPkgOptIfTable = _Dot3ExtPkgOptIfTable_Object(
    (1, 3, 6, 1, 2, 1, 155, 1, 4, 1, 5)
)
if mibBuilder.loadTexts:
    dot3ExtPkgOptIfTable.setStatus("current")
_Dot3ExtPkgOptIfEntry_Object = MibTableRow
dot3ExtPkgOptIfEntry = _Dot3ExtPkgOptIfEntry_Object(
    (1, 3, 6, 1, 2, 1, 155, 1, 4, 1, 5, 1)
)
dot3ExtPkgOptIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dot3ExtPkgOptIfEntry.setStatus("current")
_Dot3ExtPkgOptIfSuspectedFlag_Type = TruthValue
_Dot3ExtPkgOptIfSuspectedFlag_Object = MibTableColumn
dot3ExtPkgOptIfSuspectedFlag = _Dot3ExtPkgOptIfSuspectedFlag_Object(
    (1, 3, 6, 1, 2, 1, 155, 1, 4, 1, 5, 1, 1),
    _Dot3ExtPkgOptIfSuspectedFlag_Type()
)
dot3ExtPkgOptIfSuspectedFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3ExtPkgOptIfSuspectedFlag.setStatus("current")
_Dot3ExtPkgOptIfInputPower_Type = Integer32
_Dot3ExtPkgOptIfInputPower_Object = MibTableColumn
dot3ExtPkgOptIfInputPower = _Dot3ExtPkgOptIfInputPower_Object(
    (1, 3, 6, 1, 2, 1, 155, 1, 4, 1, 5, 1, 2),
    _Dot3ExtPkgOptIfInputPower_Type()
)
dot3ExtPkgOptIfInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3ExtPkgOptIfInputPower.setStatus("current")
if mibBuilder.loadTexts:
    dot3ExtPkgOptIfInputPower.setUnits("0.1 dbm")
_Dot3ExtPkgOptIfLowInputPower_Type = Integer32
_Dot3ExtPkgOptIfLowInputPower_Object = MibTableColumn
dot3ExtPkgOptIfLowInputPower = _Dot3ExtPkgOptIfLowInputPower_Object(
    (1, 3, 6, 1, 2, 1, 155, 1, 4, 1, 5, 1, 3),
    _Dot3ExtPkgOptIfLowInputPower_Type()
)
dot3ExtPkgOptIfLowInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3ExtPkgOptIfLowInputPower.setStatus("current")
if mibBuilder.loadTexts:
    dot3ExtPkgOptIfLowInputPower.setUnits("0.1 dbm")
_Dot3ExtPkgOptIfHighInputPower_Type = Integer32
_Dot3ExtPkgOptIfHighInputPower_Object = MibTableColumn
dot3ExtPkgOptIfHighInputPower = _Dot3ExtPkgOptIfHighInputPower_Object(
    (1, 3, 6, 1, 2, 1, 155, 1, 4, 1, 5, 1, 4),
    _Dot3ExtPkgOptIfHighInputPower_Type()
)
dot3ExtPkgOptIfHighInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3ExtPkgOptIfHighInputPower.setStatus("current")
if mibBuilder.loadTexts:
    dot3ExtPkgOptIfHighInputPower.setUnits("0.1 dbm")
_Dot3ExtPkgOptIfLowerInputPowerThreshold_Type = Integer32
_Dot3ExtPkgOptIfLowerInputPowerThreshold_Object = MibTableColumn
dot3ExtPkgOptIfLowerInputPowerThreshold = _Dot3ExtPkgOptIfLowerInputPowerThreshold_Object(
    (1, 3, 6, 1, 2, 1, 155, 1, 4, 1, 5, 1, 5),
    _Dot3ExtPkgOptIfLowerInputPowerThreshold_Type()
)
dot3ExtPkgOptIfLowerInputPowerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot3ExtPkgOptIfLowerInputPowerThreshold.setStatus("current")
if mibBuilder.loadTexts:
    dot3ExtPkgOptIfLowerInputPowerThreshold.setUnits("0.1 dbm")
_Dot3ExtPkgOptIfUpperInputPowerThreshold_Type = Integer32
_Dot3ExtPkgOptIfUpperInputPowerThreshold_Object = MibTableColumn
dot3ExtPkgOptIfUpperInputPowerThreshold = _Dot3ExtPkgOptIfUpperInputPowerThreshold_Object(
    (1, 3, 6, 1, 2, 1, 155, 1, 4, 1, 5, 1, 6),
    _Dot3ExtPkgOptIfUpperInputPowerThreshold_Type()
)
dot3ExtPkgOptIfUpperInputPowerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot3ExtPkgOptIfUpperInputPowerThreshold.setStatus("current")
if mibBuilder.loadTexts:
    dot3ExtPkgOptIfUpperInputPowerThreshold.setUnits("0.1 dbm")
_Dot3ExtPkgOptIfOutputPower_Type = Integer32
_Dot3ExtPkgOptIfOutputPower_Object = MibTableColumn
dot3ExtPkgOptIfOutputPower = _Dot3ExtPkgOptIfOutputPower_Object(
    (1, 3, 6, 1, 2, 1, 155, 1, 4, 1, 5, 1, 7),
    _Dot3ExtPkgOptIfOutputPower_Type()
)
dot3ExtPkgOptIfOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3ExtPkgOptIfOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    dot3ExtPkgOptIfOutputPower.setUnits("0.1 dbm")
_Dot3ExtPkgOptIfLowOutputPower_Type = Integer32
_Dot3ExtPkgOptIfLowOutputPower_Object = MibTableColumn
dot3ExtPkgOptIfLowOutputPower = _Dot3ExtPkgOptIfLowOutputPower_Object(
    (1, 3, 6, 1, 2, 1, 155, 1, 4, 1, 5, 1, 8),
    _Dot3ExtPkgOptIfLowOutputPower_Type()
)
dot3ExtPkgOptIfLowOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3ExtPkgOptIfLowOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    dot3ExtPkgOptIfLowOutputPower.setUnits("0.1 dbm")
_Dot3ExtPkgOptIfHighOutputPower_Type = Integer32
_Dot3ExtPkgOptIfHighOutputPower_Object = MibTableColumn
dot3ExtPkgOptIfHighOutputPower = _Dot3ExtPkgOptIfHighOutputPower_Object(
    (1, 3, 6, 1, 2, 1, 155, 1, 4, 1, 5, 1, 9),
    _Dot3ExtPkgOptIfHighOutputPower_Type()
)
dot3ExtPkgOptIfHighOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3ExtPkgOptIfHighOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    dot3ExtPkgOptIfHighOutputPower.setUnits("0.1 dbm")
_Dot3ExtPkgOptIfLowerOutputPowerThreshold_Type = Integer32
_Dot3ExtPkgOptIfLowerOutputPowerThreshold_Object = MibTableColumn
dot3ExtPkgOptIfLowerOutputPowerThreshold = _Dot3ExtPkgOptIfLowerOutputPowerThreshold_Object(
    (1, 3, 6, 1, 2, 1, 155, 1, 4, 1, 5, 1, 10),
    _Dot3ExtPkgOptIfLowerOutputPowerThreshold_Type()
)
dot3ExtPkgOptIfLowerOutputPowerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot3ExtPkgOptIfLowerOutputPowerThreshold.setStatus("current")
if mibBuilder.loadTexts:
    dot3ExtPkgOptIfLowerOutputPowerThreshold.setUnits("0.1 dbm")
_Dot3ExtPkgOptIfUpperOutputPowerThreshold_Type = Integer32
_Dot3ExtPkgOptIfUpperOutputPowerThreshold_Object = MibTableColumn
dot3ExtPkgOptIfUpperOutputPowerThreshold = _Dot3ExtPkgOptIfUpperOutputPowerThreshold_Object(
    (1, 3, 6, 1, 2, 1, 155, 1, 4, 1, 5, 1, 11),
    _Dot3ExtPkgOptIfUpperOutputPowerThreshold_Type()
)
dot3ExtPkgOptIfUpperOutputPowerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot3ExtPkgOptIfUpperOutputPowerThreshold.setStatus("current")
if mibBuilder.loadTexts:
    dot3ExtPkgOptIfUpperOutputPowerThreshold.setUnits("0.1 dbm")


class _Dot3ExtPkgOptIfSignalDetect_Type(TruthValue):
    """Custom type dot3ExtPkgOptIfSignalDetect based on TruthValue"""


_Dot3ExtPkgOptIfSignalDetect_Object = MibTableColumn
dot3ExtPkgOptIfSignalDetect = _Dot3ExtPkgOptIfSignalDetect_Object(
    (1, 3, 6, 1, 2, 1, 155, 1, 4, 1, 5, 1, 12),
    _Dot3ExtPkgOptIfSignalDetect_Type()
)
dot3ExtPkgOptIfSignalDetect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3ExtPkgOptIfSignalDetect.setStatus("current")


class _Dot3ExtPkgOptIfTransmitAlarm_Type(TruthValue):
    """Custom type dot3ExtPkgOptIfTransmitAlarm based on TruthValue"""


_Dot3ExtPkgOptIfTransmitAlarm_Object = MibTableColumn
dot3ExtPkgOptIfTransmitAlarm = _Dot3ExtPkgOptIfTransmitAlarm_Object(
    (1, 3, 6, 1, 2, 1, 155, 1, 4, 1, 5, 1, 13),
    _Dot3ExtPkgOptIfTransmitAlarm_Type()
)
dot3ExtPkgOptIfTransmitAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3ExtPkgOptIfTransmitAlarm.setStatus("current")


class _Dot3ExtPkgOptIfTransmitEnable_Type(TruthValue):
    """Custom type dot3ExtPkgOptIfTransmitEnable based on TruthValue"""


_Dot3ExtPkgOptIfTransmitEnable_Object = MibTableColumn
dot3ExtPkgOptIfTransmitEnable = _Dot3ExtPkgOptIfTransmitEnable_Object(
    (1, 3, 6, 1, 2, 1, 155, 1, 4, 1, 5, 1, 14),
    _Dot3ExtPkgOptIfTransmitEnable_Type()
)
dot3ExtPkgOptIfTransmitEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot3ExtPkgOptIfTransmitEnable.setStatus("current")
_Dot3EponConformance_ObjectIdentity = ObjectIdentity
dot3EponConformance = _Dot3EponConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 155, 2)
)
_Dot3EponGroups_ObjectIdentity = ObjectIdentity
dot3EponGroups = _Dot3EponGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 155, 2, 1)
)
_Dot3EponCompliances_ObjectIdentity = ObjectIdentity
dot3EponCompliances = _Dot3EponCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 155, 2, 2)
)

# Managed Objects groups

dot3MpcpGroupBase = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 155, 2, 1, 1)
)
dot3MpcpGroupBase.setObjects(
      *(("DOT3-EPON-MIB", "dot3MpcpOperStatus"),
        ("DOT3-EPON-MIB", "dot3MpcpAdminState"),
        ("DOT3-EPON-MIB", "dot3MpcpMode"),
        ("DOT3-EPON-MIB", "dot3MpcpSyncTime"),
        ("DOT3-EPON-MIB", "dot3MpcpLinkID"),
        ("DOT3-EPON-MIB", "dot3MpcpRemoteMACAddress"),
        ("DOT3-EPON-MIB", "dot3MpcpRegistrationState"),
        ("DOT3-EPON-MIB", "dot3MpcpMaximumPendingGrants"),
        ("DOT3-EPON-MIB", "dot3MpcpTransmitElapsed"),
        ("DOT3-EPON-MIB", "dot3MpcpReceiveElapsed"),
        ("DOT3-EPON-MIB", "dot3MpcpRoundTripTime"))
)
if mibBuilder.loadTexts:
    dot3MpcpGroupBase.setStatus("current")

dot3MpcpGroupStat = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 155, 2, 1, 2)
)
dot3MpcpGroupStat.setObjects(
      *(("DOT3-EPON-MIB", "dot3MpcpMACCtrlFramesTransmitted"),
        ("DOT3-EPON-MIB", "dot3MpcpMACCtrlFramesReceived"),
        ("DOT3-EPON-MIB", "dot3MpcpDiscoveryWindowsSent"),
        ("DOT3-EPON-MIB", "dot3MpcpDiscoveryTimeout"),
        ("DOT3-EPON-MIB", "dot3MpcpTxRegRequest"),
        ("DOT3-EPON-MIB", "dot3MpcpRxRegRequest"),
        ("DOT3-EPON-MIB", "dot3MpcpTxRegAck"),
        ("DOT3-EPON-MIB", "dot3MpcpRxRegAck"),
        ("DOT3-EPON-MIB", "dot3MpcpTxReport"),
        ("DOT3-EPON-MIB", "dot3MpcpRxReport"),
        ("DOT3-EPON-MIB", "dot3MpcpTxGate"),
        ("DOT3-EPON-MIB", "dot3MpcpRxGate"),
        ("DOT3-EPON-MIB", "dot3MpcpTxRegister"),
        ("DOT3-EPON-MIB", "dot3MpcpRxRegister"))
)
if mibBuilder.loadTexts:
    dot3MpcpGroupStat.setStatus("current")

dot3OmpeGroupID = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 155, 2, 1, 3)
)
dot3OmpeGroupID.setObjects(
    ("DOT3-EPON-MIB", "dot3OmpEmulationType")
)
if mibBuilder.loadTexts:
    dot3OmpeGroupID.setStatus("current")

dot3OmpeGroupStat = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 155, 2, 1, 4)
)
dot3OmpeGroupStat.setObjects(
      *(("DOT3-EPON-MIB", "dot3OmpEmulationSLDErrors"),
        ("DOT3-EPON-MIB", "dot3OmpEmulationCRC8Errors"),
        ("DOT3-EPON-MIB", "dot3OmpEmulationBadLLID"),
        ("DOT3-EPON-MIB", "dot3OmpEmulationGoodLLID"),
        ("DOT3-EPON-MIB", "dot3OmpEmulationOnuPonCastLLID"),
        ("DOT3-EPON-MIB", "dot3OmpEmulationOltPonCastLLID"),
        ("DOT3-EPON-MIB", "dot3OmpEmulationBroadcastBitNotOnuLlid"),
        ("DOT3-EPON-MIB", "dot3OmpEmulationOnuLLIDNotBroadcast"),
        ("DOT3-EPON-MIB", "dot3OmpEmulationBroadcastBitPlusOnuLlid"),
        ("DOT3-EPON-MIB", "dot3OmpEmulationNotBroadcastBitNotOnuLlid"))
)
if mibBuilder.loadTexts:
    dot3OmpeGroupStat.setStatus("current")

dot3EponFecGroupAll = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 155, 2, 1, 5)
)
dot3EponFecGroupAll.setObjects(
      *(("DOT3-EPON-MIB", "dot3EponFecPCSCodingViolation"),
        ("DOT3-EPON-MIB", "dot3EponFecAbility"),
        ("DOT3-EPON-MIB", "dot3EponFecMode"),
        ("DOT3-EPON-MIB", "dot3EponFecCorrectedBlocks"),
        ("DOT3-EPON-MIB", "dot3EponFecUncorrectableBlocks"),
        ("DOT3-EPON-MIB", "dot3EponFecBufferHeadCodingViolation"))
)
if mibBuilder.loadTexts:
    dot3EponFecGroupAll.setStatus("current")

dot3ExtPkgGroupControl = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 155, 2, 1, 6)
)
dot3ExtPkgGroupControl.setObjects(
      *(("DOT3-EPON-MIB", "dot3ExtPkgObjectReset"),
        ("DOT3-EPON-MIB", "dot3ExtPkgObjectPowerDown"),
        ("DOT3-EPON-MIB", "dot3ExtPkgObjectNumberOfLLIDs"),
        ("DOT3-EPON-MIB", "dot3ExtPkgObjectFecEnabled"),
        ("DOT3-EPON-MIB", "dot3ExtPkgObjectReportMaximumNumQueues"),
        ("DOT3-EPON-MIB", "dot3ExtPkgObjectRegisterAction"))
)
if mibBuilder.loadTexts:
    dot3ExtPkgGroupControl.setStatus("current")

dot3ExtPkgGroupQueue = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 155, 2, 1, 7)
)
dot3ExtPkgGroupQueue.setObjects(
      *(("DOT3-EPON-MIB", "dot3ExtPkgObjectReportNumThreshold"),
        ("DOT3-EPON-MIB", "dot3ExtPkgObjectReportMaximumNumThreshold"),
        ("DOT3-EPON-MIB", "dot3ExtPkgStatTxFramesQueue"),
        ("DOT3-EPON-MIB", "dot3ExtPkgStatRxFramesQueue"),
        ("DOT3-EPON-MIB", "dot3ExtPkgStatDroppedFramesQueue"))
)
if mibBuilder.loadTexts:
    dot3ExtPkgGroupQueue.setStatus("current")

dot3ExtPkgGroupQueueSets = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 155, 2, 1, 8)
)
dot3ExtPkgGroupQueueSets.setObjects(
    ("DOT3-EPON-MIB", "dot3ExtPkgObjectReportThreshold")
)
if mibBuilder.loadTexts:
    dot3ExtPkgGroupQueueSets.setStatus("current")

dot3ExtPkgGroupOptIf = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 155, 2, 1, 9)
)
dot3ExtPkgGroupOptIf.setObjects(
      *(("DOT3-EPON-MIB", "dot3ExtPkgOptIfSuspectedFlag"),
        ("DOT3-EPON-MIB", "dot3ExtPkgOptIfInputPower"),
        ("DOT3-EPON-MIB", "dot3ExtPkgOptIfLowInputPower"),
        ("DOT3-EPON-MIB", "dot3ExtPkgOptIfHighInputPower"),
        ("DOT3-EPON-MIB", "dot3ExtPkgOptIfLowerInputPowerThreshold"),
        ("DOT3-EPON-MIB", "dot3ExtPkgOptIfUpperInputPowerThreshold"),
        ("DOT3-EPON-MIB", "dot3ExtPkgOptIfOutputPower"),
        ("DOT3-EPON-MIB", "dot3ExtPkgOptIfLowOutputPower"),
        ("DOT3-EPON-MIB", "dot3ExtPkgOptIfHighOutputPower"),
        ("DOT3-EPON-MIB", "dot3ExtPkgOptIfLowerOutputPowerThreshold"),
        ("DOT3-EPON-MIB", "dot3ExtPkgOptIfUpperOutputPowerThreshold"),
        ("DOT3-EPON-MIB", "dot3ExtPkgOptIfSignalDetect"),
        ("DOT3-EPON-MIB", "dot3ExtPkgOptIfTransmitAlarm"),
        ("DOT3-EPON-MIB", "dot3ExtPkgOptIfTransmitEnable"))
)
if mibBuilder.loadTexts:
    dot3ExtPkgGroupOptIf.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

dot3MPCPCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 155, 2, 2, 1)
)
if mibBuilder.loadTexts:
    dot3MPCPCompliance.setStatus(
        "current"
    )

dot3OmpeCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 155, 2, 2, 2)
)
if mibBuilder.loadTexts:
    dot3OmpeCompliance.setStatus(
        "current"
    )

dot3EponFecCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 155, 2, 2, 3)
)
if mibBuilder.loadTexts:
    dot3EponFecCompliance.setStatus(
        "current"
    )

dot3ExtPkgCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 155, 2, 2, 4)
)
if mibBuilder.loadTexts:
    dot3ExtPkgCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DOT3-EPON-MIB",
    **{"dot3EponMIB": dot3EponMIB,
       "dot3EponObjects": dot3EponObjects,
       "dot3EponMpcpObjects": dot3EponMpcpObjects,
       "dot3MpcpControlTable": dot3MpcpControlTable,
       "dot3MpcpControlEntry": dot3MpcpControlEntry,
       "dot3MpcpOperStatus": dot3MpcpOperStatus,
       "dot3MpcpAdminState": dot3MpcpAdminState,
       "dot3MpcpMode": dot3MpcpMode,
       "dot3MpcpSyncTime": dot3MpcpSyncTime,
       "dot3MpcpLinkID": dot3MpcpLinkID,
       "dot3MpcpRemoteMACAddress": dot3MpcpRemoteMACAddress,
       "dot3MpcpRegistrationState": dot3MpcpRegistrationState,
       "dot3MpcpTransmitElapsed": dot3MpcpTransmitElapsed,
       "dot3MpcpReceiveElapsed": dot3MpcpReceiveElapsed,
       "dot3MpcpRoundTripTime": dot3MpcpRoundTripTime,
       "dot3MpcpMaximumPendingGrants": dot3MpcpMaximumPendingGrants,
       "dot3MpcpStatTable": dot3MpcpStatTable,
       "dot3MpcpStatEntry": dot3MpcpStatEntry,
       "dot3MpcpMACCtrlFramesTransmitted": dot3MpcpMACCtrlFramesTransmitted,
       "dot3MpcpMACCtrlFramesReceived": dot3MpcpMACCtrlFramesReceived,
       "dot3MpcpDiscoveryWindowsSent": dot3MpcpDiscoveryWindowsSent,
       "dot3MpcpDiscoveryTimeout": dot3MpcpDiscoveryTimeout,
       "dot3MpcpTxRegRequest": dot3MpcpTxRegRequest,
       "dot3MpcpRxRegRequest": dot3MpcpRxRegRequest,
       "dot3MpcpTxRegAck": dot3MpcpTxRegAck,
       "dot3MpcpRxRegAck": dot3MpcpRxRegAck,
       "dot3MpcpTxReport": dot3MpcpTxReport,
       "dot3MpcpRxReport": dot3MpcpRxReport,
       "dot3MpcpTxGate": dot3MpcpTxGate,
       "dot3MpcpRxGate": dot3MpcpRxGate,
       "dot3MpcpTxRegister": dot3MpcpTxRegister,
       "dot3MpcpRxRegister": dot3MpcpRxRegister,
       "dot3OmpEmulationObjects": dot3OmpEmulationObjects,
       "dot3OmpEmulationTable": dot3OmpEmulationTable,
       "dot3OmpEmulationEntry": dot3OmpEmulationEntry,
       "dot3OmpEmulationType": dot3OmpEmulationType,
       "dot3OmpEmulationStatTable": dot3OmpEmulationStatTable,
       "dot3OmpEmulationStatEntry": dot3OmpEmulationStatEntry,
       "dot3OmpEmulationSLDErrors": dot3OmpEmulationSLDErrors,
       "dot3OmpEmulationCRC8Errors": dot3OmpEmulationCRC8Errors,
       "dot3OmpEmulationBadLLID": dot3OmpEmulationBadLLID,
       "dot3OmpEmulationGoodLLID": dot3OmpEmulationGoodLLID,
       "dot3OmpEmulationOnuPonCastLLID": dot3OmpEmulationOnuPonCastLLID,
       "dot3OmpEmulationOltPonCastLLID": dot3OmpEmulationOltPonCastLLID,
       "dot3OmpEmulationBroadcastBitNotOnuLlid": dot3OmpEmulationBroadcastBitNotOnuLlid,
       "dot3OmpEmulationOnuLLIDNotBroadcast": dot3OmpEmulationOnuLLIDNotBroadcast,
       "dot3OmpEmulationBroadcastBitPlusOnuLlid": dot3OmpEmulationBroadcastBitPlusOnuLlid,
       "dot3OmpEmulationNotBroadcastBitNotOnuLlid": dot3OmpEmulationNotBroadcastBitNotOnuLlid,
       "dot3EponFecObjects": dot3EponFecObjects,
       "dot3EponFecTable": dot3EponFecTable,
       "dot3EponFecEntry": dot3EponFecEntry,
       "dot3EponFecPCSCodingViolation": dot3EponFecPCSCodingViolation,
       "dot3EponFecAbility": dot3EponFecAbility,
       "dot3EponFecMode": dot3EponFecMode,
       "dot3EponFecCorrectedBlocks": dot3EponFecCorrectedBlocks,
       "dot3EponFecUncorrectableBlocks": dot3EponFecUncorrectableBlocks,
       "dot3EponFecBufferHeadCodingViolation": dot3EponFecBufferHeadCodingViolation,
       "dot3ExtPkgObjects": dot3ExtPkgObjects,
       "dot3ExtPkgControlObjects": dot3ExtPkgControlObjects,
       "dot3ExtPkgControlTable": dot3ExtPkgControlTable,
       "dot3ExtPkgControlEntry": dot3ExtPkgControlEntry,
       "dot3ExtPkgObjectReset": dot3ExtPkgObjectReset,
       "dot3ExtPkgObjectPowerDown": dot3ExtPkgObjectPowerDown,
       "dot3ExtPkgObjectNumberOfLLIDs": dot3ExtPkgObjectNumberOfLLIDs,
       "dot3ExtPkgObjectFecEnabled": dot3ExtPkgObjectFecEnabled,
       "dot3ExtPkgObjectReportMaximumNumQueues": dot3ExtPkgObjectReportMaximumNumQueues,
       "dot3ExtPkgObjectRegisterAction": dot3ExtPkgObjectRegisterAction,
       "dot3ExtPkgQueueTable": dot3ExtPkgQueueTable,
       "dot3ExtPkgQueueEntry": dot3ExtPkgQueueEntry,
       "dot3QueueIndex": dot3QueueIndex,
       "dot3ExtPkgObjectReportNumThreshold": dot3ExtPkgObjectReportNumThreshold,
       "dot3ExtPkgObjectReportMaximumNumThreshold": dot3ExtPkgObjectReportMaximumNumThreshold,
       "dot3ExtPkgStatTxFramesQueue": dot3ExtPkgStatTxFramesQueue,
       "dot3ExtPkgStatRxFramesQueue": dot3ExtPkgStatRxFramesQueue,
       "dot3ExtPkgStatDroppedFramesQueue": dot3ExtPkgStatDroppedFramesQueue,
       "dot3ExtPkgQueueSetsTable": dot3ExtPkgQueueSetsTable,
       "dot3ExtPkgQueueSetsEntry": dot3ExtPkgQueueSetsEntry,
       "dot3QueueSetQueueIndex": dot3QueueSetQueueIndex,
       "dot3QueueSetIndex": dot3QueueSetIndex,
       "dot3ExtPkgObjectReportThreshold": dot3ExtPkgObjectReportThreshold,
       "dot3ExtPkgOptIfTable": dot3ExtPkgOptIfTable,
       "dot3ExtPkgOptIfEntry": dot3ExtPkgOptIfEntry,
       "dot3ExtPkgOptIfSuspectedFlag": dot3ExtPkgOptIfSuspectedFlag,
       "dot3ExtPkgOptIfInputPower": dot3ExtPkgOptIfInputPower,
       "dot3ExtPkgOptIfLowInputPower": dot3ExtPkgOptIfLowInputPower,
       "dot3ExtPkgOptIfHighInputPower": dot3ExtPkgOptIfHighInputPower,
       "dot3ExtPkgOptIfLowerInputPowerThreshold": dot3ExtPkgOptIfLowerInputPowerThreshold,
       "dot3ExtPkgOptIfUpperInputPowerThreshold": dot3ExtPkgOptIfUpperInputPowerThreshold,
       "dot3ExtPkgOptIfOutputPower": dot3ExtPkgOptIfOutputPower,
       "dot3ExtPkgOptIfLowOutputPower": dot3ExtPkgOptIfLowOutputPower,
       "dot3ExtPkgOptIfHighOutputPower": dot3ExtPkgOptIfHighOutputPower,
       "dot3ExtPkgOptIfLowerOutputPowerThreshold": dot3ExtPkgOptIfLowerOutputPowerThreshold,
       "dot3ExtPkgOptIfUpperOutputPowerThreshold": dot3ExtPkgOptIfUpperOutputPowerThreshold,
       "dot3ExtPkgOptIfSignalDetect": dot3ExtPkgOptIfSignalDetect,
       "dot3ExtPkgOptIfTransmitAlarm": dot3ExtPkgOptIfTransmitAlarm,
       "dot3ExtPkgOptIfTransmitEnable": dot3ExtPkgOptIfTransmitEnable,
       "dot3EponConformance": dot3EponConformance,
       "dot3EponGroups": dot3EponGroups,
       "dot3MpcpGroupBase": dot3MpcpGroupBase,
       "dot3MpcpGroupStat": dot3MpcpGroupStat,
       "dot3OmpeGroupID": dot3OmpeGroupID,
       "dot3OmpeGroupStat": dot3OmpeGroupStat,
       "dot3EponFecGroupAll": dot3EponFecGroupAll,
       "dot3ExtPkgGroupControl": dot3ExtPkgGroupControl,
       "dot3ExtPkgGroupQueue": dot3ExtPkgGroupQueue,
       "dot3ExtPkgGroupQueueSets": dot3ExtPkgGroupQueueSets,
       "dot3ExtPkgGroupOptIf": dot3ExtPkgGroupOptIf,
       "dot3EponCompliances": dot3EponCompliances,
       "dot3MPCPCompliance": dot3MPCPCompliance,
       "dot3OmpeCompliance": dot3OmpeCompliance,
       "dot3EponFecCompliance": dot3EponFecCompliance,
       "dot3ExtPkgCompliance": dot3ExtPkgCompliance}
)
