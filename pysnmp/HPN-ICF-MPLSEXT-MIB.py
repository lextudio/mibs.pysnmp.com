# SNMP MIB module (HPN-ICF-MPLSEXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-MPLSEXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:01:12 2024
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

(hpnicfCommon,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfCommon")

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

hpnicfMplsExt = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 142)
)
hpnicfMplsExt.setRevisions(
        ("2013-06-13 18:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpnicfMplsExtObjects_ObjectIdentity = ObjectIdentity
hpnicfMplsExtObjects = _HpnicfMplsExtObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 142, 1)
)
_HpnicfMplsExtScalarGroup_ObjectIdentity = ObjectIdentity
hpnicfMplsExtScalarGroup = _HpnicfMplsExtScalarGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 142, 1, 1)
)


class _HpnicfMplsExtLsrID_Type(OctetString):
    """Custom type hpnicfMplsExtLsrID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HpnicfMplsExtLsrID_Type.__name__ = "OctetString"
_HpnicfMplsExtLsrID_Object = MibScalar
hpnicfMplsExtLsrID = _HpnicfMplsExtLsrID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 142, 1, 1, 1),
    _HpnicfMplsExtLsrID_Type()
)
hpnicfMplsExtLsrID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfMplsExtLsrID.setStatus("current")
_HpnicfMplsExtLdpStatus_Type = TruthValue
_HpnicfMplsExtLdpStatus_Object = MibScalar
hpnicfMplsExtLdpStatus = _HpnicfMplsExtLdpStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 142, 1, 1, 2),
    _HpnicfMplsExtLdpStatus_Type()
)
hpnicfMplsExtLdpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfMplsExtLdpStatus.setStatus("current")
_HpnicfMplsExtTable_Object = MibTable
hpnicfMplsExtTable = _HpnicfMplsExtTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 142, 1, 2)
)
if mibBuilder.loadTexts:
    hpnicfMplsExtTable.setStatus("current")
_HpnicfMplsExtEntry_Object = MibTableRow
hpnicfMplsExtEntry = _HpnicfMplsExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 142, 1, 2, 1)
)
hpnicfMplsExtEntry.setIndexNames(
    (0, "HPN-ICF-MPLSEXT-MIB", "hpnicfMplsExtIndex"),
)
if mibBuilder.loadTexts:
    hpnicfMplsExtEntry.setStatus("current")


class _HpnicfMplsExtIndex_Type(Unsigned32):
    """Custom type hpnicfMplsExtIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_HpnicfMplsExtIndex_Type.__name__ = "Unsigned32"
_HpnicfMplsExtIndex_Object = MibTableColumn
hpnicfMplsExtIndex = _HpnicfMplsExtIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 142, 1, 2, 1, 1),
    _HpnicfMplsExtIndex_Type()
)
hpnicfMplsExtIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfMplsExtIndex.setStatus("current")


class _HpnicfMplsExtCapability_Type(TruthValue):
    """Custom type hpnicfMplsExtCapability based on TruthValue"""


_HpnicfMplsExtCapability_Object = MibTableColumn
hpnicfMplsExtCapability = _HpnicfMplsExtCapability_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 142, 1, 2, 1, 2),
    _HpnicfMplsExtCapability_Type()
)
hpnicfMplsExtCapability.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMplsExtCapability.setStatus("current")


