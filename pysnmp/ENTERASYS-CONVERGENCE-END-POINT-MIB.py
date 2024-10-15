# SNMP MIB module (ENTERASYS-CONVERGENCE-END-POINT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ENTERASYS-CONVERGENCE-END-POINT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:38:45 2024
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

(etsysModules,) = mibBuilder.importSymbols(
    "ENTERASYS-MIB-NAMES",
    "etsysModules")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

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
 MacAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

etsysConvergenceEndPointMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 40)
)
etsysConvergenceEndPointMIB.setRevisions(
        ("2005-11-18 13:25",
         "2005-10-19 15:49",
         "2005-08-16 12:33",
         "2005-06-16 14:27",
         "2005-03-31 16:10",
         "2003-11-05 19:42")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class ConvEndPointTypes(Bits, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_EtsysConvEndPointObjects_ObjectIdentity = ObjectIdentity
etsysConvEndPointObjects = _EtsysConvEndPointObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 40, 1)
)
_EtsysConvEndPointConfig_ObjectIdentity = ObjectIdentity
etsysConvEndPointConfig = _EtsysConvEndPointConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 40, 1, 1)
)


class _EtsysConvEndPointGlobalConfigEnable_Type(EnabledStatus):
    """Custom type etsysConvEndPointGlobalConfigEnable based on EnabledStatus"""


_EtsysConvEndPointGlobalConfigEnable_Object = MibScalar
etsysConvEndPointGlobalConfigEnable = _EtsysConvEndPointGlobalConfigEnable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 40, 1, 1, 1),
    _EtsysConvEndPointGlobalConfigEnable_Type()
)
etsysConvEndPointGlobalConfigEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysConvEndPointGlobalConfigEnable.setStatus("current")
_EtsysConvEndPointGlobalConfigTable_Object = MibTable
etsysConvEndPointGlobalConfigTable = _EtsysConvEndPointGlobalConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 40, 1, 1, 2)
)
if mibBuilder.loadTexts:
    etsysConvEndPointGlobalConfigTable.setStatus("current")
_EtsysConvEndPointGlobalConfigEntry_Object = MibTableRow
etsysConvEndPointGlobalConfigEntry = _EtsysConvEndPointGlobalConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 40, 1, 1, 2, 1)
)
etsysConvEndPointGlobalConfigEntry.setIndexNames(
    (0, "ENTERASYS-CONVERGENCE-END-POINT-MIB", "etsysConvEndPointGlobalEndPointType"),
)
if mibBuilder.loadTexts:
    etsysConvEndPointGlobalConfigEntry.setStatus("current")
_EtsysConvEndPointGlobalEndPointType_Type = ConvEndPointTypes
_EtsysConvEndPointGlobalEndPointType_Object = MibTableColumn
etsysConvEndPointGlobalEndPointType = _EtsysConvEndPointGlobalEndPointType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 40, 1, 1, 2, 1, 1),
    _EtsysConvEndPointGlobalEndPointType_Type()
)
etsysConvEndPointGlobalEndPointType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysConvEndPointGlobalEndPointType.setStatus("current")


