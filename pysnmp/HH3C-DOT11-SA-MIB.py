# SNMP MIB module (HH3C-DOT11-SA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-DOT11-SA-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:52:55 2024
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

(Hh3cDot11ChannelScopeType,
 Hh3cDot11ObjectIDType,
 Hh3cDot11RadioScopeType,
 Hh3cDot11SaIntfDevType,
 hh3cDot11) = mibBuilder.importSymbols(
    "HH3C-DOT11-REF-MIB",
    "Hh3cDot11ChannelScopeType",
    "Hh3cDot11ObjectIDType",
    "Hh3cDot11RadioScopeType",
    "Hh3cDot11SaIntfDevType",
    "hh3cDot11")

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

hh3cDot11Sa = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 13)
)
hh3cDot11Sa.setRevisions(
        ("2011-08-26 20:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cDot11SaCfgGroup_ObjectIdentity = ObjectIdentity
hh3cDot11SaCfgGroup = _Hh3cDot11SaCfgGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 13, 1)
)
_Hh3cDot11SaCfgTable_Object = MibTable
hh3cDot11SaCfgTable = _Hh3cDot11SaCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 13, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cDot11SaCfgTable.setStatus("current")
_Hh3cDot11SaCfgEntry_Object = MibTableRow
hh3cDot11SaCfgEntry = _Hh3cDot11SaCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 13, 1, 1, 1)
)
hh3cDot11SaCfgEntry.setIndexNames(
    (0, "HH3C-DOT11-SA-MIB", "hh3cDot11SaCfgRadioType"),
)
if mibBuilder.loadTexts:
    hh3cDot11SaCfgEntry.setStatus("current")


class _Hh3cDot11SaCfgRadioType_Type(Integer32):
    """Custom type hh3cDot11SaCfgRadioType based on Integer32"""
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


_Hh3cDot11SaCfgRadioType_Type.__name__ = "Integer32"
_Hh3cDot11SaCfgRadioType_Object = MibTableColumn
hh3cDot11SaCfgRadioType = _Hh3cDot11SaCfgRadioType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 13, 1, 1, 1, 1),
    _Hh3cDot11SaCfgRadioType_Type()
)
hh3cDot11SaCfgRadioType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11SaCfgRadioType.setStatus("current")
_Hh3cDot11SaEnable_Type = TruthValue
_Hh3cDot11SaEnable_Object = MibTableColumn
hh3cDot11SaEnable = _Hh3cDot11SaEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 13, 1, 1, 1, 2),
    _Hh3cDot11SaEnable_Type()
)
hh3cDot11SaEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11SaEnable.setStatus("current")


class _Hh3cDot11SaRptDevType_Type(Bits):
    """Custom type hh3cDot11SaRptDevType based on Bits"""
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

_Hh3cDot11SaRptDevType_Type.__name__ = "Bits"
_Hh3cDot11SaRptDevType_Object = MibTableColumn
hh3cDot11SaRptDevType = _Hh3cDot11SaRptDevType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 13, 1, 1, 1, 3),
    _Hh3cDot11SaRptDevType_Type()
)
hh3cDot11SaRptDevType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11SaRptDevType.setStatus("current")
_Hh3cDot11SaTrapDevEnable_Type = TruthValue
_Hh3cDot11SaTrapDevEnable_Object = MibTableColumn
hh3cDot11SaTrapDevEnable = _Hh3cDot11SaTrapDevEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 13, 1, 1, 1, 4),
    _Hh3cDot11SaTrapDevEnable_Type()
)
hh3cDot11SaTrapDevEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11SaTrapDevEnable.setStatus("current")


class _Hh3cDot11SaTrapDevType_Type(Bits):
    """Custom type hh3cDot11SaTrapDevType based on Bits"""
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

_Hh3cDot11SaTrapDevType_Type.__name__ = "Bits"
_Hh3cDot11SaTrapDevType_Object = MibTableColumn
hh3cDot11SaTrapDevType = _Hh3cDot11SaTrapDevType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 13, 1, 1, 1, 5),
    _Hh3cDot11SaTrapDevType_Type()
)
hh3cDot11SaTrapDevType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11SaTrapDevType.setStatus("current")
_Hh3cDot11SaTrapAQEnable_Type = TruthValue
_Hh3cDot11SaTrapAQEnable_Object = MibTableColumn
hh3cDot11SaTrapAQEnable = _Hh3cDot11SaTrapAQEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 13, 1, 1, 1, 6),
    _Hh3cDot11SaTrapAQEnable_Type()
)
hh3cDot11SaTrapAQEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11SaTrapAQEnable.setStatus("current")


