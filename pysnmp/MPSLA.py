# SNMP MIB module (MPSLA) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MPSLA
# Produced by pysmi-1.5.4 at Mon Oct 14 22:23:32 2024
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

(mpMgmt,
 mpTrapObject) = mibBuilder.importSymbols(
    "MAIPU-SMI",
    "mpMgmt",
    "mpTrapObject")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

sysSLA = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class EnabledStatus(Integer32, TextualConvention):
    status = "current"
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



# MIB Managed Objects in the order of their OIDs

_MpTrap_ObjectIdentity = ObjectIdentity
mpTrap = _MpTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 2, 1)
)
if mibBuilder.loadTexts:
    mpTrap.setStatus("current")


class _MpTrapClass_Type(Integer32):
    """Custom type mpTrapClass based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("alerts", 2),
          ("critical", 3),
          ("debugging", 8),
          ("emergencies", 1),
          ("errors", 4),
          ("informational", 7),
          ("notifications", 6),
          ("warnings", 5))
    )


_MpTrapClass_Type.__name__ = "Integer32"
_MpTrapClass_Object = MibScalar
mpTrapClass = _MpTrapClass_Object(
    (1, 3, 6, 1, 4, 1, 5651, 2, 1, 1),
    _MpTrapClass_Type()
)
mpTrapClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpTrapClass.setStatus("current")
_MpTrapDescr_Type = DisplayString
_MpTrapDescr_Object = MibScalar
mpTrapDescr = _MpTrapDescr_Object(
    (1, 3, 6, 1, 4, 1, 5651, 2, 1, 2),
    _MpTrapDescr_Type()
)
mpTrapDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpTrapDescr.setStatus("current")


class _MpTrapType_Type(Integer32):
    """Custom type mpTrapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("interface", 2),
          ("other", 3),
          ("system", 1))
    )


_MpTrapType_Type.__name__ = "Integer32"
_MpTrapType_Object = MibScalar
mpTrapType = _MpTrapType_Object(
    (1, 3, 6, 1, 4, 1, 5651, 2, 1, 3),
    _MpTrapType_Type()
)
mpTrapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpTrapType.setStatus("current")
_MpTraps_ObjectIdentity = ObjectIdentity
mpTraps = _MpTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 2, 2)
)
if mibBuilder.loadTexts:
    mpTraps.setStatus("current")
_MpSla_ObjectIdentity = ObjectIdentity
mpSla = _MpSla_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 2, 2, 62)
)
if mibBuilder.loadTexts:
    mpSla.setStatus("current")
_Mpios_ObjectIdentity = ObjectIdentity
mpios = _Mpios_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20)
)
_IosSystem_ObjectIdentity = ObjectIdentity
iosSystem = _IosSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1)
)
_IosObjects_ObjectIdentity = ObjectIdentity
iosObjects = _IosObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1)
)
_SysSlaGbl_ObjectIdentity = ObjectIdentity
sysSlaGbl = _SysSlaGbl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 1)
)
_SysSlaCtrl_Type = EnabledStatus
_SysSlaCtrl_Object = MibScalar
sysSlaCtrl = _SysSlaCtrl_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 1, 1),
    _SysSlaCtrl_Type()
)
sysSlaCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSlaCtrl.setStatus("current")
_SysSlaResponder_Type = TruthValue
_SysSlaResponder_Object = MibScalar
sysSlaResponder = _SysSlaResponder_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 1, 2),
    _SysSlaResponder_Type()
)
sysSlaResponder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSlaResponder.setStatus("current")


class _SysSlaNotUsedEntityId_Type(Integer32):
    """Custom type sysSlaNotUsedEntityId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000),
    )


_SysSlaNotUsedEntityId_Type.__name__ = "Integer32"
_SysSlaNotUsedEntityId_Object = MibScalar
sysSlaNotUsedEntityId = _SysSlaNotUsedEntityId_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 1, 3),
    _SysSlaNotUsedEntityId_Type()
)
sysSlaNotUsedEntityId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSlaNotUsedEntityId.setStatus("current")


class _SysSlaNotUsedScheId_Type(Integer32):
    """Custom type sysSlaNotUsedScheId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000),
    )


_SysSlaNotUsedScheId_Type.__name__ = "Integer32"
_SysSlaNotUsedScheId_Object = MibScalar
sysSlaNotUsedScheId = _SysSlaNotUsedScheId_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 1, 4),
    _SysSlaNotUsedScheId_Type()
)
sysSlaNotUsedScheId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSlaNotUsedScheId.setStatus("current")
_SysSlaEntityMgt_ObjectIdentity = ObjectIdentity
sysSlaEntityMgt = _SysSlaEntityMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 2)
)
_SysSlaEntityTable_Object = MibTable
sysSlaEntityTable = _SysSlaEntityTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 2, 100)
)
if mibBuilder.loadTexts:
    sysSlaEntityTable.setStatus("current")
_SysSlaEntityEntry_Object = MibTableRow
sysSlaEntityEntry = _SysSlaEntityEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 2, 100, 1)
)
sysSlaEntityEntry.setIndexNames(
    (0, "MPSLA", "rtrEntityId"),
)
if mibBuilder.loadTexts:
    sysSlaEntityEntry.setStatus("current")


class _SlaEntityId_Type(Integer32):
    """Custom type slaEntityId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000),
    )


_SlaEntityId_Type.__name__ = "Integer32"
_SlaEntityId_Object = MibTableColumn
slaEntityId = _SlaEntityId_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 2, 100, 1, 1),
    _SlaEntityId_Type()
)
slaEntityId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaEntityId.setStatus("current")


class _SlaEntityName_Type(DisplayString):
    """Custom type slaEntityName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_SlaEntityName_Type.__name__ = "DisplayString"
_SlaEntityName_Object = MibTableColumn
slaEntityName = _SlaEntityName_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 2, 100, 1, 2),
    _SlaEntityName_Type()
)
slaEntityName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaEntityName.setStatus("current")


class _SlaEntityType_Type(Integer32):
    """Custom type slaEntityType based on Integer32"""
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
        *(("flowStatistics", 3),
          ("icmpEcho", 1),
          ("icmpPathEcho", 6),
          ("icmpPathJit", 5),
          ("jitter", 2),
          ("udpecho", 4))
    )


_SlaEntityType_Type.__name__ = "Integer32"
_SlaEntityType_Object = MibTableColumn
slaEntityType = _SlaEntityType_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 2, 100, 1, 3),
    _SlaEntityType_Type()
)
slaEntityType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaEntityType.setStatus("current")
_SlaEntityRowStatus_Type = RowStatus
_SlaEntityRowStatus_Object = MibTableColumn
slaEntityRowStatus = _SlaEntityRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 2, 100, 1, 4),
    _SlaEntityRowStatus_Type()
)
slaEntityRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaEntityRowStatus.setStatus("current")
_SysSlaGroupMgt_ObjectIdentity = ObjectIdentity
sysSlaGroupMgt = _SysSlaGroupMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 3)
)
_SysSlaGroupTable_Object = MibTable
sysSlaGroupTable = _SysSlaGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 3, 100)
)
if mibBuilder.loadTexts:
    sysSlaGroupTable.setStatus("current")
_SysSlaGroupEntry_Object = MibTableRow
sysSlaGroupEntry = _SysSlaGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 3, 100, 1)
)
sysSlaGroupEntry.setIndexNames(
    (0, "MPSLA", "slaGroupId"),
)
if mibBuilder.loadTexts:
    sysSlaGroupEntry.setStatus("current")


class _SlaGroupId_Type(Integer32):
    """Custom type slaGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000),
    )


_SlaGroupId_Type.__name__ = "Integer32"
_SlaGroupId_Object = MibTableColumn
slaGroupId = _SlaGroupId_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 3, 100, 1, 1),
    _SlaGroupId_Type()
)
slaGroupId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaGroupId.setStatus("current")


class _SlaGroupName_Type(DisplayString):
    """Custom type slaGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_SlaGroupName_Type.__name__ = "DisplayString"
_SlaGroupName_Object = MibTableColumn
slaGroupName = _SlaGroupName_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 3, 100, 1, 2),
    _SlaGroupName_Type()
)
slaGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaGroupName.setStatus("current")


class _SlaGroupInterval_Type(Integer32):
    """Custom type slaGroupInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_SlaGroupInterval_Type.__name__ = "Integer32"
_SlaGroupInterval_Object = MibTableColumn
slaGroupInterval = _SlaGroupInterval_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 3, 100, 1, 3),
    _SlaGroupInterval_Type()
)
slaGroupInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaGroupInterval.setStatus("current")


class _SlaGroupEntityMembers_Type(DisplayString):
    """Custom type slaGroupEntityMembers based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SlaGroupEntityMembers_Type.__name__ = "DisplayString"
_SlaGroupEntityMembers_Object = MibTableColumn
slaGroupEntityMembers = _SlaGroupEntityMembers_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 3, 100, 1, 4),
    _SlaGroupEntityMembers_Type()
)
slaGroupEntityMembers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaGroupEntityMembers.setStatus("current")
_SlaGroupRowStatus_Type = RowStatus
_SlaGroupRowStatus_Object = MibTableColumn
slaGroupRowStatus = _SlaGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 3, 100, 1, 5),
    _SlaGroupRowStatus_Type()
)
slaGroupRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaGroupRowStatus.setStatus("current")
_SysSlaScheduleMgt_ObjectIdentity = ObjectIdentity
sysSlaScheduleMgt = _SysSlaScheduleMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 4)
)
_SysSlaScheduleTable_Object = MibTable
sysSlaScheduleTable = _SysSlaScheduleTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 4, 100)
)
if mibBuilder.loadTexts:
    sysSlaScheduleTable.setStatus("current")
_SysSlaScheduleEntry_Object = MibTableRow
sysSlaScheduleEntry = _SysSlaScheduleEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 4, 100, 1)
)
sysSlaScheduleEntry.setIndexNames(
    (0, "MPSLA", "slaScheduleId"),
)
if mibBuilder.loadTexts:
    sysSlaScheduleEntry.setStatus("current")
_SlaScheduleId_Type = Unsigned32
_SlaScheduleId_Object = MibTableColumn
slaScheduleId = _SlaScheduleId_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 4, 100, 1, 1),
    _SlaScheduleId_Type()
)
slaScheduleId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaScheduleId.setStatus("current")


class _SlaScheduleType_Type(Integer32):
    """Custom type slaScheduleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("entity", 1),
          ("group", 2))
    )


_SlaScheduleType_Type.__name__ = "Integer32"
_SlaScheduleType_Object = MibTableColumn
slaScheduleType = _SlaScheduleType_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 4, 100, 1, 2),
    _SlaScheduleType_Type()
)
slaScheduleType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaScheduleType.setStatus("current")


class _SlaScheduleObjId_Type(Integer32):
    """Custom type slaScheduleObjId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000),
    )


_SlaScheduleObjId_Type.__name__ = "Integer32"
_SlaScheduleObjId_Object = MibTableColumn
slaScheduleObjId = _SlaScheduleObjId_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 4, 100, 1, 3),
    _SlaScheduleObjId_Type()
)
slaScheduleObjId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaScheduleObjId.setStatus("current")


class _SlaScheduleStartTimeFlag_Type(Integer32):
    """Custom type slaScheduleStartTimeFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("afterTime", 2),
          ("startNow", 1),
          ("startTime", 3))
    )


_SlaScheduleStartTimeFlag_Type.__name__ = "Integer32"
_SlaScheduleStartTimeFlag_Object = MibTableColumn
slaScheduleStartTimeFlag = _SlaScheduleStartTimeFlag_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 4, 100, 1, 4),
    _SlaScheduleStartTimeFlag_Type()
)
slaScheduleStartTimeFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaScheduleStartTimeFlag.setStatus("current")


class _SlaScheduleAfterTime_Type(DisplayString):
    """Custom type slaScheduleAfterTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_SlaScheduleAfterTime_Type.__name__ = "DisplayString"
_SlaScheduleAfterTime_Object = MibTableColumn
slaScheduleAfterTime = _SlaScheduleAfterTime_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 4, 100, 1, 5),
    _SlaScheduleAfterTime_Type()
)
slaScheduleAfterTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaScheduleAfterTime.setStatus("current")


class _SlaScheduleStartTime_Type(DisplayString):
    """Custom type slaScheduleStartTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_SlaScheduleStartTime_Type.__name__ = "DisplayString"
_SlaScheduleStartTime_Object = MibTableColumn
slaScheduleStartTime = _SlaScheduleStartTime_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 4, 100, 1, 6),
    _SlaScheduleStartTime_Type()
)
slaScheduleStartTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaScheduleStartTime.setStatus("current")


class _SlaScheduleAgeOut_Type(Unsigned32):
    """Custom type slaScheduleAgeOut based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_SlaScheduleAgeOut_Type.__name__ = "Unsigned32"
_SlaScheduleAgeOut_Object = MibTableColumn
slaScheduleAgeOut = _SlaScheduleAgeOut_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 4, 100, 1, 7),
    _SlaScheduleAgeOut_Type()
)
slaScheduleAgeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaScheduleAgeOut.setStatus("current")


class _SlaScheduleLifeFlag_Type(Integer32):
    """Custom type slaScheduleLifeFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forever", 1),
          ("repeatAndDie", 2))
    )


_SlaScheduleLifeFlag_Type.__name__ = "Integer32"
_SlaScheduleLifeFlag_Object = MibTableColumn
slaScheduleLifeFlag = _SlaScheduleLifeFlag_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 4, 100, 1, 8),
    _SlaScheduleLifeFlag_Type()
)
slaScheduleLifeFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaScheduleLifeFlag.setStatus("current")


class _SlaScheduleLifeTime_Type(Unsigned32):
    """Custom type slaScheduleLifeTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SlaScheduleLifeTime_Type.__name__ = "Unsigned32"
_SlaScheduleLifeTime_Object = MibTableColumn
slaScheduleLifeTime = _SlaScheduleLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 4, 100, 1, 9),
    _SlaScheduleLifeTime_Type()
)
slaScheduleLifeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaScheduleLifeTime.setStatus("current")


class _SlaScheduleRepeat_Type(Unsigned32):
    """Custom type slaScheduleRepeat based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SlaScheduleRepeat_Type.__name__ = "Unsigned32"
_SlaScheduleRepeat_Object = MibTableColumn
slaScheduleRepeat = _SlaScheduleRepeat_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 4, 100, 1, 10),
    _SlaScheduleRepeat_Type()
)
slaScheduleRepeat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaScheduleRepeat.setStatus("current")


class _SlaScheduleInterval_Type(Unsigned32):
    """Custom type slaScheduleInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SlaScheduleInterval_Type.__name__ = "Unsigned32"