class _EtsysConvEndPointGlobalDefaultPolicyIndex_Type(Integer32):
    """Custom type etsysConvEndPointGlobalDefaultPolicyIndex based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 65535),
    )


_EtsysConvEndPointGlobalDefaultPolicyIndex_Type.__name__ = "Integer32"
_EtsysConvEndPointGlobalDefaultPolicyIndex_Object = MibTableColumn
etsysConvEndPointGlobalDefaultPolicyIndex = _EtsysConvEndPointGlobalDefaultPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 40, 1, 1, 2, 1, 2),
    _EtsysConvEndPointGlobalDefaultPolicyIndex_Type()
)
etsysConvEndPointGlobalDefaultPolicyIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysConvEndPointGlobalDefaultPolicyIndex.setStatus("current")
_EtsysConvEndPointProtocolConfigTable_Object = MibTable
etsysConvEndPointProtocolConfigTable = _EtsysConvEndPointProtocolConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 40, 1, 1, 3)
)
if mibBuilder.loadTexts:
    etsysConvEndPointProtocolConfigTable.setStatus("current")
_EtsysConvEndPointProtocolConfigEntry_Object = MibTableRow
etsysConvEndPointProtocolConfigEntry = _EtsysConvEndPointProtocolConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 40, 1, 1, 3, 1)
)
etsysConvEndPointProtocolConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ENTERASYS-CONVERGENCE-END-POINT-MIB", "etsysConvEndPointProtocolEndPointType"),
)
if mibBuilder.loadTexts:
    etsysConvEndPointProtocolConfigEntry.setStatus("current")
_EtsysConvEndPointProtocolEndPointType_Type = ConvEndPointTypes
_EtsysConvEndPointProtocolEndPointType_Object = MibTableColumn
etsysConvEndPointProtocolEndPointType = _EtsysConvEndPointProtocolEndPointType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 40, 1, 1, 3, 1, 1),
    _EtsysConvEndPointProtocolEndPointType_Type()
)
etsysConvEndPointProtocolEndPointType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysConvEndPointProtocolEndPointType.setStatus("current")


class _EtsysConvEndPointProtocolEnable_Type(EnabledStatus):
    """Custom type etsysConvEndPointProtocolEnable based on EnabledStatus"""


_EtsysConvEndPointProtocolEnable_Object = MibTableColumn
etsysConvEndPointProtocolEnable = _EtsysConvEndPointProtocolEnable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 40, 1, 1, 3, 1, 2),
    _EtsysConvEndPointProtocolEnable_Type()
)
etsysConvEndPointProtocolEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysConvEndPointProtocolEnable.setStatus("current")
_EtsysConvEndPointStatus_ObjectIdentity = ObjectIdentity
etsysConvEndPointStatus = _EtsysConvEndPointStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 40, 1, 2)
)
_EtsysConvEndPointConnMacTable_Object = MibTable
etsysConvEndPointConnMacTable = _EtsysConvEndPointConnMacTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 40, 1, 2, 1)
)
if mibBuilder.loadTexts:
    etsysConvEndPointConnMacTable.setStatus("deprecated")
_EtsysConvEndPointConnMacEntry_Object = MibTableRow
etsysConvEndPointConnMacEntry = _EtsysConvEndPointConnMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 40, 1, 2, 1, 1)
)
etsysConvEndPointConnMacEntry.setIndexNames(
    (0, "ENTERASYS-CONVERGENCE-END-POINT-MIB", "etsysConvEndPointConnMacMacAddress"),
)
if mibBuilder.loadTexts:
    etsysConvEndPointConnMacEntry.setStatus("deprecated")
_EtsysConvEndPointConnMacMacAddress_Type = MacAddress
_EtsysConvEndPointConnMacMacAddress_Object = MibTableColumn
etsysConvEndPointConnMacMacAddress = _EtsysConvEndPointConnMacMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 40, 1, 2, 1, 1, 1),
    _EtsysConvEndPointConnMacMacAddress_Type()
)
etsysConvEndPointConnMacMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysConvEndPointConnMacMacAddress.setStatus("deprecated")
_EtsysConvEndPointConnMacPortNumber_Type = InterfaceIndex
_EtsysConvEndPointConnMacPortNumber_Object = MibTableColumn
etsysConvEndPointConnMacPortNumber = _EtsysConvEndPointConnMacPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 40, 1, 2, 1, 1, 2),
    _EtsysConvEndPointConnMacPortNumber_Type()
)
etsysConvEndPointConnMacPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysConvEndPointConnMacPortNumber.setStatus("deprecated")
_EtsysConvEndPointConnMacEndPointType_Type = ConvEndPointTypes
_EtsysConvEndPointConnMacEndPointType_Object = MibTableColumn
etsysConvEndPointConnMacEndPointType = _EtsysConvEndPointConnMacEndPointType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 40, 1, 2, 1, 1, 3),
    _EtsysConvEndPointConnMacEndPointType_Type()
)
etsysConvEndPointConnMacEndPointType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysConvEndPointConnMacEndPointType.setStatus("deprecated")
_EtsysConvEndPointConnMacPolicyIndex_Type = Integer32
_EtsysConvEndPointConnMacPolicyIndex_Object = MibTableColumn
etsysConvEndPointConnMacPolicyIndex = _EtsysConvEndPointConnMacPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 40, 1, 2, 1, 1, 4),
    _EtsysConvEndPointConnMacPolicyIndex_Type()
)
etsysConvEndPointConnMacPolicyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysConvEndPointConnMacPolicyIndex.setStatus("deprecated")
_EtsysConvEndPointConnMacDiscoveryTime_Type = DateAndTime
_EtsysConvEndPointConnMacDiscoveryTime_Object = MibTableColumn
etsysConvEndPointConnMacDiscoveryTime = _EtsysConvEndPointConnMacDiscoveryTime_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 40, 1, 2, 1, 1, 5),
    _EtsysConvEndPointConnMacDiscoveryTime_Type()
)
etsysConvEndPointConnMacDiscoveryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysConvEndPointConnMacDiscoveryTime.setStatus("deprecated")


class _EtsysConvEndPointConnMacFirmwareVersion_Type(SnmpAdminString):
    """Custom type etsysConvEndPointConnMacFirmwareVersion based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_EtsysConvEndPointConnMacFirmwareVersion_Type.__name__ = "SnmpAdminString"
_EtsysConvEndPointConnMacFirmwareVersion_Object = MibTableColumn
etsysConvEndPointConnMacFirmwareVersion = _EtsysConvEndPointConnMacFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 40, 1, 2, 1, 1, 6),
    _EtsysConvEndPointConnMacFirmwareVersion_Type()
)
etsysConvEndPointConnMacFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysConvEndPointConnMacFirmwareVersion.setStatus("deprecated")


class _EtsysConvEndPointConnMacInetAddressType_Type(InetAddressType):
    """Custom type etsysConvEndPointConnMacInetAddressType based on InetAddressType"""


