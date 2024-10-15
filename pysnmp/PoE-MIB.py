# SNMP MIB module (PoE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PoE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:40:30 2024
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

(dlink_common_mgmt,) = mibBuilder.importSymbols(
    "DLINK-ID-REC-MIB",
    "dlink-common-mgmt")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

swPoEMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 24)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SwPoESystemCtrl_ObjectIdentity = ObjectIdentity
swPoESystemCtrl = _SwPoESystemCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 24, 1)
)


class _SwPoESystemPowerLimit_Type(Integer32):
    """Custom type swPoESystemPowerLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(37, 370),
    )


_SwPoESystemPowerLimit_Type.__name__ = "Integer32"
_SwPoESystemPowerLimit_Object = MibScalar
swPoESystemPowerLimit = _SwPoESystemPowerLimit_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 24, 1, 1),
    _SwPoESystemPowerLimit_Type()
)
swPoESystemPowerLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPoESystemPowerLimit.setStatus("current")


class _SwPoESystemPowerDisconnectMethod_Type(Integer32):
    """Custom type swPoESystemPowerDisconnectMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("denyLowPriorityPort", 2),
          ("denyNextPort", 1))
    )


_SwPoESystemPowerDisconnectMethod_Type.__name__ = "Integer32"
_SwPoESystemPowerDisconnectMethod_Object = MibScalar
swPoESystemPowerDisconnectMethod = _SwPoESystemPowerDisconnectMethod_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 24, 1, 2),
    _SwPoESystemPowerDisconnectMethod_Type()
)
swPoESystemPowerDisconnectMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPoESystemPowerDisconnectMethod.setStatus("current")


class _SwPoESystemManagementMode_Type(Integer32):
    """Custom type swPoESystemManagementMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 2),
          ("power-limit", 1))
    )


_SwPoESystemManagementMode_Type.__name__ = "Integer32"
_SwPoESystemManagementMode_Object = MibScalar
swPoESystemManagementMode = _SwPoESystemManagementMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 24, 1, 3),
    _SwPoESystemManagementMode_Type()
)
swPoESystemManagementMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPoESystemManagementMode.setStatus("current")


class _SwPoESystemLedMode_Type(Integer32):
    """Custom type swPoESystemLedMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("poe", 2))
    )


_SwPoESystemLedMode_Type.__name__ = "Integer32"
_SwPoESystemLedMode_Object = MibScalar
swPoESystemLedMode = _SwPoESystemLedMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 24, 1, 4),
    _SwPoESystemLedMode_Type()
)
swPoESystemLedMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPoESystemLedMode.setStatus("current")


class _SwPoESystemCtrlLegacyPD_Type(Integer32):
    """Custom type swPoESystemCtrlLegacyPD based on Integer32"""
    defaultValue = 2

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


_SwPoESystemCtrlLegacyPD_Type.__name__ = "Integer32"
_SwPoESystemCtrlLegacyPD_Object = MibScalar
swPoESystemCtrlLegacyPD = _SwPoESystemCtrlLegacyPD_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 24, 1, 6),
    _SwPoESystemCtrlLegacyPD_Type()
)
swPoESystemCtrlLegacyPD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPoESystemCtrlLegacyPD.setStatus("current")
_SwPoESystemStackingCtrlTable_Object = MibTable
swPoESystemStackingCtrlTable = _SwPoESystemStackingCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 24, 1, 11)
)
if mibBuilder.loadTexts:
    swPoESystemStackingCtrlTable.setStatus("current")
_SwPoESystemStackingCtrlEntry_Object = MibTableRow
swPoESystemStackingCtrlEntry = _SwPoESystemStackingCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 24, 1, 11, 1)
)
swPoESystemStackingCtrlEntry.setIndexNames(
    (0, "PoE-MIB", "swPoESystemStackingCtrlUnitId"),
)
if mibBuilder.loadTexts:
    swPoESystemStackingCtrlEntry.setStatus("current")


