# SNMP MIB module (Amperion-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Amperion-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:45:05 2024
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
 Opaque,
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
    "Opaque",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

amperion = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 13995)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ds2_ObjectIdentity = ObjectIdentity
ds2 = _Ds2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13995, 1)
)
_Powerline_ObjectIdentity = ObjectIdentity
powerline = _Powerline_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13995, 1, 1)
)
_PlMibIIExtension_ObjectIdentity = ObjectIdentity
plMibIIExtension = _PlMibIIExtension_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13995, 1, 1, 1)
)
_PlCards_ObjectIdentity = ObjectIdentity
plCards = _PlCards_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13995, 1, 1, 1, 2)
)
_PlCdNumber_Type = Integer32
_PlCdNumber_Object = MibScalar
plCdNumber = _PlCdNumber_Object(
    (1, 3, 6, 1, 4, 1, 13995, 1, 1, 1, 2, 1),
    _PlCdNumber_Type()
)
plCdNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plCdNumber.setStatus("current")
_PlCdTable_Object = MibTable
plCdTable = _PlCdTable_Object(
    (1, 3, 6, 1, 4, 1, 13995, 1, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    plCdTable.setStatus("current")
_PlCdEntry_Object = MibTableRow
plCdEntry = _PlCdEntry_Object(
    (1, 3, 6, 1, 4, 1, 13995, 1, 1, 1, 2, 2, 1)
)
plCdEntry.setIndexNames(
    (0, "Amperion-MIB", "plCdIndex"),
)
if mibBuilder.loadTexts:
    plCdEntry.setStatus("current")
_PlCdIndex_Type = Integer32
_PlCdIndex_Object = MibTableColumn
plCdIndex = _PlCdIndex_Object(
    (1, 3, 6, 1, 4, 1, 13995, 1, 1, 1, 2, 2, 1, 1),
    _PlCdIndex_Type()
)
plCdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    plCdIndex.setStatus("current")


class _PlCdType_Type(Integer32):
    """Custom type plCdType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("cpe", 1),
          ("he", 0))
    )


_PlCdType_Type.__name__ = "Integer32"
_PlCdType_Object = MibTableColumn
plCdType = _PlCdType_Object(
    (1, 3, 6, 1, 4, 1, 13995, 1, 1, 1, 2, 2, 1, 2),
    _PlCdType_Type()
)
plCdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plCdType.setStatus("current")


class _PlCdLink_Type(Integer32):
    """Custom type plCdLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("link1", 1),
          ("link2", 2),
          ("link3", 3),
          ("link4", 4),
          ("link5", 5),
          ("link6", 6))
    )


_PlCdLink_Type.__name__ = "Integer32"
_PlCdLink_Object = MibTableColumn
plCdLink = _PlCdLink_Object(
    (1, 3, 6, 1, 4, 1, 13995, 1, 1, 1, 2, 2, 1, 3),
    _PlCdLink_Type()
)
plCdLink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plCdLink.setStatus("current")
_PlCdShortMacAddress_Type = Integer32
_PlCdShortMacAddress_Object = MibTableColumn
plCdShortMacAddress = _PlCdShortMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 13995, 1, 1, 1, 2, 2, 1, 4),
    _PlCdShortMacAddress_Type()
)
plCdShortMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plCdShortMacAddress.setStatus("current")


class _PlCdLongMacAddress_Type(DisplayString):
    """Custom type plCdLongMacAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PlCdLongMacAddress_Type.__name__ = "DisplayString"
_PlCdLongMacAddress_Object = MibTableColumn
plCdLongMacAddress = _PlCdLongMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 13995, 1, 1, 1, 2, 2, 1, 5),
    _PlCdLongMacAddress_Type()
)
plCdLongMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plCdLongMacAddress.setStatus("current")


class _PlCdHardwareVersion_Type(DisplayString):
    """Custom type plCdHardwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PlCdHardwareVersion_Type.__name__ = "DisplayString"
_PlCdHardwareVersion_Object = MibTableColumn
plCdHardwareVersion = _PlCdHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 13995, 1, 1, 1, 2, 2, 1, 6),
    _PlCdHardwareVersion_Type()
)
plCdHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plCdHardwareVersion.setStatus("current")


class _PlCdFirmwareVersion_Type(DisplayString):
    """Custom type plCdFirmwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PlCdFirmwareVersion_Type.__name__ = "DisplayString"
_PlCdFirmwareVersion_Object = MibTableColumn
plCdFirmwareVersion = _PlCdFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 13995, 1, 1, 1, 2, 2, 1, 7),
    _PlCdFirmwareVersion_Type()
)
plCdFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plCdFirmwareVersion.setStatus("current")


class _PlCdDriverVersion_Type(DisplayString):
    """Custom type plCdDriverVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PlCdDriverVersion_Type.__name__ = "DisplayString"
_PlCdDriverVersion_Object = MibTableColumn
plCdDriverVersion = _PlCdDriverVersion_Object(
    (1, 3, 6, 1, 4, 1, 13995, 1, 1, 1, 2, 2, 1, 8),
    _PlCdDriverVersion_Type()
)
plCdDriverVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plCdDriverVersion.setStatus("current")
_PlCdReset_Type = Integer32
_PlCdReset_Object = MibTableColumn
plCdReset = _PlCdReset_Object(
    (1, 3, 6, 1, 4, 1, 13995, 1, 1, 1, 2, 2, 1, 9),
    _PlCdReset_Type()
)
plCdReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plCdReset.setStatus("current")
_PlCdFactoryReset_Type = Integer32
_PlCdFactoryReset_Object = MibTableColumn
plCdFactoryReset = _PlCdFactoryReset_Object(
    (1, 3, 6, 1, 4, 1, 13995, 1, 1, 1, 2, 2, 1, 10),
    _PlCdFactoryReset_Type()
)
plCdFactoryReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plCdFactoryReset.setStatus("current")
_PlCdSaveAsPermanent_Type = Integer32
_PlCdSaveAsPermanent_Object = MibTableColumn
plCdSaveAsPermanent = _PlCdSaveAsPermanent_Object(
    (1, 3, 6, 1, 4, 1, 13995, 1, 1, 1, 2, 2, 1, 11),
    _PlCdSaveAsPermanent_Type()
)
plCdSaveAsPermanent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plCdSaveAsPermanent.setStatus("current")
_PlCdStatus_Type = Integer32
_PlCdStatus_Object = MibTableColumn
plCdStatus = _PlCdStatus_Object(
    (1, 3, 6, 1, 4, 1, 13995, 1, 1, 1, 2, 2, 1, 12),
    _PlCdStatus_Type()
)
plCdStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plCdStatus.setStatus("current")


class _PlCdRemoteList_Type(DisplayString):
    """Custom type plCdRemoteList based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PlCdRemoteList_Type.__name__ = "DisplayString"
_PlCdRemoteList_Object = MibTableColumn
plCdRemoteList = _PlCdRemoteList_Object(
    (1, 3, 6, 1, 4, 1, 13995, 1, 1, 1, 2, 2, 1, 13),
    _PlCdRemoteList_Type()
)
plCdRemoteList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plCdRemoteList.setStatus("current")
_PlCdNumRemoteList_Type = Integer32
_PlCdNumRemoteList_Object = MibTableColumn
plCdNumRemoteList = _PlCdNumRemoteList_Object(
    (1, 3, 6, 1, 4, 1, 13995, 1, 1, 1, 2, 2, 1, 14),
    _PlCdNumRemoteList_Type()
)
plCdNumRemoteList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plCdNumRemoteList.setStatus("current")
_PlNetwork_ObjectIdentity = ObjectIdentity
plNetwork = _PlNetwork_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13995, 1, 1, 2)
)
_PlNetTable_Object = MibTable
plNetTable = _PlNetTable_Object(
    (1, 3, 6, 1, 4, 1, 13995, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    plNetTable.setStatus("current")
_PlNetEntry_Object = MibTableRow
plNetEntry = _PlNetEntry_Object(
    (1, 3, 6, 1, 4, 1, 13995, 1, 1, 2, 1, 1)
)
plNetEntry.setIndexNames(
    (0, "Amperion-MIB", "plNetShortMacAddress"),
)
if mibBuilder.loadTexts:
    plNetEntry.setStatus("current")


class _PlNetShortMacAddress_Type(Integer32):
    """Custom type plNetShortMacAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_PlNetShortMacAddress_Type.__name__ = "Integer32"
_PlNetShortMacAddress_Object = MibTableColumn
plNetShortMacAddress = _PlNetShortMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 13995, 1, 1, 2, 1, 1, 1),
    _PlNetShortMacAddress_Type()
)
plNetShortMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    plNetShortMacAddress.setStatus("current")


class _PlNetLongMacAddress_Type(DisplayString):
    """Custom type plNetLongMacAddress based on DisplayString"""
    defaultValue = OctetString("0x000000000000")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_PlNetLongMacAddress_Type.__name__ = "DisplayString"
_PlNetLongMacAddress_Object = MibTableColumn
plNetLongMacAddress = _PlNetLongMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 13995, 1, 1, 2, 1, 1, 3),
    _PlNetLongMacAddress_Type()
)
plNetLongMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    plNetLongMacAddress.setStatus("current")


class _PlNetRowStatus_Type(RowStatus):
    """Custom type plNetRowStatus based on RowStatus"""


_PlNetRowStatus_Object = MibTableColumn
plNetRowStatus = _PlNetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 13995, 1, 1, 2, 1, 1, 8),
    _PlNetRowStatus_Type()
)
plNetRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    plNetRowStatus.setStatus("current")
_PlTransmission_ObjectIdentity = ObjectIdentity
plTransmission = _PlTransmission_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13995, 1, 1, 3)
)
_PlInpTable_Object = MibTable
plInpTable = _PlInpTable_Object(
    (1, 3, 6, 1, 4, 1, 13995, 1, 1, 3, 2)
)
if mibBuilder.loadTexts:
    plInpTable.setStatus("current")
_PlInpEntry_Object = MibTableRow
plInpEntry = _PlInpEntry_Object(
    (1, 3, 6, 1, 4, 1, 13995, 1, 1, 3, 2, 1)
)
plInpEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    plInpEntry.setStatus("current")
_PlInpTotalOctets_Type = Integer32
_PlInpTotalOctets_Object = MibTableColumn
plInpTotalOctets = _PlInpTotalOctets_Object(
    (1, 3, 6, 1, 4, 1, 13995, 1, 1, 3, 2, 1, 1),
    _PlInpTotalOctets_Type()
)
plInpTotalOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plInpTotalOctets.setStatus("current")
_PlInpGain_Type = Integer32
_PlInpGain_Object = MibTableColumn
plInpGain = _PlInpGain_Object(
    (1, 3, 6, 1, 4, 1, 13995, 1, 1, 3, 2, 1, 2),
    _PlInpGain_Type()
)
plInpGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plInpGain.setStatus("current")


class _PlInpAGC_Type(Integer32):
    """Custom type plInpAGC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("agcdisabled", 0),
          ("agcenabled", 1))
    )


_PlInpAGC_Type.__name__ = "Integer32"
_PlInpAGC_Object = MibTableColumn
plInpAGC = _PlInpAGC_Object(
    (1, 3, 6, 1, 4, 1, 13995, 1, 1, 3, 2, 1, 3),
    _PlInpAGC_Type()
)
plInpAGC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plInpAGC.setStatus("current")
_PlInpMaxGain_Type = Integer32
_PlInpMaxGain_Object = MibTableColumn
plInpMaxGain = _PlInpMaxGain_Object(
    (1, 3, 6, 1, 4, 1, 13995, 1, 1, 3, 2, 1, 4),
    _PlInpMaxGain_Type()
)
plInpMaxGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plInpMaxGain.setStatus("current")


class _PlInpThresholds_Type(DisplayString):
    """Custom type plInpThresholds based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PlInpThresholds_Type.__name__ = "DisplayString"
_PlInpThresholds_Object = MibTableColumn
plInpThresholds = _PlInpThresholds_Object(
    (1, 3, 6, 1, 4, 1, 13995, 1, 1, 3, 2, 1, 5),
    _PlInpThresholds_Type()
)
plInpThresholds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plInpThresholds.setStatus("current")
_PlInpAttenuationGain_Type = Integer32
_PlInpAttenuationGain_Object = MibTableColumn
plInpAttenuationGain = _PlInpAttenuationGain_Object(
    (1, 3, 6, 1, 4, 1, 13995, 1, 1, 3, 2, 1, 6),
    _PlInpAttenuationGain_Type()
)
plInpAttenuationGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plInpAttenuationGain.setStatus("current")
_PlInpSamsDecode_Type = Integer32
_PlInpSamsDecode_Object = MibTableColumn
plInpSamsDecode = _PlInpSamsDecode_Object(
    (1, 3, 6, 1, 4, 1, 13995, 1, 1, 3, 2, 1, 7),
    _PlInpSamsDecode_Type()
)
plInpSamsDecode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plInpSamsDecode.setStatus("current")
_PlInpSamsGood_Type = Integer32
_PlInpSamsGood_Object = MibTableColumn
plInpSamsGood = _PlInpSamsGood_Object(
    (1, 3, 6, 1, 4, 1, 13995, 1, 1, 3, 2, 1, 8),
    _PlInpSamsGood_Type()
)
plInpSamsGood.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plInpSamsGood.setStatus("current")
_PlInpSamsBad_Type = Integer32
_PlInpSamsBad_Object = MibTableColumn
plInpSamsBad = _PlInpSamsBad_Object(
    (1, 3, 6, 1, 4, 1, 13995, 1, 1, 3, 2, 1, 9),
    _PlInpSamsBad_Type()
)
plInpSamsBad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plInpSamsBad.setStatus("current")
_PlInpNodeTable_Object = MibTable
plInpNodeTable = _PlInpNodeTable_Object(
    (1, 3, 6, 1, 4, 1, 13995, 1, 1, 3, 4)
)
if mibBuilder.loadTexts:
    plInpNodeTable.setStatus("current")
_PlInpNodeEntry_Object = MibTableRow
plInpNodeEntry = _PlInpNodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 13995, 1, 1, 3, 4, 1)
)
plInpNodeEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "Amperion-MIB", "plNetShortMacAddress"),
)
if mibBuilder.loadTexts:
    plInpNodeEntry.setStatus("current")
