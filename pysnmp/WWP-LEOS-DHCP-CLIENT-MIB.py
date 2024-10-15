# SNMP MIB module (WWP-LEOS-DHCP-CLIENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WWP-LEOS-DHCP-CLIENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:14:49 2024
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

(DisplayString,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(wwpModulesLeos,) = mibBuilder.importSymbols(
    "WWP-SMI",
    "wwpModulesLeos")


# MODULE-IDENTITY

wwpLeosDhcpClientMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 17)
)
wwpLeosDhcpClientMIB.setRevisions(
        ("2006-04-18 17:00",
         "2002-11-01 17:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WwpLeosDhcpClientMIBObjects_ObjectIdentity = ObjectIdentity
wwpLeosDhcpClientMIBObjects = _WwpLeosDhcpClientMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 17, 1)
)
_WwpLeosDhcpClient_ObjectIdentity = ObjectIdentity
wwpLeosDhcpClient = _WwpLeosDhcpClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 17, 1, 1)
)


class _WwpLeosDhcpIfName_Type(DisplayString):
    """Custom type wwpLeosDhcpIfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_WwpLeosDhcpIfName_Type.__name__ = "DisplayString"
_WwpLeosDhcpIfName_Object = MibScalar
wwpLeosDhcpIfName = _WwpLeosDhcpIfName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 17, 1, 1, 1),
    _WwpLeosDhcpIfName_Type()
)
wwpLeosDhcpIfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosDhcpIfName.setStatus("current")


class _WwpLeosDhcpStatus_Type(Integer32):
    """Custom type wwpLeosDhcpStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_WwpLeosDhcpStatus_Type.__name__ = "Integer32"
_WwpLeosDhcpStatus_Object = MibScalar
wwpLeosDhcpStatus = _WwpLeosDhcpStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 17, 1, 1, 2),
    _WwpLeosDhcpStatus_Type()
)
wwpLeosDhcpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosDhcpStatus.setStatus("current")


class _WwpLeosDhcpState_Type(Integer32):
    """Custom type wwpLeosDhcpState based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("bound", 1),
          ("disabled", 2),
          ("inform", 3),
          ("init", 4),
          ("rebinding", 5),
          ("renewing", 6),
          ("requesting", 7),
          ("selecting", 8),
          ("unknown", 9))
    )


_WwpLeosDhcpState_Type.__name__ = "Integer32"
_WwpLeosDhcpState_Object = MibScalar
wwpLeosDhcpState = _WwpLeosDhcpState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 17, 1, 1, 3),
    _WwpLeosDhcpState_Type()
)
wwpLeosDhcpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosDhcpState.setStatus("current")


class _WwpLeosDhcpLeaseOffered_Type(Integer32):
    """Custom type wwpLeosDhcpLeaseOffered based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WwpLeosDhcpLeaseOffered_Type.__name__ = "Integer32"
_WwpLeosDhcpLeaseOffered_Object = MibScalar
wwpLeosDhcpLeaseOffered = _WwpLeosDhcpLeaseOffered_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 17, 1, 1, 5),
    _WwpLeosDhcpLeaseOffered_Type()
)
wwpLeosDhcpLeaseOffered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosDhcpLeaseOffered.setStatus("current")
if mibBuilder.loadTexts:
    wwpLeosDhcpLeaseOffered.setUnits("seconds")


class _WwpLeosDhcpLeaseRemaining_Type(Integer32):
    """Custom type wwpLeosDhcpLeaseRemaining based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WwpLeosDhcpLeaseRemaining_Type.__name__ = "Integer32"
_WwpLeosDhcpLeaseRemaining_Object = MibScalar
wwpLeosDhcpLeaseRemaining = _WwpLeosDhcpLeaseRemaining_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 17, 1, 1, 6),
    _WwpLeosDhcpLeaseRemaining_Type()
)
wwpLeosDhcpLeaseRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosDhcpLeaseRemaining.setStatus("current")
if mibBuilder.loadTexts:
    wwpLeosDhcpLeaseRemaining.setUnits("seconds")


class _WwpLeosDhcpDiscoveryMsgInterval_Type(Integer32):
    """Custom type wwpLeosDhcpDiscoveryMsgInterval based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WwpLeosDhcpDiscoveryMsgInterval_Type.__name__ = "Integer32"
_WwpLeosDhcpDiscoveryMsgInterval_Object = MibScalar
wwpLeosDhcpDiscoveryMsgInterval = _WwpLeosDhcpDiscoveryMsgInterval_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 17, 1, 1, 7),
    _WwpLeosDhcpDiscoveryMsgInterval_Type()
)
wwpLeosDhcpDiscoveryMsgInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosDhcpDiscoveryMsgInterval.setStatus("current")
if mibBuilder.loadTexts:
    wwpLeosDhcpDiscoveryMsgInterval.setUnits("seconds")


class _WwpLeosDhcpRenewalTime_Type(Integer32):
    """Custom type wwpLeosDhcpRenewalTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WwpLeosDhcpRenewalTime_Type.__name__ = "Integer32"
_WwpLeosDhcpRenewalTime_Object = MibScalar
wwpLeosDhcpRenewalTime = _WwpLeosDhcpRenewalTime_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 17, 1, 1, 8),
    _WwpLeosDhcpRenewalTime_Type()
)
wwpLeosDhcpRenewalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosDhcpRenewalTime.setStatus("current")
if mibBuilder.loadTexts:
    wwpLeosDhcpRenewalTime.setUnits("seconds")


class _WwpLeosDhcpRebindingTime_Type(Integer32):
    """Custom type wwpLeosDhcpRebindingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WwpLeosDhcpRebindingTime_Type.__name__ = "Integer32"
