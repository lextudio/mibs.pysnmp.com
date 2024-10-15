# SNMP MIB module (HPN-ICF-FTM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-FTM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:00:28 2024
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

(hpnicfCommon,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfCommon")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

hpnicfFtmManMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 1, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpnicfFtm_ObjectIdentity = ObjectIdentity
hpnicfFtm = _HpnicfFtm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 1)
)
_HpnicfFtmManMIBObjects_ObjectIdentity = ObjectIdentity
hpnicfFtmManMIBObjects = _HpnicfFtmManMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 1, 1, 1)
)
_HpnicfFtmUnitTable_Object = MibTable
hpnicfFtmUnitTable = _HpnicfFtmUnitTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hpnicfFtmUnitTable.setStatus("current")
_HpnicfFtmUnitEntry_Object = MibTableRow
hpnicfFtmUnitEntry = _HpnicfFtmUnitEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 1, 1, 1, 1, 1)
)
hpnicfFtmUnitEntry.setIndexNames(
    (0, "HPN-ICF-FTM-MIB", "hpnicfFtmIndex"),
)
if mibBuilder.loadTexts:
    hpnicfFtmUnitEntry.setStatus("current")
_HpnicfFtmIndex_Type = Integer32
_HpnicfFtmIndex_Object = MibTableColumn
hpnicfFtmIndex = _HpnicfFtmIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 1, 1, 1, 1, 1, 1),
    _HpnicfFtmIndex_Type()
)
hpnicfFtmIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfFtmIndex.setStatus("current")
_HpnicfFtmUnitID_Type = Integer32
_HpnicfFtmUnitID_Object = MibTableColumn
hpnicfFtmUnitID = _HpnicfFtmUnitID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 1, 1, 1, 1, 1, 2),
    _HpnicfFtmUnitID_Type()
)
hpnicfFtmUnitID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfFtmUnitID.setStatus("current")
_HpnicfFtmUnitName_Type = OctetString
_HpnicfFtmUnitName_Object = MibTableColumn
hpnicfFtmUnitName = _HpnicfFtmUnitName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 1, 1, 1, 1, 1, 3),
    _HpnicfFtmUnitName_Type()
)
hpnicfFtmUnitName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfFtmUnitName.setStatus("current")


class _HpnicfFtmUnitRole_Type(Integer32):
    """Custom type hpnicfFtmUnitRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("master", 0),
          ("slave", 1))
    )


_HpnicfFtmUnitRole_Type.__name__ = "Integer32"
_HpnicfFtmUnitRole_Object = MibTableColumn
hpnicfFtmUnitRole = _HpnicfFtmUnitRole_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 1, 1, 1, 1, 1, 4),
    _HpnicfFtmUnitRole_Type()
)
hpnicfFtmUnitRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFtmUnitRole.setStatus("current")


class _HpnicfFtmNumberMode_Type(Integer32):
    """Custom type hpnicfFtmNumberMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 0),
          ("manual", 1))
    )


_HpnicfFtmNumberMode_Type.__name__ = "Integer32"
_HpnicfFtmNumberMode_Object = MibTableColumn
hpnicfFtmNumberMode = _HpnicfFtmNumberMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 1, 1, 1, 1, 1, 5),
    _HpnicfFtmNumberMode_Type()
)
hpnicfFtmNumberMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFtmNumberMode.setStatus("current")


class _HpnicfFtmAuthMode_Type(Integer32):
    """Custom type hpnicfFtmAuthMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ftm-md5", 2),
          ("ftm-none", 0),
          ("ftm-simple", 1))
    )


_HpnicfFtmAuthMode_Type.__name__ = "Integer32"
_HpnicfFtmAuthMode_Object = MibScalar
hpnicfFtmAuthMode = _HpnicfFtmAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 1, 1, 1, 2),
    _HpnicfFtmAuthMode_Type()
)
hpnicfFtmAuthMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfFtmAuthMode.setStatus("current")
_HpnicfFtmAuthValue_Type = OctetString
_HpnicfFtmAuthValue_Object = MibScalar
hpnicfFtmAuthValue = _HpnicfFtmAuthValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 1, 1, 1, 3),
    _HpnicfFtmAuthValue_Type()
)
hpnicfFtmAuthValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfFtmAuthValue.setStatus("current")


class _HpnicfFtmFabricVlanID_Type(Integer32):
    """Custom type hpnicfFtmFabricVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 4094),
    )


_HpnicfFtmFabricVlanID_Type.__name__ = "Integer32"
_HpnicfFtmFabricVlanID_Object = MibScalar
hpnicfFtmFabricVlanID = _HpnicfFtmFabricVlanID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 1, 1, 1, 4),
    _HpnicfFtmFabricVlanID_Type()
)
hpnicfFtmFabricVlanID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfFtmFabricVlanID.setStatus("current")


class _HpnicfFtmFabricType_Type(Integer32):
    """Custom type hpnicfFtmFabricType based on Integer32"""
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
        *(("line", 2),
          ("mesh", 4),
          ("outofStack", 1),
          ("ring", 3))
    )


