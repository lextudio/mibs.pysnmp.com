# SNMP MIB module (CISCO-ZS-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-ZS-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:13:51 2024
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

(vsanIndex,) = mibBuilder.importSymbols(
    "CISCO-VSAN-MIB",
    "vsanIndex")

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

ciscoZsExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 427)
)
ciscoZsExtMIB.setRevisions(
        ("2006-01-03 00:00",
         "2004-08-11 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CzseSessOwnerType(Integer32, TextualConvention):
    status = "current"
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
        *(("cli", 2),
          ("gs4client", 3),
          ("other", 1),
          ("snmp", 4))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoZsExtMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoZsExtMIBNotifs = _CiscoZsExtMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 427, 0)
)
_CiscoZsExtMIBObjects_ObjectIdentity = ObjectIdentity
ciscoZsExtMIBObjects = _CiscoZsExtMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 427, 1)
)
_CzseConfiguration_ObjectIdentity = ObjectIdentity
czseConfiguration = _CzseConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 427, 1, 1)
)
_CzseCapabilityTable_Object = MibTable
czseCapabilityTable = _CzseCapabilityTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 427, 1, 1, 1)
)
if mibBuilder.loadTexts:
    czseCapabilityTable.setStatus("current")
_CzseCapabilityEntry_Object = MibTableRow
czseCapabilityEntry = _CzseCapabilityEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 427, 1, 1, 1, 1)
)
czseCapabilityEntry.setIndexNames(
    (0, "CISCO-VSAN-MIB", "vsanIndex"),
)
if mibBuilder.loadTexts:
    czseCapabilityEntry.setStatus("current")


class _CzseCapabilityObject_Type(Bits):
    """Custom type czseCapabilityObject based on Bits"""
    namedValues = NamedValues(
        *(("dirAct", 2),
          ("enhancedMode", 0),
          ("hardZoning", 3),
          ("zsetDb", 1))
    )

_CzseCapabilityObject_Type.__name__ = "Bits"
_CzseCapabilityObject_Object = MibTableColumn
czseCapabilityObject = _CzseCapabilityObject_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 427, 1, 1, 1, 1, 1),
    _CzseCapabilityObject_Type()
)
czseCapabilityObject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    czseCapabilityObject.setStatus("current")
_CzseModeTable_Object = MibTable
czseModeTable = _CzseModeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 427, 1, 1, 2)
)
if mibBuilder.loadTexts:
    czseModeTable.setStatus("current")
_CzseModeEntry_Object = MibTableRow
czseModeEntry = _CzseModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 427, 1, 1, 2, 1)
)
czseModeEntry.setIndexNames(
    (0, "CISCO-VSAN-MIB", "vsanIndex"),
)
if mibBuilder.loadTexts:
    czseModeEntry.setStatus("current")


class _CzseOperationMode_Type(Integer32):
    """Custom type czseOperationMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("basic", 1),
          ("enhanced", 2))
    )


_CzseOperationMode_Type.__name__ = "Integer32"
_CzseOperationMode_Object = MibTableColumn
czseOperationMode = _CzseOperationMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 427, 1, 1, 2, 1, 1),
    _CzseOperationMode_Type()
)
czseOperationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    czseOperationMode.setStatus("current")


class _CzseOperationModeResult_Type(Integer32):
    """Custom type czseOperationModeResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("failure", 2),
          ("inProgress", 3),
          ("success", 1))
    )


_CzseOperationModeResult_Type.__name__ = "Integer32"
_CzseOperationModeResult_Object = MibTableColumn
czseOperationModeResult = _CzseOperationModeResult_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 427, 1, 1, 2, 1, 2),
    _CzseOperationModeResult_Type()
)
czseOperationModeResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    czseOperationModeResult.setStatus("current")