class _Hh3cDot11SaTrapAQThreshold_Type(Integer32):
    """Custom type hh3cDot11SaTrapAQThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_Hh3cDot11SaTrapAQThreshold_Type.__name__ = "Integer32"
_Hh3cDot11SaTrapAQThreshold_Object = MibTableColumn
hh3cDot11SaTrapAQThreshold = _Hh3cDot11SaTrapAQThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 13, 1, 1, 1, 7),
    _Hh3cDot11SaTrapAQThreshold_Type()
)
hh3cDot11SaTrapAQThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11SaTrapAQThreshold.setStatus("current")
_Hh3cDot11SaDrivenRRMEnable_Type = TruthValue
_Hh3cDot11SaDrivenRRMEnable_Object = MibTableColumn
hh3cDot11SaDrivenRRMEnable = _Hh3cDot11SaDrivenRRMEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 13, 1, 1, 1, 8),
    _Hh3cDot11SaDrivenRRMEnable_Type()
)
hh3cDot11SaDrivenRRMEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11SaDrivenRRMEnable.setStatus("current")


class _Hh3cDot11SaDrivenRRMSnt_Type(Integer32):
    """Custom type hh3cDot11SaDrivenRRMSnt based on Integer32"""
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


_Hh3cDot11SaDrivenRRMSnt_Type.__name__ = "Integer32"
_Hh3cDot11SaDrivenRRMSnt_Object = MibTableColumn
hh3cDot11SaDrivenRRMSnt = _Hh3cDot11SaDrivenRRMSnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 13, 1, 1, 1, 9),
    _Hh3cDot11SaDrivenRRMSnt_Type()
)
hh3cDot11SaDrivenRRMSnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11SaDrivenRRMSnt.setStatus("current")
_Hh3cDot11SaStatusGroup_ObjectIdentity = ObjectIdentity
hh3cDot11SaStatusGroup = _Hh3cDot11SaStatusGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 13, 2)
)
_Hh3cDot11SaRtFFTDataTable_Object = MibTable
hh3cDot11SaRtFFTDataTable = _Hh3cDot11SaRtFFTDataTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 13, 2, 1)
)
if mibBuilder.loadTexts:
    hh3cDot11SaRtFFTDataTable.setStatus("current")
_Hh3cDot11SaRtFFTDataEntry_Object = MibTableRow
hh3cDot11SaRtFFTDataEntry = _Hh3cDot11SaRtFFTDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 13, 2, 1, 1)
)
hh3cDot11SaRtFFTDataEntry.setIndexNames(
    (0, "HH3C-DOT11-SA-MIB", "hh3cDot11SaAPID"),
    (0, "HH3C-DOT11-SA-MIB", "hh3cDot11SaRadioID"),
    (0, "HH3C-DOT11-SA-MIB", "hh3cDot11SaRtDataGroupID"),
    (0, "HH3C-DOT11-SA-MIB", "hh3cDot11SaFrequency"),
)
if mibBuilder.loadTexts:
    hh3cDot11SaRtFFTDataEntry.setStatus("current")
_Hh3cDot11SaAPID_Type = Hh3cDot11ObjectIDType
_Hh3cDot11SaAPID_Object = MibTableColumn
hh3cDot11SaAPID = _Hh3cDot11SaAPID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 13, 2, 1, 1, 1),
    _Hh3cDot11SaAPID_Type()
)
hh3cDot11SaAPID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11SaAPID.setStatus("current")
_Hh3cDot11SaRadioID_Type = Hh3cDot11RadioScopeType
_Hh3cDot11SaRadioID_Object = MibTableColumn
hh3cDot11SaRadioID = _Hh3cDot11SaRadioID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 13, 2, 1, 1, 2),
    _Hh3cDot11SaRadioID_Type()
)
hh3cDot11SaRadioID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11SaRadioID.setStatus("current")
_Hh3cDot11SaRtDataGroupID_Type = Integer32
_Hh3cDot11SaRtDataGroupID_Object = MibTableColumn
hh3cDot11SaRtDataGroupID = _Hh3cDot11SaRtDataGroupID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 13, 2, 1, 1, 3),
    _Hh3cDot11SaRtDataGroupID_Type()
)
hh3cDot11SaRtDataGroupID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11SaRtDataGroupID.setStatus("current")
_Hh3cDot11SaFrequency_Type = Integer32
_Hh3cDot11SaFrequency_Object = MibTableColumn
hh3cDot11SaFrequency = _Hh3cDot11SaFrequency_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 13, 2, 1, 1, 4),
    _Hh3cDot11SaFrequency_Type()
)
hh3cDot11SaFrequency.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11SaFrequency.setStatus("current")
_Hh3cDot11SaRtFreqPower_Type = Integer32
_Hh3cDot11SaRtFreqPower_Object = MibTableColumn
hh3cDot11SaRtFreqPower = _Hh3cDot11SaRtFreqPower_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 13, 2, 1, 1, 5),
    _Hh3cDot11SaRtFreqPower_Type()
)
hh3cDot11SaRtFreqPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11SaRtFreqPower.setStatus("current")
_Hh3cDot11SaRtFreqMaxPower_Type = Integer32
_Hh3cDot11SaRtFreqMaxPower_Object = MibTableColumn
hh3cDot11SaRtFreqMaxPower = _Hh3cDot11SaRtFreqMaxPower_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 13, 2, 1, 1, 6),
    _Hh3cDot11SaRtFreqMaxPower_Type()
)
hh3cDot11SaRtFreqMaxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11SaRtFreqMaxPower.setStatus("current")
_Hh3cDot11SaRtFreqDutyCycle_Type = Integer32
_Hh3cDot11SaRtFreqDutyCycle_Object = MibTableColumn
hh3cDot11SaRtFreqDutyCycle = _Hh3cDot11SaRtFreqDutyCycle_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 13, 2, 1, 1, 7),
    _Hh3cDot11SaRtFreqDutyCycle_Type()
)
hh3cDot11SaRtFreqDutyCycle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11SaRtFreqDutyCycle.setStatus("current")
_Hh3cDot11SaRtFreqDataSeqNo_Type = Unsigned32
_Hh3cDot11SaRtFreqDataSeqNo_Object = MibTableColumn
hh3cDot11SaRtFreqDataSeqNo = _Hh3cDot11SaRtFreqDataSeqNo_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 13, 2, 1, 1, 8),
    _Hh3cDot11SaRtFreqDataSeqNo_Type()
)
hh3cDot11SaRtFreqDataSeqNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11SaRtFreqDataSeqNo.setStatus("current")
_Hh3cDot11SaIntfDevTable_Object = MibTable
hh3cDot11SaIntfDevTable = _Hh3cDot11SaIntfDevTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 13, 2, 2)
)
if mibBuilder.loadTexts:
    hh3cDot11SaIntfDevTable.setStatus("current")
_Hh3cDot11SaIntfDevEntry_Object = MibTableRow
hh3cDot11SaIntfDevEntry = _Hh3cDot11SaIntfDevEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 13, 2, 2, 1)
)
hh3cDot11SaIntfDevEntry.setIndexNames(
    (0, "HH3C-DOT11-SA-MIB", "hh3cDot11SaAPID"),
    (0, "HH3C-DOT11-SA-MIB", "hh3cDot11SaRadioID"),
    (0, "HH3C-DOT11-SA-MIB", "hh3cDot11SaDevID"),
)
if mibBuilder.loadTexts:
    hh3cDot11SaIntfDevEntry.setStatus("current")
_Hh3cDot11SaDevID_Type = Integer32
_Hh3cDot11SaDevID_Object = MibTableColumn
hh3cDot11SaDevID = _Hh3cDot11SaDevID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 13, 2, 2, 1, 1),
    _Hh3cDot11SaDevID_Type()
)
hh3cDot11SaDevID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11SaDevID.setStatus("current")
_Hh3cDot11SaDevType_Type = Hh3cDot11SaIntfDevType
_Hh3cDot11SaDevType_Object = MibTableColumn
hh3cDot11SaDevType = _Hh3cDot11SaDevType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 13, 2, 2, 1, 2),
    _Hh3cDot11SaDevType_Type()
)
hh3cDot11SaDevType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11SaDevType.setStatus("current")
_Hh3cDot11SaDevSI_Type = Integer32
_Hh3cDot11SaDevSI_Object = MibTableColumn
hh3cDot11SaDevSI = _Hh3cDot11SaDevSI_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 13, 2, 2, 1, 3),
    _Hh3cDot11SaDevSI_Type()
)
hh3cDot11SaDevSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11SaDevSI.setStatus("current")
_Hh3cDot11SaDevRSSI_Type = Integer32
_Hh3cDot11SaDevRSSI_Object = MibTableColumn
hh3cDot11SaDevRSSI = _Hh3cDot11SaDevRSSI_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 13, 2, 2, 1, 4),
    _Hh3cDot11SaDevRSSI_Type()
)
hh3cDot11SaDevRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11SaDevRSSI.setStatus("current")
_Hh3cDot11SaDevDutyCycle_Type = Integer32
_Hh3cDot11SaDevDutyCycle_Object = MibTableColumn
hh3cDot11SaDevDutyCycle = _Hh3cDot11SaDevDutyCycle_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 13, 2, 2, 1, 5),
    _Hh3cDot11SaDevDutyCycle_Type()
)
hh3cDot11SaDevDutyCycle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11SaDevDutyCycle.setStatus("current")
_Hh3cDot11SaDevAffectedChls_Type = OctetString
_Hh3cDot11SaDevAffectedChls_Object = MibTableColumn
hh3cDot11SaDevAffectedChls = _Hh3cDot11SaDevAffectedChls_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 13, 2, 2, 1, 6),
    _Hh3cDot11SaDevAffectedChls_Type()
)
hh3cDot11SaDevAffectedChls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11SaDevAffectedChls.setStatus("current")
_Hh3cDot11SaDevDetectedTime_Type = DateAndTime
_Hh3cDot11SaDevDetectedTime_Object = MibTableColumn
hh3cDot11SaDevDetectedTime = _Hh3cDot11SaDevDetectedTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 13, 2, 2, 1, 7),
    _Hh3cDot11SaDevDetectedTime_Type()
)
hh3cDot11SaDevDetectedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11SaDevDetectedTime.setStatus("current")
_Hh3cDot11SaAirQualityTable_Object = MibTable
hh3cDot11SaAirQualityTable = _Hh3cDot11SaAirQualityTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 13, 2, 3)
)
if mibBuilder.loadTexts:
    hh3cDot11SaAirQualityTable.setStatus("current")
_Hh3cDot11SaAirQualityEntry_Object = MibTableRow
hh3cDot11SaAirQualityEntry = _Hh3cDot11SaAirQualityEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 13, 2, 3, 1)
)
hh3cDot11SaAirQualityEntry.setIndexNames(
    (0, "HH3C-DOT11-SA-MIB", "hh3cDot11SaAPID"),
    (0, "HH3C-DOT11-SA-MIB", "hh3cDot11SaRadioID"),
    (0, "HH3C-DOT11-SA-MIB", "hh3cDot11SaChlNum"),
)
if mibBuilder.loadTexts:
    hh3cDot11SaAirQualityEntry.setStatus("current")
_Hh3cDot11SaChlNum_Type = Hh3cDot11ChannelScopeType
_Hh3cDot11SaChlNum_Object = MibTableColumn
hh3cDot11SaChlNum = _Hh3cDot11SaChlNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 13, 2, 3, 1, 1),
    _Hh3cDot11SaChlNum_Type()
)
hh3cDot11SaChlNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11SaChlNum.setStatus("current")
_Hh3cDot11SaAvgQuality_Type = Integer32
_Hh3cDot11SaAvgQuality_Object = MibTableColumn
hh3cDot11SaAvgQuality = _Hh3cDot11SaAvgQuality_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 13, 2, 3, 1, 2),
    _Hh3cDot11SaAvgQuality_Type()
)
hh3cDot11SaAvgQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11SaAvgQuality.setStatus("current")
_Hh3cDot11SaMinQuality_Type = Integer32
_Hh3cDot11SaMinQuality_Object = MibTableColumn
hh3cDot11SaMinQuality = _Hh3cDot11SaMinQuality_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 13, 2, 3, 1, 3),
    _Hh3cDot11SaMinQuality_Type()
)
hh3cDot11SaMinQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11SaMinQuality.setStatus("current")
_Hh3cDot11SaIntfDevNum_Type = Integer32
_Hh3cDot11SaIntfDevNum_Object = MibTableColumn
hh3cDot11SaIntfDevNum = _Hh3cDot11SaIntfDevNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 13, 2, 3, 1, 4),
    _Hh3cDot11SaIntfDevNum_Type()
)
hh3cDot11SaIntfDevNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11SaIntfDevNum.setStatus("current")
_Hh3cDot11SaWiFiUtil_Type = Integer32
_Hh3cDot11SaWiFiUtil_Object = MibTableColumn
hh3cDot11SaWiFiUtil = _Hh3cDot11SaWiFiUtil_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 13, 2, 3, 1, 5),
    _Hh3cDot11SaWiFiUtil_Type()
)
hh3cDot11SaWiFiUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11SaWiFiUtil.setStatus("current")
_Hh3cDot11SaNonWiFiUtil_Type = Integer32
_Hh3cDot11SaNonWiFiUtil_Object = MibTableColumn
hh3cDot11SaNonWiFiUtil = _Hh3cDot11SaNonWiFiUtil_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 13, 2, 3, 1, 6),
    _Hh3cDot11SaNonWiFiUtil_Type()
)
hh3cDot11SaNonWiFiUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11SaNonWiFiUtil.setStatus("current")
_Hh3cDot11SaNoiseFloor_Type = Integer32
_Hh3cDot11SaNoiseFloor_Object = MibTableColumn
hh3cDot11SaNoiseFloor = _Hh3cDot11SaNoiseFloor_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 13, 2, 3, 1, 7),
    _Hh3cDot11SaNoiseFloor_Type()
)
hh3cDot11SaNoiseFloor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11SaNoiseFloor.setStatus("current")
_Hh3cDot11SaNotifyGroup_ObjectIdentity = ObjectIdentity
hh3cDot11SaNotifyGroup = _Hh3cDot11SaNotifyGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 13, 3)
)
_Hh3cDot11SaTraps_ObjectIdentity = ObjectIdentity
hh3cDot11SaTraps = _Hh3cDot11SaTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 13, 3, 0)
)
_Hh3cDot11SaTrapVars_ObjectIdentity = ObjectIdentity
hh3cDot11SaTrapVars = _Hh3cDot11SaTrapVars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 13, 3, 1)
)
_Hh3cDot11SaTrapAPID_Type = Hh3cDot11ObjectIDType
_Hh3cDot11SaTrapAPID_Object = MibScalar
hh3cDot11SaTrapAPID = _Hh3cDot11SaTrapAPID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 13, 3, 1, 1),
    _Hh3cDot11SaTrapAPID_Type()
)
hh3cDot11SaTrapAPID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11SaTrapAPID.setStatus("current")
_Hh3cDot11SaTrapRadioID_Type = Hh3cDot11RadioScopeType
_Hh3cDot11SaTrapRadioID_Object = MibScalar
hh3cDot11SaTrapRadioID = _Hh3cDot11SaTrapRadioID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 13, 3, 1, 2),
    _Hh3cDot11SaTrapRadioID_Type()
)
hh3cDot11SaTrapRadioID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11SaTrapRadioID.setStatus("current")
_Hh3cDot11SaTrapDevID_Type = Integer32
_Hh3cDot11SaTrapDevID_Object = MibScalar
hh3cDot11SaTrapDevID = _Hh3cDot11SaTrapDevID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 13, 3, 1, 3),
    _Hh3cDot11SaTrapDevID_Type()
)
hh3cDot11SaTrapDevID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11SaTrapDevID.setStatus("current")
_Hh3cDot11SaTrapIntfDevType_Type = Hh3cDot11SaIntfDevType
_Hh3cDot11SaTrapIntfDevType_Object = MibScalar
hh3cDot11SaTrapIntfDevType = _Hh3cDot11SaTrapIntfDevType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 13, 3, 1, 4),
    _Hh3cDot11SaTrapIntfDevType_Type()
)
hh3cDot11SaTrapIntfDevType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11SaTrapIntfDevType.setStatus("current")
_Hh3cDot11APTrapDevSI_Type = Integer32
_Hh3cDot11APTrapDevSI_Object = MibScalar
hh3cDot11APTrapDevSI = _Hh3cDot11APTrapDevSI_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 13, 3, 1, 5),
    _Hh3cDot11APTrapDevSI_Type()
)
hh3cDot11APTrapDevSI.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11APTrapDevSI.setStatus("current")
_Hh3cDot11SaTrapDevRSSI_Type = Integer32
_Hh3cDot11SaTrapDevRSSI_Object = MibScalar
hh3cDot11SaTrapDevRSSI = _Hh3cDot11SaTrapDevRSSI_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 13, 3, 1, 6),
    _Hh3cDot11SaTrapDevRSSI_Type()
)
hh3cDot11SaTrapDevRSSI.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11SaTrapDevRSSI.setStatus("current")
_Hh3cDot11APTrapDevDC_Type = Integer32
_Hh3cDot11APTrapDevDC_Object = MibScalar
hh3cDot11APTrapDevDC = _Hh3cDot11APTrapDevDC_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 13, 3, 1, 7),
    _Hh3cDot11APTrapDevDC_Type()
)
hh3cDot11APTrapDevDC.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11APTrapDevDC.setStatus("current")
_Hh3cDot11APTrapDevChls_Type = OctetString
_Hh3cDot11APTrapDevChls_Object = MibScalar
hh3cDot11APTrapDevChls = _Hh3cDot11APTrapDevChls_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 13, 3, 1, 8),
    _Hh3cDot11APTrapDevChls_Type()
)
hh3cDot11APTrapDevChls.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11APTrapDevChls.setStatus("current")
_Hh3cDot11APTrapDevDctTime_Type = DateAndTime
_Hh3cDot11APTrapDevDctTime_Object = MibScalar
hh3cDot11APTrapDevDctTime = _Hh3cDot11APTrapDevDctTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 13, 3, 1, 9),
    _Hh3cDot11APTrapDevDctTime_Type()
)
hh3cDot11APTrapDevDctTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11APTrapDevDctTime.setStatus("current")
_Hh3cDot11SaTrapChlNum_Type = Hh3cDot11ChannelScopeType
_Hh3cDot11SaTrapChlNum_Object = MibScalar
hh3cDot11SaTrapChlNum = _Hh3cDot11SaTrapChlNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 13, 3, 1, 10),
    _Hh3cDot11SaTrapChlNum_Type()
)
hh3cDot11SaTrapChlNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11SaTrapChlNum.setStatus("current")
_Hh3cDot11SaTrapChlQlt_Type = Integer32
_Hh3cDot11SaTrapChlQlt_Object = MibScalar
hh3cDot11SaTrapChlQlt = _Hh3cDot11SaTrapChlQlt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 13, 3, 1, 11),
    _Hh3cDot11SaTrapChlQlt_Type()
)
hh3cDot11SaTrapChlQlt.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11SaTrapChlQlt.setStatus("current")
_Hh3cDot11SaTrapChlIntfNum_Type = Integer32
_Hh3cDot11SaTrapChlIntfNum_Object = MibScalar
hh3cDot11SaTrapChlIntfNum = _Hh3cDot11SaTrapChlIntfNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 13, 3, 1, 12),
    _Hh3cDot11SaTrapChlIntfNum_Type()
)
hh3cDot11SaTrapChlIntfNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11SaTrapChlIntfNum.setStatus("current")

# Managed Objects groups


# Notification objects

hh3cDot11SaIntfDevDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 13, 3, 0, 1)
)
hh3cDot11SaIntfDevDetected.setObjects(
      *(("HH3C-DOT11-SA-MIB", "hh3cDot11SaTrapAPID"),
        ("HH3C-DOT11-SA-MIB", "hh3cDot11SaTrapRadioID"),
        ("HH3C-DOT11-SA-MIB", "hh3cDot11SaTrapDevID"),
        ("HH3C-DOT11-SA-MIB", "hh3cDot11SaTrapIntfDevType"),
        ("HH3C-DOT11-SA-MIB", "hh3cDot11APTrapDevSI"),
        ("HH3C-DOT11-SA-MIB", "hh3cDot11SaTrapDevRSSI"),
        ("HH3C-DOT11-SA-MIB", "hh3cDot11APTrapDevDC"),
        ("HH3C-DOT11-SA-MIB", "hh3cDot11APTrapDevChls"),
        ("HH3C-DOT11-SA-MIB", "hh3cDot11APTrapDevDctTime"))
)
if mibBuilder.loadTexts:
    hh3cDot11SaIntfDevDetected.setStatus(
        "current"
    )

hh3cDot11SaIntfDevDisappear = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 13, 3, 0, 2)
)
hh3cDot11SaIntfDevDisappear.setObjects(
      *(("HH3C-DOT11-SA-MIB", "hh3cDot11SaTrapAPID"),
        ("HH3C-DOT11-SA-MIB", "hh3cDot11SaTrapRadioID"),
        ("HH3C-DOT11-SA-MIB", "hh3cDot11SaTrapDevID"),
        ("HH3C-DOT11-SA-MIB", "hh3cDot11SaTrapIntfDevType"))
)
if mibBuilder.loadTexts:
    hh3cDot11SaIntfDevDisappear.setStatus(
        "current"
    )

hh3cDot11SaChlQltLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 13, 3, 0, 3)
)
hh3cDot11SaChlQltLow.setObjects(
      *(("HH3C-DOT11-SA-MIB", "hh3cDot11SaTrapAPID"),
        ("HH3C-DOT11-SA-MIB", "hh3cDot11SaTrapRadioID"),
        ("HH3C-DOT11-SA-MIB", "hh3cDot11SaTrapChlNum"),
        ("HH3C-DOT11-SA-MIB", "hh3cDot11SaTrapChlQlt"),
        ("HH3C-DOT11-SA-MIB", "hh3cDot11SaTrapChlIntfNum"))
)
if mibBuilder.loadTexts:
    hh3cDot11SaChlQltLow.setStatus(
        "current"
    )

hh3cDot11SaChlQltRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 13, 3, 0, 4)
)
hh3cDot11SaChlQltRecover.setObjects(
      *(("HH3C-DOT11-SA-MIB", "hh3cDot11SaTrapAPID"),
        ("HH3C-DOT11-SA-MIB", "hh3cDot11SaTrapRadioID"),
        ("HH3C-DOT11-SA-MIB", "hh3cDot11SaTrapChlNum"),
        ("HH3C-DOT11-SA-MIB", "hh3cDot11SaTrapChlQlt"),
        ("HH3C-DOT11-SA-MIB", "hh3cDot11SaTrapChlIntfNum"))
)
if mibBuilder.loadTexts:
    hh3cDot11SaChlQltRecover.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-DOT11-SA-MIB",
    **{"hh3cDot11Sa": hh3cDot11Sa,
       "hh3cDot11SaCfgGroup": hh3cDot11SaCfgGroup,
       "hh3cDot11SaCfgTable": hh3cDot11SaCfgTable,
       "hh3cDot11SaCfgEntry": hh3cDot11SaCfgEntry,
       "hh3cDot11SaCfgRadioType": hh3cDot11SaCfgRadioType,
       "hh3cDot11SaEnable": hh3cDot11SaEnable,
       "hh3cDot11SaRptDevType": hh3cDot11SaRptDevType,
       "hh3cDot11SaTrapDevEnable": hh3cDot11SaTrapDevEnable,
       "hh3cDot11SaTrapDevType": hh3cDot11SaTrapDevType,
       "hh3cDot11SaTrapAQEnable": hh3cDot11SaTrapAQEnable,
       "hh3cDot11SaTrapAQThreshold": hh3cDot11SaTrapAQThreshold,
       "hh3cDot11SaDrivenRRMEnable": hh3cDot11SaDrivenRRMEnable,
       "hh3cDot11SaDrivenRRMSnt": hh3cDot11SaDrivenRRMSnt,
       "hh3cDot11SaStatusGroup": hh3cDot11SaStatusGroup,
       "hh3cDot11SaRtFFTDataTable": hh3cDot11SaRtFFTDataTable,
       "hh3cDot11SaRtFFTDataEntry": hh3cDot11SaRtFFTDataEntry,
       "hh3cDot11SaAPID": hh3cDot11SaAPID,
       "hh3cDot11SaRadioID": hh3cDot11SaRadioID,
       "hh3cDot11SaRtDataGroupID": hh3cDot11SaRtDataGroupID,
       "hh3cDot11SaFrequency": hh3cDot11SaFrequency,
       "hh3cDot11SaRtFreqPower": hh3cDot11SaRtFreqPower,
       "hh3cDot11SaRtFreqMaxPower": hh3cDot11SaRtFreqMaxPower,
       "hh3cDot11SaRtFreqDutyCycle": hh3cDot11SaRtFreqDutyCycle,
       "hh3cDot11SaRtFreqDataSeqNo": hh3cDot11SaRtFreqDataSeqNo,
       "hh3cDot11SaIntfDevTable": hh3cDot11SaIntfDevTable,
       "hh3cDot11SaIntfDevEntry": hh3cDot11SaIntfDevEntry,
       "hh3cDot11SaDevID": hh3cDot11SaDevID,
       "hh3cDot11SaDevType": hh3cDot11SaDevType,
       "hh3cDot11SaDevSI": hh3cDot11SaDevSI,
       "hh3cDot11SaDevRSSI": hh3cDot11SaDevRSSI,
       "hh3cDot11SaDevDutyCycle": hh3cDot11SaDevDutyCycle,
       "hh3cDot11SaDevAffectedChls": hh3cDot11SaDevAffectedChls,
       "hh3cDot11SaDevDetectedTime": hh3cDot11SaDevDetectedTime,
       "hh3cDot11SaAirQualityTable": hh3cDot11SaAirQualityTable,
       "hh3cDot11SaAirQualityEntry": hh3cDot11SaAirQualityEntry,
       "hh3cDot11SaChlNum": hh3cDot11SaChlNum,
       "hh3cDot11SaAvgQuality": hh3cDot11SaAvgQuality,
       "hh3cDot11SaMinQuality": hh3cDot11SaMinQuality,
       "hh3cDot11SaIntfDevNum": hh3cDot11SaIntfDevNum,
       "hh3cDot11SaWiFiUtil": hh3cDot11SaWiFiUtil,
       "hh3cDot11SaNonWiFiUtil": hh3cDot11SaNonWiFiUtil,
       "hh3cDot11SaNoiseFloor": hh3cDot11SaNoiseFloor,
       "hh3cDot11SaNotifyGroup": hh3cDot11SaNotifyGroup,
       "hh3cDot11SaTraps": hh3cDot11SaTraps,
       "hh3cDot11SaIntfDevDetected": hh3cDot11SaIntfDevDetected,
       "hh3cDot11SaIntfDevDisappear": hh3cDot11SaIntfDevDisappear,
       "hh3cDot11SaChlQltLow": hh3cDot11SaChlQltLow,
       "hh3cDot11SaChlQltRecover": hh3cDot11SaChlQltRecover,
       "hh3cDot11SaTrapVars": hh3cDot11SaTrapVars,
       "hh3cDot11SaTrapAPID": hh3cDot11SaTrapAPID,
       "hh3cDot11SaTrapRadioID": hh3cDot11SaTrapRadioID,
       "hh3cDot11SaTrapDevID": hh3cDot11SaTrapDevID,
       "hh3cDot11SaTrapIntfDevType": hh3cDot11SaTrapIntfDevType,
       "hh3cDot11APTrapDevSI": hh3cDot11APTrapDevSI,
       "hh3cDot11SaTrapDevRSSI": hh3cDot11SaTrapDevRSSI,
       "hh3cDot11APTrapDevDC": hh3cDot11APTrapDevDC,
       "hh3cDot11APTrapDevChls": hh3cDot11APTrapDevChls,
       "hh3cDot11APTrapDevDctTime": hh3cDot11APTrapDevDctTime,
       "hh3cDot11SaTrapChlNum": hh3cDot11SaTrapChlNum,
       "hh3cDot11SaTrapChlQlt": hh3cDot11SaTrapChlQlt,
       "hh3cDot11SaTrapChlIntfNum": hh3cDot11SaTrapChlIntfNum}
)
