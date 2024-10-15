# SNMP MIB module (WLSX-USER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WLSX-USER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:14:16 2024
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

(wlsxEnterpriseMibModules,) = mibBuilder.importSymbols(
    "ARUBA-MIB",
    "wlsxEnterpriseMibModules")

(ArubaAuthenticationMethods,
 ArubaEncryptionType,
 ArubaHTMode,
 ArubaPhyType,
 ArubaSubAuthenticationMethods,
 ArubaUserForwardMode) = mibBuilder.importSymbols(
    "ARUBA-TC",
    "ArubaAuthenticationMethods",
    "ArubaEncryptionType",
    "ArubaHTMode",
    "ArubaPhyType",
    "ArubaSubAuthenticationMethods",
    "ArubaUserForwardMode")

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
 TextualConvention,
 TimeTicks,
 Unsigned32,
 iso,
 snmpModules) = mibBuilder.importSymbols(
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
    "TextualConvention",
    "TimeTicks",
    "Unsigned32",
    "iso",
    "snmpModules")

(DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 StorageType,
 TAddress,
 TDomain,
 TextualConvention,
 TestAndIncr,
 TimeInterval,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "StorageType",
    "TAddress",
    "TDomain",
    "TextualConvention",
    "TestAndIncr",
    "TimeInterval",
    "TruthValue")

(wlanESSID,) = mibBuilder.importSymbols(
    "WLSX-WLAN-MIB",
    "wlanESSID")


# MODULE-IDENTITY

wlsxUserMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 4)
)
wlsxUserMIB.setRevisions(
        ("1910-01-26 18:06",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WlsxUserAllInfoGroup_ObjectIdentity = ObjectIdentity
wlsxUserAllInfoGroup = _WlsxUserAllInfoGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 4, 1)
)
_WlsxTotalNumOfUsers_Type = Unsigned32
_WlsxTotalNumOfUsers_Object = MibScalar
wlsxTotalNumOfUsers = _WlsxTotalNumOfUsers_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 4, 1, 1),
    _WlsxTotalNumOfUsers_Type()
)
wlsxTotalNumOfUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxTotalNumOfUsers.setStatus("current")
_WlsxUserTable_Object = MibTable
wlsxUserTable = _WlsxUserTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 4, 1, 2)
)
if mibBuilder.loadTexts:
    wlsxUserTable.setStatus("current")
_WlsxUserEntry_Object = MibTableRow
wlsxUserEntry = _WlsxUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 4, 1, 2, 1)
)
wlsxUserEntry.setIndexNames(
    (0, "WLSX-USER-MIB", "nUserPhyAddress"),
    (0, "WLSX-USER-MIB", "nUserIpAddress"),
)
if mibBuilder.loadTexts:
    wlsxUserEntry.setStatus("current")
_NUserPhyAddress_Type = MacAddress
_NUserPhyAddress_Object = MibTableColumn
nUserPhyAddress = _NUserPhyAddress_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 4, 1, 2, 1, 1),
    _NUserPhyAddress_Type()
)
nUserPhyAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nUserPhyAddress.setStatus("current")
_NUserIpAddress_Type = IpAddress
_NUserIpAddress_Object = MibTableColumn
nUserIpAddress = _NUserIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 4, 1, 2, 1, 2),
    _NUserIpAddress_Type()
)
nUserIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nUserIpAddress.setStatus("current")


class _NUserName_Type(DisplayString):
    """Custom type nUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_NUserName_Type.__name__ = "DisplayString"
_NUserName_Object = MibTableColumn
nUserName = _NUserName_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 4, 1, 2, 1, 3),
    _NUserName_Type()
)
nUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nUserName.setStatus("current")


class _NUserRole_Type(DisplayString):
    """Custom type nUserRole based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_NUserRole_Type.__name__ = "DisplayString"
