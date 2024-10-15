# SNMP MIB module (NETASQ-HOSTS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NETASQ-HOSTS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:25:31 2024
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

(ntqHosts,) = mibBuilder.importSymbols(
    "NETASQ-SMI-MIB",
    "ntqHosts")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NtqHostsTable_Object = MibTable
ntqHostsTable = _NtqHostsTable_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 3, 1)
)
if mibBuilder.loadTexts:
    ntqHostsTable.setStatus("current")
_NtqHostsEntry_Object = MibTableRow
ntqHostsEntry = _NtqHostsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 3, 1, 1)
)
ntqHostsEntry.setIndexNames(
    (0, "NETASQ-HOSTS-MIB", "ntqHostIPAddr"),
)
if mibBuilder.loadTexts:
    ntqHostsEntry.setStatus("current")
_NtqHostIPAddr_Type = DisplayString
_NtqHostIPAddr_Object = MibTableColumn
ntqHostIPAddr = _NtqHostIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 3, 1, 1, 1),
    _NtqHostIPAddr_Type()
)
ntqHostIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntqHostIPAddr.setStatus("current")
_NtqHostName_Type = SnmpAdminString
_NtqHostName_Object = MibTableColumn
ntqHostName = _NtqHostName_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 3, 1, 1, 2),
    _NtqHostName_Type()
)
ntqHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntqHostName.setStatus("current")
_NtqInterface_Type = DisplayString
_NtqInterface_Object = MibTableColumn
ntqInterface = _NtqInterface_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 3, 1, 1, 3),
    _NtqInterface_Type()
)
ntqInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntqInterface.setStatus("current")
_NtqPackets_Type = Counter64
_NtqPackets_Object = MibTableColumn
ntqPackets = _NtqPackets_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 3, 1, 1, 4),
    _NtqPackets_Type()
)
ntqPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntqPackets.setStatus("current")
_NtqBytes_Type = Counter64
_NtqBytes_Object = MibTableColumn
ntqBytes = _NtqBytes_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 3, 1, 1, 5),
    _NtqBytes_Type()
)
ntqBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntqBytes.setStatus("current")
_NtqConn_Type = Counter64
_NtqConn_Object = MibTableColumn
ntqConn = _NtqConn_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 3, 1, 1, 6),
    _NtqConn_Type()
)
ntqConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntqConn.setStatus("current")
_NtqCurThroughput_Type = Integer32
_NtqCurThroughput_Object = MibTableColumn
ntqCurThroughput = _NtqCurThroughput_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 3, 1, 1, 7),
    _NtqCurThroughput_Type()
)
ntqCurThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntqCurThroughput.setStatus("current")
_NtqMaxThroughput_Type = Integer32
_NtqMaxThroughput_Object = MibTableColumn
ntqMaxThroughput = _NtqMaxThroughput_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 3, 1, 1, 8),
    _NtqMaxThroughput_Type()
)
ntqMaxThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntqMaxThroughput.setStatus("current")
_NtqInBytes_Type = Counter64
_NtqInBytes_Object = MibTableColumn
ntqInBytes = _NtqInBytes_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 3, 1, 1, 9),
    _NtqInBytes_Type()
)
ntqInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntqInBytes.setStatus("current")
_NtqOutBytes_Type = Counter64
_NtqOutBytes_Object = MibTableColumn
ntqOutBytes = _NtqOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 3, 1, 1, 10),
    _NtqOutBytes_Type()
)
ntqOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntqOutBytes.setStatus("current")
_NtqInCurThroughput_Type = Integer32
_NtqInCurThroughput_Object = MibTableColumn
ntqInCurThroughput = _NtqInCurThroughput_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 3, 1, 1, 11),
    _NtqInCurThroughput_Type()
)
ntqInCurThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntqInCurThroughput.setStatus("current")
_NtqOutCurThroughput_Type = Integer32
_NtqOutCurThroughput_Object = MibTableColumn
ntqOutCurThroughput = _NtqOutCurThroughput_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 3, 1, 1, 12),
    _NtqOutCurThroughput_Type()
)
ntqOutCurThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntqOutCurThroughput.setStatus("current")
_NtqInMaxThroughput_Type = Integer32
_NtqInMaxThroughput_Object = MibScalar
ntqInMaxThroughput = _NtqInMaxThroughput_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 3, 1, 1, 13),
    _NtqInMaxThroughput_Type()
)
ntqInMaxThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntqInMaxThroughput.setStatus("current")
_NtqOutMaxThroughput_Type = Integer32
_NtqOutMaxThroughput_Object = MibScalar
ntqOutMaxThroughput = _NtqOutMaxThroughput_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 3, 1, 1, 14),
    _NtqOutMaxThroughput_Type()
)
ntqOutMaxThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntqOutMaxThroughput.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NETASQ-HOSTS-MIB",
    **{"ntqHostsTable": ntqHostsTable,
       "ntqHostsEntry": ntqHostsEntry,
       "ntqHostIPAddr": ntqHostIPAddr,
       "ntqHostName": ntqHostName,
       "ntqInterface": ntqInterface,
       "ntqPackets": ntqPackets,
       "ntqBytes": ntqBytes,
       "ntqConn": ntqConn,
       "ntqCurThroughput": ntqCurThroughput,
       "ntqMaxThroughput": ntqMaxThroughput,
       "ntqInBytes": ntqInBytes,
       "ntqOutBytes": ntqOutBytes,
       "ntqInCurThroughput": ntqInCurThroughput,
       "ntqOutCurThroughput": ntqOutCurThroughput,
       "ntqInMaxThroughput": ntqInMaxThroughput,
       "ntqOutMaxThroughput": ntqOutMaxThroughput}
)
