# SNMP MIB module (HPN-ICF-SLBG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-SLBG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:01:48 2024
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

hpnicfSlbg = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 130)
)
hpnicfSlbg.setRevisions(
        ("2012-10-16 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpnicfSlbgMibTable_ObjectIdentity = ObjectIdentity
hpnicfSlbgMibTable = _HpnicfSlbgMibTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 130, 1)
)
_HpnicfSlbgGroupTable_Object = MibTable
hpnicfSlbgGroupTable = _HpnicfSlbgGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 130, 1, 1)
)
if mibBuilder.loadTexts:
    hpnicfSlbgGroupTable.setStatus("current")
_HpnicfSlbgGroupEntry_Object = MibTableRow
hpnicfSlbgGroupEntry = _HpnicfSlbgGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 130, 1, 1, 1)
)
hpnicfSlbgGroupEntry.setIndexNames(
    (0, "HPN-ICF-SLBG-MIB", "hpnicfSlbgGroupNumber"),
)
if mibBuilder.loadTexts:
    hpnicfSlbgGroupEntry.setStatus("current")
_HpnicfSlbgGroupNumber_Type = Unsigned32
_HpnicfSlbgGroupNumber_Object = MibTableColumn
hpnicfSlbgGroupNumber = _HpnicfSlbgGroupNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 130, 1, 1, 1, 1),
    _HpnicfSlbgGroupNumber_Type()
)
hpnicfSlbgGroupNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfSlbgGroupNumber.setStatus("current")


class _HpnicfSlbgGroupSrvType_Type(Bits):
    """Custom type hpnicfSlbgGroupSrvType based on Bits"""
    namedValues = NamedValues(
        *(("ipv6", 0),
          ("ipv6mc", 1),
          ("mpls", 4),
          ("multicastTunnel", 3),
          ("tunnel", 2))
    )

_HpnicfSlbgGroupSrvType_Type.__name__ = "Bits"
_HpnicfSlbgGroupSrvType_Object = MibTableColumn
hpnicfSlbgGroupSrvType = _HpnicfSlbgGroupSrvType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 130, 1, 1, 1, 2),
    _HpnicfSlbgGroupSrvType_Type()
)
hpnicfSlbgGroupSrvType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfSlbgGroupSrvType.setStatus("current")
_HpnicfSlbgGroupRowStatus_Type = RowStatus
_HpnicfSlbgGroupRowStatus_Object = MibTableColumn
hpnicfSlbgGroupRowStatus = _HpnicfSlbgGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 130, 1, 1, 1, 3),
    _HpnicfSlbgGroupRowStatus_Type()
)
hpnicfSlbgGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfSlbgGroupRowStatus.setStatus("current")
_HpnicfSlbgPortTable_Object = MibTable
hpnicfSlbgPortTable = _HpnicfSlbgPortTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 130, 1, 2)
)
if mibBuilder.loadTexts:
    hpnicfSlbgPortTable.setStatus("current")
_HpnicfSlbgPortEntry_Object = MibTableRow
hpnicfSlbgPortEntry = _HpnicfSlbgPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 130, 1, 2, 1)
)
hpnicfSlbgPortEntry.setIndexNames(
    (0, "HPN-ICF-SLBG-MIB", "hpnicfSlbgPortIndex"),
)
if mibBuilder.loadTexts:
    hpnicfSlbgPortEntry.setStatus("current")
_HpnicfSlbgPortIndex_Type = InterfaceIndex
_HpnicfSlbgPortIndex_Object = MibTableColumn
hpnicfSlbgPortIndex = _HpnicfSlbgPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 130, 1, 2, 1, 1),
    _HpnicfSlbgPortIndex_Type()
)
hpnicfSlbgPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfSlbgPortIndex.setStatus("current")
_HpnicfSlbgPortAttachedGroupNumber_Type = Unsigned32
_HpnicfSlbgPortAttachedGroupNumber_Object = MibTableColumn
hpnicfSlbgPortAttachedGroupNumber = _HpnicfSlbgPortAttachedGroupNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 130, 1, 2, 1, 2),
    _HpnicfSlbgPortAttachedGroupNumber_Type()
)
hpnicfSlbgPortAttachedGroupNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfSlbgPortAttachedGroupNumber.setStatus("current")
_HpnicfSlbgPortSelectedGroupNumber_Type = Unsigned32
_HpnicfSlbgPortSelectedGroupNumber_Object = MibTableColumn
hpnicfSlbgPortSelectedGroupNumber = _HpnicfSlbgPortSelectedGroupNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 130, 1, 2, 1, 3),
    _HpnicfSlbgPortSelectedGroupNumber_Type()
)
hpnicfSlbgPortSelectedGroupNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfSlbgPortSelectedGroupNumber.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-SLBG-MIB",
    **{"hpnicfSlbg": hpnicfSlbg,
       "hpnicfSlbgMibTable": hpnicfSlbgMibTable,
       "hpnicfSlbgGroupTable": hpnicfSlbgGroupTable,
       "hpnicfSlbgGroupEntry": hpnicfSlbgGroupEntry,
       "hpnicfSlbgGroupNumber": hpnicfSlbgGroupNumber,
       "hpnicfSlbgGroupSrvType": hpnicfSlbgGroupSrvType,
       "hpnicfSlbgGroupRowStatus": hpnicfSlbgGroupRowStatus,
       "hpnicfSlbgPortTable": hpnicfSlbgPortTable,
       "hpnicfSlbgPortEntry": hpnicfSlbgPortEntry,
       "hpnicfSlbgPortIndex": hpnicfSlbgPortIndex,
       "hpnicfSlbgPortAttachedGroupNumber": hpnicfSlbgPortAttachedGroupNumber,
       "hpnicfSlbgPortSelectedGroupNumber": hpnicfSlbgPortSelectedGroupNumber}
)
