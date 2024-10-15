# SNMP MIB module (CISCO-LWAPP-RF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-LWAPP-RF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:04:56 2024
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

(CLApIfType,) = mibBuilder.importSymbols(
    "CISCO-LWAPP-TC-MIB",
    "CLApIfType")

(cLAPGroupName,) = mibBuilder.importSymbols(
    "CISCO-LWAPP-WLAN-MIB",
    "cLAPGroupName")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

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
 RowStatus,
 StorageType,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoLwappRFMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 778)
)
ciscoLwappRFMIB.setRevisions(
        ("2012-04-27 00:00",
         "2012-01-27 00:00",
         "2011-11-01 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CiscoLwappRFApDataRates(Integer32, TextualConvention):
    status = "current"
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
        *(("disabled", 0),
          ("mandatoryRate", 2),
          ("notApplicable", 3),
          ("supported", 1))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoLwappRFMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoLwappRFMIBNotifs = _CiscoLwappRFMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 778, 0)
)
_CiscoLwappRFMIBObjects_ObjectIdentity = ObjectIdentity
ciscoLwappRFMIBObjects = _CiscoLwappRFMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 778, 1)
)
_CiscoLwappRFConfig_ObjectIdentity = ObjectIdentity
ciscoLwappRFConfig = _CiscoLwappRFConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 778, 1, 1)
)
_CLAPGroupsRFProfileTable_Object = MibTable
cLAPGroupsRFProfileTable = _CLAPGroupsRFProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 778, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cLAPGroupsRFProfileTable.setStatus("current")
_CLAPGroupsRFProfileEntry_Object = MibTableRow
cLAPGroupsRFProfileEntry = _CLAPGroupsRFProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 778, 1, 1, 1, 1)
)
cLAPGroupsRFProfileEntry.setIndexNames(
    (0, "CISCO-LWAPP-WLAN-MIB", "cLAPGroupName"),
)
if mibBuilder.loadTexts:
    cLAPGroupsRFProfileEntry.setStatus("current")


class _CLAPGroups802dot11bgRFProfileName_Type(SnmpAdminString):
    """Custom type cLAPGroups802dot11bgRFProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CLAPGroups802dot11bgRFProfileName_Type.__name__ = "SnmpAdminString"
_CLAPGroups802dot11bgRFProfileName_Object = MibTableColumn
cLAPGroups802dot11bgRFProfileName = _CLAPGroups802dot11bgRFProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 778, 1, 1, 1, 1, 1),
    _CLAPGroups802dot11bgRFProfileName_Type()
)
cLAPGroups802dot11bgRFProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLAPGroups802dot11bgRFProfileName.setStatus("current")


class _CLAPGroups802dot11aRFProfileName_Type(SnmpAdminString):
    """Custom type cLAPGroups802dot11aRFProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CLAPGroups802dot11aRFProfileName_Type.__name__ = "SnmpAdminString"
_CLAPGroups802dot11aRFProfileName_Object = MibTableColumn
cLAPGroups802dot11aRFProfileName = _CLAPGroups802dot11aRFProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 778, 1, 1, 1, 1, 2),
    _CLAPGroups802dot11aRFProfileName_Type()
)
cLAPGroups802dot11aRFProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLAPGroups802dot11aRFProfileName.setStatus("current")
_CLRFProfileTable_Object = MibTable
cLRFProfileTable = _CLRFProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 778, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cLRFProfileTable.setStatus("current")
_CLRFProfileEntry_Object = MibTableRow
cLRFProfileEntry = _CLRFProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 778, 1, 1, 2, 1)
)
cLRFProfileEntry.setIndexNames(
    (0, "CISCO-LWAPP-RF-MIB", "cLRFProfileName"),
)
if mibBuilder.loadTexts:
    cLRFProfileEntry.setStatus("current")


class _CLRFProfileName_Type(SnmpAdminString):
    """Custom type cLRFProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CLRFProfileName_Type.__name__ = "SnmpAdminString"
_CLRFProfileName_Object = MibTableColumn
cLRFProfileName = _CLRFProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 778, 1, 1, 2, 1, 1),
    _CLRFProfileName_Type()
)
cLRFProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLRFProfileName.setStatus("current")


class _CLRFProfileDescr_Type(SnmpAdminString):
    """Custom type cLRFProfileDescr based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CLRFProfileDescr_Type.__name__ = "SnmpAdminString"
_CLRFProfileDescr_Object = MibTableColumn
cLRFProfileDescr = _CLRFProfileDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 778, 1, 1, 2, 1, 2),
    _CLRFProfileDescr_Type()
)
cLRFProfileDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLRFProfileDescr.setStatus("current")


class _CLRFProfileTransmitPowerMin_Type(Integer32):
    """Custom type cLRFProfileTransmitPowerMin based on Integer32"""
    defaultValue = -10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-10, 30),
    )


_CLRFProfileTransmitPowerMin_Type.__name__ = "Integer32"
_CLRFProfileTransmitPowerMin_Object = MibTableColumn
cLRFProfileTransmitPowerMin = _CLRFProfileTransmitPowerMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 778, 1, 1, 2, 1, 3),
    _CLRFProfileTransmitPowerMin_Type()
)
cLRFProfileTransmitPowerMin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLRFProfileTransmitPowerMin.setStatus("current")
if mibBuilder.loadTexts:
    cLRFProfileTransmitPowerMin.setUnits("dbm")