class _SwPoESystemStackingCtrlUnitId_Type(Integer32):
    """Custom type swPoESystemStackingCtrlUnitId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwPoESystemStackingCtrlUnitId_Type.__name__ = "Integer32"
_SwPoESystemStackingCtrlUnitId_Object = MibTableColumn
swPoESystemStackingCtrlUnitId = _SwPoESystemStackingCtrlUnitId_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 24, 1, 11, 1, 1),
    _SwPoESystemStackingCtrlUnitId_Type()
)
swPoESystemStackingCtrlUnitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPoESystemStackingCtrlUnitId.setStatus("current")


class _SwPoESystemStackingCtrlPowerLimit_Type(Integer32):
    """Custom type swPoESystemStackingCtrlPowerLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(37, 370),
    )


_SwPoESystemStackingCtrlPowerLimit_Type.__name__ = "Integer32"
_SwPoESystemStackingCtrlPowerLimit_Object = MibTableColumn
swPoESystemStackingCtrlPowerLimit = _SwPoESystemStackingCtrlPowerLimit_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 24, 1, 11, 1, 2),
    _SwPoESystemStackingCtrlPowerLimit_Type()
)
swPoESystemStackingCtrlPowerLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPoESystemStackingCtrlPowerLimit.setStatus("current")


class _SwPoESystemStackingCtrlPowerDisconnectMethod_Type(Integer32):
    """Custom type swPoESystemStackingCtrlPowerDisconnectMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("denyLowPriorityPort", 2),
          ("denyNextPort", 1))
    )


_SwPoESystemStackingCtrlPowerDisconnectMethod_Type.__name__ = "Integer32"
_SwPoESystemStackingCtrlPowerDisconnectMethod_Object = MibTableColumn
swPoESystemStackingCtrlPowerDisconnectMethod = _SwPoESystemStackingCtrlPowerDisconnectMethod_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 24, 1, 11, 1, 3),
    _SwPoESystemStackingCtrlPowerDisconnectMethod_Type()
)
swPoESystemStackingCtrlPowerDisconnectMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPoESystemStackingCtrlPowerDisconnectMethod.setStatus("current")


class _SwPoESystemStackingCtrlManagementMode_Type(Integer32):
    """Custom type swPoESystemStackingCtrlManagementMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 2),
          ("power-limit", 1))
    )


_SwPoESystemStackingCtrlManagementMode_Type.__name__ = "Integer32"
_SwPoESystemStackingCtrlManagementMode_Object = MibTableColumn
swPoESystemStackingCtrlManagementMode = _SwPoESystemStackingCtrlManagementMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 24, 1, 11, 1, 4),
    _SwPoESystemStackingCtrlManagementMode_Type()
)
swPoESystemStackingCtrlManagementMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPoESystemStackingCtrlManagementMode.setStatus("current")


class _SwPoESystemStackingCtrlLedMode_Type(Integer32):
    """Custom type swPoESystemStackingCtrlLedMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("poe", 2))
    )


_SwPoESystemStackingCtrlLedMode_Type.__name__ = "Integer32"
_SwPoESystemStackingCtrlLedMode_Object = MibTableColumn
swPoESystemStackingCtrlLedMode = _SwPoESystemStackingCtrlLedMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 24, 1, 11, 1, 5),
    _SwPoESystemStackingCtrlLedMode_Type()
)
swPoESystemStackingCtrlLedMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPoESystemStackingCtrlLedMode.setStatus("current")


class _SwPoESystemStackingCtrlLegacyPD_Type(Integer32):
    """Custom type swPoESystemStackingCtrlLegacyPD based on Integer32"""
    defaultValue = 2

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


_SwPoESystemStackingCtrlLegacyPD_Type.__name__ = "Integer32"
_SwPoESystemStackingCtrlLegacyPD_Object = MibTableColumn
swPoESystemStackingCtrlLegacyPD = _SwPoESystemStackingCtrlLegacyPD_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 24, 1, 11, 1, 6),
    _SwPoESystemStackingCtrlLegacyPD_Type()
)
swPoESystemStackingCtrlLegacyPD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPoESystemStackingCtrlLegacyPD.setStatus("current")
_SwPoESystemInfo_ObjectIdentity = ObjectIdentity
swPoESystemInfo = _SwPoESystemInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 24, 2)
)
_SwPoESystemInfoTable_Object = MibTable
swPoESystemInfoTable = _SwPoESystemInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 24, 2, 1)
)
if mibBuilder.loadTexts:
    swPoESystemInfoTable.setStatus("current")
_SwPoESystemInfoEntry_Object = MibTableRow
swPoESystemInfoEntry = _SwPoESystemInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 24, 2, 1, 1)
)
swPoESystemInfoEntry.setIndexNames(
    (0, "PoE-MIB", "swPoESystemInfoUnitId"),
)
if mibBuilder.loadTexts:
    swPoESystemInfoEntry.setStatus("current")


class _SwPoESystemInfoUnitId_Type(Integer32):
    """Custom type swPoESystemInfoUnitId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwPoESystemInfoUnitId_Type.__name__ = "Integer32"
