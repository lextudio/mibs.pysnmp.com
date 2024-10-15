# SNMP MIB module (HP-ICF-CHASSIS) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HP-ICF-CHASSIS
# Produced by pysmi-1.5.4 at Mon Oct 14 21:57:11 2024
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

(hpicfCommon,
 hpicfCommonTrapsPrefix,
 hpicfObjectModules) = mibBuilder.importSymbols(
    "HP-ICF-OID",
    "hpicfCommon",
    "hpicfCommonTrapsPrefix",
    "hpicfObjectModules")

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
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

hpicfChassisMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 3)
)
hpicfChassisMib.setRevisions(
        ("2013-02-10 08:47",
         "2011-08-25 08:47",
         "2010-08-25 00:00",
         "2009-04-22 00:00",
         "2000-11-03 22:16",
         "1997-03-06 03:34",
         "1996-09-10 02:45",
         "1995-07-13 00:00",
         "1994-11-20 00:00",
         "1993-07-09 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpicfChassisConformance_ObjectIdentity = ObjectIdentity
hpicfChassisConformance = _HpicfChassisConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 3, 1)
)
_HpicfChassisCompliances_ObjectIdentity = ObjectIdentity
hpicfChassisCompliances = _HpicfChassisCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 3, 1, 1)
)
_HpicfChassisGroups_ObjectIdentity = ObjectIdentity
hpicfChassisGroups = _HpicfChassisGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 3, 1, 2)
)
_HpicfChassis_ObjectIdentity = ObjectIdentity
hpicfChassis = _HpicfChassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2)
)


class _HpicfChassisId_Type(OctetString):
    """Custom type hpicfChassisId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_HpicfChassisId_Type.__name__ = "OctetString"
_HpicfChassisId_Object = MibScalar
hpicfChassisId = _HpicfChassisId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2, 1),
    _HpicfChassisId_Type()
)
hpicfChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfChassisId.setStatus("deprecated")


class _HpicfChassisNumSlots_Type(Integer32):
    """Custom type hpicfChassisNumSlots based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_HpicfChassisNumSlots_Type.__name__ = "Integer32"
_HpicfChassisNumSlots_Object = MibScalar
hpicfChassisNumSlots = _HpicfChassisNumSlots_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2, 2),
    _HpicfChassisNumSlots_Type()
)
hpicfChassisNumSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfChassisNumSlots.setStatus("deprecated")
_HpicfSlotTable_Object = MibTable
hpicfSlotTable = _HpicfSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2, 3)
)
if mibBuilder.loadTexts:
    hpicfSlotTable.setStatus("deprecated")
_HpicfSlotEntry_Object = MibTableRow
hpicfSlotEntry = _HpicfSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2, 3, 1)
)
hpicfSlotEntry.setIndexNames(
    (0, "HP-ICF-CHASSIS", "hpicfSlotIndex"),
)
if mibBuilder.loadTexts:
    hpicfSlotEntry.setStatus("deprecated")


class _HpicfSlotIndex_Type(Integer32):
    """Custom type hpicfSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_HpicfSlotIndex_Type.__name__ = "Integer32"
_HpicfSlotIndex_Object = MibTableColumn
hpicfSlotIndex = _HpicfSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2, 3, 1, 1),
    _HpicfSlotIndex_Type()
)
hpicfSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfSlotIndex.setStatus("deprecated")
_HpicfSlotObjectId_Type = ObjectIdentifier
_HpicfSlotObjectId_Object = MibTableColumn
hpicfSlotObjectId = _HpicfSlotObjectId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2, 3, 1, 2),
    _HpicfSlotObjectId_Type()
)
hpicfSlotObjectId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfSlotObjectId.setStatus("deprecated")
_HpicfSlotLastChange_Type = TimeStamp
_HpicfSlotLastChange_Object = MibTableColumn
hpicfSlotLastChange = _HpicfSlotLastChange_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2, 3, 1, 3),
    _HpicfSlotLastChange_Type()
)
hpicfSlotLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfSlotLastChange.setStatus("deprecated")


class _HpicfSlotDescr_Type(DisplayString):
    """Custom type hpicfSlotDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpicfSlotDescr_Type.__name__ = "DisplayString"
