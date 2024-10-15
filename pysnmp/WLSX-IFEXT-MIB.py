# SNMP MIB module (WLSX-IFEXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WLSX-IFEXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:14:06 2024
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

(ArubaDot1dState,
 ArubaEnableValue,
 ArubaIfType,
 ArubaOperStateValue,
 ArubaPoeState,
 ArubaPortDuplex,
 ArubaPortMode,
 ArubaPortSpeed,
 ArubaPortType,
 ArubaVlanValidRange) = mibBuilder.importSymbols(
    "ARUBA-TC",
    "ArubaDot1dState",
    "ArubaEnableValue",
    "ArubaIfType",
    "ArubaOperStateValue",
    "ArubaPoeState",
    "ArubaPortDuplex",
    "ArubaPortMode",
    "ArubaPortSpeed",
    "ArubaPortType",
    "ArubaVlanValidRange")

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


# MODULE-IDENTITY

wlsxIfExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3)
)
wlsxIfExtMIB.setRevisions(
        ("2012-07-12 00:00",
         "1910-01-26 18:06")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WlsxIfExtGroup_ObjectIdentity = ObjectIdentity
wlsxIfExtGroup = _WlsxIfExtGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1)
)
_WlsxIfExtPortTable_Object = MibTable
wlsxIfExtPortTable = _WlsxIfExtPortTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    wlsxIfExtPortTable.setStatus("deprecated")
_WlsxIfExtPortEntry_Object = MibTableRow
wlsxIfExtPortEntry = _WlsxIfExtPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 1, 1)
)
wlsxIfExtPortEntry.setIndexNames(
    (0, "WLSX-IFEXT-MIB", "ifExtSlotNumber"),
    (0, "WLSX-IFEXT-MIB", "ifExtPortNumber"),
)
if mibBuilder.loadTexts:
    wlsxIfExtPortEntry.setStatus("deprecated")
_IfExtSlotNumber_Type = Integer32
_IfExtSlotNumber_Object = MibTableColumn
ifExtSlotNumber = _IfExtSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 1, 1, 1),
    _IfExtSlotNumber_Type()
)
ifExtSlotNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ifExtSlotNumber.setStatus("deprecated")
_IfExtPortNumber_Type = Integer32
_IfExtPortNumber_Object = MibTableColumn
ifExtPortNumber = _IfExtPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 1, 1, 2),
    _IfExtPortNumber_Type()
)
ifExtPortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ifExtPortNumber.setStatus("deprecated")
_IfExtPortIfIndex_Type = Integer32
_IfExtPortIfIndex_Object = MibTableColumn
ifExtPortIfIndex = _IfExtPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 1, 1, 3),
    _IfExtPortIfIndex_Type()
)
ifExtPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifExtPortIfIndex.setStatus("deprecated")
_IfExtAdminState_Type = ArubaEnableValue
_IfExtAdminState_Object = MibTableColumn
ifExtAdminState = _IfExtAdminState_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 1, 1, 4),
    _IfExtAdminState_Type()
)
ifExtAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifExtAdminState.setStatus("deprecated")


class _IfExtOperState_Type(Integer32):
    """Custom type ifExtOperState based on Integer32"""
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
          ("testing", 3),
          ("up", 1))
    )


