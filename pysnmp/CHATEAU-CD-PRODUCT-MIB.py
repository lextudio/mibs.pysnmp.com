# SNMP MIB module (CHATEAU-CD-PRODUCT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CHATEAU-CD-PRODUCT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:54:36 2024
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

(ChateauEventSeverity,
 ChateauTrapControl,
 chateauCDProduct) = mibBuilder.importSymbols(
    "CHATEAUSYSTEMS-REGISTRATIONS-MIB",
    "ChateauEventSeverity",
    "ChateauTrapControl",
    "chateauCDProduct")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

chateauCDProductMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10910, 2, 2, 3, 1, 1)
)
chateauCDProductMIB.setRevisions(
        ("2005-11-09 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ChateauCDProdConfig_ObjectIdentity = ObjectIdentity
chateauCDProdConfig = _ChateauCDProdConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10910, 2, 2, 3, 1, 1, 1)
)
if mibBuilder.loadTexts:
    chateauCDProdConfig.setStatus("current")
_CdStaticConfig_ObjectIdentity = ObjectIdentity
cdStaticConfig = _CdStaticConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10910, 2, 2, 3, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cdStaticConfig.setStatus("current")
_CdStCfgManufacturer_Type = ObjectIdentifier
_CdStCfgManufacturer_Object = MibScalar
cdStCfgManufacturer = _CdStCfgManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 10910, 2, 2, 3, 1, 1, 1, 1, 1),
    _CdStCfgManufacturer_Type()
)
cdStCfgManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdStCfgManufacturer.setStatus("current")


class _CdStCfgModel_Type(DisplayString):
    """Custom type cdStCfgModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 16),
    )


_CdStCfgModel_Type.__name__ = "DisplayString"
_CdStCfgModel_Object = MibScalar
cdStCfgModel = _CdStCfgModel_Object(
    (1, 3, 6, 1, 4, 1, 10910, 2, 2, 3, 1, 1, 1, 1, 2),
    _CdStCfgModel_Type()
)
cdStCfgModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdStCfgModel.setStatus("current")
_CdStCfgFirmwareRev_Type = DisplayString
_CdStCfgFirmwareRev_Object = MibScalar
cdStCfgFirmwareRev = _CdStCfgFirmwareRev_Object(
    (1, 3, 6, 1, 4, 1, 10910, 2, 2, 3, 1, 1, 1, 1, 10),
    _CdStCfgFirmwareRev_Type()
)
cdStCfgFirmwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdStCfgFirmwareRev.setStatus("current")
_CdDynamicConfig_ObjectIdentity = ObjectIdentity
cdDynamicConfig = _CdDynamicConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10910, 2, 2, 3, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cdDynamicConfig.setStatus("current")


class _CdDynCfgUserAlias_Type(DisplayString):
    """Custom type cdDynCfgUserAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CdDynCfgUserAlias_Type.__name__ = "DisplayString"
_CdDynCfgUserAlias_Object = MibScalar
cdDynCfgUserAlias = _CdDynCfgUserAlias_Object(
    (1, 3, 6, 1, 4, 1, 10910, 2, 2, 3, 1, 1, 1, 2, 1),
    _CdDynCfgUserAlias_Type()
)
cdDynCfgUserAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdDynCfgUserAlias.setStatus("current")
_ChateauCDProdControl_ObjectIdentity = ObjectIdentity
chateauCDProdControl = _ChateauCDProdControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10910, 2, 2, 3, 1, 1, 2)
)
if mibBuilder.loadTexts:
    chateauCDProdControl.setStatus("current")


class _CdCtlPower_Type(Integer32):
    """Custom type cdCtlPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_CdCtlPower_Type.__name__ = "Integer32"
_CdCtlPower_Object = MibScalar
cdCtlPower = _CdCtlPower_Object(
    (1, 3, 6, 1, 4, 1, 10910, 2, 2, 3, 1, 1, 2, 1),
    _CdCtlPower_Type()
)
cdCtlPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdCtlPower.setStatus("current")


class _CdCtlTrayDoor_Type(Integer32):
    """Custom type cdCtlTrayDoor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("closed", 1),
          ("open", 2))
    )


