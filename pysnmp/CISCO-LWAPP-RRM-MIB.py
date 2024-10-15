# SNMP MIB module (CISCO-LWAPP-RRM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-LWAPP-RRM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:04:59 2024
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

(cLApName,) = mibBuilder.importSymbols(
    "CISCO-LWAPP-AP-MIB",
    "cLApName")

(cldcApMacAddress,
 cldcClientMacAddress,
 cldcIfType) = mibBuilder.importSymbols(
    "CISCO-LWAPP-DOT11-CLIENT-MIB",
    "cldcApMacAddress",
    "cldcClientMacAddress",
    "cldcIfType")

(CLApIfType,) = mibBuilder.importSymbols(
    "CISCO-LWAPP-TC-MIB",
    "CLApIfType")

(cLWlanChdEnable,) = mibBuilder.importSymbols(
    "CISCO-LWAPP-WLAN-MIB",
    "cLWlanChdEnable")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoLwappRrmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 615)
)
ciscoLwappRrmMIB.setRevisions(
        ("2011-03-08 00:00",
         "2007-11-13 00:00",
         "2007-02-21 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class ClrRrmTupleTuningRange(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-127, 127),
    )



# MIB Managed Objects in the order of their OIDs

_CiscoLwappRrmMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoLwappRrmMIBNotifs = _CiscoLwappRrmMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 0)
)
_CiscoLwappRrmMIBObjects_ObjectIdentity = ObjectIdentity
ciscoLwappRrmMIBObjects = _CiscoLwappRrmMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1)
)
_ClrRrmConfig_ObjectIdentity = ObjectIdentity
clrRrmConfig = _ClrRrmConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1)
)
_ClrRrmParametersTable_Object = MibTable
clrRrmParametersTable = _ClrRrmParametersTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 1)
)
if mibBuilder.loadTexts:
    clrRrmParametersTable.setStatus("current")
_ClrRrmParametersEntry_Object = MibTableRow
clrRrmParametersEntry = _ClrRrmParametersEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 1, 1)
)
clrRrmParametersEntry.setIndexNames(
    (0, "CISCO-LWAPP-RRM-MIB", "clrRrmParametersType"),
)
if mibBuilder.loadTexts:
    clrRrmParametersEntry.setStatus("current")
_ClrRrmParametersType_Type = CLApIfType
_ClrRrmParametersType_Object = MibTableColumn
clrRrmParametersType = _ClrRrmParametersType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 1, 1, 1),
    _ClrRrmParametersType_Type()
)
clrRrmParametersType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clrRrmParametersType.setStatus("current")


class _ClrRrmParametersPicoCellMode_Type(Integer32):
    """Custom type clrRrmParametersPicoCellMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("picoCellv1", 2),
          ("picoCellv2", 3))
    )


_ClrRrmParametersPicoCellMode_Type.__name__ = "Integer32"
_ClrRrmParametersPicoCellMode_Object = MibTableColumn
clrRrmParametersPicoCellMode = _ClrRrmParametersPicoCellMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 1, 1, 2),
    _ClrRrmParametersPicoCellMode_Type()
)
clrRrmParametersPicoCellMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clrRrmParametersPicoCellMode.setStatus("deprecated")


class _ClrRrmParametersChdEnable_Type(TruthValue):
    """Custom type clrRrmParametersChdEnable based on TruthValue"""


_ClrRrmParametersChdEnable_Object = MibTableColumn
clrRrmParametersChdEnable = _ClrRrmParametersChdEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 1, 1, 3),
    _ClrRrmParametersChdEnable_Type()
)
clrRrmParametersChdEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clrRrmParametersChdEnable.setStatus("current")


class _ClrRrmParametersVoicePktCountThreshold_Type(Unsigned32):
    """Custom type clrRrmParametersVoicePktCountThreshold based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ClrRrmParametersVoicePktCountThreshold_Type.__name__ = "Unsigned32"
_ClrRrmParametersVoicePktCountThreshold_Object = MibTableColumn
clrRrmParametersVoicePktCountThreshold = _ClrRrmParametersVoicePktCountThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 1, 1, 4),
    _ClrRrmParametersVoicePktCountThreshold_Type()
)
clrRrmParametersVoicePktCountThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clrRrmParametersVoicePktCountThreshold.setStatus("current")
if mibBuilder.loadTexts:
    clrRrmParametersVoicePktCountThreshold.setUnits("packets")


class _ClrRrmParametersVoicePktPercentThreshold_Type(Unsigned32):
    """Custom type clrRrmParametersVoicePktPercentThreshold based on Unsigned32"""
    defaultValue = 20

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_ClrRrmParametersVoicePktPercentThreshold_Type.__name__ = "Unsigned32"
_ClrRrmParametersVoicePktPercentThreshold_Object = MibTableColumn
clrRrmParametersVoicePktPercentThreshold = _ClrRrmParametersVoicePktPercentThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 1, 1, 5),
    _ClrRrmParametersVoicePktPercentThreshold_Type()
)
clrRrmParametersVoicePktPercentThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clrRrmParametersVoicePktPercentThreshold.setStatus("current")
if mibBuilder.loadTexts:
    clrRrmParametersVoicePktPercentThreshold.setUnits("percent")


class _ClrRrmParametersVoiceRssiThreshold_Type(Integer32):
    """Custom type clrRrmParametersVoiceRssiThreshold based on Integer32"""
    defaultValue = -80

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-90, -60),
    )


_ClrRrmParametersVoiceRssiThreshold_Type.__name__ = "Integer32"
_ClrRrmParametersVoiceRssiThreshold_Object = MibTableColumn
clrRrmParametersVoiceRssiThreshold = _ClrRrmParametersVoiceRssiThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 1, 1, 6),
    _ClrRrmParametersVoiceRssiThreshold_Type()
)
clrRrmParametersVoiceRssiThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clrRrmParametersVoiceRssiThreshold.setStatus("current")
if mibBuilder.loadTexts:
    clrRrmParametersVoiceRssiThreshold.setUnits("dbm")


