# SNMP MIB module (LINKSYS-MODEL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/LINKSYS-MODEL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:18:24 2024
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

(OwnerString,) = mibBuilder.importSymbols(
    "IF-MIB",
    "OwnerString")

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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Internet_ObjectIdentity = ObjectIdentity
internet = _Internet_ObjectIdentity(
    (1, 3, 6, 1)
)
_Directory_ObjectIdentity = ObjectIdentity
directory = _Directory_ObjectIdentity(
    (1, 3, 6, 1, 1)
)
_Mgmt_ObjectIdentity = ObjectIdentity
mgmt = _Mgmt_ObjectIdentity(
    (1, 3, 6, 1, 2)
)
_Experimental_ObjectIdentity = ObjectIdentity
experimental = _Experimental_ObjectIdentity(
    (1, 3, 6, 1, 3)
)
_Private_ObjectIdentity = ObjectIdentity
private = _Private_ObjectIdentity(
    (1, 3, 6, 1, 4)
)
_Enterprises_ObjectIdentity = ObjectIdentity
enterprises = _Enterprises_ObjectIdentity(
    (1, 3, 6, 1, 4, 1)
)
_Linksys_ObjectIdentity = ObjectIdentity
linksys = _Linksys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3955)
)
_Common_ObjectIdentity = ObjectIdentity
common = _Common_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3955, 1)
)
_CommonModelId_Type = OwnerString
_CommonModelId_Object = MibScalar
commonModelId = _CommonModelId_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1, 1),
    _CommonModelId_Type()
)
commonModelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commonModelId.setStatus("mandatory")
_CommonSoftwareVer_Type = OwnerString
_CommonSoftwareVer_Object = MibScalar
commonSoftwareVer = _CommonSoftwareVer_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1, 2),
    _CommonSoftwareVer_Type()
)
commonSoftwareVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commonSoftwareVer.setStatus("mandatory")
_CommonFirmwareVer_Type = OwnerString
_CommonFirmwareVer_Object = MibScalar
commonFirmwareVer = _CommonFirmwareVer_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1, 3),
    _CommonFirmwareVer_Type()
)
commonFirmwareVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commonFirmwareVer.setStatus("mandatory")
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3955, 2)
)
_SnmpMgt_ObjectIdentity = ObjectIdentity
snmpMgt = _SnmpMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3955, 3)
)
_CommonMgt_ObjectIdentity = ObjectIdentity
commonMgt = _CommonMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3955, 3, 1)
)


class _MgtWarmStart_Type(Integer32):
    """Custom type mgtWarmStart based on Integer32"""
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


_MgtWarmStart_Type.__name__ = "Integer32"
_MgtWarmStart_Object = MibScalar
mgtWarmStart = _MgtWarmStart_Object(
    (1, 3, 6, 1, 4, 1, 3955, 3, 1, 1),
    _MgtWarmStart_Type()
)
mgtWarmStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgtWarmStart.setStatus("mandatory")


class _MgtFactoryReset_Type(Integer32):
    """Custom type mgtFactoryReset based on Integer32"""
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


_MgtFactoryReset_Type.__name__ = "Integer32"
_MgtFactoryReset_Object = MibScalar
mgtFactoryReset = _MgtFactoryReset_Object(
    (1, 3, 6, 1, 4, 1, 3955, 3, 1, 2),
    _MgtFactoryReset_Type()
)
mgtFactoryReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgtFactoryReset.setStatus("mandatory")


class _MgtAdministrator_Type(OwnerString):
    """Custom type mgtAdministrator based on OwnerString"""
    subtypeSpec = OwnerString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_MgtAdministrator_Type.__name__ = "OwnerString"
_MgtAdministrator_Object = MibScalar
mgtAdministrator = _MgtAdministrator_Object(
    (1, 3, 6, 1, 4, 1, 3955, 3, 1, 3),
    _MgtAdministrator_Type()
)
mgtAdministrator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgtAdministrator.setStatus("mandatory")


class _MgtBootStatus_Type(Integer32):
    """Custom type mgtBootStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("abnormal", 0),
          ("normal", 1))
    )


_MgtBootStatus_Type.__name__ = "Integer32"
_MgtBootStatus_Object = MibScalar
mgtBootStatus = _MgtBootStatus_Object(
    (1, 3, 6, 1, 4, 1, 3955, 3, 1, 4),
    _MgtBootStatus_Type()
)
mgtBootStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgtBootStatus.setStatus("mandatory")


class _MgtRefreshMIB_Type(Integer32):
    """Custom type mgtRefreshMIB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("apply", 1),
          ("none", 0))
    )


_MgtRefreshMIB_Type.__name__ = "Integer32"
_MgtRefreshMIB_Object = MibScalar
mgtRefreshMIB = _MgtRefreshMIB_Object(
    (1, 3, 6, 1, 4, 1, 3955, 3, 1, 5),
    _MgtRefreshMIB_Type()
)
mgtRefreshMIB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgtRefreshMIB.setStatus("mandatory")


class _MgtUpdateNV_Type(Integer32):
    """Custom type mgtUpdateNV based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("apply", 1),
          ("none", 0))
    )


_MgtUpdateNV_Type.__name__ = "Integer32"
_MgtUpdateNV_Object = MibScalar
mgtUpdateNV = _MgtUpdateNV_Object(
    (1, 3, 6, 1, 4, 1, 3955, 3, 1, 6),
    _MgtUpdateNV_Type()
)
mgtUpdateNV.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgtUpdateNV.setStatus("mandatory")
_MgtCommunityTable_Object = MibTable
mgtCommunityTable = _MgtCommunityTable_Object(
    (1, 3, 6, 1, 4, 1, 3955, 3, 1, 7)
)
if mibBuilder.loadTexts:
    mgtCommunityTable.setStatus("mandatory")
_MgtCommunityEntry_Object = MibTableRow
mgtCommunityEntry = _MgtCommunityEntry_Object(
    (1, 3, 6, 1, 4, 1, 3955, 3, 1, 7, 1)
)
mgtCommunityEntry.setIndexNames(
    (0, "LINKSYS-MODEL-MIB", "mgtCommunityIndex"),
)
if mibBuilder.loadTexts:
    mgtCommunityEntry.setStatus("mandatory")
_MgtCommunityIndex_Type = Integer32
_MgtCommunityIndex_Object = MibTableColumn
mgtCommunityIndex = _MgtCommunityIndex_Object(
    (1, 3, 6, 1, 4, 1, 3955, 3, 1, 7, 1, 1),
    _MgtCommunityIndex_Type()
)
mgtCommunityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgtCommunityIndex.setStatus("mandatory")


class _MgtCommunityName_Type(OwnerString):
    """Custom type mgtCommunityName based on OwnerString"""
    subtypeSpec = OwnerString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MgtCommunityName_Type.__name__ = "OwnerString"
_MgtCommunityName_Object = MibTableColumn
mgtCommunityName = _MgtCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 3955, 3, 1, 7, 1, 2),
    _MgtCommunityName_Type()
)
mgtCommunityName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgtCommunityName.setStatus("mandatory")


class _MgtCommunityType_Type(Integer32):
    """Custom type mgtCommunityType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("read-only", 1),
          ("read-write", 2))
    )


