# SNMP MIB module (CISCO-STACKWISE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-STACKWISE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:08:54 2024
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

(EntPhysicalIndexOrZero,) = mibBuilder.importSymbols(
    "CISCO-TC",
    "EntPhysicalIndexOrZero")

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoStackWiseMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 500)
)
ciscoStackWiseMIB.setRevisions(
        ("2016-04-16 00:00",
         "2015-11-24 00:00",
         "2011-12-12 00:00",
         "2010-02-01 00:00",
         "2008-06-10 00:00",
         "2005-10-12 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CswPowerStackMode(Integer32, TextualConvention):
    status = "current"
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
        *(("powerSharing", 1),
          ("powerSharingStrict", 3),
          ("redundant", 2),
          ("redundantStrict", 4))
    )



class CswPowerStackType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ring", 1),
          ("star", 2))
    )



class CswSwitchNumber(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class CswSwitchNumberOrZero(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )



class CswSwitchPriority(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )



# MIB Managed Objects in the order of their OIDs

_CiscoStackWiseMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoStackWiseMIBNotifs = _CiscoStackWiseMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 500, 0)
)
_CswMIBNotifications_ObjectIdentity = ObjectIdentity
cswMIBNotifications = _CswMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 500, 0, 0)
)
_CiscoStackWiseMIBObjects_ObjectIdentity = ObjectIdentity
ciscoStackWiseMIBObjects = _CiscoStackWiseMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 500, 1)
)
_CswGlobals_ObjectIdentity = ObjectIdentity
cswGlobals = _CswGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 500, 1, 1)
)
_CswMaxSwitchNum_Type = CswSwitchNumber
_CswMaxSwitchNum_Object = MibScalar
cswMaxSwitchNum = _CswMaxSwitchNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 500, 1, 1, 1),
    _CswMaxSwitchNum_Type()
)
cswMaxSwitchNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cswMaxSwitchNum.setStatus("current")
_CswMaxSwitchConfigPriority_Type = CswSwitchPriority
_CswMaxSwitchConfigPriority_Object = MibScalar
cswMaxSwitchConfigPriority = _CswMaxSwitchConfigPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 500, 1, 1, 2),
    _CswMaxSwitchConfigPriority_Type()
)
cswMaxSwitchConfigPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cswMaxSwitchConfigPriority.setStatus("current")
_CswRingRedundant_Type = TruthValue
_CswRingRedundant_Object = MibScalar
cswRingRedundant = _CswRingRedundant_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 500, 1, 1, 3),
    _CswRingRedundant_Type()
)
cswRingRedundant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cswRingRedundant.setStatus("current")
_CswEnableStackNotifications_Type = TruthValue
_CswEnableStackNotifications_Object = MibScalar
cswEnableStackNotifications = _CswEnableStackNotifications_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 500, 1, 1, 4),
    _CswEnableStackNotifications_Type()
)
cswEnableStackNotifications.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cswEnableStackNotifications.setStatus("deprecated")


class _CswEnableIndividualStackNotifications_Type(Bits):
    """Custom type cswEnableIndividualStackNotifications based on Bits"""
    namedValues = NamedValues(
        *(("stackMemberRemoved", 5),
          ("stackMemberToBeReloadedForUpgrade", 22),
          ("stackMismatch", 2),
          ("stackNewMaster", 1),
          ("stackNewMember", 4),
          ("stackPortChange", 0),
          ("stackPowerBudgetWarning", 10),
          ("stackPowerGLS", 18),
          ("stackPowerILS", 19),
          ("stackPowerInsufficientPower", 15),
          ("stackPowerInvalidInputCurrent", 11),
          ("stackPowerInvalidOutputCurrent", 12),
          ("stackPowerInvalidTopology", 9),
          ("stackPowerLinkStatusChanged", 6),
          ("stackPowerPortOperStatusChanged", 7),
          ("stackPowerPriorityConflict", 16),
          ("stackPowerSRLS", 20),
          ("stackPowerSSLS", 21),
          ("stackPowerUnbalancedPowerSupplies", 14),
          ("stackPowerUnderBudget", 13),
          ("stackPowerUnderVoltage", 17),
          ("stackPowerVersionMismatch", 8),
          ("stackRingRedundant", 3))
    )

_CswEnableIndividualStackNotifications_Type.__name__ = "Bits"
_CswEnableIndividualStackNotifications_Object = MibScalar
cswEnableIndividualStackNotifications = _CswEnableIndividualStackNotifications_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 500, 1, 1, 5),
    _CswEnableIndividualStackNotifications_Type()
)
cswEnableIndividualStackNotifications.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cswEnableIndividualStackNotifications.setStatus("current")
_CswStackDomainNum_Type = Unsigned32
_CswStackDomainNum_Object = MibScalar
cswStackDomainNum = _CswStackDomainNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 500, 1, 1, 6),
    _CswStackDomainNum_Type()
)
cswStackDomainNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cswStackDomainNum.setStatus("current")
_CswStackType_Type = Unsigned32
_CswStackType_Object = MibScalar
cswStackType = _CswStackType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 500, 1, 1, 7),
    _CswStackType_Type()
)
cswStackType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cswStackType.setStatus("current")
_CswStackBandWidth_Type = Unsigned32
_CswStackBandWidth_Object = MibScalar
cswStackBandWidth = _CswStackBandWidth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 500, 1, 1, 8),
    _CswStackBandWidth_Type()
)
cswStackBandWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cswStackBandWidth.setStatus("current")
_CswStackInfo_ObjectIdentity = ObjectIdentity
cswStackInfo = _CswStackInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 500, 1, 2)
)
_CswSwitchInfoTable_Object = MibTable
cswSwitchInfoTable = _CswSwitchInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 500, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cswSwitchInfoTable.setStatus("current")
_CswSwitchInfoEntry_Object = MibTableRow
cswSwitchInfoEntry = _CswSwitchInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 500, 1, 2, 1, 1)
)
cswSwitchInfoEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    cswSwitchInfoEntry.setStatus("current")
_CswSwitchNumCurrent_Type = CswSwitchNumber
_CswSwitchNumCurrent_Object = MibTableColumn
cswSwitchNumCurrent = _CswSwitchNumCurrent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 500, 1, 2, 1, 1, 1),
    _CswSwitchNumCurrent_Type()
)
cswSwitchNumCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cswSwitchNumCurrent.setStatus("current")
_CswSwitchNumNextReload_Type = CswSwitchNumberOrZero
_CswSwitchNumNextReload_Object = MibTableColumn
cswSwitchNumNextReload = _CswSwitchNumNextReload_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 500, 1, 2, 1, 1, 2),
    _CswSwitchNumNextReload_Type()
)
cswSwitchNumNextReload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cswSwitchNumNextReload.setStatus("current")