_EtsysConvEndPointConnMacInetAddressType_Object = MibTableColumn
etsysConvEndPointConnMacInetAddressType = _EtsysConvEndPointConnMacInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 40, 1, 2, 1, 1, 7),
    _EtsysConvEndPointConnMacInetAddressType_Type()
)
etsysConvEndPointConnMacInetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysConvEndPointConnMacInetAddressType.setStatus("deprecated")
_EtsysConvEndPointConnMacInetAddress_Type = InetAddress
_EtsysConvEndPointConnMacInetAddress_Object = MibTableColumn
etsysConvEndPointConnMacInetAddress = _EtsysConvEndPointConnMacInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 40, 1, 2, 1, 1, 8),
    _EtsysConvEndPointConnMacInetAddress_Type()
)
etsysConvEndPointConnMacInetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysConvEndPointConnMacInetAddress.setStatus("deprecated")
_EtsysConvEndPointConnPortTable_Object = MibTable
etsysConvEndPointConnPortTable = _EtsysConvEndPointConnPortTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 40, 1, 2, 2)
)
if mibBuilder.loadTexts:
    etsysConvEndPointConnPortTable.setStatus("current")
_EtsysConvEndPointConnPortEntry_Object = MibTableRow
etsysConvEndPointConnPortEntry = _EtsysConvEndPointConnPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 40, 1, 2, 2, 1)
)
etsysConvEndPointConnPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ENTERASYS-CONVERGENCE-END-POINT-MIB", "etsysConvEndPointConnPortMacAddress"),
)
if mibBuilder.loadTexts:
    etsysConvEndPointConnPortEntry.setStatus("current")
_EtsysConvEndPointConnPortMacAddress_Type = MacAddress
_EtsysConvEndPointConnPortMacAddress_Object = MibTableColumn
etsysConvEndPointConnPortMacAddress = _EtsysConvEndPointConnPortMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 40, 1, 2, 2, 1, 1),
    _EtsysConvEndPointConnPortMacAddress_Type()
)
etsysConvEndPointConnPortMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysConvEndPointConnPortMacAddress.setStatus("current")
_EtsysCEPConnMacTable_Object = MibTable
etsysCEPConnMacTable = _EtsysCEPConnMacTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 40, 1, 2, 3)
)
if mibBuilder.loadTexts:
    etsysCEPConnMacTable.setStatus("current")
_EtsysCEPConnMacEntry_Object = MibTableRow
etsysCEPConnMacEntry = _EtsysCEPConnMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 40, 1, 2, 3, 1)
)
etsysCEPConnMacEntry.setIndexNames(
    (0, "ENTERASYS-CONVERGENCE-END-POINT-MIB", "etsysConvEndPointConnPortMacAddress"),
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    etsysCEPConnMacEntry.setStatus("current")
_EtsysCEPConnMacEndPointType_Type = ConvEndPointTypes
_EtsysCEPConnMacEndPointType_Object = MibTableColumn
etsysCEPConnMacEndPointType = _EtsysCEPConnMacEndPointType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 40, 1, 2, 3, 1, 1),
    _EtsysCEPConnMacEndPointType_Type()
)
etsysCEPConnMacEndPointType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysCEPConnMacEndPointType.setStatus("current")


class _EtsysCEPConnMacPolicyIndex_Type(Integer32):
    """Custom type etsysCEPConnMacPolicyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 65535),
    )


_EtsysCEPConnMacPolicyIndex_Type.__name__ = "Integer32"
_EtsysCEPConnMacPolicyIndex_Object = MibTableColumn
etsysCEPConnMacPolicyIndex = _EtsysCEPConnMacPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 40, 1, 2, 3, 1, 2),
    _EtsysCEPConnMacPolicyIndex_Type()
)
etsysCEPConnMacPolicyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysCEPConnMacPolicyIndex.setStatus("current")
_EtsysCEPConnMacDiscoveryTime_Type = DateAndTime
_EtsysCEPConnMacDiscoveryTime_Object = MibTableColumn
etsysCEPConnMacDiscoveryTime = _EtsysCEPConnMacDiscoveryTime_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 40, 1, 2, 3, 1, 3),
    _EtsysCEPConnMacDiscoveryTime_Type()
)
etsysCEPConnMacDiscoveryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysCEPConnMacDiscoveryTime.setStatus("current")


class _EtsysCEPConnMacFirmwareVersion_Type(SnmpAdminString):
    """Custom type etsysCEPConnMacFirmwareVersion based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_EtsysCEPConnMacFirmwareVersion_Type.__name__ = "SnmpAdminString"
_EtsysCEPConnMacFirmwareVersion_Object = MibTableColumn
etsysCEPConnMacFirmwareVersion = _EtsysCEPConnMacFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 40, 1, 2, 3, 1, 4),
    _EtsysCEPConnMacFirmwareVersion_Type()
)
etsysCEPConnMacFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysCEPConnMacFirmwareVersion.setStatus("current")


class _EtsysCEPConnMacInetAddressType_Type(InetAddressType):
    """Custom type etsysCEPConnMacInetAddressType based on InetAddressType"""


