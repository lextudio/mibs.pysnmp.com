# SNMP MIB module (ZYXEL-ARP-INSPECTION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZYXEL-ARP-INSPECTION-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:21:22 2024
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

(dot1dBasePort,) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "dot1dBasePort")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "TextualConvention")

(esMgmt,) = mibBuilder.importSymbols(
    "ZYXEL-ES-SMI",
    "esMgmt")


# MODULE-IDENTITY

zyxelArpInspection = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 12)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZyxelArpInspectSetup_ObjectIdentity = ObjectIdentity
zyxelArpInspectSetup = _ZyxelArpInspectSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 12, 1)
)
_ZyArpInspectState_Type = EnabledStatus
_ZyArpInspectState_Object = MibScalar
zyArpInspectState = _ZyArpInspectState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 12, 1, 1),
    _ZyArpInspectState_Type()
)
zyArpInspectState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyArpInspectState.setStatus("current")


class _ZyArpInspectFilterAgingTime_Type(Integer32):
    """Custom type zyArpInspectFilterAgingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ZyArpInspectFilterAgingTime_Type.__name__ = "Integer32"
_ZyArpInspectFilterAgingTime_Object = MibScalar
zyArpInspectFilterAgingTime = _ZyArpInspectFilterAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 12, 1, 2),
    _ZyArpInspectFilterAgingTime_Type()
)
zyArpInspectFilterAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyArpInspectFilterAgingTime.setStatus("current")
_ZyxelArpInspectLog_ObjectIdentity = ObjectIdentity
zyxelArpInspectLog = _ZyxelArpInspectLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 12, 1, 3)
)


class _ZyArpInspectLogEntries_Type(Integer32):
    """Custom type zyArpInspectLogEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_ZyArpInspectLogEntries_Type.__name__ = "Integer32"
_ZyArpInspectLogEntries_Object = MibScalar
zyArpInspectLogEntries = _ZyArpInspectLogEntries_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 12, 1, 3, 1),
    _ZyArpInspectLogEntries_Type()
)
zyArpInspectLogEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyArpInspectLogEntries.setStatus("current")


class _ZyArpInspectLogRate_Type(Integer32):
    """Custom type zyArpInspectLogRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_ZyArpInspectLogRate_Type.__name__ = "Integer32"
_ZyArpInspectLogRate_Object = MibScalar
zyArpInspectLogRate = _ZyArpInspectLogRate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 12, 1, 3, 2),
    _ZyArpInspectLogRate_Type()
)
zyArpInspectLogRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyArpInspectLogRate.setStatus("current")


class _ZyArpInspectLogInterval_Type(Integer32):
    """Custom type zyArpInspectLogInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ZyArpInspectLogInterval_Type.__name__ = "Integer32"
_ZyArpInspectLogInterval_Object = MibScalar
zyArpInspectLogInterval = _ZyArpInspectLogInterval_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 12, 1, 3, 3),
    _ZyArpInspectLogInterval_Type()
)
zyArpInspectLogInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyArpInspectLogInterval.setStatus("current")
_ZyxelArpInspectVlanTable_Object = MibTable
zyxelArpInspectVlanTable = _ZyxelArpInspectVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 12, 1, 4)
)
if mibBuilder.loadTexts:
    zyxelArpInspectVlanTable.setStatus("current")
_ZyxelArpInspectVlanEntry_Object = MibTableRow
zyxelArpInspectVlanEntry = _ZyxelArpInspectVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 12, 1, 4, 1)
)
zyxelArpInspectVlanEntry.setIndexNames(
    (0, "ZYXEL-ARP-INSPECTION-MIB", "zyArpInspectVlanVid"),
)
if mibBuilder.loadTexts:
    zyxelArpInspectVlanEntry.setStatus("current")


