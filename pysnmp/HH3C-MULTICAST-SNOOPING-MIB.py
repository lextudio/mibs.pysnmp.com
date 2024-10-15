# SNMP MIB module (HH3C-MULTICAST-SNOOPING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-MULTICAST-SNOOPING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:54:17 2024
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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

hh3cMulticastSnoop = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 123)
)
hh3cMulticastSnoop.setRevisions(
        ("2014-05-14 17:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Hh3cVirtualUnitType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vlan", 1),
          ("vsi", 2))
    )



# MIB Managed Objects in the order of their OIDs

_Hh3cMulticastSnoopObject_ObjectIdentity = ObjectIdentity
hh3cMulticastSnoopObject = _Hh3cMulticastSnoopObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 123, 1)
)
_Hh3cMcsGlobalConfigTable_Object = MibTable
hh3cMcsGlobalConfigTable = _Hh3cMcsGlobalConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cMcsGlobalConfigTable.setStatus("current")
_Hh3cMcsGlobalConfigEntry_Object = MibTableRow
hh3cMcsGlobalConfigEntry = _Hh3cMcsGlobalConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 1, 1)
)
hh3cMcsGlobalConfigEntry.setIndexNames(
    (0, "HH3C-MULTICAST-SNOOPING-MIB", "hh3cMcsGlbSnoopingType"),
)
if mibBuilder.loadTexts:
    hh3cMcsGlobalConfigEntry.setStatus("current")
_Hh3cMcsGlbSnoopingType_Type = InetAddressType
_Hh3cMcsGlbSnoopingType_Object = MibTableColumn
hh3cMcsGlbSnoopingType = _Hh3cMcsGlbSnoopingType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 1, 1, 1),
    _Hh3cMcsGlbSnoopingType_Type()
)
hh3cMcsGlbSnoopingType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cMcsGlbSnoopingType.setStatus("current")
_Hh3cMcsGlbRowStatus_Type = RowStatus
_Hh3cMcsGlbRowStatus_Object = MibTableColumn
hh3cMcsGlbRowStatus = _Hh3cMcsGlbRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 1, 1, 2),
    _Hh3cMcsGlbRowStatus_Type()
)
hh3cMcsGlbRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMcsGlbRowStatus.setStatus("current")
_Hh3cMcsGlbEntryLimit_Type = Unsigned32
_Hh3cMcsGlbEntryLimit_Object = MibTableColumn
hh3cMcsGlbEntryLimit = _Hh3cMcsGlbEntryLimit_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 1, 1, 3),
    _Hh3cMcsGlbEntryLimit_Type()
)
hh3cMcsGlbEntryLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMcsGlbEntryLimit.setStatus("current")


class _Hh3cMcsGlbHostAgingTime_Type(Unsigned32):
    """Custom type hh3cMcsGlbHostAgingTime based on Unsigned32"""
    defaultValue = 260

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8097894),
    )


_Hh3cMcsGlbHostAgingTime_Type.__name__ = "Unsigned32"
_Hh3cMcsGlbHostAgingTime_Object = MibTableColumn
hh3cMcsGlbHostAgingTime = _Hh3cMcsGlbHostAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 1, 1, 4),
    _Hh3cMcsGlbHostAgingTime_Type()
)
hh3cMcsGlbHostAgingTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMcsGlbHostAgingTime.setStatus("current")


class _Hh3cMcsGlbMaxResponseTime_Type(Unsigned32):
    """Custom type hh3cMcsGlbMaxResponseTime based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3174),
    )


_Hh3cMcsGlbMaxResponseTime_Type.__name__ = "Unsigned32"
_Hh3cMcsGlbMaxResponseTime_Object = MibTableColumn
hh3cMcsGlbMaxResponseTime = _Hh3cMcsGlbMaxResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 1, 1, 5),
    _Hh3cMcsGlbMaxResponseTime_Type()
)
hh3cMcsGlbMaxResponseTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMcsGlbMaxResponseTime.setStatus("current")


class _Hh3cMcsGlbRouterAgingTime_Type(Unsigned32):
    """Custom type hh3cMcsGlbRouterAgingTime based on Unsigned32"""
    defaultValue = 260

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8097894),
    )


_Hh3cMcsGlbRouterAgingTime_Type.__name__ = "Unsigned32"
_Hh3cMcsGlbRouterAgingTime_Object = MibTableColumn
hh3cMcsGlbRouterAgingTime = _Hh3cMcsGlbRouterAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 1, 1, 6),
    _Hh3cMcsGlbRouterAgingTime_Type()
)
hh3cMcsGlbRouterAgingTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMcsGlbRouterAgingTime.setStatus("current")


class _Hh3cMcsGlbLastMemQryInterval_Type(Unsigned32):
    """Custom type hh3cMcsGlbLastMemQryInterval based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 25),
    )


_Hh3cMcsGlbLastMemQryInterval_Type.__name__ = "Unsigned32"
_Hh3cMcsGlbLastMemQryInterval_Object = MibTableColumn
hh3cMcsGlbLastMemQryInterval = _Hh3cMcsGlbLastMemQryInterval_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 1, 1, 7),
    _Hh3cMcsGlbLastMemQryInterval_Type()
)
hh3cMcsGlbLastMemQryInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMcsGlbLastMemQryInterval.setStatus("current")


class _Hh3cMcsGlbDropUnknownEnabled_Type(TruthValue):
    """Custom type hh3cMcsGlbDropUnknownEnabled based on TruthValue"""


_Hh3cMcsGlbDropUnknownEnabled_Object = MibTableColumn
hh3cMcsGlbDropUnknownEnabled = _Hh3cMcsGlbDropUnknownEnabled_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 1, 1, 8),
    _Hh3cMcsGlbDropUnknownEnabled_Type()
)
hh3cMcsGlbDropUnknownEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMcsGlbDropUnknownEnabled.setStatus("current")
_Hh3cMcsVirtualUnitConfigTable_Object = MibTable
hh3cMcsVirtualUnitConfigTable = _Hh3cMcsVirtualUnitConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 2)
)
if mibBuilder.loadTexts:
    hh3cMcsVirtualUnitConfigTable.setStatus("current")
_Hh3cMcsVirtualUnitConfigEntry_Object = MibTableRow
hh3cMcsVirtualUnitConfigEntry = _Hh3cMcsVirtualUnitConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 2, 1)
)
hh3cMcsVirtualUnitConfigEntry.setIndexNames(
    (0, "HH3C-MULTICAST-SNOOPING-MIB", "hh3cMcsVUType"),
    (0, "HH3C-MULTICAST-SNOOPING-MIB", "hh3cMcsVUID"),
    (0, "HH3C-MULTICAST-SNOOPING-MIB", "hh3cMcsVUSnoopingType"),
)
if mibBuilder.loadTexts:
    hh3cMcsVirtualUnitConfigEntry.setStatus("current")