class _CLRFProfileTransmitPowerMax_Type(Integer32):
    """Custom type cLRFProfileTransmitPowerMax based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-10, 30),
    )


_CLRFProfileTransmitPowerMax_Type.__name__ = "Integer32"
_CLRFProfileTransmitPowerMax_Object = MibTableColumn
cLRFProfileTransmitPowerMax = _CLRFProfileTransmitPowerMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 778, 1, 1, 2, 1, 4),
    _CLRFProfileTransmitPowerMax_Type()
)
cLRFProfileTransmitPowerMax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLRFProfileTransmitPowerMax.setStatus("current")
if mibBuilder.loadTexts:
    cLRFProfileTransmitPowerMax.setUnits("dbm")


class _CLRFProfileTransmitPowerThresholdV1_Type(Integer32):
    """Custom type cLRFProfileTransmitPowerThresholdV1 based on Integer32"""
    defaultValue = -70

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-80, -50),
    )


_CLRFProfileTransmitPowerThresholdV1_Type.__name__ = "Integer32"
_CLRFProfileTransmitPowerThresholdV1_Object = MibTableColumn
cLRFProfileTransmitPowerThresholdV1 = _CLRFProfileTransmitPowerThresholdV1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 778, 1, 1, 2, 1, 5),
    _CLRFProfileTransmitPowerThresholdV1_Type()
)
cLRFProfileTransmitPowerThresholdV1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLRFProfileTransmitPowerThresholdV1.setStatus("current")
if mibBuilder.loadTexts:
    cLRFProfileTransmitPowerThresholdV1.setUnits("dbm")


class _CLRFProfileTransmitPowerThresholdV2_Type(Integer32):
    """Custom type cLRFProfileTransmitPowerThresholdV2 based on Integer32"""
    defaultValue = -67

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-80, -50),
    )


_CLRFProfileTransmitPowerThresholdV2_Type.__name__ = "Integer32"
_CLRFProfileTransmitPowerThresholdV2_Object = MibTableColumn
cLRFProfileTransmitPowerThresholdV2 = _CLRFProfileTransmitPowerThresholdV2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 778, 1, 1, 2, 1, 6),
    _CLRFProfileTransmitPowerThresholdV2_Type()
)
cLRFProfileTransmitPowerThresholdV2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLRFProfileTransmitPowerThresholdV2.setStatus("current")
if mibBuilder.loadTexts:
    cLRFProfileTransmitPowerThresholdV2.setUnits("dbm")


class _CLRFProfileDataRate1Mbps_Type(CiscoLwappRFApDataRates):
    """Custom type cLRFProfileDataRate1Mbps based on CiscoLwappRFApDataRates"""


_CLRFProfileDataRate1Mbps_Object = MibTableColumn
cLRFProfileDataRate1Mbps = _CLRFProfileDataRate1Mbps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 778, 1, 1, 2, 1, 7),
    _CLRFProfileDataRate1Mbps_Type()
)
cLRFProfileDataRate1Mbps.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLRFProfileDataRate1Mbps.setStatus("current")


class _CLRFProfileDataRate2Mbps_Type(CiscoLwappRFApDataRates):
    """Custom type cLRFProfileDataRate2Mbps based on CiscoLwappRFApDataRates"""


_CLRFProfileDataRate2Mbps_Object = MibTableColumn
cLRFProfileDataRate2Mbps = _CLRFProfileDataRate2Mbps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 778, 1, 1, 2, 1, 8),
    _CLRFProfileDataRate2Mbps_Type()
)
cLRFProfileDataRate2Mbps.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLRFProfileDataRate2Mbps.setStatus("current")


class _CLRFProfileDataRate5AndHalfMbps_Type(CiscoLwappRFApDataRates):
    """Custom type cLRFProfileDataRate5AndHalfMbps based on CiscoLwappRFApDataRates"""


_CLRFProfileDataRate5AndHalfMbps_Object = MibTableColumn
cLRFProfileDataRate5AndHalfMbps = _CLRFProfileDataRate5AndHalfMbps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 778, 1, 1, 2, 1, 9),
    _CLRFProfileDataRate5AndHalfMbps_Type()
)
cLRFProfileDataRate5AndHalfMbps.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLRFProfileDataRate5AndHalfMbps.setStatus("current")


class _CLRFProfileDataRate11Mbps_Type(CiscoLwappRFApDataRates):
    """Custom type cLRFProfileDataRate11Mbps based on CiscoLwappRFApDataRates"""


_CLRFProfileDataRate11Mbps_Object = MibTableColumn
cLRFProfileDataRate11Mbps = _CLRFProfileDataRate11Mbps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 778, 1, 1, 2, 1, 10),
    _CLRFProfileDataRate11Mbps_Type()
)
cLRFProfileDataRate11Mbps.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLRFProfileDataRate11Mbps.setStatus("current")


class _CLRFProfileDataRate6Mbps_Type(CiscoLwappRFApDataRates):
    """Custom type cLRFProfileDataRate6Mbps based on CiscoLwappRFApDataRates"""


_CLRFProfileDataRate6Mbps_Object = MibTableColumn
cLRFProfileDataRate6Mbps = _CLRFProfileDataRate6Mbps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 778, 1, 1, 2, 1, 11),
    _CLRFProfileDataRate6Mbps_Type()
)
cLRFProfileDataRate6Mbps.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLRFProfileDataRate6Mbps.setStatus("current")


class _CLRFProfileDataRate9Mbps_Type(CiscoLwappRFApDataRates):
    """Custom type cLRFProfileDataRate9Mbps based on CiscoLwappRFApDataRates"""


_CLRFProfileDataRate9Mbps_Object = MibTableColumn
cLRFProfileDataRate9Mbps = _CLRFProfileDataRate9Mbps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 778, 1, 1, 2, 1, 12),
    _CLRFProfileDataRate9Mbps_Type()
)
cLRFProfileDataRate9Mbps.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLRFProfileDataRate9Mbps.setStatus("current")


class _CLRFProfileDataRate12Mbps_Type(CiscoLwappRFApDataRates):
    """Custom type cLRFProfileDataRate12Mbps based on CiscoLwappRFApDataRates"""


_CLRFProfileDataRate12Mbps_Object = MibTableColumn
cLRFProfileDataRate12Mbps = _CLRFProfileDataRate12Mbps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 778, 1, 1, 2, 1, 13),
    _CLRFProfileDataRate12Mbps_Type()
)
cLRFProfileDataRate12Mbps.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLRFProfileDataRate12Mbps.setStatus("current")


class _CLRFProfileDataRate18Mbps_Type(CiscoLwappRFApDataRates):
    """Custom type cLRFProfileDataRate18Mbps based on CiscoLwappRFApDataRates"""


_CLRFProfileDataRate18Mbps_Object = MibTableColumn
cLRFProfileDataRate18Mbps = _CLRFProfileDataRate18Mbps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 778, 1, 1, 2, 1, 14),
    _CLRFProfileDataRate18Mbps_Type()
)
cLRFProfileDataRate18Mbps.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLRFProfileDataRate18Mbps.setStatus("current")


class _CLRFProfileDataRate24Mbps_Type(CiscoLwappRFApDataRates):
    """Custom type cLRFProfileDataRate24Mbps based on CiscoLwappRFApDataRates"""


_CLRFProfileDataRate24Mbps_Object = MibTableColumn
cLRFProfileDataRate24Mbps = _CLRFProfileDataRate24Mbps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 778, 1, 1, 2, 1, 15),
    _CLRFProfileDataRate24Mbps_Type()
)
cLRFProfileDataRate24Mbps.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLRFProfileDataRate24Mbps.setStatus("current")


class _CLRFProfileDataRate36Mbps_Type(CiscoLwappRFApDataRates):
    """Custom type cLRFProfileDataRate36Mbps based on CiscoLwappRFApDataRates"""


_CLRFProfileDataRate36Mbps_Object = MibTableColumn
cLRFProfileDataRate36Mbps = _CLRFProfileDataRate36Mbps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 778, 1, 1, 2, 1, 16),
    _CLRFProfileDataRate36Mbps_Type()
)
cLRFProfileDataRate36Mbps.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLRFProfileDataRate36Mbps.setStatus("current")


class _CLRFProfileDataRate48Mbps_Type(CiscoLwappRFApDataRates):
    """Custom type cLRFProfileDataRate48Mbps based on CiscoLwappRFApDataRates"""


_CLRFProfileDataRate48Mbps_Object = MibTableColumn
cLRFProfileDataRate48Mbps = _CLRFProfileDataRate48Mbps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 778, 1, 1, 2, 1, 17),
    _CLRFProfileDataRate48Mbps_Type()
)
cLRFProfileDataRate48Mbps.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLRFProfileDataRate48Mbps.setStatus("current")


class _CLRFProfileDataRate54Mbps_Type(CiscoLwappRFApDataRates):
    """Custom type cLRFProfileDataRate54Mbps based on CiscoLwappRFApDataRates"""


_CLRFProfileDataRate54Mbps_Object = MibTableColumn
cLRFProfileDataRate54Mbps = _CLRFProfileDataRate54Mbps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 778, 1, 1, 2, 1, 18),
    _CLRFProfileDataRate54Mbps_Type()
)
cLRFProfileDataRate54Mbps.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLRFProfileDataRate54Mbps.setStatus("current")
_CLRFProfileRadioType_Type = CLApIfType
_CLRFProfileRadioType_Object = MibTableColumn
cLRFProfileRadioType = _CLRFProfileRadioType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 778, 1, 1, 2, 1, 19),
    _CLRFProfileRadioType_Type()
)
cLRFProfileRadioType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLRFProfileRadioType.setStatus("current")


class _CLRFProfileStorageType_Type(StorageType):
    """Custom type cLRFProfileStorageType based on StorageType"""


_CLRFProfileStorageType_Object = MibTableColumn
cLRFProfileStorageType = _CLRFProfileStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 778, 1, 1, 2, 1, 20),
    _CLRFProfileStorageType_Type()
)
cLRFProfileStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLRFProfileStorageType.setStatus("current")
_CLRFProfileRowStatus_Type = RowStatus
_CLRFProfileRowStatus_Object = MibTableColumn
cLRFProfileRowStatus = _CLRFProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 778, 1, 1, 2, 1, 21),
    _CLRFProfileRowStatus_Type()
)
cLRFProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLRFProfileRowStatus.setStatus("current")


class _CLRFProfileHighDensityMaxRadioClients_Type(Unsigned32):
    """Custom type cLRFProfileHighDensityMaxRadioClients based on Unsigned32"""
    defaultValue = 200


_CLRFProfileHighDensityMaxRadioClients_Object = MibTableColumn
cLRFProfileHighDensityMaxRadioClients = _CLRFProfileHighDensityMaxRadioClients_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 778, 1, 1, 2, 1, 22),
    _CLRFProfileHighDensityMaxRadioClients_Type()
)
cLRFProfileHighDensityMaxRadioClients.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLRFProfileHighDensityMaxRadioClients.setStatus("current")


class _CLRFProfileBandSelectProbeResponse_Type(TruthValue):
    """Custom type cLRFProfileBandSelectProbeResponse based on TruthValue"""


_CLRFProfileBandSelectProbeResponse_Object = MibTableColumn
cLRFProfileBandSelectProbeResponse = _CLRFProfileBandSelectProbeResponse_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 778, 1, 1, 2, 1, 23),
    _CLRFProfileBandSelectProbeResponse_Type()
)
cLRFProfileBandSelectProbeResponse.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLRFProfileBandSelectProbeResponse.setStatus("current")


class _CLRFProfileBandSelectCycleCount_Type(Unsigned32):
    """Custom type cLRFProfileBandSelectCycleCount based on Unsigned32"""
    defaultValue = 2


_CLRFProfileBandSelectCycleCount_Object = MibTableColumn
cLRFProfileBandSelectCycleCount = _CLRFProfileBandSelectCycleCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 778, 1, 1, 2, 1, 24),
    _CLRFProfileBandSelectCycleCount_Type()
)
cLRFProfileBandSelectCycleCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLRFProfileBandSelectCycleCount.setStatus("current")


class _CLRFProfileBandSelectCycleThreshold_Type(Unsigned32):
    """Custom type cLRFProfileBandSelectCycleThreshold based on Unsigned32"""
    defaultValue = 200


_CLRFProfileBandSelectCycleThreshold_Object = MibTableColumn
cLRFProfileBandSelectCycleThreshold = _CLRFProfileBandSelectCycleThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 778, 1, 1, 2, 1, 25),
    _CLRFProfileBandSelectCycleThreshold_Type()
)
cLRFProfileBandSelectCycleThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLRFProfileBandSelectCycleThreshold.setStatus("current")


class _CLRFProfileBandSelectExpireSuppression_Type(Unsigned32):
    """Custom type cLRFProfileBandSelectExpireSuppression based on Unsigned32"""
    defaultValue = 20


_CLRFProfileBandSelectExpireSuppression_Object = MibTableColumn
cLRFProfileBandSelectExpireSuppression = _CLRFProfileBandSelectExpireSuppression_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 778, 1, 1, 2, 1, 26),
    _CLRFProfileBandSelectExpireSuppression_Type()
)
cLRFProfileBandSelectExpireSuppression.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLRFProfileBandSelectExpireSuppression.setStatus("current")


class _CLRFProfileBandSelectExpireDualBand_Type(Unsigned32):
    """Custom type cLRFProfileBandSelectExpireDualBand based on Unsigned32"""
    defaultValue = 60


_CLRFProfileBandSelectExpireDualBand_Object = MibTableColumn
cLRFProfileBandSelectExpireDualBand = _CLRFProfileBandSelectExpireDualBand_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 778, 1, 1, 2, 1, 27),
    _CLRFProfileBandSelectExpireDualBand_Type()
)
cLRFProfileBandSelectExpireDualBand.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLRFProfileBandSelectExpireDualBand.setStatus("current")


class _CLRFProfileBandSelectClientRSSI_Type(Integer32):
    """Custom type cLRFProfileBandSelectClientRSSI based on Integer32"""
    defaultValue = -80


_CLRFProfileBandSelectClientRSSI_Object = MibTableColumn
cLRFProfileBandSelectClientRSSI = _CLRFProfileBandSelectClientRSSI_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 778, 1, 1, 2, 1, 28),
    _CLRFProfileBandSelectClientRSSI_Type()
)
cLRFProfileBandSelectClientRSSI.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLRFProfileBandSelectClientRSSI.setStatus("current")
if mibBuilder.loadTexts:
    cLRFProfileBandSelectClientRSSI.setUnits("dbm")


class _CLRFProfileLoadBalancingWindowSize_Type(Unsigned32):
    """Custom type cLRFProfileLoadBalancingWindowSize based on Unsigned32"""
    defaultValue = 5


_CLRFProfileLoadBalancingWindowSize_Object = MibTableColumn
cLRFProfileLoadBalancingWindowSize = _CLRFProfileLoadBalancingWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 778, 1, 1, 2, 1, 29),
    _CLRFProfileLoadBalancingWindowSize_Type()
)
cLRFProfileLoadBalancingWindowSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLRFProfileLoadBalancingWindowSize.setStatus("current")


class _CLRFProfileLoadBalancingDenialCount_Type(Unsigned32):
    """Custom type cLRFProfileLoadBalancingDenialCount based on Unsigned32"""
    defaultValue = 3


_CLRFProfileLoadBalancingDenialCount_Object = MibTableColumn
cLRFProfileLoadBalancingDenialCount = _CLRFProfileLoadBalancingDenialCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 778, 1, 1, 2, 1, 30),
    _CLRFProfileLoadBalancingDenialCount_Type()
)
cLRFProfileLoadBalancingDenialCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLRFProfileLoadBalancingDenialCount.setStatus("current")


class _CLRFProfileCHDDataRSSIThreshold_Type(Integer32):
    """Custom type cLRFProfileCHDDataRSSIThreshold based on Integer32"""
    defaultValue = -80


_CLRFProfileCHDDataRSSIThreshold_Object = MibTableColumn
cLRFProfileCHDDataRSSIThreshold = _CLRFProfileCHDDataRSSIThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 778, 1, 1, 2, 1, 31),
    _CLRFProfileCHDDataRSSIThreshold_Type()
)
cLRFProfileCHDDataRSSIThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLRFProfileCHDDataRSSIThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cLRFProfileCHDDataRSSIThreshold.setUnits("dbm")


class _CLRFProfileCHDVoiceRSSIThreshold_Type(Integer32):
    """Custom type cLRFProfileCHDVoiceRSSIThreshold based on Integer32"""
    defaultValue = -80


_CLRFProfileCHDVoiceRSSIThreshold_Object = MibTableColumn
cLRFProfileCHDVoiceRSSIThreshold = _CLRFProfileCHDVoiceRSSIThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 778, 1, 1, 2, 1, 32),
    _CLRFProfileCHDVoiceRSSIThreshold_Type()
)
cLRFProfileCHDVoiceRSSIThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLRFProfileCHDVoiceRSSIThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cLRFProfileCHDVoiceRSSIThreshold.setUnits("dbm")


class _CLRFProfileCHDClientExceptionLevel_Type(Unsigned32):
    """Custom type cLRFProfileCHDClientExceptionLevel based on Unsigned32"""
    defaultValue = 3


_CLRFProfileCHDClientExceptionLevel_Object = MibTableColumn
cLRFProfileCHDClientExceptionLevel = _CLRFProfileCHDClientExceptionLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 778, 1, 1, 2, 1, 33),
    _CLRFProfileCHDClientExceptionLevel_Type()
)
cLRFProfileCHDClientExceptionLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLRFProfileCHDClientExceptionLevel.setStatus("current")


class _CLRFProfileCHDCoverageExceptionLevel_Type(Unsigned32):
    """Custom type cLRFProfileCHDCoverageExceptionLevel based on Unsigned32"""
    defaultValue = 25


_CLRFProfileCHDCoverageExceptionLevel_Object = MibTableColumn
cLRFProfileCHDCoverageExceptionLevel = _CLRFProfileCHDCoverageExceptionLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 778, 1, 1, 2, 1, 34),
    _CLRFProfileCHDCoverageExceptionLevel_Type()
)
cLRFProfileCHDCoverageExceptionLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLRFProfileCHDCoverageExceptionLevel.setStatus("current")


class _CLRFProfileMulticastDataRate_Type(Unsigned32):
    """Custom type cLRFProfileMulticastDataRate based on Unsigned32"""
    defaultValue = 0


_CLRFProfileMulticastDataRate_Object = MibTableColumn
cLRFProfileMulticastDataRate = _CLRFProfileMulticastDataRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 778, 1, 1, 2, 1, 35),
    _CLRFProfileMulticastDataRate_Type()
)
cLRFProfileMulticastDataRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLRFProfileMulticastDataRate.setStatus("current")


class _CLRFProfile11nOnly_Type(TruthValue):
    """Custom type cLRFProfile11nOnly based on TruthValue"""


_CLRFProfile11nOnly_Object = MibTableColumn
cLRFProfile11nOnly = _CLRFProfile11nOnly_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 778, 1, 1, 2, 1, 36),
    _CLRFProfile11nOnly_Type()
)
cLRFProfile11nOnly.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLRFProfile11nOnly.setStatus("current")
_CLRFProfileHDClientTrapThreshold_Type = Unsigned32
_CLRFProfileHDClientTrapThreshold_Object = MibTableColumn
cLRFProfileHDClientTrapThreshold = _CLRFProfileHDClientTrapThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 778, 1, 1, 2, 1, 37),
    _CLRFProfileHDClientTrapThreshold_Type()
)
cLRFProfileHDClientTrapThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLRFProfileHDClientTrapThreshold.setStatus("current")


class _CLRFProfileInterferenceThreshold_Type(Unsigned32):
    """Custom type cLRFProfileInterferenceThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CLRFProfileInterferenceThreshold_Type.__name__ = "Unsigned32"