_WwpLeosDhcpRebindingTime_Object = MibScalar
wwpLeosDhcpRebindingTime = _WwpLeosDhcpRebindingTime_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 17, 1, 1, 9),
    _WwpLeosDhcpRebindingTime_Type()
)
wwpLeosDhcpRebindingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosDhcpRebindingTime.setStatus("current")
if mibBuilder.loadTexts:
    wwpLeosDhcpRebindingTime.setUnits("seconds")
_WwpLeosDhcpServerAddress_Type = IpAddress
_WwpLeosDhcpServerAddress_Object = MibScalar
wwpLeosDhcpServerAddress = _WwpLeosDhcpServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 17, 1, 1, 10),
    _WwpLeosDhcpServerAddress_Type()
)
wwpLeosDhcpServerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosDhcpServerAddress.setStatus("current")


class _WwpLeosDhcpRenewLease_Type(TruthValue):
    """Custom type wwpLeosDhcpRenewLease based on TruthValue"""


_WwpLeosDhcpRenewLease_Object = MibScalar
wwpLeosDhcpRenewLease = _WwpLeosDhcpRenewLease_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 17, 1, 1, 11),
    _WwpLeosDhcpRenewLease_Type()
)
wwpLeosDhcpRenewLease.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosDhcpRenewLease.setStatus("current")


class _WwpLeosDhcpReleaseLease_Type(TruthValue):
    """Custom type wwpLeosDhcpReleaseLease based on TruthValue"""


_WwpLeosDhcpReleaseLease_Object = MibScalar
wwpLeosDhcpReleaseLease = _WwpLeosDhcpReleaseLease_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 17, 1, 1, 12),
    _WwpLeosDhcpReleaseLease_Type()
)
wwpLeosDhcpReleaseLease.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosDhcpReleaseLease.setStatus("current")
_WwpLeosDhcpClientOptionTable_Object = MibTable
wwpLeosDhcpClientOptionTable = _WwpLeosDhcpClientOptionTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 17, 1, 1, 13)
)
if mibBuilder.loadTexts:
    wwpLeosDhcpClientOptionTable.setStatus("current")
_WwpLeosDhcpClientOptionEntry_Object = MibTableRow
wwpLeosDhcpClientOptionEntry = _WwpLeosDhcpClientOptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 17, 1, 1, 13, 1)
)
wwpLeosDhcpClientOptionEntry.setIndexNames(
    (0, "WWP-LEOS-DHCP-CLIENT-MIB", "wwpLeosDhcpOptionCodeIndex"),
)
if mibBuilder.loadTexts:
    wwpLeosDhcpClientOptionEntry.setStatus("current")


class _WwpLeosDhcpOptionCodeIndex_Type(Integer32):
    """Custom type wwpLeosDhcpOptionCodeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosDhcpOptionCodeIndex_Type.__name__ = "Integer32"
_WwpLeosDhcpOptionCodeIndex_Object = MibTableColumn
wwpLeosDhcpOptionCodeIndex = _WwpLeosDhcpOptionCodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 17, 1, 1, 13, 1, 1),
    _WwpLeosDhcpOptionCodeIndex_Type()
)
wwpLeosDhcpOptionCodeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosDhcpOptionCodeIndex.setStatus("current")
_WwpLeosDhcpOptionDesc_Type = DisplayString
_WwpLeosDhcpOptionDesc_Object = MibTableColumn
wwpLeosDhcpOptionDesc = _WwpLeosDhcpOptionDesc_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 17, 1, 1, 13, 1, 2),
    _WwpLeosDhcpOptionDesc_Type()
)
wwpLeosDhcpOptionDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosDhcpOptionDesc.setStatus("current")


class _WwpLeosDhcpOptionCode_Type(Integer32):
    """Custom type wwpLeosDhcpOptionCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WwpLeosDhcpOptionCode_Type.__name__ = "Integer32"
_WwpLeosDhcpOptionCode_Object = MibTableColumn
wwpLeosDhcpOptionCode = _WwpLeosDhcpOptionCode_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 17, 1, 1, 13, 1, 3),
    _WwpLeosDhcpOptionCode_Type()
)
wwpLeosDhcpOptionCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosDhcpOptionCode.setStatus("current")


class _WwpLeosDhcpOptionState_Type(Integer32):
    """Custom type wwpLeosDhcpOptionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_WwpLeosDhcpOptionState_Type.__name__ = "Integer32"
_WwpLeosDhcpOptionState_Object = MibTableColumn
wwpLeosDhcpOptionState = _WwpLeosDhcpOptionState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 17, 1, 1, 13, 1, 4),
    _WwpLeosDhcpOptionState_Type()
)
wwpLeosDhcpOptionState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosDhcpOptionState.setStatus("current")
_WwpLeosDhcpRelayAgent_ObjectIdentity = ObjectIdentity
wwpLeosDhcpRelayAgent = _WwpLeosDhcpRelayAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 17, 1, 2)
)
_WwpLeosDhcpRelayAgentGlobalAttrs_ObjectIdentity = ObjectIdentity
wwpLeosDhcpRelayAgentGlobalAttrs = _WwpLeosDhcpRelayAgentGlobalAttrs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 17, 1, 2, 1)
)


class _WwpLeosDhcpRelayAgentCircuitId_Type(Integer32):
    """Custom type wwpLeosDhcpRelayAgentCircuitId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cidString", 3),
          ("slotAndPort", 1),
          ("slotAndPortAndVlan", 2))
    )


_WwpLeosDhcpRelayAgentCircuitId_Type.__name__ = "Integer32"
_WwpLeosDhcpRelayAgentCircuitId_Object = MibScalar
wwpLeosDhcpRelayAgentCircuitId = _WwpLeosDhcpRelayAgentCircuitId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 17, 1, 2, 1, 1),
    _WwpLeosDhcpRelayAgentCircuitId_Type()
)
wwpLeosDhcpRelayAgentCircuitId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosDhcpRelayAgentCircuitId.setStatus("current")


