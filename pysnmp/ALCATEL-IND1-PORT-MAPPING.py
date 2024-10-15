# SNMP MIB module (ALCATEL-IND1-PORT-MAPPING) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALCATEL-IND1-PORT-MAPPING
# Produced by pysmi-1.5.4 at Mon Oct 14 20:36:48 2024
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

(softentIND1PortMapping,) = mibBuilder.importSymbols(
    "ALCATEL-IND1-BASE",
    "softentIND1PortMapping")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

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

alcatelIND1PortMappingMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 33, 1)
)
alcatelIND1PortMappingMIB.setRevisions(
        ("2007-04-03 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AlcatelIND1PortMappingMIBObjects_ObjectIdentity = ObjectIdentity
alcatelIND1PortMappingMIBObjects = _AlcatelIND1PortMappingMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 33, 1, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1PortMappingMIBObjects.setStatus("current")
_PortMapping_ObjectIdentity = ObjectIdentity
portMapping = _PortMapping_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 33, 1, 1, 1)
)
_PortMappingSessionTable_Object = MibTable
portMappingSessionTable = _PortMappingSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 33, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    portMappingSessionTable.setStatus("current")
_PmapSessionEntry_Object = MibTableRow
pmapSessionEntry = _PmapSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 33, 1, 1, 1, 1, 1)
)
pmapSessionEntry.setIndexNames(
    (0, "ALCATEL-IND1-PORT-MAPPING", "pmapSessionNumber"),
)
if mibBuilder.loadTexts:
    pmapSessionEntry.setStatus("current")


class _PmapSessionNumber_Type(Integer32):
    """Custom type pmapSessionNumber based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PmapSessionNumber_Type.__name__ = "Integer32"
_PmapSessionNumber_Object = MibTableColumn
pmapSessionNumber = _PmapSessionNumber_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 33, 1, 1, 1, 1, 1, 1),
    _PmapSessionNumber_Type()
)
pmapSessionNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pmapSessionNumber.setStatus("current")


class _PmapSessionStatus_Type(Integer32):
    """Custom type pmapSessionStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_PmapSessionStatus_Type.__name__ = "Integer32"
_PmapSessionStatus_Object = MibTableColumn
pmapSessionStatus = _PmapSessionStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 33, 1, 1, 1, 1, 1, 2),
    _PmapSessionStatus_Type()
)
pmapSessionStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmapSessionStatus.setStatus("current")


class _PmapSessionDirection_Type(Integer32):
    """Custom type pmapSessionDirection based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bi", 2),
          ("uni", 1))
    )


_PmapSessionDirection_Type.__name__ = "Integer32"
_PmapSessionDirection_Object = MibTableColumn
pmapSessionDirection = _PmapSessionDirection_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 33, 1, 1, 1, 1, 1, 3),
    _PmapSessionDirection_Type()
)
pmapSessionDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmapSessionDirection.setStatus("current")
_PmapSessionRowStatus_Type = RowStatus
_PmapSessionRowStatus_Object = MibTableColumn
pmapSessionRowStatus = _PmapSessionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 33, 1, 1, 1, 1, 1, 4),
    _PmapSessionRowStatus_Type()
)
pmapSessionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmapSessionRowStatus.setStatus("current")


class _PmapSessionUnknownUnicastFloodStatus_Type(Integer32):
    """Custom type pmapSessionUnknownUnicastFloodStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_PmapSessionUnknownUnicastFloodStatus_Type.__name__ = "Integer32"
_PmapSessionUnknownUnicastFloodStatus_Object = MibTableColumn
pmapSessionUnknownUnicastFloodStatus = _PmapSessionUnknownUnicastFloodStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 33, 1, 1, 1, 1, 1, 5),
    _PmapSessionUnknownUnicastFloodStatus_Type()
)
pmapSessionUnknownUnicastFloodStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmapSessionUnknownUnicastFloodStatus.setStatus("current")
_PortMappingTable_Object = MibTable
portMappingTable = _PortMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 33, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    portMappingTable.setStatus("current")
_PmapEntry_Object = MibTableRow
pmapEntry = _PmapEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 33, 1, 1, 1, 2, 1)
)
pmapEntry.setIndexNames(
    (0, "ALCATEL-IND1-PORT-MAPPING", "pmapSessionNumber"),
    (0, "ALCATEL-IND1-PORT-MAPPING", "pmapPortIfIndex"),
)
if mibBuilder.loadTexts:
    pmapEntry.setStatus("current")