_CLRFProfileInterferenceThreshold_Object = MibTableColumn
cLRFProfileInterferenceThreshold = _CLRFProfileInterferenceThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 778, 1, 1, 2, 1, 38),
    _CLRFProfileInterferenceThreshold_Type()
)
cLRFProfileInterferenceThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLRFProfileInterferenceThreshold.setStatus("current")


class _CLRFProfileNoiseThreshold_Type(Integer32):
    """Custom type cLRFProfileNoiseThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-127, 0),
    )


_CLRFProfileNoiseThreshold_Type.__name__ = "Integer32"
_CLRFProfileNoiseThreshold_Object = MibTableColumn
cLRFProfileNoiseThreshold = _CLRFProfileNoiseThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 778, 1, 1, 2, 1, 39),
    _CLRFProfileNoiseThreshold_Type()
)
cLRFProfileNoiseThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLRFProfileNoiseThreshold.setStatus("current")


class _CLRFProfileUtilizationThreshold_Type(Unsigned32):
    """Custom type cLRFProfileUtilizationThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CLRFProfileUtilizationThreshold_Type.__name__ = "Unsigned32"
_CLRFProfileUtilizationThreshold_Object = MibTableColumn
cLRFProfileUtilizationThreshold = _CLRFProfileUtilizationThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 778, 1, 1, 2, 1, 40),
    _CLRFProfileUtilizationThreshold_Type()
)
cLRFProfileUtilizationThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLRFProfileUtilizationThreshold.setStatus("current")
_CLRFProfileDCAForeignContribution_Type = TruthValue
_CLRFProfileDCAForeignContribution_Object = MibTableColumn
cLRFProfileDCAForeignContribution = _CLRFProfileDCAForeignContribution_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 778, 1, 1, 2, 1, 41),
    _CLRFProfileDCAForeignContribution_Type()
)
cLRFProfileDCAForeignContribution.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLRFProfileDCAForeignContribution.setStatus("current")


