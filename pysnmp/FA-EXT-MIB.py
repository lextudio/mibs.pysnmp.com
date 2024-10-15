# SNMP MIB module (FA-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/FA-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:43:40 2024
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

(connUnitPortEntry,) = mibBuilder.importSymbols(
    "FCMGMT-MIB",
    "connUnitPortEntry")

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

(DisplayString,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")

(sw,) = mibBuilder.importSymbols(
    "SW-MIB",
    "sw")


# MODULE-IDENTITY

faExt = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 28)
)
faExt.setRevisions(
        ("2010-11-22 10:30",
         "2013-09-12 10:30",
         "2013-09-24 13:55",
         "2013-10-29 13:54")
)


# Types definitions



class FapwwnType(Integer32):
    """Custom type FapwwnType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 2),
          ("unknown", 1),
          ("userConfigured", 3))
    )




# TEXTUAL-CONVENTIONS



class CiperMode(Integer32, TextualConvention):
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
        *(("allFrames", 2),
          ("fcpAndNonFCP", 3),
          ("none", 1),
          ("onlyFCP", 4))
    )



class EncryptCompressStatus(Integer32, TextualConvention):
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
        *(("disabled", 2),
          ("enabled", 1),
          ("unknown", 3))
    )



# MIB Managed Objects in the order of their OIDs

_SwSfpStatTable_Object = MibTable
swSfpStatTable = _SwSfpStatTable_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 28, 1)
)
if mibBuilder.loadTexts:
    swSfpStatTable.setStatus("current")
_SwSfpStatEntry_Object = MibTableRow
swSfpStatEntry = _SwSfpStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 28, 1, 1)
)
if mibBuilder.loadTexts:
    swSfpStatEntry.setStatus("current")


class _SwSfpTemperature_Type(OctetString):
    """Custom type swSfpTemperature based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_SwSfpTemperature_Type.__name__ = "OctetString"
_SwSfpTemperature_Object = MibTableColumn
swSfpTemperature = _SwSfpTemperature_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 28, 1, 1, 1),
    _SwSfpTemperature_Type()
)
swSfpTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSfpTemperature.setStatus("current")
if mibBuilder.loadTexts:
    swSfpTemperature.setUnits("centigrade")


class _SwSfpVoltage_Type(OctetString):
    """Custom type swSfpVoltage based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_SwSfpVoltage_Type.__name__ = "OctetString"
_SwSfpVoltage_Object = MibTableColumn
swSfpVoltage = _SwSfpVoltage_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 28, 1, 1, 2),
    _SwSfpVoltage_Type()
)
swSfpVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSfpVoltage.setStatus("current")
if mibBuilder.loadTexts:
    swSfpVoltage.setUnits("milli voltage")


class _SwSfpCurrent_Type(OctetString):
    """Custom type swSfpCurrent based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_SwSfpCurrent_Type.__name__ = "OctetString"
_SwSfpCurrent_Object = MibTableColumn
swSfpCurrent = _SwSfpCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 28, 1, 1, 3),
    _SwSfpCurrent_Type()
)
swSfpCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSfpCurrent.setStatus("current")
if mibBuilder.loadTexts:
    swSfpCurrent.setUnits("milli amphere")


class _SwSfpRxPower_Type(OctetString):
    """Custom type swSfpRxPower based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_SwSfpRxPower_Type.__name__ = "OctetString"
_SwSfpRxPower_Object = MibTableColumn
swSfpRxPower = _SwSfpRxPower_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 28, 1, 1, 4),
    _SwSfpRxPower_Type()
)
swSfpRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSfpRxPower.setStatus("current")
if mibBuilder.loadTexts:
    swSfpRxPower.setUnits("dBm")


class _SwSfpTxPower_Type(OctetString):
    """Custom type swSfpTxPower based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_SwSfpTxPower_Type.__name__ = "OctetString"
_SwSfpTxPower_Object = MibTableColumn
swSfpTxPower = _SwSfpTxPower_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 28, 1, 1, 5),
    _SwSfpTxPower_Type()
)
swSfpTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSfpTxPower.setStatus("current")
if mibBuilder.loadTexts:
    swSfpTxPower.setUnits("dBm")
_SwSfpPoweronHrs_Type = Integer32
_SwSfpPoweronHrs_Object = MibTableColumn
swSfpPoweronHrs = _SwSfpPoweronHrs_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 28, 1, 1, 6),
    _SwSfpPoweronHrs_Type()
)
swSfpPoweronHrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSfpPoweronHrs.setStatus("current")
if mibBuilder.loadTexts:
    swSfpPoweronHrs.setUnits("hours")