_MgtCommunityType_Type.__name__ = "Integer32"
_MgtCommunityType_Object = MibTableColumn
mgtCommunityType = _MgtCommunityType_Object(
    (1, 3, 6, 1, 4, 1, 3955, 3, 1, 7, 1, 3),
    _MgtCommunityType_Type()
)
mgtCommunityType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgtCommunityType.setStatus("mandatory")
_InternetAccessMgt_ObjectIdentity = ObjectIdentity
internetAccessMgt = _InternetAccessMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3955, 3, 4)
)
_BroadbandGateway_ObjectIdentity = ObjectIdentity
broadbandGateway = _BroadbandGateway_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3955, 3, 4, 1)
)


class _HostName_Type(OwnerString):
    """Custom type hostName based on OwnerString"""
    subtypeSpec = OwnerString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HostName_Type.__name__ = "OwnerString"
_HostName_Object = MibScalar
hostName = _HostName_Object(
    (1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 1),
    _HostName_Type()
)
hostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hostName.setStatus("mandatory")


class _DomainName_Type(OwnerString):
    """Custom type domainName based on OwnerString"""
    subtypeSpec = OwnerString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_DomainName_Type.__name__ = "OwnerString"
_DomainName_Object = MibScalar
domainName = _DomainName_Object(
    (1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 2),
    _DomainName_Type()
)
domainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    domainName.setStatus("mandatory")
_NetAddressLAN_Type = IpAddress
_NetAddressLAN_Object = MibScalar
netAddressLAN = _NetAddressLAN_Object(
    (1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 3),
    _NetAddressLAN_Type()
)
netAddressLAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netAddressLAN.setStatus("mandatory")
_PhysicalAddrLAN_Type = PhysAddress
_PhysicalAddrLAN_Object = MibScalar
physicalAddrLAN = _PhysicalAddrLAN_Object(
    (1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 4),
    _PhysicalAddrLAN_Type()
)
physicalAddrLAN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalAddrLAN.setStatus("mandatory")
_SubnetMaskLAN_Type = IpAddress
_SubnetMaskLAN_Object = MibScalar
subnetMaskLAN = _SubnetMaskLAN_Object(
    (1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 5),
    _SubnetMaskLAN_Type()
)
subnetMaskLAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subnetMaskLAN.setStatus("mandatory")


class _DhcpStatusWAN_Type(Integer32):
    """Custom type dhcpStatusWAN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("specific", 1))
    )


_DhcpStatusWAN_Type.__name__ = "Integer32"
_DhcpStatusWAN_Object = MibScalar
dhcpStatusWAN = _DhcpStatusWAN_Object(
    (1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 6),
    _DhcpStatusWAN_Type()
)
dhcpStatusWAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpStatusWAN.setStatus("mandatory")
_NetAddressWAN_Type = IpAddress
_NetAddressWAN_Object = MibScalar
netAddressWAN = _NetAddressWAN_Object(
    (1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 7),
    _NetAddressWAN_Type()
)
netAddressWAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netAddressWAN.setStatus("mandatory")
_PhysicalAddrWAN_Type = PhysAddress
_PhysicalAddrWAN_Object = MibScalar
physicalAddrWAN = _PhysicalAddrWAN_Object(
    (1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 8),
    _PhysicalAddrWAN_Type()
)
physicalAddrWAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    physicalAddrWAN.setStatus("mandatory")
_SubnetMaskWAN_Type = IpAddress
_SubnetMaskWAN_Object = MibScalar
subnetMaskWAN = _SubnetMaskWAN_Object(
    (1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 9),
    _SubnetMaskWAN_Type()
)
subnetMaskWAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subnetMaskWAN.setStatus("mandatory")
_DefaultbroadbandGatewayWAN_Type = IpAddress
_DefaultbroadbandGatewayWAN_Object = MibScalar
defaultbroadbandGatewayWAN = _DefaultbroadbandGatewayWAN_Object(
    (1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 10),
    _DefaultbroadbandGatewayWAN_Type()
)
defaultbroadbandGatewayWAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultbroadbandGatewayWAN.setStatus("mandatory")


class _LoginStatus_Type(Integer32):
    """Custom type loginStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("pppoe", 1),
          ("ras", 2))
    )


_LoginStatus_Type.__name__ = "Integer32"
_LoginStatus_Object = MibScalar
loginStatus = _LoginStatus_Object(
    (1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 11),
    _LoginStatus_Type()
)
loginStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loginStatus.setStatus("mandatory")


class _LoginUserName_Type(OwnerString):
    """Custom type loginUserName based on OwnerString"""
    subtypeSpec = OwnerString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_LoginUserName_Type.__name__ = "OwnerString"
_LoginUserName_Object = MibScalar
loginUserName = _LoginUserName_Object(
    (1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 12),
    _LoginUserName_Type()
)
loginUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loginUserName.setStatus("mandatory")


class _LoginPassword_Type(OwnerString):
    """Custom type loginPassword based on OwnerString"""
    subtypeSpec = OwnerString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_LoginPassword_Type.__name__ = "OwnerString"
_LoginPassword_Object = MibScalar
loginPassword = _LoginPassword_Object(
    (1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 13),
    _LoginPassword_Type()
)
loginPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loginPassword.setStatus("mandatory")