_NUserRole_Object = MibTableColumn
nUserRole = _NUserRole_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 4, 1, 2, 1, 4),
    _NUserRole_Type()
)
nUserRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nUserRole.setStatus("current")
_NUserUpTime_Type = TimeTicks
_NUserUpTime_Object = MibTableColumn
nUserUpTime = _NUserUpTime_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 4, 1, 2, 1, 5),
    _NUserUpTime_Type()
)
nUserUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nUserUpTime.setStatus("current")
_NUserAuthenticationMethod_Type = ArubaAuthenticationMethods
_NUserAuthenticationMethod_Object = MibTableColumn
nUserAuthenticationMethod = _NUserAuthenticationMethod_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 4, 1, 2, 1, 6),
    _NUserAuthenticationMethod_Type()
)
nUserAuthenticationMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nUserAuthenticationMethod.setStatus("current")
_NUserSubAuthenticationMethod_Type = ArubaSubAuthenticationMethods
_NUserSubAuthenticationMethod_Object = MibTableColumn
nUserSubAuthenticationMethod = _NUserSubAuthenticationMethod_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 4, 1, 2, 1, 7),
    _NUserSubAuthenticationMethod_Type()
)
nUserSubAuthenticationMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nUserSubAuthenticationMethod.setStatus("current")


class _NUserAuthServerName_Type(DisplayString):
    """Custom type nUserAuthServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NUserAuthServerName_Type.__name__ = "DisplayString"
_NUserAuthServerName_Object = MibTableColumn
nUserAuthServerName = _NUserAuthServerName_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 4, 1, 2, 1, 8),
    _NUserAuthServerName_Type()
)
nUserAuthServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nUserAuthServerName.setStatus("current")
_NUserExtVPNAddress_Type = IpAddress
_NUserExtVPNAddress_Object = MibTableColumn
nUserExtVPNAddress = _NUserExtVPNAddress_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 4, 1, 2, 1, 9),
    _NUserExtVPNAddress_Type()
)
nUserExtVPNAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nUserExtVPNAddress.setStatus("current")


class _NUserApLocation_Type(DisplayString):
    """Custom type nUserApLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NUserApLocation_Type.__name__ = "DisplayString"
_NUserApLocation_Object = MibTableColumn
nUserApLocation = _NUserApLocation_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 4, 1, 2, 1, 10),
    _NUserApLocation_Type()
)
nUserApLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nUserApLocation.setStatus("current")
_NUserApBSSID_Type = MacAddress
_NUserApBSSID_Object = MibTableColumn
nUserApBSSID = _NUserApBSSID_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 4, 1, 2, 1, 11),
    _NUserApBSSID_Type()
)
nUserApBSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nUserApBSSID.setStatus("current")
_NUserIsOnHomeAgent_Type = TruthValue
_NUserIsOnHomeAgent_Object = MibTableColumn
nUserIsOnHomeAgent = _NUserIsOnHomeAgent_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 4, 1, 2, 1, 12),
    _NUserIsOnHomeAgent_Type()
)
nUserIsOnHomeAgent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nUserIsOnHomeAgent.setStatus("deprecated")
_NUserHomeAgentIpAddress_Type = IpAddress
_NUserHomeAgentIpAddress_Object = MibTableColumn
nUserHomeAgentIpAddress = _NUserHomeAgentIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 4, 1, 2, 1, 13),
    _NUserHomeAgentIpAddress_Type()
)
nUserHomeAgentIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nUserHomeAgentIpAddress.setStatus("deprecated")


class _NUserMobilityStatus_Type(Integer32):
    """Custom type nUserMobilityStatus based on Integer32"""
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
        *(("associated", 3),
          ("away", 2),
          ("visitor", 1),
          ("wired", 4),
          ("wireless", 5))
    )


_NUserMobilityStatus_Type.__name__ = "Integer32"
_NUserMobilityStatus_Object = MibTableColumn
nUserMobilityStatus = _NUserMobilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 4, 1, 2, 1, 14),
    _NUserMobilityStatus_Type()
)
nUserMobilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nUserMobilityStatus.setStatus("current")
_NUserHomeVlan_Type = Integer32
_NUserHomeVlan_Object = MibTableColumn
nUserHomeVlan = _NUserHomeVlan_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 4, 1, 2, 1, 15),
    _NUserHomeVlan_Type()
)
nUserHomeVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nUserHomeVlan.setStatus("deprecated")
_NUserDefaultVlan_Type = Integer32
_NUserDefaultVlan_Object = MibTableColumn
nUserDefaultVlan = _NUserDefaultVlan_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 4, 1, 2, 1, 16),
    _NUserDefaultVlan_Type()
)
nUserDefaultVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nUserDefaultVlan.setStatus("current")
_NUserAssignedVlan_Type = Integer32
_NUserAssignedVlan_Object = MibTableColumn
nUserAssignedVlan = _NUserAssignedVlan_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 4, 1, 2, 1, 17),
    _NUserAssignedVlan_Type()
)
nUserAssignedVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nUserAssignedVlan.setStatus("current")


