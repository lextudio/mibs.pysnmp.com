# SNMP MIB module (CISCO-LWAPP-CLIENT-ROAMING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-LWAPP-CLIENT-ROAMING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:04:15 2024
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

(cLApDot11IfSlotId,
 cLApSysMacAddress) = mibBuilder.importSymbols(
    "CISCO-LWAPP-AP-MIB",
    "cLApDot11IfSlotId",
    "cLApSysMacAddress")

(CLDot11Channel,
 CLDot11RfParamMode) = mibBuilder.importSymbols(
    "CISCO-LWAPP-TC-MIB",
    "CLDot11Channel",
    "CLDot11RfParamMode")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

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
 MacAddress,
 TextualConvention,
 TimeInterval) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TimeInterval")


# MODULE-IDENTITY

ciscoLwappClRoamMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 523)
)
ciscoLwappClRoamMIB.setRevisions(
        ("2010-01-29 00:00",
         "2006-04-11 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoLwappClRoamMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoLwappClRoamMIBNotifs = _CiscoLwappClRoamMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 523, 0)
)
_CiscoLwappClRoamMIBObjects_ObjectIdentity = ObjectIdentity
ciscoLwappClRoamMIBObjects = _CiscoLwappClRoamMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 523, 1)
)
_ClcrRoamDot11aRfParamConfig_ObjectIdentity = ObjectIdentity
clcrRoamDot11aRfParamConfig = _ClcrRoamDot11aRfParamConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 523, 1, 1)
)


class _ClcrDot11aMode_Type(CLDot11RfParamMode):
    """Custom type clcrDot11aMode based on CLDot11RfParamMode"""


_ClcrDot11aMode_Object = MibScalar
clcrDot11aMode = _ClcrDot11aMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 523, 1, 1, 1),
    _ClcrDot11aMode_Type()
)
clcrDot11aMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clcrDot11aMode.setStatus("current")


class _ClcrDot11aMinRssi_Type(Integer32):
    """Custom type clcrDot11aMinRssi based on Integer32"""
    defaultValue = -85

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-90, -80),
    )


_ClcrDot11aMinRssi_Type.__name__ = "Integer32"
_ClcrDot11aMinRssi_Object = MibScalar
clcrDot11aMinRssi = _ClcrDot11aMinRssi_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 523, 1, 1, 2),
    _ClcrDot11aMinRssi_Type()
)
clcrDot11aMinRssi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clcrDot11aMinRssi.setStatus("deprecated")
if mibBuilder.loadTexts:
    clcrDot11aMinRssi.setUnits("dBm")


class _ClcrDot11aHysteresis_Type(Integer32):
    """Custom type clcrDot11aHysteresis based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 4),
    )


_ClcrDot11aHysteresis_Type.__name__ = "Integer32"
_ClcrDot11aHysteresis_Object = MibScalar
clcrDot11aHysteresis = _ClcrDot11aHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 523, 1, 1, 3),
    _ClcrDot11aHysteresis_Type()
)
clcrDot11aHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clcrDot11aHysteresis.setStatus("deprecated")
if mibBuilder.loadTexts:
    clcrDot11aHysteresis.setUnits("dB")


class _ClcrDot11aAdaptiveScanThreshold_Type(Integer32):
    """Custom type clcrDot11aAdaptiveScanThreshold based on Integer32"""
    defaultValue = -72

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-77, -70),
    )


_ClcrDot11aAdaptiveScanThreshold_Type.__name__ = "Integer32"
_ClcrDot11aAdaptiveScanThreshold_Object = MibScalar
clcrDot11aAdaptiveScanThreshold = _ClcrDot11aAdaptiveScanThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 523, 1, 1, 4),
    _ClcrDot11aAdaptiveScanThreshold_Type()
)
clcrDot11aAdaptiveScanThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clcrDot11aAdaptiveScanThreshold.setStatus("deprecated")
if mibBuilder.loadTexts:
    clcrDot11aAdaptiveScanThreshold.setUnits("dBm")


class _ClcrDot11aTransitionTime_Type(TimeInterval):
    """Custom type clcrDot11aTransitionTime based on TimeInterval"""
    defaultValue = 500

    subtypeSpec = TimeInterval.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 10000),
    )


_ClcrDot11aTransitionTime_Type.__name__ = "TimeInterval"
_ClcrDot11aTransitionTime_Object = MibScalar
clcrDot11aTransitionTime = _ClcrDot11aTransitionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 523, 1, 1, 5),
    _ClcrDot11aTransitionTime_Type()
)
clcrDot11aTransitionTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clcrDot11aTransitionTime.setStatus("deprecated")


class _ClcrDot11aMinRssiV2_Type(Integer32):
    """Custom type clcrDot11aMinRssiV2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-255, 255),
    )


