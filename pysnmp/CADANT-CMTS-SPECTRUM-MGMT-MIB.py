# SNMP MIB module (CADANT-CMTS-SPECTRUM-MGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CADANT-CMTS-SPECTRUM-MGMT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:52:50 2024
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

(cadIfUpstreamChannelEntry,) = mibBuilder.importSymbols(
    "CADANT-CMTS-UPCHANNEL-MIB",
    "cadIfUpstreamChannelEntry")

(cadSpectrum,) = mibBuilder.importSymbols(
    "CADANT-PRODUCTS-MIB",
    "cadSpectrum")

(TenthdB,) = mibBuilder.importSymbols(
    "DOCS-IF-MIB",
    "TenthdB")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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

(DateAndTime,
 DisplayString,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

cadSpMgtMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 4)
)
cadSpMgtMib.setRevisions(
        ("2013-04-30 00:00",
         "2012-07-03 00:00",
         "2012-07-02 00:00",
         "2006-02-21 00:00",
         "2006-02-06 00:00",
         "2005-11-10 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class SpTriggerType(Integer32, TextualConvention):
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
        *(("degradation", 3),
          ("improvement", 4),
          ("periodic", 2),
          ("tod", 1))
    )



class SpTriggerDay(Integer32, TextualConvention):
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("everyday", 7),
          ("friday", 5),
          ("monday", 1),
          ("saturday", 6),
          ("sunday", 0),
          ("thursday", 4),
          ("tuesday", 2),
          ("wednesday", 3))
    )



class SpTimeOfDay(OctetString, TextualConvention):
    status = "current"
    displayHint = "1d:1d:1d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )



class Unsigned16(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



# MIB Managed Objects in the order of their OIDs

_CadSpMgtNotifications_ObjectIdentity = ObjectIdentity
cadSpMgtNotifications = _CadSpMgtNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 4, 1)
)
_CadSpMgtObjects_ObjectIdentity = ObjectIdentity
cadSpMgtObjects = _CadSpMgtObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 4, 2)
)
_CadSpMgtGroup_ObjectIdentity = ObjectIdentity
cadSpMgtGroup = _CadSpMgtGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 4, 2, 1)
)
_CadSpMgtGroupTable_Object = MibTable
cadSpMgtGroupTable = _CadSpMgtGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 4, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cadSpMgtGroupTable.setStatus("current")
_CadSpMgtGroupEntry_Object = MibTableRow
cadSpMgtGroupEntry = _CadSpMgtGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 4, 2, 1, 1, 1)
)
cadSpMgtGroupEntry.setIndexNames(
    (0, "CADANT-CMTS-SPECTRUM-MGMT-MIB", "cadSpMgtGroupIndex"),
)
if mibBuilder.loadTexts:
    cadSpMgtGroupEntry.setStatus("current")


class _CadSpMgtGroupIndex_Type(Integer32):
    """Custom type cadSpMgtGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 40),
    )


_CadSpMgtGroupIndex_Type.__name__ = "Integer32"
_CadSpMgtGroupIndex_Object = MibTableColumn
cadSpMgtGroupIndex = _CadSpMgtGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 4, 2, 1, 1, 1, 1),
    _CadSpMgtGroupIndex_Type()
)
cadSpMgtGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadSpMgtGroupIndex.setStatus("current")


class _CadSpMgtGroupSamplePeriod_Type(Integer32):
    """Custom type cadSpMgtGroupSamplePeriod based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_CadSpMgtGroupSamplePeriod_Type.__name__ = "Integer32"
_CadSpMgtGroupSamplePeriod_Object = MibTableColumn
cadSpMgtGroupSamplePeriod = _CadSpMgtGroupSamplePeriod_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 4, 2, 1, 1, 1, 2),
    _CadSpMgtGroupSamplePeriod_Type()
)
cadSpMgtGroupSamplePeriod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadSpMgtGroupSamplePeriod.setStatus("current")


class _CadSpMgtGroupHopPeriod_Type(Integer32):
    """Custom type cadSpMgtGroupHopPeriod based on Integer32"""
    defaultValue = 1200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_CadSpMgtGroupHopPeriod_Type.__name__ = "Integer32"
_CadSpMgtGroupHopPeriod_Object = MibTableColumn
cadSpMgtGroupHopPeriod = _CadSpMgtGroupHopPeriod_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 4, 2, 1, 1, 1, 3),
    _CadSpMgtGroupHopPeriod_Type()
)
cadSpMgtGroupHopPeriod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadSpMgtGroupHopPeriod.setStatus("current")


