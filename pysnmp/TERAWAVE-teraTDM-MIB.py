# SNMP MIB module (TERAWAVE-teraTDM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TERAWAVE-teraTDM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:01:20 2024
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
 enterprises,
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
    "enterprises",
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

_Terawave_ObjectIdentity = ObjectIdentity
terawave = _Terawave_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4513)
)
_TeraCDS3Group_ObjectIdentity = ObjectIdentity
teraCDS3Group = _TeraCDS3Group_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4513, 8)
)
_TeraTDMCardStatsTable_Object = MibTable
teraTDMCardStatsTable = _TeraTDMCardStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 8, 8)
)
if mibBuilder.loadTexts:
    teraTDMCardStatsTable.setStatus("mandatory")
_TeraTDMCardStatsTableEntry_Object = MibTableRow
teraTDMCardStatsTableEntry = _TeraTDMCardStatsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 8, 8, 1)
)
teraTDMCardStatsTableEntry.setIndexNames(
    (0, "TERAWAVE-teraTDM-MIB", "teraTDMSlotIndex"),
)
if mibBuilder.loadTexts:
    teraTDMCardStatsTableEntry.setStatus("mandatory")
_TeraTDMSlotIndex_Type = Counter32
_TeraTDMSlotIndex_Object = MibTableColumn
teraTDMSlotIndex = _TeraTDMSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 4513, 8, 8, 1, 1),
    _TeraTDMSlotIndex_Type()
)
teraTDMSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraTDMSlotIndex.setStatus("mandatory")


class _TeraTDMPeabodyLSBState_Type(Integer32):
    """Custom type teraTDMPeabodyLSBState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("idle", 1),
          ("monitoringBus", 3),
          ("waitForBus", 2))
    )


_TeraTDMPeabodyLSBState_Type.__name__ = "Integer32"
_TeraTDMPeabodyLSBState_Object = MibTableColumn
teraTDMPeabodyLSBState = _TeraTDMPeabodyLSBState_Object(
    (1, 3, 6, 1, 4, 1, 4513, 8, 8, 1, 2),
    _TeraTDMPeabodyLSBState_Type()
)
teraTDMPeabodyLSBState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraTDMPeabodyLSBState.setStatus("mandatory")
_TeraTDMPeabodyLSBCrcCount_Type = Counter32
_TeraTDMPeabodyLSBCrcCount_Object = MibTableColumn
teraTDMPeabodyLSBCrcCount = _TeraTDMPeabodyLSBCrcCount_Object(
    (1, 3, 6, 1, 4, 1, 4513, 8, 8, 1, 3),
    _TeraTDMPeabodyLSBCrcCount_Type()
)
teraTDMPeabodyLSBCrcCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraTDMPeabodyLSBCrcCount.setStatus("mandatory")
_TeraTDMPeabodyTransitionUpCount_Type = Counter32
_TeraTDMPeabodyTransitionUpCount_Object = MibTableColumn
teraTDMPeabodyTransitionUpCount = _TeraTDMPeabodyTransitionUpCount_Object(
    (1, 3, 6, 1, 4, 1, 4513, 8, 8, 1, 4),
    _TeraTDMPeabodyTransitionUpCount_Type()
)
teraTDMPeabodyTransitionUpCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraTDMPeabodyTransitionUpCount.setStatus("mandatory")
_TeraTDMPeabodyLSBCrcLastSlot_Type = Integer32
_TeraTDMPeabodyLSBCrcLastSlot_Object = MibTableColumn
teraTDMPeabodyLSBCrcLastSlot = _TeraTDMPeabodyLSBCrcLastSlot_Object(
    (1, 3, 6, 1, 4, 1, 4513, 8, 8, 1, 5),
    _TeraTDMPeabodyLSBCrcLastSlot_Type()
)
teraTDMPeabodyLSBCrcLastSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraTDMPeabodyLSBCrcLastSlot.setStatus("mandatory")
_TeraTDMPeabodyVersion_Type = Integer32
_TeraTDMPeabodyVersion_Object = MibTableColumn
teraTDMPeabodyVersion = _TeraTDMPeabodyVersion_Object(
    (1, 3, 6, 1, 4, 1, 4513, 8, 8, 1, 6),
    _TeraTDMPeabodyVersion_Type()
)
teraTDMPeabodyVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraTDMPeabodyVersion.setStatus("mandatory")
_TeraTDMPeabodyFeature_Type = Integer32
_TeraTDMPeabodyFeature_Object = MibTableColumn
teraTDMPeabodyFeature = _TeraTDMPeabodyFeature_Object(
    (1, 3, 6, 1, 4, 1, 4513, 8, 8, 1, 7),
    _TeraTDMPeabodyFeature_Type()
)
teraTDMPeabodyFeature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraTDMPeabodyFeature.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TERAWAVE-teraTDM-MIB",
    **{"terawave": terawave,
       "teraCDS3Group": teraCDS3Group,
       "teraTDMCardStatsTable": teraTDMCardStatsTable,
       "teraTDMCardStatsTableEntry": teraTDMCardStatsTableEntry,
       "teraTDMSlotIndex": teraTDMSlotIndex,
       "teraTDMPeabodyLSBState": teraTDMPeabodyLSBState,
       "teraTDMPeabodyLSBCrcCount": teraTDMPeabodyLSBCrcCount,
       "teraTDMPeabodyTransitionUpCount": teraTDMPeabodyTransitionUpCount,
       "teraTDMPeabodyLSBCrcLastSlot": teraTDMPeabodyLSBCrcLastSlot,
       "teraTDMPeabodyVersion": teraTDMPeabodyVersion,
       "teraTDMPeabodyFeature": teraTDMPeabodyFeature}
)