class _ClrRrmParametersDataPktCountThreshold_Type(Unsigned32):
    """Custom type clrRrmParametersDataPktCountThreshold based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ClrRrmParametersDataPktCountThreshold_Type.__name__ = "Unsigned32"
_ClrRrmParametersDataPktCountThreshold_Object = MibTableColumn
clrRrmParametersDataPktCountThreshold = _ClrRrmParametersDataPktCountThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 1, 1, 7),
    _ClrRrmParametersDataPktCountThreshold_Type()
)
clrRrmParametersDataPktCountThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clrRrmParametersDataPktCountThreshold.setStatus("current")
if mibBuilder.loadTexts:
    clrRrmParametersDataPktCountThreshold.setUnits("packets")


class _ClrRrmParametersDataPktPercentThreshold_Type(Unsigned32):
    """Custom type clrRrmParametersDataPktPercentThreshold based on Unsigned32"""
    defaultValue = 20

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_ClrRrmParametersDataPktPercentThreshold_Type.__name__ = "Unsigned32"
_ClrRrmParametersDataPktPercentThreshold_Object = MibTableColumn
clrRrmParametersDataPktPercentThreshold = _ClrRrmParametersDataPktPercentThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 1, 1, 8),
    _ClrRrmParametersDataPktPercentThreshold_Type()
)
clrRrmParametersDataPktPercentThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clrRrmParametersDataPktPercentThreshold.setStatus("current")
if mibBuilder.loadTexts:
    clrRrmParametersDataPktPercentThreshold.setUnits("percent")


class _ClrRrmParametersDataRssiThreshold_Type(Integer32):
    """Custom type clrRrmParametersDataRssiThreshold based on Integer32"""
    defaultValue = -74

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-90, -60),
    )


_ClrRrmParametersDataRssiThreshold_Type.__name__ = "Integer32"
_ClrRrmParametersDataRssiThreshold_Object = MibTableColumn
clrRrmParametersDataRssiThreshold = _ClrRrmParametersDataRssiThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 1, 1, 9),
    _ClrRrmParametersDataRssiThreshold_Type()
)
clrRrmParametersDataRssiThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clrRrmParametersDataRssiThreshold.setStatus("current")
if mibBuilder.loadTexts:
    clrRrmParametersDataRssiThreshold.setUnits("dbm")


class _ClrRrmParametersDcaChannelWidth_Type(Integer32):
    """Custom type clrRrmParametersDcaChannelWidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("max", 3),
          ("medium", 2),
          ("min", 1))
    )


_ClrRrmParametersDcaChannelWidth_Type.__name__ = "Integer32"
_ClrRrmParametersDcaChannelWidth_Object = MibTableColumn
clrRrmParametersDcaChannelWidth = _ClrRrmParametersDcaChannelWidth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 1, 1, 10),
    _ClrRrmParametersDcaChannelWidth_Type()
)
clrRrmParametersDcaChannelWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clrRrmParametersDcaChannelWidth.setStatus("current")


class _ClrRrmParametersMaxTxPower_Type(Integer32):
    """Custom type clrRrmParametersMaxTxPower based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-126, 126),
    )


_ClrRrmParametersMaxTxPower_Type.__name__ = "Integer32"
_ClrRrmParametersMaxTxPower_Object = MibTableColumn
clrRrmParametersMaxTxPower = _ClrRrmParametersMaxTxPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 1, 1, 11),
    _ClrRrmParametersMaxTxPower_Type()
)
clrRrmParametersMaxTxPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clrRrmParametersMaxTxPower.setStatus("current")
if mibBuilder.loadTexts:
    clrRrmParametersMaxTxPower.setUnits("dBm")


class _ClrRrmParametersMinTxPower_Type(Integer32):
    """Custom type clrRrmParametersMinTxPower based on Integer32"""
    defaultValue = -10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-126, 126),
    )


_ClrRrmParametersMinTxPower_Type.__name__ = "Integer32"
_ClrRrmParametersMinTxPower_Object = MibTableColumn
clrRrmParametersMinTxPower = _ClrRrmParametersMinTxPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 1, 1, 12),
    _ClrRrmParametersMinTxPower_Type()
)
clrRrmParametersMinTxPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clrRrmParametersMinTxPower.setStatus("current")
if mibBuilder.loadTexts:
    clrRrmParametersMinTxPower.setUnits("dBm")


class _ClrRrmParametersTpcVersion_Type(Integer32):
    """Custom type clrRrmParametersTpcVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("versionOne", 1),
          ("versionTwo", 2))
    )


_ClrRrmParametersTpcVersion_Type.__name__ = "Integer32"
_ClrRrmParametersTpcVersion_Object = MibTableColumn
clrRrmParametersTpcVersion = _ClrRrmParametersTpcVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 1, 1, 13),
    _ClrRrmParametersTpcVersion_Type()
)
clrRrmParametersTpcVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clrRrmParametersTpcVersion.setStatus("current")


class _ClrRrmParametersMaxClients_Type(Unsigned32):
    """Custom type clrRrmParametersMaxClients based on Unsigned32"""
    defaultValue = 200

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_ClrRrmParametersMaxClients_Type.__name__ = "Unsigned32"
_ClrRrmParametersMaxClients_Object = MibTableColumn
clrRrmParametersMaxClients = _ClrRrmParametersMaxClients_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 1, 1, 14),
    _ClrRrmParametersMaxClients_Type()
)
clrRrmParametersMaxClients.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clrRrmParametersMaxClients.setStatus("current")


class _ClrRrmParametersRssiCheckEnable_Type(TruthValue):
    """Custom type clrRrmParametersRssiCheckEnable based on TruthValue"""


_ClrRrmParametersRssiCheckEnable_Object = MibTableColumn
clrRrmParametersRssiCheckEnable = _ClrRrmParametersRssiCheckEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 1, 1, 15),
    _ClrRrmParametersRssiCheckEnable_Type()
)
clrRrmParametersRssiCheckEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clrRrmParametersRssiCheckEnable.setStatus("current")


class _ClrRrmParametersRssiThreshold_Type(Integer32):
    """Custom type clrRrmParametersRssiThreshold based on Integer32"""
    defaultValue = -80

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-90, -60),
    )


_ClrRrmParametersRssiThreshold_Type.__name__ = "Integer32"
_ClrRrmParametersRssiThreshold_Object = MibTableColumn
clrRrmParametersRssiThreshold = _ClrRrmParametersRssiThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 1, 1, 16),
    _ClrRrmParametersRssiThreshold_Type()
)
clrRrmParametersRssiThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clrRrmParametersRssiThreshold.setStatus("current")
if mibBuilder.loadTexts:
    clrRrmParametersRssiThreshold.setUnits("dbm")


class _ClrRrmParametersOptRoamEnable_Type(TruthValue):
    """Custom type clrRrmParametersOptRoamEnable based on TruthValue"""


_ClrRrmParametersOptRoamEnable_Object = MibTableColumn
clrRrmParametersOptRoamEnable = _ClrRrmParametersOptRoamEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 1, 1, 17),
    _ClrRrmParametersOptRoamEnable_Type()
)
clrRrmParametersOptRoamEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clrRrmParametersOptRoamEnable.setStatus("current")