_CdCtlTrayDoor_Type.__name__ = "Integer32"
_CdCtlTrayDoor_Object = MibScalar
cdCtlTrayDoor = _CdCtlTrayDoor_Object(
    (1, 3, 6, 1, 4, 1, 10910, 2, 2, 3, 1, 1, 2, 2),
    _CdCtlTrayDoor_Type()
)
cdCtlTrayDoor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdCtlTrayDoor.setStatus("current")
_CdCtlPlaying_Type = TruthValue
_CdCtlPlaying_Object = MibScalar
cdCtlPlaying = _CdCtlPlaying_Object(
    (1, 3, 6, 1, 4, 1, 10910, 2, 2, 3, 1, 1, 2, 3),
    _CdCtlPlaying_Type()
)
cdCtlPlaying.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdCtlPlaying.setStatus("current")
_ChateauCDProdStatus_ObjectIdentity = ObjectIdentity
chateauCDProdStatus = _ChateauCDProdStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10910, 2, 2, 3, 1, 1, 3)
)
if mibBuilder.loadTexts:
    chateauCDProdStatus.setStatus("current")
_CdChassisStatus_ObjectIdentity = ObjectIdentity
cdChassisStatus = _CdChassisStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10910, 2, 2, 3, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cdChassisStatus.setStatus("current")
_CdChStPowerOnHours_Type = Unsigned32
_CdChStPowerOnHours_Object = MibScalar
cdChStPowerOnHours = _CdChStPowerOnHours_Object(
    (1, 3, 6, 1, 4, 1, 10910, 2, 2, 3, 1, 1, 3, 1, 1),
    _CdChStPowerOnHours_Type()
)
cdChStPowerOnHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdChStPowerOnHours.setStatus("current")
_CdChStLaserOnHours_Type = Unsigned32
_CdChStLaserOnHours_Object = MibScalar
cdChStLaserOnHours = _CdChStLaserOnHours_Object(
    (1, 3, 6, 1, 4, 1, 10910, 2, 2, 3, 1, 1, 3, 1, 2),
    _CdChStLaserOnHours_Type()
)
cdChStLaserOnHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdChStLaserOnHours.setStatus("current")
_CdChStCrcErrorCtr_Type = Counter32
_CdChStCrcErrorCtr_Object = MibScalar
cdChStCrcErrorCtr = _CdChStCrcErrorCtr_Object(
    (1, 3, 6, 1, 4, 1, 10910, 2, 2, 3, 1, 1, 3, 1, 3),
    _CdChStCrcErrorCtr_Type()
)
cdChStCrcErrorCtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdChStCrcErrorCtr.setStatus("current")
_CdChStTemperature_Type = Integer32
_CdChStTemperature_Object = MibScalar
cdChStTemperature = _CdChStTemperature_Object(
    (1, 3, 6, 1, 4, 1, 10910, 2, 2, 3, 1, 1, 3, 1, 4),
    _CdChStTemperature_Type()
)
cdChStTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdChStTemperature.setStatus("current")
if mibBuilder.loadTexts:
    cdChStTemperature.setUnits("Celcius")


class _CdChStPowerSupply_Type(Integer32):
    """Custom type cdChStPowerSupply based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("okay", 1),
          ("voltageError", 2))
    )


_CdChStPowerSupply_Type.__name__ = "Integer32"
_CdChStPowerSupply_Object = MibScalar
cdChStPowerSupply = _CdChStPowerSupply_Object(
    (1, 3, 6, 1, 4, 1, 10910, 2, 2, 3, 1, 1, 3, 1, 5),
    _CdChStPowerSupply_Type()
)
cdChStPowerSupply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdChStPowerSupply.setStatus("current")
_CdChangerStatus_ObjectIdentity = ObjectIdentity
cdChangerStatus = _CdChangerStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10910, 2, 2, 3, 1, 1, 3, 2)
)
if mibBuilder.loadTexts:
    cdChangerStatus.setStatus("current")


class _CdChangerNbrCdSlots_Type(Unsigned32):
    """Custom type cdChangerNbrCdSlots based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_CdChangerNbrCdSlots_Type.__name__ = "Unsigned32"
