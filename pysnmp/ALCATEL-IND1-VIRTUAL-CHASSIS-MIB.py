# SNMP MIB module (ALCATEL-IND1-VIRTUAL-CHASSIS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALCATEL-IND1-VIRTUAL-CHASSIS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:37:31 2024
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

(softentIND1VirtualChassisManager,) = mibBuilder.importSymbols(
    "ALCATEL-IND1-BASE",
    "softentIND1VirtualChassisManager")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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

alcatelIND1VirtualChassisMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1)
)
alcatelIND1VirtualChassisMIB.setRevisions(
        ("2011-05-25 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class VirtualOperChassisId(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class VirtualConfigChassisId(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )



class VirtualChassisHelloInterval(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class VirtualChassisControlVlan(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 4094),
    )



class VirtualChassisCmmSlot(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              65,
              66)
        )
    )
    namedValues = NamedValues(
        *(("cmmSlot1", 65),
          ("cmmSlot2", 66),
          ("notPresent", 0))
    )



class VirtualChassisNiSlot(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )



class VirtualChassisVflId(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )



class VirtualChassisConsistency(Integer32, TextualConvention):
    status = "current"
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
        *(("consistent", 1),
          ("disabled", 3),
          ("inconsistent", 0),
          ("na", 2))
    )



class VirtualChassisRole(Integer32, TextualConvention):
    status = "current"
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
        *(("inconsistent", 3),
          ("master", 1),
          ("slave", 2),
          ("startuperror", 4),
          ("unassigned", 0))
    )



class VirtualChassisStatus(Integer32, TextualConvention):
    status = "current"
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
              11,
              12,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("commandShutdown", 13),
          ("duplicateChassisId", 4),
          ("failureShutdown", 14),
          ("helloDown", 3),
          ("init", 0),
          ("invalidChassisId", 2),
          ("invalidLicense", 11),
          ("mismatchChassisType", 6),
          ("mismatchControlVlan", 8),
          ("mismatchGroup", 9),
          ("mismatchHelloInterval", 7),
          ("mismatchImage", 5),
          ("mismatchLicenseConfig", 10),
          ("running", 1),
          ("splitTopology", 12))
    )



class VirtualChassisGroup(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class VirtualChassisPriority(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class VirtualChassisSlotResetStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("split", 1),
          ("supported", 0))
    )



class VirtualChassisType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("rushmore", 1),
          ("tor", 2))
    )



class VirtualChassisVflSpeedType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("fortyGB", 4),
          ("mismatch", 2),
          ("tenGB", 3),
          ("twentyOneGB", 5),
          ("unassigned", 0),
          ("unknown", 1))
    )



# MIB Managed Objects in the order of their OIDs

_AlcatelIND1VirtualChassisMIBNotifications_ObjectIdentity = ObjectIdentity
alcatelIND1VirtualChassisMIBNotifications = _AlcatelIND1VirtualChassisMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 0)
)
if mibBuilder.loadTexts:
    alcatelIND1VirtualChassisMIBNotifications.setStatus("current")
_AlcatelIND1VirtualChassisMIBObjects_ObjectIdentity = ObjectIdentity
alcatelIND1VirtualChassisMIBObjects = _AlcatelIND1VirtualChassisMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1VirtualChassisMIBObjects.setStatus("current")
_VirtualChassisLocalInfo_ObjectIdentity = ObjectIdentity
virtualChassisLocalInfo = _VirtualChassisLocalInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 1)
)
_VirtualChassisLocalInfoChasId_Type = VirtualOperChassisId
_VirtualChassisLocalInfoChasId_Object = MibScalar
virtualChassisLocalInfoChasId = _VirtualChassisLocalInfoChasId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 1, 1),
    _VirtualChassisLocalInfoChasId_Type()
)
virtualChassisLocalInfoChasId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualChassisLocalInfoChasId.setStatus("current")
_VirtualChassisGlobalTable_Object = MibTable
virtualChassisGlobalTable = _VirtualChassisGlobalTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 2)
)
if mibBuilder.loadTexts:
    virtualChassisGlobalTable.setStatus("current")
_VirtualChassisGlobalEntry_Object = MibTableRow
virtualChassisGlobalEntry = _VirtualChassisGlobalEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 2, 1)
)
virtualChassisGlobalEntry.setIndexNames(
    (0, "ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisOperChasId"),
)
if mibBuilder.loadTexts:
    virtualChassisGlobalEntry.setStatus("current")
_VirtualChassisOperChasId_Type = VirtualOperChassisId
_VirtualChassisOperChasId_Object = MibTableColumn
virtualChassisOperChasId = _VirtualChassisOperChasId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 2, 1, 1),
    _VirtualChassisOperChasId_Type()
)
virtualChassisOperChasId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    virtualChassisOperChasId.setStatus("current")


class _VirtualChassisConfigChassisId_Type(VirtualConfigChassisId):
    """Custom type virtualChassisConfigChassisId based on VirtualConfigChassisId"""
    defaultValue = 0


_VirtualChassisConfigChassisId_Object = MibTableColumn
virtualChassisConfigChassisId = _VirtualChassisConfigChassisId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 2, 1, 2),
    _VirtualChassisConfigChassisId_Type()
)
virtualChassisConfigChassisId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    virtualChassisConfigChassisId.setStatus("current")
_VirtualChassisRole_Type = VirtualChassisRole
_VirtualChassisRole_Object = MibTableColumn
virtualChassisRole = _VirtualChassisRole_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 2, 1, 3),
    _VirtualChassisRole_Type()
)
virtualChassisRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualChassisRole.setStatus("current")
_VirtualChassisPreviousRole_Type = VirtualChassisRole
_VirtualChassisPreviousRole_Object = MibTableColumn
virtualChassisPreviousRole = _VirtualChassisPreviousRole_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 2, 1, 4),
    _VirtualChassisPreviousRole_Type()
)
virtualChassisPreviousRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualChassisPreviousRole.setStatus("current")
_VirtualChassisStatus_Type = VirtualChassisStatus
_VirtualChassisStatus_Object = MibTableColumn
virtualChassisStatus = _VirtualChassisStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 2, 1, 5),
    _VirtualChassisStatus_Type()
)
virtualChassisStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualChassisStatus.setStatus("current")
_VirtualChassisOperPriority_Type = VirtualChassisPriority
_VirtualChassisOperPriority_Object = MibTableColumn
virtualChassisOperPriority = _VirtualChassisOperPriority_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 2, 1, 6),
    _VirtualChassisOperPriority_Type()
)
virtualChassisOperPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualChassisOperPriority.setStatus("current")