_SlaScheduleInterval_Object = MibTableColumn
slaScheduleInterval = _SlaScheduleInterval_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 4, 100, 1, 11),
    _SlaScheduleInterval_Type()
)
slaScheduleInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaScheduleInterval.setStatus("current")
_SlaScheduleRowStatus_Type = RowStatus
_SlaScheduleRowStatus_Object = MibTableColumn
slaScheduleRowStatus = _SlaScheduleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 4, 100, 1, 12),
    _SlaScheduleRowStatus_Type()
)
slaScheduleRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaScheduleRowStatus.setStatus("current")
_SysSlaIcmpEchoMgt_ObjectIdentity = ObjectIdentity
sysSlaIcmpEchoMgt = _SysSlaIcmpEchoMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 5)
)
_SysSlaIcmpEchoTable_Object = MibTable
sysSlaIcmpEchoTable = _SysSlaIcmpEchoTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 5, 100)
)
if mibBuilder.loadTexts:
    sysSlaIcmpEchoTable.setStatus("current")
_SysSlaIcmpEchoEntry_Object = MibTableRow
sysSlaIcmpEchoEntry = _SysSlaIcmpEchoEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 5, 100, 1)
)
sysSlaIcmpEchoEntry.setIndexNames(
    (0, "MPSLA", "slaIcmpEchoTableEntityId"),
)
if mibBuilder.loadTexts:
    sysSlaIcmpEchoEntry.setStatus("current")


class _SlaIcmpEchoTableEntityId_Type(Integer32):
    """Custom type slaIcmpEchoTableEntityId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000),
    )


_SlaIcmpEchoTableEntityId_Type.__name__ = "Integer32"
_SlaIcmpEchoTableEntityId_Object = MibTableColumn
slaIcmpEchoTableEntityId = _SlaIcmpEchoTableEntityId_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 5, 100, 1, 1),
    _SlaIcmpEchoTableEntityId_Type()
)
slaIcmpEchoTableEntityId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaIcmpEchoTableEntityId.setStatus("current")
_SlaIcmpEchoTargetIp_Type = IpAddress
_SlaIcmpEchoTargetIp_Object = MibTableColumn
slaIcmpEchoTargetIp = _SlaIcmpEchoTargetIp_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 5, 100, 1, 2),
    _SlaIcmpEchoTargetIp_Type()
)
slaIcmpEchoTargetIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaIcmpEchoTargetIp.setStatus("current")


class _SlaIcmpEchoPktNum_Type(Unsigned32):
    """Custom type slaIcmpEchoPktNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200000000),
    )


_SlaIcmpEchoPktNum_Type.__name__ = "Unsigned32"
_SlaIcmpEchoPktNum_Object = MibTableColumn
slaIcmpEchoPktNum = _SlaIcmpEchoPktNum_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 5, 100, 1, 3),
    _SlaIcmpEchoPktNum_Type()
)
slaIcmpEchoPktNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaIcmpEchoPktNum.setStatus("current")


class _SlaIcmpEchoPktLen_Type(Integer32):
    """Custom type slaIcmpEchoPktLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(36, 18024),
    )


_SlaIcmpEchoPktLen_Type.__name__ = "Integer32"
_SlaIcmpEchoPktLen_Object = MibTableColumn
slaIcmpEchoPktLen = _SlaIcmpEchoPktLen_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 5, 100, 1, 4),
    _SlaIcmpEchoPktLen_Type()
)
slaIcmpEchoPktLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaIcmpEchoPktLen.setStatus("current")


class _SlaIcmpEchoTimeout_Type(Integer32):
    """Custom type slaIcmpEchoTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_SlaIcmpEchoTimeout_Type.__name__ = "Integer32"
_SlaIcmpEchoTimeout_Object = MibTableColumn
slaIcmpEchoTimeout = _SlaIcmpEchoTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 5, 100, 1, 5),
    _SlaIcmpEchoTimeout_Type()
)
slaIcmpEchoTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaIcmpEchoTimeout.setStatus("current")


class _SlaIcmpEchoSchInterval_Type(Unsigned32):
    """Custom type slaIcmpEchoSchInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SlaIcmpEchoSchInterval_Type.__name__ = "Unsigned32"
_SlaIcmpEchoSchInterval_Object = MibTableColumn
slaIcmpEchoSchInterval = _SlaIcmpEchoSchInterval_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 5, 100, 1, 6),
    _SlaIcmpEchoSchInterval_Type()
)
slaIcmpEchoSchInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaIcmpEchoSchInterval.setStatus("current")
_SlaIcmpEchoExtendFlag_Type = TruthValue
_SlaIcmpEchoExtendFlag_Object = MibTableColumn
slaIcmpEchoExtendFlag = _SlaIcmpEchoExtendFlag_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 5, 100, 1, 7),
    _SlaIcmpEchoExtendFlag_Type()
)
slaIcmpEchoExtendFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaIcmpEchoExtendFlag.setStatus("current")


class _SlaIcmpEchoVrfName_Type(DisplayString):
    """Custom type slaIcmpEchoVrfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_SlaIcmpEchoVrfName_Type.__name__ = "DisplayString"
_SlaIcmpEchoVrfName_Object = MibTableColumn
slaIcmpEchoVrfName = _SlaIcmpEchoVrfName_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 5, 100, 1, 8),
    _SlaIcmpEchoVrfName_Type()
)
slaIcmpEchoVrfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaIcmpEchoVrfName.setStatus("current")
_SlaIcmpEchoSourceIp_Type = IpAddress
_SlaIcmpEchoSourceIp_Object = MibTableColumn
slaIcmpEchoSourceIp = _SlaIcmpEchoSourceIp_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 5, 100, 1, 9),
    _SlaIcmpEchoSourceIp_Type()
)
slaIcmpEchoSourceIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaIcmpEchoSourceIp.setStatus("current")


class _SlaIcmpEchoTos_Type(Integer32):
    """Custom type slaIcmpEchoTos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SlaIcmpEchoTos_Type.__name__ = "Integer32"
_SlaIcmpEchoTos_Object = MibTableColumn
slaIcmpEchoTos = _SlaIcmpEchoTos_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 5, 100, 1, 10),
    _SlaIcmpEchoTos_Type()
)
slaIcmpEchoTos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaIcmpEchoTos.setStatus("current")
_SlaIcmpEchoSetDf_Type = TruthValue
_SlaIcmpEchoSetDf_Object = MibTableColumn
slaIcmpEchoSetDf = _SlaIcmpEchoSetDf_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 5, 100, 1, 11),
    _SlaIcmpEchoSetDf_Type()
)
slaIcmpEchoSetDf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaIcmpEchoSetDf.setStatus("current")
_SlaIcmpEchoVerifyData_Type = TruthValue
_SlaIcmpEchoVerifyData_Object = MibTableColumn
slaIcmpEchoVerifyData = _SlaIcmpEchoVerifyData_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 5, 100, 1, 12),
    _SlaIcmpEchoVerifyData_Type()
)
slaIcmpEchoVerifyData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaIcmpEchoVerifyData.setStatus("current")


class _SlaIcmpEchoHistorySize_Type(Integer32):
    """Custom type slaIcmpEchoHistorySize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SlaIcmpEchoHistorySize_Type.__name__ = "Integer32"
_SlaIcmpEchoHistorySize_Object = MibTableColumn
slaIcmpEchoHistorySize = _SlaIcmpEchoHistorySize_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 5, 100, 1, 13),
    _SlaIcmpEchoHistorySize_Type()
)
slaIcmpEchoHistorySize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaIcmpEchoHistorySize.setStatus("current")


class _SlaIcmpEchoPeriods_Type(Integer32):
    """Custom type slaIcmpEchoPeriods based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_SlaIcmpEchoPeriods_Type.__name__ = "Integer32"
_SlaIcmpEchoPeriods_Object = MibTableColumn
slaIcmpEchoPeriods = _SlaIcmpEchoPeriods_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 5, 100, 1, 14),
    _SlaIcmpEchoPeriods_Type()
)
slaIcmpEchoPeriods.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaIcmpEchoPeriods.setStatus("current")


class _SlaIcmpEchoAlarmType_Type(Integer32):
    """Custom type slaIcmpEchoAlarmType based on Integer32"""
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
        *(("log", 1),
          ("logAndTrap", 3),
          ("noLogAndtrap", 4),
          ("trap", 2))
    )


_SlaIcmpEchoAlarmType_Type.__name__ = "Integer32"
_SlaIcmpEchoAlarmType_Object = MibTableColumn
slaIcmpEchoAlarmType = _SlaIcmpEchoAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 5, 100, 1, 15),
    _SlaIcmpEchoAlarmType_Type()
)
slaIcmpEchoAlarmType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaIcmpEchoAlarmType.setStatus("current")
_SlaIcmpEchoIsScheduling_Type = TruthValue
_SlaIcmpEchoIsScheduling_Object = MibTableColumn
slaIcmpEchoIsScheduling = _SlaIcmpEchoIsScheduling_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 5, 100, 1, 16),
    _SlaIcmpEchoIsScheduling_Type()
)
slaIcmpEchoIsScheduling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaIcmpEchoIsScheduling.setStatus("current")
_SlaIcmpEchoRowStatus_Type = RowStatus
_SlaIcmpEchoRowStatus_Object = MibTableColumn
slaIcmpEchoRowStatus = _SlaIcmpEchoRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 5, 100, 1, 17),
    _SlaIcmpEchoRowStatus_Type()
)
slaIcmpEchoRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaIcmpEchoRowStatus.setStatus("current")
_SysSlaIcmpEchoHistoryTable_Object = MibTable
sysSlaIcmpEchoHistoryTable = _SysSlaIcmpEchoHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 5, 200)
)
if mibBuilder.loadTexts:
    sysSlaIcmpEchoHistoryTable.setStatus("current")
_SysSlaIcmpEchoHistoryEntry_Object = MibTableRow
sysSlaIcmpEchoHistoryEntry = _SysSlaIcmpEchoHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 5, 200, 1)
)
sysSlaIcmpEchoHistoryEntry.setIndexNames(
    (0, "MPSLA", "slaIcmpEchoHisTableEntityId"),
    (0, "MPSLA", "slaIcmpechoHistoryIndex"),
)
if mibBuilder.loadTexts:
    sysSlaIcmpEchoHistoryEntry.setStatus("current")


class _SlaIcmpEchoHisTableEntityId_Type(Integer32):
    """Custom type slaIcmpEchoHisTableEntityId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000),
    )


_SlaIcmpEchoHisTableEntityId_Type.__name__ = "Integer32"
_SlaIcmpEchoHisTableEntityId_Object = MibTableColumn
slaIcmpEchoHisTableEntityId = _SlaIcmpEchoHisTableEntityId_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 5, 200, 1, 1),
    _SlaIcmpEchoHisTableEntityId_Type()
)
slaIcmpEchoHisTableEntityId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaIcmpEchoHisTableEntityId.setStatus("current")


class _SlaIcmpEchoHistoryIndex_Type(Integer32):
    """Custom type slaIcmpEchoHistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 500),
    )


_SlaIcmpEchoHistoryIndex_Type.__name__ = "Integer32"
_SlaIcmpEchoHistoryIndex_Object = MibTableColumn
slaIcmpEchoHistoryIndex = _SlaIcmpEchoHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 5, 200, 1, 2),
    _SlaIcmpEchoHistoryIndex_Type()
)
slaIcmpEchoHistoryIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaIcmpEchoHistoryIndex.setStatus("current")


class _SlaIcmpEchoRtt_Type(Integer32):
    """Custom type slaIcmpEchoRtt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_SlaIcmpEchoRtt_Type.__name__ = "Integer32"
_SlaIcmpEchoRtt_Object = MibTableColumn
slaIcmpEchoRtt = _SlaIcmpEchoRtt_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 5, 200, 1, 3),
    _SlaIcmpEchoRtt_Type()
)
slaIcmpEchoRtt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaIcmpEchoRtt.setStatus("current")


class _SlaIcmpEchoPktLoss_Type(Integer32):
    """Custom type slaIcmpEchoPktLoss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_SlaIcmpEchoPktLoss_Type.__name__ = "Integer32"
_SlaIcmpEchoPktLoss_Object = MibTableColumn
slaIcmpEchoPktLoss = _SlaIcmpEchoPktLoss_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 5, 200, 1, 4),
    _SlaIcmpEchoPktLoss_Type()
)
slaIcmpEchoPktLoss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaIcmpEchoPktLoss.setStatus("current")


class _SlaIcmpEchoTime_Type(DisplayString):
    """Custom type slaIcmpEchoTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 39),
    )


_SlaIcmpEchoTime_Type.__name__ = "DisplayString"
_SlaIcmpEchoTime_Object = MibTableColumn
slaIcmpEchoTime = _SlaIcmpEchoTime_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 5, 200, 1, 5),
    _SlaIcmpEchoTime_Type()
)
slaIcmpEchoTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaIcmpEchoTime.setStatus("current")
_SlaIcmpEchoTableRowStatus_Type = RowStatus
_SlaIcmpEchoTableRowStatus_Object = MibTableColumn
slaIcmpEchoTableRowStatus = _SlaIcmpEchoTableRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 5, 200, 1, 6),
    _SlaIcmpEchoTableRowStatus_Type()
)
slaIcmpEchoTableRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaIcmpEchoTableRowStatus.setStatus("current")
_SysSlaJitterMgt_ObjectIdentity = ObjectIdentity
sysSlaJitterMgt = _SysSlaJitterMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 6)
)
_SysSlaJitterTable_Object = MibTable
sysSlaJitterTable = _SysSlaJitterTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 6, 100)
)
if mibBuilder.loadTexts:
    sysSlaJitterTable.setStatus("current")
_SysSlaJitterEntry_Object = MibTableRow
sysSlaJitterEntry = _SysSlaJitterEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 6, 100, 1)
)
sysSlaJitterEntry.setIndexNames(
    (0, "MPSLA", "slaJitterTableEntityId"),
)
if mibBuilder.loadTexts:
    sysSlaJitterEntry.setStatus("current")


class _SlaJitterTableEntityId_Type(Integer32):
    """Custom type slaJitterTableEntityId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000),
    )


_SlaJitterTableEntityId_Type.__name__ = "Integer32"
_SlaJitterTableEntityId_Object = MibTableColumn
slaJitterTableEntityId = _SlaJitterTableEntityId_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 6, 100, 1, 1),
    _SlaJitterTableEntityId_Type()
)
slaJitterTableEntityId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaJitterTableEntityId.setStatus("current")


class _SlaJitterState_Type(Integer32):
    """Custom type slaJitterState based on Integer32"""
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
        *(("finished", 6),
          ("halt", 5),
          ("init", 1),
          ("pend", 2),
          ("request", 3),
          ("transmit", 4))
    )


_SlaJitterState_Type.__name__ = "Integer32"
_SlaJitterState_Object = MibTableColumn
slaJitterState = _SlaJitterState_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 6, 100, 1, 2),
    _SlaJitterState_Type()
)
slaJitterState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaJitterState.setStatus("current")
_SlaJitterTargetIp_Type = IpAddress
_SlaJitterTargetIp_Object = MibTableColumn
slaJitterTargetIp = _SlaJitterTargetIp_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 6, 100, 1, 3),
    _SlaJitterTargetIp_Type()
)
slaJitterTargetIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaJitterTargetIp.setStatus("current")


class _SlaJitterTargetPort_Type(Integer32):
    """Custom type slaJitterTargetPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SlaJitterTargetPort_Type.__name__ = "Integer32"