_HpicfSlotDescr_Object = MibTableColumn
hpicfSlotDescr = _HpicfSlotDescr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2, 3, 1, 4),
    _HpicfSlotDescr_Type()
)
hpicfSlotDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfSlotDescr.setStatus("deprecated")
_HpicfEntityTable_Object = MibTable
hpicfEntityTable = _HpicfEntityTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2, 4)
)
if mibBuilder.loadTexts:
    hpicfEntityTable.setStatus("deprecated")
_HpicfEntityEntry_Object = MibTableRow
hpicfEntityEntry = _HpicfEntityEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2, 4, 1)
)
hpicfEntityEntry.setIndexNames(
    (0, "HP-ICF-CHASSIS", "hpicfEntityIndex"),
)
if mibBuilder.loadTexts:
    hpicfEntityEntry.setStatus("deprecated")


class _HpicfEntityIndex_Type(Integer32):
    """Custom type hpicfEntityIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_HpicfEntityIndex_Type.__name__ = "Integer32"
_HpicfEntityIndex_Object = MibTableColumn
hpicfEntityIndex = _HpicfEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2, 4, 1, 1),
    _HpicfEntityIndex_Type()
)
hpicfEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfEntityIndex.setStatus("deprecated")


class _HpicfEntityFunction_Type(Integer32):
    """Custom type hpicfEntityFunction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_HpicfEntityFunction_Type.__name__ = "Integer32"
_HpicfEntityFunction_Object = MibTableColumn
hpicfEntityFunction = _HpicfEntityFunction_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2, 4, 1, 2),
    _HpicfEntityFunction_Type()
)
hpicfEntityFunction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfEntityFunction.setStatus("deprecated")
_HpicfEntityObjectId_Type = ObjectIdentifier
_HpicfEntityObjectId_Object = MibTableColumn
hpicfEntityObjectId = _HpicfEntityObjectId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2, 4, 1, 3),
    _HpicfEntityObjectId_Type()
)
hpicfEntityObjectId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfEntityObjectId.setStatus("deprecated")


class _HpicfEntityDescr_Type(DisplayString):
    """Custom type hpicfEntityDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpicfEntityDescr_Type.__name__ = "DisplayString"
_HpicfEntityDescr_Object = MibTableColumn
hpicfEntityDescr = _HpicfEntityDescr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2, 4, 1, 4),
    _HpicfEntityDescr_Type()
)
hpicfEntityDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfEntityDescr.setStatus("deprecated")
_HpicfEntityTimestamp_Type = TimeStamp
_HpicfEntityTimestamp_Object = MibTableColumn
hpicfEntityTimestamp = _HpicfEntityTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2, 4, 1, 5),
    _HpicfEntityTimestamp_Type()
)
hpicfEntityTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfEntityTimestamp.setStatus("deprecated")
_HpicfSlotMapTable_Object = MibTable
hpicfSlotMapTable = _HpicfSlotMapTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2, 5)
)
if mibBuilder.loadTexts:
    hpicfSlotMapTable.setStatus("deprecated")
_HpicfSlotMapEntry_Object = MibTableRow
hpicfSlotMapEntry = _HpicfSlotMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2, 5, 1)
)
hpicfSlotMapEntry.setIndexNames(
    (0, "HP-ICF-CHASSIS", "hpicfSlotMapSlot"),
    (0, "HP-ICF-CHASSIS", "hpicfSlotMapEntity"),
)
if mibBuilder.loadTexts:
    hpicfSlotMapEntry.setStatus("deprecated")


class _HpicfSlotMapSlot_Type(Integer32):
    """Custom type hpicfSlotMapSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_HpicfSlotMapSlot_Type.__name__ = "Integer32"