_SwSfpUnitId_Type = Integer32
_SwSfpUnitId_Object = MibTableColumn
swSfpUnitId = _SwSfpUnitId_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 28, 1, 1, 7),
    _SwSfpUnitId_Type()
)
swSfpUnitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSfpUnitId.setStatus("current")
_SwFapwwnFeature_ObjectIdentity = ObjectIdentity
swFapwwnFeature = _SwFapwwnFeature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 28, 2)
)
if mibBuilder.loadTexts:
    swFapwwnFeature.setStatus("current")
_SwPortFapwwnConfigTable_Object = MibTable
swPortFapwwnConfigTable = _SwPortFapwwnConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 28, 2, 1)
)
if mibBuilder.loadTexts:
    swPortFapwwnConfigTable.setStatus("current")
_SwPortFapwwnConfigEntry_Object = MibTableRow
swPortFapwwnConfigEntry = _SwPortFapwwnConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 28, 2, 1, 1)
)
if mibBuilder.loadTexts:
    swPortFapwwnConfigEntry.setStatus("current")
_SwPortFapwwnConfigEnable_Type = TruthValue
_SwPortFapwwnConfigEnable_Object = MibTableColumn
swPortFapwwnConfigEnable = _SwPortFapwwnConfigEnable_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 28, 2, 1, 1, 1),
    _SwPortFapwwnConfigEnable_Type()
)
swPortFapwwnConfigEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortFapwwnConfigEnable.setStatus("current")


class _SwPortFapwwnConfigFapwwn_Type(DisplayString):
    """Custom type swPortFapwwnConfigFapwwn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(256, 256),
    )


_SwPortFapwwnConfigFapwwn_Type.__name__ = "DisplayString"
_SwPortFapwwnConfigFapwwn_Object = MibTableColumn
swPortFapwwnConfigFapwwn = _SwPortFapwwnConfigFapwwn_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 28, 2, 1, 1, 2),
    _SwPortFapwwnConfigFapwwn_Type()
)
swPortFapwwnConfigFapwwn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortFapwwnConfigFapwwn.setStatus("current")
_SwPortFapwwnConfigType_Type = FapwwnType
_SwPortFapwwnConfigType_Object = MibTableColumn
swPortFapwwnConfigType = _SwPortFapwwnConfigType_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 28, 2, 1, 1, 3),
    _SwPortFapwwnConfigType_Type()
)
swPortFapwwnConfigType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortFapwwnConfigType.setStatus("current")
_SwPortConfigTable_Object = MibTable
swPortConfigTable = _SwPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 28, 3)
)
if mibBuilder.loadTexts:
    swPortConfigTable.setStatus("current")
_SwPortConfigEntry_Object = MibTableRow
swPortConfigEntry = _SwPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 28, 3, 1)
)
if mibBuilder.loadTexts:
    swPortConfigEntry.setStatus("current")
_SwPortEncrypt_Type = EncryptCompressStatus
_SwPortEncrypt_Object = MibTableColumn
swPortEncrypt = _SwPortEncrypt_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 28, 3, 1, 1),
    _SwPortEncrypt_Type()
)
swPortEncrypt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortEncrypt.setStatus("current")
_SwPortCompression_Type = EncryptCompressStatus
_SwPortCompression_Object = MibTableColumn
swPortCompression = _SwPortCompression_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 28, 3, 1, 2),
    _SwPortCompression_Type()
)
swPortCompression.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortCompression.setStatus("current")


class _SwPortCipherKeySize_Type(Integer32):
    """Custom type swPortCipherKeySize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwPortCipherKeySize_Type.__name__ = "Integer32"
_SwPortCipherKeySize_Object = MibTableColumn
swPortCipherKeySize = _SwPortCipherKeySize_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 28, 3, 1, 3),
    _SwPortCipherKeySize_Type()
)
swPortCipherKeySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortCipherKeySize.setStatus("current")
_SwPortCipherMode_Type = CiperMode
_SwPortCipherMode_Object = MibTableColumn
swPortCipherMode = _SwPortCipherMode_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 28, 3, 1, 4),
    _SwPortCipherMode_Type()
)
swPortCipherMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortCipherMode.setStatus("current")
_SwConnUnitPortTable_Object = MibTable
swConnUnitPortTable = _SwConnUnitPortTable_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 28, 4)
)
if mibBuilder.loadTexts:
    swConnUnitPortTable.setStatus("current")
_SwConnUnitPortEntry_Object = MibTableRow
swConnUnitPortEntry = _SwConnUnitPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 28, 4, 1)
)
if mibBuilder.loadTexts:
    swConnUnitPortEntry.setStatus("current")
_SwConnUnitPortCapableSpeeds_Type = OctetString
_SwConnUnitPortCapableSpeeds_Object = MibTableColumn
swConnUnitPortCapableSpeeds = _SwConnUnitPortCapableSpeeds_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 28, 4, 1, 1),
    _SwConnUnitPortCapableSpeeds_Type()
)
swConnUnitPortCapableSpeeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swConnUnitPortCapableSpeeds.setStatus("current")


