# SNMP MIB module (WLSX-USER6-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WLSX-USER6-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:14:17 2024
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

(wlsxSwitchMIB,) = mibBuilder.importSymbols(
    "WLSX-SWITCH-MIB",
    "wlsxSwitchMIB")

(wlanESSID,) = mibBuilder.importSymbols(
    "WLSX-WLAN-MIB",
    "wlanESSID")


# MODULE-IDENTITY

wlsxUser6MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 14)
)
wlsxUser6MIB.setRevisions(
        ("1910-01-26 18:06",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WlsxUser6InfoGroup_ObjectIdentity = ObjectIdentity
wlsxUser6InfoGroup = _WlsxUser6InfoGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 4)
)
_WlsxSwitchUser6Table_Object = MibTable
wlsxSwitchUser6Table = _WlsxSwitchUser6Table_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    wlsxSwitchUser6Table.setStatus("current")
_WlsxSwitchUser6Entry_Object = MibTableRow
wlsxSwitchUser6Entry = _WlsxSwitchUser6Entry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 4, 1, 1)
)
wlsxSwitchUser6Entry.setIndexNames(
    (0, "WLSX-USER6-MIB", "user6IpAddress"),
)
if mibBuilder.loadTexts:
    wlsxSwitchUser6Entry.setStatus("current")


class _User6IpAddress_Type(DisplayString):
    """Custom type user6IpAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_User6IpAddress_Type.__name__ = "DisplayString"
_User6IpAddress_Object = MibTableColumn
user6IpAddress = _User6IpAddress_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 4, 1, 1, 1),
    _User6IpAddress_Type()
)
user6IpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    user6IpAddress.setStatus("current")
_User6PhyAddress_Type = MacAddress
_User6PhyAddress_Object = MibTableColumn
user6PhyAddress = _User6PhyAddress_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 4, 1, 1, 2),
    _User6PhyAddress_Type()
)
user6PhyAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    user6PhyAddress.setStatus("current")


class _User6Name_Type(DisplayString):
    """Custom type user6Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_User6Name_Type.__name__ = "DisplayString"
_User6Name_Object = MibTableColumn
user6Name = _User6Name_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 4, 1, 1, 3),
    _User6Name_Type()
)
user6Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    user6Name.setStatus("current")


class _User6Role_Type(DisplayString):
    """Custom type user6Role based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_User6Role_Type.__name__ = "DisplayString"
_User6Role_Object = MibTableColumn
user6Role = _User6Role_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 4, 1, 1, 4),
    _User6Role_Type()
)
user6Role.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    user6Role.setStatus("current")
_User6UpTime_Type = TimeTicks
_User6UpTime_Object = MibTableColumn
user6UpTime = _User6UpTime_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 4, 1, 1, 5),
    _User6UpTime_Type()
)
user6UpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    user6UpTime.setStatus("current")


class _User6AuthenticationMethod_Type(Integer32):
    """Custom type user6AuthenticationMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("dot1x", 4),
          ("mac", 6),
          ("none", 1),
          ("other", 2),
          ("vpn", 5),
          ("web", 3))
    )


_User6AuthenticationMethod_Type.__name__ = "Integer32"
_User6AuthenticationMethod_Object = MibTableColumn
user6AuthenticationMethod = _User6AuthenticationMethod_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 4, 1, 1, 6),
    _User6AuthenticationMethod_Type()
)
user6AuthenticationMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    user6AuthenticationMethod.setStatus("current")


class _User6Location_Type(DisplayString):
    """Custom type user6Location based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_User6Location_Type.__name__ = "DisplayString"
_User6Location_Object = MibTableColumn
user6Location = _User6Location_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 4, 1, 1, 7),
    _User6Location_Type()
)
user6Location.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    user6Location.setStatus("current")


class _User6ServerName_Type(DisplayString):
    """Custom type user6ServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_User6ServerName_Type.__name__ = "DisplayString"