class _CzseReadFrom_Type(Integer32):
    """Custom type czseReadFrom based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("copyDB", 2),
          ("effectiveDB", 1))
    )


_CzseReadFrom_Type.__name__ = "Integer32"
_CzseReadFrom_Object = MibScalar
czseReadFrom = _CzseReadFrom_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 427, 1, 1, 3),
    _CzseReadFrom_Type()
)
czseReadFrom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    czseReadFrom.setStatus("current")
_CzseSessionTable_Object = MibTable
czseSessionTable = _CzseSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 427, 1, 1, 4)
)
if mibBuilder.loadTexts:
    czseSessionTable.setStatus("current")
_CzseSessionEntry_Object = MibTableRow
czseSessionEntry = _CzseSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 427, 1, 1, 4, 1)
)
czseSessionEntry.setIndexNames(
    (0, "CISCO-VSAN-MIB", "vsanIndex"),
)
if mibBuilder.loadTexts:
    czseSessionEntry.setStatus("current")
_CzseSessionOwnerType_Type = CzseSessOwnerType
_CzseSessionOwnerType_Object = MibTableColumn
czseSessionOwnerType = _CzseSessionOwnerType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 427, 1, 1, 4, 1, 1),
    _CzseSessionOwnerType_Type()
)
czseSessionOwnerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    czseSessionOwnerType.setStatus("current")


class _CzseSessionOwner_Type(OctetString):
    """Custom type czseSessionOwner based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CzseSessionOwner_Type.__name__ = "OctetString"
_CzseSessionOwner_Object = MibTableColumn
czseSessionOwner = _CzseSessionOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 427, 1, 1, 4, 1, 2),
    _CzseSessionOwner_Type()
)
czseSessionOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    czseSessionOwner.setStatus("current")


class _CzseSessionCntl_Type(Integer32):
    """Custom type czseSessionCntl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cleanup", 2),
          ("commitChanges", 1),
          ("noop", 3))
    )


_CzseSessionCntl_Type.__name__ = "Integer32"
_CzseSessionCntl_Object = MibTableColumn
czseSessionCntl = _CzseSessionCntl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 427, 1, 1, 4, 1, 3),
    _CzseSessionCntl_Type()
)
czseSessionCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    czseSessionCntl.setStatus("current")


class _CzseSessionCntlResult_Type(Integer32):
    """Custom type czseSessionCntlResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("commitFailure", 2),
          ("commitSuccess", 1),
          ("inProgress", 3))
    )


_CzseSessionCntlResult_Type.__name__ = "Integer32"
_CzseSessionCntlResult_Object = MibTableColumn
czseSessionCntlResult = _CzseSessionCntlResult_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 427, 1, 1, 4, 1, 4),
    _CzseSessionCntlResult_Type()
)
czseSessionCntlResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    czseSessionCntlResult.setStatus("current")
_CzseMergeControlTable_Object = MibTable
czseMergeControlTable = _CzseMergeControlTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 427, 1, 1, 5)
)
if mibBuilder.loadTexts:
    czseMergeControlTable.setStatus("current")
_CzseMergeControlEntry_Object = MibTableRow
czseMergeControlEntry = _CzseMergeControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 427, 1, 1, 5, 1)
)
czseMergeControlEntry.setIndexNames(
    (0, "CISCO-VSAN-MIB", "vsanIndex"),
)
if mibBuilder.loadTexts:
    czseMergeControlEntry.setStatus("current")


class _CzseMergeControlRestrict_Type(Integer32):
    """Custom type czseMergeControlRestrict based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("restrict", 2))
    )


_CzseMergeControlRestrict_Type.__name__ = "Integer32"
_CzseMergeControlRestrict_Object = MibTableColumn
czseMergeControlRestrict = _CzseMergeControlRestrict_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 427, 1, 1, 5, 1, 1),
    _CzseMergeControlRestrict_Type()
)
czseMergeControlRestrict.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    czseMergeControlRestrict.setStatus("current")


class _CzseGlobalDefaultZoneBehaviour_Type(Integer32):
    """Custom type czseGlobalDefaultZoneBehaviour based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 2),
          ("permit", 1))
    )


_CzseGlobalDefaultZoneBehaviour_Type.__name__ = "Integer32"
_CzseGlobalDefaultZoneBehaviour_Object = MibScalar
czseGlobalDefaultZoneBehaviour = _CzseGlobalDefaultZoneBehaviour_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 427, 1, 1, 6),
    _CzseGlobalDefaultZoneBehaviour_Type()
)
czseGlobalDefaultZoneBehaviour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    czseGlobalDefaultZoneBehaviour.setStatus("current")


