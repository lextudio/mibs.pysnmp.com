# SNMP MIB module (PDN-CROSSCONNECT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PDN-CROSSCONNECT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:37:25 2024
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

(crossConnect,) = mibBuilder.importSymbols(
    "PDN-HEADER-MIB",
    "crossConnect")

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


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DevDs1FracTable_Object = MibTable
devDs1FracTable = _DevDs1FracTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 7, 1)
)
if mibBuilder.loadTexts:
    devDs1FracTable.setStatus("mandatory")
_DevDs1FracEntry_Object = MibTableRow
devDs1FracEntry = _DevDs1FracEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 7, 1, 1)
)
devDs1FracEntry.setIndexNames(
    (0, "PDN-CROSSCONNECT-MIB", "devDs1FracIndex"),
    (0, "PDN-CROSSCONNECT-MIB", "devDs1FracNumber"),
)
if mibBuilder.loadTexts:
    devDs1FracEntry.setStatus("mandatory")
_DevDs1FracIndex_Type = Integer32
_DevDs1FracIndex_Object = MibTableColumn
devDs1FracIndex = _DevDs1FracIndex_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 7, 1, 1, 1),
    _DevDs1FracIndex_Type()
)
devDs1FracIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devDs1FracIndex.setStatus("mandatory")


class _DevDs1FracNumber_Type(Integer32):
    """Custom type devDs1FracNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_DevDs1FracNumber_Type.__name__ = "Integer32"
_DevDs1FracNumber_Object = MibTableColumn
devDs1FracNumber = _DevDs1FracNumber_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 7, 1, 1, 2),
    _DevDs1FracNumber_Type()
)
devDs1FracNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devDs1FracNumber.setStatus("mandatory")
_DevDs1FracIfIndex_Type = Integer32
_DevDs1FracIfIndex_Object = MibTableColumn
devDs1FracIfIndex = _DevDs1FracIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 7, 1, 1, 3),
    _DevDs1FracIfIndex_Type()
)
devDs1FracIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devDs1FracIfIndex.setStatus("mandatory")


class _DevDs1FracIfFracNumber_Type(Integer32):
    """Custom type devDs1FracIfFracNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_DevDs1FracIfFracNumber_Type.__name__ = "Integer32"
_DevDs1FracIfFracNumber_Object = MibTableColumn
devDs1FracIfFracNumber = _DevDs1FracIfFracNumber_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 7, 1, 1, 4),
    _DevDs1FracIfFracNumber_Type()
)
devDs1FracIfFracNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devDs1FracIfFracNumber.setStatus("mandatory")
_DevSyncDataPortAssignTable_Object = MibTable
devSyncDataPortAssignTable = _DevSyncDataPortAssignTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 7, 2)
)
if mibBuilder.loadTexts:
    devSyncDataPortAssignTable.setStatus("mandatory")
_DevSyncDataPortAssignEntry_Object = MibTableRow
devSyncDataPortAssignEntry = _DevSyncDataPortAssignEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 7, 2, 1)
)
devSyncDataPortAssignEntry.setIndexNames(
    (0, "PDN-CROSSCONNECT-MIB", "devSyncDataPortAssignIndex"),
)
if mibBuilder.loadTexts:
    devSyncDataPortAssignEntry.setStatus("mandatory")
_DevSyncDataPortAssignIndex_Type = Integer32
_DevSyncDataPortAssignIndex_Object = MibTableColumn
devSyncDataPortAssignIndex = _DevSyncDataPortAssignIndex_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 7, 2, 1, 1),
    _DevSyncDataPortAssignIndex_Type()
)
devSyncDataPortAssignIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devSyncDataPortAssignIndex.setStatus("mandatory")


class _DevSyncDataPortAssignRate_Type(Integer32):
    """Custom type devSyncDataPortAssignRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24)
        )
    )
    namedValues = NamedValues(
        *(("rate1008or1152", 18),
          ("rate1064or1216", 19),
          ("rate1120or1280", 20),
          ("rate112or128", 2),
          ("rate1176or1344", 21),
          ("rate1232or1408", 22),
          ("rate1288or1472", 23),
          ("rate1344or1536", 24),
          ("rate168or192", 3),
          ("rate224or256", 4),
          ("rate280or320", 5),
          ("rate336or384", 6),
          ("rate392or448", 7),
          ("rate448or512", 8),
          ("rate504or576", 9),
          ("rate560or640", 10),
          ("rate56or64", 1),
          ("rate616or704", 11),
          ("rate672or768", 12),
          ("rate728or832", 13),
          ("rate784or896", 14),
          ("rate840or960", 15),
          ("rate896or1024", 16),
          ("rate952or1088", 17))
    )


_DevSyncDataPortAssignRate_Type.__name__ = "Integer32"
_DevSyncDataPortAssignRate_Object = MibTableColumn
devSyncDataPortAssignRate = _DevSyncDataPortAssignRate_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 7, 2, 1, 2),
    _DevSyncDataPortAssignRate_Type()
)
devSyncDataPortAssignRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devSyncDataPortAssignRate.setStatus("mandatory")
_DevSyncDataPortAssignIfIndex_Type = Integer32
_DevSyncDataPortAssignIfIndex_Object = MibTableColumn
devSyncDataPortAssignIfIndex = _DevSyncDataPortAssignIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 7, 2, 1, 3),
    _DevSyncDataPortAssignIfIndex_Type()
)
devSyncDataPortAssignIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devSyncDataPortAssignIfIndex.setStatus("mandatory")
_DevCrossConUtility_ObjectIdentity = ObjectIdentity
devCrossConUtility = _DevCrossConUtility_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 7, 4)
)


class _DevCrossConClear_Type(Integer32):
    """Custom type devCrossConClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clear", 3),
          ("idle", 1),
          ("inprogress", 2))
    )


_DevCrossConClear_Type.__name__ = "Integer32"
_DevCrossConClear_Object = MibScalar
devCrossConClear = _DevCrossConClear_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 7, 4, 1),
    _DevCrossConClear_Type()
)
devCrossConClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devCrossConClear.setStatus("mandatory")
_DevCrossConTableLastChange_Type = TimeTicks
_DevCrossConTableLastChange_Object = MibScalar
devCrossConTableLastChange = _DevCrossConTableLastChange_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 7, 4, 2),
    _DevCrossConTableLastChange_Type()
)
devCrossConTableLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devCrossConTableLastChange.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PDN-CROSSCONNECT-MIB",
    **{"devDs1FracTable": devDs1FracTable,
       "devDs1FracEntry": devDs1FracEntry,
       "devDs1FracIndex": devDs1FracIndex,
       "devDs1FracNumber": devDs1FracNumber,
       "devDs1FracIfIndex": devDs1FracIfIndex,
       "devDs1FracIfFracNumber": devDs1FracIfFracNumber,
       "devSyncDataPortAssignTable": devSyncDataPortAssignTable,
       "devSyncDataPortAssignEntry": devSyncDataPortAssignEntry,
       "devSyncDataPortAssignIndex": devSyncDataPortAssignIndex,
       "devSyncDataPortAssignRate": devSyncDataPortAssignRate,
       "devSyncDataPortAssignIfIndex": devSyncDataPortAssignIfIndex,
       "devCrossConUtility": devCrossConUtility,
       "devCrossConClear": devCrossConClear,
       "devCrossConTableLastChange": devCrossConTableLastChange}
)
