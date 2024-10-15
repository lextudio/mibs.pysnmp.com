# SNMP MIB module (HH3C-FTM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-FTM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:53:28 2024
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

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

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

hh3cFtmManMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 1, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cFtm_ObjectIdentity = ObjectIdentity
hh3cFtm = _Hh3cFtm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 1)
)
_Hh3cFtmManMIBObjects_ObjectIdentity = ObjectIdentity
hh3cFtmManMIBObjects = _Hh3cFtmManMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 1, 1, 1)
)
_Hh3cFtmUnitTable_Object = MibTable
hh3cFtmUnitTable = _Hh3cFtmUnitTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cFtmUnitTable.setStatus("current")
_Hh3cFtmUnitEntry_Object = MibTableRow
hh3cFtmUnitEntry = _Hh3cFtmUnitEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 1, 1, 1, 1, 1)
)
hh3cFtmUnitEntry.setIndexNames(
    (0, "HH3C-FTM-MIB", "hh3cFtmIndex"),
)
if mibBuilder.loadTexts:
    hh3cFtmUnitEntry.setStatus("current")
_Hh3cFtmIndex_Type = Integer32
_Hh3cFtmIndex_Object = MibTableColumn
hh3cFtmIndex = _Hh3cFtmIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 1, 1, 1, 1, 1, 1),
    _Hh3cFtmIndex_Type()
)
hh3cFtmIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cFtmIndex.setStatus("current")
_Hh3cFtmUnitID_Type = Integer32
_Hh3cFtmUnitID_Object = MibTableColumn
hh3cFtmUnitID = _Hh3cFtmUnitID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 1, 1, 1, 1, 1, 2),
    _Hh3cFtmUnitID_Type()
)
hh3cFtmUnitID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cFtmUnitID.setStatus("current")
_Hh3cFtmUnitName_Type = OctetString
_Hh3cFtmUnitName_Object = MibTableColumn
hh3cFtmUnitName = _Hh3cFtmUnitName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 1, 1, 1, 1, 1, 3),
    _Hh3cFtmUnitName_Type()
)
hh3cFtmUnitName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cFtmUnitName.setStatus("current")


class _Hh3cFtmUnitRole_Type(Integer32):
    """Custom type hh3cFtmUnitRole based on Integer32"""
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


_Hh3cFtmUnitRole_Type.__name__ = "Integer32"
_Hh3cFtmUnitRole_Object = MibTableColumn
hh3cFtmUnitRole = _Hh3cFtmUnitRole_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 1, 1, 1, 1, 1, 4),
    _Hh3cFtmUnitRole_Type()
)
hh3cFtmUnitRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFtmUnitRole.setStatus("current")


class _Hh3cFtmNumberMode_Type(Integer32):
    """Custom type hh3cFtmNumberMode based on Integer32"""
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


_Hh3cFtmNumberMode_Type.__name__ = "Integer32"
_Hh3cFtmNumberMode_Object = MibTableColumn
hh3cFtmNumberMode = _Hh3cFtmNumberMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 1, 1, 1, 1, 1, 5),
    _Hh3cFtmNumberMode_Type()
)
hh3cFtmNumberMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFtmNumberMode.setStatus("current")


class _Hh3cFtmAuthMode_Type(Integer32):
    """Custom type hh3cFtmAuthMode based on Integer32"""
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


_Hh3cFtmAuthMode_Type.__name__ = "Integer32"
_Hh3cFtmAuthMode_Object = MibScalar
hh3cFtmAuthMode = _Hh3cFtmAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 1, 1, 1, 2),
    _Hh3cFtmAuthMode_Type()
)
hh3cFtmAuthMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cFtmAuthMode.setStatus("current")
_Hh3cFtmAuthValue_Type = OctetString
_Hh3cFtmAuthValue_Object = MibScalar
hh3cFtmAuthValue = _Hh3cFtmAuthValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 1, 1, 1, 3),
    _Hh3cFtmAuthValue_Type()
)
hh3cFtmAuthValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cFtmAuthValue.setStatus("current")