class _CswSwitchRole_Type(Integer32):
    """Custom type cswSwitchRole based on Integer32"""
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
        *(("master", 1),
          ("member", 2),
          ("notMember", 3),
          ("standby", 4))
    )


_CswSwitchRole_Type.__name__ = "Integer32"
_CswSwitchRole_Object = MibTableColumn
cswSwitchRole = _CswSwitchRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 500, 1, 2, 1, 1, 3),
    _CswSwitchRole_Type()
)
cswSwitchRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cswSwitchRole.setStatus("current")
_CswSwitchSwPriority_Type = CswSwitchPriority
_CswSwitchSwPriority_Object = MibTableColumn
cswSwitchSwPriority = _CswSwitchSwPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 500, 1, 2, 1, 1, 4),
    _CswSwitchSwPriority_Type()
)
cswSwitchSwPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cswSwitchSwPriority.setStatus("current")
_CswSwitchHwPriority_Type = CswSwitchPriority
_CswSwitchHwPriority_Object = MibTableColumn
cswSwitchHwPriority = _CswSwitchHwPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 500, 1, 2, 1, 1, 5),
    _CswSwitchHwPriority_Type()
)
cswSwitchHwPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cswSwitchHwPriority.setStatus("current")


class _CswSwitchState_Type(Integer32):
    """Custom type cswSwitchState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
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
        *(("added", 3),
          ("featureMismatch", 7),
          ("invalid", 10),
          ("newMasterInit", 8),
          ("progressing", 2),
          ("provisioned", 9),
          ("ready", 4),
          ("removed", 11),
          ("sdmMismatch", 5),
          ("verMismatch", 6),
          ("waiting", 1))
    )


_CswSwitchState_Type.__name__ = "Integer32"
_CswSwitchState_Object = MibTableColumn
cswSwitchState = _CswSwitchState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 500, 1, 2, 1, 1, 6),
    _CswSwitchState_Type()
)
cswSwitchState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cswSwitchState.setStatus("current")
_CswSwitchMacAddress_Type = MacAddress
_CswSwitchMacAddress_Object = MibTableColumn
cswSwitchMacAddress = _CswSwitchMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 500, 1, 2, 1, 1, 7),
    _CswSwitchMacAddress_Type()
)
cswSwitchMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cswSwitchMacAddress.setStatus("current")
_CswSwitchSoftwareImage_Type = SnmpAdminString
_CswSwitchSoftwareImage_Object = MibTableColumn
cswSwitchSoftwareImage = _CswSwitchSoftwareImage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 500, 1, 2, 1, 1, 8),
    _CswSwitchSoftwareImage_Type()
)
cswSwitchSoftwareImage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cswSwitchSoftwareImage.setStatus("current")
_CswSwitchPowerBudget_Type = Unsigned32
_CswSwitchPowerBudget_Object = MibTableColumn
cswSwitchPowerBudget = _CswSwitchPowerBudget_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 500, 1, 2, 1, 1, 9),
    _CswSwitchPowerBudget_Type()
)
cswSwitchPowerBudget.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cswSwitchPowerBudget.setStatus("current")
if mibBuilder.loadTexts:
    cswSwitchPowerBudget.setUnits("Watts")
_CswSwitchPowerCommited_Type = Unsigned32
_CswSwitchPowerCommited_Object = MibTableColumn
cswSwitchPowerCommited = _CswSwitchPowerCommited_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 500, 1, 2, 1, 1, 10),
    _CswSwitchPowerCommited_Type()
)
cswSwitchPowerCommited.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cswSwitchPowerCommited.setStatus("current")
if mibBuilder.loadTexts:
    cswSwitchPowerCommited.setUnits("Watts")
_CswSwitchSystemPowerPriority_Type = Unsigned32
_CswSwitchSystemPowerPriority_Object = MibTableColumn
cswSwitchSystemPowerPriority = _CswSwitchSystemPowerPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 500, 1, 2, 1, 1, 11),
    _CswSwitchSystemPowerPriority_Type()
)
cswSwitchSystemPowerPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cswSwitchSystemPowerPriority.setStatus("current")
_CswSwitchPoeDevicesLowPriority_Type = Unsigned32
_CswSwitchPoeDevicesLowPriority_Object = MibTableColumn
cswSwitchPoeDevicesLowPriority = _CswSwitchPoeDevicesLowPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 500, 1, 2, 1, 1, 12),
    _CswSwitchPoeDevicesLowPriority_Type()
)
cswSwitchPoeDevicesLowPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cswSwitchPoeDevicesLowPriority.setStatus("current")
_CswSwitchPoeDevicesHighPriority_Type = Unsigned32
_CswSwitchPoeDevicesHighPriority_Object = MibTableColumn
cswSwitchPoeDevicesHighPriority = _CswSwitchPoeDevicesHighPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 500, 1, 2, 1, 1, 13),
    _CswSwitchPoeDevicesHighPriority_Type()
)
cswSwitchPoeDevicesHighPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cswSwitchPoeDevicesHighPriority.setStatus("current")
_CswSwitchPowerAllocated_Type = Unsigned32
_CswSwitchPowerAllocated_Object = MibTableColumn
cswSwitchPowerAllocated = _CswSwitchPowerAllocated_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 500, 1, 2, 1, 1, 14),
    _CswSwitchPowerAllocated_Type()
)
cswSwitchPowerAllocated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cswSwitchPowerAllocated.setStatus("current")
if mibBuilder.loadTexts:
    cswSwitchPowerAllocated.setUnits("Watts")
_CswStackPortInfoTable_Object = MibTable
cswStackPortInfoTable = _CswStackPortInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 500, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cswStackPortInfoTable.setStatus("current")
_CswStackPortInfoEntry_Object = MibTableRow
cswStackPortInfoEntry = _CswStackPortInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 500, 1, 2, 2, 1)
)
cswStackPortInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cswStackPortInfoEntry.setStatus("current")


class _CswStackPortOperStatus_Type(Integer32):
    """Custom type cswStackPortOperStatus based on Integer32"""
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
          ("forcedDown", 3),
          ("up", 1))
    )


_CswStackPortOperStatus_Type.__name__ = "Integer32"
_CswStackPortOperStatus_Object = MibTableColumn
cswStackPortOperStatus = _CswStackPortOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 500, 1, 2, 2, 1, 1),
    _CswStackPortOperStatus_Type()
)
cswStackPortOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cswStackPortOperStatus.setStatus("current")
_CswStackPortNeighbor_Type = EntPhysicalIndexOrZero
_CswStackPortNeighbor_Object = MibTableColumn
cswStackPortNeighbor = _CswStackPortNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 500, 1, 2, 2, 1, 2),
    _CswStackPortNeighbor_Type()
)
cswStackPortNeighbor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cswStackPortNeighbor.setStatus("current")
_CswDistrStackLinkInfoTable_Object = MibTable
cswDistrStackLinkInfoTable = _CswDistrStackLinkInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 500, 1, 2, 3)
)
if mibBuilder.loadTexts:
    cswDistrStackLinkInfoTable.setStatus("current")
_CswDistrStackLinkInfoEntry_Object = MibTableRow
cswDistrStackLinkInfoEntry = _CswDistrStackLinkInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 500, 1, 2, 3, 1)
)
cswDistrStackLinkInfoEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-STACKWISE-MIB", "cswDSLindex"),
)
if mibBuilder.loadTexts:
    cswDistrStackLinkInfoEntry.setStatus("current")


class _CswDSLindex_Type(Unsigned32):
    """Custom type cswDSLindex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_CswDSLindex_Type.__name__ = "Unsigned32"