class _CadSpMgtGroupCodeword_Type(Integer32):
    """Custom type cadSpMgtGroupCodeword based on Integer32"""
    defaultValue = 256

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 32768),
    )


_CadSpMgtGroupCodeword_Type.__name__ = "Integer32"
_CadSpMgtGroupCodeword_Object = MibTableColumn
cadSpMgtGroupCodeword = _CadSpMgtGroupCodeword_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 4, 2, 1, 1, 1, 4),
    _CadSpMgtGroupCodeword_Type()
)
cadSpMgtGroupCodeword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadSpMgtGroupCodeword.setStatus("current")


class _CadSpMgtGroupRetryPeriod_Type(Integer32):
    """Custom type cadSpMgtGroupRetryPeriod based on Integer32"""
    defaultValue = 86400

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 604800),
    )


_CadSpMgtGroupRetryPeriod_Type.__name__ = "Integer32"
_CadSpMgtGroupRetryPeriod_Object = MibTableColumn
cadSpMgtGroupRetryPeriod = _CadSpMgtGroupRetryPeriod_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 4, 2, 1, 1, 1, 5),
    _CadSpMgtGroupRetryPeriod_Type()
)
cadSpMgtGroupRetryPeriod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadSpMgtGroupRetryPeriod.setStatus("current")


class _CadSpMgtGroupEnabled_Type(TruthValue):
    """Custom type cadSpMgtGroupEnabled based on TruthValue"""


_CadSpMgtGroupEnabled_Object = MibTableColumn
cadSpMgtGroupEnabled = _CadSpMgtGroupEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 4, 2, 1, 1, 1, 6),
    _CadSpMgtGroupEnabled_Type()
)
cadSpMgtGroupEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadSpMgtGroupEnabled.setStatus("current")
_CadSpMgtGroupRowStatus_Type = RowStatus
_CadSpMgtGroupRowStatus_Object = MibTableColumn
cadSpMgtGroupRowStatus = _CadSpMgtGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 4, 2, 1, 1, 1, 7),
    _CadSpMgtGroupRowStatus_Type()
)
cadSpMgtGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadSpMgtGroupRowStatus.setStatus("current")
_CadSpMgtStateTable_Object = MibTable
cadSpMgtStateTable = _CadSpMgtStateTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 4, 2, 1, 2)
)
if mibBuilder.loadTexts:
    cadSpMgtStateTable.setStatus("current")
_CadSpMgtStateEntry_Object = MibTableRow
cadSpMgtStateEntry = _CadSpMgtStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 4, 2, 1, 2, 1)
)
cadSpMgtStateEntry.setIndexNames(
    (0, "CADANT-CMTS-SPECTRUM-MGMT-MIB", "cadSpMgtGroupIndex"),
    (0, "CADANT-CMTS-SPECTRUM-MGMT-MIB", "cadSpMgtStateIndex"),
)
if mibBuilder.loadTexts:
    cadSpMgtStateEntry.setStatus("current")


class _CadSpMgtStateIndex_Type(Integer32):
    """Custom type cadSpMgtStateIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_CadSpMgtStateIndex_Type.__name__ = "Integer32"
_CadSpMgtStateIndex_Object = MibTableColumn
cadSpMgtStateIndex = _CadSpMgtStateIndex_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 4, 2, 1, 2, 1, 1),
    _CadSpMgtStateIndex_Type()
)
cadSpMgtStateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadSpMgtStateIndex.setStatus("current")


class _CadSpMgtStateFrequency_Type(Integer32):
    """Custom type cadSpMgtStateFrequency based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(5000000, 85000000),
    )


_CadSpMgtStateFrequency_Type.__name__ = "Integer32"
_CadSpMgtStateFrequency_Object = MibTableColumn
cadSpMgtStateFrequency = _CadSpMgtStateFrequency_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 4, 2, 1, 2, 1, 2),
    _CadSpMgtStateFrequency_Type()
)
cadSpMgtStateFrequency.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadSpMgtStateFrequency.setStatus("current")
if mibBuilder.loadTexts:
    cadSpMgtStateFrequency.setUnits("hertz")