_Hh3cMcsVUType_Type = Hh3cVirtualUnitType
_Hh3cMcsVUType_Object = MibTableColumn
hh3cMcsVUType = _Hh3cMcsVUType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 2, 1, 1),
    _Hh3cMcsVUType_Type()
)
hh3cMcsVUType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cMcsVUType.setStatus("current")
_Hh3cMcsVUID_Type = Unsigned32
_Hh3cMcsVUID_Object = MibTableColumn
hh3cMcsVUID = _Hh3cMcsVUID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 2, 1, 2),
    _Hh3cMcsVUID_Type()
)
hh3cMcsVUID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cMcsVUID.setStatus("current")
_Hh3cMcsVUSnoopingType_Type = InetAddressType
_Hh3cMcsVUSnoopingType_Object = MibTableColumn
hh3cMcsVUSnoopingType = _Hh3cMcsVUSnoopingType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 2, 1, 3),
    _Hh3cMcsVUSnoopingType_Type()
)
hh3cMcsVUSnoopingType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cMcsVUSnoopingType.setStatus("current")
_Hh3cMcsVURowStatus_Type = RowStatus
_Hh3cMcsVURowStatus_Object = MibTableColumn
hh3cMcsVURowStatus = _Hh3cMcsVURowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 2, 1, 4),
    _Hh3cMcsVURowStatus_Type()
)
hh3cMcsVURowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMcsVURowStatus.setStatus("current")


class _Hh3cMcsVUHostAgingTime_Type(Unsigned32):
    """Custom type hh3cMcsVUHostAgingTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8097894),
    )


_Hh3cMcsVUHostAgingTime_Type.__name__ = "Unsigned32"
_Hh3cMcsVUHostAgingTime_Object = MibTableColumn
hh3cMcsVUHostAgingTime = _Hh3cMcsVUHostAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 2, 1, 5),
    _Hh3cMcsVUHostAgingTime_Type()
)
hh3cMcsVUHostAgingTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMcsVUHostAgingTime.setStatus("current")


class _Hh3cMcsVUMaxResponseTime_Type(Unsigned32):
    """Custom type hh3cMcsVUMaxResponseTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3174),
    )


_Hh3cMcsVUMaxResponseTime_Type.__name__ = "Unsigned32"
_Hh3cMcsVUMaxResponseTime_Object = MibTableColumn
hh3cMcsVUMaxResponseTime = _Hh3cMcsVUMaxResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 2, 1, 6),
    _Hh3cMcsVUMaxResponseTime_Type()
)
hh3cMcsVUMaxResponseTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMcsVUMaxResponseTime.setStatus("current")


class _Hh3cMcsVURouterAgingTime_Type(Unsigned32):
    """Custom type hh3cMcsVURouterAgingTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8097894),
    )


_Hh3cMcsVURouterAgingTime_Type.__name__ = "Unsigned32"
_Hh3cMcsVURouterAgingTime_Object = MibTableColumn
hh3cMcsVURouterAgingTime = _Hh3cMcsVURouterAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 2, 1, 7),
    _Hh3cMcsVURouterAgingTime_Type()
)
hh3cMcsVURouterAgingTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMcsVURouterAgingTime.setStatus("current")


class _Hh3cMcsVULastMemQryInterval_Type(Unsigned32):
    """Custom type hh3cMcsVULastMemQryInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 25),
    )


_Hh3cMcsVULastMemQryInterval_Type.__name__ = "Unsigned32"
_Hh3cMcsVULastMemQryInterval_Object = MibTableColumn
hh3cMcsVULastMemQryInterval = _Hh3cMcsVULastMemQryInterval_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 2, 1, 8),
    _Hh3cMcsVULastMemQryInterval_Type()
)
hh3cMcsVULastMemQryInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMcsVULastMemQryInterval.setStatus("current")


class _Hh3cMcsVUDropUnknownEnabled_Type(TruthValue):
    """Custom type hh3cMcsVUDropUnknownEnabled based on TruthValue"""


_Hh3cMcsVUDropUnknownEnabled_Object = MibTableColumn
hh3cMcsVUDropUnknownEnabled = _Hh3cMcsVUDropUnknownEnabled_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 2, 1, 9),
    _Hh3cMcsVUDropUnknownEnabled_Type()
)
hh3cMcsVUDropUnknownEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMcsVUDropUnknownEnabled.setStatus("current")


class _Hh3cMcsVUPimSnoopingEnabled_Type(TruthValue):
    """Custom type hh3cMcsVUPimSnoopingEnabled based on TruthValue"""


_Hh3cMcsVUPimSnoopingEnabled_Object = MibTableColumn
hh3cMcsVUPimSnoopingEnabled = _Hh3cMcsVUPimSnoopingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 2, 1, 10),
    _Hh3cMcsVUPimSnoopingEnabled_Type()
)
hh3cMcsVUPimSnoopingEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMcsVUPimSnoopingEnabled.setStatus("current")