class _VirtualChassisConfigPriority_Type(VirtualChassisPriority):
    """Custom type virtualChassisConfigPriority based on VirtualChassisPriority"""
    defaultValue = 100


_VirtualChassisConfigPriority_Object = MibTableColumn
virtualChassisConfigPriority = _VirtualChassisConfigPriority_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 2, 1, 7),
    _VirtualChassisConfigPriority_Type()
)
virtualChassisConfigPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    virtualChassisConfigPriority.setStatus("current")


class _VirtualChassisGroup_Type(VirtualChassisGroup):
    """Custom type virtualChassisGroup based on VirtualChassisGroup"""
    defaultValue = 0


_VirtualChassisGroup_Object = MibTableColumn
virtualChassisGroup = _VirtualChassisGroup_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 2, 1, 8),
    _VirtualChassisGroup_Type()
)
virtualChassisGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    virtualChassisGroup.setStatus("current")
_VirtualChassisMac_Type = MacAddress
_VirtualChassisMac_Object = MibTableColumn
virtualChassisMac = _VirtualChassisMac_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 2, 1, 9),
    _VirtualChassisMac_Type()
)
virtualChassisMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualChassisMac.setStatus("current")
_VirtualChassisUpTime_Type = TimeTicks
_VirtualChassisUpTime_Object = MibTableColumn
virtualChassisUpTime = _VirtualChassisUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 2, 1, 10),
    _VirtualChassisUpTime_Type()
)
virtualChassisUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualChassisUpTime.setStatus("current")
_VirtualChassisDesigNI_Type = VirtualChassisNiSlot
_VirtualChassisDesigNI_Object = MibTableColumn
virtualChassisDesigNI = _VirtualChassisDesigNI_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 2, 1, 11),
    _VirtualChassisDesigNI_Type()
)
virtualChassisDesigNI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualChassisDesigNI.setStatus("current")
_VirtualChassisPriCmm_Type = VirtualChassisCmmSlot
_VirtualChassisPriCmm_Object = MibTableColumn
virtualChassisPriCmm = _VirtualChassisPriCmm_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 2, 1, 12),
    _VirtualChassisPriCmm_Type()
)
virtualChassisPriCmm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualChassisPriCmm.setStatus("current")
_VirtualChassisSecCmm_Type = VirtualChassisCmmSlot
_VirtualChassisSecCmm_Object = MibTableColumn
virtualChassisSecCmm = _VirtualChassisSecCmm_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 2, 1, 13),
    _VirtualChassisSecCmm_Type()
)
virtualChassisSecCmm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualChassisSecCmm.setStatus("current")


class _VirtualChassisOperHelloInterval_Type(VirtualChassisHelloInterval):
    """Custom type virtualChassisOperHelloInterval based on VirtualChassisHelloInterval"""
    defaultValue = 10


_VirtualChassisOperHelloInterval_Object = MibTableColumn
virtualChassisOperHelloInterval = _VirtualChassisOperHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 2, 1, 14),
    _VirtualChassisOperHelloInterval_Type()
)
virtualChassisOperHelloInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    virtualChassisOperHelloInterval.setStatus("current")
if mibBuilder.loadTexts:
    virtualChassisOperHelloInterval.setUnits("seconds")
_VirtualChassisOperControlVlan_Type = VirtualChassisControlVlan
_VirtualChassisOperControlVlan_Object = MibTableColumn
virtualChassisOperControlVlan = _VirtualChassisOperControlVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 2, 1, 15),
    _VirtualChassisOperControlVlan_Type()
)
virtualChassisOperControlVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualChassisOperControlVlan.setStatus("current")


class _VirtualChassisConfigHelloInterval_Type(VirtualChassisHelloInterval):
    """Custom type virtualChassisConfigHelloInterval based on VirtualChassisHelloInterval"""
    defaultValue = 2


_VirtualChassisConfigHelloInterval_Object = MibTableColumn
virtualChassisConfigHelloInterval = _VirtualChassisConfigHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 2, 1, 16),
    _VirtualChassisConfigHelloInterval_Type()
)
virtualChassisConfigHelloInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    virtualChassisConfigHelloInterval.setStatus("deprecated")
if mibBuilder.loadTexts:
    virtualChassisConfigHelloInterval.setUnits("seconds")


class _VirtualChassisConfigControlVlan_Type(VirtualChassisControlVlan):
    """Custom type virtualChassisConfigControlVlan based on VirtualChassisControlVlan"""
    defaultValue = 4094


_VirtualChassisConfigControlVlan_Object = MibTableColumn
virtualChassisConfigControlVlan = _VirtualChassisConfigControlVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 2, 1, 17),
    _VirtualChassisConfigControlVlan_Type()
)
virtualChassisConfigControlVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    virtualChassisConfigControlVlan.setStatus("current")
_VirtualChassisType_Type = VirtualChassisType
_VirtualChassisType_Object = MibTableColumn
virtualChassisType = _VirtualChassisType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 2, 1, 18),
    _VirtualChassisType_Type()
)
virtualChassisType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualChassisType.setStatus("current")


