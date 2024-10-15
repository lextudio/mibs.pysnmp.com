# SNMP MIB module (AP-SYSTEM-NETWORK) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AP-SYSTEM-NETWORK
# Produced by pysmi-1.5.4 at Mon Oct 14 20:39:05 2024
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
 enterprises,
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
    "enterprises",
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


# MODULE-IDENTITY

ap_system_network_mib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Pepwave_ObjectIdentity = ObjectIdentity
pepwave = _Pepwave_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27662)
)
_ProductID_ObjectIdentity = ObjectIdentity
productID = _ProductID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27662, 200)
)
_ApMib_ObjectIdentity = ObjectIdentity
apMib = _ApMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1)
)
_ApGeneralMib_ObjectIdentity = ObjectIdentity
apGeneralMib = _ApGeneralMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1)
)
_ApNetworkInfo_ObjectIdentity = ObjectIdentity
apNetworkInfo = _ApNetworkInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 2, 1)
)
_ApWanInfo_ObjectIdentity = ObjectIdentity
apWanInfo = _ApWanInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 2, 1, 1)
)


class _ApCurrentIpAddressMode_Type(Integer32):
    """Custom type apCurrentIpAddressMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 0),
          ("manual", 1),
          ("pppoe", 2))
    )


_ApCurrentIpAddressMode_Type.__name__ = "Integer32"
_ApCurrentIpAddressMode_Object = MibScalar
apCurrentIpAddressMode = _ApCurrentIpAddressMode_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 2, 1, 1, 1),
    _ApCurrentIpAddressMode_Type()
)
apCurrentIpAddressMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCurrentIpAddressMode.setStatus("current")
_ApCurrentIpAddress_Type = IpAddress
_ApCurrentIpAddress_Object = MibScalar
apCurrentIpAddress = _ApCurrentIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 2, 1, 1, 2),
    _ApCurrentIpAddress_Type()
)
apCurrentIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCurrentIpAddress.setStatus("current")
_ApCurrentSubnetMask_Type = IpAddress
_ApCurrentSubnetMask_Object = MibScalar
apCurrentSubnetMask = _ApCurrentSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 2, 1, 1, 3),
    _ApCurrentSubnetMask_Type()
)
apCurrentSubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCurrentSubnetMask.setStatus("current")
_ApCurrentGateway_Type = IpAddress
_ApCurrentGateway_Object = MibScalar
apCurrentGateway = _ApCurrentGateway_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 2, 1, 1, 4),
    _ApCurrentGateway_Type()
)
apCurrentGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCurrentGateway.setStatus("current")
_ApCurrentDns_Type = IpAddress
_ApCurrentDns_Object = MibScalar
apCurrentDns = _ApCurrentDns_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 2, 1, 1, 5),
    _ApCurrentDns_Type()
)
apCurrentDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCurrentDns.setStatus("current")
_ApPppoeInfo_ObjectIdentity = ObjectIdentity
apPppoeInfo = _ApPppoeInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 2, 1, 4)
)


class _ApPppoeStatus_Type(Integer32):
    """Custom type apPppoeStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("connected", 2),
          ("connecting", 1),
          ("disable", 0))
    )


_ApPppoeStatus_Type.__name__ = "Integer32"
_ApPppoeStatus_Object = MibScalar
apPppoeStatus = _ApPppoeStatus_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 2, 1, 4, 1),
    _ApPppoeStatus_Type()
)
apPppoeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apPppoeStatus.setStatus("current")


class _ApPppoeStatusMessage_Type(OctetString):
    """Custom type apPppoeStatusMessage based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ApPppoeStatusMessage_Type.__name__ = "OctetString"
_ApPppoeStatusMessage_Object = MibScalar
apPppoeStatusMessage = _ApPppoeStatusMessage_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 2, 1, 4, 2),
    _ApPppoeStatusMessage_Type()
)
apPppoeStatusMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apPppoeStatusMessage.setStatus("current")
_ApNetworkConfig_ObjectIdentity = ObjectIdentity
apNetworkConfig = _ApNetworkConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 2, 2)
)
_ApWanConfig_ObjectIdentity = ObjectIdentity
apWanConfig = _ApWanConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 2, 2, 1)
)


class _ApKeepDefaultIp_Type(Integer32):
    """Custom type apKeepDefaultIp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_ApKeepDefaultIp_Type.__name__ = "Integer32"