_CdChangerNbrCdSlots_Object = MibScalar
cdChangerNbrCdSlots = _CdChangerNbrCdSlots_Object(
    (1, 3, 6, 1, 4, 1, 10910, 2, 2, 3, 1, 1, 3, 2, 1),
    _CdChangerNbrCdSlots_Type()
)
cdChangerNbrCdSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdChangerNbrCdSlots.setStatus("current")
_CdChangerSlotTable_Object = MibTable
cdChangerSlotTable = _CdChangerSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 10910, 2, 2, 3, 1, 1, 3, 2, 2)
)
if mibBuilder.loadTexts:
    cdChangerSlotTable.setStatus("current")
_CdChangerSlotEntry_Object = MibTableRow
cdChangerSlotEntry = _CdChangerSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 10910, 2, 2, 3, 1, 1, 3, 2, 2, 1)
)
cdChangerSlotEntry.setIndexNames(
    (0, "CHATEAU-CD-PRODUCT-MIB", "cdChangerSlotNbr"),
)
if mibBuilder.loadTexts:
    cdChangerSlotEntry.setStatus("current")


class _CdChangerSlotNbr_Type(Unsigned32):
    """Custom type cdChangerSlotNbr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_CdChangerSlotNbr_Type.__name__ = "Unsigned32"
_CdChangerSlotNbr_Object = MibTableColumn
cdChangerSlotNbr = _CdChangerSlotNbr_Object(
    (1, 3, 6, 1, 4, 1, 10910, 2, 2, 3, 1, 1, 3, 2, 2, 1, 1),
    _CdChangerSlotNbr_Type()
)
cdChangerSlotNbr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdChangerSlotNbr.setStatus("current")


class _CdChangerSlotStatus_Type(Integer32):
    """Custom type cdChangerSlotStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("containsCD", 1),
          ("empty", 2))
    )


_CdChangerSlotStatus_Type.__name__ = "Integer32"
_CdChangerSlotStatus_Object = MibTableColumn
cdChangerSlotStatus = _CdChangerSlotStatus_Object(
    (1, 3, 6, 1, 4, 1, 10910, 2, 2, 3, 1, 1, 3, 2, 2, 1, 2),
    _CdChangerSlotStatus_Type()
)
cdChangerSlotStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdChangerSlotStatus.setStatus("current")
_CdChangerSlotCDTrackPlaying_Type = Unsigned32
_CdChangerSlotCDTrackPlaying_Object = MibTableColumn
cdChangerSlotCDTrackPlaying = _CdChangerSlotCDTrackPlaying_Object(
    (1, 3, 6, 1, 4, 1, 10910, 2, 2, 3, 1, 1, 3, 2, 2, 1, 3),
    _CdChangerSlotCDTrackPlaying_Type()
)
cdChangerSlotCDTrackPlaying.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdChangerSlotCDTrackPlaying.setStatus("current")
_CdChangerCDNbrTracks_Type = Unsigned32
_CdChangerCDNbrTracks_Object = MibTableColumn
cdChangerCDNbrTracks = _CdChangerCDNbrTracks_Object(
    (1, 3, 6, 1, 4, 1, 10910, 2, 2, 3, 1, 1, 3, 2, 2, 1, 4),
    _CdChangerCDNbrTracks_Type()
)
cdChangerCDNbrTracks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdChangerCDNbrTracks.setStatus("current")
_CdChangerCDTrackTable_Object = MibTable
cdChangerCDTrackTable = _CdChangerCDTrackTable_Object(
    (1, 3, 6, 1, 4, 1, 10910, 2, 2, 3, 1, 1, 3, 2, 3)
)
if mibBuilder.loadTexts:
    cdChangerCDTrackTable.setStatus("current")