_User6ServerName_Object = MibTableColumn
user6ServerName = _User6ServerName_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 4, 1, 1, 8),
    _User6ServerName_Type()
)
user6ServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    user6ServerName.setStatus("current")
_User6ConnectedVlan_Type = Integer32
_User6ConnectedVlan_Object = MibTableColumn
user6ConnectedVlan = _User6ConnectedVlan_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 4, 1, 1, 9),
    _User6ConnectedVlan_Type()
)
user6ConnectedVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    user6ConnectedVlan.setStatus("current")
_User6ConnectedSlot_Type = Integer32
_User6ConnectedSlot_Object = MibTableColumn
user6ConnectedSlot = _User6ConnectedSlot_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 4, 1, 1, 10),
    _User6ConnectedSlot_Type()
)
user6ConnectedSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    user6ConnectedSlot.setStatus("current")
_User6ConnectedPort_Type = Integer32
_User6ConnectedPort_Object = MibTableColumn
user6ConnectedPort = _User6ConnectedPort_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 4, 1, 1, 11),
    _User6ConnectedPort_Type()
)
user6ConnectedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    user6ConnectedPort.setStatus("current")


class _User6BWContractName_Type(DisplayString):
    """Custom type user6BWContractName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_User6BWContractName_Type.__name__ = "DisplayString"
_User6BWContractName_Object = MibTableColumn
user6BWContractName = _User6BWContractName_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 4, 1, 1, 12),
    _User6BWContractName_Type()
)
user6BWContractName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    user6BWContractName.setStatus("current")


class _User6BWContractUsage_Type(Integer32):
    """Custom type user6BWContractUsage based on Integer32"""
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


_User6BWContractUsage_Type.__name__ = "Integer32"
_User6BWContractUsage_Object = MibTableColumn
user6BWContractUsage = _User6BWContractUsage_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 4, 1, 1, 13),
    _User6BWContractUsage_Type()
)
user6BWContractUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    user6BWContractUsage.setStatus("current")
_User6ConnectedModule_Type = Integer32
_User6ConnectedModule_Object = MibTableColumn
user6ConnectedModule = _User6ConnectedModule_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 4, 1, 1, 14),
    _User6ConnectedModule_Type()
)
user6ConnectedModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    user6ConnectedModule.setStatus("current")
_WlsxUser6AllInfoGroup_ObjectIdentity = ObjectIdentity
wlsxUser6AllInfoGroup = _WlsxUser6AllInfoGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 14, 1)
)
_WlsxTotalNumOfUsers6_Type = Unsigned32
_WlsxTotalNumOfUsers6_Object = MibScalar
wlsxTotalNumOfUsers6 = _WlsxTotalNumOfUsers6_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 14, 1, 1),
    _WlsxTotalNumOfUsers6_Type()
)
wlsxTotalNumOfUsers6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxTotalNumOfUsers6.setStatus("current")
_WlsxUser6Table_Object = MibTable
wlsxUser6Table = _WlsxUser6Table_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 14, 1, 2)
)
if mibBuilder.loadTexts:
    wlsxUser6Table.setStatus("current")
_WlsxUser6Entry_Object = MibTableRow
wlsxUser6Entry = _WlsxUser6Entry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 14, 1, 2, 1)
)
wlsxUser6Entry.setIndexNames(
    (0, "WLSX-USER6-MIB", "nUser6PhyAddress"),
    (0, "WLSX-USER6-MIB", "nUser6IpAddress"),
)
if mibBuilder.loadTexts:
    wlsxUser6Entry.setStatus("current")
_NUser6PhyAddress_Type = MacAddress
_NUser6PhyAddress_Object = MibTableColumn
nUser6PhyAddress = _NUser6PhyAddress_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 14, 1, 2, 1, 1),
    _NUser6PhyAddress_Type()
)
nUser6PhyAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nUser6PhyAddress.setStatus("current")


class _NUser6IpAddress_Type(DisplayString):
    """Custom type nUser6IpAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_NUser6IpAddress_Type.__name__ = "DisplayString"
_NUser6IpAddress_Object = MibTableColumn
nUser6IpAddress = _NUser6IpAddress_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 14, 1, 2, 1, 2),
    _NUser6IpAddress_Type()
)
nUser6IpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nUser6IpAddress.setStatus("current")


class _NUser6Name_Type(DisplayString):
    """Custom type nUser6Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_NUser6Name_Type.__name__ = "DisplayString"
_NUser6Name_Object = MibTableColumn
nUser6Name = _NUser6Name_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 14, 1, 2, 1, 3),
    _NUser6Name_Type()
)
nUser6Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nUser6Name.setStatus("current")


class _NUser6Role_Type(DisplayString):
    """Custom type nUser6Role based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_NUser6Role_Type.__name__ = "DisplayString"
