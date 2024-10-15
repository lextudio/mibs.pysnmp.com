# SNMP MIB module (CLAB-GW-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CLAB-GW-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:15:39 2024
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

(clabCommonMibs,) = mibBuilder.importSymbols(
    "CLAB-DEF-MIB",
    "clabCommonMibs")

(InetAddressIPv4,
 InetAddressIPv6,
 InetAddressPrefixLength) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressIPv4",
    "InetAddressIPv6",
    "InetAddressPrefixLength")

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

(DateAndTime,
 DisplayString,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

clabGWMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 4, 6)
)
clabGWMib.setRevisions(
        ("2016-08-04 00:00",
         "2016-02-24 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ClabGWNotifications_ObjectIdentity = ObjectIdentity
clabGWNotifications = _ClabGWNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 4, 6, 0)
)
_ClabGWMibObjects_ObjectIdentity = ObjectIdentity
clabGWMibObjects = _ClabGWMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 4, 6, 1)
)
_ClabGWDeviceInfoObjects_ObjectIdentity = ObjectIdentity
clabGWDeviceInfoObjects = _ClabGWDeviceInfoObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 4, 6, 1, 1)
)


class _ClabGWDeviceInfoManufacturer_Type(SnmpAdminString):
    """Custom type clabGWDeviceInfoManufacturer based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_ClabGWDeviceInfoManufacturer_Type.__name__ = "SnmpAdminString"
_ClabGWDeviceInfoManufacturer_Object = MibScalar
clabGWDeviceInfoManufacturer = _ClabGWDeviceInfoManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 6, 1, 1, 1),
    _ClabGWDeviceInfoManufacturer_Type()
)
clabGWDeviceInfoManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabGWDeviceInfoManufacturer.setStatus("current")


class _ClabGWDeviceInfoManufacturerOUI_Type(SnmpAdminString):
    """Custom type clabGWDeviceInfoManufacturerOUI based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_ClabGWDeviceInfoManufacturerOUI_Type.__name__ = "SnmpAdminString"
_ClabGWDeviceInfoManufacturerOUI_Object = MibScalar
clabGWDeviceInfoManufacturerOUI = _ClabGWDeviceInfoManufacturerOUI_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 6, 1, 1, 2),
    _ClabGWDeviceInfoManufacturerOUI_Type()
)
clabGWDeviceInfoManufacturerOUI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabGWDeviceInfoManufacturerOUI.setStatus("current")


class _ClabGWDeviceInfoDeviceCategory_Type(SnmpAdminString):
    """Custom type clabGWDeviceInfoDeviceCategory based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(127, 127),
    )


_ClabGWDeviceInfoDeviceCategory_Type.__name__ = "SnmpAdminString"
_ClabGWDeviceInfoDeviceCategory_Object = MibScalar
clabGWDeviceInfoDeviceCategory = _ClabGWDeviceInfoDeviceCategory_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 6, 1, 1, 3),
    _ClabGWDeviceInfoDeviceCategory_Type()
)
clabGWDeviceInfoDeviceCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabGWDeviceInfoDeviceCategory.setStatus("current")


class _ClabGWDeviceInfoModelName_Type(SnmpAdminString):
    """Custom type clabGWDeviceInfoModelName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_ClabGWDeviceInfoModelName_Type.__name__ = "SnmpAdminString"
_ClabGWDeviceInfoModelName_Object = MibScalar
clabGWDeviceInfoModelName = _ClabGWDeviceInfoModelName_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 6, 1, 1, 4),
    _ClabGWDeviceInfoModelName_Type()
)
clabGWDeviceInfoModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabGWDeviceInfoModelName.setStatus("current")


class _ClabGWDeviceInfoModelNumber_Type(SnmpAdminString):
    """Custom type clabGWDeviceInfoModelNumber based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_ClabGWDeviceInfoModelNumber_Type.__name__ = "SnmpAdminString"
_ClabGWDeviceInfoModelNumber_Object = MibScalar
clabGWDeviceInfoModelNumber = _ClabGWDeviceInfoModelNumber_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 6, 1, 1, 5),
    _ClabGWDeviceInfoModelNumber_Type()
)
clabGWDeviceInfoModelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabGWDeviceInfoModelNumber.setStatus("current")


class _ClabGWDeviceInfoDescription_Type(SnmpAdminString):
    """Custom type clabGWDeviceInfoDescription based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(255, 255),
    )


_ClabGWDeviceInfoDescription_Type.__name__ = "SnmpAdminString"
_ClabGWDeviceInfoDescription_Object = MibScalar
clabGWDeviceInfoDescription = _ClabGWDeviceInfoDescription_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 6, 1, 1, 6),
    _ClabGWDeviceInfoDescription_Type()
)
clabGWDeviceInfoDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabGWDeviceInfoDescription.setStatus("current")


class _ClabGWDeviceInfoProductClass_Type(SnmpAdminString):
    """Custom type clabGWDeviceInfoProductClass based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_ClabGWDeviceInfoProductClass_Type.__name__ = "SnmpAdminString"
_ClabGWDeviceInfoProductClass_Object = MibScalar
clabGWDeviceInfoProductClass = _ClabGWDeviceInfoProductClass_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 6, 1, 1, 7),
    _ClabGWDeviceInfoProductClass_Type()
)
clabGWDeviceInfoProductClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabGWDeviceInfoProductClass.setStatus("current")


class _ClabGWDeviceInfoSerialNumber_Type(SnmpAdminString):
    """Custom type clabGWDeviceInfoSerialNumber based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_ClabGWDeviceInfoSerialNumber_Type.__name__ = "SnmpAdminString"
_ClabGWDeviceInfoSerialNumber_Object = MibScalar
clabGWDeviceInfoSerialNumber = _ClabGWDeviceInfoSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 6, 1, 1, 8),
    _ClabGWDeviceInfoSerialNumber_Type()
)
clabGWDeviceInfoSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabGWDeviceInfoSerialNumber.setStatus("current")


class _ClabGWDeviceInfoHardwareVersion_Type(SnmpAdminString):
    """Custom type clabGWDeviceInfoHardwareVersion based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_ClabGWDeviceInfoHardwareVersion_Type.__name__ = "SnmpAdminString"
_ClabGWDeviceInfoHardwareVersion_Object = MibScalar
clabGWDeviceInfoHardwareVersion = _ClabGWDeviceInfoHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 6, 1, 1, 9),
    _ClabGWDeviceInfoHardwareVersion_Type()
)
clabGWDeviceInfoHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabGWDeviceInfoHardwareVersion.setStatus("current")


class _ClabGWDeviceInfoSoftwareVersion_Type(SnmpAdminString):
    """Custom type clabGWDeviceInfoSoftwareVersion based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_ClabGWDeviceInfoSoftwareVersion_Type.__name__ = "SnmpAdminString"
_ClabGWDeviceInfoSoftwareVersion_Object = MibScalar
clabGWDeviceInfoSoftwareVersion = _ClabGWDeviceInfoSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 6, 1, 1, 10),
    _ClabGWDeviceInfoSoftwareVersion_Type()
)
clabGWDeviceInfoSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabGWDeviceInfoSoftwareVersion.setStatus("current")


class _ClabGWDeviceInfoAdditionalHardwareVersion_Type(SnmpAdminString):
    """Custom type clabGWDeviceInfoAdditionalHardwareVersion based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_ClabGWDeviceInfoAdditionalHardwareVersion_Type.__name__ = "SnmpAdminString"
_ClabGWDeviceInfoAdditionalHardwareVersion_Object = MibScalar
clabGWDeviceInfoAdditionalHardwareVersion = _ClabGWDeviceInfoAdditionalHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 6, 1, 1, 11),
    _ClabGWDeviceInfoAdditionalHardwareVersion_Type()
)
clabGWDeviceInfoAdditionalHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabGWDeviceInfoAdditionalHardwareVersion.setStatus("current")


class _ClabGWDeviceInfoAdditonalSoftwareVersion_Type(SnmpAdminString):
    """Custom type clabGWDeviceInfoAdditonalSoftwareVersion based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_ClabGWDeviceInfoAdditonalSoftwareVersion_Type.__name__ = "SnmpAdminString"
