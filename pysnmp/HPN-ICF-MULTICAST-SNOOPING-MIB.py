# SNMP MIB module (HPN-ICF-MULTICAST-SNOOPING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-MULTICAST-SNOOPING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:01:16 2024
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

hpnicfMulticastSnoop = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 123)
)
hpnicfMulticastSnoop.setRevisions(
        ("2014-05-14 17:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class HpnicfVirtualUnitType(Integer32, TextualConvention):
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

_HpnicfMulticastSnoopObject_ObjectIdentity = ObjectIdentity
hpnicfMulticastSnoopObject = _HpnicfMulticastSnoopObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 123, 1)
)
_HpnicfMcsGlobalConfigTable_Object = MibTable
hpnicfMcsGlobalConfigTable = _HpnicfMcsGlobalConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 123, 1, 1)
)
if mibBuilder.loadTexts:
    hpnicfMcsGlobalConfigTable.setStatus("current")
_HpnicfMcsGlobalConfigEntry_Object = MibTableRow
hpnicfMcsGlobalConfigEntry = _HpnicfMcsGlobalConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 123, 1, 1, 1)
)
hpnicfMcsGlobalConfigEntry.setIndexNames(
    (0, "HPN-ICF-MULTICAST-SNOOPING-MIB", "hpnicfMcsGlbSnoopingType"),
)
if mibBuilder.loadTexts:
    hpnicfMcsGlobalConfigEntry.setStatus("current")
_HpnicfMcsGlbSnoopingType_Type = InetAddressType
_HpnicfMcsGlbSnoopingType_Object = MibTableColumn
hpnicfMcsGlbSnoopingType = _HpnicfMcsGlbSnoopingType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 123, 1, 1, 1, 1),
    _HpnicfMcsGlbSnoopingType_Type()
)
hpnicfMcsGlbSnoopingType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfMcsGlbSnoopingType.setStatus("current")
_HpnicfMcsGlbRowStatus_Type = RowStatus
_HpnicfMcsGlbRowStatus_Object = MibTableColumn
hpnicfMcsGlbRowStatus = _HpnicfMcsGlbRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 123, 1, 1, 1, 2),
    _HpnicfMcsGlbRowStatus_Type()
)
hpnicfMcsGlbRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMcsGlbRowStatus.setStatus("current")
_HpnicfMcsGlbEntryLimit_Type = Unsigned32
_HpnicfMcsGlbEntryLimit_Object = MibTableColumn
hpnicfMcsGlbEntryLimit = _HpnicfMcsGlbEntryLimit_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 123, 1, 1, 1, 3),
    _HpnicfMcsGlbEntryLimit_Type()
)
hpnicfMcsGlbEntryLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMcsGlbEntryLimit.setStatus("current")


class _HpnicfMcsGlbHostAgingTime_Type(Unsigned32):
    """Custom type hpnicfMcsGlbHostAgingTime based on Unsigned32"""
    defaultValue = 260

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8097894),
    )


_HpnicfMcsGlbHostAgingTime_Type.__name__ = "Unsigned32"
_HpnicfMcsGlbHostAgingTime_Object = MibTableColumn
hpnicfMcsGlbHostAgingTime = _HpnicfMcsGlbHostAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 123, 1, 1, 1, 4),
    _HpnicfMcsGlbHostAgingTime_Type()
)
hpnicfMcsGlbHostAgingTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMcsGlbHostAgingTime.setStatus("current")


class _HpnicfMcsGlbMaxResponseTime_Type(Unsigned32):
    """Custom type hpnicfMcsGlbMaxResponseTime based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3174),
    )


_HpnicfMcsGlbMaxResponseTime_Type.__name__ = "Unsigned32"
_HpnicfMcsGlbMaxResponseTime_Object = MibTableColumn
hpnicfMcsGlbMaxResponseTime = _HpnicfMcsGlbMaxResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 123, 1, 1, 1, 5),
    _HpnicfMcsGlbMaxResponseTime_Type()
)
hpnicfMcsGlbMaxResponseTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMcsGlbMaxResponseTime.setStatus("current")


class _HpnicfMcsGlbRouterAgingTime_Type(Unsigned32):
    """Custom type hpnicfMcsGlbRouterAgingTime based on Unsigned32"""
    defaultValue = 260

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8097894),
    )


_HpnicfMcsGlbRouterAgingTime_Type.__name__ = "Unsigned32"
_HpnicfMcsGlbRouterAgingTime_Object = MibTableColumn
hpnicfMcsGlbRouterAgingTime = _HpnicfMcsGlbRouterAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 123, 1, 1, 1, 6),
    _HpnicfMcsGlbRouterAgingTime_Type()
)
hpnicfMcsGlbRouterAgingTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMcsGlbRouterAgingTime.setStatus("current")


class _HpnicfMcsGlbLastMemQryInterval_Type(Unsigned32):
    """Custom type hpnicfMcsGlbLastMemQryInterval based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 25),
    )


_HpnicfMcsGlbLastMemQryInterval_Type.__name__ = "Unsigned32"
_HpnicfMcsGlbLastMemQryInterval_Object = MibTableColumn
hpnicfMcsGlbLastMemQryInterval = _HpnicfMcsGlbLastMemQryInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 123, 1, 1, 1, 7),
    _HpnicfMcsGlbLastMemQryInterval_Type()
)
hpnicfMcsGlbLastMemQryInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMcsGlbLastMemQryInterval.setStatus("current")


class _HpnicfMcsGlbDropUnknownEnabled_Type(TruthValue):
    """Custom type hpnicfMcsGlbDropUnknownEnabled based on TruthValue"""


_HpnicfMcsGlbDropUnknownEnabled_Object = MibTableColumn
hpnicfMcsGlbDropUnknownEnabled = _HpnicfMcsGlbDropUnknownEnabled_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 123, 1, 1, 1, 8),
    _HpnicfMcsGlbDropUnknownEnabled_Type()
)
hpnicfMcsGlbDropUnknownEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMcsGlbDropUnknownEnabled.setStatus("current")
_HpnicfMcsVirtualUnitConfigTable_Object = MibTable
hpnicfMcsVirtualUnitConfigTable = _HpnicfMcsVirtualUnitConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 123, 1, 2)
)
if mibBuilder.loadTexts:
    hpnicfMcsVirtualUnitConfigTable.setStatus("current")
_HpnicfMcsVirtualUnitConfigEntry_Object = MibTableRow
hpnicfMcsVirtualUnitConfigEntry = _HpnicfMcsVirtualUnitConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 123, 1, 2, 1)
)
hpnicfMcsVirtualUnitConfigEntry.setIndexNames(
    (0, "HPN-ICF-MULTICAST-SNOOPING-MIB", "hpnicfMcsVUType"),
    (0, "HPN-ICF-MULTICAST-SNOOPING-MIB", "hpnicfMcsVUID"),
    (0, "HPN-ICF-MULTICAST-SNOOPING-MIB", "hpnicfMcsVUSnoopingType"),
)
if mibBuilder.loadTexts:
    hpnicfMcsVirtualUnitConfigEntry.setStatus("current")
