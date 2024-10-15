# SNMP MIB module (A3COM-HUAWEI-DOT11-SA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/A3COM-HUAWEI-DOT11-SA-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:27:41 2024
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

(H3cDot11ChannelScopeType,
 H3cDot11ObjectIDType,
 H3cDot11RadioScopeType,
 H3cDot11SaIntfDevType,
 h3cDot11) = mibBuilder.importSymbols(
    "A3COM-HUAWEI-DOT11-REF-MIB",
    "H3cDot11ChannelScopeType",
    "H3cDot11ObjectIDType",
    "H3cDot11RadioScopeType",
    "H3cDot11SaIntfDevType",
    "h3cDot11")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

h3cDot11Sa = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 13)
)
h3cDot11Sa.setRevisions(
        ("2011-08-26 20:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cDot11SaCfgGroup_ObjectIdentity = ObjectIdentity
h3cDot11SaCfgGroup = _H3cDot11SaCfgGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 13, 1)
)
_H3cDot11SaCfgTable_Object = MibTable
h3cDot11SaCfgTable = _H3cDot11SaCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 13, 1, 1)
)
if mibBuilder.loadTexts:
    h3cDot11SaCfgTable.setStatus("current")
_H3cDot11SaCfgEntry_Object = MibTableRow
h3cDot11SaCfgEntry = _H3cDot11SaCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 13, 1, 1, 1)
)
h3cDot11SaCfgEntry.setIndexNames(
    (0, "A3COM-HUAWEI-DOT11-SA-MIB", "h3cDot11SaCfgRadioType"),
)
if mibBuilder.loadTexts:
    h3cDot11SaCfgEntry.setStatus("current")


class _H3cDot11SaCfgRadioType_Type(Integer32):
    """Custom type h3cDot11SaCfgRadioType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dot11a", 2),
          ("dot11bg", 1))
    )


_H3cDot11SaCfgRadioType_Type.__name__ = "Integer32"
_H3cDot11SaCfgRadioType_Object = MibTableColumn
h3cDot11SaCfgRadioType = _H3cDot11SaCfgRadioType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 13, 1, 1, 1, 1),
    _H3cDot11SaCfgRadioType_Type()
)
h3cDot11SaCfgRadioType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDot11SaCfgRadioType.setStatus("current")
_H3cDot11SaEnable_Type = TruthValue
_H3cDot11SaEnable_Object = MibTableColumn
h3cDot11SaEnable = _H3cDot11SaEnable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 13, 1, 1, 1, 2),
    _H3cDot11SaEnable_Type()
)
h3cDot11SaEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11SaEnable.setStatus("current")


class _H3cDot11SaRptDevType_Type(Bits):
    """Custom type h3cDot11SaRptDevType based on Bits"""
    namedValues = NamedValues(
        *(("bluetooth", 2),
          ("fixedFreqAudio", 6),
          ("fixedFreqCordlessPhone", 4),
          ("fixedFreqOthers", 3),
          ("fixedFreqVideo", 5),
          ("freqHopperCordlessBase", 8),
          ("freqHopperCordlessNetwork", 9),
          ("freqHopperOthers", 7),
          ("freqHopperXbox", 10),
          ("genericInterferer", 11),
          ("microwave", 0),
          ("microwaveInverter", 1))
    )

_H3cDot11SaRptDevType_Type.__name__ = "Bits"
_H3cDot11SaRptDevType_Object = MibTableColumn
h3cDot11SaRptDevType = _H3cDot11SaRptDevType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 13, 1, 1, 1, 3),
    _H3cDot11SaRptDevType_Type()
)
h3cDot11SaRptDevType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11SaRptDevType.setStatus("current")
_H3cDot11SaTrapDevEnable_Type = TruthValue
_H3cDot11SaTrapDevEnable_Object = MibTableColumn
h3cDot11SaTrapDevEnable = _H3cDot11SaTrapDevEnable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 13, 1, 1, 1, 4),
    _H3cDot11SaTrapDevEnable_Type()
)
h3cDot11SaTrapDevEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11SaTrapDevEnable.setStatus("current")


class _H3cDot11SaTrapDevType_Type(Bits):
    """Custom type h3cDot11SaTrapDevType based on Bits"""
    namedValues = NamedValues(
        *(("bluetooth", 2),
          ("fixedFreqAudio", 6),
          ("fixedFreqCordlessPhone", 4),
          ("fixedFreqOthers", 3),
          ("fixedFreqVideo", 5),
          ("freqHopperCordlessBase", 8),
          ("freqHopperCordlessNetwork", 9),
          ("freqHopperOthers", 7),
          ("freqHopperXbox", 10),
          ("genericInterferer", 11),
          ("microwave", 0),
          ("microwaveInverter", 1))
    )

_H3cDot11SaTrapDevType_Type.__name__ = "Bits"
_H3cDot11SaTrapDevType_Object = MibTableColumn
h3cDot11SaTrapDevType = _H3cDot11SaTrapDevType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 13, 1, 1, 1, 5),
    _H3cDot11SaTrapDevType_Type()
)
h3cDot11SaTrapDevType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11SaTrapDevType.setStatus("current")
_H3cDot11SaTrapAQEnable_Type = TruthValue
_H3cDot11SaTrapAQEnable_Object = MibTableColumn
h3cDot11SaTrapAQEnable = _H3cDot11SaTrapAQEnable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 13, 1, 1, 1, 6),
    _H3cDot11SaTrapAQEnable_Type()
)
h3cDot11SaTrapAQEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11SaTrapAQEnable.setStatus("current")


class _H3cDot11SaTrapAQThreshold_Type(Integer32):
    """Custom type h3cDot11SaTrapAQThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_H3cDot11SaTrapAQThreshold_Type.__name__ = "Integer32"
