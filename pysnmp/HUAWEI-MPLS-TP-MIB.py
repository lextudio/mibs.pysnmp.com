# SNMP MIB module (HUAWEI-MPLS-TP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-MPLS-TP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:05:09 2024
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

(hwDatacomm,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "hwDatacomm")

(ifIndex,
 ifName) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex",
    "ifName")

(MplsExtendedTunnelId,
 MplsTunnelIndex,
 MplsTunnelInstanceIndex) = mibBuilder.importSymbols(
    "MPLS-TC-STD-MIB",
    "MplsExtendedTunnelId",
    "MplsTunnelIndex",
    "MplsTunnelInstanceIndex")

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
 Bits,
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

hwMplsTpMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 305)
)
hwMplsTpMib.setRevisions(
        ("2012-03-20 10:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwMplsTpObjects_ObjectIdentity = ObjectIdentity
hwMplsTpObjects = _HwMplsTpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 305, 1)
)
_HwMplsTpTables_ObjectIdentity = ObjectIdentity
hwMplsTpTables = _HwMplsTpTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 305, 1, 1)
)
_HwMplsTpTunnelTable_Object = MibTable
hwMplsTpTunnelTable = _HwMplsTpTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 305, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hwMplsTpTunnelTable.setStatus("current")
_HwMplsTpTunnelEntry_Object = MibTableRow
hwMplsTpTunnelEntry = _HwMplsTpTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 305, 1, 1, 1, 1)
)
hwMplsTpTunnelEntry.setIndexNames(
    (0, "HUAWEI-MPLS-TP-MIB", "hwMplsTpTunnelIngressIndex"),
    (0, "HUAWEI-MPLS-TP-MIB", "hwMplsTpTunnelIngressLSRId"),
    (0, "HUAWEI-MPLS-TP-MIB", "hwMplsTpIngressGlobalId"),
    (0, "HUAWEI-MPLS-TP-MIB", "hwMplsTpTunnelEgressIndex"),
    (0, "HUAWEI-MPLS-TP-MIB", "hwMplsTpTunnelEgressLSRId"),
    (0, "HUAWEI-MPLS-TP-MIB", "hwMplsTpEgressGlobalId"),
)
if mibBuilder.loadTexts:
    hwMplsTpTunnelEntry.setStatus("current")
_HwMplsTpTunnelIngressIndex_Type = MplsTunnelIndex
_HwMplsTpTunnelIngressIndex_Object = MibTableColumn
hwMplsTpTunnelIngressIndex = _HwMplsTpTunnelIngressIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 305, 1, 1, 1, 1, 1),
    _HwMplsTpTunnelIngressIndex_Type()
)
hwMplsTpTunnelIngressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMplsTpTunnelIngressIndex.setStatus("current")
_HwMplsTpTunnelIngressLSRId_Type = MplsExtendedTunnelId
_HwMplsTpTunnelIngressLSRId_Object = MibTableColumn
hwMplsTpTunnelIngressLSRId = _HwMplsTpTunnelIngressLSRId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 305, 1, 1, 1, 1, 2),
    _HwMplsTpTunnelIngressLSRId_Type()
)
hwMplsTpTunnelIngressLSRId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMplsTpTunnelIngressLSRId.setStatus("current")


class _HwMplsTpIngressGlobalId_Type(Integer32):
    """Custom type hwMplsTpIngressGlobalId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_HwMplsTpIngressGlobalId_Type.__name__ = "Integer32"
_HwMplsTpIngressGlobalId_Object = MibTableColumn
hwMplsTpIngressGlobalId = _HwMplsTpIngressGlobalId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 305, 1, 1, 1, 1, 3),
    _HwMplsTpIngressGlobalId_Type()
)
hwMplsTpIngressGlobalId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMplsTpIngressGlobalId.setStatus("current")
_HwMplsTpTunnelEgressIndex_Type = MplsTunnelIndex
_HwMplsTpTunnelEgressIndex_Object = MibTableColumn
hwMplsTpTunnelEgressIndex = _HwMplsTpTunnelEgressIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 305, 1, 1, 1, 1, 4),
    _HwMplsTpTunnelEgressIndex_Type()
)
hwMplsTpTunnelEgressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMplsTpTunnelEgressIndex.setStatus("current")
_HwMplsTpTunnelEgressLSRId_Type = MplsExtendedTunnelId
_HwMplsTpTunnelEgressLSRId_Object = MibTableColumn
hwMplsTpTunnelEgressLSRId = _HwMplsTpTunnelEgressLSRId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 305, 1, 1, 1, 1, 5),
    _HwMplsTpTunnelEgressLSRId_Type()
)
hwMplsTpTunnelEgressLSRId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMplsTpTunnelEgressLSRId.setStatus("current")


class _HwMplsTpEgressGlobalId_Type(Integer32):
    """Custom type hwMplsTpEgressGlobalId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_HwMplsTpEgressGlobalId_Type.__name__ = "Integer32"