_EtsysCEPConnMacInetAddressType_Object = MibTableColumn
etsysCEPConnMacInetAddressType = _EtsysCEPConnMacInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 40, 1, 2, 3, 1, 5),
    _EtsysCEPConnMacInetAddressType_Type()
)
etsysCEPConnMacInetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysCEPConnMacInetAddressType.setStatus("current")
_EtsysCEPConnMacInetAddress_Type = InetAddress
_EtsysCEPConnMacInetAddress_Object = MibTableColumn
etsysCEPConnMacInetAddress = _EtsysCEPConnMacInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 40, 1, 2, 3, 1, 6),
    _EtsysCEPConnMacInetAddress_Type()
)
etsysCEPConnMacInetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysCEPConnMacInetAddress.setStatus("current")
_EtsysConvEndPointDetection_ObjectIdentity = ObjectIdentity
etsysConvEndPointDetection = _EtsysConvEndPointDetection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 40, 1, 3)
)
_EtsysConvEndPointDetectionMaxEntries_Type = Integer32
_EtsysConvEndPointDetectionMaxEntries_Object = MibScalar
etsysConvEndPointDetectionMaxEntries = _EtsysConvEndPointDetectionMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 40, 1, 3, 1),
    _EtsysConvEndPointDetectionMaxEntries_Type()
)
etsysConvEndPointDetectionMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysConvEndPointDetectionMaxEntries.setStatus("current")
_EtsysConvEndPointDetectionTable_Object = MibTable
etsysConvEndPointDetectionTable = _EtsysConvEndPointDetectionTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 40, 1, 3, 2)
)
if mibBuilder.loadTexts:
    etsysConvEndPointDetectionTable.setStatus("current")
_EtsysConvEndPointDetectionEntry_Object = MibTableRow
etsysConvEndPointDetectionEntry = _EtsysConvEndPointDetectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 40, 1, 3, 2, 1)
)
etsysConvEndPointDetectionEntry.setIndexNames(
    (0, "ENTERASYS-CONVERGENCE-END-POINT-MIB", "etsysConvEndPointDetectionRuleIndex"),
)
if mibBuilder.loadTexts:
    etsysConvEndPointDetectionEntry.setStatus("current")


class _EtsysConvEndPointDetectionRuleIndex_Type(Integer32):
    """Custom type etsysConvEndPointDetectionRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_EtsysConvEndPointDetectionRuleIndex_Type.__name__ = "Integer32"
_EtsysConvEndPointDetectionRuleIndex_Object = MibTableColumn
etsysConvEndPointDetectionRuleIndex = _EtsysConvEndPointDetectionRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 40, 1, 3, 2, 1, 1),
    _EtsysConvEndPointDetectionRuleIndex_Type()
)
etsysConvEndPointDetectionRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysConvEndPointDetectionRuleIndex.setStatus("current")


class _EtsysConvEndPointDetectionEndPointType_Type(Integer32):
    """Custom type etsysConvEndPointDetectionEndPointType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("h323", 0),
          ("siemens", 1),
          ("sip", 2))
    )


_EtsysConvEndPointDetectionEndPointType_Type.__name__ = "Integer32"
_EtsysConvEndPointDetectionEndPointType_Object = MibTableColumn
etsysConvEndPointDetectionEndPointType = _EtsysConvEndPointDetectionEndPointType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 40, 1, 3, 2, 1, 2),
    _EtsysConvEndPointDetectionEndPointType_Type()
)
etsysConvEndPointDetectionEndPointType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysConvEndPointDetectionEndPointType.setStatus("current")


class _EtsysConvEndPointDetectionProtocol_Type(Bits):
    """Custom type etsysConvEndPointDetectionProtocol based on Bits"""
    defaultBinValue = "11"

    namedValues = NamedValues(
        *(("tcp", 1),
          ("udp", 0))
    )

_EtsysConvEndPointDetectionProtocol_Type.__name__ = "Bits"
_EtsysConvEndPointDetectionProtocol_Object = MibTableColumn
etsysConvEndPointDetectionProtocol = _EtsysConvEndPointDetectionProtocol_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 40, 1, 3, 2, 1, 3),
    _EtsysConvEndPointDetectionProtocol_Type()
)
etsysConvEndPointDetectionProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysConvEndPointDetectionProtocol.setStatus("current")


class _EtsysConvEndPointDetectionPortLow_Type(Integer32):
    """Custom type etsysConvEndPointDetectionPortLow based on Integer32"""
    defaultValue = 4060

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_EtsysConvEndPointDetectionPortLow_Type.__name__ = "Integer32"
_EtsysConvEndPointDetectionPortLow_Object = MibTableColumn
etsysConvEndPointDetectionPortLow = _EtsysConvEndPointDetectionPortLow_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 40, 1, 3, 2, 1, 4),
    _EtsysConvEndPointDetectionPortLow_Type()
)
etsysConvEndPointDetectionPortLow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysConvEndPointDetectionPortLow.setStatus("current")