class _WwpLeosDhcpRelayAgentRemoteId_Type(Integer32):
    """Custom type wwpLeosDhcpRelayAgentRemoteId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hostName", 2),
          ("macAddress", 1))
    )


_WwpLeosDhcpRelayAgentRemoteId_Type.__name__ = "Integer32"
_WwpLeosDhcpRelayAgentRemoteId_Object = MibScalar
wwpLeosDhcpRelayAgentRemoteId = _WwpLeosDhcpRelayAgentRemoteId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 17, 1, 2, 1, 2),
    _WwpLeosDhcpRelayAgentRemoteId_Type()
)
wwpLeosDhcpRelayAgentRemoteId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosDhcpRelayAgentRemoteId.setStatus("current")


class _WwpLeosDhcpRelayAgentL2State_Type(Integer32):
    """Custom type wwpLeosDhcpRelayAgentL2State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_WwpLeosDhcpRelayAgentL2State_Type.__name__ = "Integer32"
_WwpLeosDhcpRelayAgentL2State_Object = MibScalar
wwpLeosDhcpRelayAgentL2State = _WwpLeosDhcpRelayAgentL2State_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 17, 1, 2, 1, 3),
    _WwpLeosDhcpRelayAgentL2State_Type()
)
wwpLeosDhcpRelayAgentL2State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosDhcpRelayAgentL2State.setStatus("current")


class _WwpLeosDhcpRelayAgentL3State_Type(Integer32):
    """Custom type wwpLeosDhcpRelayAgentL3State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_WwpLeosDhcpRelayAgentL3State_Type.__name__ = "Integer32"
_WwpLeosDhcpRelayAgentL3State_Object = MibScalar
wwpLeosDhcpRelayAgentL3State = _WwpLeosDhcpRelayAgentL3State_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 17, 1, 2, 1, 4),
    _WwpLeosDhcpRelayAgentL3State_Type()
)
wwpLeosDhcpRelayAgentL3State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosDhcpRelayAgentL3State.setStatus("current")
_WwpLeosDhcpRelayAgentL2StateTable_Object = MibTable
wwpLeosDhcpRelayAgentL2StateTable = _WwpLeosDhcpRelayAgentL2StateTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 17, 1, 2, 2)
)
if mibBuilder.loadTexts:
    wwpLeosDhcpRelayAgentL2StateTable.setStatus("current")
_WwpLeosDhcpRelayAgentL2StateEntry_Object = MibTableRow
wwpLeosDhcpRelayAgentL2StateEntry = _WwpLeosDhcpRelayAgentL2StateEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 17, 1, 2, 2, 1)
)
wwpLeosDhcpRelayAgentL2StateEntry.setIndexNames(
    (0, "WWP-LEOS-DHCP-CLIENT-MIB", "wwpLeosDhcpRelayAgentVlan"),
)
if mibBuilder.loadTexts:
    wwpLeosDhcpRelayAgentL2StateEntry.setStatus("current")


class _WwpLeosDhcpRelayAgentVlan_Type(Integer32):
    """Custom type wwpLeosDhcpRelayAgentVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24576),
    )


_WwpLeosDhcpRelayAgentVlan_Type.__name__ = "Integer32"
_WwpLeosDhcpRelayAgentVlan_Object = MibTableColumn
wwpLeosDhcpRelayAgentVlan = _WwpLeosDhcpRelayAgentVlan_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 17, 1, 2, 2, 1, 1),
    _WwpLeosDhcpRelayAgentVlan_Type()
)
wwpLeosDhcpRelayAgentVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosDhcpRelayAgentVlan.setStatus("current")


class _WwpLeosDhcpRelayAgentL2AdminState_Type(Integer32):
    """Custom type wwpLeosDhcpRelayAgentL2AdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_WwpLeosDhcpRelayAgentL2AdminState_Type.__name__ = "Integer32"
_WwpLeosDhcpRelayAgentL2AdminState_Object = MibTableColumn
wwpLeosDhcpRelayAgentL2AdminState = _WwpLeosDhcpRelayAgentL2AdminState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 17, 1, 2, 2, 1, 2),
    _WwpLeosDhcpRelayAgentL2AdminState_Type()
)
wwpLeosDhcpRelayAgentL2AdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosDhcpRelayAgentL2AdminState.setStatus("current")


class _WwpLeosDhcpRelayAgentL2OperState_Type(Integer32):
    """Custom type wwpLeosDhcpRelayAgentL2OperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_WwpLeosDhcpRelayAgentL2OperState_Type.__name__ = "Integer32"
_WwpLeosDhcpRelayAgentL2OperState_Object = MibTableColumn
wwpLeosDhcpRelayAgentL2OperState = _WwpLeosDhcpRelayAgentL2OperState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 17, 1, 2, 2, 1, 3),
    _WwpLeosDhcpRelayAgentL2OperState_Type()
)
wwpLeosDhcpRelayAgentL2OperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosDhcpRelayAgentL2OperState.setStatus("current")
_WwpLeosDhcpRelayAgentL2StatsClear_Type = TruthValue
_WwpLeosDhcpRelayAgentL2StatsClear_Object = MibTableColumn
wwpLeosDhcpRelayAgentL2StatsClear = _WwpLeosDhcpRelayAgentL2StatsClear_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 17, 1, 2, 2, 1, 4),
    _WwpLeosDhcpRelayAgentL2StatsClear_Type()
)
wwpLeosDhcpRelayAgentL2StatsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosDhcpRelayAgentL2StatsClear.setStatus("current")
_WwpLeosDhcpRelayAgentL2RowStatus_Type = RowStatus
_WwpLeosDhcpRelayAgentL2RowStatus_Object = MibTableColumn
wwpLeosDhcpRelayAgentL2RowStatus = _WwpLeosDhcpRelayAgentL2RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 17, 1, 2, 2, 1, 5),
    _WwpLeosDhcpRelayAgentL2RowStatus_Type()
)
wwpLeosDhcpRelayAgentL2RowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosDhcpRelayAgentL2RowStatus.setStatus("current")
_WwpLeosDhcpRelayAgentL3StateTable_Object = MibTable
wwpLeosDhcpRelayAgentL3StateTable = _WwpLeosDhcpRelayAgentL3StateTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 17, 1, 2, 3)
)
if mibBuilder.loadTexts:
    wwpLeosDhcpRelayAgentL3StateTable.setStatus("current")
