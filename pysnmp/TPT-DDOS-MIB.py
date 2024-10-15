# SNMP MIB module (TPT-DDOS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TPT-DDOS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:06:55 2024
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

(tpt_tpa_objs,) = mibBuilder.importSymbols(
    "TPT-TPAMIBS-MIB",
    "tpt-tpa-objs")


# MODULE-IDENTITY

tpt_ddos = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9)
)
tpt_ddos.setRevisions(
        ("2016-05-25 18:54",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RejectSynHistSecondsTable_Object = MibTable
rejectSynHistSecondsTable = _RejectSynHistSecondsTable_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 5)
)
if mibBuilder.loadTexts:
    rejectSynHistSecondsTable.setStatus("current")
_RejectSynHistSecondsEntry_Object = MibTableRow
rejectSynHistSecondsEntry = _RejectSynHistSecondsEntry_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 5, 1)
)
rejectSynHistSecondsEntry.setIndexNames(
    (0, "TPT-DDOS-MIB", "rejectSynHistSecondsGlobalID"),
    (0, "TPT-DDOS-MIB", "rejectSynHistSecondsIndex"),
)
if mibBuilder.loadTexts:
    rejectSynHistSecondsEntry.setStatus("current")


class _RejectSynHistSecondsGlobalID_Type(OctetString):
    """Custom type rejectSynHistSecondsGlobalID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_RejectSynHistSecondsGlobalID_Type.__name__ = "OctetString"
_RejectSynHistSecondsGlobalID_Object = MibTableColumn
rejectSynHistSecondsGlobalID = _RejectSynHistSecondsGlobalID_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 5, 1, 1),
    _RejectSynHistSecondsGlobalID_Type()
)
rejectSynHistSecondsGlobalID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rejectSynHistSecondsGlobalID.setStatus("current")
_RejectSynHistSecondsIndex_Type = Unsigned32
_RejectSynHistSecondsIndex_Object = MibTableColumn
rejectSynHistSecondsIndex = _RejectSynHistSecondsIndex_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 5, 1, 2),
    _RejectSynHistSecondsIndex_Type()
)
rejectSynHistSecondsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rejectSynHistSecondsIndex.setStatus("current")
_RejectSynHistSecondsUnitCount_Type = Counter64
_RejectSynHistSecondsUnitCount_Object = MibTableColumn
rejectSynHistSecondsUnitCount = _RejectSynHistSecondsUnitCount_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 5, 1, 3),
    _RejectSynHistSecondsUnitCount_Type()
)
rejectSynHistSecondsUnitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rejectSynHistSecondsUnitCount.setStatus("current")
_RejectSynHistSecondsTimestamp_Type = Unsigned32
_RejectSynHistSecondsTimestamp_Object = MibTableColumn
rejectSynHistSecondsTimestamp = _RejectSynHistSecondsTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 5, 1, 4),
    _RejectSynHistSecondsTimestamp_Type()
)
rejectSynHistSecondsTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rejectSynHistSecondsTimestamp.setStatus("current")
_RejectSynHistMinutesTable_Object = MibTable
rejectSynHistMinutesTable = _RejectSynHistMinutesTable_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 6)
)
if mibBuilder.loadTexts:
    rejectSynHistMinutesTable.setStatus("current")
_RejectSynHistMinutesEntry_Object = MibTableRow
rejectSynHistMinutesEntry = _RejectSynHistMinutesEntry_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 6, 1)
)
rejectSynHistMinutesEntry.setIndexNames(
    (0, "TPT-DDOS-MIB", "rejectSynHistMinutesGlobalID"),
    (0, "TPT-DDOS-MIB", "rejectSynHistMinutesIndex"),
)
if mibBuilder.loadTexts:
    rejectSynHistMinutesEntry.setStatus("current")


class _RejectSynHistMinutesGlobalID_Type(OctetString):
    """Custom type rejectSynHistMinutesGlobalID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_RejectSynHistMinutesGlobalID_Type.__name__ = "OctetString"
_RejectSynHistMinutesGlobalID_Object = MibTableColumn
rejectSynHistMinutesGlobalID = _RejectSynHistMinutesGlobalID_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 6, 1, 1),
    _RejectSynHistMinutesGlobalID_Type()
)
rejectSynHistMinutesGlobalID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rejectSynHistMinutesGlobalID.setStatus("current")
_RejectSynHistMinutesIndex_Type = Unsigned32
_RejectSynHistMinutesIndex_Object = MibTableColumn
rejectSynHistMinutesIndex = _RejectSynHistMinutesIndex_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 6, 1, 2),
    _RejectSynHistMinutesIndex_Type()
)
rejectSynHistMinutesIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rejectSynHistMinutesIndex.setStatus("current")
_RejectSynHistMinutesUnitCount_Type = Counter64
_RejectSynHistMinutesUnitCount_Object = MibTableColumn
rejectSynHistMinutesUnitCount = _RejectSynHistMinutesUnitCount_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 6, 1, 3),
    _RejectSynHistMinutesUnitCount_Type()
)
rejectSynHistMinutesUnitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rejectSynHistMinutesUnitCount.setStatus("current")
_RejectSynHistMinutesTimestamp_Type = Unsigned32
_RejectSynHistMinutesTimestamp_Object = MibTableColumn
rejectSynHistMinutesTimestamp = _RejectSynHistMinutesTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 6, 1, 4),
    _RejectSynHistMinutesTimestamp_Type()
)
rejectSynHistMinutesTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rejectSynHistMinutesTimestamp.setStatus("current")
_RejectSynHistHoursTable_Object = MibTable
rejectSynHistHoursTable = _RejectSynHistHoursTable_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 7)
)
if mibBuilder.loadTexts:
    rejectSynHistHoursTable.setStatus("current")
_RejectSynHistHoursEntry_Object = MibTableRow
rejectSynHistHoursEntry = _RejectSynHistHoursEntry_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 7, 1)
)
rejectSynHistHoursEntry.setIndexNames(
    (0, "TPT-DDOS-MIB", "rejectSynHistHoursGlobalID"),
    (0, "TPT-DDOS-MIB", "rejectSynHistHoursIndex"),
)
if mibBuilder.loadTexts:
    rejectSynHistHoursEntry.setStatus("current")


class _RejectSynHistHoursGlobalID_Type(OctetString):
    """Custom type rejectSynHistHoursGlobalID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_RejectSynHistHoursGlobalID_Type.__name__ = "OctetString"
_RejectSynHistHoursGlobalID_Object = MibTableColumn
rejectSynHistHoursGlobalID = _RejectSynHistHoursGlobalID_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 7, 1, 1),
    _RejectSynHistHoursGlobalID_Type()
)
rejectSynHistHoursGlobalID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rejectSynHistHoursGlobalID.setStatus("current")
_RejectSynHistHoursIndex_Type = Unsigned32
_RejectSynHistHoursIndex_Object = MibTableColumn
rejectSynHistHoursIndex = _RejectSynHistHoursIndex_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 7, 1, 2),
    _RejectSynHistHoursIndex_Type()
)
rejectSynHistHoursIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rejectSynHistHoursIndex.setStatus("current")
_RejectSynHistHoursUnitCount_Type = Counter64
_RejectSynHistHoursUnitCount_Object = MibTableColumn
rejectSynHistHoursUnitCount = _RejectSynHistHoursUnitCount_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 7, 1, 3),
    _RejectSynHistHoursUnitCount_Type()
)
rejectSynHistHoursUnitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rejectSynHistHoursUnitCount.setStatus("current")
_RejectSynHistHoursTimestamp_Type = Unsigned32
_RejectSynHistHoursTimestamp_Object = MibTableColumn
rejectSynHistHoursTimestamp = _RejectSynHistHoursTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 7, 1, 4),
    _RejectSynHistHoursTimestamp_Type()
)
rejectSynHistHoursTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rejectSynHistHoursTimestamp.setStatus("current")
_RejectSynHistDaysTable_Object = MibTable
rejectSynHistDaysTable = _RejectSynHistDaysTable_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 8)
)
if mibBuilder.loadTexts:
    rejectSynHistDaysTable.setStatus("current")
_RejectSynHistDaysEntry_Object = MibTableRow
rejectSynHistDaysEntry = _RejectSynHistDaysEntry_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 8, 1)
)
rejectSynHistDaysEntry.setIndexNames(
    (0, "TPT-DDOS-MIB", "rejectSynHistDaysGlobalID"),
    (0, "TPT-DDOS-MIB", "rejectSynHistDaysIndex"),
)
if mibBuilder.loadTexts:
    rejectSynHistDaysEntry.setStatus("current")


class _RejectSynHistDaysGlobalID_Type(OctetString):
    """Custom type rejectSynHistDaysGlobalID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_RejectSynHistDaysGlobalID_Type.__name__ = "OctetString"
