# SNMP MIB module (CISCO-LWAPP-MOBILITY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-LWAPP-MOBILITY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:04:47 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

ciscoLwappMobilityMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 576)
)
ciscoLwappMobilityMIB.setRevisions(
        ("2010-08-23 00:00",
         "2006-07-19 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoLwappMobilityMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoLwappMobilityMIBNotifs = _CiscoLwappMobilityMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 0)
)
_CiscoLwappMobilityMIBObjects_ObjectIdentity = ObjectIdentity
ciscoLwappMobilityMIBObjects = _CiscoLwappMobilityMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 1)
)
_CLMobilityAnchorTable_Object = MibTable
cLMobilityAnchorTable = _CLMobilityAnchorTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 1, 1)
)
if mibBuilder.loadTexts:
    cLMobilityAnchorTable.setStatus("current")
_CLMobilityAnchorEntry_Object = MibTableRow
cLMobilityAnchorEntry = _CLMobilityAnchorEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 1, 1, 1)
)
cLMobilityAnchorEntry.setIndexNames(
    (0, "CISCO-LWAPP-MOBILITY-MIB", "cLMobilityAnchorWlanSsid"),
    (0, "CISCO-LWAPP-MOBILITY-MIB", "cLMobilityAnchorSwitchAddressType"),
    (0, "CISCO-LWAPP-MOBILITY-MIB", "cLMobilityAnchorSwitchAddress"),
)
if mibBuilder.loadTexts:
    cLMobilityAnchorEntry.setStatus("current")


class _CLMobilityAnchorWlanSsid_Type(DisplayString):
    """Custom type cLMobilityAnchorWlanSsid based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CLMobilityAnchorWlanSsid_Type.__name__ = "DisplayString"
_CLMobilityAnchorWlanSsid_Object = MibTableColumn
cLMobilityAnchorWlanSsid = _CLMobilityAnchorWlanSsid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 1, 1, 1, 1),
    _CLMobilityAnchorWlanSsid_Type()
)
cLMobilityAnchorWlanSsid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLMobilityAnchorWlanSsid.setStatus("current")
_CLMobilityAnchorSwitchAddressType_Type = InetAddressType
_CLMobilityAnchorSwitchAddressType_Object = MibTableColumn
cLMobilityAnchorSwitchAddressType = _CLMobilityAnchorSwitchAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 1, 1, 1, 2),
    _CLMobilityAnchorSwitchAddressType_Type()
)
cLMobilityAnchorSwitchAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLMobilityAnchorSwitchAddressType.setStatus("current")
_CLMobilityAnchorSwitchAddress_Type = InetAddress
_CLMobilityAnchorSwitchAddress_Object = MibTableColumn
cLMobilityAnchorSwitchAddress = _CLMobilityAnchorSwitchAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 1, 1, 1, 3),
    _CLMobilityAnchorSwitchAddress_Type()
)
cLMobilityAnchorSwitchAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLMobilityAnchorSwitchAddress.setStatus("current")


class _CLMobilityAnchorStatus_Type(Bits):
    """Custom type cLMobilityAnchorStatus based on Bits"""
    namedValues = NamedValues(
        *(("controlpath", 0),
          ("datapath", 1))
    )

_CLMobilityAnchorStatus_Type.__name__ = "Bits"
_CLMobilityAnchorStatus_Object = MibTableColumn
cLMobilityAnchorStatus = _CLMobilityAnchorStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 1, 1, 1, 4),
    _CLMobilityAnchorStatus_Type()
)
cLMobilityAnchorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLMobilityAnchorStatus.setStatus("current")
_CLMobilityAnchorRowStatus_Type = RowStatus
_CLMobilityAnchorRowStatus_Object = MibTableColumn
cLMobilityAnchorRowStatus = _CLMobilityAnchorRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 1, 1, 1, 5),
    _CLMobilityAnchorRowStatus_Type()
)
cLMobilityAnchorRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLMobilityAnchorRowStatus.setStatus("current")
_CLMobilityAnchorGlobalDot11Config_ObjectIdentity = ObjectIdentity
cLMobilityAnchorGlobalDot11Config = _CLMobilityAnchorGlobalDot11Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 1, 2)
)


class _CLMobilityAnchorGroupKeepAliveNumber_Type(Integer32):
    """Custom type cLMobilityAnchorGroupKeepAliveNumber based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 20),
    )