class _ClrRrmParametersOptRoamDataRate_Type(Integer32):
    """Custom type clrRrmParametersOptRoamDataRate based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 54),
    )


_ClrRrmParametersOptRoamDataRate_Type.__name__ = "Integer32"
_ClrRrmParametersOptRoamDataRate_Object = MibTableColumn
clrRrmParametersOptRoamDataRate = _ClrRrmParametersOptRoamDataRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 1, 1, 18),
    _ClrRrmParametersOptRoamDataRate_Type()
)
clrRrmParametersOptRoamDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clrRrmParametersOptRoamDataRate.setStatus("current")


class _ClrRrmParametersOptRoamInterval_Type(Integer32):
    """Custom type clrRrmParametersOptRoamInterval based on Integer32"""
    defaultValue = 90

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 90),
    )


_ClrRrmParametersOptRoamInterval_Type.__name__ = "Integer32"
_ClrRrmParametersOptRoamInterval_Object = MibTableColumn
clrRrmParametersOptRoamInterval = _ClrRrmParametersOptRoamInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 1, 1, 19),
    _ClrRrmParametersOptRoamInterval_Type()
)
clrRrmParametersOptRoamInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clrRrmParametersOptRoamInterval.setStatus("current")
_ClrRrmTupleTable_Object = MibTable
clrRrmTupleTable = _ClrRrmTupleTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 2)
)
if mibBuilder.loadTexts:
    clrRrmTupleTable.setStatus("deprecated")
_ClrRrmTupleEntry_Object = MibTableRow
clrRrmTupleEntry = _ClrRrmTupleEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 2, 1)
)
clrRrmTupleEntry.setIndexNames(
    (0, "CISCO-LWAPP-RRM-MIB", "clrRrmParametersType"),
)
if mibBuilder.loadTexts:
    clrRrmTupleEntry.setStatus("deprecated")


class _ClrRrmTupleRxSenseThresholdMin_Type(ClrRrmTupleTuningRange):
    """Custom type clrRrmTupleRxSenseThresholdMin based on ClrRrmTupleTuningRange"""
    defaultValue = -127


_ClrRrmTupleRxSenseThresholdMin_Object = MibTableColumn
clrRrmTupleRxSenseThresholdMin = _ClrRrmTupleRxSenseThresholdMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 2, 1, 1),
    _ClrRrmTupleRxSenseThresholdMin_Type()
)
clrRrmTupleRxSenseThresholdMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clrRrmTupleRxSenseThresholdMin.setStatus("deprecated")
if mibBuilder.loadTexts:
    clrRrmTupleRxSenseThresholdMin.setUnits("dbm")


class _ClrRrmTupleRxSenseThresholdMax_Type(ClrRrmTupleTuningRange):
    """Custom type clrRrmTupleRxSenseThresholdMax based on ClrRrmTupleTuningRange"""
    defaultValue = 127


_ClrRrmTupleRxSenseThresholdMax_Object = MibTableColumn
clrRrmTupleRxSenseThresholdMax = _ClrRrmTupleRxSenseThresholdMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 2, 1, 2),
    _ClrRrmTupleRxSenseThresholdMax_Type()
)
clrRrmTupleRxSenseThresholdMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clrRrmTupleRxSenseThresholdMax.setStatus("deprecated")
if mibBuilder.loadTexts:
    clrRrmTupleRxSenseThresholdMax.setUnits("dbm")


class _ClrRrmTupleRxSenseThreshold_Type(ClrRrmTupleTuningRange):
    """Custom type clrRrmTupleRxSenseThreshold based on ClrRrmTupleTuningRange"""
    defaultValue = -80


_ClrRrmTupleRxSenseThreshold_Object = MibTableColumn
clrRrmTupleRxSenseThreshold = _ClrRrmTupleRxSenseThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 2, 1, 3),
    _ClrRrmTupleRxSenseThreshold_Type()
)
clrRrmTupleRxSenseThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clrRrmTupleRxSenseThreshold.setStatus("deprecated")
if mibBuilder.loadTexts:
    clrRrmTupleRxSenseThreshold.setUnits("dbm")


class _ClrRrmTupleCcaSenseThresholdMin_Type(ClrRrmTupleTuningRange):
    """Custom type clrRrmTupleCcaSenseThresholdMin based on ClrRrmTupleTuningRange"""
    defaultValue = -127


_ClrRrmTupleCcaSenseThresholdMin_Object = MibTableColumn
clrRrmTupleCcaSenseThresholdMin = _ClrRrmTupleCcaSenseThresholdMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 2, 1, 4),
    _ClrRrmTupleCcaSenseThresholdMin_Type()
)
clrRrmTupleCcaSenseThresholdMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clrRrmTupleCcaSenseThresholdMin.setStatus("deprecated")
if mibBuilder.loadTexts:
    clrRrmTupleCcaSenseThresholdMin.setUnits("dbm")


class _ClrRrmTupleCcaSenseThresholdMax_Type(ClrRrmTupleTuningRange):
    """Custom type clrRrmTupleCcaSenseThresholdMax based on ClrRrmTupleTuningRange"""
    defaultValue = 127


_ClrRrmTupleCcaSenseThresholdMax_Object = MibTableColumn
clrRrmTupleCcaSenseThresholdMax = _ClrRrmTupleCcaSenseThresholdMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 2, 1, 5),
    _ClrRrmTupleCcaSenseThresholdMax_Type()
)
clrRrmTupleCcaSenseThresholdMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clrRrmTupleCcaSenseThresholdMax.setStatus("deprecated")
if mibBuilder.loadTexts:
    clrRrmTupleCcaSenseThresholdMax.setUnits("dbm")


class _ClrRrmTupleCcaSenseThreshold_Type(ClrRrmTupleTuningRange):
    """Custom type clrRrmTupleCcaSenseThreshold based on ClrRrmTupleTuningRange"""
    defaultValue = -60


_ClrRrmTupleCcaSenseThreshold_Object = MibTableColumn
clrRrmTupleCcaSenseThreshold = _ClrRrmTupleCcaSenseThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 2, 1, 6),
    _ClrRrmTupleCcaSenseThreshold_Type()
)
clrRrmTupleCcaSenseThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clrRrmTupleCcaSenseThreshold.setStatus("deprecated")
if mibBuilder.loadTexts:
    clrRrmTupleCcaSenseThreshold.setUnits("dbm")


class _ClrRrmTupleTransmitPowerLevelMin_Type(ClrRrmTupleTuningRange):
    """Custom type clrRrmTupleTransmitPowerLevelMin based on ClrRrmTupleTuningRange"""
    defaultValue = -127


_ClrRrmTupleTransmitPowerLevelMin_Object = MibTableColumn
clrRrmTupleTransmitPowerLevelMin = _ClrRrmTupleTransmitPowerLevelMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 2, 1, 7),
    _ClrRrmTupleTransmitPowerLevelMin_Type()
)
clrRrmTupleTransmitPowerLevelMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clrRrmTupleTransmitPowerLevelMin.setStatus("deprecated")
if mibBuilder.loadTexts:
    clrRrmTupleTransmitPowerLevelMin.setUnits("dbm")


class _ClrRrmTupleTransmitPowerLevelMax_Type(ClrRrmTupleTuningRange):
    """Custom type clrRrmTupleTransmitPowerLevelMax based on ClrRrmTupleTuningRange"""
    defaultValue = 127


_ClrRrmTupleTransmitPowerLevelMax_Object = MibTableColumn
clrRrmTupleTransmitPowerLevelMax = _ClrRrmTupleTransmitPowerLevelMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 2, 1, 8),
    _ClrRrmTupleTransmitPowerLevelMax_Type()
)
clrRrmTupleTransmitPowerLevelMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clrRrmTupleTransmitPowerLevelMax.setStatus("deprecated")
if mibBuilder.loadTexts:
    clrRrmTupleTransmitPowerLevelMax.setUnits("dbm")


class _ClrRrmTupleTransmitPowerLevel_Type(ClrRrmTupleTuningRange):
    """Custom type clrRrmTupleTransmitPowerLevel based on ClrRrmTupleTuningRange"""
    defaultValue = 10


_ClrRrmTupleTransmitPowerLevel_Object = MibTableColumn
clrRrmTupleTransmitPowerLevel = _ClrRrmTupleTransmitPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 2, 1, 9),
    _ClrRrmTupleTransmitPowerLevel_Type()
)
clrRrmTupleTransmitPowerLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clrRrmTupleTransmitPowerLevel.setStatus("deprecated")
if mibBuilder.loadTexts:
    clrRrmTupleTransmitPowerLevel.setUnits("dbm")
_ClrRrmTupleSetDefault_Type = TruthValue
_ClrRrmTupleSetDefault_Object = MibTableColumn
clrRrmTupleSetDefault = _ClrRrmTupleSetDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 2, 1, 10),
    _ClrRrmTupleSetDefault_Type()
)
clrRrmTupleSetDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clrRrmTupleSetDefault.setStatus("deprecated")
_ClrRrmChannelTable_Object = MibTable
clrRrmChannelTable = _ClrRrmChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 4)
)
if mibBuilder.loadTexts:
    clrRrmChannelTable.setStatus("current")
_ClrRrmChannelEntry_Object = MibTableRow
clrRrmChannelEntry = _ClrRrmChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 4, 1)
)
clrRrmChannelEntry.setIndexNames(
    (0, "CISCO-LWAPP-RRM-MIB", "clrRrmParametersType"),
    (0, "CISCO-LWAPP-RRM-MIB", "clrRrmChannelNum"),
)
if mibBuilder.loadTexts:
    clrRrmChannelEntry.setStatus("current")
_ClrRrmChannelNum_Type = Unsigned32
_ClrRrmChannelNum_Object = MibTableColumn
clrRrmChannelNum = _ClrRrmChannelNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 4, 1, 1),
    _ClrRrmChannelNum_Type()
)
clrRrmChannelNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clrRrmChannelNum.setStatus("current")


class _ClrRrmChannelDcaState_Type(TruthValue):
    """Custom type clrRrmChannelDcaState based on TruthValue"""


_ClrRrmChannelDcaState_Object = MibTableColumn
clrRrmChannelDcaState = _ClrRrmChannelDcaState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 4, 1, 2),
    _ClrRrmChannelDcaState_Type()
)
clrRrmChannelDcaState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clrRrmChannelDcaState.setStatus("current")
_ClrRrmDot11BandGrpTable_Object = MibTable
clrRrmDot11BandGrpTable = _ClrRrmDot11BandGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 5)
)
if mibBuilder.loadTexts:
    clrRrmDot11BandGrpTable.setStatus("current")
_ClrRrmDot11BandGrpEntry_Object = MibTableRow
clrRrmDot11BandGrpEntry = _ClrRrmDot11BandGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 5, 1)
)
clrRrmDot11BandGrpEntry.setIndexNames(
    (0, "CISCO-LWAPP-RRM-MIB", "clrRrmParametersType"),
)
if mibBuilder.loadTexts:
    clrRrmDot11BandGrpEntry.setStatus("current")
_ClrRrmDot11BandGrpLeaderIpAddressType_Type = InetAddressType
_ClrRrmDot11BandGrpLeaderIpAddressType_Object = MibTableColumn
clrRrmDot11BandGrpLeaderIpAddressType = _ClrRrmDot11BandGrpLeaderIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 5, 1, 1),
    _ClrRrmDot11BandGrpLeaderIpAddressType_Type()
)
clrRrmDot11BandGrpLeaderIpAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clrRrmDot11BandGrpLeaderIpAddressType.setStatus("current")
_ClrRrmDot11BandGrpLeaderIpAddress_Type = InetAddress
_ClrRrmDot11BandGrpLeaderIpAddress_Object = MibTableColumn
clrRrmDot11BandGrpLeaderIpAddress = _ClrRrmDot11BandGrpLeaderIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 5, 1, 2),
    _ClrRrmDot11BandGrpLeaderIpAddress_Type()
)
clrRrmDot11BandGrpLeaderIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clrRrmDot11BandGrpLeaderIpAddress.setStatus("current")
_ClrRrmDot11BandGrpLeaderName_Type = SnmpAdminString
_ClrRrmDot11BandGrpLeaderName_Object = MibTableColumn
clrRrmDot11BandGrpLeaderName = _ClrRrmDot11BandGrpLeaderName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 5, 1, 3),
    _ClrRrmDot11BandGrpLeaderName_Type()
)
clrRrmDot11BandGrpLeaderName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clrRrmDot11BandGrpLeaderName.setStatus("current")


class _ClrRrmDot11BandGrpMode_Type(Integer32):
    """Custom type clrRrmDot11BandGrpMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 1),
          ("leader", 3),
          ("off", 2))
    )


