# SNMP MIB module (Wellfleet-ARP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-ARP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:15:46 2024
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

(wfArpGroup,) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfArpGroup")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfArpBase_ObjectIdentity = ObjectIdentity
wfArpBase = _WfArpBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 1, 1)
)


class _WfArpBaseCreate_Type(Integer32):
    """Custom type wfArpBaseCreate based on Integer32"""
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


_WfArpBaseCreate_Type.__name__ = "Integer32"
_WfArpBaseCreate_Object = MibScalar
wfArpBaseCreate = _WfArpBaseCreate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 1, 1, 1),
    _WfArpBaseCreate_Type()
)
wfArpBaseCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfArpBaseCreate.setStatus("mandatory")


class _WfArpBaseEnable_Type(Integer32):
    """Custom type wfArpBaseEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfArpBaseEnable_Type.__name__ = "Integer32"
_WfArpBaseEnable_Object = MibScalar
wfArpBaseEnable = _WfArpBaseEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 1, 1, 2),
    _WfArpBaseEnable_Type()
)
wfArpBaseEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfArpBaseEnable.setStatus("mandatory")


class _WfArpBaseForwarding_Type(Integer32):
    """Custom type wfArpBaseForwarding based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forwarding", 1),
          ("notforwarding", 2))
    )


_WfArpBaseForwarding_Type.__name__ = "Integer32"
_WfArpBaseForwarding_Object = MibScalar
wfArpBaseForwarding = _WfArpBaseForwarding_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 1, 1, 3),
    _WfArpBaseForwarding_Type()
)
wfArpBaseForwarding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfArpBaseForwarding.setStatus("mandatory")


class _WfArpBaseNonlocalSrc_Type(Integer32):
    """Custom type wfArpBaseNonlocalSrc based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("drop", 2),
          ("log", 1))
    )


_WfArpBaseNonlocalSrc_Type.__name__ = "Integer32"
_WfArpBaseNonlocalSrc_Object = MibScalar
wfArpBaseNonlocalSrc = _WfArpBaseNonlocalSrc_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 1, 1, 4),
    _WfArpBaseNonlocalSrc_Type()
)
wfArpBaseNonlocalSrc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfArpBaseNonlocalSrc.setStatus("mandatory")


class _WfArpBaseNonlocalDest_Type(Integer32):
    """Custom type wfArpBaseNonlocalDest based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("accept", 2),
          ("drop", 1))
    )


_WfArpBaseNonlocalDest_Type.__name__ = "Integer32"
_WfArpBaseNonlocalDest_Object = MibScalar
wfArpBaseNonlocalDest = _WfArpBaseNonlocalDest_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 1, 1, 5),
    _WfArpBaseNonlocalDest_Type()
)
wfArpBaseNonlocalDest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfArpBaseNonlocalDest.setStatus("mandatory")
_WfArpIntfTable_Object = MibTable
wfArpIntfTable = _WfArpIntfTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 1, 2)
)
if mibBuilder.loadTexts:
    wfArpIntfTable.setStatus("mandatory")
_WfArpIntfEntry_Object = MibTableRow
wfArpIntfEntry = _WfArpIntfEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 1, 2, 1)
)
wfArpIntfEntry.setIndexNames(
    (0, "Wellfleet-ARP-MIB", "wfArpCctno"),
)
if mibBuilder.loadTexts:
    wfArpIntfEntry.setStatus("mandatory")


class _WfArpCreate_Type(Integer32):
    """Custom type wfArpCreate based on Integer32"""
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


_WfArpCreate_Type.__name__ = "Integer32"
_WfArpCreate_Object = MibTableColumn
wfArpCreate = _WfArpCreate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 1, 2, 1, 1),
    _WfArpCreate_Type()
)
wfArpCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfArpCreate.setStatus("mandatory")


class _WfArpEnable_Type(Integer32):
    """Custom type wfArpEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfArpEnable_Type.__name__ = "Integer32"
_WfArpEnable_Object = MibTableColumn
wfArpEnable = _WfArpEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 1, 2, 1, 2),
    _WfArpEnable_Type()
)
wfArpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfArpEnable.setStatus("mandatory")
_WfArpCctno_Type = Integer32
_WfArpCctno_Object = MibTableColumn
wfArpCctno = _WfArpCctno_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 1, 2, 1, 3),
    _WfArpCctno_Type()
)
wfArpCctno.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfArpCctno.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-ARP-MIB",
    **{"wfArpBase": wfArpBase,
       "wfArpBaseCreate": wfArpBaseCreate,
       "wfArpBaseEnable": wfArpBaseEnable,
       "wfArpBaseForwarding": wfArpBaseForwarding,
       "wfArpBaseNonlocalSrc": wfArpBaseNonlocalSrc,
       "wfArpBaseNonlocalDest": wfArpBaseNonlocalDest,
       "wfArpIntfTable": wfArpIntfTable,
       "wfArpIntfEntry": wfArpIntfEntry,
       "wfArpCreate": wfArpCreate,
       "wfArpEnable": wfArpEnable,
       "wfArpCctno": wfArpCctno}
)
