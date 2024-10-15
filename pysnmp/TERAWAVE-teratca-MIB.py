# SNMP MIB module (TERAWAVE-teratca-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TERAWAVE-teratca-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:01:25 2024
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
_Teratraps_ObjectIdentity = ObjectIdentity
teratraps = _Teratraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4513, 1)
)
_TeraTCA_ObjectIdentity = ObjectIdentity
teraTCA = _TeraTCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4513, 1, 4)
)
_TeraTcaTable_Object = MibTable
teraTcaTable = _TeraTcaTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 4, 1)
)
if mibBuilder.loadTexts:
    teraTcaTable.setStatus("mandatory")
_TeraTcaTableEntry_Object = MibTableRow
teraTcaTableEntry = _TeraTcaTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 4, 1, 1)
)
teraTcaTableEntry.setIndexNames(
    (0, "TERAWAVE-teratca-MIB", "teraTcaIndex"),
)
if mibBuilder.loadTexts:
    teraTcaTableEntry.setStatus("mandatory")
_TeraTcaIndex_Type = Integer32
_TeraTcaIndex_Object = MibTableColumn
teraTcaIndex = _TeraTcaIndex_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 4, 1, 1, 1),
    _TeraTcaIndex_Type()
)
teraTcaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraTcaIndex.setStatus("mandatory")


class _TeraTcaInterval_Type(Integer32):
    """Custom type teraTcaInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("duration-15m", 1),
          ("duration-1day", 2),
          ("duration-Var", 3))
    )


_TeraTcaInterval_Type.__name__ = "Integer32"
_TeraTcaInterval_Object = MibTableColumn
teraTcaInterval = _TeraTcaInterval_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 4, 1, 1, 2),
    _TeraTcaInterval_Type()
)
teraTcaInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraTcaInterval.setStatus("mandatory")
_TeraTcaVariable_Type = ObjectIdentifier
_TeraTcaVariable_Object = MibTableColumn
teraTcaVariable = _TeraTcaVariable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 4, 1, 1, 3),
    _TeraTcaVariable_Type()
)
teraTcaVariable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraTcaVariable.setStatus("mandatory")
_TeraTcaIntervalSec_Type = Integer32
_TeraTcaIntervalSec_Object = MibTableColumn
teraTcaIntervalSec = _TeraTcaIntervalSec_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 4, 1, 1, 4),
    _TeraTcaIntervalSec_Type()
)
teraTcaIntervalSec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraTcaIntervalSec.setStatus("mandatory")
_TeraTcaValue_Type = Integer32
_TeraTcaValue_Object = MibTableColumn
teraTcaValue = _TeraTcaValue_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 4, 1, 1, 5),
    _TeraTcaValue_Type()
)
teraTcaValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraTcaValue.setStatus("mandatory")


class _TeraTcaType_Type(Integer32):
    """Custom type teraTcaType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fallingTca", 2),
          ("risingOrFalingTca", 3),
          ("risingTca", 1))
    )


_TeraTcaType_Type.__name__ = "Integer32"
_TeraTcaType_Object = MibTableColumn
teraTcaType = _TeraTcaType_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 4, 1, 1, 6),
    _TeraTcaType_Type()
)
teraTcaType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraTcaType.setStatus("mandatory")
_TeraTcaRisingThreshold_Type = Integer32
_TeraTcaRisingThreshold_Object = MibTableColumn
teraTcaRisingThreshold = _TeraTcaRisingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 4, 1, 1, 7),
    _TeraTcaRisingThreshold_Type()
)
teraTcaRisingThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraTcaRisingThreshold.setStatus("mandatory")
_TeraTcaFallingThreshold_Type = Integer32
_TeraTcaFallingThreshold_Object = MibTableColumn
teraTcaFallingThreshold = _TeraTcaFallingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 4, 1, 1, 8),
    _TeraTcaFallingThreshold_Type()
)
teraTcaFallingThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraTcaFallingThreshold.setStatus("mandatory")


class _TeraTcaRisingEvent_Type(Integer32):
    """Custom type teraTcaRisingEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("tcaIgnore", 3),
          ("tcaLog", 2),
          ("tcaTrap", 1))
    )


_TeraTcaRisingEvent_Type.__name__ = "Integer32"
_TeraTcaRisingEvent_Object = MibTableColumn
teraTcaRisingEvent = _TeraTcaRisingEvent_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 4, 1, 1, 9),
    _TeraTcaRisingEvent_Type()
)
teraTcaRisingEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraTcaRisingEvent.setStatus("mandatory")


class _TeraTcaFallingEvent_Type(Integer32):
    """Custom type teraTcaFallingEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("tcaIgnore", 3),
          ("tcaLog", 2),
          ("tcaTrap", 1))
    )


_TeraTcaFallingEvent_Type.__name__ = "Integer32"
_TeraTcaFallingEvent_Object = MibTableColumn
teraTcaFallingEvent = _TeraTcaFallingEvent_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 4, 1, 1, 10),
    _TeraTcaFallingEvent_Type()
)
teraTcaFallingEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraTcaFallingEvent.setStatus("mandatory")
_TeraTcaOwner_Type = OctetString
_TeraTcaOwner_Object = MibTableColumn
teraTcaOwner = _TeraTcaOwner_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 4, 1, 1, 11),
    _TeraTcaOwner_Type()
)
teraTcaOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraTcaOwner.setStatus("mandatory")


class _TeraTcaStatus_Type(Integer32):
    """Custom type teraTcaStatus based on Integer32"""
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
        *(("createdRequest", 2),
          ("invalid", 4),
          ("underCreation", 3),
          ("valid", 1))
    )


_TeraTcaStatus_Type.__name__ = "Integer32"
_TeraTcaStatus_Object = MibTableColumn
teraTcaStatus = _TeraTcaStatus_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 4, 1, 1, 12),
    _TeraTcaStatus_Type()
)
teraTcaStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraTcaStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TERAWAVE-teratca-MIB",
    **{"terawave": terawave,
       "teratraps": teratraps,
       "teraTCA": teraTCA,
       "teraTcaTable": teraTcaTable,
       "teraTcaTableEntry": teraTcaTableEntry,
       "teraTcaIndex": teraTcaIndex,
       "teraTcaInterval": teraTcaInterval,
       "teraTcaVariable": teraTcaVariable,
       "teraTcaIntervalSec": teraTcaIntervalSec,
       "teraTcaValue": teraTcaValue,
       "teraTcaType": teraTcaType,
       "teraTcaRisingThreshold": teraTcaRisingThreshold,
       "teraTcaFallingThreshold": teraTcaFallingThreshold,
       "teraTcaRisingEvent": teraTcaRisingEvent,
       "teraTcaFallingEvent": teraTcaFallingEvent,
       "teraTcaOwner": teraTcaOwner,
       "teraTcaStatus": teraTcaStatus}
)
