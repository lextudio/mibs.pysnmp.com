# SNMP MIB module (NORTEL-SECURE-NETWORK-ACCESS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NORTEL-SECURE-NETWORK-ACCESS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:28:58 2024
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

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType",
    "InetPortNumber")

(VlanId,
 VlanIdOrNone) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId",
    "VlanIdOrNone")

(IdList,) = mibBuilder.importSymbols(
    "RAPID-CITY",
    "IdList")

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
 MacAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(bayStackMibs,) = mibBuilder.importSymbols(
    "SYNOPTICS-ROOT-MIB",
    "bayStackMibs")


# MODULE-IDENTITY

nortelSecureNetworkAccessMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 10)
)
nortelSecureNetworkAccessMib.setRevisions(
        ("2007-06-29 00:00",
         "2007-05-21 00:00",
         "2007-04-18 00:00",
         "2007-03-13 00:00",
         "2006-11-30 00:00",
         "2006-07-07 00:00",
         "2006-05-22 00:00",
         "2006-05-19 00:00",
         "2006-04-26 00:00",
         "2006-02-24 00:00",
         "2005-10-24 00:00",
         "2005-08-18 00:00",
         "2005-08-10 00:00",
         "2005-07-28 00:00",
         "2005-07-18 00:00",
         "2005-07-07 00:00",
         "2005-06-22 00:00",
         "2005-06-02 00:00",
         "2005-05-04 00:00",
         "2005-04-21 00:00",
         "2005-04-19 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class NsnaVlanIdOrNone(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4094),
    )



# MIB Managed Objects in the order of their OIDs

_NsnaNotifications_ObjectIdentity = ObjectIdentity
nsnaNotifications = _NsnaNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 10, 0)
)
_NsnaObjects_ObjectIdentity = ObjectIdentity
nsnaObjects = _NsnaObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 10, 1)
)
_NsnaScalars_ObjectIdentity = ObjectIdentity
nsnaScalars = _NsnaScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 1)
)
_NsnaEnabled_Type = TruthValue
_NsnaEnabled_Object = MibScalar
nsnaEnabled = _NsnaEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 1, 1),
    _NsnaEnabled_Type()
)
nsnaEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsnaEnabled.setStatus("current")


class _NsnaNsnasConnectionState_Type(Integer32):
    """Custom type nsnaNsnasConnectionState based on Integer32"""
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
        *(("closing", 4),
          ("connected", 2),
          ("connecting", 3),
          ("notConnected", 1))
    )


_NsnaNsnasConnectionState_Type.__name__ = "Integer32"
_NsnaNsnasConnectionState_Object = MibScalar
nsnaNsnasConnectionState = _NsnaNsnasConnectionState_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 1, 3),
    _NsnaNsnasConnectionState_Type()
)
nsnaNsnasConnectionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsnaNsnasConnectionState.setStatus("current")
_NsnaNsnasInetAddressType_Type = InetAddressType
_NsnaNsnasInetAddressType_Object = MibScalar
nsnaNsnasInetAddressType = _NsnaNsnasInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 1, 4),
    _NsnaNsnasInetAddressType_Type()
)
nsnaNsnasInetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsnaNsnasInetAddressType.setStatus("current")
_NsnaNsnasInetAddress_Type = InetAddress
_NsnaNsnasInetAddress_Object = MibScalar
nsnaNsnasInetAddress = _NsnaNsnasInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 1, 5),
    _NsnaNsnasInetAddress_Type()
)
nsnaNsnasInetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsnaNsnasInetAddress.setStatus("current")


class _NsnaNsnasSendHelloInterval_Type(Integer32):
    """Custom type nsnaNsnasSendHelloInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NsnaNsnasSendHelloInterval_Type.__name__ = "Integer32"
_NsnaNsnasSendHelloInterval_Object = MibScalar
nsnaNsnasSendHelloInterval = _NsnaNsnasSendHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 1, 6),
    _NsnaNsnasSendHelloInterval_Type()
)
nsnaNsnasSendHelloInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsnaNsnasSendHelloInterval.setStatus("current")
if mibBuilder.loadTexts:
    nsnaNsnasSendHelloInterval.setUnits("seconds")


class _NsnaNsnasInactivityInterval_Type(Integer32):
    """Custom type nsnaNsnasInactivityInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NsnaNsnasInactivityInterval_Type.__name__ = "Integer32"
_NsnaNsnasInactivityInterval_Object = MibScalar
nsnaNsnasInactivityInterval = _NsnaNsnasInactivityInterval_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 1, 7),
    _NsnaNsnasInactivityInterval_Type()
)
nsnaNsnasInactivityInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsnaNsnasInactivityInterval.setStatus("current")
if mibBuilder.loadTexts:
    nsnaNsnasInactivityInterval.setUnits("seconds")