class _VirtualChassisLicense_Type(SnmpAdminString):
    """Custom type virtualChassisLicense based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VirtualChassisLicense_Type.__name__ = "SnmpAdminString"
_VirtualChassisLicense_Object = MibTableColumn
virtualChassisLicense = _VirtualChassisLicense_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 2, 1, 19),
    _VirtualChassisLicense_Type()
)
virtualChassisLicense.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualChassisLicense.setStatus("current")
_VirtualChassisOperChasIdConsis_Type = VirtualChassisConsistency
_VirtualChassisOperChasIdConsis_Object = MibTableColumn
virtualChassisOperChasIdConsis = _VirtualChassisOperChasIdConsis_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 2, 1, 20),
    _VirtualChassisOperChasIdConsis_Type()
)
virtualChassisOperChasIdConsis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualChassisOperChasIdConsis.setStatus("current")
_VirtualChassisConfigChasIdConsis_Type = VirtualChassisConsistency
_VirtualChassisConfigChasIdConsis_Object = MibTableColumn
virtualChassisConfigChasIdConsis = _VirtualChassisConfigChasIdConsis_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 2, 1, 21),
    _VirtualChassisConfigChasIdConsis_Type()
)
virtualChassisConfigChasIdConsis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualChassisConfigChasIdConsis.setStatus("current")
_VirtualChassisOperControlVlanConsis_Type = VirtualChassisConsistency
_VirtualChassisOperControlVlanConsis_Object = MibTableColumn
virtualChassisOperControlVlanConsis = _VirtualChassisOperControlVlanConsis_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 2, 1, 22),
    _VirtualChassisOperControlVlanConsis_Type()
)
virtualChassisOperControlVlanConsis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualChassisOperControlVlanConsis.setStatus("current")
_VirtualChassisConfigControlVlanConsis_Type = VirtualChassisConsistency
_VirtualChassisConfigControlVlanConsis_Object = MibTableColumn
virtualChassisConfigControlVlanConsis = _VirtualChassisConfigControlVlanConsis_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 2, 1, 23),
    _VirtualChassisConfigControlVlanConsis_Type()
)
virtualChassisConfigControlVlanConsis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualChassisConfigControlVlanConsis.setStatus("current")
_VirtualChassisOperHelloIntervalConsis_Type = VirtualChassisConsistency
_VirtualChassisOperHelloIntervalConsis_Object = MibTableColumn
virtualChassisOperHelloIntervalConsis = _VirtualChassisOperHelloIntervalConsis_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 2, 1, 24),
    _VirtualChassisOperHelloIntervalConsis_Type()
)
virtualChassisOperHelloIntervalConsis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualChassisOperHelloIntervalConsis.setStatus("current")
_VirtualChassisConfigHelloIntervalConsis_Type = VirtualChassisConsistency
_VirtualChassisConfigHelloIntervalConsis_Object = MibTableColumn
virtualChassisConfigHelloIntervalConsis = _VirtualChassisConfigHelloIntervalConsis_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 2, 1, 25),
    _VirtualChassisConfigHelloIntervalConsis_Type()
)
virtualChassisConfigHelloIntervalConsis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualChassisConfigHelloIntervalConsis.setStatus("deprecated")
_VirtualChassisChassisTypeConsis_Type = VirtualChassisConsistency
_VirtualChassisChassisTypeConsis_Object = MibTableColumn
virtualChassisChassisTypeConsis = _VirtualChassisChassisTypeConsis_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 2, 1, 26),
    _VirtualChassisChassisTypeConsis_Type()
)
virtualChassisChassisTypeConsis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualChassisChassisTypeConsis.setStatus("current")
_VirtualChassisGroupConsis_Type = VirtualChassisConsistency
_VirtualChassisGroupConsis_Object = MibTableColumn
virtualChassisGroupConsis = _VirtualChassisGroupConsis_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 2, 1, 27),
    _VirtualChassisGroupConsis_Type()
)
virtualChassisGroupConsis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualChassisGroupConsis.setStatus("current")
_VirtualChassisLicenseConsis_Type = VirtualChassisConsistency
_VirtualChassisLicenseConsis_Object = MibTableColumn
virtualChassisLicenseConsis = _VirtualChassisLicenseConsis_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 2, 1, 28),
    _VirtualChassisLicenseConsis_Type()
)
virtualChassisLicenseConsis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualChassisLicenseConsis.setStatus("current")
_VirtualChassisGlobalConsis_Type = VirtualChassisConsistency
_VirtualChassisGlobalConsis_Object = MibTableColumn
virtualChassisGlobalConsis = _VirtualChassisGlobalConsis_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 2, 1, 29),
    _VirtualChassisGlobalConsis_Type()
)
virtualChassisGlobalConsis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualChassisGlobalConsis.setStatus("current")


class _VirtualChassisNumOfNeighbor_Type(Integer32):
    """Custom type virtualChassisNumOfNeighbor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VirtualChassisNumOfNeighbor_Type.__name__ = "Integer32"
_VirtualChassisNumOfNeighbor_Object = MibTableColumn
virtualChassisNumOfNeighbor = _VirtualChassisNumOfNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 2, 1, 30),
    _VirtualChassisNumOfNeighbor_Type()
)
virtualChassisNumOfNeighbor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualChassisNumOfNeighbor.setStatus("current")