_IfExtOperState_Type.__name__ = "Integer32"
_IfExtOperState_Object = MibTableColumn
ifExtOperState = _IfExtOperState_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 1, 1, 5),
    _IfExtOperState_Type()
)
ifExtOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifExtOperState.setStatus("deprecated")
_IfExtPoeState_Type = ArubaPoeState
_IfExtPoeState_Object = MibTableColumn
ifExtPoeState = _IfExtPoeState_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 1, 1, 6),
    _IfExtPoeState_Type()
)
ifExtPoeState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifExtPoeState.setStatus("deprecated")
_IfExtIsTrusted_Type = TruthValue
_IfExtIsTrusted_Object = MibTableColumn
ifExtIsTrusted = _IfExtIsTrusted_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 1, 1, 7),
    _IfExtIsTrusted_Type()
)
ifExtIsTrusted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifExtIsTrusted.setStatus("deprecated")
_IfExtDot1DState_Type = ArubaDot1dState
_IfExtDot1DState_Object = MibTableColumn
ifExtDot1DState = _IfExtDot1DState_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 1, 1, 8),
    _IfExtDot1DState_Type()
)
ifExtDot1DState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifExtDot1DState.setStatus("deprecated")
_IfExtMode_Type = ArubaPortMode
_IfExtMode_Object = MibTableColumn
ifExtMode = _IfExtMode_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 1, 1, 9),
    _IfExtMode_Type()
)
ifExtMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifExtMode.setStatus("deprecated")
_IfExtAccessVlanId_Type = ArubaVlanValidRange
_IfExtAccessVlanId_Object = MibTableColumn
ifExtAccessVlanId = _IfExtAccessVlanId_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 1, 1, 10),
    _IfExtAccessVlanId_Type()
)
ifExtAccessVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifExtAccessVlanId.setStatus("deprecated")
_IfExtTrunkNativeVlanId_Type = ArubaVlanValidRange
_IfExtTrunkNativeVlanId_Object = MibTableColumn
ifExtTrunkNativeVlanId = _IfExtTrunkNativeVlanId_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 1, 1, 11),
    _IfExtTrunkNativeVlanId_Type()
)
ifExtTrunkNativeVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifExtTrunkNativeVlanId.setStatus("deprecated")
_IfExtTrunkIsAllowedAll_Type = TruthValue
_IfExtTrunkIsAllowedAll_Object = MibTableColumn
ifExtTrunkIsAllowedAll = _IfExtTrunkIsAllowedAll_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 1, 1, 12),
    _IfExtTrunkIsAllowedAll_Type()
)
ifExtTrunkIsAllowedAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifExtTrunkIsAllowedAll.setStatus("deprecated")


class _IfExtTrunkAllowedVlanList_Type(OctetString):
    """Custom type ifExtTrunkAllowedVlanList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_IfExtTrunkAllowedVlanList_Type.__name__ = "OctetString"
_IfExtTrunkAllowedVlanList_Object = MibTableColumn
ifExtTrunkAllowedVlanList = _IfExtTrunkAllowedVlanList_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 1, 1, 13),
    _IfExtTrunkAllowedVlanList_Type()
)
ifExtTrunkAllowedVlanList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifExtTrunkAllowedVlanList.setStatus("deprecated")


class _IfExtIngressACLName_Type(DisplayString):
    """Custom type ifExtIngressACLName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_IfExtIngressACLName_Type.__name__ = "DisplayString"
_IfExtIngressACLName_Object = MibTableColumn
ifExtIngressACLName = _IfExtIngressACLName_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 1, 1, 14),
    _IfExtIngressACLName_Type()
)
ifExtIngressACLName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifExtIngressACLName.setStatus("deprecated")


class _IfExtEgressACLName_Type(DisplayString):
    """Custom type ifExtEgressACLName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_IfExtEgressACLName_Type.__name__ = "DisplayString"
_IfExtEgressACLName_Object = MibTableColumn
ifExtEgressACLName = _IfExtEgressACLName_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 1, 1, 15),
    _IfExtEgressACLName_Type()
)
ifExtEgressACLName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifExtEgressACLName.setStatus("deprecated")


class _IfExtSessionACLName_Type(DisplayString):
    """Custom type ifExtSessionACLName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_IfExtSessionACLName_Type.__name__ = "DisplayString"