_ClabGWDeviceInfoAdditonalSoftwareVersion_Object = MibScalar
clabGWDeviceInfoAdditonalSoftwareVersion = _ClabGWDeviceInfoAdditonalSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 6, 1, 1, 12),
    _ClabGWDeviceInfoAdditonalSoftwareVersion_Type()
)
clabGWDeviceInfoAdditonalSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabGWDeviceInfoAdditonalSoftwareVersion.setStatus("current")


class _ClabGWDeviceInfoProvisioningCode_Type(SnmpAdminString):
    """Custom type clabGWDeviceInfoProvisioningCode based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_ClabGWDeviceInfoProvisioningCode_Type.__name__ = "SnmpAdminString"
_ClabGWDeviceInfoProvisioningCode_Object = MibScalar
clabGWDeviceInfoProvisioningCode = _ClabGWDeviceInfoProvisioningCode_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 6, 1, 1, 13),
    _ClabGWDeviceInfoProvisioningCode_Type()
)
clabGWDeviceInfoProvisioningCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clabGWDeviceInfoProvisioningCode.setStatus("current")
_ClabGWDeviceInfoUpTime_Type = TimeTicks
_ClabGWDeviceInfoUpTime_Object = MibScalar
clabGWDeviceInfoUpTime = _ClabGWDeviceInfoUpTime_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 6, 1, 1, 14),
    _ClabGWDeviceInfoUpTime_Type()
)
clabGWDeviceInfoUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabGWDeviceInfoUpTime.setStatus("current")
_ClabGWDeviceInfoFirstUseDate_Type = DateAndTime
_ClabGWDeviceInfoFirstUseDate_Object = MibScalar
clabGWDeviceInfoFirstUseDate = _ClabGWDeviceInfoFirstUseDate_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 6, 1, 1, 15),
    _ClabGWDeviceInfoFirstUseDate_Type()
)
clabGWDeviceInfoFirstUseDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabGWDeviceInfoFirstUseDate.setStatus("current")


class _ClabGWDevicePublicAccessEnabled_Type(TruthValue):
    """Custom type clabGWDevicePublicAccessEnabled based on TruthValue"""


_ClabGWDevicePublicAccessEnabled_Object = MibScalar
clabGWDevicePublicAccessEnabled = _ClabGWDevicePublicAccessEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 6, 1, 1, 16),
    _ClabGWDevicePublicAccessEnabled_Type()
)
clabGWDevicePublicAccessEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clabGWDevicePublicAccessEnabled.setStatus("current")
_ClabGWDNSObjects_ObjectIdentity = ObjectIdentity
clabGWDNSObjects = _ClabGWDNSObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 4, 6, 1, 2)
)


class _ClabGWDeviceDNSIpv6QueryForDualMode_Type(TruthValue):
    """Custom type clabGWDeviceDNSIpv6QueryForDualMode based on TruthValue"""


_ClabGWDeviceDNSIpv6QueryForDualMode_Object = MibScalar
clabGWDeviceDNSIpv6QueryForDualMode = _ClabGWDeviceDNSIpv6QueryForDualMode_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 6, 1, 2, 1),
    _ClabGWDeviceDNSIpv6QueryForDualMode_Type()
)
clabGWDeviceDNSIpv6QueryForDualMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clabGWDeviceDNSIpv6QueryForDualMode.setStatus("current")
_ClabGWMAPObjects_ObjectIdentity = ObjectIdentity
clabGWMAPObjects = _ClabGWMAPObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 4, 6, 1, 3)
)


class _ClabGWMAPEnable_Type(TruthValue):
    """Custom type clabGWMAPEnable based on TruthValue"""


_ClabGWMAPEnable_Object = MibScalar
clabGWMAPEnable = _ClabGWMAPEnable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 6, 1, 3, 1),
    _ClabGWMAPEnable_Type()
)
clabGWMAPEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clabGWMAPEnable.setStatus("current")


class _ClabGWMAPTunnelDomainNumEntries_Type(Unsigned32):
    """Custom type clabGWMAPTunnelDomainNumEntries based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_ClabGWMAPTunnelDomainNumEntries_Type.__name__ = "Unsigned32"
_ClabGWMAPTunnelDomainNumEntries_Object = MibScalar
clabGWMAPTunnelDomainNumEntries = _ClabGWMAPTunnelDomainNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 6, 1, 3, 2),
    _ClabGWMAPTunnelDomainNumEntries_Type()
)
clabGWMAPTunnelDomainNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabGWMAPTunnelDomainNumEntries.setStatus("current")
_ClabGWMAPDomainTable_Object = MibTable
clabGWMAPDomainTable = _ClabGWMAPDomainTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 6, 1, 3, 3)
)
if mibBuilder.loadTexts:
    clabGWMAPDomainTable.setStatus("current")
_ClabGWMAPDomainEntry_Object = MibTableRow
clabGWMAPDomainEntry = _ClabGWMAPDomainEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 6, 1, 3, 3, 1)
)
clabGWMAPDomainEntry.setIndexNames(
    (0, "CLAB-GW-MIB", "clabGWMAPDomainIndex"),
)
if mibBuilder.loadTexts:
    clabGWMAPDomainEntry.setStatus("current")


class _ClabGWMAPDomainIndex_Type(Unsigned32):
    """Custom type clabGWMAPDomainIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_ClabGWMAPDomainIndex_Type.__name__ = "Unsigned32"
_ClabGWMAPDomainIndex_Object = MibTableColumn
clabGWMAPDomainIndex = _ClabGWMAPDomainIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 6, 1, 3, 3, 1, 1),
    _ClabGWMAPDomainIndex_Type()
)
clabGWMAPDomainIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clabGWMAPDomainIndex.setStatus("current")


class _ClabGWMAPDomainEnable_Type(TruthValue):
    """Custom type clabGWMAPDomainEnable based on TruthValue"""


_ClabGWMAPDomainEnable_Object = MibTableColumn
clabGWMAPDomainEnable = _ClabGWMAPDomainEnable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 6, 1, 3, 3, 1, 2),
    _ClabGWMAPDomainEnable_Type()
)
clabGWMAPDomainEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabGWMAPDomainEnable.setStatus("current")


class _ClabGWMAPDomainStatus_Type(Integer32):
    """Custom type clabGWMAPDomainStatus based on Integer32"""
    defaultValue = 1

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
        *(("disabled", 1),
          ("enabled", 2),
          ("error", 4),
          ("errorMisconfigured", 3))
    )


_ClabGWMAPDomainStatus_Type.__name__ = "Integer32"
_ClabGWMAPDomainStatus_Object = MibTableColumn
clabGWMAPDomainStatus = _ClabGWMAPDomainStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 6, 1, 3, 3, 1, 3),
    _ClabGWMAPDomainStatus_Type()
)
clabGWMAPDomainStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabGWMAPDomainStatus.setStatus("current")


class _ClabGWMAPDomainAlias_Type(OctetString):
    """Custom type clabGWMAPDomainAlias based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ClabGWMAPDomainAlias_Type.__name__ = "OctetString"
_ClabGWMAPDomainAlias_Object = MibTableColumn
clabGWMAPDomainAlias = _ClabGWMAPDomainAlias_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 6, 1, 3, 3, 1, 4),
    _ClabGWMAPDomainAlias_Type()
)
clabGWMAPDomainAlias.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabGWMAPDomainAlias.setStatus("current")


class _ClabGWMAPDomainTransportMode_Type(Integer32):
    """Custom type clabGWMAPDomainTransportMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("encapsulation", 1),
          ("translation", 2))
    )


_ClabGWMAPDomainTransportMode_Type.__name__ = "Integer32"
_ClabGWMAPDomainTransportMode_Object = MibTableColumn
clabGWMAPDomainTransportMode = _ClabGWMAPDomainTransportMode_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 6, 1, 3, 3, 1, 5),
    _ClabGWMAPDomainTransportMode_Type()
)
clabGWMAPDomainTransportMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabGWMAPDomainTransportMode.setStatus("current")


class _ClabGWMAPDomainWANInterface_Type(OctetString):
    """Custom type clabGWMAPDomainWANInterface based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_ClabGWMAPDomainWANInterface_Type.__name__ = "OctetString"