class _NUserBWContractName_Type(DisplayString):
    """Custom type nUserBWContractName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NUserBWContractName_Type.__name__ = "DisplayString"
_NUserBWContractName_Object = MibTableColumn
nUserBWContractName = _NUserBWContractName_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 4, 1, 2, 1, 18),
    _NUserBWContractName_Type()
)
nUserBWContractName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nUserBWContractName.setStatus("deprecated")


class _NUserBWContractUsage_Type(Integer32):
    """Custom type nUserBWContractUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("shared", 2),
          ("user", 1))
    )


_NUserBWContractUsage_Type.__name__ = "Integer32"
_NUserBWContractUsage_Object = MibTableColumn
nUserBWContractUsage = _NUserBWContractUsage_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 4, 1, 2, 1, 19),
    _NUserBWContractUsage_Type()
)
nUserBWContractUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nUserBWContractUsage.setStatus("deprecated")
_NUserBWContractId_Type = Integer32
_NUserBWContractId_Object = MibTableColumn
nUserBWContractId = _NUserBWContractId_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 4, 1, 2, 1, 20),
    _NUserBWContractId_Type()
)
nUserBWContractId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nUserBWContractId.setStatus("deprecated")
_NUserIsProxyArpEnabled_Type = TruthValue
_NUserIsProxyArpEnabled_Object = MibTableColumn
nUserIsProxyArpEnabled = _NUserIsProxyArpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 4, 1, 2, 1, 21),
    _NUserIsProxyArpEnabled_Type()
)
nUserIsProxyArpEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nUserIsProxyArpEnabled.setStatus("current")
_NUserCurrentVlan_Type = Integer32
_NUserCurrentVlan_Object = MibTableColumn
nUserCurrentVlan = _NUserCurrentVlan_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 4, 1, 2, 1, 22),
    _NUserCurrentVlan_Type()
)
nUserCurrentVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nUserCurrentVlan.setStatus("current")
_NUserIsWired_Type = TruthValue
_NUserIsWired_Object = MibTableColumn
nUserIsWired = _NUserIsWired_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 4, 1, 2, 1, 23),
    _NUserIsWired_Type()
)
nUserIsWired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nUserIsWired.setStatus("current")
_NUserConnectedSlot_Type = Integer32
_NUserConnectedSlot_Object = MibTableColumn
nUserConnectedSlot = _NUserConnectedSlot_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 4, 1, 2, 1, 24),
    _NUserConnectedSlot_Type()
)
nUserConnectedSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nUserConnectedSlot.setStatus("current")
_NUserConnectedPort_Type = Integer32
_NUserConnectedPort_Object = MibTableColumn
nUserConnectedPort = _NUserConnectedPort_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 4, 1, 2, 1, 25),
    _NUserConnectedPort_Type()
)
nUserConnectedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nUserConnectedPort.setStatus("current")
_NUserPhyType_Type = ArubaPhyType
_NUserPhyType_Object = MibTableColumn
nUserPhyType = _NUserPhyType_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 4, 1, 2, 1, 26),
    _NUserPhyType_Type()
)
nUserPhyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nUserPhyType.setStatus("current")


class _NUserMobilityDomainName_Type(DisplayString):
    """Custom type nUserMobilityDomainName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_NUserMobilityDomainName_Type.__name__ = "DisplayString"
_NUserMobilityDomainName_Object = MibTableColumn
nUserMobilityDomainName = _NUserMobilityDomainName_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 4, 1, 2, 1, 27),
    _NUserMobilityDomainName_Type()
)
nUserMobilityDomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nUserMobilityDomainName.setStatus("current")


class _NUserUPBWContractName_Type(DisplayString):
    """Custom type nUserUPBWContractName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NUserUPBWContractName_Type.__name__ = "DisplayString"
_NUserUPBWContractName_Object = MibTableColumn
nUserUPBWContractName = _NUserUPBWContractName_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 4, 1, 2, 1, 28),
    _NUserUPBWContractName_Type()
)
nUserUPBWContractName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nUserUPBWContractName.setStatus("current")


