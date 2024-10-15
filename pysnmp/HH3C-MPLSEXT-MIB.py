# SNMP MIB module (HH3C-MPLSEXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-MPLSEXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:54:12 2024
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

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hh3cMplsExt = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 142)
)
hh3cMplsExt.setRevisions(
        ("2013-06-13 18:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cMplsExtObjects_ObjectIdentity = ObjectIdentity
hh3cMplsExtObjects = _Hh3cMplsExtObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 142, 1)
)
_Hh3cMplsExtScalarGroup_ObjectIdentity = ObjectIdentity
hh3cMplsExtScalarGroup = _Hh3cMplsExtScalarGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 142, 1, 1)
)


class _Hh3cMplsExtLsrID_Type(OctetString):
    """Custom type hh3cMplsExtLsrID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hh3cMplsExtLsrID_Type.__name__ = "OctetString"
_Hh3cMplsExtLsrID_Object = MibScalar
hh3cMplsExtLsrID = _Hh3cMplsExtLsrID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 142, 1, 1, 1),
    _Hh3cMplsExtLsrID_Type()
)
hh3cMplsExtLsrID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cMplsExtLsrID.setStatus("current")
_Hh3cMplsExtLdpStatus_Type = TruthValue
_Hh3cMplsExtLdpStatus_Object = MibScalar
hh3cMplsExtLdpStatus = _Hh3cMplsExtLdpStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 142, 1, 1, 2),
    _Hh3cMplsExtLdpStatus_Type()
)
hh3cMplsExtLdpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cMplsExtLdpStatus.setStatus("current")
_Hh3cMplsExtTable_Object = MibTable
hh3cMplsExtTable = _Hh3cMplsExtTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 142, 1, 2)
)
if mibBuilder.loadTexts:
    hh3cMplsExtTable.setStatus("current")
_Hh3cMplsExtEntry_Object = MibTableRow
hh3cMplsExtEntry = _Hh3cMplsExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 142, 1, 2, 1)
)
hh3cMplsExtEntry.setIndexNames(
    (0, "HH3C-MPLSEXT-MIB", "hh3cMplsExtIndex"),
)
if mibBuilder.loadTexts:
    hh3cMplsExtEntry.setStatus("current")


class _Hh3cMplsExtIndex_Type(Unsigned32):
    """Custom type hh3cMplsExtIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Hh3cMplsExtIndex_Type.__name__ = "Unsigned32"
_Hh3cMplsExtIndex_Object = MibTableColumn
hh3cMplsExtIndex = _Hh3cMplsExtIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 142, 1, 2, 1, 1),
    _Hh3cMplsExtIndex_Type()
)
hh3cMplsExtIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cMplsExtIndex.setStatus("current")


class _Hh3cMplsExtCapability_Type(TruthValue):
    """Custom type hh3cMplsExtCapability based on TruthValue"""


_Hh3cMplsExtCapability_Object = MibTableColumn
hh3cMplsExtCapability = _Hh3cMplsExtCapability_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 142, 1, 2, 1, 2),
    _Hh3cMplsExtCapability_Type()
)
hh3cMplsExtCapability.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMplsExtCapability.setStatus("current")


class _Hh3cMplsExtMtu_Type(Unsigned32):
    """Custom type hh3cMplsExtMtu based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(46, 65535),
    )


_Hh3cMplsExtMtu_Type.__name__ = "Unsigned32"
_Hh3cMplsExtMtu_Object = MibTableColumn
hh3cMplsExtMtu = _Hh3cMplsExtMtu_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 142, 1, 2, 1, 3),
    _Hh3cMplsExtMtu_Type()
)
hh3cMplsExtMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMplsExtMtu.setStatus("current")
_Hh3cMplsExtRowStatus_Type = RowStatus
_Hh3cMplsExtRowStatus_Object = MibTableColumn
hh3cMplsExtRowStatus = _Hh3cMplsExtRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 142, 1, 2, 1, 4),
    _Hh3cMplsExtRowStatus_Type()
)
hh3cMplsExtRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMplsExtRowStatus.setStatus("current")
_Hh3cMplsExtLdpTable_Object = MibTable
hh3cMplsExtLdpTable = _Hh3cMplsExtLdpTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 142, 1, 3)
)
if mibBuilder.loadTexts:
    hh3cMplsExtLdpTable.setStatus("current")
_Hh3cMplsExtLdpEntry_Object = MibTableRow
hh3cMplsExtLdpEntry = _Hh3cMplsExtLdpEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 142, 1, 3, 1)
)
hh3cMplsExtLdpEntry.setIndexNames(
    (0, "HH3C-MPLSEXT-MIB", "hh3cMplsExtLdpIndex"),
)
if mibBuilder.loadTexts:
    hh3cMplsExtLdpEntry.setStatus("current")


class _Hh3cMplsExtLdpIndex_Type(Unsigned32):
    """Custom type hh3cMplsExtLdpIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Hh3cMplsExtLdpIndex_Type.__name__ = "Unsigned32"
_Hh3cMplsExtLdpIndex_Object = MibTableColumn
hh3cMplsExtLdpIndex = _Hh3cMplsExtLdpIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 142, 1, 3, 1, 1),
    _Hh3cMplsExtLdpIndex_Type()
)
hh3cMplsExtLdpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cMplsExtLdpIndex.setStatus("current")


class _Hh3cMplsExtLdpCapability_Type(TruthValue):
    """Custom type hh3cMplsExtLdpCapability based on TruthValue"""


_Hh3cMplsExtLdpCapability_Object = MibTableColumn
hh3cMplsExtLdpCapability = _Hh3cMplsExtLdpCapability_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 142, 1, 3, 1, 2),
    _Hh3cMplsExtLdpCapability_Type()
)
hh3cMplsExtLdpCapability.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMplsExtLdpCapability.setStatus("current")
_Hh3cMplsExtLdpRowStatus_Type = RowStatus
_Hh3cMplsExtLdpRowStatus_Object = MibTableColumn
hh3cMplsExtLdpRowStatus = _Hh3cMplsExtLdpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 142, 1, 3, 1, 3),
    _Hh3cMplsExtLdpRowStatus_Type()
)
hh3cMplsExtLdpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMplsExtLdpRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-MPLSEXT-MIB",
    **{"hh3cMplsExt": hh3cMplsExt,
       "hh3cMplsExtObjects": hh3cMplsExtObjects,
       "hh3cMplsExtScalarGroup": hh3cMplsExtScalarGroup,
       "hh3cMplsExtLsrID": hh3cMplsExtLsrID,
       "hh3cMplsExtLdpStatus": hh3cMplsExtLdpStatus,
       "hh3cMplsExtTable": hh3cMplsExtTable,
       "hh3cMplsExtEntry": hh3cMplsExtEntry,
       "hh3cMplsExtIndex": hh3cMplsExtIndex,
       "hh3cMplsExtCapability": hh3cMplsExtCapability,
       "hh3cMplsExtMtu": hh3cMplsExtMtu,
       "hh3cMplsExtRowStatus": hh3cMplsExtRowStatus,
       "hh3cMplsExtLdpTable": hh3cMplsExtLdpTable,
       "hh3cMplsExtLdpEntry": hh3cMplsExtLdpEntry,
       "hh3cMplsExtLdpIndex": hh3cMplsExtLdpIndex,
       "hh3cMplsExtLdpCapability": hh3cMplsExtLdpCapability,
       "hh3cMplsExtLdpRowStatus": hh3cMplsExtLdpRowStatus}
)