class _VirtualChassisNumOfDirectNeighbor_Type(Integer32):
    """Custom type virtualChassisNumOfDirectNeighbor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VirtualChassisNumOfDirectNeighbor_Type.__name__ = "Integer32"
_VirtualChassisNumOfDirectNeighbor_Object = MibTableColumn
virtualChassisNumOfDirectNeighbor = _VirtualChassisNumOfDirectNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 2, 1, 31),
    _VirtualChassisNumOfDirectNeighbor_Type()
)
virtualChassisNumOfDirectNeighbor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualChassisNumOfDirectNeighbor.setStatus("current")
_VirtualChassisNeighborTable_Object = MibTable
virtualChassisNeighborTable = _VirtualChassisNeighborTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 3)
)
if mibBuilder.loadTexts:
    virtualChassisNeighborTable.setStatus("current")
_VirtualChassisNeighborEntry_Object = MibTableRow
virtualChassisNeighborEntry = _VirtualChassisNeighborEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 3, 1)
)
virtualChassisNeighborEntry.setIndexNames(
    (0, "ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisOperChasId"),
    (0, "ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisNeighborChasId"),
)
if mibBuilder.loadTexts:
    virtualChassisNeighborEntry.setStatus("current")
_VirtualChassisNeighborChasId_Type = VirtualOperChassisId
_VirtualChassisNeighborChasId_Object = MibTableColumn
virtualChassisNeighborChasId = _VirtualChassisNeighborChasId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 3, 1, 1),
    _VirtualChassisNeighborChasId_Type()
)
virtualChassisNeighborChasId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    virtualChassisNeighborChasId.setStatus("current")


class _VirtualChassisNeighborShortestPath_Type(SnmpAdminString):
    """Custom type virtualChassisNeighborShortestPath based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VirtualChassisNeighborShortestPath_Type.__name__ = "SnmpAdminString"
_VirtualChassisNeighborShortestPath_Object = MibTableColumn
virtualChassisNeighborShortestPath = _VirtualChassisNeighborShortestPath_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 3, 1, 2),
    _VirtualChassisNeighborShortestPath_Type()
)
virtualChassisNeighborShortestPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualChassisNeighborShortestPath.setStatus("current")
_VirtualChassisNeighborIsDirect_Type = TruthValue
_VirtualChassisNeighborIsDirect_Object = MibTableColumn
virtualChassisNeighborIsDirect = _VirtualChassisNeighborIsDirect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 3, 1, 3),
    _VirtualChassisNeighborIsDirect_Type()
)
virtualChassisNeighborIsDirect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualChassisNeighborIsDirect.setStatus("current")
_VirtualChassisChassisResetListTable_Object = MibTable
virtualChassisChassisResetListTable = _VirtualChassisChassisResetListTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 4)
)
if mibBuilder.loadTexts:
    virtualChassisChassisResetListTable.setStatus("current")
_VirtualChassisChassisResetListEntry_Object = MibTableRow
virtualChassisChassisResetListEntry = _VirtualChassisChassisResetListEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 4, 1)
)
virtualChassisChassisResetListEntry.setIndexNames(
    (0, "ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisOperChasId"),
)
if mibBuilder.loadTexts:
    virtualChassisChassisResetListEntry.setStatus("current")


class _VirtualChassisChassisResetList_Type(SnmpAdminString):
    """Custom type virtualChassisChassisResetList based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VirtualChassisChassisResetList_Type.__name__ = "SnmpAdminString"
_VirtualChassisChassisResetList_Object = MibTableColumn
virtualChassisChassisResetList = _VirtualChassisChassisResetList_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 4, 1, 1),
    _VirtualChassisChassisResetList_Type()
)
virtualChassisChassisResetList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualChassisChassisResetList.setStatus("current")
_VirtualChassisSlotResetStatusTable_Object = MibTable
virtualChassisSlotResetStatusTable = _VirtualChassisSlotResetStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 5)
)
if mibBuilder.loadTexts:
    virtualChassisSlotResetStatusTable.setStatus("current")
_VirtualChassisSlotResetStatusEntry_Object = MibTableRow
virtualChassisSlotResetStatusEntry = _VirtualChassisSlotResetStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 5, 1)
)
virtualChassisSlotResetStatusEntry.setIndexNames(
    (0, "ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisOperChasId"),
    (0, "ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisSlotNum"),
)
if mibBuilder.loadTexts:
    virtualChassisSlotResetStatusEntry.setStatus("current")
_VirtualChassisSlotNum_Type = VirtualChassisNiSlot
_VirtualChassisSlotNum_Object = MibTableColumn
virtualChassisSlotNum = _VirtualChassisSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 5, 1, 1),
    _VirtualChassisSlotNum_Type()
)
virtualChassisSlotNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    virtualChassisSlotNum.setStatus("current")
_VirtualChassisSlotResetStatus_Type = VirtualChassisSlotResetStatus
_VirtualChassisSlotResetStatus_Object = MibTableColumn
virtualChassisSlotResetStatus = _VirtualChassisSlotResetStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 5, 1, 2),
    _VirtualChassisSlotResetStatus_Type()
)
virtualChassisSlotResetStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualChassisSlotResetStatus.setStatus("current")
_VirtualChassisVflTable_Object = MibTable
virtualChassisVflTable = _VirtualChassisVflTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 6)
)
if mibBuilder.loadTexts:
    virtualChassisVflTable.setStatus("current")
_VirtualChassisVflEntry_Object = MibTableRow
virtualChassisVflEntry = _VirtualChassisVflEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 6, 1)
)
virtualChassisVflEntry.setIndexNames(
    (0, "ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisOperChasId"),
    (0, "ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisVflId"),
)
if mibBuilder.loadTexts:
    virtualChassisVflEntry.setStatus("current")
_VirtualChassisVflId_Type = VirtualChassisVflId
_VirtualChassisVflId_Object = MibTableColumn
virtualChassisVflId = _VirtualChassisVflId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 6, 1, 1),
    _VirtualChassisVflId_Type()
)
virtualChassisVflId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    virtualChassisVflId.setStatus("current")


class _VirtualChassisVflDefaultVlan_Type(Integer32):
    """Custom type virtualChassisVflDefaultVlan based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_VirtualChassisVflDefaultVlan_Type.__name__ = "Integer32"