class _EtsysConvEndPointDetectionPortHigh_Type(Integer32):
    """Custom type etsysConvEndPointDetectionPortHigh based on Integer32"""
    defaultValue = 4060

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_EtsysConvEndPointDetectionPortHigh_Type.__name__ = "Integer32"
_EtsysConvEndPointDetectionPortHigh_Object = MibTableColumn
etsysConvEndPointDetectionPortHigh = _EtsysConvEndPointDetectionPortHigh_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 40, 1, 3, 2, 1, 5),
    _EtsysConvEndPointDetectionPortHigh_Type()
)
etsysConvEndPointDetectionPortHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysConvEndPointDetectionPortHigh.setStatus("current")


class _EtsysConvEndPointDetectionAddrType_Type(InetAddressType):
    """Custom type etsysConvEndPointDetectionAddrType based on InetAddressType"""


_EtsysConvEndPointDetectionAddrType_Object = MibTableColumn
etsysConvEndPointDetectionAddrType = _EtsysConvEndPointDetectionAddrType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 40, 1, 3, 2, 1, 6),
    _EtsysConvEndPointDetectionAddrType_Type()
)
etsysConvEndPointDetectionAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysConvEndPointDetectionAddrType.setStatus("current")
_EtsysConvEndPointDetectionAddr_Type = InetAddress
_EtsysConvEndPointDetectionAddr_Object = MibTableColumn
etsysConvEndPointDetectionAddr = _EtsysConvEndPointDetectionAddr_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 40, 1, 3, 2, 1, 7),
    _EtsysConvEndPointDetectionAddr_Type()
)
etsysConvEndPointDetectionAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysConvEndPointDetectionAddr.setStatus("current")


class _EtsysConvEndPointDetectionAddrMaskType_Type(InetAddressType):
    """Custom type etsysConvEndPointDetectionAddrMaskType based on InetAddressType"""


_EtsysConvEndPointDetectionAddrMaskType_Object = MibTableColumn
etsysConvEndPointDetectionAddrMaskType = _EtsysConvEndPointDetectionAddrMaskType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 40, 1, 3, 2, 1, 8),
    _EtsysConvEndPointDetectionAddrMaskType_Type()
)
etsysConvEndPointDetectionAddrMaskType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysConvEndPointDetectionAddrMaskType.setStatus("current")
_EtsysConvEndPointDetectionAddrMask_Type = InetAddress
_EtsysConvEndPointDetectionAddrMask_Object = MibTableColumn
etsysConvEndPointDetectionAddrMask = _EtsysConvEndPointDetectionAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 40, 1, 3, 2, 1, 9),
    _EtsysConvEndPointDetectionAddrMask_Type()
)
etsysConvEndPointDetectionAddrMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysConvEndPointDetectionAddrMask.setStatus("current")
_EtsysConvEndPointDetectionRowStatus_Type = RowStatus
_EtsysConvEndPointDetectionRowStatus_Object = MibTableColumn
etsysConvEndPointDetectionRowStatus = _EtsysConvEndPointDetectionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 40, 1, 3, 2, 1, 10),
    _EtsysConvEndPointDetectionRowStatus_Type()
)
etsysConvEndPointDetectionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysConvEndPointDetectionRowStatus.setStatus("current")
_EtsysCEPDetectionPortConfigTable_Object = MibTable
etsysCEPDetectionPortConfigTable = _EtsysCEPDetectionPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 40, 1, 3, 3)
)
if mibBuilder.loadTexts:
    etsysCEPDetectionPortConfigTable.setStatus("current")
_EtsysCEPDetectionPortConfigEntry_Object = MibTableRow
etsysCEPDetectionPortConfigEntry = _EtsysCEPDetectionPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 40, 1, 3, 3, 1)
)
etsysCEPDetectionPortConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    etsysCEPDetectionPortConfigEntry.setStatus("current")


class _EtsysCEPPortClearUsers_Type(TruthValue):
    """Custom type etsysCEPPortClearUsers based on TruthValue"""


_EtsysCEPPortClearUsers_Object = MibTableColumn
etsysCEPPortClearUsers = _EtsysCEPPortClearUsers_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 40, 1, 3, 3, 1, 1),
    _EtsysCEPPortClearUsers_Type()
)
etsysCEPPortClearUsers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysCEPPortClearUsers.setStatus("current")
_EtsysCEPCdpPortConfigTable_Object = MibTable
etsysCEPCdpPortConfigTable = _EtsysCEPCdpPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 40, 1, 3, 4)
)
if mibBuilder.loadTexts:
    etsysCEPCdpPortConfigTable.setStatus("current")
_EtsysCEPCdpPortConfigEntry_Object = MibTableRow
etsysCEPCdpPortConfigEntry = _EtsysCEPCdpPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 40, 1, 3, 4, 1)
)
etsysCEPCdpPortConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    etsysCEPCdpPortConfigEntry.setStatus("current")