_ClrRrmDot11BandGrpMode_Type.__name__ = "Integer32"
_ClrRrmDot11BandGrpMode_Object = MibTableColumn
clrRrmDot11BandGrpMode = _ClrRrmDot11BandGrpMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 5, 1, 4),
    _ClrRrmDot11BandGrpMode_Type()
)
clrRrmDot11BandGrpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clrRrmDot11BandGrpMode.setStatus("current")


class _ClrRrmDot11BandGrpRole_Type(Integer32):
    """Custom type clrRrmDot11BandGrpRole based on Integer32"""
    defaultValue = 2

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
        *(("auto-leader", 2),
          ("auto-member", 3),
          ("none", 1),
          ("static-leader", 4),
          ("static-member", 5))
    )


_ClrRrmDot11BandGrpRole_Type.__name__ = "Integer32"
_ClrRrmDot11BandGrpRole_Object = MibTableColumn
clrRrmDot11BandGrpRole = _ClrRrmDot11BandGrpRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 5, 1, 5),
    _ClrRrmDot11BandGrpRole_Type()
)
clrRrmDot11BandGrpRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clrRrmDot11BandGrpRole.setStatus("current")


class _ClrRrmDot11BandGrpRestart_Type(TruthValue):
    """Custom type clrRrmDot11BandGrpRestart based on TruthValue"""


_ClrRrmDot11BandGrpRestart_Object = MibTableColumn
clrRrmDot11BandGrpRestart = _ClrRrmDot11BandGrpRestart_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 5, 1, 6),
    _ClrRrmDot11BandGrpRestart_Type()
)
clrRrmDot11BandGrpRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clrRrmDot11BandGrpRestart.setStatus("current")
_ClrRrmDot11BandGrpLastUpdateTime_Type = Unsigned32
_ClrRrmDot11BandGrpLastUpdateTime_Object = MibTableColumn
clrRrmDot11BandGrpLastUpdateTime = _ClrRrmDot11BandGrpLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 5, 1, 7),
    _ClrRrmDot11BandGrpLastUpdateTime_Type()
)
clrRrmDot11BandGrpLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clrRrmDot11BandGrpLastUpdateTime.setStatus("current")
_ClrRrmDot11BandGrpInterval_Type = Unsigned32
_ClrRrmDot11BandGrpInterval_Object = MibTableColumn
clrRrmDot11BandGrpInterval = _ClrRrmDot11BandGrpInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 5, 1, 8),
    _ClrRrmDot11BandGrpInterval_Type()
)
clrRrmDot11BandGrpInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clrRrmDot11BandGrpInterval.setStatus("current")
_ClrRrmDot11BandGrpMemberTable_Object = MibTable
clrRrmDot11BandGrpMemberTable = _ClrRrmDot11BandGrpMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 6)
)
if mibBuilder.loadTexts:
    clrRrmDot11BandGrpMemberTable.setStatus("current")