_VirtualChassisVflDefaultVlan_Object = MibTableColumn
virtualChassisVflDefaultVlan = _VirtualChassisVflDefaultVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 6, 1, 2),
    _VirtualChassisVflDefaultVlan_Type()
)
virtualChassisVflDefaultVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    virtualChassisVflDefaultVlan.setStatus("current")


class _VirtualChassisVflOperStatus_Type(Integer32):
    """Custom type virtualChassisVflOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("down", 2),
          ("up", 1))
    )


_VirtualChassisVflOperStatus_Type.__name__ = "Integer32"
_VirtualChassisVflOperStatus_Object = MibTableColumn
virtualChassisVflOperStatus = _VirtualChassisVflOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 6, 1, 3),
    _VirtualChassisVflOperStatus_Type()
)
virtualChassisVflOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualChassisVflOperStatus.setStatus("current")
_VirtualChassisVflPrimaryPort_Type = InterfaceIndex
_VirtualChassisVflPrimaryPort_Object = MibTableColumn
virtualChassisVflPrimaryPort = _VirtualChassisVflPrimaryPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 6, 1, 4),
    _VirtualChassisVflPrimaryPort_Type()
)
virtualChassisVflPrimaryPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualChassisVflPrimaryPort.setStatus("current")


class _VirtualChassisVflActivePortNum_Type(Integer32):
    """Custom type virtualChassisVflActivePortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_VirtualChassisVflActivePortNum_Type.__name__ = "Integer32"
_VirtualChassisVflActivePortNum_Object = MibTableColumn
virtualChassisVflActivePortNum = _VirtualChassisVflActivePortNum_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 6, 1, 5),
    _VirtualChassisVflActivePortNum_Type()
)
virtualChassisVflActivePortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualChassisVflActivePortNum.setStatus("current")


class _VirtualChassisVflConfigPortNum_Type(Integer32):
    """Custom type virtualChassisVflConfigPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_VirtualChassisVflConfigPortNum_Type.__name__ = "Integer32"
_VirtualChassisVflConfigPortNum_Object = MibTableColumn
virtualChassisVflConfigPortNum = _VirtualChassisVflConfigPortNum_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 6, 1, 6),
    _VirtualChassisVflConfigPortNum_Type()
)
virtualChassisVflConfigPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualChassisVflConfigPortNum.setStatus("current")
_VirtualChassisVflRowStatus_Type = RowStatus
_VirtualChassisVflRowStatus_Object = MibTableColumn
virtualChassisVflRowStatus = _VirtualChassisVflRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 6, 1, 7),
    _VirtualChassisVflRowStatus_Type()
)
virtualChassisVflRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    virtualChassisVflRowStatus.setStatus("current")
_VirtualChassisVflDirectNeighborChasId_Type = VirtualOperChassisId
_VirtualChassisVflDirectNeighborChasId_Object = MibTableColumn
virtualChassisVflDirectNeighborChasId = _VirtualChassisVflDirectNeighborChasId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 6, 1, 8),
    _VirtualChassisVflDirectNeighborChasId_Type()
)
virtualChassisVflDirectNeighborChasId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualChassisVflDirectNeighborChasId.setStatus("current")
_VirtualChassisVflSpeedType_Type = VirtualChassisVflSpeedType
_VirtualChassisVflSpeedType_Object = MibTableColumn
virtualChassisVflSpeedType = _VirtualChassisVflSpeedType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 6, 1, 9),
    _VirtualChassisVflSpeedType_Type()
)
virtualChassisVflSpeedType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualChassisVflSpeedType.setStatus("current")
_VirtualChassisVflMemberPortTable_Object = MibTable
virtualChassisVflMemberPortTable = _VirtualChassisVflMemberPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 7)
)
if mibBuilder.loadTexts:
    virtualChassisVflMemberPortTable.setStatus("current")
_VirtualChassisVflMemberPortEntry_Object = MibTableRow
virtualChassisVflMemberPortEntry = _VirtualChassisVflMemberPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 7, 1)
)
virtualChassisVflMemberPortEntry.setIndexNames(
    (0, "ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisOperChasId"),
    (0, "ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisVflId"),
    (0, "ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisVflMemberPortIfindex"),
)
if mibBuilder.loadTexts:
    virtualChassisVflMemberPortEntry.setStatus("current")
_VirtualChassisVflMemberPortIfindex_Type = InterfaceIndex
_VirtualChassisVflMemberPortIfindex_Object = MibTableColumn
virtualChassisVflMemberPortIfindex = _VirtualChassisVflMemberPortIfindex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 7, 1, 1),
    _VirtualChassisVflMemberPortIfindex_Type()
)
virtualChassisVflMemberPortIfindex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    virtualChassisVflMemberPortIfindex.setStatus("current")
_VirtualChassisVflMemberPortIsPrimay_Type = TruthValue
_VirtualChassisVflMemberPortIsPrimay_Object = MibTableColumn
virtualChassisVflMemberPortIsPrimay = _VirtualChassisVflMemberPortIsPrimay_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 7, 1, 2),
    _VirtualChassisVflMemberPortIsPrimay_Type()
)
virtualChassisVflMemberPortIsPrimay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualChassisVflMemberPortIsPrimay.setStatus("current")


class _VirtualChassisVflMemberPortOperStatus_Type(Integer32):
    """Custom type virtualChassisVflMemberPortOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("down", 2),
          ("up", 1))
    )