_RejectSynHistDaysGlobalID_Object = MibTableColumn
rejectSynHistDaysGlobalID = _RejectSynHistDaysGlobalID_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 8, 1, 1),
    _RejectSynHistDaysGlobalID_Type()
)
rejectSynHistDaysGlobalID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rejectSynHistDaysGlobalID.setStatus("current")
_RejectSynHistDaysIndex_Type = Unsigned32
_RejectSynHistDaysIndex_Object = MibTableColumn
rejectSynHistDaysIndex = _RejectSynHistDaysIndex_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 8, 1, 2),
    _RejectSynHistDaysIndex_Type()
)
rejectSynHistDaysIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rejectSynHistDaysIndex.setStatus("current")
_RejectSynHistDaysUnitCount_Type = Counter64
_RejectSynHistDaysUnitCount_Object = MibTableColumn
rejectSynHistDaysUnitCount = _RejectSynHistDaysUnitCount_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 8, 1, 3),
    _RejectSynHistDaysUnitCount_Type()
)
rejectSynHistDaysUnitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rejectSynHistDaysUnitCount.setStatus("current")
_RejectSynHistDaysTimestamp_Type = Unsigned32
_RejectSynHistDaysTimestamp_Object = MibTableColumn
rejectSynHistDaysTimestamp = _RejectSynHistDaysTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 8, 1, 4),
    _RejectSynHistDaysTimestamp_Type()
)
rejectSynHistDaysTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rejectSynHistDaysTimestamp.setStatus("current")
_ProxyConnHistSecondsTable_Object = MibTable
proxyConnHistSecondsTable = _ProxyConnHistSecondsTable_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 9)
)
if mibBuilder.loadTexts:
    proxyConnHistSecondsTable.setStatus("current")
_ProxyConnHistSecondsEntry_Object = MibTableRow
proxyConnHistSecondsEntry = _ProxyConnHistSecondsEntry_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 9, 1)
)
proxyConnHistSecondsEntry.setIndexNames(
    (0, "TPT-DDOS-MIB", "proxyConnHistSecondsGlobalID"),
    (0, "TPT-DDOS-MIB", "proxyConnHistSecondsIndex"),
)
if mibBuilder.loadTexts:
    proxyConnHistSecondsEntry.setStatus("current")


class _ProxyConnHistSecondsGlobalID_Type(OctetString):
    """Custom type proxyConnHistSecondsGlobalID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_ProxyConnHistSecondsGlobalID_Type.__name__ = "OctetString"
_ProxyConnHistSecondsGlobalID_Object = MibTableColumn
proxyConnHistSecondsGlobalID = _ProxyConnHistSecondsGlobalID_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 9, 1, 1),
    _ProxyConnHistSecondsGlobalID_Type()
)
proxyConnHistSecondsGlobalID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    proxyConnHistSecondsGlobalID.setStatus("current")
_ProxyConnHistSecondsIndex_Type = Unsigned32
_ProxyConnHistSecondsIndex_Object = MibTableColumn
proxyConnHistSecondsIndex = _ProxyConnHistSecondsIndex_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 9, 1, 2),
    _ProxyConnHistSecondsIndex_Type()
)
proxyConnHistSecondsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    proxyConnHistSecondsIndex.setStatus("current")
_ProxyConnHistSecondsUnitCount_Type = Counter64
_ProxyConnHistSecondsUnitCount_Object = MibTableColumn
proxyConnHistSecondsUnitCount = _ProxyConnHistSecondsUnitCount_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 9, 1, 3),
    _ProxyConnHistSecondsUnitCount_Type()
)
proxyConnHistSecondsUnitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proxyConnHistSecondsUnitCount.setStatus("current")
_ProxyConnHistSecondsTimestamp_Type = Unsigned32
_ProxyConnHistSecondsTimestamp_Object = MibTableColumn
proxyConnHistSecondsTimestamp = _ProxyConnHistSecondsTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 9, 1, 4),
    _ProxyConnHistSecondsTimestamp_Type()
)
proxyConnHistSecondsTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proxyConnHistSecondsTimestamp.setStatus("current")
_ProxyConnHistMinutesTable_Object = MibTable
proxyConnHistMinutesTable = _ProxyConnHistMinutesTable_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 10)
)
if mibBuilder.loadTexts:
    proxyConnHistMinutesTable.setStatus("current")
_ProxyConnHistMinutesEntry_Object = MibTableRow
proxyConnHistMinutesEntry = _ProxyConnHistMinutesEntry_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 10, 1)
)
proxyConnHistMinutesEntry.setIndexNames(
    (0, "TPT-DDOS-MIB", "proxyConnHistMinutesGlobalID"),
    (0, "TPT-DDOS-MIB", "proxyConnHistMinutesIndex"),
)
if mibBuilder.loadTexts:
    proxyConnHistMinutesEntry.setStatus("current")


class _ProxyConnHistMinutesGlobalID_Type(OctetString):
    """Custom type proxyConnHistMinutesGlobalID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_ProxyConnHistMinutesGlobalID_Type.__name__ = "OctetString"
_ProxyConnHistMinutesGlobalID_Object = MibTableColumn
proxyConnHistMinutesGlobalID = _ProxyConnHistMinutesGlobalID_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 10, 1, 1),
    _ProxyConnHistMinutesGlobalID_Type()
)
proxyConnHistMinutesGlobalID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    proxyConnHistMinutesGlobalID.setStatus("current")
_ProxyConnHistMinutesIndex_Type = Unsigned32
_ProxyConnHistMinutesIndex_Object = MibTableColumn
proxyConnHistMinutesIndex = _ProxyConnHistMinutesIndex_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 10, 1, 2),
    _ProxyConnHistMinutesIndex_Type()
)
proxyConnHistMinutesIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    proxyConnHistMinutesIndex.setStatus("current")
_ProxyConnHistMinutesUnitCount_Type = Counter64
_ProxyConnHistMinutesUnitCount_Object = MibTableColumn
proxyConnHistMinutesUnitCount = _ProxyConnHistMinutesUnitCount_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 10, 1, 3),
    _ProxyConnHistMinutesUnitCount_Type()
)
proxyConnHistMinutesUnitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proxyConnHistMinutesUnitCount.setStatus("current")
_ProxyConnHistMinutesTimestamp_Type = Unsigned32
_ProxyConnHistMinutesTimestamp_Object = MibTableColumn
proxyConnHistMinutesTimestamp = _ProxyConnHistMinutesTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 10, 1, 4),
    _ProxyConnHistMinutesTimestamp_Type()
)
proxyConnHistMinutesTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proxyConnHistMinutesTimestamp.setStatus("current")
_ProxyConnHistHoursTable_Object = MibTable
proxyConnHistHoursTable = _ProxyConnHistHoursTable_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 11)
)
if mibBuilder.loadTexts:
    proxyConnHistHoursTable.setStatus("current")
_ProxyConnHistHoursEntry_Object = MibTableRow
proxyConnHistHoursEntry = _ProxyConnHistHoursEntry_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 11, 1)
)
proxyConnHistHoursEntry.setIndexNames(
    (0, "TPT-DDOS-MIB", "proxyConnHistHoursGlobalID"),
    (0, "TPT-DDOS-MIB", "proxyConnHistHoursIndex"),
)
if mibBuilder.loadTexts:
    proxyConnHistHoursEntry.setStatus("current")


class _ProxyConnHistHoursGlobalID_Type(OctetString):
    """Custom type proxyConnHistHoursGlobalID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_ProxyConnHistHoursGlobalID_Type.__name__ = "OctetString"
_ProxyConnHistHoursGlobalID_Object = MibTableColumn
proxyConnHistHoursGlobalID = _ProxyConnHistHoursGlobalID_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 11, 1, 1),
    _ProxyConnHistHoursGlobalID_Type()
)
proxyConnHistHoursGlobalID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    proxyConnHistHoursGlobalID.setStatus("current")
_ProxyConnHistHoursIndex_Type = Unsigned32
_ProxyConnHistHoursIndex_Object = MibTableColumn
proxyConnHistHoursIndex = _ProxyConnHistHoursIndex_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 11, 1, 2),
    _ProxyConnHistHoursIndex_Type()
)
proxyConnHistHoursIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    proxyConnHistHoursIndex.setStatus("current")
_ProxyConnHistHoursUnitCount_Type = Counter64
_ProxyConnHistHoursUnitCount_Object = MibTableColumn
proxyConnHistHoursUnitCount = _ProxyConnHistHoursUnitCount_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 11, 1, 3),
    _ProxyConnHistHoursUnitCount_Type()
)
proxyConnHistHoursUnitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proxyConnHistHoursUnitCount.setStatus("current")
_ProxyConnHistHoursTimestamp_Type = Unsigned32
_ProxyConnHistHoursTimestamp_Object = MibTableColumn
proxyConnHistHoursTimestamp = _ProxyConnHistHoursTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 11, 1, 4),
    _ProxyConnHistHoursTimestamp_Type()
)
proxyConnHistHoursTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proxyConnHistHoursTimestamp.setStatus("current")
_ProxyConnHistDaysTable_Object = MibTable
proxyConnHistDaysTable = _ProxyConnHistDaysTable_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 12)
)
if mibBuilder.loadTexts:
    proxyConnHistDaysTable.setStatus("current")
_ProxyConnHistDaysEntry_Object = MibTableRow
proxyConnHistDaysEntry = _ProxyConnHistDaysEntry_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 12, 1)
)
proxyConnHistDaysEntry.setIndexNames(
    (0, "TPT-DDOS-MIB", "proxyConnHistDaysGlobalID"),
    (0, "TPT-DDOS-MIB", "proxyConnHistDaysIndex"),
)
if mibBuilder.loadTexts:
    proxyConnHistDaysEntry.setStatus("current")


class _ProxyConnHistDaysGlobalID_Type(OctetString):
    """Custom type proxyConnHistDaysGlobalID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_ProxyConnHistDaysGlobalID_Type.__name__ = "OctetString"