_HwMplsTpEgressGlobalId_Object = MibTableColumn
hwMplsTpEgressGlobalId = _HwMplsTpEgressGlobalId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 305, 1, 1, 1, 1, 6),
    _HwMplsTpEgressGlobalId_Type()
)
hwMplsTpEgressGlobalId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMplsTpEgressGlobalId.setStatus("current")
_HwMplsTpTunnelIfName_Type = SnmpAdminString
_HwMplsTpTunnelIfName_Object = MibTableColumn
hwMplsTpTunnelIfName = _HwMplsTpTunnelIfName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 305, 1, 1, 1, 1, 7),
    _HwMplsTpTunnelIfName_Type()
)
hwMplsTpTunnelIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsTpTunnelIfName.setStatus("current")


class _HwMplsTpTunnelAdminStatus_Type(Integer32):
    """Custom type hwMplsTpTunnelAdminStatus based on Integer32"""
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


_HwMplsTpTunnelAdminStatus_Type.__name__ = "Integer32"
_HwMplsTpTunnelAdminStatus_Object = MibTableColumn
hwMplsTpTunnelAdminStatus = _HwMplsTpTunnelAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 305, 1, 1, 1, 1, 8),
    _HwMplsTpTunnelAdminStatus_Type()
)
hwMplsTpTunnelAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsTpTunnelAdminStatus.setStatus("current")


class _HwMplsTpTunnelOperStatus_Type(Integer32):
    """Custom type hwMplsTpTunnelOperStatus based on Integer32"""
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
        *(("dormant", 5),
          ("down", 2),
          ("lowerLayerDown", 7),
          ("notPresent", 6),
          ("testing", 3),
          ("unknown", 4),
          ("up", 1))
    )


_HwMplsTpTunnelOperStatus_Type.__name__ = "Integer32"
_HwMplsTpTunnelOperStatus_Object = MibTableColumn
hwMplsTpTunnelOperStatus = _HwMplsTpTunnelOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 305, 1, 1, 1, 1, 9),
    _HwMplsTpTunnelOperStatus_Type()
)
hwMplsTpTunnelOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsTpTunnelOperStatus.setStatus("current")
_HwMplsTpLspTable_Object = MibTable
hwMplsTpLspTable = _HwMplsTpLspTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 305, 1, 1, 2)
)
if mibBuilder.loadTexts:
    hwMplsTpLspTable.setStatus("current")
_HwMplsTpLspEntry_Object = MibTableRow
hwMplsTpLspEntry = _HwMplsTpLspEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 305, 1, 1, 2, 1)
)
hwMplsTpLspEntry.setIndexNames(
    (0, "HUAWEI-MPLS-TP-MIB", "hwMplsTpTunnelIngressIndex"),
    (0, "HUAWEI-MPLS-TP-MIB", "hwMplsTpTunnelIngressInstance"),
    (0, "HUAWEI-MPLS-TP-MIB", "hwMplsTpTunnelIngressLSRId"),
    (0, "HUAWEI-MPLS-TP-MIB", "hwMplsTpIngressGlobalId"),
    (0, "HUAWEI-MPLS-TP-MIB", "hwMplsTpTunnelEgressIndex"),
    (0, "HUAWEI-MPLS-TP-MIB", "hwMplsTpTunnelEgressInstance"),
    (0, "HUAWEI-MPLS-TP-MIB", "hwMplsTpTunnelEgressLSRId"),
    (0, "HUAWEI-MPLS-TP-MIB", "hwMplsTpEgressGlobalId"),
)
if mibBuilder.loadTexts:
    hwMplsTpLspEntry.setStatus("current")
