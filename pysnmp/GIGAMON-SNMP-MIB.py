# SNMP MIB module (GIGAMON-SNMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/GIGAMON-SNMP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:48:39 2024
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
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(sysLocation,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysLocation")

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
 PhysAddress,
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

gigamonSnmp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 26866)
)
gigamonSnmp.setRevisions(
        ("2013-09-25 00:00",
         "2013-08-09 00:00",
         "2013-04-15 00:00",
         "2012-12-04 00:00",
         "2012-05-09 00:00",
         "2012-05-09 00:00",
         "2012-03-27 00:00",
         "2011-03-25 00:00",
         "2011-03-24 00:00",
         "2011-03-03 00:00",
         "2010-07-10 10:00",
         "2010-07-10 10:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_GigamonSnmpNotifications_ObjectIdentity = ObjectIdentity
gigamonSnmpNotifications = _GigamonSnmpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26866, 1)
)
_GigamonGigaVUE_ObjectIdentity = ObjectIdentity
gigamonGigaVUE = _GigamonGigaVUE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26866, 1, 1)
)
_GigamonSnmpNotificationObjects_ObjectIdentity = ObjectIdentity
gigamonSnmpNotificationObjects = _GigamonSnmpNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26866, 1, 2)
)


class _GigamonSnmpNotifLevel_Type(Integer32):
    """Custom type gigamonSnmpNotifLevel based on Integer32"""
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
        *(("critical", 4),
          ("information", 1),
          ("major", 3),
          ("minor", 2))
    )


_GigamonSnmpNotifLevel_Type.__name__ = "Integer32"
_GigamonSnmpNotifLevel_Object = MibScalar
gigamonSnmpNotifLevel = _GigamonSnmpNotifLevel_Object(
    (1, 3, 6, 1, 4, 1, 26866, 1, 2, 1),
    _GigamonSnmpNotifLevel_Type()
)
gigamonSnmpNotifLevel.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    gigamonSnmpNotifLevel.setStatus("current")
_GigamonSnmpNotifDescription_Type = OctetString
_GigamonSnmpNotifDescription_Object = MibScalar
gigamonSnmpNotifDescription = _GigamonSnmpNotifDescription_Object(
    (1, 3, 6, 1, 4, 1, 26866, 1, 2, 2),
    _GigamonSnmpNotifDescription_Type()
)
gigamonSnmpNotifDescription.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    gigamonSnmpNotifDescription.setStatus("current")


class _GigamonSnmpNotifOpType_Type(Integer32):
    """Custom type gigamonSnmpNotifOpType based on Integer32"""
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
        *(("change", 5),
          ("delete", 3),
          ("read", 1),
          ("validate", 4),
          ("write", 2))
    )


_GigamonSnmpNotifOpType_Type.__name__ = "Integer32"
_GigamonSnmpNotifOpType_Object = MibScalar
gigamonSnmpNotifOpType = _GigamonSnmpNotifOpType_Object(
    (1, 3, 6, 1, 4, 1, 26866, 1, 2, 3),
    _GigamonSnmpNotifOpType_Type()
)
gigamonSnmpNotifOpType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    gigamonSnmpNotifOpType.setStatus("current")
_GigamonSnmpNotifPortName_Type = OctetString
_GigamonSnmpNotifPortName_Object = MibScalar
gigamonSnmpNotifPortName = _GigamonSnmpNotifPortName_Object(
    (1, 3, 6, 1, 4, 1, 26866, 1, 2, 4),
    _GigamonSnmpNotifPortName_Type()
)
gigamonSnmpNotifPortName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    gigamonSnmpNotifPortName.setStatus("current")


class _GigamonSnmpNotifPortLinkStatus_Type(Integer32):
    """Custom type gigamonSnmpNotifPortLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("up", 1))
    )


_GigamonSnmpNotifPortLinkStatus_Type.__name__ = "Integer32"
_GigamonSnmpNotifPortLinkStatus_Object = MibScalar
gigamonSnmpNotifPortLinkStatus = _GigamonSnmpNotifPortLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 26866, 1, 2, 5),
    _GigamonSnmpNotifPortLinkStatus_Type()
)
gigamonSnmpNotifPortLinkStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    gigamonSnmpNotifPortLinkStatus.setStatus("current")


class _GigamonSnmpNotifTAPRelayStatus_Type(Integer32):
    """Custom type gigamonSnmpNotifTAPRelayStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("none", 0),
          ("passive", 1))
    )


_GigamonSnmpNotifTAPRelayStatus_Type.__name__ = "Integer32"
_GigamonSnmpNotifTAPRelayStatus_Object = MibScalar
gigamonSnmpNotifTAPRelayStatus = _GigamonSnmpNotifTAPRelayStatus_Object(
    (1, 3, 6, 1, 4, 1, 26866, 1, 2, 6),
    _GigamonSnmpNotifTAPRelayStatus_Type()
)
gigamonSnmpNotifTAPRelayStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    gigamonSnmpNotifTAPRelayStatus.setStatus("current")


