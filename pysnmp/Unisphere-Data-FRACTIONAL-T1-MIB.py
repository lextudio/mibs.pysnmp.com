# SNMP MIB module (Unisphere-Data-FRACTIONAL-T1-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Unisphere-Data-FRACTIONAL-T1-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:10:43 2024
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
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
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

(usDataMibs,) = mibBuilder.importSymbols(
    "Unisphere-Data-MIBs",
    "usDataMibs")

(UsdNextIfIndex,
 UsdTimeSlotMap) = mibBuilder.importSymbols(
    "Unisphere-Data-TC",
    "UsdNextIfIndex",
    "UsdTimeSlotMap")


# MODULE-IDENTITY

usdFt1MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 6)
)
usdFt1MIB.setRevisions(
        ("2000-09-26 17:30",
         "1999-07-14 00:00",
         "1998-11-13 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_UsdFt1Objects_ObjectIdentity = ObjectIdentity
usdFt1Objects = _UsdFt1Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 6, 1)
)
_UsdFt1NextIfIndex_Type = UsdNextIfIndex
_UsdFt1NextIfIndex_Object = MibScalar
usdFt1NextIfIndex = _UsdFt1NextIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 6, 1, 1),
    _UsdFt1NextIfIndex_Type()
)
usdFt1NextIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdFt1NextIfIndex.setStatus("current")
_UsdFt1IfTable_Object = MibTable
usdFt1IfTable = _UsdFt1IfTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 6, 1, 2)
)
if mibBuilder.loadTexts:
    usdFt1IfTable.setStatus("current")
_UsdFt1IfEntry_Object = MibTableRow
usdFt1IfEntry = _UsdFt1IfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 6, 1, 2, 1)
)
usdFt1IfEntry.setIndexNames(
    (0, "Unisphere-Data-FRACTIONAL-T1-MIB", "usdFt1IfIndex"),
)
if mibBuilder.loadTexts:
    usdFt1IfEntry.setStatus("current")
_UsdFt1IfIndex_Type = InterfaceIndex
_UsdFt1IfIndex_Object = MibTableColumn
usdFt1IfIndex = _UsdFt1IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 6, 1, 2, 1, 1),
    _UsdFt1IfIndex_Type()
)
usdFt1IfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdFt1IfIndex.setStatus("current")
_UsdFt1IfRowStatus_Type = RowStatus
_UsdFt1IfRowStatus_Object = MibTableColumn
usdFt1IfRowStatus = _UsdFt1IfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 6, 1, 2, 1, 2),
    _UsdFt1IfRowStatus_Type()
)
usdFt1IfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdFt1IfRowStatus.setStatus("current")
_UsdFt1IfLowerIfIndex_Type = InterfaceIndexOrZero
_UsdFt1IfLowerIfIndex_Object = MibTableColumn
usdFt1IfLowerIfIndex = _UsdFt1IfLowerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 6, 1, 2, 1, 3),
    _UsdFt1IfLowerIfIndex_Type()
)
usdFt1IfLowerIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdFt1IfLowerIfIndex.setStatus("current")
_UsdFt1IfTimeSlotMap_Type = UsdTimeSlotMap
_UsdFt1IfTimeSlotMap_Object = MibTableColumn
usdFt1IfTimeSlotMap = _UsdFt1IfTimeSlotMap_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 6, 1, 2, 1, 4),
    _UsdFt1IfTimeSlotMap_Type()
)
usdFt1IfTimeSlotMap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdFt1IfTimeSlotMap.setStatus("current")


class _UsdFt1IfTimeSlotRate_Type(Integer32):
    """Custom type usdFt1IfTimeSlotRate based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nx56kbps", 0),
          ("nx64kbps", 1))
    )


_UsdFt1IfTimeSlotRate_Type.__name__ = "Integer32"
_UsdFt1IfTimeSlotRate_Object = MibTableColumn
usdFt1IfTimeSlotRate = _UsdFt1IfTimeSlotRate_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 6, 1, 2, 1, 5),
    _UsdFt1IfTimeSlotRate_Type()
)
usdFt1IfTimeSlotRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdFt1IfTimeSlotRate.setStatus("current")


class _UsdFt1IfDataPolarity_Type(Integer32):
    """Custom type usdFt1IfDataPolarity based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inverted", 1),
          ("normal", 0))
    )


_UsdFt1IfDataPolarity_Type.__name__ = "Integer32"
_UsdFt1IfDataPolarity_Object = MibTableColumn
usdFt1IfDataPolarity = _UsdFt1IfDataPolarity_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 6, 1, 2, 1, 6),
    _UsdFt1IfDataPolarity_Type()
)
usdFt1IfDataPolarity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdFt1IfDataPolarity.setStatus("obsolete")


