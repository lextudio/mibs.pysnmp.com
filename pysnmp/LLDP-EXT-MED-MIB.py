# SNMP MIB module (LLDP-EXT-MED-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/LLDP-EXT-MED-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:46:08 2024
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

(Dscp,) = mibBuilder.importSymbols(
    "DIFFSERV-DSCP-TC",
    "Dscp")

(lldpExtensions,
 lldpLocPortNum,
 lldpPortConfigEntry,
 lldpRemChassisId,
 lldpRemChassisIdSubtype,
 lldpRemIndex,
 lldpRemLocalPortNum,
 lldpRemTimeMark) = mibBuilder.importSymbols(
    "LLDP-MIB",
    "lldpExtensions",
    "lldpLocPortNum",
    "lldpPortConfigEntry",
    "lldpRemChassisId",
    "lldpRemChassisIdSubtype",
    "lldpRemIndex",
    "lldpRemLocalPortNum",
    "lldpRemTimeMark")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

lldpXMedMIB = ModuleIdentity(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4795)
)
lldpXMedMIB.setRevisions(
        ("2005-07-28 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class LldpXMedDeviceClass(Integer32, TextualConvention):
    status = "current"
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
        *(("endpointClass1", 1),
          ("endpointClass2", 2),
          ("endpointClass3", 3),
          ("networkConnectivity", 4),
          ("notDefined", 0))
    )



class LldpXMedCapabilities(Bits, TextualConvention):
    status = "current"


class LocationSubtype(Integer32, TextualConvention):
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
        *(("civicAddress", 3),
          ("coordinateBased", 2),
          ("elin", 4),
          ("unknown", 1))
    )



class PolicyAppType(Bits, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_LldpXMedNotifications_ObjectIdentity = ObjectIdentity
lldpXMedNotifications = _LldpXMedNotifications_ObjectIdentity(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4795, 0)
)
_LldpXMedObjects_ObjectIdentity = ObjectIdentity
lldpXMedObjects = _LldpXMedObjects_ObjectIdentity(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4795, 1)
)
_LldpXMedConfig_ObjectIdentity = ObjectIdentity
lldpXMedConfig = _LldpXMedConfig_ObjectIdentity(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4795, 1, 1)
)
_LldpXMedLocDeviceClass_Type = LldpXMedDeviceClass
_LldpXMedLocDeviceClass_Object = MibScalar
lldpXMedLocDeviceClass = _LldpXMedLocDeviceClass_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4795, 1, 1, 1),
    _LldpXMedLocDeviceClass_Type()
)
lldpXMedLocDeviceClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXMedLocDeviceClass.setStatus("current")
_LldpXMedPortConfigTable_Object = MibTable
lldpXMedPortConfigTable = _LldpXMedPortConfigTable_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4795, 1, 1, 2)
)
if mibBuilder.loadTexts:
    lldpXMedPortConfigTable.setStatus("current")
_LldpXMedPortConfigEntry_Object = MibTableRow
lldpXMedPortConfigEntry = _LldpXMedPortConfigEntry_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4795, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    lldpXMedPortConfigEntry.setStatus("current")
_LldpXMedPortCapSupported_Type = LldpXMedCapabilities
_LldpXMedPortCapSupported_Object = MibTableColumn
lldpXMedPortCapSupported = _LldpXMedPortCapSupported_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4795, 1, 1, 2, 1, 1),
    _LldpXMedPortCapSupported_Type()
)
lldpXMedPortCapSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXMedPortCapSupported.setStatus("current")


class _LldpXMedPortConfigTLVsTxEnable_Type(LldpXMedCapabilities):
    """Custom type lldpXMedPortConfigTLVsTxEnable based on LldpXMedCapabilities"""
    defaultBinValue = "0"


_LldpXMedPortConfigTLVsTxEnable_Object = MibTableColumn
lldpXMedPortConfigTLVsTxEnable = _LldpXMedPortConfigTLVsTxEnable_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4795, 1, 1, 2, 1, 2),
    _LldpXMedPortConfigTLVsTxEnable_Type()
)
lldpXMedPortConfigTLVsTxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpXMedPortConfigTLVsTxEnable.setStatus("current")


class _LldpXMedPortConfigNotifEnable_Type(TruthValue):
    """Custom type lldpXMedPortConfigNotifEnable based on TruthValue"""


_LldpXMedPortConfigNotifEnable_Object = MibTableColumn
lldpXMedPortConfigNotifEnable = _LldpXMedPortConfigNotifEnable_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4795, 1, 1, 2, 1, 3),
    _LldpXMedPortConfigNotifEnable_Type()
)
lldpXMedPortConfigNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpXMedPortConfigNotifEnable.setStatus("current")


class _LldpXMedFastStartRepeatCount_Type(Unsigned32):
    """Custom type lldpXMedFastStartRepeatCount based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_LldpXMedFastStartRepeatCount_Type.__name__ = "Unsigned32"
_LldpXMedFastStartRepeatCount_Object = MibScalar
lldpXMedFastStartRepeatCount = _LldpXMedFastStartRepeatCount_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4795, 1, 1, 3),
    _LldpXMedFastStartRepeatCount_Type()
)
lldpXMedFastStartRepeatCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpXMedFastStartRepeatCount.setStatus("current")
_LldpXMedLocalData_ObjectIdentity = ObjectIdentity
lldpXMedLocalData = _LldpXMedLocalData_ObjectIdentity(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4795, 1, 2)
)
_LldpXMedLocMediaPolicyTable_Object = MibTable
lldpXMedLocMediaPolicyTable = _LldpXMedLocMediaPolicyTable_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4795, 1, 2, 1)
)
if mibBuilder.loadTexts:
    lldpXMedLocMediaPolicyTable.setStatus("current")
_LldpXMedLocMediaPolicyEntry_Object = MibTableRow
lldpXMedLocMediaPolicyEntry = _LldpXMedLocMediaPolicyEntry_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4795, 1, 2, 1, 1)
)
lldpXMedLocMediaPolicyEntry.setIndexNames(
    (0, "LLDP-MIB", "lldpLocPortNum"),
    (0, "LLDP-EXT-MED-MIB", "lldpXMedLocMediaPolicyAppType"),
)
if mibBuilder.loadTexts:
    lldpXMedLocMediaPolicyEntry.setStatus("current")
_LldpXMedLocMediaPolicyAppType_Type = PolicyAppType
_LldpXMedLocMediaPolicyAppType_Object = MibTableColumn
lldpXMedLocMediaPolicyAppType = _LldpXMedLocMediaPolicyAppType_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4795, 1, 2, 1, 1, 1),
    _LldpXMedLocMediaPolicyAppType_Type()
)
lldpXMedLocMediaPolicyAppType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpXMedLocMediaPolicyAppType.setStatus("current")


class _LldpXMedLocMediaPolicyVlanID_Type(Integer32):
    """Custom type lldpXMedLocMediaPolicyVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4094),
        ValueRangeConstraint(4095, 4095),
    )


_LldpXMedLocMediaPolicyVlanID_Type.__name__ = "Integer32"
_LldpXMedLocMediaPolicyVlanID_Object = MibTableColumn
lldpXMedLocMediaPolicyVlanID = _LldpXMedLocMediaPolicyVlanID_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4795, 1, 2, 1, 1, 2),
    _LldpXMedLocMediaPolicyVlanID_Type()
)
lldpXMedLocMediaPolicyVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXMedLocMediaPolicyVlanID.setStatus("current")