_HpnicfFtmFabricType_Type.__name__ = "Integer32"
_HpnicfFtmFabricType_Object = MibScalar
hpnicfFtmFabricType = _HpnicfFtmFabricType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 1, 1, 1, 5),
    _HpnicfFtmFabricType_Type()
)
hpnicfFtmFabricType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFtmFabricType.setStatus("current")
_HpnicfFtmManMIBComformance_ObjectIdentity = ObjectIdentity
hpnicfFtmManMIBComformance = _HpnicfFtmManMIBComformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 1, 1, 2)
)
_HpnicfFtmMIBCompliances_ObjectIdentity = ObjectIdentity
hpnicfFtmMIBCompliances = _HpnicfFtmMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 1, 1, 2, 1)
)
_HpnicfFtmMIBGroups_ObjectIdentity = ObjectIdentity
hpnicfFtmMIBGroups = _HpnicfFtmMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 1, 1, 2, 2)
)
_HpnicfFtmManMIBNotification_ObjectIdentity = ObjectIdentity
hpnicfFtmManMIBNotification = _HpnicfFtmManMIBNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 1, 1, 3)
)

# Managed Objects groups

hpnicfFtmConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 1, 1, 2, 2, 1)
)
hpnicfFtmConfigGroup.setObjects(
      *(("HPN-ICF-FTM-MIB", "hpnicfFtmUnitID"),
        ("HPN-ICF-FTM-MIB", "hpnicfFtmUnitName"),
        ("HPN-ICF-FTM-MIB", "hpnicfFtmAuthMode"),
        ("HPN-ICF-FTM-MIB", "hpnicfFtmAuthValue"),
        ("HPN-ICF-FTM-MIB", "hpnicfFtmFabricVlanID"),
        ("HPN-ICF-FTM-MIB", "hpnicfFtmFabricType"))
)
if mibBuilder.loadTexts:
    hpnicfFtmConfigGroup.setStatus("current")


# Notification objects

hpnicfFtmUnitIDChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 1, 1, 3, 1)
)
hpnicfFtmUnitIDChange.setObjects(
      *(("HPN-ICF-FTM-MIB", "hpnicfFtmIndex"),
        ("HPN-ICF-FTM-MIB", "hpnicfFtmUnitID"))
)
if mibBuilder.loadTexts:
    hpnicfFtmUnitIDChange.setStatus(
        "current"
    )

hpnicfFtmUnitNameChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 1, 1, 3, 2)
)
hpnicfFtmUnitNameChange.setObjects(
      *(("HPN-ICF-FTM-MIB", "hpnicfFtmIndex"),
        ("HPN-ICF-FTM-MIB", "hpnicfFtmUnitName"))
)
if mibBuilder.loadTexts:
    hpnicfFtmUnitNameChange.setStatus(
        "current"
    )


# Notifications groups

hpnicfFtmNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 1, 1, 2, 2, 2)
)
hpnicfFtmNotificationGroup.setObjects(
      *(("HPN-ICF-FTM-MIB", "hpnicfFtmUnitIDChange"),
        ("HPN-ICF-FTM-MIB", "hpnicfFtmUnitNameChange"))
)
if mibBuilder.loadTexts:
    hpnicfFtmNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hpnicfFtmMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 1, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hpnicfFtmMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-FTM-MIB",
    **{"hpnicfFtm": hpnicfFtm,
       "hpnicfFtmManMIB": hpnicfFtmManMIB,
       "hpnicfFtmManMIBObjects": hpnicfFtmManMIBObjects,
       "hpnicfFtmUnitTable": hpnicfFtmUnitTable,
       "hpnicfFtmUnitEntry": hpnicfFtmUnitEntry,
       "hpnicfFtmIndex": hpnicfFtmIndex,
       "hpnicfFtmUnitID": hpnicfFtmUnitID,
       "hpnicfFtmUnitName": hpnicfFtmUnitName,
       "hpnicfFtmUnitRole": hpnicfFtmUnitRole,
       "hpnicfFtmNumberMode": hpnicfFtmNumberMode,
       "hpnicfFtmAuthMode": hpnicfFtmAuthMode,
       "hpnicfFtmAuthValue": hpnicfFtmAuthValue,
       "hpnicfFtmFabricVlanID": hpnicfFtmFabricVlanID,
       "hpnicfFtmFabricType": hpnicfFtmFabricType,
       "hpnicfFtmManMIBComformance": hpnicfFtmManMIBComformance,
       "hpnicfFtmMIBCompliances": hpnicfFtmMIBCompliances,
       "hpnicfFtmMIBCompliance": hpnicfFtmMIBCompliance,
       "hpnicfFtmMIBGroups": hpnicfFtmMIBGroups,
       "hpnicfFtmConfigGroup": hpnicfFtmConfigGroup,
       "hpnicfFtmNotificationGroup": hpnicfFtmNotificationGroup,
       "hpnicfFtmManMIBNotification": hpnicfFtmManMIBNotification,
       "hpnicfFtmUnitIDChange": hpnicfFtmUnitIDChange,
       "hpnicfFtmUnitNameChange": hpnicfFtmUnitNameChange}
)
