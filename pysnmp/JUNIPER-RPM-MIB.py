# SNMP MIB module (JUNIPER-RPM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/JUNIPER-RPM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:14:07 2024
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

(pingCtlOwnerIndex,
 pingCtlTestName,
 pingProbeHistoryIndex) = mibBuilder.importSymbols(
    "DISMAN-PING-MIB",
    "pingCtlOwnerIndex",
    "pingCtlTestName",
    "pingProbeHistoryIndex")

(CounterBasedGauge64,) = mibBuilder.importSymbols(
    "HCNUM-TC",
    "CounterBasedGauge64")

(jnxRpmMibRoot,) = mibBuilder.importSymbols(
    "JUNIPER-SMI",
    "jnxRpmMibRoot")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

jnxRpmMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 50, 1)
)
jnxRpmMib.setRevisions(
        ("2007-03-01 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class JnxRpmCollectionType(Integer32, TextualConvention):
    status = "current"
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
        *(("allTests", 4),
          ("currentTest", 1),
          ("lastCompletedTest", 2),
          ("movingAverage", 3))
    )



class JnxRpmMeasurementType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("egress", 4),
          ("egressInterarrivalJitter", 6),
          ("egressJitter", 5),
          ("ingress", 7),
          ("ingressInterarrivalJitter", 9),
          ("ingressJitter", 8),
          ("roundTripTime", 1),
          ("rttInterarrivalJitter", 3),
          ("rttJitter", 2))
    )



class JnxRpmMeasurementSet(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("egress", 4),
          ("ingress", 7),
          ("negEgressJitter", 6),
          ("negIngressJitter", 9),
          ("negRttJitter", 3),
          ("posEgressJitter", 5),
          ("posIngressJitter", 8),
          ("posRttJitter", 2),
          ("roundTripTime", 1))
    )



class JnxRpmTimestampType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clientAndServerHardware", 3),
          ("clientHardware", 2),
          ("software", 1))
    )



# MIB Managed Objects in the order of their OIDs

_JnxRpmResultsSampleTable_Object = MibTable
jnxRpmResultsSampleTable = _JnxRpmResultsSampleTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 50, 1, 1)
)
if mibBuilder.loadTexts:
    jnxRpmResultsSampleTable.setStatus("current")
_JnxRpmResultsSampleEntry_Object = MibTableRow
jnxRpmResultsSampleEntry = _JnxRpmResultsSampleEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 50, 1, 1, 1)
)
jnxRpmResultsSampleEntry.setIndexNames(
    (0, "DISMAN-PING-MIB", "pingCtlOwnerIndex"),
    (0, "DISMAN-PING-MIB", "pingCtlTestName"),
    (0, "JUNIPER-RPM-MIB", "jnxRpmResSampleType"),
)
if mibBuilder.loadTexts:
    jnxRpmResultsSampleEntry.setStatus("current")
_JnxRpmResSampleType_Type = JnxRpmMeasurementType
_JnxRpmResSampleType_Object = MibTableColumn
jnxRpmResSampleType = _JnxRpmResSampleType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 50, 1, 1, 1, 1),
    _JnxRpmResSampleType_Type()
)
jnxRpmResSampleType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxRpmResSampleType.setStatus("current")
_JnxRpmResSampleValue_Type = Integer32
_JnxRpmResSampleValue_Object = MibTableColumn
jnxRpmResSampleValue = _JnxRpmResSampleValue_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 50, 1, 1, 1, 2),
    _JnxRpmResSampleValue_Type()
)
jnxRpmResSampleValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxRpmResSampleValue.setStatus("current")
_JnxRpmResSampleTsType_Type = JnxRpmTimestampType
_JnxRpmResSampleTsType_Object = MibTableColumn
jnxRpmResSampleTsType = _JnxRpmResSampleTsType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 50, 1, 1, 1, 3),
    _JnxRpmResSampleTsType_Type()
)
jnxRpmResSampleTsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxRpmResSampleTsType.setStatus("current")
_JnxRpmResSampleDate_Type = DateAndTime
_JnxRpmResSampleDate_Object = MibTableColumn
jnxRpmResSampleDate = _JnxRpmResSampleDate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 50, 1, 1, 1, 4),
    _JnxRpmResSampleDate_Type()
)
jnxRpmResSampleDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxRpmResSampleDate.setStatus("current")
_JnxRpmResultsSummaryTable_Object = MibTable
jnxRpmResultsSummaryTable = _JnxRpmResultsSummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 50, 1, 2)
)
if mibBuilder.loadTexts:
    jnxRpmResultsSummaryTable.setStatus("current")
