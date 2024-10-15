# SNMP MIB module (DECHUB900-HRIP-MIB-V3-0) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DECHUB900-HRIP-MIB-V3-0
# Produced by pysmi-1.5.4 at Mon Oct 14 21:23:41 2024
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

_Dec_ObjectIdentity = ObjectIdentity
dec = _Dec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36)
)
_Ema_ObjectIdentity = ObjectIdentity
ema = _Ema_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2)
)
_DecMIBextension_ObjectIdentity = ObjectIdentity
decMIBextension = _DecMIBextension_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18)
)
_DecHub900_ObjectIdentity = ObjectIdentity
decHub900 = _DecHub900_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11)
)
_MgmtAgent_ObjectIdentity = ObjectIdentity
mgmtAgent = _MgmtAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1)
)
_MgmtAgentVersion1_ObjectIdentity = ObjectIdentity
mgmtAgentVersion1 = _MgmtAgentVersion1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1)
)
_Hrip_ObjectIdentity = ObjectIdentity
hrip = _Hrip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 2)
)
_HripPubRingCfgTable_Object = MibTable
hripPubRingCfgTable = _HripPubRingCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hripPubRingCfgTable.setStatus("mandatory")
_HripPubRingCfgEntry_Object = MibTableRow
hripPubRingCfgEntry = _HripPubRingCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 2, 1, 1)
)
hripPubRingCfgEntry.setIndexNames(
    (0, "DECHUB900-HRIP-MIB-V3-0", "hripRingCfgIndex"),
)
if mibBuilder.loadTexts:
    hripPubRingCfgEntry.setStatus("mandatory")


class _HripRingCfgIndex_Type(Integer32):
    """Custom type hripRingCfgIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ringA", 1),
          ("ringB", 2))
    )


_HripRingCfgIndex_Type.__name__ = "Integer32"
_HripRingCfgIndex_Object = MibTableColumn
hripRingCfgIndex = _HripRingCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 2, 1, 1, 1),
    _HripRingCfgIndex_Type()
)
hripRingCfgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hripRingCfgIndex.setStatus("mandatory")


class _HripRingCfgSpeed_Type(Integer32):
    """Custom type hripRingCfgSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("speed16", 3),
          ("speed4", 2))
    )


_HripRingCfgSpeed_Type.__name__ = "Integer32"
_HripRingCfgSpeed_Object = MibTableColumn
hripRingCfgSpeed = _HripRingCfgSpeed_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 2, 1, 1, 2),
    _HripRingCfgSpeed_Type()
)
hripRingCfgSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hripRingCfgSpeed.setStatus("mandatory")
_HripPubSlotCfgTable_Object = MibTable
hripPubSlotCfgTable = _HripPubSlotCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    hripPubSlotCfgTable.setStatus("mandatory")
_HripPubSlotCfgEntry_Object = MibTableRow
hripPubSlotCfgEntry = _HripPubSlotCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 2, 2, 1)
)
hripPubSlotCfgEntry.setIndexNames(
    (0, "DECHUB900-HRIP-MIB-V3-0", "hripSlotCfgIndex"),
)
if mibBuilder.loadTexts:
    hripPubSlotCfgEntry.setStatus("mandatory")


class _HripSlotCfgIndex_Type(Integer32):
    """Custom type hripSlotCfgIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HripSlotCfgIndex_Type.__name__ = "Integer32"
_HripSlotCfgIndex_Object = MibTableColumn
hripSlotCfgIndex = _HripSlotCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 2, 2, 1, 1),
    _HripSlotCfgIndex_Type()
)
hripSlotCfgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hripSlotCfgIndex.setStatus("mandatory")


class _HripSlotCfgDisable_Type(Integer32):
    """Custom type hripSlotCfgDisable based on Integer32"""
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
        *(("disabled-1", 2),
          ("disabled-4", 4),
          ("enabled-1", 1),
          ("enabled-2", 3))
    )


_HripSlotCfgDisable_Type.__name__ = "Integer32"
_HripSlotCfgDisable_Object = MibTableColumn
hripSlotCfgDisable = _HripSlotCfgDisable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 2, 2, 1, 2),
    _HripSlotCfgDisable_Type()
)
hripSlotCfgDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hripSlotCfgDisable.setStatus("mandatory")


class _HripSlotCfgForce_Type(Integer32):
    """Custom type hripSlotCfgForce based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("forceRingA-1", 2),
          ("forceRingA-2", 5),
          ("forceRingB-1", 3),
          ("forceRingB-2", 6),
          ("noForce-1", 1),
          ("noForce-2", 4))
    )


_HripSlotCfgForce_Type.__name__ = "Integer32"
_HripSlotCfgForce_Object = MibTableColumn
hripSlotCfgForce = _HripSlotCfgForce_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 2, 2, 1, 3),
    _HripSlotCfgForce_Type()
)
hripSlotCfgForce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hripSlotCfgForce.setStatus("mandatory")
_HripPubRingStatTable_Object = MibTable
hripPubRingStatTable = _HripPubRingStatTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 2, 3)
)
if mibBuilder.loadTexts:
    hripPubRingStatTable.setStatus("mandatory")
_HripPubRingStatEntry_Object = MibTableRow
hripPubRingStatEntry = _HripPubRingStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 2, 3, 1)
)
hripPubRingStatEntry.setIndexNames(
    (0, "DECHUB900-HRIP-MIB-V3-0", "hripRingStatIndex"),
)
if mibBuilder.loadTexts:
    hripPubRingStatEntry.setStatus("mandatory")