class _NsnaNsnasStatusQuoInterval_Type(Integer32):
    """Custom type nsnaNsnasStatusQuoInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NsnaNsnasStatusQuoInterval_Type.__name__ = "Integer32"
_NsnaNsnasStatusQuoInterval_Object = MibScalar
nsnaNsnasStatusQuoInterval = _NsnaNsnasStatusQuoInterval_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 1, 8),
    _NsnaNsnasStatusQuoInterval_Type()
)
nsnaNsnasStatusQuoInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsnaNsnasStatusQuoInterval.setStatus("current")
if mibBuilder.loadTexts:
    nsnaNsnasStatusQuoInterval.setUnits("seconds")
_NsnaMacAuthenticationEnabled_Type = TruthValue
_NsnaMacAuthenticationEnabled_Object = MibScalar
nsnaMacAuthenticationEnabled = _NsnaMacAuthenticationEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 1, 9),
    _NsnaMacAuthenticationEnabled_Type()
)
nsnaMacAuthenticationEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsnaMacAuthenticationEnabled.setStatus("current")
_NsnaFailOpenEnabled_Type = TruthValue
_NsnaFailOpenEnabled_Object = MibScalar
nsnaFailOpenEnabled = _NsnaFailOpenEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 1, 10),
    _NsnaFailOpenEnabled_Type()
)
nsnaFailOpenEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsnaFailOpenEnabled.setStatus("current")
_NsnaFailOpenVlan_Type = VlanIdOrNone
_NsnaFailOpenVlan_Object = MibScalar
nsnaFailOpenVlan = _NsnaFailOpenVlan_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 1, 11),
    _NsnaFailOpenVlan_Type()
)
nsnaFailOpenVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsnaFailOpenVlan.setStatus("current")
_NsnaFailOpenFilterVlan_Type = VlanIdOrNone
_NsnaFailOpenFilterVlan_Object = MibScalar
nsnaFailOpenFilterVlan = _NsnaFailOpenFilterVlan_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 1, 12),
    _NsnaFailOpenFilterVlan_Type()
)
nsnaFailOpenFilterVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsnaFailOpenFilterVlan.setStatus("current")


class _NsnaNsnasConnectionVersion_Type(Integer32):
    """Custom type nsnaNsnasConnectionVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NsnaNsnasConnectionVersion_Type.__name__ = "Integer32"
_NsnaNsnasConnectionVersion_Object = MibScalar
nsnaNsnasConnectionVersion = _NsnaNsnasConnectionVersion_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 1, 14),
    _NsnaNsnasConnectionVersion_Type()
)
nsnaNsnasConnectionVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsnaNsnasConnectionVersion.setStatus("current")
_NsnaNsnasRadiusServerEnabled_Type = TruthValue
_NsnaNsnasRadiusServerEnabled_Object = MibScalar
nsnaNsnasRadiusServerEnabled = _NsnaNsnasRadiusServerEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 1, 15),
    _NsnaNsnasRadiusServerEnabled_Type()
)
nsnaNsnasRadiusServerEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsnaNsnasRadiusServerEnabled.setStatus("current")
_NsnaNsnasRadiusServerPort_Type = InetPortNumber
_NsnaNsnasRadiusServerPort_Object = MibScalar
nsnaNsnasRadiusServerPort = _NsnaNsnasRadiusServerPort_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 1, 16),
    _NsnaNsnasRadiusServerPort_Type()
)
nsnaNsnasRadiusServerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsnaNsnasRadiusServerPort.setStatus("current")
_NsnaNsnasTable_Object = MibTable
nsnaNsnasTable = _NsnaNsnasTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 2)
)
if mibBuilder.loadTexts:
    nsnaNsnasTable.setStatus("current")
_NsnaNsnasEntry_Object = MibTableRow
nsnaNsnasEntry = _NsnaNsnasEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 2, 1)
)
nsnaNsnasEntry.setIndexNames(
    (0, "NORTEL-SECURE-NETWORK-ACCESS-MIB", "nsnaNsnasAddressType"),
    (0, "NORTEL-SECURE-NETWORK-ACCESS-MIB", "nsnaNsnasAddress"),
    (0, "NORTEL-SECURE-NETWORK-ACCESS-MIB", "nsnaNsnasAddressMask"),
)
if mibBuilder.loadTexts:
    nsnaNsnasEntry.setStatus("current")
