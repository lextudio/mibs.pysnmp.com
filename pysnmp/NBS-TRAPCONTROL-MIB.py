# SNMP MIB module (NBS-TRAPCONTROL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NBS-TRAPCONTROL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:25:04 2024
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

(InterfaceIndex,
 nbs) = mibBuilder.importSymbols(
    "NBS-CMMC-MIB",
    "InterfaceIndex",
    "nbs")

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

nbsTrapControlMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 629, 209)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NbsTrapListGrp_ObjectIdentity = ObjectIdentity
nbsTrapListGrp = _NbsTrapListGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 209, 1)
)
if mibBuilder.loadTexts:
    nbsTrapListGrp.setStatus("current")
_NbsTrapListTableSize_Type = Unsigned32
_NbsTrapListTableSize_Object = MibScalar
nbsTrapListTableSize = _NbsTrapListTableSize_Object(
    (1, 3, 6, 1, 4, 1, 629, 209, 1, 1),
    _NbsTrapListTableSize_Type()
)
nbsTrapListTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsTrapListTableSize.setStatus("current")
_NbsTrapListTable_Object = MibTable
nbsTrapListTable = _NbsTrapListTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 209, 1, 2)
)
if mibBuilder.loadTexts:
    nbsTrapListTable.setStatus("current")
_NbsTrapListEntry_Object = MibTableRow
nbsTrapListEntry = _NbsTrapListEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 209, 1, 2, 1)
)
nbsTrapListEntry.setIndexNames(
    (0, "NBS-TRAPCONTROL-MIB", "nbsTrapListIndex"),
)
if mibBuilder.loadTexts:
    nbsTrapListEntry.setStatus("current")
_NbsTrapListIndex_Type = Unsigned32
_NbsTrapListIndex_Object = MibTableColumn
nbsTrapListIndex = _NbsTrapListIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 209, 1, 2, 1, 1),
    _NbsTrapListIndex_Type()
)
nbsTrapListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nbsTrapListIndex.setStatus("current")


class _NbsTrapListTrapMib_Type(DisplayString):
    """Custom type nbsTrapListTrapMib based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NbsTrapListTrapMib_Type.__name__ = "DisplayString"
_NbsTrapListTrapMib_Object = MibTableColumn
nbsTrapListTrapMib = _NbsTrapListTrapMib_Object(
    (1, 3, 6, 1, 4, 1, 629, 209, 1, 2, 1, 2),
    _NbsTrapListTrapMib_Type()
)
nbsTrapListTrapMib.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsTrapListTrapMib.setStatus("current")


class _NbsTrapListTrapName_Type(DisplayString):
    """Custom type nbsTrapListTrapName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_NbsTrapListTrapName_Type.__name__ = "DisplayString"
_NbsTrapListTrapName_Object = MibTableColumn
nbsTrapListTrapName = _NbsTrapListTrapName_Object(
    (1, 3, 6, 1, 4, 1, 629, 209, 1, 2, 1, 3),
    _NbsTrapListTrapName_Type()
)
nbsTrapListTrapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsTrapListTrapName.setStatus("current")


class _NbsTrapListTrapDescription_Type(DisplayString):
    """Custom type nbsTrapListTrapDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_NbsTrapListTrapDescription_Type.__name__ = "DisplayString"
_NbsTrapListTrapDescription_Object = MibTableColumn
nbsTrapListTrapDescription = _NbsTrapListTrapDescription_Object(
    (1, 3, 6, 1, 4, 1, 629, 209, 1, 2, 1, 4),
    _NbsTrapListTrapDescription_Type()
)
nbsTrapListTrapDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsTrapListTrapDescription.setStatus("current")


class _NbsTrapListTrapOID_Type(DisplayString):
    """Custom type nbsTrapListTrapOID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_NbsTrapListTrapOID_Type.__name__ = "DisplayString"