_PlInpNodeReceivedPkts_Type = Integer32
_PlInpNodeReceivedPkts_Object = MibTableColumn
plInpNodeReceivedPkts = _PlInpNodeReceivedPkts_Object(
    (1, 3, 6, 1, 4, 1, 13995, 1, 1, 3, 4, 1, 1),
    _PlInpNodeReceivedPkts_Type()
)
plInpNodeReceivedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plInpNodeReceivedPkts.setStatus("current")
_PlInpNodeReceivedUnrecPkts_Type = Integer32
_PlInpNodeReceivedUnrecPkts_Object = MibTableColumn
plInpNodeReceivedUnrecPkts = _PlInpNodeReceivedUnrecPkts_Object(
    (1, 3, 6, 1, 4, 1, 13995, 1, 1, 3, 4, 1, 2),
    _PlInpNodeReceivedUnrecPkts_Type()
)
plInpNodeReceivedUnrecPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plInpNodeReceivedUnrecPkts.setStatus("current")
_PlInpNodeReceivedCorrectedPkts_Type = Integer32
_PlInpNodeReceivedCorrectedPkts_Object = MibTableColumn
plInpNodeReceivedCorrectedPkts = _PlInpNodeReceivedCorrectedPkts_Object(
    (1, 3, 6, 1, 4, 1, 13995, 1, 1, 3, 4, 1, 3),
    _PlInpNodeReceivedCorrectedPkts_Type()
)
plInpNodeReceivedCorrectedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plInpNodeReceivedCorrectedPkts.setStatus("current")
_PlInpNodeReceivedOctets_Type = Integer32
_PlInpNodeReceivedOctets_Object = MibTableColumn
plInpNodeReceivedOctets = _PlInpNodeReceivedOctets_Object(
    (1, 3, 6, 1, 4, 1, 13995, 1, 1, 3, 4, 1, 4),
    _PlInpNodeReceivedOctets_Type()
)
plInpNodeReceivedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plInpNodeReceivedOctets.setStatus("current")
_PlInpNodeReceivedCorrectedOctets_Type = Integer32
_PlInpNodeReceivedCorrectedOctets_Object = MibTableColumn
plInpNodeReceivedCorrectedOctets = _PlInpNodeReceivedCorrectedOctets_Object(
    (1, 3, 6, 1, 4, 1, 13995, 1, 1, 3, 4, 1, 5),
    _PlInpNodeReceivedCorrectedOctets_Type()
)
plInpNodeReceivedCorrectedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plInpNodeReceivedCorrectedOctets.setStatus("current")
_PlInpNodeReceivedPower_Type = Integer32
_PlInpNodeReceivedPower_Object = MibTableColumn
plInpNodeReceivedPower = _PlInpNodeReceivedPower_Object(
    (1, 3, 6, 1, 4, 1, 13995, 1, 1, 3, 4, 1, 6),
    _PlInpNodeReceivedPower_Type()
)
plInpNodeReceivedPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plInpNodeReceivedPower.setStatus("current")
_PlInpNodePLR_Type = Integer32
_PlInpNodePLR_Object = MibTableColumn
plInpNodePLR = _PlInpNodePLR_Object(
    (1, 3, 6, 1, 4, 1, 13995, 1, 1, 3, 4, 1, 7),
    _PlInpNodePLR_Type()
)
plInpNodePLR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plInpNodePLR.setStatus("current")
_PlInpNodeMeanBPC_Type = Integer32
_PlInpNodeMeanBPC_Object = MibTableColumn
plInpNodeMeanBPC = _PlInpNodeMeanBPC_Object(
    (1, 3, 6, 1, 4, 1, 13995, 1, 1, 3, 4, 1, 8),
    _PlInpNodeMeanBPC_Type()
)
plInpNodeMeanBPC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plInpNodeMeanBPC.setStatus("current")
_PlInpNodeSNRChanges_Type = Integer32
_PlInpNodeSNRChanges_Object = MibTableColumn
plInpNodeSNRChanges = _PlInpNodeSNRChanges_Object(
    (1, 3, 6, 1, 4, 1, 13995, 1, 1, 3, 4, 1, 9),
    _PlInpNodeSNRChanges_Type()
)
plInpNodeSNRChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plInpNodeSNRChanges.setStatus("current")


class _PlInpNodeSNR_Type(DisplayString):
    """Custom type plInpNodeSNR based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PlInpNodeSNR_Type.__name__ = "DisplayString"
_PlInpNodeSNR_Object = MibTableColumn
plInpNodeSNR = _PlInpNodeSNR_Object(
    (1, 3, 6, 1, 4, 1, 13995, 1, 1, 3, 4, 1, 10),
    _PlInpNodeSNR_Type()
)
plInpNodeSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plInpNodeSNR.setStatus("current")


class _PlInpNodeBPC_Type(DisplayString):
    """Custom type plInpNodeBPC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PlInpNodeBPC_Type.__name__ = "DisplayString"
_PlInpNodeBPC_Object = MibTableColumn
plInpNodeBPC = _PlInpNodeBPC_Object(
    (1, 3, 6, 1, 4, 1, 13995, 1, 1, 3, 4, 1, 11),
    _PlInpNodeBPC_Type()
)
plInpNodeBPC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plInpNodeBPC.setStatus("current")


class _PlInpNodeCFR_Type(DisplayString):
    """Custom type plInpNodeCFR based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PlInpNodeCFR_Type.__name__ = "DisplayString"
_PlInpNodeCFR_Object = MibTableColumn
plInpNodeCFR = _PlInpNodeCFR_Object(
    (1, 3, 6, 1, 4, 1, 13995, 1, 1, 3, 4, 1, 12),
    _PlInpNodeCFR_Type()
)
plInpNodeCFR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plInpNodeCFR.setStatus("current")


class _PlInpNodeEnableCarriers_Type(DisplayString):
    """Custom type plInpNodeEnableCarriers based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PlInpNodeEnableCarriers_Type.__name__ = "DisplayString"
_PlInpNodeEnableCarriers_Object = MibTableColumn
plInpNodeEnableCarriers = _PlInpNodeEnableCarriers_Object(
    (1, 3, 6, 1, 4, 1, 13995, 1, 1, 3, 4, 1, 13),
    _PlInpNodeEnableCarriers_Type()
)
plInpNodeEnableCarriers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plInpNodeEnableCarriers.setStatus("current")


class _PlInpNodeProtocolEnableCarriers_Type(DisplayString):
    """Custom type plInpNodeProtocolEnableCarriers based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PlInpNodeProtocolEnableCarriers_Type.__name__ = "DisplayString"
_PlInpNodeProtocolEnableCarriers_Object = MibTableColumn
plInpNodeProtocolEnableCarriers = _PlInpNodeProtocolEnableCarriers_Object(
    (1, 3, 6, 1, 4, 1, 13995, 1, 1, 3, 4, 1, 14),
    _PlInpNodeProtocolEnableCarriers_Type()
)
plInpNodeProtocolEnableCarriers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plInpNodeProtocolEnableCarriers.setStatus("current")
_PlInpNodeEnableProtocolEnableCarriers_Type = Integer32
_PlInpNodeEnableProtocolEnableCarriers_Object = MibTableColumn
plInpNodeEnableProtocolEnableCarriers = _PlInpNodeEnableProtocolEnableCarriers_Object(
    (1, 3, 6, 1, 4, 1, 13995, 1, 1, 3, 4, 1, 15),
    _PlInpNodeEnableProtocolEnableCarriers_Type()
)
plInpNodeEnableProtocolEnableCarriers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plInpNodeEnableProtocolEnableCarriers.setStatus("current")
_PlTraps_ObjectIdentity = ObjectIdentity
plTraps = _PlTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13995, 1, 1, 4)
)
_PlRemoteCPE_ObjectIdentity = ObjectIdentity
plRemoteCPE = _PlRemoteCPE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13995, 1, 1, 5)
)
_Internal_ObjectIdentity = ObjectIdentity
internal = _Internal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13995, 1, 2)
)
_AmperionSystem_ObjectIdentity = ObjectIdentity
amperionSystem = _AmperionSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13995, 2)
)


class _SerialNumber_Type(DisplayString):
    """Custom type serialNumber based on DisplayString"""
    defaultValue = OctetString("####")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SerialNumber_Type.__name__ = "DisplayString"
_SerialNumber_Object = MibScalar
serialNumber = _SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 13995, 2, 1),
    _SerialNumber_Type()
)
serialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialNumber.setStatus("current")


class _PartNumber_Type(DisplayString):
    """Custom type partNumber based on DisplayString"""
    defaultValue = OctetString("####")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PartNumber_Type.__name__ = "DisplayString"
_PartNumber_Object = MibScalar
partNumber = _PartNumber_Object(
    (1, 3, 6, 1, 4, 1, 13995, 2, 2),
    _PartNumber_Type()
)
partNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    partNumber.setStatus("current")


class _RombootVersion_Type(DisplayString):
    """Custom type rombootVersion based on DisplayString"""
    defaultValue = OctetString("####")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_RombootVersion_Type.__name__ = "DisplayString"
_RombootVersion_Object = MibScalar
rombootVersion = _RombootVersion_Object(
    (1, 3, 6, 1, 4, 1, 13995, 2, 3),
    _RombootVersion_Type()
)
rombootVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rombootVersion.setStatus("current")
_Alarms_Object = MibTable
alarms = _Alarms_Object(
    (1, 3, 6, 1, 4, 1, 13995, 2, 4)
)
if mibBuilder.loadTexts:
    alarms.setStatus("current")
_AlarmsEntry_Object = MibTableRow
alarmsEntry = _AlarmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 13995, 2, 4, 1)
)
alarmsEntry.setIndexNames(
    (0, "Amperion-MIB", "alarmIndex"),
)
if mibBuilder.loadTexts:
    alarmsEntry.setStatus("current")
_AlarmIndex_Type = Integer32
_AlarmIndex_Object = MibTableColumn
alarmIndex = _AlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 13995, 2, 4, 1, 1),
    _AlarmIndex_Type()
)
alarmIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alarmIndex.setStatus("current")


class _Description_Type(DisplayString):
    """Custom type description based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Description_Type.__name__ = "DisplayString"
_Description_Object = MibTableColumn
description = _Description_Object(
    (1, 3, 6, 1, 4, 1, 13995, 2, 4, 1, 2),
    _Description_Type()
)
description.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    description.setStatus("current")


class _ProductType_Type(Integer32):
    """Custom type productType based on Integer32"""
    defaultValue = 0

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
              8)
        )
    )
    namedValues = NamedValues(
        *(("ohExtractor", 2),
          ("ohInjector", 1),
          ("ohRepeater", 3),
          ("ohRepeaterExt", 4),
          ("ugExtractor", 6),
          ("ugInjector", 5),
          ("ugRepeater", 7),
          ("ugRepeaterExt", 8),
          ("unknown", 0))
    )


_ProductType_Type.__name__ = "Integer32"
_ProductType_Object = MibScalar
productType = _ProductType_Object(
    (1, 3, 6, 1, 4, 1, 13995, 2, 5),
    _ProductType_Type()
)
productType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productType.setStatus("current")


class _UserGpsInfoString_Type(DisplayString):
    """Custom type userGpsInfoString based on DisplayString"""
    defaultValue = OctetString("none")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_UserGpsInfoString_Type.__name__ = "DisplayString"
_UserGpsInfoString_Object = MibScalar
userGpsInfoString = _UserGpsInfoString_Object(
    (1, 3, 6, 1, 4, 1, 13995, 2, 6),
    _UserGpsInfoString_Type()
)
userGpsInfoString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userGpsInfoString.setStatus("current")


class _LinuxVersion_Type(DisplayString):
    """Custom type linuxVersion based on DisplayString"""
    defaultValue = OctetString("####")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_LinuxVersion_Type.__name__ = "DisplayString"
_LinuxVersion_Object = MibScalar
linuxVersion = _LinuxVersion_Object(
    (1, 3, 6, 1, 4, 1, 13995, 2, 8),
    _LinuxVersion_Type()
)
linuxVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linuxVersion.setStatus("current")


class _AmperionSysDescr_Type(DisplayString):
    """Custom type amperionSysDescr based on DisplayString"""
    defaultValue = OctetString("####")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AmperionSysDescr_Type.__name__ = "DisplayString"
_AmperionSysDescr_Object = MibScalar
amperionSysDescr = _AmperionSysDescr_Object(
    (1, 3, 6, 1, 4, 1, 13995, 2, 10),
    _AmperionSysDescr_Type()
)
amperionSysDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amperionSysDescr.setStatus("current")
_AmperionSysObjectID_Type = ObjectIdentifier
_AmperionSysObjectID_Object = MibScalar
amperionSysObjectID = _AmperionSysObjectID_Object(
    (1, 3, 6, 1, 4, 1, 13995, 2, 11),
    _AmperionSysObjectID_Type()
)
amperionSysObjectID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amperionSysObjectID.setStatus("current")
_AmperionSysUpTime_Type = TimeTicks
_AmperionSysUpTime_Object = MibScalar
amperionSysUpTime = _AmperionSysUpTime_Object(
    (1, 3, 6, 1, 4, 1, 13995, 2, 12),
    _AmperionSysUpTime_Type()
)
amperionSysUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amperionSysUpTime.setStatus("current")


class _AmperionSysContact_Type(DisplayString):
    """Custom type amperionSysContact based on DisplayString"""
    defaultValue = OctetString("Amperion Inc. Andover MA")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AmperionSysContact_Type.__name__ = "DisplayString"
_AmperionSysContact_Object = MibScalar
amperionSysContact = _AmperionSysContact_Object(
    (1, 3, 6, 1, 4, 1, 13995, 2, 13),
    _AmperionSysContact_Type()
)
amperionSysContact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    amperionSysContact.setStatus("current")


class _AmperionSysName_Type(DisplayString):
    """Custom type amperionSysName based on DisplayString"""
    defaultValue = OctetString("Amperion")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AmperionSysName_Type.__name__ = "DisplayString"
_AmperionSysName_Object = MibScalar
amperionSysName = _AmperionSysName_Object(
    (1, 3, 6, 1, 4, 1, 13995, 2, 14),
    _AmperionSysName_Type()
)
amperionSysName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    amperionSysName.setStatus("current")


class _AmperionSysLocation_Type(DisplayString):
    """Custom type amperionSysLocation based on DisplayString"""
    defaultValue = OctetString("default")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AmperionSysLocation_Type.__name__ = "DisplayString"
_AmperionSysLocation_Object = MibScalar
amperionSysLocation = _AmperionSysLocation_Object(
    (1, 3, 6, 1, 4, 1, 13995, 2, 15),
    _AmperionSysLocation_Type()
)
amperionSysLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    amperionSysLocation.setStatus("current")


class _AmperionSysServices_Type(Integer32):
    """Custom type amperionSysServices based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_AmperionSysServices_Type.__name__ = "Integer32"
_AmperionSysServices_Object = MibScalar
amperionSysServices = _AmperionSysServices_Object(
    (1, 3, 6, 1, 4, 1, 13995, 2, 16),
    _AmperionSysServices_Type()
)
amperionSysServices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amperionSysServices.setStatus("current")


class _AmperionTrapMgr1_Type(IpAddress):
    """Custom type amperionTrapMgr1 based on IpAddress"""
    defaultHexValue = "7f000001"


_AmperionTrapMgr1_Object = MibScalar
amperionTrapMgr1 = _AmperionTrapMgr1_Object(
    (1, 3, 6, 1, 4, 1, 13995, 2, 18),
    _AmperionTrapMgr1_Type()
)
amperionTrapMgr1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    amperionTrapMgr1.setStatus("current")


class _AmperionTrapMgr2_Type(IpAddress):
    """Custom type amperionTrapMgr2 based on IpAddress"""
    defaultHexValue = "7f000001"


_AmperionTrapMgr2_Object = MibScalar
amperionTrapMgr2 = _AmperionTrapMgr2_Object(
    (1, 3, 6, 1, 4, 1, 13995, 2, 19),
    _AmperionTrapMgr2_Type()
)
amperionTrapMgr2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    amperionTrapMgr2.setStatus("current")


class _AmperionTrapMgr3_Type(IpAddress):
    """Custom type amperionTrapMgr3 based on IpAddress"""
    defaultHexValue = "7f000001"


_AmperionTrapMgr3_Object = MibScalar
amperionTrapMgr3 = _AmperionTrapMgr3_Object(
    (1, 3, 6, 1, 4, 1, 13995, 2, 20),
    _AmperionTrapMgr3_Type()
)
amperionTrapMgr3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    amperionTrapMgr3.setStatus("current")
_SoftwareUpgrade_ObjectIdentity = ObjectIdentity
softwareUpgrade = _SoftwareUpgrade_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13995, 3)
)


class _ServerAddress_Type(DisplayString):
    """Custom type serverAddress based on DisplayString"""
    defaultValue = OctetString("0.0.0.0")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_ServerAddress_Type.__name__ = "DisplayString"
_ServerAddress_Object = MibScalar
serverAddress = _ServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 13995, 3, 1),
    _ServerAddress_Type()
)
serverAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serverAddress.setStatus("current")


class _PrimaryPartitionContents_Type(DisplayString):
    """Custom type primaryPartitionContents based on DisplayString"""
    defaultValue = OctetString("none")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_PrimaryPartitionContents_Type.__name__ = "DisplayString"
_PrimaryPartitionContents_Object = MibScalar
primaryPartitionContents = _PrimaryPartitionContents_Object(
    (1, 3, 6, 1, 4, 1, 13995, 3, 2),
    _PrimaryPartitionContents_Type()
)
primaryPartitionContents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    primaryPartitionContents.setStatus("current")


class _CurrentState_Type(Integer32):
    """Custom type currentState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("idle", 1),
          ("inProgress", 2))
    )