class _ZyArpInspectVlanVid_Type(Integer32):
    """Custom type zyArpInspectVlanVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_ZyArpInspectVlanVid_Type.__name__ = "Integer32"
_ZyArpInspectVlanVid_Object = MibTableColumn
zyArpInspectVlanVid = _ZyArpInspectVlanVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 12, 1, 4, 1, 1),
    _ZyArpInspectVlanVid_Type()
)
zyArpInspectVlanVid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyArpInspectVlanVid.setStatus("current")
_ZyArpInspectVlanState_Type = EnabledStatus
_ZyArpInspectVlanState_Object = MibTableColumn
zyArpInspectVlanState = _ZyArpInspectVlanState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 12, 1, 4, 1, 2),
    _ZyArpInspectVlanState_Type()
)
zyArpInspectVlanState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyArpInspectVlanState.setStatus("current")


class _ZyArpInspectVlanLog_Type(Integer32):
    """Custom type zyArpInspectVlanLog based on Integer32"""
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
        *(("all", 1),
          ("deny", 4),
          ("none", 2),
          ("permit", 3))
    )


_ZyArpInspectVlanLog_Type.__name__ = "Integer32"
_ZyArpInspectVlanLog_Object = MibTableColumn
zyArpInspectVlanLog = _ZyArpInspectVlanLog_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 12, 1, 4, 1, 3),
    _ZyArpInspectVlanLog_Type()
)
zyArpInspectVlanLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyArpInspectVlanLog.setStatus("current")
_ZyxelArpInspectPortTable_Object = MibTable
zyxelArpInspectPortTable = _ZyxelArpInspectPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 12, 1, 5)
)
if mibBuilder.loadTexts:
    zyxelArpInspectPortTable.setStatus("current")
_ZyxelArpInspectPortEntry_Object = MibTableRow
zyxelArpInspectPortEntry = _ZyxelArpInspectPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 12, 1, 5, 1)
)
zyxelArpInspectPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    zyxelArpInspectPortEntry.setStatus("current")


class _ZyArpInspectPortTrustState_Type(EnabledStatus):
    """Custom type zyArpInspectPortTrustState based on EnabledStatus"""
    subtypeSpec = EnabledStatus.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("trusted", 1),
          ("untrusted", 2))
    )


_ZyArpInspectPortTrustState_Type.__name__ = "EnabledStatus"
_ZyArpInspectPortTrustState_Object = MibTableColumn
zyArpInspectPortTrustState = _ZyArpInspectPortTrustState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 12, 1, 5, 1, 1),
    _ZyArpInspectPortTrustState_Type()
)
zyArpInspectPortTrustState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyArpInspectPortTrustState.setStatus("current")


class _ZyArpInspectPortRate_Type(Integer32):
    """Custom type zyArpInspectPortRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048),
    )


_ZyArpInspectPortRate_Type.__name__ = "Integer32"
_ZyArpInspectPortRate_Object = MibTableColumn
zyArpInspectPortRate = _ZyArpInspectPortRate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 12, 1, 5, 1, 2),
    _ZyArpInspectPortRate_Type()
)
zyArpInspectPortRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyArpInspectPortRate.setStatus("current")