_VirtualChassisVflMemberPortOperStatus_Type.__name__ = "Integer32"
_VirtualChassisVflMemberPortOperStatus_Object = MibTableColumn
virtualChassisVflMemberPortOperStatus = _VirtualChassisVflMemberPortOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 7, 1, 3),
    _VirtualChassisVflMemberPortOperStatus_Type()
)
virtualChassisVflMemberPortOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualChassisVflMemberPortOperStatus.setStatus("current")
_VirtualChassisVflMemberPortRowStatus_Type = RowStatus
_VirtualChassisVflMemberPortRowStatus_Object = MibTableColumn
virtualChassisVflMemberPortRowStatus = _VirtualChassisVflMemberPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 7, 1, 4),
    _VirtualChassisVflMemberPortRowStatus_Type()
)
virtualChassisVflMemberPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    virtualChassisVflMemberPortRowStatus.setStatus("current")
_VirtualChassisTrapInfo_ObjectIdentity = ObjectIdentity
virtualChassisTrapInfo = _VirtualChassisTrapInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 8)
)


class _VirtualChassisDiagnostic_Type(Integer32):
    """Custom type virtualChassisDiagnostic based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("duplexMode", 1),
          ("speed", 2))
    )


_VirtualChassisDiagnostic_Type.__name__ = "Integer32"
_VirtualChassisDiagnostic_Object = MibScalar
virtualChassisDiagnostic = _VirtualChassisDiagnostic_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 8, 1),
    _VirtualChassisDiagnostic_Type()
)
virtualChassisDiagnostic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualChassisDiagnostic.setStatus("current")


class _VirtualChassisUpgradeCompleteStatus_Type(Integer32):
    """Custom type virtualChassisUpgradeCompleteStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failure", 2),
          ("success", 1))
    )


_VirtualChassisUpgradeCompleteStatus_Type.__name__ = "Integer32"
_VirtualChassisUpgradeCompleteStatus_Object = MibScalar
virtualChassisUpgradeCompleteStatus = _VirtualChassisUpgradeCompleteStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 8, 2),
    _VirtualChassisUpgradeCompleteStatus_Type()
)
virtualChassisUpgradeCompleteStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualChassisUpgradeCompleteStatus.setStatus("current")
_AlcatelIND1VirtualChassisMIBConformance_ObjectIdentity = ObjectIdentity
alcatelIND1VirtualChassisMIBConformance = _AlcatelIND1VirtualChassisMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1VirtualChassisMIBConformance.setStatus("current")
_AlcatelIND1VirtualChassisMIBGroups_ObjectIdentity = ObjectIdentity
alcatelIND1VirtualChassisMIBGroups = _AlcatelIND1VirtualChassisMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1VirtualChassisMIBGroups.setStatus("current")
_AlcatelIND1VirtualChassisMIBCompliances_ObjectIdentity = ObjectIdentity
alcatelIND1VirtualChassisMIBCompliances = _AlcatelIND1VirtualChassisMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 2, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1VirtualChassisMIBCompliances.setStatus("current")

# Managed Objects groups

virtualChassisLocalInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 2, 1, 1)
)
virtualChassisLocalInfoGroup.setObjects(
    ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisLocalInfoChasId")
)
if mibBuilder.loadTexts:
    virtualChassisLocalInfoGroup.setStatus("current")

virtualChassisGlobalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 2, 1, 2)
)
virtualChassisGlobalGroup.setObjects(
      *(("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisConfigChassisId"),
        ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisRole"),
        ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisPreviousRole"),
        ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisStatus"),
        ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisOperPriority"),
        ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisConfigPriority"),
        ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisGroup"),
        ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisMac"),
        ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisUpTime"),
        ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisDesigNI"),
        ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisPriCmm"),
        ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisSecCmm"),
        ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisOperHelloInterval"),
        ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisOperControlVlan"),
        ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisConfigHelloInterval"),
        ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisConfigControlVlan"),
        ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisType"),
        ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisLicense"),
        ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisOperChasIdConsis"),
        ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisConfigChasIdConsis"),
        ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisOperControlVlanConsis"),
        ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisConfigControlVlanConsis"),
        ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisOperHelloIntervalConsis"),
        ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisConfigHelloIntervalConsis"),
        ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisChassisTypeConsis"),
        ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisGroupConsis"),
        ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisLicenseConsis"),
        ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisGlobalConsis"),
        ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisNumOfNeighbor"),
        ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisNumOfDirectNeighbor"))
)
if mibBuilder.loadTexts:
    virtualChassisGlobalGroup.setStatus("current")

virtualChassisNeighborGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 2, 1, 3)
)
virtualChassisNeighborGroup.setObjects(
      *(("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisNeighborShortestPath"),
        ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisNeighborIsDirect"))
)
if mibBuilder.loadTexts:
    virtualChassisNeighborGroup.setStatus("current")

virtualChassisChassisResetListGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 2, 1, 4)
)
virtualChassisChassisResetListGroup.setObjects(
    ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisChassisResetList")
)
if mibBuilder.loadTexts:
    virtualChassisChassisResetListGroup.setStatus("current")

virtualChassisSlotRestStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 2, 1, 5)
)
virtualChassisSlotRestStatusGroup.setObjects(
    ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisSlotResetStatus")
)
if mibBuilder.loadTexts:
    virtualChassisSlotRestStatusGroup.setStatus("current")

virtualChassisVflGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 2, 1, 6)
)
virtualChassisVflGroup.setObjects(
      *(("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisVflDefaultVlan"),
        ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisVflOperStatus"),
        ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisVflPrimaryPort"),
        ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisVflActivePortNum"),
        ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisVflConfigPortNum"),
        ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisVflRowStatus"),
        ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisVflDirectNeighborChasId"),
        ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisVflSpeedType"))
)
if mibBuilder.loadTexts:
    virtualChassisVflGroup.setStatus("current")

virtualChassisVflMemberPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 2, 1, 7)
)
virtualChassisVflMemberPortGroup.setObjects(
      *(("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisVflMemberPortIsPrimay"),
        ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisVflMemberPortOperStatus"),
        ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisVflMemberPortRowStatus"))
)
if mibBuilder.loadTexts:
    virtualChassisVflMemberPortGroup.setStatus("current")

virtualChassisTrapInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 2, 1, 8)
)
virtualChassisTrapInfoGroup.setObjects(
      *(("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisDiagnostic"),
        ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisUpgradeCompleteStatus"))
)
if mibBuilder.loadTexts:
    virtualChassisTrapInfoGroup.setStatus("current")


# Notification objects

virtualChassisStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 0, 1)
)
virtualChassisStatusChange.setObjects(
      *(("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisOperChasId"),
        ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisStatus"))
)
if mibBuilder.loadTexts:
    virtualChassisStatusChange.setStatus(
        "current"
    )

virtualChassisRoleChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 0, 2)
)
virtualChassisRoleChange.setObjects(
      *(("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisOperChasId"),
        ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisRole"))
)
if mibBuilder.loadTexts:
    virtualChassisRoleChange.setStatus(
        "current"
    )

virtualChassisVflStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 0, 3)
)
virtualChassisVflStatusChange.setObjects(
      *(("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisOperChasId"),
        ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisVflId"),
        ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisVflOperStatus"))
)
if mibBuilder.loadTexts:
    virtualChassisVflStatusChange.setStatus(
        "current"
    )

virtualChassisVflMemberPortStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 0, 4)
)
virtualChassisVflMemberPortStatusChange.setObjects(
      *(("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisOperChasId"),
        ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisVflId"),
        ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisVflMemberPortIfindex"),
        ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisVflMemberPortOperStatus"))
)
if mibBuilder.loadTexts:
    virtualChassisVflMemberPortStatusChange.setStatus(
        "deprecated"
    )

virtualChassisVflMemberPortJoinFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 0, 5)
)
virtualChassisVflMemberPortJoinFailure.setObjects(
      *(("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisOperChasId"),
        ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisVflId"),
        ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisVflMemberPortIfindex"),
        ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisDiagnostic"))
)
if mibBuilder.loadTexts:
    virtualChassisVflMemberPortJoinFailure.setStatus(
        "current"
    )

virtualChassisUpgradeComplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 0, 6)
)
virtualChassisUpgradeComplete.setObjects(
    ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisUpgradeCompleteStatus")
)
if mibBuilder.loadTexts:
    virtualChassisUpgradeComplete.setStatus(
        "current"
    )

virtualChassisVflSpeedTypeChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 0, 7)
)
virtualChassisVflSpeedTypeChange.setObjects(
      *(("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisOperChasId"),
        ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisVflId"),
        ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisVflSpeedType"))
)
if mibBuilder.loadTexts:
    virtualChassisVflSpeedTypeChange.setStatus(
        "current"
    )


# Notifications groups

virtualChassisTrapOBJGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 2, 1, 9)
)
virtualChassisTrapOBJGroup.setObjects(
      *(("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisStatusChange"),
        ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisRoleChange"),
        ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisVflStatusChange"),
        ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisVflMemberPortStatusChange"),
        ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisVflMemberPortJoinFailure"),
        ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisUpgradeComplete"),
        ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisVflSpeedTypeChange"))
)
if mibBuilder.loadTexts:
    virtualChassisTrapOBJGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

alcatelIND1VirtualChassisMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1VirtualChassisMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-VIRTUAL-CHASSIS-MIB",
    **{"VirtualOperChassisId": VirtualOperChassisId,
       "VirtualConfigChassisId": VirtualConfigChassisId,
       "VirtualChassisHelloInterval": VirtualChassisHelloInterval,
       "VirtualChassisControlVlan": VirtualChassisControlVlan,
       "VirtualChassisCmmSlot": VirtualChassisCmmSlot,
       "VirtualChassisNiSlot": VirtualChassisNiSlot,
       "VirtualChassisVflId": VirtualChassisVflId,
       "VirtualChassisConsistency": VirtualChassisConsistency,
       "VirtualChassisRole": VirtualChassisRole,
       "VirtualChassisStatus": VirtualChassisStatus,
       "VirtualChassisGroup": VirtualChassisGroup,
       "VirtualChassisPriority": VirtualChassisPriority,
       "VirtualChassisSlotResetStatus": VirtualChassisSlotResetStatus,
       "VirtualChassisType": VirtualChassisType,
       "VirtualChassisVflSpeedType": VirtualChassisVflSpeedType,
       "alcatelIND1VirtualChassisMIB": alcatelIND1VirtualChassisMIB,
       "alcatelIND1VirtualChassisMIBNotifications": alcatelIND1VirtualChassisMIBNotifications,
       "virtualChassisStatusChange": virtualChassisStatusChange,
       "virtualChassisRoleChange": virtualChassisRoleChange,
       "virtualChassisVflStatusChange": virtualChassisVflStatusChange,
       "virtualChassisVflMemberPortStatusChange": virtualChassisVflMemberPortStatusChange,
       "virtualChassisVflMemberPortJoinFailure": virtualChassisVflMemberPortJoinFailure,
       "virtualChassisUpgradeComplete": virtualChassisUpgradeComplete,
       "virtualChassisVflSpeedTypeChange": virtualChassisVflSpeedTypeChange,
       "alcatelIND1VirtualChassisMIBObjects": alcatelIND1VirtualChassisMIBObjects,
       "virtualChassisLocalInfo": virtualChassisLocalInfo,
       "virtualChassisLocalInfoChasId": virtualChassisLocalInfoChasId,
       "virtualChassisGlobalTable": virtualChassisGlobalTable,
       "virtualChassisGlobalEntry": virtualChassisGlobalEntry,
       "virtualChassisOperChasId": virtualChassisOperChasId,
       "virtualChassisConfigChassisId": virtualChassisConfigChassisId,
       "virtualChassisRole": virtualChassisRole,
       "virtualChassisPreviousRole": virtualChassisPreviousRole,
       "virtualChassisStatus": virtualChassisStatus,
       "virtualChassisOperPriority": virtualChassisOperPriority,
       "virtualChassisConfigPriority": virtualChassisConfigPriority,
       "virtualChassisGroup": virtualChassisGroup,
       "virtualChassisMac": virtualChassisMac,
       "virtualChassisUpTime": virtualChassisUpTime,
       "virtualChassisDesigNI": virtualChassisDesigNI,
       "virtualChassisPriCmm": virtualChassisPriCmm,
       "virtualChassisSecCmm": virtualChassisSecCmm,
       "virtualChassisOperHelloInterval": virtualChassisOperHelloInterval,
       "virtualChassisOperControlVlan": virtualChassisOperControlVlan,
       "virtualChassisConfigHelloInterval": virtualChassisConfigHelloInterval,
       "virtualChassisConfigControlVlan": virtualChassisConfigControlVlan,
       "virtualChassisType": virtualChassisType,
       "virtualChassisLicense": virtualChassisLicense,
       "virtualChassisOperChasIdConsis": virtualChassisOperChasIdConsis,
       "virtualChassisConfigChasIdConsis": virtualChassisConfigChasIdConsis,
       "virtualChassisOperControlVlanConsis": virtualChassisOperControlVlanConsis,
       "virtualChassisConfigControlVlanConsis": virtualChassisConfigControlVlanConsis,
       "virtualChassisOperHelloIntervalConsis": virtualChassisOperHelloIntervalConsis,
       "virtualChassisConfigHelloIntervalConsis": virtualChassisConfigHelloIntervalConsis,
       "virtualChassisChassisTypeConsis": virtualChassisChassisTypeConsis,
       "virtualChassisGroupConsis": virtualChassisGroupConsis,
       "virtualChassisLicenseConsis": virtualChassisLicenseConsis,
       "virtualChassisGlobalConsis": virtualChassisGlobalConsis,
       "virtualChassisNumOfNeighbor": virtualChassisNumOfNeighbor,
       "virtualChassisNumOfDirectNeighbor": virtualChassisNumOfDirectNeighbor,
       "virtualChassisNeighborTable": virtualChassisNeighborTable,
       "virtualChassisNeighborEntry": virtualChassisNeighborEntry,
       "virtualChassisNeighborChasId": virtualChassisNeighborChasId,
       "virtualChassisNeighborShortestPath": virtualChassisNeighborShortestPath,
       "virtualChassisNeighborIsDirect": virtualChassisNeighborIsDirect,
       "virtualChassisChassisResetListTable": virtualChassisChassisResetListTable,
       "virtualChassisChassisResetListEntry": virtualChassisChassisResetListEntry,
       "virtualChassisChassisResetList": virtualChassisChassisResetList,
       "virtualChassisSlotResetStatusTable": virtualChassisSlotResetStatusTable,
       "virtualChassisSlotResetStatusEntry": virtualChassisSlotResetStatusEntry,
       "virtualChassisSlotNum": virtualChassisSlotNum,
       "virtualChassisSlotResetStatus": virtualChassisSlotResetStatus,
       "virtualChassisVflTable": virtualChassisVflTable,
       "virtualChassisVflEntry": virtualChassisVflEntry,
       "virtualChassisVflId": virtualChassisVflId,
       "virtualChassisVflDefaultVlan": virtualChassisVflDefaultVlan,
       "virtualChassisVflOperStatus": virtualChassisVflOperStatus,
       "virtualChassisVflPrimaryPort": virtualChassisVflPrimaryPort,
       "virtualChassisVflActivePortNum": virtualChassisVflActivePortNum,
       "virtualChassisVflConfigPortNum": virtualChassisVflConfigPortNum,
       "virtualChassisVflRowStatus": virtualChassisVflRowStatus,
       "virtualChassisVflDirectNeighborChasId": virtualChassisVflDirectNeighborChasId,
       "virtualChassisVflSpeedType": virtualChassisVflSpeedType,
       "virtualChassisVflMemberPortTable": virtualChassisVflMemberPortTable,
       "virtualChassisVflMemberPortEntry": virtualChassisVflMemberPortEntry,
       "virtualChassisVflMemberPortIfindex": virtualChassisVflMemberPortIfindex,
       "virtualChassisVflMemberPortIsPrimay": virtualChassisVflMemberPortIsPrimay,
       "virtualChassisVflMemberPortOperStatus": virtualChassisVflMemberPortOperStatus,
       "virtualChassisVflMemberPortRowStatus": virtualChassisVflMemberPortRowStatus,
       "virtualChassisTrapInfo": virtualChassisTrapInfo,
       "virtualChassisDiagnostic": virtualChassisDiagnostic,
       "virtualChassisUpgradeCompleteStatus": virtualChassisUpgradeCompleteStatus,
       "alcatelIND1VirtualChassisMIBConformance": alcatelIND1VirtualChassisMIBConformance,
       "alcatelIND1VirtualChassisMIBGroups": alcatelIND1VirtualChassisMIBGroups,
       "virtualChassisLocalInfoGroup": virtualChassisLocalInfoGroup,
       "virtualChassisGlobalGroup": virtualChassisGlobalGroup,
       "virtualChassisNeighborGroup": virtualChassisNeighborGroup,
       "virtualChassisChassisResetListGroup": virtualChassisChassisResetListGroup,
       "virtualChassisSlotRestStatusGroup": virtualChassisSlotRestStatusGroup,
       "virtualChassisVflGroup": virtualChassisVflGroup,
       "virtualChassisVflMemberPortGroup": virtualChassisVflMemberPortGroup,
       "virtualChassisTrapInfoGroup": virtualChassisTrapInfoGroup,
       "virtualChassisTrapOBJGroup": virtualChassisTrapOBJGroup,
       "alcatelIND1VirtualChassisMIBCompliances": alcatelIND1VirtualChassisMIBCompliances,
       "alcatelIND1VirtualChassisMIBCompliance": alcatelIND1VirtualChassisMIBCompliance}
)
