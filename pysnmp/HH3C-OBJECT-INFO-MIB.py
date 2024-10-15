# SNMP MIB module (HH3C-OBJECT-INFO-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-OBJECT-INFO-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:54:24 2024
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

hh3cObjectInfo = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 55)
)
hh3cObjectInfo.setRevisions(
        ("2004-12-27 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cObjectInformation_ObjectIdentity = ObjectIdentity
hh3cObjectInformation = _Hh3cObjectInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 55, 1)
)
_Hh3cObjectInfoTable_Object = MibTable
hh3cObjectInfoTable = _Hh3cObjectInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 55, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cObjectInfoTable.setStatus("current")
_Hh3cObjectInfoEntry_Object = MibTableRow
hh3cObjectInfoEntry = _Hh3cObjectInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 55, 1, 1, 1)
)
hh3cObjectInfoEntry.setIndexNames(
    (0, "HH3C-OBJECT-INFO-MIB", "hh3cObjectInfoOID"),
    (0, "HH3C-OBJECT-INFO-MIB", "hh3cObjectInfoType"),
    (0, "HH3C-OBJECT-INFO-MIB", "hh3cObjectInfoTypeExtension"),
)
if mibBuilder.loadTexts:
    hh3cObjectInfoEntry.setStatus("current")
_Hh3cObjectInfoOID_Type = ObjectIdentifier
_Hh3cObjectInfoOID_Object = MibTableColumn
hh3cObjectInfoOID = _Hh3cObjectInfoOID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 55, 1, 1, 1, 1),
    _Hh3cObjectInfoOID_Type()
)
hh3cObjectInfoOID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cObjectInfoOID.setStatus("current")


class _Hh3cObjectInfoType_Type(Integer32):
    """Custom type hh3cObjectInfoType based on Integer32"""
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
        *(("accessType", 2),
          ("dataLength", 5),
          ("dataRange", 4),
          ("dataType", 3),
          ("reserved", 1))
    )


_Hh3cObjectInfoType_Type.__name__ = "Integer32"
_Hh3cObjectInfoType_Object = MibTableColumn
hh3cObjectInfoType = _Hh3cObjectInfoType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 55, 1, 1, 1, 2),
    _Hh3cObjectInfoType_Type()
)
hh3cObjectInfoType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cObjectInfoType.setStatus("current")


class _Hh3cObjectInfoTypeExtension_Type(OctetString):
    """Custom type hh3cObjectInfoTypeExtension based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_Hh3cObjectInfoTypeExtension_Type.__name__ = "OctetString"
_Hh3cObjectInfoTypeExtension_Object = MibTableColumn
hh3cObjectInfoTypeExtension = _Hh3cObjectInfoTypeExtension_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 55, 1, 1, 1, 3),
    _Hh3cObjectInfoTypeExtension_Type()
)
hh3cObjectInfoTypeExtension.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cObjectInfoTypeExtension.setStatus("current")
_Hh3cObjectInfoValue_Type = OctetString
_Hh3cObjectInfoValue_Object = MibTableColumn
hh3cObjectInfoValue = _Hh3cObjectInfoValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 55, 1, 1, 1, 4),
    _Hh3cObjectInfoValue_Type()
)
hh3cObjectInfoValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cObjectInfoValue.setStatus("current")
_Hh3cObjectInfoMIBConformance_ObjectIdentity = ObjectIdentity
hh3cObjectInfoMIBConformance = _Hh3cObjectInfoMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 55, 2)
)
_Hh3cObjectInfoMIBCompliances_ObjectIdentity = ObjectIdentity
hh3cObjectInfoMIBCompliances = _Hh3cObjectInfoMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 55, 2, 1)
)
_Hh3cObjectInfoMIBGroups_ObjectIdentity = ObjectIdentity
hh3cObjectInfoMIBGroups = _Hh3cObjectInfoMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 55, 2, 2)
)

# Managed Objects groups

hh3cObjectInfoTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 2, 55, 2, 2, 1)
)
hh3cObjectInfoTableGroup.setObjects(
    ("HH3C-OBJECT-INFO-MIB", "hh3cObjectInfoValue")
)
if mibBuilder.loadTexts:
    hh3cObjectInfoTableGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hh3cObjectInfoMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 25506, 2, 55, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cObjectInfoMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-OBJECT-INFO-MIB",
    **{"hh3cObjectInfo": hh3cObjectInfo,
       "hh3cObjectInformation": hh3cObjectInformation,
       "hh3cObjectInfoTable": hh3cObjectInfoTable,
       "hh3cObjectInfoEntry": hh3cObjectInfoEntry,
       "hh3cObjectInfoOID": hh3cObjectInfoOID,
       "hh3cObjectInfoType": hh3cObjectInfoType,
       "hh3cObjectInfoTypeExtension": hh3cObjectInfoTypeExtension,
       "hh3cObjectInfoValue": hh3cObjectInfoValue,
       "hh3cObjectInfoMIBConformance": hh3cObjectInfoMIBConformance,
       "hh3cObjectInfoMIBCompliances": hh3cObjectInfoMIBCompliances,
       "hh3cObjectInfoMIBCompliance": hh3cObjectInfoMIBCompliance,
       "hh3cObjectInfoMIBGroups": hh3cObjectInfoMIBGroups,
       "hh3cObjectInfoTableGroup": hh3cObjectInfoTableGroup}
)