_JnxRpmResultsSummaryEntry_Object = MibTableRow
jnxRpmResultsSummaryEntry = _JnxRpmResultsSummaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 50, 1, 2, 1)
)
jnxRpmResultsSummaryEntry.setIndexNames(
    (0, "DISMAN-PING-MIB", "pingCtlOwnerIndex"),
    (0, "DISMAN-PING-MIB", "pingCtlTestName"),
    (0, "JUNIPER-RPM-MIB", "jnxRpmResSumCollection"),
)
if mibBuilder.loadTexts:
    jnxRpmResultsSummaryEntry.setStatus("current")
_JnxRpmResSumCollection_Type = JnxRpmCollectionType
_JnxRpmResSumCollection_Object = MibTableColumn
jnxRpmResSumCollection = _JnxRpmResSumCollection_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 50, 1, 2, 1, 1),
    _JnxRpmResSumCollection_Type()
)
jnxRpmResSumCollection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxRpmResSumCollection.setStatus("current")
_JnxRpmResSumSent_Type = Unsigned32
_JnxRpmResSumSent_Object = MibTableColumn
jnxRpmResSumSent = _JnxRpmResSumSent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 50, 1, 2, 1, 2),
    _JnxRpmResSumSent_Type()
)
jnxRpmResSumSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxRpmResSumSent.setStatus("current")
_JnxRpmResSumReceived_Type = Unsigned32
_JnxRpmResSumReceived_Object = MibTableColumn
jnxRpmResSumReceived = _JnxRpmResSumReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 50, 1, 2, 1, 3),
    _JnxRpmResSumReceived_Type()
)
jnxRpmResSumReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxRpmResSumReceived.setStatus("current")
_JnxRpmResSumPercentLost_Type = Unsigned32
_JnxRpmResSumPercentLost_Object = MibTableColumn
jnxRpmResSumPercentLost = _JnxRpmResSumPercentLost_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 50, 1, 2, 1, 4),
    _JnxRpmResSumPercentLost_Type()
)
jnxRpmResSumPercentLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxRpmResSumPercentLost.setStatus("current")
_JnxRpmResSumDate_Type = DateAndTime
_JnxRpmResSumDate_Object = MibTableColumn
jnxRpmResSumDate = _JnxRpmResSumDate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 50, 1, 2, 1, 5),
    _JnxRpmResSumDate_Type()
)
jnxRpmResSumDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxRpmResSumDate.setStatus("current")
_JnxRpmResultsCalculatedTable_Object = MibTable
jnxRpmResultsCalculatedTable = _JnxRpmResultsCalculatedTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 50, 1, 3)
)
if mibBuilder.loadTexts:
    jnxRpmResultsCalculatedTable.setStatus("current")
_JnxRpmResultsCalculatedEntry_Object = MibTableRow
jnxRpmResultsCalculatedEntry = _JnxRpmResultsCalculatedEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 50, 1, 3, 1)
)
jnxRpmResultsCalculatedEntry.setIndexNames(
    (0, "DISMAN-PING-MIB", "pingCtlOwnerIndex"),
    (0, "DISMAN-PING-MIB", "pingCtlTestName"),
    (0, "JUNIPER-RPM-MIB", "jnxRpmResSumCollection"),
    (0, "JUNIPER-RPM-MIB", "jnxRpmResCalcSet"),
)
if mibBuilder.loadTexts:
    jnxRpmResultsCalculatedEntry.setStatus("current")