class _RasPlan_Type(Integer32):
    """Custom type rasPlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ethernet-256k", 1),
          ("ethernet-512k", 0))
    )


_RasPlan_Type.__name__ = "Integer32"
_RasPlan_Object = MibScalar
rasPlan = _RasPlan_Object(
    (1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 14),
    _RasPlan_Type()
)
rasPlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rasPlan.setStatus("mandatory")


class _ConnectedState_Type(Integer32):
    """Custom type connectedState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("keepAlive", 0),
          ("onDemand", 1))
    )


_ConnectedState_Type.__name__ = "Integer32"
_ConnectedState_Object = MibScalar
connectedState = _ConnectedState_Object(
    (1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 15),
    _ConnectedState_Type()
)
connectedState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connectedState.setStatus("mandatory")
_ConnectedIdleTime_Type = Integer32
_ConnectedIdleTime_Object = MibScalar
connectedIdleTime = _ConnectedIdleTime_Object(
    (1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 16),
    _ConnectedIdleTime_Type()
)
connectedIdleTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connectedIdleTime.setStatus("mandatory")


class _DhcpStatusLAN_Type(Integer32):
    """Custom type dhcpStatusLAN based on Integer32"""
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


_DhcpStatusLAN_Type.__name__ = "Integer32"
_DhcpStatusLAN_Object = MibScalar
dhcpStatusLAN = _DhcpStatusLAN_Object(
    (1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 17),
    _DhcpStatusLAN_Type()
)
dhcpStatusLAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpStatusLAN.setStatus("mandatory")
_DhcpStartNetAddr_Type = IpAddress
_DhcpStartNetAddr_Object = MibScalar
dhcpStartNetAddr = _DhcpStartNetAddr_Object(
    (1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 18),
    _DhcpStartNetAddr_Type()
)
dhcpStartNetAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpStartNetAddr.setStatus("mandatory")
_DhcpNumberUsers_Type = Integer32
_DhcpNumberUsers_Object = MibScalar
dhcpNumberUsers = _DhcpNumberUsers_Object(
    (1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 19),
    _DhcpNumberUsers_Type()
)
dhcpNumberUsers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpNumberUsers.setStatus("mandatory")


class _WorkingMode_Type(Integer32):
    """Custom type workingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("broadbandGateway", 1),
          ("router", 2))
    )


_WorkingMode_Type.__name__ = "Integer32"
_WorkingMode_Object = MibScalar
workingMode = _WorkingMode_Object(
    (1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 20),
    _WorkingMode_Type()
)
workingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    workingMode.setStatus("mandatory")


class _DynamicRoutingTX_Type(Integer32):
    """Custom type dynamicRoutingTX based on Integer32"""
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
        *(("disable", 0),
          ("rip1", 1),
          ("rip1-compatible", 2),
          ("rip2", 3))
    )


_DynamicRoutingTX_Type.__name__ = "Integer32"
_DynamicRoutingTX_Object = MibScalar
dynamicRoutingTX = _DynamicRoutingTX_Object(
    (1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 21),
    _DynamicRoutingTX_Type()
)
dynamicRoutingTX.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dynamicRoutingTX.setStatus("mandatory")


class _DynamicRoutingRX_Type(Integer32):
    """Custom type dynamicRoutingRX based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("rip1", 1),
          ("rip2", 2))
    )


_DynamicRoutingRX_Type.__name__ = "Integer32"
_DynamicRoutingRX_Object = MibScalar
dynamicRoutingRX = _DynamicRoutingRX_Object(
    (1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 22),
    _DynamicRoutingRX_Type()
)
dynamicRoutingRX.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dynamicRoutingRX.setStatus("mandatory")


class _SpiStatus_Type(Integer32):
    """Custom type spiStatus based on Integer32"""
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


_SpiStatus_Type.__name__ = "Integer32"
_SpiStatus_Object = MibScalar
spiStatus = _SpiStatus_Object(
    (1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 23),
    _SpiStatus_Type()
)
spiStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spiStatus.setStatus("mandatory")


class _WanReqBlockStatus_Type(Integer32):
    """Custom type wanReqBlockStatus based on Integer32"""
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


_WanReqBlockStatus_Type.__name__ = "Integer32"
_WanReqBlockStatus_Object = MibScalar
wanReqBlockStatus = _WanReqBlockStatus_Object(
    (1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 24),
    _WanReqBlockStatus_Type()
)
wanReqBlockStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanReqBlockStatus.setStatus("mandatory")


class _IpSecPassThroughStatus_Type(Integer32):
    """Custom type ipSecPassThroughStatus based on Integer32"""
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


_IpSecPassThroughStatus_Type.__name__ = "Integer32"
_IpSecPassThroughStatus_Object = MibScalar
ipSecPassThroughStatus = _IpSecPassThroughStatus_Object(
    (1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 25),
    _IpSecPassThroughStatus_Type()
)
ipSecPassThroughStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSecPassThroughStatus.setStatus("mandatory")


class _PptpPassThroughStatus_Type(Integer32):
    """Custom type pptpPassThroughStatus based on Integer32"""
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


_PptpPassThroughStatus_Type.__name__ = "Integer32"
_PptpPassThroughStatus_Object = MibScalar
pptpPassThroughStatus = _PptpPassThroughStatus_Object(
    (1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 26),
    _PptpPassThroughStatus_Type()
)
pptpPassThroughStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pptpPassThroughStatus.setStatus("mandatory")


class _RemoteMgtStatus_Type(Integer32):
    """Custom type remoteMgtStatus based on Integer32"""
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


_RemoteMgtStatus_Type.__name__ = "Integer32"
_RemoteMgtStatus_Object = MibScalar
remoteMgtStatus = _RemoteMgtStatus_Object(
    (1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 27),
    _RemoteMgtStatus_Type()
)
remoteMgtStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteMgtStatus.setStatus("mandatory")


class _RemoteUpgradeStatus_Type(Integer32):
    """Custom type remoteUpgradeStatus based on Integer32"""
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


_RemoteUpgradeStatus_Type.__name__ = "Integer32"
_RemoteUpgradeStatus_Object = MibScalar
remoteUpgradeStatus = _RemoteUpgradeStatus_Object(
    (1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 28),
    _RemoteUpgradeStatus_Type()
)
remoteUpgradeStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteUpgradeStatus.setStatus("mandatory")


class _AccessLogStatus_Type(Integer32):
    """Custom type accessLogStatus based on Integer32"""
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