_NsnaNsnasAddressType_Type = InetAddressType
_NsnaNsnasAddressType_Object = MibTableColumn
nsnaNsnasAddressType = _NsnaNsnasAddressType_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 2, 1, 1),
    _NsnaNsnasAddressType_Type()
)
nsnaNsnasAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nsnaNsnasAddressType.setStatus("current")
_NsnaNsnasAddress_Type = InetAddress
_NsnaNsnasAddress_Object = MibTableColumn
nsnaNsnasAddress = _NsnaNsnasAddress_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 2, 1, 2),
    _NsnaNsnasAddress_Type()
)
nsnaNsnasAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nsnaNsnasAddress.setStatus("current")
_NsnaNsnasAddressMask_Type = InetAddressPrefixLength
_NsnaNsnasAddressMask_Object = MibTableColumn
nsnaNsnasAddressMask = _NsnaNsnasAddressMask_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 2, 1, 3),
    _NsnaNsnasAddressMask_Type()
)
nsnaNsnasAddressMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nsnaNsnasAddressMask.setStatus("current")


class _NsnaNsnasPort_Type(InetPortNumber):
    """Custom type nsnaNsnasPort based on InetPortNumber"""
    defaultValue = 5000

    subtypeSpec = InetPortNumber.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1024, 65535),
    )


_NsnaNsnasPort_Type.__name__ = "InetPortNumber"
_NsnaNsnasPort_Object = MibTableColumn
nsnaNsnasPort = _NsnaNsnasPort_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 2, 1, 4),
    _NsnaNsnasPort_Type()
)
nsnaNsnasPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsnaNsnasPort.setStatus("current")
_NsnaNsnasRowStatus_Type = RowStatus
_NsnaNsnasRowStatus_Object = MibTableColumn
nsnaNsnasRowStatus = _NsnaNsnasRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 2, 1, 5),
    _NsnaNsnasRowStatus_Type()
)
nsnaNsnasRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsnaNsnasRowStatus.setStatus("current")
_NsnaPortTable_Object = MibTable
nsnaPortTable = _NsnaPortTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 3)
)
if mibBuilder.loadTexts:
    nsnaPortTable.setStatus("current")
_NsnaPortEntry_Object = MibTableRow
nsnaPortEntry = _NsnaPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 3, 1)
)
nsnaPortEntry.setIndexNames(
    (0, "NORTEL-SECURE-NETWORK-ACCESS-MIB", "nsnaPortIfIndex"),
)
if mibBuilder.loadTexts:
    nsnaPortEntry.setStatus("current")
_NsnaPortIfIndex_Type = InterfaceIndex
_NsnaPortIfIndex_Object = MibTableColumn
nsnaPortIfIndex = _NsnaPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 3, 1, 1),
    _NsnaPortIfIndex_Type()
)
nsnaPortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nsnaPortIfIndex.setStatus("current")


class _NsnaPortMode_Type(Integer32):
    """Custom type nsnaPortMode based on Integer32"""
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
        *(("disabled", 1),
          ("dynamic", 3),
          ("secure", 5),
          ("static", 2),
          ("uplink", 4))
    )


_NsnaPortMode_Type.__name__ = "Integer32"
_NsnaPortMode_Object = MibTableColumn
nsnaPortMode = _NsnaPortMode_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 3, 1, 2),
    _NsnaPortMode_Type()
)
nsnaPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsnaPortMode.setStatus("current")
_NsnaPortGreenVlanId_Type = NsnaVlanIdOrNone
_NsnaPortGreenVlanId_Object = MibTableColumn
nsnaPortGreenVlanId = _NsnaPortGreenVlanId_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 3, 1, 3),
    _NsnaPortGreenVlanId_Type()
)
nsnaPortGreenVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsnaPortGreenVlanId.setStatus("current")
_NsnaPortVoipVlans_Type = IdList
_NsnaPortVoipVlans_Object = MibTableColumn
nsnaPortVoipVlans = _NsnaPortVoipVlans_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 3, 1, 4),
    _NsnaPortVoipVlans_Type()
)
nsnaPortVoipVlans.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsnaPortVoipVlans.setStatus("current")
_NsnaPortUplinkVlans_Type = IdList
_NsnaPortUplinkVlans_Object = MibTableColumn
nsnaPortUplinkVlans = _NsnaPortUplinkVlans_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 3, 1, 5),
    _NsnaPortUplinkVlans_Type()
)
nsnaPortUplinkVlans.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsnaPortUplinkVlans.setStatus("current")


class _NsnaPortState_Type(Integer32):
    """Custom type nsnaPortState based on Integer32"""
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
        *(("green", 3),
          ("none", 1),
          ("red", 2),
          ("yellow", 4))
    )


