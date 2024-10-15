# SNMP MIB module (CTRON-FNBTR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CTRON-FNBTR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:18:53 2024
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

(ctTokenRingFnb,) = mibBuilder.importSymbols(
    "CTRON-MIB-NAMES",
    "ctTokenRingFnb")

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


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CtronFnbTR_ObjectIdentity = ObjectIdentity
ctronFnbTR = _CtronFnbTR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 6, 1, 1)
)
_CtronFnbTRTable_Object = MibTable
ctronFnbTRTable = _CtronFnbTRTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 6, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ctronFnbTRTable.setStatus("mandatory")
_CtronFnbTREntry_Object = MibTableRow
ctronFnbTREntry = _CtronFnbTREntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 6, 1, 1, 1, 1)
)
ctronFnbTREntry.setIndexNames(
    (0, "CTRON-FNBTR-MIB", "ctronFnbTRIndex"),
)
if mibBuilder.loadTexts:
    ctronFnbTREntry.setStatus("mandatory")
_CtronFnbTRIndex_Type = Integer32
_CtronFnbTRIndex_Object = MibTableColumn
ctronFnbTRIndex = _CtronFnbTRIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 6, 1, 1, 1, 1, 1),
    _CtronFnbTRIndex_Type()
)
ctronFnbTRIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctronFnbTRIndex.setStatus("mandatory")


class _CtronFnbConnectLeft_Type(Integer32):
    """Custom type ctronFnbConnectLeft based on Integer32"""
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
        *(("attached", 3),
          ("detached", 2),
          ("faulted", 4),
          ("other", 1))
    )


_CtronFnbConnectLeft_Type.__name__ = "Integer32"
_CtronFnbConnectLeft_Object = MibTableColumn
ctronFnbConnectLeft = _CtronFnbConnectLeft_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 6, 1, 1, 1, 1, 2),
    _CtronFnbConnectLeft_Type()
)
ctronFnbConnectLeft.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctronFnbConnectLeft.setStatus("mandatory")


class _CtronFnbConnectRight_Type(Integer32):
    """Custom type ctronFnbConnectRight based on Integer32"""
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
        *(("attached", 3),
          ("detached", 2),
          ("faulted", 4),
          ("other", 1))
    )


_CtronFnbConnectRight_Type.__name__ = "Integer32"
_CtronFnbConnectRight_Object = MibTableColumn
ctronFnbConnectRight = _CtronFnbConnectRight_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 6, 1, 1, 1, 1, 3),
    _CtronFnbConnectRight_Type()
)
ctronFnbConnectRight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctronFnbConnectRight.setStatus("mandatory")


class _CtronFnbBypass_Type(Integer32):
    """Custom type ctronFnbBypass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_CtronFnbBypass_Type.__name__ = "Integer32"
_CtronFnbBypass_Object = MibTableColumn
ctronFnbBypass = _CtronFnbBypass_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 6, 1, 1, 1, 1, 4),
    _CtronFnbBypass_Type()
)
ctronFnbBypass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctronFnbBypass.setStatus("mandatory")


class _CtronFnbRPBypass_Type(Integer32):
    """Custom type ctronFnbRPBypass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enable", 2),
          ("other", 1))
    )


_CtronFnbRPBypass_Type.__name__ = "Integer32"
_CtronFnbRPBypass_Object = MibTableColumn
ctronFnbRPBypass = _CtronFnbRPBypass_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 6, 1, 1, 1, 1, 5),
    _CtronFnbRPBypass_Type()
)
ctronFnbRPBypass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctronFnbRPBypass.setStatus("mandatory")
_CtronMultiFnbTR_ObjectIdentity = ObjectIdentity
ctronMultiFnbTR = _CtronMultiFnbTR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 6, 1, 2)
)
_CtronMultiFnbTRTable_Object = MibTable
ctronMultiFnbTRTable = _CtronMultiFnbTRTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 6, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ctronMultiFnbTRTable.setStatus("mandatory")
_CtronMultiFnbTREntry_Object = MibTableRow
ctronMultiFnbTREntry = _CtronMultiFnbTREntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 6, 1, 2, 1, 1)
)
ctronMultiFnbTREntry.setIndexNames(
    (0, "CTRON-FNBTR-MIB", "ctronMultiFnbTRIndex"),
    (0, "CTRON-FNBTR-MIB", "ctronMultiFnbRingIndex"),
)
if mibBuilder.loadTexts:
    ctronMultiFnbTREntry.setStatus("mandatory")
