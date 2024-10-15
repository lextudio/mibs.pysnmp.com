# SNMP MIB module (HH3C-LswSMON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-LswSMON-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:54:01 2024
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

(hh3cRhw,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cRhw")

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

_Hh3cSmonExtend_ObjectIdentity = ObjectIdentity
hh3cSmonExtend = _Hh3cSmonExtend_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 26)
)
_Hh3csmonExtendObject_ObjectIdentity = ObjectIdentity
hh3csmonExtendObject = _Hh3csmonExtendObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 26, 1)
)
_Hh3cdot1qVlanStatNumber_Type = Integer32
_Hh3cdot1qVlanStatNumber_Object = MibScalar
hh3cdot1qVlanStatNumber = _Hh3cdot1qVlanStatNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 26, 1, 1),
    _Hh3cdot1qVlanStatNumber_Type()
)
hh3cdot1qVlanStatNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cdot1qVlanStatNumber.setStatus("mandatory")
_Hh3cdot1qVlanStatStatusTable_Object = MibTable
hh3cdot1qVlanStatStatusTable = _Hh3cdot1qVlanStatStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 26, 1, 2)
)
if mibBuilder.loadTexts:
    hh3cdot1qVlanStatStatusTable.setStatus("mandatory")
_Hh3cdot1qVlanStatStatusEntry_Object = MibTableRow
hh3cdot1qVlanStatStatusEntry = _Hh3cdot1qVlanStatStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 26, 1, 2, 1)
)
hh3cdot1qVlanStatStatusEntry.setIndexNames(
    (0, "HH3C-LswSMON-MIB", "hh3cdot1qVlanStatEnableIndex"),
)
if mibBuilder.loadTexts:
    hh3cdot1qVlanStatStatusEntry.setStatus("mandatory")
_Hh3cdot1qVlanStatEnableIndex_Type = Integer32
_Hh3cdot1qVlanStatEnableIndex_Object = MibTableColumn
hh3cdot1qVlanStatEnableIndex = _Hh3cdot1qVlanStatEnableIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 26, 1, 2, 1, 1),
    _Hh3cdot1qVlanStatEnableIndex_Type()
)
hh3cdot1qVlanStatEnableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cdot1qVlanStatEnableIndex.setStatus("mandatory")


class _Hh3cdot1qVlanStatEnableStatus_Type(Integer32):
    """Custom type hh3cdot1qVlanStatEnableStatus based on Integer32"""
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


_Hh3cdot1qVlanStatEnableStatus_Type.__name__ = "Integer32"
_Hh3cdot1qVlanStatEnableStatus_Object = MibTableColumn
hh3cdot1qVlanStatEnableStatus = _Hh3cdot1qVlanStatEnableStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 26, 1, 2, 1, 2),
    _Hh3cdot1qVlanStatEnableStatus_Type()
)
hh3cdot1qVlanStatEnableStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdot1qVlanStatEnableStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-LswSMON-MIB",
    **{"hh3cSmonExtend": hh3cSmonExtend,
       "hh3csmonExtendObject": hh3csmonExtendObject,
       "hh3cdot1qVlanStatNumber": hh3cdot1qVlanStatNumber,
       "hh3cdot1qVlanStatStatusTable": hh3cdot1qVlanStatStatusTable,
       "hh3cdot1qVlanStatStatusEntry": hh3cdot1qVlanStatStatusEntry,
       "hh3cdot1qVlanStatEnableIndex": hh3cdot1qVlanStatEnableIndex,
       "hh3cdot1qVlanStatEnableStatus": hh3cdot1qVlanStatEnableStatus}
)