class _HpnicfMplsExtMtu_Type(Unsigned32):
    """Custom type hpnicfMplsExtMtu based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(46, 65535),
    )


_HpnicfMplsExtMtu_Type.__name__ = "Unsigned32"
_HpnicfMplsExtMtu_Object = MibTableColumn
hpnicfMplsExtMtu = _HpnicfMplsExtMtu_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 142, 1, 2, 1, 3),
    _HpnicfMplsExtMtu_Type()
)
hpnicfMplsExtMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMplsExtMtu.setStatus("current")
_HpnicfMplsExtRowStatus_Type = RowStatus
_HpnicfMplsExtRowStatus_Object = MibTableColumn
hpnicfMplsExtRowStatus = _HpnicfMplsExtRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 142, 1, 2, 1, 4),
    _HpnicfMplsExtRowStatus_Type()
)
hpnicfMplsExtRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMplsExtRowStatus.setStatus("current")
_HpnicfMplsExtLdpTable_Object = MibTable
hpnicfMplsExtLdpTable = _HpnicfMplsExtLdpTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 142, 1, 3)
)
if mibBuilder.loadTexts:
    hpnicfMplsExtLdpTable.setStatus("current")
_HpnicfMplsExtLdpEntry_Object = MibTableRow
hpnicfMplsExtLdpEntry = _HpnicfMplsExtLdpEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 142, 1, 3, 1)
)
hpnicfMplsExtLdpEntry.setIndexNames(
    (0, "HPN-ICF-MPLSEXT-MIB", "hpnicfMplsExtLdpIndex"),
)
if mibBuilder.loadTexts:
    hpnicfMplsExtLdpEntry.setStatus("current")


class _HpnicfMplsExtLdpIndex_Type(Unsigned32):
    """Custom type hpnicfMplsExtLdpIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_HpnicfMplsExtLdpIndex_Type.__name__ = "Unsigned32"
_HpnicfMplsExtLdpIndex_Object = MibTableColumn
hpnicfMplsExtLdpIndex = _HpnicfMplsExtLdpIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 142, 1, 3, 1, 1),
    _HpnicfMplsExtLdpIndex_Type()
)
hpnicfMplsExtLdpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfMplsExtLdpIndex.setStatus("current")


class _HpnicfMplsExtLdpCapability_Type(TruthValue):
    """Custom type hpnicfMplsExtLdpCapability based on TruthValue"""


_HpnicfMplsExtLdpCapability_Object = MibTableColumn
hpnicfMplsExtLdpCapability = _HpnicfMplsExtLdpCapability_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 142, 1, 3, 1, 2),
    _HpnicfMplsExtLdpCapability_Type()
)
hpnicfMplsExtLdpCapability.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMplsExtLdpCapability.setStatus("current")
_HpnicfMplsExtLdpRowStatus_Type = RowStatus
_HpnicfMplsExtLdpRowStatus_Object = MibTableColumn
hpnicfMplsExtLdpRowStatus = _HpnicfMplsExtLdpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 142, 1, 3, 1, 3),
    _HpnicfMplsExtLdpRowStatus_Type()
)
hpnicfMplsExtLdpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMplsExtLdpRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-MPLSEXT-MIB",
    **{"hpnicfMplsExt": hpnicfMplsExt,
       "hpnicfMplsExtObjects": hpnicfMplsExtObjects,
       "hpnicfMplsExtScalarGroup": hpnicfMplsExtScalarGroup,
       "hpnicfMplsExtLsrID": hpnicfMplsExtLsrID,
       "hpnicfMplsExtLdpStatus": hpnicfMplsExtLdpStatus,
       "hpnicfMplsExtTable": hpnicfMplsExtTable,
       "hpnicfMplsExtEntry": hpnicfMplsExtEntry,
       "hpnicfMplsExtIndex": hpnicfMplsExtIndex,
       "hpnicfMplsExtCapability": hpnicfMplsExtCapability,
       "hpnicfMplsExtMtu": hpnicfMplsExtMtu,
       "hpnicfMplsExtRowStatus": hpnicfMplsExtRowStatus,
       "hpnicfMplsExtLdpTable": hpnicfMplsExtLdpTable,
       "hpnicfMplsExtLdpEntry": hpnicfMplsExtLdpEntry,
       "hpnicfMplsExtLdpIndex": hpnicfMplsExtLdpIndex,
       "hpnicfMplsExtLdpCapability": hpnicfMplsExtLdpCapability,
       "hpnicfMplsExtLdpRowStatus": hpnicfMplsExtLdpRowStatus}
)
