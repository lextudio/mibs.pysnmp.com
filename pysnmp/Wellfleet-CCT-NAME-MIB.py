# SNMP MIB module (Wellfleet-CCT-NAME-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-CCT-NAME-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:15:55 2024
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

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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

(wfCircuitNameExtension,
 wfServices) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfCircuitNameExtension",
    "wfServices")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfCircuitNameTable_Object = MibTable
wfCircuitNameTable = _WfCircuitNameTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 3)
)
if mibBuilder.loadTexts:
    wfCircuitNameTable.setStatus("mandatory")
_WfCircuitNameEntry_Object = MibTableRow
wfCircuitNameEntry = _WfCircuitNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 3, 1)
)
wfCircuitNameEntry.setIndexNames(
    (0, "Wellfleet-CCT-NAME-MIB", "wfCircuitNumber"),
)
if mibBuilder.loadTexts:
    wfCircuitNameEntry.setStatus("mandatory")


class _WfCircuitNameDelete_Type(Integer32):
    """Custom type wfCircuitNameDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("delete", 2))
    )


_WfCircuitNameDelete_Type.__name__ = "Integer32"
_WfCircuitNameDelete_Object = MibTableColumn
wfCircuitNameDelete = _WfCircuitNameDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 3, 1, 1),
    _WfCircuitNameDelete_Type()
)
wfCircuitNameDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCircuitNameDelete.setStatus("mandatory")
_WfCircuitNumber_Type = Integer32
_WfCircuitNumber_Object = MibTableColumn
wfCircuitNumber = _WfCircuitNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 3, 1, 2),
    _WfCircuitNumber_Type()
)
wfCircuitNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCircuitNumber.setStatus("mandatory")
_WfCircuitName_Type = DisplayString
_WfCircuitName_Object = MibTableColumn
wfCircuitName = _WfCircuitName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 3, 1, 3),
    _WfCircuitName_Type()
)
wfCircuitName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCircuitName.setStatus("mandatory")


class _WfCircuitIfType_Type(Integer32):
    """Custom type wfCircuitIfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(10,
              20,
              30,
              40,
              50,
              60,
              70,
              80,
              90,
              100,
              110,
              120,
              130,
              140,
              150,
              160,
              170)
        )
    )
    namedValues = NamedValues(
        *(("async", 120),
          ("atm", 110),
          ("atmz", 140),
          ("bisync", 150),
          ("csmacd", 10),
          ("ds1e1", 90),
          ("ds3e3", 170),
          ("e1", 40),
          ("fddi", 60),
          ("gre", 160),
          ("hssi", 70),
          ("isdn", 130),
          ("mct1", 80),
          ("none", 100),
          ("sync", 20),
          ("t1", 30),
          ("token", 50))
    )


_WfCircuitIfType_Type.__name__ = "Integer32"
_WfCircuitIfType_Object = MibTableColumn
wfCircuitIfType = _WfCircuitIfType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 3, 1, 4),
    _WfCircuitIfType_Type()
)
wfCircuitIfType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCircuitIfType.setStatus("mandatory")
_WfCircuitProtoMap_Type = OctetString
_WfCircuitProtoMap_Object = MibTableColumn
wfCircuitProtoMap = _WfCircuitProtoMap_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 3, 1, 5),
    _WfCircuitProtoMap_Type()
)
wfCircuitProtoMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCircuitProtoMap.setStatus("mandatory")


class _WfCircuitType_Type(Integer32):
    """Custom type wfCircuitType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("clip", 4),
          ("gre", 6),
          ("internal", 5),
          ("master", 3),
          ("normal", 1),
          ("notrouted", 7),
          ("virtual", 2))
    )


_WfCircuitType_Type.__name__ = "Integer32"
_WfCircuitType_Object = MibTableColumn
wfCircuitType = _WfCircuitType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 3, 1, 6),
    _WfCircuitType_Type()
)
wfCircuitType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCircuitType.setStatus("mandatory")
_WfCircuitRelCctList_Type = OctetString
_WfCircuitRelCctList_Object = MibTableColumn
wfCircuitRelCctList = _WfCircuitRelCctList_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 3, 1, 7),
    _WfCircuitRelCctList_Type()
)
wfCircuitRelCctList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCircuitRelCctList.setStatus("mandatory")
_WfCircuitLineList_Type = OctetString
_WfCircuitLineList_Object = MibTableColumn
wfCircuitLineList = _WfCircuitLineList_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 3, 1, 8),
    _WfCircuitLineList_Type()
)
wfCircuitLineList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCircuitLineList.setStatus("mandatory")
_WfCircuitMultilineName_Type = DisplayString
_WfCircuitMultilineName_Object = MibTableColumn
wfCircuitMultilineName = _WfCircuitMultilineName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 3, 1, 9),
    _WfCircuitMultilineName_Type()
)
wfCircuitMultilineName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCircuitMultilineName.setStatus("mandatory")


class _WfCircuitTdmRes_Type(Integer32):
    """Custom type wfCircuitTdmRes based on Integer32"""
    defaultValue = 1

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
        *(("cesh110", 4),
          ("notdmresources", 1),
          ("routedh110", 3),
          ("switchedh110", 2))
    )


_WfCircuitTdmRes_Type.__name__ = "Integer32"
_WfCircuitTdmRes_Object = MibTableColumn
wfCircuitTdmRes = _WfCircuitTdmRes_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 3, 1, 10),
    _WfCircuitTdmRes_Type()
)
wfCircuitTdmRes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCircuitTdmRes.setStatus("mandatory")


class _WfCircuitTdmCctInUse_Type(Integer32):
    """Custom type wfCircuitTdmCctInUse based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inuse", 2),
          ("notinuse", 1))
    )