_NsnaPortState_Type.__name__ = "Integer32"
_NsnaPortState_Object = MibTableColumn
nsnaPortState = _NsnaPortState_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 3, 1, 6),
    _NsnaPortState_Type()
)
nsnaPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsnaPortState.setStatus("current")


class _NsnaPortDhcpState_Type(Integer32):
    """Custom type nsnaPortDhcpState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("blocked", 1),
          ("unblocked", 2))
    )


_NsnaPortDhcpState_Type.__name__ = "Integer32"
_NsnaPortDhcpState_Object = MibTableColumn
nsnaPortDhcpState = _NsnaPortDhcpState_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 3, 1, 7),
    _NsnaPortDhcpState_Type()
)
nsnaPortDhcpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsnaPortDhcpState.setStatus("current")
_NsnaPortHubModeEnabled_Type = TruthValue
_NsnaPortHubModeEnabled_Object = MibTableColumn
nsnaPortHubModeEnabled = _NsnaPortHubModeEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 3, 1, 8),
    _NsnaPortHubModeEnabled_Type()
)
nsnaPortHubModeEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsnaPortHubModeEnabled.setStatus("current")


class _NsnaPortHubModeMaxClients_Type(Integer32):
    """Custom type nsnaPortHubModeMaxClients based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_NsnaPortHubModeMaxClients_Type.__name__ = "Integer32"
_NsnaPortHubModeMaxClients_Object = MibTableColumn
nsnaPortHubModeMaxClients = _NsnaPortHubModeMaxClients_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 3, 1, 9),
    _NsnaPortHubModeMaxClients_Type()
)
nsnaPortHubModeMaxClients.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsnaPortHubModeMaxClients.setStatus("current")
_NsnaVlanTable_Object = MibTable
nsnaVlanTable = _NsnaVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 4)
)
if mibBuilder.loadTexts:
    nsnaVlanTable.setStatus("current")
_NsnaVlanEntry_Object = MibTableRow
nsnaVlanEntry = _NsnaVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 4, 1)
)
nsnaVlanEntry.setIndexNames(
    (0, "NORTEL-SECURE-NETWORK-ACCESS-MIB", "nsnaVlanId"),
)
if mibBuilder.loadTexts:
    nsnaVlanEntry.setStatus("current")
_NsnaVlanId_Type = VlanId
_NsnaVlanId_Object = MibTableColumn
nsnaVlanId = _NsnaVlanId_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 4, 1, 1),
    _NsnaVlanId_Type()
)
nsnaVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nsnaVlanId.setStatus("current")


class _NsnaVlanColor_Type(Integer32):
    """Custom type nsnaVlanColor based on Integer32"""
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
        *(("green", 3),
          ("none", 1),
          ("red", 2),
          ("voip", 5),
          ("yellow", 4))
    )


_NsnaVlanColor_Type.__name__ = "Integer32"
_NsnaVlanColor_Object = MibTableColumn
nsnaVlanColor = _NsnaVlanColor_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 4, 1, 2),
    _NsnaVlanColor_Type()
)
nsnaVlanColor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsnaVlanColor.setStatus("current")


class _NsnaVlanFilterSetName_Type(SnmpAdminString):
    """Custom type nsnaVlanFilterSetName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NsnaVlanFilterSetName_Type.__name__ = "SnmpAdminString"
_NsnaVlanFilterSetName_Object = MibTableColumn
nsnaVlanFilterSetName = _NsnaVlanFilterSetName_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 4, 1, 3),
    _NsnaVlanFilterSetName_Type()
)
nsnaVlanFilterSetName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsnaVlanFilterSetName.setStatus("current")


class _NsnaVlanFilterSetId_Type(Integer32):
    """Custom type nsnaVlanFilterSetId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_NsnaVlanFilterSetId_Type.__name__ = "Integer32"
_NsnaVlanFilterSetId_Object = MibTableColumn
nsnaVlanFilterSetId = _NsnaVlanFilterSetId_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 4, 1, 4),
    _NsnaVlanFilterSetId_Type()
)
nsnaVlanFilterSetId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsnaVlanFilterSetId.setStatus("current")
_NsnaVlanYellowSubnetType_Type = InetAddressType
_NsnaVlanYellowSubnetType_Object = MibTableColumn
nsnaVlanYellowSubnetType = _NsnaVlanYellowSubnetType_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 4, 1, 5),
    _NsnaVlanYellowSubnetType_Type()
)
nsnaVlanYellowSubnetType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsnaVlanYellowSubnetType.setStatus("current")
_NsnaVlanYellowSubnet_Type = InetAddress
_NsnaVlanYellowSubnet_Object = MibTableColumn
nsnaVlanYellowSubnet = _NsnaVlanYellowSubnet_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 4, 1, 6),
    _NsnaVlanYellowSubnet_Type()
)
nsnaVlanYellowSubnet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsnaVlanYellowSubnet.setStatus("current")
_NsnaVlanYellowSubnetMask_Type = InetAddressPrefixLength
_NsnaVlanYellowSubnetMask_Object = MibTableColumn
nsnaVlanYellowSubnetMask = _NsnaVlanYellowSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 4, 1, 7),
    _NsnaVlanYellowSubnetMask_Type()
)
nsnaVlanYellowSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsnaVlanYellowSubnetMask.setStatus("current")
_NsnaClientTable_Object = MibTable
nsnaClientTable = _NsnaClientTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 5)
)
if mibBuilder.loadTexts:
    nsnaClientTable.setStatus("current")