class _CLRFProfileDCAChannelWidth_Type(Integer32):
    """Custom type cLRFProfileDCAChannelWidth based on Integer32"""
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


_CLRFProfileDCAChannelWidth_Type.__name__ = "Integer32"
_CLRFProfileDCAChannelWidth_Object = MibTableColumn
cLRFProfileDCAChannelWidth = _CLRFProfileDCAChannelWidth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 778, 1, 1, 2, 1, 42),
    _CLRFProfileDCAChannelWidth_Type()
)
cLRFProfileDCAChannelWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLRFProfileDCAChannelWidth.setStatus("current")


class _CLRFProfileDCAChannelList_Type(SnmpAdminString):
    """Custom type cLRFProfileDCAChannelList based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 500),
    )


_CLRFProfileDCAChannelList_Type.__name__ = "SnmpAdminString"
_CLRFProfileDCAChannelList_Object = MibTableColumn
cLRFProfileDCAChannelList = _CLRFProfileDCAChannelList_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 778, 1, 1, 2, 1, 43),
    _CLRFProfileDCAChannelList_Type()
)
cLRFProfileDCAChannelList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLRFProfileDCAChannelList.setStatus("current")


class _CLRFProfileRxSopThreshold_Type(Integer32):
    """Custom type cLRFProfileRxSopThreshold based on Integer32"""
    defaultValue = 0

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
        *(("auto", 0),
          ("high", 3),
          ("low", 1),
          ("medium", 2))
    )


_CLRFProfileRxSopThreshold_Type.__name__ = "Integer32"
_CLRFProfileRxSopThreshold_Object = MibTableColumn
cLRFProfileRxSopThreshold = _CLRFProfileRxSopThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 778, 1, 1, 2, 1, 44),
    _CLRFProfileRxSopThreshold_Type()
)
cLRFProfileRxSopThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLRFProfileRxSopThreshold.setStatus("current")
_CLRFProfileMcsDataRateTable_Object = MibTable
cLRFProfileMcsDataRateTable = _CLRFProfileMcsDataRateTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 778, 1, 1, 3)
)
if mibBuilder.loadTexts:
    cLRFProfileMcsDataRateTable.setStatus("current")
_CLRFProfileMcsDataRateEntry_Object = MibTableRow
cLRFProfileMcsDataRateEntry = _CLRFProfileMcsDataRateEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 778, 1, 1, 3, 1)
)
cLRFProfileMcsDataRateEntry.setIndexNames(
    (0, "CISCO-LWAPP-RF-MIB", "cLRFProfileMcsName"),
    (0, "CISCO-LWAPP-RF-MIB", "cLRFProfileMcsRate"),
)
if mibBuilder.loadTexts:
    cLRFProfileMcsDataRateEntry.setStatus("current")


class _CLRFProfileMcsName_Type(SnmpAdminString):
    """Custom type cLRFProfileMcsName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CLRFProfileMcsName_Type.__name__ = "SnmpAdminString"
