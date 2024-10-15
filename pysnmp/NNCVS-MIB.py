# SNMP MIB module (NNCVS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NNCVS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:28:31 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(nncExtensions,) = mibBuilder.importSymbols(
    "NNCGNI0001-SMI",
    "nncExtensions")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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

nncVS = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 123, 3, 72)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NncVSObjects_ObjectIdentity = ObjectIdentity
nncVSObjects = _NncVSObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 3, 72, 1)
)
_NncVSConfiguration_ObjectIdentity = ObjectIdentity
nncVSConfiguration = _NncVSConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 3, 72, 1, 1)
)
_NncVSStatistics_ObjectIdentity = ObjectIdentity
nncVSStatistics = _NncVSStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 3, 72, 1, 2)
)
_NncVSStatisticsTable_Object = MibTable
nncVSStatisticsTable = _NncVSStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 72, 1, 2, 1)
)
if mibBuilder.loadTexts:
    nncVSStatisticsTable.setStatus("current")
_NncVSStatisticsEntry_Object = MibTableRow
nncVSStatisticsEntry = _NncVSStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 72, 1, 2, 1, 1)
)
nncVSStatisticsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    nncVSStatisticsEntry.setStatus("current")
_NncVSLOCSeconds_Type = Counter32
_NncVSLOCSeconds_Object = MibTableColumn
nncVSLOCSeconds = _NncVSLOCSeconds_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 72, 1, 2, 1, 1, 1),
    _NncVSLOCSeconds_Type()
)
nncVSLOCSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncVSLOCSeconds.setStatus("current")
_NncVSRemoteChanFailureSeconds_Type = Counter32
_NncVSRemoteChanFailureSeconds_Object = MibTableColumn
nncVSRemoteChanFailureSeconds = _NncVSRemoteChanFailureSeconds_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 72, 1, 2, 1, 1, 2),
    _NncVSRemoteChanFailureSeconds_Type()
)
nncVSRemoteChanFailureSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncVSRemoteChanFailureSeconds.setStatus("current")
_NncVSUnderrunSeconds_Type = Counter32
_NncVSUnderrunSeconds_Object = MibTableColumn
nncVSUnderrunSeconds = _NncVSUnderrunSeconds_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 72, 1, 2, 1, 1, 3),
    _NncVSUnderrunSeconds_Type()
)
nncVSUnderrunSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncVSUnderrunSeconds.setStatus("current")
_NncVSBufferUnderflows_Type = Counter32
_NncVSBufferUnderflows_Object = MibTableColumn
nncVSBufferUnderflows = _NncVSBufferUnderflows_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 72, 1, 2, 1, 1, 4),
    _NncVSBufferUnderflows_Type()
)
nncVSBufferUnderflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncVSBufferUnderflows.setStatus("current")
_NncVSBufferOverflows_Type = Counter32
_NncVSBufferOverflows_Object = MibTableColumn
nncVSBufferOverflows = _NncVSBufferOverflows_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 72, 1, 2, 1, 1, 5),
    _NncVSBufferOverflows_Type()
)
nncVSBufferOverflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncVSBufferOverflows.setStatus("current")
_NncVSSequenceDiscontinuities_Type = Counter32
_NncVSSequenceDiscontinuities_Object = MibTableColumn
nncVSSequenceDiscontinuities = _NncVSSequenceDiscontinuities_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 72, 1, 2, 1, 1, 6),
    _NncVSSequenceDiscontinuities_Type()
)
nncVSSequenceDiscontinuities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncVSSequenceDiscontinuities.setStatus("current")
_NncVSSpeechRx_Type = Counter32
_NncVSSpeechRx_Object = MibTableColumn
nncVSSpeechRx = _NncVSSpeechRx_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 72, 1, 2, 1, 1, 7),
    _NncVSSpeechRx_Type()
)
nncVSSpeechRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncVSSpeechRx.setStatus("current")
_NncVSSpeechTx_Type = Counter32
_NncVSSpeechTx_Object = MibTableColumn
nncVSSpeechTx = _NncVSSpeechTx_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 72, 1, 2, 1, 1, 8),
    _NncVSSpeechTx_Type()
)
nncVSSpeechTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncVSSpeechTx.setStatus("current")
_NncVSFaxRx_Type = Counter32
_NncVSFaxRx_Object = MibTableColumn
nncVSFaxRx = _NncVSFaxRx_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 72, 1, 2, 1, 1, 9),
    _NncVSFaxRx_Type()
)
nncVSFaxRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncVSFaxRx.setStatus("current")
_NncVSFaxTx_Type = Counter32
_NncVSFaxTx_Object = MibTableColumn
nncVSFaxTx = _NncVSFaxTx_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 72, 1, 2, 1, 1, 10),
    _NncVSFaxTx_Type()
)
nncVSFaxTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncVSFaxTx.setStatus("current")
_NncVSBypassRx_Type = Counter32
_NncVSBypassRx_Object = MibTableColumn
nncVSBypassRx = _NncVSBypassRx_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 72, 1, 2, 1, 1, 11),
    _NncVSBypassRx_Type()
)
nncVSBypassRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncVSBypassRx.setStatus("current")
_NncVSBypassTx_Type = Counter32
_NncVSBypassTx_Object = MibTableColumn
nncVSBypassTx = _NncVSBypassTx_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 72, 1, 2, 1, 1, 12),
    _NncVSBypassTx_Type()
)
nncVSBypassTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncVSBypassTx.setStatus("current")
_NncVSCASRx_Type = Counter32
_NncVSCASRx_Object = MibTableColumn
nncVSCASRx = _NncVSCASRx_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 72, 1, 2, 1, 1, 13),
    _NncVSCASRx_Type()
)
nncVSCASRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncVSCASRx.setStatus("current")
_NncVSCASTx_Type = Counter32
_NncVSCASTx_Object = MibTableColumn
nncVSCASTx = _NncVSCASTx_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 72, 1, 2, 1, 1, 14),
    _NncVSCASTx_Type()
)
nncVSCASTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncVSCASTx.setStatus("current")
_NncVSDTMFDigitsRx_Type = Counter32
_NncVSDTMFDigitsRx_Object = MibTableColumn
nncVSDTMFDigitsRx = _NncVSDTMFDigitsRx_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 72, 1, 2, 1, 1, 15),
    _NncVSDTMFDigitsRx_Type()
)
nncVSDTMFDigitsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncVSDTMFDigitsRx.setStatus("current")
_NncVSDTMFDigitsTx_Type = Counter32
_NncVSDTMFDigitsTx_Object = MibTableColumn
nncVSDTMFDigitsTx = _NncVSDTMFDigitsTx_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 72, 1, 2, 1, 1, 16),
    _NncVSDTMFDigitsTx_Type()
)
nncVSDTMFDigitsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncVSDTMFDigitsTx.setStatus("current")
_NncVSSilenceRx_Type = Counter32
_NncVSSilenceRx_Object = MibTableColumn
nncVSSilenceRx = _NncVSSilenceRx_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 72, 1, 2, 1, 1, 17),
    _NncVSSilenceRx_Type()
)
nncVSSilenceRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncVSSilenceRx.setStatus("current")
_NncVSSilenceTx_Type = Counter32
_NncVSSilenceTx_Object = MibTableColumn
nncVSSilenceTx = _NncVSSilenceTx_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 72, 1, 2, 1, 1, 18),
    _NncVSSilenceTx_Type()
)
nncVSSilenceTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncVSSilenceTx.setStatus("current")
_NncVSTraps_ObjectIdentity = ObjectIdentity
nncVSTraps = _NncVSTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 3, 72, 2)
)
_NncVSGroups_ObjectIdentity = ObjectIdentity
nncVSGroups = _NncVSGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 3, 72, 3)
)
_NncVSCompliances_ObjectIdentity = ObjectIdentity
nncVSCompliances = _NncVSCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 3, 72, 4)
)