_ClabGWMAPDomainWANInterface_Object = MibTableColumn
clabGWMAPDomainWANInterface = _ClabGWMAPDomainWANInterface_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 6, 1, 3, 3, 1, 6),
    _ClabGWMAPDomainWANInterface_Type()
)
clabGWMAPDomainWANInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabGWMAPDomainWANInterface.setStatus("current")


class _ClabGWMAPDomainIPv6Prefix_Type(InetAddressIPv6):
    """Custom type clabGWMAPDomainIPv6Prefix based on InetAddressIPv6"""
    defaultHexValue = "0000000000000000"


_ClabGWMAPDomainIPv6Prefix_Object = MibTableColumn
clabGWMAPDomainIPv6Prefix = _ClabGWMAPDomainIPv6Prefix_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 6, 1, 3, 3, 1, 7),
    _ClabGWMAPDomainIPv6Prefix_Type()
)
clabGWMAPDomainIPv6Prefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabGWMAPDomainIPv6Prefix.setStatus("current")


class _ClabGWMAPDomainIPv6PrefixLen_Type(InetAddressPrefixLength):
    """Custom type clabGWMAPDomainIPv6PrefixLen based on InetAddressPrefixLength"""
    defaultValue = 0


_ClabGWMAPDomainIPv6PrefixLen_Object = MibTableColumn
clabGWMAPDomainIPv6PrefixLen = _ClabGWMAPDomainIPv6PrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 6, 1, 3, 3, 1, 8),
    _ClabGWMAPDomainIPv6PrefixLen_Type()
)
clabGWMAPDomainIPv6PrefixLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabGWMAPDomainIPv6PrefixLen.setStatus("current")


class _ClabGWMAPDomainBRIPv6Prefix_Type(InetAddressIPv6):
    """Custom type clabGWMAPDomainBRIPv6Prefix based on InetAddressIPv6"""
    defaultHexValue = "0000000000000000"


_ClabGWMAPDomainBRIPv6Prefix_Object = MibTableColumn
clabGWMAPDomainBRIPv6Prefix = _ClabGWMAPDomainBRIPv6Prefix_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 6, 1, 3, 3, 1, 9),
    _ClabGWMAPDomainBRIPv6Prefix_Type()
)
clabGWMAPDomainBRIPv6Prefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabGWMAPDomainBRIPv6Prefix.setStatus("current")


class _ClabGWMAPDomainBRIPv6PrefixLen_Type(InetAddressPrefixLength):
    """Custom type clabGWMAPDomainBRIPv6PrefixLen based on InetAddressPrefixLength"""
    defaultValue = 64


_ClabGWMAPDomainBRIPv6PrefixLen_Object = MibTableColumn
clabGWMAPDomainBRIPv6PrefixLen = _ClabGWMAPDomainBRIPv6PrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 6, 1, 3, 3, 1, 10),
    _ClabGWMAPDomainBRIPv6PrefixLen_Type()
)
clabGWMAPDomainBRIPv6PrefixLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabGWMAPDomainBRIPv6PrefixLen.setStatus("current")


class _ClabGWMAPDomainDSCPMarkPolicy_Type(Integer32):
    """Custom type clabGWMAPDomainDSCPMarkPolicy based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, 63),
    )


_ClabGWMAPDomainDSCPMarkPolicy_Type.__name__ = "Integer32"
_ClabGWMAPDomainDSCPMarkPolicy_Object = MibTableColumn
clabGWMAPDomainDSCPMarkPolicy = _ClabGWMAPDomainDSCPMarkPolicy_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 6, 1, 3, 3, 1, 11),
    _ClabGWMAPDomainDSCPMarkPolicy_Type()
)
clabGWMAPDomainDSCPMarkPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabGWMAPDomainDSCPMarkPolicy.setStatus("current")


class _ClabGWMAPDomainIncludeSystemPorts_Type(TruthValue):
    """Custom type clabGWMAPDomainIncludeSystemPorts based on TruthValue"""


_ClabGWMAPDomainIncludeSystemPorts_Object = MibTableColumn
clabGWMAPDomainIncludeSystemPorts = _ClabGWMAPDomainIncludeSystemPorts_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 6, 1, 3, 3, 1, 12),
    _ClabGWMAPDomainIncludeSystemPorts_Type()
)
clabGWMAPDomainIncludeSystemPorts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabGWMAPDomainIncludeSystemPorts.setStatus("current")


class _ClabGWMAPDomainRuleNumEntries_Type(Unsigned32):
    """Custom type clabGWMAPDomainRuleNumEntries based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ClabGWMAPDomainRuleNumEntries_Type.__name__ = "Unsigned32"
_ClabGWMAPDomainRuleNumEntries_Object = MibTableColumn
clabGWMAPDomainRuleNumEntries = _ClabGWMAPDomainRuleNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 6, 1, 3, 3, 1, 13),
    _ClabGWMAPDomainRuleNumEntries_Type()
)
clabGWMAPDomainRuleNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabGWMAPDomainRuleNumEntries.setStatus("current")
_ClabGWMAPDomainRowStatus_Type = RowStatus
_ClabGWMAPDomainRowStatus_Object = MibTableColumn
clabGWMAPDomainRowStatus = _ClabGWMAPDomainRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 6, 1, 3, 3, 1, 14),
    _ClabGWMAPDomainRowStatus_Type()
)
clabGWMAPDomainRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabGWMAPDomainRowStatus.setStatus("current")
_ClabGWMAPDomainRuleTable_Object = MibTable
clabGWMAPDomainRuleTable = _ClabGWMAPDomainRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 6, 1, 3, 4)
)
if mibBuilder.loadTexts:
    clabGWMAPDomainRuleTable.setStatus("current")
_ClabGWMAPDomainRuleEntry_Object = MibTableRow
clabGWMAPDomainRuleEntry = _ClabGWMAPDomainRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 6, 1, 3, 4, 1)
)
clabGWMAPDomainRuleEntry.setIndexNames(
    (0, "CLAB-GW-MIB", "clabGWMAPDomainIndex"),
    (0, "CLAB-GW-MIB", "clabGWMAPDomainRuleIndex"),
)
if mibBuilder.loadTexts:
    clabGWMAPDomainRuleEntry.setStatus("current")


class _ClabGWMAPDomainRuleIndex_Type(Unsigned32):
    """Custom type clabGWMAPDomainRuleIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_ClabGWMAPDomainRuleIndex_Type.__name__ = "Unsigned32"
_ClabGWMAPDomainRuleIndex_Object = MibTableColumn
clabGWMAPDomainRuleIndex = _ClabGWMAPDomainRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 6, 1, 3, 4, 1, 1),
    _ClabGWMAPDomainRuleIndex_Type()
)
clabGWMAPDomainRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clabGWMAPDomainRuleIndex.setStatus("current")


class _ClabGWMAPDomainRuleEnable_Type(TruthValue):
    """Custom type clabGWMAPDomainRuleEnable based on TruthValue"""


_ClabGWMAPDomainRuleEnable_Object = MibTableColumn
clabGWMAPDomainRuleEnable = _ClabGWMAPDomainRuleEnable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 6, 1, 3, 4, 1, 2),
    _ClabGWMAPDomainRuleEnable_Type()
)
clabGWMAPDomainRuleEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabGWMAPDomainRuleEnable.setStatus("current")


class _ClabGWMAPDomainRuleStatus_Type(Integer32):
    """Custom type clabGWMAPDomainRuleStatus based on Integer32"""
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
        *(("disabled", 1),
          ("enabled", 2),
          ("error", 3))
    )


_ClabGWMAPDomainRuleStatus_Type.__name__ = "Integer32"
_ClabGWMAPDomainRuleStatus_Object = MibTableColumn
clabGWMAPDomainRuleStatus = _ClabGWMAPDomainRuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 6, 1, 3, 4, 1, 3),
    _ClabGWMAPDomainRuleStatus_Type()
)
clabGWMAPDomainRuleStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabGWMAPDomainRuleStatus.setStatus("current")


class _ClabGWMAPDomainRuleAlias_Type(OctetString):
    """Custom type clabGWMAPDomainRuleAlias based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ClabGWMAPDomainRuleAlias_Type.__name__ = "OctetString"