_CdChangerCDTrackEntry_Object = MibTableRow
cdChangerCDTrackEntry = _CdChangerCDTrackEntry_Object(
    (1, 3, 6, 1, 4, 1, 10910, 2, 2, 3, 1, 1, 3, 2, 3, 1)
)
cdChangerCDTrackEntry.setIndexNames(
    (0, "CHATEAU-CD-PRODUCT-MIB", "cdChangerSlotNbr"),
    (0, "CHATEAU-CD-PRODUCT-MIB", "cdChangerCDTrackNbr"),
)
if mibBuilder.loadTexts:
    cdChangerCDTrackEntry.setStatus("current")
_CdChangerCDTrackNbr_Type = Unsigned32
_CdChangerCDTrackNbr_Object = MibTableColumn
cdChangerCDTrackNbr = _CdChangerCDTrackNbr_Object(
    (1, 3, 6, 1, 4, 1, 10910, 2, 2, 3, 1, 1, 3, 2, 3, 1, 1),
    _CdChangerCDTrackNbr_Type()
)
cdChangerCDTrackNbr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdChangerCDTrackNbr.setStatus("current")
_CdChangerCDTrackPlaying_Type = TruthValue
_CdChangerCDTrackPlaying_Object = MibTableColumn
cdChangerCDTrackPlaying = _CdChangerCDTrackPlaying_Object(
    (1, 3, 6, 1, 4, 1, 10910, 2, 2, 3, 1, 1, 3, 2, 3, 1, 2),
    _CdChangerCDTrackPlaying_Type()
)
cdChangerCDTrackPlaying.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdChangerCDTrackPlaying.setStatus("current")
_CdChangerCDTrackLengthSecs_Type = Unsigned32
_CdChangerCDTrackLengthSecs_Object = MibTableColumn
cdChangerCDTrackLengthSecs = _CdChangerCDTrackLengthSecs_Object(
    (1, 3, 6, 1, 4, 1, 10910, 2, 2, 3, 1, 1, 3, 2, 3, 1, 3),
    _CdChangerCDTrackLengthSecs_Type()
)
cdChangerCDTrackLengthSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdChangerCDTrackLengthSecs.setStatus("current")
_CdChangerCDTrackLengthStr_Type = DisplayString
_CdChangerCDTrackLengthStr_Object = MibTableColumn
cdChangerCDTrackLengthStr = _CdChangerCDTrackLengthStr_Object(
    (1, 3, 6, 1, 4, 1, 10910, 2, 2, 3, 1, 1, 3, 2, 3, 1, 4),
    _CdChangerCDTrackLengthStr_Type()
)
cdChangerCDTrackLengthStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdChangerCDTrackLengthStr.setStatus("current")


class _CdChangerCDTrackTitle_Type(DisplayString):
    """Custom type cdChangerCDTrackTitle based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CdChangerCDTrackTitle_Type.__name__ = "DisplayString"
_CdChangerCDTrackTitle_Object = MibTableColumn
cdChangerCDTrackTitle = _CdChangerCDTrackTitle_Object(
    (1, 3, 6, 1, 4, 1, 10910, 2, 2, 3, 1, 1, 3, 2, 3, 1, 5),
    _CdChangerCDTrackTitle_Type()
)
cdChangerCDTrackTitle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdChangerCDTrackTitle.setStatus("current")


class _CdChangerCDTrackArtist_Type(DisplayString):
    """Custom type cdChangerCDTrackArtist based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CdChangerCDTrackArtist_Type.__name__ = "DisplayString"