_NUser6Role_Object = MibTableColumn
nUser6Role = _NUser6Role_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 14, 1, 2, 1, 4),
    _NUser6Role_Type()
)
nUser6Role.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nUser6Role.setStatus("current")
_NUser6UpTime_Type = TimeTicks
_NUser6UpTime_Object = MibTableColumn
nUser6UpTime = _NUser6UpTime_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 14, 1, 2, 1, 5),
    _NUser6UpTime_Type()
)
nUser6UpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nUser6UpTime.setStatus("current")
_NUser6AuthenticationMethod_Type = ArubaAuthenticationMethods
_NUser6AuthenticationMethod_Object = MibTableColumn
nUser6AuthenticationMethod = _NUser6AuthenticationMethod_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 14, 1, 2, 1, 6),
    _NUser6AuthenticationMethod_Type()
)
nUser6AuthenticationMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nUser6AuthenticationMethod.setStatus("current")
_NUser6SubAuthenticationMethod_Type = ArubaSubAuthenticationMethods
_NUser6SubAuthenticationMethod_Object = MibTableColumn
nUser6SubAuthenticationMethod = _NUser6SubAuthenticationMethod_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 14, 1, 2, 1, 7),
    _NUser6SubAuthenticationMethod_Type()
)
nUser6SubAuthenticationMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nUser6SubAuthenticationMethod.setStatus("current")


class _NUser6AuthServerName_Type(DisplayString):
    """Custom type nUser6AuthServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NUser6AuthServerName_Type.__name__ = "DisplayString"
_NUser6AuthServerName_Object = MibTableColumn
nUser6AuthServerName = _NUser6AuthServerName_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 14, 1, 2, 1, 8),
    _NUser6AuthServerName_Type()
)
nUser6AuthServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nUser6AuthServerName.setStatus("current")
_NUser6ExtVPNAddress_Type = IpAddress
_NUser6ExtVPNAddress_Object = MibTableColumn
nUser6ExtVPNAddress = _NUser6ExtVPNAddress_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 14, 1, 2, 1, 9),
    _NUser6ExtVPNAddress_Type()
)
nUser6ExtVPNAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nUser6ExtVPNAddress.setStatus("current")


class _NUser6ApLocation_Type(DisplayString):
    """Custom type nUser6ApLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NUser6ApLocation_Type.__name__ = "DisplayString"
_NUser6ApLocation_Object = MibTableColumn
nUser6ApLocation = _NUser6ApLocation_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 14, 1, 2, 1, 10),
    _NUser6ApLocation_Type()
)
nUser6ApLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nUser6ApLocation.setStatus("current")
_NUser6ApBSSID_Type = MacAddress
_NUser6ApBSSID_Object = MibTableColumn
nUser6ApBSSID = _NUser6ApBSSID_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 14, 1, 2, 1, 11),
    _NUser6ApBSSID_Type()
)
nUser6ApBSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nUser6ApBSSID.setStatus("current")
_NUser6IsOnHomeAgent_Type = TruthValue
_NUser6IsOnHomeAgent_Object = MibTableColumn
nUser6IsOnHomeAgent = _NUser6IsOnHomeAgent_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 14, 1, 2, 1, 12),
    _NUser6IsOnHomeAgent_Type()
)
nUser6IsOnHomeAgent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nUser6IsOnHomeAgent.setStatus("current")
_NUser6HomeAgentIpAddress_Type = IpAddress
_NUser6HomeAgentIpAddress_Object = MibTableColumn
nUser6HomeAgentIpAddress = _NUser6HomeAgentIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 14, 1, 2, 1, 13),
    _NUser6HomeAgentIpAddress_Type()
)
nUser6HomeAgentIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nUser6HomeAgentIpAddress.setStatus("current")


class _NUser6MobilityStatus_Type(Integer32):
    """Custom type nUser6MobilityStatus based on Integer32"""
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