_CLRFProfileMcsName_Object = MibTableColumn
cLRFProfileMcsName = _CLRFProfileMcsName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 778, 1, 1, 3, 1, 1),
    _CLRFProfileMcsName_Type()
)
cLRFProfileMcsName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLRFProfileMcsName.setStatus("current")
_CLRFProfileMcsRate_Type = Unsigned32
_CLRFProfileMcsRate_Object = MibTableColumn
cLRFProfileMcsRate = _CLRFProfileMcsRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 778, 1, 1, 3, 1, 2),
    _CLRFProfileMcsRate_Type()
)
cLRFProfileMcsRate.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLRFProfileMcsRate.setStatus("current")


class _CLRFProfileMcsRateSupport_Type(TruthValue):
    """Custom type cLRFProfileMcsRateSupport based on TruthValue"""


_CLRFProfileMcsRateSupport_Object = MibTableColumn
cLRFProfileMcsRateSupport = _CLRFProfileMcsRateSupport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 778, 1, 1, 3, 1, 3),
    _CLRFProfileMcsRateSupport_Type()
)
cLRFProfileMcsRateSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLRFProfileMcsRateSupport.setStatus("current")
_CiscoLwappRFGlobalObjects_ObjectIdentity = ObjectIdentity
ciscoLwappRFGlobalObjects = _CiscoLwappRFGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 778, 1, 2)
)
_CLRFProfileOutOfBoxAPConfig_Type = TruthValue
_CLRFProfileOutOfBoxAPConfig_Object = MibScalar
cLRFProfileOutOfBoxAPConfig = _CLRFProfileOutOfBoxAPConfig_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 778, 1, 2, 1),
    _CLRFProfileOutOfBoxAPConfig_Type()
)
cLRFProfileOutOfBoxAPConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLRFProfileOutOfBoxAPConfig.setStatus("current")
_CiscoLwappRFMIBConform_ObjectIdentity = ObjectIdentity
ciscoLwappRFMIBConform = _CiscoLwappRFMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 778, 2)
)
_CiscoLwappRFMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoLwappRFMIBCompliances = _CiscoLwappRFMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 778, 2, 1)
)
_CiscoLwappRFMIBGroups_ObjectIdentity = ObjectIdentity
ciscoLwappRFMIBGroups = _CiscoLwappRFMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 778, 2, 2)
)