_ProxyConnHistDaysGlobalID_Object = MibTableColumn
proxyConnHistDaysGlobalID = _ProxyConnHistDaysGlobalID_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 12, 1, 1),
    _ProxyConnHistDaysGlobalID_Type()
)
proxyConnHistDaysGlobalID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    proxyConnHistDaysGlobalID.setStatus("current")
_ProxyConnHistDaysIndex_Type = Unsigned32
_ProxyConnHistDaysIndex_Object = MibTableColumn
proxyConnHistDaysIndex = _ProxyConnHistDaysIndex_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 12, 1, 2),
    _ProxyConnHistDaysIndex_Type()
)
proxyConnHistDaysIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    proxyConnHistDaysIndex.setStatus("current")
_ProxyConnHistDaysUnitCount_Type = Counter64
_ProxyConnHistDaysUnitCount_Object = MibTableColumn
proxyConnHistDaysUnitCount = _ProxyConnHistDaysUnitCount_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 12, 1, 3),
    _ProxyConnHistDaysUnitCount_Type()
)
proxyConnHistDaysUnitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proxyConnHistDaysUnitCount.setStatus("current")
_ProxyConnHistDaysTimestamp_Type = Unsigned32
_ProxyConnHistDaysTimestamp_Object = MibTableColumn
proxyConnHistDaysTimestamp = _ProxyConnHistDaysTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 12, 1, 4),
    _ProxyConnHistDaysTimestamp_Type()
)
proxyConnHistDaysTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proxyConnHistDaysTimestamp.setStatus("current")
_RejectCpsHistSecondsTable_Object = MibTable
rejectCpsHistSecondsTable = _RejectCpsHistSecondsTable_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 15)
)
if mibBuilder.loadTexts:
    rejectCpsHistSecondsTable.setStatus("current")
_RejectCpsHistSecondsEntry_Object = MibTableRow
rejectCpsHistSecondsEntry = _RejectCpsHistSecondsEntry_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 15, 1)
)
rejectCpsHistSecondsEntry.setIndexNames(
    (0, "TPT-DDOS-MIB", "rejectCpsHistSecondsGlobalID"),
    (0, "TPT-DDOS-MIB", "rejectCpsHistSecondsIndex"),
)
if mibBuilder.loadTexts:
    rejectCpsHistSecondsEntry.setStatus("current")


class _RejectCpsHistSecondsGlobalID_Type(OctetString):
    """Custom type rejectCpsHistSecondsGlobalID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_RejectCpsHistSecondsGlobalID_Type.__name__ = "OctetString"
_RejectCpsHistSecondsGlobalID_Object = MibTableColumn
rejectCpsHistSecondsGlobalID = _RejectCpsHistSecondsGlobalID_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 15, 1, 1),
    _RejectCpsHistSecondsGlobalID_Type()
)
rejectCpsHistSecondsGlobalID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rejectCpsHistSecondsGlobalID.setStatus("current")
_RejectCpsHistSecondsIndex_Type = Unsigned32
_RejectCpsHistSecondsIndex_Object = MibTableColumn
rejectCpsHistSecondsIndex = _RejectCpsHistSecondsIndex_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 15, 1, 2),
    _RejectCpsHistSecondsIndex_Type()
)
rejectCpsHistSecondsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rejectCpsHistSecondsIndex.setStatus("current")
_RejectCpsHistSecondsUnitCount_Type = Counter64
_RejectCpsHistSecondsUnitCount_Object = MibTableColumn
rejectCpsHistSecondsUnitCount = _RejectCpsHistSecondsUnitCount_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 15, 1, 3),
    _RejectCpsHistSecondsUnitCount_Type()
)
rejectCpsHistSecondsUnitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rejectCpsHistSecondsUnitCount.setStatus("current")
_RejectCpsHistSecondsTimestamp_Type = Unsigned32
_RejectCpsHistSecondsTimestamp_Object = MibTableColumn
rejectCpsHistSecondsTimestamp = _RejectCpsHistSecondsTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 15, 1, 4),
    _RejectCpsHistSecondsTimestamp_Type()
)
rejectCpsHistSecondsTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rejectCpsHistSecondsTimestamp.setStatus("current")
_RejectCpsHistMinutesTable_Object = MibTable
rejectCpsHistMinutesTable = _RejectCpsHistMinutesTable_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 16)
)
if mibBuilder.loadTexts:
    rejectCpsHistMinutesTable.setStatus("current")
_RejectCpsHistMinutesEntry_Object = MibTableRow
rejectCpsHistMinutesEntry = _RejectCpsHistMinutesEntry_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 16, 1)
)
rejectCpsHistMinutesEntry.setIndexNames(
    (0, "TPT-DDOS-MIB", "rejectCpsHistMinutesGlobalID"),
    (0, "TPT-DDOS-MIB", "rejectCpsHistMinutesIndex"),
)
if mibBuilder.loadTexts:
    rejectCpsHistMinutesEntry.setStatus("current")


class _RejectCpsHistMinutesGlobalID_Type(OctetString):
    """Custom type rejectCpsHistMinutesGlobalID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_RejectCpsHistMinutesGlobalID_Type.__name__ = "OctetString"
_RejectCpsHistMinutesGlobalID_Object = MibTableColumn
rejectCpsHistMinutesGlobalID = _RejectCpsHistMinutesGlobalID_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 16, 1, 1),
    _RejectCpsHistMinutesGlobalID_Type()
)
rejectCpsHistMinutesGlobalID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rejectCpsHistMinutesGlobalID.setStatus("current")
_RejectCpsHistMinutesIndex_Type = Unsigned32
_RejectCpsHistMinutesIndex_Object = MibTableColumn
rejectCpsHistMinutesIndex = _RejectCpsHistMinutesIndex_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 16, 1, 2),
    _RejectCpsHistMinutesIndex_Type()
)
rejectCpsHistMinutesIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rejectCpsHistMinutesIndex.setStatus("current")
_RejectCpsHistMinutesUnitCount_Type = Counter64
_RejectCpsHistMinutesUnitCount_Object = MibTableColumn
rejectCpsHistMinutesUnitCount = _RejectCpsHistMinutesUnitCount_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 16, 1, 3),
    _RejectCpsHistMinutesUnitCount_Type()
)
rejectCpsHistMinutesUnitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rejectCpsHistMinutesUnitCount.setStatus("current")
_RejectCpsHistMinutesTimestamp_Type = Unsigned32
_RejectCpsHistMinutesTimestamp_Object = MibTableColumn
rejectCpsHistMinutesTimestamp = _RejectCpsHistMinutesTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 16, 1, 4),
    _RejectCpsHistMinutesTimestamp_Type()
)
rejectCpsHistMinutesTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rejectCpsHistMinutesTimestamp.setStatus("current")
_RejectCpsHistHoursTable_Object = MibTable
rejectCpsHistHoursTable = _RejectCpsHistHoursTable_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 17)
)
if mibBuilder.loadTexts:
    rejectCpsHistHoursTable.setStatus("current")
_RejectCpsHistHoursEntry_Object = MibTableRow
rejectCpsHistHoursEntry = _RejectCpsHistHoursEntry_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 17, 1)
)
rejectCpsHistHoursEntry.setIndexNames(
    (0, "TPT-DDOS-MIB", "rejectCpsHistHoursGlobalID"),
    (0, "TPT-DDOS-MIB", "rejectCpsHistHoursIndex"),
)
if mibBuilder.loadTexts:
    rejectCpsHistHoursEntry.setStatus("current")