_HpnicfMcsVUType_Type = HpnicfVirtualUnitType
_HpnicfMcsVUType_Object = MibTableColumn
hpnicfMcsVUType = _HpnicfMcsVUType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 123, 1, 2, 1, 1),
    _HpnicfMcsVUType_Type()
)
hpnicfMcsVUType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfMcsVUType.setStatus("current")
_HpnicfMcsVUID_Type = Unsigned32
_HpnicfMcsVUID_Object = MibTableColumn
hpnicfMcsVUID = _HpnicfMcsVUID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 123, 1, 2, 1, 2),
    _HpnicfMcsVUID_Type()
)
hpnicfMcsVUID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfMcsVUID.setStatus("current")
_HpnicfMcsVUSnoopingType_Type = InetAddressType
_HpnicfMcsVUSnoopingType_Object = MibTableColumn
hpnicfMcsVUSnoopingType = _HpnicfMcsVUSnoopingType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 123, 1, 2, 1, 3),
    _HpnicfMcsVUSnoopingType_Type()
)
hpnicfMcsVUSnoopingType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfMcsVUSnoopingType.setStatus("current")
_HpnicfMcsVURowStatus_Type = RowStatus
_HpnicfMcsVURowStatus_Object = MibTableColumn
hpnicfMcsVURowStatus = _HpnicfMcsVURowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 123, 1, 2, 1, 4),
    _HpnicfMcsVURowStatus_Type()
)
hpnicfMcsVURowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMcsVURowStatus.setStatus("current")


class _HpnicfMcsVUHostAgingTime_Type(Unsigned32):
    """Custom type hpnicfMcsVUHostAgingTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8097894),
    )


_HpnicfMcsVUHostAgingTime_Type.__name__ = "Unsigned32"
_HpnicfMcsVUHostAgingTime_Object = MibTableColumn
hpnicfMcsVUHostAgingTime = _HpnicfMcsVUHostAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 123, 1, 2, 1, 5),
    _HpnicfMcsVUHostAgingTime_Type()
)
hpnicfMcsVUHostAgingTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMcsVUHostAgingTime.setStatus("current")


class _HpnicfMcsVUMaxResponseTime_Type(Unsigned32):
    """Custom type hpnicfMcsVUMaxResponseTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3174),
    )


_HpnicfMcsVUMaxResponseTime_Type.__name__ = "Unsigned32"
_HpnicfMcsVUMaxResponseTime_Object = MibTableColumn
hpnicfMcsVUMaxResponseTime = _HpnicfMcsVUMaxResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 123, 1, 2, 1, 6),
    _HpnicfMcsVUMaxResponseTime_Type()
)
hpnicfMcsVUMaxResponseTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMcsVUMaxResponseTime.setStatus("current")


class _HpnicfMcsVURouterAgingTime_Type(Unsigned32):
    """Custom type hpnicfMcsVURouterAgingTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8097894),
    )


_HpnicfMcsVURouterAgingTime_Type.__name__ = "Unsigned32"
_HpnicfMcsVURouterAgingTime_Object = MibTableColumn
hpnicfMcsVURouterAgingTime = _HpnicfMcsVURouterAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 123, 1, 2, 1, 7),
    _HpnicfMcsVURouterAgingTime_Type()
)
hpnicfMcsVURouterAgingTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMcsVURouterAgingTime.setStatus("current")


class _HpnicfMcsVULastMemQryInterval_Type(Unsigned32):
    """Custom type hpnicfMcsVULastMemQryInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 25),
    )


_HpnicfMcsVULastMemQryInterval_Type.__name__ = "Unsigned32"
_HpnicfMcsVULastMemQryInterval_Object = MibTableColumn
hpnicfMcsVULastMemQryInterval = _HpnicfMcsVULastMemQryInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 123, 1, 2, 1, 8),
    _HpnicfMcsVULastMemQryInterval_Type()
)
hpnicfMcsVULastMemQryInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMcsVULastMemQryInterval.setStatus("current")


class _HpnicfMcsVUDropUnknownEnabled_Type(TruthValue):
    """Custom type hpnicfMcsVUDropUnknownEnabled based on TruthValue"""


_HpnicfMcsVUDropUnknownEnabled_Object = MibTableColumn
hpnicfMcsVUDropUnknownEnabled = _HpnicfMcsVUDropUnknownEnabled_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 123, 1, 2, 1, 9),
    _HpnicfMcsVUDropUnknownEnabled_Type()
)
hpnicfMcsVUDropUnknownEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMcsVUDropUnknownEnabled.setStatus("current")


class _HpnicfMcsVUPimSnoopingEnabled_Type(TruthValue):
    """Custom type hpnicfMcsVUPimSnoopingEnabled based on TruthValue"""


_HpnicfMcsVUPimSnoopingEnabled_Object = MibTableColumn
hpnicfMcsVUPimSnoopingEnabled = _HpnicfMcsVUPimSnoopingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 123, 1, 2, 1, 10),
    _HpnicfMcsVUPimSnoopingEnabled_Type()
)
hpnicfMcsVUPimSnoopingEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMcsVUPimSnoopingEnabled.setStatus("current")