class _Hh3cMcsVUVersion_Type(Unsigned32):
    """Custom type hh3cMcsVUVersion based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(3, 3),
    )


_Hh3cMcsVUVersion_Type.__name__ = "Unsigned32"
_Hh3cMcsVUVersion_Object = MibTableColumn
hh3cMcsVUVersion = _Hh3cMcsVUVersion_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 2, 1, 11),
    _Hh3cMcsVUVersion_Type()
)
hh3cMcsVUVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMcsVUVersion.setStatus("current")


class _Hh3cMcsVUQuerierEnabled_Type(TruthValue):
    """Custom type hh3cMcsVUQuerierEnabled based on TruthValue"""


_Hh3cMcsVUQuerierEnabled_Object = MibTableColumn
hh3cMcsVUQuerierEnabled = _Hh3cMcsVUQuerierEnabled_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 2, 1, 12),
    _Hh3cMcsVUQuerierEnabled_Type()
)
hh3cMcsVUQuerierEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMcsVUQuerierEnabled.setStatus("current")


class _Hh3cMcsVUQuerierInterval_Type(Unsigned32):
    """Custom type hh3cMcsVUQuerierInterval based on Unsigned32"""
    defaultValue = 125

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 31744),
    )


_Hh3cMcsVUQuerierInterval_Type.__name__ = "Unsigned32"
_Hh3cMcsVUQuerierInterval_Object = MibTableColumn
hh3cMcsVUQuerierInterval = _Hh3cMcsVUQuerierInterval_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 2, 1, 13),
    _Hh3cMcsVUQuerierInterval_Type()
)
hh3cMcsVUQuerierInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMcsVUQuerierInterval.setStatus("current")
_Hh3cMcsVUGeneQuerierSourceAddress_Type = InetAddress
_Hh3cMcsVUGeneQuerierSourceAddress_Object = MibTableColumn
hh3cMcsVUGeneQuerierSourceAddress = _Hh3cMcsVUGeneQuerierSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 2, 1, 14),
    _Hh3cMcsVUGeneQuerierSourceAddress_Type()
)
hh3cMcsVUGeneQuerierSourceAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMcsVUGeneQuerierSourceAddress.setStatus("current")
_Hh3cMcsVUSpecQuerierSourceAddress_Type = InetAddress
_Hh3cMcsVUSpecQuerierSourceAddress_Object = MibTableColumn
hh3cMcsVUSpecQuerierSourceAddress = _Hh3cMcsVUSpecQuerierSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 2, 1, 15),
    _Hh3cMcsVUSpecQuerierSourceAddress_Type()
)
hh3cMcsVUSpecQuerierSourceAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMcsVUSpecQuerierSourceAddress.setStatus("current")
_Hh3cMcsVULeaveSourceAddress_Type = InetAddress
_Hh3cMcsVULeaveSourceAddress_Object = MibTableColumn
hh3cMcsVULeaveSourceAddress = _Hh3cMcsVULeaveSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 2, 1, 16),
    _Hh3cMcsVULeaveSourceAddress_Type()
)
hh3cMcsVULeaveSourceAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMcsVULeaveSourceAddress.setStatus("current")
_Hh3cMcsVUReportSourceAddress_Type = InetAddress
_Hh3cMcsVUReportSourceAddress_Object = MibTableColumn
hh3cMcsVUReportSourceAddress = _Hh3cMcsVUReportSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 2, 1, 17),
    _Hh3cMcsVUReportSourceAddress_Type()
)
hh3cMcsVUReportSourceAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMcsVUReportSourceAddress.setStatus("current")
_Hh3cMcsL2EntryTable_Object = MibTable
hh3cMcsL2EntryTable = _Hh3cMcsL2EntryTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 3)
)
if mibBuilder.loadTexts:
    hh3cMcsL2EntryTable.setStatus("current")
_Hh3cMcsL2EntryEntry_Object = MibTableRow
hh3cMcsL2EntryEntry = _Hh3cMcsL2EntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 3, 1)
)
hh3cMcsL2EntryEntry.setIndexNames(
    (0, "HH3C-MULTICAST-SNOOPING-MIB", "hh3cMcsL2EntryVUType"),
    (0, "HH3C-MULTICAST-SNOOPING-MIB", "hh3cMcsL2EntryVUID"),
    (0, "HH3C-MULTICAST-SNOOPING-MIB", "hh3cMcsL2EntryAddressType"),
    (0, "HH3C-MULTICAST-SNOOPING-MIB", "hh3cMcsL2EntryGroupAddress"),
    (0, "HH3C-MULTICAST-SNOOPING-MIB", "hh3cMcsL2EntrySourceAddress"),
    (0, "HH3C-MULTICAST-SNOOPING-MIB", "hh3cMcsL2EntryIfIndex"),
)
if mibBuilder.loadTexts:
    hh3cMcsL2EntryEntry.setStatus("current")
_Hh3cMcsL2EntryVUType_Type = Hh3cVirtualUnitType
_Hh3cMcsL2EntryVUType_Object = MibTableColumn
hh3cMcsL2EntryVUType = _Hh3cMcsL2EntryVUType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 3, 1, 1),
    _Hh3cMcsL2EntryVUType_Type()
)
hh3cMcsL2EntryVUType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cMcsL2EntryVUType.setStatus("current")
_Hh3cMcsL2EntryVUID_Type = Unsigned32
_Hh3cMcsL2EntryVUID_Object = MibTableColumn
hh3cMcsL2EntryVUID = _Hh3cMcsL2EntryVUID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 3, 1, 2),
    _Hh3cMcsL2EntryVUID_Type()
)
hh3cMcsL2EntryVUID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cMcsL2EntryVUID.setStatus("current")
_Hh3cMcsL2EntryAddressType_Type = InetAddressType
_Hh3cMcsL2EntryAddressType_Object = MibTableColumn
hh3cMcsL2EntryAddressType = _Hh3cMcsL2EntryAddressType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 3, 1, 3),
    _Hh3cMcsL2EntryAddressType_Type()
)
hh3cMcsL2EntryAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cMcsL2EntryAddressType.setStatus("current")
_Hh3cMcsL2EntryGroupAddress_Type = InetAddress
_Hh3cMcsL2EntryGroupAddress_Object = MibTableColumn
hh3cMcsL2EntryGroupAddress = _Hh3cMcsL2EntryGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 3, 1, 4),
    _Hh3cMcsL2EntryGroupAddress_Type()
)
hh3cMcsL2EntryGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cMcsL2EntryGroupAddress.setStatus("current")
_Hh3cMcsL2EntrySourceAddress_Type = InetAddress
_Hh3cMcsL2EntrySourceAddress_Object = MibTableColumn
hh3cMcsL2EntrySourceAddress = _Hh3cMcsL2EntrySourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 3, 1, 5),
    _Hh3cMcsL2EntrySourceAddress_Type()
)
hh3cMcsL2EntrySourceAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cMcsL2EntrySourceAddress.setStatus("current")
_Hh3cMcsL2EntryIfIndex_Type = InterfaceIndex
_Hh3cMcsL2EntryIfIndex_Object = MibTableColumn
hh3cMcsL2EntryIfIndex = _Hh3cMcsL2EntryIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 3, 1, 6),
    _Hh3cMcsL2EntryIfIndex_Type()
)
hh3cMcsL2EntryIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cMcsL2EntryIfIndex.setStatus("current")


class _Hh3cMcsL2EntryPortType_Type(Integer32):
    """Custom type hh3cMcsL2EntryPortType based on Integer32"""
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
        *(("ac", 2),
          ("interface", 1),
          ("npw", 3),
          ("trill", 5),
          ("upw", 4))
    )


_Hh3cMcsL2EntryPortType_Type.__name__ = "Integer32"
_Hh3cMcsL2EntryPortType_Object = MibTableColumn
hh3cMcsL2EntryPortType = _Hh3cMcsL2EntryPortType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 3, 1, 7),
    _Hh3cMcsL2EntryPortType_Type()
)
hh3cMcsL2EntryPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMcsL2EntryPortType.setStatus("current")


class _Hh3cMcsL2EntryPortAttribute_Type(Bits):
    """Custom type hh3cMcsL2EntryPortAttribute based on Bits"""
    namedValues = NamedValues(
        *(("d", 0),
          ("k", 3),
          ("p", 2),
          ("r", 4),
          ("s", 1),
          ("w", 5))
    )

_Hh3cMcsL2EntryPortAttribute_Type.__name__ = "Bits"
_Hh3cMcsL2EntryPortAttribute_Object = MibTableColumn
hh3cMcsL2EntryPortAttribute = _Hh3cMcsL2EntryPortAttribute_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 3, 1, 8),
    _Hh3cMcsL2EntryPortAttribute_Type()
)
hh3cMcsL2EntryPortAttribute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMcsL2EntryPortAttribute.setStatus("current")
_Hh3cMcsPacketStatisticsTable_Object = MibTable
hh3cMcsPacketStatisticsTable = _Hh3cMcsPacketStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 4)
)
if mibBuilder.loadTexts:
    hh3cMcsPacketStatisticsTable.setStatus("current")
_Hh3cMcsPacketStatisticsEntry_Object = MibTableRow
hh3cMcsPacketStatisticsEntry = _Hh3cMcsPacketStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 4, 1)
)
hh3cMcsPacketStatisticsEntry.setIndexNames(
    (0, "HH3C-MULTICAST-SNOOPING-MIB", "hh3cMcsStatisticsSnoopingType"),
)
if mibBuilder.loadTexts:
    hh3cMcsPacketStatisticsEntry.setStatus("current")
_Hh3cMcsStatisticsSnoopingType_Type = InetAddressType
_Hh3cMcsStatisticsSnoopingType_Object = MibTableColumn
hh3cMcsStatisticsSnoopingType = _Hh3cMcsStatisticsSnoopingType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 4, 1, 1),
    _Hh3cMcsStatisticsSnoopingType_Type()
)
hh3cMcsStatisticsSnoopingType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cMcsStatisticsSnoopingType.setStatus("current")
_Hh3cMcsRxGeneryQueryNum_Type = Counter64
_Hh3cMcsRxGeneryQueryNum_Object = MibTableColumn
hh3cMcsRxGeneryQueryNum = _Hh3cMcsRxGeneryQueryNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 4, 1, 2),
    _Hh3cMcsRxGeneryQueryNum_Type()
)
hh3cMcsRxGeneryQueryNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMcsRxGeneryQueryNum.setStatus("current")
_Hh3cMcsRxV2SpecificQueryNum_Type = Counter64
_Hh3cMcsRxV2SpecificQueryNum_Object = MibTableColumn
hh3cMcsRxV2SpecificQueryNum = _Hh3cMcsRxV2SpecificQueryNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 4, 1, 3),
    _Hh3cMcsRxV2SpecificQueryNum_Type()
)
hh3cMcsRxV2SpecificQueryNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMcsRxV2SpecificQueryNum.setStatus("current")
_Hh3cMcsRxV3SpecificQueryNum_Type = Counter64
_Hh3cMcsRxV3SpecificQueryNum_Object = MibTableColumn
hh3cMcsRxV3SpecificQueryNum = _Hh3cMcsRxV3SpecificQueryNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 4, 1, 4),
    _Hh3cMcsRxV3SpecificQueryNum_Type()
)
hh3cMcsRxV3SpecificQueryNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMcsRxV3SpecificQueryNum.setStatus("current")
_Hh3cMcsRxV3SpecificSGQueryNum_Type = Counter64
_Hh3cMcsRxV3SpecificSGQueryNum_Object = MibTableColumn
hh3cMcsRxV3SpecificSGQueryNum = _Hh3cMcsRxV3SpecificSGQueryNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 4, 1, 5),
    _Hh3cMcsRxV3SpecificSGQueryNum_Type()
)
hh3cMcsRxV3SpecificSGQueryNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMcsRxV3SpecificSGQueryNum.setStatus("current")
_Hh3cMcsRxV1ReportNum_Type = Counter64
_Hh3cMcsRxV1ReportNum_Object = MibTableColumn
hh3cMcsRxV1ReportNum = _Hh3cMcsRxV1ReportNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 4, 1, 6),
    _Hh3cMcsRxV1ReportNum_Type()
)
hh3cMcsRxV1ReportNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMcsRxV1ReportNum.setStatus("current")
_Hh3cMcsRxV2ReportNum_Type = Counter64
_Hh3cMcsRxV2ReportNum_Object = MibTableColumn
hh3cMcsRxV2ReportNum = _Hh3cMcsRxV2ReportNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 4, 1, 7),
    _Hh3cMcsRxV2ReportNum_Type()
)
hh3cMcsRxV2ReportNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMcsRxV2ReportNum.setStatus("current")
_Hh3cMcsRxV3ReportNum_Type = Counter64
_Hh3cMcsRxV3ReportNum_Object = MibTableColumn
hh3cMcsRxV3ReportNum = _Hh3cMcsRxV3ReportNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 4, 1, 8),
    _Hh3cMcsRxV3ReportNum_Type()
)
hh3cMcsRxV3ReportNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMcsRxV3ReportNum.setStatus("current")
_Hh3cMcsRxV3ErrCorReportNum_Type = Counter64
_Hh3cMcsRxV3ErrCorReportNum_Object = MibTableColumn
hh3cMcsRxV3ErrCorReportNum = _Hh3cMcsRxV3ErrCorReportNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 4, 1, 9),
    _Hh3cMcsRxV3ErrCorReportNum_Type()
)
hh3cMcsRxV3ErrCorReportNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMcsRxV3ErrCorReportNum.setStatus("current")
_Hh3cMcsRxLeaveNum_Type = Counter64
_Hh3cMcsRxLeaveNum_Object = MibTableColumn
hh3cMcsRxLeaveNum = _Hh3cMcsRxLeaveNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 4, 1, 10),
    _Hh3cMcsRxLeaveNum_Type()
)
hh3cMcsRxLeaveNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMcsRxLeaveNum.setStatus("current")
_Hh3cMcsRxPimHelloNum_Type = Counter64
_Hh3cMcsRxPimHelloNum_Object = MibTableColumn
hh3cMcsRxPimHelloNum = _Hh3cMcsRxPimHelloNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 4, 1, 11),
    _Hh3cMcsRxPimHelloNum_Type()
)
hh3cMcsRxPimHelloNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMcsRxPimHelloNum.setStatus("current")
_Hh3cMcsRxErrorPacketNum_Type = Counter64
_Hh3cMcsRxErrorPacketNum_Object = MibTableColumn
hh3cMcsRxErrorPacketNum = _Hh3cMcsRxErrorPacketNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 4, 1, 12),
    _Hh3cMcsRxErrorPacketNum_Type()
)
hh3cMcsRxErrorPacketNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMcsRxErrorPacketNum.setStatus("current")
_Hh3cMcsTxV2SpecificQueryNum_Type = Counter64
_Hh3cMcsTxV2SpecificQueryNum_Object = MibTableColumn
hh3cMcsTxV2SpecificQueryNum = _Hh3cMcsTxV2SpecificQueryNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 4, 1, 13),
    _Hh3cMcsTxV2SpecificQueryNum_Type()
)
hh3cMcsTxV2SpecificQueryNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMcsTxV2SpecificQueryNum.setStatus("current")
_Hh3cMcsTxV3SpecificQueryNum_Type = Counter64
_Hh3cMcsTxV3SpecificQueryNum_Object = MibTableColumn
hh3cMcsTxV3SpecificQueryNum = _Hh3cMcsTxV3SpecificQueryNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 4, 1, 14),
    _Hh3cMcsTxV3SpecificQueryNum_Type()
)
hh3cMcsTxV3SpecificQueryNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMcsTxV3SpecificQueryNum.setStatus("current")
_Hh3cMcsTxV3SpecificSGQueryNum_Type = Counter64
_Hh3cMcsTxV3SpecificSGQueryNum_Object = MibTableColumn
hh3cMcsTxV3SpecificSGQueryNum = _Hh3cMcsTxV3SpecificSGQueryNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 4, 1, 15),
    _Hh3cMcsTxV3SpecificSGQueryNum_Type()
)
hh3cMcsTxV3SpecificSGQueryNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMcsTxV3SpecificSGQueryNum.setStatus("current")
_Hh3cMcsPortJoinGroupConfigTable_Object = MibTable
hh3cMcsPortJoinGroupConfigTable = _Hh3cMcsPortJoinGroupConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 5)
)
if mibBuilder.loadTexts:
    hh3cMcsPortJoinGroupConfigTable.setStatus("current")
_Hh3cMcsPortJoinGroupConfigEntry_Object = MibTableRow
hh3cMcsPortJoinGroupConfigEntry = _Hh3cMcsPortJoinGroupConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 5, 1)
)
hh3cMcsPortJoinGroupConfigEntry.setIndexNames(
    (0, "HH3C-MULTICAST-SNOOPING-MIB", "hh3cMcsPortJoinGroupIfIndex"),
    (0, "HH3C-MULTICAST-SNOOPING-MIB", "hh3cMcsPortJoinGroupSnoopingType"),
    (0, "HH3C-MULTICAST-SNOOPING-MIB", "hh3cMcsPortJoinGroupVlanID"),
    (0, "HH3C-MULTICAST-SNOOPING-MIB", "hh3cMcsPortJoinGroupGroupAddress"),
    (0, "HH3C-MULTICAST-SNOOPING-MIB", "hh3cMcsPortJoinGroupSourceAddress"),
)
if mibBuilder.loadTexts:
    hh3cMcsPortJoinGroupConfigEntry.setStatus("current")
_Hh3cMcsPortJoinGroupIfIndex_Type = InterfaceIndex
_Hh3cMcsPortJoinGroupIfIndex_Object = MibTableColumn
hh3cMcsPortJoinGroupIfIndex = _Hh3cMcsPortJoinGroupIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 5, 1, 1),
    _Hh3cMcsPortJoinGroupIfIndex_Type()
)
hh3cMcsPortJoinGroupIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cMcsPortJoinGroupIfIndex.setStatus("current")
_Hh3cMcsPortJoinGroupSnoopingType_Type = InetAddressType
_Hh3cMcsPortJoinGroupSnoopingType_Object = MibTableColumn
hh3cMcsPortJoinGroupSnoopingType = _Hh3cMcsPortJoinGroupSnoopingType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 5, 1, 2),
    _Hh3cMcsPortJoinGroupSnoopingType_Type()
)
hh3cMcsPortJoinGroupSnoopingType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cMcsPortJoinGroupSnoopingType.setStatus("current")


class _Hh3cMcsPortJoinGroupVlanID_Type(Unsigned32):
    """Custom type hh3cMcsPortJoinGroupVlanID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Hh3cMcsPortJoinGroupVlanID_Type.__name__ = "Unsigned32"
