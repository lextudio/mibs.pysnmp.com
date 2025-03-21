# SNMP MIB module (RADLAN-JUMBOFRAMES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RADLAN-JUMBOFRAMES-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:42:33 2024
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

(rnd,) = mibBuilder.importSymbols(
    "RADLAN-MIB",
    "rnd")

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

rlJumboFrames = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 89, 91)
)
rlJumboFrames.setRevisions(
        ("2007-01-02 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _RlJumboFramesCurrentStatus_Type(Integer32):
    """Custom type rlJumboFramesCurrentStatus based on Integer32"""
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


_RlJumboFramesCurrentStatus_Type.__name__ = "Integer32"
_RlJumboFramesCurrentStatus_Object = MibScalar
rlJumboFramesCurrentStatus = _RlJumboFramesCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 91, 1),
    _RlJumboFramesCurrentStatus_Type()
)
rlJumboFramesCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlJumboFramesCurrentStatus.setStatus("current")


class _RlJumboFramesStatusAfterReset_Type(Integer32):
    """Custom type rlJumboFramesStatusAfterReset based on Integer32"""
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


_RlJumboFramesStatusAfterReset_Type.__name__ = "Integer32"
_RlJumboFramesStatusAfterReset_Object = MibScalar
rlJumboFramesStatusAfterReset = _RlJumboFramesStatusAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 91, 2),
    _RlJumboFramesStatusAfterReset_Type()
)
rlJumboFramesStatusAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlJumboFramesStatusAfterReset.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RADLAN-JUMBOFRAMES-MIB",
    **{"rlJumboFrames": rlJumboFrames,
       "rlJumboFramesCurrentStatus": rlJumboFramesCurrentStatus,
       "rlJumboFramesStatusAfterReset": rlJumboFramesStatusAfterReset}
)