_IfExtSessionACLName_Object = MibTableColumn
ifExtSessionACLName = _IfExtSessionACLName_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 1, 1, 16),
    _IfExtSessionACLName_Type()
)
ifExtSessionACLName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifExtSessionACLName.setStatus("deprecated")
_IfExtXsecVlan_Type = ArubaVlanValidRange
_IfExtXsecVlan_Object = MibTableColumn
ifExtXsecVlan = _IfExtXsecVlan_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 1, 1, 17),
    _IfExtXsecVlan_Type()
)
ifExtXsecVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifExtXsecVlan.setStatus("deprecated")
_IfExtIsMonitoring_Type = TruthValue
_IfExtIsMonitoring_Object = MibTableColumn
ifExtIsMonitoring = _IfExtIsMonitoring_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 1, 1, 18),
    _IfExtIsMonitoring_Type()
)
ifExtIsMonitoring.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifExtIsMonitoring.setStatus("deprecated")
_IfExtIsMux_Type = TruthValue
_IfExtIsMux_Object = MibTableColumn
ifExtIsMux = _IfExtIsMux_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 1, 1, 19),
    _IfExtIsMux_Type()
)
ifExtIsMux.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifExtIsMux.setStatus("deprecated")
_IfExtUserSlotNumber_Type = Integer32
_IfExtUserSlotNumber_Object = MibTableColumn
ifExtUserSlotNumber = _IfExtUserSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 1, 1, 20),
    _IfExtUserSlotNumber_Type()
)
ifExtUserSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifExtUserSlotNumber.setStatus("deprecated")
_IfExtUserPortNumber_Type = Integer32
_IfExtUserPortNumber_Object = MibTableColumn
ifExtUserPortNumber = _IfExtUserPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 1, 1, 21),
    _IfExtUserPortNumber_Type()
)
ifExtUserPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifExtUserPortNumber.setStatus("deprecated")
_IfExtPortSpeed_Type = ArubaPortSpeed
_IfExtPortSpeed_Object = MibTableColumn
ifExtPortSpeed = _IfExtPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 1, 1, 22),
    _IfExtPortSpeed_Type()
)
ifExtPortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifExtPortSpeed.setStatus("deprecated")
_IfExtPortDuplex_Type = ArubaPortDuplex
_IfExtPortDuplex_Object = MibTableColumn
ifExtPortDuplex = _IfExtPortDuplex_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 1, 1, 23),
    _IfExtPortDuplex_Type()
)
ifExtPortDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifExtPortDuplex.setStatus("deprecated")
_IfExtPortType_Type = ArubaPortType
_IfExtPortType_Object = MibTableColumn
ifExtPortType = _IfExtPortType_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 1, 1, 24),
    _IfExtPortType_Type()
)
ifExtPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifExtPortType.setStatus("deprecated")
_IfExtDescr_Type = DisplayString
_IfExtDescr_Object = MibTableColumn
ifExtDescr = _IfExtDescr_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 1, 1, 25),
    _IfExtDescr_Type()
)
ifExtDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifExtDescr.setStatus("deprecated")
_IfExtUserModuleNumber_Type = Integer32
_IfExtUserModuleNumber_Object = MibTableColumn
ifExtUserModuleNumber = _IfExtUserModuleNumber_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 1, 1, 26),
    _IfExtUserModuleNumber_Type()
)
ifExtUserModuleNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifExtUserModuleNumber.setStatus("deprecated")
_WlsxIfExtVlanTable_Object = MibTable
wlsxIfExtVlanTable = _WlsxIfExtVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 2)
)
if mibBuilder.loadTexts:
    wlsxIfExtVlanTable.setStatus("current")
_WlsxIfExtVlanEntry_Object = MibTableRow
wlsxIfExtVlanEntry = _WlsxIfExtVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 2, 1)
)
wlsxIfExtVlanEntry.setIndexNames(
    (0, "WLSX-IFEXT-MIB", "ifExtVlanId"),
)
if mibBuilder.loadTexts:
    wlsxIfExtVlanEntry.setStatus("current")
_IfExtVlanId_Type = ArubaVlanValidRange
_IfExtVlanId_Object = MibTableColumn
ifExtVlanId = _IfExtVlanId_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 2, 1, 1),
    _IfExtVlanId_Type()
)
ifExtVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ifExtVlanId.setStatus("current")