_ClcrDot11aMinRssiV2_Type.__name__ = "Integer32"
_ClcrDot11aMinRssiV2_Object = MibScalar
clcrDot11aMinRssiV2 = _ClcrDot11aMinRssiV2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 523, 1, 1, 6),
    _ClcrDot11aMinRssiV2_Type()
)
clcrDot11aMinRssiV2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clcrDot11aMinRssiV2.setStatus("current")
if mibBuilder.loadTexts:
    clcrDot11aMinRssiV2.setUnits("dBm")


class _ClcrDot11aHysteresisV2_Type(Integer32):
    """Custom type clcrDot11aHysteresisV2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ClcrDot11aHysteresisV2_Type.__name__ = "Integer32"
_ClcrDot11aHysteresisV2_Object = MibScalar
clcrDot11aHysteresisV2 = _ClcrDot11aHysteresisV2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 523, 1, 1, 7),
    _ClcrDot11aHysteresisV2_Type()
)
clcrDot11aHysteresisV2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clcrDot11aHysteresisV2.setStatus("current")
if mibBuilder.loadTexts:
    clcrDot11aHysteresisV2.setUnits("dB")


class _ClcrDot11aAdaptiveScanThresholdV2_Type(Integer32):
    """Custom type clcrDot11aAdaptiveScanThresholdV2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-255, 255),
    )


_ClcrDot11aAdaptiveScanThresholdV2_Type.__name__ = "Integer32"
_ClcrDot11aAdaptiveScanThresholdV2_Object = MibScalar
clcrDot11aAdaptiveScanThresholdV2 = _ClcrDot11aAdaptiveScanThresholdV2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 523, 1, 1, 8),
    _ClcrDot11aAdaptiveScanThresholdV2_Type()
)
clcrDot11aAdaptiveScanThresholdV2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clcrDot11aAdaptiveScanThresholdV2.setStatus("current")
if mibBuilder.loadTexts:
    clcrDot11aAdaptiveScanThresholdV2.setUnits("dBm")


class _ClcrDot11aTransitionTimeV2_Type(TimeInterval):
    """Custom type clcrDot11aTransitionTimeV2 based on TimeInterval"""
    subtypeSpec = TimeInterval.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_ClcrDot11aTransitionTimeV2_Type.__name__ = "TimeInterval"
_ClcrDot11aTransitionTimeV2_Object = MibScalar
clcrDot11aTransitionTimeV2 = _ClcrDot11aTransitionTimeV2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 523, 1, 1, 9),
    _ClcrDot11aTransitionTimeV2_Type()
)
clcrDot11aTransitionTimeV2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clcrDot11aTransitionTimeV2.setStatus("current")
_ClcrRoamDot11bRfParamConfig_ObjectIdentity = ObjectIdentity
clcrRoamDot11bRfParamConfig = _ClcrRoamDot11bRfParamConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 523, 1, 2)
)


class _ClcrDot11bMode_Type(CLDot11RfParamMode):
    """Custom type clcrDot11bMode based on CLDot11RfParamMode"""


_ClcrDot11bMode_Object = MibScalar
clcrDot11bMode = _ClcrDot11bMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 523, 1, 2, 1),
    _ClcrDot11bMode_Type()
)
clcrDot11bMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clcrDot11bMode.setStatus("current")