_JnxRpmResCalcSet_Type = JnxRpmMeasurementSet
_JnxRpmResCalcSet_Object = MibTableColumn
jnxRpmResCalcSet = _JnxRpmResCalcSet_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 50, 1, 3, 1, 1),
    _JnxRpmResCalcSet_Type()
)
jnxRpmResCalcSet.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxRpmResCalcSet.setStatus("current")
_JnxRpmResCalcSamples_Type = Unsigned32
_JnxRpmResCalcSamples_Object = MibTableColumn
jnxRpmResCalcSamples = _JnxRpmResCalcSamples_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 50, 1, 3, 1, 2),
    _JnxRpmResCalcSamples_Type()
)
jnxRpmResCalcSamples.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxRpmResCalcSamples.setStatus("current")
_JnxRpmResCalcMin_Type = Unsigned32
_JnxRpmResCalcMin_Object = MibTableColumn
jnxRpmResCalcMin = _JnxRpmResCalcMin_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 50, 1, 3, 1, 3),
    _JnxRpmResCalcMin_Type()
)
jnxRpmResCalcMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxRpmResCalcMin.setStatus("current")
_JnxRpmResCalcMax_Type = Unsigned32
_JnxRpmResCalcMax_Object = MibTableColumn
jnxRpmResCalcMax = _JnxRpmResCalcMax_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 50, 1, 3, 1, 4),
    _JnxRpmResCalcMax_Type()
)
jnxRpmResCalcMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxRpmResCalcMax.setStatus("current")
_JnxRpmResCalcAverage_Type = Unsigned32
_JnxRpmResCalcAverage_Object = MibTableColumn
jnxRpmResCalcAverage = _JnxRpmResCalcAverage_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 50, 1, 3, 1, 5),
    _JnxRpmResCalcAverage_Type()
)
jnxRpmResCalcAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxRpmResCalcAverage.setStatus("current")
_JnxRpmResCalcPkToPk_Type = Unsigned32
_JnxRpmResCalcPkToPk_Object = MibTableColumn
jnxRpmResCalcPkToPk = _JnxRpmResCalcPkToPk_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 50, 1, 3, 1, 6),
    _JnxRpmResCalcPkToPk_Type()
)
jnxRpmResCalcPkToPk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxRpmResCalcPkToPk.setStatus("current")
_JnxRpmResCalcStdDev_Type = Unsigned32
_JnxRpmResCalcStdDev_Object = MibTableColumn
jnxRpmResCalcStdDev = _JnxRpmResCalcStdDev_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 50, 1, 3, 1, 7),
    _JnxRpmResCalcStdDev_Type()
)
jnxRpmResCalcStdDev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxRpmResCalcStdDev.setStatus("current")
_JnxRpmResCalcSum_Type = CounterBasedGauge64
_JnxRpmResCalcSum_Object = MibTableColumn
jnxRpmResCalcSum = _JnxRpmResCalcSum_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 50, 1, 3, 1, 8),
    _JnxRpmResCalcSum_Type()
)
jnxRpmResCalcSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxRpmResCalcSum.setStatus("current")
_JnxRpmHistorySampleTable_Object = MibTable
jnxRpmHistorySampleTable = _JnxRpmHistorySampleTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 50, 1, 4)
)
if mibBuilder.loadTexts:
    jnxRpmHistorySampleTable.setStatus("current")
_JnxRpmHistorySampleEntry_Object = MibTableRow
jnxRpmHistorySampleEntry = _JnxRpmHistorySampleEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 50, 1, 4, 1)
)
jnxRpmHistorySampleEntry.setIndexNames(
    (0, "DISMAN-PING-MIB", "pingCtlOwnerIndex"),
    (0, "DISMAN-PING-MIB", "pingCtlTestName"),
    (0, "DISMAN-PING-MIB", "pingProbeHistoryIndex"),
    (0, "JUNIPER-RPM-MIB", "jnxRpmHistSampleType"),
)
if mibBuilder.loadTexts:
    jnxRpmHistorySampleEntry.setStatus("current")