class _HpnicfMcsVUVersion_Type(Unsigned32):
    """Custom type hpnicfMcsVUVersion based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(3, 3),
    )


_HpnicfMcsVUVersion_Type.__name__ = "Unsigned32"
_HpnicfMcsVUVersion_Object = MibTableColumn
hpnicfMcsVUVersion = _HpnicfMcsVUVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 123, 1, 2, 1, 11),
    _HpnicfMcsVUVersion_Type()
)
hpnicfMcsVUVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMcsVUVersion.setStatus("current")


class _HpnicfMcsVUQuerierEnabled_Type(TruthValue):
    """Custom type hpnicfMcsVUQuerierEnabled based on TruthValue"""


_HpnicfMcsVUQuerierEnabled_Object = MibTableColumn
hpnicfMcsVUQuerierEnabled = _HpnicfMcsVUQuerierEnabled_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 123, 1, 2, 1, 12),
    _HpnicfMcsVUQuerierEnabled_Type()
)
hpnicfMcsVUQuerierEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMcsVUQuerierEnabled.setStatus("current")


class _HpnicfMcsVUQuerierInterval_Type(Unsigned32):
    """Custom type hpnicfMcsVUQuerierInterval based on Unsigned32"""
    defaultValue = 125

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 31744),
    )


_HpnicfMcsVUQuerierInterval_Type.__name__ = "Unsigned32"
_HpnicfMcsVUQuerierInterval_Object = MibTableColumn
hpnicfMcsVUQuerierInterval = _HpnicfMcsVUQuerierInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 123, 1, 2, 1, 13),
    _HpnicfMcsVUQuerierInterval_Type()
)
hpnicfMcsVUQuerierInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMcsVUQuerierInterval.setStatus("current")
_HpnicfMcsVUGeneQuerierSourceAddress_Type = InetAddress
_HpnicfMcsVUGeneQuerierSourceAddress_Object = MibTableColumn
hpnicfMcsVUGeneQuerierSourceAddress = _HpnicfMcsVUGeneQuerierSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 123, 1, 2, 1, 14),
    _HpnicfMcsVUGeneQuerierSourceAddress_Type()
)
hpnicfMcsVUGeneQuerierSourceAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMcsVUGeneQuerierSourceAddress.setStatus("current")
_HpnicfMcsVUSpecQuerierSourceAddress_Type = InetAddress
_HpnicfMcsVUSpecQuerierSourceAddress_Object = MibTableColumn
hpnicfMcsVUSpecQuerierSourceAddress = _HpnicfMcsVUSpecQuerierSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 123, 1, 2, 1, 15),
    _HpnicfMcsVUSpecQuerierSourceAddress_Type()
)
hpnicfMcsVUSpecQuerierSourceAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMcsVUSpecQuerierSourceAddress.setStatus("current")
_HpnicfMcsVULeaveSourceAddress_Type = InetAddress
_HpnicfMcsVULeaveSourceAddress_Object = MibTableColumn
hpnicfMcsVULeaveSourceAddress = _HpnicfMcsVULeaveSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 123, 1, 2, 1, 16),
    _HpnicfMcsVULeaveSourceAddress_Type()
)
hpnicfMcsVULeaveSourceAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMcsVULeaveSourceAddress.setStatus("current")
_HpnicfMcsVUReportSourceAddress_Type = InetAddress
_HpnicfMcsVUReportSourceAddress_Object = MibTableColumn
hpnicfMcsVUReportSourceAddress = _HpnicfMcsVUReportSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 123, 1, 2, 1, 17),
    _HpnicfMcsVUReportSourceAddress_Type()
)
hpnicfMcsVUReportSourceAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMcsVUReportSourceAddress.setStatus("current")
_HpnicfMcsL2EntryTable_Object = MibTable
hpnicfMcsL2EntryTable = _HpnicfMcsL2EntryTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 123, 1, 3)
)
if mibBuilder.loadTexts:
    hpnicfMcsL2EntryTable.setStatus("current")
_HpnicfMcsL2EntryEntry_Object = MibTableRow
hpnicfMcsL2EntryEntry = _HpnicfMcsL2EntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 123, 1, 3, 1)
)
hpnicfMcsL2EntryEntry.setIndexNames(
    (0, "HPN-ICF-MULTICAST-SNOOPING-MIB", "hpnicfMcsL2EntryVUType"),
    (0, "HPN-ICF-MULTICAST-SNOOPING-MIB", "hpnicfMcsL2EntryVUID"),
    (0, "HPN-ICF-MULTICAST-SNOOPING-MIB", "hpnicfMcsL2EntryAddressType"),
    (0, "HPN-ICF-MULTICAST-SNOOPING-MIB", "hpnicfMcsL2EntryGroupAddress"),
    (0, "HPN-ICF-MULTICAST-SNOOPING-MIB", "hpnicfMcsL2EntrySourceAddress"),
    (0, "HPN-ICF-MULTICAST-SNOOPING-MIB", "hpnicfMcsL2EntryIfIndex"),
)
if mibBuilder.loadTexts:
    hpnicfMcsL2EntryEntry.setStatus("current")
_HpnicfMcsL2EntryVUType_Type = HpnicfVirtualUnitType
_HpnicfMcsL2EntryVUType_Object = MibTableColumn
hpnicfMcsL2EntryVUType = _HpnicfMcsL2EntryVUType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 123, 1, 3, 1, 1),
    _HpnicfMcsL2EntryVUType_Type()
)
hpnicfMcsL2EntryVUType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfMcsL2EntryVUType.setStatus("current")
_HpnicfMcsL2EntryVUID_Type = Unsigned32
_HpnicfMcsL2EntryVUID_Object = MibTableColumn
hpnicfMcsL2EntryVUID = _HpnicfMcsL2EntryVUID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 123, 1, 3, 1, 2),
    _HpnicfMcsL2EntryVUID_Type()
)
hpnicfMcsL2EntryVUID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfMcsL2EntryVUID.setStatus("current")
_HpnicfMcsL2EntryAddressType_Type = InetAddressType
_HpnicfMcsL2EntryAddressType_Object = MibTableColumn
hpnicfMcsL2EntryAddressType = _HpnicfMcsL2EntryAddressType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 123, 1, 3, 1, 3),
    _HpnicfMcsL2EntryAddressType_Type()
)
hpnicfMcsL2EntryAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfMcsL2EntryAddressType.setStatus("current")
_HpnicfMcsL2EntryGroupAddress_Type = InetAddress
_HpnicfMcsL2EntryGroupAddress_Object = MibTableColumn
hpnicfMcsL2EntryGroupAddress = _HpnicfMcsL2EntryGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 123, 1, 3, 1, 4),
    _HpnicfMcsL2EntryGroupAddress_Type()
)
hpnicfMcsL2EntryGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfMcsL2EntryGroupAddress.setStatus("current")
_HpnicfMcsL2EntrySourceAddress_Type = InetAddress
_HpnicfMcsL2EntrySourceAddress_Object = MibTableColumn
hpnicfMcsL2EntrySourceAddress = _HpnicfMcsL2EntrySourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 123, 1, 3, 1, 5),
    _HpnicfMcsL2EntrySourceAddress_Type()
)
hpnicfMcsL2EntrySourceAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfMcsL2EntrySourceAddress.setStatus("current")
_HpnicfMcsL2EntryIfIndex_Type = InterfaceIndex
_HpnicfMcsL2EntryIfIndex_Object = MibTableColumn
hpnicfMcsL2EntryIfIndex = _HpnicfMcsL2EntryIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 123, 1, 3, 1, 6),
    _HpnicfMcsL2EntryIfIndex_Type()
)
hpnicfMcsL2EntryIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfMcsL2EntryIfIndex.setStatus("current")


class _HpnicfMcsL2EntryPortType_Type(Integer32):
    """Custom type hpnicfMcsL2EntryPortType based on Integer32"""
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


_HpnicfMcsL2EntryPortType_Type.__name__ = "Integer32"
_HpnicfMcsL2EntryPortType_Object = MibTableColumn
hpnicfMcsL2EntryPortType = _HpnicfMcsL2EntryPortType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 123, 1, 3, 1, 7),
    _HpnicfMcsL2EntryPortType_Type()
)
hpnicfMcsL2EntryPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfMcsL2EntryPortType.setStatus("current")


class _HpnicfMcsL2EntryPortAttribute_Type(Bits):
    """Custom type hpnicfMcsL2EntryPortAttribute based on Bits"""
    namedValues = NamedValues(
        *(("d", 0),
          ("k", 3),
          ("p", 2),
          ("r", 4),
          ("s", 1),
          ("w", 5))
    )

_HpnicfMcsL2EntryPortAttribute_Type.__name__ = "Bits"
_HpnicfMcsL2EntryPortAttribute_Object = MibTableColumn
hpnicfMcsL2EntryPortAttribute = _HpnicfMcsL2EntryPortAttribute_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 123, 1, 3, 1, 8),
    _HpnicfMcsL2EntryPortAttribute_Type()
)
hpnicfMcsL2EntryPortAttribute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfMcsL2EntryPortAttribute.setStatus("current")
_HpnicfMcsPacketStatisticsTable_Object = MibTable
hpnicfMcsPacketStatisticsTable = _HpnicfMcsPacketStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 123, 1, 4)
)
if mibBuilder.loadTexts:
    hpnicfMcsPacketStatisticsTable.setStatus("current")
_HpnicfMcsPacketStatisticsEntry_Object = MibTableRow
hpnicfMcsPacketStatisticsEntry = _HpnicfMcsPacketStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 123, 1, 4, 1)
)
hpnicfMcsPacketStatisticsEntry.setIndexNames(
    (0, "HPN-ICF-MULTICAST-SNOOPING-MIB", "hpnicfMcsStatisticsSnoopingType"),
)
if mibBuilder.loadTexts:
    hpnicfMcsPacketStatisticsEntry.setStatus("current")
_HpnicfMcsStatisticsSnoopingType_Type = InetAddressType
_HpnicfMcsStatisticsSnoopingType_Object = MibTableColumn
hpnicfMcsStatisticsSnoopingType = _HpnicfMcsStatisticsSnoopingType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 123, 1, 4, 1, 1),
    _HpnicfMcsStatisticsSnoopingType_Type()
)
hpnicfMcsStatisticsSnoopingType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfMcsStatisticsSnoopingType.setStatus("current")
_HpnicfMcsRxGeneryQueryNum_Type = Counter64
_HpnicfMcsRxGeneryQueryNum_Object = MibTableColumn
hpnicfMcsRxGeneryQueryNum = _HpnicfMcsRxGeneryQueryNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 123, 1, 4, 1, 2),
    _HpnicfMcsRxGeneryQueryNum_Type()
)
hpnicfMcsRxGeneryQueryNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfMcsRxGeneryQueryNum.setStatus("current")
_HpnicfMcsRxV2SpecificQueryNum_Type = Counter64
_HpnicfMcsRxV2SpecificQueryNum_Object = MibTableColumn
hpnicfMcsRxV2SpecificQueryNum = _HpnicfMcsRxV2SpecificQueryNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 123, 1, 4, 1, 3),
    _HpnicfMcsRxV2SpecificQueryNum_Type()
)
hpnicfMcsRxV2SpecificQueryNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfMcsRxV2SpecificQueryNum.setStatus("current")
_HpnicfMcsRxV3SpecificQueryNum_Type = Counter64
_HpnicfMcsRxV3SpecificQueryNum_Object = MibTableColumn
hpnicfMcsRxV3SpecificQueryNum = _HpnicfMcsRxV3SpecificQueryNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 123, 1, 4, 1, 4),
    _HpnicfMcsRxV3SpecificQueryNum_Type()
)
hpnicfMcsRxV3SpecificQueryNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfMcsRxV3SpecificQueryNum.setStatus("current")
_HpnicfMcsRxV3SpecificSGQueryNum_Type = Counter64
_HpnicfMcsRxV3SpecificSGQueryNum_Object = MibTableColumn
hpnicfMcsRxV3SpecificSGQueryNum = _HpnicfMcsRxV3SpecificSGQueryNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 123, 1, 4, 1, 5),
    _HpnicfMcsRxV3SpecificSGQueryNum_Type()
)
hpnicfMcsRxV3SpecificSGQueryNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfMcsRxV3SpecificSGQueryNum.setStatus("current")
_HpnicfMcsRxV1ReportNum_Type = Counter64
_HpnicfMcsRxV1ReportNum_Object = MibTableColumn
hpnicfMcsRxV1ReportNum = _HpnicfMcsRxV1ReportNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 123, 1, 4, 1, 6),
    _HpnicfMcsRxV1ReportNum_Type()
)
hpnicfMcsRxV1ReportNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfMcsRxV1ReportNum.setStatus("current")
_HpnicfMcsRxV2ReportNum_Type = Counter64
_HpnicfMcsRxV2ReportNum_Object = MibTableColumn
hpnicfMcsRxV2ReportNum = _HpnicfMcsRxV2ReportNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 123, 1, 4, 1, 7),
    _HpnicfMcsRxV2ReportNum_Type()
)
hpnicfMcsRxV2ReportNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfMcsRxV2ReportNum.setStatus("current")
_HpnicfMcsRxV3ReportNum_Type = Counter64
_HpnicfMcsRxV3ReportNum_Object = MibTableColumn
hpnicfMcsRxV3ReportNum = _HpnicfMcsRxV3ReportNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 123, 1, 4, 1, 8),
    _HpnicfMcsRxV3ReportNum_Type()
)
hpnicfMcsRxV3ReportNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfMcsRxV3ReportNum.setStatus("current")
_HpnicfMcsRxV3ErrCorReportNum_Type = Counter64
_HpnicfMcsRxV3ErrCorReportNum_Object = MibTableColumn
hpnicfMcsRxV3ErrCorReportNum = _HpnicfMcsRxV3ErrCorReportNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 123, 1, 4, 1, 9),
    _HpnicfMcsRxV3ErrCorReportNum_Type()
)
hpnicfMcsRxV3ErrCorReportNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfMcsRxV3ErrCorReportNum.setStatus("current")
_HpnicfMcsRxLeaveNum_Type = Counter64
_HpnicfMcsRxLeaveNum_Object = MibTableColumn
hpnicfMcsRxLeaveNum = _HpnicfMcsRxLeaveNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 123, 1, 4, 1, 10),
    _HpnicfMcsRxLeaveNum_Type()
)
hpnicfMcsRxLeaveNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfMcsRxLeaveNum.setStatus("current")
_HpnicfMcsRxPimHelloNum_Type = Counter64
_HpnicfMcsRxPimHelloNum_Object = MibTableColumn
hpnicfMcsRxPimHelloNum = _HpnicfMcsRxPimHelloNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 123, 1, 4, 1, 11),
    _HpnicfMcsRxPimHelloNum_Type()
)
hpnicfMcsRxPimHelloNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfMcsRxPimHelloNum.setStatus("current")
_HpnicfMcsRxErrorPacketNum_Type = Counter64
_HpnicfMcsRxErrorPacketNum_Object = MibTableColumn
hpnicfMcsRxErrorPacketNum = _HpnicfMcsRxErrorPacketNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 123, 1, 4, 1, 12),
    _HpnicfMcsRxErrorPacketNum_Type()
)
hpnicfMcsRxErrorPacketNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfMcsRxErrorPacketNum.setStatus("current")
_HpnicfMcsTxV2SpecificQueryNum_Type = Counter64
_HpnicfMcsTxV2SpecificQueryNum_Object = MibTableColumn
hpnicfMcsTxV2SpecificQueryNum = _HpnicfMcsTxV2SpecificQueryNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 123, 1, 4, 1, 13),
    _HpnicfMcsTxV2SpecificQueryNum_Type()
)
hpnicfMcsTxV2SpecificQueryNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfMcsTxV2SpecificQueryNum.setStatus("current")
_HpnicfMcsTxV3SpecificQueryNum_Type = Counter64
_HpnicfMcsTxV3SpecificQueryNum_Object = MibTableColumn
hpnicfMcsTxV3SpecificQueryNum = _HpnicfMcsTxV3SpecificQueryNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 123, 1, 4, 1, 14),
    _HpnicfMcsTxV3SpecificQueryNum_Type()
)
hpnicfMcsTxV3SpecificQueryNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfMcsTxV3SpecificQueryNum.setStatus("current")
_HpnicfMcsTxV3SpecificSGQueryNum_Type = Counter64
_HpnicfMcsTxV3SpecificSGQueryNum_Object = MibTableColumn
hpnicfMcsTxV3SpecificSGQueryNum = _HpnicfMcsTxV3SpecificSGQueryNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 123, 1, 4, 1, 15),
    _HpnicfMcsTxV3SpecificSGQueryNum_Type()
)
hpnicfMcsTxV3SpecificSGQueryNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfMcsTxV3SpecificSGQueryNum.setStatus("current")
_HpnicfMcsPortJoinGroupConfigTable_Object = MibTable
hpnicfMcsPortJoinGroupConfigTable = _HpnicfMcsPortJoinGroupConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 123, 1, 5)
)
if mibBuilder.loadTexts:
    hpnicfMcsPortJoinGroupConfigTable.setStatus("current")
_HpnicfMcsPortJoinGroupConfigEntry_Object = MibTableRow
hpnicfMcsPortJoinGroupConfigEntry = _HpnicfMcsPortJoinGroupConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 123, 1, 5, 1)
)
hpnicfMcsPortJoinGroupConfigEntry.setIndexNames(
    (0, "HPN-ICF-MULTICAST-SNOOPING-MIB", "hpnicfMcsPortJoinGroupIfIndex"),
    (0, "HPN-ICF-MULTICAST-SNOOPING-MIB", "hpnicfMcsPortJoinGroupSnoopingType"),
    (0, "HPN-ICF-MULTICAST-SNOOPING-MIB", "hpnicfMcsPortJoinGroupVlanID"),
    (0, "HPN-ICF-MULTICAST-SNOOPING-MIB", "hpnicfMcsPortJoinGroupGroupAddress"),
    (0, "HPN-ICF-MULTICAST-SNOOPING-MIB", "hpnicfMcsPortJoinGroupSourceAddress"),
)
if mibBuilder.loadTexts:
    hpnicfMcsPortJoinGroupConfigEntry.setStatus("current")
_HpnicfMcsPortJoinGroupIfIndex_Type = InterfaceIndex
_HpnicfMcsPortJoinGroupIfIndex_Object = MibTableColumn
hpnicfMcsPortJoinGroupIfIndex = _HpnicfMcsPortJoinGroupIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 123, 1, 5, 1, 1),
    _HpnicfMcsPortJoinGroupIfIndex_Type()
)
hpnicfMcsPortJoinGroupIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfMcsPortJoinGroupIfIndex.setStatus("current")
_HpnicfMcsPortJoinGroupSnoopingType_Type = InetAddressType
_HpnicfMcsPortJoinGroupSnoopingType_Object = MibTableColumn
hpnicfMcsPortJoinGroupSnoopingType = _HpnicfMcsPortJoinGroupSnoopingType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 123, 1, 5, 1, 2),
    _HpnicfMcsPortJoinGroupSnoopingType_Type()
)
hpnicfMcsPortJoinGroupSnoopingType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfMcsPortJoinGroupSnoopingType.setStatus("current")


class _HpnicfMcsPortJoinGroupVlanID_Type(Unsigned32):
    """Custom type hpnicfMcsPortJoinGroupVlanID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_HpnicfMcsPortJoinGroupVlanID_Type.__name__ = "Unsigned32"