_CurrentState_Type.__name__ = "Integer32"
_CurrentState_Object = MibScalar
currentState = _CurrentState_Object(
    (1, 3, 6, 1, 4, 1, 13995, 3, 3),
    _CurrentState_Type()
)
currentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentState.setStatus("current")


class _BootPartition_Type(Integer32):
    """Custom type bootPartition based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("backup", 2),
          ("primary", 1))
    )


_BootPartition_Type.__name__ = "Integer32"
_BootPartition_Object = MibScalar
bootPartition = _BootPartition_Object(
    (1, 3, 6, 1, 4, 1, 13995, 3, 4),
    _BootPartition_Type()
)
bootPartition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bootPartition.setStatus("current")


class _UpgradePartition_Type(Integer32):
    """Custom type upgradePartition based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("backup", 2),
          ("primary", 1))
    )


_UpgradePartition_Type.__name__ = "Integer32"
_UpgradePartition_Object = MibScalar
upgradePartition = _UpgradePartition_Object(
    (1, 3, 6, 1, 4, 1, 13995, 3, 5),
    _UpgradePartition_Type()
)
upgradePartition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upgradePartition.setStatus("current")


class _CurrentPartition_Type(Integer32):
    """Custom type currentPartition based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("backup", 2),
          ("primary", 1),
          ("unknown", 0))
    )


_CurrentPartition_Type.__name__ = "Integer32"
_CurrentPartition_Object = MibScalar
currentPartition = _CurrentPartition_Object(
    (1, 3, 6, 1, 4, 1, 13995, 3, 6),
    _CurrentPartition_Type()
)
currentPartition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentPartition.setStatus("current")


class _CommandOptions_Type(DisplayString):
    """Custom type commandOptions based on DisplayString"""
    defaultValue = OctetString("none")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_CommandOptions_Type.__name__ = "DisplayString"
_CommandOptions_Object = MibScalar
commandOptions = _CommandOptions_Object(
    (1, 3, 6, 1, 4, 1, 13995, 3, 7),
    _CommandOptions_Type()
)
commandOptions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commandOptions.setStatus("current")


class _BackupPartitionContents_Type(DisplayString):
    """Custom type backupPartitionContents based on DisplayString"""
    defaultValue = OctetString("none")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_BackupPartitionContents_Type.__name__ = "DisplayString"
_BackupPartitionContents_Object = MibScalar
backupPartitionContents = _BackupPartitionContents_Object(
    (1, 3, 6, 1, 4, 1, 13995, 3, 8),
    _BackupPartitionContents_Type()
)
backupPartitionContents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    backupPartitionContents.setStatus("current")


class _PrimaryCRC_Type(Integer32):
    """Custom type primaryCRC based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failed", 2),
          ("ok", 1),
          ("unknown", 0))
    )


_PrimaryCRC_Type.__name__ = "Integer32"
_PrimaryCRC_Object = MibScalar
primaryCRC = _PrimaryCRC_Object(
    (1, 3, 6, 1, 4, 1, 13995, 3, 9),
    _PrimaryCRC_Type()
)
primaryCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    primaryCRC.setStatus("current")


class _BackupCRC_Type(Integer32):
    """Custom type backupCRC based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failed", 2),
          ("ok", 1),
          ("unknown", 0))
    )


_BackupCRC_Type.__name__ = "Integer32"
_BackupCRC_Object = MibScalar
backupCRC = _BackupCRC_Object(
    (1, 3, 6, 1, 4, 1, 13995, 3, 10),
    _BackupCRC_Type()
)
backupCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    backupCRC.setStatus("current")


class _LastStatus_Type(DisplayString):
    """Custom type lastStatus based on DisplayString"""
    defaultValue = OctetString("none")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_LastStatus_Type.__name__ = "DisplayString"
_LastStatus_Object = MibScalar
lastStatus = _LastStatus_Object(
    (1, 3, 6, 1, 4, 1, 13995, 3, 11),
    _LastStatus_Type()
)
lastStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastStatus.setStatus("current")


class _Filename_Type(DisplayString):
    """Custom type filename based on DisplayString"""
    defaultValue = OctetString("ampmulti")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Filename_Type.__name__ = "DisplayString"
_Filename_Object = MibScalar
filename = _Filename_Object(
    (1, 3, 6, 1, 4, 1, 13995, 3, 12),
    _Filename_Type()
)
filename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filename.setStatus("current")


class _Server1Address_Type(DisplayString):
    """Custom type server1Address based on DisplayString"""
    defaultValue = OctetString("0.0.0.0")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Server1Address_Type.__name__ = "DisplayString"
_Server1Address_Object = MibScalar
server1Address = _Server1Address_Object(
    (1, 3, 6, 1, 4, 1, 13995, 3, 13),
    _Server1Address_Type()
)
server1Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    server1Address.setStatus("current")


class _Server2Address_Type(DisplayString):
    """Custom type server2Address based on DisplayString"""
    defaultValue = OctetString("0.0.0.0")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Server2Address_Type.__name__ = "DisplayString"
_Server2Address_Object = MibScalar
server2Address = _Server2Address_Object(
    (1, 3, 6, 1, 4, 1, 13995, 3, 14),
    _Server2Address_Type()
)
server2Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    server2Address.setStatus("current")


class _UpgradeSchedule_Type(DisplayString):
    """Custom type upgradeSchedule based on DisplayString"""
    defaultValue = OctetString("None scheduled")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_UpgradeSchedule_Type.__name__ = "DisplayString"
_UpgradeSchedule_Object = MibScalar
upgradeSchedule = _UpgradeSchedule_Object(
    (1, 3, 6, 1, 4, 1, 13995, 3, 15),
    _UpgradeSchedule_Type()
)
upgradeSchedule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upgradeSchedule.setStatus("current")


class _RebootSchedule_Type(DisplayString):
    """Custom type rebootSchedule based on DisplayString"""
    defaultValue = OctetString("None scheduled")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_RebootSchedule_Type.__name__ = "DisplayString"
_RebootSchedule_Object = MibScalar
rebootSchedule = _RebootSchedule_Object(
    (1, 3, 6, 1, 4, 1, 13995, 3, 16),
    _RebootSchedule_Type()
)
rebootSchedule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rebootSchedule.setStatus("current")


class _Login_Type(DisplayString):
    """Custom type login based on DisplayString"""
    defaultValue = OctetString("anonymous")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Login_Type.__name__ = "DisplayString"
_Login_Object = MibScalar
login = _Login_Object(
    (1, 3, 6, 1, 4, 1, 13995, 3, 17),
    _Login_Type()
)
login.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    login.setStatus("current")


class _Password_Type(DisplayString):
    """Custom type password based on DisplayString"""
    defaultValue = OctetString("root@Amperion000000.com")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Password_Type.__name__ = "DisplayString"
_Password_Object = MibScalar
password = _Password_Object(
    (1, 3, 6, 1, 4, 1, 13995, 3, 18),
    _Password_Type()
)
password.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    password.setStatus("current")
_PsGroup_ObjectIdentity = ObjectIdentity
psGroup = _PsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13995, 4)
)


class _AcLineVoltage_Type(Integer32):
    """Custom type acLineVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_AcLineVoltage_Type.__name__ = "Integer32"
_AcLineVoltage_Object = MibScalar
acLineVoltage = _AcLineVoltage_Object(
    (1, 3, 6, 1, 4, 1, 13995, 4, 1),
    _AcLineVoltage_Type()
)
acLineVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acLineVoltage.setStatus("current")


class _Plus12v_Type(DisplayString):
    """Custom type plus12v based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Plus12v_Type.__name__ = "DisplayString"
_Plus12v_Object = MibScalar
plus12v = _Plus12v_Object(
    (1, 3, 6, 1, 4, 1, 13995, 4, 2),
    _Plus12v_Type()
)
plus12v.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plus12v.setStatus("current")


class _Minus8point5v_Type(DisplayString):
    """Custom type minus8point5v based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Minus8point5v_Type.__name__ = "DisplayString"
_Minus8point5v_Object = MibScalar
minus8point5v = _Minus8point5v_Object(
    (1, 3, 6, 1, 4, 1, 13995, 4, 3),
    _Minus8point5v_Type()
)
minus8point5v.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    minus8point5v.setStatus("current")


class _Plus5v_Type(DisplayString):
    """Custom type plus5v based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Plus5v_Type.__name__ = "DisplayString"
_Plus5v_Object = MibScalar
plus5v = _Plus5v_Object(
    (1, 3, 6, 1, 4, 1, 13995, 4, 4),
    _Plus5v_Type()
)
plus5v.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plus5v.setStatus("current")


class _Plus3point3v_Type(DisplayString):
    """Custom type plus3point3v based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Plus3point3v_Type.__name__ = "DisplayString"
_Plus3point3v_Object = MibScalar
plus3point3v = _Plus3point3v_Object(
    (1, 3, 6, 1, 4, 1, 13995, 4, 5),
    _Plus3point3v_Type()
)
plus3point3v.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plus3point3v.setStatus("current")


class _BatteryCaseTemp_Type(DisplayString):
    """Custom type batteryCaseTemp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_BatteryCaseTemp_Type.__name__ = "DisplayString"
_BatteryCaseTemp_Object = MibScalar
batteryCaseTemp = _BatteryCaseTemp_Object(
    (1, 3, 6, 1, 4, 1, 13995, 4, 6),
    _BatteryCaseTemp_Type()
)
batteryCaseTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryCaseTemp.setStatus("current")


class _InternalMcuTemp_Type(DisplayString):
    """Custom type internalMcuTemp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_InternalMcuTemp_Type.__name__ = "DisplayString"
_InternalMcuTemp_Object = MibScalar
internalMcuTemp = _InternalMcuTemp_Object(
    (1, 3, 6, 1, 4, 1, 13995, 4, 7),
    _InternalMcuTemp_Type()
)
internalMcuTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    internalMcuTemp.setStatus("current")


class _BatteryCurrent_Type(DisplayString):
    """Custom type batteryCurrent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_BatteryCurrent_Type.__name__ = "DisplayString"
_BatteryCurrent_Object = MibScalar
batteryCurrent = _BatteryCurrent_Object(
    (1, 3, 6, 1, 4, 1, 13995, 4, 8),
    _BatteryCurrent_Type()
)
batteryCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryCurrent.setStatus("current")


class _BatteryVoltage_Type(DisplayString):
    """Custom type batteryVoltage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_BatteryVoltage_Type.__name__ = "DisplayString"
_BatteryVoltage_Object = MibScalar
batteryVoltage = _BatteryVoltage_Object(
    (1, 3, 6, 1, 4, 1, 13995, 4, 9),
    _BatteryVoltage_Type()
)
batteryVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryVoltage.setStatus("current")


class _McuSoftwareVersion_Type(DisplayString):
    """Custom type mcuSoftwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_McuSoftwareVersion_Type.__name__ = "DisplayString"
_McuSoftwareVersion_Object = MibScalar
mcuSoftwareVersion = _McuSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 13995, 4, 10),
    _McuSoftwareVersion_Type()
)
mcuSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcuSoftwareVersion.setStatus("current")


class _PowerCycleNpu_Type(Integer32):
    """Custom type powerCycleNpu based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("commit", 1),
          ("idle", 0))
    )


_PowerCycleNpu_Type.__name__ = "Integer32"
_PowerCycleNpu_Object = MibScalar
powerCycleNpu = _PowerCycleNpu_Object(
    (1, 3, 6, 1, 4, 1, 13995, 4, 11),
    _PowerCycleNpu_Type()
)
powerCycleNpu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    powerCycleNpu.setStatus("current")


class _PsMode_Type(Integer32):
    """Custom type psMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("dump", 1),
          ("protocol", 0))
    )


_PsMode_Type.__name__ = "Integer32"
_PsMode_Object = MibScalar
psMode = _PsMode_Object(
    (1, 3, 6, 1, 4, 1, 13995, 4, 12),
    _PsMode_Type()
)
psMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psMode.setStatus("current")


class _ShutdownNpu_Type(Integer32):
    """Custom type shutdownNpu based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("commit", 1),
          ("idle", 0))
    )


_ShutdownNpu_Type.__name__ = "Integer32"
_ShutdownNpu_Object = MibScalar
shutdownNpu = _ShutdownNpu_Object(
    (1, 3, 6, 1, 4, 1, 13995, 4, 13),
    _ShutdownNpu_Type()
)
shutdownNpu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    shutdownNpu.setStatus("current")


class _PsHardwareVersion_Type(DisplayString):
    """Custom type psHardwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_PsHardwareVersion_Type.__name__ = "DisplayString"
_PsHardwareVersion_Object = MibScalar
psHardwareVersion = _PsHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 13995, 4, 28),
    _PsHardwareVersion_Type()
)
psHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psHardwareVersion.setStatus("current")


class _PsEt_Type(DisplayString):
    """Custom type psEt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_PsEt_Type.__name__ = "DisplayString"
_PsEt_Object = MibScalar
psEt = _PsEt_Object(
    (1, 3, 6, 1, 4, 1, 13995, 4, 30),
    _PsEt_Type()
)
psEt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psEt.setStatus("current")


class _NpuEt_Type(DisplayString):
    """Custom type npuEt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_NpuEt_Type.__name__ = "DisplayString"
_NpuEt_Object = MibScalar
npuEt = _NpuEt_Object(
    (1, 3, 6, 1, 4, 1, 13995, 4, 31),
    _NpuEt_Type()
)
npuEt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npuEt.setStatus("current")
_NpuPuTimes_Type = Integer32
_NpuPuTimes_Object = MibScalar
npuPuTimes = _NpuPuTimes_Object(
    (1, 3, 6, 1, 4, 1, 13995, 4, 32),
    _NpuPuTimes_Type()
)
npuPuTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npuPuTimes.setStatus("current")


class _EventDescription_Type(DisplayString):
    """Custom type eventDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_EventDescription_Type.__name__ = "DisplayString"
