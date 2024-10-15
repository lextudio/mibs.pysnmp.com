# SNMP MIB module (Wellfleet-NPK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-NPK-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:16:48 2024
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

(wfGameGroup,) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfGameGroup")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfNpkBase_ObjectIdentity = ObjectIdentity
wfNpkBase = _WfNpkBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 8)
)


class _WfNpkBaseCreate_Type(Integer32):
    """Custom type wfNpkBaseCreate based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfNpkBaseCreate_Type.__name__ = "Integer32"
_WfNpkBaseCreate_Object = MibScalar
wfNpkBaseCreate = _WfNpkBaseCreate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 8, 1),
    _WfNpkBaseCreate_Type()
)
wfNpkBaseCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNpkBaseCreate.setStatus("mandatory")
_WfNpkBaseHash_Type = OctetString
_WfNpkBaseHash_Object = MibScalar
wfNpkBaseHash = _WfNpkBaseHash_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 8, 2),
    _WfNpkBaseHash_Type()
)
wfNpkBaseHash.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNpkBaseHash.setStatus("mandatory")
_WfNpkBaseLastMod_Type = DisplayString
_WfNpkBaseLastMod_Object = MibScalar
wfNpkBaseLastMod = _WfNpkBaseLastMod_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 8, 3),
    _WfNpkBaseLastMod_Type()
)
wfNpkBaseLastMod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNpkBaseLastMod.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-NPK-MIB",
    **{"wfNpkBase": wfNpkBase,
       "wfNpkBaseCreate": wfNpkBaseCreate,
       "wfNpkBaseHash": wfNpkBaseHash,
       "wfNpkBaseLastMod": wfNpkBaseLastMod}
)