_ClabGWMAPDomainRuleAlias_Object = MibTableColumn
clabGWMAPDomainRuleAlias = _ClabGWMAPDomainRuleAlias_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 6, 1, 3, 4, 1, 4),
    _ClabGWMAPDomainRuleAlias_Type()
)
clabGWMAPDomainRuleAlias.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabGWMAPDomainRuleAlias.setStatus("current")


class _ClabGWMAPDomainRuleOrigin_Type(Integer32):
    """Custom type clabGWMAPDomainRuleOrigin based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dhcpv6", 1),
          ("static", 2))
    )


_ClabGWMAPDomainRuleOrigin_Type.__name__ = "Integer32"
_ClabGWMAPDomainRuleOrigin_Object = MibTableColumn
clabGWMAPDomainRuleOrigin = _ClabGWMAPDomainRuleOrigin_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 6, 1, 3, 4, 1, 5),
    _ClabGWMAPDomainRuleOrigin_Type()
)
clabGWMAPDomainRuleOrigin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabGWMAPDomainRuleOrigin.setStatus("current")
_ClabGWMAPDomainRuleIPv6Prefix_Type = InetAddressIPv6
_ClabGWMAPDomainRuleIPv6Prefix_Object = MibTableColumn
clabGWMAPDomainRuleIPv6Prefix = _ClabGWMAPDomainRuleIPv6Prefix_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 6, 1, 3, 4, 1, 6),
    _ClabGWMAPDomainRuleIPv6Prefix_Type()
)
clabGWMAPDomainRuleIPv6Prefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabGWMAPDomainRuleIPv6Prefix.setStatus("current")


class _ClabGWMAPDomainRuleIPv6PrefixLen_Type(InetAddressPrefixLength):
    """Custom type clabGWMAPDomainRuleIPv6PrefixLen based on InetAddressPrefixLength"""
    defaultValue = 0


_ClabGWMAPDomainRuleIPv6PrefixLen_Object = MibTableColumn
clabGWMAPDomainRuleIPv6PrefixLen = _ClabGWMAPDomainRuleIPv6PrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 6, 1, 3, 4, 1, 7),
    _ClabGWMAPDomainRuleIPv6PrefixLen_Type()
)
clabGWMAPDomainRuleIPv6PrefixLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabGWMAPDomainRuleIPv6PrefixLen.setStatus("current")


class _ClabGWMAPDomainRuleIPv4Prefix_Type(InetAddressIPv4):
    """Custom type clabGWMAPDomainRuleIPv4Prefix based on InetAddressIPv4"""
    defaultHexValue = "00000000"


_ClabGWMAPDomainRuleIPv4Prefix_Object = MibTableColumn
clabGWMAPDomainRuleIPv4Prefix = _ClabGWMAPDomainRuleIPv4Prefix_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 6, 1, 3, 4, 1, 8),
    _ClabGWMAPDomainRuleIPv4Prefix_Type()
)
clabGWMAPDomainRuleIPv4Prefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabGWMAPDomainRuleIPv4Prefix.setStatus("current")


class _ClabGWMAPDomainRuleIPv4PrefixLen_Type(InetAddressPrefixLength):
    """Custom type clabGWMAPDomainRuleIPv4PrefixLen based on InetAddressPrefixLength"""
    defaultValue = 0


_ClabGWMAPDomainRuleIPv4PrefixLen_Object = MibTableColumn
clabGWMAPDomainRuleIPv4PrefixLen = _ClabGWMAPDomainRuleIPv4PrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 6, 1, 3, 4, 1, 9),
    _ClabGWMAPDomainRuleIPv4PrefixLen_Type()
)
clabGWMAPDomainRuleIPv4PrefixLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabGWMAPDomainRuleIPv4PrefixLen.setStatus("current")


class _ClabGWMAPDomainRuleEABitsLength_Type(Unsigned32):
    """Custom type clabGWMAPDomainRuleEABitsLength based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 48),
    )


_ClabGWMAPDomainRuleEABitsLength_Type.__name__ = "Unsigned32"
_ClabGWMAPDomainRuleEABitsLength_Object = MibTableColumn
clabGWMAPDomainRuleEABitsLength = _ClabGWMAPDomainRuleEABitsLength_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 6, 1, 3, 4, 1, 10),
    _ClabGWMAPDomainRuleEABitsLength_Type()
)
clabGWMAPDomainRuleEABitsLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabGWMAPDomainRuleEABitsLength.setStatus("current")


class _ClabGWMAPDomainRuleIsFMR_Type(TruthValue):
    """Custom type clabGWMAPDomainRuleIsFMR based on TruthValue"""


_ClabGWMAPDomainRuleIsFMR_Object = MibTableColumn
clabGWMAPDomainRuleIsFMR = _ClabGWMAPDomainRuleIsFMR_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 6, 1, 3, 4, 1, 11),
    _ClabGWMAPDomainRuleIsFMR_Type()
)
clabGWMAPDomainRuleIsFMR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabGWMAPDomainRuleIsFMR.setStatus("current")


class _ClabGWMAPDomainRulePSIDOffset_Type(Unsigned32):
    """Custom type clabGWMAPDomainRulePSIDOffset based on Unsigned32"""
    defaultValue = 6

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_ClabGWMAPDomainRulePSIDOffset_Type.__name__ = "Unsigned32"
_ClabGWMAPDomainRulePSIDOffset_Object = MibTableColumn
clabGWMAPDomainRulePSIDOffset = _ClabGWMAPDomainRulePSIDOffset_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 6, 1, 3, 4, 1, 12),
    _ClabGWMAPDomainRulePSIDOffset_Type()
)
clabGWMAPDomainRulePSIDOffset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabGWMAPDomainRulePSIDOffset.setStatus("current")


class _ClabGWMAPDomainRulePSIDLength_Type(Unsigned32):
    """Custom type clabGWMAPDomainRulePSIDLength based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_ClabGWMAPDomainRulePSIDLength_Type.__name__ = "Unsigned32"
_ClabGWMAPDomainRulePSIDLength_Object = MibTableColumn
clabGWMAPDomainRulePSIDLength = _ClabGWMAPDomainRulePSIDLength_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 6, 1, 3, 4, 1, 13),
    _ClabGWMAPDomainRulePSIDLength_Type()
)
clabGWMAPDomainRulePSIDLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabGWMAPDomainRulePSIDLength.setStatus("current")


class _ClabGWMAPDomainRulePSID_Type(Unsigned32):
    """Custom type clabGWMAPDomainRulePSID based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ClabGWMAPDomainRulePSID_Type.__name__ = "Unsigned32"
_ClabGWMAPDomainRulePSID_Object = MibTableColumn
clabGWMAPDomainRulePSID = _ClabGWMAPDomainRulePSID_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 6, 1, 3, 4, 1, 14),
    _ClabGWMAPDomainRulePSID_Type()
)
clabGWMAPDomainRulePSID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabGWMAPDomainRulePSID.setStatus("current")
_ClabGWMAPDomainRuleRowStatus_Type = RowStatus
_ClabGWMAPDomainRuleRowStatus_Object = MibTableColumn
clabGWMAPDomainRuleRowStatus = _ClabGWMAPDomainRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 6, 1, 3, 4, 1, 15),
    _ClabGWMAPDomainRuleRowStatus_Type()
)
clabGWMAPDomainRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabGWMAPDomainRuleRowStatus.setStatus("current")
_ClabGWMAPDomainIfTable_Object = MibTable
clabGWMAPDomainIfTable = _ClabGWMAPDomainIfTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 6, 1, 3, 5)
)
if mibBuilder.loadTexts:
    clabGWMAPDomainIfTable.setStatus("current")
_ClabGWMAPDomainIfEntry_Object = MibTableRow
clabGWMAPDomainIfEntry = _ClabGWMAPDomainIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 6, 1, 3, 5, 1)
)
clabGWMAPDomainIfEntry.setIndexNames(
    (0, "CLAB-GW-MIB", "clabGWMAPDomainIndex"),
)
if mibBuilder.loadTexts:
    clabGWMAPDomainIfEntry.setStatus("current")