_SlaJitterTargetPort_Object = MibTableColumn
slaJitterTargetPort = _SlaJitterTargetPort_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 6, 100, 1, 4),
    _SlaJitterTargetPort_Type()
)
slaJitterTargetPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaJitterTargetPort.setStatus("current")


class _SlaJitterCodec_Type(Integer32):
    """Custom type slaJitterCodec based on Integer32"""
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
        *(("g711ALAW", 2),
          ("g711MULAW", 1),
          ("g729A", 3),
          ("invalid", 5),
          ("userDefined", 4))
    )


_SlaJitterCodec_Type.__name__ = "Integer32"
_SlaJitterCodec_Object = MibTableColumn
slaJitterCodec = _SlaJitterCodec_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 6, 100, 1, 5),
    _SlaJitterCodec_Type()
)
slaJitterCodec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaJitterCodec.setStatus("current")


class _SlaJitterPktLen_Type(Integer32):
    """Custom type slaJitterPktLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1500),
    )


_SlaJitterPktLen_Type.__name__ = "Integer32"
_SlaJitterPktLen_Object = MibTableColumn
slaJitterPktLen = _SlaJitterPktLen_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 6, 100, 1, 6),
    _SlaJitterPktLen_Type()
)
slaJitterPktLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaJitterPktLen.setStatus("current")


class _SlaJitterPktNum_Type(Integer32):
    """Custom type slaJitterPktNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6000),
    )


_SlaJitterPktNum_Type.__name__ = "Integer32"
_SlaJitterPktNum_Object = MibTableColumn
slaJitterPktNum = _SlaJitterPktNum_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 6, 100, 1, 7),
    _SlaJitterPktNum_Type()
)
slaJitterPktNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaJitterPktNum.setStatus("current")


class _SlaJitterPktInterval_Type(Integer32):
    """Custom type slaJitterPktInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 6000),
    )


_SlaJitterPktInterval_Type.__name__ = "Integer32"
_SlaJitterPktInterval_Object = MibTableColumn
slaJitterPktInterval = _SlaJitterPktInterval_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 6, 100, 1, 8),
    _SlaJitterPktInterval_Type()
)
slaJitterPktInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaJitterPktInterval.setStatus("current")


class _SlaJitterSchInterval_Type(Integer32):
    """Custom type slaJitterSchInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SlaJitterSchInterval_Type.__name__ = "Integer32"
_SlaJitterSchInterval_Object = MibTableColumn
slaJitterSchInterval = _SlaJitterSchInterval_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 6, 100, 1, 9),
    _SlaJitterSchInterval_Type()
)
slaJitterSchInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaJitterSchInterval.setStatus("current")
_SlaJitterSourceIp_Type = IpAddress
_SlaJitterSourceIp_Object = MibTableColumn
slaJitterSourceIp = _SlaJitterSourceIp_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 6, 100, 1, 10),
    _SlaJitterSourceIp_Type()
)
slaJitterSourceIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaJitterSourceIp.setStatus("current")


class _SlaJitterSourcePort_Type(Integer32):
    """Custom type slaJitterSourcePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SlaJitterSourcePort_Type.__name__ = "Integer32"
_SlaJitterSourcePort_Object = MibTableColumn
slaJitterSourcePort = _SlaJitterSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 6, 100, 1, 11),
    _SlaJitterSourcePort_Type()
)
slaJitterSourcePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaJitterSourcePort.setStatus("current")


class _SlaJitterTimeout_Type(Integer32):
    """Custom type slaJitterTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 604800000),
    )


_SlaJitterTimeout_Type.__name__ = "Integer32"
_SlaJitterTimeout_Object = MibTableColumn
slaJitterTimeout = _SlaJitterTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 6, 100, 1, 12),
    _SlaJitterTimeout_Type()
)
slaJitterTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaJitterTimeout.setStatus("current")


class _SlaJitterVrfName_Type(DisplayString):
    """Custom type slaJitterVrfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_SlaJitterVrfName_Type.__name__ = "DisplayString"
_SlaJitterVrfName_Object = MibTableColumn
slaJitterVrfName = _SlaJitterVrfName_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 6, 100, 1, 13),
    _SlaJitterVrfName_Type()
)
slaJitterVrfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaJitterVrfName.setStatus("current")


class _SlaJitterTos_Type(Integer32):
    """Custom type slaJitterTos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SlaJitterTos_Type.__name__ = "Integer32"
_SlaJitterTos_Object = MibTableColumn
slaJitterTos = _SlaJitterTos_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 6, 100, 1, 14),
    _SlaJitterTos_Type()
)
slaJitterTos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaJitterTos.setStatus("current")


class _SlaJitterHistorySize_Type(Integer32):
    """Custom type slaJitterHistorySize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SlaJitterHistorySize_Type.__name__ = "Integer32"
_SlaJitterHistorySize_Object = MibTableColumn
slaJitterHistorySize = _SlaJitterHistorySize_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 6, 100, 1, 15),
    _SlaJitterHistorySize_Type()
)
slaJitterHistorySize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaJitterHistorySize.setStatus("current")


class _SlaJitterPeriods_Type(Integer32):
    """Custom type slaJitterPeriods based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_SlaJitterPeriods_Type.__name__ = "Integer32"
_SlaJitterPeriods_Object = MibTableColumn
slaJitterPeriods = _SlaJitterPeriods_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 6, 100, 1, 16),
    _SlaJitterPeriods_Type()
)
slaJitterPeriods.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaJitterPeriods.setStatus("current")


class _SlaJitterAlarmType_Type(Integer32):
    """Custom type slaJitterAlarmType based on Integer32"""
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
        *(("log", 1),
          ("logAndTrap", 3),
          ("noLogAndtrap", 4),
          ("trap", 2))
    )


_SlaJitterAlarmType_Type.__name__ = "Integer32"
_SlaJitterAlarmType_Object = MibTableColumn
slaJitterAlarmType = _SlaJitterAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 6, 100, 1, 17),
    _SlaJitterAlarmType_Type()
)
slaJitterAlarmType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaJitterAlarmType.setStatus("current")
_SlaJitterTableRowStatus_Type = RowStatus
_SlaJitterTableRowStatus_Object = MibTableColumn
slaJitterTableRowStatus = _SlaJitterTableRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 6, 100, 1, 18),
    _SlaJitterTableRowStatus_Type()
)
slaJitterTableRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaJitterTableRowStatus.setStatus("current")
_SysSlaJitterHistoryTable_Object = MibTable
sysSlaJitterHistoryTable = _SysSlaJitterHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 6, 200)
)
if mibBuilder.loadTexts:
    sysSlaJitterHistoryTable.setStatus("current")
_SysSlaJitterHistoryEntry_Object = MibTableRow
sysSlaJitterHistoryEntry = _SysSlaJitterHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 6, 200, 1)
)
sysSlaJitterHistoryEntry.setIndexNames(
    (0, "MPSLA", "slaJitterHisTableEntityId"),
    (0, "MPSLA", "slaJitterHistoryIndex"),
)
if mibBuilder.loadTexts:
    sysSlaJitterHistoryEntry.setStatus("current")


class _SlaJitterHisTableEntityId_Type(Integer32):
    """Custom type slaJitterHisTableEntityId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000),
    )


_SlaJitterHisTableEntityId_Type.__name__ = "Integer32"
_SlaJitterHisTableEntityId_Object = MibTableColumn
slaJitterHisTableEntityId = _SlaJitterHisTableEntityId_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 6, 200, 1, 1),
    _SlaJitterHisTableEntityId_Type()
)
slaJitterHisTableEntityId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaJitterHisTableEntityId.setStatus("current")


class _SlaJitterHistoryIndex_Type(Integer32):
    """Custom type slaJitterHistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SlaJitterHistoryIndex_Type.__name__ = "Integer32"
_SlaJitterHistoryIndex_Object = MibTableColumn
slaJitterHistoryIndex = _SlaJitterHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 6, 200, 1, 2),
    _SlaJitterHistoryIndex_Type()
)
slaJitterHistoryIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaJitterHistoryIndex.setStatus("current")
_SlaJitterRtt_Type = Integer32
_SlaJitterRtt_Object = MibTableColumn
slaJitterRtt = _SlaJitterRtt_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 6, 200, 1, 3),
    _SlaJitterRtt_Type()
)
slaJitterRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaJitterRtt.setStatus("current")
_SlaJitterPktLossSd_Type = Integer32
_SlaJitterPktLossSd_Object = MibTableColumn
slaJitterPktLossSd = _SlaJitterPktLossSd_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 6, 200, 1, 4),
    _SlaJitterPktLossSd_Type()
)
slaJitterPktLossSd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaJitterPktLossSd.setStatus("current")
_SlaJitterPktLossDs_Type = Integer32
_SlaJitterPktLossDs_Object = MibTableColumn
slaJitterPktLossDs = _SlaJitterPktLossDs_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 6, 200, 1, 5),
    _SlaJitterPktLossDs_Type()
)
slaJitterPktLossDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaJitterPktLossDs.setStatus("current")
_SlaJitterSd_Type = Integer32
_SlaJitterSd_Object = MibTableColumn
slaJitterSd = _SlaJitterSd_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 6, 200, 1, 6),
    _SlaJitterSd_Type()
)
slaJitterSd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaJitterSd.setStatus("current")
_SlaJitterDs_Type = Integer32
_SlaJitterDs_Object = MibTableColumn
slaJitterDs = _SlaJitterDs_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 6, 200, 1, 7),
    _SlaJitterDs_Type()
)
slaJitterDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaJitterDs.setStatus("current")
_SlaJitterDelaySd_Type = Integer32
_SlaJitterDelaySd_Object = MibTableColumn
slaJitterDelaySd = _SlaJitterDelaySd_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 6, 200, 1, 8),
    _SlaJitterDelaySd_Type()
)
slaJitterDelaySd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaJitterDelaySd.setStatus("current")
_SlaJitterDelayDs_Type = Integer32
_SlaJitterDelayDs_Object = MibTableColumn
slaJitterDelayDs = _SlaJitterDelayDs_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 6, 200, 1, 9),
    _SlaJitterDelayDs_Type()
)
slaJitterDelayDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaJitterDelayDs.setStatus("current")
_SlaJitterIcpif_Type = Integer32
_SlaJitterIcpif_Object = MibTableColumn
slaJitterIcpif = _SlaJitterIcpif_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 6, 200, 1, 10),
    _SlaJitterIcpif_Type()
)
slaJitterIcpif.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaJitterIcpif.setStatus("current")
_SlaJitterMos_Type = Integer32
_SlaJitterMos_Object = MibTableColumn
slaJitterMos = _SlaJitterMos_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 6, 200, 1, 11),
    _SlaJitterMos_Type()
)
slaJitterMos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaJitterMos.setStatus("current")


class _SlaJitterTime_Type(DisplayString):
    """Custom type slaJitterTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_SlaJitterTime_Type.__name__ = "DisplayString"
_SlaJitterTime_Object = MibTableColumn
slaJitterTime = _SlaJitterTime_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 6, 200, 1, 12),
    _SlaJitterTime_Type()
)
slaJitterTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaJitterTime.setStatus("current")
_SlaJitterHisTableRowStatus_Type = RowStatus
_SlaJitterHisTableRowStatus_Object = MibTableColumn
slaJitterHisTableRowStatus = _SlaJitterHisTableRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 6, 200, 1, 13),
    _SlaJitterHisTableRowStatus_Type()
)
slaJitterHisTableRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaJitterHisTableRowStatus.setStatus("current")
_SysSlaUdpEchoMgt_ObjectIdentity = ObjectIdentity
sysSlaUdpEchoMgt = _SysSlaUdpEchoMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 7)
)
_SysSlaUdpEchoTable_Object = MibTable
sysSlaUdpEchoTable = _SysSlaUdpEchoTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 7, 100)
)
if mibBuilder.loadTexts:
    sysSlaUdpEchoTable.setStatus("current")
_SysSlaUdpEchoEntry_Object = MibTableRow
sysSlaUdpEchoEntry = _SysSlaUdpEchoEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 7, 100, 1)
)
sysSlaUdpEchoEntry.setIndexNames(
    (0, "MPSLA", "slaUdpEchoTableEntityId"),
)
if mibBuilder.loadTexts:
    sysSlaUdpEchoEntry.setStatus("current")


class _SlaUdpEchoTableEntityId_Type(Integer32):
    """Custom type slaUdpEchoTableEntityId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000),
    )


_SlaUdpEchoTableEntityId_Type.__name__ = "Integer32"
_SlaUdpEchoTableEntityId_Object = MibTableColumn
slaUdpEchoTableEntityId = _SlaUdpEchoTableEntityId_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 7, 100, 1, 1),
    _SlaUdpEchoTableEntityId_Type()
)
slaUdpEchoTableEntityId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaUdpEchoTableEntityId.setStatus("current")


class _SlaUdpEchoState_Type(Integer32):
    """Custom type slaUdpEchoState based on Integer32"""
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
        *(("finished", 6),
          ("halt", 5),
          ("init", 1),
          ("pend", 2),
          ("request", 3),
          ("transmit", 4))
    )


_SlaUdpEchoState_Type.__name__ = "Integer32"
_SlaUdpEchoState_Object = MibTableColumn
slaUdpEchoState = _SlaUdpEchoState_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 7, 100, 1, 2),
    _SlaUdpEchoState_Type()
)
slaUdpEchoState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaUdpEchoState.setStatus("current")
_SlaUdpEchoTargetIp_Type = IpAddress
_SlaUdpEchoTargetIp_Object = MibTableColumn
slaUdpEchoTargetIp = _SlaUdpEchoTargetIp_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 7, 100, 1, 3),
    _SlaUdpEchoTargetIp_Type()
)
slaUdpEchoTargetIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaUdpEchoTargetIp.setStatus("current")


class _SlaUdpEchoTargetPort_Type(Unsigned32):
    """Custom type slaUdpEchoTargetPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SlaUdpEchoTargetPort_Type.__name__ = "Unsigned32"
_SlaUdpEchoTargetPort_Object = MibTableColumn
slaUdpEchoTargetPort = _SlaUdpEchoTargetPort_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 7, 100, 1, 4),
    _SlaUdpEchoTargetPort_Type()
)
slaUdpEchoTargetPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaUdpEchoTargetPort.setStatus("current")


class _SlaUdpEchoPktLen_Type(Integer32):
    """Custom type slaUdpEchoPktLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 1500),
    )


_SlaUdpEchoPktLen_Type.__name__ = "Integer32"
_SlaUdpEchoPktLen_Object = MibTableColumn
slaUdpEchoPktLen = _SlaUdpEchoPktLen_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 7, 100, 1, 5),
    _SlaUdpEchoPktLen_Type()
)
slaUdpEchoPktLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaUdpEchoPktLen.setStatus("current")


