# SNMP MIB module (SCTE-HMS-QAM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SCTE-HMS-QAM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:50:08 2024
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

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(QAMChannelInterleaveMode,
 QAMChannelModulationFormat) = mibBuilder.importSymbols(
    "SCTE-HMS-HEADENDIDENT-TC-MIB",
    "QAMChannelInterleaveMode",
    "QAMChannelModulationFormat")

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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

heDigitalQamMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 3, 1)
)
heDigitalQamMIB.setRevisions(
        ("2008-07-16 03:05",
         "2008-04-18 10:55",
         "2008-02-04 18:50",
         "2007-12-17 11:50",
         "2007-10-03 17:00",
         "2007-10-02 12:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_QamMIBObjects_ObjectIdentity = ObjectIdentity
qamMIBObjects = _QamMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 3, 1, 1)
)
if mibBuilder.loadTexts:
    qamMIBObjects.setStatus("current")
_QamChannelTable_Object = MibTable
qamChannelTable = _QamChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 3, 1, 1, 1)
)
if mibBuilder.loadTexts:
    qamChannelTable.setStatus("current")
_QamChannelEntry_Object = MibTableRow
qamChannelEntry = _QamChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 3, 1, 1, 1, 1)
)
qamChannelEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    qamChannelEntry.setStatus("current")
_QamChannelFrequency_Type = Unsigned32
_QamChannelFrequency_Object = MibTableColumn
qamChannelFrequency = _QamChannelFrequency_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 3, 1, 1, 1, 1, 1),
    _QamChannelFrequency_Type()
)
qamChannelFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qamChannelFrequency.setStatus("current")
if mibBuilder.loadTexts:
    qamChannelFrequency.setUnits("Hertz")
_QamChannelModulationFormat_Type = QAMChannelModulationFormat
_QamChannelModulationFormat_Object = MibTableColumn
qamChannelModulationFormat = _QamChannelModulationFormat_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 3, 1, 1, 1, 1, 2),
    _QamChannelModulationFormat_Type()
)
qamChannelModulationFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qamChannelModulationFormat.setStatus("current")


class _QamChannelInterleaverLevel_Type(Integer32):
    """Custom type qamChannelInterleaverLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("level1", 1),
          ("level2", 2))
    )


_QamChannelInterleaverLevel_Type.__name__ = "Integer32"
_QamChannelInterleaverLevel_Object = MibTableColumn
qamChannelInterleaverLevel = _QamChannelInterleaverLevel_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 3, 1, 1, 1, 1, 3),
    _QamChannelInterleaverLevel_Type()
)
qamChannelInterleaverLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qamChannelInterleaverLevel.setStatus("current")
_QamChannelInterleaverMode_Type = QAMChannelInterleaveMode
_QamChannelInterleaverMode_Object = MibTableColumn
qamChannelInterleaverMode = _QamChannelInterleaverMode_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 3, 1, 1, 1, 1, 4),
    _QamChannelInterleaverMode_Type()
)
qamChannelInterleaverMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qamChannelInterleaverMode.setStatus("current")
_QamChannelPower_Type = Integer32
_QamChannelPower_Object = MibTableColumn
qamChannelPower = _QamChannelPower_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 3, 1, 1, 1, 1, 5),
    _QamChannelPower_Type()
)
qamChannelPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qamChannelPower.setStatus("current")
if mibBuilder.loadTexts:
    qamChannelPower.setUnits("0.1 dBmV")


class _QamChannelSquelch_Type(Integer32):
    """Custom type qamChannelSquelch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("muted", 2),
          ("unmuted", 1))
    )


_QamChannelSquelch_Type.__name__ = "Integer32"
_QamChannelSquelch_Object = MibTableColumn
qamChannelSquelch = _QamChannelSquelch_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 3, 1, 1, 1, 1, 6),
    _QamChannelSquelch_Type()
)
qamChannelSquelch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qamChannelSquelch.setStatus("current")