_AccessLogStatus_Type.__name__ = "Integer32"
_AccessLogStatus_Object = MibScalar
accessLogStatus = _AccessLogStatus_Object(
    (1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 29),
    _AccessLogStatus_Type()
)
accessLogStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accessLogStatus.setStatus("mandatory")
_DmzHostIPAddress_Type = IpAddress
_DmzHostIPAddress_Object = MibScalar
dmzHostIPAddress = _DmzHostIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 30),
    _DmzHostIPAddress_Type()
)
dmzHostIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmzHostIPAddress.setStatus("mandatory")


class _QosStatus_Type(Integer32):
    """Custom type qosStatus based on Integer32"""
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


_QosStatus_Type.__name__ = "Integer32"
_QosStatus_Object = MibScalar
qosStatus = _QosStatus_Object(
    (1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 31),
    _QosStatus_Type()
)
qosStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosStatus.setStatus("mandatory")
_DhcpActiveTable_Object = MibTable
dhcpActiveTable = _DhcpActiveTable_Object(
    (1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 32)
)
if mibBuilder.loadTexts:
    dhcpActiveTable.setStatus("mandatory")
_DhcpActiveEntry_Object = MibTableRow
dhcpActiveEntry = _DhcpActiveEntry_Object(
    (1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 32, 1)
)
dhcpActiveEntry.setIndexNames(
    (0, "LINKSYS-MODEL-MIB", "dhcpActiveIndex"),
)
if mibBuilder.loadTexts:
    dhcpActiveEntry.setStatus("mandatory")
_DhcpActiveIndex_Type = Integer32
_DhcpActiveIndex_Object = MibTableColumn
dhcpActiveIndex = _DhcpActiveIndex_Object(
    (1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 32, 1, 1),
    _DhcpActiveIndex_Type()
)
dhcpActiveIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpActiveIndex.setStatus("mandatory")


class _DhcpClientHostName_Type(OwnerString):
    """Custom type dhcpClientHostName based on OwnerString"""
    subtypeSpec = OwnerString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DhcpClientHostName_Type.__name__ = "OwnerString"
_DhcpClientHostName_Object = MibTableColumn
dhcpClientHostName = _DhcpClientHostName_Object(
    (1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 32, 1, 2),
    _DhcpClientHostName_Type()
)
dhcpClientHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpClientHostName.setStatus("mandatory")
_DhcpNetAddress_Type = IpAddress
_DhcpNetAddress_Object = MibTableColumn
dhcpNetAddress = _DhcpNetAddress_Object(
    (1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 32, 1, 3),
    _DhcpNetAddress_Type()
)
dhcpNetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpNetAddress.setStatus("mandatory")
_DhcpPhysicalAddress_Type = PhysAddress
_DhcpPhysicalAddress_Object = MibTableColumn
dhcpPhysicalAddress = _DhcpPhysicalAddress_Object(
    (1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 32, 1, 4),
    _DhcpPhysicalAddress_Type()
)
dhcpPhysicalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpPhysicalAddress.setStatus("mandatory")
_StaticRoutingTable_Object = MibTable
staticRoutingTable = _StaticRoutingTable_Object(
    (1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 33)
)
if mibBuilder.loadTexts:
    staticRoutingTable.setStatus("mandatory")
_StaticRoutingEntry_Object = MibTableRow
staticRoutingEntry = _StaticRoutingEntry_Object(
    (1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 33, 1)
)
staticRoutingEntry.setIndexNames(
    (0, "LINKSYS-MODEL-MIB", "staticRoutingIndex"),
)
if mibBuilder.loadTexts:
    staticRoutingEntry.setStatus("mandatory")
_StaticRoutingIndex_Type = Integer32
_StaticRoutingIndex_Object = MibTableColumn
staticRoutingIndex = _StaticRoutingIndex_Object(
    (1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 33, 1, 1),
    _StaticRoutingIndex_Type()
)
staticRoutingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staticRoutingIndex.setStatus("mandatory")
_DestinationNetAddress_Type = IpAddress
_DestinationNetAddress_Object = MibTableColumn
destinationNetAddress = _DestinationNetAddress_Object(
    (1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 33, 1, 2),
    _DestinationNetAddress_Type()
)
destinationNetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    destinationNetAddress.setStatus("mandatory")
_RoutingSubnetMask_Type = IpAddress
_RoutingSubnetMask_Object = MibTableColumn
routingSubnetMask = _RoutingSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 33, 1, 3),
    _RoutingSubnetMask_Type()
)
routingSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    routingSubnetMask.setStatus("mandatory")
_RoutingDefaultbroadbandGateway_Type = IpAddress
_RoutingDefaultbroadbandGateway_Object = MibTableColumn
routingDefaultbroadbandGateway = _RoutingDefaultbroadbandGateway_Object(
    (1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 33, 1, 4),
    _RoutingDefaultbroadbandGateway_Type()
)
routingDefaultbroadbandGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    routingDefaultbroadbandGateway.setStatus("mandatory")
_RoutingHopCount_Type = Integer32
_RoutingHopCount_Object = MibTableColumn
routingHopCount = _RoutingHopCount_Object(
    (1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 33, 1, 5),
    _RoutingHopCount_Type()
)
routingHopCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    routingHopCount.setStatus("mandatory")


class _RoutingInterface_Type(Integer32):
    """Custom type routingInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lan", 1),
          ("wan", 2))
    )


_RoutingInterface_Type.__name__ = "Integer32"
_RoutingInterface_Object = MibTableColumn
routingInterface = _RoutingInterface_Object(
    (1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 33, 1, 6),
    _RoutingInterface_Type()
)
routingInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    routingInterface.setStatus("mandatory")


class _NFlagStatus_Type(Integer32):
    """Custom type nFlagStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("free", 0),
          ("ready", 1))
    )


_NFlagStatus_Type.__name__ = "Integer32"
_NFlagStatus_Object = MibTableColumn
nFlagStatus = _NFlagStatus_Object(
    (1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 33, 1, 7),
    _NFlagStatus_Type()
)
nFlagStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nFlagStatus.setStatus("mandatory")
_FilterIPRangeTable_Object = MibTable
filterIPRangeTable = _FilterIPRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 34)
)
if mibBuilder.loadTexts:
    filterIPRangeTable.setStatus("mandatory")
