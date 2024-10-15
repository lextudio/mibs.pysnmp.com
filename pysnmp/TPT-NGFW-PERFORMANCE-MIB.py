# SNMP MIB module (TPT-NGFW-PERFORMANCE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TPT-NGFW-PERFORMANCE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:07:02 2024
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

(tpt_ngfw_compls,
 tpt_ngfw_groups,
 tpt_ngfw_objs) = mibBuilder.importSymbols(
    "TPT-NGFW-REG-MIB",
    "tpt-ngfw-compls",
    "tpt-ngfw-groups",
    "tpt-ngfw-objs")


# MODULE-IDENTITY

tptNgfwPerformance = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 3)
)
tptNgfwPerformance.setRevisions(
        ("2016-05-25 18:54",
         "2013-01-03 17:39")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class TptNgfwPerfPacketSizeGrouping(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("bytes1024to1518", 5),
          ("bytes128to255", 2),
          ("bytes1519to4095", 6),
          ("bytes256to511", 3),
          ("bytes4096to9216", 7),
          ("bytes512to1023", 4),
          ("bytes64", 0),
          ("bytes65to127", 1),
          ("bytes9217to16383", 8),
          ("oversize", 10),
          ("undersize", 9))
    )



# MIB Managed Objects in the order of their OIDs

_TptNgfwPerformanceObjs_ObjectIdentity = ObjectIdentity
tptNgfwPerformanceObjs = _TptNgfwPerformanceObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 3, 1)
)
if mibBuilder.loadTexts:
    tptNgfwPerformanceObjs.setStatus("current")
_TptNgfwPerfPacketsIn_Type = Counter64
_TptNgfwPerfPacketsIn_Object = MibScalar
tptNgfwPerfPacketsIn = _TptNgfwPerfPacketsIn_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 3, 1, 1),
    _TptNgfwPerfPacketsIn_Type()
)
tptNgfwPerfPacketsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptNgfwPerfPacketsIn.setStatus("current")
_TptNgfwPerfPacketsOut_Type = Counter64
_TptNgfwPerfPacketsOut_Object = MibScalar
tptNgfwPerfPacketsOut = _TptNgfwPerfPacketsOut_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 3, 1, 2),
    _TptNgfwPerfPacketsOut_Type()
)
tptNgfwPerfPacketsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptNgfwPerfPacketsOut.setStatus("current")
_TptNgfwPerfBytesIn_Type = Counter64
_TptNgfwPerfBytesIn_Object = MibScalar
tptNgfwPerfBytesIn = _TptNgfwPerfBytesIn_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 3, 1, 3),
    _TptNgfwPerfBytesIn_Type()
)
tptNgfwPerfBytesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptNgfwPerfBytesIn.setStatus("current")
_TptNgfwPerfBytesOut_Type = Counter64
_TptNgfwPerfBytesOut_Object = MibScalar
tptNgfwPerfBytesOut = _TptNgfwPerfBytesOut_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 3, 1, 4),
    _TptNgfwPerfBytesOut_Type()
)
tptNgfwPerfBytesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptNgfwPerfBytesOut.setStatus("current")
_TptNgfwPerfFragmentsIn_Type = Counter64
_TptNgfwPerfFragmentsIn_Object = MibScalar
tptNgfwPerfFragmentsIn = _TptNgfwPerfFragmentsIn_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 3, 1, 5),
    _TptNgfwPerfFragmentsIn_Type()
)
tptNgfwPerfFragmentsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptNgfwPerfFragmentsIn.setStatus("current")
_TptNgfwPerfFragmentsOut_Type = Counter64
_TptNgfwPerfFragmentsOut_Object = MibScalar
tptNgfwPerfFragmentsOut = _TptNgfwPerfFragmentsOut_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 3, 1, 6),
    _TptNgfwPerfFragmentsOut_Type()
)
tptNgfwPerfFragmentsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptNgfwPerfFragmentsOut.setStatus("current")
_TptNgfwPerfPacketDistTable_Object = MibTable
tptNgfwPerfPacketDistTable = _TptNgfwPerfPacketDistTable_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 3, 1, 7)
)
if mibBuilder.loadTexts:
    tptNgfwPerfPacketDistTable.setStatus("current")
