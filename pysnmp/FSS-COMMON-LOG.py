# SNMP MIB module (FSS-COMMON-LOG) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/FSS-COMMON-LOG
# Produced by pysmi-1.5.4 at Mon Oct 14 21:46:39 2024
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

(fssCommon,) = mibBuilder.importSymbols(
    "FSS-COMMON-SMI",
    "fssCommon")

(FCCondEffect,
 FCCondType,
 FCDirection,
 FCLocation,
 FCObjectName,
 FCServEffect,
 FCSeverity,
 FCStdObjectIndex,
 FCStdTypeIndex,
 FCTcCondType,
 FCTcaCondType,
 FCTimePeriod,
 FCTrapHistIndex,
 FCTrapType) = mibBuilder.importSymbols(
    "FSS-COMMON-TC",
    "FCCondEffect",
    "FCCondType",
    "FCDirection",
    "FCLocation",
    "FCObjectName",
    "FCServEffect",
    "FCSeverity",
    "FCStdObjectIndex",
    "FCStdTypeIndex",
    "FCTcCondType",
    "FCTcaCondType",
    "FCTimePeriod",
    "FCTrapHistIndex",
    "FCTrapType")

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

(DateAndTime,
 DisplayString,
 RowPointer,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowPointer",
    "TextualConvention")


# MODULE-IDENTITY

fssLog = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 1000)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FssAlarm_ObjectIdentity = ObjectIdentity
fssAlarm = _FssAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 200)
)
_FssAlarmCurrent_ObjectIdentity = ObjectIdentity
fssAlarmCurrent = _FssAlarmCurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 200, 1)
)
_FssStandingAlarmXTable_Object = MibTable
fssStandingAlarmXTable = _FssStandingAlarmXTable_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 200, 1, 1)
)
if mibBuilder.loadTexts:
    fssStandingAlarmXTable.setStatus("current")
_FssStandingAlarmXEntry_Object = MibTableRow
fssStandingAlarmXEntry = _FssStandingAlarmXEntry_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 200, 1, 1, 1)
)
fssStandingAlarmXEntry.setIndexNames(
    (0, "FSS-COMMON-LOG", "fssStdAlarmObjectIndex"),
    (0, "FSS-COMMON-LOG", "fssStdAlarmTypeIndex"),
)
if mibBuilder.loadTexts:
    fssStandingAlarmXEntry.setStatus("current")
_FssStdAlarmObjectIndex_Type = FCStdObjectIndex
_FssStdAlarmObjectIndex_Object = MibTableColumn
fssStdAlarmObjectIndex = _FssStdAlarmObjectIndex_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 200, 1, 1, 1, 1),
    _FssStdAlarmObjectIndex_Type()
)
fssStdAlarmObjectIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fssStdAlarmObjectIndex.setStatus("current")
_FssStdAlarmTypeIndex_Type = FCStdTypeIndex
_FssStdAlarmTypeIndex_Object = MibTableColumn
fssStdAlarmTypeIndex = _FssStdAlarmTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 200, 1, 1, 1, 2),
    _FssStdAlarmTypeIndex_Type()
)
fssStdAlarmTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fssStdAlarmTypeIndex.setStatus("current")
_FssStdAlarmObjectName_Type = FCObjectName
_FssStdAlarmObjectName_Object = MibTableColumn
fssStdAlarmObjectName = _FssStdAlarmObjectName_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 200, 1, 1, 1, 3),
    _FssStdAlarmObjectName_Type()
)
fssStdAlarmObjectName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fssStdAlarmObjectName.setStatus("current")
_FssStdAlarmType_Type = FCCondType
_FssStdAlarmType_Object = MibTableColumn
fssStdAlarmType = _FssStdAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 200, 1, 1, 1, 4),
    _FssStdAlarmType_Type()
)
fssStdAlarmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fssStdAlarmType.setStatus("current")
_FssStdAlarmSeverity_Type = FCSeverity
_FssStdAlarmSeverity_Object = MibTableColumn
fssStdAlarmSeverity = _FssStdAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 200, 1, 1, 1, 5),
    _FssStdAlarmSeverity_Type()
)
fssStdAlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fssStdAlarmSeverity.setStatus("current")
_FssStdAlarmServEffect_Type = FCServEffect
_FssStdAlarmServEffect_Object = MibTableColumn
fssStdAlarmServEffect = _FssStdAlarmServEffect_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 200, 1, 1, 1, 6),
    _FssStdAlarmServEffect_Type()
)
fssStdAlarmServEffect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fssStdAlarmServEffect.setStatus("current")
_FssStdAlarmLocn_Type = FCLocation
_FssStdAlarmLocn_Object = MibTableColumn
fssStdAlarmLocn = _FssStdAlarmLocn_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 200, 1, 1, 1, 7),
    _FssStdAlarmLocn_Type()
)
fssStdAlarmLocn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fssStdAlarmLocn.setStatus("current")
_FssStdAlarmDir_Type = FCDirection
_FssStdAlarmDir_Object = MibTableColumn
fssStdAlarmDir = _FssStdAlarmDir_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 200, 1, 1, 1, 8),
    _FssStdAlarmDir_Type()
)
fssStdAlarmDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fssStdAlarmDir.setStatus("current")
_FssAlarmType_Type = FCCondType
_FssAlarmType_Object = MibScalar
fssAlarmType = _FssAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 200, 3),
    _FssAlarmType_Type()
)
fssAlarmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fssAlarmType.setStatus("current")
_FssAlarmCondEffect_Type = FCCondEffect
_FssAlarmCondEffect_Object = MibScalar
fssAlarmCondEffect = _FssAlarmCondEffect_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 200, 4),
    _FssAlarmCondEffect_Type()
)
fssAlarmCondEffect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fssAlarmCondEffect.setStatus("current")