_ClrRrmDot11BandGrpMemberEntry_Object = MibTableRow
clrRrmDot11BandGrpMemberEntry = _ClrRrmDot11BandGrpMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 6, 1)
)
clrRrmDot11BandGrpMemberEntry.setIndexNames(
    (0, "CISCO-LWAPP-RRM-MIB", "clrRrmParametersType"),
    (0, "CISCO-LWAPP-RRM-MIB", "clrRrmDot11BandMemberIpAddressType"),
    (0, "CISCO-LWAPP-RRM-MIB", "clrRrmDot11BandMemberIpAddress"),
)
if mibBuilder.loadTexts:
    clrRrmDot11BandGrpMemberEntry.setStatus("current")
_ClrRrmDot11BandMemberIpAddressType_Type = InetAddressType
_ClrRrmDot11BandMemberIpAddressType_Object = MibTableColumn
clrRrmDot11BandMemberIpAddressType = _ClrRrmDot11BandMemberIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 6, 1, 1),
    _ClrRrmDot11BandMemberIpAddressType_Type()
)
clrRrmDot11BandMemberIpAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clrRrmDot11BandMemberIpAddressType.setStatus("current")
_ClrRrmDot11BandMemberIpAddress_Type = InetAddress
_ClrRrmDot11BandMemberIpAddress_Object = MibTableColumn
clrRrmDot11BandMemberIpAddress = _ClrRrmDot11BandMemberIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 6, 1, 2),
    _ClrRrmDot11BandMemberIpAddress_Type()
)
clrRrmDot11BandMemberIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clrRrmDot11BandMemberIpAddress.setStatus("current")
_ClrRrmDot11BandMemberName_Type = SnmpAdminString
_ClrRrmDot11BandMemberName_Object = MibTableColumn
clrRrmDot11BandMemberName = _ClrRrmDot11BandMemberName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 6, 1, 3),
    _ClrRrmDot11BandMemberName_Type()
)
clrRrmDot11BandMemberName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clrRrmDot11BandMemberName.setStatus("current")


class _ClrRrmDot11BandMemberIsJoined_Type(TruthValue):
    """Custom type clrRrmDot11BandMemberIsJoined based on TruthValue"""


_ClrRrmDot11BandMemberIsJoined_Object = MibTableColumn
clrRrmDot11BandMemberIsJoined = _ClrRrmDot11BandMemberIsJoined_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 6, 1, 4),
    _ClrRrmDot11BandMemberIsJoined_Type()
)
clrRrmDot11BandMemberIsJoined.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clrRrmDot11BandMemberIsJoined.setStatus("current")


class _ClrRrmDot11BandMemberJoinFailureReason_Type(Integer32):
    """Custom type clrRrmDot11BandMemberJoinFailureReason based on Integer32"""
    defaultValue = 1

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
              23)
        )
    )
    namedValues = NamedValues(
        *(("alreadyAStaticLeader", 15),
          ("cntlrNameAndIpMismatch", 18),
          ("countryCodeMismatch", 13),
          ("groupSizeExceeded", 3),
          ("groupingDelayed", 10),
          ("groupingDisabled", 11),
          ("invalidGroupOrder", 4),
          ("invalidHierarchy", 14),
          ("invalidIp", 2),
          ("invalidProtocolVersion", 12),
          ("joinPending", 8),
          ("joinedSuccessfully", 1),
          ("memberOfAnotherGroup", 16),
          ("nonMatchingGroupID", 5),
          ("notAManager", 9),
          ("rfDomainMismatch", 20),
          ("splitDueToUserAction", 23),
          ("splitForInvalidStateRequest", 21),
          ("transitioningToStaticFromAuto", 22),
          ("unconfiguredAsStaticMember", 17),
          ("unexpectedError", 6),
          ("unexpectedMemoryError", 19),
          ("weakSignalStrength", 7))
    )


_ClrRrmDot11BandMemberJoinFailureReason_Type.__name__ = "Integer32"
_ClrRrmDot11BandMemberJoinFailureReason_Object = MibTableColumn
clrRrmDot11BandMemberJoinFailureReason = _ClrRrmDot11BandMemberJoinFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 6, 1, 5),
    _ClrRrmDot11BandMemberJoinFailureReason_Type()
)
clrRrmDot11BandMemberJoinFailureReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clrRrmDot11BandMemberJoinFailureReason.setStatus("current")
_ClrRrmDot11BandMemberRowStatus_Type = RowStatus
_ClrRrmDot11BandMemberRowStatus_Object = MibTableColumn
clrRrmDot11BandMemberRowStatus = _ClrRrmDot11BandMemberRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 6, 1, 6),
    _ClrRrmDot11BandMemberRowStatus_Type()
)
clrRrmDot11BandMemberRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clrRrmDot11BandMemberRowStatus.setStatus("current")
_ClrRrmDcaConfig_ObjectIdentity = ObjectIdentity
clrRrmDcaConfig = _ClrRrmDcaConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 7)
)
_ClrRrmDcaDot11aOutdoorAPDca_Type = TruthValue
_ClrRrmDcaDot11aOutdoorAPDca_Object = MibScalar
clrRrmDcaDot11aOutdoorAPDca = _ClrRrmDcaDot11aOutdoorAPDca_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 7, 1),
    _ClrRrmDcaDot11aOutdoorAPDca_Type()
)
clrRrmDcaDot11aOutdoorAPDca.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clrRrmDcaDot11aOutdoorAPDca.setStatus("current")
_ClrRrmRfGroupingPriority_Type = Unsigned32
_ClrRrmRfGroupingPriority_Object = MibScalar
clrRrmRfGroupingPriority = _ClrRrmRfGroupingPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 8),
    _ClrRrmRfGroupingPriority_Type()
)
clrRrmRfGroupingPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clrRrmRfGroupingPriority.setStatus("current")
_ClrRrmPakRssiConfig_ObjectIdentity = ObjectIdentity
clrRrmPakRssiConfig = _ClrRrmPakRssiConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 10)
)


class _ClrRrmPakRssiEnable_Type(TruthValue):
    """Custom type clrRrmPakRssiEnable based on TruthValue"""


_ClrRrmPakRssiEnable_Object = MibScalar
clrRrmPakRssiEnable = _ClrRrmPakRssiEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 10, 1),
    _ClrRrmPakRssiEnable_Type()
)
clrRrmPakRssiEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clrRrmPakRssiEnable.setStatus("current")


class _ClrRrmPakRssiThreshold_Type(Integer32):
    """Custom type clrRrmPakRssiThreshold based on Integer32"""
    defaultValue = -100


_ClrRrmPakRssiThreshold_Object = MibScalar
clrRrmPakRssiThreshold = _ClrRrmPakRssiThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 10, 2),
    _ClrRrmPakRssiThreshold_Type()
)
clrRrmPakRssiThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clrRrmPakRssiThreshold.setStatus("current")


class _ClrRrmPakRssiThresholdTrigger_Type(Integer32):
    """Custom type clrRrmPakRssiThresholdTrigger based on Integer32"""
    defaultValue = 10


_ClrRrmPakRssiThresholdTrigger_Object = MibScalar
clrRrmPakRssiThresholdTrigger = _ClrRrmPakRssiThresholdTrigger_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 10, 3),
    _ClrRrmPakRssiThresholdTrigger_Type()
)
clrRrmPakRssiThresholdTrigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clrRrmPakRssiThresholdTrigger.setStatus("current")


