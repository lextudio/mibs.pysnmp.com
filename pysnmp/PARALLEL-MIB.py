# SNMP MIB module (PARALLEL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PARALLEL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:36:56 2024
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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
 transmission) = mibBuilder.importSymbols(
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
    "transmission")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

para = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 10, 34)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ParaNumber_Type = Integer32
_ParaNumber_Object = MibScalar
paraNumber = _ParaNumber_Object(
    (1, 3, 6, 1, 2, 1, 10, 34, 1),
    _ParaNumber_Type()
)
paraNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paraNumber.setStatus("current")
_ParaPortTable_Object = MibTable
paraPortTable = _ParaPortTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 34, 2)
)
if mibBuilder.loadTexts:
    paraPortTable.setStatus("current")
_ParaPortEntry_Object = MibTableRow
paraPortEntry = _ParaPortEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 34, 2, 1)
)
paraPortEntry.setIndexNames(
    (0, "PARALLEL-MIB", "paraPortIndex"),
)
if mibBuilder.loadTexts:
    paraPortEntry.setStatus("current")
_ParaPortIndex_Type = InterfaceIndex
_ParaPortIndex_Object = MibTableColumn
paraPortIndex = _ParaPortIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 34, 2, 1, 1),
    _ParaPortIndex_Type()
)
paraPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paraPortIndex.setStatus("current")


class _ParaPortType_Type(Integer32):
    """Custom type paraPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("centronics", 2),
          ("dataproducts", 3),
          ("other", 1))
    )


_ParaPortType_Type.__name__ = "Integer32"
_ParaPortType_Object = MibTableColumn
paraPortType = _ParaPortType_Object(
    (1, 3, 6, 1, 2, 1, 10, 34, 2, 1, 2),
    _ParaPortType_Type()
)
paraPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paraPortType.setStatus("current")
_ParaPortInSigNumber_Type = Integer32
_ParaPortInSigNumber_Object = MibTableColumn
paraPortInSigNumber = _ParaPortInSigNumber_Object(
    (1, 3, 6, 1, 2, 1, 10, 34, 2, 1, 3),
    _ParaPortInSigNumber_Type()
)
paraPortInSigNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paraPortInSigNumber.setStatus("current")
_ParaPortOutSigNumber_Type = Integer32
_ParaPortOutSigNumber_Object = MibTableColumn
paraPortOutSigNumber = _ParaPortOutSigNumber_Object(
    (1, 3, 6, 1, 2, 1, 10, 34, 2, 1, 4),
    _ParaPortOutSigNumber_Type()
)
paraPortOutSigNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paraPortOutSigNumber.setStatus("current")
_ParaInSigTable_Object = MibTable
paraInSigTable = _ParaInSigTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 34, 3)
)
if mibBuilder.loadTexts:
    paraInSigTable.setStatus("current")
_ParaInSigEntry_Object = MibTableRow
paraInSigEntry = _ParaInSigEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 34, 3, 1)
)
paraInSigEntry.setIndexNames(
    (0, "PARALLEL-MIB", "paraInSigPortIndex"),
    (0, "PARALLEL-MIB", "paraInSigName"),
)
if mibBuilder.loadTexts:
    paraInSigEntry.setStatus("current")
_ParaInSigPortIndex_Type = InterfaceIndex
_ParaInSigPortIndex_Object = MibTableColumn
paraInSigPortIndex = _ParaInSigPortIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 34, 3, 1, 1),
    _ParaInSigPortIndex_Type()
)
paraInSigPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paraInSigPortIndex.setStatus("current")


class _ParaInSigName_Type(Integer32):
    """Custom type paraInSigName based on Integer32"""
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
        *(("busy", 3),
          ("fault", 5),
          ("online", 2),
          ("paperout", 4),
          ("power", 1))
    )


_ParaInSigName_Type.__name__ = "Integer32"
_ParaInSigName_Object = MibTableColumn
paraInSigName = _ParaInSigName_Object(
    (1, 3, 6, 1, 2, 1, 10, 34, 3, 1, 2),
    _ParaInSigName_Type()
)
paraInSigName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paraInSigName.setStatus("current")


class _ParaInSigState_Type(Integer32):
    """Custom type paraInSigState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("off", 3),
          ("on", 2))
    )


_ParaInSigState_Type.__name__ = "Integer32"
_ParaInSigState_Object = MibTableColumn
paraInSigState = _ParaInSigState_Object(
    (1, 3, 6, 1, 2, 1, 10, 34, 3, 1, 3),
    _ParaInSigState_Type()
)
paraInSigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paraInSigState.setStatus("current")
_ParaInSigChanges_Type = Counter32
_ParaInSigChanges_Object = MibTableColumn
paraInSigChanges = _ParaInSigChanges_Object(
    (1, 3, 6, 1, 2, 1, 10, 34, 3, 1, 4),
    _ParaInSigChanges_Type()
)
paraInSigChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paraInSigChanges.setStatus("current")
_ParaOutSigTable_Object = MibTable
paraOutSigTable = _ParaOutSigTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 34, 4)
)
if mibBuilder.loadTexts:
    paraOutSigTable.setStatus("current")