_WwpLeosDhcpRelayAgentL3StateEntry_Object = MibTableRow
wwpLeosDhcpRelayAgentL3StateEntry = _WwpLeosDhcpRelayAgentL3StateEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 17, 1, 2, 3, 1)
)
wwpLeosDhcpRelayAgentL3StateEntry.setIndexNames(
    (0, "WWP-LEOS-DHCP-CLIENT-MIB", "wwpLeosDhcpRelayAgentInterfaceIndex"),
)
if mibBuilder.loadTexts:
    wwpLeosDhcpRelayAgentL3StateEntry.setStatus("current")


class _WwpLeosDhcpRelayAgentInterfaceIndex_Type(Integer32):
    """Custom type wwpLeosDhcpRelayAgentInterfaceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosDhcpRelayAgentInterfaceIndex_Type.__name__ = "Integer32"
_WwpLeosDhcpRelayAgentInterfaceIndex_Object = MibTableColumn
wwpLeosDhcpRelayAgentInterfaceIndex = _WwpLeosDhcpRelayAgentInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 17, 1, 2, 3, 1, 1),
    _WwpLeosDhcpRelayAgentInterfaceIndex_Type()
)
wwpLeosDhcpRelayAgentInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosDhcpRelayAgentInterfaceIndex.setStatus("current")


class _WwpLeosDhcpRelayAgentL3AdminState_Type(Integer32):
    """Custom type wwpLeosDhcpRelayAgentL3AdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_WwpLeosDhcpRelayAgentL3AdminState_Type.__name__ = "Integer32"
_WwpLeosDhcpRelayAgentL3AdminState_Object = MibTableColumn
wwpLeosDhcpRelayAgentL3AdminState = _WwpLeosDhcpRelayAgentL3AdminState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 17, 1, 2, 3, 1, 2),
    _WwpLeosDhcpRelayAgentL3AdminState_Type()
)
wwpLeosDhcpRelayAgentL3AdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosDhcpRelayAgentL3AdminState.setStatus("current")


class _WwpLeosDhcpRelayAgentL3OperState_Type(Integer32):
    """Custom type wwpLeosDhcpRelayAgentL3OperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_WwpLeosDhcpRelayAgentL3OperState_Type.__name__ = "Integer32"
_WwpLeosDhcpRelayAgentL3OperState_Object = MibTableColumn
wwpLeosDhcpRelayAgentL3OperState = _WwpLeosDhcpRelayAgentL3OperState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 17, 1, 2, 3, 1, 3),
    _WwpLeosDhcpRelayAgentL3OperState_Type()
)
wwpLeosDhcpRelayAgentL3OperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosDhcpRelayAgentL3OperState.setStatus("current")
_WwpLeosDhcpRelayAgentL3RowStatus_Type = RowStatus
_WwpLeosDhcpRelayAgentL3RowStatus_Object = MibTableColumn
wwpLeosDhcpRelayAgentL3RowStatus = _WwpLeosDhcpRelayAgentL3RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 17, 1, 2, 3, 1, 4),
    _WwpLeosDhcpRelayAgentL3RowStatus_Type()
)
wwpLeosDhcpRelayAgentL3RowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosDhcpRelayAgentL3RowStatus.setStatus("current")
_WwpLeosDhcpRelayAgentInterfaceIpTable_Object = MibTable
wwpLeosDhcpRelayAgentInterfaceIpTable = _WwpLeosDhcpRelayAgentInterfaceIpTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 17, 1, 2, 4)
)
if mibBuilder.loadTexts:
    wwpLeosDhcpRelayAgentInterfaceIpTable.setStatus("current")
_WwpLeosDhcpRelayAgentInterfaceIpEntry_Object = MibTableRow
wwpLeosDhcpRelayAgentInterfaceIpEntry = _WwpLeosDhcpRelayAgentInterfaceIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 17, 1, 2, 4, 1)
)
wwpLeosDhcpRelayAgentInterfaceIpEntry.setIndexNames(
    (0, "WWP-LEOS-DHCP-CLIENT-MIB", "wwpLeosDhcpRelayAgentInterfaceIpIndex"),
)
if mibBuilder.loadTexts:
    wwpLeosDhcpRelayAgentInterfaceIpEntry.setStatus("current")


class _WwpLeosDhcpRelayAgentInterfaceIpIndex_Type(Integer32):
    """Custom type wwpLeosDhcpRelayAgentInterfaceIpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_WwpLeosDhcpRelayAgentInterfaceIpIndex_Type.__name__ = "Integer32"