class _LldpXMedLocMediaPolicyPriority_Type(Integer32):
    """Custom type lldpXMedLocMediaPolicyPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_LldpXMedLocMediaPolicyPriority_Type.__name__ = "Integer32"
_LldpXMedLocMediaPolicyPriority_Object = MibTableColumn
lldpXMedLocMediaPolicyPriority = _LldpXMedLocMediaPolicyPriority_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4795, 1, 2, 1, 1, 3),
    _LldpXMedLocMediaPolicyPriority_Type()
)
lldpXMedLocMediaPolicyPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXMedLocMediaPolicyPriority.setStatus("current")
_LldpXMedLocMediaPolicyDscp_Type = Dscp
_LldpXMedLocMediaPolicyDscp_Object = MibTableColumn
lldpXMedLocMediaPolicyDscp = _LldpXMedLocMediaPolicyDscp_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4795, 1, 2, 1, 1, 4),
    _LldpXMedLocMediaPolicyDscp_Type()
)
lldpXMedLocMediaPolicyDscp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXMedLocMediaPolicyDscp.setStatus("current")
_LldpXMedLocMediaPolicyUnknown_Type = TruthValue
_LldpXMedLocMediaPolicyUnknown_Object = MibTableColumn
lldpXMedLocMediaPolicyUnknown = _LldpXMedLocMediaPolicyUnknown_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4795, 1, 2, 1, 1, 5),
    _LldpXMedLocMediaPolicyUnknown_Type()
)
lldpXMedLocMediaPolicyUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXMedLocMediaPolicyUnknown.setStatus("current")
_LldpXMedLocMediaPolicyTagged_Type = TruthValue
_LldpXMedLocMediaPolicyTagged_Object = MibTableColumn
lldpXMedLocMediaPolicyTagged = _LldpXMedLocMediaPolicyTagged_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4795, 1, 2, 1, 1, 6),
    _LldpXMedLocMediaPolicyTagged_Type()
)
lldpXMedLocMediaPolicyTagged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXMedLocMediaPolicyTagged.setStatus("current")


class _LldpXMedLocHardwareRev_Type(SnmpAdminString):
    """Custom type lldpXMedLocHardwareRev based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LldpXMedLocHardwareRev_Type.__name__ = "SnmpAdminString"
_LldpXMedLocHardwareRev_Object = MibScalar
lldpXMedLocHardwareRev = _LldpXMedLocHardwareRev_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4795, 1, 2, 2),
    _LldpXMedLocHardwareRev_Type()
)
lldpXMedLocHardwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXMedLocHardwareRev.setStatus("current")


class _LldpXMedLocFirmwareRev_Type(SnmpAdminString):
    """Custom type lldpXMedLocFirmwareRev based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LldpXMedLocFirmwareRev_Type.__name__ = "SnmpAdminString"
_LldpXMedLocFirmwareRev_Object = MibScalar
lldpXMedLocFirmwareRev = _LldpXMedLocFirmwareRev_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4795, 1, 2, 3),
    _LldpXMedLocFirmwareRev_Type()
)
lldpXMedLocFirmwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXMedLocFirmwareRev.setStatus("current")


class _LldpXMedLocSoftwareRev_Type(SnmpAdminString):
    """Custom type lldpXMedLocSoftwareRev based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LldpXMedLocSoftwareRev_Type.__name__ = "SnmpAdminString"
_LldpXMedLocSoftwareRev_Object = MibScalar
lldpXMedLocSoftwareRev = _LldpXMedLocSoftwareRev_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4795, 1, 2, 4),
    _LldpXMedLocSoftwareRev_Type()
)
lldpXMedLocSoftwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXMedLocSoftwareRev.setStatus("current")


class _LldpXMedLocSerialNum_Type(SnmpAdminString):
    """Custom type lldpXMedLocSerialNum based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LldpXMedLocSerialNum_Type.__name__ = "SnmpAdminString"
_LldpXMedLocSerialNum_Object = MibScalar
lldpXMedLocSerialNum = _LldpXMedLocSerialNum_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4795, 1, 2, 5),
    _LldpXMedLocSerialNum_Type()
)
lldpXMedLocSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXMedLocSerialNum.setStatus("current")


class _LldpXMedLocMfgName_Type(SnmpAdminString):
    """Custom type lldpXMedLocMfgName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LldpXMedLocMfgName_Type.__name__ = "SnmpAdminString"
_LldpXMedLocMfgName_Object = MibScalar
lldpXMedLocMfgName = _LldpXMedLocMfgName_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4795, 1, 2, 6),
    _LldpXMedLocMfgName_Type()
)
lldpXMedLocMfgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXMedLocMfgName.setStatus("current")


class _LldpXMedLocModelName_Type(SnmpAdminString):
    """Custom type lldpXMedLocModelName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LldpXMedLocModelName_Type.__name__ = "SnmpAdminString"
_LldpXMedLocModelName_Object = MibScalar
lldpXMedLocModelName = _LldpXMedLocModelName_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4795, 1, 2, 7),
    _LldpXMedLocModelName_Type()
)
lldpXMedLocModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXMedLocModelName.setStatus("current")


class _LldpXMedLocAssetID_Type(SnmpAdminString):
    """Custom type lldpXMedLocAssetID based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LldpXMedLocAssetID_Type.__name__ = "SnmpAdminString"
_LldpXMedLocAssetID_Object = MibScalar
lldpXMedLocAssetID = _LldpXMedLocAssetID_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4795, 1, 2, 8),
    _LldpXMedLocAssetID_Type()
)
lldpXMedLocAssetID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXMedLocAssetID.setStatus("current")
_LldpXMedLocLocationTable_Object = MibTable
lldpXMedLocLocationTable = _LldpXMedLocLocationTable_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4795, 1, 2, 9)
)
if mibBuilder.loadTexts:
    lldpXMedLocLocationTable.setStatus("current")
_LldpXMedLocLocationEntry_Object = MibTableRow
lldpXMedLocLocationEntry = _LldpXMedLocLocationEntry_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4795, 1, 2, 9, 1)
)
lldpXMedLocLocationEntry.setIndexNames(
    (0, "LLDP-MIB", "lldpLocPortNum"),
    (0, "LLDP-EXT-MED-MIB", "lldpXMedLocLocationSubtype"),
)
if mibBuilder.loadTexts:
    lldpXMedLocLocationEntry.setStatus("current")
_LldpXMedLocLocationSubtype_Type = LocationSubtype
_LldpXMedLocLocationSubtype_Object = MibTableColumn
lldpXMedLocLocationSubtype = _LldpXMedLocLocationSubtype_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4795, 1, 2, 9, 1, 1),
    _LldpXMedLocLocationSubtype_Type()
)
lldpXMedLocLocationSubtype.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpXMedLocLocationSubtype.setStatus("current")


