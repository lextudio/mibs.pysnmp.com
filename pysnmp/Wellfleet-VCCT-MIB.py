# SNMP MIB module (Wellfleet-VCCT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-VCCT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:17:23 2024
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

(wfVcctGroup,) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfVcctGroup")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfVcct_ObjectIdentity = ObjectIdentity
wfVcct = _WfVcct_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 24, 1)
)


class _WfVcctDelete_Type(Integer32):
    """Custom type wfVcctDelete based on Integer32"""
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


_WfVcctDelete_Type.__name__ = "Integer32"
_WfVcctDelete_Object = MibScalar
wfVcctDelete = _WfVcctDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 24, 1, 1),
    _WfVcctDelete_Type()
)
wfVcctDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfVcctDelete.setStatus("mandatory")


class _WfVcctDisable_Type(Integer32):
    """Custom type wfVcctDisable based on Integer32"""
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


_WfVcctDisable_Type.__name__ = "Integer32"
_WfVcctDisable_Object = MibScalar
wfVcctDisable = _WfVcctDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 24, 1, 2),
    _WfVcctDisable_Type()
)
wfVcctDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfVcctDisable.setStatus("mandatory")


class _WfVcctState_Type(Integer32):
    """Custom type wfVcctState based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("init", 3),
          ("notpresent", 4),
          ("up", 1))
    )


_WfVcctState_Type.__name__ = "Integer32"
_WfVcctState_Object = MibScalar
wfVcctState = _WfVcctState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 24, 1, 3),
    _WfVcctState_Type()
)
wfVcctState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVcctState.setStatus("mandatory")
_WfVcctTable_Object = MibTable
wfVcctTable = _WfVcctTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 24, 2)
)
if mibBuilder.loadTexts:
    wfVcctTable.setStatus("mandatory")
_WfVcctEntry_Object = MibTableRow
wfVcctEntry = _WfVcctEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 24, 2, 1)
)
wfVcctEntry.setIndexNames(
    (0, "Wellfleet-VCCT-MIB", "wfVcctEntrySlot"),
    (0, "Wellfleet-VCCT-MIB", "wfVcctEntryCct"),
)
if mibBuilder.loadTexts:
    wfVcctEntry.setStatus("mandatory")


class _WfVcctEntryDelete_Type(Integer32):
    """Custom type wfVcctEntryDelete based on Integer32"""
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


_WfVcctEntryDelete_Type.__name__ = "Integer32"
_WfVcctEntryDelete_Object = MibTableColumn
wfVcctEntryDelete = _WfVcctEntryDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 24, 2, 1, 1),
    _WfVcctEntryDelete_Type()
)
wfVcctEntryDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfVcctEntryDelete.setStatus("mandatory")


class _WfVcctEntryDisable_Type(Integer32):
    """Custom type wfVcctEntryDisable based on Integer32"""
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


_WfVcctEntryDisable_Type.__name__ = "Integer32"
_WfVcctEntryDisable_Object = MibTableColumn
wfVcctEntryDisable = _WfVcctEntryDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 24, 2, 1, 2),
    _WfVcctEntryDisable_Type()
)
wfVcctEntryDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfVcctEntryDisable.setStatus("mandatory")


class _WfVcctEntryState_Type(Integer32):
    """Custom type wfVcctEntryState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("coisapwait", 1),
          ("connectrcv", 4),
          ("connectrspwait", 3),
          ("connectwait", 2),
          ("disconnectrspwait", 5))
    )


_WfVcctEntryState_Type.__name__ = "Integer32"
_WfVcctEntryState_Object = MibTableColumn
wfVcctEntryState = _WfVcctEntryState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 24, 2, 1, 3),
    _WfVcctEntryState_Type()
)
wfVcctEntryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVcctEntryState.setStatus("mandatory")
_WfVcctEntrySlot_Type = Integer32
_WfVcctEntrySlot_Object = MibTableColumn
wfVcctEntrySlot = _WfVcctEntrySlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 24, 2, 1, 4),
    _WfVcctEntrySlot_Type()
)
wfVcctEntrySlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVcctEntrySlot.setStatus("mandatory")
_WfVcctEntryCct_Type = Integer32
_WfVcctEntryCct_Object = MibTableColumn
wfVcctEntryCct = _WfVcctEntryCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 24, 2, 1, 5),
    _WfVcctEntryCct_Type()
)
wfVcctEntryCct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVcctEntryCct.setStatus("mandatory")
_WfVcctEntryNumClients_Type = Integer32
_WfVcctEntryNumClients_Object = MibTableColumn
wfVcctEntryNumClients = _WfVcctEntryNumClients_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 24, 2, 1, 6),
    _WfVcctEntryNumClients_Type()
)
wfVcctEntryNumClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVcctEntryNumClients.setStatus("mandatory")


class _WfVcctEntryServiceType_Type(Integer32):
    """Custom type wfVcctEntryServiceType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("dlcClientApi", 1)
    )


_WfVcctEntryServiceType_Type.__name__ = "Integer32"
_WfVcctEntryServiceType_Object = MibTableColumn
wfVcctEntryServiceType = _WfVcctEntryServiceType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 24, 2, 1, 7),
    _WfVcctEntryServiceType_Type()
)
wfVcctEntryServiceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfVcctEntryServiceType.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-VCCT-MIB",
    **{"wfVcct": wfVcct,
       "wfVcctDelete": wfVcctDelete,
       "wfVcctDisable": wfVcctDisable,
       "wfVcctState": wfVcctState,
       "wfVcctTable": wfVcctTable,
       "wfVcctEntry": wfVcctEntry,
       "wfVcctEntryDelete": wfVcctEntryDelete,
       "wfVcctEntryDisable": wfVcctEntryDisable,
       "wfVcctEntryState": wfVcctEntryState,
       "wfVcctEntrySlot": wfVcctEntrySlot,
       "wfVcctEntryCct": wfVcctEntryCct,
       "wfVcctEntryNumClients": wfVcctEntryNumClients,
       "wfVcctEntryServiceType": wfVcctEntryServiceType}
)
