# SNMP MIB module (CISCO-STACKMAKER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-STACKMAKER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:08:53 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

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

ciscoStackMakerMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 59)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoStackMakerMIBObjects_ObjectIdentity = ObjectIdentity
ciscoStackMakerMIBObjects = _CiscoStackMakerMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 59, 1)
)
_CiscoStackMakerConf_ObjectIdentity = ObjectIdentity
ciscoStackMakerConf = _CiscoStackMakerConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 59, 1, 1)
)


class _CsmStackName_Type(DisplayString):
    """Custom type csmStackName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CsmStackName_Type.__name__ = "DisplayString"
_CsmStackName_Object = MibScalar
csmStackName = _CsmStackName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 59, 1, 1, 1),
    _CsmStackName_Type()
)
csmStackName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csmStackName.setStatus("current")


class _CsmClearStackTable_Type(Integer32):
    """Custom type csmClearStackTable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clearTable", 1),
          ("noClearTable", 2))
    )


_CsmClearStackTable_Type.__name__ = "Integer32"
_CsmClearStackTable_Object = MibScalar
csmClearStackTable = _CsmClearStackTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 59, 1, 1, 2),
    _CsmClearStackTable_Type()
)
csmClearStackTable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csmClearStackTable.setStatus("current")
_CsmStackTable_Object = MibTable
csmStackTable = _CsmStackTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 59, 1, 1, 3)
)
if mibBuilder.loadTexts:
    csmStackTable.setStatus("current")
_CsmStackEntry_Object = MibTableRow
csmStackEntry = _CsmStackEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 59, 1, 1, 3, 1)
)
csmStackEntry.setIndexNames(
    (0, "CISCO-STACKMAKER-MIB", "csmStackIndex"),
)
if mibBuilder.loadTexts:
    csmStackEntry.setStatus("current")


class _CsmStackIndex_Type(Integer32):
    """Custom type csmStackIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_CsmStackIndex_Type.__name__ = "Integer32"
_CsmStackIndex_Object = MibTableColumn
csmStackIndex = _CsmStackIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 59, 1, 1, 3, 1, 1),
    _CsmStackIndex_Type()
)
csmStackIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csmStackIndex.setStatus("current")
_CsmStackIpAddress_Type = IpAddress
_CsmStackIpAddress_Object = MibTableColumn
csmStackIpAddress = _CsmStackIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 59, 1, 1, 3, 1, 2),
    _CsmStackIpAddress_Type()
)
csmStackIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    csmStackIpAddress.setStatus("current")
_CiscoStackMakerMIBConformance_ObjectIdentity = ObjectIdentity
ciscoStackMakerMIBConformance = _CiscoStackMakerMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 59, 3)
)
_CiscoStackMakerMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoStackMakerMIBCompliances = _CiscoStackMakerMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 59, 3, 1)
)
_CiscoStackMakerMIBGroups_ObjectIdentity = ObjectIdentity
ciscoStackMakerMIBGroups = _CiscoStackMakerMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 59, 3, 2)
)

# Managed Objects groups

ciscoStackMakerBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 59, 3, 2, 1)
)
ciscoStackMakerBasicGroup.setObjects(
      *(("CISCO-STACKMAKER-MIB", "csmStackName"),
        ("CISCO-STACKMAKER-MIB", "csmClearStackTable"),
        ("CISCO-STACKMAKER-MIB", "csmStackIpAddress"))
)
if mibBuilder.loadTexts:
    ciscoStackMakerBasicGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoStackMakerMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 59, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoStackMakerMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-STACKMAKER-MIB",
    **{"ciscoStackMakerMIB": ciscoStackMakerMIB,
       "ciscoStackMakerMIBObjects": ciscoStackMakerMIBObjects,
       "ciscoStackMakerConf": ciscoStackMakerConf,
       "csmStackName": csmStackName,
       "csmClearStackTable": csmClearStackTable,
       "csmStackTable": csmStackTable,
       "csmStackEntry": csmStackEntry,
       "csmStackIndex": csmStackIndex,
       "csmStackIpAddress": csmStackIpAddress,
       "ciscoStackMakerMIBConformance": ciscoStackMakerMIBConformance,
       "ciscoStackMakerMIBCompliances": ciscoStackMakerMIBCompliances,
       "ciscoStackMakerMIBCompliance": ciscoStackMakerMIBCompliance,
       "ciscoStackMakerMIBGroups": ciscoStackMakerMIBGroups,
       "ciscoStackMakerBasicGroup": ciscoStackMakerBasicGroup}
)
