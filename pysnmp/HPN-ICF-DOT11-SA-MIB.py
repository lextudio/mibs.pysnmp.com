# SNMP MIB module (HPN-ICF-DOT11-SA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-DOT11-SA-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:59:54 2024
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

(HpnicfDot11ChannelScopeType,
 HpnicfDot11ObjectIDType,
 HpnicfDot11RadioScopeType,
 HpnicfDot11SaIntfDevType,
 hpnicfDot11) = mibBuilder.importSymbols(
    "HPN-ICF-DOT11-REF-MIB",
    "HpnicfDot11ChannelScopeType",
    "HpnicfDot11ObjectIDType",
    "HpnicfDot11RadioScopeType",
    "HpnicfDot11SaIntfDevType",
    "hpnicfDot11")

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

hpnicfDot11Sa = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 13)
)
hpnicfDot11Sa.setRevisions(
        ("2011-08-26 20:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpnicfDot11SaCfgGroup_ObjectIdentity = ObjectIdentity
hpnicfDot11SaCfgGroup = _HpnicfDot11SaCfgGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 13, 1)
)
_HpnicfDot11SaCfgTable_Object = MibTable
hpnicfDot11SaCfgTable = _HpnicfDot11SaCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 13, 1, 1)
)
if mibBuilder.loadTexts:
    hpnicfDot11SaCfgTable.setStatus("current")
_HpnicfDot11SaCfgEntry_Object = MibTableRow
hpnicfDot11SaCfgEntry = _HpnicfDot11SaCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 13, 1, 1, 1)
)
hpnicfDot11SaCfgEntry.setIndexNames(
    (0, "HPN-ICF-DOT11-SA-MIB", "hpnicfDot11SaCfgRadioType"),
)
if mibBuilder.loadTexts:
    hpnicfDot11SaCfgEntry.setStatus("current")


class _HpnicfDot11SaCfgRadioType_Type(Integer32):
    """Custom type hpnicfDot11SaCfgRadioType based on Integer32"""
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


_HpnicfDot11SaCfgRadioType_Type.__name__ = "Integer32"
_HpnicfDot11SaCfgRadioType_Object = MibTableColumn
hpnicfDot11SaCfgRadioType = _HpnicfDot11SaCfgRadioType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 13, 1, 1, 1, 1),
    _HpnicfDot11SaCfgRadioType_Type()
)
hpnicfDot11SaCfgRadioType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDot11SaCfgRadioType.setStatus("current")
_HpnicfDot11SaEnable_Type = TruthValue
_HpnicfDot11SaEnable_Object = MibTableColumn
hpnicfDot11SaEnable = _HpnicfDot11SaEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 13, 1, 1, 1, 2),
    _HpnicfDot11SaEnable_Type()
)
hpnicfDot11SaEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11SaEnable.setStatus("current")


class _HpnicfDot11SaRptDevType_Type(Bits):
    """Custom type hpnicfDot11SaRptDevType based on Bits"""
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

_HpnicfDot11SaRptDevType_Type.__name__ = "Bits"
_HpnicfDot11SaRptDevType_Object = MibTableColumn
hpnicfDot11SaRptDevType = _HpnicfDot11SaRptDevType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 13, 1, 1, 1, 3),
    _HpnicfDot11SaRptDevType_Type()
)
hpnicfDot11SaRptDevType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11SaRptDevType.setStatus("current")
_HpnicfDot11SaTrapDevEnable_Type = TruthValue
_HpnicfDot11SaTrapDevEnable_Object = MibTableColumn
hpnicfDot11SaTrapDevEnable = _HpnicfDot11SaTrapDevEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 13, 1, 1, 1, 4),
    _HpnicfDot11SaTrapDevEnable_Type()
)
hpnicfDot11SaTrapDevEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11SaTrapDevEnable.setStatus("current")


class _HpnicfDot11SaTrapDevType_Type(Bits):
    """Custom type hpnicfDot11SaTrapDevType based on Bits"""
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