class _RejectCpsHistHoursGlobalID_Type(OctetString):
    """Custom type rejectCpsHistHoursGlobalID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_RejectCpsHistHoursGlobalID_Type.__name__ = "OctetString"
_RejectCpsHistHoursGlobalID_Object = MibTableColumn
rejectCpsHistHoursGlobalID = _RejectCpsHistHoursGlobalID_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 17, 1, 1),
    _RejectCpsHistHoursGlobalID_Type()
)
rejectCpsHistHoursGlobalID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rejectCpsHistHoursGlobalID.setStatus("current")
_RejectCpsHistHoursIndex_Type = Unsigned32
_RejectCpsHistHoursIndex_Object = MibTableColumn
rejectCpsHistHoursIndex = _RejectCpsHistHoursIndex_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 17, 1, 2),
    _RejectCpsHistHoursIndex_Type()
)
rejectCpsHistHoursIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rejectCpsHistHoursIndex.setStatus("current")
_RejectCpsHistHoursUnitCount_Type = Counter64
_RejectCpsHistHoursUnitCount_Object = MibTableColumn
rejectCpsHistHoursUnitCount = _RejectCpsHistHoursUnitCount_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 17, 1, 3),
    _RejectCpsHistHoursUnitCount_Type()
)
rejectCpsHistHoursUnitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rejectCpsHistHoursUnitCount.setStatus("current")
_RejectCpsHistHoursTimestamp_Type = Unsigned32
_RejectCpsHistHoursTimestamp_Object = MibTableColumn
rejectCpsHistHoursTimestamp = _RejectCpsHistHoursTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 17, 1, 4),
    _RejectCpsHistHoursTimestamp_Type()
)
rejectCpsHistHoursTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rejectCpsHistHoursTimestamp.setStatus("current")
_RejectCpsHistDaysTable_Object = MibTable
rejectCpsHistDaysTable = _RejectCpsHistDaysTable_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 18)
)
if mibBuilder.loadTexts:
    rejectCpsHistDaysTable.setStatus("current")
_RejectCpsHistDaysEntry_Object = MibTableRow
rejectCpsHistDaysEntry = _RejectCpsHistDaysEntry_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 18, 1)
)
rejectCpsHistDaysEntry.setIndexNames(
    (0, "TPT-DDOS-MIB", "rejectCpsHistDaysGlobalID"),
    (0, "TPT-DDOS-MIB", "rejectCpsHistDaysIndex"),
)
if mibBuilder.loadTexts:
    rejectCpsHistDaysEntry.setStatus("current")


class _RejectCpsHistDaysGlobalID_Type(OctetString):
    """Custom type rejectCpsHistDaysGlobalID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_RejectCpsHistDaysGlobalID_Type.__name__ = "OctetString"
_RejectCpsHistDaysGlobalID_Object = MibTableColumn
rejectCpsHistDaysGlobalID = _RejectCpsHistDaysGlobalID_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 18, 1, 1),
    _RejectCpsHistDaysGlobalID_Type()
)
rejectCpsHistDaysGlobalID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rejectCpsHistDaysGlobalID.setStatus("current")
_RejectCpsHistDaysIndex_Type = Unsigned32
_RejectCpsHistDaysIndex_Object = MibTableColumn
rejectCpsHistDaysIndex = _RejectCpsHistDaysIndex_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 18, 1, 2),
    _RejectCpsHistDaysIndex_Type()
)
rejectCpsHistDaysIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rejectCpsHistDaysIndex.setStatus("current")
_RejectCpsHistDaysUnitCount_Type = Counter64
_RejectCpsHistDaysUnitCount_Object = MibTableColumn
rejectCpsHistDaysUnitCount = _RejectCpsHistDaysUnitCount_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 18, 1, 3),
    _RejectCpsHistDaysUnitCount_Type()
)
rejectCpsHistDaysUnitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rejectCpsHistDaysUnitCount.setStatus("current")
_RejectCpsHistDaysTimestamp_Type = Unsigned32
_RejectCpsHistDaysTimestamp_Object = MibTableColumn
rejectCpsHistDaysTimestamp = _RejectCpsHistDaysTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 18, 1, 4),
    _RejectCpsHistDaysTimestamp_Type()
)
rejectCpsHistDaysTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rejectCpsHistDaysTimestamp.setStatus("current")
_AcceptCpsHistSecondsTable_Object = MibTable
acceptCpsHistSecondsTable = _AcceptCpsHistSecondsTable_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 19)
)
if mibBuilder.loadTexts:
    acceptCpsHistSecondsTable.setStatus("current")
_AcceptCpsHistSecondsEntry_Object = MibTableRow
acceptCpsHistSecondsEntry = _AcceptCpsHistSecondsEntry_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 19, 1)
)
acceptCpsHistSecondsEntry.setIndexNames(
    (0, "TPT-DDOS-MIB", "acceptCpsHistSecondsGlobalID"),
    (0, "TPT-DDOS-MIB", "acceptCpsHistSecondsIndex"),
)
if mibBuilder.loadTexts:
    acceptCpsHistSecondsEntry.setStatus("current")


class _AcceptCpsHistSecondsGlobalID_Type(OctetString):
    """Custom type acceptCpsHistSecondsGlobalID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_AcceptCpsHistSecondsGlobalID_Type.__name__ = "OctetString"
_AcceptCpsHistSecondsGlobalID_Object = MibTableColumn
acceptCpsHistSecondsGlobalID = _AcceptCpsHistSecondsGlobalID_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 19, 1, 1),
    _AcceptCpsHistSecondsGlobalID_Type()
)
acceptCpsHistSecondsGlobalID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acceptCpsHistSecondsGlobalID.setStatus("current")
_AcceptCpsHistSecondsIndex_Type = Unsigned32
_AcceptCpsHistSecondsIndex_Object = MibTableColumn
acceptCpsHistSecondsIndex = _AcceptCpsHistSecondsIndex_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 19, 1, 2),
    _AcceptCpsHistSecondsIndex_Type()
)
acceptCpsHistSecondsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acceptCpsHistSecondsIndex.setStatus("current")
_AcceptCpsHistSecondsUnitCount_Type = Counter64
_AcceptCpsHistSecondsUnitCount_Object = MibTableColumn
acceptCpsHistSecondsUnitCount = _AcceptCpsHistSecondsUnitCount_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 19, 1, 3),
    _AcceptCpsHistSecondsUnitCount_Type()
)
acceptCpsHistSecondsUnitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acceptCpsHistSecondsUnitCount.setStatus("current")
_AcceptCpsHistSecondsTimestamp_Type = Unsigned32
_AcceptCpsHistSecondsTimestamp_Object = MibTableColumn
acceptCpsHistSecondsTimestamp = _AcceptCpsHistSecondsTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 19, 1, 4),
    _AcceptCpsHistSecondsTimestamp_Type()
)
acceptCpsHistSecondsTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acceptCpsHistSecondsTimestamp.setStatus("current")
_AcceptCpsHistMinutesTable_Object = MibTable
acceptCpsHistMinutesTable = _AcceptCpsHistMinutesTable_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 20)
)
if mibBuilder.loadTexts:
    acceptCpsHistMinutesTable.setStatus("current")
_AcceptCpsHistMinutesEntry_Object = MibTableRow
acceptCpsHistMinutesEntry = _AcceptCpsHistMinutesEntry_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 20, 1)
)
acceptCpsHistMinutesEntry.setIndexNames(
    (0, "TPT-DDOS-MIB", "acceptCpsHistMinutesGlobalID"),
    (0, "TPT-DDOS-MIB", "acceptCpsHistMinutesIndex"),
)
if mibBuilder.loadTexts:
    acceptCpsHistMinutesEntry.setStatus("current")


class _AcceptCpsHistMinutesGlobalID_Type(OctetString):
    """Custom type acceptCpsHistMinutesGlobalID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_AcceptCpsHistMinutesGlobalID_Type.__name__ = "OctetString"
_AcceptCpsHistMinutesGlobalID_Object = MibTableColumn
acceptCpsHistMinutesGlobalID = _AcceptCpsHistMinutesGlobalID_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 20, 1, 1),
    _AcceptCpsHistMinutesGlobalID_Type()
)
acceptCpsHistMinutesGlobalID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acceptCpsHistMinutesGlobalID.setStatus("current")
_AcceptCpsHistMinutesIndex_Type = Unsigned32
_AcceptCpsHistMinutesIndex_Object = MibTableColumn
acceptCpsHistMinutesIndex = _AcceptCpsHistMinutesIndex_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 20, 1, 2),
    _AcceptCpsHistMinutesIndex_Type()
)
acceptCpsHistMinutesIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acceptCpsHistMinutesIndex.setStatus("current")
_AcceptCpsHistMinutesUnitCount_Type = Counter64
_AcceptCpsHistMinutesUnitCount_Object = MibTableColumn
acceptCpsHistMinutesUnitCount = _AcceptCpsHistMinutesUnitCount_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 20, 1, 3),
    _AcceptCpsHistMinutesUnitCount_Type()
)
acceptCpsHistMinutesUnitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acceptCpsHistMinutesUnitCount.setStatus("current")
_AcceptCpsHistMinutesTimestamp_Type = Unsigned32
_AcceptCpsHistMinutesTimestamp_Object = MibTableColumn
acceptCpsHistMinutesTimestamp = _AcceptCpsHistMinutesTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 20, 1, 4),
    _AcceptCpsHistMinutesTimestamp_Type()
)
acceptCpsHistMinutesTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acceptCpsHistMinutesTimestamp.setStatus("current")
_AcceptCpsHistHoursTable_Object = MibTable
acceptCpsHistHoursTable = _AcceptCpsHistHoursTable_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 21)
)
if mibBuilder.loadTexts:
    acceptCpsHistHoursTable.setStatus("current")
_AcceptCpsHistHoursEntry_Object = MibTableRow
acceptCpsHistHoursEntry = _AcceptCpsHistHoursEntry_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 21, 1)
)
acceptCpsHistHoursEntry.setIndexNames(
    (0, "TPT-DDOS-MIB", "acceptCpsHistHoursGlobalID"),
    (0, "TPT-DDOS-MIB", "acceptCpsHistHoursIndex"),
)
if mibBuilder.loadTexts:
    acceptCpsHistHoursEntry.setStatus("current")