_FilterIPRangeEntry_Object = MibTableRow
filterIPRangeEntry = _FilterIPRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 34, 1)
)
filterIPRangeEntry.setIndexNames(
    (0, "LINKSYS-MODEL-MIB", "filterIPRangeIndex"),
)
if mibBuilder.loadTexts:
    filterIPRangeEntry.setStatus("mandatory")
_FilterIPRangeIndex_Type = Integer32
_FilterIPRangeIndex_Object = MibTableColumn
filterIPRangeIndex = _FilterIPRangeIndex_Object(
    (1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 34, 1, 1),
    _FilterIPRangeIndex_Type()
)
filterIPRangeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filterIPRangeIndex.setStatus("mandatory")
_FilterIPStart_Type = IpAddress
_FilterIPStart_Object = MibTableColumn
filterIPStart = _FilterIPStart_Object(
    (1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 34, 1, 2),
    _FilterIPStart_Type()
)
filterIPStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterIPStart.setStatus("mandatory")
_FilterIPEnd_Type = IpAddress
_FilterIPEnd_Object = MibTableColumn
filterIPEnd = _FilterIPEnd_Object(
    (1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 34, 1, 3),
    _FilterIPEnd_Type()
)
filterIPEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterIPEnd.setStatus("mandatory")
_FilterPortRangeTable_Object = MibTable
filterPortRangeTable = _FilterPortRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 35)
)
if mibBuilder.loadTexts:
    filterPortRangeTable.setStatus("mandatory")
_FilterPortRangeEntry_Object = MibTableRow
filterPortRangeEntry = _FilterPortRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 35, 1)
)
filterPortRangeEntry.setIndexNames(
    (0, "LINKSYS-MODEL-MIB", "filterPortRangeIndex"),
)
if mibBuilder.loadTexts:
    filterPortRangeEntry.setStatus("mandatory")
_FilterPortRangeIndex_Type = Integer32
_FilterPortRangeIndex_Object = MibTableColumn
filterPortRangeIndex = _FilterPortRangeIndex_Object(
    (1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 35, 1, 1),
    _FilterPortRangeIndex_Type()
)
filterPortRangeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filterPortRangeIndex.setStatus("mandatory")


class _FilterPortProto_Type(Integer32):
    """Custom type filterPortProto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("both", 0),
          ("tcp", 2),
          ("udp", 1))
    )


_FilterPortProto_Type.__name__ = "Integer32"
_FilterPortProto_Object = MibTableColumn
filterPortProto = _FilterPortProto_Object(
    (1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 35, 1, 2),
    _FilterPortProto_Type()
)
filterPortProto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterPortProto.setStatus("mandatory")
_FilterPortStart_Type = Integer32
_FilterPortStart_Object = MibTableColumn
filterPortStart = _FilterPortStart_Object(
    (1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 35, 1, 3),
    _FilterPortStart_Type()
)
filterPortStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterPortStart.setStatus("mandatory")
_FilterPortEnd_Type = Integer32
_FilterPortEnd_Object = MibTableColumn
filterPortEnd = _FilterPortEnd_Object(
    (1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 35, 1, 4),
    _FilterPortEnd_Type()
)
filterPortEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterPortEnd.setStatus("mandatory")
_FilterMACTable_Object = MibTable
filterMACTable = _FilterMACTable_Object(
    (1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 36)
)
if mibBuilder.loadTexts:
    filterMACTable.setStatus("mandatory")
_FilterMACEntry_Object = MibTableRow
filterMACEntry = _FilterMACEntry_Object(
    (1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 36, 1)
)
filterMACEntry.setIndexNames(
    (0, "LINKSYS-MODEL-MIB", "filterMACIndex"),
)
if mibBuilder.loadTexts:
    filterMACEntry.setStatus("mandatory")
_FilterMACIndex_Type = Integer32
_FilterMACIndex_Object = MibTableColumn
filterMACIndex = _FilterMACIndex_Object(
    (1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 36, 1, 1),
    _FilterMACIndex_Type()
)
filterMACIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filterMACIndex.setStatus("mandatory")
_FilterMAC_Type = PhysAddress
_FilterMAC_Object = MibTableColumn
filterMAC = _FilterMAC_Object(
    (1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 36, 1, 2),
    _FilterMAC_Type()
)
filterMAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterMAC.setStatus("mandatory")
_ForwardTable_Object = MibTable
forwardTable = _ForwardTable_Object(
    (1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 37)
)
if mibBuilder.loadTexts:
    forwardTable.setStatus("mandatory")
_ForwardEntry_Object = MibTableRow
forwardEntry = _ForwardEntry_Object(
    (1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 37, 1)
)
forwardEntry.setIndexNames(
    (0, "LINKSYS-MODEL-MIB", "forwardIndex"),
)
if mibBuilder.loadTexts:
    forwardEntry.setStatus("mandatory")
_ForwardIndex_Type = Integer32
_ForwardIndex_Object = MibTableColumn
forwardIndex = _ForwardIndex_Object(
    (1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 37, 1, 1),
    _ForwardIndex_Type()
)
forwardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forwardIndex.setStatus("mandatory")
_ServicePortStart_Type = Integer32
_ServicePortStart_Object = MibTableColumn
servicePortStart = _ServicePortStart_Object(
    (1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 37, 1, 2),
    _ServicePortStart_Type()
)
servicePortStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    servicePortStart.setStatus("mandatory")
_ServicePortEnd_Type = Integer32
_ServicePortEnd_Object = MibTableColumn
servicePortEnd = _ServicePortEnd_Object(
    (1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 37, 1, 3),
    _ServicePortEnd_Type()
)
servicePortEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    servicePortEnd.setStatus("mandatory")


class _ServicePortProto_Type(Integer32):
    """Custom type servicePortProto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("both", 0),
          ("tcp", 2),
          ("udp", 1))
    )


_ServicePortProto_Type.__name__ = "Integer32"
_ServicePortProto_Object = MibTableColumn
servicePortProto = _ServicePortProto_Object(
    (1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 37, 1, 4),
    _ServicePortProto_Type()
)
servicePortProto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    servicePortProto.setStatus("mandatory")
_ForwardIPAddress_Type = IpAddress
_ForwardIPAddress_Object = MibTableColumn
forwardIPAddress = _ForwardIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 37, 1, 5),
    _ForwardIPAddress_Type()
)
forwardIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    forwardIPAddress.setStatus("mandatory")
_DnsNetAddressWANTable_Object = MibTable
dnsNetAddressWANTable = _DnsNetAddressWANTable_Object(
    (1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 38)
)
if mibBuilder.loadTexts:
    dnsNetAddressWANTable.setStatus("mandatory")