_CdChangerCDTrackArtist_Object = MibTableColumn
cdChangerCDTrackArtist = _CdChangerCDTrackArtist_Object(
    (1, 3, 6, 1, 4, 1, 10910, 2, 2, 3, 1, 1, 3, 2, 3, 1, 6),
    _CdChangerCDTrackArtist_Type()
)
cdChangerCDTrackArtist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdChangerCDTrackArtist.setStatus("current")
_ChateauCDProdEvents_ObjectIdentity = ObjectIdentity
chateauCDProdEvents = _ChateauCDProdEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10910, 2, 2, 3, 1, 1, 10)
)
if mibBuilder.loadTexts:
    chateauCDProdEvents.setStatus("current")
_CdEventList_ObjectIdentity = ObjectIdentity
cdEventList = _CdEventList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10910, 2, 2, 3, 1, 1, 10, 0)
)
if mibBuilder.loadTexts:
    cdEventList.setStatus("current")
_CdEventControl_ObjectIdentity = ObjectIdentity
cdEventControl = _CdEventControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10910, 2, 2, 3, 1, 1, 10, 1)
)
if mibBuilder.loadTexts:
    cdEventControl.setStatus("current")


class _CdEvCtlAgtPollFreq_Type(Unsigned32):
    """Custom type cdEvCtlAgtPollFreq based on Unsigned32"""
    defaultValue = 30


_CdEvCtlAgtPollFreq_Object = MibScalar
cdEvCtlAgtPollFreq = _CdEvCtlAgtPollFreq_Object(
    (1, 3, 6, 1, 4, 1, 10910, 2, 2, 3, 1, 1, 10, 1, 1),
    _CdEvCtlAgtPollFreq_Type()
)
cdEvCtlAgtPollFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdEvCtlAgtPollFreq.setStatus("current")
if mibBuilder.loadTexts:
    cdEvCtlAgtPollFreq.setUnits("seconds")


class _CdChassisTempAlarmThresh_Type(Integer32):
    """Custom type cdChassisTempAlarmThresh based on Integer32"""
    defaultValue = 40


_CdChassisTempAlarmThresh_Object = MibScalar
cdChassisTempAlarmThresh = _CdChassisTempAlarmThresh_Object(
    (1, 3, 6, 1, 4, 1, 10910, 2, 2, 3, 1, 1, 10, 1, 2),
    _CdChassisTempAlarmThresh_Type()
)
cdChassisTempAlarmThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdChassisTempAlarmThresh.setStatus("current")
if mibBuilder.loadTexts:
    cdChassisTempAlarmThresh.setUnits("Celcius")


class _CdChassisTempEvTrapEn_Type(ChateauTrapControl):
    """Custom type cdChassisTempEvTrapEn based on ChateauTrapControl"""


_CdChassisTempEvTrapEn_Object = MibScalar
cdChassisTempEvTrapEn = _CdChassisTempEvTrapEn_Object(
    (1, 3, 6, 1, 4, 1, 10910, 2, 2, 3, 1, 1, 10, 1, 10),
    _CdChassisTempEvTrapEn_Type()
)
cdChassisTempEvTrapEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdChassisTempEvTrapEn.setStatus("current")


class _CdPowerSupplyEvTrapEn_Type(ChateauTrapControl):
    """Custom type cdPowerSupplyEvTrapEn based on ChateauTrapControl"""


_CdPowerSupplyEvTrapEn_Object = MibScalar
cdPowerSupplyEvTrapEn = _CdPowerSupplyEvTrapEn_Object(
    (1, 3, 6, 1, 4, 1, 10910, 2, 2, 3, 1, 1, 10, 1, 20),
    _CdPowerSupplyEvTrapEn_Type()
)
cdPowerSupplyEvTrapEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdPowerSupplyEvTrapEn.setStatus("current")
_CdEventDescriptors_ObjectIdentity = ObjectIdentity
cdEventDescriptors = _CdEventDescriptors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10910, 2, 2, 3, 1, 1, 10, 2)
)
if mibBuilder.loadTexts:
    cdEventDescriptors.setStatus("current")