_ApKeepDefaultIp_Object = MibScalar
apKeepDefaultIp = _ApKeepDefaultIp_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 2, 2, 1, 1),
    _ApKeepDefaultIp_Type()
)
apKeepDefaultIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apKeepDefaultIp.setStatus("current")


class _ApIpAddressMode_Type(Integer32):
    """Custom type apIpAddressMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 0),
          ("manual", 1),
          ("pppoe", 2))
    )


_ApIpAddressMode_Type.__name__ = "Integer32"
_ApIpAddressMode_Object = MibScalar
apIpAddressMode = _ApIpAddressMode_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 2, 2, 1, 2),
    _ApIpAddressMode_Type()
)
apIpAddressMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apIpAddressMode.setStatus("current")
_ApIpAddress_Type = IpAddress
_ApIpAddress_Object = MibScalar
apIpAddress = _ApIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 2, 2, 1, 3),
    _ApIpAddress_Type()
)
apIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apIpAddress.setStatus("current")
_ApSubnetMask_Type = IpAddress
_ApSubnetMask_Object = MibScalar
apSubnetMask = _ApSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 2, 2, 1, 4),
    _ApSubnetMask_Type()
)
apSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSubnetMask.setStatus("current")
_ApGateway_Type = IpAddress
_ApGateway_Object = MibScalar
apGateway = _ApGateway_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 2, 2, 1, 5),
    _ApGateway_Type()
)
apGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apGateway.setStatus("current")
_ApDns_Type = IpAddress
_ApDns_Object = MibScalar
apDns = _ApDns_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 2, 2, 1, 6),
    _ApDns_Type()
)
apDns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apDns.setStatus("current")
_ApLanConfig_ObjectIdentity = ObjectIdentity
apLanConfig = _ApLanConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 2, 2, 2)
)
_ApLanIpAddress_Type = IpAddress
_ApLanIpAddress_Object = MibScalar
apLanIpAddress = _ApLanIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 2, 2, 2, 1),
    _ApLanIpAddress_Type()
)
apLanIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apLanIpAddress.setStatus("current")
_ApLanSubnetMask_Type = IpAddress
_ApLanSubnetMask_Object = MibScalar
apLanSubnetMask = _ApLanSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 2, 2, 2, 2),
    _ApLanSubnetMask_Type()
)
apLanSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apLanSubnetMask.setStatus("current")


class _ApLanDhcpServer_Type(Integer32):
    """Custom type apLanDhcpServer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_ApLanDhcpServer_Type.__name__ = "Integer32"