_EventDescription_Object = MibScalar
eventDescription = _EventDescription_Object(
    (1, 3, 6, 1, 4, 1, 13995, 4, 33),
    _EventDescription_Type()
)
eventDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventDescription.setStatus("current")
_AmperionInterfaces_ObjectIdentity = ObjectIdentity
amperionInterfaces = _AmperionInterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13995, 5)
)
_AmperionifNumber_Type = Integer32
_AmperionifNumber_Object = MibScalar
amperionifNumber = _AmperionifNumber_Object(
    (1, 3, 6, 1, 4, 1, 13995, 5, 1),
    _AmperionifNumber_Type()
)
amperionifNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amperionifNumber.setStatus("current")
_AmperionifTable_Object = MibTable
amperionifTable = _AmperionifTable_Object(
    (1, 3, 6, 1, 4, 1, 13995, 5, 2)
)
if mibBuilder.loadTexts:
    amperionifTable.setStatus("current")
_AmperionifEntry_Object = MibTableRow
amperionifEntry = _AmperionifEntry_Object(
    (1, 3, 6, 1, 4, 1, 13995, 5, 2, 1)
)
amperionifEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    amperionifEntry.setStatus("current")


class _AmperionWirelessActivate_Type(TruthValue):
    """Custom type amperionWirelessActivate based on TruthValue"""


_AmperionWirelessActivate_Object = MibTableColumn
amperionWirelessActivate = _AmperionWirelessActivate_Object(
    (1, 3, 6, 1, 4, 1, 13995, 5, 2, 1, 1),
    _AmperionWirelessActivate_Type()
)
amperionWirelessActivate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    amperionWirelessActivate.setStatus("current")


class _AmperionifDescr_Type(DisplayString):
    """Custom type amperionifDescr based on DisplayString"""
    defaultValue = OctetString("none")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AmperionifDescr_Type.__name__ = "DisplayString"
_AmperionifDescr_Object = MibTableColumn
amperionifDescr = _AmperionifDescr_Object(
    (1, 3, 6, 1, 4, 1, 13995, 5, 2, 1, 2),
    _AmperionifDescr_Type()
)
amperionifDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amperionifDescr.setStatus("current")


class _AmperionifType_Type(Integer32):
    """Custom type amperionifType based on Integer32"""
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
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35)
        )
    )
    namedValues = NamedValues(
        *(("basicISDN", 20),
          ("ddnx25", 4),
          ("ds1", 18),
          ("ds3", 30),
          ("e1", 19),
          ("eon", 25),
          ("ethernet3Mbit", 26),
          ("ethernetcsmacd", 6),
          ("fddi", 15),
          ("framerelay", 32),
          ("hdh1822", 3),
          ("hyperchannel", 14),
          ("ieee80211a", 34),
          ("ieee80211b", 33),
          ("ieee80211g", 35),
          ("iso88023csmacd", 7),
          ("iso88024tokenBus", 8),
          ("iso88025tokenRing", 9),
          ("iso88026man", 10),
          ("lapb", 16),
          ("nsip", 27),
          ("other", 1),
          ("ppp", 23),
          ("primaryISDN", 21),
          ("propPointToPointSerial", 22),
          ("proteon10Mbit", 12),
          ("proteon80Mbit", 13),
          ("regular1822", 2),
          ("rfc877x25", 5),
          ("sdlc", 17),
          ("sip", 31),
          ("slip", 28),
          ("softwareLoopback", 24),
          ("starLan", 11),
          ("ultra", 29))
    )


_AmperionifType_Type.__name__ = "Integer32"
_AmperionifType_Object = MibTableColumn
amperionifType = _AmperionifType_Object(
    (1, 3, 6, 1, 4, 1, 13995, 5, 2, 1, 3),
    _AmperionifType_Type()
)
amperionifType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amperionifType.setStatus("current")
_AmperionifMtu_Type = Integer32
_AmperionifMtu_Object = MibTableColumn
amperionifMtu = _AmperionifMtu_Object(
    (1, 3, 6, 1, 4, 1, 13995, 5, 2, 1, 4),
    _AmperionifMtu_Type()
)
amperionifMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amperionifMtu.setStatus("current")
_AmperionifSpeed_Type = Gauge32
_AmperionifSpeed_Object = MibTableColumn
amperionifSpeed = _AmperionifSpeed_Object(
    (1, 3, 6, 1, 4, 1, 13995, 5, 2, 1, 5),
    _AmperionifSpeed_Type()
)
amperionifSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amperionifSpeed.setStatus("current")


class _AmperionifPhysAddress_Type(DisplayString):
    """Custom type amperionifPhysAddress based on DisplayString"""
    defaultValue = OctetString("none")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AmperionifPhysAddress_Type.__name__ = "DisplayString"
_AmperionifPhysAddress_Object = MibTableColumn
amperionifPhysAddress = _AmperionifPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 13995, 5, 2, 1, 6),
    _AmperionifPhysAddress_Type()
)
amperionifPhysAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amperionifPhysAddress.setStatus("current")


class _AmperionifAdminStatus_Type(Integer32):
    """Custom type amperionifAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_AmperionifAdminStatus_Type.__name__ = "Integer32"
_AmperionifAdminStatus_Object = MibTableColumn
amperionifAdminStatus = _AmperionifAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 13995, 5, 2, 1, 7),
    _AmperionifAdminStatus_Type()
)
amperionifAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    amperionifAdminStatus.setStatus("current")


class _AmperionifOperStatus_Type(Integer32):
    """Custom type amperionifOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_AmperionifOperStatus_Type.__name__ = "Integer32"
_AmperionifOperStatus_Object = MibTableColumn
amperionifOperStatus = _AmperionifOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 13995, 5, 2, 1, 8),
    _AmperionifOperStatus_Type()
)
amperionifOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amperionifOperStatus.setStatus("current")
_AmperionifLastChange_Type = TimeTicks
_AmperionifLastChange_Object = MibTableColumn
amperionifLastChange = _AmperionifLastChange_Object(
    (1, 3, 6, 1, 4, 1, 13995, 5, 2, 1, 9),
    _AmperionifLastChange_Type()
)
amperionifLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amperionifLastChange.setStatus("current")
_AmperionifInOctets_Type = Counter32
_AmperionifInOctets_Object = MibTableColumn
amperionifInOctets = _AmperionifInOctets_Object(
    (1, 3, 6, 1, 4, 1, 13995, 5, 2, 1, 10),
    _AmperionifInOctets_Type()
)
amperionifInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amperionifInOctets.setStatus("current")
_AmperionifInUcastPkts_Type = Counter32
_AmperionifInUcastPkts_Object = MibTableColumn
amperionifInUcastPkts = _AmperionifInUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 13995, 5, 2, 1, 11),
    _AmperionifInUcastPkts_Type()
)
amperionifInUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amperionifInUcastPkts.setStatus("current")
_AmperionifInNUcastPkts_Type = Counter32
_AmperionifInNUcastPkts_Object = MibTableColumn
amperionifInNUcastPkts = _AmperionifInNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 13995, 5, 2, 1, 12),
    _AmperionifInNUcastPkts_Type()
)
amperionifInNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amperionifInNUcastPkts.setStatus("current")
_AmperionifInDiscards_Type = Counter32
_AmperionifInDiscards_Object = MibTableColumn
amperionifInDiscards = _AmperionifInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 13995, 5, 2, 1, 13),
    _AmperionifInDiscards_Type()
)
amperionifInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amperionifInDiscards.setStatus("current")
_AmperionifInErrors_Type = Counter32
_AmperionifInErrors_Object = MibTableColumn
amperionifInErrors = _AmperionifInErrors_Object(
    (1, 3, 6, 1, 4, 1, 13995, 5, 2, 1, 14),
    _AmperionifInErrors_Type()
)
amperionifInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amperionifInErrors.setStatus("current")
_AmperionifInUnknownProtos_Type = Counter32
_AmperionifInUnknownProtos_Object = MibTableColumn
amperionifInUnknownProtos = _AmperionifInUnknownProtos_Object(
    (1, 3, 6, 1, 4, 1, 13995, 5, 2, 1, 15),
    _AmperionifInUnknownProtos_Type()
)
amperionifInUnknownProtos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amperionifInUnknownProtos.setStatus("current")
_AmperionifOutOctets_Type = Counter32
_AmperionifOutOctets_Object = MibTableColumn
amperionifOutOctets = _AmperionifOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 13995, 5, 2, 1, 16),
    _AmperionifOutOctets_Type()
)
amperionifOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amperionifOutOctets.setStatus("current")
_AmperionifOutUcastPkts_Type = Counter32
_AmperionifOutUcastPkts_Object = MibTableColumn
amperionifOutUcastPkts = _AmperionifOutUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 13995, 5, 2, 1, 17),
    _AmperionifOutUcastPkts_Type()
)
amperionifOutUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amperionifOutUcastPkts.setStatus("current")
_AmperionifOutNUcastPkts_Type = Counter32
_AmperionifOutNUcastPkts_Object = MibTableColumn
amperionifOutNUcastPkts = _AmperionifOutNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 13995, 5, 2, 1, 18),
    _AmperionifOutNUcastPkts_Type()
)
amperionifOutNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amperionifOutNUcastPkts.setStatus("current")
_AmperionifOutDiscards_Type = Counter32
_AmperionifOutDiscards_Object = MibTableColumn
amperionifOutDiscards = _AmperionifOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 13995, 5, 2, 1, 19),
    _AmperionifOutDiscards_Type()
)
amperionifOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amperionifOutDiscards.setStatus("current")
_AmperionifOutErrors_Type = Counter32
_AmperionifOutErrors_Object = MibTableColumn
amperionifOutErrors = _AmperionifOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 13995, 5, 2, 1, 20),
    _AmperionifOutErrors_Type()
)
amperionifOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amperionifOutErrors.setStatus("current")
_AmperionifOutQLen_Type = Gauge32
_AmperionifOutQLen_Object = MibTableColumn
amperionifOutQLen = _AmperionifOutQLen_Object(
    (1, 3, 6, 1, 4, 1, 13995, 5, 2, 1, 21),
    _AmperionifOutQLen_Type()
)
amperionifOutQLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amperionifOutQLen.setStatus("current")
_AmperionifSpecific_Type = ObjectIdentifier
_AmperionifSpecific_Object = MibTableColumn
amperionifSpecific = _AmperionifSpecific_Object(
    (1, 3, 6, 1, 4, 1, 13995, 5, 2, 1, 22),
    _AmperionifSpecific_Type()
)
amperionifSpecific.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amperionifSpecific.setStatus("current")


class _AmperionWirelessConfigEssid_Type(DisplayString):
    """Custom type amperionWirelessConfigEssid based on DisplayString"""
    defaultValue = OctetString("none")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 33),
    )


_AmperionWirelessConfigEssid_Type.__name__ = "DisplayString"
_AmperionWirelessConfigEssid_Object = MibTableColumn
amperionWirelessConfigEssid = _AmperionWirelessConfigEssid_Object(
    (1, 3, 6, 1, 4, 1, 13995, 5, 2, 1, 23),
    _AmperionWirelessConfigEssid_Type()
)
amperionWirelessConfigEssid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    amperionWirelessConfigEssid.setStatus("current")


class _AmperionWirelessConfigMode_Type(Integer32):
    """Custom type amperionWirelessConfigMode based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("adhoc", 1),
          ("managed", 2),
          ("master", 3),
          ("none", 0),
          ("repeater", 4))
    )


_AmperionWirelessConfigMode_Type.__name__ = "Integer32"
_AmperionWirelessConfigMode_Object = MibTableColumn
amperionWirelessConfigMode = _AmperionWirelessConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 13995, 5, 2, 1, 24),
    _AmperionWirelessConfigMode_Type()
)
amperionWirelessConfigMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    amperionWirelessConfigMode.setStatus("current")
_AmperionWirelessConfigChanFreq_Type = Unsigned32
_AmperionWirelessConfigChanFreq_Object = MibTableColumn
amperionWirelessConfigChanFreq = _AmperionWirelessConfigChanFreq_Object(
    (1, 3, 6, 1, 4, 1, 13995, 5, 2, 1, 25),
    _AmperionWirelessConfigChanFreq_Type()
)
amperionWirelessConfigChanFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    amperionWirelessConfigChanFreq.setStatus("current")


class _AmperionWirelessConfigKey_Type(DisplayString):
    """Custom type amperionWirelessConfigKey based on DisplayString"""
    defaultValue = OctetString("none")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 33),
    )


_AmperionWirelessConfigKey_Type.__name__ = "DisplayString"
_AmperionWirelessConfigKey_Object = MibTableColumn
amperionWirelessConfigKey = _AmperionWirelessConfigKey_Object(
    (1, 3, 6, 1, 4, 1, 13995, 5, 2, 1, 26),
    _AmperionWirelessConfigKey_Type()
)
amperionWirelessConfigKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    amperionWirelessConfigKey.setStatus("current")


class _AmperionWirelessLinkQuality_Type(Unsigned32):
    """Custom type amperionWirelessLinkQuality based on Unsigned32"""
    defaultValue = 0


_AmperionWirelessLinkQuality_Object = MibTableColumn
amperionWirelessLinkQuality = _AmperionWirelessLinkQuality_Object(
    (1, 3, 6, 1, 4, 1, 13995, 5, 2, 1, 27),
    _AmperionWirelessLinkQuality_Type()
)
amperionWirelessLinkQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amperionWirelessLinkQuality.setStatus("current")


class _AmperionWirelessSignalLevel_Type(Unsigned32):
    """Custom type amperionWirelessSignalLevel based on Unsigned32"""
    defaultValue = 0


_AmperionWirelessSignalLevel_Object = MibTableColumn
amperionWirelessSignalLevel = _AmperionWirelessSignalLevel_Object(
    (1, 3, 6, 1, 4, 1, 13995, 5, 2, 1, 28),
    _AmperionWirelessSignalLevel_Type()
)
amperionWirelessSignalLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amperionWirelessSignalLevel.setStatus("current")


class _AmperionWirelessNoiseLevel_Type(Unsigned32):
    """Custom type amperionWirelessNoiseLevel based on Unsigned32"""
    defaultValue = 0


_AmperionWirelessNoiseLevel_Object = MibTableColumn
amperionWirelessNoiseLevel = _AmperionWirelessNoiseLevel_Object(
    (1, 3, 6, 1, 4, 1, 13995, 5, 2, 1, 29),
    _AmperionWirelessNoiseLevel_Type()
)
amperionWirelessNoiseLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amperionWirelessNoiseLevel.setStatus("current")


class _AmperionWirelessConfigWifType_Type(Integer32):
    """Custom type amperionWirelessConfigWifType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("wtype11a", 1),
          ("wtype11b", 2),
          ("wtype11g", 3))
    )


_AmperionWirelessConfigWifType_Type.__name__ = "Integer32"
_AmperionWirelessConfigWifType_Object = MibTableColumn
amperionWirelessConfigWifType = _AmperionWirelessConfigWifType_Object(
    (1, 3, 6, 1, 4, 1, 13995, 5, 2, 1, 30),
    _AmperionWirelessConfigWifType_Type()
)
amperionWirelessConfigWifType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    amperionWirelessConfigWifType.setStatus("current")