_NUser6MobilityStatus_Type.__name__ = "Integer32"
_NUser6MobilityStatus_Object = MibTableColumn
nUser6MobilityStatus = _NUser6MobilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 14, 1, 2, 1, 14),
    _NUser6MobilityStatus_Type()
)
nUser6MobilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nUser6MobilityStatus.setStatus("current")
_NUser6HomeVlan_Type = Integer32
_NUser6HomeVlan_Object = MibTableColumn
nUser6HomeVlan = _NUser6HomeVlan_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 14, 1, 2, 1, 15),
    _NUser6HomeVlan_Type()
)
nUser6HomeVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nUser6HomeVlan.setStatus("current")
_NUser6DefaultVlan_Type = Integer32
_NUser6DefaultVlan_Object = MibTableColumn
nUser6DefaultVlan = _NUser6DefaultVlan_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 14, 1, 2, 1, 16),
    _NUser6DefaultVlan_Type()
)
nUser6DefaultVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nUser6DefaultVlan.setStatus("current")
_NUser6AssignedVlan_Type = Integer32
_NUser6AssignedVlan_Object = MibTableColumn
nUser6AssignedVlan = _NUser6AssignedVlan_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 14, 1, 2, 1, 17),
    _NUser6AssignedVlan_Type()
)
nUser6AssignedVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nUser6AssignedVlan.setStatus("current")


class _NUser6BWContractName_Type(DisplayString):
    """Custom type nUser6BWContractName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NUser6BWContractName_Type.__name__ = "DisplayString"
_NUser6BWContractName_Object = MibTableColumn
nUser6BWContractName = _NUser6BWContractName_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 14, 1, 2, 1, 18),
    _NUser6BWContractName_Type()
)
nUser6BWContractName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nUser6BWContractName.setStatus("deprecated")


class _NUser6BWContractUsage_Type(Integer32):
    """Custom type nUser6BWContractUsage based on Integer32"""
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


_NUser6BWContractUsage_Type.__name__ = "Integer32"
_NUser6BWContractUsage_Object = MibTableColumn
nUser6BWContractUsage = _NUser6BWContractUsage_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 14, 1, 2, 1, 19),
    _NUser6BWContractUsage_Type()
)
nUser6BWContractUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nUser6BWContractUsage.setStatus("deprecated")
_NUser6BWContractId_Type = Integer32
_NUser6BWContractId_Object = MibTableColumn
nUser6BWContractId = _NUser6BWContractId_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 14, 1, 2, 1, 20),
    _NUser6BWContractId_Type()
)
nUser6BWContractId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nUser6BWContractId.setStatus("deprecated")
_NUser6IsProxyArpEnabled_Type = TruthValue
_NUser6IsProxyArpEnabled_Object = MibTableColumn
nUser6IsProxyArpEnabled = _NUser6IsProxyArpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 14, 1, 2, 1, 21),
    _NUser6IsProxyArpEnabled_Type()
)
nUser6IsProxyArpEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nUser6IsProxyArpEnabled.setStatus("current")
_NUser6CurrentVlan_Type = Integer32
_NUser6CurrentVlan_Object = MibTableColumn
nUser6CurrentVlan = _NUser6CurrentVlan_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 14, 1, 2, 1, 22),
    _NUser6CurrentVlan_Type()
)
nUser6CurrentVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nUser6CurrentVlan.setStatus("current")
_NUser6IsWired_Type = TruthValue
_NUser6IsWired_Object = MibTableColumn
nUser6IsWired = _NUser6IsWired_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 14, 1, 2, 1, 23),
    _NUser6IsWired_Type()
)
nUser6IsWired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nUser6IsWired.setStatus("current")
_NUser6ConnectedSlot_Type = Integer32
_NUser6ConnectedSlot_Object = MibTableColumn
nUser6ConnectedSlot = _NUser6ConnectedSlot_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 14, 1, 2, 1, 24),
    _NUser6ConnectedSlot_Type()
)
nUser6ConnectedSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nUser6ConnectedSlot.setStatus("current")
_NUser6ConnectedPort_Type = Integer32
_NUser6ConnectedPort_Object = MibTableColumn
nUser6ConnectedPort = _NUser6ConnectedPort_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 14, 1, 2, 1, 25),
    _NUser6ConnectedPort_Type()
)
nUser6ConnectedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nUser6ConnectedPort.setStatus("current")
_NUser6PhyType_Type = ArubaPhyType
_NUser6PhyType_Object = MibTableColumn
nUser6PhyType = _NUser6PhyType_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 14, 1, 2, 1, 26),
    _NUser6PhyType_Type()
)
nUser6PhyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nUser6PhyType.setStatus("current")


class _NUser6MobilityDomainName_Type(DisplayString):
    """Custom type nUser6MobilityDomainName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_NUser6MobilityDomainName_Type.__name__ = "DisplayString"
_NUser6MobilityDomainName_Object = MibTableColumn
nUser6MobilityDomainName = _NUser6MobilityDomainName_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 14, 1, 2, 1, 27),
    _NUser6MobilityDomainName_Type()
)
nUser6MobilityDomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nUser6MobilityDomainName.setStatus("current")