_ApLanDhcpServer_Object = MibScalar
apLanDhcpServer = _ApLanDhcpServer_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 2, 2, 2, 3),
    _ApLanDhcpServer_Type()
)
apLanDhcpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apLanDhcpServer.setStatus("current")
_ApLanDhcpServerStartRange_Type = IpAddress
_ApLanDhcpServerStartRange_Object = MibScalar
apLanDhcpServerStartRange = _ApLanDhcpServerStartRange_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 2, 2, 2, 4),
    _ApLanDhcpServerStartRange_Type()
)
apLanDhcpServerStartRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apLanDhcpServerStartRange.setStatus("current")
_ApLanDhcpServerStopRange_Type = IpAddress
_ApLanDhcpServerStopRange_Object = MibScalar
apLanDhcpServerStopRange = _ApLanDhcpServerStopRange_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 2, 2, 2, 5),
    _ApLanDhcpServerStopRange_Type()
)
apLanDhcpServerStopRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apLanDhcpServerStopRange.setStatus("current")
_ApLanDhcpServerSubnetMask_Type = IpAddress
_ApLanDhcpServerSubnetMask_Object = MibScalar
apLanDhcpServerSubnetMask = _ApLanDhcpServerSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 2, 2, 2, 6),
    _ApLanDhcpServerSubnetMask_Type()
)
apLanDhcpServerSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apLanDhcpServerSubnetMask.setStatus("current")
_ApLanDhcpServerBroadcast_Type = IpAddress
_ApLanDhcpServerBroadcast_Object = MibScalar
apLanDhcpServerBroadcast = _ApLanDhcpServerBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 2, 2, 2, 7),
    _ApLanDhcpServerBroadcast_Type()
)
apLanDhcpServerBroadcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apLanDhcpServerBroadcast.setStatus("current")
_ApLanDhcpServerGateway_Type = IpAddress
_ApLanDhcpServerGateway_Object = MibScalar
apLanDhcpServerGateway = _ApLanDhcpServerGateway_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 2, 2, 2, 8),
    _ApLanDhcpServerGateway_Type()
)
apLanDhcpServerGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apLanDhcpServerGateway.setStatus("current")
_ApLanDhcpServerDns1_Type = IpAddress
_ApLanDhcpServerDns1_Object = MibScalar
apLanDhcpServerDns1 = _ApLanDhcpServerDns1_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 2, 2, 2, 9),
    _ApLanDhcpServerDns1_Type()
)
apLanDhcpServerDns1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apLanDhcpServerDns1.setStatus("current")
_ApLanDhcpServerDns2_Type = IpAddress
_ApLanDhcpServerDns2_Object = MibScalar
apLanDhcpServerDns2 = _ApLanDhcpServerDns2_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 2, 2, 2, 10),
    _ApLanDhcpServerDns2_Type()
)
apLanDhcpServerDns2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apLanDhcpServerDns2.setStatus("current")
_ApLanDhcpServerDns3_Type = IpAddress
_ApLanDhcpServerDns3_Object = MibScalar
apLanDhcpServerDns3 = _ApLanDhcpServerDns3_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 2, 2, 2, 11),
    _ApLanDhcpServerDns3_Type()
)
apLanDhcpServerDns3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apLanDhcpServerDns3.setStatus("current")


class _ApLanDhcpDomain_Type(OctetString):
    """Custom type apLanDhcpDomain based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ApLanDhcpDomain_Type.__name__ = "OctetString"
_ApLanDhcpDomain_Object = MibScalar
apLanDhcpDomain = _ApLanDhcpDomain_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 2, 2, 2, 12),
    _ApLanDhcpDomain_Type()
)
apLanDhcpDomain.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apLanDhcpDomain.setStatus("current")


class _ApLanDhcpRelease_Type(Integer32):
    """Custom type apLanDhcpRelease based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 9999999),
    )


_ApLanDhcpRelease_Type.__name__ = "Integer32"
_ApLanDhcpRelease_Object = MibScalar
apLanDhcpRelease = _ApLanDhcpRelease_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 2, 2, 2, 13),
    _ApLanDhcpRelease_Type()
)
apLanDhcpRelease.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apLanDhcpRelease.setStatus("current")
_ApLanReservationTable_Object = MibTable
apLanReservationTable = _ApLanReservationTable_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 2, 2, 2, 14)
)
if mibBuilder.loadTexts:
    apLanReservationTable.setStatus("current")
_ApLanReservationEntry_Object = MibTableRow
apLanReservationEntry = _ApLanReservationEntry_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 2, 2, 2, 14, 1)
)
apLanReservationEntry.setIndexNames(
    (0, "AP-SYSTEM-NETWORK", "apLanReservationIndex"),
)
if mibBuilder.loadTexts:
    apLanReservationEntry.setStatus("current")