class _AcceptCpsHistHoursGlobalID_Type(OctetString):
    """Custom type acceptCpsHistHoursGlobalID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_AcceptCpsHistHoursGlobalID_Type.__name__ = "OctetString"
_AcceptCpsHistHoursGlobalID_Object = MibTableColumn
acceptCpsHistHoursGlobalID = _AcceptCpsHistHoursGlobalID_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 21, 1, 1),
    _AcceptCpsHistHoursGlobalID_Type()
)
acceptCpsHistHoursGlobalID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acceptCpsHistHoursGlobalID.setStatus("current")
_AcceptCpsHistHoursIndex_Type = Unsigned32
_AcceptCpsHistHoursIndex_Object = MibTableColumn
acceptCpsHistHoursIndex = _AcceptCpsHistHoursIndex_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 21, 1, 2),
    _AcceptCpsHistHoursIndex_Type()
)
acceptCpsHistHoursIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acceptCpsHistHoursIndex.setStatus("current")
_AcceptCpsHistHoursUnitCount_Type = Counter64
_AcceptCpsHistHoursUnitCount_Object = MibTableColumn
acceptCpsHistHoursUnitCount = _AcceptCpsHistHoursUnitCount_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 21, 1, 3),
    _AcceptCpsHistHoursUnitCount_Type()
)
acceptCpsHistHoursUnitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acceptCpsHistHoursUnitCount.setStatus("current")
_AcceptCpsHistHoursTimestamp_Type = Unsigned32
_AcceptCpsHistHoursTimestamp_Object = MibTableColumn
acceptCpsHistHoursTimestamp = _AcceptCpsHistHoursTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 21, 1, 4),
    _AcceptCpsHistHoursTimestamp_Type()
)
acceptCpsHistHoursTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acceptCpsHistHoursTimestamp.setStatus("current")
_AcceptCpsHistDaysTable_Object = MibTable
acceptCpsHistDaysTable = _AcceptCpsHistDaysTable_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 22)
)
if mibBuilder.loadTexts:
    acceptCpsHistDaysTable.setStatus("current")
_AcceptCpsHistDaysEntry_Object = MibTableRow
acceptCpsHistDaysEntry = _AcceptCpsHistDaysEntry_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 22, 1)
)
acceptCpsHistDaysEntry.setIndexNames(
    (0, "TPT-DDOS-MIB", "acceptCpsHistDaysGlobalID"),
    (0, "TPT-DDOS-MIB", "acceptCpsHistDaysIndex"),
)
if mibBuilder.loadTexts:
    acceptCpsHistDaysEntry.setStatus("current")


class _AcceptCpsHistDaysGlobalID_Type(OctetString):
    """Custom type acceptCpsHistDaysGlobalID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_AcceptCpsHistDaysGlobalID_Type.__name__ = "OctetString"
_AcceptCpsHistDaysGlobalID_Object = MibTableColumn
acceptCpsHistDaysGlobalID = _AcceptCpsHistDaysGlobalID_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 22, 1, 1),
    _AcceptCpsHistDaysGlobalID_Type()
)
acceptCpsHistDaysGlobalID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acceptCpsHistDaysGlobalID.setStatus("current")
_AcceptCpsHistDaysIndex_Type = Unsigned32
_AcceptCpsHistDaysIndex_Object = MibTableColumn
acceptCpsHistDaysIndex = _AcceptCpsHistDaysIndex_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 22, 1, 2),
    _AcceptCpsHistDaysIndex_Type()
)
acceptCpsHistDaysIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acceptCpsHistDaysIndex.setStatus("current")
_AcceptCpsHistDaysUnitCount_Type = Counter64
_AcceptCpsHistDaysUnitCount_Object = MibTableColumn
acceptCpsHistDaysUnitCount = _AcceptCpsHistDaysUnitCount_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 22, 1, 3),
    _AcceptCpsHistDaysUnitCount_Type()
)
acceptCpsHistDaysUnitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acceptCpsHistDaysUnitCount.setStatus("current")
_AcceptCpsHistDaysTimestamp_Type = Unsigned32
_AcceptCpsHistDaysTimestamp_Object = MibTableColumn
acceptCpsHistDaysTimestamp = _AcceptCpsHistDaysTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 22, 1, 4),
    _AcceptCpsHistDaysTimestamp_Type()
)
acceptCpsHistDaysTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acceptCpsHistDaysTimestamp.setStatus("current")
_RejectEstHistSecondsTable_Object = MibTable
rejectEstHistSecondsTable = _RejectEstHistSecondsTable_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 25)
)
if mibBuilder.loadTexts:
    rejectEstHistSecondsTable.setStatus("current")
_RejectEstHistSecondsEntry_Object = MibTableRow
rejectEstHistSecondsEntry = _RejectEstHistSecondsEntry_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 25, 1)
)
rejectEstHistSecondsEntry.setIndexNames(
    (0, "TPT-DDOS-MIB", "rejectEstHistSecondsGlobalID"),
    (0, "TPT-DDOS-MIB", "rejectEstHistSecondsIndex"),
)
if mibBuilder.loadTexts:
    rejectEstHistSecondsEntry.setStatus("current")


class _RejectEstHistSecondsGlobalID_Type(OctetString):
    """Custom type rejectEstHistSecondsGlobalID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_RejectEstHistSecondsGlobalID_Type.__name__ = "OctetString"
_RejectEstHistSecondsGlobalID_Object = MibTableColumn
rejectEstHistSecondsGlobalID = _RejectEstHistSecondsGlobalID_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 25, 1, 1),
    _RejectEstHistSecondsGlobalID_Type()
)
rejectEstHistSecondsGlobalID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rejectEstHistSecondsGlobalID.setStatus("current")
_RejectEstHistSecondsIndex_Type = Unsigned32
_RejectEstHistSecondsIndex_Object = MibTableColumn
rejectEstHistSecondsIndex = _RejectEstHistSecondsIndex_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 25, 1, 2),
    _RejectEstHistSecondsIndex_Type()
)
rejectEstHistSecondsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rejectEstHistSecondsIndex.setStatus("current")
_RejectEstHistSecondsUnitCount_Type = Counter64
_RejectEstHistSecondsUnitCount_Object = MibTableColumn
rejectEstHistSecondsUnitCount = _RejectEstHistSecondsUnitCount_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 25, 1, 3),
    _RejectEstHistSecondsUnitCount_Type()
)
rejectEstHistSecondsUnitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rejectEstHistSecondsUnitCount.setStatus("current")
_RejectEstHistSecondsTimestamp_Type = Unsigned32
_RejectEstHistSecondsTimestamp_Object = MibTableColumn
rejectEstHistSecondsTimestamp = _RejectEstHistSecondsTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 25, 1, 4),
    _RejectEstHistSecondsTimestamp_Type()
)
rejectEstHistSecondsTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rejectEstHistSecondsTimestamp.setStatus("current")
_RejectEstHistMinutesTable_Object = MibTable
rejectEstHistMinutesTable = _RejectEstHistMinutesTable_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 26)
)
if mibBuilder.loadTexts:
    rejectEstHistMinutesTable.setStatus("current")
_RejectEstHistMinutesEntry_Object = MibTableRow
rejectEstHistMinutesEntry = _RejectEstHistMinutesEntry_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 26, 1)
)
rejectEstHistMinutesEntry.setIndexNames(
    (0, "TPT-DDOS-MIB", "rejectEstHistMinutesGlobalID"),
    (0, "TPT-DDOS-MIB", "rejectEstHistMinutesIndex"),
)
if mibBuilder.loadTexts:
    rejectEstHistMinutesEntry.setStatus("current")


class _RejectEstHistMinutesGlobalID_Type(OctetString):
    """Custom type rejectEstHistMinutesGlobalID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_RejectEstHistMinutesGlobalID_Type.__name__ = "OctetString"
_RejectEstHistMinutesGlobalID_Object = MibTableColumn
rejectEstHistMinutesGlobalID = _RejectEstHistMinutesGlobalID_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 26, 1, 1),
    _RejectEstHistMinutesGlobalID_Type()
)
rejectEstHistMinutesGlobalID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rejectEstHistMinutesGlobalID.setStatus("current")
_RejectEstHistMinutesIndex_Type = Unsigned32
_RejectEstHistMinutesIndex_Object = MibTableColumn
rejectEstHistMinutesIndex = _RejectEstHistMinutesIndex_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 26, 1, 2),
    _RejectEstHistMinutesIndex_Type()
)
rejectEstHistMinutesIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rejectEstHistMinutesIndex.setStatus("current")
_RejectEstHistMinutesUnitCount_Type = Counter64
_RejectEstHistMinutesUnitCount_Object = MibTableColumn
rejectEstHistMinutesUnitCount = _RejectEstHistMinutesUnitCount_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 26, 1, 3),
    _RejectEstHistMinutesUnitCount_Type()
)
rejectEstHistMinutesUnitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rejectEstHistMinutesUnitCount.setStatus("current")
_RejectEstHistMinutesTimestamp_Type = Unsigned32
_RejectEstHistMinutesTimestamp_Object = MibTableColumn
rejectEstHistMinutesTimestamp = _RejectEstHistMinutesTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 26, 1, 4),
    _RejectEstHistMinutesTimestamp_Type()
)
rejectEstHistMinutesTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rejectEstHistMinutesTimestamp.setStatus("current")
_RejectEstHistHoursTable_Object = MibTable
rejectEstHistHoursTable = _RejectEstHistHoursTable_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 27)
)
if mibBuilder.loadTexts:
    rejectEstHistHoursTable.setStatus("current")