class _ClabGWMAPDomainIfIndex_Type(Unsigned32):
    """Custom type clabGWMAPDomainIfIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_ClabGWMAPDomainIfIndex_Type.__name__ = "Unsigned32"
_ClabGWMAPDomainIfIndex_Object = MibTableColumn
clabGWMAPDomainIfIndex = _ClabGWMAPDomainIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 6, 1, 3, 5, 1, 1),
    _ClabGWMAPDomainIfIndex_Type()
)
clabGWMAPDomainIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clabGWMAPDomainIfIndex.setStatus("current")


class _ClabGWMAPDomainIfEnable_Type(TruthValue):
    """Custom type clabGWMAPDomainIfEnable based on TruthValue"""


_ClabGWMAPDomainIfEnable_Object = MibTableColumn
clabGWMAPDomainIfEnable = _ClabGWMAPDomainIfEnable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 6, 1, 3, 5, 1, 2),
    _ClabGWMAPDomainIfEnable_Type()
)
clabGWMAPDomainIfEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabGWMAPDomainIfEnable.setStatus("current")


class _ClabGWMAPDomainIfStatus_Type(Integer32):
    """Custom type clabGWMAPDomainIfStatus based on Integer32"""
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
        *(("dormant", 4),
          ("down", 2),
          ("error", 7),
          ("lowerLayerDown", 6),
          ("notPresent", 5),
          ("unknown", 3),
          ("up", 1))
    )


_ClabGWMAPDomainIfStatus_Type.__name__ = "Integer32"
_ClabGWMAPDomainIfStatus_Object = MibTableColumn
clabGWMAPDomainIfStatus = _ClabGWMAPDomainIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 6, 1, 3, 5, 1, 3),
    _ClabGWMAPDomainIfStatus_Type()
)
clabGWMAPDomainIfStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabGWMAPDomainIfStatus.setStatus("current")


class _ClabGWMAPDomainIfAlias_Type(OctetString):
    """Custom type clabGWMAPDomainIfAlias based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ClabGWMAPDomainIfAlias_Type.__name__ = "OctetString"
_ClabGWMAPDomainIfAlias_Object = MibTableColumn
clabGWMAPDomainIfAlias = _ClabGWMAPDomainIfAlias_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 6, 1, 3, 5, 1, 4),
    _ClabGWMAPDomainIfAlias_Type()
)
clabGWMAPDomainIfAlias.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabGWMAPDomainIfAlias.setStatus("current")


class _ClabGWMAPDomainIfName_Type(OctetString):
    """Custom type clabGWMAPDomainIfName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ClabGWMAPDomainIfName_Type.__name__ = "OctetString"
_ClabGWMAPDomainIfName_Object = MibTableColumn
clabGWMAPDomainIfName = _ClabGWMAPDomainIfName_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 6, 1, 3, 5, 1, 5),
    _ClabGWMAPDomainIfName_Type()
)
clabGWMAPDomainIfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabGWMAPDomainIfName.setStatus("current")
_ClabGWMAPDomainIfLastChange_Type = Unsigned32
_ClabGWMAPDomainIfLastChange_Object = MibTableColumn
clabGWMAPDomainIfLastChange = _ClabGWMAPDomainIfLastChange_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 6, 1, 3, 5, 1, 6),
    _ClabGWMAPDomainIfLastChange_Type()
)
clabGWMAPDomainIfLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabGWMAPDomainIfLastChange.setStatus("current")
if mibBuilder.loadTexts:
    clabGWMAPDomainIfLastChange.setUnits("seconds")


class _ClabGWMAPDomainIfLowerLayers_Type(OctetString):
    """Custom type clabGWMAPDomainIfLowerLayers based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_ClabGWMAPDomainIfLowerLayers_Type.__name__ = "OctetString"
_ClabGWMAPDomainIfLowerLayers_Object = MibTableColumn
clabGWMAPDomainIfLowerLayers = _ClabGWMAPDomainIfLowerLayers_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 6, 1, 3, 5, 1, 7),
    _ClabGWMAPDomainIfLowerLayers_Type()
)
clabGWMAPDomainIfLowerLayers.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabGWMAPDomainIfLowerLayers.setStatus("current")
_ClabGWMAPDomainIfRowStatus_Type = RowStatus
_ClabGWMAPDomainIfRowStatus_Object = MibTableColumn
clabGWMAPDomainIfRowStatus = _ClabGWMAPDomainIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 6, 1, 3, 5, 1, 8),
    _ClabGWMAPDomainIfRowStatus_Type()
)
clabGWMAPDomainIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabGWMAPDomainIfRowStatus.setStatus("current")
_ClabGWMAPDomainIfStatsTable_Object = MibTable
clabGWMAPDomainIfStatsTable = _ClabGWMAPDomainIfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 6, 1, 3, 6)
)
if mibBuilder.loadTexts:
    clabGWMAPDomainIfStatsTable.setStatus("current")
_ClabGWMAPDomainIfStatsEntry_Object = MibTableRow
clabGWMAPDomainIfStatsEntry = _ClabGWMAPDomainIfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 6, 1, 3, 6, 1)
)
clabGWMAPDomainIfStatsEntry.setIndexNames(
    (0, "CLAB-GW-MIB", "clabGWMAPDomainIndex"),
)
if mibBuilder.loadTexts:
    clabGWMAPDomainIfStatsEntry.setStatus("current")
_ClabGWMAPDomainIfStatsBytesSent_Type = Counter64
_ClabGWMAPDomainIfStatsBytesSent_Object = MibTableColumn
clabGWMAPDomainIfStatsBytesSent = _ClabGWMAPDomainIfStatsBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 6, 1, 3, 6, 1, 1),
    _ClabGWMAPDomainIfStatsBytesSent_Type()
)
clabGWMAPDomainIfStatsBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabGWMAPDomainIfStatsBytesSent.setStatus("current")
if mibBuilder.loadTexts:
    clabGWMAPDomainIfStatsBytesSent.setUnits("bytes")
_ClabGWMAPDomainIfStatsBytesRcvd_Type = Counter64
_ClabGWMAPDomainIfStatsBytesRcvd_Object = MibTableColumn
clabGWMAPDomainIfStatsBytesRcvd = _ClabGWMAPDomainIfStatsBytesRcvd_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 6, 1, 3, 6, 1, 2),
    _ClabGWMAPDomainIfStatsBytesRcvd_Type()
)
clabGWMAPDomainIfStatsBytesRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabGWMAPDomainIfStatsBytesRcvd.setStatus("current")
if mibBuilder.loadTexts:
    clabGWMAPDomainIfStatsBytesRcvd.setUnits("bytes")
_ClabGWMAPDomainIfStatsPktSent_Type = Counter64
_ClabGWMAPDomainIfStatsPktSent_Object = MibTableColumn
clabGWMAPDomainIfStatsPktSent = _ClabGWMAPDomainIfStatsPktSent_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 6, 1, 3, 6, 1, 3),
    _ClabGWMAPDomainIfStatsPktSent_Type()
)
clabGWMAPDomainIfStatsPktSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabGWMAPDomainIfStatsPktSent.setStatus("current")
if mibBuilder.loadTexts:
    clabGWMAPDomainIfStatsPktSent.setUnits("packets")
_ClabGWMAPDomainIfStatsPktRcvd_Type = Counter64
_ClabGWMAPDomainIfStatsPktRcvd_Object = MibTableColumn
clabGWMAPDomainIfStatsPktRcvd = _ClabGWMAPDomainIfStatsPktRcvd_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 6, 1, 3, 6, 1, 4),
    _ClabGWMAPDomainIfStatsPktRcvd_Type()
)
clabGWMAPDomainIfStatsPktRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabGWMAPDomainIfStatsPktRcvd.setStatus("current")
if mibBuilder.loadTexts:
    clabGWMAPDomainIfStatsPktRcvd.setUnits("packets")