_HpicfSlotMapSlot_Object = MibTableColumn
hpicfSlotMapSlot = _HpicfSlotMapSlot_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2, 5, 1, 1),
    _HpicfSlotMapSlot_Type()
)
hpicfSlotMapSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfSlotMapSlot.setStatus("deprecated")


class _HpicfSlotMapEntity_Type(Integer32):
    """Custom type hpicfSlotMapEntity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_HpicfSlotMapEntity_Type.__name__ = "Integer32"
_HpicfSlotMapEntity_Object = MibTableColumn
hpicfSlotMapEntity = _HpicfSlotMapEntity_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2, 5, 1, 2),
    _HpicfSlotMapEntity_Type()
)
hpicfSlotMapEntity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfSlotMapEntity.setStatus("deprecated")
_HpicfSensorTable_Object = MibTable
hpicfSensorTable = _HpicfSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2, 6)
)
if mibBuilder.loadTexts:
    hpicfSensorTable.setStatus("current")
_HpicfSensorEntry_Object = MibTableRow
hpicfSensorEntry = _HpicfSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2, 6, 1)
)
hpicfSensorEntry.setIndexNames(
    (0, "HP-ICF-CHASSIS", "hpicfSensorIndex"),
)
if mibBuilder.loadTexts:
    hpicfSensorEntry.setStatus("current")


class _HpicfSensorIndex_Type(Integer32):
    """Custom type hpicfSensorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpicfSensorIndex_Type.__name__ = "Integer32"
_HpicfSensorIndex_Object = MibTableColumn
hpicfSensorIndex = _HpicfSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2, 6, 1, 1),
    _HpicfSensorIndex_Type()
)
hpicfSensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfSensorIndex.setStatus("current")
_HpicfSensorObjectId_Type = ObjectIdentifier
_HpicfSensorObjectId_Object = MibTableColumn
hpicfSensorObjectId = _HpicfSensorObjectId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2, 6, 1, 2),
    _HpicfSensorObjectId_Type()
)
hpicfSensorObjectId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfSensorObjectId.setStatus("current")
_HpicfSensorNumber_Type = Integer32
_HpicfSensorNumber_Object = MibTableColumn
hpicfSensorNumber = _HpicfSensorNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2, 6, 1, 3),
    _HpicfSensorNumber_Type()
)
hpicfSensorNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfSensorNumber.setStatus("current")


class _HpicfSensorStatus_Type(Integer32):
    """Custom type hpicfSensorStatus based on Integer32"""
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
        *(("bad", 2),
          ("good", 4),
          ("notPresent", 5),
          ("unknown", 1),
          ("warning", 3))
    )


_HpicfSensorStatus_Type.__name__ = "Integer32"
_HpicfSensorStatus_Object = MibTableColumn
hpicfSensorStatus = _HpicfSensorStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2, 6, 1, 4),
    _HpicfSensorStatus_Type()
)
hpicfSensorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfSensorStatus.setStatus("current")
_HpicfSensorWarnings_Type = Counter32
_HpicfSensorWarnings_Object = MibTableColumn
hpicfSensorWarnings = _HpicfSensorWarnings_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2, 6, 1, 5),
    _HpicfSensorWarnings_Type()
)
hpicfSensorWarnings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfSensorWarnings.setStatus("current")
_HpicfSensorFailures_Type = Counter32
_HpicfSensorFailures_Object = MibTableColumn
hpicfSensorFailures = _HpicfSensorFailures_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2, 6, 1, 6),
    _HpicfSensorFailures_Type()
)
hpicfSensorFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfSensorFailures.setStatus("current")
_HpicfSensorDescr_Type = DisplayString
_HpicfSensorDescr_Object = MibTableColumn
hpicfSensorDescr = _HpicfSensorDescr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2, 6, 1, 7),
    _HpicfSensorDescr_Type()
)
hpicfSensorDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfSensorDescr.setStatus("current")
_HpicfChassisAddrTable_Object = MibTable
hpicfChassisAddrTable = _HpicfChassisAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2, 7)
)
if mibBuilder.loadTexts:
    hpicfChassisAddrTable.setStatus("deprecated")
