# SNMP MIB module (INTEL-HDLC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/INTEL-HDLC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:09:45 2024
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

(mib2ext,) = mibBuilder.importSymbols(
    "INTEL-GEN-MIB",
    "mib2ext")

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

_Hdlc_ObjectIdentity = ObjectIdentity
hdlc = _Hdlc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 30)
)
_HdlcMonitor_ObjectIdentity = ObjectIdentity
hdlcMonitor = _HdlcMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 30, 1)
)
_HdlcMonitorTable_Object = MibTable
hdlcMonitorTable = _HdlcMonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 30, 1, 1)
)
if mibBuilder.loadTexts:
    hdlcMonitorTable.setStatus("mandatory")
_HdlcMonitorEntry_Object = MibTableRow
hdlcMonitorEntry = _HdlcMonitorEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 30, 1, 1, 1)
)
hdlcMonitorEntry.setIndexNames(
    (0, "INTEL-HDLC-MIB", "hdlcMonitorIndex"),
)
if mibBuilder.loadTexts:
    hdlcMonitorEntry.setStatus("mandatory")
_HdlcMonitorIndex_Type = Integer32
_HdlcMonitorIndex_Object = MibTableColumn
hdlcMonitorIndex = _HdlcMonitorIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 30, 1, 1, 1, 1),
    _HdlcMonitorIndex_Type()
)
hdlcMonitorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdlcMonitorIndex.setStatus("mandatory")
_HdlcMonitorReceiverChecksumErrors_Type = Integer32
_HdlcMonitorReceiverChecksumErrors_Object = MibTableColumn
hdlcMonitorReceiverChecksumErrors = _HdlcMonitorReceiverChecksumErrors_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 30, 1, 1, 1, 2),
    _HdlcMonitorReceiverChecksumErrors_Type()
)
hdlcMonitorReceiverChecksumErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdlcMonitorReceiverChecksumErrors.setStatus("mandatory")
_HdlcMonitorReceiverGiants_Type = Integer32
_HdlcMonitorReceiverGiants_Object = MibTableColumn
hdlcMonitorReceiverGiants = _HdlcMonitorReceiverGiants_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 30, 1, 1, 1, 3),
    _HdlcMonitorReceiverGiants_Type()
)
hdlcMonitorReceiverGiants.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdlcMonitorReceiverGiants.setStatus("mandatory")
_HdlcMonitorReceiverDwarves_Type = Integer32
_HdlcMonitorReceiverDwarves_Object = MibTableColumn
hdlcMonitorReceiverDwarves = _HdlcMonitorReceiverDwarves_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 30, 1, 1, 1, 4),
    _HdlcMonitorReceiverDwarves_Type()
)
hdlcMonitorReceiverDwarves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdlcMonitorReceiverDwarves.setStatus("mandatory")
_HdlcMonitorReceiverAborts_Type = Integer32
_HdlcMonitorReceiverAborts_Object = MibTableColumn
hdlcMonitorReceiverAborts = _HdlcMonitorReceiverAborts_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 30, 1, 1, 1, 5),
    _HdlcMonitorReceiverAborts_Type()
)
hdlcMonitorReceiverAborts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdlcMonitorReceiverAborts.setStatus("mandatory")
_HdlcMonitorReceiverOverruns_Type = Integer32
_HdlcMonitorReceiverOverruns_Object = MibTableColumn
hdlcMonitorReceiverOverruns = _HdlcMonitorReceiverOverruns_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 30, 1, 1, 1, 6),
    _HdlcMonitorReceiverOverruns_Type()
)
hdlcMonitorReceiverOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdlcMonitorReceiverOverruns.setStatus("mandatory")
_HdlcMonitorReceiverMisalignments_Type = Integer32
_HdlcMonitorReceiverMisalignments_Object = MibTableColumn
hdlcMonitorReceiverMisalignments = _HdlcMonitorReceiverMisalignments_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 30, 1, 1, 1, 7),
    _HdlcMonitorReceiverMisalignments_Type()
)
hdlcMonitorReceiverMisalignments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdlcMonitorReceiverMisalignments.setStatus("mandatory")
_HdlcMonitorTransmitterUnderruns_Type = Integer32
_HdlcMonitorTransmitterUnderruns_Object = MibTableColumn
hdlcMonitorTransmitterUnderruns = _HdlcMonitorTransmitterUnderruns_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 30, 1, 1, 1, 8),
    _HdlcMonitorTransmitterUnderruns_Type()
)
hdlcMonitorTransmitterUnderruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdlcMonitorTransmitterUnderruns.setStatus("mandatory")
_HdlcMonitorReceiverAsyncParityErrors_Type = Integer32
_HdlcMonitorReceiverAsyncParityErrors_Object = MibTableColumn
hdlcMonitorReceiverAsyncParityErrors = _HdlcMonitorReceiverAsyncParityErrors_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 30, 1, 1, 1, 9),
    _HdlcMonitorReceiverAsyncParityErrors_Type()
)
hdlcMonitorReceiverAsyncParityErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdlcMonitorReceiverAsyncParityErrors.setStatus("mandatory")
_HdlcMonitorReceiverAsyncFramingErrors_Type = Integer32
_HdlcMonitorReceiverAsyncFramingErrors_Object = MibTableColumn
hdlcMonitorReceiverAsyncFramingErrors = _HdlcMonitorReceiverAsyncFramingErrors_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 30, 1, 1, 1, 10),
    _HdlcMonitorReceiverAsyncFramingErrors_Type()
)
hdlcMonitorReceiverAsyncFramingErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdlcMonitorReceiverAsyncFramingErrors.setStatus("mandatory")
_HdlcMonitorReceiverAsyncBreaks_Type = Integer32
_HdlcMonitorReceiverAsyncBreaks_Object = MibTableColumn
hdlcMonitorReceiverAsyncBreaks = _HdlcMonitorReceiverAsyncBreaks_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 30, 1, 1, 1, 11),
    _HdlcMonitorReceiverAsyncBreaks_Type()
)
hdlcMonitorReceiverAsyncBreaks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdlcMonitorReceiverAsyncBreaks.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INTEL-HDLC-MIB",
    **{"hdlc": hdlc,
       "hdlcMonitor": hdlcMonitor,
       "hdlcMonitorTable": hdlcMonitorTable,
       "hdlcMonitorEntry": hdlcMonitorEntry,
       "hdlcMonitorIndex": hdlcMonitorIndex,
       "hdlcMonitorReceiverChecksumErrors": hdlcMonitorReceiverChecksumErrors,
       "hdlcMonitorReceiverGiants": hdlcMonitorReceiverGiants,
       "hdlcMonitorReceiverDwarves": hdlcMonitorReceiverDwarves,
       "hdlcMonitorReceiverAborts": hdlcMonitorReceiverAborts,
       "hdlcMonitorReceiverOverruns": hdlcMonitorReceiverOverruns,
       "hdlcMonitorReceiverMisalignments": hdlcMonitorReceiverMisalignments,
       "hdlcMonitorTransmitterUnderruns": hdlcMonitorTransmitterUnderruns,
       "hdlcMonitorReceiverAsyncParityErrors": hdlcMonitorReceiverAsyncParityErrors,
       "hdlcMonitorReceiverAsyncFramingErrors": hdlcMonitorReceiverAsyncFramingErrors,
       "hdlcMonitorReceiverAsyncBreaks": hdlcMonitorReceiverAsyncBreaks}
)