_ClabGWMAPDomainIfStatsErrorsSent_Type = Counter64
_ClabGWMAPDomainIfStatsErrorsSent_Object = MibTableColumn
clabGWMAPDomainIfStatsErrorsSent = _ClabGWMAPDomainIfStatsErrorsSent_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 6, 1, 3, 6, 1, 5),
    _ClabGWMAPDomainIfStatsErrorsSent_Type()
)
clabGWMAPDomainIfStatsErrorsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabGWMAPDomainIfStatsErrorsSent.setStatus("current")
if mibBuilder.loadTexts:
    clabGWMAPDomainIfStatsErrorsSent.setUnits("packets")
_ClabGWMAPDomainIfStatsErrsRcvd_Type = Counter64
_ClabGWMAPDomainIfStatsErrsRcvd_Object = MibTableColumn
clabGWMAPDomainIfStatsErrsRcvd = _ClabGWMAPDomainIfStatsErrsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 6, 1, 3, 6, 1, 6),
    _ClabGWMAPDomainIfStatsErrsRcvd_Type()
)
clabGWMAPDomainIfStatsErrsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabGWMAPDomainIfStatsErrsRcvd.setStatus("current")
if mibBuilder.loadTexts:
    clabGWMAPDomainIfStatsErrsRcvd.setUnits("packets")
_ClabGWMAPDomainIfStatsUcastPktSent_Type = Counter64
_ClabGWMAPDomainIfStatsUcastPktSent_Object = MibTableColumn
clabGWMAPDomainIfStatsUcastPktSent = _ClabGWMAPDomainIfStatsUcastPktSent_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 6, 1, 3, 6, 1, 7),
    _ClabGWMAPDomainIfStatsUcastPktSent_Type()
)
clabGWMAPDomainIfStatsUcastPktSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabGWMAPDomainIfStatsUcastPktSent.setStatus("current")
if mibBuilder.loadTexts:
    clabGWMAPDomainIfStatsUcastPktSent.setUnits("packets")
_ClabGWMAPDomainIfStatsUcastPktRcvd_Type = Counter64
_ClabGWMAPDomainIfStatsUcastPktRcvd_Object = MibTableColumn
clabGWMAPDomainIfStatsUcastPktRcvd = _ClabGWMAPDomainIfStatsUcastPktRcvd_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 6, 1, 3, 6, 1, 8),
    _ClabGWMAPDomainIfStatsUcastPktRcvd_Type()
)
clabGWMAPDomainIfStatsUcastPktRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabGWMAPDomainIfStatsUcastPktRcvd.setStatus("current")
if mibBuilder.loadTexts:
    clabGWMAPDomainIfStatsUcastPktRcvd.setUnits("packets")
_ClabGWMAPDomainIfStatsDcardPktSent_Type = Counter64
_ClabGWMAPDomainIfStatsDcardPktSent_Object = MibTableColumn
clabGWMAPDomainIfStatsDcardPktSent = _ClabGWMAPDomainIfStatsDcardPktSent_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 6, 1, 3, 6, 1, 9),
    _ClabGWMAPDomainIfStatsDcardPktSent_Type()
)
clabGWMAPDomainIfStatsDcardPktSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabGWMAPDomainIfStatsDcardPktSent.setStatus("current")
if mibBuilder.loadTexts:
    clabGWMAPDomainIfStatsDcardPktSent.setUnits("packets")
_ClabGWMAPDomainIfStatsDcardPktRcvd_Type = Counter64
_ClabGWMAPDomainIfStatsDcardPktRcvd_Object = MibTableColumn
clabGWMAPDomainIfStatsDcardPktRcvd = _ClabGWMAPDomainIfStatsDcardPktRcvd_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 6, 1, 3, 6, 1, 10),
    _ClabGWMAPDomainIfStatsDcardPktRcvd_Type()
)
clabGWMAPDomainIfStatsDcardPktRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabGWMAPDomainIfStatsDcardPktRcvd.setStatus("current")
if mibBuilder.loadTexts:
    clabGWMAPDomainIfStatsDcardPktRcvd.setUnits("packets")
_ClabGWMAPDomainIfStatsMcastPktSent_Type = Counter64
_ClabGWMAPDomainIfStatsMcastPktSent_Object = MibTableColumn
clabGWMAPDomainIfStatsMcastPktSent = _ClabGWMAPDomainIfStatsMcastPktSent_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 6, 1, 3, 6, 1, 11),
    _ClabGWMAPDomainIfStatsMcastPktSent_Type()
)
clabGWMAPDomainIfStatsMcastPktSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabGWMAPDomainIfStatsMcastPktSent.setStatus("current")
if mibBuilder.loadTexts:
    clabGWMAPDomainIfStatsMcastPktSent.setUnits("packets")
_ClabGWMAPDomainIfStatsMcastPktRcvd_Type = Counter64
_ClabGWMAPDomainIfStatsMcastPktRcvd_Object = MibTableColumn
clabGWMAPDomainIfStatsMcastPktRcvd = _ClabGWMAPDomainIfStatsMcastPktRcvd_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 6, 1, 3, 6, 1, 12),
    _ClabGWMAPDomainIfStatsMcastPktRcvd_Type()
)
clabGWMAPDomainIfStatsMcastPktRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabGWMAPDomainIfStatsMcastPktRcvd.setStatus("current")
if mibBuilder.loadTexts:
    clabGWMAPDomainIfStatsMcastPktRcvd.setUnits("packets")
_ClabGWMAPDomainIfStatsBcastPktSent_Type = Counter64
_ClabGWMAPDomainIfStatsBcastPktSent_Object = MibTableColumn
clabGWMAPDomainIfStatsBcastPktSent = _ClabGWMAPDomainIfStatsBcastPktSent_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 6, 1, 3, 6, 1, 13),
    _ClabGWMAPDomainIfStatsBcastPktSent_Type()
)
clabGWMAPDomainIfStatsBcastPktSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabGWMAPDomainIfStatsBcastPktSent.setStatus("current")
if mibBuilder.loadTexts:
    clabGWMAPDomainIfStatsBcastPktSent.setUnits("packets")
_ClabGWMAPDomainIfStatsBcastPktRcvd_Type = Counter64
_ClabGWMAPDomainIfStatsBcastPktRcvd_Object = MibTableColumn
clabGWMAPDomainIfStatsBcastPktRcvd = _ClabGWMAPDomainIfStatsBcastPktRcvd_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 6, 1, 3, 6, 1, 14),
    _ClabGWMAPDomainIfStatsBcastPktRcvd_Type()
)
clabGWMAPDomainIfStatsBcastPktRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabGWMAPDomainIfStatsBcastPktRcvd.setStatus("current")
if mibBuilder.loadTexts:
    clabGWMAPDomainIfStatsBcastPktRcvd.setUnits("packets")
_ClabGWMAPDomainIfStatsUkwnProtoPkt_Type = Counter64
_ClabGWMAPDomainIfStatsUkwnProtoPkt_Object = MibTableColumn
clabGWMAPDomainIfStatsUkwnProtoPkt = _ClabGWMAPDomainIfStatsUkwnProtoPkt_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 6, 1, 3, 6, 1, 15),
    _ClabGWMAPDomainIfStatsUkwnProtoPkt_Type()
)
clabGWMAPDomainIfStatsUkwnProtoPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabGWMAPDomainIfStatsUkwnProtoPkt.setStatus("current")
if mibBuilder.loadTexts:
    clabGWMAPDomainIfStatsUkwnProtoPkt.setUnits("packets")
_ClabGWMAPDomainIfStatsInvV4Pkts_Type = Counter64
_ClabGWMAPDomainIfStatsInvV4Pkts_Object = MibTableColumn
clabGWMAPDomainIfStatsInvV4Pkts = _ClabGWMAPDomainIfStatsInvV4Pkts_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 6, 1, 3, 6, 1, 16),
    _ClabGWMAPDomainIfStatsInvV4Pkts_Type()
)
clabGWMAPDomainIfStatsInvV4Pkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabGWMAPDomainIfStatsInvV4Pkts.setStatus("current")
if mibBuilder.loadTexts:
    clabGWMAPDomainIfStatsInvV4Pkts.setUnits("packets")
_ClabGWMibConformance_ObjectIdentity = ObjectIdentity
clabGWMibConformance = _ClabGWMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 4, 6, 2)
)
_ClabGWMibCompliances_ObjectIdentity = ObjectIdentity
clabGWMibCompliances = _ClabGWMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 4, 6, 2, 1)
)
_ClabGWMibGroups_ObjectIdentity = ObjectIdentity
clabGWMibGroups = _ClabGWMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 4, 6, 2, 2)
)