class _ZyArpInspectPortInterval_Type(Integer32):
    """Custom type zyArpInspectPortInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_ZyArpInspectPortInterval_Type.__name__ = "Integer32"
_ZyArpInspectPortInterval_Object = MibTableColumn
zyArpInspectPortInterval = _ZyArpInspectPortInterval_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 12, 1, 5, 1, 3),
    _ZyArpInspectPortInterval_Type()
)
zyArpInspectPortInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyArpInspectPortInterval.setStatus("current")
_ZyxelArpInspectStatus_ObjectIdentity = ObjectIdentity
zyxelArpInspectStatus = _ZyxelArpInspectStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 12, 2)
)
_ZyArpInspectFilterClearAll_Type = EnabledStatus
_ZyArpInspectFilterClearAll_Object = MibScalar
zyArpInspectFilterClearAll = _ZyArpInspectFilterClearAll_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 12, 2, 1),
    _ZyArpInspectFilterClearAll_Type()
)
zyArpInspectFilterClearAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyArpInspectFilterClearAll.setStatus("current")
_ZyArpInspectLogClear_Type = EnabledStatus
_ZyArpInspectLogClear_Object = MibScalar
zyArpInspectLogClear = _ZyArpInspectLogClear_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 12, 2, 2),
    _ZyArpInspectLogClear_Type()
)
zyArpInspectLogClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyArpInspectLogClear.setStatus("current")
_ZyxelArpInspectFilterTable_Object = MibTable
zyxelArpInspectFilterTable = _ZyxelArpInspectFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 12, 2, 3)
)
if mibBuilder.loadTexts:
    zyxelArpInspectFilterTable.setStatus("current")
_ZyxelArpInspectFilterEntry_Object = MibTableRow
zyxelArpInspectFilterEntry = _ZyxelArpInspectFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 12, 2, 3, 1)
)
zyxelArpInspectFilterEntry.setIndexNames(
    (0, "ZYXEL-ARP-INSPECTION-MIB", "zyArpInspectFilterMacAddress"),
    (0, "ZYXEL-ARP-INSPECTION-MIB", "zyArpInspectFilterVid"),
)
if mibBuilder.loadTexts:
    zyxelArpInspectFilterEntry.setStatus("current")
_ZyArpInspectFilterMacAddress_Type = MacAddress
_ZyArpInspectFilterMacAddress_Object = MibTableColumn
zyArpInspectFilterMacAddress = _ZyArpInspectFilterMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 12, 2, 3, 1, 1),
    _ZyArpInspectFilterMacAddress_Type()
)
zyArpInspectFilterMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyArpInspectFilterMacAddress.setStatus("current")


class _ZyArpInspectFilterVid_Type(Integer32):
    """Custom type zyArpInspectFilterVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_ZyArpInspectFilterVid_Type.__name__ = "Integer32"
_ZyArpInspectFilterVid_Object = MibTableColumn
zyArpInspectFilterVid = _ZyArpInspectFilterVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 12, 2, 3, 1, 2),
    _ZyArpInspectFilterVid_Type()
)
zyArpInspectFilterVid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyArpInspectFilterVid.setStatus("current")
_ZyArpInspectFilterPort_Type = Integer32
_ZyArpInspectFilterPort_Object = MibTableColumn
zyArpInspectFilterPort = _ZyArpInspectFilterPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 12, 2, 3, 1, 3),
    _ZyArpInspectFilterPort_Type()
)
zyArpInspectFilterPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyArpInspectFilterPort.setStatus("current")
_ZyArpInspectFilterExpiry_Type = Integer32
_ZyArpInspectFilterExpiry_Object = MibTableColumn
zyArpInspectFilterExpiry = _ZyArpInspectFilterExpiry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 12, 2, 3, 1, 4),
    _ZyArpInspectFilterExpiry_Type()
)
zyArpInspectFilterExpiry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyArpInspectFilterExpiry.setStatus("current")


