# SNMP MIB module (XYLAN-SONET-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/XYLAN-SONET-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:19:15 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

(xylanSonetArch,) = mibBuilder.importSymbols(
    "XYLAN-BASE-MIB",
    "xylanSonetArch")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_XylanSonetErrConfig_ObjectIdentity = ObjectIdentity
xylanSonetErrConfig = _XylanSonetErrConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 23, 1)
)
_XylanSonetTable_Object = MibTable
xylanSonetTable = _XylanSonetTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 23, 1, 1)
)
if mibBuilder.loadTexts:
    xylanSonetTable.setStatus("mandatory")
_XylanSonetEntry_Object = MibTableRow
xylanSonetEntry = _XylanSonetEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 23, 1, 1, 1)
)
xylanSonetEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    xylanSonetEntry.setStatus("mandatory")


class _XylanSonetStatsEnable_Type(Integer32):
    """Custom type xylanSonetStatsEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_XylanSonetStatsEnable_Type.__name__ = "Integer32"
_XylanSonetStatsEnable_Object = MibTableColumn
xylanSonetStatsEnable = _XylanSonetStatsEnable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 23, 1, 1, 1, 1),
    _XylanSonetStatsEnable_Type()
)
xylanSonetStatsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanSonetStatsEnable.setStatus("mandatory")


class _XylanSonetNumOfSamples_Type(Integer32):
    """Custom type xylanSonetNumOfSamples based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 96),
    )


_XylanSonetNumOfSamples_Type.__name__ = "Integer32"
_XylanSonetNumOfSamples_Object = MibTableColumn
xylanSonetNumOfSamples = _XylanSonetNumOfSamples_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 23, 1, 1, 1, 2),
    _XylanSonetNumOfSamples_Type()
)
xylanSonetNumOfSamples.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanSonetNumOfSamples.setStatus("mandatory")


class _XylanSonetClearCurrentSample_Type(Integer32):
    """Custom type xylanSonetClearCurrentSample based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_XylanSonetClearCurrentSample_Type.__name__ = "Integer32"
_XylanSonetClearCurrentSample_Object = MibTableColumn
xylanSonetClearCurrentSample = _XylanSonetClearCurrentSample_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 23, 1, 1, 1, 3),
    _XylanSonetClearCurrentSample_Type()
)
xylanSonetClearCurrentSample.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanSonetClearCurrentSample.setStatus("mandatory")
_XylanSonetErrGroup_ObjectIdentity = ObjectIdentity
xylanSonetErrGroup = _XylanSonetErrGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 23, 3)
)


class _XylanSonetSlotIndex_Type(Integer32):
    """Custom type xylanSonetSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_XylanSonetSlotIndex_Type.__name__ = "Integer32"
_XylanSonetSlotIndex_Object = MibScalar
xylanSonetSlotIndex = _XylanSonetSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 23, 3, 1),
    _XylanSonetSlotIndex_Type()
)
xylanSonetSlotIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xylanSonetSlotIndex.setStatus("mandatory")


class _XylanSonetPortIndex_Type(Integer32):
    """Custom type xylanSonetPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_XylanSonetPortIndex_Type.__name__ = "Integer32"
_XylanSonetPortIndex_Object = MibScalar
xylanSonetPortIndex = _XylanSonetPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 23, 3, 2),
    _XylanSonetPortIndex_Type()
)
xylanSonetPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xylanSonetPortIndex.setStatus("mandatory")
_XylanSonetHardwareIndex_Type = Integer32
_XylanSonetHardwareIndex_Object = MibScalar
xylanSonetHardwareIndex = _XylanSonetHardwareIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 23, 3, 3),
    _XylanSonetHardwareIndex_Type()
)
xylanSonetHardwareIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xylanSonetHardwareIndex.setStatus("mandatory")
_XylanSonetErrType_Type = Integer32
_XylanSonetErrType_Object = MibScalar
xylanSonetErrType = _XylanSonetErrType_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 23, 3, 4),
    _XylanSonetErrType_Type()
)
xylanSonetErrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xylanSonetErrType.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XYLAN-SONET-MIB",
    **{"xylanSonetErrConfig": xylanSonetErrConfig,
       "xylanSonetTable": xylanSonetTable,
       "xylanSonetEntry": xylanSonetEntry,
       "xylanSonetStatsEnable": xylanSonetStatsEnable,
       "xylanSonetNumOfSamples": xylanSonetNumOfSamples,
       "xylanSonetClearCurrentSample": xylanSonetClearCurrentSample,
       "xylanSonetErrGroup": xylanSonetErrGroup,
       "xylanSonetSlotIndex": xylanSonetSlotIndex,
       "xylanSonetPortIndex": xylanSonetPortIndex,
       "xylanSonetHardwareIndex": xylanSonetHardwareIndex,
       "xylanSonetErrType": xylanSonetErrType}
)