_SwPoESystemInfoUnitId_Object = MibTableColumn
swPoESystemInfoUnitId = _SwPoESystemInfoUnitId_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 24, 2, 1, 1, 1),
    _SwPoESystemInfoUnitId_Type()
)
swPoESystemInfoUnitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPoESystemInfoUnitId.setStatus("current")


class _SwPoESystemInfoPowerConsumption_Type(Integer32):
    """Custom type swPoESystemInfoPowerConsumption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 370),
    )


_SwPoESystemInfoPowerConsumption_Type.__name__ = "Integer32"
_SwPoESystemInfoPowerConsumption_Object = MibTableColumn
swPoESystemInfoPowerConsumption = _SwPoESystemInfoPowerConsumption_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 24, 2, 1, 1, 2),
    _SwPoESystemInfoPowerConsumption_Type()
)
swPoESystemInfoPowerConsumption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPoESystemInfoPowerConsumption.setStatus("current")


class _SwPoESystemInfoPowerRemained_Type(Integer32):
    """Custom type swPoESystemInfoPowerRemained based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 370),
    )


_SwPoESystemInfoPowerRemained_Type.__name__ = "Integer32"
_SwPoESystemInfoPowerRemained_Object = MibTableColumn
swPoESystemInfoPowerRemained = _SwPoESystemInfoPowerRemained_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 24, 2, 1, 1, 3),
    _SwPoESystemInfoPowerRemained_Type()
)
swPoESystemInfoPowerRemained.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPoESystemInfoPowerRemained.setStatus("current")


class _SwPoESystemInfoPowerLimit_Type(Integer32):
    """Custom type swPoESystemInfoPowerLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(37, 370),
    )


_SwPoESystemInfoPowerLimit_Type.__name__ = "Integer32"
_SwPoESystemInfoPowerLimit_Object = MibTableColumn
swPoESystemInfoPowerLimit = _SwPoESystemInfoPowerLimit_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 24, 2, 1, 1, 4),
    _SwPoESystemInfoPowerLimit_Type()
)
swPoESystemInfoPowerLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPoESystemInfoPowerLimit.setStatus("current")


class _SwPoESystemInfoPowerDisconnectMethod_Type(Integer32):
    """Custom type swPoESystemInfoPowerDisconnectMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("denyLowPriorityPort", 2),
          ("denyNextPort", 1))
    )


_SwPoESystemInfoPowerDisconnectMethod_Type.__name__ = "Integer32"
_SwPoESystemInfoPowerDisconnectMethod_Object = MibTableColumn
swPoESystemInfoPowerDisconnectMethod = _SwPoESystemInfoPowerDisconnectMethod_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 24, 2, 1, 1, 5),
    _SwPoESystemInfoPowerDisconnectMethod_Type()
)
swPoESystemInfoPowerDisconnectMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPoESystemInfoPowerDisconnectMethod.setStatus("current")