# Managed Objects groups

ciscoLwappRFConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 778, 2, 2, 1)
)
ciscoLwappRFConfigGroup.setObjects(
      *(("CISCO-LWAPP-RF-MIB", "cLAPGroups802dot11bgRFProfileName"),
        ("CISCO-LWAPP-RF-MIB", "cLAPGroups802dot11aRFProfileName"),
        ("CISCO-LWAPP-RF-MIB", "cLRFProfileDescr"),
        ("CISCO-LWAPP-RF-MIB", "cLRFProfileTransmitPowerMin"),
        ("CISCO-LWAPP-RF-MIB", "cLRFProfileTransmitPowerMax"),
        ("CISCO-LWAPP-RF-MIB", "cLRFProfileTransmitPowerThresholdV1"),
        ("CISCO-LWAPP-RF-MIB", "cLRFProfileTransmitPowerThresholdV2"),
        ("CISCO-LWAPP-RF-MIB", "cLRFProfileDataRate1Mbps"),
        ("CISCO-LWAPP-RF-MIB", "cLRFProfileDataRate2Mbps"),
        ("CISCO-LWAPP-RF-MIB", "cLRFProfileDataRate5AndHalfMbps"),
        ("CISCO-LWAPP-RF-MIB", "cLRFProfileDataRate11Mbps"),
        ("CISCO-LWAPP-RF-MIB", "cLRFProfileDataRate6Mbps"),
        ("CISCO-LWAPP-RF-MIB", "cLRFProfileDataRate9Mbps"),
        ("CISCO-LWAPP-RF-MIB", "cLRFProfileDataRate12Mbps"),
        ("CISCO-LWAPP-RF-MIB", "cLRFProfileDataRate18Mbps"),
        ("CISCO-LWAPP-RF-MIB", "cLRFProfileDataRate24Mbps"),
        ("CISCO-LWAPP-RF-MIB", "cLRFProfileDataRate36Mbps"),
        ("CISCO-LWAPP-RF-MIB", "cLRFProfileDataRate48Mbps"),
        ("CISCO-LWAPP-RF-MIB", "cLRFProfileDataRate54Mbps"),
        ("CISCO-LWAPP-RF-MIB", "cLRFProfileRadioType"),
        ("CISCO-LWAPP-RF-MIB", "cLRFProfileStorageType"),
        ("CISCO-LWAPP-RF-MIB", "cLRFProfileRowStatus"),
        ("CISCO-LWAPP-RF-MIB", "cLRFProfile11nOnly"))
)
if mibBuilder.loadTexts:
    ciscoLwappRFConfigGroup.setStatus("deprecated")

ciscoLwappRFConfigGroupVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 778, 2, 2, 2)
)
ciscoLwappRFConfigGroupVer1.setObjects(
      *(("CISCO-LWAPP-RF-MIB", "cLAPGroups802dot11bgRFProfileName"),
        ("CISCO-LWAPP-RF-MIB", "cLAPGroups802dot11aRFProfileName"),
        ("CISCO-LWAPP-RF-MIB", "cLRFProfileDescr"),
        ("CISCO-LWAPP-RF-MIB", "cLRFProfileTransmitPowerMin"),
        ("CISCO-LWAPP-RF-MIB", "cLRFProfileTransmitPowerMax"),
        ("CISCO-LWAPP-RF-MIB", "cLRFProfileTransmitPowerThresholdV1"),
        ("CISCO-LWAPP-RF-MIB", "cLRFProfileTransmitPowerThresholdV2"),
        ("CISCO-LWAPP-RF-MIB", "cLRFProfileDataRate1Mbps"),
        ("CISCO-LWAPP-RF-MIB", "cLRFProfileDataRate2Mbps"),
        ("CISCO-LWAPP-RF-MIB", "cLRFProfileDataRate5AndHalfMbps"),
        ("CISCO-LWAPP-RF-MIB", "cLRFProfileDataRate11Mbps"),
        ("CISCO-LWAPP-RF-MIB", "cLRFProfileDataRate6Mbps"),
        ("CISCO-LWAPP-RF-MIB", "cLRFProfileDataRate9Mbps"),
        ("CISCO-LWAPP-RF-MIB", "cLRFProfileDataRate12Mbps"),
        ("CISCO-LWAPP-RF-MIB", "cLRFProfileDataRate18Mbps"),
        ("CISCO-LWAPP-RF-MIB", "cLRFProfileDataRate24Mbps"),
        ("CISCO-LWAPP-RF-MIB", "cLRFProfileDataRate36Mbps"),
        ("CISCO-LWAPP-RF-MIB", "cLRFProfileDataRate48Mbps"),
        ("CISCO-LWAPP-RF-MIB", "cLRFProfileDataRate54Mbps"),
        ("CISCO-LWAPP-RF-MIB", "cLRFProfileRadioType"),
        ("CISCO-LWAPP-RF-MIB", "cLRFProfileStorageType"),
        ("CISCO-LWAPP-RF-MIB", "cLRFProfileRowStatus"),
        ("CISCO-LWAPP-RF-MIB", "cLRFProfile11nOnly"),
        ("CISCO-LWAPP-RF-MIB", "cLRFProfileMcsName"),
        ("CISCO-LWAPP-RF-MIB", "cLRFProfileMcsRate"),
        ("CISCO-LWAPP-RF-MIB", "cLRFProfileMcsRateSupport"))
)
if mibBuilder.loadTexts:
    ciscoLwappRFConfigGroupVer1.setStatus("current")

ciscoLwappRFGlobalConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 778, 2, 2, 3)
)
ciscoLwappRFGlobalConfigGroup.setObjects(
    ("CISCO-LWAPP-RF-MIB", "cLRFProfileOutOfBoxAPConfig")
)
if mibBuilder.loadTexts:
    ciscoLwappRFGlobalConfigGroup.setStatus("current")

ciscoLwappRFConfigGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 778, 2, 2, 4)
)
ciscoLwappRFConfigGroup2.setObjects(
      *(("CISCO-LWAPP-RF-MIB", "cLRFProfileHDClientTrapThreshold"),
        ("CISCO-LWAPP-RF-MIB", "cLRFProfileInterferenceThreshold"),
        ("CISCO-LWAPP-RF-MIB", "cLRFProfileNoiseThreshold"),
        ("CISCO-LWAPP-RF-MIB", "cLRFProfileUtilizationThreshold"))
)
if mibBuilder.loadTexts:
    ciscoLwappRFConfigGroup2.setStatus("current")

ciscoLwappRFConfigGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 778, 2, 2, 5)
)
ciscoLwappRFConfigGroup1.setObjects(
      *(("CISCO-LWAPP-RF-MIB", "cLRFProfileHighDensityMaxRadioClients"),
        ("CISCO-LWAPP-RF-MIB", "cLRFProfileBandSelectProbeResponse"),
        ("CISCO-LWAPP-RF-MIB", "cLRFProfileBandSelectCycleCount"),
        ("CISCO-LWAPP-RF-MIB", "cLRFProfileBandSelectCycleThreshold"),
        ("CISCO-LWAPP-RF-MIB", "cLRFProfileBandSelectExpireSuppression"),
        ("CISCO-LWAPP-RF-MIB", "cLRFProfileBandSelectExpireDualBand"),
        ("CISCO-LWAPP-RF-MIB", "cLRFProfileBandSelectClientRSSI"),
        ("CISCO-LWAPP-RF-MIB", "cLRFProfileLoadBalancingWindowSize"),
        ("CISCO-LWAPP-RF-MIB", "cLRFProfileLoadBalancingDenialCount"),
        ("CISCO-LWAPP-RF-MIB", "cLRFProfileCHDDataRSSIThreshold"),
        ("CISCO-LWAPP-RF-MIB", "cLRFProfileCHDVoiceRSSIThreshold"),
        ("CISCO-LWAPP-RF-MIB", "cLRFProfileCHDClientExceptionLevel"),
        ("CISCO-LWAPP-RF-MIB", "cLRFProfileCHDCoverageExceptionLevel"),
        ("CISCO-LWAPP-RF-MIB", "cLRFProfileMulticastDataRate"))
)
if mibBuilder.loadTexts:
    ciscoLwappRFConfigGroup1.setStatus("current")

ciscoLwappRFConfigGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 778, 2, 2, 6)
)
ciscoLwappRFConfigGroup3.setObjects(
      *(("CISCO-LWAPP-RF-MIB", "cLRFProfileDCAForeignContribution"),
        ("CISCO-LWAPP-RF-MIB", "cLRFProfileDCAChannelWidth"),
        ("CISCO-LWAPP-RF-MIB", "cLRFProfileDCAChannelList"))
)
if mibBuilder.loadTexts:
    ciscoLwappRFConfigGroup3.setStatus("current")

ciscoLwappRFConfigGroup4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 778, 2, 2, 7)
)
ciscoLwappRFConfigGroup4.setObjects(
    ("CISCO-LWAPP-RF-MIB", "cLRFProfileRxSopThreshold")
)
if mibBuilder.loadTexts:
    ciscoLwappRFConfigGroup4.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoLwappRFMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 778, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoLwappRFMIBCompliance.setStatus(
        "deprecated"
    )

ciscoLwappRFMIBComplianceVer1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 778, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoLwappRFMIBComplianceVer1.setStatus(
        "current"
    )