_HwMplsTpTunnelIngressInstance_Type = MplsTunnelInstanceIndex
_HwMplsTpTunnelIngressInstance_Object = MibTableColumn
hwMplsTpTunnelIngressInstance = _HwMplsTpTunnelIngressInstance_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 305, 1, 1, 2, 1, 1),
    _HwMplsTpTunnelIngressInstance_Type()
)
hwMplsTpTunnelIngressInstance.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwMplsTpTunnelIngressInstance.setStatus("current")
_HwMplsTpTunnelEgressInstance_Type = MplsTunnelInstanceIndex
_HwMplsTpTunnelEgressInstance_Object = MibTableColumn
hwMplsTpTunnelEgressInstance = _HwMplsTpTunnelEgressInstance_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 305, 1, 1, 2, 1, 2),
    _HwMplsTpTunnelEgressInstance_Type()
)
hwMplsTpTunnelEgressInstance.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwMplsTpTunnelEgressInstance.setStatus("current")


class _HwMplsTpLspType_Type(Integer32):
    """Custom type hwMplsTpLspType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("protection", 1),
          ("working", 2))
    )


_HwMplsTpLspType_Type.__name__ = "Integer32"
_HwMplsTpLspType_Object = MibTableColumn
hwMplsTpLspType = _HwMplsTpLspType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 305, 1, 1, 2, 1, 3),
    _HwMplsTpLspType_Type()
)
hwMplsTpLspType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwMplsTpLspType.setStatus("current")
_HwMplsTpGlobalObjects_ObjectIdentity = ObjectIdentity
hwMplsTpGlobalObjects = _HwMplsTpGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 305, 1, 2)
)
_HwMplsTpNotifications_ObjectIdentity = ObjectIdentity
hwMplsTpNotifications = _HwMplsTpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 305, 2)
)
_HwMplsTpTrapObjects_ObjectIdentity = ObjectIdentity
hwMplsTpTrapObjects = _HwMplsTpTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 305, 2, 1)
)
_HwMplsTpTunnelTrap_ObjectIdentity = ObjectIdentity
hwMplsTpTunnelTrap = _HwMplsTpTunnelTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 305, 2, 2)
)
_HwMplsTpLspTrap_ObjectIdentity = ObjectIdentity
hwMplsTpLspTrap = _HwMplsTpLspTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 305, 2, 3)
)
_HwMplsTpConformance_ObjectIdentity = ObjectIdentity
hwMplsTpConformance = _HwMplsTpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 305, 3)
)
_HwMplsTpCompliances_ObjectIdentity = ObjectIdentity
hwMplsTpCompliances = _HwMplsTpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 305, 3, 1)
)
_HwMplsTpGroups_ObjectIdentity = ObjectIdentity
hwMplsTpGroups = _HwMplsTpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 305, 3, 2)
)

# Managed Objects groups

hwMplsTPGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 305, 3, 2, 1)
)
hwMplsTPGeneralGroup.setObjects(
      *(("HUAWEI-MPLS-TP-MIB", "hwMplsTpTunnelIfName"),
        ("HUAWEI-MPLS-TP-MIB", "hwMplsTpTunnelAdminStatus"),
        ("HUAWEI-MPLS-TP-MIB", "hwMplsTpTunnelOperStatus"),
        ("HUAWEI-MPLS-TP-MIB", "hwMplsTpTunnelIngressInstance"),
        ("HUAWEI-MPLS-TP-MIB", "hwMplsTpTunnelEgressInstance"),
        ("HUAWEI-MPLS-TP-MIB", "hwMplsTpLspType"))
)
if mibBuilder.loadTexts:
    hwMplsTPGeneralGroup.setStatus("current")


# Notification objects

hwMplsTpTunnelDownClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 305, 2, 2, 1)
)
hwMplsTpTunnelDownClear.setObjects(
      *(("HUAWEI-MPLS-TP-MIB", "hwMplsTpTunnelIfName"),
        ("HUAWEI-MPLS-TP-MIB", "hwMplsTpTunnelAdminStatus"),
        ("HUAWEI-MPLS-TP-MIB", "hwMplsTpTunnelOperStatus"),
        ("IF-MIB", "ifName"))
)
if mibBuilder.loadTexts:
    hwMplsTpTunnelDownClear.setStatus(
        "current"
    )

hwMplsTpTunnelDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 305, 2, 2, 2)
)
hwMplsTpTunnelDown.setObjects(
      *(("HUAWEI-MPLS-TP-MIB", "hwMplsTpTunnelIfName"),
        ("HUAWEI-MPLS-TP-MIB", "hwMplsTpTunnelAdminStatus"),
        ("HUAWEI-MPLS-TP-MIB", "hwMplsTpTunnelOperStatus"),
        ("IF-MIB", "ifName"))
)
if mibBuilder.loadTexts:
    hwMplsTpTunnelDown.setStatus(
        "current"
    )

hwMplsTpTunnelResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 305, 2, 2, 3)
)
hwMplsTpTunnelResume.setObjects(
    ("HUAWEI-MPLS-TP-MIB", "hwMplsTpTunnelIfName")
)
if mibBuilder.loadTexts:
    hwMplsTpTunnelResume.setStatus(
        "current"
    )

hwMplsTpTunnelSwitch = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 305, 2, 2, 4)
)
hwMplsTpTunnelSwitch.setObjects(
    ("HUAWEI-MPLS-TP-MIB", "hwMplsTpTunnelIfName")
)
if mibBuilder.loadTexts:
    hwMplsTpTunnelSwitch.setStatus(
        "current"
    )

hwMplsTpLspOamDlocClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 305, 2, 3, 1)
)
hwMplsTpLspOamDlocClear.setObjects(
      *(("HUAWEI-MPLS-TP-MIB", "hwMplsTpTunnelIfName"),
        ("HUAWEI-MPLS-TP-MIB", "hwMplsTpLspType"),
        ("IF-MIB", "ifName"))
)
if mibBuilder.loadTexts:
    hwMplsTpLspOamDlocClear.setStatus(
        "current"
    )

hwMplsTpLspOamDloc = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 305, 2, 3, 2)
)
hwMplsTpLspOamDloc.setObjects(
      *(("HUAWEI-MPLS-TP-MIB", "hwMplsTpTunnelIfName"),
        ("HUAWEI-MPLS-TP-MIB", "hwMplsTpLspType"),
        ("IF-MIB", "ifName"))
)
if mibBuilder.loadTexts:
    hwMplsTpLspOamDloc.setStatus(
        "current"
    )

hwMplsTpLspOamRdiClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 305, 2, 3, 3)
)
hwMplsTpLspOamRdiClear.setObjects(
      *(("HUAWEI-MPLS-TP-MIB", "hwMplsTpTunnelIfName"),
        ("HUAWEI-MPLS-TP-MIB", "hwMplsTpLspType"),
        ("IF-MIB", "ifName"))
)
if mibBuilder.loadTexts:
    hwMplsTpLspOamRdiClear.setStatus(
        "current"
    )

hwMplsTpLspOamRdi = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 305, 2, 3, 4)
)
hwMplsTpLspOamRdi.setObjects(
      *(("HUAWEI-MPLS-TP-MIB", "hwMplsTpTunnelIfName"),
        ("HUAWEI-MPLS-TP-MIB", "hwMplsTpLspType"),
        ("IF-MIB", "ifName"))
)
if mibBuilder.loadTexts:
    hwMplsTpLspOamRdi.setStatus(
        "current"
    )

hwMplsTpLspOamMisconnectionEncapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 305, 2, 3, 5)
)
hwMplsTpLspOamMisconnectionEncapClear.setObjects(
      *(("HUAWEI-MPLS-TP-MIB", "hwMplsTpTunnelIfName"),
        ("HUAWEI-MPLS-TP-MIB", "hwMplsTpLspType"))
)
if mibBuilder.loadTexts:
    hwMplsTpLspOamMisconnectionEncapClear.setStatus(
        "current"
    )

hwMplsTpLspOamMisconnectionEncap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 305, 2, 3, 6)
)
hwMplsTpLspOamMisconnectionEncap.setObjects(
      *(("HUAWEI-MPLS-TP-MIB", "hwMplsTpTunnelIfName"),
        ("HUAWEI-MPLS-TP-MIB", "hwMplsTpLspType"))
)
if mibBuilder.loadTexts:
    hwMplsTpLspOamMisconnectionEncap.setStatus(
        "current"
    )

hwMplsTpLspOamMisconnectionDiscrClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 305, 2, 3, 7)
)
hwMplsTpLspOamMisconnectionDiscrClear.setObjects(
      *(("HUAWEI-MPLS-TP-MIB", "hwMplsTpTunnelIfName"),
        ("HUAWEI-MPLS-TP-MIB", "hwMplsTpLspType"))
)
if mibBuilder.loadTexts:
    hwMplsTpLspOamMisconnectionDiscrClear.setStatus(
        "current"
    )

hwMplsTpLspOamMisconnectionDiscr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 305, 2, 3, 8)
)
hwMplsTpLspOamMisconnectionDiscr.setObjects(
      *(("HUAWEI-MPLS-TP-MIB", "hwMplsTpTunnelIfName"),
        ("HUAWEI-MPLS-TP-MIB", "hwMplsTpLspType"))
)
if mibBuilder.loadTexts:
    hwMplsTpLspOamMisconnectionDiscr.setStatus(
        "current"
    )

hwMplsTpLspOamMisconnectionMEPClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 305, 2, 3, 9)
)
hwMplsTpLspOamMisconnectionMEPClear.setObjects(
      *(("HUAWEI-MPLS-TP-MIB", "hwMplsTpTunnelIfName"),
        ("HUAWEI-MPLS-TP-MIB", "hwMplsTpLspType"))
)
if mibBuilder.loadTexts:
    hwMplsTpLspOamMisconnectionMEPClear.setStatus(
        "current"
    )

hwMplsTpLspOamMisconnectionMEP = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 305, 2, 3, 10)
)
hwMplsTpLspOamMisconnectionMEP.setObjects(
      *(("HUAWEI-MPLS-TP-MIB", "hwMplsTpTunnelIfName"),
        ("HUAWEI-MPLS-TP-MIB", "hwMplsTpLspType"))
)
if mibBuilder.loadTexts:
    hwMplsTpLspOamMisconnectionMEP.setStatus(
        "current"
    )

hwMplsTpLspOamMisconnectionSECClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 305, 2, 3, 11)
)
hwMplsTpLspOamMisconnectionSECClear.setObjects(
      *(("HUAWEI-MPLS-TP-MIB", "hwMplsTpTunnelIfName"),
        ("HUAWEI-MPLS-TP-MIB", "hwMplsTpLspType"))
)
if mibBuilder.loadTexts:
    hwMplsTpLspOamMisconnectionSECClear.setStatus(
        "current"
    )

hwMplsTpLspOamMisconnectionSEC = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 305, 2, 3, 12)
)
hwMplsTpLspOamMisconnectionSEC.setObjects(
      *(("HUAWEI-MPLS-TP-MIB", "hwMplsTpTunnelIfName"),
        ("HUAWEI-MPLS-TP-MIB", "hwMplsTpLspType"))
)
if mibBuilder.loadTexts:
    hwMplsTpLspOamMisconnectionSEC.setStatus(
        "current"
    )


# Notifications groups

hwMplsTPNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 305, 3, 2, 2)
)
hwMplsTPNotificationGroup.setObjects(
      *(("HUAWEI-MPLS-TP-MIB", "hwMplsTpTunnelDownClear"),
        ("HUAWEI-MPLS-TP-MIB", "hwMplsTpTunnelDown"),
        ("HUAWEI-MPLS-TP-MIB", "hwMplsTpTunnelResume"),
        ("HUAWEI-MPLS-TP-MIB", "hwMplsTpTunnelSwitch"),
        ("HUAWEI-MPLS-TP-MIB", "hwMplsTpLspOamDlocClear"),
        ("HUAWEI-MPLS-TP-MIB", "hwMplsTpLspOamDloc"),
        ("HUAWEI-MPLS-TP-MIB", "hwMplsTpLspOamRdiClear"),
        ("HUAWEI-MPLS-TP-MIB", "hwMplsTpLspOamRdi"),
        ("HUAWEI-MPLS-TP-MIB", "hwMplsTpLspOamMisconnectionEncapClear"),
        ("HUAWEI-MPLS-TP-MIB", "hwMplsTpLspOamMisconnectionEncap"),
        ("HUAWEI-MPLS-TP-MIB", "hwMplsTpLspOamMisconnectionDiscrClear"),
        ("HUAWEI-MPLS-TP-MIB", "hwMplsTpLspOamMisconnectionDiscr"),
        ("HUAWEI-MPLS-TP-MIB", "hwMplsTpLspOamMisconnectionMEPClear"),
        ("HUAWEI-MPLS-TP-MIB", "hwMplsTpLspOamMisconnectionMEP"),
        ("HUAWEI-MPLS-TP-MIB", "hwMplsTpLspOamMisconnectionSECClear"),
        ("HUAWEI-MPLS-TP-MIB", "hwMplsTpLspOamMisconnectionSEC"))
)
if mibBuilder.loadTexts:
    hwMplsTPNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hwMplsTpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 305, 3, 1, 1)
)
if mibBuilder.loadTexts:
    hwMplsTpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-MPLS-TP-MIB",
    **{"hwMplsTpMib": hwMplsTpMib,
       "hwMplsTpObjects": hwMplsTpObjects,
       "hwMplsTpTables": hwMplsTpTables,
       "hwMplsTpTunnelTable": hwMplsTpTunnelTable,
       "hwMplsTpTunnelEntry": hwMplsTpTunnelEntry,
       "hwMplsTpTunnelIngressIndex": hwMplsTpTunnelIngressIndex,
       "hwMplsTpTunnelIngressLSRId": hwMplsTpTunnelIngressLSRId,
       "hwMplsTpIngressGlobalId": hwMplsTpIngressGlobalId,
       "hwMplsTpTunnelEgressIndex": hwMplsTpTunnelEgressIndex,
       "hwMplsTpTunnelEgressLSRId": hwMplsTpTunnelEgressLSRId,
       "hwMplsTpEgressGlobalId": hwMplsTpEgressGlobalId,
       "hwMplsTpTunnelIfName": hwMplsTpTunnelIfName,
       "hwMplsTpTunnelAdminStatus": hwMplsTpTunnelAdminStatus,
       "hwMplsTpTunnelOperStatus": hwMplsTpTunnelOperStatus,
       "hwMplsTpLspTable": hwMplsTpLspTable,
       "hwMplsTpLspEntry": hwMplsTpLspEntry,
       "hwMplsTpTunnelIngressInstance": hwMplsTpTunnelIngressInstance,
       "hwMplsTpTunnelEgressInstance": hwMplsTpTunnelEgressInstance,
       "hwMplsTpLspType": hwMplsTpLspType,
       "hwMplsTpGlobalObjects": hwMplsTpGlobalObjects,
       "hwMplsTpNotifications": hwMplsTpNotifications,
       "hwMplsTpTrapObjects": hwMplsTpTrapObjects,
       "hwMplsTpTunnelTrap": hwMplsTpTunnelTrap,
       "hwMplsTpTunnelDownClear": hwMplsTpTunnelDownClear,
       "hwMplsTpTunnelDown": hwMplsTpTunnelDown,
       "hwMplsTpTunnelResume": hwMplsTpTunnelResume,
       "hwMplsTpTunnelSwitch": hwMplsTpTunnelSwitch,
       "hwMplsTpLspTrap": hwMplsTpLspTrap,
       "hwMplsTpLspOamDlocClear": hwMplsTpLspOamDlocClear,
       "hwMplsTpLspOamDloc": hwMplsTpLspOamDloc,
       "hwMplsTpLspOamRdiClear": hwMplsTpLspOamRdiClear,
       "hwMplsTpLspOamRdi": hwMplsTpLspOamRdi,
       "hwMplsTpLspOamMisconnectionEncapClear": hwMplsTpLspOamMisconnectionEncapClear,
       "hwMplsTpLspOamMisconnectionEncap": hwMplsTpLspOamMisconnectionEncap,
       "hwMplsTpLspOamMisconnectionDiscrClear": hwMplsTpLspOamMisconnectionDiscrClear,
       "hwMplsTpLspOamMisconnectionDiscr": hwMplsTpLspOamMisconnectionDiscr,
       "hwMplsTpLspOamMisconnectionMEPClear": hwMplsTpLspOamMisconnectionMEPClear,
       "hwMplsTpLspOamMisconnectionMEP": hwMplsTpLspOamMisconnectionMEP,
       "hwMplsTpLspOamMisconnectionSECClear": hwMplsTpLspOamMisconnectionSECClear,
       "hwMplsTpLspOamMisconnectionSEC": hwMplsTpLspOamMisconnectionSEC,
       "hwMplsTpConformance": hwMplsTpConformance,
       "hwMplsTpCompliances": hwMplsTpCompliances,
       "hwMplsTpCompliance": hwMplsTpCompliance,
       "hwMplsTpGroups": hwMplsTpGroups,
       "hwMplsTPGeneralGroup": hwMplsTPGeneralGroup,
       "hwMplsTPNotificationGroup": hwMplsTPNotificationGroup}
)