_HpicfChassisAddrEntry_Object = MibTableRow
hpicfChassisAddrEntry = _HpicfChassisAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2, 7, 1)
)
hpicfChassisAddrEntry.setIndexNames(
    (0, "HP-ICF-CHASSIS", "hpicfChasAddrType"),
    (0, "HP-ICF-CHASSIS", "hpicfChasAddrAddress"),
)
if mibBuilder.loadTexts:
    hpicfChassisAddrEntry.setStatus("deprecated")


class _HpicfChasAddrType_Type(Integer32):
    """Custom type hpicfChasAddrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ipAddr", 1),
          ("ipxAddr", 2),
          ("macAddr", 3))
    )


_HpicfChasAddrType_Type.__name__ = "Integer32"
_HpicfChasAddrType_Object = MibTableColumn
hpicfChasAddrType = _HpicfChasAddrType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2, 7, 1, 1),
    _HpicfChasAddrType_Type()
)
hpicfChasAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfChasAddrType.setStatus("deprecated")


class _HpicfChasAddrAddress_Type(OctetString):
    """Custom type hpicfChasAddrAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 10),
    )


_HpicfChasAddrAddress_Type.__name__ = "OctetString"
_HpicfChasAddrAddress_Object = MibTableColumn
hpicfChasAddrAddress = _HpicfChasAddrAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2, 7, 1, 2),
    _HpicfChasAddrAddress_Type()
)
hpicfChasAddrAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfChasAddrAddress.setStatus("deprecated")


class _HpicfChasAddrEntity_Type(Integer32):
    """Custom type hpicfChasAddrEntity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_HpicfChasAddrEntity_Type.__name__ = "Integer32"
_HpicfChasAddrEntity_Object = MibTableColumn
hpicfChasAddrEntity = _HpicfChasAddrEntity_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2, 7, 1, 3),
    _HpicfChasAddrEntity_Type()
)
hpicfChasAddrEntity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfChasAddrEntity.setStatus("deprecated")
_HpChassisTemperature_ObjectIdentity = ObjectIdentity
hpChassisTemperature = _HpChassisTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2, 8)
)
_HpSystemAirTempTable_Object = MibTable
hpSystemAirTempTable = _HpSystemAirTempTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2, 8, 1)
)
if mibBuilder.loadTexts:
    hpSystemAirTempTable.setStatus("current")
_HpSystemAirTempEntry_Object = MibTableRow
hpSystemAirTempEntry = _HpSystemAirTempEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2, 8, 1, 1)
)
hpSystemAirTempEntry.setIndexNames(
    (0, "HP-ICF-CHASSIS", "hpSystemAirSensor"),
)
if mibBuilder.loadTexts:
    hpSystemAirTempEntry.setStatus("current")


class _HpSystemAirSensor_Type(Integer32):
    """Custom type hpSystemAirSensor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HpSystemAirSensor_Type.__name__ = "Integer32"
_HpSystemAirSensor_Object = MibTableColumn
hpSystemAirSensor = _HpSystemAirSensor_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2, 8, 1, 1, 1),
    _HpSystemAirSensor_Type()
)
hpSystemAirSensor.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpSystemAirSensor.setStatus("current")


class _HpSystemAirName_Type(OctetString):
    """Custom type hpSystemAirName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_HpSystemAirName_Type.__name__ = "OctetString"
_HpSystemAirName_Object = MibTableColumn
hpSystemAirName = _HpSystemAirName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2, 8, 1, 1, 2),
    _HpSystemAirName_Type()
)
hpSystemAirName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSystemAirName.setStatus("current")


class _HpSystemAirCurrentTemp_Type(OctetString):
    """Custom type hpSystemAirCurrentTemp based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 6),
    )