class _SwPoESystemInfoManagementMode_Type(Integer32):
    """Custom type swPoESystemInfoManagementMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 2),
          ("power-limit", 1))
    )


_SwPoESystemInfoManagementMode_Type.__name__ = "Integer32"
_SwPoESystemInfoManagementMode_Object = MibTableColumn
swPoESystemInfoManagementMode = _SwPoESystemInfoManagementMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 24, 2, 1, 1, 6),
    _SwPoESystemInfoManagementMode_Type()
)
swPoESystemInfoManagementMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPoESystemInfoManagementMode.setStatus("current")


class _SwPoESystemInfoLegacyPD_Type(Integer32):
    """Custom type swPoESystemInfoLegacyPD based on Integer32"""
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


_SwPoESystemInfoLegacyPD_Type.__name__ = "Integer32"
_SwPoESystemInfoLegacyPD_Object = MibTableColumn
swPoESystemInfoLegacyPD = _SwPoESystemInfoLegacyPD_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 24, 2, 1, 1, 7),
    _SwPoESystemInfoLegacyPD_Type()
)
swPoESystemInfoLegacyPD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPoESystemInfoLegacyPD.setStatus("current")
_SwPoEPortCtrl_ObjectIdentity = ObjectIdentity
swPoEPortCtrl = _SwPoEPortCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 24, 3)
)
_SwPoEPortCtrlTable_Object = MibTable
swPoEPortCtrlTable = _SwPoEPortCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 24, 3, 1)
)
if mibBuilder.loadTexts:
    swPoEPortCtrlTable.setStatus("current")
_SwPoEPortCtrlEntry_Object = MibTableRow
swPoEPortCtrlEntry = _SwPoEPortCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 24, 3, 1, 1)
)
swPoEPortCtrlEntry.setIndexNames(
    (0, "PoE-MIB", "swPoEPortCtrlPortIndex"),
)
if mibBuilder.loadTexts:
    swPoEPortCtrlEntry.setStatus("current")


class _SwPoEPortCtrlPortIndex_Type(Integer32):
    """Custom type swPoEPortCtrlPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwPoEPortCtrlPortIndex_Type.__name__ = "Integer32"
_SwPoEPortCtrlPortIndex_Object = MibTableColumn
swPoEPortCtrlPortIndex = _SwPoEPortCtrlPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 24, 3, 1, 1, 1),
    _SwPoEPortCtrlPortIndex_Type()
)
swPoEPortCtrlPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPoEPortCtrlPortIndex.setStatus("current")


class _SwPoEPortCtrlState_Type(Integer32):
    """Custom type swPoEPortCtrlState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 3),
          ("enable", 2),
          ("other", 1))
    )


_SwPoEPortCtrlState_Type.__name__ = "Integer32"
_SwPoEPortCtrlState_Object = MibTableColumn
swPoEPortCtrlState = _SwPoEPortCtrlState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 24, 3, 1, 1, 2),
    _SwPoEPortCtrlState_Type()
)
swPoEPortCtrlState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPoEPortCtrlState.setStatus("current")


class _SwPoEPortCtrlPriority_Type(Integer32):
    """Custom type swPoEPortCtrlPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("critical", 1),
          ("high", 2),
          ("low", 3))
    )


_SwPoEPortCtrlPriority_Type.__name__ = "Integer32"
_SwPoEPortCtrlPriority_Object = MibTableColumn
swPoEPortCtrlPriority = _SwPoEPortCtrlPriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 24, 3, 1, 1, 3),
    _SwPoEPortCtrlPriority_Type()
)
swPoEPortCtrlPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPoEPortCtrlPriority.setStatus("current")


class _SwPoEPortCtrlPowerLimit_Type(Integer32):
    """Custom type swPoEPortCtrlPowerLimit based on Integer32"""
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
        *(("class0", 1),
          ("class1", 2),
          ("class2", 3),
          ("class3", 4),
          ("user-defined", 5))
    )


_SwPoEPortCtrlPowerLimit_Type.__name__ = "Integer32"
_SwPoEPortCtrlPowerLimit_Object = MibTableColumn
swPoEPortCtrlPowerLimit = _SwPoEPortCtrlPowerLimit_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 24, 3, 1, 1, 4),
    _SwPoEPortCtrlPowerLimit_Type()
)
swPoEPortCtrlPowerLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPoEPortCtrlPowerLimit.setStatus("current")


class _SwPoEPortCtrlUserDefined_Type(Integer32):
    """Custom type swPoEPortCtrlUserDefined based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 35000),
    )


_SwPoEPortCtrlUserDefined_Type.__name__ = "Integer32"
_SwPoEPortCtrlUserDefined_Object = MibTableColumn
swPoEPortCtrlUserDefined = _SwPoEPortCtrlUserDefined_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 24, 3, 1, 1, 5),
    _SwPoEPortCtrlUserDefined_Type()
)
swPoEPortCtrlUserDefined.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPoEPortCtrlUserDefined.setStatus("current")


class _SwPoEPortCtrlTimeRangeName_Type(SnmpAdminString):
    """Custom type swPoEPortCtrlTimeRangeName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SwPoEPortCtrlTimeRangeName_Type.__name__ = "SnmpAdminString"