_HpnicfMcsPortJoinGroupVlanID_Object = MibTableColumn
hpnicfMcsPortJoinGroupVlanID = _HpnicfMcsPortJoinGroupVlanID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 123, 1, 5, 1, 3),
    _HpnicfMcsPortJoinGroupVlanID_Type()
)
hpnicfMcsPortJoinGroupVlanID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfMcsPortJoinGroupVlanID.setStatus("current")
_HpnicfMcsPortJoinGroupGroupAddress_Type = InetAddress
_HpnicfMcsPortJoinGroupGroupAddress_Object = MibTableColumn
hpnicfMcsPortJoinGroupGroupAddress = _HpnicfMcsPortJoinGroupGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 123, 1, 5, 1, 4),
    _HpnicfMcsPortJoinGroupGroupAddress_Type()
)
hpnicfMcsPortJoinGroupGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfMcsPortJoinGroupGroupAddress.setStatus("current")
_HpnicfMcsPortJoinGroupSourceAddress_Type = InetAddress
_HpnicfMcsPortJoinGroupSourceAddress_Object = MibTableColumn
hpnicfMcsPortJoinGroupSourceAddress = _HpnicfMcsPortJoinGroupSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 123, 1, 5, 1, 5),
    _HpnicfMcsPortJoinGroupSourceAddress_Type()
)
hpnicfMcsPortJoinGroupSourceAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfMcsPortJoinGroupSourceAddress.setStatus("current")
_HpnicfMcsPortJoinGroupStatus_Type = RowStatus
_HpnicfMcsPortJoinGroupStatus_Object = MibTableColumn
hpnicfMcsPortJoinGroupStatus = _HpnicfMcsPortJoinGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 123, 1, 5, 1, 6),
    _HpnicfMcsPortJoinGroupStatus_Type()
)
hpnicfMcsPortJoinGroupStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMcsPortJoinGroupStatus.setStatus("current")
_HpnicfMcsPortStaticGroupConfigTable_Object = MibTable
hpnicfMcsPortStaticGroupConfigTable = _HpnicfMcsPortStaticGroupConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 123, 1, 6)
)
if mibBuilder.loadTexts:
    hpnicfMcsPortStaticGroupConfigTable.setStatus("current")