class _FssAlarmTypeQual_Type(DisplayString):
    """Custom type fssAlarmTypeQual based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_FssAlarmTypeQual_Type.__name__ = "DisplayString"
_FssAlarmTypeQual_Object = MibScalar
fssAlarmTypeQual = _FssAlarmTypeQual_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 200, 5),
    _FssAlarmTypeQual_Type()
)
fssAlarmTypeQual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fssAlarmTypeQual.setStatus("current")
_FssAlarmLocn_Type = FCLocation
_FssAlarmLocn_Object = MibScalar
fssAlarmLocn = _FssAlarmLocn_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 200, 6),
    _FssAlarmLocn_Type()
)
fssAlarmLocn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fssAlarmLocn.setStatus("current")
_FssAlarmDir_Type = FCDirection
_FssAlarmDir_Object = MibScalar
fssAlarmDir = _FssAlarmDir_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 200, 7),
    _FssAlarmDir_Type()
)
fssAlarmDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fssAlarmDir.setStatus("current")
_FssAlarmSeverity_Type = FCSeverity
_FssAlarmSeverity_Object = MibScalar
fssAlarmSeverity = _FssAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 200, 8),
    _FssAlarmSeverity_Type()
)
fssAlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fssAlarmSeverity.setStatus("current")
_FssAlarmServiceEffect_Type = FCServEffect
_FssAlarmServiceEffect_Object = MibScalar
fssAlarmServiceEffect = _FssAlarmServiceEffect_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 200, 9),
    _FssAlarmServiceEffect_Type()
)
fssAlarmServiceEffect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fssAlarmServiceEffect.setStatus("current")
_FssAlarmTraps_ObjectIdentity = ObjectIdentity
fssAlarmTraps = _FssAlarmTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 200, 100)
)
_FssAlarmPrefix_ObjectIdentity = ObjectIdentity
fssAlarmPrefix = _FssAlarmPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 200, 100, 0)
)


class _FssCondQual_Type(Unsigned32):
    """Custom type fssCondQual based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FssCondQual_Type.__name__ = "Unsigned32"
_FssCondQual_Object = MibScalar
fssCondQual = _FssCondQual_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 200, 100, 100),
    _FssCondQual_Type()
)
fssCondQual.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fssCondQual.setStatus("current")
_FssTca_ObjectIdentity = ObjectIdentity
fssTca = _FssTca_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 300)
)
_FssTcaType_Type = FCTcaCondType
_FssTcaType_Object = MibScalar
fssTcaType = _FssTcaType_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 300, 1),
    _FssTcaType_Type()
)
fssTcaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fssTcaType.setStatus("current")