class _SlaUdpEchoSchInterval_Type(Unsigned32):
    """Custom type slaUdpEchoSchInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SlaUdpEchoSchInterval_Type.__name__ = "Unsigned32"
_SlaUdpEchoSchInterval_Object = MibTableColumn
slaUdpEchoSchInterval = _SlaUdpEchoSchInterval_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 7, 100, 1, 6),
    _SlaUdpEchoSchInterval_Type()
)
slaUdpEchoSchInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaUdpEchoSchInterval.setStatus("current")
_SlaUdpEchoSourceIp_Type = IpAddress
_SlaUdpEchoSourceIp_Object = MibTableColumn
slaUdpEchoSourceIp = _SlaUdpEchoSourceIp_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 7, 100, 1, 7),
    _SlaUdpEchoSourceIp_Type()
)
slaUdpEchoSourceIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaUdpEchoSourceIp.setStatus("current")


class _SlaUdpEchoSourcePort_Type(Unsigned32):
    """Custom type slaUdpEchoSourcePort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SlaUdpEchoSourcePort_Type.__name__ = "Unsigned32"
_SlaUdpEchoSourcePort_Object = MibTableColumn
slaUdpEchoSourcePort = _SlaUdpEchoSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 7, 100, 1, 8),
    _SlaUdpEchoSourcePort_Type()
)
slaUdpEchoSourcePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaUdpEchoSourcePort.setStatus("current")


class _SlaUdpEchoTimeout_Type(Unsigned32):
    """Custom type slaUdpEchoTimeout based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 604800000),
    )


_SlaUdpEchoTimeout_Type.__name__ = "Unsigned32"
_SlaUdpEchoTimeout_Object = MibTableColumn
slaUdpEchoTimeout = _SlaUdpEchoTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 7, 100, 1, 9),
    _SlaUdpEchoTimeout_Type()
)
slaUdpEchoTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaUdpEchoTimeout.setStatus("current")


class _SlaUdpEchoVrfName_Type(DisplayString):
    """Custom type slaUdpEchoVrfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_SlaUdpEchoVrfName_Type.__name__ = "DisplayString"
_SlaUdpEchoVrfName_Object = MibTableColumn
slaUdpEchoVrfName = _SlaUdpEchoVrfName_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 7, 100, 1, 10),
    _SlaUdpEchoVrfName_Type()
)
slaUdpEchoVrfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaUdpEchoVrfName.setStatus("current")


class _SlaUdpEchoTos_Type(Integer32):
    """Custom type slaUdpEchoTos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SlaUdpEchoTos_Type.__name__ = "Integer32"
_SlaUdpEchoTos_Object = MibTableColumn
slaUdpEchoTos = _SlaUdpEchoTos_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 7, 100, 1, 11),
    _SlaUdpEchoTos_Type()
)
slaUdpEchoTos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaUdpEchoTos.setStatus("current")


class _SlaUdpEchoHistorySize_Type(Integer32):
    """Custom type slaUdpEchoHistorySize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SlaUdpEchoHistorySize_Type.__name__ = "Integer32"
_SlaUdpEchoHistorySize_Object = MibTableColumn
slaUdpEchoHistorySize = _SlaUdpEchoHistorySize_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 7, 100, 1, 12),
    _SlaUdpEchoHistorySize_Type()
)
slaUdpEchoHistorySize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaUdpEchoHistorySize.setStatus("current")


class _SlaUdpEchoPeriods_Type(Integer32):
    """Custom type slaUdpEchoPeriods based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_SlaUdpEchoPeriods_Type.__name__ = "Integer32"
_SlaUdpEchoPeriods_Object = MibTableColumn
slaUdpEchoPeriods = _SlaUdpEchoPeriods_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 7, 100, 1, 13),
    _SlaUdpEchoPeriods_Type()
)
slaUdpEchoPeriods.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaUdpEchoPeriods.setStatus("current")


class _SlaUdpEchoAlarmType_Type(Integer32):
    """Custom type slaUdpEchoAlarmType based on Integer32"""
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
        *(("log", 1),
          ("logAndTrap", 3),
          ("noLogAndtrap", 4),
          ("trap", 2))
    )


_SlaUdpEchoAlarmType_Type.__name__ = "Integer32"
_SlaUdpEchoAlarmType_Object = MibTableColumn
slaUdpEchoAlarmType = _SlaUdpEchoAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 7, 100, 1, 14),
    _SlaUdpEchoAlarmType_Type()
)
slaUdpEchoAlarmType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaUdpEchoAlarmType.setStatus("current")
_SlaUdpEchoTableRowStatus_Type = RowStatus
_SlaUdpEchoTableRowStatus_Object = MibTableColumn
slaUdpEchoTableRowStatus = _SlaUdpEchoTableRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 7, 100, 1, 15),
    _SlaUdpEchoTableRowStatus_Type()
)
slaUdpEchoTableRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaUdpEchoTableRowStatus.setStatus("current")
_SysSlaUdpEchoHistoryTable_Object = MibTable
sysSlaUdpEchoHistoryTable = _SysSlaUdpEchoHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 7, 200)
)
if mibBuilder.loadTexts:
    sysSlaUdpEchoHistoryTable.setStatus("current")
_SysSlaUdpEchoHistoryEntry_Object = MibTableRow
sysSlaUdpEchoHistoryEntry = _SysSlaUdpEchoHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 7, 200, 1)
)
sysSlaUdpEchoHistoryEntry.setIndexNames(
    (0, "MPSLA", "slaUdpEchoHisTableEntityId"),
    (0, "MPSLA", "slaUdpEchoHistoryIndex"),
)
if mibBuilder.loadTexts:
    sysSlaUdpEchoHistoryEntry.setStatus("current")


class _SlaUdpEchoHisTableEntityId_Type(Integer32):
    """Custom type slaUdpEchoHisTableEntityId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000),
    )


_SlaUdpEchoHisTableEntityId_Type.__name__ = "Integer32"
_SlaUdpEchoHisTableEntityId_Object = MibTableColumn
slaUdpEchoHisTableEntityId = _SlaUdpEchoHisTableEntityId_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 7, 200, 1, 1),
    _SlaUdpEchoHisTableEntityId_Type()
)
slaUdpEchoHisTableEntityId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaUdpEchoHisTableEntityId.setStatus("current")


class _SlaUdpEchoHistoryIndex_Type(Integer32):
    """Custom type slaUdpEchoHistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SlaUdpEchoHistoryIndex_Type.__name__ = "Integer32"
_SlaUdpEchoHistoryIndex_Object = MibTableColumn
slaUdpEchoHistoryIndex = _SlaUdpEchoHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 7, 200, 1, 2),
    _SlaUdpEchoHistoryIndex_Type()
)
slaUdpEchoHistoryIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaUdpEchoHistoryIndex.setStatus("current")
_SlaUdpEchoPktLoss_Type = Integer32
_SlaUdpEchoPktLoss_Object = MibTableColumn
slaUdpEchoPktLoss = _SlaUdpEchoPktLoss_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 7, 200, 1, 3),
    _SlaUdpEchoPktLoss_Type()
)
slaUdpEchoPktLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaUdpEchoPktLoss.setStatus("current")
_SlaUdpEchoRtt_Type = Integer32
_SlaUdpEchoRtt_Object = MibTableColumn
slaUdpEchoRtt = _SlaUdpEchoRtt_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 7, 200, 1, 4),
    _SlaUdpEchoRtt_Type()
)
slaUdpEchoRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaUdpEchoRtt.setStatus("current")


class _SlaUdpEchoTime_Type(DisplayString):
    """Custom type slaUdpEchoTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_SlaUdpEchoTime_Type.__name__ = "DisplayString"
_SlaUdpEchoTime_Object = MibTableColumn
slaUdpEchoTime = _SlaUdpEchoTime_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 7, 200, 1, 5),
    _SlaUdpEchoTime_Type()
)
slaUdpEchoTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaUdpEchoTime.setStatus("current")
_SlaUdpEchoHisTableRowStatus_Type = RowStatus
_SlaUdpEchoHisTableRowStatus_Object = MibTableColumn
slaUdpEchoHisTableRowStatus = _SlaUdpEchoHisTableRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 7, 200, 1, 6),
    _SlaUdpEchoHisTableRowStatus_Type()
)
slaUdpEchoHisTableRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaUdpEchoHisTableRowStatus.setStatus("current")
_SysSlaFlStaMgt_ObjectIdentity = ObjectIdentity
sysSlaFlStaMgt = _SysSlaFlStaMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 8)
)
_SysSlaFlStaTable_Object = MibTable
sysSlaFlStaTable = _SysSlaFlStaTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 8, 100)
)
if mibBuilder.loadTexts:
    sysSlaFlStaTable.setStatus("current")
_SysSlaFlStaEntry_Object = MibTableRow
sysSlaFlStaEntry = _SysSlaFlStaEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 8, 100, 1)
)
sysSlaFlStaEntry.setIndexNames(
    (0, "MPSLA", "slaFlStaTableEntityId"),
)
if mibBuilder.loadTexts:
    sysSlaFlStaEntry.setStatus("current")


class _SlaFlStaTableEntityId_Type(Integer32):
    """Custom type slaFlStaTableEntityId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000),
    )


_SlaFlStaTableEntityId_Type.__name__ = "Integer32"
_SlaFlStaTableEntityId_Object = MibTableColumn
slaFlStaTableEntityId = _SlaFlStaTableEntityId_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 8, 100, 1, 1),
    _SlaFlStaTableEntityId_Type()
)
slaFlStaTableEntityId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaFlStaTableEntityId.setStatus("current")


class _SlaFlStaIfName_Type(DisplayString):
    """Custom type slaFlStaIfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_SlaFlStaIfName_Type.__name__ = "DisplayString"
_SlaFlStaIfName_Object = MibTableColumn
slaFlStaIfName = _SlaFlStaIfName_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 8, 100, 1, 2),
    _SlaFlStaIfName_Type()
)
slaFlStaIfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaFlStaIfName.setStatus("current")


class _SlaFlStaInterval_Type(Integer32):
    """Custom type slaFlStaInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 600),
    )


_SlaFlStaInterval_Type.__name__ = "Integer32"
_SlaFlStaInterval_Object = MibTableColumn
slaFlStaInterval = _SlaFlStaInterval_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 8, 100, 1, 3),
    _SlaFlStaInterval_Type()
)
slaFlStaInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaFlStaInterval.setStatus("current")


class _SlaFlStaHistorySize_Type(Integer32):
    """Custom type slaFlStaHistorySize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SlaFlStaHistorySize_Type.__name__ = "Integer32"
_SlaFlStaHistorySize_Object = MibTableColumn
slaFlStaHistorySize = _SlaFlStaHistorySize_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 8, 100, 1, 4),
    _SlaFlStaHistorySize_Type()
)
slaFlStaHistorySize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaFlStaHistorySize.setStatus("current")


class _SlaFlStaPeriods_Type(Integer32):
    """Custom type slaFlStaPeriods based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 500),
    )


_SlaFlStaPeriods_Type.__name__ = "Integer32"
_SlaFlStaPeriods_Object = MibTableColumn
slaFlStaPeriods = _SlaFlStaPeriods_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 8, 100, 1, 5),
    _SlaFlStaPeriods_Type()
)
slaFlStaPeriods.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaFlStaPeriods.setStatus("current")


class _SlaFlStaAlarmType_Type(Integer32):
    """Custom type slaFlStaAlarmType based on Integer32"""
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
        *(("log", 1),
          ("logAndTrap", 3),
          ("noLogAndtrap", 4),
          ("trap", 2))
    )


_SlaFlStaAlarmType_Type.__name__ = "Integer32"
_SlaFlStaAlarmType_Object = MibTableColumn
slaFlStaAlarmType = _SlaFlStaAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 8, 100, 1, 6),
    _SlaFlStaAlarmType_Type()
)
slaFlStaAlarmType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaFlStaAlarmType.setStatus("current")
_SlaFlStaTableRowStatus_Type = RowStatus
_SlaFlStaTableRowStatus_Object = MibTableColumn
slaFlStaTableRowStatus = _SlaFlStaTableRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 8, 100, 1, 7),
    _SlaFlStaTableRowStatus_Type()
)
slaFlStaTableRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaFlStaTableRowStatus.setStatus("current")
_SysSlaFlStaHistoryTable_Object = MibTable
sysSlaFlStaHistoryTable = _SysSlaFlStaHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 8, 200)
)
if mibBuilder.loadTexts:
    sysSlaFlStaHistoryTable.setStatus("current")
_SysSlaFlStaHistoryEntry_Object = MibTableRow
sysSlaFlStaHistoryEntry = _SysSlaFlStaHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 8, 200, 1)
)
sysSlaFlStaHistoryEntry.setIndexNames(
    (0, "MPSLA", "slaFlStaHisTableEntityId"),
    (0, "MPSLA", "slaFlStaHistoryIndex"),
)
if mibBuilder.loadTexts:
    sysSlaFlStaHistoryEntry.setStatus("current")


class _SlaFlStaHisTableEntityId_Type(Integer32):
    """Custom type slaFlStaHisTableEntityId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000),
    )


_SlaFlStaHisTableEntityId_Type.__name__ = "Integer32"
_SlaFlStaHisTableEntityId_Object = MibTableColumn
slaFlStaHisTableEntityId = _SlaFlStaHisTableEntityId_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 8, 200, 1, 1),
    _SlaFlStaHisTableEntityId_Type()
)
slaFlStaHisTableEntityId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaFlStaHisTableEntityId.setStatus("current")


class _SlaFlStaHistoryIndex_Type(Integer32):
    """Custom type slaFlStaHistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SlaFlStaHistoryIndex_Type.__name__ = "Integer32"
_SlaFlStaHistoryIndex_Object = MibTableColumn
slaFlStaHistoryIndex = _SlaFlStaHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 8, 200, 1, 2),
    _SlaFlStaHistoryIndex_Type()
)
slaFlStaHistoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaFlStaHistoryIndex.setStatus("current")
_SlaFlStaInputPkts_Type = Integer32
_SlaFlStaInputPkts_Object = MibTableColumn
slaFlStaInputPkts = _SlaFlStaInputPkts_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 8, 200, 1, 3),
    _SlaFlStaInputPkts_Type()
)
slaFlStaInputPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaFlStaInputPkts.setStatus("current")
_SlaFlStaInputFlow_Type = Integer32
_SlaFlStaInputFlow_Object = MibTableColumn
slaFlStaInputFlow = _SlaFlStaInputFlow_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 8, 200, 1, 4),
    _SlaFlStaInputFlow_Type()
)
slaFlStaInputFlow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaFlStaInputFlow.setStatus("current")
_SlaFlStaOutputPkts_Type = Integer32
_SlaFlStaOutputPkts_Object = MibTableColumn
slaFlStaOutputPkts = _SlaFlStaOutputPkts_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 8, 200, 1, 5),
    _SlaFlStaOutputPkts_Type()
)
slaFlStaOutputPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaFlStaOutputPkts.setStatus("current")
_SlaFlStaOutputFlow_Type = Integer32
_SlaFlStaOutputFlow_Object = MibTableColumn
slaFlStaOutputFlow = _SlaFlStaOutputFlow_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 8, 200, 1, 6),
    _SlaFlStaOutputFlow_Type()
)
slaFlStaOutputFlow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaFlStaOutputFlow.setStatus("current")


class _SlaFlStaTime_Type(DisplayString):
    """Custom type slaFlStaTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_SlaFlStaTime_Type.__name__ = "DisplayString"