class _QamChannelContWaveMode_Type(Integer32):
    """Custom type qamChannelContWaveMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cwmOff", 1),
          ("cwmOn", 2))
    )


_QamChannelContWaveMode_Type.__name__ = "Integer32"
_QamChannelContWaveMode_Object = MibTableColumn
qamChannelContWaveMode = _QamChannelContWaveMode_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 3, 1, 1, 1, 1, 7),
    _QamChannelContWaveMode_Type()
)
qamChannelContWaveMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qamChannelContWaveMode.setStatus("current")


class _QamChannelAnnexMode_Type(Integer32):
    """Custom type qamChannelAnnexMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("annexA", 3),
          ("annexB", 4),
          ("annexC", 5),
          ("other", 2),
          ("unknown", 1))
    )


_QamChannelAnnexMode_Type.__name__ = "Integer32"
_QamChannelAnnexMode_Object = MibTableColumn
qamChannelAnnexMode = _QamChannelAnnexMode_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 3, 1, 1, 1, 1, 8),
    _QamChannelAnnexMode_Type()
)
qamChannelAnnexMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qamChannelAnnexMode.setStatus("current")
_QamChannelCommonTable_Object = MibTable
qamChannelCommonTable = _QamChannelCommonTable_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 3, 1, 1, 2)
)
if mibBuilder.loadTexts:
    qamChannelCommonTable.setStatus("current")
_QamChannelCommonEntry_Object = MibTableRow
qamChannelCommonEntry = _QamChannelCommonEntry_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 3, 1, 1, 2, 1)
)
qamChannelCommonEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    qamChannelCommonEntry.setStatus("current")
_QamChannelCommonOutputBw_Type = Integer32
_QamChannelCommonOutputBw_Object = MibTableColumn
qamChannelCommonOutputBw = _QamChannelCommonOutputBw_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 3, 1, 1, 2, 1, 1),
    _QamChannelCommonOutputBw_Type()
)
qamChannelCommonOutputBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qamChannelCommonOutputBw.setStatus("current")
if mibBuilder.loadTexts:
    qamChannelCommonOutputBw.setUnits("bps")


class _QamChannelCommonUtilization_Type(Integer32):
    """Custom type qamChannelCommonUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 1000),
    )


_QamChannelCommonUtilization_Type.__name__ = "Integer32"
_QamChannelCommonUtilization_Object = MibTableColumn
qamChannelCommonUtilization = _QamChannelCommonUtilization_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 3, 1, 1, 2, 1, 2),
    _QamChannelCommonUtilization_Type()
)
qamChannelCommonUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qamChannelCommonUtilization.setStatus("current")
if mibBuilder.loadTexts:
    qamChannelCommonUtilization.setUnits("0.1 Percent")
_QamConfigTable_Object = MibTable
qamConfigTable = _QamConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 3, 1, 1, 3)
)
if mibBuilder.loadTexts:
    qamConfigTable.setStatus("current")
_QamConfigEntry_Object = MibTableRow
qamConfigEntry = _QamConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 3, 1, 1, 3, 1)
)
qamConfigEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "SCTE-HMS-QAM-MIB", "qamConfigIndex"),
)
if mibBuilder.loadTexts:
    qamConfigEntry.setStatus("current")
_QamConfigIndex_Type = Unsigned32
_QamConfigIndex_Object = MibTableColumn
qamConfigIndex = _QamConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 3, 1, 1, 3, 1, 1),
    _QamConfigIndex_Type()
)
qamConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qamConfigIndex.setStatus("current")


class _QamConfigQamChannelIdMin_Type(Integer32):
    """Custom type qamConfigQamChannelIdMin based on Integer32"""
    defaultValue = 1


_QamConfigQamChannelIdMin_Object = MibTableColumn
qamConfigQamChannelIdMin = _QamConfigQamChannelIdMin_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 3, 1, 1, 3, 1, 2),
    _QamConfigQamChannelIdMin_Type()
)
qamConfigQamChannelIdMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qamConfigQamChannelIdMin.setStatus("current")
_QamConfigQamChannelIdMax_Type = Integer32
_QamConfigQamChannelIdMax_Object = MibTableColumn
qamConfigQamChannelIdMax = _QamConfigQamChannelIdMax_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 3, 1, 1, 3, 1, 3),
    _QamConfigQamChannelIdMax_Type()
)
qamConfigQamChannelIdMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qamConfigQamChannelIdMax.setStatus("current")


class _QamConfigIPAddrType_Type(InetAddressType):
    """Custom type qamConfigIPAddrType based on InetAddressType"""


_QamConfigIPAddrType_Object = MibTableColumn
qamConfigIPAddrType = _QamConfigIPAddrType_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 3, 1, 1, 3, 1, 4),
    _QamConfigIPAddrType_Type()
)
qamConfigIPAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qamConfigIPAddrType.setStatus("current")
_QamConfigIPAddr_Type = InetAddress
_QamConfigIPAddr_Object = MibTableColumn
qamConfigIPAddr = _QamConfigIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 3, 1, 1, 3, 1, 5),
    _QamConfigIPAddr_Type()
)
qamConfigIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qamConfigIPAddr.setStatus("current")


class _QamConfigUdpPortRangeMin_Type(Integer32):
    """Custom type qamConfigUdpPortRangeMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_QamConfigUdpPortRangeMin_Type.__name__ = "Integer32"