class _AmperionWirelessConfigBitRate_Type(Integer32):
    """Custom type amperionWirelessConfigBitRate based on Integer32"""
    defaultValue = 0


_AmperionWirelessConfigBitRate_Object = MibTableColumn
amperionWirelessConfigBitRate = _AmperionWirelessConfigBitRate_Object(
    (1, 3, 6, 1, 4, 1, 13995, 5, 2, 1, 31),
    _AmperionWirelessConfigBitRate_Type()
)
amperionWirelessConfigBitRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    amperionWirelessConfigBitRate.setStatus("current")


class _AmperionWirelessConfigWDSPeer_Type(DisplayString):
    """Custom type amperionWirelessConfigWDSPeer based on DisplayString"""
    defaultValue = OctetString("0")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_AmperionWirelessConfigWDSPeer_Type.__name__ = "DisplayString"
_AmperionWirelessConfigWDSPeer_Object = MibTableColumn
amperionWirelessConfigWDSPeer = _AmperionWirelessConfigWDSPeer_Object(
    (1, 3, 6, 1, 4, 1, 13995, 5, 2, 1, 32),
    _AmperionWirelessConfigWDSPeer_Type()
)
amperionWirelessConfigWDSPeer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    amperionWirelessConfigWDSPeer.setStatus("current")
_AmperionWireless_ObjectIdentity = ObjectIdentity
amperionWireless = _AmperionWireless_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13995, 6)
)


class _AccessControlStatus_Type(Integer32):
    """Custom type accessControlStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_AccessControlStatus_Type.__name__ = "Integer32"
_AccessControlStatus_Object = MibScalar
accessControlStatus = _AccessControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 13995, 6, 1),
    _AccessControlStatus_Type()
)
accessControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accessControlStatus.setStatus("current")
_AmpMacAcceptTable_Object = MibTable
ampMacAcceptTable = _AmpMacAcceptTable_Object(
    (1, 3, 6, 1, 4, 1, 13995, 6, 3)
)
if mibBuilder.loadTexts:
    ampMacAcceptTable.setStatus("current")
_AmpMacAcceptEntry_Object = MibTableRow
ampMacAcceptEntry = _AmpMacAcceptEntry_Object(
    (1, 3, 6, 1, 4, 1, 13995, 6, 3, 1)
)
ampMacAcceptEntry.setIndexNames(
    (0, "Amperion-MIB", "macAcceptTableIndex"),
)
if mibBuilder.loadTexts:
    ampMacAcceptEntry.setStatus("current")


class _MacAcceptTableMacAddress_Type(DisplayString):
    """Custom type macAcceptTableMacAddress based on DisplayString"""
    defaultValue = OctetString("00:00:00:00:00:00")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_MacAcceptTableMacAddress_Type.__name__ = "DisplayString"
_MacAcceptTableMacAddress_Object = MibTableColumn
macAcceptTableMacAddress = _MacAcceptTableMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 13995, 6, 3, 1, 1),
    _MacAcceptTableMacAddress_Type()
)
macAcceptTableMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    macAcceptTableMacAddress.setStatus("current")


class _MacAcceptTableRowStatus_Type(RowStatus):
    """Custom type macAcceptTableRowStatus based on RowStatus"""


_MacAcceptTableRowStatus_Object = MibTableColumn
macAcceptTableRowStatus = _MacAcceptTableRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 13995, 6, 3, 1, 2),
    _MacAcceptTableRowStatus_Type()
)
macAcceptTableRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    macAcceptTableRowStatus.setStatus("current")


class _MacAcceptTableIndex_Type(Unsigned32):
    """Custom type macAcceptTableIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65536),
    )


_MacAcceptTableIndex_Type.__name__ = "Unsigned32"
_MacAcceptTableIndex_Object = MibTableColumn
macAcceptTableIndex = _MacAcceptTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 13995, 6, 3, 1, 3),
    _MacAcceptTableIndex_Type()
)
macAcceptTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    macAcceptTableIndex.setStatus("current")


class _MacAcceptTableWirelessIf_Type(Unsigned32):
    """Custom type macAcceptTableWirelessIf based on Unsigned32"""
    defaultValue = 0


_MacAcceptTableWirelessIf_Object = MibTableColumn
macAcceptTableWirelessIf = _MacAcceptTableWirelessIf_Object(
    (1, 3, 6, 1, 4, 1, 13995, 6, 3, 1, 4),
    _MacAcceptTableWirelessIf_Type()
)
macAcceptTableWirelessIf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    macAcceptTableWirelessIf.setStatus("current")
_AmperionipAddrTable_Object = MibTable
amperionipAddrTable = _AmperionipAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 13995, 7)
)
if mibBuilder.loadTexts:
    amperionipAddrTable.setStatus("current")
_AmperionipAddrEntry_Object = MibTableRow
amperionipAddrEntry = _AmperionipAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 13995, 7, 1)
)
amperionipAddrEntry.setIndexNames(
    (0, "Amperion-MIB", "amperionipAdEntAddr"),
)
if mibBuilder.loadTexts:
    amperionipAddrEntry.setStatus("current")
_AmperionipAdEntAddr_Type = IpAddress
_AmperionipAdEntAddr_Object = MibTableColumn
amperionipAdEntAddr = _AmperionipAdEntAddr_Object(
    (1, 3, 6, 1, 4, 1, 13995, 7, 1, 1),
    _AmperionipAdEntAddr_Type()
)
amperionipAdEntAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    amperionipAdEntAddr.setStatus("current")


class _AmperionipAdEntIfName_Type(DisplayString):
    """Custom type amperionipAdEntIfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_AmperionipAdEntIfName_Type.__name__ = "DisplayString"
_AmperionipAdEntIfName_Object = MibTableColumn
amperionipAdEntIfName = _AmperionipAdEntIfName_Object(
    (1, 3, 6, 1, 4, 1, 13995, 7, 1, 2),
    _AmperionipAdEntIfName_Type()
)
amperionipAdEntIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amperionipAdEntIfName.setStatus("current")
_AmperionipAdEntNetMask_Type = IpAddress
_AmperionipAdEntNetMask_Object = MibTableColumn
amperionipAdEntNetMask = _AmperionipAdEntNetMask_Object(
    (1, 3, 6, 1, 4, 1, 13995, 7, 1, 3),
    _AmperionipAdEntNetMask_Type()
)
amperionipAdEntNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amperionipAdEntNetMask.setStatus("current")
_AmperionipAdEntBcastAddr_Type = Integer32
_AmperionipAdEntBcastAddr_Object = MibTableColumn
amperionipAdEntBcastAddr = _AmperionipAdEntBcastAddr_Object(
    (1, 3, 6, 1, 4, 1, 13995, 7, 1, 4),
    _AmperionipAdEntBcastAddr_Type()
)
amperionipAdEntBcastAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amperionipAdEntBcastAddr.setStatus("current")


class _AmperionipAdEntReasmMaxSize_Type(Integer32):
    """Custom type amperionipAdEntReasmMaxSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AmperionipAdEntReasmMaxSize_Type.__name__ = "Integer32"
_AmperionipAdEntReasmMaxSize_Object = MibTableColumn
amperionipAdEntReasmMaxSize = _AmperionipAdEntReasmMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 13995, 7, 1, 5),
    _AmperionipAdEntReasmMaxSize_Type()
)
amperionipAdEntReasmMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amperionipAdEntReasmMaxSize.setStatus("current")
_AmperionipAdRowStatus_Type = RowStatus
_AmperionipAdRowStatus_Object = MibTableColumn
amperionipAdRowStatus = _AmperionipAdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 13995, 7, 1, 6),
    _AmperionipAdRowStatus_Type()
)
amperionipAdRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    amperionipAdRowStatus.setStatus("current")


class _AmperionipAdEntActivate_Type(TruthValue):
    """Custom type amperionipAdEntActivate based on TruthValue"""


_AmperionipAdEntActivate_Object = MibTableColumn
amperionipAdEntActivate = _AmperionipAdEntActivate_Object(
    (1, 3, 6, 1, 4, 1, 13995, 7, 1, 7),
    _AmperionipAdEntActivate_Type()
)
amperionipAdEntActivate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    amperionipAdEntActivate.setStatus("current")
_QualityOfService_ObjectIdentity = ObjectIdentity
qualityOfService = _QualityOfService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13995, 8)
)


class _ServiceClassA_Type(Unsigned32):
    """Custom type serviceClassA based on Unsigned32"""
    defaultValue = 1024

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 65536),
    )


_ServiceClassA_Type.__name__ = "Unsigned32"
_ServiceClassA_Object = MibScalar
serviceClassA = _ServiceClassA_Object(
    (1, 3, 6, 1, 4, 1, 13995, 8, 1),
    _ServiceClassA_Type()
)
serviceClassA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serviceClassA.setStatus("current")


class _ServiceClassB_Type(Unsigned32):
    """Custom type serviceClassB based on Unsigned32"""
    defaultValue = 512

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 65536),
    )


_ServiceClassB_Type.__name__ = "Unsigned32"
_ServiceClassB_Object = MibScalar
serviceClassB = _ServiceClassB_Object(
    (1, 3, 6, 1, 4, 1, 13995, 8, 2),
    _ServiceClassB_Type()
)
serviceClassB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serviceClassB.setStatus("current")


class _ServiceClassC_Type(Unsigned32):
    """Custom type serviceClassC based on Unsigned32"""
    defaultValue = 256

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 65536),
    )


_ServiceClassC_Type.__name__ = "Unsigned32"
_ServiceClassC_Object = MibScalar
serviceClassC = _ServiceClassC_Object(
    (1, 3, 6, 1, 4, 1, 13995, 8, 3),
    _ServiceClassC_Type()
)
serviceClassC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serviceClassC.setStatus("current")


class _ServiceClassD_Type(Unsigned32):
    """Custom type serviceClassD based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 65536),
    )


_ServiceClassD_Type.__name__ = "Unsigned32"
_ServiceClassD_Object = MibScalar
serviceClassD = _ServiceClassD_Object(
    (1, 3, 6, 1, 4, 1, 13995, 8, 4),
    _ServiceClassD_Type()
)
serviceClassD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serviceClassD.setStatus("current")
_SubscriberTable_Object = MibTable
subscriberTable = _SubscriberTable_Object(
    (1, 3, 6, 1, 4, 1, 13995, 8, 5)
)
if mibBuilder.loadTexts:
    subscriberTable.setStatus("current")
_SubscriberEntry_Object = MibTableRow
subscriberEntry = _SubscriberEntry_Object(
    (1, 3, 6, 1, 4, 1, 13995, 8, 5, 1)
)
subscriberEntry.setIndexNames(
    (0, "Amperion-MIB", "index"),
)
if mibBuilder.loadTexts:
    subscriberEntry.setStatus("current")


class _Index_Type(Unsigned32):
    """Custom type index based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65536),
    )


_Index_Type.__name__ = "Unsigned32"
_Index_Object = MibTableColumn
index = _Index_Object(
    (1, 3, 6, 1, 4, 1, 13995, 8, 5, 1, 1),
    _Index_Type()
)
index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    index.setStatus("current")


class _Name_Type(DisplayString):
    """Custom type name based on DisplayString"""
    defaultValue = OctetString("none")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Name_Type.__name__ = "DisplayString"
_Name_Object = MibTableColumn
name = _Name_Object(
    (1, 3, 6, 1, 4, 1, 13995, 8, 5, 1, 2),
    _Name_Type()
)
name.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    name.setStatus("current")


class _IpAddress_Type(IpAddress):
    """Custom type ipAddress based on IpAddress"""
    defaultHexValue = "0"


_IpAddress_Object = MibTableColumn
ipAddress = _IpAddress_Object(
    (1, 3, 6, 1, 4, 1, 13995, 8, 5, 1, 3),
    _IpAddress_Type()
)
ipAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipAddress.setStatus("current")


class _MacAddress_Type(DisplayString):
    """Custom type macAddress based on DisplayString"""
    defaultValue = OctetString("00:00:00:00:00:00")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_MacAddress_Type.__name__ = "DisplayString"
_MacAddress_Object = MibTableColumn
macAddress = _MacAddress_Object(
    (1, 3, 6, 1, 4, 1, 13995, 8, 5, 1, 4),
    _MacAddress_Type()
)
macAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    macAddress.setStatus("current")


class _ServiceClass_Type(Integer32):
    """Custom type serviceClass based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("classA", 1),
          ("classB", 2),
          ("classC", 3),
          ("classD", 4),
          ("none", 0))
    )


_ServiceClass_Type.__name__ = "Integer32"
_ServiceClass_Object = MibTableColumn
serviceClass = _ServiceClass_Object(
    (1, 3, 6, 1, 4, 1, 13995, 8, 5, 1, 5),
    _ServiceClass_Type()
)
serviceClass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    serviceClass.setStatus("current")


class _RowStatus_Type(RowStatus):
    """Custom type rowStatus based on RowStatus"""


_RowStatus_Object = MibTableColumn
rowStatus = _RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 13995, 8, 5, 1, 6),
    _RowStatus_Type()
)
rowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rowStatus.setStatus("current")


class _UpstreamDownstreamRatio_Type(DisplayString):
    """Custom type upstreamDownstreamRatio based on DisplayString"""
    defaultValue = OctetString("1:3")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_UpstreamDownstreamRatio_Type.__name__ = "DisplayString"
_UpstreamDownstreamRatio_Object = MibScalar
upstreamDownstreamRatio = _UpstreamDownstreamRatio_Object(
    (1, 3, 6, 1, 4, 1, 13995, 8, 6),
    _UpstreamDownstreamRatio_Type()
)
upstreamDownstreamRatio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upstreamDownstreamRatio.setStatus("current")


class _QosStatus_Type(Integer32):
    """Custom type qosStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_QosStatus_Type.__name__ = "Integer32"
_QosStatus_Object = MibScalar
qosStatus = _QosStatus_Object(
    (1, 3, 6, 1, 4, 1, 13995, 8, 7),
    _QosStatus_Type()
)
qosStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosStatus.setStatus("current")
_Afe_ObjectIdentity = ObjectIdentity
afe = _Afe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13995, 9)
)
_AfeExtractor_ObjectIdentity = ObjectIdentity
afeExtractor = _AfeExtractor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13995, 9, 1)
)
_AfeExtTxGain_Type = Integer32
_AfeExtTxGain_Object = MibScalar
afeExtTxGain = _AfeExtTxGain_Object(
    (1, 3, 6, 1, 4, 1, 13995, 9, 1, 1),
    _AfeExtTxGain_Type()
)
afeExtTxGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    afeExtTxGain.setStatus("current")
_AfeExtRxGain_Type = Integer32
_AfeExtRxGain_Object = MibScalar
afeExtRxGain = _AfeExtRxGain_Object(
    (1, 3, 6, 1, 4, 1, 13995, 9, 1, 2),
    _AfeExtRxGain_Type()
)
afeExtRxGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    afeExtRxGain.setStatus("current")


class _AfeExtDownstream_Type(DisplayString):
    """Custom type afeExtDownstream based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 4),
    )


_AfeExtDownstream_Type.__name__ = "DisplayString"
_AfeExtDownstream_Object = MibScalar
afeExtDownstream = _AfeExtDownstream_Object(
    (1, 3, 6, 1, 4, 1, 13995, 9, 1, 3),
    _AfeExtDownstream_Type()
)
afeExtDownstream.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    afeExtDownstream.setStatus("current")


class _AfeExtUpstream_Type(DisplayString):
    """Custom type afeExtUpstream based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 4),
    )