_HpnicfMcsPortStaticGroupConfigEntry_Object = MibTableRow
hpnicfMcsPortStaticGroupConfigEntry = _HpnicfMcsPortStaticGroupConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 123, 1, 6, 1)
)
hpnicfMcsPortStaticGroupConfigEntry.setIndexNames(
    (0, "HPN-ICF-MULTICAST-SNOOPING-MIB", "hpnicfMcsPortStaticGroupIfIndex"),
    (0, "HPN-ICF-MULTICAST-SNOOPING-MIB", "hpnicfMcsPortStaticGroupSnoopingType"),
    (0, "HPN-ICF-MULTICAST-SNOOPING-MIB", "hpnicfMcsPortStaticGroupVlanID"),
    (0, "HPN-ICF-MULTICAST-SNOOPING-MIB", "hpnicfMcsPortStaticGroupGroupAddress"),
    (0, "HPN-ICF-MULTICAST-SNOOPING-MIB", "hpnicfMcsPortStaticGroupSourceAddress"),
)
if mibBuilder.loadTexts:
    hpnicfMcsPortStaticGroupConfigEntry.setStatus("current")
_HpnicfMcsPortStaticGroupIfIndex_Type = InterfaceIndex
_HpnicfMcsPortStaticGroupIfIndex_Object = MibTableColumn
hpnicfMcsPortStaticGroupIfIndex = _HpnicfMcsPortStaticGroupIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 123, 1, 6, 1, 1),
    _HpnicfMcsPortStaticGroupIfIndex_Type()
)
hpnicfMcsPortStaticGroupIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfMcsPortStaticGroupIfIndex.setStatus("current")
_HpnicfMcsPortStaticGroupSnoopingType_Type = InetAddressType
_HpnicfMcsPortStaticGroupSnoopingType_Object = MibTableColumn
hpnicfMcsPortStaticGroupSnoopingType = _HpnicfMcsPortStaticGroupSnoopingType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 123, 1, 6, 1, 2),
    _HpnicfMcsPortStaticGroupSnoopingType_Type()
)
hpnicfMcsPortStaticGroupSnoopingType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfMcsPortStaticGroupSnoopingType.setStatus("current")


