# SNMP MIB module (SALIX-ITX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SALIX-ITX-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:49:29 2024
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

(PhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "PhysicalIndex")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(voip,) = mibBuilder.importSymbols(
    "SALIX-MIB",
    "voip")

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

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

itxMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2158, 3, 2, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ItxMIBObjects_ObjectIdentity = ObjectIdentity
itxMIBObjects = _ItxMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2158, 3, 2, 1, 1)
)
_ItxSystem_ObjectIdentity = ObjectIdentity
itxSystem = _ItxSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2158, 3, 2, 1, 1, 1)
)
_ItxDsp_ObjectIdentity = ObjectIdentity
itxDsp = _ItxDsp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2158, 3, 2, 1, 1, 2)
)
_ItxDspStatusTable_Object = MibTable
itxDspStatusTable = _ItxDspStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 2, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    itxDspStatusTable.setStatus("current")
_ItxDspStatusEntry_Object = MibTableRow
itxDspStatusEntry = _ItxDspStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 2, 1, 1, 2, 1, 1)
)
itxDspStatusEntry.setIndexNames(
    (0, "SALIX-ITX-MIB", "itxDspStatusPhysIndex"),
    (0, "SALIX-ITX-MIB", "itxDspStatusRow"),
    (0, "SALIX-ITX-MIB", "itxDspStatusColumn"),
)
if mibBuilder.loadTexts:
    itxDspStatusEntry.setStatus("current")
_ItxDspStatusPhysIndex_Type = PhysicalIndex
_ItxDspStatusPhysIndex_Object = MibTableColumn
itxDspStatusPhysIndex = _ItxDspStatusPhysIndex_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 2, 1, 1, 2, 1, 1, 1),
    _ItxDspStatusPhysIndex_Type()
)
itxDspStatusPhysIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    itxDspStatusPhysIndex.setStatus("current")


class _ItxDspStatusRow_Type(Integer32):
    """Custom type itxDspStatusRow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_ItxDspStatusRow_Type.__name__ = "Integer32"
_ItxDspStatusRow_Object = MibTableColumn
itxDspStatusRow = _ItxDspStatusRow_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 2, 1, 1, 2, 1, 1, 2),
    _ItxDspStatusRow_Type()
)
itxDspStatusRow.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    itxDspStatusRow.setStatus("current")


class _ItxDspStatusColumn_Type(Integer32):
    """Custom type itxDspStatusColumn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_ItxDspStatusColumn_Type.__name__ = "Integer32"
_ItxDspStatusColumn_Object = MibTableColumn
itxDspStatusColumn = _ItxDspStatusColumn_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 2, 1, 1, 2, 1, 1, 3),
    _ItxDspStatusColumn_Type()
)
itxDspStatusColumn.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    itxDspStatusColumn.setStatus("current")


class _ItxDspStatusOperStatus_Type(Integer32):
    """Custom type itxDspStatusOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("unknown", 3),
          ("up", 1))
    )


_ItxDspStatusOperStatus_Type.__name__ = "Integer32"
_ItxDspStatusOperStatus_Object = MibTableColumn
itxDspStatusOperStatus = _ItxDspStatusOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 2, 1, 1, 2, 1, 1, 4),
    _ItxDspStatusOperStatus_Type()
)
itxDspStatusOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    itxDspStatusOperStatus.setStatus("current")
_ItxMediaController_ObjectIdentity = ObjectIdentity
itxMediaController = _ItxMediaController_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2158, 3, 2, 1, 1, 3)
)
_ItxMediaControllerPrimaryIpAddress_Type = IpAddress
_ItxMediaControllerPrimaryIpAddress_Object = MibScalar
itxMediaControllerPrimaryIpAddress = _ItxMediaControllerPrimaryIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 2, 1, 1, 3, 1),
    _ItxMediaControllerPrimaryIpAddress_Type()
)
itxMediaControllerPrimaryIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    itxMediaControllerPrimaryIpAddress.setStatus("current")


class _ItxMediaControllerPrimaryPort_Type(Integer32):
    """Custom type itxMediaControllerPrimaryPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ItxMediaControllerPrimaryPort_Type.__name__ = "Integer32"