class _UsdFt1IfLoopbackConfig_Type(Integer32):
    """Custom type usdFt1IfLoopbackConfig based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("loop", 1),
          ("noLoop", 0))
    )


_UsdFt1IfLoopbackConfig_Type.__name__ = "Integer32"
_UsdFt1IfLoopbackConfig_Object = MibTableColumn
usdFt1IfLoopbackConfig = _UsdFt1IfLoopbackConfig_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 6, 1, 2, 1, 7),
    _UsdFt1IfLoopbackConfig_Type()
)
usdFt1IfLoopbackConfig.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdFt1IfLoopbackConfig.setStatus("current")
_UsdFt1Conformance_ObjectIdentity = ObjectIdentity
usdFt1Conformance = _UsdFt1Conformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 6, 4)
)
_UsdFt1Compliances_ObjectIdentity = ObjectIdentity
usdFt1Compliances = _UsdFt1Compliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 6, 4, 1)
)
_UsdFt1Groups_ObjectIdentity = ObjectIdentity
usdFt1Groups = _UsdFt1Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 6, 4, 2)
)

# Managed Objects groups

usdFt1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 6, 4, 2, 1)
)
usdFt1Group.setObjects(
      *(("Unisphere-Data-FRACTIONAL-T1-MIB", "usdFt1NextIfIndex"),
        ("Unisphere-Data-FRACTIONAL-T1-MIB", "usdFt1IfRowStatus"),
        ("Unisphere-Data-FRACTIONAL-T1-MIB", "usdFt1IfLowerIfIndex"),
        ("Unisphere-Data-FRACTIONAL-T1-MIB", "usdFt1IfTimeSlotMap"),
        ("Unisphere-Data-FRACTIONAL-T1-MIB", "usdFt1IfTimeSlotRate"),
        ("Unisphere-Data-FRACTIONAL-T1-MIB", "usdFt1IfDataPolarity"),
        ("Unisphere-Data-FRACTIONAL-T1-MIB", "usdFt1IfLoopbackConfig"))
)
if mibBuilder.loadTexts:
    usdFt1Group.setStatus("obsolete")

usdFt1Group2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 6, 4, 2, 2)
)
usdFt1Group2.setObjects(
      *(("Unisphere-Data-FRACTIONAL-T1-MIB", "usdFt1NextIfIndex"),
        ("Unisphere-Data-FRACTIONAL-T1-MIB", "usdFt1IfRowStatus"),
        ("Unisphere-Data-FRACTIONAL-T1-MIB", "usdFt1IfLowerIfIndex"),
        ("Unisphere-Data-FRACTIONAL-T1-MIB", "usdFt1IfTimeSlotMap"),
        ("Unisphere-Data-FRACTIONAL-T1-MIB", "usdFt1IfTimeSlotRate"),
        ("Unisphere-Data-FRACTIONAL-T1-MIB", "usdFt1IfLoopbackConfig"))
)
if mibBuilder.loadTexts:
    usdFt1Group2.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

usdFt1Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 6, 4, 1, 1)
)
if mibBuilder.loadTexts:
    usdFt1Compliance.setStatus(
        "obsolete"
    )

usdFt1Compliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 6, 4, 1, 2)
)
if mibBuilder.loadTexts:
    usdFt1Compliance2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Unisphere-Data-FRACTIONAL-T1-MIB",
    **{"usdFt1MIB": usdFt1MIB,
       "usdFt1Objects": usdFt1Objects,
       "usdFt1NextIfIndex": usdFt1NextIfIndex,
       "usdFt1IfTable": usdFt1IfTable,
       "usdFt1IfEntry": usdFt1IfEntry,
       "usdFt1IfIndex": usdFt1IfIndex,
       "usdFt1IfRowStatus": usdFt1IfRowStatus,
       "usdFt1IfLowerIfIndex": usdFt1IfLowerIfIndex,
       "usdFt1IfTimeSlotMap": usdFt1IfTimeSlotMap,
       "usdFt1IfTimeSlotRate": usdFt1IfTimeSlotRate,
       "usdFt1IfDataPolarity": usdFt1IfDataPolarity,
       "usdFt1IfLoopbackConfig": usdFt1IfLoopbackConfig,
       "usdFt1Conformance": usdFt1Conformance,
       "usdFt1Compliances": usdFt1Compliances,
       "usdFt1Compliance": usdFt1Compliance,
       "usdFt1Compliance2": usdFt1Compliance2,
       "usdFt1Groups": usdFt1Groups,
       "usdFt1Group": usdFt1Group,
       "usdFt1Group2": usdFt1Group2}
)