_TptNgfwPerfPacketDistEntry_Object = MibTableRow
tptNgfwPerfPacketDistEntry = _TptNgfwPerfPacketDistEntry_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 3, 1, 7, 1)
)
tptNgfwPerfPacketDistEntry.setIndexNames(
    (0, "TPT-NGFW-PERFORMANCE-MIB", "tptNgfwPerfPacketDistEntryIndex"),
)
if mibBuilder.loadTexts:
    tptNgfwPerfPacketDistEntry.setStatus("current")
_TptNgfwPerfPacketDistEntryIndex_Type = Unsigned32
_TptNgfwPerfPacketDistEntryIndex_Object = MibTableColumn
tptNgfwPerfPacketDistEntryIndex = _TptNgfwPerfPacketDistEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 3, 1, 7, 1, 1),
    _TptNgfwPerfPacketDistEntryIndex_Type()
)
tptNgfwPerfPacketDistEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tptNgfwPerfPacketDistEntryIndex.setStatus("current")
_TptNgfwPerfPacketDistSizeGrp_Type = TptNgfwPerfPacketSizeGrouping
_TptNgfwPerfPacketDistSizeGrp_Object = MibTableColumn
tptNgfwPerfPacketDistSizeGrp = _TptNgfwPerfPacketDistSizeGrp_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 3, 1, 7, 1, 2),
    _TptNgfwPerfPacketDistSizeGrp_Type()
)
tptNgfwPerfPacketDistSizeGrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptNgfwPerfPacketDistSizeGrp.setStatus("current")
_TptNgfwPerfPacketDistSizeGrpCount_Type = Counter64
_TptNgfwPerfPacketDistSizeGrpCount_Object = MibTableColumn
tptNgfwPerfPacketDistSizeGrpCount = _TptNgfwPerfPacketDistSizeGrpCount_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 3, 1, 7, 1, 3),
    _TptNgfwPerfPacketDistSizeGrpCount_Type()
)
tptNgfwPerfPacketDistSizeGrpCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptNgfwPerfPacketDistSizeGrpCount.setStatus("current")
_TptNgfwPerfFWObjs_ObjectIdentity = ObjectIdentity
tptNgfwPerfFWObjs = _TptNgfwPerfFWObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 3, 2)
)
if mibBuilder.loadTexts:
    tptNgfwPerfFWObjs.setStatus("current")
_TptNgfwPerfFWBlocks_Type = Counter64
_TptNgfwPerfFWBlocks_Object = MibScalar
tptNgfwPerfFWBlocks = _TptNgfwPerfFWBlocks_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 3, 2, 1),
    _TptNgfwPerfFWBlocks_Type()
)
tptNgfwPerfFWBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptNgfwPerfFWBlocks.setStatus("current")
_TptNgfwPerfFWPermits_Type = Counter64
_TptNgfwPerfFWPermits_Object = MibScalar
tptNgfwPerfFWPermits = _TptNgfwPerfFWPermits_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 3, 2, 2),
    _TptNgfwPerfFWPermits_Type()
)
tptNgfwPerfFWPermits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptNgfwPerfFWPermits.setStatus("current")
_TptNgfwPerfFWSessions_Type = Counter64
_TptNgfwPerfFWSessions_Object = MibScalar
tptNgfwPerfFWSessions = _TptNgfwPerfFWSessions_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 3, 2, 3),
    _TptNgfwPerfFWSessions_Type()
)
tptNgfwPerfFWSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptNgfwPerfFWSessions.setStatus("current")
_TptNgfwPerfIPSObjs_ObjectIdentity = ObjectIdentity
tptNgfwPerfIPSObjs = _TptNgfwPerfIPSObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 3, 3)
)
if mibBuilder.loadTexts:
    tptNgfwPerfIPSObjs.setStatus("current")