_ItxMediaControllerPrimaryPort_Object = MibScalar
itxMediaControllerPrimaryPort = _ItxMediaControllerPrimaryPort_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 2, 1, 1, 3, 2),
    _ItxMediaControllerPrimaryPort_Type()
)
itxMediaControllerPrimaryPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    itxMediaControllerPrimaryPort.setStatus("current")
_ItxMediaControllerSecondaryIpAddress_Type = IpAddress
_ItxMediaControllerSecondaryIpAddress_Object = MibScalar
itxMediaControllerSecondaryIpAddress = _ItxMediaControllerSecondaryIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 2, 1, 1, 3, 3),
    _ItxMediaControllerSecondaryIpAddress_Type()
)
itxMediaControllerSecondaryIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    itxMediaControllerSecondaryIpAddress.setStatus("current")


class _ItxMediaControllerSecondaryPort_Type(Integer32):
    """Custom type itxMediaControllerSecondaryPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ItxMediaControllerSecondaryPort_Type.__name__ = "Integer32"
_ItxMediaControllerSecondaryPort_Object = MibScalar
itxMediaControllerSecondaryPort = _ItxMediaControllerSecondaryPort_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 2, 1, 1, 3, 4),
    _ItxMediaControllerSecondaryPort_Type()
)
itxMediaControllerSecondaryPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    itxMediaControllerSecondaryPort.setStatus("current")


class _ItxMediaControllerActiveController_Type(Integer32):
    """Custom type itxMediaControllerActiveController based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2))
    )


_ItxMediaControllerActiveController_Type.__name__ = "Integer32"
_ItxMediaControllerActiveController_Object = MibScalar
itxMediaControllerActiveController = _ItxMediaControllerActiveController_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 2, 1, 1, 3, 5),
    _ItxMediaControllerActiveController_Type()
)
itxMediaControllerActiveController.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    itxMediaControllerActiveController.setStatus("current")
_ItxIsdnBackHaulMediaControllerIpAddress_Type = IpAddress
_ItxIsdnBackHaulMediaControllerIpAddress_Object = MibScalar
itxIsdnBackHaulMediaControllerIpAddress = _ItxIsdnBackHaulMediaControllerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 2, 1, 1, 3, 6),
    _ItxIsdnBackHaulMediaControllerIpAddress_Type()
)
itxIsdnBackHaulMediaControllerIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    itxIsdnBackHaulMediaControllerIpAddress.setStatus("current")


class _ItxIsdnBackHaulMediaControllerPort_Type(Integer32):
    """Custom type itxIsdnBackHaulMediaControllerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ItxIsdnBackHaulMediaControllerPort_Type.__name__ = "Integer32"
_ItxIsdnBackHaulMediaControllerPort_Object = MibScalar
itxIsdnBackHaulMediaControllerPort = _ItxIsdnBackHaulMediaControllerPort_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 2, 1, 1, 3, 7),
    _ItxIsdnBackHaulMediaControllerPort_Type()
)
itxIsdnBackHaulMediaControllerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    itxIsdnBackHaulMediaControllerPort.setStatus("current")
_ItxMediaSubnet_Type = IpAddress
_ItxMediaSubnet_Object = MibScalar
itxMediaSubnet = _ItxMediaSubnet_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 2, 1, 1, 4),
    _ItxMediaSubnet_Type()
)
itxMediaSubnet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    itxMediaSubnet.setStatus("current")


class _ItxMediaSubnetMask_Type(IpAddress):
    """Custom type itxMediaSubnetMask based on IpAddress"""
    defaultHexValue = "FFFFFFFF"


_ItxMediaSubnetMask_Object = MibScalar
itxMediaSubnetMask = _ItxMediaSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 2, 1, 1, 5),
    _ItxMediaSubnetMask_Type()
)
itxMediaSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    itxMediaSubnetMask.setStatus("current")
_ItxNetworkManagementAddress_Type = IpAddress
_ItxNetworkManagementAddress_Object = MibScalar
itxNetworkManagementAddress = _ItxNetworkManagementAddress_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 2, 1, 1, 7),
    _ItxNetworkManagementAddress_Type()
)
itxNetworkManagementAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    itxNetworkManagementAddress.setStatus("current")
_ItxNetworkManagementSubnetMask_Type = IpAddress
_ItxNetworkManagementSubnetMask_Object = MibScalar
itxNetworkManagementSubnetMask = _ItxNetworkManagementSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 2, 1, 1, 8),
    _ItxNetworkManagementSubnetMask_Type()
)
itxNetworkManagementSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    itxNetworkManagementSubnetMask.setStatus("current")
_ItxCallControlAddress_Type = IpAddress
_ItxCallControlAddress_Object = MibScalar
itxCallControlAddress = _ItxCallControlAddress_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 2, 1, 1, 10),
    _ItxCallControlAddress_Type()
)
itxCallControlAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    itxCallControlAddress.setStatus("current")
_ItxCallControlSubnetMask_Type = IpAddress
_ItxCallControlSubnetMask_Object = MibScalar
itxCallControlSubnetMask = _ItxCallControlSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 2, 1, 1, 11),
    _ItxCallControlSubnetMask_Type()
)
itxCallControlSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    itxCallControlSubnetMask.setStatus("current")
_ItxSnmpManagementEntityIpAddress_Type = IpAddress
_ItxSnmpManagementEntityIpAddress_Object = MibScalar
itxSnmpManagementEntityIpAddress = _ItxSnmpManagementEntityIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 2, 1, 1, 13),
    _ItxSnmpManagementEntityIpAddress_Type()
)
itxSnmpManagementEntityIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    itxSnmpManagementEntityIpAddress.setStatus("current")


class _ItxSnmpManagementEntityPort_Type(Integer32):
    """Custom type itxSnmpManagementEntityPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ItxSnmpManagementEntityPort_Type.__name__ = "Integer32"