_HpSystemAirCurrentTemp_Type.__name__ = "OctetString"
_HpSystemAirCurrentTemp_Object = MibTableColumn
hpSystemAirCurrentTemp = _HpSystemAirCurrentTemp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2, 8, 1, 1, 3),
    _HpSystemAirCurrentTemp_Type()
)
hpSystemAirCurrentTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSystemAirCurrentTemp.setStatus("current")


class _HpSystemAirMaxTemp_Type(OctetString):
    """Custom type hpSystemAirMaxTemp based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 6),
    )


_HpSystemAirMaxTemp_Type.__name__ = "OctetString"
_HpSystemAirMaxTemp_Object = MibTableColumn
hpSystemAirMaxTemp = _HpSystemAirMaxTemp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2, 8, 1, 1, 4),
    _HpSystemAirMaxTemp_Type()
)
hpSystemAirMaxTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSystemAirMaxTemp.setStatus("current")


class _HpSystemAirMinTemp_Type(OctetString):
    """Custom type hpSystemAirMinTemp based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 6),
    )


_HpSystemAirMinTemp_Type.__name__ = "OctetString"
_HpSystemAirMinTemp_Object = MibTableColumn
hpSystemAirMinTemp = _HpSystemAirMinTemp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2, 8, 1, 1, 5),
    _HpSystemAirMinTemp_Type()
)
hpSystemAirMinTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSystemAirMinTemp.setStatus("current")


class _HpSystemAirOverTemp_Type(Integer32):
    """Custom type hpSystemAirOverTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_HpSystemAirOverTemp_Type.__name__ = "Integer32"
_HpSystemAirOverTemp_Object = MibTableColumn
hpSystemAirOverTemp = _HpSystemAirOverTemp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2, 8, 1, 1, 6),
    _HpSystemAirOverTemp_Type()
)
hpSystemAirOverTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSystemAirOverTemp.setStatus("current")


class _HpSystemAirThresholdTemp_Type(OctetString):
    """Custom type hpSystemAirThresholdTemp based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 6),
    )


_HpSystemAirThresholdTemp_Type.__name__ = "OctetString"
_HpSystemAirThresholdTemp_Object = MibTableColumn
hpSystemAirThresholdTemp = _HpSystemAirThresholdTemp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2, 8, 1, 1, 7),
    _HpSystemAirThresholdTemp_Type()
)
hpSystemAirThresholdTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSystemAirThresholdTemp.setStatus("current")


class _HpSystemAirAvgTemp_Type(OctetString):
    """Custom type hpSystemAirAvgTemp based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 5),
    )


_HpSystemAirAvgTemp_Type.__name__ = "OctetString"
_HpSystemAirAvgTemp_Object = MibTableColumn
hpSystemAirAvgTemp = _HpSystemAirAvgTemp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2, 8, 1, 1, 8),
    _HpSystemAirAvgTemp_Type()
)
hpSystemAirAvgTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSystemAirAvgTemp.setStatus("deprecated")
_HpSystemAirEntPhysicalIndex_Type = PhysicalIndex
_HpSystemAirEntPhysicalIndex_Object = MibTableColumn
hpSystemAirEntPhysicalIndex = _HpSystemAirEntPhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2, 8, 1, 1, 9),
    _HpSystemAirEntPhysicalIndex_Type()
)
hpSystemAirEntPhysicalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSystemAirEntPhysicalIndex.setStatus("current")


class _HpSystemAirAvgTemp1_Type(OctetString):
    """Custom type hpSystemAirAvgTemp1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 6),
    )


_HpSystemAirAvgTemp1_Type.__name__ = "OctetString"
_HpSystemAirAvgTemp1_Object = MibTableColumn
hpSystemAirAvgTemp1 = _HpSystemAirAvgTemp1_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2, 8, 1, 1, 10),
    _HpSystemAirAvgTemp1_Type()
)
hpSystemAirAvgTemp1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSystemAirAvgTemp1.setStatus("current")