_RejectEstHistHoursEntry_Object = MibTableRow
rejectEstHistHoursEntry = _RejectEstHistHoursEntry_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 27, 1)
)
rejectEstHistHoursEntry.setIndexNames(
    (0, "TPT-DDOS-MIB", "rejectEstHistHoursGlobalID"),
    (0, "TPT-DDOS-MIB", "rejectEstHistHoursIndex"),
)
if mibBuilder.loadTexts:
    rejectEstHistHoursEntry.setStatus("current")


class _RejectEstHistHoursGlobalID_Type(OctetString):
    """Custom type rejectEstHistHoursGlobalID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_RejectEstHistHoursGlobalID_Type.__name__ = "OctetString"
_RejectEstHistHoursGlobalID_Object = MibTableColumn
rejectEstHistHoursGlobalID = _RejectEstHistHoursGlobalID_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 27, 1, 1),
    _RejectEstHistHoursGlobalID_Type()
)
rejectEstHistHoursGlobalID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rejectEstHistHoursGlobalID.setStatus("current")
_RejectEstHistHoursIndex_Type = Unsigned32
_RejectEstHistHoursIndex_Object = MibTableColumn
rejectEstHistHoursIndex = _RejectEstHistHoursIndex_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 27, 1, 2),
    _RejectEstHistHoursIndex_Type()
)
rejectEstHistHoursIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rejectEstHistHoursIndex.setStatus("current")
_RejectEstHistHoursUnitCount_Type = Counter64
_RejectEstHistHoursUnitCount_Object = MibTableColumn
rejectEstHistHoursUnitCount = _RejectEstHistHoursUnitCount_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 27, 1, 3),
    _RejectEstHistHoursUnitCount_Type()
)
rejectEstHistHoursUnitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rejectEstHistHoursUnitCount.setStatus("current")
_RejectEstHistHoursTimestamp_Type = Unsigned32
_RejectEstHistHoursTimestamp_Object = MibTableColumn
rejectEstHistHoursTimestamp = _RejectEstHistHoursTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 27, 1, 4),
    _RejectEstHistHoursTimestamp_Type()
)
rejectEstHistHoursTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rejectEstHistHoursTimestamp.setStatus("current")
_RejectEstHistDaysTable_Object = MibTable
rejectEstHistDaysTable = _RejectEstHistDaysTable_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 28)
)
if mibBuilder.loadTexts:
    rejectEstHistDaysTable.setStatus("current")
_RejectEstHistDaysEntry_Object = MibTableRow
rejectEstHistDaysEntry = _RejectEstHistDaysEntry_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 28, 1)
)
rejectEstHistDaysEntry.setIndexNames(
    (0, "TPT-DDOS-MIB", "rejectEstHistDaysGlobalID"),
    (0, "TPT-DDOS-MIB", "rejectEstHistDaysIndex"),
)
if mibBuilder.loadTexts:
    rejectEstHistDaysEntry.setStatus("current")


class _RejectEstHistDaysGlobalID_Type(OctetString):
    """Custom type rejectEstHistDaysGlobalID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_RejectEstHistDaysGlobalID_Type.__name__ = "OctetString"
_RejectEstHistDaysGlobalID_Object = MibTableColumn
rejectEstHistDaysGlobalID = _RejectEstHistDaysGlobalID_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 28, 1, 1),
    _RejectEstHistDaysGlobalID_Type()
)
rejectEstHistDaysGlobalID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rejectEstHistDaysGlobalID.setStatus("current")
_RejectEstHistDaysIndex_Type = Unsigned32
_RejectEstHistDaysIndex_Object = MibTableColumn
rejectEstHistDaysIndex = _RejectEstHistDaysIndex_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 28, 1, 2),
    _RejectEstHistDaysIndex_Type()
)
rejectEstHistDaysIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rejectEstHistDaysIndex.setStatus("current")
_RejectEstHistDaysUnitCount_Type = Counter64
_RejectEstHistDaysUnitCount_Object = MibTableColumn
rejectEstHistDaysUnitCount = _RejectEstHistDaysUnitCount_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 28, 1, 3),
    _RejectEstHistDaysUnitCount_Type()
)
rejectEstHistDaysUnitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rejectEstHistDaysUnitCount.setStatus("current")
_RejectEstHistDaysTimestamp_Type = Unsigned32
_RejectEstHistDaysTimestamp_Object = MibTableColumn
rejectEstHistDaysTimestamp = _RejectEstHistDaysTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 28, 1, 4),
    _RejectEstHistDaysTimestamp_Type()
)
rejectEstHistDaysTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rejectEstHistDaysTimestamp.setStatus("current")
_AcceptEstHistSecondsTable_Object = MibTable
acceptEstHistSecondsTable = _AcceptEstHistSecondsTable_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 29)
)
if mibBuilder.loadTexts:
    acceptEstHistSecondsTable.setStatus("current")
_AcceptEstHistSecondsEntry_Object = MibTableRow
acceptEstHistSecondsEntry = _AcceptEstHistSecondsEntry_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 29, 1)
)
acceptEstHistSecondsEntry.setIndexNames(
    (0, "TPT-DDOS-MIB", "acceptEstHistSecondsGlobalID"),
    (0, "TPT-DDOS-MIB", "acceptEstHistSecondsIndex"),
)
if mibBuilder.loadTexts:
    acceptEstHistSecondsEntry.setStatus("current")


class _AcceptEstHistSecondsGlobalID_Type(OctetString):
    """Custom type acceptEstHistSecondsGlobalID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_AcceptEstHistSecondsGlobalID_Type.__name__ = "OctetString"
_AcceptEstHistSecondsGlobalID_Object = MibTableColumn
acceptEstHistSecondsGlobalID = _AcceptEstHistSecondsGlobalID_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 29, 1, 1),
    _AcceptEstHistSecondsGlobalID_Type()
)
acceptEstHistSecondsGlobalID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acceptEstHistSecondsGlobalID.setStatus("current")
_AcceptEstHistSecondsIndex_Type = Unsigned32
_AcceptEstHistSecondsIndex_Object = MibTableColumn
acceptEstHistSecondsIndex = _AcceptEstHistSecondsIndex_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 29, 1, 2),
    _AcceptEstHistSecondsIndex_Type()
)
acceptEstHistSecondsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acceptEstHistSecondsIndex.setStatus("current")
_AcceptEstHistSecondsUnitCount_Type = Counter64
_AcceptEstHistSecondsUnitCount_Object = MibTableColumn
acceptEstHistSecondsUnitCount = _AcceptEstHistSecondsUnitCount_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 29, 1, 3),
    _AcceptEstHistSecondsUnitCount_Type()
)
acceptEstHistSecondsUnitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acceptEstHistSecondsUnitCount.setStatus("current")
_AcceptEstHistSecondsTimestamp_Type = Unsigned32
_AcceptEstHistSecondsTimestamp_Object = MibTableColumn
acceptEstHistSecondsTimestamp = _AcceptEstHistSecondsTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 29, 1, 4),
    _AcceptEstHistSecondsTimestamp_Type()
)
acceptEstHistSecondsTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acceptEstHistSecondsTimestamp.setStatus("current")
_AcceptEstHistMinutesTable_Object = MibTable
acceptEstHistMinutesTable = _AcceptEstHistMinutesTable_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 30)
)
if mibBuilder.loadTexts:
    acceptEstHistMinutesTable.setStatus("current")
_AcceptEstHistMinutesEntry_Object = MibTableRow
acceptEstHistMinutesEntry = _AcceptEstHistMinutesEntry_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 30, 1)
)
acceptEstHistMinutesEntry.setIndexNames(
    (0, "TPT-DDOS-MIB", "acceptEstHistMinutesGlobalID"),
    (0, "TPT-DDOS-MIB", "acceptEstHistMinutesIndex"),
)
if mibBuilder.loadTexts:
    acceptEstHistMinutesEntry.setStatus("current")


class _AcceptEstHistMinutesGlobalID_Type(OctetString):
    """Custom type acceptEstHistMinutesGlobalID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_AcceptEstHistMinutesGlobalID_Type.__name__ = "OctetString"