_SlaFlStaTime_Object = MibTableColumn
slaFlStaTime = _SlaFlStaTime_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 8, 200, 1, 7),
    _SlaFlStaTime_Type()
)
slaFlStaTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaFlStaTime.setStatus("current")
_SlaFlStaHisTableRowStatus_Type = RowStatus
_SlaFlStaHisTableRowStatus_Object = MibTableColumn
slaFlStaHisTableRowStatus = _SlaFlStaHisTableRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 8, 200, 1, 8),
    _SlaFlStaHisTableRowStatus_Type()
)
slaFlStaHisTableRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaFlStaHisTableRowStatus.setStatus("current")
_SysSlaIcmpPathJitMgt_ObjectIdentity = ObjectIdentity
sysSlaIcmpPathJitMgt = _SysSlaIcmpPathJitMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 9)
)
_SysSlaIcmpPathJitTable_Object = MibTable
sysSlaIcmpPathJitTable = _SysSlaIcmpPathJitTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 9, 100)
)
if mibBuilder.loadTexts:
    sysSlaIcmpPathJitTable.setStatus("current")
_SysSlaIcmpPathJitEntry_Object = MibTableRow
sysSlaIcmpPathJitEntry = _SysSlaIcmpPathJitEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 9, 100, 1)
)
sysSlaIcmpPathJitEntry.setIndexNames(
    (0, "MPSLA", "slaIcmpPJTableEntityId"),
)
if mibBuilder.loadTexts:
    sysSlaIcmpPathJitEntry.setStatus("current")


class _SlaIcmpPJTableEntityId_Type(Integer32):
    """Custom type slaIcmpPJTableEntityId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000),
    )


_SlaIcmpPJTableEntityId_Type.__name__ = "Integer32"
_SlaIcmpPJTableEntityId_Object = MibTableColumn
slaIcmpPJTableEntityId = _SlaIcmpPJTableEntityId_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 9, 100, 1, 1),
    _SlaIcmpPJTableEntityId_Type()
)
slaIcmpPJTableEntityId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaIcmpPJTableEntityId.setStatus("current")
_SlaIcmpPJTargetIp_Type = IpAddress
_SlaIcmpPJTargetIp_Object = MibTableColumn
slaIcmpPJTargetIp = _SlaIcmpPJTargetIp_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 9, 100, 1, 2),
    _SlaIcmpPJTargetIp_Type()
)
slaIcmpPJTargetIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaIcmpPJTargetIp.setStatus("current")


class _SlaIcmpPJPktNum_Type(Unsigned32):
    """Custom type slaIcmpPJPktNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200000000),
    )


_SlaIcmpPJPktNum_Type.__name__ = "Unsigned32"
_SlaIcmpPJPktNum_Object = MibTableColumn
slaIcmpPJPktNum = _SlaIcmpPJPktNum_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 9, 100, 1, 3),
    _SlaIcmpPJPktNum_Type()
)
slaIcmpPJPktNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaIcmpPJPktNum.setStatus("current")


class _SlaIcmpPJPktLen_Type(Integer32):
    """Custom type slaIcmpPJPktLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(36, 18024),
    )


_SlaIcmpPJPktLen_Type.__name__ = "Integer32"
_SlaIcmpPJPktLen_Object = MibTableColumn
slaIcmpPJPktLen = _SlaIcmpPJPktLen_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 9, 100, 1, 4),
    _SlaIcmpPJPktLen_Type()
)
slaIcmpPJPktLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaIcmpPJPktLen.setStatus("current")


class _SlaIcmpPJTimeout_Type(Integer32):
    """Custom type slaIcmpPJTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 604800000),
    )


_SlaIcmpPJTimeout_Type.__name__ = "Integer32"
_SlaIcmpPJTimeout_Object = MibTableColumn
slaIcmpPJTimeout = _SlaIcmpPJTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 9, 100, 1, 5),
    _SlaIcmpPJTimeout_Type()
)
slaIcmpPJTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaIcmpPJTimeout.setStatus("current")


class _SlaIcmpPJPktInterval_Type(Unsigned32):
    """Custom type slaIcmpPJPktInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 6000),
    )


_SlaIcmpPJPktInterval_Type.__name__ = "Unsigned32"
_SlaIcmpPJPktInterval_Object = MibTableColumn
slaIcmpPJPktInterval = _SlaIcmpPJPktInterval_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 9, 100, 1, 6),
    _SlaIcmpPJPktInterval_Type()
)
slaIcmpPJPktInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaIcmpPJPktInterval.setStatus("current")


class _SlaIcmpPJSchInterval_Type(Unsigned32):
    """Custom type slaIcmpPJSchInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 604800),
    )


_SlaIcmpPJSchInterval_Type.__name__ = "Unsigned32"
_SlaIcmpPJSchInterval_Object = MibTableColumn
slaIcmpPJSchInterval = _SlaIcmpPJSchInterval_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 9, 100, 1, 7),
    _SlaIcmpPJSchInterval_Type()
)
slaIcmpPJSchInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaIcmpPJSchInterval.setStatus("current")


class _SlaIcmpPJVrfName_Type(DisplayString):
    """Custom type slaIcmpPJVrfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_SlaIcmpPJVrfName_Type.__name__ = "DisplayString"
_SlaIcmpPJVrfName_Object = MibTableColumn
slaIcmpPJVrfName = _SlaIcmpPJVrfName_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 9, 100, 1, 8),
    _SlaIcmpPJVrfName_Type()
)
slaIcmpPJVrfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaIcmpPJVrfName.setStatus("current")
_SlaIcmpPJSourceIp_Type = IpAddress
_SlaIcmpPJSourceIp_Object = MibTableColumn
slaIcmpPJSourceIp = _SlaIcmpPJSourceIp_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 9, 100, 1, 9),
    _SlaIcmpPJSourceIp_Type()
)
slaIcmpPJSourceIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaIcmpPJSourceIp.setStatus("current")


class _SlaIcmpPJTos_Type(Integer32):
    """Custom type slaIcmpPJTos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SlaIcmpPJTos_Type.__name__ = "Integer32"
_SlaIcmpPJTos_Object = MibTableColumn
slaIcmpPJTos = _SlaIcmpPJTos_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 9, 100, 1, 10),
    _SlaIcmpPJTos_Type()
)
slaIcmpPJTos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaIcmpPJTos.setStatus("current")
_SlaIcmpPJVerifyData_Type = TruthValue
_SlaIcmpPJVerifyData_Object = MibTableColumn
slaIcmpPJVerifyData = _SlaIcmpPJVerifyData_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 9, 100, 1, 11),
    _SlaIcmpPJVerifyData_Type()
)
slaIcmpPJVerifyData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaIcmpPJVerifyData.setStatus("current")


class _SlaIcmpPJAlarmType_Type(Integer32):
    """Custom type slaIcmpPJAlarmType based on Integer32"""
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
        *(("log", 1),
          ("logAndTrap", 3),
          ("noLogAndtrap", 4),
          ("trap", 2))
    )


_SlaIcmpPJAlarmType_Type.__name__ = "Integer32"
_SlaIcmpPJAlarmType_Object = MibTableColumn
slaIcmpPJAlarmType = _SlaIcmpPJAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 9, 100, 1, 12),
    _SlaIcmpPJAlarmType_Type()
)
slaIcmpPJAlarmType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaIcmpPJAlarmType.setStatus("current")
_SlaIcmpPJTargetOnly_Type = TruthValue
_SlaIcmpPJTargetOnly_Object = MibTableColumn
slaIcmpPJTargetOnly = _SlaIcmpPJTargetOnly_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 9, 100, 1, 13),
    _SlaIcmpPJTargetOnly_Type()
)
slaIcmpPJTargetOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaIcmpPJTargetOnly.setStatus("current")


class _SlaIcmpPJHistorySize_Type(Integer32):
    """Custom type slaIcmpPJHistorySize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SlaIcmpPJHistorySize_Type.__name__ = "Integer32"
_SlaIcmpPJHistorySize_Object = MibTableColumn
slaIcmpPJHistorySize = _SlaIcmpPJHistorySize_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 9, 100, 1, 14),
    _SlaIcmpPJHistorySize_Type()
)
slaIcmpPJHistorySize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaIcmpPJHistorySize.setStatus("current")


class _SlaIcmpPJPeriods_Type(Integer32):
    """Custom type slaIcmpPJPeriods based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 500),
    )


_SlaIcmpPJPeriods_Type.__name__ = "Integer32"
_SlaIcmpPJPeriods_Object = MibTableColumn
slaIcmpPJPeriods = _SlaIcmpPJPeriods_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 9, 100, 1, 15),
    _SlaIcmpPJPeriods_Type()
)
slaIcmpPJPeriods.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaIcmpPJPeriods.setStatus("current")
_SlaIcmpPJLsrPath_Type = IpAddress
_SlaIcmpPJLsrPath_Object = MibTableColumn
slaIcmpPJLsrPath = _SlaIcmpPJLsrPath_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 9, 100, 1, 16),
    _SlaIcmpPJLsrPath_Type()
)
slaIcmpPJLsrPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaIcmpPJLsrPath.setStatus("current")
_SlaIcmpPJIsScheduling_Type = TruthValue
_SlaIcmpPJIsScheduling_Object = MibTableColumn
slaIcmpPJIsScheduling = _SlaIcmpPJIsScheduling_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 9, 100, 1, 17),
    _SlaIcmpPJIsScheduling_Type()
)
slaIcmpPJIsScheduling.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaIcmpPJIsScheduling.setStatus("current")
_SlaIcmpPJTableRowStatus_Type = RowStatus
_SlaIcmpPJTableRowStatus_Object = MibTableColumn
slaIcmpPJTableRowStatus = _SlaIcmpPJTableRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 9, 100, 1, 18),
    _SlaIcmpPJTableRowStatus_Type()
)
slaIcmpPJTableRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaIcmpPJTableRowStatus.setStatus("current")
_SysSlaIcmpPathJitHistoryTable_Object = MibTable
sysSlaIcmpPathJitHistoryTable = _SysSlaIcmpPathJitHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 9, 200)
)
if mibBuilder.loadTexts:
    sysSlaIcmpPathJitHistoryTable.setStatus("current")
_SysSlaIcmpPathJitHistoryEntry_Object = MibTableRow
sysSlaIcmpPathJitHistoryEntry = _SysSlaIcmpPathJitHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 9, 200, 1)
)
sysSlaIcmpPathJitHistoryEntry.setIndexNames(
    (0, "MPSLA", "slaIcmpPJHisTableEntityId"),
    (0, "MPSLA", "slaIcmpPJHopIndex"),
    (0, "MPSLA", "slaIcmpPJHistoryIndex"),
    (0, "MPSLA", "slaIcmpPJGetStatus"),
)
if mibBuilder.loadTexts:
    sysSlaIcmpPathJitHistoryEntry.setStatus("current")


class _SlaIcmpPJHisTableEntityId_Type(Integer32):
    """Custom type slaIcmpPJHisTableEntityId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000),
    )


_SlaIcmpPJHisTableEntityId_Type.__name__ = "Integer32"
_SlaIcmpPJHisTableEntityId_Object = MibTableColumn
slaIcmpPJHisTableEntityId = _SlaIcmpPJHisTableEntityId_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 9, 200, 1, 1),
    _SlaIcmpPJHisTableEntityId_Type()
)
slaIcmpPJHisTableEntityId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaIcmpPJHisTableEntityId.setStatus("current")


class _SlaIcmpPJHopIndex_Type(Integer32):
    """Custom type slaIcmpPJHopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_SlaIcmpPJHopIndex_Type.__name__ = "Integer32"
_SlaIcmpPJHopIndex_Object = MibTableColumn
slaIcmpPJHopIndex = _SlaIcmpPJHopIndex_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 9, 200, 1, 2),
    _SlaIcmpPJHopIndex_Type()
)
slaIcmpPJHopIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaIcmpPJHopIndex.setStatus("current")


class _SlaIcmpPJHistoryIndex_Type(Integer32):
    """Custom type slaIcmpPJHistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SlaIcmpPJHistoryIndex_Type.__name__ = "Integer32"
_SlaIcmpPJHistoryIndex_Object = MibTableColumn
slaIcmpPJHistoryIndex = _SlaIcmpPJHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 9, 200, 1, 3),
    _SlaIcmpPJHistoryIndex_Type()
)
slaIcmpPJHistoryIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaIcmpPJHistoryIndex.setStatus("current")


class _SlaIcmpPJRtt_Type(Integer32):
    """Custom type slaIcmpPJRtt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_SlaIcmpPJRtt_Type.__name__ = "Integer32"
_SlaIcmpPJRtt_Object = MibTableColumn
slaIcmpPJRtt = _SlaIcmpPJRtt_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 9, 200, 1, 4),
    _SlaIcmpPJRtt_Type()
)
slaIcmpPJRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaIcmpPJRtt.setStatus("current")


class _SlaIcmpPJJitter_Type(Integer32):
    """Custom type slaIcmpPJJitter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6000),
    )


_SlaIcmpPJJitter_Type.__name__ = "Integer32"
_SlaIcmpPJJitter_Object = MibTableColumn
slaIcmpPJJitter = _SlaIcmpPJJitter_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 9, 200, 1, 5),
    _SlaIcmpPJJitter_Type()
)
slaIcmpPJJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaIcmpPJJitter.setStatus("current")
_SlaIcmpPJPktLoss_Type = Integer32
_SlaIcmpPJPktLoss_Object = MibTableColumn
slaIcmpPJPktLoss = _SlaIcmpPJPktLoss_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 9, 200, 1, 6),
    _SlaIcmpPJPktLoss_Type()
)
slaIcmpPJPktLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaIcmpPJPktLoss.setStatus("current")


class _SlaIcmpPJTime_Type(DisplayString):
    """Custom type slaIcmpPJTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_SlaIcmpPJTime_Type.__name__ = "DisplayString"
_SlaIcmpPJTime_Object = MibTableColumn
slaIcmpPJTime = _SlaIcmpPJTime_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 9, 200, 1, 7),
    _SlaIcmpPJTime_Type()
)
slaIcmpPJTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaIcmpPJTime.setStatus("current")