class _HpnicfMcsPortStaticGroupVlanID_Type(Unsigned32):
    """Custom type hpnicfMcsPortStaticGroupVlanID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_HpnicfMcsPortStaticGroupVlanID_Type.__name__ = "Unsigned32"
_HpnicfMcsPortStaticGroupVlanID_Object = MibTableColumn
hpnicfMcsPortStaticGroupVlanID = _HpnicfMcsPortStaticGroupVlanID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 123, 1, 6, 1, 3),
    _HpnicfMcsPortStaticGroupVlanID_Type()
)
hpnicfMcsPortStaticGroupVlanID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfMcsPortStaticGroupVlanID.setStatus("current")
_HpnicfMcsPortStaticGroupGroupAddress_Type = InetAddress
_HpnicfMcsPortStaticGroupGroupAddress_Object = MibTableColumn
hpnicfMcsPortStaticGroupGroupAddress = _HpnicfMcsPortStaticGroupGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 123, 1, 6, 1, 4),
    _HpnicfMcsPortStaticGroupGroupAddress_Type()
)
hpnicfMcsPortStaticGroupGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfMcsPortStaticGroupGroupAddress.setStatus("current")
_HpnicfMcsPortStaticGroupSourceAddress_Type = InetAddress
_HpnicfMcsPortStaticGroupSourceAddress_Object = MibTableColumn
hpnicfMcsPortStaticGroupSourceAddress = _HpnicfMcsPortStaticGroupSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 123, 1, 6, 1, 5),
    _HpnicfMcsPortStaticGroupSourceAddress_Type()
)
hpnicfMcsPortStaticGroupSourceAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfMcsPortStaticGroupSourceAddress.setStatus("current")
_HpnicfMcsPortStaticGroupStatus_Type = RowStatus
_HpnicfMcsPortStaticGroupStatus_Object = MibTableColumn
hpnicfMcsPortStaticGroupStatus = _HpnicfMcsPortStaticGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 123, 1, 6, 1, 6),
    _HpnicfMcsPortStaticGroupStatus_Type()
)
hpnicfMcsPortStaticGroupStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMcsPortStaticGroupStatus.setStatus("current")
_HpnicfMcsRouterPortConfigTable_Object = MibTable
hpnicfMcsRouterPortConfigTable = _HpnicfMcsRouterPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 123, 1, 7)
)
if mibBuilder.loadTexts:
    hpnicfMcsRouterPortConfigTable.setStatus("current")
_HpnicfMcsRouterPortConfigEntry_Object = MibTableRow
hpnicfMcsRouterPortConfigEntry = _HpnicfMcsRouterPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 123, 1, 7, 1)
)
hpnicfMcsRouterPortConfigEntry.setIndexNames(
    (0, "HPN-ICF-MULTICAST-SNOOPING-MIB", "hpnicfMcsRouterPortConfigIfIndex"),
    (0, "HPN-ICF-MULTICAST-SNOOPING-MIB", "hpnicfMcsRouterPortConfigSnoopingType"),
    (0, "HPN-ICF-MULTICAST-SNOOPING-MIB", "hpnicfMcsRouterPortConfigVlanID"),
)
if mibBuilder.loadTexts:
    hpnicfMcsRouterPortConfigEntry.setStatus("current")
_HpnicfMcsRouterPortConfigIfIndex_Type = InterfaceIndex
_HpnicfMcsRouterPortConfigIfIndex_Object = MibTableColumn
hpnicfMcsRouterPortConfigIfIndex = _HpnicfMcsRouterPortConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 123, 1, 7, 1, 1),
    _HpnicfMcsRouterPortConfigIfIndex_Type()
)
hpnicfMcsRouterPortConfigIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfMcsRouterPortConfigIfIndex.setStatus("current")
_HpnicfMcsRouterPortConfigSnoopingType_Type = InetAddressType
_HpnicfMcsRouterPortConfigSnoopingType_Object = MibTableColumn
hpnicfMcsRouterPortConfigSnoopingType = _HpnicfMcsRouterPortConfigSnoopingType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 123, 1, 7, 1, 2),
    _HpnicfMcsRouterPortConfigSnoopingType_Type()
)
hpnicfMcsRouterPortConfigSnoopingType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfMcsRouterPortConfigSnoopingType.setStatus("current")


class _HpnicfMcsRouterPortConfigVlanID_Type(Unsigned32):
    """Custom type hpnicfMcsRouterPortConfigVlanID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_HpnicfMcsRouterPortConfigVlanID_Type.__name__ = "Unsigned32"
_HpnicfMcsRouterPortConfigVlanID_Object = MibTableColumn
hpnicfMcsRouterPortConfigVlanID = _HpnicfMcsRouterPortConfigVlanID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 123, 1, 7, 1, 3),
    _HpnicfMcsRouterPortConfigVlanID_Type()
)
hpnicfMcsRouterPortConfigVlanID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfMcsRouterPortConfigVlanID.setStatus("current")
_HpnicfMcsRouterPortConfigRowStatus_Type = RowStatus
_HpnicfMcsRouterPortConfigRowStatus_Object = MibTableColumn
hpnicfMcsRouterPortConfigRowStatus = _HpnicfMcsRouterPortConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 123, 1, 7, 1, 4),
    _HpnicfMcsRouterPortConfigRowStatus_Type()
)
hpnicfMcsRouterPortConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMcsRouterPortConfigRowStatus.setStatus("current")
_HpnicfMcsPortConfigTable_Object = MibTable
hpnicfMcsPortConfigTable = _HpnicfMcsPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 123, 1, 8)
)
if mibBuilder.loadTexts:
    hpnicfMcsPortConfigTable.setStatus("current")
_HpnicfMcsPortConfigEntry_Object = MibTableRow
hpnicfMcsPortConfigEntry = _HpnicfMcsPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 123, 1, 8, 1)
)
hpnicfMcsPortConfigEntry.setIndexNames(
    (0, "HPN-ICF-MULTICAST-SNOOPING-MIB", "hpnicfMcsPortConfigIfIndex"),
    (0, "HPN-ICF-MULTICAST-SNOOPING-MIB", "hpnicfMcsPortConfigSnoopingType"),
    (0, "HPN-ICF-MULTICAST-SNOOPING-MIB", "hpnicfMcsPortConfigVlanID"),
)
if mibBuilder.loadTexts:
    hpnicfMcsPortConfigEntry.setStatus("current")