_DnsNetAddressWANEntry_Object = MibTableRow
dnsNetAddressWANEntry = _DnsNetAddressWANEntry_Object(
    (1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 38, 1)
)
dnsNetAddressWANEntry.setIndexNames(
    (0, "LINKSYS-MODEL-MIB", "dnsNetAddressWANIndex"),
)
if mibBuilder.loadTexts:
    dnsNetAddressWANEntry.setStatus("mandatory")
_DnsNetAddressWANIndex_Type = Integer32
_DnsNetAddressWANIndex_Object = MibTableColumn
dnsNetAddressWANIndex = _DnsNetAddressWANIndex_Object(
    (1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 38, 1, 1),
    _DnsNetAddressWANIndex_Type()
)
dnsNetAddressWANIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsNetAddressWANIndex.setStatus("mandatory")
_DnsNetAddressWAN_Type = IpAddress
_DnsNetAddressWAN_Object = MibTableColumn
dnsNetAddressWAN = _DnsNetAddressWAN_Object(
    (1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 38, 1, 2),
    _DnsNetAddressWAN_Type()
)
dnsNetAddressWAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnsNetAddressWAN.setStatus("mandatory")
_OutgoingLogTable_Object = MibTable
outgoingLogTable = _OutgoingLogTable_Object(
    (1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 39)
)
if mibBuilder.loadTexts:
    outgoingLogTable.setStatus("mandatory")
_OutgoingLogEntry_Object = MibTableRow
outgoingLogEntry = _OutgoingLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 39, 1)
)
outgoingLogEntry.setIndexNames(
    (0, "LINKSYS-MODEL-MIB", "outgoingLogIndex"),
)
if mibBuilder.loadTexts:
    outgoingLogEntry.setStatus("mandatory")
_OutgoingLogIndex_Type = Integer32
_OutgoingLogIndex_Object = MibTableColumn
outgoingLogIndex = _OutgoingLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 39, 1, 1),
    _OutgoingLogIndex_Type()
)
outgoingLogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outgoingLogIndex.setStatus("mandatory")
_SourceIPLAN_Type = IpAddress
_SourceIPLAN_Object = MibTableColumn
sourceIPLAN = _SourceIPLAN_Object(
    (1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 39, 1, 2),
    _SourceIPLAN_Type()
)
sourceIPLAN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sourceIPLAN.setStatus("mandatory")
_DestinationIP_Type = IpAddress
_DestinationIP_Object = MibTableColumn
destinationIP = _DestinationIP_Object(
    (1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 39, 1, 3),
    _DestinationIP_Type()
)
destinationIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    destinationIP.setStatus("mandatory")
_ServicePortNumber_Type = Integer32
_ServicePortNumber_Object = MibTableColumn
servicePortNumber = _ServicePortNumber_Object(
    (1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 39, 1, 4),
    _ServicePortNumber_Type()
)
servicePortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    servicePortNumber.setStatus("mandatory")
_IncomingLogTable_Object = MibTable
incomingLogTable = _IncomingLogTable_Object(
    (1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 40)
)
if mibBuilder.loadTexts:
    incomingLogTable.setStatus("mandatory")
_IncomingLogEntry_Object = MibTableRow
incomingLogEntry = _IncomingLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 40, 1)
)
incomingLogEntry.setIndexNames(
    (0, "LINKSYS-MODEL-MIB", "incomingLogIndex"),
)
if mibBuilder.loadTexts:
    incomingLogEntry.setStatus("mandatory")
_IncomingLogIndex_Type = Integer32
_IncomingLogIndex_Object = MibTableColumn
incomingLogIndex = _IncomingLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 40, 1, 1),
    _IncomingLogIndex_Type()
)
incomingLogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    incomingLogIndex.setStatus("mandatory")
_SourceIP_Type = IpAddress
_SourceIP_Object = MibTableColumn
sourceIP = _SourceIP_Object(
    (1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 40, 1, 2),
    _SourceIP_Type()
)
sourceIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sourceIP.setStatus("mandatory")
_DestinationPortNumber_Type = Integer32
_DestinationPortNumber_Object = MibTableColumn
destinationPortNumber = _DestinationPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 40, 1, 3),
    _DestinationPortNumber_Type()
)
destinationPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    destinationPortNumber.setStatus("mandatory")
_TrapManagerTable_Object = MibTable
trapManagerTable = _TrapManagerTable_Object(
    (1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 41)
)
if mibBuilder.loadTexts:
    trapManagerTable.setStatus("mandatory")
_TrapManagerEntry_Object = MibTableRow
trapManagerEntry = _TrapManagerEntry_Object(
    (1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 41, 1)
)
trapManagerEntry.setIndexNames(
    (0, "LINKSYS-MODEL-MIB", "trapManagerIndex"),
)
if mibBuilder.loadTexts:
    trapManagerEntry.setStatus("mandatory")
_TrapManagerIndex_Type = Integer32
_TrapManagerIndex_Object = MibTableColumn
trapManagerIndex = _TrapManagerIndex_Object(
    (1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 41, 1, 1),
    _TrapManagerIndex_Type()
)
trapManagerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapManagerIndex.setStatus("mandatory")
_TrapMgrNetAddress_Type = IpAddress
_TrapMgrNetAddress_Object = MibTableColumn
trapMgrNetAddress = _TrapMgrNetAddress_Object(
    (1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 41, 1, 2),
    _TrapMgrNetAddress_Type()
)
trapMgrNetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapMgrNetAddress.setStatus("mandatory")
_QosAppTable_Object = MibTable
qosAppTable = _QosAppTable_Object(
    (1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 42)
)
if mibBuilder.loadTexts:
    qosAppTable.setStatus("mandatory")
_QosAppEntry_Object = MibTableRow
qosAppEntry = _QosAppEntry_Object(
    (1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 42, 1)
)
qosAppEntry.setIndexNames(
    (0, "LINKSYS-MODEL-MIB", "qosAppIndex"),
)
if mibBuilder.loadTexts:
    qosAppEntry.setStatus("mandatory")