_ApLanReservationIndex_Type = Integer32
_ApLanReservationIndex_Object = MibTableColumn
apLanReservationIndex = _ApLanReservationIndex_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 2, 2, 2, 14, 1, 1),
    _ApLanReservationIndex_Type()
)
apLanReservationIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apLanReservationIndex.setStatus("current")
_ApLanReservationRowControl_Type = RowStatus
_ApLanReservationRowControl_Object = MibTableColumn
apLanReservationRowControl = _ApLanReservationRowControl_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 2, 2, 2, 14, 1, 2),
    _ApLanReservationRowControl_Type()
)
apLanReservationRowControl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apLanReservationRowControl.setStatus("current")
_ApLanReservationMacAddress_Type = MacAddress
_ApLanReservationMacAddress_Object = MibTableColumn
apLanReservationMacAddress = _ApLanReservationMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 2, 2, 2, 14, 1, 3),
    _ApLanReservationMacAddress_Type()
)
apLanReservationMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apLanReservationMacAddress.setStatus("current")
_ApLanReservationIp_Type = IpAddress
_ApLanReservationIp_Object = MibTableColumn
apLanReservationIp = _ApLanReservationIp_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 2, 2, 2, 14, 1, 4),
    _ApLanReservationIp_Type()
)
apLanReservationIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apLanReservationIp.setStatus("current")
_ApPppoeConfig_ObjectIdentity = ObjectIdentity
apPppoeConfig = _ApPppoeConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 2, 2, 3)
)


class _ApPppoeUsername_Type(OctetString):
    """Custom type apPppoeUsername based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ApPppoeUsername_Type.__name__ = "OctetString"
_ApPppoeUsername_Object = MibScalar
apPppoeUsername = _ApPppoeUsername_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 2, 2, 3, 1),
    _ApPppoeUsername_Type()
)
apPppoeUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apPppoeUsername.setStatus("current")


class _ApPppoePassword_Type(OctetString):
    """Custom type apPppoePassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ApPppoePassword_Type.__name__ = "OctetString"
_ApPppoePassword_Object = MibScalar
apPppoePassword = _ApPppoePassword_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 2, 2, 3, 2),
    _ApPppoePassword_Type()
)
apPppoePassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apPppoePassword.setStatus("current")


class _ApPppoeServiceName_Type(OctetString):
    """Custom type apPppoeServiceName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ApPppoeServiceName_Type.__name__ = "OctetString"
_ApPppoeServiceName_Object = MibScalar
apPppoeServiceName = _ApPppoeServiceName_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 2, 2, 3, 3),
    _ApPppoeServiceName_Type()
)
apPppoeServiceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apPppoeServiceName.setStatus("current")
_ApDmzConfig_ObjectIdentity = ObjectIdentity
apDmzConfig = _ApDmzConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 2, 2, 4)
)


class _ApDmzStatus_Type(Integer32):
    """Custom type apDmzStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_ApDmzStatus_Type.__name__ = "Integer32"
_ApDmzStatus_Object = MibScalar
apDmzStatus = _ApDmzStatus_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 2, 2, 4, 1),
    _ApDmzStatus_Type()
)
apDmzStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apDmzStatus.setStatus("current")
_ApDmzIp_Type = IpAddress
_ApDmzIp_Object = MibScalar
apDmzIp = _ApDmzIp_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 2, 2, 4, 2),
    _ApDmzIp_Type()
)
apDmzIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apDmzIp.setStatus("current")
_ApPortForwardTable_Object = MibTable
apPortForwardTable = _ApPortForwardTable_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 2, 2, 5)
)
if mibBuilder.loadTexts:
    apPortForwardTable.setStatus("current")
_ApPortForwardEntry_Object = MibTableRow
apPortForwardEntry = _ApPortForwardEntry_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 2, 2, 5, 1)
)
apPortForwardEntry.setIndexNames(
    (0, "AP-SYSTEM-NETWORK", "apPortForwardIndex"),
)
if mibBuilder.loadTexts:
    apPortForwardEntry.setStatus("current")
_ApPortForwardIndex_Type = Integer32
_ApPortForwardIndex_Object = MibTableColumn
apPortForwardIndex = _ApPortForwardIndex_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 2, 2, 5, 1, 1),
    _ApPortForwardIndex_Type()
)
apPortForwardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apPortForwardIndex.setStatus("current")
_ApPortForwardRowControl_Type = RowStatus
_ApPortForwardRowControl_Object = MibTableColumn
apPortForwardRowControl = _ApPortForwardRowControl_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 2, 2, 5, 1, 2),
    _ApPortForwardRowControl_Type()
)
apPortForwardRowControl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apPortForwardRowControl.setStatus("current")