_AfeExtUpstream_Type.__name__ = "DisplayString"
_AfeExtUpstream_Object = MibScalar
afeExtUpstream = _AfeExtUpstream_Object(
    (1, 3, 6, 1, 4, 1, 13995, 9, 1, 4),
    _AfeExtUpstream_Type()
)
afeExtUpstream.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    afeExtUpstream.setStatus("current")


class _AfeExtActivate_Type(TruthValue):
    """Custom type afeExtActivate based on TruthValue"""


_AfeExtActivate_Object = MibScalar
afeExtActivate = _AfeExtActivate_Object(
    (1, 3, 6, 1, 4, 1, 13995, 9, 1, 5),
    _AfeExtActivate_Type()
)
afeExtActivate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    afeExtActivate.setStatus("current")
_AfeInjector_ObjectIdentity = ObjectIdentity
afeInjector = _AfeInjector_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13995, 9, 2)
)
_AfeInjTxGain_Type = Integer32
_AfeInjTxGain_Object = MibScalar
afeInjTxGain = _AfeInjTxGain_Object(
    (1, 3, 6, 1, 4, 1, 13995, 9, 2, 1),
    _AfeInjTxGain_Type()
)
afeInjTxGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    afeInjTxGain.setStatus("current")
_AfeInjRxGain_Type = Integer32
_AfeInjRxGain_Object = MibScalar
afeInjRxGain = _AfeInjRxGain_Object(
    (1, 3, 6, 1, 4, 1, 13995, 9, 2, 2),
    _AfeInjRxGain_Type()
)
afeInjRxGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    afeInjRxGain.setStatus("current")


class _AfeInjDownstream_Type(DisplayString):
    """Custom type afeInjDownstream based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 4),
    )


_AfeInjDownstream_Type.__name__ = "DisplayString"
_AfeInjDownstream_Object = MibScalar
afeInjDownstream = _AfeInjDownstream_Object(
    (1, 3, 6, 1, 4, 1, 13995, 9, 2, 3),
    _AfeInjDownstream_Type()
)
afeInjDownstream.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    afeInjDownstream.setStatus("current")


class _AfeInjUpstream_Type(DisplayString):
    """Custom type afeInjUpstream based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 4),
    )


_AfeInjUpstream_Type.__name__ = "DisplayString"
_AfeInjUpstream_Object = MibScalar
afeInjUpstream = _AfeInjUpstream_Object(
    (1, 3, 6, 1, 4, 1, 13995, 9, 2, 4),
    _AfeInjUpstream_Type()
)
afeInjUpstream.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    afeInjUpstream.setStatus("current")


class _AfeInjActivate_Type(TruthValue):
    """Custom type afeInjActivate based on TruthValue"""


_AfeInjActivate_Object = MibScalar
afeInjActivate = _AfeInjActivate_Object(
    (1, 3, 6, 1, 4, 1, 13995, 9, 2, 5),
    _AfeInjActivate_Type()
)
afeInjActivate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    afeInjActivate.setStatus("current")
_AmperionRoutes_ObjectIdentity = ObjectIdentity
amperionRoutes = _AmperionRoutes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13995, 10)
)
_AmperionRouteTable_Object = MibTable
amperionRouteTable = _AmperionRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 13995, 10, 1)
)
if mibBuilder.loadTexts:
    amperionRouteTable.setStatus("current")
_AmperionRouteEntry_Object = MibTableRow
amperionRouteEntry = _AmperionRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 13995, 10, 1, 1)
)
amperionRouteEntry.setIndexNames(
    (0, "Amperion-MIB", "ipRouteDest"),
)
if mibBuilder.loadTexts:
    amperionRouteEntry.setStatus("current")
_IpRouteDest_Type = IpAddress
_IpRouteDest_Object = MibTableColumn
ipRouteDest = _IpRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 13995, 10, 1, 1, 1),
    _IpRouteDest_Type()
)
ipRouteDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRouteDest.setStatus("current")
_IpRouteIfIndex_Type = Integer32
_IpRouteIfIndex_Object = MibTableColumn
ipRouteIfIndex = _IpRouteIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 13995, 10, 1, 1, 2),
    _IpRouteIfIndex_Type()
)
ipRouteIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipRouteIfIndex.setStatus("current")
_IpRouteMetric1_Type = Integer32
_IpRouteMetric1_Object = MibTableColumn
ipRouteMetric1 = _IpRouteMetric1_Object(
    (1, 3, 6, 1, 4, 1, 13995, 10, 1, 1, 3),
    _IpRouteMetric1_Type()
)
ipRouteMetric1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipRouteMetric1.setStatus("current")
_IpRouteMetric2_Type = Integer32
_IpRouteMetric2_Object = MibTableColumn
ipRouteMetric2 = _IpRouteMetric2_Object(
    (1, 3, 6, 1, 4, 1, 13995, 10, 1, 1, 4),
    _IpRouteMetric2_Type()
)
ipRouteMetric2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipRouteMetric2.setStatus("current")
_IpRouteMetric3_Type = Integer32
_IpRouteMetric3_Object = MibTableColumn
ipRouteMetric3 = _IpRouteMetric3_Object(
    (1, 3, 6, 1, 4, 1, 13995, 10, 1, 1, 5),
    _IpRouteMetric3_Type()
)
ipRouteMetric3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipRouteMetric3.setStatus("current")
_IpRouteMetric4_Type = Integer32
_IpRouteMetric4_Object = MibTableColumn
ipRouteMetric4 = _IpRouteMetric4_Object(
    (1, 3, 6, 1, 4, 1, 13995, 10, 1, 1, 6),
    _IpRouteMetric4_Type()
)
ipRouteMetric4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipRouteMetric4.setStatus("current")
_IpRouteNextHop_Type = IpAddress
_IpRouteNextHop_Object = MibTableColumn
ipRouteNextHop = _IpRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 13995, 10, 1, 1, 7),
    _IpRouteNextHop_Type()
)
ipRouteNextHop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipRouteNextHop.setStatus("current")


class _IpRouteType_Type(Integer32):
    """Custom type ipRouteType based on Integer32"""
    defaultValue = 3

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
        *(("direct", 3),
          ("indirect", 4),
          ("invalid", 2),
          ("other", 1))
    )


_IpRouteType_Type.__name__ = "Integer32"
_IpRouteType_Object = MibTableColumn
ipRouteType = _IpRouteType_Object(
    (1, 3, 6, 1, 4, 1, 13995, 10, 1, 1, 8),
    _IpRouteType_Type()
)
ipRouteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRouteType.setStatus("current")


class _IpRouteProto_Type(Integer32):
    """Custom type ipRouteProto based on Integer32"""
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
              9,
              10,
              11,
              12,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("bbnSpfIgp", 12),
          ("bgp", 14),
          ("ciscoIgrp", 11),
          ("egp", 5),
          ("esis", 10),
          ("ggp", 6),
          ("hello", 7),
          ("icmp", 4),
          ("isis", 9),
          ("local", 2),
          ("netmgt", 3),
          ("ospf", 13),
          ("other", 1),
          ("rip", 8))
    )


_IpRouteProto_Type.__name__ = "Integer32"
_IpRouteProto_Object = MibTableColumn
ipRouteProto = _IpRouteProto_Object(
    (1, 3, 6, 1, 4, 1, 13995, 10, 1, 1, 9),
    _IpRouteProto_Type()
)
ipRouteProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRouteProto.setStatus("current")
_IpRouteAge_Type = Integer32
_IpRouteAge_Object = MibTableColumn
ipRouteAge = _IpRouteAge_Object(
    (1, 3, 6, 1, 4, 1, 13995, 10, 1, 1, 10),
    _IpRouteAge_Type()
)
ipRouteAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipRouteAge.setStatus("current")
_IpRouteMask_Type = IpAddress
_IpRouteMask_Object = MibTableColumn
ipRouteMask = _IpRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 13995, 10, 1, 1, 11),
    _IpRouteMask_Type()
)
ipRouteMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipRouteMask.setStatus("current")
_IpRouteMetric5_Type = Integer32
_IpRouteMetric5_Object = MibTableColumn
ipRouteMetric5 = _IpRouteMetric5_Object(
    (1, 3, 6, 1, 4, 1, 13995, 10, 1, 1, 12),
    _IpRouteMetric5_Type()
)
ipRouteMetric5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipRouteMetric5.setStatus("current")
_IpRouteInfo_Type = ObjectIdentifier
_IpRouteInfo_Object = MibTableColumn
ipRouteInfo = _IpRouteInfo_Object(
    (1, 3, 6, 1, 4, 1, 13995, 10, 1, 1, 13),
    _IpRouteInfo_Type()
)
ipRouteInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRouteInfo.setStatus("current")


class _IpDefRouteActivate_Type(TruthValue):
    """Custom type ipDefRouteActivate based on TruthValue"""


_IpDefRouteActivate_Object = MibTableColumn
ipDefRouteActivate = _IpDefRouteActivate_Object(
    (1, 3, 6, 1, 4, 1, 13995, 10, 1, 1, 14),
    _IpDefRouteActivate_Type()
)
ipDefRouteActivate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipDefRouteActivate.setStatus("current")
_Plc_ObjectIdentity = ObjectIdentity
plc = _Plc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13995, 11)
)
_PlcExtractor_ObjectIdentity = ObjectIdentity
plcExtractor = _PlcExtractor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13995, 11, 1)
)


class _PlcExtTxGain_Type(Integer32):
    """Custom type plcExtTxGain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_PlcExtTxGain_Type.__name__ = "Integer32"
_PlcExtTxGain_Object = MibScalar
plcExtTxGain = _PlcExtTxGain_Object(
    (1, 3, 6, 1, 4, 1, 13995, 11, 1, 1),
    _PlcExtTxGain_Type()
)
plcExtTxGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plcExtTxGain.setStatus("current")


class _PlcExtRxGain_Type(Integer32):
    """Custom type plcExtRxGain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_PlcExtRxGain_Type.__name__ = "Integer32"
_PlcExtRxGain_Object = MibScalar
plcExtRxGain = _PlcExtRxGain_Object(
    (1, 3, 6, 1, 4, 1, 13995, 11, 1, 2),
    _PlcExtRxGain_Type()
)
plcExtRxGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plcExtRxGain.setStatus("current")
_PlcInjector_ObjectIdentity = ObjectIdentity
plcInjector = _PlcInjector_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13995, 11, 2)
)


class _PlcInjTxGain_Type(Integer32):
    """Custom type plcInjTxGain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_PlcInjTxGain_Type.__name__ = "Integer32"
_PlcInjTxGain_Object = MibScalar
plcInjTxGain = _PlcInjTxGain_Object(
    (1, 3, 6, 1, 4, 1, 13995, 11, 2, 1),
    _PlcInjTxGain_Type()
)
plcInjTxGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plcInjTxGain.setStatus("current")


class _PlcInjRxGain_Type(Integer32):
    """Custom type plcInjRxGain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_PlcInjRxGain_Type.__name__ = "Integer32"
_PlcInjRxGain_Object = MibScalar
plcInjRxGain = _PlcInjRxGain_Object(
    (1, 3, 6, 1, 4, 1, 13995, 11, 2, 2),
    _PlcInjRxGain_Type()
)
plcInjRxGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plcInjRxGain.setStatus("current")
_AfeCpldResetCount_Type = Counter32
_AfeCpldResetCount_Object = MibScalar
afeCpldResetCount = _AfeCpldResetCount_Object(
    (1, 3, 6, 1, 4, 1, 13995, 11, 5),
    _AfeCpldResetCount_Type()
)
afeCpldResetCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    afeCpldResetCount.setStatus("current")
_PlcLossCount_Type = Counter32
_PlcLossCount_Object = MibScalar
plcLossCount = _PlcLossCount_Object(
    (1, 3, 6, 1, 4, 1, 13995, 11, 6),
    _PlcLossCount_Type()
)
plcLossCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plcLossCount.setStatus("current")


class _ResetCounters_Type(Integer32):
    """Custom type resetCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("idle", 1),
          ("reset", 2))
    )


_ResetCounters_Type.__name__ = "Integer32"
_ResetCounters_Object = MibScalar
resetCounters = _ResetCounters_Object(
    (1, 3, 6, 1, 4, 1, 13995, 11, 7),
    _ResetCounters_Type()
)
resetCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    resetCounters.setStatus("current")
_OptimizationTable_Object = MibTable
optimizationTable = _OptimizationTable_Object(
    (1, 3, 6, 1, 4, 1, 13995, 11, 8)
)
if mibBuilder.loadTexts:
    optimizationTable.setStatus("current")
_OptimizationEntry_Object = MibTableRow
optimizationEntry = _OptimizationEntry_Object(
    (1, 3, 6, 1, 4, 1, 13995, 11, 8, 1)
)
optimizationEntry.setIndexNames(
    (0, "Amperion-MIB", "extrIpaddress"),
    (0, "Amperion-MIB", "extrChannelNumber"),
)
if mibBuilder.loadTexts:
    optimizationEntry.setStatus("current")
_ExtrIpaddress_Type = IpAddress
_ExtrIpaddress_Object = MibTableColumn
extrIpaddress = _ExtrIpaddress_Object(
    (1, 3, 6, 1, 4, 1, 13995, 11, 8, 1, 1),
    _ExtrIpaddress_Type()
)
extrIpaddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extrIpaddress.setStatus("current")
_ExtrChannelNumber_Type = Integer32
_ExtrChannelNumber_Object = MibTableColumn
extrChannelNumber = _ExtrChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 13995, 11, 8, 1, 2),
    _ExtrChannelNumber_Type()
)
extrChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extrChannelNumber.setStatus("current")
_UpstreamFreq_Type = DisplayString
_UpstreamFreq_Object = MibTableColumn
upstreamFreq = _UpstreamFreq_Object(
    (1, 3, 6, 1, 4, 1, 13995, 11, 8, 1, 3),
    _UpstreamFreq_Type()
)
upstreamFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upstreamFreq.setStatus("current")
_DownstreamFreq_Type = DisplayString
_DownstreamFreq_Object = MibTableColumn
downstreamFreq = _DownstreamFreq_Object(
    (1, 3, 6, 1, 4, 1, 13995, 11, 8, 1, 4),
    _DownstreamFreq_Type()
)
downstreamFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    downstreamFreq.setStatus("current")
_RxGain_Type = DisplayString
_RxGain_Object = MibTableColumn
rxGain = _RxGain_Object(
    (1, 3, 6, 1, 4, 1, 13995, 11, 8, 1, 5),
    _RxGain_Type()
)
rxGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxGain.setStatus("current")
_TxGain_Type = DisplayString
_TxGain_Object = MibTableColumn
txGain = _TxGain_Object(
    (1, 3, 6, 1, 4, 1, 13995, 11, 8, 1, 6),
    _TxGain_Type()
)
txGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txGain.setStatus("current")
_PlcThroughput_Type = DisplayString
_PlcThroughput_Object = MibTableColumn
plcThroughput = _PlcThroughput_Object(
    (1, 3, 6, 1, 4, 1, 13995, 11, 8, 1, 7),
    _PlcThroughput_Type()
)
plcThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plcThroughput.setStatus("current")


class _UpStreamDownStream_Type(Integer32):
    """Custom type upStreamDownStream based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("downstream", 2),
          ("unknown", 3),
          ("upstream", 1))
    )