_HpnicfMcsPortConfigIfIndex_Type = InterfaceIndex
_HpnicfMcsPortConfigIfIndex_Object = MibTableColumn
hpnicfMcsPortConfigIfIndex = _HpnicfMcsPortConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 123, 1, 8, 1, 1),
    _HpnicfMcsPortConfigIfIndex_Type()
)
hpnicfMcsPortConfigIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfMcsPortConfigIfIndex.setStatus("current")
_HpnicfMcsPortConfigSnoopingType_Type = InetAddressType
_HpnicfMcsPortConfigSnoopingType_Object = MibTableColumn
hpnicfMcsPortConfigSnoopingType = _HpnicfMcsPortConfigSnoopingType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 123, 1, 8, 1, 2),
    _HpnicfMcsPortConfigSnoopingType_Type()
)
hpnicfMcsPortConfigSnoopingType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfMcsPortConfigSnoopingType.setStatus("current")


class _HpnicfMcsPortConfigVlanID_Type(Unsigned32):
    """Custom type hpnicfMcsPortConfigVlanID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_HpnicfMcsPortConfigVlanID_Type.__name__ = "Unsigned32"
_HpnicfMcsPortConfigVlanID_Object = MibTableColumn
hpnicfMcsPortConfigVlanID = _HpnicfMcsPortConfigVlanID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 123, 1, 8, 1, 3),
    _HpnicfMcsPortConfigVlanID_Type()
)
hpnicfMcsPortConfigVlanID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfMcsPortConfigVlanID.setStatus("current")
_HpnicfMcsPortConfigGroupLimitNumber_Type = Unsigned32
_HpnicfMcsPortConfigGroupLimitNumber_Object = MibTableColumn
hpnicfMcsPortConfigGroupLimitNumber = _HpnicfMcsPortConfigGroupLimitNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 123, 1, 8, 1, 4),
    _HpnicfMcsPortConfigGroupLimitNumber_Type()
)
hpnicfMcsPortConfigGroupLimitNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMcsPortConfigGroupLimitNumber.setStatus("current")


class _HpnicfMcsPortConfigFastLeaveStatus_Type(TruthValue):
    """Custom type hpnicfMcsPortConfigFastLeaveStatus based on TruthValue"""


_HpnicfMcsPortConfigFastLeaveStatus_Object = MibTableColumn
hpnicfMcsPortConfigFastLeaveStatus = _HpnicfMcsPortConfigFastLeaveStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 123, 1, 8, 1, 5),
    _HpnicfMcsPortConfigFastLeaveStatus_Type()
)
hpnicfMcsPortConfigFastLeaveStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMcsPortConfigFastLeaveStatus.setStatus("current")


class _HpnicfMcsPortConfigGroupPolicyParameter_Type(Unsigned32):
    """Custom type hpnicfMcsPortConfigGroupPolicyParameter based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2000, 3999),
    )


_HpnicfMcsPortConfigGroupPolicyParameter_Type.__name__ = "Unsigned32"
_HpnicfMcsPortConfigGroupPolicyParameter_Object = MibTableColumn
hpnicfMcsPortConfigGroupPolicyParameter = _HpnicfMcsPortConfigGroupPolicyParameter_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 123, 1, 8, 1, 6),
    _HpnicfMcsPortConfigGroupPolicyParameter_Type()
)
hpnicfMcsPortConfigGroupPolicyParameter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMcsPortConfigGroupPolicyParameter.setStatus("current")


class _HpnicfMcsPortConfigOverflowReplace_Type(TruthValue):
    """Custom type hpnicfMcsPortConfigOverflowReplace based on TruthValue"""


