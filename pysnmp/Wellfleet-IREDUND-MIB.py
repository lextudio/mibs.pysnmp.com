# SNMP MIB module (Wellfleet-IREDUND-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-IREDUND-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:16:32 2024
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

(wfIRedundGroup,) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfIRedundGroup")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfIRedundIfTable_Object = MibTable
wfIRedundIfTable = _WfIRedundIfTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 10, 1)
)
if mibBuilder.loadTexts:
    wfIRedundIfTable.setStatus("mandatory")
_WfIRedundIfEntry_Object = MibTableRow
wfIRedundIfEntry = _WfIRedundIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 10, 1, 1)
)
wfIRedundIfEntry.setIndexNames(
    (0, "Wellfleet-IREDUND-MIB", "wfIRedundIfSlot"),
    (0, "Wellfleet-IREDUND-MIB", "wfIRedundIfPort"),
)
if mibBuilder.loadTexts:
    wfIRedundIfEntry.setStatus("mandatory")


class _WfIRedundIfDelete_Type(Integer32):
    """Custom type wfIRedundIfDelete based on Integer32"""
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


_WfIRedundIfDelete_Type.__name__ = "Integer32"
_WfIRedundIfDelete_Object = MibTableColumn
wfIRedundIfDelete = _WfIRedundIfDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 10, 1, 1, 1),
    _WfIRedundIfDelete_Type()
)
wfIRedundIfDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIRedundIfDelete.setStatus("mandatory")


class _WfIRedundIfDisable_Type(Integer32):
    """Custom type wfIRedundIfDisable based on Integer32"""
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


_WfIRedundIfDisable_Type.__name__ = "Integer32"
_WfIRedundIfDisable_Object = MibTableColumn
wfIRedundIfDisable = _WfIRedundIfDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 10, 1, 1, 2),
    _WfIRedundIfDisable_Type()
)
wfIRedundIfDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIRedundIfDisable.setStatus("mandatory")


class _WfIRedundIfCct_Type(Integer32):
    """Custom type wfIRedundIfCct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_WfIRedundIfCct_Type.__name__ = "Integer32"
_WfIRedundIfCct_Object = MibTableColumn
wfIRedundIfCct = _WfIRedundIfCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 10, 1, 1, 3),
    _WfIRedundIfCct_Type()
)
wfIRedundIfCct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIRedundIfCct.setStatus("mandatory")


class _WfIRedundIfSlot_Type(Integer32):
    """Custom type wfIRedundIfSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_WfIRedundIfSlot_Type.__name__ = "Integer32"
_WfIRedundIfSlot_Object = MibTableColumn
wfIRedundIfSlot = _WfIRedundIfSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 10, 1, 1, 4),
    _WfIRedundIfSlot_Type()
)
wfIRedundIfSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIRedundIfSlot.setStatus("mandatory")


class _WfIRedundIfPort_Type(Integer32):
    """Custom type wfIRedundIfPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 44),
    )


_WfIRedundIfPort_Type.__name__ = "Integer32"
_WfIRedundIfPort_Object = MibTableColumn
wfIRedundIfPort = _WfIRedundIfPort_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 10, 1, 1, 5),
    _WfIRedundIfPort_Type()
)
wfIRedundIfPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIRedundIfPort.setStatus("mandatory")


class _WfIRedundIfPrimary_Type(Integer32):
    """Custom type wfIRedundIfPrimary based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nonprimary", 2),
          ("primary", 1))
    )


_WfIRedundIfPrimary_Type.__name__ = "Integer32"
_WfIRedundIfPrimary_Object = MibTableColumn
wfIRedundIfPrimary = _WfIRedundIfPrimary_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 10, 1, 1, 6),
    _WfIRedundIfPrimary_Type()
)
wfIRedundIfPrimary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIRedundIfPrimary.setStatus("mandatory")


class _WfIRedundIfActive_Type(Integer32):
    """Custom type wfIRedundIfActive based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 3),
          ("notavailable", 1),
          ("standby", 2))
    )


_WfIRedundIfActive_Type.__name__ = "Integer32"
_WfIRedundIfActive_Object = MibTableColumn
wfIRedundIfActive = _WfIRedundIfActive_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 10, 1, 1, 7),
    _WfIRedundIfActive_Type()
)
wfIRedundIfActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIRedundIfActive.setStatus("mandatory")
_WfIRedundIfMACAddr_Type = OctetString
_WfIRedundIfMACAddr_Object = MibTableColumn
wfIRedundIfMACAddr = _WfIRedundIfMACAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 10, 1, 1, 8),
    _WfIRedundIfMACAddr_Type()
)
wfIRedundIfMACAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIRedundIfMACAddr.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-IREDUND-MIB",
    **{"wfIRedundIfTable": wfIRedundIfTable,
       "wfIRedundIfEntry": wfIRedundIfEntry,
       "wfIRedundIfDelete": wfIRedundIfDelete,
       "wfIRedundIfDisable": wfIRedundIfDisable,
       "wfIRedundIfCct": wfIRedundIfCct,
       "wfIRedundIfSlot": wfIRedundIfSlot,
       "wfIRedundIfPort": wfIRedundIfPort,
       "wfIRedundIfPrimary": wfIRedundIfPrimary,
       "wfIRedundIfActive": wfIRedundIfActive,
       "wfIRedundIfMACAddr": wfIRedundIfMACAddr}
)