_CtronMultiFnbTRIndex_Type = Integer32
_CtronMultiFnbTRIndex_Object = MibTableColumn
ctronMultiFnbTRIndex = _CtronMultiFnbTRIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 6, 1, 2, 1, 1, 1),
    _CtronMultiFnbTRIndex_Type()
)
ctronMultiFnbTRIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctronMultiFnbTRIndex.setStatus("mandatory")
_CtronMultiFnbRingIndex_Type = Integer32
_CtronMultiFnbRingIndex_Object = MibTableColumn
ctronMultiFnbRingIndex = _CtronMultiFnbRingIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 6, 1, 2, 1, 1, 2),
    _CtronMultiFnbRingIndex_Type()
)
ctronMultiFnbRingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctronMultiFnbRingIndex.setStatus("mandatory")


class _CtronMultiFnbConnectLeft_Type(Integer32):
    """Custom type ctronMultiFnbConnectLeft based on Integer32"""
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
        *(("attached", 3),
          ("detached", 2),
          ("faulted", 4),
          ("other", 1))
    )


_CtronMultiFnbConnectLeft_Type.__name__ = "Integer32"
_CtronMultiFnbConnectLeft_Object = MibTableColumn
ctronMultiFnbConnectLeft = _CtronMultiFnbConnectLeft_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 6, 1, 2, 1, 1, 3),
    _CtronMultiFnbConnectLeft_Type()
)
ctronMultiFnbConnectLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctronMultiFnbConnectLeft.setStatus("mandatory")


class _CtronMultiFnbConnectRight_Type(Integer32):
    """Custom type ctronMultiFnbConnectRight based on Integer32"""
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
        *(("attached", 3),
          ("detached", 2),
          ("faulted", 4),
          ("other", 1))
    )


_CtronMultiFnbConnectRight_Type.__name__ = "Integer32"
_CtronMultiFnbConnectRight_Object = MibTableColumn
ctronMultiFnbConnectRight = _CtronMultiFnbConnectRight_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 6, 1, 2, 1, 1, 4),
    _CtronMultiFnbConnectRight_Type()
)
ctronMultiFnbConnectRight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctronMultiFnbConnectRight.setStatus("mandatory")


class _CtronMultiFnbBypass_Type(Integer32):
    """Custom type ctronMultiFnbBypass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_CtronMultiFnbBypass_Type.__name__ = "Integer32"
_CtronMultiFnbBypass_Object = MibTableColumn
ctronMultiFnbBypass = _CtronMultiFnbBypass_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 6, 1, 2, 1, 1, 5),
    _CtronMultiFnbBypass_Type()
)
ctronMultiFnbBypass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctronMultiFnbBypass.setStatus("mandatory")


class _CtronMultiFnbRPBypass_Type(Integer32):
    """Custom type ctronMultiFnbRPBypass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enable", 2),
          ("other", 1))
    )


_CtronMultiFnbRPBypass_Type.__name__ = "Integer32"
_CtronMultiFnbRPBypass_Object = MibTableColumn
ctronMultiFnbRPBypass = _CtronMultiFnbRPBypass_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 6, 1, 2, 1, 1, 6),
    _CtronMultiFnbRPBypass_Type()
)
ctronMultiFnbRPBypass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctronMultiFnbRPBypass.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CTRON-FNBTR-MIB",
    **{"ctronFnbTR": ctronFnbTR,
       "ctronFnbTRTable": ctronFnbTRTable,
       "ctronFnbTREntry": ctronFnbTREntry,
       "ctronFnbTRIndex": ctronFnbTRIndex,
       "ctronFnbConnectLeft": ctronFnbConnectLeft,
       "ctronFnbConnectRight": ctronFnbConnectRight,
       "ctronFnbBypass": ctronFnbBypass,
       "ctronFnbRPBypass": ctronFnbRPBypass,
       "ctronMultiFnbTR": ctronMultiFnbTR,
       "ctronMultiFnbTRTable": ctronMultiFnbTRTable,
       "ctronMultiFnbTREntry": ctronMultiFnbTREntry,
       "ctronMultiFnbTRIndex": ctronMultiFnbTRIndex,
       "ctronMultiFnbRingIndex": ctronMultiFnbRingIndex,
       "ctronMultiFnbConnectLeft": ctronMultiFnbConnectLeft,
       "ctronMultiFnbConnectRight": ctronMultiFnbConnectRight,
       "ctronMultiFnbBypass": ctronMultiFnbBypass,
       "ctronMultiFnbRPBypass": ctronMultiFnbRPBypass}
)