class _FssTcaTypeQual_Type(DisplayString):
    """Custom type fssTcaTypeQual based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_FssTcaTypeQual_Type.__name__ = "DisplayString"
_FssTcaTypeQual_Object = MibScalar
fssTcaTypeQual = _FssTcaTypeQual_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 300, 2),
    _FssTcaTypeQual_Type()
)
fssTcaTypeQual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fssTcaTypeQual.setStatus("current")
_FssTcaCondEffect_Type = FCCondEffect
_FssTcaCondEffect_Object = MibScalar
fssTcaCondEffect = _FssTcaCondEffect_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 300, 3),
    _FssTcaCondEffect_Type()
)
fssTcaCondEffect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fssTcaCondEffect.setStatus("current")
_FssTcaLocn_Type = FCLocation
_FssTcaLocn_Object = MibScalar
fssTcaLocn = _FssTcaLocn_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 300, 4),
    _FssTcaLocn_Type()
)
fssTcaLocn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fssTcaLocn.setStatus("current")
_FssTcaDir_Type = FCDirection
_FssTcaDir_Object = MibScalar
fssTcaDir = _FssTcaDir_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 300, 5),
    _FssTcaDir_Type()
)
fssTcaDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fssTcaDir.setStatus("current")


class _FssTcaMonVal_Type(DisplayString):
    """Custom type fssTcaMonVal based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_FssTcaMonVal_Type.__name__ = "DisplayString"
_FssTcaMonVal_Object = MibScalar
fssTcaMonVal = _FssTcaMonVal_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 300, 6),
    _FssTcaMonVal_Type()
)
fssTcaMonVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fssTcaMonVal.setStatus("current")


class _FssTcaThLev_Type(DisplayString):
    """Custom type fssTcaThLev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_FssTcaThLev_Type.__name__ = "DisplayString"
_FssTcaThLev_Object = MibScalar
fssTcaThLev = _FssTcaThLev_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 300, 7),
    _FssTcaThLev_Type()
)
fssTcaThLev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fssTcaThLev.setStatus("current")
_FssTcaTimePeriod_Type = FCTimePeriod
_FssTcaTimePeriod_Object = MibScalar
fssTcaTimePeriod = _FssTcaTimePeriod_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 300, 8),
    _FssTcaTimePeriod_Type()
)
fssTcaTimePeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fssTcaTimePeriod.setStatus("current")
_FssTcaTraps_ObjectIdentity = ObjectIdentity
fssTcaTraps = _FssTcaTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 300, 100)
)
_FssTcaPrefix_ObjectIdentity = ObjectIdentity
fssTcaPrefix = _FssTcaPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 300, 100, 0)
)


class _FssTcaCondQual_Type(Unsigned32):
    """Custom type fssTcaCondQual based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FssTcaCondQual_Type.__name__ = "Unsigned32"
_FssTcaCondQual_Object = MibScalar
fssTcaCondQual = _FssTcaCondQual_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 300, 100, 100),
    _FssTcaCondQual_Type()
)
fssTcaCondQual.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fssTcaCondQual.setStatus("current")
_FssTc_ObjectIdentity = ObjectIdentity
fssTc = _FssTc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 400)
)
_FssTcType_Type = FCTcCondType
_FssTcType_Object = MibScalar
fssTcType = _FssTcType_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 400, 1),
    _FssTcType_Type()
)
fssTcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fssTcType.setStatus("current")


class _FssTcTypeQual_Type(DisplayString):
    """Custom type fssTcTypeQual based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_FssTcTypeQual_Type.__name__ = "DisplayString"
_FssTcTypeQual_Object = MibScalar
fssTcTypeQual = _FssTcTypeQual_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 400, 2),
    _FssTcTypeQual_Type()
)
fssTcTypeQual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fssTcTypeQual.setStatus("current")
_FssTcTraps_ObjectIdentity = ObjectIdentity
fssTcTraps = _FssTcTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 400, 100)
)
_FssTcPrefix_ObjectIdentity = ObjectIdentity
fssTcPrefix = _FssTcPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 400, 100, 0)
)


class _FssTcCondQual_Type(Unsigned32):
    """Custom type fssTcCondQual based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FssTcCondQual_Type.__name__ = "Unsigned32"
_FssTcCondQual_Object = MibScalar
fssTcCondQual = _FssTcCondQual_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 400, 100, 100),
    _FssTcCondQual_Type()
)
fssTcCondQual.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fssTcCondQual.setStatus("current")
_FssBase_ObjectIdentity = ObjectIdentity
fssBase = _FssBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 500)
)
_FssTrapObjectName_Type = FCObjectName
_FssTrapObjectName_Object = MibScalar
fssTrapObjectName = _FssTrapObjectName_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 500, 1),
    _FssTrapObjectName_Type()
)
fssTrapObjectName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fssTrapObjectName.setStatus("current")