_HpnicfDot11SaTrapDevType_Type.__name__ = "Bits"
_HpnicfDot11SaTrapDevType_Object = MibTableColumn
hpnicfDot11SaTrapDevType = _HpnicfDot11SaTrapDevType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 13, 1, 1, 1, 5),
    _HpnicfDot11SaTrapDevType_Type()
)
hpnicfDot11SaTrapDevType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11SaTrapDevType.setStatus("current")
_HpnicfDot11SaTrapAQEnable_Type = TruthValue
_HpnicfDot11SaTrapAQEnable_Object = MibTableColumn
hpnicfDot11SaTrapAQEnable = _HpnicfDot11SaTrapAQEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 13, 1, 1, 1, 6),
    _HpnicfDot11SaTrapAQEnable_Type()
)
hpnicfDot11SaTrapAQEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11SaTrapAQEnable.setStatus("current")


class _HpnicfDot11SaTrapAQThreshold_Type(Integer32):
    """Custom type hpnicfDot11SaTrapAQThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HpnicfDot11SaTrapAQThreshold_Type.__name__ = "Integer32"
_HpnicfDot11SaTrapAQThreshold_Object = MibTableColumn
hpnicfDot11SaTrapAQThreshold = _HpnicfDot11SaTrapAQThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 13, 1, 1, 1, 7),
    _HpnicfDot11SaTrapAQThreshold_Type()
)
hpnicfDot11SaTrapAQThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11SaTrapAQThreshold.setStatus("current")
_HpnicfDot11SaDrivenRRMEnable_Type = TruthValue
_HpnicfDot11SaDrivenRRMEnable_Object = MibTableColumn
hpnicfDot11SaDrivenRRMEnable = _HpnicfDot11SaDrivenRRMEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 13, 1, 1, 1, 8),
    _HpnicfDot11SaDrivenRRMEnable_Type()
)
hpnicfDot11SaDrivenRRMEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11SaDrivenRRMEnable.setStatus("current")


class _HpnicfDot11SaDrivenRRMSnt_Type(Integer32):
    """Custom type hpnicfDot11SaDrivenRRMSnt based on Integer32"""
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


_HpnicfDot11SaDrivenRRMSnt_Type.__name__ = "Integer32"
_HpnicfDot11SaDrivenRRMSnt_Object = MibTableColumn
hpnicfDot11SaDrivenRRMSnt = _HpnicfDot11SaDrivenRRMSnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 13, 1, 1, 1, 9),
    _HpnicfDot11SaDrivenRRMSnt_Type()
)
hpnicfDot11SaDrivenRRMSnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11SaDrivenRRMSnt.setStatus("current")
_HpnicfDot11SaStatusGroup_ObjectIdentity = ObjectIdentity
hpnicfDot11SaStatusGroup = _HpnicfDot11SaStatusGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 13, 2)
)
_HpnicfDot11SaRtFFTDataTable_Object = MibTable
hpnicfDot11SaRtFFTDataTable = _HpnicfDot11SaRtFFTDataTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 13, 2, 1)
)
if mibBuilder.loadTexts:
    hpnicfDot11SaRtFFTDataTable.setStatus("current")
_HpnicfDot11SaRtFFTDataEntry_Object = MibTableRow
hpnicfDot11SaRtFFTDataEntry = _HpnicfDot11SaRtFFTDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 13, 2, 1, 1)
)
hpnicfDot11SaRtFFTDataEntry.setIndexNames(
    (0, "HPN-ICF-DOT11-SA-MIB", "hpnicfDot11SaAPID"),
    (0, "HPN-ICF-DOT11-SA-MIB", "hpnicfDot11SaRadioID"),
    (0, "HPN-ICF-DOT11-SA-MIB", "hpnicfDot11SaRtDataGroupID"),
    (0, "HPN-ICF-DOT11-SA-MIB", "hpnicfDot11SaFrequency"),
)
if mibBuilder.loadTexts:
    hpnicfDot11SaRtFFTDataEntry.setStatus("current")
_HpnicfDot11SaAPID_Type = HpnicfDot11ObjectIDType
_HpnicfDot11SaAPID_Object = MibTableColumn
hpnicfDot11SaAPID = _HpnicfDot11SaAPID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 13, 2, 1, 1, 1),
    _HpnicfDot11SaAPID_Type()
)
hpnicfDot11SaAPID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDot11SaAPID.setStatus("current")
_HpnicfDot11SaRadioID_Type = HpnicfDot11RadioScopeType
_HpnicfDot11SaRadioID_Object = MibTableColumn
hpnicfDot11SaRadioID = _HpnicfDot11SaRadioID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 13, 2, 1, 1, 2),
    _HpnicfDot11SaRadioID_Type()
)
hpnicfDot11SaRadioID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDot11SaRadioID.setStatus("current")
_HpnicfDot11SaRtDataGroupID_Type = Integer32
_HpnicfDot11SaRtDataGroupID_Object = MibTableColumn
hpnicfDot11SaRtDataGroupID = _HpnicfDot11SaRtDataGroupID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 13, 2, 1, 1, 3),
    _HpnicfDot11SaRtDataGroupID_Type()
)
hpnicfDot11SaRtDataGroupID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDot11SaRtDataGroupID.setStatus("current")
_HpnicfDot11SaFrequency_Type = Integer32
_HpnicfDot11SaFrequency_Object = MibTableColumn
hpnicfDot11SaFrequency = _HpnicfDot11SaFrequency_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 13, 2, 1, 1, 4),
    _HpnicfDot11SaFrequency_Type()
)
hpnicfDot11SaFrequency.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDot11SaFrequency.setStatus("current")
_HpnicfDot11SaRtFreqPower_Type = Integer32
_HpnicfDot11SaRtFreqPower_Object = MibTableColumn
hpnicfDot11SaRtFreqPower = _HpnicfDot11SaRtFreqPower_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 13, 2, 1, 1, 5),
    _HpnicfDot11SaRtFreqPower_Type()
)
hpnicfDot11SaRtFreqPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11SaRtFreqPower.setStatus("current")
_HpnicfDot11SaRtFreqMaxPower_Type = Integer32
_HpnicfDot11SaRtFreqMaxPower_Object = MibTableColumn
hpnicfDot11SaRtFreqMaxPower = _HpnicfDot11SaRtFreqMaxPower_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 13, 2, 1, 1, 6),
    _HpnicfDot11SaRtFreqMaxPower_Type()
)
hpnicfDot11SaRtFreqMaxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11SaRtFreqMaxPower.setStatus("current")
_HpnicfDot11SaRtFreqDutyCycle_Type = Integer32
_HpnicfDot11SaRtFreqDutyCycle_Object = MibTableColumn
hpnicfDot11SaRtFreqDutyCycle = _HpnicfDot11SaRtFreqDutyCycle_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 13, 2, 1, 1, 7),
    _HpnicfDot11SaRtFreqDutyCycle_Type()
)
hpnicfDot11SaRtFreqDutyCycle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11SaRtFreqDutyCycle.setStatus("current")
_HpnicfDot11SaRtFreqDataSeqNo_Type = Unsigned32
_HpnicfDot11SaRtFreqDataSeqNo_Object = MibTableColumn
hpnicfDot11SaRtFreqDataSeqNo = _HpnicfDot11SaRtFreqDataSeqNo_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 13, 2, 1, 1, 8),
    _HpnicfDot11SaRtFreqDataSeqNo_Type()
)
hpnicfDot11SaRtFreqDataSeqNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11SaRtFreqDataSeqNo.setStatus("current")
_HpnicfDot11SaIntfDevTable_Object = MibTable
hpnicfDot11SaIntfDevTable = _HpnicfDot11SaIntfDevTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 13, 2, 2)
)
if mibBuilder.loadTexts:
    hpnicfDot11SaIntfDevTable.setStatus("current")
_HpnicfDot11SaIntfDevEntry_Object = MibTableRow
hpnicfDot11SaIntfDevEntry = _HpnicfDot11SaIntfDevEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 13, 2, 2, 1)
)
hpnicfDot11SaIntfDevEntry.setIndexNames(
    (0, "HPN-ICF-DOT11-SA-MIB", "hpnicfDot11SaAPID"),
    (0, "HPN-ICF-DOT11-SA-MIB", "hpnicfDot11SaRadioID"),
    (0, "HPN-ICF-DOT11-SA-MIB", "hpnicfDot11SaDevID"),
)
if mibBuilder.loadTexts:
    hpnicfDot11SaIntfDevEntry.setStatus("current")
_HpnicfDot11SaDevID_Type = Integer32
_HpnicfDot11SaDevID_Object = MibTableColumn
hpnicfDot11SaDevID = _HpnicfDot11SaDevID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 13, 2, 2, 1, 1),
    _HpnicfDot11SaDevID_Type()
)
hpnicfDot11SaDevID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDot11SaDevID.setStatus("current")
_HpnicfDot11SaDevType_Type = HpnicfDot11SaIntfDevType
_HpnicfDot11SaDevType_Object = MibTableColumn
hpnicfDot11SaDevType = _HpnicfDot11SaDevType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 13, 2, 2, 1, 2),
    _HpnicfDot11SaDevType_Type()
)
hpnicfDot11SaDevType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11SaDevType.setStatus("current")
_HpnicfDot11SaDevSI_Type = Integer32
_HpnicfDot11SaDevSI_Object = MibTableColumn
hpnicfDot11SaDevSI = _HpnicfDot11SaDevSI_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 13, 2, 2, 1, 3),
    _HpnicfDot11SaDevSI_Type()
)
hpnicfDot11SaDevSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11SaDevSI.setStatus("current")
_HpnicfDot11SaDevRSSI_Type = Integer32
_HpnicfDot11SaDevRSSI_Object = MibTableColumn
hpnicfDot11SaDevRSSI = _HpnicfDot11SaDevRSSI_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 13, 2, 2, 1, 4),
    _HpnicfDot11SaDevRSSI_Type()
)
hpnicfDot11SaDevRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11SaDevRSSI.setStatus("current")
_HpnicfDot11SaDevDutyCycle_Type = Integer32
_HpnicfDot11SaDevDutyCycle_Object = MibTableColumn
hpnicfDot11SaDevDutyCycle = _HpnicfDot11SaDevDutyCycle_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 13, 2, 2, 1, 5),
    _HpnicfDot11SaDevDutyCycle_Type()
)
hpnicfDot11SaDevDutyCycle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11SaDevDutyCycle.setStatus("current")
_HpnicfDot11SaDevAffectedChls_Type = OctetString
_HpnicfDot11SaDevAffectedChls_Object = MibTableColumn
hpnicfDot11SaDevAffectedChls = _HpnicfDot11SaDevAffectedChls_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 13, 2, 2, 1, 6),
    _HpnicfDot11SaDevAffectedChls_Type()
)
hpnicfDot11SaDevAffectedChls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11SaDevAffectedChls.setStatus("current")
_HpnicfDot11SaDevDetectedTime_Type = DateAndTime
_HpnicfDot11SaDevDetectedTime_Object = MibTableColumn
hpnicfDot11SaDevDetectedTime = _HpnicfDot11SaDevDetectedTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 13, 2, 2, 1, 7),
    _HpnicfDot11SaDevDetectedTime_Type()
)
hpnicfDot11SaDevDetectedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11SaDevDetectedTime.setStatus("current")
_HpnicfDot11SaAirQualityTable_Object = MibTable
hpnicfDot11SaAirQualityTable = _HpnicfDot11SaAirQualityTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 13, 2, 3)
)
if mibBuilder.loadTexts:
    hpnicfDot11SaAirQualityTable.setStatus("current")
_HpnicfDot11SaAirQualityEntry_Object = MibTableRow
hpnicfDot11SaAirQualityEntry = _HpnicfDot11SaAirQualityEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 13, 2, 3, 1)
)
hpnicfDot11SaAirQualityEntry.setIndexNames(
    (0, "HPN-ICF-DOT11-SA-MIB", "hpnicfDot11SaAPID"),
    (0, "HPN-ICF-DOT11-SA-MIB", "hpnicfDot11SaRadioID"),
    (0, "HPN-ICF-DOT11-SA-MIB", "hpnicfDot11SaChlNum"),
)
if mibBuilder.loadTexts:
    hpnicfDot11SaAirQualityEntry.setStatus("current")
_HpnicfDot11SaChlNum_Type = HpnicfDot11ChannelScopeType
_HpnicfDot11SaChlNum_Object = MibTableColumn
hpnicfDot11SaChlNum = _HpnicfDot11SaChlNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 13, 2, 3, 1, 1),
    _HpnicfDot11SaChlNum_Type()
)
hpnicfDot11SaChlNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDot11SaChlNum.setStatus("current")
_HpnicfDot11SaAvgQuality_Type = Integer32
_HpnicfDot11SaAvgQuality_Object = MibTableColumn
hpnicfDot11SaAvgQuality = _HpnicfDot11SaAvgQuality_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 13, 2, 3, 1, 2),
    _HpnicfDot11SaAvgQuality_Type()
)
hpnicfDot11SaAvgQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11SaAvgQuality.setStatus("current")
_HpnicfDot11SaMinQuality_Type = Integer32
_HpnicfDot11SaMinQuality_Object = MibTableColumn
hpnicfDot11SaMinQuality = _HpnicfDot11SaMinQuality_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 13, 2, 3, 1, 3),
    _HpnicfDot11SaMinQuality_Type()
)
hpnicfDot11SaMinQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11SaMinQuality.setStatus("current")
_HpnicfDot11SaIntfDevNum_Type = Integer32
_HpnicfDot11SaIntfDevNum_Object = MibTableColumn
hpnicfDot11SaIntfDevNum = _HpnicfDot11SaIntfDevNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 13, 2, 3, 1, 4),
    _HpnicfDot11SaIntfDevNum_Type()
)
hpnicfDot11SaIntfDevNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11SaIntfDevNum.setStatus("current")
_HpnicfDot11SaWiFiUtil_Type = Integer32
_HpnicfDot11SaWiFiUtil_Object = MibTableColumn
hpnicfDot11SaWiFiUtil = _HpnicfDot11SaWiFiUtil_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 13, 2, 3, 1, 5),
    _HpnicfDot11SaWiFiUtil_Type()
)
hpnicfDot11SaWiFiUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11SaWiFiUtil.setStatus("current")
_HpnicfDot11SaNonWiFiUtil_Type = Integer32
_HpnicfDot11SaNonWiFiUtil_Object = MibTableColumn
hpnicfDot11SaNonWiFiUtil = _HpnicfDot11SaNonWiFiUtil_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 13, 2, 3, 1, 6),
    _HpnicfDot11SaNonWiFiUtil_Type()
)
hpnicfDot11SaNonWiFiUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11SaNonWiFiUtil.setStatus("current")
_HpnicfDot11SaNoiseFloor_Type = Integer32
_HpnicfDot11SaNoiseFloor_Object = MibTableColumn
hpnicfDot11SaNoiseFloor = _HpnicfDot11SaNoiseFloor_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 13, 2, 3, 1, 7),
    _HpnicfDot11SaNoiseFloor_Type()
)
hpnicfDot11SaNoiseFloor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11SaNoiseFloor.setStatus("current")
_HpnicfDot11SaNotifyGroup_ObjectIdentity = ObjectIdentity
hpnicfDot11SaNotifyGroup = _HpnicfDot11SaNotifyGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 13, 3)
)
_HpnicfDot11SaTraps_ObjectIdentity = ObjectIdentity
hpnicfDot11SaTraps = _HpnicfDot11SaTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 13, 3, 0)
)
_HpnicfDot11SaTrapVars_ObjectIdentity = ObjectIdentity
hpnicfDot11SaTrapVars = _HpnicfDot11SaTrapVars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 13, 3, 1)
)
_HpnicfDot11SaTrapAPID_Type = HpnicfDot11ObjectIDType
_HpnicfDot11SaTrapAPID_Object = MibScalar
hpnicfDot11SaTrapAPID = _HpnicfDot11SaTrapAPID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 13, 3, 1, 1),
    _HpnicfDot11SaTrapAPID_Type()
)
hpnicfDot11SaTrapAPID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfDot11SaTrapAPID.setStatus("current")
_HpnicfDot11SaTrapRadioID_Type = HpnicfDot11RadioScopeType
_HpnicfDot11SaTrapRadioID_Object = MibScalar
hpnicfDot11SaTrapRadioID = _HpnicfDot11SaTrapRadioID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 13, 3, 1, 2),
    _HpnicfDot11SaTrapRadioID_Type()
)
hpnicfDot11SaTrapRadioID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfDot11SaTrapRadioID.setStatus("current")
_HpnicfDot11SaTrapDevID_Type = Integer32
_HpnicfDot11SaTrapDevID_Object = MibScalar
hpnicfDot11SaTrapDevID = _HpnicfDot11SaTrapDevID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 13, 3, 1, 3),
    _HpnicfDot11SaTrapDevID_Type()
)
hpnicfDot11SaTrapDevID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfDot11SaTrapDevID.setStatus("current")
_HpnicfDot11SaTrapIntfDevType_Type = HpnicfDot11SaIntfDevType
_HpnicfDot11SaTrapIntfDevType_Object = MibScalar
hpnicfDot11SaTrapIntfDevType = _HpnicfDot11SaTrapIntfDevType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 13, 3, 1, 4),
    _HpnicfDot11SaTrapIntfDevType_Type()
)
hpnicfDot11SaTrapIntfDevType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfDot11SaTrapIntfDevType.setStatus("current")
_HpnicfDot11APTrapDevSI_Type = Integer32
_HpnicfDot11APTrapDevSI_Object = MibScalar
hpnicfDot11APTrapDevSI = _HpnicfDot11APTrapDevSI_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 13, 3, 1, 5),
    _HpnicfDot11APTrapDevSI_Type()
)
hpnicfDot11APTrapDevSI.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfDot11APTrapDevSI.setStatus("current")
_HpnicfDot11SaTrapDevRSSI_Type = Integer32
_HpnicfDot11SaTrapDevRSSI_Object = MibScalar
hpnicfDot11SaTrapDevRSSI = _HpnicfDot11SaTrapDevRSSI_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 13, 3, 1, 6),
    _HpnicfDot11SaTrapDevRSSI_Type()
)
hpnicfDot11SaTrapDevRSSI.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfDot11SaTrapDevRSSI.setStatus("current")
_HpnicfDot11APTrapDevDC_Type = Integer32
_HpnicfDot11APTrapDevDC_Object = MibScalar
hpnicfDot11APTrapDevDC = _HpnicfDot11APTrapDevDC_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 13, 3, 1, 7),
    _HpnicfDot11APTrapDevDC_Type()
)
hpnicfDot11APTrapDevDC.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfDot11APTrapDevDC.setStatus("current")
_HpnicfDot11APTrapDevChls_Type = OctetString
_HpnicfDot11APTrapDevChls_Object = MibScalar
hpnicfDot11APTrapDevChls = _HpnicfDot11APTrapDevChls_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 13, 3, 1, 8),
    _HpnicfDot11APTrapDevChls_Type()
)
hpnicfDot11APTrapDevChls.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfDot11APTrapDevChls.setStatus("current")
_HpnicfDot11APTrapDevDctTime_Type = DateAndTime
_HpnicfDot11APTrapDevDctTime_Object = MibScalar
hpnicfDot11APTrapDevDctTime = _HpnicfDot11APTrapDevDctTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 13, 3, 1, 9),
    _HpnicfDot11APTrapDevDctTime_Type()
)
hpnicfDot11APTrapDevDctTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfDot11APTrapDevDctTime.setStatus("current")
_HpnicfDot11SaTrapChlNum_Type = HpnicfDot11ChannelScopeType
_HpnicfDot11SaTrapChlNum_Object = MibScalar
hpnicfDot11SaTrapChlNum = _HpnicfDot11SaTrapChlNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 13, 3, 1, 10),
    _HpnicfDot11SaTrapChlNum_Type()
)
hpnicfDot11SaTrapChlNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfDot11SaTrapChlNum.setStatus("current")
_HpnicfDot11SaTrapChlQlt_Type = Integer32
_HpnicfDot11SaTrapChlQlt_Object = MibScalar
hpnicfDot11SaTrapChlQlt = _HpnicfDot11SaTrapChlQlt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 13, 3, 1, 11),
    _HpnicfDot11SaTrapChlQlt_Type()
)
hpnicfDot11SaTrapChlQlt.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfDot11SaTrapChlQlt.setStatus("current")
_HpnicfDot11SaTrapChlIntfNum_Type = Integer32
_HpnicfDot11SaTrapChlIntfNum_Object = MibScalar
hpnicfDot11SaTrapChlIntfNum = _HpnicfDot11SaTrapChlIntfNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 13, 3, 1, 12),
    _HpnicfDot11SaTrapChlIntfNum_Type()
)
hpnicfDot11SaTrapChlIntfNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfDot11SaTrapChlIntfNum.setStatus("current")

# Managed Objects groups


# Notification objects

hpnicfDot11SaIntfDevDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 13, 3, 0, 1)
)
hpnicfDot11SaIntfDevDetected.setObjects(
      *(("HPN-ICF-DOT11-SA-MIB", "hpnicfDot11SaTrapAPID"),
        ("HPN-ICF-DOT11-SA-MIB", "hpnicfDot11SaTrapRadioID"),
        ("HPN-ICF-DOT11-SA-MIB", "hpnicfDot11SaTrapDevID"),
        ("HPN-ICF-DOT11-SA-MIB", "hpnicfDot11SaTrapIntfDevType"),
        ("HPN-ICF-DOT11-SA-MIB", "hpnicfDot11APTrapDevSI"),
        ("HPN-ICF-DOT11-SA-MIB", "hpnicfDot11SaTrapDevRSSI"),
        ("HPN-ICF-DOT11-SA-MIB", "hpnicfDot11APTrapDevDC"),
        ("HPN-ICF-DOT11-SA-MIB", "hpnicfDot11APTrapDevChls"),
        ("HPN-ICF-DOT11-SA-MIB", "hpnicfDot11APTrapDevDctTime"))
)
if mibBuilder.loadTexts:
    hpnicfDot11SaIntfDevDetected.setStatus(
        "current"
    )

hpnicfDot11SaIntfDevDisappear = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 13, 3, 0, 2)
)
hpnicfDot11SaIntfDevDisappear.setObjects(
      *(("HPN-ICF-DOT11-SA-MIB", "hpnicfDot11SaTrapAPID"),
        ("HPN-ICF-DOT11-SA-MIB", "hpnicfDot11SaTrapRadioID"),
        ("HPN-ICF-DOT11-SA-MIB", "hpnicfDot11SaTrapDevID"),
        ("HPN-ICF-DOT11-SA-MIB", "hpnicfDot11SaTrapIntfDevType"))
)
if mibBuilder.loadTexts:
    hpnicfDot11SaIntfDevDisappear.setStatus(
        "current"
    )

hpnicfDot11SaChlQltLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 13, 3, 0, 3)
)
hpnicfDot11SaChlQltLow.setObjects(
      *(("HPN-ICF-DOT11-SA-MIB", "hpnicfDot11SaTrapAPID"),
        ("HPN-ICF-DOT11-SA-MIB", "hpnicfDot11SaTrapRadioID"),
        ("HPN-ICF-DOT11-SA-MIB", "hpnicfDot11SaTrapChlNum"),
        ("HPN-ICF-DOT11-SA-MIB", "hpnicfDot11SaTrapChlQlt"),
        ("HPN-ICF-DOT11-SA-MIB", "hpnicfDot11SaTrapChlIntfNum"))
)
if mibBuilder.loadTexts:
    hpnicfDot11SaChlQltLow.setStatus(
        "current"
    )

hpnicfDot11SaChlQltRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 13, 3, 0, 4)
)
hpnicfDot11SaChlQltRecover.setObjects(
      *(("HPN-ICF-DOT11-SA-MIB", "hpnicfDot11SaTrapAPID"),
        ("HPN-ICF-DOT11-SA-MIB", "hpnicfDot11SaTrapRadioID"),
        ("HPN-ICF-DOT11-SA-MIB", "hpnicfDot11SaTrapChlNum"),
        ("HPN-ICF-DOT11-SA-MIB", "hpnicfDot11SaTrapChlQlt"),
        ("HPN-ICF-DOT11-SA-MIB", "hpnicfDot11SaTrapChlIntfNum"))
)
if mibBuilder.loadTexts:
    hpnicfDot11SaChlQltRecover.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-DOT11-SA-MIB",
    **{"hpnicfDot11Sa": hpnicfDot11Sa,
       "hpnicfDot11SaCfgGroup": hpnicfDot11SaCfgGroup,
       "hpnicfDot11SaCfgTable": hpnicfDot11SaCfgTable,
       "hpnicfDot11SaCfgEntry": hpnicfDot11SaCfgEntry,
       "hpnicfDot11SaCfgRadioType": hpnicfDot11SaCfgRadioType,
       "hpnicfDot11SaEnable": hpnicfDot11SaEnable,
       "hpnicfDot11SaRptDevType": hpnicfDot11SaRptDevType,
       "hpnicfDot11SaTrapDevEnable": hpnicfDot11SaTrapDevEnable,
       "hpnicfDot11SaTrapDevType": hpnicfDot11SaTrapDevType,
       "hpnicfDot11SaTrapAQEnable": hpnicfDot11SaTrapAQEnable,
       "hpnicfDot11SaTrapAQThreshold": hpnicfDot11SaTrapAQThreshold,
       "hpnicfDot11SaDrivenRRMEnable": hpnicfDot11SaDrivenRRMEnable,
       "hpnicfDot11SaDrivenRRMSnt": hpnicfDot11SaDrivenRRMSnt,
       "hpnicfDot11SaStatusGroup": hpnicfDot11SaStatusGroup,
       "hpnicfDot11SaRtFFTDataTable": hpnicfDot11SaRtFFTDataTable,
       "hpnicfDot11SaRtFFTDataEntry": hpnicfDot11SaRtFFTDataEntry,
       "hpnicfDot11SaAPID": hpnicfDot11SaAPID,
       "hpnicfDot11SaRadioID": hpnicfDot11SaRadioID,
       "hpnicfDot11SaRtDataGroupID": hpnicfDot11SaRtDataGroupID,
       "hpnicfDot11SaFrequency": hpnicfDot11SaFrequency,
       "hpnicfDot11SaRtFreqPower": hpnicfDot11SaRtFreqPower,
       "hpnicfDot11SaRtFreqMaxPower": hpnicfDot11SaRtFreqMaxPower,
       "hpnicfDot11SaRtFreqDutyCycle": hpnicfDot11SaRtFreqDutyCycle,
       "hpnicfDot11SaRtFreqDataSeqNo": hpnicfDot11SaRtFreqDataSeqNo,
       "hpnicfDot11SaIntfDevTable": hpnicfDot11SaIntfDevTable,
       "hpnicfDot11SaIntfDevEntry": hpnicfDot11SaIntfDevEntry,
       "hpnicfDot11SaDevID": hpnicfDot11SaDevID,
       "hpnicfDot11SaDevType": hpnicfDot11SaDevType,
       "hpnicfDot11SaDevSI": hpnicfDot11SaDevSI,
       "hpnicfDot11SaDevRSSI": hpnicfDot11SaDevRSSI,
       "hpnicfDot11SaDevDutyCycle": hpnicfDot11SaDevDutyCycle,
       "hpnicfDot11SaDevAffectedChls": hpnicfDot11SaDevAffectedChls,
       "hpnicfDot11SaDevDetectedTime": hpnicfDot11SaDevDetectedTime,
       "hpnicfDot11SaAirQualityTable": hpnicfDot11SaAirQualityTable,
       "hpnicfDot11SaAirQualityEntry": hpnicfDot11SaAirQualityEntry,
       "hpnicfDot11SaChlNum": hpnicfDot11SaChlNum,
       "hpnicfDot11SaAvgQuality": hpnicfDot11SaAvgQuality,
       "hpnicfDot11SaMinQuality": hpnicfDot11SaMinQuality,
       "hpnicfDot11SaIntfDevNum": hpnicfDot11SaIntfDevNum,
       "hpnicfDot11SaWiFiUtil": hpnicfDot11SaWiFiUtil,
       "hpnicfDot11SaNonWiFiUtil": hpnicfDot11SaNonWiFiUtil,
       "hpnicfDot11SaNoiseFloor": hpnicfDot11SaNoiseFloor,
       "hpnicfDot11SaNotifyGroup": hpnicfDot11SaNotifyGroup,
       "hpnicfDot11SaTraps": hpnicfDot11SaTraps,
       "hpnicfDot11SaIntfDevDetected": hpnicfDot11SaIntfDevDetected,
       "hpnicfDot11SaIntfDevDisappear": hpnicfDot11SaIntfDevDisappear,
       "hpnicfDot11SaChlQltLow": hpnicfDot11SaChlQltLow,
       "hpnicfDot11SaChlQltRecover": hpnicfDot11SaChlQltRecover,
       "hpnicfDot11SaTrapVars": hpnicfDot11SaTrapVars,
       "hpnicfDot11SaTrapAPID": hpnicfDot11SaTrapAPID,
       "hpnicfDot11SaTrapRadioID": hpnicfDot11SaTrapRadioID,
       "hpnicfDot11SaTrapDevID": hpnicfDot11SaTrapDevID,
       "hpnicfDot11SaTrapIntfDevType": hpnicfDot11SaTrapIntfDevType,
       "hpnicfDot11APTrapDevSI": hpnicfDot11APTrapDevSI,
       "hpnicfDot11SaTrapDevRSSI": hpnicfDot11SaTrapDevRSSI,
       "hpnicfDot11APTrapDevDC": hpnicfDot11APTrapDevDC,
       "hpnicfDot11APTrapDevChls": hpnicfDot11APTrapDevChls,
       "hpnicfDot11APTrapDevDctTime": hpnicfDot11APTrapDevDctTime,
       "hpnicfDot11SaTrapChlNum": hpnicfDot11SaTrapChlNum,
       "hpnicfDot11SaTrapChlQlt": hpnicfDot11SaTrapChlQlt,
       "hpnicfDot11SaTrapChlIntfNum": hpnicfDot11SaTrapChlIntfNum}
)
