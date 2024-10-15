# SNMP MIB module (CISCO-WAN-TRAP-VARS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-WAN-TRAP-VARS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:13:23 2024
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

(ciscoWan,) = mibBuilder.importSymbols(
    "CISCOWAN-SMI",
    "ciscoWan")

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

(AutonomousType,
 DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "AutonomousType",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

ciscoWanTrapVarsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 5)
)
ciscoWanTrapVarsMIB.setRevisions(
        ("2002-11-26 00:00",
         "2002-07-17 00:00",
         "2001-11-07 00:00",
         "2001-11-06 00:00",
         "2001-07-26 00:00",
         "1999-05-21 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CwTrapVarMIBObjects_ObjectIdentity = ObjectIdentity
cwTrapVarMIBObjects = _CwTrapVarMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 5, 1)
)
_CwTrapVars_ObjectIdentity = ObjectIdentity
cwTrapVars = _CwTrapVars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 5, 1, 1)
)


class _CwTrapIndex_Type(Integer32):
    """Custom type cwTrapIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwTrapIndex_Type.__name__ = "Integer32"
_CwTrapIndex_Object = MibScalar
cwTrapIndex = _CwTrapIndex_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 5, 1, 1, 1),
    _CwTrapIndex_Type()
)
cwTrapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwTrapIndex.setStatus("current")


class _CwTrapSlotNumber_Type(Integer32):
    """Custom type cwTrapSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_CwTrapSlotNumber_Type.__name__ = "Integer32"
_CwTrapSlotNumber_Object = MibScalar
cwTrapSlotNumber = _CwTrapSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 5, 1, 1, 2),
    _CwTrapSlotNumber_Type()
)
cwTrapSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwTrapSlotNumber.setStatus("current")
_CwTrapPhysicalVendorType_Type = AutonomousType
_CwTrapPhysicalVendorType_Object = MibScalar
cwTrapPhysicalVendorType = _CwTrapPhysicalVendorType_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 5, 1, 1, 3),
    _CwTrapPhysicalVendorType_Type()
)
cwTrapPhysicalVendorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwTrapPhysicalVendorType.setStatus("current")


class _CwTrapLineModuleNumber_Type(Integer32):
    """Custom type cwTrapLineModuleNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_CwTrapLineModuleNumber_Type.__name__ = "Integer32"
_CwTrapLineModuleNumber_Object = MibScalar
cwTrapLineModuleNumber = _CwTrapLineModuleNumber_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 5, 1, 1, 4),
    _CwTrapLineModuleNumber_Type()
)
cwTrapLineModuleNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwTrapLineModuleNumber.setStatus("current")


class _CwTrapOctetString_Type(OctetString):
    """Custom type cwTrapOctetString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_CwTrapOctetString_Type.__name__ = "OctetString"
_CwTrapOctetString_Object = MibScalar
cwTrapOctetString = _CwTrapOctetString_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 5, 1, 1, 5),
    _CwTrapOctetString_Type()
)
cwTrapOctetString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwTrapOctetString.setStatus("current")
_CwTrapDisplayString_Type = DisplayString
_CwTrapDisplayString_Object = MibScalar
cwTrapDisplayString = _CwTrapDisplayString_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 5, 1, 1, 6),
    _CwTrapDisplayString_Type()
)
cwTrapDisplayString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwTrapDisplayString.setStatus("current")


class _CwTrapPhysicalContainer_Type(Integer32):
    """Custom type cwTrapPhysicalContainer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwTrapPhysicalContainer_Type.__name__ = "Integer32"
_CwTrapPhysicalContainer_Object = MibScalar
cwTrapPhysicalContainer = _CwTrapPhysicalContainer_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 5, 1, 1, 7),
    _CwTrapPhysicalContainer_Type()
)
cwTrapPhysicalContainer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwTrapPhysicalContainer.setStatus("current")


class _CwTrapPhysicalUnit_Type(Integer32):
    """Custom type cwTrapPhysicalUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwTrapPhysicalUnit_Type.__name__ = "Integer32"