class _NUser6UPBWContractName_Type(DisplayString):
    """Custom type nUser6UPBWContractName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NUser6UPBWContractName_Type.__name__ = "DisplayString"
_NUser6UPBWContractName_Object = MibTableColumn
nUser6UPBWContractName = _NUser6UPBWContractName_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 14, 1, 2, 1, 28),
    _NUser6UPBWContractName_Type()
)
nUser6UPBWContractName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nUser6UPBWContractName.setStatus("current")


class _NUser6UPBWContractUsage_Type(Integer32):
    """Custom type nUser6UPBWContractUsage based on Integer32"""
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


_NUser6UPBWContractUsage_Type.__name__ = "Integer32"
_NUser6UPBWContractUsage_Object = MibTableColumn
nUser6UPBWContractUsage = _NUser6UPBWContractUsage_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 14, 1, 2, 1, 29),
    _NUser6UPBWContractUsage_Type()
)
nUser6UPBWContractUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nUser6UPBWContractUsage.setStatus("current")
_NUser6UPBWContractId_Type = Integer32
_NUser6UPBWContractId_Object = MibTableColumn
nUser6UPBWContractId = _NUser6UPBWContractId_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 14, 1, 2, 1, 30),
    _NUser6UPBWContractId_Type()
)
nUser6UPBWContractId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nUser6UPBWContractId.setStatus("current")


class _NUser6DNBWContractName_Type(DisplayString):
    """Custom type nUser6DNBWContractName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NUser6DNBWContractName_Type.__name__ = "DisplayString"
_NUser6DNBWContractName_Object = MibTableColumn
nUser6DNBWContractName = _NUser6DNBWContractName_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 14, 1, 2, 1, 31),
    _NUser6DNBWContractName_Type()
)
nUser6DNBWContractName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nUser6DNBWContractName.setStatus("current")


class _NUser6DNBWContractUsage_Type(Integer32):
    """Custom type nUser6DNBWContractUsage based on Integer32"""
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


_NUser6DNBWContractUsage_Type.__name__ = "Integer32"
_NUser6DNBWContractUsage_Object = MibTableColumn
nUser6DNBWContractUsage = _NUser6DNBWContractUsage_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 14, 1, 2, 1, 32),
    _NUser6DNBWContractUsage_Type()
)
nUser6DNBWContractUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nUser6DNBWContractUsage.setStatus("current")
_NUser6DNBWContractId_Type = Integer32
_NUser6DNBWContractId_Object = MibTableColumn
nUser6DNBWContractId = _NUser6DNBWContractId_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 14, 1, 2, 1, 33),
    _NUser6DNBWContractId_Type()
)
nUser6DNBWContractId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nUser6DNBWContractId.setStatus("current")
_NUser6HTMode_Type = ArubaHTMode
_NUser6HTMode_Object = MibTableColumn
nUser6HTMode = _NUser6HTMode_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 14, 1, 2, 1, 34),
    _NUser6HTMode_Type()
)
nUser6HTMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nUser6HTMode.setStatus("current")


class _NUser6DeviceID_Type(DisplayString):
    """Custom type nUser6DeviceID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_NUser6DeviceID_Type.__name__ = "DisplayString"
_NUser6DeviceID_Object = MibTableColumn
nUser6DeviceID = _NUser6DeviceID_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 14, 1, 2, 1, 35),
    _NUser6DeviceID_Type()
)
nUser6DeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nUser6DeviceID.setStatus("current")


class _NUser6DeviceType_Type(DisplayString):
    """Custom type nUser6DeviceType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_NUser6DeviceType_Type.__name__ = "DisplayString"