_Hh3cMcsPortJoinGroupVlanID_Object = MibTableColumn
hh3cMcsPortJoinGroupVlanID = _Hh3cMcsPortJoinGroupVlanID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 5, 1, 3),
    _Hh3cMcsPortJoinGroupVlanID_Type()
)
hh3cMcsPortJoinGroupVlanID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cMcsPortJoinGroupVlanID.setStatus("current")
_Hh3cMcsPortJoinGroupGroupAddress_Type = InetAddress
_Hh3cMcsPortJoinGroupGroupAddress_Object = MibTableColumn
hh3cMcsPortJoinGroupGroupAddress = _Hh3cMcsPortJoinGroupGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 5, 1, 4),
    _Hh3cMcsPortJoinGroupGroupAddress_Type()
)
hh3cMcsPortJoinGroupGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cMcsPortJoinGroupGroupAddress.setStatus("current")
_Hh3cMcsPortJoinGroupSourceAddress_Type = InetAddress
_Hh3cMcsPortJoinGroupSourceAddress_Object = MibTableColumn
hh3cMcsPortJoinGroupSourceAddress = _Hh3cMcsPortJoinGroupSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 5, 1, 5),
    _Hh3cMcsPortJoinGroupSourceAddress_Type()
)
hh3cMcsPortJoinGroupSourceAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cMcsPortJoinGroupSourceAddress.setStatus("current")
_Hh3cMcsPortJoinGroupStatus_Type = RowStatus
_Hh3cMcsPortJoinGroupStatus_Object = MibTableColumn
hh3cMcsPortJoinGroupStatus = _Hh3cMcsPortJoinGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 5, 1, 6),
    _Hh3cMcsPortJoinGroupStatus_Type()
)
hh3cMcsPortJoinGroupStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMcsPortJoinGroupStatus.setStatus("current")
_Hh3cMcsPortStaticGroupConfigTable_Object = MibTable
hh3cMcsPortStaticGroupConfigTable = _Hh3cMcsPortStaticGroupConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 6)
)
if mibBuilder.loadTexts:
    hh3cMcsPortStaticGroupConfigTable.setStatus("current")