# Managed Objects groups

nncVSGeneralStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 123, 3, 72, 3, 1)
)
nncVSGeneralStatisticsGroup.setObjects(
      *(("NNCVS-MIB", "nncVSLOCSeconds"),
        ("NNCVS-MIB", "nncVSRemoteChanFailureSeconds"),
        ("NNCVS-MIB", "nncVSUnderrunSeconds"),
        ("NNCVS-MIB", "nncVSBufferUnderflows"),
        ("NNCVS-MIB", "nncVSBufferOverflows"),
        ("NNCVS-MIB", "nncVSSequenceDiscontinuities"))
)
if mibBuilder.loadTexts:
    nncVSGeneralStatisticsGroup.setStatus("current")

nncVSSubframeStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 123, 3, 72, 3, 2)
)
nncVSSubframeStatisticsGroup.setObjects(
      *(("NNCVS-MIB", "nncVSSpeechRx"),
        ("NNCVS-MIB", "nncVSSpeechTx"),
        ("NNCVS-MIB", "nncVSFaxRx"),
        ("NNCVS-MIB", "nncVSFaxTx"),
        ("NNCVS-MIB", "nncVSBypassRx"),
        ("NNCVS-MIB", "nncVSBypassTx"),
        ("NNCVS-MIB", "nncVSCASRx"),
        ("NNCVS-MIB", "nncVSCASTx"),
        ("NNCVS-MIB", "nncVSDTMFDigitsRx"),
        ("NNCVS-MIB", "nncVSDTMFDigitsTx"),
        ("NNCVS-MIB", "nncVSSilenceRx"),
        ("NNCVS-MIB", "nncVSSilenceTx"))
)
if mibBuilder.loadTexts:
    nncVSSubframeStatisticsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

nncVSCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 123, 3, 72, 4, 1)
)
if mibBuilder.loadTexts:
    nncVSCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NNCVS-MIB",
    **{"nncVS": nncVS,
       "nncVSObjects": nncVSObjects,
       "nncVSConfiguration": nncVSConfiguration,
       "nncVSStatistics": nncVSStatistics,
       "nncVSStatisticsTable": nncVSStatisticsTable,
       "nncVSStatisticsEntry": nncVSStatisticsEntry,
       "nncVSLOCSeconds": nncVSLOCSeconds,
       "nncVSRemoteChanFailureSeconds": nncVSRemoteChanFailureSeconds,
       "nncVSUnderrunSeconds": nncVSUnderrunSeconds,
       "nncVSBufferUnderflows": nncVSBufferUnderflows,
       "nncVSBufferOverflows": nncVSBufferOverflows,
       "nncVSSequenceDiscontinuities": nncVSSequenceDiscontinuities,
       "nncVSSpeechRx": nncVSSpeechRx,
       "nncVSSpeechTx": nncVSSpeechTx,
       "nncVSFaxRx": nncVSFaxRx,
       "nncVSFaxTx": nncVSFaxTx,
       "nncVSBypassRx": nncVSBypassRx,
       "nncVSBypassTx": nncVSBypassTx,
       "nncVSCASRx": nncVSCASRx,
       "nncVSCASTx": nncVSCASTx,
       "nncVSDTMFDigitsRx": nncVSDTMFDigitsRx,
       "nncVSDTMFDigitsTx": nncVSDTMFDigitsTx,
       "nncVSSilenceRx": nncVSSilenceRx,
       "nncVSSilenceTx": nncVSSilenceTx,
       "nncVSTraps": nncVSTraps,
       "nncVSGroups": nncVSGroups,
       "nncVSGeneralStatisticsGroup": nncVSGeneralStatisticsGroup,
       "nncVSSubframeStatisticsGroup": nncVSSubframeStatisticsGroup,
       "nncVSCompliances": nncVSCompliances,
       "nncVSCompliance": nncVSCompliance}
)