class _ApPortForwardName_Type(OctetString):
    """Custom type apPortForwardName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ApPortForwardName_Type.__name__ = "OctetString"
_ApPortForwardName_Object = MibTableColumn
apPortForwardName = _ApPortForwardName_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 2, 2, 5, 1, 3),
    _ApPortForwardName_Type()
)
apPortForwardName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apPortForwardName.setStatus("current")
_ApPortForwardToIp_Type = IpAddress
_ApPortForwardToIp_Object = MibTableColumn
apPortForwardToIp = _ApPortForwardToIp_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 2, 2, 5, 1, 4),
    _ApPortForwardToIp_Type()
)
apPortForwardToIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apPortForwardToIp.setStatus("current")


class _ApPortForwardPortProtocol_Type(Integer32):
    """Custom type apPortForwardPortProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("tcp", 0),
          ("udp", 1))
    )


_ApPortForwardPortProtocol_Type.__name__ = "Integer32"
_ApPortForwardPortProtocol_Object = MibTableColumn
apPortForwardPortProtocol = _ApPortForwardPortProtocol_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 2, 2, 5, 1, 5),
    _ApPortForwardPortProtocol_Type()
)
apPortForwardPortProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apPortForwardPortProtocol.setStatus("current")


class _ApPortForwardAppServiceType_Type(Integer32):
    """Custom type apPortForwardAppServiceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              21,
              22,
              23,
              25,
              53,
              80,
              110,
              113,
              123,
              143,
              161,
              162,
              389,
              443,
              514,
              554,
              1352,
              1433,
              1434,
              1494,
              1812,
              1813,
              3389,
              5190,
              33434)
        )
    )
    namedValues = NamedValues(
        *(("aol", 5190),
          ("auth", 113),
          ("citrix", 1494),
          ("dns", 53),
          ("ftp", 21),
          ("http", 80),
          ("https", 443),
          ("iamp", 143),
          ("ldap", 389),
          ("loctusnotes", 1352),
          ("ms-sql-monitor", 1434),
          ("ms-sql-server", 1433),
          ("na", 0),
          ("ntp", 123),
          ("pop3", 110),
          ("radius", 1812),
          ("radius-acct", 1813),
          ("rdp", 3389),
          ("rtsp", 554),
          ("smtp", 25),
          ("snmp", 161),
          ("snmp-trap", 162),
          ("ssh", 22),
          ("syslog", 514),
          ("telnet", 23),
          ("traceroute", 33434))
    )


_ApPortForwardAppServiceType_Type.__name__ = "Integer32"
_ApPortForwardAppServiceType_Object = MibTableColumn
apPortForwardAppServiceType = _ApPortForwardAppServiceType_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 2, 2, 5, 1, 6),
    _ApPortForwardAppServiceType_Type()
)
apPortForwardAppServiceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apPortForwardAppServiceType.setStatus("current")


class _ApPortForwardPortType_Type(Integer32):
    """Custom type apPortForwardPortType based on Integer32"""
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
        *(("port-mapping", 2),
          ("port-range", 1),
          ("range-mapping", 3),
          ("single-port", 0))
    )


_ApPortForwardPortType_Type.__name__ = "Integer32"
_ApPortForwardPortType_Object = MibTableColumn
apPortForwardPortType = _ApPortForwardPortType_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 2, 2, 5, 1, 7),
    _ApPortForwardPortType_Type()
)
apPortForwardPortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apPortForwardPortType.setStatus("current")


class _ApPortForwardFromPort_Type(OctetString):
    """Custom type apPortForwardFromPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 11),
    )


_ApPortForwardFromPort_Type.__name__ = "OctetString"
_ApPortForwardFromPort_Object = MibTableColumn
apPortForwardFromPort = _ApPortForwardFromPort_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 2, 2, 5, 1, 8),
    _ApPortForwardFromPort_Type()
)
apPortForwardFromPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apPortForwardFromPort.setStatus("current")