class _LldpXMedLocLocationInfo_Type(OctetString):
    """Custom type lldpXMedLocLocationInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_LldpXMedLocLocationInfo_Type.__name__ = "OctetString"
_LldpXMedLocLocationInfo_Object = MibTableColumn
lldpXMedLocLocationInfo = _LldpXMedLocLocationInfo_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4795, 1, 2, 9, 1, 2),
    _LldpXMedLocLocationInfo_Type()
)
lldpXMedLocLocationInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpXMedLocLocationInfo.setStatus("current")


class _LldpXMedLocXPoEDeviceType_Type(Integer32):
    """Custom type lldpXMedLocXPoEDeviceType based on Integer32"""
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
        *(("none", 4),
          ("pdDevice", 3),
          ("pseDevice", 2),
          ("unknown", 1))
    )


_LldpXMedLocXPoEDeviceType_Type.__name__ = "Integer32"
_LldpXMedLocXPoEDeviceType_Object = MibScalar
lldpXMedLocXPoEDeviceType = _LldpXMedLocXPoEDeviceType_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4795, 1, 2, 10),
    _LldpXMedLocXPoEDeviceType_Type()
)
lldpXMedLocXPoEDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXMedLocXPoEDeviceType.setStatus("current")
_LldpXMedLocXPoEPSEPortTable_Object = MibTable
lldpXMedLocXPoEPSEPortTable = _LldpXMedLocXPoEPSEPortTable_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4795, 1, 2, 11)
)
if mibBuilder.loadTexts:
    lldpXMedLocXPoEPSEPortTable.setStatus("current")
_LldpXMedLocXPoEPSEPortEntry_Object = MibTableRow
lldpXMedLocXPoEPSEPortEntry = _LldpXMedLocXPoEPSEPortEntry_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4795, 1, 2, 11, 1)
)
lldpXMedLocXPoEPSEPortEntry.setIndexNames(
    (0, "LLDP-MIB", "lldpLocPortNum"),
)
if mibBuilder.loadTexts:
    lldpXMedLocXPoEPSEPortEntry.setStatus("current")


class _LldpXMedLocXPoEPSEPortPowerAv_Type(Gauge32):
    """Custom type lldpXMedLocXPoEPSEPortPowerAv based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_LldpXMedLocXPoEPSEPortPowerAv_Type.__name__ = "Gauge32"
_LldpXMedLocXPoEPSEPortPowerAv_Object = MibTableColumn
lldpXMedLocXPoEPSEPortPowerAv = _LldpXMedLocXPoEPSEPortPowerAv_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4795, 1, 2, 11, 1, 1),
    _LldpXMedLocXPoEPSEPortPowerAv_Type()
)
lldpXMedLocXPoEPSEPortPowerAv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXMedLocXPoEPSEPortPowerAv.setStatus("current")
if mibBuilder.loadTexts:
    lldpXMedLocXPoEPSEPortPowerAv.setUnits("tenth of watt")


class _LldpXMedLocXPoEPSEPortPDPriority_Type(Integer32):
    """Custom type lldpXMedLocXPoEPSEPortPDPriority based on Integer32"""
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
        *(("critical", 2),
          ("high", 3),
          ("low", 4),
          ("unknown", 1))
    )


_LldpXMedLocXPoEPSEPortPDPriority_Type.__name__ = "Integer32"
_LldpXMedLocXPoEPSEPortPDPriority_Object = MibTableColumn
lldpXMedLocXPoEPSEPortPDPriority = _LldpXMedLocXPoEPSEPortPDPriority_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4795, 1, 2, 11, 1, 2),
    _LldpXMedLocXPoEPSEPortPDPriority_Type()
)
lldpXMedLocXPoEPSEPortPDPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXMedLocXPoEPSEPortPDPriority.setStatus("current")


class _LldpXMedLocXPoEPSEPowerSource_Type(Integer32):
    """Custom type lldpXMedLocXPoEPSEPowerSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("backup", 3),
          ("primary", 2),
          ("unknown", 1))
    )


_LldpXMedLocXPoEPSEPowerSource_Type.__name__ = "Integer32"
_LldpXMedLocXPoEPSEPowerSource_Object = MibScalar
lldpXMedLocXPoEPSEPowerSource = _LldpXMedLocXPoEPSEPowerSource_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4795, 1, 2, 12),
    _LldpXMedLocXPoEPSEPowerSource_Type()
)
lldpXMedLocXPoEPSEPowerSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXMedLocXPoEPSEPowerSource.setStatus("current")


class _LldpXMedLocXPoEPDPowerReq_Type(Gauge32):
    """Custom type lldpXMedLocXPoEPDPowerReq based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_LldpXMedLocXPoEPDPowerReq_Type.__name__ = "Gauge32"
_LldpXMedLocXPoEPDPowerReq_Object = MibScalar
lldpXMedLocXPoEPDPowerReq = _LldpXMedLocXPoEPDPowerReq_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4795, 1, 2, 13),
    _LldpXMedLocXPoEPDPowerReq_Type()
)
lldpXMedLocXPoEPDPowerReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXMedLocXPoEPDPowerReq.setStatus("current")
if mibBuilder.loadTexts:
    lldpXMedLocXPoEPDPowerReq.setUnits("tenth of watt")


class _LldpXMedLocXPoEPDPowerSource_Type(Integer32):
    """Custom type lldpXMedLocXPoEPDPowerSource based on Integer32"""
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
        *(("fromPSE", 2),
          ("local", 3),
          ("localAndPSE", 4),
          ("unknown", 1))
    )


_LldpXMedLocXPoEPDPowerSource_Type.__name__ = "Integer32"
_LldpXMedLocXPoEPDPowerSource_Object = MibScalar
lldpXMedLocXPoEPDPowerSource = _LldpXMedLocXPoEPDPowerSource_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4795, 1, 2, 14),
    _LldpXMedLocXPoEPDPowerSource_Type()
)
lldpXMedLocXPoEPDPowerSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXMedLocXPoEPDPowerSource.setStatus("current")


class _LldpXMedLocXPoEPDPowerPriority_Type(Integer32):
    """Custom type lldpXMedLocXPoEPDPowerPriority based on Integer32"""
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
        *(("critical", 2),
          ("high", 3),
          ("low", 4),
          ("unknown", 1))
    )


_LldpXMedLocXPoEPDPowerPriority_Type.__name__ = "Integer32"
_LldpXMedLocXPoEPDPowerPriority_Object = MibScalar
lldpXMedLocXPoEPDPowerPriority = _LldpXMedLocXPoEPDPowerPriority_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4795, 1, 2, 15),
    _LldpXMedLocXPoEPDPowerPriority_Type()
)
lldpXMedLocXPoEPDPowerPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXMedLocXPoEPDPowerPriority.setStatus("current")
_LldpXMedRemoteData_ObjectIdentity = ObjectIdentity
lldpXMedRemoteData = _LldpXMedRemoteData_ObjectIdentity(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4795, 1, 3)
)
_LldpXMedRemCapabilitiesTable_Object = MibTable
lldpXMedRemCapabilitiesTable = _LldpXMedRemCapabilitiesTable_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4795, 1, 3, 1)
)
if mibBuilder.loadTexts:
    lldpXMedRemCapabilitiesTable.setStatus("current")
_LldpXMedRemCapabilitiesEntry_Object = MibTableRow
lldpXMedRemCapabilitiesEntry = _LldpXMedRemCapabilitiesEntry_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4795, 1, 3, 1, 1)
)
lldpXMedRemCapabilitiesEntry.setIndexNames(
    (0, "LLDP-MIB", "lldpRemTimeMark"),
    (0, "LLDP-MIB", "lldpRemLocalPortNum"),
    (0, "LLDP-MIB", "lldpRemIndex"),
)
if mibBuilder.loadTexts:
    lldpXMedRemCapabilitiesEntry.setStatus("current")
