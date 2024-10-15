# SNMP MIB module (A3COM-HUAWEI-FTM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/A3COM-HUAWEI-FTM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:28:02 2024
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

(h3cCommon,) = mibBuilder.importSymbols(
    "A3COM-HUAWEI-OID-MIB",
    "h3cCommon")

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

h3cFtmManMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 1, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cFtm_ObjectIdentity = ObjectIdentity
h3cFtm = _H3cFtm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 1)
)
_H3cFtmManMIBObjects_ObjectIdentity = ObjectIdentity
h3cFtmManMIBObjects = _H3cFtmManMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 1, 1, 1)
)
_H3cFtmUnitTable_Object = MibTable
h3cFtmUnitTable = _H3cFtmUnitTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    h3cFtmUnitTable.setStatus("current")
_H3cFtmUnitEntry_Object = MibTableRow
h3cFtmUnitEntry = _H3cFtmUnitEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 1, 1, 1, 1, 1)
)
h3cFtmUnitEntry.setIndexNames(
    (0, "A3COM-HUAWEI-FTM-MIB", "h3cFtmIndex"),
)
if mibBuilder.loadTexts:
    h3cFtmUnitEntry.setStatus("current")
_H3cFtmIndex_Type = Integer32
_H3cFtmIndex_Object = MibTableColumn
h3cFtmIndex = _H3cFtmIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 1, 1, 1, 1, 1, 1),
    _H3cFtmIndex_Type()
)
h3cFtmIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cFtmIndex.setStatus("current")
_H3cFtmUnitID_Type = Integer32
_H3cFtmUnitID_Object = MibTableColumn
h3cFtmUnitID = _H3cFtmUnitID_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 1, 1, 1, 1, 1, 2),
    _H3cFtmUnitID_Type()
)
h3cFtmUnitID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cFtmUnitID.setStatus("current")
_H3cFtmUnitName_Type = OctetString
_H3cFtmUnitName_Object = MibTableColumn
h3cFtmUnitName = _H3cFtmUnitName_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 1, 1, 1, 1, 1, 3),
    _H3cFtmUnitName_Type()
)
h3cFtmUnitName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cFtmUnitName.setStatus("current")


class _H3cFtmUnitRole_Type(Integer32):
    """Custom type h3cFtmUnitRole based on Integer32"""
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


_H3cFtmUnitRole_Type.__name__ = "Integer32"
_H3cFtmUnitRole_Object = MibTableColumn
h3cFtmUnitRole = _H3cFtmUnitRole_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 1, 1, 1, 1, 1, 4),
    _H3cFtmUnitRole_Type()
)
h3cFtmUnitRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFtmUnitRole.setStatus("current")


class _H3cFtmNumberMode_Type(Integer32):
    """Custom type h3cFtmNumberMode based on Integer32"""
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


_H3cFtmNumberMode_Type.__name__ = "Integer32"
_H3cFtmNumberMode_Object = MibTableColumn
h3cFtmNumberMode = _H3cFtmNumberMode_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 1, 1, 1, 1, 1, 5),
    _H3cFtmNumberMode_Type()
)
h3cFtmNumberMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFtmNumberMode.setStatus("current")


class _H3cFtmAuthMode_Type(Integer32):
    """Custom type h3cFtmAuthMode based on Integer32"""
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


_H3cFtmAuthMode_Type.__name__ = "Integer32"
_H3cFtmAuthMode_Object = MibScalar
h3cFtmAuthMode = _H3cFtmAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 1, 1, 1, 2),
    _H3cFtmAuthMode_Type()
)
h3cFtmAuthMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cFtmAuthMode.setStatus("current")
_H3cFtmAuthValue_Type = OctetString
_H3cFtmAuthValue_Object = MibScalar
h3cFtmAuthValue = _H3cFtmAuthValue_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 1, 1, 1, 3),
    _H3cFtmAuthValue_Type()
)
h3cFtmAuthValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cFtmAuthValue.setStatus("current")