_CwTrapPhysicalUnit_Object = MibScalar
cwTrapPhysicalUnit = _CwTrapPhysicalUnit_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 5, 1, 1, 8),
    _CwTrapPhysicalUnit_Type()
)
cwTrapPhysicalUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwTrapPhysicalUnit.setStatus("current")


class _CwTrapCardRole_Type(Integer32):
    """Custom type cwTrapCardRole based on Integer32"""
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
        *(("e1", 2),
          ("e3", 4),
          ("t1", 1),
          ("t3", 3))
    )


_CwTrapCardRole_Type.__name__ = "Integer32"
_CwTrapCardRole_Object = MibScalar
cwTrapCardRole = _CwTrapCardRole_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 5, 1, 1, 9),
    _CwTrapCardRole_Type()
)
cwTrapCardRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwTrapCardRole.setStatus("current")


class _CwTrapSctCardType_Type(Integer32):
    """Custom type cwTrapSctCardType based on Integer32"""
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
        *(("axsm", 1),
          ("axsme", 2),
          ("hsfr", 4),
          ("pxm1e", 3))
    )


_CwTrapSctCardType_Type.__name__ = "Integer32"
_CwTrapSctCardType_Object = MibScalar
cwTrapSctCardType = _CwTrapSctCardType_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 5, 1, 1, 10),
    _CwTrapSctCardType_Type()
)
cwTrapSctCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwTrapSctCardType.setStatus("current")


class _CwTrapSctType_Type(Integer32):
    """Custom type cwTrapSctType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cardSct", 2),
          ("portSct", 1))
    )


_CwTrapSctType_Type.__name__ = "Integer32"
_CwTrapSctType_Object = MibScalar
cwTrapSctType = _CwTrapSctType_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 5, 1, 1, 11),
    _CwTrapSctType_Type()
)
cwTrapSctType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwTrapSctType.setStatus("current")


class _CwTrapSctId_Type(Unsigned32):
    """Custom type cwTrapSctId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CwTrapSctId_Type.__name__ = "Unsigned32"
_CwTrapSctId_Object = MibScalar
cwTrapSctId = _CwTrapSctId_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 5, 1, 1, 12),
    _CwTrapSctId_Type()
)
cwTrapSctId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwTrapSctId.setStatus("current")


class _CwTrapSctMajorVersion_Type(Unsigned32):
    """Custom type cwTrapSctMajorVersion based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CwTrapSctMajorVersion_Type.__name__ = "Unsigned32"
_CwTrapSctMajorVersion_Object = MibScalar
cwTrapSctMajorVersion = _CwTrapSctMajorVersion_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 5, 1, 1, 13),
    _CwTrapSctMajorVersion_Type()
)
cwTrapSctMajorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwTrapSctMajorVersion.setStatus("current")


class _CwTrapVarLength_Type(Unsigned32):
    """Custom type cwTrapVarLength based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_CwTrapVarLength_Type.__name__ = "Unsigned32"
_CwTrapVarLength_Object = MibScalar
cwTrapVarLength = _CwTrapVarLength_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 5, 1, 1, 14),
    _CwTrapVarLength_Type()
)
cwTrapVarLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwTrapVarLength.setStatus("current")


class _CwTrapAtmAddressType_Type(Integer32):
    """Custom type cwTrapAtmAddressType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              8)
        )
    )
    namedValues = NamedValues(
        *(("e164", 3),
          ("nsap", 8))
    )


_CwTrapAtmAddressType_Type.__name__ = "Integer32"
_CwTrapAtmAddressType_Object = MibScalar
cwTrapAtmAddressType = _CwTrapAtmAddressType_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 5, 1, 1, 15),
    _CwTrapAtmAddressType_Type()
)
cwTrapAtmAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwTrapAtmAddressType.setStatus("current")


class _CwTrapReference_Type(Integer32):
    """Custom type cwTrapReference based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CwTrapReference_Type.__name__ = "Integer32"