_WwpLeosDhcpRelayAgentInterfaceIpIndex_Object = MibTableColumn
wwpLeosDhcpRelayAgentInterfaceIpIndex = _WwpLeosDhcpRelayAgentInterfaceIpIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 17, 1, 2, 4, 1, 1),
    _WwpLeosDhcpRelayAgentInterfaceIpIndex_Type()
)
wwpLeosDhcpRelayAgentInterfaceIpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosDhcpRelayAgentInterfaceIpIndex.setStatus("current")
_WwpLeosDhcpRelayAgentInterfaceIpAddr_Type = IpAddress
_WwpLeosDhcpRelayAgentInterfaceIpAddr_Object = MibTableColumn
wwpLeosDhcpRelayAgentInterfaceIpAddr = _WwpLeosDhcpRelayAgentInterfaceIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 17, 1, 2, 4, 1, 2),
    _WwpLeosDhcpRelayAgentInterfaceIpAddr_Type()
)
wwpLeosDhcpRelayAgentInterfaceIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosDhcpRelayAgentInterfaceIpAddr.setStatus("current")
_WwpLeosDhcpRelayAgentInterfaceIpRowStatus_Type = RowStatus
_WwpLeosDhcpRelayAgentInterfaceIpRowStatus_Object = MibTableColumn
wwpLeosDhcpRelayAgentInterfaceIpRowStatus = _WwpLeosDhcpRelayAgentInterfaceIpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 17, 1, 2, 4, 1, 3),
    _WwpLeosDhcpRelayAgentInterfaceIpRowStatus_Type()
)
wwpLeosDhcpRelayAgentInterfaceIpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosDhcpRelayAgentInterfaceIpRowStatus.setStatus("current")
_WwpLeosDhcpRelayAgentTrustTable_Object = MibTable
wwpLeosDhcpRelayAgentTrustTable = _WwpLeosDhcpRelayAgentTrustTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 17, 1, 2, 5)
)
if mibBuilder.loadTexts:
    wwpLeosDhcpRelayAgentTrustTable.setStatus("current")
_WwpLeosDhcpRelayAgentTrustEntry_Object = MibTableRow
wwpLeosDhcpRelayAgentTrustEntry = _WwpLeosDhcpRelayAgentTrustEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 17, 1, 2, 5, 1)
)
wwpLeosDhcpRelayAgentTrustEntry.setIndexNames(
    (0, "WWP-LEOS-DHCP-CLIENT-MIB", "wwpLeosDhcpRelayAgentVlan"),
    (0, "WWP-LEOS-DHCP-CLIENT-MIB", "wwpLeosDhcpRelayAgentPort"),
)
if mibBuilder.loadTexts:
    wwpLeosDhcpRelayAgentTrustEntry.setStatus("current")