class _NUserUPBWContractUsage_Type(Integer32):
    """Custom type nUserUPBWContractUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("shared", 2),
          ("user", 1))
    )


_NUserUPBWContractUsage_Type.__name__ = "Integer32"
_NUserUPBWContractUsage_Object = MibTableColumn
nUserUPBWContractUsage = _NUserUPBWContractUsage_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 4, 1, 2, 1, 29),
    _NUserUPBWContractUsage_Type()
)
nUserUPBWContractUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nUserUPBWContractUsage.setStatus("current")
_NUserUPBWContractId_Type = Integer32
_NUserUPBWContractId_Object = MibTableColumn
nUserUPBWContractId = _NUserUPBWContractId_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 4, 1, 2, 1, 30),
    _NUserUPBWContractId_Type()
)
nUserUPBWContractId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nUserUPBWContractId.setStatus("current")


class _NUserDNBWContractName_Type(DisplayString):
    """Custom type nUserDNBWContractName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NUserDNBWContractName_Type.__name__ = "DisplayString"
_NUserDNBWContractName_Object = MibTableColumn
nUserDNBWContractName = _NUserDNBWContractName_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 4, 1, 2, 1, 31),
    _NUserDNBWContractName_Type()
)
nUserDNBWContractName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nUserDNBWContractName.setStatus("current")


class _NUserDNBWContractUsage_Type(Integer32):
    """Custom type nUserDNBWContractUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("shared", 2),
          ("user", 1))
    )


_NUserDNBWContractUsage_Type.__name__ = "Integer32"
_NUserDNBWContractUsage_Object = MibTableColumn
nUserDNBWContractUsage = _NUserDNBWContractUsage_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 4, 1, 2, 1, 32),
    _NUserDNBWContractUsage_Type()
)
nUserDNBWContractUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nUserDNBWContractUsage.setStatus("current")
_NUserDNBWContractId_Type = Integer32
_NUserDNBWContractId_Object = MibTableColumn
nUserDNBWContractId = _NUserDNBWContractId_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 4, 1, 2, 1, 33),
    _NUserDNBWContractId_Type()
)
nUserDNBWContractId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nUserDNBWContractId.setStatus("current")
_NUserHTMode_Type = ArubaHTMode
_NUserHTMode_Object = MibTableColumn
nUserHTMode = _NUserHTMode_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 4, 1, 2, 1, 34),
    _NUserHTMode_Type()
)
nUserHTMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nUserHTMode.setStatus("current")
_NUserEncryptionMethod_Type = ArubaEncryptionType
_NUserEncryptionMethod_Object = MibTableColumn
nUserEncryptionMethod = _NUserEncryptionMethod_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 4, 1, 2, 1, 35),
    _NUserEncryptionMethod_Type()
)
nUserEncryptionMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nUserEncryptionMethod.setStatus("current")
_NUserForwardMode_Type = ArubaUserForwardMode
_NUserForwardMode_Object = MibTableColumn
nUserForwardMode = _NUserForwardMode_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 4, 1, 2, 1, 36),
    _NUserForwardMode_Type()
)
nUserForwardMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nUserForwardMode.setStatus("current")


class _NUserDeviceID_Type(DisplayString):
    """Custom type nUserDeviceID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_NUserDeviceID_Type.__name__ = "DisplayString"
_NUserDeviceID_Object = MibTableColumn
nUserDeviceID = _NUserDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 4, 1, 2, 1, 37),
    _NUserDeviceID_Type()
)
nUserDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nUserDeviceID.setStatus("current")
_NUserConnectedModule_Type = Integer32
_NUserConnectedModule_Object = MibTableColumn
nUserConnectedModule = _NUserConnectedModule_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 4, 1, 2, 1, 38),
    _NUserConnectedModule_Type()
)
nUserConnectedModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nUserConnectedModule.setStatus("current")