_NUser6DeviceType_Object = MibTableColumn
nUser6DeviceType = _NUser6DeviceType_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 14, 1, 2, 1, 36),
    _NUser6DeviceType_Type()
)
nUser6DeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nUser6DeviceType.setStatus("current")
_NUser6ConnectedModule_Type = Integer32
_NUser6ConnectedModule_Object = MibTableColumn
nUser6ConnectedModule = _NUser6ConnectedModule_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 14, 1, 2, 1, 37),
    _NUser6ConnectedModule_Type()
)
nUser6ConnectedModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nUser6ConnectedModule.setStatus("current")
_NUser6RxDataPkts64_Type = Counter64
_NUser6RxDataPkts64_Object = MibTableColumn
nUser6RxDataPkts64 = _NUser6RxDataPkts64_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 14, 1, 2, 1, 38),
    _NUser6RxDataPkts64_Type()
)
nUser6RxDataPkts64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nUser6RxDataPkts64.setStatus("current")
_NUser6TxDataPkts64_Type = Counter64
_NUser6TxDataPkts64_Object = MibTableColumn
nUser6TxDataPkts64 = _NUser6TxDataPkts64_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 14, 1, 2, 1, 39),
    _NUser6TxDataPkts64_Type()
)
nUser6TxDataPkts64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nUser6TxDataPkts64.setStatus("current")
_NUser6RxDataOctets64_Type = Counter64
_NUser6RxDataOctets64_Object = MibTableColumn
nUser6RxDataOctets64 = _NUser6RxDataOctets64_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 14, 1, 2, 1, 40),
    _NUser6RxDataOctets64_Type()
)
nUser6RxDataOctets64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nUser6RxDataOctets64.setStatus("current")
_NUser6TxDataOctets64_Type = Counter64
_NUser6TxDataOctets64_Object = MibTableColumn
nUser6TxDataOctets64 = _NUser6TxDataOctets64_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 14, 1, 2, 1, 41),
    _NUser6TxDataOctets64_Type()
)
nUser6TxDataOctets64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nUser6TxDataOctets64.setStatus("current")
_NUser6ForwardMode_Type = ArubaUserForwardMode
_NUser6ForwardMode_Object = MibTableColumn
nUser6ForwardMode = _NUser6ForwardMode_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 14, 1, 2, 1, 42),
    _NUser6ForwardMode_Type()
)
nUser6ForwardMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nUser6ForwardMode.setStatus("current")
_NUser6EncryptionMethod_Type = ArubaEncryptionType
_NUser6EncryptionMethod_Object = MibTableColumn
nUser6EncryptionMethod = _NUser6EncryptionMethod_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 14, 1, 2, 1, 43),
    _NUser6EncryptionMethod_Type()
)
nUser6EncryptionMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nUser6EncryptionMethod.setStatus("current")
_NVIAUser6DeviceID_Type = MacAddress
_NVIAUser6DeviceID_Object = MibTableColumn
nVIAUser6DeviceID = _NVIAUser6DeviceID_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 14, 1, 2, 1, 44),
    _NVIAUser6DeviceID_Type()
)
nVIAUser6DeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nVIAUser6DeviceID.setStatus("current")
_WlsxUser6SessionTimeTable_Object = MibTable
wlsxUser6SessionTimeTable = _WlsxUser6SessionTimeTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 14, 1, 3)
)
if mibBuilder.loadTexts:
    wlsxUser6SessionTimeTable.setStatus("current")
_WlsxUser6SessionTimeEntry_Object = MibTableRow
wlsxUser6SessionTimeEntry = _WlsxUser6SessionTimeEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 14, 1, 3, 1)
)
wlsxUser6SessionTimeEntry.setIndexNames(
    (0, "WLSX-WLAN-MIB", "wlanESSID"),
    (0, "WLSX-USER6-MIB", "wlsxUser6SessionTimeLength"),
)
if mibBuilder.loadTexts:
    wlsxUser6SessionTimeEntry.setStatus("current")