class _HpicfFanTrayType_Type(Integer32):
    """Custom type hpicfFanTrayType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("highPerformance", 2),
          ("standard", 1))
    )


_HpicfFanTrayType_Type.__name__ = "Integer32"
_HpicfFanTrayType_Object = MibScalar
hpicfFanTrayType = _HpicfFanTrayType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2, 9),
    _HpicfFanTrayType_Type()
)
hpicfFanTrayType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfFanTrayType.setStatus("current")


class _HpicfOpacityShieldInstalled_Type(TruthValue):
    """Custom type hpicfOpacityShieldInstalled based on TruthValue"""


_HpicfOpacityShieldInstalled_Object = MibScalar
hpicfOpacityShieldInstalled = _HpicfOpacityShieldInstalled_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2, 10),
    _HpicfOpacityShieldInstalled_Type()
)
hpicfOpacityShieldInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOpacityShieldInstalled.setStatus("current")

# Managed Objects groups

hpicfChassisBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 3, 1, 2, 1)
)
hpicfChassisBasicGroup.setObjects(
      *(("HP-ICF-CHASSIS", "hpicfChassisId"),
        ("HP-ICF-CHASSIS", "hpicfChassisNumSlots"),
        ("HP-ICF-CHASSIS", "hpicfSlotIndex"),
        ("HP-ICF-CHASSIS", "hpicfSlotObjectId"),
        ("HP-ICF-CHASSIS", "hpicfSlotLastChange"),
        ("HP-ICF-CHASSIS", "hpicfSlotDescr"),
        ("HP-ICF-CHASSIS", "hpicfEntityIndex"),
        ("HP-ICF-CHASSIS", "hpicfEntityFunction"),
        ("HP-ICF-CHASSIS", "hpicfEntityObjectId"),
        ("HP-ICF-CHASSIS", "hpicfEntityDescr"),
        ("HP-ICF-CHASSIS", "hpicfEntityTimestamp"),
        ("HP-ICF-CHASSIS", "hpicfSlotMapSlot"),
        ("HP-ICF-CHASSIS", "hpicfSlotMapEntity"))
)
if mibBuilder.loadTexts:
    hpicfChassisBasicGroup.setStatus("deprecated")

hpicfSensorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 3, 1, 2, 2)
)
hpicfSensorGroup.setObjects(
      *(("HP-ICF-CHASSIS", "hpicfSensorIndex"),
        ("HP-ICF-CHASSIS", "hpicfSensorObjectId"),
        ("HP-ICF-CHASSIS", "hpicfSensorNumber"),
        ("HP-ICF-CHASSIS", "hpicfSensorStatus"),
        ("HP-ICF-CHASSIS", "hpicfSensorWarnings"),
        ("HP-ICF-CHASSIS", "hpicfSensorFailures"),
        ("HP-ICF-CHASSIS", "hpicfSensorDescr"))
)
if mibBuilder.loadTexts:
    hpicfSensorGroup.setStatus("current")

hpicfChassisAddrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 3, 1, 2, 3)
)
hpicfChassisAddrGroup.setObjects(
    ("HP-ICF-CHASSIS", "hpicfChasAddrEntity")
)
if mibBuilder.loadTexts:
    hpicfChassisAddrGroup.setStatus("deprecated")

hpicfChasTempGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 3, 1, 2, 5)
)
hpicfChasTempGroup.setObjects(
      *(("HP-ICF-CHASSIS", "hpSystemAirName"),
        ("HP-ICF-CHASSIS", "hpSystemAirCurrentTemp"),
        ("HP-ICF-CHASSIS", "hpSystemAirMaxTemp"),
        ("HP-ICF-CHASSIS", "hpSystemAirMinTemp"),
        ("HP-ICF-CHASSIS", "hpSystemAirThresholdTemp"),
        ("HP-ICF-CHASSIS", "hpSystemAirOverTemp"),
        ("HP-ICF-CHASSIS", "hpSystemAirAvgTemp"),
        ("HP-ICF-CHASSIS", "hpSystemAirEntPhysicalIndex"))
)
if mibBuilder.loadTexts:
    hpicfChasTempGroup.setStatus("deprecated")

hpicfOpacityShieldsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 3, 1, 2, 6)
)
hpicfOpacityShieldsGroup.setObjects(
      *(("HP-ICF-CHASSIS", "hpicfFanTrayType"),
        ("HP-ICF-CHASSIS", "hpicfOpacityShieldInstalled"))
)
if mibBuilder.loadTexts:
    hpicfOpacityShieldsGroup.setStatus("current")

hpicfChasTempGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 3, 1, 2, 7)
)
hpicfChasTempGroup1.setObjects(
      *(("HP-ICF-CHASSIS", "hpSystemAirName"),
        ("HP-ICF-CHASSIS", "hpSystemAirCurrentTemp"),
        ("HP-ICF-CHASSIS", "hpSystemAirMaxTemp"),
        ("HP-ICF-CHASSIS", "hpSystemAirMinTemp"),
        ("HP-ICF-CHASSIS", "hpSystemAirThresholdTemp"),
        ("HP-ICF-CHASSIS", "hpSystemAirOverTemp"),
        ("HP-ICF-CHASSIS", "hpSystemAirAvgTemp"),
        ("HP-ICF-CHASSIS", "hpSystemAirAvgTemp1"),
        ("HP-ICF-CHASSIS", "hpSystemAirEntPhysicalIndex"))
)
if mibBuilder.loadTexts:
    hpicfChasTempGroup1.setStatus("current")


# Notification objects

hpicfSensorTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 12, 1, 0, 3)
)
hpicfSensorTrap.setObjects(
      *(("HP-ICF-CHASSIS", "hpicfSensorStatus"),
        ("HP-ICF-CHASSIS", "hpicfSensorDescr"))
)
if mibBuilder.loadTexts:
    hpicfSensorTrap.setStatus(
        "current"
    )


# Notifications groups

hpicfSensorNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 3, 1, 2, 4)
)
hpicfSensorNotifyGroup.setObjects(
    ("HP-ICF-CHASSIS", "hpicfSensorTrap")
)
if mibBuilder.loadTexts:
    hpicfSensorNotifyGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hpicfChasAdvStkCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 3, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hpicfChasAdvStkCompliance.setStatus(
        "deprecated"
    )

hpicfChasAdvStk2Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 3, 1, 1, 2)
)
if mibBuilder.loadTexts:
    hpicfChasAdvStk2Compliance.setStatus(
        "deprecated"
    )

hpicfChasSensorCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 3, 1, 1, 3)
)
if mibBuilder.loadTexts:
    hpicfChasSensorCompliance.setStatus(
        "current"
    )

hpicfChasTempCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 3, 1, 1, 4)
)
if mibBuilder.loadTexts:
    hpicfChasTempCompliance.setStatus(
        "deprecated"
    )

hpicfOpacityShieldsCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 3, 1, 1, 5)
)
if mibBuilder.loadTexts:
    hpicfOpacityShieldsCompliance.setStatus(
        "current"
    )

hpicfChasTempCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 3, 1, 1, 6)
)
if mibBuilder.loadTexts:
    hpicfChasTempCompliance1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-ICF-CHASSIS",
    **{"hpicfChassisMib": hpicfChassisMib,
       "hpicfChassisConformance": hpicfChassisConformance,
       "hpicfChassisCompliances": hpicfChassisCompliances,
       "hpicfChasAdvStkCompliance": hpicfChasAdvStkCompliance,
       "hpicfChasAdvStk2Compliance": hpicfChasAdvStk2Compliance,
       "hpicfChasSensorCompliance": hpicfChasSensorCompliance,
       "hpicfChasTempCompliance": hpicfChasTempCompliance,
       "hpicfOpacityShieldsCompliance": hpicfOpacityShieldsCompliance,
       "hpicfChasTempCompliance1": hpicfChasTempCompliance1,
       "hpicfChassisGroups": hpicfChassisGroups,
       "hpicfChassisBasicGroup": hpicfChassisBasicGroup,
       "hpicfSensorGroup": hpicfSensorGroup,
       "hpicfChassisAddrGroup": hpicfChassisAddrGroup,
       "hpicfSensorNotifyGroup": hpicfSensorNotifyGroup,
       "hpicfChasTempGroup": hpicfChasTempGroup,
       "hpicfOpacityShieldsGroup": hpicfOpacityShieldsGroup,
       "hpicfChasTempGroup1": hpicfChasTempGroup1,
       "hpicfChassis": hpicfChassis,
       "hpicfChassisId": hpicfChassisId,
       "hpicfChassisNumSlots": hpicfChassisNumSlots,
       "hpicfSlotTable": hpicfSlotTable,
       "hpicfSlotEntry": hpicfSlotEntry,
       "hpicfSlotIndex": hpicfSlotIndex,
       "hpicfSlotObjectId": hpicfSlotObjectId,
       "hpicfSlotLastChange": hpicfSlotLastChange,
       "hpicfSlotDescr": hpicfSlotDescr,
       "hpicfEntityTable": hpicfEntityTable,
       "hpicfEntityEntry": hpicfEntityEntry,
       "hpicfEntityIndex": hpicfEntityIndex,
       "hpicfEntityFunction": hpicfEntityFunction,
       "hpicfEntityObjectId": hpicfEntityObjectId,
       "hpicfEntityDescr": hpicfEntityDescr,
       "hpicfEntityTimestamp": hpicfEntityTimestamp,
       "hpicfSlotMapTable": hpicfSlotMapTable,
       "hpicfSlotMapEntry": hpicfSlotMapEntry,
       "hpicfSlotMapSlot": hpicfSlotMapSlot,
       "hpicfSlotMapEntity": hpicfSlotMapEntity,
       "hpicfSensorTable": hpicfSensorTable,
       "hpicfSensorEntry": hpicfSensorEntry,
       "hpicfSensorIndex": hpicfSensorIndex,
       "hpicfSensorObjectId": hpicfSensorObjectId,
       "hpicfSensorNumber": hpicfSensorNumber,
       "hpicfSensorStatus": hpicfSensorStatus,
       "hpicfSensorWarnings": hpicfSensorWarnings,
       "hpicfSensorFailures": hpicfSensorFailures,
       "hpicfSensorDescr": hpicfSensorDescr,
       "hpicfChassisAddrTable": hpicfChassisAddrTable,
       "hpicfChassisAddrEntry": hpicfChassisAddrEntry,
       "hpicfChasAddrType": hpicfChasAddrType,
       "hpicfChasAddrAddress": hpicfChasAddrAddress,
       "hpicfChasAddrEntity": hpicfChasAddrEntity,
       "hpChassisTemperature": hpChassisTemperature,
       "hpSystemAirTempTable": hpSystemAirTempTable,
       "hpSystemAirTempEntry": hpSystemAirTempEntry,
       "hpSystemAirSensor": hpSystemAirSensor,
       "hpSystemAirName": hpSystemAirName,
       "hpSystemAirCurrentTemp": hpSystemAirCurrentTemp,
       "hpSystemAirMaxTemp": hpSystemAirMaxTemp,
       "hpSystemAirMinTemp": hpSystemAirMinTemp,
       "hpSystemAirOverTemp": hpSystemAirOverTemp,
       "hpSystemAirThresholdTemp": hpSystemAirThresholdTemp,
       "hpSystemAirAvgTemp": hpSystemAirAvgTemp,
       "hpSystemAirEntPhysicalIndex": hpSystemAirEntPhysicalIndex,
       "hpSystemAirAvgTemp1": hpSystemAirAvgTemp1,
       "hpicfFanTrayType": hpicfFanTrayType,
       "hpicfOpacityShieldInstalled": hpicfOpacityShieldInstalled,
       "hpicfSensorTrap": hpicfSensorTrap}
)