class _SlaIcmpPJGetStatus_Type(Integer32):
    """Custom type slaIcmpPJGetStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_SlaIcmpPJGetStatus_Type.__name__ = "Integer32"
_SlaIcmpPJGetStatus_Object = MibTableColumn
slaIcmpPJGetStatus = _SlaIcmpPJGetStatus_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 9, 200, 1, 8),
    _SlaIcmpPJGetStatus_Type()
)
slaIcmpPJGetStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaIcmpPJGetStatus.setStatus("current")
_SlaIcmpPJHisTableRowStatus_Type = RowStatus
_SlaIcmpPJHisTableRowStatus_Object = MibTableColumn
slaIcmpPJHisTableRowStatus = _SlaIcmpPJHisTableRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 9, 200, 1, 9),
    _SlaIcmpPJHisTableRowStatus_Type()
)
slaIcmpPJHisTableRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaIcmpPJHisTableRowStatus.setStatus("current")
_SysSlaIcmpPathEchoMgt_ObjectIdentity = ObjectIdentity
sysSlaIcmpPathEchoMgt = _SysSlaIcmpPathEchoMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 10)
)
_SysSlaIcmpPathEchoTable_Object = MibTable
sysSlaIcmpPathEchoTable = _SysSlaIcmpPathEchoTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 10, 100)
)
if mibBuilder.loadTexts:
    sysSlaIcmpPathEchoTable.setStatus("current")
_SysSlaIcmpPathEchoEntry_Object = MibTableRow
sysSlaIcmpPathEchoEntry = _SysSlaIcmpPathEchoEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 10, 100, 1)
)
sysSlaIcmpPathEchoEntry.setIndexNames(
    (0, "MPSLA", "slaIcmpPETableEntityId"),
)
if mibBuilder.loadTexts:
    sysSlaIcmpPathEchoEntry.setStatus("current")


class _SlaIcmpPETableEntityId_Type(Integer32):
    """Custom type slaIcmpPETableEntityId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000),
    )


_SlaIcmpPETableEntityId_Type.__name__ = "Integer32"
_SlaIcmpPETableEntityId_Object = MibTableColumn
slaIcmpPETableEntityId = _SlaIcmpPETableEntityId_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 10, 100, 1, 1),
    _SlaIcmpPETableEntityId_Type()
)
slaIcmpPETableEntityId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaIcmpPETableEntityId.setStatus("current")
_SlaIcmpPETargetIp_Type = IpAddress
_SlaIcmpPETargetIp_Object = MibTableColumn
slaIcmpPETargetIp = _SlaIcmpPETargetIp_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 10, 100, 1, 2),
    _SlaIcmpPETargetIp_Type()
)
slaIcmpPETargetIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaIcmpPETargetIp.setStatus("current")


class _SlaIcmpPEPktLen_Type(Integer32):
    """Custom type slaIcmpPEPktLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(36, 18024),
    )


_SlaIcmpPEPktLen_Type.__name__ = "Integer32"
_SlaIcmpPEPktLen_Object = MibTableColumn
slaIcmpPEPktLen = _SlaIcmpPEPktLen_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 10, 100, 1, 3),
    _SlaIcmpPEPktLen_Type()
)
slaIcmpPEPktLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaIcmpPEPktLen.setStatus("current")


class _SlaIcmpPETimeout_Type(Integer32):
    """Custom type slaIcmpPETimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 604800000),
    )


_SlaIcmpPETimeout_Type.__name__ = "Integer32"
_SlaIcmpPETimeout_Object = MibTableColumn
slaIcmpPETimeout = _SlaIcmpPETimeout_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 10, 100, 1, 4),
    _SlaIcmpPETimeout_Type()
)
slaIcmpPETimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaIcmpPETimeout.setStatus("current")


class _SlaIcmpPESchInterval_Type(Unsigned32):
    """Custom type slaIcmpPESchInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SlaIcmpPESchInterval_Type.__name__ = "Unsigned32"
_SlaIcmpPESchInterval_Object = MibTableColumn
slaIcmpPESchInterval = _SlaIcmpPESchInterval_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 10, 100, 1, 5),
    _SlaIcmpPESchInterval_Type()
)
slaIcmpPESchInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaIcmpPESchInterval.setStatus("current")


class _SlaIcmpPEVrfName_Type(DisplayString):
    """Custom type slaIcmpPEVrfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_SlaIcmpPEVrfName_Type.__name__ = "DisplayString"
_SlaIcmpPEVrfName_Object = MibTableColumn
slaIcmpPEVrfName = _SlaIcmpPEVrfName_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 10, 100, 1, 6),
    _SlaIcmpPEVrfName_Type()
)
slaIcmpPEVrfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaIcmpPEVrfName.setStatus("current")
_SlaIcmpPESourceIp_Type = IpAddress
_SlaIcmpPESourceIp_Object = MibTableColumn
slaIcmpPESourceIp = _SlaIcmpPESourceIp_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 10, 100, 1, 7),
    _SlaIcmpPESourceIp_Type()
)
slaIcmpPESourceIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaIcmpPESourceIp.setStatus("current")


class _SlaIcmpPETos_Type(Integer32):
    """Custom type slaIcmpPETos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SlaIcmpPETos_Type.__name__ = "Integer32"
_SlaIcmpPETos_Object = MibTableColumn
slaIcmpPETos = _SlaIcmpPETos_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 10, 100, 1, 8),
    _SlaIcmpPETos_Type()
)
slaIcmpPETos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaIcmpPETos.setStatus("current")
_SlaIcmpPEVerifyData_Type = TruthValue
_SlaIcmpPEVerifyData_Object = MibTableColumn
slaIcmpPEVerifyData = _SlaIcmpPEVerifyData_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 10, 100, 1, 9),
    _SlaIcmpPEVerifyData_Type()
)
slaIcmpPEVerifyData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaIcmpPEVerifyData.setStatus("current")
_SlaIcmpPELsrPath_Type = IpAddress
_SlaIcmpPELsrPath_Object = MibTableColumn
slaIcmpPELsrPath = _SlaIcmpPELsrPath_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 10, 100, 1, 10),
    _SlaIcmpPELsrPath_Type()
)
slaIcmpPELsrPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaIcmpPELsrPath.setStatus("current")


class _SlaIcmpPEHistorySize_Type(Integer32):
    """Custom type slaIcmpPEHistorySize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SlaIcmpPEHistorySize_Type.__name__ = "Integer32"
_SlaIcmpPEHistorySize_Object = MibTableColumn
slaIcmpPEHistorySize = _SlaIcmpPEHistorySize_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 10, 100, 1, 11),
    _SlaIcmpPEHistorySize_Type()
)
slaIcmpPEHistorySize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaIcmpPEHistorySize.setStatus("current")


class _SlaIcmpPEPeriods_Type(Integer32):
    """Custom type slaIcmpPEPeriods based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 500),
    )


_SlaIcmpPEPeriods_Type.__name__ = "Integer32"
_SlaIcmpPEPeriods_Object = MibTableColumn
slaIcmpPEPeriods = _SlaIcmpPEPeriods_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 10, 100, 1, 12),
    _SlaIcmpPEPeriods_Type()
)
slaIcmpPEPeriods.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaIcmpPEPeriods.setStatus("current")


class _SlaIcmpPEAlarmType_Type(Integer32):
    """Custom type slaIcmpPEAlarmType based on Integer32"""
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
        *(("log", 1),
          ("logAndTrap", 3),
          ("noLogAndtrap", 4),
          ("trap", 2))
    )


_SlaIcmpPEAlarmType_Type.__name__ = "Integer32"
_SlaIcmpPEAlarmType_Object = MibTableColumn
slaIcmpPEAlarmType = _SlaIcmpPEAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 10, 100, 1, 13),
    _SlaIcmpPEAlarmType_Type()
)
slaIcmpPEAlarmType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaIcmpPEAlarmType.setStatus("current")
_SlaIcmpPETargetOnly_Type = TruthValue
_SlaIcmpPETargetOnly_Object = MibTableColumn
slaIcmpPETargetOnly = _SlaIcmpPETargetOnly_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 10, 100, 1, 14),
    _SlaIcmpPETargetOnly_Type()
)
slaIcmpPETargetOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaIcmpPETargetOnly.setStatus("current")
_SlaIcmpPEIsScheduling_Type = TruthValue
_SlaIcmpPEIsScheduling_Object = MibTableColumn
slaIcmpPEIsScheduling = _SlaIcmpPEIsScheduling_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 10, 100, 1, 15),
    _SlaIcmpPEIsScheduling_Type()
)
slaIcmpPEIsScheduling.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaIcmpPEIsScheduling.setStatus("current")
_SlaIcmpPETableRowStatus_Type = RowStatus
_SlaIcmpPETableRowStatus_Object = MibTableColumn
slaIcmpPETableRowStatus = _SlaIcmpPETableRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 10, 100, 1, 16),
    _SlaIcmpPETableRowStatus_Type()
)
slaIcmpPETableRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaIcmpPETableRowStatus.setStatus("current")
_SysSlaIcmpPathEchoHistoryTable_Object = MibTable
sysSlaIcmpPathEchoHistoryTable = _SysSlaIcmpPathEchoHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 10, 200)
)
if mibBuilder.loadTexts:
    sysSlaIcmpPathEchoHistoryTable.setStatus("current")
_SysSlaIcmpPathEchoHistoryEntry_Object = MibTableRow
sysSlaIcmpPathEchoHistoryEntry = _SysSlaIcmpPathEchoHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 10, 200, 1)
)
sysSlaIcmpPathEchoHistoryEntry.setIndexNames(
    (0, "MPSLA", "slaIcmpPEHisTableEntityId"),
    (0, "MPSLA", "slaIcmpPEHopIndex"),
    (0, "MPSLA", "slaIcmpPEHistoryIndex"),
    (0, "MPSLA", "slaIcmpPEGetStatus"),
)
if mibBuilder.loadTexts:
    sysSlaIcmpPathEchoHistoryEntry.setStatus("current")


class _SlaIcmpPEHisTableEntityId_Type(Integer32):
    """Custom type slaIcmpPEHisTableEntityId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000),
    )


_SlaIcmpPEHisTableEntityId_Type.__name__ = "Integer32"
_SlaIcmpPEHisTableEntityId_Object = MibTableColumn
slaIcmpPEHisTableEntityId = _SlaIcmpPEHisTableEntityId_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 10, 200, 1, 1),
    _SlaIcmpPEHisTableEntityId_Type()
)
slaIcmpPEHisTableEntityId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaIcmpPEHisTableEntityId.setStatus("current")


class _SlaIcmpPEHopIndex_Type(Integer32):
    """Custom type slaIcmpPEHopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_SlaIcmpPEHopIndex_Type.__name__ = "Integer32"
_SlaIcmpPEHopIndex_Object = MibTableColumn
slaIcmpPEHopIndex = _SlaIcmpPEHopIndex_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 10, 200, 1, 2),
    _SlaIcmpPEHopIndex_Type()
)
slaIcmpPEHopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaIcmpPEHopIndex.setStatus("current")
_SlaIcmpPEHistoryIndex_Type = Integer32
_SlaIcmpPEHistoryIndex_Object = MibTableColumn
slaIcmpPEHistoryIndex = _SlaIcmpPEHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 10, 200, 1, 3),
    _SlaIcmpPEHistoryIndex_Type()
)
slaIcmpPEHistoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaIcmpPEHistoryIndex.setStatus("current")


class _SlaIcmpPERtt_Type(Integer32):
    """Custom type slaIcmpPERtt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_SlaIcmpPERtt_Type.__name__ = "Integer32"
_SlaIcmpPERtt_Object = MibTableColumn
slaIcmpPERtt = _SlaIcmpPERtt_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 10, 200, 1, 4),
    _SlaIcmpPERtt_Type()
)
slaIcmpPERtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaIcmpPERtt.setStatus("current")


class _SlaIcmpPEPktLoss_Type(Integer32):
    """Custom type slaIcmpPEPktLoss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_SlaIcmpPEPktLoss_Type.__name__ = "Integer32"
_SlaIcmpPEPktLoss_Object = MibTableColumn
slaIcmpPEPktLoss = _SlaIcmpPEPktLoss_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 10, 200, 1, 5),
    _SlaIcmpPEPktLoss_Type()
)
slaIcmpPEPktLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaIcmpPEPktLoss.setStatus("current")


class _SlaIcmpPETime_Type(DisplayString):
    """Custom type slaIcmpPETime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 29),
    )


_SlaIcmpPETime_Type.__name__ = "DisplayString"
_SlaIcmpPETime_Object = MibTableColumn
slaIcmpPETime = _SlaIcmpPETime_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 10, 200, 1, 6),
    _SlaIcmpPETime_Type()
)
slaIcmpPETime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaIcmpPETime.setStatus("current")


class _SlaIcmpPEGetStatus_Type(Integer32):
    """Custom type slaIcmpPEGetStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_SlaIcmpPEGetStatus_Type.__name__ = "Integer32"
_SlaIcmpPEGetStatus_Object = MibTableColumn
slaIcmpPEGetStatus = _SlaIcmpPEGetStatus_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 10, 200, 1, 7),
    _SlaIcmpPEGetStatus_Type()
)
slaIcmpPEGetStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaIcmpPEGetStatus.setStatus("current")
_SlaIcmpPEHisTableRowStatus_Type = RowStatus
_SlaIcmpPEHisTableRowStatus_Object = MibTableColumn
slaIcmpPEHisTableRowStatus = _SlaIcmpPEHisTableRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 10, 200, 1, 8),
    _SlaIcmpPEHisTableRowStatus_Type()
)
slaIcmpPEHisTableRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaIcmpPEHisTableRowStatus.setStatus("current")
_SysSlaThresholdMgt_ObjectIdentity = ObjectIdentity
sysSlaThresholdMgt = _SysSlaThresholdMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 11)
)
_SysSlaThresholdTable_Object = MibTable
sysSlaThresholdTable = _SysSlaThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 11, 100)
)
if mibBuilder.loadTexts:
    sysSlaThresholdTable.setStatus("current")
_SysSlaThresholdEntry_Object = MibTableRow
sysSlaThresholdEntry = _SysSlaThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 11, 100, 1)
)
sysSlaThresholdEntry.setIndexNames(
    (0, "MPSLA", "slaThresholdTableEntityId"),
    (0, "MPSLA", "slaThresholdString"),
    (0, "MPSLA", "slaThresholdIndex"),
)
if mibBuilder.loadTexts:
    sysSlaThresholdEntry.setStatus("current")


class _SlaThresholdTableEntityId_Type(Integer32):
    """Custom type slaThresholdTableEntityId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000),
    )


_SlaThresholdTableEntityId_Type.__name__ = "Integer32"
_SlaThresholdTableEntityId_Object = MibTableColumn
slaThresholdTableEntityId = _SlaThresholdTableEntityId_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 11, 100, 1, 1),
    _SlaThresholdTableEntityId_Type()
)
slaThresholdTableEntityId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaThresholdTableEntityId.setStatus("current")


class _SlaThresholdString_Type(DisplayString):
    """Custom type slaThresholdString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 29),
    )


_SlaThresholdString_Type.__name__ = "DisplayString"
_SlaThresholdString_Object = MibTableColumn
slaThresholdString = _SlaThresholdString_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 11, 100, 1, 2),
    _SlaThresholdString_Type()
)
slaThresholdString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaThresholdString.setStatus("current")
_SlaThresholdValue_Type = Integer32
_SlaThresholdValue_Object = MibTableColumn
slaThresholdValue = _SlaThresholdValue_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 11, 100, 1, 3),
    _SlaThresholdValue_Type()
)
slaThresholdValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaThresholdValue.setStatus("current")


class _SlaThresholdDirection_Type(Integer32):
    """Custom type slaThresholdDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_SlaThresholdDirection_Type.__name__ = "Integer32"