_UpStreamDownStream_Type.__name__ = "Integer32"
_UpStreamDownStream_Object = MibTableColumn
upStreamDownStream = _UpStreamDownStream_Object(
    (1, 3, 6, 1, 4, 1, 13995, 11, 8, 1, 8),
    _UpStreamDownStream_Type()
)
upStreamDownStream.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upStreamDownStream.setStatus("current")


class _GpsInfo_Type(DisplayString):
    """Custom type gpsInfo based on DisplayString"""
    defaultValue = OctetString("none")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_GpsInfo_Type.__name__ = "DisplayString"
_GpsInfo_Object = MibTableColumn
gpsInfo = _GpsInfo_Object(
    (1, 3, 6, 1, 4, 1, 13995, 11, 8, 1, 9),
    _GpsInfo_Type()
)
gpsInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsInfo.setStatus("current")


class _PlcEventDescription_Type(DisplayString):
    """Custom type plcEventDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_PlcEventDescription_Type.__name__ = "DisplayString"
_PlcEventDescription_Object = MibScalar
plcEventDescription = _PlcEventDescription_Object(
    (1, 3, 6, 1, 4, 1, 13995, 11, 9),
    _PlcEventDescription_Type()
)
plcEventDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plcEventDescription.setStatus("current")
_TempGroup_ObjectIdentity = ObjectIdentity
tempGroup = _TempGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13995, 12)
)


class _TempFanState_Type(Integer32):
    """Custom type tempFanState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_TempFanState_Type.__name__ = "Integer32"
_TempFanState_Object = MibScalar
tempFanState = _TempFanState_Object(
    (1, 3, 6, 1, 4, 1, 13995, 12, 1),
    _TempFanState_Type()
)
tempFanState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempFanState.setStatus("current")


class _TempFanTargetTemp_Type(Integer32):
    """Custom type tempFanTargetTemp based on Integer32"""
    defaultValue = 25

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 70),
    )


_TempFanTargetTemp_Type.__name__ = "Integer32"
_TempFanTargetTemp_Object = MibScalar
tempFanTargetTemp = _TempFanTargetTemp_Object(
    (1, 3, 6, 1, 4, 1, 13995, 12, 2),
    _TempFanTargetTemp_Type()
)
tempFanTargetTemp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tempFanTargetTemp.setStatus("current")
if mibBuilder.loadTexts:
    tempFanTargetTemp.setUnits("degrees celcius")


class _TempHighWarnLimit_Type(Integer32):
    """Custom type tempHighWarnLimit based on Integer32"""
    defaultValue = 65

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 150),
    )


_TempHighWarnLimit_Type.__name__ = "Integer32"
_TempHighWarnLimit_Object = MibScalar
tempHighWarnLimit = _TempHighWarnLimit_Object(
    (1, 3, 6, 1, 4, 1, 13995, 12, 3),
    _TempHighWarnLimit_Type()
)
tempHighWarnLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tempHighWarnLimit.setStatus("current")
if mibBuilder.loadTexts:
    tempHighWarnLimit.setUnits("degrees Celsius")


class _TempEventDescription_Type(DisplayString):
    """Custom type tempEventDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 130),
    )


_TempEventDescription_Type.__name__ = "DisplayString"
_TempEventDescription_Object = MibScalar
tempEventDescription = _TempEventDescription_Object(
    (1, 3, 6, 1, 4, 1, 13995, 12, 5),
    _TempEventDescription_Type()
)
tempEventDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempEventDescription.setStatus("current")


class _TempHighErrorLimit_Type(Integer32):
    """Custom type tempHighErrorLimit based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 150),
    )


_TempHighErrorLimit_Type.__name__ = "Integer32"
_TempHighErrorLimit_Object = MibScalar
tempHighErrorLimit = _TempHighErrorLimit_Object(
    (1, 3, 6, 1, 4, 1, 13995, 12, 9),
    _TempHighErrorLimit_Type()
)
tempHighErrorLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tempHighErrorLimit.setStatus("current")
if mibBuilder.loadTexts:
    tempHighErrorLimit.setUnits("degrees Celscius")


class _TempLowWarnLimit_Type(Integer32):
    """Custom type tempLowWarnLimit based on Integer32"""
    defaultValue = -10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 60),
    )


_TempLowWarnLimit_Type.__name__ = "Integer32"
_TempLowWarnLimit_Object = MibScalar
tempLowWarnLimit = _TempLowWarnLimit_Object(
    (1, 3, 6, 1, 4, 1, 13995, 12, 10),
    _TempLowWarnLimit_Type()
)
tempLowWarnLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tempLowWarnLimit.setStatus("current")
if mibBuilder.loadTexts:
    tempLowWarnLimit.setUnits("degrees Celscius")


class _TempLowErrorLimit_Type(Integer32):
    """Custom type tempLowErrorLimit based on Integer32"""
    defaultValue = -30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 60),
    )


_TempLowErrorLimit_Type.__name__ = "Integer32"
_TempLowErrorLimit_Object = MibScalar
tempLowErrorLimit = _TempLowErrorLimit_Object(
    (1, 3, 6, 1, 4, 1, 13995, 12, 11),
    _TempLowErrorLimit_Type()
)
tempLowErrorLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tempLowErrorLimit.setStatus("current")
if mibBuilder.loadTexts:
    tempLowErrorLimit.setUnits("degrees Celscius")


class _TempHighWarnHist_Type(Integer32):
    """Custom type tempHighWarnHist based on Integer32"""
    defaultValue = 55

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-10, 150),
    )


_TempHighWarnHist_Type.__name__ = "Integer32"
_TempHighWarnHist_Object = MibScalar
tempHighWarnHist = _TempHighWarnHist_Object(
    (1, 3, 6, 1, 4, 1, 13995, 12, 12),
    _TempHighWarnHist_Type()
)
tempHighWarnHist.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tempHighWarnHist.setStatus("current")
if mibBuilder.loadTexts:
    tempHighWarnHist.setUnits("degrees Celsius")


class _TempHighErrorHist_Type(Integer32):
    """Custom type tempHighErrorHist based on Integer32"""
    defaultValue = 90

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-10, 150),
    )


_TempHighErrorHist_Type.__name__ = "Integer32"
_TempHighErrorHist_Object = MibScalar
tempHighErrorHist = _TempHighErrorHist_Object(
    (1, 3, 6, 1, 4, 1, 13995, 12, 13),
    _TempHighErrorHist_Type()
)
tempHighErrorHist.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tempHighErrorHist.setStatus("current")
if mibBuilder.loadTexts:
    tempHighErrorHist.setUnits("degrees Celscius")