class _WwpLeosDhcpRelayAgentPort_Type(Integer32):
    """Custom type wwpLeosDhcpRelayAgentPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosDhcpRelayAgentPort_Type.__name__ = "Integer32"
_WwpLeosDhcpRelayAgentPort_Object = MibTableColumn
wwpLeosDhcpRelayAgentPort = _WwpLeosDhcpRelayAgentPort_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 17, 1, 2, 5, 1, 1),
    _WwpLeosDhcpRelayAgentPort_Type()
)
wwpLeosDhcpRelayAgentPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosDhcpRelayAgentPort.setStatus("current")


class _WwpLeosDhcpRelayAgentTrustMode_Type(Integer32):
    """Custom type wwpLeosDhcpRelayAgentTrustMode based on Integer32"""
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
        *(("clientTrust", 1),
          ("dualRoleTrust", 3),
          ("serverTrust", 2),
          ("unTrust", 4))
    )


_WwpLeosDhcpRelayAgentTrustMode_Type.__name__ = "Integer32"
_WwpLeosDhcpRelayAgentTrustMode_Object = MibTableColumn
wwpLeosDhcpRelayAgentTrustMode = _WwpLeosDhcpRelayAgentTrustMode_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 17, 1, 2, 5, 1, 2),
    _WwpLeosDhcpRelayAgentTrustMode_Type()
)
wwpLeosDhcpRelayAgentTrustMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosDhcpRelayAgentTrustMode.setStatus("current")
_WwpLeosDhcpRelayAgentL2StatsTable_Object = MibTable
wwpLeosDhcpRelayAgentL2StatsTable = _WwpLeosDhcpRelayAgentL2StatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 17, 1, 2, 6)
)
if mibBuilder.loadTexts:
    wwpLeosDhcpRelayAgentL2StatsTable.setStatus("current")
_WwpLeosDhcpRelayAgentL2StatsEntry_Object = MibTableRow
wwpLeosDhcpRelayAgentL2StatsEntry = _WwpLeosDhcpRelayAgentL2StatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 17, 1, 2, 6, 1)
)
wwpLeosDhcpRelayAgentL2StatsEntry.setIndexNames(
    (0, "WWP-LEOS-DHCP-CLIENT-MIB", "wwpLeosDhcpRelayAgentVlan"),
)
if mibBuilder.loadTexts:
    wwpLeosDhcpRelayAgentL2StatsEntry.setStatus("current")
_WwpLeosDhcpRelayAgentL2IpSecHeaders_Type = Counter32
_WwpLeosDhcpRelayAgentL2IpSecHeaders_Object = MibTableColumn
wwpLeosDhcpRelayAgentL2IpSecHeaders = _WwpLeosDhcpRelayAgentL2IpSecHeaders_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 17, 1, 2, 6, 1, 1),
    _WwpLeosDhcpRelayAgentL2IpSecHeaders_Type()
)
wwpLeosDhcpRelayAgentL2IpSecHeaders.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosDhcpRelayAgentL2IpSecHeaders.setStatus("current")
_WwpLeosDhcpRelayAgentL2Option82Added_Type = Counter32
_WwpLeosDhcpRelayAgentL2Option82Added_Object = MibTableColumn
wwpLeosDhcpRelayAgentL2Option82Added = _WwpLeosDhcpRelayAgentL2Option82Added_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 17, 1, 2, 6, 1, 2),
    _WwpLeosDhcpRelayAgentL2Option82Added_Type()
)
wwpLeosDhcpRelayAgentL2Option82Added.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosDhcpRelayAgentL2Option82Added.setStatus("current")
_WwpLeosDhcpRelayAgentL2Option82Removed_Type = Counter32
_WwpLeosDhcpRelayAgentL2Option82Removed_Object = MibTableColumn
wwpLeosDhcpRelayAgentL2Option82Removed = _WwpLeosDhcpRelayAgentL2Option82Removed_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 17, 1, 2, 6, 1, 3),
    _WwpLeosDhcpRelayAgentL2Option82Removed_Type()
)
wwpLeosDhcpRelayAgentL2Option82Removed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosDhcpRelayAgentL2Option82Removed.setStatus("current")
_WwpLeosDhcpRelayAgentL2UntrustedClientPortPktsRx_Type = Counter32
_WwpLeosDhcpRelayAgentL2UntrustedClientPortPktsRx_Object = MibTableColumn
wwpLeosDhcpRelayAgentL2UntrustedClientPortPktsRx = _WwpLeosDhcpRelayAgentL2UntrustedClientPortPktsRx_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 17, 1, 2, 6, 1, 4),
    _WwpLeosDhcpRelayAgentL2UntrustedClientPortPktsRx_Type()
)
wwpLeosDhcpRelayAgentL2UntrustedClientPortPktsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosDhcpRelayAgentL2UntrustedClientPortPktsRx.setStatus("current")
_WwpLeosDhcpRelayAgentL2UntrustedServerPortPktsRx_Type = Counter32
_WwpLeosDhcpRelayAgentL2UntrustedServerPortPktsRx_Object = MibTableColumn
wwpLeosDhcpRelayAgentL2UntrustedServerPortPktsRx = _WwpLeosDhcpRelayAgentL2UntrustedServerPortPktsRx_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 17, 1, 2, 6, 1, 5),
    _WwpLeosDhcpRelayAgentL2UntrustedServerPortPktsRx_Type()
)
wwpLeosDhcpRelayAgentL2UntrustedServerPortPktsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosDhcpRelayAgentL2UntrustedServerPortPktsRx.setStatus("current")
_WwpLeosDhcpRelayAgentL2SpoofedDhcpPkts_Type = Counter32
_WwpLeosDhcpRelayAgentL2SpoofedDhcpPkts_Object = MibTableColumn
wwpLeosDhcpRelayAgentL2SpoofedDhcpPkts = _WwpLeosDhcpRelayAgentL2SpoofedDhcpPkts_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 17, 1, 2, 6, 1, 6),
    _WwpLeosDhcpRelayAgentL2SpoofedDhcpPkts_Type()
)
wwpLeosDhcpRelayAgentL2SpoofedDhcpPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosDhcpRelayAgentL2SpoofedDhcpPkts.setStatus("current")
_WwpLeosDhcpRelayAgentL2Option82ExceedMTU_Type = Counter32
_WwpLeosDhcpRelayAgentL2Option82ExceedMTU_Object = MibTableColumn
wwpLeosDhcpRelayAgentL2Option82ExceedMTU = _WwpLeosDhcpRelayAgentL2Option82ExceedMTU_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 17, 1, 2, 6, 1, 7),
    _WwpLeosDhcpRelayAgentL2Option82ExceedMTU_Type()
)
wwpLeosDhcpRelayAgentL2Option82ExceedMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosDhcpRelayAgentL2Option82ExceedMTU.setStatus("current")
_WwpLeosDhcpRelayAgentL2NoTrustedServerPktDrop_Type = Counter32
_WwpLeosDhcpRelayAgentL2NoTrustedServerPktDrop_Object = MibTableColumn
wwpLeosDhcpRelayAgentL2NoTrustedServerPktDrop = _WwpLeosDhcpRelayAgentL2NoTrustedServerPktDrop_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 17, 1, 2, 6, 1, 8),
    _WwpLeosDhcpRelayAgentL2NoTrustedServerPktDrop_Type()
)
wwpLeosDhcpRelayAgentL2NoTrustedServerPktDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosDhcpRelayAgentL2NoTrustedServerPktDrop.setStatus("current")
_WwpLeosDhcpRelayAgentL2NoTrustedClientPktDrop_Type = Counter32
_WwpLeosDhcpRelayAgentL2NoTrustedClientPktDrop_Object = MibTableColumn
wwpLeosDhcpRelayAgentL2NoTrustedClientPktDrop = _WwpLeosDhcpRelayAgentL2NoTrustedClientPktDrop_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 17, 1, 2, 6, 1, 9),
    _WwpLeosDhcpRelayAgentL2NoTrustedClientPktDrop_Type()
)
wwpLeosDhcpRelayAgentL2NoTrustedClientPktDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosDhcpRelayAgentL2NoTrustedClientPktDrop.setStatus("current")
_WwpLeosDhcpRelayAgentCidStringTable_Object = MibTable
wwpLeosDhcpRelayAgentCidStringTable = _WwpLeosDhcpRelayAgentCidStringTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 17, 1, 2, 7)
)
if mibBuilder.loadTexts:
    wwpLeosDhcpRelayAgentCidStringTable.setStatus("current")
_WwpLeosDhcpRelayAgentCidStringEntry_Object = MibTableRow
wwpLeosDhcpRelayAgentCidStringEntry = _WwpLeosDhcpRelayAgentCidStringEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 17, 1, 2, 7, 1)
)
wwpLeosDhcpRelayAgentCidStringEntry.setIndexNames(
    (0, "WWP-LEOS-DHCP-CLIENT-MIB", "wwpLeosDhcpRelayAgentVlan"),
    (0, "WWP-LEOS-DHCP-CLIENT-MIB", "wwpLeosDhcpRelayAgentCidStringPort"),
)
if mibBuilder.loadTexts:
    wwpLeosDhcpRelayAgentCidStringEntry.setStatus("current")


class _WwpLeosDhcpRelayAgentCidStringPort_Type(Integer32):
    """Custom type wwpLeosDhcpRelayAgentCidStringPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosDhcpRelayAgentCidStringPort_Type.__name__ = "Integer32"