class _ClrRrmPakRssiNtpIpAddressType_Type(InetAddressType):
    """Custom type clrRrmPakRssiNtpIpAddressType based on InetAddressType"""
    defaultValue = 0


_ClrRrmPakRssiNtpIpAddressType_Object = MibScalar
clrRrmPakRssiNtpIpAddressType = _ClrRrmPakRssiNtpIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 10, 4),
    _ClrRrmPakRssiNtpIpAddressType_Type()
)
clrRrmPakRssiNtpIpAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clrRrmPakRssiNtpIpAddressType.setStatus("current")


class _ClrRrmPakRssiNtp_Type(InetAddress):
    """Custom type clrRrmPakRssiNtp based on InetAddress"""
    defaultValue = 0


_ClrRrmPakRssiNtp_Object = MibScalar
clrRrmPakRssiNtp = _ClrRrmPakRssiNtp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 10, 5),
    _ClrRrmPakRssiNtp_Type()
)
clrRrmPakRssiNtp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clrRrmPakRssiNtp.setStatus("current")
_ClrRrmNotificationVariable_ObjectIdentity = ObjectIdentity
clrRrmNotificationVariable = _ClrRrmNotificationVariable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 2)
)


class _ClrRrmApTransmitPowerLevel_Type(Integer32):
    """Custom type clrRrmApTransmitPowerLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-200, 200),
    )


_ClrRrmApTransmitPowerLevel_Type.__name__ = "Integer32"
_ClrRrmApTransmitPowerLevel_Object = MibScalar
clrRrmApTransmitPowerLevel = _ClrRrmApTransmitPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 2, 1),
    _ClrRrmApTransmitPowerLevel_Type()
)
clrRrmApTransmitPowerLevel.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    clrRrmApTransmitPowerLevel.setStatus("current")
_ClrRrmTimeStamp_Type = TimeStamp
_ClrRrmTimeStamp_Object = MibScalar
clrRrmTimeStamp = _ClrRrmTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 2, 2),
    _ClrRrmTimeStamp_Type()
)
clrRrmTimeStamp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    clrRrmTimeStamp.setStatus("current")


class _ClrRrmClientType_Type(Integer32):
    """Custom type clrRrmClientType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("data", 1),
          ("voice", 2))
    )


_ClrRrmClientType_Type.__name__ = "Integer32"
_ClrRrmClientType_Object = MibScalar
clrRrmClientType = _ClrRrmClientType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 2, 3),
    _ClrRrmClientType_Type()
)
clrRrmClientType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    clrRrmClientType.setStatus("current")
_ClrRrmRssiHistogramLength_Type = Unsigned32
_ClrRrmRssiHistogramLength_Object = MibScalar
clrRrmRssiHistogramLength = _ClrRrmRssiHistogramLength_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 2, 4),
    _ClrRrmRssiHistogramLength_Type()
)
clrRrmRssiHistogramLength.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    clrRrmRssiHistogramLength.setStatus("current")
_ClrRrmRssiHistogramMaxIndex_Type = Integer32
_ClrRrmRssiHistogramMaxIndex_Object = MibScalar
clrRrmRssiHistogramMaxIndex = _ClrRrmRssiHistogramMaxIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 2, 5),
    _ClrRrmRssiHistogramMaxIndex_Type()
)
clrRrmRssiHistogramMaxIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    clrRrmRssiHistogramMaxIndex.setStatus("current")
_ClrRrmRssiHistogramMinIndex_Type = Integer32
_ClrRrmRssiHistogramMinIndex_Object = MibScalar
clrRrmRssiHistogramMinIndex = _ClrRrmRssiHistogramMinIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 2, 6),
    _ClrRrmRssiHistogramMinIndex_Type()
)
clrRrmRssiHistogramMinIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    clrRrmRssiHistogramMinIndex.setStatus("current")
_ClrRrmRssiHistogramValues_Type = SnmpAdminString
_ClrRrmRssiHistogramValues_Object = MibScalar
clrRrmRssiHistogramValues = _ClrRrmRssiHistogramValues_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 2, 7),
    _ClrRrmRssiHistogramValues_Type()
)
clrRrmRssiHistogramValues.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    clrRrmRssiHistogramValues.setStatus("current")
_ClrRrmNeighborApCount_Type = Unsigned32
_ClrRrmNeighborApCount_Object = MibScalar
clrRrmNeighborApCount = _ClrRrmNeighborApCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 2, 8),
    _ClrRrmNeighborApCount_Type()
)
clrRrmNeighborApCount.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    clrRrmNeighborApCount.setStatus("current")
_ClrRrmNeighborApMacAddress_Type = SnmpAdminString
_ClrRrmNeighborApMacAddress_Object = MibScalar
clrRrmNeighborApMacAddress = _ClrRrmNeighborApMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 2, 9),
    _ClrRrmNeighborApMacAddress_Type()
)
clrRrmNeighborApMacAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    clrRrmNeighborApMacAddress.setStatus("current")
_ClrRrmNeighborApRssi_Type = SnmpAdminString
_ClrRrmNeighborApRssi_Object = MibScalar
clrRrmNeighborApRssi = _ClrRrmNeighborApRssi_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 2, 10),
    _ClrRrmNeighborApRssi_Type()
)
clrRrmNeighborApRssi.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    clrRrmNeighborApRssi.setStatus("current")
_ClrRrmNeighborApIfType_Type = SnmpAdminString
_ClrRrmNeighborApIfType_Object = MibScalar
clrRrmNeighborApIfType = _ClrRrmNeighborApIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 2, 11),
    _ClrRrmNeighborApIfType_Type()
)
clrRrmNeighborApIfType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    clrRrmNeighborApIfType.setStatus("current")
_ClrRrmSysMacAddress_Type = MacAddress
_ClrRrmSysMacAddress_Object = MibScalar
clrRrmSysMacAddress = _ClrRrmSysMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 2, 12),
    _ClrRrmSysMacAddress_Type()
)
clrRrmSysMacAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    clrRrmSysMacAddress.setStatus("current")
_ClrRrmSysIpAddress_Type = InetAddress
_ClrRrmSysIpAddress_Object = MibScalar
clrRrmSysIpAddress = _ClrRrmSysIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 2, 13),
    _ClrRrmSysIpAddress_Type()
)
clrRrmSysIpAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    clrRrmSysIpAddress.setStatus("current")
_CiscoLwappRrmMIBConform_ObjectIdentity = ObjectIdentity
ciscoLwappRrmMIBConform = _CiscoLwappRrmMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 2)
)
_CiscoLwappRrmMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoLwappRrmMIBCompliances = _CiscoLwappRrmMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 2, 1)
)
_CiscoLwappRrmMIBGroups_ObjectIdentity = ObjectIdentity
ciscoLwappRrmMIBGroups = _CiscoLwappRrmMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 2, 2)
)

# Managed Objects groups

ciscoLwappRrmConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 2, 2, 1)
)
ciscoLwappRrmConfigGroup.setObjects(
      *(("CISCO-LWAPP-RRM-MIB", "clrRrmParametersPicoCellMode"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmTupleRxSenseThresholdMin"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmTupleRxSenseThresholdMax"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmTupleRxSenseThreshold"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmTupleCcaSenseThresholdMin"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmTupleCcaSenseThresholdMax"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmTupleCcaSenseThreshold"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmTupleTransmitPowerLevelMin"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmTupleTransmitPowerLevelMax"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmTupleTransmitPowerLevel"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmTupleSetDefault"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmChannelDcaState"))
)
if mibBuilder.loadTexts:
    ciscoLwappRrmConfigGroup.setStatus("deprecated")

ciscoLwappRrmConfigGroupSup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 2, 2, 2)
)
ciscoLwappRrmConfigGroupSup1.setObjects(
      *(("CISCO-LWAPP-RRM-MIB", "clrRrmParametersChdEnable"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmParametersVoicePktCountThreshold"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmParametersVoicePktPercentThreshold"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmParametersVoiceRssiThreshold"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmParametersDataPktCountThreshold"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmParametersDataPktPercentThreshold"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmParametersDataRssiThreshold"))
)
if mibBuilder.loadTexts:
    ciscoLwappRrmConfigGroupSup1.setStatus("current")

ciscoLwappRrmConfigGroupSup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 2, 2, 3)
)
ciscoLwappRrmConfigGroupSup2.setObjects(
      *(("CISCO-LWAPP-RRM-MIB", "clrRrmChannelDcaState"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmParametersDcaChannelWidth"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmDcaDot11aOutdoorAPDca"))
)
if mibBuilder.loadTexts:
    ciscoLwappRrmConfigGroupSup2.setStatus("current")

ciscoLwappRrmConfigGroupSup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 2, 2, 4)
)
ciscoLwappRrmConfigGroupSup3.setObjects(
      *(("CISCO-LWAPP-RRM-MIB", "clrRrmParametersMaxTxPower"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmParametersMinTxPower"))
)
if mibBuilder.loadTexts:
    ciscoLwappRrmConfigGroupSup3.setStatus("current")

ciscoLwappRrmConfigGroupSup4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 2, 2, 5)
)
ciscoLwappRrmConfigGroupSup4.setObjects(
      *(("CISCO-LWAPP-RRM-MIB", "clrRrmDot11BandGrpMode"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmDot11BandGrpRestart"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmDot11BandMemberName"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmDot11BandMemberRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoLwappRrmConfigGroupSup4.setStatus("current")

ciscoLwappRrmGrpStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 2, 2, 6)
)
ciscoLwappRrmGrpStatusGroup.setObjects(
      *(("CISCO-LWAPP-RRM-MIB", "clrRrmDot11BandGrpLeaderIpAddressType"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmDot11BandGrpLeaderIpAddress"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmDot11BandGrpLeaderName"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmDot11BandGrpRole"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmDot11BandGrpLastUpdateTime"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmDot11BandGrpInterval"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmDot11BandMemberIsJoined"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmDot11BandMemberJoinFailureReason"))
)
if mibBuilder.loadTexts:
    ciscoLwappRrmGrpStatusGroup.setStatus("current")


# Notification objects

ciscoLwappDot11ClientCoverageHolePreAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 0, 1)
)
ciscoLwappDot11ClientCoverageHolePreAlarm.setObjects(
      *(("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientMacAddress"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcApMacAddress"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcIfType"),
        ("CISCO-LWAPP-AP-MIB", "cLApName"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmApTransmitPowerLevel"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmTimeStamp"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmClientType"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmRssiHistogramLength"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmRssiHistogramMaxIndex"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmRssiHistogramMinIndex"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmRssiHistogramValues"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmNeighborApCount"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmNeighborApMacAddress"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmNeighborApRssi"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmNeighborApIfType"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlanChdEnable"))
)
if mibBuilder.loadTexts:
    ciscoLwappDot11ClientCoverageHolePreAlarm.setStatus(
        "current"
    )

ciscoLwappRrmRfGroupLeaderChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 0, 2)
)
ciscoLwappRrmRfGroupLeaderChange.setObjects(
      *(("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcIfType"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmSysMacAddress"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmSysIpAddress"))
)
if mibBuilder.loadTexts:
    ciscoLwappRrmRfGroupLeaderChange.setStatus(
        "current"
    )

ciscoLwappRrmRfGroupMemberAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 0, 3)
)
ciscoLwappRrmRfGroupMemberAdded.setObjects(
      *(("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcIfType"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmSysMacAddress"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmSysIpAddress"))
)
if mibBuilder.loadTexts:
    ciscoLwappRrmRfGroupMemberAdded.setStatus(
        "current"
    )

ciscoLwappRrmRfGroupMemberRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 0, 4)
)
ciscoLwappRrmRfGroupMemberRemoved.setObjects(
      *(("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcIfType"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmSysMacAddress"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmSysIpAddress"))
)
if mibBuilder.loadTexts:
    ciscoLwappRrmRfGroupMemberRemoved.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

ciscoLwappRrmMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoLwappRrmMIBCompliance.setStatus(
        "deprecated"
    )

ciscoLwappRrmMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoLwappRrmMIBComplianceRev1.setStatus(
        "deprecated"
    )

ciscoLwappRrmMIBComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 2, 1, 3)
)
if mibBuilder.loadTexts:
    ciscoLwappRrmMIBComplianceRev2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-LWAPP-RRM-MIB",
    **{"ClrRrmTupleTuningRange": ClrRrmTupleTuningRange,
       "ciscoLwappRrmMIB": ciscoLwappRrmMIB,
       "ciscoLwappRrmMIBNotifs": ciscoLwappRrmMIBNotifs,
       "ciscoLwappDot11ClientCoverageHolePreAlarm": ciscoLwappDot11ClientCoverageHolePreAlarm,
       "ciscoLwappRrmRfGroupLeaderChange": ciscoLwappRrmRfGroupLeaderChange,
       "ciscoLwappRrmRfGroupMemberAdded": ciscoLwappRrmRfGroupMemberAdded,
       "ciscoLwappRrmRfGroupMemberRemoved": ciscoLwappRrmRfGroupMemberRemoved,
       "ciscoLwappRrmMIBObjects": ciscoLwappRrmMIBObjects,
       "clrRrmConfig": clrRrmConfig,
       "clrRrmParametersTable": clrRrmParametersTable,
       "clrRrmParametersEntry": clrRrmParametersEntry,
       "clrRrmParametersType": clrRrmParametersType,
       "clrRrmParametersPicoCellMode": clrRrmParametersPicoCellMode,
       "clrRrmParametersChdEnable": clrRrmParametersChdEnable,
       "clrRrmParametersVoicePktCountThreshold": clrRrmParametersVoicePktCountThreshold,
       "clrRrmParametersVoicePktPercentThreshold": clrRrmParametersVoicePktPercentThreshold,
       "clrRrmParametersVoiceRssiThreshold": clrRrmParametersVoiceRssiThreshold,
       "clrRrmParametersDataPktCountThreshold": clrRrmParametersDataPktCountThreshold,
       "clrRrmParametersDataPktPercentThreshold": clrRrmParametersDataPktPercentThreshold,
       "clrRrmParametersDataRssiThreshold": clrRrmParametersDataRssiThreshold,
       "clrRrmParametersDcaChannelWidth": clrRrmParametersDcaChannelWidth,
       "clrRrmParametersMaxTxPower": clrRrmParametersMaxTxPower,
       "clrRrmParametersMinTxPower": clrRrmParametersMinTxPower,
       "clrRrmParametersTpcVersion": clrRrmParametersTpcVersion,
       "clrRrmParametersMaxClients": clrRrmParametersMaxClients,
       "clrRrmParametersRssiCheckEnable": clrRrmParametersRssiCheckEnable,
       "clrRrmParametersRssiThreshold": clrRrmParametersRssiThreshold,
       "clrRrmParametersOptRoamEnable": clrRrmParametersOptRoamEnable,
       "clrRrmParametersOptRoamDataRate": clrRrmParametersOptRoamDataRate,
       "clrRrmParametersOptRoamInterval": clrRrmParametersOptRoamInterval,
       "clrRrmTupleTable": clrRrmTupleTable,
       "clrRrmTupleEntry": clrRrmTupleEntry,
       "clrRrmTupleRxSenseThresholdMin": clrRrmTupleRxSenseThresholdMin,
       "clrRrmTupleRxSenseThresholdMax": clrRrmTupleRxSenseThresholdMax,
       "clrRrmTupleRxSenseThreshold": clrRrmTupleRxSenseThreshold,
       "clrRrmTupleCcaSenseThresholdMin": clrRrmTupleCcaSenseThresholdMin,
       "clrRrmTupleCcaSenseThresholdMax": clrRrmTupleCcaSenseThresholdMax,
       "clrRrmTupleCcaSenseThreshold": clrRrmTupleCcaSenseThreshold,
       "clrRrmTupleTransmitPowerLevelMin": clrRrmTupleTransmitPowerLevelMin,
       "clrRrmTupleTransmitPowerLevelMax": clrRrmTupleTransmitPowerLevelMax,
       "clrRrmTupleTransmitPowerLevel": clrRrmTupleTransmitPowerLevel,
       "clrRrmTupleSetDefault": clrRrmTupleSetDefault,
       "clrRrmChannelTable": clrRrmChannelTable,
       "clrRrmChannelEntry": clrRrmChannelEntry,
       "clrRrmChannelNum": clrRrmChannelNum,
       "clrRrmChannelDcaState": clrRrmChannelDcaState,
       "clrRrmDot11BandGrpTable": clrRrmDot11BandGrpTable,
       "clrRrmDot11BandGrpEntry": clrRrmDot11BandGrpEntry,
       "clrRrmDot11BandGrpLeaderIpAddressType": clrRrmDot11BandGrpLeaderIpAddressType,
       "clrRrmDot11BandGrpLeaderIpAddress": clrRrmDot11BandGrpLeaderIpAddress,
       "clrRrmDot11BandGrpLeaderName": clrRrmDot11BandGrpLeaderName,
       "clrRrmDot11BandGrpMode": clrRrmDot11BandGrpMode,
       "clrRrmDot11BandGrpRole": clrRrmDot11BandGrpRole,
       "clrRrmDot11BandGrpRestart": clrRrmDot11BandGrpRestart,
       "clrRrmDot11BandGrpLastUpdateTime": clrRrmDot11BandGrpLastUpdateTime,
       "clrRrmDot11BandGrpInterval": clrRrmDot11BandGrpInterval,
       "clrRrmDot11BandGrpMemberTable": clrRrmDot11BandGrpMemberTable,
       "clrRrmDot11BandGrpMemberEntry": clrRrmDot11BandGrpMemberEntry,
       "clrRrmDot11BandMemberIpAddressType": clrRrmDot11BandMemberIpAddressType,
       "clrRrmDot11BandMemberIpAddress": clrRrmDot11BandMemberIpAddress,
       "clrRrmDot11BandMemberName": clrRrmDot11BandMemberName,
       "clrRrmDot11BandMemberIsJoined": clrRrmDot11BandMemberIsJoined,
       "clrRrmDot11BandMemberJoinFailureReason": clrRrmDot11BandMemberJoinFailureReason,
       "clrRrmDot11BandMemberRowStatus": clrRrmDot11BandMemberRowStatus,
       "clrRrmDcaConfig": clrRrmDcaConfig,
       "clrRrmDcaDot11aOutdoorAPDca": clrRrmDcaDot11aOutdoorAPDca,
       "clrRrmRfGroupingPriority": clrRrmRfGroupingPriority,
       "clrRrmPakRssiConfig": clrRrmPakRssiConfig,
       "clrRrmPakRssiEnable": clrRrmPakRssiEnable,
       "clrRrmPakRssiThreshold": clrRrmPakRssiThreshold,
       "clrRrmPakRssiThresholdTrigger": clrRrmPakRssiThresholdTrigger,
       "clrRrmPakRssiNtpIpAddressType": clrRrmPakRssiNtpIpAddressType,
       "clrRrmPakRssiNtp": clrRrmPakRssiNtp,
       "clrRrmNotificationVariable": clrRrmNotificationVariable,
       "clrRrmApTransmitPowerLevel": clrRrmApTransmitPowerLevel,
       "clrRrmTimeStamp": clrRrmTimeStamp,
       "clrRrmClientType": clrRrmClientType,
       "clrRrmRssiHistogramLength": clrRrmRssiHistogramLength,
       "clrRrmRssiHistogramMaxIndex": clrRrmRssiHistogramMaxIndex,
       "clrRrmRssiHistogramMinIndex": clrRrmRssiHistogramMinIndex,
       "clrRrmRssiHistogramValues": clrRrmRssiHistogramValues,
       "clrRrmNeighborApCount": clrRrmNeighborApCount,
       "clrRrmNeighborApMacAddress": clrRrmNeighborApMacAddress,
       "clrRrmNeighborApRssi": clrRrmNeighborApRssi,
       "clrRrmNeighborApIfType": clrRrmNeighborApIfType,
       "clrRrmSysMacAddress": clrRrmSysMacAddress,
       "clrRrmSysIpAddress": clrRrmSysIpAddress,
       "ciscoLwappRrmMIBConform": ciscoLwappRrmMIBConform,
       "ciscoLwappRrmMIBCompliances": ciscoLwappRrmMIBCompliances,
       "ciscoLwappRrmMIBCompliance": ciscoLwappRrmMIBCompliance,
       "ciscoLwappRrmMIBComplianceRev1": ciscoLwappRrmMIBComplianceRev1,
       "ciscoLwappRrmMIBComplianceRev2": ciscoLwappRrmMIBComplianceRev2,
       "ciscoLwappRrmMIBGroups": ciscoLwappRrmMIBGroups,
       "ciscoLwappRrmConfigGroup": ciscoLwappRrmConfigGroup,
       "ciscoLwappRrmConfigGroupSup1": ciscoLwappRrmConfigGroupSup1,
       "ciscoLwappRrmConfigGroupSup2": ciscoLwappRrmConfigGroupSup2,
       "ciscoLwappRrmConfigGroupSup3": ciscoLwappRrmConfigGroupSup3,
       "ciscoLwappRrmConfigGroupSup4": ciscoLwappRrmConfigGroupSup4,
       "ciscoLwappRrmGrpStatusGroup": ciscoLwappRrmGrpStatusGroup}
)