_SlaThresholdDirection_Object = MibTableColumn
slaThresholdDirection = _SlaThresholdDirection_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 11, 100, 1, 4),
    _SlaThresholdDirection_Type()
)
slaThresholdDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaThresholdDirection.setStatus("current")
_SlaThresholdIndex_Type = Integer32
_SlaThresholdIndex_Object = MibTableColumn
slaThresholdIndex = _SlaThresholdIndex_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 11, 100, 1, 5),
    _SlaThresholdIndex_Type()
)
slaThresholdIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaThresholdIndex.setStatus("current")
_SlaThresholdRowStatus_Type = RowStatus
_SlaThresholdRowStatus_Object = MibTableColumn
slaThresholdRowStatus = _SlaThresholdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 11, 100, 1, 6),
    _SlaThresholdRowStatus_Type()
)
slaThresholdRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaThresholdRowStatus.setStatus("current")
_SysSlaMacPingMgt_ObjectIdentity = ObjectIdentity
sysSlaMacPingMgt = _SysSlaMacPingMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 12)
)
_MpMacPingTraps_ObjectIdentity = ObjectIdentity
mpMacPingTraps = _MpMacPingTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 12, 1)
)
_SysSlaMacPingTable_Object = MibTable
sysSlaMacPingTable = _SysSlaMacPingTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 12, 100)
)
if mibBuilder.loadTexts:
    sysSlaMacPingTable.setStatus("current")
_SysSlaMacPingEntry_Object = MibTableRow
sysSlaMacPingEntry = _SysSlaMacPingEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 12, 100, 1)
)
sysSlaMacPingEntry.setIndexNames(
    (0, "MPSLA", "slaMacPingEntityId"),
)
if mibBuilder.loadTexts:
    sysSlaMacPingEntry.setStatus("current")


class _SlaMacPingEntityId_Type(Integer32):
    """Custom type slaMacPingEntityId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000),
    )


_SlaMacPingEntityId_Type.__name__ = "Integer32"
_SlaMacPingEntityId_Object = MibTableColumn
slaMacPingEntityId = _SlaMacPingEntityId_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 12, 100, 1, 1),
    _SlaMacPingEntityId_Type()
)
slaMacPingEntityId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaMacPingEntityId.setStatus("current")


class _SlaMacPingState_Type(Integer32):
    """Custom type slaMacPingState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("pause", 3),
          ("run", 2),
          ("stop", 1))
    )


_SlaMacPingState_Type.__name__ = "Integer32"
_SlaMacPingState_Object = MibTableColumn
slaMacPingState = _SlaMacPingState_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 12, 100, 1, 2),
    _SlaMacPingState_Type()
)
slaMacPingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaMacPingState.setStatus("current")


class _SlaMacPingName_Type(DisplayString):
    """Custom type slaMacPingName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 49),
    )


_SlaMacPingName_Type.__name__ = "DisplayString"
_SlaMacPingName_Object = MibTableColumn
slaMacPingName = _SlaMacPingName_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 12, 100, 1, 3),
    _SlaMacPingName_Type()
)
slaMacPingName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaMacPingName.setStatus("current")


class _SlaMacPingCfmMdId_Type(DisplayString):
    """Custom type slaMacPingCfmMdId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 43),
    )


_SlaMacPingCfmMdId_Type.__name__ = "DisplayString"
_SlaMacPingCfmMdId_Object = MibTableColumn
slaMacPingCfmMdId = _SlaMacPingCfmMdId_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 12, 100, 1, 4),
    _SlaMacPingCfmMdId_Type()
)
slaMacPingCfmMdId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaMacPingCfmMdId.setStatus("current")


class _SlaMacPingCfmMaId_Type(DisplayString):
    """Custom type slaMacPingCfmMaId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 45),
    )


_SlaMacPingCfmMaId_Type.__name__ = "DisplayString"
_SlaMacPingCfmMaId_Object = MibTableColumn
slaMacPingCfmMaId = _SlaMacPingCfmMaId_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 12, 100, 1, 5),
    _SlaMacPingCfmMaId_Type()
)
slaMacPingCfmMaId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaMacPingCfmMaId.setStatus("current")


class _SlaMacPingCfmSrcMepId_Type(Unsigned32):
    """Custom type slaMacPingCfmSrcMepId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_SlaMacPingCfmSrcMepId_Type.__name__ = "Unsigned32"
_SlaMacPingCfmSrcMepId_Object = MibTableColumn
slaMacPingCfmSrcMepId = _SlaMacPingCfmSrcMepId_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 12, 100, 1, 6),
    _SlaMacPingCfmSrcMepId_Type()
)
slaMacPingCfmSrcMepId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaMacPingCfmSrcMepId.setStatus("current")


class _SlaMacPingDesMepId_Type(Unsigned32):
    """Custom type slaMacPingDesMepId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_SlaMacPingDesMepId_Type.__name__ = "Unsigned32"
_SlaMacPingDesMepId_Object = MibTableColumn
slaMacPingDesMepId = _SlaMacPingDesMepId_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 12, 100, 1, 7),
    _SlaMacPingDesMepId_Type()
)
slaMacPingDesMepId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaMacPingDesMepId.setStatus("current")
_SlaMacPingCyclsec_Type = Unsigned32
_SlaMacPingCyclsec_Object = MibTableColumn
slaMacPingCyclsec = _SlaMacPingCyclsec_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 12, 100, 1, 8),
    _SlaMacPingCyclsec_Type()
)
slaMacPingCyclsec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaMacPingCyclsec.setStatus("current")


class _SlaMacPingPktNumPerCycl_Type(Unsigned32):
    """Custom type slaMacPingPktNumPerCycl based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_SlaMacPingPktNumPerCycl_Type.__name__ = "Unsigned32"
_SlaMacPingPktNumPerCycl_Object = MibTableColumn
slaMacPingPktNumPerCycl = _SlaMacPingPktNumPerCycl_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 12, 100, 1, 9),
    _SlaMacPingPktNumPerCycl_Type()
)
slaMacPingPktNumPerCycl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaMacPingPktNumPerCycl.setStatus("current")


class _SlaMacPingAvgCyclNum_Type(Unsigned32):
    """Custom type slaMacPingAvgCyclNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_SlaMacPingAvgCyclNum_Type.__name__ = "Unsigned32"
_SlaMacPingAvgCyclNum_Object = MibTableColumn
slaMacPingAvgCyclNum = _SlaMacPingAvgCyclNum_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 12, 100, 1, 10),
    _SlaMacPingAvgCyclNum_Type()
)
slaMacPingAvgCyclNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaMacPingAvgCyclNum.setStatus("current")


class _SlaMacPingLastCycleTime_Type(DisplayString):
    """Custom type slaMacPingLastCycleTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_SlaMacPingLastCycleTime_Type.__name__ = "DisplayString"
_SlaMacPingLastCycleTime_Object = MibTableColumn
slaMacPingLastCycleTime = _SlaMacPingLastCycleTime_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 12, 100, 1, 11),
    _SlaMacPingLastCycleTime_Type()
)
slaMacPingLastCycleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaMacPingLastCycleTime.setStatus("current")
_SlaMacPingAvgValueTimes_Type = Unsigned32
_SlaMacPingAvgValueTimes_Object = MibTableColumn
slaMacPingAvgValueTimes = _SlaMacPingAvgValueTimes_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 12, 100, 1, 12),
    _SlaMacPingAvgValueTimes_Type()
)
slaMacPingAvgValueTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaMacPingAvgValueTimes.setStatus("current")
_SlaMacPingRowStatus_Type = RowStatus
_SlaMacPingRowStatus_Object = MibTableColumn
slaMacPingRowStatus = _SlaMacPingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 12, 100, 1, 13),
    _SlaMacPingRowStatus_Type()
)
slaMacPingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slaMacPingRowStatus.setStatus("current")


class _SlaMacPingSchedInterval_Type(Unsigned32):
    """Custom type slaMacPingSchedInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 4294967295),
    )


_SlaMacPingSchedInterval_Type.__name__ = "Unsigned32"
_SlaMacPingSchedInterval_Object = MibTableColumn
slaMacPingSchedInterval = _SlaMacPingSchedInterval_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 12, 100, 1, 14),
    _SlaMacPingSchedInterval_Type()
)
slaMacPingSchedInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaMacPingSchedInterval.setStatus("current")


class _SlaMacPingHistoryMaxCount_Type(Integer32):
    """Custom type slaMacPingHistoryMaxCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SlaMacPingHistoryMaxCount_Type.__name__ = "Integer32"
_SlaMacPingHistoryMaxCount_Object = MibTableColumn
slaMacPingHistoryMaxCount = _SlaMacPingHistoryMaxCount_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 12, 100, 1, 15),
    _SlaMacPingHistoryMaxCount_Type()
)
slaMacPingHistoryMaxCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaMacPingHistoryMaxCount.setStatus("current")
_SlaMacPingDesMac_Type = PhysAddress
_SlaMacPingDesMac_Object = MibTableColumn
slaMacPingDesMac = _SlaMacPingDesMac_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 12, 100, 1, 16),
    _SlaMacPingDesMac_Type()
)
slaMacPingDesMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaMacPingDesMac.setStatus("current")


class _SlaMacPingRemDevName_Type(DisplayString):
    """Custom type slaMacPingRemDevName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_SlaMacPingRemDevName_Type.__name__ = "DisplayString"
_SlaMacPingRemDevName_Object = MibTableColumn
slaMacPingRemDevName = _SlaMacPingRemDevName_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 12, 100, 1, 17),
    _SlaMacPingRemDevName_Type()
)
slaMacPingRemDevName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaMacPingRemDevName.setStatus("current")
_SysSlaNmsMgt_ObjectIdentity = ObjectIdentity
sysSlaNmsMgt = _SysSlaNmsMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 13)
)
_SysSlaNmsTable_Object = MibTable
sysSlaNmsTable = _SysSlaNmsTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 13, 100)
)
if mibBuilder.loadTexts:
    sysSlaNmsTable.setStatus("current")
_SysSlaNmsEntry_Object = MibTableRow
sysSlaNmsEntry = _SysSlaNmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 13, 100, 1)
)
sysSlaNmsEntry.setIndexNames(
    (0, "MPSLA", "rtrEntityId"),
)
if mibBuilder.loadTexts:
    sysSlaNmsEntry.setStatus("current")


class _SlaNmsEntityId_Type(Integer32):
    """Custom type slaNmsEntityId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000),
    )


_SlaNmsEntityId_Type.__name__ = "Integer32"
_SlaNmsEntityId_Object = MibTableColumn
slaNmsEntityId = _SlaNmsEntityId_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 13, 100, 1, 1),
    _SlaNmsEntityId_Type()
)
slaNmsEntityId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaNmsEntityId.setStatus("current")