_ItxSnmpManagementEntityPort_Object = MibScalar
itxSnmpManagementEntityPort = _ItxSnmpManagementEntityPort_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 2, 1, 1, 14),
    _ItxSnmpManagementEntityPort_Type()
)
itxSnmpManagementEntityPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    itxSnmpManagementEntityPort.setStatus("current")
_ItxEthernetTable_Object = MibTable
itxEthernetTable = _ItxEthernetTable_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 2, 1, 1, 15)
)
if mibBuilder.loadTexts:
    itxEthernetTable.setStatus("current")
_ItxEthernetEntry_Object = MibTableRow
itxEthernetEntry = _ItxEthernetEntry_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 2, 1, 1, 15, 1)
)
itxEthernetEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    itxEthernetEntry.setStatus("current")
_ItxDefaultGateway_Type = IpAddress
_ItxDefaultGateway_Object = MibTableColumn
itxDefaultGateway = _ItxDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 2, 1, 1, 15, 1, 1),
    _ItxDefaultGateway_Type()
)
itxDefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    itxDefaultGateway.setStatus("current")
_ItxIpAddress_Type = IpAddress
_ItxIpAddress_Object = MibTableColumn
itxIpAddress = _ItxIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 2, 1, 1, 15, 1, 2),
    _ItxIpAddress_Type()
)
itxIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    itxIpAddress.setStatus("current")
_ItxSubnetMask_Type = IpAddress
_ItxSubnetMask_Object = MibTableColumn
itxSubnetMask = _ItxSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 2, 1, 1, 15, 1, 3),
    _ItxSubnetMask_Type()
)
itxSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    itxSubnetMask.setStatus("current")


class _ItxCallControlProtocol_Type(Integer32):
    """Custom type itxCallControlProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ipdcVersion0dot15", 1),
          ("mgcpVersion0dot1", 3),
          ("sgcpVersion0", 2))
    )


_ItxCallControlProtocol_Type.__name__ = "Integer32"
_ItxCallControlProtocol_Object = MibScalar
itxCallControlProtocol = _ItxCallControlProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 2, 1, 1, 16),
    _ItxCallControlProtocol_Type()
)
itxCallControlProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    itxCallControlProtocol.setStatus("current")


class _ItxCompandingLaw_Type(Integer32):
    """Custom type itxCompandingLaw based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("aLaw", 0),
          ("muLaw", 1))
    )