class _GigamonSnmpNotifRxTxType_Type(Integer32):
    """Custom type gigamonSnmpNotifRxTxType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("rx", 0),
          ("tx", 1))
    )


_GigamonSnmpNotifRxTxType_Type.__name__ = "Integer32"
_GigamonSnmpNotifRxTxType_Object = MibScalar
gigamonSnmpNotifRxTxType = _GigamonSnmpNotifRxTxType_Object(
    (1, 3, 6, 1, 4, 1, 26866, 1, 2, 7),
    _GigamonSnmpNotifRxTxType_Type()
)
gigamonSnmpNotifRxTxType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    gigamonSnmpNotifRxTxType.setStatus("current")


class _GigamonSnmpNotifRxTxErrorType_Type(Integer32):
    """Custom type gigamonSnmpNotifRxTxErrorType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("crc-align", 4),
          ("fragments", 1),
          ("jabbers", 3),
          ("obsolete", 2),
          ("under-size", 0),
          ("unknown", 5))
    )


_GigamonSnmpNotifRxTxErrorType_Type.__name__ = "Integer32"
_GigamonSnmpNotifRxTxErrorType_Object = MibScalar
gigamonSnmpNotifRxTxErrorType = _GigamonSnmpNotifRxTxErrorType_Object(
    (1, 3, 6, 1, 4, 1, 26866, 1, 2, 8),
    _GigamonSnmpNotifRxTxErrorType_Type()
)
gigamonSnmpNotifRxTxErrorType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    gigamonSnmpNotifRxTxErrorType.setStatus("current")
_GigamonSnmpNotifCounter_Type = Integer32
_GigamonSnmpNotifCounter_Object = MibScalar
gigamonSnmpNotifCounter = _GigamonSnmpNotifCounter_Object(
    (1, 3, 6, 1, 4, 1, 26866, 1, 2, 9),
    _GigamonSnmpNotifCounter_Type()
)
gigamonSnmpNotifCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    gigamonSnmpNotifCounter.setStatus("current")
_GigamonSnmpNotifFirmwareName_Type = OctetString
_GigamonSnmpNotifFirmwareName_Object = MibScalar
gigamonSnmpNotifFirmwareName = _GigamonSnmpNotifFirmwareName_Object(
    (1, 3, 6, 1, 4, 1, 26866, 1, 2, 10),
    _GigamonSnmpNotifFirmwareName_Type()
)
gigamonSnmpNotifFirmwareName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    gigamonSnmpNotifFirmwareName.setStatus("current")


class _GigamonSnmpNotifModuleOperationType_Type(Integer32):
    """Custom type gigamonSnmpNotifModuleOperationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("changed", 2),
          ("inserted", 1),
          ("license-mismatch", 6),
          ("mismatch", 3),
          ("removed", 0),
          ("shutdown", 4),
          ("up", 5))
    )


_GigamonSnmpNotifModuleOperationType_Type.__name__ = "Integer32"
_GigamonSnmpNotifModuleOperationType_Object = MibScalar
gigamonSnmpNotifModuleOperationType = _GigamonSnmpNotifModuleOperationType_Object(
    (1, 3, 6, 1, 4, 1, 26866, 1, 2, 11),
    _GigamonSnmpNotifModuleOperationType_Type()
)
gigamonSnmpNotifModuleOperationType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    gigamonSnmpNotifModuleOperationType.setStatus("current")
_GigamonSnmpNotifModuleName_Type = OctetString
_GigamonSnmpNotifModuleName_Object = MibScalar
gigamonSnmpNotifModuleName = _GigamonSnmpNotifModuleName_Object(
    (1, 3, 6, 1, 4, 1, 26866, 1, 2, 12),
    _GigamonSnmpNotifModuleName_Type()
)
gigamonSnmpNotifModuleName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    gigamonSnmpNotifModuleName.setStatus("current")


class _GigamonNotifSlotNumber_Type(Integer32):
    """Custom type gigamonNotifSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              10,
              11,
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("daughter-Card", 5),
          ("gigaLink-Back", 4),
          ("mid-plane", 0),
          ("slot-1", 1),
          ("slot-2", 2),
          ("slot-3", 3),
          ("slot-4", 10),
          ("slot-5", 11),
          ("slot-6", 12),
          ("slot-7", 13),
          ("slot-8", 14),
          ("slot-CC1", 15),
          ("slot-CC2", 16))
    )


_GigamonNotifSlotNumber_Type.__name__ = "Integer32"
_GigamonNotifSlotNumber_Object = MibScalar
gigamonNotifSlotNumber = _GigamonNotifSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 26866, 1, 2, 13),
    _GigamonNotifSlotNumber_Type()
)
gigamonNotifSlotNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    gigamonNotifSlotNumber.setStatus("current")
_GigamonSnmpNotifUserName_Type = OctetString
_GigamonSnmpNotifUserName_Object = MibScalar
gigamonSnmpNotifUserName = _GigamonSnmpNotifUserName_Object(
    (1, 3, 6, 1, 4, 1, 26866, 1, 2, 14),
    _GigamonSnmpNotifUserName_Type()
)
gigamonSnmpNotifUserName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    gigamonSnmpNotifUserName.setStatus("current")
_GigamonSnmpNotifFileName_Type = OctetString
_GigamonSnmpNotifFileName_Object = MibScalar
gigamonSnmpNotifFileName = _GigamonSnmpNotifFileName_Object(
    (1, 3, 6, 1, 4, 1, 26866, 1, 2, 15),
    _GigamonSnmpNotifFileName_Type()
)
gigamonSnmpNotifFileName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    gigamonSnmpNotifFileName.setStatus("current")