_CdEvSeverity_Type = ChateauEventSeverity
_CdEvSeverity_Object = MibScalar
cdEvSeverity = _CdEvSeverity_Object(
    (1, 3, 6, 1, 4, 1, 10910, 2, 2, 3, 1, 1, 10, 2, 1),
    _CdEvSeverity_Type()
)
cdEvSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cdEvSeverity.setStatus("current")


class _CdEvDescription_Type(DisplayString):
    """Custom type cdEvDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CdEvDescription_Type.__name__ = "DisplayString"
_CdEvDescription_Object = MibScalar
cdEvDescription = _CdEvDescription_Object(
    (1, 3, 6, 1, 4, 1, 10910, 2, 2, 3, 1, 1, 10, 2, 2),
    _CdEvDescription_Type()
)
cdEvDescription.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cdEvDescription.setStatus("current")
_ChateauCDProdConformance_ObjectIdentity = ObjectIdentity
chateauCDProdConformance = _ChateauCDProdConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10910, 2, 2, 3, 1, 1, 20)
)
if mibBuilder.loadTexts:
    chateauCDProdConformance.setStatus("current")
_CdConformanceGroups_ObjectIdentity = ObjectIdentity
cdConformanceGroups = _CdConformanceGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10910, 2, 2, 3, 1, 1, 20, 1)
)
if mibBuilder.loadTexts:
    cdConformanceGroups.setStatus("current")

# Managed Objects groups

cdProdConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 10910, 2, 2, 3, 1, 1, 20, 1, 1)
)
cdProdConfigGroup.setObjects(
      *(("CHATEAU-CD-PRODUCT-MIB", "cdStCfgManufacturer"),
        ("CHATEAU-CD-PRODUCT-MIB", "cdStCfgModel"),
        ("CHATEAU-CD-PRODUCT-MIB", "cdStCfgFirmwareRev"),
        ("CHATEAU-CD-PRODUCT-MIB", "cdDynCfgUserAlias"))
)
if mibBuilder.loadTexts:
    cdProdConfigGroup.setStatus("current")

cdProdControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 10910, 2, 2, 3, 1, 1, 20, 1, 2)
)
cdProdControlGroup.setObjects(
      *(("CHATEAU-CD-PRODUCT-MIB", "cdCtlPower"),
        ("CHATEAU-CD-PRODUCT-MIB", "cdCtlTrayDoor"),
        ("CHATEAU-CD-PRODUCT-MIB", "cdCtlPlaying"))
)
if mibBuilder.loadTexts:
    cdProdControlGroup.setStatus("current")

cdProdStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 10910, 2, 2, 3, 1, 1, 20, 1, 3)
)
cdProdStatusGroup.setObjects(
      *(("CHATEAU-CD-PRODUCT-MIB", "cdChStPowerOnHours"),
        ("CHATEAU-CD-PRODUCT-MIB", "cdChStLaserOnHours"),
        ("CHATEAU-CD-PRODUCT-MIB", "cdChStCrcErrorCtr"),
        ("CHATEAU-CD-PRODUCT-MIB", "cdChStTemperature"),
        ("CHATEAU-CD-PRODUCT-MIB", "cdChStPowerSupply"),
        ("CHATEAU-CD-PRODUCT-MIB", "cdChangerNbrCdSlots"),
        ("CHATEAU-CD-PRODUCT-MIB", "cdChangerSlotStatus"),
        ("CHATEAU-CD-PRODUCT-MIB", "cdChangerSlotCDTrackPlaying"),
        ("CHATEAU-CD-PRODUCT-MIB", "cdChangerCDNbrTracks"),
        ("CHATEAU-CD-PRODUCT-MIB", "cdChangerCDTrackPlaying"),
        ("CHATEAU-CD-PRODUCT-MIB", "cdChangerCDTrackLengthSecs"),
        ("CHATEAU-CD-PRODUCT-MIB", "cdChangerCDTrackLengthStr"),
        ("CHATEAU-CD-PRODUCT-MIB", "cdChangerCDTrackTitle"),
        ("CHATEAU-CD-PRODUCT-MIB", "cdChangerCDTrackArtist"))
)
if mibBuilder.loadTexts:
    cdProdStatusGroup.setStatus("current")

cdProdEventGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 10910, 2, 2, 3, 1, 1, 20, 1, 4)
)
cdProdEventGroup.setObjects(
      *(("CHATEAU-CD-PRODUCT-MIB", "cdEvCtlAgtPollFreq"),
        ("CHATEAU-CD-PRODUCT-MIB", "cdChassisTempAlarmThresh"),
        ("CHATEAU-CD-PRODUCT-MIB", "cdChassisTempEvTrapEn"),
        ("CHATEAU-CD-PRODUCT-MIB", "cdPowerSupplyEvTrapEn"),
        ("CHATEAU-CD-PRODUCT-MIB", "cdEvSeverity"),
        ("CHATEAU-CD-PRODUCT-MIB", "cdEvDescription"))
)
if mibBuilder.loadTexts:
    cdProdEventGroup.setStatus("current")


# Notification objects

cdChassisTempAlarmEv = NotificationType(
    (1, 3, 6, 1, 4, 1, 10910, 2, 2, 3, 1, 1, 10, 0, 10)
)
cdChassisTempAlarmEv.setObjects(
      *(("CHATEAU-CD-PRODUCT-MIB", "cdDynCfgUserAlias"),
        ("CHATEAU-CD-PRODUCT-MIB", "cdStCfgModel"),
        ("CHATEAU-CD-PRODUCT-MIB", "cdChStTemperature"),
        ("CHATEAU-CD-PRODUCT-MIB", "cdEvSeverity"),
        ("CHATEAU-CD-PRODUCT-MIB", "cdEvDescription"))
)
if mibBuilder.loadTexts:
    cdChassisTempAlarmEv.setStatus(
        "current"
    )

cdChassisTempOkayEv = NotificationType(
    (1, 3, 6, 1, 4, 1, 10910, 2, 2, 3, 1, 1, 10, 0, 11)
)
cdChassisTempOkayEv.setObjects(
      *(("CHATEAU-CD-PRODUCT-MIB", "cdDynCfgUserAlias"),
        ("CHATEAU-CD-PRODUCT-MIB", "cdStCfgModel"),
        ("CHATEAU-CD-PRODUCT-MIB", "cdChStTemperature"),
        ("CHATEAU-CD-PRODUCT-MIB", "cdEvSeverity"),
        ("CHATEAU-CD-PRODUCT-MIB", "cdEvDescription"))
)
if mibBuilder.loadTexts:
    cdChassisTempOkayEv.setStatus(
        "current"
    )

cdPowerSupplyEv = NotificationType(
    (1, 3, 6, 1, 4, 1, 10910, 2, 2, 3, 1, 1, 10, 0, 20)
)
cdPowerSupplyEv.setObjects(
      *(("CHATEAU-CD-PRODUCT-MIB", "cdDynCfgUserAlias"),
        ("CHATEAU-CD-PRODUCT-MIB", "cdStCfgModel"),
        ("CHATEAU-CD-PRODUCT-MIB", "cdChStPowerSupply"),
        ("CHATEAU-CD-PRODUCT-MIB", "cdEvSeverity"),
        ("CHATEAU-CD-PRODUCT-MIB", "cdEvDescription"))
)
if mibBuilder.loadTexts:
    cdPowerSupplyEv.setStatus(
        "current"
    )


# Notifications groups

cdProdNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 10910, 2, 2, 3, 1, 1, 20, 1, 5)
)
cdProdNotificationsGroup.setObjects(
      *(("CHATEAU-CD-PRODUCT-MIB", "cdChassisTempAlarmEv"),
        ("CHATEAU-CD-PRODUCT-MIB", "cdChassisTempOkayEv"),
        ("CHATEAU-CD-PRODUCT-MIB", "cdPowerSupplyEv"))
)
if mibBuilder.loadTexts:
    cdProdNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

cdCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 10910, 2, 2, 3, 1, 1, 20, 2)
)
if mibBuilder.loadTexts:
    cdCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CHATEAU-CD-PRODUCT-MIB",
    **{"chateauCDProductMIB": chateauCDProductMIB,
       "chateauCDProdConfig": chateauCDProdConfig,
       "cdStaticConfig": cdStaticConfig,
       "cdStCfgManufacturer": cdStCfgManufacturer,
       "cdStCfgModel": cdStCfgModel,
       "cdStCfgFirmwareRev": cdStCfgFirmwareRev,
       "cdDynamicConfig": cdDynamicConfig,
       "cdDynCfgUserAlias": cdDynCfgUserAlias,
       "chateauCDProdControl": chateauCDProdControl,
       "cdCtlPower": cdCtlPower,
       "cdCtlTrayDoor": cdCtlTrayDoor,
       "cdCtlPlaying": cdCtlPlaying,
       "chateauCDProdStatus": chateauCDProdStatus,
       "cdChassisStatus": cdChassisStatus,
       "cdChStPowerOnHours": cdChStPowerOnHours,
       "cdChStLaserOnHours": cdChStLaserOnHours,
       "cdChStCrcErrorCtr": cdChStCrcErrorCtr,
       "cdChStTemperature": cdChStTemperature,
       "cdChStPowerSupply": cdChStPowerSupply,
       "cdChangerStatus": cdChangerStatus,
       "cdChangerNbrCdSlots": cdChangerNbrCdSlots,
       "cdChangerSlotTable": cdChangerSlotTable,
       "cdChangerSlotEntry": cdChangerSlotEntry,
       "cdChangerSlotNbr": cdChangerSlotNbr,
       "cdChangerSlotStatus": cdChangerSlotStatus,
       "cdChangerSlotCDTrackPlaying": cdChangerSlotCDTrackPlaying,
       "cdChangerCDNbrTracks": cdChangerCDNbrTracks,
       "cdChangerCDTrackTable": cdChangerCDTrackTable,
       "cdChangerCDTrackEntry": cdChangerCDTrackEntry,
       "cdChangerCDTrackNbr": cdChangerCDTrackNbr,
       "cdChangerCDTrackPlaying": cdChangerCDTrackPlaying,
       "cdChangerCDTrackLengthSecs": cdChangerCDTrackLengthSecs,
       "cdChangerCDTrackLengthStr": cdChangerCDTrackLengthStr,
       "cdChangerCDTrackTitle": cdChangerCDTrackTitle,
       "cdChangerCDTrackArtist": cdChangerCDTrackArtist,
       "chateauCDProdEvents": chateauCDProdEvents,
       "cdEventList": cdEventList,
       "cdChassisTempAlarmEv": cdChassisTempAlarmEv,
       "cdChassisTempOkayEv": cdChassisTempOkayEv,
       "cdPowerSupplyEv": cdPowerSupplyEv,
       "cdEventControl": cdEventControl,
       "cdEvCtlAgtPollFreq": cdEvCtlAgtPollFreq,
       "cdChassisTempAlarmThresh": cdChassisTempAlarmThresh,
       "cdChassisTempEvTrapEn": cdChassisTempEvTrapEn,
       "cdPowerSupplyEvTrapEn": cdPowerSupplyEvTrapEn,
       "cdEventDescriptors": cdEventDescriptors,
       "cdEvSeverity": cdEvSeverity,
       "cdEvDescription": cdEvDescription,
       "chateauCDProdConformance": chateauCDProdConformance,
       "cdConformanceGroups": cdConformanceGroups,
       "cdProdConfigGroup": cdProdConfigGroup,
       "cdProdControlGroup": cdProdControlGroup,
       "cdProdStatusGroup": cdProdStatusGroup,
       "cdProdEventGroup": cdProdEventGroup,
       "cdProdNotificationsGroup": cdProdNotificationsGroup,
       "cdCompliance": cdCompliance}
)