_LldpXMedRemCapSupported_Type = LldpXMedCapabilities
_LldpXMedRemCapSupported_Object = MibTableColumn
lldpXMedRemCapSupported = _LldpXMedRemCapSupported_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4795, 1, 3, 1, 1, 1),
    _LldpXMedRemCapSupported_Type()
)
lldpXMedRemCapSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXMedRemCapSupported.setStatus("current")
_LldpXMedRemCapCurrent_Type = LldpXMedCapabilities
_LldpXMedRemCapCurrent_Object = MibTableColumn
lldpXMedRemCapCurrent = _LldpXMedRemCapCurrent_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4795, 1, 3, 1, 1, 2),
    _LldpXMedRemCapCurrent_Type()
)
lldpXMedRemCapCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXMedRemCapCurrent.setStatus("current")
_LldpXMedRemDeviceClass_Type = LldpXMedDeviceClass
_LldpXMedRemDeviceClass_Object = MibTableColumn
lldpXMedRemDeviceClass = _LldpXMedRemDeviceClass_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4795, 1, 3, 1, 1, 3),
    _LldpXMedRemDeviceClass_Type()
)
lldpXMedRemDeviceClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXMedRemDeviceClass.setStatus("current")
_LldpXMedRemMediaPolicyTable_Object = MibTable
lldpXMedRemMediaPolicyTable = _LldpXMedRemMediaPolicyTable_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4795, 1, 3, 2)
)
if mibBuilder.loadTexts:
    lldpXMedRemMediaPolicyTable.setStatus("current")
_LldpXMedRemMediaPolicyEntry_Object = MibTableRow
lldpXMedRemMediaPolicyEntry = _LldpXMedRemMediaPolicyEntry_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4795, 1, 3, 2, 1)
)
lldpXMedRemMediaPolicyEntry.setIndexNames(
    (0, "LLDP-MIB", "lldpRemTimeMark"),
    (0, "LLDP-MIB", "lldpRemLocalPortNum"),
    (0, "LLDP-MIB", "lldpRemIndex"),
    (0, "LLDP-EXT-MED-MIB", "lldpXMedRemMediaPolicyAppType"),
)
if mibBuilder.loadTexts:
    lldpXMedRemMediaPolicyEntry.setStatus("current")
_LldpXMedRemMediaPolicyAppType_Type = PolicyAppType
_LldpXMedRemMediaPolicyAppType_Object = MibTableColumn
lldpXMedRemMediaPolicyAppType = _LldpXMedRemMediaPolicyAppType_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4795, 1, 3, 2, 1, 1),
    _LldpXMedRemMediaPolicyAppType_Type()
)
lldpXMedRemMediaPolicyAppType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpXMedRemMediaPolicyAppType.setStatus("current")


class _LldpXMedRemMediaPolicyVlanID_Type(Integer32):
    """Custom type lldpXMedRemMediaPolicyVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4094),
        ValueRangeConstraint(4095, 4095),
    )


_LldpXMedRemMediaPolicyVlanID_Type.__name__ = "Integer32"
_LldpXMedRemMediaPolicyVlanID_Object = MibTableColumn
lldpXMedRemMediaPolicyVlanID = _LldpXMedRemMediaPolicyVlanID_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4795, 1, 3, 2, 1, 2),
    _LldpXMedRemMediaPolicyVlanID_Type()
)
lldpXMedRemMediaPolicyVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXMedRemMediaPolicyVlanID.setStatus("current")


class _LldpXMedRemMediaPolicyPriority_Type(Integer32):
    """Custom type lldpXMedRemMediaPolicyPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_LldpXMedRemMediaPolicyPriority_Type.__name__ = "Integer32"
_LldpXMedRemMediaPolicyPriority_Object = MibTableColumn
lldpXMedRemMediaPolicyPriority = _LldpXMedRemMediaPolicyPriority_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4795, 1, 3, 2, 1, 3),
    _LldpXMedRemMediaPolicyPriority_Type()
)
lldpXMedRemMediaPolicyPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXMedRemMediaPolicyPriority.setStatus("current")
_LldpXMedRemMediaPolicyDscp_Type = Dscp
_LldpXMedRemMediaPolicyDscp_Object = MibTableColumn
lldpXMedRemMediaPolicyDscp = _LldpXMedRemMediaPolicyDscp_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4795, 1, 3, 2, 1, 4),
    _LldpXMedRemMediaPolicyDscp_Type()
)
lldpXMedRemMediaPolicyDscp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXMedRemMediaPolicyDscp.setStatus("current")
_LldpXMedRemMediaPolicyUnknown_Type = TruthValue
_LldpXMedRemMediaPolicyUnknown_Object = MibTableColumn
lldpXMedRemMediaPolicyUnknown = _LldpXMedRemMediaPolicyUnknown_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4795, 1, 3, 2, 1, 5),
    _LldpXMedRemMediaPolicyUnknown_Type()
)
lldpXMedRemMediaPolicyUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXMedRemMediaPolicyUnknown.setStatus("current")
_LldpXMedRemMediaPolicyTagged_Type = TruthValue
_LldpXMedRemMediaPolicyTagged_Object = MibTableColumn
lldpXMedRemMediaPolicyTagged = _LldpXMedRemMediaPolicyTagged_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4795, 1, 3, 2, 1, 6),
    _LldpXMedRemMediaPolicyTagged_Type()
)
lldpXMedRemMediaPolicyTagged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXMedRemMediaPolicyTagged.setStatus("current")
_LldpXMedRemInventoryTable_Object = MibTable
lldpXMedRemInventoryTable = _LldpXMedRemInventoryTable_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4795, 1, 3, 3)
)
if mibBuilder.loadTexts:
    lldpXMedRemInventoryTable.setStatus("current")
_LldpXMedRemInventoryEntry_Object = MibTableRow
lldpXMedRemInventoryEntry = _LldpXMedRemInventoryEntry_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4795, 1, 3, 3, 1)
)
lldpXMedRemInventoryEntry.setIndexNames(
    (0, "LLDP-MIB", "lldpRemTimeMark"),
    (0, "LLDP-MIB", "lldpRemLocalPortNum"),
    (0, "LLDP-MIB", "lldpRemIndex"),
)
if mibBuilder.loadTexts:
    lldpXMedRemInventoryEntry.setStatus("current")


class _LldpXMedRemHardwareRev_Type(SnmpAdminString):
    """Custom type lldpXMedRemHardwareRev based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LldpXMedRemHardwareRev_Type.__name__ = "SnmpAdminString"
_LldpXMedRemHardwareRev_Object = MibTableColumn
lldpXMedRemHardwareRev = _LldpXMedRemHardwareRev_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4795, 1, 3, 3, 1, 1),
    _LldpXMedRemHardwareRev_Type()
)
lldpXMedRemHardwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXMedRemHardwareRev.setStatus("current")


class _LldpXMedRemFirmwareRev_Type(SnmpAdminString):
    """Custom type lldpXMedRemFirmwareRev based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LldpXMedRemFirmwareRev_Type.__name__ = "SnmpAdminString"
_LldpXMedRemFirmwareRev_Object = MibTableColumn
lldpXMedRemFirmwareRev = _LldpXMedRemFirmwareRev_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4795, 1, 3, 3, 1, 2),
    _LldpXMedRemFirmwareRev_Type()
)
lldpXMedRemFirmwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXMedRemFirmwareRev.setStatus("current")