_SwPoEPortCtrlTimeRangeName_Object = MibTableColumn
swPoEPortCtrlTimeRangeName = _SwPoEPortCtrlTimeRangeName_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 24, 3, 1, 1, 6),
    _SwPoEPortCtrlTimeRangeName_Type()
)
swPoEPortCtrlTimeRangeName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPoEPortCtrlTimeRangeName.setStatus("current")
_SwPoEPortInfo_ObjectIdentity = ObjectIdentity
swPoEPortInfo = _SwPoEPortInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 24, 4)
)
_SwPoEPortInfoTable_Object = MibTable
swPoEPortInfoTable = _SwPoEPortInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 24, 4, 1)
)
if mibBuilder.loadTexts:
    swPoEPortInfoTable.setStatus("current")
_SwPoEPortInfoEntry_Object = MibTableRow
swPoEPortInfoEntry = _SwPoEPortInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 24, 4, 1, 1)
)
swPoEPortInfoEntry.setIndexNames(
    (0, "PoE-MIB", "swPoEPortInfoPortIndex"),
)
if mibBuilder.loadTexts:
    swPoEPortInfoEntry.setStatus("current")


class _SwPoEPortInfoPortIndex_Type(Integer32):
    """Custom type swPoEPortInfoPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwPoEPortInfoPortIndex_Type.__name__ = "Integer32"
_SwPoEPortInfoPortIndex_Object = MibTableColumn
swPoEPortInfoPortIndex = _SwPoEPortInfoPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 24, 4, 1, 1, 1),
    _SwPoEPortInfoPortIndex_Type()
)
swPoEPortInfoPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPoEPortInfoPortIndex.setStatus("current")


class _SwPoEPortInfoClass_Type(Integer32):
    """Custom type swPoEPortInfoClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_SwPoEPortInfoClass_Type.__name__ = "Integer32"
_SwPoEPortInfoClass_Object = MibTableColumn
swPoEPortInfoClass = _SwPoEPortInfoClass_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 24, 4, 1, 1, 2),
    _SwPoEPortInfoClass_Type()
)
swPoEPortInfoClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPoEPortInfoClass.setStatus("current")
_SwPoEPortInfoPower_Type = Integer32
_SwPoEPortInfoPower_Object = MibTableColumn
swPoEPortInfoPower = _SwPoEPortInfoPower_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 24, 4, 1, 1, 3),
    _SwPoEPortInfoPower_Type()
)
swPoEPortInfoPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPoEPortInfoPower.setStatus("current")
_SwPoEPortInfoVoltage_Type = Integer32
_SwPoEPortInfoVoltage_Object = MibTableColumn
swPoEPortInfoVoltage = _SwPoEPortInfoVoltage_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 24, 4, 1, 1, 4),
    _SwPoEPortInfoVoltage_Type()
)
swPoEPortInfoVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPoEPortInfoVoltage.setStatus("current")
_SwPoEPortInfoCurrent_Type = Integer32
_SwPoEPortInfoCurrent_Object = MibTableColumn
swPoEPortInfoCurrent = _SwPoEPortInfoCurrent_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 24, 4, 1, 1, 5),
    _SwPoEPortInfoCurrent_Type()
)
swPoEPortInfoCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPoEPortInfoCurrent.setStatus("current")


class _SwPoEPortInfoStatus_Type(DisplayString):
    """Custom type swPoEPortInfoStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 76),
    )


_SwPoEPortInfoStatus_Type.__name__ = "DisplayString"
_SwPoEPortInfoStatus_Object = MibTableColumn
swPoEPortInfoStatus = _SwPoEPortInfoStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 24, 4, 1, 1, 6),
    _SwPoEPortInfoStatus_Type()
)
swPoEPortInfoStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPoEPortInfoStatus.setStatus("current")


class _SwpoEPortInfoLedStatus_Type(Integer32):
    """Custom type swpoEPortInfoLedStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("error", 3),
          ("off", 2),
          ("on", 1))
    )


