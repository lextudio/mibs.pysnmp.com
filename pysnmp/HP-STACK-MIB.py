# SNMP MIB module (HP-STACK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HP-STACK-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:58:59 2024
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

(hpSwitch,) = mibBuilder.importSymbols(
    "HP-ICF-OID",
    "hpSwitch")

(hpSwitchBaseMACAddress,) = mibBuilder.importSymbols(
    "NETSWITCH-MIB",
    "hpSwitchBaseMACAddress")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hpStackMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 69)
)
hpStackMIB.setRevisions(
        ("2010-01-03 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpStackNotifications_ObjectIdentity = ObjectIdentity
hpStackNotifications = _HpStackNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 69, 0)
)
_HpStackObjects_ObjectIdentity = ObjectIdentity
hpStackObjects = _HpStackObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 69, 1)
)
_HpStackConfig_ObjectIdentity = ObjectIdentity
hpStackConfig = _HpStackConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 69, 1, 1)
)


class _HpStackId_Type(OctetString):
    """Custom type hpStackId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_HpStackId_Type.__name__ = "OctetString"
_HpStackId_Object = MibScalar
hpStackId = _HpStackId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 69, 1, 1, 1),
    _HpStackId_Type()
)
hpStackId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpStackId.setStatus("current")


class _HpStackOperStatus_Type(Integer32):
    """Custom type hpStackOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("disabled", 1),
          ("fragmentActive", 4),
          ("fragmentInactive", 3),
          ("unAvailable", 0))
    )


_HpStackOperStatus_Type.__name__ = "Integer32"
_HpStackOperStatus_Object = MibScalar
hpStackOperStatus = _HpStackOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 69, 1, 1, 2),
    _HpStackOperStatus_Type()
)
hpStackOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpStackOperStatus.setStatus("current")
_HpStackSetStacking_Type = TruthValue
_HpStackSetStacking_Object = MibScalar
hpStackSetStacking = _HpStackSetStacking_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 69, 1, 1, 3),
    _HpStackSetStacking_Type()
)
hpStackSetStacking.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpStackSetStacking.setStatus("current")


class _HpStackTopology_Type(Integer32):
    """Custom type hpStackTopology based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("chain", 1),
          ("mesh", 3),
          ("partialMesh", 4),
          ("ring", 2),
          ("unKnown", 0))
    )


_HpStackTopology_Type.__name__ = "Integer32"
_HpStackTopology_Object = MibScalar
hpStackTopology = _HpStackTopology_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 69, 1, 1, 4),
    _HpStackTopology_Type()
)
hpStackTopology.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpStackTopology.setStatus("current")


class _HpStackTrapEnable_Type(Integer32):
    """Custom type hpStackTrapEnable based on Integer32"""
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


_HpStackTrapEnable_Type.__name__ = "Integer32"
_HpStackTrapEnable_Object = MibScalar
hpStackTrapEnable = _HpStackTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 69, 1, 1, 5),
    _HpStackTrapEnable_Type()
)
hpStackTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpStackTrapEnable.setStatus("current")


class _HpStackSplitPolicy_Type(Integer32):
    """Custom type hpStackSplitPolicy based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allFragmentsUp", 2),
          ("oneFragmentUp", 1))
    )


_HpStackSplitPolicy_Type.__name__ = "Integer32"
_HpStackSplitPolicy_Object = MibScalar
hpStackSplitPolicy = _HpStackSplitPolicy_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 69, 1, 1, 6),
    _HpStackSplitPolicy_Type()
)
hpStackSplitPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpStackSplitPolicy.setStatus("current")
_HpStackConfigTable_Object = MibTable
hpStackConfigTable = _HpStackConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 69, 1, 2)
)
if mibBuilder.loadTexts:
    hpStackConfigTable.setStatus("current")
_HpStackConfigEntry_Object = MibTableRow
hpStackConfigEntry = _HpStackConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 69, 1, 2, 1)
)
hpStackConfigEntry.setIndexNames(
    (0, "HP-STACK-MIB", "hpStackSequenceNum"),
)
if mibBuilder.loadTexts:
    hpStackConfigEntry.setStatus("current")