class _GigamonNotifPowerStatus_Type(Integer32):
    """Custom type gigamonNotifPowerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("abnormal", 0),
          ("failure", -1),
          ("normal", 1))
    )


_GigamonNotifPowerStatus_Type.__name__ = "Integer32"
_GigamonNotifPowerStatus_Object = MibScalar
gigamonNotifPowerStatus = _GigamonNotifPowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 26866, 1, 2, 16),
    _GigamonNotifPowerStatus_Type()
)
gigamonNotifPowerStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    gigamonNotifPowerStatus.setStatus("current")
_GigamonSnmpNotifHardWareName_Type = OctetString
_GigamonSnmpNotifHardWareName_Object = MibScalar
gigamonSnmpNotifHardWareName = _GigamonSnmpNotifHardWareName_Object(
    (1, 3, 6, 1, 4, 1, 26866, 1, 2, 17),
    _GigamonSnmpNotifHardWareName_Type()
)
gigamonSnmpNotifHardWareName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    gigamonSnmpNotifHardWareName.setStatus("current")


class _GigamonSnmpNotifGigaVUE420SlotNumber_Type(Integer32):
    """Custom type gigamonSnmpNotifGigaVUE420SlotNumber based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("expansion-slot-1", 1),
          ("expansion-slot-2", 2),
          ("expansion-slot-3", 3),
          ("expansion-slot-4", 4),
          ("expansion-slot-5", 5),
          ("mid-plane", 0),
          ("x1-slot", 6),
          ("x2-slot", 7),
          ("x3-slot", 8),
          ("x4-slot", 9))
    )


_GigamonSnmpNotifGigaVUE420SlotNumber_Type.__name__ = "Integer32"
_GigamonSnmpNotifGigaVUE420SlotNumber_Object = MibScalar
gigamonSnmpNotifGigaVUE420SlotNumber = _GigamonSnmpNotifGigaVUE420SlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 26866, 1, 2, 18),
    _GigamonSnmpNotifGigaVUE420SlotNumber_Type()
)
gigamonSnmpNotifGigaVUE420SlotNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    gigamonSnmpNotifGigaVUE420SlotNumber.setStatus("current")
_GigamonSnmpNotifFanName_Type = OctetString
_GigamonSnmpNotifFanName_Object = MibScalar
gigamonSnmpNotifFanName = _GigamonSnmpNotifFanName_Object(
    (1, 3, 6, 1, 4, 1, 26866, 1, 2, 19),
    _GigamonSnmpNotifFanName_Type()
)
gigamonSnmpNotifFanName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    gigamonSnmpNotifFanName.setStatus("current")


class _GigamonNotifFanStatus_Type(Integer32):
    """Custom type gigamonNotifFanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("abnormal", 0),
          ("failure", -1),
          ("normal", 1))
    )


_GigamonNotifFanStatus_Type.__name__ = "Integer32"
_GigamonNotifFanStatus_Object = MibScalar
gigamonNotifFanStatus = _GigamonNotifFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 26866, 1, 2, 20),
    _GigamonNotifFanStatus_Type()
)
gigamonNotifFanStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    gigamonNotifFanStatus.setStatus("current")


class _GigamonSnmpNotifUtilizationAlarm_Type(Integer32):
    """Custom type gigamonSnmpNotifUtilizationAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("below", 0),
          ("exceed", 1))
    )


_GigamonSnmpNotifUtilizationAlarm_Type.__name__ = "Integer32"
_GigamonSnmpNotifUtilizationAlarm_Object = MibScalar
gigamonSnmpNotifUtilizationAlarm = _GigamonSnmpNotifUtilizationAlarm_Object(
    (1, 3, 6, 1, 4, 1, 26866, 1, 2, 21),
    _GigamonSnmpNotifUtilizationAlarm_Type()
)
gigamonSnmpNotifUtilizationAlarm.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    gigamonSnmpNotifUtilizationAlarm.setStatus("current")
_GigamonSnmpNotifUtilizationThreshold_Type = Integer32
_GigamonSnmpNotifUtilizationThreshold_Object = MibScalar
gigamonSnmpNotifUtilizationThreshold = _GigamonSnmpNotifUtilizationThreshold_Object(
    (1, 3, 6, 1, 4, 1, 26866, 1, 2, 22),
    _GigamonSnmpNotifUtilizationThreshold_Type()
)
gigamonSnmpNotifUtilizationThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    gigamonSnmpNotifUtilizationThreshold.setStatus("current")


class _GigamonSnmpBatteryLevel_Type(Integer32):
    """Custom type gigamonSnmpBatteryLevel based on Integer32"""
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
        *(("batteryChargeComplete", 0),
          ("downBelow25", 3),
          ("downBelow50", 2),
          ("downBelow75", 1),
          ("shutDownSystem", 4))
    )


