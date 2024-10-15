# SNMP MIB module (REDSTONE-FRACTIONAL-T1-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/REDSTONE-FRACTIONAL-T1-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:46:37 2024
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

(rsMgmt,) = mibBuilder.importSymbols(
    "REDSTONE-SMI",
    "rsMgmt")

(RsNextIfIndex,
 RsTimeSlotMap) = mibBuilder.importSymbols(
    "REDSTONE-TC",
    "RsNextIfIndex",
    "RsTimeSlotMap")

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

rsFt1MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 6)
)
rsFt1MIB.setRevisions(
        ("1999-07-14 00:00",
         "1998-01-01 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RsFt1Objects_ObjectIdentity = ObjectIdentity
rsFt1Objects = _RsFt1Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 6, 1)
)
_RsFt1NextIfIndex_Type = RsNextIfIndex
_RsFt1NextIfIndex_Object = MibScalar
rsFt1NextIfIndex = _RsFt1NextIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 6, 1, 1),
    _RsFt1NextIfIndex_Type()
)
rsFt1NextIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsFt1NextIfIndex.setStatus("current")
_RsFt1IfTable_Object = MibTable
rsFt1IfTable = _RsFt1IfTable_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 6, 1, 2)
)
if mibBuilder.loadTexts:
    rsFt1IfTable.setStatus("current")
_RsFt1IfEntry_Object = MibTableRow
rsFt1IfEntry = _RsFt1IfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 6, 1, 2, 1)
)
rsFt1IfEntry.setIndexNames(
    (0, "REDSTONE-FRACTIONAL-T1-MIB", "rsFt1IfIndex"),
)
if mibBuilder.loadTexts:
    rsFt1IfEntry.setStatus("current")
_RsFt1IfIndex_Type = InterfaceIndex
_RsFt1IfIndex_Object = MibTableColumn
rsFt1IfIndex = _RsFt1IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 6, 1, 2, 1, 1),
    _RsFt1IfIndex_Type()
)
rsFt1IfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rsFt1IfIndex.setStatus("current")
_RsFt1IfRowStatus_Type = RowStatus
_RsFt1IfRowStatus_Object = MibTableColumn
rsFt1IfRowStatus = _RsFt1IfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 6, 1, 2, 1, 2),
    _RsFt1IfRowStatus_Type()
)
rsFt1IfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsFt1IfRowStatus.setStatus("current")
_RsFt1IfLowerIfIndex_Type = InterfaceIndexOrZero
_RsFt1IfLowerIfIndex_Object = MibTableColumn
rsFt1IfLowerIfIndex = _RsFt1IfLowerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 6, 1, 2, 1, 3),
    _RsFt1IfLowerIfIndex_Type()
)
rsFt1IfLowerIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsFt1IfLowerIfIndex.setStatus("current")
_RsFt1IfTimeSlotMap_Type = RsTimeSlotMap
_RsFt1IfTimeSlotMap_Object = MibTableColumn
rsFt1IfTimeSlotMap = _RsFt1IfTimeSlotMap_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 6, 1, 2, 1, 4),
    _RsFt1IfTimeSlotMap_Type()
)
rsFt1IfTimeSlotMap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsFt1IfTimeSlotMap.setStatus("current")


class _RsFt1IfTimeSlotRate_Type(Integer32):
    """Custom type rsFt1IfTimeSlotRate based on Integer32"""
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


_RsFt1IfTimeSlotRate_Type.__name__ = "Integer32"
_RsFt1IfTimeSlotRate_Object = MibTableColumn
rsFt1IfTimeSlotRate = _RsFt1IfTimeSlotRate_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 6, 1, 2, 1, 5),
    _RsFt1IfTimeSlotRate_Type()
)
rsFt1IfTimeSlotRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsFt1IfTimeSlotRate.setStatus("current")


class _RsFt1IfDataPolarity_Type(Integer32):
    """Custom type rsFt1IfDataPolarity based on Integer32"""
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


_RsFt1IfDataPolarity_Type.__name__ = "Integer32"
_RsFt1IfDataPolarity_Object = MibTableColumn
rsFt1IfDataPolarity = _RsFt1IfDataPolarity_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 6, 1, 2, 1, 6),
    _RsFt1IfDataPolarity_Type()
)
rsFt1IfDataPolarity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsFt1IfDataPolarity.setStatus("obsolete")


class _RsFt1IfLoopbackConfig_Type(Integer32):
    """Custom type rsFt1IfLoopbackConfig based on Integer32"""
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