class _IfExtVlanName_Type(DisplayString):
    """Custom type ifExtVlanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_IfExtVlanName_Type.__name__ = "DisplayString"
_IfExtVlanName_Object = MibTableColumn
ifExtVlanName = _IfExtVlanName_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 2, 1, 2),
    _IfExtVlanName_Type()
)
ifExtVlanName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifExtVlanName.setStatus("current")
_IfExtVlanStatus_Type = RowStatus
_IfExtVlanStatus_Object = MibTableColumn
ifExtVlanStatus = _IfExtVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 2, 1, 3),
    _IfExtVlanStatus_Type()
)
ifExtVlanStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifExtVlanStatus.setStatus("current")
_WlsxIfExtVlanMemberTable_Object = MibTable
wlsxIfExtVlanMemberTable = _WlsxIfExtVlanMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 3)
)
if mibBuilder.loadTexts:
    wlsxIfExtVlanMemberTable.setStatus("current")
_WlsxIfExtVlanMemberEntry_Object = MibTableRow
wlsxIfExtVlanMemberEntry = _WlsxIfExtVlanMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 3, 1)
)
wlsxIfExtVlanMemberEntry.setIndexNames(
    (0, "WLSX-IFEXT-MIB", "ifExtVlanId"),
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    wlsxIfExtVlanMemberEntry.setStatus("current")
_IfExtVlanMemberStatus_Type = RowStatus
_IfExtVlanMemberStatus_Object = MibTableColumn
ifExtVlanMemberStatus = _IfExtVlanMemberStatus_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 3, 1, 1),
    _IfExtVlanMemberStatus_Type()
)
ifExtVlanMemberStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifExtVlanMemberStatus.setStatus("current")
_IfExtVlanMemberSlot_Type = Integer32
_IfExtVlanMemberSlot_Object = MibTableColumn
ifExtVlanMemberSlot = _IfExtVlanMemberSlot_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 3, 1, 2),
    _IfExtVlanMemberSlot_Type()
)
ifExtVlanMemberSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifExtVlanMemberSlot.setStatus("current")
_IfExtVlanMemberPort_Type = Integer32
_IfExtVlanMemberPort_Object = MibTableColumn
ifExtVlanMemberPort = _IfExtVlanMemberPort_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 3, 1, 3),
    _IfExtVlanMemberPort_Type()
)
ifExtVlanMemberPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifExtVlanMemberPort.setStatus("current")
_IfExtVlanMemberType_Type = ArubaIfType
_IfExtVlanMemberType_Object = MibTableColumn
ifExtVlanMemberType = _IfExtVlanMemberType_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 3, 1, 4),
    _IfExtVlanMemberType_Type()
)
ifExtVlanMemberType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifExtVlanMemberType.setStatus("current")
_WlsxIfExtVlanInterfaceTable_Object = MibTable
wlsxIfExtVlanInterfaceTable = _WlsxIfExtVlanInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 4)
)
if mibBuilder.loadTexts:
    wlsxIfExtVlanInterfaceTable.setStatus("current")
_WlsxIfExtVlanInterfaceEntry_Object = MibTableRow
wlsxIfExtVlanInterfaceEntry = _WlsxIfExtVlanInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 4, 1)
)
wlsxIfExtVlanInterfaceEntry.setIndexNames(
    (0, "WLSX-IFEXT-MIB", "ifExtVlanId"),
)
if mibBuilder.loadTexts:
    wlsxIfExtVlanInterfaceEntry.setStatus("current")
_IfExtVlanInterfaceIfIndex_Type = Integer32
_IfExtVlanInterfaceIfIndex_Object = MibTableColumn
ifExtVlanInterfaceIfIndex = _IfExtVlanInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 4, 1, 1),
    _IfExtVlanInterfaceIfIndex_Type()
)
ifExtVlanInterfaceIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifExtVlanInterfaceIfIndex.setStatus("current")


class _IfExtVlanInterfaceDescription_Type(DisplayString):
    """Custom type ifExtVlanInterfaceDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_IfExtVlanInterfaceDescription_Type.__name__ = "DisplayString"
_IfExtVlanInterfaceDescription_Object = MibTableColumn
ifExtVlanInterfaceDescription = _IfExtVlanInterfaceDescription_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 4, 1, 2),
    _IfExtVlanInterfaceDescription_Type()
)
ifExtVlanInterfaceDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifExtVlanInterfaceDescription.setStatus("current")