class _HripRingStatIndex_Type(Integer32):
    """Custom type hripRingStatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ringA", 1),
          ("ringB", 2))
    )


_HripRingStatIndex_Type.__name__ = "Integer32"
_HripRingStatIndex_Object = MibTableColumn
hripRingStatIndex = _HripRingStatIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 2, 3, 1, 1),
    _HripRingStatIndex_Type()
)
hripRingStatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hripRingStatIndex.setStatus("mandatory")


class _HripRingStatNumModInserted_Type(Integer32):
    """Custom type hripRingStatNumModInserted based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HripRingStatNumModInserted_Type.__name__ = "Integer32"
_HripRingStatNumModInserted_Object = MibTableColumn
hripRingStatNumModInserted = _HripRingStatNumModInserted_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 2, 3, 1, 2),
    _HripRingStatNumModInserted_Type()
)
hripRingStatNumModInserted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hripRingStatNumModInserted.setStatus("mandatory")
_HripPubSlotStatTable_Object = MibTable
hripPubSlotStatTable = _HripPubSlotStatTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 2, 4)
)
if mibBuilder.loadTexts:
    hripPubSlotStatTable.setStatus("mandatory")
_HripPubSlotStatEntry_Object = MibTableRow
hripPubSlotStatEntry = _HripPubSlotStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 2, 4, 1)
)
hripPubSlotStatEntry.setIndexNames(
    (0, "DECHUB900-HRIP-MIB-V3-0", "hripSlotStatIndex"),
)
if mibBuilder.loadTexts:
    hripPubSlotStatEntry.setStatus("mandatory")


class _HripSlotStatIndex_Type(Integer32):
    """Custom type hripSlotStatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_HripSlotStatIndex_Type.__name__ = "Integer32"
_HripSlotStatIndex_Object = MibTableColumn
hripSlotStatIndex = _HripSlotStatIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 2, 4, 1, 1),
    _HripSlotStatIndex_Type()
)
hripSlotStatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hripSlotStatIndex.setStatus("mandatory")
_HripSlotStatRingAInsertCount_Type = Gauge32
_HripSlotStatRingAInsertCount_Object = MibTableColumn
hripSlotStatRingAInsertCount = _HripSlotStatRingAInsertCount_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 2, 4, 1, 2),
    _HripSlotStatRingAInsertCount_Type()
)
hripSlotStatRingAInsertCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hripSlotStatRingAInsertCount.setStatus("mandatory")
_HripSlotStatRingBInsertCount_Type = Gauge32
_HripSlotStatRingBInsertCount_Object = MibTableColumn
hripSlotStatRingBInsertCount = _HripSlotStatRingBInsertCount_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 2, 4, 1, 3),
    _HripSlotStatRingBInsertCount_Type()
)
hripSlotStatRingBInsertCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hripSlotStatRingBInsertCount.setStatus("mandatory")


class _HripSlotStatTcuA_Type(Integer32):
    """Custom type hripSlotStatTcuA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inserted", 1),
          ("notTR", 3),
          ("wrapped", 2))
    )


_HripSlotStatTcuA_Type.__name__ = "Integer32"
_HripSlotStatTcuA_Object = MibTableColumn
hripSlotStatTcuA = _HripSlotStatTcuA_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 2, 4, 1, 4),
    _HripSlotStatTcuA_Type()
)
hripSlotStatTcuA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hripSlotStatTcuA.setStatus("mandatory")


class _HripSlotStatTcuB_Type(Integer32):
    """Custom type hripSlotStatTcuB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inserted", 1),
          ("notTR", 3),
          ("wrapped", 2))
    )


_HripSlotStatTcuB_Type.__name__ = "Integer32"
_HripSlotStatTcuB_Object = MibTableColumn
hripSlotStatTcuB = _HripSlotStatTcuB_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 2, 4, 1, 5),
    _HripSlotStatTcuB_Type()
)
hripSlotStatTcuB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hripSlotStatTcuB.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DECHUB900-HRIP-MIB-V3-0",
    **{"dec": dec,
       "ema": ema,
       "decMIBextension": decMIBextension,
       "decHub900": decHub900,
       "mgmtAgent": mgmtAgent,
       "mgmtAgentVersion1": mgmtAgentVersion1,
       "hrip": hrip,
       "hripPubRingCfgTable": hripPubRingCfgTable,
       "hripPubRingCfgEntry": hripPubRingCfgEntry,
       "hripRingCfgIndex": hripRingCfgIndex,
       "hripRingCfgSpeed": hripRingCfgSpeed,
       "hripPubSlotCfgTable": hripPubSlotCfgTable,
       "hripPubSlotCfgEntry": hripPubSlotCfgEntry,
       "hripSlotCfgIndex": hripSlotCfgIndex,
       "hripSlotCfgDisable": hripSlotCfgDisable,
       "hripSlotCfgForce": hripSlotCfgForce,
       "hripPubRingStatTable": hripPubRingStatTable,
       "hripPubRingStatEntry": hripPubRingStatEntry,
       "hripRingStatIndex": hripRingStatIndex,
       "hripRingStatNumModInserted": hripRingStatNumModInserted,
       "hripPubSlotStatTable": hripPubSlotStatTable,
       "hripPubSlotStatEntry": hripPubSlotStatEntry,
       "hripSlotStatIndex": hripSlotStatIndex,
       "hripSlotStatRingAInsertCount": hripSlotStatRingAInsertCount,
       "hripSlotStatRingBInsertCount": hripSlotStatRingBInsertCount,
       "hripSlotStatTcuA": hripSlotStatTcuA,
       "hripSlotStatTcuB": hripSlotStatTcuB}
)