class _HpStackSequenceNum_Type(Integer32):
    """Custom type hpStackSequenceNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_HpStackSequenceNum_Type.__name__ = "Integer32"
_HpStackSequenceNum_Object = MibTableColumn
hpStackSequenceNum = _HpStackSequenceNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 69, 1, 2, 1, 1),
    _HpStackSequenceNum_Type()
)
hpStackSequenceNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpStackSequenceNum.setStatus("current")


class _HpStackSwitchAdminStatus_Type(Integer32):
    """Custom type hpStackSwitchAdminStatus based on Integer32"""
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


_HpStackSwitchAdminStatus_Type.__name__ = "Integer32"
_HpStackSwitchAdminStatus_Object = MibTableColumn
hpStackSwitchAdminStatus = _HpStackSwitchAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 69, 1, 2, 1, 2),
    _HpStackSwitchAdminStatus_Type()
)
hpStackSwitchAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpStackSwitchAdminStatus.setStatus("current")


class _HpStackSwitchPreferredPriority_Type(Integer32):
    """Custom type hpStackSwitchPreferredPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_HpStackSwitchPreferredPriority_Type.__name__ = "Integer32"
_HpStackSwitchPreferredPriority_Object = MibTableColumn
hpStackSwitchPreferredPriority = _HpStackSwitchPreferredPriority_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 69, 1, 2, 1, 3),
    _HpStackSwitchPreferredPriority_Type()
)
hpStackSwitchPreferredPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpStackSwitchPreferredPriority.setStatus("current")


class _HpStackSwitchPreferredMemberId_Type(Integer32):
    """Custom type hpStackSwitchPreferredMemberId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpStackSwitchPreferredMemberId_Type.__name__ = "Integer32"
_HpStackSwitchPreferredMemberId_Object = MibTableColumn
hpStackSwitchPreferredMemberId = _HpStackSwitchPreferredMemberId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 69, 1, 2, 1, 4),
    _HpStackSwitchPreferredMemberId_Type()
)
hpStackSwitchPreferredMemberId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpStackSwitchPreferredMemberId.setStatus("current")
_HpStackMemberTable_Object = MibTable
hpStackMemberTable = _HpStackMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 69, 1, 3)
)
if mibBuilder.loadTexts:
    hpStackMemberTable.setStatus("current")
_HpStackMemberEntry_Object = MibTableRow
hpStackMemberEntry = _HpStackMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 69, 1, 3, 1)
)
hpStackMemberEntry.setIndexNames(
    (0, "HP-STACK-MIB", "hpStackMemberId"),
)
if mibBuilder.loadTexts:
    hpStackMemberEntry.setStatus("current")


class _HpStackMemberId_Type(Integer32):
    """Custom type hpStackMemberId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpStackMemberId_Type.__name__ = "Integer32"
_HpStackMemberId_Object = MibTableColumn
hpStackMemberId = _HpStackMemberId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 69, 1, 3, 1, 1),
    _HpStackMemberId_Type()
)
hpStackMemberId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpStackMemberId.setStatus("current")
_HpStackMemberProductId_Type = DisplayString
_HpStackMemberProductId_Object = MibTableColumn
hpStackMemberProductId = _HpStackMemberProductId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 69, 1, 3, 1, 2),
    _HpStackMemberProductId_Type()
)
hpStackMemberProductId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpStackMemberProductId.setStatus("current")


class _HpStackMemberMacAddr_Type(OctetString):
    """Custom type hpStackMemberMacAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(6, 6),
    )


_HpStackMemberMacAddr_Type.__name__ = "OctetString"
_HpStackMemberMacAddr_Object = MibTableColumn
hpStackMemberMacAddr = _HpStackMemberMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 69, 1, 3, 1, 3),
    _HpStackMemberMacAddr_Type()
)
hpStackMemberMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpStackMemberMacAddr.setStatus("current")
_HpStackMemberShutdown_Type = TruthValue
_HpStackMemberShutdown_Object = MibTableColumn
hpStackMemberShutdown = _HpStackMemberShutdown_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 69, 1, 3, 1, 4),
    _HpStackMemberShutdown_Type()
)
hpStackMemberShutdown.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpStackMemberShutdown.setStatus("current")
_HpStackMemberReboot_Type = TruthValue
_HpStackMemberReboot_Object = MibTableColumn
hpStackMemberReboot = _HpStackMemberReboot_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 69, 1, 3, 1, 5),
    _HpStackMemberReboot_Type()
)
hpStackMemberReboot.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpStackMemberReboot.setStatus("current")


class _HpStackMemberAdminPriority_Type(Integer32):
    """Custom type hpStackMemberAdminPriority based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_HpStackMemberAdminPriority_Type.__name__ = "Integer32"