class _ClcrDot11bMinRssi_Type(Integer32):
    """Custom type clcrDot11bMinRssi based on Integer32"""
    defaultValue = -85

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-90, -80),
    )


_ClcrDot11bMinRssi_Type.__name__ = "Integer32"
_ClcrDot11bMinRssi_Object = MibScalar
clcrDot11bMinRssi = _ClcrDot11bMinRssi_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 523, 1, 2, 2),
    _ClcrDot11bMinRssi_Type()
)
clcrDot11bMinRssi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clcrDot11bMinRssi.setStatus("deprecated")
if mibBuilder.loadTexts:
    clcrDot11bMinRssi.setUnits("dBm")


class _ClcrDot11bHysteresis_Type(Integer32):
    """Custom type clcrDot11bHysteresis based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 4),
    )


_ClcrDot11bHysteresis_Type.__name__ = "Integer32"
_ClcrDot11bHysteresis_Object = MibScalar
clcrDot11bHysteresis = _ClcrDot11bHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 523, 1, 2, 3),
    _ClcrDot11bHysteresis_Type()
)
clcrDot11bHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clcrDot11bHysteresis.setStatus("deprecated")
if mibBuilder.loadTexts:
    clcrDot11bHysteresis.setUnits("dB")


class _ClcrDot11bAdaptiveScanThreshold_Type(Integer32):
    """Custom type clcrDot11bAdaptiveScanThreshold based on Integer32"""
    defaultValue = -72

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-77, -70),
    )


_ClcrDot11bAdaptiveScanThreshold_Type.__name__ = "Integer32"
_ClcrDot11bAdaptiveScanThreshold_Object = MibScalar
clcrDot11bAdaptiveScanThreshold = _ClcrDot11bAdaptiveScanThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 523, 1, 2, 4),
    _ClcrDot11bAdaptiveScanThreshold_Type()
)
clcrDot11bAdaptiveScanThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clcrDot11bAdaptiveScanThreshold.setStatus("deprecated")
if mibBuilder.loadTexts:
    clcrDot11bAdaptiveScanThreshold.setUnits("dBm")


class _ClcrDot11bTransitionTime_Type(TimeInterval):
    """Custom type clcrDot11bTransitionTime based on TimeInterval"""
    defaultValue = 500

    subtypeSpec = TimeInterval.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 10000),
    )


_ClcrDot11bTransitionTime_Type.__name__ = "TimeInterval"
_ClcrDot11bTransitionTime_Object = MibScalar
clcrDot11bTransitionTime = _ClcrDot11bTransitionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 523, 1, 2, 5),
    _ClcrDot11bTransitionTime_Type()
)
clcrDot11bTransitionTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clcrDot11bTransitionTime.setStatus("deprecated")


class _ClcrDot11bMinRssiV2_Type(Integer32):
    """Custom type clcrDot11bMinRssiV2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-255, 255),
    )


_ClcrDot11bMinRssiV2_Type.__name__ = "Integer32"
_ClcrDot11bMinRssiV2_Object = MibScalar
clcrDot11bMinRssiV2 = _ClcrDot11bMinRssiV2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 523, 1, 2, 6),
    _ClcrDot11bMinRssiV2_Type()
)
clcrDot11bMinRssiV2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clcrDot11bMinRssiV2.setStatus("current")
if mibBuilder.loadTexts:
    clcrDot11bMinRssiV2.setUnits("dBm")


class _ClcrDot11bHysteresisV2_Type(Integer32):
    """Custom type clcrDot11bHysteresisV2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ClcrDot11bHysteresisV2_Type.__name__ = "Integer32"
_ClcrDot11bHysteresisV2_Object = MibScalar
clcrDot11bHysteresisV2 = _ClcrDot11bHysteresisV2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 523, 1, 2, 7),
    _ClcrDot11bHysteresisV2_Type()
)
clcrDot11bHysteresisV2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clcrDot11bHysteresisV2.setStatus("current")
if mibBuilder.loadTexts:
    clcrDot11bHysteresisV2.setUnits("dB")


class _ClcrDot11bAdaptiveScanThresholdV2_Type(Integer32):
    """Custom type clcrDot11bAdaptiveScanThresholdV2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-255, 255),
    )


