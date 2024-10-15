# SNMP MIB module (MICOMETHER) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MICOMETHER
# Produced by pysmi-1.5.4 at Mon Oct 14 22:21:54 2024
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

(micom_oscar,) = mibBuilder.importSymbols(
    "MICOM-OSCAR-MIB",
    "micom-oscar")

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

_McmEth_ObjectIdentity = ObjectIdentity
mcmEth = _McmEth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 10)
)
_McmEthCntr_ObjectIdentity = ObjectIdentity
mcmEthCntr = _McmEthCntr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 10, 1)
)
_McmEthCntrZeroTable_Object = MibTable
mcmEthCntrZeroTable = _McmEthCntrZeroTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 10, 1, 1)
)
if mibBuilder.loadTexts:
    mcmEthCntrZeroTable.setStatus("obsolete")
_McmEthCntrZeroEntry_Object = MibTableRow
mcmEthCntrZeroEntry = _McmEthCntrZeroEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 10, 1, 1, 1)
)
mcmEthCntrZeroEntry.setIndexNames(
    (0, "MICOMETHER", "mcmEthCntrZeroPort"),
)
if mibBuilder.loadTexts:
    mcmEthCntrZeroEntry.setStatus("obsolete")
_McmEthCntrZeroPort_Type = Integer32
_McmEthCntrZeroPort_Object = MibTableColumn
mcmEthCntrZeroPort = _McmEthCntrZeroPort_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 10, 1, 1, 1, 1),
    _McmEthCntrZeroPort_Type()
)
mcmEthCntrZeroPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmEthCntrZeroPort.setStatus("obsolete")


class _McmEthStatsGrpCounterZero_Type(Integer32):
    """Custom type mcmEthStatsGrpCounterZero based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 2),
          ("reset", 1))
    )


_McmEthStatsGrpCounterZero_Type.__name__ = "Integer32"
_McmEthStatsGrpCounterZero_Object = MibTableColumn
mcmEthStatsGrpCounterZero = _McmEthStatsGrpCounterZero_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 10, 1, 1, 1, 2),
    _McmEthStatsGrpCounterZero_Type()
)
mcmEthStatsGrpCounterZero.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mcmEthStatsGrpCounterZero.setStatus("obsolete")


class _McmEthCollStatsGrpCounterZero_Type(Integer32):
    """Custom type mcmEthCollStatsGrpCounterZero based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 2),
          ("reset", 1))
    )


_McmEthCollStatsGrpCounterZero_Type.__name__ = "Integer32"
_McmEthCollStatsGrpCounterZero_Object = MibTableColumn
mcmEthCollStatsGrpCounterZero = _McmEthCollStatsGrpCounterZero_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 10, 1, 1, 1, 3),
    _McmEthCollStatsGrpCounterZero_Type()
)
mcmEthCollStatsGrpCounterZero.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mcmEthCollStatsGrpCounterZero.setStatus("obsolete")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MICOMETHER",
    **{"mcmEth": mcmEth,
       "mcmEthCntr": mcmEthCntr,
       "mcmEthCntrZeroTable": mcmEthCntrZeroTable,
       "mcmEthCntrZeroEntry": mcmEthCntrZeroEntry,
       "mcmEthCntrZeroPort": mcmEthCntrZeroPort,
       "mcmEthStatsGrpCounterZero": mcmEthStatsGrpCounterZero,
       "mcmEthCollStatsGrpCounterZero": mcmEthCollStatsGrpCounterZero}
)