_ItxCompandingLaw_Type.__name__ = "Integer32"
_ItxCompandingLaw_Object = MibScalar
itxCompandingLaw = _ItxCompandingLaw_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 2, 1, 1, 18),
    _ItxCompandingLaw_Type()
)
itxCompandingLaw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    itxCompandingLaw.setStatus("current")
_ItxDnsIpAddress_Type = IpAddress
_ItxDnsIpAddress_Object = MibScalar
itxDnsIpAddress = _ItxDnsIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 2, 1, 1, 19),
    _ItxDnsIpAddress_Type()
)
itxDnsIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    itxDnsIpAddress.setStatus("current")


class _ItxHostname_Type(DisplayString):
    """Custom type itxHostname based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_ItxHostname_Type.__name__ = "DisplayString"
_ItxHostname_Object = MibScalar
itxHostname = _ItxHostname_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 2, 1, 1, 20),
    _ItxHostname_Type()
)
itxHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    itxHostname.setStatus("current")


class _ItxEthernetLoadSharing_Type(Integer32):
    """Custom type itxEthernetLoadSharing based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 0))
    )


_ItxEthernetLoadSharing_Type.__name__ = "Integer32"
_ItxEthernetLoadSharing_Object = MibScalar
itxEthernetLoadSharing = _ItxEthernetLoadSharing_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 2, 1, 1, 21),
    _ItxEthernetLoadSharing_Type()
)
itxEthernetLoadSharing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    itxEthernetLoadSharing.setStatus("current")
_ItxNFSObjects_ObjectIdentity = ObjectIdentity
itxNFSObjects = _ItxNFSObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2158, 3, 2, 1, 1, 22)
)
_ItxNFSIpAddress_Type = IpAddress
_ItxNFSIpAddress_Object = MibScalar
itxNFSIpAddress = _ItxNFSIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 2, 1, 1, 22, 1),
    _ItxNFSIpAddress_Type()
)
itxNFSIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    itxNFSIpAddress.setStatus("current")


class _ItxNFSPath_Type(DisplayString):
    """Custom type itxNFSPath based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_ItxNFSPath_Type.__name__ = "DisplayString"
_ItxNFSPath_Object = MibScalar
itxNFSPath = _ItxNFSPath_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 2, 1, 1, 22, 2),
    _ItxNFSPath_Type()
)
itxNFSPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    itxNFSPath.setStatus("current")
_ItxNFSUserId_Type = Integer32
_ItxNFSUserId_Object = MibScalar
itxNFSUserId = _ItxNFSUserId_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 2, 1, 1, 22, 3),
    _ItxNFSUserId_Type()
)
itxNFSUserId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    itxNFSUserId.setStatus("current")
_ItxNFSGroupId_Type = Integer32
_ItxNFSGroupId_Object = MibScalar
itxNFSGroupId = _ItxNFSGroupId_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 2, 1, 1, 22, 4),
    _ItxNFSGroupId_Type()
)
itxNFSGroupId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    itxNFSGroupId.setStatus("current")


class _ItxNFSStatus_Type(Integer32):
    """Custom type itxNFSStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mounted", 1),
          ("unmounted", 2))
    )


_ItxNFSStatus_Type.__name__ = "Integer32"
_ItxNFSStatus_Object = MibScalar
itxNFSStatus = _ItxNFSStatus_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 2, 1, 1, 22, 5),
    _ItxNFSStatus_Type()
)
itxNFSStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    itxNFSStatus.setStatus("current")
_ItxMIBTraps_ObjectIdentity = ObjectIdentity
itxMIBTraps = _ItxMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2158, 3, 2, 1, 2)
)
_ItxMIBTrapPrefix_ObjectIdentity = ObjectIdentity
itxMIBTrapPrefix = _ItxMIBTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2158, 3, 2, 1, 2, 0)
)
_ItxMIBCompliance_ObjectIdentity = ObjectIdentity
itxMIBCompliance = _ItxMIBCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2158, 3, 2, 1, 3)
)
_ItxGroups_ObjectIdentity = ObjectIdentity
itxGroups = _ItxGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2158, 3, 2, 1, 3, 1)
)
_ItxCompliances_ObjectIdentity = ObjectIdentity
itxCompliances = _ItxCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2158, 3, 2, 1, 3, 2)
)