_HpStackMemberAdminPriority_Object = MibTableColumn
hpStackMemberAdminPriority = _HpStackMemberAdminPriority_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 69, 1, 3, 1, 6),
    _HpStackMemberAdminPriority_Type()
)
hpStackMemberAdminPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpStackMemberAdminPriority.setStatus("current")
_HpStackMemberEntryStatus_Type = RowStatus
_HpStackMemberEntryStatus_Object = MibTableColumn
hpStackMemberEntryStatus = _HpStackMemberEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 69, 1, 3, 1, 7),
    _HpStackMemberEntryStatus_Type()
)
hpStackMemberEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpStackMemberEntryStatus.setStatus("current")
_HpStackMemberEntPhysicalIndex_Type = PhysicalIndex
_HpStackMemberEntPhysicalIndex_Object = MibTableColumn
hpStackMemberEntPhysicalIndex = _HpStackMemberEntPhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 69, 1, 3, 1, 8),
    _HpStackMemberEntPhysicalIndex_Type()
)
hpStackMemberEntPhysicalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpStackMemberEntPhysicalIndex.setStatus("current")


class _HpStackMemberState_Type(Integer32):
    """Custom type hpStackMemberState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("booting", 7),
          ("commander", 3),
          ("communicationFailure", 8),
          ("incompatibleOs", 9),
          ("member", 5),
          ("missing", 1),
          ("provision", 2),
          ("shutdown", 6),
          ("standby", 4),
          ("standbyBooting", 11),
          ("unknownState", 10),
          ("unusedId", 0))
    )


_HpStackMemberState_Type.__name__ = "Integer32"
_HpStackMemberState_Object = MibTableColumn
hpStackMemberState = _HpStackMemberState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 69, 1, 3, 1, 9),
    _HpStackMemberState_Type()
)
hpStackMemberState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpStackMemberState.setStatus("current")
_HpStackMemberProductName_Type = SnmpAdminString
_HpStackMemberProductName_Object = MibTableColumn
hpStackMemberProductName = _HpStackMemberProductName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 69, 1, 3, 1, 10),
    _HpStackMemberProductName_Type()
)
hpStackMemberProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpStackMemberProductName.setStatus("current")
_HpStackMemberUpTime_Type = TimeTicks
_HpStackMemberUpTime_Object = MibTableColumn
hpStackMemberUpTime = _HpStackMemberUpTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 69, 1, 3, 1, 11),
    _HpStackMemberUpTime_Type()
)
hpStackMemberUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpStackMemberUpTime.setStatus("current")
_HpStackMemberSysOid_Type = ObjectIdentifier
_HpStackMemberSysOid_Object = MibTableColumn
hpStackMemberSysOid = _HpStackMemberSysOid_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 69, 1, 3, 1, 12),
    _HpStackMemberSysOid_Type()
)
hpStackMemberSysOid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpStackMemberSysOid.setStatus("current")
_HpStackMemberIdForTrap_Type = Integer32
_HpStackMemberIdForTrap_Object = MibTableColumn
hpStackMemberIdForTrap = _HpStackMemberIdForTrap_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 69, 1, 3, 1, 13),
    _HpStackMemberIdForTrap_Type()
)
hpStackMemberIdForTrap.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpStackMemberIdForTrap.setStatus("current")
_HpStackMemberSerialNum_Type = DisplayString
_HpStackMemberSerialNum_Object = MibTableColumn
hpStackMemberSerialNum = _HpStackMemberSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 69, 1, 3, 1, 14),
    _HpStackMemberSerialNum_Type()
)
hpStackMemberSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpStackMemberSerialNum.setStatus("current")
_HpStackMemberCpuUtil_Type = Integer32
_HpStackMemberCpuUtil_Object = MibTableColumn
hpStackMemberCpuUtil = _HpStackMemberCpuUtil_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 69, 1, 3, 1, 15),
    _HpStackMemberCpuUtil_Type()
)
hpStackMemberCpuUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpStackMemberCpuUtil.setStatus("current")
_HpStackMemberTotalMemory_Type = Integer32
_HpStackMemberTotalMemory_Object = MibTableColumn
hpStackMemberTotalMemory = _HpStackMemberTotalMemory_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 69, 1, 3, 1, 16),
    _HpStackMemberTotalMemory_Type()
)
hpStackMemberTotalMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpStackMemberTotalMemory.setStatus("current")
_HpStackMemberFreeMemory_Type = Integer32
_HpStackMemberFreeMemory_Object = MibTableColumn
hpStackMemberFreeMemory = _HpStackMemberFreeMemory_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 69, 1, 3, 1, 17),
    _HpStackMemberFreeMemory_Type()
)
hpStackMemberFreeMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpStackMemberFreeMemory.setStatus("current")
_HpStackMemberBootRomVersion_Type = DisplayString
_HpStackMemberBootRomVersion_Object = MibTableColumn
hpStackMemberBootRomVersion = _HpStackMemberBootRomVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 69, 1, 3, 1, 18),
    _HpStackMemberBootRomVersion_Type()
)
hpStackMemberBootRomVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpStackMemberBootRomVersion.setStatus("current")
_HpStackMemberOsVersion_Type = DisplayString
_HpStackMemberOsVersion_Object = MibTableColumn
hpStackMemberOsVersion = _HpStackMemberOsVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 69, 1, 3, 1, 19),
    _HpStackMemberOsVersion_Type()
)
hpStackMemberOsVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpStackMemberOsVersion.setStatus("current")


class _HpStackMemberBootImage_Type(Integer32):
    """Custom type hpStackMemberBootImage based on Integer32"""
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


_HpStackMemberBootImage_Type.__name__ = "Integer32"
_HpStackMemberBootImage_Object = MibTableColumn
hpStackMemberBootImage = _HpStackMemberBootImage_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 69, 1, 3, 1, 20),
    _HpStackMemberBootImage_Type()
)
hpStackMemberBootImage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpStackMemberBootImage.setStatus("current")
_HpStackPortTable_Object = MibTable
hpStackPortTable = _HpStackPortTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 69, 1, 5)
)
if mibBuilder.loadTexts:
    hpStackPortTable.setStatus("current")
_HpStackPortEntry_Object = MibTableRow
hpStackPortEntry = _HpStackPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 69, 1, 5, 1)
)
hpStackPortEntry.setIndexNames(
    (0, "HP-STACK-MIB", "hpStackMemberId"),
    (0, "HP-STACK-MIB", "hpStackPortId"),
    (0, "HP-STACK-MIB", "hpStackPortType"),
)
if mibBuilder.loadTexts:
    hpStackPortEntry.setStatus("current")


class _HpStackPortId_Type(Integer32):
    """Custom type hpStackPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpStackPortId_Type.__name__ = "Integer32"