_WlsxUser6SessionTimeLength_Type = Integer32
_WlsxUser6SessionTimeLength_Object = MibTableColumn
wlsxUser6SessionTimeLength = _WlsxUser6SessionTimeLength_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 14, 1, 3, 1, 1),
    _WlsxUser6SessionTimeLength_Type()
)
wlsxUser6SessionTimeLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wlsxUser6SessionTimeLength.setStatus("current")
_WlsxUser6SessionTimeCount_Type = Counter32
_WlsxUser6SessionTimeCount_Object = MibTableColumn
wlsxUser6SessionTimeCount = _WlsxUser6SessionTimeCount_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 14, 1, 3, 1, 2),
    _WlsxUser6SessionTimeCount_Type()
)
wlsxUser6SessionTimeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxUser6SessionTimeCount.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WLSX-USER6-MIB",
    **{"wlsxUser6InfoGroup": wlsxUser6InfoGroup,
       "wlsxSwitchUser6Table": wlsxSwitchUser6Table,
       "wlsxSwitchUser6Entry": wlsxSwitchUser6Entry,
       "user6IpAddress": user6IpAddress,
       "user6PhyAddress": user6PhyAddress,
       "user6Name": user6Name,
       "user6Role": user6Role,
       "user6UpTime": user6UpTime,
       "user6AuthenticationMethod": user6AuthenticationMethod,
       "user6Location": user6Location,
       "user6ServerName": user6ServerName,
       "user6ConnectedVlan": user6ConnectedVlan,
       "user6ConnectedSlot": user6ConnectedSlot,
       "user6ConnectedPort": user6ConnectedPort,
       "user6BWContractName": user6BWContractName,
       "user6BWContractUsage": user6BWContractUsage,
       "user6ConnectedModule": user6ConnectedModule,
       "wlsxUser6MIB": wlsxUser6MIB,
       "wlsxUser6AllInfoGroup": wlsxUser6AllInfoGroup,
       "wlsxTotalNumOfUsers6": wlsxTotalNumOfUsers6,
       "wlsxUser6Table": wlsxUser6Table,
       "wlsxUser6Entry": wlsxUser6Entry,
       "nUser6PhyAddress": nUser6PhyAddress,
       "nUser6IpAddress": nUser6IpAddress,
       "nUser6Name": nUser6Name,
       "nUser6Role": nUser6Role,
       "nUser6UpTime": nUser6UpTime,
       "nUser6AuthenticationMethod": nUser6AuthenticationMethod,
       "nUser6SubAuthenticationMethod": nUser6SubAuthenticationMethod,
       "nUser6AuthServerName": nUser6AuthServerName,
       "nUser6ExtVPNAddress": nUser6ExtVPNAddress,
       "nUser6ApLocation": nUser6ApLocation,
       "nUser6ApBSSID": nUser6ApBSSID,
       "nUser6IsOnHomeAgent": nUser6IsOnHomeAgent,
       "nUser6HomeAgentIpAddress": nUser6HomeAgentIpAddress,
       "nUser6MobilityStatus": nUser6MobilityStatus,
       "nUser6HomeVlan": nUser6HomeVlan,
       "nUser6DefaultVlan": nUser6DefaultVlan,
       "nUser6AssignedVlan": nUser6AssignedVlan,
       "nUser6BWContractName": nUser6BWContractName,
       "nUser6BWContractUsage": nUser6BWContractUsage,
       "nUser6BWContractId": nUser6BWContractId,
       "nUser6IsProxyArpEnabled": nUser6IsProxyArpEnabled,
       "nUser6CurrentVlan": nUser6CurrentVlan,
       "nUser6IsWired": nUser6IsWired,
       "nUser6ConnectedSlot": nUser6ConnectedSlot,
       "nUser6ConnectedPort": nUser6ConnectedPort,
       "nUser6PhyType": nUser6PhyType,
       "nUser6MobilityDomainName": nUser6MobilityDomainName,
       "nUser6UPBWContractName": nUser6UPBWContractName,
       "nUser6UPBWContractUsage": nUser6UPBWContractUsage,
       "nUser6UPBWContractId": nUser6UPBWContractId,
       "nUser6DNBWContractName": nUser6DNBWContractName,
       "nUser6DNBWContractUsage": nUser6DNBWContractUsage,
       "nUser6DNBWContractId": nUser6DNBWContractId,
       "nUser6HTMode": nUser6HTMode,
       "nUser6DeviceID": nUser6DeviceID,
       "nUser6DeviceType": nUser6DeviceType,
       "nUser6ConnectedModule": nUser6ConnectedModule,
       "nUser6RxDataPkts64": nUser6RxDataPkts64,
       "nUser6TxDataPkts64": nUser6TxDataPkts64,
       "nUser6RxDataOctets64": nUser6RxDataOctets64,
       "nUser6TxDataOctets64": nUser6TxDataOctets64,
       "nUser6ForwardMode": nUser6ForwardMode,
       "nUser6EncryptionMethod": nUser6EncryptionMethod,
       "nVIAUser6DeviceID": nVIAUser6DeviceID,
       "wlsxUser6SessionTimeTable": wlsxUser6SessionTimeTable,
       "wlsxUser6SessionTimeEntry": wlsxUser6SessionTimeEntry,
       "wlsxUser6SessionTimeLength": wlsxUser6SessionTimeLength,
       "wlsxUser6SessionTimeCount": wlsxUser6SessionTimeCount}
)