class _ApPortForwardToPort_Type(OctetString):
    """Custom type apPortForwardToPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_ApPortForwardToPort_Type.__name__ = "OctetString"
_ApPortForwardToPort_Object = MibTableColumn
apPortForwardToPort = _ApPortForwardToPort_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 2, 2, 5, 1, 9),
    _ApPortForwardToPort_Type()
)
apPortForwardToPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apPortForwardToPort.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AP-SYSTEM-NETWORK",
    **{"pepwave": pepwave,
       "productID": productID,
       "apMib": apMib,
       "apGeneralMib": apGeneralMib,
       "ap-system-network-mib": ap_system_network_mib,
       "apNetworkInfo": apNetworkInfo,
       "apWanInfo": apWanInfo,
       "apCurrentIpAddressMode": apCurrentIpAddressMode,
       "apCurrentIpAddress": apCurrentIpAddress,
       "apCurrentSubnetMask": apCurrentSubnetMask,
       "apCurrentGateway": apCurrentGateway,
       "apCurrentDns": apCurrentDns,
       "apPppoeInfo": apPppoeInfo,
       "apPppoeStatus": apPppoeStatus,
       "apPppoeStatusMessage": apPppoeStatusMessage,
       "apNetworkConfig": apNetworkConfig,
       "apWanConfig": apWanConfig,
       "apKeepDefaultIp": apKeepDefaultIp,
       "apIpAddressMode": apIpAddressMode,
       "apIpAddress": apIpAddress,
       "apSubnetMask": apSubnetMask,
       "apGateway": apGateway,
       "apDns": apDns,
       "apLanConfig": apLanConfig,
       "apLanIpAddress": apLanIpAddress,
       "apLanSubnetMask": apLanSubnetMask,
       "apLanDhcpServer": apLanDhcpServer,
       "apLanDhcpServerStartRange": apLanDhcpServerStartRange,
       "apLanDhcpServerStopRange": apLanDhcpServerStopRange,
       "apLanDhcpServerSubnetMask": apLanDhcpServerSubnetMask,
       "apLanDhcpServerBroadcast": apLanDhcpServerBroadcast,
       "apLanDhcpServerGateway": apLanDhcpServerGateway,
       "apLanDhcpServerDns1": apLanDhcpServerDns1,
       "apLanDhcpServerDns2": apLanDhcpServerDns2,
       "apLanDhcpServerDns3": apLanDhcpServerDns3,
       "apLanDhcpDomain": apLanDhcpDomain,
       "apLanDhcpRelease": apLanDhcpRelease,
       "apLanReservationTable": apLanReservationTable,
       "apLanReservationEntry": apLanReservationEntry,
       "apLanReservationIndex": apLanReservationIndex,
       "apLanReservationRowControl": apLanReservationRowControl,
       "apLanReservationMacAddress": apLanReservationMacAddress,
       "apLanReservationIp": apLanReservationIp,
       "apPppoeConfig": apPppoeConfig,
       "apPppoeUsername": apPppoeUsername,
       "apPppoePassword": apPppoePassword,
       "apPppoeServiceName": apPppoeServiceName,
       "apDmzConfig": apDmzConfig,
       "apDmzStatus": apDmzStatus,
       "apDmzIp": apDmzIp,
       "apPortForwardTable": apPortForwardTable,
       "apPortForwardEntry": apPortForwardEntry,
       "apPortForwardIndex": apPortForwardIndex,
       "apPortForwardRowControl": apPortForwardRowControl,
       "apPortForwardName": apPortForwardName,
       "apPortForwardToIp": apPortForwardToIp,
       "apPortForwardPortProtocol": apPortForwardPortProtocol,
       "apPortForwardAppServiceType": apPortForwardAppServiceType,
       "apPortForwardPortType": apPortForwardPortType,
       "apPortForwardFromPort": apPortForwardFromPort,
       "apPortForwardToPort": apPortForwardToPort}
)