_ClcrDot11bAdaptiveScanThresholdV2_Type.__name__ = "Integer32"
_ClcrDot11bAdaptiveScanThresholdV2_Object = MibScalar
clcrDot11bAdaptiveScanThresholdV2 = _ClcrDot11bAdaptiveScanThresholdV2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 523, 1, 2, 8),
    _ClcrDot11bAdaptiveScanThresholdV2_Type()
)
clcrDot11bAdaptiveScanThresholdV2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clcrDot11bAdaptiveScanThresholdV2.setStatus("current")
if mibBuilder.loadTexts:
    clcrDot11bAdaptiveScanThresholdV2.setUnits("dBm")


class _ClcrDot11bTransitionTimeV2_Type(TimeInterval):
    """Custom type clcrDot11bTransitionTimeV2 based on TimeInterval"""
    subtypeSpec = TimeInterval.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_ClcrDot11bTransitionTimeV2_Type.__name__ = "TimeInterval"
_ClcrDot11bTransitionTimeV2_Object = MibScalar
clcrDot11bTransitionTimeV2 = _ClcrDot11bTransitionTimeV2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 523, 1, 2, 9),
    _ClcrDot11bTransitionTimeV2_Type()
)
clcrDot11bTransitionTimeV2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clcrDot11bTransitionTimeV2.setStatus("current")
_ClcrRoamReasonReport_ObjectIdentity = ObjectIdentity
clcrRoamReasonReport = _ClcrRoamReasonReport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 523, 1, 3)
)
_ClcrRoamReasonReportTable_Object = MibTable
clcrRoamReasonReportTable = _ClcrRoamReasonReportTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 523, 1, 3, 1)
)
if mibBuilder.loadTexts:
    clcrRoamReasonReportTable.setStatus("current")
_ClcrRoamReasonReportEntry_Object = MibTableRow
clcrRoamReasonReportEntry = _ClcrRoamReasonReportEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 523, 1, 3, 1, 1)
)
clcrRoamReasonReportEntry.setIndexNames(
    (0, "CISCO-LWAPP-CLIENT-ROAMING-MIB", "clcrRoamClientMacAddress"),
    (0, "CISCO-LWAPP-CLIENT-ROAMING-MIB", "clcrRoamClientTimeStamp"),
)
if mibBuilder.loadTexts:
    clcrRoamReasonReportEntry.setStatus("current")
_ClcrRoamClientMacAddress_Type = MacAddress
_ClcrRoamClientMacAddress_Object = MibTableColumn
clcrRoamClientMacAddress = _ClcrRoamClientMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 523, 1, 3, 1, 1, 1),
    _ClcrRoamClientMacAddress_Type()
)
clcrRoamClientMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clcrRoamClientMacAddress.setStatus("current")
_ClcrRoamClientTimeStamp_Type = TimeTicks
_ClcrRoamClientTimeStamp_Object = MibTableColumn
clcrRoamClientTimeStamp = _ClcrRoamClientTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 523, 1, 3, 1, 1, 2),
    _ClcrRoamClientTimeStamp_Type()
)
clcrRoamClientTimeStamp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clcrRoamClientTimeStamp.setStatus("current")
_ClcrRoamNewApMacAddress_Type = MacAddress
_ClcrRoamNewApMacAddress_Object = MibTableColumn
clcrRoamNewApMacAddress = _ClcrRoamNewApMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 523, 1, 3, 1, 1, 3),
    _ClcrRoamNewApMacAddress_Type()
)
clcrRoamNewApMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clcrRoamNewApMacAddress.setStatus("current")
_ClcrRoamPrevApMacAddress_Type = MacAddress
_ClcrRoamPrevApMacAddress_Object = MibTableColumn
clcrRoamPrevApMacAddress = _ClcrRoamPrevApMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 523, 1, 3, 1, 1, 4),
    _ClcrRoamPrevApMacAddress_Type()
)
clcrRoamPrevApMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clcrRoamPrevApMacAddress.setStatus("current")
_ClcrRoamPrevApChannel_Type = CLDot11Channel
_ClcrRoamPrevApChannel_Object = MibTableColumn
clcrRoamPrevApChannel = _ClcrRoamPrevApChannel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 523, 1, 3, 1, 1, 5),
    _ClcrRoamPrevApChannel_Type()
)
clcrRoamPrevApChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clcrRoamPrevApChannel.setStatus("current")


