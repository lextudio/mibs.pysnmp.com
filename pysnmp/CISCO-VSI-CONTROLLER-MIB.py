# SNMP MIB module (CISCO-VSI-CONTROLLER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-VSI-CONTROLLER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:12:39 2024
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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

ciscoVSIControllerMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 141)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CvcControllerShelfLocation(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("external", 2),
          ("internal", 1))
    )



class CvcControllerType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("lsc", 3),
          ("par", 1),
          ("pnni", 2))
    )



# MIB Managed Objects in the order of their OIDs

_CvcMIBObjects_ObjectIdentity = ObjectIdentity
cvcMIBObjects = _CvcMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 141, 1)
)
_CvcConfController_ObjectIdentity = ObjectIdentity
cvcConfController = _CvcConfController_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 141, 1, 1)
)
_CvcConfTable_Object = MibTable
cvcConfTable = _CvcConfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 141, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cvcConfTable.setStatus("current")
_CvcConfEntry_Object = MibTableRow
cvcConfEntry = _CvcConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 141, 1, 1, 1, 1)
)
cvcConfEntry.setIndexNames(
    (0, "CISCO-VSI-CONTROLLER-MIB", "cvcConfControllerID"),
)
if mibBuilder.loadTexts:
    cvcConfEntry.setStatus("current")


class _CvcConfControllerID_Type(Integer32):
    """Custom type cvcConfControllerID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CvcConfControllerID_Type.__name__ = "Integer32"
_CvcConfControllerID_Object = MibTableColumn
cvcConfControllerID = _CvcConfControllerID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 141, 1, 1, 1, 1, 1),
    _CvcConfControllerID_Type()
)
cvcConfControllerID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cvcConfControllerID.setStatus("current")
_CvcConfControllerType_Type = CvcControllerType
_CvcConfControllerType_Object = MibTableColumn
cvcConfControllerType = _CvcConfControllerType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 141, 1, 1, 1, 1, 2),
    _CvcConfControllerType_Type()
)
cvcConfControllerType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cvcConfControllerType.setStatus("current")
_CvcConfControllerShelfLocation_Type = CvcControllerShelfLocation
_CvcConfControllerShelfLocation_Object = MibTableColumn
cvcConfControllerShelfLocation = _CvcConfControllerShelfLocation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 141, 1, 1, 1, 1, 3),
    _CvcConfControllerShelfLocation_Type()
)
cvcConfControllerShelfLocation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cvcConfControllerShelfLocation.setStatus("current")


class _CvcConfControllerLocation_Type(Integer32):
    """Custom type cvcConfControllerLocation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CvcConfControllerLocation_Type.__name__ = "Integer32"
_CvcConfControllerLocation_Object = MibTableColumn
cvcConfControllerLocation = _CvcConfControllerLocation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 141, 1, 1, 1, 1, 4),
    _CvcConfControllerLocation_Type()
)
cvcConfControllerLocation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cvcConfControllerLocation.setStatus("current")
_CvcConfControllerName_Type = DisplayString
_CvcConfControllerName_Object = MibTableColumn
cvcConfControllerName = _CvcConfControllerName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 141, 1, 1, 1, 1, 5),
    _CvcConfControllerName_Type()
)
cvcConfControllerName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cvcConfControllerName.setStatus("current")


class _CvcConfVpi_Type(Integer32):
    """Custom type cvcConfVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_CvcConfVpi_Type.__name__ = "Integer32"
_CvcConfVpi_Object = MibTableColumn
cvcConfVpi = _CvcConfVpi_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 141, 1, 1, 1, 1, 6),
    _CvcConfVpi_Type()
)
cvcConfVpi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cvcConfVpi.setStatus("current")


class _CvcConfVci_Type(Integer32):
    """Custom type cvcConfVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 65535),
    )


_CvcConfVci_Type.__name__ = "Integer32"
_CvcConfVci_Object = MibTableColumn
cvcConfVci = _CvcConfVci_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 141, 1, 1, 1, 1, 7),
    _CvcConfVci_Type()
)
cvcConfVci.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cvcConfVci.setStatus("current")
_CvcConfRowStatus_Type = RowStatus
_CvcConfRowStatus_Object = MibTableColumn
cvcConfRowStatus = _CvcConfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 141, 1, 1, 1, 1, 8),
    _CvcConfRowStatus_Type()
)
cvcConfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cvcConfRowStatus.setStatus("current")
_CvcMIBConformance_ObjectIdentity = ObjectIdentity
cvcMIBConformance = _CvcMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 141, 3)
)
_CvcMIBCompliances_ObjectIdentity = ObjectIdentity
cvcMIBCompliances = _CvcMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 141, 3, 1)
)
_CvcMIBGroups_ObjectIdentity = ObjectIdentity
cvcMIBGroups = _CvcMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 141, 3, 2)
)

# Managed Objects groups

cvcConfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 141, 3, 2, 1)
)
cvcConfGroup.setObjects(
      *(("CISCO-VSI-CONTROLLER-MIB", "cvcConfControllerType"),
        ("CISCO-VSI-CONTROLLER-MIB", "cvcConfControllerShelfLocation"),
        ("CISCO-VSI-CONTROLLER-MIB", "cvcConfControllerLocation"),
        ("CISCO-VSI-CONTROLLER-MIB", "cvcConfControllerName"),
        ("CISCO-VSI-CONTROLLER-MIB", "cvcConfRowStatus"))
)
if mibBuilder.loadTexts:
    cvcConfGroup.setStatus("current")

cvcConfGroupExternal = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 141, 3, 2, 2)
)
cvcConfGroupExternal.setObjects(
      *(("CISCO-VSI-CONTROLLER-MIB", "cvcConfVpi"),
        ("CISCO-VSI-CONTROLLER-MIB", "cvcConfVci"))
)
if mibBuilder.loadTexts:
    cvcConfGroupExternal.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cvcMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 141, 3, 1, 1)
)
if mibBuilder.loadTexts:
    cvcMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-VSI-CONTROLLER-MIB",
    **{"CvcControllerShelfLocation": CvcControllerShelfLocation,
       "CvcControllerType": CvcControllerType,
       "ciscoVSIControllerMIB": ciscoVSIControllerMIB,
       "cvcMIBObjects": cvcMIBObjects,
       "cvcConfController": cvcConfController,
       "cvcConfTable": cvcConfTable,
       "cvcConfEntry": cvcConfEntry,
       "cvcConfControllerID": cvcConfControllerID,
       "cvcConfControllerType": cvcConfControllerType,
       "cvcConfControllerShelfLocation": cvcConfControllerShelfLocation,
       "cvcConfControllerLocation": cvcConfControllerLocation,
       "cvcConfControllerName": cvcConfControllerName,
       "cvcConfVpi": cvcConfVpi,
       "cvcConfVci": cvcConfVci,
       "cvcConfRowStatus": cvcConfRowStatus,
       "cvcMIBConformance": cvcMIBConformance,
       "cvcMIBCompliances": cvcMIBCompliances,
       "cvcMIBCompliance": cvcMIBCompliance,
       "cvcMIBGroups": cvcMIBGroups,
       "cvcConfGroup": cvcConfGroup,
       "cvcConfGroupExternal": cvcConfGroupExternal}
)