_WfCircuitTdmCctInUse_Type.__name__ = "Integer32"
_WfCircuitTdmCctInUse_Object = MibTableColumn
wfCircuitTdmCctInUse = _WfCircuitTdmCctInUse_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 3, 1, 11),
    _WfCircuitTdmCctInUse_Type()
)
wfCircuitTdmCctInUse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCircuitTdmCctInUse.setStatus("mandatory")
_WfLineMappingTable_Object = MibTable
wfLineMappingTable = _WfLineMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 9, 1)
)
if mibBuilder.loadTexts:
    wfLineMappingTable.setStatus("mandatory")
_WfLineMappingEntry_Object = MibTableRow
wfLineMappingEntry = _WfLineMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 9, 1, 1)
)
wfLineMappingEntry.setIndexNames(
    (0, "Wellfleet-CCT-NAME-MIB", "wfLineMappingNumber"),
)
if mibBuilder.loadTexts:
    wfLineMappingEntry.setStatus("mandatory")


class _WfLineMappingDelete_Type(Integer32):
    """Custom type wfLineMappingDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfLineMappingDelete_Type.__name__ = "Integer32"
_WfLineMappingDelete_Object = MibTableColumn
wfLineMappingDelete = _WfLineMappingDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 9, 1, 1, 1),
    _WfLineMappingDelete_Type()
)
wfLineMappingDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLineMappingDelete.setStatus("mandatory")
_WfLineMappingNumber_Type = Integer32
_WfLineMappingNumber_Object = MibTableColumn
wfLineMappingNumber = _WfLineMappingNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 9, 1, 1, 2),
    _WfLineMappingNumber_Type()
)
wfLineMappingNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLineMappingNumber.setStatus("mandatory")
_WfLineMappingCct_Type = Integer32
_WfLineMappingCct_Object = MibTableColumn
wfLineMappingCct = _WfLineMappingCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 9, 1, 1, 3),
    _WfLineMappingCct_Type()
)
wfLineMappingCct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLineMappingCct.setStatus("mandatory")
_WfLineMappingDef_Type = OctetString
_WfLineMappingDef_Object = MibTableColumn
wfLineMappingDef = _WfLineMappingDef_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 9, 1, 1, 4),
    _WfLineMappingDef_Type()
)
wfLineMappingDef.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLineMappingDef.setStatus("mandatory")
_WfNode_ObjectIdentity = ObjectIdentity
wfNode = _WfNode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 9, 2)
)


class _WfNodeDelete_Type(Integer32):
    """Custom type wfNodeDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfNodeDelete_Type.__name__ = "Integer32"
_WfNodeDelete_Object = MibScalar
wfNodeDelete = _WfNodeDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 9, 2, 1),
    _WfNodeDelete_Type()
)
wfNodeDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNodeDelete.setStatus("mandatory")
_WfNodeProtoMap_Type = OctetString
_WfNodeProtoMap_Object = MibScalar
wfNodeProtoMap = _WfNodeProtoMap_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 9, 2, 2),
    _WfNodeProtoMap_Type()
)
wfNodeProtoMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNodeProtoMap.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-CCT-NAME-MIB",
    **{"wfCircuitNameTable": wfCircuitNameTable,
       "wfCircuitNameEntry": wfCircuitNameEntry,
       "wfCircuitNameDelete": wfCircuitNameDelete,
       "wfCircuitNumber": wfCircuitNumber,
       "wfCircuitName": wfCircuitName,
       "wfCircuitIfType": wfCircuitIfType,
       "wfCircuitProtoMap": wfCircuitProtoMap,
       "wfCircuitType": wfCircuitType,
       "wfCircuitRelCctList": wfCircuitRelCctList,
       "wfCircuitLineList": wfCircuitLineList,
       "wfCircuitMultilineName": wfCircuitMultilineName,
       "wfCircuitTdmRes": wfCircuitTdmRes,
       "wfCircuitTdmCctInUse": wfCircuitTdmCctInUse,
       "wfLineMappingTable": wfLineMappingTable,
       "wfLineMappingEntry": wfLineMappingEntry,
       "wfLineMappingDelete": wfLineMappingDelete,
       "wfLineMappingNumber": wfLineMappingNumber,
       "wfLineMappingCct": wfLineMappingCct,
       "wfLineMappingDef": wfLineMappingDef,
       "wfNode": wfNode,
       "wfNodeDelete": wfNodeDelete,
       "wfNodeProtoMap": wfNodeProtoMap}
)