_Hh3cMcsPortStaticGroupConfigEntry_Object = MibTableRow
hh3cMcsPortStaticGroupConfigEntry = _Hh3cMcsPortStaticGroupConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 6, 1)
)
hh3cMcsPortStaticGroupConfigEntry.setIndexNames(
    (0, "HH3C-MULTICAST-SNOOPING-MIB", "hh3cMcsPortStaticGroupIfIndex"),
    (0, "HH3C-MULTICAST-SNOOPING-MIB", "hh3cMcsPortStaticGroupSnoopingType"),
    (0, "HH3C-MULTICAST-SNOOPING-MIB", "hh3cMcsPortStaticGroupVlanID"),
    (0, "HH3C-MULTICAST-SNOOPING-MIB", "hh3cMcsPortStaticGroupGroupAddress"),
    (0, "HH3C-MULTICAST-SNOOPING-MIB", "hh3cMcsPortStaticGroupSourceAddress"),
)
if mibBuilder.loadTexts:
    hh3cMcsPortStaticGroupConfigEntry.setStatus("current")
_Hh3cMcsPortStaticGroupIfIndex_Type = InterfaceIndex
_Hh3cMcsPortStaticGroupIfIndex_Object = MibTableColumn
hh3cMcsPortStaticGroupIfIndex = _Hh3cMcsPortStaticGroupIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 6, 1, 1),
    _Hh3cMcsPortStaticGroupIfIndex_Type()
)
hh3cMcsPortStaticGroupIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cMcsPortStaticGroupIfIndex.setStatus("current")
_Hh3cMcsPortStaticGroupSnoopingType_Type = InetAddressType
_Hh3cMcsPortStaticGroupSnoopingType_Object = MibTableColumn
hh3cMcsPortStaticGroupSnoopingType = _Hh3cMcsPortStaticGroupSnoopingType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 6, 1, 2),
    _Hh3cMcsPortStaticGroupSnoopingType_Type()
)
hh3cMcsPortStaticGroupSnoopingType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cMcsPortStaticGroupSnoopingType.setStatus("current")