_NsnaClientEntry_Object = MibTableRow
nsnaClientEntry = _NsnaClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 5, 1)
)
nsnaClientEntry.setIndexNames(
    (0, "NORTEL-SECURE-NETWORK-ACCESS-MIB", "nsnaClientIfIndex"),
    (0, "NORTEL-SECURE-NETWORK-ACCESS-MIB", "nsnaClientMacAddress"),
)
if mibBuilder.loadTexts:
    nsnaClientEntry.setStatus("current")
_NsnaClientIfIndex_Type = InterfaceIndex
_NsnaClientIfIndex_Object = MibTableColumn
nsnaClientIfIndex = _NsnaClientIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 5, 1, 1),
    _NsnaClientIfIndex_Type()
)
nsnaClientIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nsnaClientIfIndex.setStatus("current")
_NsnaClientMacAddress_Type = MacAddress
_NsnaClientMacAddress_Object = MibTableColumn
nsnaClientMacAddress = _NsnaClientMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 5, 1, 2),
    _NsnaClientMacAddress_Type()
)
nsnaClientMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nsnaClientMacAddress.setStatus("current")


class _NsnaClientDeviceType_Type(Integer32):
    """Custom type nsnaClientDeviceType based on Integer32"""
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
        *(("ipPhone", 2),
          ("passive", 3),
          ("pc", 1),
          ("unknown", 0))
    )


_NsnaClientDeviceType_Type.__name__ = "Integer32"
_NsnaClientDeviceType_Object = MibTableColumn
nsnaClientDeviceType = _NsnaClientDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 5, 1, 3),
    _NsnaClientDeviceType_Type()
)
nsnaClientDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsnaClientDeviceType.setStatus("current")
_NsnaClientVlanId_Type = VlanId
_NsnaClientVlanId_Object = MibTableColumn
nsnaClientVlanId = _NsnaClientVlanId_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 5, 1, 4),
    _NsnaClientVlanId_Type()
)
nsnaClientVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsnaClientVlanId.setStatus("current")
_NsnaClientAddressType_Type = InetAddressType
_NsnaClientAddressType_Object = MibTableColumn
nsnaClientAddressType = _NsnaClientAddressType_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 5, 1, 5),
    _NsnaClientAddressType_Type()
)
nsnaClientAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsnaClientAddressType.setStatus("current")
_NsnaClientAddress_Type = InetAddress
_NsnaClientAddress_Object = MibTableColumn
nsnaClientAddress = _NsnaClientAddress_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 5, 1, 6),
    _NsnaClientAddress_Type()
)
nsnaClientAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsnaClientAddress.setStatus("current")
_NsnaClientExpired_Type = TruthValue
_NsnaClientExpired_Object = MibTableColumn
nsnaClientExpired = _NsnaClientExpired_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 5, 1, 7),
    _NsnaClientExpired_Type()
)
nsnaClientExpired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsnaClientExpired.setStatus("current")
_NsnaClientFilterVlanId_Type = VlanId
_NsnaClientFilterVlanId_Object = MibTableColumn
nsnaClientFilterVlanId = _NsnaClientFilterVlanId_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 5, 1, 8),
    _NsnaClientFilterVlanId_Type()
)
nsnaClientFilterVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsnaClientFilterVlanId.setStatus("current")


class _NsnaClientStatus_Type(Integer32):
    """Custom type nsnaClientStatus based on Integer32"""
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
        *(("authenticatedByNsnas", 1),
          ("authenticatedLocally", 2),
          ("blacklistedByNsnas", 5),
          ("disallowedByNsnas", 3),
          ("isolatedByNsnas", 4))
    )


_NsnaClientStatus_Type.__name__ = "Integer32"
_NsnaClientStatus_Object = MibTableColumn
nsnaClientStatus = _NsnaClientStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 5, 1, 9),
    _NsnaClientStatus_Type()
)
nsnaClientStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsnaClientStatus.setStatus("current")
_NsnaStaticClientTable_Object = MibTable
nsnaStaticClientTable = _NsnaStaticClientTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 6)
)
if mibBuilder.loadTexts:
    nsnaStaticClientTable.setStatus("current")