_CswDSLindex_Object = MibTableColumn
cswDSLindex = _CswDSLindex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 500, 1, 2, 3, 1, 1),
    _CswDSLindex_Type()
)
cswDSLindex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cswDSLindex.setStatus("current")


class _CswDistrStackLinkBundleOperStatus_Type(Integer32):
    """Custom type cswDistrStackLinkBundleOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_CswDistrStackLinkBundleOperStatus_Type.__name__ = "Integer32"
_CswDistrStackLinkBundleOperStatus_Object = MibTableColumn
cswDistrStackLinkBundleOperStatus = _CswDistrStackLinkBundleOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 500, 1, 2, 3, 1, 2),
    _CswDistrStackLinkBundleOperStatus_Type()
)
cswDistrStackLinkBundleOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cswDistrStackLinkBundleOperStatus.setStatus("current")
_CswDistrStackPhyPortInfoTable_Object = MibTable
cswDistrStackPhyPortInfoTable = _CswDistrStackPhyPortInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 500, 1, 2, 4)
)
if mibBuilder.loadTexts:
    cswDistrStackPhyPortInfoTable.setStatus("current")
_CswDistrStackPhyPortInfoEntry_Object = MibTableRow
cswDistrStackPhyPortInfoEntry = _CswDistrStackPhyPortInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 500, 1, 2, 4, 1)
)
cswDistrStackPhyPortInfoEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-STACKWISE-MIB", "cswDSLindex"),
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cswDistrStackPhyPortInfoEntry.setStatus("current")
_CswDistrStackPhyPort_Type = SnmpAdminString
_CswDistrStackPhyPort_Object = MibTableColumn
cswDistrStackPhyPort = _CswDistrStackPhyPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 500, 1, 2, 4, 1, 1),
    _CswDistrStackPhyPort_Type()
)
cswDistrStackPhyPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cswDistrStackPhyPort.setStatus("current")


class _CswDistrStackPhyPortOperStatus_Type(Integer32):
    """Custom type cswDistrStackPhyPortOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_CswDistrStackPhyPortOperStatus_Type.__name__ = "Integer32"
_CswDistrStackPhyPortOperStatus_Object = MibTableColumn
cswDistrStackPhyPortOperStatus = _CswDistrStackPhyPortOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 500, 1, 2, 4, 1, 2),
    _CswDistrStackPhyPortOperStatus_Type()
)
cswDistrStackPhyPortOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cswDistrStackPhyPortOperStatus.setStatus("current")
_CswDistrStackPhyPortNbr_Type = SnmpAdminString
_CswDistrStackPhyPortNbr_Object = MibTableColumn
cswDistrStackPhyPortNbr = _CswDistrStackPhyPortNbr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 500, 1, 2, 4, 1, 3),
    _CswDistrStackPhyPortNbr_Type()
)
cswDistrStackPhyPortNbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cswDistrStackPhyPortNbr.setStatus("current")
_CswDistrStackPhyPortNbrsw_Type = EntPhysicalIndexOrZero
_CswDistrStackPhyPortNbrsw_Object = MibTableColumn
cswDistrStackPhyPortNbrsw = _CswDistrStackPhyPortNbrsw_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 500, 1, 2, 4, 1, 4),
    _CswDistrStackPhyPortNbrsw_Type()
)
cswDistrStackPhyPortNbrsw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cswDistrStackPhyPortNbrsw.setStatus("current")
_CswStackPowerInfo_ObjectIdentity = ObjectIdentity
cswStackPowerInfo = _CswStackPowerInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 500, 1, 3)
)
_CswStackPowerInfoTable_Object = MibTable
cswStackPowerInfoTable = _CswStackPowerInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 500, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cswStackPowerInfoTable.setStatus("current")
_CswStackPowerInfoEntry_Object = MibTableRow
cswStackPowerInfoEntry = _CswStackPowerInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 500, 1, 3, 1, 1)
)
cswStackPowerInfoEntry.setIndexNames(
    (0, "CISCO-STACKWISE-MIB", "cswStackPowerStackNumber"),
)
if mibBuilder.loadTexts:
    cswStackPowerInfoEntry.setStatus("current")
_CswStackPowerStackNumber_Type = Unsigned32
_CswStackPowerStackNumber_Object = MibTableColumn
cswStackPowerStackNumber = _CswStackPowerStackNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 500, 1, 3, 1, 1, 1),
    _CswStackPowerStackNumber_Type()
)
cswStackPowerStackNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cswStackPowerStackNumber.setStatus("current")
_CswStackPowerMode_Type = CswPowerStackMode
_CswStackPowerMode_Object = MibTableColumn
cswStackPowerMode = _CswStackPowerMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 500, 1, 3, 1, 1, 2),
    _CswStackPowerMode_Type()
)
cswStackPowerMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cswStackPowerMode.setStatus("current")
_CswStackPowerMasterMacAddress_Type = MacAddress
_CswStackPowerMasterMacAddress_Object = MibTableColumn
cswStackPowerMasterMacAddress = _CswStackPowerMasterMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 500, 1, 3, 1, 1, 3),
    _CswStackPowerMasterMacAddress_Type()
)
cswStackPowerMasterMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cswStackPowerMasterMacAddress.setStatus("current")
_CswStackPowerMasterSwitchNum_Type = Unsigned32
_CswStackPowerMasterSwitchNum_Object = MibTableColumn
cswStackPowerMasterSwitchNum = _CswStackPowerMasterSwitchNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 500, 1, 3, 1, 1, 4),
    _CswStackPowerMasterSwitchNum_Type()
)
cswStackPowerMasterSwitchNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cswStackPowerMasterSwitchNum.setStatus("current")
_CswStackPowerNumMembers_Type = Unsigned32
_CswStackPowerNumMembers_Object = MibTableColumn
cswStackPowerNumMembers = _CswStackPowerNumMembers_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 500, 1, 3, 1, 1, 5),
    _CswStackPowerNumMembers_Type()
)
cswStackPowerNumMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cswStackPowerNumMembers.setStatus("current")
_CswStackPowerType_Type = CswPowerStackType
_CswStackPowerType_Object = MibTableColumn
cswStackPowerType = _CswStackPowerType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 500, 1, 3, 1, 1, 6),
    _CswStackPowerType_Type()
)
cswStackPowerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cswStackPowerType.setStatus("current")
_CswStackPowerName_Type = SnmpAdminString
_CswStackPowerName_Object = MibTableColumn
cswStackPowerName = _CswStackPowerName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 500, 1, 3, 1, 1, 7),
    _CswStackPowerName_Type()
)
cswStackPowerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cswStackPowerName.setStatus("current")
_CswStackPowerPortInfoTable_Object = MibTable
cswStackPowerPortInfoTable = _CswStackPowerPortInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 500, 1, 3, 2)
)
if mibBuilder.loadTexts:
    cswStackPowerPortInfoTable.setStatus("current")