class _Hh3cMcsPortStaticGroupVlanID_Type(Unsigned32):
    """Custom type hh3cMcsPortStaticGroupVlanID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Hh3cMcsPortStaticGroupVlanID_Type.__name__ = "Unsigned32"
_Hh3cMcsPortStaticGroupVlanID_Object = MibTableColumn
hh3cMcsPortStaticGroupVlanID = _Hh3cMcsPortStaticGroupVlanID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 6, 1, 3),
    _Hh3cMcsPortStaticGroupVlanID_Type()
)
hh3cMcsPortStaticGroupVlanID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cMcsPortStaticGroupVlanID.setStatus("current")
_Hh3cMcsPortStaticGroupGroupAddress_Type = InetAddress
_Hh3cMcsPortStaticGroupGroupAddress_Object = MibTableColumn
hh3cMcsPortStaticGroupGroupAddress = _Hh3cMcsPortStaticGroupGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 6, 1, 4),
    _Hh3cMcsPortStaticGroupGroupAddress_Type()
)
hh3cMcsPortStaticGroupGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cMcsPortStaticGroupGroupAddress.setStatus("current")
_Hh3cMcsPortStaticGroupSourceAddress_Type = InetAddress
_Hh3cMcsPortStaticGroupSourceAddress_Object = MibTableColumn
hh3cMcsPortStaticGroupSourceAddress = _Hh3cMcsPortStaticGroupSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 6, 1, 5),
    _Hh3cMcsPortStaticGroupSourceAddress_Type()
)
hh3cMcsPortStaticGroupSourceAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cMcsPortStaticGroupSourceAddress.setStatus("current")
_Hh3cMcsPortStaticGroupStatus_Type = RowStatus
_Hh3cMcsPortStaticGroupStatus_Object = MibTableColumn
hh3cMcsPortStaticGroupStatus = _Hh3cMcsPortStaticGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 6, 1, 6),
    _Hh3cMcsPortStaticGroupStatus_Type()
)
hh3cMcsPortStaticGroupStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMcsPortStaticGroupStatus.setStatus("current")
_Hh3cMcsRouterPortConfigTable_Object = MibTable
hh3cMcsRouterPortConfigTable = _Hh3cMcsRouterPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 7)
)
if mibBuilder.loadTexts:
    hh3cMcsRouterPortConfigTable.setStatus("current")
_Hh3cMcsRouterPortConfigEntry_Object = MibTableRow
hh3cMcsRouterPortConfigEntry = _Hh3cMcsRouterPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 7, 1)
)
hh3cMcsRouterPortConfigEntry.setIndexNames(
    (0, "HH3C-MULTICAST-SNOOPING-MIB", "hh3cMcsRouterPortConfigIfIndex"),
    (0, "HH3C-MULTICAST-SNOOPING-MIB", "hh3cMcsRouterPortConfigSnoopingType"),
    (0, "HH3C-MULTICAST-SNOOPING-MIB", "hh3cMcsRouterPortConfigVlanID"),
)
if mibBuilder.loadTexts:
    hh3cMcsRouterPortConfigEntry.setStatus("current")
_Hh3cMcsRouterPortConfigIfIndex_Type = InterfaceIndex
_Hh3cMcsRouterPortConfigIfIndex_Object = MibTableColumn
hh3cMcsRouterPortConfigIfIndex = _Hh3cMcsRouterPortConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 7, 1, 1),
    _Hh3cMcsRouterPortConfigIfIndex_Type()
)
hh3cMcsRouterPortConfigIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cMcsRouterPortConfigIfIndex.setStatus("current")
_Hh3cMcsRouterPortConfigSnoopingType_Type = InetAddressType
_Hh3cMcsRouterPortConfigSnoopingType_Object = MibTableColumn
hh3cMcsRouterPortConfigSnoopingType = _Hh3cMcsRouterPortConfigSnoopingType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 7, 1, 2),
    _Hh3cMcsRouterPortConfigSnoopingType_Type()
)
hh3cMcsRouterPortConfigSnoopingType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cMcsRouterPortConfigSnoopingType.setStatus("current")


class _Hh3cMcsRouterPortConfigVlanID_Type(Unsigned32):
    """Custom type hh3cMcsRouterPortConfigVlanID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Hh3cMcsRouterPortConfigVlanID_Type.__name__ = "Unsigned32"
_Hh3cMcsRouterPortConfigVlanID_Object = MibTableColumn
hh3cMcsRouterPortConfigVlanID = _Hh3cMcsRouterPortConfigVlanID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 7, 1, 3),
    _Hh3cMcsRouterPortConfigVlanID_Type()
)
hh3cMcsRouterPortConfigVlanID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cMcsRouterPortConfigVlanID.setStatus("current")
_Hh3cMcsRouterPortConfigRowStatus_Type = RowStatus
_Hh3cMcsRouterPortConfigRowStatus_Object = MibTableColumn
hh3cMcsRouterPortConfigRowStatus = _Hh3cMcsRouterPortConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 7, 1, 4),
    _Hh3cMcsRouterPortConfigRowStatus_Type()
)
hh3cMcsRouterPortConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMcsRouterPortConfigRowStatus.setStatus("current")
_Hh3cMcsPortConfigTable_Object = MibTable
hh3cMcsPortConfigTable = _Hh3cMcsPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 8)
)
if mibBuilder.loadTexts:
    hh3cMcsPortConfigTable.setStatus("current")
_Hh3cMcsPortConfigEntry_Object = MibTableRow
hh3cMcsPortConfigEntry = _Hh3cMcsPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 8, 1)
)
hh3cMcsPortConfigEntry.setIndexNames(
    (0, "HH3C-MULTICAST-SNOOPING-MIB", "hh3cMcsPortConfigIfIndex"),
    (0, "HH3C-MULTICAST-SNOOPING-MIB", "hh3cMcsPortConfigSnoopingType"),
    (0, "HH3C-MULTICAST-SNOOPING-MIB", "hh3cMcsPortConfigVlanID"),
)
if mibBuilder.loadTexts:
    hh3cMcsPortConfigEntry.setStatus("current")