class _IfExtVlanInterfaceBWContract_Type(DisplayString):
    """Custom type ifExtVlanInterfaceBWContract based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_IfExtVlanInterfaceBWContract_Type.__name__ = "DisplayString"
_IfExtVlanInterfaceBWContract_Object = MibTableColumn
ifExtVlanInterfaceBWContract = _IfExtVlanInterfaceBWContract_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 4, 1, 3),
    _IfExtVlanInterfaceBWContract_Type()
)
ifExtVlanInterfaceBWContract.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifExtVlanInterfaceBWContract.setStatus("current")
_IfExtVlanInterfaceAdminState_Type = ArubaEnableValue
_IfExtVlanInterfaceAdminState_Object = MibTableColumn
ifExtVlanInterfaceAdminState = _IfExtVlanInterfaceAdminState_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 4, 1, 4),
    _IfExtVlanInterfaceAdminState_Type()
)
ifExtVlanInterfaceAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifExtVlanInterfaceAdminState.setStatus("current")
_IfExtVlanInterfaceOperState_Type = ArubaOperStateValue
_IfExtVlanInterfaceOperState_Object = MibTableColumn
ifExtVlanInterfaceOperState = _IfExtVlanInterfaceOperState_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 4, 1, 5),
    _IfExtVlanInterfaceOperState_Type()
)
ifExtVlanInterfaceOperState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifExtVlanInterfaceOperState.setStatus("current")
_IfExtVlanInterfaceIpAddress_Type = IpAddress
_IfExtVlanInterfaceIpAddress_Object = MibTableColumn
ifExtVlanInterfaceIpAddress = _IfExtVlanInterfaceIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 4, 1, 6),
    _IfExtVlanInterfaceIpAddress_Type()
)
ifExtVlanInterfaceIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifExtVlanInterfaceIpAddress.setStatus("current")
_IfExtVlanInterfaceIpMask_Type = IpAddress
_IfExtVlanInterfaceIpMask_Object = MibTableColumn
ifExtVlanInterfaceIpMask = _IfExtVlanInterfaceIpMask_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 4, 1, 7),
    _IfExtVlanInterfaceIpMask_Type()
)
ifExtVlanInterfaceIpMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifExtVlanInterfaceIpMask.setStatus("current")
_IfExtVlanInterfaceIsLocalArp_Type = ArubaEnableValue
_IfExtVlanInterfaceIsLocalArp_Object = MibTableColumn
ifExtVlanInterfaceIsLocalArp = _IfExtVlanInterfaceIsLocalArp_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 4, 1, 8),
    _IfExtVlanInterfaceIsLocalArp_Type()
)
ifExtVlanInterfaceIsLocalArp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifExtVlanInterfaceIsLocalArp.setStatus("current")
_IfExtVlanInterfaceStatus_Type = RowStatus
_IfExtVlanInterfaceStatus_Object = MibTableColumn
ifExtVlanInterfaceStatus = _IfExtVlanInterfaceStatus_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 4, 1, 9),
    _IfExtVlanInterfaceStatus_Type()
)
ifExtVlanInterfaceStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifExtVlanInterfaceStatus.setStatus("current")
_IfExtVlanInterfaceIpRouting_Type = ArubaEnableValue
_IfExtVlanInterfaceIpRouting_Object = MibTableColumn
ifExtVlanInterfaceIpRouting = _IfExtVlanInterfaceIpRouting_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 4, 1, 10),
    _IfExtVlanInterfaceIpRouting_Type()
)
ifExtVlanInterfaceIpRouting.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifExtVlanInterfaceIpRouting.setStatus("current")
_IfExtVlanInterfaceIpNatInside_Type = ArubaEnableValue
_IfExtVlanInterfaceIpNatInside_Object = MibTableColumn
ifExtVlanInterfaceIpNatInside = _IfExtVlanInterfaceIpNatInside_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 4, 1, 11),
    _IfExtVlanInterfaceIpNatInside_Type()
)
ifExtVlanInterfaceIpNatInside.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifExtVlanInterfaceIpNatInside.setStatus("current")
_IfExtVlanInterfaceIpIgmpSnooping_Type = ArubaEnableValue
_IfExtVlanInterfaceIpIgmpSnooping_Object = MibTableColumn
ifExtVlanInterfaceIpIgmpSnooping = _IfExtVlanInterfaceIpIgmpSnooping_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 4, 1, 12),
    _IfExtVlanInterfaceIpIgmpSnooping_Type()
)
ifExtVlanInterfaceIpIgmpSnooping.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifExtVlanInterfaceIpIgmpSnooping.setStatus("current")
_WlsxIfExtNPortTable_Object = MibTable
wlsxIfExtNPortTable = _WlsxIfExtNPortTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 5)
)
if mibBuilder.loadTexts:
    wlsxIfExtNPortTable.setStatus("current")
_WlsxIfExtNPortEntry_Object = MibTableRow
wlsxIfExtNPortEntry = _WlsxIfExtNPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 5, 1)
)
wlsxIfExtNPortEntry.setIndexNames(
    (0, "WLSX-IFEXT-MIB", "ifExtNSlotNumber"),
    (0, "WLSX-IFEXT-MIB", "ifExtNModuleNumber"),
    (0, "WLSX-IFEXT-MIB", "ifExtNPortNumber"),
)
if mibBuilder.loadTexts:
    wlsxIfExtNPortEntry.setStatus("current")
_IfExtNSlotNumber_Type = Integer32
_IfExtNSlotNumber_Object = MibTableColumn
ifExtNSlotNumber = _IfExtNSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 5, 1, 1),
    _IfExtNSlotNumber_Type()
)
ifExtNSlotNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ifExtNSlotNumber.setStatus("current")
_IfExtNModuleNumber_Type = Integer32
_IfExtNModuleNumber_Object = MibTableColumn
ifExtNModuleNumber = _IfExtNModuleNumber_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 5, 1, 2),
    _IfExtNModuleNumber_Type()
)
ifExtNModuleNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ifExtNModuleNumber.setStatus("current")
_IfExtNPortNumber_Type = Integer32
_IfExtNPortNumber_Object = MibTableColumn
ifExtNPortNumber = _IfExtNPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 5, 1, 3),
    _IfExtNPortNumber_Type()
)
ifExtNPortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ifExtNPortNumber.setStatus("current")
_IfExtNPortIfIndex_Type = Integer32
_IfExtNPortIfIndex_Object = MibTableColumn
ifExtNPortIfIndex = _IfExtNPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 5, 1, 4),
    _IfExtNPortIfIndex_Type()
)
ifExtNPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifExtNPortIfIndex.setStatus("current")
_IfExtNAdminState_Type = ArubaEnableValue
_IfExtNAdminState_Object = MibTableColumn
ifExtNAdminState = _IfExtNAdminState_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 5, 1, 5),
    _IfExtNAdminState_Type()
)
ifExtNAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifExtNAdminState.setStatus("current")


class _IfExtNOperState_Type(Integer32):
    """Custom type ifExtNOperState based on Integer32"""
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
          ("testing", 3),
          ("up", 1))
    )


_IfExtNOperState_Type.__name__ = "Integer32"
_IfExtNOperState_Object = MibTableColumn
ifExtNOperState = _IfExtNOperState_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 5, 1, 6),
    _IfExtNOperState_Type()
)
ifExtNOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifExtNOperState.setStatus("current")
_IfExtNPoeState_Type = ArubaPoeState
_IfExtNPoeState_Object = MibTableColumn
ifExtNPoeState = _IfExtNPoeState_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 5, 1, 7),
    _IfExtNPoeState_Type()
)
ifExtNPoeState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifExtNPoeState.setStatus("current")
_IfExtNIsTrusted_Type = TruthValue
_IfExtNIsTrusted_Object = MibTableColumn
ifExtNIsTrusted = _IfExtNIsTrusted_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 5, 1, 8),
    _IfExtNIsTrusted_Type()
)
ifExtNIsTrusted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifExtNIsTrusted.setStatus("current")
_IfExtNDot1DState_Type = ArubaDot1dState
_IfExtNDot1DState_Object = MibTableColumn
ifExtNDot1DState = _IfExtNDot1DState_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 5, 1, 9),
    _IfExtNDot1DState_Type()
)
ifExtNDot1DState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifExtNDot1DState.setStatus("current")
_IfExtNMode_Type = ArubaPortMode
_IfExtNMode_Object = MibTableColumn
ifExtNMode = _IfExtNMode_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 5, 1, 10),
    _IfExtNMode_Type()
)
ifExtNMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifExtNMode.setStatus("current")
_IfExtNAccessVlanId_Type = ArubaVlanValidRange
_IfExtNAccessVlanId_Object = MibTableColumn
ifExtNAccessVlanId = _IfExtNAccessVlanId_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 5, 1, 11),
    _IfExtNAccessVlanId_Type()
)
ifExtNAccessVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifExtNAccessVlanId.setStatus("current")
_IfExtNTrunkNativeVlanId_Type = ArubaVlanValidRange
_IfExtNTrunkNativeVlanId_Object = MibTableColumn
ifExtNTrunkNativeVlanId = _IfExtNTrunkNativeVlanId_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 5, 1, 12),
    _IfExtNTrunkNativeVlanId_Type()
)
ifExtNTrunkNativeVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifExtNTrunkNativeVlanId.setStatus("current")
_IfExtNTrunkIsAllowedAll_Type = TruthValue
_IfExtNTrunkIsAllowedAll_Object = MibTableColumn
ifExtNTrunkIsAllowedAll = _IfExtNTrunkIsAllowedAll_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 5, 1, 13),
    _IfExtNTrunkIsAllowedAll_Type()
)
ifExtNTrunkIsAllowedAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifExtNTrunkIsAllowedAll.setStatus("current")


class _IfExtNTrunkAllowedVlanList_Type(OctetString):
    """Custom type ifExtNTrunkAllowedVlanList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_IfExtNTrunkAllowedVlanList_Type.__name__ = "OctetString"