_HpnicfMcsPortConfigOverflowReplace_Object = MibTableColumn
hpnicfMcsPortConfigOverflowReplace = _HpnicfMcsPortConfigOverflowReplace_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 123, 1, 8, 1, 7),
    _HpnicfMcsPortConfigOverflowReplace_Type()
)
hpnicfMcsPortConfigOverflowReplace.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMcsPortConfigOverflowReplace.setStatus("current")
_HpnicfMcsPortConfigRowStatus_Type = RowStatus
_HpnicfMcsPortConfigRowStatus_Object = MibTableColumn
hpnicfMcsPortConfigRowStatus = _HpnicfMcsPortConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 123, 1, 8, 1, 8),
    _HpnicfMcsPortConfigRowStatus_Type()
)
hpnicfMcsPortConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMcsPortConfigRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-MULTICAST-SNOOPING-MIB",
    **{"HpnicfVirtualUnitType": HpnicfVirtualUnitType,
       "hpnicfMulticastSnoop": hpnicfMulticastSnoop,
       "hpnicfMulticastSnoopObject": hpnicfMulticastSnoopObject,
       "hpnicfMcsGlobalConfigTable": hpnicfMcsGlobalConfigTable,
       "hpnicfMcsGlobalConfigEntry": hpnicfMcsGlobalConfigEntry,
       "hpnicfMcsGlbSnoopingType": hpnicfMcsGlbSnoopingType,
       "hpnicfMcsGlbRowStatus": hpnicfMcsGlbRowStatus,
       "hpnicfMcsGlbEntryLimit": hpnicfMcsGlbEntryLimit,
       "hpnicfMcsGlbHostAgingTime": hpnicfMcsGlbHostAgingTime,
       "hpnicfMcsGlbMaxResponseTime": hpnicfMcsGlbMaxResponseTime,
       "hpnicfMcsGlbRouterAgingTime": hpnicfMcsGlbRouterAgingTime,
       "hpnicfMcsGlbLastMemQryInterval": hpnicfMcsGlbLastMemQryInterval,
       "hpnicfMcsGlbDropUnknownEnabled": hpnicfMcsGlbDropUnknownEnabled,
       "hpnicfMcsVirtualUnitConfigTable": hpnicfMcsVirtualUnitConfigTable,
       "hpnicfMcsVirtualUnitConfigEntry": hpnicfMcsVirtualUnitConfigEntry,
       "hpnicfMcsVUType": hpnicfMcsVUType,
       "hpnicfMcsVUID": hpnicfMcsVUID,
       "hpnicfMcsVUSnoopingType": hpnicfMcsVUSnoopingType,
       "hpnicfMcsVURowStatus": hpnicfMcsVURowStatus,
       "hpnicfMcsVUHostAgingTime": hpnicfMcsVUHostAgingTime,
       "hpnicfMcsVUMaxResponseTime": hpnicfMcsVUMaxResponseTime,
       "hpnicfMcsVURouterAgingTime": hpnicfMcsVURouterAgingTime,
       "hpnicfMcsVULastMemQryInterval": hpnicfMcsVULastMemQryInterval,
       "hpnicfMcsVUDropUnknownEnabled": hpnicfMcsVUDropUnknownEnabled,
       "hpnicfMcsVUPimSnoopingEnabled": hpnicfMcsVUPimSnoopingEnabled,
       "hpnicfMcsVUVersion": hpnicfMcsVUVersion,
       "hpnicfMcsVUQuerierEnabled": hpnicfMcsVUQuerierEnabled,
       "hpnicfMcsVUQuerierInterval": hpnicfMcsVUQuerierInterval,
       "hpnicfMcsVUGeneQuerierSourceAddress": hpnicfMcsVUGeneQuerierSourceAddress,
       "hpnicfMcsVUSpecQuerierSourceAddress": hpnicfMcsVUSpecQuerierSourceAddress,
       "hpnicfMcsVULeaveSourceAddress": hpnicfMcsVULeaveSourceAddress,
       "hpnicfMcsVUReportSourceAddress": hpnicfMcsVUReportSourceAddress,
       "hpnicfMcsL2EntryTable": hpnicfMcsL2EntryTable,
       "hpnicfMcsL2EntryEntry": hpnicfMcsL2EntryEntry,
       "hpnicfMcsL2EntryVUType": hpnicfMcsL2EntryVUType,
       "hpnicfMcsL2EntryVUID": hpnicfMcsL2EntryVUID,
       "hpnicfMcsL2EntryAddressType": hpnicfMcsL2EntryAddressType,
       "hpnicfMcsL2EntryGroupAddress": hpnicfMcsL2EntryGroupAddress,
       "hpnicfMcsL2EntrySourceAddress": hpnicfMcsL2EntrySourceAddress,
       "hpnicfMcsL2EntryIfIndex": hpnicfMcsL2EntryIfIndex,
       "hpnicfMcsL2EntryPortType": hpnicfMcsL2EntryPortType,
       "hpnicfMcsL2EntryPortAttribute": hpnicfMcsL2EntryPortAttribute,
       "hpnicfMcsPacketStatisticsTable": hpnicfMcsPacketStatisticsTable,
       "hpnicfMcsPacketStatisticsEntry": hpnicfMcsPacketStatisticsEntry,
       "hpnicfMcsStatisticsSnoopingType": hpnicfMcsStatisticsSnoopingType,
       "hpnicfMcsRxGeneryQueryNum": hpnicfMcsRxGeneryQueryNum,
       "hpnicfMcsRxV2SpecificQueryNum": hpnicfMcsRxV2SpecificQueryNum,
       "hpnicfMcsRxV3SpecificQueryNum": hpnicfMcsRxV3SpecificQueryNum,
       "hpnicfMcsRxV3SpecificSGQueryNum": hpnicfMcsRxV3SpecificSGQueryNum,
       "hpnicfMcsRxV1ReportNum": hpnicfMcsRxV1ReportNum,
       "hpnicfMcsRxV2ReportNum": hpnicfMcsRxV2ReportNum,
       "hpnicfMcsRxV3ReportNum": hpnicfMcsRxV3ReportNum,
       "hpnicfMcsRxV3ErrCorReportNum": hpnicfMcsRxV3ErrCorReportNum,
       "hpnicfMcsRxLeaveNum": hpnicfMcsRxLeaveNum,
       "hpnicfMcsRxPimHelloNum": hpnicfMcsRxPimHelloNum,
       "hpnicfMcsRxErrorPacketNum": hpnicfMcsRxErrorPacketNum,
       "hpnicfMcsTxV2SpecificQueryNum": hpnicfMcsTxV2SpecificQueryNum,
       "hpnicfMcsTxV3SpecificQueryNum": hpnicfMcsTxV3SpecificQueryNum,
       "hpnicfMcsTxV3SpecificSGQueryNum": hpnicfMcsTxV3SpecificSGQueryNum,
       "hpnicfMcsPortJoinGroupConfigTable": hpnicfMcsPortJoinGroupConfigTable,
       "hpnicfMcsPortJoinGroupConfigEntry": hpnicfMcsPortJoinGroupConfigEntry,
       "hpnicfMcsPortJoinGroupIfIndex": hpnicfMcsPortJoinGroupIfIndex,
       "hpnicfMcsPortJoinGroupSnoopingType": hpnicfMcsPortJoinGroupSnoopingType,
       "hpnicfMcsPortJoinGroupVlanID": hpnicfMcsPortJoinGroupVlanID,
       "hpnicfMcsPortJoinGroupGroupAddress": hpnicfMcsPortJoinGroupGroupAddress,
       "hpnicfMcsPortJoinGroupSourceAddress": hpnicfMcsPortJoinGroupSourceAddress,
       "hpnicfMcsPortJoinGroupStatus": hpnicfMcsPortJoinGroupStatus,
       "hpnicfMcsPortStaticGroupConfigTable": hpnicfMcsPortStaticGroupConfigTable,
       "hpnicfMcsPortStaticGroupConfigEntry": hpnicfMcsPortStaticGroupConfigEntry,
       "hpnicfMcsPortStaticGroupIfIndex": hpnicfMcsPortStaticGroupIfIndex,
       "hpnicfMcsPortStaticGroupSnoopingType": hpnicfMcsPortStaticGroupSnoopingType,
       "hpnicfMcsPortStaticGroupVlanID": hpnicfMcsPortStaticGroupVlanID,
       "hpnicfMcsPortStaticGroupGroupAddress": hpnicfMcsPortStaticGroupGroupAddress,
       "hpnicfMcsPortStaticGroupSourceAddress": hpnicfMcsPortStaticGroupSourceAddress,
       "hpnicfMcsPortStaticGroupStatus": hpnicfMcsPortStaticGroupStatus,
       "hpnicfMcsRouterPortConfigTable": hpnicfMcsRouterPortConfigTable,
       "hpnicfMcsRouterPortConfigEntry": hpnicfMcsRouterPortConfigEntry,
       "hpnicfMcsRouterPortConfigIfIndex": hpnicfMcsRouterPortConfigIfIndex,
       "hpnicfMcsRouterPortConfigSnoopingType": hpnicfMcsRouterPortConfigSnoopingType,
       "hpnicfMcsRouterPortConfigVlanID": hpnicfMcsRouterPortConfigVlanID,
       "hpnicfMcsRouterPortConfigRowStatus": hpnicfMcsRouterPortConfigRowStatus,
       "hpnicfMcsPortConfigTable": hpnicfMcsPortConfigTable,
       "hpnicfMcsPortConfigEntry": hpnicfMcsPortConfigEntry,
       "hpnicfMcsPortConfigIfIndex": hpnicfMcsPortConfigIfIndex,
       "hpnicfMcsPortConfigSnoopingType": hpnicfMcsPortConfigSnoopingType,
       "hpnicfMcsPortConfigVlanID": hpnicfMcsPortConfigVlanID,
       "hpnicfMcsPortConfigGroupLimitNumber": hpnicfMcsPortConfigGroupLimitNumber,
       "hpnicfMcsPortConfigFastLeaveStatus": hpnicfMcsPortConfigFastLeaveStatus,
       "hpnicfMcsPortConfigGroupPolicyParameter": hpnicfMcsPortConfigGroupPolicyParameter,
       "hpnicfMcsPortConfigOverflowReplace": hpnicfMcsPortConfigOverflowReplace,
       "hpnicfMcsPortConfigRowStatus": hpnicfMcsPortConfigRowStatus}
)