_HpStackPortId_Object = MibTableColumn
hpStackPortId = _HpStackPortId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 69, 1, 5, 1, 1),
    _HpStackPortId_Type()
)
hpStackPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpStackPortId.setStatus("current")


class _HpStackPortType_Type(Integer32):
    """Custom type hpStackPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("backPlane", 1),
          ("frontPlane", 2))
    )


_HpStackPortType_Type.__name__ = "Integer32"
_HpStackPortType_Object = MibTableColumn
hpStackPortType = _HpStackPortType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 69, 1, 5, 1, 2),
    _HpStackPortType_Type()
)
hpStackPortType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpStackPortType.setStatus("current")


class _HpStackPortOperStatus_Type(Integer32):
    """Custom type hpStackPortOperStatus based on Integer32"""
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
        *(("blocked", 4),
          ("disabled", 3),
          ("down", 2),
          ("up", 1))
    )


_HpStackPortOperStatus_Type.__name__ = "Integer32"
_HpStackPortOperStatus_Object = MibTableColumn
hpStackPortOperStatus = _HpStackPortOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 69, 1, 5, 1, 3),
    _HpStackPortOperStatus_Type()
)
hpStackPortOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpStackPortOperStatus.setStatus("current")


class _HpStackPortNeighbor_Type(OctetString):
    """Custom type hpStackPortNeighbor based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_HpStackPortNeighbor_Type.__name__ = "OctetString"