_AcceptEstHistMinutesGlobalID_Object = MibTableColumn
acceptEstHistMinutesGlobalID = _AcceptEstHistMinutesGlobalID_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 30, 1, 1),
    _AcceptEstHistMinutesGlobalID_Type()
)
acceptEstHistMinutesGlobalID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acceptEstHistMinutesGlobalID.setStatus("current")
_AcceptEstHistMinutesIndex_Type = Unsigned32
_AcceptEstHistMinutesIndex_Object = MibTableColumn
acceptEstHistMinutesIndex = _AcceptEstHistMinutesIndex_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 30, 1, 2),
    _AcceptEstHistMinutesIndex_Type()
)
acceptEstHistMinutesIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acceptEstHistMinutesIndex.setStatus("current")
_AcceptEstHistMinutesUnitCount_Type = Counter64
_AcceptEstHistMinutesUnitCount_Object = MibTableColumn
acceptEstHistMinutesUnitCount = _AcceptEstHistMinutesUnitCount_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 30, 1, 3),
    _AcceptEstHistMinutesUnitCount_Type()
)
acceptEstHistMinutesUnitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acceptEstHistMinutesUnitCount.setStatus("current")
_AcceptEstHistMinutesTimestamp_Type = Unsigned32
_AcceptEstHistMinutesTimestamp_Object = MibTableColumn
acceptEstHistMinutesTimestamp = _AcceptEstHistMinutesTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 30, 1, 4),
    _AcceptEstHistMinutesTimestamp_Type()
)
acceptEstHistMinutesTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acceptEstHistMinutesTimestamp.setStatus("current")
_AcceptEstHistHoursTable_Object = MibTable
acceptEstHistHoursTable = _AcceptEstHistHoursTable_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 31)
)
if mibBuilder.loadTexts:
    acceptEstHistHoursTable.setStatus("current")
_AcceptEstHistHoursEntry_Object = MibTableRow
acceptEstHistHoursEntry = _AcceptEstHistHoursEntry_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 31, 1)
)
acceptEstHistHoursEntry.setIndexNames(
    (0, "TPT-DDOS-MIB", "acceptEstHistHoursGlobalID"),
    (0, "TPT-DDOS-MIB", "acceptEstHistHoursIndex"),
)
if mibBuilder.loadTexts:
    acceptEstHistHoursEntry.setStatus("current")


class _AcceptEstHistHoursGlobalID_Type(OctetString):
    """Custom type acceptEstHistHoursGlobalID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_AcceptEstHistHoursGlobalID_Type.__name__ = "OctetString"
_AcceptEstHistHoursGlobalID_Object = MibTableColumn
acceptEstHistHoursGlobalID = _AcceptEstHistHoursGlobalID_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 31, 1, 1),
    _AcceptEstHistHoursGlobalID_Type()
)
acceptEstHistHoursGlobalID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acceptEstHistHoursGlobalID.setStatus("current")
_AcceptEstHistHoursIndex_Type = Unsigned32
_AcceptEstHistHoursIndex_Object = MibTableColumn
acceptEstHistHoursIndex = _AcceptEstHistHoursIndex_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 31, 1, 2),
    _AcceptEstHistHoursIndex_Type()
)
acceptEstHistHoursIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acceptEstHistHoursIndex.setStatus("current")
_AcceptEstHistHoursUnitCount_Type = Counter64
_AcceptEstHistHoursUnitCount_Object = MibTableColumn
acceptEstHistHoursUnitCount = _AcceptEstHistHoursUnitCount_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 31, 1, 3),
    _AcceptEstHistHoursUnitCount_Type()
)
acceptEstHistHoursUnitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acceptEstHistHoursUnitCount.setStatus("current")
_AcceptEstHistHoursTimestamp_Type = Unsigned32
_AcceptEstHistHoursTimestamp_Object = MibTableColumn
acceptEstHistHoursTimestamp = _AcceptEstHistHoursTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 31, 1, 4),
    _AcceptEstHistHoursTimestamp_Type()
)
acceptEstHistHoursTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acceptEstHistHoursTimestamp.setStatus("current")
_AcceptEstHistDaysTable_Object = MibTable
acceptEstHistDaysTable = _AcceptEstHistDaysTable_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 32)
)
if mibBuilder.loadTexts:
    acceptEstHistDaysTable.setStatus("current")
_AcceptEstHistDaysEntry_Object = MibTableRow
acceptEstHistDaysEntry = _AcceptEstHistDaysEntry_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 32, 1)
)
acceptEstHistDaysEntry.setIndexNames(
    (0, "TPT-DDOS-MIB", "acceptEstHistDaysGlobalID"),
    (0, "TPT-DDOS-MIB", "acceptEstHistDaysIndex"),
)
if mibBuilder.loadTexts:
    acceptEstHistDaysEntry.setStatus("current")


class _AcceptEstHistDaysGlobalID_Type(OctetString):
    """Custom type acceptEstHistDaysGlobalID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_AcceptEstHistDaysGlobalID_Type.__name__ = "OctetString"