# Managed Objects groups

clabGWGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 4, 6, 2, 2, 1)
)
clabGWGroup.setObjects(
      *(("CLAB-GW-MIB", "clabGWDeviceInfoManufacturer"),
        ("CLAB-GW-MIB", "clabGWDeviceInfoManufacturerOUI"),
        ("CLAB-GW-MIB", "clabGWDeviceInfoDeviceCategory"),
        ("CLAB-GW-MIB", "clabGWDeviceInfoModelName"),
        ("CLAB-GW-MIB", "clabGWDeviceInfoModelNumber"),
        ("CLAB-GW-MIB", "clabGWDeviceInfoDescription"),
        ("CLAB-GW-MIB", "clabGWDeviceInfoProductClass"),
        ("CLAB-GW-MIB", "clabGWDeviceInfoSerialNumber"),
        ("CLAB-GW-MIB", "clabGWDeviceInfoHardwareVersion"),
        ("CLAB-GW-MIB", "clabGWDeviceInfoSoftwareVersion"),
        ("CLAB-GW-MIB", "clabGWDeviceInfoAdditionalHardwareVersion"),
        ("CLAB-GW-MIB", "clabGWDeviceInfoAdditonalSoftwareVersion"),
        ("CLAB-GW-MIB", "clabGWDeviceInfoProvisioningCode"),
        ("CLAB-GW-MIB", "clabGWDeviceInfoUpTime"),
        ("CLAB-GW-MIB", "clabGWDeviceInfoFirstUseDate"),
        ("CLAB-GW-MIB", "clabGWDevicePublicAccessEnabled"))
)
if mibBuilder.loadTexts:
    clabGWGroup.setStatus("current")

clabGWDNSGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 4, 6, 2, 2, 3)
)
clabGWDNSGroup.setObjects(
    ("CLAB-GW-MIB", "clabGWDeviceDNSIpv6QueryForDualMode")
)
if mibBuilder.loadTexts:
    clabGWDNSGroup.setStatus("current")

clabGWMAPGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 4, 6, 2, 2, 4)
)
clabGWMAPGroup.setObjects(
      *(("CLAB-GW-MIB", "clabGWMAPEnable"),
        ("CLAB-GW-MIB", "clabGWMAPTunnelDomainNumEntries"),
        ("CLAB-GW-MIB", "clabGWMAPDomainEnable"),
        ("CLAB-GW-MIB", "clabGWMAPDomainStatus"),
        ("CLAB-GW-MIB", "clabGWMAPDomainAlias"),
        ("CLAB-GW-MIB", "clabGWMAPDomainTransportMode"),
        ("CLAB-GW-MIB", "clabGWMAPDomainWANInterface"),
        ("CLAB-GW-MIB", "clabGWMAPDomainIPv6Prefix"),
        ("CLAB-GW-MIB", "clabGWMAPDomainIPv6PrefixLen"),
        ("CLAB-GW-MIB", "clabGWMAPDomainBRIPv6Prefix"),
        ("CLAB-GW-MIB", "clabGWMAPDomainBRIPv6PrefixLen"),
        ("CLAB-GW-MIB", "clabGWMAPDomainDSCPMarkPolicy"),
        ("CLAB-GW-MIB", "clabGWMAPDomainIncludeSystemPorts"),
        ("CLAB-GW-MIB", "clabGWMAPDomainRuleNumEntries"),
        ("CLAB-GW-MIB", "clabGWMAPDomainRowStatus"),
        ("CLAB-GW-MIB", "clabGWMAPDomainRuleEnable"),
        ("CLAB-GW-MIB", "clabGWMAPDomainRuleStatus"),
        ("CLAB-GW-MIB", "clabGWMAPDomainRuleAlias"),
        ("CLAB-GW-MIB", "clabGWMAPDomainRuleOrigin"),
        ("CLAB-GW-MIB", "clabGWMAPDomainRuleIPv6Prefix"),
        ("CLAB-GW-MIB", "clabGWMAPDomainRuleIPv6PrefixLen"),
        ("CLAB-GW-MIB", "clabGWMAPDomainRuleIPv4Prefix"),
        ("CLAB-GW-MIB", "clabGWMAPDomainRuleIPv4PrefixLen"),
        ("CLAB-GW-MIB", "clabGWMAPDomainRuleEABitsLength"),
        ("CLAB-GW-MIB", "clabGWMAPDomainRuleIsFMR"),
        ("CLAB-GW-MIB", "clabGWMAPDomainRulePSIDOffset"),
        ("CLAB-GW-MIB", "clabGWMAPDomainRulePSIDLength"),
        ("CLAB-GW-MIB", "clabGWMAPDomainRulePSID"),
        ("CLAB-GW-MIB", "clabGWMAPDomainRuleRowStatus"),
        ("CLAB-GW-MIB", "clabGWMAPDomainIfEnable"),
        ("CLAB-GW-MIB", "clabGWMAPDomainIfStatus"),
        ("CLAB-GW-MIB", "clabGWMAPDomainIfAlias"),
        ("CLAB-GW-MIB", "clabGWMAPDomainIfName"),
        ("CLAB-GW-MIB", "clabGWMAPDomainIfLastChange"),
        ("CLAB-GW-MIB", "clabGWMAPDomainIfLowerLayers"),
        ("CLAB-GW-MIB", "clabGWMAPDomainIfRowStatus"),
        ("CLAB-GW-MIB", "clabGWMAPDomainIfStatsBytesSent"),
        ("CLAB-GW-MIB", "clabGWMAPDomainIfStatsBytesRcvd"),
        ("CLAB-GW-MIB", "clabGWMAPDomainIfStatsPktSent"),
        ("CLAB-GW-MIB", "clabGWMAPDomainIfStatsPktRcvd"),
        ("CLAB-GW-MIB", "clabGWMAPDomainIfStatsErrorsSent"),
        ("CLAB-GW-MIB", "clabGWMAPDomainIfStatsErrsRcvd"),
        ("CLAB-GW-MIB", "clabGWMAPDomainIfStatsUcastPktSent"),
        ("CLAB-GW-MIB", "clabGWMAPDomainIfStatsUcastPktRcvd"),
        ("CLAB-GW-MIB", "clabGWMAPDomainIfStatsDcardPktSent"),
        ("CLAB-GW-MIB", "clabGWMAPDomainIfStatsDcardPktRcvd"),
        ("CLAB-GW-MIB", "clabGWMAPDomainIfStatsMcastPktSent"),
        ("CLAB-GW-MIB", "clabGWMAPDomainIfStatsMcastPktRcvd"),
        ("CLAB-GW-MIB", "clabGWMAPDomainIfStatsBcastPktSent"),
        ("CLAB-GW-MIB", "clabGWMAPDomainIfStatsBcastPktRcvd"),
        ("CLAB-GW-MIB", "clabGWMAPDomainIfStatsUkwnProtoPkt"),
        ("CLAB-GW-MIB", "clabGWMAPDomainIfStatsInvV4Pkts"))
)
if mibBuilder.loadTexts:
    clabGWMAPGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

clabGWCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4491, 4, 6, 2, 1, 1)
)
if mibBuilder.loadTexts:
    clabGWCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CLAB-GW-MIB",
    **{"clabGWMib": clabGWMib,
       "clabGWNotifications": clabGWNotifications,
       "clabGWMibObjects": clabGWMibObjects,
       "clabGWDeviceInfoObjects": clabGWDeviceInfoObjects,
       "clabGWDeviceInfoManufacturer": clabGWDeviceInfoManufacturer,
       "clabGWDeviceInfoManufacturerOUI": clabGWDeviceInfoManufacturerOUI,
       "clabGWDeviceInfoDeviceCategory": clabGWDeviceInfoDeviceCategory,
       "clabGWDeviceInfoModelName": clabGWDeviceInfoModelName,
       "clabGWDeviceInfoModelNumber": clabGWDeviceInfoModelNumber,
       "clabGWDeviceInfoDescription": clabGWDeviceInfoDescription,
       "clabGWDeviceInfoProductClass": clabGWDeviceInfoProductClass,
       "clabGWDeviceInfoSerialNumber": clabGWDeviceInfoSerialNumber,
       "clabGWDeviceInfoHardwareVersion": clabGWDeviceInfoHardwareVersion,
       "clabGWDeviceInfoSoftwareVersion": clabGWDeviceInfoSoftwareVersion,
       "clabGWDeviceInfoAdditionalHardwareVersion": clabGWDeviceInfoAdditionalHardwareVersion,
       "clabGWDeviceInfoAdditonalSoftwareVersion": clabGWDeviceInfoAdditonalSoftwareVersion,
       "clabGWDeviceInfoProvisioningCode": clabGWDeviceInfoProvisioningCode,
       "clabGWDeviceInfoUpTime": clabGWDeviceInfoUpTime,
       "clabGWDeviceInfoFirstUseDate": clabGWDeviceInfoFirstUseDate,
       "clabGWDevicePublicAccessEnabled": clabGWDevicePublicAccessEnabled,
       "clabGWDNSObjects": clabGWDNSObjects,
       "clabGWDeviceDNSIpv6QueryForDualMode": clabGWDeviceDNSIpv6QueryForDualMode,
       "clabGWMAPObjects": clabGWMAPObjects,
       "clabGWMAPEnable": clabGWMAPEnable,
       "clabGWMAPTunnelDomainNumEntries": clabGWMAPTunnelDomainNumEntries,
       "clabGWMAPDomainTable": clabGWMAPDomainTable,
       "clabGWMAPDomainEntry": clabGWMAPDomainEntry,
       "clabGWMAPDomainIndex": clabGWMAPDomainIndex,
       "clabGWMAPDomainEnable": clabGWMAPDomainEnable,
       "clabGWMAPDomainStatus": clabGWMAPDomainStatus,
       "clabGWMAPDomainAlias": clabGWMAPDomainAlias,
       "clabGWMAPDomainTransportMode": clabGWMAPDomainTransportMode,
       "clabGWMAPDomainWANInterface": clabGWMAPDomainWANInterface,
       "clabGWMAPDomainIPv6Prefix": clabGWMAPDomainIPv6Prefix,
       "clabGWMAPDomainIPv6PrefixLen": clabGWMAPDomainIPv6PrefixLen,
       "clabGWMAPDomainBRIPv6Prefix": clabGWMAPDomainBRIPv6Prefix,
       "clabGWMAPDomainBRIPv6PrefixLen": clabGWMAPDomainBRIPv6PrefixLen,
       "clabGWMAPDomainDSCPMarkPolicy": clabGWMAPDomainDSCPMarkPolicy,
       "clabGWMAPDomainIncludeSystemPorts": clabGWMAPDomainIncludeSystemPorts,
       "clabGWMAPDomainRuleNumEntries": clabGWMAPDomainRuleNumEntries,
       "clabGWMAPDomainRowStatus": clabGWMAPDomainRowStatus,
       "clabGWMAPDomainRuleTable": clabGWMAPDomainRuleTable,
       "clabGWMAPDomainRuleEntry": clabGWMAPDomainRuleEntry,
       "clabGWMAPDomainRuleIndex": clabGWMAPDomainRuleIndex,
       "clabGWMAPDomainRuleEnable": clabGWMAPDomainRuleEnable,
       "clabGWMAPDomainRuleStatus": clabGWMAPDomainRuleStatus,
       "clabGWMAPDomainRuleAlias": clabGWMAPDomainRuleAlias,
       "clabGWMAPDomainRuleOrigin": clabGWMAPDomainRuleOrigin,
       "clabGWMAPDomainRuleIPv6Prefix": clabGWMAPDomainRuleIPv6Prefix,
       "clabGWMAPDomainRuleIPv6PrefixLen": clabGWMAPDomainRuleIPv6PrefixLen,
       "clabGWMAPDomainRuleIPv4Prefix": clabGWMAPDomainRuleIPv4Prefix,
       "clabGWMAPDomainRuleIPv4PrefixLen": clabGWMAPDomainRuleIPv4PrefixLen,
       "clabGWMAPDomainRuleEABitsLength": clabGWMAPDomainRuleEABitsLength,
       "clabGWMAPDomainRuleIsFMR": clabGWMAPDomainRuleIsFMR,
       "clabGWMAPDomainRulePSIDOffset": clabGWMAPDomainRulePSIDOffset,
       "clabGWMAPDomainRulePSIDLength": clabGWMAPDomainRulePSIDLength,
       "clabGWMAPDomainRulePSID": clabGWMAPDomainRulePSID,
       "clabGWMAPDomainRuleRowStatus": clabGWMAPDomainRuleRowStatus,
       "clabGWMAPDomainIfTable": clabGWMAPDomainIfTable,
       "clabGWMAPDomainIfEntry": clabGWMAPDomainIfEntry,
       "clabGWMAPDomainIfIndex": clabGWMAPDomainIfIndex,
       "clabGWMAPDomainIfEnable": clabGWMAPDomainIfEnable,
       "clabGWMAPDomainIfStatus": clabGWMAPDomainIfStatus,
       "clabGWMAPDomainIfAlias": clabGWMAPDomainIfAlias,
       "clabGWMAPDomainIfName": clabGWMAPDomainIfName,
       "clabGWMAPDomainIfLastChange": clabGWMAPDomainIfLastChange,
       "clabGWMAPDomainIfLowerLayers": clabGWMAPDomainIfLowerLayers,
       "clabGWMAPDomainIfRowStatus": clabGWMAPDomainIfRowStatus,
       "clabGWMAPDomainIfStatsTable": clabGWMAPDomainIfStatsTable,
       "clabGWMAPDomainIfStatsEntry": clabGWMAPDomainIfStatsEntry,
       "clabGWMAPDomainIfStatsBytesSent": clabGWMAPDomainIfStatsBytesSent,
       "clabGWMAPDomainIfStatsBytesRcvd": clabGWMAPDomainIfStatsBytesRcvd,
       "clabGWMAPDomainIfStatsPktSent": clabGWMAPDomainIfStatsPktSent,
       "clabGWMAPDomainIfStatsPktRcvd": clabGWMAPDomainIfStatsPktRcvd,
       "clabGWMAPDomainIfStatsErrorsSent": clabGWMAPDomainIfStatsErrorsSent,
       "clabGWMAPDomainIfStatsErrsRcvd": clabGWMAPDomainIfStatsErrsRcvd,
       "clabGWMAPDomainIfStatsUcastPktSent": clabGWMAPDomainIfStatsUcastPktSent,
       "clabGWMAPDomainIfStatsUcastPktRcvd": clabGWMAPDomainIfStatsUcastPktRcvd,
       "clabGWMAPDomainIfStatsDcardPktSent": clabGWMAPDomainIfStatsDcardPktSent,
       "clabGWMAPDomainIfStatsDcardPktRcvd": clabGWMAPDomainIfStatsDcardPktRcvd,
       "clabGWMAPDomainIfStatsMcastPktSent": clabGWMAPDomainIfStatsMcastPktSent,
       "clabGWMAPDomainIfStatsMcastPktRcvd": clabGWMAPDomainIfStatsMcastPktRcvd,
       "clabGWMAPDomainIfStatsBcastPktSent": clabGWMAPDomainIfStatsBcastPktSent,
       "clabGWMAPDomainIfStatsBcastPktRcvd": clabGWMAPDomainIfStatsBcastPktRcvd,
       "clabGWMAPDomainIfStatsUkwnProtoPkt": clabGWMAPDomainIfStatsUkwnProtoPkt,
       "clabGWMAPDomainIfStatsInvV4Pkts": clabGWMAPDomainIfStatsInvV4Pkts,
       "clabGWMibConformance": clabGWMibConformance,
       "clabGWMibCompliances": clabGWMibCompliances,
       "clabGWCompliance": clabGWCompliance,
       "clabGWMibGroups": clabGWMibGroups,
       "clabGWGroup": clabGWGroup,
       "clabGWDNSGroup": clabGWDNSGroup,
       "clabGWMAPGroup": clabGWMAPGroup}
)