class _ZyArpInspectFilterReasonType_Type(Integer32):
    """Custom type zyArpInspectFilterReasonType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ip", 3),
          ("macVid", 1),
          ("port", 2))
    )


_ZyArpInspectFilterReasonType_Type.__name__ = "Integer32"
_ZyArpInspectFilterReasonType_Object = MibTableColumn
zyArpInspectFilterReasonType = _ZyArpInspectFilterReasonType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 12, 2, 3, 1, 5),
    _ZyArpInspectFilterReasonType_Type()
)
zyArpInspectFilterReasonType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyArpInspectFilterReasonType.setStatus("current")
_ZyArpInspectFilterClear_Type = EnabledStatus
_ZyArpInspectFilterClear_Object = MibTableColumn
zyArpInspectFilterClear = _ZyArpInspectFilterClear_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 12, 2, 3, 1, 6),
    _ZyArpInspectFilterClear_Type()
)
zyArpInspectFilterClear.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zyArpInspectFilterClear.setStatus("current")
_ZyxelArpInspectLogTable_Object = MibTable
zyxelArpInspectLogTable = _ZyxelArpInspectLogTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 12, 2, 4)
)
if mibBuilder.loadTexts:
    zyxelArpInspectLogTable.setStatus("current")
_ZyxelArpInspectLogEntry_Object = MibTableRow
zyxelArpInspectLogEntry = _ZyxelArpInspectLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 12, 2, 4, 1)
)
zyxelArpInspectLogEntry.setIndexNames(
    (0, "ZYXEL-ARP-INSPECTION-MIB", "zyArpInspectLogMacAdderss"),
    (0, "ZYXEL-ARP-INSPECTION-MIB", "zyArpInspectLogVid"),
    (0, "ZYXEL-ARP-INSPECTION-MIB", "zyArpInspectLogPort"),
    (0, "ZYXEL-ARP-INSPECTION-MIB", "zyArpInspectLogIpAddress"),
    (0, "ZYXEL-ARP-INSPECTION-MIB", "zyArpInspectLogReasonType"),
)
if mibBuilder.loadTexts:
    zyxelArpInspectLogEntry.setStatus("current")
_ZyArpInspectLogMacAdderss_Type = MacAddress
_ZyArpInspectLogMacAdderss_Object = MibTableColumn
zyArpInspectLogMacAdderss = _ZyArpInspectLogMacAdderss_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 12, 2, 4, 1, 1),
    _ZyArpInspectLogMacAdderss_Type()
)
zyArpInspectLogMacAdderss.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyArpInspectLogMacAdderss.setStatus("current")


class _ZyArpInspectLogVid_Type(Integer32):
    """Custom type zyArpInspectLogVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_ZyArpInspectLogVid_Type.__name__ = "Integer32"
_ZyArpInspectLogVid_Object = MibTableColumn
zyArpInspectLogVid = _ZyArpInspectLogVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 12, 2, 4, 1, 2),
    _ZyArpInspectLogVid_Type()
)
zyArpInspectLogVid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyArpInspectLogVid.setStatus("current")
_ZyArpInspectLogPort_Type = Integer32
_ZyArpInspectLogPort_Object = MibTableColumn
zyArpInspectLogPort = _ZyArpInspectLogPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 12, 2, 4, 1, 3),
    _ZyArpInspectLogPort_Type()
)
zyArpInspectLogPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyArpInspectLogPort.setStatus("current")
_ZyArpInspectLogIpAddress_Type = IpAddress
_ZyArpInspectLogIpAddress_Object = MibTableColumn
zyArpInspectLogIpAddress = _ZyArpInspectLogIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 12, 2, 4, 1, 4),
    _ZyArpInspectLogIpAddress_Type()
)
zyArpInspectLogIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyArpInspectLogIpAddress.setStatus("current")
_ZyArpInspectLogNumberPacket_Type = Integer32
_ZyArpInspectLogNumberPacket_Object = MibTableColumn
zyArpInspectLogNumberPacket = _ZyArpInspectLogNumberPacket_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 12, 2, 4, 1, 5),
    _ZyArpInspectLogNumberPacket_Type()
)
zyArpInspectLogNumberPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyArpInspectLogNumberPacket.setStatus("current")


class _ZyArpInspectLogReasonType_Type(Integer32):
    """Custom type zyArpInspectLogReasonType based on Integer32"""
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
        *(("deny", 1),
          ("denyDHCP", 3),
          ("denyStatic", 2),
          ("permitDHCP", 5),
          ("permitStatic", 4))
    )


