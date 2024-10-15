# SNMP MIB module (EVENTLOG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EVENTLOG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:41:00 2024
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

(eventlog,) = mibBuilder.importSymbols(
    "CORIOLIS-MIB",
    "eventlog")

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

eventlogMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5812, 9, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EventlogTable_Object = MibTable
eventlogTable = _EventlogTable_Object(
    (1, 3, 6, 1, 4, 1, 5812, 9, 2)
)
if mibBuilder.loadTexts:
    eventlogTable.setStatus("current")
_EventlogEntry_Object = MibTableRow
eventlogEntry = _EventlogEntry_Object(
    (1, 3, 6, 1, 4, 1, 5812, 9, 2, 1)
)
eventlogEntry.setIndexNames(
    (0, "EVENTLOG-MIB", "eventlogEventID"),
)
if mibBuilder.loadTexts:
    eventlogEntry.setStatus("current")
_EventlogName_Type = OctetString
_EventlogName_Object = MibTableColumn
eventlogName = _EventlogName_Object(
    (1, 3, 6, 1, 4, 1, 5812, 9, 2, 1, 1),
    _EventlogName_Type()
)
eventlogName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventlogName.setStatus("current")
_EventlogDesc_Type = OctetString
_EventlogDesc_Object = MibTableColumn
eventlogDesc = _EventlogDesc_Object(
    (1, 3, 6, 1, 4, 1, 5812, 9, 2, 1, 2),
    _EventlogDesc_Type()
)
eventlogDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventlogDesc.setStatus("current")
_EventlogSeverity_Type = OctetString
_EventlogSeverity_Object = MibTableColumn
eventlogSeverity = _EventlogSeverity_Object(
    (1, 3, 6, 1, 4, 1, 5812, 9, 2, 1, 3),
    _EventlogSeverity_Type()
)
eventlogSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventlogSeverity.setStatus("current")
_EventlogTime_Type = OctetString
_EventlogTime_Object = MibTableColumn
eventlogTime = _EventlogTime_Object(
    (1, 3, 6, 1, 4, 1, 5812, 9, 2, 1, 4),
    _EventlogTime_Type()
)
eventlogTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventlogTime.setStatus("current")
_EventlogSrcIpAddr_Type = IpAddress
_EventlogSrcIpAddr_Object = MibTableColumn
eventlogSrcIpAddr = _EventlogSrcIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 5812, 9, 2, 1, 5),
    _EventlogSrcIpAddr_Type()
)
eventlogSrcIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventlogSrcIpAddr.setStatus("current")
_EventlogCorEventIpAddr_Type = IpAddress
_EventlogCorEventIpAddr_Object = MibTableColumn
eventlogCorEventIpAddr = _EventlogCorEventIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 5812, 9, 2, 1, 6),
    _EventlogCorEventIpAddr_Type()
)
eventlogCorEventIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventlogCorEventIpAddr.setStatus("current")
_EventlogEventID_Type = Integer32
_EventlogEventID_Object = MibTableColumn
eventlogEventID = _EventlogEventID_Object(
    (1, 3, 6, 1, 4, 1, 5812, 9, 2, 1, 7),
    _EventlogEventID_Type()
)
eventlogEventID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventlogEventID.setStatus("current")
_EventlogCorEventID_Type = Integer32
_EventlogCorEventID_Object = MibTableColumn
eventlogCorEventID = _EventlogCorEventID_Object(
    (1, 3, 6, 1, 4, 1, 5812, 9, 2, 1, 8),
    _EventlogCorEventID_Type()
)
eventlogCorEventID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventlogCorEventID.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EVENTLOG-MIB",
    **{"eventlogMIB": eventlogMIB,
       "eventlogTable": eventlogTable,
       "eventlogEntry": eventlogEntry,
       "eventlogName": eventlogName,
       "eventlogDesc": eventlogDesc,
       "eventlogSeverity": eventlogSeverity,
       "eventlogTime": eventlogTime,
       "eventlogSrcIpAddr": eventlogSrcIpAddr,
       "eventlogCorEventIpAddr": eventlogCorEventIpAddr,
       "eventlogEventID": eventlogEventID,
       "eventlogCorEventID": eventlogCorEventID}
)