_QosAppIndex_Type = Integer32
_QosAppIndex_Object = MibTableColumn
qosAppIndex = _QosAppIndex_Object(
    (1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 42, 1, 1),
    _QosAppIndex_Type()
)
qosAppIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosAppIndex.setStatus("mandatory")
_AppPort_Type = Integer32
_AppPort_Object = MibTableColumn
appPort = _AppPort_Object(
    (1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 42, 1, 2),
    _AppPort_Type()
)
appPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appPort.setStatus("mandatory")


class _AppPriority_Type(Integer32):
    """Custom type appPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("high", 2),
          ("low", 1))
    )


_AppPriority_Type.__name__ = "Integer32"
_AppPriority_Object = MibTableColumn
appPriority = _AppPriority_Object(
    (1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 42, 1, 3),
    _AppPriority_Type()
)
appPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appPriority.setStatus("mandatory")
_QosPortTable_Object = MibTable
qosPortTable = _QosPortTable_Object(
    (1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 43)
)
if mibBuilder.loadTexts:
    qosPortTable.setStatus("mandatory")
_QosPortEntry_Object = MibTableRow
qosPortEntry = _QosPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 43, 1)
)
qosPortEntry.setIndexNames(
    (0, "LINKSYS-MODEL-MIB", "qosPortIndex"),
)
if mibBuilder.loadTexts:
    qosPortEntry.setStatus("mandatory")
_QosPortIndex_Type = Integer32
_QosPortIndex_Object = MibTableColumn
qosPortIndex = _QosPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 43, 1, 1),
    _QosPortIndex_Type()
)
qosPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosPortIndex.setStatus("mandatory")
_LanPort_Type = Integer32
_LanPort_Object = MibTableColumn
lanPort = _LanPort_Object(
    (1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 43, 1, 2),
    _LanPort_Type()
)
lanPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanPort.setStatus("mandatory")


class _PortPriority_Type(Integer32):
    """Custom type portPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("high", 2),
          ("low", 1))
    )


_PortPriority_Type.__name__ = "Integer32"
_PortPriority_Object = MibTableColumn
portPriority = _PortPriority_Object(
    (1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 43, 1, 3),
    _PortPriority_Type()
)
portPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portPriority.setStatus("mandatory")


class _MulticastPassStatus_Type(Integer32):
    """Custom type multicastPassStatus based on Integer32"""
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


_MulticastPassStatus_Type.__name__ = "Integer32"
_MulticastPassStatus_Object = MibScalar
multicastPassStatus = _MulticastPassStatus_Object(
    (1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 44),
    _MulticastPassStatus_Type()
)
multicastPassStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    multicastPassStatus.setStatus("mandatory")


class _MtuStatus_Type(Integer32):
    """Custom type mtuStatus based on Integer32"""
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


_MtuStatus_Type.__name__ = "Integer32"
_MtuStatus_Object = MibScalar
mtuStatus = _MtuStatus_Object(
    (1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 45),
    _MtuStatus_Type()
)
mtuStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mtuStatus.setStatus("mandatory")
_MtuSize_Type = Integer32
_MtuSize_Object = MibScalar
mtuSize = _MtuSize_Object(
    (1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 46),
    _MtuSize_Type()
)
mtuSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mtuSize.setStatus("mandatory")
_RedialPeriod_Type = Integer32
_RedialPeriod_Object = MibScalar
redialPeriod = _RedialPeriod_Object(
    (1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 47),
    _RedialPeriod_Type()
)
redialPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    redialPeriod.setStatus("mandatory")
_PortTriggering_Object = MibTable
portTriggering = _PortTriggering_Object(
    (1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 48)
)
if mibBuilder.loadTexts:
    portTriggering.setStatus("mandatory")
_PortTriggerEntry_Object = MibTableRow
portTriggerEntry = _PortTriggerEntry_Object(
    (1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 48, 1)
)
portTriggerEntry.setIndexNames(
    (0, "LINKSYS-MODEL-MIB", "portTriggerIndex"),
)
if mibBuilder.loadTexts:
    portTriggerEntry.setStatus("mandatory")
_PortTriggerIndex_Type = Integer32
_PortTriggerIndex_Object = MibTableColumn
portTriggerIndex = _PortTriggerIndex_Object(
    (1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 48, 1, 1),
    _PortTriggerIndex_Type()
)
portTriggerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portTriggerIndex.setStatus("mandatory")


class _AppName_Type(OwnerString):
    """Custom type appName based on OwnerString"""
    subtypeSpec = OwnerString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_AppName_Type.__name__ = "OwnerString"
