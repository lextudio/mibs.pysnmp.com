# SNMP MIB module (BROCADE-MAPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BROCADE-MAPS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:49:25 2024
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

(bcsiModules,) = mibBuilder.importSymbols(
    "Brocade-REG-MIB",
    "bcsiModules")

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

(swVfId,) = mibBuilder.importSymbols(
    "SW-MIB",
    "swVfId")


# MODULE-IDENTITY

maps = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 4)
)
maps.setRevisions(
        ("2013-03-01 14:00",
         "2013-04-22 13:30")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MapsTraps_ObjectIdentity = ObjectIdentity
mapsTraps = _MapsTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 4, 0)
)
if mibBuilder.loadTexts:
    mapsTraps.setStatus("current")
_MapsConfig_ObjectIdentity = ObjectIdentity
mapsConfig = _MapsConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 4, 1)
)
if mibBuilder.loadTexts:
    mapsConfig.setStatus("current")


class _MapsConfigRuleName_Type(OctetString):
    """Custom type mapsConfigRuleName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_MapsConfigRuleName_Type.__name__ = "OctetString"
_MapsConfigRuleName_Object = MibScalar
mapsConfigRuleName = _MapsConfigRuleName_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 4, 1, 1),
    _MapsConfigRuleName_Type()
)
mapsConfigRuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mapsConfigRuleName.setStatus("current")


class _MapsConfigCondition_Type(OctetString):
    """Custom type mapsConfigCondition based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_MapsConfigCondition_Type.__name__ = "OctetString"
_MapsConfigCondition_Object = MibScalar
mapsConfigCondition = _MapsConfigCondition_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 4, 1, 2),
    _MapsConfigCondition_Type()
)
mapsConfigCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mapsConfigCondition.setStatus("current")
_MapsConfigNumOfMS_Type = Integer32
_MapsConfigNumOfMS_Object = MibScalar
mapsConfigNumOfMS = _MapsConfigNumOfMS_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 4, 1, 3),
    _MapsConfigNumOfMS_Type()
)
mapsConfigNumOfMS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mapsConfigNumOfMS.setStatus("current")


class _MapsConfigMsName_Type(OctetString):
    """Custom type mapsConfigMsName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_MapsConfigMsName_Type.__name__ = "OctetString"
_MapsConfigMsName_Object = MibScalar
mapsConfigMsName = _MapsConfigMsName_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 4, 1, 4),
    _MapsConfigMsName_Type()
)
mapsConfigMsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mapsConfigMsName.setStatus("current")


class _MapsConfigObjectGroupType_Type(Integer32):
    """Custom type mapsConfigObjectGroupType based on Integer32"""
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
              11,
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("chassis", 12),
          ("cpu", 13),
          ("fan", 3),
          ("flash", 9),
          ("flow", 15),
          ("gbic", 8),
          ("port", 4),
          ("ps", 2),
          ("rule", 10),
          ("slot", 7),
          ("switch", 11),
          ("ts", 6),
          ("unknown", 1),
          ("ve-port-cir", 5),
          ("wwn", 14))
    )


_MapsConfigObjectGroupType_Type.__name__ = "Integer32"
_MapsConfigObjectGroupType_Object = MibScalar
mapsConfigObjectGroupType = _MapsConfigObjectGroupType_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 4, 1, 5),
    _MapsConfigObjectGroupType_Type()
)
mapsConfigObjectGroupType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mapsConfigObjectGroupType.setStatus("current")


class _MapsConfigObjectKeyType_Type(Integer32):
    """Custom type mapsConfigObjectKeyType based on Integer32"""
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
        *(("float", 3),
          ("int32", 1),
          ("string", 4),
          ("uint32", 2))
    )


_MapsConfigObjectKeyType_Type.__name__ = "Integer32"
_MapsConfigObjectKeyType_Object = MibScalar
mapsConfigObjectKeyType = _MapsConfigObjectKeyType_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 4, 1, 6),
    _MapsConfigObjectKeyType_Type()
)
mapsConfigObjectKeyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mapsConfigObjectKeyType.setStatus("current")


class _MapsConfigObjectKeyValue_Type(OctetString):
    """Custom type mapsConfigObjectKeyValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_MapsConfigObjectKeyValue_Type.__name__ = "OctetString"
_MapsConfigObjectKeyValue_Object = MibScalar
mapsConfigObjectKeyValue = _MapsConfigObjectKeyValue_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 4, 1, 7),
    _MapsConfigObjectKeyValue_Type()
)
mapsConfigObjectKeyValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mapsConfigObjectKeyValue.setStatus("current")


class _MapsConfigValueType_Type(Integer32):
    """Custom type mapsConfigValueType based on Integer32"""
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
        *(("float", 3),
          ("int32", 1),
          ("string", 4),
          ("uint32", 2))
    )


_MapsConfigValueType_Type.__name__ = "Integer32"
_MapsConfigValueType_Object = MibScalar
mapsConfigValueType = _MapsConfigValueType_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 4, 1, 8),
    _MapsConfigValueType_Type()
)
mapsConfigValueType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mapsConfigValueType.setStatus("current")