_TptNgfwPerfIPSManagedStreams_Type = Counter64
_TptNgfwPerfIPSManagedStreams_Object = MibScalar
tptNgfwPerfIPSManagedStreams = _TptNgfwPerfIPSManagedStreams_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 3, 3, 1),
    _TptNgfwPerfIPSManagedStreams_Type()
)
tptNgfwPerfIPSManagedStreams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptNgfwPerfIPSManagedStreams.setStatus("current")
_TptNgfwPerfIPSQuarantineCount_Type = Counter64
_TptNgfwPerfIPSQuarantineCount_Object = MibScalar
tptNgfwPerfIPSQuarantineCount = _TptNgfwPerfIPSQuarantineCount_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 3, 3, 2),
    _TptNgfwPerfIPSQuarantineCount_Type()
)
tptNgfwPerfIPSQuarantineCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptNgfwPerfIPSQuarantineCount.setStatus("current")
_TptNgfwPerfIPSRateLimitCount_Type = Counter64
_TptNgfwPerfIPSRateLimitCount_Object = MibScalar
tptNgfwPerfIPSRateLimitCount = _TptNgfwPerfIPSRateLimitCount_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 3, 3, 3),
    _TptNgfwPerfIPSRateLimitCount_Type()
)
tptNgfwPerfIPSRateLimitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptNgfwPerfIPSRateLimitCount.setStatus("current")
_TptNgfwPerfIPSAfcEntries_Type = Counter64
_TptNgfwPerfIPSAfcEntries_Object = MibScalar
tptNgfwPerfIPSAfcEntries = _TptNgfwPerfIPSAfcEntries_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 3, 3, 4),
    _TptNgfwPerfIPSAfcEntries_Type()
)
tptNgfwPerfIPSAfcEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptNgfwPerfIPSAfcEntries.setStatus("current")
_TptNgfwPerfIPSAfcAppEntries_Type = Counter64
_TptNgfwPerfIPSAfcAppEntries_Object = MibScalar
tptNgfwPerfIPSAfcAppEntries = _TptNgfwPerfIPSAfcAppEntries_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 3, 3, 5),
    _TptNgfwPerfIPSAfcAppEntries_Type()
)
tptNgfwPerfIPSAfcAppEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptNgfwPerfIPSAfcAppEntries.setStatus("current")
_TptNgfwPerfIPSBlockedStreams_Type = Counter64
_TptNgfwPerfIPSBlockedStreams_Object = MibScalar
tptNgfwPerfIPSBlockedStreams = _TptNgfwPerfIPSBlockedStreams_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 3, 3, 6),
    _TptNgfwPerfIPSBlockedStreams_Type()
)
tptNgfwPerfIPSBlockedStreams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptNgfwPerfIPSBlockedStreams.setStatus("current")
_TptNgfwPerfIPSTrustedStreams_Type = Counter64
_TptNgfwPerfIPSTrustedStreams_Object = MibScalar
tptNgfwPerfIPSTrustedStreams = _TptNgfwPerfIPSTrustedStreams_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 3, 3, 7),
    _TptNgfwPerfIPSTrustedStreams_Type()
)
tptNgfwPerfIPSTrustedStreams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptNgfwPerfIPSTrustedStreams.setStatus("current")

# Managed Objects groups

tptNgfwPerformanceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 1, 1, 6)
)
tptNgfwPerformanceGroup.setObjects(
      *(("TPT-NGFW-PERFORMANCE-MIB", "tptNgfwPerfPacketsIn"),
        ("TPT-NGFW-PERFORMANCE-MIB", "tptNgfwPerfPacketsOut"),
        ("TPT-NGFW-PERFORMANCE-MIB", "tptNgfwPerfBytesIn"),
        ("TPT-NGFW-PERFORMANCE-MIB", "tptNgfwPerfBytesOut"),
        ("TPT-NGFW-PERFORMANCE-MIB", "tptNgfwPerfFragmentsIn"),
        ("TPT-NGFW-PERFORMANCE-MIB", "tptNgfwPerfFragmentsOut"),
        ("TPT-NGFW-PERFORMANCE-MIB", "tptNgfwPerfFWBlocks"),
        ("TPT-NGFW-PERFORMANCE-MIB", "tptNgfwPerfFWPermits"),
        ("TPT-NGFW-PERFORMANCE-MIB", "tptNgfwPerfFWSessions"),
        ("TPT-NGFW-PERFORMANCE-MIB", "tptNgfwPerfIPSManagedStreams"),
        ("TPT-NGFW-PERFORMANCE-MIB", "tptNgfwPerfIPSQuarantineCount"),
        ("TPT-NGFW-PERFORMANCE-MIB", "tptNgfwPerfIPSRateLimitCount"),
        ("TPT-NGFW-PERFORMANCE-MIB", "tptNgfwPerfIPSAfcEntries"),
        ("TPT-NGFW-PERFORMANCE-MIB", "tptNgfwPerfIPSAfcAppEntries"),
        ("TPT-NGFW-PERFORMANCE-MIB", "tptNgfwPerfIPSBlockedStreams"),
        ("TPT-NGFW-PERFORMANCE-MIB", "tptNgfwPerfIPSTrustedStreams"),
        ("TPT-NGFW-PERFORMANCE-MIB", "tptNgfwPerfPacketDistSizeGrp"),
        ("TPT-NGFW-PERFORMANCE-MIB", "tptNgfwPerfPacketDistSizeGrpCount"))
)
if mibBuilder.loadTexts:
    tptNgfwPerformanceGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

tptNgfwPerformanceCompl = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 1, 2, 3)
)
if mibBuilder.loadTexts:
    tptNgfwPerformanceCompl.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPT-NGFW-PERFORMANCE-MIB",
    **{"TptNgfwPerfPacketSizeGrouping": TptNgfwPerfPacketSizeGrouping,
       "tptNgfwPerformanceGroup": tptNgfwPerformanceGroup,
       "tptNgfwPerformanceCompl": tptNgfwPerformanceCompl,
       "tptNgfwPerformance": tptNgfwPerformance,
       "tptNgfwPerformanceObjs": tptNgfwPerformanceObjs,
       "tptNgfwPerfPacketsIn": tptNgfwPerfPacketsIn,
       "tptNgfwPerfPacketsOut": tptNgfwPerfPacketsOut,
       "tptNgfwPerfBytesIn": tptNgfwPerfBytesIn,
       "tptNgfwPerfBytesOut": tptNgfwPerfBytesOut,
       "tptNgfwPerfFragmentsIn": tptNgfwPerfFragmentsIn,
       "tptNgfwPerfFragmentsOut": tptNgfwPerfFragmentsOut,
       "tptNgfwPerfPacketDistTable": tptNgfwPerfPacketDistTable,
       "tptNgfwPerfPacketDistEntry": tptNgfwPerfPacketDistEntry,
       "tptNgfwPerfPacketDistEntryIndex": tptNgfwPerfPacketDistEntryIndex,
       "tptNgfwPerfPacketDistSizeGrp": tptNgfwPerfPacketDistSizeGrp,
       "tptNgfwPerfPacketDistSizeGrpCount": tptNgfwPerfPacketDistSizeGrpCount,
       "tptNgfwPerfFWObjs": tptNgfwPerfFWObjs,
       "tptNgfwPerfFWBlocks": tptNgfwPerfFWBlocks,
       "tptNgfwPerfFWPermits": tptNgfwPerfFWPermits,
       "tptNgfwPerfFWSessions": tptNgfwPerfFWSessions,
       "tptNgfwPerfIPSObjs": tptNgfwPerfIPSObjs,
       "tptNgfwPerfIPSManagedStreams": tptNgfwPerfIPSManagedStreams,
       "tptNgfwPerfIPSQuarantineCount": tptNgfwPerfIPSQuarantineCount,
       "tptNgfwPerfIPSRateLimitCount": tptNgfwPerfIPSRateLimitCount,
       "tptNgfwPerfIPSAfcEntries": tptNgfwPerfIPSAfcEntries,
       "tptNgfwPerfIPSAfcAppEntries": tptNgfwPerfIPSAfcAppEntries,
       "tptNgfwPerfIPSBlockedStreams": tptNgfwPerfIPSBlockedStreams,
       "tptNgfwPerfIPSTrustedStreams": tptNgfwPerfIPSTrustedStreams}
)
