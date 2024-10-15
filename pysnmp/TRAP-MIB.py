# SNMP MIB module (TRAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TRAP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:07:24 2024
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

(ctTrapTable,) = mibBuilder.importSymbols(
    "CTRON-MIB-NAMES",
    "ctTrapTable")

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

_Trap_ObjectIdentity = ObjectIdentity
trap = _Trap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 7, 1)
)
_TrapTable_Object = MibTable
trapTable = _TrapTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 7, 1, 1)
)
if mibBuilder.loadTexts:
    trapTable.setStatus("mandatory")
_TrapEntry_Object = MibTableRow
trapEntry = _TrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 7, 1, 1, 1)
)
trapEntry.setIndexNames(
    (0, "TRAP-MIB", "trapIndex"),
)
if mibBuilder.loadTexts:
    trapEntry.setStatus("mandatory")


class _TrapIndex_Type(Integer32):
    """Custom type trapIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_TrapIndex_Type.__name__ = "Integer32"
_TrapIndex_Object = MibTableColumn
trapIndex = _TrapIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 7, 1, 1, 1, 1),
    _TrapIndex_Type()
)
trapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapIndex.setStatus("mandatory")


class _TrapCommunityName_Type(OctetString):
    """Custom type trapCommunityName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TrapCommunityName_Type.__name__ = "OctetString"
_TrapCommunityName_Object = MibTableColumn
trapCommunityName = _TrapCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 7, 1, 1, 1, 2),
    _TrapCommunityName_Type()
)
trapCommunityName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapCommunityName.setStatus("mandatory")


class _TrapStatus_Type(Integer32):
    """Custom type trapStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("trapsDisabled", 1),
          ("trapsEnabled", 2))
    )


_TrapStatus_Type.__name__ = "Integer32"
_TrapStatus_Object = MibTableColumn
trapStatus = _TrapStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 7, 1, 1, 1, 3),
    _TrapStatus_Type()
)
trapStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapStatus.setStatus("mandatory")
_TrapIPAddr_Type = IpAddress
_TrapIPAddr_Object = MibTableColumn
trapIPAddr = _TrapIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 7, 1, 1, 1, 4),
    _TrapIPAddr_Type()
)
trapIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapIPAddr.setStatus("mandatory")
_TrapSrcParty_Type = ObjectIdentifier
_TrapSrcParty_Object = MibTableColumn
trapSrcParty = _TrapSrcParty_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 7, 1, 1, 1, 5),
    _TrapSrcParty_Type()
)
trapSrcParty.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapSrcParty.setStatus("mandatory")
_TrapDstParty_Type = ObjectIdentifier
_TrapDstParty_Object = MibTableColumn
trapDstParty = _TrapDstParty_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 7, 1, 1, 1, 6),
    _TrapDstParty_Type()
)
trapDstParty.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapDstParty.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TRAP-MIB",
    **{"trap": trap,
       "trapTable": trapTable,
       "trapEntry": trapEntry,
       "trapIndex": trapIndex,
       "trapCommunityName": trapCommunityName,
       "trapStatus": trapStatus,
       "trapIPAddr": trapIPAddr,
       "trapSrcParty": trapSrcParty,
       "trapDstParty": trapDstParty}
)