_CswStackPowerPortInfoEntry_Object = MibTableRow
cswStackPowerPortInfoEntry = _CswStackPowerPortInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 500, 1, 3, 2, 1)
)
cswStackPowerPortInfoEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-STACKWISE-MIB", "cswStackPowerPortIndex"),
)
if mibBuilder.loadTexts:
    cswStackPowerPortInfoEntry.setStatus("current")
_CswStackPowerPortIndex_Type = Unsigned32
_CswStackPowerPortIndex_Object = MibTableColumn
cswStackPowerPortIndex = _CswStackPowerPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 500, 1, 3, 2, 1, 1),
    _CswStackPowerPortIndex_Type()
)
cswStackPowerPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cswStackPowerPortIndex.setStatus("current")


class _CswStackPowerPortOperStatus_Type(Integer32):
    """Custom type cswStackPowerPortOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_CswStackPowerPortOperStatus_Type.__name__ = "Integer32"
_CswStackPowerPortOperStatus_Object = MibTableColumn
cswStackPowerPortOperStatus = _CswStackPowerPortOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 500, 1, 3, 2, 1, 2),
    _CswStackPowerPortOperStatus_Type()
)
cswStackPowerPortOperStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cswStackPowerPortOperStatus.setStatus("current")
_CswStackPowerPortNeighborMacAddress_Type = MacAddress
_CswStackPowerPortNeighborMacAddress_Object = MibTableColumn
cswStackPowerPortNeighborMacAddress = _CswStackPowerPortNeighborMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 500, 1, 3, 2, 1, 3),
    _CswStackPowerPortNeighborMacAddress_Type()
)
cswStackPowerPortNeighborMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cswStackPowerPortNeighborMacAddress.setStatus("current")
_CswStackPowerPortNeighborSwitchNum_Type = CswSwitchNumberOrZero
_CswStackPowerPortNeighborSwitchNum_Object = MibTableColumn
cswStackPowerPortNeighborSwitchNum = _CswStackPowerPortNeighborSwitchNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 500, 1, 3, 2, 1, 4),
    _CswStackPowerPortNeighborSwitchNum_Type()
)
cswStackPowerPortNeighborSwitchNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cswStackPowerPortNeighborSwitchNum.setStatus("current")


class _CswStackPowerPortLinkStatus_Type(Integer32):
    """Custom type cswStackPowerPortLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_CswStackPowerPortLinkStatus_Type.__name__ = "Integer32"
_CswStackPowerPortLinkStatus_Object = MibTableColumn
cswStackPowerPortLinkStatus = _CswStackPowerPortLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 500, 1, 3, 2, 1, 5),
    _CswStackPowerPortLinkStatus_Type()
)
cswStackPowerPortLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cswStackPowerPortLinkStatus.setStatus("current")
_CswStackPowerPortOverCurrentThreshold_Type = Unsigned32
_CswStackPowerPortOverCurrentThreshold_Object = MibTableColumn
cswStackPowerPortOverCurrentThreshold = _CswStackPowerPortOverCurrentThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 500, 1, 3, 2, 1, 6),
    _CswStackPowerPortOverCurrentThreshold_Type()
)
cswStackPowerPortOverCurrentThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cswStackPowerPortOverCurrentThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cswStackPowerPortOverCurrentThreshold.setUnits("Amperes")
_CswStackPowerPortName_Type = SnmpAdminString
_CswStackPowerPortName_Object = MibTableColumn
cswStackPowerPortName = _CswStackPowerPortName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 500, 1, 3, 2, 1, 7),
    _CswStackPowerPortName_Type()
)
cswStackPowerPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cswStackPowerPortName.setStatus("current")
_CiscoStackWiseMIBConform_ObjectIdentity = ObjectIdentity
ciscoStackWiseMIBConform = _CiscoStackWiseMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 500, 2)
)
_CswStackWiseMIBCompliances_ObjectIdentity = ObjectIdentity
cswStackWiseMIBCompliances = _CswStackWiseMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 500, 2, 1)
)
_CswStackWiseMIBGroups_ObjectIdentity = ObjectIdentity
cswStackWiseMIBGroups = _CswStackWiseMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 500, 2, 2)
)

# Managed Objects groups

cswStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 500, 2, 2, 1)
)
cswStatusGroup.setObjects(
      *(("CISCO-STACKWISE-MIB", "cswMaxSwitchNum"),
        ("CISCO-STACKWISE-MIB", "cswMaxSwitchConfigPriority"),
        ("CISCO-STACKWISE-MIB", "cswRingRedundant"),
        ("CISCO-STACKWISE-MIB", "cswEnableStackNotifications"),
        ("CISCO-STACKWISE-MIB", "cswSwitchNumCurrent"),
        ("CISCO-STACKWISE-MIB", "cswSwitchNumNextReload"),
        ("CISCO-STACKWISE-MIB", "cswSwitchRole"),
        ("CISCO-STACKWISE-MIB", "cswSwitchSwPriority"),
        ("CISCO-STACKWISE-MIB", "cswSwitchHwPriority"),
        ("CISCO-STACKWISE-MIB", "cswSwitchState"),
        ("CISCO-STACKWISE-MIB", "cswSwitchMacAddress"),
        ("CISCO-STACKWISE-MIB", "cswSwitchSoftwareImage"),
        ("CISCO-STACKWISE-MIB", "cswStackPortOperStatus"),
        ("CISCO-STACKWISE-MIB", "cswStackPortNeighbor"),
        ("CISCO-STACKWISE-MIB", "cswStackPowerType"))
)
if mibBuilder.loadTexts:
    cswStatusGroup.setStatus("deprecated")

cswStatusGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 500, 2, 2, 3)
)
cswStatusGroupRev1.setObjects(
      *(("CISCO-STACKWISE-MIB", "cswMaxSwitchNum"),
        ("CISCO-STACKWISE-MIB", "cswMaxSwitchConfigPriority"),
        ("CISCO-STACKWISE-MIB", "cswRingRedundant"),
        ("CISCO-STACKWISE-MIB", "cswSwitchNumCurrent"),
        ("CISCO-STACKWISE-MIB", "cswSwitchNumNextReload"),
        ("CISCO-STACKWISE-MIB", "cswSwitchRole"),
        ("CISCO-STACKWISE-MIB", "cswSwitchSwPriority"),
        ("CISCO-STACKWISE-MIB", "cswSwitchHwPriority"),
        ("CISCO-STACKWISE-MIB", "cswSwitchState"),
        ("CISCO-STACKWISE-MIB", "cswSwitchMacAddress"),
        ("CISCO-STACKWISE-MIB", "cswSwitchSoftwareImage"))
)
if mibBuilder.loadTexts:
    cswStatusGroupRev1.setStatus("current")

cswStackPowerStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 500, 2, 2, 4)
)
cswStackPowerStatusGroup.setObjects(
      *(("CISCO-STACKWISE-MIB", "cswStackPowerMode"),
        ("CISCO-STACKWISE-MIB", "cswStackPowerMasterMacAddress"),
        ("CISCO-STACKWISE-MIB", "cswStackPowerMasterSwitchNum"),
        ("CISCO-STACKWISE-MIB", "cswStackPowerNumMembers"),
        ("CISCO-STACKWISE-MIB", "cswStackPowerType"),
        ("CISCO-STACKWISE-MIB", "cswStackPowerName"))
)
if mibBuilder.loadTexts:
    cswStackPowerStatusGroup.setStatus("current")

cswStackPowerSwitchStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 500, 2, 2, 5)
)
cswStackPowerSwitchStatusGroup.setObjects(
      *(("CISCO-STACKWISE-MIB", "cswSwitchPowerBudget"),
        ("CISCO-STACKWISE-MIB", "cswSwitchPowerCommited"),
        ("CISCO-STACKWISE-MIB", "cswSwitchSystemPowerPriority"),
        ("CISCO-STACKWISE-MIB", "cswSwitchPoeDevicesLowPriority"),
        ("CISCO-STACKWISE-MIB", "cswSwitchPoeDevicesHighPriority"))
)
if mibBuilder.loadTexts:
    cswStackPowerSwitchStatusGroup.setStatus("current")

cswStackPowerPortStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 500, 2, 2, 6)
)
cswStackPowerPortStatusGroup.setObjects(
      *(("CISCO-STACKWISE-MIB", "cswStackPowerPortOperStatus"),
        ("CISCO-STACKWISE-MIB", "cswStackPowerPortNeighborMacAddress"),
        ("CISCO-STACKWISE-MIB", "cswStackPowerPortNeighborSwitchNum"),
        ("CISCO-STACKWISE-MIB", "cswStackPowerPortLinkStatus"),
        ("CISCO-STACKWISE-MIB", "cswStackPowerPortOverCurrentThreshold"),
        ("CISCO-STACKWISE-MIB", "cswStackPowerPortName"))
)
if mibBuilder.loadTexts:
    cswStackPowerPortStatusGroup.setStatus("current")

cswStackPowerEnableNotificationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 500, 2, 2, 8)
)
cswStackPowerEnableNotificationGroup.setObjects(
    ("CISCO-STACKWISE-MIB", "cswEnableIndividualStackNotifications")
)
if mibBuilder.loadTexts:
    cswStackPowerEnableNotificationGroup.setStatus("current")

cswStackPowerAllocatedGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 500, 2, 2, 10)
)
cswStackPowerAllocatedGroup.setObjects(
    ("CISCO-STACKWISE-MIB", "cswSwitchPowerAllocated")
)
if mibBuilder.loadTexts:
    cswStackPowerAllocatedGroup.setStatus("current")

cswStatusGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 500, 2, 2, 11)
)
cswStatusGroupRev2.setObjects(
      *(("CISCO-STACKWISE-MIB", "cswMaxSwitchNum"),
        ("CISCO-STACKWISE-MIB", "cswMaxSwitchConfigPriority"),
        ("CISCO-STACKWISE-MIB", "cswRingRedundant"),
        ("CISCO-STACKWISE-MIB", "cswSwitchNumCurrent"),
        ("CISCO-STACKWISE-MIB", "cswSwitchNumNextReload"),
        ("CISCO-STACKWISE-MIB", "cswSwitchRole"),
        ("CISCO-STACKWISE-MIB", "cswSwitchSwPriority"),
        ("CISCO-STACKWISE-MIB", "cswSwitchHwPriority"),
        ("CISCO-STACKWISE-MIB", "cswSwitchState"),
        ("CISCO-STACKWISE-MIB", "cswSwitchMacAddress"),
        ("CISCO-STACKWISE-MIB", "cswStackDomainNum"),
        ("CISCO-STACKWISE-MIB", "cswStackType"),
        ("CISCO-STACKWISE-MIB", "cswStackBandWidth"))
)
if mibBuilder.loadTexts:
    cswStatusGroupRev2.setStatus("current")

cswDistrStackLinkStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 500, 2, 2, 12)
)
cswDistrStackLinkStatusGroup.setObjects(
    ("CISCO-STACKWISE-MIB", "cswDistrStackLinkBundleOperStatus")
)
if mibBuilder.loadTexts:
    cswDistrStackLinkStatusGroup.setStatus("current")

cswDistrStackPhyPortStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 500, 2, 2, 13)
)
cswDistrStackPhyPortStatusGroup.setObjects(
      *(("CISCO-STACKWISE-MIB", "cswDistrStackPhyPort"),
        ("CISCO-STACKWISE-MIB", "cswDistrStackPhyPortOperStatus"),
        ("CISCO-STACKWISE-MIB", "cswDistrStackPhyPortNbr"),
        ("CISCO-STACKWISE-MIB", "cswDistrStackPhyPortNbrsw"))
)
if mibBuilder.loadTexts:
    cswDistrStackPhyPortStatusGroup.setStatus("current")


# Notification objects

cswStackPortChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 500, 0, 0, 1)
)
cswStackPortChange.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CISCO-STACKWISE-MIB", "cswStackPortOperStatus"),
        ("CISCO-STACKWISE-MIB", "cswSwitchNumCurrent"))
)
if mibBuilder.loadTexts:
    cswStackPortChange.setStatus(
        "current"
    )

