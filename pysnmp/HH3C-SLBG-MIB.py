# SNMP MIB module (HH3C-SLBG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-SLBG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:54:51 2024
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

hh3cSlbg = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 130)
)
hh3cSlbg.setRevisions(
        ("2012-10-16 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cSlbgMibTable_ObjectIdentity = ObjectIdentity
hh3cSlbgMibTable = _Hh3cSlbgMibTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 130, 1)
)
_Hh3cSlbgGroupTable_Object = MibTable
hh3cSlbgGroupTable = _Hh3cSlbgGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 130, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cSlbgGroupTable.setStatus("current")
_Hh3cSlbgGroupEntry_Object = MibTableRow
hh3cSlbgGroupEntry = _Hh3cSlbgGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 130, 1, 1, 1)
)
hh3cSlbgGroupEntry.setIndexNames(
    (0, "HH3C-SLBG-MIB", "hh3cSlbgGroupNumber"),
)
if mibBuilder.loadTexts:
    hh3cSlbgGroupEntry.setStatus("current")
_Hh3cSlbgGroupNumber_Type = Unsigned32
_Hh3cSlbgGroupNumber_Object = MibTableColumn
hh3cSlbgGroupNumber = _Hh3cSlbgGroupNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 130, 1, 1, 1, 1),
    _Hh3cSlbgGroupNumber_Type()
)
hh3cSlbgGroupNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cSlbgGroupNumber.setStatus("current")


class _Hh3cSlbgGroupSrvType_Type(Bits):
    """Custom type hh3cSlbgGroupSrvType based on Bits"""
    namedValues = NamedValues(
        *(("ipv6", 0),
          ("ipv6mc", 1),
          ("mpls", 4),
          ("multicastTunnel", 3),
          ("tunnel", 2))
    )

_Hh3cSlbgGroupSrvType_Type.__name__ = "Bits"
_Hh3cSlbgGroupSrvType_Object = MibTableColumn
hh3cSlbgGroupSrvType = _Hh3cSlbgGroupSrvType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 130, 1, 1, 1, 2),
    _Hh3cSlbgGroupSrvType_Type()
)
hh3cSlbgGroupSrvType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cSlbgGroupSrvType.setStatus("current")
_Hh3cSlbgGroupRowStatus_Type = RowStatus
_Hh3cSlbgGroupRowStatus_Object = MibTableColumn
hh3cSlbgGroupRowStatus = _Hh3cSlbgGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 130, 1, 1, 1, 3),
    _Hh3cSlbgGroupRowStatus_Type()
)
hh3cSlbgGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cSlbgGroupRowStatus.setStatus("current")
_Hh3cSlbgPortTable_Object = MibTable
hh3cSlbgPortTable = _Hh3cSlbgPortTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 130, 1, 2)
)
if mibBuilder.loadTexts:
    hh3cSlbgPortTable.setStatus("current")
_Hh3cSlbgPortEntry_Object = MibTableRow
hh3cSlbgPortEntry = _Hh3cSlbgPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 130, 1, 2, 1)
)
hh3cSlbgPortEntry.setIndexNames(
    (0, "HH3C-SLBG-MIB", "hh3cSlbgPortIndex"),
)
if mibBuilder.loadTexts:
    hh3cSlbgPortEntry.setStatus("current")
_Hh3cSlbgPortIndex_Type = InterfaceIndex
_Hh3cSlbgPortIndex_Object = MibTableColumn
hh3cSlbgPortIndex = _Hh3cSlbgPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 130, 1, 2, 1, 1),
    _Hh3cSlbgPortIndex_Type()
)
hh3cSlbgPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cSlbgPortIndex.setStatus("current")
_Hh3cSlbgPortAttachedGroupNumber_Type = Unsigned32
_Hh3cSlbgPortAttachedGroupNumber_Object = MibTableColumn
hh3cSlbgPortAttachedGroupNumber = _Hh3cSlbgPortAttachedGroupNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 130, 1, 2, 1, 2),
    _Hh3cSlbgPortAttachedGroupNumber_Type()
)
hh3cSlbgPortAttachedGroupNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cSlbgPortAttachedGroupNumber.setStatus("current")
_Hh3cSlbgPortSelectedGroupNumber_Type = Unsigned32
_Hh3cSlbgPortSelectedGroupNumber_Object = MibTableColumn
hh3cSlbgPortSelectedGroupNumber = _Hh3cSlbgPortSelectedGroupNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 130, 1, 2, 1, 3),
    _Hh3cSlbgPortSelectedGroupNumber_Type()
)
hh3cSlbgPortSelectedGroupNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSlbgPortSelectedGroupNumber.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-SLBG-MIB",
    **{"hh3cSlbg": hh3cSlbg,
       "hh3cSlbgMibTable": hh3cSlbgMibTable,
       "hh3cSlbgGroupTable": hh3cSlbgGroupTable,
       "hh3cSlbgGroupEntry": hh3cSlbgGroupEntry,
       "hh3cSlbgGroupNumber": hh3cSlbgGroupNumber,
       "hh3cSlbgGroupSrvType": hh3cSlbgGroupSrvType,
       "hh3cSlbgGroupRowStatus": hh3cSlbgGroupRowStatus,
       "hh3cSlbgPortTable": hh3cSlbgPortTable,
       "hh3cSlbgPortEntry": hh3cSlbgPortEntry,
       "hh3cSlbgPortIndex": hh3cSlbgPortIndex,
       "hh3cSlbgPortAttachedGroupNumber": hh3cSlbgPortAttachedGroupNumber,
       "hh3cSlbgPortSelectedGroupNumber": hh3cSlbgPortSelectedGroupNumber}
)