_GigamonSnmpBatteryLevel_Type.__name__ = "Integer32"
_GigamonSnmpBatteryLevel_Object = MibScalar
gigamonSnmpBatteryLevel = _GigamonSnmpBatteryLevel_Object(
    (1, 3, 6, 1, 4, 1, 26866, 1, 2, 23),
    _GigamonSnmpBatteryLevel_Type()
)
gigamonSnmpBatteryLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigamonSnmpBatteryLevel.setStatus("current")


class _GigamonSnmpPortLinkSpeed_Type(Integer32):
    """Custom type gigamonSnmpPortLinkSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("notApply", 0),
          ("speed10", 1),
          ("speed100", 2),
          ("speed1000", 3),
          ("speed10000", 4),
          ("speed100000", 6),
          ("speed40000", 5))
    )


_GigamonSnmpPortLinkSpeed_Type.__name__ = "Integer32"
_GigamonSnmpPortLinkSpeed_Object = MibScalar
gigamonSnmpPortLinkSpeed = _GigamonSnmpPortLinkSpeed_Object(
    (1, 3, 6, 1, 4, 1, 26866, 1, 2, 24),
    _GigamonSnmpPortLinkSpeed_Type()
)
gigamonSnmpPortLinkSpeed.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    gigamonSnmpPortLinkSpeed.setStatus("current")


class _GigamonSnmpPortLinkDuplex_Type(Integer32):
    """Custom type gigamonSnmpPortLinkDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("full", 1),
          ("half", 2),
          ("notApply", 0))
    )


_GigamonSnmpPortLinkDuplex_Type.__name__ = "Integer32"
_GigamonSnmpPortLinkDuplex_Object = MibScalar
gigamonSnmpPortLinkDuplex = _GigamonSnmpPortLinkDuplex_Object(
    (1, 3, 6, 1, 4, 1, 26866, 1, 2, 25),
    _GigamonSnmpPortLinkDuplex_Type()
)
gigamonSnmpPortLinkDuplex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    gigamonSnmpPortLinkDuplex.setStatus("current")
_GigamonSnmpNotifCpuIndex_Type = Unsigned32
_GigamonSnmpNotifCpuIndex_Object = MibScalar
gigamonSnmpNotifCpuIndex = _GigamonSnmpNotifCpuIndex_Object(
    (1, 3, 6, 1, 4, 1, 26866, 1, 2, 26),
    _GigamonSnmpNotifCpuIndex_Type()
)
gigamonSnmpNotifCpuIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    gigamonSnmpNotifCpuIndex.setStatus("current")
_GigamonSnmpNotifFsMountPoint_Type = OctetString
_GigamonSnmpNotifFsMountPoint_Object = MibScalar
gigamonSnmpNotifFsMountPoint = _GigamonSnmpNotifFsMountPoint_Object(
    (1, 3, 6, 1, 4, 1, 26866, 1, 2, 27),
    _GigamonSnmpNotifFsMountPoint_Type()
)
gigamonSnmpNotifFsMountPoint.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    gigamonSnmpNotifFsMountPoint.setStatus("current")


class _GigamonSnmpPowerSource_Type(Integer32):
    """Custom type gigamonSnmpPowerSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mainPower", 0),
          ("poe", 1),
          ("power48V", 2))
    )


_GigamonSnmpPowerSource_Type.__name__ = "Integer32"
_GigamonSnmpPowerSource_Object = MibScalar
gigamonSnmpPowerSource = _GigamonSnmpPowerSource_Object(
    (1, 3, 6, 1, 4, 1, 26866, 1, 2, 28),
    _GigamonSnmpPowerSource_Type()
)
gigamonSnmpPowerSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigamonSnmpPowerSource.setStatus("current")
_GigamonSnmpNotifBpsUnitName_Type = OctetString
_GigamonSnmpNotifBpsUnitName_Object = MibScalar
gigamonSnmpNotifBpsUnitName = _GigamonSnmpNotifBpsUnitName_Object(
    (1, 3, 6, 1, 4, 1, 26866, 1, 2, 29),
    _GigamonSnmpNotifBpsUnitName_Type()
)
gigamonSnmpNotifBpsUnitName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    gigamonSnmpNotifBpsUnitName.setStatus("current")


class _GigamonSnmpNotifBpsFailoverStatus_Type(Integer32):
    """Custom type gigamonSnmpNotifBpsFailoverStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("primary", 0),
          ("secondary", 1))
    )