class _TempLowWarnHist_Type(Integer32):
    """Custom type tempLowWarnHist based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 60),
    )


_TempLowWarnHist_Type.__name__ = "Integer32"
_TempLowWarnHist_Object = MibScalar
tempLowWarnHist = _TempLowWarnHist_Object(
    (1, 3, 6, 1, 4, 1, 13995, 12, 14),
    _TempLowWarnHist_Type()
)
tempLowWarnHist.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tempLowWarnHist.setStatus("current")
if mibBuilder.loadTexts:
    tempLowWarnHist.setUnits("degrees Celscius")


class _TempLowErrorHist_Type(Integer32):
    """Custom type tempLowErrorHist based on Integer32"""
    defaultValue = -20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 60),
    )


_TempLowErrorHist_Type.__name__ = "Integer32"
_TempLowErrorHist_Object = MibScalar
tempLowErrorHist = _TempLowErrorHist_Object(
    (1, 3, 6, 1, 4, 1, 13995, 12, 15),
    _TempLowErrorHist_Type()
)
tempLowErrorHist.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tempLowErrorHist.setStatus("current")
if mibBuilder.loadTexts:
    tempLowErrorHist.setUnits("degrees Celsius")


class _TempSystemTemp_Type(Integer32):
    """Custom type tempSystemTemp based on Integer32"""
    defaultValue = 0


_TempSystemTemp_Object = MibScalar
tempSystemTemp = _TempSystemTemp_Object(
    (1, 3, 6, 1, 4, 1, 13995, 12, 16),
    _TempSystemTemp_Type()
)
tempSystemTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempSystemTemp.setStatus("current")

# Managed Objects groups


# Notification objects

swupgradeCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 13995, 3, 19)
)
swupgradeCompleted.setObjects(
      *(("Amperion-MIB", "backupPartitionContents"),
        ("Amperion-MIB", "backupCRC"),
        ("Amperion-MIB", "primaryPartitionContents"),
        ("Amperion-MIB", "primaryCRC"),
        ("Amperion-MIB", "bootPartition"))
)
if mibBuilder.loadTexts:
    swupgradeCompleted.setStatus(
        "current"
    )

psImageChecksumError = NotificationType(
    (1, 3, 6, 1, 4, 1, 13995, 4, 14)
)
psImageChecksumError.setObjects(
    ("Amperion-MIB", "eventDescription")
)
if mibBuilder.loadTexts:
    psImageChecksumError.setStatus(
        "current"
    )

criticalBatteryShutdownWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 13995, 4, 15)
)
criticalBatteryShutdownWarning.setObjects(
    ("Amperion-MIB", "eventDescription")
)
if mibBuilder.loadTexts:
    criticalBatteryShutdownWarning.setStatus(
        "current"
    )

p12vOutOfRange = NotificationType(
    (1, 3, 6, 1, 4, 1, 13995, 4, 16)
)
p12vOutOfRange.setObjects(
    ("Amperion-MIB", "eventDescription")
)
if mibBuilder.loadTexts:
    p12vOutOfRange.setStatus(
        "current"
    )

m8point5vOutOfRange = NotificationType(
    (1, 3, 6, 1, 4, 1, 13995, 4, 17)
)
m8point5vOutOfRange.setObjects(
    ("Amperion-MIB", "eventDescription")
)
if mibBuilder.loadTexts:
    m8point5vOutOfRange.setStatus(
        "current"
    )

p5vOutOfRange = NotificationType(
    (1, 3, 6, 1, 4, 1, 13995, 4, 18)
)
p5vOutOfRange.setObjects(
    ("Amperion-MIB", "eventDescription")
)
if mibBuilder.loadTexts:
    p5vOutOfRange.setStatus(
        "current"
    )

p3point3vOutOfRange = NotificationType(
    (1, 3, 6, 1, 4, 1, 13995, 4, 19)
)
p3point3vOutOfRange.setObjects(
    ("Amperion-MIB", "eventDescription")
)
if mibBuilder.loadTexts:
    p3point3vOutOfRange.setStatus(
        "current"
    )

batteryVoltsOutOfRange = NotificationType(
    (1, 3, 6, 1, 4, 1, 13995, 4, 20)
)
batteryVoltsOutOfRange.setObjects(
    ("Amperion-MIB", "eventDescription")
)
if mibBuilder.loadTexts:
    batteryVoltsOutOfRange.setStatus(
        "current"
    )

mcuTempOutOfRange = NotificationType(
    (1, 3, 6, 1, 4, 1, 13995, 4, 21)
)
mcuTempOutOfRange.setObjects(
    ("Amperion-MIB", "eventDescription")
)
if mibBuilder.loadTexts:
    mcuTempOutOfRange.setStatus(
        "current"
    )

batteryTempOutOfRange = NotificationType(
    (1, 3, 6, 1, 4, 1, 13995, 4, 22)
)
batteryTempOutOfRange.setObjects(
    ("Amperion-MIB", "eventDescription")
)
if mibBuilder.loadTexts:
    batteryTempOutOfRange.setStatus(
        "current"
    )

psDetectedCommLapse = NotificationType(
    (1, 3, 6, 1, 4, 1, 13995, 4, 23)
)
psDetectedCommLapse.setObjects(
    ("Amperion-MIB", "eventDescription")
)
if mibBuilder.loadTexts:
    psDetectedCommLapse.setStatus(
        "current"
    )

criticalRequestAborted = NotificationType(
    (1, 3, 6, 1, 4, 1, 13995, 4, 24)
)
criticalRequestAborted.setObjects(
    ("Amperion-MIB", "eventDescription")
)
if mibBuilder.loadTexts:
    criticalRequestAborted.setStatus(
        "current"
    )

powerSupplyInternalError = NotificationType(
    (1, 3, 6, 1, 4, 1, 13995, 4, 25)
)
powerSupplyInternalError.setObjects(
    ("Amperion-MIB", "eventDescription")
)
if mibBuilder.loadTexts:
    powerSupplyInternalError.setStatus(
        "current"
    )

psBatteryNotConnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 13995, 4, 26)
)
psBatteryNotConnected.setObjects(
    ("Amperion-MIB", "eventDescription")
)
if mibBuilder.loadTexts:
    psBatteryNotConnected.setStatus(
        "current"
    )

psAcOnOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 13995, 4, 27)
)
psAcOnOff.setObjects(
    ("Amperion-MIB", "eventDescription")
)
if mibBuilder.loadTexts:
    psAcOnOff.setStatus(
        "current"
    )

psHardwareError = NotificationType(
    (1, 3, 6, 1, 4, 1, 13995, 4, 29)
)
psHardwareError.setObjects(
    ("Amperion-MIB", "eventDescription")
)
if mibBuilder.loadTexts:
    psHardwareError.setStatus(
        "current"
    )

npuDetectedCommLapse = NotificationType(
    (1, 3, 6, 1, 4, 1, 13995, 4, 34)
)
npuDetectedCommLapse.setObjects(
    ("Amperion-MIB", "eventDescription")
)
if mibBuilder.loadTexts:
    npuDetectedCommLapse.setStatus(
        "current"
    )

interfaceAdminDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 13995, 5, 3)
)
interfaceAdminDown.setObjects(
    ("Amperion-MIB", "amperionifDescr")
)
if mibBuilder.loadTexts:
    interfaceAdminDown.setStatus(
        "current"
    )

interfaceAdminUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 13995, 5, 4)
)
interfaceAdminUp.setObjects(
    ("Amperion-MIB", "amperionifDescr")
)
if mibBuilder.loadTexts:
    interfaceAdminUp.setStatus(
        "current"
    )

plcUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 13995, 11, 3)
)
plcUp.setObjects(
    ("Amperion-MIB", "plcEventDescription")
)
if mibBuilder.loadTexts:
    plcUp.setStatus(
        "current"
    )

plcDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 13995, 11, 4)
)
plcDown.setObjects(
    ("Amperion-MIB", "plcEventDescription")
)
if mibBuilder.loadTexts:
    plcDown.setStatus(
        "current"
    )

tempHighWarnLimitTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 13995, 12, 4)
)
tempHighWarnLimitTrap.setObjects(
      *(("Amperion-MIB", "tempEventDescription"),
        ("Amperion-MIB", "tempHighWarnLimit"),
        ("Amperion-MIB", "tempSystemTemp"))
)
if mibBuilder.loadTexts:
    tempHighWarnLimitTrap.setStatus(
        "current"
    )

tempHighErrorLimitTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 13995, 12, 6)
)
tempHighErrorLimitTrap.setObjects(
      *(("Amperion-MIB", "tempEventDescription"),
        ("Amperion-MIB", "tempHighErrorLimit"),
        ("Amperion-MIB", "tempSystemTemp"))
)
if mibBuilder.loadTexts:
    tempHighErrorLimitTrap.setStatus(
        "current"
    )

tempLowWarnLimitTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 13995, 12, 7)
)
tempLowWarnLimitTrap.setObjects(
      *(("Amperion-MIB", "tempEventDescription"),
        ("Amperion-MIB", "tempLowWarnLimit"),
        ("Amperion-MIB", "tempSystemTemp"))
)
if mibBuilder.loadTexts:
    tempLowWarnLimitTrap.setStatus(
        "current"
    )

tempLowErrorLimitTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 13995, 12, 8)
)
tempLowErrorLimitTrap.setObjects(
      *(("Amperion-MIB", "tempEventDescription"),
        ("Amperion-MIB", "tempLowErrorLimit"),
        ("Amperion-MIB", "tempSystemTemp"))
)
if mibBuilder.loadTexts:
    tempLowErrorLimitTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Amperion-MIB",
    **{"amperion": amperion,
       "ds2": ds2,
       "powerline": powerline,
       "plMibIIExtension": plMibIIExtension,
       "plCards": plCards,
       "plCdNumber": plCdNumber,
       "plCdTable": plCdTable,
       "plCdEntry": plCdEntry,
       "plCdIndex": plCdIndex,
       "plCdType": plCdType,
       "plCdLink": plCdLink,
       "plCdShortMacAddress": plCdShortMacAddress,
       "plCdLongMacAddress": plCdLongMacAddress,
       "plCdHardwareVersion": plCdHardwareVersion,
       "plCdFirmwareVersion": plCdFirmwareVersion,
       "plCdDriverVersion": plCdDriverVersion,
       "plCdReset": plCdReset,
       "plCdFactoryReset": plCdFactoryReset,
       "plCdSaveAsPermanent": plCdSaveAsPermanent,
       "plCdStatus": plCdStatus,
       "plCdRemoteList": plCdRemoteList,
       "plCdNumRemoteList": plCdNumRemoteList,
       "plNetwork": plNetwork,
       "plNetTable": plNetTable,
       "plNetEntry": plNetEntry,
       "plNetShortMacAddress": plNetShortMacAddress,
       "plNetLongMacAddress": plNetLongMacAddress,
       "plNetRowStatus": plNetRowStatus,
       "plTransmission": plTransmission,
       "plInpTable": plInpTable,
       "plInpEntry": plInpEntry,
       "plInpTotalOctets": plInpTotalOctets,
       "plInpGain": plInpGain,
       "plInpAGC": plInpAGC,
       "plInpMaxGain": plInpMaxGain,
       "plInpThresholds": plInpThresholds,
       "plInpAttenuationGain": plInpAttenuationGain,
       "plInpSamsDecode": plInpSamsDecode,
       "plInpSamsGood": plInpSamsGood,
       "plInpSamsBad": plInpSamsBad,
       "plInpNodeTable": plInpNodeTable,
       "plInpNodeEntry": plInpNodeEntry,
       "plInpNodeReceivedPkts": plInpNodeReceivedPkts,
       "plInpNodeReceivedUnrecPkts": plInpNodeReceivedUnrecPkts,
       "plInpNodeReceivedCorrectedPkts": plInpNodeReceivedCorrectedPkts,
       "plInpNodeReceivedOctets": plInpNodeReceivedOctets,
       "plInpNodeReceivedCorrectedOctets": plInpNodeReceivedCorrectedOctets,
       "plInpNodeReceivedPower": plInpNodeReceivedPower,
       "plInpNodePLR": plInpNodePLR,
       "plInpNodeMeanBPC": plInpNodeMeanBPC,
       "plInpNodeSNRChanges": plInpNodeSNRChanges,
       "plInpNodeSNR": plInpNodeSNR,
       "plInpNodeBPC": plInpNodeBPC,
       "plInpNodeCFR": plInpNodeCFR,
       "plInpNodeEnableCarriers": plInpNodeEnableCarriers,
       "plInpNodeProtocolEnableCarriers": plInpNodeProtocolEnableCarriers,
       "plInpNodeEnableProtocolEnableCarriers": plInpNodeEnableProtocolEnableCarriers,
       "plTraps": plTraps,
       "plRemoteCPE": plRemoteCPE,
       "internal": internal,
       "amperionSystem": amperionSystem,
       "serialNumber": serialNumber,
       "partNumber": partNumber,
       "rombootVersion": rombootVersion,
       "alarms": alarms,
       "alarmsEntry": alarmsEntry,
       "alarmIndex": alarmIndex,
       "description": description,
       "productType": productType,
       "userGpsInfoString": userGpsInfoString,
       "linuxVersion": linuxVersion,
       "amperionSysDescr": amperionSysDescr,
       "amperionSysObjectID": amperionSysObjectID,
       "amperionSysUpTime": amperionSysUpTime,
       "amperionSysContact": amperionSysContact,
       "amperionSysName": amperionSysName,
       "amperionSysLocation": amperionSysLocation,
       "amperionSysServices": amperionSysServices,
       "amperionTrapMgr1": amperionTrapMgr1,
       "amperionTrapMgr2": amperionTrapMgr2,
       "amperionTrapMgr3": amperionTrapMgr3,
       "softwareUpgrade": softwareUpgrade,
       "serverAddress": serverAddress,
       "primaryPartitionContents": primaryPartitionContents,
       "currentState": currentState,
       "bootPartition": bootPartition,
       "upgradePartition": upgradePartition,
       "currentPartition": currentPartition,
       "commandOptions": commandOptions,
       "backupPartitionContents": backupPartitionContents,
       "primaryCRC": primaryCRC,
       "backupCRC": backupCRC,
       "lastStatus": lastStatus,
       "filename": filename,
       "server1Address": server1Address,
       "server2Address": server2Address,
       "upgradeSchedule": upgradeSchedule,
       "rebootSchedule": rebootSchedule,
       "login": login,
       "password": password,
       "swupgradeCompleted": swupgradeCompleted,
       "psGroup": psGroup,
       "acLineVoltage": acLineVoltage,
       "plus12v": plus12v,
       "minus8point5v": minus8point5v,
       "plus5v": plus5v,
       "plus3point3v": plus3point3v,
       "batteryCaseTemp": batteryCaseTemp,
       "internalMcuTemp": internalMcuTemp,
       "batteryCurrent": batteryCurrent,
       "batteryVoltage": batteryVoltage,
       "mcuSoftwareVersion": mcuSoftwareVersion,
       "powerCycleNpu": powerCycleNpu,
       "psMode": psMode,
       "shutdownNpu": shutdownNpu,
       "psImageChecksumError": psImageChecksumError,
       "criticalBatteryShutdownWarning": criticalBatteryShutdownWarning,
       "p12vOutOfRange": p12vOutOfRange,
       "m8point5vOutOfRange": m8point5vOutOfRange,
       "p5vOutOfRange": p5vOutOfRange,
       "p3point3vOutOfRange": p3point3vOutOfRange,
       "batteryVoltsOutOfRange": batteryVoltsOutOfRange,
       "mcuTempOutOfRange": mcuTempOutOfRange,
       "batteryTempOutOfRange": batteryTempOutOfRange,
       "psDetectedCommLapse": psDetectedCommLapse,
       "criticalRequestAborted": criticalRequestAborted,
       "powerSupplyInternalError": powerSupplyInternalError,
       "psBatteryNotConnected": psBatteryNotConnected,
       "psAcOnOff": psAcOnOff,
       "psHardwareVersion": psHardwareVersion,
       "psHardwareError": psHardwareError,
       "psEt": psEt,
       "npuEt": npuEt,
       "npuPuTimes": npuPuTimes,
       "eventDescription": eventDescription,
       "npuDetectedCommLapse": npuDetectedCommLapse,
       "amperionInterfaces": amperionInterfaces,
       "amperionifNumber": amperionifNumber,
       "amperionifTable": amperionifTable,
       "amperionifEntry": amperionifEntry,
       "amperionWirelessActivate": amperionWirelessActivate,
       "amperionifDescr": amperionifDescr,
       "amperionifType": amperionifType,
       "amperionifMtu": amperionifMtu,
       "amperionifSpeed": amperionifSpeed,
       "amperionifPhysAddress": amperionifPhysAddress,
       "amperionifAdminStatus": amperionifAdminStatus,
       "amperionifOperStatus": amperionifOperStatus,
       "amperionifLastChange": amperionifLastChange,
       "amperionifInOctets": amperionifInOctets,
       "amperionifInUcastPkts": amperionifInUcastPkts,
       "amperionifInNUcastPkts": amperionifInNUcastPkts,
       "amperionifInDiscards": amperionifInDiscards,
       "amperionifInErrors": amperionifInErrors,
       "amperionifInUnknownProtos": amperionifInUnknownProtos,
       "amperionifOutOctets": amperionifOutOctets,
       "amperionifOutUcastPkts": amperionifOutUcastPkts,
       "amperionifOutNUcastPkts": amperionifOutNUcastPkts,
       "amperionifOutDiscards": amperionifOutDiscards,
       "amperionifOutErrors": amperionifOutErrors,
       "amperionifOutQLen": amperionifOutQLen,
       "amperionifSpecific": amperionifSpecific,
       "amperionWirelessConfigEssid": amperionWirelessConfigEssid,
       "amperionWirelessConfigMode": amperionWirelessConfigMode,
       "amperionWirelessConfigChanFreq": amperionWirelessConfigChanFreq,
       "amperionWirelessConfigKey": amperionWirelessConfigKey,
       "amperionWirelessLinkQuality": amperionWirelessLinkQuality,
       "amperionWirelessSignalLevel": amperionWirelessSignalLevel,
       "amperionWirelessNoiseLevel": amperionWirelessNoiseLevel,
       "amperionWirelessConfigWifType": amperionWirelessConfigWifType,
       "amperionWirelessConfigBitRate": amperionWirelessConfigBitRate,
       "amperionWirelessConfigWDSPeer": amperionWirelessConfigWDSPeer,
       "interfaceAdminDown": interfaceAdminDown,
       "interfaceAdminUp": interfaceAdminUp,
       "amperionWireless": amperionWireless,
       "accessControlStatus": accessControlStatus,
       "ampMacAcceptTable": ampMacAcceptTable,
       "ampMacAcceptEntry": ampMacAcceptEntry,
       "macAcceptTableMacAddress": macAcceptTableMacAddress,
       "macAcceptTableRowStatus": macAcceptTableRowStatus,
       "macAcceptTableIndex": macAcceptTableIndex,
       "macAcceptTableWirelessIf": macAcceptTableWirelessIf,
       "amperionipAddrTable": amperionipAddrTable,
       "amperionipAddrEntry": amperionipAddrEntry,
       "amperionipAdEntAddr": amperionipAdEntAddr,
       "amperionipAdEntIfName": amperionipAdEntIfName,
       "amperionipAdEntNetMask": amperionipAdEntNetMask,
       "amperionipAdEntBcastAddr": amperionipAdEntBcastAddr,
       "amperionipAdEntReasmMaxSize": amperionipAdEntReasmMaxSize,
       "amperionipAdRowStatus": amperionipAdRowStatus,
       "amperionipAdEntActivate": amperionipAdEntActivate,
       "qualityOfService": qualityOfService,
       "serviceClassA": serviceClassA,
       "serviceClassB": serviceClassB,
       "serviceClassC": serviceClassC,
       "serviceClassD": serviceClassD,
       "subscriberTable": subscriberTable,
       "subscriberEntry": subscriberEntry,
       "index": index,
       "name": name,
       "ipAddress": ipAddress,
       "macAddress": macAddress,
       "serviceClass": serviceClass,
       "rowStatus": rowStatus,
       "upstreamDownstreamRatio": upstreamDownstreamRatio,
       "qosStatus": qosStatus,
       "afe": afe,
       "afeExtractor": afeExtractor,
       "afeExtTxGain": afeExtTxGain,
       "afeExtRxGain": afeExtRxGain,
       "afeExtDownstream": afeExtDownstream,
       "afeExtUpstream": afeExtUpstream,
       "afeExtActivate": afeExtActivate,
       "afeInjector": afeInjector,
       "afeInjTxGain": afeInjTxGain,
       "afeInjRxGain": afeInjRxGain,
       "afeInjDownstream": afeInjDownstream,
       "afeInjUpstream": afeInjUpstream,
       "afeInjActivate": afeInjActivate,
       "amperionRoutes": amperionRoutes,
       "amperionRouteTable": amperionRouteTable,
       "amperionRouteEntry": amperionRouteEntry,
       "ipRouteDest": ipRouteDest,
       "ipRouteIfIndex": ipRouteIfIndex,
       "ipRouteMetric1": ipRouteMetric1,
       "ipRouteMetric2": ipRouteMetric2,
       "ipRouteMetric3": ipRouteMetric3,
       "ipRouteMetric4": ipRouteMetric4,
       "ipRouteNextHop": ipRouteNextHop,
       "ipRouteType": ipRouteType,
       "ipRouteProto": ipRouteProto,
       "ipRouteAge": ipRouteAge,
       "ipRouteMask": ipRouteMask,
       "ipRouteMetric5": ipRouteMetric5,
       "ipRouteInfo": ipRouteInfo,
       "ipDefRouteActivate": ipDefRouteActivate,
       "plc": plc,
       "plcExtractor": plcExtractor,
       "plcExtTxGain": plcExtTxGain,
       "plcExtRxGain": plcExtRxGain,
       "plcInjector": plcInjector,
       "plcInjTxGain": plcInjTxGain,
       "plcInjRxGain": plcInjRxGain,
       "plcUp": plcUp,
       "plcDown": plcDown,
       "afeCpldResetCount": afeCpldResetCount,
       "plcLossCount": plcLossCount,
       "resetCounters": resetCounters,
       "optimizationTable": optimizationTable,
       "optimizationEntry": optimizationEntry,
       "extrIpaddress": extrIpaddress,
       "extrChannelNumber": extrChannelNumber,
       "upstreamFreq": upstreamFreq,
       "downstreamFreq": downstreamFreq,
       "rxGain": rxGain,
       "txGain": txGain,
       "plcThroughput": plcThroughput,
       "upStreamDownStream": upStreamDownStream,
       "gpsInfo": gpsInfo,
       "plcEventDescription": plcEventDescription,
       "tempGroup": tempGroup,
       "tempFanState": tempFanState,
       "tempFanTargetTemp": tempFanTargetTemp,
       "tempHighWarnLimit": tempHighWarnLimit,
       "tempHighWarnLimitTrap": tempHighWarnLimitTrap,
       "tempEventDescription": tempEventDescription,
       "tempHighErrorLimitTrap": tempHighErrorLimitTrap,
       "tempLowWarnLimitTrap": tempLowWarnLimitTrap,
       "tempLowErrorLimitTrap": tempLowErrorLimitTrap,
       "tempHighErrorLimit": tempHighErrorLimit,
       "tempLowWarnLimit": tempLowWarnLimit,
       "tempLowErrorLimit": tempLowErrorLimit,
       "tempHighWarnHist": tempHighWarnHist,
       "tempHighErrorHist": tempHighErrorHist,
       "tempLowWarnHist": tempLowWarnHist,
       "tempLowErrorHist": tempLowErrorHist,
       "tempSystemTemp": tempSystemTemp}
)