_QamConfigUdpPortRangeMin_Object = MibTableColumn
qamConfigUdpPortRangeMin = _QamConfigUdpPortRangeMin_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 3, 1, 1, 3, 1, 6),
    _QamConfigUdpPortRangeMin_Type()
)
qamConfigUdpPortRangeMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qamConfigUdpPortRangeMin.setStatus("current")


class _QamConfigUdpPortRangeMax_Type(Integer32):
    """Custom type qamConfigUdpPortRangeMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_QamConfigUdpPortRangeMax_Type.__name__ = "Integer32"
_QamConfigUdpPortRangeMax_Object = MibTableColumn
qamConfigUdpPortRangeMax = _QamConfigUdpPortRangeMax_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 3, 1, 1, 3, 1, 7),
    _QamConfigUdpPortRangeMax_Type()
)
qamConfigUdpPortRangeMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qamConfigUdpPortRangeMax.setStatus("current")


class _QamConfigOutputProgNoMin_Type(Integer32):
    """Custom type qamConfigOutputProgNoMin based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_QamConfigOutputProgNoMin_Type.__name__ = "Integer32"
_QamConfigOutputProgNoMin_Object = MibTableColumn
qamConfigOutputProgNoMin = _QamConfigOutputProgNoMin_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 3, 1, 1, 3, 1, 8),
    _QamConfigOutputProgNoMin_Type()
)
qamConfigOutputProgNoMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qamConfigOutputProgNoMin.setStatus("current")


