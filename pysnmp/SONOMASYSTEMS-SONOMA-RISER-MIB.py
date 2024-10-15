# SNMP MIB module (SONOMASYSTEMS-SONOMA-RISER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SONOMASYSTEMS-SONOMA-RISER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:56:46 2024
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

(sonomaSeries,) = mibBuilder.importSymbols(
    "SONOMASYSTEMS-SONOMA-MIB",
    "sonomaSeries")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SonomaRiser_ObjectIdentity = ObjectIdentity
sonomaRiser = _SonomaRiser_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2926, 25, 12)
)
_RiserFanTable_Object = MibTable
riserFanTable = _RiserFanTable_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 12, 1)
)
if mibBuilder.loadTexts:
    riserFanTable.setStatus("mandatory")
_RiserFanEntry_Object = MibTableRow
riserFanEntry = _RiserFanEntry_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 12, 1, 1)
)
riserFanEntry.setIndexNames(
    (0, "SONOMASYSTEMS-SONOMA-RISER-MIB", "riserFanIndex"),
)
if mibBuilder.loadTexts:
    riserFanEntry.setStatus("mandatory")
_RiserFanIndex_Type = Integer32
_RiserFanIndex_Object = MibTableColumn
riserFanIndex = _RiserFanIndex_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 12, 1, 1, 1),
    _RiserFanIndex_Type()
)
riserFanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riserFanIndex.setStatus("mandatory")


class _RiserFanStatus_Type(Integer32):
    """Custom type riserFanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fail", 2),
          ("ok", 1))
    )


_RiserFanStatus_Type.__name__ = "Integer32"
_RiserFanStatus_Object = MibTableColumn
riserFanStatus = _RiserFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 12, 1, 1, 2),
    _RiserFanStatus_Type()
)
riserFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riserFanStatus.setStatus("mandatory")
_ThermalGroup_ObjectIdentity = ObjectIdentity
thermalGroup = _ThermalGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2926, 25, 12, 2)
)
_RiserTemperatureC_Type = Integer32
_RiserTemperatureC_Object = MibScalar
riserTemperatureC = _RiserTemperatureC_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 12, 2, 1),
    _RiserTemperatureC_Type()
)
riserTemperatureC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riserTemperatureC.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SONOMASYSTEMS-SONOMA-RISER-MIB",
    **{"sonomaRiser": sonomaRiser,
       "riserFanTable": riserFanTable,
       "riserFanEntry": riserFanEntry,
       "riserFanIndex": riserFanIndex,
       "riserFanStatus": riserFanStatus,
       "thermalGroup": thermalGroup,
       "riserTemperatureC": riserTemperatureC}
)