cswStackNewMaster = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 500, 0, 0, 2)
)
cswStackNewMaster.setObjects(
    ("CISCO-STACKWISE-MIB", "cswSwitchNumCurrent")
)
if mibBuilder.loadTexts:
    cswStackNewMaster.setStatus(
        "current"
    )

cswStackMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 500, 0, 0, 3)
)
cswStackMismatch.setObjects(
      *(("CISCO-STACKWISE-MIB", "cswSwitchState"),
        ("CISCO-STACKWISE-MIB", "cswSwitchNumCurrent"))
)
if mibBuilder.loadTexts:
    cswStackMismatch.setStatus(
        "current"
    )

cswStackRingRedundant = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 500, 0, 0, 4)
)
cswStackRingRedundant.setObjects(
    ("CISCO-STACKWISE-MIB", "cswRingRedundant")
)
if mibBuilder.loadTexts:
    cswStackRingRedundant.setStatus(
        "current"
    )

cswStackNewMember = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 500, 0, 0, 5)
)
cswStackNewMember.setObjects(
    ("CISCO-STACKWISE-MIB", "cswSwitchNumCurrent")
)
if mibBuilder.loadTexts:
    cswStackNewMember.setStatus(
        "current"
    )

cswStackMemberRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 500, 0, 0, 6)
)
cswStackMemberRemoved.setObjects(
    ("CISCO-STACKWISE-MIB", "cswSwitchNumCurrent")
)
if mibBuilder.loadTexts:
    cswStackMemberRemoved.setStatus(
        "current"
    )

cswStackPowerPortLinkStatusChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 500, 0, 0, 7)
)
cswStackPowerPortLinkStatusChanged.setObjects(
      *(("CISCO-STACKWISE-MIB", "cswStackPowerPortLinkStatus"),
        ("CISCO-STACKWISE-MIB", "cswSwitchNumCurrent"),
        ("CISCO-STACKWISE-MIB", "cswStackPowerPortName"))
)
if mibBuilder.loadTexts:
    cswStackPowerPortLinkStatusChanged.setStatus(
        "current"
    )

cswStackPowerPortOperStatusChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 500, 0, 0, 8)
)
cswStackPowerPortOperStatusChanged.setObjects(
      *(("CISCO-STACKWISE-MIB", "cswSwitchNumCurrent"),
        ("CISCO-STACKWISE-MIB", "cswStackPowerPortOperStatus"),
        ("CISCO-STACKWISE-MIB", "cswStackPowerPortName"))
)
if mibBuilder.loadTexts:
    cswStackPowerPortOperStatusChanged.setStatus(
        "current"
    )

cswStackPowerVersionMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 500, 0, 0, 9)
)
cswStackPowerVersionMismatch.setObjects(
    ("CISCO-STACKWISE-MIB", "cswSwitchNumCurrent")
)
if mibBuilder.loadTexts:
    cswStackPowerVersionMismatch.setStatus(
        "current"
    )

cswStackPowerInvalidTopology = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 500, 0, 0, 10)
)
cswStackPowerInvalidTopology.setObjects(
    ("CISCO-STACKWISE-MIB", "cswSwitchNumCurrent")
)
if mibBuilder.loadTexts:
    cswStackPowerInvalidTopology.setStatus(
        "current"
    )

cscwStackPowerBudgetWarrning = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 500, 0, 0, 11)
)
cscwStackPowerBudgetWarrning.setObjects(
    ("CISCO-STACKWISE-MIB", "cswSwitchNumCurrent")
)
if mibBuilder.loadTexts:
    cscwStackPowerBudgetWarrning.setStatus(
        "current"
    )

cswStackPowerInvalidInputCurrent = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 500, 0, 0, 12)
)
cswStackPowerInvalidInputCurrent.setObjects(
      *(("CISCO-STACKWISE-MIB", "cswSwitchNumCurrent"),
        ("CISCO-STACKWISE-MIB", "cswStackPowerPortOverCurrentThreshold"),
        ("CISCO-STACKWISE-MIB", "cswStackPowerPortName"))
)
if mibBuilder.loadTexts:
    cswStackPowerInvalidInputCurrent.setStatus(
        "current"
    )

cswStackPowerInvalidOutputCurrent = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 500, 0, 0, 13)
)
cswStackPowerInvalidOutputCurrent.setObjects(
      *(("CISCO-STACKWISE-MIB", "cswSwitchNumCurrent"),
        ("CISCO-STACKWISE-MIB", "cswStackPowerPortOverCurrentThreshold"),
        ("CISCO-STACKWISE-MIB", "cswStackPowerPortName"))
)
if mibBuilder.loadTexts:
    cswStackPowerInvalidOutputCurrent.setStatus(
        "current"
    )

cswStackPowerUnderBudget = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 500, 0, 0, 14)
)
cswStackPowerUnderBudget.setObjects(
    ("CISCO-STACKWISE-MIB", "cswSwitchNumCurrent")
)
if mibBuilder.loadTexts:
    cswStackPowerUnderBudget.setStatus(
        "current"
    )

cswStackPowerUnbalancedPowerSupplies = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 500, 0, 0, 15)
)
cswStackPowerUnbalancedPowerSupplies.setObjects(
    ("CISCO-STACKWISE-MIB", "cswStackPowerName")
)
if mibBuilder.loadTexts:
    cswStackPowerUnbalancedPowerSupplies.setStatus(
        "current"
    )

cswStackPowerInsufficientPower = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 500, 0, 0, 16)
)
cswStackPowerInsufficientPower.setObjects(
    ("CISCO-STACKWISE-MIB", "cswStackPowerName")
)
if mibBuilder.loadTexts:
    cswStackPowerInsufficientPower.setStatus(
        "current"
    )

cswStackPowerPriorityConflict = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 500, 0, 0, 17)
)
cswStackPowerPriorityConflict.setObjects(
    ("CISCO-STACKWISE-MIB", "cswStackPowerName")
)
if mibBuilder.loadTexts:
    cswStackPowerPriorityConflict.setStatus(
        "current"
    )

cswStackPowerUnderVoltage = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 500, 0, 0, 18)
)
cswStackPowerUnderVoltage.setObjects(
    ("CISCO-STACKWISE-MIB", "cswSwitchNumCurrent")
)
if mibBuilder.loadTexts:
    cswStackPowerUnderVoltage.setStatus(
        "current"
    )

cswStackPowerGLS = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 500, 0, 0, 19)
)
cswStackPowerGLS.setObjects(
    ("CISCO-STACKWISE-MIB", "cswSwitchNumCurrent")
)
if mibBuilder.loadTexts:
    cswStackPowerGLS.setStatus(
        "current"
    )