class _CadSpMgtStateWidth_Type(Integer32):
    """Custom type cadSpMgtStateWidth based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6400000),
    )


_CadSpMgtStateWidth_Type.__name__ = "Integer32"
_CadSpMgtStateWidth_Object = MibTableColumn
cadSpMgtStateWidth = _CadSpMgtStateWidth_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 4, 2, 1, 2, 1, 3),
    _CadSpMgtStateWidth_Type()
)
cadSpMgtStateWidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadSpMgtStateWidth.setStatus("current")
if mibBuilder.loadTexts:
    cadSpMgtStateWidth.setUnits("hertz")


class _CadSpMgtStateModulationProfile_Type(Unsigned32):
    """Custom type cadSpMgtStateModulationProfile based on Unsigned32"""
    defaultValue = 0


_CadSpMgtStateModulationProfile_Object = MibTableColumn
cadSpMgtStateModulationProfile = _CadSpMgtStateModulationProfile_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 4, 2, 1, 2, 1, 4),
    _CadSpMgtStateModulationProfile_Type()
)
cadSpMgtStateModulationProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadSpMgtStateModulationProfile.setStatus("current")
_CadSpMgtStateRowStatus_Type = RowStatus
_CadSpMgtStateRowStatus_Object = MibTableColumn
cadSpMgtStateRowStatus = _CadSpMgtStateRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 4, 2, 1, 2, 1, 5),
    _CadSpMgtStateRowStatus_Type()
)
cadSpMgtStateRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadSpMgtStateRowStatus.setStatus("current")
_CadSpMgtTriggerTable_Object = MibTable
cadSpMgtTriggerTable = _CadSpMgtTriggerTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 4, 2, 1, 3)
)
if mibBuilder.loadTexts:
    cadSpMgtTriggerTable.setStatus("current")
_CadSpMgtTriggerEntry_Object = MibTableRow
cadSpMgtTriggerEntry = _CadSpMgtTriggerEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 4, 2, 1, 3, 1)
)
cadSpMgtTriggerEntry.setIndexNames(
    (0, "CADANT-CMTS-SPECTRUM-MGMT-MIB", "cadSpMgtTriggerIndex"),
)
if mibBuilder.loadTexts:
    cadSpMgtTriggerEntry.setStatus("current")


class _CadSpMgtTriggerIndex_Type(Integer32):
    """Custom type cadSpMgtTriggerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_CadSpMgtTriggerIndex_Type.__name__ = "Integer32"
_CadSpMgtTriggerIndex_Object = MibTableColumn
cadSpMgtTriggerIndex = _CadSpMgtTriggerIndex_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 4, 2, 1, 3, 1, 1),
    _CadSpMgtTriggerIndex_Type()
)
cadSpMgtTriggerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadSpMgtTriggerIndex.setStatus("current")


class _CadSpMgtTriggerType_Type(SpTriggerType):
    """Custom type cadSpMgtTriggerType based on SpTriggerType"""


_CadSpMgtTriggerType_Object = MibTableColumn
cadSpMgtTriggerType = _CadSpMgtTriggerType_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 4, 2, 1, 3, 1, 2),
    _CadSpMgtTriggerType_Type()
)
cadSpMgtTriggerType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadSpMgtTriggerType.setStatus("current")
_CadSpMgtTriggerDay_Type = SpTriggerDay
_CadSpMgtTriggerDay_Object = MibTableColumn
cadSpMgtTriggerDay = _CadSpMgtTriggerDay_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 4, 2, 1, 3, 1, 3),
    _CadSpMgtTriggerDay_Type()
)
cadSpMgtTriggerDay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadSpMgtTriggerDay.setStatus("current")


class _CadSpMgtTriggerTOD_Type(SpTimeOfDay):
    """Custom type cadSpMgtTriggerTOD based on SpTimeOfDay"""
    defaultHexValue = "000000"


_CadSpMgtTriggerTOD_Object = MibTableColumn
cadSpMgtTriggerTOD = _CadSpMgtTriggerTOD_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 4, 2, 1, 3, 1, 4),
    _CadSpMgtTriggerTOD_Type()
)
cadSpMgtTriggerTOD.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadSpMgtTriggerTOD.setStatus("current")


class _CadSpMgtTriggerPeriod_Type(Integer32):
    """Custom type cadSpMgtTriggerPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 604800),
    )


_CadSpMgtTriggerPeriod_Type.__name__ = "Integer32"
_CadSpMgtTriggerPeriod_Object = MibTableColumn
cadSpMgtTriggerPeriod = _CadSpMgtTriggerPeriod_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 4, 2, 1, 3, 1, 5),
    _CadSpMgtTriggerPeriod_Type()
)
cadSpMgtTriggerPeriod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadSpMgtTriggerPeriod.setStatus("current")
if mibBuilder.loadTexts:
    cadSpMgtTriggerPeriod.setUnits("seconds")


class _CadSpMgtTriggerThres1_Type(Unsigned32):
    """Custom type cadSpMgtTriggerThres1 based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_CadSpMgtTriggerThres1_Type.__name__ = "Unsigned32"