class _NUserDeviceType_Type(DisplayString):
    """Custom type nUserDeviceType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_NUserDeviceType_Type.__name__ = "DisplayString"
_NUserDeviceType_Object = MibTableColumn
nUserDeviceType = _NUserDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 4, 1, 2, 1, 39),
    _NUserDeviceType_Type()
)
nUserDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nUserDeviceType.setStatus("current")
_NUserRxDataPkts64_Type = Counter64
_NUserRxDataPkts64_Object = MibTableColumn
nUserRxDataPkts64 = _NUserRxDataPkts64_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 4, 1, 2, 1, 40),
    _NUserRxDataPkts64_Type()
)
nUserRxDataPkts64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nUserRxDataPkts64.setStatus("current")
_NUserTxDataPkts64_Type = Counter64
_NUserTxDataPkts64_Object = MibTableColumn
nUserTxDataPkts64 = _NUserTxDataPkts64_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 4, 1, 2, 1, 41),
    _NUserTxDataPkts64_Type()
)
nUserTxDataPkts64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nUserTxDataPkts64.setStatus("current")
_NUserRxDataOctets64_Type = Counter64
_NUserRxDataOctets64_Object = MibTableColumn
nUserRxDataOctets64 = _NUserRxDataOctets64_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 4, 1, 2, 1, 42),
    _NUserRxDataOctets64_Type()
)
nUserRxDataOctets64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nUserRxDataOctets64.setStatus("current")
_NUserTxDataOctets64_Type = Counter64
_NUserTxDataOctets64_Object = MibTableColumn
nUserTxDataOctets64 = _NUserTxDataOctets64_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 4, 1, 2, 1, 43),
    _NUserTxDataOctets64_Type()
)
nUserTxDataOctets64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nUserTxDataOctets64.setStatus("current")
_WlsxUserSessionTimeTable_Object = MibTable
wlsxUserSessionTimeTable = _WlsxUserSessionTimeTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 4, 1, 3)
)
if mibBuilder.loadTexts:
    wlsxUserSessionTimeTable.setStatus("current")
_WlsxUserSessionTimeEntry_Object = MibTableRow
wlsxUserSessionTimeEntry = _WlsxUserSessionTimeEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 4, 1, 3, 1)
)
wlsxUserSessionTimeEntry.setIndexNames(
    (0, "WLSX-WLAN-MIB", "wlanESSID"),
    (0, "WLSX-USER-MIB", "wlsxUserSessionTimeLength"),
)
if mibBuilder.loadTexts:
    wlsxUserSessionTimeEntry.setStatus("current")
_WlsxUserSessionTimeLength_Type = Integer32
_WlsxUserSessionTimeLength_Object = MibTableColumn
wlsxUserSessionTimeLength = _WlsxUserSessionTimeLength_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 4, 1, 3, 1, 1),
    _WlsxUserSessionTimeLength_Type()
)
wlsxUserSessionTimeLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wlsxUserSessionTimeLength.setStatus("current")
_WlsxUserSessionTimeCount_Type = Counter32
_WlsxUserSessionTimeCount_Object = MibTableColumn
wlsxUserSessionTimeCount = _WlsxUserSessionTimeCount_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 4, 1, 3, 1, 2),
    _WlsxUserSessionTimeCount_Type()
)
wlsxUserSessionTimeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxUserSessionTimeCount.setStatus("current")
_WlsxUserStatsGroup_ObjectIdentity = ObjectIdentity
wlsxUserStatsGroup = _WlsxUserStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 4, 1, 4)
)
_WlsxNumOfUsers8021x_Type = Unsigned32
_WlsxNumOfUsers8021x_Object = MibScalar
wlsxNumOfUsers8021x = _WlsxNumOfUsers8021x_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 4, 1, 4, 1),
    _WlsxNumOfUsers8021x_Type()
)
wlsxNumOfUsers8021x.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxNumOfUsers8021x.setStatus("current")
_WlsxNumOfUsersVPN_Type = Unsigned32
_WlsxNumOfUsersVPN_Object = MibScalar
wlsxNumOfUsersVPN = _WlsxNumOfUsersVPN_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 4, 1, 4, 2),
    _WlsxNumOfUsersVPN_Type()
)
wlsxNumOfUsersVPN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxNumOfUsersVPN.setStatus("current")
_WlsxNumOfUsersCP_Type = Unsigned32
_WlsxNumOfUsersCP_Object = MibScalar
wlsxNumOfUsersCP = _WlsxNumOfUsersCP_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 4, 1, 4, 3),
    _WlsxNumOfUsersCP_Type()
)
wlsxNumOfUsersCP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxNumOfUsersCP.setStatus("current")
_WlsxNumOfUsersMAC_Type = Unsigned32
_WlsxNumOfUsersMAC_Object = MibScalar
wlsxNumOfUsersMAC = _WlsxNumOfUsersMAC_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 4, 1, 4, 4),
    _WlsxNumOfUsersMAC_Type()
)
wlsxNumOfUsersMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxNumOfUsersMAC.setStatus("current")
_WlsxNumOfUsersStateful8021x_Type = Unsigned32
_WlsxNumOfUsersStateful8021x_Object = MibScalar
wlsxNumOfUsersStateful8021x = _WlsxNumOfUsersStateful8021x_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 4, 1, 4, 5),
    _WlsxNumOfUsersStateful8021x_Type()
)
wlsxNumOfUsersStateful8021x.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxNumOfUsersStateful8021x.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WLSX-USER-MIB",
    **{"wlsxUserMIB": wlsxUserMIB,
       "wlsxUserAllInfoGroup": wlsxUserAllInfoGroup,
       "wlsxTotalNumOfUsers": wlsxTotalNumOfUsers,
       "wlsxUserTable": wlsxUserTable,
       "wlsxUserEntry": wlsxUserEntry,
       "nUserPhyAddress": nUserPhyAddress,
       "nUserIpAddress": nUserIpAddress,
       "nUserName": nUserName,
       "nUserRole": nUserRole,
       "nUserUpTime": nUserUpTime,
       "nUserAuthenticationMethod": nUserAuthenticationMethod,
       "nUserSubAuthenticationMethod": nUserSubAuthenticationMethod,
       "nUserAuthServerName": nUserAuthServerName,
       "nUserExtVPNAddress": nUserExtVPNAddress,
       "nUserApLocation": nUserApLocation,
       "nUserApBSSID": nUserApBSSID,
       "nUserIsOnHomeAgent": nUserIsOnHomeAgent,
       "nUserHomeAgentIpAddress": nUserHomeAgentIpAddress,
       "nUserMobilityStatus": nUserMobilityStatus,
       "nUserHomeVlan": nUserHomeVlan,
       "nUserDefaultVlan": nUserDefaultVlan,
       "nUserAssignedVlan": nUserAssignedVlan,
       "nUserBWContractName": nUserBWContractName,
       "nUserBWContractUsage": nUserBWContractUsage,
       "nUserBWContractId": nUserBWContractId,
       "nUserIsProxyArpEnabled": nUserIsProxyArpEnabled,
       "nUserCurrentVlan": nUserCurrentVlan,
       "nUserIsWired": nUserIsWired,
       "nUserConnectedSlot": nUserConnectedSlot,
       "nUserConnectedPort": nUserConnectedPort,
       "nUserPhyType": nUserPhyType,
       "nUserMobilityDomainName": nUserMobilityDomainName,
       "nUserUPBWContractName": nUserUPBWContractName,
       "nUserUPBWContractUsage": nUserUPBWContractUsage,
       "nUserUPBWContractId": nUserUPBWContractId,
       "nUserDNBWContractName": nUserDNBWContractName,
       "nUserDNBWContractUsage": nUserDNBWContractUsage,
       "nUserDNBWContractId": nUserDNBWContractId,
       "nUserHTMode": nUserHTMode,
       "nUserEncryptionMethod": nUserEncryptionMethod,
       "nUserForwardMode": nUserForwardMode,
       "nUserDeviceID": nUserDeviceID,
       "nUserConnectedModule": nUserConnectedModule,
       "nUserDeviceType": nUserDeviceType,
       "nUserRxDataPkts64": nUserRxDataPkts64,
       "nUserTxDataPkts64": nUserTxDataPkts64,
       "nUserRxDataOctets64": nUserRxDataOctets64,
       "nUserTxDataOctets64": nUserTxDataOctets64,
       "wlsxUserSessionTimeTable": wlsxUserSessionTimeTable,
       "wlsxUserSessionTimeEntry": wlsxUserSessionTimeEntry,
       "wlsxUserSessionTimeLength": wlsxUserSessionTimeLength,
       "wlsxUserSessionTimeCount": wlsxUserSessionTimeCount,
       "wlsxUserStatsGroup": wlsxUserStatsGroup,
       "wlsxNumOfUsers8021x": wlsxNumOfUsers8021x,
       "wlsxNumOfUsersVPN": wlsxNumOfUsersVPN,
       "wlsxNumOfUsersCP": wlsxNumOfUsersCP,
       "wlsxNumOfUsersMAC": wlsxNumOfUsersMAC,
       "wlsxNumOfUsersStateful8021x": wlsxNumOfUsersStateful8021x}
)