class _FssTrapDescription_Type(DisplayString):
    """Custom type fssTrapDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_FssTrapDescription_Type.__name__ = "DisplayString"
_FssTrapDescription_Object = MibScalar
fssTrapDescription = _FssTrapDescription_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 500, 2),
    _FssTrapDescription_Type()
)
fssTrapDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fssTrapDescription.setStatus("current")
_FssTrapType_Type = FCTrapType
_FssTrapType_Object = MibScalar
fssTrapType = _FssTrapType_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 500, 3),
    _FssTrapType_Type()
)
fssTrapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fssTrapType.setStatus("current")


class _FssTrapTimeStamp_Type(DisplayString):
    """Custom type fssTrapTimeStamp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_FssTrapTimeStamp_Type.__name__ = "DisplayString"
_FssTrapTimeStamp_Object = MibScalar
fssTrapTimeStamp = _FssTrapTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 500, 4),
    _FssTrapTimeStamp_Type()
)
fssTrapTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fssTrapTimeStamp.setStatus("current")
_FssLogConformance_ObjectIdentity = ObjectIdentity
fssLogConformance = _FssLogConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 1000, 100)
)
_FssLogGroups_ObjectIdentity = ObjectIdentity
fssLogGroups = _FssLogGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 1000, 100, 1)
)
_FssLogCompliances_ObjectIdentity = ObjectIdentity
fssLogCompliances = _FssLogCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 1000, 100, 2)
)

# Managed Objects groups

fssLogTrapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 1000, 100, 1, 1)
)
fssLogTrapGroup.setObjects(
    ("FSS-COMMON-LOG", "fssCondQual")
)
if mibBuilder.loadTexts:
    fssLogTrapGroup.setStatus("current")

fssTcaLogTrapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 1000, 100, 1, 2)
)
fssTcaLogTrapGroup.setObjects(
    ("FSS-COMMON-LOG", "fssTcaCondQual")
)
if mibBuilder.loadTexts:
    fssTcaLogTrapGroup.setStatus("current")

fssLogAlarmStandingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 1000, 100, 1, 7)
)
fssLogAlarmStandingGroup.setObjects(
      *(("FSS-COMMON-LOG", "fssStdAlarmType"),
        ("FSS-COMMON-LOG", "fssStdAlarmSeverity"),
        ("FSS-COMMON-LOG", "fssStdAlarmServEffect"))
)
if mibBuilder.loadTexts:
    fssLogAlarmStandingGroup.setStatus("current")


# Notification objects

fssCondTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 200, 100, 0, 1)
)
fssCondTrap.setObjects(
      *(("FSS-COMMON-LOG", "fssTrapObjectName"),
        ("FSS-COMMON-LOG", "fssAlarmType"),
        ("FSS-COMMON-LOG", "fssAlarmCondEffect"),
        ("FSS-COMMON-LOG", "fssAlarmTypeQual"),
        ("FSS-COMMON-LOG", "fssTrapTimeStamp"),
        ("FSS-COMMON-LOG", "fssAlarmSeverity"),
        ("FSS-COMMON-LOG", "fssTrapDescription"),
        ("FSS-COMMON-LOG", "fssAlarmServiceEffect"))
)
if mibBuilder.loadTexts:
    fssCondTrap.setStatus(
        "current"
    )

fssTcaTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 300, 100, 0, 1)
)
fssTcaTrap.setObjects(
      *(("FSS-COMMON-LOG", "fssTrapObjectName"),
        ("FSS-COMMON-LOG", "fssTcaType"),
        ("FSS-COMMON-LOG", "fssTcaTypeQual"),
        ("FSS-COMMON-LOG", "fssTrapTimeStamp"),
        ("FSS-COMMON-LOG", "fssTrapDescription"),
        ("FSS-COMMON-LOG", "fssTcaMonVal"),
        ("FSS-COMMON-LOG", "fssTcaThLev"))
)
if mibBuilder.loadTexts:
    fssTcaTrap.setStatus(
        "current"
    )

fssTcTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 400, 100, 0, 1)
)
fssTcTrap.setObjects(
      *(("FSS-COMMON-LOG", "fssTrapObjectName"),
        ("FSS-COMMON-LOG", "fssTcType"),
        ("FSS-COMMON-LOG", "fssTcTypeQual"),
        ("FSS-COMMON-LOG", "fssTrapTimeStamp"),
        ("FSS-COMMON-LOG", "fssTrapDescription"))
)
if mibBuilder.loadTexts:
    fssTcTrap.setStatus(
        "current"
    )


# Notifications groups

fssLogNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 1000, 100, 1, 100)
)
fssLogNotificationGroup.setObjects(
    ("FSS-COMMON-LOG", "fssCondTrap")
)
if mibBuilder.loadTexts:
    fssLogNotificationGroup.setStatus(
        "current"
    )

fssTcaLogNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 1000, 100, 1, 101)
)
fssTcaLogNotificationGroup.setObjects(
    ("FSS-COMMON-LOG", "fssTcaTrap")
)
if mibBuilder.loadTexts:
    fssTcaLogNotificationGroup.setStatus(
        "current"
    )

fssTcLogNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 1000, 100, 1, 102)
)
fssTcLogNotificationGroup.setObjects(
    ("FSS-COMMON-LOG", "fssTcTrap")
)
if mibBuilder.loadTexts:
    fssTcLogNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

fssLogTrapCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 1000, 100, 2, 1)
)
if mibBuilder.loadTexts:
    fssLogTrapCompliance.setStatus(
        "current"
    )

fssLogStandingCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 1000, 100, 2, 3)
)
if mibBuilder.loadTexts:
    fssLogStandingCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FSS-COMMON-LOG",
    **{"fssAlarm": fssAlarm,
       "fssAlarmCurrent": fssAlarmCurrent,
       "fssStandingAlarmXTable": fssStandingAlarmXTable,
       "fssStandingAlarmXEntry": fssStandingAlarmXEntry,
       "fssStdAlarmObjectIndex": fssStdAlarmObjectIndex,
       "fssStdAlarmTypeIndex": fssStdAlarmTypeIndex,
       "fssStdAlarmObjectName": fssStdAlarmObjectName,
       "fssStdAlarmType": fssStdAlarmType,
       "fssStdAlarmSeverity": fssStdAlarmSeverity,
       "fssStdAlarmServEffect": fssStdAlarmServEffect,
       "fssStdAlarmLocn": fssStdAlarmLocn,
       "fssStdAlarmDir": fssStdAlarmDir,
       "fssAlarmType": fssAlarmType,
       "fssAlarmCondEffect": fssAlarmCondEffect,
       "fssAlarmTypeQual": fssAlarmTypeQual,
       "fssAlarmLocn": fssAlarmLocn,
       "fssAlarmDir": fssAlarmDir,
       "fssAlarmSeverity": fssAlarmSeverity,
       "fssAlarmServiceEffect": fssAlarmServiceEffect,
       "fssAlarmTraps": fssAlarmTraps,
       "fssAlarmPrefix": fssAlarmPrefix,
       "fssCondTrap": fssCondTrap,
       "fssCondQual": fssCondQual,
       "fssTca": fssTca,
       "fssTcaType": fssTcaType,
       "fssTcaTypeQual": fssTcaTypeQual,
       "fssTcaCondEffect": fssTcaCondEffect,
       "fssTcaLocn": fssTcaLocn,
       "fssTcaDir": fssTcaDir,
       "fssTcaMonVal": fssTcaMonVal,
       "fssTcaThLev": fssTcaThLev,
       "fssTcaTimePeriod": fssTcaTimePeriod,
       "fssTcaTraps": fssTcaTraps,
       "fssTcaPrefix": fssTcaPrefix,
       "fssTcaTrap": fssTcaTrap,
       "fssTcaCondQual": fssTcaCondQual,
       "fssTc": fssTc,
       "fssTcType": fssTcType,
       "fssTcTypeQual": fssTcTypeQual,
       "fssTcTraps": fssTcTraps,
       "fssTcPrefix": fssTcPrefix,
       "fssTcTrap": fssTcTrap,
       "fssTcCondQual": fssTcCondQual,
       "fssBase": fssBase,
       "fssTrapObjectName": fssTrapObjectName,
       "fssTrapDescription": fssTrapDescription,
       "fssTrapType": fssTrapType,
       "fssTrapTimeStamp": fssTrapTimeStamp,
       "fssLog": fssLog,
       "fssLogConformance": fssLogConformance,
       "fssLogGroups": fssLogGroups,
       "fssLogTrapGroup": fssLogTrapGroup,
       "fssTcaLogTrapGroup": fssTcaLogTrapGroup,
       "fssLogAlarmStandingGroup": fssLogAlarmStandingGroup,
       "fssLogNotificationGroup": fssLogNotificationGroup,
       "fssTcaLogNotificationGroup": fssTcaLogNotificationGroup,
       "fssTcLogNotificationGroup": fssTcLogNotificationGroup,
       "fssLogCompliances": fssLogCompliances,
       "fssLogTrapCompliance": fssLogTrapCompliance,
       "fssLogStandingCompliance": fssLogStandingCompliance}
)