_CadSpMgtTriggerThres1_Object = MibTableColumn
cadSpMgtTriggerThres1 = _CadSpMgtTriggerThres1_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 4, 2, 1, 3, 1, 6),
    _CadSpMgtTriggerThres1_Type()
)
cadSpMgtTriggerThres1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadSpMgtTriggerThres1.setStatus("current")
if mibBuilder.loadTexts:
    cadSpMgtTriggerThres1.setUnits("0.001 percentage")


class _CadSpMgtTriggerThres2_Type(Unsigned32):
    """Custom type cadSpMgtTriggerThres2 based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_CadSpMgtTriggerThres2_Type.__name__ = "Unsigned32"
_CadSpMgtTriggerThres2_Object = MibTableColumn
cadSpMgtTriggerThres2 = _CadSpMgtTriggerThres2_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 4, 2, 1, 3, 1, 7),
    _CadSpMgtTriggerThres2_Type()
)
cadSpMgtTriggerThres2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadSpMgtTriggerThres2.setStatus("current")
if mibBuilder.loadTexts:
    cadSpMgtTriggerThres2.setUnits("0.001 percentage")


class _CadSpMgtTriggerThres3_Type(TenthdB):
    """Custom type cadSpMgtTriggerThres3 based on TenthdB"""
    defaultValue = 1000

    subtypeSpec = TenthdB.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_CadSpMgtTriggerThres3_Type.__name__ = "TenthdB"
_CadSpMgtTriggerThres3_Object = MibTableColumn
cadSpMgtTriggerThres3 = _CadSpMgtTriggerThres3_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 4, 2, 1, 3, 1, 8),
    _CadSpMgtTriggerThres3_Type()
)
cadSpMgtTriggerThres3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadSpMgtTriggerThres3.setStatus("current")
if mibBuilder.loadTexts:
    cadSpMgtTriggerThres3.setUnits("dB")
_CadSpMgtTriggerRowStatus_Type = RowStatus
_CadSpMgtTriggerRowStatus_Object = MibTableColumn
cadSpMgtTriggerRowStatus = _CadSpMgtTriggerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 4, 2, 1, 3, 1, 9),
    _CadSpMgtTriggerRowStatus_Type()
)
cadSpMgtTriggerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadSpMgtTriggerRowStatus.setStatus("current")
_CadSpMgtStateTransTable_Object = MibTable
cadSpMgtStateTransTable = _CadSpMgtStateTransTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 4, 2, 1, 4)
)
if mibBuilder.loadTexts:
    cadSpMgtStateTransTable.setStatus("current")
_CadSpMgtStateTransEntry_Object = MibTableRow
cadSpMgtStateTransEntry = _CadSpMgtStateTransEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 4, 2, 1, 4, 1)
)
cadSpMgtStateTransEntry.setIndexNames(
    (0, "CADANT-CMTS-SPECTRUM-MGMT-MIB", "cadSpMgtGroupIndex"),
    (0, "CADANT-CMTS-SPECTRUM-MGMT-MIB", "cadSpMgtStateIndex"),
    (0, "CADANT-CMTS-SPECTRUM-MGMT-MIB", "cadSpMgtTriggerIndex"),
)
if mibBuilder.loadTexts:
    cadSpMgtStateTransEntry.setStatus("current")


class _CadSpMgtTransNextState_Type(Integer32):
    """Custom type cadSpMgtTransNextState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_CadSpMgtTransNextState_Type.__name__ = "Integer32"
_CadSpMgtTransNextState_Object = MibTableColumn
cadSpMgtTransNextState = _CadSpMgtTransNextState_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 4, 2, 1, 4, 1, 1),
    _CadSpMgtTransNextState_Type()
)
cadSpMgtTransNextState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadSpMgtTransNextState.setStatus("current")
_CadSpMgtStateTransRowStatus_Type = RowStatus
_CadSpMgtStateTransRowStatus_Object = MibTableColumn
cadSpMgtStateTransRowStatus = _CadSpMgtStateTransRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 4, 2, 1, 4, 1, 2),
    _CadSpMgtStateTransRowStatus_Type()
)
cadSpMgtStateTransRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadSpMgtStateTransRowStatus.setStatus("current")
_CadSpMgtHistoryTable_Object = MibTable
cadSpMgtHistoryTable = _CadSpMgtHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 4, 2, 1, 5)
)
if mibBuilder.loadTexts:
    cadSpMgtHistoryTable.setStatus("current")