class _QamConfigOutputProgNoMax_Type(Integer32):
    """Custom type qamConfigOutputProgNoMax based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_QamConfigOutputProgNoMax_Type.__name__ = "Integer32"
_QamConfigOutputProgNoMax_Object = MibTableColumn
qamConfigOutputProgNoMax = _QamConfigOutputProgNoMax_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 3, 1, 1, 3, 1, 9),
    _QamConfigOutputProgNoMax_Type()
)
qamConfigOutputProgNoMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qamConfigOutputProgNoMax.setStatus("current")
_QamMIBConformance_ObjectIdentity = ObjectIdentity
qamMIBConformance = _QamMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 3, 1, 2)
)
if mibBuilder.loadTexts:
    qamMIBConformance.setStatus("current")
_QamMIBCompliances_ObjectIdentity = ObjectIdentity
qamMIBCompliances = _QamMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 3, 1, 2, 1)
)
if mibBuilder.loadTexts:
    qamMIBCompliances.setStatus("current")
_QamMIBGroups_ObjectIdentity = ObjectIdentity
qamMIBGroups = _QamMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 3, 1, 2, 2)
)
if mibBuilder.loadTexts:
    qamMIBGroups.setStatus("current")

# Managed Objects groups

qamMpegDocsisCommonGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 3, 1, 2, 2, 1)
)
qamMpegDocsisCommonGroup.setObjects(
      *(("SCTE-HMS-QAM-MIB", "qamChannelCommonOutputBw"),
        ("SCTE-HMS-QAM-MIB", "qamChannelCommonUtilization"))
)
if mibBuilder.loadTexts:
    qamMpegDocsisCommonGroup.setStatus("current")

qamChannelGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 3, 1, 2, 2, 2)
)
qamChannelGroup.setObjects(
      *(("SCTE-HMS-QAM-MIB", "qamChannelFrequency"),
        ("SCTE-HMS-QAM-MIB", "qamChannelModulationFormat"),
        ("SCTE-HMS-QAM-MIB", "qamChannelInterleaverLevel"),
        ("SCTE-HMS-QAM-MIB", "qamChannelInterleaverMode"),
        ("SCTE-HMS-QAM-MIB", "qamChannelPower"),
        ("SCTE-HMS-QAM-MIB", "qamChannelSquelch"),
        ("SCTE-HMS-QAM-MIB", "qamChannelContWaveMode"),
        ("SCTE-HMS-QAM-MIB", "qamChannelAnnexMode"))
)
if mibBuilder.loadTexts:
    qamChannelGroup.setStatus("current")

qamConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 3, 1, 2, 2, 3)
)
qamConfigGroup.setObjects(
      *(("SCTE-HMS-QAM-MIB", "qamConfigQamChannelIdMin"),
        ("SCTE-HMS-QAM-MIB", "qamConfigQamChannelIdMax"),
        ("SCTE-HMS-QAM-MIB", "qamConfigIPAddrType"),
        ("SCTE-HMS-QAM-MIB", "qamConfigIPAddr"),
        ("SCTE-HMS-QAM-MIB", "qamConfigUdpPortRangeMin"),
        ("SCTE-HMS-QAM-MIB", "qamConfigUdpPortRangeMax"),
        ("SCTE-HMS-QAM-MIB", "qamConfigOutputProgNoMin"),
        ("SCTE-HMS-QAM-MIB", "qamConfigOutputProgNoMax"))
)
if mibBuilder.loadTexts:
    qamConfigGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

qamSupport = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 3, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    qamSupport.setStatus(
        "current"
    )

docsisSupport = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 3, 1, 2, 1, 2)
)
if mibBuilder.loadTexts:
    docsisSupport.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SCTE-HMS-QAM-MIB",
    **{"heDigitalQamMIB": heDigitalQamMIB,
       "qamMIBObjects": qamMIBObjects,
       "qamChannelTable": qamChannelTable,
       "qamChannelEntry": qamChannelEntry,
       "qamChannelFrequency": qamChannelFrequency,
       "qamChannelModulationFormat": qamChannelModulationFormat,
       "qamChannelInterleaverLevel": qamChannelInterleaverLevel,
       "qamChannelInterleaverMode": qamChannelInterleaverMode,
       "qamChannelPower": qamChannelPower,
       "qamChannelSquelch": qamChannelSquelch,
       "qamChannelContWaveMode": qamChannelContWaveMode,
       "qamChannelAnnexMode": qamChannelAnnexMode,
       "qamChannelCommonTable": qamChannelCommonTable,
       "qamChannelCommonEntry": qamChannelCommonEntry,
       "qamChannelCommonOutputBw": qamChannelCommonOutputBw,
       "qamChannelCommonUtilization": qamChannelCommonUtilization,
       "qamConfigTable": qamConfigTable,
       "qamConfigEntry": qamConfigEntry,
       "qamConfigIndex": qamConfigIndex,
       "qamConfigQamChannelIdMin": qamConfigQamChannelIdMin,
       "qamConfigQamChannelIdMax": qamConfigQamChannelIdMax,
       "qamConfigIPAddrType": qamConfigIPAddrType,
       "qamConfigIPAddr": qamConfigIPAddr,
       "qamConfigUdpPortRangeMin": qamConfigUdpPortRangeMin,
       "qamConfigUdpPortRangeMax": qamConfigUdpPortRangeMax,
       "qamConfigOutputProgNoMin": qamConfigOutputProgNoMin,
       "qamConfigOutputProgNoMax": qamConfigOutputProgNoMax,
       "qamMIBConformance": qamMIBConformance,
       "qamMIBCompliances": qamMIBCompliances,
       "qamSupport": qamSupport,
       "docsisSupport": docsisSupport,
       "qamMIBGroups": qamMIBGroups,
       "qamMpegDocsisCommonGroup": qamMpegDocsisCommonGroup,
       "qamChannelGroup": qamChannelGroup,
       "qamConfigGroup": qamConfigGroup}
)