_NsnaStaticClientEntry_Object = MibTableRow
nsnaStaticClientEntry = _NsnaStaticClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 6, 1)
)
nsnaStaticClientEntry.setIndexNames(
    (0, "NORTEL-SECURE-NETWORK-ACCESS-MIB", "nsnaStaticClientVlanId"),
    (0, "NORTEL-SECURE-NETWORK-ACCESS-MIB", "nsnaStaticClientMacAddress"),
)
if mibBuilder.loadTexts:
    nsnaStaticClientEntry.setStatus("current")
_NsnaStaticClientVlanId_Type = VlanId
_NsnaStaticClientVlanId_Object = MibTableColumn
nsnaStaticClientVlanId = _NsnaStaticClientVlanId_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 6, 1, 1),
    _NsnaStaticClientVlanId_Type()
)
nsnaStaticClientVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nsnaStaticClientVlanId.setStatus("current")
_NsnaStaticClientMacAddress_Type = MacAddress
_NsnaStaticClientMacAddress_Object = MibTableColumn
nsnaStaticClientMacAddress = _NsnaStaticClientMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 6, 1, 2),
    _NsnaStaticClientMacAddress_Type()
)
nsnaStaticClientMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nsnaStaticClientMacAddress.setStatus("current")


class _NsnaStaticClientDeviceType_Type(Integer32):
    """Custom type nsnaStaticClientDeviceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ipPhone", 2),
          ("passive", 3),
          ("pc", 1))
    )


_NsnaStaticClientDeviceType_Type.__name__ = "Integer32"
_NsnaStaticClientDeviceType_Object = MibTableColumn
nsnaStaticClientDeviceType = _NsnaStaticClientDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 6, 1, 3),
    _NsnaStaticClientDeviceType_Type()
)
nsnaStaticClientDeviceType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsnaStaticClientDeviceType.setStatus("current")
_NsnaStaticClientAddressType_Type = InetAddressType
_NsnaStaticClientAddressType_Object = MibTableColumn
nsnaStaticClientAddressType = _NsnaStaticClientAddressType_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 6, 1, 4),
    _NsnaStaticClientAddressType_Type()
)
nsnaStaticClientAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsnaStaticClientAddressType.setStatus("current")
_NsnaStaticClientAddress_Type = InetAddress
_NsnaStaticClientAddress_Object = MibTableColumn
nsnaStaticClientAddress = _NsnaStaticClientAddress_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 6, 1, 5),
    _NsnaStaticClientAddress_Type()
)
nsnaStaticClientAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsnaStaticClientAddress.setStatus("current")
_NsnaStaticClientRowStatus_Type = RowStatus
_NsnaStaticClientRowStatus_Object = MibTableColumn
nsnaStaticClientRowStatus = _NsnaStaticClientRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 6, 1, 6),
    _NsnaStaticClientRowStatus_Type()
)
nsnaStaticClientRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsnaStaticClientRowStatus.setStatus("current")
_NsnaIpPhoneSignatureTable_Object = MibTable
nsnaIpPhoneSignatureTable = _NsnaIpPhoneSignatureTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 7)
)
if mibBuilder.loadTexts:
    nsnaIpPhoneSignatureTable.setStatus("current")
_NsnaIpPhoneSignatureEntry_Object = MibTableRow
nsnaIpPhoneSignatureEntry = _NsnaIpPhoneSignatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 7, 1)
)
nsnaIpPhoneSignatureEntry.setIndexNames(
    (1, "NORTEL-SECURE-NETWORK-ACCESS-MIB", "nsnaIpPhoneSignatureString"),
)
if mibBuilder.loadTexts:
    nsnaIpPhoneSignatureEntry.setStatus("current")


class _NsnaIpPhoneSignatureString_Type(OctetString):
    """Custom type nsnaIpPhoneSignatureString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_NsnaIpPhoneSignatureString_Type.__name__ = "OctetString"
_NsnaIpPhoneSignatureString_Object = MibTableColumn
nsnaIpPhoneSignatureString = _NsnaIpPhoneSignatureString_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 7, 1, 1),
    _NsnaIpPhoneSignatureString_Type()
)
nsnaIpPhoneSignatureString.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nsnaIpPhoneSignatureString.setStatus("current")
_NsnaIpPhoneSignatureRowStatus_Type = RowStatus
_NsnaIpPhoneSignatureRowStatus_Object = MibTableColumn
nsnaIpPhoneSignatureRowStatus = _NsnaIpPhoneSignatureRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 7, 1, 2),
    _NsnaIpPhoneSignatureRowStatus_Type()
)
nsnaIpPhoneSignatureRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsnaIpPhoneSignatureRowStatus.setStatus("current")
_NsnaNotificationObjects_ObjectIdentity = ObjectIdentity
nsnaNotificationObjects = _NsnaNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 8)
)