cswStackPowerILS = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 500, 0, 0, 20)
)
cswStackPowerILS.setObjects(
    ("CISCO-STACKWISE-MIB", "cswSwitchNumCurrent")
)
if mibBuilder.loadTexts:
    cswStackPowerILS.setStatus(
        "current"
    )

cswStackPowerSRLS = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 500, 0, 0, 21)
)
cswStackPowerSRLS.setObjects(
    ("CISCO-STACKWISE-MIB", "cswSwitchNumCurrent")
)
if mibBuilder.loadTexts:
    cswStackPowerSRLS.setStatus(
        "current"
    )

cswStackPowerSSLS = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 500, 0, 0, 22)
)
cswStackPowerSSLS.setObjects(
    ("CISCO-STACKWISE-MIB", "cswSwitchNumCurrent")
)
if mibBuilder.loadTexts:
    cswStackPowerSSLS.setStatus(
        "current"
    )

cswStackMemberToBeReloadedForUpgrade = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 500, 0, 0, 23)
)
cswStackMemberToBeReloadedForUpgrade.setObjects(
    ("CISCO-STACKWISE-MIB", "cswSwitchNumCurrent")
)
if mibBuilder.loadTexts:
    cswStackMemberToBeReloadedForUpgrade.setStatus(
        "current"
    )


# Notifications groups

cswNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 500, 2, 2, 2)
)
cswNotificationGroup.setObjects(
      *(("CISCO-STACKWISE-MIB", "cswStackPortChange"),
        ("CISCO-STACKWISE-MIB", "cswStackNewMaster"),
        ("CISCO-STACKWISE-MIB", "cswStackMismatch"),
        ("CISCO-STACKWISE-MIB", "cswStackRingRedundant"),
        ("CISCO-STACKWISE-MIB", "cswStackNewMember"),
        ("CISCO-STACKWISE-MIB", "cswStackMemberRemoved"))
)
if mibBuilder.loadTexts:
    cswNotificationGroup.setStatus(
        "current"
    )

cswStackPowerNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 500, 2, 2, 7)
)
cswStackPowerNotificationGroup.setObjects(
      *(("CISCO-STACKWISE-MIB", "cswStackPowerPortLinkStatusChanged"),
        ("CISCO-STACKWISE-MIB", "cswStackPowerPortOperStatusChanged"),
        ("CISCO-STACKWISE-MIB", "cswStackPowerVersionMismatch"),
        ("CISCO-STACKWISE-MIB", "cswStackPowerInvalidTopology"),
        ("CISCO-STACKWISE-MIB", "cscwStackPowerBudgetWarrning"),
        ("CISCO-STACKWISE-MIB", "cswStackPowerInvalidInputCurrent"),
        ("CISCO-STACKWISE-MIB", "cswStackPowerInvalidOutputCurrent"),
        ("CISCO-STACKWISE-MIB", "cswStackPowerUnderBudget"),
        ("CISCO-STACKWISE-MIB", "cswStackPowerUnbalancedPowerSupplies"),
        ("CISCO-STACKWISE-MIB", "cswStackPowerInsufficientPower"),
        ("CISCO-STACKWISE-MIB", "cswStackPowerPriorityConflict"),
        ("CISCO-STACKWISE-MIB", "cswStackPowerUnderVoltage"),
        ("CISCO-STACKWISE-MIB", "cswStackPowerGLS"),
        ("CISCO-STACKWISE-MIB", "cswStackPowerILS"),
        ("CISCO-STACKWISE-MIB", "cswStackPowerSRLS"),
        ("CISCO-STACKWISE-MIB", "cswStackPowerSSLS"))
)
if mibBuilder.loadTexts:
    cswStackPowerNotificationGroup.setStatus(
        "current"
    )

cswNotificationGroupSup1 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 500, 2, 2, 9)
)
cswNotificationGroupSup1.setObjects(
    ("CISCO-STACKWISE-MIB", "cswStackMemberToBeReloadedForUpgrade")
)
if mibBuilder.loadTexts:
    cswNotificationGroupSup1.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

cswStackWiseMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 500, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cswStackWiseMIBCompliance.setStatus(
        "deprecated"
    )

cswStackWiseMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 500, 2, 1, 2)
)
if mibBuilder.loadTexts:
    cswStackWiseMIBComplianceRev1.setStatus(
        "deprecated"
    )

cswStackWiseMIBComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 500, 2, 1, 3)
)
if mibBuilder.loadTexts:
    cswStackWiseMIBComplianceRev2.setStatus(
        "deprecated"
    )

cswStackWiseMIBComplianceRev3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 500, 2, 1, 4)
)
if mibBuilder.loadTexts:
    cswStackWiseMIBComplianceRev3.setStatus(
        "deprecated"
    )