_RsFt1IfLoopbackConfig_Type.__name__ = "Integer32"
_RsFt1IfLoopbackConfig_Object = MibTableColumn
rsFt1IfLoopbackConfig = _RsFt1IfLoopbackConfig_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 6, 1, 2, 1, 7),
    _RsFt1IfLoopbackConfig_Type()
)
rsFt1IfLoopbackConfig.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsFt1IfLoopbackConfig.setStatus("current")
_RsFt1Conformance_ObjectIdentity = ObjectIdentity
rsFt1Conformance = _RsFt1Conformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 6, 4)
)
_RsFt1Compliances_ObjectIdentity = ObjectIdentity
rsFt1Compliances = _RsFt1Compliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 6, 4, 1)
)
_RsFt1Groups_ObjectIdentity = ObjectIdentity
rsFt1Groups = _RsFt1Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 6, 4, 2)
)

# Managed Objects groups

rsFt1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2773, 2, 6, 4, 2, 1)
)
rsFt1Group.setObjects(
      *(("REDSTONE-FRACTIONAL-T1-MIB", "rsFt1NextIfIndex"),
        ("REDSTONE-FRACTIONAL-T1-MIB", "rsFt1IfRowStatus"),
        ("REDSTONE-FRACTIONAL-T1-MIB", "rsFt1IfLowerIfIndex"),
        ("REDSTONE-FRACTIONAL-T1-MIB", "rsFt1IfTimeSlotMap"),
        ("REDSTONE-FRACTIONAL-T1-MIB", "rsFt1IfTimeSlotRate"),
        ("REDSTONE-FRACTIONAL-T1-MIB", "rsFt1IfDataPolarity"),
        ("REDSTONE-FRACTIONAL-T1-MIB", "rsFt1IfLoopbackConfig"))
)
if mibBuilder.loadTexts:
    rsFt1Group.setStatus("obsolete")

rsFt1Group2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2773, 2, 6, 4, 2, 2)
)
rsFt1Group2.setObjects(
      *(("REDSTONE-FRACTIONAL-T1-MIB", "rsFt1NextIfIndex"),
        ("REDSTONE-FRACTIONAL-T1-MIB", "rsFt1IfRowStatus"),
        ("REDSTONE-FRACTIONAL-T1-MIB", "rsFt1IfLowerIfIndex"),
        ("REDSTONE-FRACTIONAL-T1-MIB", "rsFt1IfTimeSlotMap"),
        ("REDSTONE-FRACTIONAL-T1-MIB", "rsFt1IfTimeSlotRate"),
        ("REDSTONE-FRACTIONAL-T1-MIB", "rsFt1IfLoopbackConfig"))
)
if mibBuilder.loadTexts:
    rsFt1Group2.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

rsFt1Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2773, 2, 6, 4, 1, 1)
)
if mibBuilder.loadTexts:
    rsFt1Compliance.setStatus(
        "obsolete"
    )

rsFt1Compliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2773, 2, 6, 4, 1, 2)
)
if mibBuilder.loadTexts:
    rsFt1Compliance2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "REDSTONE-FRACTIONAL-T1-MIB",
    **{"rsFt1MIB": rsFt1MIB,
       "rsFt1Objects": rsFt1Objects,
       "rsFt1NextIfIndex": rsFt1NextIfIndex,
       "rsFt1IfTable": rsFt1IfTable,
       "rsFt1IfEntry": rsFt1IfEntry,
       "rsFt1IfIndex": rsFt1IfIndex,
       "rsFt1IfRowStatus": rsFt1IfRowStatus,
       "rsFt1IfLowerIfIndex": rsFt1IfLowerIfIndex,
       "rsFt1IfTimeSlotMap": rsFt1IfTimeSlotMap,
       "rsFt1IfTimeSlotRate": rsFt1IfTimeSlotRate,
       "rsFt1IfDataPolarity": rsFt1IfDataPolarity,
       "rsFt1IfLoopbackConfig": rsFt1IfLoopbackConfig,
       "rsFt1Conformance": rsFt1Conformance,
       "rsFt1Compliances": rsFt1Compliances,
       "rsFt1Compliance": rsFt1Compliance,
       "rsFt1Compliance2": rsFt1Compliance2,
       "rsFt1Groups": rsFt1Groups,
       "rsFt1Group": rsFt1Group,
       "rsFt1Group2": rsFt1Group2}
)