_ZyArpInspectLogReasonType_Type.__name__ = "Integer32"
_ZyArpInspectLogReasonType_Object = MibTableColumn
zyArpInspectLogReasonType = _ZyArpInspectLogReasonType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 12, 2, 4, 1, 6),
    _ZyArpInspectLogReasonType_Type()
)
zyArpInspectLogReasonType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyArpInspectLogReasonType.setStatus("current")
_ZyArpInspectLogTime_Type = DateAndTime
_ZyArpInspectLogTime_Object = MibTableColumn
zyArpInspectLogTime = _ZyArpInspectLogTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 12, 2, 4, 1, 7),
    _ZyArpInspectLogTime_Type()
)
zyArpInspectLogTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyArpInspectLogTime.setStatus("current")
_ZyxelArpInspectStatisticsTable_Object = MibTable
zyxelArpInspectStatisticsTable = _ZyxelArpInspectStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 12, 2, 5)
)
if mibBuilder.loadTexts:
    zyxelArpInspectStatisticsTable.setStatus("current")
_ZyxelArpInspectStatisticsEntry_Object = MibTableRow
zyxelArpInspectStatisticsEntry = _ZyxelArpInspectStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 12, 2, 5, 1)
)
zyxelArpInspectStatisticsEntry.setIndexNames(
    (0, "ZYXEL-ARP-INSPECTION-MIB", "zyArpInspectStatisticsVid"),
)
if mibBuilder.loadTexts:
    zyxelArpInspectStatisticsEntry.setStatus("current")