_IfExtNTrunkAllowedVlanList_Object = MibTableColumn
ifExtNTrunkAllowedVlanList = _IfExtNTrunkAllowedVlanList_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 5, 1, 14),
    _IfExtNTrunkAllowedVlanList_Type()
)
ifExtNTrunkAllowedVlanList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifExtNTrunkAllowedVlanList.setStatus("current")


class _IfExtNIngressACLName_Type(DisplayString):
    """Custom type ifExtNIngressACLName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_IfExtNIngressACLName_Type.__name__ = "DisplayString"
_IfExtNIngressACLName_Object = MibTableColumn
ifExtNIngressACLName = _IfExtNIngressACLName_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 5, 1, 15),
    _IfExtNIngressACLName_Type()
)
ifExtNIngressACLName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifExtNIngressACLName.setStatus("current")


class _IfExtNEgressACLName_Type(DisplayString):
    """Custom type ifExtNEgressACLName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_IfExtNEgressACLName_Type.__name__ = "DisplayString"
_IfExtNEgressACLName_Object = MibTableColumn
ifExtNEgressACLName = _IfExtNEgressACLName_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 5, 1, 16),
    _IfExtNEgressACLName_Type()
)
ifExtNEgressACLName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifExtNEgressACLName.setStatus("current")


