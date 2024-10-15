# SNMP MIB module (MERU-SYSLOG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MERU-SYSLOG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:21:14 2024
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

(Ipv6Address,) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address")

(mwDiagnostics,) = mibBuilder.importSymbols(
    "MERU-SMI",
    "mwDiagnostics")

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
 enterprises,
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
    "enterprises",
    "iso")

(DateAndTime,
 DisplayString,
 MacAddress,
 RowStatus,
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

mwSyslog = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 5, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MwSyslogTable_Object = MibTable
mwSyslogTable = _MwSyslogTable_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 5, 2, 1)
)
if mibBuilder.loadTexts:
    mwSyslogTable.setStatus("current")
_MwSyslogEntry_Object = MibTableRow
mwSyslogEntry = _MwSyslogEntry_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 5, 2, 1, 1)
)
mwSyslogEntry.setIndexNames(
    (0, "MERU-SYSLOG-MIB", "mwSyslogTableIndex"),
)
if mibBuilder.loadTexts:
    mwSyslogEntry.setStatus("current")
_MwSyslogTableIndex_Type = Integer32
_MwSyslogTableIndex_Object = MibTableColumn
mwSyslogTableIndex = _MwSyslogTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 5, 2, 1, 1, 1),
    _MwSyslogTableIndex_Type()
)
mwSyslogTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwSyslogTableIndex.setStatus("current")
_MwSysloglinenb_Type = Unsigned32
_MwSysloglinenb_Object = MibTableColumn
mwSysloglinenb = _MwSysloglinenb_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 5, 2, 1, 1, 2),
    _MwSysloglinenb_Type()
)
mwSysloglinenb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwSysloglinenb.setStatus("current")
_MwSyslogrecord_Type = DisplayString
_MwSyslogrecord_Object = MibTableColumn
mwSyslogrecord = _MwSyslogrecord_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 5, 2, 1, 1, 3),
    _MwSyslogrecord_Type()
)
mwSyslogrecord.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwSyslogrecord.setStatus("current")
_MwSyslogpriority_Type = DisplayString
_MwSyslogpriority_Object = MibTableColumn
mwSyslogpriority = _MwSyslogpriority_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 5, 2, 1, 1, 4),
    _MwSyslogpriority_Type()
)
mwSyslogpriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwSyslogpriority.setStatus("current")
_MwSyslogmnemonic_Type = DisplayString
_MwSyslogmnemonic_Object = MibTableColumn
mwSyslogmnemonic = _MwSyslogmnemonic_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 5, 2, 1, 1, 5),
    _MwSyslogmnemonic_Type()
)
mwSyslogmnemonic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwSyslogmnemonic.setStatus("current")
_MwSyslogtimestamp_Type = DateAndTime
_MwSyslogtimestamp_Object = MibTableColumn
mwSyslogtimestamp = _MwSyslogtimestamp_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 5, 2, 1, 1, 6),
    _MwSyslogtimestamp_Type()
)
mwSyslogtimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwSyslogtimestamp.setStatus("current")
_MwLogTransferTable_Object = MibTable
mwLogTransferTable = _MwLogTransferTable_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 5, 2, 2)
)
if mibBuilder.loadTexts:
    mwLogTransferTable.setStatus("current")
_MwLogTransferEntry_Object = MibTableRow
mwLogTransferEntry = _MwLogTransferEntry_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 5, 2, 2, 1)
)
mwLogTransferEntry.setIndexNames(
    (0, "MERU-SYSLOG-MIB", "mwLogTransferTableIndex"),
)
if mibBuilder.loadTexts:
    mwLogTransferEntry.setStatus("current")
_MwLogTransferTableIndex_Type = Integer32
_MwLogTransferTableIndex_Object = MibTableColumn
mwLogTransferTableIndex = _MwLogTransferTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 5, 2, 2, 1, 1),
    _MwLogTransferTableIndex_Type()
)
mwLogTransferTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwLogTransferTableIndex.setStatus("current")
_MwLogTransfersize_Type = Unsigned32
_MwLogTransfersize_Object = MibTableColumn
mwLogTransfersize = _MwLogTransfersize_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 5, 2, 2, 1, 2),
    _MwLogTransfersize_Type()
)
mwLogTransfersize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwLogTransfersize.setStatus("current")
_MwLogTransfernblines_Type = Unsigned32
_MwLogTransfernblines_Object = MibTableColumn
mwLogTransfernblines = _MwLogTransfernblines_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 5, 2, 2, 1, 3),
    _MwLogTransfernblines_Type()
)
mwLogTransfernblines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwLogTransfernblines.setStatus("current")
_MwLogTransferlastaccess_Type = DateAndTime
_MwLogTransferlastaccess_Object = MibTableColumn
mwLogTransferlastaccess = _MwLogTransferlastaccess_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 5, 2, 2, 1, 4),
    _MwLogTransferlastaccess_Type()
)
mwLogTransferlastaccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwLogTransferlastaccess.setStatus("current")
_MwLogTransferlastrecord_Type = DisplayString
_MwLogTransferlastrecord_Object = MibTableColumn
mwLogTransferlastrecord = _MwLogTransferlastrecord_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 5, 2, 2, 1, 5),
    _MwLogTransferlastrecord_Type()
)
mwLogTransferlastrecord.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwLogTransferlastrecord.setStatus("current")
_MwLogTransferdescription_Type = DisplayString
_MwLogTransferdescription_Object = MibTableColumn
mwLogTransferdescription = _MwLogTransferdescription_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 5, 2, 2, 1, 6),
    _MwLogTransferdescription_Type()
)
mwLogTransferdescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwLogTransferdescription.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MERU-SYSLOG-MIB",
    **{"mwSyslog": mwSyslog,
       "mwSyslogTable": mwSyslogTable,
       "mwSyslogEntry": mwSyslogEntry,
       "mwSyslogTableIndex": mwSyslogTableIndex,
       "mwSysloglinenb": mwSysloglinenb,
       "mwSyslogrecord": mwSyslogrecord,
       "mwSyslogpriority": mwSyslogpriority,
       "mwSyslogmnemonic": mwSyslogmnemonic,
       "mwSyslogtimestamp": mwSyslogtimestamp,
       "mwLogTransferTable": mwLogTransferTable,
       "mwLogTransferEntry": mwLogTransferEntry,
       "mwLogTransferTableIndex": mwLogTransferTableIndex,
       "mwLogTransfersize": mwLogTransfersize,
       "mwLogTransfernblines": mwLogTransfernblines,
       "mwLogTransferlastaccess": mwLogTransferlastaccess,
       "mwLogTransferlastrecord": mwLogTransferlastrecord,
       "mwLogTransferdescription": mwLogTransferdescription}
)