_HpStackPortNeighbor_Object = MibTableColumn
hpStackPortNeighbor = _HpStackPortNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 69, 1, 5, 1, 4),
    _HpStackPortNeighbor_Type()
)
hpStackPortNeighbor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpStackPortNeighbor.setStatus("current")
_HpStackPortCost_Type = Integer32
_HpStackPortCost_Object = MibTableColumn
hpStackPortCost = _HpStackPortCost_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 69, 1, 5, 1, 5),
    _HpStackPortCost_Type()
)
hpStackPortCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpStackPortCost.setStatus("current")
_HpStackPortIdForTrap_Type = Integer32
_HpStackPortIdForTrap_Object = MibTableColumn
hpStackPortIdForTrap = _HpStackPortIdForTrap_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 69, 1, 5, 1, 6),
    _HpStackPortIdForTrap_Type()
)
hpStackPortIdForTrap.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpStackPortIdForTrap.setStatus("current")


class _HpStackPortTypeForTrap_Type(Integer32):
    """Custom type hpStackPortTypeForTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("backPlane", 1),
          ("frontPlane", 2))
    )


_HpStackPortTypeForTrap_Type.__name__ = "Integer32"
_HpStackPortTypeForTrap_Object = MibTableColumn
hpStackPortTypeForTrap = _HpStackPortTypeForTrap_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 69, 1, 5, 1, 7),
    _HpStackPortTypeForTrap_Type()
)
hpStackPortTypeForTrap.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpStackPortTypeForTrap.setStatus("current")


class _HpStackPortAdminStatus_Type(Integer32):
    """Custom type hpStackPortAdminStatus based on Integer32"""
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


_HpStackPortAdminStatus_Type.__name__ = "Integer32"
_HpStackPortAdminStatus_Object = MibTableColumn
hpStackPortAdminStatus = _HpStackPortAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 69, 1, 5, 1, 8),
    _HpStackPortAdminStatus_Type()
)
hpStackPortAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpStackPortAdminStatus.setStatus("current")
_HpStackConformance_ObjectIdentity = ObjectIdentity
hpStackConformance = _HpStackConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 69, 2)
)
_HpStackCompliances_ObjectIdentity = ObjectIdentity
hpStackCompliances = _HpStackCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 69, 2, 1)
)
_HpStackGroups_ObjectIdentity = ObjectIdentity
hpStackGroups = _HpStackGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 69, 2, 2)
)

# Managed Objects groups

hpStackConfigScalarGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 69, 2, 2, 1)
)
hpStackConfigScalarGroup.setObjects(
      *(("HP-STACK-MIB", "hpStackId"),
        ("HP-STACK-MIB", "hpStackOperStatus"),
        ("HP-STACK-MIB", "hpStackSetStacking"),
        ("HP-STACK-MIB", "hpStackTopology"),
        ("HP-STACK-MIB", "hpStackTrapEnable"),
        ("HP-STACK-MIB", "hpStackSwitchAdminStatus"),
        ("HP-STACK-MIB", "hpStackSwitchPreferredPriority"),
        ("HP-STACK-MIB", "hpStackSwitchPreferredMemberId"),
        ("HP-STACK-MIB", "hpStackSplitPolicy"))
)
if mibBuilder.loadTexts:
    hpStackConfigScalarGroup.setStatus("current")

hpStackMemberGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 69, 2, 2, 2)
)
hpStackMemberGroup.setObjects(
      *(("HP-STACK-MIB", "hpStackMemberProductId"),
        ("HP-STACK-MIB", "hpStackMemberMacAddr"),
        ("HP-STACK-MIB", "hpStackMemberShutdown"),
        ("HP-STACK-MIB", "hpStackMemberReboot"),
        ("HP-STACK-MIB", "hpStackMemberAdminPriority"),
        ("HP-STACK-MIB", "hpStackMemberEntryStatus"),
        ("HP-STACK-MIB", "hpStackMemberEntPhysicalIndex"),
        ("HP-STACK-MIB", "hpStackMemberState"),
        ("HP-STACK-MIB", "hpStackMemberProductName"),
        ("HP-STACK-MIB", "hpStackMemberUpTime"),
        ("HP-STACK-MIB", "hpStackMemberSysOid"),
        ("HP-STACK-MIB", "hpStackMemberIdForTrap"),
        ("HP-STACK-MIB", "hpStackMemberSerialNum"),
        ("HP-STACK-MIB", "hpStackMemberCpuUtil"),
        ("HP-STACK-MIB", "hpStackMemberTotalMemory"),
        ("HP-STACK-MIB", "hpStackMemberFreeMemory"),
        ("HP-STACK-MIB", "hpStackMemberBootRomVersion"),
        ("HP-STACK-MIB", "hpStackMemberOsVersion"),
        ("HP-STACK-MIB", "hpStackMemberBootImage"))
)
if mibBuilder.loadTexts:
    hpStackMemberGroup.setStatus("current")

hpStackPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 69, 2, 2, 3)
)
hpStackPortGroup.setObjects(
      *(("HP-STACK-MIB", "hpStackPortOperStatus"),
        ("HP-STACK-MIB", "hpStackPortNeighbor"),
        ("HP-STACK-MIB", "hpStackPortCost"),
        ("HP-STACK-MIB", "hpStackPortIdForTrap"),
        ("HP-STACK-MIB", "hpStackPortTypeForTrap"),
        ("HP-STACK-MIB", "hpStackPortAdminStatus"))
)
if mibBuilder.loadTexts:
    hpStackPortGroup.setStatus("current")


# Notification objects

hpStackPortChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 69, 0, 1)
)
hpStackPortChange.setObjects(
      *(("HP-STACK-MIB", "hpStackMemberIdForTrap"),
        ("HP-STACK-MIB", "hpStackPortIdForTrap"),
        ("HP-STACK-MIB", "hpStackPortTypeForTrap"),
        ("HP-STACK-MIB", "hpStackPortOperStatus"),
        ("HP-STACK-MIB", "hpStackPortNeighbor"))
)
if mibBuilder.loadTexts:
    hpStackPortChange.setStatus(
        "current"
    )

hpStackCommanderChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 69, 0, 2)
)
hpStackCommanderChange.setObjects(
      *(("HP-STACK-MIB", "hpStackMemberIdForTrap"),
        ("HP-STACK-MIB", "hpStackMemberState"))
)
if mibBuilder.loadTexts:
    hpStackCommanderChange.setStatus(
        "current"
    )

hpStackMemberChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 69, 0, 3)
)
hpStackMemberChange.setObjects(
      *(("HP-STACK-MIB", "hpStackMemberIdForTrap"),
        ("HP-STACK-MIB", "hpStackMemberState"))
)
if mibBuilder.loadTexts:
    hpStackMemberChange.setStatus(
        "current"
    )

hpStackMemberStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 69, 0, 4)
)
hpStackMemberStatusChange.setObjects(
      *(("HP-STACK-MIB", "hpStackMemberIdForTrap"),
        ("NETSWITCH-MIB", "hpSwitchBaseMACAddress"),
        ("HP-STACK-MIB", "hpStackMemberState"))
)
if mibBuilder.loadTexts:
    hpStackMemberStatusChange.setStatus(
        "current"
    )

hpStackMergeFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 69, 0, 5)
)
hpStackMergeFailed.setObjects(
      *(("HP-STACK-MIB", "hpStackMemberIdForTrap"),
        ("HP-STACK-MIB", "hpStackMemberState"),
        ("HP-STACK-MIB", "hpStackId"))
)
if mibBuilder.loadTexts:
    hpStackMergeFailed.setStatus(
        "current"
    )

hpStackMergeSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 69, 0, 6)
)
hpStackMergeSuccess.setObjects(
      *(("HP-STACK-MIB", "hpStackMemberIdForTrap"),
        ("HP-STACK-MIB", "hpStackMemberState"),
        ("HP-STACK-MIB", "hpStackId"))
)
if mibBuilder.loadTexts:
    hpStackMergeSuccess.setStatus(
        "current"
    )


# Notifications groups

hpStackNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 69, 2, 2, 4)
)
hpStackNotificationsGroup.setObjects(
      *(("HP-STACK-MIB", "hpStackPortChange"),
        ("HP-STACK-MIB", "hpStackCommanderChange"),
        ("HP-STACK-MIB", "hpStackMemberChange"),
        ("HP-STACK-MIB", "hpStackMemberStatusChange"),
        ("HP-STACK-MIB", "hpStackMergeFailed"),
        ("HP-STACK-MIB", "hpStackMergeSuccess"))
)
if mibBuilder.loadTexts:
    hpStackNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hpStackCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 69, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hpStackCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-STACK-MIB",
    **{"hpStackMIB": hpStackMIB,
       "hpStackNotifications": hpStackNotifications,
       "hpStackPortChange": hpStackPortChange,
       "hpStackCommanderChange": hpStackCommanderChange,
       "hpStackMemberChange": hpStackMemberChange,
       "hpStackMemberStatusChange": hpStackMemberStatusChange,
       "hpStackMergeFailed": hpStackMergeFailed,
       "hpStackMergeSuccess": hpStackMergeSuccess,
       "hpStackObjects": hpStackObjects,
       "hpStackConfig": hpStackConfig,
       "hpStackId": hpStackId,
       "hpStackOperStatus": hpStackOperStatus,
       "hpStackSetStacking": hpStackSetStacking,
       "hpStackTopology": hpStackTopology,
       "hpStackTrapEnable": hpStackTrapEnable,
       "hpStackSplitPolicy": hpStackSplitPolicy,
       "hpStackConfigTable": hpStackConfigTable,
       "hpStackConfigEntry": hpStackConfigEntry,
       "hpStackSequenceNum": hpStackSequenceNum,
       "hpStackSwitchAdminStatus": hpStackSwitchAdminStatus,
       "hpStackSwitchPreferredPriority": hpStackSwitchPreferredPriority,
       "hpStackSwitchPreferredMemberId": hpStackSwitchPreferredMemberId,
       "hpStackMemberTable": hpStackMemberTable,
       "hpStackMemberEntry": hpStackMemberEntry,
       "hpStackMemberId": hpStackMemberId,
       "hpStackMemberProductId": hpStackMemberProductId,
       "hpStackMemberMacAddr": hpStackMemberMacAddr,
       "hpStackMemberShutdown": hpStackMemberShutdown,
       "hpStackMemberReboot": hpStackMemberReboot,
       "hpStackMemberAdminPriority": hpStackMemberAdminPriority,
       "hpStackMemberEntryStatus": hpStackMemberEntryStatus,
       "hpStackMemberEntPhysicalIndex": hpStackMemberEntPhysicalIndex,
       "hpStackMemberState": hpStackMemberState,
       "hpStackMemberProductName": hpStackMemberProductName,
       "hpStackMemberUpTime": hpStackMemberUpTime,
       "hpStackMemberSysOid": hpStackMemberSysOid,
       "hpStackMemberIdForTrap": hpStackMemberIdForTrap,
       "hpStackMemberSerialNum": hpStackMemberSerialNum,
       "hpStackMemberCpuUtil": hpStackMemberCpuUtil,
       "hpStackMemberTotalMemory": hpStackMemberTotalMemory,
       "hpStackMemberFreeMemory": hpStackMemberFreeMemory,
       "hpStackMemberBootRomVersion": hpStackMemberBootRomVersion,
       "hpStackMemberOsVersion": hpStackMemberOsVersion,
       "hpStackMemberBootImage": hpStackMemberBootImage,
       "hpStackPortTable": hpStackPortTable,
       "hpStackPortEntry": hpStackPortEntry,
       "hpStackPortId": hpStackPortId,
       "hpStackPortType": hpStackPortType,
       "hpStackPortOperStatus": hpStackPortOperStatus,
       "hpStackPortNeighbor": hpStackPortNeighbor,
       "hpStackPortCost": hpStackPortCost,
       "hpStackPortIdForTrap": hpStackPortIdForTrap,
       "hpStackPortTypeForTrap": hpStackPortTypeForTrap,
       "hpStackPortAdminStatus": hpStackPortAdminStatus,
       "hpStackConformance": hpStackConformance,
       "hpStackCompliances": hpStackCompliances,
       "hpStackCompliance": hpStackCompliance,
       "hpStackGroups": hpStackGroups,
       "hpStackConfigScalarGroup": hpStackConfigScalarGroup,
       "hpStackMemberGroup": hpStackMemberGroup,
       "hpStackPortGroup": hpStackPortGroup,
       "hpStackNotificationsGroup": hpStackNotificationsGroup}
)