# Managed Objects groups

itxDspGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2158, 3, 2, 1, 3, 1, 4)
)
itxDspGroup.setObjects(
    ("SALIX-ITX-MIB", "itxDspStatusOperStatus")
)
if mibBuilder.loadTexts:
    itxDspGroup.setStatus("current")

itxMediaControllerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2158, 3, 2, 1, 3, 1, 7)
)
itxMediaControllerGroup.setObjects(
      *(("SALIX-ITX-MIB", "itxMediaControllerPrimaryIpAddress"),
        ("SALIX-ITX-MIB", "itxMediaControllerPrimaryPort"),
        ("SALIX-ITX-MIB", "itxMediaControllerSecondaryIpAddress"),
        ("SALIX-ITX-MIB", "itxMediaControllerSecondaryPort"))
)
if mibBuilder.loadTexts:
    itxMediaControllerGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

itxCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2158, 3, 2, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    itxCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SALIX-ITX-MIB",
    **{"itxMIB": itxMIB,
       "itxMIBObjects": itxMIBObjects,
       "itxSystem": itxSystem,
       "itxDsp": itxDsp,
       "itxDspStatusTable": itxDspStatusTable,
       "itxDspStatusEntry": itxDspStatusEntry,
       "itxDspStatusPhysIndex": itxDspStatusPhysIndex,
       "itxDspStatusRow": itxDspStatusRow,
       "itxDspStatusColumn": itxDspStatusColumn,
       "itxDspStatusOperStatus": itxDspStatusOperStatus,
       "itxMediaController": itxMediaController,
       "itxMediaControllerPrimaryIpAddress": itxMediaControllerPrimaryIpAddress,
       "itxMediaControllerPrimaryPort": itxMediaControllerPrimaryPort,
       "itxMediaControllerSecondaryIpAddress": itxMediaControllerSecondaryIpAddress,
       "itxMediaControllerSecondaryPort": itxMediaControllerSecondaryPort,
       "itxMediaControllerActiveController": itxMediaControllerActiveController,
       "itxIsdnBackHaulMediaControllerIpAddress": itxIsdnBackHaulMediaControllerIpAddress,
       "itxIsdnBackHaulMediaControllerPort": itxIsdnBackHaulMediaControllerPort,
       "itxMediaSubnet": itxMediaSubnet,
       "itxMediaSubnetMask": itxMediaSubnetMask,
       "itxNetworkManagementAddress": itxNetworkManagementAddress,
       "itxNetworkManagementSubnetMask": itxNetworkManagementSubnetMask,
       "itxCallControlAddress": itxCallControlAddress,
       "itxCallControlSubnetMask": itxCallControlSubnetMask,
       "itxSnmpManagementEntityIpAddress": itxSnmpManagementEntityIpAddress,
       "itxSnmpManagementEntityPort": itxSnmpManagementEntityPort,
       "itxEthernetTable": itxEthernetTable,
       "itxEthernetEntry": itxEthernetEntry,
       "itxDefaultGateway": itxDefaultGateway,
       "itxIpAddress": itxIpAddress,
       "itxSubnetMask": itxSubnetMask,
       "itxCallControlProtocol": itxCallControlProtocol,
       "itxCompandingLaw": itxCompandingLaw,
       "itxDnsIpAddress": itxDnsIpAddress,
       "itxHostname": itxHostname,
       "itxEthernetLoadSharing": itxEthernetLoadSharing,
       "itxNFSObjects": itxNFSObjects,
       "itxNFSIpAddress": itxNFSIpAddress,
       "itxNFSPath": itxNFSPath,
       "itxNFSUserId": itxNFSUserId,
       "itxNFSGroupId": itxNFSGroupId,
       "itxNFSStatus": itxNFSStatus,
       "itxMIBTraps": itxMIBTraps,
       "itxMIBTrapPrefix": itxMIBTrapPrefix,
       "itxMIBCompliance": itxMIBCompliance,
       "itxGroups": itxGroups,
       "itxDspGroup": itxDspGroup,
       "itxMediaControllerGroup": itxMediaControllerGroup,
       "itxCompliances": itxCompliances,
       "itxCompliance": itxCompliance}
)