_GigamonSnmpNotifBpsFailoverStatus_Type.__name__ = "Integer32"
_GigamonSnmpNotifBpsFailoverStatus_Object = MibScalar
gigamonSnmpNotifBpsFailoverStatus = _GigamonSnmpNotifBpsFailoverStatus_Object(
    (1, 3, 6, 1, 4, 1, 26866, 1, 2, 30),
    _GigamonSnmpNotifBpsFailoverStatus_Type()
)
gigamonSnmpNotifBpsFailoverStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    gigamonSnmpNotifBpsFailoverStatus.setStatus("current")
_GigamonSystem_ObjectIdentity = ObjectIdentity
gigamonSystem = _GigamonSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26866, 2)
)
_Manufacturer_Type = OctetString
_Manufacturer_Object = MibScalar
manufacturer = _Manufacturer_Object(
    (1, 3, 6, 1, 4, 1, 26866, 2, 1),
    _Manufacturer_Type()
)
manufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    manufacturer.setStatus("current")
_Model_Type = OctetString
_Model_Object = MibScalar
model = _Model_Object(
    (1, 3, 6, 1, 4, 1, 26866, 2, 2),
    _Model_Type()
)
model.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    model.setStatus("current")
_Name_Type = OctetString
_Name_Object = MibScalar
name = _Name_Object(
    (1, 3, 6, 1, 4, 1, 26866, 2, 3),
    _Name_Type()
)
name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    name.setStatus("current")
_SerialNumber_Type = OctetString
_SerialNumber_Object = MibScalar
serialNumber = _SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 26866, 2, 4),
    _SerialNumber_Type()
)
serialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialNumber.setStatus("current")
_SystemDescription_Type = OctetString
_SystemDescription_Object = MibScalar
systemDescription = _SystemDescription_Object(
    (1, 3, 6, 1, 4, 1, 26866, 2, 5),
    _SystemDescription_Type()
)
systemDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemDescription.setStatus("current")
_Version_Type = OctetString
_Version_Object = MibScalar
version = _Version_Object(
    (1, 3, 6, 1, 4, 1, 26866, 2, 6),
    _Version_Type()
)
version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    version.setStatus("current")
_ChassisModelNumber_Type = OctetString
_ChassisModelNumber_Object = MibScalar
chassisModelNumber = _ChassisModelNumber_Object(
    (1, 3, 6, 1, 4, 1, 26866, 2, 7),
    _ChassisModelNumber_Type()
)
chassisModelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisModelNumber.setStatus("current")
_ChassisSerialNumber_Type = OctetString
_ChassisSerialNumber_Object = MibScalar
chassisSerialNumber = _ChassisSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 26866, 2, 8),
    _ChassisSerialNumber_Type()
)
chassisSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisSerialNumber.setStatus("current")
_BladeSerialNumbers_Type = OctetString
_BladeSerialNumbers_Object = MibScalar
bladeSerialNumbers = _BladeSerialNumbers_Object(
    (1, 3, 6, 1, 4, 1, 26866, 2, 9),
    _BladeSerialNumbers_Type()
)
bladeSerialNumbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeSerialNumbers.setStatus("current")
_FirmwareVersion_Type = OctetString
_FirmwareVersion_Object = MibScalar
firmwareVersion = _FirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 26866, 2, 10),
    _FirmwareVersion_Type()
)
firmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmwareVersion.setStatus("current")
_HardwareVersion_Type = OctetString
_HardwareVersion_Object = MibScalar
hardwareVersion = _HardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 26866, 2, 11),
    _HardwareVersion_Type()
)
hardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardwareVersion.setStatus("current")
_CpuRAMSize_Type = OctetString
_CpuRAMSize_Object = MibScalar
cpuRAMSize = _CpuRAMSize_Object(
    (1, 3, 6, 1, 4, 1, 26866, 2, 12),
    _CpuRAMSize_Type()
)
cpuRAMSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuRAMSize.setStatus("current")
_CpuUtilization_Type = OctetString
_CpuUtilization_Object = MibScalar
cpuUtilization = _CpuUtilization_Object(
    (1, 3, 6, 1, 4, 1, 26866, 2, 13),
    _CpuUtilization_Type()
)
cpuUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuUtilization.setStatus("current")
_Fans_Type = OctetString
_Fans_Object = MibScalar
fans = _Fans_Object(
    (1, 3, 6, 1, 4, 1, 26866, 2, 14),
    _Fans_Type()
)
fans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fans.setStatus("current")
_TemperatureSensors_Type = OctetString
_TemperatureSensors_Object = MibScalar
temperatureSensors = _TemperatureSensors_Object(
    (1, 3, 6, 1, 4, 1, 26866, 2, 15),
    _TemperatureSensors_Type()
)
temperatureSensors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureSensors.setStatus("current")
_PowerSupply_Type = OctetString
_PowerSupply_Object = MibScalar
powerSupply = _PowerSupply_Object(
    (1, 3, 6, 1, 4, 1, 26866, 2, 16),
    _PowerSupply_Type()
)
powerSupply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupply.setStatus("current")
_GigamonProducts_ObjectIdentity = ObjectIdentity
gigamonProducts = _GigamonProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26866, 3)
)
_GigamonGV2404_ObjectIdentity = ObjectIdentity
gigamonGV2404 = _GigamonGV2404_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26866, 3, 1)
)
_GigamonGV420_ObjectIdentity = ObjectIdentity
gigamonGV420 = _GigamonGV420_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26866, 3, 2)
)
_GigamonGV212_ObjectIdentity = ObjectIdentity
gigamonGV212 = _GigamonGV212_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26866, 3, 3)
)
_GigamonGV216_ObjectIdentity = ObjectIdentity
gigamonGV216 = _GigamonGV216_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26866, 3, 4)
)

# Managed Objects groups


# Notification objects

gigamonSnmpResetSystemNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 26866, 1, 1, 1)
)
gigamonSnmpResetSystemNotification.setObjects(
      *(("GIGAMON-SNMP-MIB", "gigamonSnmpNotifHardWareName"),
        ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifLevel"),
        ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifDescription"))
)
if mibBuilder.loadTexts:
    gigamonSnmpResetSystemNotification.setStatus(
        "current"
    )

gigamonSnmpUserAuthFailNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 26866, 1, 1, 2)
)
gigamonSnmpUserAuthFailNotification.setObjects(
      *(("GIGAMON-SNMP-MIB", "gigamonSnmpNotifHardWareName"),
        ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifLevel"),
        ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifDescription"),
        ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifUserName"))
)
if mibBuilder.loadTexts:
    gigamonSnmpUserAuthFailNotification.setStatus(
        "current"
    )

gigamonSnmpFirmwareChangeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 26866, 1, 1, 3)
)
gigamonSnmpFirmwareChangeNotification.setObjects(
      *(("GIGAMON-SNMP-MIB", "gigamonSnmpNotifHardWareName"),
        ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifLevel"),
        ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifDescription"),
        ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifFirmwareName"))
)
if mibBuilder.loadTexts:
    gigamonSnmpFirmwareChangeNotification.setStatus(
        "current"
    )

gigamonSnmpConfigSaveNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 26866, 1, 1, 4)
)
gigamonSnmpConfigSaveNotification.setObjects(
      *(("GIGAMON-SNMP-MIB", "gigamonSnmpNotifHardWareName"),
        ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifLevel"),
        ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifDescription"),
        ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifFileName"))
)
if mibBuilder.loadTexts:
    gigamonSnmpConfigSaveNotification.setStatus(
        "current"
    )

gigamonSnmpModuleChangeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 26866, 1, 1, 5)
)
gigamonSnmpModuleChangeNotification.setObjects(
      *(("GIGAMON-SNMP-MIB", "gigamonSnmpNotifHardWareName"),
        ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifLevel"),
        ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifDescription"),
        ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifModuleOperationType"),
        ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifModuleName"),
        ("GIGAMON-SNMP-MIB", "gigamonNotifSlotNumber"))
)
if mibBuilder.loadTexts:
    gigamonSnmpModuleChangeNotification.setStatus(
        "current"
    )

gigamonSnmpPacketDropNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 26866, 1, 1, 6)
)
gigamonSnmpPacketDropNotification.setObjects(
      *(("GIGAMON-SNMP-MIB", "gigamonSnmpNotifHardWareName"),
        ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifLevel"),
        ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifDescription"),
        ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifPortName"),
        ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifCounter"))
)
if mibBuilder.loadTexts:
    gigamonSnmpPacketDropNotification.setStatus(
        "current"
    )

gigamonSnmpTapRelayChangeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 26866, 1, 1, 7)
)
gigamonSnmpTapRelayChangeNotification.setObjects(
      *(("GIGAMON-SNMP-MIB", "gigamonSnmpNotifHardWareName"),
        ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifLevel"),
        ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifDescription"),
        ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifPortName"),
        ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifTAPRelayStatus"))
)
if mibBuilder.loadTexts:
    gigamonSnmpTapRelayChangeNotification.setStatus(
        "current"
    )

gigamonSnmpPortLinkChangeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 26866, 1, 1, 8)
)
gigamonSnmpPortLinkChangeNotification.setObjects(
      *(("GIGAMON-SNMP-MIB", "gigamonSnmpNotifHardWareName"),
        ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifLevel"),
        ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifDescription"),
        ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifPortName"),
        ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifPortLinkStatus"))
)
if mibBuilder.loadTexts:
    gigamonSnmpPortLinkChangeNotification.setStatus(
        "current"
    )

gigamonSnmpRxTxErrorNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 26866, 1, 1, 9)
)
gigamonSnmpRxTxErrorNotification.setObjects(
      *(("GIGAMON-SNMP-MIB", "gigamonSnmpNotifHardWareName"),
        ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifLevel"),
        ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifDescription"),
        ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifPortName"),
        ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifRxTxType"),
        ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifRxTxErrorType"),
        ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifCounter"))
)
if mibBuilder.loadTexts:
    gigamonSnmpRxTxErrorNotification.setStatus(
        "current"
    )

gigamonPowerChangeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 26866, 1, 1, 10)
)
gigamonPowerChangeNotification.setObjects(
      *(("GIGAMON-SNMP-MIB", "gigamonSnmpNotifHardWareName"),
        ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifLevel"),
        ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifDescription"),
        ("GIGAMON-SNMP-MIB", "gigamonNotifPowerStatus"))
)
if mibBuilder.loadTexts:
    gigamonPowerChangeNotification.setStatus(
        "current"
    )

gigamonFanChangeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 26866, 1, 1, 11)
)
gigamonFanChangeNotification.setObjects(
      *(("GIGAMON-SNMP-MIB", "gigamonSnmpNotifHardWareName"),
        ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifLevel"),
        ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifDescription"),
        ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifFanName"),
        ("GIGAMON-SNMP-MIB", "gigamonNotifFanStatus"))
)
if mibBuilder.loadTexts:
    gigamonFanChangeNotification.setStatus(
        "current"
    )

gigamonSnmpOverThresholdChangeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 26866, 1, 1, 12)
)
gigamonSnmpOverThresholdChangeNotification.setObjects(
      *(("GIGAMON-SNMP-MIB", "gigamonSnmpNotifHardWareName"),
        ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifLevel"),
        ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifDescription"),
        ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifPortName"),
        ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifUtilizationAlarm"),
        ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifUtilizationThreshold"))
)
if mibBuilder.loadTexts:
    gigamonSnmpOverThresholdChangeNotification.setStatus(
        "current"
    )

gigamonSnmpBatteryLevelChangeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 26866, 1, 1, 13)
)
gigamonSnmpBatteryLevelChangeNotification.setObjects(
      *(("GIGAMON-SNMP-MIB", "gigamonSnmpNotifHardWareName"),
        ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifLevel"),
        ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifDescription"),
        ("GIGAMON-SNMP-MIB", "gigamonSnmpBatteryLevel"))
)
if mibBuilder.loadTexts:
    gigamonSnmpBatteryLevelChangeNotification.setStatus(
        "current"
    )

gigamonLinkSpeedStatusChangeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 26866, 1, 1, 14)
)
gigamonLinkSpeedStatusChangeNotification.setObjects(
      *(("GIGAMON-SNMP-MIB", "gigamonSnmpNotifHardWareName"),
        ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifLevel"),
        ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifDescription"),
        ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifPortName"),
        ("GIGAMON-SNMP-MIB", "gigamonSnmpPortLinkSpeed"),
        ("GIGAMON-SNMP-MIB", "gigamonSnmpPortLinkDuplex"),
        ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifPortLinkStatus"))
)
if mibBuilder.loadTexts:
    gigamonLinkSpeedStatusChangeNotification.setStatus(
        "current"
    )

gigamonPowerSourceChangeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 26866, 1, 1, 15)
)
gigamonPowerSourceChangeNotification.setObjects(
      *(("GIGAMON-SNMP-MIB", "gigamonSnmpNotifHardWareName"),
        ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifLevel"),
        ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifDescription"),
        ("GIGAMON-SNMP-MIB", "gigamonSnmpPowerSource"),
        ("GIGAMON-SNMP-MIB", "gigamonNotifPowerStatus"))
)
if mibBuilder.loadTexts:
    gigamonPowerSourceChangeNotification.setStatus(
        "current"
    )

gigamonSnmpCpuUtilHighNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 26866, 1, 1, 16)
)
gigamonSnmpCpuUtilHighNotification.setObjects(
      *(("GIGAMON-SNMP-MIB", "gigamonSnmpNotifHardWareName"),
        ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifLevel"),
        ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifDescription"),
        ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifCpuIndex"),
        ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifUtilizationThreshold"))
)
if mibBuilder.loadTexts:
    gigamonSnmpCpuUtilHighNotification.setStatus(
        "current"
    )

gigamonSnmpUnexpectedShutdownNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 26866, 1, 1, 17)
)
gigamonSnmpUnexpectedShutdownNotification.setObjects(
      *(("GIGAMON-SNMP-MIB", "gigamonSnmpNotifHardWareName"),
        ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifLevel"),
        ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifDescription"))
)
if mibBuilder.loadTexts:
    gigamonSnmpUnexpectedShutdownNotification.setStatus(
        "current"
    )

gigamonSnmpDiskSpaceLowNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 26866, 1, 1, 18)
)
gigamonSnmpDiskSpaceLowNotification.setObjects(
      *(("GIGAMON-SNMP-MIB", "gigamonSnmpNotifHardWareName"),
        ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifLevel"),
        ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifDescription"),
        ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifFsMountPoint"))
)
if mibBuilder.loadTexts:
    gigamonSnmpDiskSpaceLowNotification.setStatus(
        "current"
    )

gigamonSnmpWatchdogResetNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 26866, 1, 1, 19)
)
gigamonSnmpWatchdogResetNotification.setObjects(
      *(("GIGAMON-SNMP-MIB", "gigamonSnmpNotifHardWareName"),
        ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifLevel"),
        ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifDescription"))
)
if mibBuilder.loadTexts:
    gigamonSnmpWatchdogResetNotification.setStatus(
        "current"
    )

gigamonSnmpBpsFailoverNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 26866, 1, 1, 20)
)
gigamonSnmpBpsFailoverNotification.setObjects(
      *(("GIGAMON-SNMP-MIB", "gigamonSnmpNotifHardWareName"),
        ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifLevel"),
        ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifDescription"),
        ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifBpsUnitName"),
        ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifBpsFailoverStatus"))
)
if mibBuilder.loadTexts:
    gigamonSnmpBpsFailoverNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GIGAMON-SNMP-MIB",
    **{"gigamonSnmp": gigamonSnmp,
       "gigamonSnmpNotifications": gigamonSnmpNotifications,
       "gigamonGigaVUE": gigamonGigaVUE,
       "gigamonSnmpResetSystemNotification": gigamonSnmpResetSystemNotification,
       "gigamonSnmpUserAuthFailNotification": gigamonSnmpUserAuthFailNotification,
       "gigamonSnmpFirmwareChangeNotification": gigamonSnmpFirmwareChangeNotification,
       "gigamonSnmpConfigSaveNotification": gigamonSnmpConfigSaveNotification,
       "gigamonSnmpModuleChangeNotification": gigamonSnmpModuleChangeNotification,
       "gigamonSnmpPacketDropNotification": gigamonSnmpPacketDropNotification,
       "gigamonSnmpTapRelayChangeNotification": gigamonSnmpTapRelayChangeNotification,
       "gigamonSnmpPortLinkChangeNotification": gigamonSnmpPortLinkChangeNotification,
       "gigamonSnmpRxTxErrorNotification": gigamonSnmpRxTxErrorNotification,
       "gigamonPowerChangeNotification": gigamonPowerChangeNotification,
       "gigamonFanChangeNotification": gigamonFanChangeNotification,
       "gigamonSnmpOverThresholdChangeNotification": gigamonSnmpOverThresholdChangeNotification,
       "gigamonSnmpBatteryLevelChangeNotification": gigamonSnmpBatteryLevelChangeNotification,
       "gigamonLinkSpeedStatusChangeNotification": gigamonLinkSpeedStatusChangeNotification,
       "gigamonPowerSourceChangeNotification": gigamonPowerSourceChangeNotification,
       "gigamonSnmpCpuUtilHighNotification": gigamonSnmpCpuUtilHighNotification,
       "gigamonSnmpUnexpectedShutdownNotification": gigamonSnmpUnexpectedShutdownNotification,
       "gigamonSnmpDiskSpaceLowNotification": gigamonSnmpDiskSpaceLowNotification,
       "gigamonSnmpWatchdogResetNotification": gigamonSnmpWatchdogResetNotification,
       "gigamonSnmpBpsFailoverNotification": gigamonSnmpBpsFailoverNotification,
       "gigamonSnmpNotificationObjects": gigamonSnmpNotificationObjects,
       "gigamonSnmpNotifLevel": gigamonSnmpNotifLevel,
       "gigamonSnmpNotifDescription": gigamonSnmpNotifDescription,
       "gigamonSnmpNotifOpType": gigamonSnmpNotifOpType,
       "gigamonSnmpNotifPortName": gigamonSnmpNotifPortName,
       "gigamonSnmpNotifPortLinkStatus": gigamonSnmpNotifPortLinkStatus,
       "gigamonSnmpNotifTAPRelayStatus": gigamonSnmpNotifTAPRelayStatus,
       "gigamonSnmpNotifRxTxType": gigamonSnmpNotifRxTxType,
       "gigamonSnmpNotifRxTxErrorType": gigamonSnmpNotifRxTxErrorType,
       "gigamonSnmpNotifCounter": gigamonSnmpNotifCounter,
       "gigamonSnmpNotifFirmwareName": gigamonSnmpNotifFirmwareName,
       "gigamonSnmpNotifModuleOperationType": gigamonSnmpNotifModuleOperationType,
       "gigamonSnmpNotifModuleName": gigamonSnmpNotifModuleName,
       "gigamonNotifSlotNumber": gigamonNotifSlotNumber,
       "gigamonSnmpNotifUserName": gigamonSnmpNotifUserName,
       "gigamonSnmpNotifFileName": gigamonSnmpNotifFileName,
       "gigamonNotifPowerStatus": gigamonNotifPowerStatus,
       "gigamonSnmpNotifHardWareName": gigamonSnmpNotifHardWareName,
       "gigamonSnmpNotifGigaVUE420SlotNumber": gigamonSnmpNotifGigaVUE420SlotNumber,
       "gigamonSnmpNotifFanName": gigamonSnmpNotifFanName,
       "gigamonNotifFanStatus": gigamonNotifFanStatus,
       "gigamonSnmpNotifUtilizationAlarm": gigamonSnmpNotifUtilizationAlarm,
       "gigamonSnmpNotifUtilizationThreshold": gigamonSnmpNotifUtilizationThreshold,
       "gigamonSnmpBatteryLevel": gigamonSnmpBatteryLevel,
       "gigamonSnmpPortLinkSpeed": gigamonSnmpPortLinkSpeed,
       "gigamonSnmpPortLinkDuplex": gigamonSnmpPortLinkDuplex,
       "gigamonSnmpNotifCpuIndex": gigamonSnmpNotifCpuIndex,
       "gigamonSnmpNotifFsMountPoint": gigamonSnmpNotifFsMountPoint,
       "gigamonSnmpPowerSource": gigamonSnmpPowerSource,
       "gigamonSnmpNotifBpsUnitName": gigamonSnmpNotifBpsUnitName,
       "gigamonSnmpNotifBpsFailoverStatus": gigamonSnmpNotifBpsFailoverStatus,
       "gigamonSystem": gigamonSystem,
       "manufacturer": manufacturer,
       "model": model,
       "name": name,
       "serialNumber": serialNumber,
       "systemDescription": systemDescription,
       "version": version,
       "chassisModelNumber": chassisModelNumber,
       "chassisSerialNumber": chassisSerialNumber,
       "bladeSerialNumbers": bladeSerialNumbers,
       "firmwareVersion": firmwareVersion,
       "hardwareVersion": hardwareVersion,
       "cpuRAMSize": cpuRAMSize,
       "cpuUtilization": cpuUtilization,
       "fans": fans,
       "temperatureSensors": temperatureSensors,
       "powerSupply": powerSupply,
       "gigamonProducts": gigamonProducts,
       "gigamonGV2404": gigamonGV2404,
       "gigamonGV420": gigamonGV420,
       "gigamonGV212": gigamonGV212,
       "gigamonGV216": gigamonGV216}
)