class _SlaNmsScheduleId_Type(Integer32):
    """Custom type slaNmsScheduleId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000),
    )


_SlaNmsScheduleId_Type.__name__ = "Integer32"
_SlaNmsScheduleId_Object = MibTableColumn
slaNmsScheduleId = _SlaNmsScheduleId_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 13, 100, 1, 2),
    _SlaNmsScheduleId_Type()
)
slaNmsScheduleId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaNmsScheduleId.setStatus("current")
_SlaNmsId_Type = Unsigned32
_SlaNmsId_Object = MibTableColumn
slaNmsId = _SlaNmsId_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 13, 100, 1, 3),
    _SlaNmsId_Type()
)
slaNmsId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaNmsId.setStatus("current")
_SlaNmsRowStatus_Type = RowStatus
_SlaNmsRowStatus_Object = MibTableColumn
slaNmsRowStatus = _SlaNmsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 201, 13, 100, 1, 4),
    _SlaNmsRowStatus_Type()
)
slaNmsRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaNmsRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects

mpSlaTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5651, 2, 2, 62, 1)
)
mpSlaTrap.setObjects(
      *(("MPSLA", "slaThresholdTableEntityId"),
        ("MPSLA", "slaThresholdString"),
        ("MPSLA", "slaThresholdValue"),
        ("MPSLA", "slaThresholdDirection"))
)
if mibBuilder.loadTexts:
    mpSlaTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MPSLA",
    **{"EnabledStatus": EnabledStatus,
       "mpTrap": mpTrap,
       "mpTrapClass": mpTrapClass,
       "mpTrapDescr": mpTrapDescr,
       "mpTrapType": mpTrapType,
       "mpTraps": mpTraps,
       "mpSla": mpSla,
       "mpSlaTrap": mpSlaTrap,
       "mpios": mpios,
       "iosSystem": iosSystem,
       "iosObjects": iosObjects,
       "sysSLA": sysSLA,
       "sysSlaGbl": sysSlaGbl,
       "sysSlaCtrl": sysSlaCtrl,
       "sysSlaResponder": sysSlaResponder,
       "sysSlaNotUsedEntityId": sysSlaNotUsedEntityId,
       "sysSlaNotUsedScheId": sysSlaNotUsedScheId,
       "sysSlaEntityMgt": sysSlaEntityMgt,
       "sysSlaEntityTable": sysSlaEntityTable,
       "sysSlaEntityEntry": sysSlaEntityEntry,
       "slaEntityId": slaEntityId,
       "slaEntityName": slaEntityName,
       "slaEntityType": slaEntityType,
       "slaEntityRowStatus": slaEntityRowStatus,
       "sysSlaGroupMgt": sysSlaGroupMgt,
       "sysSlaGroupTable": sysSlaGroupTable,
       "sysSlaGroupEntry": sysSlaGroupEntry,
       "slaGroupId": slaGroupId,
       "slaGroupName": slaGroupName,
       "slaGroupInterval": slaGroupInterval,
       "slaGroupEntityMembers": slaGroupEntityMembers,
       "slaGroupRowStatus": slaGroupRowStatus,
       "sysSlaScheduleMgt": sysSlaScheduleMgt,
       "sysSlaScheduleTable": sysSlaScheduleTable,
       "sysSlaScheduleEntry": sysSlaScheduleEntry,
       "slaScheduleId": slaScheduleId,
       "slaScheduleType": slaScheduleType,
       "slaScheduleObjId": slaScheduleObjId,
       "slaScheduleStartTimeFlag": slaScheduleStartTimeFlag,
       "slaScheduleAfterTime": slaScheduleAfterTime,
       "slaScheduleStartTime": slaScheduleStartTime,
       "slaScheduleAgeOut": slaScheduleAgeOut,
       "slaScheduleLifeFlag": slaScheduleLifeFlag,
       "slaScheduleLifeTime": slaScheduleLifeTime,
       "slaScheduleRepeat": slaScheduleRepeat,
       "slaScheduleInterval": slaScheduleInterval,
       "slaScheduleRowStatus": slaScheduleRowStatus,
       "sysSlaIcmpEchoMgt": sysSlaIcmpEchoMgt,
       "sysSlaIcmpEchoTable": sysSlaIcmpEchoTable,
       "sysSlaIcmpEchoEntry": sysSlaIcmpEchoEntry,
       "slaIcmpEchoTableEntityId": slaIcmpEchoTableEntityId,
       "slaIcmpEchoTargetIp": slaIcmpEchoTargetIp,
       "slaIcmpEchoPktNum": slaIcmpEchoPktNum,
       "slaIcmpEchoPktLen": slaIcmpEchoPktLen,
       "slaIcmpEchoTimeout": slaIcmpEchoTimeout,
       "slaIcmpEchoSchInterval": slaIcmpEchoSchInterval,
       "slaIcmpEchoExtendFlag": slaIcmpEchoExtendFlag,
       "slaIcmpEchoVrfName": slaIcmpEchoVrfName,
       "slaIcmpEchoSourceIp": slaIcmpEchoSourceIp,
       "slaIcmpEchoTos": slaIcmpEchoTos,
       "slaIcmpEchoSetDf": slaIcmpEchoSetDf,
       "slaIcmpEchoVerifyData": slaIcmpEchoVerifyData,
       "slaIcmpEchoHistorySize": slaIcmpEchoHistorySize,
       "slaIcmpEchoPeriods": slaIcmpEchoPeriods,
       "slaIcmpEchoAlarmType": slaIcmpEchoAlarmType,
       "slaIcmpEchoIsScheduling": slaIcmpEchoIsScheduling,
       "slaIcmpEchoRowStatus": slaIcmpEchoRowStatus,
       "sysSlaIcmpEchoHistoryTable": sysSlaIcmpEchoHistoryTable,
       "sysSlaIcmpEchoHistoryEntry": sysSlaIcmpEchoHistoryEntry,
       "slaIcmpEchoHisTableEntityId": slaIcmpEchoHisTableEntityId,
       "slaIcmpEchoHistoryIndex": slaIcmpEchoHistoryIndex,
       "slaIcmpEchoRtt": slaIcmpEchoRtt,
       "slaIcmpEchoPktLoss": slaIcmpEchoPktLoss,
       "slaIcmpEchoTime": slaIcmpEchoTime,
       "slaIcmpEchoTableRowStatus": slaIcmpEchoTableRowStatus,
       "sysSlaJitterMgt": sysSlaJitterMgt,
       "sysSlaJitterTable": sysSlaJitterTable,
       "sysSlaJitterEntry": sysSlaJitterEntry,
       "slaJitterTableEntityId": slaJitterTableEntityId,
       "slaJitterState": slaJitterState,
       "slaJitterTargetIp": slaJitterTargetIp,
       "slaJitterTargetPort": slaJitterTargetPort,
       "slaJitterCodec": slaJitterCodec,
       "slaJitterPktLen": slaJitterPktLen,
       "slaJitterPktNum": slaJitterPktNum,
       "slaJitterPktInterval": slaJitterPktInterval,
       "slaJitterSchInterval": slaJitterSchInterval,
       "slaJitterSourceIp": slaJitterSourceIp,
       "slaJitterSourcePort": slaJitterSourcePort,
       "slaJitterTimeout": slaJitterTimeout,
       "slaJitterVrfName": slaJitterVrfName,
       "slaJitterTos": slaJitterTos,
       "slaJitterHistorySize": slaJitterHistorySize,
       "slaJitterPeriods": slaJitterPeriods,
       "slaJitterAlarmType": slaJitterAlarmType,
       "slaJitterTableRowStatus": slaJitterTableRowStatus,
       "sysSlaJitterHistoryTable": sysSlaJitterHistoryTable,
       "sysSlaJitterHistoryEntry": sysSlaJitterHistoryEntry,
       "slaJitterHisTableEntityId": slaJitterHisTableEntityId,
       "slaJitterHistoryIndex": slaJitterHistoryIndex,
       "slaJitterRtt": slaJitterRtt,
       "slaJitterPktLossSd": slaJitterPktLossSd,
       "slaJitterPktLossDs": slaJitterPktLossDs,
       "slaJitterSd": slaJitterSd,
       "slaJitterDs": slaJitterDs,
       "slaJitterDelaySd": slaJitterDelaySd,
       "slaJitterDelayDs": slaJitterDelayDs,
       "slaJitterIcpif": slaJitterIcpif,
       "slaJitterMos": slaJitterMos,
       "slaJitterTime": slaJitterTime,
       "slaJitterHisTableRowStatus": slaJitterHisTableRowStatus,
       "sysSlaUdpEchoMgt": sysSlaUdpEchoMgt,
       "sysSlaUdpEchoTable": sysSlaUdpEchoTable,
       "sysSlaUdpEchoEntry": sysSlaUdpEchoEntry,
       "slaUdpEchoTableEntityId": slaUdpEchoTableEntityId,
       "slaUdpEchoState": slaUdpEchoState,
       "slaUdpEchoTargetIp": slaUdpEchoTargetIp,
       "slaUdpEchoTargetPort": slaUdpEchoTargetPort,
       "slaUdpEchoPktLen": slaUdpEchoPktLen,
       "slaUdpEchoSchInterval": slaUdpEchoSchInterval,
       "slaUdpEchoSourceIp": slaUdpEchoSourceIp,
       "slaUdpEchoSourcePort": slaUdpEchoSourcePort,
       "slaUdpEchoTimeout": slaUdpEchoTimeout,
       "slaUdpEchoVrfName": slaUdpEchoVrfName,
       "slaUdpEchoTos": slaUdpEchoTos,
       "slaUdpEchoHistorySize": slaUdpEchoHistorySize,
       "slaUdpEchoPeriods": slaUdpEchoPeriods,
       "slaUdpEchoAlarmType": slaUdpEchoAlarmType,
       "slaUdpEchoTableRowStatus": slaUdpEchoTableRowStatus,
       "sysSlaUdpEchoHistoryTable": sysSlaUdpEchoHistoryTable,
       "sysSlaUdpEchoHistoryEntry": sysSlaUdpEchoHistoryEntry,
       "slaUdpEchoHisTableEntityId": slaUdpEchoHisTableEntityId,
       "slaUdpEchoHistoryIndex": slaUdpEchoHistoryIndex,
       "slaUdpEchoPktLoss": slaUdpEchoPktLoss,
       "slaUdpEchoRtt": slaUdpEchoRtt,
       "slaUdpEchoTime": slaUdpEchoTime,
       "slaUdpEchoHisTableRowStatus": slaUdpEchoHisTableRowStatus,
       "sysSlaFlStaMgt": sysSlaFlStaMgt,
       "sysSlaFlStaTable": sysSlaFlStaTable,
       "sysSlaFlStaEntry": sysSlaFlStaEntry,
       "slaFlStaTableEntityId": slaFlStaTableEntityId,
       "slaFlStaIfName": slaFlStaIfName,
       "slaFlStaInterval": slaFlStaInterval,
       "slaFlStaHistorySize": slaFlStaHistorySize,
       "slaFlStaPeriods": slaFlStaPeriods,
       "slaFlStaAlarmType": slaFlStaAlarmType,
       "slaFlStaTableRowStatus": slaFlStaTableRowStatus,
       "sysSlaFlStaHistoryTable": sysSlaFlStaHistoryTable,
       "sysSlaFlStaHistoryEntry": sysSlaFlStaHistoryEntry,
       "slaFlStaHisTableEntityId": slaFlStaHisTableEntityId,
       "slaFlStaHistoryIndex": slaFlStaHistoryIndex,
       "slaFlStaInputPkts": slaFlStaInputPkts,
       "slaFlStaInputFlow": slaFlStaInputFlow,
       "slaFlStaOutputPkts": slaFlStaOutputPkts,
       "slaFlStaOutputFlow": slaFlStaOutputFlow,
       "slaFlStaTime": slaFlStaTime,
       "slaFlStaHisTableRowStatus": slaFlStaHisTableRowStatus,
       "sysSlaIcmpPathJitMgt": sysSlaIcmpPathJitMgt,
       "sysSlaIcmpPathJitTable": sysSlaIcmpPathJitTable,
       "sysSlaIcmpPathJitEntry": sysSlaIcmpPathJitEntry,
       "slaIcmpPJTableEntityId": slaIcmpPJTableEntityId,
       "slaIcmpPJTargetIp": slaIcmpPJTargetIp,
       "slaIcmpPJPktNum": slaIcmpPJPktNum,
       "slaIcmpPJPktLen": slaIcmpPJPktLen,
       "slaIcmpPJTimeout": slaIcmpPJTimeout,
       "slaIcmpPJPktInterval": slaIcmpPJPktInterval,
       "slaIcmpPJSchInterval": slaIcmpPJSchInterval,
       "slaIcmpPJVrfName": slaIcmpPJVrfName,
       "slaIcmpPJSourceIp": slaIcmpPJSourceIp,
       "slaIcmpPJTos": slaIcmpPJTos,
       "slaIcmpPJVerifyData": slaIcmpPJVerifyData,
       "slaIcmpPJAlarmType": slaIcmpPJAlarmType,
       "slaIcmpPJTargetOnly": slaIcmpPJTargetOnly,
       "slaIcmpPJHistorySize": slaIcmpPJHistorySize,
       "slaIcmpPJPeriods": slaIcmpPJPeriods,
       "slaIcmpPJLsrPath": slaIcmpPJLsrPath,
       "slaIcmpPJIsScheduling": slaIcmpPJIsScheduling,
       "slaIcmpPJTableRowStatus": slaIcmpPJTableRowStatus,
       "sysSlaIcmpPathJitHistoryTable": sysSlaIcmpPathJitHistoryTable,
       "sysSlaIcmpPathJitHistoryEntry": sysSlaIcmpPathJitHistoryEntry,
       "slaIcmpPJHisTableEntityId": slaIcmpPJHisTableEntityId,
       "slaIcmpPJHopIndex": slaIcmpPJHopIndex,
       "slaIcmpPJHistoryIndex": slaIcmpPJHistoryIndex,
       "slaIcmpPJRtt": slaIcmpPJRtt,
       "slaIcmpPJJitter": slaIcmpPJJitter,
       "slaIcmpPJPktLoss": slaIcmpPJPktLoss,
       "slaIcmpPJTime": slaIcmpPJTime,
       "slaIcmpPJGetStatus": slaIcmpPJGetStatus,
       "slaIcmpPJHisTableRowStatus": slaIcmpPJHisTableRowStatus,
       "sysSlaIcmpPathEchoMgt": sysSlaIcmpPathEchoMgt,
       "sysSlaIcmpPathEchoTable": sysSlaIcmpPathEchoTable,
       "sysSlaIcmpPathEchoEntry": sysSlaIcmpPathEchoEntry,
       "slaIcmpPETableEntityId": slaIcmpPETableEntityId,
       "slaIcmpPETargetIp": slaIcmpPETargetIp,
       "slaIcmpPEPktLen": slaIcmpPEPktLen,
       "slaIcmpPETimeout": slaIcmpPETimeout,
       "slaIcmpPESchInterval": slaIcmpPESchInterval,
       "slaIcmpPEVrfName": slaIcmpPEVrfName,
       "slaIcmpPESourceIp": slaIcmpPESourceIp,
       "slaIcmpPETos": slaIcmpPETos,
       "slaIcmpPEVerifyData": slaIcmpPEVerifyData,
       "slaIcmpPELsrPath": slaIcmpPELsrPath,
       "slaIcmpPEHistorySize": slaIcmpPEHistorySize,
       "slaIcmpPEPeriods": slaIcmpPEPeriods,
       "slaIcmpPEAlarmType": slaIcmpPEAlarmType,
       "slaIcmpPETargetOnly": slaIcmpPETargetOnly,
       "slaIcmpPEIsScheduling": slaIcmpPEIsScheduling,
       "slaIcmpPETableRowStatus": slaIcmpPETableRowStatus,
       "sysSlaIcmpPathEchoHistoryTable": sysSlaIcmpPathEchoHistoryTable,
       "sysSlaIcmpPathEchoHistoryEntry": sysSlaIcmpPathEchoHistoryEntry,
       "slaIcmpPEHisTableEntityId": slaIcmpPEHisTableEntityId,
       "slaIcmpPEHopIndex": slaIcmpPEHopIndex,
       "slaIcmpPEHistoryIndex": slaIcmpPEHistoryIndex,
       "slaIcmpPERtt": slaIcmpPERtt,
       "slaIcmpPEPktLoss": slaIcmpPEPktLoss,
       "slaIcmpPETime": slaIcmpPETime,
       "slaIcmpPEGetStatus": slaIcmpPEGetStatus,
       "slaIcmpPEHisTableRowStatus": slaIcmpPEHisTableRowStatus,
       "sysSlaThresholdMgt": sysSlaThresholdMgt,
       "sysSlaThresholdTable": sysSlaThresholdTable,
       "sysSlaThresholdEntry": sysSlaThresholdEntry,
       "slaThresholdTableEntityId": slaThresholdTableEntityId,
       "slaThresholdString": slaThresholdString,
       "slaThresholdValue": slaThresholdValue,
       "slaThresholdDirection": slaThresholdDirection,
       "slaThresholdIndex": slaThresholdIndex,
       "slaThresholdRowStatus": slaThresholdRowStatus,
       "sysSlaMacPingMgt": sysSlaMacPingMgt,
       "mpMacPingTraps": mpMacPingTraps,
       "sysSlaMacPingTable": sysSlaMacPingTable,
       "sysSlaMacPingEntry": sysSlaMacPingEntry,
       "slaMacPingEntityId": slaMacPingEntityId,
       "slaMacPingState": slaMacPingState,
       "slaMacPingName": slaMacPingName,
       "slaMacPingCfmMdId": slaMacPingCfmMdId,
       "slaMacPingCfmMaId": slaMacPingCfmMaId,
       "slaMacPingCfmSrcMepId": slaMacPingCfmSrcMepId,
       "slaMacPingDesMepId": slaMacPingDesMepId,
       "slaMacPingCyclsec": slaMacPingCyclsec,
       "slaMacPingPktNumPerCycl": slaMacPingPktNumPerCycl,
       "slaMacPingAvgCyclNum": slaMacPingAvgCyclNum,
       "slaMacPingLastCycleTime": slaMacPingLastCycleTime,
       "slaMacPingAvgValueTimes": slaMacPingAvgValueTimes,
       "slaMacPingRowStatus": slaMacPingRowStatus,
       "slaMacPingSchedInterval": slaMacPingSchedInterval,
       "slaMacPingHistoryMaxCount": slaMacPingHistoryMaxCount,
       "slaMacPingDesMac": slaMacPingDesMac,
       "slaMacPingRemDevName": slaMacPingRemDevName,
       "sysSlaNmsMgt": sysSlaNmsMgt,
       "sysSlaNmsTable": sysSlaNmsTable,
       "sysSlaNmsEntry": sysSlaNmsEntry,
       "slaNmsEntityId": slaNmsEntityId,
       "slaNmsScheduleId": slaNmsScheduleId,
       "slaNmsId": slaNmsId,
       "slaNmsRowStatus": slaNmsRowStatus}
)