ciscoLwappRFMIBComplianceVer2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 778, 2, 1, 3)
)
if mibBuilder.loadTexts:
    ciscoLwappRFMIBComplianceVer2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-LWAPP-RF-MIB",
    **{"CiscoLwappRFApDataRates": CiscoLwappRFApDataRates,
       "ciscoLwappRFMIB": ciscoLwappRFMIB,
       "ciscoLwappRFMIBNotifs": ciscoLwappRFMIBNotifs,
       "ciscoLwappRFMIBObjects": ciscoLwappRFMIBObjects,
       "ciscoLwappRFConfig": ciscoLwappRFConfig,
       "cLAPGroupsRFProfileTable": cLAPGroupsRFProfileTable,
       "cLAPGroupsRFProfileEntry": cLAPGroupsRFProfileEntry,
       "cLAPGroups802dot11bgRFProfileName": cLAPGroups802dot11bgRFProfileName,
       "cLAPGroups802dot11aRFProfileName": cLAPGroups802dot11aRFProfileName,
       "cLRFProfileTable": cLRFProfileTable,
       "cLRFProfileEntry": cLRFProfileEntry,
       "cLRFProfileName": cLRFProfileName,
       "cLRFProfileDescr": cLRFProfileDescr,
       "cLRFProfileTransmitPowerMin": cLRFProfileTransmitPowerMin,
       "cLRFProfileTransmitPowerMax": cLRFProfileTransmitPowerMax,
       "cLRFProfileTransmitPowerThresholdV1": cLRFProfileTransmitPowerThresholdV1,
       "cLRFProfileTransmitPowerThresholdV2": cLRFProfileTransmitPowerThresholdV2,
       "cLRFProfileDataRate1Mbps": cLRFProfileDataRate1Mbps,
       "cLRFProfileDataRate2Mbps": cLRFProfileDataRate2Mbps,
       "cLRFProfileDataRate5AndHalfMbps": cLRFProfileDataRate5AndHalfMbps,
       "cLRFProfileDataRate11Mbps": cLRFProfileDataRate11Mbps,
       "cLRFProfileDataRate6Mbps": cLRFProfileDataRate6Mbps,
       "cLRFProfileDataRate9Mbps": cLRFProfileDataRate9Mbps,
       "cLRFProfileDataRate12Mbps": cLRFProfileDataRate12Mbps,
       "cLRFProfileDataRate18Mbps": cLRFProfileDataRate18Mbps,
       "cLRFProfileDataRate24Mbps": cLRFProfileDataRate24Mbps,
       "cLRFProfileDataRate36Mbps": cLRFProfileDataRate36Mbps,
       "cLRFProfileDataRate48Mbps": cLRFProfileDataRate48Mbps,
       "cLRFProfileDataRate54Mbps": cLRFProfileDataRate54Mbps,
       "cLRFProfileRadioType": cLRFProfileRadioType,
       "cLRFProfileStorageType": cLRFProfileStorageType,
       "cLRFProfileRowStatus": cLRFProfileRowStatus,
       "cLRFProfileHighDensityMaxRadioClients": cLRFProfileHighDensityMaxRadioClients,
       "cLRFProfileBandSelectProbeResponse": cLRFProfileBandSelectProbeResponse,
       "cLRFProfileBandSelectCycleCount": cLRFProfileBandSelectCycleCount,
       "cLRFProfileBandSelectCycleThreshold": cLRFProfileBandSelectCycleThreshold,
       "cLRFProfileBandSelectExpireSuppression": cLRFProfileBandSelectExpireSuppression,
       "cLRFProfileBandSelectExpireDualBand": cLRFProfileBandSelectExpireDualBand,
       "cLRFProfileBandSelectClientRSSI": cLRFProfileBandSelectClientRSSI,
       "cLRFProfileLoadBalancingWindowSize": cLRFProfileLoadBalancingWindowSize,
       "cLRFProfileLoadBalancingDenialCount": cLRFProfileLoadBalancingDenialCount,
       "cLRFProfileCHDDataRSSIThreshold": cLRFProfileCHDDataRSSIThreshold,
       "cLRFProfileCHDVoiceRSSIThreshold": cLRFProfileCHDVoiceRSSIThreshold,
       "cLRFProfileCHDClientExceptionLevel": cLRFProfileCHDClientExceptionLevel,
       "cLRFProfileCHDCoverageExceptionLevel": cLRFProfileCHDCoverageExceptionLevel,
       "cLRFProfileMulticastDataRate": cLRFProfileMulticastDataRate,
       "cLRFProfile11nOnly": cLRFProfile11nOnly,
       "cLRFProfileHDClientTrapThreshold": cLRFProfileHDClientTrapThreshold,
       "cLRFProfileInterferenceThreshold": cLRFProfileInterferenceThreshold,
       "cLRFProfileNoiseThreshold": cLRFProfileNoiseThreshold,
       "cLRFProfileUtilizationThreshold": cLRFProfileUtilizationThreshold,
       "cLRFProfileDCAForeignContribution": cLRFProfileDCAForeignContribution,
       "cLRFProfileDCAChannelWidth": cLRFProfileDCAChannelWidth,
       "cLRFProfileDCAChannelList": cLRFProfileDCAChannelList,
       "cLRFProfileRxSopThreshold": cLRFProfileRxSopThreshold,
       "cLRFProfileMcsDataRateTable": cLRFProfileMcsDataRateTable,
       "cLRFProfileMcsDataRateEntry": cLRFProfileMcsDataRateEntry,
       "cLRFProfileMcsName": cLRFProfileMcsName,
       "cLRFProfileMcsRate": cLRFProfileMcsRate,
       "cLRFProfileMcsRateSupport": cLRFProfileMcsRateSupport,
       "ciscoLwappRFGlobalObjects": ciscoLwappRFGlobalObjects,
       "cLRFProfileOutOfBoxAPConfig": cLRFProfileOutOfBoxAPConfig,
       "ciscoLwappRFMIBConform": ciscoLwappRFMIBConform,
       "ciscoLwappRFMIBCompliances": ciscoLwappRFMIBCompliances,
       "ciscoLwappRFMIBCompliance": ciscoLwappRFMIBCompliance,
       "ciscoLwappRFMIBComplianceVer1": ciscoLwappRFMIBComplianceVer1,
       "ciscoLwappRFMIBComplianceVer2": ciscoLwappRFMIBComplianceVer2,
       "ciscoLwappRFMIBGroups": ciscoLwappRFMIBGroups,
       "ciscoLwappRFConfigGroup": ciscoLwappRFConfigGroup,
       "ciscoLwappRFConfigGroupVer1": ciscoLwappRFConfigGroupVer1,
       "ciscoLwappRFGlobalConfigGroup": ciscoLwappRFGlobalConfigGroup,
       "ciscoLwappRFConfigGroup2": ciscoLwappRFConfigGroup2,
       "ciscoLwappRFConfigGroup1": ciscoLwappRFConfigGroup1,
       "ciscoLwappRFConfigGroup3": ciscoLwappRFConfigGroup3,
       "ciscoLwappRFConfigGroup4": ciscoLwappRFConfigGroup4}
)
