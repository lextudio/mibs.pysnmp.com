# SNMP MIB module (NETWORK-ALCHEMY-CONFIG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NETWORK-ALCHEMY-CONFIG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:27:16 2024
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

(config,
 netalModules) = mibBuilder.importSymbols(
    "NETAL-SMI",
    "config",
    "netalModules")

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

networkAlchemyConfigMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2972, 5, 6)
)
networkAlchemyConfigMIB.setRevisions(
        ("1900-08-30 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _ConfigDirtyBit_Type(Integer32):
    """Custom type configDirtyBit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_ConfigDirtyBit_Type.__name__ = "Integer32"
_ConfigDirtyBit_Object = MibScalar
configDirtyBit = _ConfigDirtyBit_Object(
    (1, 3, 6, 1, 4, 1, 2972, 2, 5, 1),
    _ConfigDirtyBit_Type()
)
configDirtyBit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configDirtyBit.setStatus("current")


class _ConfigCommit_Type(Integer32):
    """Custom type configCommit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_ConfigCommit_Type.__name__ = "Integer32"
_ConfigCommit_Object = MibScalar
configCommit = _ConfigCommit_Object(
    (1, 3, 6, 1, 4, 1, 2972, 2, 5, 2),
    _ConfigCommit_Type()
)
configCommit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configCommit.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NETWORK-ALCHEMY-CONFIG-MIB",
    **{"configDirtyBit": configDirtyBit,
       "configCommit": configCommit,
       "networkAlchemyConfigMIB": networkAlchemyConfigMIB}
)
