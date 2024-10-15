# SNMP MIB module (Wellfleet-RARP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-RARP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:16:58 2024
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

(wfRarpGroup,) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfRarpGroup")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfRarp_ObjectIdentity = ObjectIdentity
wfRarp = _WfRarp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 9, 1)
)


class _WfRarpDelete_Type(Integer32):
    """Custom type wfRarpDelete based on Integer32"""
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


_WfRarpDelete_Type.__name__ = "Integer32"
_WfRarpDelete_Object = MibScalar
wfRarpDelete = _WfRarpDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 9, 1, 1),
    _WfRarpDelete_Type()
)
wfRarpDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRarpDelete.setStatus("mandatory")


class _WfRarpDisable_Type(Integer32):
    """Custom type wfRarpDisable based on Integer32"""
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


_WfRarpDisable_Type.__name__ = "Integer32"
_WfRarpDisable_Object = MibScalar
wfRarpDisable = _WfRarpDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 9, 1, 2),
    _WfRarpDisable_Type()
)
wfRarpDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRarpDisable.setStatus("mandatory")
_WfRarpNumNoMatches_Type = Counter32
_WfRarpNumNoMatches_Object = MibScalar
wfRarpNumNoMatches = _WfRarpNumNoMatches_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 9, 1, 3),
    _WfRarpNumNoMatches_Type()
)
wfRarpNumNoMatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRarpNumNoMatches.setStatus("mandatory")
_WfRarpMapTable_Object = MibTable
wfRarpMapTable = _WfRarpMapTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 9, 2)
)
if mibBuilder.loadTexts:
    wfRarpMapTable.setStatus("mandatory")
_WfRarpMapEntry_Object = MibTableRow
wfRarpMapEntry = _WfRarpMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 9, 2, 1)
)
wfRarpMapEntry.setIndexNames(
    (0, "Wellfleet-RARP-MIB", "wfRarpMapMadr"),
)
if mibBuilder.loadTexts:
    wfRarpMapEntry.setStatus("mandatory")


class _WfRarpMapDelete_Type(Integer32):
    """Custom type wfRarpMapDelete based on Integer32"""
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


_WfRarpMapDelete_Type.__name__ = "Integer32"
_WfRarpMapDelete_Object = MibTableColumn
wfRarpMapDelete = _WfRarpMapDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 9, 2, 1, 1),
    _WfRarpMapDelete_Type()
)
wfRarpMapDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRarpMapDelete.setStatus("mandatory")


class _WfRarpMapMadr_Type(OctetString):
    """Custom type wfRarpMapMadr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_WfRarpMapMadr_Type.__name__ = "OctetString"
_WfRarpMapMadr_Object = MibTableColumn
wfRarpMapMadr = _WfRarpMapMadr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 9, 2, 1, 2),
    _WfRarpMapMadr_Type()
)
wfRarpMapMadr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRarpMapMadr.setStatus("mandatory")
_WfRarpMapIpAddr_Type = IpAddress
_WfRarpMapIpAddr_Object = MibTableColumn
wfRarpMapIpAddr = _WfRarpMapIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 9, 2, 1, 3),
    _WfRarpMapIpAddr_Type()
)
wfRarpMapIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRarpMapIpAddr.setStatus("mandatory")
_WfRarpIntfTable_Object = MibTable
wfRarpIntfTable = _WfRarpIntfTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 9, 3)
)
if mibBuilder.loadTexts:
    wfRarpIntfTable.setStatus("mandatory")
_WfRarpIntfEntry_Object = MibTableRow
wfRarpIntfEntry = _WfRarpIntfEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 9, 3, 1)
)
wfRarpIntfEntry.setIndexNames(
    (0, "Wellfleet-RARP-MIB", "wfRarpIntfCctno"),
)
if mibBuilder.loadTexts:
    wfRarpIntfEntry.setStatus("mandatory")


class _WfRarpIntfDelete_Type(Integer32):
    """Custom type wfRarpIntfDelete based on Integer32"""
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


_WfRarpIntfDelete_Type.__name__ = "Integer32"
_WfRarpIntfDelete_Object = MibTableColumn
wfRarpIntfDelete = _WfRarpIntfDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 9, 3, 1, 1),
    _WfRarpIntfDelete_Type()
)
wfRarpIntfDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRarpIntfDelete.setStatus("mandatory")


class _WfRarpIntfDisable_Type(Integer32):
    """Custom type wfRarpIntfDisable based on Integer32"""
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


_WfRarpIntfDisable_Type.__name__ = "Integer32"
_WfRarpIntfDisable_Object = MibTableColumn
wfRarpIntfDisable = _WfRarpIntfDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 9, 3, 1, 2),
    _WfRarpIntfDisable_Type()
)
wfRarpIntfDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRarpIntfDisable.setStatus("mandatory")
_WfRarpIntfCctno_Type = Integer32
_WfRarpIntfCctno_Object = MibTableColumn
wfRarpIntfCctno = _WfRarpIntfCctno_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 9, 3, 1, 3),
    _WfRarpIntfCctno_Type()
)
wfRarpIntfCctno.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRarpIntfCctno.setStatus("mandatory")
_WfRarpIntfIpAddr_Type = IpAddress
_WfRarpIntfIpAddr_Object = MibTableColumn
wfRarpIntfIpAddr = _WfRarpIntfIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 9, 3, 1, 4),
    _WfRarpIntfIpAddr_Type()
)
wfRarpIntfIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRarpIntfIpAddr.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-RARP-MIB",
    **{"wfRarp": wfRarp,
       "wfRarpDelete": wfRarpDelete,
       "wfRarpDisable": wfRarpDisable,
       "wfRarpNumNoMatches": wfRarpNumNoMatches,
       "wfRarpMapTable": wfRarpMapTable,
       "wfRarpMapEntry": wfRarpMapEntry,
       "wfRarpMapDelete": wfRarpMapDelete,
       "wfRarpMapMadr": wfRarpMapMadr,
       "wfRarpMapIpAddr": wfRarpMapIpAddr,
       "wfRarpIntfTable": wfRarpIntfTable,
       "wfRarpIntfEntry": wfRarpIntfEntry,
       "wfRarpIntfDelete": wfRarpIntfDelete,
       "wfRarpIntfDisable": wfRarpIntfDisable,
       "wfRarpIntfCctno": wfRarpIntfCctno,
       "wfRarpIntfIpAddr": wfRarpIntfIpAddr}
)
