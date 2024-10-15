# SNMP MIB module (Wellfleet-IFWALL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-IFWALL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:16:23 2024
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

(wfFwallGroup,) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfFwallGroup")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfIFwallIfTable_Object = MibTable
wfIFwallIfTable = _WfIFwallIfTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 11, 1)
)
if mibBuilder.loadTexts:
    wfIFwallIfTable.setStatus("obsolete")
_WfIFwallIfEntry_Object = MibTableRow
wfIFwallIfEntry = _WfIFwallIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 11, 1, 1)
)
wfIFwallIfEntry.setIndexNames(
    (0, "Wellfleet-IFWALL-MIB", "wfIFwallIfSlot"),
    (0, "Wellfleet-IFWALL-MIB", "wfIFwallIfPort"),
)
if mibBuilder.loadTexts:
    wfIFwallIfEntry.setStatus("obsolete")


class _WfIFwallIfDelete_Type(Integer32):
    """Custom type wfIFwallIfDelete based on Integer32"""
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


_WfIFwallIfDelete_Type.__name__ = "Integer32"
_WfIFwallIfDelete_Object = MibTableColumn
wfIFwallIfDelete = _WfIFwallIfDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 11, 1, 1, 1),
    _WfIFwallIfDelete_Type()
)
wfIFwallIfDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIFwallIfDelete.setStatus("obsolete")


class _WfIFwallIfDisable_Type(Integer32):
    """Custom type wfIFwallIfDisable based on Integer32"""
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


_WfIFwallIfDisable_Type.__name__ = "Integer32"
_WfIFwallIfDisable_Object = MibTableColumn
wfIFwallIfDisable = _WfIFwallIfDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 11, 1, 1, 2),
    _WfIFwallIfDisable_Type()
)
wfIFwallIfDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIFwallIfDisable.setStatus("obsolete")


class _WfIFwallIfCct_Type(Integer32):
    """Custom type wfIFwallIfCct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_WfIFwallIfCct_Type.__name__ = "Integer32"
_WfIFwallIfCct_Object = MibTableColumn
wfIFwallIfCct = _WfIFwallIfCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 11, 1, 1, 3),
    _WfIFwallIfCct_Type()
)
wfIFwallIfCct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIFwallIfCct.setStatus("obsolete")


class _WfIFwallIfSlot_Type(Integer32):
    """Custom type wfIFwallIfSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_WfIFwallIfSlot_Type.__name__ = "Integer32"
_WfIFwallIfSlot_Object = MibTableColumn
wfIFwallIfSlot = _WfIFwallIfSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 11, 1, 1, 4),
    _WfIFwallIfSlot_Type()
)
wfIFwallIfSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIFwallIfSlot.setStatus("obsolete")


class _WfIFwallIfPort_Type(Integer32):
    """Custom type wfIFwallIfPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 44),
    )


_WfIFwallIfPort_Type.__name__ = "Integer32"
_WfIFwallIfPort_Object = MibTableColumn
wfIFwallIfPort = _WfIFwallIfPort_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 11, 1, 1, 5),
    _WfIFwallIfPort_Type()
)
wfIFwallIfPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIFwallIfPort.setStatus("obsolete")
_WfIFwallIfLineNumber_Type = Integer32
_WfIFwallIfLineNumber_Object = MibTableColumn
wfIFwallIfLineNumber = _WfIFwallIfLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 11, 1, 1, 6),
    _WfIFwallIfLineNumber_Type()
)
wfIFwallIfLineNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIFwallIfLineNumber.setStatus("obsolete")


class _WfIFwallIfName_Type(DisplayString):
    """Custom type wfIFwallIfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_WfIFwallIfName_Type.__name__ = "DisplayString"
_WfIFwallIfName_Object = MibTableColumn
wfIFwallIfName = _WfIFwallIfName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 11, 1, 1, 7),
    _WfIFwallIfName_Type()
)
wfIFwallIfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIFwallIfName.setStatus("obsolete")
_WfFwallIntfTable_Object = MibTable
wfFwallIntfTable = _WfFwallIntfTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 11, 3)
)
if mibBuilder.loadTexts:
    wfFwallIntfTable.setStatus("mandatory")