class _PmapPortIfIndex_Type(InterfaceIndexOrZero):
    """Custom type pmapPortIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_PmapPortIfIndex_Object = MibTableColumn
pmapPortIfIndex = _PmapPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 33, 1, 1, 1, 2, 1, 1),
    _PmapPortIfIndex_Type()
)
pmapPortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pmapPortIfIndex.setStatus("current")


class _PmapPortType_Type(Integer32):
    """Custom type pmapPortType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("network", 2),
          ("user", 1))
    )


_PmapPortType_Type.__name__ = "Integer32"
_PmapPortType_Object = MibTableColumn
pmapPortType = _PmapPortType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 33, 1, 1, 1, 2, 1, 2),
    _PmapPortType_Type()
)
pmapPortType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmapPortType.setStatus("current")
_PmapRowStatus_Type = RowStatus
_PmapRowStatus_Object = MibTableColumn
pmapRowStatus = _PmapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 33, 1, 1, 1, 2, 1, 3),
    _PmapRowStatus_Type()
)
pmapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmapRowStatus.setStatus("current")
_PmapConformance_ObjectIdentity = ObjectIdentity
pmapConformance = _PmapConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 33, 1, 2)
)
_PmapGroups_ObjectIdentity = ObjectIdentity
pmapGroups = _PmapGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 33, 1, 2, 1)
)
_PmapCompliances_ObjectIdentity = ObjectIdentity
pmapCompliances = _PmapCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 33, 1, 2, 2)
)

# Managed Objects groups

pmapSessionTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 33, 1, 2, 1, 1)
)
pmapSessionTableGroup.setObjects(
      *(("ALCATEL-IND1-PORT-MAPPING", "pmapSessionStatus"),
        ("ALCATEL-IND1-PORT-MAPPING", "pmapSessionDirection"),
        ("ALCATEL-IND1-PORT-MAPPING", "pmapSessionRowStatus"),
        ("ALCATEL-IND1-PORT-MAPPING", "pmapSessionUnknownUnicastFloodStatus"))
)
if mibBuilder.loadTexts:
    pmapSessionTableGroup.setStatus("current")

pmapTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 33, 1, 2, 1, 2)
)
pmapTableGroup.setObjects(
      *(("ALCATEL-IND1-PORT-MAPPING", "pmapPortType"),
        ("ALCATEL-IND1-PORT-MAPPING", "pmapRowStatus"))
)
if mibBuilder.loadTexts:
    pmapTableGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

pmapCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 33, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    pmapCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-PORT-MAPPING",
    **{"alcatelIND1PortMappingMIB": alcatelIND1PortMappingMIB,
       "alcatelIND1PortMappingMIBObjects": alcatelIND1PortMappingMIBObjects,
       "portMapping": portMapping,
       "portMappingSessionTable": portMappingSessionTable,
       "pmapSessionEntry": pmapSessionEntry,
       "pmapSessionNumber": pmapSessionNumber,
       "pmapSessionStatus": pmapSessionStatus,
       "pmapSessionDirection": pmapSessionDirection,
       "pmapSessionRowStatus": pmapSessionRowStatus,
       "pmapSessionUnknownUnicastFloodStatus": pmapSessionUnknownUnicastFloodStatus,
       "portMappingTable": portMappingTable,
       "pmapEntry": pmapEntry,
       "pmapPortIfIndex": pmapPortIfIndex,
       "pmapPortType": pmapPortType,
       "pmapRowStatus": pmapRowStatus,
       "pmapConformance": pmapConformance,
       "pmapGroups": pmapGroups,
       "pmapSessionTableGroup": pmapSessionTableGroup,
       "pmapTableGroup": pmapTableGroup,
       "pmapCompliances": pmapCompliances,
       "pmapCompliance": pmapCompliance}
)