class _SwConnUnitPortSpeedMode_Type(Integer32):
    """Custom type swConnUnitPortSpeedMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto-neg", 1),
          ("static", 2))
    )


_SwConnUnitPortSpeedMode_Type.__name__ = "Integer32"
_SwConnUnitPortSpeedMode_Object = MibTableColumn
swConnUnitPortSpeedMode = _SwConnUnitPortSpeedMode_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 28, 4, 1, 2),
    _SwConnUnitPortSpeedMode_Type()
)
swConnUnitPortSpeedMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swConnUnitPortSpeedMode.setStatus("current")


class _SwConnUnitPortFECMode_Type(Integer32):
    """Custom type swConnUnitPortFECMode based on Integer32"""
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
        *(("disabled", 2),
          ("enabled", 3),
          ("notsupported", 4),
          ("unknown", 1))
    )


_SwConnUnitPortFECMode_Type.__name__ = "Integer32"
_SwConnUnitPortFECMode_Object = MibTableColumn
swConnUnitPortFECMode = _SwConnUnitPortFECMode_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 28, 4, 1, 3),
    _SwConnUnitPortFECMode_Type()
)
swConnUnitPortFECMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swConnUnitPortFECMode.setStatus("current")


class _SwConnUnitPortFECState_Type(Integer32):
    """Custom type swConnUnitPortFECState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2),
          ("notsupported", 3),
          ("unknown", 0))
    )


_SwConnUnitPortFECState_Type.__name__ = "Integer32"
_SwConnUnitPortFECState_Object = MibTableColumn
swConnUnitPortFECState = _SwConnUnitPortFECState_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 28, 4, 1, 4),
    _SwConnUnitPortFECState_Type()
)
swConnUnitPortFECState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swConnUnitPortFECState.setStatus("current")
connUnitPortEntry.registerAugmentions(
    ("FA-EXT-MIB",
     "swSfpStatEntry")
)
swSfpStatEntry.setIndexNames(*connUnitPortEntry.getIndexNames())
connUnitPortEntry.registerAugmentions(
    ("FA-EXT-MIB",
     "swPortFapwwnConfigEntry")
)
swPortFapwwnConfigEntry.setIndexNames(*connUnitPortEntry.getIndexNames())
connUnitPortEntry.registerAugmentions(
    ("FA-EXT-MIB",
     "swPortConfigEntry")
)
swPortConfigEntry.setIndexNames(*connUnitPortEntry.getIndexNames())
connUnitPortEntry.registerAugmentions(
    ("FA-EXT-MIB",
     "swConnUnitPortEntry")
)
swConnUnitPortEntry.setIndexNames(*connUnitPortEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FA-EXT-MIB",
    **{"FapwwnType": FapwwnType,
       "CiperMode": CiperMode,
       "EncryptCompressStatus": EncryptCompressStatus,
       "faExt": faExt,
       "swSfpStatTable": swSfpStatTable,
       "swSfpStatEntry": swSfpStatEntry,
       "swSfpTemperature": swSfpTemperature,
       "swSfpVoltage": swSfpVoltage,
       "swSfpCurrent": swSfpCurrent,
       "swSfpRxPower": swSfpRxPower,
       "swSfpTxPower": swSfpTxPower,
       "swSfpPoweronHrs": swSfpPoweronHrs,
       "swSfpUnitId": swSfpUnitId,
       "swFapwwnFeature": swFapwwnFeature,
       "swPortFapwwnConfigTable": swPortFapwwnConfigTable,
       "swPortFapwwnConfigEntry": swPortFapwwnConfigEntry,
       "swPortFapwwnConfigEnable": swPortFapwwnConfigEnable,
       "swPortFapwwnConfigFapwwn": swPortFapwwnConfigFapwwn,
       "swPortFapwwnConfigType": swPortFapwwnConfigType,
       "swPortConfigTable": swPortConfigTable,
       "swPortConfigEntry": swPortConfigEntry,
       "swPortEncrypt": swPortEncrypt,
       "swPortCompression": swPortCompression,
       "swPortCipherKeySize": swPortCipherKeySize,
       "swPortCipherMode": swPortCipherMode,
       "swConnUnitPortTable": swConnUnitPortTable,
       "swConnUnitPortEntry": swConnUnitPortEntry,
       "swConnUnitPortCapableSpeeds": swConnUnitPortCapableSpeeds,
       "swConnUnitPortSpeedMode": swConnUnitPortSpeedMode,
       "swConnUnitPortFECMode": swConnUnitPortFECMode,
       "swConnUnitPortFECState": swConnUnitPortFECState}
)