class _ClcrRoamPrevApSsid_Type(OctetString):
    """Custom type clcrRoamPrevApSsid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ClcrRoamPrevApSsid_Type.__name__ = "OctetString"
_ClcrRoamPrevApSsid_Object = MibTableColumn
clcrRoamPrevApSsid = _ClcrRoamPrevApSsid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 523, 1, 3, 1, 1, 6),
    _ClcrRoamPrevApSsid_Type()
)
clcrRoamPrevApSsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clcrRoamPrevApSsid.setStatus("current")
_ClcrRoamDisassocTimeInterval_Type = TimeInterval
_ClcrRoamDisassocTimeInterval_Object = MibTableColumn
clcrRoamDisassocTimeInterval = _ClcrRoamDisassocTimeInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 523, 1, 3, 1, 1, 7),
    _ClcrRoamDisassocTimeInterval_Type()
)
clcrRoamDisassocTimeInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clcrRoamDisassocTimeInterval.setStatus("current")


class _ClcrRoamReason_Type(Integer32):
    """Custom type clcrRoamReason based on Integer32"""
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
        *(("clcrBetterAp", 8),
          ("clcrDirectedRoam", 4),
          ("clcrDisassociated", 9),
          ("clcrFirstAssociation", 5),
          ("clcrInsufficientCapacity", 3),
          ("clcrLoadBalancing", 2),
          ("clcrPoorLink", 1),
          ("clcrRoamingIn", 6),
          ("clcrRoamingOut", 7),
          ("clcrUnspecified", 0))
    )


_ClcrRoamReason_Type.__name__ = "Integer32"
_ClcrRoamReason_Object = MibTableColumn
clcrRoamReason = _ClcrRoamReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 523, 1, 3, 1, 1, 8),
    _ClcrRoamReason_Type()
)
clcrRoamReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clcrRoamReason.setStatus("current")
_ClcrRoamDot11Stats_ObjectIdentity = ObjectIdentity
clcrRoamDot11Stats = _ClcrRoamDot11Stats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 523, 1, 4)
)
_ClcrDot11StatsTable_Object = MibTable
clcrDot11StatsTable = _ClcrDot11StatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 523, 1, 4, 1)
)
if mibBuilder.loadTexts:
    clcrDot11StatsTable.setStatus("current")
_ClcrDot11StatsEntry_Object = MibTableRow
clcrDot11StatsEntry = _ClcrDot11StatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 523, 1, 4, 1, 1)
)
clcrDot11StatsEntry.setIndexNames(
    (0, "CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
    (0, "CISCO-LWAPP-AP-MIB", "cLApDot11IfSlotId"),
)
if mibBuilder.loadTexts:
    clcrDot11StatsEntry.setStatus("current")
_ClcrDot11NeighborRequestRx_Type = Counter32
_ClcrDot11NeighborRequestRx_Object = MibTableColumn
clcrDot11NeighborRequestRx = _ClcrDot11NeighborRequestRx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 523, 1, 4, 1, 1, 1),
    _ClcrDot11NeighborRequestRx_Type()
)
clcrDot11NeighborRequestRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clcrDot11NeighborRequestRx.setStatus("current")
_ClcrDot11NeighborReplySent_Type = Counter32
_ClcrDot11NeighborReplySent_Object = MibTableColumn
clcrDot11NeighborReplySent = _ClcrDot11NeighborReplySent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 523, 1, 4, 1, 1, 2),
    _ClcrDot11NeighborReplySent_Type()
)
clcrDot11NeighborReplySent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clcrDot11NeighborReplySent.setStatus("current")
_ClcrDot11RoamReasonReportRx_Type = Counter32
_ClcrDot11RoamReasonReportRx_Object = MibTableColumn
clcrDot11RoamReasonReportRx = _ClcrDot11RoamReasonReportRx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 523, 1, 4, 1, 1, 3),
    _ClcrDot11RoamReasonReportRx_Type()
)
clcrDot11RoamReasonReportRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clcrDot11RoamReasonReportRx.setStatus("current")
_ClcrDot11BcastUpdatesSent_Type = Counter32
_ClcrDot11BcastUpdatesSent_Object = MibTableColumn
clcrDot11BcastUpdatesSent = _ClcrDot11BcastUpdatesSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 523, 1, 4, 1, 1, 4),
    _ClcrDot11BcastUpdatesSent_Type()
)
clcrDot11BcastUpdatesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clcrDot11BcastUpdatesSent.setStatus("current")
_CiscoLwappClRoamMIBConform_ObjectIdentity = ObjectIdentity
ciscoLwappClRoamMIBConform = _CiscoLwappClRoamMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 523, 2)
)
_CiscoLwappClRoamMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoLwappClRoamMIBCompliances = _CiscoLwappClRoamMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 523, 2, 1)
)
_CiscoLwappClRoamMIBGroups_ObjectIdentity = ObjectIdentity
ciscoLwappClRoamMIBGroups = _CiscoLwappClRoamMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 523, 2, 2)
)

# Managed Objects groups

ciscoLwappClRoamDot11aRfParamsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 523, 2, 2, 1)
)
ciscoLwappClRoamDot11aRfParamsGroup.setObjects(
      *(("CISCO-LWAPP-CLIENT-ROAMING-MIB", "clcrDot11aMode"),
        ("CISCO-LWAPP-CLIENT-ROAMING-MIB", "clcrDot11aMinRssi"),
        ("CISCO-LWAPP-CLIENT-ROAMING-MIB", "clcrDot11aHysteresis"),
        ("CISCO-LWAPP-CLIENT-ROAMING-MIB", "clcrDot11aAdaptiveScanThreshold"),
        ("CISCO-LWAPP-CLIENT-ROAMING-MIB", "clcrDot11aTransitionTime"))
)
if mibBuilder.loadTexts:
    ciscoLwappClRoamDot11aRfParamsGroup.setStatus("deprecated")

ciscoLwappClRoamDot11bRfParamsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 523, 2, 2, 2)
)
ciscoLwappClRoamDot11bRfParamsGroup.setObjects(
      *(("CISCO-LWAPP-CLIENT-ROAMING-MIB", "clcrDot11bMode"),
        ("CISCO-LWAPP-CLIENT-ROAMING-MIB", "clcrDot11bMinRssi"),
        ("CISCO-LWAPP-CLIENT-ROAMING-MIB", "clcrDot11bHysteresis"),
        ("CISCO-LWAPP-CLIENT-ROAMING-MIB", "clcrDot11bAdaptiveScanThreshold"),
        ("CISCO-LWAPP-CLIENT-ROAMING-MIB", "clcrDot11bTransitionTime"))
)
if mibBuilder.loadTexts:
    ciscoLwappClRoamDot11bRfParamsGroup.setStatus("deprecated")

ciscoLwappClRoamroamReasonGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 523, 2, 2, 3)
)
ciscoLwappClRoamroamReasonGroup.setObjects(
      *(("CISCO-LWAPP-CLIENT-ROAMING-MIB", "clcrRoamNewApMacAddress"),
        ("CISCO-LWAPP-CLIENT-ROAMING-MIB", "clcrRoamPrevApMacAddress"),
        ("CISCO-LWAPP-CLIENT-ROAMING-MIB", "clcrRoamPrevApChannel"),
        ("CISCO-LWAPP-CLIENT-ROAMING-MIB", "clcrRoamPrevApSsid"),
        ("CISCO-LWAPP-CLIENT-ROAMING-MIB", "clcrRoamDisassocTimeInterval"),
        ("CISCO-LWAPP-CLIENT-ROAMING-MIB", "clcrRoamReason"))
)
if mibBuilder.loadTexts:
    ciscoLwappClRoamroamReasonGroup.setStatus("current")

ciscoLwappClRoamroamingStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 523, 2, 2, 4)
)
ciscoLwappClRoamroamingStatsGroup.setObjects(
      *(("CISCO-LWAPP-CLIENT-ROAMING-MIB", "clcrDot11NeighborRequestRx"),
        ("CISCO-LWAPP-CLIENT-ROAMING-MIB", "clcrDot11NeighborReplySent"),
        ("CISCO-LWAPP-CLIENT-ROAMING-MIB", "clcrDot11RoamReasonReportRx"),
        ("CISCO-LWAPP-CLIENT-ROAMING-MIB", "clcrDot11BcastUpdatesSent"))
)
if mibBuilder.loadTexts:
    ciscoLwappClRoamroamingStatsGroup.setStatus("current")

ciscoLwappClRoamDot11aRfParamsGroupSup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 523, 2, 2, 5)
)
ciscoLwappClRoamDot11aRfParamsGroupSup1.setObjects(
      *(("CISCO-LWAPP-CLIENT-ROAMING-MIB", "clcrDot11aMode"),
        ("CISCO-LWAPP-CLIENT-ROAMING-MIB", "clcrDot11aMinRssiV2"),
        ("CISCO-LWAPP-CLIENT-ROAMING-MIB", "clcrDot11aHysteresisV2"),
        ("CISCO-LWAPP-CLIENT-ROAMING-MIB", "clcrDot11aAdaptiveScanThresholdV2"),
        ("CISCO-LWAPP-CLIENT-ROAMING-MIB", "clcrDot11aTransitionTimeV2"))
)
if mibBuilder.loadTexts:
    ciscoLwappClRoamDot11aRfParamsGroupSup1.setStatus("current")

ciscoLwappClRoamDot11bRfParamsGroupSup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 523, 2, 2, 6)
)
ciscoLwappClRoamDot11bRfParamsGroupSup1.setObjects(
      *(("CISCO-LWAPP-CLIENT-ROAMING-MIB", "clcrDot11bMode"),
        ("CISCO-LWAPP-CLIENT-ROAMING-MIB", "clcrDot11bMinRssiV2"),
        ("CISCO-LWAPP-CLIENT-ROAMING-MIB", "clcrDot11bHysteresisV2"),
        ("CISCO-LWAPP-CLIENT-ROAMING-MIB", "clcrDot11bAdaptiveScanThresholdV2"),
        ("CISCO-LWAPP-CLIENT-ROAMING-MIB", "clcrDot11bTransitionTimeV2"))
)
if mibBuilder.loadTexts:
    ciscoLwappClRoamDot11bRfParamsGroupSup1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

clcrMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 523, 2, 1, 1)
)
if mibBuilder.loadTexts:
    clcrMIBCompliance.setStatus(
        "deprecated"
    )

clcrMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 523, 2, 1, 2)
)
if mibBuilder.loadTexts:
    clcrMIBComplianceRev1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-LWAPP-CLIENT-ROAMING-MIB",
    **{"ciscoLwappClRoamMIB": ciscoLwappClRoamMIB,
       "ciscoLwappClRoamMIBNotifs": ciscoLwappClRoamMIBNotifs,
       "ciscoLwappClRoamMIBObjects": ciscoLwappClRoamMIBObjects,
       "clcrRoamDot11aRfParamConfig": clcrRoamDot11aRfParamConfig,
       "clcrDot11aMode": clcrDot11aMode,
       "clcrDot11aMinRssi": clcrDot11aMinRssi,
       "clcrDot11aHysteresis": clcrDot11aHysteresis,
       "clcrDot11aAdaptiveScanThreshold": clcrDot11aAdaptiveScanThreshold,
       "clcrDot11aTransitionTime": clcrDot11aTransitionTime,
       "clcrDot11aMinRssiV2": clcrDot11aMinRssiV2,
       "clcrDot11aHysteresisV2": clcrDot11aHysteresisV2,
       "clcrDot11aAdaptiveScanThresholdV2": clcrDot11aAdaptiveScanThresholdV2,
       "clcrDot11aTransitionTimeV2": clcrDot11aTransitionTimeV2,
       "clcrRoamDot11bRfParamConfig": clcrRoamDot11bRfParamConfig,
       "clcrDot11bMode": clcrDot11bMode,
       "clcrDot11bMinRssi": clcrDot11bMinRssi,
       "clcrDot11bHysteresis": clcrDot11bHysteresis,
       "clcrDot11bAdaptiveScanThreshold": clcrDot11bAdaptiveScanThreshold,
       "clcrDot11bTransitionTime": clcrDot11bTransitionTime,
       "clcrDot11bMinRssiV2": clcrDot11bMinRssiV2,
       "clcrDot11bHysteresisV2": clcrDot11bHysteresisV2,
       "clcrDot11bAdaptiveScanThresholdV2": clcrDot11bAdaptiveScanThresholdV2,
       "clcrDot11bTransitionTimeV2": clcrDot11bTransitionTimeV2,
       "clcrRoamReasonReport": clcrRoamReasonReport,
       "clcrRoamReasonReportTable": clcrRoamReasonReportTable,
       "clcrRoamReasonReportEntry": clcrRoamReasonReportEntry,
       "clcrRoamClientMacAddress": clcrRoamClientMacAddress,
       "clcrRoamClientTimeStamp": clcrRoamClientTimeStamp,
       "clcrRoamNewApMacAddress": clcrRoamNewApMacAddress,
       "clcrRoamPrevApMacAddress": clcrRoamPrevApMacAddress,
       "clcrRoamPrevApChannel": clcrRoamPrevApChannel,
       "clcrRoamPrevApSsid": clcrRoamPrevApSsid,
       "clcrRoamDisassocTimeInterval": clcrRoamDisassocTimeInterval,
       "clcrRoamReason": clcrRoamReason,
       "clcrRoamDot11Stats": clcrRoamDot11Stats,
       "clcrDot11StatsTable": clcrDot11StatsTable,
       "clcrDot11StatsEntry": clcrDot11StatsEntry,
       "clcrDot11NeighborRequestRx": clcrDot11NeighborRequestRx,
       "clcrDot11NeighborReplySent": clcrDot11NeighborReplySent,
       "clcrDot11RoamReasonReportRx": clcrDot11RoamReasonReportRx,
       "clcrDot11BcastUpdatesSent": clcrDot11BcastUpdatesSent,
       "ciscoLwappClRoamMIBConform": ciscoLwappClRoamMIBConform,
       "ciscoLwappClRoamMIBCompliances": ciscoLwappClRoamMIBCompliances,
       "clcrMIBCompliance": clcrMIBCompliance,
       "clcrMIBComplianceRev1": clcrMIBComplianceRev1,
       "ciscoLwappClRoamMIBGroups": ciscoLwappClRoamMIBGroups,
       "ciscoLwappClRoamDot11aRfParamsGroup": ciscoLwappClRoamDot11aRfParamsGroup,
       "ciscoLwappClRoamDot11bRfParamsGroup": ciscoLwappClRoamDot11bRfParamsGroup,
       "ciscoLwappClRoamroamReasonGroup": ciscoLwappClRoamroamReasonGroup,
       "ciscoLwappClRoamroamingStatsGroup": ciscoLwappClRoamroamingStatsGroup,
       "ciscoLwappClRoamDot11aRfParamsGroupSup1": ciscoLwappClRoamDot11aRfParamsGroupSup1,
       "ciscoLwappClRoamDot11bRfParamsGroupSup1": ciscoLwappClRoamDot11bRfParamsGroupSup1}
)