_CadSpMgtHistoryEntry_Object = MibTableRow
cadSpMgtHistoryEntry = _CadSpMgtHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 4, 2, 1, 5, 1)
)
cadSpMgtHistoryEntry.setIndexNames(
    (0, "CADANT-CMTS-SPECTRUM-MGMT-MIB", "cadSpMgtHistoryUpChannelIfIndex"),
    (0, "CADANT-CMTS-SPECTRUM-MGMT-MIB", "cadSpMgtHistoryTime"),
)
if mibBuilder.loadTexts:
    cadSpMgtHistoryEntry.setStatus("current")
_CadSpMgtHistoryUpChannelIfIndex_Type = InterfaceIndex
_CadSpMgtHistoryUpChannelIfIndex_Object = MibTableColumn
cadSpMgtHistoryUpChannelIfIndex = _CadSpMgtHistoryUpChannelIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 4, 2, 1, 5, 1, 1),
    _CadSpMgtHistoryUpChannelIfIndex_Type()
)
cadSpMgtHistoryUpChannelIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadSpMgtHistoryUpChannelIfIndex.setStatus("current")
_CadSpMgtHistoryTime_Type = DateAndTime
_CadSpMgtHistoryTime_Object = MibTableColumn
cadSpMgtHistoryTime = _CadSpMgtHistoryTime_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 4, 2, 1, 5, 1, 2),
    _CadSpMgtHistoryTime_Type()
)
cadSpMgtHistoryTime.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadSpMgtHistoryTime.setStatus("current")
_CadSpMgtHistoryTriggerIndex_Type = Integer32
_CadSpMgtHistoryTriggerIndex_Object = MibTableColumn
cadSpMgtHistoryTriggerIndex = _CadSpMgtHistoryTriggerIndex_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 4, 2, 1, 5, 1, 3),
    _CadSpMgtHistoryTriggerIndex_Type()
)
cadSpMgtHistoryTriggerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSpMgtHistoryTriggerIndex.setStatus("current")
_CadSpMgtHistoryFromStateIndex_Type = Integer32
_CadSpMgtHistoryFromStateIndex_Object = MibTableColumn
cadSpMgtHistoryFromStateIndex = _CadSpMgtHistoryFromStateIndex_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 4, 2, 1, 5, 1, 4),
    _CadSpMgtHistoryFromStateIndex_Type()
)
cadSpMgtHistoryFromStateIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSpMgtHistoryFromStateIndex.setStatus("current")
_CadSpMgtHistoryNextStateIndex_Type = Integer32
_CadSpMgtHistoryNextStateIndex_Object = MibTableColumn
cadSpMgtHistoryNextStateIndex = _CadSpMgtHistoryNextStateIndex_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 4, 2, 1, 5, 1, 5),
    _CadSpMgtHistoryNextStateIndex_Type()
)
cadSpMgtHistoryNextStateIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSpMgtHistoryNextStateIndex.setStatus("current")
_CadSpMgtHistoryResultStateIndex_Type = Integer32
_CadSpMgtHistoryResultStateIndex_Object = MibTableColumn
cadSpMgtHistoryResultStateIndex = _CadSpMgtHistoryResultStateIndex_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 4, 2, 1, 5, 1, 6),
    _CadSpMgtHistoryResultStateIndex_Type()
)
cadSpMgtHistoryResultStateIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSpMgtHistoryResultStateIndex.setStatus("current")
_CadSpMgtHistorySNR_Type = TenthdB
_CadSpMgtHistorySNR_Object = MibTableColumn
cadSpMgtHistorySNR = _CadSpMgtHistorySNR_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 4, 2, 1, 5, 1, 7),
    _CadSpMgtHistorySNR_Type()
)
cadSpMgtHistorySNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSpMgtHistorySNR.setStatus("current")
if mibBuilder.loadTexts:
    cadSpMgtHistorySNR.setUnits("dB")


class _CadSpMgtHistoryUFecError_Type(Unsigned32):
    """Custom type cadSpMgtHistoryUFecError based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_CadSpMgtHistoryUFecError_Type.__name__ = "Unsigned32"
_CadSpMgtHistoryUFecError_Object = MibTableColumn
cadSpMgtHistoryUFecError = _CadSpMgtHistoryUFecError_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 4, 2, 1, 5, 1, 8),
    _CadSpMgtHistoryUFecError_Type()
)
cadSpMgtHistoryUFecError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSpMgtHistoryUFecError.setStatus("current")
if mibBuilder.loadTexts:
    cadSpMgtHistoryUFecError.setUnits("0.001 percentage")


class _CadSpMgtHistoryFecError_Type(Unsigned32):
    """Custom type cadSpMgtHistoryFecError based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_CadSpMgtHistoryFecError_Type.__name__ = "Unsigned32"