class _LldpXMedRemSoftwareRev_Type(SnmpAdminString):
    """Custom type lldpXMedRemSoftwareRev based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LldpXMedRemSoftwareRev_Type.__name__ = "SnmpAdminString"
_LldpXMedRemSoftwareRev_Object = MibTableColumn
lldpXMedRemSoftwareRev = _LldpXMedRemSoftwareRev_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4795, 1, 3, 3, 1, 3),
    _LldpXMedRemSoftwareRev_Type()
)
lldpXMedRemSoftwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXMedRemSoftwareRev.setStatus("current")


class _LldpXMedRemSerialNum_Type(SnmpAdminString):
    """Custom type lldpXMedRemSerialNum based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LldpXMedRemSerialNum_Type.__name__ = "SnmpAdminString"
_LldpXMedRemSerialNum_Object = MibTableColumn
lldpXMedRemSerialNum = _LldpXMedRemSerialNum_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4795, 1, 3, 3, 1, 4),
    _LldpXMedRemSerialNum_Type()
)
lldpXMedRemSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXMedRemSerialNum.setStatus("current")


class _LldpXMedRemMfgName_Type(SnmpAdminString):
    """Custom type lldpXMedRemMfgName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LldpXMedRemMfgName_Type.__name__ = "SnmpAdminString"
_LldpXMedRemMfgName_Object = MibTableColumn
lldpXMedRemMfgName = _LldpXMedRemMfgName_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4795, 1, 3, 3, 1, 5),
    _LldpXMedRemMfgName_Type()
)
lldpXMedRemMfgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXMedRemMfgName.setStatus("current")


class _LldpXMedRemModelName_Type(SnmpAdminString):
    """Custom type lldpXMedRemModelName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LldpXMedRemModelName_Type.__name__ = "SnmpAdminString"
_LldpXMedRemModelName_Object = MibTableColumn
lldpXMedRemModelName = _LldpXMedRemModelName_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4795, 1, 3, 3, 1, 6),
    _LldpXMedRemModelName_Type()
)
lldpXMedRemModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXMedRemModelName.setStatus("current")


class _LldpXMedRemAssetID_Type(SnmpAdminString):
    """Custom type lldpXMedRemAssetID based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LldpXMedRemAssetID_Type.__name__ = "SnmpAdminString"
_LldpXMedRemAssetID_Object = MibTableColumn
lldpXMedRemAssetID = _LldpXMedRemAssetID_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4795, 1, 3, 3, 1, 7),
    _LldpXMedRemAssetID_Type()
)
lldpXMedRemAssetID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXMedRemAssetID.setStatus("current")
_LldpXMedRemLocationTable_Object = MibTable
lldpXMedRemLocationTable = _LldpXMedRemLocationTable_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4795, 1, 3, 4)
)
if mibBuilder.loadTexts:
    lldpXMedRemLocationTable.setStatus("current")
_LldpXMedRemLocationEntry_Object = MibTableRow
lldpXMedRemLocationEntry = _LldpXMedRemLocationEntry_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4795, 1, 3, 4, 1)
)
lldpXMedRemLocationEntry.setIndexNames(
    (0, "LLDP-MIB", "lldpRemTimeMark"),
    (0, "LLDP-MIB", "lldpRemLocalPortNum"),
    (0, "LLDP-MIB", "lldpRemIndex"),
    (0, "LLDP-EXT-MED-MIB", "lldpXMedRemLocationSubtype"),
)
if mibBuilder.loadTexts:
    lldpXMedRemLocationEntry.setStatus("current")
_LldpXMedRemLocationSubtype_Type = LocationSubtype
_LldpXMedRemLocationSubtype_Object = MibTableColumn
lldpXMedRemLocationSubtype = _LldpXMedRemLocationSubtype_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4795, 1, 3, 4, 1, 1),
    _LldpXMedRemLocationSubtype_Type()
)
lldpXMedRemLocationSubtype.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpXMedRemLocationSubtype.setStatus("current")


class _LldpXMedRemLocationInfo_Type(OctetString):
    """Custom type lldpXMedRemLocationInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_LldpXMedRemLocationInfo_Type.__name__ = "OctetString"
_LldpXMedRemLocationInfo_Object = MibTableColumn
lldpXMedRemLocationInfo = _LldpXMedRemLocationInfo_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4795, 1, 3, 4, 1, 2),
    _LldpXMedRemLocationInfo_Type()
)
lldpXMedRemLocationInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXMedRemLocationInfo.setStatus("current")
_LldpXMedRemXPoETable_Object = MibTable
lldpXMedRemXPoETable = _LldpXMedRemXPoETable_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4795, 1, 3, 5)
)
if mibBuilder.loadTexts:
    lldpXMedRemXPoETable.setStatus("current")
_LldpXMedRemXPoEEntry_Object = MibTableRow
lldpXMedRemXPoEEntry = _LldpXMedRemXPoEEntry_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4795, 1, 3, 5, 1)
)
lldpXMedRemXPoEEntry.setIndexNames(
    (0, "LLDP-MIB", "lldpRemTimeMark"),
    (0, "LLDP-MIB", "lldpRemLocalPortNum"),
    (0, "LLDP-MIB", "lldpRemIndex"),
)
if mibBuilder.loadTexts:
    lldpXMedRemXPoEEntry.setStatus("current")


class _LldpXMedRemXPoEDeviceType_Type(Integer32):
    """Custom type lldpXMedRemXPoEDeviceType based on Integer32"""
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
        *(("none", 4),
          ("pdDevice", 3),
          ("pseDevice", 2),
          ("unknown", 1))
    )


_LldpXMedRemXPoEDeviceType_Type.__name__ = "Integer32"
_LldpXMedRemXPoEDeviceType_Object = MibTableColumn
lldpXMedRemXPoEDeviceType = _LldpXMedRemXPoEDeviceType_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4795, 1, 3, 5, 1, 1),
    _LldpXMedRemXPoEDeviceType_Type()
)
lldpXMedRemXPoEDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXMedRemXPoEDeviceType.setStatus("current")
_LldpXMedRemXPoEPSETable_Object = MibTable
lldpXMedRemXPoEPSETable = _LldpXMedRemXPoEPSETable_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4795, 1, 3, 6)
)
if mibBuilder.loadTexts:
    lldpXMedRemXPoEPSETable.setStatus("current")
_LldpXMedRemXPoEPSEEntry_Object = MibTableRow
lldpXMedRemXPoEPSEEntry = _LldpXMedRemXPoEPSEEntry_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4795, 1, 3, 6, 1)
)
lldpXMedRemXPoEPSEEntry.setIndexNames(
    (0, "LLDP-MIB", "lldpRemTimeMark"),
    (0, "LLDP-MIB", "lldpRemLocalPortNum"),
    (0, "LLDP-MIB", "lldpRemIndex"),
)
if mibBuilder.loadTexts:
    lldpXMedRemXPoEPSEEntry.setStatus("current")