_Hh3cMcsPortConfigIfIndex_Type = InterfaceIndex
_Hh3cMcsPortConfigIfIndex_Object = MibTableColumn
hh3cMcsPortConfigIfIndex = _Hh3cMcsPortConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 8, 1, 1),
    _Hh3cMcsPortConfigIfIndex_Type()
)
hh3cMcsPortConfigIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cMcsPortConfigIfIndex.setStatus("current")
_Hh3cMcsPortConfigSnoopingType_Type = InetAddressType
_Hh3cMcsPortConfigSnoopingType_Object = MibTableColumn
hh3cMcsPortConfigSnoopingType = _Hh3cMcsPortConfigSnoopingType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 8, 1, 2),
    _Hh3cMcsPortConfigSnoopingType_Type()
)
hh3cMcsPortConfigSnoopingType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cMcsPortConfigSnoopingType.setStatus("current")


class _Hh3cMcsPortConfigVlanID_Type(Unsigned32):
    """Custom type hh3cMcsPortConfigVlanID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Hh3cMcsPortConfigVlanID_Type.__name__ = "Unsigned32"
_Hh3cMcsPortConfigVlanID_Object = MibTableColumn
hh3cMcsPortConfigVlanID = _Hh3cMcsPortConfigVlanID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 8, 1, 3),
    _Hh3cMcsPortConfigVlanID_Type()
)
hh3cMcsPortConfigVlanID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cMcsPortConfigVlanID.setStatus("current")
_Hh3cMcsPortConfigGroupLimitNumber_Type = Unsigned32
_Hh3cMcsPortConfigGroupLimitNumber_Object = MibTableColumn
hh3cMcsPortConfigGroupLimitNumber = _Hh3cMcsPortConfigGroupLimitNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 8, 1, 4),
    _Hh3cMcsPortConfigGroupLimitNumber_Type()
)
hh3cMcsPortConfigGroupLimitNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMcsPortConfigGroupLimitNumber.setStatus("current")


class _Hh3cMcsPortConfigFastLeaveStatus_Type(TruthValue):
    """Custom type hh3cMcsPortConfigFastLeaveStatus based on TruthValue"""


_Hh3cMcsPortConfigFastLeaveStatus_Object = MibTableColumn
hh3cMcsPortConfigFastLeaveStatus = _Hh3cMcsPortConfigFastLeaveStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 8, 1, 5),
    _Hh3cMcsPortConfigFastLeaveStatus_Type()
)
hh3cMcsPortConfigFastLeaveStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMcsPortConfigFastLeaveStatus.setStatus("current")


class _Hh3cMcsPortConfigGroupPolicyParameter_Type(Unsigned32):
    """Custom type hh3cMcsPortConfigGroupPolicyParameter based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2000, 3999),
    )


_Hh3cMcsPortConfigGroupPolicyParameter_Type.__name__ = "Unsigned32"
_Hh3cMcsPortConfigGroupPolicyParameter_Object = MibTableColumn
hh3cMcsPortConfigGroupPolicyParameter = _Hh3cMcsPortConfigGroupPolicyParameter_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 8, 1, 6),
    _Hh3cMcsPortConfigGroupPolicyParameter_Type()
)
hh3cMcsPortConfigGroupPolicyParameter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMcsPortConfigGroupPolicyParameter.setStatus("current")


class _Hh3cMcsPortConfigOverflowReplace_Type(TruthValue):
    """Custom type hh3cMcsPortConfigOverflowReplace based on TruthValue"""