class _EtsysCEPCiscoCDPVoicePortVlan_Type(Integer32):
    """Custom type etsysCEPCiscoCDPVoicePortVlan based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4094),
        ValueRangeConstraint(4095, 4095),
    )


_EtsysCEPCiscoCDPVoicePortVlan_Type.__name__ = "Integer32"
_EtsysCEPCiscoCDPVoicePortVlan_Object = MibTableColumn
etsysCEPCiscoCDPVoicePortVlan = _EtsysCEPCiscoCDPVoicePortVlan_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 40, 1, 3, 4, 1, 1),
    _EtsysCEPCiscoCDPVoicePortVlan_Type()
)
etsysCEPCiscoCDPVoicePortVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysCEPCiscoCDPVoicePortVlan.setStatus("current")
_EtsysConvEndPointConformance_ObjectIdentity = ObjectIdentity
etsysConvEndPointConformance = _EtsysConvEndPointConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 40, 2)
)
_EtsysConvEndPointGroups_ObjectIdentity = ObjectIdentity
etsysConvEndPointGroups = _EtsysConvEndPointGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 40, 2, 1)
)
_EtsysConvEndPointCompliances_ObjectIdentity = ObjectIdentity
etsysConvEndPointCompliances = _EtsysConvEndPointCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 40, 2, 2)
)

# Managed Objects groups

etsysConvEndPointGlobalConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 40, 2, 1, 1)
)
etsysConvEndPointGlobalConfigGroup.setObjects(
      *(("ENTERASYS-CONVERGENCE-END-POINT-MIB", "etsysConvEndPointGlobalConfigEnable"),
        ("ENTERASYS-CONVERGENCE-END-POINT-MIB", "etsysConvEndPointGlobalDefaultPolicyIndex"))
)
if mibBuilder.loadTexts:
    etsysConvEndPointGlobalConfigGroup.setStatus("current")

etsysConvEndPointConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 40, 2, 1, 2)
)
etsysConvEndPointConfigGroup.setObjects(
    ("ENTERASYS-CONVERGENCE-END-POINT-MIB", "etsysConvEndPointProtocolEnable")
)
if mibBuilder.loadTexts:
    etsysConvEndPointConfigGroup.setStatus("current")

etsysConvEndPointDetectionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 40, 2, 1, 3)
)
etsysConvEndPointDetectionGroup.setObjects(
      *(("ENTERASYS-CONVERGENCE-END-POINT-MIB", "etsysConvEndPointDetectionEndPointType"),
        ("ENTERASYS-CONVERGENCE-END-POINT-MIB", "etsysConvEndPointDetectionProtocol"),
        ("ENTERASYS-CONVERGENCE-END-POINT-MIB", "etsysConvEndPointDetectionPortLow"),
        ("ENTERASYS-CONVERGENCE-END-POINT-MIB", "etsysConvEndPointDetectionPortHigh"),
        ("ENTERASYS-CONVERGENCE-END-POINT-MIB", "etsysConvEndPointDetectionAddrType"),
        ("ENTERASYS-CONVERGENCE-END-POINT-MIB", "etsysConvEndPointDetectionAddr"),
        ("ENTERASYS-CONVERGENCE-END-POINT-MIB", "etsysConvEndPointDetectionAddrMaskType"),
        ("ENTERASYS-CONVERGENCE-END-POINT-MIB", "etsysConvEndPointDetectionAddrMask"),
        ("ENTERASYS-CONVERGENCE-END-POINT-MIB", "etsysConvEndPointDetectionRowStatus"))
)
if mibBuilder.loadTexts:
    etsysConvEndPointDetectionGroup.setStatus("deprecated")

etsysConvEndPointStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 40, 2, 1, 4)
)
etsysConvEndPointStatusGroup.setObjects(
      *(("ENTERASYS-CONVERGENCE-END-POINT-MIB", "etsysConvEndPointConnMacPortNumber"),
        ("ENTERASYS-CONVERGENCE-END-POINT-MIB", "etsysConvEndPointConnMacEndPointType"),
        ("ENTERASYS-CONVERGENCE-END-POINT-MIB", "etsysConvEndPointConnMacPolicyIndex"),
        ("ENTERASYS-CONVERGENCE-END-POINT-MIB", "etsysConvEndPointConnMacDiscoveryTime"),
        ("ENTERASYS-CONVERGENCE-END-POINT-MIB", "etsysConvEndPointConnMacFirmwareVersion"),
        ("ENTERASYS-CONVERGENCE-END-POINT-MIB", "etsysConvEndPointConnMacInetAddressType"),
        ("ENTERASYS-CONVERGENCE-END-POINT-MIB", "etsysConvEndPointConnMacInetAddress"),
        ("ENTERASYS-CONVERGENCE-END-POINT-MIB", "etsysConvEndPointConnPortMacAddress"))
)
if mibBuilder.loadTexts:
    etsysConvEndPointStatusGroup.setStatus("deprecated")

etsysConvEndPointStatusGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 40, 2, 1, 5)
)
etsysConvEndPointStatusGroup2.setObjects(
      *(("ENTERASYS-CONVERGENCE-END-POINT-MIB", "etsysConvEndPointConnPortMacAddress"),
        ("ENTERASYS-CONVERGENCE-END-POINT-MIB", "etsysCEPConnMacEndPointType"),
        ("ENTERASYS-CONVERGENCE-END-POINT-MIB", "etsysCEPConnMacPolicyIndex"),
        ("ENTERASYS-CONVERGENCE-END-POINT-MIB", "etsysCEPConnMacDiscoveryTime"),
        ("ENTERASYS-CONVERGENCE-END-POINT-MIB", "etsysCEPConnMacFirmwareVersion"),
        ("ENTERASYS-CONVERGENCE-END-POINT-MIB", "etsysCEPConnMacInetAddressType"),
        ("ENTERASYS-CONVERGENCE-END-POINT-MIB", "etsysCEPConnMacInetAddress"))
)
if mibBuilder.loadTexts:
    etsysConvEndPointStatusGroup2.setStatus("current")

etsysConvEndPointDetectionGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 40, 2, 1, 6)
)
etsysConvEndPointDetectionGroup2.setObjects(
      *(("ENTERASYS-CONVERGENCE-END-POINT-MIB", "etsysConvEndPointDetectionEndPointType"),
        ("ENTERASYS-CONVERGENCE-END-POINT-MIB", "etsysConvEndPointDetectionProtocol"),
        ("ENTERASYS-CONVERGENCE-END-POINT-MIB", "etsysConvEndPointDetectionPortLow"),
        ("ENTERASYS-CONVERGENCE-END-POINT-MIB", "etsysConvEndPointDetectionPortHigh"),
        ("ENTERASYS-CONVERGENCE-END-POINT-MIB", "etsysConvEndPointDetectionAddrType"),
        ("ENTERASYS-CONVERGENCE-END-POINT-MIB", "etsysConvEndPointDetectionAddr"),
        ("ENTERASYS-CONVERGENCE-END-POINT-MIB", "etsysConvEndPointDetectionAddrMaskType"),
        ("ENTERASYS-CONVERGENCE-END-POINT-MIB", "etsysConvEndPointDetectionAddrMask"),
        ("ENTERASYS-CONVERGENCE-END-POINT-MIB", "etsysConvEndPointDetectionRowStatus"),
        ("ENTERASYS-CONVERGENCE-END-POINT-MIB", "etsysConvEndPointDetectionMaxEntries"))
)
if mibBuilder.loadTexts:
    etsysConvEndPointDetectionGroup2.setStatus("current")

etsysConvEndPointPortConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 40, 2, 1, 7)
)
etsysConvEndPointPortConfigGroup.setObjects(
    ("ENTERASYS-CONVERGENCE-END-POINT-MIB", "etsysCEPPortClearUsers")
)
if mibBuilder.loadTexts:
    etsysConvEndPointPortConfigGroup.setStatus("current")

etsysConvEndPointCiscoVoiceVLANGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 40, 2, 1, 8)
)
etsysConvEndPointCiscoVoiceVLANGroup.setObjects(
    ("ENTERASYS-CONVERGENCE-END-POINT-MIB", "etsysCEPCiscoCDPVoicePortVlan")
)
if mibBuilder.loadTexts:
    etsysConvEndPointCiscoVoiceVLANGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

etsysConvEndPointCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 40, 2, 2, 1)
)
if mibBuilder.loadTexts:
    etsysConvEndPointCompliance.setStatus(
        "deprecated"
    )

etsysConvEndPointCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 40, 2, 2, 2)
)
if mibBuilder.loadTexts:
    etsysConvEndPointCompliance2.setStatus(
        "current"
    )

etsysConvEndPointPortConfigCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 40, 2, 2, 3)
)
if mibBuilder.loadTexts:
    etsysConvEndPointPortConfigCompliance.setStatus(
        "current"
    )

etsysConvEndPointCiscoVoiceVLANCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 40, 2, 2, 4)
)
if mibBuilder.loadTexts:
    etsysConvEndPointCiscoVoiceVLANCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ENTERASYS-CONVERGENCE-END-POINT-MIB",
    **{"ConvEndPointTypes": ConvEndPointTypes,
       "etsysConvergenceEndPointMIB": etsysConvergenceEndPointMIB,
       "etsysConvEndPointObjects": etsysConvEndPointObjects,
       "etsysConvEndPointConfig": etsysConvEndPointConfig,
       "etsysConvEndPointGlobalConfigEnable": etsysConvEndPointGlobalConfigEnable,
       "etsysConvEndPointGlobalConfigTable": etsysConvEndPointGlobalConfigTable,
       "etsysConvEndPointGlobalConfigEntry": etsysConvEndPointGlobalConfigEntry,
       "etsysConvEndPointGlobalEndPointType": etsysConvEndPointGlobalEndPointType,
       "etsysConvEndPointGlobalDefaultPolicyIndex": etsysConvEndPointGlobalDefaultPolicyIndex,
       "etsysConvEndPointProtocolConfigTable": etsysConvEndPointProtocolConfigTable,
       "etsysConvEndPointProtocolConfigEntry": etsysConvEndPointProtocolConfigEntry,
       "etsysConvEndPointProtocolEndPointType": etsysConvEndPointProtocolEndPointType,
       "etsysConvEndPointProtocolEnable": etsysConvEndPointProtocolEnable,
       "etsysConvEndPointStatus": etsysConvEndPointStatus,
       "etsysConvEndPointConnMacTable": etsysConvEndPointConnMacTable,
       "etsysConvEndPointConnMacEntry": etsysConvEndPointConnMacEntry,
       "etsysConvEndPointConnMacMacAddress": etsysConvEndPointConnMacMacAddress,
       "etsysConvEndPointConnMacPortNumber": etsysConvEndPointConnMacPortNumber,
       "etsysConvEndPointConnMacEndPointType": etsysConvEndPointConnMacEndPointType,
       "etsysConvEndPointConnMacPolicyIndex": etsysConvEndPointConnMacPolicyIndex,
       "etsysConvEndPointConnMacDiscoveryTime": etsysConvEndPointConnMacDiscoveryTime,
       "etsysConvEndPointConnMacFirmwareVersion": etsysConvEndPointConnMacFirmwareVersion,
       "etsysConvEndPointConnMacInetAddressType": etsysConvEndPointConnMacInetAddressType,
       "etsysConvEndPointConnMacInetAddress": etsysConvEndPointConnMacInetAddress,
       "etsysConvEndPointConnPortTable": etsysConvEndPointConnPortTable,
       "etsysConvEndPointConnPortEntry": etsysConvEndPointConnPortEntry,
       "etsysConvEndPointConnPortMacAddress": etsysConvEndPointConnPortMacAddress,
       "etsysCEPConnMacTable": etsysCEPConnMacTable,
       "etsysCEPConnMacEntry": etsysCEPConnMacEntry,
       "etsysCEPConnMacEndPointType": etsysCEPConnMacEndPointType,
       "etsysCEPConnMacPolicyIndex": etsysCEPConnMacPolicyIndex,
       "etsysCEPConnMacDiscoveryTime": etsysCEPConnMacDiscoveryTime,
       "etsysCEPConnMacFirmwareVersion": etsysCEPConnMacFirmwareVersion,
       "etsysCEPConnMacInetAddressType": etsysCEPConnMacInetAddressType,
       "etsysCEPConnMacInetAddress": etsysCEPConnMacInetAddress,
       "etsysConvEndPointDetection": etsysConvEndPointDetection,
       "etsysConvEndPointDetectionMaxEntries": etsysConvEndPointDetectionMaxEntries,
       "etsysConvEndPointDetectionTable": etsysConvEndPointDetectionTable,
       "etsysConvEndPointDetectionEntry": etsysConvEndPointDetectionEntry,
       "etsysConvEndPointDetectionRuleIndex": etsysConvEndPointDetectionRuleIndex,
       "etsysConvEndPointDetectionEndPointType": etsysConvEndPointDetectionEndPointType,
       "etsysConvEndPointDetectionProtocol": etsysConvEndPointDetectionProtocol,
       "etsysConvEndPointDetectionPortLow": etsysConvEndPointDetectionPortLow,
       "etsysConvEndPointDetectionPortHigh": etsysConvEndPointDetectionPortHigh,
       "etsysConvEndPointDetectionAddrType": etsysConvEndPointDetectionAddrType,
       "etsysConvEndPointDetectionAddr": etsysConvEndPointDetectionAddr,
       "etsysConvEndPointDetectionAddrMaskType": etsysConvEndPointDetectionAddrMaskType,
       "etsysConvEndPointDetectionAddrMask": etsysConvEndPointDetectionAddrMask,
       "etsysConvEndPointDetectionRowStatus": etsysConvEndPointDetectionRowStatus,
       "etsysCEPDetectionPortConfigTable": etsysCEPDetectionPortConfigTable,
       "etsysCEPDetectionPortConfigEntry": etsysCEPDetectionPortConfigEntry,
       "etsysCEPPortClearUsers": etsysCEPPortClearUsers,
       "etsysCEPCdpPortConfigTable": etsysCEPCdpPortConfigTable,
       "etsysCEPCdpPortConfigEntry": etsysCEPCdpPortConfigEntry,
       "etsysCEPCiscoCDPVoicePortVlan": etsysCEPCiscoCDPVoicePortVlan,
       "etsysConvEndPointConformance": etsysConvEndPointConformance,
       "etsysConvEndPointGroups": etsysConvEndPointGroups,
       "etsysConvEndPointGlobalConfigGroup": etsysConvEndPointGlobalConfigGroup,
       "etsysConvEndPointConfigGroup": etsysConvEndPointConfigGroup,
       "etsysConvEndPointDetectionGroup": etsysConvEndPointDetectionGroup,
       "etsysConvEndPointStatusGroup": etsysConvEndPointStatusGroup,
       "etsysConvEndPointStatusGroup2": etsysConvEndPointStatusGroup2,
       "etsysConvEndPointDetectionGroup2": etsysConvEndPointDetectionGroup2,
       "etsysConvEndPointPortConfigGroup": etsysConvEndPointPortConfigGroup,
       "etsysConvEndPointCiscoVoiceVLANGroup": etsysConvEndPointCiscoVoiceVLANGroup,
       "etsysConvEndPointCompliances": etsysConvEndPointCompliances,
       "etsysConvEndPointCompliance": etsysConvEndPointCompliance,
       "etsysConvEndPointCompliance2": etsysConvEndPointCompliance2,
       "etsysConvEndPointPortConfigCompliance": etsysConvEndPointPortConfigCompliance,
       "etsysConvEndPointCiscoVoiceVLANCompliance": etsysConvEndPointCiscoVoiceVLANCompliance}
)