_CwTrapReference_Object = MibScalar
cwTrapReference = _CwTrapReference_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 5, 1, 1, 16),
    _CwTrapReference_Type()
)
cwTrapReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwTrapReference.setStatus("current")


class _CwTrapSecondIndex_Type(Integer32):
    """Custom type cwTrapSecondIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwTrapSecondIndex_Type.__name__ = "Integer32"
_CwTrapSecondIndex_Object = MibScalar
cwTrapSecondIndex = _CwTrapSecondIndex_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 5, 1, 1, 17),
    _CwTrapSecondIndex_Type()
)
cwTrapSecondIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwTrapSecondIndex.setStatus("current")


class _CwTrapThirdIndex_Type(Integer32):
    """Custom type cwTrapThirdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwTrapThirdIndex_Type.__name__ = "Integer32"
_CwTrapThirdIndex_Object = MibScalar
cwTrapThirdIndex = _CwTrapThirdIndex_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 5, 1, 1, 18),
    _CwTrapThirdIndex_Type()
)
cwTrapThirdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwTrapThirdIndex.setStatus("current")
_CwTrapVarsMIBConformance_ObjectIdentity = ObjectIdentity
cwTrapVarsMIBConformance = _CwTrapVarsMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 5, 2)
)
_CwTrapVarsMIBCompliances_ObjectIdentity = ObjectIdentity
cwTrapVarsMIBCompliances = _CwTrapVarsMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 5, 2, 1)
)
_CwTrapVarsMIBGroups_ObjectIdentity = ObjectIdentity
cwTrapVarsMIBGroups = _CwTrapVarsMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 5, 2, 2)
)

# Managed Objects groups

cwTrapVarsTrapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 5, 2, 2, 1)
)
cwTrapVarsTrapGroup.setObjects(
      *(("CISCO-WAN-TRAP-VARS-MIB", "cwTrapIndex"),
        ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapSlotNumber"),
        ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapPhysicalVendorType"),
        ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapLineModuleNumber"),
        ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapOctetString"))
)
if mibBuilder.loadTexts:
    cwTrapVarsTrapGroup.setStatus("deprecated")

cwTrapVarsTrapGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 5, 2, 2, 2)
)
cwTrapVarsTrapGroup2.setObjects(
      *(("CISCO-WAN-TRAP-VARS-MIB", "cwTrapIndex"),
        ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapSlotNumber"),
        ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapPhysicalVendorType"),
        ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapLineModuleNumber"),
        ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapOctetString"),
        ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapDisplayString"))
)
if mibBuilder.loadTexts:
    cwTrapVarsTrapGroup2.setStatus("deprecated")

cwTrapVarsTrapGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 5, 2, 2, 3)
)
cwTrapVarsTrapGroup3.setObjects(
      *(("CISCO-WAN-TRAP-VARS-MIB", "cwTrapIndex"),
        ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapSlotNumber"),
        ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapPhysicalVendorType"),
        ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapLineModuleNumber"),
        ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapOctetString"),
        ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapDisplayString"),
        ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapPhysicalContainer"),
        ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapPhysicalUnit"))
)
if mibBuilder.loadTexts:
    cwTrapVarsTrapGroup3.setStatus("deprecated")

cwTrapVarsTrapGroup4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 5, 2, 2, 4)
)
cwTrapVarsTrapGroup4.setObjects(
      *(("CISCO-WAN-TRAP-VARS-MIB", "cwTrapIndex"),
        ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapSlotNumber"),
        ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapPhysicalVendorType"),
        ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapLineModuleNumber"),
        ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapOctetString"),
        ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapDisplayString"),
        ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapPhysicalContainer"),
        ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapPhysicalUnit"),
        ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapCardRole"),
        ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapSctCardType"),
        ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapSctType"),
        ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapSctId"),
        ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapSctMajorVersion"))
)
if mibBuilder.loadTexts:
    cwTrapVarsTrapGroup4.setStatus("deprecated")

cwTrapVarsTrapGroup5 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 5, 2, 2, 5)
)
cwTrapVarsTrapGroup5.setObjects(
      *(("CISCO-WAN-TRAP-VARS-MIB", "cwTrapIndex"),
        ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapSlotNumber"),
        ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapPhysicalVendorType"),
        ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapLineModuleNumber"),
        ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapOctetString"),
        ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapDisplayString"),
        ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapPhysicalContainer"),
        ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapPhysicalUnit"),
        ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapCardRole"),
        ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapSctCardType"),
        ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapSctType"),
        ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapSctId"),
        ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapSctMajorVersion"),
        ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapVarLength"),
        ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapAtmAddressType"),
        ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapReference"),
        ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapSecondIndex"),
        ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapThirdIndex"))
)
if mibBuilder.loadTexts:
    cwTrapVarsTrapGroup5.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cwTrapVarsCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 351, 150, 5, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cwTrapVarsCompliance.setStatus(
        "deprecated"
    )

cwTrapVarsCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 351, 150, 5, 2, 1, 2)
)
if mibBuilder.loadTexts:
    cwTrapVarsCompliance2.setStatus(
        "deprecated"
    )

cwTrapVarsCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 351, 150, 5, 2, 1, 3)
)
if mibBuilder.loadTexts:
    cwTrapVarsCompliance3.setStatus(
        "deprecated"
    )

cwTrapVarsCompliance4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 351, 150, 5, 2, 1, 4)
)
if mibBuilder.loadTexts:
    cwTrapVarsCompliance4.setStatus(
        "deprecated"
    )

cwTrapVarsCompliance5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 351, 150, 5, 2, 1, 5)
)
if mibBuilder.loadTexts:
    cwTrapVarsCompliance5.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-WAN-TRAP-VARS-MIB",
    **{"ciscoWanTrapVarsMIB": ciscoWanTrapVarsMIB,
       "cwTrapVarMIBObjects": cwTrapVarMIBObjects,
       "cwTrapVars": cwTrapVars,
       "cwTrapIndex": cwTrapIndex,
       "cwTrapSlotNumber": cwTrapSlotNumber,
       "cwTrapPhysicalVendorType": cwTrapPhysicalVendorType,
       "cwTrapLineModuleNumber": cwTrapLineModuleNumber,
       "cwTrapOctetString": cwTrapOctetString,
       "cwTrapDisplayString": cwTrapDisplayString,
       "cwTrapPhysicalContainer": cwTrapPhysicalContainer,
       "cwTrapPhysicalUnit": cwTrapPhysicalUnit,
       "cwTrapCardRole": cwTrapCardRole,
       "cwTrapSctCardType": cwTrapSctCardType,
       "cwTrapSctType": cwTrapSctType,
       "cwTrapSctId": cwTrapSctId,
       "cwTrapSctMajorVersion": cwTrapSctMajorVersion,
       "cwTrapVarLength": cwTrapVarLength,
       "cwTrapAtmAddressType": cwTrapAtmAddressType,
       "cwTrapReference": cwTrapReference,
       "cwTrapSecondIndex": cwTrapSecondIndex,
       "cwTrapThirdIndex": cwTrapThirdIndex,
       "cwTrapVarsMIBConformance": cwTrapVarsMIBConformance,
       "cwTrapVarsMIBCompliances": cwTrapVarsMIBCompliances,
       "cwTrapVarsCompliance": cwTrapVarsCompliance,
       "cwTrapVarsCompliance2": cwTrapVarsCompliance2,
       "cwTrapVarsCompliance3": cwTrapVarsCompliance3,
       "cwTrapVarsCompliance4": cwTrapVarsCompliance4,
       "cwTrapVarsCompliance5": cwTrapVarsCompliance5,
       "cwTrapVarsMIBGroups": cwTrapVarsMIBGroups,
       "cwTrapVarsTrapGroup": cwTrapVarsTrapGroup,
       "cwTrapVarsTrapGroup2": cwTrapVarsTrapGroup2,
       "cwTrapVarsTrapGroup3": cwTrapVarsTrapGroup3,
       "cwTrapVarsTrapGroup4": cwTrapVarsTrapGroup4,
       "cwTrapVarsTrapGroup5": cwTrapVarsTrapGroup5}
)