class _NsnaClosedConnectionReason_Type(Integer32):
    """Custom type nsnaClosedConnectionReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("bufferAllocationFailure", 4),
          ("dataStreamCorrupted", 3),
          ("inactivityIntervalExpired", 6),
          ("messageProcessingFailure", 5),
          ("nsnaAdministrativelyDown", 7),
          ("snasClosedConnection", 2),
          ("unknown", 1))
    )


_NsnaClosedConnectionReason_Type.__name__ = "Integer32"
_NsnaClosedConnectionReason_Object = MibScalar
nsnaClosedConnectionReason = _NsnaClosedConnectionReason_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 8, 1),
    _NsnaClosedConnectionReason_Type()
)
nsnaClosedConnectionReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nsnaClosedConnectionReason.setStatus("current")


class _NsnaInvalidMessageHeader_Type(OctetString):
    """Custom type nsnaInvalidMessageHeader based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_NsnaInvalidMessageHeader_Type.__name__ = "OctetString"
_NsnaInvalidMessageHeader_Object = MibScalar
nsnaInvalidMessageHeader = _NsnaInvalidMessageHeader_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 8, 2),
    _NsnaInvalidMessageHeader_Type()
)
nsnaInvalidMessageHeader.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nsnaInvalidMessageHeader.setStatus("current")

# Managed Objects groups


# Notification objects

nsnaClosedConnectionToSnas = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 5, 10, 0, 1)
)
nsnaClosedConnectionToSnas.setObjects(
    ("NORTEL-SECURE-NETWORK-ACCESS-MIB", "nsnaClosedConnectionReason")
)
if mibBuilder.loadTexts:
    nsnaClosedConnectionToSnas.setStatus(
        "current"
    )

nsnaStatusQuoIntervalExpired = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 5, 10, 0, 2)
)
if mibBuilder.loadTexts:
    nsnaStatusQuoIntervalExpired.setStatus(
        "current"
    )

nsnaInvalidMessageFromSnas = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 5, 10, 0, 3)
)
nsnaInvalidMessageFromSnas.setObjects(
    ("NORTEL-SECURE-NETWORK-ACCESS-MIB", "nsnaInvalidMessageHeader")
)
if mibBuilder.loadTexts:
    nsnaInvalidMessageFromSnas.setStatus(
        "current"
    )

nsnaSnasConnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 5, 10, 0, 4)
)
nsnaSnasConnected.setObjects(
      *(("NORTEL-SECURE-NETWORK-ACCESS-MIB", "nsnaNsnasInetAddressType"),
        ("NORTEL-SECURE-NETWORK-ACCESS-MIB", "nsnaNsnasInetAddress"),
        ("NORTEL-SECURE-NETWORK-ACCESS-MIB", "nsnaNsnasSendHelloInterval"),
        ("NORTEL-SECURE-NETWORK-ACCESS-MIB", "nsnaNsnasInactivityInterval"),
        ("NORTEL-SECURE-NETWORK-ACCESS-MIB", "nsnaNsnasStatusQuoInterval"))
)
if mibBuilder.loadTexts:
    nsnaSnasConnected.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NORTEL-SECURE-NETWORK-ACCESS-MIB",
    **{"NsnaVlanIdOrNone": NsnaVlanIdOrNone,
       "nortelSecureNetworkAccessMib": nortelSecureNetworkAccessMib,
       "nsnaNotifications": nsnaNotifications,
       "nsnaClosedConnectionToSnas": nsnaClosedConnectionToSnas,
       "nsnaStatusQuoIntervalExpired": nsnaStatusQuoIntervalExpired,
       "nsnaInvalidMessageFromSnas": nsnaInvalidMessageFromSnas,
       "nsnaSnasConnected": nsnaSnasConnected,
       "nsnaObjects": nsnaObjects,
       "nsnaScalars": nsnaScalars,
       "nsnaEnabled": nsnaEnabled,
       "nsnaNsnasConnectionState": nsnaNsnasConnectionState,
       "nsnaNsnasInetAddressType": nsnaNsnasInetAddressType,
       "nsnaNsnasInetAddress": nsnaNsnasInetAddress,
       "nsnaNsnasSendHelloInterval": nsnaNsnasSendHelloInterval,
       "nsnaNsnasInactivityInterval": nsnaNsnasInactivityInterval,
       "nsnaNsnasStatusQuoInterval": nsnaNsnasStatusQuoInterval,
       "nsnaMacAuthenticationEnabled": nsnaMacAuthenticationEnabled,
       "nsnaFailOpenEnabled": nsnaFailOpenEnabled,
       "nsnaFailOpenVlan": nsnaFailOpenVlan,
       "nsnaFailOpenFilterVlan": nsnaFailOpenFilterVlan,
       "nsnaNsnasConnectionVersion": nsnaNsnasConnectionVersion,
       "nsnaNsnasRadiusServerEnabled": nsnaNsnasRadiusServerEnabled,
       "nsnaNsnasRadiusServerPort": nsnaNsnasRadiusServerPort,
       "nsnaNsnasTable": nsnaNsnasTable,
       "nsnaNsnasEntry": nsnaNsnasEntry,
       "nsnaNsnasAddressType": nsnaNsnasAddressType,
       "nsnaNsnasAddress": nsnaNsnasAddress,
       "nsnaNsnasAddressMask": nsnaNsnasAddressMask,
       "nsnaNsnasPort": nsnaNsnasPort,
       "nsnaNsnasRowStatus": nsnaNsnasRowStatus,
       "nsnaPortTable": nsnaPortTable,
       "nsnaPortEntry": nsnaPortEntry,
       "nsnaPortIfIndex": nsnaPortIfIndex,
       "nsnaPortMode": nsnaPortMode,
       "nsnaPortGreenVlanId": nsnaPortGreenVlanId,
       "nsnaPortVoipVlans": nsnaPortVoipVlans,
       "nsnaPortUplinkVlans": nsnaPortUplinkVlans,
       "nsnaPortState": nsnaPortState,
       "nsnaPortDhcpState": nsnaPortDhcpState,
       "nsnaPortHubModeEnabled": nsnaPortHubModeEnabled,
       "nsnaPortHubModeMaxClients": nsnaPortHubModeMaxClients,
       "nsnaVlanTable": nsnaVlanTable,
       "nsnaVlanEntry": nsnaVlanEntry,
       "nsnaVlanId": nsnaVlanId,
       "nsnaVlanColor": nsnaVlanColor,
       "nsnaVlanFilterSetName": nsnaVlanFilterSetName,
       "nsnaVlanFilterSetId": nsnaVlanFilterSetId,
       "nsnaVlanYellowSubnetType": nsnaVlanYellowSubnetType,
       "nsnaVlanYellowSubnet": nsnaVlanYellowSubnet,
       "nsnaVlanYellowSubnetMask": nsnaVlanYellowSubnetMask,
       "nsnaClientTable": nsnaClientTable,
       "nsnaClientEntry": nsnaClientEntry,
       "nsnaClientIfIndex": nsnaClientIfIndex,
       "nsnaClientMacAddress": nsnaClientMacAddress,
       "nsnaClientDeviceType": nsnaClientDeviceType,
       "nsnaClientVlanId": nsnaClientVlanId,
       "nsnaClientAddressType": nsnaClientAddressType,
       "nsnaClientAddress": nsnaClientAddress,
       "nsnaClientExpired": nsnaClientExpired,
       "nsnaClientFilterVlanId": nsnaClientFilterVlanId,
       "nsnaClientStatus": nsnaClientStatus,
       "nsnaStaticClientTable": nsnaStaticClientTable,
       "nsnaStaticClientEntry": nsnaStaticClientEntry,
       "nsnaStaticClientVlanId": nsnaStaticClientVlanId,
       "nsnaStaticClientMacAddress": nsnaStaticClientMacAddress,
       "nsnaStaticClientDeviceType": nsnaStaticClientDeviceType,
       "nsnaStaticClientAddressType": nsnaStaticClientAddressType,
       "nsnaStaticClientAddress": nsnaStaticClientAddress,
       "nsnaStaticClientRowStatus": nsnaStaticClientRowStatus,
       "nsnaIpPhoneSignatureTable": nsnaIpPhoneSignatureTable,
       "nsnaIpPhoneSignatureEntry": nsnaIpPhoneSignatureEntry,
       "nsnaIpPhoneSignatureString": nsnaIpPhoneSignatureString,
       "nsnaIpPhoneSignatureRowStatus": nsnaIpPhoneSignatureRowStatus,
       "nsnaNotificationObjects": nsnaNotificationObjects,
       "nsnaClosedConnectionReason": nsnaClosedConnectionReason,
       "nsnaInvalidMessageHeader": nsnaInvalidMessageHeader}
)
