# SNMP MIB module (SCTE-HMS-HEADENDIDENT-TC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SCTE-HMS-HEADENDIDENT-TC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:53:50 2024
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

hmsTextualConventionMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 1)
)
hmsTextualConventionMIB.setRevisions(
        ("2008-07-23 13:00",
         "2008-07-12 13:00",
         "2008-01-16 13:00",
         "2007-12-17 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class VideoInputFrameRateType(Integer32, TextualConvention):
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
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("autoSelect", 2),
          ("f24Hz", 3),
          ("f25Hz", 4),
          ("f29Hz97", 5),
          ("f29or30Hz", 7),
          ("f30Hz", 6),
          ("f48Hz", 8),
          ("f50Hz", 9),
          ("f59Hz94", 10),
          ("f59or60Hz", 12),
          ("f60Hz", 11),
          ("other", 1))
    )



class QAMChannelModulationFormat(Integer32, TextualConvention):
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("other", 2),
          ("qam1024", 7),
          ("qam128", 5),
          ("qam256", 4),
          ("qam512", 6),
          ("qam64", 3),
          ("unknown", 1))
    )



class QAMChannelInterleaveMode(Integer32, TextualConvention):
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
              9,
              10,
              11,
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("fecI128J1", 7),
          ("fecI128J2", 9),
          ("fecI128J3", 10),
          ("fecI128J4", 11),
          ("fecI128J5", 12),
          ("fecI128J6", 13),
          ("fecI128J7", 14),
          ("fecI128J8", 15),
          ("fecI12J17", 8),
          ("fecI16J8", 4),
          ("fecI32J4", 5),
          ("fecI64J2", 6),
          ("fecI8J16", 3),
          ("other", 2),
          ("unknown", 1))
    )



class ProgDataType(Integer32, TextualConvention):
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
        *(("audio", 2),
          ("data", 3),
          ("other", 4),
          ("video", 1))
    )



class DeviceEnableDisableValues(Integer32, TextualConvention):
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
        *(("disabled", 1),
          ("enabled", 2),
          ("notSupported", 3))
    )



class MpegErrorStatus(Integer32, TextualConvention):
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
        *(("errors", 2),
          ("good", 1),
          ("notSupported", 3))
    )



class HePIDValue(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8191),
        ValueRangeConstraint(65535, 65535),
    )



class HeClockSource(Integer32, TextualConvention):
    status = "current"
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
        *(("external", 4),
          ("internal", 3),
          ("none", 6),
          ("ntp", 5),
          ("other", 2),
          ("unknown", 1))
    )



class HeResetValue(Integer32, TextualConvention):
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
        *(("reset", 1),
          ("resetting", 3),
          ("running", 2))
    )



class HeTenthVolt(Integer32, TextualConvention):
    status = "current"
    displayHint = "d-1"


class HeTenthdBm(Integer32, TextualConvention):
    status = "current"
    displayHint = "d-1"


class HeTenthdBmV(Integer32, TextualConvention):
    status = "current"
    displayHint = "d-1"


class HeTenthCentigrade(Integer32, TextualConvention):
    status = "current"
    displayHint = "d-1"


class HeHundredthNanoMeter(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d-2"


class HeTenthdB(Integer32, TextualConvention):
    status = "current"
    displayHint = "d-1"


class HeOnOffControl(Integer32, TextualConvention):
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
        *(("meaningless", 3),
          ("off", 1),
          ("on", 2))
    )



class HeOnOffStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )



class HeAlarmControl(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alarmDisabled", 2),
          ("alarmEnabled", 1))
    )



class HeTrapRegenerate(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("trapNormal", 2),
          ("trapRegenerate", 1))
    )



class HeDigitalAlarmSeverity(Integer32, TextualConvention):
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("clear", 6),
          ("critical", 1),
          ("information", 7),
          ("major", 2),
          ("minor", 3),
          ("status", 5),
          ("warning", 4))
    )



class HeDigitalAlarmType(Integer32, TextualConvention):
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
        *(("capacity", 4),
          ("communication", 1),
          ("maintenance", 5),
          ("other", 9),
          ("process", 2),
          ("programMgmt", 7),
          ("provisioning", 6),
          ("redundancy", 8),
          ("session", 3))
    )



class HeFaultStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fault", 2),
          ("normal", 1))
    )



class HeMilliAmp(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d-3"


class HeHundredthWatts(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d-2"


# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SCTE-HMS-HEADENDIDENT-TC-MIB",
    **{"VideoInputFrameRateType": VideoInputFrameRateType,
       "QAMChannelModulationFormat": QAMChannelModulationFormat,
       "QAMChannelInterleaveMode": QAMChannelInterleaveMode,
       "ProgDataType": ProgDataType,
       "DeviceEnableDisableValues": DeviceEnableDisableValues,
       "MpegErrorStatus": MpegErrorStatus,
       "HePIDValue": HePIDValue,
       "HeClockSource": HeClockSource,
       "HeResetValue": HeResetValue,
       "HeTenthVolt": HeTenthVolt,
       "HeTenthdBm": HeTenthdBm,
       "HeTenthdBmV": HeTenthdBmV,
       "HeTenthCentigrade": HeTenthCentigrade,
       "HeHundredthNanoMeter": HeHundredthNanoMeter,
       "HeTenthdB": HeTenthdB,
       "HeOnOffControl": HeOnOffControl,
       "HeOnOffStatus": HeOnOffStatus,
       "HeAlarmControl": HeAlarmControl,
       "HeTrapRegenerate": HeTrapRegenerate,
       "HeDigitalAlarmSeverity": HeDigitalAlarmSeverity,
       "HeDigitalAlarmType": HeDigitalAlarmType,
       "HeFaultStatus": HeFaultStatus,
       "HeMilliAmp": HeMilliAmp,
       "HeHundredthWatts": HeHundredthWatts,
       "hmsTextualConventionMIB": hmsTextualConventionMIB}
)