_ZyArpInspectStatisticsVid_Type = Integer32
_ZyArpInspectStatisticsVid_Object = MibTableColumn
zyArpInspectStatisticsVid = _ZyArpInspectStatisticsVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 12, 2, 5, 1, 1),
    _ZyArpInspectStatisticsVid_Type()
)
zyArpInspectStatisticsVid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyArpInspectStatisticsVid.setStatus("current")
_ZyArpInspectStatisticsReceived_Type = Counter32
_ZyArpInspectStatisticsReceived_Object = MibTableColumn
zyArpInspectStatisticsReceived = _ZyArpInspectStatisticsReceived_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 12, 2, 5, 1, 2),
    _ZyArpInspectStatisticsReceived_Type()
)
zyArpInspectStatisticsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyArpInspectStatisticsReceived.setStatus("current")
_ZyArpInspectStatisticsRequest_Type = Counter32
_ZyArpInspectStatisticsRequest_Object = MibTableColumn
zyArpInspectStatisticsRequest = _ZyArpInspectStatisticsRequest_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 12, 2, 5, 1, 3),
    _ZyArpInspectStatisticsRequest_Type()
)
zyArpInspectStatisticsRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyArpInspectStatisticsRequest.setStatus("current")
_ZyArpInspectStatisticsReply_Type = Counter32
_ZyArpInspectStatisticsReply_Object = MibTableColumn
zyArpInspectStatisticsReply = _ZyArpInspectStatisticsReply_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 12, 2, 5, 1, 4),
    _ZyArpInspectStatisticsReply_Type()
)
zyArpInspectStatisticsReply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyArpInspectStatisticsReply.setStatus("current")
_ZyArpInspectStatisticsForward_Type = Counter32
_ZyArpInspectStatisticsForward_Object = MibTableColumn
zyArpInspectStatisticsForward = _ZyArpInspectStatisticsForward_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 12, 2, 5, 1, 5),
    _ZyArpInspectStatisticsForward_Type()
)
zyArpInspectStatisticsForward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyArpInspectStatisticsForward.setStatus("current")
_ZyArpInspectStatisticsDrop_Type = Counter32
_ZyArpInspectStatisticsDrop_Object = MibTableColumn
zyArpInspectStatisticsDrop = _ZyArpInspectStatisticsDrop_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 12, 2, 5, 1, 6),
    _ZyArpInspectStatisticsDrop_Type()
)
zyArpInspectStatisticsDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyArpInspectStatisticsDrop.setStatus("current")
_ZyArpInspectStatisticsClear_Type = EnabledStatus
_ZyArpInspectStatisticsClear_Object = MibTableColumn
zyArpInspectStatisticsClear = _ZyArpInspectStatisticsClear_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 12, 2, 5, 1, 7),
    _ZyArpInspectStatisticsClear_Type()
)
zyArpInspectStatisticsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyArpInspectStatisticsClear.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-ARP-INSPECTION-MIB",
    **{"zyxelArpInspection": zyxelArpInspection,
       "zyxelArpInspectSetup": zyxelArpInspectSetup,
       "zyArpInspectState": zyArpInspectState,
       "zyArpInspectFilterAgingTime": zyArpInspectFilterAgingTime,
       "zyxelArpInspectLog": zyxelArpInspectLog,
       "zyArpInspectLogEntries": zyArpInspectLogEntries,
       "zyArpInspectLogRate": zyArpInspectLogRate,
       "zyArpInspectLogInterval": zyArpInspectLogInterval,
       "zyxelArpInspectVlanTable": zyxelArpInspectVlanTable,
       "zyxelArpInspectVlanEntry": zyxelArpInspectVlanEntry,
       "zyArpInspectVlanVid": zyArpInspectVlanVid,
       "zyArpInspectVlanState": zyArpInspectVlanState,
       "zyArpInspectVlanLog": zyArpInspectVlanLog,
       "zyxelArpInspectPortTable": zyxelArpInspectPortTable,
       "zyxelArpInspectPortEntry": zyxelArpInspectPortEntry,
       "zyArpInspectPortTrustState": zyArpInspectPortTrustState,
       "zyArpInspectPortRate": zyArpInspectPortRate,
       "zyArpInspectPortInterval": zyArpInspectPortInterval,
       "zyxelArpInspectStatus": zyxelArpInspectStatus,
       "zyArpInspectFilterClearAll": zyArpInspectFilterClearAll,
       "zyArpInspectLogClear": zyArpInspectLogClear,
       "zyxelArpInspectFilterTable": zyxelArpInspectFilterTable,
       "zyxelArpInspectFilterEntry": zyxelArpInspectFilterEntry,
       "zyArpInspectFilterMacAddress": zyArpInspectFilterMacAddress,
       "zyArpInspectFilterVid": zyArpInspectFilterVid,
       "zyArpInspectFilterPort": zyArpInspectFilterPort,
       "zyArpInspectFilterExpiry": zyArpInspectFilterExpiry,
       "zyArpInspectFilterReasonType": zyArpInspectFilterReasonType,
       "zyArpInspectFilterClear": zyArpInspectFilterClear,
       "zyxelArpInspectLogTable": zyxelArpInspectLogTable,
       "zyxelArpInspectLogEntry": zyxelArpInspectLogEntry,
       "zyArpInspectLogMacAdderss": zyArpInspectLogMacAdderss,
       "zyArpInspectLogVid": zyArpInspectLogVid,
       "zyArpInspectLogPort": zyArpInspectLogPort,
       "zyArpInspectLogIpAddress": zyArpInspectLogIpAddress,
       "zyArpInspectLogNumberPacket": zyArpInspectLogNumberPacket,
       "zyArpInspectLogReasonType": zyArpInspectLogReasonType,
       "zyArpInspectLogTime": zyArpInspectLogTime,
       "zyxelArpInspectStatisticsTable": zyxelArpInspectStatisticsTable,
       "zyxelArpInspectStatisticsEntry": zyxelArpInspectStatisticsEntry,
       "zyArpInspectStatisticsVid": zyArpInspectStatisticsVid,
       "zyArpInspectStatisticsReceived": zyArpInspectStatisticsReceived,
       "zyArpInspectStatisticsRequest": zyArpInspectStatisticsRequest,
       "zyArpInspectStatisticsReply": zyArpInspectStatisticsReply,
       "zyArpInspectStatisticsForward": zyArpInspectStatisticsForward,
       "zyArpInspectStatisticsDrop": zyArpInspectStatisticsDrop,
       "zyArpInspectStatisticsClear": zyArpInspectStatisticsClear}
)