_ParaOutSigEntry_Object = MibTableRow
paraOutSigEntry = _ParaOutSigEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 34, 4, 1)
)
paraOutSigEntry.setIndexNames(
    (0, "PARALLEL-MIB", "paraOutSigPortIndex"),
    (0, "PARALLEL-MIB", "paraOutSigName"),
)
if mibBuilder.loadTexts:
    paraOutSigEntry.setStatus("current")
_ParaOutSigPortIndex_Type = InterfaceIndex
_ParaOutSigPortIndex_Object = MibTableColumn
paraOutSigPortIndex = _ParaOutSigPortIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 34, 4, 1, 1),
    _ParaOutSigPortIndex_Type()
)
paraOutSigPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paraOutSigPortIndex.setStatus("current")


class _ParaOutSigName_Type(Integer32):
    """Custom type paraOutSigName based on Integer32"""
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
        *(("busy", 3),
          ("fault", 5),
          ("online", 2),
          ("paperout", 4),
          ("power", 1))
    )


_ParaOutSigName_Type.__name__ = "Integer32"
_ParaOutSigName_Object = MibTableColumn
paraOutSigName = _ParaOutSigName_Object(
    (1, 3, 6, 1, 2, 1, 10, 34, 4, 1, 2),
    _ParaOutSigName_Type()
)
paraOutSigName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paraOutSigName.setStatus("current")


class _ParaOutSigState_Type(Integer32):
    """Custom type paraOutSigState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("off", 3),
          ("on", 2))
    )


_ParaOutSigState_Type.__name__ = "Integer32"
_ParaOutSigState_Object = MibTableColumn
paraOutSigState = _ParaOutSigState_Object(
    (1, 3, 6, 1, 2, 1, 10, 34, 4, 1, 3),
    _ParaOutSigState_Type()
)
paraOutSigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paraOutSigState.setStatus("current")
_ParaOutSigChanges_Type = Counter32
_ParaOutSigChanges_Object = MibTableColumn
paraOutSigChanges = _ParaOutSigChanges_Object(
    (1, 3, 6, 1, 2, 1, 10, 34, 4, 1, 4),
    _ParaOutSigChanges_Type()
)
paraOutSigChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paraOutSigChanges.setStatus("current")
_ParaConformance_ObjectIdentity = ObjectIdentity
paraConformance = _ParaConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 34, 5)
)
_ParaGroups_ObjectIdentity = ObjectIdentity
paraGroups = _ParaGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 34, 5, 1)
)
_ParaCompliances_ObjectIdentity = ObjectIdentity
paraCompliances = _ParaCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 34, 5, 2)
)

# Managed Objects groups

paraGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 34, 5, 1, 1)
)
paraGroup.setObjects(
      *(("PARALLEL-MIB", "paraNumber"),
        ("PARALLEL-MIB", "paraPortIndex"),
        ("PARALLEL-MIB", "paraPortType"),
        ("PARALLEL-MIB", "paraPortInSigNumber"),
        ("PARALLEL-MIB", "paraPortOutSigNumber"),
        ("PARALLEL-MIB", "paraInSigPortIndex"),
        ("PARALLEL-MIB", "paraInSigName"),
        ("PARALLEL-MIB", "paraInSigState"),
        ("PARALLEL-MIB", "paraInSigChanges"),
        ("PARALLEL-MIB", "paraOutSigPortIndex"),
        ("PARALLEL-MIB", "paraOutSigName"),
        ("PARALLEL-MIB", "paraOutSigState"),
        ("PARALLEL-MIB", "paraOutSigChanges"))
)
if mibBuilder.loadTexts:
    paraGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

paraCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 10, 34, 5, 2, 1)
)
if mibBuilder.loadTexts:
    paraCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PARALLEL-MIB",
    **{"para": para,
       "paraNumber": paraNumber,
       "paraPortTable": paraPortTable,
       "paraPortEntry": paraPortEntry,
       "paraPortIndex": paraPortIndex,
       "paraPortType": paraPortType,
       "paraPortInSigNumber": paraPortInSigNumber,
       "paraPortOutSigNumber": paraPortOutSigNumber,
       "paraInSigTable": paraInSigTable,
       "paraInSigEntry": paraInSigEntry,
       "paraInSigPortIndex": paraInSigPortIndex,
       "paraInSigName": paraInSigName,
       "paraInSigState": paraInSigState,
       "paraInSigChanges": paraInSigChanges,
       "paraOutSigTable": paraOutSigTable,
       "paraOutSigEntry": paraOutSigEntry,
       "paraOutSigPortIndex": paraOutSigPortIndex,
       "paraOutSigName": paraOutSigName,
       "paraOutSigState": paraOutSigState,
       "paraOutSigChanges": paraOutSigChanges,
       "paraConformance": paraConformance,
       "paraGroups": paraGroups,
       "paraGroup": paraGroup,
       "paraCompliances": paraCompliances,
       "paraCompliance": paraCompliance}
)