class _LldpXMedRemXPoEPSEPowerAv_Type(Gauge32):
    """Custom type lldpXMedRemXPoEPSEPowerAv based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_LldpXMedRemXPoEPSEPowerAv_Type.__name__ = "Gauge32"
_LldpXMedRemXPoEPSEPowerAv_Object = MibTableColumn
lldpXMedRemXPoEPSEPowerAv = _LldpXMedRemXPoEPSEPowerAv_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4795, 1, 3, 6, 1, 1),
    _LldpXMedRemXPoEPSEPowerAv_Type()
)
lldpXMedRemXPoEPSEPowerAv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXMedRemXPoEPSEPowerAv.setStatus("current")
if mibBuilder.loadTexts:
    lldpXMedRemXPoEPSEPowerAv.setUnits("tenth of watt")


class _LldpXMedRemXPoEPSEPowerSource_Type(Integer32):
    """Custom type lldpXMedRemXPoEPSEPowerSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("backup", 3),
          ("primary", 2),
          ("unknown", 1))
    )


_LldpXMedRemXPoEPSEPowerSource_Type.__name__ = "Integer32"
_LldpXMedRemXPoEPSEPowerSource_Object = MibTableColumn
lldpXMedRemXPoEPSEPowerSource = _LldpXMedRemXPoEPSEPowerSource_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4795, 1, 3, 6, 1, 2),
    _LldpXMedRemXPoEPSEPowerSource_Type()
)
lldpXMedRemXPoEPSEPowerSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXMedRemXPoEPSEPowerSource.setStatus("current")


class _LldpXMedRemXPoEPSEPowerPriority_Type(Integer32):
    """Custom type lldpXMedRemXPoEPSEPowerPriority based on Integer32"""
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
        *(("critical", 2),
          ("high", 3),
          ("low", 4),
          ("unknown", 1))
    )


_LldpXMedRemXPoEPSEPowerPriority_Type.__name__ = "Integer32"
_LldpXMedRemXPoEPSEPowerPriority_Object = MibTableColumn
lldpXMedRemXPoEPSEPowerPriority = _LldpXMedRemXPoEPSEPowerPriority_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4795, 1, 3, 6, 1, 3),
    _LldpXMedRemXPoEPSEPowerPriority_Type()
)
lldpXMedRemXPoEPSEPowerPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXMedRemXPoEPSEPowerPriority.setStatus("current")
_LldpXMedRemXPoEPDTable_Object = MibTable
lldpXMedRemXPoEPDTable = _LldpXMedRemXPoEPDTable_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4795, 1, 3, 7)
)
if mibBuilder.loadTexts:
    lldpXMedRemXPoEPDTable.setStatus("current")
_LldpXMedRemXPoEPDEntry_Object = MibTableRow
lldpXMedRemXPoEPDEntry = _LldpXMedRemXPoEPDEntry_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4795, 1, 3, 7, 1)
)
lldpXMedRemXPoEPDEntry.setIndexNames(
    (0, "LLDP-MIB", "lldpRemTimeMark"),
    (0, "LLDP-MIB", "lldpRemLocalPortNum"),
    (0, "LLDP-MIB", "lldpRemIndex"),
)
if mibBuilder.loadTexts:
    lldpXMedRemXPoEPDEntry.setStatus("current")