cswStackWiseMIBComplianceRev4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 500, 2, 1, 5)
)
if mibBuilder.loadTexts:
    cswStackWiseMIBComplianceRev4.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-STACKWISE-MIB",
    **{"CswPowerStackMode": CswPowerStackMode,
       "CswPowerStackType": CswPowerStackType,
       "CswSwitchNumber": CswSwitchNumber,
       "CswSwitchNumberOrZero": CswSwitchNumberOrZero,
       "CswSwitchPriority": CswSwitchPriority,
       "ciscoStackWiseMIB": ciscoStackWiseMIB,
       "ciscoStackWiseMIBNotifs": ciscoStackWiseMIBNotifs,
       "cswMIBNotifications": cswMIBNotifications,
       "cswStackPortChange": cswStackPortChange,
       "cswStackNewMaster": cswStackNewMaster,
       "cswStackMismatch": cswStackMismatch,
       "cswStackRingRedundant": cswStackRingRedundant,
       "cswStackNewMember": cswStackNewMember,
       "cswStackMemberRemoved": cswStackMemberRemoved,
       "cswStackPowerPortLinkStatusChanged": cswStackPowerPortLinkStatusChanged,
       "cswStackPowerPortOperStatusChanged": cswStackPowerPortOperStatusChanged,
       "cswStackPowerVersionMismatch": cswStackPowerVersionMismatch,
       "cswStackPowerInvalidTopology": cswStackPowerInvalidTopology,
       "cscwStackPowerBudgetWarrning": cscwStackPowerBudgetWarrning,
       "cswStackPowerInvalidInputCurrent": cswStackPowerInvalidInputCurrent,
       "cswStackPowerInvalidOutputCurrent": cswStackPowerInvalidOutputCurrent,
       "cswStackPowerUnderBudget": cswStackPowerUnderBudget,
       "cswStackPowerUnbalancedPowerSupplies": cswStackPowerUnbalancedPowerSupplies,
       "cswStackPowerInsufficientPower": cswStackPowerInsufficientPower,
       "cswStackPowerPriorityConflict": cswStackPowerPriorityConflict,
       "cswStackPowerUnderVoltage": cswStackPowerUnderVoltage,
       "cswStackPowerGLS": cswStackPowerGLS,
       "cswStackPowerILS": cswStackPowerILS,
       "cswStackPowerSRLS": cswStackPowerSRLS,
       "cswStackPowerSSLS": cswStackPowerSSLS,
       "cswStackMemberToBeReloadedForUpgrade": cswStackMemberToBeReloadedForUpgrade,
       "ciscoStackWiseMIBObjects": ciscoStackWiseMIBObjects,
       "cswGlobals": cswGlobals,
       "cswMaxSwitchNum": cswMaxSwitchNum,
       "cswMaxSwitchConfigPriority": cswMaxSwitchConfigPriority,
       "cswRingRedundant": cswRingRedundant,
       "cswEnableStackNotifications": cswEnableStackNotifications,
       "cswEnableIndividualStackNotifications": cswEnableIndividualStackNotifications,
       "cswStackDomainNum": cswStackDomainNum,
       "cswStackType": cswStackType,
       "cswStackBandWidth": cswStackBandWidth,
       "cswStackInfo": cswStackInfo,
       "cswSwitchInfoTable": cswSwitchInfoTable,
       "cswSwitchInfoEntry": cswSwitchInfoEntry,
       "cswSwitchNumCurrent": cswSwitchNumCurrent,
       "cswSwitchNumNextReload": cswSwitchNumNextReload,
       "cswSwitchRole": cswSwitchRole,
       "cswSwitchSwPriority": cswSwitchSwPriority,
       "cswSwitchHwPriority": cswSwitchHwPriority,
       "cswSwitchState": cswSwitchState,
       "cswSwitchMacAddress": cswSwitchMacAddress,
       "cswSwitchSoftwareImage": cswSwitchSoftwareImage,
       "cswSwitchPowerBudget": cswSwitchPowerBudget,
       "cswSwitchPowerCommited": cswSwitchPowerCommited,
       "cswSwitchSystemPowerPriority": cswSwitchSystemPowerPriority,
       "cswSwitchPoeDevicesLowPriority": cswSwitchPoeDevicesLowPriority,
       "cswSwitchPoeDevicesHighPriority": cswSwitchPoeDevicesHighPriority,
       "cswSwitchPowerAllocated": cswSwitchPowerAllocated,
       "cswStackPortInfoTable": cswStackPortInfoTable,
       "cswStackPortInfoEntry": cswStackPortInfoEntry,
       "cswStackPortOperStatus": cswStackPortOperStatus,
       "cswStackPortNeighbor": cswStackPortNeighbor,
       "cswDistrStackLinkInfoTable": cswDistrStackLinkInfoTable,
       "cswDistrStackLinkInfoEntry": cswDistrStackLinkInfoEntry,
       "cswDSLindex": cswDSLindex,
       "cswDistrStackLinkBundleOperStatus": cswDistrStackLinkBundleOperStatus,
       "cswDistrStackPhyPortInfoTable": cswDistrStackPhyPortInfoTable,
       "cswDistrStackPhyPortInfoEntry": cswDistrStackPhyPortInfoEntry,
       "cswDistrStackPhyPort": cswDistrStackPhyPort,
       "cswDistrStackPhyPortOperStatus": cswDistrStackPhyPortOperStatus,
       "cswDistrStackPhyPortNbr": cswDistrStackPhyPortNbr,
       "cswDistrStackPhyPortNbrsw": cswDistrStackPhyPortNbrsw,
       "cswStackPowerInfo": cswStackPowerInfo,
       "cswStackPowerInfoTable": cswStackPowerInfoTable,
       "cswStackPowerInfoEntry": cswStackPowerInfoEntry,
       "cswStackPowerStackNumber": cswStackPowerStackNumber,
       "cswStackPowerMode": cswStackPowerMode,
       "cswStackPowerMasterMacAddress": cswStackPowerMasterMacAddress,
       "cswStackPowerMasterSwitchNum": cswStackPowerMasterSwitchNum,
       "cswStackPowerNumMembers": cswStackPowerNumMembers,
       "cswStackPowerType": cswStackPowerType,
       "cswStackPowerName": cswStackPowerName,
       "cswStackPowerPortInfoTable": cswStackPowerPortInfoTable,
       "cswStackPowerPortInfoEntry": cswStackPowerPortInfoEntry,
       "cswStackPowerPortIndex": cswStackPowerPortIndex,
       "cswStackPowerPortOperStatus": cswStackPowerPortOperStatus,
       "cswStackPowerPortNeighborMacAddress": cswStackPowerPortNeighborMacAddress,
       "cswStackPowerPortNeighborSwitchNum": cswStackPowerPortNeighborSwitchNum,
       "cswStackPowerPortLinkStatus": cswStackPowerPortLinkStatus,
       "cswStackPowerPortOverCurrentThreshold": cswStackPowerPortOverCurrentThreshold,
       "cswStackPowerPortName": cswStackPowerPortName,
       "ciscoStackWiseMIBConform": ciscoStackWiseMIBConform,
       "cswStackWiseMIBCompliances": cswStackWiseMIBCompliances,
       "cswStackWiseMIBCompliance": cswStackWiseMIBCompliance,
       "cswStackWiseMIBComplianceRev1": cswStackWiseMIBComplianceRev1,
       "cswStackWiseMIBComplianceRev2": cswStackWiseMIBComplianceRev2,
       "cswStackWiseMIBComplianceRev3": cswStackWiseMIBComplianceRev3,
       "cswStackWiseMIBComplianceRev4": cswStackWiseMIBComplianceRev4,
       "cswStackWiseMIBGroups": cswStackWiseMIBGroups,
       "cswStatusGroup": cswStatusGroup,
       "cswNotificationGroup": cswNotificationGroup,
       "cswStatusGroupRev1": cswStatusGroupRev1,
       "cswStackPowerStatusGroup": cswStackPowerStatusGroup,
       "cswStackPowerSwitchStatusGroup": cswStackPowerSwitchStatusGroup,
       "cswStackPowerPortStatusGroup": cswStackPowerPortStatusGroup,
       "cswStackPowerNotificationGroup": cswStackPowerNotificationGroup,
       "cswStackPowerEnableNotificationGroup": cswStackPowerEnableNotificationGroup,
       "cswNotificationGroupSup1": cswNotificationGroupSup1,
       "cswStackPowerAllocatedGroup": cswStackPowerAllocatedGroup,
       "cswStatusGroupRev2": cswStatusGroupRev2,
       "cswDistrStackLinkStatusGroup": cswDistrStackLinkStatusGroup,
       "cswDistrStackPhyPortStatusGroup": cswDistrStackPhyPortStatusGroup}
)
