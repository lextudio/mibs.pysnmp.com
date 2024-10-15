# SNMP MIB module (CISCOSB-WeightedRandomTailDrop-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCOSB-WeightedRandomTailDrop-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:15:12 2024
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

(switch001,) = mibBuilder.importSymbols(
    "CISCOSB-MIB",
    "switch001")

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

rlWeightedRandomTailDrop = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 146)
)
rlWeightedRandomTailDrop.setRevisions(
        ("2009-09-29 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _RlWeightedRandomTailDropCurrentStatus_Type(Integer32):
    """Custom type rlWeightedRandomTailDropCurrentStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 0))
    )


_RlWeightedRandomTailDropCurrentStatus_Type.__name__ = "Integer32"
_RlWeightedRandomTailDropCurrentStatus_Object = MibScalar
rlWeightedRandomTailDropCurrentStatus = _RlWeightedRandomTailDropCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 146, 1),
    _RlWeightedRandomTailDropCurrentStatus_Type()
)
rlWeightedRandomTailDropCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlWeightedRandomTailDropCurrentStatus.setStatus("current")


class _RlWeightedRandomTailDropStatusAfterReset_Type(Integer32):
    """Custom type rlWeightedRandomTailDropStatusAfterReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 0))
    )


_RlWeightedRandomTailDropStatusAfterReset_Type.__name__ = "Integer32"
_RlWeightedRandomTailDropStatusAfterReset_Object = MibScalar
rlWeightedRandomTailDropStatusAfterReset = _RlWeightedRandomTailDropStatusAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 146, 2),
    _RlWeightedRandomTailDropStatusAfterReset_Type()
)
rlWeightedRandomTailDropStatusAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlWeightedRandomTailDropStatusAfterReset.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCOSB-WeightedRandomTailDrop-MIB",
    **{"rlWeightedRandomTailDrop": rlWeightedRandomTailDrop,
       "rlWeightedRandomTailDropCurrentStatus": rlWeightedRandomTailDropCurrentStatus,
       "rlWeightedRandomTailDropStatusAfterReset": rlWeightedRandomTailDropStatusAfterReset}
)