class _H3cFtmFabricVlanID_Type(Integer32):
    """Custom type h3cFtmFabricVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 4094),
    )


_H3cFtmFabricVlanID_Type.__name__ = "Integer32"
_H3cFtmFabricVlanID_Object = MibScalar
h3cFtmFabricVlanID = _H3cFtmFabricVlanID_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 1, 1, 1, 4),
    _H3cFtmFabricVlanID_Type()
)
h3cFtmFabricVlanID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cFtmFabricVlanID.setStatus("current")


class _H3cFtmFabricType_Type(Integer32):
    """Custom type h3cFtmFabricType based on Integer32"""
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


_H3cFtmFabricType_Type.__name__ = "Integer32"
_H3cFtmFabricType_Object = MibScalar
h3cFtmFabricType = _H3cFtmFabricType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 1, 1, 1, 5),
    _H3cFtmFabricType_Type()
)
h3cFtmFabricType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFtmFabricType.setStatus("current")
_H3cFtmManMIBComformance_ObjectIdentity = ObjectIdentity
h3cFtmManMIBComformance = _H3cFtmManMIBComformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 1, 1, 2)
)
_H3cFtmMIBCompliances_ObjectIdentity = ObjectIdentity
h3cFtmMIBCompliances = _H3cFtmMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 1, 1, 2, 1)
)
_H3cFtmMIBGroups_ObjectIdentity = ObjectIdentity
h3cFtmMIBGroups = _H3cFtmMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 1, 1, 2, 2)
)
_H3cFtmManMIBNotification_ObjectIdentity = ObjectIdentity
h3cFtmManMIBNotification = _H3cFtmManMIBNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 1, 1, 3)
)

# Managed Objects groups

h3cFtmConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 1, 1, 2, 2, 1)
)
h3cFtmConfigGroup.setObjects(
      *(("A3COM-HUAWEI-FTM-MIB", "h3cFtmUnitID"),
        ("A3COM-HUAWEI-FTM-MIB", "h3cFtmUnitName"),
        ("A3COM-HUAWEI-FTM-MIB", "h3cFtmAuthMode"),
        ("A3COM-HUAWEI-FTM-MIB", "h3cFtmAuthValue"),
        ("A3COM-HUAWEI-FTM-MIB", "h3cFtmFabricVlanID"),
        ("A3COM-HUAWEI-FTM-MIB", "h3cFtmFabricType"))
)
if mibBuilder.loadTexts:
    h3cFtmConfigGroup.setStatus("current")


# Notification objects

h3cFtmUnitIDChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 1, 1, 3, 1)
)
h3cFtmUnitIDChange.setObjects(
      *(("A3COM-HUAWEI-FTM-MIB", "h3cFtmIndex"),
        ("A3COM-HUAWEI-FTM-MIB", "h3cFtmUnitID"))
)
if mibBuilder.loadTexts:
    h3cFtmUnitIDChange.setStatus(
        "current"
    )

h3cFtmUnitNameChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 1, 1, 3, 2)
)
h3cFtmUnitNameChange.setObjects(
      *(("A3COM-HUAWEI-FTM-MIB", "h3cFtmIndex"),
        ("A3COM-HUAWEI-FTM-MIB", "h3cFtmUnitName"))
)
if mibBuilder.loadTexts:
    h3cFtmUnitNameChange.setStatus(
        "current"
    )


# Notifications groups

h3cFtmNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 1, 1, 2, 2, 2)
)
h3cFtmNotificationGroup.setObjects(
      *(("A3COM-HUAWEI-FTM-MIB", "h3cFtmUnitIDChange"),
        ("A3COM-HUAWEI-FTM-MIB", "h3cFtmUnitNameChange"))
)
if mibBuilder.loadTexts:
    h3cFtmNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

h3cFtmMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 1, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    h3cFtmMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM-HUAWEI-FTM-MIB",
    **{"h3cFtm": h3cFtm,
       "h3cFtmManMIB": h3cFtmManMIB,
       "h3cFtmManMIBObjects": h3cFtmManMIBObjects,
       "h3cFtmUnitTable": h3cFtmUnitTable,
       "h3cFtmUnitEntry": h3cFtmUnitEntry,
       "h3cFtmIndex": h3cFtmIndex,
       "h3cFtmUnitID": h3cFtmUnitID,
       "h3cFtmUnitName": h3cFtmUnitName,
       "h3cFtmUnitRole": h3cFtmUnitRole,
       "h3cFtmNumberMode": h3cFtmNumberMode,
       "h3cFtmAuthMode": h3cFtmAuthMode,
       "h3cFtmAuthValue": h3cFtmAuthValue,
       "h3cFtmFabricVlanID": h3cFtmFabricVlanID,
       "h3cFtmFabricType": h3cFtmFabricType,
       "h3cFtmManMIBComformance": h3cFtmManMIBComformance,
       "h3cFtmMIBCompliances": h3cFtmMIBCompliances,
       "h3cFtmMIBCompliance": h3cFtmMIBCompliance,
       "h3cFtmMIBGroups": h3cFtmMIBGroups,
       "h3cFtmConfigGroup": h3cFtmConfigGroup,
       "h3cFtmNotificationGroup": h3cFtmNotificationGroup,
       "h3cFtmManMIBNotification": h3cFtmManMIBNotification,
       "h3cFtmUnitIDChange": h3cFtmUnitIDChange,
       "h3cFtmUnitNameChange": h3cFtmUnitNameChange}
)
