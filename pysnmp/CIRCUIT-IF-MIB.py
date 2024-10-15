# SNMP MIB module (CIRCUIT-IF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CIRCUIT-IF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:55:17 2024
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

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 RowPointer,
 RowStatus,
 StorageType,
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowPointer",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

circuitIfMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 94)
)
circuitIfMIB.setRevisions(
        ("2002-01-03 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CiFlowDirection(Integer32, TextualConvention):
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
        *(("both", 3),
          ("receive", 2),
          ("transmit", 1))
    )



# MIB Managed Objects in the order of their OIDs

_CiObjects_ObjectIdentity = ObjectIdentity
ciObjects = _CiObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 94, 1)
)
_CiCircuitTable_Object = MibTable
ciCircuitTable = _CiCircuitTable_Object(
    (1, 3, 6, 1, 2, 1, 94, 1, 1)
)
if mibBuilder.loadTexts:
    ciCircuitTable.setStatus("current")
_CiCircuitEntry_Object = MibTableRow
ciCircuitEntry = _CiCircuitEntry_Object(
    (1, 3, 6, 1, 2, 1, 94, 1, 1, 1)
)
ciCircuitEntry.setIndexNames(
    (0, "CIRCUIT-IF-MIB", "ciCircuitObject"),
    (0, "CIRCUIT-IF-MIB", "ciCircuitFlow"),
)
if mibBuilder.loadTexts:
    ciCircuitEntry.setStatus("current")
_CiCircuitObject_Type = RowPointer
_CiCircuitObject_Object = MibTableColumn
ciCircuitObject = _CiCircuitObject_Object(
    (1, 3, 6, 1, 2, 1, 94, 1, 1, 1, 1),
    _CiCircuitObject_Type()
)
ciCircuitObject.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciCircuitObject.setStatus("current")
_CiCircuitFlow_Type = CiFlowDirection
_CiCircuitFlow_Object = MibTableColumn
ciCircuitFlow = _CiCircuitFlow_Object(
    (1, 3, 6, 1, 2, 1, 94, 1, 1, 1, 2),
    _CiCircuitFlow_Type()
)
ciCircuitFlow.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciCircuitFlow.setStatus("current")
_CiCircuitStatus_Type = RowStatus
_CiCircuitStatus_Object = MibTableColumn
ciCircuitStatus = _CiCircuitStatus_Object(
    (1, 3, 6, 1, 2, 1, 94, 1, 1, 1, 3),
    _CiCircuitStatus_Type()
)
ciCircuitStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciCircuitStatus.setStatus("current")
_CiCircuitIfIndex_Type = InterfaceIndex
_CiCircuitIfIndex_Object = MibTableColumn
ciCircuitIfIndex = _CiCircuitIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 94, 1, 1, 1, 4),
    _CiCircuitIfIndex_Type()
)
ciCircuitIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciCircuitIfIndex.setStatus("current")
_CiCircuitCreateTime_Type = TimeStamp
_CiCircuitCreateTime_Object = MibTableColumn
ciCircuitCreateTime = _CiCircuitCreateTime_Object(
    (1, 3, 6, 1, 2, 1, 94, 1, 1, 1, 5),
    _CiCircuitCreateTime_Type()
)
ciCircuitCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciCircuitCreateTime.setStatus("current")
_CiCircuitStorageType_Type = StorageType
_CiCircuitStorageType_Object = MibTableColumn
ciCircuitStorageType = _CiCircuitStorageType_Object(
    (1, 3, 6, 1, 2, 1, 94, 1, 1, 1, 6),
    _CiCircuitStorageType_Type()
)
ciCircuitStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciCircuitStorageType.setStatus("current")
_CiIfMapTable_Object = MibTable
ciIfMapTable = _CiIfMapTable_Object(
    (1, 3, 6, 1, 2, 1, 94, 1, 2)
)
if mibBuilder.loadTexts:
    ciIfMapTable.setStatus("current")