_WwpLeosDhcpRelayAgentCidStringPort_Object = MibTableColumn
wwpLeosDhcpRelayAgentCidStringPort = _WwpLeosDhcpRelayAgentCidStringPort_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 17, 1, 2, 7, 1, 1),
    _WwpLeosDhcpRelayAgentCidStringPort_Type()
)
wwpLeosDhcpRelayAgentCidStringPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosDhcpRelayAgentCidStringPort.setStatus("current")
_WwpLeosDhcpRelayAgentCidString_Type = DisplayString
_WwpLeosDhcpRelayAgentCidString_Object = MibTableColumn
wwpLeosDhcpRelayAgentCidString = _WwpLeosDhcpRelayAgentCidString_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 17, 1, 2, 7, 1, 2),
    _WwpLeosDhcpRelayAgentCidString_Type()
)
wwpLeosDhcpRelayAgentCidString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosDhcpRelayAgentCidString.setStatus("current")
_WwpLeosDhcpRelayAgentCidStringRowStatus_Type = RowStatus
_WwpLeosDhcpRelayAgentCidStringRowStatus_Object = MibTableColumn
wwpLeosDhcpRelayAgentCidStringRowStatus = _WwpLeosDhcpRelayAgentCidStringRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 17, 1, 2, 7, 1, 3),
    _WwpLeosDhcpRelayAgentCidStringRowStatus_Type()
)
wwpLeosDhcpRelayAgentCidStringRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosDhcpRelayAgentCidStringRowStatus.setStatus("current")
_WwpLeosDhcpClientMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
wwpLeosDhcpClientMIBNotificationPrefix = _WwpLeosDhcpClientMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 17, 2)
)
_WwpLeosDhcpClientMIBNotifications_ObjectIdentity = ObjectIdentity
wwpLeosDhcpClientMIBNotifications = _WwpLeosDhcpClientMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 17, 2, 0)
)
_WwpLeosDhcpClientMIBConformance_ObjectIdentity = ObjectIdentity
wwpLeosDhcpClientMIBConformance = _WwpLeosDhcpClientMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 17, 3)
)
_WwpLeosDhcpClientMIBCompliances_ObjectIdentity = ObjectIdentity
wwpLeosDhcpClientMIBCompliances = _WwpLeosDhcpClientMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 17, 3, 1)
)
_WwpLeosDhcpClientMIBGroups_ObjectIdentity = ObjectIdentity
wwpLeosDhcpClientMIBGroups = _WwpLeosDhcpClientMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 17, 3, 2)
)

# Managed Objects groups


# Notification objects

wwpLeosDhcpClientOptionDisabledNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 17, 2, 0, 1)
)
wwpLeosDhcpClientOptionDisabledNotification.setObjects(
    ("WWP-LEOS-DHCP-CLIENT-MIB", "wwpLeosDhcpOptionCode")
)
if mibBuilder.loadTexts:
    wwpLeosDhcpClientOptionDisabledNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WWP-LEOS-DHCP-CLIENT-MIB",
    **{"wwpLeosDhcpClientMIB": wwpLeosDhcpClientMIB,
       "wwpLeosDhcpClientMIBObjects": wwpLeosDhcpClientMIBObjects,
       "wwpLeosDhcpClient": wwpLeosDhcpClient,
       "wwpLeosDhcpIfName": wwpLeosDhcpIfName,
       "wwpLeosDhcpStatus": wwpLeosDhcpStatus,
       "wwpLeosDhcpState": wwpLeosDhcpState,
       "wwpLeosDhcpLeaseOffered": wwpLeosDhcpLeaseOffered,
       "wwpLeosDhcpLeaseRemaining": wwpLeosDhcpLeaseRemaining,
       "wwpLeosDhcpDiscoveryMsgInterval": wwpLeosDhcpDiscoveryMsgInterval,
       "wwpLeosDhcpRenewalTime": wwpLeosDhcpRenewalTime,
       "wwpLeosDhcpRebindingTime": wwpLeosDhcpRebindingTime,
       "wwpLeosDhcpServerAddress": wwpLeosDhcpServerAddress,
       "wwpLeosDhcpRenewLease": wwpLeosDhcpRenewLease,
       "wwpLeosDhcpReleaseLease": wwpLeosDhcpReleaseLease,
       "wwpLeosDhcpClientOptionTable": wwpLeosDhcpClientOptionTable,
       "wwpLeosDhcpClientOptionEntry": wwpLeosDhcpClientOptionEntry,
       "wwpLeosDhcpOptionCodeIndex": wwpLeosDhcpOptionCodeIndex,
       "wwpLeosDhcpOptionDesc": wwpLeosDhcpOptionDesc,
       "wwpLeosDhcpOptionCode": wwpLeosDhcpOptionCode,
       "wwpLeosDhcpOptionState": wwpLeosDhcpOptionState,
       "wwpLeosDhcpRelayAgent": wwpLeosDhcpRelayAgent,
       "wwpLeosDhcpRelayAgentGlobalAttrs": wwpLeosDhcpRelayAgentGlobalAttrs,
       "wwpLeosDhcpRelayAgentCircuitId": wwpLeosDhcpRelayAgentCircuitId,
       "wwpLeosDhcpRelayAgentRemoteId": wwpLeosDhcpRelayAgentRemoteId,
       "wwpLeosDhcpRelayAgentL2State": wwpLeosDhcpRelayAgentL2State,
       "wwpLeosDhcpRelayAgentL3State": wwpLeosDhcpRelayAgentL3State,
       "wwpLeosDhcpRelayAgentL2StateTable": wwpLeosDhcpRelayAgentL2StateTable,
       "wwpLeosDhcpRelayAgentL2StateEntry": wwpLeosDhcpRelayAgentL2StateEntry,
       "wwpLeosDhcpRelayAgentVlan": wwpLeosDhcpRelayAgentVlan,
       "wwpLeosDhcpRelayAgentL2AdminState": wwpLeosDhcpRelayAgentL2AdminState,
       "wwpLeosDhcpRelayAgentL2OperState": wwpLeosDhcpRelayAgentL2OperState,
       "wwpLeosDhcpRelayAgentL2StatsClear": wwpLeosDhcpRelayAgentL2StatsClear,
       "wwpLeosDhcpRelayAgentL2RowStatus": wwpLeosDhcpRelayAgentL2RowStatus,
       "wwpLeosDhcpRelayAgentL3StateTable": wwpLeosDhcpRelayAgentL3StateTable,
       "wwpLeosDhcpRelayAgentL3StateEntry": wwpLeosDhcpRelayAgentL3StateEntry,
       "wwpLeosDhcpRelayAgentInterfaceIndex": wwpLeosDhcpRelayAgentInterfaceIndex,
       "wwpLeosDhcpRelayAgentL3AdminState": wwpLeosDhcpRelayAgentL3AdminState,
       "wwpLeosDhcpRelayAgentL3OperState": wwpLeosDhcpRelayAgentL3OperState,
       "wwpLeosDhcpRelayAgentL3RowStatus": wwpLeosDhcpRelayAgentL3RowStatus,
       "wwpLeosDhcpRelayAgentInterfaceIpTable": wwpLeosDhcpRelayAgentInterfaceIpTable,
       "wwpLeosDhcpRelayAgentInterfaceIpEntry": wwpLeosDhcpRelayAgentInterfaceIpEntry,
       "wwpLeosDhcpRelayAgentInterfaceIpIndex": wwpLeosDhcpRelayAgentInterfaceIpIndex,
       "wwpLeosDhcpRelayAgentInterfaceIpAddr": wwpLeosDhcpRelayAgentInterfaceIpAddr,
       "wwpLeosDhcpRelayAgentInterfaceIpRowStatus": wwpLeosDhcpRelayAgentInterfaceIpRowStatus,
       "wwpLeosDhcpRelayAgentTrustTable": wwpLeosDhcpRelayAgentTrustTable,
       "wwpLeosDhcpRelayAgentTrustEntry": wwpLeosDhcpRelayAgentTrustEntry,
       "wwpLeosDhcpRelayAgentPort": wwpLeosDhcpRelayAgentPort,
       "wwpLeosDhcpRelayAgentTrustMode": wwpLeosDhcpRelayAgentTrustMode,
       "wwpLeosDhcpRelayAgentL2StatsTable": wwpLeosDhcpRelayAgentL2StatsTable,
       "wwpLeosDhcpRelayAgentL2StatsEntry": wwpLeosDhcpRelayAgentL2StatsEntry,
       "wwpLeosDhcpRelayAgentL2IpSecHeaders": wwpLeosDhcpRelayAgentL2IpSecHeaders,
       "wwpLeosDhcpRelayAgentL2Option82Added": wwpLeosDhcpRelayAgentL2Option82Added,
       "wwpLeosDhcpRelayAgentL2Option82Removed": wwpLeosDhcpRelayAgentL2Option82Removed,
       "wwpLeosDhcpRelayAgentL2UntrustedClientPortPktsRx": wwpLeosDhcpRelayAgentL2UntrustedClientPortPktsRx,
       "wwpLeosDhcpRelayAgentL2UntrustedServerPortPktsRx": wwpLeosDhcpRelayAgentL2UntrustedServerPortPktsRx,
       "wwpLeosDhcpRelayAgentL2SpoofedDhcpPkts": wwpLeosDhcpRelayAgentL2SpoofedDhcpPkts,
       "wwpLeosDhcpRelayAgentL2Option82ExceedMTU": wwpLeosDhcpRelayAgentL2Option82ExceedMTU,
       "wwpLeosDhcpRelayAgentL2NoTrustedServerPktDrop": wwpLeosDhcpRelayAgentL2NoTrustedServerPktDrop,
       "wwpLeosDhcpRelayAgentL2NoTrustedClientPktDrop": wwpLeosDhcpRelayAgentL2NoTrustedClientPktDrop,
       "wwpLeosDhcpRelayAgentCidStringTable": wwpLeosDhcpRelayAgentCidStringTable,
       "wwpLeosDhcpRelayAgentCidStringEntry": wwpLeosDhcpRelayAgentCidStringEntry,
       "wwpLeosDhcpRelayAgentCidStringPort": wwpLeosDhcpRelayAgentCidStringPort,
       "wwpLeosDhcpRelayAgentCidString": wwpLeosDhcpRelayAgentCidString,
       "wwpLeosDhcpRelayAgentCidStringRowStatus": wwpLeosDhcpRelayAgentCidStringRowStatus,
       "wwpLeosDhcpClientMIBNotificationPrefix": wwpLeosDhcpClientMIBNotificationPrefix,
       "wwpLeosDhcpClientMIBNotifications": wwpLeosDhcpClientMIBNotifications,
       "wwpLeosDhcpClientOptionDisabledNotification": wwpLeosDhcpClientOptionDisabledNotification,
       "wwpLeosDhcpClientMIBConformance": wwpLeosDhcpClientMIBConformance,
       "wwpLeosDhcpClientMIBCompliances": wwpLeosDhcpClientMIBCompliances,
       "wwpLeosDhcpClientMIBGroups": wwpLeosDhcpClientMIBGroups}
)