class _IfExtNSessionACLName_Type(DisplayString):
    """Custom type ifExtNSessionACLName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_IfExtNSessionACLName_Type.__name__ = "DisplayString"
_IfExtNSessionACLName_Object = MibTableColumn
ifExtNSessionACLName = _IfExtNSessionACLName_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 5, 1, 17),
    _IfExtNSessionACLName_Type()
)
ifExtNSessionACLName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifExtNSessionACLName.setStatus("current")
_IfExtNXsecVlan_Type = ArubaVlanValidRange
_IfExtNXsecVlan_Object = MibTableColumn
ifExtNXsecVlan = _IfExtNXsecVlan_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 5, 1, 18),
    _IfExtNXsecVlan_Type()
)
ifExtNXsecVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifExtNXsecVlan.setStatus("current")
_IfExtNIsMonitoring_Type = TruthValue
_IfExtNIsMonitoring_Object = MibTableColumn
ifExtNIsMonitoring = _IfExtNIsMonitoring_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 5, 1, 19),
    _IfExtNIsMonitoring_Type()
)
ifExtNIsMonitoring.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifExtNIsMonitoring.setStatus("current")
_IfExtNIsMux_Type = TruthValue
_IfExtNIsMux_Object = MibTableColumn
ifExtNIsMux = _IfExtNIsMux_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 5, 1, 20),
    _IfExtNIsMux_Type()
)
ifExtNIsMux.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifExtNIsMux.setStatus("current")
_IfExtNPortSpeed_Type = ArubaPortSpeed
_IfExtNPortSpeed_Object = MibTableColumn
ifExtNPortSpeed = _IfExtNPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 5, 1, 21),
    _IfExtNPortSpeed_Type()
)
ifExtNPortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifExtNPortSpeed.setStatus("current")
_IfExtNPortDuplex_Type = ArubaPortDuplex
_IfExtNPortDuplex_Object = MibTableColumn
ifExtNPortDuplex = _IfExtNPortDuplex_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 5, 1, 22),
    _IfExtNPortDuplex_Type()
)
ifExtNPortDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifExtNPortDuplex.setStatus("current")
_IfExtNPortType_Type = ArubaPortType
_IfExtNPortType_Object = MibTableColumn
ifExtNPortType = _IfExtNPortType_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 5, 1, 23),
    _IfExtNPortType_Type()
)
ifExtNPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifExtNPortType.setStatus("current")
_IfExtNDescr_Type = DisplayString
_IfExtNDescr_Object = MibTableColumn
ifExtNDescr = _IfExtNDescr_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 5, 1, 24),
    _IfExtNDescr_Type()
)
ifExtNDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifExtNDescr.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WLSX-IFEXT-MIB",
    **{"wlsxIfExtMIB": wlsxIfExtMIB,
       "wlsxIfExtGroup": wlsxIfExtGroup,
       "wlsxIfExtPortTable": wlsxIfExtPortTable,
       "wlsxIfExtPortEntry": wlsxIfExtPortEntry,
       "ifExtSlotNumber": ifExtSlotNumber,
       "ifExtPortNumber": ifExtPortNumber,
       "ifExtPortIfIndex": ifExtPortIfIndex,
       "ifExtAdminState": ifExtAdminState,
       "ifExtOperState": ifExtOperState,
       "ifExtPoeState": ifExtPoeState,
       "ifExtIsTrusted": ifExtIsTrusted,
       "ifExtDot1DState": ifExtDot1DState,
       "ifExtMode": ifExtMode,
       "ifExtAccessVlanId": ifExtAccessVlanId,
       "ifExtTrunkNativeVlanId": ifExtTrunkNativeVlanId,
       "ifExtTrunkIsAllowedAll": ifExtTrunkIsAllowedAll,
       "ifExtTrunkAllowedVlanList": ifExtTrunkAllowedVlanList,
       "ifExtIngressACLName": ifExtIngressACLName,
       "ifExtEgressACLName": ifExtEgressACLName,
       "ifExtSessionACLName": ifExtSessionACLName,
       "ifExtXsecVlan": ifExtXsecVlan,
       "ifExtIsMonitoring": ifExtIsMonitoring,
       "ifExtIsMux": ifExtIsMux,
       "ifExtUserSlotNumber": ifExtUserSlotNumber,
       "ifExtUserPortNumber": ifExtUserPortNumber,
       "ifExtPortSpeed": ifExtPortSpeed,
       "ifExtPortDuplex": ifExtPortDuplex,
       "ifExtPortType": ifExtPortType,
       "ifExtDescr": ifExtDescr,
       "ifExtUserModuleNumber": ifExtUserModuleNumber,
       "wlsxIfExtVlanTable": wlsxIfExtVlanTable,
       "wlsxIfExtVlanEntry": wlsxIfExtVlanEntry,
       "ifExtVlanId": ifExtVlanId,
       "ifExtVlanName": ifExtVlanName,
       "ifExtVlanStatus": ifExtVlanStatus,
       "wlsxIfExtVlanMemberTable": wlsxIfExtVlanMemberTable,
       "wlsxIfExtVlanMemberEntry": wlsxIfExtVlanMemberEntry,
       "ifExtVlanMemberStatus": ifExtVlanMemberStatus,
       "ifExtVlanMemberSlot": ifExtVlanMemberSlot,
       "ifExtVlanMemberPort": ifExtVlanMemberPort,
       "ifExtVlanMemberType": ifExtVlanMemberType,
       "wlsxIfExtVlanInterfaceTable": wlsxIfExtVlanInterfaceTable,
       "wlsxIfExtVlanInterfaceEntry": wlsxIfExtVlanInterfaceEntry,
       "ifExtVlanInterfaceIfIndex": ifExtVlanInterfaceIfIndex,
       "ifExtVlanInterfaceDescription": ifExtVlanInterfaceDescription,
       "ifExtVlanInterfaceBWContract": ifExtVlanInterfaceBWContract,
       "ifExtVlanInterfaceAdminState": ifExtVlanInterfaceAdminState,
       "ifExtVlanInterfaceOperState": ifExtVlanInterfaceOperState,
       "ifExtVlanInterfaceIpAddress": ifExtVlanInterfaceIpAddress,
       "ifExtVlanInterfaceIpMask": ifExtVlanInterfaceIpMask,
       "ifExtVlanInterfaceIsLocalArp": ifExtVlanInterfaceIsLocalArp,
       "ifExtVlanInterfaceStatus": ifExtVlanInterfaceStatus,
       "ifExtVlanInterfaceIpRouting": ifExtVlanInterfaceIpRouting,
       "ifExtVlanInterfaceIpNatInside": ifExtVlanInterfaceIpNatInside,
       "ifExtVlanInterfaceIpIgmpSnooping": ifExtVlanInterfaceIpIgmpSnooping,
       "wlsxIfExtNPortTable": wlsxIfExtNPortTable,
       "wlsxIfExtNPortEntry": wlsxIfExtNPortEntry,
       "ifExtNSlotNumber": ifExtNSlotNumber,
       "ifExtNModuleNumber": ifExtNModuleNumber,
       "ifExtNPortNumber": ifExtNPortNumber,
       "ifExtNPortIfIndex": ifExtNPortIfIndex,
       "ifExtNAdminState": ifExtNAdminState,
       "ifExtNOperState": ifExtNOperState,
       "ifExtNPoeState": ifExtNPoeState,
       "ifExtNIsTrusted": ifExtNIsTrusted,
       "ifExtNDot1DState": ifExtNDot1DState,
       "ifExtNMode": ifExtNMode,
       "ifExtNAccessVlanId": ifExtNAccessVlanId,
       "ifExtNTrunkNativeVlanId": ifExtNTrunkNativeVlanId,
       "ifExtNTrunkIsAllowedAll": ifExtNTrunkIsAllowedAll,
       "ifExtNTrunkAllowedVlanList": ifExtNTrunkAllowedVlanList,
       "ifExtNIngressACLName": ifExtNIngressACLName,
       "ifExtNEgressACLName": ifExtNEgressACLName,
       "ifExtNSessionACLName": ifExtNSessionACLName,
       "ifExtNXsecVlan": ifExtNXsecVlan,
       "ifExtNIsMonitoring": ifExtNIsMonitoring,
       "ifExtNIsMux": ifExtNIsMux,
       "ifExtNPortSpeed": ifExtNPortSpeed,
       "ifExtNPortDuplex": ifExtNPortDuplex,
       "ifExtNPortType": ifExtNPortType,
       "ifExtNDescr": ifExtNDescr}
)