_AppName_Object = MibTableColumn
appName = _AppName_Object(
    (1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 48, 1, 2),
    _AppName_Type()
)
appName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appName.setStatus("mandatory")
_TriggerPortStart_Type = Integer32
_TriggerPortStart_Object = MibTableColumn
triggerPortStart = _TriggerPortStart_Object(
    (1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 48, 1, 3),
    _TriggerPortStart_Type()
)
triggerPortStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    triggerPortStart.setStatus("mandatory")
_TriggerPortEnd_Type = Integer32
_TriggerPortEnd_Object = MibTableColumn
triggerPortEnd = _TriggerPortEnd_Object(
    (1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 48, 1, 4),
    _TriggerPortEnd_Type()
)
triggerPortEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    triggerPortEnd.setStatus("mandatory")
_IncomingPortStart_Type = Integer32
_IncomingPortStart_Object = MibTableColumn
incomingPortStart = _IncomingPortStart_Object(
    (1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 48, 1, 5),
    _IncomingPortStart_Type()
)
incomingPortStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    incomingPortStart.setStatus("mandatory")
_IncomingPortEnd_Type = Integer32
_IncomingPortEnd_Object = MibTableColumn
incomingPortEnd = _IncomingPortEnd_Object(
    (1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 48, 1, 6),
    _IncomingPortEnd_Type()
)
incomingPortEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    incomingPortEnd.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LINKSYS-MODEL-MIB",
    **{"internet": internet,
       "directory": directory,
       "mgmt": mgmt,
       "experimental": experimental,
       "private": private,
       "enterprises": enterprises,
       "linksys": linksys,
       "common": common,
       "commonModelId": commonModelId,
       "commonSoftwareVer": commonSoftwareVer,
       "commonFirmwareVer": commonFirmwareVer,
       "products": products,
       "snmpMgt": snmpMgt,
       "commonMgt": commonMgt,
       "mgtWarmStart": mgtWarmStart,
       "mgtFactoryReset": mgtFactoryReset,
       "mgtAdministrator": mgtAdministrator,
       "mgtBootStatus": mgtBootStatus,
       "mgtRefreshMIB": mgtRefreshMIB,
       "mgtUpdateNV": mgtUpdateNV,
       "mgtCommunityTable": mgtCommunityTable,
       "mgtCommunityEntry": mgtCommunityEntry,
       "mgtCommunityIndex": mgtCommunityIndex,
       "mgtCommunityName": mgtCommunityName,
       "mgtCommunityType": mgtCommunityType,
       "internetAccessMgt": internetAccessMgt,
       "broadbandGateway": broadbandGateway,
       "hostName": hostName,
       "domainName": domainName,
       "netAddressLAN": netAddressLAN,
       "physicalAddrLAN": physicalAddrLAN,
       "subnetMaskLAN": subnetMaskLAN,
       "dhcpStatusWAN": dhcpStatusWAN,
       "netAddressWAN": netAddressWAN,
       "physicalAddrWAN": physicalAddrWAN,
       "subnetMaskWAN": subnetMaskWAN,
       "defaultbroadbandGatewayWAN": defaultbroadbandGatewayWAN,
       "loginStatus": loginStatus,
       "loginUserName": loginUserName,
       "loginPassword": loginPassword,
       "rasPlan": rasPlan,
       "connectedState": connectedState,
       "connectedIdleTime": connectedIdleTime,
       "dhcpStatusLAN": dhcpStatusLAN,
       "dhcpStartNetAddr": dhcpStartNetAddr,
       "dhcpNumberUsers": dhcpNumberUsers,
       "workingMode": workingMode,
       "dynamicRoutingTX": dynamicRoutingTX,
       "dynamicRoutingRX": dynamicRoutingRX,
       "spiStatus": spiStatus,
       "wanReqBlockStatus": wanReqBlockStatus,
       "ipSecPassThroughStatus": ipSecPassThroughStatus,
       "pptpPassThroughStatus": pptpPassThroughStatus,
       "remoteMgtStatus": remoteMgtStatus,
       "remoteUpgradeStatus": remoteUpgradeStatus,
       "accessLogStatus": accessLogStatus,
       "dmzHostIPAddress": dmzHostIPAddress,
       "qosStatus": qosStatus,
       "dhcpActiveTable": dhcpActiveTable,
       "dhcpActiveEntry": dhcpActiveEntry,
       "dhcpActiveIndex": dhcpActiveIndex,
       "dhcpClientHostName": dhcpClientHostName,
       "dhcpNetAddress": dhcpNetAddress,
       "dhcpPhysicalAddress": dhcpPhysicalAddress,
       "staticRoutingTable": staticRoutingTable,
       "staticRoutingEntry": staticRoutingEntry,
       "staticRoutingIndex": staticRoutingIndex,
       "destinationNetAddress": destinationNetAddress,
       "routingSubnetMask": routingSubnetMask,
       "routingDefaultbroadbandGateway": routingDefaultbroadbandGateway,
       "routingHopCount": routingHopCount,
       "routingInterface": routingInterface,
       "nFlagStatus": nFlagStatus,
       "filterIPRangeTable": filterIPRangeTable,
       "filterIPRangeEntry": filterIPRangeEntry,
       "filterIPRangeIndex": filterIPRangeIndex,
       "filterIPStart": filterIPStart,
       "filterIPEnd": filterIPEnd,
       "filterPortRangeTable": filterPortRangeTable,
       "filterPortRangeEntry": filterPortRangeEntry,
       "filterPortRangeIndex": filterPortRangeIndex,
       "filterPortProto": filterPortProto,
       "filterPortStart": filterPortStart,
       "filterPortEnd": filterPortEnd,
       "filterMACTable": filterMACTable,
       "filterMACEntry": filterMACEntry,
       "filterMACIndex": filterMACIndex,
       "filterMAC": filterMAC,
       "forwardTable": forwardTable,
       "forwardEntry": forwardEntry,
       "forwardIndex": forwardIndex,
       "servicePortStart": servicePortStart,
       "servicePortEnd": servicePortEnd,
       "servicePortProto": servicePortProto,
       "forwardIPAddress": forwardIPAddress,
       "dnsNetAddressWANTable": dnsNetAddressWANTable,
       "dnsNetAddressWANEntry": dnsNetAddressWANEntry,
       "dnsNetAddressWANIndex": dnsNetAddressWANIndex,
       "dnsNetAddressWAN": dnsNetAddressWAN,
       "outgoingLogTable": outgoingLogTable,
       "outgoingLogEntry": outgoingLogEntry,
       "outgoingLogIndex": outgoingLogIndex,
       "sourceIPLAN": sourceIPLAN,
       "destinationIP": destinationIP,
       "servicePortNumber": servicePortNumber,
       "incomingLogTable": incomingLogTable,
       "incomingLogEntry": incomingLogEntry,
       "incomingLogIndex": incomingLogIndex,
       "sourceIP": sourceIP,
       "destinationPortNumber": destinationPortNumber,
       "trapManagerTable": trapManagerTable,
       "trapManagerEntry": trapManagerEntry,
       "trapManagerIndex": trapManagerIndex,
       "trapMgrNetAddress": trapMgrNetAddress,
       "qosAppTable": qosAppTable,
       "qosAppEntry": qosAppEntry,
       "qosAppIndex": qosAppIndex,
       "appPort": appPort,
       "appPriority": appPriority,
       "qosPortTable": qosPortTable,
       "qosPortEntry": qosPortEntry,
       "qosPortIndex": qosPortIndex,
       "lanPort": lanPort,
       "portPriority": portPriority,
       "multicastPassStatus": multicastPassStatus,
       "mtuStatus": mtuStatus,
       "mtuSize": mtuSize,
       "redialPeriod": redialPeriod,
       "portTriggering": portTriggering,
       "portTriggerEntry": portTriggerEntry,
       "portTriggerIndex": portTriggerIndex,
       "appName": appName,
       "triggerPortStart": triggerPortStart,
       "triggerPortEnd": triggerPortEnd,
       "incomingPortStart": incomingPortStart,
       "incomingPortEnd": incomingPortEnd}
)