_SwpoEPortInfoLedStatus_Type.__name__ = "Integer32"
_SwpoEPortInfoLedStatus_Object = MibTableColumn
swpoEPortInfoLedStatus = _SwpoEPortInfoLedStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 24, 4, 1, 1, 7),
    _SwpoEPortInfoLedStatus_Type()
)
swpoEPortInfoLedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swpoEPortInfoLedStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PoE-MIB",
    **{"swPoEMIB": swPoEMIB,
       "swPoESystemCtrl": swPoESystemCtrl,
       "swPoESystemPowerLimit": swPoESystemPowerLimit,
       "swPoESystemPowerDisconnectMethod": swPoESystemPowerDisconnectMethod,
       "swPoESystemManagementMode": swPoESystemManagementMode,
       "swPoESystemLedMode": swPoESystemLedMode,
       "swPoESystemCtrlLegacyPD": swPoESystemCtrlLegacyPD,
       "swPoESystemStackingCtrlTable": swPoESystemStackingCtrlTable,
       "swPoESystemStackingCtrlEntry": swPoESystemStackingCtrlEntry,
       "swPoESystemStackingCtrlUnitId": swPoESystemStackingCtrlUnitId,
       "swPoESystemStackingCtrlPowerLimit": swPoESystemStackingCtrlPowerLimit,
       "swPoESystemStackingCtrlPowerDisconnectMethod": swPoESystemStackingCtrlPowerDisconnectMethod,
       "swPoESystemStackingCtrlManagementMode": swPoESystemStackingCtrlManagementMode,
       "swPoESystemStackingCtrlLedMode": swPoESystemStackingCtrlLedMode,
       "swPoESystemStackingCtrlLegacyPD": swPoESystemStackingCtrlLegacyPD,
       "swPoESystemInfo": swPoESystemInfo,
       "swPoESystemInfoTable": swPoESystemInfoTable,
       "swPoESystemInfoEntry": swPoESystemInfoEntry,
       "swPoESystemInfoUnitId": swPoESystemInfoUnitId,
       "swPoESystemInfoPowerConsumption": swPoESystemInfoPowerConsumption,
       "swPoESystemInfoPowerRemained": swPoESystemInfoPowerRemained,
       "swPoESystemInfoPowerLimit": swPoESystemInfoPowerLimit,
       "swPoESystemInfoPowerDisconnectMethod": swPoESystemInfoPowerDisconnectMethod,
       "swPoESystemInfoManagementMode": swPoESystemInfoManagementMode,
       "swPoESystemInfoLegacyPD": swPoESystemInfoLegacyPD,
       "swPoEPortCtrl": swPoEPortCtrl,
       "swPoEPortCtrlTable": swPoEPortCtrlTable,
       "swPoEPortCtrlEntry": swPoEPortCtrlEntry,
       "swPoEPortCtrlPortIndex": swPoEPortCtrlPortIndex,
       "swPoEPortCtrlState": swPoEPortCtrlState,
       "swPoEPortCtrlPriority": swPoEPortCtrlPriority,
       "swPoEPortCtrlPowerLimit": swPoEPortCtrlPowerLimit,
       "swPoEPortCtrlUserDefined": swPoEPortCtrlUserDefined,
       "swPoEPortCtrlTimeRangeName": swPoEPortCtrlTimeRangeName,
       "swPoEPortInfo": swPoEPortInfo,
       "swPoEPortInfoTable": swPoEPortInfoTable,
       "swPoEPortInfoEntry": swPoEPortInfoEntry,
       "swPoEPortInfoPortIndex": swPoEPortInfoPortIndex,
       "swPoEPortInfoClass": swPoEPortInfoClass,
       "swPoEPortInfoPower": swPoEPortInfoPower,
       "swPoEPortInfoVoltage": swPoEPortInfoVoltage,
       "swPoEPortInfoCurrent": swPoEPortInfoCurrent,
       "swPoEPortInfoStatus": swPoEPortInfoStatus,
       "swpoEPortInfoLedStatus": swpoEPortInfoLedStatus}
)