_AcceptEstHistDaysGlobalID_Object = MibTableColumn
acceptEstHistDaysGlobalID = _AcceptEstHistDaysGlobalID_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 32, 1, 1),
    _AcceptEstHistDaysGlobalID_Type()
)
acceptEstHistDaysGlobalID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acceptEstHistDaysGlobalID.setStatus("current")
_AcceptEstHistDaysIndex_Type = Unsigned32
_AcceptEstHistDaysIndex_Object = MibTableColumn
acceptEstHistDaysIndex = _AcceptEstHistDaysIndex_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 32, 1, 2),
    _AcceptEstHistDaysIndex_Type()
)
acceptEstHistDaysIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acceptEstHistDaysIndex.setStatus("current")
_AcceptEstHistDaysUnitCount_Type = Counter64
_AcceptEstHistDaysUnitCount_Object = MibTableColumn
acceptEstHistDaysUnitCount = _AcceptEstHistDaysUnitCount_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 32, 1, 3),
    _AcceptEstHistDaysUnitCount_Type()
)
acceptEstHistDaysUnitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acceptEstHistDaysUnitCount.setStatus("current")
_AcceptEstHistDaysTimestamp_Type = Unsigned32
_AcceptEstHistDaysTimestamp_Object = MibTableColumn
acceptEstHistDaysTimestamp = _AcceptEstHistDaysTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 9, 32, 1, 4),
    _AcceptEstHistDaysTimestamp_Type()
)
acceptEstHistDaysTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acceptEstHistDaysTimestamp.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPT-DDOS-MIB",
    **{"tpt-ddos": tpt_ddos,
       "rejectSynHistSecondsTable": rejectSynHistSecondsTable,
       "rejectSynHistSecondsEntry": rejectSynHistSecondsEntry,
       "rejectSynHistSecondsGlobalID": rejectSynHistSecondsGlobalID,
       "rejectSynHistSecondsIndex": rejectSynHistSecondsIndex,
       "rejectSynHistSecondsUnitCount": rejectSynHistSecondsUnitCount,
       "rejectSynHistSecondsTimestamp": rejectSynHistSecondsTimestamp,
       "rejectSynHistMinutesTable": rejectSynHistMinutesTable,
       "rejectSynHistMinutesEntry": rejectSynHistMinutesEntry,
       "rejectSynHistMinutesGlobalID": rejectSynHistMinutesGlobalID,
       "rejectSynHistMinutesIndex": rejectSynHistMinutesIndex,
       "rejectSynHistMinutesUnitCount": rejectSynHistMinutesUnitCount,
       "rejectSynHistMinutesTimestamp": rejectSynHistMinutesTimestamp,
       "rejectSynHistHoursTable": rejectSynHistHoursTable,
       "rejectSynHistHoursEntry": rejectSynHistHoursEntry,
       "rejectSynHistHoursGlobalID": rejectSynHistHoursGlobalID,
       "rejectSynHistHoursIndex": rejectSynHistHoursIndex,
       "rejectSynHistHoursUnitCount": rejectSynHistHoursUnitCount,
       "rejectSynHistHoursTimestamp": rejectSynHistHoursTimestamp,
       "rejectSynHistDaysTable": rejectSynHistDaysTable,
       "rejectSynHistDaysEntry": rejectSynHistDaysEntry,
       "rejectSynHistDaysGlobalID": rejectSynHistDaysGlobalID,
       "rejectSynHistDaysIndex": rejectSynHistDaysIndex,
       "rejectSynHistDaysUnitCount": rejectSynHistDaysUnitCount,
       "rejectSynHistDaysTimestamp": rejectSynHistDaysTimestamp,
       "proxyConnHistSecondsTable": proxyConnHistSecondsTable,
       "proxyConnHistSecondsEntry": proxyConnHistSecondsEntry,
       "proxyConnHistSecondsGlobalID": proxyConnHistSecondsGlobalID,
       "proxyConnHistSecondsIndex": proxyConnHistSecondsIndex,
       "proxyConnHistSecondsUnitCount": proxyConnHistSecondsUnitCount,
       "proxyConnHistSecondsTimestamp": proxyConnHistSecondsTimestamp,
       "proxyConnHistMinutesTable": proxyConnHistMinutesTable,
       "proxyConnHistMinutesEntry": proxyConnHistMinutesEntry,
       "proxyConnHistMinutesGlobalID": proxyConnHistMinutesGlobalID,
       "proxyConnHistMinutesIndex": proxyConnHistMinutesIndex,
       "proxyConnHistMinutesUnitCount": proxyConnHistMinutesUnitCount,
       "proxyConnHistMinutesTimestamp": proxyConnHistMinutesTimestamp,
       "proxyConnHistHoursTable": proxyConnHistHoursTable,
       "proxyConnHistHoursEntry": proxyConnHistHoursEntry,
       "proxyConnHistHoursGlobalID": proxyConnHistHoursGlobalID,
       "proxyConnHistHoursIndex": proxyConnHistHoursIndex,
       "proxyConnHistHoursUnitCount": proxyConnHistHoursUnitCount,
       "proxyConnHistHoursTimestamp": proxyConnHistHoursTimestamp,
       "proxyConnHistDaysTable": proxyConnHistDaysTable,
       "proxyConnHistDaysEntry": proxyConnHistDaysEntry,
       "proxyConnHistDaysGlobalID": proxyConnHistDaysGlobalID,
       "proxyConnHistDaysIndex": proxyConnHistDaysIndex,
       "proxyConnHistDaysUnitCount": proxyConnHistDaysUnitCount,
       "proxyConnHistDaysTimestamp": proxyConnHistDaysTimestamp,
       "rejectCpsHistSecondsTable": rejectCpsHistSecondsTable,
       "rejectCpsHistSecondsEntry": rejectCpsHistSecondsEntry,
       "rejectCpsHistSecondsGlobalID": rejectCpsHistSecondsGlobalID,
       "rejectCpsHistSecondsIndex": rejectCpsHistSecondsIndex,
       "rejectCpsHistSecondsUnitCount": rejectCpsHistSecondsUnitCount,
       "rejectCpsHistSecondsTimestamp": rejectCpsHistSecondsTimestamp,
       "rejectCpsHistMinutesTable": rejectCpsHistMinutesTable,
       "rejectCpsHistMinutesEntry": rejectCpsHistMinutesEntry,
       "rejectCpsHistMinutesGlobalID": rejectCpsHistMinutesGlobalID,
       "rejectCpsHistMinutesIndex": rejectCpsHistMinutesIndex,
       "rejectCpsHistMinutesUnitCount": rejectCpsHistMinutesUnitCount,
       "rejectCpsHistMinutesTimestamp": rejectCpsHistMinutesTimestamp,
       "rejectCpsHistHoursTable": rejectCpsHistHoursTable,
       "rejectCpsHistHoursEntry": rejectCpsHistHoursEntry,
       "rejectCpsHistHoursGlobalID": rejectCpsHistHoursGlobalID,
       "rejectCpsHistHoursIndex": rejectCpsHistHoursIndex,
       "rejectCpsHistHoursUnitCount": rejectCpsHistHoursUnitCount,
       "rejectCpsHistHoursTimestamp": rejectCpsHistHoursTimestamp,
       "rejectCpsHistDaysTable": rejectCpsHistDaysTable,
       "rejectCpsHistDaysEntry": rejectCpsHistDaysEntry,
       "rejectCpsHistDaysGlobalID": rejectCpsHistDaysGlobalID,
       "rejectCpsHistDaysIndex": rejectCpsHistDaysIndex,
       "rejectCpsHistDaysUnitCount": rejectCpsHistDaysUnitCount,
       "rejectCpsHistDaysTimestamp": rejectCpsHistDaysTimestamp,
       "acceptCpsHistSecondsTable": acceptCpsHistSecondsTable,
       "acceptCpsHistSecondsEntry": acceptCpsHistSecondsEntry,
       "acceptCpsHistSecondsGlobalID": acceptCpsHistSecondsGlobalID,
       "acceptCpsHistSecondsIndex": acceptCpsHistSecondsIndex,
       "acceptCpsHistSecondsUnitCount": acceptCpsHistSecondsUnitCount,
       "acceptCpsHistSecondsTimestamp": acceptCpsHistSecondsTimestamp,
       "acceptCpsHistMinutesTable": acceptCpsHistMinutesTable,
       "acceptCpsHistMinutesEntry": acceptCpsHistMinutesEntry,
       "acceptCpsHistMinutesGlobalID": acceptCpsHistMinutesGlobalID,
       "acceptCpsHistMinutesIndex": acceptCpsHistMinutesIndex,
       "acceptCpsHistMinutesUnitCount": acceptCpsHistMinutesUnitCount,
       "acceptCpsHistMinutesTimestamp": acceptCpsHistMinutesTimestamp,
       "acceptCpsHistHoursTable": acceptCpsHistHoursTable,
       "acceptCpsHistHoursEntry": acceptCpsHistHoursEntry,
       "acceptCpsHistHoursGlobalID": acceptCpsHistHoursGlobalID,
       "acceptCpsHistHoursIndex": acceptCpsHistHoursIndex,
       "acceptCpsHistHoursUnitCount": acceptCpsHistHoursUnitCount,
       "acceptCpsHistHoursTimestamp": acceptCpsHistHoursTimestamp,
       "acceptCpsHistDaysTable": acceptCpsHistDaysTable,
       "acceptCpsHistDaysEntry": acceptCpsHistDaysEntry,
       "acceptCpsHistDaysGlobalID": acceptCpsHistDaysGlobalID,
       "acceptCpsHistDaysIndex": acceptCpsHistDaysIndex,
       "acceptCpsHistDaysUnitCount": acceptCpsHistDaysUnitCount,
       "acceptCpsHistDaysTimestamp": acceptCpsHistDaysTimestamp,
       "rejectEstHistSecondsTable": rejectEstHistSecondsTable,
       "rejectEstHistSecondsEntry": rejectEstHistSecondsEntry,
       "rejectEstHistSecondsGlobalID": rejectEstHistSecondsGlobalID,
       "rejectEstHistSecondsIndex": rejectEstHistSecondsIndex,
       "rejectEstHistSecondsUnitCount": rejectEstHistSecondsUnitCount,
       "rejectEstHistSecondsTimestamp": rejectEstHistSecondsTimestamp,
       "rejectEstHistMinutesTable": rejectEstHistMinutesTable,
       "rejectEstHistMinutesEntry": rejectEstHistMinutesEntry,
       "rejectEstHistMinutesGlobalID": rejectEstHistMinutesGlobalID,
       "rejectEstHistMinutesIndex": rejectEstHistMinutesIndex,
       "rejectEstHistMinutesUnitCount": rejectEstHistMinutesUnitCount,
       "rejectEstHistMinutesTimestamp": rejectEstHistMinutesTimestamp,
       "rejectEstHistHoursTable": rejectEstHistHoursTable,
       "rejectEstHistHoursEntry": rejectEstHistHoursEntry,
       "rejectEstHistHoursGlobalID": rejectEstHistHoursGlobalID,
       "rejectEstHistHoursIndex": rejectEstHistHoursIndex,
       "rejectEstHistHoursUnitCount": rejectEstHistHoursUnitCount,
       "rejectEstHistHoursTimestamp": rejectEstHistHoursTimestamp,
       "rejectEstHistDaysTable": rejectEstHistDaysTable,
       "rejectEstHistDaysEntry": rejectEstHistDaysEntry,
       "rejectEstHistDaysGlobalID": rejectEstHistDaysGlobalID,
       "rejectEstHistDaysIndex": rejectEstHistDaysIndex,
       "rejectEstHistDaysUnitCount": rejectEstHistDaysUnitCount,
       "rejectEstHistDaysTimestamp": rejectEstHistDaysTimestamp,
       "acceptEstHistSecondsTable": acceptEstHistSecondsTable,
       "acceptEstHistSecondsEntry": acceptEstHistSecondsEntry,
       "acceptEstHistSecondsGlobalID": acceptEstHistSecondsGlobalID,
       "acceptEstHistSecondsIndex": acceptEstHistSecondsIndex,
       "acceptEstHistSecondsUnitCount": acceptEstHistSecondsUnitCount,
       "acceptEstHistSecondsTimestamp": acceptEstHistSecondsTimestamp,
       "acceptEstHistMinutesTable": acceptEstHistMinutesTable,
       "acceptEstHistMinutesEntry": acceptEstHistMinutesEntry,
       "acceptEstHistMinutesGlobalID": acceptEstHistMinutesGlobalID,
       "acceptEstHistMinutesIndex": acceptEstHistMinutesIndex,
       "acceptEstHistMinutesUnitCount": acceptEstHistMinutesUnitCount,
       "acceptEstHistMinutesTimestamp": acceptEstHistMinutesTimestamp,
       "acceptEstHistHoursTable": acceptEstHistHoursTable,
       "acceptEstHistHoursEntry": acceptEstHistHoursEntry,
       "acceptEstHistHoursGlobalID": acceptEstHistHoursGlobalID,
       "acceptEstHistHoursIndex": acceptEstHistHoursIndex,
       "acceptEstHistHoursUnitCount": acceptEstHistHoursUnitCount,
       "acceptEstHistHoursTimestamp": acceptEstHistHoursTimestamp,
       "acceptEstHistDaysTable": acceptEstHistDaysTable,
       "acceptEstHistDaysEntry": acceptEstHistDaysEntry,
       "acceptEstHistDaysGlobalID": acceptEstHistDaysGlobalID,
       "acceptEstHistDaysIndex": acceptEstHistDaysIndex,
       "acceptEstHistDaysUnitCount": acceptEstHistDaysUnitCount,
       "acceptEstHistDaysTimestamp": acceptEstHistDaysTimestamp}
)