_NbsTrapListTrapOID_Object = MibTableColumn
nbsTrapListTrapOID = _NbsTrapListTrapOID_Object(
    (1, 3, 6, 1, 4, 1, 629, 209, 1, 2, 1, 5),
    _NbsTrapListTrapOID_Type()
)
nbsTrapListTrapOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsTrapListTrapOID.setStatus("current")
_NbsTrapIfGrp_ObjectIdentity = ObjectIdentity
nbsTrapIfGrp = _NbsTrapIfGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 209, 2)
)
if mibBuilder.loadTexts:
    nbsTrapIfGrp.setStatus("current")
_NbsTrapIfTableSize_Type = Unsigned32
_NbsTrapIfTableSize_Object = MibScalar
nbsTrapIfTableSize = _NbsTrapIfTableSize_Object(
    (1, 3, 6, 1, 4, 1, 629, 209, 2, 1),
    _NbsTrapIfTableSize_Type()
)
nbsTrapIfTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsTrapIfTableSize.setStatus("current")
_NbsTrapIfTable_Object = MibTable
nbsTrapIfTable = _NbsTrapIfTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 209, 2, 2)
)
if mibBuilder.loadTexts:
    nbsTrapIfTable.setStatus("current")
_NbsTrapIfEntry_Object = MibTableRow
nbsTrapIfEntry = _NbsTrapIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 209, 2, 2, 1)
)
nbsTrapIfEntry.setIndexNames(
    (0, "NBS-TRAPCONTROL-MIB", "nbsTrapIfIndex"),
)
if mibBuilder.loadTexts:
    nbsTrapIfEntry.setStatus("current")
_NbsTrapIfIndex_Type = InterfaceIndex
_NbsTrapIfIndex_Object = MibTableColumn
nbsTrapIfIndex = _NbsTrapIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 209, 2, 2, 1, 1),
    _NbsTrapIfIndex_Type()
)
nbsTrapIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nbsTrapIfIndex.setStatus("current")
_NbsTrapIfTrapsCaps_Type = OctetString
_NbsTrapIfTrapsCaps_Object = MibTableColumn
nbsTrapIfTrapsCaps = _NbsTrapIfTrapsCaps_Object(
    (1, 3, 6, 1, 4, 1, 629, 209, 2, 2, 1, 2),
    _NbsTrapIfTrapsCaps_Type()
)
nbsTrapIfTrapsCaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsTrapIfTrapsCaps.setStatus("current")
_NbsTrapIfTrapsSelect_Type = OctetString
_NbsTrapIfTrapsSelect_Object = MibTableColumn
nbsTrapIfTrapsSelect = _NbsTrapIfTrapsSelect_Object(
    (1, 3, 6, 1, 4, 1, 629, 209, 2, 2, 1, 3),
    _NbsTrapIfTrapsSelect_Type()
)
nbsTrapIfTrapsSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsTrapIfTrapsSelect.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NBS-TRAPCONTROL-MIB",
    **{"nbsTrapControlMib": nbsTrapControlMib,
       "nbsTrapListGrp": nbsTrapListGrp,
       "nbsTrapListTableSize": nbsTrapListTableSize,
       "nbsTrapListTable": nbsTrapListTable,
       "nbsTrapListEntry": nbsTrapListEntry,
       "nbsTrapListIndex": nbsTrapListIndex,
       "nbsTrapListTrapMib": nbsTrapListTrapMib,
       "nbsTrapListTrapName": nbsTrapListTrapName,
       "nbsTrapListTrapDescription": nbsTrapListTrapDescription,
       "nbsTrapListTrapOID": nbsTrapListTrapOID,
       "nbsTrapIfGrp": nbsTrapIfGrp,
       "nbsTrapIfTableSize": nbsTrapIfTableSize,
       "nbsTrapIfTable": nbsTrapIfTable,
       "nbsTrapIfEntry": nbsTrapIfEntry,
       "nbsTrapIfIndex": nbsTrapIfIndex,
       "nbsTrapIfTrapsCaps": nbsTrapIfTrapsCaps,
       "nbsTrapIfTrapsSelect": nbsTrapIfTrapsSelect}
)