class _Hh3cFtmFabricVlanID_Type(Integer32):
    """Custom type hh3cFtmFabricVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 4094),
    )


_Hh3cFtmFabricVlanID_Type.__name__ = "Integer32"
_Hh3cFtmFabricVlanID_Object = MibScalar
hh3cFtmFabricVlanID = _Hh3cFtmFabricVlanID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 1, 1, 1, 4),
    _Hh3cFtmFabricVlanID_Type()
)
hh3cFtmFabricVlanID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cFtmFabricVlanID.setStatus("current")


class _Hh3cFtmFabricType_Type(Integer32):
    """Custom type hh3cFtmFabricType based on Integer32"""
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


_Hh3cFtmFabricType_Type.__name__ = "Integer32"
_Hh3cFtmFabricType_Object = MibScalar
hh3cFtmFabricType = _Hh3cFtmFabricType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 1, 1, 1, 5),
    _Hh3cFtmFabricType_Type()
)
hh3cFtmFabricType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFtmFabricType.setStatus("current")
_Hh3cFtmManMIBComformance_ObjectIdentity = ObjectIdentity
hh3cFtmManMIBComformance = _Hh3cFtmManMIBComformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 1, 1, 2)
)
_Hh3cFtmMIBCompliances_ObjectIdentity = ObjectIdentity
hh3cFtmMIBCompliances = _Hh3cFtmMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 1, 1, 2, 1)
)
_Hh3cFtmMIBGroups_ObjectIdentity = ObjectIdentity
hh3cFtmMIBGroups = _Hh3cFtmMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 1, 1, 2, 2)
)
_Hh3cFtmManMIBNotification_ObjectIdentity = ObjectIdentity
hh3cFtmManMIBNotification = _Hh3cFtmManMIBNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 1, 1, 3)
)

# Managed Objects groups

hh3cFtmConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 2, 1, 1, 2, 2, 1)
)
hh3cFtmConfigGroup.setObjects(
      *(("HH3C-FTM-MIB", "hh3cFtmUnitID"),
        ("HH3C-FTM-MIB", "hh3cFtmUnitName"),
        ("HH3C-FTM-MIB", "hh3cFtmAuthMode"),
        ("HH3C-FTM-MIB", "hh3cFtmAuthValue"),
        ("HH3C-FTM-MIB", "hh3cFtmFabricVlanID"),
        ("HH3C-FTM-MIB", "hh3cFtmFabricType"))
)
if mibBuilder.loadTexts:
    hh3cFtmConfigGroup.setStatus("current")


# Notification objects

hh3cFtmUnitIDChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 1, 1, 3, 1)
)
hh3cFtmUnitIDChange.setObjects(
      *(("HH3C-FTM-MIB", "hh3cFtmIndex"),
        ("HH3C-FTM-MIB", "hh3cFtmUnitID"))
)
if mibBuilder.loadTexts:
    hh3cFtmUnitIDChange.setStatus(
        "current"
    )

hh3cFtmUnitNameChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 1, 1, 3, 2)
)
hh3cFtmUnitNameChange.setObjects(
      *(("HH3C-FTM-MIB", "hh3cFtmIndex"),
        ("HH3C-FTM-MIB", "hh3cFtmUnitName"))
)
if mibBuilder.loadTexts:
    hh3cFtmUnitNameChange.setStatus(
        "current"
    )


# Notifications groups

hh3cFtmNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 25506, 2, 1, 1, 2, 2, 2)
)
hh3cFtmNotificationGroup.setObjects(
      *(("HH3C-FTM-MIB", "hh3cFtmUnitIDChange"),
        ("HH3C-FTM-MIB", "hh3cFtmUnitNameChange"))
)
if mibBuilder.loadTexts:
    hh3cFtmNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hh3cFtmMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 25506, 2, 1, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cFtmMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-FTM-MIB",
    **{"hh3cFtm": hh3cFtm,
       "hh3cFtmManMIB": hh3cFtmManMIB,
       "hh3cFtmManMIBObjects": hh3cFtmManMIBObjects,
       "hh3cFtmUnitTable": hh3cFtmUnitTable,
       "hh3cFtmUnitEntry": hh3cFtmUnitEntry,
       "hh3cFtmIndex": hh3cFtmIndex,
       "hh3cFtmUnitID": hh3cFtmUnitID,
       "hh3cFtmUnitName": hh3cFtmUnitName,
       "hh3cFtmUnitRole": hh3cFtmUnitRole,
       "hh3cFtmNumberMode": hh3cFtmNumberMode,
       "hh3cFtmAuthMode": hh3cFtmAuthMode,
       "hh3cFtmAuthValue": hh3cFtmAuthValue,
       "hh3cFtmFabricVlanID": hh3cFtmFabricVlanID,
       "hh3cFtmFabricType": hh3cFtmFabricType,
       "hh3cFtmManMIBComformance": hh3cFtmManMIBComformance,
       "hh3cFtmMIBCompliances": hh3cFtmMIBCompliances,
       "hh3cFtmMIBCompliance": hh3cFtmMIBCompliance,
       "hh3cFtmMIBGroups": hh3cFtmMIBGroups,
       "hh3cFtmConfigGroup": hh3cFtmConfigGroup,
       "hh3cFtmNotificationGroup": hh3cFtmNotificationGroup,
       "hh3cFtmManMIBNotification": hh3cFtmManMIBNotification,
       "hh3cFtmUnitIDChange": hh3cFtmUnitIDChange,
       "hh3cFtmUnitNameChange": hh3cFtmUnitNameChange}
)