_WfFwallIntfEntry_Object = MibTableRow
wfFwallIntfEntry = _WfFwallIntfEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 11, 3, 1)
)
wfFwallIntfEntry.setIndexNames(
    (0, "Wellfleet-IFWALL-MIB", "wfFwallIntfCct"),
)
if mibBuilder.loadTexts:
    wfFwallIntfEntry.setStatus("mandatory")


class _WfFwallIntfDelete_Type(Integer32):
    """Custom type wfFwallIntfDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("delete", 2))
    )


_WfFwallIntfDelete_Type.__name__ = "Integer32"
_WfFwallIntfDelete_Object = MibTableColumn
wfFwallIntfDelete = _WfFwallIntfDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 11, 3, 1, 1),
    _WfFwallIntfDelete_Type()
)
wfFwallIntfDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFwallIntfDelete.setStatus("mandatory")


class _WfFwallIntfDisable_Type(Integer32):
    """Custom type wfFwallIntfDisable based on Integer32"""
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


_WfFwallIntfDisable_Type.__name__ = "Integer32"
_WfFwallIntfDisable_Object = MibTableColumn
wfFwallIntfDisable = _WfFwallIntfDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 11, 3, 1, 2),
    _WfFwallIntfDisable_Type()
)
wfFwallIntfDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFwallIntfDisable.setStatus("mandatory")


class _WfFwallIntfCct_Type(Integer32):
    """Custom type wfFwallIntfCct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_WfFwallIntfCct_Type.__name__ = "Integer32"
_WfFwallIntfCct_Object = MibTableColumn
wfFwallIntfCct = _WfFwallIntfCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 11, 3, 1, 3),
    _WfFwallIntfCct_Type()
)
wfFwallIntfCct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFwallIntfCct.setStatus("mandatory")


class _WfFwallIntfName_Type(DisplayString):
    """Custom type wfFwallIntfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_WfFwallIntfName_Type.__name__ = "DisplayString"
_WfFwallIntfName_Object = MibTableColumn
wfFwallIntfName = _WfFwallIntfName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 11, 3, 1, 4),
    _WfFwallIntfName_Type()
)
wfFwallIntfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFwallIntfName.setStatus("mandatory")


class _WfFwallIntfPolicyIndex_Type(Integer32):
    """Custom type wfFwallIntfPolicyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_WfFwallIntfPolicyIndex_Type.__name__ = "Integer32"
_WfFwallIntfPolicyIndex_Object = MibTableColumn
wfFwallIntfPolicyIndex = _WfFwallIntfPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 11, 3, 1, 5),
    _WfFwallIntfPolicyIndex_Type()
)
wfFwallIntfPolicyIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFwallIntfPolicyIndex.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-IFWALL-MIB",
    **{"wfIFwallIfTable": wfIFwallIfTable,
       "wfIFwallIfEntry": wfIFwallIfEntry,
       "wfIFwallIfDelete": wfIFwallIfDelete,
       "wfIFwallIfDisable": wfIFwallIfDisable,
       "wfIFwallIfCct": wfIFwallIfCct,
       "wfIFwallIfSlot": wfIFwallIfSlot,
       "wfIFwallIfPort": wfIFwallIfPort,
       "wfIFwallIfLineNumber": wfIFwallIfLineNumber,
       "wfIFwallIfName": wfIFwallIfName,
       "wfFwallIntfTable": wfFwallIntfTable,
       "wfFwallIntfEntry": wfFwallIntfEntry,
       "wfFwallIntfDelete": wfFwallIntfDelete,
       "wfFwallIntfDisable": wfFwallIntfDisable,
       "wfFwallIntfCct": wfFwallIntfCct,
       "wfFwallIntfName": wfFwallIntfName,
       "wfFwallIntfPolicyIndex": wfFwallIntfPolicyIndex}
)