_CiIfMapEntry_Object = MibTableRow
ciIfMapEntry = _CiIfMapEntry_Object(
    (1, 3, 6, 1, 2, 1, 94, 1, 2, 1)
)
ciIfMapEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ciIfMapEntry.setStatus("current")
_CiIfMapObject_Type = RowPointer
_CiIfMapObject_Object = MibTableColumn
ciIfMapObject = _CiIfMapObject_Object(
    (1, 3, 6, 1, 2, 1, 94, 1, 2, 1, 1),
    _CiIfMapObject_Type()
)
ciIfMapObject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciIfMapObject.setStatus("current")
_CiIfMapFlow_Type = CiFlowDirection
_CiIfMapFlow_Object = MibTableColumn
ciIfMapFlow = _CiIfMapFlow_Object(
    (1, 3, 6, 1, 2, 1, 94, 1, 2, 1, 2),
    _CiIfMapFlow_Type()
)
ciIfMapFlow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciIfMapFlow.setStatus("current")
_CiIfLastChange_Type = TimeStamp
_CiIfLastChange_Object = MibScalar
ciIfLastChange = _CiIfLastChange_Object(
    (1, 3, 6, 1, 2, 1, 94, 1, 3),
    _CiIfLastChange_Type()
)
ciIfLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciIfLastChange.setStatus("current")
_CiIfNumActive_Type = Gauge32
_CiIfNumActive_Object = MibScalar
ciIfNumActive = _CiIfNumActive_Object(
    (1, 3, 6, 1, 2, 1, 94, 1, 4),
    _CiIfNumActive_Type()
)
ciIfNumActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciIfNumActive.setStatus("current")
_CiCapabilities_ObjectIdentity = ObjectIdentity
ciCapabilities = _CiCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 94, 2)
)
_CiConformance_ObjectIdentity = ObjectIdentity
ciConformance = _CiConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 94, 3)
)
_CiMIBGroups_ObjectIdentity = ObjectIdentity
ciMIBGroups = _CiMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 94, 3, 1)
)
_CiMIBCompliances_ObjectIdentity = ObjectIdentity
ciMIBCompliances = _CiMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 94, 3, 2)
)

# Managed Objects groups

ciCircuitGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 94, 3, 1, 1)
)
ciCircuitGroup.setObjects(
      *(("CIRCUIT-IF-MIB", "ciCircuitStatus"),
        ("CIRCUIT-IF-MIB", "ciCircuitIfIndex"),
        ("CIRCUIT-IF-MIB", "ciCircuitCreateTime"),
        ("CIRCUIT-IF-MIB", "ciCircuitStorageType"))
)
if mibBuilder.loadTexts:
    ciCircuitGroup.setStatus("current")

ciIfMapGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 94, 3, 1, 2)
)
ciIfMapGroup.setObjects(
      *(("CIRCUIT-IF-MIB", "ciIfMapObject"),
        ("CIRCUIT-IF-MIB", "ciIfMapFlow"))
)
if mibBuilder.loadTexts:
    ciIfMapGroup.setStatus("current")

ciStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 94, 3, 1, 3)
)
ciStatsGroup.setObjects(
      *(("CIRCUIT-IF-MIB", "ciIfLastChange"),
        ("CIRCUIT-IF-MIB", "ciIfNumActive"))
)
if mibBuilder.loadTexts:
    ciStatsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 94, 3, 2, 1)
)
if mibBuilder.loadTexts:
    ciCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CIRCUIT-IF-MIB",
    **{"CiFlowDirection": CiFlowDirection,
       "circuitIfMIB": circuitIfMIB,
       "ciObjects": ciObjects,
       "ciCircuitTable": ciCircuitTable,
       "ciCircuitEntry": ciCircuitEntry,
       "ciCircuitObject": ciCircuitObject,
       "ciCircuitFlow": ciCircuitFlow,
       "ciCircuitStatus": ciCircuitStatus,
       "ciCircuitIfIndex": ciCircuitIfIndex,
       "ciCircuitCreateTime": ciCircuitCreateTime,
       "ciCircuitStorageType": ciCircuitStorageType,
       "ciIfMapTable": ciIfMapTable,
       "ciIfMapEntry": ciIfMapEntry,
       "ciIfMapObject": ciIfMapObject,
       "ciIfMapFlow": ciIfMapFlow,
       "ciIfLastChange": ciIfLastChange,
       "ciIfNumActive": ciIfNumActive,
       "ciCapabilities": ciCapabilities,
       "ciConformance": ciConformance,
       "ciMIBGroups": ciMIBGroups,
       "ciCircuitGroup": ciCircuitGroup,
       "ciIfMapGroup": ciIfMapGroup,
       "ciStatsGroup": ciStatsGroup,
       "ciMIBCompliances": ciMIBCompliances,
       "ciCompliance": ciCompliance}
)