_Hh3cMcsPortConfigOverflowReplace_Object = MibTableColumn
hh3cMcsPortConfigOverflowReplace = _Hh3cMcsPortConfigOverflowReplace_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 8, 1, 7),
    _Hh3cMcsPortConfigOverflowReplace_Type()
)
hh3cMcsPortConfigOverflowReplace.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMcsPortConfigOverflowReplace.setStatus("current")
_Hh3cMcsPortConfigRowStatus_Type = RowStatus
_Hh3cMcsPortConfigRowStatus_Object = MibTableColumn
hh3cMcsPortConfigRowStatus = _Hh3cMcsPortConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 123, 1, 8, 1, 8),
    _Hh3cMcsPortConfigRowStatus_Type()
)
hh3cMcsPortConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMcsPortConfigRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-MULTICAST-SNOOPING-MIB",
    **{"Hh3cVirtualUnitType": Hh3cVirtualUnitType,
       "hh3cMulticastSnoop": hh3cMulticastSnoop,
       "hh3cMulticastSnoopObject": hh3cMulticastSnoopObject,
       "hh3cMcsGlobalConfigTable": hh3cMcsGlobalConfigTable,
       "hh3cMcsGlobalConfigEntry": hh3cMcsGlobalConfigEntry,
       "hh3cMcsGlbSnoopingType": hh3cMcsGlbSnoopingType,
       "hh3cMcsGlbRowStatus": hh3cMcsGlbRowStatus,
       "hh3cMcsGlbEntryLimit": hh3cMcsGlbEntryLimit,
       "hh3cMcsGlbHostAgingTime": hh3cMcsGlbHostAgingTime,
       "hh3cMcsGlbMaxResponseTime": hh3cMcsGlbMaxResponseTime,
       "hh3cMcsGlbRouterAgingTime": hh3cMcsGlbRouterAgingTime,
       "hh3cMcsGlbLastMemQryInterval": hh3cMcsGlbLastMemQryInterval,
       "hh3cMcsGlbDropUnknownEnabled": hh3cMcsGlbDropUnknownEnabled,
       "hh3cMcsVirtualUnitConfigTable": hh3cMcsVirtualUnitConfigTable,
       "hh3cMcsVirtualUnitConfigEntry": hh3cMcsVirtualUnitConfigEntry,
       "hh3cMcsVUType": hh3cMcsVUType,
       "hh3cMcsVUID": hh3cMcsVUID,
       "hh3cMcsVUSnoopingType": hh3cMcsVUSnoopingType,
       "hh3cMcsVURowStatus": hh3cMcsVURowStatus,
       "hh3cMcsVUHostAgingTime": hh3cMcsVUHostAgingTime,
       "hh3cMcsVUMaxResponseTime": hh3cMcsVUMaxResponseTime,
       "hh3cMcsVURouterAgingTime": hh3cMcsVURouterAgingTime,
       "hh3cMcsVULastMemQryInterval": hh3cMcsVULastMemQryInterval,
       "hh3cMcsVUDropUnknownEnabled": hh3cMcsVUDropUnknownEnabled,
       "hh3cMcsVUPimSnoopingEnabled": hh3cMcsVUPimSnoopingEnabled,
       "hh3cMcsVUVersion": hh3cMcsVUVersion,
       "hh3cMcsVUQuerierEnabled": hh3cMcsVUQuerierEnabled,
       "hh3cMcsVUQuerierInterval": hh3cMcsVUQuerierInterval,
       "hh3cMcsVUGeneQuerierSourceAddress": hh3cMcsVUGeneQuerierSourceAddress,
       "hh3cMcsVUSpecQuerierSourceAddress": hh3cMcsVUSpecQuerierSourceAddress,
       "hh3cMcsVULeaveSourceAddress": hh3cMcsVULeaveSourceAddress,
       "hh3cMcsVUReportSourceAddress": hh3cMcsVUReportSourceAddress,
       "hh3cMcsL2EntryTable": hh3cMcsL2EntryTable,
       "hh3cMcsL2EntryEntry": hh3cMcsL2EntryEntry,
       "hh3cMcsL2EntryVUType": hh3cMcsL2EntryVUType,
       "hh3cMcsL2EntryVUID": hh3cMcsL2EntryVUID,
       "hh3cMcsL2EntryAddressType": hh3cMcsL2EntryAddressType,
       "hh3cMcsL2EntryGroupAddress": hh3cMcsL2EntryGroupAddress,
       "hh3cMcsL2EntrySourceAddress": hh3cMcsL2EntrySourceAddress,
       "hh3cMcsL2EntryIfIndex": hh3cMcsL2EntryIfIndex,
       "hh3cMcsL2EntryPortType": hh3cMcsL2EntryPortType,
       "hh3cMcsL2EntryPortAttribute": hh3cMcsL2EntryPortAttribute,
       "hh3cMcsPacketStatisticsTable": hh3cMcsPacketStatisticsTable,
       "hh3cMcsPacketStatisticsEntry": hh3cMcsPacketStatisticsEntry,
       "hh3cMcsStatisticsSnoopingType": hh3cMcsStatisticsSnoopingType,
       "hh3cMcsRxGeneryQueryNum": hh3cMcsRxGeneryQueryNum,
       "hh3cMcsRxV2SpecificQueryNum": hh3cMcsRxV2SpecificQueryNum,
       "hh3cMcsRxV3SpecificQueryNum": hh3cMcsRxV3SpecificQueryNum,
       "hh3cMcsRxV3SpecificSGQueryNum": hh3cMcsRxV3SpecificSGQueryNum,
       "hh3cMcsRxV1ReportNum": hh3cMcsRxV1ReportNum,
       "hh3cMcsRxV2ReportNum": hh3cMcsRxV2ReportNum,
       "hh3cMcsRxV3ReportNum": hh3cMcsRxV3ReportNum,
       "hh3cMcsRxV3ErrCorReportNum": hh3cMcsRxV3ErrCorReportNum,
       "hh3cMcsRxLeaveNum": hh3cMcsRxLeaveNum,
       "hh3cMcsRxPimHelloNum": hh3cMcsRxPimHelloNum,
       "hh3cMcsRxErrorPacketNum": hh3cMcsRxErrorPacketNum,
       "hh3cMcsTxV2SpecificQueryNum": hh3cMcsTxV2SpecificQueryNum,
       "hh3cMcsTxV3SpecificQueryNum": hh3cMcsTxV3SpecificQueryNum,
       "hh3cMcsTxV3SpecificSGQueryNum": hh3cMcsTxV3SpecificSGQueryNum,
       "hh3cMcsPortJoinGroupConfigTable": hh3cMcsPortJoinGroupConfigTable,
       "hh3cMcsPortJoinGroupConfigEntry": hh3cMcsPortJoinGroupConfigEntry,
       "hh3cMcsPortJoinGroupIfIndex": hh3cMcsPortJoinGroupIfIndex,
       "hh3cMcsPortJoinGroupSnoopingType": hh3cMcsPortJoinGroupSnoopingType,
       "hh3cMcsPortJoinGroupVlanID": hh3cMcsPortJoinGroupVlanID,
       "hh3cMcsPortJoinGroupGroupAddress": hh3cMcsPortJoinGroupGroupAddress,
       "hh3cMcsPortJoinGroupSourceAddress": hh3cMcsPortJoinGroupSourceAddress,
       "hh3cMcsPortJoinGroupStatus": hh3cMcsPortJoinGroupStatus,
       "hh3cMcsPortStaticGroupConfigTable": hh3cMcsPortStaticGroupConfigTable,
       "hh3cMcsPortStaticGroupConfigEntry": hh3cMcsPortStaticGroupConfigEntry,
       "hh3cMcsPortStaticGroupIfIndex": hh3cMcsPortStaticGroupIfIndex,
       "hh3cMcsPortStaticGroupSnoopingType": hh3cMcsPortStaticGroupSnoopingType,
       "hh3cMcsPortStaticGroupVlanID": hh3cMcsPortStaticGroupVlanID,
       "hh3cMcsPortStaticGroupGroupAddress": hh3cMcsPortStaticGroupGroupAddress,
       "hh3cMcsPortStaticGroupSourceAddress": hh3cMcsPortStaticGroupSourceAddress,
       "hh3cMcsPortStaticGroupStatus": hh3cMcsPortStaticGroupStatus,
       "hh3cMcsRouterPortConfigTable": hh3cMcsRouterPortConfigTable,
       "hh3cMcsRouterPortConfigEntry": hh3cMcsRouterPortConfigEntry,
       "hh3cMcsRouterPortConfigIfIndex": hh3cMcsRouterPortConfigIfIndex,
       "hh3cMcsRouterPortConfigSnoopingType": hh3cMcsRouterPortConfigSnoopingType,
       "hh3cMcsRouterPortConfigVlanID": hh3cMcsRouterPortConfigVlanID,
       "hh3cMcsRouterPortConfigRowStatus": hh3cMcsRouterPortConfigRowStatus,
       "hh3cMcsPortConfigTable": hh3cMcsPortConfigTable,
       "hh3cMcsPortConfigEntry": hh3cMcsPortConfigEntry,
       "hh3cMcsPortConfigIfIndex": hh3cMcsPortConfigIfIndex,
       "hh3cMcsPortConfigSnoopingType": hh3cMcsPortConfigSnoopingType,
       "hh3cMcsPortConfigVlanID": hh3cMcsPortConfigVlanID,
       "hh3cMcsPortConfigGroupLimitNumber": hh3cMcsPortConfigGroupLimitNumber,
       "hh3cMcsPortConfigFastLeaveStatus": hh3cMcsPortConfigFastLeaveStatus,
       "hh3cMcsPortConfigGroupPolicyParameter": hh3cMcsPortConfigGroupPolicyParameter,
       "hh3cMcsPortConfigOverflowReplace": hh3cMcsPortConfigOverflowReplace,
       "hh3cMcsPortConfigRowStatus": hh3cMcsPortConfigRowStatus}
)
