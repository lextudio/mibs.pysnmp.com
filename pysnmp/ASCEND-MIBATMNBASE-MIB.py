# SNMP MIB module (ASCEND-MIBATMNBASE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MIBATMNBASE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:41:08 2024
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

(configuration,) = mibBuilder.importSymbols(
    "ASCEND-MIB",
    "configuration")

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



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MibatmNbaseProfile_ObjectIdentity = ObjectIdentity
mibatmNbaseProfile = _MibatmNbaseProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 41)
)
_MibatmNbaseProfileTable_Object = MibTable
mibatmNbaseProfileTable = _MibatmNbaseProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 41, 1)
)
if mibBuilder.loadTexts:
    mibatmNbaseProfileTable.setStatus("mandatory")
_MibatmNbaseProfileEntry_Object = MibTableRow
mibatmNbaseProfileEntry = _MibatmNbaseProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 41, 1, 1)
)
mibatmNbaseProfileEntry.setIndexNames(
    (0, "ASCEND-MIBATMNBASE-MIB", "atmNbaseProfile-Index-o"),
)
if mibBuilder.loadTexts:
    mibatmNbaseProfileEntry.setStatus("mandatory")
_AtmNbaseProfile_Index_o_Type = Integer32
_AtmNbaseProfile_Index_o_Object = MibScalar
atmNbaseProfile_Index_o = _AtmNbaseProfile_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 41, 1, 1, 1),
    _AtmNbaseProfile_Index_o_Type()
)
atmNbaseProfile_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmNbaseProfile_Index_o.setStatus("mandatory")
_AtmNbaseProfile_RandSeed_Type = Integer32
_AtmNbaseProfile_RandSeed_Object = MibScalar
atmNbaseProfile_RandSeed = _AtmNbaseProfile_RandSeed_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 41, 1, 1, 6),
    _AtmNbaseProfile_RandSeed_Type()
)
atmNbaseProfile_RandSeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmNbaseProfile_RandSeed.setStatus("mandatory")


class _AtmNbaseProfile_Action_o_Type(Integer32):
    """Custom type atmNbaseProfile_Action_o based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("createProfile", 2),
          ("deleteProfile", 3),
          ("noAction", 1))
    )


_AtmNbaseProfile_Action_o_Type.__name__ = "Integer32"
_AtmNbaseProfile_Action_o_Object = MibScalar
atmNbaseProfile_Action_o = _AtmNbaseProfile_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 41, 1, 1, 16),
    _AtmNbaseProfile_Action_o_Type()
)
atmNbaseProfile_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmNbaseProfile_Action_o.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MIBATMNBASE-MIB",
    **{"DisplayString": DisplayString,
       "mibatmNbaseProfile": mibatmNbaseProfile,
       "mibatmNbaseProfileTable": mibatmNbaseProfileTable,
       "mibatmNbaseProfileEntry": mibatmNbaseProfileEntry,
       "atmNbaseProfile-Index-o": atmNbaseProfile_Index_o,
       "atmNbaseProfile-RandSeed": atmNbaseProfile_RandSeed,
       "atmNbaseProfile-Action-o": atmNbaseProfile_Action_o}
)