_CadSpMgtHistoryFecError_Object = MibTableColumn
cadSpMgtHistoryFecError = _CadSpMgtHistoryFecError_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 4, 2, 1, 5, 1, 9),
    _CadSpMgtHistoryFecError_Type()
)
cadSpMgtHistoryFecError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSpMgtHistoryFecError.setStatus("current")
if mibBuilder.loadTexts:
    cadSpMgtHistoryFecError.setUnits("0.001 percentage")


class _CadSpMgtHistorySpareCardId_Type(Integer32):
    """Custom type cadSpMgtHistorySpareCardId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_CadSpMgtHistorySpareCardId_Type.__name__ = "Integer32"
_CadSpMgtHistorySpareCardId_Object = MibTableColumn
cadSpMgtHistorySpareCardId = _CadSpMgtHistorySpareCardId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 4, 2, 1, 5, 1, 10),
    _CadSpMgtHistorySpareCardId_Type()
)
cadSpMgtHistorySpareCardId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSpMgtHistorySpareCardId.setStatus("current")
_CadSpMgtHistoryText_Type = DisplayString
_CadSpMgtHistoryText_Object = MibTableColumn
cadSpMgtHistoryText = _CadSpMgtHistoryText_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 4, 2, 1, 5, 1, 11),
    _CadSpMgtHistoryText_Type()
)
cadSpMgtHistoryText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSpMgtHistoryText.setStatus("current")
_CadSpMgtHistoryGroupId_Type = Integer32
_CadSpMgtHistoryGroupId_Object = MibTableColumn
cadSpMgtHistoryGroupId = _CadSpMgtHistoryGroupId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 4, 2, 1, 5, 1, 12),
    _CadSpMgtHistoryGroupId_Type()
)
cadSpMgtHistoryGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSpMgtHistoryGroupId.setStatus("current")
_CadSpMgtHistoryStateChangeCount_Type = Unsigned16
_CadSpMgtHistoryStateChangeCount_Object = MibTableColumn
cadSpMgtHistoryStateChangeCount = _CadSpMgtHistoryStateChangeCount_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 4, 2, 1, 5, 1, 13),
    _CadSpMgtHistoryStateChangeCount_Type()
)
cadSpMgtHistoryStateChangeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSpMgtHistoryStateChangeCount.setStatus("current")
_CadSpMgtHistorySysUpTime_Type = Unsigned32
_CadSpMgtHistorySysUpTime_Object = MibTableColumn
cadSpMgtHistorySysUpTime = _CadSpMgtHistorySysUpTime_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 4, 2, 1, 5, 1, 14),
    _CadSpMgtHistorySysUpTime_Type()
)
cadSpMgtHistorySysUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSpMgtHistorySysUpTime.setStatus("current")
_CadSpMgtUpChannelTable_Object = MibTable
cadSpMgtUpChannelTable = _CadSpMgtUpChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 4, 2, 1, 6)
)
if mibBuilder.loadTexts:
    cadSpMgtUpChannelTable.setStatus("current")
_CadSpMgtUpChannelEntry_Object = MibTableRow
cadSpMgtUpChannelEntry = _CadSpMgtUpChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 4, 2, 1, 6, 1)
)
if mibBuilder.loadTexts:
    cadSpMgtUpChannelEntry.setStatus("current")
_CadSpMgtUpChannelCurrState_Type = Integer32
_CadSpMgtUpChannelCurrState_Object = MibTableColumn
cadSpMgtUpChannelCurrState = _CadSpMgtUpChannelCurrState_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 4, 2, 1, 6, 1, 1),
    _CadSpMgtUpChannelCurrState_Type()
)
cadSpMgtUpChannelCurrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSpMgtUpChannelCurrState.setStatus("current")
_CadSpMgtUpChannelStateTransTime_Type = DateAndTime
_CadSpMgtUpChannelStateTransTime_Object = MibTableColumn
cadSpMgtUpChannelStateTransTime = _CadSpMgtUpChannelStateTransTime_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 4, 2, 1, 6, 1, 2),
    _CadSpMgtUpChannelStateTransTime_Type()
)
cadSpMgtUpChannelStateTransTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSpMgtUpChannelStateTransTime.setStatus("current")
_CadSpMgtRequests_ObjectIdentity = ObjectIdentity
cadSpMgtRequests = _CadSpMgtRequests_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 4, 2, 2)
)
_CadSpMgtRequestUpChannelIfIndex_Type = InterfaceIndex
_CadSpMgtRequestUpChannelIfIndex_Object = MibScalar
cadSpMgtRequestUpChannelIfIndex = _CadSpMgtRequestUpChannelIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 4, 2, 2, 1),
    _CadSpMgtRequestUpChannelIfIndex_Type()
)
cadSpMgtRequestUpChannelIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadSpMgtRequestUpChannelIfIndex.setStatus("current")
_CadSpMgtRequestTriggerIndex_Type = Integer32
_CadSpMgtRequestTriggerIndex_Object = MibScalar
cadSpMgtRequestTriggerIndex = _CadSpMgtRequestTriggerIndex_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 4, 2, 2, 2),
    _CadSpMgtRequestTriggerIndex_Type()
)
cadSpMgtRequestTriggerIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadSpMgtRequestTriggerIndex.setStatus("current")
_CadSpMgtRequestNextState_Type = Integer32
_CadSpMgtRequestNextState_Object = MibScalar
cadSpMgtRequestNextState = _CadSpMgtRequestNextState_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 4, 2, 2, 3),
    _CadSpMgtRequestNextState_Type()
)
cadSpMgtRequestNextState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadSpMgtRequestNextState.setStatus("current")
_CadSpMgtRequestSNR_Type = TenthdB
_CadSpMgtRequestSNR_Object = MibScalar
cadSpMgtRequestSNR = _CadSpMgtRequestSNR_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 4, 2, 2, 4),
    _CadSpMgtRequestSNR_Type()
)
cadSpMgtRequestSNR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadSpMgtRequestSNR.setStatus("current")
if mibBuilder.loadTexts:
    cadSpMgtRequestSNR.setUnits("dB")


class _CadSpMgtRequestUFecError_Type(Unsigned32):
    """Custom type cadSpMgtRequestUFecError based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_CadSpMgtRequestUFecError_Type.__name__ = "Unsigned32"