class _LldpXMedRemXPoEPDPowerReq_Type(Gauge32):
    """Custom type lldpXMedRemXPoEPDPowerReq based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_LldpXMedRemXPoEPDPowerReq_Type.__name__ = "Gauge32"
_LldpXMedRemXPoEPDPowerReq_Object = MibTableColumn
lldpXMedRemXPoEPDPowerReq = _LldpXMedRemXPoEPDPowerReq_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4795, 1, 3, 7, 1, 1),
    _LldpXMedRemXPoEPDPowerReq_Type()
)
lldpXMedRemXPoEPDPowerReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXMedRemXPoEPDPowerReq.setStatus("current")
if mibBuilder.loadTexts:
    lldpXMedRemXPoEPDPowerReq.setUnits("tenth of watt")


class _LldpXMedRemXPoEPDPowerSource_Type(Integer32):
    """Custom type lldpXMedRemXPoEPDPowerSource based on Integer32"""
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
        *(("fromPSE", 2),
          ("local", 3),
          ("localAndPSE", 4),
          ("unknown", 1))
    )


_LldpXMedRemXPoEPDPowerSource_Type.__name__ = "Integer32"
_LldpXMedRemXPoEPDPowerSource_Object = MibTableColumn
lldpXMedRemXPoEPDPowerSource = _LldpXMedRemXPoEPDPowerSource_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4795, 1, 3, 7, 1, 2),
    _LldpXMedRemXPoEPDPowerSource_Type()
)
lldpXMedRemXPoEPDPowerSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXMedRemXPoEPDPowerSource.setStatus("current")


class _LldpXMedRemXPoEPDPowerPriority_Type(Integer32):
    """Custom type lldpXMedRemXPoEPDPowerPriority based on Integer32"""
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
        *(("critical", 2),
          ("high", 3),
          ("low", 4),
          ("unknown", 1))
    )


_LldpXMedRemXPoEPDPowerPriority_Type.__name__ = "Integer32"
_LldpXMedRemXPoEPDPowerPriority_Object = MibTableColumn
lldpXMedRemXPoEPDPowerPriority = _LldpXMedRemXPoEPDPowerPriority_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4795, 1, 3, 7, 1, 3),
    _LldpXMedRemXPoEPDPowerPriority_Type()
)
lldpXMedRemXPoEPDPowerPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXMedRemXPoEPDPowerPriority.setStatus("current")
_LldpXMedConformance_ObjectIdentity = ObjectIdentity
lldpXMedConformance = _LldpXMedConformance_ObjectIdentity(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4795, 2)
)
_LldpXMedCompliances_ObjectIdentity = ObjectIdentity
lldpXMedCompliances = _LldpXMedCompliances_ObjectIdentity(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4795, 2, 1)
)
_LldpXMedGroups_ObjectIdentity = ObjectIdentity
lldpXMedGroups = _LldpXMedGroups_ObjectIdentity(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4795, 2, 2)
)
lldpPortConfigEntry.registerAugmentions(
    ("LLDP-EXT-MED-MIB",
     "lldpXMedPortConfigEntry")
)
lldpXMedPortConfigEntry.setIndexNames(*lldpPortConfigEntry.getIndexNames())

# Managed Objects groups

lldpXMedConfigGroup = ObjectGroup(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4795, 2, 2, 1)
)
lldpXMedConfigGroup.setObjects(
      *(("LLDP-EXT-MED-MIB", "lldpXMedPortCapSupported"),
        ("LLDP-EXT-MED-MIB", "lldpXMedPortConfigTLVsTxEnable"),
        ("LLDP-EXT-MED-MIB", "lldpXMedPortConfigNotifEnable"),
        ("LLDP-EXT-MED-MIB", "lldpXMedFastStartRepeatCount"),
        ("LLDP-EXT-MED-MIB", "lldpXMedLocXPoEDeviceType"),
        ("LLDP-EXT-MED-MIB", "lldpXMedLocDeviceClass"))
)
if mibBuilder.loadTexts:
    lldpXMedConfigGroup.setStatus("current")

lldpXMedOptMediaPolicyGroup = ObjectGroup(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4795, 2, 2, 2)
)
lldpXMedOptMediaPolicyGroup.setObjects(
      *(("LLDP-EXT-MED-MIB", "lldpXMedLocMediaPolicyVlanID"),
        ("LLDP-EXT-MED-MIB", "lldpXMedLocMediaPolicyPriority"),
        ("LLDP-EXT-MED-MIB", "lldpXMedLocMediaPolicyDscp"),
        ("LLDP-EXT-MED-MIB", "lldpXMedLocMediaPolicyUnknown"),
        ("LLDP-EXT-MED-MIB", "lldpXMedLocMediaPolicyTagged"))
)
if mibBuilder.loadTexts:
    lldpXMedOptMediaPolicyGroup.setStatus("current")

lldpXMedOptInventoryGroup = ObjectGroup(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4795, 2, 2, 3)
)
lldpXMedOptInventoryGroup.setObjects(
      *(("LLDP-EXT-MED-MIB", "lldpXMedLocHardwareRev"),
        ("LLDP-EXT-MED-MIB", "lldpXMedLocFirmwareRev"),
        ("LLDP-EXT-MED-MIB", "lldpXMedLocSoftwareRev"),
        ("LLDP-EXT-MED-MIB", "lldpXMedLocSerialNum"),
        ("LLDP-EXT-MED-MIB", "lldpXMedLocMfgName"),
        ("LLDP-EXT-MED-MIB", "lldpXMedLocModelName"),
        ("LLDP-EXT-MED-MIB", "lldpXMedLocAssetID"))
)
if mibBuilder.loadTexts:
    lldpXMedOptInventoryGroup.setStatus("current")

lldpXMedOptLocationGroup = ObjectGroup(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4795, 2, 2, 4)
)
lldpXMedOptLocationGroup.setObjects(
    ("LLDP-EXT-MED-MIB", "lldpXMedLocLocationInfo")
)
if mibBuilder.loadTexts:
    lldpXMedOptLocationGroup.setStatus("current")

lldpXMedOptPoEPSEGroup = ObjectGroup(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4795, 2, 2, 5)
)
lldpXMedOptPoEPSEGroup.setObjects(
      *(("LLDP-EXT-MED-MIB", "lldpXMedLocXPoEPSEPortPowerAv"),
        ("LLDP-EXT-MED-MIB", "lldpXMedLocXPoEPSEPortPDPriority"),
        ("LLDP-EXT-MED-MIB", "lldpXMedLocXPoEPSEPowerSource"))
)
if mibBuilder.loadTexts:
    lldpXMedOptPoEPSEGroup.setStatus("current")

lldpXMedOptPoEPDGroup = ObjectGroup(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4795, 2, 2, 6)
)
lldpXMedOptPoEPDGroup.setObjects(
      *(("LLDP-EXT-MED-MIB", "lldpXMedLocXPoEPDPowerReq"),
        ("LLDP-EXT-MED-MIB", "lldpXMedLocXPoEPDPowerSource"),
        ("LLDP-EXT-MED-MIB", "lldpXMedLocXPoEPDPowerPriority"))
)
if mibBuilder.loadTexts:
    lldpXMedOptPoEPDGroup.setStatus("current")

lldpXMedRemSysGroup = ObjectGroup(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4795, 2, 2, 7)
)
lldpXMedRemSysGroup.setObjects(
      *(("LLDP-EXT-MED-MIB", "lldpXMedRemCapSupported"),
        ("LLDP-EXT-MED-MIB", "lldpXMedRemCapCurrent"),
        ("LLDP-EXT-MED-MIB", "lldpXMedRemDeviceClass"),
        ("LLDP-EXT-MED-MIB", "lldpXMedRemMediaPolicyVlanID"),
        ("LLDP-EXT-MED-MIB", "lldpXMedRemMediaPolicyPriority"),
        ("LLDP-EXT-MED-MIB", "lldpXMedRemMediaPolicyDscp"),
        ("LLDP-EXT-MED-MIB", "lldpXMedRemMediaPolicyUnknown"),
        ("LLDP-EXT-MED-MIB", "lldpXMedRemMediaPolicyTagged"),
        ("LLDP-EXT-MED-MIB", "lldpXMedRemHardwareRev"),
        ("LLDP-EXT-MED-MIB", "lldpXMedRemFirmwareRev"),
        ("LLDP-EXT-MED-MIB", "lldpXMedRemSoftwareRev"),
        ("LLDP-EXT-MED-MIB", "lldpXMedRemSerialNum"),
        ("LLDP-EXT-MED-MIB", "lldpXMedRemMfgName"),
        ("LLDP-EXT-MED-MIB", "lldpXMedRemModelName"),
        ("LLDP-EXT-MED-MIB", "lldpXMedRemAssetID"),
        ("LLDP-EXT-MED-MIB", "lldpXMedRemLocationInfo"),
        ("LLDP-EXT-MED-MIB", "lldpXMedRemXPoEDeviceType"),
        ("LLDP-EXT-MED-MIB", "lldpXMedRemXPoEPSEPowerAv"),
        ("LLDP-EXT-MED-MIB", "lldpXMedRemXPoEPSEPowerSource"),
        ("LLDP-EXT-MED-MIB", "lldpXMedRemXPoEPSEPowerPriority"),
        ("LLDP-EXT-MED-MIB", "lldpXMedRemXPoEPDPowerReq"),
        ("LLDP-EXT-MED-MIB", "lldpXMedRemXPoEPDPowerSource"),
        ("LLDP-EXT-MED-MIB", "lldpXMedRemXPoEPDPowerPriority"))
)
if mibBuilder.loadTexts:
    lldpXMedRemSysGroup.setStatus("current")


# Notification objects

lldpXMedTopologyChangeDetected = NotificationType(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4795, 0, 1)
)
lldpXMedTopologyChangeDetected.setObjects(
      *(("LLDP-MIB", "lldpRemChassisIdSubtype"),
        ("LLDP-MIB", "lldpRemChassisId"),
        ("LLDP-EXT-MED-MIB", "lldpXMedRemDeviceClass"))
)
if mibBuilder.loadTexts:
    lldpXMedTopologyChangeDetected.setStatus(
        "current"
    )


# Notifications groups

lldpXMedNotificationsGroup = NotificationGroup(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4795, 2, 2, 8)
)
lldpXMedNotificationsGroup.setObjects(
    ("LLDP-EXT-MED-MIB", "lldpXMedTopologyChangeDetected")
)
if mibBuilder.loadTexts:
    lldpXMedNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

lldpXMedCompliance = ModuleCompliance(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4795, 2, 1, 1)
)
if mibBuilder.loadTexts:
    lldpXMedCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LLDP-EXT-MED-MIB",
    **{"LldpXMedDeviceClass": LldpXMedDeviceClass,
       "LldpXMedCapabilities": LldpXMedCapabilities,
       "LocationSubtype": LocationSubtype,
       "PolicyAppType": PolicyAppType,
       "lldpXMedMIB": lldpXMedMIB,
       "lldpXMedNotifications": lldpXMedNotifications,
       "lldpXMedTopologyChangeDetected": lldpXMedTopologyChangeDetected,
       "lldpXMedObjects": lldpXMedObjects,
       "lldpXMedConfig": lldpXMedConfig,
       "lldpXMedLocDeviceClass": lldpXMedLocDeviceClass,
       "lldpXMedPortConfigTable": lldpXMedPortConfigTable,
       "lldpXMedPortConfigEntry": lldpXMedPortConfigEntry,
       "lldpXMedPortCapSupported": lldpXMedPortCapSupported,
       "lldpXMedPortConfigTLVsTxEnable": lldpXMedPortConfigTLVsTxEnable,
       "lldpXMedPortConfigNotifEnable": lldpXMedPortConfigNotifEnable,
       "lldpXMedFastStartRepeatCount": lldpXMedFastStartRepeatCount,
       "lldpXMedLocalData": lldpXMedLocalData,
       "lldpXMedLocMediaPolicyTable": lldpXMedLocMediaPolicyTable,
       "lldpXMedLocMediaPolicyEntry": lldpXMedLocMediaPolicyEntry,
       "lldpXMedLocMediaPolicyAppType": lldpXMedLocMediaPolicyAppType,
       "lldpXMedLocMediaPolicyVlanID": lldpXMedLocMediaPolicyVlanID,
       "lldpXMedLocMediaPolicyPriority": lldpXMedLocMediaPolicyPriority,
       "lldpXMedLocMediaPolicyDscp": lldpXMedLocMediaPolicyDscp,
       "lldpXMedLocMediaPolicyUnknown": lldpXMedLocMediaPolicyUnknown,
       "lldpXMedLocMediaPolicyTagged": lldpXMedLocMediaPolicyTagged,
       "lldpXMedLocHardwareRev": lldpXMedLocHardwareRev,
       "lldpXMedLocFirmwareRev": lldpXMedLocFirmwareRev,
       "lldpXMedLocSoftwareRev": lldpXMedLocSoftwareRev,
       "lldpXMedLocSerialNum": lldpXMedLocSerialNum,
       "lldpXMedLocMfgName": lldpXMedLocMfgName,
       "lldpXMedLocModelName": lldpXMedLocModelName,
       "lldpXMedLocAssetID": lldpXMedLocAssetID,
       "lldpXMedLocLocationTable": lldpXMedLocLocationTable,
       "lldpXMedLocLocationEntry": lldpXMedLocLocationEntry,
       "lldpXMedLocLocationSubtype": lldpXMedLocLocationSubtype,
       "lldpXMedLocLocationInfo": lldpXMedLocLocationInfo,
       "lldpXMedLocXPoEDeviceType": lldpXMedLocXPoEDeviceType,
       "lldpXMedLocXPoEPSEPortTable": lldpXMedLocXPoEPSEPortTable,
       "lldpXMedLocXPoEPSEPortEntry": lldpXMedLocXPoEPSEPortEntry,
       "lldpXMedLocXPoEPSEPortPowerAv": lldpXMedLocXPoEPSEPortPowerAv,
       "lldpXMedLocXPoEPSEPortPDPriority": lldpXMedLocXPoEPSEPortPDPriority,
       "lldpXMedLocXPoEPSEPowerSource": lldpXMedLocXPoEPSEPowerSource,
       "lldpXMedLocXPoEPDPowerReq": lldpXMedLocXPoEPDPowerReq,
       "lldpXMedLocXPoEPDPowerSource": lldpXMedLocXPoEPDPowerSource,
       "lldpXMedLocXPoEPDPowerPriority": lldpXMedLocXPoEPDPowerPriority,
       "lldpXMedRemoteData": lldpXMedRemoteData,
       "lldpXMedRemCapabilitiesTable": lldpXMedRemCapabilitiesTable,
       "lldpXMedRemCapabilitiesEntry": lldpXMedRemCapabilitiesEntry,
       "lldpXMedRemCapSupported": lldpXMedRemCapSupported,
       "lldpXMedRemCapCurrent": lldpXMedRemCapCurrent,
       "lldpXMedRemDeviceClass": lldpXMedRemDeviceClass,
       "lldpXMedRemMediaPolicyTable": lldpXMedRemMediaPolicyTable,
       "lldpXMedRemMediaPolicyEntry": lldpXMedRemMediaPolicyEntry,
       "lldpXMedRemMediaPolicyAppType": lldpXMedRemMediaPolicyAppType,
       "lldpXMedRemMediaPolicyVlanID": lldpXMedRemMediaPolicyVlanID,
       "lldpXMedRemMediaPolicyPriority": lldpXMedRemMediaPolicyPriority,
       "lldpXMedRemMediaPolicyDscp": lldpXMedRemMediaPolicyDscp,
       "lldpXMedRemMediaPolicyUnknown": lldpXMedRemMediaPolicyUnknown,
       "lldpXMedRemMediaPolicyTagged": lldpXMedRemMediaPolicyTagged,
       "lldpXMedRemInventoryTable": lldpXMedRemInventoryTable,
       "lldpXMedRemInventoryEntry": lldpXMedRemInventoryEntry,
       "lldpXMedRemHardwareRev": lldpXMedRemHardwareRev,
       "lldpXMedRemFirmwareRev": lldpXMedRemFirmwareRev,
       "lldpXMedRemSoftwareRev": lldpXMedRemSoftwareRev,
       "lldpXMedRemSerialNum": lldpXMedRemSerialNum,
       "lldpXMedRemMfgName": lldpXMedRemMfgName,
       "lldpXMedRemModelName": lldpXMedRemModelName,
       "lldpXMedRemAssetID": lldpXMedRemAssetID,
       "lldpXMedRemLocationTable": lldpXMedRemLocationTable,
       "lldpXMedRemLocationEntry": lldpXMedRemLocationEntry,
       "lldpXMedRemLocationSubtype": lldpXMedRemLocationSubtype,
       "lldpXMedRemLocationInfo": lldpXMedRemLocationInfo,
       "lldpXMedRemXPoETable": lldpXMedRemXPoETable,
       "lldpXMedRemXPoEEntry": lldpXMedRemXPoEEntry,
       "lldpXMedRemXPoEDeviceType": lldpXMedRemXPoEDeviceType,
       "lldpXMedRemXPoEPSETable": lldpXMedRemXPoEPSETable,
       "lldpXMedRemXPoEPSEEntry": lldpXMedRemXPoEPSEEntry,
       "lldpXMedRemXPoEPSEPowerAv": lldpXMedRemXPoEPSEPowerAv,
       "lldpXMedRemXPoEPSEPowerSource": lldpXMedRemXPoEPSEPowerSource,
       "lldpXMedRemXPoEPSEPowerPriority": lldpXMedRemXPoEPSEPowerPriority,
       "lldpXMedRemXPoEPDTable": lldpXMedRemXPoEPDTable,
       "lldpXMedRemXPoEPDEntry": lldpXMedRemXPoEPDEntry,
       "lldpXMedRemXPoEPDPowerReq": lldpXMedRemXPoEPDPowerReq,
       "lldpXMedRemXPoEPDPowerSource": lldpXMedRemXPoEPDPowerSource,
       "lldpXMedRemXPoEPDPowerPriority": lldpXMedRemXPoEPDPowerPriority,
       "lldpXMedConformance": lldpXMedConformance,
       "lldpXMedCompliances": lldpXMedCompliances,
       "lldpXMedCompliance": lldpXMedCompliance,
       "lldpXMedGroups": lldpXMedGroups,
       "lldpXMedConfigGroup": lldpXMedConfigGroup,
       "lldpXMedOptMediaPolicyGroup": lldpXMedOptMediaPolicyGroup,
       "lldpXMedOptInventoryGroup": lldpXMedOptInventoryGroup,
       "lldpXMedOptLocationGroup": lldpXMedOptLocationGroup,
       "lldpXMedOptPoEPSEGroup": lldpXMedOptPoEPSEGroup,
       "lldpXMedOptPoEPDGroup": lldpXMedOptPoEPDGroup,
       "lldpXMedRemSysGroup": lldpXMedRemSysGroup,
       "lldpXMedNotificationsGroup": lldpXMedNotificationsGroup}
)