class _CzseGlobalPropagationMode_Type(Integer32):
    """Custom type czseGlobalPropagationMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("activeZoneset", 2),
          ("fullZoneset", 1))
    )


_CzseGlobalPropagationMode_Type.__name__ = "Integer32"
_CzseGlobalPropagationMode_Object = MibScalar
czseGlobalPropagationMode = _CzseGlobalPropagationMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 427, 1, 1, 7),
    _CzseGlobalPropagationMode_Type()
)
czseGlobalPropagationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    czseGlobalPropagationMode.setStatus("current")
_CzseStats_ObjectIdentity = ObjectIdentity
czseStats = _CzseStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 427, 1, 2)
)
_CiscoZsExtMIBConform_ObjectIdentity = ObjectIdentity
ciscoZsExtMIBConform = _CiscoZsExtMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 427, 2)
)
_CiscoZsExtMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoZsExtMIBCompliances = _CiscoZsExtMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 427, 2, 1)
)
_CiscoZsExtMIBGroups_ObjectIdentity = ObjectIdentity
ciscoZsExtMIBGroups = _CiscoZsExtMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 427, 2, 2)
)

# Managed Objects groups

ciscoZsExtConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 427, 2, 2, 1)
)
ciscoZsExtConfigGroup.setObjects(
      *(("CISCO-ZS-EXT-MIB", "czseCapabilityObject"),
        ("CISCO-ZS-EXT-MIB", "czseOperationMode"),
        ("CISCO-ZS-EXT-MIB", "czseOperationModeResult"),
        ("CISCO-ZS-EXT-MIB", "czseReadFrom"),
        ("CISCO-ZS-EXT-MIB", "czseSessionOwnerType"),
        ("CISCO-ZS-EXT-MIB", "czseSessionOwner"),
        ("CISCO-ZS-EXT-MIB", "czseSessionCntl"),
        ("CISCO-ZS-EXT-MIB", "czseSessionCntlResult"),
        ("CISCO-ZS-EXT-MIB", "czseMergeControlRestrict"))
)
if mibBuilder.loadTexts:
    ciscoZsExtConfigGroup.setStatus("current")

ciscoZsExtConfigGroupSup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 427, 2, 2, 2)
)
ciscoZsExtConfigGroupSup1.setObjects(
      *(("CISCO-ZS-EXT-MIB", "czseGlobalDefaultZoneBehaviour"),
        ("CISCO-ZS-EXT-MIB", "czseGlobalPropagationMode"))
)
if mibBuilder.loadTexts:
    ciscoZsExtConfigGroupSup1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoZsExtMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 427, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoZsExtMIBCompliance.setStatus(
        "deprecated"
    )

ciscoZsExtMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 427, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoZsExtMIBComplianceRev1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-ZS-EXT-MIB",
    **{"CzseSessOwnerType": CzseSessOwnerType,
       "ciscoZsExtMIB": ciscoZsExtMIB,
       "ciscoZsExtMIBNotifs": ciscoZsExtMIBNotifs,
       "ciscoZsExtMIBObjects": ciscoZsExtMIBObjects,
       "czseConfiguration": czseConfiguration,
       "czseCapabilityTable": czseCapabilityTable,
       "czseCapabilityEntry": czseCapabilityEntry,
       "czseCapabilityObject": czseCapabilityObject,
       "czseModeTable": czseModeTable,
       "czseModeEntry": czseModeEntry,
       "czseOperationMode": czseOperationMode,
       "czseOperationModeResult": czseOperationModeResult,
       "czseReadFrom": czseReadFrom,
       "czseSessionTable": czseSessionTable,
       "czseSessionEntry": czseSessionEntry,
       "czseSessionOwnerType": czseSessionOwnerType,
       "czseSessionOwner": czseSessionOwner,
       "czseSessionCntl": czseSessionCntl,
       "czseSessionCntlResult": czseSessionCntlResult,
       "czseMergeControlTable": czseMergeControlTable,
       "czseMergeControlEntry": czseMergeControlEntry,
       "czseMergeControlRestrict": czseMergeControlRestrict,
       "czseGlobalDefaultZoneBehaviour": czseGlobalDefaultZoneBehaviour,
       "czseGlobalPropagationMode": czseGlobalPropagationMode,
       "czseStats": czseStats,
       "ciscoZsExtMIBConform": ciscoZsExtMIBConform,
       "ciscoZsExtMIBCompliances": ciscoZsExtMIBCompliances,
       "ciscoZsExtMIBCompliance": ciscoZsExtMIBCompliance,
       "ciscoZsExtMIBComplianceRev1": ciscoZsExtMIBComplianceRev1,
       "ciscoZsExtMIBGroups": ciscoZsExtMIBGroups,
       "ciscoZsExtConfigGroup": ciscoZsExtConfigGroup,
       "ciscoZsExtConfigGroupSup1": ciscoZsExtConfigGroupSup1}
)