_JnxRpmHistSampleType_Type = JnxRpmMeasurementType
_JnxRpmHistSampleType_Object = MibTableColumn
jnxRpmHistSampleType = _JnxRpmHistSampleType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 50, 1, 4, 1, 1),
    _JnxRpmHistSampleType_Type()
)
jnxRpmHistSampleType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxRpmHistSampleType.setStatus("current")
_JnxRpmHistSampleValue_Type = Integer32
_JnxRpmHistSampleValue_Object = MibTableColumn
jnxRpmHistSampleValue = _JnxRpmHistSampleValue_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 50, 1, 4, 1, 2),
    _JnxRpmHistSampleValue_Type()
)
jnxRpmHistSampleValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxRpmHistSampleValue.setStatus("current")
_JnxRpmHistSampleTsType_Type = JnxRpmTimestampType
_JnxRpmHistSampleTsType_Object = MibTableColumn
jnxRpmHistSampleTsType = _JnxRpmHistSampleTsType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 50, 1, 4, 1, 3),
    _JnxRpmHistSampleTsType_Type()
)
jnxRpmHistSampleTsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxRpmHistSampleTsType.setStatus("current")
_JnxRpmHistorySummaryTable_Object = MibTable
jnxRpmHistorySummaryTable = _JnxRpmHistorySummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 50, 1, 5)
)
if mibBuilder.loadTexts:
    jnxRpmHistorySummaryTable.setStatus("current")
_JnxRpmHistorySummaryEntry_Object = MibTableRow
jnxRpmHistorySummaryEntry = _JnxRpmHistorySummaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 50, 1, 5, 1)
)
jnxRpmHistorySummaryEntry.setIndexNames(
    (0, "DISMAN-PING-MIB", "pingCtlOwnerIndex"),
    (0, "DISMAN-PING-MIB", "pingCtlTestName"),
    (0, "DISMAN-PING-MIB", "pingProbeHistoryIndex"),
    (0, "JUNIPER-RPM-MIB", "jnxRpmHistSumCollection"),
)
if mibBuilder.loadTexts:
    jnxRpmHistorySummaryEntry.setStatus("current")
_JnxRpmHistSumCollection_Type = JnxRpmCollectionType
_JnxRpmHistSumCollection_Object = MibTableColumn
jnxRpmHistSumCollection = _JnxRpmHistSumCollection_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 50, 1, 5, 1, 1),
    _JnxRpmHistSumCollection_Type()
)
jnxRpmHistSumCollection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxRpmHistSumCollection.setStatus("current")
_JnxRpmHistSumSent_Type = Unsigned32
_JnxRpmHistSumSent_Object = MibTableColumn
jnxRpmHistSumSent = _JnxRpmHistSumSent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 50, 1, 5, 1, 2),
    _JnxRpmHistSumSent_Type()
)
jnxRpmHistSumSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxRpmHistSumSent.setStatus("current")
_JnxRpmHistSumReceived_Type = Unsigned32
_JnxRpmHistSumReceived_Object = MibTableColumn
jnxRpmHistSumReceived = _JnxRpmHistSumReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 50, 1, 5, 1, 3),
    _JnxRpmHistSumReceived_Type()
)
jnxRpmHistSumReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxRpmHistSumReceived.setStatus("current")
_JnxRpmHistSumPercentLost_Type = Unsigned32
_JnxRpmHistSumPercentLost_Object = MibTableColumn
jnxRpmHistSumPercentLost = _JnxRpmHistSumPercentLost_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 50, 1, 5, 1, 4),
    _JnxRpmHistSumPercentLost_Type()
)
jnxRpmHistSumPercentLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxRpmHistSumPercentLost.setStatus("current")
_JnxRpmHistoryCalculatedTable_Object = MibTable
jnxRpmHistoryCalculatedTable = _JnxRpmHistoryCalculatedTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 50, 1, 6)
)
if mibBuilder.loadTexts:
    jnxRpmHistoryCalculatedTable.setStatus("current")