_H3cDot11SaTrapAQThreshold_Object = MibTableColumn
h3cDot11SaTrapAQThreshold = _H3cDot11SaTrapAQThreshold_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 13, 1, 1, 1, 7),
    _H3cDot11SaTrapAQThreshold_Type()
)
h3cDot11SaTrapAQThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11SaTrapAQThreshold.setStatus("current")
_H3cDot11SaDrivenRRMEnable_Type = TruthValue
_H3cDot11SaDrivenRRMEnable_Object = MibTableColumn
h3cDot11SaDrivenRRMEnable = _H3cDot11SaDrivenRRMEnable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 13, 1, 1, 1, 8),
    _H3cDot11SaDrivenRRMEnable_Type()
)
h3cDot11SaDrivenRRMEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11SaDrivenRRMEnable.setStatus("current")


class _H3cDot11SaDrivenRRMSnt_Type(Integer32):
    """Custom type h3cDot11SaDrivenRRMSnt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("high", 3),
          ("low", 1),
          ("medium", 2))
    )


_H3cDot11SaDrivenRRMSnt_Type.__name__ = "Integer32"
_H3cDot11SaDrivenRRMSnt_Object = MibTableColumn
h3cDot11SaDrivenRRMSnt = _H3cDot11SaDrivenRRMSnt_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 13, 1, 1, 1, 9),
    _H3cDot11SaDrivenRRMSnt_Type()
)
h3cDot11SaDrivenRRMSnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11SaDrivenRRMSnt.setStatus("current")
_H3cDot11SaStatusGroup_ObjectIdentity = ObjectIdentity
h3cDot11SaStatusGroup = _H3cDot11SaStatusGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 13, 2)
)
_H3cDot11SaRtFFTDataTable_Object = MibTable
h3cDot11SaRtFFTDataTable = _H3cDot11SaRtFFTDataTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 13, 2, 1)
)
if mibBuilder.loadTexts:
    h3cDot11SaRtFFTDataTable.setStatus("current")
_H3cDot11SaRtFFTDataEntry_Object = MibTableRow
h3cDot11SaRtFFTDataEntry = _H3cDot11SaRtFFTDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 13, 2, 1, 1)
)
h3cDot11SaRtFFTDataEntry.setIndexNames(
    (0, "A3COM-HUAWEI-DOT11-SA-MIB", "h3cDot11SaAPID"),
    (0, "A3COM-HUAWEI-DOT11-SA-MIB", "h3cDot11SaRadioID"),
    (0, "A3COM-HUAWEI-DOT11-SA-MIB", "h3cDot11SaRtDataGroupID"),
    (0, "A3COM-HUAWEI-DOT11-SA-MIB", "h3cDot11SaFrequency"),
)
if mibBuilder.loadTexts:
    h3cDot11SaRtFFTDataEntry.setStatus("current")
_H3cDot11SaAPID_Type = H3cDot11ObjectIDType
_H3cDot11SaAPID_Object = MibTableColumn
h3cDot11SaAPID = _H3cDot11SaAPID_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 13, 2, 1, 1, 1),
    _H3cDot11SaAPID_Type()
)
h3cDot11SaAPID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDot11SaAPID.setStatus("current")
_H3cDot11SaRadioID_Type = H3cDot11RadioScopeType
_H3cDot11SaRadioID_Object = MibTableColumn
h3cDot11SaRadioID = _H3cDot11SaRadioID_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 13, 2, 1, 1, 2),
    _H3cDot11SaRadioID_Type()
)
h3cDot11SaRadioID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDot11SaRadioID.setStatus("current")
_H3cDot11SaRtDataGroupID_Type = Integer32
_H3cDot11SaRtDataGroupID_Object = MibTableColumn
h3cDot11SaRtDataGroupID = _H3cDot11SaRtDataGroupID_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 13, 2, 1, 1, 3),
    _H3cDot11SaRtDataGroupID_Type()
)
h3cDot11SaRtDataGroupID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDot11SaRtDataGroupID.setStatus("current")
_H3cDot11SaFrequency_Type = Integer32
_H3cDot11SaFrequency_Object = MibTableColumn
h3cDot11SaFrequency = _H3cDot11SaFrequency_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 13, 2, 1, 1, 4),
    _H3cDot11SaFrequency_Type()
)
h3cDot11SaFrequency.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDot11SaFrequency.setStatus("current")
_H3cDot11SaRtFreqPower_Type = Integer32
_H3cDot11SaRtFreqPower_Object = MibTableColumn
h3cDot11SaRtFreqPower = _H3cDot11SaRtFreqPower_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 13, 2, 1, 1, 5),
    _H3cDot11SaRtFreqPower_Type()
)
h3cDot11SaRtFreqPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11SaRtFreqPower.setStatus("current")
_H3cDot11SaRtFreqMaxPower_Type = Integer32
_H3cDot11SaRtFreqMaxPower_Object = MibTableColumn
h3cDot11SaRtFreqMaxPower = _H3cDot11SaRtFreqMaxPower_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 13, 2, 1, 1, 6),
    _H3cDot11SaRtFreqMaxPower_Type()
)
h3cDot11SaRtFreqMaxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11SaRtFreqMaxPower.setStatus("current")
_H3cDot11SaRtFreqDutyCycle_Type = Integer32
_H3cDot11SaRtFreqDutyCycle_Object = MibTableColumn
h3cDot11SaRtFreqDutyCycle = _H3cDot11SaRtFreqDutyCycle_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 13, 2, 1, 1, 7),
    _H3cDot11SaRtFreqDutyCycle_Type()
)
h3cDot11SaRtFreqDutyCycle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11SaRtFreqDutyCycle.setStatus("current")
_H3cDot11SaRtFreqDataSeqNo_Type = Unsigned32
_H3cDot11SaRtFreqDataSeqNo_Object = MibTableColumn
h3cDot11SaRtFreqDataSeqNo = _H3cDot11SaRtFreqDataSeqNo_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 13, 2, 1, 1, 8),
    _H3cDot11SaRtFreqDataSeqNo_Type()
)
h3cDot11SaRtFreqDataSeqNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11SaRtFreqDataSeqNo.setStatus("current")
_H3cDot11SaIntfDevTable_Object = MibTable
h3cDot11SaIntfDevTable = _H3cDot11SaIntfDevTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 13, 2, 2)
)
if mibBuilder.loadTexts:
    h3cDot11SaIntfDevTable.setStatus("current")
_H3cDot11SaIntfDevEntry_Object = MibTableRow
h3cDot11SaIntfDevEntry = _H3cDot11SaIntfDevEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 13, 2, 2, 1)
)
h3cDot11SaIntfDevEntry.setIndexNames(
    (0, "A3COM-HUAWEI-DOT11-SA-MIB", "h3cDot11SaAPID"),
    (0, "A3COM-HUAWEI-DOT11-SA-MIB", "h3cDot11SaRadioID"),
    (0, "A3COM-HUAWEI-DOT11-SA-MIB", "h3cDot11SaDevID"),
)
if mibBuilder.loadTexts:
    h3cDot11SaIntfDevEntry.setStatus("current")
_H3cDot11SaDevID_Type = Integer32
_H3cDot11SaDevID_Object = MibTableColumn
h3cDot11SaDevID = _H3cDot11SaDevID_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 13, 2, 2, 1, 1),
    _H3cDot11SaDevID_Type()
)
h3cDot11SaDevID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDot11SaDevID.setStatus("current")
_H3cDot11SaDevType_Type = H3cDot11SaIntfDevType
_H3cDot11SaDevType_Object = MibTableColumn
h3cDot11SaDevType = _H3cDot11SaDevType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 13, 2, 2, 1, 2),
    _H3cDot11SaDevType_Type()
)
h3cDot11SaDevType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11SaDevType.setStatus("current")
_H3cDot11SaDevSI_Type = Integer32
_H3cDot11SaDevSI_Object = MibTableColumn
h3cDot11SaDevSI = _H3cDot11SaDevSI_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 13, 2, 2, 1, 3),
    _H3cDot11SaDevSI_Type()
)
h3cDot11SaDevSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11SaDevSI.setStatus("current")
_H3cDot11SaDevRSSI_Type = Integer32
_H3cDot11SaDevRSSI_Object = MibTableColumn
h3cDot11SaDevRSSI = _H3cDot11SaDevRSSI_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 13, 2, 2, 1, 4),
    _H3cDot11SaDevRSSI_Type()
)
h3cDot11SaDevRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11SaDevRSSI.setStatus("current")
_H3cDot11SaDevDutyCycle_Type = Integer32
_H3cDot11SaDevDutyCycle_Object = MibTableColumn
h3cDot11SaDevDutyCycle = _H3cDot11SaDevDutyCycle_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 13, 2, 2, 1, 5),
    _H3cDot11SaDevDutyCycle_Type()
)
h3cDot11SaDevDutyCycle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11SaDevDutyCycle.setStatus("current")
_H3cDot11SaDevAffectedChls_Type = OctetString
_H3cDot11SaDevAffectedChls_Object = MibTableColumn
h3cDot11SaDevAffectedChls = _H3cDot11SaDevAffectedChls_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 13, 2, 2, 1, 6),
    _H3cDot11SaDevAffectedChls_Type()
)
h3cDot11SaDevAffectedChls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11SaDevAffectedChls.setStatus("current")
_H3cDot11SaDevDetectedTime_Type = DateAndTime
_H3cDot11SaDevDetectedTime_Object = MibTableColumn
h3cDot11SaDevDetectedTime = _H3cDot11SaDevDetectedTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 13, 2, 2, 1, 7),
    _H3cDot11SaDevDetectedTime_Type()
)
h3cDot11SaDevDetectedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11SaDevDetectedTime.setStatus("current")
_H3cDot11SaAirQualityTable_Object = MibTable
h3cDot11SaAirQualityTable = _H3cDot11SaAirQualityTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 13, 2, 3)
)
if mibBuilder.loadTexts:
    h3cDot11SaAirQualityTable.setStatus("current")
_H3cDot11SaAirQualityEntry_Object = MibTableRow
h3cDot11SaAirQualityEntry = _H3cDot11SaAirQualityEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 13, 2, 3, 1)
)
h3cDot11SaAirQualityEntry.setIndexNames(
    (0, "A3COM-HUAWEI-DOT11-SA-MIB", "h3cDot11SaAPID"),
    (0, "A3COM-HUAWEI-DOT11-SA-MIB", "h3cDot11SaRadioID"),
    (0, "A3COM-HUAWEI-DOT11-SA-MIB", "h3cDot11SaChlNum"),
)
if mibBuilder.loadTexts:
    h3cDot11SaAirQualityEntry.setStatus("current")
_H3cDot11SaChlNum_Type = H3cDot11ChannelScopeType
_H3cDot11SaChlNum_Object = MibTableColumn
h3cDot11SaChlNum = _H3cDot11SaChlNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 13, 2, 3, 1, 1),
    _H3cDot11SaChlNum_Type()
)
h3cDot11SaChlNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDot11SaChlNum.setStatus("current")
_H3cDot11SaAvgQuality_Type = Integer32
_H3cDot11SaAvgQuality_Object = MibTableColumn
h3cDot11SaAvgQuality = _H3cDot11SaAvgQuality_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 13, 2, 3, 1, 2),
    _H3cDot11SaAvgQuality_Type()
)
h3cDot11SaAvgQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11SaAvgQuality.setStatus("current")
_H3cDot11SaMinQuality_Type = Integer32
_H3cDot11SaMinQuality_Object = MibTableColumn
h3cDot11SaMinQuality = _H3cDot11SaMinQuality_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 13, 2, 3, 1, 3),
    _H3cDot11SaMinQuality_Type()
)
h3cDot11SaMinQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11SaMinQuality.setStatus("current")
_H3cDot11SaIntfDevNum_Type = Integer32
_H3cDot11SaIntfDevNum_Object = MibTableColumn
h3cDot11SaIntfDevNum = _H3cDot11SaIntfDevNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 13, 2, 3, 1, 4),
    _H3cDot11SaIntfDevNum_Type()
)
h3cDot11SaIntfDevNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11SaIntfDevNum.setStatus("current")
_H3cDot11SaWiFiUtil_Type = Integer32
_H3cDot11SaWiFiUtil_Object = MibTableColumn
h3cDot11SaWiFiUtil = _H3cDot11SaWiFiUtil_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 13, 2, 3, 1, 5),
    _H3cDot11SaWiFiUtil_Type()
)
h3cDot11SaWiFiUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11SaWiFiUtil.setStatus("current")
_H3cDot11SaNonWiFiUtil_Type = Integer32
_H3cDot11SaNonWiFiUtil_Object = MibTableColumn
h3cDot11SaNonWiFiUtil = _H3cDot11SaNonWiFiUtil_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 13, 2, 3, 1, 6),
    _H3cDot11SaNonWiFiUtil_Type()
)
h3cDot11SaNonWiFiUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11SaNonWiFiUtil.setStatus("current")
_H3cDot11SaNoiseFloor_Type = Integer32
_H3cDot11SaNoiseFloor_Object = MibTableColumn
h3cDot11SaNoiseFloor = _H3cDot11SaNoiseFloor_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 13, 2, 3, 1, 7),
    _H3cDot11SaNoiseFloor_Type()
)
h3cDot11SaNoiseFloor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11SaNoiseFloor.setStatus("current")
_H3cDot11SaNotifyGroup_ObjectIdentity = ObjectIdentity
h3cDot11SaNotifyGroup = _H3cDot11SaNotifyGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 13, 3)
)
_H3cDot11SaTraps_ObjectIdentity = ObjectIdentity
h3cDot11SaTraps = _H3cDot11SaTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 13, 3, 0)
)
_H3cDot11SaTrapVars_ObjectIdentity = ObjectIdentity
h3cDot11SaTrapVars = _H3cDot11SaTrapVars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 13, 3, 1)
)
_H3cDot11SaTrapAPID_Type = H3cDot11ObjectIDType
_H3cDot11SaTrapAPID_Object = MibScalar
h3cDot11SaTrapAPID = _H3cDot11SaTrapAPID_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 13, 3, 1, 1),
    _H3cDot11SaTrapAPID_Type()
)
h3cDot11SaTrapAPID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cDot11SaTrapAPID.setStatus("current")
_H3cDot11SaTrapRadioID_Type = H3cDot11RadioScopeType
_H3cDot11SaTrapRadioID_Object = MibScalar
h3cDot11SaTrapRadioID = _H3cDot11SaTrapRadioID_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 13, 3, 1, 2),
    _H3cDot11SaTrapRadioID_Type()
)
h3cDot11SaTrapRadioID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cDot11SaTrapRadioID.setStatus("current")
_H3cDot11SaTrapDevID_Type = Integer32
_H3cDot11SaTrapDevID_Object = MibScalar
h3cDot11SaTrapDevID = _H3cDot11SaTrapDevID_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 13, 3, 1, 3),
    _H3cDot11SaTrapDevID_Type()
)
h3cDot11SaTrapDevID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cDot11SaTrapDevID.setStatus("current")
_H3cDot11SaTrapIntfDevType_Type = H3cDot11SaIntfDevType
_H3cDot11SaTrapIntfDevType_Object = MibScalar
h3cDot11SaTrapIntfDevType = _H3cDot11SaTrapIntfDevType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 13, 3, 1, 4),
    _H3cDot11SaTrapIntfDevType_Type()
)
h3cDot11SaTrapIntfDevType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cDot11SaTrapIntfDevType.setStatus("current")
_H3cDot11APTrapDevSI_Type = Integer32
_H3cDot11APTrapDevSI_Object = MibScalar
h3cDot11APTrapDevSI = _H3cDot11APTrapDevSI_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 13, 3, 1, 5),
    _H3cDot11APTrapDevSI_Type()
)
h3cDot11APTrapDevSI.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cDot11APTrapDevSI.setStatus("current")
_H3cDot11SaTrapDevRSSI_Type = Integer32
_H3cDot11SaTrapDevRSSI_Object = MibScalar
h3cDot11SaTrapDevRSSI = _H3cDot11SaTrapDevRSSI_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 13, 3, 1, 6),
    _H3cDot11SaTrapDevRSSI_Type()
)
h3cDot11SaTrapDevRSSI.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cDot11SaTrapDevRSSI.setStatus("current")
_H3cDot11APTrapDevDC_Type = Integer32
_H3cDot11APTrapDevDC_Object = MibScalar
h3cDot11APTrapDevDC = _H3cDot11APTrapDevDC_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 13, 3, 1, 7),
    _H3cDot11APTrapDevDC_Type()
)
h3cDot11APTrapDevDC.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cDot11APTrapDevDC.setStatus("current")
_H3cDot11APTrapDevChls_Type = OctetString
_H3cDot11APTrapDevChls_Object = MibScalar
h3cDot11APTrapDevChls = _H3cDot11APTrapDevChls_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 13, 3, 1, 8),
    _H3cDot11APTrapDevChls_Type()
)
h3cDot11APTrapDevChls.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cDot11APTrapDevChls.setStatus("current")
_H3cDot11APTrapDevDctTime_Type = DateAndTime
_H3cDot11APTrapDevDctTime_Object = MibScalar
h3cDot11APTrapDevDctTime = _H3cDot11APTrapDevDctTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 13, 3, 1, 9),
    _H3cDot11APTrapDevDctTime_Type()
)
h3cDot11APTrapDevDctTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cDot11APTrapDevDctTime.setStatus("current")
_H3cDot11SaTrapChlNum_Type = H3cDot11ChannelScopeType
_H3cDot11SaTrapChlNum_Object = MibScalar
h3cDot11SaTrapChlNum = _H3cDot11SaTrapChlNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 13, 3, 1, 10),
    _H3cDot11SaTrapChlNum_Type()
)
h3cDot11SaTrapChlNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cDot11SaTrapChlNum.setStatus("current")
_H3cDot11SaTrapChlQlt_Type = Integer32
_H3cDot11SaTrapChlQlt_Object = MibScalar
h3cDot11SaTrapChlQlt = _H3cDot11SaTrapChlQlt_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 13, 3, 1, 11),
    _H3cDot11SaTrapChlQlt_Type()
)
h3cDot11SaTrapChlQlt.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cDot11SaTrapChlQlt.setStatus("current")
_H3cDot11SaTrapChlIntfNum_Type = Integer32
_H3cDot11SaTrapChlIntfNum_Object = MibScalar
h3cDot11SaTrapChlIntfNum = _H3cDot11SaTrapChlIntfNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 13, 3, 1, 12),
    _H3cDot11SaTrapChlIntfNum_Type()
)
h3cDot11SaTrapChlIntfNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cDot11SaTrapChlIntfNum.setStatus("current")

# Managed Objects groups


# Notification objects

h3cDot11SaIntfDevDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 13, 3, 0, 1)
)
h3cDot11SaIntfDevDetected.setObjects(
      *(("A3COM-HUAWEI-DOT11-SA-MIB", "h3cDot11SaTrapAPID"),
        ("A3COM-HUAWEI-DOT11-SA-MIB", "h3cDot11SaTrapRadioID"),
        ("A3COM-HUAWEI-DOT11-SA-MIB", "h3cDot11SaTrapDevID"),
        ("A3COM-HUAWEI-DOT11-SA-MIB", "h3cDot11SaTrapIntfDevType"),
        ("A3COM-HUAWEI-DOT11-SA-MIB", "h3cDot11APTrapDevSI"),
        ("A3COM-HUAWEI-DOT11-SA-MIB", "h3cDot11SaTrapDevRSSI"),
        ("A3COM-HUAWEI-DOT11-SA-MIB", "h3cDot11APTrapDevDC"),
        ("A3COM-HUAWEI-DOT11-SA-MIB", "h3cDot11APTrapDevChls"),
        ("A3COM-HUAWEI-DOT11-SA-MIB", "h3cDot11APTrapDevDctTime"))
)
if mibBuilder.loadTexts:
    h3cDot11SaIntfDevDetected.setStatus(
        "current"
    )

h3cDot11SaIntfDevDisappear = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 13, 3, 0, 2)
)
h3cDot11SaIntfDevDisappear.setObjects(
      *(("A3COM-HUAWEI-DOT11-SA-MIB", "h3cDot11SaTrapAPID"),
        ("A3COM-HUAWEI-DOT11-SA-MIB", "h3cDot11SaTrapRadioID"),
        ("A3COM-HUAWEI-DOT11-SA-MIB", "h3cDot11SaTrapDevID"),
        ("A3COM-HUAWEI-DOT11-SA-MIB", "h3cDot11SaTrapIntfDevType"))
)
if mibBuilder.loadTexts:
    h3cDot11SaIntfDevDisappear.setStatus(
        "current"
    )

h3cDot11SaChlQltLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 13, 3, 0, 3)
)
h3cDot11SaChlQltLow.setObjects(
      *(("A3COM-HUAWEI-DOT11-SA-MIB", "h3cDot11SaTrapAPID"),
        ("A3COM-HUAWEI-DOT11-SA-MIB", "h3cDot11SaTrapRadioID"),
        ("A3COM-HUAWEI-DOT11-SA-MIB", "h3cDot11SaTrapChlNum"),
        ("A3COM-HUAWEI-DOT11-SA-MIB", "h3cDot11SaTrapChlQlt"),
        ("A3COM-HUAWEI-DOT11-SA-MIB", "h3cDot11SaTrapChlIntfNum"))
)
if mibBuilder.loadTexts:
    h3cDot11SaChlQltLow.setStatus(
        "current"
    )

h3cDot11SaChlQltRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 13, 3, 0, 4)
)
h3cDot11SaChlQltRecover.setObjects(
      *(("A3COM-HUAWEI-DOT11-SA-MIB", "h3cDot11SaTrapAPID"),
        ("A3COM-HUAWEI-DOT11-SA-MIB", "h3cDot11SaTrapRadioID"),
        ("A3COM-HUAWEI-DOT11-SA-MIB", "h3cDot11SaTrapChlNum"),
        ("A3COM-HUAWEI-DOT11-SA-MIB", "h3cDot11SaTrapChlQlt"),
        ("A3COM-HUAWEI-DOT11-SA-MIB", "h3cDot11SaTrapChlIntfNum"))
)
if mibBuilder.loadTexts:
    h3cDot11SaChlQltRecover.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM-HUAWEI-DOT11-SA-MIB",
    **{"h3cDot11Sa": h3cDot11Sa,
       "h3cDot11SaCfgGroup": h3cDot11SaCfgGroup,
       "h3cDot11SaCfgTable": h3cDot11SaCfgTable,
       "h3cDot11SaCfgEntry": h3cDot11SaCfgEntry,
       "h3cDot11SaCfgRadioType": h3cDot11SaCfgRadioType,
       "h3cDot11SaEnable": h3cDot11SaEnable,
       "h3cDot11SaRptDevType": h3cDot11SaRptDevType,
       "h3cDot11SaTrapDevEnable": h3cDot11SaTrapDevEnable,
       "h3cDot11SaTrapDevType": h3cDot11SaTrapDevType,
       "h3cDot11SaTrapAQEnable": h3cDot11SaTrapAQEnable,
       "h3cDot11SaTrapAQThreshold": h3cDot11SaTrapAQThreshold,
       "h3cDot11SaDrivenRRMEnable": h3cDot11SaDrivenRRMEnable,
       "h3cDot11SaDrivenRRMSnt": h3cDot11SaDrivenRRMSnt,
       "h3cDot11SaStatusGroup": h3cDot11SaStatusGroup,
       "h3cDot11SaRtFFTDataTable": h3cDot11SaRtFFTDataTable,
       "h3cDot11SaRtFFTDataEntry": h3cDot11SaRtFFTDataEntry,
       "h3cDot11SaAPID": h3cDot11SaAPID,
       "h3cDot11SaRadioID": h3cDot11SaRadioID,
       "h3cDot11SaRtDataGroupID": h3cDot11SaRtDataGroupID,
       "h3cDot11SaFrequency": h3cDot11SaFrequency,
       "h3cDot11SaRtFreqPower": h3cDot11SaRtFreqPower,
       "h3cDot11SaRtFreqMaxPower": h3cDot11SaRtFreqMaxPower,
       "h3cDot11SaRtFreqDutyCycle": h3cDot11SaRtFreqDutyCycle,
       "h3cDot11SaRtFreqDataSeqNo": h3cDot11SaRtFreqDataSeqNo,
       "h3cDot11SaIntfDevTable": h3cDot11SaIntfDevTable,
       "h3cDot11SaIntfDevEntry": h3cDot11SaIntfDevEntry,
       "h3cDot11SaDevID": h3cDot11SaDevID,
       "h3cDot11SaDevType": h3cDot11SaDevType,
       "h3cDot11SaDevSI": h3cDot11SaDevSI,
       "h3cDot11SaDevRSSI": h3cDot11SaDevRSSI,
       "h3cDot11SaDevDutyCycle": h3cDot11SaDevDutyCycle,
       "h3cDot11SaDevAffectedChls": h3cDot11SaDevAffectedChls,
       "h3cDot11SaDevDetectedTime": h3cDot11SaDevDetectedTime,
       "h3cDot11SaAirQualityTable": h3cDot11SaAirQualityTable,
       "h3cDot11SaAirQualityEntry": h3cDot11SaAirQualityEntry,
       "h3cDot11SaChlNum": h3cDot11SaChlNum,
       "h3cDot11SaAvgQuality": h3cDot11SaAvgQuality,
       "h3cDot11SaMinQuality": h3cDot11SaMinQuality,
       "h3cDot11SaIntfDevNum": h3cDot11SaIntfDevNum,
       "h3cDot11SaWiFiUtil": h3cDot11SaWiFiUtil,
       "h3cDot11SaNonWiFiUtil": h3cDot11SaNonWiFiUtil,
       "h3cDot11SaNoiseFloor": h3cDot11SaNoiseFloor,
       "h3cDot11SaNotifyGroup": h3cDot11SaNotifyGroup,
       "h3cDot11SaTraps": h3cDot11SaTraps,
       "h3cDot11SaIntfDevDetected": h3cDot11SaIntfDevDetected,
       "h3cDot11SaIntfDevDisappear": h3cDot11SaIntfDevDisappear,
       "h3cDot11SaChlQltLow": h3cDot11SaChlQltLow,
       "h3cDot11SaChlQltRecover": h3cDot11SaChlQltRecover,
       "h3cDot11SaTrapVars": h3cDot11SaTrapVars,
       "h3cDot11SaTrapAPID": h3cDot11SaTrapAPID,
       "h3cDot11SaTrapRadioID": h3cDot11SaTrapRadioID,
       "h3cDot11SaTrapDevID": h3cDot11SaTrapDevID,
       "h3cDot11SaTrapIntfDevType": h3cDot11SaTrapIntfDevType,
       "h3cDot11APTrapDevSI": h3cDot11APTrapDevSI,
       "h3cDot11SaTrapDevRSSI": h3cDot11SaTrapDevRSSI,
       "h3cDot11APTrapDevDC": h3cDot11APTrapDevDC,
       "h3cDot11APTrapDevChls": h3cDot11APTrapDevChls,
       "h3cDot11APTrapDevDctTime": h3cDot11APTrapDevDctTime,
       "h3cDot11SaTrapChlNum": h3cDot11SaTrapChlNum,
       "h3cDot11SaTrapChlQlt": h3cDot11SaTrapChlQlt,
       "h3cDot11SaTrapChlIntfNum": h3cDot11SaTrapChlIntfNum}
)