class _MapsConfigCurrentValue_Type(OctetString):
    """Custom type mapsConfigCurrentValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_MapsConfigCurrentValue_Type.__name__ = "OctetString"
_MapsConfigCurrentValue_Object = MibScalar
mapsConfigCurrentValue = _MapsConfigCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 4, 1, 9),
    _MapsConfigCurrentValue_Type()
)
mapsConfigCurrentValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mapsConfigCurrentValue.setStatus("current")


class _MapsConfigTimeBase_Type(OctetString):
    """Custom type mapsConfigTimeBase based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_MapsConfigTimeBase_Type.__name__ = "OctetString"
_MapsConfigTimeBase_Object = MibScalar
mapsConfigTimeBase = _MapsConfigTimeBase_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 4, 1, 10),
    _MapsConfigTimeBase_Type()
)
mapsConfigTimeBase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mapsConfigTimeBase.setStatus("current")


class _MapsConfigSeverityLevel_Type(Integer32):
    """Custom type mapsConfigSeverityLevel based on Integer32"""
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
        *(("critical", 1),
          ("debug", 5),
          ("error", 2),
          ("informational", 4),
          ("warning", 3))
    )


_MapsConfigSeverityLevel_Type.__name__ = "Integer32"
_MapsConfigSeverityLevel_Object = MibScalar
mapsConfigSeverityLevel = _MapsConfigSeverityLevel_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 4, 1, 11),
    _MapsConfigSeverityLevel_Type()
)
mapsConfigSeverityLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mapsConfigSeverityLevel.setStatus("current")


class _MapsConfigMsList_Type(OctetString):
    """Custom type mapsConfigMsList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(128, 128),
    )


_MapsConfigMsList_Type.__name__ = "OctetString"
_MapsConfigMsList_Object = MibScalar
mapsConfigMsList = _MapsConfigMsList_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 4, 1, 12),
    _MapsConfigMsList_Type()
)
mapsConfigMsList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mapsConfigMsList.setStatus("current")
_MapsConfigAction_Type = Integer32
_MapsConfigAction_Object = MibScalar
mapsConfigAction = _MapsConfigAction_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 4, 1, 13),
    _MapsConfigAction_Type()
)
mapsConfigAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mapsConfigAction.setStatus("current")


class _MapsDbCategory_Type(OctetString):
    """Custom type mapsDbCategory based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(24, 24),
    )


_MapsDbCategory_Type.__name__ = "OctetString"
_MapsDbCategory_Object = MibScalar
mapsDbCategory = _MapsDbCategory_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 4, 1, 14),
    _MapsDbCategory_Type()
)
mapsDbCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mapsDbCategory.setStatus("current")

# Managed Objects groups


# Notification objects

mapsTrapAM = NotificationType(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 4, 0, 1)
)
mapsTrapAM.setObjects(
      *(("BROCADE-MAPS-MIB", "mapsConfigRuleName"),
        ("BROCADE-MAPS-MIB", "mapsConfigObjectGroupType"),
        ("BROCADE-MAPS-MIB", "mapsConfigObjectKeyType"),
        ("BROCADE-MAPS-MIB", "mapsConfigObjectKeyValue"),
        ("BROCADE-MAPS-MIB", "mapsConfigNumOfMS"),
        ("BROCADE-MAPS-MIB", "mapsConfigMsList"),
        ("BROCADE-MAPS-MIB", "mapsConfigSeverityLevel"),
        ("BROCADE-MAPS-MIB", "mapsConfigCondition"),
        ("BROCADE-MAPS-MIB", "mapsConfigAction"),
        ("SW-MIB", "swVfId"),
        ("BROCADE-MAPS-MIB", "mapsDbCategory"))
)
if mibBuilder.loadTexts:
    mapsTrapAM.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BROCADE-MAPS-MIB",
    **{"maps": maps,
       "mapsTraps": mapsTraps,
       "mapsTrapAM": mapsTrapAM,
       "mapsConfig": mapsConfig,
       "mapsConfigRuleName": mapsConfigRuleName,
       "mapsConfigCondition": mapsConfigCondition,
       "mapsConfigNumOfMS": mapsConfigNumOfMS,
       "mapsConfigMsName": mapsConfigMsName,
       "mapsConfigObjectGroupType": mapsConfigObjectGroupType,
       "mapsConfigObjectKeyType": mapsConfigObjectKeyType,
       "mapsConfigObjectKeyValue": mapsConfigObjectKeyValue,
       "mapsConfigValueType": mapsConfigValueType,
       "mapsConfigCurrentValue": mapsConfigCurrentValue,
       "mapsConfigTimeBase": mapsConfigTimeBase,
       "mapsConfigSeverityLevel": mapsConfigSeverityLevel,
       "mapsConfigMsList": mapsConfigMsList,
       "mapsConfigAction": mapsConfigAction,
       "mapsDbCategory": mapsDbCategory}
)
