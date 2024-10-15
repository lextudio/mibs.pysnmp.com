# SNMP MIB module (ACC-DSX) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ACC-DSX
# Produced by pysmi-1.5.4 at Mon Oct 14 20:32:09 2024
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

(accBRG,) = mibBuilder.importSymbols(
    "ACC-MIB",
    "accBRG")

(accTrapLogSeqNum,) = mibBuilder.importSymbols(
    "ACC-SYSTEM",
    "accTrapLogSeqNum")

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

_AccDsx_ObjectIdentity = ObjectIdentity
accDsx = _AccDsx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 90)
)
_AccDsxParmTable_ObjectIdentity = ObjectIdentity
accDsxParmTable = _AccDsxParmTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 90, 1)
)
_AccDsxParmEntry_ObjectIdentity = ObjectIdentity
accDsxParmEntry = _AccDsxParmEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 90, 1, 1)
)


class _AccPstnDs1InCompandMode_Type(Integer32):
    """Custom type accPstnDs1InCompandMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alaw", 2),
          ("ulaw", 1))
    )


_AccPstnDs1InCompandMode_Type.__name__ = "Integer32"
_AccPstnDs1InCompandMode_Object = MibScalar
accPstnDs1InCompandMode = _AccPstnDs1InCompandMode_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 90, 1, 1, 1),
    _AccPstnDs1InCompandMode_Type()
)
accPstnDs1InCompandMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPstnDs1InCompandMode.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ACC-DSX",
    **{"accDsx": accDsx,
       "accDsxParmTable": accDsxParmTable,
       "accDsxParmEntry": accDsxParmEntry,
       "accPstnDs1InCompandMode": accPstnDs1InCompandMode}
)