_CadSpMgtRequestUFecError_Object = MibScalar
cadSpMgtRequestUFecError = _CadSpMgtRequestUFecError_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 4, 2, 2, 5),
    _CadSpMgtRequestUFecError_Type()
)
cadSpMgtRequestUFecError.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadSpMgtRequestUFecError.setStatus("current")
if mibBuilder.loadTexts:
    cadSpMgtRequestUFecError.setUnits("0.001 percentage")


class _CadSpMgtRequestFecError_Type(Unsigned32):
    """Custom type cadSpMgtRequestFecError based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_CadSpMgtRequestFecError_Type.__name__ = "Unsigned32"
_CadSpMgtRequestFecError_Object = MibScalar
cadSpMgtRequestFecError = _CadSpMgtRequestFecError_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 4, 2, 2, 6),
    _CadSpMgtRequestFecError_Type()
)
cadSpMgtRequestFecError.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadSpMgtRequestFecError.setStatus("current")
if mibBuilder.loadTexts:
    cadSpMgtRequestFecError.setUnits("0.001 percentage")


class _CadSpMgtRequestCommit_Type(TruthValue):
    """Custom type cadSpMgtRequestCommit based on TruthValue"""


_CadSpMgtRequestCommit_Object = MibScalar
cadSpMgtRequestCommit = _CadSpMgtRequestCommit_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 4, 2, 2, 7),
    _CadSpMgtRequestCommit_Type()
)
cadSpMgtRequestCommit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadSpMgtRequestCommit.setStatus("current")
_CadSpMgtConformance_ObjectIdentity = ObjectIdentity
cadSpMgtConformance = _CadSpMgtConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 4, 3)
)
cadIfUpstreamChannelEntry.registerAugmentions(
    ("CADANT-CMTS-SPECTRUM-MGMT-MIB",
     "cadSpMgtUpChannelEntry")
)
cadSpMgtUpChannelEntry.setIndexNames(*cadIfUpstreamChannelEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CADANT-CMTS-SPECTRUM-MGMT-MIB",
    **{"SpTriggerType": SpTriggerType,
       "SpTriggerDay": SpTriggerDay,
       "SpTimeOfDay": SpTimeOfDay,
       "Unsigned16": Unsigned16,
       "cadSpMgtMib": cadSpMgtMib,
       "cadSpMgtNotifications": cadSpMgtNotifications,
       "cadSpMgtObjects": cadSpMgtObjects,
       "cadSpMgtGroup": cadSpMgtGroup,
       "cadSpMgtGroupTable": cadSpMgtGroupTable,
       "cadSpMgtGroupEntry": cadSpMgtGroupEntry,
       "cadSpMgtGroupIndex": cadSpMgtGroupIndex,
       "cadSpMgtGroupSamplePeriod": cadSpMgtGroupSamplePeriod,
       "cadSpMgtGroupHopPeriod": cadSpMgtGroupHopPeriod,
       "cadSpMgtGroupCodeword": cadSpMgtGroupCodeword,
       "cadSpMgtGroupRetryPeriod": cadSpMgtGroupRetryPeriod,
       "cadSpMgtGroupEnabled": cadSpMgtGroupEnabled,
       "cadSpMgtGroupRowStatus": cadSpMgtGroupRowStatus,
       "cadSpMgtStateTable": cadSpMgtStateTable,
       "cadSpMgtStateEntry": cadSpMgtStateEntry,
       "cadSpMgtStateIndex": cadSpMgtStateIndex,
       "cadSpMgtStateFrequency": cadSpMgtStateFrequency,
       "cadSpMgtStateWidth": cadSpMgtStateWidth,
       "cadSpMgtStateModulationProfile": cadSpMgtStateModulationProfile,
       "cadSpMgtStateRowStatus": cadSpMgtStateRowStatus,
       "cadSpMgtTriggerTable": cadSpMgtTriggerTable,
       "cadSpMgtTriggerEntry": cadSpMgtTriggerEntry,
       "cadSpMgtTriggerIndex": cadSpMgtTriggerIndex,
       "cadSpMgtTriggerType": cadSpMgtTriggerType,
       "cadSpMgtTriggerDay": cadSpMgtTriggerDay,
       "cadSpMgtTriggerTOD": cadSpMgtTriggerTOD,
       "cadSpMgtTriggerPeriod": cadSpMgtTriggerPeriod,
       "cadSpMgtTriggerThres1": cadSpMgtTriggerThres1,
       "cadSpMgtTriggerThres2": cadSpMgtTriggerThres2,
       "cadSpMgtTriggerThres3": cadSpMgtTriggerThres3,
       "cadSpMgtTriggerRowStatus": cadSpMgtTriggerRowStatus,
       "cadSpMgtStateTransTable": cadSpMgtStateTransTable,
       "cadSpMgtStateTransEntry": cadSpMgtStateTransEntry,
       "cadSpMgtTransNextState": cadSpMgtTransNextState,
       "cadSpMgtStateTransRowStatus": cadSpMgtStateTransRowStatus,
       "cadSpMgtHistoryTable": cadSpMgtHistoryTable,
       "cadSpMgtHistoryEntry": cadSpMgtHistoryEntry,
       "cadSpMgtHistoryUpChannelIfIndex": cadSpMgtHistoryUpChannelIfIndex,
       "cadSpMgtHistoryTime": cadSpMgtHistoryTime,
       "cadSpMgtHistoryTriggerIndex": cadSpMgtHistoryTriggerIndex,
       "cadSpMgtHistoryFromStateIndex": cadSpMgtHistoryFromStateIndex,
       "cadSpMgtHistoryNextStateIndex": cadSpMgtHistoryNextStateIndex,
       "cadSpMgtHistoryResultStateIndex": cadSpMgtHistoryResultStateIndex,
       "cadSpMgtHistorySNR": cadSpMgtHistorySNR,
       "cadSpMgtHistoryUFecError": cadSpMgtHistoryUFecError,
       "cadSpMgtHistoryFecError": cadSpMgtHistoryFecError,
       "cadSpMgtHistorySpareCardId": cadSpMgtHistorySpareCardId,
       "cadSpMgtHistoryText": cadSpMgtHistoryText,
       "cadSpMgtHistoryGroupId": cadSpMgtHistoryGroupId,
       "cadSpMgtHistoryStateChangeCount": cadSpMgtHistoryStateChangeCount,
       "cadSpMgtHistorySysUpTime": cadSpMgtHistorySysUpTime,
       "cadSpMgtUpChannelTable": cadSpMgtUpChannelTable,
       "cadSpMgtUpChannelEntry": cadSpMgtUpChannelEntry,
       "cadSpMgtUpChannelCurrState": cadSpMgtUpChannelCurrState,
       "cadSpMgtUpChannelStateTransTime": cadSpMgtUpChannelStateTransTime,
       "cadSpMgtRequests": cadSpMgtRequests,
       "cadSpMgtRequestUpChannelIfIndex": cadSpMgtRequestUpChannelIfIndex,
       "cadSpMgtRequestTriggerIndex": cadSpMgtRequestTriggerIndex,
       "cadSpMgtRequestNextState": cadSpMgtRequestNextState,
       "cadSpMgtRequestSNR": cadSpMgtRequestSNR,
       "cadSpMgtRequestUFecError": cadSpMgtRequestUFecError,
       "cadSpMgtRequestFecError": cadSpMgtRequestFecError,
       "cadSpMgtRequestCommit": cadSpMgtRequestCommit,
       "cadSpMgtConformance": cadSpMgtConformance}
)