_CLMobilityAnchorGroupKeepAliveNumber_Type.__name__ = "Integer32"
_CLMobilityAnchorGroupKeepAliveNumber_Object = MibScalar
cLMobilityAnchorGroupKeepAliveNumber = _CLMobilityAnchorGroupKeepAliveNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 1, 2, 1),
    _CLMobilityAnchorGroupKeepAliveNumber_Type()
)
cLMobilityAnchorGroupKeepAliveNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLMobilityAnchorGroupKeepAliveNumber.setStatus("current")


class _CLMobilityAnchorGroupKeepAliveInterval_Type(Integer32):
    """Custom type cLMobilityAnchorGroupKeepAliveInterval based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_CLMobilityAnchorGroupKeepAliveInterval_Type.__name__ = "Integer32"
_CLMobilityAnchorGroupKeepAliveInterval_Object = MibScalar
cLMobilityAnchorGroupKeepAliveInterval = _CLMobilityAnchorGroupKeepAliveInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 1, 2, 2),
    _CLMobilityAnchorGroupKeepAliveInterval_Type()
)
cLMobilityAnchorGroupKeepAliveInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLMobilityAnchorGroupKeepAliveInterval.setStatus("current")
_CLMobilityAnchorSmtStatus_Type = TruthValue
_CLMobilityAnchorSmtStatus_Object = MibScalar
cLMobilityAnchorSmtStatus = _CLMobilityAnchorSmtStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 1, 2, 3),
    _CLMobilityAnchorSmtStatus_Type()
)
cLMobilityAnchorSmtStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLMobilityAnchorSmtStatus.setStatus("current")
_CLMobilityAnchorCurrentSmt_Type = TruthValue
_CLMobilityAnchorCurrentSmt_Object = MibScalar
cLMobilityAnchorCurrentSmt = _CLMobilityAnchorCurrentSmt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 1, 2, 4),
    _CLMobilityAnchorCurrentSmt_Type()
)
cLMobilityAnchorCurrentSmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLMobilityAnchorCurrentSmt.setStatus("current")
_CLMobilityTrapVariables_ObjectIdentity = ObjectIdentity
cLMobilityTrapVariables = _CLMobilityTrapVariables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 1, 3)
)
_CLMobilityAnchorWlanId_Type = Unsigned32
_CLMobilityAnchorWlanId_Object = MibScalar
cLMobilityAnchorWlanId = _CLMobilityAnchorWlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 1, 3, 1),
    _CLMobilityAnchorWlanId_Type()
)
cLMobilityAnchorWlanId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cLMobilityAnchorWlanId.setStatus("current")
_CLMobilityAnchorAddressType_Type = InetAddressType
_CLMobilityAnchorAddressType_Object = MibScalar
cLMobilityAnchorAddressType = _CLMobilityAnchorAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 1, 3, 2),
    _CLMobilityAnchorAddressType_Type()
)
cLMobilityAnchorAddressType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cLMobilityAnchorAddressType.setStatus("current")
_CLMobilityAnchorAddress_Type = InetAddress
_CLMobilityAnchorAddress_Object = MibScalar
cLMobilityAnchorAddress = _CLMobilityAnchorAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 1, 3, 3),
    _CLMobilityAnchorAddress_Type()
)
cLMobilityAnchorAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cLMobilityAnchorAddress.setStatus("current")
_CLMobilityMulticastGroupConfig_ObjectIdentity = ObjectIdentity
cLMobilityMulticastGroupConfig = _CLMobilityMulticastGroupConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 1, 4)
)
_CLMobilityMulticastMessagingEnable_Type = TruthValue
_CLMobilityMulticastMessagingEnable_Object = MibScalar
cLMobilityMulticastMessagingEnable = _CLMobilityMulticastMessagingEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 1, 4, 1),
    _CLMobilityMulticastMessagingEnable_Type()
)
cLMobilityMulticastMessagingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLMobilityMulticastMessagingEnable.setStatus("current")
_CLMobilityMulticastGroupTable_Object = MibTable
cLMobilityMulticastGroupTable = _CLMobilityMulticastGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 1, 4, 2)
)
if mibBuilder.loadTexts:
    cLMobilityMulticastGroupTable.setStatus("current")
_CLMobilityMulticastGroupEntry_Object = MibTableRow
cLMobilityMulticastGroupEntry = _CLMobilityMulticastGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 1, 4, 2, 1)
)
cLMobilityMulticastGroupEntry.setIndexNames(
    (0, "CISCO-LWAPP-MOBILITY-MIB", "cLMobilityGroupMacAddress"),
)
if mibBuilder.loadTexts:
    cLMobilityMulticastGroupEntry.setStatus("current")
_CLMobilityGroupMacAddress_Type = MacAddress
_CLMobilityGroupMacAddress_Object = MibTableColumn
cLMobilityGroupMacAddress = _CLMobilityGroupMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 1, 4, 2, 1, 1),
    _CLMobilityGroupMacAddress_Type()
)
cLMobilityGroupMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLMobilityGroupMacAddress.setStatus("current")
_CLMobilityMulticastGroupIPAddress_Type = InetAddress
_CLMobilityMulticastGroupIPAddress_Object = MibTableColumn
cLMobilityMulticastGroupIPAddress = _CLMobilityMulticastGroupIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 1, 4, 2, 1, 2),
    _CLMobilityMulticastGroupIPAddress_Type()
)
cLMobilityMulticastGroupIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLMobilityMulticastGroupIPAddress.setStatus("current")
_CLMobilityMulticastGroupIPAddressType_Type = InetAddressType
_CLMobilityMulticastGroupIPAddressType_Object = MibTableColumn
cLMobilityMulticastGroupIPAddressType = _CLMobilityMulticastGroupIPAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 1, 4, 2, 1, 3),
    _CLMobilityMulticastGroupIPAddressType_Type()
)
cLMobilityMulticastGroupIPAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLMobilityMulticastGroupIPAddressType.setStatus("current")
_CLMobilityGroupMembersTable_Object = MibTable
cLMobilityGroupMembersTable = _CLMobilityGroupMembersTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 1, 5)
)
if mibBuilder.loadTexts:
    cLMobilityGroupMembersTable.setStatus("current")
_CLMobilityGroupMembersEntry_Object = MibTableRow
cLMobilityGroupMembersEntry = _CLMobilityGroupMembersEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 1, 5, 1)
)
cLMobilityGroupMembersEntry.setIndexNames(
    (0, "CISCO-LWAPP-MOBILITY-MIB", "cLMobilityGroupMacAddress"),
)
if mibBuilder.loadTexts:
    cLMobilityGroupMembersEntry.setStatus("current")
_CLMobilityGroupMemberIPAddressType_Type = InetAddressType
_CLMobilityGroupMemberIPAddressType_Object = MibTableColumn
cLMobilityGroupMemberIPAddressType = _CLMobilityGroupMemberIPAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 1, 5, 1, 1),
    _CLMobilityGroupMemberIPAddressType_Type()
)
cLMobilityGroupMemberIPAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLMobilityGroupMemberIPAddressType.setStatus("current")
_CLMobilityGroupMemberIPAddress_Type = InetAddress
_CLMobilityGroupMemberIPAddress_Object = MibTableColumn
cLMobilityGroupMemberIPAddress = _CLMobilityGroupMemberIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 1, 5, 1, 2),
    _CLMobilityGroupMemberIPAddress_Type()
)
cLMobilityGroupMemberIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLMobilityGroupMemberIPAddress.setStatus("current")


class _CLMobilityGroupMemberControlPathStatusUp_Type(TruthValue):
    """Custom type cLMobilityGroupMemberControlPathStatusUp based on TruthValue"""


_CLMobilityGroupMemberControlPathStatusUp_Object = MibTableColumn
cLMobilityGroupMemberControlPathStatusUp = _CLMobilityGroupMemberControlPathStatusUp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 1, 5, 1, 3),
    _CLMobilityGroupMemberControlPathStatusUp_Type()
)
cLMobilityGroupMemberControlPathStatusUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLMobilityGroupMemberControlPathStatusUp.setStatus("current")


class _CLMobilityGroupMemberDataPathStatusUp_Type(TruthValue):
    """Custom type cLMobilityGroupMemberDataPathStatusUp based on TruthValue"""


_CLMobilityGroupMemberDataPathStatusUp_Object = MibTableColumn
cLMobilityGroupMemberDataPathStatusUp = _CLMobilityGroupMemberDataPathStatusUp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 1, 5, 1, 4),
    _CLMobilityGroupMemberDataPathStatusUp_Type()
)
cLMobilityGroupMemberDataPathStatusUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLMobilityGroupMemberDataPathStatusUp.setStatus("current")
_CLMobilityForeignWlcMapTable_Object = MibTable
cLMobilityForeignWlcMapTable = _CLMobilityForeignWlcMapTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 1, 6)
)
if mibBuilder.loadTexts:
    cLMobilityForeignWlcMapTable.setStatus("current")
_CLMobilityForeignWlcMapEntry_Object = MibTableRow
cLMobilityForeignWlcMapEntry = _CLMobilityForeignWlcMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 1, 6, 1)
)
cLMobilityForeignWlcMapEntry.setIndexNames(
    (0, "CISCO-LWAPP-MOBILITY-MIB", "cLMobilityAnchorWlanSsid"),
    (0, "CISCO-LWAPP-MOBILITY-MIB", "cLMobilityForeignWlcMapMacAddress"),
)
if mibBuilder.loadTexts:
    cLMobilityForeignWlcMapEntry.setStatus("current")
_CLMobilityForeignWlcMapMacAddress_Type = MacAddress
_CLMobilityForeignWlcMapMacAddress_Object = MibTableColumn
cLMobilityForeignWlcMapMacAddress = _CLMobilityForeignWlcMapMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 1, 6, 1, 1),
    _CLMobilityForeignWlcMapMacAddress_Type()
)
cLMobilityForeignWlcMapMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLMobilityForeignWlcMapMacAddress.setStatus("current")
_CLMobilityForeignWlcMapIf_Type = SnmpAdminString
_CLMobilityForeignWlcMapIf_Object = MibTableColumn
cLMobilityForeignWlcMapIf = _CLMobilityForeignWlcMapIf_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 1, 6, 1, 2),
    _CLMobilityForeignWlcMapIf_Type()
)
cLMobilityForeignWlcMapIf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLMobilityForeignWlcMapIf.setStatus("current")
_CLMobilityForeignWlcMapRowStatus_Type = RowStatus
_CLMobilityForeignWlcMapRowStatus_Object = MibTableColumn
cLMobilityForeignWlcMapRowStatus = _CLMobilityForeignWlcMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 1, 6, 1, 3),
    _CLMobilityForeignWlcMapRowStatus_Type()
)
cLMobilityForeignWlcMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLMobilityForeignWlcMapRowStatus.setStatus("current")
_CiscoLwappMobilityMIBConform_ObjectIdentity = ObjectIdentity
ciscoLwappMobilityMIBConform = _CiscoLwappMobilityMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 2)
)
_CiscoLwappMobilityMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoLwappMobilityMIBCompliances = _CiscoLwappMobilityMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 2, 1)
)
_CiscoLwappMobilityMIBGroups_ObjectIdentity = ObjectIdentity
ciscoLwappMobilityMIBGroups = _CiscoLwappMobilityMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 2, 2)
)

# Managed Objects groups

cLNplus1RedundancyRev01ConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 2, 2, 1)
)
cLNplus1RedundancyRev01ConfigGroup.setObjects(
      *(("CISCO-LWAPP-MOBILITY-MIB", "cLMobilityAnchorGroupKeepAliveNumber"),
        ("CISCO-LWAPP-MOBILITY-MIB", "cLMobilityAnchorGroupKeepAliveInterval"))
)
if mibBuilder.loadTexts:
    cLNplus1RedundancyRev01ConfigGroup.setStatus("current")

cLNplus1RedundancyRev01StatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 2, 2, 2)
)
cLNplus1RedundancyRev01StatusGroup.setObjects(
      *(("CISCO-LWAPP-MOBILITY-MIB", "cLMobilityAnchorStatus"),
        ("CISCO-LWAPP-MOBILITY-MIB", "cLMobilityAnchorRowStatus"),
        ("CISCO-LWAPP-MOBILITY-MIB", "cLMobilityAnchorWlanId"),
        ("CISCO-LWAPP-MOBILITY-MIB", "cLMobilityAnchorAddressType"),
        ("CISCO-LWAPP-MOBILITY-MIB", "cLMobilityAnchorAddress"))
)
if mibBuilder.loadTexts:
    cLNplus1RedundancyRev01StatusGroup.setStatus("current")

cLSymmetricTunnelingRev01ConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 2, 2, 4)
)
cLSymmetricTunnelingRev01ConfigGroup.setObjects(
    ("CISCO-LWAPP-MOBILITY-MIB", "cLMobilityAnchorSmtStatus")
)
if mibBuilder.loadTexts:
    cLSymmetricTunnelingRev01ConfigGroup.setStatus("current")

cLSymmetricTunnelingRev01StatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 2, 2, 5)
)
cLSymmetricTunnelingRev01StatusGroup.setObjects(
    ("CISCO-LWAPP-MOBILITY-MIB", "cLMobilityAnchorCurrentSmt")
)
if mibBuilder.loadTexts:
    cLSymmetricTunnelingRev01StatusGroup.setStatus("current")

cLMobilityGroupRev01ConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 2, 2, 6)
)
cLMobilityGroupRev01ConfigGroup.setObjects(
      *(("CISCO-LWAPP-MOBILITY-MIB", "cLMobilityMulticastMessagingEnable"),
        ("CISCO-LWAPP-MOBILITY-MIB", "cLMobilityMulticastGroupIPAddress"),
        ("CISCO-LWAPP-MOBILITY-MIB", "cLMobilityMulticastGroupIPAddressType"),
        ("CISCO-LWAPP-MOBILITY-MIB", "cLMobilityGroupMemberIPAddressType"),
        ("CISCO-LWAPP-MOBILITY-MIB", "cLMobilityGroupMemberIPAddress"),
        ("CISCO-LWAPP-MOBILITY-MIB", "cLMobilityGroupMemberControlPathStatusUp"),
        ("CISCO-LWAPP-MOBILITY-MIB", "cLMobilityGroupMemberDataPathStatusUp"),
        ("CISCO-LWAPP-MOBILITY-MIB", "cLMobilityForeignWlcMapIf"),
        ("CISCO-LWAPP-MOBILITY-MIB", "cLMobilityForeignWlcMapRowStatus"))
)
if mibBuilder.loadTexts:
    cLMobilityGroupRev01ConfigGroup.setStatus("current")


# Notification objects

ciscoLwappMobilityAnchorControlPathDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 0, 1)
)
ciscoLwappMobilityAnchorControlPathDown.setObjects(
      *(("CISCO-LWAPP-MOBILITY-MIB", "cLMobilityAnchorAddressType"),
        ("CISCO-LWAPP-MOBILITY-MIB", "cLMobilityAnchorAddress"))
)
if mibBuilder.loadTexts:
    ciscoLwappMobilityAnchorControlPathDown.setStatus(
        "current"
    )

ciscoLwappMobilityAnchorControlPathUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 0, 2)
)
ciscoLwappMobilityAnchorControlPathUp.setObjects(
      *(("CISCO-LWAPP-MOBILITY-MIB", "cLMobilityAnchorAddressType"),
        ("CISCO-LWAPP-MOBILITY-MIB", "cLMobilityAnchorAddress"))
)
if mibBuilder.loadTexts:
    ciscoLwappMobilityAnchorControlPathUp.setStatus(
        "current"
    )

ciscoLwappMobilityAnchorDataPathDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 0, 3)
)
ciscoLwappMobilityAnchorDataPathDown.setObjects(
      *(("CISCO-LWAPP-MOBILITY-MIB", "cLMobilityAnchorAddressType"),
        ("CISCO-LWAPP-MOBILITY-MIB", "cLMobilityAnchorAddress"))
)
if mibBuilder.loadTexts:
    ciscoLwappMobilityAnchorDataPathDown.setStatus(
        "current"
    )

ciscoLwappMobilityAnchorDataPathUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 0, 4)
)
ciscoLwappMobilityAnchorDataPathUp.setObjects(
      *(("CISCO-LWAPP-MOBILITY-MIB", "cLMobilityAnchorAddressType"),
        ("CISCO-LWAPP-MOBILITY-MIB", "cLMobilityAnchorAddress"))
)
if mibBuilder.loadTexts:
    ciscoLwappMobilityAnchorDataPathUp.setStatus(
        "current"
    )

ciscoLwappMobilityAllAnchorsOnWlanDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 0, 5)
)
ciscoLwappMobilityAllAnchorsOnWlanDown.setObjects(
    ("CISCO-LWAPP-MOBILITY-MIB", "cLMobilityAnchorWlanId")
)
if mibBuilder.loadTexts:
    ciscoLwappMobilityAllAnchorsOnWlanDown.setStatus(
        "current"
    )

ciscoLwappMobilityOneAnchorOnWlanUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 0, 6)
)
ciscoLwappMobilityOneAnchorOnWlanUp.setObjects(
    ("CISCO-LWAPP-MOBILITY-MIB", "cLMobilityAnchorWlanId")
)
if mibBuilder.loadTexts:
    ciscoLwappMobilityOneAnchorOnWlanUp.setStatus(
        "current"
    )


# Notifications groups

cLNplus1RedundancyRev01NotifsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 2, 2, 3)
)
cLNplus1RedundancyRev01NotifsGroup.setObjects(
      *(("CISCO-LWAPP-MOBILITY-MIB", "ciscoLwappMobilityAnchorControlPathDown"),
        ("CISCO-LWAPP-MOBILITY-MIB", "ciscoLwappMobilityAnchorControlPathUp"),
        ("CISCO-LWAPP-MOBILITY-MIB", "ciscoLwappMobilityAnchorDataPathDown"),
        ("CISCO-LWAPP-MOBILITY-MIB", "ciscoLwappMobilityAnchorDataPathUp"),
        ("CISCO-LWAPP-MOBILITY-MIB", "ciscoLwappMobilityAllAnchorsOnWlanDown"),
        ("CISCO-LWAPP-MOBILITY-MIB", "ciscoLwappMobilityOneAnchorOnWlanUp"))
)
if mibBuilder.loadTexts:
    cLNplus1RedundancyRev01NotifsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoLwappMobilityMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoLwappMobilityMIBCompliance.setStatus(
        "deprecated"
    )

ciscoLwappMobilityMIBComplianceRev01 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoLwappMobilityMIBComplianceRev01.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-LWAPP-MOBILITY-MIB",
    **{"ciscoLwappMobilityMIB": ciscoLwappMobilityMIB,
       "ciscoLwappMobilityMIBNotifs": ciscoLwappMobilityMIBNotifs,
       "ciscoLwappMobilityAnchorControlPathDown": ciscoLwappMobilityAnchorControlPathDown,
       "ciscoLwappMobilityAnchorControlPathUp": ciscoLwappMobilityAnchorControlPathUp,
       "ciscoLwappMobilityAnchorDataPathDown": ciscoLwappMobilityAnchorDataPathDown,
       "ciscoLwappMobilityAnchorDataPathUp": ciscoLwappMobilityAnchorDataPathUp,
       "ciscoLwappMobilityAllAnchorsOnWlanDown": ciscoLwappMobilityAllAnchorsOnWlanDown,
       "ciscoLwappMobilityOneAnchorOnWlanUp": ciscoLwappMobilityOneAnchorOnWlanUp,
       "ciscoLwappMobilityMIBObjects": ciscoLwappMobilityMIBObjects,
       "cLMobilityAnchorTable": cLMobilityAnchorTable,
       "cLMobilityAnchorEntry": cLMobilityAnchorEntry,
       "cLMobilityAnchorWlanSsid": cLMobilityAnchorWlanSsid,
       "cLMobilityAnchorSwitchAddressType": cLMobilityAnchorSwitchAddressType,
       "cLMobilityAnchorSwitchAddress": cLMobilityAnchorSwitchAddress,
       "cLMobilityAnchorStatus": cLMobilityAnchorStatus,
       "cLMobilityAnchorRowStatus": cLMobilityAnchorRowStatus,
       "cLMobilityAnchorGlobalDot11Config": cLMobilityAnchorGlobalDot11Config,
       "cLMobilityAnchorGroupKeepAliveNumber": cLMobilityAnchorGroupKeepAliveNumber,
       "cLMobilityAnchorGroupKeepAliveInterval": cLMobilityAnchorGroupKeepAliveInterval,
       "cLMobilityAnchorSmtStatus": cLMobilityAnchorSmtStatus,
       "cLMobilityAnchorCurrentSmt": cLMobilityAnchorCurrentSmt,
       "cLMobilityTrapVariables": cLMobilityTrapVariables,
       "cLMobilityAnchorWlanId": cLMobilityAnchorWlanId,
       "cLMobilityAnchorAddressType": cLMobilityAnchorAddressType,
       "cLMobilityAnchorAddress": cLMobilityAnchorAddress,
       "cLMobilityMulticastGroupConfig": cLMobilityMulticastGroupConfig,
       "cLMobilityMulticastMessagingEnable": cLMobilityMulticastMessagingEnable,
       "cLMobilityMulticastGroupTable": cLMobilityMulticastGroupTable,
       "cLMobilityMulticastGroupEntry": cLMobilityMulticastGroupEntry,
       "cLMobilityGroupMacAddress": cLMobilityGroupMacAddress,
       "cLMobilityMulticastGroupIPAddress": cLMobilityMulticastGroupIPAddress,
       "cLMobilityMulticastGroupIPAddressType": cLMobilityMulticastGroupIPAddressType,
       "cLMobilityGroupMembersTable": cLMobilityGroupMembersTable,
       "cLMobilityGroupMembersEntry": cLMobilityGroupMembersEntry,
       "cLMobilityGroupMemberIPAddressType": cLMobilityGroupMemberIPAddressType,
       "cLMobilityGroupMemberIPAddress": cLMobilityGroupMemberIPAddress,
       "cLMobilityGroupMemberControlPathStatusUp": cLMobilityGroupMemberControlPathStatusUp,
       "cLMobilityGroupMemberDataPathStatusUp": cLMobilityGroupMemberDataPathStatusUp,
       "cLMobilityForeignWlcMapTable": cLMobilityForeignWlcMapTable,
       "cLMobilityForeignWlcMapEntry": cLMobilityForeignWlcMapEntry,
       "cLMobilityForeignWlcMapMacAddress": cLMobilityForeignWlcMapMacAddress,
       "cLMobilityForeignWlcMapIf": cLMobilityForeignWlcMapIf,
       "cLMobilityForeignWlcMapRowStatus": cLMobilityForeignWlcMapRowStatus,
       "ciscoLwappMobilityMIBConform": ciscoLwappMobilityMIBConform,
       "ciscoLwappMobilityMIBCompliances": ciscoLwappMobilityMIBCompliances,
       "ciscoLwappMobilityMIBCompliance": ciscoLwappMobilityMIBCompliance,
       "ciscoLwappMobilityMIBComplianceRev01": ciscoLwappMobilityMIBComplianceRev01,
       "ciscoLwappMobilityMIBGroups": ciscoLwappMobilityMIBGroups,
       "cLNplus1RedundancyRev01ConfigGroup": cLNplus1RedundancyRev01ConfigGroup,
       "cLNplus1RedundancyRev01StatusGroup": cLNplus1RedundancyRev01StatusGroup,
       "cLNplus1RedundancyRev01NotifsGroup": cLNplus1RedundancyRev01NotifsGroup,
       "cLSymmetricTunnelingRev01ConfigGroup": cLSymmetricTunnelingRev01ConfigGroup,
       "cLSymmetricTunnelingRev01StatusGroup": cLSymmetricTunnelingRev01StatusGroup,
       "cLMobilityGroupRev01ConfigGroup": cLMobilityGroupRev01ConfigGroup}
)