_JnxRpmHistoryCalculatedEntry_Object = MibTableRow
jnxRpmHistoryCalculatedEntry = _JnxRpmHistoryCalculatedEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 50, 1, 6, 1)
)
jnxRpmHistoryCalculatedEntry.setIndexNames(
    (0, "DISMAN-PING-MIB", "pingCtlOwnerIndex"),
    (0, "DISMAN-PING-MIB", "pingCtlTestName"),
    (0, "DISMAN-PING-MIB", "pingProbeHistoryIndex"),
    (0, "JUNIPER-RPM-MIB", "jnxRpmHistSumCollection"),
    (0, "JUNIPER-RPM-MIB", "jnxRpmHistCalcSet"),
)
if mibBuilder.loadTexts:
    jnxRpmHistoryCalculatedEntry.setStatus("current")
_JnxRpmHistCalcSet_Type = JnxRpmMeasurementSet
_JnxRpmHistCalcSet_Object = MibTableColumn
jnxRpmHistCalcSet = _JnxRpmHistCalcSet_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 50, 1, 6, 1, 1),
    _JnxRpmHistCalcSet_Type()
)
jnxRpmHistCalcSet.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxRpmHistCalcSet.setStatus("current")
_JnxRpmHistCalcSamples_Type = Unsigned32
_JnxRpmHistCalcSamples_Object = MibTableColumn
jnxRpmHistCalcSamples = _JnxRpmHistCalcSamples_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 50, 1, 6, 1, 2),
    _JnxRpmHistCalcSamples_Type()
)
jnxRpmHistCalcSamples.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxRpmHistCalcSamples.setStatus("current")
_JnxRpmHistCalcMin_Type = Unsigned32
_JnxRpmHistCalcMin_Object = MibTableColumn
jnxRpmHistCalcMin = _JnxRpmHistCalcMin_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 50, 1, 6, 1, 3),
    _JnxRpmHistCalcMin_Type()
)
jnxRpmHistCalcMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxRpmHistCalcMin.setStatus("current")
_JnxRpmHistCalcMax_Type = Unsigned32
_JnxRpmHistCalcMax_Object = MibTableColumn
jnxRpmHistCalcMax = _JnxRpmHistCalcMax_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 50, 1, 6, 1, 4),
    _JnxRpmHistCalcMax_Type()
)
jnxRpmHistCalcMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxRpmHistCalcMax.setStatus("current")
_JnxRpmHistCalcAverage_Type = Unsigned32
_JnxRpmHistCalcAverage_Object = MibTableColumn
jnxRpmHistCalcAverage = _JnxRpmHistCalcAverage_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 50, 1, 6, 1, 5),
    _JnxRpmHistCalcAverage_Type()
)
jnxRpmHistCalcAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxRpmHistCalcAverage.setStatus("current")
_JnxRpmHistCalcPkToPk_Type = Unsigned32
_JnxRpmHistCalcPkToPk_Object = MibTableColumn
jnxRpmHistCalcPkToPk = _JnxRpmHistCalcPkToPk_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 50, 1, 6, 1, 6),
    _JnxRpmHistCalcPkToPk_Type()
)
jnxRpmHistCalcPkToPk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxRpmHistCalcPkToPk.setStatus("current")
_JnxRpmHistCalcStdDev_Type = Unsigned32
_JnxRpmHistCalcStdDev_Object = MibTableColumn
jnxRpmHistCalcStdDev = _JnxRpmHistCalcStdDev_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 50, 1, 6, 1, 7),
    _JnxRpmHistCalcStdDev_Type()
)
jnxRpmHistCalcStdDev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxRpmHistCalcStdDev.setStatus("current")
_JnxRpmHistCalcSum_Type = CounterBasedGauge64
_JnxRpmHistCalcSum_Object = MibTableColumn
jnxRpmHistCalcSum = _JnxRpmHistCalcSum_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 50, 1, 6, 1, 8),
    _JnxRpmHistCalcSum_Type()
)
jnxRpmHistCalcSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxRpmHistCalcSum.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-RPM-MIB",
    **{"JnxRpmCollectionType": JnxRpmCollectionType,
       "JnxRpmMeasurementType": JnxRpmMeasurementType,
       "JnxRpmMeasurementSet": JnxRpmMeasurementSet,
       "JnxRpmTimestampType": JnxRpmTimestampType,
       "jnxRpmMib": jnxRpmMib,
       "jnxRpmResultsSampleTable": jnxRpmResultsSampleTable,
       "jnxRpmResultsSampleEntry": jnxRpmResultsSampleEntry,
       "jnxRpmResSampleType": jnxRpmResSampleType,
       "jnxRpmResSampleValue": jnxRpmResSampleValue,
       "jnxRpmResSampleTsType": jnxRpmResSampleTsType,
       "jnxRpmResSampleDate": jnxRpmResSampleDate,
       "jnxRpmResultsSummaryTable": jnxRpmResultsSummaryTable,
       "jnxRpmResultsSummaryEntry": jnxRpmResultsSummaryEntry,
       "jnxRpmResSumCollection": jnxRpmResSumCollection,
       "jnxRpmResSumSent": jnxRpmResSumSent,
       "jnxRpmResSumReceived": jnxRpmResSumReceived,
       "jnxRpmResSumPercentLost": jnxRpmResSumPercentLost,
       "jnxRpmResSumDate": jnxRpmResSumDate,
       "jnxRpmResultsCalculatedTable": jnxRpmResultsCalculatedTable,
       "jnxRpmResultsCalculatedEntry": jnxRpmResultsCalculatedEntry,
       "jnxRpmResCalcSet": jnxRpmResCalcSet,
       "jnxRpmResCalcSamples": jnxRpmResCalcSamples,
       "jnxRpmResCalcMin": jnxRpmResCalcMin,
       "jnxRpmResCalcMax": jnxRpmResCalcMax,
       "jnxRpmResCalcAverage": jnxRpmResCalcAverage,
       "jnxRpmResCalcPkToPk": jnxRpmResCalcPkToPk,
       "jnxRpmResCalcStdDev": jnxRpmResCalcStdDev,
       "jnxRpmResCalcSum": jnxRpmResCalcSum,
       "jnxRpmHistorySampleTable": jnxRpmHistorySampleTable,
       "jnxRpmHistorySampleEntry": jnxRpmHistorySampleEntry,
       "jnxRpmHistSampleType": jnxRpmHistSampleType,
       "jnxRpmHistSampleValue": jnxRpmHistSampleValue,
       "jnxRpmHistSampleTsType": jnxRpmHistSampleTsType,
       "jnxRpmHistorySummaryTable": jnxRpmHistorySummaryTable,
       "jnxRpmHistorySummaryEntry": jnxRpmHistorySummaryEntry,
       "jnxRpmHistSumCollection": jnxRpmHistSumCollection,
       "jnxRpmHistSumSent": jnxRpmHistSumSent,
       "jnxRpmHistSumReceived": jnxRpmHistSumReceived,
       "jnxRpmHistSumPercentLost": jnxRpmHistSumPercentLost,
       "jnxRpmHistoryCalculatedTable": jnxRpmHistoryCalculatedTable,
       "jnxRpmHistoryCalculatedEntry": jnxRpmHistoryCalculatedEntry,
       "jnxRpmHistCalcSet": jnxRpmHistCalcSet,
       "jnxRpmHistCalcSamples": jnxRpmHistCalcSamples,
       "jnxRpmHistCalcMin": jnxRpmHistCalcMin,
       "jnxRpmHistCalcMax": jnxRpmHistCalcMax,
       "jnxRpmHistCalcAverage": jnxRpmHistCalcAverage,
       "jnxRpmHistCalcPkToPk": jnxRpmHistCalcPkToPk,
       "jnxRpmHistCalcStdDev": jnxRpmHistCalcStdDev,
       "jnxRpmHistCalcSum": jnxRpmHistCalcSum}
)
